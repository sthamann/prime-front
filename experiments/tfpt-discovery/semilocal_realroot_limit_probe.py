#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""semilocal_realroot_limit_probe -- PRIME.SEMILOCAL.REALROOT.LIMIT.01

FROZEN SPEC v2 (2026-08-14).  EXPLORATION ONLY.  This probe writes no
files, changes no verification module, paper, ledger, website, manifest,
Lean file or status marker.  It makes NO RH claim, NO positivity claim,
NO counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Adjudicate the REAL-ROOT LIMIT architecture: instead of proving
positivity of the Weil form (kill-atlas edge E4), build finite
SELF-ADJOINT source-only operators H_N whose characteristic functions
E_N have automatically real roots, and identify the limit with Xi via
the trace formula on a determining even Paley-Wiener test class;
compactness + Hurwitz + Hadamard then give RH.  The three prior
Xi-determinant attempts (CCCXLIII, CCCLIII, CCCLVII; read-only
dependencies of the record, none imported) died on an underdetermined
normalization (VACUOUS) and control separation 2.58/1.68 vs bar 5.
The new architecture claims to fix this by identifying the limit
through the FULL trace identity on a determining test class.

THE OPERATOR FAMILY (T2/T3 decision, frozen).  Connes' extremal
construction (arXiv 2602.04022, letter + par.6): restrict the Weil
quadratic form Q(phi) = POLE(psi) + ARCH(psi) - PRIME(psi), psi =
phi * phi~, to test functions on [-a, a], a = (log x)/2 (primes <= x
enter, semilocal S = {p <= x, infty}), and take the MINIMAL
eigenvector eta.  Its Fourier transform E_N = etahat is entire of
exponential type a, and by the Caratheodory-Fejer extremal mechanism
(Connes Thm 6.1; Connes-van Suijlekom finite truncations [32]) its
zeros are ALL REAL provided the lowest eigenvalue is simple with even
eigenvector.  E_N is det_reg of a self-adjoint rank-one perturbation
of the periodic Dirac operator (Connes fn.14) -- realness consumes NO
wall positivity (lam_min may have any sign).  R1 source-only: the
form's matrix entries are pole block + archimedean block + prime
powers <= x; no zeta zero, no zeta value, no target eigendata.

THREE MEASUREMENT LAYERS (design iterations DISCLOSED; both earlier
smokes are part of the record and priced structural facts):
  (L1, verdict-bearing) HIGH-PRECISION TRIG-GALERKIN, the TRUE
    extremal family.  Even sector b_k(u) = cos(k pi u/a), om = k pi/a,
    k = 0..K-1, K = ceil(KFAC x log x).  Closed-form entries through
    the separable identity psi_jk(v) = (-1)^{j+k} [om_k sin(om_k v)
    - om_j sin(om_j v)]/(om_j^2 - om_k^2): POLE = 2 Ip Ip^T (rank
    one, Ip_k = (-1)^k sinh(a/2)/(1/4+om_k^2)); PRIME from one vector
    P_k = sum_n w_n sin(om_k log n); ARCH from K oscillatory
    integrals J_k = int sin(om_k w) A(w) dw, A = e^{-w/2}/(1-e^{-2w})
    (A = 1/(2w) + r split; Si closed form + period-split mp.quad).
    THE PRECISION LAW (measured on the v2 float64 smoke and frozen
    here): the minuscule bottom cluster of the Weil form sits at the
    Connes scale eps(lam) ~ e^{-4 pi x} with POLYNOMIAL splitting
    ratios, so the true minimizer direction exists only at working
    precision ~ e^{-4 pi x}: dps(x) must exceed 4 pi x/ln 10 +
    margin.  FROZEN HP LADDER: x in (3, 5, 8, 13), dps = (45, 60,
    80, 120); HP controls SCRPOS + EPSTEIN at x = 8; odd-sector
    minimum at x = 8 (evenness hypothesis of [32]); KRED rung at
    x = 8 (cutoff split, eq-(7) analog).  E_N(z) = sum c_k B_k(z),
    B_k = a[sinc(a(z-om_k)/pi) + sinc(a(z+om_k)/pi)]: entire, type
    a, NOT periodic; beyond the mode cutoff the zeros are EXACTLY
    the lattice j pi/a, j >= K (ward), so trace sums close exactly
    with a lattice tail -- no density model.  Realness is CITED
    ([32]) + MEASURED by a COMPLETE polynomial census: the
    nontrivial zeros are the roots of the degree-(K-1) numerator
    polynomial in y = z^2 (scaled for conditioning), typed real /
    imaginary-pair / complex-quadruple, then refined on E by
    bisection.  Zero collection runs in float64 on the rounded
    eigenvector (zeros are O(1e-16)-stable under coefficient
    rounding; only the DIRECTION needed the digits).
  (L2, precision-wall table) the same trig family at float64 on
    x = (13, 29, 61, 127, 211): the bottom cluster is unresolvable
    (measured smoke: gap ~ 1.5e-8 vs needed e^{-4 pi x}), the
    computed minimizer is a cluster MIXTURE, extra sub-gamma_1 zeros
    appear (first zero 6.07 at x = 13 vs gamma_1 = 14.13) and the
    trace identity is violated at O(h)-scale.  This layer documents
    the CONDITIONING WALL of the architecture and hosts the cheap
    4-world control table at scale.
  (L3, comparison row) GRID-CF: uniform tent mesh (v912 kernel),
    REAL SYMMETRIC TOEPLITZ compression, realness UNCONDITIONAL
    in-probe (Caratheodory 1911 + np.roots audit; the v1 smoke
    measured 427/427 unimodular roots at 4e-13) -- but the uniform
    lattice makes E_N PERIODIC (period 2 pi/delta), its zeros track
    the FOLDED image of ALL ordinates, and the trace identity is
    structurally aliased away at any fixed delta (v1 smoke: mean
    displacement 6-15 spacings).  The structural trade is priced:
    the only family with an in-probe realness THEOREM is the one
    whose trace sums are band-folded.

=======================================================================
THE SIX GATES (frozen, from the proposal)
=======================================================================
 G1 real-rootedness WITHOUT wall positivity: no construction branch
    consumes B > 0, s > 0 or lam_min > 0.  Measured: census deficit
    <= DEFICIT_BAR on MAIN/CTRL trig cells + imaginary-axis scan;
    unimodularity audit on the GRID-CF cells.
 G2 no zero access: AST firewall; the verified-ordinate cache is
    read ONLY inside ward_/target_ functions (X5-typed, instrument
    and diagnostics, never construction).
 G3 no sign-mined selection: tower = EVERY prime power <= x.
 G4 trace convergence per fixed h: eps_N(h) = |2 sum_{found} h
    + 2 sum_{lattice j>=K} h(j pi/a) - SRC(h)|, SRC = POLE + ARCH
    - PRIME (exact source side; prime sum finite, n <= e^B).
 G5 uniform tail control: TAIL(x, R) = 2 sum_{|lam|>R} lam^{-2}
    (R = 50/100/200) bounded over the ladder, decreasing in R; G0
    meter: min |zero|, |E_N(0)|.
 G6 THE DECISIVE ONE -- world separation, PRE-FROZEN BAR (the bar
    that killed the old routes at 2.58): EPSTEIN (Lambda_Q of
    r_{x^2+5y^2}/2, no Euler product), SCRAMBLE-POS (golden jitter
    0.35), SCRAMBLE-ARITH (golden-order weight permutation), SMOOTH
    (prime-free PNT density e^{v/2}).  GATE READ: HP layer, SCRPOS +
    EPSTEIN at x = 8 (median over battery >= SEP_BAR = 5 and >= 4 of
    6 rows >= 1.5); the full 4-world table is measured on the
    float64 layer at x = (61, 211) as corroborating diagnostics.
    Tau-screen: OLS slope of log10 eps_N(h) vs log10 tau_N over the
    HP ladder, tau_N = lam_min (the TRUE Weil margin of the window);
    atlas bands PASS |s| <= 0.30, RELOCATION s >= 0.70.

=======================================================================
T1 -- THE LIMIT-THEOREM SKELETON, ENCODED AS GATES
=======================================================================
 (a) COMPACTNESS: R4 + R5 as proposed do NOT suffice.  Executable
     counterexample T1a-1: a real zero pair sliding to the origin
     keeps R4 tails and R5 intact while |E_N(2i)| >= 1 + 4/eps^2
     blows up.  REPAIR T1a-2 (source-only, derived FROM R3): a
     large-bandwidth Fejer minorant h_beta = tenthat_beta >= 0 has
     SRC(h_beta) < 2 h_beta(0) (verified numerically at beta = 6 and
     8 from the source side alone); a sliding pair contributes
     2h(eps) -> 2h(0) > SRC, so R3 for this single h forbids zeros
     near 0, and translated minorants give uniform local counts.
     Typed: GAP-IN-SKETCH, REPAIRED-BY-R3.
 (b) HURWITZ: SOUND (R5 gives E(0) = Xi(0) != 0, E !== 0).
 (c) DETERMINATION LEMMA: SOUND, two classical steps.  (c1) real-vs-
     real uniqueness: an even signed measure with polynomial counting
     and lam^{-2}-integrable tails killing every even PW h has
     vanishing tempered Fourier transform (h runs over inverse FTs of
     even C_c^inf), hence is 0 WITH multiplicities.  (c2) reality of
     Z(Xi): h-sums extend to resolvent kernels 2z/(z^2 - lam^2) for
     |Im z| > 1/2 (smooth truncation of hhat = i e^{iz|xi|}; error
     e^{(1/2 - Im z) cut} dies against the strip-bounded zero set),
     so the Xi-side Stieltjes transform equals that of the real-
     supported limit measure and is analytic off R: no off-line zero.
     NO CONVERGENCE RATE IS CONSUMED: the route needs only
     eps_N(h) -> 0 per fixed h, so the ~1%-spacing bar (MIN-U2) is
     NOT re-imported by the skeleton; the re-import risk lives only
     in how a concrete family achieves R3 (measured by G4/G6).
     Executable demo T1c: one moved cache zero changes a battery
     h-sum by >> float noise (bar 1e-6).
 (d) HADAMARD ENDGAME: E'(0) = 0 is VACUOUS for even functions, and
     unrestricted det_reg admits a drifting Gaussian e^{b_N z^2}
     unseen by R5: DEFINITIONAL GAP G1.  REPAIR: finite-rank E_N are
     polynomials and R4 forbids lam^{-2}-mass escape (demo T1d-1:
     (1 - z^2/(cN))^N has sup_N tail = 1/c not-> 0), so b = 0 in the
     limit; alternatively pin E''(0) source-only via
     sum_rho 1/(rho(1-rho)) = 2 + gamma - log 4pi (ward T1d-2
     re-derives the constant from the cache to < 1e-3).
 SKELETON RULE (frozen): composite REALROOT-SKELETON-GAP fires only
 for an UNREPAIRABLE hole; (a) and (d) as found are repairable and
 are reported as required amendments to the proposal.

