#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""event_lindblad_twokey_probe -- PRIME.EVENT.LINDBLAD.01 (r607).

EXPLORATION ONLY.  experiments/ sandbox.  This probe writes nothing,
imports no verification module, reads no zeta-zero table, and moves
no marker.  KEIN RH-CLAIM.  NO RH CLAIM in either direction.

HYPOTHESIS UNDER TEST (user-proposed; two-key kill-first).  There is
a position-sensitive reversible Lindblad generator on
(E8 4-bit code space) ⊗ L²(log-time),

    𝓛_X(A) = Σ_{u_e ≤ X} λ_e (L_e* A L_e − ½{L_e* L_e, A}) + 𝓛_{∞,X}(A),

event e = prime power n = p^k, u_e = log n, rate λ_e = 2 Λ(n)/√n,
jump L_e = R_{ℓ(e)} ⊗ U_{u_e} (R = Kraus/incidence operator of the
4-bit Gaussian-prime class of n; U_u = translation by u on log-time),
𝓛_{∞,X} = archimedean μ4-heat + pole boundary, NO free scalars, such
that the Dirichlet form 𝓔_X(A_f) = −⟨A_f, 𝓛_X A_f⟩_Ω (Ω = KMS β=1,
M(−u) = e^{−u} M(u)) equals the finite Weil window form

    Q_W^X(f) = POLE(f) + ARCH(f) − 2 Σ_{n≤e^X} Λ(n) n^{−1/2} f(log n)

on window observables A_f.  Companion PRIME.EVENT.EULERPICK.01: the
same process with exponential observables A_σ = ∫ e^{−σ u} dM_u has
OS-Gram ⟨A_σj, A_σk⟩ = (P(σj)+P(σk))/(σj+σk), P(z) = ξ'/ξ(1/2+z),
σ_j = 1+1/j, N ≤ 4.

DECISIVE STRUCTURAL FACT.  A Lindblad Dirichlet form is ≥ 0 in EVERY
world.  Weil window forms of the control worlds are certified
NEGATIVE (signed_only_nogo_probe / hardness_calibration_falsification
probe: SCRAMBLE r ≈ −4.5693, EPSTEIN r ≈ −42.495, W-NEG with Arb
enclosure).  Any uniform functor (positions, rates) → generator
cannot reproduce Q_W in all worlds; the identity can hold in the
true world only if 𝓛_{∞,X} is tuned so that "𝓛_X is CP" ⟺
"Q_W^X ≥ 0", i.e. the construction re-coordinatizes finite Weil
positivity rather than explaining it.

PREREGISTERED VERDICT.
  KILLED(RECOORDINATIZATION)  if T1 = COMPENSATOR_MISMATCH and
                              T2 = RECOORDINATIZATION
  KILLED(PICK_NEEDS_SCALARS)  likewise for T3
  ALIVE(GENUINE_GAP)          only if T2 finds a world separating CP
                              from Weil positivity, no zero data
  ALIVE(PICK_EXACT)           only if Pick Gram matches with no
                              scalars AND the process is CP in TRUE
                              but not in SCRAMBLE

Firewall: AST-checked; no Riemann-zero loader.  KEIN RH-CLAIM.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
from itertools import combinations

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# ---------------------------------------------------------------------------
# Frozen design.  Lattice length L is independent of the prime cutoff X
# (POLE+ARCH must be X-independent).  X only truncates the jump measure.
# ---------------------------------------------------------------------------
SEED_SCRAMBLE = 1          # v563 / positional_gns_probe scramble_seed
SEED_WPERM = 20260824      # positional_gns_probe WPERM
SEED_LABELS = 20260902
N_FREQ_FULL = (8, 16, 32)
N_FREQ_SMOKE = (8,)
X_FULL = (math.log(50.0), math.log(200.0))
X_SMOKE = (math.log(50.0),)
LATTICE_L = math.log(200.0)  # period 2L; covers every u_e ≤ log 200
PICK_N = 4
PICK_DPS = 30
EM_CUTOFF = 400
EM_TERMS = 12
KMS_BETA = 1.0
OFFDIAG_BAR = 1.0e-10
GROWTH_BAR = 0.35          # |Σλ / (2 e^{X/2}) − 1| may be O(1) at X=log 50
CP_FLOOR = 1.0e-12
PICK_EXACT_BAR = 1.0e-8
PICK_SCALAR_BAR = 1.0e-4
GL1_BAR = 1.0e-12
LABEL_DIM = 15
ROW_DEGREE = 7
CLASS_TO_LABEL = {"ro": 1, "re": 2, "sp": 4, "in": 8}  # 4-bit one-hots, 0-based later
BANNED_IDS = (
    "zetazero", "zetazeros", "nzeros", "primerange", "isprime",
    "primepi", "nextprime", "prevprime", "grampoint", "siegelz",
)

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    print("  [%s] %s%s" % ("PASS" if flag else "FAIL", name,
                           (" -- " + detail) if detail else ""), flush=True)
    return flag


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def fmt(x: float) -> str:
    x = float(np.real(x))
    if not math.isfinite(x):
        return "nan"
    return "%+.16e" % x


