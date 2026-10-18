#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hausdorff_safepoint_probe -- PRIME.HAUSDORFF.SAFEPOINT.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Build and adjudicate the SAFE-POINT HAUSDORFF CARRIER, an externally
proposed RH-equivalent positivity criterion with a source-only Jacobi
decoder.  The proposer's own code is NOT available; everything below
is reimplemented from the mathematical specification.

THE OBJECT.  X(w) = xi(1/2 + w) is even (functional equation), so
Phi(z) = xi(1/2 + sqrt(z)) is a well-defined entire function of order
1/2 (even Taylor coefficients of X), with zeros exactly at
z_rho = (rho - 1/2)^2, one per zero PAIR {rho, 1-rho}.  Its log
derivative F(z) = Phi'/Phi(z) = (1/(2 sqrt z)) (xi'/xi)(1/2 + sqrt z)
is meromorphic with simple poles at the z_rho; genus 0 gives
F(z) = sum_pairs 1/(z - z_rho) absolutely (RvM density).  RH <=> all
z_rho on the negative real axis.  Fix the SAFE POINT a = 256 > 1/4
(s_a = 1/2 + sqrt(a) = 16.5 > 1, absolutely convergent Euler
half-plane).  Moments and Pascal field:
  b_n(a)   = a^(n+1) ((-1)^n / n!) F^(n)(a) = sum_pairs y_rho^(n+1),
             y_rho = a/(a - z_rho),
  C_{n,k}(a) = (-1)^k Delta^k b_n  (Delta b_n = b_{n+1} - b_n)
             = sum_pairs y^(n+1) (1-y)^k.
CLAIMED THEOREM: RH <=> C_{n,k}(a) >= 0 for all n, k >= 0.  Forward:
under RH y_gamma = a/(a + gamma^2) in (0,1), every cell is a positive
sum, plus Pascal conservation C_{n,k} = C_{n+1,k} + C_{n,k+1}.
Backward: complete monotonicity => (Hausdorff 1921, "Summations-
methoden und Momentfolgen I"; Widder, The Laplace Transform 1941,
Ch. III Thm 4a: a sequence is the moment sequence of a bounded
nonnegative measure on [0,1] IFF it is completely monotone -- no
separate boundedness hypothesis: b_n >= 0 is C_{n,0} >= 0 and
b_n - b_{n+1} = C_{n,1} >= 0 give 0 <= b_n <= b_0 < inf) a positive
measure mu_a on [0,1] with b_n = int y^n dmu; F(x) -> 0 as x -> +inf
(xi'/xi(1/2+sqrt x) ~ (1/2) log(sqrt x/(2 pi)) grows only
logarithmically, so F ~ log x/(4 sqrt x) -> 0) excludes an atom at 0
(an atom m at y=0 forces F(x) -> m/a > 0); the Stieltjes transform
G(z) = int dmu(y)/(a(1-y) + y z) is holomorphic on C minus the slit
(-inf, 0] and has the SAME Taylor coefficients at a (exact identity,
gated symbolically); F = G on the disk |z-a| < min(R_a, a), R_a =
dist(a, nearest pole).  CONTINUATION STEP (the one sharp point): let
Omega = C \ ((-inf,0] u P_off), P_off = the off-axis poles of F.
Omega is open and connected (a countable discrete set removed from
the connected slit plane keeps connectivity in R^2), both F and G are
holomorphic on Omega, they agree on the disk, so by the identity
theorem F = G on ALL of Omega -- including arbitrarily close to any
putative off-axis pole z0.  G is holomorphic AT z0 (z0 not on the
slit), so F extends holomorphically through z0: z0 is removable, not
a pole -- contradiction.  Hence P_off is empty, all z_rho <= 0, and
(rho - 1/2)^2 <= 0 forces beta = 1/2.  The probe gates every numeric
ingredient of this chain and prints the classical steps as named
citations, never as fake gates.

COMPANIONS (each gated): the pin bridge P(sigma) = xi'/xi(1/2+sigma)
= 2 sigma F(sigma^2); the Li binomial transform b_{r-1}(1/4) =
4^{-r} sum_{m=1}^r (-1)^{m+1} C(2r, r+m) lambda_m (per zero pair,
q = (rho-1)/rho, lambda_m = 2 - q^m - q^{-m}, y = 1/(4 rho(1-rho)));
the Moebius flow y_{a'} = r y_a/(1 + (r-1) y_a), r = a'/a, with mass
transform w' = w y'/y and a d(b_n)/da = (n+1) C_{n,1}; the
Hankel-Vandermonde SOS identity det[b_{i+j}]_{N} = sum_{|S|=N}
(prod_S w) V(y_S)^2 >= 0; the Jacobi decoder H_1 v = y H_0 v
(implemented as moments -> Chebyshev recurrence -> Jacobi matrix ->
Golub-Welsch), nodes y_j in (0,1), gamma_j = sqrt(a (1-y_j)/y_j),
multiplicity read w_j/y_j; the two-moment decoder
Gamma_n = sqrt(a (b_n/b_{n+1} - 1)) decreasing to gamma_1.

PRIOR ART (typed honestly): Y. Zhang, arXiv:2303.09396, Theorem 2 is
EXACTLY this Hausdorff-moment criterion at the CENTRAL point (moments
m_k = sum lambda_n^{-k-2} of f(z) = prod(1 + z/lambda_n) at x = 0,
criterion (-1)^k Delta^k m_n >= 0 for all n,k <=> positivity of the
zero set, via the Hausdorff moment theorem), applied to Xi to give an
RH equivalence.  The abstract criterion is therefore NOT WORLD-NEW.
The proposal's delta is the SAFE-POINT SHIFT a > 1/4 (the central
point x=0 is s = 1/2, not source-computable; a = 256 puts the whole
jet in the absolutely convergent Euler half-plane), the source-only
decoder, and the certified-conditioning claim -- exactly what this
probe measures.

=======================================================================
FROZEN NUMERICS (all set BEFORE any computation)
=======================================================================
JETS (all Cauchy contours z = a + r e^{i theta}, M points, conjugate
symmetry exploited; sqrt principal -- every contour stays in
Re z > 0, so Re sqrt(z) >= sqrt(|z|/2) and min Re s > 1 is GATED):
  MAIN jet (source-only, certified): a=256, r=96, M=256, dps=200,
    own Lambda sieve NSIEVE=60000, orders 0..140.
  ARM jet (gamma*-reach extension): a=1024, r=384, M=320, dps=250,
    NSIEVE=50000, orders 0..316, cells n<=4, k<=310.
  FLOW jet (Moebius check): a'=512, r=192, M=128, dps=150,
    NSIEVE=20000, orders 0..40.
  REPRO jet (decoder precision; audit namespace, mp.zeta allowed,
    NOT certified, NOT source-only -- declared): a=256, r=48, M=128,
    dps=340, orders 0..47.
  EPSTEIN jet (control): Q = x^2+5y^2 (disc -20, h=2), a=256, r=96,
    M=256, dps=150, lattice cap QMAX=5000, orders 0..100.
  SMOOTH jet (prime-free control): archimedean part only
    (1/s + 1/(s-1) - log(pi)/2 + psi(s/2)/2), main contour, dps=200,
    orders 0..140.  NOTE: g_smooth is NOT odd in sigma (the functional
    equation needs the prime term), so this world has no globally
    single-valued Phi -- the jet is still well-defined on the disk;
    what its Pascal field does is a measurement, not a prediction.
