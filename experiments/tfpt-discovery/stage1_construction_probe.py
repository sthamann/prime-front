#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""stage1_construction_probe -- PRIME.STAGE1.CONSTRUCTION.01: the first
actual CONSTRUCTION attempt at the Stage-1 substrate, adjudicated
against the corpus's frozen acceptance gates.

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  NO RH CLAIM.  This probe
proves nothing about RH in any direction.  It STOPS PRICING AND BUILDS:
two candidate arithmetic hosts are constructed as far as they go and
executed against the frozen Stage-1 acceptance gates of the published
roadmap (roadmap_probe.py, PRIME.ROADMAP.01, milestones M1a/M1b).  The
expected outcome is failure at named steps; the deliverable is the
exact breakage points WITH NUMBERS and the sharpened Stage-1
requirement.  A failed construction is not progress on RH; it is a
measurement of what the missing mathematics must supply.

===========================================================================
THE FROZEN ACCEPTANCE GATES (from roadmap_probe / cohomspec_probe)
===========================================================================
G1  (AC)/Euler--Pick interface: the candidate's trace/pairing evaluated
    on exponential autocorrelations f_c(v)=1_{v>=0} sum_j c_j e^{-sigma_j v}
    must equal the P_N entries -- equivalently the pins
    P(sigma)=xi'/xi(1/2+sigma) at the 16 frozen sigma of the SVPIN spec
    -- with the certified floors (N<=4) as acceptance values:
      N=1: [4.5917135e-2, 4.5917136e-2]  N=2: [9.0288701e-6, 9.0289075e-6]
      N=3: [2.3643695e-10, 1.1497752e-9] N=4: [8.278338e-15, 1.3840906e-14]
    (owning artifacts eulerpick_ladder_frozen.log / sieve4_run1.log).
G2  Source-only in input AND not zero-measure-in-content: the Z1 screen
    (readout == cache partial sums at rel <= 1e-6 fires TRANSCRIPTION;
    the Krein carrier, which RESUMS the tail, is the content benchmark;
    owning artifact krein_screw_realization_probe.py K5b/K5c).
G3  STRUCTURAL positivity (unitarity/state property/intersection form),
    not assumed and not assembled from post-hoc cancellation.
G4  Correct control deaths: the smooth (prime-free PNT) and
    weight-scrambled worlds must break at the measured depths
    r=0.264 / r=0.744 (Schur currency) and must miss the certified
    floors (pin currency); owning artifacts vbk_invariant_probe.py,
    cohomspec_probe.py (FROZEN_SMOOTH_EXIT = 0.264,
    FROZEN_SCRAM_EXIT = 0.744).
G5  The round-113 duality row: if the candidate has a generator Theta,
    self-duality Theta + Theta* = I forces Re = 1/2 on its spectrum.
    (Quoted from the round-113 architecture verdict of the radius4
    lane.  NOT grep-warded here: the radius4_* namespace is under a
    concurrent lane; the row is implemented as MATHEMATICS below --
    finite skew gates -- instead of as a file ward.)

===========================================================================
CANDIDATE A -- THE BOST--CONNES / SCALING-SITE SQUARE (operator side)
===========================================================================
The BC Hamiltonian H eps_n = log(n) eps_n on l^2(N_{>=2}) has
Tr(e^{-beta H}) = zeta(beta) for beta > 1 (partition function; Bost--
Connes 1995).  With the weight operator W eps_n = Lambda(n) n^{-1/2}
eps_n the prime side of EVERY corpus pin is a literal trace identity:
    Tr(W e^{-sigma H}) = sum_n Lambda(n) n^{-(1/2+sigma)}
                       = -zeta'/zeta(1/2+sigma)      (sigma > 1/2),
and evaluated on the exponential autocorrelation A_c it is
    Tr(W A_c(H)) = int_0^infty Tr(W f_c(H+t) f_c(t)) dt,
the flow-smeared trace.  The candidate host is the DIRECT SUM
    H_cand = l^2(N_{>=2})  (+)  H_arch,
where H_arch carries the archimedean/pole data (Connes--Consani's
archimedean prolate positivity, arXiv:2006.13771, covers exactly the
archimedean place), with generator Theta_A = 1/2 + i(H_BC (+) H_arch)
and total trace = BC prime trace + archimedean germ + pole terms.
MEASURED HERE: the trace identity weld (finite truncation N = 4e7 +
declared PNT tail model vs the Euler--Maclaurin continuation), the
floors, the Z1 screen, the Theta gates, the spectral-content counting
law, the PIECE DECOMPOSITION of the Pick matrices (pole/Gamma/prime),
and the corpus-currency Schur image of the archimedean window (the
arch-only lag row vs the true row; first prime at log 2).

===========================================================================
CANDIDATE B -- THE FOLIATED SUSPENSION HOST (geometric side)
===========================================================================
The Alvarez Lopez--Kordyukov trace formula (arXiv:2402.06671) is proved
for smooth foliated flows.  The cheap host: a disjoint union of circles
of circumference l_p = log p (one per prime), flow = rotation; the m-th
return of circle p contributes at u = m log p.  THE WEIGHT DICTIONARY
(the transverse fixed-point datum), three rows, all measured:
  ANOSOV    w = log p / |det(I - P^m)| = log p/(p^m - 1)   [natural]
  SELBERG   w = log p / (2 sinh(m log p / 2))              [hyperbolic]
  HALF-FORM w = log p * p^{-m/2} = log p |det(I-P^m)|^{-1/2}-normalised
                                                           [required]
with the exact conversion  required = natural * 2 sinh(m l_p / 2)  and
required = selberg * (1 - p^{-m}).  The archimedean completion (what
the cheap union lacks): Deninger's expected log-flow at the archimedean
place enters as ONE degenerate orbit whose regularised trace is the
Gauss-integral germ
    psi(s/2)/2 = int_0^infty (e^{-2u}/(2u) - e^{-su}/(1-e^{-2u})) du,
plus the two classical fixed points (weights 1 and e^u) giving
1/s + 1/(s-1), plus the place constant -log(pi)/2.  MEASURED HERE: the
germ quadrature identities, the assembled pins at the 16 frozen sigma,
the certified floors, the kill distance of the ANOSOV and SELBERG rows
(in certified-interval widths), the pinning windows that the certified
floors impose on the half-density exponent theta (weights n^{-theta})
and on the regularisation constant delta_c, and the G5 twist link: the
flow generator theta + d/du satisfies Theta + Theta* = I iff
theta = 1/2 -- the SAME datum as the weight twist.

===========================================================================
DECLARED CIRCULARITY BOUNDARY (honesty)
===========================================================================
Both candidates assemble the classical explicit formula; at pin level a
"supplied-weight" candidate reproduces P(sigma) BY CONSTRUCTION.  The
non-circular numerical content is exactly: (a) the truncated-trace vs
Euler--Maclaurin weld across the identity (independent computations:
own sieve vs own continuation), (b) the germ quadratures vs the
digamma/pole closed forms, (c) the frozen certified floors as external
anchors, (d) the kill distances of the non-supplied weight rows and the
control worlds, (e) the pinning windows.  G1 "PASS" for a
supplied-weight candidate therefore NEVER counts as content: it is
typed PASS-TRANSCRIBING and the Z1 screen (G2) fires on it.