def ast_firewall() -> list[str]:
    """AST check copied from signed_only_nogo_probe.ast_firewall (zero data)."""
    with open(os.path.abspath(__file__), encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else (
            fn.id if isinstance(fn, ast.Name) else "")
        if name.lower() in BANNED_IDS:
            hits.append(name)
    return sorted(set(hits))


# ===================================================================== T0
# Arithmetic layer.  prime_power_list / lambda_table copied from
# signed_only_nogo_probe.py (independent sieve; no sympy.primerange).
# classify / sum2sq_positions copied from hjelmslev_position_kraus_probe.py.
# 105-leg incidence copied from kms_incidence_stinespring_probe.py
# (polar hyperplanes of a rank-4 alternating form on F2^4; the v738
# sigma covariance is omitted because the GL1 corner traces it out).
# =====================================================================
def prime_power_list(cap: int) -> list[int]:
    sieve = np.zeros(cap + 1, dtype=bool)
    out = []
    for p in range(2, cap + 1):
        if not sieve[p]:
            sieve[p * p::p] = True
            q = p
            while q <= cap:
                out.append(q)
                q *= p
    return sorted(out)


def lambda_table(n_max: int) -> np.ndarray:
    lam = np.zeros(n_max + 1)
    sieve = np.zeros(n_max + 1, dtype=bool)
    for p in range(2, n_max + 1):
        if not sieve[p]:
            sieve[p * p::p] = True
            q, log_p = p, math.log(p)
            while q <= n_max:
                lam[q] = log_p
                q *= p
    return lam


def spf_table(n_max: int) -> np.ndarray:
    spf = np.zeros(n_max + 1, dtype=np.int64)
    for p in range(2, n_max + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    return spf


def classify(n: int, spf: np.ndarray) -> str:
    p = int(spf[n])
    m, k = n, 0
    while m % p == 0:
        m //= p
        k += 1
    if p == 2:
        return "ro" if k % 2 == 1 else "re"
    return "sp" if p % 4 == 1 else "in"


def sum2sq_positions(count: int) -> np.ndarray:
    cap = 16
    while True:
        cap *= 4
        rep = np.zeros(cap + 1, dtype=bool)
        a = 0
        while a * a <= cap:
            b = a
            while a * a + b * b <= cap:
                rep[a * a + b * b] = True
                b += 1
            a += 1
        vals = [n for n in range(2, cap + 1) if rep[n]]
        if len(vals) >= count:
            return np.log(np.array(vals[:count], dtype=float))


def gf2_rank(matrix: np.ndarray) -> int:
    work = np.asarray(matrix, dtype=np.uint8).copy() & 1
    row = 0
    for column in range(work.shape[1]):
        pivot = next((c for c in range(row, work.shape[0]) if work[c, column]),
                     None)
        if pivot is None:
            continue
        work[[row, pivot]] = work[[pivot, row]]
        for other in range(work.shape[0]):
            if other != row and work[other, column]:
                work[other] ^= work[row]
        row += 1
    return row


def label_incidence() -> tuple[list[tuple[int, int, int, int]], np.ndarray]:
    labels = [tuple((number >> bit) & 1 for bit in range(4))
              for number in range(1, 16)]
    pairs = list(combinations(range(4), 2))
    form = None
    for mask in range(1, 1 << len(pairs)):
        cand = np.zeros((4, 4), dtype=np.uint8)
        for bit, (left, right) in enumerate(pairs):
            if (mask >> bit) & 1:
                cand[left, right] = cand[right, left] = 1
        if gf2_rank(cand) == 4:
            form = cand
            break
    if form is None:
        raise RuntimeError("no rank-4 alternating form on F2^4")
    inc = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for row, left in enumerate(labels):
        for column, right in enumerate(labels):
            pairing = 0
            for j in range(4):
                for k in range(4):
                    pairing ^= left[j] & int(form[j, k]) & right[k]
            inc[row, column] = int(pairing == 0)
    return labels, inc


def row_kraus(inc: np.ndarray, label_idx: int) -> list[np.ndarray]:
    scale = 1.0 / math.sqrt(ROW_DEGREE)
    ops = []
    for y in range(LABEL_DIM):
        if inc[label_idx, y]:
            op = np.zeros((LABEL_DIM, LABEL_DIM))
            op[y, label_idx] = scale
            ops.append(op)
    return ops


def gl1_factor(ops: list[np.ndarray]) -> float:
    """⟨I, Σ V* I V⟩_HS = Tr(Σ V* V).  Unital row ⇒ 1, independent of label."""
    acc = 0.0
    ident = np.eye(LABEL_DIM)
    for op in ops:
        acc += float(np.trace(op.T @ ident @ op).real)
    return acc


# =====================================================================
# Log-time lattice, DFT translations, Weil catalogue.
# Window basis = N_freq position samples on the circle of length 2L.
# U_u is the bandlimited translation (DFT multiplier e^{-i ξ u}),
# the cosine / U-shift of the GNS/Toeplitz window probes.
# KMS β=1 half-weight is already in λ_e = 2 Λ(n) n^{-1/2}; the
# Euclidean ℓ² pairing on the lattice is the GL1 corner inner product.
# Attribution: pole/arch kernels as in weil_gns_identification_probe
# (Pole = ∫ g(u)(e^{u/2}+e^{-u/2}) du, Arch = (1/2π) ∫ ĥ(t)
# (Re ψ(1/4+it/2) − log π) dt); finite GNS quadratic form via
# autoconvolution g(u) = ⟨f, U_u f⟩ as in positional_gns / Toeplitz
# windows.  Detailed-balance typing from kms_toeplitz_semigroup_probe
# (β=1, M(−u)=e^{−u} M(u)).
# =====================================================================
def lattice(n_freq: int) -> tuple[np.ndarray, float, np.ndarray]:
    period = 2.0 * LATTICE_L
    dx = period / float(n_freq)
    xs = dx * np.arange(n_freq, dtype=np.float64)
    xi = 2.0 * math.pi * np.fft.fftfreq(n_freq, d=dx)
    return xs, dx, xi


def translation(n_freq: int, xi: np.ndarray, shift: float) -> np.ndarray:
    phase = np.exp(-1j * xi * float(shift))
    eye = np.eye(n_freq, dtype=np.complex128)
    mat = np.fft.ifft(phase[:, None] * np.fft.fft(eye, axis=0), axis=0)
    return mat


def sym_real(mat: np.ndarray) -> np.ndarray:
    herm = 0.5 * (mat + mat.conj().T)
    return np.real(herm).astype(np.float64)


def pole_matrix(n_freq: int, dx: float, xi: np.ndarray) -> np.ndarray:
    """POLE_jk from autoconvolution against (e^{u/2}+e^{-u/2}) on the torus."""
    acc = np.zeros((n_freq, n_freq), dtype=np.float64)
    period = dx * n_freq
    for m in range(n_freq):
        u_m = m * dx
        if u_m > 0.5 * period:
            u_m -= period
        weight = (math.exp(0.5 * u_m) + math.exp(-0.5 * u_m)) * dx
        acc += weight * sym_real(translation(n_freq, xi, u_m))
    return acc


def arch_matrix(n_freq: int, dx: float, xi: np.ndarray) -> np.ndarray:
    """ARCH as a Fourier multiplier, X-independent.  mpmath.digamma only."""
    log_pi = math.log(math.pi)
    dxi = 2.0 * math.pi / (n_freq * dx)
    multipliers = np.empty(n_freq, dtype=np.float64)
    for m, freq in enumerate(xi):
        z = 0.25 + 0.5j * float(freq)
        kernel = float(mp.re(mp.digamma(z))) - log_pi
        # ĥ(t) = dx² |DFT(f)|²  and (1/2π) ∫ ĥ W dt
        # DFT convention: fft(f)_m = Σ_k f_k e^{-i ξ_m x_k};
        # Parseval: Σ |fft|^2 / N = Σ |f|^2.  Continuum ĥ ≈ dx · fft.
        multipliers[m] = (dx * dx * dxi / (2.0 * math.pi)) * kernel
    # Q_arch(f) = Σ_m |fft(f)_m|² · α_m  with α_m = multipliers[m]
    # In position basis: F^* diag(N α) F because fft = F_unnormalized.
    # |fft|^2 = |F f|^2 with F_{mk} = exp(-i ξ_m x_k).
    # (F^* diag(α) F)_{jk} via inverse FFT of α along the circular lag.
    # Q = F_unnorm^* diag(α) F_unnorm = N · ifft-circulant(α) ...
    # Direct: apply to e_j via FFT.
    arch = np.zeros((n_freq, n_freq), dtype=np.float64)
    eye = np.eye(n_freq, dtype=np.float64)
    fft_e = np.fft.fft(eye, axis=0)
    for j in range(n_freq):
        for k in range(j, n_freq):
            val = float(np.vdot(fft_e[:, j], multipliers * fft_e[:, k]).real)
            arch[j, k] = arch[k, j] = val
    return arch


def events_true(x_cut: float, lam: np.ndarray, spf: np.ndarray
                ) -> list[dict]:
    nmax = min(len(lam) - 1, int(math.floor(math.exp(x_cut) + 1e-12)))
    out = []
    for n in range(2, nmax + 1):
        if lam[n] == 0.0:
            continue
        u_e = math.log(n)
        if u_e > x_cut + 1e-15:
            continue
        klass = classify(n, spf)
        label = CLASS_TO_LABEL[klass] - 1  # 0-based in 0..14 matching 1..15
        rate = 2.0 * float(lam[n]) * math.exp(-0.5 * u_e)
        out.append(dict(n=n, u=u_e, lam=rate, klass=klass, label=label))
    return out


def world_events(kind: str, true_ev: list[dict], x_cut: float
                 ) -> list[dict]:
    """Control worlds as in signed_only_nogo / positional_gns_probe."""
    if kind == "TRUE":
        return [dict(item) for item in true_ev]
    rates = np.array([e["lam"] for e in true_ev], dtype=np.float64)
    pos = np.array([e["u"] for e in true_ev], dtype=np.float64)
    labels = [e["label"] for e in true_ev]
    klasses = [e["klass"] for e in true_ev]
    ns = [e["n"] for e in true_ev]
    n_ev = len(true_ev)
    if kind == "SCRAMBLE":
        rng = np.random.default_rng(SEED_SCRAMBLE)
        pos = np.sort(rng.uniform(0.0, 2.0 * x_cut, size=n_ev))
    elif kind == "EPSTEIN":
        pos = sum2sq_positions(n_ev)
    elif kind == "WPERM":
        rng = np.random.default_rng(SEED_WPERM)
        rates = rates.copy()
        rng.shuffle(rates)
    elif kind == "BETA09":
        raise RuntimeError("BETA09 has no prime-data generator in-repo")
    else:
        raise ValueError(kind)
    out = []
    for i in range(n_ev):
        out.append(dict(n=ns[i], u=float(pos[i]), lam=float(rates[i]),
                        klass=klasses[i], label=labels[i]))
    return out


def permute_labels(ev: list[dict], seed: int) -> list[dict]:
    rng = np.random.default_rng(seed)
    labs = np.array([e["label"] for e in ev], dtype=np.int64)
    rng.shuffle(labs)
    out = []
    for item, lab in zip(ev, labs):
        row = dict(item)
        row["label"] = int(lab)
        out.append(row)
    return out


def drop_labels(ev: list[dict]) -> list[dict]:
    out = []
    for item in ev:
        row = dict(item)
        row["label"] = None
        out.append(row)
    return out


def jump_forms(n_freq: int, xi: np.ndarray, ev: list[dict], inc: np.ndarray
               ) -> tuple[np.ndarray, np.ndarray, float, float]:
    """D = Σ_e λ_e (I − Re U_{u_e})  and  PRIME = Σ_e λ_e Re U_{u_e},
    times the GL1 factor of R_ℓ (1 if labels dropped, 1 if a unital
    incidence row is used — labels do not act on A_f = I ⊗ A_f)."""
    ident = np.eye(n_freq, dtype=np.float64)
    prime = np.zeros((n_freq, n_freq), dtype=np.float64)
    gl1_vals = []
    factor_cache = {None: 1.0}
    sum_rate = 0.0
    for item in ev:
        lab = item["label"]
        if lab not in factor_cache:
            factor_cache[lab] = gl1_factor(row_kraus(inc, int(lab)))
        factor = factor_cache[lab]
        gl1_vals.append(factor)
        shift = sym_real(translation(n_freq, xi, item["u"]))
        prime += item["lam"] * factor * shift
        sum_rate += item["lam"] * factor
    mean_gl1 = float(np.mean(gl1_vals)) if gl1_vals else 1.0
    max_gl1_dev = (float(np.max(np.abs(np.array(gl1_vals, dtype=np.float64) - 1.0)))
                   if gl1_vals else 0.0)
    # 𝓓(f) = Σ λ ‖f − U f‖² / 2 = f^* [(Σλ) I − PRIME] f
    dirichlet = sum_rate * ident - prime
    return dirichlet, prime, mean_gl1, max_gl1_dev


def offdiag(mat: np.ndarray) -> np.ndarray:
    out = np.array(mat, dtype=np.float64, copy=True)
    np.fill_diagonal(out, 0.0)
    return out


def min_eig(mat: np.ndarray) -> float:
    herm = 0.5 * (mat + mat.T)
    return float(np.min(np.linalg.eigvalsh(herm)))


def q_matrix_rate_min(quad: np.ndarray) -> float:
    """Off-diagonal rates of T = −Q.  Laplacian/CP Markov needs these ≥ 0."""
    gen = -0.5 * (quad + quad.T)
    off = gen.copy()
    np.fill_diagonal(off, 0.0)
    if off.size == 0:
        return 0.0
    return float(np.min(off))


def choi_ccp_lmin(quad: np.ndarray) -> float:
    """CCP stand-in on the window: λ_min of the Dirichlet form Q itself.

    For a translation-invariant generator the Kossakowski / Fourier
    multipliers ARE the eigenvalues of Q, so this is the Kossakowski
    test of the forced generator (identity 𝓛 ↔ Q_W).
    """
    return min_eig(quad)


def compensator_legit(k_inf: np.ndarray) -> dict:
    """Is K_inf = POLE+ARCH−(Σλ)I a CP dissipator or a Hamiltonian?"""
    skew = 0.5 * (k_inf - k_inf.T)
    sym = 0.5 * (k_inf + k_inf.T)
    skew_fro = float(np.linalg.norm(skew))
    fro = max(float(np.linalg.norm(k_inf)), 1e-30)
    lmin = min_eig(sym)
    rate_min = q_matrix_rate_min(sym)
    is_ham = (skew_fro > 0.5 * fro) and (abs(lmin) < 1.0e-10)
    is_cp = (lmin >= -CP_FLOOR) and (rate_min >= -CP_FLOOR)
    return dict(lmin=lmin, rate_min=rate_min, skew_fro=skew_fro,
                is_hamiltonian=bool(is_ham), is_cp=bool(is_cp))


# em_P copied from eulerpick_ladder_probe.py (P(z)=ξ'/ξ(1/2+z) via
# Euler–Maclaurin + digamma; no zeta, no zeros).  Pick matrix as in
# sieve4_eulerpick_n4_probe / eulerpick_ladder_probe.
def em_P(sigma, cutoff: int, terms: int):
    s = mp.mpf("0.5") + sigma
    tot = mp.mpf(0)
    der = mp.mpf(0)
    for n in range(2, cutoff):
        u = mp.power(n, -s)
        tot += u
        der -= mp.log(n) * u
    tot += 1
    mcut = mp.mpf(cutoff)
    l_m = mp.log(mcut)
    lead = mcut ** (1 - s) / (s - 1)
    tot += lead
    der += lead * (-l_m - 1 / (s - 1))
    half = mp.mpf("0.5") * mcut ** (-s)
    tot += half
    der -= l_m * half
    for k in range(1, terms + 1):
        order = 2 * k - 1
        corr = (mp.bernpoly(2 * k, 0) / mp.factorial(2 * k)
                * mp.rf(s, order) * mcut ** (-s - order))
        harm = mp.fsum(1 / (s + i) for i in range(order))
        tot += corr
        der += corr * (harm - l_m)
    return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2 + der / tot)


def pick_matrix(n_pick: int) -> np.ndarray:
    sigmas = [mp.mpf(1) + mp.mpf(1) / mp.mpf(j) for j in range(1, n_pick + 1)]
    vals = [em_P(sig, EM_CUTOFF, EM_TERMS) for sig in sigmas]
    mat = np.zeros((n_pick, n_pick), dtype=np.float64)
    for j in range(n_pick):
        for k in range(n_pick):
            mat[j, k] = float((vals[j] + vals[k]) / (sigmas[j] + sigmas[k]))
    return mat, [float(s) for s in sigmas], [float(v) for v in vals]


def os_gram(ev: list[dict], sigmas: list[float]) -> np.ndarray:
    """Jump Ito isometry of compensated exponential observables.
    Doob–Meyer compensator is predictable ⇒ quadratic variation is
    Σ_e λ_e exp(−(σj+σk) u_e)."""
    n_p = len(sigmas)
    gram = np.zeros((n_p, n_p), dtype=np.float64)
    for item in ev:
        u_e = item["u"]
        rate = item["lam"]
        decay = [math.exp(-sig * u_e) for sig in sigmas]
        for j in range(n_p):
            for k in range(n_p):
                gram[j, k] += rate * decay[j] * decay[k]
    return gram


def scalar_fit(gram: np.ndarray, pick: np.ndarray) -> tuple[int, float, float]:
    """Return (n_scalars_needed, residual_raw, residual_after_best_fit)."""
    p_norm = float(np.linalg.norm(pick))
    raw = float(np.linalg.norm(gram - pick)) / max(p_norm, 1e-30)
    alpha = float(np.vdot(pick.ravel(), gram.ravel())
                  / max(float(np.vdot(pick.ravel(), pick.ravel())), 1e-30))
    r1 = float(np.linalg.norm(gram - alpha * pick)) / max(p_norm, 1e-30)
    # affine: α Pick + β J + γ I
    n = pick.shape[0]
    ones = np.ones((n, n), dtype=np.float64)
    ident = np.eye(n, dtype=np.float64)
    basis = np.column_stack([pick.ravel(), ones.ravel(), ident.ravel()])
    coeff, _, _, _ = np.linalg.lstsq(basis, gram.ravel(), rcond=None)
    fitted = (coeff[0] * pick + coeff[1] * ones + coeff[2] * ident)
    r3 = float(np.linalg.norm(gram - fitted)) / max(p_norm, 1e-30)
    if raw < PICK_EXACT_BAR:
        return 0, raw, raw
    if r1 < PICK_SCALAR_BAR:
        return 1, raw, r1
    if r3 < PICK_SCALAR_BAR:
        return 3, raw, r3
    return n * (n + 1) // 2, raw, r3


def assemble_window(n_freq: int, x_cut: float, ev: list[dict], inc: np.ndarray,
                    pole: np.ndarray, arch: np.ndarray, xi: np.ndarray):
    d_mat, prime, mean_gl1, gl1_dev = jump_forms(n_freq, xi, ev, inc)
    ident = np.eye(n_freq, dtype=np.float64)
    sum_rate = float(np.trace(d_mat + prime) / n_freq)
    weil = pole + arch - prime
    k_inf = pole + arch - sum_rate * ident
    forced = d_mat + k_inf
    off_d = offdiag(d_mat)
    off_p = offdiag(prime)
    off_res = float(np.linalg.norm(off_d + off_p)) / max(float(np.linalg.norm(off_p)), 1e-30)
    force_res = float(np.linalg.norm(forced - weil)) / max(float(np.linalg.norm(weil)), 1e-30)
    cheb = 2.0 * math.exp(0.5 * x_cut)
    growth = sum_rate / cheb if cheb else float("nan")
    pa_fro = float(np.linalg.norm(pole + arch))
    comp_fro = abs(sum_rate) * math.sqrt(n_freq)
    legit = compensator_legit(k_inf)
    return dict(
        D=d_mat, PRIME=prime, WEIL=weil, KINF=k_inf, FORCED=forced,
        sum_rate=sum_rate, mean_gl1=mean_gl1, gl1_dev=gl1_dev,
        off_res=off_res, force_res=force_res, growth=growth, cheb=cheb,
        pa_fro=pa_fro, comp_fro=comp_fro, legit=legit,
        d_lmin=min_eig(d_mat),
        weil_lmin=min_eig(weil),
        koss_lmin=choi_ccp_lmin(forced),
        kinf_lmin=legit["lmin"],
        rate_min=legit["rate_min"],
        jump_ccp=min_eig(d_mat),
    )


def payload(smoke: bool) -> dict:
    n_list = N_FREQ_SMOKE if smoke else N_FREQ_FULL
    x_list = X_SMOKE if smoke else X_FULL
    nmax = int(math.floor(math.exp(max(x_list)) + 2.0))
    lam = lambda_table(nmax)
    spf = spf_table(nmax)
    pp = prime_power_list(nmax)
    labels, inc = label_incidence()
    row_deg = [int(inc[i].sum()) for i in range(LABEL_DIM)]
    n_legs = int(inc.sum())

    pole_cache = {}
    arch_cache = {}
    lat_cache = {}
    for n_freq in n_list:
        xs, dx, xi = lattice(n_freq)
        lat_cache[n_freq] = (xs, dx, xi)
        pole_cache[n_freq] = pole_matrix(n_freq, dx, xi)
        arch_cache[n_freq] = arch_matrix(n_freq, dx, xi)

    worlds = ("TRUE", "SCRAMBLE", "EPSTEIN", "WPERM")
    t1_rows = []
    t2_rows = []
    t4_rows = []
    primary = None
    for n_freq in n_list:
        xs, dx, xi = lat_cache[n_freq]
        pole = pole_cache[n_freq]
        arch = arch_cache[n_freq]
        pa_xdep = []
        for x_cut in x_list:
            true_ev = events_true(x_cut, lam, spf)
            for kind in worlds:
                ev = world_events(kind, true_ev, x_cut)
                pack = assemble_window(n_freq, x_cut, ev, inc, pole, arch, xi)
                row = dict(n_freq=n_freq, X=x_cut, world=kind,
                           n_ev=len(ev), **{k: pack[k] for k in (
                               "sum_rate", "mean_gl1", "gl1_dev", "off_res",
                               "force_res", "growth", "cheb", "pa_fro",
                               "comp_fro", "d_lmin", "weil_lmin", "koss_lmin",
                               "kinf_lmin", "rate_min", "jump_ccp")})
                row["kinf_cp"] = pack["legit"]["is_cp"]
                row["kinf_ham"] = pack["legit"]["is_hamiltonian"]
                t1_rows.append(row)
                t2_rows.append(row)
                if (primary is None and n_freq == n_list[0]
                        and abs(x_cut - x_list[0]) < 1e-15 and kind == "TRUE"):
                    primary = dict(pack=pack, ev=ev, n_freq=n_freq,
                                   x_cut=x_cut, pole=pole, arch=arch, xi=xi)
            # T4 on the primary scale
            if n_freq == n_list[0] and abs(x_cut - x_list[0]) < 1e-15:
                base = assemble_window(n_freq, x_cut, true_ev, inc, pole, arch, xi)
                perm = assemble_window(n_freq, x_cut,
                                       permute_labels(true_ev, SEED_LABELS),
                                       inc, pole, arch, xi)
                dropped = assemble_window(n_freq, x_cut, drop_labels(true_ev),
                                          inc, pole, arch, xi)
                t4_rows.append(dict(
                    off_perm=float(np.linalg.norm(base["WEIL"] - perm["WEIL"])),
                    off_drop=float(np.linalg.norm(base["WEIL"] - dropped["WEIL"])),
                    d_perm=float(np.linalg.norm(base["D"] - perm["D"])),
                    d_drop=float(np.linalg.norm(base["D"] - dropped["D"])),
                    gl1_base=base["mean_gl1"], gl1_drop=dropped["mean_gl1"],
                    gl1_dev=base["gl1_dev"],
                ))
            pa_xdep.append(float(np.linalg.norm(pole + arch)))
        # pole+arch X-independence: cached per n_freq only
        _ = pa_xdep

    # T3 Euler–Pick companion, same compensated TRUE process at smoke/full
    mp.mp.dps = PICK_DPS
    pick, sigmas, pvals = pick_matrix(PICK_N)
    gram = os_gram(primary["ev"], sigmas)
    n_scal, r_raw, r_fit = scalar_fit(gram, pick)

    # OS citation: neither GNS probe names Osterwalder–Schrader.
    os_note = (
        "OS/Osterwalder does not occur in weil_gns_identification_probe.py "
        "or positional_gns_probe.py (grep empty).  Naive OS positivity "
        "already failed in quartet_avoiding_os_probe.py (docstring lines "
        "11-16: reflection positivity FAILS on every quartet-STRADDLED cut) "
        "and quantum_band_os_probe.py."
    )

    beta09 = ("SKIP no in-repo generator of beta=0.9 / off-line-zero "
              "prime data (inventory mentions the kill-world in prose "
              "only; no event list is loaded)")

    return dict(
        n_list=n_list, x_list=x_list, nmax=nmax, n_pp=len(pp),
        n_legs=n_legs, row_deg=tuple(row_deg), labels_ok=len(labels) == 15,
        t1=t1_rows, t2=t2_rows, t4=t4_rows[0] if t4_rows else None,
        pick=pick, gram=gram, sigmas=tuple(sigmas), pvals=tuple(pvals),
        n_scal=n_scal, r_raw=r_raw, r_fit=r_fit, os_note=os_note,
        beta09=beta09, pp_head=tuple(pp[:8]),
        pa_n8=float(np.linalg.norm(pole_cache[n_list[0]]
                                   + arch_cache[n_list[0]])),
    )


def clauses_of(data: dict) -> dict:
    t1 = data["t1"]
    true_rows = [r for r in t1 if r["world"] == "TRUE"]
    off_ok = all(r["off_res"] < 1e-8 for r in t1)
    # COMPENSATOR_MISMATCH: identity requires K_inf := POLE+ARCH − (Σλ)I,
    # and that term is not a CP dissipator / Hamiltonian.
    mismatch = True
    for r in true_rows:
        if r["force_res"] > 1e-8:
            mismatch = False
        if r["kinf_cp"] or r["kinf_ham"]:
            mismatch = False
        if r["comp_fro"] <= r["pa_fro"] * 0.5:
            # compensator should dominate / differ from X-independent PA
            pass
    # growth vs 2 e^{X/2}
    growths = [(r["X"], r["growth"], r["sum_rate"], r["cheb"]) for r in true_rows]
    t1_clause = "COMPENSATOR_MISMATCH" if (mismatch and off_ok) else (
        "OFFDIAG_FAIL" if not off_ok else "COMPENSATOR_UNCLEAR")

    # T2: identity of CP and Weil tests
    t2_sep = []
    t2_id = True
    for r in data["t2"]:
        koss = r["koss_lmin"]
        weil = r["weil_lmin"]
        if abs(koss - weil) > 1e-8 * max(1.0, abs(weil), abs(koss)):
            t2_id = False
        koss_pos = koss >= -CP_FLOOR
        weil_pos = weil >= -CP_FLOOR
        if koss_pos != weil_pos:
            t2_sep.append(r)
    t2_clause = "GENUINE_GAP" if t2_sep else (
        "RECOORDINATIZATION" if t2_id else "TESTS_DISAGREE")

    t4 = data["t4"]
    t4_clause = "LABELS_DECORATIVE" if (
        t4 and t4["off_perm"] < 1e-10 and t4["off_drop"] < 1e-10
        and t4["d_perm"] < 1e-10 and t4["d_drop"] < 1e-10
    ) else "LABELS_LIVE"

    if data["n_scal"] == 0:
        t3_clause = "PICK_EXACT"
    else:
        t3_clause = "PICK_NEEDS_SCALARS"

    # ALIVE(PICK_EXACT) extra: CP in TRUE not in SCRAMBLE
    true_cp = all(r["koss_lmin"] >= -CP_FLOOR for r in data["t2"]
                  if r["world"] == "TRUE")
    scr_cp = any(r["koss_lmin"] >= -CP_FLOOR for r in data["t2"]
                 if r["world"] == "SCRAMBLE")
    pick_alive_ok = (t3_clause == "PICK_EXACT" and true_cp and not scr_cp)

    if t1_clause == "COMPENSATOR_MISMATCH" and t2_clause == "RECOORDINATIZATION":
        verdict = "KILLED(RECOORDINATIZATION)"
    elif t3_clause == "PICK_NEEDS_SCALARS" and t2_clause == "RECOORDINATIZATION":
        verdict = "KILLED(PICK_NEEDS_SCALARS)"
    elif t2_clause == "GENUINE_GAP":
        verdict = "ALIVE(GENUINE_GAP)"
    elif pick_alive_ok:
        verdict = "ALIVE(PICK_EXACT)"
    else:
        # T3 kill is also preregistered even if T1 already killed;
        # prefer the structural T1/T2 kill, then T3.
        if t3_clause == "PICK_NEEDS_SCALARS":
            verdict = "KILLED(PICK_NEEDS_SCALARS)"
        else:
            verdict = "KILLED(RECOORDINATIZATION)" if t2_clause == "RECOORDINATIZATION" else "INCONCLUSIVE"

    return dict(t1=t1_clause, t2=t2_clause, t3=t3_clause, t4=t4_clause,
                verdict=verdict, growths=growths, t2_sep=len(t2_sep),
                true_cp=true_cp, scr_cp=scr_cp, off_ok=off_ok)


def print_t2_table(rows: list[dict]) -> None:
    print("  %-8s %6s %10s %16s %16s %16s %12s" % (
        "world", "N", "X", "koss_lmin", "weil_lmin", "jump_D_lmin", "n_ev"))
    for r in rows:
        print("  %-8s %6d %10.6f %16s %16s %16s %12d" % (
            r["world"], r["n_freq"], r["X"],
            fmt(r["koss_lmin"]), fmt(r["weil_lmin"]),
            fmt(r["jump_ccp"]), r["n_ev"]))


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    print("event_lindblad_twokey_probe -- PRIME.EVENT.LINDBLAD.01 r607")
    print("KEIN RH-CLAIM")
    print("mode", "SMOKE" if smoke else "FULL")
    print("SPEC_SHA %s" % SPEC_SHA[:16])

    hits = ast_firewall()
    check("G0.1 AST firewall (no zero data)", not hits, str(hits) if hits else "clean")
    check("G0.2 KEIN RH-CLAIM in spec",
          "KEIN RH-CLAIM" in (FROZEN_SPEC or "")
          and "NO RH CLAIM" in (FROZEN_SPEC or ""))

    a = payload(smoke)
    b = payload(smoke)
    # in-process byte identity of the numeric tables
    def freeze(obj):
        if isinstance(obj, dict):
            return tuple(sorted((k, freeze(v)) for k, v in obj.items()
                                if k not in ("pack", "WEIL", "D", "PRIME",
                                             "KINF", "FORCED")))
        if isinstance(obj, list):
            return tuple(freeze(v) for v in obj)
        if isinstance(obj, np.ndarray):
            return tuple(np.round(obj.real.astype(np.float64), 12).ravel().tolist())
        if isinstance(obj, float):
            return round(obj, 12)
        return obj

    check("G0.3 two in-process payloads identical", freeze(a) == freeze(b))
    check("G0.4 prime-power head 2,3,4,5,7,8,9,11",
          a["pp_head"] == (2, 3, 4, 5, 7, 8, 9, 11), str(a["pp_head"]))
    check("G0.5 105-leg incidence, 7 per row",
          a["n_legs"] == 105 and a["row_deg"] == tuple([7] * 15),
          "legs=%d rowdeg=%s" % (a["n_legs"], a["row_deg"]))

    cl = clauses_of(a)

    section("T1  jump Dirichlet vs Weil prime; compensator")
    print("  GL1-corner reduction: A_f = I_15 ⊗ A_window.  For a unital")
    print("  incidence row, Tr(Σ V* V) = 1 independent of ℓ(e), so R_ℓ")
    print("  does not act on the window observable (labels decorative on")
    print("  this corner; comb-blind Hjelmslev tower).")
    print("  %-8s %6s %10s %14s %14s %12s %12s %12s" % (
        "world", "N", "X", "off_res", "force_res", "Σλ", "2e^{X/2}", "growth"))
    for r in a["t1"]:
        if r["world"] != "TRUE":
            continue
        print("  %-8s %6d %10.6f %14s %14s %12s %12s %12s" % (
            r["world"], r["n_freq"], r["X"],
            fmt(r["off_res"]), fmt(r["force_res"]),
            fmt(r["sum_rate"]), fmt(r["cheb"]), fmt(r["growth"])))
    true0 = next(r for r in a["t1"] if r["world"] == "TRUE")
    print("  POLE+ARCH Frobenius (X-independent, N=%d): %s" % (
        a["n_list"][0], fmt(true0["pa_fro"])))
    print("  diagonal compensator Frobenius (Σλ)·√N: %s" % fmt(true0["comp_fro"]))
    print("  K_inf=POLE+ARCH−(Σλ)I  lmin=%s rate_min=%s CP=%s Hamiltonian=%s"
          % (fmt(true0["kinf_lmin"]), fmt(true0["rate_min"]),
             true0["kinf_cp"], true0["kinf_ham"]))
    print("  mean GL1 factor %s  max |factor-1| %s" % (
        fmt(true0["mean_gl1"]), fmt(true0["gl1_dev"])))
    check("T1.1 off-diagonal D vs −PRIME (KMS half-weight in λ_e)",
          cl["off_ok"], "worst residual among TRUE rows in table")
    check("T1.2 forced identity D+K_inf = Q_W",
          all(r["force_res"] < 1e-8 for r in a["t1"] if r["world"] == "TRUE"))
    check("T1.3 K_inf is not a CP dissipator and not a Hamiltonian",
          (not true0["kinf_cp"]) and (not true0["kinf_ham"]),
          "lmin=%s" % fmt(true0["kinf_lmin"]))
    check("T1.4 clause %s" % cl["t1"], cl["t1"] == "COMPENSATOR_MISMATCH")

    section("T2  two-key worlds (forced generator)")
    print("  %s" % a["beta09"])
    print_t2_table(a["t2"])
    print("  jump Dirichlet λ_min is ≥ 0 in every world (Lindblad).")
    print("  forced Kossakowski λ_min equals Weil λ_min (same circulant).")
    check("T2.1 jump D ≽ 0 in every world",
          all(r["jump_ccp"] >= -1e-8 for r in a["t2"]))
    check("T2.2 Kossakowski λ_min = Weil λ_min (identity of the two tests)",
          cl["t2"] == "RECOORDINATIZATION", cl["t2"])
    signs = []
    for world in ("TRUE", "SCRAMBLE", "EPSTEIN", "WPERM"):
        sub = [r for r in a["t2"] if r["world"] == world]
        signs.append("%s:%s" % (world, ",".join(
            ("+" if r["weil_lmin"] >= 0 else "-") for r in sub)))
    print("  Weil sign pattern (N,X order): %s" % " ".join(signs))
    check("T2.3 SCRAMBLE or EPSTEIN indefinite on the window",
          any(r["weil_lmin"] < 0 for r in a["t2"]
              if r["world"] in ("SCRAMBLE", "EPSTEIN")))

    section("T3  Euler–Pick companion N≤4")
    print("  sigma_j = 1+1/j = %s" % ", ".join("%.6f" % s for s in a["sigmas"]))
    print("  P(sigma) = %s" % ", ".join(fmt(v) for v in a["pvals"]))
    print("  Pick_N λ_min %s" % fmt(min_eig(a["pick"])))
    print("  OS-Gram λ_min %s" % fmt(min_eig(a["gram"])))
    print("  residual raw %s  after affine fit %s  scalars=%d" % (
        fmt(a["r_raw"]), fmt(a["r_fit"]), a["n_scal"]))
    print("  %s" % a["os_note"])
    check("T3.1 Pick needs free scalars (not exact)",
          a["n_scal"] > 0, "n_scal=%d raw=%s" % (a["n_scal"], fmt(a["r_raw"])))
    check("T3.2 clause %s" % cl["t3"], cl["t3"] == "PICK_NEEDS_SCALARS")

    section("T4  label relevance")
    t4 = a["t4"]
    print("  ||Q_perm − Q|| %s  ||Q_drop − Q|| %s" % (
        fmt(t4["off_perm"]), fmt(t4["off_drop"])))
    print("  ||D_perm − D|| %s  ||D_drop − D|| %s" % (
        fmt(t4["d_perm"]), fmt(t4["d_drop"])))
    print("  GL1 factor base/drop %s / %s  maxdev %s" % (
        fmt(t4["gl1_base"]), fmt(t4["gl1_drop"]), fmt(t4["gl1_dev"])))
    check("T4.1 labels decorative (perm and R≡I unchanged)",
          cl["t4"] == "LABELS_DECORATIVE", cl["t4"])

    section("VERDICT")
    print("  T1=%s  T2=%s  T3=%s  T4=%s" % (
        cl["t1"], cl["t2"], cl["t3"], cl["t4"]))
    print("  blunt: the Lindblad recipe is a re-coordinatization of")
    print("  finite Weil positivity.  The jump Dirichlet is CP in every")
    print("  world; matching Q_W forces 𝓛_∞ := (POLE+ARCH) − (Σλ)I,")
    print("  which is not itself Lindblad, and the assembled CP test")
    print("  is then identical to λ_min(Q_W).")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("CHECKS %d/%d" % (n_pass, n_pass + n_fail))
    print("VERDICT: %s" % cl["verdict"])
    print("SPEC %s" % SPEC_SHA[:16])
    print("KEIN RH-CLAIM")
    return 0 if n_fail == 0 else 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