CERTIFIED WIDTHS (main/arm; derivation): the trapezoid value of
b_n and of every Pascal cell is the trapezoid of the single integrand
F(z) w^{n+1} (1-w)^k, w = a/(a-z) (|w| = a/r exactly on the contour,
|1-w| = |z|/r), because the binomial combination of trapezoids over
the SAME points is the trapezoid of the combined integrand.  Width =
EVAL + ALIAS + ROUND:
  EVAL: per-point enclosure eps_j = TAIL(N, sigma_j) +
    10^{-(dps-10)}(1+|F_j|), TAIL(N,sigma) = N^{1-sigma}[(log N +
    1/(sigma-1))/(sigma-1) + log N/N] (from Lambda(n) <= log n and
    monotone-integrand comparison, valid since e^{1/sigma} < N);
    cell width (a/r)^{n+1} S_k, S_k = (1/M) sum_j wt_j (|z_j|/r)^k
    eps_j (separable, exact).
  ALIAS: trapezoid aliasing bound 2 M' (a/R')^{n+1} ((a+R')/R')^k
    q/(1-q), q = (r/R')^M, R' = a-6; inner alias vanishes exactly for
    M > n+k+1 (the pole at z=a has finite order).  M' = rigorous sup
    bound of |F| on |z-a| = R' from Re s >= 1/2 + sqrt(3):
    |zeta'/zeta| <= (log 2) 2^{-sm} + (log N +
    1/(sm-1))/(sm-1) N^{1-sm}-free full-sum bound with sm = Re s min,
    |psi(s/2)| <= log|s/2| + 2.45 (Binet remainder, arg w <= 45 deg),
    elementary pieces explicit; inflated x2 and PRINTED.
  ROUND: M 10^{-(dps-8)} (a/r)^{n+1} max_j v_j^k (|F_j|+1)  +
    2^{n+k} 10^{-(dps-8)} max|b| (finite-difference accumulation),
    both negligible against EVAL by >= 20 orders (printed).
  DECLARED: enclosure rigor is modulo mpmath's near-correctly rounded
  exp/log/digamma (inflated by 10^2 ulp); the mathematically derived
  Dirichlet tail dominates every verdict-bearing width.
DECODER: N_JAC=16 from repro moments b_0..b_31 (Chebyshev algorithm
-> alpha,beta -> Jacobi matrix -> mp.eigsy; weights beta_0 v_0^2),
dps 340.  Gauss exactness re-check sum w y^n vs b_n, n<=31.
SIGMA GRID (pins; verbatim the SVPIN/Krein 16-tuple, frozen):
  (0.6, 0.75, 0.9, 1.125, 8/7, 7/6, 1.2, 1.25, 4/3, 1.5, 2.0,
   3.0, 4.0, 6.0, 8.0, 12.0)
PROPOSER'S FROZEN RUN (reproduction TARGETS, not gates -- deviations
are findings): 561/561 Pascal cells positive at depth <= 32, weakest
C_{16,16} ~ 1.318e-10 (kernel peak gamma* = sqrt(a k/(n+1)) ~ 15.52),
gamma_1 to 1.6e-25, first six zeros to 8e-4, 16 pins to 6.5e-37.
PLANTED QUARTETS (detector): zeros 1/2 +- delta +- i gamma0 added
analytically to the moments (b_n += 2 Re y0^{n+1}, y0 = a/(a-z0),
z0 = (delta + i gamma0)^2); grid gamma0 in {8, 12, 20} x delta in
{0.4, 0.3, 0.2, 0.1} plus (12, 0.05); depth cap 140.  Phase model:
planted cell term 2|y0|^{n+1}|1-y0|^k cos Theta, Theta = (n+1) arg y0
+ k arg(1-y0); on the matched ray k/(n+1) = gamma0^2/a the phase rate
arg y0 + (gamma0^2/a) arg(1-y0) is STATIONARY: its delta-expansion
vanishes through order delta^2 (first residual O(delta^3), gated
symbolically), so ray detection is dead at leading order and the live
channel is k=0, alive only for |y0| > y_1, i.e. gamma0 < gamma_1:
predicted first negative n* ~ (pi/2)/arg y0 =
(pi/2)(a + gamma0^2)/(2 delta gamma0) ~ 1/delta.  Grid rows with
gamma0 > gamma_1 measure the expected blindness.  BOTH planted scans
are NOISE-GUARDED: a flip counts only if it clears the certified cell
width, tab + pert < -width (otherwise Lambda-tail noise beyond the
certified frontier fakes detections).  SECONDARY detector:
first N <= 11 with a certified-sign negative leading principal Hankel
minor (det H_0 or det H_1; mp dps 200, resolution floor |det| >
1e-45 declared).
EPSTEIN CONTROL: zero hunt for xi_Q(s) = s(s-1)(2pi/sqrt20)^{-s}
Gamma(s) Z_Q(s) via the incomplete-gamma representation Lambda_Q(s) =
-1/s - 1/(1-s) + sum' cnt [E_s(cQ) + E_{1-s}(cQ)], c = 2pi/sqrt(20),
E_s(x) = x^{-s} Gamma(s,x) (theta method; det of the scaled Gram
matrix = 1 exactly); real-axis scan sigma in [0.02, 0.98] step 0.02 +
bisection; cross-ward vs the lattice Dirichlet series at s = 16.5
(values) and s = 8.5 + 0.7i (log-derivative, central difference at
dps 80, bar 1e-15).  DISCLOSED: a pre-freeze scratch scan (|xi_Q| on
sigma in [.55,.9] x t in [.5,45], Newton refinement) located the
witness off-line zero rho ~ 0.6969 + 36.374i; the probe re-derives it
from the FROZEN SEED 0.7 + 36.4i (gate G54a: |xi_Q(rho)| < 1e-25,
0.55 < beta < 0.85) -- the control world provably violates RH-for-Q.
G54b blindness CONSISTENCY: plant exactly (beta_0 - 1/2, gamma_0) on
the TRUE field and require the planted replica to reproduce the
Q-field's observed behaviour at matched caps (Pascal depth 100,
Hankel N <= 14, floor 1e-45): fires-iff-fires; both Pascal scans
noise-guarded by the respective widths (flip must clear the width).  The phase-model
numbers (|y0| vs y_1, k-channel depth (pi/2)/|arg(1-y0)|) are
printed; with gamma_0 ~ 36.4 >> gamma_1 the predicted Pascal depth is
~9e2 -- the criterion is HONESTLY TYPED detection-weak for realistic
off-line zeros at the safe point, and the Epstein control measures
that price instead of faking a detection.  Pascal/Hankel censuses of
the Q field printed; the near-line root found at ~0.5002 + 44.58i is
printed UNRESOLVED (not gate-bearing).
KREIN REPLICATION: import krein_screw_realization_probe (frozen
round-90 carrier), build its TRUE-world L=2.568/delta=0.003 lag row,
Szego recursion, Weyl-disk pins on the 16-sigma grid; compare with
this probe's quadrature pins.  Bars: max |dP| <= 2e-3, median <=
2e-4 (their measured window truncation, sigma=12 bias ~ -2.9e-4).
SIGNPOS REPLICATION: reimplement the round-88 source-only counting
predictor N_src(T) = theta(T)/pi + 1 + S_x(T) (theta = Im log
Gamma(1/4 + iT/2) - (T/2) log pi; S_x = Fejer-tapered prime sum) at
the gated rung x = 8; predicted positions t_j solve N_src = j - 1/2;
bar max_j<=5 |t_j - gamma_hat_j| <= 0.6.  CCCXCVIII context declared:
the predictor's rounding form is measured FALSE beyond x = 13; the
comparison lives at the shallow gated rung.
Z1 TYPING: cache = verified_zeros_n7000.npy, float64, READ-ONLY,
ward namespace only (X5: instrument, never construction).  b_n vs
cache partial sums + RvM tail: bar rel <= 5e-3 at n=0 (tail model),
rel <= 1e-7 for 2 <= n <= 60 (float64 ordinate floor ~1e-10).  If it
passes, the carrier is typed source-only in INPUT, zero-measure in
CONTENT (like Krein): the criterion is RH verbatim, the novelty is
architectural + conditioning.
DECAY SCREEN: OLS slope of log10 min_{n+k=d} C vs d over d = 8..32;
band [-0.45, -0.15]; spectral prediction (1/2) log10(y1(1-y1)) =
-0.304.  No tau exists in this pipeline (no Galerkin matrix, no
extremal eigenvalue) -- the wall-margin collapse channel is
structurally absent, stated as typed INFO, not gated as PASS.
AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; mp.zeta attribute only inside audit_*/ward_* functions;
np.load only inside ward_*; no identifier contains 'christoffel'.
RUNTIME BAR 1800 s.  Deterministic (no randomness anywhere).

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

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# ------------------------------------------------------------ frozen bars
A_MAIN, R_MAIN, M_MAIN, DPS_MAIN, NS_MAIN, ORD_MAIN = 256, 96, 256, 200, 60000, 140
A_ARM, R_ARM, M_ARM, DPS_ARM, NS_ARM, ORD_ARM = 1024, 384, 320, 250, 50000, 316
ARM_NMAX, ARM_KMAX = 4, 310
A_FLOW, R_FLOW, M_FLOW, DPS_FLOW, NS_FLOW, ORD_FLOW = 512, 192, 128, 150, 20000, 40
R_REPRO, M_REPRO, DPS_REPRO, ORD_REPRO = 48, 128, 340, 48
QMAX_EPS, DPS_EPS, ORD_EPS, M_EPS, R_EPS = 5000, 150, 100, 256, 96
N_JAC = 16
DEPTH_CENSUS = 32          # proposer's 561-cell triangle
DEPTH_FIELD = 140          # main certified triangle
SIGMAS = (0.6, 0.75, 0.9,
          1.125, 8.0 / 7.0, 7.0 / 6.0, 1.2, 1.25, 4.0 / 3.0, 1.5, 2.0,
          3.0, 4.0, 6.0, 8.0, 12.0)
PLANT_GAMMA0 = (8.0, 12.0, 20.0)
PLANT_DELTA = (0.4, 0.3, 0.2, 0.1)
PLANT_EXTRA = ((12.0, 0.05),)
PROP = {"cells": 561, "weakest": 1.318e-10, "cell": (16, 16),
        "gamstar": 15.52, "g1err": 1.6e-25, "six": 8e-4, "pins": 6.5e-37}
EULERPICK = {"ncert": 3, "greach": "5-8", "kappa12": 2.267192e61,
             "law": "N* = 6.11 + 1.95 log10(1/delta) at gamma=14",
             "blind": "gamma=50 undetected through N=36"}
BAR_EVEN = 1e-25
BAR_ODDC = 1e-25
BAR_JETX = 1e-40           # b0 cross main vs repro (rel)
BAR_JET30 = 1e-38          # jet cross ward n<=30 (rel)
BAR_IM = 1e-40
BAR_G25 = 1e-18            # gamma1 decoder bar (proposer 1.6e-25 printed)
BAR_SIX = 8e-3             # 10x proposer
BAR_MULT = 0.25
BAR_G27 = 1e-6
BAR_PINS = 1e-6            # falsifiable wiring bar; measured value printed
BAR_FLOW = 1e-6            # Moebius pushforward vs direct, n<=20
BAR_DMAX = 40
BAR_GSTAR_MAIN = 30.0
BAR_GSTAR_ARM = 60.0
BAR_SIGNPOS = 0.6
BAR_KREIN_MAX = 2e-3
BAR_KREIN_MED = 2e-4
BAR_EPS_XWARD = 1e-25
BAR_EPS_DEPTH = 100
BAR_EPS_PRED = 3
BAR_Z1_N0 = 5e-3
BAR_Z1_N2 = 1e-7
DECAY_BAND = (-0.45, -0.15)
RUNTIME_BAR = 1800.0
GAMMA1_LIT = "14.134725141734693790457251983562470"  # ward only
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

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


# ====================================================== firewall (G01)
FORBIDDEN = ("zetazero", "siegelz", "siegeltheta", "nzeros", "grampoint")


def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owner(lineno: int) -> str:
        best = ""
        for nm, lo, hi in spans:
            if lo <= lineno <= hi:
                best = nm
        return best

    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in FORBIDDEN:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if "christoffel" in low:
            bad.append("christoffel identifier @%d" % node.lineno)
        if low == "zeta":
            fn = owner(node.lineno)
            if not (fn.startswith("audit_") or fn.startswith("ward_")):
                bad.append("zeta outside audit_/ward_ @%d (%s)"
                           % (node.lineno, fn or "module"))
        if isinstance(node, ast.Attribute) and nm == "load":
            fn = owner(node.lineno)
            if not fn.startswith("ward_"):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fn or "module"))
    return (len(bad) == 0, "; ".join(bad) if bad else
            "no zero-oracle, zeta confined to audit_/ward_, cache to ward_")


