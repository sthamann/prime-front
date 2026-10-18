#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""coupling_ansatz_probe -- PRIME.STAGE1.COUPLING.01: the first direct
test of geometric COUPLING ansaetze against the measured cross-piece
cancellation debt of the Stage-1 host (round 115 breakage
BRK-A1-CROSSTERMS).

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  NO RH CLAIM.  This probe
proves nothing about RH in any direction.  Round 115
(stage1_construction_probe.py, STAGE1-BREAKAGE-LOCATED) measured that
the Stage-1 host's positivity lives ONLY in cross-piece cancellation:
the pole/Gamma/prime Pick pieces at N=4 have lambda_min = -1.3e-2 /
-2.39 / -1.82 individually while the total floor is ~1.1e-14 -- 14.60
decimal digits of cancellation at N=4, growing ~6 digits per rung; a
direct sum supplies exactly ZERO of them; the transverse datum is
pinned (|theta-1/2| <= 3.3e-10; Theta+Theta*=I IS that datum).  The
refined milestone demands a geometric coupling that supplies the
cancellation STRUCTURALLY.  This probe BUILDS three coupling ansaetze
and adjudicates each against exact targets.

===========================================================================
THE ANSATZ BATTERY
===========================================================================
C1 -- CROSSED-PRODUCT / ADELE-CLASS (EISENSTEIN) LIFT.  Connes' map
   E(f)(x) = |x|^{1/2} sum_{n>=1} f(nx) on the class-space surrogate
   (0,infty).  DERIVED HERE AND GATED: on L^2((0,infty), dx/x) the
   half-density lift E = sum_n n^{-1/2} U_n (U_n u(x) = u(nx)) is
   Mellin-DIAGONAL with multiplier m(tau) = zeta(1/2 - i tau); the
   corpus node vectors are v_j(tau) = 1/(sigma_j + i tau) (Mellin of
   x^{-sigma_j} 1_{x>=1}), ambient Gram = Cauchy 1/(sigma_j+sigma_k).
   (a) The x-space lift is built LITERALLY on a discretized
       fundamental domain (Muentz-subtracted, integers only) and
       welded to the multiplier picture (instrument).
   (b) The NAIVE completion: the plain L^2 Gram of the lifted vectors
       is the |zeta|^2-weighted second-moment form
       (1/2pi) int |zeta(1/2+i tau)|^2 /((sigma_j - i tau)(sigma_k + i
       tau)) d tau -- a PSD object which is NOT the Pick matrix; the
       defect is measured and shown to FLOOR OUT under refinement:
       this is the wall in naive lift coordinates, in numbers.
   (c) THE COKERNEL/QUOTIENT COUPLING (the priority): the range of E
       is m * (test space); its orthogonal complement in the
       delta-weighted completion H^1_ell,omega (inner product
       int omega (u v~ + ell^2 u' v~')) is spanned by reproducing-
       kernel bumps AT THE ZEROS of m -- zeros never input, they
       emerge from the geometry.  The quotient Gram of the node
       vectors is predicted = 2*ell * T_omega with
       T_omega[j,k] = sum_{|gamma|<=T} omega(gamma) *
                      (pair) 1/((sigma_j - i gamma)(sigma_k + i gamma)),
       computed SOURCE-ONLY by a box-contour integral of
       (xi'/xi)(1/2+z) (own Euler--Maclaurin; no zero location, no
       cache, no mp.zeta).  A quotient Gram is automatically PSD: if
       it reproduces the truncated Pick block, the cancellation is
       STRUCTURAL in that completion and the open question sharpens to
       the completion datum (which Hilbert norm makes E isometric).
       Fitness: defect vs T_omega along ladders in ell (RK scale),
       basis density, grid step, arithmetic truncation X of the
       multiplier (integer currency), Euler-product truncation (prime
       currency -- measured to FAIL on the line), plus smooth and
       scrambled controls THROUGH THE SAME LIFT and the Z1 screen (the
       cache-transcribed integrand has NO poles in the box: its
       readout is exactly zero -- the coupling readout cannot be
       transcribed, only resummed).
C2 -- THETA / WEIL-REPRESENTATION (METAPLECTIC) LIFT.  The finite
   surrogate of the theta coupling: squared dilations
   E_2 = sum_n n^{-1/2} U_{n^2}, multiplier m_2(tau) =
   zeta(1/2 - 2 i tau), zeros at tau = gamma/2 (doubled spectral
   density).  RAW fitness vs the C1 target (measured MISS = the
   metaplectic mismatch) and MATCHED fitness with the doubled test
   family w_j(tau) = 1/(sigma_j + 2 i tau) vs its own box target
   (the dictionary: theta lift == C1 conjugated by the square flow).
C3 -- HALF-DENSITY SUSPENSION + PROLATE (ARCHIMEDEAN ORBIT) COUPLING.
   The round-115 suspension with theta = 1/2 forced; the transverse
   fixed-point datum at the degenerate orbit is the Connes--Consani
   archimedean (prolate) positivity, arXiv:2006.13771 (proved: the
   Weil form restricted to test functions supported in the sqrt2
   window is positive).  Measured here in corpus Weil-window currency:
   (i)   the arch-only (pole+Gamma) window Gram is PSD for
         autocorrelation support < log 2 (their theorem's corpus
         image) and its wall is located by bisection -- cross-currency
         confirmation of the r115 Schur exit r = 0.732 (overhang
         +0.039 past log 2);
   (ii)  the FIRST PRIME ATOM at log 2 rescues positivity past the
         arch wall (the coupled true form stays PSD where arch-only
         dies): the orbit-coupling residual measured at the first
         atom;
   (iii) the degenerate orbit's spectral density (Re psi(1/4+i tau/2)/2
         - log(pi)/2)/pi equals the mean zero-counting density (RvM)
         -- the structural role of the archimedean orbit is to supply
         the MEAN density the primes oscillate around (welded);
   (iv)  the c*-packet accounting at the N=4 floor: piece
         contributions of the ground eigenvector, the PNT/smooth
         (density-level) replacement residual -- how many of the 14.60
         digits the density-level coupling supplies vs what the
         oscillation coupling still owes; zero-side band masses
         (consistency, resolution-limited at the declared box bar).

===========================================================================
FITNESS DISCIPLINE (frozen)
===========================================================================
* exact targets: the certified Euler--Pick floors N<=4 (warded
  verbatim from the owning logs), the r115 piece decomposition and
  debt digits (reproduced at declared bars), box-contour truncated
  zero-side blocks with dual-resolution quadrature gates and integer
  zero-count gates;
* the Z1 screen: a coupling that transcribes the cache is dead on
  arrival (measured: the cache integrand readout is quadrature-zero
  in the coupling currency; the EM continuation is a resummation,
  deviation from raw partial sums measured);
* controls: smooth (integers -> Lebesgue, multiplier 1/(s-1), no
  zeros) and position-scrambled (golden permutation of dilation
  lengths, weights kept) worlds pushed THROUGH THE SAME LIFT must
  miss the target by measured factors;
* cancellation accounting: per ansatz, how many digits the structure
  supplies (a quotient Gram supplies the SIGN exactly -- all
  cancellation digits structurally -- at measured entry defect;
  magnitude reproduction is limited by the measured defect and the
  instrument bars, reported honestly per rung N=2,3,4).

===========================================================================
DECLARED NUMERICS / SUBSAMPLING (frozen before the adjudication run)
===========================================================================
mp: DPS=100 pins/floors/pieces (mp.eigsy), EM cutoff 96/28 vs 128/32
stability gate at 1e-70.  numpy: own vectorized Euler--Maclaurin
zeta/zeta' (M=250 contour / M=400 emission line, K=12 Bernoulli
terms), own complex digamma (shift 32 + asymptotic), gated against mp
at 1e-10/1e-12.  Box contours at c = 0.45 (inside |Re z| < 1/2: the
z = +-1/2 poles of the pole factor and ALL trivial-zero poles are
outside), heights chosen SOURCE-ONLY as argmax |zeta(1/2+i tau)| on
declared scan windows [58,64] (T*), [123,129] (T2, C2), [16,20],
[38.5,40.5] (bands); vertical step 0.004 primary with dual-step gate;
zero-count integral must be integer to 2e-4.  Coker grids
tau in [-T*,T*], dtau = 0.015 (0.010 at the finest rung; stability
gate at ell = 0.4, dtau = 0.0075), basis = global hats at spacing
0.5*ell plus 24 Cauchy atoms plus SOURCE-ONLY adaptive dip
refinement (fine hats at spacing 2*dtau on windows +-min(3*ell,1.0)
around local minima of |m| below 0.35*median: the multiplier's own
dips, zero locations never input), ridge 1e-11 on normalized
normal equations (gated vs lstsq on the no-refinement config), ambient
weight omega(tau) = (Omega^2/(Omega^2+tau^2))^2, Omega = 25 (ladder
rung 40 report-only; omega's analytic continuation
(Omega^2/(Omega^2-z^2))^2 has poles only at z = +-Omega, far outside
the box).  ell ladder {0.8, 0.4, 0.2}; arithmetic multiplier ladder
X in {30, 60, 120} as the EM-smoothed partial sum (two Bernoulli
terms declared -- the integer-currency refinement axis); Euler-product
rungs x_p in {20, 100}.  Emission grid tau <= 200 (dtau 0.005) with
declared mean-|zeta|^2 tail model (log(tau/2pi) + 2*euler_gamma),
model bar 20 percent of tail.  x-space lift grid u in [-8,8],
du = 0.004 (refine 0.008), Muentz-subtracted, exact staircase via own
zeta(a) and prefix sums, analytic tails beyond |u| = 8.  C3: v-grid
dv = 2.5e-4 on [-0.45,0.45], FFT cross-correlations (gated vs direct
convolution once), log-u Gamma-integrator 12000 points on [1e-8, 45]
(guard rewrite over the common 1-e^{-2u} denominator; sub-1e-8 mass
declared < |limit|*1e-8), hats nb = 21 per window, PSD tolerance
1e-9 * ||M||, wall bisection to 0.005.  Frozen r115 reads:
FROZEN_DEBT_DIGITS = (1.07, 5.23, 9.61, 14.60) at N=1..4 (growth to
37.43 at N=8), FROZEN_PIECES_4 = (-1.3e-2, -2.39, -1.82),
FROZEN_ARCH_EXIT = 0.732.  Pin nodes sigma_j = 1 + 1/j.  Golden
scramble (sqrt(5)-1)/2, deterministic, no randomness anywhere.
Runtime bar 900 s.

