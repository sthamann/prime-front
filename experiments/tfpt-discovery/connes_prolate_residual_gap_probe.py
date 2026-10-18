#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""connes_prolate_residual_gap_probe -- r606b.

Numerical measurement scout of the Connes / Connes--van Suijlekom
residual-vs-gap ratio for the truncated Weil form Q_W on [-L, L].

r606 (6-9 mode, t_cut=150) was INCONCLUSIVE: mu jumped to 5.9 and
g<0 at L>=0.6.  That is a discretization artefact (r478: small
blocks do not suffice at L=0.8).  Chuk (arXiv:2608.24827) has
Q_W > 0 at total support 1.6, i.e. L=0.8.  This follow-up climbs
Slepian N in {6,12,24,48} and Fourier N_F in {16,32,64,128,256}
with t_cut in {150,400,1000} until successive sizes differ <1 %%
and the two discretizations agree <5 %%, or a documented wall.

Q_W = A + Pi - P  (r478/r479/r480).  Pi_even = 2|<.,cosh(x/2)>|^2,
Pi_odd = 2|<.,sinh(x/2)>|^2 (kappa_high_probe.pi_matrix).  Prime
nodes: n with log n <= 2L.  float64 only; no intervals.

CANDIDATES (even, L2-normalized).
  k  = CCM Poisson candidate of blockreal_lemma_probe.py
       (Prolate / prolate_pair / k_lambda_on_v; arXiv:2511.22755
       L7.3), lam2=exp(2L), evenized.  NOT a psi0 alias.
  psi0 = lowest even Slepian/sinc mode, band t_c from r479 pins
       (kappa_high_probe.nystrom_modes).

MINCUT (measured, not proved).  mu=<Q kappa,kappa>, r=(Q-mu)kappa,
g=min(l2_even-mu, l1_odd-mu), eta=sqrt(lambda)||r||/g, lambda=e^L.
Davis--Kahan: ||r||<g/3.

PREREGISTERED VERDICT (unchanged from r606).
  GO           g>0 on all L, DK ok on holdout, fitted p>0.55,
               holdout rel-err of ||r||/g <= 20 %.
  PARTIAL      ||r||/g decreases but p<=0.5 or holdout misses.
  STOP         p<=0 or g<=0 anywhere.
  INCONCLUSIVE discretizations disagree >5 % or eigenvalues have
               not converged (successive sizes >1 % or no 5 %%
               cross-disc), or smoke (no holdout).

SCRAMBLE GATE: P uses literal log n.  KEIN RH-CLAIM.  NO RH CLAIM.
Exploration only; not a positivity SATZ; not lambda_*(L)>=0.
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

HERE = os.path.abspath(os.path.dirname(__file__))
CANDIDATES = [
    HERE,
    os.path.join(HERE, "..", "..", "experiments", "tfpt-discovery"),
    "/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery",
]
for path in CANDIDATES:
    path = os.path.abspath(path)
    if os.path.isfile(os.path.join(path, "classical_cert_probe.py")):
        if path not in sys.path:
            sys.path.insert(0, path)
        break

import endtoend_fixedl_probe as E  # noqa: E402
import kappa_high_probe as KH  # noqa: E402
import lambdastar03_probe as L479  # noqa: E402

SEED = 20260902
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

SCRAMBLE_SENSITIVE = True
SCRAMBLE_REASON = (
    "P uses literal log n on nodes log n <= 2L.  Empty at "
    "L <= log(2)/2; live for L >= 0.4.  Not fold-mode pairing."
)

REF_GAMMAS = (
    14.134725141734695, 21.022039638771556, 25.010857580145689,
    30.424876125859513,
)
N_REF_LT30 = sum(1 for g in REF_GAMMAS if g < 30.0)

L_TRAIN = (0.3, 0.4, 0.5, 0.6)
L_HOLDOUT = (0.7, 0.8)
L_FULL = L_TRAIN + L_HOLDOUT
L_SMOKE = (0.3, 0.6)

T_C = 0.5 * (float(L479.T_C_LO_PIN) + float(L479.T_C_HI_PIN))
LOG2_HALF = 0.5 * math.log(2.0)

SUCC_TOL = 0.01
CROSS_TOL = 0.05
P_GO = 0.55
P_PARTIAL = 0.5
HOLDOUT_TOL = 0.20
N_NY_CAP = 320
NT_CAP = 10001

SLEPIAN_N_FULL = (6, 12, 24, 48)
FOURIER_N_FULL = (16, 32, 64, 128, 256)
TCUT_FULL = (150.0, 400.0, 1000.0)
SLEPIAN_N_SMOKE = (6, 12)
FOURIER_N_SMOKE = (16, 32)
TCUT_SMOKE = (150.0, 400.0)


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    forbidden = {"zetazero", "nzeros", "grampoint", "zetazeros"}
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in forbidden:
            bad.append(node.id)
        if isinstance(node, ast.Attribute) and node.attr in forbidden:
            bad.append(node.attr)
    return (not bad), (",".join(sorted(set(bad))) if bad else "")