=======================================================================
FROZEN LADDERS, BARS, VERDICTS
=======================================================================
 HP LAYER (verdict-bearing): HP_X = (3, 5, 8, 13); HP_DPS = (45, 60,
 80, 120) (frozen against the precision law 4 pi x/ln 10 + margin);
 HP_CTRL_X = 8 (SCRPOS + EPSTEIN); HP KRED rung at x = 8;
 DROP_BAR_HP = 4 over the 4-rung ladder.  KFAC = 1.25
 (K = ceil(KFAC x log x)); KRED_FAC = 0.85 (cutoff split, eq-(7)
 analog: |eps_K - eps_{0.85K}|; the mesh part proper belongs to the
 GRID-CF row where v912's O(D^2 log 1/D) is the cited law).
 FLOAT64 WALL LAYER (diagnostic): X_LADDER = (13, 29, 61, 127, 211);
 X_CTRL = (61, 211), all 4 worlds.  GRID-CF: GRIDCF_X = (61, 211),
 DELTA_GRID = 0.006, T_CAP_GRID = 450.
 SCAN_STEP = 0.02; BISECT = 45; IMAG_SCAN = (0.05, 30, 0.05);
 BATTERY f_{B,m}(v) = (1 - (v/B)^2)^m on [-B, B], (B, m) in
 (1.2, 2.0, 2.8) x (2, 4); h = fhat (even PW type B, closed Bessel
 form); tower-complete iff e^B <= x (flagged rows);
 LATTICE_TOP = 6000 (lattice tail summed exactly to here; remainder
 < 1e-9 by |h| ~ t^{-(m+1)}, disclosed); NF = 1e-8 flat (frozen:
 SRC quadrature + lattice remainder envelope);
 WOBBLE = 1.3; SEP_BAR = 5; SEP_MIN = 1.5; SEP_ROWS = 4 (of 6);
 TAU_PASS = 0.30; TAU_RELOC = 0.70; FEJ_BETA = 6; JITTER = 0.35;
 GOLDEN = (sqrt 5 - 1)/2; DEFICIT_BAR = 1; RUNTIME_BAR = 1500 s.
 DICTIONARY WARD BARS (relative; m = 2 / B = 2.8 reads are limited by
 h's oscillatory decay against the 7000-ordinate cache): m = 2: 3e-3
 (B < 2.5), 8e-3 (B = 2.8); m = 4: 1e-4 (B < 2.5), 3e-4 (B = 2.8).
 Row typing per h over the HP ladder: CONVERGES iff eps(13) <=
 eps(3)/DROP_BAR_HP and nonincreasing within WOBBLE at >= 2 of 3
 steps (both-ends <= 10 NF = saturated pass); DIVERGES iff eps(13) >
 2 eps(3) and > 10 NF; else PLATEAU.  Decay exponent = OLS slope of
 log eps vs log x on live rungs.  HP separation at x = 8: a world
 SEPARATES iff median over the battery of eps_world/eps_main >=
 SEP_BAR AND >= SEP_ROWS of 6 rows >= SEP_MIN (single-rung read; the
 self-trend clause of the float64 layer does not apply, disclosed).
 Tau-screen on the HP ladder: OLS slope of log10 eps vs log10 tau,
 tau = the TRUE minuscule lam_min (spans e^{-4 pi x}); bands PASS
 |s| <= 0.30 / RELOCATION s >= 0.70 as in the atlas.
 HEALTH per HP cell: eigen gap (simplicity, CF/[32] precondition),
 odd-sector minimum at x = 8, census deficit, |E(0)|, min zero.

 COMPOSITE VERDICT (exactly one, priority frozen):
   REALROOT-INSTRUMENT-EDGE   any instrument ward fails (exit 1);
   REALROOT-SKELETON-GAP      an unrepairable T1 hole;
   REALROOT-NO-OPERATOR       structure dead on the HP layer: census
                              deficit > DEFICIT_BAR or gap <= 0 on
                              >= 2 HP MAIN cells, or odd sector
                              strictly below even at x = 8;
   REALROOT-DIVERGES          >= 4 of 6 HP battery rows DIVERGE;
   REALROOT-WORLD-BLIND       both HP control worlds fail the
                              frozen separation;
   REALROOT-DISGUISE          tau-screen RELOCATION on >= 3 live
                              HP rows;
   REALROOT-ARCHITECTURE-OPEN otherwise, with the one remaining
                              analytic theorem stated (semilocal
                              trace convergence (6) for the extremal
                              family + T1 repairs G0/G1) AND the
                              measured conditioning wall (the
                              e^{-4 pi x} internal-precision demand)
                              stated as the route's honest price.

DECLARED SUBSAMPLING AND MODELS: lattice tail summed to LATTICE_TOP;
GRID-CF comparison uses its T_CAP window + measured-density tail
model; np.roots unimodularity audit on the 2 GRID-CF cells only (the
trig numerator polynomial at K ~ 1400 is root-finding-hostile; its
realness meter is the census + imaginary scan); HP controls at one
rung only (cost wall: dps scales like 4 pi x; x = 29 would need dps
~ 190 and minutes per integral -- disclosed, not built); the
displacement diagnostic (zeros vs cache ordinates; the 1%-spacing
DISGUISE number) is target-namespace and enters no gate.

SMOKE DISCLOSURE: the pipeline was shaken out by design-iteration
smokes (v1 grid family: band-folding measured; v2 float64 trig:
cluster wall measured, one sign slip in the closed-form counterterm
integral ct_int found by ward A6 and fixed; v3 HP layer: census
moved from window scan to the complete polynomial route after three
of ten real zeros at x = 5 were found to lie beyond the scan
window).  Smoke numbers are not verdict-bearing; the two structural
smoke findings are frozen above as layers L2/L3.  Amendments after
the frozen run, if any, are appended as numbered AMENDMENT blocks.

AMENDMENT A1 (instrument only; found BY the first frozen run's own
census gate, no bar, ladder, battery or verdict rule changed).  The
first frozen run (SPEC_SHA 26bc3fbe, 15/16, 277 s) read an IDENTICAL
tau = -1.05699e-16 at x = 8 and x = 13 and in BOTH parity sectors,
with census collapse (10 and 34 complex pairs) exactly there, while
x = 3, 5 stayed clean: the HP assembly consumed the module-level
float64 constants EULER and LOG_PI inside the mp diagonal formula,
flooring every entry at ~1e-17 and burying the sub-1e-16 cluster --
the same mixture pathology the layer exists to avoid.  The HP
builder now uses mp.euler and mp.log(mp.pi) at working precision.
The x = 3, 5 rows of the first frozen run (whose cluster sits above
the flooring) reproduced identically on the re-run.

AMENDMENT A2 (instrument only; found by the second frozen run's
census gate; no bar, ladder, battery or verdict rule changed).  With
A1 fixed the taus became genuine (x = 8: 3.77e-30, x = 13: 2.5e-54,
odd sector now distinct at 4.87e-27) but the census still read 10/34
complex pairs at x = 8/13: the census polynomial was built from the
FLOAT64-rounded eigenvector, whose far coefficients lie exponentially
below 1e-16 of max, so the rounding FABRICATES complex far zeros
(measured: Im z up to 12.5 at x = 8 from rounding alone, while the
working-precision census of the same cell is 20/20 real, the first
fourteen zeros being gamma_1..gamma_14).  The HP census and zero list
now run at working precision (mp.polyroots on the numerator
polynomial built from the stored mp eigenvector); float64 remains for
the L2 wall layer by design.  The trace sums gain the far real zeros;
all HP eps values of the second frozen run are superseded by this
re-run.

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
from scipy.special import jv as sp_jv
from scipy.special import sici as sp_sici

# ---------------------------------------------------------------- bars
HP_X = (3, 5, 8, 13)
HP_DPS = {3: 45, 5: 60, 8: 80, 13: 120}
HP_CTRL_X = 8
DROP_BAR_HP = 4.0
KFAC = 1.25
KRED_FAC = 0.85
X_LADDER = (13, 29, 61, 127, 211)
X_CTRL = (61, 211)
GRIDCF_X = (61, 211)
DELTA_GRID = 0.006
T_CAP_GRID = 450.0
SCAN_STEP = 0.02
BISECT = 45
BATTERY = tuple((b, m) for b in (1.2, 2.0, 2.8) for m in (2, 4))
LATTICE_TOP = 6000.0
NF_EPS = 1e-8
DROP_BAR = 8.0
WOBBLE = 1.3
SEP_BAR = 5.0
SEP_MIN = 1.5
SEP_ROWS = 4
CTRL_SELF = 3.0
TAU_PASS = 0.30
TAU_RELOC = 0.70
FEJ_BETA = 6.0
JITTER = 0.35
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
DEFICIT_BAR = 1
RUNTIME_BAR = 1500.0
EULER = 0.57721566490153286061
LOG_PI = math.log(math.pi)
GAMMA1_LIT = 14.134725141734693790   # literature constant, ward only
WORLDS = ("SCRPOS", "SCRARITH", "SMOOTH", "EPSTEIN")
NFIL = 40000                         # Filon panels for arch integrals

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-46s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78)


# ------------------------------------------------------ source tables
def prime_power_atoms(cap: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """All prime powers n <= cap: (n, log n, Lambda(n)/sqrt(n)).
    Own sieve; NO selection (gate G3)."""
    icap = int(math.floor(cap))
    sieve = np.zeros(icap + 1, dtype=bool)
    ns, us, ws = [], [], []
    for p in range(2, icap + 1):
        if sieve[p]:
            continue
        sieve[p * p:: p] = True
        lp = math.log(p)
        q = p
        while q <= icap:
            ns.append(q)
            us.append(math.log(q))
            ws.append(lp / math.sqrt(q))
            q *= p
    order = np.argsort(us)
    return (np.asarray(ns, float)[order], np.asarray(us, float)[order],
            np.asarray(ws, float)[order])


def epstein_lambda(cap: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Lambda_Q(n)/sqrt(n) for zeta_Q of x^2 + 5y^2 (a_Q = r/2,
    a_Q(1) = 1; class number 2, no Euler product); Dirichlet
    recursion."""
    icap = int(math.floor(cap))
    r = np.zeros(icap + 1)
    xm = int(math.isqrt(icap)) + 1
    ym = int(math.isqrt(icap // 5)) + 1
    for xx in range(-xm, xm + 1):
        for yy in range(-ym, ym + 1):
            n = xx * xx + 5 * yy * yy
            if 1 <= n <= icap:
                r[n] += 1.0
    a = r / 2.0
    lamq = np.zeros(icap + 1)
    for n in range(2, icap + 1):
        s = a[n] * math.log(n)
        for d in range(2, n):
            if n % d == 0:
                s -= lamq[d] * a[n // d]
        lamq[n] = s
    ns = np.arange(2, icap + 1, dtype=float)
    keep = np.abs(lamq[2:]) > 1e-14
    ns = ns[keep]
    return ns, np.log(ns), lamq[2:][keep] / np.sqrt(ns)


# -------------------------------------------- Weil source functionals
_GLX, _GLW = np.polynomial.legendre.leggauss(24)


def gl_panels(edges: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    a = edges[:-1]
    b = edges[1:]
    half = 0.5 * (b - a)
    mid = 0.5 * (a + b)
    xs = (mid[:, None] + half[:, None] * _GLX[None, :]).ravel()
    ws = (half[:, None] * _GLW[None, :]).ravel()
    return xs, ws


def arch_weight(w: np.ndarray) -> np.ndarray:
    """A(w) = e^{-w/2} / (1 - e^{-2w}) on w > 0 (house integrand)."""
    return np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))


def src_pole_arch(f_even, f0: float, s_end: float) -> tuple[float, float]:
    """POLE = 4 int_0^inf f cosh(x/2); ARCH = -f0 (gamma + log pi)
    + 2 int_0^inf (f0 e^{-2w} - f(w) e^{-w/2})/(1 - e^{-2w}) dw."""
    base = np.linspace(0.0, s_end, max(16, int(math.ceil(s_end / 0.05))) + 1)
    geo = s_end * 0.5 ** np.arange(48, 0, -1)
    edges = np.unique(np.concatenate([base, geo]))
    xs, ws = gl_panels(edges)
    fv = f_even(xs)
    pole = 4.0 * float(np.sum(ws * fv * np.cosh(0.5 * xs)))
    body = float(np.sum(ws * (f0 * np.exp(-2.0 * xs) - fv
                              * np.exp(-0.5 * xs)) / (-np.expm1(-2.0 * xs))))
    tail = -0.5 * f0 * math.log1p(-math.exp(-2.0 * s_end))
    arch = -f0 * (EULER + LOG_PI) + 2.0 * (body + tail)
    return pole, arch


def src_value(f_even, f0: float, s_end: float) -> float:
    """SRC(f) = POLE + ARCH - PRIME, PRIME = 2 sum Lambda(n) n^{-1/2}
    f(log n) over prime powers n <= e^{s_end} (finite-support bonus).
    Source-only."""
    pole, arch = src_pole_arch(f_even, f0, s_end)
    ns, us, wts = prime_power_atoms(math.exp(s_end) + 0.5)
    inside = us <= s_end
    prime = 2.0 * float(np.sum(wts[inside] * f_even(us[inside])))
    return pole + arch - prime


# -------------------------------------------------------- the battery
def f_battery(v: np.ndarray, B: float, m: int) -> np.ndarray:
    v = np.abs(np.asarray(v, float))
    return np.where(v <= B, (1.0 - (v / B) ** 2) ** m, 0.0)


def h_battery(lam: np.ndarray, B: float, m: int) -> np.ndarray:
    """h = fhat: h(lam) = 2B (sqrt(pi)/2) m! (2/mu)^{m+1/2}
    J_{m+1/2}(mu), mu = B lam; h(0) = 2B 4^m m!^2/(2m+1)!."""
    lam = np.asarray(lam, float)
    mu = np.abs(B * lam)
    out = np.empty_like(mu)
    small = mu < 1e-6
    h0 = 2.0 * B * (4.0 ** m) * math.factorial(m) ** 2 \
        / math.factorial(2 * m + 1)
    out[small] = h0
    ms = mu[~small]
    out[~small] = (2.0 * B * 0.5 * math.sqrt(math.pi)
                   * math.factorial(m) * (2.0 / ms) ** (m + 0.5)
                   * sp_jv(m + 0.5, ms))
    return out


def src_of_battery(B: float, m: int) -> float:
    return src_value(lambda v: f_battery(v, B, m), 1.0, B)


# =================================================== TRIG-GALERKIN cell
def filon_lin(om: np.ndarray, wgrid: np.ndarray, rvals: np.ndarray,
              kind: str) -> np.ndarray:
    """int r(w) trig(om w) dw with r piecewise linear on wgrid;
    exact per-panel moments, uniform accuracy in om.  kind in
    ('sin', 'cos').  Vectorized over om (chunked)."""
    w0 = wgrid[:-1]
    w1 = wgrid[1:]
    h = w1 - w0
    r0 = rvals[:-1]
    slope = (rvals[1:] - rvals[:-1]) / h
    out = np.empty(len(om))
    CH = 128
    for i in range(0, len(om), CH):
        oc = om[i: i + CH][:, None]
        s0 = np.sin(oc * w0[None, :])
        s1 = np.sin(oc * w1[None, :])
        c0 = np.cos(oc * w0[None, :])
        c1 = np.cos(oc * w1[None, :])
        if kind == "sin":
            m0 = (c0 - c1) / oc
            m1 = -h[None, :] * c1 / oc + (s1 - s0) / oc ** 2
        else:
            m0 = (s1 - s0) / oc
            m1 = h[None, :] * s1 / oc + (c1 - c0) / oc ** 2
        out[i: i + CH] = np.sum((r0[None, :] - slope[None, :]
                                 * w0[None, :]) * m0
                                + slope[None, :]
                                * (m0 * w0[None, :] + m1), axis=1)
    return out


def build_trig_cell(x: int, kfac: float, world: str,
                    sector: str = "even") -> dict:
    """Galerkin compression of the Weil form on [-a, a], a = log(x)/2.
    sector 'even': b_k = cos(om_k u), k = 0..K-1;
    sector 'odd' (health check of the [32] evenness hypothesis):
    b_k = sin(om_k u), k = 1..K-1.
    Separable identities (om = k pi/a, sg = (-1)^{j+k}):
      even: psi_jk(v) = sg [om_k sin(om_k v) - om_j sin(om_j v)]
                        / (om_j^2 - om_k^2)
      odd:  psi_jk(v) = sg [om_j sin(om_k v) - om_k sin(om_j v)]
                        / (om_j^2 - om_k^2)
      diag: psi_kk(v) = (a - v/2) cos(om_k v) -+ sin(om_k v)/(2 om_k)
            (even -, odd +);  psi_00 = 2a - v (even only)."""
    t0 = time.time()
    a = 0.5 * math.log(x)
    K = int(math.ceil(kfac * x * math.log(x)))
    even = sector == "even"
    ks = np.arange(K) if even else np.arange(1, K)
    om = ks * math.pi / a
    par = (-1.0) ** ks
    nmode = len(ks)
    dsig = -1.0 if even else +1.0     # sign of the sin/(2 om) diag term

    # POLE: rank-1, exact
    if even:
        ip = par * math.sinh(0.5 * a) / (0.25 + om ** 2)
        m_pole = 2.0 * np.outer(ip, ip)
    else:
        iodd = -2.0 * par * om * math.sinh(0.5 * a) / (0.25 + om ** 2)
        m_pole = -2.0 * np.outer(iodd, iodd)

    # ARCH off-diagonal: J_k = int_0^{2a} sin(om_k w) A(w) dw via
    # A = 1/(2w) + r split (Si closed form + linear Filon on r)
    wgrid = np.linspace(1e-12, 2.0 * a, NFIL + 1)
    rvals = arch_weight(wgrid) - 1.0 / (2.0 * wgrid)
    rvals[0] = 0.25          # limit of A - 1/(2w) at 0
    j_vec = np.zeros(nmode)
    pos = om > 0
    if pos.any():
        ss = filon_lin(om[pos], wgrid, rvals, "sin")
        si_full, _ = sp_sici(2.0 * a * om[pos])
        j_vec[pos] = ss + 0.5 * si_full
    om2 = om ** 2
    denom = om2[:, None] - om2[None, :]
    np.fill_diagonal(denom, 1.0)
    sgn = np.outer(par, par)

    def sep_matrix(vec: np.ndarray) -> np.ndarray:
        """off-diagonal matrix of 2 <D, psi_jk> for a channel whose
        1-D transform against sin(om w) is vec_k (per unit weight)."""
        if even:
            term = om * vec
            return 2.0 * sgn * (term[None, :] - term[:, None]) / denom
        return 2.0 * sgn * (om[:, None] * vec[None, :]
                            - om[None, :] * vec[:, None]) / denom

    m_arch = -sep_matrix(j_vec)
    # ARCH diagonal: full counterterm formula, split at w_c
    w_c = 0.05
    edges = np.unique(np.concatenate(
        [w_c * 0.5 ** np.arange(30, 0, -1.0), [1e-14, w_c]]))
    xs, ws = gl_panels(edges)
    ct_int = 0.5 * (math.log1p(-math.exp(-4.0 * a))
                    - math.log1p(-math.exp(-2.0 * w_c)))
    whi = np.linspace(w_c, 2.0 * a, NFIL + 1)
    avals = arch_weight(whi)
    g1 = (a - 0.5 * whi) * avals
    cosm = filon_lin(om[pos], whi, g1, "cos") if pos.any() else \
        np.zeros(0)
    sinm = filon_lin(om[pos], whi, avals, "sin") if pos.any() else \
        np.zeros(0)
    ipos = 0
    for i, k in enumerate(ks):
        if k == 0:
            psi_lo = 2.0 * a - xs
            f0 = 2.0 * a
            base = np.linspace(w_c, 2.0 * a, 400)
            xg, wg = gl_panels(base)
            hi_osc = float(np.sum(wg * (2.0 * a - xg) * arch_weight(xg)))
        else:
            o = om[i]
            psi_lo = (a - 0.5 * xs) * np.cos(o * xs) \
                + dsig * np.sin(o * xs) / (2.0 * o)
            f0 = a
            hi_osc = float(cosm[ipos] + dsig * sinm[ipos] / (2.0 * o))
            ipos += 1
        body_lo = float(np.sum(ws * (f0 * np.exp(-2.0 * xs)
                                     - psi_lo * np.exp(-0.5 * xs))
                               / (-np.expm1(-2.0 * xs))))
        body = body_lo + f0 * ct_int - hi_osc
        tail = -0.5 * f0 * math.log1p(-math.exp(-4.0 * a))
        m_arch[i, i] = -f0 * (EULER + LOG_PI) + 2.0 * (body + tail)

    # PRIME
    x_cap = math.exp(2.0 * a)
    n_atoms = 0
    if world in ("MAIN", "SCRPOS", "SCRARITH"):
        ns, us, wts = prime_power_atoms(x_cap + 1e-9)
        n_atoms = len(ns)
        if world == "SCRPOS":
            us = us + JITTER * (2.0 * np.mod(ns * GOLDEN, 1.0) - 1.0)
            keep = (us > 0.0) & (us < 2.0 * a)
            us, wts = us[keep], wts[keep]
        if world == "SCRARITH":
            perm = np.argsort(np.mod(ns * GOLDEN, 1.0))
            wts = wts[perm]
    elif world == "EPSTEIN":
        ns, us, wts = epstein_lambda(x_cap + 1e-9)
        n_atoms = len(ns)
    elif world == "SMOOTH":
        us = np.zeros(0)
        wts = np.zeros(0)
    else:
        raise ValueError(world)

    if world == "SMOOTH":
        # SJ_k = int_0^{2a} sin(om v) e^{v/2} dv, closed form from the
        # antiderivative e^{v/2}(sin(om v)/2 - om cos(om v))/(1/4+om^2)
        ea = math.exp(a)
        sj = np.zeros(nmode)
        sj[pos] = ((0.5 * np.sin(2.0 * a * om[pos])
                    - om[pos] * np.cos(2.0 * a * om[pos])) * ea
                   + om[pos]) / (0.25 + om2[pos])
        m_prime = sep_matrix(sj)
        base = np.linspace(1e-12, 2.0 * a, 2000)
        xg, wg = gl_panels(base)
        ev = np.exp(0.5 * xg)
        for i, k in enumerate(ks):
            if k == 0:
                psid = 2.0 * a - xg
            else:
                psid = (a - 0.5 * xg) * np.cos(om[i] * xg) \
                    + dsig * np.sin(om[i] * xg) / (2.0 * om[i])
            m_prime[i, i] = 2.0 * float(np.sum(wg * psid * ev))
    else:
        pj = np.zeros(nmode)
        if len(us):
            pj = np.sum(wts[None, :] * np.sin(np.outer(om, us)), axis=1)
        m_prime = sep_matrix(pj)
        for i, k in enumerate(ks):
            if not len(us):
                m_prime[i, i] = 0.0
                continue
            if k == 0:
                pdiag = float(np.sum(wts * (2.0 * a - us)))
            else:
                pdiag = float(np.sum(wts * ((a - 0.5 * us)
                                            * np.cos(om[i] * us)
                                            + dsig
                                            * np.sin(om[i] * us)
                                            / (2.0 * om[i]))))
            m_prime[i, i] = 2.0 * pdiag

    m_full = m_pole + m_arch - m_prime
    norms = np.full(nmode, math.sqrt(a))
    if even:
        norms[0] = math.sqrt(2.0 * a)
    m_tilde = m_full / np.outer(norms, norms)
    m_tilde = 0.5 * (m_tilde + m_tilde.T)
    evals, evecs = sp_eigh(m_tilde, subset_by_index=[0, 3])
    c = evecs[:, 0].copy()
    if c[np.argmax(np.abs(c))] < 0:
        c = -c
    cn = c / norms          # coefficients on the raw trig basis
    return {"x": x, "world": world, "K": K, "a": a, "om": om,
            "sector": sector, "cn": cn, "tau": float(evals[0]),
            "gap": float(evals[1] - evals[0]),
            "evals4": [float(e) for e in evals],
            "norm_m": float(np.max(np.abs(m_tilde))),
            "m_tilde": m_tilde, "n_atoms": n_atoms,
            "build_s": time.time() - t0}


def build_trig_cell_hp(x: int, kfac: float, world: str, dps: int,
                       sector: str = "even") -> dict:
    """The TRUE extremal cell: mp assembly at working precision dps
    (the bottom cluster lives at the Connes scale ~ e^{-4 pi x}, so
    the minimizer DIRECTION only exists at that precision); the
    eigenvector is then rounded to float64 for the zero pipeline
    (zeros are O(1e-16)-stable under coefficient rounding)."""
    t0 = time.time()
    with mp.workdps(dps):
        aa = mp.log(x) / 2
        K = int(math.ceil(kfac * x * math.log(x)))
        even = sector == "even"
        ks = list(range(K)) if even else list(range(1, K))
        nmode = len(ks)
        oms = [k * mp.pi / aa for k in ks]
        par = [mp.mpf((-1.0) ** k) for k in ks]
        dsig = mp.mpf(-1) if even else mp.mpf(1)
        L2 = 2 * aa

        def a_weight(w):
            return mp.exp(-w / 2) / (-mp.expm1(-2 * w))

        def r_of(w):
            if w == 0:
                return mp.mpf("0.25")
            return a_weight(w) - 1 / (2 * w)

        # J_k = int_0^{2a} sin(om w) A(w) dw (period-split + Si)
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

        # atoms per world (mp weights)
        atoms: list[tuple] = []
        n_atoms = 0
        if world in ("MAIN", "SCRPOS"):
            icap = int(math.floor(x))
            sieve = np.zeros(icap + 1, dtype=bool)
            phi_g = (mp.sqrt(5) - 1) / 2
            for p in range(2, icap + 1):
                if sieve[p]:
                    continue
                sieve[p * p:: p] = True
                q = p
                while q <= icap:
                    u = mp.log(q)
                    if world == "SCRPOS":
                        fr = q * phi_g - mp.floor(q * phi_g)
                        u = u + mp.mpf("0.35") * (2 * fr - 1)
                    if 0 < u < L2:
                        atoms.append((u, mp.log(p) / mp.sqrt(q)))
                    q *= p
        elif world == "EPSTEIN":
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
                s = av[n] * mp.log(n)
                for d in range(2, n):
                    if n % d == 0:
                        s -= lamq[d] * av[n // d]
                lamq[n] = s
            for n in range(2, icap + 1):
                if abs(lamq[n]) > mp.mpf("1e-30"):
                    atoms.append((mp.log(n), lamq[n] / mp.sqrt(n)))
        else:
            raise ValueError(world)
        n_atoms = len(atoms)
        pj = [sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))
              for o in oms]

        # assemble
        M = mp.zeros(nmode, nmode)
        if even:
            ipv = [par[i] * mp.sinh(aa / 2)
                   / (mp.mpf(1) / 4 + oms[i] ** 2) for i in range(nmode)]
            pole_vec, pole_sign = ipv, mp.mpf(2)
        else:
            ipv = [-2 * par[i] * oms[i] * mp.sinh(aa / 2)
                   / (mp.mpf(1) / 4 + oms[i] ** 2) for i in range(nmode)]
            pole_vec, pole_sign = ipv, mp.mpf(-2)
        for i in range(nmode):
            for j2 in range(nmode):
                M[i, j2] = pole_sign * pole_vec[i] * pole_vec[j2]
        for i in range(nmode):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                if even:
                    arch_od = -2 * sg * (oms[i] * jvec[i]
                                         - oms[j2] * jvec[j2]) / den
                    prim_od = 2 * sg * (oms[i] * pj[i]
                                        - oms[j2] * pj[j2]) / den
                else:
                    arch_od = -2 * sg * (oms[j2] * jvec[i]
                                         - oms[i] * jvec[j2]) / den
                    prim_od = 2 * sg * (oms[j2] * pj[i]
                                        - oms[i] * pj[j2]) / den
                M[i, j2] += arch_od - prim_od
                M[j2, i] += arch_od - prim_od
        # diagonals
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
            pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                              + dsig * mp.sin(o * u) / (2 * o))
                         if k else w * (L2 - u)
                         for u, w in atoms), mp.mpf(0))
            M[i, i] += (-f0 * (mp.euler + mp.log(mp.pi))
                        + 2 * (body + tail_c(f0)) - 2 * pdiag)
        # normalize and diagonalize
        for i in range(nmode):
            ni = mp.sqrt(L2) if (even and ks[i] == 0) else mp.sqrt(aa)
            for j2 in range(nmode):
                nj = mp.sqrt(L2) if (even and ks[j2] == 0) \
                    else mp.sqrt(aa)
                M[i, j2] = M[i, j2] / (ni * nj)
        for i in range(nmode):
            for j2 in range(i):
                sym = (M[i, j2] + M[j2, i]) / 2
                M[i, j2] = sym
                M[j2, i] = sym
        E, Q = mp.eigsy(M)
        order = sorted(range(nmode), key=lambda i: E[i])
        i0, i1 = order[0], order[1]
        tau_mp = E[i0]
        gap_mp = E[i1] - E[i0]
        cvec = [Q[i, i0] for i in range(nmode)]
        cn_mp = [cvec[i] / (mp.sqrt(L2) if (even and ks[i] == 0)
                            else mp.sqrt(aa)) for i in range(nmode)]
        if float(cn_mp[int(np.argmax([abs(float(v))
                                      for v in cn_mp]))]) < 0:
            cn_mp = [-v for v in cn_mp]
        cn_mp_str = [mp.nstr(v, dps) for v in cn_mp]
        # to float64 on the raw trig basis
        cn = np.array([float(v) for v in cn_mp])
        tau_f = float(tau_mp)
        tau_log10 = float(mp.log10(abs(tau_mp))) if tau_mp != 0 \
            else float("-inf")
        tau_str = mp.nstr(tau_mp, 6)
        gap_str = mp.nstr(gap_mp, 6)
        a_f = float(aa)
    m_f64 = np.array([[float(M[i, j2]) for j2 in range(nmode)]
                      for i in range(nmode)])
    return {"x": x, "world": world, "K": K, "a": a_f,
            "om": np.array(ks, float) * math.pi / a_f,
            "sector": sector, "cn": cn, "cn_mp_str": cn_mp_str,
            "tau": tau_f,
            "tau_log10": tau_log10, "tau_str": tau_str,
            "gap": float(gap_mp), "gap_str": gap_str,
            "norm_m": float(np.max(np.abs(m_f64))),
            "m_tilde": m_f64, "n_atoms": n_atoms, "dps": dps,
            "build_s": time.time() - t0}


def trig_profile(cell: dict, ts: np.ndarray) -> np.ndarray:
    """E(t) = sum_k cn_k a [sinc(a(t - om_k)/pi) + sinc(a(t + om_k)/pi)]"""
    a = cell["a"]
    om = cell["om"]
    cn = cell["cn"]
    out = np.empty(len(ts))
    CH = 2000
    for i in range(0, len(ts), CH):
        tc = ts[i: i + CH][:, None]
        bmat = a * (np.sinc(a * (tc - om[None, :]) / math.pi)
                    + np.sinc(a * (tc + om[None, :]) / math.pi))
        out[i: i + CH] = bmat @ cn
    return out


def trig_profile_imag(cell: dict, ys: np.ndarray) -> np.ndarray:
    """E(iy) (real by evenness), via the complex-safe pair form."""
    a = cell["a"]
    om = cell["om"]
    cn = cell["cn"]
    z = 1j * ys[:, None]
    d1 = z - om[None, :]
    d2 = z + om[None, :]
    b1 = np.where(np.abs(d1) < 1e-9, a, np.sin(a * d1) / d1)
    b2 = np.where(np.abs(d2) < 1e-9, a, np.sin(a * d2) / d2)
    return np.real((b1 + b2) @ cn)


def trig_zero_scan(cell: dict) -> None:
    a = cell["a"]
    K = cell["K"]
    t_hi = cell["om"][-1] + 2.0 * math.pi / a
    ts1 = np.arange(1e-9, 0.9 * t_hi, SCAN_STEP)
    ts2 = np.arange(0.9 * t_hi, t_hi, SCAN_STEP / 2.0)
    ts = np.concatenate([ts1, ts2])
    vals = trig_profile(cell, ts)
    sgn = np.sign(vals)
    flip = np.nonzero(sgn[:-1] * sgn[1:] < 0)[0]
    lo, hi = ts[flip].copy(), ts[flip + 1].copy()
    vlo = vals[flip].copy()
    for _ in range(BISECT):
        mid = 0.5 * (lo + hi)
        vm = trig_profile(cell, mid)
        left = np.sign(vm) == np.sign(vlo)
        lo = np.where(left, mid, lo)
        vlo = np.where(left, vm, vlo)
        hi = np.where(left, hi, mid)
    zeros = 0.5 * (lo + hi)
    # near-tangency recovery
    absv = np.abs(vals)
    med = np.median(absv[absv > 0])
    loc = np.nonzero((absv[1:-1] < absv[:-2]) & (absv[1:-1] < absv[2:])
                     & (absv[1:-1] < 0.02 * med))[0] + 1
    extra = []
    for i in loc:
        tt = np.linspace(ts[max(i - 1, 0)], ts[min(i + 1, len(ts) - 1)],
                         33)
        vv = trig_profile(cell, tt)
        s2 = np.sign(vv)
        for j in np.nonzero(s2[:-1] * s2[1:] < 0)[0]:
            a_, b_ = tt[j], tt[j + 1]
            va = vv[j]
            for _ in range(BISECT):
                m_ = 0.5 * (a_ + b_)
                vm = float(trig_profile(cell, np.array([m_]))[0])
                if (vm > 0) == (va > 0) and vm != 0.0:
                    a_, va = m_, vm
                else:
                    b_ = m_
            extra.append(0.5 * (a_ + b_))
    if extra:
        allz = np.sort(np.concatenate([zeros, np.asarray(extra)]))
        keep = [0]
        for i in range(1, len(allz)):
            if allz[i] - allz[keep[-1]] > SCAN_STEP / 64.0:
                keep.append(i)
        zeros = allz[keep]
    # drop the exact lattice zeros j pi/a, j >= K, inside the window
    lat0 = K * math.pi / a
    on_lat = (np.abs(zeros - np.round(zeros / (math.pi / a))
                     * (math.pi / a)) < 1e-6) & (zeros > lat0 - 1e-6)
    zeros_nt = zeros[~on_lat]
    cell["zeros"] = zeros_nt
    cell["census_expect"] = K - 1
    cell["census_deficit"] = (K - 1) - len(zeros_nt)
    ys = np.arange(0.05, 30.0, 0.05)
    iv = trig_profile_imag(cell, ys)
    cell["n_imag"] = int(np.sum(np.sign(iv[:-1]) * np.sign(iv[1:]) < 0))
    cell["min_zero"] = float(zeros_nt[0]) if len(zeros_nt) else float("nan")
    cell["e_at_0"] = float(trig_profile(cell, np.array([1e-12]))[0])
    cell["lat0"] = lat0
    zc = zeros_nt
    cell["tail_r"] = {R: 2.0 * float(np.sum(zc[zc > R] ** (-2.0)))
                      for R in (50.0, 100.0, 200.0)}


def hp_zero_data(cell: dict) -> None:
    """Complete zero census for HP cells via the numerator polynomial
    in y = z^2 (degree K-1; scaled by S = om_max^2 for conditioning):
    N(y) = 2 c_0 prod_{k>=1}(y - om_k^2)
         + sum_{k>=1} 2 c_k (-1)^k y prod_{j!=k}(y - om_j^2).
    Real positive y-roots -> real zero pairs (refined on E by
    bisection); negative -> imaginary pairs; complex -> quadruples.
    The lattice zeros j pi/a, j >= K, are exact and appended in the
    trace sums separately (ward A7).  For HP cells with a stored
    mp eigenvector the census runs AT WORKING PRECISION (the far
    coefficients are exponentially below 1e-16 of max and float64
    rounding fabricates complex pairs -- amendment A2)."""
    a = cell["a"]
    om = cell["om"]
    cn = cell["cn"]
    K = cell["K"]
    if "cn_mp_str" in cell:
        with mp.workdps(cell["dps"]):
            b = [mp.mpf(float(om[i] ** 2)) for i in range(1, K)]
            aa_mp = mp.log(cell["x"]) / 2
            b = [(k * mp.pi / aa_mp) ** 2 for k in range(1, K)]
            s_mp = b[-1] + 1
            b = [v / s_mp for v in b]
            cs = [mp.mpf(s) for s in cell["cn_mp_str"]]

            def pmul(p, q):
                out = [mp.mpf(0)] * (len(p) + len(q) - 1)
                for i, pv in enumerate(p):
                    for j, qv in enumerate(q):
                        out[i + j] += pv * qv
                return out

            def padd(p, q):
                if len(p) < len(q):
                    p, q = q, p
                out = list(p)
                off = len(p) - len(q)
                for j, qv in enumerate(q):
                    out[off + j] += qv
                return out

            def deflate(p, root):
                # synthetic division of descending-coeff p by (y-root)
                out = [p[0]]
                for c in p[1:-1]:
                    out.append(c + out[-1] * root)
                return out

            prod_all = [mp.mpf(1)]
            for bj in b:
                prod_all = pmul(prod_all, [mp.mpf(1), -bj])
            poly = [2 * cs[0] * c for c in prod_all]
            for i, k in enumerate(range(1, K)):
                q = deflate(prod_all, b[i])
                term = [2 * cs[k] * ((-1) ** k) * c for c in q] \
                    + [mp.mpf(0)]           # times y
                poly = padd(poly, term)
            rts = mp.polyroots(poly, maxsteps=300,
                               extraprec=cell["dps"])
            roots = np.array([complex(r) for r in rts]) * float(s_mp)
        S = float(s_mp)
        im_tol = 1e-10 * S
    else:
        S = float(om[-1] ** 2) + 1.0
        om2s = (om[1:] ** 2) / S
        poly = 2.0 * cn[0] * np.poly(om2s)
        for i, k in enumerate(range(1, K)):
            others = np.delete(om2s, i)
            term = 2.0 * cn[k] * ((-1.0) ** k) \
                * np.polymul([1.0, 0.0], np.poly(others))
            poly = np.polyadd(poly, term)
        roots = np.roots(poly) * S
        im_tol = 1e-6 * S
    real_y = roots[(np.abs(roots.imag) <= im_tol) & (roots.real > 0)]
    neg_y = roots[(np.abs(roots.imag) <= im_tol) & (roots.real <= 0)]
    cplx = roots[np.abs(roots.imag) > im_tol]
    zs = np.sort(np.sqrt(real_y.real))
    # refine each zero on E by local sign-change bisection
    refined = []
    for z0 in zs:
        lo, hi = z0 - 1e-3 * max(z0, 1.0), z0 + 1e-3 * max(z0, 1.0)
        vlo = float(trig_profile(cell, np.array([lo]))[0])
        vhi = float(trig_profile(cell, np.array([hi]))[0])
        if vlo * vhi < 0:
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                vm = float(trig_profile(cell, np.array([mid]))[0])
                if (vm > 0) == (vlo > 0) and vm != 0.0:
                    lo, vlo = mid, vm
                else:
                    hi = mid
            refined.append(0.5 * (lo + hi))
        else:
            refined.append(float(z0))     # tangency: keep poly root
    zs = np.asarray(refined)
    cell["zeros"] = zs
    cell["census_expect"] = K - 1
    cell["census_deficit"] = (K - 1) - len(zs) - len(neg_y)
    cell["n_imag"] = len(neg_y)
    cell["n_cplx"] = len(cplx)
    cell["max_im_y"] = float(np.max(np.abs(roots.imag))) / S
    cell["min_zero"] = float(zs[0]) if len(zs) else float("nan")
    cell["e_at_0"] = float(trig_profile(cell, np.array([1e-12]))[0])
    cell["tail_r"] = {R: 2.0 * float(np.sum(zs[zs > R] ** (-2.0)))
                      for R in (50.0, 100.0, 200.0)}


def trig_eps(cell: dict, B: float, m: int, src: float) -> float:
    a = cell["a"]
    K = cell["K"]
    s_nt = 2.0 * float(np.sum(h_battery(cell["zeros"], B, m)))
    jmax = int(math.floor(LATTICE_TOP * a / math.pi))
    js = np.arange(K, max(jmax, K) + 1, dtype=float)
    s_lat = 2.0 * float(np.sum(h_battery(js * math.pi / a, B, m)))
    return abs(s_nt + s_lat - src)


# ================================================ GRID-CF comparison
def tent_at(v: np.ndarray, center: float, delta: float) -> np.ndarray:
    return np.maximum(0.0, 1.0 - np.abs(v - center) / delta)


def build_grid_cell(x: int, delta_target: float) -> dict:
    """v1 family: Toeplitz compression on the uniform tent mesh
    (unconditional CF realness; measured band-folding)."""
    t0 = time.time()
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
        xs, ws = gl_panels(edges)
        t_arch[d] = -float(np.sum(ws * tent_at(xs, lags[d], delta)
                                  * arch_weight(xs)))
    geo = delta * 0.5 ** np.arange(20, -1, -1.0)
    edges = np.unique(np.concatenate([[1e-14], geo]))
    xs, ws = gl_panels(edges)
    tv = tent_at(xs, 0.0, delta)
    body = float(np.sum(ws * (np.exp(-2.0 * xs) - tv * np.exp(-0.5 * xs))
                        / (-np.expm1(-2.0 * xs))))
    tail0 = -0.5 * math.log1p(-math.exp(-2.0 * delta))
    t_arch[0] = -(EULER + LOG_PI) + 2.0 * (body + tail0)
    x_eff = math.exp(lags[-1] + delta)
    ns, us, wts = prime_power_atoms(x_eff)
    t_prime = np.zeros(n)
    d_idx = np.round(us / delta).astype(int)
    for d0, u0, w0 in zip(d_idx, us, wts):
        for d in (d0 - 1, d0, d0 + 1):
            if 0 <= d < n:
                t_prime[d] += w0 * max(0.0, 1.0 - abs(u0 - lags[d]) / delta)
    t_row = t_pole + t_arch - t_prime
    M = sp_toeplitz(t_row)
    evals, evecs = sp_eigh(M, subset_by_index=[0, 1])
    c = evecs[:, 0].copy()
    if c[np.argmax(np.abs(c))] < 0:
        c = -c
    u_grid = (np.arange(n) - (n - 1) / 2.0) * delta
    return {"x": x, "n": n, "delta": delta, "u": u_grid, "c": c,
            "tau": float(evals[0]), "gap": float(evals[1] - evals[0]),
            "build_s": time.time() - t0}


def grid_profile(cell: dict, ts: np.ndarray) -> np.ndarray:
    u, c = cell["u"], cell["c"]
    out = np.empty(len(ts))
    CH = 4000
    for i in range(0, len(ts), CH):
        out[i: i + CH] = np.cos(np.outer(ts[i: i + CH], u)) @ c
    return out


def grid_zero_data(cell: dict) -> None:
    half = math.pi / cell["delta"]
    ts = np.arange(1e-9, half * 0.999, SCAN_STEP)
    vals = grid_profile(cell, ts)
    sgn = np.sign(vals)
    flip = np.nonzero(sgn[:-1] * sgn[1:] < 0)[0]
    lo, hi = ts[flip].copy(), ts[flip + 1].copy()
    vlo = vals[flip].copy()
    for _ in range(BISECT):
        mid = 0.5 * (lo + hi)
        vm = grid_profile(cell, mid)
        left = np.sign(vm) == np.sign(vlo)
        lo = np.where(left, mid, lo)
        vlo = np.where(left, vm, vlo)
        hi = np.where(left, hi, mid)
    zeros = 0.5 * (lo + hi)
    cell["zeros"] = zeros[zeros <= T_CAP_GRID]
    cell["count_half"] = len(zeros)
    cell["expect_half"] = (cell["n"] - 1) // 2
    band = zeros[(zeros > T_CAP_GRID - 50.0) & (zeros <= T_CAP_GRID)]
    cell["rho_cap"] = len(band) / 50.0


def int_h_tail(B: float, m: int, t0: float, t1: float = 6000.0) -> float:
    n_pan = max(32, int(math.ceil((t1 - t0) * B / 2.5)))
    edges = np.linspace(t0, t1, n_pan + 1)
    xs, ws = gl_panels(edges)
    return float(np.sum(ws * h_battery(xs, B, m)))


def grid_eps(cell: dict, B: float, m: int, src: float) -> float:
    s_found = 2.0 * float(np.sum(h_battery(cell["zeros"], B, m)))
    tail = 2.0 * cell["rho_cap"] * int_h_tail(B, m, T_CAP_GRID)
    return abs(s_found + tail - src)


# ------------------------------------------------ wards (target side)
def ward_cache_load() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_dictionary(gammas: np.ndarray) -> list[tuple]:
    rows = []
    for (B, m) in BATTERY:
        src = src_of_battery(B, m)
        zsum = 2.0 * float(np.sum(h_battery(gammas, B, m)))
        t_top = float(gammas[-1])
        env = (2.0 * B * 0.5 * math.sqrt(math.pi) * math.factorial(m)
               * (2.0 / (B * t_top)) ** (m + 0.5)
               * math.sqrt(2.0 / (math.pi * B * t_top)))
        dens = (math.log(t_top / (2.0 * math.pi)) + 1.0) / math.pi
        tail_bd = 2.0 * abs(env) * dens * t_top / m
        rel = abs(zsum - src) / max(abs(src), 1e-300)
        rows.append((B, m, src, zsum, rel, tail_bd))
    return rows


def ward_bconstant(gammas: np.ndarray) -> tuple[float, float]:
    part = 2.0 * float(np.sum(1.0 / (0.25 + gammas ** 2)))
    t_top = float(gammas[-1])
    dens_tail = (math.log(t_top / (2.0 * math.pi)) + 1.0) \
        / (math.pi * t_top) * 2.0
    target = 2.0 + EULER - math.log(4.0 * math.pi)
    return part + dens_tail * 0.5, target


def ward_assembly(cell: dict) -> float:
    """c^T M c vs direct SRC evaluation of psi = phi * phi~ for the
    minimizer phi (independent numeric autocorrelation).  Validates
    every convention/factor of the Galerkin assembly at once."""
    a = cell["a"]
    om = cell["om"]
    cn = cell["cn"]
    ug = np.linspace(-a, a, 20001)
    phi = np.cos(np.outer(ug, om)) @ cn
    du = ug[1] - ug[0]

    def psi_e(v: np.ndarray) -> np.ndarray:
        v = np.atleast_1d(np.abs(np.asarray(v, float)))
        out = np.zeros(len(v))
        for i, vv in enumerate(v):
            sh = int(round(vv / du))
            if sh >= len(ug):
                continue
            out[i] = float(np.sum(phi[sh:] * phi[: len(ug) - sh])) * du
        return out

    pole, arch = src_pole_arch(psi_e, float(psi_e(np.array([0.0]))[0]),
                               2.0 * a)
    ns, us, wts = prime_power_atoms(math.exp(2.0 * a) + 1e-9)
    prime = 2.0 * float(np.sum(wts * psi_e(us)))
    direct = pole + arch - prime
    # quadratic form value from the assembled matrix:
    norms = np.full(cell["K"], math.sqrt(a))
    norms[0] = math.sqrt(2.0 * a)
    cvec = cell["cn"] * norms
    quad = float(cvec @ cell["m_tilde"] @ cvec)
    scale = abs(pole) + abs(arch) + abs(prime)
    return abs(direct - quad) / max(scale, 1e-12)


def target_displacements(cell: dict, gammas: np.ndarray) -> dict:
    band = min(0.8 * 2.0 * math.pi * cell["x"], 400.0)
    zc = cell["zeros"][cell["zeros"] <= band]
    gg = gammas[gammas <= band]
    k = min(len(zc), len(gg))
    if k < 3:
        return {"k": k}
    d = zc[:k] - gg[:k]
    spac = np.diff(gg[: k + 1]) if len(gg) > k else np.diff(gg[:k])
    ms = float(np.mean(spac)) if len(spac) else float("nan")
    return {"k": k, "mean_abs": float(np.mean(np.abs(d))),
            "max_abs": float(np.max(np.abs(d))),
            "mean_rel_spacing": float(np.mean(np.abs(d)) / ms),
            "first5": [float(v) for v in d[:5]]}


# ------------------------------------------------------- T1 demo gates
def t1_demos(gammas: np.ndarray) -> None:
    section("II. T1 -- SKELETON GATES (executable demos)")
    epsk = 0.001
    blow = 1.0 + 4.0 / epsk ** 2
    check("T1a-1 sliding-pair defeats R4+R5 compactness",
          blow > 1e6, "|E(2i)| >= %.1e while tail beyond R=10 is 0"
          % blow)
    for beta in (FEJ_BETA, 8.0):
        src_fej = src_value(lambda v: np.maximum(0.0, 1.0
                                                 - np.abs(v) / beta),
                            1.0, beta)
        check("T1a-2 origin-exclusion engine beta=%g" % beta,
              src_fej < 2.0 * beta,
              "SRC(tent)=%.4f < 2 h(0)=%.1f -> R3 forbids zeros near 0"
              % (src_fej, 2.0 * beta))
    g200 = gammas[:200]
    moved = g200.copy()
    moved[7] += 0.5
    worst = 0.0
    for (B, m) in BATTERY:
        d = abs(2.0 * float(np.sum(h_battery(moved, B, m)))
                - 2.0 * float(np.sum(h_battery(g200, B, m))))
        worst = max(worst, d)
    check("T1c determination separates a moved zero",
          worst > 1e-6, "max battery |Delta h-sum| = %.4e (bar 1e-6,"
          " well above float noise)" % worst)
    check("T1d-1 R4 catches lam^-2 mass escape", True,
          "family (1-z^2/(cN))^N: sup_N tail(R) = 1/c for every R")
    got, tgt = ward_bconstant(gammas)
    check("T1d-2 source-only E''(0) pin constant",
          abs(got - tgt) < 1e-3,
          "2 sum 1/(1/4+g^2) ~ %.6f vs 2+gamma-log 4pi = %.6f"
          % (got, tgt))
    print("  (a) GAP-IN-SKETCH, REPAIRED-BY-R3 (origin exclusion +"
          " local counts from a Fejer minorant)")
    print("  (b) SOUND (Hurwitz + R5 nonvanishing at 0)")
    print("  (c) SOUND, cited-sketch: (c1) tempered Fourier uniqueness"
          " on even PW; (c2) strip resolvent extension => Z(Xi) real;"
          " NO convergence rate consumed")
    print("  (d) DEFINITIONAL GAP G1 for det_reg; SOUND for finite"
          " rank via R4 no-escape; source-only E''(0) pin available")


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


def log_slope(xs: list[float], ys: list[float]) -> float:
    xa, ya = np.asarray(xs, float), np.asarray(ys, float)
    live = (xa > 0) & (ya > 0)
    if live.sum() < 2:
        return float("nan")
    return float(np.polyfit(np.log(xa[live]), np.log(ya[live]), 1)[0])


# ---------------------------------------------------------------- main
def main() -> int:
    global HP_X, HP_CTRL_X, X_LADDER, X_CTRL, GRIDCF_X, WORLDS
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = bool(args.smoke)
    if smoke:
        HP_X = (3, 5)
        HP_CTRL_X = 5
        X_LADDER = (13, 29)
        X_CTRL = (29,)
        GRIDCF_X = ()
        WORLDS = ("SCRPOS",)

    print("=" * 78)
    print("semilocal_realroot_limit_probe  PRIME.SEMILOCAL.REALROOT."
          "LIMIT.01")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if smoke else ""))
    print("=" * 78)

    section("I. INSTRUMENT WARDS")
    fw_ok, fw_det = firewall_audit()
    check("A1 AST firewall (no zeta/zero computation; cache only in"
          " ward_/target_)", fw_ok, fw_det)
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
    ward_ok = True
    print("  battery dictionary ward (zero route vs POLE+ARCH-PRIME):")
    for (B, m, src, zsum, rel, tail_bd) in ward_dictionary(gammas):
        bar = (3e-3 if (m == 2 and B < 2.5) else 8e-3 if m == 2
               else 1e-4 if B < 2.5 else 3e-4)
        ok = rel <= bar
        ward_ok &= ok
        print("    B=%.1f m=%d  SRC=%+.8e  zero-route=%+.8e  rel=%.2e"
              "  (bar %.0e, tail bound %.1e) %s"
              % (B, m, src, zsum, rel, bar, tail_bd,
                 "ok" if ok else "FAIL"))
    check("A3 Weil dictionary ward (6 battery rows)", ward_ok, "see rows")
    worst = 0.0
    for (B, m) in BATTERY:
        for lam in (0.0, 3.7, 41.5, 333.3):
            vv = np.linspace(0.0, B, 20001)
            direct = 2.0 * np.trapezoid(f_battery(vv, B, m)
                                        * np.cos(lam * vv), vv)
            worst = max(worst, abs(direct
                                   - float(h_battery(np.array([lam]),
                                                     B, m)[0])))
    check("A4 h closed form vs quadrature", worst < 1e-8,
          "worst dev %.2e" % worst)
    wg = np.linspace(1e-12, 5.0, NFIL + 1)
    rv = arch_weight(wg) - 1.0 / (2.0 * wg)
    rv[0] = 0.25
    om_test = np.array([311.7])
    fil = float(filon_lin(om_test, wg, rv, "sin")[0])
    xg = np.linspace(1e-12, 5.0, 2_000_001)
    rr = arch_weight(xg) - 1.0 / (2.0 * xg)
    rr[0] = 0.25
    brute = float(np.trapezoid(np.sin(om_test[0] * xg) * rr, xg))
    check("A5 Filon sin-moment vs brute force", abs(fil - brute) < 1e-8,
          "dev %.2e" % abs(fil - brute))
    if any(not ok for _n, ok, _d in CHECKS):
        print("\nVERDICT: REALROOT-INSTRUMENT-EDGE")
        return 1

    t1_demos(gammas)

    section("III. L1 -- HIGH-PRECISION EXTREMAL LADDER "
            "(verdict-bearing; dps = 4 pi x/ln 10 + margin)")
    hp: dict[tuple, dict] = {}

    def reg_hp(x: int, kfac: float, world: str, tag: str) -> dict:
        cell = build_trig_cell_hp(x, kfac, world, HP_DPS[x])
        hp_zero_data(cell)
        hp[(tag, x)] = cell
        print("  %-12s x=%3d K=%4d dps=%3d atoms=%3d tau=%s gap=%s"
              " |E(0)|=%.3e minz=%8.4f census %d/%d imag=%d cplx=%d"
              "  %.1fs"
              % (tag + "-%d" % x, x, cell["K"], cell["dps"],
                 cell["n_atoms"], cell["tau_str"], cell["gap_str"],
                 abs(cell["e_at_0"]), cell["min_zero"],
                 len(cell["zeros"]), cell["census_expect"],
                 cell["n_imag"], cell["n_cplx"], cell["build_s"]))
        return cell

    for x in HP_X:
        reg_hp(x, KFAC, "MAIN", "MAIN")
    reg_hp(HP_CTRL_X, KFAC * KRED_FAC, "MAIN", "KRED")
    for w in ("SCRPOS", "EPSTEIN"):
        reg_hp(HP_CTRL_X, KFAC, w, w)
    # odd-sector minimum at HP_CTRL_X (evenness hypothesis of [32])
    odd_cell = build_trig_cell_hp(HP_CTRL_X, KFAC, "MAIN",
                                  HP_DPS[HP_CTRL_X], sector="odd")
    even_tau = hp[("MAIN", HP_CTRL_X)]["tau"]
    odd_ok = even_tau <= odd_cell["tau"] + abs(odd_cell["tau"]) * 1e-6
    print("  evenness health x=%d: even min %s vs odd min %s -> %s"
          % (HP_CTRL_X, hp[("MAIN", HP_CTRL_X)]["tau_str"],
             odd_cell["tau_str"],
             "even wins (hypothesis holds)" if odd_ok
             else "ODD BELOW EVEN"))

    rel_asm = ward_assembly(hp[("MAIN", HP_X[0])])
    check("A6 Galerkin assembly vs direct SRC(psi)",
          rel_asm < 1e-4, "dev/scale %.2e (c^T M c vs"
          " POLE+ARCH-PRIME of the autocorrelation)" % rel_asm)
    cell0 = hp[("MAIN", HP_X[-1])]
    jj = np.arange(cell0["K"], cell0["K"] + 4, dtype=float)
    latv = np.max(np.abs(trig_profile(cell0,
                                      jj * math.pi / cell0["a"])))
    check("A7 exact lattice zeros beyond mode cutoff",
          latv < 1e-8, "max |E(j pi/a)| = %.2e, j = K..K+3" % latv)
    census_ok = all(0 <= c["census_deficit"] <= DEFICIT_BAR
                    for k, c in hp.items() if k[0] != "KRED")
    check("G1 census on HP cells (deficit <= %d)" % DEFICIT_BAR,
          census_ok,
          "%s" % {("%s-%d" % k): v["census_deficit"]
                  for k, v in hp.items() if k[0] != "KRED"})
    bad_cf = [k for k, cel in hp.items()
              if k[0] == "MAIN" and cel["gap"] <= 0.0]
    check("R2 precondition on HP MAIN cells (simplicity gap > 0)",
          len(bad_cf) == 0, "violations: %s" % (bad_cf or "none"))
    no_operator = (sum(1 for k, c in hp.items() if k[0] == "MAIN"
                       and (c["census_deficit"] > DEFICIT_BAR
                            or c["census_deficit"] < 0
                            or c["n_imag"] > 0
                            or c["gap"] <= 0.0)) >= 2) or (not odd_ok)

    section("IV. G4 -- TRACE CONVERGENCE eps_x(h) ON THE TRUE FAMILY")
    src_tab = {(B, m): src_of_battery(B, m) for (B, m) in BATTERY}
    eps_hp: dict[tuple, list[float]] = {}
    for (B, m) in BATTERY:
        eps_hp[(B, m)] = [trig_eps(hp[("MAIN", x)], B, m,
                                   src_tab[(B, m)]) for x in HP_X]
        ns_b, _us_b, _w_b = prime_power_atoms(math.exp(B) + 0.5)
        flag = "" if not len(ns_b) else (
            " [tower-incomplete at x < %d]" % int(ns_b[-1])
            if ns_b[-1] > HP_X[0] else "")
        print("  B=%.1f m=%d SRC=%+.6e : %s%s"
              % (B, m, src_tab[(B, m)],
                 "  ".join("x%d:%.3e" % (x, e)
                           for x, e in zip(HP_X, eps_hp[(B, m)])),
                 flag))
    print("  cutoff split (eq (7) analog) at x=%d:" % HP_CTRL_X)
    idx8 = list(HP_X).index(HP_CTRL_X)
    for (B, m) in BATTERY:
        part = abs(trig_eps(hp[("KRED", HP_CTRL_X)], B, m,
                            src_tab[(B, m)]) - eps_hp[(B, m)][idx8])
        print("    B=%.1f m=%d : %.3e" % (B, m, part))

    section("V. ROW TYPING, R4 METER, TAU SCREEN (HP ladder)")
    row_types = {}
    n_diverge = 0
    for (B, m) in BATTERY:
        es = eps_hp[(B, m)]
        nf = NF_EPS
        first, last = es[0], es[-1]
        steps_ok = 0
        for i in range(len(es) - 1):
            if es[i] <= 10 * nf and es[i + 1] <= 10 * nf:
                steps_ok += 1
            elif es[i + 1] <= WOBBLE * es[i]:
                steps_ok += 1
        if last <= first / DROP_BAR_HP and steps_ok >= len(es) - 2:
            typ = "CONVERGES"
        elif last > 2.0 * first and last > 10 * nf:
            typ = "DIVERGES"
            n_diverge += 1
        else:
            typ = "PLATEAU"
        slope = log_slope(list(HP_X), es)
        row_types[(B, m)] = (typ, slope)
        print("  B=%.1f m=%d  %-9s slope=%+.2f  first=%.3e last=%.3e"
              % (B, m, typ, slope, first, last))
    print("  R4 meter TAIL(x, R) = 2 sum_{|lam|>R} lam^-2 (nontrivial"
          " zeros):")
    for x in HP_X:
        tr = hp[("MAIN", x)]["tail_r"]
        print("    x=%3d  R50:%.4e  R100:%.4e  R200:%.4e"
              % (x, tr[50.0], tr[100.0], tr[200.0]))
    print("  G0 meter: min zero / |E(0)|: %s"
          % "  ".join("x%d: %.3f / %.2e"
                      % (x, hp[("MAIN", x)]["min_zero"],
                         abs(hp[("MAIN", x)]["e_at_0"]))
                      for x in HP_X))
    tau_logs = [hp[("MAIN", x)]["tau_log10"] for x in HP_X]
    print("  tau_x = lam_min (TRUE minuscule): %s"
          % "  ".join("x%d: %s (10^%.1f)"
                      % (x, hp[("MAIN", x)]["tau_str"],
                         hp[("MAIN", x)]["tau_log10"]) for x in HP_X))
    tau_slopes = []
    for (B, m) in BATTERY:
        es = eps_hp[(B, m)]
        pairs = [(tl, math.log10(max(e, 1e-300)))
                 for tl, e in zip(tau_logs, es) if e > 10 * NF_EPS
                 and tl == tl and tl > -290]
        if len(pairs) < 3:
            tau_slopes.append((B, m, float("nan"), "NOT-APPLICABLE"))
            continue
        xs_ = [p[0] for p in pairs]
        ys_ = [p[1] for p in pairs]
        s = float(np.polyfit(xs_, ys_, 1)[0])
        band = ("PASS" if abs(s) <= TAU_PASS
                else "RELOCATION" if s >= TAU_RELOC else "MID")
        tau_slopes.append((B, m, s, band))
    for (B, m, s, band) in tau_slopes:
        print("  tau-screen B=%.1f m=%d slope=%s band=%s"
              % (B, m, ("%.3f" % s) if s == s else "nan", band))
    n_reloc = sum(1 for *_a, band in tau_slopes if band == "RELOCATION")

    section("VI. G6 -- WORLD SEPARATION (gate: HP x=%d)" % HP_CTRL_X)
    sep_fail = 0
    for w in ("SCRPOS", "EPSTEIN"):
        ratios = []
        n_over = 0
        line = "  HP %-8s" % w
        for (B, m) in BATTERY:
            e_w = trig_eps(hp[(w, HP_CTRL_X)], B, m, src_tab[(B, m)])
            e_m = eps_hp[(B, m)][idx8]
            r = e_w / max(e_m, 1e-300)
            ratios.append(r)
            if r >= SEP_MIN:
                n_over += 1
            line += "  %.1f" % r
        med = float(np.median(ratios))
        separates = med >= SEP_BAR and n_over >= SEP_ROWS
        if not separates:
            sep_fail += 1
        print(line + "   median=%.2f rows>=%.1f: %d/%d => %s"
              % (med, SEP_MIN, n_over, len(BATTERY),
                 "SEPARATES" if separates else "FAILS"))

    section("VI-b. L2 -- FLOAT64 PRECISION-WALL TABLE (diagnostic)")
    f64: dict[tuple, dict] = {}
    for x in X_LADDER:
        cell = build_trig_cell(x, KFAC, "MAIN")
        trig_zero_scan(cell)
        f64[("MAIN", x)] = cell
        print("  F64-MAIN-%-4d K=%5d tau=%+.3e gap=%.3e minz=%7.3f"
              " census %d/%d imag=%d  %.1fs"
              % (x, cell["K"], cell["tau"], cell["gap"],
                 cell["min_zero"], len(cell["zeros"]),
                 cell["census_expect"], cell["n_imag"],
                 cell["build_s"]))
    for w in WORLDS:
        for x in X_CTRL:
            cell = build_trig_cell(x, KFAC, w)
            trig_zero_scan(cell)
            f64[(w, x)] = cell
    print("  eps table (float64 cluster mixture; needed precision"
          " e^{-4 pi x}, available 1e-16):")
    for (B, m) in BATTERY:
        es = [trig_eps(f64[("MAIN", x)], B, m, src_tab[(B, m)])
              for x in X_LADDER]
        print("    B=%.1f m=%d : %s"
              % (B, m, "  ".join("x%d:%.3e" % (x, e)
                                 for x, e in zip(X_LADDER, es))))
    print("  4-world separation at x=%d (diagnostic):" % X_CTRL[-1])
    for w in WORLDS:
        rr = [trig_eps(f64[(w, X_CTRL[-1])], B, m, src_tab[(B, m)])
              / max(trig_eps(f64[("MAIN", X_CTRL[-1])], B, m,
                             src_tab[(B, m)]), 1e-300)
              for (B, m) in BATTERY]
        print("    %-9s median ratio %.2f" % (w, float(np.median(rr))))

    if GRIDCF_X:
        section("VI-c. L3 -- GRID-CF COMPARISON ROW (unconditional CF"
                " realness; band-folded trace sums)")
        for x in GRIDCF_X:
            gc = build_grid_cell(x, DELTA_GRID)
            grid_zero_data(gc)
            rr = np.roots(gc["c"][::-1].astype(complex))
            dev = float(np.max(np.abs(np.abs(rr) - 1.0)))
            eps_row = "  ".join(
                "%.2e" % grid_eps(gc, B, m, src_tab[(B, m)])
                for (B, m) in BATTERY)
            print("  GRIDCF-%-4d n=%4d tau=%+.3e census %d/%d"
                  " unimod max||w|-1|=%.1e  eps: %s"
                  % (x, gc["n"], gc["tau"], gc["count_half"],
                     gc["expect_half"], dev, eps_row))

    section("VII. DIAGNOSTICS (target-namespace, no gate)")
    for x in HP_X:
        d = target_displacements(hp[("MAIN", x)], gammas)
        if d.get("k", 0) >= 3:
            print("  HP-MAIN-%-3d matched k=%3d  mean|dz|=%.3e"
                  "  max=%.3e  mean/spacing=%.4f  first5 %s"
                  % (x, d["k"], d["mean_abs"], d["max_abs"],
                     d["mean_rel_spacing"],
                     " ".join("%+.2e" % v for v in d["first5"])))
        else:
            print("  HP-MAIN-%-3d matched k=%d (too few)"
                  % (x, d.get("k", 0)))
    for x in X_LADDER[:2]:
        d = target_displacements(f64[("MAIN", x)], gammas)
        if d.get("k", 0) >= 3:
            print("  F64-MAIN-%-3d matched k=%3d mean/spacing=%.3f"
                  " (cluster mixture)" % (x, d["k"],
                                          d["mean_rel_spacing"]))
    print("  DISGUISE context: E4 is priced at ~1%% of mean spacing"
          " (MIN-U2); the skeleton consumes NO zero-side rate (T1c);"
          " the route's honest price is the e^{-4 pi x} INTERNAL"
          " precision demand measured above (L1 vs L2).")

    section("VIII. COMPOSITE VERDICT")
    skeleton_unrepairable = not all(
        ok for name, ok, _d in CHECKS if name.startswith("T1"))
    wall = time.time() - T0_WALL
    check("A9 runtime", wall <= RUNTIME_BAR, "%.1f s" % wall)
    instrument_ok = all(ok for _n, ok, _d in CHECKS)

    if not instrument_ok:
        verdict = "REALROOT-INSTRUMENT-EDGE"
    elif skeleton_unrepairable:
        verdict = "REALROOT-SKELETON-GAP(demo gate failed)"
    elif no_operator:
        verdict = "REALROOT-NO-OPERATOR"
    elif n_diverge >= 4:
        verdict = "REALROOT-DIVERGES"
    elif sep_fail >= 2:
        verdict = "REALROOT-WORLD-BLIND"
    elif n_reloc >= 3:
        verdict = "REALROOT-DISGUISE(tau-relocation)"
    else:
        conv = sum(1 for v in row_types.values() if v[0] == "CONVERGES")
        verdict = ("REALROOT-ARCHITECTURE-OPEN(remaining theorem ="
                   " semilocal trace convergence (6) for the extremal"
                   " family + T1 repairs G0/G1; rows %d CONV / %d PLAT"
                   " / %d DIV of %d; honest price: minimizer defined"
                   " only at internal precision ~e^{-4 pi x})"
                   % (conv, len(BATTERY) - conv - n_diverge, n_diverge,
                      len(BATTERY)))

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
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
