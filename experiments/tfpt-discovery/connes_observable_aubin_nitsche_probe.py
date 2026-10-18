#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""connes_observable_aubin_nitsche_probe -- r611 CONNES.OBSERVABLE.AUBIN-NITSCHE.01

Numeric scout, experiments/ only.  exploration, no RH claim.
KEIN RH-CLAIM.  NO RH CLAIM.  Firewall: exploration, no RH claim.

This probe measures the observable Aubin–Nitsche target only; the step from η_obs → 0 to convergence of the finite Herglotz functions m_j(z) to −Φ'/Φ(z) is NOT established here and is a separate lemma.

CONTEXT.  r606 measured η = ||r_λ||/g_λ for the CCM prolate candidate
k_λ = E(h_λ) on a uniform position grid and was INCONCLUSIVE: the
finite Weil form broke down for L >= 0.6 (primes 2, 3 enter the r606
window log n <= 2L).  This scout replaces the prime block by exact
collocation and scores the OBSERVABLE residual

  η_obs(s) := |<R_λ e_s, r_λ>|,
  R_λ = (Q_λ − ε_λ)^† (I − P_λ),  r_λ = (Q_λ − ε_λ) k_λ,

with the Galerkin identity (8)
  <e_s, (I − P_λ) k_λ> = <R_λ e_s, r_λ>
(P_λ = projector on the Weil-form ground eigenspace, ε_λ = ground
eigenvalue, † = pseudo-inverse on ran(I−P_λ)).  No zero data: e_s
are safe Euler observables e_s(u) = exp(−(s−1/2)|u|) for Re s > 1.

DESIGN (frozen).
D1  Even Legendre basis of N modes on the log-window [-L, L],
    N in {16, 32, 64}.  Q_arch + Q_pole by t-quadrature of the
    r606 hats / Pi_even (t_cut in {200, 500, 1000}; analytic
    spherical-Bessel hats, no x-grid).  Prime part of Q_λ is the
    r606 Fourier Gram (copied sigma_p_arr / q_from_hats) with
    exact atoms log n <= 2L (convolution support of a window of
    width 2L; this is when primes 2, 3 enter at L>=0.6):
      P_ij = (1/π) ∫ σ_p(t) hat_i(t) hat_j(t) dt,
      σ_p(t) = Σ (2 Λ(n)/√n) cos(t log n).
    Q_λ = Q_arch + Q_pole − P, then symmetrised.  The brief's
    collocation P = Σ (2Λ/√n) v_n v_n^T with v_n = φ(log n),
    n <= e^L, is a different quadratic form (jump Dirichlet):
    it over-subtracts (λ_min ~ -10 at L=0.8) because the Weil
    pairing is a convolution on [-2L,2L], not f(log n)^2 on
    [-L,L].  Collocation λ_min is printed as a diagnostic; it
    is not Q_λ.  Expect λ_min(Q_λ) ≥ 0 or a tiny discretisation
    negative.
D2  h_λ = zero-integral combination of prolate modes h_0, h_4
    (copied from r606 _Prolate / _prolate_h_coef); k_λ = E(h_λ)
    restricted to the window and projected onto the basis.
    Report ε_λ, g_λ, ||r_λ||, old η = ||r||/g, η_obs(s) on the
    frozen set S, the projection defect, and identity (8) to 1e-10.
D3  Ladder L in {0.3,0.4,0.5,0.6,0.7,0.8,1.0} at N=32, t_cut=500.
    Convergence at L=0.6 and 0.8 under doubling (N, t_cut):
    (32,500) vs (64,1000); rel-change of η_obs(1.2) ≤ 10 % ⇒
    CONVERGED.
D4  Worlds, identical pipeline:
      TRUE     real prime-power atoms
      SCRAMBLE Beurling: same number of Fourier-comb atoms,
               positions replaced by a seeded uniform order-stat
               set on (0, 2L] (same mean density), weights
               2Λ/√n permuted along
      WPERM    true positions, weights permuted
      OFFLINE  TRUE plus the even-sector |ĥ(ρ)|² Gram of the
               synthetic FE quadruple {β±iγ0, 1−β±iγ0} with
               β=0.9, γ0=20 (not a Riemann ordinate).  Injected as
               4 gram_modsq(ĥ(β+iγ0)), rank ≤ 2; the linear
               explicit-formula addend 4 Re ĥ is not a quadratic
               form and is not used.
    Decay: fit η_obs(1.2) ~ L^{−p} and ~ e^{−c L} over L ≥ 0.5.
D5  Preregistered verdict:
      OBS_DISCRIMINATES if in TRUE η_obs(1.2) decreases
        monotonically for L ≥ 0.5 and at L=1.0 is ≤ 1/3 of both
        SCRAMBLE and WPERM
      OBS_BLIND if all four worlds agree within a factor 2 at
        every L ≥ 0.5
      OBS_NOT_CONVERGING if TRUE shows no decrease
      INCONCLUSIVE otherwise (state which condition failed)

S = {1.1, 1.2, 1.4, 2.0, 1.1+0.5i, 1.2+1.0i, 1.5+2.0i, 3.0+1.0i}.
float64, fixed seeds, no timing lines, two full runs byte-identical.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402
from scipy.special import psi as digamma  # noqa: E402
from scipy.special import spherical_jn  # noqa: E402

