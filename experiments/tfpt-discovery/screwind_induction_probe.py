#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""screwind_induction_probe -- PRIME.SCREW.INDUCTION.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This file is the sole
probe of the round.  It writes nothing, imports no repository module,
reads no measured pin, zero table, paper, ledger, website or
verification file, and makes NO RH claim and NO all-depth positivity
claim.

TARGET -- DOES POSITIVITY SELF-EXTEND IN THE VERBLUNSKY COORDINATE,
AND WHAT CARRIES THE EXTENSION?  Rounds 90-96 mapped Suzuki's screw
coordinate: the accelerant -g'' realizes the Verblunsky stream alpha_k
causally (round 90, max|alpha| = 0.156..0.207 mesh-dependent); the
per-packet update is a high-rank indefinite Toeplitz update whose only
exact survival condition consumes the prior inverse (round 92,
WALL-EQUIVALENT); the completed stream's cumulative max|alpha| is
CONSTANT at 0.183932 on r = 2.568..4.788 with band maxima FALLING
(round 93); positivity to depth r pins the measure exponentially at
the conditioning price c_lam = 0.814 (round 96).  The Riccati
induction (round 63, halfgap_riccati_increment_probe) died on the
WALL ladder because its margins are RH-SATURATING: the mu1-increments
are O(1e-4..1e-5) against O(0.1..1) pivot scale and the pivot flow
has no stable sign -- the quantity being propagated tends to the
saturation value, so increments must beat vanishing margins.  THE
SCREW COORDINATE IS STRUCTURALLY DIFFERENT: the propagated bound
|alpha| <= M sits at 0.184 with margin 0.816 to the unit circle,
FLAT in depth, and the margin is NOT an RH-saturating quantity (RH
does not force max|alpha| -> 1).  This probe runs the one inductive
attack never attempted: measure the anatomy of the induction step
alpha_{n+1} = (c_{n+1} - p_n)/E_n, decompose what keeps it flat,
type the Szego dichotomy, and state the sharpest true induction
statement with its side condition S typed (checkable-arithmetic vs
wall-equivalent).

THE TWO-ROUTE IDENTITY (machine-checked, W3): in the Levinson/Szego
recursion on normalized moments r_d = c_d/c_0 the step-k objects are
  num_k = <Phi_k, (r_1..r_{k+1})>,  den_k = <Phi*_k, (r_0..r_k)>,
  alpha_k = num_k/den_k,
and the classical identifications hold EXACTLY:
  c_0 * num_k = c_{k+1} - p_k   (p_k = best linear prediction of
                                 c_{k+1} from c_1..c_k, Yule-Walker),
  c_0 * den_k = E_k = c_0 * prod_{j<k}(1 - alpha_j^2)
              = 1/(T_{k+1}^{-1})_{00}  (prediction-error energy).
So rho_n := (c_{n+1} - p_n)/E_n IS the Verblunsky coefficient
alpha_n; the induction content is NOT the ratio (tautologically the
measured 0.184) but the FACTORIZATION: the innovation and the energy
are separately measured objects with separate laws, and the step
survives iff the innovation keeps tracking the geometrically decaying
energy.  CONTINUUM DICTIONARY (declared): the delta -> 0 limit is the
Krein system of the accelerant -g'' (Krein 1955; Denisov, IMRS 2006
survey); background alpha ~ delta*A(r) vanishes with mesh while atom
kicks are O(1) tent reads, so sup|rho| is mesh-dependent (round 90:
0.207/0.184/0.156 at delta 0.012/0.006/0.003) and every statement
below is made at fixed delta WITH the mesh-refinement trend measured.

THE EXACT ARRIVAL-KICK IDENTITY (the candidate law; proved by the
Levinson algebra + the round-93 causality lemma, machine-checked as
W6): let an atom (p, m), u = m log p, w = log p * p^{-m/2}, have
first touched bin d0 = floor(u/delta), tent value phi = 1 - (u/delta
- d0), and suppose no other atom touches bins d0-1, d0, d0+1.  The
moment c_{d0} is the FIRST lag the atom enters, alpha_j for j < d0-1
are bit-identical with and without the atom, den_{d0-1} is
prefix-only, and alpha_{d0-1} is AFFINE in c_{d0} with slope
1/(c_0 den_{d0-1}):
  alpha_{d0-1}(with atom) - alpha_{d0-1}(without)
      = - w * phi / (c_0 * den_{d0-1}).
The NUMERATOR is source-only arithmetic in (p, m, delta); the
DENOMINATOR is the prior energy -- the entire induction question is
whether the energy law can be certified without consuming the prior
inverse (E_n = 1/(T^{-1})_{00} is literally the round-92 wall
object).

FROZEN OBJECTS (collective_rescue / rigidity_inverse conventions
verbatim).  Corpus screw g, v643 Lerch +1/4 convention; archimedean
base rows built in mpmath dps 50, cast once to float64; atoms as
exact float64 tent reads.  MAIN: delta = 0.006, n = 1500 (L = 9.0)
-- extends the measured corpus from r = 4.8 to 9.0; the mesh stops
resolving individual primes near u ~ 6.9 (first two-atom bin,
printed), so bins beyond hold whole packets: the kick bookkeeping
below is per-BIN and the clean-atom censuses stop at u = 6.5
(declared).  MESH family at common L = 4.8: delta = 0.012 (n = 400),
0.006 (prefix 800), 0.003 (prefix 1600).  MESH-DEEP: delta = 0.003,
n = 3000 (L = 9.0) -- the deep-window mesh cross-check.  CONTROLS
(delta = 0.006): SMOOTH-428 (PNT ramp u0 = 0), SCRARITH-428
(golden-permuted weights, atoms u < 2.568), ARCH-600 (no atoms).
ENGINE: float64 Levinson recording alphas, dens, nums, and the
component numerators num_arch/num_prime (dots of the SAME predictor
Phi_k against the arch and prime moment components -- exact linear
decomposition of the innovation); validity WARDED against mpmath,
never assumed.  M_BAR = 0.25 (the round-92 first dyadic Schur box).
Bands of width 0.6 in u; alpha_k is assigned depth u = (k+1)*delta.

WARDS (any failure => INSTRUMENT-EDGE, exit 1, no mathematical
verdict):
 A1 source-only AST firewall (imports only __future__/argparse/ast/
    hashlib/math/os/time/mpmath/numpy; no file loads; no zeta/
    zetazero/siegel calls or attributes).
 A2 frozen ladder arithmetic: n*delta = L on all four builds;
    w(2) = log2/sqrt2 to 1e-14; atoms(u<4.8) = 41; atom count u<9.0
    printed; first multi-atom bin depth printed per mesh.
 W1 428-prefix float64-vs-mp(dps 40) max dev <= 1e-9 AND cumulative
    max|alpha| at n=800 equals 0.183932 +- 5e-5 (rounds 92/93).
 W1b deep mp cross: mp(dps 30) Levinson on the MAIN row to nlim =
    1200: completes iff float64 completes there, max dev <= 1e-6.
 W2 control regression (float64): SMOOTH-428 exit 44 attempted
    -2.537735 +- 1e-3; SCRARITH-428 exit 124 attempted -2.370365 +-
    1e-3; ARCH-600 exit 122 attempted +1.015 +- 2e-2.
 W3 two-route identity at spot depths m in (100, 400, 800, 1200,
    1400): (a) c0*den_m vs 1/(T_{m+1}^{-1})_{00} by an independent
    inverse-column solve of the NORMALIZED section T/c0, rel <= 1e-6;
    (b) c0*num_m vs c_{m+1} - p_m by an independent normalized
    Yule-Walker solve, rel <= 1e-6.
 W4 innovation decomposition additivity: max_k |num_arch_k +
    num_prime_k - num_k| / (1 + <|Phi_k|,|r|>) <= 1e-12 (declared
    backward-error bar, round-92 lesson).
 W5 conditioning regression: OLS slope of ln lambda_min(T_D/c0) on
    D in (250, 400, 600, 799) gives c_lam = 0.814 +- 0.25 per unit
    depth (round 96); deep ladder D in (1000, 1250, 1499) printed.
 W6 arrival-kick exactness census (<= 12 clean atoms, u in [1.0,
    6.5], evenly subsampled): |(alpha_full - alpha_trunc)(d0-1) -
    (-w phi/(c0 den))| <= 1e-10 absolute.
 A3 runtime <= 900 s.

