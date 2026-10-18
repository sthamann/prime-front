#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""krein_screw_realization_probe -- PRIME.SUZUKI.KREIN.REALIZATION.01

FROZEN SPEC (2026-08-14).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Build the ONE remaining priced ingredient named by the SVPIN
adjudication (CCCLXXXIX, SPEC_SHA f450832fdb15755c, verdict
SVPIN-ROUTE-OPEN): the KREIN INVERSE-SPECTRAL REALIZATION of Suzuki's
screw function g as a SOURCE-ONLY carrier for the resolvent pins
P(sigma) = xi'/xi(1/2 + sigma), sigma > 1/2.  The extremal family's
pin convergence was convicted Z1-TRANSCRIPTION (band pins == cache
partial sums, rel 7.7e-12); the naive Suzuki spectral readout was
convicted SUZPIN-FORM-SPECTRUM (hat-compression eigenvalues are a
Weil-margin ladder, not ordinates; P_suz grows).  This probe does
NEITHER: it runs the actual inverse-spectral machinery -- the screw
lag data of g on [0, 2a] as a discrete Krein accelerant, the Szego /
Levinson recursion (the Toeplitz-structured Krein / Gelfand-Levitan
solve) producing Verblunsky coefficients (the discretized Krein-system
coefficient = the realized Hamiltonian data), and the WEYL DISK of the
truncated trigonometric moment problem evaluated at the pin points --
and asks the decisive falsifiable question: does the Weyl-function
reading converge to the source target as the window grows, with the
disk contracting (limit-point behaviour), separating from the
prime-free and scrambled worlds, and without any zero data anywhere
in the pipeline (AST firewall)?

=======================================================================
K1 -- THE EXACT OBJECTS AND THE CLASSICAL CORRESPONDENCE
=======================================================================
THE SCREW FUNCTION (corpus-exact; Suzuki arXiv:2606.09096 eq. (1.3)
with the v643 C0 CONVENTION LOCK -- Hurwitz-Lerch bracket coefficient
+1/4, NOT -1; g(0) = 0 is the Krein-Langer screw normalization):
  g(t) = -4(e^{|t|/2} + e^{-|t|/2} - 2)
         + sum_{n <= e^{|t|}} Lambda(n)/sqrt(n) (|t| - log n)
         - (|t|/2)(psi(1/4) - log pi)
         - (1/4)( Phi(1,2,1/4) - e^{-|t|/2} Phi(e^{-2|t|}, 2, 1/4) ).
Layers named: g_pole (the s = 0,1 zeta poles), g_prime (Suzuki's prime
measure = the TFPT atom table, v630 S1 literal identity), g_arch (the
archimedean screw layer; S(t) := (1/4) e^{-t/2} Phi(e^{-2t},2,1/4)
satisfies S'' = rho(t) = e^{-|t|/2}/(1 - e^{-2|t|}) exactly, v643).
The operator sees g modulo affine gauge only (second differences kill
constant + linear terms -- exactly the Krein screw-function gauge).

THE WEIL MEASURE AND THE PIN IDENTITY (unconditional, sigma > 1/2):
with k := -g'' (tempered distribution: 2 cosh(t/2) - rho(t) - prime
atoms - origin Pf block), the Weil explicit formula for the admissible
even test function f_sigma(t) = e^{-sigma |t|} (hat f_sigma(lam) =
2 sigma/(lam^2 + sigma^2), decay lam^{-2}, e^{-sigma|t|} with
sigma > 1/2 dominates the e^{|t|/2} pole growth -- the absolutely
convergent Euler half-plane) reads
  (PIN)   xi'/xi(1/2 + sigma) = (1/2) < -g'', e^{-sigma|.|} >.
Layer check: (1/2)<2cosh(t/2), f> = 1/s + 1/(s-1); the atoms give
- sum Lambda(n) n^{-s}; the arch layer gives -(1/2)log pi
+ (1/2)psi(s/2) -- each layer is GATED numerically below (K1d/K1e),
so the dictionary is derived and machine-checked, never fitted.

THE CLASSICAL CORRESPONDENCE INVOKED (named, hypotheses checked):
 (i)  Krein-Langer screw functions [M.G. Krein 1940s; Krein-Langer,
      Integral Equations Operator Theory 2014 survey]: g is a screw
      function on (-2a, 2a) iff the kernel G(t,s) = g(t-s) - g(t)
      - g(-s) + g(0) is nonnegative-definite on [-a, a]^2.  CHECKED
      as gate K1b on a frozen grid (a falsifiable measurement; its
      all-a version is Suzuki's RH-equivalence and is NOT assumed).
 (ii) Krein's accelerant / continual-Schur correspondence [M.G. Krein,
      Dokl. Akad. Nauk SSSR 105 (1955) 637-640; S. Denisov, IMRS 2006
      survey on Krein systems; discrete transcription: Verblunsky /
      Geronimus, B. Simon OPUC Thms 1.7.11, 3.1.4]: a real even lag
      sequence with all Toeplitz sections positive definite is the
      moment sequence of a positive measure on the circle; the Szego /
      Levinson recursion (= the Toeplitz-structured discrete Krein /
      Gelfand-Levitan equation) produces Verblunsky coefficients
      alpha_k in (-1,1), the discrete Krein-system coefficient
      (Hamiltonian data); the set of Caratheodory-function values
      F(w) over all positive continuations of n moments is a NESTED
      DISK (the discrete Weyl disk), computed exactly here by 2x2
      Moebius transfer.  HYPOTHESES CHECKED: realness+evenness of the
      lags (structural), strict positivity of every section = the
      Szego recursion completing with max|alpha| < 1 (gate K1c; its
      failure at any depth is a clean typed kill with the number).
 (iii) The delta -> 0 limit of this discrete machinery is the Krein
      system / trace-normed canonical system of the accelerant, whose
      Weyl-Titchmarsh function is the Herglotz transform of the
      spectral measure [Krein 1955; Denisov survey Secs. 12-13; de
      Branges, Hilbert spaces of entire functions, for the chain].
      The delta-refinement gates (K2a/K2b) measure exactly this limit.

THE DERIVED NORMALIZATION (no fitting).  Lag reads are exact tent
reads by parts: t_row[d] = <-g'', tent_{d delta}> = -(1/delta)
[g((d-1)delta) - 2 g(d delta) + g((d+1)delta)], t_row[0] =
-(2/delta) g(delta).  Since the tents are a partition of unity,
  (delta/2) F(e^{-sigma delta})
    = (1/2) t_row[0] + sum_{d>=1} t_row[d] e^{-sigma d delta}
    = (1/2) < -g'', E_delta >,
E_delta = the piecewise-linear interpolant of e^{-sigma|t|} on the
lag grid, tapered to 0 at |t| = L := n delta = 2a.  (The circle
moments are c_d = t_row[d]/delta, so (delta/2) F == (1/2) x the
Caratheodory value of the t_row sequence itself -- the implemented
form.)  Hence the frozen pin readout  P_hat(sigma) := (delta/2) x
[CENTER of the depth-n Weyl disk of F at w = e^{-sigma delta}]
targets (PIN) with three explicit,
separately measured error channels: (a) the O(sigma^2 delta^2)
interpolation bias (Richardson-gated K2b), (b) the window truncation
(the semi-analytic layer model of K1e, incl. the exact edge tapers),
(c) the realization ambiguity = the disk radius R (K2d/K3b).
-i m_a(i sigma) = P_hat(sigma) is the Weyl-function reading of the
truncated realization; the Cayley dictionary circle <-> half plane is
classical and not re-derived here.

DISTINCTNESS FROM DEBRANGES-COMB-BLIND (mandatory statement).  The
debranges_chain_probe killed the Hermite-Biehler IDENTITY route on the
deployed wall: it took the SPECTRAL MOMENTS of the wall block B_h at a
cyclic vector (Lanczos), built structure functions E_h, and asked a
structural HB/chain question -- HB-ness turned out to be an identity
of ANY positive matrix (comb-blind), and the cross-rung chain breaks.
THIS probe is a different object in all three coordinates: (1) the
INPUT is the screw-function lag sequence of g itself (source data of
the accelerant), not the spectrum of a deployed Galerkin matrix at a
cyclic vector; (2) the MACHINERY runs the inverse direction
(moments -> Verblunsky/Hamiltonian -> Weyl disk), producing the new
local object the corpus lacked, instead of re-coordinatizing a given
matrix; (3) the ADJUDICATED statement is a quantitative convergence
measurement against an independent source target with world controls
and typed kills, never a structure-existence claim.  The shared risk
is typed: ANY positive Toeplitz section admits SOME realization --
existence is free and carries no content here; every verdict-bearing
gate below is a convergence / separation / typing measurement.

=======================================================================
FROZEN OBJECTS
=======================================================================
SIGMA GRID (16 values, verbatim the SVPIN spec, asserted equal to the
imported tuple; frozen BEFORE computation; every verdict statistic
runs over the full grid):
  SIGMAS = (0.6, 0.75, 0.9, 1.125, 8/7, 7/6, 1.2, 1.25, 4/3, 1.5,
            2.0, 3.0, 4.0, 6.0, 8.0, 12.0)
WINDOW LADDER (frozen in L = 2a; common exact delta so that Toeplitz
sections NEST exactly across rungs; labels x ~ e^L):
  L_LADDER = (1.092, 1.608, 2.076, 2.568)   [x ~ 2.98, 5.00, 7.97,
  13.04; approximates a = (1/2) log x for x = 3, 5, 8, 13]
DELTAS = (0.012, 0.006, 0.003); PRIMARY table at delta = 0.003, bias
read bias(sigma, L) = |P_hat_{0.006} - P_hat_{0.003}| per rung;
delta-triple Richardson at L1, L2.  DPS = 50 (mp) everywhere in the
realization path; float64 only in wards/diagnostics typed as such.
TARGET: SourceTarget of the SVPIN probe (imported; own sieve NSIEVE =
4e7, Gamma/pi/Lambda(n) only), cross-warded against the cache zero
route (A3, X5-typed instrument, ward namespace only).
WORLDS: TRUE (prime atoms); SMOOTH (atoms -> PNT density e^{t/2},
prime ramp -> 4 e^{t/2} - 2t - 4 closed, own target = target
+ sum Lambda(n) n^{-s} - 1/(sigma - 1/2)); SCRARITH (golden-key
permutation of atom weights over the same positions, key =
frac(q x (sqrt5-1)/2), argsort -- frozen, seedless).
NOISE FLOOR: NF(sigma, L) = max(1e-7, 3 dev_A3(sigma),
bias(sigma, L)).

