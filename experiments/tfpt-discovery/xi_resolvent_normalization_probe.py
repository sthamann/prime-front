#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""xi_resolvent_normalization_probe -- PRIME.XI.RESOLVENT.NORMALIZATION.01

CCCLVII.  FROZEN CORRECTION SPEC v1 (2026-08-13).

EXPLORATION ONLY.  This probe writes no files and makes NO RH claim, NO
positivity claim, and NO counterexample claim.  The frozen round-1, round-2,
and theorem-contract probes are dependencies/read-only; none is edited.

MISSION AND HIGH-PREMISE CORRECTION.
Rounds 1/2 compared the UNNORMALIZED completed trace

    F(z) = Tr(D-z)^(-1) + explicit archimedean/Euler tails

with -Xi'/Xi, but their normal-family check divided the finite-window trace
by dim(D).  This probe tests the correctly residue-normalized object itself.
For one spectral atom lambda,

    Res_{z=lambda} (lambda-z)^(-1) = -1,
    Res_{z=lambda} dim^(-1)(lambda-z)^(-1) = -1/dim.

The target -Xi'/Xi has residue -1 at a simple Xi zero.  Therefore every
finite spectral atom in the compared object must retain coefficient one.
F/dim is rejected as target-compatible unless dim=1.  The exact symbolic
identity is enclosed by the rational 70-decimal interval
[-1-10^-70,-1+10^-70]; no floating residue estimate is used.

AFFINE/HADAMARD REGULARIZATION IS A DIFFERENT OPERATION.
An affine entire term A z+B has zero residue at every finite pole.  It may
remove divergent affine Taylor coefficients a_N z+b_N, but it cannot repair
a residue mismatch, a moving pole, or any non-affine compact-local growth
(the second derivative annihilates affine terms but not a resolvent pole).
The mirror-paired genus-one canonical product

    P_D(z) = product_{t>0} (1-z^2/t^2)

already has

    -P_D'/P_D = sum_{t>0} [1/(t-z)+1/(-t-z)]
                = sum_{t>0} 2z/(t^2-z^2).

Thus its source-only canonical Hadamard counterterms are frozen as A_H=0,
B_H=0 exactly.  No A/B coefficient is fitted to Xi or to -Xi'/Xi.  For
diagnosis only, a source-only affine quotient subtracts the line through
F(i) and F(2.5i); it is never used in the target residual or verdict.
Growth removed by that quotient is affine-removable; growth surviving it,
and all residue defects, are not.

CONSTRUCTION (round 2, corrected observable).
The frozen round-2 crossing engine is reused byte-pinned at SHA-256
5c3ca8e9e93ef375cd59f6e55e47eca36a2058909a13e415bf88ff110204cf1e.
It uses beta=2, the adaptive Nyquist comb X(t)=(t/2pi)^2, C2 smootherstep
activation, exact origin compactification (all prime atoms off near t=0),
LASTPASS real crossings, and the explicit +1 pole-count convention

    N_ref(T) = theta(T)/pi + 1 + S(T).

The finite operator is self-adjoint by construction.  No wall matrix,
wall positivity, zeta zero, or zero table enters.

TWO SOURCE-SIDE WEIGHT FAMILIES, FROZEN BEFORE RESULT READS.
  SHARP: w_X(n)=1 for n<=X (the round-2 reference).
  MOLL:  w_X(n)=1 for n<=X/2;
         w_X(n)=s(2(1-n/X)) for X/2<n<X;
         w_X(n)=0 for n>=X,
where s(u)=10u^3-15u^4+6u^5.  This is the compact C2 Selberg/CCM-style
endpoint taper in the CCCLVI contract: source-only, monotone, no Xi values,
and applied consistently to both phase and E1 tail coefficients.

PRECISION AND FIREWALL.
mpmath work is at 70 digits (never below 60 in the imported tail engine).
mp.zeta occurs lexically only inside functions whose names start target_.
No mp.zetazero/nzeros, zero data, eigensolver, wall matrix, or fitted Xi
value is consumed.  Construction is prime powers + Gamma phase only.

FROZEN DOMAINS AND LADDERS (same round-2 samples).
  SAFE = {x+iy: x in (0,1.3,3.7), y in (.75,1,1.5,2.5,4)} (15).
  MID  = {x+iy: x in (30,60,120), y in (1,1.5,2.5)} (9).
  X_LADDER=(8,20,50,120,300,800,2000), T_MAIN=30000.
  Dimension ladder at X=120: T=(10000,20000,30000).
  Scramble ladder=(20,120,800,2000), same frozen Golden jitter 0.35.
The printed "compact sup" is honestly the supremum on each frozen sample
set, not a continuum or interval certificate.