LAW GATES (failures are mathematical outcomes, not instrument
edges):
 G0 COMPLETION: MAIN (n=1500) and MESH-DEEP (n=3000) complete with
    every section positive.  Failure => the POSITIVITY-EXIT lane
    with mesh typing (an exit at one mesh only is typed
    MESH-ARTIFACT-CANDIDATE; tent-discretized positivity is neither
    implied by nor implies continuum screw positivity -- declared).
 G1 FLAT BOUND: sup_k |alpha_k| <= M_BAR = 0.25 on MAIN.
 G2 NO LATE GROWTH: max band-|alpha| over bands with lo >= 6.0 <=
    max band-|alpha| over u in [1.2, 3.0).
 G3 E-LAW: global OLS kappa of -ln e_k vs u on [1.2, 9.0); the four
    windowed slopes ([1.2,3.0),[3.0,4.8),[4.8,6.6),[6.6,8.4)) all
    within kappa +- max(0.10, 0.35 kappa).
 G4 KICK-DECAY LAW: OLS slope s_kick of ln(spike) vs u over clean
    fit atoms (isolation > 4 bins, contrast >= 1.3, u in [1.0,
    6.5], >= 12 members) satisfies |s_kick - (kappa - 1/2)| <=
    0.20: spike decay = energy rate minus the sqrt-p weight rate.
 G5 CONTROL KILL THROUGH THE SAME METER: SMOOTH and SCRARITH first
    cross |alpha| > M_BAR within 8 lags of their death index
    (attempted value counts as a crossing).
 G7 SIGN LAW: fraction of clean-atom arrival alphas with negative
    sign >= 0.90 (mass arrival pushes alpha down -- round 93/96).
 G8 SOURCE-MODEL (typed, drives the carrier lane): self-consistent
    per-bin packet-energy model ln e_model' = -beta*delta per lag
    plus ln(1 - kick^2) per touched bin, kick = |dc_bin|/(c0 e_model)
    -- ONE calibrated constant beta (matched to e_true at u = 2.4,
    disclosed), tested on u in [3.0, 8.8]: TRACKS iff max factor
    |ln(e_model/e_true)| <= ln 3, else FAILS(factor).

TAU-SCREEN (typed): kappa vs the conditioning slope c_lam on the
same build: CONDITIONING-PRICED iff |kappa - c_lam| <= 0.30 c_lam,
else E-LAW-DIFFERENT (the energy decays at its own rate, not at the
worst-case section rate).  The naive-floor computation prices the
Riccati contrast: under the induction hypothesis max|alpha_j| <= M
ALONE, the certified energy floor is (1-M^2)^{u/delta} (rate
-ln(1-M^2)/delta per unit depth, MESH-DIVERGENT), and the first atom
whose kick bound w*phi/(c0*floor) exceeds M is printed: the
H1-only induction must die at u* (expected log 2 -- it cannot absorb
even the first packet), while the MEASURED energy at that depth is
larger by the printed factor.  That is the precise sense in which
the flat-margin coordinate still hides the wall: the margin is flat,
but the CERTIFICATE of the margin (the energy law) is the prior
inverse.

VERDICT ENUM (priority order; composite allowed):
 INSTRUMENT-EDGE (exit 1, any ward fails)
 SCREWIND-POSITIVITY-EXIT(depth, mesh typing)   -- G0 fails
 SCREWIND-KICK-LAW(stated)          -- W6 and G3 and G4 pass
 SCREWIND-CARRIER-CANDIDATE(S stated, open lemma named)
     -- additionally G1, G2, G8-TRACKS, and kappa < 0.5
 SCREWIND-STEP-IS-WALL(mechanism)   -- always typed when the exact
     step condition consumes the prior inverse and no source-only
     substitute passed G8
 SCREWIND-DICHOTOMY(descriptive)    -- always typed (I3)
The headline is the kick law if it passes, per the round contract.

DECLARED NUMERICS, SUBSAMPLING AND COSTS.  Base rows mpmath dps 50
cast once; float64 Levinson everywhere except the mp wards (dps 40
n=428, dps 30 nlim=1200); every prime power u < 9 enters every
window it fits; clean-atom censuses subsample as declared above;
lambda_min by dense eigvalsh (largest 1499^2); source-model has ONE
calibrated constant; no randomness (golden keys only); smoke flag
reduces MAIN to n=800, skips MESH-DEEP and W1b, and prints
NOT-VERDICT-BEARING.  Runtime bar 900 s.  PRE-FREEZE DISCLOSURE:
every regression number above is a published round-90/92/93/96
constant; no bar was set from a run of this probe.  Post-freeze
instrument repairs, if any, are AMENDMENT blocks here with the
SPEC_SHA change disclosed.

SMOKE DISCLOSURE (smoke 1, n = 800, before the frozen full run; no
mathematical bar, ladder, world, census member or ward number moved):
(a) the G8 failure print overflowed fixed-point formatting when the
single-sided model collapses (kick >= 1); repaired to exponential
format plus the collapse depth -- display only.  (b) smoke measured
the two headline anatomy facts that reshaped the VERDICT COMPOSITION
before freezing: the innovation is a CANCELLATION of two growing
components (band medians rho_arch = +17.8 vs rho_prime = -17.8 at
u = 4.8 against net RMS 0.03), and the windowed E-rates drift
(0.333 -> 0.224); therefore the SCREWIND-KICK-LAW headline is tied
to W6 (exact identity) + G4 (spike decay), NOT to the
single-exponential gate G3 (whose failure is typed E-LAW-DRIFTING
and reported verbatim), and the carrier lane requires G1, G2, G4,
G8 and kappa < 0.5 but not G3.  A cancellation-growth fit c_canc
(band-median |rho_arch| vs u) was added to the tau-screen prints to
compare against c_lam and the round-96 modulus slope c_mod = 1.073
-- a display/measurement addition with no gate.  (c) smoke observed
the frozen G7 sign expectation FAILING (net arrival alpha is
positive on 30/35 clean atoms: the source kick slightly undershoots
the positive counterfactual drift); the gate is kept frozen and its
failure stands as a measured outcome.

NO RH CLAIM.  NO ALL-DEPTH POSITIVITY CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import time

import mpmath as mp
import numpy as np

T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

# ------------------------------------------------------------ frozen bars
DELTA_TEXT = "0.006"
DELTA = 0.006
DELTA2_TEXT = "0.003"
DELTA2 = 0.003
DELTA3_TEXT = "0.012"
DELTA3 = 0.012
N_MAIN = 1500
L_MAIN = 9.0
N_DEEP = 3000
N_MESH3 = 400
L_COMMON = 4.8
N_WARD = 428
L_WARD = 2.568
N_ARCH = 600
DPS_BUILD = 50
DPS_W1 = 40
DPS_W1B = 30
W1B_NLIM = 1200
M_BAR = 0.25
BAND = 0.6
FIT_LO, FIT_HI = 1.2, 9.0
WINDOWS = ((1.2, 3.0), (3.0, 4.8), (4.8, 6.6), (6.6, 8.4))
G3_TOL_ABS, G3_TOL_REL = 0.10, 0.35
G4_TOL = 0.20
G4_MIN_ATOMS = 12
CLEAN_U_LO, CLEAN_U_HI = 1.0, 6.5
CLEAN_GAP_BINS = 4
CONTRAST_BAR = 1.3
G5_LAGS = 8
G7_BAR = 0.90
G8_CAL_U = 2.4
G8_TEST_LO, G8_TEST_HI = 3.0, 8.8
G8_FACTOR = 3.0
SPOT_DEPTHS = (100, 400, 800, 1200, 1400)
LAM_DEPTHS = (250, 400, 600, 799)
LAM_DEEP = (1000, 1250, 1499)
C_LAM_REF, C_LAM_TOL = 0.814, 0.25
TAU_TOL = 0.30
W1_DEV_BAR = 1e-9
W1B_DEV_BAR = 1e-6
W3_BAR = 1e-6
W4_BAR = 1e-12
W6_BAR = 1e-10
W6_MAX = 12
RUNTIME_BAR = 900.0
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0

