#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""stieltjes_vitali_pin_probe -- PRIME.STIELTJES.VITALI.PIN.01

FROZEN SPEC (2026-08-14).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Build and adjudicate the STIELTJES-VITALI PIN route: replace the full
semilocal trace convergence (the remaining theorem of CCCLXXXII) by
countably many positive resolvent scalars in the absolutely convergent
Euler half-plane.  Setup: Xi(z) = xi(1/2 - i z), zeta-zero rho = beta
+ i gamma maps to z_rho = -gamma + i(beta - 1/2), so Xi is zero-free
on |Im z| >= 1/2.  For a source-only self-adjoint family H_x with
symmetric real spectrum {+-lam_{x,k}} define the Herglotz function
m_x(z) = sum_k 2z/(lam_k^2 - z^2) and the PIN SCALARS
    P_x(sigma) = sum_k 2 sigma/(lam_k^2 + sigma^2) = -i m_x(i sigma).
(SV): for the fixed sequence sigma_r = 1 + 1/r (accumulating at
sigma* = 1 > 1/2): lim_x P_x(sigma_r) = xi'/xi(1/2 + sigma_r) for
every r, the right side source-only through
    xi'/xi(s) = 1/s + 1/(s-1) - (1/2) log pi + (1/2) psi(s/2)
                - sum_{n>=2} Lambda(n) n^{-s}      (s > 1, absolute).
CLAIMED THEOREM (SV) => RH by: (1) one pin bounds the total resolvent
mass (convergent sequences are bounded; weight comparability) =>
normal family on C+; (2) Vitali: convergence at i sigma_r with
interior accumulation point i => locally uniform limit m holomorphic
on C+; (3) identity theorem near i sigma* identifies m = -Xi'/Xi on
Im z > 1/2, then unique continuation on the connected set
C+ \ Z(Xi); (4) an off-line zero z0 in C+ would make -Xi'/Xi blow up
near z0 while m is holomorphic there -- contradiction; (5) the
functional equation kills beta < 1/2.  This probe gates the skeleton,
runs the finite pre-check on the buildable extremal rungs, runs the
owner's frozen kill list, and types the circularity.

CONVENTION LOCK (T1c).  With Xi(z) = xi(1/2 - iz) the chain rule
gives -Xi'/Xi(i sigma) = i xi'/xi(1/2 + sigma) exactly; with the
opposite convention Xi(z) = xi(1/2 + iz) the functional equation
xi'/xi(1-s) = -xi'/xi(s) gives THE SAME target identity, so the
sign ambiguity of earlier rounds is harmless for the pins.  Numeric
verification at sigma = 1 (gate T1c): source formula vs the cache
zero route sum_{gamma>0} 2 sigma/(sigma^2 + gamma^2), bar 2e-4.

=======================================================================
FROZEN OBJECTS
=======================================================================
OPERATOR FAMILY: the record extremal trig-Galerkin family of
semilocal_realroot_limit_probe (imported, not re-implemented), HP
ladder x = (3, 5, 8, 13), dps = (45, 60, 80, 120), K = ceil(1.25 x
log x); zero census at working precision (record pipeline).  The
x = 21 rung is SKIPPED and declared: by the arbiter cost law the
build alone is 675.7 s (K = 80, dps = 128) and its census needs an
mp band scan over (0, 163] because float64 fabricates zeros beyond
tau ~ 30 and mp.polyroots does not converge at degree 79 (CCCLXXXIII)
-- beyond this probe's minutes-scale budget.

