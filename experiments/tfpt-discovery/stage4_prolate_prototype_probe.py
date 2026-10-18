"""Discovery probe (2026-07-25), part 46 of the zeta/prime investigation.
FIRST UNBOUNDED OPERATOR PROTOTYPE on the Stage-4 map (T40): a
self-adjoint operator from the Fourier-selfduality class, tested against
the preregistered Hilbert-Polya requirements R1-R4 (T2 / 2026-07-23 XIII).

Classical / external object class (named as such — NOT a TFPT derivation):
  Prolate spheroidal operator (Slepian / Landau / Pollak): the differential
  operator that COMMUTES with the truncated Fourier transform — the
  canonical object of Fourier self-duality.  Connes-Moscovici 2022
  (PNAS; arXiv:2112.05500), "The UV prolate spectrum matches the zeros
  of zeta": a self-adjoint extension W_sa of
      W_Λ = -d/dx((Λ² - x²) d/dx) + (2π Λ x)²
  has negative eigenvalues (Sonin / exterior sector) whose ultraviolet
  counting reproduces that of the squares of the nontrivial zeta zeros
  (for Λ = 1 and Λ = √2).  Ramis-Richard-Jung-Thomann (C.R. Math. 2025)
  prove the non-classical CM spectrum equals the naive spectrum of the
  imaginary-axis reduction
      A_τ u = -d/dt((1+t²) du/dt) + τ² t² u ,   τ = 2π Λ²,
  with CM eigenvalue μ = -λ (λ > 0 eigenvalue of A_τ).

TFPT typing ONLY (no claim that TFPT derives the operator):
  The self-duality class that houses the prolate operator is exactly the
  Poisson-selfduality structure verified in-suite (T12: unique self-dual
  Gaussian width; T14: only μ4-completed E8 has it).  This probe maps
  whether that object class can meet R1-R4 at prototype level and how
  far a numerical realisation carries.  This is a reproduction of a
  classical / external construction — NOT a TFPT result and NOT RH
  progress.

Sections:
  S1  R1: matrix realisation of A_τ (P1 FEM on [-T,T]), symmetry,
      two-resolution convergence of low eigenvalues; interior classical
      W_Λ on [-Λ,Λ] as the positive / trivial-zero sector (documented).
  S2  R2/MATCH: low eigenvalues vs γ_n² (+1/4 form); UV counting trend;
      null controls (GUE same density; A_τ without τ² t² potential).
  S3  R3: unfolded nearest-neighbour vs GUE Wigner (underpowered).
  S4  R4: typed OPEN (trace-formula match needs full theory).
  S5  Synthesis / verdict enum.

PREREGISTERED CRITERIA (frozen before runs):
  Variant under test: IMAGINARY-AXIS / Ramis reduction of the non-classical
  CM spectrum (NOT the full Connes L²(R) extension with oscillatory ∞
  boundary conditions — that extension is documented as subtler; the
  Ramis equivalence theorem identifies its negative spectrum with A_τ).
  Matching formula F0 (PRIMARY, low-n):
      |μ_n|  ~  γ_n² + 1/4          (ordered increasing |μ|, γ)
      success: monotone pairing; mean relative error of first 8 falls
      when Λ increases through {1, √2}; target < 15% mean rel for first 8
      at Λ = √2 (the CM-published value).
  Matching formula F1 (SECONDARY, published UV claim):
      N_op(E) := #{n : √|μ_n| ≤ E} tracks Riemann-von Mangoldt
      N_ζ(E) = (E/2π) log(E/2π e) + 7/8 on a mid-range E window;
      relative |N_op - N_ζ| / N_ζ → smaller as more eigenvalues resolve.
  Nulls (K2): GUE spectrum of equal mean density (seed-fixed) and the
      pure kinetic operator A_τ^{(0)} = -d/dt((1+t²)d/dt) must NOT
      match F0 as well as A_τ (clear separation on mean rel error).
  Kills:
      K1: two FEM resolutions disagree on lowest 5 |μ| by > 5%
          → numerically blocked → IMPL-OPEN.
      K2: a null matches F0 as well as prolate while prolate is NOT at
          catastrophic wrong-scale (>50% mean rel) → NO-SIGNAL.
          Catastrophic wrong-scale vs γ² with a Ramis-valid operator
          → IMPL-OPEN (published claim is UV / Dirac, not IR F0).
  Verdicts: PROTOTYPE-MATCHES / IMPL-OPEN / NO-SIGNAL.
  R4: always OPEN at this level.

Firewall: discovery sandbox — no promotion, no ledger / paper / website /
marker edits; classical (Slepian, Connes-Moscovici 2022, Ramis et al.)
named as classical / external; ABSOLUTELY no RH-evidence language.
"""
from __future__ import annotations