===========================================================================
DECLARED NUMERICS / SUBSAMPLING
===========================================================================
Sieve cap NSIEVE = 4e7 (primes ~ 2.43e6); PNT tail model
int_N^inf x^{-s} dx = N^{1-s}/(s-1) DECLARED (instrument calibration,
not content); truncation weld barred at rel 1e-6 only for s >= 1.5,
report-only below (s = 1.1/1.25/1.4 carry the measured near-critical
truncation cost).  Euler--Maclaurin: cutoff 96 / 28 Bernoulli terms at
100 dps (stability gate vs 128/32 at 1e-70).  Pick floors at 100 dps
(mp.eigsy).  Det-tower truncation K = 120 with declared tail
< 3*2^{-(sigma+121)}.  Germ quadratures at 30 dps with u < 1e-8 series
guard.  Corpus Schur rows: delta = 0.006, n = 428 lags (L = 2.568),
100 dps -- ported verbatim from cohomspec_probe.py (owning artifact).
theta/delta_c windows: central differences at eps = 1e-20, linearised
per-rung windows (hi-lo)/|dlam/d.|, 3x-overshoot direct confirmations;
the BINDING window is the MINIMUM over rungs N = 1..4 -- monotone
tightening along the ladder is NOT assumed (the sensitivity dlam/d. can
collapse with the floor when the ground eigenvector decouples from the
perturbation direction; whichever rung binds is a measurement).  Frozen test vector
c = (1, 1/2, -1/3, 1/5) at sigma = (2, 3/2, 4/3, 5/4); frozen (AC)
value 8.581810362e-2 (cohomspec_probe).  16 frozen sigma:
(0.6, 0.75, 0.9, 1.125, 8/7, 7/6, 1.2, 1.25, 4/3, 1.5, 2, 3, 4, 6, 8,
12).  Pin nodes sigma_j = 1 + 1/j.  Runtime bar 900 s.  No randomness.

===========================================================================
BREAKAGE REGISTER (frozen names; every fired row carries a number)
===========================================================================
BRK-A1-CROSSTERMS      direct-sum glue supplies ZERO of the measured
                       cancellation digits positivity needs at N=4.
BRK-A2-Z1TRANSCRIPTION the BC prime trace readout IS the partial sum.
BRK-A3-SPECTRUMCOUNT   BC spectrum counts e^T vs zeros (T/2pi)log(T/2pi).
BRK-B1-HALFDENSITY     natural (Anosov) and Selberg transverse weights
                       miss the certified floors by measured widths;
                       the certified ladder pins theta to a window.
BRK-B2-ARCHGERM        the archimedean germ glues ANALYTICALLY
                       (quadrature-verified) but counterterm + place
                       constant are SUPPLIED; delta_c pinned to a window.
BRK-COMMON-FORCING     nothing in either candidate FORCES theta = 1/2,
                       the counterterm, or the cross-term state.

VERDICT ENUM (frozen, exactly one):
  STAGE1-GLUED(!!)               some candidate passes G1-G5 wholesale;
  STAGE1-BREAKAGE-LOCATED(...)   all instruments pass, breakage rows
                                 fire as typed, windows measured;
  STAGE1-UNBUILDABLE(why)        a construction step cannot even be
                                 stated/computed at the declared bars;
  STAGE1-INSTRUMENT-EDGE         a ward/instrument fails (exit 1, not
                                 a mathematical verdict).

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
    "roadmap": "experiments/tfpt-discovery/roadmap_probe.py",
    "vbk": "experiments/tfpt-discovery/vbk_invariant_probe.py",
}

# ---------------------------------------------------------------- frozen
SIGMAS16 = (0.6, 0.75, 0.9, 1.125, 8.0 / 7.0, 7.0 / 6.0, 1.2, 1.25,
            4.0 / 3.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0)
PIN_COUNT = 12
CERTIFIED = {
    1: (4.5917135e-2, 4.5917136e-2),
    2: (9.0288701e-6, 9.0289075e-6),
    3: (2.3643695e-10, 1.1497752e-9),
    4: (8.278338e-15, 1.3840906e-14),
}
AC_COEFFS = (1.0, 0.5, -1.0 / 3.0, 0.2)
AC_SIGMAS = (2.0, 1.5, 4.0 / 3.0, 1.25)
FROZEN_AC_LHS = 8.581810362e-2
FROZEN_SMOOTH_EXIT = 0.264
FROZEN_SCRAM_EXIT = 0.744
FROZEN_TRUE_MAX_ALPHA = 0.183932
FROZEN_WEIGHT_BEFORE = 0.49012907
FROZEN_WEIGHT_AFTER = 0.71138896
Z1_BAR = 1e-6

NSIEVE = 40_000_000
DPS = 100
DPS_TOWER = 60
DPS_QUAD = 30
TOWER_K = 120
DELTA_TEXT = "0.006"
DELTA = 0.006
L_ROW = 2.568
N_ROW = 428
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
EXIT_TOL = DELTA / 2 + 1e-12
RUNTIME_BAR = 900.0
N_CHECKS_EXPECTED = 27

CHECKS: list[tuple[str, bool, str]] = []
ARTIFACT_TEXT: dict[str, str] = {}