def _legendre_vals(nmax: int, z: np.ndarray) -> np.ndarray:
    pmat = np.zeros((nmax, len(z)))
    pmat[0] = 1.0
    if nmax > 1:
        pmat[1] = z
    for n in range(1, nmax - 1):
        pmat[n + 1] = ((2 * n + 1) * z * pmat[n] - n * pmat[n - 1]) / (n + 1)
    return pmat


class _Prolate:
    """Legendre-Galerkin PW_lambda on [-lam, lam] (blockreal r112)."""

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


def connes_k_on_grid(lf: float, x: np.ndarray, w: np.ndarray) -> np.ndarray:
    pro = _Prolate(math.exp(2.0 * lf))
    coef = _prolate_h_coef(pro)
    raw = _k_lambda_on_v(pro, coef, x)
    even = 0.5 * (raw + raw[::-1])
    nrm = math.sqrt(max(float(np.sum(w * even * even)), 0.0))
    if nrm < 1e-30:
        return even
    even = even / nrm
    mid = int(np.argmin(np.abs(x)))
    if even[mid] < 0.0:
        even = -even
    return even


def fix_sign_grid(x: np.ndarray, f: np.ndarray) -> np.ndarray:
    mid = int(np.argmin(np.abs(x)))
    if f[mid] < 0.0:
        return -f
    return f


def nystrom_modes_mat(lf: float, tc: float, n: int):
    """Vectorized KH.nystrom_modes; returns ev, x, w, F (n x n)."""
    x_ref, w_ref = np.polynomial.legendre.leggauss(n)
    x = lf * x_ref
    w = lf * w_ref
    sw = np.sqrt(np.maximum(w, 0.0))
    dx = x[:, None] - x[None, :]
    ker = np.empty_like(dx)
    small = np.abs(dx) < 1e-15
    ker[small] = tc / math.pi
    ker[~small] = np.sin(tc * dx[~small]) / (math.pi * dx[~small])
    amat = (sw[:, None] * ker) * sw[None, :]
    amat = 0.5 * (amat + amat.T)
    ev, evecs = np.linalg.eigh(amat)
    idx = np.argsort(ev)[::-1]
    ev, evecs = ev[idx], evecs[:, idx]
    fmat = evecs / np.maximum(sw[:, None], 1e-30)
    nrms = np.sqrt(np.maximum(np.sum(w[:, None] * fmat * fmat, axis=0),
                              1e-30))
    fmat = fmat / nrms
    mid = int(np.argmin(np.abs(x)))
    for k in range(0, fmat.shape[1], 2):
        if fmat[mid, k] < 0.0:
            fmat[:, k] *= -1.0
    return ev, x, w, fmat


def fourier_even_mat(x, w, lf, n_modes) -> np.ndarray:
    fmat = np.empty((len(x), n_modes))
    fmat[:, 0] = 1.0 / math.sqrt(2.0 * lf)
    if n_modes > 1:
        ns = np.arange(1, n_modes)
        fmat[:, 1:] = np.cos(np.pi * x[:, None] * ns / lf) / math.sqrt(lf)
    nrms = np.sqrt(np.maximum(w @ (fmat * fmat), 1e-30))
    return fmat / nrms


def fourier_odd_mat(x, w, lf, n_modes) -> np.ndarray:
    ns = np.arange(1, n_modes + 1)
    fmat = np.sin(np.pi * x[:, None] * ns / lf) / math.sqrt(lf)
    nrms = np.sqrt(np.maximum(w @ (fmat * fmat), 1e-30))
    return fmat / nrms


def hat_mat(x, w, fmat, ts) -> np.ndarray:
    return np.exp(1j * ts[:, None] * x[None, :]) @ (w[:, None] * fmat)


def trap_weights(ts: np.ndarray) -> np.ndarray:
    dt = float(ts[1] - ts[0])
    wts = np.full(len(ts), dt)
    wts[0] *= 0.5
    wts[-1] *= 0.5
    return wts


def gram_from_hats(hats: np.ndarray, wts: np.ndarray,
                   sig: np.ndarray) -> np.ndarray:
    """(1/pi) trapz sig * hats_i * conj(hats_j); same as KH.a_matrix."""
    weighted = hats * (wts * sig)[:, None]
    gram = (weighted.T @ hats.conj()).real / math.pi
    return 0.5 * (gram + gram.T)


def pi_from_F(x, w, fmat, even: bool) -> np.ndarray:
    kern = np.cosh(0.5 * x) if even else np.sinh(0.5 * x)
    ov = fmat.T @ (w * kern)
    return 2.0 * np.outer(ov, ov)


def sigma_p_arr(ts: np.ndarray, nodes) -> np.ndarray:
    out = np.zeros(len(ts))
    for n, lam in nodes:
        out += 2.0 * lam / math.sqrt(n) * np.cos(ts * math.log(n))
    return out


def omega_p_of(nodes) -> float:
    if not nodes:
        return 0.0
    return max(math.log(n) for n, _lam in nodes)