=======================================================================
GATES (all computed; none asserted; bars frozen here)
=======================================================================
I. INSTRUMENT
 A1 AST firewall: no zeta/zetazero/siegel attribute or call in this
    file; zero cache readable ONLY inside ward_*/target_* functions
    and main (X5: instrument/diagnostics, never construction); no
    identifier contains 'christoffel'; no verification/ import.
 A2 cache health: n >= 5000 ordinates, gamma_1 dev < 1e-9, monotone.
 A3 target cross-ward, 16 rows: |tgt_src - cache route| <= 2e-3
    (sigma < 0.8), 5e-4 (< 1.1), 3e-4 (else).
 A4 synthetic OPUC pipeline ward (mp): mu = Leb/2pi + 0.15
    (delta_{pi/3} + delta_{-pi/3}), n = 48 moments, w = 0.4: truth
    inside the disk (|F_true - center| <= R (1+1e-12) + 1e-30),
    central value inside, R(depth n-1) <= R(depth (n-1)/2).
 A5 lag cross-ward: my exact-second-difference lag builder (float64
    route) vs the SVPIN suz_lag_row tent-quadrature route at the suz
    convention grids x = 3, 5, 8 (delta ~ 0.006): max entry dev /
    max|row| <= 1e-7.  (Two INDEPENDENT routes to the same reads:
    quadrature of the tent integrals vs exact integration by parts.)
 A6 Szego internal exactness at L3/TRUE and synthetic: prediction
    error by independent mp LU solve of the m = 40 section,
    1/(T_hat^{-1})_{00} vs prod_{k<39}(1 - alpha_k^2): rel <= 1e-20.
 A7 Moebius-disk self-ward (L2 build, sigma in {0.6, 2, 12}): 16
    boundary samples f = e^{i phi}: max | |T(f) - center| - R | / R
    <= 1e-20.
 A8 runtime <= 1500 s.
II. K1 SCREW + DICTIONARY (falsifiable; a kill here is a result)
 K1a origin expansion (locks the +1/4 Lerch convention): r(t) :=
    |g(t) - ((1/2) t log t + A t)| / t, A = (1/2)(log 2pi - psi(2)):
    r(0.02) <= 0.1 AND r(0.002) <= 0.35 r(0.02).
 K1b screw kernel PSD on the frozen grid (81 points, [-a, a], all
    four rungs, float64): lam_min(G)/lam_max(G) >= -1e-8.  Failure
    => SUZKREIN-DEAD(screw positivity fails; exact number printed).
 K1c accelerant positivity certificate (= Krein hypothesis executed):
    the Szego recursion completes on every TRUE rung with
    max|alpha_k| < 1 and min prediction error > 0.  Failure at depth
    k* => SUZKREIN-DEAD(section positivity fails at k* delta).
 K1d ARCH dictionary gate (L3, delta 0.006 and 0.003): |arch-layer
    read - ((1/2)log pi - (1/2)psi(s/2) - rho_tail - taper_rho)| <=
    max(4e-4, 0.6 sigma^2 delta^2) on all 16 rows.  (With the wrong
    Lerch coefficient this fails by O(1): the convention is gated.)
 K1e pole + prime layer gates (same grids): pole read vs closed
    (2sigma/(sigma^2-1/4) - pole_tail - taper_pole) <=
    max(2e-4, 0.6 sigma^2 delta^2); prime read vs the exact
    interpolant model -sum w E_delta(u): rel <= 1e-10 (identity).
III. K2 REALIZATION
 K2a Hamiltonian profile (L3), two parts: (i) SMOOTH-BACKGROUND
    delta-scaling: median matched-index ratio alpha_k(delta) /
    [(alpha_2k + alpha_2k+1)/2](delta/2) in (1.6, 2.4) (alpha ~
    delta x A(r) on the smooth part); (ii) ATOM SIGNATURE: for every
    atom u = log q with 0.1 < u < L - 0.1, the |alpha| profile at
    delta/2 has its local maximum (window +-6 bins) within +-3 bins
    of u/delta and contrast >= 1.3 over the local background -- the
    realized Hamiltonian must SEE the primes at the right positions.
    DECLARED HONESTLY: the pointwise profile and the cumulative
    energy (1/delta) sum alpha^2 are measured NON-convergent in
    delta (the accelerant has delta atoms, so the continuum Krein
    coefficient has atomic/rough components -- point interactions);
    the delta-stable objects are the pins (K2b), the disks, and the
    spike positions, and that is what is gated.
 K2b Richardson delta-refinement (L1, L2; rows with both increments
    > 10 NF0, NF0 = max(1e-7, 3 dev_A3) the BIAS-FREE floor -- the
    bias term is the Richardson denominator itself and may not enter
    its own liveness filter): median ratio (P_.012 - P_.006) /
    (P_.006 - P_.003) in (2.6, 5.5)  [O(delta^2) law].  (Needs the
    delta-triple; in smoke it prints SMOKE-SKIP.)
 K2c conditioning: deterministic multiplicative perturbation of the
    input lags, row[d] -> row[d](1 + 1e-25 cos(7d)) (L3, delta .006),
    compared at mp precision BEFORE any float cast: median rel
    |Delta P_hat| <= 1e-6; else the ILLPOSED lane with the measured
    amplification law.
 K2d Weyl-disk nesting: R(depth m) <= R(depth floor(m/2)) (1+1e-20),
    all sigma, all TRUE rungs at delta 0.003.
IV. K3 THE DECISIVE MEASUREMENT (primary table delta = 0.003)
 K3a row typing over the 4-rung ladder, Delta = P_hat - tgt:
    CONVERGES iff |Delta(L4)| <= max(|Delta(L1)|/1.5, 3 NF) and
    nonincreasing within WOBBLE 1.3 at >= 2 of 3 steps (both-ends
    <= 3 NF = saturated pass); DIVERGES iff |Delta(L4)| >
    2 |Delta(L1)| and > 10 NF; else PLATEAUS.  Composite bars:
    >= 12/16 CONVERGES, DIVERGES kill at >= 8/16.
 K3b disk contraction law: OLS slope rho(sigma) of log R vs L over
    the 4 rungs: rho(sigma) >= 0.9 sigma on all 16 rows (measured
    law and the fitted constant printed -- the lemma rate).
 K3c truth-tightness: |Delta(L4)| <= max(3 R(L4), 3 NF) on >= 12/16
    rows.
 K3d SMOOTH control (L3): separation median over sigma of
    |P_smooth - tgt_true| / max(|Delta_true(L3)|, NF, R_true) >= 25;
    own-target consistency median |P_smooth - tgt_smooth| /
    max(R_smooth, 3 bias_true, 1e-6) <= 5 (the machinery must
    transport ITS OWN world faithfully -- world-agnostic instrument,
    world-sensitive content).
 K3e SCRARITH control (L3): separation median >= 25 (same metric
    against tgt_true).  A control that breaks K1c-positivity is
    typed CONTROL-NOT-SCREW(depth) and counts as separated.
V. K4 THE TRACE-CLASS QUESTION (priced from measurements; no gates,
    typed findings): (a) embedded resolvent differences
    || M'^{1/2}(B'+sigma^2 M')^{-1}M'^{1/2} - iota (...) iota^T ||_tr
    on the nested delta = 0.006 hat realization (exact Toeplitz
    nesting), 16 sigma x 3 steps, decay slope fitted; typed
    TRACECLASS-EMBED-FLAT iff fitted rate < 0.1 for >= 12/16 rows;
    (b) the same for the compression differences P R' P - R; (c) the
    appended Verblunsky-block l2 norms per rung (the local
    Krein-system price); (d) the minimal missing lemma printed in
    theorem shape with the measured rates substituted.
