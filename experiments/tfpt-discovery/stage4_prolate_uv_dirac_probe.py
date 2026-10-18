"""Discovery probe (2026-07-25), part 47 of the zeta/prime investigation.
UV / DIRAC PROTOTYPE of the Stage-4 selfduality-operator class, following
the diagnosis of part 46 (stage4_prolate_prototype_probe.py): the published
Connes–Moscovici 2022 identification is NOT the IR interior / Ramis A_τ
eigenvalue↔γ² pairing, but the ultraviolet behaviour of the negative
spectrum of the self-adjoint extension W_sa (Sonin / exterior sector) and
of a Darboux square-root Dirac family.

Classical / external object (named as such — NOT a TFPT derivation):
  Connes–Moscovici 2022, PNAS / arXiv:2112.05500,
  "The UV prolate spectrum matches the zeros of zeta".
  Prolate operator (Slepian / Landau / Pollak; CM eq. (1)):
      W_Λ u = -d/dx((Λ² - x²) du/dx) + (2π Λ)² x² u
  Unique self-adjoint extension W_sa commuting with the cutoff P_Λ and
  with Fourier (CM Thm 2.6): deficiency indices (4,4); published domain
  L_β enforces the natural flux condition at the regular singular points
      lim_{x→±Λ} (Λ² - x²) u'(x) = 0
  and oscillatory LCO conditions at ±∞ (even sector ~ sin(2π Λ x)/x).
  Because W_sa commutes with P_Λ, interior and exterior spectra DECOUPLE
  (documented convention C1): the zeta-related negative eigenvalues live
  on the EXTERIOR restriction (I − P_Λ) W_sa / Sonin space.
  Semiclassical UV counting of negative eigenvalues |μ| ≤ E² tracks
  squares of zeta zeros for Λ ∈ {1, √2} (CM §4).  Darboux / Riccati
  square-root D/ satisfies (CM Thm 6.1, Λ = √2): spectrum of 2 D/ lies
  in R ∪ iR and the positive-imaginary counting matches the Riemann
  main term; imaginary eigenvalues are ξ = ± 2 √α with α ∈ spec(W_sa).
  Ramis–Richard–Jung–Thomann (C.R. Math. 2025) equate the non-classical
  CM negative spectrum with the imaginary-axis operator
      A_τ u = -d/dt((1+t²) du/dt) + τ² t² u ,   τ = 2π Λ²,
  via μ = -λ (T46 validated: μ₁ = −13.3088 vs lit −13.3027).

Convention decisions (every choice named):
  C1  Dual track (honest about numerics):
        TRACK A (PRIMARY): Dirac maps on Ramis A_τ negative spectrum —
          the published CM negative spectrum via Ramis equivalence;
          FEM already R1-validated in T46.  No artificial θ here.
        TRACK B (SECONDARY): direct exterior FEM on [Λ, X_max] with
          one-parameter limit-circle family U(θ) at x=Λ, as a
          reconstruction attempt of the exterior problem.  LCO at ∞
          makes low eigenvalues truncation-sensitive — K1 may fire.
  C2  Λ = √2 (CM §6 published Dirac case); Λ = 1 retained as diagnostic.
  C3  A_τ / W sign: as in T46 / CM (1).  Negative μ ⇒ UV / Sonin sector.
  C4  Track B far BC: truncate even oscillatory condition at finite X_max,
      preferring Dirichlet at nodes sin(2π Λ X)=0 (clean LCO samples);
      also Robin form of CM (17) as fallback.  X_max convergence checked.
  C5  Track B near BC family U(θ), θ ∈ [0, π):
          cos(θ) · u(Λ+) + sin(θ) · lim (p u') = 0,  p=Λ²−x².
      Published CM choice: θ = π/2 (pure flux-zero / L_β).
  C6  Dirac / matching family (PREREGISTERED, look-elsewhere of size 3):
        S0 (PRIMARY, CM Thm 6.1):  δ_n = 2 √|μ_n|
        S1:                         δ_n = √|μ_n|
        S2:                         δ_n = √(|μ_n| + 1/4)
      Targets: ordered ζ-zeros γ_n = Im ρ_n.
      No free affine α beyond this LEE of 3 — a fitted global scale
      that is not one of {1,2}·√|μ| or √(|μ|+1/4) would be a different
      claim than CM Thm 6.1 and is NOT admitted to the success criterion.
  C7  Track A has fixed spectrum (Ramis); training chooses S ∈ {S0,S1,S2}
      only.  Track B trains the geometric θ (C5) together with S.
  C8  K1 (Track A): two A_τ FEM resolutions agree < 5% on lowest 5 |μ|
      (T46 standard).  K1 (Track B): mesh+X agree < 10% on lowest 5;
      ALSO report UV-window (indices 4..8) convergence as soft diagnostic.
  C9  Mesh non-degradation: OOS_HI ≤ OOS_LO + 0.005 (absolute FEM noise
      allowance on the relative-error scale — "falls or stays").

Sections:
  S0  Preregistered criteria + ζ-zero cache.
  S1  U1: Track A Ramis A_τ (K1-A); Track B exterior FEM (K1-B).
  S2  U2: train/test Dirac match on both tracks; null controls.
  S3  R3 spacing trend (underpowered); R4 typed OPEN.
  S4  Synthesis / verdict enum.

PREREGISTERED CRITERIA (frozen before runs):
  Track A train: choose S ∈ {S0,S1,S2} on the fixed A_τ spectrum to
      minimise mean rel δ_n↔γ_n for n=1,2,3.  LEE size 3 documented.
  Track B train: choose (θ, S) on exterior spectrum likewise.
  Out-of-sample success on a track:
      mean rel(δ_n, γ_n) for n=4..10 < 0.05
      AND mean rel does not degrade under mesh refinement LO→HI.
  Nulls (on the driving track): GUE same-density and kinetic-only must
      be clearly worse (null ≥ proto·1.20 or +0.05 abs).
  Kills / verdict (driving = Track A if K1-A clear; else Track B):
      K1 both blocked → IMPL-BLOCKED.
      K1 clear on driving track but no OOS success → UV-NO-SIGNAL.
      OOS success + null separation on driving track → UV-PROTOTYPE-MATCHES.
  Verdicts: UV-PROTOTYPE-MATCHES / IMPL-BLOCKED / UV-NO-SIGNAL.
  R3 underpowered (report only); R4 always OPEN.
  Fence: classical / external reproduction attempt — NOT a TFPT result,
  NOT RH progress, NOT evidence for the Riemann hypothesis.

Firewall: discovery sandbox — no promotion, no ledger / paper / website /
marker / next.txt edits; classical (Slepian, Weyl limit-circle,
Connes–Moscovici 2022, Ramis et al.) named as classical / external;
ABSOLUTELY no RH-evidence language.
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
LAM = math.sqrt(2.0)
LAM_DIAG = 1.0
# Track A: A_τ FEM (T46-compatible)
FEM_LO = (10.0, 600)
FEM_HI = (14.0, 1200)
# Track B: exterior
XMAX_LO = 24.0
XMAX_HI = 36.0
N_MESH_LO = 800
N_MESH_HI = 1600
N_NEG_KEEP = 24
N_TRAIN = 3
N_TEST_END = 10
N_THETA = 37
THETA_GRID = np.linspace(0.0, math.pi, N_THETA, endpoint=False)
OOS_MEAN_REL = 0.05
MESH_ABS_TOL = 0.005  # C9: OOS may "stay" within this absolute band
K1A_TOL = 0.05
K1B_TOL = 0.10
K2_SEPARATION = 0.20
RAMIS_MU_ODD1 = -13.3027463832915625
RAMIS_MU_EVEN1 = -39.38321657426153947615
RAMIS_TOL_REL = 0.02


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


# ================================================================ FEM core
def assemble_A_tau_fem(tau: float, T: float, n_interior: int, with_potential: bool):
    """P1 FEM for A_τ on [-T, T], Dirichlet ends (T46)."""
    n_el = n_interior + 1
    h = 2.0 * T / n_el
    t = np.linspace(-T, T, n_el + 1)
    n = n_interior
    amat = np.zeros((n, n))
    mass = np.zeros((n, n))
    xi = np.array([-1.0 / math.sqrt(3.0), 1.0 / math.sqrt(3.0)])
    wloc = np.array([1.0, 1.0])
    for e in range(n_el):
        t0, t1 = t[e], t[e + 1]
        tt = 0.5 * (t0 + t1) + 0.5 * (t1 - t0) * xi
        jac = 0.5 * h
        dN = np.array([-1.0 / h, 1.0 / h])
        for a in range(2):
            for b in range(2):
                k_ab = m_ab = p_ab = 0.0
                for q in range(2):
                    Na = 0.5 * (1.0 - xi[q]) if a == 0 else 0.5 * (1.0 + xi[q])
                    Nb = 0.5 * (1.0 - xi[q]) if b == 0 else 0.5 * (1.0 + xi[q])
                    k_ab += wloc[q] * jac * (1.0 + tt[q] * tt[q]) * dN[a] * dN[b]
                    m_ab += wloc[q] * jac * Na * Nb
                    p_ab += wloc[q] * jac * (tt[q] * tt[q]) * Na * Nb
                ga, gb = e + a - 1, e + b - 1
                if 0 <= ga < n and 0 <= gb < n:
                    amat[ga, gb] += k_ab + (tau * tau * p_ab if with_potential else 0.0)
                    mass[ga, gb] += m_ab
    return 0.5 * (amat + amat.T), 0.5 * (mass + mass.T)


def generalised_eigh(amat, mass) -> np.ndarray:
    evals_m, evecs_m = np.linalg.eigh(mass)
    evals_m = np.maximum(evals_m, 1e-14)
    inv_sqrt = evecs_m * (1.0 / np.sqrt(evals_m))
    a_red = inv_sqrt.T @ amat @ inv_sqrt
    a_red = 0.5 * (a_red + a_red.T)
    return np.sort(np.linalg.eigh(a_red)[0])


def cm_neg_from_Atau(tau: float, fem_spec, n_keep: int, with_potential: bool = True):
    T, n_int = fem_spec
    amat, mass = assemble_A_tau_fem(tau, T, n_int, with_potential)
    lam = generalised_eigh(amat, mass)
    mu = -lam
    mu = mu[mu < -1e-8]
    mu = mu[np.argsort(np.abs(mu))]
    return mu[:n_keep]


def graded_nodes(lam: float, xmax: float, n_unknowns: int) -> np.ndarray:
    n_el = n_unknowns + 1
    s = np.linspace(0.0, 1.0, n_el + 1)
    x = lam + (xmax - lam) * (s * s)
    x[0] = lam
    x[-1] = xmax
    return x


def dirichlet_node_xmax(lam: float, target: float) -> float:
    """Nearest X ≥ target with sin(2π Λ X) = 0, X = k/(2Λ), k∈N."""
    step = 1.0 / (2.0 * lam)
    k = max(1, int(math.ceil(target / step - 1e-12)))
    return k * step


def far_robin_coeff(lam: float, xmax: float) -> float:
    kappa = 2.0 * math.pi * lam * xmax
    sk, ck = math.sin(kappa), math.cos(kappa)
    if abs(sk) < 1e-8:
        return float("nan")
    kx = 2.0 * math.pi * lam
    return (kx * xmax * ck - sk) / (xmax * sk)


def assemble_exterior_fem(
    lam: float,
    xmax: float,
    n_unknowns: int,
    theta: float,
    with_potential: bool = True,
):
    """P1 FEM exterior W on [Λ, X] with U(θ) at Λ (C5) and C4 at X."""
    nodes = graded_nodes(lam, xmax, n_unknowns)
    n_nodes = len(nodes)
    sin_t, cos_t = math.sin(theta), math.cos(theta)
    dirichlet_near = abs(sin_t) < 1e-10
    c_far = far_robin_coeff(lam, xmax)
    far_dirichlet = not math.isfinite(c_far)
    active = np.ones(n_nodes, dtype=bool)
    if dirichlet_near:
        active[0] = False
    if far_dirichlet:
        active[-1] = False
    idx = np.where(active)[0]
    n = len(idx)
    inv = -np.ones(n_nodes, dtype=int)
    inv[idx] = np.arange(n)
    amat = np.zeros((n, n))
    mass = np.zeros((n, n))
    q0 = (2.0 * math.pi * lam) ** 2
    xi = np.array([-1.0 / math.sqrt(3.0), 1.0 / math.sqrt(3.0)])
    wloc = np.array([1.0, 1.0])
    for e in range(n_nodes - 1):
        x0, x1 = float(nodes[e]), float(nodes[e + 1])
        h = x1 - x0
        if h <= 0:
            continue
        tt = 0.5 * (x0 + x1) + 0.5 * h * xi
        jac = 0.5 * h
        dN = np.array([-1.0 / h, 1.0 / h])
        for a in range(2):
            for b in range(2):
                k_ab = m_ab = 0.0
                for q in range(2):
                    Na = 0.5 * (1.0 - xi[q]) if a == 0 else 0.5 * (1.0 + xi[q])
                    Nb = 0.5 * (1.0 - xi[q]) if b == 0 else 0.5 * (1.0 + xi[q])
                    pval = lam * lam - tt[q] * tt[q]
                    k_ab += wloc[q] * jac * pval * dN[a] * dN[b]
                    if with_potential:
                        k_ab += wloc[q] * jac * q0 * (tt[q] * tt[q]) * Na * Nb
                    m_ab += wloc[q] * jac * Na * Nb
                ga, gb = inv[e + a], inv[e + b]
                if ga >= 0 and gb >= 0:
                    amat[ga, gb] += k_ab
                    mass[ga, gb] += m_ab
    if (not dirichlet_near) and inv[0] >= 0:
        amat[inv[0], inv[0]] += -(cos_t / sin_t)
    if (not far_dirichlet) and inv[-1] >= 0 and math.isfinite(c_far):
        pX = lam * lam - xmax * xmax
        amat[inv[-1], inv[-1]] += -pX * c_far
    meta = {
        "n": n,
        "dirichlet_near": dirichlet_near,
        "far_dirichlet": far_dirichlet,
        "c_far": c_far,
        "theta": theta,
        "xmax": xmax,
    }
    return 0.5 * (amat + amat.T), 0.5 * (mass + mass.T), meta


def negative_eigs(amat, mass, n_keep: int) -> np.ndarray:
    ev = generalised_eigh(amat, mass)
    neg = ev[ev < -1e-8]
    if len(neg) == 0:
        return np.array([])
    return neg[np.argsort(np.abs(neg))][:n_keep]


def exterior_neg(lam, xmax, n_mesh, theta, n_keep, with_potential=True):
    amat, mass, meta = assemble_exterior_fem(
        lam, xmax, n_mesh, theta, with_potential=with_potential
    )
    return negative_eigs(amat, mass, n_keep), meta


# ================================================================ maps / stats
def apply_map(kind: str, mu_neg: np.ndarray) -> np.ndarray:
    """Dirac-scale maps (C6). kind in {S0, S1, S2}."""
    abs_mu = np.abs(mu_neg)
    if kind == "S0":
        return 2.0 * np.sqrt(abs_mu)
    if kind == "S1":
        return np.sqrt(abs_mu)
    if kind == "S2":
        return np.sqrt(abs_mu + 0.25)
    raise ValueError(kind)


def mean_rel(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.mean(np.abs(a - b) / np.maximum(np.abs(b), 1e-30)))


def gue_spectrum_like(n: int, ref_levels: np.ndarray) -> np.ndarray:
    ref = np.sort(np.asarray(ref_levels[:n], dtype=float))
    mean_sp = float(np.mean(np.diff(ref))) if n > 1 else 1.0
    spac = []
    while len(spac) < n - 1:
        s = RNG.uniform(0.0, 4.0)
        pdf = (32.0 / math.pi ** 2) * s * s * math.exp(-4.0 * s * s / math.pi)
        if RNG.uniform(0.0, 0.6) < pdf:
            spac.append(s)
    spac = np.asarray(spac[: n - 1], dtype=float)
    spac = spac / float(np.mean(spac)) * mean_sp
    return ref[0] + np.concatenate([[0.0], np.cumsum(spac)])


def unfold_spacings(levels: np.ndarray) -> np.ndarray:
    x = np.sort(np.asarray(levels, dtype=float))
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 5:
        return np.array([])
    idx = np.arange(1, n + 1, dtype=float)
    N_smooth = np.polyval(np.polyfit(x, idx, 2), x)
    for i in range(1, n):
        if N_smooth[i] <= N_smooth[i - 1]:
            N_smooth[i] = N_smooth[i - 1] + 1e-9
    spac = np.diff(N_smooth)
    spac = spac[spac > 0]
    ms = float(np.mean(spac))
    return spac / ms if ms > 0 else np.array([])


def gue_wigner_cdf(s: float) -> float:
    if s <= 0:
        return 0.0
    a = 4.0 / math.pi
    from math import erf

    sqrt_a = math.sqrt(a)
    integ = (math.sqrt(math.pi) / (4.0 * a ** 1.5)) * erf(sqrt_a * s) - (
        s * math.exp(-a * s * s) / (2.0 * a)
    )
    return float((32.0 / math.pi ** 2) * integ)


def ks_distance(sample: np.ndarray, cdf) -> float:
    x = np.sort(sample)
    n = len(x)
    if n == 0:
        return 1.0
    F = np.array([cdf(float(xi)) for xi in x])
    return float(
        max(
            np.max(np.abs(np.arange(1, n + 1) / n - F)),
            np.max(np.abs(np.arange(0, n) / n - F)),
        )
    )


def riemann_N(E: float) -> float:
    if E <= 2.0 * math.pi:
        return 0.0
    return (E / (2.0 * math.pi)) * math.log(E / (2.0 * math.pi * math.e)) + 7.0 / 8.0


# ================================================================ S0
print("=" * 72)
print("S0 -- preregistered criteria + zero cache")
print("=" * 72)
info("Classical/external: Connes–Moscovici 2022 UV/Dirac (NOT TFPT, no RH)")
info("C1 dual track: A=Ramis A_τ Dirac (primary); B=exterior U(θ) (secondary)")
info("C2 Λ=√2; C6 LEE={S0=2√|μ|, S1=√|μ|, S2=√(|μ|+1/4)} — no free α")
info("Train n=1..3; OOS success: mean rel n=4..10 < 5% + mesh non-degrade")
info("K1-A: A_τ FEM <5% lowest5; K1-B: exterior mesh/X <10% lowest5")
info("Verdict driver: Track A if K1-A clear, else Track B if K1-B clear,")
info("                else IMPL-BLOCKED")

t_z = time.time()
GAMMAS = np.array([float(mpmath.zetazero(n).imag) for n in range(1, N_ZEROS + 1)])
info(
    f"cached {N_ZEROS} zeta zeros in {time.time() - t_z:.1f}s; "
    f"γ1={GAMMAS[0]:.6f}, γ10={GAMMAS[9]:.6f}"
)
check(
    f"zero cache length={N_ZEROS}, strictly increasing, γ1≈14.1347",
    len(GAMMAS) == N_ZEROS
    and bool(np.all(np.diff(GAMMAS) > 0))
    and abs(GAMMAS[0] - 14.134725) < 1e-4,
)
TRAIN_G = GAMMAS[:N_TRAIN]
TEST_G = GAMMAS[N_TRAIN:N_TEST_END]
info(f"train γ={np.array2string(TRAIN_G, precision=4)}")
info(f"test  γ[4..{N_TEST_END}]={np.array2string(TEST_G, precision=4)}")

# ================================================================ S1A
print()
print("=" * 72)
print("S1a -- TRACK A: Ramis A_τ negative spectrum (K1-A, primary)")
print("=" * 72)

tau = 2.0 * math.pi * LAM * LAM
mu_A_hi = cm_neg_from_Atau(tau, FEM_HI, N_NEG_KEEP)
mu_A_lo = cm_neg_from_Atau(tau, FEM_LO, N_NEG_KEEP)
mu_A_kin = cm_neg_from_Atau(tau, FEM_HI, N_NEG_KEEP, with_potential=False)

amat_s, mass_s = assemble_A_tau_fem(tau, FEM_HI[0], FEM_HI[1], True)
sym_err = float(np.max(np.abs(amat_s - amat_s.T)))
check(
    f"A_τ FEM symmetric (max|A-A^T|={sym_err:.2e})",
    sym_err < 1e-10,
)

rel_A = np.abs(np.abs(mu_A_lo[:5]) - np.abs(mu_A_hi[:5])) / np.maximum(
    np.abs(mu_A_hi[:5]), 1e-30
)
k1a_ok = bool(rel_A.max() < K1A_TOL)
info(f"A_τ HI |μ|[:6]={np.array2string(np.abs(mu_A_hi[:6]), precision=5)}")
info(f"A_τ LO |μ|[:6]={np.array2string(np.abs(mu_A_lo[:6]), precision=5)}")
info(f"K1-A max rel lowest5 = {rel_A.max():.4e}")
check(
    f"K1-A fact: two A_τ FEM agree < {K1A_TOL:.0%} on lowest5 "
    f"(max rel={rel_A.max():.4e}); clear={k1a_ok}",
    True,
)

rel_odd = abs(mu_A_hi[0] - RAMIS_MU_ODD1) / abs(RAMIS_MU_ODD1)
rel_even = abs(mu_A_hi[1] - RAMIS_MU_EVEN1) / abs(RAMIS_MU_EVEN1)
ramis_ok = rel_odd < RAMIS_TOL_REL and rel_even < RAMIS_TOL_REL
info(f"Ramis μ1: num={mu_A_hi[0]:.8f} lit={RAMIS_MU_ODD1:.8f} rel={rel_odd:.4e}")
info(f"Ramis μ2: num={mu_A_hi[1]:.8f} lit={RAMIS_MU_EVEN1:.8f} rel={rel_even:.4e}")
check(
    f"Ramis anchors at τ=4π within {RAMIS_TOL_REL} (validates Track A)",
    ramis_ok,
)

info("Track A published S0=2√|μ| vs γ (diagnostic):")
dA0 = apply_map("S0", mu_A_hi[:N_TEST_END])
info(f"{'n':>3} {'2√|μ|':>12} {'γ':>12} {'rel':>10}")
for i in range(N_TEST_END):
    r = abs(dA0[i] - GAMMAS[i]) / GAMMAS[i]
    info(f"{i+1:3d} {dA0[i]:12.6f} {GAMMAS[i]:12.6f} {r:10.4f}")

# ================================================================ S1B
print()
print("=" * 72)
print("S1b -- TRACK B: exterior FEM + U(θ) (K1-B, secondary)")
print("=" * 72)

# Prefer Dirichlet nodes for clean LCO sampling (C4).
X_HI = dirichlet_node_xmax(LAM, XMAX_HI)
X_LO = dirichlet_node_xmax(LAM, XMAX_LO)
info(f"Dirichlet-node X_LO={X_LO:.6f}, X_HI={X_HI:.6f} (sin(2πΛX)=0)")

theta_cm = 0.5 * math.pi
mu_B_hi, meta_B = exterior_neg(LAM, X_HI, N_MESH_HI, theta_cm, N_NEG_KEEP)
mu_B_lo_m, _ = exterior_neg(LAM, X_HI, N_MESH_LO, theta_cm, N_NEG_KEEP)
mu_B_lo_x, _ = exterior_neg(LAM, X_LO, N_MESH_HI, theta_cm, N_NEG_KEEP)
info(
    f"meta: n={meta_B['n']}, far_D={meta_B['far_dirichlet']}, "
    f"c_far={meta_B['c_far'] if math.isfinite(meta_B['c_far']) else float('nan')}"
)
info(f"B HI  |μ|[:6]={np.array2string(np.abs(mu_B_hi[:6]), precision=5)}")
info(f"B mesh|μ|[:6]={np.array2string(np.abs(mu_B_lo_m[:6]), precision=5)}")
info(f"B X   |μ|[:6]={np.array2string(np.abs(mu_B_lo_x[:6]), precision=5)}")

n_cmp = min(5, len(mu_B_hi), len(mu_B_lo_m), len(mu_B_lo_x))
if n_cmp >= 5:
    rel_Bm = np.abs(np.abs(mu_B_lo_m[:5]) - np.abs(mu_B_hi[:5])) / np.maximum(
        np.abs(mu_B_hi[:5]), 1e-30
    )
    rel_Bx = np.abs(np.abs(mu_B_lo_x[:5]) - np.abs(mu_B_hi[:5])) / np.maximum(
        np.abs(mu_B_hi[:5]), 1e-30
    )
    # UV-window soft diagnostic (indices 4..8 → 0-based 3..7)
    uv_ok = False
    if min(len(mu_B_hi), len(mu_B_lo_m), len(mu_B_lo_x)) >= 8:
        sl = slice(3, 8)
        r_uv_m = np.abs(np.abs(mu_B_lo_m[sl]) - np.abs(mu_B_hi[sl])) / np.maximum(
            np.abs(mu_B_hi[sl]), 1e-30
        )
        r_uv_x = np.abs(np.abs(mu_B_lo_x[sl]) - np.abs(mu_B_hi[sl])) / np.maximum(
            np.abs(mu_B_hi[sl]), 1e-30
        )
        uv_ok = bool(r_uv_m.max() < K1B_TOL and r_uv_x.max() < K1B_TOL)
        info(f"K1-B UV-window(4..8) mesh max rel={r_uv_m.max():.4e}, "
             f"X max rel={r_uv_x.max():.4e}; soft_ok={uv_ok}")
else:
    rel_Bm = np.array([1.0])
    rel_Bx = np.array([1.0])
    uv_ok = False

k1b_ok = bool(n_cmp >= 5 and rel_Bm.max() < K1B_TOL and rel_Bx.max() < K1B_TOL)
info(f"K1-B IR lowest5 mesh max rel={rel_Bm.max():.4e}, X max rel={rel_Bx.max():.4e}")
check(
    f"K1-B fact: exterior mesh+X < {K1B_TOL:.0%} on lowest5 "
    f"(mesh={rel_Bm.max():.4e}, X={rel_Bx.max():.4e}); clear={k1b_ok}; "
    f"UV-window soft_ok={uv_ok}",
    True,
)
check(
    f"Track B resolved ≥10 negative eigs at HI (got {len(mu_B_hi)})",
    len(mu_B_hi) >= 10,
)

if len(mu_B_hi) >= N_TEST_END:
    dB0 = apply_map("S0", mu_B_hi[:N_TEST_END])
    info("Track B θ=π/2 S0=2√|μ| vs γ (diagnostic, pre-training):")
    info(f"{'n':>3} {'2√|μ|':>12} {'γ':>12} {'rel':>10}")
    for i in range(N_TEST_END):
        r = abs(dB0[i] - GAMMAS[i]) / GAMMAS[i]
        info(f"{i+1:3d} {dB0[i]:12.6f} {GAMMAS[i]:12.6f} {r:10.4f}")

# ================================================================ S2A
print()
print("=" * 72)
print("S2a -- TRACK A: S-family training + OOS + nulls")
print("=" * 72)

# Candidate maps for Track A: preregistered LEE {S0,S1,S2} only (C6/C7).
cands_A = []
lee_A = 0
for sname in ("S0", "S1", "S2"):
    lee_A += 1
    delta = apply_map(sname, mu_A_hi)
    if len(delta) < N_TEST_END:
        continue
    tr = mean_rel(delta[:N_TRAIN], TRAIN_G)
    oos = mean_rel(delta[N_TRAIN:N_TEST_END], TEST_G)
    cands_A.append((tr, oos, sname, delta))

cands_A.sort(key=lambda r: (r[0], r[1]))
best_A = cands_A[0]
tr_A, oos_A, kind_A, delta_A = best_A
delta_A_lo = apply_map(kind_A, mu_A_lo)
oos_A_lo = mean_rel(delta_A_lo[N_TRAIN:N_TEST_END], TEST_G)
mesh_A_ok = oos_A <= oos_A_lo + MESH_ABS_TOL
oos_A_success = bool(oos_A < OOS_MEAN_REL and mesh_A_ok)

info(
    f"TRAIN-A pick: S*={kind_A}, train_rel={tr_A:.4f}, "
    f"OOS={oos_A:.4f}, LO-OOS={oos_A_lo:.4f}, mesh_ok={mesh_A_ok}"
)
info(f"Track A LEE evaluations: {lee_A} (S0/S1/S2)")
for sn, tr, oos in [(c[2], c[0], c[1]) for c in sorted(cands_A, key=lambda r: r[1])]:
    info(f"  S={sn}: train={tr:.4f} OOS={oos:.4f}")
info(f"{'n':>3} {'δ_n':>12} {'γ_n':>12} {'rel':>10} {'set':>6}")
for i in range(N_TEST_END):
    r = abs(delta_A[i] - GAMMAS[i]) / GAMMAS[i]
    info(
        f"{i+1:3d} {delta_A[i]:12.6f} {GAMMAS[i]:12.6f} {r:10.4f} "
        f"{'train' if i < N_TRAIN else 'OOS':>6}"
    )

oos_A_cm = mean_rel(apply_map("S0", mu_A_hi)[N_TRAIN:N_TEST_END], TEST_G)
info(f"published CM S0=2√|μ| OOS mean rel = {oos_A_cm:.4f}")

d_kin_A = apply_map(kind_A, mu_A_kin)
oos_kin_A = mean_rel(d_kin_A[N_TRAIN:N_TEST_END], TEST_G)
gue_A = gue_spectrum_like(N_TEST_END, delta_A[:N_TEST_END])
oos_gue_A = mean_rel(gue_A[N_TRAIN:N_TEST_END], TEST_G)
sep_kin_A = oos_kin_A >= oos_A * (1.0 + K2_SEPARATION) or (oos_kin_A - oos_A > 0.05)
sep_gue_A = oos_gue_A >= oos_A * (1.0 + K2_SEPARATION) or (oos_gue_A - oos_A > 0.05)
info(
    f"null-A OOS: kinetic={oos_kin_A:.4f} (worse? {sep_kin_A}), "
    f"GUE={oos_gue_A:.4f} (worse? {sep_gue_A})"
)
check(
    f"Track-A OOS fact: rel={oos_A:.4f}, success={oos_A_success}, S*={kind_A}",
    True,
)
check(
    f"Track-A null facts: kin_sep={sep_kin_A}, GUE_sep={sep_gue_A}",
    True,
)

# UV counting on published S0
print()
print("S2a2 -- UV counting N(E) for Track-A S0=2√|μ| (CM published level)")
d_count = apply_map("S0", mu_A_hi)
info(f"{'E':>8} {'N_op':>8} {'N_ζ':>10} {'emp':>6} {'rel':>10}")
for E in (20.0, 30.0, 40.0, 50.0, 60.0):
    if d_count[-1] < E:
        info(f"{E:8.1f}  (insufficient resolved levels)")
        continue
    n_op = int(np.sum(d_count <= E))
    n_z = riemann_N(E)
    n_emp = int(np.sum(GAMMAS <= E))
    rel = abs(n_op - n_z) / max(n_z, 1e-30)
    info(f"{E:8.1f} {n_op:8d} {n_z:10.3f} {n_emp:6d} {rel:10.4f}")
check("UV counting diagnostic (Track A, S0) recorded", True)

# ================================================================ S2B
print()
print("=" * 72)
print("S2b -- TRACK B: θ-training + OOS + nulls (secondary)")
print("=" * 72)

spectra_B: dict[float, np.ndarray] = {}
t_scan = time.time()
for th in THETA_GRID:
    mu, _ = exterior_neg(LAM, X_HI, N_MESH_HI, float(th), N_NEG_KEEP)
    spectra_B[float(th)] = mu
info(f"θ-scan ({N_THETA} angles) in {time.time() - t_scan:.1f}s")

mu_B_kin, _ = exterior_neg(
    LAM, X_HI, N_MESH_HI, theta_cm, N_NEG_KEEP, with_potential=False
)

cands_B = []
lee_B = 0
for th in THETA_GRID:
    mu = spectra_B[float(th)]
    if len(mu) < N_TEST_END:
        continue
    for sname in ("S0", "S1", "S2"):
        lee_B += 1
        delta = apply_map(sname, mu)
        tr = mean_rel(delta[:N_TRAIN], TRAIN_G)
        oos = mean_rel(delta[N_TRAIN:N_TEST_END], TEST_G)
        cands_B.append((tr, oos, float(th), sname, mu, delta))

cands_B.sort(key=lambda r: (r[0], r[1]))
best_B = cands_B[0]
tr_B, oos_B, th_B, s_B, mu_B_star, delta_B = best_B
mu_B_star_lo, _ = exterior_neg(LAM, X_HI, N_MESH_LO, th_B, N_NEG_KEEP)
oos_B_lo = (
    mean_rel(apply_map(s_B, mu_B_star_lo)[N_TRAIN:N_TEST_END], TEST_G)
    if len(mu_B_star_lo) >= N_TEST_END
    else 1.0
)
mesh_B_ok = oos_B <= oos_B_lo + MESH_ABS_TOL
oos_B_success = bool(
    oos_B < OOS_MEAN_REL and mesh_B_ok and k1b_ok  # require K1-B for B-success
)

info(
    f"TRAIN-B pick: θ*={th_B:.6f} ({th_B/math.pi:.4f}π), S*={s_B}, "
    f"train={tr_B:.4f}, OOS={oos_B:.4f}, LO-OOS={oos_B_lo:.4f}, "
    f"mesh_ok={mesh_B_ok}"
)
info(f"Track B LEE evaluations: {lee_B}")
info(f"|θ*−π/2|={abs(th_B - theta_cm):.4f}")
info(f"{'n':>3} {'δ_n':>12} {'γ_n':>12} {'rel':>10} {'set':>6}")
for i in range(min(N_TEST_END, len(delta_B))):
    r = abs(delta_B[i] - GAMMAS[i]) / GAMMAS[i]
    info(
        f"{i+1:3d} {delta_B[i]:12.6f} {GAMMAS[i]:12.6f} {r:10.4f} "
        f"{'train' if i < N_TRAIN else 'OOS':>6}"
    )

# best OOS in LEE (honesty)
by_oos = sorted(cands_B, key=lambda r: r[1])
info("top-5 Track-B by OOS (LEE surface):")
for tr, oos, th, sn, _, _ in by_oos[:5]:
    info(f"  OOS={oos:.4f} train={tr:.4f} θ={th:.4f} S={sn}")
best_oos_B_any = by_oos[0][1]

th_cm_grid = float(THETA_GRID[int(np.argmin(np.abs(THETA_GRID - theta_cm)))])
mu_B_cm = spectra_B[th_cm_grid]
oos_B_cm = (
    mean_rel(apply_map("S0", mu_B_cm)[N_TRAIN:N_TEST_END], TEST_G)
    if len(mu_B_cm) >= N_TEST_END
    else 1.0
)
info(f"published-like (θ_grid≈π/2, S0) OOS = {oos_B_cm:.4f}")

d_kin_B = apply_map(s_B, mu_B_kin) if len(mu_B_kin) >= N_TEST_END else np.zeros(1)
oos_kin_B = (
    mean_rel(d_kin_B[N_TRAIN:N_TEST_END], TEST_G)
    if len(d_kin_B) >= N_TEST_END
    else 1.0
)
gue_B = gue_spectrum_like(N_TEST_END, delta_B[:N_TEST_END])
oos_gue_B = mean_rel(gue_B[N_TRAIN:N_TEST_END], TEST_G)
sep_kin_B = oos_kin_B >= oos_B * (1.0 + K2_SEPARATION) or (oos_kin_B - oos_B > 0.05)
sep_gue_B = oos_gue_B >= oos_B * (1.0 + K2_SEPARATION) or (oos_gue_B - oos_B > 0.05)
info(
    f"null-B OOS: kinetic={oos_kin_B:.4f} (worse? {sep_kin_B}), "
    f"GUE={oos_gue_B:.4f} (worse? {sep_gue_B})"
)
check(
    f"Track-B OOS fact: rel={oos_B:.4f}, success={oos_B_success} "
    f"(requires K1-B), θ*={th_B:.4f}, S*={s_B}",
    True,
)
check(
    f"Track-B null facts: kin_sep={sep_kin_B}, GUE_sep={sep_gue_B}; "
    f"best_any_OOS={best_oos_B_any:.4f}",
    True,
)

# Λ=1 diagnostic on Track A published S0
mu_A_l1 = cm_neg_from_Atau(2.0 * math.pi * LAM_DIAG * LAM_DIAG, FEM_HI, N_NEG_KEEP)
oos_l1 = (
    mean_rel(apply_map("S0", mu_A_l1)[N_TRAIN:N_TEST_END], TEST_G)
    if len(mu_A_l1) >= N_TEST_END
    else 1.0
)
info(f"diagnostic Λ=1 Track-A S0 OOS mean rel = {oos_l1:.4f}")
check("Λ=1 diagnostic recorded (trend only)", True)

# ================================================================ S3
print()
print("=" * 72)
print("S3 -- R3 spacings (UNDERPOWERED); R4 OPEN")
print("=" * 72)
levels = delta_A[:16] if len(delta_A) >= 16 else delta_A
spac = unfold_spacings(levels)
ks_p = ks_distance(spac, gue_wigner_cdf) if len(spac) else 1.0
ks_po = ks_distance(RNG.exponential(1.0, size=max(len(spac), 1)), gue_wigner_cdf)
info(f"Track-A unfolded n={len(spac)}; KS(proto,GUE)={ks_p:.4f}; "
     f"KS(Poisson,GUE)={ks_po:.4f}")
check(
    f"R3 trend recorded: KS_proto={ks_p:.4f} vs KS_poisson_ctrl={ks_po:.4f}",
    True,
)
check("R4 typed OPEN at prototype level (no false closure)", True)

# ================================================================ S4
print()
print("=" * 72)
print("S4 -- synthesis / verdict")
print("=" * 72)

# Driving track selection (preregistered)
if k1a_ok and ramis_ok:
    driver = "A"
    k1_ok = True
    oos_success = oos_A_success
    sep_kin, sep_gue = sep_kin_A, sep_gue_A
    oos_rel = oos_A
elif k1b_ok:
    driver = "B"
    k1_ok = True
    oos_success = oos_B_success
    sep_kin, sep_gue = sep_kin_B, sep_gue_B
    oos_rel = oos_B
else:
    driver = "NONE"
    k1_ok = False
    oos_success = False
    sep_kin, sep_gue = False, False
    oos_rel = min(oos_A, oos_B)

info(f"driving track = {driver} (K1-A={k1a_ok}, K1-B={k1b_ok}, Ramis={ramis_ok})")

if not k1_ok:
    verdict = "IMPL-BLOCKED"
    reason = (
        "Both tracks numerically blocked on K1: Track A unexpectedly failed "
        f"(k1a={k1a_ok}, ramis={ramis_ok}); Track B exterior LCO truncation "
        f"did not converge (k1b={k1b_ok}, UV-soft={uv_ok})"
    )
elif oos_success and sep_kin and sep_gue:
    verdict = "UV-PROTOTYPE-MATCHES"
    reason = (
        f"Driving track {driver}: OOS mean rel={oos_rel:.4f} < 5% with null "
        "separation and mesh non-degradation"
    )
elif oos_success and not (sep_kin and sep_gue):
    verdict = "UV-NO-SIGNAL"
    reason = (
        f"Driving track {driver}: OOS threshold met (rel={oos_rel:.4f}) but "
        "nulls not separated — association not specific"
    )
else:
    verdict = "UV-NO-SIGNAL"
    reason = (
        f"Driving track {driver} K1-clear but no out-of-sample <5% Dirac↔γ "
        f"match under LEE={{S0,S1,S2}}"
        f" (A: S*={kind_A} OOS={oos_A:.4f}, published S0 OOS={oos_A_cm:.4f}; "
        f"B: θ*={th_B:.4f} S*={s_B} OOS={oos_B:.4f}, K1-B={k1b_ok}, "
        f"published-like OOS={oos_B_cm:.4f}).  "
        "CM published claim is UV asymptotic counting of 2D/ (and of "
        "negative W_sa), not a few-% low-n eigenvalue match; this "
        "prototype does not promote counting to pointwise γ-match.  "
        "Route rests as classical/external, numerically demanding on the "
        "direct exterior LCO side.  R4 open."
    )

info(f"VERDICT: {verdict}")
info(f"reason: {reason}")
info("Stage-4 map consequence:")
info("  T46: R1 via A_τ; IR F0 dead → pointed here (UV/Dirac).")
info(f"  T47: UV/Dirac pointwise under C6/C7 → {verdict}.")
info("  Selfduality class still R1-ok; R2 not closed at prototype level;")
info("  next lever: compiler-native Λ-scale / operator selection, OR treat")
info("  CM strictly as external UV-counting anchor (no few-% claim), OR")
info("  full even+odd ⊕ true ∞-oscillatory theory beyond FEM truncation.")
info("  TFPT link remains [O]-contract (selection principle only).")

check(
    f"verdict enum is UV-PROTOTYPE-MATCHES / IMPL-BLOCKED / UV-NO-SIGNAL "
    f"(got {verdict})",
    verdict in ("UV-PROTOTYPE-MATCHES", "IMPL-BLOCKED", "UV-NO-SIGNAL"),
)
check(
    f"computed fact: driver={driver}, K1A={k1a_ok}, K1B={k1b_ok}, "
    f"oos_A={oos_A:.4f}, oos_B={oos_B:.4f}, oos_success={oos_success}",
    True,
)
check(
    f"synthesis assigns {verdict} consistently with preregistered rules",
    (
        (verdict == "IMPL-BLOCKED" and not k1_ok)
        or (
            verdict == "UV-PROTOTYPE-MATCHES"
            and k1_ok
            and oos_success
            and sep_kin
            and sep_gue
        )
        or (
            verdict == "UV-NO-SIGNAL"
            and k1_ok
            and not (oos_success and sep_kin and sep_gue)
        )
    ),
)

# ================================================================ end
print()
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)", flush=True)
print(f"VERDICT: {verdict}", flush=True)
raise SystemExit(0 if FAIL == 0 else 1)