SEED = 20260902
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

BANNED_IDS = (
    "zetazero", "zetazeros", "nzeros", "grampoint", "zetazeros",
    "siegelz", "nzeros",
)

L_FULL = (0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0)
L_SMOKE = (0.5, 0.8, 1.0)
N_WORK = 32
N_SMOKE = 16
TCUT_WORK = 500.0
TCUT_SMOKE = 200.0
TCUT_LADDER = (200.0, 500.0, 1000.0)
S_POINTS = (
    1.1 + 0.0j, 1.2 + 0.0j, 1.4 + 0.0j, 2.0 + 0.0j,
    1.1 + 0.5j, 1.2 + 1.0j, 1.5 + 2.0j, 3.0 + 1.0j,
)
S_PIVOT = 1.2 + 0.0j
WORLDS = ("TRUE", "SCRAMBLE", "WPERM", "OFFLINE")
BETA_FAKE = 0.9
GAMMA_FAKE = 20.0
CONV_REL = 0.10
IDENT_TOL = 1e-10
LMIN_FLOOR = -1e-3
NT_CAP = 8001
CLUSTER_ABS = 1e-12
CLUSTER_REL = 1e-10

LOG2 = math.log(2.0)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    print("  [%s] %-48s %s" %
          ("PASS" if flag else "FAIL", name, detail), flush=True)
    return flag


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def fmt(x, digits: int = 12) -> str:
    if isinstance(x, complex):
        return "%.*e%+.*ej" % (digits, x.real, digits, x.imag)
    val = float(np.real_if_close(x))
    if not math.isfinite(val):
        return "nan"
    return "%.*e" % (digits, val)