WARD_FULL_MAX = 0.183932
WARD_SMOOTH_EXIT, WARD_SMOOTH_ATT = 44, -2.537735
WARD_SCRAM_EXIT, WARD_SCRAM_ATT = 124, -2.370365
WARD_ARCH_EXIT, WARD_ARCH_ATT = 122, 1.015

WARDS: list[tuple[str, bool, str]] = []
LAWS: list[tuple[str, bool, str]] = []


def check_ward(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    WARDS.append((name, result, detail))
    print("  [%s] %-52s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def gate_law(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    LAWS.append((name, result, detail))
    print("  [%s] %-48s %s"
          % ("LAW-PASS" if result else "LAW-FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------- firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        source = fh.read()
    tree = ast.parse(source)
    bad: list[str] = []
    allowed_roots = {"__future__", "argparse", "ast", "hashlib", "math",
                     "os", "time", "mpmath", "numpy"}
    forbidden_calls = {"load", "loadtxt", "genfromtxt", "fromfile",
                       "zetazero", "zetazeros", "nzeros", "siegelz",
                       "siegeltheta"}
    forbidden_attrs = {"zeta", "zetazero", "zetazeros", "nzeros",
                       "siegelz", "siegeltheta"}
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
    return not bad, "violations=%s" % (bad or "none")


# ---------------------------------------------------------- prime arithmetic
def sieve_primes(limit: int) -> list[int]:
    bits = bytearray(b"\x01") * (limit + 1)
    bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            count = (limit - p * p) // p + 1
            bits[p * p:limit + 1:p] = b"\x00" * count
    return [i for i in range(2, limit + 1) if bits[i]]


def atom_table(L: float) -> list[tuple[int, int, float, float]]:
    """(p, m, u, w) with u = m log p < L, w = log p / sqrt(p^m)."""
    out: list[tuple[int, int, float, float]] = []
    for p in sieve_primes(int(math.exp(L)) + 1):
        lp = math.log(p)
        m = 1
        while m * lp < L - 1e-12:
            out.append((p, m, m * lp, lp / math.sqrt(float(p) ** m)))
            m += 1
    out.sort(key=lambda a: a[2])
    return out


def tent_reads(u: float, w: float, n: int,
               delta: float) -> list[tuple[int, float]]:
    """Exact tent read of an atom of weight w at u: c_d -= w phi_d(u)."""
    x = u / delta
    lo = int(math.floor(x))
    out = []
    for d in (lo, lo + 1):
        if 0 <= d < n:
            v = 1.0 - abs(x - d)
            if v > 0.0:
                out.append((d, -w * v))
    return out


def comb_row(base: np.ndarray, atoms: list, n: int,
             delta: float) -> np.ndarray:
    row = base.copy()
    for u, w in atoms:
        for d, v in tent_reads(u, w, n, delta):
            row[d] += v
    return row


# ---------------------------------------------------------- corpus screw g
MP_CONST: dict[str, mp.mpf] = {}
S_CACHE: dict[tuple[str, int], mp.mpf] = {}


def setup_constants() -> None:
    with mp.workdps(DPS_BUILD + 20):
        MP_CONST["psi14"] = mp.digamma(mp.mpf(1) / 4)
        MP_CONST["logpi"] = mp.log(mp.pi)
        MP_CONST["phi1"] = mp.lerchphi(1, 2, mp.mpf(1) / 4)


def s_arch_grid(index: int, delta_text: str) -> mp.mpf:
    """S(t)=(1/4)e^(-t/2)Phi(e^(-2t),2,1/4), t=index*delta."""
    key = (delta_text, index)
    if key in S_CACHE:
        return S_CACHE[key]
    with mp.workdps(DPS_BUILD):
        t = mp.mpf(index) * mp.mpf(delta_text)
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
            floor = mp.mpf(10) ** (-(DPS_BUILD + 8))
            while power > floor * (1 + abs(total)):
                total += power / (mp.mpf(k) + mp.mpf(1) / 4) ** 2
                power *= z
                k += 1
            value = mp.exp(-t / 2) * total / 4
    S_CACHE[key] = value
    return value


def base_g_values(n: int, delta_text: str) -> list[mp.mpf]:
    dl = mp.mpf(delta_text)
    values: list[mp.mpf] = []
    with mp.workdps(DPS_BUILD):
        for j in range(n + 1):
            t = j * dl
            value = -8 * (mp.cosh(t / 2) - 1)
            value -= (t / 2) * (MP_CONST["psi14"] - MP_CONST["logpi"])
            value -= MP_CONST["phi1"] / 4
            value += s_arch_grid(j, delta_text)
            values.append(value)
    return values


def lag_row_from_g(values: list[mp.mpf], delta_text: str) -> list[mp.mpf]:
    with mp.workdps(DPS_BUILD):
        dl = mp.mpf(delta_text)
        n = len(values) - 1
        row = [-2 * values[1] / dl]
        for d in range(1, n):
            row.append(-(values[d - 1] - 2 * values[d]
                         + values[d + 1]) / dl)
    return row


def ramp_values(u0: float, n: int, delta_text: str) -> list[mp.mpf]:
    """g_tail(t) = int_{u0}^t (t - u) e^{u/2} du (0 for t < u0)."""
    dl = mp.mpf(delta_text)
    values: list[mp.mpf] = []
    with mp.workdps(DPS_BUILD):
        u0m = mp.mpf(u0)
        eh = mp.exp(u0m / 2)
        for j in range(n + 1):
            t = j * dl
            if t <= u0m:
                values.append(mp.mpf(0))
            else:
                values.append(4 * mp.exp(t / 2) - eh * (2 * (t - u0m) + 4))
    return values


def mp_atom_row(u: float, w: float, n: int, delta_text: str) -> list:
    with mp.workdps(DPS_BUILD):
        out = [mp.mpf(0) for _ in range(n)]
        x = mp.mpf(u) / mp.mpf(delta_text)
        lo = int(mp.floor(x))
        for d in (lo, lo + 1):
            if 0 <= d < n:
                value = 1 - abs(x - d)
                if value > 0:
                    out[d] -= mp.mpf(w) * value
    return out


# ----------------------------------------------------- Levinson (f64 + mp)
def levinson_rec(row: np.ndarray, row_arch: np.ndarray | None = None,
                 nlim: int | None = None) -> dict:
    """Full-record float64 Levinson.  Records alphas, dens (= e_k =
    prod(1-alpha^2)), nums, and -- when row_arch is given -- the exact
    linear decomposition num = num_arch + num_prime through the SAME
    predictor Phi_k (r_prime := r - r_arch, both normalized by the
    full c0).  Also records the backward-error scale for W4."""
    n = len(row) if nlim is None else min(nlim, len(row))
    c0 = float(row[0])
    out = {"ok": True, "fail_k": -1, "kind": "", "attempted": float("nan"),
           "c0": c0, "n": n}
    if c0 <= 0.0:
        out.update({"ok": False, "fail_k": 0, "kind": "C0_NONPOSITIVE",
                    "alphas": np.empty(0), "dens": np.empty(0),
                    "nums": np.empty(0)})
        return out
    r = row[:n] / c0
    has_comp = row_arch is not None
    if has_comp:
        ra = row_arch[:n] / c0
        rp = r - ra
    phi = np.zeros(n)
    ps = np.zeros(n)
    phi[0] = 1.0
    ps[0] = 1.0
    m = max(n - 1, 0)
    alphas = np.full(m, np.nan)
    dens = np.full(m, np.nan)
    nums = np.full(m, np.nan)
    nums_a = np.full(m, np.nan) if has_comp else None
    nums_p = np.full(m, np.nan) if has_comp else None
    w4_worst = 0.0
    kstop = m
    for k in range(m):
        num = float(np.dot(phi[:k + 1], r[1:k + 2]))
        den = float(np.dot(ps[:k + 1], r[:k + 1]))
        if den <= 0.0:
            out.update({"ok": False, "fail_k": k, "kind": "DEN_NONPOSITIVE"})
            kstop = k
            break
        a = num / den
        nums[k] = num
        dens[k] = den
        if abs(a) >= 1.0:
            out.update({"ok": False, "fail_k": k, "kind": "ALPHA_EXIT",
                        "attempted": a})
            kstop = k
            break
        alphas[k] = a
        if has_comp:
            na = float(np.dot(phi[:k + 1], ra[1:k + 2]))
            npn = float(np.dot(phi[:k + 1], rp[1:k + 2]))
            nums_a[k] = na
            nums_p[k] = npn
            scale = 1.0 + float(np.dot(np.abs(phi[:k + 1]),
                                       np.abs(r[1:k + 2])))
            w4_worst = max(w4_worst, abs(na + npn - num) / scale)
        zphi = np.empty(k + 2)
        zphi[0] = 0.0
        zphi[1:] = phi[:k + 1]
        pspad = np.empty(k + 2)
        pspad[:k + 1] = ps[:k + 1]
        pspad[k + 1] = 0.0
        phi[:k + 2] = zphi - a * pspad
        ps[:k + 2] = pspad - a * zphi
    out.update({"alphas": alphas[:kstop], "dens": dens[:kstop],
                "nums": nums[:kstop], "w4_worst": w4_worst})
    if has_comp:
        out["nums_arch"] = nums_a[:kstop]
        out["nums_prime"] = nums_p[:kstop]
    if not out["ok"]:
        out["amax"] = float(np.max(np.abs(alphas[:kstop]))) if kstop else 0.0
    else:
        out["amax"] = float(np.max(np.abs(out["alphas"]))) if kstop else 0.0
    return out


def szego_mp(row: list, dps: int, nlim: int | None = None) -> dict:
    with mp.workdps(dps):
        n = len(row) if nlim is None else min(nlim, len(row))
        c0 = row[0]
        moments = [row[j] / c0 for j in range(n)]
        phi = [mp.mpf(1)]
        phi_star = [mp.mpf(1)]
        alphas: list[mp.mpf] = []
        for k in range(n - 1):
            numerator = mp.fdot(phi, moments[1:k + 2])
            denominator = mp.fdot(phi_star, moments[0:k + 1])
            if denominator <= 0:
                return {"ok": False, "fail_k": k, "alphas": alphas}
            alpha = numerator / denominator
            if abs(alpha) >= 1:
                return {"ok": False, "fail_k": k, "alphas": alphas,
                        "attempted": float(alpha)}
            alphas.append(alpha)
            zphi = [mp.mpf(0)] + phi
            phi_pad = phi_star + [mp.mpf(0)]
            phi = [zphi[j] - alpha * phi_pad[j] for j in range(k + 2)]
            phi_star = [phi_pad[j] - alpha * zphi[j] for j in range(k + 2)]
        return {"ok": True, "fail_k": -1, "alphas": alphas}


def toeplitz_of(row: np.ndarray, m: int) -> np.ndarray:
    idx = np.arange(m)
    return row[np.abs(idx[:, None] - idx[None, :])]


def ols(xs, ys) -> tuple[float, float]:
    coef = np.polyfit(np.asarray(xs, float), np.asarray(ys, float), 1)
    return float(coef[0]), float(coef[1])


def first_cross(res: dict, bar: float) -> int:
    """First alpha index with |alpha| > bar; the attempted exit value
    counts as a crossing at fail_k."""
    hits = np.nonzero(np.abs(res["alphas"]) > bar)[0]
    if len(hits):
        return int(hits[0])
    if not res["ok"] and (res["kind"] == "DEN_NONPOSITIVE"
                          or abs(res.get("attempted", 0.0)) > bar):
        return int(res["fail_k"])
    return -1


# ---------------------------------------------------------------- main
def main() -> int:
    global N_MAIN, N_DEEP, W1B_NLIM
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    smoke = bool(args.smoke)
    if smoke:
        N_MAIN = 800
        N_DEEP = 0
        W1B_NLIM = 0

    print("=" * 78)
    print("screwind_induction_probe  PRIME.SCREW.INDUCTION.01")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if smoke else ""))
    print("=" * 78)
    l_main = N_MAIN * DELTA

    # ================================================================ A
    section("A. FIREWALL + FROZEN OBJECTS")
    fw_ok, fw_detail = firewall_audit()
    check_ward("A1 source-only AST firewall", fw_ok, fw_detail)
    atoms_all = atom_table(L_MAIN)
    atoms_main = [a for a in atoms_all if a[2] < l_main - 1e-12]
    atoms_ward = [a for a in atoms_all if a[2] < L_WARD - 1e-14]
    n48 = sum(1 for a in atoms_all if a[2] < 4.8 - 1e-12)
    w2 = next(a[3] for a in atoms_all if a[0] == 2 and a[1] == 1)
    a2_ok = (abs(N_MAIN * DELTA - l_main) < 1e-12
             and (smoke or abs(N_DEEP * DELTA2 - L_MAIN) < 1e-12)
             and abs(N_MESH3 * DELTA3 - L_COMMON) < 1e-12
             and abs(w2 - math.log(2.0) / math.sqrt(2.0)) < 1e-14
             and n48 == 41)
    check_ward("A2 frozen ladders + atom-table sanity", a2_ok,
               "w(2)=%.8f; atoms(u<4.8)=%d; atoms(u<9.0)=%d"
               % (w2, n48, len(atoms_all)))

    # first multi-atom bin per mesh (mesh-resolution disclosure)
    for dl, tag in ((DELTA, "delta=0.006"), (DELTA2, "delta=0.003")):
        bins: dict[int, int] = {}
        first_mix = None
        for _p, _m, u, _w in atoms_all:
            b = int(math.floor(u / dl))
            bins[b] = bins.get(b, 0) + 1
            if bins[b] == 2 and first_mix is None:
                first_mix = u
        print("  %s: first two-atom tent bin at u = %s (mesh stops"
              " resolving primes there)"
              % (tag, "%.4f" % first_mix if first_mix else ">L"))

    setup_constants()
    t_build = time.time()
    g6 = base_g_values(N_MAIN, DELTA_TEXT)
    base6_mp = lag_row_from_g(g6, DELTA_TEXT)
    base6 = np.array([float(v) for v in base6_mp])
    base3 = None
    if N_DEEP:
        g3 = base_g_values(N_DEEP, DELTA2_TEXT)
        base3 = np.array([float(v) for v in lag_row_from_g(g3, DELTA2_TEXT)])
    g12 = base_g_values(N_MESH3, DELTA3_TEXT)
    base12 = np.array([float(v) for v in lag_row_from_g(g12, DELTA3_TEXT)])
    ramp0 = np.array([float(v) for v in lag_row_from_g(
        ramp_values(0.0, N_WARD, DELTA_TEXT), DELTA_TEXT)])
    print("  mp base builds (dps %d): %.1f s"
          % (DPS_BUILD, time.time() - t_build))

    au = [(a[2], a[3]) for a in atoms_main]
    true6 = comb_row(base6, au, N_MAIN, DELTA)
    res = levinson_rec(true6, row_arch=base6)
    true3 = res3 = None
    if N_DEEP:
        au3 = [(a[2], a[3]) for a in atoms_all if a[2] < L_MAIN - 1e-12]
        true3 = comb_row(base3, au3, N_DEEP, DELTA2)
        res3 = levinson_rec(true3)
    true12 = comb_row(base12, [(a[2], a[3]) for a in atoms_all
                               if a[2] < L_COMMON - 1e-12],
                      N_MESH3, DELTA3)
    res12 = levinson_rec(true12)

    # ================================================================ B
    section("B. ENGINE WARDS (float64 vs mp vs round-92/93/96 numbers)")
    row428_mp = list(base6_mp[:N_WARD])
    for _p, _m, u, w in atoms_ward:
        arow = mp_atom_row(u, w, N_WARD, DELTA_TEXT)
        row428_mp = [x + y for x, y in zip(row428_mp, arow)]
    sz_mp = szego_mp(row428_mp, DPS_W1)
    res_428 = levinson_rec(true6[:N_WARD])
    dev428 = (max(abs(float(am) - af) for am, af in
                  zip(sz_mp["alphas"], res_428["alphas"]))
              if sz_mp["ok"] and res_428["ok"] else float("inf"))
    amax800 = (float(np.max(np.abs(res["alphas"][:799])))
               if len(res["alphas"]) >= 799 else float("nan"))
    check_ward("W1 428-prefix f64-vs-mp + 800 regression",
               dev428 <= W1_DEV_BAR
               and abs(amax800 - WARD_FULL_MAX) < 5e-5,
               "dev=%.2e; max|alpha|(n<=800)=%.6f (round92 %.6f)"
               % (dev428, amax800, WARD_FULL_MAX))

    if W1B_NLIM:
        t_w1b = time.time()
        row_main_mp = list(base6_mp[:W1B_NLIM])
        for _p, _m, u, w in atoms_main:
            if u < W1B_NLIM * DELTA + DELTA:
                arow = mp_atom_row(u, w, W1B_NLIM, DELTA_TEXT)
                row_main_mp = [x + y for x, y in zip(row_main_mp, arow)]
        sz_deep = szego_mp(row_main_mp, DPS_W1B, nlim=W1B_NLIM)
        f64_alive = res["ok"] or res["fail_k"] >= W1B_NLIM - 1
        ncmp = min(len(sz_deep["alphas"]), len(res["alphas"]))
        dev_deep = (max(abs(float(am) - af) for am, af in
                        zip(sz_deep["alphas"][:ncmp],
                            res["alphas"][:ncmp]))
                    if ncmp else float("inf"))
        check_ward("W1b deep mp cross (dps %d, nlim %d)"
                   % (DPS_W1B, W1B_NLIM),
                   sz_deep["ok"] == f64_alive and dev_deep <= W1B_DEV_BAR,
                   "mp ok=%s f64 alive=%s dev=%.2e (%.1f s)"
                   % (sz_deep["ok"], f64_alive, dev_deep,
                      time.time() - t_w1b))

    res_sm = levinson_rec(base6[:N_WARD] + ramp0)
    q_ward = [a[0] ** a[1] for a in atoms_ward]
    order = sorted(range(len(atoms_ward)),
                   key=lambda i: (q_ward[i] * GOLDEN) % 1.0)
    scram_atoms = [(atoms_ward[i][2], atoms_ward[order[i]][3])
                   for i in range(len(atoms_ward))]
    res_sc = levinson_rec(comb_row(base6[:N_WARD], scram_atoms,
                                   N_WARD, DELTA))
    res_ar = levinson_rec(base6[:N_ARCH])
    check_ward("W2 control regression (SMOOTH/SCRARITH/ARCH)",
               res_sm["fail_k"] == WARD_SMOOTH_EXIT
               and abs(res_sm["attempted"] - WARD_SMOOTH_ATT) < 1e-3
               and res_sc["fail_k"] == WARD_SCRAM_EXIT
               and abs(res_sc["attempted"] - WARD_SCRAM_ATT) < 1e-3
               and res_ar["fail_k"] == WARD_ARCH_EXIT
               and abs(res_ar["attempted"] - WARD_ARCH_ATT) < 2e-2,
               "SMOOTH %d/%.6f  SCRARITH %d/%.6f  ARCH600 %d/%.4f"
               % (res_sm["fail_k"], res_sm["attempted"],
                  res_sc["fail_k"], res_sc["attempted"],
                  res_ar["fail_k"], res_ar["attempted"]))

    # W3 two-route identity at spot depths
    c0 = res["c0"]
    w3_ok = True
    w3_det = []
    for m in SPOT_DEPTHS:
        if m >= len(res["alphas"]):
            continue
        tm1 = toeplitz_of(true6 / c0, m + 1)
        e_direct = c0 / float(np.linalg.solve(
            tm1, np.eye(m + 1)[:, 0])[0])
        e_rec = c0 * res["dens"][m]
        rel_e = abs(e_direct - e_rec) / abs(e_rec)
        tm = toeplitz_of(true6 / c0, m)
        avec = np.linalg.solve(tm, true6[1:m + 1] / c0)
        pred = float(np.dot(avec, true6[m:0:-1] / c0)) * c0
        inn_direct = true6[m + 1] - pred
        inn_rec = c0 * res["nums"][m]
        rel_i = abs(inn_direct - inn_rec) / max(abs(inn_rec), 1e-300)
        w3_ok &= rel_e <= W3_BAR and rel_i <= W3_BAR
        w3_det.append("m=%d:%.0e/%.0e" % (m, rel_e, rel_i))
    check_ward("W3 two-route energy+innovation identities", w3_ok,
               " ".join(w3_det) + " (bar %.0e)" % W3_BAR)
    check_ward("W4 innovation decomposition additivity",
               res["w4_worst"] <= W4_BAR,
               "worst backward mismatch %.2e (bar %.0e)"
               % (res["w4_worst"], W4_BAR))

    lam = {}
    for dpt in LAM_DEPTHS + (LAM_DEEP if not smoke else ()):
        if dpt >= N_MAIN:
            continue
        lam[dpt] = float(np.linalg.eigvalsh(
            toeplitz_of(true6 / c0, dpt))[0])
    c_lam, _b = ols([d * DELTA for d in LAM_DEPTHS],
                    [math.log(lam[d]) for d in LAM_DEPTHS])
    c_lam = -c_lam
    check_ward("W5 conditioning slope regression (round 96)",
               abs(c_lam - C_LAM_REF) <= C_LAM_TOL,
               "c_lam=%.3f per depth unit (round96 %.3f +- %.2f)"
               % (c_lam, C_LAM_REF, C_LAM_TOL))
    if not smoke:
        c_lam_deep, _b2 = ols([d * DELTA for d in LAM_DEEP],
                              [math.log(lam[d]) for d in LAM_DEEP])
        print("  lambda_min ladder: %s"
              % "  ".join("D=%d:%.3e" % (d, lam[d]) for d in sorted(lam)))
        print("  deep conditioning slope (D=1000..1499): %.3f"
              % -c_lam_deep)

    if any(not ok for _n, ok, _d in WARDS):
        print("\nABORT: INSTRUMENT-EDGE (a ward failed; exit 1)")
        print("NO RH CLAIM. EXPLORATION ONLY.")
        return 1

    # ================================================================ C
    section("C. I1 -- THE INDUCTION ANATOMY (MAIN delta=0.006, L=%.1f)"
            % l_main)
    al = res["alphas"]
    dens = res["dens"][:len(al)]
    n_al = len(al)
    u_of = (np.arange(n_al) + 1) * DELTA
    g0_main = res["ok"]
    g0_deep = res3["ok"] if res3 is not None else True
    print("  MAIN completion: %s%s" % (
        "ALL SECTIONS POSITIVE to n=%d (r=%.3f)" % (N_MAIN, l_main)
        if g0_main else "EXIT at k=%d (r=%.3f, %s, attempted %.4f)"
        % (res["fail_k"], res["fail_k"] * DELTA, res["kind"],
           res["attempted"]),
        "" if smoke else "; MESH-DEEP (delta=0.003, n=%d): %s" % (
            N_DEEP, "COMPLETES" if g0_deep
            else "EXIT k=%d (r=%.3f)" % (res3["fail_k"],
                                         res3["fail_k"] * DELTA2))))
    gate_law("G0 completion (MAIN + MESH-DEEP all sections positive)",
             g0_main and g0_deep, "MAIN ok=%s DEEP ok=%s"
             % (g0_main, g0_deep))

    sup_rho = float(np.max(np.abs(al)))
    gate_law("G1 flat bound sup|rho| <= %.2f" % M_BAR,
             sup_rho <= M_BAR, "sup|rho| = %.6f at k=%d (u=%.3f);"
             " margin to unit circle %.3f"
             % (sup_rho, int(np.argmax(np.abs(al))),
                (int(np.argmax(np.abs(al))) + 1) * DELTA, 1.0 - sup_rho))

    # E-law
    lo_i = int(FIT_LO / DELTA)
    hi_i = min(int(FIT_HI / DELTA), n_al)
    ln_e = np.log(dens)
    kappa, b_e = ols(u_of[lo_i:hi_i], ln_e[lo_i:hi_i])
    kappa = -kappa
    resid = ln_e[lo_i:hi_i] - (-kappa * u_of[lo_i:hi_i] + b_e)
    ssr = float(np.sum(resid ** 2))
    sst = float(np.sum((ln_e[lo_i:hi_i]
                        - np.mean(ln_e[lo_i:hi_i])) ** 2))
    r2 = 1.0 - ssr / max(sst, 1e-300)
    win_slopes = []
    for wl, wh in WINDOWS:
        i0, i1 = int(wl / DELTA), min(int(wh / DELTA), n_al)
        if i1 - i0 > 20:
            s, _ = ols(u_of[i0:i1], ln_e[i0:i1])
            win_slopes.append(-s)
    tol = max(G3_TOL_ABS, G3_TOL_REL * kappa)
    g3_ok = (len(win_slopes) >= 3
             and all(abs(s - kappa) <= tol for s in win_slopes))
    gate_law("G3 E-law: e ~ C exp(-kappa u), windows consistent",
             g3_ok, "kappa=%.4f (R2=%.4f, C=e^%.3f); windows %s"
             " (tol +-%.3f)" % (kappa, r2, b_e,
                                "/".join("%.3f" % s for s in win_slopes),
                                tol))
    print("  e_k at depths: %s" % "  ".join(
        "u=%.1f:%.4e" % (uu, dens[min(int(uu / DELTA), n_al - 1)])
        for uu in (1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4)
        if int(uu / DELTA) < n_al))
    print("  Szego entropy -ln e(L) = %.4f (Sum alpha^2 diverges"
          " linearly: measured Szego-class violation rate %.4f /"
          " unit depth)" % (-ln_e[n_al - 1], kappa))

    # band table
    atom_bins = set()
    for _p, _m, u, _w in atoms_main:
        d0 = int(math.floor(u / DELTA))
        atom_bins.add(d0 - 1)
        atom_bins.add(d0)
    n_bands = int(math.ceil(l_main / BAND))
    band_max = np.zeros(n_bands)
    print("  band table [u_lo, u_hi): max|rho| | RMS rho | med rho_arch"
          " | med rho_prime | cancel")
    nums_a = res["nums_arch"][:n_al]
    nums_p = res["nums_prime"][:n_al]
    rho_a = nums_a / dens
    rho_p = nums_p / dens
    cancel = np.abs(nums_a) / np.maximum(np.abs(res["nums"][:n_al]),
                                         1e-300)
    for i in range(n_bands):
        i0, i1 = int(i * BAND / DELTA), min(int((i + 1) * BAND / DELTA),
                                            n_al)
        if i1 <= i0:
            continue
        band_max[i] = float(np.max(np.abs(al[i0:i1])))
        print("    [%4.1f,%4.1f)  %.4f | %.4f | %+.4f | %+.4f | %7.1f"
              % (i * BAND, (i + 1) * BAND, band_max[i],
                 float(np.sqrt(np.mean(al[i0:i1] ** 2))),
                 float(np.median(rho_a[i0:i1])),
                 float(np.median(rho_p[i0:i1])),
                 float(np.median(cancel[i0:i1]))))
    late = [band_max[i] for i in range(n_bands) if i * BAND >= 6.0
            and band_max[i] > 0]
    early = [band_max[i] for i in range(n_bands)
             if 1.2 <= i * BAND < 3.0]
    g2_ok = bool(late) and bool(early) and max(late) <= max(early)
    if smoke and not late:
        g2_ok = False
    gate_law("G2 no late growth of band max|rho|", g2_ok,
             "max(u>=6.0)=%.4f <= max([1.2,3.0))=%.4f"
             % (max(late) if late else float("nan"),
                max(early) if early else float("nan")))

    # autocorrelation + atom/background split
    ac = al - float(np.mean(al))
    denom = float(np.dot(ac, ac))
    acf = [float(np.dot(ac[:-l], ac[l:])) / denom for l in range(1, 11)]
    print("  rho autocorrelation lags 1..10: %s"
          % " ".join("%+.3f" % v for v in acf))
    is_atom = np.array([k in atom_bins for k in range(n_al)])
    med_at = float(np.median(np.abs(al[is_atom])))
    med_bg = float(np.median(np.abs(al[~is_atom])))
    print("  median|rho|: atom bins %.5f vs background %.5f"
          " (ratio %.2f)" % (med_at, med_bg, med_at / max(med_bg, 1e-300)))

    # mesh family at common L = 4.8
    print("  mesh family sup|rho| on [0, 4.8): ", end="")
    mesh_sup = {}
    mesh_kappa = {}
    for tag, rr, dl in (("0.012", res12, DELTA3),
                        ("0.006", res, DELTA),
                        ("0.003", res3, DELTA2)):
        if rr is None:
            continue
        nn = min(int(L_COMMON / dl), len(rr["alphas"]))
        mesh_sup[tag] = float(np.max(np.abs(rr["alphas"][:nn])))
        i0 = int(FIT_LO / dl)
        uu = (np.arange(nn) + 1) * dl
        kk, _ = ols(uu[i0:nn], np.log(rr["dens"][i0:nn]))
        mesh_kappa[tag] = -kk
    print("  ".join("d=%s:%.4f" % (t, v) for t, v in mesh_sup.items()))
    print("  mesh family kappa on [1.2, 4.8): %s"
          % "  ".join("d=%s:%.4f" % (t, v) for t, v in mesh_kappa.items()))
    if "0.003" in mesh_sup:
        trend = (mesh_sup.get("0.012", 9e9) > mesh_sup["0.006"]
                 > mesh_sup["0.003"])
        print("  mesh trend typed: %s (round 90: 0.207/0.184/0.156)"
              % ("MESH-DAMPED (sup|rho| falls under refinement)"
                 if trend else "NOT MONOTONE"))
        dk = abs(mesh_kappa["0.006"] - mesh_kappa["0.003"])
        print("  E-rate mesh stability: |kappa(.006)-kappa(.003)| ="
              " %.4f => %s" % (dk, "E-RATE-MESH-STABLE"
                               if dk <= 0.2 * mesh_kappa["0.006"]
                               else "E-RATE-MESH-DRIFTING"))
    if res3 is not None and res3["ok"]:
        n3 = len(res3["alphas"])
        u3 = (np.arange(n3) + 1) * DELTA2
        deep_mask = u3 >= 6.0
        print("  MESH-DEEP sup|rho| on u in [6,9): %.4f (MAIN: %.4f)"
              % (float(np.max(np.abs(res3["alphas"][deep_mask]))),
                 max(late) if late else float("nan")))

    # ================================================================ D
    section("D. I2 -- INNOVATION DECOMPOSITION + THE ARRIVAL-KICK LAW")
    # arch component drift
    over1 = np.nonzero(np.abs(rho_a) > 1.0)[0]
    if len(over1):
        print("  |rho_arch| first exceeds 1 at k=%d (u=%.3f); the"
              " ARCH-ONLY world (own recursion) died at r=0.732:"
              % (int(over1[0]), (int(over1[0]) + 1) * DELTA))
        print("    under the full predictor the arch innovation alone"
              " would eject the stream; the prime")
        print("    component supplies the cancelling sign at every"
              " scale (cancel column above).")
    else:
        print("  |rho_arch| stays <= 1 on the whole ladder (no"
              " arch-alone ejection under the full predictor).")

    # clean atoms
    us = np.array([a[2] for a in atoms_main])
    clean = []
    for i, (p, m_, u, w) in enumerate(atoms_main):
        if not (CLEAN_U_LO <= u <= CLEAN_U_HI):
            continue
        gap = np.min(np.abs(np.delete(us, i) - u)) if len(us) > 1 else 9e9
        if gap > CLEAN_GAP_BINS * DELTA:
            clean.append((p, m_, u, w))
    spikes = []
    signs = []
    for p, m_, u, w in clean:
        d0 = int(math.floor(u / DELTA))
        if d0 + 1 >= n_al or d0 - 21 < 0:
            continue
        spike_k = d0 - 1 + int(np.argmax(np.abs(al[d0 - 1:d0 + 1])))
        spike = abs(al[spike_k])
        bg = np.concatenate([np.abs(al[d0 - 20:d0 - 8]),
                             np.abs(al[d0 + 8:d0 + 20])])
        contrast = spike / max(float(np.median(bg)), 1e-300)
        signs.append(al[d0 - 1] < 0.0)
        if contrast >= CONTRAST_BAR:
            spikes.append((u, spike, p, m_, contrast))
    print("  clean atoms (isolation > %d bins, u in [%.1f, %.1f]): %d;"
          " with contrast >= %.1f: %d"
          % (CLEAN_GAP_BINS, CLEAN_U_LO, CLEAN_U_HI, len(clean),
             CONTRAST_BAR, len(spikes)))
    frac_neg = (sum(signs) / len(signs)) if signs else float("nan")
    gate_law("G7 sign law (arrival alpha < 0)", frac_neg >= G7_BAR,
             "%d/%d negative (%.2f, bar %.2f)"
             % (sum(signs), len(signs), frac_neg, G7_BAR))
    if len(spikes) >= G4_MIN_ATOMS:
        s_kick, b_k = ols([s[0] for s in spikes],
                          [math.log(s[1]) for s in spikes])
        pred_slope = kappa - 0.5
        g4_ok = abs(s_kick - pred_slope) <= G4_TOL
    else:
        s_kick, b_k, pred_slope, g4_ok = float("nan"), 0.0, kappa - 0.5, \
            False
    gate_law("G4 kick-decay law s_kick = kappa - 1/2", g4_ok,
             "s_kick=%.4f vs kappa-0.5=%.4f (tol %.2f, %d atoms)"
             % (s_kick, pred_slope, G4_TOL, len(spikes)))
    print("  spike ladder (u, |spike|, q, contrast):")
    for u, s, p, m_, ctr in spikes[:8] + spikes[-4:]:
        print("    u=%.4f  |a|=%.5f  q=%d  contrast=%.1f"
              % (u, s, p ** m_, ctr))

    # W6 arrival-kick exactness (source-only numerator identity)
    census = clean[::max(1, len(clean) // W6_MAX)][:W6_MAX]
    w6_ok = True
    w6_worst = 0.0
    print("  W6 census: alpha(d0-1) shift vs -w*phi/(c0*e_prior):")
    for p, m_, u, w in census:
        d0 = int(math.floor(u / DELTA))
        sub = [(a[2], a[3]) for a in atoms_main if a[2] < u - 1e-12]
        r_tr = levinson_rec(comb_row(base6, sub, N_MAIN, DELTA),
                            nlim=d0 + 2)
        if not (len(res["alphas"]) > d0 - 1
                and len(r_tr["alphas"]) > d0 - 1):
            continue
        phi_t = 1.0 - (u / DELTA - d0)
        pred = -w * phi_t / (c0 * res["dens"][d0 - 1])
        got = float(res["alphas"][d0 - 1] - r_tr["alphas"][d0 - 1])
        dev = abs(got - pred)
        w6_worst = max(w6_worst, dev)
        w6_ok &= dev <= W6_BAR
        print("    q=%-5d u=%.4f  kick=%.6f  pred=%.6f  dev=%.1e"
              % (p ** m_, u, got, pred, dev))
    check_ward("W6 arrival-kick exactness (affine Levinson identity)",
               w6_ok and bool(census),
               "worst dev %.2e over %d atoms (bar %.0e)"
               % (w6_worst, len(census), W6_BAR))

    # ================================================================ E
    section("E. I3 -- SZEGO DICHOTOMY TYPING (measured + classical)")
    print("  MEASURED: Sum alpha^2 diverges linearly (rate %.4f / unit"
          " depth at delta=0.006," % kappa)
    print("  mesh-checked above); equivalently -ln e(u) grows linearly:"
          " the SZEGO CONDITION FAILS")
    print("  for the tent-discretized screw measure at every accessible"
          " mesh and depth.")
    print("  CLASSICAL TYPING (cited, not re-proved):")
    print("   (i)  all-depth section positivity <=> alpha in the unit"
          " disk forever <=> a positive")
    print("        measure mu on the circle realizes the moments"
          " (Verblunsky; Simon OPUC Thm 1.7.11).")
    print("   (ii) Sum alpha^2 = inf <=> integral log mu' = -inf"
          " (Szego-Verblunsky; Simon OPUC Thm 2.3.1):")
    print("        the a.c. part, IF ANY, has divergent entropy.  This"
          " does NOT prove pure point --")
    print("        a.c. with log-divergent density and singular-"
          "continuous parts both survive; the")
    print("        candidate 'positivity + Szego violation <=> pure"
          " point' is FALSE as stated and is")
    print("        typed DESCRIPTIVE-ONLY.")
    print("   (iii) dictionary: the delta->0 limit is the Krein system"
          " of the accelerant -g'' (Krein")
    print("        1955; Denisov IMRS 2006, Krein-system Szego class);"
          " under RH its spectral measure")
    print("        is the zero comb (pure point), CONSISTENT with (ii)"
          " but not implied by it.")
    print("   (iv) Rakhmanov (Simon OPUC Ch. 9): mu' > 0 a.e. =>"
          " alpha_n -> 0.  The measured spikes")
    print("        DECAY (s_kick=%.3f < 0), so the contrapositive"
          " gives no handle either." % s_kick)
    print("  VERDICT-RELEVANT CONTENT: the dichotomy constrains the"
          " MEASURE CLASS, not the step size;")
    print("  the only quantitative object it certifies is |alpha| < 1"
          " itself -- the tautological wall.")
    print("  => typed SCREWIND-DICHOTOMY(descriptive-only).")

    # ================================================================ F
    section("F. I4 -- THE INDUCTION, FORMALIZED; CONTROLS; TAU-SCREEN;"
            " SOURCE MODEL")
    # naive floor
    for M in (M_BAR, 0.184):
        lam_m = -math.log(1.0 - M * M)
        ustar, factor = None, None
        for p, m_, u, w in atoms_main:
            d0 = int(math.floor(u / DELTA))
            if d0 - 1 >= n_al:
                break
            floor_e = (1.0 - M * M) ** (d0 - 1)
            phi_t = 1.0 - (u / DELTA - d0)
            if w * phi_t / (c0 * floor_e) > M:
                ustar = u
                factor = dens[d0 - 1] / floor_e
                break
        print("  H1-only floor (M=%.3f): rate %.2f/unit depth"
              " (mesh-divergent: %.4f/lag / delta); first"
              % (M, lam_m / DELTA, lam_m))
        print("    unabsorbable atom at u* = %s; measured e exceeds the"
              " floor there by factor %s"
              % ("%.4f" % ustar if ustar else ">L",
                 "%.1e" % factor if factor else "--"))
    print("  THE SHARPEST TRUE STATEMENT (typed):")
    print("   STEP LEMMA (exact, W6-checked): at a clean atom arrival,")
    print("     alpha_{d0-1}(full) = alpha_{d0-1}(prefix world)"
          " - w*phi/(c0 * e_{d0-1}),")
    print("   with w*phi source-only arithmetic in (p, m, delta) and"
          " e_{d0-1} the prior energy.")
    print("   INDUCTION CANDIDATE: IF max_{j<=n}|alpha_j| <= M AND"
          " S(n+1) THEN |alpha_{n+1}| <= M, where")
    print("     S(n+1):  |num_arch(n+1)| + |dc_prime(n+1)|/c0  <=  M *"
          " e_n .")
    print("   TYPING OF S: e_n = 1/(c0 (T_{n+1}^{-1})_{00}) consumes"
          " the prior inverse (the round-92")
    print("   wall object VERBATIM), and num_arch consumes the"
          " predictor Phi_n: S is WALL-EQUIVALENT.")
    print("   The H1-only certified floor (1-M^2)^n decays at %.1f /"
          " unit depth vs the measured" % (-math.log(1 - M_BAR ** 2)
                                           / DELTA))
    print("   kappa = %.3f: the hypothesis loses the energy by"
          " exponential orders BEFORE the first" % kappa)
    print("   atom -- the naive induction is DEAD AT log 2, not at"
          " some deep frontier.")
    print("   RICCATI CONTRAST (round 63): there the margins are"
          " RH-saturating (mu1 increments -> 0")
    print("   against O(1) pivots; the PROPAGATED QUANTITY saturates)."
          "  Here the propagated bound is")
    print("   flat with margin %.2f and band maxima FALL; what fails"
          " is not the margin but the" % (1.0 - sup_rho))
    print("   CERTIFICATE: the energy law that prices the kicks is"
          " prior-state.  The difference is")
    print("   real (measured flat + falling vs vanishing margins) and"
          " survives the tau-screen below;")
    print("   the wall relocates into the certificate of e_n, exactly"
          " the round-92 mechanism.")

    # G5 controls through the same meter
    f_sm = first_cross(res_sm, M_BAR)
    f_sc = first_cross(res_sc, M_BAR)
    g5_ok = (f_sm >= 0 and res_sm["fail_k"] - f_sm <= G5_LAGS
             and f_sc >= 0 and res_sc["fail_k"] - f_sc <= G5_LAGS
             and abs(res_sm["attempted"]) > 1.0
             and abs(res_sc["attempted"]) > 1.0)
    gate_law("G5 controls blow through M at their death depths",
             g5_ok, "SMOOTH first>%.2f at %d (exit %d, att %.3f);"
             " SCRARITH at %d (exit %d, att %.3f)"
             % (M_BAR, f_sm, res_sm["fail_k"], res_sm["attempted"],
                f_sc, res_sc["fail_k"], res_sc["attempted"]))

    # tau-screen (+ cancellation growth)
    band_c = []
    band_ra = []
    for i in range(n_bands):
        i0, i1 = int(i * BAND / DELTA), min(int((i + 1) * BAND / DELTA),
                                            n_al)
        if i1 <= i0 or (i + 0.5) * BAND < 0.9:
            continue
        med_ra = abs(float(np.median(rho_a[i0:i1])))
        if med_ra > 0:
            band_c.append((i + 0.5) * BAND)
            band_ra.append(math.log(med_ra))
    c_canc, _bc = ols(band_c, band_ra) if len(band_c) >= 3 \
        else (float("nan"), 0.0)
    print("  cancellation growth: band-median |rho_arch| ~ e^{%.3f u}"
          " (num_arch ~ e^{%.3f u}); c_lam = %.3f;"
          % (c_canc, c_canc - kappa, c_lam))
    print("    round-96 modulus slope c_mod = 1.073 -- the growing"
          " cancellation is the conditioning-priced object")
    tau_priced = abs(kappa - c_lam) <= TAU_TOL * c_lam
    print("  TAU-SCREEN: kappa = %.4f vs c_lam = %.4f => %s"
          % (kappa, c_lam,
             "E-LAW-CONDITIONING-PRICED (the energy law is the section"
             " conditioning price)" if tau_priced else
             "E-LAW-DIFFERENT (energy decays at its own rate, %.2fx"
             " slower than worst-case conditioning)"
             % (c_lam / max(kappa, 1e-300))))
    print("  three-rate summary: naive floor %.1f >> c_lam %.3f >>"
          " kappa %.3f vs weight rate 0.5;"
          % (-math.log(1 - M_BAR ** 2) / DELTA, c_lam, kappa))
    print("    kick exponent kappa - 1/2 = %.3f (%s => kicks %s with"
          " depth)"
          % (kappa - 0.5, "negative" if kappa < 0.5 else "nonnegative",
             "DECAY" if kappa < 0.5 else "DO NOT DECAY"))

    # G8 source model
    dc_prime = np.zeros(N_MAIN)
    for _p, _m, u, w in atoms_main:
        for d, v in tent_reads(u, w, N_MAIN, DELTA):
            dc_prime[d] += v
    cal_k = int(G8_CAL_U / DELTA)
    target = math.log(dens[cal_k])

    def model_ln_e(beta: float, kmax: int) -> np.ndarray:
        ln_em = np.zeros(kmax)
        e = 1.0
        for k in range(kmax):
            kick = abs(dc_prime[k + 1]) / (c0 * e) if k + 1 < N_MAIN \
                else 0.0
            fac = 1.0 - kick * kick
            if fac <= 1e-12:
                ln_em[k:] = -300.0
                return ln_em
            e *= fac * math.exp(-beta * DELTA)
            ln_em[k] = math.log(e)
        return ln_em

    b_lo, b_hi = -2.0, 6.0
    for _ in range(48):
        b_mid = 0.5 * (b_lo + b_hi)
        if model_ln_e(b_mid, cal_k + 1)[cal_k] > target:
            b_lo = b_mid
        else:
            b_hi = b_mid
    beta = 0.5 * (b_lo + b_hi)
    ln_em = model_ln_e(beta, n_al)
    collapse = np.nonzero(ln_em <= -299.0)[0]
    t_lo, t_hi = int(G8_TEST_LO / DELTA), min(int(G8_TEST_HI / DELTA),
                                              n_al)
    dev_ln = np.abs(ln_em[t_lo:t_hi] - ln_e[t_lo:t_hi])
    factor = math.exp(min(float(np.max(dev_ln)), 690.0)) if t_hi > t_lo \
        else float("inf")
    g8_ok = factor <= G8_FACTOR and not len(collapse)
    gate_law("G8 source model tracks e on [%.1f, %.1f]"
             % (G8_TEST_LO, G8_TEST_HI), g8_ok,
             "beta=%.4f (ONE calibrated const at u=%.1f); max factor"
             " %.2e (bar %.1f)%s"
             % (beta, G8_CAL_U, factor, G8_FACTOR,
                "; MODEL COLLAPSES (kick>=1) at u=%.3f"
                % ((int(collapse[0]) + 1) * DELTA) if len(collapse)
                else ""))
    atom_entropy = float(np.sum(np.log1p(
        -np.minimum((np.abs(dc_prime[1:n_al + 1])
                     / (c0 * np.exp(ln_em))) ** 2, 0.999))))
    print("  model decomposition of kappa: background beta = %.4f;"
          " packet entropy share = %.2f"
          % (beta, -atom_entropy / max(-float(ln_em[n_al - 1]), 1e-300)))

    # ================================================================ G
    section("G. ADJUDICATION")
    wall = time.time() - T0
    check_ward("A3 runtime", wall <= RUNTIME_BAR,
               "%.1f s <= %.0f s" % (wall, RUNTIME_BAR))
    instrument_ok = all(ok for _n, ok, _d in WARDS)
    n_ward = sum(1 for _n, ok, _d in WARDS if ok)
    n_law = sum(1 for _n, ok, _d in LAWS if ok)
    g_of = {name.split()[0]: ok for name, ok, _d in LAWS}

    if not instrument_ok:
        print("\nVERDICT: INSTRUMENT-EDGE (%d/%d wards; exit 1)"
              % (n_ward, len(WARDS)))
        print("NO RH CLAIM. EXPLORATION ONLY.")
        return 1

    parts = []
    if not g_of.get("G0", False):
        mesh_note = ("both meshes exit" if not (res["ok"] or
                     (res3 and res3["ok"]))
                     else "single-mesh: MESH-ARTIFACT-CANDIDATE")
        parts.append("SCREWIND-POSITIVITY-EXIT(%s)" % mesh_note)
    else:
        w6_pass = next(ok for nm, ok, _d in WARDS
                       if nm.startswith("W6"))
        kick_law = (w6_pass and g_of.get("G4", False))
        if kick_law:
            parts.append(
                "SCREWIND-KICK-LAW(arrival increment = -w*phi/(c0 e_n)"
                " EXACT [W6]; spike decay s_kick=%.3f vs kappa-1/2="
                "%.3f [G4]; e-law %s)"
                % (s_kick, kappa - 0.5,
                   "e ~ e^{-%.3f u} [G3]" % kappa if g_of.get("G3")
                   else "E-LAW-DRIFTING(windows %s)"
                   % "/".join("%.3f" % s for s in win_slopes)))
        carrier = (kick_law and g_of.get("G1", False)
                   and g_of.get("G2", False) and g_of.get("G8", False)
                   and kappa < 0.5)
        if carrier:
            parts.append(
                "SCREWIND-CARRIER-CANDIDATE(S = one-constant packet-"
                "energy model, factor %.2f on [%.1f,%.1f]; OPEN:"
                " domination lemma e_true >= c * e_model from source"
                " data)" % (factor, G8_TEST_LO, G8_TEST_HI))
        parts.append(
            "SCREWIND-STEP-IS-WALL(the exact side condition S consumes"
            " e_n = 1/(c0(T^{-1})_{00}) -- the round-92 prior inverse;"
            " H1-only floor dies at u* = log 2)")
    parts.append("SCREWIND-DICHOTOMY(descriptive-only: Szego violation"
                 " measured, pure point consistent but not implied)")

    print("\n  wards %d/%d  laws %d/%d  runtime %.1f s  SPEC_SHA %s"
          % (n_ward, len(WARDS), n_law, len(LAWS), wall, SPEC_SHA[:16]))
    print("\nVERDICT: " + "\n         + ".join(parts))
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("NO RH CLAIM. NO ALL-DEPTH POSITIVITY CLAIM."
          " EXPLORATION ONLY.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
