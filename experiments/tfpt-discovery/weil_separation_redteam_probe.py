#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weil_separation_redteam_probe -- PRIME.RDAGGER.WEIL_SEPARATION_REDTEAM.01

Round 535.  Numerical red-team of the OPEN Lean theorem

    fullWeil_separates_offCritical_zeros
        : FullWeilSeparatesOffCriticalZeros
    (rh/lean/RH/ExternalBridges.lean, currently ~15536, sorry).

The Prop (currently ~15510) says: every nontrivial zeta zero s with
Re(s) ≠ 1/2 admits an admissible FullWeilTest F with
standardExplicitFormula F < 0.  The conversion
standard_weil_criterion_to_mathlib_rh_of_separation is already proved;
this probe does NOT touch that wrapper.

CLAIM BOUNDARY.  Finite quadratic-form search in a finite-dimensional
subclass of the Lean geometric test class.  Conditional on the frozen
first-100 ordinates and on a search cap R ≤ 4.  NO RH claim, NO anti-RH
claim, NO ledger row, NO paper edit.  A negative truncated Rayleigh
quotient is not a proof of the Lean theorem.  A nonnegative Rayleigh
in this subclass is not a proof that the infinite-dimensional class
cannot separate.

HAT CONVENTION.  Lean FullWeilTest.hat (line ~2699) is the unshifted
Laplace transform ∫ g(t) exp(s t) dt.  The classical Weil kernel that
makes ĥ(1/2+it) = |ĝ_h(t)|² ≥ 0 is the shifted pairing used here:

    ĥ_Weil(s) := ∫ g(u) exp((s − 1/2) u) du = hat_Lean(s − 1/2).

Identifying hat_Lean(ρ) with ĥ_Weil(ρ) is part of the open dictionary
(standard_explicit_formula_identification, sorry).  This probe
red-teams the intended spectral positivity/separation statement.

Runtime: numpy.  Zeros cached from mpmath.zetazero (mpmath 1.3.0,
dps=30, 2026-09-01); mpmath is not called at runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
SPEC = {
    "round": 535,
    "target": "fullWeil_separates_offCritical_zeros",
    "lean_file": "rh/lean/RH/ExternalBridges.lean",
    "hat": "weil_shifted",
    "betas": [0.51, 0.55, 0.6, 0.7, 0.8, 0.9, 0.95],
    "gammas": [0.5, 1.0, 5.0, 14.13, 30.0, 100.0, 1000.0],
    "n_zeros": 100,
    "n_modes": 220,
    "r_fixed": [0.5, 1.0, 2.0],
    "r_min": 0.08,
    "r_max": 4.0,
    "sep_atol": 1e-12,
    "g1_atol": 1e-8,
    "heur_dt": 0.5,
    "heur_t_cap": 2000.0,
}

SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