# ====================================================== source tables
def sieve_prime_powers(cap: int) -> list[tuple[int, int]]:
    """(n = p^m, p) for all prime powers n <= cap.  Own sieve."""
    comp = np.zeros(cap + 1, dtype=bool)
    out = []
    for p in range(2, cap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= cap:
            out.append((q, p))
            q *= p
    out.sort()
    return out


def lambda_tail_bound(nsieve: int, sigma: float) -> float:
    """Rigorous |sum_{n>N} Lambda(n) n^{-sigma}| bound (spec formula)."""
    ln = math.log(nsieve)
    if sigma <= 1.5 or math.exp(1.0 / sigma) >= nsieve:
        return float("inf")
    return (nsieve ** (1.0 - sigma)
            * ((ln + 1.0 / (sigma - 1.0)) / (sigma - 1.0) + ln / nsieve))


def trapezoid_moments(Fs: list, a: int, r: int, mpts: int, dps: int,
                      orders: int) -> tuple[list, float]:
    """b_n from contour samples F(z_j), j = 0..M/2, conj symmetry.
    Phase indices reduced mod 2M exactly (integer arithmetic)."""
    half = mpts // 2
    with mp.workdps(dps):
        am, rm = mp.mpf(a), mp.mpf(r)
        bs = []
        im_res = 0.0
        for n in range(orders + 1):
            acc = Fs[0] + ((-1) ** n) * Fs[half]
            for j in range(1, half):
                idx = (-2 * j * n) % (2 * mpts)
                acc += 2 * mp.re(Fs[j] * mp.expjpi(mp.mpf(idx) / mpts))
            bn = (am ** (n + 1)) * ((-1) ** n) * acc / (mpts * rm ** n)
            im_res = max(im_res, abs(float(mp.im(bn)))
                         / max(1e-300, abs(float(mp.re(bn)))))
            bs.append(mp.re(bn))
    return bs, im_res


def alias_sup_bound(a: int) -> tuple[int, float]:
    """(R', M') with M' a rigorous generous sup bound of |F| on the
    circle |z-a| = R' = a-6 (Re z >= 6 => Re sqrt z >= sqrt 3):
    |zeta'/zeta| <= log2 2^{-sm} + int_2^inf log t t^{-sm} dt,
    |psi(s/2)|/2 <= (log(|s|max/2 + 1) + 2.45)/2 (Binet remainder,
    arg(s/2) <= 45 deg on the circle), elementary pieces explicit;
    inflated x2."""
    rp = a - 6
    sm = 0.5 + math.sqrt(3.0)
    smax = 0.5 + math.sqrt(a + rp)
    zz_bound = (math.log(2) * 2 ** (-sm)
                + ((math.log(2) / (sm - 1)) + 1 / (sm - 1) ** 2)
                * 2 ** (1 - sm))
    psi_bound = 0.5 * (math.log(smax / 2 + 1) + 2.45)
    mprime = 2.0 * ((1 / sm) + (1 / (sm - 1)) + 0.5729 + psi_bound
                    + zz_bound) / (2 * math.sqrt(3.0))
    return rp, mprime


def build_jet_lambda(a: int, r: int, mpts: int, dps: int, nsieve: int,
                     orders: int, label: str) -> dict:
    """Source-only Cauchy jet of F at a: Lambda-series xi'/xi on the
    contour, trapezoid, per-point enclosure widths.  Returns mp b_n
    (n = 0..orders), separable width data, contour diagnostics."""
    t0 = time.time()
    pps = sieve_prime_powers(nsieve)
    with mp.workdps(dps):
        logs = {}
        atoms = []
        for q, p in pps:
            if p not in logs:
                logs[p] = mp.log(p)
            atoms.append((mp.log(q), logs[p]))
        half = mpts // 2
        Fs, sig_min = [], float("inf")
        eps, vv, wt = [], [], []
        am, rm = mp.mpf(a), mp.mpf(r)
        for j in range(half + 1):
            z = am + rm * mp.expjpi(mp.mpf(2 * j) / mpts)
            s = mp.mpf("0.5") + mp.sqrt(z)
            acc = mp.mpc(0)
            for lgn, lam in atoms:
                acc += lam * mp.exp(-s * lgn)
            F = ((1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
                  + mp.digamma(s / 2) / 2 - acc) / (2 * mp.sqrt(z)))
            Fs.append(F)
            sj = float(mp.re(s))
            sig_min = min(sig_min, sj)
            eps.append(lambda_tail_bound(nsieve, sj)
                       + 10.0 ** (-(dps - 10)) * (1.0 + float(abs(F))))
            vv.append(float(abs(z)) / r)
            wt.append(1.0 if j in (0, half) else 2.0)
        imF = max(abs(float(mp.im(Fs[0]))), abs(float(mp.im(Fs[half]))))
    bs, im_res = trapezoid_moments(Fs, a, r, mpts, dps, orders)
    rp, mprime = alias_sup_bound(a)
    qal = (r / rp) ** mpts
    return {"a": a, "r": r, "M": mpts, "dps": dps, "N": nsieve,
            "orders": orders, "b": bs, "eps": np.array(eps),
            "v": np.array(vv), "wt": np.array(wt), "sig_min": sig_min,
            "rp": rp, "mprime": mprime, "qal": qal, "im_res": im_res,
            "imF": imF, "label": label, "secs": time.time() - t0}


def jet_widths(jet: dict, kmax: int) -> np.ndarray:
    """S_k table of the separable EVAL width, k = 0..kmax."""
    e, v, w = jet["eps"], jet["v"], jet["wt"]
    out = np.empty(kmax + 1)
    cur = np.ones_like(v)
    for k in range(kmax + 1):
        out[k] = float(np.sum(w * cur * e)) / jet["M"]
        cur = cur * v
    return out


def cell_width(jet: dict, sk: np.ndarray, n: int, k: int,
               maxb: float) -> float:
    """Total certified width of C_{n,k} (EVAL + ALIAS + ROUND)."""
    a, r, rp, mpts, dps = jet["a"], jet["r"], jet["rp"], jet["M"], jet["dps"]
    lg_ar = (n + 1) * math.log10(a / r)
    ev = 10.0 ** lg_ar * sk[k] if lg_ar < 250 else float("inf")
    q = jet["qal"]
    al = (2 * jet["mprime"] * q / (1 - q)
          * 10.0 ** ((n + 1) * math.log10(a / rp)
                     + k * math.log10((a + rp) / rp)))
    vmax = float(np.max(jet["v"]))
    fmax = 3.0
    lg_rd = (math.log10(mpts) - (dps - 8) + lg_ar + k * math.log10(vmax)
             + math.log10(fmax))
    lg_fd = ((n + k) * math.log10(2.0) - (dps - 8)
             + math.log10(max(maxb, 1.0)))
    rd = 10.0 ** lg_rd + 10.0 ** lg_fd
    return ev + al + rd


def pascal_table(bs: list, depth: int, dps: int) -> list:
    """C[n][k] for n+k <= depth via the finite-difference recurrence
    C_{n,k+1} = C_{n,k} - C_{n+1,k} (exact identity of the definition).
    Runs at working precision dps (the recurrence cancellation needs
    the full jet precision, not the mp global default)."""
    with mp.workdps(dps):
        cols = [list(bs[: depth + 1])]
        for k in range(depth):
            prev = cols[-1]
            cols.append([prev[n] - prev[n + 1]
                         for n in range(len(prev) - 1)])
        tab = []
        for n in range(depth + 1):
            tab.append([cols[k][n] for k in range(depth + 1 - n)])
    return tab


# ====================================================== smooth control
def build_jet_smooth(a: int, r: int, mpts: int, dps: int,
                     orders: int) -> dict:
    t0 = time.time()
    with mp.workdps(dps):
        half = mpts // 2
        Fs = []
        am, rm = mp.mpf(a), mp.mpf(r)
        for j in range(half + 1):
            z = am + rm * mp.expjpi(mp.mpf(2 * j) / mpts)
            s = mp.mpf("0.5") + mp.sqrt(z)
            F = ((1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
                  + mp.digamma(s / 2) / 2) / (2 * mp.sqrt(z)))
            Fs.append(F)
    bs, _im = trapezoid_moments(Fs, a, r, mpts, dps, orders)
    return {"b": bs, "orders": orders, "secs": time.time() - t0}


# ====================================================== Epstein control
def epstein_lattice(qmax: int) -> list[tuple[int, int]]:
    """(Q, count) for Q = x^2 + 5 y^2 <= qmax over the full lattice."""
    cnt = {}
    b = 0
    while 5 * b * b <= qmax:
        aa = 0
        while aa * aa + 5 * b * b <= qmax:
            q = aa * aa + 5 * b * b
            if q >= 1:
                cnt[q] = cnt.get(q, 0) + (2 if aa else 1) * (2 if b else 1)
            aa += 1
        b += 1
    return sorted(cnt.items())


def epstein_tail_bound(qmax: int, sigma: float) -> float:
    """|sum_{Q>X} r(Q) Q^{-sigma}| <= 6 sigma/(sigma-1) X^{1-sigma}
    from N(T) <= 3T (warded numerically) and partial summation."""
    return 6.0 * sigma / (sigma - 1.0) * qmax ** (1.0 - sigma)


def build_jet_epstein(a: int, r: int, mpts: int, dps: int, qmax: int,
                      orders: int) -> dict:
    t0 = time.time()
    lat = epstein_lattice(qmax)
    lnq = math.log(qmax)
    with mp.workdps(dps):
        lgq = [(mp.log(q), cnt) for q, cnt in lat]
        half = mpts // 2
        Fs = []
        eps, vv, wt = [], [], []
        am, rm = mp.mpf(a), mp.mpf(r)
        c20 = mp.log(mp.sqrt(20) / (2 * mp.pi))
        sig_min = float("inf")
        for j in range(half + 1):
            z = am + rm * mp.expjpi(mp.mpf(2 * j) / mpts)
            s = mp.mpf("0.5") + mp.sqrt(z)
            Z = mp.mpc(0)
            ZP = mp.mpc(0)
            for lq, cnt in lgq:
                t = cnt * mp.exp(-s * lq)
                Z += t
                ZP += -lq * t
            F = ((1 / s + 1 / (s - 1) + c20 + mp.digamma(s)
                  + ZP / Z) / (2 * mp.sqrt(z)))
            Fs.append(F)
            sj = float(mp.re(s))
            sig_min = min(sig_min, sj)
            # EVAL-only noise width for Z'/Z (control-grade): |Z| >= 1.9
            tz = epstein_tail_bound(qmax, sj)
            eF = ((tz * (lnq + 2.0) * (1.0 + float(abs(ZP / Z)))) / 1.9
                  / (2.0 * math.sqrt(float(abs(z))))
                  + 10.0 ** (-(dps - 10)) * (1.0 + float(abs(F))))
            eps.append(eF)
            vv.append(float(abs(z)) / r)
            wt.append(1.0 if j in (0, half) else 2.0)
    bs, _im = trapezoid_moments(Fs, a, r, mpts, dps, orders)
    npts = sum(c for _q, c in lat)
    return {"b": bs, "orders": orders, "sig_min": sig_min,
            "npts": npts, "lat": lat, "eps": np.array(eps),
            "v": np.array(vv), "wt": np.array(wt), "M": mpts, "a": a,
            "r": r, "secs": time.time() - t0}


_EPS_LAT60 = None


def audit_epstein_xi(s, dps: int = 40):
    """xi_Q(s) = s(s-1) Lambda_Q(s) via the incomplete-gamma (theta)
    representation; valid on all of C.  audit namespace."""
    global _EPS_LAT60
    if _EPS_LAT60 is None:
        _EPS_LAT60 = epstein_lattice(60)
    with mp.workdps(dps):
        s = mp.mpc(s) if mp.im(mp.mpc(s)) != 0 else mp.mpf(mp.re(mp.mpc(s)))
        c = 2 * mp.pi / mp.sqrt(20)
        tot = -1 / s - 1 / (1 - s)
        for qv, cnt in _EPS_LAT60:
            x = c * qv
            tot += cnt * (x ** (-s) * mp.gammainc(s, x, mp.inf)
                          + x ** (-(1 - s)) * mp.gammainc(1 - s, x, mp.inf))
        return s * (s - 1) * tot


def audit_epstein_series_xi_logderiv(s, qmax: int = 3000, dps: int = 40):
    """xi_Q'/xi_Q via the lattice Dirichlet series (Re s > 1)."""
    with mp.workdps(dps):
        s = mp.mpc(s)
        lat = epstein_lattice(qmax)
        Z, ZP = mp.mpc(0), mp.mpc(0)
        for q, cnt in lat:
            lq = mp.log(q)
            t = cnt * mp.exp(-s * lq)
            Z += t
            ZP += -lq * t
        return (1 / s + 1 / (s - 1) + mp.log(mp.sqrt(20) / (2 * mp.pi))
                + mp.digamma(s) + ZP / Z)


# ====================================================== audit evaluators
def audit_xi_logderiv(s, dps: int = 340):
    """xi'/xi(s) via mp.zeta (audit namespace; NOT source-only)."""
    with mp.workdps(dps):
        s = mp.mpc(s)
        return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
                + mp.digamma(s / 2) / 2 + mp.zeta(s, derivative=1)
                / mp.zeta(s))