def nt_for(t_cut: float, lf: float, omega_p: float) -> int:
    n_sinc = 16.0 * t_cut * lf / math.pi
    n_p = 8.0 * t_cut * max(omega_p, 1e-15) / math.pi
    n_lin = 4.0 * t_cut
    n = int(max(512.0, n_sinc, n_p, n_lin))
    n = min(n, NT_CAP)
    if n % 2 == 0:
        n += 1
    return n


def n_ny_for(lf: float, n_mode: int, t_cut: float, kind: str) -> int:
    spatial = int(math.ceil(2.5 * t_cut * lf / math.pi))
    if kind == "fourier":
        mode = 4 * n_mode
    else:
        mode = max(2 * n_mode, 64)
    return min(max(spatial, mode, 64), N_NY_CAP)


def t_grid(t_cut: float, nt: int, nodes):
    ts = np.linspace(0.0, t_cut, nt)
    sig_a = KH.sigma_arr(ts)
    sig_p = sigma_p_arr(ts, nodes) if nodes else None
    wts = trap_weights(ts)
    return ts, wts, sig_a, sig_p


def q_from_hats(hats, wts, sig_a, sig_p, x, w, fmat, even: bool):
    amat = gram_from_hats(hats, wts, sig_a)
    pmat = (gram_from_hats(hats, wts, sig_p) if sig_p is not None
            else np.zeros_like(amat))
    return amat - pmat + pi_from_F(x, w, fmat, even)


def evals3(q_e: np.ndarray, q_o: np.ndarray) -> tuple[float, float, float]:
    ev_e = np.sort(np.linalg.eigvalsh(q_e))
    ev_o = np.sort(np.linalg.eigvalsh(q_o))
    l2 = float(ev_e[1]) if ev_e.size > 1 else float("nan")
    return float(ev_e[0]), l2, float(ev_o[0])


def lowest_even_vec(qmat: np.ndarray) -> np.ndarray:
    ev, evecs = np.linalg.eigh(qmat)
    v = evecs[:, int(np.argmin(ev))]
    if v[0] < 0.0:
        v = -v
    return v


def expand_mat(x, w, fmat, fgrid) -> np.ndarray:
    c = fmat.T @ (w * fgrid)
    nrm = float(np.linalg.norm(c))
    if nrm < 1e-30:
        return c
    return c / nrm


def metrics(q_even, q_odd, kappa) -> dict:
    ev_e = np.sort(np.linalg.eigvalsh(q_even))
    ev_o = np.sort(np.linalg.eigvalsh(q_odd))
    mu = float(kappa @ q_even @ kappa)
    resid = q_even @ kappa - mu * kappa
    rnorm = float(np.linalg.norm(resid))
    l1e = float(ev_e[0])
    l2e = float(ev_e[1]) if ev_e.size > 1 else float("nan")
    l1o = float(ev_o[0])
    g_even = l2e - mu
    g_odd = l1o - mu
    return {
        "mu": mu, "r": rnorm, "g_even": g_even, "g_odd": g_odd,
        "g": min(g_even, g_odd), "l1e": l1e, "l2e": l2e, "l1o": l1o,
        "theta": lowest_even_vec(q_even),
    }


def eta_of(lf: float, rnorm: float, g: float) -> float:
    if not (g > 0.0) or not math.isfinite(g) or not math.isfinite(rnorm):
        return float("nan")
    return math.sqrt(math.exp(lf)) * rnorm / g


def dk_of(rnorm: float, g: float) -> str:
    if not (g > 0.0) or not math.isfinite(g):
        return "fail"
    return "ok" if rnorm < g / 3.0 else "fail"


def rel_change(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-15)


def triple_rel(a, b) -> tuple[float, float, float]:
    return (rel_change(a[0], b[0]), rel_change(a[1], b[1]),
            rel_change(a[2], b[2]))


def triple_ok(rels, tol: float) -> bool:
    return all(math.isfinite(r) and r <= tol for r in rels)


def hat_complex(x, w, f, zs: np.ndarray) -> np.ndarray:
    return np.exp(1j * np.outer(zs, x)) @ (w * f)


def count_sign_changes(ys: np.ndarray, eps: float = 1e-14) -> int:
    n = 0
    last = 0.0
    for val in ys:
        if abs(val) < eps:
            continue
        sgn = 1.0 if val > 0.0 else -1.0
        if last != 0.0 and sgn != last:
            n += 1
        last = sgn
    return n


def offaxis_boxes(h_lo: np.ndarray, h_hi: np.ndarray) -> int:
    n = 0
    for i in range(len(h_lo) - 1):
        re = (h_lo[i].real, h_lo[i + 1].real,
              h_hi[i + 1].real, h_hi[i].real)
        im = (h_lo[i].imag, h_lo[i + 1].imag,
              h_hi[i + 1].imag, h_hi[i].imag)
        if min(re) < 0.0 < max(re) and min(im) < 0.0 < max(im):
            n += 1
    return n