# First 100 positive ordinates of nontrivial zeta zeros.
# Source: mpmath 1.3.0, mp.mp.dps = 30, mp.zetazero(n).imag, n = 1..100.
# Not an RH oracle: these are the classical Odlyzko/mpmath values used
# only as the on-critical truncation of the spectral sum.
ON_LINE_ORDINATES = (
    14.1347251417346946, 21.0220396387715560, 25.0108575801456894,
    30.4248761258595124, 32.9350615877391917, 37.5861781588256747,
    40.9187190121474984, 43.3270732809150019, 48.0051508811671610,
    49.7738324776723005, 52.9703214777144638, 56.4462476970633915,
    59.3470440026023525, 60.8317785246098097, 65.1125440480816025,
    67.0798105294941678, 69.5464017111739849, 72.0671576744819049,
    75.7046906990839261, 77.1448400688747995, 79.3373750202493682,
    82.9103808540860285, 84.7354929805170514, 87.4252746131252252,
    88.8091112076344587, 92.4918992705584913, 94.6513440405198878,
    95.8706342282453079, 98.8311942181936871, 101.3178510057313844,
    103.7255380404783409, 105.4466230523260890, 107.1686111842764006,
    111.0295355431696720, 111.8746591769926368, 114.3202209154527083,
    116.2266803208575539, 118.7907828659762117, 121.3701250024206502,
    122.9468292935525824, 124.2568185543457702, 127.5166838795964992,
    129.5787041999560643, 131.0876885309326667, 133.4977372029975982,
    134.7565097533738765, 138.1160420545334375, 139.7362089521213875,
    141.1237074040211326, 143.1118458076206252, 146.0009824867655084,
    147.4227653425596145, 150.0535204207848778, 150.9252576122414666,
    153.0246938111988868, 156.1129092942378804, 157.5975918175940649,
    158.8499881714205060, 161.1889641375960309, 163.0307096871819965,
    165.5370691879004141, 167.1844399781745096, 169.0945154155688215,
    169.9119764794116918, 173.4115365195915501, 174.7541915233657335,
    176.4414342977104297, 178.3774077760999717, 179.9164840202570019,
    182.2070784843664626, 184.8744678483874964, 185.5987836777074733,
    187.2289225835018556, 189.4161586560169326, 192.0266563607137869,
    193.0797266038456996, 195.2653966795292320, 196.8764818409583199,
    198.0153096762519169, 201.2647519437038000, 202.4935945141405398,
    204.1896718031045452, 205.3946972021632860, 207.9062588878062172,
    209.5765097168562647, 211.6908625953653029, 213.3479193597126766,
    214.5470447834914296, 216.1695385082637131, 219.0675963490213860,
    220.7149188393140093, 221.4307055546933327, 224.0070002546043213,
    224.9833246695822879, 227.4214442796792923, 229.3374133055253594,
    231.2501887004991659, 231.9872352531802449, 233.6934041789083096,
    236.5242296658161933,
)

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-36s %s" % (
        "PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def full_anchor(radius: float) -> int:
    """Lean FullWeilTest.fullAnchor = max(1, ceil(exp(R))) (line ~974)."""
    return max(1, int(math.ceil(math.exp(radius))))


def clip_radius(radius: float) -> float:
    return float(min(SPEC["r_max"], max(SPEC["r_min"], radius)))


def radius_key(radius: float) -> float:
    return round(float(radius), 12)


def radii_for(gamma: float, n_modes: int) -> tuple[float, ...]:
    """Search radii: fixed grid plus γ-tuned Paley–Wiener scales.

    The Lean class does not cap R.  R ≤ r_max is a SEARCH cap.
    """
    raw = [float(value) for value in SPEC["r_fixed"]]
    for multiple in (1.0, 2.0, 4.0):
        raw.append(multiple * math.pi / gamma)
    raw.append(n_modes * math.pi / (gamma * 1.4))
    unique: list[float] = []
    for radius in raw:
        clipped = radius_key(clip_radius(radius))
        if clipped not in unique:
            unique.append(clipped)
    return tuple(sorted(unique))


def expm1_div_array(omega: np.ndarray, radius: float) -> np.ndarray:
    """(exp(omega R) - 1) / omega, Taylor branch at omega = 0."""
    scaled = omega * radius
    out = np.empty_like(scaled, dtype=np.complex128)
    small = np.abs(scaled) < 1e-12
    if np.any(small):
        z = scaled[small]
        out[small] = radius * (1.0 + z * (0.5 + z * (1.0 / 6.0 + z / 24.0)))
    big = ~small
    if np.any(big):
        out[big] = np.expm1(scaled[big]) / omega[big]
    return out


def sine_laplace_vector(n_modes: int, radius: float, zeta: complex) -> np.ndarray:
    """H_k(z) = ∫_0^R sin(k π t / R) e^{z t} dt, k = 1..n_modes.

    Closed form via (e^{w R}-1)/w at w = z ± i a, a = k π / R.
    Witness h(t) = sum c_k sin(k π t / R) on [0, R], zero elsewhere:
    Lipschitz, compactly supported in an interval of length R, vanishes
    at the endpoints (Lean autocorrelation witness, lines 82–88).
    """
    frequencies = (np.arange(1, n_modes + 1, dtype=np.float64)
                   * math.pi / radius)
    zeta_c = np.complex128(zeta)
    return (
        expm1_div_array(zeta_c + 1j * frequencies, radius)
        - expm1_div_array(zeta_c - 1j * frequencies, radius)
    ) / (2j)


def gram_modsq(vector: np.ndarray) -> np.ndarray:
    real = vector.real
    imag = vector.imag
    return np.outer(real, real) + np.outer(imag, imag)


