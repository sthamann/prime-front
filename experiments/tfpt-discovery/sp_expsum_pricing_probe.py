#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sp_expsum_pricing_probe.py -- THE (SP) ROUNDING-MARGIN STATEMENT PRICED
AGAINST CLASSICAL EXPONENTIAL-SUM TECHNOLOGY, WITH THE CHAIN'S QUANTIFIER
STRUCTURE EXTRACTED EXACTLY AND THE MARGIN CENSUS PUSHED TO THE CACHE EDGE.

EXPLORATION PROBE, experiments/ only.  NO RH CLAIM.  NO POSITIVITY CLAIM.
Nothing here is load-bearing, nothing promoted, no marker moves, no gate
closed or narrowed.

=======================================================================
THE OBJECT (round-88 record, signpos_probe.py; re-implemented here)
=======================================================================
a = (log x)/2, Nyquist lattice om_k = k pi/a, K(x) = ceil(1.25 x log x).
Source-only counting predictor (signpos_probe.py lines 50-58, 508-541):
  N_src(T) = theta(T)/pi + 1 + S_x(T),
  theta(T) = Im log Gamma(1/4 + iT/2) - (T/2) log pi,
  S_x(T)   = -(1/pi) sum_{n = p^m <= x} (Lambda(n)/sqrt(n))
             * sin(T log n)/log n * taper(log n),
  taper    = 1 - log n/(2a)   (Fejer, PRIMARY; declared round 88).
EXPONENTIAL-SUM NORMAL FORM (S1 deliverable, verified bit-level here):
  S_x(T) = Im[ (1/pi) sum_{n=p^m<=x} beta_n e^{-iT log n} ],
  beta_n = Lambda(n) n^{-1/2} (log n)^{-1} (1 - log n/log x)  >= 0,
i.e. ONE finite exponential sum over prime powers, frequencies
u_n = log n in (0, 2a], amplitudes beta_n, band limit exactly 2a.
(SP) [open; TPL(i) verbatim per note CCCLXXXVII]: at every lattice point
of every rung of a predeclared cofinal family,
  dist(N_src(om_k), Z + 1/2) > 0,
equivalently margin_k = 1/2 - |eps_k| > 0 with
eps_k = N_src(om_k) - N_true(om_k) (signpos_probe.py line 64).

=======================================================================
WHAT THIS PROBE DOES (S1..S4 of the round order)
=======================================================================
S1  Extract the sum exactly (identity ward vs an independent
    amplitude-phase implementation), measure its analytic profile:
    band limit, l1/l2 coefficient masses, total variation over the
    band, and the value distribution at the lattice points.
S2  Price the classical arsenal against the half-integer budget 1/2:
    (a) trivial l1;  (b) van der Corput 2nd/3rd-derivative tests with
    the actual phase derivatives (f(v) = (t/2pi) log v);  (c) the
    Vaughan/Vinogradov route ceiling = the argument-principle bound
    S(t) = O(log t), explicit constants [T14], exponent pair
    (13/84, 55/84) [B17];  (d) large sieve / mean values: the EXACT
    large-sieve constant of the deployed configuration (lambda_max of
    the dual Gram matrix, rigorous per-rung census bound on the
    finite sum), plus the quantifier answer extracted verbatim from
    v848/v849/tp_opus;  (e) the conditional ladder (Lindelof, density,
    RH) -- all magnitude routes evaluated numerically at the deployed
    heights.
S3  The margin census to the cache edge: ladder x = 3..890 (source
    side + read-only cache ONLY; the round-88 eigenvector truth
    channel is NOT re-verified beyond x = 13 -- declared), min-margin
    trend, exceptional-set census vs eps, violation positions,
    ordinate-distance coupling, Weyl/discrepancy of the phase mod 1,
    and the declared heuristic variance model vs measurement.
S4  Composite verdict with the pricing table; every reported margin
    tau-screened (mp dps-40 recompute + cache jitter).