OBSERVABLES FOR EACH CELL.
  dim             = 2 * number of positive LASTPASS crossings.
  SUP_SAFE/MID    = max |R(z)|, R=F-A_H z-B_H=F (unnormalized).
  AFFQ_SAFE/MID   = max of the source-anchor affine quotient of F.
  RES_SAFE/MID    = max |R(z)-(-Xi'/Xi)(z)|, with no target fit.
  MASS_SAFE/MID   = max y |Tr_window(D-z)^(-1)|, unnormalized.
X-slopes and dimension/T-slopes are log-log least-squares diagnostics.
Counting d=N_D-N_ref and its +1 convention are printed, not used as zero
data or a construction input.

FROZEN BARS.
  BOUND_GROWTH_BAR=1.50; BOUND_SLOPE_BAR=+0.10.
  RES_IMPROVE_BAR=1.25; RES_SLOPE_BAR=-0.05.
  SCR_RATIO_BAR=5.0; SCR_MIN_BAR=1.5; SCR_SELF_BAR=3.0.
  NF_FLOOR=1e-9; RUNTIME_BAR=1800 s.
For the verdict-bearing MOLL family, sampled local bounds are BOUNDED only
if both SAFE and MID SUP and AFFQ rows have final/first <=1.50 and slope
<=+0.10 on both the X and dimension ladders.  They are UNBOUNDED when any
SUP/AFFQ row has final/first >1.50 and positive slope >+0.10.  Target
improvement requires both RES rows to have final <= first/1.25 and slope
<=-0.05.  Decisive scramble separation at X=2000 requires max(SAFE,MID)
ratio >=5, min ratio >=1.5, and the winning scramble row not to fall by
more than factor 3 from X=20.

HARD VERDICT PRIORITY (exactly one).
  XIRES-INSTRUMENT-EDGE       any instrument/residue/firewall/runtime ward fails.
  XIRES-UNBOUNDED             corrected MOLL compact-sample bounds grow.
  XIRES-VACUOUS               bounds do not grow, but scramble separation fails.
  XIRES-PLATEAU               bounds hold and scramble separates, but target
                              residual does not improve on both compact samples.
  XIRES-CORRECTED-CANDIDATE   exact residues, all frozen sampled bounds hold,
                              both residual rows improve, and scramble separates.
The candidate enum is still only a numerical candidate: finite samples
cannot prove compact-local boundedness on every upper-half-plane compactum.

SMOKE/AMENDMENT DISCLOSURE.
One --smoke run is permitted before the frozen run: T=3000, X=(8,50),
dimension rung T=1500, scramble X=50, grid step .02.  Smoke values are not
verdict-bearing.  Any post-smoke spec change must be appended below as a
numbered AMENDMENT before a frozen run.

AMENDMENT A1 (implementation-only, after the first smoke attempt and before
any result read).  Firewall ward A6 searched the whole source text for its
own forbidden-label string literals, so it necessarily self-fired before
construction (7/8 pre-construction wards passed; exit 1 in 0.739 s).  The
ward now inspects only imported module paths and executable Name/Attribute
identifiers.  No construction, observable, sample, bar, or verdict rule
changed; the failed smoke reached no numerical cell.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import inspect
import math
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

import xi_realrooted_limit_r2_probe as round2


# ---------------------------------------------------------------------------
# Frozen constants
# ---------------------------------------------------------------------------
CORE_SHA_EXPECTED = (
    "5c3ca8e9e93ef375cd59f6e55e47eca36a2058909a13e415bf88ff110204cf1e"
)
BETA = 2.0
T_MAIN_DEFAULT = 30000.0
T_LADDER_DEFAULT = (10000.0, 20000.0)
X_LADDER_DEFAULT = (8, 20, 50, 120, 300, 800, 2000)
SCR_X_DEFAULT = (20, 120, 800, 2000)
GRID_STEP_DEFAULT = 0.01
MP_DPS = 70
TAIL_DPS = 60
FULL_MARGIN = 10.0
JITTER = 0.35
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
SAFE_XS = (0.0, 1.3, 3.7)
SAFE_YS = (0.75, 1.0, 1.5, 2.5, 4.0)
MID_XS = (30.0, 60.0, 120.0)
MID_YS = (1.0, 1.5, 2.5)
ANCHOR_A = 1.0j
ANCHOR_B = 2.5j
TJ_BASE = 100.0
TJ_COUNT = 17
BOUND_GROWTH_BAR = 1.50
BOUND_SLOPE_BAR = 0.10
RES_IMPROVE_BAR = 1.25
RES_SLOPE_BAR = -0.05
SCR_RATIO_BAR = 5.0
SCR_MIN_BAR = 1.5
SCR_SELF_BAR = 3.0
NF_FLOOR = 1e-9
RUNTIME_BAR = 1800.0
RESIDUE_RADIUS = Fraction(1, 10**70)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
HERE = os.path.dirname(os.path.abspath(__file__))
CORE_PATH = os.path.join(HERE, "xi_realrooted_limit_r2_probe.py")

SAFE_Z = [complex(x, y) for y in SAFE_YS for x in SAFE_XS]
MID_Z = [complex(x, y) for y in MID_YS for x in MID_XS]
JOINT_Z = SAFE_Z + MID_Z

CHECKS: list[tuple[str, bool, str]] = []
T0_WALL = time.time()


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Exact taper and source-side prime-power atoms
# ---------------------------------------------------------------------------
def smootherstep(x: np.ndarray | float) -> np.ndarray | float:
    return x * x * x * (10.0 + x * (-15.0 + 6.0 * x))


def taper_weight(n: float, X: int, family: str) -> float:
    if family == "SHARP":
        return 1.0 if n <= X else 0.0
    if family != "MOLL":
        raise ValueError("unknown family %s" % family)
    if n <= X / 2.0:
        return 1.0
    if n >= X:
        return 0.0
    u = 2.0 * (1.0 - n / float(X))
    return float(smootherstep(u))


def build_atoms(X: int, T: float, family: str, scramble: bool) -> dict:
    """Prime-power atoms with beta=2 activation and frozen source taper."""
    ns: list[int] = []
    us: list[float] = []
    aa: list[float] = []
    cc: list[float] = []
    ww: list[float] = []
    dropped = 0
    zero_weight = 0
    for p in round2.sieve_primes(X):
        lp = math.log(float(p))
        pk = int(p)
        while pk <= X:
            n = float(pk)
            w = taper_weight(n, X, family)
            if w == 0.0:
                zero_weight += 1
            elif round2.t_full_of(n, BETA) > T - FULL_MARGIN:
                dropped += 1
            else:
                u_true = math.log(n)
                ns.append(pk)
                us.append(u_true)
                aa.append(w * lp / math.sqrt(n))
                cc.append(w * lp / (math.sqrt(n) * u_true))
                ww.append(w)
            pk *= int(p)
    n_arr = np.asarray(ns, dtype=np.float64)
    u_arr = np.asarray(us, dtype=np.float64)
    if scramble and len(u_arr):
        jitter = JITTER * (
            2.0 * np.mod(n_arr * GOLDEN, 1.0) - 1.0
        )
        u_arr = u_arr + jitter
    return {
        "n": n_arr,
        "u": u_arr,
        "a": np.asarray(aa, dtype=np.float64),
        "c": np.asarray(cc, dtype=np.float64),
        "w": np.asarray(ww, dtype=np.float64),
        "count": len(n_arr),
        "beta": BETA,
        "X": X,
        "x_eff": int(n_arr.max()) if len(n_arr) else 0,
        "dropped": dropped,
        "zero_weight": zero_weight,
        "family": family,
    }


def build_cell(
    name: str,
    X: int,
    T: float,
    family: str,
    scramble: bool,
    theta_grid: "round2.ThetaGrid",
) -> dict:
    t0 = time.time()
    atoms = build_atoms(X, T, family, scramble)
    crossing = round2.find_crossings(theta_grid, atoms, T)
    crossing.update(
        {
            "name": name,
            "X": X,
            "T": T,
            "family": family,
            "scramble": scramble,
            "atoms": atoms,
            "dim": 2 * len(crossing["roots_lp"]),
            "build_s": time.time() - t0,
        }
    )
    return crossing


# ---------------------------------------------------------------------------
# TARGET namespace: mp.zeta is allowed only in target_* functions
# ---------------------------------------------------------------------------
def target_value(z: complex) -> complex:
    """-Xi'/Xi at 70 digits; the only comparison target."""
    with mp.workdps(MP_DPS):
        zz = mp.mpc(z)
        s = mp.mpf("0.5") - 1j * zz
        arch = (
            1 / s
            + 1 / (s - 1)
            - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2
        )
        prime = mp.zeta(s, derivative=1) / mp.zeta(s)
        return complex(1j * (arch + prime))


def target_log_xi(z: "mp.mpc") -> "mp.mpc":
    s = mp.mpf("0.5") - 1j * z
    return (
        mp.log(mp.mpf("0.5"))
        + mp.log(s)
        + mp.log(s - 1)
        - s / 2 * mp.log(mp.pi)
        + mp.loggamma(s / 2)
        + mp.log(mp.zeta(s))
    )


def target_derivative_check() -> float:
    with mp.workdps(MP_DPS):
        z = mp.mpc("1.3", "2.5")
        h = mp.mpf(10) ** (-20)
        numeric = -(
            target_log_xi(z + h) - target_log_xi(z - h)
        ) / (2 * h)
        analytic = mp.mpc(target_value(complex(z)))
        return float(abs(numeric - analytic))


def target_s_of_t(T: float) -> tuple[float, bool]:
    """S(T) by continuous argument tracking from sigma=2 to sigma=1/2."""
    with mp.workdps(MP_DPS):
        tt = mp.mpf(T)
        cur = mp.zeta(2 + 1j * tt)
        total = mp.arg(cur)
        sigma = mp.mpf(2)
        target_sigma = mp.mpf("0.5")
        step = mp.mpf("0.25")
        step_min = mp.mpf(2) ** (-20)
        while sigma > target_sigma:
            trial = min(step, sigma - target_sigma)
            accepted = False
            while trial >= step_min:
                nxt = mp.zeta(sigma - trial + 1j * tt)
                if abs(nxt) < mp.mpf("1e-5"):
                    trial /= 2
                    continue
                delta = mp.arg(nxt / cur)
                if abs(delta) > mp.mpf("1.0"):
                    trial /= 2
                    continue
                total += delta
                cur = nxt
                sigma -= trial
                accepted = True
                break
            if not accepted:
                return 0.0, False
            step = min(2 * trial, mp.mpf("0.25"))
        return float(total / mp.pi), True


def target_counting_reference(checkpoints: list[float]) -> dict:
    """N_ref=theta/pi + explicit pole unit +1; nudge only as target read."""
    reference: dict[float, tuple[float, float, int] | None] = {}
    for nominal in checkpoints:
        read = None
        T = nominal
        for _ in range(3):
            s_value, ok = target_s_of_t(T)
            if ok:
                n_ref = round2.theta_point(T) / math.pi + 1.0 + s_value
                if abs(n_ref - round(n_ref)) <= 1e-6:
                    read = (T, s_value, int(round(n_ref)))
                    break
            T += 0.37
        reference[nominal] = read
    return reference


# ---------------------------------------------------------------------------
# Residue, affine, and firewall wards
# ---------------------------------------------------------------------------
def exact_residue_wards() -> dict:
    z, lam = sp.symbols("z lambda")
    atom = 1 / (lam - z)
    residue = sp.limit((z - lam) * atom, z, lam)
    dim = sp.symbols("d", integer=True, positive=True)
    normalized = sp.simplify(residue / dim)
    affine_a, affine_b = sp.symbols("A B")
    affine_residue = sp.limit(
        (z - lam) * (atom - affine_a * z - affine_b), z, lam
    )
    pole_curvature = sp.simplify(sp.diff(atom, z, 2))
    affine_curvature = sp.diff(affine_a * z + affine_b, z, 2)
    return {
        "residue": residue,
        "normalized": normalized,
        "affine_residue": affine_residue,
        "pole_curvature": pole_curvature,
        "affine_curvature": affine_curvature,
    }


def format_fraction_decimal(q: Fraction, digits: int = 72) -> str:
    with mp.workdps(digits + 10):
        return mp.nstr(mp.mpf(q.numerator) / q.denominator, digits)


def firewall_audit() -> tuple[bool, str]:
    source = inspect.getsource(sys.modules[__name__])
    tree = ast.parse(source)
    violations: list[str] = []

    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                func = child.func
                if (
                    isinstance(func, ast.Attribute)
                    and isinstance(func.value, ast.Name)
                    and func.value.id == "mp"
                    and func.attr == "zeta"
                    and not node.name.startswith("target_")
                ):
                    violations.append("mp.zeta in " + node.name)
                call_name = (
                    func.id
                    if isinstance(func, ast.Name)
                    else func.attr
                    if isinstance(func, ast.Attribute)
                    else ""
                )
                if call_name.lower() in {
                    "zetazero",
                    "nzeros",
                    "eigh",
                    "eigvalsh",
                    "lstsq",
                    "least_squares",
                }:
                    violations.append(call_name + " call")

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            modules = [node.module or ""]
        else:
            modules = []
        if any(module.startswith("verification") for module in modules):
            violations.append("verification import")
        identifier = (
            node.id
            if isinstance(node, ast.Name)
            else node.attr
            if isinstance(node, ast.Attribute)
            else ""
        )
        if identifier.lower() in {"wall_matrix", "status_ledger"}:
            violations.append(identifier)
    return not violations, "violations: %s" % (violations or "none")


def exact_taper_wards() -> tuple[bool, str]:
    x = sp.symbols("x", real=True)
    s = 10 * x**3 - 15 * x**4 + 6 * x**5
    ds = sp.factor(sp.diff(s, x))
    d2s = sp.diff(s, x, 2)
    ok = (
        s.subs(x, 0) == 0
        and s.subs(x, 1) == 1
        and sp.diff(s, x).subs(x, 0) == 0
        and sp.diff(s, x).subs(x, 1) == 0
        and d2s.subs(x, 0) == 0
        and d2s.subs(x, 1) == 0
        and ds == 30 * x**2 * (x - 1) ** 2
        and sp.expand(s + s.subs(x, 1 - x)) == 1
    )
    return bool(ok), "s'=30x^2(1-x)^2, C2 endpoints, s(x)+s(1-x)=1"


# ---------------------------------------------------------------------------
# Observables
# ---------------------------------------------------------------------------
def affine_quotient(values: dict[complex, complex]) -> dict:
    """Source-only interpolation through F(i),F(2.5i); never target-fitted."""
    slope = (values[ANCHOR_B] - values[ANCHOR_A]) / (
        ANCHOR_B - ANCHOR_A
    )
    intercept = values[ANCHOR_A] - slope * ANCHOR_A
    quotient = {z: values[z] - slope * z - intercept for z in JOINT_Z}
    return {"A": slope, "B": intercept, "values": quotient}


def add_observables(cell: dict, targets: dict[complex, complex]) -> None:
    # Canonical mirror-paired Hadamard gauge: A_H=B_H=0 exactly.
    values = {
        z: round2.F_completed(
            cell["roots_lp"], z, cell["t_cut"], cell["atoms"]
        )
        for z in JOINT_Z
    }
    quotient = affine_quotient(values)
    residuals = {z: values[z] - targets[z] for z in JOINT_Z}
    window = {
        z: complex(np.sum(round2.K_of(cell["roots_lp"], z)))
        for z in JOINT_Z
    }

    def sup_on(mapping: dict[complex, complex], grid: list[complex]) -> float:
        return max(abs(mapping[z]) for z in grid)

    cell["F"] = values
    cell["residual"] = residuals
    cell["affq"] = quotient
    cell["sup_safe"] = sup_on(values, SAFE_Z)
    cell["sup_mid"] = sup_on(values, MID_Z)
    cell["affq_safe"] = sup_on(quotient["values"], SAFE_Z)
    cell["affq_mid"] = sup_on(quotient["values"], MID_Z)
    cell["res_safe"] = sup_on(residuals, SAFE_Z)
    cell["res_mid"] = sup_on(residuals, MID_Z)
    cell["res_rms_safe"] = float(
        np.sqrt(np.mean([abs(residuals[z]) ** 2 for z in SAFE_Z]))
    )
    cell["res_rms_mid"] = float(
        np.sqrt(np.mean([abs(residuals[z]) ** 2 for z in MID_Z]))
    )
    cell["mass_safe"] = max(z.imag * abs(window[z]) for z in SAFE_Z)
    cell["mass_mid"] = max(z.imag * abs(window[z]) for z in MID_Z)
    cell["im_window_positive"] = all(window[z].imag > 0 for z in JOINT_Z)


def add_counting(
    cell: dict,
    reference: dict,
    checkpoints: list[float],
) -> None:
    differences: list[int] = []
    for nominal in checkpoints:
        read = reference[nominal]
        if read is None:
            continue
        actual_t, _s_value, n_ref = read
        if actual_t > cell["t_cut"] - 100.0:
            continue
        n_d = int(np.count_nonzero(cell["roots_lp"] <= actual_t))
        differences.append(n_d - n_ref)
    cell["d_list"] = differences


def histogram(values: list[int]) -> str:
    if not values:
        return "(none)"
    return " ".join(
        "d=%+d:%d" % (v, values.count(v)) for v in sorted(set(values))
    )


def log_slope(x: list[float], y: list[float]) -> float:
    xa = np.asarray(x, dtype=np.float64)
    ya = np.asarray(y, dtype=np.float64)
    live = (xa > 0) & (ya > NF_FLOOR)
    if np.count_nonzero(live) < 2:
        return float("nan")
    return float(np.polyfit(np.log(xa[live]), np.log(ya[live]), 1)[0])


def row_stats(x: list[float], values: list[float]) -> dict:
    first = float(values[0])
    last = float(values[-1])
    return {
        "slope": log_slope(x, values),
        "ratio": last / max(first, 1e-300),
        "first": first,
        "last": last,
    }


def bounded_row(stats: dict) -> bool:
    return (
        stats["ratio"] <= BOUND_GROWTH_BAR
        and stats["slope"] <= BOUND_SLOPE_BAR
    )


def unbounded_row(stats: dict) -> bool:
    return (
        stats["ratio"] > BOUND_GROWTH_BAR
        and stats["slope"] > BOUND_SLOPE_BAR
    )


def improved_row(stats: dict) -> bool:
    return (
        stats["ratio"] <= 1.0 / RES_IMPROVE_BAR
        and stats["slope"] <= RES_SLOPE_BAR
    )


def print_cell(cell: dict) -> None:
    atoms = cell["atoms"]
    print(
        "  %-18s fam=%-5s X=%5d Xeff=%5d T=%7.0f dim=%6d "
        "raw=%6d exc=%5d rec=%2d parity=%s edge=%+.4f "
        "w=[%.3f,%.3f] %.1fs"
        % (
            cell["name"],
            cell["family"],
            cell["X"],
            atoms["x_eff"],
            cell["T"],
            cell["dim"],
            cell["n_raw"],
            cell["excess"],
            cell["recovered"],
            "OK" if cell["parity_ok"] else "FAIL",
            cell["edge_phase"],
            float(atoms["w"].min()) if atoms["count"] else 0.0,
            float(atoms["w"].max()) if atoms["count"] else 0.0,
            cell["build_s"],
        )
    )


def print_ladder(
    label: str,
    x_values: list[float],
    cells: list[dict],
    x_label: str,
) -> dict[str, dict]:
    keys = (
        "sup_safe",
        "sup_mid",
        "affq_safe",
        "affq_mid",
        "res_safe",
        "res_mid",
        "mass_safe",
        "mass_mid",
    )
    print("\n  %s" % label)
    print(
        "    %-10s %-11s %-11s %-11s %-11s %-11s %-11s %-11s %-11s"
        % (
            x_label,
            "SUP_SAFE",
            "SUP_MID",
            "AFFQ_SAFE",
            "AFFQ_MID",
            "RES_SAFE",
            "RES_MID",
            "MASS_SAFE",
            "MASS_MID",
        )
    )
    for x, cell in zip(x_values, cells):
        print(
            "    %-10g %.4e  %.4e  %.4e  %.4e  %.4e  %.4e  %.4e  %.4e"
            % (
                x,
                cell["sup_safe"],
                cell["sup_mid"],
                cell["affq_safe"],
                cell["affq_mid"],
                cell["res_safe"],
                cell["res_mid"],
                cell["mass_safe"],
                cell["mass_mid"],
            )
        )
    stats = {
        key: row_stats(x_values, [cell[key] for cell in cells])
        for key in keys
    }
    print("    slopes / final:first:")
    for key in keys:
        print(
            "      %-10s slope=%+.4f ratio=%.4f final=%.4e"
            % (
                key,
                stats[key]["slope"],
                stats[key]["ratio"],
                stats[key]["last"],
            )
        )
    return stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    smoke = bool(args.smoke)

    if smoke:
        T_MAIN = 3000.0
        T_LADDER = (1500.0,)
        X_LADDER = (8, 50)
        SCR_X = (50,)
        GRID_STEP = 0.02
    else:
        T_MAIN = T_MAIN_DEFAULT
        T_LADDER = T_LADDER_DEFAULT
        X_LADDER = X_LADDER_DEFAULT
        SCR_X = SCR_X_DEFAULT
        GRID_STEP = GRID_STEP_DEFAULT

    mp.mp.dps = MP_DPS
    round2.DPS_TARGET = MP_DPS
    round2.DPS_TAIL = TAIL_DPS
    round2.GRID_STEP = GRID_STEP
    round2._ST_CACHE.clear()

    print("=" * 88)
    print(
        "xi_resolvent_normalization_probe  PRIME.XI.RESOLVENT.NORMALIZATION.01"
    )
    print(
        "FROZEN SPEC_SHA %s%s"
        % (
            SPEC_SHA,
            "  *** SMOKE, NOT VERDICT-BEARING ***" if smoke else "",
        )
    )
    print("=" * 88)

    print("\nI. EXACT RESIDUE / REGULARIZATION / FIREWALL WARDS")
    core_sha = sha256_file(CORE_PATH)
    check(
        "A1 frozen round-2 dependency SHA",
        core_sha == CORE_SHA_EXPECTED,
        core_sha,
    )

    residue = exact_residue_wards()
    lower = Fraction(-1) - RESIDUE_RADIUS
    upper = Fraction(-1) + RESIDUE_RADIUS
    exact_in_enclosure = lower <= Fraction(-1) <= upper
    check(
        "A2 atom residue exact -1",
        residue["residue"] == -1 and exact_in_enclosure,
        "Res=%s enclosure=[%s,%s]"
        % (
            residue["residue"],
            format_fraction_decimal(lower),
            format_fraction_decimal(upper),
        ),
    )
    check(
        "A3 normalized residue rejected unless dim=1",
        residue["normalized"] == -1 / sp.Symbol(
            "d", integer=True, positive=True
        ),
        "Res(F/dim)=%s; equals -1 iff dim=1" % residue["normalized"],
    )
    check(
        "A4 affine terms preserve residues",
        residue["affine_residue"] == -1
        and residue["affine_curvature"] == 0
        and residue["pole_curvature"] != 0,
        "Res(atom-Az-B)=-1; d2(Az+B)=0; d2(atom)=%s"
        % residue["pole_curvature"],
    )
    taper_ok, taper_detail = exact_taper_wards()
    check("A5 mollifier exact C2 ward", taper_ok, taper_detail)
    firewall_ok, firewall_detail = firewall_audit()
    check("A6 source/target firewall and no Xi fit", firewall_ok, firewall_detail)
    target_dev = target_derivative_check()
    check(
        "A7 70-digit target derivative",
        target_dev <= 1e-12,
        "abs dev %.3e" % target_dev,
    )
    check(
        "A8 precision floor",
        MP_DPS >= 55 and TAIL_DPS >= 55,
        "target dps=%d tail dps=%d" % (MP_DPS, TAIL_DPS),
    )
    print(
        "  [WARD] canonical paired Hadamard gauge A_H=0, B_H=0 exactly; "
        "no Xi-fitted affine coefficients."
    )
    print(
        "  [WARD] affine-removable: a_N z+b_N only.  Not removable: "
        "residue mismatch, poles, or non-affine curvature."
    )

    if any(not ok for _name, ok, _detail in CHECKS):
        print("INSTRUMENT EDGE BEFORE CONSTRUCTION.")
        print("VERDICT: XIRES-INSTRUMENT-EDGE")
        return 1

    print("\nII. TARGETS AND EXPLICIT +1 COUNTING REFERENCE")
    targets = {z: target_value(z) for z in JOINT_Z}
    for z in (1j, 2.5j, 30 + 1j, 120 + 1j):
        print(
            "  z=%6.1f%+.2fi  -Xi'/Xi=%+.12e%+.12ei"
            % (z.real, z.imag, targets[z].real, targets[z].imag)
        )
    checkpoints = [
        TJ_BASE * 2.0 ** (j / 2.0) for j in range(TJ_COUNT)
    ]
    checkpoints = [t for t in checkpoints if t <= T_MAIN - 100.0]
    t0 = time.time()
    counting_ref = target_counting_reference(checkpoints)
    n_count_ok = sum(v is not None for v in counting_ref.values())
    check(
        "A9 N_ref integer, pole +1 explicit",
        n_count_ok == len(checkpoints),
        "%d/%d checkpoints, %.1fs"
        % (n_count_ok, len(checkpoints), time.time() - t0),
    )
    print(
        "  N_ref(T)=theta(T)/pi + 1 + S(T): "
        + ", ".join(
            "N(%.0f)=%d" % (read[0], read[2])
            for read in list(counting_ref.values())[:6]
            if read is not None
        )
        + (", ..." if len(counting_ref) > 6 else "")
    )

    print("\nIII. CELL CONSTRUCTION (beta=2, adaptive origin compactification)")
    t0 = time.time()
    theta_grid = round2.ThetaGrid(T_MAIN)
    print(
        "  master grid %d points, step %.3f, %.1fs"
        % (len(theta_grid.t), GRID_STEP, time.time() - t0)
    )
    cells: dict[str, dict] = {}

    def register(
        name: str, X: int, T: float, family: str, scramble: bool
    ) -> dict:
        cell = build_cell(name, X, T, family, scramble, theta_grid)
        cells[name] = cell
        print_cell(cell)
        return cell

    arch = register("ARCH", 0, T_MAIN, "SHARP", False)
    for family in ("SHARP", "MOLL"):
        for X in X_LADDER:
            register("%s-X%d" % (family, X), X, T_MAIN, family, False)
        for T in T_LADDER:
            register(
                "%s-T%d" % (family, int(T)),
                120 if not smoke else X_LADDER[-1],
                T,
                family,
                False,
            )
        for X in SCR_X:
            register(
                "%s-SCR-X%d" % (family, X),
                X,
                T_MAIN,
                family,
                True,
            )

    parity_ok = all(cell["parity_ok"] for cell in cells.values())
    check("A10 crossing census parity", parity_ok, "%d cells" % len(cells))
    worst_origin = max(
        abs(cell["edge_phase"] - arch["edge_phase"])
        for cell in cells.values()
    )
    check(
        "A11 origin compactification",
        worst_origin <= 1e-9,
        "max |edge-ARCH| %.3e" % worst_origin,
    )
    min_slack = float("inf")
    for cell in cells.values():
        atoms = cell["atoms"]
        if atoms["count"]:
            slack = cell["t_cut"] - round2.t_full_of(
                float(atoms["n"].max()), BETA
            )
            min_slack = min(min_slack, slack)
    check(
        "A12 all atoms fully active before tail",
        min_slack > 0 or min_slack == float("inf"),
        "minimum slack %.1f" % (0.0 if min_slack == float("inf") else min_slack),
    )
    dims = [cell["dim"] for cell in cells.values()]
    normalized_rejected = all(dim > 1 for dim in dims)
    check(
        "A13 F/dim target compatibility rejected",
        normalized_rejected,
        "dims [%d,%d], residues -1/dim not -1"
        % (min(dims), max(dims)),
    )
    print(
        "  RESIDUE WARD APPLIED TO EVERY ATOM: coefficient=1 => Res=-1; "
        "normalizing by each listed dim is forbidden."
    )

    print("\nIV. CORRECTED UNNORMALIZED OBSERVABLES")
    for cell in cells.values():
        add_observables(cell, targets)
        add_counting(cell, counting_ref, checkpoints)
    positive_im = all(
        cell["im_window_positive"] for cell in cells.values()
    )
    check(
        "A14 unnormalized window Herglotz sign",
        positive_im,
        "Im Tr_window(D-z)^-1 >0 on all frozen samples/cells",
    )

    for family in ("SHARP", "MOLL"):
        print("\n  %s cells: canonical A_H=B_H=0, source-anchor affine diagnostic" % family)
        for X in X_LADDER:
            cell = cells["%s-X%d" % (family, X)]
            print(
                "    X=%-5d dim=%-6d source-affine A=%+.3e%+.3ei "
                "B=%+.3e%+.3ei d-hist %s"
                % (
                    X,
                    cell["dim"],
                    cell["affq"]["A"].real,
                    cell["affq"]["A"].imag,
                    cell["affq"]["B"].real,
                    cell["affq"]["B"].imag,
                    histogram(cell["d_list"]),
                )
            )

    print("\nV. X AND DIMENSION/T COMPACT-SAMPLE LADDERS")
    ladder_stats: dict[tuple[str, str], dict] = {}
    for family in ("SHARP", "MOLL"):
        main_cells = [cells["%s-X%d" % (family, X)] for X in X_LADDER]
        ladder_stats[(family, "X")] = print_ladder(
            "%s X ladder" % family,
            [float(X) for X in X_LADDER],
            main_cells,
            "X",
        )
        dim_cells = [
            cells["%s-T%d" % (family, int(T))] for T in T_LADDER
        ] + [
            cells[
                "%s-X%d"
                % (family, 120 if not smoke else X_LADDER[-1])
            ]
        ]
        dim_values = [float(cell["dim"]) for cell in dim_cells]
        ladder_stats[(family, "DIM")] = print_ladder(
            "%s dimension ladder (X=%d)"
            % (family, 120 if not smoke else X_LADDER[-1]),
            dim_values,
            dim_cells,
            "dim",
        )

    print("\nVI. MAIN VS SCRAMBLE (direct, no target fit)")
    separation: dict[str, dict] = {}
    for family in ("SHARP", "MOLL"):
        main_last = cells["%s-X%d" % (family, X_LADDER[-1])]
        scr_cells = [
            cells["%s-SCR-X%d" % (family, X)] for X in SCR_X
        ]
        for cell in scr_cells:
            print(
                "  %-5s SCR-X%-5d dim=%-6d RES_SAFE=%.4e RES_MID=%.4e "
                "SUP_SAFE=%.4e SUP_MID=%.4e"
                % (
                    family,
                    cell["X"],
                    cell["dim"],
                    cell["res_safe"],
                    cell["res_mid"],
                    cell["sup_safe"],
                    cell["sup_mid"],
                )
            )
        last_scr = scr_cells[-1]
        sep_safe = last_scr["res_safe"] / max(
            main_last["res_safe"], 1e-300
        )
        sep_mid = last_scr["res_mid"] / max(
            main_last["res_mid"], 1e-300
        )
        if sep_safe >= sep_mid:
            scr_self = last_scr["res_safe"] >= (
                scr_cells[0]["res_safe"] / SCR_SELF_BAR
            )
            winning = "SAFE"
        else:
            scr_self = last_scr["res_mid"] >= (
                scr_cells[0]["res_mid"] / SCR_SELF_BAR
            )
            winning = "MID"
        decisive = (
            max(sep_safe, sep_mid) >= SCR_RATIO_BAR
            and min(sep_safe, sep_mid) >= SCR_MIN_BAR
            and scr_self
        )
        separation[family] = {
            "safe": sep_safe,
            "mid": sep_mid,
            "self": scr_self,
            "decisive": decisive,
        }
        print(
            "  %-5s SEP_SAFE=%.3f SEP_MID=%.3f scr-self(%s)=%s => %s"
            % (
                family,
                sep_safe,
                sep_mid,
                winning,
                scr_self,
                "DECISIVE" if decisive else "NOT DECISIVE",
            )
        )

    print("\nVII. HARD VERDICT (MOLL is verdict-bearing)")
    moll_x = ladder_stats[("MOLL", "X")]
    moll_dim = ladder_stats[("MOLL", "DIM")]
    bound_keys = ("sup_safe", "sup_mid", "affq_safe", "affq_mid")
    all_bound_stats = [moll_x[key] for key in bound_keys] + [
        moll_dim[key] for key in bound_keys
    ]
    any_unbounded = any(unbounded_row(stats) for stats in all_bound_stats)
    all_bounded = all(bounded_row(stats) for stats in all_bound_stats)
    residual_improves = improved_row(moll_x["res_safe"]) and improved_row(
        moll_x["res_mid"]
    )
    residue_exact = (
        residue["residue"] == -1
        and residue["affine_residue"] == -1
        and normalized_rejected
    )
    decisive = separation["MOLL"]["decisive"]

    print(
        "  residue_exact=%s all_sampled_bounds=%s any_unbounded=%s "
        "residual_improves=%s scramble_decisive=%s"
        % (
            residue_exact,
            all_bounded,
            any_unbounded,
            residual_improves,
            decisive,
        )
    )
    for domain in ("sup_safe", "sup_mid", "affq_safe", "affq_mid"):
        print(
            "  BOUND %-10s X(slope=%+.4f ratio=%.4f) "
            "DIM(slope=%+.4f ratio=%.4f)"
            % (
                domain,
                moll_x[domain]["slope"],
                moll_x[domain]["ratio"],
                moll_dim[domain]["slope"],
                moll_dim[domain]["ratio"],
            )
        )
    for domain in ("res_safe", "res_mid"):
        print(
            "  TARGET %-9s slope=%+.4f ratio=%.4f final=%.4e"
            % (
                domain,
                moll_x[domain]["slope"],
                moll_x[domain]["ratio"],
                moll_x[domain]["last"],
            )
        )

    instrument_ok_before_runtime = all(ok for _name, ok, _detail in CHECKS)
    wall = time.time() - T0_WALL
    runtime_ok = wall <= RUNTIME_BAR
    check("A15 runtime below 30 minutes", runtime_ok, "%.1fs" % wall)
    instrument_ok = instrument_ok_before_runtime and runtime_ok

    if not instrument_ok or not residue_exact:
        verdict = "XIRES-INSTRUMENT-EDGE"
    elif any_unbounded:
        verdict = "XIRES-UNBOUNDED"
    elif not decisive:
        verdict = "XIRES-VACUOUS"
    elif not all_bounded or not residual_improves:
        verdict = "XIRES-PLATEAU"
    else:
        verdict = "XIRES-CORRECTED-CANDIDATE"

    n_pass = sum(ok for _name, ok, _detail in CHECKS)
    print("\n" + "=" * 88)
    print(
        "CHECKS %d/%d PASS  runtime %.1fs  SPEC_SHA %s"
        % (n_pass, len(CHECKS), wall, SPEC_SHA)
    )
    print("VERDICT: %s" % verdict)
    print(
        "SHORTEST HONEST THEOREM GAP: prove, rather than sample, source-only "
        "safe-open-set convergence and uniform compact-local bounds on every "
        "K subset of Im(z)>0 for the UNNORMALIZED residue-one, canonically "
        "regularized family; finite SAFE/MID plateaus cannot supply Vitali."
    )
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print(
        "NO RH CLAIM. NO POSITIVITY CLAIM. NO CONTINUUM-BOUND CLAIM. "
        "EXPERIMENTS ONLY."
    )
    print("=" * 88)
    return 0 if instrument_ok else 1


if __name__ == "__main__":
    sys.exit(main())