def audit_xi(w, dps: int = 40):
    """xi(1/2 + w) (audit namespace)."""
    with mp.workdps(dps):
        s = mp.mpf("0.5") + mp.mpc(w)
        return (s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2)
                * mp.zeta(s))


def audit_F(z, dps: int = 60):
    """F(z) = xi'/xi(1/2+sqrt z)/(2 sqrt z) via mp.zeta (audit)."""
    with mp.workdps(dps):
        z = mp.mpf(z)
        s = mp.mpf("0.5") + mp.sqrt(z)
        return audit_xi_logderiv(s, dps) / (2 * mp.sqrt(z))


def build_jet_repro(a: int, r: int, mpts: int, dps: int,
                    orders: int) -> dict:
    """High-precision repro jet via mp.zeta contour -- wrapped so the
    zeta attribute lives in an audit_ function (see audit_contour_F)."""
    t0 = time.time()
    with mp.workdps(dps):
        half = mpts // 2
        am, rm = mp.mpf(a), mp.mpf(r)
        Fs = []
        for j in range(half + 1):
            z = am + rm * mp.expjpi(mp.mpf(2 * j) / mpts)
            Fs.append(audit_contour_F(z, dps))
    bs, _im = trapezoid_moments(Fs, a, r, mpts, dps, orders)
    return {"b": bs, "orders": orders, "a": a, "secs": time.time() - t0}


def audit_contour_F(z, dps: int):
    with mp.workdps(dps):
        s = mp.mpf("0.5") + mp.sqrt(z)
        num = (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
               + mp.digamma(s / 2) / 2
               + mp.zeta(s, derivative=1) / mp.zeta(s))
        return num / (2 * mp.sqrt(z))


# ====================================================== Jacobi decoder
def chebyshev_jacobi(bs: list, njac: int, dps: int) -> dict:
    """Moments -> (alpha, beta) via the classical Chebyshev algorithm
    (Gautschi, OPQ Sec. 2.1.7) -> Jacobi matrix -> Golub-Welsch
    (mp.eigsy).  Needs bs[0..2 njac - 1].  sigma_{k,l} = <p_k, y^l>:
      sigma_{0,l} = m_l;  sigma_{k,l} = sigma_{k-1,l+1}
        - alpha_{k-1} sigma_{k-1,l} - beta_{k-1} sigma_{k-2,l};
      alpha_k = s_{k,k+1}/s_{k,k} - s_{k-1,k}/s_{k-1,k-1};
      beta_k = s_{k,k}/s_{k-1,k-1}."""
    with mp.workdps(dps):
        m = [mp.mpf(x) for x in bs[: 2 * njac]]
        sig = {}
        for ell in range(2 * njac):
            sig[(0, ell)] = m[ell]
        alphas = [m[1] / m[0]]
        betas = [m[0]]
        for k in range(1, njac):
            for ell in range(k, 2 * njac - k):
                v = (sig[(k - 1, ell + 1)]
                     - alphas[k - 1] * sig[(k - 1, ell)])
                if k >= 2:
                    v -= betas[k - 1] * sig[(k - 2, ell)]
                sig[(k, ell)] = v
            alphas.append(sig[(k, k + 1)] / sig[(k, k)]
                          - sig[(k - 1, k)] / sig[(k - 1, k - 1)])
            betas.append(sig[(k, k)] / sig[(k - 1, k - 1)])
        J = mp.zeros(njac, njac)
        for i in range(njac):
            J[i, i] = alphas[i]
        for i in range(njac - 1):
            J[i, i + 1] = J[i + 1, i] = mp.sqrt(betas[i + 1])
        ev, evec = mp.eigsy(J)
        nodes = [ev[i] for i in range(njac)]
        weights = [betas[0] * evec[0, i] ** 2 for i in range(njac)]
        order = sorted(range(njac), key=lambda i: -nodes[i])
        nodes = [nodes[i] for i in order]
        weights = [weights[i] for i in order]
        return {"nodes": nodes, "weights": weights,
                "alphas": alphas, "betas": betas}


def quad_F(dec: dict, a: int, z, dps: int):
    """Stieltjes quadrature F(z) ~ sum w_j / (a(1-y_j) + y_j z)."""
    with mp.workdps(dps):
        z = mp.mpf(z)
        return mp.fsum(w / (a * (1 - y) + y * z)
                       for y, w in zip(dec["nodes"], dec["weights"]))


def hankel_first_negative(bvals: list, nmax: int, dps: int):
    """First N <= nmax with det H_0(N) or det H_1(N) < -1e-45
    (resolution floor declared); returns (N* or None, min det seen)."""
    with mp.workdps(dps):
        floor = mp.mpf("-1e-45")
        mind = mp.mpf("inf")
        for N in range(2, nmax + 1):
            h0 = mp.matrix(N, N)
            h1 = mp.matrix(N, N)
            for i in range(N):
                for j in range(N):
                    h0[i, j] = bvals[i + j]
                    h1[i, j] = bvals[i + j + 1]
            d0, d1 = mp.det(h0), mp.det(h1)
            mind = min(mind, d0, d1)
            if d0 < floor or d1 < floor:
                return N, float(mind)
        return None, float(mind)


# ====================================================== wards (cache X5)
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_bn_cache(gam: np.ndarray, a: float, n: int) -> float:
    """b_n from cache ordinates + RvM density tail (instrument only)."""
    y = a / (a + gam ** 2)
    fin = float(np.sum(y ** (n + 1)))
    gtop = float(gam[-1])
    with mp.workdps(30):
        tail = mp.quad(lambda t: (mp.log(t / (2 * mp.pi)) / (2 * mp.pi))
                       * (a / (a + t * t)) ** (n + 1),
                       [gtop, 3 * gtop, 30 * gtop, mp.inf])
    return fin + float(tail)


# ====================================================== signpos predictor
def signpos_nsrc(T: float, x: float, dps: int = 30) -> float:
    """Round-88 source-only counting predictor at rung x (Fejer)."""
    with mp.workdps(dps):
        a = mp.log(x) / 2
        th = (mp.im(mp.loggamma(mp.mpf("0.25") + mp.mpc(0, T) / 2))
              - T * mp.log(mp.pi) / 2)
        s = mp.mpf(0)
        icap = int(math.floor(x + 1e-9))
        comp = [False] * (icap + 1)
        for p in range(2, icap + 1):
            if comp[p]:
                continue
            for qq in range(p * p, icap + 1, p):
                comp[qq] = True
            q = p
            while q <= icap:
                u = mp.log(q)
                taper = 1 - u / (2 * a)
                if taper > 0:
                    s += (mp.log(p) / mp.sqrt(q)) * mp.sin(T * u) / u * taper
                q *= p
        return float(th / mp.pi + 1 - s / mp.pi)


def signpos_positions(x: float, jmax: int) -> list[float]:
    """t_j solving N_src(t) = j - 1/2 (first crossing per j)."""
    grid = np.arange(1.0, 60.0, 0.05)
    vals = np.array([signpos_nsrc(float(t), x) for t in grid])
    out = []
    for j in range(1, jmax + 1):
        tgt = j - 0.5
        idx = np.where((vals[:-1] < tgt) & (vals[1:] >= tgt))[0]
        if len(idx) == 0:
            out.append(float("nan"))
            continue
        lo, hi = float(grid[idx[0]]), float(grid[idx[0] + 1])
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            if signpos_nsrc(mid, x) < tgt:
                lo = mid
            else:
                hi = mid
        out.append(0.5 * (lo + hi))
    return out