FROZEN LADDER, BARS, MODELS, SEEDS (before any run)
  Ladder X = (3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 890);
  rung admitted iff om_{K-1} <= gamma_top - 2.0 (cache coverage).
  K(x) = ceil(1.25 x log x) (round-88 KFAC).  PRIMARY taper fejer;
  sharp printed, never gated.  Round-88 reproduction bars: min margins
  (0.4371, 0.3250, 0.0470, 0.0317) at x = (3,5,8,13) tol 5e-4;
  density-only failure sets {10,11}@x=8, {23,25}@x=13; the four
  repaired eps pairs tol 2e-3.  Representation-identity bar 1e-12.
  Trivial-bound crossing claim: B_triv > 1/2 from some rung x* <= 89
  onward.  Pricing gate: every unconditional pointwise technology
  value at band top > 1/2 on every admitted rung x >= 8.  Large-sieve
  gates: Sum_k |A(om_k)|^2 <= lambda_max(H) Sum beta^2/pi^2 and
  #{|S_x| >= 1/2} <= that/(1/2)^2 (both theorems; numeric wards).
  Phase-concentration gate: pooled mean dist(N_src, Z) < 0.15 and
  pooled |W_1| > 0.2.  tau-screen bars: mp dev <= 1e-8, jitter
  (+-1e-8, seed 20260815) min-margin dev < 1e-6 barring a lattice
  crossing (reported).  Prefix bar for the average-route verdict:
  all measured violations (if none: all margins < 0.05) at relative
  height k/K >= 0.20.  Variance model (DECLARED HEURISTIC, typed,
  never gated): eps(t) treated as random-phase sum with resolved
  cutoff n <= t: Var = (1/2 pi^2) [ sum_{n<=min(x,t)} b_n^2
  (u_n/2a)^2 + sum_{t<n<=x} beta_n'^2 + sum_{x<n<=t} b_n^2 ],
  b_n = Lambda(n)/(sqrt(n) log n), beta_n' = b_n (1 - u_n/2a).
  TV grid: 6x Nyquist oversampling (2x in smoke).  Runtime bar 900 s.

DECLARED SUBSAMPLING AND LIMITS
  Extension rungs x > 13 consume float64 source evaluations and the
  read-only ordinate cache only -- no mp matrix, no eigenvector: the
  (SP) margins are the direct object; predictor-vs-EIGENVECTOR
  exactness stays measured only on the round-88 rungs.  The variance
  model and the Gaussian census prediction are heuristics for
  COMPARISON, typed, never gated.  The vdC/exponent-pair pricing
  grants the technology constant 1 and ignores partial-summation and
  Vaughan-decomposition losses (GENEROUS by design: a kill under
  generous pricing is a clean kill).  tau-screen covers precision and
  cache jitter, not the choice of taper (both tapers printed).

CITATIONS (each with its exact role; [T14]/[CCM13] verified live
2026-08-15 against publisher/ANU/ADS records)
  [T14]  T. S. Trudgian, J. Number Theory 134 (2014) 280-292,
         DOI 10.1016/j.jnt.2013.07.017: |S(t)| <= 0.112 log t
         + 0.278 log log t + 2.510 for t >= e -- the sharpest-in-class
         explicit unconditional pointwise bound (Backlund method).
  [CCM13] E. Carneiro, V. Chandee, M. B. Milinovich, Math. Ann. 356
         (2013) 939-968: RH => |S(t)| <= (1/4 + o(1)) log t/log log t.
  [B17]  J. Bourgain, J. Amer. Math. Soc. 30 (2017) 205-224:
         zeta(1/2+it) << t^{13/84+eps}; exponent pair (13/84, 55/84).
  [GK91] S. W. Graham, G. Kolesnik, Van der Corput's Method of
         Exponential Sums, CUP 1991: Thm 2.2 (2nd-derivative test),
         Thm 2.6 (3rd-derivative test).
  [V77]  R. C. Vaughan, C. R. Acad. Sci. Paris A 285 (1977) 981-983;
         H. Davenport, Multiplicative Number Theory 3rd ed. Ch. 24:
         the identity decomposing sum Lambda(n) e(f(n)).
  [S46]  A. Selberg, Arch. Math. Naturvid. 48 (1946) 89-155:
         unconditional moments of S(t); prime-sum approximation on
         average with cutoff a SMALL POWER of the height.
  [G87]  D. A. Goldston, J. Number Theory 27 (1987) 149-177: the mean
         value of S(t) and its prime-sum approximation; the long-
         cutoff regime is tied to pair correlation.
  [MV74] H. L. Montgomery, R. C. Vaughan, J. London Math. Soc. (2) 8
         (1974) 73-82: Hilbert inequality / large sieve for
         well-spaced points.
  [Ts86] K.-M. Tsang, Acta Arith. 46 (1986) 369-395: unconditional
         S(t) = Omega_{+-}((log t/log log t)^{1/3}).
  [M77]  H. L. Montgomery, Comment. Math. Helv. 52 (1977): RH =>
         S(t) = Omega_{+-}((log t/log log t)^{1/2}).
  [L24]  J. E. Littlewood 1924 (see Titchmarsh, Theory of the Riemann
         Zeta-Function, 2nd ed., Ch. 13-14): RH => S = O(log t/
         log log t); Lindelof => S = o(log t) (no explicit constant).
  [PP37] M. Plancherel, G. Polya, Comment. Math. Helv. 9 (1937):
         lattice l2 <= C L2 for band-limited functions -- the transfer
         that FAILS for the non-band-limited error S_x - S.
  CORPUS: v848_extraction_chain.py (STEP 2 cofinality), v849 (H_cof
  kernel hierarchy), tp_opus_probe.py (count_depth / TPL(i) prefix
  form), kill_atlas_dag_probe.py + v913 (Littlewood emptiness
  ||K_D'||_1 = 4, ratios 214.7/1527.1), signpos_probe.py + note
  CCCLXXXVII (the object and the frozen margins).

TWO FORMS OF (SP), SEPARATED (measured separately, verdicts typed)
  SP-OPERATIVE (TPL(i) finite form, the corpus margin): margin_k =
    1/2 - |eps_k| > 0, i.e. round(N_src(om_k)) == N_true(om_k).
  SP-LITERAL (the bare non-vanishing): dist(N_src(om_k), Z+1/2) > 0
    = |margin_k| -- true also at a rounding VIOLATION (where the
    predictor rounds to the WRONG integer while missing the exact
    half-integer).  Literal non-vanishing without a lower-bound law
    carries no extraction content; the operative form is what the
    round-88 exactness measured.

AMENDMENT (disclosed; after the first full ladder run, before the
frozen run; no measured number changed): the original G08 gated the
pooled phase concentration (mean dist(N_src, Z) < 0.15, |W_1| > 0.2)
-- a bar written EXPECTING (SP)-operative survival.  The first full
run measured the falsification instead (parity violations from x = 21
on).  Gating the hypothesis under test smuggles the expected outcome
into the instrument (signpos G12 precedent: a measurement channel is
'recorded either way').  G08 is therefore TYPED: the gate now checks
only instrument sanity (|W_m| <= 1, D* in (0,1], census computed);
the concentration/equidistribution VERDICT is printed and typed,
never gated.  The taper-variance decomposition print (section V) was
added in the same amendment to name the mechanism: the Fejer taper
deficit alone carries Var >= (1/2)(1/2pi^2), i.e. tracking rms ->
1/(2pi) ~= 0.159 as x -> inf -- an O(1) floor against the 1/2 budget,
independent of arithmetic.  No bar of the round-88 reproduction ward,
the pricing gates, the large-sieve wards or the tau-screen moved.

NO RH CLAIM.  EXPLORATION ONLY.  A clean kill with numbers is a
success.
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
from scipy.special import loggamma as sp_loggamma
from scipy.special import digamma as sp_digamma

# ------------------------------------------------------------------ bars
KFAC = 1.25
LADDER = (3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 890)
R88_RUNGS = (3, 5, 8, 13)
R88_MINMARG = {3: 0.4371, 5: 0.3250, 8: 0.0470, 13: 0.0317}
R88_TOL = 5e-4
R88_P0FAIL = {3: (), 5: (), 8: (10, 11), 13: (23, 25)}
R88_EPS = {(8, 10): (0.619, 0.453), (8, 11): (-0.603, -0.420),
           (13, 23): (0.578, 0.468), (13, 25): (-0.679, -0.371)}
R88_EPS_TOL = 2e-3
REPR_BAR = 1e-12
COVER_MARGIN = 2.0
TRIV_CROSS_MAX = 89
NEED = 0.5
PRICE_MIN_X = 8
EPS_GRID = (0.02, 0.05, 0.10, 0.20, 0.30)
PREFIX_REL_BAR = 0.20
CONC_DIST_BAR = 0.15
CONC_W1_BAR = 0.20
TAU_MP_BAR = 1e-8
TAU_JIT_BAR = 1e-6
JIT_SIZE = 1e-8
SEED = 20260815
TV_OVS = 6
MP_DPS = 40
RUNTIME_BAR = 900.0
EULER = 0.57721566490153286061
LOG_PI = math.log(math.pi)
GAMMA1_LIT = 14.134725141734693790          # literature constant, ward only

# exact-string corpus wards (quantifier extraction, S2d)
WARD_STRINGS = (
    ("verification/v848_extraction_chain.py",
     "cofinal set meets every tail"),
    ("verification/v849_cfin_unique_cofinal_lean.py",
     "never mined from measured signs"),
    ("verification/v849_cfin_unique_cofinal_lean.py",
     "cofinal_not_pointwise"),
    ("experiments/tfpt-discovery/tp_opus_probe.py",
     "the largest m such that"),
    ("experiments/tfpt-discovery/tp_opus_probe.py",
     "TPL(i) is exactly the statement D(x) -> inf"),
    ("experiments/tfpt-discovery/kill_atlas_dag_probe.py",
     "||K_D'||_1 = 4 uniformly"),
    ("experiments/tfpt-discovery/signpos_probe.py",
     "margin_k = 1/2 - |eps_k|"),
)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-46s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ======================================================== source tables
def prime_power_atoms(cap: float):
    """(n, u = log n, w = Lambda(n)/sqrt(n)) for ALL p^m <= cap.
    Own sieve (signpos_probe.py lines 160-179 convention), no oracle."""
    icap = int(math.floor(cap + 1e-12))
    if icap < 2:
        return np.zeros(0), np.zeros(0), np.zeros(0)
    comp = np.zeros(icap + 1, dtype=bool)
    ns, us, ws = [], [], []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        lp = math.log(p)
        q = p
        while q <= icap:
            ns.append(float(q))
            us.append(math.log(q))
            ws.append(lp / math.sqrt(q))
            q *= p
    o = np.argsort(np.asarray(us))
    return (np.asarray(ns)[o], np.asarray(us)[o], np.asarray(ws)[o])


def theta_arch(T: np.ndarray) -> np.ndarray:
    """Riemann-Siegel theta via log Gamma (archimedean source data;
    signpos_probe.py lines 501-505 verbatim convention)."""
    T = np.asarray(T, float)
    z = 0.25 + 0.5j * T
    return np.imag(sp_loggamma(z)) - 0.5 * T * LOG_PI


def s_band_direct(T, us, ws, a, taper="fejer"):
    """S_x(T), DIRECT sine implementation -- verbatim port of
    signpos_probe.py lines 508-522 (fejer taper 1 - u/2a)."""
    T = np.asarray(T, float)[:, None]
    if len(us) == 0:
        return np.zeros(T.shape[0])
    tp = 1.0 - us / (2.0 * a) if taper == "fejer" else np.ones_like(us)
    coef = ws / us * tp
    return -(1.0 / math.pi) * (coef[None, :]
                               * np.sin(T * us[None, :])).sum(1)


def s_band_ampphase(T, us, ws, a, taper="fejer"):
    """INDEPENDENT amplitude-phase form: Im[(1/pi) sum beta_n
    e^{-iT u_n}], beta_n = Lambda(n) n^{-1/2}/log n * taper."""
    T = np.asarray(T, float)[:, None]
    tp = 1.0 - us / (2.0 * a) if taper == "fejer" else np.ones_like(us)
    beta = ws / us * tp
    z = (beta[None, :] * np.exp(-1j * T * us[None, :])).sum(1)
    return np.imag(z) / math.pi


# ============================================== target-namespace tools
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def target_counts(gam: np.ndarray, om: np.ndarray) -> np.ndarray:
    """N_true(om_k) = #{gamma < om_k} from the READ-ONLY cache."""
    return np.searchsorted(gam, om).astype(int)


def target_nearest_dist(gam: np.ndarray, om: np.ndarray) -> np.ndarray:
    """min_i |gamma_i - om_k| (cache side, census annotation only)."""
    idx = np.clip(np.searchsorted(gam, om), 1, len(gam) - 1)
    return np.minimum(np.abs(gam[idx] - om), np.abs(gam[idx - 1] - om))


def target_theta_prime(t: np.ndarray) -> np.ndarray:
    z = 0.25 + 0.5j * np.abs(np.asarray(t, float))
    return 0.5 * np.real(sp_digamma(z)) - 0.5 * LOG_PI


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import) else [node.module or ""])
            for m in mods:
                if m.startswith("verification") or "probe" in m:
                    bad.append("import " + m)
        if isinstance(node, ast.Attribute) and node.attr.lower() in {
                "zetazero", "zetazeros", "nzeros", "siegelz", "siegeltheta"}:
            bad.append("attr " + node.attr)
        if isinstance(node, ast.Call):
            fn = node.func
            nm = (fn.id if isinstance(fn, ast.Name)
                  else fn.attr if isinstance(fn, ast.Attribute) else "")
            if nm.lower() in {"zetazero", "zetazeros", "nzeros"}:
                bad.append("call " + nm)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        ok = node.name.startswith(("ward_", "target_")) or node.name == "main"
        for ch in ast.walk(node):
            if isinstance(ch, ast.Name) and ch.id == "CACHE_N7000" and not ok:
                bad.append("cache in " + node.name)
    return not bad, "violations: %s" % (bad or "none")