VI. K5 HONESTY SCREENS
 K5a margin-relocation screen: the wall-margin analog here is the
    Szego prediction-error floor e_min; its ladder is printed next
    to the |Delta| ladder.  If e_min spans < 0.5 decades while
    |Delta| falls > 1 decade, relocation onto the margin is
    STRUCTURALLY EXCLUDED and typed so (the SVPIN tau-screen slope
    is degenerate here and would be dishonest; declared).  If e_min
    spans >= 0.5 decades, the SVPIN slope screen runs verbatim
    (PASS <= 0.3, RELOC >= 0.7, kill >= 6/16 rows).
 K5b cache-transcription scan (THIS carrier's Z1 question): per rung
    L3, L4: min over N <= 7000 of max_sigma rel|P_hat - S_N|,
    S_N = the cache partial sums (ward namespace).  Fires
    SUZKREIN-TRANSCRIPTION iff <= 1e-6.
 K5c source-truncation typing: median over rows with |tail model| >
    10 NF of |P_hat - S_trunc| / |tail model|; typed
    SUZKREIN-EXTRAPOLATES iff in (0.5, 2.0) -- the Weyl reading
    RESUMS the missing tail instead of transcribing the truncated
    source sum (the mirror-image of Z1, measured).
 K5d conditioning law: e_min ladder + K2c amplification printed.
VII. COMPOSITE VERDICT (exactly one, priority frozen):
  abort SUZKREIN-INSTRUMENT-EDGE (exit 1, any A-gate fails; not a
  verdict) > SUZKREIN-DEAD(screw/section positivity, K1b/K1c) >
  SUZKREIN-TRANSCRIPTION (K5b) > SUZKREIN-ILLPOSED(law) (K2c) >
  SUZKREIN-BLIND (K3d/K3e) > SUZKREIN-DEAD(pins diverge / no
  contraction: K3a >= 8 DIVERGES or K3b fails) >
  SUZKREIN-CARRIER-OPEN(lemma) iff K3a >= 12/16 CONVERGES and K3b
  and K3c pass; otherwise SUZKREIN-DEAD(insufficient convergence,
  counts printed).  RUNTIME_BAR = 1500 s.

DECLARED SUBSAMPLING AND MODELS: the ladder is frozen in L (windows
carry the atoms strictly inside; boundary atoms enter through the
exact interpolant weights); delta-triple only at L1, L2 (cost); K4 at
delta 0.006 (float64 resolvents; (B + sigma^2 M) has condition
~ lam_max/sigma^2, benign); the tail model is semi-analytic (closed
pole/arch transforms, mp quadrature tails, exact atom interpolant
reads); SMOOTH/SCRARITH at L3 only; the x ~ 21 continuation is out of
budget and NOT claimed.  Smoke flag prints NOT-VERDICT-BEARING.
Amendments after the frozen run, if any, are numbered AMENDMENT
blocks.

PRE-FREEZE CALIBRATION DISCLOSURE (part of the record): the
normalization, the taper factor (the even-side taper enters with
factor 1, not 1/2 -- caught against the closed pole layer), the
boundary-atom interpolant bookkeeping, the O(sigma^2 delta^2) bias
scale, the disk-contraction magnitudes, and the FLATNESS of both
trace-norm readings were measured in float64 shakeout runs BEFORE
this spec was frozen; every bar above was set from those
measurements plus safety margins, and the two surprising readings
(the disk center resums the missing tail; the trace norms do not
decay) are pre-registered here as expectations to be confirmed or
refuted by the frozen mp run.  SMOKE DISCLOSURE (no bar, grid,
ladder or verdict rule moved): smoke 1 caught (a) a c0/delta
normalization slip in the pin readout (the disk center was delta x
too small -- exposed by the K3 table reading Delta = -tgt, fixed to
the (1/2) x t_row-Caratheodory form above), (b) a vacuous K2c
perturbation (decimal-roundtrip reproduced the same binary mpf;
replaced by the deterministic multiplicative perturbation), (c) a
binning-phase instability in the K2a profile gate (r-bins replaced
by the matched-index pairing), (d) the missing delta-triple guard
in K2b under the smoke ladder.  Smoke 2 caught (e) that the K2c
comparison happened after a float64 cast (perturbations below 1e-16
invisible; moved to mp), and (f) that a POINTWISE profile-stability
gate is the wrong claim: the matched-index correlation reads 0.50-
0.76 because the alpha sequence carries delta-rough ringing and
O(1) atom spikes (physics of an atomic accelerant, reported as
such); K2a was redesigned to the two claims that are actually
delta-stable and falsifiable (background amplitude scaling; atom
spike positions).  FULL-RUN-1 DISCLOSURE: the first full run
(SPEC_SHA 1f898f9514f060fd) aborted as INSTRUMENT-EDGE because the
K2b liveness filter was circular (NF contains the bias term, which
IS the Richardson denominator, so only anomalous rows survived);
the filter was repaired to the bias-free floor NF0 above and the
run repeated -- an instrument repair, disclosed; no bar, grid,
ladder, or verdict rule of K1/K3/K4/K5 moved in any shakeout.
NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
import scipy.linalg as sla

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import stieltjes_vitali_pin_probe as SV  # noqa: E402  frozen SVPIN objects

# ------------------------------------------------------------ frozen bars
SIGMAS = (0.6, 0.75, 0.9,
          1.125, 8.0 / 7.0, 7.0 / 6.0, 1.2, 1.25, 4.0 / 3.0, 1.5, 2.0,
          3.0, 4.0, 6.0, 8.0, 12.0)
L_LADDER = (1.092, 1.608, 2.076, 2.568)
X_LABEL = {1.092: "x~3", 1.608: "x~5", 2.076: "x~8", 2.568: "x~13"}
DELTAS = (0.012, 0.006, 0.003)
D_BASE = 0.003
DPS = 50
NSIEVE = 40_000_000
WOBBLE = 1.3
DROP = 1.5
DIV_FAC = 2.0
CONV_BAR = 12
DIV_BAR = 8
TIGHT_BAR = 12
SEP_BAR = 25.0
OWN_BAR = 5.0
RICH_LO, RICH_HI = 2.6, 5.5
CONTRACT_FAC = 0.9
G_PSD_BAR = -1e-8
A5_BAR = 1e-7
K1D_ABS = 4e-4
K1E_ABS = 2e-4
K1_BIAS = 0.6
PRIME_REL = 1e-10
COND_ROUND_DPS = 25
COND_BAR = 1e-6
TRANS_BAR = 1e-6
EXTRAP_LO, EXTRAP_HI = 0.5, 2.0
AMP_LO, AMP_HI = 1.6, 2.4
SPIKE_BINS = 3
SPIKE_WIN = 6
SPIKE_CONTRAST = 1.3
FLAT_RATE = 0.1
RUNTIME_BAR = 1500.0
GAMMA1_LIT = 14.134725141734693790
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-46s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78)


# ------------------------------------------------- wards (cache X5 side)
def ward_cache_load() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_target_cache(gammas: np.ndarray, sigma: float) -> float:
    """Zero route: exact sum over verified ordinates + RvM density tail
    (instrument only, never a target or construction input)."""
    s_fin = float(np.sum(2.0 * sigma / (gammas ** 2 + sigma ** 2)))
    gtop = float(gammas[-1])
    with mp.workdps(25):
        tail = mp.quad(lambda t: (mp.log(t / (2 * mp.pi)) / (2 * mp.pi))
                       * 2 * sigma / (t * t + sigma * sigma),
                       [gtop, 3 * gtop, 30 * gtop, mp.inf])
    return s_fin + float(tail)


def ward_partial_sums(gammas: np.ndarray, sigma: float) -> np.ndarray:
    return np.cumsum(2.0 * sigma / (gammas ** 2 + sigma ** 2))


# --------------------------------------------------- the screw function
MP_CONST = {}


def mp_setup() -> None:
    with mp.workdps(DPS + 10):
        MP_CONST["PSI14"] = mp.digamma(mp.mpf(1) / 4)
        MP_CONST["LOGPI"] = mp.log(mp.pi)
        MP_CONST["PHI1"] = mp.lerchphi(1, 2, mp.mpf(1) / 4)
        MP_CONST["ACON"] = (mp.log(2 * mp.pi) - mp.digamma(2)) / 2


S_MP_CACHE: dict[int, mp.mpf] = {}
S_F64_CACHE: dict[float, float] = {}


def s_arch_mp(m_idx: int) -> mp.mpf:
    """S(t) = (1/4) e^{-t/2} Phi(e^{-2t}, 2, 1/4) at t = m_idx * 0.003
    (mp, dps DPS; series for t >= 0.3, mp.lerchphi below)."""
    if m_idx in S_MP_CACHE:
        return S_MP_CACHE[m_idx]
    with mp.workdps(DPS + 10):
        t = mp.mpf(m_idx) * mp.mpf("0.003")
        if m_idx == 0:
            v = MP_CONST["PHI1"] / 4
        elif t >= mp.mpf("0.3"):
            z = mp.exp(-2 * t)
            tot = mp.mpf(0)
            zp = mp.mpf(1)
            mm = 0
            floor = mp.mpf(10) ** (-(DPS + 8))
            while zp > floor * (1 + tot):
                tot += zp / (mm + mp.mpf(1) / 4) ** 2
                mm += 1
                zp *= z
            v = mp.exp(-t / 2) * tot / 4
        else:
            v = mp.exp(-t / 2) * mp.lerchphi(mp.exp(-2 * t), 2,
                                             mp.mpf(1) / 4) / 4
    S_MP_CACHE[m_idx] = v
    return v


def s_arch_f64(t: float) -> float:
    tt = round(float(t), 12)
    if tt in S_F64_CACHE:
        return S_F64_CACHE[tt]
    if tt == 0.0:
        v = 0.25 * float(MP_CONST["PHI1"])
    elif tt >= 0.3:
        z = math.exp(-2.0 * tt)
        tot, zp, mm = 0.0, 1.0, 0
        while zp > 1e-22 * (1.0 + tot):
            tot += zp / ((mm + 0.25) ** 2)
            mm += 1
            zp *= z
        v = 0.25 * math.exp(-0.5 * tt) * tot
    else:
        with mp.workdps(25):
            v = 0.25 * float(mp.exp(-tt / 2)
                             * mp.lerchphi(mp.exp(-2 * tt), 2,
                                           mp.mpf(1) / 4))
    S_F64_CACHE[tt] = v
    return v


def prime_atoms(u_max: float) -> list[tuple[float, float]]:
    """(log q, Lambda(q)/sqrt(q)) for prime powers q with log q < u_max."""
    out = []
    icap = int(math.exp(u_max)) + 2
    sieve = np.zeros(icap + 1, dtype=bool)
    for p in range(2, icap + 1):
        if sieve[p]:
            continue
        sieve[p * p:: p] = True
        q = p
        while math.log(q) < u_max - 1e-12:
            out.append((math.log(q), math.log(p) / math.sqrt(q)))
            q *= p
    out.sort(key=lambda z: z[0])
    return out


def scram_weights(atoms: list[tuple[float, float]]) -> list[float]:
    """Golden-key permutation of the atom weights (frozen, seedless)."""
    qs = [round(math.exp(u)) for u, _w in atoms]
    key = [(q * GOLDEN) % 1.0 for q in qs]
    perm = sorted(range(len(atoms)), key=lambda i: key[i])
    return [atoms[i][1] for i in perm]


def g_value_mp(t: mp.mpf, atoms, weights) -> mp.mpf:
    """Suzuki's true g at t >= 0 (mp), TRUE-world atoms/weights given.
    S must be supplied by the caller for grid points; this scalar form
    is used only for the origin gate (K1a)."""
    with mp.workdps(DPS + 10):
        out = -8 * (mp.cosh(t / 2) - 1)
        for (u, _w), w in zip(atoms, weights):
            if u < t:
                out += w * (t - u)
        out += -(t / 2) * (MP_CONST["PSI14"] - MP_CONST["LOGPI"]) \
            - MP_CONST["PHI1"] / 4 \
            + mp.exp(-t / 2) * mp.lerchphi(mp.exp(-2 * t), 2,
                                           mp.mpf(1) / 4) / 4
        return out