===========================================================================
VERDICT ENUM (frozen, exactly one composite)
===========================================================================
  COUPLING-STRUCTURAL(ansatz named)   an ansatz's quotient Gram
      reproduces the truncated Pick block at defect <= 3e-2, the
      defect collapsing on the discretization ratio dtau/ell
      (equal-ratio configs agree to 25 percent: cross-talk
      subdominant), normalization within 15 percent of the RK
      prediction 2*ell, PSD exact, controls missing by the declared
      factors and Z1 clean -- the cancellation is structural in the
      named completion; the open requirement sharpens to the
      completion datum (measured normalization + IR limit).
  COUPLING-DEFECT-FLOORS(measured)    every ansatz's defect floors
      out above the bar under all declared refinements: the wall in
      lift coordinates, with the floor value per ansatz.
  COUPLING-UNBUILDABLE(why)           a declared construction step
      cannot be stated/computed at the declared bars.
  COUPLING-INSTRUMENT-EDGE            an instrument/ward gate fails
      (exit 1, not a mathematical verdict).

Writes stdout only.  No verification/, no ledger, no manifest, no
website.  Reads only the declared ARTIFACTS allowlist (read-only).
NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import time

import mpmath as mp
import numpy as np

T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

ARTIFACTS = {
    "ep_log": "experiments/tfpt-discovery/eulerpick_ladder_frozen.log",
    "s4_log": "experiments/tfpt-discovery/sieve4_run1.log",
    "krein": "experiments/tfpt-discovery/krein_screw_realization_probe.py",
    "cohomspec": "experiments/tfpt-discovery/cohomspec_probe.py",
    "vbk": "experiments/tfpt-discovery/vbk_invariant_probe.py",
    "stage1": "experiments/tfpt-discovery/stage1_construction_probe.py",
}

# ---------------------------------------------------------------- frozen
PIN_COUNT = 8
CERTIFIED = {
    1: (4.5917135e-2, 4.5917136e-2),
    2: (9.0288701e-6, 9.0289075e-6),
    3: (2.3643695e-10, 1.1497752e-9),
    4: (8.278338e-15, 1.3840906e-14),
}
FROZEN_DEBT_DIGITS = (1.07, 5.23, 9.61, 14.60)
FROZEN_DEBT_N8 = 37.43
FROZEN_PIECES_4 = (-1.3e-2, -2.39, -1.82)   # pole / Gamma / prime
FROZEN_ARCH_EXIT = 0.732                     # r115 B8 Schur currency
LOG2 = math.log(2.0)
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
EULER_GAMMA = 0.5772156649015328606

DPS = 100
BOX_C = 0.45
BOX_DT = 0.004
OMEGA = 25.0
ELL_LADDER = (0.8, 0.4, 0.2)
DTAU = 0.015
DTAU_FINE = 0.010
X_LADDER = (30, 60, 120)
XP_LADDER = (20, 100)
EMIT_TMAX = 200.0
EMIT_DT = 0.005
XGRID_U = 8.0
XGRID_DU = 0.004
RIDGE = 1e-11
DEFECT_BAR = 3e-2
NORM_BAR = 0.15
RUNTIME_BAR = 900.0
N_CHECKS_EXPECTED = 39

CHECKS: list[tuple[str, bool, str]] = []
ARTIFACT_TEXT: dict[str, str] = {}


def check(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    CHECKS.append((name, result, detail))
    print("  [%s] %-46s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print("%s   [t=%.1f s]" % (title, time.time() - T0))
    print("=" * 78)


def fmt(x, digits: int = 8) -> str:
    return mp.nstr(x if isinstance(x, mp.mpf) else mp.mpf(x), digits,
                   min_fixed=0, max_fixed=0)


def read_artifact(key: str) -> str:
    """The ONLY repository read path.  Allowlist enforced."""
    if key not in ARTIFACTS:
        raise RuntimeError("artifact not in allowlist: %s" % key)
    if key in ARTIFACT_TEXT:
        return ARTIFACT_TEXT[key]
    path = os.path.join(ROOT, ARTIFACTS[key])
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        ARTIFACT_TEXT[key] = fh.read()
    return ARTIFACT_TEXT[key]


def ward(key: str, tokens: list[str]) -> tuple[bool, list[str]]:
    text = read_artifact(key)
    missing = [token for token in tokens if token not in text]
    return not missing, missing


# ---------------------------------------------------------------- firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        source = fh.read()
    tree = ast.parse(source)
    bad: list[str] = []
    allowed_roots = {"__future__", "ast", "hashlib", "math", "os", "time",
                     "mpmath", "numpy"}
    forbidden_calls = {"load", "loadtxt", "genfromtxt", "fromfile",
                       "zetazero", "zetazeros", "nzeros", "siegelz",
                       "siegeltheta"}
    forbidden_attrs = {"zeta", "zetazero", "zetazeros", "nzeros", "siegelz",
                       "siegeltheta"}
    open_scopes: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in allowed_roots:
                    bad.append("import:" + alias.name)
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] not in allowed_roots:
                bad.append("from:" + (node.module or ""))
        elif isinstance(node, ast.Call):
            called = (node.func.id if isinstance(node.func, ast.Name)
                      else node.func.attr
                      if isinstance(node.func, ast.Attribute) else "")
            if called.lower() in forbidden_calls:
                bad.append("call:" + called)
        elif isinstance(node, ast.Attribute):
            if node.attr.lower() in forbidden_attrs:
                bad.append("attr:" + node.attr)
    for fn in ast.walk(tree):
        if isinstance(fn, ast.FunctionDef):
            for node in ast.walk(fn):
                if (isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Name)
                        and node.func.id == "open"):
                    open_scopes.append(fn.name)
    stray = [name for name in open_scopes
             if name not in ("read_artifact", "firewall_audit")]
    if stray:
        bad.append("open-outside-allowlist:%s" % stray)
    return not bad, "violations=%s" % (bad or "none")


# ------------------------------------------- Euler--Maclaurin source (mp)
LOGDERIV_CACHE: dict[tuple[str, int], mp.mpf] = {}


def dirichlet_logderivative(s, cutoff: int, terms: int):
    total = mp.mpf(0)
    derivative = mp.mpf(0)
    for n in range(1, cutoff):
        power = mp.power(n, -s)
        total += power
        derivative -= mp.log(n) * power
    M = mp.mpf(cutoff)
    logM = mp.log(M)
    lead = M ** (1 - s) / (s - 1)
    total += lead
    derivative += lead * (-logM - 1 / (s - 1))
    half = mp.mpf("0.5") * M ** (-s)
    total += half
    derivative -= logM * half
    for k in range(1, terms + 1):
        order = 2 * k - 1
        rising = mp.rf(s, order)
        coefficient = mp.bernpoly(2 * k, 0) / mp.factorial(2 * k)
        correction = coefficient * rising * M ** (-s - order)
        harmonic = mp.fsum(1 / (s + j) for j in range(order))
        total += correction
        derivative += correction * (harmonic - logM)
    return total, derivative


def zeta_logderiv(s, cutoff: int = 96, terms: int = 28):
    key = (mp.nstr(s, 40), mp.mp.dps)
    if key in LOGDERIV_CACHE and cutoff == 96 and terms == 28:
        return LOGDERIV_CACHE[key]
    value, derivative = dirichlet_logderivative(s, cutoff, terms)
    out = derivative / value
    if cutoff == 96 and terms == 28:
        LOGDERIV_CACHE[key] = out
    return out


def em_zeta_value(s, cutoff: int = 96, terms: int = 28):
    value, _ = dirichlet_logderivative(s, cutoff, terms)
    return value


def h_pole(sigma):
    s = mp.mpf("0.5") + sigma
    return 1 / s + 1 / (s - 1)


def h_gamma(sigma):
    s = mp.mpf("0.5") + sigma
    return mp.digamma(s / 2) / 2 - mp.log(mp.pi) / 2


def pin_reference(sigma):
    return h_pole(sigma) + h_gamma(sigma) + zeta_logderiv(mp.mpf("0.5")
                                                          + sigma)


def pick_matrix(values, sigmas):
    n = len(values)
    matrix = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            matrix[j, k] = (values[j] + values[k]) / (sigmas[j] + sigmas[k])
    return matrix


def eig_range(matrix):
    eigenvalues = mp.eigsy(matrix, eigvals_only=True)
    absmax = max(abs(eigenvalues[i]) for i in range(matrix.rows))
    return eigenvalues[0], absmax


# ------------------------------------------- numpy Euler--Maclaurin zeta
BERN2K = (1.0 / 6, -1.0 / 30, 1.0 / 42, -1.0 / 30, 5.0 / 66,
          -691.0 / 2730, 7.0 / 6, -3617.0 / 510, 43867.0 / 798,
          -174611.0 / 330, 854513.0 / 138, -236364091.0 / 2730)