# ============================================================ rung build
def build_rung(x: int, gam: np.ndarray) -> dict:
    """All per-rung source data + cache counts (target side annotated)."""
    a = 0.5 * math.log(x)
    K = int(math.ceil(KFAC * x * math.log(x)))
    om = np.arange(K) * math.pi / a
    ns_v, us, ws = prime_power_atoms(x)
    th = theta_arch(om)
    dens = th / math.pi + 1.0
    sx = s_band_direct(om, us, ws, a, "fejer")
    sx_sharp = s_band_direct(om, us, ws, a, "sharp")
    nsrc = dens + sx
    nt = target_counts(gam, om)
    eps = nsrc - nt
    eps[0] = 0.0
    marg = 0.5 - np.abs(eps)
    marg[0] = 0.5
    chat = np.rint(nsrc).astype(int)
    chat[0] = 0
    viol = [k for k in range(1, K) if chat[k] != nt[k]]
    chat0 = np.rint(dens).astype(int)
    chat0[0] = 0
    p0fail = [k for k in range(1, K) if (chat0[k] - nt[k]) % 2 != 0]
    eps_sharp = dens + sx_sharp - nt
    eps_sharp[0] = 0.0
    dnear = target_nearest_dist(gam, om)
    dcnt = dnear * target_theta_prime(om) / math.pi     # counting units
    return {"x": x, "a": a, "K": K, "om": om, "nv": ns_v, "us": us,
            "ws": ws, "th": th, "dens": dens, "sx": sx,
            "sx_sharp": sx_sharp, "nsrc": nsrc, "nt": nt, "eps": eps,
            "marg": marg, "viol": viol, "p0fail": p0fail,
            "eps_sharp": eps_sharp, "dnear": dnear, "dcnt": dcnt,
            "eps0": dens - nt}


# ============================================================== pricing
def price_trivial(r: dict) -> float:
    tp = 1.0 - r["us"] / (2.0 * r["a"])
    return float(np.sum(r["ws"] / r["us"] * tp)) / math.pi


def price_blocks(r: dict, t: float) -> dict:
    """GENEROUS per-dyadic-block pricing of |S_x(t)|: partial summation
    granted at constant 1, prime support granted the FULL unweighted
    saving (no Vaughan loss).  Phase f(v) = (t/2pi) log v:
    f''(v) = -t/(2pi v^2), f'''(v) = t/(pi v^3)."""
    x = r["x"]
    out = {"triv": 0.0, "vdc2": 0.0, "vdc3": 0.0, "ep": 0.0}
    lo = 2.0
    while lo <= x:
        hi = min(2.0 * lo, float(x) + 1.0)
        m = (r["nv"] >= lo) & (r["nv"] < hi)
        cnt = int(np.sum(m))
        if cnt:
            bmax = float(np.max(r["ws"][m] / r["us"][m]))
            N = lo
            lam2 = t / (2.0 * math.pi * N * N)
            lam3 = t / (math.pi * N ** 3)
            e_triv = float(cnt)
            e_vdc2 = N * math.sqrt(lam2) + 1.0 / math.sqrt(lam2)
            e_vdc3 = N * lam3 ** (1.0 / 6.0) + math.sqrt(N) \
                / lam3 ** (1.0 / 6.0)
            e_ep = (t / (2.0 * math.pi * N)) ** (13.0 / 84.0) \
                * N ** (55.0 / 84.0)
            out["triv"] += bmax * e_triv / math.pi
            out["vdc2"] += bmax * min(e_triv, e_vdc2) / math.pi
            out["vdc3"] += bmax * min(e_triv, e_vdc3) / math.pi
            out["ep"] += bmax * min(e_triv, e_ep) / math.pi
        lo *= 2.0
    return out


def trudgian_S(t: float) -> float:
    """[T14] |S(t)| <= 0.112 log t + 0.278 log log t + 2.510, t >= e."""
    t = max(t, math.e + 1e-9)
    return 0.112 * math.log(t) + 0.278 * math.log(math.log(t)) + 2.510


def ccm_S(t: float) -> float:
    """[CCM13] RH bound with o(1) -> 0 (most favorable reading)."""
    t = max(t, 16.0)
    return 0.25 * math.log(t) / math.log(math.log(t))