def lstsq_p(log_lam: np.ndarray, log_rg: np.ndarray) -> tuple[float, float]:
    amat = np.column_stack([np.ones(len(log_lam)), log_lam])
    coef, residuals, *_ = np.linalg.lstsq(amat, log_rg, rcond=None)
    p_exp = -float(coef[1])
    if residuals.size:
        rss = float(residuals[0])
    else:
        pred = amat @ coef
        rss = float(np.sum((log_rg - pred) ** 2))
    return p_exp, rss


def fmt(x: float) -> str:
    if not math.isfinite(x):
        return "nan"
    return "%.6e" % x


def line_for(lf, disc, cand, row) -> str:
    eta = eta_of(lf, row["r"], row["g"])
    return (
        "L=%.1f lambda=%.6f disc=%s cand=%s mu=%s |r|=%s "
        "g_even=%s g_odd=%s eta=%s DK=%s l1e=%s"
        % (lf, math.exp(lf), disc, cand, fmt(row["mu"]), fmt(row["r"]),
           fmt(row["g_even"]), fmt(row["g_odd"]), fmt(eta),
           dk_of(row["r"], row["g"]), fmt(row["l1e"]))
    )


def node_label(lf: float, nodes) -> str:
    if lf <= LOG2_HALF + 1e-12:
        return "P=0 (e^{2L}<%.4f<2)" % math.exp(2.0 * lf)
    ns = ",".join(str(n) for n, _lam in nodes)
    return "P-nodes n=%s (log n<=2L)" % ns


def prefix_q(hats, wts, sig_a, sig_p, x, w, fmat, n, even: bool):
    return q_from_hats(hats[:, :n], wts, sig_a, sig_p, x, w,
                       fmat[:, :n], even)