TWO PIN ROWS (both frozen before any computation):
  PRIMARY (NT row, the D# spectrum): P_x = pins over the NONTRIVIAL
    zeros of E_x only.  License: arbiter gate Q1d -- the CvS quotient
    D# = D - |D xi><1| has exactly the non-lattice zeros as spectrum
    (max |E(lam)|/scale = 1.85e-16), a source-only self-adjoint host.
  SECONDARY (FULL row, the E-divisor): NT plus the exact lattice tail
    sum_{j>=K} 2 sigma/((j pi/a)^2 + sigma^2)
      = (2a/pi) Im psi(K + i sigma a/pi)          (closed form, A6).
Pins are UNWEIGHTED by definition; gate A1 enforces this structurally
(AST purity of pin_sum: no identifiers besides its arguments and
numpy; no identifier in the file contains the substring
'christoffel'; the ordinate cache is readable only inside ward_* /
target_* functions and main -- X5-typed, instrument and diagnostics,
never construction; no zeta/zetazero/siegel attribute or call
anywhere).

FROZEN SIGMA GRID (16 values; the eight 1 + 1/r pins r = 8..1 plus
three sub-1 boundary probes plus five deep-half-plane values; frozen
here BEFORE any computation; no post-hoc selection -- every verdict
statistic runs over the full grid):
  SIGMAS = (0.6, 0.75, 0.9,
            1.125, 8/7, 7/6, 1.2, 1.25, 4/3, 1.5, 2.0,
            3.0, 4.0, 6.0, 8.0, 12.0)

TARGET SIDE (source-only: Gamma, pi, Lambda(n), n^{-s}, own sieve):
  tgt(sigma) = 1/s + 1/(s-1) - (1/2) log pi + (1/2) psi(s/2)
               - LAM(s),   s = 1/2 + sigma,
  LAM(s) = exact prime-power sum to NSIEVE = 4e7 (own sieve, ALL
  prime powers, no selection) plus the partial-summation tail
    s int_N^inf psitilde(t) t^{-s-1} dt - psi_exact(N) N^{-s},
    psitilde(t) = t - log(2 pi) - (1/2) log(1 - t^{-2}),
  with psi_exact(N) EXACT from the sieve (the E(N) offset enters
  exactly; the model error is the oscillatory integral
  s int_N^inf (E(t)-E(N)) t^{-s-1} dt ~ N^{1/2-s}).  MEASURED target
  uncertainty: dev(sigma) = |tgt - cache route| (A3), cache route =
  exact sum over the n7000 verified ordinates + RvM density tail
  (ward namespace).  A3 bars: 2e-3 (sigma < 0.8), 5e-4 (0.8 <=
  sigma < 1.1), 3e-4 (else).  NOISE FLOOR per sigma:
  NF(sigma) = max(1e-6, 3 dev(sigma)).

ROW TYPING per sigma over the 4-rung ladder (Delta_x = P_x - tgt):
  CONVERGES iff |Delta(13)| <= |Delta(3)|/DROP_SV and nonincreasing
    within WOBBLE = 1.3 at >= 2 of 3 steps (both-ends <= 10 NF =
    saturated pass); DROP_SV = 1.6, frozen a priori from the RvM
    tail model: the model drop of the missing-tail scalar between
    x = 3 and x = 13 is ~2.6 at sigma = 1 (printed per sigma); 1.6
    is ~60 percent of it (log-margin for edge-excess wobble).
  DIVERGES iff |Delta(13)| > 2 |Delta(3)| and |Delta(13)| > 10 NF.
  PLATEAUS otherwise.  Decay exponent = OLS slope of log |Delta| vs
  log x on live rungs (diagnostic, never a gate).

T1 SKELETON GATES (each computed, none asserted):
  T1a-1 weight comparability: C_D = max over the frozen compact
    D = {u + iv : u in (-3,-1.5,0,1.5,3), v in (0.05,0.3,1,3)} and
    over the union lambda-grid (dense 0..50, log 50..2000, plus every
    measured cell zero) of |2z/(lam^2-z^2)| (lam^2+sig1^2)/(2 sig1),
    sig1 = 2.0 (the r = 1 pin); bar C_D <= 2e3.
  T1a-2 ONE pin suffices: per MAIN rung, max_z sum_k
    |2z/(lam_k^2 - z^2)| (abs term-wise, NT + first 5000 lattice
    modes) <= C_D * P_x(2.0) + 1e-9.  This is the normal-family
    bound executed.
  T1a-3 spectrum honesty: on every MAIN cell census deficit <= 1,
    n_imag = 0, n_cplx = 0, min zero > 1, min zero spacing > 1e-6
    (multiplicity guard).  The all-x realness is the CF simplicity +
    evenness HYPOTHESIS of the family (cited [32], measured here) --
    the skeleton is conditional on it and this is named in print.
  T1b Vitali hypotheses: min sigma_r > 1/2 (accumulation point
    i sigma* = i is interior to C+ and to Im z > 1/2), pins pairwise
    distinct (computed from the frozen tuple).
  T1c convention/target identity at sigma = 1 (bar 2e-4, see LOCK).
  T1d tail bookkeeping (the two explicit computations of the task,
    plus the lattice comb): at sigma = 1, over x = 5 -> 13, the three
    sequences (i) true-zero tail beyond the band edge (cache + RvM,
    O(log T/T) law printed), (ii) measured Nyquist-excess edge mass
    (pin mass of ALL cell zeros above 0.75*2 pi x minus cache zeros
    in (0.75*2 pi x, band]; the cell side is windowed above only,
    because the excess zeros spill PAST the band edge K pi/a --
    measured on the smoke and frozen here), O(x/band^2) law printed,
    (iii) exact lattice tail (closed form, O(log x/x) law printed)
    are each decreasing (step tolerance 1.15x, ends strictly
    decreasing).
  Steps (2)-(5) of the chain are classical (Vitali-Porter, identity
  theorem on a domain minus a discrete set, isolated pole blow-up,
  functional equation) and are printed as prose with the exact
  citations, not faked as gates.

CONTROLS (the owner's kill list, frozen):
  (i) MESH-CF family: the record grid builder (uniform tent mesh,
    DELTA = 0.006, cap 450, unconditional CF realness), rungs
    x = (3, 5, 8, 13); mesh pin = pins over its zeros <= 450 plus its
    own measured-density tail rho_cap * 2 (pi/2 - atan(450/sigma)).
    Instrument ward A7: mesh census (0,30) = 9 +- 1 at x = 8 and
    11 +- 1 at x = 13 (arbiter uniform-density law), MAIN census
    (0,30) = 3 at x = 8 and 13.  Expected poisoning: uniform Nyquist
    density ~ log(x)/(2 pi) at ALL heights => P_mesh grows ~ log(x)/2
    instead of converging; measured as overshoot ratio P_mesh/tgt
    with its x-trend.  Typed MESH-POISONED iff median overshoot at
    x = 13 >= 3 and overshoot grows 3 -> 13.
  (ii) WORLD CONTROLS at x = 8 (HP): SCRPOS and EPSTEIN through the
    record HP builder; SMOOTH (prime-free PNT density e^{v/2}) and
    SCRARITH (golden-order weight permutation) through an mp
    extension builder in this file, WARDED against the record
    builder on MAIN at x = 3 and 5 (A5: tau rel <= 1e-6, zero max
    dev <= 1e-8).  TWO frozen separation metrics per world:
      metric A (target distance): |P^w_nt - tgt| / max(|Delta_nt(8)|,
        NF); EXPECTED to be weak: at accessible depth both numerator
        and denominator are dominated by the same tail bookkeeping --
        the honest reading is printed either way.
      metric B (band transcription): |P^w_band - S_cache_band| /
        max(|P^main_band - S_cache_band|, 1e-6), band = 0.75*2 pi x.
    A world SEPARATES iff metric B median over the sigma grid >= 5
    and >= 12/16 rows >= 1.5, with guard metric A median >= 1 (a
    world strictly CLOSER to the xi'/xi target than MAIN in median
    would be decisive world-blindness).
  (iii) NO Christoffel weights: structural gate in A1 (pins are raw
    unweighted sums).
  (iv) no zero cache in construction (A1), no tau_h consumed by any
    gate, no fit-as-gate (slopes are diagnostics), sigma grid frozen
    above.  TAU-SCREEN: OLS slope of log10 |Delta_nt| vs log10 tau
    over the ladder per sigma (tau = the true minuscule lam_min,
    spans ~47 decades); bands PASS |s| <= 0.30, RELOCATION s >= 0.70;
    SVPIN-DISGUISE fires iff >= 6 of 16 rows RELOCATE.  Expected
    honest outcome: |slope| ~ 0.01 (the pins live away from the
    critical line; Delta is polynomial in x, tau is e^{-4 pi x}).

T4 CIRCULARITY TYPING:
  Z1 gate: per rung x in (5, 8, 13) and per sigma, the band pin
  P_x^band (cell zeros <= 0.75*2 pi x) must equal the cache partial
  sum S_cache_band to rel <= 0.05 (Z1: the extremal Galerkin matrix
  IS the Gram matrix of zero evaluations; measured pin convergence on
  this family is a TRANSCRIPTION of partial sums of
  sum_gamma 2 sigma/(gamma^2 + sigma^2)).  x = 3 printed unGated
  (2 matched zeros).  If the gate passes the typing is
  SVPIN-Z1-TRANSCRIPTION: the finite pre-check can establish
  instrument consistency and tail bookkeeping, NEVER source-side
  content, on this family.
  SUZUKI HOST (the only corpus candidate for a non-minimizer host):
  A_a = Friedrichs extension of D* G_a D on H^1_0(-a,a) (Suzuki
  arXiv:2606.09096 Thm 1.1; v643 P1: hats on the lattice are exactly
  H^1_0 conforming, the L^2_0 projection generates no term; v630 S1:
  the atom layer is literally Suzuki's prime measure).  The hat
  compression is EXACTLY Toeplitz(t_row)/delta against the hat mass
  matrix delta*tridiag(2/3,1/6), t_row = the record grid lag vector
  (B[i,j] = -<g'', tent_{i-j}> = t_row[i-j]/delta since g'' =
  -2 cosh(t/2) + W); WARD A8: lam_min(Toeplitz(t_row)) reproduces the
  record grid builder tau to rel 1e-9.  SUZ pins at x = (8, 13):
  generalized eigenvalues mu_k, pin = sum over mu_k > 0 of
  2 sigma/(mu_k + sigma^2) (negative-mu count and mass reported
  separately).  Typed SUZPIN-TRACKS iff the first 5 sqrt(mu) match
  gamma_1..gamma_5 within 5 percent, else SUZPIN-FORM-SPECTRUM (the
  operator's spectrum is Weil-form margins, not ordinate squares,
  and the non-Z1 host needs the Krein inverse-spectral step).

COMPOSITE VERDICT (exactly one, priority frozen):
  SVPIN-INSTRUMENT-EDGE   any instrument ward fails (exit 1);
  SVPIN-SKELETON-GAP      a T1 gate fails (named);
  SVPIN-DIVERGES          >= 8/16 NT rows DIVERGE;
  SVPIN-WORLD-BLIND       metric-B separation fails for >= 2 of 4
                          worlds, or any world metric-A median < 1;
  SVPIN-DISGUISE          tau-relocation on >= 6/16 NT rows;
  SVPIN-PLATEAUS          < 12/16 NT rows CONVERGE;
  SVPIN-ROUTE-OPEN        otherwise, with the one remaining analytic
                          task stated exactly and priced.
Sub-verdicts always printed: SVPIN-SKELETON-SOUND/GAP(named);
SVPIN-CONVERGES(slopes)/PLATEAUS/DIVERGES per row and composite;
SVPIN-SEPARATES/WORLD-BLIND; disguise line; SVPIN-Z1-TRANSCRIPTION;
SUZPIN line.  RUNTIME_BAR = 1800 s.

DECLARED SUBSAMPLING AND MODELS: x = 21 skipped (cost law above);
mesh tail beyond 450 = measured-density model; SUZ host at 2 rungs;
lattice pin tail exact (closed form); target tail = psitilde model
anchored at exact psi(N); NT/FULL is the only row split, both frozen
here.  Smoke flag exists for pipeline shakeout only and prints
NOT-VERDICT-BEARING.  Amendments after the frozen run, if any, are
appended as numbered AMENDMENT blocks.

SMOKE DISCLOSURE (both smokes are part of the record; no bar, grid,
ladder, battery or verdict rule was changed): smoke 1 caught a grid
lookup (T1d used sigma = 1, not a grid key; now computed directly);
smoke 2 caught (a) the T1d edge-window definition (the Nyquist-excess
zeros spill past the band edge K pi/a, so the cell side of the edge
read is windowed above only -- with the old two-sided window the
edge term read ~0 by construction), (b) two smoke-only crashes
(tau-slope max() on an empty 2-rung list; the T1d decreasing test on
a 1-element smoke sequence), guarded without touching full-run
logic.  Substantive smoke readings (2 rungs, not verdict-bearing):
target cross-ward dev ~1e-7, extension builder identical to the
record builder at 0.0 deviation, NT deltas tail-dominated and
negative, FULL deltas smaller by the lattice compensation.

NO RH CLAIM.  NO POSITIVITY CLAIM.  EXPLORATION ONLY.
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
from scipy.linalg import eigh as sp_eigh
from scipy.linalg import toeplitz as sp_toeplitz

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import semilocal_realroot_limit_probe as SL  # record builder, imported

# ---------------------------------------------------------------- bars
HP_X = (3, 5, 8, 13)
SIGMAS = (0.6, 0.75, 0.9,
          1.125, 8.0 / 7.0, 7.0 / 6.0, 1.2, 1.25, 4.0 / 3.0, 1.5, 2.0,
          3.0, 4.0, 6.0, 8.0, 12.0)
PIN_SEQ = (2.0, 1.5, 4.0 / 3.0, 1.25, 1.2, 7.0 / 6.0, 8.0 / 7.0, 1.125)
NSIEVE = 40_000_000
DROP_SV = 1.6
WOBBLE = 1.3
DIV_FAC = 2.0
SEP_BAR = 5.0
SEP_MIN = 1.5
SEP_ROWS = 12
TAU_PASS = 0.30
TAU_RELOC = 0.70
DISGUISE_ROWS = 6
CD_BAR = 2e3
SIG1 = 2.0
ZBAND_FAC = 0.75
Z1_BAR = 0.05
T1C_BAR = 2e-4
A5_TAU_BAR = 1e-6
A5_ZERO_BAR = 1e-8
DELTA_GRID = 0.006
T_CAP_GRID = 450.0
SUZ_X = (8, 13)
SUZ_TRACK_BAR = 0.05
RUNTIME_BAR = 1800.0
GAMMA1_LIT = 14.134725141734693790
REC_TAU = {3: 3.06e-7, 5: 1.61e-16, 8: 3.77e-30, 13: 2.50e-54}
REC_TAU_REL = 0.05
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


# ----------------------------------------------------------- the sieve
def sieve_primes(n: int) -> np.ndarray:
    m = np.ones(n + 1, dtype=bool)
    m[:2] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if m[p]:
            m[p * p:: p] = False
    return np.nonzero(m)[0]


class SourceTarget:
    """xi'/xi(1/2 + sigma) from Gamma, pi, Lambda(n), n^{-s} only."""

    def __init__(self, nsieve: int) -> None:
        self.n = nsieve
        self.primes = sieve_primes(nsieve)
        self.logp = np.log(self.primes.astype(float))
        self.small = self.primes[self.primes <= math.isqrt(nsieve)]
        # exact psi(N) = sum_p log p * floor(log N / log p)
        tot = float(np.sum(self.logp))
        for p in self.small:
            lp = math.log(p)
            q = p * p
            while q <= nsieve:
                tot += lp
                q *= p
        self.psi_exact = tot

    def lam_finite(self, s: float) -> float:
        val = float(np.sum(self.logp * np.exp(-s * self.logp)))
        for p in self.small:
            lp = math.log(p)
            q = p * p
            while q <= self.n:
                val += lp * math.exp(-s * math.log(q))
                q *= p
        return val

    def lam_tail(self, s: float) -> float:
        """s int_N^inf psitilde t^{-s-1} dt - psi_exact(N) N^{-s},
        psitilde = t - log 2pi - (1/2) log(1 - t^{-2}); closed forms."""
        N = float(self.n)
        main = s * N ** (1.0 - s) / (s - 1.0)
        c2pi = -math.log(2.0 * math.pi) * N ** (-s)
        ser = 0.0
        for k in range(1, 4):
            ser += (s / 2.0) * N ** (-2.0 * k - s) / (k * (2.0 * k + s))
        return main + c2pi + ser - self.psi_exact * N ** (-s)

    def lam_sum(self, s: float) -> float:
        return self.lam_finite(s) + self.lam_tail(s)

    def value(self, sigma: float) -> float:
        s = 0.5 + sigma
        with mp.workdps(30):
            gpart = float(mp.psi(0, mp.mpf(s) / 2)) / 2.0
        return (1.0 / s + 1.0 / (s - 1.0) - 0.5 * math.log(math.pi)
                + gpart - self.lam_sum(s))


# ------------------------------------------------ wards (cache X5 side)
def ward_cache_load() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_target_cache(gammas: np.ndarray, sigma: float) -> float:
    """Zero route: exact sum over verified ordinates + RvM density
    tail (ward namespace; instrument only, never a target)."""
    s_fin = float(np.sum(2.0 * sigma / (gammas ** 2 + sigma ** 2)))
    gtop = float(gammas[-1])
    with mp.workdps(25):
        tail = mp.quad(lambda t: (mp.log(t / (2 * mp.pi)) / (2 * mp.pi))
                       * 2 * sigma / (t * t + sigma * sigma),
                       [gtop, 3 * gtop, 30 * gtop, mp.inf])
    return s_fin + float(tail)


def ward_cache_band_sum(gammas: np.ndarray, sigma: float,
                        tband: float) -> float:
    gg = gammas[gammas <= tband]
    return float(np.sum(2.0 * sigma / (gg ** 2 + sigma ** 2)))


def ward_true_tail(gammas: np.ndarray, sigma: float, tcut: float) -> float:
    """True-zero pin mass beyond tcut (cache + RvM beyond cache top)."""
    gg = gammas[gammas > tcut]
    s_fin = float(np.sum(2.0 * sigma / (gg ** 2 + sigma ** 2)))
    gtop = float(gammas[-1])
    with mp.workdps(25):
        tail = mp.quad(lambda t: (mp.log(t / (2 * mp.pi)) / (2 * mp.pi))
                       * 2 * sigma / (t * t + sigma * sigma),
                       [gtop, 3 * gtop, 30 * gtop, mp.inf])
    return s_fin + float(tail)


# ------------------------------------------------------------- the pins
def pin_sum(zr: np.ndarray, sig: float) -> float:
    return float(np.sum(2.0 * sig / (zr * zr + sig * sig)))


def pin_lattice(K: int, a: float, sig: float) -> float:
    """sum_{j>=K} 2 sig/((j pi/a)^2 + sig^2) = (2a/pi) Im psi(K+iq),
    q = sig a / pi (exact closed form)."""
    q = sig * a / math.pi
    with mp.workdps(30):
        v = mp.im(mp.psi(0, mp.mpc(K, q)))
    return float(2.0 * a / math.pi * v)


def lattice_abs_m(K: int, a: float, z: complex, jtop: int) -> float:
    """sum over lattice modes j = K..K+jtop of |2z/((j pi/a)^2 - z^2)|."""
    js = np.arange(K, K + jtop, dtype=float) * math.pi / a
    return float(np.sum(np.abs(2.0 * z / (js * js - z * z))))


# ---------------------------------- extension HP builder (SMOOTH/SCRAR)
def build_hp_ext(x: int, kfac: float, world: str, dps: int) -> dict:
    """mp trig-Galerkin cell, transcribed from the record builder
    (even sector) with two extra worlds: SMOOTH (prime-free density
    e^{v/2}, closed-form transform + mp.quad diagonals) and SCRARITH
    (golden-order weight permutation of the MAIN atoms).  MAIN is
    supported for the A5 equivalence ward only."""
    t0 = time.time()
    with mp.workdps(dps):
        aa = mp.log(x) / 2
        K = int(math.ceil(kfac * x * math.log(x)))
        ks = list(range(K))
        nmode = K
        oms = [k * mp.pi / aa for k in ks]
        par = [mp.mpf((-1.0) ** k) for k in ks]
        dsig = mp.mpf(-1)
        L2 = 2 * aa

        def a_weight(w):
            return mp.exp(-w / 2) / (-mp.expm1(-2 * w))

        def r_of(w):
            if w == 0:
                return mp.mpf("0.25")
            return a_weight(w) - 1 / (2 * w)

        jvec = []
        for i, o in enumerate(oms):
            if ks[i] == 0:
                jvec.append(mp.mpf(0))
                continue
            npts = int(mp.floor(L2 * o / mp.pi))
            pts = ([mp.mpf(0)]
                   + [jj * mp.pi / o for jj in range(1, npts + 1)]
                   + [L2])
            val = mp.quad(lambda w, o=o: mp.sin(o * w) * r_of(w), pts)
            jvec.append(val + mp.si(L2 * o) / 2)

        smooth = world == "SMOOTH"
        atoms: list[tuple] = []
        if world in ("MAIN", "SCRARITH"):
            icap = int(math.floor(x))
            sieve = np.zeros(icap + 1, dtype=bool)
            raw = []
            for p in range(2, icap + 1):
                if sieve[p]:
                    continue
                sieve[p * p:: p] = True
                q = p
                while q <= icap:
                    u = mp.log(q)
                    if 0 < u < L2:
                        raw.append((q, u, mp.log(p) / mp.sqrt(q)))
                    q *= p
            raw.sort(key=lambda t: float(t[1]))
            if world == "SCRARITH":
                key = np.mod(np.array([t[0] for t in raw], float)
                             * GOLDEN, 1.0)
                perm = np.argsort(key)
                ws = [raw[int(i)][2] for i in perm]
                atoms = [(raw[i][1], ws[i]) for i in range(len(raw))]
            else:
                atoms = [(u, w) for _q, u, w in raw]
        elif not smooth:
            raise ValueError(world)
        n_atoms = len(atoms)

        if smooth:
            pj = []
            for i, o in enumerate(oms):
                if ks[i] == 0:
                    pj.append(mp.mpf(0))
                    continue
                pj.append((mp.exp(L2 / 2) * (mp.sin(L2 * o) / 2
                                             - o * mp.cos(L2 * o)) + o)
                          / (mp.mpf(1) / 4 + o * o))
        else:
            pj = [sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))
                  for o in oms]

        M = mp.zeros(nmode, nmode)
        ipv = [par[i] * mp.sinh(aa / 2)
               / (mp.mpf(1) / 4 + oms[i] ** 2) for i in range(nmode)]
        for i in range(nmode):
            for j2 in range(nmode):
                M[i, j2] = 2 * ipv[i] * ipv[j2]
        for i in range(nmode):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                arch_od = -2 * sg * (oms[i] * jvec[i]
                                     - oms[j2] * jvec[j2]) / den
                prim_od = 2 * sg * (oms[i] * pj[i]
                                    - oms[j2] * pj[j2]) / den
                M[i, j2] += arch_od - prim_od
                M[j2, i] += arch_od - prim_od
        tail_c = lambda f0: -f0 / 2 * mp.log1p(-mp.exp(-2 * L2))
        for i in range(nmode):
            k = ks[i]
            o = oms[i]
            if k == 0:
                f0 = L2

                def psi_d(w):
                    return L2 - w
            else:
                f0 = aa

                def psi_d(w, o=o):
                    return ((aa - w / 2) * mp.cos(o * w)
                            + dsig * mp.sin(o * w) / (2 * o))

            def integrand(w, f0=f0, psi_d=psi_d):
                return ((f0 * mp.exp(-2 * w)
                         - psi_d(w) * mp.exp(-w / 2))
                        / (-mp.expm1(-2 * w)))
            npts = max(int(mp.floor(L2 * o / mp.pi)), 1) if k else 1
            base_pts = [mp.mpf(0), mp.mpf("1e-6"), mp.mpf("1e-3"),
                        mp.mpf("0.05"), L2]
            if k:
                base_pts += [jj * mp.pi / o for jj in range(1, npts + 1)]
            pts = sorted(set(p for p in base_pts if p <= L2))
            body = mp.quad(integrand, pts)
            if smooth:
                dpts = [mp.mpf(0), L2]
                if k:
                    dpts = sorted(set(
                        [mp.mpf(0), L2]
                        + [jj * mp.pi / o for jj in range(1, npts + 1)]))
                pdiag = mp.quad(lambda u, psi_d=psi_d:
                                psi_d(u) * mp.exp(u / 2), dpts)
            else:
                pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                                  + dsig * mp.sin(o * u) / (2 * o))
                             if k else w * (L2 - u)
                             for u, w in atoms), mp.mpf(0))
            M[i, i] += (-f0 * (mp.euler + mp.log(mp.pi))
                        + 2 * (body + tail_c(f0)) - 2 * pdiag)
        for i in range(nmode):
            ni = mp.sqrt(L2) if ks[i] == 0 else mp.sqrt(aa)
            for j2 in range(nmode):
                nj = mp.sqrt(L2) if ks[j2] == 0 else mp.sqrt(aa)
                M[i, j2] = M[i, j2] / (ni * nj)
        for i in range(nmode):
            for j2 in range(i):
                sym = (M[i, j2] + M[j2, i]) / 2
                M[i, j2] = sym
                M[j2, i] = sym
        E, Q = mp.eigsy(M)
        order = sorted(range(nmode), key=lambda i: E[i])
        i0 = order[0]
        tau_mp = E[i0]
        gap_mp = E[order[1]] - E[i0]
        cvec = [Q[i, i0] for i in range(nmode)]
        cn_mp = [cvec[i] / (mp.sqrt(L2) if ks[i] == 0 else mp.sqrt(aa))
                 for i in range(nmode)]
        if float(cn_mp[int(np.argmax([abs(float(v))
                                      for v in cn_mp]))]) < 0:
            cn_mp = [-v for v in cn_mp]
        cn_mp_str = [mp.nstr(v, dps) for v in cn_mp]
        cn = np.array([float(v) for v in cn_mp])
        tau_f = float(tau_mp)
        tau_log10 = float(mp.log10(abs(tau_mp))) if tau_mp != 0 \
            else float("-inf")
        tau_str = mp.nstr(tau_mp, 6)
        gap_str = mp.nstr(gap_mp, 6)
        a_f = float(aa)
    return {"x": x, "world": world, "K": K, "a": a_f,
            "om": np.arange(K, dtype=float) * math.pi / a_f,
            "sector": "even", "cn": cn, "cn_mp_str": cn_mp_str,
            "tau": tau_f, "tau_log10": tau_log10, "tau_str": tau_str,
            "gap": float(gap_mp), "gap_str": gap_str,
            "n_atoms": n_atoms, "dps": dps,
            "build_s": time.time() - t0}