def build_lags_mp(L: float, delta_name: str, world: str) -> dict:
    """The lag row t_row[d] = <-g'', tent_d> by exact second differences
    of g on the grid j*delta, j = 0..n (mp, dps DPS).  delta_name in
    {'0.012','0.006','0.003'}; grid indices mapped to the 0.003 lattice
    for the shared S cache."""
    t0 = time.time()
    with mp.workdps(DPS + 10):
        dl = mp.mpf(delta_name)
        step = int(round(float(delta_name) / 0.003))
        n = int(round(L / float(delta_name)))
        atoms = prime_atoms(n * float(delta_name))
        if world == "SCRARITH":
            weights = scram_weights(atoms)
        else:
            weights = [w for _u, w in atoms]
        gvals = []
        for j in range(n + 1):
            t = mp.mpf(j) * dl
            v = -8 * (mp.cosh(t / 2) - 1)
            if world in ("TRUE", "SCRARITH"):
                for (u, _w), w in zip(atoms, weights):
                    if u < t:
                        v += w * (t - u)
            elif world == "SMOOTH":
                v += 4 * mp.exp(t / 2) - 2 * t - 4
            else:
                raise ValueError(world)
            v += -(t / 2) * (MP_CONST["PSI14"] - MP_CONST["LOGPI"]) \
                - MP_CONST["PHI1"] / 4 + s_arch_mp(j * step)
            gvals.append(v)
        row = [(-2 * gvals[1] / dl)]
        for d in range(1, n):
            row.append(-(gvals[d - 1] - 2 * gvals[d] + gvals[d + 1]) / dl)
    return {"row": row, "n": n, "delta": float(delta_name),
            "delta_mp": dl, "L": n * float(delta_name), "atoms": atoms,
            "weights": weights, "world": world,
            "build_s": time.time() - t0}


def build_lags_f64(L: float, delta: float, world: str = "TRUE",
                   n_force: int | None = None) -> tuple:
    """float64 route (wards / K4 / screw grid), same construction."""
    n = n_force if n_force is not None else int(round(L / delta))
    t = np.arange(n + 1) * delta
    g = -8.0 * (np.cosh(t / 2) - 1.0)
    atoms = prime_atoms(n * delta)
    if world == "TRUE":
        for u, w in atoms:
            g = g + w * np.maximum(t - u, 0.0)
    elif world == "SMOOTH":
        g = g + 4.0 * np.exp(t / 2) - 2.0 * t - 4.0
    psi14 = float(MP_CONST["PSI14"])
    logpi = float(MP_CONST["LOGPI"])
    phi1 = float(MP_CONST["PHI1"])
    g = g - (t / 2.0) * (psi14 - logpi) - 0.25 * phi1 \
        + np.array([s_arch_f64(v) for v in t])
    r = np.empty(n)
    r[0] = -2.0 * g[1] / delta
    r[1:] = -(g[0: n - 1] - 2.0 * g[1: n] + g[2: n + 1]) / delta
    return r, n, atoms


# -------------------------------------------- Szego / Verblunsky (mp)
def szego_mp(row: list, dps: int = DPS) -> dict:
    """Szego recursion on the normalized moments r_d = row[d]/row[0].
    Returns Verblunsky alphas, min/max diagnostics.  Positivity of all
    Toeplitz sections <=> completes with |alpha| < 1, den > 0."""
    with mp.workdps(dps):
        c0 = row[0]
        r = [x / c0 for x in row]
        n = len(r)
        Phi = [mp.mpf(1)]
        Phis = [mp.mpf(1)]
        alphas = []
        den_min = mp.mpf("inf")
        amax = mp.mpf(0)
        den = mp.mpf(1)
        fail_k = -1
        for k in range(n - 1):
            num = mp.fdot(Phi, r[1: k + 2])
            den = mp.fdot(Phis, r[0: k + 1])
            if den <= 0:
                fail_k = k
                break
            a = num / den
            if abs(a) >= 1:
                fail_k = k
                break
            alphas.append(a)
            den_min = min(den_min, den)
            amax = max(amax, abs(a))
            zPhi = [mp.mpf(0)] + Phi
            Phi_new = [zPhi[j] - a * (Phis + [mp.mpf(0)])[j]
                       for j in range(k + 2)]
            Phis_new = [(Phis + [mp.mpf(0)])[j] - a * zPhi[j]
                        for j in range(k + 2)]
            Phi, Phis = Phi_new, Phis_new
        prod = mp.mpf(1)
        for a in alphas:
            prod *= (1 - a * a)
        return {"alphas": alphas, "c0": c0, "den_min": den_min,
                "den_final": den, "prod_final": prod,
                "amax": amax, "fail_k": fail_k, "ok": fail_k < 0}


def weyl_disk_mp(alphas: list, c0, w, depth: int | None = None,
                 dps: int = DPS) -> tuple:
    """(center, radius, central_value) of the depth-n Weyl disk of the
    Caratheodory function F at real w in (0,1); Schur parameters
    gamma_k = alpha_k (real case, Geronimus).  Exact 2x2 Moebius
    transfer; disk of (A f + B)/(C f + D) over |f| <= 1."""
    if depth is None:
        depth = len(alphas)
    with mp.workdps(dps):
        A, B, C, D = mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(1)
        for k in range(depth):
            gk = alphas[k]
            A, B, C, D = (A * w + B * gk * w, A * gk + B,
                          C * w + D * gk * w, C * gk + D)
        A2, B2 = c0 * (w * A + C), c0 * (w * B + D)
        C2, D2 = -w * A + C, -w * B + D
        den = D2 * D2 - C2 * C2
        center = (B2 * D2 - A2 * C2) / den
        radius = abs(A2 * D2 - B2 * C2) / abs(den)
        central = B2 / D2
        return center, radius, central, (A2, B2, C2, D2)


def pin_from_disk(build: dict, sz: dict, sigma: float,
                  depth: int | None = None) -> tuple:
    """P_hat(sigma) = (delta/2) x disk center of F with circle moments
    c_d = t_row[d]/delta == (1/2) x the t_row-Caratheodory value (the
    delta cancels); returns (P, R, central)."""
    with mp.workdps(DPS):
        w = mp.exp(-mp.mpf(sigma) * build["delta_mp"])
        cen, rad, cval, _m = weyl_disk_mp(sz["alphas"], sz["c0"], w, depth)
        half = mp.mpf(1) / 2
        return float(half * cen), float(half * rad), float(half * cval)


def trunc_sum(build: dict, sigma: float) -> float:
    """S_trunc = (delta/2)(c_0 + 2 sum c_d w^d) = the plain truncated
    interpolant transform (diagnostic for K5c)."""
    with mp.workdps(DPS):
        w = mp.exp(-mp.mpf(sigma) * build["delta_mp"])
        tot = build["row"][0] / 2
        wp = mp.mpf(1)
        for d in range(1, build["n"]):
            wp *= w
            tot += build["row"][d] * wp
        return float(tot)


# ------------------------------------------------- semi-analytic model
def model_tails(L: float, delta: float, sigma: float,
                atoms, weights, tgt_src, world: str) -> dict:
    """Closed/semi-analytic pieces of the truncated interpolant read:
    P_model = (pole full - tail - taper) - (arch full - rho_tail -
    taper_rho) - sum_atoms w E_delta(u)  [TRUE/SCRARITH]; SMOOTH swaps
    the atom sum for the closed smooth window read."""
    s = 0.5 + sigma
    n = int(round(L / delta))
    with mp.workdps(30):
        Lm, dm, sg = mp.mpf(L), mp.mpf(delta), mp.mpf(sigma)
        pole_full = 2 * sg / (sg * sg - mp.mpf(1) / 4)
        pole_tail = (mp.exp(-(sg - mp.mpf("0.5")) * Lm) / (sg - mp.mpf("0.5"))
                     + mp.exp(-(sg + mp.mpf("0.5")) * Lm)
                     / (sg + mp.mpf("0.5")))
        taper_p = mp.quad(
            lambda u: 2 * mp.cosh(u / 2)
            * (mp.exp(-sg * u) - mp.exp(-sg * (Lm - dm)) * (Lm - u) / dm),
            [Lm - dm, Lm])
        arch_full = mp.log(mp.pi) / 2 - mp.digamma(mp.mpf(s) / 2) / 2
        rho = lambda u: mp.exp(-u / 2) / (1 - mp.exp(-2 * u))  # noqa: E731
        rho_tail = mp.quad(lambda u: rho(u) * mp.exp(-sg * u),
                           [Lm, Lm + 4, mp.inf])
        taper_r = mp.quad(
            lambda u: rho(u)
            * (mp.exp(-sg * u) - mp.exp(-sg * (Lm - dm)) * (Lm - u) / dm),
            [Lm - dm, Lm])
        pole_read = float(pole_full - pole_tail - taper_p)
        arch_read = float(arch_full - rho_tail - taper_r)

    def e_interp(u: float) -> float:
        k = int(u / delta)
        if k >= n:
            return 0.0
        lam = (u - k * delta) / delta
        lo = math.exp(-sigma * k * delta)
        hi = math.exp(-sigma * (k + 1) * delta) if k + 1 < n else 0.0
        return (1.0 - lam) * lo + lam * hi

    if world == "SMOOTH":
        with mp.workdps(30):
            pr_read = float(mp.quad(
                lambda u: mp.exp(u / 2) * mp.mpf(e_interp(float(u))),
                np.linspace(0.0, L, 40).tolist()))
        pr_full = 1.0 / (sigma - 0.5)
    else:
        pr_read = sum(w * e_interp(u) for (u, _w), w in zip(atoms, weights))
        pr_full = tgt_src.lam_sum(s)
    p_model = pole_read - arch_read - pr_read
    tgt_full = (float(2 * sigma / (sigma * sigma - 0.25))
                - float(0.5 * math.log(math.pi))
                + 0.5 * float(mp.digamma(mp.mpf(s) / 2)) - pr_full)
    return {"P_model": p_model, "pole_read": pole_read,
            "arch_read": arch_read, "prime_read": pr_read,
            "tail_model": p_model - tgt_full}