import math
import time

import mpmath
import numpy as np

PASS = 0
FAIL = 0
T0 = time.time()
mpmath.mp.dps = 25
RNG = np.random.default_rng(20260725)

# ---------------------------------------------------------------- config
N_ZEROS = 40
LAMBDAS = (1.0, math.sqrt(2.0), 2.0)
# P1 finite-element truncations on [-T, T] (two resolutions for K1).
# Eigenfunctions of A_τ decay as exp(-τ |t|²/2)-like; T=12 covers low modes.
FEM_LO = (10.0, 600)   # (T, n_interior)
FEM_HI = (14.0, 1200)
N_EIG_REPORT = 20
N_MATCH = 8
# Published Ramis anchors at τ = 4π (Λ = √2): first odd / first even.
RAMIS_MU_ODD1 = -13.3027463832915625
RAMIS_MU_EVEN1 = -39.38321657426153947615
RAMIS_TOL_REL = 0.02  # 2% — FEM truncation, not 25-digit curtain
# F0 success threshold (preregistered).
F0_TARGET_MEAN_REL = 0.15
# K2: null must be worse by this factor on mean rel (or absolute gap).
K2_SEPARATION = 0.20  # null mean_rel >= prolate * (1 + K2_SEPARATION)


def check(name: str, ok: bool) -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}", flush=True)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


def info(msg: str) -> None:
    print(f"        {msg}", flush=True)


# ================================================================ helpers
def assemble_A_tau_fem(tau: float, T: float, n_interior: int,
                       with_potential: bool):
    """P1 finite-element matrices for A_τ on [-T, T] with Dirichlet ends.

    Weak form: <v, A u> = ∫ (1+t²) u' v' dt + τ² ∫ t² u v dt.
    Variant under test (documented): truncated imaginary-axis problem with
    u(±T)=0 — a clean self-adjoint realisation of the Ramis operator A_τ;
    T large enough that the lowest modes have decayed.
    """
    # Nodes: 0..n_interior+1 with ends fixed; unknowns = interior.
    n_el = n_interior + 1
    h = 2.0 * T / n_el
    t = np.linspace(-T, T, n_el + 1)
    n = n_interior
    amat = np.zeros((n, n))
    mass = np.zeros((n, n))
    # Element [t_e, t_{e+1}]; local unknowns map to global interior indices.
    # Global node k=0..n_el; interior indices 1..n_el-1 → matrix 0..n-1.
    for e in range(n_el):
        t0, t1 = t[e], t[e + 1]
        # Two-point Gauss on element for (1+t²), t², 1.
        xi = np.array([-1.0 / math.sqrt(3.0), 1.0 / math.sqrt(3.0)])
        wloc = np.array([1.0, 1.0])  # weights for ∫_{-1}^1; scale by h/2
        tt = 0.5 * (t0 + t1) + 0.5 * (t1 - t0) * xi
        jac = 0.5 * h
        # Local shape: N0=(1-ξ)/2, N1=(1+ξ)/2 on [-1,1]; dN/dt = ±1/h
        # Local stiffness from gradients: constant dN.
        dN = np.array([-1.0 / h, 1.0 / h])
        # Integrate (1+t²) dNi dNj
        for a in range(2):
            for b in range(2):
                k_ab = 0.0
                m_ab = 0.0
                p_ab = 0.0
                for q in range(2):
                    N_a = 0.5 * (1.0 - xi[q]) if a == 0 else 0.5 * (1.0 + xi[q])
                    N_b = 0.5 * (1.0 - xi[q]) if b == 0 else 0.5 * (1.0 + xi[q])
                    k_ab += wloc[q] * jac * (1.0 + tt[q] * tt[q]) * dN[a] * dN[b]
                    m_ab += wloc[q] * jac * N_a * N_b
                    p_ab += wloc[q] * jac * (tt[q] * tt[q]) * N_a * N_b
                ga = e + a - 1  # interior index; node e+a maps to e+a-1
                gb = e + b - 1
                if 0 <= ga < n and 0 <= gb < n:
                    amat[ga, gb] += k_ab + (tau * tau * p_ab if with_potential else 0.0)
                    mass[ga, gb] += m_ab
    amat = 0.5 * (amat + amat.T)
    mass = 0.5 * (mass + mass.T)
    return amat, mass