# ------------------------------------------- Suzuki hat host (t_row)
def suz_lag_row(x: int, delta_target: float) -> tuple:
    """The record grid lag vector t_row (pole + arch - prime tent
    reads), transcribed from the record builder; warded by A8 against
    build_grid_cell's tau."""
    L = math.log(x)
    n = int(round(L / delta_target))
    if n % 2 == 0:
        n += 1
    delta = L / n
    lags = np.arange(n) * delta
    icosh = (8.0 / delta) * (math.cosh(0.5 * delta) - 1.0)
    t_pole = 2.0 * np.cosh(0.5 * lags) * icosh
    t_arch = np.zeros(n)
    for d in range(1, n):
        lo = max(lags[d] - delta, 1e-14)
        edges = np.array([lo, lags[d], lags[d] + delta])
        if d == 1:
            geo = delta * 0.5 ** np.arange(14, 0, -1)
            edges = np.unique(np.concatenate([geo, edges]))
        xs, ws = SL.gl_panels(edges)
        t_arch[d] = -float(np.sum(ws * SL.tent_at(xs, lags[d], delta)
                                  * SL.arch_weight(xs)))
    geo = delta * 0.5 ** np.arange(20, -1, -1.0)
    edges = np.unique(np.concatenate([[1e-14], geo]))
    xs, ws = SL.gl_panels(edges)
    tv = SL.tent_at(xs, 0.0, delta)
    body = float(np.sum(ws * (np.exp(-2.0 * xs) - tv * np.exp(-0.5 * xs))
                        / (-np.expm1(-2.0 * xs))))
    tail0 = -0.5 * math.log1p(-math.exp(-2.0 * delta))
    t_arch[0] = -(SL.EULER + SL.LOG_PI) + 2.0 * (body + tail0)
    x_eff = math.exp(lags[-1] + delta)
    _ns, us, wts = SL.prime_power_atoms(x_eff)
    t_prime = np.zeros(n)
    d_idx = np.round(us / delta).astype(int)
    for d0, u0, w0 in zip(d_idx, us, wts):
        for d in (d0 - 1, d0, d0 + 1):
            if 0 <= d < n:
                t_prime[d] += w0 * max(0.0, 1.0 - abs(u0 - lags[d]) / delta)
    return t_pole + t_arch - t_prime, n, delta


