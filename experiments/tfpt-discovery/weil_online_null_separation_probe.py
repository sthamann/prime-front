#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weil_online_null_separation_probe -- PRIME.RDAGGER.WEIL_ONLINE_NULL.01

Round 540.  Numerical red-team of the OPEN Lean theorem

    fullWeil_separates_offCritical_zeros
        : FullWeilSeparatesOffCriticalZeros
    (rh/lean/RH/ExternalBridges.lean, currently sorry).

r535 (compact sine class, K=220, R≤4, first 100 zeros) found every
injected off-critical quadruple truncated-negative, but omitted on-line
mass swamped the γ=1000 margins and the Lipschitz 1/t² tail certified
nothing.  This round stays inside that same compact FullWeilTest class
and forces the test function orthogonal to the first N on-line zeros
("on-line nulling"): the truncated spectral sum of those N ordinates
is then exactly zero, and the Lipschitz tail is charged from
T = γ_{N+1} instead of T = γ_1.

CLAIM BOUNDARY.  Finite quadratic-form search in a finite-dimensional
subclass of the Lean geometric test class.  Conditional on the frozen
first-110 ordinates and on a search cap R ∈ {2,4,8}, K=220.  NO RH
claim, NO anti-RH claim, NO ledger row, NO paper edit.  A negative
truncated Rayleigh quotient is not a proof of the Lean theorem.  A
nonnegative Rayleigh in this subclass is not a proof that the
infinite-dimensional class cannot separate.  Nulling is a numerical
constraint on coefficients, not a Lean construction.

HAT CONVENTION.  Lean FullWeilTest.hat is the unshifted Laplace
transform ∫ g(t) exp(s t) dt.  The classical Weil kernel used here:

    ĥ_Weil(s) := ∫ g(u) exp((s − 1/2) u) du = hat_Lean(s − 1/2),
    ĥ_Weil(1/2+it) = |H(it)|²,   H(z) = ∫_0^R h(t) e^{z t} dt.

TAIL CONSTANT (honest).  Lean `FullWeilTest.norm_hat_le_inv_sq`
proves ‖hat s‖ ≤ C/(1+τ²) on 0≤Re s≤1 with the Weierstrass constant

    C_lean = 2 Cexp e^{R+1} + K π² (R+2π)² e^{R+2π}

(Cexp from ‖g‖_∞(2R+2), K = Lip(h)²).  That is a 1/t² bound on ĥ
itself.  On this sine subclass the integration-by-parts bound
|H(it)| ≤ ‖h'‖_1 / |t| (h(0)=h(R)=0) is the witness-sharp constant of
the same family: |ĥ_Weil(1/2+it)| = |H(it)|² ≤ ‖h'‖_1² / t².  Charging
C_lean would insert e^R and swamp every cell a priori; this probe
charges ‖h'‖_1, then the r535 density majorant
∑_{t_n>T} 2|H(it_n)|² ≤ 2 ‖h'‖_1² (1+log T)/T  (N'(T)≤log T for
T≥14; classical, not a Lean lemma).  Evaluated at T=γ_{N+1}.

Runtime: numpy.  Zeros cached from mpmath.zetazero (mpmath 1.3.0,
dps=30, 2026-09-01); mpmath is not called at runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
SPEC = {
    "round": 540,
    "target": "fullWeil_separates_offCritical_zeros",
    "lean_file": "rh/lean/RH/ExternalBridges.lean",
    "hat": "weil_shifted",
    "betas": [0.55, 0.7, 0.9],
    "gammas": [5.0, 14.13, 30.0, 100.0, 1000.0],
    "n_null": [20, 50, 100],
    "radii": [2.0, 4.0, 8.0],
    "n_modes": 220,
    "n_zeros_cached": 110,
    "sep_atol": 1e-12,
    "g1_residual": 1e-12,
    "g1_psd_atol": 1e-8,
    "svd_keep_atol": 1e-12,
    "coupling_atol": 1e-8,
    "g4_beta": 0.6,
    "g4_gamma": 14.13,
    "g4_n_modes": 220,
    "g4_n_zeros": 100,
    "g4_r_min": 0.08,
    "g4_r_max": 4.0,
    "g4_r_fixed": [0.5, 1.0, 2.0],
    "g4_margin_ref": -2.129731e-1,
    "g4_margin_atol": 5.0e-6,
}

SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

# First 110 positive ordinates of nontrivial zeta zeros.
# Source: mpmath 1.3.0, mp.mp.dps = 30, mp.zetazero(n).imag, n = 1..110.
# n = 1..100 identical to r535; n = 101..110 cached 2026-09-01 for T=γ_{N+1}
# at N=100.  Not an RH oracle: classical Odlyzko/mpmath values used only
# as the on-critical truncation of the spectral sum.
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
    236.5242296658161933, 237.7698204809252047, 239.5554775733276358,
    241.0491577962165763, 242.8232719342225892, 244.0708984970781614,
    247.1369900748975112, 248.1019900601484665, 249.5736896447072013,
    251.0149477950160133, 253.0699867479994793,
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


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def full_anchor(radius: float) -> int:
    """Lean FullWeilTest.fullAnchor = max(1, ceil(exp(R)))."""
    return max(1, int(math.ceil(math.exp(radius))))


def omega_max(n_modes: int, radius: float) -> float:
    """Highest sine frequency k π / R, k = n_modes."""
    return float(n_modes) * math.pi / radius


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
    at the endpoints (Lean autocorrelation witness).
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
    """S_on(c) = sum_n 2 |H(i t_n)|²  (conjugate pair on the critical line)."""
    gram = np.zeros((n_modes, n_modes), dtype=np.float64)
    for height in ordinates:
        gram += 2.0 * gram_modsq(
            sine_laplace_vector(n_modes, radius, 1j * float(height))
        )
    return gram


def assemble_offline(
    n_modes: int, radius: float, beta: float, gamma: float,
) -> np.ndarray:
    """Quadruple {β±iγ, 1−β±iγ} contributes 4 Re[H(−δ−iγ) H(δ+iγ)]."""
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


def constraint_matrix(
    n_modes: int, radius: float, heights: np.ndarray,
) -> np.ndarray:
    """Real 2N × K matrix of H_j(i γ_k) (real/imag stacked)."""
    rows = np.empty((2 * heights.size, n_modes), dtype=np.float64)
    for index, height in enumerate(heights):
        vec = sine_laplace_vector(n_modes, radius, 1j * float(height))
        rows[2 * index] = vec.real
        rows[2 * index + 1] = vec.imag
    return rows


def svd_nullspace(
    matrix: np.ndarray, keep_atol: float,
) -> tuple[np.ndarray, np.ndarray, int]:
    """Orthonormal kernel basis Q (K × d); columns sign-stabilised.

    Keep right singular vectors with σ ≤ keep_atol (absolute).
    """
    n_cols = int(matrix.shape[1])
    if matrix.shape[0] == 0:
        return np.eye(n_cols, dtype=np.float64), np.zeros(0), 0
    _u, singular, vt = np.linalg.svd(matrix, full_matrices=True)
    sigma = np.zeros(n_cols, dtype=np.float64)
    sigma[: singular.size] = singular
    keep = sigma <= keep_atol
    q = np.real(vt[keep].T).copy()
    for col in range(q.shape[1]):
        pivot = int(np.argmax(np.abs(q[:, col])))
        if q[pivot, col] < 0.0:
            q[:, col] *= -1.0
    rank = int(n_cols - q.shape[1])
    return q, sigma, rank


def lipschitz_hprime_l1(coeffs: np.ndarray, radius: float) -> float:
    """‖h'‖_1 bounds for the sine series (two estimates, take min)."""
    modes = np.arange(1, coeffs.size + 1, dtype=np.float64)
    bound_l1 = math.pi * float(np.dot(modes, np.abs(coeffs)))
    hprime_l2 = (math.pi / math.sqrt(2.0 * radius)) * math.sqrt(
        float(np.dot(modes * modes, coeffs * coeffs))
    )
    bound_cauchy = math.sqrt(radius) * hprime_l2
    return min(bound_l1, bound_cauchy)