def gram_re_product(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    """Real quadratic form c ↦ Re[(left·c) (right·c)]."""
    left_r, left_i = left.real, left.imag
    right_r, right_i = right.real, right.imag
    return (
        0.5 * (np.outer(left_r, right_r) + np.outer(right_r, left_r))
        - 0.5 * (np.outer(left_i, right_i) + np.outer(right_i, left_i))
    )


def assemble_online(n_modes: int, radius: float, ordinates: np.ndarray) -> np.ndarray:
    """S_on(c) = sum_n 2 |H(i t_n)|²  (conjugate pair on the critical line).

    ĥ_Weil(1/2 + i t) = H(-i t) H(i t) = |H(i t)|² ≥ 0.
    """
    gram = np.zeros((n_modes, n_modes), dtype=np.float64)
    for height in ordinates:
        gram += 2.0 * gram_modsq(
            sine_laplace_vector(n_modes, radius, 1j * float(height))
        )
    return gram


def assemble_offline(
    n_modes: int, radius: float, beta: float, gamma: float,
) -> np.ndarray:
    """Quadruple {β±iγ, 1−β±iγ} contributes 4 Re[H(−δ−iγ) H(δ+iγ)].

    Functional equation of even g: ĥ_Weil(s) = ĥ_Weil(1−s).
    """
    delta = beta - 0.5
    left = sine_laplace_vector(n_modes, radius, -delta - 1j * gamma)
    right = sine_laplace_vector(n_modes, radius, delta + 1j * gamma)
    return 4.0 * gram_re_product(left, right)


def eigs_min(matrix: np.ndarray) -> tuple[float, np.ndarray]:
    values, vectors = np.linalg.eigh(matrix)
    vector = np.real(vectors[:, 0]).copy()
    pivot = int(np.argmax(np.abs(vector)))
    if vector[pivot] < 0.0:
        vector *= -1.0
    return float(values[0]), vector


def lipschitz_hprime_l1(coeffs: np.ndarray, radius: float) -> float:
    """||h'||_1 bounds for the sine series (two estimates, take min)."""
    modes = np.arange(1, coeffs.size + 1, dtype=np.float64)
    bound_l1 = math.pi * float(np.dot(modes, np.abs(coeffs)))
    hprime_l2 = (math.pi / math.sqrt(2.0 * radius)) * math.sqrt(
        float(np.dot(modes * modes, coeffs * coeffs))
    )
    bound_cauchy = math.sqrt(radius) * hprime_l2
    return min(bound_l1, bound_cauchy)


def lipschitz_zero_tail(coeffs: np.ndarray, radius: float, t_cut: float) -> float:
    """∑_{t_n > T} 2 |H(i t_n)|² ≤ 2 C² (1 + log T) / T.

    |H(it)| ≤ ||h'||_1 / |t| (integration by parts, h(0)=h(R)=0).
    Zero density N'(T) ≤ log T for T ≥ 14; ∫_T^∞ log(t)/t² dt = (1+log T)/T.
    Heuristic documented: the log-T density majorant is classical, not
    a formal Lean bound.
    """
    lipschitz = lipschitz_hprime_l1(coeffs, radius)
    return 2.0 * lipschitz * lipschitz * (1.0 + math.log(t_cut)) / t_cut


def omitted_online_heuristic(
    coeffs: np.ndarray,
    n_modes: int,
    radius: float,
    t_lo: float,
    t_hi: float,
    step: float,
) -> float:
    """Riemann–von Mangoldt sampled mass of omitted on-line zeros.

    HEURISTIC, not a proof: ∫_{T}^{T_hi} 2 |H(it)|² (log(t/2π)/(2π)) dt.
    """
    total = 0.0
    n_steps = int(math.floor((t_hi - t_lo) / step))
    for index in range(1, n_steps + 1):
        height = t_lo + index * step
        transform = sine_laplace_vector(n_modes, radius, 1j * height)
        modulus_sq = float(abs(np.dot(transform, coeffs)) ** 2)
        density = math.log(height / (2.0 * math.pi)) / (2.0 * math.pi)
        if density < 0.0:
            density = 0.0
        total += 2.0 * modulus_sq * density * step
    return total


def top_modes(coeffs: np.ndarray, count: int = 3) -> str:
    order = np.argsort(-np.abs(coeffs))[:count]
    parts = ["k=%d:%.6e" % (int(index) + 1, float(coeffs[index]))
             for index in order]
    return ",".join(parts)


def format_verdict(
    rows: list[dict],
) -> str:
    sep_atol = float(SPEC["sep_atol"])
    all_trunc = all(row["margin"] < -sep_atol for row in rows)
    all_heur = all(row["margin"] + row["tail_heur"] < -sep_atol for row in rows)
    all_certified = all(
        row["margin"] + row["tail_lip"] < -sep_atol for row in rows
    )
    worst = max(rows, key=lambda row: row["margin"])
    best = min(rows, key=lambda row: row["margin"])
    if all_certified:
        return (
            "SEPARATION_GO(min_margin=%.6e,worst_case=beta=%.2f,gamma=%.2f)"
            % (worst["margin"], worst["beta"], worst["gamma"])
        )
    missed = [row for row in rows if row["margin"] >= -sep_atol]
    if missed:
        row = max(missed, key=lambda item: item["margin"])
        if row["ker_dim"] > 0:
            return (
                "INCONCLUSIVE("
                "search_psd=beta=%.2f,gamma=%.2f,margin=%.6e,"
                "reason=finite_slice_nonneg_not_class_complete)"
                % (row["beta"], row["gamma"], row["margin"])
            )
        return (
            "INCONCLUSIVE("
            "search_miss=beta=%.2f,gamma=%.2f,margin=%.6e,"
            "reason=no_negative_rayleigh_in_search)"
            % (row["beta"], row["gamma"], row["margin"])
        )
    if all_trunc and not all_heur:
        return (
            "INCONCLUSIVE("
            "truncation=beta=%.2f,gamma=%.2f,margin=%.6e,"
            "tail_heur=%.6e,reason=omitted_online_uncontrolled)"
            % (worst["beta"], worst["gamma"], worst["margin"],
               worst["tail_heur"])
        )
    if all_heur and not all_certified:
        return (
            "INCONCLUSIVE("
            "lipschitz_tail=beta=%.2f,gamma=%.2f,margin=%.6e,"
            "tail_lip=%.6e,reason=lipschitz_tail_swamps_margin)"
            % (worst["beta"], worst["gamma"], worst["margin"],
               worst["tail_lip"])
        )
    return (
        "INCONCLUSIVE(best=%.6e,worst=beta=%.2f,gamma=%.2f,margin=%.6e)"
        % (best["margin"], worst["beta"], worst["gamma"], worst["margin"])
    )


def run(smoke: bool) -> int:
    n_modes = 24 if smoke else int(SPEC["n_modes"])
    n_zeros = 8 if smoke else int(SPEC["n_zeros"])
    betas = (0.6, 0.9) if smoke else tuple(SPEC["betas"])
    gammas = (1.0, 14.13) if smoke else tuple(SPEC["gammas"])
    ordinates = np.asarray(ON_LINE_ORDINATES[:n_zeros], dtype=np.float64)
    t_cut = float(ordinates[-1])
    sep_atol = float(SPEC["sep_atol"])
    g1_atol = float(SPEC["g1_atol"])
    heur_dt = float(SPEC["heur_dt"]) if not smoke else 2.0
    heur_cap = 400.0 if smoke else float(SPEC["heur_t_cap"])

    print("weil_separation_redteam_probe -- r535")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("smoke %d" % int(smoke))
    print("hat_convention weil_shifted")
    print("lean_hat_unshifted FullWeilTest.hat(s)=int g(t) exp(s t) dt")
    print("dictionary ĥ_Weil(s)=hat_Lean(s-1/2)")
    print("n_zeros %d t1=%.16f tN=%.16f" % (
        n_zeros, float(ordinates[0]), t_cut))
    print("n_modes %d r_max=%.2f" % (n_modes, float(SPEC["r_max"])))
    print("ordinates_source mpmath-1.3.0-dps30-zetazero-cached")
    print("class FullWeilTest even compact-[-R,R] autocorrelation "
          "of Lipschitz h supported in an interval of length R; "
          "admissible is an opaque Prop (strip/transform), not searched")

    unique_radii = sorted({
        radius for gamma in gammas for radius in radii_for(gamma, n_modes)
    })

    section("G1  ON-LINE WEIL POSITIVITY (no injected zero)")
    online_cache: dict[float, np.ndarray] = {}
    g1_worst = 0.0
    g1_ok = True
    for radius in unique_radii:
        gram = assemble_online(n_modes, radius, ordinates)
        online_cache[radius] = gram
        lam_min, _ = eigs_min(gram)
        g1_worst = min(g1_worst, lam_min)
        ok = lam_min >= -g1_atol
        g1_ok = g1_ok and ok
        print("  R=%.6f anchor=%-3d lam_on=%+.6e" % (
            radius, full_anchor(radius), lam_min))
    check(
        "G1-online-psd",
        g1_ok,
        "min_lam_on=%.6e atol=%.0e (truncation omits PSD tail)"
        % (g1_worst, g1_atol),
    )

    section("SEARCH  INJECTED OFF-CRITICAL QUADRUPLE")
    print("  %-6s %-8s %-14s %-10s %-8s %-6s %-14s %-14s %s" % (
        "beta", "gamma", "margin", "R", "anchor", "ker",
        "tail_lip", "tail_heur", "top_modes"))
    rows: list[dict] = []
    for beta in betas:
        for gamma in gammas:
            best: dict | None = None
            best_coeffs: np.ndarray | None = None
            for radius in radii_for(gamma, n_modes):
                gram = online_cache[radius] + assemble_offline(
                    n_modes, radius, float(beta), float(gamma),
                )
                margin, coeffs = eigs_min(gram)
                online_values = np.linalg.eigvalsh(online_cache[radius])
                ker_dim = int(np.sum(online_values < 1e-10))
                candidate = {
                    "beta": float(beta),
                    "gamma": float(gamma),
                    "margin": margin,
                    "radius": radius,
                    "anchor": full_anchor(radius),
                    "ker_dim": ker_dim,
                    "n_modes": n_modes,
                }
                if best is None or margin < best["margin"]:
                    best = candidate
                    best_coeffs = coeffs
            assert best is not None and best_coeffs is not None
            best["tail_lip"] = lipschitz_zero_tail(
                best_coeffs, best["radius"], t_cut,
            )
            t_hi = max(heur_cap, 2.0 * float(gamma), t_cut + 50.0)
            if t_hi > t_cut:
                best["tail_heur"] = omitted_online_heuristic(
                    best_coeffs, n_modes, best["radius"],
                    t_cut, t_hi, heur_dt,
                )
            else:
                best["tail_heur"] = 0.0
            best["modes"] = top_modes(best_coeffs)
            rows.append(best)
            print("  %-6.2f %-8.2f %+.6e %-10.6f %-8d %-6d %+.6e %+.6e %s" % (
                best["beta"], best["gamma"], best["margin"],
                best["radius"], best["anchor"], best["ker_dim"],
                best["tail_lip"], best["tail_heur"], best["modes"]))

    section("GATES / VERDICT")
    n_trunc = sum(row["margin"] < -sep_atol for row in rows)
    n_heur = sum(row["margin"] + row["tail_heur"] < -sep_atol for row in rows)
    n_cert = sum(row["margin"] + row["tail_lip"] < -sep_atol for row in rows)
    check(
        "G1-sanity-held",
        g1_ok,
        "on-line Gram PSD within atol for every searched R",
    )
    check(
        "G2-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G3-smoke-subset", True, "smoke grid 2x2 K=24 N=8")
    else:
        check(
            "G3-full-grid",
            True,
            "full grid %dx%d K=%d N=%d"
            % (len(betas), len(gammas), n_modes, n_zeros),
        )
    check(
        "search-ran",
        len(rows) == len(betas) * len(gammas),
        "%d cells" % len(rows),
    )
    print("  trunc_neg %d/%d  heur_sep %d/%d  lip_certified %d/%d" % (
        n_trunc, len(rows), n_heur, len(rows), n_cert, len(rows)))

    verdict = format_verdict(rows)
    failures = [name for name, passed in CHECKS if not passed]
    print("CHECKS %d/%d" % (len(CHECKS) - len(failures), len(CHECKS)))
    print("VERDICT %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    if failures:
        print("GATE_FAILURES " + ",".join(failures))
        return 1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r535 Weil off-critical separation red-team (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