def np_zeta_pair(s: np.ndarray, cutoff: int = 250,
                 terms: int = 12) -> tuple[np.ndarray, np.ndarray]:
    """Own vectorized EM continuation: returns (zeta(s), zeta'(s))."""
    s = np.asarray(s, dtype=complex)
    flat = s.ravel()
    z = np.zeros(flat.shape, dtype=complex)
    dz = np.zeros(flat.shape, dtype=complex)
    n = np.arange(1, cutoff, dtype=float)
    lg = np.log(n)
    chunk = 4000
    for lo in range(0, flat.size, chunk):
        sc = flat[lo:lo + chunk, None]
        P = np.exp(-sc * lg[None, :])
        z[lo:lo + chunk] = P.sum(axis=1)
        dz[lo:lo + chunk] = -(P * lg[None, :]).sum(axis=1)
    logM = math.log(cutoff)
    lead = np.exp((1.0 - flat) * logM) / (flat - 1.0)
    z += lead
    dz += lead * (-logM - 1.0 / (flat - 1.0))
    half = 0.5 * np.exp(-flat * logM)
    z += half
    dz += -logM * half
    rising = flat.copy()          # (s)_1
    harm = 1.0 / flat             # sum_{j<1} 1/(s+j)
    for k in range(1, terms + 1):
        order = 2 * k - 1
        coeff = BERN2K[k - 1] / math.factorial(2 * k)
        term = coeff * rising * np.exp(-(flat + order) * logM)
        z += term
        dz += term * (harm - logM)
        rising = rising * (flat + order) * (flat + order + 1)
        harm = harm + 1.0 / (flat + order) + 1.0 / (flat + order + 1)
    return z.reshape(s.shape), dz.reshape(s.shape)


def np_digamma(z: np.ndarray) -> np.ndarray:
    """Own complex digamma: 32-step recurrence + asymptotic series."""
    z = np.asarray(z, dtype=complex)
    res = np.zeros_like(z)
    zz = z.copy()
    for _ in range(32):
        res -= 1.0 / zz
        zz = zz + 1.0
    inv = 1.0 / zz
    inv2 = inv * inv
    res += np.log(zz) - 0.5 * inv
    coeffs = (1.0 / 12, -1.0 / 120, 1.0 / 252, -1.0 / 240, 1.0 / 132,
              -691.0 / 32760, 1.0 / 12)
    p = inv2.copy()
    for c in coeffs:
        res -= c * p
        p = p * inv2
    return res


def np_xi_logderiv(z: np.ndarray, cutoff: int = 250) -> np.ndarray:
    """(xi'/xi)(1/2+z), own EM + own digamma, vectorized."""
    s = 0.5 + np.asarray(z, dtype=complex)
    zeta_v, dzeta_v = np_zeta_pair(s, cutoff=cutoff)
    return (1.0 / s + 1.0 / (s - 1.0) - 0.5 * math.log(math.pi)
            + 0.5 * np_digamma(s / 2.0) + dzeta_v / zeta_v)


# ------------------------------------------------------- box contours
def scan_height(lo: float, hi: float) -> float:
    """SOURCE-ONLY height choice: argmax |zeta(1/2+i tau)| on [lo,hi]."""
    taus = np.arange(lo, hi, 0.02)
    vals, _ = np_zeta_pair(0.5 + 1j * taus, cutoff=250)
    return float(taus[int(np.argmax(np.abs(vals)))])


def box_nodes(T: float, c: float, dt: float,
              dx: float = 0.005) -> tuple[np.ndarray, np.ndarray]:
    """Counterclockwise rectangle |Re z|<=c, |Im z|<=T: nodes, dz-weights."""
    tv = np.arange(-T, T + dt / 2, dt)
    wt = np.full(tv.shape, dt)
    wt[0] = wt[-1] = dt / 2
    xv = np.arange(-c, c + dx / 2, dx)
    wx = np.full(xv.shape, dx)
    wx[0] = wx[-1] = dx / 2
    nodes = np.concatenate([
        c + 1j * tv,               # right, upward
        xv[::-1] + 1j * T,         # top, right->left
        -c + 1j * tv[::-1],        # left, downward
        xv - 1j * T,               # bottom, left->right
    ])
    weights = np.concatenate([1j * wt, -wx, -1j * wt, wx])
    return nodes, weights


class BoxData:
    """Holds contour nodes, weights and the xi'/xi values (computed once)."""

    def __init__(self, T: float, dt: float, cutoff: int = 250):
        self.T = T
        self.nodes, self.weights = box_nodes(T, BOX_C, dt)
        self.F = np_xi_logderiv(self.nodes, cutoff=cutoff)

    def integrate(self, kernel_vals: np.ndarray) -> complex:
        return complex(np.sum(self.weights * self.F * kernel_vals)
                       / (2j * math.pi))

    def integrate_plain(self, kernel_vals: np.ndarray,
                        Fvals: np.ndarray) -> complex:
        return complex(np.sum(self.weights * Fvals * kernel_vals)
                       / (2j * math.pi))

    def zero_count(self) -> float:
        return float(np.real(np.sum(self.weights * self.F)
                             / (2j * math.pi)))


def omega_line(tau: np.ndarray, om: float = OMEGA) -> np.ndarray:
    return (om * om / (om * om + tau * tau)) ** 2


def omega_analytic(z: np.ndarray, om: float = OMEGA) -> np.ndarray:
    return (om * om / (om * om - z * z)) ** 2


def target_block(box: BoxData, sig: list[float], om: float = OMEGA,
                 half_speed: bool = False,
                 matched: bool = False) -> np.ndarray:
    """T_omega[j,k] via the box: kernels
    C1        : omega(z) / ((sigma_j - z)(sigma_k + z))
    C2 raw    : omega(z/2)/((sigma_j + z/2)(sigma_k - z/2))
    C2 matched: omega(z/2)/((sigma_j + z)(sigma_k - z))."""
    n = len(sig)
    z = box.nodes
    if half_speed:
        w = omega_analytic(z / 2.0, om)
    else:
        w = omega_analytic(z, om)
    out = np.zeros((n, n))
    for j in range(n):
        for k in range(j, n):
            if half_speed and not matched:
                ker = w / ((sig[j] + z / 2.0) * (sig[k] - z / 2.0))
            elif half_speed and matched:
                ker = w / ((sig[j] + z) * (sig[k] - z))
            else:
                ker = w / ((sig[j] - z) * (sig[k] + z))
            val = box.integrate(ker)
            out[j, k] = out[k, j] = val.real
            if abs(val.imag) > 1e-7:
                out[j, k] = out[k, j] = float("nan")
    return out


# ------------------------------------------------------- coker machinery
def hat_columns(tau: np.ndarray, spacing: float, T: float) -> np.ndarray:
    centers = np.arange(-T + spacing, T - spacing / 2, spacing)
    cols = 1.0 - np.abs(tau[:, None] - centers[None, :]) / spacing
    np.clip(cols, 0.0, None, out=cols)
    return cols


ATOM_BETAS = (0.6, 0.8, 1.0, 13.0 / 12, 9.0 / 8, 1.2, 1.25, 4.0 / 3,
              1.5, 2.0, 2.5, 3.0)


def atom_columns(tau: np.ndarray) -> np.ndarray:
    cols = []
    for beta in ATOM_BETAS:
        cols.append(1.0 / (beta + 1j * tau))
        cols.append(1.0 / (beta - 1j * tau))
    return np.stack(cols, axis=1)


def embed(vecs: np.ndarray, omega: np.ndarray, ell: float,
          dtau: float) -> np.ndarray:
    """H^1_{ell,omega} isometric embedding: value + derivative channel."""
    top = vecs * np.sqrt(omega * dtau)[:, None]
    der = np.diff(vecs, axis=0) / dtau
    om_mid = 0.5 * (omega[:-1] + omega[1:])
    bot = ell * der * np.sqrt(om_mid * dtau)[:, None]
    return np.concatenate([top, bot], axis=0)


def dip_windows(m_vals: np.ndarray, tau: np.ndarray,
                ell: float) -> list[tuple[float, float]]:
    """SOURCE-ONLY adaptive refinement windows: local minima of |m|
    below 0.35 * median (the multiplier's own dips; zeros never
    input), merged at radius 0.25, window +-min(3*ell, 1.0)."""
    a = np.abs(m_vals)
    med = float(np.median(a))
    idx = np.where((a[1:-1] < a[:-2]) & (a[1:-1] <= a[2:])
                   & (a[1:-1] < 0.35 * med))[0] + 1
    centers: list[float] = []
    for i in idx:
        t = float(tau[i])
        if not centers or t - centers[-1] > 0.25:
            centers.append(t)
    half = min(3.0 * ell, 1.0)
    return [(c - half, c + half) for c in centers]


def dip_columns(tau: np.ndarray, windows: list[tuple[float, float]],
                dtau: float) -> np.ndarray:
    """Fine hats (spacing 2*dtau) on the refinement windows."""
    cols = []
    sp = 2.0 * dtau
    for lo, hi in windows:
        centers = np.arange(lo, hi + sp / 2, sp)
        c = 1.0 - np.abs(tau[:, None] - centers[None, :]) / sp
        np.clip(c, 0.0, None, out=c)
        cols.append(c)
    if not cols:
        return np.zeros((len(tau), 0))
    return np.concatenate(cols, axis=1)