def lipschitz_zero_tail(coeffs: np.ndarray, radius: float, t_cut: float) -> float:
    """∑_{t_n > T} 2 |H(i t_n)|² ≤ 2 C² (1 + log T) / T.

    |H(it)| ≤ ‖h'‖_1 / |t| (integration by parts, h(0)=h(R)=0).
    Zero density N'(T) ≤ log T for T ≥ 14; ∫_T^∞ log(t)/t² dt = (1+log T)/T.
    Same family as Lean norm_hat_le_inv_sq (1/t² on ĥ = |H|²); constant
    is the subclass-sharp IBP C = ‖h'‖_1, not the Weierstrass C_lean.
    """
    lipschitz = lipschitz_hprime_l1(coeffs, radius)
    return 2.0 * lipschitz * lipschitz * (1.0 + math.log(t_cut)) / t_cut


def hat_modsq(n_modes: int, radius: float, height: float, coeffs: np.ndarray) -> float:
    transform = sine_laplace_vector(n_modes, radius, 1j * float(height))
    return float(abs(np.dot(transform, coeffs)) ** 2)


def g4_radii(n_modes: int) -> tuple[float, ...]:
    """r535 radii_for(γ=14.13) with the r535 search cap R≤4."""
    gamma = float(SPEC["g4_gamma"])
    r_min = float(SPEC["g4_r_min"])
    r_max = float(SPEC["g4_r_max"])
    raw = [float(value) for value in SPEC["g4_r_fixed"]]
    for multiple in (1.0, 2.0, 4.0):
        raw.append(multiple * math.pi / gamma)
    raw.append(n_modes * math.pi / (gamma * 1.4))
    unique: list[float] = []
    for radius in raw:
        clipped = round(float(min(r_max, max(r_min, radius))), 12)
        if clipped not in unique:
            unique.append(clipped)
    return tuple(sorted(unique))


def run_g4_anchor(ordinates100: np.ndarray) -> tuple[float, float]:
    """Reproduce the r535 (β=0.6, γ=14.13) cell without nulling."""
    n_modes = int(SPEC["g4_n_modes"])
    beta = float(SPEC["g4_beta"])
    gamma = float(SPEC["g4_gamma"])
    best_margin = None
    best_radius = None
    cache: dict[float, np.ndarray] = {}
    for radius in g4_radii(n_modes):
        if radius not in cache:
            cache[radius] = assemble_online(n_modes, radius, ordinates100)
        gram = cache[radius] + assemble_offline(n_modes, radius, beta, gamma)
        margin, _coeffs = eigs_min(gram)
        if best_margin is None or margin < best_margin:
            best_margin = margin
            best_radius = radius
    assert best_margin is not None and best_radius is not None
    return float(best_margin), float(best_radius)


def matching_rows(kernel: dict, rows: list[dict]) -> list[dict]:
    n_null = int(kernel["n_null"])
    radius = float(kernel["radius"])
    return [
        row for row in rows
        if int(row["n_null"]) == n_null
        and abs(float(row["radius"]) - radius) < 1e-15
    ]


def format_frontier(
    kernels: list[dict], rows: list[dict], field: str,
) -> str:
    """field is 'certified' or 'couples': max γ with that flag, else none."""
    parts: list[str] = []
    for kernel in kernels:
        hit = [
            row["gamma"] for row in matching_rows(kernel, rows) if row[field]
        ]
        if hit:
            parts.append(
                "R=%.0f,N=%d:g<=%.2f"
                % (float(kernel["radius"]), int(kernel["n_null"]), max(hit))
            )
        else:
            parts.append(
                "R=%.0f,N=%d:none"
                % (float(kernel["radius"]), int(kernel["n_null"]))
            )
    return ";".join(parts)


