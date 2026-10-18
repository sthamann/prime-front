#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""iiks_vanishing_metric_probe -- r625b  PRIME.IIKS.VANISHING.METRIC.01

Experiments-only scout of Zhou's vanishing-lemma metric for the discrete
2x2 IIKS jump of the wall kernel.  Copied (not imported) constructions:
v563 window/comb/arch (von_mangoldt_table, arch_lags, atom_lags_at,
frame-A geometry), v881/PIK (grid_density, lambda_eps, folded_measure,
lanczos_chain, eval_chain), tau_symbolic / v955 (CD generators
F = sqrt(v) p_h, G = sqrt(v) p_{h-1}, E the node Gram, EPSTEIN comb),
r265 s-family (tau(s) = det(I - sE), X'(s) = -||(I - sE)^{-1} F||^2).

THE QUESTION.  For an IIKS kernel the RHP jump is
    J_s(z) = I_2 - 2 pi i s f(z) g(z)^T
on the discrete contour {y_k} (CD nodes).  Zhou: if J + J* ⪰ 0, or
more generally J* H J - H ⪯ 0 for a positive fiber metric H, the
homogeneous RHP is trivial => Fredholm index 0 => tau(s) != 0.  With
tau(0) = 1 and continuity, tau(1) > 0 would follow as a topological
no-crossing.  Does a SOURCE-EXPLICIT H exist?

Worlds TRUE / SCRAMBLE / WPERM / EPSTEIN at a handful of frame-A rungs.
T1 reports min_z lambda_min(J+J*) as a 2x2 fiber diagnostic only
(H=I Hermitian part is NOT a Zhou hypothesis for this tau: the
contour is real, so Zhou needs J*=J^{-1}, which fails; and det J=1
at nodes while det(I-sE)=0, so this J is not the RHP jump equivalent
to tau).  T2 widened (r625b): (a) H=diag(w1,w2) with wi in
{|z|^a, e^{b|z|}, arch^g, comb^d}, 41-pt grids on [-3,3]; (b) c(s) I
and c(s) w_arch I, c in {1, 1-s, 1/(1-s kappa)} kappa in {1/2,1,2};
(c) H=[[1,rho],[rho,1]], |rho|<1.  T3/T4 firewall 6 on a SINGLE
source-explicit H.  T5 same-object ODE ward.

Verdict enum:
  IIKS_METRIC_STRICT_SUFFICIENT / IIKS_METRIC_EQUIVALENT_WALLPAPER /
  IIKS_NO_METRIC_IN_CLASS / INCONCLUSIVE.
Fence: "Finite IIKS/RHP diagnostics; no RH claim."

Claim boundary: experiments only, not a ledger row, not a paper claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

ROUND = 625
CONTRACT = "PRIME.IIKS.VANISHING.METRIC.01"
FENCE = "Finite IIKS/RHP diagnostics; no RH claim."
SEED_SCRAMBLE = 1
SEED_WPERM = 625202609
S_GRID = (0.1, 0.3, 0.5, 0.7, 0.9, 1.0)
RUNGS_FULL = (9, 12, 13, 20, 26)
RUNGS_SMOKE = (9,)
WORLDS = ("TRUE", "SCRAMBLE", "WPERM", "EPSTEIN")
PASS_BAR = -1.0e-12
T1_S0_BAR = 1.0e-12
CD_BAR = 1.0e-8
SYL_BAR = 1.0e-8
ODE_BAR = 1.0e-4
FD_H = 1.0e-4
SMOKE_WALL = 90.0
FULL_WALL = 300.0
PARAM_LO, PARAM_HI = -3.0, 3.0
PARAM_N_FULL, PARAM_N_SMOKE = 41, 11
RHO_N_FULL, RHO_N_SMOKE = 41, 11
FAMILIES = ("pow", "exp", "arch", "comb")
OLD_TRUE_WORST = -3.3645e-7
KAPPA_C = (0.5, 1.0, 2.0)

# v563 T170 surface (copied)
ATOM_MAX = 400000
ZONE_DEEP = 380000
NU_MAIN = 4
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

ALPHA_GRID_FULL = (-2.0, -1.0, 0.0, 1.0, 2.0)
ALPHA_GRID_SMOKE = (0.0, 1.0)
BETA_GRID_FULL = (-1.0, 0.0, 1.0)
BETA_GRID_SMOKE = (0.0, 1.0)

SPEC = {
    "round": ROUND,
    "tag": "r625b",
    "contract": CONTRACT,
    "s_grid": list(S_GRID),
    "rungs_full": list(RUNGS_FULL),
    "rungs_smoke": list(RUNGS_SMOKE),
    "worlds": list(WORLDS),
    "jump": "J = I - 2 pi i s f g^T, f=sqrt(bh)(F,G), g=sqrt(bh)(G,-F)",
    "kernel": "E_ij = bh (F_i G_j - G_i F_j)/(y_i - y_j); tau(s)=det(I-sE)",
    "t1_role": "fiber Hermitian part only; not a Zhou hypothesis",
    "t2_widen": {
        "a": "diag(w1,w2), wi in {pow,exp,arch,comb}, params [-3,3]",
        "n_full": PARAM_N_FULL,
        "n_smoke": PARAM_N_SMOKE,
        "b": "c(s)*I and c(s)*w_arch I, c in {1,1-s,1/(1-s k)} k=1/2,1,2",
        "c": "Sylvester [[1,rho],[rho,1]] |rho|<1",
    },
    "pass_bar": PASS_BAR,
    "seed_scramble": SEED_SCRAMBLE,
    "seed_wperm": SEED_WPERM,
    "copied": [
        "v563 von_mangoldt/arch_lags/atom_lags_at/frame-A geom",
        "PIK grid_density/lambda_eps/folded_measure/lanczos/eval_chain",
        "tau_symbolic CD generators + EPSTEIN comb (v955)",
        "r265 X'(s) = -||(I-sE)^{-1} F||^2",
    ],
    "fence": FENCE,
    "claim_boundary": "experiments_only_not_a_ledger_claim",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []
T0 = 0.0


def emit(line: str = "") -> None:
    LINES.append(line)
    print(line, flush=True)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    emit("  [%s] %-48s %s" % ("PASS" if flag else "FAIL", name, detail))
    return flag


def section(title: str) -> None:
    emit("")
    emit("=" * 74)
    emit(title)
    emit("=" * 74)


def fmt(value, digits: int = 6) -> str:
    if value is None:
        return "nan"
    if isinstance(value, (bool, np.bool_)):
        return "1" if value else "0"
    if isinstance(value, (int, np.integer)) and not isinstance(
            value, (bool, np.bool_)):
        return "%d" % int(value)
    number = float(value)
    if math.isnan(number):
        return "nan"
    if not math.isfinite(number):
        return "+inf" if number > 0.0 else "-inf"
    return "%+.*e" % (digits, number)


def file_sha256() -> str:
    path = os.path.abspath(__file__)
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {
        "zetazero", "nzeros", "primerange", "isprime", "primepi",
        "nextprime", "prevprime", "gram_point", "hp_zero_data",
    }
    bad: list[str] = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
        if isinstance(node, ast.Name) and nm and nm.lower() == "zeta":
            bad.append("zeta@%d" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = (
                [al.name for al in node.names]
                if isinstance(node, ast.Import)
                else [node.module or ""]
            )
            for mod in mods:
                root = (mod or "").split(".")[0]
                if root in (
                    "verification", "v563_paper2_readouts",
                    "tfpt_constants", "port_integrable_kernel_probe",
                    "tau_symbolic_probe", "s_monotonicity_probe",
                    "quenched_opening_probe",
                ):
                    bad.append("import " + (mod or root))
    return (not bad), (
        "NO zero/prime oracles, no verification/ import; "
        "constructions copied"
        if not bad else "; ".join(bad)
    )


# ---------------------------------------------------------------------------
# v563 constructions (copied; no import)
# ---------------------------------------------------------------------------
def von_mangoldt_table(n_max: int) -> np.ndarray:
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


LAM_TAB = von_mangoldt_table(ATOM_MAX)
_NN = np.nonzero(LAM_TAB > 0.0)[0]
U_ALL = np.log(_NN.astype(float))
MU_ALL = 2.0 * LAM_TAB[_NN] / np.sqrt(_NN.astype(float))
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
G_ALL = np.diff(U_ALL)


def atoms_in(alpha: float) -> int:
    return int(np.searchsorted(U_ALL, 2.0 * alpha + 1.0e-14, side="right"))


def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
               / (-np.expm1(-2.0 * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    ess = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
                 + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return ((tri_s * np.exp(-2.0 * w) - ess * np.exp(-0.5 * w))
            / (-np.expm1(-2.0 * w)))


def _arch_A_near(s, D):
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    wmax = s + D
    pts = sorted({0.0, s, D - s, wmax})
    pts = [p for p in pts if 0.0 <= p <= wmax]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        tot += half * float(np.dot(_GLW, _arch_integrand(w, s, D)))
    return (-(EULER + LOG_PI) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * wmax))))


def arch_A(sv, D):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        out[far] = _arch_A_far(sv[far], D)
    for i in np.nonzero(~far)[0]:
        out[i] = _arch_A_near(sv[i], D)
    return out


def arch_lags(m_size, D):
    out = np.empty(m_size)
    for a in range(0, m_size, CHUNK):
        b = min(m_size, a + CHUNK)
        out[a:b] = arch_A(np.arange(a, b) * D, D)
    return out


def atom_lags_at(alpha, m_size, positions, masses):
    D = 2.0 * alpha / m_size
    c = np.zeros(m_size)
    for u_j, mu_j in zip(positions, masses):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(m_size, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(m_size, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D


# ---------------------------------------------------------------------------
# PIK constructions (copied; no import)
# ---------------------------------------------------------------------------
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(n_max: int) -> np.ndarray:
    r = np.zeros(n_max + 1)
    s = int(math.isqrt(n_max)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= n_max:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(n_max + 1)
    for n in range(2, n_max + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def folded_measure(d_arm, length, sign=+1.0):
    jj = np.arange(length)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / length
    wt = (np.abs(d_arm[keep]) / (2.0 * length)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, length - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / length)
    mask = wagg > 1e-300
    return xs[mask], wagg[mask], uf[mask]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    q = np.zeros((m, n))
    q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * q[:, k]
        al[k] = float(q[:, k] @ z)
        z = z - al[k] * q[:, k]
        if k > 0:
            z = z - be[k - 1] * q[:, k - 1]
        for _ in range(2):
            z = z - q[:, :k + 1] @ (q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    p = np.zeros((len(y), n))
    p[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        p[:, 1] = (y - al[0]) * p[:, 0] / be[0]
    for k in range(1, n - 1):
        p[:, k + 1] = ((y - al[k]) * p[:, k]
                       - be[k - 1] * p[:, k - 1]) / be[k]
    return p


def epstein_comb(alpha: float):
    n_e = int(math.floor(math.exp(2.0 * alpha))) + 1
    lam_e = lambda_eps(n_e)
    nn = np.nonzero(np.abs(lam_e) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lam_e[nn] / np.sqrt(nn.astype(float)))


def window_geom(kz: int, scramble_seed=None, comb=None, wperm_seed=None):
    """Frame-A window + lag density.  Copied from v563.build_window +
    PIK.build_rung, minus the unused 2x2 Ahat readout."""
    alpha = float(U_ALL[kz])
    d_k = 0.5 * float(G_ALL[kz]) / float(NU_MAIN)
    mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
    if mz % 2:
        mz += 1
    hz = mz // 2
    ka = atoms_in(alpha)
    uu = U_ALL[:ka].copy()
    mm = MU_ALL[:ka].copy()
    if scramble_seed is not None:
        rng = np.random.default_rng(scramble_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    if wperm_seed is not None:
        rng = np.random.default_rng(wperm_seed)
        mm = rng.permutation(mm)
    if comb is not None:
        uu, mm = np.asarray(comb[0], float), np.asarray(comb[1], float)
    c_at, d_lag = atom_lags_at(alpha, mz, uu, mm)
    c_ar = np.asarray(arch_lags(mz, d_lag), float)
    dens = grid_density(c_ar + c_at)
    dens_arch = grid_density(c_ar)
    return dict(
        h=hz, M=mz, D=d_lag, alpha=alpha, uu=uu, mm=mm,
        d=dens, d_arch=dens_arch, L=2 * mz - 2, kz=kz,
    )


def iiks_cell(kz: int, world: str = "TRUE"):
    """CD / IIKS node Gram + generators.  tau_symbolic.ext_objects
    copied; worlds as v955 TRUE/SCRAMBLE/EPSTEIN plus WPERM."""
    kw: dict = {}
    if world == "SCRAMBLE":
        kw["scramble_seed"] = SEED_SCRAMBLE
    elif world == "WPERM":
        kw["wperm_seed"] = SEED_WPERM
    elif world == "EPSTEIN":
        alpha = float(U_ALL[kz])
        kw["comb"] = epstein_comb(alpha)
    b = window_geom(kz, **kw)
    h, length, d_lag = b["h"], b["L"], b["D"]
    xs, ws, _ = folded_measure(b["d"], length, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], length, -1.0)
    _ya, va, uf_a = folded_measure(b["d_arch"], length, -1.0)
    arch_w = np.zeros(len(uf_n))
    imap = {int(u): i for i, u in enumerate(uf_a)}
    for i, u in enumerate(uf_n):
        j = imap.get(int(u))
        arch_w[i] = float(va[j]) if j is not None else 0.0
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    bh = float(be[h - 1])
    pn = eval_chain(al, be, m0, ys, h + 1)
    sq = np.sqrt(vs)
    e_gram = sq[:, None] * (pn[:, :h] @ pn[:, :h].T) * sq[None, :]
    e_gram = 0.5 * (e_gram + e_gram.T)
    f_vec = sq * pn[:, h]
    g_vec = sq * pn[:, h - 1]
    a_state = sq[:, None] * pn[:, :h]
    q_state = a_state.T @ a_state
    theta = 2.0 * math.pi * uf_n / length
    return dict(
        kz=kz, world=world, h=h, ys=ys, vs=vs, uf=uf_n, E=e_gram,
        F=f_vec, G=g_vec, bh=bh, Q=q_state, A=a_state,
        arch_w=arch_w, theta=theta, D=d_lag, alpha=b["alpha"],
    )


def cd_pred(ys, f_vec, g_vec, bh):
    dx = ys[:, None] - ys[None, :] + np.eye(len(ys))
    return bh * (f_vec[:, None] * g_vec[None, :]
                 - g_vec[:, None] * f_vec[None, :]) / dx


def offdiag_dev(a, b):
    m = a - b
    np.fill_diagonal(m, 0.0)
    a0 = a.copy()
    np.fill_diagonal(a0, 0.0)
    n0 = np.linalg.norm(a0)
    return float(np.linalg.norm(m) / (n0 if n0 > 0 else 1.0))


def slogdet_is(k_mat, s):
    sgn, ld = np.linalg.slogdet(np.eye(k_mat.shape[0]) - s * k_mat)
    return float(sgn), float(ld)


def tau_value(k_mat, s):
    sgn, ld = slogdet_is(k_mat, s)
    if not math.isfinite(ld):
        return 0.0
    return float(sgn * math.exp(min(ld, 700.0)))


# ---------------------------------------------------------------------------
# IIKS jump + Zhou metric (2x2 fiber at each node)
# ---------------------------------------------------------------------------
def fiber_fg(f_scalar, g_scalar, bh):
    scale = math.sqrt(max(bh, 0.0))
    f = scale * np.stack([f_scalar, g_scalar], axis=1)
    g = scale * np.stack([g_scalar, -f_scalar], axis=1)
    return f, g


def jump_at(s, f2, g2):
    return np.eye(2, dtype=complex) - (2j * math.pi * s) * np.outer(f2, g2)


def herm_lmin(mat):
    h = 0.5 * (mat + mat.conj().T)
    ev = np.linalg.eigvalsh(h)
    return float(np.real(ev[0]))


def t1_lmin_closed(s, f_scalar, g_scalar, bh):
    """lambda_min(J+J*) = 2 - 2 pi s bh (F^2 + G^2) for real generators."""
    return 2.0 - 2.0 * math.pi * s * bh * (f_scalar * f_scalar
                                           + g_scalar * g_scalar)


def metric_lmin(js, h_mat):
    jc = js.conj().T
    return herm_lmin(h_mat - jc @ h_mat @ js)


def clip_pos(w, lo=1.0e-8, hi=1.0e8):
    w = np.asarray(w, float)
    return np.clip(np.maximum(np.abs(w), lo), lo, hi)


def herm2_lmin(mat):
    """Vectorized λ_min of the Hermitian part of a (...,2,2) stack."""
    h = 0.5 * (mat + np.conjugate(np.swapaxes(mat, -1, -2)))
    p = np.real(h[..., 0, 0])
    r = np.real(h[..., 1, 1])
    q = h[..., 0, 1]
    disc = (p - r) ** 2 + 4.0 * np.abs(q) ** 2
    return 0.5 * (p + r - np.sqrt(np.maximum(disc, 0.0)))


def jumps_stack(cell, s_grid):
    f, g = fiber_fg(cell["F"], cell["G"], cell["bh"])
    s = np.asarray(s_grid, float)[:, None, None, None]
    outer = (f[:, :, None] * g[:, None, :])[None, :, :, :]
    eye = np.eye(2, dtype=complex)
    return eye - (2j * math.pi * s) * outer, f, g


def family_weight(cell, name, params):
    """name in FAMILIES; params shape (P,); returns (P, Z)."""
    params = np.asarray(params, float).reshape(-1)
    y = np.abs(np.asarray(cell["ys"], float))
    zsafe = np.maximum(y, 1.0e-12)
    if name == "pow":
        w = np.power(zsafe[None, :], params[:, None])
    elif name == "exp":
        w = np.exp(params[:, None] * y[None, :])
    elif name == "arch":
        base = clip_pos(cell["arch_w"])
        w = np.power(base[None, :], params[:, None])
    else:
        base = clip_pos(cell["vs"])
        w = np.power(base[None, :], params[:, None])
    return clip_pos(w)


def metric_diag_mins(j_stack, a, b, chunk=160):
    """min_{s,z} λ_min(H-J*HJ) for H=diag(a,b). a,b: (P,Z) or (Z,)."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if a.ndim == 1:
        a = a[None, :]
        b = b[None, :]
    p_count = a.shape[0]
    out = np.empty(p_count)
    jc = np.conjugate(np.swapaxes(j_stack, -1, -2))
    for i0 in range(0, p_count, chunk):
        i1 = min(p_count, i0 + chunk)
        aa = a[i0:i1]
        bb = b[i0:i1]
        hj = np.empty(aa.shape[:1] + j_stack.shape, dtype=complex)
        hj[..., 0, :] = aa[:, None, :, None] * j_stack[None, ..., 0, :]
        hj[..., 1, :] = bb[:, None, :, None] * j_stack[None, ..., 1, :]
        jshj = np.einsum("szik,pszkj->pszij", jc, hj)
        h = np.zeros((aa.shape[0], aa.shape[1], 2, 2), dtype=complex)
        h[:, :, 0, 0] = aa
        h[:, :, 1, 1] = bb
        lmin = herm2_lmin(h[:, None, :, :, :] - jshj)
        out[i0:i1] = np.min(lmin, axis=(1, 2))
    return out


def metric_const_min(j_stack, h_mat):
    h_mat = np.asarray(h_mat, dtype=complex)
    hj = np.einsum("ik,szkj->szij", h_mat, j_stack)
    jc = np.conjugate(np.swapaxes(j_stack, -1, -2))
    jshj = np.einsum("szik,szkj->szij", jc, hj)
    return float(np.min(herm2_lmin(h_mat - jshj)))


def finite_lmin(val):
    if not math.isfinite(val):
        return -1.0e300
    return float(val)


def t1_crossing(cell):
    """Smallest s>0 at which min_z lambda_min(J+J*) hits 0 (H=I)."""
    mag = cell["bh"] * (cell["F"] * cell["F"] + cell["G"] * cell["G"])
    m = float(np.max(mag))
    k = int(np.argmax(mag))
    if m <= 0.0:
        return None, None
    return 1.0 / (math.pi * m), float(cell["ys"][k])


def scan_t1(cell, s_grid):
    f, g = fiber_fg(cell["F"], cell["G"], cell["bh"])
    rows = []
    s0_dev = 0.0
    closed_dev = 0.0
    for s in s_grid:
        lmins = []
        closed = t1_lmin_closed(s, cell["F"], cell["G"], cell["bh"])
        for k in range(len(cell["ys"])):
            js = jump_at(s, f[k], g[k])
            val = finite_lmin(herm_lmin(js + js.conj().T))
            lmins.append(val)
            cval = float(closed[k])
            if math.isfinite(val) and math.isfinite(cval):
                scale = max(1.0, abs(cval), abs(val))
                closed_dev = max(closed_dev, abs(val - cval) / scale)
        rows.append({
            "s": s,
            "min": float(np.min(lmins)),
            "max": float(np.max(lmins)),
            "argmin": int(np.argmin(lmins)),
            "z": float(cell["ys"][int(np.argmin(lmins))]),
        })
    # s = 0 explicit
    js0 = jump_at(0.0, f[0], g[0])
    s0_dev = max(s0_dev, float(np.linalg.norm(js0 - np.eye(2))))
    return dict(rows=rows, s0_dev=s0_dev, closed_dev=closed_dev)


def first_tau_zero(e_gram):
    ev = np.linalg.eigvalsh(e_gram)
    lmax = float(ev[-1])
    if lmax <= 0.0:
        return float("inf"), lmax
    return 1.0 / lmax, lmax


def paradox_audit(cell, s_star):
    """Zhou symmetry + tau-link on one cell (WPERM s* in (0,1))."""
    f, g = fiber_fg(cell["F"], cell["G"], cell["bh"])
    pair = np.sum(f * g, axis=1)
    pair_dev = float(np.max(np.abs(pair)))
    out = {"pair_dev": pair_dev}
    for tag, s in (("sstar", float(s_star)), ("s1", 1.0)):
        if not math.isfinite(s) or s <= 0.0:
            continue
        j_stack, _, _ = jumps_stack(cell, (s,))
        js = j_stack[0]
        detj = js[:, 0, 0] * js[:, 1, 1] - js[:, 0, 1] * js[:, 1, 0]
        jinv = np.eye(2, dtype=complex)[None, :, :] + (
            2j * math.pi * s) * (f[:, :, None] * g[:, None, :])
        jstar = np.conjugate(np.swapaxes(js, -1, -2))
        rel = []
        for k in range(len(f)):
            den = max(float(np.linalg.norm(jinv[k])), 1.0)
            rel.append(float(np.linalg.norm(jstar[k] - jinv[k])) / den)
        lmin = float(np.min(herm2_lmin(js + jstar)))
        sgn, ld = slogdet_is(cell["E"], s)
        out[tag] = dict(
            s=s,
            detj_dev=float(np.max(np.abs(detj - 1.0))),
            unitarity=float(np.max(rel)),
            lmin_jj=lmin,
            tau=float(sgn * math.exp(min(ld, 700.0))),
            logabs=ld,
        )
    return out


def apply_h_margin(cell, s_grid, recipe):
    """Evaluate one source-explicit H recipe; returns margin and weights."""
    kind = recipe["kind"]
    j_stack, _, _ = jumps_stack(cell, s_grid)
    if kind == "diag":
        a = family_weight(cell, recipe["f1"], np.array([recipe["p1"]]))[0]
        b = family_weight(cell, recipe["f2"], np.array([recipe["p2"]]))[0]
        return float(metric_diag_mins(j_stack, a, b)[0]), a, b
    if kind == "cs":
        cvals = []
        form = recipe["form"]
        kap = recipe.get("kappa", 1.0)
        for s in s_grid:
            if form == "1":
                cvals.append(1.0)
            elif form == "1-s":
                cvals.append(1.0 - s)
            else:
                den = 1.0 - s * kap
                cvals.append(den if abs(den) > 1e-12 else float("nan"))
        cvals = np.asarray(cvals, float)
        if np.any(~np.isfinite(cvals)) or np.any(cvals <= 0.0):
            return -1.0e300, None, None
        arch = clip_pos(cell["arch_w"]) if recipe.get("arch") else np.ones(
            len(cell["ys"]))
        mins = []
        for i, s in enumerate(s_grid):
            a = cvals[i] * arch
            mins.append(float(metric_diag_mins(j_stack[i:i + 1], a, a)[0]))
        return float(np.min(mins)), cvals[0] * arch, cvals[0] * arch
    if kind == "rho":
        rho = float(recipe["rho"])
        h_mat = np.array([[1.0, rho], [rho, 1.0]], dtype=complex)
        return metric_const_min(j_stack, h_mat), None, None
    return -1.0e300, None, None


def first_fail_recipe(cell, recipe, s_hi=1.0):
    s_grid = np.geomspace(1.0e-12, max(float(s_hi), 1.0e-12), 32)
    for s in s_grid:
        m, _, _ = apply_h_margin(cell, (float(s),), recipe)
        if m < PASS_BAR:
            return float(s)
    return None


def widen_scan_cell(cell, s_grid, p_grid, rho_grid):
    """Per-cell best over (a)(b)(c). Also returns (a) margins per pair."""
    j_stack, _, _ = jumps_stack(cell, s_grid)
    best = dict(margin=-1.0e300, name="none", recipe=None)
    pair_best = {}
    n_p = len(p_grid)
    for f1 in FAMILIES:
        w1 = family_weight(cell, f1, p_grid)
        for f2 in FAMILIES:
            w2 = family_weight(cell, f2, p_grid)
            a = np.broadcast_to(w1[:, None, :], (n_p, n_p, w1.shape[1]))
            b = np.broadcast_to(w2[None, :, :], (n_p, n_p, w2.shape[1]))
            a = np.reshape(a, (n_p * n_p, -1))
            b = np.reshape(b, (n_p * n_p, -1))
            mins = metric_diag_mins(j_stack, a, b)
            k = int(np.argmax(mins))
            i, j = divmod(k, n_p)
            rec = dict(
                margin=float(mins[k]),
                name="diag:%s^%+.2f:%s^%+.2f" % (
                    f1, p_grid[i], f2, p_grid[j]),
                recipe=dict(kind="diag", f1=f1, f2=f2,
                            p1=float(p_grid[i]), p2=float(p_grid[j])),
                mins=mins,
            )
            pair_best[(f1, f2)] = rec
            if rec["margin"] > best["margin"]:
                best = dict(rec)
    for form, kap in (("1", None), ("1-s", None),
                      ("1/(1-sk)", 0.5), ("1/(1-sk)", 1.0),
                      ("1/(1-sk)", 2.0)):
        for use_arch in (False, True):
            recipe = dict(kind="cs", form=form, kappa=kap, arch=use_arch)
            m, _, _ = apply_h_margin(cell, s_grid, recipe)
            name = "cs:%s%s%s" % (
                form,
                ("" if kap is None else "*k=%.1f" % kap),
                ("*arch" if use_arch else ""),
            )
            if m > best["margin"]:
                best = dict(margin=m, name=name, recipe=recipe)
    for rho in rho_grid:
        recipe = dict(kind="rho", rho=float(rho))
        m, _, _ = apply_h_margin(cell, s_grid, recipe)
        name = "rho=%+.3f" % rho
        if m > best["margin"]:
            best = dict(margin=m, name=name, recipe=recipe)
    best["pass_"] = best["margin"] >= PASS_BAR
    return best, pair_best


def rejj_track(cell, s_grid):
    f, g = fiber_fg(cell["F"], cell["G"], cell["bh"])
    track = []
    for s in s_grid:
        lmins = [
            herm_lmin(jump_at(s, f[k], g[k]) + jump_at(s, f[k], g[k]).conj().T)
            for k in range(len(cell["ys"]))
        ]
        sgn, ld = slogdet_is(cell["E"], s)
        track.append(dict(
            s=s, lmin=float(np.min(lmins)),
            tau=float(sgn * math.exp(min(ld, 700.0))),
            logabs=ld, sign=int(sgn),
        ))
    return track


def ode_ward(cell, s_eval=0.5):
    """T5: JMU d log tau / ds vs FD, and r265 X' identity on the same E, F."""
    e_gram = cell["E"]
    f_vec = cell["F"]
    n = e_gram.shape[0]
    eye = np.eye(n)
    s = float(s_eval)
    if s <= FD_H or s >= 1.0 - FD_H:
        s = 0.5

    def log_tau(sv):
        sgn, ld = slogdet_is(e_gram, sv)
        return ld + (0.0 if sgn >= 0 else math.pi * 1j)

    def x_of(sv):
        m = np.linalg.solve(eye - sv * e_gram, f_vec)
        return 1.0 - sv * float(f_vec @ m), m

    # JMU
    mids = np.linalg.solve(eye - s * e_gram, e_gram)
    jmu = -float(np.trace(mids))
    fd_tau = (np.linalg.slogdet(eye - (s + FD_H) * e_gram)[1]
              - np.linalg.slogdet(eye - (s - FD_H) * e_gram)[1]) / (
                  2.0 * FD_H)
    # X and X'
    xs, mvec = x_of(s)
    x_ode = -float(mvec @ mvec)
    xp, _ = x_of(s + FD_H)
    xm, _ = x_of(s - FD_H)
    x_fd = (xp - xm) / (2.0 * FD_H)
    # Sylvester
    q = cell["Q"]
    syl_ok = True
    syl_dev = 0.0
    for sv in (0.5, 1.0):
        s1, l1 = slogdet_is(e_gram, sv)
        s2, l2 = slogdet_is(q, sv)
        syl_ok = syl_ok and (s1 == s2) and abs(l1 - l2) <= SYL_BAR * (
            1.0 + abs(l1))
        syl_dev = max(syl_dev, abs(l1 - l2))
    tau0_sign, tau0_ld = slogdet_is(e_gram, 0.0)
    return dict(
        jmu=jmu, fd_tau=float(fd_tau),
        jmu_rel=abs(jmu - float(fd_tau)) / max(abs(jmu), 1e-30),
        x_ode=x_ode, x_fd=x_fd,
        x_rel=abs(x_ode - x_fd) / max(abs(x_ode), 1e-30),
        x_s=xs, syl_ok=syl_ok, syl_dev=syl_dev,
        tau0=(tau0_sign, tau0_ld),
    )


# ---------------------------------------------------------------------------
# protocol
# ---------------------------------------------------------------------------
def type_t3(records):
    """Firewall 6: pass/fail of any T2 class vs sign tau(1)."""
    pos = []
    neg = []
    for rec in records:
        key = (rec["kz"], rec["world"])
        if rec["tau1"] > 0.0:
            pos.append((key, rec["class_pass"], rec["h"]))
        else:
            neg.append((key, rec["class_pass"], rec["h"]))
    if not pos:
        return "INCONCLUSIVE", "no tau(1)>0 cell"
    pos_pass = [p for p in pos if p[1]]
    pos_fail = [p for p in pos if not p[1]]
    neg_pass = [p for p in neg if p[1]]
    if not pos_pass:
        return "IIKS_NO_METRIC_IN_CLASS", (
            "no source-explicit class passes anywhere tau(1)>0 "
            "(%d positive cells)" % len(pos)
        )
    if pos_fail:
        rungs = sorted({p[0][0] for p in pos_pass})
        return "IIKS_METRIC_STRICT_SUFFICIENT", (
            "passes on a strict subset of tau(1)>0 cells; "
            "pass rungs %s (%d/%d positive)" % (
                rungs, len(pos_pass), len(pos))
        )
    # all positive pass
    if neg_pass:
        return "IIKS_METRIC_STRICT_SUFFICIENT", (
            "passes on all tau(1)>0 but also on %d non-positive "
            "control cell(s) — not equivalent" % len(neg_pass)
        )
    return "IIKS_METRIC_EQUIVALENT_WALLPAPER", (
        "some class passes exactly on tau(1)>0 cells and fails "
        "where tau(1)<=0 (%d pos / %d nonpos)" % (len(pos), len(neg))
    )


def run(smoke: bool) -> int:
    global T0, CHECKS, LINES
    T0 = time.time()
    CHECKS = []
    LINES = []
    rungs = RUNGS_SMOKE if smoke else RUNGS_FULL
    n_param = PARAM_N_SMOKE if smoke else PARAM_N_FULL
    n_rho = RHO_N_SMOKE if smoke else RHO_N_FULL
    p_grid = np.linspace(PARAM_LO, PARAM_HI, n_param)
    rho_grid = np.linspace(-0.95, 0.95, n_rho)
    wall_bar = SMOKE_WALL if smoke else FULL_WALL
    s_pos = S_GRID

    emit("=" * 74)
    emit("iiks_vanishing_metric_probe -- r%d  %s" % (ROUND, CONTRACT))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("mode: %s" % ("SMOKE" if smoke else "FULL"))
    emit("rungs %s  worlds %s  s %s" % (rungs, WORLDS, S_GRID))
    emit(FENCE)
    emit("=" * 74)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G01-spec-frozen", True,
          "SPEC_SHA %s; r625b widen a/b/c; n_param=%d; "
          "pass_bar %.0e; H=I Re(J) is not a Zhou hypothesis"
          % (SPEC_SHA[:16], n_param, PASS_BAR))

    section("S1  BUILD IIKS CELLS")
    cells = {}
    build_ok = True
    for kz in rungs:
        for world in WORLDS:
            cell = iiks_cell(kz, world)
            key = (kz, world)
            cells[key] = cell
            if cell is None:
                build_ok = False
                emit("  BUILD FAIL kz=%d %s" % (kz, world))
            else:
                emit("  built kz=%-3d %-8s h=%-4d nodes=%-4d bh=%s"
                     % (kz, world, cell["h"], len(cell["ys"]),
                        fmt(cell["bh"], 4)))
    check("G02-build", build_ok and all(cells[k] is not None
                                        for k in cells),
          "%d cells (rungs x worlds)" % len(cells))

    section("S2  T1  H=I  min_z lambda_min(J+J*)")
    t1 = {}
    t1_s0_ok = True
    t1_closed_ok = True
    cd_ok = True
    closed_true_dev = 0.0
    for key, cell in cells.items():
        if cell is None:
            continue
        pred = cd_pred(cell["ys"], cell["F"], cell["G"], cell["bh"])
        d_cd = offdiag_dev(cell["E"], pred)
        cd_ok = cd_ok and d_cd <= CD_BAR
        rec = scan_t1(cell, s_pos)
        rec["cd"] = d_cd
        # s=0 gate
        f, g = fiber_fg(cell["F"], cell["G"], cell["bh"])
        dev0 = 0.0
        for k in range(len(cell["ys"])):
            js = jump_at(0.0, f[k], g[k])
            dev0 = max(dev0, float(np.linalg.norm(js - np.eye(2))))
        rec["s0_dev"] = dev0
        rec["rejj_pos"] = min(r["min"] for r in rec["rows"]) >= PASS_BAR
        t1_s0_ok = t1_s0_ok and dev0 <= T1_S0_BAR
        if key[1] == "TRUE":
            t1_closed_ok = t1_closed_ok and rec["closed_dev"] <= 1.0e-8
            closed_true_dev = max(closed_true_dev, rec["closed_dev"])
        t1[key] = rec
        row_s = " ".join(
            "s%s:%s" % (fmt(r["s"], 1).replace("+", ""), fmt(r["min"], 3))
            for r in rec["rows"]
        )
        emit("  T1 kz=%-3d %-8s cd=%s s0=%s ReJJ>=0=%s  %s"
             % (key[0], key[1], fmt(d_cd, 2), fmt(dev0, 2),
                "Y" if rec["rejj_pos"] else "N", row_s))
    check("G10-t1-s0-is-I", t1_s0_ok,
          "J(s=0)=I on every node (max ||J-I|| <= %.0e)" % T1_S0_BAR)
    check("G11-t1-closed-form", t1_closed_ok,
          "TRUE: matrix lambda_min(J+J*) == 2-2pi s bh(F^2+G^2) "
          "rel <= 1e-8 (worst %s); scramble overflow skipped"
          % fmt(closed_true_dev, 2))
    check("G12-cd-identity", cd_ok,
          "offdiag E == CD kernel (bar %.0e)" % CD_BAR)

    section("S2b  PARADOX  Zhou symmetry vs tau=0")
    wperm_cells = [(kz, "WPERM") for kz in rungs
                   if cells.get((kz, "WPERM")) is not None]
    paradox = None
    px_key = None
    for kz, world in wperm_cells:
        s_star, _lmax = first_tau_zero(cells[(kz, world)]["E"])
        if 0.0 < s_star < 1.0:
            px_key = (kz, world)
            paradox = paradox_audit(cells[px_key], s_star)
            break
    if paradox is None and wperm_cells:
        px_key = wperm_cells[0]
        s_star, _lmax = first_tau_zero(cells[px_key]["E"])
        paradox = paradox_audit(cells[px_key], s_star)
    if paradox is None:
        paradox = {"pair_dev": 0.0}
    emit("  PARADOX cell kz=%s WPERM" % (
        px_key[0] if px_key else "?"))
    emit("    pairing max|f^T g| = %s (IIKS Sigma f_i g_i = 0)"
         % fmt(paradox["pair_dev"], 3))
    for tag in ("sstar", "s1"):
        if tag not in paradox:
            continue
        p = paradox[tag]
        emit("    %s s=%s  detJ-1=%s  ||J*-Jinv||rel=%s  "
             "min λ(J+J*)=%s  tau=%s"
             % (tag, fmt(p["s"], 4), fmt(p["detj_dev"], 3),
                fmt(p["unitarity"], 3), fmt(p["lmin_jj"], 3),
                fmt(p["tau"], 3)))
    emit("  RESOLUTION: contour is real (CD nodes in [-1,1]), so "
         "Zhou needs J*=J^{-1}.  This J has det=1 and (fg^T)^2=0 "
         "so J^{-1}=I+2pii s fg^T, but J*=I+2pii s gf^T ≠ J^{-1}.")
    emit("  tau(s)=0 is det(I-sE)=0 (discrete CD Gram), not "
         "solvability of a Cauchy RHP on these fibers: at s* one "
         "has det J=1 at every node while tau=0.  H=I Re(J+J*)>=0 "
         "is the wrong sufficient condition for this tau.")
    pstar = paradox.get("sstar", {})
    check("G13-pairing-zero", paradox["pair_dev"] <= 1e-10,
          "max |f^T g| %s" % fmt(paradox["pair_dev"], 3))
    check("G14-detJ-is-1",
          pstar.get("detj_dev", 1.0) <= 1e-10,
          "det J(s*)-1 = %s" % fmt(pstar.get("detj_dev", 1.0), 3))
    check("G15-tau0-not-Jsing",
          pstar.get("detj_dev", 1.0) <= 1e-10
          and abs(pstar.get("logabs", 0.0)) >= 1.0,
          "at s* det J=1 but |tau|~exp(%s): no tau=0 <=> J singular"
          % fmt(pstar.get("logabs", 0.0), 2))
    check("G16-zhou-symmetry-fails",
          pstar.get("unitarity", 0.0) >= 1e-3,
          "max ||J*-J^{-1}||rel = %s (not unitary on the real line)"
          % fmt(pstar.get("unitarity", 0.0), 3))

    section("S3  T2  WIDENED SOURCE-EXPLICIT METRICS")
    t2 = {}
    t2_any = True
    global_a = {pair: None for pair in (
        (f1, f2) for f1 in FAMILIES for f2 in FAMILIES)}
    global_rho = np.full(len(rho_grid), np.inf)
    global_cs = {}
    for key, cell in cells.items():
        if cell is None:
            t2_any = False
            continue
        best, pair_best = widen_scan_cell(cell, s_pos, p_grid, rho_grid)
        t2[key] = dict(best=best, pairs=pair_best)
        emit("  T2 kz=%-3d %-8s best=%s margin=%s pass=%s"
             % (key[0], key[1], best["name"], fmt(best["margin"], 4),
                "Y" if best["pass_"] else "N"))
        if key[1] == "TRUE":
            for pair, rec in pair_best.items():
                if global_a[pair] is None:
                    global_a[pair] = rec["mins"].copy()
                else:
                    global_a[pair] = np.minimum(global_a[pair], rec["mins"])
            for i, rho in enumerate(rho_grid):
                recipe = dict(kind="rho", rho=float(rho))
                m, _, _ = apply_h_margin(cell, s_pos, recipe)
                global_rho[i] = min(global_rho[i], m)
            for form, kap in (("1", None), ("1-s", None),
                              ("1/(1-sk)", 0.5), ("1/(1-sk)", 1.0),
                              ("1/(1-sk)", 2.0)):
                for use_arch in (False, True):
                    ck = (form, kap, use_arch)
                    recipe = dict(kind="cs", form=form, kappa=kap,
                                  arch=use_arch)
                    m, _, _ = apply_h_margin(cell, s_pos, recipe)
                    global_cs[ck] = min(global_cs.get(ck, 1e300), m)
    check("G20-t2-widened", t2_any and len(t2) == len(cells),
          "%d cells; (a) %d^2 x 16 pairs + (b) cs + (c) %d rho"
          % (len(t2), n_param, n_rho))

    # best SINGLE H across all TRUE
    glob = dict(margin=-1.0e300, name="none", recipe=None)
    for pair, mins in global_a.items():
        if mins is None:
            continue
        k = int(np.argmax(mins))
        i, j = divmod(k, n_param)
        m = float(mins[k])
        name = "diag:%s^%+.2f:%s^%+.2f" % (
            pair[0], p_grid[i], pair[1], p_grid[j])
        if m > glob["margin"]:
            glob = dict(
                margin=m, name=name,
                recipe=dict(kind="diag", f1=pair[0], f2=pair[1],
                            p1=float(p_grid[i]), p2=float(p_grid[j])),
            )
    if np.any(np.isfinite(global_rho)):
        i = int(np.nanargmax(global_rho))
        m = float(global_rho[i])
        if m > glob["margin"]:
            glob = dict(
                margin=m, name="rho=%+.3f" % rho_grid[i],
                recipe=dict(kind="rho", rho=float(rho_grid[i])),
            )
    for ck, m in global_cs.items():
        form, kap, use_arch = ck
        name = "cs:%s%s%s" % (
            form,
            ("" if kap is None else "*k=%.1f" % kap),
            ("*arch" if use_arch else ""),
        )
        if m > glob["margin"]:
            glob = dict(
                margin=m, name=name,
                recipe=dict(kind="cs", form=form, kappa=kap, arch=use_arch),
            )
    glob["pass_"] = glob["margin"] >= PASS_BAR
    emit("  T2 GLOBAL-TRUE best=%s margin=%s pass=%s"
         % (glob["name"], fmt(glob["margin"], 4),
            "Y" if glob["pass_"] else "N"))
    true_worst = min(t2[(kz, "TRUE")]["best"]["margin"] for kz in rungs
                     if (kz, "TRUE") in t2)
    emit("  T2 TRUE per-cell worst-best %s  (r625 was %s, moved %s)"
         % (fmt(true_worst, 4), fmt(OLD_TRUE_WORST, 4),
            fmt(true_worst - OLD_TRUE_WORST, 4)))

    section("S4  T3  PATTERN vs sign tau(1)")
    recs = []
    for key, cell in cells.items():
        if cell is None:
            continue
        sgn1, ld1 = slogdet_is(cell["E"], 1.0)
        tau1 = float(sgn1 * math.exp(min(ld1, 700.0)))
        if glob["recipe"] is not None:
            m_g, _, _ = apply_h_margin(cell, s_pos, glob["recipe"])
        else:
            m_g = t2[key]["best"]["margin"]
        recs.append(dict(
            kz=key[0], world=key[1], h=cell["h"],
            tau1=tau1, sign=int(np.sign(tau1)) if tau1 != 0 else 0,
            ld1=ld1, class_pass=bool(m_g >= PASS_BAR),
            best_name=t2[key]["best"]["name"],
            best_margin=t2[key]["best"]["margin"],
            glob_margin=m_g,
        ))
        emit("  T3 kz=%-3d %-8s tau(1)=%s sign=%+d  cellbest=%s  "
             "globH=%s pass=%s"
             % (key[0], key[1], fmt(tau1, 4), int(np.sign(tau1)),
                fmt(t2[key]["best"]["margin"], 3), fmt(m_g, 3),
                "Y" if m_g >= PASS_BAR else "N"))
    if not glob["pass_"]:
        verd = "IIKS_NO_METRIC_IN_CLASS"
        why = (
            "no single source-explicit H passes all TRUE "
            "(global-TRUE margin %s; per-cell worst-best %s, "
            "r625 %s -> %s)"
            % (fmt(glob["margin"], 4), fmt(true_worst, 4),
               fmt(OLD_TRUE_WORST, 4),
               fmt(true_worst - OLD_TRUE_WORST, 4))
        )
    else:
        verd, why = type_t3(recs)
        why = "H=%s | %s" % (glob["name"], why)
    check("G30-t3-typed", verd != "INCONCLUSIVE" or any(
        r["tau1"] > 0 for r in recs),
          "%s -- %s" % (verd, why))

    section("S5  T4  CONTROLS vs tau-zero")
    t4_rows = []
    t4_ok = True
    recipe_t4 = glob["recipe"] or t2[(rungs[0], "TRUE")]["best"]["recipe"]
    for kz in rungs:
        for world in ("SCRAMBLE", "WPERM", "EPSTEIN"):
            key = (kz, world)
            cell = cells[key]
            if cell is None:
                t4_ok = False
                continue
            s_star, lmax = first_tau_zero(cell["E"])
            class_fail_s = first_fail_recipe(
                cell, recipe_t4, s_hi=max(s_star, 1.0))
            before_cl = (class_fail_s is not None) and (
                class_fail_s < s_star - 1e-15)
            m_g = next(r["glob_margin"] for r in recs
                       if r["kz"] == kz and r["world"] == world)
            ctrl_breaks = m_g < PASS_BAR
            if world in ("SCRAMBLE", "EPSTEIN"):
                t4_ok = t4_ok and ctrl_breaks
            t4_rows.append(dict(
                kz=kz, world=world, s_star=s_star, lmax=lmax,
                class_fail_s=class_fail_s,
                before=bool(before_cl),
                breaks=ctrl_breaks,
            ))
            emit(
                "  T4 kz=%-3d %-8s s*=%s  class_fail_s=%s before=%s "
                "globH=%s"
                % (kz, world, fmt(s_star, 4),
                   fmt(class_fail_s, 3) if class_fail_s is not None
                   else "none",
                   "Y" if before_cl else "N", fmt(m_g, 3))
            )
    check("G40-t4-controls-break", t4_ok,
          "SCRAMBLE/EPSTEIN fail the scored H (before/after s* reported)")

    section("S6  T5  SAME-OBJECT ODE (r265 / JMU)")
    t5_syl = True
    t5_jmu = True
    t5_x = True
    t5_tau0 = True
    t5_detail = []
    t5_keys = [(rungs[0], "TRUE")]
    if not smoke:
        t5_keys.append((rungs[0], "SCRAMBLE"))
        if (rungs[-1], "TRUE") not in t5_keys:
            t5_keys.append((rungs[-1], "TRUE"))
    for key in t5_keys:
        cell = cells[key]
        s_star, _lmax = first_tau_zero(cell["E"])
        s_eval = 0.5 if s_star > 0.7 else max(0.05, 0.45 * min(s_star, 1.0))
        w = ode_ward(cell, s_eval)
        t5_syl = t5_syl and w["syl_ok"]
        t5_jmu = t5_jmu and w["jmu_rel"] <= ODE_BAR
        t5_x = t5_x and w["x_rel"] <= ODE_BAR
        t5_tau0 = t5_tau0 and (w["tau0"][0] == 1.0 and abs(w["tau0"][1]) <= 1e-12)
        t5_detail.append(w)
        emit("  T5 kz=%-3d %-8s s=%s syl_dev=%s  JMU rel=%s  X' rel=%s  "
             "X=%s  tau(0)=(%s,%s)"
             % (key[0], key[1], fmt(s_eval, 2), fmt(w["syl_dev"], 3),
                fmt(w["jmu_rel"], 3), fmt(w["x_rel"], 3), fmt(w["x_s"], 4),
                fmt(w["tau0"][0], 1), fmt(w["tau0"][1], 3)))
    check("G50-t5-sylvester", t5_syl,
          "det(I-sE)==det(I-s Q_state) at s=0.5,1 (corpus objects)")
    check("G51-t5-jmu", t5_jmu,
          "d log tau/ds == -Tr[(I-sE)^{-1} E] vs FD (bar %.0e)" % ODE_BAR)
    check("G52-t5-crossratio-ode", t5_x,
          "X'(s)==-||(I-sE)^{-1} F||^2 vs FD (r265 identity, "
          "same E,F)")
    check("G53-t5-tau0-is-1", t5_tau0, "tau(0)=det(I)=1")

    # must-fail: rank-one truncation of the CD kernel
    cell0 = cells[(rungs[0], "TRUE")]
    pred = cd_pred(cell0["ys"], cell0["F"], cell0["G"], cell0["bh"])
    pred1 = cell0["bh"] * np.outer(cell0["F"], cell0["G"]) / (
        cell0["ys"][:, None] - cell0["ys"][None, :] + np.eye(len(cell0["ys"])))
    must = offdiag_dev(cell0["E"], pred) <= CD_BAR and offdiag_dev(
        cell0["E"], pred1) > 1e-3
    check("G60-mustfail-rank1-cd", must,
          "rank-one truncation of the CD kernel breaks the identity")

    section("S7  VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    pipeline = n_pass == n_gate
    if not pipeline:
        verd = "INCONCLUSIVE"
        why = "pipeline gate failure: " + ",".join(
            n for n, ok in CHECKS if not ok)
    emit("VERDICT %s" % verd)
    emit("WHY %s" % why)
    emit("PARADOX H=I Re(J+J*) is not a Zhou hypothesis for this tau")
    wall = time.time() - T0
    check("G90-runtime", wall <= wall_bar,
          "WALL %.1f s (bar %.0f)" % (wall, wall_bar))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    emit("")
    emit("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
         % (n_pass, n_gate, " (SMOKE)" if smoke else "", SPEC_SHA[:16]))
    emit("NO RH CLAIM in either direction.")

    # deterministic numeric payload
    payload = {
        "verdict": verd,
        "glob": {"name": glob["name"],
                 "margin": round(float(glob["margin"]), 12),
                 "pass": bool(glob["pass_"])},
        "true_worst": round(float(true_worst), 12),
        "paradox": {
            "pair": round(float(paradox.get("pair_dev", 0.0)), 12),
            "unitarity": round(float(pstar.get("unitarity", 0.0)), 12),
            "detj": round(float(pstar.get("detj_dev", 0.0)), 12),
        },
        "t2_best": {
            "%d:%s" % key: {
                "name": t2[key]["best"]["name"],
                "margin": round(float(t2[key]["best"]["margin"]), 12),
                "pass": bool(t2[key]["best"]["pass_"]),
            }
            for key in t2
        },
        "t3": [
            {"kz": r["kz"], "w": r["world"],
             "tau1": round(float(r["tau1"]), 12),
             "pass": r["class_pass"],
             "glob": round(float(r["glob_margin"]), 12)}
            for r in recs
        ],
        "t4": [
            {"kz": r["kz"], "w": r["world"],
             "s_star": round(float(r["s_star"]), 12) if math.isfinite(
                 r["s_star"]) else None,
             "class_fail_s": r["class_fail_s"],
             "before": r["before"]}
            for r in t4_rows
        ],
        "t5": {
            "syl": t5_syl, "jmu": t5_jmu, "x": t5_x,
        },
    }
    num_sha = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"),
                   default=str).encode("utf-8")
    ).hexdigest()

    emit("")
    emit("STATE r625b %s" % CONTRACT)
    emit("SHA %s" % file_sha256())
    emit("SPEC %s" % SPEC_SHA)
    emit("NUM %s" % num_sha)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("VERDICT %s" % verd)
    emit("PARADOX real contour => Zhou needs J*=Jinv; measured "
         "||J*-Jinv||=%s while detJ=1 and tau(s*)=0 (WPERM kz%s). "
         "H=I Re(J+J*) is the wrong sufficient condition."
         % (fmt(pstar.get("unitarity", 0.0), 3),
            px_key[0] if px_key else "?"))
    emit("T2 GLOBAL %s margin=%s pass=%s"
         % (glob["name"], fmt(glob["margin"], 4),
            "Y" if glob["pass_"] else "N"))
    emit("T2 TRUE worst-best %s (r625 %s -> %s)"
         % (fmt(true_worst, 4), fmt(OLD_TRUE_WORST, 4),
            fmt(true_worst - OLD_TRUE_WORST, 4)))
    for world in WORLDS:
        bits = []
        for kz in rungs:
            key = (kz, world)
            if key not in t2:
                continue
            bits.append("%s:%s" % (kz, fmt(t2[key]["best"]["margin"], 2)))
        emit("T2 %s cellbest %s" % (world, " ".join(bits)))
    emit("T3 %s | %s" % (verd, why))
    for world in ("SCRAMBLE", "WPERM", "EPSTEIN"):
        rows_w = [r for r in t4_rows if r["world"] == world]
        if not rows_w:
            continue
        r0 = rows_w[0]
        n_before = sum(1 for r in rows_w if r["before"])
        emit("T4 %s s*=%s fail_s=%s before=%d/%d"
             % (world, fmt(r0["s_star"], 3),
                fmt(r0["class_fail_s"], 3) if r0["class_fail_s"] is not None
                else "none",
                n_before, len(rows_w)))
    emit("REUSED copied v563/PIK/tau_symbolic/v955/r265")
    emit("FENCE %s" % FENCE)

    state_prefixes = (
        "STATE ", "SHA ", "SPEC ", "NUM ", "GATES ", "VERDICT ",
        "PARADOX ", "T2 ", "T3 ", "T4 ", "REUSED ", "FENCE ",
    )
    n_state = sum(
        1 for line in LINES
        if line.startswith(state_prefixes)
    )
    emit("STATE_LINES %d" % n_state)
    if n_state > 35:
        emit("STATE_LINES_WARN over 35")
    return 0 if n_pass == n_gate else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r625 IIKS vanishing-lemma metric (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    raise SystemExit(run(args.smoke))


if __name__ == "__main__":
    main()