def ls_exact_constant(r: dict) -> tuple[float, float, float]:
    """EXACT large-sieve constant of the deployed configuration:
    lambda_max(H), H_{nm} = sum_{k=1}^{K-1} e^{i om_k (u_n - u_m)}
    (closed geometric form), so that rigorously
      sum_{k>=1} |A(om_k)|^2 <= lambda_max * sum_n a_n^2,
    A(t) = sum a_n e^{-i t u_n}, a_n = beta_n/pi, |S_x| <= |A|.
    Returns (lambda_max, rigorous bound, measured sum)."""
    a, us, ws, K = r["a"], r["us"], r["ws"], r["K"]
    tp = 1.0 - us / (2.0 * a)
    an = ws / us * tp / math.pi
    dl = us[:, None] - us[None, :]
    phi = math.pi * dl / a
    Km = K - 1
    num = np.exp(1j * phi) * (np.exp(1j * Km * phi) - 1.0)
    den = np.exp(1j * phi) - 1.0
    small = np.abs(phi) < 1e-9
    den = np.where(small, 1.0, den)
    H = np.where(small, float(Km), num / den)
    lam = float(np.max(np.linalg.eigvalsh(
        0.5 * (H + H.conj().T))).real)
    bound = lam * float(np.sum(an ** 2))
    z = (an[None, :] * np.exp(-1j * r["om"][1:, None]
                              * us[None, :])).sum(1)
    meas = float(np.sum(np.abs(z) ** 2))
    return lam, bound, meas


# ================================================= heuristic variance
def model_sigma(r: dict) -> np.ndarray:
    """DECLARED HEURISTIC (typed, never gated): random-phase variance
    of eps(t) with resolved cutoff n <= t; see frozen spec."""
    us, ws, nv, a = r["us"], r["ws"], r["nv"], r["a"]
    b = ws / us
    tapdef = b * (us / (2.0 * a))          # (taper-1) piece, n <= x
    beta = b * (1.0 - us / (2.0 * a))
    om = r["om"]
    out = np.zeros(len(om))
    for i, t in enumerate(om):
        res = nv <= max(t, 2.0)
        v = (np.sum(tapdef[res] ** 2) + np.sum(beta[~res] ** 2))
        out[i] = math.sqrt(v / (2.0 * math.pi ** 2))
    return out


def star_discrepancy(u: np.ndarray) -> float:
    u = np.sort(np.mod(u, 1.0))
    n = len(u)
    i = np.arange(1, n + 1)
    return float(max(np.max(i / n - u), np.max(u - (i - 1) / n)))


# ------------------------------------------------------------- tau screen
def tau_screen_points(r: dict, ks: list[int]) -> float:
    """mp dps-40 recompute of margin at the given lattice points;
    returns max |f64 - mp| deviation."""
    dev = 0.0
    with mp.workdps(MP_DPS):
        aa = mp.log(r["x"]) / 2
        for k in ks:
            T = mp.mpf(k) * mp.pi / aa
            th = mp.im(mp.loggamma(mp.mpf(1) / 4 + T / 2 * 1j)) \
                - T / 2 * mp.log(mp.pi)
            s = mp.mpf(0)
            for n_v, u, w in zip(r["nv"], r["us"], r["ws"]):
                uu = mp.log(int(round(n_v)))
                tpv = 1 - uu / (2 * aa)
                s -= (mp.mpf(w) / uu * tpv * mp.sin(T * uu))
            s = s / mp.pi
            nsrc = th / mp.pi + 1 + s
            m = mp.mpf(1) / 2 - abs(nsrc - int(r["nt"][k]))
            dev = max(dev, abs(float(m) - float(r["marg"][k])))
    return dev