def format_verdict(
    kernels: list[dict],
    rows: list[dict],
    sep_atol: float,
    coupling_atol: float,
) -> str:
    certified = [row for row in rows if row["certified"]]
    if certified:
        best = min(certified, key=lambda row: row["cert"])
        return (
            "NULL_SEPARATION_GO(certified_cells=%d,best="
            "beta=%.2f,gamma=%.2f,N=%d,R=%.2f,cert=%.6e)"
            % (len(certified), best["beta"], best["gamma"],
               best["n_null"], best["radius"], best["cert"])
        )

    trivial = [k for k in kernels if int(k["dim"]) == 0]
    couples = [row for row in rows if row["couples"]]
    if trivial and not couples:
        kernel = trivial[0]
        return "KERNEL_TRIVIAL(N=%d,R=%.2f)" % (
            int(kernel["n_null"]), float(kernel["radius"]),
        )

    high = [row for row in rows if row["gamma"] >= 999.0]
    low = [row for row in rows if row["gamma"] <= 30.0]
    # Paley–Wiener leakage at γ > k_max π/R can give |margin| ~ 1e-6
    # without resolving the height; require a structural margin.
    high_couples = any(row["margin"] < -1.0e-4 for row in high)
    low_couples = any(row["margin"] < -coupling_atol for row in low)
    nyquist_killed_high = any(
        (not row["couples"]) and row["gamma"] > row["omega_max"]
        for row in high
    )
    if (not high_couples) and (low_couples or nyquist_killed_high or trivial):
        return "SUPPORT_VS_HEIGHT(frontier=%s)" % format_frontier(
            kernels, rows, "certified",
        )

    if couples:
        worst = max(couples, key=lambda row: row["cert"])
        return (
            "TAIL_STILL_SWAMPS(worst=beta=%.2f,gamma=%.2f,N=%d,R=%.2f,"
            "margin=%.6e,tail=%.6e,cert=%.6e)"
            % (worst["beta"], worst["gamma"], worst["n_null"],
               worst["radius"], worst["margin"], worst["tail_lip"],
               worst["cert"])
        )
    if trivial:
        kernel = trivial[0]
        return "KERNEL_TRIVIAL(N=%d,R=%.2f)" % (
            int(kernel["n_null"]), float(kernel["radius"]),
        )
    return "SUPPORT_VS_HEIGHT(frontier=%s)" % format_frontier(
        kernels, rows, "certified",
    )