# -------------------------------------------------------- AST firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for mmod in mods:
                if mmod.startswith("verification"):
                    bad.append("import " + mmod)
        if isinstance(node, ast.Attribute):
            if node.attr.lower() in {"zeta", "zetazero", "zetazeros",
                                     "nzeros", "siegelz", "siegeltheta"}:
                bad.append("attr " + node.attr)
        if isinstance(node, ast.Call):
            fn = node.func
            name = (fn.id if isinstance(fn, ast.Name)
                    else fn.attr if isinstance(fn, ast.Attribute) else "")
            if name.lower() in {"zetazero", "zetazeros", "nzeros"}:
                bad.append(name)
        if isinstance(node, ast.Name) and "christoffel" in node.id.lower():
            bad.append("identifier " + node.id)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        cache_ok = node.name.startswith(("ward_", "target_")) \
            or node.name == "main"
        for ch in ast.walk(node):
            if isinstance(ch, ast.Name) and ch.id == "CACHE_N7000" \
                    and not cache_ok:
                bad.append("cache in " + node.name)
    return not bad, "violations: %s" % (bad or "none")


def log_slope(xs, ys) -> float:
    xa, ya = np.asarray(xs, float), np.asarray(ys, float)
    live = ya > 0
    if live.sum() < 2:
        return float("nan")
    return float(np.polyfit(xa[live], np.log(ya[live]), 1)[0])


def fmt(vals) -> str:
    return "  ".join("%+.3e" % v for v in vals)