# ---------------------------------------------------------------- main
def main() -> int:
    global LADDER, TV_OVS
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    if args.smoke:
        LADDER = (3, 5, 8, 13, 21)
        TV_OVS = 2

    print("=" * 78)
    print("sp_expsum_pricing_probe  (SP) ROUNDING MARGIN vs CLASSICAL"
          " EXP-SUM TECHNOLOGY")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if args.smoke else ""))
    print("=" * 78)

    # ------------------------------------------------ I. instrument wards
    section("I. INSTRUMENT WARDS")
    fw_ok, fw_det = firewall_audit()
    check("G01 AST firewall (no zero oracle, no probe imports; cache"
          " only in ward_/target_/main)", fw_ok, fw_det)
    gam = ward_cache()
    gtop = float(gam[-1])
    check("G02 ordinate cache health (READ-ONLY, target namespace)",
          len(gam) == 7000 and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e top %.3f"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT), gtop))
    g3_ok = True
    g3_miss = []
    for rel, s in WARD_STRINGS:
        p = os.path.join(ROOT, rel)
        try:
            txt = open(p, encoding="utf-8").read()
        except OSError:
            txt = ""
        if s not in txt:
            g3_ok = False
            g3_miss.append((rel, s[:30]))
    check("G03 corpus quantifier wards: the 7 exact strings present in"
          " v848/v849/tp_opus/kill_atlas/signpos", g3_ok,
          "missing: %s" % (g3_miss or "none"))

    # build all admitted rungs
    rungs: dict[int, dict] = {}
    admitted, skipped = [], []
    for xv in LADDER:
        a = 0.5 * math.log(xv)
        K = int(math.ceil(KFAC * xv * math.log(xv)))
        om_top = (K - 1) * math.pi / a
        if om_top <= gtop - COVER_MARGIN:
            rungs[xv] = build_rung(xv, gam)
            admitted.append(xv)
        else:
            skipped.append((xv, om_top))
    print("  admitted rungs %s" % admitted)
    if skipped:
        print("  skipped (cache coverage): %s vs top %.1f"
              % (["x=%d om_top=%.1f" % s for s in skipped], gtop))

    # round-88 reproduction ward
    r88_ok = True
    det = []
    for xv in R88_RUNGS:
        r = rungs[xv]
        mm = float(np.min(r["marg"][1:]))
        ok_m = abs(mm - R88_MINMARG[xv]) <= R88_TOL
        ok_p = tuple(r["p0fail"]) == R88_P0FAIL[xv]
        r88_ok &= ok_m and ok_p
        det.append("x=%d mm=%.4f(ref %.4f) P0=%s(ref %s)"
                   % (xv, mm, R88_MINMARG[xv], r["p0fail"],
                      list(R88_P0FAIL[xv])))
        for (xr, kr), (e0, ef) in R88_EPS.items():
            if xr != xv:
                continue
            d0 = abs(float(r["eps0"][kr]) - e0)
            df = abs(float(r["eps"][kr]) - ef)
            r88_ok &= d0 <= R88_EPS_TOL and df <= R88_EPS_TOL
    check("G04 round-88 reproduction: frozen min margins, P0-failure"
          " sets and the four repaired eps pairs", r88_ok,
          "; ".join(det))

    # representation identity
    dev_r = 0.0
    for xv in admitted:
        r = rungs[xv]
        alt = s_band_ampphase(r["om"], r["us"], r["ws"], r["a"], "fejer")
        dev_r = max(dev_r, float(np.max(np.abs(alt - r["sx"]))))
    check("G05 exponential-sum normal form == direct sine"
          " implementation (all rungs, all lattice points)",
          dev_r <= REPR_BAR, "max dev %.2e (bar %.0e)" % (dev_r, REPR_BAR))

    # ------------------------------------------------ II. S1 the object
    section("II. S1 -- THE EXACT OBJECT AND ITS ANALYTIC PROFILE\n"
            "     S_x(T) = Im[(1/pi) sum_{n=p^m<=x} beta_n e^{-iT log n}],"
            "\n     beta_n = Lambda(n) n^{-1/2} (log n)^{-1}"
            " (1 - log n/log x)")
    print("  %5s %4s %6s %7s %8s %9s %9s %9s %10s"
          % ("x", "K", "atoms", "u_max", "2a", "l1=Btriv", "sig_mod",
             "sig_meas", "TV[0,top]"))
    band_ok = True
    triv = {}
    for xv in admitted:
        r = rungs[xv]
        umax = float(r["us"][-1])
        band_ok &= umax <= 2.0 * r["a"] + 1e-15
        b_tr = price_trivial(r)
        triv[xv] = b_tr
        tp = 1.0 - r["us"] / (2.0 * r["a"])
        beta = r["ws"] / r["us"] * tp
        sig_mod = math.sqrt(float(np.sum(beta ** 2))
                            / (2.0 * math.pi ** 2))
        sig_me = float(np.std(r["sx"][1:]))
        # total variation over the band (declared TV grid)
        ttop = float(r["om"][-1])
        npts = max(2000, int(ttop * 2.0 * r["a"] * TV_OVS / math.pi))
        tv = 0.0
        chunk = 200000
        coefs = r["ws"] * tp
        tgrid = np.linspace(0.0, ttop, npts)
        for i0 in range(0, npts, chunk):
            tt = tgrid[i0:i0 + chunk][:, None]
            sp = -(coefs[None, :] * np.cos(tt * r["us"][None, :])
                   ).sum(1) / math.pi
            tv += float(np.sum(np.abs(sp))) * (ttop / (npts - 1))
        print("  %5d %4d %6d %7.3f %8.3f %9.4f %9.4f %9.4f %10.2f"
              % (xv, r["K"], len(r["us"]), umax, 2.0 * r["a"], b_tr,
                 sig_mod, sig_me, tv), flush=True)
    cross = None
    for xv in admitted:
        if triv[xv] > NEED:
            cross = xv
            break
    check("G06 band limit exact (u_max <= 2a on every rung) AND the"
          " trivial l1 bound crosses the half-integer budget on the"
          " ladder at x* <= %d" % TRIV_CROSS_MAX,
          band_ok and cross is not None and cross <= TRIV_CROSS_MAX
          and triv[admitted[-1]] > NEED,
          "crossing x* = %s; B_triv(x_max=%d) = %.3f > %.1f"
          % (cross, admitted[-1], triv[admitted[-1]], NEED))

    # ------------------------------------------------ III. S2 pricing
    section("III. S2 -- PRICING THE CLASSICAL ARSENAL AGAINST THE"
            " HALF-INTEGER BUDGET\n     need: pointwise"
            " |S_x - S|(om_k) < 1/2 at every lattice point of a rung;\n"
            "     all technology values GENEROUS (constant 1, no"
            " Vaughan/partial-summation loss)")
    print("  %5s %9s | %8s %8s %8s %8s | %9s %9s"
          % ("x", "t_top", "triv", "vdC2", "vdC3", "ep13/84",
             "TrudgS", "CCM(RH)"))
    price_ok = True
    price_rows = {}
    for xv in admitted:
        r = rungs[xv]
        ttop = float(r["om"][-1])
        pb = price_blocks(r, ttop)
        tS = trudgian_S(ttop)
        cS = ccm_S(ttop)
        price_rows[xv] = (pb, tS, cS, ttop)
        if xv >= PRICE_MIN_X:
            price_ok &= (triv[xv] > NEED or xv < cross) \
                and pb["vdc2"] > NEED and pb["vdc3"] > NEED \
                and pb["ep"] > NEED and tS > NEED
        print("  %5d %9.1f | %8.3f %8.3f %8.3f %8.3f | %9.3f %9.3f"
              % (xv, ttop, pb["triv"], pb["vdc2"], pb["vdc3"],
                 pb["ep"], tS, cS))
    xm = admitted[-1]
    pbm, tSm, cSm, ttopm = price_rows[xm]
    gap_min = min(pbm["vdc2"], pbm["vdc3"], pbm["ep"], tSm) / NEED
    check("G09 unconditional pointwise pricing: every technology value"
          " at band top exceeds the 1/2 budget on every rung x >= %d"
          % PRICE_MIN_X, price_ok,
          "deepest rung x=%d: vdC2 %.2f vdC3 %.2f ep %.2f TrudgianS"
          " %.2f vs need %.1f -> min gap x%.1f"
          % (xm, pbm["vdc2"], pbm["vdc3"], pbm["ep"], tSm, NEED,
             gap_min))
    print("""
  PRICING TABLE (technology -> what it CAN give here -> gap to need):
   (a) trivial l1                 |S_x| <= %.3f at x=%d (crossing x*=%s)
                                  -> grows ~ 2 sqrt(x)/(pi log x); EMPTY
                                     beyond x* and bounds the WRONG side
                                     (need |S_x - S|, S unbounded [Ts86]).
   (b) van der Corput [GK91]      2nd/3rd-derivative tests on f(v) =
       Thm 2.2/2.6                (t/2pi) log v: f'' = -t/(2pi v^2);
                                  generous composite %.2f / %.2f at the
                                  deepest rung -- O(1)-scale per block,
                                  ~log x blocks: the route reproduces
                                  S = O(log t), never o(1); gap x%.1f.
   (c) Vaughan+Vinogradov [V77]   ceiling = argument-principle bound
       + subconvexity [B17]       S(t) = O(log t); sharpest explicit
       explicit [T14]             form 0.112 log t + 0.278 loglog t
                                  + 2.510 = %.2f at t_top=%.0f; Bourgain
                                  13/84 improves ZETA growth, not the
                                  S ceiling; gap x%.1f.  Exponent pair
                                  (13/84,55/84) composite %.2f.
   (d) large sieve [MV74]         EXACT per-rung constant computed in
       mean values [S46][G87]     section IV below: controls the lattice
                                  l2 of S_x RIGOROUSLY, i.e. the census
                                  of LARGE |S_x|; for eps = S_x - S it
                                  needs (L-a) a mean value in the
                                  deployed regime x ~= t/7.85 (published
                                  regimes: cutoff a small power of t
                                  [S46]; x ~ t is pair-correlation
                                  territory [G87]) and (L-b) an
                                  integral->lattice transfer past the
                                  jumps of S ([PP37] needs band-limited;
                                  eps is not) -- the transfer at the
                                  lattice IS ordinate repulsion, i.e.
                                  (SP)'s own content: typed CIRCULARITY.
   (e) conditional ladder         Lindelof: S = o(log t), no constant
       [L24][CCM13][M77]          [L24]; density hyp: nothing pointwise
                                  below o(log t); RH: (1/4+o(1)) log t/
                                  loglog t = %.2f at t_top (o(1)->0) --
                                  STILL > 1/2 everywhere in range, and
                                  RH makes S = Omega_pm(sqrt(log t/
                                  loglog t)) [M77]: no magnitude route
                                  reaches (SP) even under RH.  (SP)
                                  does NOT follow from Lindelof, the
                                  density hypothesis, or RH by any
                                  priced technology: it sits ABOVE the
                                  conditional magnitude ladder, at
                                  TPL(i) itself (corpus, CCCLXXXVII).
""" % (triv[xm], xm, cross, pbm["vdc2"], pbm["vdc3"],
       min(pbm["vdc2"], pbm["vdc3"]) / NEED, tSm, ttopm, tSm / NEED,
       pbm["ep"], cSm))

    # ------------------------------------ IV. large sieve, exact constant
    section("IV. S2d -- THE LARGE SIEVE PRICED EXACTLY, AND THE CHAIN'S"
            " QUANTIFIER ANSWER")
    ls_ok = True
    print("  %5s %9s %11s %11s %8s %10s %8s"
          % ("x", "K-1", "lam_max(H)", "MV-heur", "sumSx2", "LSbound",
             "#|Sx|>.5"))
    for xv in admitted:
        r = rungs[xv]
        lam, bound, meas = ls_exact_constant(r)
        mv_h = (r["K"] - 1) * 1.0 + 2.0 * r["a"] * r["a"] / math.pi
        nbig = int(np.sum(np.abs(r["sx"][1:]) >= NEED))
        cens = bound / NEED ** 2
        ls_ok &= meas <= bound * (1.0 + 1e-9) and nbig <= cens
        print("  %5d %9d %11.1f %11.1f %8.3f %10.3f %8d (cens bar %.1f)"
              % (xv, r["K"] - 1, lam, mv_h, meas, bound, nbig, cens))
    check("G10 large-sieve wards: sum_k |A(om_k)|^2 <= lambda_max *"
          " sum a_n^2 AND #{|S_x| >= 1/2} <= LS census bound, every"
          " rung (both are theorems; numeric verification)", ls_ok,
          "the LS controls the FINITE SUM's lattice l2 rigorously;"
          " eps needs (L-a)+(L-b) above")
    print("""
  THE QUANTIFIER ANSWER (extracted verbatim, warded by G03):
  (Q1) RUNG LEVEL -- v848 STEP 2: hypothesis (H) is consumed along ONE
       ladder cofinal in the mesh order; 'a cofinal set meets every
       tail'.  v849 kernel-checks the hierarchy uniform SUBSET-NEQ
       pointwise SUBSET-NEQ cofinal ('cofinal_not_pointwise': cofinal
       positivity does not even require all-rung positivity).  So the
       chain TOLERATES an exceptional set of rungs: it needs one clean
       cofinal subfamily, nothing more.
  (Q2) PREREGISTRATION -- v849: the ladder is DATA, 'a PRE-FIXED
       strictly monotone index sequence ... never mined from measured
       signs'.  A pure existence proof of infinitely many clean rungs
       closes the mathematical hypothesis (classically the sequence
       exists as data); the corpus discipline additionally demands the
       family be NAMEABLE first -- an effective/localized exceptional
       set, not just a density-zero one.
  (Q3) WITHIN A RUNG -- tp_opus count_depth: the consumed object is the
       PREFIX depth ('the largest m such that ... for all i <= m');
       'TPL(i) is exactly the statement D(x) -> inf'.  Hence ONE bad
       lattice point does NOT kill a rung: it CAPS that rung's depth at
       its position.  'All but finitely many k per rung' SUFFICES iff
       the lowest bad position is unbounded along a predeclarable
       cofinal family; it FAILS iff bad points recur at bounded k.
  (Q4) THE DECISIVE TARGET for average technology is therefore NOT
       'zero exceptions per rung' but 'exceptions only above height
       m(x) with m(x) -> inf on a predeclared family'.  The measured
       exception-position census (section V) tests exactly this.""")

    # ------------------------------------------------ V. S3 the census
    section("V. S3 -- THE MARGIN CENSUS TO THE CACHE EDGE\n"
            "     (extension rungs: source + read-only cache only;"
            " declared)")
    print("  %5s %5s %8s %6s %7s %7s | %s | %6s %7s"
          % ("x", "K", "minMarg", "argk", "k/K", "maxE",
             "census margin<" + "/".join("%.2f" % e for e in EPS_GRID),
             "#viol", "PFX"))
    all_marg, all_frac_full, all_frac_dens = [], [], []
    census_ok = True
    viol_all = []
    small_marg = []
    pfx = {}
    minmarg = {}
    for xv in admitted:
        r = rungs[xv]
        m = r["marg"][1:]
        k_arg = int(np.argmin(m)) + 1
        mm = float(np.min(m))
        minmarg[xv] = (mm, k_arg)
        cen = [int(np.sum(m < e)) for e in EPS_GRID]
        census_ok &= all(cen[i] <= cen[i + 1]
                         for i in range(len(cen) - 1))
        v = r["viol"]
        pfx[xv] = (min(v) - 1) if v else (r["K"] - 1)
        census_ok &= pfx[xv] >= 1
        for k in v:
            viol_all.append((xv, k, k / (r["K"] - 1.0),
                             float(r["eps"][k]), float(r["dcnt"][k])))
        for k in np.nonzero(m < 0.05)[0] + 1:
            small_marg.append((xv, int(k), k / (r["K"] - 1.0),
                               float(r["marg"][k]),
                               float(r["dcnt"][k])))
        all_marg.append(m)
        all_frac_full.append(np.mod(r["nsrc"][1:], 1.0))
        all_frac_dens.append(np.mod(r["dens"][1:], 1.0))
        print("  %5d %5d %8.4f %6d %7.3f %7.3f | %s | %6d %7d"
              % (xv, r["K"], mm, k_arg, k_arg / (r["K"] - 1.0),
                 float(np.max(np.abs(r["eps"][1:]))),
                 " ".join("%5d" % c for c in cen), len(v), pfx[xv]))
    check("G07 census internal consistency: exceptional counts monotone"
          " in eps AND prefix depth >= 1 on every rung", census_ok,
          "PFX = %s" % {x: pfx[x] for x in admitted})
    if viol_all:
        print("\n  PARITY VIOLATIONS (SP-OPERATIVE channel;"
              " MEASUREMENTS, recorded):")
        print("  per-rung summary: x, #viol, density, lowest k,"
              " lowest k/K, #above tracking band k/K>0.8:")
        for xv in admitted:
            vv = [(k, rel, e, d) for (x2, k, rel, e, d) in viol_all
                  if x2 == xv]
            if not vv:
                continue
            print("    x=%4d  #%4d  dens %.4f  k_min=%5d  k/K_min="
                  "%.3f  top-band %d"
                  % (xv, len(vv), len(vv) / (rungs[xv]["K"] - 1.0),
                     min(k for k, *_ in vv),
                     min(r for _k, r, *_ in vv),
                     sum(1 for _k, r, *_ in vv if r > 0.8)))
        low = sorted([v for v in viol_all if v[2] < PREFIX_REL_BAR],
                     key=lambda v: v[2])
        print("  prefix-critical detail (k/K < %.2f, first %d of %d):"
              % (PREFIX_REL_BAR, min(20, len(low)), len(low)))
        for xv, k, rel, e, d in low[:20]:
            print("    x=%4d k=%5d k/K=%.3f eps=%+.4f"
                  " d(ordinate,lattice)=%.4f counting units"
                  % (xv, k, rel, e, d))
    else:
        print("\n  no parity violation on any admitted rung")
    # SP-LITERAL census: closest approach to an exact half-integer
    lit = []
    for xv in admitted:
        r = rungs[xv]
        am = np.abs(r["marg"][1:])
        kl = int(np.argmin(am)) + 1
        lit.append((float(am[kl - 1]), xv, kl))
    lit_min, lit_x, lit_k = min(lit)
    print("\n  SP-LITERAL census (dist to Z+1/2 = |margin|): global"
          " min %.2e at x=%d k=%d; per-rung mins %s"
          % (lit_min, lit_x, lit_k,
             ["%.0e" % v for (v, _x, _k) in lit]))
    print("\n  margins < 0.05 (position census):")
    for xv, k, rel, mg, d in small_marg[:24]:
        print("    x=%4d k=%5d k/K=%.3f margin=%.4f d_cnt=%.4f"
              % (xv, k, rel, mg, d))
    if len(small_marg) > 24:
        print("    ... (%d total)" % len(small_marg))

    # min-margin trend (positive rungs only; violation rungs excluded)
    xs = np.array([x for x in admitted
                   if x >= 8 and minmarg[x][0] > 0], float)
    ms = np.array([minmarg[int(x)][0] for x in xs])
    if len(xs) >= 3:
        sl = float(np.polyfit(np.log(xs), np.log(ms), 1)[0])
        print("\n  min-margin trend: OLS slope d log(minMarg)/d log x ="
              " %+.3f over the %d positive rungs x >= 8 (1/(2K)"
              " envelope slope ~ -1); violation rungs excluded: %s"
              % (sl, len(xs),
                 [x for x in admitted if minmarg[x][0] <= 0] or "none"))
    else:
        sl = float("nan")
        print("\n  min-margin trend: not fit (<3 positive rungs)")

    # prefix table (the Q3/Q4 object)
    print("\n  FORALL-m-EXISTS-x table: smallest admitted x with prefix"
          " depth >= m")
    for mreq in (5, 10, 20, 50, 100, 500, 1000, 3000):
        xs_ok = [x for x in admitted if pfx[x] >= mreq]
        print("    m=%5d -> x = %s" % (mreq, min(xs_ok) if xs_ok
                                       else "NONE"))

    # ordinate-distance coupling (L3 modulus, corpus claim)
    mg_all = np.concatenate(all_marg)
    dc_all = np.concatenate([rungs[x]["dcnt"][1:] for x in admitted])
    sel = mg_all < 0.25
    if np.sum(sel) >= 8:
        cc = float(np.corrcoef(mg_all[sel],
                               np.minimum(dc_all[sel], 0.75))[0, 1])
    else:
        cc = float("nan")
    print("\n  margin vs ordinate-to-lattice distance (counting units),"
          " margins < 0.25: corr = %.3f over %d points (L3 modulus:"
          " expected strongly positive)" % (cc, int(np.sum(sel))))

    # Weyl / discrepancy
    ff = np.concatenate(all_frac_full)
    fd = np.concatenate(all_frac_dens)
    dist_f = np.minimum(ff, 1.0 - ff)
    dist_d = np.minimum(fd, 1.0 - fd)
    w_full = [abs(np.mean(np.exp(2j * np.pi * m * ff)))
              for m in (1, 2, 3, 4)]
    w_dens = [abs(np.mean(np.exp(2j * np.pi * m * fd)))
              for m in (1, 2, 3, 4)]
    d_full = star_discrepancy(ff)
    d_dens = star_discrepancy(fd)
    print("\n  Weyl/discrepancy at the lattice (pooled %d points):"
          % len(ff))
    print("    FULL phase N_src mod 1: mean dist-to-Z %.4f (uniform"
          " 0.25), |W_1..4| = %s, D* = %.4f"
          % (float(np.mean(dist_f)),
             ["%.3f" % w for w in w_full], d_full))
    print("    DENSITY phase theta/pi+1 mod 1: mean dist-to-Z %.4f,"
          " |W_1..4| = %s, D* = %.4f  (near-equidistributed: the"
          " density predictor MUST fail at a positive rate; the prime"
          " comb concentrates the phase at Z)"
          % (float(np.mean(dist_d)),
             ["%.3f" % w for w in w_dens], d_dens))
    conc_alive = (float(np.mean(dist_f)) < CONC_DIST_BAR
                  and w_full[0] > CONC_W1_BAR)
    print("    TYPED concentration verdict (recorded either way,"
          " AMENDMENT in spec): %s (bars: mean dist < %.2f, |W_1| >"
          " %.2f; survival would need both)"
          % ("CONCENTRATED" if conc_alive else
             "DRIFTING-TO-EQUIDISTRIBUTION", CONC_DIST_BAR,
             CONC_W1_BAR))
    check("G08 Weyl/discrepancy instrument sane (|W_m| <= 1, D* in"
          " (0,1], both phases; concentration verdict TYPED above)",
          all(w <= 1.0 + 1e-12 for w in w_full + w_dens)
          and 0.0 < d_full <= 1.0 and 0.0 < d_dens <= 1.0,
          "mean dist full/dens %.4f/%.4f, |W_1| %.3f/%.3f, uniform"
          " ref (0.25, ~%.3f)"
          % (float(np.mean(dist_f)), float(np.mean(dist_d)),
             w_full[0], w_dens[0], 1.0 / math.sqrt(len(ff))))

    # variance model vs measurement (typed)
    print("\n  variance model vs measurement (DECLARED HEURISTIC,"
          " typed):")
    print("  %5s | %s" % ("x", "rms(eps) measured/model per height"
                          " quintile (k/K in 0-.2,...,.8-1)"))
    exp_cens = {e: 0.0 for e in EPS_GRID}
    for xv in admitted:
        r = rungs[xv]
        sg = model_sigma(r)
        e = r["eps"][1:]
        s = sg[1:]
        K = r["K"] - 1
        qs = []
        for q in range(5):
            i0, i1 = int(q * K / 5), int((q + 1) * K / 5)
            if i1 <= i0:
                qs.append("--")
                continue
            rm = float(np.sqrt(np.mean(e[i0:i1] ** 2)))
            rmm = float(np.sqrt(np.mean(s[i0:i1] ** 2)))
            qs.append("%.2f/%.2f" % (rm, rmm))
        if xv in (8, 34, 144, 610, 890, admitted[-1]):
            print("  %5d | %s" % (xv, "  ".join(qs)))
        from scipy.stats import norm as _norm
        for eb in EPS_GRID:
            z = (NEED - eb) / np.maximum(s, 1e-12)
            exp_cens[eb] += float(np.sum(2.0 * _norm.sf(z)))
    meas_cens = {e: int(np.sum(mg_all < e)) for e in EPS_GRID}
    print("  pooled exceptional census vs Gaussian-model prediction:")
    for eb in EPS_GRID:
        print("    margin < %.2f : measured %5d  model %8.1f"
              % (eb, meas_cens[eb], exp_cens[eb]))

    # THE MECHANISM: the Fejer taper's irreducible variance floor
    print("\n  THE MECHANISM (taper-deficit decomposition; exact"
          " finite sums):")
    print("  %5s %12s %10s %10s %12s" % ("x", "tapdef_var",
                                         "rms_tapdef", "rms_meas",
                                         "E[#viol] floor"))
    for xv in admitted:
        r = rungs[xv]
        b = r["ws"] / r["us"]
        vt = float(np.sum((b * r["us"] / (2.0 * r["a"])) ** 2)) \
            / (2.0 * math.pi ** 2)
        rms_t = math.sqrt(vt)
        rms_m = float(np.sqrt(np.mean(r["eps"][1:] ** 2)))
        from scipy.stats import norm as _norm2
        efloor = 2.0 * _norm2.sf(NEED / rms_t) * (r["K"] - 1)
        print("  %5d %12.5f %10.4f %10.4f %12.2f"
              % (xv, vt, rms_t, rms_m, efloor))
    print("  asymptote: sum Lambda(n)^2/(n log^2 n) (log n/log x)^2"
          " -> 1/2, so tapdef rms -> 1/(2 pi) = %.4f: an O(1)"
          " tracking floor against the 1/2 budget, independent of"
          " arithmetic -- the deployed Fejer approximant CANNOT"
          " satisfy SP-OPERATIVE at scale; the sharp taper (no"
          " deficit) fails worse by resolution error (section VI"
          " print)" % (1.0 / (2.0 * math.pi)))

    # ------------------------------------------------ VI. tau screen
    section("VI. TAU-SCREEN OF EVERY REPORTED MARGIN")
    dev_mp = 0.0
    for xv in admitted:
        ks = [minmarg[xv][1]]
        ks += [k for (x2, k, _r, _m, _d) in small_marg if x2 == xv][:4]
        ks += [k for (x2, k, _r, _e, _d) in viol_all if x2 == xv][:4]
        dev_mp = max(dev_mp, tau_screen_points(rungs[xv],
                                               sorted(set(ks))))
    check("G11a tau-screen (precision): mp dps-%d recompute of every"
          " reported min/violation margin" % MP_DPS,
          dev_mp <= TAU_MP_BAR, "max |f64 - mp| = %.2e (bar %.0e)"
          % (dev_mp, TAU_MP_BAR))
    rng = np.random.default_rng(SEED)
    jit_dev, jit_cross = 0.0, 0
    for xv in admitted:
        r = rungs[xv]
        gj = np.sort(gam + rng.uniform(-JIT_SIZE, JIT_SIZE, len(gam)))
        ntj = target_counts(gj, r["om"])
        if not np.array_equal(ntj, r["nt"]):
            jit_cross += 1
            continue
        # counts unchanged -> margins identical by construction
    check("G11b tau-screen (cache jitter +-%.0e, seed %d): counting"
          " margins invariant unless an ordinate crosses the lattice"
          % (JIT_SIZE, SEED), jit_cross == 0 and jit_dev < TAU_JIT_BAR,
          "rungs with a jitter-induced crossing: %d" % jit_cross)
    print("  taper sensitivity (typed, PRIMARY stays fejer): min margin"
          " sharp-taper per rung:")
    print("    %s" % {x: "%.4f" % float(np.min(
        0.5 - np.abs(rungs[x]["eps_sharp"][1:]))) for x in admitted})

    # ------------------------------------------------------- verdict
    section("VII. VERDICT")
    wall = time.time() - T0_WALL
    check("G12 runtime", wall <= RUNTIME_BAR, "%.1f s (bar %.0f)"
          % (wall, RUNTIME_BAR))
    npass = sum(1 for _n, o, _d in CHECKS if o)
    ok_all = npass == len(CHECKS)
    # composite verdict pieces
    if viol_all:
        excep = [(x, k, rel) for (x, k, rel, _e, _d) in viol_all]
    else:
        excep = [(x, k, rel) for (x, k, rel, _m, _d) in small_marg]
    min_rel = min((rel for (_x, _k, rel) in excep), default=1.0)
    prefix_open = min_rel >= PREFIX_REL_BAR
    if viol_all:
        first_v = viol_all[0]
        v_op = ("SP-OPERATIVE-FALSIFIED(deployed Fejer S_x: first"
                " counterexample x=%d k=%d eps=%+.3f; %d points over"
                " %d rungs, density ~%.3f at x=%d, stationary;"
                " mechanism = taper variance floor rms -> 1/(2pi))"
                % (first_v[0], first_v[1], first_v[3], len(viol_all),
                   sum(1 for x in admitted if rungs[x]["viol"]),
                   len(rungs[admitted[-1]]["viol"])
                   / (rungs[admitted[-1]]["K"] - 1.0), admitted[-1]))
        v_avg = ("SP-PREFIX-DEAD-IN-WINDOW(deployed S_x: PFX stalls"
                 " at max %d, lowest violation k/K = %.3f < bar %.2f;"
                 " an average/prefix salvage needs a SHARPER"
                 " approximant, not more rungs)"
                 % (max(pfx.values()), min_rel, PREFIX_REL_BAR))
    else:
        v_op = "SP-OPERATIVE-ALIVE-IN-RANGE"
        v_avg = ("SP-AVERAGE-ROUTE-OPEN(exceptions confined to k/K >="
                 " %.2f >= bar %.2f; remaining: (L-a) mean value at"
                 " cutoff x ~= t/7.85, (L-b) lattice transfer past the"
                 " S-jumps)" % (min_rel, PREFIX_REL_BAR)
                 if prefix_open else
                 "SP-PREFIX-THREATENED(lowest exception at k/K = %.3f"
                 " < bar %.2f)" % (min_rel, PREFIX_REL_BAR))
    v_lit = ("SP-LITERAL-NONVANISHING-IN-RANGE(min dist to Z+1/2 ="
             " %.1e at x=%d k=%d; shrinking, no content without a"
             " repulsion law)" % (lit_min, lit_x, lit_k))
    mm_all = min(minmarg[x][0] for x in admitted)
    print("""
DELIVERABLE:
  D1  The exact object (S1): ONE finite exponential sum over prime
      powers, beta_n = Lambda(n) n^{-1/2}/log n * Fejer taper,
      frequencies log n <= 2a: band-limited, l1 ~ 2 sqrt(x)/(pi log x)
      (crossing the 1/2 budget at x* = %s), value scale at the lattice
      = sqrt(sum beta^2/2)/pi (measured above).
  D2  The pricing (S2): every unconditional pointwise technology --
      trivial, vdC 2nd/3rd derivative [GK91], Vaughan+Vinogradov
      ceiling with explicit constants [T14], exponent pair 13/84 [B17]
      -- exceeds the half-integer budget at every priced rung (G09,
      min gap x%.1f at the deepest rung); the conditional ladder
      (Lindelof, density, RH [L24][CCM13]) stays above 1/2 too, and
      RH even forces S = Omega_pm [M77]: (SP) is NOT a magnitude
      statement and no magnitude route -- unconditional or RH-grade --
      reaches it.  The large sieve DOES control the finite sum's
      lattice l2 exactly (G10); for eps = S_x - S it leaves exactly
      (L-a) + (L-b), and (L-b) at the lattice IS ordinate repulsion:
      typed CIRCULARITY.
  D3  The quantifier answer (S2d): rung-exceptions TOLERATED (cofinal
      consumption, v848/v849, kernel-checked); within a rung one bad
      point only CAPS the prefix depth (tp_opus count_depth); the
      average route survives iff exceptions sit at unboundedly growing
      positions on a predeclarable family -- measured above.
  D4  The census (S3): the round-88 exactness is a SMALL-x accident
      of the margin budget -- the operative (SP) fails from x = 21 on
      (tau-screened counterexamples, positions and densities above);
      the mechanism is the Fejer taper's variance floor rms ->
      1/(2pi), an O(1) obstruction independent of arithmetic; the
      literal non-vanishing survives trivially and carries no
      extraction content without a repulsion law.  The TRUTH side
      (eigenvector positions, TPL(i) proper) is NOT re-measured
      beyond x = 13 here and stays open: what died is the deployed
      source-only APPROXIMANT, and any successor needs pointwise
      tracking error < 1/2 at ~x log x lattice points -- exactly the
      budget no priced technology reaches.

NO RH CLAIM.  EXPLORATION ONLY.""" % (cross, gap_min))
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (npass, len(CHECKS), wall, SPEC_SHA[:16]))
    print("VERDICT: %s\n  + SP-PRICED(7 technologies, table above)"
          "\n  + SP-CLASSICALLY-OUT-OF-REACH(pointwise; min"
          " unconditional gap x%.1f at x=%d, t_top=%.0f; and the"
          " budget itself is measured EXCEEDED: |S_x - S| > 1/2 at"
          " positive density)\n  + SP-CONDITIONAL-LADDER(Lindelof/"
          "density/RH all > 1/2 pointwise; RH-CCM %.2f; (SP) above"
          " the whole magnitude ladder)\n  + %s\n  + %s"
          % (v_op, gap_min, xm, ttopm, cSm, v_avg, v_lit))
    print("tau-screened global min margin %.4f (mp dev %.1e);"
          " min-margin trend %s"
          % (mm_all, dev_mp,
             ("slope %+.3f" % sl) if sl == sl else
             "not fit (violations from x = 21 on)"))
    if args.smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("=" * 78)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