def climb_eigs(ns, hats_e, hats_o, wts, sig_a, sig_p, x, w,
               fe, fo, lf, tag, t_cut):
    rows = []
    last = None
    stop_n = ns[0]
    succ = False
    for n in ns:
        n_e = min(n, fe.shape[1], hats_e.shape[1])
        n_o = min(n, fo.shape[1], hats_o.shape[1])
        qe = prefix_q(hats_e, wts, sig_a, sig_p, x, w, fe, n_e, True)
        qo = prefix_q(hats_o, wts, sig_a, sig_p, x, w, fo, n_o, False)
        trip = evals3(qe, qo)
        peak = (n - 1) * math.pi / lf
        cover = "yes" if t_cut >= peak else "no"
        rels = (float("nan"), float("nan"), float("nan"))
        flag = ""
        if last is not None:
            rels = triple_rel(last, trip)
            ok = triple_ok(rels, SUCC_TOL)
            flag = "ok" if ok else "FAIL"
            if ok:
                succ = True
                stop_n = n
        print("  climb L=%.1f %s N=%d tcut=%.0f l1e=%s l2e=%s l1o=%s "
              "rel=%s,%s,%s peak=%s cover=%s %s"
              % (lf, tag, n, t_cut, fmt(trip[0]), fmt(trip[1]),
                 fmt(trip[2]), fmt(rels[0]), fmt(rels[1]), fmt(rels[2]),
                 fmt(peak), cover, flag))
        rows.append((n, trip, qe, qo, n_e, n_o))
        last = trip
    return rows, stop_n, succ


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    rng = np.random.default_rng(SEED)
    _ = rng.random()
    print("connes_prolate_residual_gap_probe -- r606b")
    print("KEIN RH-CLAIM")
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("t_c", "%.15f" % T_C)
    print("k_lambda source",
          "blockreal_lemma_probe Prolate/prolate_pair/k_lambda_on_v "
          "(CCM Poisson, lam2=exp(2L), evenized); NOT a psi0 alias")
    print("psi0 source",
          "nystrom_modes_mat = vectorized kappa_high_probe.nystrom_modes "
          "sinc band t_c (r479)")
    print("prime-range", "n <= exp(2L)")
    print("float64-only", "yes")

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "literal log n")
    check("no-rh-claim",
          "NO RH CLAIM" in (__doc__ or "")
          and "KEIN RH-CLAIM" in (__doc__ or ""),
          "doc boundary")
    check("k-not-dressed-as-psi0",
          "NOT a psi0 alias" in (__doc__ or "")
          and "CCM Poisson" in (__doc__ or ""),
          "Connes k is the CCM Poisson candidate")

    if smoke:
        l_list = L_SMOKE
        s_ns = SLEPIAN_N_SMOKE
        f_ns = FOURIER_N_SMOKE
        tcuts = TCUT_SMOKE
        t_work = 400.0
        x_hi, x_step = 30.0, 1.0
        y_grid = (0.0, 0.45)
    else:
        l_list = L_FULL
        s_ns = SLEPIAN_N_FULL
        f_ns = FOURIER_N_FULL
        tcuts = TCUT_FULL
        t_work = 400.0
        x_hi, x_step = 30.0, 0.25
        y_grid = (0.0, 0.25, 0.45)

    print("ladder slepian", ",".join(str(n) for n in s_ns),
          "fourier", ",".join(str(n) for n in f_ns),
          "tcut", ",".join("%.0f" % t for t in tcuts),
          "t_work", "%.0f" % t_work)

    table: dict[tuple, dict] = {}
    conv_at: dict[float, dict] = {}
    nreal_by_l: dict[float, int] = {}
    sup_by_l: dict[float, float] = {}
    slepian_ev0_03 = None
    xs_strip = np.arange(-x_hi, x_hi + 0.5 * x_step, x_step)

    for lf in l_list:
        nodes = E.prime_nodes(lf)
        om_p = omega_p_of(nodes)
        print("  nodes L=%.1f %s" % (lf, node_label(lf, nodes)))
        f_ns_use = tuple(n for n in f_ns
                         if (n - 1) * math.pi / lf <= t_work + 1e-12)
        if len(f_ns_use) < 2:
            f_ns_use = tuple(f_ns[:2])
        print("  fourier-allowed L=%.1f N=%s (peak<=t_work)"
              % (lf, ",".join(str(n) for n in f_ns_use)))
        n_ny_s = n_ny_for(lf, max(s_ns), t_work, "slepian")
        n_ny_f = n_ny_for(lf, max(f_ns_use), t_work, "fourier")
        # one spatial grid per disc, sized for the workhorse t_cut
        ev_k, xs, ws, fsl = nystrom_modes_mat(lf, T_C, n_ny_s)
        if abs(lf - 0.3) < 1e-12:
            slepian_ev0_03 = float(ev_k[0])
        fe_s = fsl[:, 0::2]
        fo_s = fsl[:, 1::2]
        conc = " ".join("%.3e" % float(ev_k[2 * i])
                        for i in range(min(max(s_ns), fe_s.shape[1])))
        print("  slepian-even-conc L=%.1f %s" % (lf, conc))

        xfr, wfr = np.polynomial.legendre.leggauss(n_ny_f)
        xf, wf = lf * xfr, lf * wfr
        fe_f = fourier_even_mat(xf, wf, lf, max(f_ns_use))
        fo_f = fourier_odd_mat(xf, wf, lf, max(f_ns_use))

        nt_w = nt_for(t_work, lf, om_p)
        ts_w, wts_w, sa_w, sp_w = t_grid(t_work, nt_w, nodes)
        dt = float(ts_w[1] - ts_w[0])
        marg_p = (math.pi / dt) / om_p if om_p > 0.0 else float("inf")
        need_x = 2.0 * t_work * lf / math.pi
        marg_xs = n_ny_s / max(need_x, 1e-15)
        marg_xf = n_ny_f / max(need_x, 1e-15)
        print("  nyquist L=%.1f omega_P=%s dt=%s nt=%d margin_P=%s "
              "n_ny_s=%d n_ny_f=%d need_x=%s margin_xS=%s margin_xF=%s"
              % (lf, fmt(om_p), fmt(dt), nt_w, fmt(marg_p),
                 n_ny_s, n_ny_f, fmt(need_x), fmt(marg_xs), fmt(marg_xf)))

        hats_se = hat_mat(xs, ws, fe_s[:, :max(s_ns)], ts_w)
        hats_so = hat_mat(xs, ws, fo_s[:, :max(s_ns)], ts_w)
        hats_fe = hat_mat(xf, wf, fe_f, ts_w)
        hats_fo = hat_mat(xf, wf, fo_f, ts_w)

        s_rows, s_n, s_ok = climb_eigs(
            s_ns, hats_se, hats_so, wts_w, sa_w, sp_w, xs, ws,
            fe_s, fo_s, lf, "slepian", t_work)
        f_rows, f_n, f_ok = climb_eigs(
            f_ns_use, hats_fe, hats_fo, wts_w, sa_w, sp_w, xf, wf,
            fe_f, fo_f, lf, "fourier", t_work)

        # t_cut ladder at the stopped N (or last)
        s_pick = next(r for r in s_rows if r[0] == s_n)
        f_pick = next(r for r in f_rows if r[0] == f_n)
        tcut_ok = True
        for tag, n_use, xg, wg, fe, fo, n_e, n_o in (
            ("slepian", s_n, xs, ws, fe_s, fo_s, s_pick[4], s_pick[5]),
            ("fourier", f_n, xf, wf, fe_f, fo_f, f_pick[4], f_pick[5]),
        ):
            trips = []
            n_ny_here = len(xg)
            for tc in tcuts:
                need = 2.0 * tc * lf / math.pi
                peak = (n_use - 1) * math.pi / lf
                if n_ny_here < need:
                    print("  tcut L=%.1f %s N=%d tcut=%.0f SKIP "
                          "spatial Nyquist n_ny=%d need=%s"
                          % (lf, tag, n_use, tc, n_ny_here, fmt(need)))
                    continue
                if tc < peak:
                    print("  tcut L=%.1f %s N=%d tcut=%.0f SKIP "
                          "peak=%s uncovered"
                          % (lf, tag, n_use, tc, fmt(peak)))
                    continue
                ntt = nt_for(tc, lf, om_p)
                ts, wts, sa, sp = t_grid(tc, ntt, nodes)
                he = hat_mat(xg, wg, fe[:, :n_e], ts)
                ho = hat_mat(xg, wg, fo[:, :n_o], ts)
                qe = q_from_hats(he, wts, sa, sp, xg, wg, fe[:, :n_e], True)
                qo = q_from_hats(ho, wts, sa, sp, xg, wg, fo[:, :n_o], False)
                trip = evals3(qe, qo)
                trips.append((tc, trip, qe, qo))
                print("  tcut L=%.1f %s N=%d tcut=%.0f l1e=%s l2e=%s l1o=%s"
                      % (lf, tag, n_use, tc, fmt(trip[0]), fmt(trip[1]),
                         fmt(trip[2])))
            # 400 vs 1000 or last two
            if len(trips) >= 2:
                rels = triple_rel(trips[-2][1], trips[-1][1])
                ok_t = triple_ok(rels, SUCC_TOL)
                tcut_ok = tcut_ok and ok_t
                print("  tcut-succ L=%.1f %s rel=%s,%s,%s %s"
                      % (lf, tag, fmt(rels[0]), fmt(rels[1]), fmt(rels[2]),
                         "ok" if ok_t else "FAIL"))
            elif len(trips) == 1:
                print("  tcut-succ L=%.1f %s only-one-resolved" % (lf, tag))
            if trips:
                qe_use, qo_use = trips[-1][2], trips[-1][3]
                trip_use = trips[-1][1]
                tcut_use = trips[-1][0]
            elif tag == "slepian":
                qe_use, qo_use = s_pick[2], s_pick[3]
                trip_use = s_pick[1]
                tcut_use = t_work
            else:
                qe_use, qo_use = f_pick[2], f_pick[3]
                trip_use = f_pick[1]
                tcut_use = t_work
            if tag == "slepian":
                s_qe, s_qo, s_trip, s_tcut = (
                    qe_use, qo_use, trip_use, tcut_use)
            else:
                f_qe, f_qo, f_trip, f_tcut = (
                    qe_use, qo_use, trip_use, tcut_use)

        cross_e = triple_rel(s_trip, f_trip)
        cross_e_ok = triple_ok(cross_e, CROSS_TOL)
        print("  eval-cross L=%.1f l1e,l2e,l1o rel=%s,%s,%s %s"
              % (lf, fmt(cross_e[0]), fmt(cross_e[1]), fmt(cross_e[2]),
                 "ok" if cross_e_ok else "FAIL"))

        converged = bool(s_ok and f_ok and tcut_ok and cross_e_ok)
        wall = ""
        if not converged:
            bits = []
            if not s_ok:
                bits.append("slepian-succ>1pct")
            if not f_ok:
                bits.append("fourier-succ>1pct")
            if not tcut_ok:
                bits.append("tcut-succ>1pct")
            if not cross_e_ok:
                bits.append("eval-cross>5pct")
            wall = ",".join(bits)
        print("  CONV L=%.1f slepian N=%d tcut=%.0f fourier N=%d tcut=%.0f "
              "l1e_S=%s l1e_F=%s %s"
              % (lf, s_n, s_tcut, f_n, f_tcut, fmt(s_trip[0]),
                 fmt(f_trip[0]),
                 "CONVERGED" if converged else ("WALL " + wall)))

        if (abs(lf - 0.6) < 1e-12 or abs(lf - 0.7) < 1e-12
                or abs(lf - 0.8) < 1e-12):
            for tag, l1 in (("slepian", s_trip[0]), ("fourier", f_trip[0])):
                sign = "pos" if l1 > 0.0 else "neg"
                note = ""
                if converged and l1 <= 0.0:
                    note = " CHUK-CONFLICT insufficient-basis-or-probe-bug"
                print("  l1e-sign L=%.1f %s %s l1e=%s%s"
                      % (lf, tag, sign, fmt(l1), note))

        k_s = connes_k_on_grid(lf, xs, ws)
        k_f = connes_k_on_grid(lf, xf, wf)
        p0_s = fix_sign_grid(xs, fe_s[:, 0])
        p0_f = fix_sign_grid(xf, fe_f[:, 0])
        for dname, qe, qo, xg, wg, fe, kgrid, p0 in (
            ("slepian", s_qe, s_qo, xs, ws, fe_s[:, :s_pick[4]], k_s, p0_s),
            ("fourier", f_qe, f_qo, xf, wf, fe_f[:, :f_pick[4]], k_f, p0_f),
        ):
            for cname, cgrid in (("k", kgrid), ("psi0", p0)):
                kap = expand_mat(xg, wg, fe, cgrid)
                row = metrics(qe, qo, kap)
                table[(lf, dname, cname)] = row
                table[(lf, dname, cname, "F")] = fe
                table[(lf, dname, cname, "x")] = xg
                table[(lf, dname, cname, "w")] = wg
                table[(lf, dname, cname, "cgrid")] = cgrid
                print("  " + line_for(lf, dname, cname, row))

        conv_at[lf] = {
            "ok": converged, "wall": wall, "s_n": s_n, "f_n": f_n,
            "s_tcut": s_tcut, "f_tcut": f_tcut,
            "s_l1e": s_trip[0], "f_l1e": f_trip[0],
            "s_ok": s_ok, "f_ok": f_ok, "cross": cross_e_ok,
        }

        # Strip on Slepian evec vs k at the stopped Slepian size.
        row_th = table[(lf, "slepian", "k")]
        theta_c = row_th["theta"]
        fe_use = fe_s[:, :s_pick[4]]
        theta_g = fix_sign_grid(xs, fe_use @ theta_c)
        tn = math.sqrt(max(float(np.sum(ws * theta_g * theta_g)), 1e-30))
        theta_g = theta_g / tn
        hats_th = [hat_complex(xs, ws, theta_g, xs_strip + 1j * yv)
                   for yv in y_grid]
        hats_k = [hat_complex(xs, ws, k_s, xs_strip + 1j * yv)
                  for yv in y_grid]
        sups = [float(np.max(np.abs(ht - hk)))
                for ht, hk in zip(hats_th, hats_k)]
        sup_all = max(sups)
        sup_by_l[lf] = sup_all
        mask = (xs_strip >= 0.0) & (xs_strip <= 30.0)
        nreal = count_sign_changes(hats_th[0].real[mask])
        nreal_by_l[lf] = nreal
        nbox = 0
        if len(y_grid) >= 3:
            nbox = offaxis_boxes(hats_th[1], hats_th[2])
        print("  strip L=%.1f sup|that-khat|=%s nreal[0,30]=%d nref_lt30=%d "
              "offaxis_boxes=%d"
              % (lf, fmt(sup_all), nreal, N_REF_LT30, nbox))

    # Candidate cross-disc
    disagree = []
    for lf in l_list:
        for cname in ("k", "psi0"):
            a = table[(lf, "slepian", cname)]
            b = table[(lf, "fourier", cname)]
            rels = {
                "mu": rel_change(a["mu"], b["mu"]),
                "g": rel_change(a["g"], b["g"]),
            }
            ea = eta_of(lf, a["r"], a["g"])
            eb = eta_of(lf, b["r"], b["g"])
            rels["eta"] = (rel_change(ea, eb)
                           if math.isfinite(ea) and math.isfinite(eb)
                           else float("nan"))
            bad = any(math.isfinite(rels[k]) and rels[k] > CROSS_TOL
                      for k in ("mu", "g", "eta"))
            print("  cross L=%.1f cand=%s mu_rel=%s g_rel=%s eta_rel=%s %s"
                  % (lf, cname, fmt(rels["mu"]), fmt(rels["g"]),
                     fmt(rels["eta"]), "FAIL" if bad else "ok"))
            if bad:
                disagree.append((lf, cname))

    train_ls = [lf for lf in l_list if lf in L_TRAIN]
    hold_ls = [lf for lf in l_list if lf in L_HOLDOUT]
    conv_train = [lf for lf in train_ls if conv_at[lf]["ok"]]
    conv_hold = [lf for lf in hold_ls if conv_at[lf]["ok"]]
    conv_all = [lf for lf in l_list if conv_at[lf]["ok"]]
    lmax_conv = max(conv_all) if conv_all else float("nan")
    print("conv-Lmax", "nan" if not conv_all else "%.1f" % lmax_conv)
    print("N-growth",
          " ".join("L=%.1f:Ns=%d Nf=%d%s" % (
              lf, conv_at[lf]["s_n"], conv_at[lf]["f_n"],
              "" if conv_at[lf]["ok"] else "/WALL")
                   for lf in l_list))

    fit_p = float("nan")
    fit_rss = float("nan")
    hold_err = float("nan")
    rg_decreases = False
    g_all_pos = True
    dk_hold = True
    p_nonpos = False

    # Fit on converged training L only (need >=4 for a full verdict).
    def series(disc, cand, lseq):
        xs, ys, rgs, gs, dks = [], [], [], [], []
        for lf in lseq:
            row = table[(lf, disc, cand)]
            g = row["g"]
            r = row["r"]
            gs.append(g)
            dks.append(dk_of(r, g))
            if g > 0.0 and r > 0.0 and math.isfinite(g) and math.isfinite(r):
                xs.append(float(lf))
                ys.append(math.log(r / g))
                rgs.append(r / g)
            else:
                xs.append(float("nan"))
                ys.append(float("nan"))
                rgs.append(float("nan"))
        return xs, ys, rgs, gs, dks

    fit_ls = conv_train if conv_train else train_ls
    hold_fit = conv_hold if conv_train else hold_ls
    xs, ys, rgs, gs, dks = series("slepian", "k", fit_ls + hold_fit)
    g_all_pos = all(
        table[(lf, "slepian", "k")]["g"] > 0.0 for lf in l_list)
    n_tr = len(fit_ls)
    tr_x = np.array([xs[i] for i in range(n_tr) if math.isfinite(ys[i])])
    tr_y = np.array([ys[i] for i in range(n_tr) if math.isfinite(ys[i])])
    tr_rg = [rgs[i] for i in range(n_tr) if math.isfinite(rgs[i])]
    if len(tr_rg) >= 2:
        rg_decreases = tr_rg[-1] < tr_rg[0]
    if len(tr_x) >= 2:
        # x stored as L; log lambda = L
        fit_p, fit_rss = lstsq_p(tr_x, tr_y)
        p_nonpos = fit_p <= 0.0
        intercept = float(np.mean(tr_y + fit_p * tr_x))
        hold_rel = []
        for i, lf in enumerate(hold_fit):
            j = n_tr + i
            if j >= len(rgs) or not math.isfinite(rgs[j]):
                continue
            pred = math.exp(intercept - fit_p * xs[j])
            meas = rgs[j]
            if meas == 0.0:
                continue
            hold_rel.append(abs(pred - meas) / abs(meas))
        if hold_fit and hold_rel:
            hold_err = max(hold_rel)
        elif hold_fit:
            hold_err = float("nan")
            dk_hold = False
        for i, lf in enumerate(hold_fit):
            j = n_tr + i
            if j < len(dks) and dks[j] != "ok":
                dk_hold = False
        if not hold_fit:
            dk_hold = False
    else:
        dk_hold = False

    print("fit disc=slepian cand=k p=%s rss=%s holdout_relerr=%s "
          "rg_decreases=%s ntrain_used=%d"
          % (fmt(fit_p), fmt(fit_rss), fmt(hold_err),
             "yes" if rg_decreases else "no", len(tr_x)))
    print("fit g_all_pos=%s DK_holdout=%s"
          % ("yes" if g_all_pos else "no",
             "ok" if dk_hold else "fail"))

    if slepian_ev0_03 is not None:
        check("leiter-l0",
              0.8593 < slepian_ev0_03 < 0.8595,
              "psi0 Slepian ev0=%.6e at L=0.3" % slepian_ev0_03)

    eval_conv = all(conv_at[lf]["ok"] for lf in l_list)
    cross_ok = not disagree
    print("eigen-converged", "yes" if eval_conv else "no")
    print("cross-disc", "yes" if cross_ok else "no (%d flags)" % len(disagree))

    l_sorted = sorted(sup_by_l)
    strip_dec = False
    if len(l_sorted) >= 2:
        strip_dec = sup_by_l[l_sorted[-1]] < sup_by_l[l_sorted[0]]
    print("strip-monotone-sup", "yes" if strip_dec else "no",
          "Lmin=%s Lmax=%s" % (
              fmt(sup_by_l[l_sorted[0]]) if l_sorted else "nan",
              fmt(sup_by_l[l_sorted[-1]]) if l_sorted else "nan"))
    print("theta-real-zeros",
          " ".join("L=%.1f:%d" % (lf, nreal_by_l[lf]) for lf in l_list))
    nreal_vals = [nreal_by_l[lf] for lf in l_list]
    tends = (len(nreal_vals) >= 2
             and nreal_vals[-1] == N_REF_LT30
             and all(v >= N_REF_LT30 for v in nreal_vals))
    print("nreal-tends-to-nref", "yes" if tends else "no",
          "nref_lt30=%d" % N_REF_LT30)

    if smoke:
        verdict = "INCONCLUSIVE"
        reason = "smoke-no-holdout"
    elif (not eval_conv) or (not cross_ok):
        verdict = "INCONCLUSIVE"
        bits = []
        if not eval_conv:
            bits.append("evals-not-converged")
        if not cross_ok:
            bits.append("disc-disagree>5pct")
        if len(conv_train) < 4 and not smoke:
            bits.append("train-unconverged n=%d need=4" % len(conv_train))
        reason = ",".join(bits)
    elif (not g_all_pos) or p_nonpos:
        verdict = "STOP"
        reason = "g<=0" if not g_all_pos else "p<=0"
    elif (g_all_pos and dk_hold and math.isfinite(fit_p)
          and fit_p > P_GO and math.isfinite(hold_err)
          and hold_err <= HOLDOUT_TOL):
        verdict = "GO"
        reason = "g>0,DK-holdout,p>0.55,holdout<=20pct"
    elif rg_decreases and (fit_p <= P_PARTIAL or not (
            math.isfinite(hold_err) and hold_err <= HOLDOUT_TOL
            and dk_hold)):
        verdict = "PARTIAL"
        reason = ("rg-decreases,p<=0.5" if fit_p <= P_PARTIAL
                  else "rg-decreases,holdout-miss")
    else:
        verdict = "PARTIAL"
        reason = "no-GO-clause"

    check("type-not-proved", True, "measurement; not a SATZ")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("CHECKS %d/%d" % (n_pass, n_pass + n_fail))
    print("VERDICT: %s(%s)" % (verdict, reason))
    print("SPEC %s" % SPEC_SHA[:16])
    return 0 if n_fail == 0 else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