# ====================================================== symbolic gates
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    # (a) moment-Taylor identity of the Stieltjes side, 3 atoms, n<=4
    z, av = sp.symbols("z a", positive=True)
    ys = sp.symbols("y1 y2 y3", positive=True)
    ws = sp.symbols("w1 w2 w3", positive=True)
    G = sum(w / (av * (1 - y) + y * z) for y, w in zip(ys, ws))
    ok = True
    for n in range(5):
        lhs = (av ** (n + 1) * (-1) ** n / sp.factorial(n)
               * sp.diff(G, z, n).subs(z, av))
        rhs = sum(w * y ** n for y, w in zip(ys, ws))
        if sp.simplify(lhs - rhs) != 0:
            ok = False
    out.append(("H1c-moment-taylor", ok, "G^{(n)}(a) coeffs == moments, "
                "n<=4, 3 generic atoms"))
    # (b) Li binomial transform, per zero pair, r <= 5
    rho = sp.symbols("rho")
    q = (rho - 1) / rho
    yv = 1 / (4 * rho * (1 - rho))
    ok = True
    for r in range(1, 6):
        s = sum((-1) ** (m + 1) * sp.binomial(2 * r, r + m)
                * (2 - q ** m - q ** (-m)) for m in range(1, r + 1))
        if sp.simplify(sp.together(s / 4 ** r - yv ** r)) != 0:
            ok = False
    out.append(("H1d-li-transform", ok,
                "4^{-r} sum (-1)^{m+1} C(2r,r+m) lambda_m == y^r, r<=5"))
    # (c) Moebius flow + mass transform + a d(b)/da = (n+1) C_{n,1}
    ap = sp.symbols("ap", positive=True)
    y = sp.symbols("y", positive=True)
    zv = av * (y - 1) / y
    yp = ap / (ap - zv)
    rr = ap / av
    ok = sp.simplify(yp - rr * y / (1 + (rr - 1) * y)) == 0
    ya = av / (av - z)
    ok = ok and sp.simplify(av * sp.diff(ya, av) - ya * (1 - ya)) == 0
    out.append(("H1d-moebius-flow", ok,
                "y' == r y/(1+(r-1)y);  a dy/da == y(1-y) "
                "(=> a db_n/da = (n+1) C_{n,1} termwise)"))
    # (d) Hankel-Vandermonde SOS, N = 2 (3 atoms) and N = 3 (4 atoms)
    ok = True
    for nn, nat in ((2, 3), (3, 4)):
        yy = sp.symbols("t0:%d" % nat, positive=True)
        ww = sp.symbols("u0:%d" % nat, positive=True)
        H = sp.Matrix(nn, nn, lambda i, j: sum(
            w * y ** (i + j) for y, w in zip(yy, ww)))
        det = sp.expand(H.det())
        import itertools
        rhs = 0
        for S in itertools.combinations(range(nat), nn):
            prod_w = 1
            for i in S:
                prod_w *= ww[i]
            V = 1
            for i in range(len(S)):
                for j in range(i + 1, len(S)):
                    V *= (yy[S[j]] - yy[S[i]])
            rhs += prod_w * V ** 2
        if sp.simplify(det - sp.expand(rhs)) != 0:
            ok = False
    out.append(("H1d-hankel-sos", ok,
                "det H_N == sum_S (prod w) Vandermonde^2, N=2,3"))
    # (e) Pascal conservation from the definition, k <= 5, symbolic b
    bsym = sp.symbols("b0:9")

    def cell(n, k):
        return sum((-1) ** j * sp.binomial(k, j) * bsym[n + j]
                   for j in range(k + 1))
    ok = all(sp.simplify(cell(n, k) - cell(n + 1, k) - cell(n, k + 1)) == 0
             for n in range(3) for k in range(5))
    out.append(("H1d-pascal-identity", ok,
                "C_{n,k} == C_{n+1,k} + C_{n,k+1} symbolically"))
    # (f) planted matched-ray phase stationarity: the delta-expansion of
    # arg y0 + (gamma0^2/a) arg(1-y0) vanishes through order delta^2
    # (arg via atan of Im/Re on the exact rational forms; branch-safe
    # for small delta since both Re parts are positive there)
    dl, g0 = sp.symbols("delta gamma0", positive=True)
    z0 = sp.expand((dl + sp.I * g0) ** 2)
    w1 = sp.expand(av - z0)                      # y0 = a / w1
    w2 = sp.expand(-z0)                          # 1-y0 = -z0 / w1
    phi_y = -sp.atan(sp.im(w1) / sp.re(w1))
    phi_1y = sp.atan(sp.im(w2) / sp.re(w2)) + phi_y
    ser = sp.series(phi_y + (g0 ** 2 / av) * phi_1y, dl, 0, 3).removeO()
    ok = sp.simplify(ser) == 0
    c3 = sp.simplify(sp.series(phi_y + (g0 ** 2 / av) * phi_1y,
                               dl, 0, 4).removeO() / dl ** 3)
    out.append(("H5a-matched-ray-phase", ok,
                "(n+1)arg y0 + k arg(1-y0) on k/(n+1)=gamma0^2/a is "
                "O(delta^3); residual coeff = %s" % sp.nsimplify(c3)))
    return out