# ------------------------------------------------------------ firewall
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
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and "christoffel" in node.name.lower():
            bad.append("def " + node.name)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        cache_ok = node.name.startswith(("ward_", "target_")) \
            or node.name == "main"
        for ch in ast.walk(node):
            if isinstance(ch, ast.Name) and ch.id == "CACHE_N7000" \
                    and not cache_ok:
                bad.append("cache in " + node.name)
        if node.name == "pin_sum":
            allowed = {"zr", "sig", "np", "float"}
            for ch in ast.walk(node):
                if isinstance(ch, ast.Name) and ch.id not in allowed:
                    bad.append("pin_sum name " + ch.id)
    return not bad, "violations: %s" % (bad or "none")


def log_slope(xs: list[float], ys: list[float]) -> float:
    xa, ya = np.asarray(xs, float), np.asarray(ys, float)
    live = (xa > 0) & (ya > 0)
    if live.sum() < 2:
        return float("nan")
    return float(np.polyfit(np.log(xa[live]), np.log(ya[live]), 1)[0])


def fmt_row(vals: list[float]) -> str:
    return "  ".join("%+.3e" % v for v in vals)


# ---------------------------------------------------------------- main
def main() -> int:
    global HP_X, SUZ_X, NSIEVE
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = bool(args.smoke)
    if smoke:
        HP_X = (3, 5)
        SUZ_X = (5,)
        NSIEVE = 4_000_000

    print("=" * 78)
    print("stieltjes_vitali_pin_probe  PRIME.STIELTJES.VITALI.PIN.01")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if smoke else ""))
    print("=" * 78)

    # ================================================================
    section("I. INSTRUMENT WARDS")
    fw_ok, fw_det = firewall_audit()
    check("A1 AST firewall (zeta-free; cache X5 in ward_/target_;"
          " unweighted pins)", fw_ok, fw_det)
    ok_cache = os.path.exists(CACHE_N7000)
    gammas = ward_cache_load() if ok_cache else np.zeros(0)
    check("A2 zero cache health (READ-ONLY, X5-typed)",
          ok_cache and len(gammas) >= 5000
          and abs(float(gammas[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gammas) > 0)),
          "n=%d gamma_1 dev %.1e top %.1f"
          % (len(gammas), abs(float(gammas[0]) - GAMMA1_LIT)
             if len(gammas) else float("nan"),
             float(gammas[-1]) if len(gammas) else float("nan")))

    t_sv = time.time()
    tgt_src = SourceTarget(NSIEVE)
    print("  sieve: N=%d  primes=%d  psi_exact(N)=%.6f  (%.1f s)"
          % (NSIEVE, len(tgt_src.primes), tgt_src.psi_exact,
             time.time() - t_sv))
    tgt = {s: tgt_src.value(s) for s in SIGMAS}
    dev = {}
    a3_ok = True
    print("  A3 target cross-ward: source route vs cache route"
          " (dev = measured target uncertainty):")
    for s in SIGMAS:
        cch = ward_target_cache(gammas, s)
        dev[s] = abs(tgt[s] - cch)
        bar = 2e-3 if s < 0.8 else (5e-4 if s < 1.1 else 3e-4)
        ok = dev[s] <= bar
        a3_ok &= ok
        print("    sigma=%-8.5f tgt(src)=%+.8e cache=%+.8e dev=%.2e"
              " (bar %.0e) %s" % (s, tgt[s], cch, dev[s], bar,
                                  "ok" if ok else "FAIL"))
    check("A3 target cross-ward (16 sigma rows)", a3_ok, "see rows")
    NF = {s: max(1e-6, 3.0 * dev[s]) for s in SIGMAS}

    # lattice closed form: exact digamma telescoping + partial sum
    a_t, k_t, s_t = 1.0405, 21, 1.7
    lhs = pin_lattice(k_t, a_t, s_t)
    step = 2.0 * s_t / ((k_t * math.pi / a_t) ** 2 + s_t ** 2)
    rec = pin_lattice(k_t + 1, a_t, s_t) + step
    js = np.arange(k_t, k_t + 5000, dtype=float) * math.pi / a_t
    part = float(np.sum(2.0 * s_t / (js * js + s_t * s_t)))
    tele = part + pin_lattice(k_t + 5000, a_t, s_t)
    check("A6 lattice pin closed form (recurrence + telescope)",
          abs(lhs - rec) < 1e-14 and abs(lhs - tele) < 1e-12,
          "recur dev %.1e  telescope dev %.1e"
          % (abs(lhs - rec), abs(lhs - tele)))

    # ================================================================
    section("II. T1 -- SKELETON AUDIT, PART 1 (pre-build gates)")
    # T1a-1 comparability constant on the frozen compact
    zgrid = [complex(u, v) for u in (-3.0, -1.5, 0.0, 1.5, 3.0)
             for v in (0.05, 0.3, 1.0, 3.0)]
    lam_grid = np.concatenate([np.arange(0.0, 50.0, 0.02),
                               np.geomspace(50.0, 2000.0, 400)])
    cd = 0.0
    for z in zgrid:
        num = np.abs(2.0 * z / (lam_grid ** 2 - z * z))
        den = 2.0 * SIG1 / (lam_grid ** 2 + SIG1 ** 2)
        cd = max(cd, float(np.max(num / den)))
    check("T1a-1 weight comparability constant C_D",
          cd <= CD_BAR, "C_D = %.2f on frozen compact (bar %.0e);"
          " one pin at sigma_1 = 2 bounds |m_x| on D" % (cd, CD_BAR))
    # T1b Vitali hypotheses (frozen pin sequence)
    pin_arr = np.asarray(PIN_SEQ)
    check("T1b Vitali hypotheses (interior accumulation)",
          float(np.min(pin_arr)) > 0.5
          and float(np.min(np.abs(np.diff(np.sort(pin_arr))))) > 1e-6,
          "min sigma_r = %.4f > 1/2; accumulation point i sigma* = i"
          " (Im = 1, interior to C+ and to Im z > 1/2); %d distinct"
          " pins" % (float(np.min(pin_arr)), len(pin_arr)))
    # T1c convention lock at sigma = 1
    tgt1 = tgt_src.value(1.0)
    cch1 = ward_target_cache(gammas, 1.0)
    check("T1c target identity at sigma = 1",
          abs(tgt1 - cch1) <= T1C_BAR,
          "xi'/xi(3/2) src %+.8e vs zero route %+.8e dev %.2e"
          % (tgt1, cch1, abs(tgt1 - cch1)))
    print("  convention: Xi(z) = xi(1/2 - iz) => -Xi'/Xi(i sigma)"
          " = i xi'/xi(1/2 + sigma) (chain rule, exact);")
    print("  the opposite convention gives the SAME identity via"
          " xi'/xi(1-s) = -xi'/xi(s): harmless ambiguity.")
    print("  classical steps (prose, not gates): (2) Vitali-Porter on"
          " the locally bounded Herglotz family;")
    print("  (3) identity theorem on Im z > 1/2 then unique"
          " continuation on C+ minus the discrete set Z(Xi)")
    print("      (Xi entire, not identically 0 => Z(Xi) discrete =>"
          " C+ \\ Z(Xi) connected);")
    print("  (4) a zero z0 of Xi in C+ is a pole of -Xi'/Xi (residue"
          " = -mult != 0) while the locally bounded")
    print("      holomorphic limit m is bounded near z0 --"
          " contradiction; degenerate m == const excluded by")
    print("      local boundedness (limit is a genuine holomorphic"
          " function, never the constant infinity);")
    print("  (5) beta < 1/2 zeros map to C- and are killed by"
          " xi(s) = xi(1-s).")
    print("  NAMED CONDITION: the skeleton is conditional on real"
          " symmetric spectra for ALL x -- for the extremal")
    print("  family that is the CF simplicity+evenness hypothesis"
          " ([32], cited + measured per rung below, unproven all-x).")
    print("  NAMED GAP CARRIER: all content sits in (SV) itself --"
          " gates below type what the finite pre-check can carry.")

    if any(not ok for _n, ok, _d in CHECKS):
        print("\nVERDICT: SVPIN-INSTRUMENT-EDGE")
        return 1

    # ================================================================
    section("III. THE EXTREMAL LADDER (record builder) + SKELETON"
            " PART 2")
    cells: dict[int, dict] = {}
    for x in HP_X:
        c = SL.build_trig_cell_hp(x, SL.KFAC, "MAIN", SL.HP_DPS[x])
        SL.hp_zero_data(c)
        cells[x] = c
        print("  MAIN-%-3d K=%3d dps=%3d tau=%s gap=%s census %d/%d"
              " imag=%d cplx=%d minz=%8.4f  %.1fs"
              % (x, c["K"], c["dps"], c["tau_str"], c["gap_str"],
                 len(c["zeros"]), c["census_expect"], c["n_imag"],
                 c["n_cplx"], c["min_zero"], c["build_s"]))
    a4_ok = True
    a4_det = []
    for x in HP_X:
        if x in REC_TAU:
            rel = abs(cells[x]["tau"] - REC_TAU[x]) / REC_TAU[x]
            a4_ok &= rel <= REC_TAU_REL
            a4_det.append("x%d:%.3f" % (x, rel))
    check("A4 record tau ladder reproduction", a4_ok,
          "rel dev vs frozen record %s (bar %.2f)"
          % (" ".join(a4_det), REC_TAU_REL))
    # A5 extension-builder equivalence on MAIN
    a5_ok = True
    a5_det = []
    for x in (3, 5):
        if x not in cells:
            continue
        ce = build_hp_ext(x, SL.KFAC, "MAIN", SL.HP_DPS[x])
        SL.hp_zero_data(ce)
        rt = abs(ce["tau"] - cells[x]["tau"]) / abs(cells[x]["tau"])
        nz = min(len(ce["zeros"]), len(cells[x]["zeros"]))
        dz = float(np.max(np.abs(ce["zeros"][:nz]
                                 - cells[x]["zeros"][:nz]))) if nz else 1.0
        a5_ok &= (rt <= A5_TAU_BAR and dz <= A5_ZERO_BAR
                  and len(ce["zeros"]) == len(cells[x]["zeros"]))
        a5_det.append("x%d: tau rel %.1e, max|dz| %.1e" % (x, rt, dz))
    check("A5 extension builder == record builder (MAIN x=3,5)",
          a5_ok, "; ".join(a5_det))
    # A7 census wards
    c30 = {x: int(np.sum(cells[x]["zeros"] < 30.0)) for x in HP_X}
    a7_main = all(c30[x] == 3 for x in HP_X if x >= 8)
    print("  MAIN census (0,30): %s"
          % "  ".join("x%d:%d" % (x, c30[x]) for x in HP_X))
    # T1a-3 spectrum honesty
    hon_ok = True
    hon_det = []
    for x in HP_X:
        c = cells[x]
        minsp = float(np.min(np.diff(c["zeros"]))) if len(c["zeros"]) > 1 \
            else float("inf")
        ok = (0 <= c["census_deficit"] <= 1 and c["n_imag"] == 0
              and c["n_cplx"] == 0 and c["min_zero"] > 1.0
              and minsp > 1e-6)
        hon_ok &= ok
        hon_det.append("x%d[def %d, imag %d, cplx %d, minsp %.1e]"
                       % (x, c["census_deficit"], c["n_imag"],
                          c["n_cplx"], minsp))
    check("T1a-3 spectrum honesty (real, simple, no lam=0)",
          hon_ok, " ".join(hon_det))

    # pins on the ladder
    P_nt = {x: {s: pin_sum(cells[x]["zeros"], s) for s in SIGMAS}
            for x in HP_X}
    LAT = {x: {s: pin_lattice(cells[x]["K"], cells[x]["a"], s)
               for s in SIGMAS} for x in HP_X}
    P_full = {x: {s: P_nt[x][s] + LAT[x][s] for s in SIGMAS}
              for x in HP_X}

    # T1a-2 one-pin normal-family bound, executed per rung
    t1a2_ok = True
    t1a2_det = []
    for x in HP_X:
        c = cells[x]
        p2 = P_full[x][2.0]
        worst = 0.0
        for z in zgrid:
            zz = np.asarray(c["zeros"], float)
            mabs = float(np.sum(np.abs(2.0 * z / (zz * zz - z * z))))
            mabs += lattice_abs_m(c["K"], c["a"], z, 5000)
            worst = max(worst, mabs / (cd * p2))
        t1a2_ok &= worst <= 1.0 + 1e-9
        t1a2_det.append("x%d:%.4f" % (x, worst))
    check("T1a-2 one-pin bound max|m|/(C_D P_x(2)) <= 1",
          t1a2_ok, " ".join(t1a2_det))

    # T1d tail bookkeeping at sigma = 1
    s1 = 1.0
    seq_tail, seq_edge, seq_lat = [], [], []
    print("  T1d tail bookkeeping at sigma = 1 (models printed):")
    for x in HP_X:
        c = cells[x]
        band = c["K"] * math.pi / c["a"]
        tcmp = ZBAND_FAC * 2.0 * math.pi * x
        true_tail = ward_true_tail(gammas, s1, band)
        zz = c["zeros"]
        edge_cell = pin_sum(zz[zz > tcmp], s1)
        gg = gammas[(gammas > tcmp) & (gammas <= band)]
        edge_true = pin_sum(gg, s1)
        edge = edge_cell - edge_true
        lat1 = pin_lattice(cells[x]["K"], cells[x]["a"], s1)
        mod_tail = (s1 / math.pi) * (math.log(band / (2 * math.pi))
                                     + 1.0) / band
        mod_edge = 2.0 * s1 * (x - 0.375) / band ** 2
        if x >= 5:
            seq_tail.append(true_tail)
            seq_edge.append(abs(edge))
            seq_lat.append(lat1)
        print("    x=%-3d band=%7.2f true-tail=%.4e (model logT/T"
              " %.4e)  edge-excess=%+.4e (model %.4e)  lattice=%.4e"
              % (x, band, true_tail, mod_tail, edge, mod_edge, lat1))

    def decr(seq: list[float]) -> bool:
        if len(seq) < 2:      # smoke-only ladder truncation
            return True
        return (all(seq[i + 1] <= 1.15 * seq[i]
                    for i in range(len(seq) - 1))
                and seq[-1] < seq[0])

    check("T1d tail bookkeeping decreasing (x = 5 -> 13)",
          decr(seq_tail) and decr(seq_edge) and decr(seq_lat),
          "tail %s | edge %s | lattice %s"
          % (fmt_row(seq_tail), fmt_row(seq_edge), fmt_row(seq_lat)))

    # ================================================================
    section("IV. T2 -- THE PIN PRE-CHECK Delta_x(sigma) = P_x - tgt")
    print("  PRIMARY row: NT pins (D# spectrum, arbiter Q1d);"
          " SECONDARY row: FULL pins (E-divisor incl. lattice).")

    def type_row(seq_abs: list[float], nf: float) -> str:
        first, last = seq_abs[0], seq_abs[-1]
        steps_ok = 0
        for i in range(len(seq_abs) - 1):
            if seq_abs[i] <= 10 * nf and seq_abs[i + 1] <= 10 * nf:
                steps_ok += 1
            elif seq_abs[i + 1] <= WOBBLE * seq_abs[i]:
                steps_ok += 1
        if last <= first / DROP_SV and steps_ok >= len(seq_abs) - 2:
            return "CONVERGES"
        if last > DIV_FAC * first and last > 10 * nf:
            return "DIVERGES"
        return "PLATEAUS"

    tau_logs = [cells[x]["tau_log10"] for x in HP_X]
    rows_nt, rows_full = {}, {}
    slopes_nt, tau_slopes = {}, {}
    print("  NT table (Delta per x; type; slope d log|Delta|/d log x;"
          " tau-screen slope):")
    for s in SIGMAS:
        d_nt = [P_nt[x][s] - tgt[s] for x in HP_X]
        d_fl = [P_full[x][s] - tgt[s] for x in HP_X]
        abs_nt = [abs(v) for v in d_nt]
        typ = type_row(abs_nt, NF[s])
        rows_nt[s] = typ
        rows_full[s] = type_row([abs(v) for v in d_fl], NF[s])
        slp = log_slope(list(HP_X), abs_nt)
        slopes_nt[s] = slp
        pairs = [(tl, math.log10(max(a, 1e-300)))
                 for tl, a in zip(tau_logs, abs_nt) if a > 10 * NF[s]]
        ts = (float(np.polyfit([p[0] for p in pairs],
                               [p[1] for p in pairs], 1)[0])
              if len(pairs) >= 3 else float("nan"))
        tau_slopes[s] = ts
        flag = " [pin r=%d]" % round(1.0 / (s - 1.0)) \
            if any(abs(s - p) < 1e-12 for p in PIN_SEQ) else ""
        print("    sigma=%-8.5f tgt=%+.6e  D: %s  %-9s slope=%+.2f"
              " tau-slope=%s%s"
              % (s, tgt[s], fmt_row(d_nt), typ, slp,
                 ("%.3f" % ts) if ts == ts else "nan", flag))
    print("  FULL table (secondary; lattice comb included):")
    for s in SIGMAS:
        d_fl = [P_full[x][s] - tgt[s] for x in HP_X]
        print("    sigma=%-8.5f D: %s  %-9s"
              % (s, fmt_row(d_fl), rows_full[s]))
    print("  RvM model drop of the missing-tail scalar x=3 -> 13"
          " (a-priori justification of DROP_SV = 1.6):")
    for s in (0.6, 1.5, 4.0, 12.0):
        b3 = cells[HP_X[0]]["K"] * math.pi / cells[HP_X[0]]["a"]
        b13 = cells[HP_X[-1]]["K"] * math.pi / cells[HP_X[-1]]["a"]
        m3 = ward_true_tail(gammas, s, b3)
        m13 = ward_true_tail(gammas, s, b13)
        print("    sigma=%-6.3f model drop %.2f" % (s, m3 / m13))
    n_conv = sum(1 for t in rows_nt.values() if t == "CONVERGES")
    n_div = sum(1 for t in rows_nt.values() if t == "DIVERGES")
    n_plat = len(SIGMAS) - n_conv - n_div
    lo_s = [slopes_nt[s] for s in SIGMAS[:3]]
    hi_s = [slopes_nt[s] for s in SIGMAS[-4:]]
    print("  NT typing: %d CONVERGES / %d PLATEAUS / %d DIVERGES"
          " of %d" % (n_conv, n_plat, n_div, len(SIGMAS)))
    print("  sigma-dependence of the rate: slopes at sigma<1: %s |"
          " deep half-plane: %s"
          % (" ".join("%+.2f" % v for v in lo_s),
             " ".join("%+.2f" % v for v in hi_s)))
    n_reloc = sum(1 for v in tau_slopes.values()
                  if v == v and v >= TAU_RELOC)
    live_ts = [abs(v) for v in tau_slopes.values() if v == v]
    print("  tau-screen: %d/%d rows RELOCATE (bar %d fires DISGUISE);"
          " max |slope| = %s"
          % (n_reloc, len(SIGMAS), DISGUISE_ROWS,
             ("%.3f" % max(live_ts)) if live_ts else "nan (smoke)"))
    print("  x = 21 rung: SKIPPED, declared (arbiter cost law: build"
          " 675.7 s at K=80/dps=128; census needs an mp band scan --")
    print("  float64 fabricates zeros beyond tau ~ 30 and mp.polyroots"
          " does not converge at degree 79; ~30 min total).")

    # ================================================================
    section("V. T3 -- CONTROLS (frozen kill list)")
    # (i) mesh-CF
    print("  (i) MESH-CF pins (uniform tent mesh, delta = %.3f):"
          % DELTA_GRID)
    mesh_over = {}
    mesh_c30 = {}
    for x in HP_X:
        gc = SL.build_grid_cell(x, DELTA_GRID)
        SL.grid_zero_data(gc)
        mesh_c30[x] = int(np.sum(gc["zeros"] < 30.0))
        overs = []
        for s in SIGMAS:
            pm = pin_sum(gc["zeros"], s) + gc["rho_cap"] * 2.0 \
                * (math.pi / 2.0 - math.atan(T_CAP_GRID / s))
            overs.append(pm / tgt[s])
        mesh_over[x] = float(np.median(overs))
        print("    x=%-3d n=%4d census(0,30)=%2d (Xi: 3)  median"
              " P_mesh/tgt = %.2f  [range %.2f .. %.2f]"
              % (x, gc["n"], mesh_c30[x], mesh_over[x],
                 min(overs), max(overs)))
    a7_ok = a7_main
    if 8 in mesh_c30:
        a7_ok &= abs(mesh_c30[8] - 9) <= 1
    if 13 in mesh_c30:
        a7_ok &= abs(mesh_c30[13] - 11) <= 1
    check("A7 census wards (MAIN (0,30)=3 at x>=8; mesh follows"
          " uniform-density law)", a7_ok,
          "MAIN %s; mesh %s"
          % ({x: c30[x] for x in HP_X}, mesh_c30))
    mesh_poisoned = (mesh_over[HP_X[-1]] >= 3.0
                     and mesh_over[HP_X[-1]] > mesh_over[HP_X[0]])
    print("    mesh verdict: %s (uniform Nyquist density poisons the"
          " pins; wrong limit, growing like log x)"
          % ("MESH-POISONED" if mesh_poisoned else "MESH-NOT-POISONED"))

    # (ii) worlds at x = 8
    xw = 8 if 8 in HP_X else HP_X[-1]
    print("  (ii) WORLD CONTROLS at x = %d (HP):" % xw)
    worlds = {}
    for w in ("SCRPOS", "EPSTEIN"):
        cw = SL.build_trig_cell_hp(xw, SL.KFAC, w, SL.HP_DPS[xw])
        SL.hp_zero_data(cw)
        worlds[w] = cw
    for w in ("SMOOTH", "SCRARITH"):
        cw = build_hp_ext(xw, SL.KFAC, w, SL.HP_DPS[xw])
        SL.hp_zero_data(cw)
        worlds[w] = cw
    tband_w = ZBAND_FAC * 2.0 * math.pi * xw
    zmain = cells[xw]["zeros"]
    sep_fail = 0
    guard_fail = 0
    for w, cw in worlds.items():
        zz = cw["zeros"]
        ra, rb, nb_over = [], [], 0
        for s in SIGMAS:
            d_w = abs(pin_sum(zz, s) - tgt[s])
            d_m = abs(P_nt[xw][s] - tgt[s])
            ra.append(d_w / max(d_m, NF[s]))
            bw = abs(pin_sum(zz[zz <= tband_w], s)
                     - ward_cache_band_sum(gammas, s, tband_w))
            bm = abs(pin_sum(zmain[zmain <= tband_w], s)
                     - ward_cache_band_sum(gammas, s, tband_w))
            rB = bw / max(bm, 1e-6)
            rb.append(rB)
            if rB >= SEP_MIN:
                nb_over += 1
        medA = float(np.median(ra))
        medB = float(np.median(rb))
        seps = medB >= SEP_BAR and nb_over >= SEP_ROWS
        if not seps:
            sep_fail += 1
        if medA < 1.0:
            guard_fail += 1
        print("    %-9s census %d/%d imag=%d cplx=%d tau=%s |"
              " metricA med %.2f | metricB med %.2e rows>=%.1f:"
              " %d/%d => %s%s"
              % (w, len(cw["zeros"]), cw["census_expect"],
                 cw["n_imag"], cw["n_cplx"], cw["tau_str"], medA,
                 medB, SEP_MIN, nb_over, len(SIGMAS),
                 "SEPARATES" if seps else "FAILS",
                 "  [metricA<1: WORLD CLOSER THAN MAIN]"
                 if medA < 1.0 else ""))
    print("    (iii) Christoffel-free + unweighted pins: enforced"
          " structurally by gate A1.")
    print("    (iv) no zero cache in construction (A1), no tau in any"
          " gate input, slopes diagnostic-only, sigma grid frozen.")

    # ================================================================
    section("VI. T4 -- CIRCULARITY TYPING + THE SUZUKI HOST")
    z1_ok = True
    z1_det = []
    print("  Z1 partial-sum comparison (band = %.2f * 2 pi x):"
          % ZBAND_FAC)
    for x in HP_X:
        c = cells[x]
        tb = ZBAND_FAC * 2.0 * math.pi * x
        zz = c["zeros"][c["zeros"] <= tb]
        rels = []
        for s in SIGMAS:
            pb = pin_sum(zz, s)
            sb = ward_cache_band_sum(gammas, s, tb)
            rels.append(abs(pb - sb) / max(abs(sb), 1e-12))
        mx = max(rels)
        if x >= 5:
            z1_ok &= mx <= Z1_BAR
        z1_det.append("x%d:%.2e" % (x, mx))
        print("    x=%-3d matched %d cell zeros vs %d cache ordinates"
              " <= %.1f; max rel dev over grid = %.3e%s"
              % (x, len(zz), int(np.sum(gammas <= tb)), tb, mx,
                 "" if x >= 5 else "  [unGated, 1-2 zeros]"))
    check("Z1 band pins ARE cache partial sums (x = 5, 8, 13)",
          z1_ok, " ".join(z1_det) + "  (bar %.2f)" % Z1_BAR)
    print("  TYPING: the measured pin convergence on the extremal"
          " family is a Z1 TRANSCRIPTION of partial sums of")
    print("  sum_gamma 2 sigma/(gamma^2+sigma^2): the finite pre-check"
          " establishes instrument consistency and tail")
    print("  bookkeeping, never source-side content (the Galerkin"
          " matrix IS the Gram matrix of zero evaluations,")
    print("  CCCLXXXIII).  A non-circular proof needs (SV) derived"
          " from the source side: see the price below.")

    # Suzuki host
    print("  SUZUKI HOST (v630 S1 / v643 P1: A_a = Friedrichs of"
          " D*G_aD; hat compression = Toeplitz(t_row)/delta):")
    suz_tracks = None
    for x in SUZ_X:
        row, n, delta = suz_lag_row(x, DELTA_GRID)
        M = sp_toeplitz(row)
        gc_ref = SL.build_grid_cell(x, DELTA_GRID)
        ev_ref = float(np.linalg.eigvalsh(M)[0])
        a8 = abs(ev_ref - gc_ref["tau"]) / max(abs(gc_ref["tau"]), 1e-300)
        check("A8 Suzuki lag row == record grid builder (x=%d)" % x,
              a8 <= 1e-9, "lam_min rel dev %.2e" % a8)
        T3 = np.diag(np.full(n, 2.0 / 3.0)) \
            + np.diag(np.full(n - 1, 1.0 / 6.0), 1) \
            + np.diag(np.full(n - 1, 1.0 / 6.0), -1)
        w = sp_eigh(M, T3, eigvals_only=True)
        mu = w / (delta * delta)
        pos = mu[mu > 0]
        neg = mu[mu <= 0]
        smu = np.sqrt(np.sort(pos))
        gg = gammas[:5]
        track = (float(np.max(np.abs(smu[:5] - gg) / gg))
                 if len(smu) >= 5 else float("inf"))
        if suz_tracks is None:
            suz_tracks = track <= SUZ_TRACK_BAR
        else:
            suz_tracks &= track <= SUZ_TRACK_BAR
        pin_pos = {s: float(np.sum(2.0 * s / (pos + s * s)))
                   for s in (1.0, 2.0)}
        pin_neg = {s: float(np.sum(2.0 * s / (neg + s * s)))
                   for s in (1.0, 2.0)}
        print("    x=%-3d n=%4d mu<0: %d (pin mass %.3e at sigma=1)"
              "  first sqrt(mu): %s"
              % (x, n, len(neg), pin_neg[1.0],
                 " ".join("%.3f" % v for v in smu[:6])))
        print("          vs gamma_k:      %s   max rel track dev"
              " (first 5) = %.3f"
              % (" ".join("%.3f" % v for v in gg[:6]), track))
        print("          P_suz(1) = %.4e vs tgt %.4e | P_suz(2)"
              " = %.4e vs tgt %.4e"
              % (pin_pos[1.0] + pin_neg[1.0], tgt.get(1.0, tgt1),
                 pin_pos[2.0] + pin_neg[2.0], tgt[2.0]))
    suz_line = ("SUZPIN-TRACKS" if suz_tracks
                else "SUZPIN-FORM-SPECTRUM(the hat compression of"
                " A_a reads Weil-form margins, not ordinate squares)")
    print("    SUZ verdict: %s" % suz_line)
    print("  PRICE of the non-circular route (source-side (SV)):")
    print("    operator: Suzuki's A_a (screw function g exact in the"
          " corpus: v630 S1 atom identity, v643 convention lock +")
    print("    W1 measure-level theorem) -- but the pins need the"
          " KREIN INVERSE-SPECTRAL step (canonical system / Weyl")
    print("    m-function of g), which the corpus does NOT have;"
          " norm: || (A_a + sigma^2)^{-1} - (A + sigma^2)^{-1} ||_tr")
    print("    -> 0 uniformly on sigma >= 1/2 + eps; known bound in"
          " corpus: NONE (v714-v719 J_K truncations track ordinates")
    print("    only to ~2.4e-2 with spurious pole/UV bands; v643's"
          " smooth-layer conversion profile is measured non-scalar).")

    # ================================================================
    section("VII. COMPOSITE VERDICT")
    wall = time.time() - T0_WALL
    check("A9 runtime", wall <= RUNTIME_BAR, "%.1f s" % wall)
    instrument_ok = all(ok for _n, ok, _d in CHECKS)
    t1_ok = all(ok for name, ok, _d in CHECKS if name.startswith("T1"))
    skeleton = ("SVPIN-SKELETON-SOUND(conditional on the CF"
                " realness hypothesis; all content in (SV))"
                if t1_ok else "SVPIN-SKELETON-GAP(failed T1 gate)")
    conv_line = ("SVPIN-CONVERGES" if n_conv >= 12 and n_div == 0
                 else "SVPIN-DIVERGES" if n_div >= 8
                 else "SVPIN-PLATEAUS")
    sep_line = ("SVPIN-SEPARATES"
                if sep_fail <= 1 and guard_fail == 0
                else "SVPIN-WORLD-BLIND")
    disg = n_reloc >= DISGUISE_ROWS
    if not instrument_ok:
        verdict = "SVPIN-INSTRUMENT-EDGE"
    elif not t1_ok:
        verdict = "SVPIN-SKELETON-GAP(see failed T1 gate)"
    elif n_div >= 8:
        verdict = "SVPIN-DIVERGES"
    elif sep_fail >= 2 or guard_fail > 0:
        verdict = "SVPIN-WORLD-BLIND"
    elif disg:
        verdict = "SVPIN-DISGUISE(tau-relocation on %d rows)" % n_reloc
    elif n_conv < 12:
        verdict = ("SVPIN-PLATEAUS(%d CONV / %d PLAT / %d DIV)"
                   % (n_conv, n_plat, n_div))
    else:
        med_slope = float(np.median([slopes_nt[s] for s in SIGMAS]))
        verdict = ("SVPIN-ROUTE-OPEN(NT rows %d CONV / %d PLAT /"
                   " %d DIV, median slope %+.2f; remaining analytic"
                   " task = prove (SV) source-side: a uniform"
                   " trace-class/resolvent bound for a source-only"
                   " family in sigma >= 1/2 + eps -- for the extremal"
                   " family the statement is Z1-transcribed, so the"
                   " honest carrier is the Suzuki/Krein inverse-"
                   "spectral realization priced in VI)"
                   % (n_conv, n_plat, n_div, med_slope))

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n  sub-verdicts: %s" % skeleton)
    print("                %s (NT primary; FULL row reported)"
          % conv_line)
    print("                %s (metric B; metric A reported honestly)"
          % sep_line)
    print("                %s"
          % ("SVPIN-DISGUISE" if disg
             else "no disguise (tau-screen flat, no Christoffel,"
             " no zero consumption)"))
    print("                SVPIN-Z1-TRANSCRIPTION(%s)"
          % ("confirmed" if z1_ok else "NOT confirmed"))
    print("                %s" % suz_line)
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    print("VERDICT: %s" % verdict)
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("NO RH CLAIM. NO POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