def coker_gram(m_vals: np.ndarray, node_vecs: np.ndarray,
               tau: np.ndarray, dtau: float, ell: float,
               spacing: float, om: float = OMEGA,
               use_lstsq: bool = False, refine: bool = True) -> np.ndarray:
    """Gram of the projections of node_vecs onto coker(m * basis) in
    H^1_{ell,omega}; returns Ghat / (2*ell) (the RK-normalized block)."""
    T = float(tau[-1])
    omega = omega_line(tau, om)
    parts = [hat_columns(tau, spacing, T).astype(complex),
             atom_columns(tau)]
    if refine:
        parts.append(dip_columns(tau, dip_windows(m_vals, tau, ell),
                                 dtau).astype(complex))
    basis = np.concatenate(parts, axis=1)
    basis = basis * m_vals[:, None]
    A = embed(basis, omega, ell, dtau)
    V = embed(node_vecs, omega, ell, dtau)
    norms = np.sqrt(np.sum(np.abs(A) ** 2, axis=0))
    norms[norms == 0] = 1.0
    A = A / norms[None, :]
    if use_lstsq:
        coef, *_ = np.linalg.lstsq(A, V, rcond=1e-10)
    else:
        G = A.conj().T @ A
        G[np.diag_indices_from(G)] += RIDGE
        coef = np.linalg.solve(G, A.conj().T @ V)
    resid = V - A @ coef
    return (resid.conj().T @ resid) / (2.0 * ell)


def rel_defect(G: np.ndarray, Ttarget: np.ndarray) -> float:
    return float(np.linalg.norm(np.real(G) - Ttarget)
                 / np.linalg.norm(Ttarget))


# ------------------------------------------------------- small sieve
def sieve_small(limit: int) -> list[int]:
    bits = bytearray(b"\x01") * (limit + 1)
    bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            count = (limit - p * p) // p + 1
            bits[p * p:limit + 1:p] = b"\x00" * count
    return [i for i in range(2, limit + 1) if bits[i]]


def mangoldt_array(limit: int) -> np.ndarray:
    lam = np.zeros(limit + 1)
    for p in sieve_small(limit):
        q = p
        while q <= limit:
            lam[q] = math.log(p)
            q *= p
    return lam


# ------------------------------------------------------- C3 machinery
ULOG_N = 12000
ULOG = np.exp(np.linspace(math.log(1e-8), math.log(45.0), ULOG_N))


def gamma_pair_grid(g_vals: np.ndarray, g0: float) -> float:
    """<mu_Gamma, g> = int_0^inf [g(0)e^{-2u}/(2u) - g(u)e^{-u/2}/
    (1-e^{-2u})] du  -  g(0) log(pi)/2, on the frozen log-u grid.
    g_vals = g evaluated on ULOG (zero beyond support)."""
    u = ULOG
    A = -np.expm1(-2.0 * u)                       # 1 - e^{-2u}, stable
    bracket = g0 * np.exp(-2.0 * u) * (A / (2.0 * u)) \
        - g_vals * np.exp(-u / 2.0)
    integrand = bracket / A
    val = float(np.trapezoid(integrand * u, np.log(u)))
    return val - g0 * 0.5 * math.log(math.pi)


def pole_pair_grid(g_vals: np.ndarray) -> float:
    """<mu_pole, g> = int_0^inf 2 cosh(u/2) g(u) du on ULOG."""
    return float(np.trapezoid(2.0 * np.cosh(ULOG / 2.0) * g_vals * ULOG,
                          np.log(ULOG)))