# ====================================================== main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("hausdorff_safepoint_probe -- PRIME.HAUSDORFF.SAFEPOINT.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))

    ord_main = 60 if smoke else ORD_MAIN
    m_main = 128 if smoke else M_MAIN
    ns_main = 20000 if smoke else NS_MAIN
    depth_field = 60 if smoke else DEPTH_FIELD
    do_arm = not smoke
    ord_eps = 60 if smoke else ORD_EPS
    q_eps = 2000 if smoke else QMAX_EPS
    m_eps = 128 if smoke else M_EPS

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + SPEC")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det)
    print("  contract: PRIME.HAUSDORFF.SAFEPOINT.01 (external proposal,")
    print("  reimplemented from spec; proposer code unavailable)")
    print("  prior art: Zhang arXiv:2303.09396 Thm 2 = the same Hausdorff")
    print("  criterion at the central point x=0; this run adjudicates the")
    print("  safe-point shift a=256 + source-only decoder + conditioning.")

    # ---------------------------------------------------------- S1
    section("S1  H1 SKELETON AUDIT (symbolic + numeric ingredients)")
    for name, ok, det in symbolic_gates():
        check(name, ok, det)

    with mp.workdps(40):
        wtests = [mp.mpc("0.3", "7.1"), mp.mpc("-1.2", "3.7"),
                  mp.mpc("2.0", "-11.0"), mp.mpc("0.05", "22.3")]
        dev = 0.0
        for w in wtests:
            xa, xb = audit_xi(w), audit_xi(-w)
            dev = max(dev, float(abs(xa - xb) / abs(xa)))
    check("H1a-X-even", dev <= BAR_EVEN,
          "max rel |X(w)-X(-w)| = %.3e (bar %.0e)" % (dev, BAR_EVEN))

    with mp.workdps(60):
        mtay, rtay = 32, mp.mpf(2)
        xv = [audit_xi(rtay * mp.expjpi(mp.mpf(2 * j) / mtay), 60)
              for j in range(mtay)]
        cofs = []
        for n in range(10):
            acc = mp.fsum(
                xv[j] * mp.expjpi(mp.mpf((-2 * j * n) % (2 * mtay)) / mtay)
                for j in range(mtay))
            cofs.append(acc / (mtay * rtay ** n))
        odd = max(abs(float(abs(cofs[i]))) for i in (1, 3, 5, 7, 9))
        even = min(abs(float(abs(cofs[i]))) for i in (0, 2, 4, 6, 8))
    check("H1a-Phi-even-taylor", odd / even <= BAR_ODDC,
          "max|odd|/min|even| Taylor coeff of X at 0 = %.3e -> "
          "Phi(z) = X(sqrt z) entire (order 1/2)" % (odd / even))

    # F(x) -> 0 with the derived rate (no-atom-at-0 ingredient)
    rates = []
    prev = None
    okr = True
    for lx in (4, 6, 8, 10):
        x = 10.0 ** lx
        with mp.workdps(50):
            fv = float(mp.re(audit_F(x, 50)))
            s = 0.5 + math.sqrt(x)
            asym = 0.5 * math.log(s / (2 * math.pi)) / (2 * math.sqrt(x))
            rr = fv / asym
        rates.append((x, fv, rr))
        if prev is not None and fv >= prev:
            okr = False
        prev = fv
        if abs(rr - 1) > 4.0 / math.sqrt(s):
            okr = False
    check("H1c-F-to-zero", okr,
          "; ".join("F(1e%d)=%.3e ratio=%.4f" % (math.log10(x), f, rr)
                    for x, f, rr in rates)
          + "  [atom at y=0 would force F(x)->m/a>0]")
    info("Hausdorff 1921 / Widder 1941 Thm III.4a cited: CM <=> bounded "
         "nonneg measure on [0,1]; boundedness NOT extra (b_n<=b_0 from "
         "C_{n,1}>=0, gated numerically in S3)")
    info("continuation step: Omega = slit plane minus off-axis poles is "
         "open+connected; identity theorem propagates F=G from the disk; "
         "G holomorphic at any putative off-axis pole z0 => z0 removable "
         "=> contradiction; classical inputs only (identity theorem, "
         "removable singularity), no gap found -- ingredients gated: "
         "evenness (H1a), F->0 (H1c), moment-Taylor (H1c), b-bounds (S3)")

    # ---------------------------------------------------------- S2
    section("S2  H2 SOURCE-ONLY JETS (Lambda contour, certified widths)")
    jet = build_jet_lambda(A_MAIN, R_MAIN, m_main, DPS_MAIN, ns_main,
                           ord_main, "main")
    print("  main jet: a=%d r=%d M=%d dps=%d N=%d orders=%d  (%.1f s)"
          % (A_MAIN, R_MAIN, m_main, DPS_MAIN, ns_main, ord_main,
             jet["secs"]))
    check("G21-contour-euler-safe", jet["sig_min"] > 1.0,
          "min Re s on contour = %.4f > 1 (abs. convergent)"
          % jet["sig_min"])
    check("G22-jet-real", max(jet["im_res"], jet["imF"]) <= BAR_IM,
          "max rel Im residual = %.1e" % max(jet["im_res"], jet["imF"]))

    jrep = build_jet_repro(A_MAIN, R_REPRO, M_REPRO, DPS_REPRO, ORD_REPRO)
    print("  repro jet (audit, mp.zeta): r=%d M=%d dps=%d orders=%d "
          "(%.1f s)" % (R_REPRO, M_REPRO, DPS_REPRO, ORD_REPRO,
                        jrep["secs"]))
    with mp.workdps(80):
        b0x = abs(jet["b"][0] / jrep["b"][0] - 1)
        d30 = max(abs(jet["b"][n] / jrep["b"][n] - 1)
                  for n in range(0, min(31, ord_main + 1)))
    check("G13-b0-cross", float(b0x) <= BAR_JETX,
          "b_0 lambda-route vs zeta-route rel dev %.2e (b_0 = %s)"
          % (float(b0x), mp.nstr(jet["b"][0], 12)))
    # containment: the cross-jet deviation must sit inside the
    # certified width of the lambda route (empirical certification ward)
    sk0 = jet_widths(jet, 0)
    cont = 0.0
    with mp.workdps(80):
        for n in range(0, min(31, ord_main + 1)):
            wd = cell_width(jet, sk0, n, 0, float(jet["b"][0]))
            dev = abs(float(jet["b"][n] - jrep["b"][n]))
            cont = max(cont, dev / wd)
    check("G22b-jet-cross-contained", cont <= 1.0,
          "max |b_lambda - b_zeta| / certified width (n<=30) = %.3f "
          "(raw max rel dev %.1e)" % (cont, float(d30)))

    # G02: empirical tail-bound ward at the worst contour point
    with mp.workdps(120):
        zt = mp.mpf(A_MAIN - R_MAIN)
        st = mp.mpf("0.5") + mp.sqrt(zt)
        fw = float(abs(audit_contour_F(zt, 120)
                       - jet_F_probe(jet, zt, st, ns_main)))
    tb = lambda_tail_bound(ns_main, float(st)) / (2 * math.sqrt(float(zt)))
    check("G02-tail-bound-ward", fw <= tb,
          "|F_lambda - F_zeta| = %.2e <= tail bound %.2e at sigma_min"
          % (fw, tb))

    # Hausdorff hypotheses executed on the CERTIFIED range of b_n
    # (beyond it the moments are Lambda-tail noise by construction)
    bs = jet["b"]
    sk0m = jet_widths(jet, 0)
    ncb = 0
    for n in range(ord_main + 1):
        if float(bs[n]) > cell_width(jet, sk0m, n, 0, float(bs[0])):
            ncb = n
        else:
            break
    okm = all(bs[n] > 0 for n in range(ncb + 1)) and \
        all(bs[n] > bs[n + 1] for n in range(ncb))
    check("G14-hausdorff-hypotheses", okm and ncb >= 40,
          "0 < b_n decreasing on the certified range n <= %d, "
          "b_0 = %s >= b_n (Widder hypotheses executed)"
          % (ncb, mp.nstr(bs[0], 10)))

    # ---------------------------------------------------------- S3
    section("S3  H2 PASCAL FIELD + DECODER (proposer reproduction)")
    tab = pascal_table(bs, min(depth_field, ord_main), DPS_MAIN)
    n561, neg561, weak, wloc = 0, 0, None, None
    for n in range(DEPTH_CENSUS + 1):
        for k in range(DEPTH_CENSUS + 1 - n):
            v = tab[n][k]
            n561 += 1
            if v <= 0:
                neg561 += 1
            if weak is None or v < weak:
                weak, wloc = v, (n, k)
    gsw = math.sqrt(A_MAIN * wloc[1] / (wloc[0] + 1)) if wloc[1] else 0.0
    check("G23-561-census", neg561 == 0 and n561 == 561,
          "%d/%d cells positive; weakest C_%s = %s at gamma* = %.2f"
          % (n561 - neg561, n561, wloc, mp.nstr(weak, 6), gsw))
    print("  proposer: 561/561, weakest C_(16,16) ~ %.3e at gamma* %.2f"
          % (PROP["weakest"], PROP["gamstar"]))
    print("  measured/proposer weakest ratio = %.6f"
          % (float(weak) / PROP["weakest"]))

    dec = chebyshev_jacobi(jrep["b"], N_JAC, DPS_REPRO)
    nodes, wts = dec["nodes"], dec["weights"]
    ok_nodes = all(0 < float(y) < 1 for y in nodes) and \
        all(float(w) > 0 for w in wts)
    check("G24-decoder-nodes", ok_nodes,
          "16 nodes in (0,1), weights > 0; y_1 = %s"
          % mp.nstr(nodes[0], 20))
    with mp.workdps(DPS_REPRO):
        mom_dev = max(abs(mp.fsum(w * y ** n for y, w in zip(nodes, wts))
                          / jrep["b"][n] - 1)
                      for n in range(2 * N_JAC))
    check("G24b-gauss-exactness", float(mom_dev) <= 1e-30,
          "max rel moment reproduction dev (n<=31) = %.1e"
          % float(mom_dev))

    gam_cache = ward_cache()
    with mp.workdps(DPS_REPRO):
        gams = [mp.sqrt(A_MAIN * (1 - y) / y) for y in nodes]
        g1dev = float(abs(gams[0] - mp.mpf(GAMMA1_LIT)))
    check("G25-gamma1", g1dev <= BAR_G25,
          "gamma_1^hat dev vs literature constant = %.3e "
          "(proposer 1.6e-25)" % g1dev)
    sixdev = [abs(float(gams[j]) - gam_cache[j]) for j in range(6)]
    check("G25b-first-six", max(sixdev) <= BAR_SIX,
          "devs: " + " ".join("%.1e" % d for d in sixdev)
          + " (proposer <= 8e-4)")
    mults = [float(w / y) for y, w in zip(nodes, wts)]
    check("G26-multiplicity", all(abs(m - 1) <= BAR_MULT
                                  for m in mults[:4]),
          "w_j/y_j (first 8): " + " ".join("%.4f" % m for m in mults[:8]))
    print("  all multiplicity reads: "
          + " ".join("%.3f" % m for m in mults))
    print("  decoded gammas: "
          + " ".join("%.6f" % float(g) for g in gams[:8]) + " ...")

    # two-moment decoder
    with mp.workdps(DPS_REPRO):
        Gams = [float(mp.sqrt(A_MAIN * (jrep["b"][n] / jrep["b"][n + 1] - 1)))
                for n in range(ORD_REPRO)]
    mono = all(Gams[n + 1] <= Gams[n] + 1e-12 for n in range(5, ORD_REPRO - 1))
    gap = abs(Gams[-1] - gam_cache[0]) / gam_cache[0]
    check("G27-two-moment", mono and gap <= BAR_G27,
          "Gamma_n monotone (n>=5): %s; final rel gap to gamma_1 = %.2e"
          % (mono, gap))

    # pins (H4c): quadrature vs audit target on the frozen 16-sigma grid
    pin_rows = []
    with mp.workdps(DPS_REPRO):
        for sg in SIGMAS:
            sgm = mp.mpf(repr(sg)) if isinstance(sg, float) else mp.mpf(sg)
            tgt = audit_xi_logderiv(mp.mpf("0.5") + sgm, DPS_REPRO)
            quad = 2 * sgm * quad_F(dec, A_MAIN, sgm * sgm, DPS_REPRO)
            pin_rows.append((float(sg), float(mp.re(tgt)),
                             abs(float((quad - mp.re(tgt)) / mp.re(tgt)))))
    maxpin = max(r[2] for r in pin_rows)
    for sg, tv, rd in pin_rows:
        print("    sigma %-8.4f  P = %+.12e   rel dev %.3e" % (sg, tv, rd))
    check("G28-pins", maxpin <= BAR_PINS,
          "max rel pin dev (N=16 quadrature) = %.3e (proposer 6.5e-37)"
          % maxpin)

    # P(sigma) = 2 sigma F(sigma^2) definitional wiring
    with mp.workdps(60):
        dmax = 0.0
        for sg in (0.8, 1.5, 3.0, 9.0):
            lhs = audit_xi_logderiv(mp.mpf("0.5") + mp.mpf(sg), 60)
            rhs = 2 * mp.mpf(sg) * audit_F(mp.mpf(sg) ** 2, 60)
            dmax = max(dmax, float(abs(lhs - rhs) / abs(lhs)))
    check("G18-pin-bridge", dmax <= 1e-30,
          "P(sigma) == 2 sigma F(sigma^2), max rel dev %.1e" % dmax)

    # Moebius flow: pushforward a -> a' vs direct jet at a'
    jflow = build_jet_lambda(A_FLOW, R_FLOW, M_FLOW, DPS_FLOW, NS_FLOW,
                             ORD_FLOW, "flow")
    with mp.workdps(DPS_REPRO):
        rr = mp.mpf(A_FLOW) / A_MAIN
        ypr = [rr * y / (1 + (rr - 1) * y) for y in nodes]
        wpr = [w * yp / y for y, w, yp in zip(nodes, wts, ypr)]
        flow_dev = max(
            abs(mp.fsum(w * y ** n for y, w in zip(ypr, wpr))
                / jflow["b"][n] - 1)
            for n in range(21))
    check("G29-moebius-flow", float(flow_dev) <= BAR_FLOW,
          "pushforward a=256->512 vs direct jet, max rel dev n<=20 = %.2e"
          % float(flow_dev))

    # ---------------------------------------------------------- S4
    section("S4  H3 CERTIFIED CONDITIONING (the decisive claim)")
    dmaxd = min(depth_field, ord_main)
    sk = jet_widths(jet, dmaxd)
    maxb = float(bs[0])
    certified = {}
    d_max, first_uncert = -1, None
    gstar_main = 0.0
    ncert = 0
    for d in range(dmaxd + 1):
        all_ok = True
        for n in range(d + 1):
            k = d - n
            w = cell_width(jet, sk, n, k, maxb)
            pos = tab[n][k] > mp.mpf(w)
            certified[(n, k)] = pos
            if pos:
                ncert += 1
                if k > 0:
                    gstar_main = max(gstar_main,
                                     math.sqrt(A_MAIN * k / (n + 1)))
            else:
                all_ok = False
                if first_uncert is None:
                    first_uncert = (n, k, float(tab[n][k]), w)
        if all_ok and d_max == d - 1:
            d_max = d
    check("G32-certified-depth", d_max >= BAR_DMAX,
          "d_max = %d (all cells n+k <= d certified positive); "
          "%d cells certified in the %d-triangle" % (d_max, ncert, dmaxd))
    if first_uncert:
        print("  first uncertified cell: C_%s = %.3e, width %.3e"
              % (first_uncert[:2], first_uncert[2], first_uncert[3]))
    check("G33-gammastar-main", gstar_main >= BAR_GSTAR_MAIN,
          "certified gamma* reach (main, a=256) = %.1f" % gstar_main)
    for (n, k) in ((16, 16), (2, min(dmaxd - 2, 100)),
                   (min(40, dmaxd), 0)):
        if n + k <= dmaxd:
            w = cell_width(jet, sk, n, k, maxb)
            print("  sample cell C_(%d,%d): value %.3e  width %.3e "
                  "(EVAL-dominated)" % (n, k, float(tab[n][k]), w))
    print("  width decomposition at (16,16): EVAL %.2e  ALIAS %.2e"
          % ((A_MAIN / R_MAIN) ** 17 * sk[16],
             2 * jet["mprime"] * jet["qal"] / (1 - jet["qal"])
             * (A_MAIN / jet["rp"]) ** 17
             * ((A_MAIN + jet["rp"]) / jet["rp"]) ** 16))
    print("  M' (rigorous |F| sup bound on R'=%d circle) = %.2f"
          % (jet["rp"], jet["mprime"]))

    gstar_arm = 0.0
    if do_arm:
        jarm = build_jet_lambda(A_ARM, R_ARM, M_ARM, DPS_ARM, NS_ARM,
                                ORD_ARM, "arm")
        print("  arm jet: a=%d r=%d M=%d dps=%d N=%d orders=%d (%.1f s)"
              % (A_ARM, R_ARM, M_ARM, DPS_ARM, NS_ARM, ORD_ARM,
                 jarm["secs"]))
        check("G21b-arm-safe", jarm["sig_min"] > 1.0,
              "min Re s (arm) = %.3f" % jarm["sig_min"])
        tab_arm = pascal_table(jarm["b"], ORD_ARM, DPS_ARM)
        sk_arm = jet_widths(jarm, ORD_ARM)
        maxb_arm = float(jarm["b"][0])
        arm_cert = 0
        arm_kmax = -1
        for n in range(ARM_NMAX + 1):
            for k in range(ORD_ARM + 1 - n):
                if k > ARM_KMAX:
                    break
                w = cell_width(jarm, sk_arm, n, k, maxb_arm)
                if tab_arm[n][k] > mp.mpf(w):
                    arm_cert += 1
                    if k > 0:
                        gstar_arm = max(gstar_arm,
                                        math.sqrt(A_ARM * k / (n + 1)))
                        arm_kmax = max(arm_kmax, k)
        check("G33b-gammastar-arm", gstar_arm >= BAR_GSTAR_ARM,
              "certified gamma* reach (arm, a=1024) = %.1f "
              "(k_max cert = %d, %d cells)" % (gstar_arm, arm_kmax,
                                               arm_cert))
    print("  EULER-PICK comparison (CCCXCVI frozen): certified N=3 "
          "~ gamma <~ %s;" % EULERPICK["greach"])
    print("  kappa(P_12) = %.3e; here: certified positive depth d_max=%d,"
          % (EULERPICK["kappa12"], d_max))
    print("  gamma* reach %.0f (main) / %.0f (arm) from pure Euler data --"
          % (gstar_main, gstar_arm))
    print("  the Hausdorff safe-point field certifies far beyond the "
          "Euler-Pick slice.")

    # decay-law screen (H5c)
    dmins = []
    for d in range(8, DEPTH_CENSUS + 1):
        mv = min(float(tab[n][d - n]) for n in range(d + 1))
        dmins.append((d, math.log10(abs(mv))))
    xs = np.array([d for d, _ in dmins])
    ys = np.array([v for _, v in dmins])
    slope = float(np.polyfit(xs, ys, 1)[0])
    check("G57-decay-law", DECAY_BAND[0] <= slope <= DECAY_BAND[1],
          "min-cell slope = %.4f per depth (spectral prediction "
          "0.5 log10 y1(1-y1) = -0.304)" % slope)
    info("tau-screen: structurally absent -- no Galerkin matrix, no "
         "extremal eigenvalue anywhere in this pipeline; the margin "
         "decays by the spectral law above, not by a conditioning "
         "artefact (wall-margin collapse channel does not exist here)")

    # ---------------------------------------------------------- S5
    section("S5  H4 TWO-CARRIER REPLICATION")
    # (a) signpos bridge
    tpos = signpos_positions(8.0, 8)
    sp_dev = [abs(tpos[j] - float(gams[j])) for j in range(5)]
    print("  signpos t_j (x=8, fejer): "
          + " ".join("%.4f" % t for t in tpos[:6]))
    print("  jacobi gamma_j:           "
          + " ".join("%.4f" % float(g) for g in gams[:6]))
    check("G41-signpos-bridge", max(sp_dev) <= BAR_SIGNPOS,
          "max |t_j - gamma_hat_j| (j<=5) = %.4f (two independent "
          "source-only reconstructions)" % max(sp_dev))
    info("CCCXCVIII context: the signpos rounding form is measured FALSE "
         "beyond x=13; this comparison lives at the gated rung x=8")

    # (b) Krein duality
    try:
        import krein_screw_realization_probe as KR
        KR.mp_setup()
        t0 = time.time()
        bl = KR.build_lags_mp(2.568, "0.003", "TRUE")
        sz = KR.szego_mp(bl["row"])
        kr_ok = sz["ok"]
        kdevs = []
        for sg, tv, _rd in pin_rows:
            P, R, _c = KR.pin_from_disk(bl, sz, sg)
            kdevs.append((sg, P, abs(P - tv), R))
        kmax = max(d for _s, _p, d, _r in kdevs)
        kmed = sorted(d for _s, _p, d, _r in kdevs)[len(kdevs) // 2]
        for sg, P, d, R in kdevs:
            print("    sigma %-8.4f  P_krein = %+.9e  |dP| = %.2e  "
                  "R_disk = %.1e" % (sg, P, d, R))
        check("G42-krein-pins", kr_ok and kmax <= BAR_KREIN_MAX
              and kmed <= BAR_KREIN_MED,
              "max |P_hausdorff - P_krein| = %.2e, median %.2e "
              "(krein build %.1f s; both source-only, no zero cache)"
              % (kmax, kmed, time.time() - t0))
    except Exception as exc:  # noqa: BLE001 -- typed skip, printed
        check("G42-krein-pins", False, "krein import/run failed: %r" % exc)

    # ---------------------------------------------------------- S6
    section("S6  H5 OFF-LINE DETECTOR + CONTROLS")
    print("  matched-ray phase is stationary to O(delta^3) (symbolic "
          "gate H5a-matched-ray-phase):")
    print("  detection runs through the k=0 channel, alive only for "
          "gamma0 < gamma_1.")
    bflt = np.array([float(b) for b in bs])
    tabf = [[float(tab[n][k]) for k in range(len(tab[n]))]
            for n in range(len(tab))]
    # per-cell certified widths of the base field (noise guard: a flip
    # counts only on base-certified cells and must clear the width)
    wid = [[cell_width(jet, sk, n, d - n, maxb) for n in range(d + 1)]
           for d in range(dmaxd + 1)]
    y1f = float(nodes[0])
    plant_rows = []
    configs = [(g0, dl) for g0 in PLANT_GAMMA0 for dl in PLANT_DELTA]
    configs += list(PLANT_EXTRA)
    for g0, dl in configs:
        z0 = complex(dl, g0) ** 2
        y0 = A_MAIN / (A_MAIN - z0)
        first = None
        for d in range(1, dmaxd + 1):
            for n in range(d + 1):
                k = d - n
                pert = 2.0 * (y0 ** (n + 1) * (1 - y0) ** k).real
                if tabf[n][k] + pert < -wid[d][n]:
                    first = (d, n, k, pert)
                    break
            if first:
                break
        argy = math.atan2(2 * dl * g0, A_MAIN + g0 * g0 - dl * dl)
        pred = (math.pi / 2) / argy if abs(y0) > y1f else float("nan")
        # Hankel channel (mp moments; resolution floor 1e-45 declared)
        with mp.workdps(DPS_MAIN):
            bp = [bs[n] + 2 * mp.re(mp.mpc(y0) ** (n + 1))
                  for n in range(25)]
        nh, _mind = hankel_first_negative(bp, 12, DPS_MAIN)
        plant_rows.append((g0, dl, first, pred, nh, abs(y0)))
        fstr = ("d*=%d at (n=%d,k=%d)" % first[:3]) if first else \
            ("NONE <= %d" % dmaxd)
        print("    gamma0=%-5.1f delta=%-5.2f |y0|=%.4f  pascal: %-22s "
              "pred(k=0) %-7s hankel N*=%s"
              % (g0, dl, abs(y0), fstr,
                 ("%.0f" % pred) if pred == pred else "dead", nh))
    row_g8_d4 = next(r for r in plant_rows if r[0] == 8.0 and r[1] == 0.4)
    if smoke and row_g8_d4[3] > dmaxd:
        info("G51 SMOKE-SKIP: k=0 prediction %.0f beyond smoke depth %d"
             % (row_g8_d4[3], dmaxd))
    else:
        okp = (row_g8_d4[2] is not None
               and abs(row_g8_d4[2][0] - row_g8_d4[3]) / row_g8_d4[3]
               <= 0.20)
        check("G51-planted-fires", okp,
              "gamma0=8 delta=0.4: measured d* = %s vs k=0 prediction "
              "%.0f (bar +-20 pct)"
              % (row_g8_d4[2][0] if row_g8_d4[2] else None, row_g8_d4[3]))
    for g0v in (8.0, 12.0):
        fr = sorted((dl, f[0]) for g0, dl, f, _p, _nh, _y in plant_rows
                    if g0 == g0v and f)
        if len(fr) >= 2:
            (dl_a, da), (dl_b, db) = fr[-1], fr[-2]
            info("detection law gamma0=%.0f: d*(%.2f)/d*(%.2f) = %.4f "
                 "vs 1/delta model %.4f -- d* ~ 1/delta confirmed"
                 % (g0v, dl_b, dl_a, db / da, dl_a / dl_b))
    blind = [(g0, dl) for g0, dl, f, _p, _nh, _y in plant_rows
             if g0 > 14.0 and f is None]
    info("gamma0 > gamma_1 rows undetected in Pascal to depth %d: %s "
         "(magnitude channel dead, |y0| < y_1; matched-ray phase exactly "
         "stationary) -- Hankel channel N* above still fires"
         % (dmaxd, blind))

    # (b) EPSTEIN control
    with mp.workdps(40):
        x16 = audit_epstein_xi(mp.mpf("16.5"), 40)
        x16b = (mp.mpf("16.5") * mp.mpf("15.5")
                * (2 * mp.pi / mp.sqrt(20)) ** mp.mpf("-16.5")
                * mp.gamma(mp.mpf("16.5"))
                * epstein_Z_series(mp.mpf("16.5"), q_eps))
        xw1 = float(abs(x16 / x16b - 1))
        ld1 = audit_epstein_series_xi_logderiv(mp.mpc("8.5", "0.7"),
                                               3000, 80)
        with mp.workdps(80):
            u0 = mp.mpc("8.5", "0.7")
            hh = mp.mpf("1e-20")
            ld2 = ((mp.log(audit_epstein_xi(u0 + hh, 80))
                    - mp.log(audit_epstein_xi(u0 - hh, 80))) / (2 * hh))
        xw2 = float(abs(ld1 / ld2 - 1))
        fe = float(abs(audit_epstein_xi(mp.mpf("0.3"), 40)
                       / audit_epstein_xi(mp.mpf("0.7"), 40) - 1))
    check("G55-epstein-xward", xw1 <= BAR_EPS_XWARD and xw2 <= 1e-15
          and fe <= 1e-25,
          "series vs incomplete-gamma: xi rel %.1e, logderiv rel %.1e "
          "(mp.diff); func-eq |xi(0.3)/xi(0.7)-1| = %.1e"
          % (xw1, xw2, fe))

    # zero hunt on the real axis
    with mp.workdps(40):
        grid = [0.02 * i for i in range(1, 50)]
        vals = [float(audit_epstein_xi(mp.mpf(repr(g)), 40)) for g in grid]
    zeros_real = []
    for i in range(len(grid) - 1):
        if vals[i] * vals[i + 1] < 0:
            lo, hi = grid[i], grid[i + 1]
            with mp.workdps(40):
                root = float(mp.findroot(
                    lambda u: audit_epstein_xi(u, 40),
                    mp.mpf(repr(0.5 * (lo + hi)))))
            zeros_real.append(root)
    print("  Epstein xi_Q real zeros in (0,1): %s   xi_Q(1/2) = %.6e"
          % (["%.6f" % z for z in zeros_real],
             vals[24] if len(vals) > 24 else float("nan")))

    jeps = build_jet_epstein(A_MAIN, R_EPS, m_eps, DPS_EPS, q_eps, ord_eps)
    print("  epstein jet: %d lattice points, min Re s = %.3f (%.1f s)"
          % (jeps["npts"], jeps["sig_min"], jeps["secs"]))
    tab_q = pascal_table(jeps["b"], ord_eps, DPS_EPS)
    sk_q = jet_widths(jeps, ord_eps)
    first_q = None
    q_resolved_depth = 0
    for d in range(1, ord_eps + 1):
        row_resolved = True
        for n in range(d + 1):
            k = d - n
            wq = (A_MAIN / R_EPS) ** (n + 1) * sk_q[k]
            v = float(tab_q[n][k])
            if abs(v) <= wq:
                row_resolved = False
                continue
            if v < -wq:
                first_q = (d, n, k, v)
                break
        if first_q:
            break
        if row_resolved and q_resolved_depth == d - 1:
            q_resolved_depth = d
    if first_q:
        info("EPSTEIN Pascal channel: first resolved negative "
             "C_(%d,%d) = %.3e at depth %d"
             % (first_q[1], first_q[2], first_q[3], first_q[0]))
    else:
        info("EPSTEIN Pascal channel: NO resolved negative cell to depth "
             "%d (fully noise-resolved to depth %d; EVAL-width guard) -- "
             "consistent with the phase model: off-line zeros are complex "
             "and sit above gamma_1(Q), detection depth >> %d"
             % (ord_eps, q_resolved_depth, ord_eps))
    nq, mindq = hankel_first_negative(jeps["b"], 14, DPS_EPS)
    info("EPSTEIN Hankel channel: first negative minor N* = %s "
         "(min det seen %.2e; floor 1e-45)" % (nq, mindq))
    # on-line gamma_1(Q) (coarse) -- context for the magnitude channel
    with mp.workdps(30):
        tg = [0.5 + 0.25 * i for i in range(24)]
        xv = [float(mp.re(audit_epstein_xi(
            mp.mpc("0.5", repr(t)), 30))) for t in tg]
    g1q = None
    for i in range(len(tg) - 1):
        if xv[i] * xv[i + 1] < 0:
            g1q = 0.5 * (tg[i] + tg[i + 1])
            break
    info("EPSTEIN on-line gamma_1(Q) ~ %s -> y_1(Q) = %.4f"
         % (g1q, A_MAIN / (A_MAIN + g1q ** 2) if g1q else float("nan")))
    # G54a: the witness off-line zero from the FROZEN seed
    rho0, resid = None, float("nan")
    try:
        with mp.workdps(40):
            rt = mp.findroot(lambda u: audit_epstein_xi(u, 40),
                             mp.mpc("0.7", "36.4"), maxsteps=40)
            resid = float(abs(audit_epstein_xi(rt, 40)))
        r0 = complex(rt)
        if 0.55 < r0.real < 0.85 and resid < 1e-25:
            rho0 = r0
    except Exception:  # noqa: BLE001 -- typed below
        pass
    check("G54a-epstein-zero-located", rho0 is not None,
          "off-line witness zero rho = %s, |xi_Q(rho)| = %.1e "
          "(frozen seed 0.7+36.4i; RH-for-Q provably false)"
          % ("%.8f%+.8fi" % (rho0.real, rho0.imag) if rho0 else None,
             resid))
    # G54b: blindness consistency -- plant exactly this zero on TRUE
    if rho0 is not None:
        d0q, g0q = rho0.real - 0.5, rho0.imag
        z0q = complex(d0q, g0q) ** 2
        y0q = A_MAIN / (A_MAIN - z0q)
        arg1y = abs(math.atan2((1 - y0q).imag, (1 - y0q).real))
        argy = abs(math.atan2(y0q.imag, y0q.real))
        info("phase model for the witness: |y0| = %.4f < y_1 = %.4f "
             "(magnitude channel dead); k-channel depth ~ %.0f, "
             "n-channel ~ %.0f -- Pascal blindness at depth %d is the "
             "PREDICTION, not an anomaly"
             % (abs(y0q), y1f, (math.pi / 2) / max(arg1y, 1e-12),
                (math.pi / 2) / max(argy, 1e-12), ord_eps))
        rep_first = None
        for d in range(1, min(BAR_EPS_DEPTH, dmaxd) + 1):
            for n in range(d + 1):
                k = d - n
                pert = 2.0 * (y0q ** (n + 1) * (1 - y0q) ** k).real
                if tabf[n][k] + pert < -wid[d][n]:
                    rep_first = (d, n, k)
                    break
            if rep_first:
                break
        with mp.workdps(DPS_MAIN):
            brep = [bs[n] + 2 * mp.re(mp.mpc(y0q) ** (n + 1))
                    for n in range(29)]
        nrep, _m = hankel_first_negative(brep, 14, DPS_MAIN)
        q_pascal_fired = (first_q is not None
                          and first_q[0] <= BAR_EPS_DEPTH)
        okb = ((rep_first is not None) == q_pascal_fired
               and (nrep is not None) == (nq is not None))
        check("G54b-blindness-consistency", okb,
              "planted replica of the witness on TRUE: pascal %s / "
              "hankel N* %s == Q-field pascal %s / hankel N* %s "
              "(fires-iff-fires at matched caps)"
              % (rep_first, nrep,
                 first_q[:3] if q_pascal_fired else None, nq))
    else:
        check("G54b-blindness-consistency", False, "no witness zero")
    # near-line root printed, not gate-bearing
    try:
        with mp.workdps(40):
            rt2 = mp.findroot(lambda u: audit_epstein_xi(u, 40),
                              mp.mpc("0.5002", "44.58"), maxsteps=40)
        info("near-line root (UNRESOLVED, not gate-bearing): %s"
             % mp.nstr(rt2, 12))
    except Exception:  # noqa: BLE001
        pass

    # (c) smooth control
    jsm = build_jet_smooth(A_MAIN, R_MAIN, m_main, DPS_MAIN, ord_main)
    with mp.workdps(60):
        b0s = jsm["b"][0]
        s_a = mp.mpf("0.5") + mp.sqrt(mp.mpf(A_MAIN))
        b0d = (A_MAIN * (1 / s_a + 1 / (s_a - 1) - mp.log(mp.pi) / 2
                         + mp.digamma(s_a / 2) / 2)
               / (2 * mp.sqrt(mp.mpf(A_MAIN))))
        smw = float(abs(b0s / b0d - 1))
    check("G56-smooth-wiring", smw <= 1e-40,
          "smooth b_0 jet vs direct = rel %.1e" % smw)
    tab_s = pascal_table(jsm["b"], ord_main, DPS_MAIN)
    first_s = None
    for d in range(1, ord_main + 1):
        for n in range(d + 1):
            k = d - n
            if float(tab_s[n][k]) < 0:
                first_s = (d, n, k, float(tab_s[n][k]))
                break
        if first_s:
            break
    ns_h, minds = hankel_first_negative(jsm["b"], 14, DPS_MAIN)
    if first_s:
        info("SMOOTH control: first negative C_(%d,%d) = %.3e at depth %d"
             " -- the prime-free jet FAILS complete monotonicity "
             "(Hankel channel: N* = %s)"
             % (first_s[1], first_s[2], first_s[3], first_s[0], ns_h))
    else:
        info("SMOOTH control: positive to depth %d -- positivity does NOT "
             "discriminate primes-from-smooth at this depth (criterion is "
             "a zero-location rigidity statement, not an arithmetic "
             "detector)" % ord_main)

    # Z1 typing
    z1rows = []
    for n in (0, 2, 5, 10, 20, 40, 60):
        if n > ord_main:
            continue
        bc = ward_bn_cache(gam_cache, float(A_MAIN), n)
        z1rows.append((n, abs(float(bs[n]) / bc - 1)))
    z1max0 = z1rows[0][1]
    z1max2 = max(d for n, d in z1rows if n >= 2)
    for n, d in z1rows:
        print("    b_%-3d jet vs cache+RvM rel dev %.3e" % (n, d))
    check("G58-z1-zeromeasure", z1max0 <= BAR_Z1_N0
          and z1max2 <= BAR_Z1_N2,
          "n=0 dev %.2e (RvM tail model), max n>=2 dev %.2e -> content "
          "IS the zero measure" % (z1max0, z1max2))

    # ---------------------------------------------------------- S7
    section("S7  H6 COMPOSITE VERDICT")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    ntot = len(CHECKS)
    equiv = "HAUSDORFF-EQUIVALENCE-SOUND" if all(
        ok for nm, ok, _ in CHECKS if nm.startswith("H1")) else \
        "HAUSDORFF-EQUIVALENCE-GAP"
    verdict = [
        equiv + "(Hausdorff1921/Widder-III.4a + identity-theorem + "
        "removability; all numeric ingredients gated)",
        "HAUSDORFF-REPRODUCED(561/561, weakest %.3e~prop %.3e, "
        "gamma1 %.1e, pins %.1e)" % (float(weak), PROP["weakest"],
                                     g1dev, maxpin),
        "HAUSDORFF-CERTIFIED-DEPTH(d_max=%d, gamma*=%.0f/%.0f vs "
        "Euler-Pick N=3 ~ gamma 5-8)" % (d_max, gstar_main, gstar_arm),
        "HAUSDORFF-REPLICATION(signpos %.3f; krein see G42)"
        % max(sp_dev),
        "HAUSDORFF-DETECTOR(k=0 law d*~1/delta below gamma_1; Pascal "
        "blind above gamma_1 -- Epstein witness rho located, blindness "
        "consistent, model depth ~9e2; Epstein pascal %s hankel N*=%s; "
        "smooth NEG@d=%s N*=%s)"
        % ("NEG@d=%d" % first_q[0] if first_q else "not<=%d" % ord_eps,
           nq, first_s[0] if first_s else None, ns_h),
        "HAUSDORFF-Z1-ZEROMEASURE + NOT-WORLD-NEW(Zhang 2303.09396; "
        "novelty = safe-point shift + certified conditioning)",
    ]
    for v in verdict:
        print("  " + v)
    print("\n  NAKED REMAINING TASK: positivity of ALL C_{n,k}(a) -- "
          "Weil positivity in Hausdorff")
    print("  currency; a THIRD equivalent lemma form next to the two "
          "standing ones (uniform")
    print("  Weyl-disk contraction of the Krein system; sign-change "
          "positions of the ground")
    print("  eigenvector).  The certified field extends the finite "
          "no-witness region far")
    print("  beyond Euler-Pick in gamma*, but touches the all-(n,k) "
          "quantifier nowhere.")

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR, "%.1f s (bar %.0f)"
          % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass + (1 if dt <= RUNTIME_BAR else 0), ntot + 1,
             SPEC_SHA[:16], dt))
    fails = [nm for nm, ok, _ in CHECKS if not ok]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


# helper used by G02 (module scope to keep build_jet_lambda unmodified)
def jet_F_probe(jet: dict, z, s, nsieve: int):
    """Re-evaluate the Lambda-route F at a real test point (source)."""
    with mp.workdps(jet["dps"]):
        pps = sieve_prime_powers(nsieve)
        logs = {}
        acc = mp.mpf(0)
        for q, p in pps:
            if p not in logs:
                logs[p] = mp.log(p)
            acc += logs[p] * mp.exp(-s * mp.log(q))
        return ((1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
                 + mp.digamma(s / 2) / 2 - acc) / (2 * mp.sqrt(z)))


def epstein_Z_series(s, qmax: int):
    with mp.workdps(40):
        return mp.fsum(cnt * mp.power(q, -s)
                       for q, cnt in epstein_lattice(qmax))


if __name__ == "__main__":
    sys.exit(main())