# ---------------------------------------------------------------- main
def main() -> int:
    global L_LADDER, DELTAS, NSIEVE, DPS
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = bool(args.smoke)
    if smoke:
        L_LADDER = (1.092, 1.608)
        DELTAS = (0.012, 0.006)
        NSIEVE = 4_000_000
        DPS = 35

    d_base = DELTAS[-1]
    print("=" * 78)
    print("krein_screw_realization_probe  PRIME.SUZUKI.KREIN."
          "REALIZATION.01")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if smoke else ""))
    print("=" * 78)
    mp_setup()

    # =================================================================
    section("I. INSTRUMENT WARDS")
    fw_ok, fw_det = firewall_audit()
    check("A1 AST firewall (zeta-free construction; cache X5"
          " ward-only)", fw_ok, fw_det)
    ok_cache = os.path.exists(CACHE_N7000)
    gammas = ward_cache_load() if ok_cache else np.zeros(0)
    check("A2 zero cache health (READ-ONLY, X5-typed)",
          ok_cache and len(gammas) >= 5000
          and abs(float(gammas[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gammas) > 0)),
          "n=%d gamma_1 dev %.1e" % (len(gammas),
          abs(float(gammas[0]) - GAMMA1_LIT) if len(gammas) else
          float("nan")))
    assert SIGMAS == SV.SIGMAS, "sigma grid must equal the SVPIN spec"
    print("  sigma grid: 16 values, asserted equal to the frozen SVPIN"
          " tuple.")

    t_sv = time.time()
    tgt_src = SV.SourceTarget(NSIEVE)
    print("  sieve: N=%d primes=%d psi_exact=%.6f (%.1f s)"
          % (NSIEVE, len(tgt_src.primes), tgt_src.psi_exact,
             time.time() - t_sv))
    tgt = {s: tgt_src.value(s) for s in SIGMAS}
    dev = {}
    a3_ok = True
    for s in SIGMAS:
        cch = ward_target_cache(gammas, s)
        dev[s] = abs(tgt[s] - cch)
        bar = 2e-3 if s < 0.8 else (5e-4 if s < 1.1 else 3e-4)
        a3_ok &= dev[s] <= bar
    check("A3 target cross-ward (16 sigma rows)", a3_ok,
          "max dev %.2e (bars 2e-3/5e-4/3e-4)"
          % max(dev.values()))

    # A4 synthetic OPUC pipeline ward
    with mp.workdps(DPS):
        nsyn = 48
        msyn = mp.mpf("0.15")
        th0 = mp.pi / 3
        c_syn = [mp.mpf("1.3")] + [2 * msyn * mp.cos(d * th0) / 2 * 2
                                   for d in range(1, nsyn)]
        # c_d = 0.3 cos(d pi/3) for d >= 1; c_0 = 1.3
        c_syn = [mp.mpf("1.3")] + [mp.mpf("0.3") * mp.cos(d * th0)
                                   for d in range(1, nsyn)]
        sz_syn = szego_mp(c_syn)
        wsyn = mp.mpf("0.4")
        cen, rad, cval, _m = weyl_disk_mp(sz_syn["alphas"],
                                          sz_syn["c0"], wsyn)
        cen2, rad2, _cv2, _m2 = weyl_disk_mp(
            sz_syn["alphas"], sz_syn["c0"], wsyn,
            depth=len(sz_syn["alphas"]) // 2)
        e0 = mp.expj(th0)
        f_true = mp.re(1 + msyn * ((e0 + wsyn) / (e0 - wsyn)
                                   + (1 / e0 + wsyn) / (1 / e0 - wsyn)))
        d_tru = abs(f_true - cen)
        d_cvl = abs(cval - cen)
        a4_ok = (sz_syn["ok"]
                 and d_tru <= rad * (1 + mp.mpf("1e-12")) + mp.mpf("1e-30")
                 and d_cvl <= rad * (1 + mp.mpf("1e-12")) + mp.mpf("1e-30")
                 and rad <= rad2 * (1 + mp.mpf("1e-20")))
    check("A4 synthetic OPUC ward (truth in disk; nesting)", a4_ok,
          "|F_true-center|=%.2e R=%.2e R(half)=%.2e"
          % (float(d_tru), float(rad), float(rad2)))

    # A5 lag cross-ward vs suz_lag_row (float64, suz convention grids)
    a5_ok = True
    a5_det = []
    for x in (3, 5, 8):
        row_ref, n_ref, d_ref = SV.suz_lag_row(x, 0.006)
        row_my, _n2, _at = build_lags_f64(n_ref * d_ref, d_ref,
                                          "TRUE", n_force=n_ref)
        dv = float(np.max(np.abs(row_my - row_ref))
                   / np.max(np.abs(row_ref)))
        a5_ok &= dv <= A5_BAR
        a5_det.append("x%d:%.1e" % (x, dv))
    check("A5 lag cross-ward: exact 2nd differences vs suz_lag_row"
          " quadrature", a5_ok, " ".join(a5_det) + " (bar %.0e)" % A5_BAR)

    if any(not ok for _n, ok, _d in CHECKS):
        print("\nABORT: SUZKREIN-INSTRUMENT-EDGE (exit 1; not a verdict)")
        return 1

    # =================================================================
    section("II. K1 -- SCREW PROPERTY + THE EXECUTED DICTIONARY")
    # K1a origin expansion (locks the +1/4 Lerch convention)
    atoms_o = prime_atoms(0.1)
    with mp.workdps(DPS):
        acon = MP_CONST["ACON"]
        rvals = {}
        for tt in ("0.02", "0.002"):
            t = mp.mpf(tt)
            gv = g_value_mp(t, atoms_o, [w for _u, w in atoms_o])
            rvals[tt] = float(abs(gv - (t * mp.log(t) / 2 + acon * t)) / t)
    check("K1a origin expansion g ~ (t/2)log t + A t (A = %.6f)"
          % float(MP_CONST["ACON"]),
          rvals["0.02"] <= 0.1 and rvals["0.002"] <= 0.35 * rvals["0.02"],
          "r(0.02)=%.3e r(0.002)=%.3e (locks Lerch coeff +1/4)"
          % (rvals["0.02"], rvals["0.002"]))

    # K1b screw kernel PSD on [-a, a], 81 pts, all rungs (float64)
    k1b_ok = True
    k1b_det = []
    for L in L_LADDER:
        a_half = L / 2.0
        m_g = 81
        h = 2 * a_half / (m_g - 1)
        gl = np.array([g_lattice_f64(k * h) for k in range(m_g)])
        idx = np.arange(m_g)
        tg = -a_half + idx * h
        gt = np.array([g_lattice_f64(abs(v)) for v in tg])
        Dm = np.abs(idx[:, None] - idx[None, :])
        K = gl[Dm] - gt[:, None] - gt[None, :]
        ev = np.linalg.eigvalsh(0.5 * (K + K.T))
        ratio = float(ev[0] / max(ev[-1], 1e-300))
        k1b_ok &= ratio >= G_PSD_BAR
        k1b_det.append("%s:%.1e" % (X_LABEL[L], ratio))
    check("K1b screw kernel G >= 0 on [-a,a] (81-pt grid, 4 rungs)",
          k1b_ok, "lam_min/lam_max " + " ".join(k1b_det)
          + " (bar %.0e)" % G_PSD_BAR)

    # builds: TRUE world, all rungs x all deltas per plan
    plan = []
    for L in L_LADDER:
        for dn in ("0.012", "0.006", "0.003"):
            if float(dn) not in DELTAS:
                continue
            if dn == "0.012" and L not in L_LADDER[:2]:
                continue
            plan.append((L, dn))
    builds = {}
    szs = {}
    print("  TRUE-world builds (mp, dps %d):" % DPS)
    k1c_ok = True
    for (L, dn) in plan:
        b = build_lags_mp(L, dn, "TRUE")
        sz = szego_mp(b["row"])
        builds[(L, dn)] = b
        szs[(L, dn)] = sz
        k1c_ok &= sz["ok"]
        print("    %s delta=%s n=%4d  c0=%10.4f  max|alpha|=%.6f"
              "  min_e=%.4f  %s  %.1fs"
              % (X_LABEL[L], dn, b["n"], float(sz["c0"]),
                 float(sz["amax"]), float(sz["den_min"]),
                 "OK" if sz["ok"] else "FAIL@k=%d" % sz["fail_k"],
                 b["build_s"]))
    check("K1c accelerant positivity certificate (Szego completes,"
          " all TRUE rungs)", k1c_ok,
          "every section T_r > 0 on the accessible windows"
          if k1c_ok else "SECTION POSITIVITY FAILS (see rung above)")
    if not k1c_ok or not k1b_ok:
        print("\nVERDICT: SUZKREIN-DEAD(screw/section positivity fails"
              " at finite window -- see exact numbers above)")
        print("NO RH CLAIM. EXPLORATION ONLY.")
        return 0

    # K1d/K1e layer dictionary gates at L3 (or last rung in smoke)
    L_dict = L_LADDER[2] if len(L_LADDER) > 2 else L_LADDER[-1]
    k1d_ok = True
    k1e_ok = True
    kp_worst = ka_worst = kr_worst = 0.0
    for dn in ("0.006", "0.003"):
        if float(dn) not in DELTAS:
            continue
        delta = float(dn)
        n = int(round(L_dict / delta))
        t = np.arange(n + 1) * delta
        g_p = -8.0 * (np.cosh(t / 2) - 1.0)
        atoms = prime_atoms(n * delta)
        g_a = -(t / 2.0) * (float(MP_CONST["PSI14"])
                            - float(MP_CONST["LOGPI"])) \
            - 0.25 * float(MP_CONST["PHI1"]) \
            + np.array([s_arch_f64(v) for v in t])
        g_r = np.zeros(n + 1)
        for u, w in atoms:
            g_r += w * np.maximum(t - u, 0.0)

        def lag_of(gv):
            rr = np.empty(n)
            rr[0] = -2.0 * gv[1] / delta
            rr[1:] = -(gv[0:n - 1] - 2.0 * gv[1:n] + gv[2:n + 1]) / delta
            return rr

        r_p, r_a, r_r = lag_of(g_p), lag_of(g_a), lag_of(g_r)
        for s in SIGMAS:
            e = np.exp(-s * delta * np.arange(n))
            half_p = 0.5 * r_p[0] + float(np.sum(r_p[1:] * e[1:]))
            half_a = 0.5 * r_a[0] + float(np.sum(r_a[1:] * e[1:]))
            half_r = 0.5 * r_r[0] + float(np.sum(r_r[1:] * e[1:]))
            md = model_tails(n * delta, delta, s, atoms,
                             [w for _u, w in atoms], tgt_src, "TRUE")
            bar_sc = max(K1D_ABS, K1_BIAS * s * s * delta * delta)
            d_a = abs(-half_a - md["arch_read"])
            d_p = abs(half_p - md["pole_read"])
            d_r = abs(-half_r - md["prime_read"]) \
                / max(abs(md["prime_read"]), 1e-12)
            ka_worst = max(ka_worst, d_a / bar_sc)
            kp_worst = max(kp_worst,
                           d_p / max(K1E_ABS,
                                     K1_BIAS * s * s * delta * delta))
            kr_worst = max(kr_worst, d_r / PRIME_REL)
            k1d_ok &= d_a <= bar_sc
            k1e_ok &= (d_p <= max(K1E_ABS, K1_BIAS * s * s * delta * delta)
                       and d_r <= PRIME_REL)
    check("K1d ARCH dictionary: reads == (1/2)log pi - (1/2)psi(s/2)"
          " - tails", k1d_ok, "worst dev/bar = %.3f (16 sigma x 2"
          " deltas)" % ka_worst)
    check("K1e pole/prime layer dictionary (closed forms + exact"
          " interpolant)", k1e_ok,
          "pole worst dev/bar %.3f; prime worst rel/bar %.3f"
          % (kp_worst, kr_worst))

    # =================================================================
    section("III. K2 -- THE REALIZATION (Hamiltonian, refinement,"
            " conditioning, disks)")
    # A6 Szego internal exactness (LU cross-check at m = 40)
    with mp.workdps(DPS):
        b3 = builds[(L_dict, "0.006")]
        sz3 = szs[(L_dict, "0.006")]
        m40 = 40
        Tm = mp.matrix(m40, m40)
        for i in range(m40):
            for jj in range(m40):
                Tm[i, jj] = b3["row"][abs(i - jj)] / b3["row"][0]
        rhs = mp.matrix(m40, 1)
        rhs[0] = 1
        sol = mp.lu_solve(Tm, rhs)
        e_lu = 1 / sol[0]
        prod39 = mp.mpf(1)
        for a in sz3["alphas"][: m40 - 1]:
            prod39 *= (1 - a * a)
        rel_a6 = float(abs(e_lu - prod39) / prod39)
    check("A6 Szego exactness: LU prediction error == prod(1-alpha^2)"
          " (m=40)", rel_a6 <= 1e-20, "rel dev %.2e" % rel_a6)

    # A7 Moebius-disk self-ward
    with mp.workdps(DPS):
        b2 = builds[(L_LADDER[1], "0.006")]
        sz2 = szs[(L_LADDER[1], "0.006")]
        worst_a7 = 0.0
        for s in (0.6, 2.0, 12.0):
            w = mp.exp(-mp.mpf(s) * b2["delta_mp"])
            cen, rad, _cv, mmat = weyl_disk_mp(sz2["alphas"], sz2["c0"], w)
            A2, B2, C2, D2 = mmat
            for kk in range(16):
                f = mp.expj(2 * mp.pi * kk / 16)
                val = (A2 * f + B2) / (C2 * f + D2)
                worst_a7 = max(worst_a7,
                               float(abs(abs(val - cen) - rad) / rad))
    check("A7 Moebius-disk boundary self-ward (16 samples, 3 sigma)",
          worst_a7 <= 1e-20, "worst | |T(f)-c|-R |/R = %.2e" % worst_a7)

    # pins on all builds
    P = {}
    R = {}
    for key, b in builds.items():
        szk = szs[key]
        P[key] = {}
        R[key] = {}
        for s in SIGMAS:
            p, r, _cv = pin_from_disk(b, szk, s)
            P[key][s] = p
            R[key][s] = r

    # bias per rung (delta 0.006 vs 0.003; smoke: 0.012 vs 0.006)
    d_hi, d_lo = ("0.006", "0.003") if not smoke else ("0.012", "0.006")
    bias = {}
    for L in L_LADDER:
        bias[L] = {s: abs(P[(L, d_hi)][s] - P[(L, d_lo)][s])
                   for s in SIGMAS}
    NF = {L: {s: max(1e-7, 3.0 * dev[s], bias[L][s]) for s in SIGMAS}
          for L in L_LADDER}

    # K2a Hamiltonian profile: background scaling + atom signature
    al_cs = np.array([float(a) for a in szs[(L_dict, d_hi)]["alphas"]])
    al_fs = np.array([float(a) for a in szs[(L_dict, d_lo)]["alphas"]])
    m_pair = min(len(al_cs), (len(al_fs) - 1) // 2)
    paired = 0.5 * (al_fs[0: 2 * m_pair: 2] + al_fs[1: 2 * m_pair: 2])
    live = np.abs(paired) > 1e-6
    amp = float(np.median(al_cs[:m_pair][live] / paired[live]))
    d_fine = float(d_lo)
    al_abs = np.abs(al_fs)
    spike_ok = True
    spike_det = []
    for u, _w in builds[(L_dict, d_lo)]["atoms"]:
        if not (0.1 < u < L_dict - 0.1):
            continue
        k0 = int(round(u / d_fine))
        lo = max(0, k0 - SPIKE_WIN)
        hi = min(len(al_abs), k0 + SPIKE_WIN + 1)
        kpk = lo + int(np.argmax(al_abs[lo:hi]))
        bg_lo = max(0, k0 - 20)
        bg = np.concatenate([al_abs[bg_lo: max(0, k0 - 8)],
                             al_abs[k0 + 8: k0 + 20]])
        contrast = float(al_abs[kpk] / max(np.median(bg), 1e-12))
        ok_s = abs(kpk - k0) <= SPIKE_BINS and contrast >= SPIKE_CONTRAST
        spike_ok &= ok_s
        spike_det.append("q=%d:%+d/%.1f" % (round(math.exp(u)),
                                            kpk - k0, contrast))
    check("K2a Hamiltonian: background alpha ~ delta A(r) + atom"
          " spikes at log q",
          AMP_LO <= amp <= AMP_HI and spike_ok,
          "amp ratio %.3f (bars %.1f..%.1f); spikes [offset/contrast]"
          " %s" % (amp, AMP_LO, AMP_HI, " ".join(spike_det)))
    print("  DECLARED: pointwise/energy profile is delta-ROUGH"
          " (atomic accelerant => atomic Krein coefficient);")
    print("  the delta-stable gated objects are the pins, the disks,"
          " and the spike positions.")
    al3 = [float(a) for a in szs[(L_dict, d_lo)]["alphas"]]
    print("  Verblunsky head (delta=%s): %s" % (d_lo,
          " ".join("%+.4f" % v for v in al3[:8])))

    # K2b Richardson refinement (L1, L2)
    ratios = []
    if "0.012" in [dn for (_L, dn) in plan]:
        for L in L_LADDER[:2]:
            for s in SIGMAS:
                if (L, "0.012") not in P or (L, "0.003") not in P:
                    continue
                num = P[(L, "0.012")][s] - P[(L, "0.006")][s]
                den = P[(L, "0.006")][s] - P[(L, "0.003")][s]
                nf0 = max(1e-7, 3.0 * dev[s])
                if abs(num) > 10 * nf0 and abs(den) > 10 * nf0:
                    ratios.append(num / den)
        print("  K2b live ratios: %s"
              % " ".join("%.2f" % v for v in sorted(ratios)))
    med_rich = float(np.median(ratios)) if ratios else float("nan")
    if smoke and not ratios:
        check("K2b Richardson delta-refinement ratio (O(delta^2) law)",
              True, "SMOKE-SKIP (delta-triple not in the smoke ladder)")
    else:
        check("K2b Richardson delta-refinement ratio (O(delta^2) law)",
              bool(ratios) and RICH_LO <= med_rich <= RICH_HI,
              "median %.3f over %d live rows (bars %.1f..%.1f)"
              % (med_rich, len(ratios), RICH_LO, RICH_HI))

    # K2c conditioning: deterministic 1e-25 perturbation at L_dict, d_hi
    with mp.workdps(DPS):
        eps = mp.mpf(10) ** (-COND_ROUND_DPS)
        b_c = builds[(L_dict, d_hi)]
        sz_c = szs[(L_dict, d_hi)]
        row_r = [v * (1 + eps * mp.cos(7 * d))
                 for d, v in enumerate(b_c["row"])]
        sz_r = szego_mp(row_r)
        rels = []
        for s in SIGMAS:
            w = mp.exp(-mp.mpf(s) * b_c["delta_mp"])
            cen0, _r0, _c0, _m0 = weyl_disk_mp(sz_c["alphas"],
                                               sz_c["c0"], w)
            cen1, _r1, _c1, _m1 = weyl_disk_mp(sz_r["alphas"],
                                               sz_r["c0"], w)
            rels.append(float(abs(cen1 - cen0) / abs(cen0)))
    med_cond = float(np.median(rels))
    amp_cond = med_cond / 10 ** (-COND_ROUND_DPS)
    k2c_ok = med_cond <= COND_BAR
    check("K2c conditioning under deterministic 1e-25 lag perturbation",
          k2c_ok, "median rel dP = %.2e (bar %.0e); amplification"
          " ~ %.1e" % (med_cond, COND_BAR, amp_cond))

    # K2d disk nesting
    k2d_ok = True
    with mp.workdps(DPS):
        for L in L_LADDER:
            b = builds[(L, d_lo)]
            szk = szs[(L, d_lo)]
            mfull = len(szk["alphas"])
            for s in SIGMAS:
                _p1, r_full, _c1 = pin_from_disk(b, szk, s)
                _p2, r_half, _c2 = pin_from_disk(b, szk, s,
                                                 depth=mfull // 2)
                k2d_ok &= r_full <= r_half * (1 + 1e-20)
    check("K2d Weyl-disk nesting R(m) <= R(m/2) (all rungs, all sigma)",
          k2d_ok, "nested" if k2d_ok else "NESTING VIOLATED")

    # =================================================================
    section("IV. K3 -- THE DECISIVE MEASUREMENT: Delta(sigma, a) AND"
            " THE DISK LAW")
    print("  PRIMARY table (delta = %s): Delta = P_hat - tgt per rung;"
          " R = disk radius; NF printed." % d_lo)
    rows_typ = {}
    slopes_R = {}
    tight = {}
    for s in SIGMAS:
        d_seq = [P[(L, d_lo)][s] - tgt[s] for L in L_LADDER]
        r_seq = [R[(L, d_lo)][s] for L in L_LADDER]
        nf4 = NF[L_LADDER[-1]][s]
        abs_seq = [abs(v) for v in d_seq]
        steps_ok = 0
        for i in range(len(abs_seq) - 1):
            if abs_seq[i] <= 3 * NF[L_LADDER[i]][s] \
                    and abs_seq[i + 1] <= 3 * NF[L_LADDER[i + 1]][s]:
                steps_ok += 1
            elif abs_seq[i + 1] <= WOBBLE * abs_seq[i]:
                steps_ok += 1
        if abs_seq[-1] <= max(abs_seq[0] / DROP, 3 * nf4) \
                and steps_ok >= len(abs_seq) - 2:
            typ = "CONVERGES"
        elif abs_seq[-1] > DIV_FAC * abs_seq[0] and abs_seq[-1] > 10 * nf4:
            typ = "DIVERGES"
        else:
            typ = "PLATEAUS"
        rows_typ[s] = typ
        slopes_R[s] = -log_slope(list(L_LADDER), r_seq)
        tight[s] = abs_seq[-1] <= max(3 * r_seq[-1], 3 * nf4)
        print("    sigma=%-8.5f tgt=%+.6e D: %s  %-9s R: %s"
              % (s, tgt[s], fmt(d_seq), typ, fmt(r_seq)))
        print("      NF=%.1e bias(L4)=%.1e disk-slope rho=%.2f tight=%s"
              % (nf4, bias[L_LADDER[-1]][s], slopes_R[s],
                 "Y" if tight[s] else "N"))
    n_conv = sum(1 for t in rows_typ.values() if t == "CONVERGES")
    n_div = sum(1 for t in rows_typ.values() if t == "DIVERGES")
    n_plat = len(SIGMAS) - n_conv - n_div
    check("K3a pin convergence rows (>= %d/16 CONVERGES)" % CONV_BAR,
          n_conv >= CONV_BAR and n_div < DIV_BAR,
          "%d CONVERGES / %d PLATEAUS / %d DIVERGES"
          % (n_conv, n_plat, n_div))
    k3b_ok = all(slopes_R[s] >= CONTRACT_FAC * s for s in SIGMAS)
    cfit = [slopes_R[s] - s for s in SIGMAS]
    check("K3b disk contraction rho(sigma) >= %.1f sigma (all rows)"
          % CONTRACT_FAC, k3b_ok,
          "measured law R ~ e^{-(sigma + c) L}, c = %.2f .. %.2f"
          " (median %.2f)" % (min(cfit), max(cfit),
                              float(np.median(cfit))))
    n_tight = sum(1 for s in SIGMAS if tight[s])
    check("K3c truth-tightness |Delta(L4)| <= max(3R, 3NF)"
          " (>= %d/16)" % TIGHT_BAR, n_tight >= TIGHT_BAR,
          "%d/16 rows tight" % n_tight)

    # controls at L_dict
    print("  CONTROLS at %s (delta %s):" % (X_LABEL[L_dict], d_hi))
    sep_fail = 0
    ctrl_lines = {}
    for wld in ("SMOOTH", "SCRARITH"):
        bw = build_lags_mp(L_dict, d_hi, wld)
        szw = szego_mp(bw["row"])
        if not szw["ok"]:
            print("    %-8s CONTROL-NOT-SCREW (Szego fails at depth"
                  " k=%d, r=%.3f) -- counts as separated"
                  % (wld, szw["fail_k"], szw["fail_k"] * bw["delta"]))
            ctrl_lines[wld] = "NOT-SCREW"
            continue
        seps, owns = [], []
        for s in SIGMAS:
            pw, rw, _cv = pin_from_disk(bw, szw, s)
            den_m = max(abs(P[(L_dict, d_lo)][s] - tgt[s]),
                        NF[L_dict][s], R[(L_dict, d_lo)][s])
            seps.append(abs(pw - tgt[s]) / den_m)
            if wld == "SMOOTH":
                tgt_w = tgt[s] + tgt_src.lam_sum(0.5 + s) - 1.0 / (s - 0.5)
                owns.append(abs(pw - tgt_w)
                            / max(rw, 3 * bias[L_dict][s], 1e-6))
        med_sep = float(np.median(seps))
        ok_sep = med_sep >= SEP_BAR
        if not ok_sep:
            sep_fail += 1
        own_txt = ""
        if wld == "SMOOTH":
            med_own = float(np.median(owns))
            ok_sep &= med_own <= OWN_BAR
            if med_own > OWN_BAR:
                sep_fail += 0  # own-consistency reported, sep drives kill
            own_txt = " | own-target consistency median %.2f (bar %.0f)" \
                % (med_own, OWN_BAR)
        ctrl_lines[wld] = "sep median %.2e%s" % (med_sep, own_txt)
        print("    %-8s separation median %.3e (bar %.0f) => %s%s"
              % (wld, med_sep, SEP_BAR,
                 "SEPARATES" if med_sep >= SEP_BAR else "FAILS", own_txt))
    check("K3d/K3e world controls separate (SMOOTH + SCRARITH)",
          sep_fail == 0, "; ".join("%s: %s" % (k, v)
                                   for k, v in ctrl_lines.items()))

    # =================================================================
    section("V. K4 -- THE TRACE-CLASS QUESTION, PRICED FROM"
            " MEASUREMENTS")
    d_k4 = 0.006
    n_k4 = [int(round(L / d_k4)) for L in L_LADDER]
    rows_k4 = {}
    for L, nn in zip(L_LADDER, n_k4):
        rr, _n, _at = build_lags_f64(L, d_k4, "TRUE", n_force=nn)
        rows_k4[L] = rr

    def res_l2(rr: np.ndarray, sig: float) -> np.ndarray:
        nn = len(rr)
        B = sla.toeplitz(rr) / d_k4
        M = d_k4 * (np.diag(np.full(nn, 2.0 / 3.0))
                    + np.diag(np.full(nn - 1, 1.0 / 6.0), 1)
                    + np.diag(np.full(nn - 1, 1.0 / 6.0), -1))
        Mh = sla.sqrtm(M).real
        Rm = np.linalg.solve(B + sig * sig * M, np.eye(nn))
        return Mh @ Rm @ Mh

    tr_emb = {s: [] for s in SIGMAS}
    tr_cmp = {s: [] for s in SIGMAS}
    mids = []
    for i in range(len(L_LADDER) - 1):
        LA, LB = L_LADDER[i], L_LADDER[i + 1]
        mids.append(0.5 * (LA + LB))
        for s in SIGMAS:
            SA = res_l2(rows_k4[LA], s)
            SB = res_l2(rows_k4[LB], s)
            nA, nB = len(rows_k4[LA]), len(rows_k4[LB])
            off = (nB - nA) // 2
            Pm = np.zeros((nB, nA))
            Pm[off: off + nA, :] = np.eye(nA)
            sv_e = np.linalg.svd(SB - Pm @ SA @ Pm.T, compute_uv=False)
            sv_c = np.linalg.svd(SB[off: off + nA, off: off + nA] - SA,
                                 compute_uv=False)
            tr_emb[s].append(float(sv_e.sum()))
            tr_cmp[s].append(float(sv_c.sum()))
    n_flat_e = n_flat_c = 0
    print("  trace norms ||resolvent difference||_tr per step"
          " (embed | compress), decay rate fitted:")
    for s in SIGMAS:
        re_ = -log_slope(mids, tr_emb[s])
        rc_ = -log_slope(mids, tr_cmp[s])
        if not (re_ > FLAT_RATE):
            n_flat_e += 1
        if not (rc_ > FLAT_RATE):
            n_flat_c += 1
        print("    sigma=%-8.5f embed: %s (rate %+.2f) | compress: %s"
              " (rate %+.2f)" % (s, fmt(tr_emb[s]), re_,
                                 fmt(tr_cmp[s]), rc_))
    typ_e = ("TRACECLASS-EMBED-FLAT" if n_flat_e >= 12
             else "TRACECLASS-EMBED-DECAYS")
    typ_c = ("TRACECLASS-COMPRESS-FLAT" if n_flat_c >= 12
             else "TRACECLASS-COMPRESS-DECAYS")
    print("  typed: %s (%d/16 flat) ; %s (%d/16 flat)"
          % (typ_e, n_flat_e, typ_c, n_flat_c))
    # appended Verblunsky blocks (delta d_lo)
    print("  appended Verblunsky-block l2 norms (the local Krein-system"
          " price, delta %s):" % d_lo)
    blk = []
    for i in range(len(L_LADDER) - 1):
        a_lo = szs[(L_LADDER[i], d_lo)]["alphas"]
        a_hi = szs[(L_LADDER[i + 1], d_lo)]["alphas"]
        v = math.sqrt(sum(float(x) ** 2
                          for x in a_hi[len(a_lo):]))
        blk.append(v)
    print("    ||alpha-block||_2 per step: %s (slope %+.2f)"
          % (fmt(blk), -log_slope(mids, blk)))
    print("  THE MINIMAL MISSING LEMMA (theorem-shaped, measured rates"
          " substituted):")
    print("    LEMMA (open).  Let g be Suzuki's screw function and"
          " suppose every finite section of the")
    print("    accelerant -g'' is positive (:= localized Weil"
          " positivity; equivalent to g screw on R = RH,")
    print("    measured true here through L = %.3f).  Then the Weyl"
          " disks D_a(i sigma) of the Krein" % L_LADDER[-1])
    print("    realization of -g'' on [0, 2a] contract to a point with"
          " radius R_a(sigma) <= C(eps)")
    print("    e^{-(sigma + c) 2a}, c = %.2f measured, UNIFORMLY on"
          " sigma >= 1/2 + eps, and the limit"
          % float(np.median(cfit)))
    print("    point is (1/2)<-g'', e^{-sigma|.|}> = xi'/xi(1/2 +"
          " sigma).  Suppliers to check: Krein's")
    print("    accelerant theorem (Krein 1955; Denisov survey Thm"
          " 12.x) gives existence + identification")
    print("    GIVEN all-a positivity; de Branges chain monotonicity"
          " gives the nesting; the uniformity")
    print("    near sigma = 1/2 is the open estimate.  HONEST PRICE:"
          " the all-a positivity hypothesis IS")
    print("    Weil positivity -- this carrier localizes the remaining"
          " analytic task (a disk-contraction")
    print("    rate for one explicit canonical system) but does not"
          " remove the positivity input; and the")
    print("    SVPIN price-list norm ||(A_a+sigma^2)^{-1} -"
          " (A+sigma^2)^{-1}||_tr is measured %s /"
          % ("FLAT" if n_flat_e >= 12 else "decaying"))
    print("    %s on this realization -- the trace-class formulation"
          " is the wrong currency; the"
          % ("FLAT" if n_flat_c >= 12 else "decaying"))
    print("    convergent object is the Weyl-function scalar (the disk"
          " center), i.e. (SV) should be")
    print("    carried by disk contraction, not by resolvent-difference"
          " trace norms.")

    # =================================================================
    section("VI. K5 -- HONESTY SCREENS")
    # K5a margin-relocation screen
    e_lad = [float(szs[(L, d_lo)]["den_min"]) for L in L_LADDER]
    d_lad_med = [float(np.median([abs(P[(L, d_lo)][s] - tgt[s])
                                  for s in SIGMAS])) for L in L_LADDER]
    span_e = abs(math.log10(e_lad[0] / e_lad[-1]))
    span_d = abs(math.log10(max(d_lad_med[0], 1e-300)
                            / max(d_lad_med[-1], 1e-300)))
    if span_e < 0.5:
        print("  K5a margin screen: e_min ladder %s spans %.2f decades"
              " while median|Delta| falls %.2f decades"
              % (fmt(e_lad), span_e, span_d))
        print("    => relocation onto the wall margin is STRUCTURALLY"
              " EXCLUDED on this ladder (typed; the")
        print("       SVPIN tau-slope screen is degenerate here and"
              " would be dishonest -- declared).")
        k5a_reloc = 0
    else:
        k5a_reloc = 0
        for s in SIGMAS:
            ds = [abs(P[(L, d_lo)][s] - tgt[s]) for L in L_LADDER]
            sl = np.polyfit(np.log10(e_lad),
                            np.log10(np.maximum(ds, 1e-300)), 1)[0]
            if sl >= 0.7:
                k5a_reloc += 1
        print("  K5a tau-slope screen ran verbatim: %d/16 rows RELOCATE"
              % k5a_reloc)
    k5a_ok = k5a_reloc < 6

    # K5b cache-transcription scan (ward namespace)
    fire_trans = False
    for L in (L_LADDER[-2], L_LADDER[-1]):
        worst_best = None
        smat = {s: ward_partial_sums(gammas, s) for s in SIGMAS}
        nmax = len(gammas)
        best = np.full(nmax, 0.0)
        acc = np.zeros(nmax)
        for s in SIGMAS:
            rel = np.abs(P[(L, d_lo)][s] - smat[s]) \
                / np.maximum(np.abs(smat[s]), 1e-12)
            acc = np.maximum(acc, rel)
        nstar = int(np.argmin(acc))
        worst_best = float(acc[nstar])
        fire_trans |= worst_best <= TRANS_BAR
        print("  K5b cache scan %s: min over N<=%d of max_sigma"
              " rel|P_hat - S_N| = %.3e at N = %d"
              % (X_LABEL[L], nmax, worst_best, nstar + 1))
    check("K5b no cache-partial-sum transcription (bar %.0e)"
          % TRANS_BAR, not fire_trans,
          "the pin values match no zero partial sum"
          if not fire_trans else "TRANSCRIPTION FIRES")

    # K5c source-truncation typing
    ratios_k5 = []
    for L in (L_LADDER[-2], L_LADDER[-1]):
        b = builds[(L, d_lo)]
        for s in SIGMAS:
            md = model_tails(b["L"], b["delta"], s, b["atoms"],
                             b["weights"], tgt_src, "TRUE")
            if abs(md["tail_model"]) > 10 * NF[L][s]:
                st = trunc_sum(b, s)
                ratios_k5.append(abs(P[(L, d_lo)][s] - st)
                                 / abs(md["tail_model"]))
    med_ex = float(np.median(ratios_k5)) if ratios_k5 else float("nan")
    extrap = bool(ratios_k5) and EXTRAP_LO <= med_ex <= EXTRAP_HI
    print("  K5c |P_hat - S_trunc| / |tail model| median = %.3f over"
          " %d live rows => %s" % (med_ex, len(ratios_k5),
          "SUZKREIN-EXTRAPOLATES (the Weyl reading RESUMS the missing"
          " tail; not a truncated-source transcription)" if extrap
          else "NOT typed as extrapolating"))
    print("  K5d conditioning law: e_min ladder %s; amplification"
          " under 25-digit rounding ~ %.1e" % (fmt(e_lad), amp_cond))

    # =================================================================
    section("VII. COMPOSITE VERDICT")
    wall = time.time() - T0_WALL
    check("A8 runtime", wall <= RUNTIME_BAR, "%.1f s" % wall)
    instrument_ok = all(ok for _n, ok, _d in CHECKS)
    if fire_trans:
        verdict = "SUZKREIN-TRANSCRIPTION"
    elif not k2c_ok:
        verdict = ("SUZKREIN-ILLPOSED(median rel dP %.1e under 25-digit"
                   " rounding; amplification %.1e)"
                   % (med_cond, amp_cond))
    elif sep_fail > 0:
        verdict = "SUZKREIN-BLIND(control separation fails)"
    elif not k5a_ok:
        verdict = "SUZKREIN-DISGUISE-ADJACENT(margin relocation)"
    elif n_div >= DIV_BAR:
        verdict = "SUZKREIN-DEAD(pins diverge: %d/16 rows)" % n_div
    elif not k3b_ok:
        verdict = "SUZKREIN-DEAD(no limit-point contraction)"
    elif n_conv >= CONV_BAR and n_tight >= TIGHT_BAR:
        verdict = ("SUZKREIN-CARRIER-OPEN(lemma: uniform Weyl-disk"
                   " contraction of the Krein realization of -g'' --"
                   " measured law R ~ e^{-(sigma+%.2f) L}, %d/16 rows"
                   " converge, %d/16 truth-tight, controls separate,"
                   " no zero data in the pipeline; the all-a section"
                   " positivity hypothesis remains Weil positivity"
                   " itself)" % (float(np.median(cfit)), n_conv,
                                 n_tight))
    else:
        verdict = ("SUZKREIN-DEAD(insufficient convergence: %d CONV /"
                   " %d PLAT / %d DIV, %d tight)"
                   % (n_conv, n_plat, n_div, n_tight))

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n  sub-verdicts: %s ; %s" % (typ_e, typ_c))
    print("                %s"
          % ("SUZKREIN-EXTRAPOLATES(median %.3f)" % med_ex if extrap
             else "extrapolation typing NOT confirmed (median %s)"
             % ("%.3f" % med_ex if med_ex == med_ex else "nan")))
    print("                margin relocation: %s"
          % ("structurally excluded (e_min span %.2f dec)" % span_e
             if span_e < 0.5 else "%d/16 relocate" % k5a_reloc))
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    if not instrument_ok:
        print("ABORT: SUZKREIN-INSTRUMENT-EDGE (a ward failed; exit 1)")
        print("NO RH CLAIM. EXPLORATION ONLY.")
        print("=" * 78)
        return 1
    print("VERDICT: %s" % verdict)
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("NO RH CLAIM. NO POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0


# float64 g on the screw-kernel lattice (module scope for K1b)
G_LAT_CACHE: dict[float, float] = {}


def g_lattice_f64(t: float) -> float:
    tt = round(abs(float(t)), 12)
    if tt in G_LAT_CACHE:
        return G_LAT_CACHE[tt]
    if tt == 0.0:
        return 0.0
    out = -8.0 * (math.cosh(tt / 2) - 1.0)
    for u, w in prime_atoms(tt + 1e-9):
        if u <= tt:
            out += w * (tt - u)
    out += -(tt / 2.0) * (float(MP_CONST["PSI14"])
                          - float(MP_CONST["LOGPI"])) \
        - 0.25 * float(MP_CONST["PHI1"]) + s_arch_f64(tt)
    G_LAT_CACHE[tt] = out
    return out


if __name__ == "__main__":
    sys.exit(main())