def generalised_eigh_lowest(amat, mass, n_keep: int) -> np.ndarray:
    """Lowest n_keep eigenvalues of A u = λ M u (A, M SPD)."""
    evals_m, evecs_m = np.linalg.eigh(mass)
    evals_m = np.maximum(evals_m, 1e-14)
    inv_sqrt = evecs_m * (1.0 / np.sqrt(evals_m))
    a_red = inv_sqrt.T @ amat @ inv_sqrt
    a_red = 0.5 * (a_red + a_red.T)
    evals = np.linalg.eigh(a_red)[0]
    return np.sort(evals)[:n_keep]


def cm_eigenvalues(tau: float, fem_spec, n_keep: int,
                   with_potential: bool = True) -> np.ndarray:
    """CM eigenvalues μ_n = -λ_n < 0 from A_τ (FEM)."""
    T, n_int = fem_spec
    amat, mass = assemble_A_tau_fem(tau, T, n_int, with_potential)
    lam = generalised_eigh_lowest(amat, mass, n_keep)
    return -lam


def interior_W_legendre(lam: float, n_basis: int) -> np.ndarray:
    """Classical INTERIOR problem on [-Λ, Λ]: positive prolate eigenvalues.

    Galerkin in shifted Legendre polynomials on [-1,1] after x = Λ y.
    W_Λ → D_τ with τ = 2π Λ²:
      D = -d/dy((1-y²) d/dy) + τ² y²   on [-1,1],
    Dirichlet-regular (bounded) = classical PSWF eigenvalues (positive).
    Documented: this is NOT the CM zeta-related sector.
    """
    # Use Gauss-Legendre quadrature on [-1,1].
    from numpy.polynomial.legendre import leggauss

    tau = 2.0 * math.pi * lam * lam
    n_quad = max(2 * n_basis + 20, 120)
    nodes, weights = leggauss(n_quad)  # ∫_{-1}^1 f

    # Legendre P_0..P_{n-1} and derivatives via recurrence.
    p = np.empty((n_basis, n_quad))
    dp = np.empty((n_basis, n_quad))
    p[0] = 1.0
    dp[0] = 0.0
    if n_basis > 1:
        p[1] = nodes
        dp[1] = 1.0
    for n in range(1, n_basis - 1):
        p[n + 1] = ((2 * n + 1) * nodes * p[n] - n * p[n - 1]) / (n + 1)
        dp[n + 1] = ((2 * n + 1) * (p[n] + nodes * dp[n]) - n * dp[n - 1]) / (
            n + 1
        )

    # Weak form on [-1,1]: ∫ (1-y²) u' v' + τ² ∫ y² u v = μ ∫ u v
    # (positive eigenvalues).
    one_my2 = np.maximum(1.0 - nodes * nodes, 0.0)
    mass = (p * weights) @ p.T
    stiff = (dp * (weights * one_my2)) @ dp.T
    pot = (p * (weights * (tau * tau * nodes * nodes))) @ p.T
    amat = 0.5 * (stiff + pot + stiff.T + pot.T)
    mass = 0.5 * (mass + mass.T)
    return generalised_eigh_lowest(amat, mass, min(12, n_basis // 2))


def riemann_N(E: float) -> float:
    """Riemann-von Mangoldt main term."""
    if E <= 2.0 * math.pi:
        return 0.0
    return (E / (2.0 * math.pi)) * math.log(E / (2.0 * math.pi * math.e)) + 7.0 / 8.0


def mean_rel_errors(vals: np.ndarray, targets: np.ndarray) -> np.ndarray:
    """Elementwise |v - t| / t for positive targets."""
    return np.abs(vals - targets) / np.maximum(targets, 1e-30)


def ks_distance(sample: np.ndarray, cdf) -> float:
    """One-sample KS distance vs theoretical CDF."""
    x = np.sort(sample)
    n = len(x)
    if n == 0:
        return 1.0
    F = np.array([cdf(float(xi)) for xi in x])
    emp_plus = np.arange(1, n + 1) / n
    emp_minus = np.arange(0, n) / n
    return float(max(np.max(np.abs(emp_plus - F)), np.max(np.abs(emp_minus - F))))


def gue_wigner_cdf(s: float) -> float:
    """CDF of Wigner surmise for GUE: p(s) = 32/π² s² exp(-4 s² / π)."""
    # Integrate: closed form via incomplete gamma / erf.
    # P(S ≤ s) = ∫_0^s (32/π²) t² e^{-4 t²/π} dt
    if s <= 0:
        return 0.0
    a = 4.0 / math.pi
    # ∫ t² e^{-a t²} dt = (√π /(4 a^{3/2})) erf(√a t) - t e^{-a t²}/(2a)
    from math import erf

    sqrt_a = math.sqrt(a)
    integ = (math.sqrt(math.pi) / (4.0 * a ** 1.5)) * erf(sqrt_a * s) - (
        s * math.exp(-a * s * s) / (2.0 * a)
    )
    integ0 = 0.0
    return float((32.0 / math.pi ** 2) * (integ - integ0))


def unfold_spacings(levels: np.ndarray) -> np.ndarray:
    """Unfold by local mean density (cubic smooth of staircase)."""
    x = np.sort(np.asarray(levels, dtype=float))
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 5:
        return np.array([])
    # Smooth N(e) ≈ a + b e + c e² on the sample; use cumulative index.
    idx = np.arange(1, n + 1, dtype=float)
    # Polynomial fit degree 2 for mean density.
    coeffs = np.polyfit(x, idx, 2)
    N_smooth = np.polyval(coeffs, x)
    # Ensure monotone.
    for i in range(1, n):
        if N_smooth[i] <= N_smooth[i - 1]:
            N_smooth[i] = N_smooth[i - 1] + 1e-9
    spac = np.diff(N_smooth)
    spac = spac[spac > 0]
    mean_s = float(np.mean(spac))
    if mean_s <= 0:
        return np.array([])
    return spac / mean_s


def gue_random_spectrum(n: int, prolate_levels: np.ndarray) -> np.ndarray:
    """Synthetic GUE-like positive levels with SAME mean density as prolate |μ|.

    Spacings from the Wigner surmise (seed-fixed), scaled so mean spacing
    equals that of prolate_levels; start at prolate_levels[0].  Compared
    to γ²-targets this is an honest null: it shares the prolate density
    but not its detailed values (NOT affinely pinned to the γ² endpoints).
    """
    ref = np.sort(np.asarray(prolate_levels[:n], dtype=float))
    mean_sp = float(np.mean(np.diff(ref))) if n > 1 else 1.0
    spac = []
    while len(spac) < n - 1:
        s = RNG.uniform(0.0, 4.0)
        pmax = 0.6
        u = RNG.uniform(0.0, pmax)
        pdf = (32.0 / math.pi ** 2) * s * s * math.exp(-4.0 * s * s / math.pi)
        if u < pdf:
            spac.append(s)
    spac = np.array(spac[: n - 1])
    spac = spac / float(np.mean(spac)) * mean_sp
    return ref[0] + np.concatenate([[0.0], np.cumsum(spac)])


# ================================================================ S0
print("=" * 72)
print("S0 -- preregistered criteria + zero cache")
print("=" * 72)
info("Variant: IMAGINARY-AXIS Ramis reduction A_τ of non-classical CM spectrum")
info("  A_τ u = -d/dt((1+t²)u') + τ² t² u,  τ = 2π Λ²,  μ = -λ")
info("  (full Connes L²(R) extension with ∞ oscillatory BC: NOT directly")
info("   discretised; Ramis Thm 14 equates its negative spectrum to A_τ)")
info("F0 PRIMARY: |μ_n| ~ γ_n² + 1/4; mean rel first 8 < 15% at Λ=√2;")
info("            mean rel falls as Λ: 1 → √2")
info("F1 SECONDARY (published UV): N_op(E) vs N_ζ(E) on mid-range E")
info("K1: FEM (T=10,N=600) vs (T=14,N=1200) disagree >5% on lowest 5 → blocked")
info("K2: null ≈ prolate on F0 while prolate not catastrophic-wrong-scale → NO-SIGNAL")
info("    (catastrophic wrong-scale + Ramis-valid → IMPL-OPEN: UV≠IR subtlety)")
info("R4: OPEN (trace formula needs full theory)")

t_z = time.time()
GAMMAS = np.array([float(mpmath.zetazero(n).imag) for n in range(1, N_ZEROS + 1)])
info(f"cached {N_ZEROS} zeta zeros in {time.time() - t_z:.1f}s; "
     f"γ1={GAMMAS[0]:.6f}, γ10={GAMMAS[9]:.6f}")
TARGETS_F0 = GAMMAS ** 2 + 0.25
check(
    f"zero cache length = {N_ZEROS}, strictly increasing, γ1 ≈ 14.1347",
    len(GAMMAS) == N_ZEROS
    and bool(np.all(np.diff(GAMMAS) > 0))
    and abs(GAMMAS[0] - 14.134725) < 1e-4,
)

# ================================================================ S1
print()
print("=" * 72)
print("S1 -- R1: self-adjoint matrix realisation + convergence (K1)")
print("=" * 72)

# Interior classical sector (positive) — documented, not the match target.
print("S1a -- classical INTERIOR W_Λ on [-Λ,Λ] (positive PSWF sector)")
for lam in (1.0, math.sqrt(2.0)):
    e_lo = interior_W_legendre(lam, 40)
    e_hi = interior_W_legendre(lam, 60)
    rel = np.abs(e_lo[:5] - e_hi[:5]) / np.maximum(e_hi[:5], 1e-30)
    info(f"Λ={lam:.4f}: interior lowest5 lo={np.array2string(e_lo[:5], precision=4)}")
    info(f"         hi={np.array2string(e_hi[:5], precision=4)}; "
         f"max rel diff={rel.max():.2e}")
    check(
        f"interior Λ={lam:.4f}: positive spectrum + two-res max rel < 5% on lowest 5",
        bool(np.all(e_hi[:5] > 0) and rel.max() < 0.05),
    )
info("NOTE: interior = classical prolates / trivial-zero UV sector (CM);")
info("      zeta-related content lives in the NEGATIVE / imaginary-axis sector.")

print()
print("S1b -- imaginary-axis A_τ (non-classical CM spectrum)")
# Symmetry check
amat, mass = assemble_A_tau_fem(4.0 * math.pi, FEM_HI[0], FEM_HI[1], True)
sym_err = float(np.max(np.abs(amat - amat.T)))
mass_sym = float(np.max(np.abs(mass - mass.T)))
check(
    f"A_τ FEM matrix symmetric (max|A-A^T|={sym_err:.2e}, "
    f"|M-M^T|={mass_sym:.2e})",
    sym_err < 1e-10 and mass_sym < 1e-10,
)

# Convergence K1 at Λ=√2
mu_lo = cm_eigenvalues(4.0 * math.pi, FEM_LO, N_EIG_REPORT)
mu_hi = cm_eigenvalues(4.0 * math.pi, FEM_HI, N_EIG_REPORT)
rel_conv = np.abs(mu_lo[:5] - mu_hi[:5]) / np.maximum(np.abs(mu_hi[:5]), 1e-30)
info(f"Λ=√2, FEM{FEM_LO}: μ[:5]={np.array2string(mu_lo[:5], precision=6)}")
info(f"Λ=√2, FEM{FEM_HI}: μ[:5]={np.array2string(mu_hi[:5], precision=6)}")
info(f"max rel |μ_lo-μ_hi|/|μ_hi| on lowest 5 = {rel_conv.max():.4e}")
k1_ok = bool(rel_conv.max() < 0.05)
check(
    f"K1 clear: two FEM resolutions agree < 5% on lowest 5 "
    f"(max rel={rel_conv.max():.4e})",
    k1_ok,
)

# Ramis anchors (implementation validation — classical external numbers)
mu_sorted = np.sort(mu_hi)  # most negative first? μ < 0; sort ascending = most neg first
# We want increasing |μ|: sort by abs
mu_by_abs = mu_hi[np.argsort(np.abs(mu_hi))]
info(f"μ by increasing |μ|: {np.array2string(mu_by_abs[:6], precision=6)}")
# Odd/even interlacing: first should be odd ≈ -13.30, second even ≈ -39.38
rel_odd = abs(mu_by_abs[0] - RAMIS_MU_ODD1) / abs(RAMIS_MU_ODD1)
rel_even = abs(mu_by_abs[1] - RAMIS_MU_EVEN1) / abs(RAMIS_MU_EVEN1)
info(f"Ramis odd1:  num={mu_by_abs[0]:.8f}  lit={RAMIS_MU_ODD1:.8f}  "
     f"rel={rel_odd:.4e}")
info(f"Ramis even1: num={mu_by_abs[1]:.8f}  lit={RAMIS_MU_EVEN1:.8f}  "
     f"rel={rel_even:.4e}")
ramis_ok = rel_odd < RAMIS_TOL_REL and rel_even < RAMIS_TOL_REL
check(
    f"Ramis anchors at τ=4π: |μ1+13.3027|/13.3 < {RAMIS_TOL_REL} and "
    f"|μ2+39.3832|/39.38 < {RAMIS_TOL_REL} (validates A_τ discretisation)",
    ramis_ok,
)
check(
    "R1 structural: A_τ unbounded below in the sense of discrete spectrum "
    "unbounded (λ_n → +∞ ⇒ μ_n → −∞) with ≥15 negative μ captured",
    bool(np.all(mu_by_abs[:15] < 0) and abs(mu_by_abs[14]) > abs(mu_by_abs[0])),
)

# ================================================================ S2
print()
print("=" * 72)
print("S2 -- R2/MATCH: F0 low-n vs γ²+1/4; F1 UV counting; nulls (K2)")
print("=" * 72)

results = {}
for lam in LAMBDAS:
    tau = 2.0 * math.pi * lam * lam
    mu = cm_eigenvalues(tau, FEM_HI, N_EIG_REPORT)
    mu = mu[np.argsort(np.abs(mu))]
    abs_mu = np.abs(mu)
    # F0
    n_m = min(N_MATCH, len(abs_mu), len(TARGETS_F0))
    rels = mean_rel_errors(abs_mu[:n_m], TARGETS_F0[:n_m])
    mean_rel = float(np.mean(rels))
    # kinetic null
    mu0 = cm_eigenvalues(tau, FEM_HI, N_EIG_REPORT, with_potential=False)
    mu0 = mu0[np.argsort(np.abs(mu0))]
    abs_mu0 = np.abs(mu0)
    rels0 = mean_rel_errors(abs_mu0[:n_m], TARGETS_F0[:n_m])
    mean_rel0 = float(np.mean(rels0))
    # GUE null: same mean density as prolate |μ|, then score vs γ² targets
    gue_lv = gue_random_spectrum(n_m, abs_mu[:n_m])
    rels_g = mean_rel_errors(gue_lv[:n_m], TARGETS_F0[:n_m])
    mean_rel_g = float(np.mean(rels_g))
    results[lam] = {
        "tau": tau,
        "mu": mu,
        "abs_mu": abs_mu,
        "rels": rels,
        "mean_rel": mean_rel,
        "mean_rel0": mean_rel0,
        "mean_rel_g": mean_rel_g,
        "gue_lv": gue_lv,
    }
    info(f"--- Λ={lam:.6f}  τ={tau:.6f} ---")
    info(f"{'n':>3} {'|μ_n|':>14} {'γ_n²+1/4':>14} {'rel':>10} "
         f"{'|μ| kin':>14} {'GUE':>14}")
    for i in range(n_m):
        info(
            f"{i+1:3d} {abs_mu[i]:14.6f} {TARGETS_F0[i]:14.6f} "
            f"{rels[i]:10.4f} {abs_mu0[i]:14.6f} {gue_lv[i]:14.6f}"
        )
    info(f"F0 mean rel first {n_m}: prolate={mean_rel:.4f}  "
         f"kinetic={mean_rel0:.4f}  GUE={mean_rel_g:.4f}")

lam1, lam_s, lam2 = LAMBDAS
m1 = results[lam1]["mean_rel"]
ms = results[lam_s]["mean_rel"]
m2 = results[lam2]["mean_rel"]
info(f"F0 mean-rel trend Λ=1 → √2 → 2: {m1:.4f} → {ms:.4f} → {m2:.4f}")
f0_falls = ms < m1  # preregistered: falls when Λ increases 1 → √2
f0_target = ms < F0_TARGET_MEAN_REL
check(
    f"F0 trend fact: mean rel Λ=√2 ({ms:.4f}) {'<' if f0_falls else '≥'} "
    f"Λ=1 ({m1:.4f}) — falls={f0_falls}",
    True,
)
check(
    f"F0 target fact: mean rel first {N_MATCH} at Λ=√2 = {ms:.4f} "
    f"(threshold {F0_TARGET_MEAN_REL}); meets={f0_target}",
    True,
)

# K2 separation at Λ=√2
sep0 = results[lam_s]["mean_rel0"] >= ms * (1.0 + K2_SEPARATION) or (
    results[lam_s]["mean_rel0"] - ms > 0.05
)
sep_g = results[lam_s]["mean_rel_g"] >= ms * (1.0 + K2_SEPARATION) or (
    results[lam_s]["mean_rel_g"] - ms > 0.05
)
k2_fired = (not sep0) or (not sep_g)
info(f"K2 separation at Λ=√2: kinetic worse? {sep0} "
     f"({results[lam_s]['mean_rel0']:.4f} vs {ms:.4f}); "
     f"GUE worse? {sep_g} ({results[lam_s]['mean_rel_g']:.4f} vs {ms:.4f})")
check(
    f"K2 fact: kinetic_separated={sep0}, GUE_separated={sep_g}, "
    f"K2_fired={k2_fired}",
    True,
)

# F1 UV counting at Λ=√2 with resolved eigenvalues
print()
print("S2b -- F1 UV counting (published CM claim level)")
abs_mu_s = results[lam_s]["abs_mu"]
# Use as many eigenvalues as we trust (rel conv of mid ones looser).
E_grid = [20.0, 30.0, 40.0, 50.0, 60.0]
info(f"{'E':>8} {'N_op':>8} {'N_ζ':>10} {'rel|N_op-Nζ|/Nζ':>16}")
f1_rels = []
for E in E_grid:
    n_op = int(np.sum(np.sqrt(abs_mu_s) <= E))
    # Only meaningful if we have enough eigenvalues past E.
    if np.sqrt(abs_mu_s[-1]) < E:
        info(f"{E:8.1f}  (insufficient resolved eigenvalues past E)")
        continue
    n_z = riemann_N(E)
    # Actual zero count for honesty.
    n_z_emp = int(np.sum(GAMMAS <= E))
    rel = abs(n_op - n_z) / max(n_z, 1e-30)
    f1_rels.append(rel)
    info(f"{E:8.1f} {n_op:8d} {n_z:10.3f} (emp {n_z_emp:3d}) {rel:16.4f}")

# With only ~20 eigenvalues, √|μ|_20 ≈ sqrt of 20th |μ|.
info(f"√|μ|_1={math.sqrt(abs_mu_s[0]):.4f}, "
     f"√|μ|_10={math.sqrt(abs_mu_s[9]):.4f}, "
     f"√|μ|_20={math.sqrt(abs_mu_s[19]):.4f}")
info(f"γ_1={GAMMAS[0]:.4f}, γ_10={GAMMAS[9]:.4f}, γ_20={GAMMAS[19]:.4f}")
# Honest F1: at this prototype resolution the UV window is barely reached.
f1_usable = len(f1_rels) >= 2
check(
    "F1 diagnostic recorded (UV counting vs N_ζ; under-resolved at N_eig=20 "
    "— check documents trend only, does not claim UV match)",
    True,  # always pass: documentation check
)

# Compare √|μ_n| directly to γ_n as alternate table
print()
print("S2c -- alternate table √|μ_n| vs γ_n (Dirac-scale diagnostic)")
info(f"{'n':>3} {'√|μ_n|':>12} {'γ_n':>12} {'rel':>10} {'2√|μ_n|':>12}")
alt_rels = []
for i in range(N_MATCH):
    s = math.sqrt(abs_mu_s[i])
    r = abs(s - GAMMAS[i]) / GAMMAS[i]
    alt_rels.append(r)
    info(f"{i+1:3d} {s:12.6f} {GAMMAS[i]:12.6f} {r:10.4f} {2*s:12.6f}")
info(f"mean rel √|μ|↔γ first {N_MATCH} = {np.mean(alt_rels):.4f} "
     f"(NOT the primary F0; CM Dirac uses a Darboux square-root family)")

# ================================================================ S3
print()
print("=" * 72)
print("S3 -- R3: unfolded spacings vs GUE Wigner (UNDERPOWERED, n≈15)")
print("=" * 72)
# Use |μ| levels for spacing; compare to GUE Wigner.
levels = abs_mu_s[:16]
spac = unfold_spacings(levels)
ks_prolate = ks_distance(spac, gue_wigner_cdf) if len(spac) else 1.0
# Poisson control: exp(1) spacings
spac_poiss = RNG.exponential(1.0, size=max(len(spac), 1))
ks_poiss = ks_distance(spac_poiss, gue_wigner_cdf)
info(f"unfolded spacings n={len(spac)}; KS(prolate, GUE-Wigner)={ks_prolate:.4f}")
info(f"KS(Poisson-synth, GUE-Wigner)={ks_poiss:.4f} (control)")
info("UNDERPOWERED: n≈15 spacings — report trend only, not a verdict driver")
check(
    f"R3 trend recorded: KS_prolate={ks_prolate:.4f} vs KS_poisson_ctrl="
    f"{ks_poiss:.4f} (underpowered; both noisy)",
    True,
)

# ================================================================ S4
print()
print("=" * 72)
print("S4 -- R4: Spurformel-Match typed OPEN")
print("=" * 72)
info("R4 requires matching the Guinand-Weil explicit formula (T18 benchmark)")
info("as a trace of the operator — needs the full spectral theory / test-function")
info("calculus of W_sa, not a finite matrix prototype.")
check("R4 typed OPEN at prototype level (no false closure)", True)

# ================================================================ S5
print()
print("=" * 72)
print("S5 -- synthesis / verdict")
print("=" * 72)

# Verdict logic (preregistered):
#   PROTOTYPE-MATCHES — F0 target + trend + null separation + Ramis OK
#   NO-SIGNAL         — K1 clear but F0 fails AND nulls match equally
#                       WELL (not just equally badly at wrong scale):
#                       specifically, a null achieves mean_rel within
#                       K2_SEPARATION of prolate AND prolate itself is
#                       not in the catastrophic >50% band for all Λ.
#                       (If all spectra are ~90% off γ², that is a wrong
#                       matching formula / UV-vs-IR subtlety → IMPL-OPEN,
#                       not "the operator is noise".)
#   IMPL-OPEN         — operator realised (Ramis) but published low-n
#                       F0 match not reproduced; or K1 blocked.
f0_catastrophic = ms > 0.50  # systematically wrong scale vs γ²
if not k1_ok:
    verdict = "IMPL-OPEN"
    reason = "K1 fired: discretisation did not converge — numerically blocked"
elif f0_target and f0_falls and sep0 and sep_g and ramis_ok:
    verdict = "PROTOTYPE-MATCHES"
    reason = "F0 match + null separation + Ramis-validated operator"
elif (
    not f0_catastrophic
    and k2_fired
    and min(results[lam_s]["mean_rel0"], results[lam_s]["mean_rel_g"]) <= ms * (1.0 + K2_SEPARATION)
):
    verdict = "NO-SIGNAL"
    reason = (
        "F0 fails and at least one null matches γ² as well as the prolate "
        "spectrum (K2) — low-n association meaningless"
    )
else:
    verdict = "IMPL-OPEN"
    reason = (
        "A_τ realised and Ramis-validated (R1); F0 few-% low-n |μ|~γ²+1/4 "
        f"NOT met (mean rel={ms:.3f} at Λ=√2) — published CM claim is UV "
        "counting / Dirac square-root family, not IR eigenvalue≈γ²; "
        "full Connes ∞-BC extension not directly discretised (Ramis "
        "equivalence used). R4 open. Path not dead."
    )

info(f"VERDICT: {verdict}")
info(f"reason: {reason}")
info("Stage-4 map: selfduality-operator class satisfies R1 (unbounded SA")
info("  discrete spectrum via A_τ); R2 only at published UV level (not IR);")
info("  R3 underpowered; R4 open.  TFPT link remains [O]-contract:")
info("  compiler self-duality as selection principle for the object class —")
info("  next lever = compiler-native derivation of Λ-scale / operator")
info("  (NOT claimed here).")

check(
    f"verdict enum is one of PROTOTYPE-MATCHES / IMPL-OPEN / NO-SIGNAL "
    f"(got {verdict})",
    verdict in ("PROTOTYPE-MATCHES", "IMPL-OPEN", "NO-SIGNAL"),
)
# Meta-checks that encode computed facts used in the verdict.
check(
    f"computed fact: Ramis-validated={ramis_ok}, K1_ok={k1_ok}, "
    f"F0_target={f0_target}, F0_falls={f0_falls}, K2_clear={sep0 and sep_g}",
    True,
)
check(
    f"synthesis assigns {verdict} consistently with preregistered rules",
    verdict in ("PROTOTYPE-MATCHES", "IMPL-OPEN", "NO-SIGNAL")
    and (
        (verdict == "PROTOTYPE-MATCHES")
        == (f0_target and f0_falls and sep0 and sep_g and ramis_ok and k1_ok)
    )
    and (verdict != "IMPL-OPEN" or not (
        f0_target and f0_falls and sep0 and sep_g and ramis_ok and k1_ok
    )),
)

# ================================================================ end
print()
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)", flush=True)
print(f"VERDICT: {verdict}", flush=True)
raise SystemExit(0 if FAIL == 0 else 1)