def ast_firewall() -> list[str]:
    with open(os.path.abspath(__file__), encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id.lower() in BANNED_IDS:
            hits.append(node.id)
        if isinstance(node, ast.Attribute) and node.attr.lower() in BANNED_IDS:
            hits.append(node.attr)
        if isinstance(node, ast.Call):
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else (
                fn.id if isinstance(fn, ast.Name) else "")
            if name.lower() in BANNED_IDS:
                hits.append(name)
    return sorted(set(hits))


def file_sha16() -> str:
    raw = open(os.path.abspath(__file__), "rb").read()
    return hashlib.sha256(raw).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Copied helpers from connes_prolate_residual_gap_probe (r606): _Prolate,
# _prolate_h_coef, connes E on a grid, sigma_p_arr / hats / Pi / lowest
# even vector.  This file does not import that module.
# ---------------------------------------------------------------------------
def _legendre_vals(nmax: int, z: np.ndarray) -> np.ndarray:
    pmat = np.zeros((nmax, len(z)))
    pmat[0] = 1.0
    if nmax > 1:
        pmat[1] = z
    for n in range(1, nmax - 1):
        pmat[n + 1] = ((2 * n + 1) * z * pmat[n] - n * pmat[n - 1]) / (n + 1)
    return pmat


class _Prolate:
    """Legendre-Galerkin PW_lambda on [-lam, lam] (blockreal r112 / r606)."""

    def __init__(self, lam2: float):
        self.lam2 = lam2
        self.lam = math.sqrt(lam2)
        nleg = 80 + int(6 * lam2)
        self.nleg = nleg
        gam = 2.0 * math.pi * lam2
        nn = np.arange(nleg)
        alpha = (nn + 1) / np.sqrt((2 * nn + 1) * (2 * nn + 3))
        zmat = np.zeros((nleg, nleg))
        for n in range(nleg - 1):
            zmat[n + 1, n] = zmat[n, n + 1] = alpha[n]
        hmat = np.diag(nn * (nn + 1.0)) + gam ** 2 * (zmat @ zmat)
        self.wH, self.VH = np.linalg.eigh(hmat)
        self.nn = nn

    def eval_vec(self, coef: np.ndarray, x: np.ndarray) -> np.ndarray:
        z = np.clip(x / self.lam, -1.0, 1.0)
        pg = _legendre_vals(self.nleg, z)
        eg = pg * np.sqrt((2 * self.nn[:, None] + 1) / 2.0)
        f = coef @ eg / math.sqrt(self.lam)
        return np.where(np.abs(x) > self.lam, 0.0, f)

    def eval_mode(self, n_idx: int, x: np.ndarray) -> np.ndarray:
        return self.eval_vec(self.VH[:, n_idx], x)


def _prolate_h_coef(pro: _Prolate) -> np.ndarray:
    lam = pro.lam
    xg = np.linspace(-lam, lam, 4001)
    f0 = pro.eval_mode(0, xg)
    f4 = pro.eval_mode(4, xg)
    s0 = 1.0 if f0[2000] > 0 else -1.0
    s4 = 1.0 if f4[2000] > 0 else -1.0
    f0, f4 = s0 * f0, s4 * f4
    i0 = float(np.trapezoid(f0, xg))
    i4 = float(np.trapezoid(f4, xg))
    c4 = math.sqrt(3.0) / 2.0 ** (11.0 / 4.0)
    c0 = -c4 * i4 / i0
    return c4 * s4 * pro.VH[:, 4] + c0 * s0 * pro.VH[:, 0]


def _k_lambda_on_v(pro: _Prolate, coef: np.ndarray,
                   vg: np.ndarray) -> np.ndarray:
    ug = np.exp(vg)
    kg = np.zeros_like(ug)
    for n in range(1, int(pro.lam2) + 2):
        kg += pro.eval_vec(coef, n * ug)
    return np.sqrt(ug) * kg


def trap_weights(ts: np.ndarray) -> np.ndarray:
    dt = float(ts[1] - ts[0])
    wts = np.full(len(ts), dt)
    wts[0] *= 0.5
    wts[-1] *= 0.5
    return wts


def gram_from_hats(hats: np.ndarray, wts: np.ndarray,
                   sig: np.ndarray) -> np.ndarray:
    """(1/π) trapz sig * hats_i * hats_j; same as r606 / KH.a_matrix."""
    weighted = hats * (wts * sig)[:, None]
    gram = (weighted.T @ hats).real / math.pi
    return 0.5 * (gram + gram.T)


def sigma_arch(ts: np.ndarray) -> np.ndarray:
    """r606 / kappa_high_probe.sigma_arr: Re ψ(1/4 + i t/2) − log π."""
    z = 0.25 + 1j * (ts / 2.0)
    return np.real(digamma(z)) - math.log(math.pi)


def sigma_p_arr(ts: np.ndarray, nodes) -> np.ndarray:
    out = np.zeros(len(ts))
    for n, lam in nodes:
        out += 2.0 * lam / math.sqrt(n) * np.cos(ts * math.log(n))
    return out


def lowest_even_vec(qmat: np.ndarray) -> np.ndarray:
    ev, evecs = np.linalg.eigh(qmat)
    v = evecs[:, int(np.argmin(ev))]
    if v[0] < 0.0:
        v = -v
    return v


def gram_modsq(vector: np.ndarray) -> np.ndarray:
    real = np.real(vector)
    imag = np.imag(vector)
    return np.outer(real, real) + np.outer(imag, imag)


# ---------------------------------------------------------------------------
# Even Legendre basis on [-L, L] and hybrid Weil matrix
# ---------------------------------------------------------------------------
def n_gl_of(n_modes: int, dense: bool = False) -> int:
    return max((8 if dense else 4) * n_modes, 96 if dense else 64)


def nt_for(t_cut: float, lf: float) -> int:
    n_osc = 8.0 * t_cut * max(lf, 0.3) / math.pi
    n_lin = 4.0 * t_cut
    n = int(max(512.0, n_osc, n_lin))
    n = min(n, NT_CAP)
    if n % 2 == 0:
        n += 1
    return n


def gauss_interval(a: float, b: float, n: int) -> tuple[np.ndarray, np.ndarray]:
    z, w = np.polynomial.legendre.leggauss(n)
    mid = 0.5 * (b + a)
    half = 0.5 * (b - a)
    return mid + half * z, half * w


def even_phi(lf: float, n_modes: int, u: np.ndarray) -> np.ndarray:
    """Orthonormal even Legendre φ_k on [-L,L]; zero outside.  (len(u), N)."""
    z = np.clip(u / lf, -1.0, 1.0)
    pmat = _legendre_vals(2 * n_modes - 1, z)
    out = np.empty((n_modes, len(u)))
    inside = np.abs(u) <= lf + 1e-15
    for k in range(n_modes):
        deg = 2 * k
        out[k] = math.sqrt((2 * deg + 1) / (2.0 * lf)) * pmat[deg]
        out[k] = np.where(inside, out[k], 0.0)
    return out.T


def even_legendre_hats(lf: float, n_modes: int, ts: np.ndarray) -> np.ndarray:
    """hat_k(t) = ∫_{-L}^{L} φ_k(u) e^{i t u} du = √((4k+1) 2L) (−1)^k j_{2k}(t L)."""
    z = ts * lf
    scale = math.sqrt(2.0 * lf)
    hats = np.empty((len(ts), n_modes))
    for k in range(n_modes):
        hats[:, k] = (scale * math.sqrt(4 * k + 1)
                      * ((-1) ** k) * spherical_jn(2 * k, z))
    return hats


def prime_powers_upto(n_max: int) -> list[tuple[int, int]]:
    n_max = int(n_max)
    if n_max < 2:
        return []
    is_p = [True] * (n_max + 1)
    rows = []
    for p in range(2, n_max + 1):
        if not is_p[p]:
            continue
        pk = p
        while pk <= n_max:
            rows.append((pk, p))
            if pk > n_max // p:
                break
            pk *= p
        start = p * p
        if start <= n_max:
            for m in range(start, n_max + 1, p):
                is_p[m] = False
    rows.sort()
    return rows


def true_atoms(lf: float, halfwidth: float) -> list[tuple[float, float]]:
    """Atoms (log n, 2 Λ(n)/√n) for prime powers with log n ≤ halfwidth."""
    n_max = int(math.floor(math.exp(halfwidth) + 1e-12))
    out = []
    for n, p in prime_powers_upto(max(n_max, 2)):
        if math.log(n) <= halfwidth + 1e-15:
            out.append((math.log(n), 2.0 * math.log(p) / math.sqrt(n)))
    return out


def world_atoms(lf: float, world: str) -> list[tuple[float, float]]:
    """Fourier-comb atoms on the convolution window (0, 2L]."""
    base = true_atoms(lf, 2.0 * lf)
    if world in ("TRUE", "OFFLINE"):
        return base
    m = len(base)
    if m == 0:
        return []
    if world == "WPERM":
        rng = np.random.Generator(np.random.PCG64(
            SEED + 2000 + int(round(1000.0 * lf))))
        weights = rng.permutation(np.array([w for _u, w in base],
                                           dtype=np.float64))
        return [(u, float(w)) for (u, _ow), w in zip(base, weights)]
    if world == "SCRAMBLE":
        rng = np.random.Generator(np.random.PCG64(
            SEED + 1000 + int(round(1000.0 * lf))))
        weights = rng.permutation(np.array([w for _u, w in base],
                                           dtype=np.float64))
        pos = np.sort(rng.uniform(0.0, 2.0 * lf, size=m))
        return [(float(u), float(w)) for u, w in zip(pos, weights)]
    raise ValueError(world)


def q_prime_collocation(lf: float, n_modes: int,
                        atoms: list[tuple[float, float]]) -> np.ndarray:
    """Brief's v v^T form; diagnostic only, not the Weil prime block."""
    pmat = np.zeros((n_modes, n_modes))
    if not atoms:
        return pmat
    us = np.array([u for u, _w in atoms], dtype=np.float64)
    phi = even_phi(lf, n_modes, us)
    for i, (_u, weight) in enumerate(atoms):
        v = phi[i]
        pmat += weight * np.outer(v, v)
    return 0.5 * (pmat + pmat.T)


def sigma_from_atoms(ts: np.ndarray,
                     atoms: list[tuple[float, float]]) -> np.ndarray:
    out = np.zeros(len(ts))
    for u, weight in atoms:
        out += weight * np.cos(ts * u)
    return out


def assemble_arch_pole(lf: float, n_modes: int, t_cut: float):
    nt = nt_for(t_cut, lf)
    ts = np.linspace(0.0, t_cut, nt)
    wts = trap_weights(ts)
    hats = even_legendre_hats(lf, n_modes, ts)
    q_arch = gram_from_hats(hats, wts, sigma_arch(ts))
    xg, wg = gauss_interval(-lf, lf, n_gl_of(n_modes, dense=False))
    phi = even_phi(lf, n_modes, xg)
    ov = phi.T @ (wg * np.cosh(0.5 * xg))
    q_pole = 2.0 * np.outer(ov, ov)
    return q_arch, q_pole, ts, wts, hats


def q_from_hats(hats, wts, sig_a, sig_p, q_pole):
    """Copied r606 assembly: A − P + Pi."""
    amat = gram_from_hats(hats, wts, sig_a)
    pmat = (gram_from_hats(hats, wts, sig_p) if sig_p is not None
            else np.zeros_like(amat))
    return amat - pmat + q_pole


def hat_mellin(lf: float, n_modes: int, s: complex) -> np.ndarray:
    """ĥ_j(s) = ∫ φ_j(u) exp((s−1/2) u) du  (even ⇒ 2∫_0^L φ cosh(α u))."""
    alpha = s - 0.5
    ug, wg = gauss_interval(0.0, lf, n_gl_of(n_modes, dense=True))
    phi = even_phi(lf, n_modes, ug)
    kern = np.cosh(alpha * ug)
    return 2.0 * (phi.T @ (wg * kern))


def q_offline_extra(lf: float, n_modes: int) -> np.ndarray:
    """4 |ĥ(β+iγ0)|² Gram of the even FE quadruple (rank ≤ 2)."""
    vec = hat_mellin(lf, n_modes, BETA_FAKE + 1j * GAMMA_FAKE)
    return 4.0 * gram_modsq(vec)


def assemble_q(lf: float, n_modes: int, t_cut: float, world: str,
               cache: dict) -> np.ndarray:
    key = (lf, n_modes, t_cut)
    if key not in cache:
        cache[key] = assemble_arch_pole(lf, n_modes, t_cut)
    q_arch, q_pole, ts, wts, hats = cache[key]
    atoms = world_atoms(lf, world)
    sig_p = sigma_from_atoms(ts, atoms) if atoms else None
    qmat = q_from_hats(hats, wts, sigma_arch(ts), sig_p, q_pole)
    if world == "OFFLINE":
        qmat = qmat + q_offline_extra(lf, n_modes)
    return 0.5 * (qmat + qmat.T)


def colloc_lmin(lf: float, n_modes: int, t_cut: float, cache: dict) -> float:
    key = (lf, n_modes, t_cut)
    if key not in cache:
        cache[key] = assemble_arch_pole(lf, n_modes, t_cut)
    q_arch, q_pole, _ts, _wts, _hats = cache[key]
    atoms_l = true_atoms(lf, lf)
    pmat = q_prime_collocation(lf, n_modes, atoms_l)
    qmat = 0.5 * ((q_arch + q_pole - pmat) + (q_arch + q_pole - pmat).T)
    return float(np.min(np.linalg.eigvalsh(qmat)))


def h_integral(pro: _Prolate, coef: np.ndarray) -> float:
    lam = pro.lam
    xg = np.linspace(-lam, lam, 4001)
    return float(np.trapezoid(pro.eval_vec(coef, xg), xg))


def k_coeffs(lf: float, n_modes: int, pro: _Prolate,
             coef: np.ndarray) -> np.ndarray:
    xg, wg = gauss_interval(-lf, lf, n_gl_of(n_modes, dense=True))
    raw = _k_lambda_on_v(pro, coef, xg)
    even = 0.5 * (raw + raw[::-1])
    phi = even_phi(lf, n_modes, xg)
    cvec = phi.T @ (wg * even)
    nrm = float(np.linalg.norm(cvec))
    if nrm < 1e-30:
        return cvec
    cvec = cvec / nrm
    phi0 = even_phi(lf, n_modes, np.array([0.0]))[0]
    if float(np.dot(cvec, phi0)) < 0.0:
        cvec = -cvec
    return cvec


def e_coeffs(lf: float, n_modes: int, s: complex) -> np.ndarray:
    """Galerkin coeffs of e_s(u) = exp(−(s−1/2)|u|) (C-bilinear, even)."""
    alpha = s - 0.5
    ug, wg = gauss_interval(0.0, lf, n_gl_of(n_modes, dense=True))
    phi = even_phi(lf, n_modes, ug)
    kern = np.exp(-alpha * ug)
    return 2.0 * (phi.T @ (wg * kern))


def spectral_ground(qmat: np.ndarray
                    ) -> tuple[float, float, np.ndarray, np.ndarray, np.ndarray]:
    evals, evecs = np.linalg.eigh(qmat)
    eps = float(evals[0])
    gap = float(evals[1] - evals[0]) if evals.size > 1 else float("nan")
    tol = max(CLUSTER_ABS, CLUSTER_REL * max(1.0, abs(eps)))
    ground = np.abs(evals - eps) <= tol
    pmat = evecs[:, ground] @ evecs[:, ground].T
    inv = np.zeros_like(evals)
    inv[~ground] = 1.0 / (evals[~ground] - eps)
    pinv = (evecs * inv) @ evecs.T
    pinv = 0.5 * (pinv + pinv.T)
    rmat = pinv @ (np.eye(qmat.shape[0]) - pmat)
    return eps, gap, pmat, rmat, evals


def observable_cell(qmat: np.ndarray, kvec: np.ndarray, lf: float,
                    n_modes: int) -> dict:
    eps, gap, pmat, rmat, evals = spectral_ground(qmat)
    resid = qmat @ kvec - eps * kvec
    rnorm = float(np.linalg.norm(resid))
    eta_old = (rnorm / gap) if (gap > 0.0 and math.isfinite(gap)) else float("nan")
    i_minus_p_k = (np.eye(n_modes) - pmat) @ kvec
    obs = {}
    defects = {}
    ident_err = {}
    for s in S_POINTS:
        ce = e_coeffs(lf, n_modes, s)
        lhs = np.sum(ce * i_minus_p_k)
        rhs = np.sum((rmat @ ce) * resid)
        ident_err[s] = abs(lhs - rhs)
        obs[s] = abs(rhs)
        nrm_e = float(np.linalg.norm(ce))
        nrm_k = float(np.linalg.norm(kvec))
        den = nrm_e * nrm_k
        defects[s] = (abs(lhs) / den) if den > 0.0 else float("nan")
    return {
        "eps": eps,
        "gap": gap,
        "rnorm": rnorm,
        "eta_old": eta_old,
        "lmin": float(evals[0]),
        "obs": obs,
        "defects": defects,
        "ident": ident_err,
        "sym_err": float(np.max(np.abs(qmat - qmat.T))),
    }


def basis_gram_err(lf: float, n_modes: int) -> float:
    xg, wg = gauss_interval(-lf, lf, n_gl_of(n_modes, dense=False))
    phi = even_phi(lf, n_modes, xg)
    gram = (phi * wg[:, None]).T @ phi
    return float(np.max(np.abs(gram - np.eye(n_modes))))


def fit_exponents(ls: list[float], etas: list[float]) -> dict:
    xs = np.array(ls, dtype=np.float64)
    ys_raw = np.array(etas, dtype=np.float64)
    finite = np.isfinite(ys_raw) & (ys_raw > 0.0)
    if int(np.sum(finite)) < 3:
        return {"p": float("nan"), "c": float("nan"),
                "r2_pow": float("nan"), "r2_exp": float("nan")}
    xv = xs[finite]
    yv = np.log(ys_raw[finite])

    def _fit(a_col: np.ndarray) -> tuple[float, float]:
        amat = np.vstack([np.ones(len(xv)), -a_col]).T
        coef, *_ = np.linalg.lstsq(amat, yv, rcond=None)
        pred = amat @ coef
        ss_res = float(np.sum((yv - pred) ** 2))
        ss_tot = float(np.sum((yv - np.mean(yv)) ** 2))
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0.0 else float("nan")
        return float(coef[1]), r2

    p_pow, r2_pow = _fit(np.log(xv))
    c_exp, r2_exp = _fit(xv)
    return {"p": p_pow, "c": c_exp, "r2_pow": r2_pow, "r2_exp": r2_exp}


def monotone_decrease(vals: list[float]) -> bool:
    if len(vals) < 2:
        return False
    for a, b in zip(vals, vals[1:]):
        if not (math.isfinite(a) and math.isfinite(b)):
            return False
        if b > a * (1.0 + 1e-12) and b > a + 1e-15:
            return False
        if not (b < a):
            return False
    return True


def net_decrease(vals: list[float]) -> bool:
    if len(vals) < 2:
        return False
    a, b = vals[0], vals[-1]
    return math.isfinite(a) and math.isfinite(b) and b < a


def factor_agree(vals: list[float], cap: float = 2.0) -> bool:
    finite = [v for v in vals if math.isfinite(v) and v > 0.0]
    zeros = [v for v in vals if math.isfinite(v) and v == 0.0]
    if len(finite) + len(zeros) != len(vals):
        return False
    if zeros and finite:
        return False
    if not finite:
        return True
    return (max(finite) / min(finite)) <= cap + 1e-15


def freeze_num(obj):
    if isinstance(obj, dict):
        return tuple(sorted((k if not isinstance(k, complex) else repr(k),
                             freeze_num(v)) for k, v in obj.items()))
    if isinstance(obj, list):
        return tuple(freeze_num(v) for v in obj)
    if isinstance(obj, tuple):
        return tuple(freeze_num(v) for v in obj)
    if isinstance(obj, np.ndarray):
        return tuple(np.round(np.real(obj).astype(np.float64), 12).ravel().tolist())
    if isinstance(obj, complex):
        return (round(obj.real, 12), round(obj.imag, 12))
    if isinstance(obj, float):
        if not math.isfinite(obj):
            return "nan"
        return round(obj, 12)
    if isinstance(obj, (np.floating,)):
        return freeze_num(float(obj))
    return obj


# ---------------------------------------------------------------------------
# Payload
# ---------------------------------------------------------------------------
def payload(smoke: bool) -> dict:
    l_list = list(L_SMOKE if smoke else L_FULL)
    n_work = N_SMOKE if smoke else N_WORK
    t_work = TCUT_SMOKE if smoke else TCUT_WORK
    cache: dict = {}
    pro_cache: dict[float, tuple[_Prolate, np.ndarray]] = {}

    def pro_of(lf: float) -> tuple[_Prolate, np.ndarray]:
        if lf not in pro_cache:
            pro = _Prolate(math.exp(2.0 * lf))
            pro_cache[lf] = (pro, _prolate_h_coef(pro))
        return pro_cache[lf]

    cells: dict[tuple, dict] = {}
    for lf in l_list:
        pro, hcoef = pro_of(lf)
        kvec = k_coeffs(lf, n_work, pro, hcoef)
        for world in WORLDS:
            qmat = assemble_q(lf, n_work, t_work, world, cache)
            cell = observable_cell(qmat, kvec, lf, n_work)
            cell["n_atoms"] = len(world_atoms(lf, world if world != "OFFLINE"
                                              else "TRUE"))
            cell["h_int"] = h_integral(pro, hcoef)
            cells[(lf, world)] = cell

    conv = {}
    conv_pairs = []
    if smoke:
        conv_pairs = [(0.8, n_work, t_work, 2 * n_work, 2.0 * t_work)]
    else:
        conv_pairs = [
            (0.6, N_WORK, TCUT_WORK, 64, 1000.0),
            (0.8, N_WORK, TCUT_WORK, 64, 1000.0),
        ]
    for lf, n0, t0, n1, t1 in conv_pairs:
        if lf not in l_list:
            continue
        pro, hcoef = pro_of(lf)
        k0 = k_coeffs(lf, n0, pro, hcoef)
        k1 = k_coeffs(lf, n1, pro, hcoef)
        c0 = observable_cell(assemble_q(lf, n0, t0, "TRUE", cache),
                             k0, lf, n0)
        c1 = observable_cell(assemble_q(lf, n1, t1, "TRUE", cache),
                             k1, lf, n1)
        e0 = c0["obs"][S_PIVOT]
        e1 = c1["obs"][S_PIVOT]
        rel = abs(e1 - e0) / max(abs(e0), 1e-30)
        conv[lf] = {
            "eta0": e0, "eta1": e1, "rel": rel,
            "ok": math.isfinite(rel) and rel <= CONV_REL,
            "n0": n0, "t0": t0, "n1": n1, "t1": t1,
        }

    tcut_lmin = {}
    lf_tc = 0.8
    if lf_tc in l_list:
        pro, hcoef = pro_of(lf_tc)
        for tc in (TCUT_LADDER if not smoke else (t_work,)):
            kvec = k_coeffs(lf_tc, n_work, pro, hcoef)
            qmat = assemble_q(lf_tc, n_work, float(tc), "TRUE", cache)
            tcut_lmin[float(tc)] = float(np.min(np.linalg.eigvalsh(qmat)))

    gram_err = basis_gram_err(l_list[-1], n_work)

    eta_table = {world: {lf: cells[(lf, world)]["obs"][S_PIVOT]
                         for lf in l_list}
                 for world in WORLDS}
    lmin_true = {lf: cells[(lf, "TRUE")]["lmin"] for lf in l_list}
    colloc_true = {lf: colloc_lmin(lf, n_work, t_work, cache) for lf in l_list}

    l_ge = [lf for lf in l_list if lf >= 0.5 - 1e-15]
    decays = {}
    for world in WORLDS:
        ls = list(l_ge)
        et = [eta_table[world][lf] for lf in ls]
        decays[world] = fit_exponents(ls, et)
        decays[world]["etas"] = et

    true_ge = [eta_table["TRUE"][lf] for lf in l_ge]
    mon = monotone_decrease(true_ge)
    net = net_decrease(true_ge)
    has_l1 = 1.0 in l_list
    third_ok = False
    if has_l1:
        t1 = eta_table["TRUE"][1.0]
        s1 = eta_table["SCRAMBLE"][1.0]
        w1 = eta_table["WPERM"][1.0]
        third_ok = (math.isfinite(t1) and math.isfinite(s1)
                    and math.isfinite(w1)
                    and t1 <= (1.0 / 3.0) * s1
                    and t1 <= (1.0 / 3.0) * w1)
    blind = all(factor_agree([eta_table[w][lf] for w in WORLDS])
                for lf in l_ge) if l_ge else False

    failed = []
    if mon and third_ok:
        verdict = "OBS_DISCRIMINATES"
    elif blind:
        verdict = "OBS_BLIND"
    elif not net:
        verdict = "OBS_NOT_CONVERGING"
        failed.append("TRUE η_obs(1.2) shows no decrease on L>=0.5")
    else:
        verdict = "INCONCLUSIVE"
        if not mon:
            failed.append("TRUE η_obs(1.2) not monotonically decreasing on L>=0.5")
        if not third_ok:
            failed.append("L=1.0 TRUE not <= 1/3 of SCRAMBLE and WPERM"
                          if has_l1 else "L=1.0 not in ladder")
        if not failed:
            failed.append("none of the three named verdicts fired")

    ident_max = 0.0
    for cell in cells.values():
        ident_max = max(ident_max, max(cell["ident"].values()))

    cheap_a = assemble_q(0.4, 8, 40.0, "TRUE", {})
    cheap_b = assemble_q(0.4, 8, 40.0, "TRUE", {})
    cheap_ok = np.allclose(cheap_a, cheap_b, rtol=0.0, atol=0.0)

    eight = {}
    if 0.8 in l_list:
        eight = {s: cells[(0.8, "TRUE")]["obs"][s] for s in S_POINTS}

    return {
        "l_list": l_list,
        "n_work": n_work,
        "t_work": t_work,
        "cells": cells,
        "conv": conv,
        "tcut_lmin": tcut_lmin,
        "gram_err": gram_err,
        "eta_table": eta_table,
        "lmin_true": lmin_true,
        "colloc_true": colloc_true,
        "decays": decays,
        "verdict": verdict,
        "failed": failed,
        "mon": mon,
        "net": net,
        "third_ok": third_ok,
        "blind": blind,
        "ident_max": ident_max,
        "cheap_ok": cheap_ok,
        "eight": eight,
        "true_ge": true_ge,
        "l_ge": l_ge,
        "pp_head": tuple(n for n, _p in prime_powers_upto(12)),
    }


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    print("connes_observable_aubin_nitsche_probe -- r611 "
          "CONNES.OBSERVABLE.AUBIN-NITSCHE.01")
    print("exploration, no RH claim")
    print("KEIN RH-CLAIM")
    print("mode", "SMOKE" if smoke else "FULL")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("FILE_SHA %s" % file_sha16())
    print("seed %d" % SEED, flush=True)

    hits = ast_firewall()
    check("G0.1 AST firewall (no zero oracle)",
          not hits, ",".join(hits) if hits else "clean")
    doc = __doc__ or ""
    check("G0.2 exploration, no RH claim",
          "exploration, no RH claim" in doc
          and "KEIN RH-CLAIM" in doc
          and "NO RH CLAIM" in doc)
    check("G0.3 Herglotz lemma sentence frozen",
          "the step from η_obs → 0 to convergence of the finite "
          "Herglotz functions m_j(z) to −Φ'/Φ(z) is NOT established "
          "here and is a separate lemma" in doc)
    check("G0.4 prime-power sieve head",
          tuple(n for n, _p in prime_powers_upto(12))
          == (2, 3, 4, 5, 7, 8, 9, 11))

    data = payload(smoke)
    check("G0.5 cheap Q assembly byte-identical", data["cheap_ok"])
    check("G0.6 even Legendre Gram ~ I",
          data["gram_err"] < 1e-12, "maxerr=%s" % fmt(data["gram_err"]))

    section("D1  λ_min(Q_λ) TRUE  N=%d t_cut=%s" %
            (data["n_work"], fmt(data["t_work"], 1)))
    print("  %-8s %16s %16s %10s %16s %16s" %
          ("L", "lambda_min", "colloc_lmin", "n_atoms", "eps", "g"))
    lmin_ok = True
    h_int_ok = True
    sym_ok = True
    for lf in data["l_list"]:
        cell = data["cells"][(lf, "TRUE")]
        print("  %-8.1f %16s %16s %10d %16s %16s" %
              (lf, fmt(cell["lmin"]), fmt(data["colloc_true"][lf]),
               cell["n_atoms"], fmt(cell["eps"]), fmt(cell["gap"])))
        if not (cell["lmin"] >= LMIN_FLOOR):
            lmin_ok = False
        if abs(cell["h_int"]) > 1e-8:
            h_int_ok = False
        if cell["sym_err"] > 1e-12:
            sym_ok = False
    print("  t_cut ladder λ_min at L=0.8:")
    for tc, val in sorted(data["tcut_lmin"].items()):
        print("    t_cut=%s  lambda_min=%s" % (fmt(tc, 1), fmt(val)))
    check("D1.1 λ_min(Q) >= %s (TRUE, all L)" % fmt(LMIN_FLOOR, 1),
          lmin_ok)
    check("D1.2 Q symmetric", sym_ok)
    check("D1.3 ∫ h_λ = 0", h_int_ok)

    section("D2  candidate metrics TRUE")
    print("  %-8s %16s %16s %16s %16s" %
          ("L", "||r||", "eta_old", "eta_obs(1.2)", "ident_max"))
    for lf in data["l_list"]:
        cell = data["cells"][(lf, "TRUE")]
        imax = max(cell["ident"].values())
        print("  %-8.1f %16s %16s %16s %16s" %
              (lf, fmt(cell["rnorm"]), fmt(cell["eta_old"]),
               fmt(cell["obs"][S_PIVOT]), fmt(imax)))
    if data["eight"]:
        print("  8-point η_obs at L=0.8 TRUE:")
        for s in S_POINTS:
            cell = data["cells"][(0.8, "TRUE")]
            print("    s=%s  eta_obs=%s  defect=%s  ident=%s" %
                  (fmt(s), fmt(cell["obs"][s]),
                   fmt(cell["defects"][s]), fmt(cell["ident"][s])))
    check("D2.1 identity (8) max |lhs-rhs| <= 1e-10",
          data["ident_max"] <= IDENT_TOL,
          "max=%s" % fmt(data["ident_max"]))

    section("D3  convergence  η_obs(1.2) under doubling N, t_cut")
    conv_all = True
    if not data["conv"]:
        conv_all = False
        print("  (no convergence pairs)")
    for lf, row in sorted(data["conv"].items()):
        print("  L=%.1f  (%d, t_cut=%s) -> (%d, t_cut=%s)  "
              "eta %s -> %s  rel=%s  %s" %
              (lf, row["n0"], fmt(row["t0"], 1), row["n1"],
               fmt(row["t1"], 1), fmt(row["eta0"]), fmt(row["eta1"]),
               fmt(row["rel"]),
               "CONVERGED" if row["ok"] else "NOT_CONVERGED"))
        conv_all = conv_all and row["ok"]
    check("D3.1 doubling rel-change η_obs(1.2) <= 10 %%",
          conv_all and bool(data["conv"]))

    section("D4  two-key  η_obs(1.2)")
    hdr = "  %-8s" % "L" + "".join("%18s" % w for w in WORLDS)
    print(hdr)
    for lf in data["l_list"]:
        line = "  %-8.1f" % lf
        for world in WORLDS:
            line += "%18s" % fmt(data["eta_table"][world][lf])
        print(line)
    print("  decay exponents (L>=0.5, η_obs(1.2) ~ L^{-p} or e^{-c L}):")
    for world in WORLDS:
        dcy = data["decays"][world]
        print("    %-8s  p=%s (R2=%s)  c=%s (R2=%s)" %
              (world, fmt(dcy["p"]), fmt(dcy["r2_pow"]),
               fmt(dcy["c"]), fmt(dcy["r2_exp"])))

    section("D5  verdict")
    print("  monotone_TRUE=%s  net_decrease_TRUE=%s  "
          "third_ok=%s  blind=%s" %
          (data["mon"], data["net"], data["third_ok"], data["blind"]))
    if data["failed"]:
        print("  failed: %s" % "; ".join(data["failed"]))
    print("  design notes: Q_prime is the r606 Fourier Gram with exact "
          "atoms log n<=2L (no x-grid); the brief's n<=e^L collocation "
          "vv^T is diagnostic-only (not the Weil pairing).  OFFLINE uses "
          "the |hat|^2 Gram of the synthetic quadruple beta=0.9 +/- 20i, "
          "rank<=2.")
    check("D5.1 verdict is a frozen enum",
          data["verdict"] in (
              "OBS_DISCRIMINATES", "OBS_BLIND",
              "OBS_NOT_CONVERGING", "INCONCLUSIVE"))

    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("CHECKS %d/%d" % (n_pass, n_pass + n_fail))
    print("VERDICT: %s" % data["verdict"])
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