class WindowForm:
    """Weil window form on hat packets of half-support w_f."""

    def __init__(self, dv: float = 2.5e-4, vmax: float = 0.45,
                 nb: int = 21):
        self.dv = dv
        self.vmax = vmax
        self.nb = nb
        self.v = np.arange(-vmax, vmax + dv / 2, dv)
        self.nfft = 16384

    def basis(self, w_f: float) -> np.ndarray:
        hw = 2.0 * w_f / (self.nb + 1)
        centers = -w_f + hw + np.arange(self.nb) * hw
        F = 1.0 - np.abs(self.v[:, None] - centers[None, :]) / hw
        np.clip(F, 0.0, None, out=F)
        return F

    def correlations(self, F: np.ndarray) -> np.ndarray:
        """g_ab(t>=0) for all pairs on the t-grid k*dv, via FFT."""
        FT = np.fft.rfft(F, n=self.nfft, axis=0)
        nb = F.shape[1]
        nt = self.nfft // 2
        out = np.empty((nb, nb, nt))
        for a in range(nb):
            spec = np.conj(FT[:, a:a + 1]) * FT
            cc = np.fft.irfft(spec, n=self.nfft, axis=0) * self.dv
            # cc[k] = sum_i F[i,a] F[i+k,b] dv  (correlation at lag +k)
            sym = 0.5 * (cc[:nt] + np.roll(cc[::-1], 1, axis=0)[:nt])
            out[a] = sym.T
        return out

    def gram(self, w_f: float, prime_mode: str) -> np.ndarray:
        """prime_mode: 'none' (arch-only), 'true' (atoms), 'smooth'."""
        F = self.basis(w_f)
        corr = self.correlations(F)
        nb = self.nb
        tgrid = np.arange(self.nfft // 2) * self.dv
        M = np.zeros((nb, nb))
        lam3000 = MANGOLDT_3000
        for a in range(nb):
            for b in range(a, nb):
                g = corr[a, b]
                g0 = float(g[0])
                gu = np.interp(ULOG, tgrid, g, right=0.0)
                val = pole_pair_grid(gu) + gamma_pair_grid(gu, g0)
                if prime_mode == "true":
                    s = 0.0
                    for n_at in (2, 3, 4, 5):
                        ln = math.log(n_at)
                        if ln < tgrid[-1]:
                            s += (lam3000[n_at] / math.sqrt(n_at)
                                  * float(np.interp(ln, tgrid, g)))
                    val -= s
                elif prime_mode == "smooth":
                    val -= float(np.trapezoid(np.exp(ULOG / 2.0) * gu * ULOG,
                                          np.log(ULOG)))
                M[a, b] = M[b, a] = 2.0 * val
        return M

    def lam_min(self, w_f: float, prime_mode: str) -> tuple[float, float]:
        M = self.gram(w_f, prime_mode)
        ev = np.linalg.eigvalsh(M)
        return float(ev[0]), float(np.abs(ev).max())


def window_wall(wform: WindowForm, prime_mode: str, lo: float,
                hi: float) -> float:
    """Bisect the smallest half-support with lambda_min < -1e-9 ||M||."""
    def is_neg(w_f: float) -> bool:
        lam, rad = wform.lam_min(w_f, prime_mode)
        return lam < -1e-9 * rad
    if not is_neg(hi):
        return float("inf")
    while hi - lo > 0.0025:
        mid = 0.5 * (lo + hi)
        if is_neg(mid):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


MANGOLDT_3000 = mangoldt_array(3000)


# ---------------------------------------------------------------- main
def main() -> int:
    print("=" * 78)
    print("coupling_ansatz_probe  PRIME.STAGE1.COUPLING.01")
    print("FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM. EXPLORATION ONLY. A measured coupling defect is a")
    print("specification of the missing mathematics, not progress on RH.")
    print("=" * 78)

    flags: dict[str, object] = {}

    # ============================================================ A
    section("A. INSTRUMENTS: firewall, wards, floors, the debt table")

    fw_ok, fw_detail = firewall_audit()
    check("A1 source-only AST firewall", fw_ok, fw_detail)

    ok_ep, miss_ep = ward("ep_log", [
        "N=1  lo=4.5917135e-2", "hi=4.5917136e-2",
        "N=2  lo=9.0288701e-6", "hi=9.0289075e-6",
        "N=3  lo=2.3643695e-10", "hi=1.1497752e-9", "CERTIFIED POSITIVE"])
    ok_s4, miss_s4 = ward("s4_log", [
        "N=4  lo=8.278338e-15", "hi=1.3840906e-14", "CERTIFIED POSITIVE"])
    check("A2 certified floors warded verbatim", ok_ep and ok_s4,
          "ep_log missing=%s; s4_log missing=%s"
          % (miss_ep or "none", miss_s4 or "none"))

    ok_kr, miss_kr = ward("krein", [
        "SUZKREIN-TRANSCRIPTION iff <= 1e-6",
        "Z1-TRANSCRIPTION (band pins == cache"])
    ok_cs, miss_cs = ward("cohomspec", [
        "P4  THE (AC) GRAM INTERFACE.",
        "c^T Pick_N c = <-g'', f_c * f_c~>            (AC)"])
    ok_vb, miss_vb = ward("vbk", ["c^T Pick_N c = <-g'', f_c*f_c~>."])
    ok_s1, miss_s1 = ward("stage1", [
        "BRK-A1-CROSSTERMS      direct-sum glue supplies ZERO",
        "HALF-FORM w = log p * p^{-m/2}",
        "psi(s/2)/2 = int_0^infty (e^{-2u}/(2u) - e^{-su}/(1-e^{-2u})) du,"])
    check("A3 interface wards (Z1 / (AC) / r115 breakage)",
          ok_kr and ok_cs and ok_vb and ok_s1,
          "krein=%s cohomspec=%s vbk=%s stage1=%s"
          % (miss_kr or "ok", miss_cs or "ok", miss_vb or "ok",
             miss_s1 or "ok"))

    mp.mp.dps = DPS
    pin_sigmas = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, PIN_COUNT + 1)]
    p_pins = [pin_reference(sig) for sig in pin_sigmas]
    p_pins_refined = [h_pole(sig) + h_gamma(sig)
                      + zeta_logderiv(mp.mpf("0.5") + sig, 128, 32)
                      for sig in pin_sigmas]
    em_dev = max(abs(a - b) for a, b in zip(p_pins, p_pins_refined))
    check("A4 Euler--Maclaurin stability (96/28 vs 128/32)",
          em_dev < mp.mpf("1e-70"), "max dev=%s" % fmt(em_dev, 4))

    floors_ref = []
    for n in range(1, PIN_COUNT + 1):
        lam, _rad = eig_range(pick_matrix(p_pins[:n], pin_sigmas[:n]))
        floors_ref.append(lam)
    in_intervals = all(
        CERTIFIED[n][0] <= float(floors_ref[n - 1]) <= CERTIFIED[n][1]
        for n in range(1, 5))
    for n in range(1, 5):
        print("    N=%d  lambda_min=%-14s  certified=[%.7e, %.7e]"
              % (n, fmt(floors_ref[n - 1], 9), CERTIFIED[n][0],
                 CERTIFIED[n][1]))
    check("A5 reference floors inside certified intervals (N<=4)",
          in_intervals and all(f > 0 for f in floors_ref),
          "ladder N=1..%d all positive" % PIN_COUNT)

    # the debt table (r115 piece decomposition, reproduced)
    vals_pole = [h_pole(sig) for sig in pin_sigmas]
    vals_gam = [h_gamma(sig) for sig in pin_sigmas]
    vals_pr = [zeta_logderiv(mp.mpf("0.5") + sig) for sig in pin_sigmas]
    debt_digits = []
    pieces_4 = None
    for n in range(1, PIN_COUNT + 1):
        lam_p, rad_p = eig_range(pick_matrix(vals_pole[:n], pin_sigmas[:n]))
        lam_g, rad_g = eig_range(pick_matrix(vals_gam[:n], pin_sigmas[:n]))
        lam_r, rad_r = eig_range(pick_matrix(vals_pr[:n], pin_sigmas[:n]))
        lam_t = floors_ref[n - 1]
        digits = float(mp.log10(max(rad_p, rad_g, rad_r) / lam_t))
        debt_digits.append(digits)
        if n == 4:
            pieces_4 = (float(lam_p), float(lam_g), float(lam_r))
        if n <= 4:
            print("    N=%d  lam_min: pole=%-11s Gamma=%-11s prime=%-11s"
                  "  cancel=%.2f digits"
                  % (n, fmt(lam_p, 4), fmt(lam_g, 4), fmt(lam_r, 4),
                     digits))
    debt_ok = (all(abs(debt_digits[i] - FROZEN_DEBT_DIGITS[i]) < 0.05
                   for i in range(4))
               and abs(debt_digits[7] - FROZEN_DEBT_N8) < 0.05
               and all(abs(pieces_4[i] / FROZEN_PIECES_4[i] - 1) < 0.05
                       for i in range(3)))
    check("A6 r115 debt table reproduced (frozen reads)",
          debt_ok,
          "digits N=1..4: %s (frozen %s); N=8: %.2f (frozen %.2f); "
          "pieces_4=(%.3g, %.3g, %.3g)"
          % (", ".join("%.2f" % d for d in debt_digits[:4]),
             FROZEN_DEBT_DIGITS, debt_digits[7], FROZEN_DEBT_N8,
             *pieces_4))
    debt_4 = debt_digits[3]

    # the c* packet (ground eigenvector of Pick_4) for section E
    E4, Q4 = mp.eigsy(pick_matrix(p_pins[:4], pin_sigmas[:4]))
    cstar = [float(Q4[i, 0]) for i in range(4)]
    lam4 = float(E4[0])

    # ============================================================ B
    section("B. SOURCE-ONLY ZERO-SIDE TARGETS (box contours of xi'/xi)")

    # B1: numpy instrument welds against mp
    spots = [complex(2, 0), complex(1.5, 0), complex(0.5, 14.1),
             complex(0.05, 30.0), complex(0.95, -50.0)]
    z_np, dz_np = np_zeta_pair(np.array(spots), cutoff=250)
    zeta_dev = 0.0
    with mp.workdps(40):
        for i, sp in enumerate(spots):
            ref, dref = dirichlet_logderivative(mp.mpc(sp.real, sp.imag),
                                                250, 12)
            zeta_dev = max(zeta_dev,
                           abs(complex(z_np[i]) - complex(ref))
                           / abs(complex(ref)),
                           abs(complex(dz_np[i]) - complex(dref))
                           / abs(complex(dref)))
        dg_spots = [complex(0.25, 7.5), complex(1.0, 0), complex(0.475, 31)]
        dg_np = np_digamma(np.array(dg_spots))
        dg_dev = max(abs(complex(dg_np[i])
                         - complex(mp.digamma(mp.mpc(s.real, s.imag))))
                     for i, s in enumerate(dg_spots))
    check("B1 numpy EM zeta / digamma weld vs mp",
          zeta_dev < 1e-10 and dg_dev < 1e-12,
          "zeta rel=%.2e; digamma abs=%.2e" % (zeta_dev, dg_dev))

    # B2: heights (source-only scans) and integer zero counts
    T_star = scan_height(58.0, 64.0)
    T_two = scan_height(123.0, 129.0)
    T_b1 = scan_height(16.0, 20.0)
    T_b2 = scan_height(38.5, 40.5)
    print("    heights: T*=%.2f  T2=%.2f  bands=(%.2f, %.2f)"
          % (T_star, T_two, T_b1, T_b2))
    box_main = BoxData(T_star, BOX_DT)
    box_two = BoxData(T_two, BOX_DT)
    box_b1 = BoxData(T_b1, BOX_DT)
    box_b2 = BoxData(T_b2, BOX_DT)
    counts = [box.zero_count() for box in (box_main, box_two, box_b1,
                                           box_b2)]
    int_dev = max(abs(cv - round(cv)) for cv in counts)
    check("B2 zero-count integrals integer (all boxes)",
          int_dev < 2e-4,
          "counts=%s  max integer distance=%.2e"
          % (["%.6f" % cv for cv in counts], int_dev))

    n_rvm = (T_star / (2 * math.pi) * math.log(T_star / (2 * math.pi))
             - T_star / (2 * math.pi) + 7.0 / 8.0)
    check("B3 N(T*) vs Riemann--von-Mangoldt mean",
          abs(counts[0] / 2 - n_rvm) < 1.0,
          "N(T*)/2=%.3f vs RvM=%.3f (|S(T)| currency, bar 1.0)"
          % (counts[0] / 2, n_rvm))

    sig4 = [float(s) for s in pin_sigmas[:4]]
    T_om = target_block(box_main, sig4)
    box_half = BoxData(T_star, 2 * BOX_DT)
    T_om_half = target_block(box_half, sig4)
    dual_dev = float(np.max(np.abs(T_om - T_om_half)))
    check("B4 box dual-resolution stability",
          dual_dev < 1e-6,
          "max |dt - 2dt| entry dev=%.2e (primary dt=%.3f)"
          % (dual_dev, BOX_DT))
    flags["box_bar"] = max(dual_dev, 1e-9)

    ev_T = np.linalg.eigvalsh(T_om)
    check("B5 T_omega hermitian block is PSD at the box bar",
          ev_T[0] > -5e-8,
          "lambda_min(T_omega,4)=%.3e (a truncated zero-side Gram); "
          "entries scale %.3e" % (ev_T[0], np.max(np.abs(T_om))))

    # ============================================================ C
    section("C. ANSATZ C1 -- ADELE-CLASS / EISENSTEIN LIFT E(f)")

    # ---- C1a: the literal x-space lift on a discretized domain
    print("  -- C1a: x-space E_mu(f_j), Muentz-subtracted, exact "
          "staircase --")
    a_exp = [s + 0.5 for s in sig4]
    zeta_a = []
    n3 = np.arange(1, 3001, dtype=float)
    for a in a_exp:
        za = float(np.sum(n3 ** (-a))) + 3000.0 ** (1 - a) / (a - 1) \
            + 0.5 * 3000.0 ** (-a)
        zeta_a.append(za)
    prefix = {a: np.concatenate([[0.0], np.cumsum(n3 ** (-a))])
              for a in a_exp}

    def xlift_gram(du: float) -> np.ndarray:
        u = np.arange(-XGRID_U, XGRID_U + du / 2, du)
        x = np.exp(u)
        Mx = np.ceil(1.0 / x - 1e-12).astype(int)
        Mx[x >= 1.0] = 1
        E = np.zeros((len(a_exp), len(u)))
        for i, a in enumerate(a_exp):
            Sj = prefix[a][np.clip(Mx - 1, 0, 3000)]
            E[i] = np.sqrt(x) * (x ** (-a) * (zeta_a[i] - Sj)
                                 - 1.0 / ((a - 1.0) * x))
        G = (E * du) @ E.T
        # analytic tails beyond u = +XGRID_U
        U = XGRID_U
        for i, ai in enumerate(a_exp):
            for k, ak in enumerate(a_exp):
                t1 = (zeta_a[i] * zeta_a[k]
                      * math.exp((1 - ai - ak) * U) / (ai + ak - 1))
                t2 = -(zeta_a[i] / (ak - 1)) * math.exp(-ai * U) / ai
                t3 = -(zeta_a[k] / (ai - 1)) * math.exp(-ak * U) / ak
                t4 = math.exp(-U) / ((ai - 1) * (ak - 1))
                G[i, k] += t1 + t2 + t3 + t4
        return G

    G_x = xlift_gram(XGRID_DU)
    G_x_coarse = xlift_gram(2 * XGRID_DU)

    # Mellin-side emission Gram (continuum instrument)
    taus_e = np.arange(0.0, EMIT_TMAX + EMIT_DT / 2, EMIT_DT)
    zline, _ = np_zeta_pair(0.5 + 1j * taus_e, cutoff=400)
    absz2 = np.abs(zline) ** 2
    wq = np.full(taus_e.shape, EMIT_DT)
    wq[0] = wq[-1] = EMIT_DT / 2
    G_emit = np.zeros((4, 4))
    tail_scale = np.zeros((4, 4))
    tt = np.exp(np.linspace(math.log(EMIT_TMAX), math.log(1e5), 2000))
    mean2 = np.log(tt / (2 * math.pi)) + 2 * EULER_GAMMA
    for j in range(4):
        for k in range(4):
            ker = np.real(1.0 / ((sig4[j] - 1j * taus_e)
                                 * (sig4[k] + 1j * taus_e)))
            core = float(np.sum(wq * absz2 * ker)) / math.pi
            kt = np.real(1.0 / ((sig4[j] - 1j * tt) * (sig4[k] + 1j * tt)))
            tail = float(np.trapezoid(mean2 * kt * tt, np.log(tt))) / math.pi
            G_emit[j, k] = core + tail
            tail_scale[j, k] = abs(tail)
    # halve the tau=0 double count (even symmetry used a factor 2 via /pi)
    dev_x = float(np.max(np.abs(G_x - G_emit) / np.abs(G_emit)))
    dev_x_c = float(np.max(np.abs(G_x_coarse - G_emit) / np.abs(G_emit)))
    tail_rel = float(np.max(tail_scale / np.abs(G_emit)))
    check("C1a x-space lift == Mellin multiplier object",
          dev_x < 1e-2 and dev_x < dev_x_c,
          "grid-vs-continuum rel dev %.2e (du=%.3f) < %.2e (du=%.3f); "
          "tail model rel %.2e (bar 20%% of tail)"
          % (dev_x, XGRID_DU, dev_x_c, 2 * XGRID_DU, tail_rel))

    # ---- C1b: the naive completion floors out
    P4_mp = pick_matrix(p_pins[:4], pin_sigmas[:4])
    P4 = np.array([[float(P4_mp[j, k]) for k in range(4)]
                   for j in range(4)])
    D_naive = G_emit - P4
    naive_rel = float(np.linalg.norm(D_naive) / np.linalg.norm(P4))
    grid_resid = float(np.linalg.norm(G_x - G_emit) / np.linalg.norm(P4))
    ev_D = np.linalg.eigvalsh(D_naive)
    check("C1b NAIVE-COMPLETION-FLOORS (measured wall)",
          naive_rel > 50 * grid_resid and ev_D[0] > 0,
          "|G_emit - Pick_4|_F/|Pick_4|_F = %.3f (grid residual %.2e "
          "shrinks, defect stays); D_4 eigs [%.3g..%.3g]: the naive L^2 "
          "lift MAJORIZES Pick_4 (emission form = |zeta|^2 second "
          "moment, not the zero sum)"
          % (naive_rel, grid_resid, ev_D[0], ev_D[-1]))
    print("    G_emit[1,1]=%.4f vs Pick[1,1]=%.6f: overshoot factor %.1f"
          % (G_emit[0, 0], P4[0, 0], G_emit[0, 0] / P4[0, 0]))

    # ---- C1c: the cokernel/quotient coupling (the priority)
    print("  -- C1c: quotient Gram in H^1_{ell,omega}; zeros emerge, "
          "never input --")
    tau = np.arange(-T_star, T_star + DTAU / 2, DTAU)
    m_true = np_zeta_pair(0.5 - 1j * tau, cutoff=250)[0]
    nodes4 = np.stack([1.0 / (s + 1j * tau) for s in sig4], axis=1)
    tau_b = np.arange(-T_star, T_star + DTAU_FINE / 2, DTAU_FINE)
    m_b = np_zeta_pair(0.5 - 1j * tau_b, cutoff=250)[0]
    nodes_b = np.stack([1.0 / (s + 1j * tau_b) for s in sig4], axis=1)

    defects = {}
    grams = {}
    for ell in ELL_LADDER:
        if ell == ELL_LADDER[-1]:
            Gq = coker_gram(m_b, nodes_b, tau_b, DTAU_FINE, ell,
                            0.5 * ell)
            ratio = DTAU_FINE / ell
        else:
            Gq = coker_gram(m_true, nodes4, tau, DTAU, ell, 0.5 * ell)
            ratio = DTAU / ell
        defects[ell] = rel_defect(Gq, T_om)
        grams[ell] = Gq
        print("    ell=%.2f  dtau/ell=%.4f  defect vs T_omega = %.4f"
              % (ell, ratio, defects[ell]))
    tau_f = np.arange(-T_star, T_star + DTAU / 4, DTAU / 2)
    m_f = np_zeta_pair(0.5 - 1j * tau_f, cutoff=250)[0]
    nodes_f = np.stack([1.0 / (s + 1j * tau_f) for s in sig4], axis=1)
    G_fine = coker_gram(m_f, nodes_f, tau_f, DTAU / 2, 0.4, 0.2)
    d_fine = rel_defect(G_fine, T_om)
    print("    ell=0.40  dtau/ell=%.4f  defect vs T_omega = %.4f "
          "(refined grid)" % (DTAU / 2 / 0.4, d_fine))

    ell_best = min(defects, key=lambda e: defects[e])
    d_best = defects[ell_best]
    G_best = grams[ell_best]
    check("C1c coker quotient reproduces the zero-side block",
          d_best <= DEFECT_BAR,
          "rel Frobenius defect %.4f <= %.2f at ell=%.2f (Gram => PSD "
          "exact: the cancellation is STRUCTURAL in this completion at "
          "the measured defect)" % (d_best, DEFECT_BAR, ell_best))
    collapse_dev = abs(defects[0.8] - d_fine) / max(defects[0.8], d_fine)
    check("C1d defect collapses on dtau/ell (discretization law)",
          collapse_dev <= 0.25,
          "equal-ratio configs (ell=0.8, dtau=%.4f) vs (ell=0.4, "
          "dtau=%.4f): %.4f vs %.4f (dev %.0f%%) -- RK cross-talk "
          "subdominant, the residual defect is pure grid resolution"
          % (DTAU, DTAU / 2, defects[0.8], d_fine, 100 * collapse_dev))

    s_fit = float(np.sum(np.real(G_best) * T_om)
                  / np.sum(np.real(G_best) ** 2))
    check("C1e normalization == RK prediction 2*ell*omega",
          abs(s_fit - 1.0) <= NORM_BAR,
          "fitted scale vs 2*ell theory: %.4f at the best rung "
          "(bar |dev| <= %.2f)" % (s_fit, NORM_BAR))

    G_nr = coker_gram(m_true, nodes4, tau, DTAU, 0.8, 0.4, refine=False)
    G_ls = coker_gram(m_true, nodes4, tau, DTAU, 0.8, 0.4,
                      refine=False, use_lstsq=True)
    d_nr = rel_defect(G_nr, T_om)
    d_ls = rel_defect(G_ls, T_om)
    check("C1f solver gate (ridge normal eq vs lstsq)",
          abs(d_ls - d_nr) < 1e-3,
          "defect ridge=%.5f vs lstsq=%.5f (no-refinement config, "
          "ell=0.8)" % (d_nr, d_ls))

    evG = np.linalg.eigvalsh(np.real(G_best))
    check("C1g quotient Gram PSD exact (the structural sign)",
          evG[0] > -1e-12 * np.trace(np.real(G_best)),
          "lambda_min(Ghat_4)=%.3e (>= 0 by construction: sign supplies "
          "ALL %.1f cancellation digits at N=4 structurally; magnitude "
          "to %.1f digits at the measured defect)"
          % (evG[0], debt_4, -math.log10(d_best)))

    check("C1h grid refinement improves the mid rung",
          d_fine < defects[0.4],
          "defect dtau=%.4f: %.4f < dtau=%.4f: %.4f at ell=0.4"
          % (DTAU / 2, d_fine, DTAU, defects[0.4]))

    # ---- arithmetic truncation ladder (integer currency)
    print("  -- multiplier truncation ladders (the 'primes <= x' axis) --")
    ell_mid = 0.4
    d_x = {}
    s_line = 0.5 - 1j * tau
    for X in X_LADDER:
        mX = np_zeta_pair(s_line, cutoff=X, terms=2)[0]
        GX = coker_gram(mX, nodes4, tau, DTAU, ell_mid, 0.5 * ell_mid)
        d_x[X] = rel_defect(GX, T_om)
        print("    integer truncation X=%4d (EM-smoothed partial sum): "
              "defect %.4f" % (X, d_x[X]))
    d_em_mid = defects[ell_mid]
    check("C1i integer currency converges inside the omega window",
          max(d_x.values()) <= 2.0 * d_em_mid,
          "defects X=30/60/120: %.4f/%.4f/%.4f vs EM %.4f: the "
          "EM-smoothed integer truncation is already at the "
          "continuation value by X=30 in the Omega=%.0f window (deeper "
          "X is an IR requirement, not a window one)"
          % (d_x[30], d_x[60], d_x[120], d_em_mid, OMEGA))

    d_p = {}
    min_mp = {}
    for xp in XP_LADDER:
        logm = np.zeros(tau.shape, dtype=complex)
        for p in sieve_small(xp):
            logm -= np.log(1.0 - np.exp(-s_line * math.log(p)))
        mP = np.exp(logm)
        min_mp[xp] = float(np.min(np.abs(mP)))
        GP = coker_gram(mP, nodes4, tau, DTAU, ell_mid, 0.5 * ell_mid)
        d_p[xp] = rel_defect(GP, T_om)
    check("C1j EULER-CURRENCY-FAILS on the line (measured)",
          d_p[100] > 5.0 * d_em_mid,
          "Euler-product truncation x_p=20/100: defect %.3f/%.3f "
          "(min|m_P|=%.3f/%.3f: no on-line zeros form) vs EM %.4f -- "
          "the finite adelic level must be taken in integer/resummed "
          "currency, not Euler currency"
          % (d_p[20], d_p[100], min_mp[20], min_mp[100], d_em_mid))

    # ---- controls through the same lift
    m_sm = 1.0 / (s_line - 1.0)
    G_sm = coker_gram(m_sm, nodes4, tau, DTAU, ell_mid, 0.5 * ell_mid)
    d_sm = rel_defect(G_sm, T_om)
    check("C1k smooth control dies through the lift",
          d_sm > 0.5,
          "integers->Lebesgue multiplier 1/(s-1) (no zeros): defect "
          "%.4f, trace ratio %.2e (coker empties)"
          % (d_sm, float(np.trace(np.real(G_sm)) / np.trace(T_om))))

    Xs = 250
    order = np.argsort([(n * GOLDEN) % 1.0 for n in range(1, Xs + 1)])
    log_perm = np.log(np.arange(1, Xs + 1, dtype=float)[order])
    wgt = np.arange(1, Xs + 1, dtype=float) ** (-0.5)
    m_scr = (wgt[None, :]
             * np.exp(1j * np.outer(tau, log_perm))).sum(axis=1)
    G_scr = coker_gram(m_scr, nodes4, tau, DTAU, ell_mid, 0.5 * ell_mid)
    d_scr = rel_defect(G_scr, T_om)
    check("C1l scrambled control dies through the lift",
          d_scr > 0.5,
          "golden-permuted dilation lengths (weights kept): defect %.4f"
          % d_scr)

    # ---- Z1 screen
    lam_arr = MANGOLDT_3000
    ns = np.arange(2, 251, dtype=float)
    lam_s = lam_arr[2:251]
    cache_F = np.zeros(box_main.nodes.shape, dtype=complex)
    sbox = 0.5 + box_main.nodes
    cache_F = (1.0 / sbox + 1.0 / (sbox - 1.0)
               - 0.5 * math.log(math.pi) + 0.5 * np_digamma(sbox / 2.0)
               - (lam_s[None, :]
                  * np.exp(-sbox[:, None] * np.log(ns)[None, :])).sum(1))
    ker11 = omega_analytic(box_main.nodes) / ((sig4[0] - box_main.nodes)
                                              * (sig4[0] + box_main.nodes))
    t_cache = box_main.integrate_plain(ker11, cache_F)
    with mp.workdps(40):
        em15 = em_zeta_value(mp.mpf("1.5"))
        raw15 = mp.fsum(mp.power(n, mp.mpf("-1.5")) for n in range(1, 251))
        resum_dev = float(abs(em15 - raw15) / abs(em15))
    check("C1m Z1 screen: coupling readout not transcribable",
          abs(t_cache) < 1e-5 and resum_dev > 1e-3,
          "cache-integrand box readout %.2e (pole-free: quadrature zero "
          "vs T_omega[1,1]=%.3e -- the readout lives on the poles of "
          "xi'/xi, which only the RESUMMED object has); EM-vs-partial "
          "dev %.2e > 1e-3 (Z1-CLEAN-BY-CURRENCY)"
          % (abs(t_cache), T_om[0, 0], resum_dev))

    # omega ladder (IR requirement), report-only
    T_om40 = target_block(box_main, sig4, om=40.0)
    G_40 = coker_gram(m_true, nodes4, tau, DTAU, 0.8, 0.4, om=40.0)
    print("    omega ladder (IR): Omega=25 defect %.4f | Omega=40 "
          "defect %.4f (ell=0.8 rung; omega->1 requires T->infty: the "
          "completion's IR datum)"
          % (defects[0.8], rel_defect(G_40, T_om40)))

    # ============================================================ D
    section("D. ANSATZ C2 -- THETA / METAPLECTIC LIFT")

    m_two = np_zeta_pair(0.5 - 2j * tau_b, cutoff=250)[0]
    T2_raw = target_block(box_two, sig4, half_speed=True)
    T2_m = target_block(box_two, sig4, half_speed=True, matched=True)
    ell_c2 = 0.2
    G2_raw = coker_gram(m_two, nodes_b, tau_b, DTAU_FINE, ell_c2,
                        0.5 * ell_c2)
    d2_raw_vs_c1 = rel_defect(G2_raw, T_om)
    d2_raw_own = rel_defect(G2_raw, T2_raw)
    nodes4m = np.stack([1.0 / (s + 2j * tau_b) for s in sig4], axis=1)
    G2_m = coker_gram(m_two, nodes4m, tau_b, DTAU_FINE, ell_c2,
                      0.5 * ell_c2)
    d2_m = rel_defect(G2_m, T2_m)
    check("D1 theta lift RAW misses the Pick target (measured)",
          d2_raw_vs_c1 > 5.0 * d2_raw_own,
          "raw defect vs C1 target %.4f vs own (gamma/2-evaluation) "
          "target %.4f: the metaplectic coupling lands on the halved "
          "spectrum" % (d2_raw_vs_c1, d2_raw_own))
    check("D2 theta lift MATCHED via the doubled test family",
          d2_m <= 0.2,
          "matched defect %.4f (doubled spectral density: RK cross-talk "
          "floor rises; min zero gap halves)" % d2_m)
    check("D3 theta raw own-target consistency",
          d2_raw_own <= 0.2,
          "the machinery is sound (%.4f); the mismatch is the coupling "
          "dictionary, not the instrument" % d2_raw_own)
    print("    C2 dictionary: theta lift == C1 conjugated by the square "
          "flow; no new positivity channel beyond C1 at doubled density")

    # ============================================================ E
    section("E. ANSATZ C3 -- SUSPENSION + PROLATE (ARCHIMEDEAN ORBIT)")

    # E1/E2: mu-instrument validation on exponentials
    dev_real = 0.0
    U_TOP = 45.0
    for sg in (0.6, 1.0, 2.0, 4.0):
        gu = np.exp(-sg * ULOG)
        num = pole_pair_grid(gu) + gamma_pair_grid(gu, 1.0)
        # closed pole tails beyond U_TOP (validation packets are not
        # compactly supported; window packets are, and need no tail)
        num += (math.exp((0.5 - sg) * U_TOP) / (sg - 0.5)
                + math.exp(-(0.5 + sg) * U_TOP) / (sg + 0.5))
        with mp.workdps(40):
            ref = float(h_pole(mp.mpf(repr(sg)))
                        + h_gamma(mp.mpf(repr(sg))))
        dev_real = max(dev_real, abs(num - ref) / abs(ref))
    check("E1 mu integrator reproduces pole+Gamma pins",
          dev_real < 5e-7, "max rel dev %.2e over sigma grid (bar 5e-7; "
          "window packets live at u <= 0.9 where the grid is densest)"
          % dev_real)

    dev_cx = 0.0
    for tau_c in (5.0, 15.0, 30.0):
        gu = np.exp(-0.5 * ULOG) * np.cos(tau_c * ULOG)
        num = gamma_pair_grid(gu, 1.0)
        with mp.workdps(40):
            s_c = mp.mpc(1.0, -tau_c)   # s = 1/2 + sigma, sigma=0.5-i*tau
            ref = float(mp.re(mp.digamma(s_c / 2) / 2)
                        - 0.5 * math.log(math.pi))
        dev_cx = max(dev_cx, abs(num - ref) / max(abs(ref), 1.0))
    check("E2 mu integrator on oscillatory packets",
          dev_cx < 1e-6, "max rel dev %.2e at tau=5/15/30" % dev_cx)

    # correlation instrument gate (FFT vs direct, one pair)
    wform = WindowForm()
    Fb = wform.basis(0.30)
    corr = wform.correlations(Fb)
    a_i, b_i = 3, 11
    direct = np.correlate(Fb[:, b_i], Fb[:, a_i], mode="full") * wform.dv
    mid = len(Fb) - 1
    nt_c = 400
    d_fft = float(np.max(np.abs(
        corr[a_i, b_i][:nt_c]
        - 0.5 * (direct[mid:mid + nt_c] + direct[mid::-1][:nt_c]))))
    print("    correlation instrument: FFT vs direct max dev %.2e" % d_fft)

    # E3/E4: arch-only window positivity and its wall
    lam_arch = {}
    for w_f in (0.15, 0.25, 0.30, 0.34):
        lam, rad = wform.lam_min(w_f, "none")
        lam_arch[w_f] = (lam, rad)
        print("    arch-only  2w_f=%.3f: lambda_min=%.3e (scale %.2e)"
              % (2 * w_f, lam, rad))
    arch_psd = all(lam > -1e-9 * rad for lam, rad in lam_arch.values())
    check("E3 CC prolate positivity, corpus window currency",
          arch_psd and d_fft < 1e-10,
          "arch-only (pole+Gamma) Gram PSD for autocorrelation support "
          "2w_f <= 0.68 < log2 (their proven sqrt2-window, our currency)")

    w_wall = window_wall(wform, "none", 0.30, 0.42)
    check("E4 arch wall == r115 Schur exit (cross-currency)",
          abs(2 * w_wall - FROZEN_ARCH_EXIT) <= 0.03,
          "arch-only wall at autocorrelation depth %.3f vs frozen r115 "
          "ALPHA_EXIT %.3f (overhang past log2: %+.3f)"
          % (2 * w_wall, FROZEN_ARCH_EXIT, 2 * w_wall - LOG2))

    # E5: the first prime atom rescues positivity past the arch wall
    rescue = []
    for w_f in (0.36, 0.375, 0.40):
        lam_a, rad_a = wform.lam_min(w_f, "none")
        lam_t, rad_t = wform.lam_min(w_f, "true")
        rescue.append((w_f, lam_a, lam_t, rad_t))
        print("    2w_f=%.2f: arch-only lam=%.3e | +atom(log2) lam=%.3e"
              % (2 * w_f, lam_a, lam_t))
    atom_rescues = all(lam_t > -1e-8 * rad_t
                       for _w, _la, lam_t, rad_t in rescue) \
        and any(lam_a < 0 for _w, lam_a, _lt, _r in rescue)
    check("E5 ORBIT-COUPLING at the first atom (measured rescue)",
          atom_rescues,
          "past the arch wall the log-2 atom restores lambda_min >= 0 "
          "(MEASURED, consistent-with-corpus; not a proof): the debt "
          "localizes at the orbit/atom coupling, window currency")

    w_wall_sm = window_wall(wform, "smooth", 0.05, 0.42)
    check("E6 smooth control dies below the prime support edge",
          2 * w_wall_sm < LOG2 and w_wall_sm < w_wall,
          "smooth (PNT density) window wall at depth %.3f < log2=%.3f "
          "and < arch wall %.3f: the support-error signature"
          % (2 * w_wall_sm, LOG2, 2 * w_wall))

    # E7: degenerate orbit == mean zero density
    tau_d = np.arange(10.0, T_star, 0.25)
    d_arch = (np.real(np_digamma(0.25 + 0.5j * tau_d)) * 0.5
              - 0.5 * math.log(math.pi)) / math.pi
    d_rvm = np.log(tau_d / (2 * math.pi)) / (2 * math.pi)
    dev_d = np.abs(d_arch - d_rvm)
    dev30 = float(np.max(dev_d[tau_d >= 30.0]))
    check("E7 germ FT == mean zero-counting density (welded)",
          dev30 < 1e-3,
          "max |arch density - RvM| = %.2e (tau>=30; %.2e over "
          "[10,%.0f]): the degenerate orbit supplies the MEAN density "
          "the primes oscillate around" % (dev30, float(np.max(dev_d)),
                                           T_star))

    # E8: the c*-packet accounting at the N=4 floor
    print("  -- c* = ground eigenvector of Pick_4 (the hardest packet) --")
    q_piece = {}
    for name, vals in (("pole", vals_pole), ("Gamma", vals_gam),
                       ("prime", vals_pr)):
        Mp = pick_matrix(vals[:4], pin_sigmas[:4])
        q = mp.mpf(0)
        for j in range(4):
            for k in range(4):
                q += mp.mpf(repr(cstar[j])) * mp.mpf(repr(cstar[k])) \
                    * Mp[j, k]
        q_piece[name] = float(q)
    vals_sm = [h_pole(sig) + h_gamma(sig) - 1 / (sig - mp.mpf("0.5"))
               for sig in pin_sigmas[:4]]
    Msm = pick_matrix(vals_sm, pin_sigmas[:4])
    q_sm = float(sum(cstar[j] * cstar[k] * float(Msm[j, k])
                     for j in range(4) for k in range(4)))
    q_sum = q_piece["pole"] + q_piece["Gamma"] + q_piece["prime"]
    digits_remaining = math.log10(abs(q_sm) / lam4)
    digits_density = math.log10(
        max(abs(q) for q in q_piece.values()) / abs(q_sm))
    print("    piece contractions: pole=%+.6e Gamma=%+.6e prime=%+.6e"
          % (q_piece["pole"], q_piece["Gamma"], q_piece["prime"]))
    print("    sum=%.3e == lambda_4=%.3e | PNT-density residual "
          "q_sm=%+.3e" % (q_sum, lam4, q_sm))
    check("E8 density-level coupling accounting",
          abs(q_sum / lam4 - 1) < 1e-6 and digits_remaining >= 2.0,
          "of the %.2f digits at N=4 the mean-density (PNT) coupling "
          "supplies %.2f; the prime-oscillation coupling still owes "
          "%.2f digits (residual %.2e vs floor %.2e)"
          % (debt_4, digits_density, digits_remaining, q_sm, lam4))

    # E9: zero-side band masses of the c* packet (consistency)
    bands = []
    for box in (box_b1, box_b2, box_main):
        zb = box.nodes
        kc = ((sum(cstar[j] / (sig4[j] - zb) for j in range(4)))
              * (sum(cstar[k] / (sig4[k] + zb) for k in range(4))))
        bands.append(abs(box.integrate(kc)))
    band_bar = 5 * max(flags["box_bar"], 1e-8)
    check("E9 c* zero-side band masses below instrument bar",
          all(b <= band_bar for b in bands),
          "|c*^T P^(T) c*| at T=%.0f/%.0f/%.0f: %.1e/%.1e/%.1e <= %.1e "
          "(cancellation depth 1e-14 certified only by the mp ladder; "
          "bands resolution-limited, consistent)"
          % (T_b1, T_b2, T_star, *bands, band_bar))

    # ============================================================ F
    section("F. FITNESS TABLE, SHARPENED REQUIREMENT, VERDICT")

    print("  FITNESS TABLE (per ansatz):")
    print("    ansatz  P_N reproduction              digits supplied "
          "@N=4        Z1     controls")
    print("    C1      T_omega block, defect %.4f    sign: ALL %.1f "
          "(Gram-PSD);  clean  smooth %.2f / scram %.2f"
          % (d_best, debt_4, d_sm, d_scr))
    print("            (naive L^2 floors at %.2f)    magnitude: %.1f "
          "digits" % (naive_rel, -math.log10(d_best)))
    print("    C2      matched defect %.4f           same channel as C1 "
          "at        clean  raw-miss factor %.1f"
          % (d2_m, d2_raw_vs_c1 / max(d2_raw_own, 1e-9)))
    print("            (raw misses: %.4f)            doubled density"
          % d2_raw_vs_c1)
    print("    C3      window currency: arch wall    density level: "
          "%.2f digits;      n/a    smooth wall %.3f"
          % (digits_density, 2 * w_wall_sm))
    print("            %.3f + atom rescue past it    oscillation owes "
          "%.2f" % (2 * w_wall, digits_remaining))

    structural = (d_best <= DEFECT_BAR
                  and collapse_dev <= 0.25
                  and abs(s_fit - 1.0) <= NORM_BAR
                  and evG[0] > -1e-12 * np.trace(np.real(G_best))
                  and d_sm > 0.5 and d_scr > 0.5
                  and abs(t_cache) < 1e-5)
    flags["structural"] = structural

    print("\n  SHARPENED COUPLING REQUIREMENT (the deliverable):")
    print("  the cancellation is a QUOTIENT-GRAM identity: Pick block = "
          "Gram of the")
    print("  node vectors' projections onto coker(E) -- 'full minus "
          "range', both PSD,")
    print("  never three indefinite pieces.  What the finite surrogate "
          "PINS as the")
    print("  remaining open data of the coupling:")
    print("  (i)   the COMPLETION: the delta-weighted H^1_ell quotient "
          "with the RK")
    print("        normalization 2*ell*omega (measured %.4f vs theory "
          "1); E isometric" % s_fit)
    print("        <=> the zero evaluations orthonormal; RK cross-talk "
          "measured")
    print("        SUBDOMINANT (defect collapses on dtau/ell: %.4f vs "
          "%.4f at equal" % (defects[0.8], d_fine))
    print("        ratio -- the finite defect is grid resolution, not "
          "structure);")
    print("  (ii)  the IR limit omega -> 1, T -> infty (the certified "
          "floors live at")
    print("        omega == 1; finite-Omega defect measured);")
    print("  (iii) the currency: integer/resummed multiplier only "
          "(Euler-truncation")
    print("        fails on the line, factor %.0fx; Z1: the readout "
          "lives on the poles" % (d_p[100] / d_em_mid))
    print("        of xi'/xi -- transcription reads exactly zero);")
    print("  (iv)  the archimedean orbit supplies the MEAN density "
          "(welded %.1e) and" % dev30)
    print("        the first-atom rescue is measured in window currency "
          "-- the")
    print("        oscillation coupling still owes %.2f digits at the "
          "N=4 packet." % digits_remaining)

    typed_ok = (naive_rel > 0.5 and d2_raw_vs_c1 > 5 * d2_raw_own
                and arch_psd and atom_rescues)
    check("F1 composite typing consistent",
          typed_ok and structural,
          "naive floors, metaplectic dictionary, prolate window, atom "
          "rescue and the structural C1 quotient all fire as typed")

    wall = time.time() - T0
    check("F2 runtime", wall <= RUNTIME_BAR,
          "%.1f s <= %.0f s" % (wall, RUNTIME_BAR))

    prior = len(CHECKS)
    prior_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("F3 pattern gate",
          prior == N_CHECKS_EXPECTED - 1 and prior_pass == prior,
          "expected %d prior checks, zero fails (got %d, %d fails)"
          % (N_CHECKS_EXPECTED - 1, prior, prior - prior_pass))

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    if n_pass != len(CHECKS):
        print("VERDICT: COUPLING-INSTRUMENT-EDGE (failed gate; no "
              "mathematical verdict)")
        print("NO RH CLAIM. EXPLORATION ONLY.")
        print("=" * 78)
        return 1
    if structural:
        print("VERDICT: COUPLING-STRUCTURAL(C1 adele-class cokernel "
              "lift:")
        print("  the quotient Gram of the corpus nodes against coker(E),")
        print("  E = sum_n n^{-1/2} U_n (multiplier zeta(1/2-i tau)), in "
              "the")
        print("  omega-weighted H^1_ell completion, reproduces the "
              "truncated")
        print("  zero-side Pick block at defect %.4f (ell=%.2f), "
              "normalization" % (d_best, ell_best))
        print("  2*ell*omega fitted %.4f, PSD exact -- the %.1f-digit "
              "cancellation" % (s_fit, debt_4))
        print("  at N=4 is the positivity of a quotient Gram, i.e. "
              "STRUCTURAL in")
        print("  this completion; zeros were never input, they emerge "
              "from the")
        print("  lift geometry.  OPEN: the completion datum (i)-(iv) "
              "above.)")
    else:
        print("VERDICT: COUPLING-DEFECT-FLOORS(best defect %.4f > bar "
              "%.2f;" % (d_best, DEFECT_BAR))
        print("  the wall in lift coordinates: naive %.3f, quotient "
              "ladder %.4f/%.4f/%.4f)"
              % (naive_rel, defects[0.8], defects[0.4], defects[0.2]))
    print()
    print("NO RH CLAIM. EXPLORATION ONLY. A structural representation of")
    print("a TRUNCATED block is not RH; the untruncated statement is the")
    print("open IR limit, and Stage 1 remains OPEN.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