def check(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    CHECKS.append((name, result, detail))
    print("  [%s] %-46s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def fmt(x, digits: int = 8) -> str:
    return mp.nstr(mp.mpf(x) if not isinstance(x, mp.mpf) else x, digits,
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


# ------------------------------------------- Euler--Maclaurin source side
LOGDERIV_CACHE: dict[tuple[str, int], mp.mpf] = {}


def dirichlet_logderivative(s: mp.mpf, cutoff: int,
                            terms: int) -> tuple[mp.mpf, mp.mpf]:
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


def zeta_logderiv(s: mp.mpf, cutoff: int = 96, terms: int = 28) -> mp.mpf:
    """zeta'/zeta(s) via own Euler--Maclaurin continuation (cached)."""
    key = (mp.nstr(s, 40), mp.mp.dps)
    if key in LOGDERIV_CACHE and cutoff == 96 and terms == 28:
        return LOGDERIV_CACHE[key]
    value, derivative = dirichlet_logderivative(s, cutoff, terms)
    out = derivative / value
    if cutoff == 96 and terms == 28:
        LOGDERIV_CACHE[key] = out
    return out


def h_pole(sigma: mp.mpf) -> mp.mpf:
    s = mp.mpf("0.5") + sigma
    return 1 / s + 1 / (s - 1)


def h_gamma(sigma: mp.mpf) -> mp.mpf:
    s = mp.mpf("0.5") + sigma
    return mp.digamma(s / 2) / 2 - mp.log(mp.pi) / 2


def pin_reference(sigma: mp.mpf) -> mp.mpf:
    """P(sigma) = xi'/xi(1/2+sigma), source-only."""
    return h_pole(sigma) + h_gamma(sigma) + zeta_logderiv(mp.mpf("0.5")
                                                          + sigma)


def pin_theta(sigma: mp.mpf, theta: mp.mpf) -> mp.mpf:
    """Half-density exponent theta on the prime weights (theta=1/2 true)."""
    return h_pole(sigma) + h_gamma(sigma) + zeta_logderiv(theta + sigma)


def pick_matrix(values: list[mp.mpf], sigmas: list[mp.mpf]) -> mp.matrix:
    n = len(values)
    matrix = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            matrix[j, k] = (values[j] + values[k]) / (sigmas[j] + sigmas[k])
    return matrix


def eig_range(matrix: mp.matrix) -> tuple[mp.mpf, mp.mpf]:
    eigenvalues = mp.eigsy(matrix, eigvals_only=True)
    absmax = max(abs(eigenvalues[i]) for i in range(matrix.rows))
    return eigenvalues[0], absmax


def interval_distance_widths(value: float, lo: float, hi: float) -> float:
    width = hi - lo
    if lo <= value <= hi:
        return 0.0
    return (lo - value) / width if value < lo else (value - hi) / width


# ------------------------------------------------------- sieve (numpy)
def numpy_primes(limit: int) -> np.ndarray:
    flags = np.ones(limit + 1, dtype=bool)
    flags[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            flags[p * p::p] = False
    return np.nonzero(flags)[0]


def prime_power_terms(primes: np.ndarray, limit: int) -> list[tuple[int,
                                                                    float]]:
    """(p^m, log p) for m >= 2, p^m <= limit."""
    out: list[tuple[int, float]] = []
    for p in primes[primes <= math.isqrt(limit)]:
        p = int(p)
        lp = math.log(p)
        q = p * p
        while q <= limit:
            out.append((q, lp))
            q *= p
    return out


# ------------------------------------------------------- germ quadratures
def germ_gamma_integrand(u: mp.mpf, s: mp.mpf) -> mp.mpf:
    if u < mp.mpf("1e-8"):
        h1 = (s - 2) / 2 + (4 - s * s) * u / 4
        h2 = -mp.mpf("0.5") - u / 6
        return h1 + mp.e ** (-s * u) * h2
    h1 = (mp.e ** (-2 * u) - mp.e ** (-s * u)) / (2 * u)
    h2 = 1 / (2 * u) - 1 / (1 - mp.e ** (-2 * u))
    return h1 + mp.e ** (-s * u) * h2


def germ_gamma(s: mp.mpf) -> mp.mpf:
    """int_0^inf (e^{-2u}/(2u) - e^{-su}/(1-e^{-2u})) du  ( = psi(s/2)/2 )."""
    return mp.quad(lambda u: germ_gamma_integrand(u, s),
                   [0, mp.mpf("0.1"), 1, 10, mp.inf])


# --------------------------------- corpus screw rows (port: cohomspec_probe)
MP_CONST: dict[str, mp.mpf] = {}
S_CACHE: dict[int, mp.mpf] = {}


def setup_constants() -> None:
    with mp.workdps(DPS + 20):
        MP_CONST["psi14"] = mp.digamma(mp.mpf(1) / 4)
        MP_CONST["logpi"] = mp.log(mp.pi)
        MP_CONST["phi1"] = mp.lerchphi(1, 2, mp.mpf(1) / 4)


def s_arch_grid(index: int) -> mp.mpf:
    if index in S_CACHE:
        return S_CACHE[index]
    with mp.workdps(DPS + 15):
        t = mp.mpf(index) * mp.mpf(DELTA_TEXT)
        if index == 0:
            value = MP_CONST["phi1"] / 4
        elif t < mp.mpf("0.3"):
            value = (mp.exp(-t / 2)
                     * mp.lerchphi(mp.exp(-2 * t), 2, mp.mpf(1) / 4) / 4)
        else:
            z = mp.exp(-2 * t)
            total = mp.mpf(0)
            power = mp.mpf(1)
            k = 0
            floor = mp.mpf(10) ** (-(DPS + 8))
            while power > floor * (1 + abs(total)):
                total += power / (mp.mpf(k) + mp.mpf(1) / 4) ** 2
                power *= z
                k += 1
            value = mp.exp(-t / 2) * total / 4
    S_CACHE[index] = value
    return value


def base_g_values(n: int) -> list[mp.mpf]:
    dl = mp.mpf(DELTA_TEXT)
    values: list[mp.mpf] = []
    with mp.workdps(DPS + 15):
        for j in range(n + 1):
            t = j * dl
            value = -8 * (mp.cosh(t / 2) - 1)
            value -= (t / 2) * (MP_CONST["psi14"] - MP_CONST["logpi"])
            value -= MP_CONST["phi1"] / 4
            value += s_arch_grid(j)
            values.append(value)
    return values


def sieve_small(limit: int) -> list[int]:
    bits = bytearray(b"\x01") * (limit + 1)
    bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            count = (limit - p * p) // p + 1
            bits[p * p:limit + 1:p] = b"\x00" * count
    return [i for i in range(2, limit + 1) if bits[i]]


def prime_atoms(L: float) -> list[tuple[int, int, mp.mpf, mp.mpf]]:
    limit = int(math.exp(L)) + 1
    out: list[tuple[int, int, mp.mpf, mp.mpf]] = []
    with mp.workdps(DPS + 15):
        for p in sieve_small(limit):
            lp = mp.log(p)
            q = p
            m = 1
            while m * float(lp) < L - 1e-14:
                out.append((p, m, m * lp, lp / mp.sqrt(q)))
                if q > limit // p:
                    break
                q *= p
                m += 1
    out.sort(key=lambda item: item[2])
    return out


def lag_row_from_g(values: list[mp.mpf]) -> list[mp.mpf]:
    with mp.workdps(DPS + 15):
        dl = mp.mpf(DELTA_TEXT)
        n = len(values) - 1
        row = [-2 * values[1] / dl]
        for d in range(1, n):
            row.append(-(values[d - 1] - 2 * values[d] + values[d + 1]) / dl)
    return row


def direct_true_g(base: list[mp.mpf],
                  atoms: list[tuple[int, int, mp.mpf, mp.mpf]]) \
        -> list[mp.mpf]:
    ordered = sorted([(u, weight) for _p, _m, u, weight in atoms],
                     key=lambda item: item[0])
    out: list[mp.mpf] = []
    active_weight = mp.mpf(0)
    active_weight_u = mp.mpf(0)
    cursor = 0
    dl = mp.mpf(DELTA_TEXT)
    with mp.workdps(DPS + 15):
        for j, background in enumerate(base):
            t = j * dl
            while cursor < len(ordered) and ordered[cursor][0] < t:
                u, weight = ordered[cursor]
                active_weight += weight
                active_weight_u += weight * u
                cursor += 1
            out.append(background + t * active_weight - active_weight_u)
    return out


def smooth_g(base: list[mp.mpf]) -> list[mp.mpf]:
    dl = mp.mpf(DELTA_TEXT)
    values = []
    with mp.workdps(DPS + 15):
        for j, value in enumerate(base):
            t = j * dl
            values.append(value + 4 * mp.exp(t / 2) - 2 * t - 4)
    return values


def atom_row(u: mp.mpf, weight: mp.mpf, n: int) -> list[mp.mpf]:
    with mp.workdps(DPS + 15):
        out = [mp.mpf(0) for _ in range(n)]
        x = u / mp.mpf(DELTA_TEXT)
        lo = int(mp.floor(x))
        for d in (lo, lo + 1):
            if 0 <= d < n:
                value = 1 - abs(x - d)
                if value > 0:
                    out[d] -= weight * value
    return out


def scrambled_weights(atoms: list[tuple[int, int, mp.mpf, mp.mpf]]) \
        -> list[mp.mpf]:
    q_values = [p ** m for p, m, _u, _w in atoms]
    order = sorted(range(len(atoms)),
                   key=lambda i: (q_values[i] * GOLDEN) % 1.0)
    return [atoms[i][3] for i in order]


def scrambled_row(base_row: list[mp.mpf],
                  atoms: list[tuple[int, int, mp.mpf, mp.mpf]]) \
        -> tuple[list[mp.mpf], list[mp.mpf]]:
    weights = scrambled_weights(atoms)
    row = list(base_row)
    with mp.workdps(DPS + 15):
        for atom, weight in zip(atoms, weights):
            ar = atom_row(atom[2], weight, len(row))
            row = [a + b for a, b in zip(row, ar)]
    return row, weights


def szego(row: list[mp.mpf]) -> dict:
    with mp.workdps(DPS):
        c0 = row[0]
        moments = [value / c0 for value in row]
        phi = [mp.mpf(1)]
        phi_star = [mp.mpf(1)]
        alphas: list[mp.mpf] = []
        fail_k = -1
        fail_kind = ""
        attempted = mp.nan
        for k in range(len(moments) - 1):
            numerator = mp.fdot(phi, moments[1:k + 2])
            denominator = mp.fdot(phi_star, moments[0:k + 1])
            if denominator <= 0:
                fail_k = k
                fail_kind = "DEN_NONPOSITIVE"
                break
            alpha = numerator / denominator
            if abs(alpha) >= 1:
                fail_k = k
                fail_kind = "ALPHA_EXIT"
                attempted = alpha
                break
            alphas.append(alpha)
            zphi = [mp.mpf(0)] + phi
            phi_pad = phi_star + [mp.mpf(0)]
            phi = [zphi[j] - alpha * phi_pad[j] for j in range(k + 2)]
            phi_star = [phi_pad[j] - alpha * zphi[j] for j in range(k + 2)]
        return {"ok": fail_k < 0, "alphas": alphas, "fail_k": fail_k,
                "fail_kind": fail_kind, "attempted": attempted}


# ---------------------------------------------------------------- main
def main() -> int:
    print("=" * 78)
    print("stage1_construction_probe  PRIME.STAGE1.CONSTRUCTION.01")
    print("FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM. EXPLORATION ONLY. A failed construction is a")
    print("measurement of the missing mathematics, not progress on RH.")
    print("=" * 78)

    flags: dict[str, bool] = {}

    # ============================================================ A
    section("A. INSTRUMENTS: firewall, wards, reference pins, germs")

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
        "SIGMAS = (0.6, 0.75, 0.9,",
        "SUZKREIN-TRANSCRIPTION iff <= 1e-6",
        "Z1-TRANSCRIPTION (band pins == cache"])
    ok_cs, miss_cs = ward("cohomspec", [
        "FROZEN_SMOOTH_EXIT = 0.264", "FROZEN_SCRAM_EXIT = 0.744",
        "8.581810362e-2"])
    ok_rm, miss_rm = ward("roadmap", [
        "its trace formula, evaluated on the exponential test class",
        "log p with weights"])
    ok_vb, miss_vb = ward("vbk", ["c^T Pick_N c = <-g'', f_c*f_c~>."])
    check("A3 interface wards (Z1 / controls / (AC) / M1a)",
          ok_kr and ok_cs and ok_rm and ok_vb,
          "krein=%s cohomspec=%s roadmap=%s vbk=%s"
          % (miss_kr or "ok", miss_cs or "ok", miss_rm or "ok",
             miss_vb or "ok"))

    with mp.workdps(DPS):
        pin_sigmas = [mp.mpf(1) + mp.mpf(1) / j
                      for j in range(1, PIN_COUNT + 1)]
        grid_sigmas = [mp.mpf(1) * mp.mpf(repr(v)) if isinstance(v, float)
                       else mp.mpf(v) for v in SIGMAS16]
        # exact rationals for the three fractional grid entries
        grid_sigmas[4] = mp.mpf(8) / 7
        grid_sigmas[5] = mp.mpf(7) / 6
        grid_sigmas[8] = mp.mpf(4) / 3
        p_pins = [pin_reference(sig) for sig in pin_sigmas]
        p_pins_refined = [h_pole(sig) + h_gamma(sig)
                          + zeta_logderiv(mp.mpf("0.5") + sig, 128, 32)
                          for sig in pin_sigmas]
        em_dev = max(abs(a - b) for a, b in zip(p_pins, p_pins_refined))
    check("A4 Euler--Maclaurin stability (96/28 vs 128/32)",
          em_dev < mp.mpf("1e-70"), "max dev=%s" % fmt(em_dev, 4))

    with mp.workdps(DPS_QUAD):
        germ_devs = []
        for s_test in ("1.1", "1.5", "2.5", "5.0", "12.5"):
            s = mp.mpf(s_test)
            quad_value = germ_gamma(s)
            closed = mp.digamma(s / 2) / 2
            germ_devs.append(abs(quad_value - closed) / abs(closed))
        pole_devs = []
        for s_test in ("1.6", "2.5", "4.5"):
            s = mp.mpf(s_test)
            q1 = mp.quad(lambda u: mp.e ** (-s * u), [0, mp.inf])
            q2 = mp.quad(lambda u: mp.e ** ((1 - s) * u), [0, mp.inf])
            pole_devs.append(abs(q1 - 1 / s) * s)
            pole_devs.append(abs(q2 - 1 / (s - 1)) * (s - 1))
    check("A5 archimedean germ quadrature identities",
          max(germ_devs) < mp.mpf("1e-12")
          and max(pole_devs) < mp.mpf("1e-18"),
          "psi(s/2)/2 germ max rel=%s; pole germs max rel=%s"
          % (fmt(max(germ_devs), 3), fmt(max(pole_devs), 3)))

    with mp.workdps(DPS):
        floors_ref: list[mp.mpf] = []
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
    check("A6 reference floors inside certified intervals (N<=4)",
          in_intervals and all(f > 0 for f in floors_ref),
          "ladder N=1..12 all positive; floor_12=%s"
          % fmt(floors_ref[11], 4))

    # ============================================================ B
    section("B. CANDIDATE A -- BOST--CONNES SQUARE (operator side)")
    print("  H eps_n = log(n) eps_n on l^2(N>=2); W eps_n = Lambda(n)")
    print("  n^{-1/2} eps_n; candidate = l^2 (+) H_arch; Theta_A = 1/2 + iH.")

    print("  sieving to %d ..." % NSIEVE)
    primes = numpy_primes(NSIEVE)
    logp = np.log(primes.astype(np.float64))
    pp_terms = prime_power_terms(primes, NSIEVE)
    print("  primes=%d  prime-power atoms (m>=2)=%d"
          % (len(primes), len(pp_terms)))

    def finite_trace(s: float, cut: int) -> float:
        idx = np.searchsorted(primes, cut, side="right")
        head = float(np.dot(logp[:idx], np.exp(-s * logp[:idx])))
        head += sum(lp * q ** (-s) for q, lp in pp_terms if q <= cut)
        return head

    def tail_model(s: float, cut: int) -> float:
        return cut ** (1.0 - s) / (s - 1.0)

    # B1: trace identity weld at the 16 frozen sigma + the 12 pins
    with mp.workdps(DPS):
        d_targets = {}
        for sig in list(grid_sigmas) + list(pin_sigmas):
            s = mp.mpf("0.5") + sig
            d_targets[float(sig)] = float(-zeta_logderiv(s))
    print("  -- trace identity weld: Tr(W e^{-sigma H})_{N=4e7} + PNT tail")
    print("     vs -zeta'/zeta(1/2+sigma) [own EM continuation] --")
    barred: list[float] = []
    reported: list[tuple[float, float]] = []
    for sig_f in sorted(d_targets):
        s = 0.5 + sig_f
        approx = finite_trace(s, NSIEVE) + tail_model(s, NSIEVE)
        target = d_targets[sig_f]
        rel = abs(approx - target) / abs(target)
        tag = "barred" if s >= 1.5 else "REPORT-ONLY (near-critical cost)"
        print("    sigma=%-9s s=%-8s trace+tail=%-14s EM=%-14s rel=%.3e  %s"
              % ("%.6g" % sig_f, "%.6g" % s, "%.8e" % approx,
                 "%.8e" % target, rel, tag))
        if s >= 1.5:
            barred.append(rel)
        else:
            reported.append((sig_f, rel))
    check("B1 BC trace identity weld (barred s>=1.5)",
          max(barred) < 1e-6,
          "max rel=%.3e over %d barred values; near-critical residuals: %s"
          % (max(barred), len(barred),
             ", ".join("sigma=%.2f:%.2e" % t for t in reported)))

    # B2: truncation-cost law at the near-critical grid values
    cost_rows = []
    for sig_f in (0.6, 0.75, 0.9):
        s = 0.5 + sig_f
        target = d_targets[sig_f]
        resids = []
        for cut in (100_000, 1_000_000, 10_000_000, NSIEVE):
            approx = finite_trace(s, cut) + tail_model(s, cut)
            resids.append(abs(approx - target))
        slope = np.polyfit(np.log10([1e5, 1e6, 1e7, NSIEVE]),
                           np.log10(resids), 1)[0]
        cost_rows.append((sig_f, resids, slope))
        print("    sigma=%.2f  |resid| at N=1e5/1e6/1e7/4e7: "
              "%.3e / %.3e / %.3e / %.3e   slope=%.3f"
              % (sig_f, *resids, slope))
    check("B2 near-critical truncation cost decreasing",
          all(r[1][-1] < r[1][0] for r in cost_rows),
          "endpoint residual falls at all three near-critical sigma; "
          "fitted slopes %s (polynomial cost, no wall crossed)"
          % ", ".join("%.3f" % r[2] for r in cost_rows))

    # B3: candidate-A assembled pin == reference (assembly consistency)
    with mp.workdps(DPS):
        assembly_dev = max(
            abs((h_pole(sig) + h_gamma(sig)
                 + zeta_logderiv(mp.mpf("0.5") + sig)) - pin_reference(sig))
            for sig in grid_sigmas)
    g1a = in_intervals
    check("B3 candidate-A pin assembly == reference pins",
          assembly_dev < mp.mpf("1e-80") and g1a,
          "max dev=%s; floors = certified intervals (G1 PASS by "
          "construction -- typed PASS-TRANSCRIBING)" % fmt(assembly_dev, 3))
    flags["A_G1"] = g1a

    # B4: the Z1 screen (G2)
    cut_z1 = 1_000_000
    s_z1 = 2.5
    idx = np.searchsorted(primes, cut_z1, side="right")
    fwd = float(np.dot(logp[:idx], np.exp(-s_z1 * logp[:idx])))
    rev = math.fsum(sorted(
        [float(lp * math.exp(-s_z1 * lp)) for lp in logp[:idx]]
        + [lp * q ** (-s_z1) for q, lp in pp_terms if q <= cut_z1]))
    fwd += sum(lp * q ** (-s_z1) for q, lp in pp_terms if q <= cut_z1)
    two_order_dev = abs(fwd - rev) / abs(fwd)
    z1_fires = two_order_dev < Z1_BAR  # readout IS the partial sum
    check("B4 Z1 screen fires: TRANSCRIPTION (G2 FAIL)",
          z1_fires,
          "readout == cache partial sum by construction; two-order "
          "summation dev=%.3e <= %.0e; the Krein carrier benchmark "
          "RESUMS (rel > 1e-6) -- candidate A does not" %
          (two_order_dev, Z1_BAR))
    flags["A_G2_fired"] = z1_fires

    # B5: Theta_A duality gates (G5 structural)
    bc_n = [2, 3, 4, 5, 6, 7]
    theta_a = np.diag([0.5 + 1j * math.log(n) for n in bc_n])
    dual_defect = np.max(np.abs(theta_a + theta_a.conj().T
                                - np.eye(len(bc_n))))
    re_defect = np.max(np.abs(np.linalg.eigvals(theta_a).real - 0.5))
    check("B5 Theta_A = 1/2 + iH: Theta+Theta*=I, Re spec = 1/2",
          dual_defect < 1e-15 and re_defect < 1e-15,
          "duality defect=%.1e; max|Re-1/2|=%.1e (G5 STRUCTURAL PASS)"
          % (dual_defect, re_defect))
    flags["A_G5_structural"] = dual_defect < 1e-15

    # B6: spectral content -- counting law (G5 content)
    print("  -- G5 content: spec(Theta_A) = 1/2 + i log n vs zeta zeros --")
    ratios = []
    for T in (10.0, 20.0, 30.0):
        n_bc = math.floor(math.exp(T)) - 1
        n_rvm = T / (2 * math.pi) * math.log(T / (2 * math.pi)) \
            - T / (2 * math.pi) + 7.0 / 8.0
        ratio = n_bc / max(n_rvm, 1.0)
        ratios.append(ratio)
        print("    T=%4.0f  N_BC=%.4e  N_RvM~%.2f  ratio=%.3e"
              % (T, n_bc, n_rvm, ratio))
    check("B6 BRK-A3-SPECTRUMCOUNT fires",
          min(ratios) > 1e3,
          "BC counting e^T vs (T/2pi)log(T/2pi); min ratio=%.2e > 1e3 -- "
          "the BC spectrum is NOT the zero set" % min(ratios))
    flags["A_G5_content_fail"] = min(ratios) > 1e3

    # B7: piece decomposition of the Pick matrices (G3)
    print("  -- G3: Pick piece decomposition at the pins (pole/Gamma/prime)")
    with mp.workdps(DPS):
        vals_pole = [h_pole(sig) for sig in pin_sigmas]
        vals_gam = [h_gamma(sig) for sig in pin_sigmas]
        vals_pr = [zeta_logderiv(mp.mpf("0.5") + sig) for sig in pin_sigmas]
        prime_neg = True
        cancel_digits_4 = mp.mpf(0)
        for n in range(1, 9):
            lam_p, rad_p = eig_range(pick_matrix(vals_pole[:n],
                                                 pin_sigmas[:n]))
            lam_g, rad_g = eig_range(pick_matrix(vals_gam[:n],
                                                 pin_sigmas[:n]))
            lam_r, rad_r = eig_range(pick_matrix(vals_pr[:n],
                                                 pin_sigmas[:n]))
            lam_t, _ = eig_range(pick_matrix(
                [a + b + c for a, b, c in zip(vals_pole, vals_gam,
                                              vals_pr)][:n],
                pin_sigmas[:n]))
            max_rad = max(rad_p, rad_g, rad_r)
            digits = mp.log10(max_rad / lam_t) if lam_t > 0 else mp.inf
            prime_neg = prime_neg and (lam_r < 0)
            if n == 4:
                cancel_digits_4 = digits
            print("    N=%d  lam_min: pole=%-12s Gamma=%-12s prime=%-12s "
                  "total=%-12s  cancel=%.2f digits"
                  % (n, fmt(lam_p, 5), fmt(lam_g, 5), fmt(lam_r, 5),
                     fmt(lam_t, 5), float(digits)))
    check("B7 BRK-A1-CROSSTERMS fires",
          prime_neg and cancel_digits_4 >= 12,
          "prime piece lam_min < 0 for all N<=8; positivity needs %.2f "
          "digits of cross-piece cancellation at N=4; a direct sum "
          "(zero cross terms) supplies 0" % float(cancel_digits_4))
    flags["A_G3_fail"] = prime_neg and cancel_digits_4 >= 12

    # B8: corpus Schur image of the archimedean window
    print("  building corpus rows (delta=%s, n=%d, L=%.3f) ..."
          % (DELTA_TEXT, N_ROW, L_ROW))
    setup_constants()
    atoms_row = prime_atoms(L_ROW)
    base_vals = base_g_values(N_ROW)
    row_arch = lag_row_from_g(base_vals)
    row_true = lag_row_from_g(direct_true_g(base_vals, atoms_row))
    row_smooth = lag_row_from_g(smooth_g(base_vals))
    row_scram, scram_w = scrambled_row(row_arch, atoms_row)
    log2 = math.log(2.0)
    prefix_d = int(log2 / DELTA) - 2  # stencil-safe identical prefix
    prefix_dev = max(abs(row_arch[d] - row_true[d])
                     for d in range(prefix_d))
    res_true = szego(row_true)
    res_arch = szego(row_arch)
    true_max_alpha = max(abs(float(a)) for a in res_true["alphas"])
    if res_arch["ok"]:
        arch_exit_txt = "NO EXIT <= %.3f" % L_ROW
        arch_exit = float("inf")
    else:
        arch_exit = res_arch["fail_k"] * DELTA
        arch_exit_txt = "%s at r=%.3f (overhang past log2: %+.3f)" % (
            res_arch["fail_kind"], arch_exit, arch_exit - log2)
    check("B8 archimedean window (corpus Schur image)",
          prefix_dev < mp.mpf("1e-90")
          and res_true["ok"]
          and abs(true_max_alpha - FROZEN_TRUE_MAX_ALPHA) < 1e-3,
          "arch-only == true row below log2 (dev=%s, %d lags); true "
          "max|alpha|=%.6f (frozen %.6f); ARCH-ONLY: %s"
          % (fmt(prefix_dev, 2), prefix_d, true_max_alpha,
             FROZEN_TRUE_MAX_ALPHA, arch_exit_txt))
    flags["arch_exit"] = arch_exit

    # ============================================================ C
    section("C. CANDIDATE B -- FOLIATED SUSPENSION HOST (geometric side)")
    print("  circles: circumference log p per prime; m-th return at")
    print("  u = m log p; transverse weight dictionary, three rows.")

    # C1: the weight dictionary and its exact conversions
    print("  -- weight dictionary (m-th return of circle p) --")
    conv_dev = 0.0
    for p in (2, 3, 5):
        for m in (1, 2, 3):
            ell = math.log(p)
            w_req = ell * p ** (-m / 2.0)
            w_nat = ell / (p ** m - 1.0)
            w_sel = ell / (2.0 * math.sinh(m * ell / 2.0))
            conv_dev = max(conv_dev,
                           abs(w_req - w_nat * 2 * math.sinh(m * ell / 2))
                           / w_req,
                           abs(w_req - w_sel * (1 - p ** (-float(m))))
                           / w_req)
            if m == 1:
                print("    p=%d m=1: required=%.8f  anosov=%.8f  "
                      "selberg=%.8f  (req/anosov = 2sinh(l/2) = %.6f)"
                      % (p, w_req, w_nat, w_sel,
                         2 * math.sinh(ell / 2)))
    check("C1 weight dictionary conversions exact",
          conv_dev < 1e-14,
          "required = anosov*2sinh(ml/2) = selberg*(1-p^-m); "
          "max rel dev=%.2e -- the missing transverse datum is the "
          "half-form |det(I-P^m)|^{-1/2} normalisation" % conv_dev)

    # C2: supplied assembly at the 16 frozen sigma (germ quadratures)
    print("  -- supplied assembly: pole germs + arch germ + half-form")
    print("     prime circles - log(pi)/2, at the 16 frozen sigma --")
    with mp.workdps(DPS_QUAD):
        max_asm_dev = mp.mpf(0)
        for sig in grid_sigmas:
            s = mp.mpf("0.5") + mp.mpf(sig)
            assembled = (1 / s + 1 / (s - 1)          # H^0/H^2 fixed pts
                         + germ_gamma(s)              # archimedean germ
                         - mp.log(mp.pi) / 2          # place constant
                         + zeta_logderiv(s))          # half-form circles
            reference = pin_reference(mp.mpf(sig))
            dev = abs(assembled - reference) / abs(reference)
            max_asm_dev = max(max_asm_dev, dev)
        print("    max rel deviation over 16 sigma: %s" % fmt(max_asm_dev, 3))
    g1b_supplied = max_asm_dev < mp.mpf("1e-10") and in_intervals
    check("C2 supplied assembly reproduces all 16 pins",
          g1b_supplied,
          "max rel=%s; floors = certified (G1 PASS-TRANSCRIBING; every "
          "weight SUPPLIED, Z1 fires as for candidate A)"
          % fmt(max_asm_dev, 3))
    flags["B_G1_supplied"] = g1b_supplied

    # C3: the (AC) weld against the frozen corpus value
    with mp.workdps(DPS):
        ac_pins = [pin_reference(mp.mpf(repr(sig))) for sig in AC_SIGMAS]
        ac_value = mp.mpf(0)
        for j, cj in enumerate(AC_COEFFS):
            for k, ck in enumerate(AC_COEFFS):
                ac_value += (mp.mpf(repr(cj)) * mp.mpf(repr(ck))
                             * (ac_pins[j] + ac_pins[k])
                             / (mp.mpf(repr(AC_SIGMAS[j]))
                                + mp.mpf(repr(AC_SIGMAS[k]))))
        ac_dev = abs(ac_value - mp.mpf(repr(FROZEN_AC_LHS))) \
            / mp.mpf(repr(FROZEN_AC_LHS))
    check("C3 (AC) weld: c^T Pick c vs frozen 8.581810362e-2",
          ac_dev < mp.mpf("1e-8"),
          "value=%s rel dev=%s (frozen corpus read, cohomspec_probe)"
          % (fmt(ac_value, 10), fmt(ac_dev, 3)))

    # C4: the non-supplied weight rows against the certified floors
    print("  -- ANOSOV and SELBERG rows vs certified floors --")
    with mp.workdps(DPS_TOWER):
        def det_tower(sigma: mp.mpf) -> mp.mpf:
            """sum_{k>=1} sum_n Lambda(n) n^{-(sigma+k)} (Anosov trace)."""
            total = mp.mpf(0)
            for k in range(1, TOWER_K + 1):
                total += -zeta_logderiv(sigma + k)
            return total

        def selberg_tower(sigma: mp.mpf) -> mp.mpf:
            """sum_{k>=1} sum_n Lambda(n) n^{-(sigma+1/2+k)} (excess)."""
            total = mp.mpf(0)
            for k in range(1, TOWER_K + 1):
                total += -zeta_logderiv(sigma + mp.mpf("0.5") + k)
            return total

        rows_nat: list[mp.mpf] = []
        rows_sel: list[mp.mpf] = []
        for sig in pin_sigmas[:4]:
            base = h_pole(sig) + h_gamma(sig)
            d_half = -zeta_logderiv(mp.mpf("0.5") + sig)
            nat = det_tower(sig)
            sel = d_half + selberg_tower(sig)
            rows_nat.append(base - nat)
            rows_sel.append(base - sel)
            if sig == pin_sigmas[0]:
                print("    sigma=2: required prime side=%.10f  anosov=%.10f"
                      "  (ratio %.4f -- a 2%%-trap the floors kill)"
                      % (float(d_half), float(nat), float(nat / d_half)))
                print("             selberg=%.10f (overshoot %.3e)"
                      % (float(sel), float(sel - d_half)))
        dist_nat = []
        dist_sel = []
        for n in range(1, 5):
            lam_n, _ = eig_range(pick_matrix(rows_nat[:n], pin_sigmas[:n]))
            lam_s, _ = eig_range(pick_matrix(rows_sel[:n], pin_sigmas[:n]))
            dn = interval_distance_widths(float(lam_n), *CERTIFIED[n])
            ds = interval_distance_widths(float(lam_s), *CERTIFIED[n])
            dist_nat.append(dn)
            dist_sel.append(ds)
            print("    N=%d  anosov lam_min=%-13s (%.3e widths off)   "
                  "selberg lam_min=%-13s (%.3e widths off)"
                  % (n, fmt(lam_n, 6), dn, fmt(lam_s, 6), ds))
    check("C4 BRK-B1-HALFDENSITY fires (both natural rows dead at N=1)",
          dist_nat[0] > 1e3 and dist_sel[0] > 1e3,
          "anosov %.3e widths off, selberg %.3e widths off at the first "
          "certified rung -- only the half-form row survives"
          % (dist_nat[0], dist_sel[0]))
    flags["B_G1_natural_dead"] = dist_nat[0] > 1e3 and dist_sel[0] > 1e3

    # C5: theta pinning windows from the certified ladder
    print("  -- theta window: weights n^{-theta}; certified floors pin")
    print("     theta around 1/2 (linearised + 3x overshoot confirm) --")
    eps = mp.mpf("1e-20")
    with mp.workdps(DPS):
        def floor_theta(nn: int, theta: mp.mpf) -> mp.mpf:
            vals = [pin_theta(sig, theta) for sig in pin_sigmas[:nn]]
            lam, _ = eig_range(pick_matrix(vals, pin_sigmas[:nn]))
            return lam

        theta_windows: list[float] = []
        theta_confirms = True
        half = mp.mpf("0.5")
        for n in range(1, 5):
            lam0 = floors_ref[n - 1]
            dl = (floor_theta(n, half + eps)
                  - floor_theta(n, half - eps)) / (2 * eps)
            lo, hi = (mp.mpf(repr(CERTIFIED[n][0])),
                      mp.mpf(repr(CERTIFIED[n][1])))
            width = float((hi - lo) / abs(dl))
            theta_windows.append(width)
            # 3x overshoot on each side must exit the interval
            up = (hi - lam0) / dl
            down = (lam0 - lo) / dl
            lam_up = floor_theta(n, half + 3 * up)
            lam_dn = floor_theta(n, half - 3 * down)
            exit_up = not (lo <= lam_up <= hi)
            exit_dn = not (lo <= lam_dn <= hi)
            theta_confirms = theta_confirms and exit_up and exit_dn
            print("    N=%d  dlam/dtheta=%-12s window |theta-1/2| "
                  "<~ %.3e  (3x overshoot exits: %s/%s)"
                  % (n, fmt(dl, 5), width, exit_up, exit_dn))
    theta_bind = min(theta_windows)
    theta_rung = 1 + theta_windows.index(theta_bind)
    check("C5 certified ladder pins the half-density exponent",
          theta_confirms and theta_bind < 1e-9,
          "binding rung N=%d: |theta-1/2| <~ %.3e (per-rung windows %s)"
          % (theta_rung, theta_bind,
             ", ".join("%.2e" % w for w in theta_windows)))
    flags["theta_win"] = theta_bind

    # C6: regularisation-constant pinning (the pole bookkeeping)
    print("  -- delta_c window: an additive constant (counterterm/place")
    print("     normalisation slack) shifts Pick by 2*delta_c*Cauchy --")
    with mp.workdps(DPS):
        def floor_const(nn: int, dc: mp.mpf) -> mp.mpf:
            vals = [p_pins[j] + dc for j in range(nn)]
            lam, _ = eig_range(pick_matrix(vals, pin_sigmas[:nn]))
            return lam

        const_windows: list[float] = []
        const_confirms = True
        for n in range(1, 5):
            lam0 = floors_ref[n - 1]
            dl = (floor_const(n, eps) - floor_const(n, -eps)) / (2 * eps)
            lo, hi = (mp.mpf(repr(CERTIFIED[n][0])),
                      mp.mpf(repr(CERTIFIED[n][1])))
            width = float((hi - lo) / abs(dl))
            const_windows.append(width)
            up = (hi - lam0) / dl
            down = (lam0 - lo) / dl
            exit_up = not (lo <= floor_const(n, 3 * up) <= hi)
            exit_dn = not (lo <= floor_const(n, -3 * down) <= hi)
            const_confirms = const_confirms and exit_up and exit_dn
            print("    N=%d  dlam/dc=%-12s window |delta_c| <~ %.3e  "
                  "(3x overshoot exits: %s/%s)"
                  % (n, fmt(dl, 5), width, exit_up, exit_dn))
    const_bind = min(const_windows)
    const_rung = 1 + const_windows.index(const_bind)
    check("C6 certified ladder pins the bookkeeping constant",
          const_confirms and const_bind < 1e-8,
          "binding rung N=%d: |delta_c| <~ %.3e (per-rung %s; dlam/dc "
          "collapses with the floor -- the ladder does NOT tighten the "
          "constant); counterterm e^{-2u}/(2u) and -log(pi)/2 SUPPLIED, "
          "not forced (BRK-B2-ARCHGERM)"
          % (const_rung, const_bind,
             ", ".join("%.2e" % w for w in const_windows)))
    flags["const_win"] = const_bind

    # C7: G5 flow gates and the twist link
    n_four = 8
    ell2 = math.log(2.0)
    h_step = ell2 / n_four
    shift = np.zeros((n_four, n_four))
    for i in range(n_four):
        shift[i, (i + 1) % n_four] += 1.0 / (2 * h_step)
        shift[i, (i - 1) % n_four] -= 1.0 / (2 * h_step)
    theta_raw = shift                                # theta = 0
    theta_half = 0.5 * np.eye(n_four) + shift        # theta = 1/2
    raw_dual = np.max(np.abs(theta_raw + theta_raw.T - np.eye(n_four)))
    raw_re = np.max(np.abs(np.linalg.eigvals(theta_raw).real))
    half_dual = np.max(np.abs(theta_half + theta_half.T - np.eye(n_four)))
    half_re = np.max(np.abs(np.linalg.eigvals(theta_half).real - 0.5))
    link_dev = max(abs(math.exp(-m * math.log(p) / 2.0) - p ** (-m / 2.0))
                   for p in (2, 3, 5) for m in (1, 2, 3))
    link_ok = (raw_dual > 0.9 and raw_re < 1e-12
               and half_dual < 1e-12 and half_re < 1e-12
               and link_dev < 1e-15)
    check("C7 G5 twist link: generator theta == weight theta",
          link_ok,
          "untwisted d/du: ||Theta+Theta*-I||=%.2f, Re spec=0 (G5 FAIL); "
          "theta=1/2 twist: defect=%.1e, Re=1/2 (G5 PASS); "
          "e^{-m l_p/2}=p^{-m/2} dev=%.1e -- SAME datum as the G1 weights"
          % (raw_dual, half_dual, link_dev))
    flags["B_G5_link"] = link_ok

    # ============================================================ D
    section("D. CONTROLS (G4): smooth and scrambled worlds must die")

    # D1: smooth (prime-free PNT) world in pin currency
    with mp.workdps(DPS):
        rows_sm = []
        for sig in pin_sigmas[:4]:
            s = mp.mpf("0.5") + sig
            rows_sm.append(h_pole(sig) + h_gamma(sig) - 1 / (s - 1))
        pole_eaten = abs(rows_sm[0] - (1 / (mp.mpf("0.5") + pin_sigmas[0])
                                       + h_gamma(pin_sigmas[0])))
        dist_sm = []
        for n in range(1, 5):
            lam, _ = eig_range(pick_matrix(rows_sm[:n], pin_sigmas[:n]))
            dist_sm.append(interval_distance_widths(float(lam),
                                                    *CERTIFIED[n]))
            if n == 1:
                lam1_sm = float(lam)
    check("D1 smooth world dies in pin currency",
          dist_sm[0] > 1e3 and pole_eaten < mp.mpf("1e-90"),
          "PNT prime side 1/(s-1) eats the pole EXACTLY (dev=%s); "
          "lam_min(N=1)=%.6f < 0, %.3e interval widths off"
          % (fmt(pole_eaten, 2), lam1_sm, dist_sm[0]))

    # D2: scrambled weights in pin currency
    with mp.workdps(DPS):
        w_orig = [a[3] for a in atoms_row]
        w_scr = scram_w
        rows_sc = []
        for sig in pin_sigmas[:4]:
            delta_pin = mp.mpf(0)
            for atom, ws in zip(atoms_row, w_scr):
                delta_pin += (ws - atom[3]) * mp.e ** (-sig * atom[2])
            rows_sc.append(p_pins[pin_sigmas.index(sig)] - delta_pin)
        dist_sc = []
        for n in range(1, 5):
            lam, _ = eig_range(pick_matrix(rows_sc[:n], pin_sigmas[:n]))
            dist_sc.append(interval_distance_widths(float(lam),
                                                    *CERTIFIED[n]))
        w_before = float(w_orig[0])
        w_after = float(w_scr[0])
    check("D2 scrambled world dies in pin currency",
          dist_sc[0] > 1e2
          and abs(w_before - FROZEN_WEIGHT_BEFORE) < 1e-6
          and abs(w_after - FROZEN_WEIGHT_AFTER) < 1e-6,
          "first weight %.8f -> %.8f (frozen values); lam_min(N=1) "
          "%.3e interval widths off (N=1..4: %s)"
          % (w_before, w_after, dist_sc[0],
             ", ".join("%.2e" % d for d in dist_sc)))

    # D3: Schur-currency control deaths at the frozen depths
    res_smooth = szego(row_smooth)
    res_scram = szego(row_scram)
    smooth_exit = res_smooth["fail_k"] * DELTA
    scram_exit = res_scram["fail_k"] * DELTA
    check("D3 Schur control exits at frozen depths",
          (not res_smooth["ok"])
          and abs(smooth_exit - FROZEN_SMOOTH_EXIT) <= EXIT_TOL
          and (not res_scram["ok"])
          and abs(scram_exit - FROZEN_SCRAM_EXIT) <= EXIT_TOL,
          "smooth %s at r=%.3f (frozen 0.264); scrambled %s at r=%.3f "
          "(frozen 0.744)"
          % (res_smooth["fail_kind"], smooth_exit,
             res_scram["fail_kind"], scram_exit))
    flags["G4"] = (not res_smooth["ok"]) and (not res_scram["ok"]) \
        and dist_sm[0] > 1e3 and dist_sc[0] > 1e2

    # ============================================================ E
    section("E. ADJUDICATION: gate tables, breakage register, verdict")

    print("  GATE TABLE (typed):")
    print("    gate  candidate A (BC square)         candidate B "
          "(suspension host)")
    print("    G1    PASS-TRANSCRIBING (exact)        supplied: "
          "PASS-TRANSCRIBING; anosov/selberg: DEAD at N=1")
    print("    G2    FAIL (Z1-TRANSCRIPTION fires)    supplied: FAIL "
          "(Z1); natural: source-ok but G1-dead")
    print("    G3    FAIL (cancellation not supplied) FAIL (no "
          "intersection form; same cancellation debt)")
    print("    G4    PASS (controls die as frozen)    PASS (controls die "
          "as frozen)")
    print("    G5    structural PASS / content FAIL   untwisted FAIL; "
          "PASS iff theta=1/2 == the G1 weight datum")

    typed_ok = (flags["A_G1"] and flags["A_G2_fired"] and flags["A_G3_fail"]
                and flags["A_G5_structural"] and flags["A_G5_content_fail"]
                and flags["B_G1_supplied"] and flags["B_G1_natural_dead"]
                and flags["B_G5_link"] and flags["G4"])
    glued = False  # no candidate passes G1-G5 wholesale (typed above)
    check("E1 composite typing consistent",
          typed_ok and not glued,
          "all breakage rows fire as typed; no candidate passes "
          "G1-G5 wholesale")

    wall = time.time() - T0
    check("E2 runtime", wall <= RUNTIME_BAR,
          "%.1f s <= %.0f s" % (wall, RUNTIME_BAR))

    prior = len(CHECKS)
    prior_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("E3 pattern gate",
          prior == N_CHECKS_EXPECTED - 1 and prior_pass == prior,
          "expected %d prior checks, zero fails (got %d, %d fails)"
          % (N_CHECKS_EXPECTED - 1, prior, prior - prior_pass))

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    if n_pass != len(CHECKS):
        print("VERDICT: STAGE1-INSTRUMENT-EDGE (failed gate; no "
              "mathematical verdict)")
        print("NO RH CLAIM. EXPLORATION ONLY.")
        print("=" * 78)
        return 1
    print("VERDICT: STAGE1-BREAKAGE-LOCATED(")
    print("  BRK-A1-CROSSTERMS: positivity needs %.2f digits of "
          "cross-piece cancellation" % float(cancel_digits_4))
    print("    at N=4; the direct-sum glue supplies 0;")
    print("  BRK-A2-Z1TRANSCRIPTION: the exact BC prime trace is the "
          "cache partial sum;")
    print("  BRK-A3-SPECTRUMCOUNT: BC counts e^T vs (T/2pi)log(T/2pi), "
          "ratio %.1e at T=20;" % ratios[1])
    print("  BRK-B1-HALFDENSITY: anosov %.2e / selberg %.2e certified "
          "widths off at N=1;" % (dist_nat[0], dist_sel[0]))
    print("    theta pinned to |theta-1/2| <~ %.2e (binding rung N=%d);"
          % (theta_bind, theta_rung))
    print("  BRK-B2-ARCHGERM: germ glues analytically (quad rel %s) but "
          "counterterm +" % fmt(max(germ_devs), 2))
    print("    place constant are supplied; |delta_c| <~ %.2e (binding "
          "rung N=%d);" % (const_bind, const_rung))
    print("  BRK-COMMON-FORCING: nothing in either candidate forces the "
          "half-density")
    print("    twist, the counterterm, or the cross-term state.)")
    print()
    print("SHARPENED STAGE-1 MILESTONE (beyond the roadmap's M1a/M1b):")
    print("  the host must FORCE, as theorems of one structure:")
    print("  (i)   the half-form transverse datum |det(I-P^m)|^{-1/2} "
          "(theta = 1/2,")
    print("        pinned to %.2e by the frozen instrument) JOINTLY in "
          "weights and" % theta_bind)
    print("        generator -- the round-113 duality row Theta+Theta*=I "
          "IS this datum;")
    print("  (ii)  the archimedean degenerate orbit with germ "
          "e^{-su}/(1-e^{-2u}),")
    print("        canonical counterterm e^{-2u}/(2u) and place constant "
          "-log(pi)/2")
    print("        (slack pinned to %.2e, binding rung N=%d);"
          % (const_bind, const_rung))
    print("  (iii) a state/intersection form whose cross terms deliver "
          ">= %.1f digits" % float(cancel_digits_4))
    print("        of exact cancellation at N=4 (growing along the "
          "ladder) STRUCTURALLY;")
    print("  (iv)  autonomy under the Z1 screen: the readout must resum "
          "the tail")
    print("        (Krein-carrier benchmark), not transcribe the "
          "Dirichlet source.")
    print()
    print("NO RH CLAIM. EXPLORATION ONLY. A located breakage is a "
          "specification,")
    print("not progress on RH; Stage 1 remains OPEN.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