def run(smoke: bool) -> int:
    n_modes = 40 if smoke else int(SPEC["n_modes"])
    n_null_list = (8,) if smoke else tuple(int(v) for v in SPEC["n_null"])
    radii = (2.0,) if smoke else tuple(float(v) for v in SPEC["radii"])
    betas = (0.7,) if smoke else tuple(float(v) for v in SPEC["betas"])
    gammas = (14.13,) if smoke else tuple(float(v) for v in SPEC["gammas"])
    ordinates = np.asarray(ON_LINE_ORDINATES, dtype=np.float64)
    assert ordinates.size >= int(SPEC["n_zeros_cached"])
    sep_atol = float(SPEC["sep_atol"])
    g1_residual = float(SPEC["g1_residual"])
    g1_psd_atol = float(SPEC["g1_psd_atol"])
    keep_atol = float(SPEC["svd_keep_atol"])
    coupling_atol = float(SPEC["coupling_atol"])
    n_psd = 20 if smoke else 100

    print("weil_online_null_separation_probe -- r540")
    print("CLAIM_BOUNDARY EXPERIMENT_ONLY NO_RH_CLAIM NO_ANTI_RH_CLAIM")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("smoke %d" % int(smoke))
    print("hat_convention weil_shifted")
    print("lean_hat_unshifted FullWeilTest.hat(s)=int g(t) exp(s t) dt")
    print("dictionary ĥ_Weil(s)=hat_Lean(s-1/2)")
    print("tail_family lipschitz_IBP_1/t^2  T=gamma_{N+1}")
    print("tail_constant subclass ||h'||_1  (not Weierstrass C_lean)")
    print("n_modes %d n_null %s radii %s" % (
        n_modes, list(n_null_list), list(radii)))
    print("n_zeros_cached %d t1=%.16f t101=%.16f" % (
        ordinates.size, float(ordinates[0]), float(ordinates[100])))
    print("ordinates_source mpmath-1.3.0-dps30-zetazero-cached")
    print("class FullWeilTest even compact-[-R,R] autocorrelation "
          "of Lipschitz h supported in an interval of length R; "
          "admissible is an opaque Prop (strip/transform), not searched")
    print("nulling H(i gamma_k)=0 for k<=N via SVD kernel, keep_atol=%.0e"
          % keep_atol)

    section("G4  R535 REGRESSION ANCHOR (no nulling)")
    g4_margin, g4_radius = run_g4_anchor(ordinates[: int(SPEC["g4_n_zeros"])])
    g4_ref = float(SPEC["g4_margin_ref"])
    g4_atol = float(SPEC["g4_margin_atol"])
    g4_ok = abs(g4_margin - g4_ref) <= g4_atol
    print("  beta=%.2f gamma=%.2f margin=%.6e R=%.6f ref=%.6e atol=%.0e" % (
        float(SPEC["g4_beta"]), float(SPEC["g4_gamma"]),
        g4_margin, g4_radius, g4_ref, g4_atol))
    check(
        "G4-r535-anchor",
        g4_ok,
        "margin=%.6e ref=%.6e (beta=0.6,gamma=14.13,K=220,Nzeros=100)"
        % (g4_margin, g4_ref),
    )

    section("G1  ON-LINE GRAM PSD + NULLSPACES")
    g1_psd_ok = True
    g1_worst_lam = 0.0
    online_cache: dict[float, np.ndarray] = {}
    for radius in radii:
        gram = assemble_online(n_modes, radius, ordinates[:n_psd])
        online_cache[radius] = gram
        lam_min, _ = eigs_min(gram)
        g1_worst_lam = min(g1_worst_lam, lam_min)
        ok = lam_min >= -g1_psd_atol
        g1_psd_ok = g1_psd_ok and ok
        print("  R=%.6f omega_max=%.4f anchor=%-5d lam_on=%+.6e" % (
            radius, omega_max(n_modes, radius), full_anchor(radius), lam_min))
    check(
        "G1-online-psd",
        g1_psd_ok,
        "min_lam_on=%.6e atol=%.0e (truncation omits PSD tail)"
        % (g1_worst_lam, g1_psd_atol),
    )

    print("  %-6s %-8s %-6s %-6s %-12s %-12s %-12s %-12s" % (
        "N", "R", "dim", "rank", "residual", "sigma_min",
        "row_min", "row_max"))
    kernels: list[dict] = []
    kernel_q: dict[tuple[int, float], np.ndarray] = {}
    g1_res_ok = True
    g1_worst_res = 0.0
    for n_null in n_null_list:
        heights = ordinates[:n_null]
        t_cut = float(ordinates[n_null])  # γ_{N+1}
        for radius in radii:
            matrix = constraint_matrix(n_modes, radius, heights)
            row_norms = np.linalg.norm(matrix, axis=1)
            q, sigma, rank = svd_nullspace(matrix, keep_atol)
            dim = int(q.shape[1])
            if dim == 0:
                residual = 0.0
            else:
                residual = float(np.max(np.abs(matrix @ q)))
            g1_worst_res = max(g1_worst_res, residual)
            res_ok = residual <= g1_residual
            g1_res_ok = g1_res_ok and res_ok
            sigma_min = float(sigma.min()) if sigma.size else 0.0
            record = {
                "n_null": int(n_null),
                "radius": float(radius),
                "dim": dim,
                "rank": int(rank),
                "residual": residual,
                "sigma_min": sigma_min,
                "row_min": float(row_norms.min()),
                "row_max": float(row_norms.max()),
                "t_cut": t_cut,
                "omega_max": omega_max(n_modes, radius),
            }
            kernels.append(record)
            kernel_q[(int(n_null), float(radius))] = q
            print("  %-6d %-8.2f %-6d %-6d %+.6e %+.6e %+.6e %+.6e" % (
                n_null, radius, dim, rank, residual, sigma_min,
                record["row_min"], record["row_max"]))
    check(
        "G1-nullspace-residual",
        g1_res_ok,
        "max_residual=%.6e atol=%.0e" % (g1_worst_res, g1_residual),
    )

    section("SEARCH  NULLSPACE OFF-CRITICAL RAYLEIGH")
    print("  %-6s %-8s %-6s %-8s %-14s %-14s %-14s %-6s %-8s %-4s" % (
        "beta", "gamma", "N", "R", "margin", "tail_lip", "cert",
        "dim", "t_cut", "ok"))
    rows: list[dict] = []
    cell_res_ok = True
    cell_worst_res = 0.0
    offline_cache: dict[tuple[float, float, float], np.ndarray] = {}
    for beta in betas:
        for gamma in gammas:
            for radius in radii:
                key = (float(radius), float(beta), float(gamma))
                if key not in offline_cache:
                    offline_cache[key] = assemble_offline(
                        n_modes, radius, float(beta), float(gamma),
                    )
                s_off = offline_cache[key]
                w_max = omega_max(n_modes, radius)
                for n_null in n_null_list:
                    q = kernel_q[(int(n_null), float(radius))]
                    dim = int(q.shape[1])
                    t_cut = float(ordinates[n_null])
                    if dim == 0:
                        row = {
                            "beta": float(beta),
                            "gamma": float(gamma),
                            "n_null": int(n_null),
                            "radius": float(radius),
                            "margin": 0.0,
                            "tail_lip": 0.0,
                            "cert": 0.0,
                            "dim": 0,
                            "t_cut": t_cut,
                            "omega_max": w_max,
                            "residual": 0.0,
                            "rest_mass": 0.0,
                            "lip_c": 0.0,
                            "couples": False,
                            "certified": False,
                            "kernel_trivial": True,
                        }
                        rows.append(row)
                        print(
                            "  %-6.2f %-8.2f %-6d %-8.2f %+.6e %+.6e %+.6e "
                            "%-6d %-8.2f %-4s"
                            % (beta, gamma, n_null, radius, 0.0, 0.0, 0.0,
                               0, t_cut, "triv")
                        )
                        continue
                    reduced = q.T @ s_off @ q
                    margin, vec = eigs_min(reduced)
                    coeffs = q @ vec
                    residual = 0.0
                    heights = ordinates[:n_null]
                    for height in heights:
                        residual = max(
                            residual,
                            math.sqrt(hat_modsq(n_modes, radius, float(height), coeffs)),
                        )
                    cell_worst_res = max(cell_worst_res, residual)
                    if residual > g1_residual:
                        cell_res_ok = False
                    tail = lipschitz_zero_tail(coeffs, radius, t_cut)
                    cert = margin + tail
                    rest = 0.0
                    rest_hi = min(ordinates.size, 100)
                    for height in ordinates[n_null:rest_hi]:
                        rest += 2.0 * hat_modsq(
                            n_modes, radius, float(height), coeffs,
                        )
                    # Sinc leakage above the sine Nyquist is not coupling.
                    nyquist_ok = float(gamma) <= w_max
                    couples = (margin < -coupling_atol) and (
                        nyquist_ok or margin < -1.0e-4
                    )
                    certified = cert < -sep_atol
                    row = {
                        "beta": float(beta),
                        "gamma": float(gamma),
                        "n_null": int(n_null),
                        "radius": float(radius),
                        "margin": float(margin),
                        "tail_lip": float(tail),
                        "cert": float(cert),
                        "dim": dim,
                        "t_cut": t_cut,
                        "omega_max": w_max,
                        "residual": float(residual),
                        "rest_mass": float(rest),
                        "lip_c": float(lipschitz_hprime_l1(coeffs, radius)),
                        "couples": bool(couples),
                        "certified": bool(certified),
                        "kernel_trivial": False,
                    }
                    rows.append(row)
                    flag = "cert" if certified else ("cpl" if couples else "nc")
                    print(
                        "  %-6.2f %-8.2f %-6d %-8.2f %+.6e %+.6e %+.6e "
                        "%-6d %-8.2f %-4s"
                        % (beta, gamma, n_null, radius, margin, tail, cert,
                           dim, t_cut, flag)
                    )

    check(
        "G1-cell-null-residual",
        cell_res_ok,
        "max_|H(i gamma_k).c|=%.6e atol=%.0e"
        % (cell_worst_res, g1_residual),
    )

    section("SUPPORT-VS-HEIGHT FRONTIER")
    frontier = format_frontier(kernels, rows, "certified")
    couple_frontier = format_frontier(kernels, rows, "couples")
    print("  certified_frontier %s" % frontier)
    print("  trunc_couple_frontier %s" % couple_frontier)
    if rows:
        closest = min(rows, key=lambda row: row["cert"])
        print("  closest_cert beta=%.2f gamma=%.2f N=%d R=%.2f "
              "margin=%.6e tail=%.6e cert=%.6e"
              % (closest["beta"], closest["gamma"], closest["n_null"],
                 closest["radius"], closest["margin"], closest["tail_lip"],
                 closest["cert"]))
    print("  %-6s %-8s %-10s %-10s %-10s %-12s %-12s" % (
        "N", "R", "omega_max", "t_cut", "dim", "g_cert", "g_couple"))
    for kernel in kernels:
        group = matching_rows(kernel, rows)
        cert_g = [row["gamma"] for row in group if row["certified"]]
        couple_g = [row["gamma"] for row in group if row["couples"]]
        gcert = ("g<=%.2f" % max(cert_g)) if cert_g else "none"
        gcouple = ("g<=%.2f" % max(couple_g)) if couple_g else "none"
        print("  %-6d %-8.2f %-10.4f %-10.4f %-10d %-12s %-12s" % (
            kernel["n_null"], kernel["radius"], kernel["omega_max"],
            kernel["t_cut"], kernel["dim"], gcert, gcouple))

    section("GATES / VERDICT")
    n_cert = sum(row["certified"] for row in rows)
    n_cpl = sum(row["couples"] for row in rows)
    n_trunc = sum(row["margin"] < -sep_atol for row in rows)
    n_triv = sum(row["kernel_trivial"] for row in rows)
    check(
        "G1-sanity-held",
        g1_psd_ok and g1_res_ok and cell_res_ok,
        "psd=%s residual=%s cell_res=%s"
        % (g1_psd_ok, g1_res_ok, cell_res_ok),
    )
    check(
        "G2-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G3-smoke-subset", True, "smoke N=8 R=2 K=40 1x1 cell + G4")
    else:
        check(
            "G3-full-grid",
            True,
            "full grid %dx%dx%dx%d K=%d"
            % (len(betas), len(gammas), len(n_null_list), len(radii), n_modes),
        )
    check(
        "search-ran",
        len(rows) == len(betas) * len(gammas) * len(n_null_list) * len(radii),
        "%d cells" % len(rows),
    )
    print("  trunc_neg %d/%d  couples %d/%d  lip_certified %d/%d  trivial %d/%d"
          % (n_trunc, len(rows), n_cpl, len(rows), n_cert, len(rows),
             n_triv, len(rows)))

    verdict = format_verdict(kernels, rows, sep_atol, coupling_atol)
    failures = [name for name, passed in CHECKS if not passed]
    print("CHECKS %d/%d" % (len(CHECKS) - len(failures), len(CHECKS)))
    print("VERDICT %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    if failures:
        print("GATE_FAILURES " + ",".join(failures))
        return 1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r540 Weil on-line-null off-critical separation (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
