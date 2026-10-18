#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""certificate_class_atlas_probe -- PRIME.CERTIFICATE.ATLAS.01 (r629).

EXPLORATION ONLY.  experiments/tfpt-discovery sandbox.  NO promotion,
NO ledger/paper/website/next.txt/rh/ edit, NO RH CLAIM.

Certificate-class atlas: for each CLASS of inputs, the maximal
fraction of zeros that could be off the line or non-simple while
matching those inputs, via a linear program on a discretized
zero/spectral measure.  Machinery copied (not imported) from
inertia_highermoment_probe.py (r616) and the r267 reconstruction
in ranktrace_adjudication_probe.py.  A3 windows copy the
edge-damped Legendre convention of r619 (support_relay_census).

Rows
  A1  Two trace moments, bandwidth one (Alpoge--Furman class).
      Gate: max off-line = 1-p0 with p0 = 0.6818287 (LawN256).
  A2  A1 + Riemann--von Mangoldt N(T) with an explicit S(T) bound.
  A3  A1 + prime-free-window Weil positivity (Connes--Consani 2021)
      on an edge-damped Legendre basis, N <= 24, supp f subset
      [-log 2 / 2, log 2 / 2] ~ [-0.3466, 0.3466].  Off-line
      quadruple uses 2 Re[fhat(1/2+sig+i g) conj(fhat(1/2-sig+i g))].
      Parent: redundant (r619 L_det >= 0.5; these windows are
      zero-blind).  Measure |opt_A3-opt_A1| <= 1e-6?
  A4  A1 + k-level GUE moments, k = 3, 4 (r616 check:
      0.75 -> 5/6 -> 31/36).
  A5  A1 + pair correlation beyond support 1, Montgomery strength
      alpha_max in {1, 1.5, 2, inf}.  Conditional for alpha_max > 1.
  A6  A1 + Huxley/Ingham N(sig, T) << T^{12(1-sig)/5} log^c T,
      as a per-slice cap.  Off-line mass with sig >= 1/12 is
      forced to a zero fraction at T = inf; report the shift.

Zeros of zeta are not LP data.  Model sanity is the sigma -> 0
limit of the off-line kernel, not an ordinate table.

NO RH CLAIM IN EITHER DIRECTION.
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
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import linprog

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

# ---------------------------------------------------------------------------
# Frozen spec.  SPEC_SHA = sha256 of canonical JSON(SPEC).
# ---------------------------------------------------------------------------
P0_NUM = 10909258999421303588095230195816054408197
P0_DEN = 16000000000000000000000000000000000000000
R267_CEIL_P0 = 0.6818287
TARGET_CEIL = 0.6818
PROP_23 = 2.0 / 3.0
GUE_MOMENTS = (1.0, 4.0 / 3.0, 2.0, 13.0 / 4.0)
L_PF = 0.5 * math.log(2.0)
L_PF_LABEL = 0.3466
HUXLEY_EXP = 12.0 / 5.0
HUXLEY_CUT = 1.0 / 12.0
ALPHA_MAX_LIST = (1.0, 1.5, 2.0, float("inf"))
T_RVM = 1.0e12
N_BASIS_FULL = 24
N_BASIS_SMOKE = 8
DAMP_POWER = 3
FENCE = (
    "Certificate-class atlas; conditional rows are not claims; no RH claim."
)

# Exact theorem statements consumed as inputs (not re-proved here).
CITATIONS = (
    {
        "row": "A1",
        "uncond": True,
        "who": "Alpoge-Furman",
        "year": 2026,
        "ref": "arXiv:2608.13637; Lean Zeta23.PairCeiling.ceiling_law256 / LawN256",
        "statement": (
            "Unconditionally, at least 2/3 of the nontrivial zeros of "
            "zeta are simple and on the critical line, via a rank-trace "
            "inequality on a bandwidth-one Gabor compression of Weil's "
            "form (tr G ~ N, ||G||_HS^2 ~ R(psi) N, R(psi_0)=4/3).  Any "
            "certificate that consumes only those two trace moments "
            "against bandwidth-one test functions plus the on/off block "
            "partition is bounded by the configuration ceiling "
            "p0 = 0.6818287 (N=256 marked-configuration law; p0 := 1-a_N)."
        ),
    },
    {
        "row": "A2",
        "uncond": True,
        "who": "Riemann-von Mangoldt + Bellotti / Trudgian / Platt",
        "year": 2025,
        "ref": (
            "classical N(T); Bellotti Math. Comp. 2025 Cor. 1.5 "
            "arXiv:2412.15470; Trudgian JNT 134 (2014) Thm 1; "
            "Platt Math. Comp. 86 (2017) / LMFDB isolation"
        ),
        "statement": (
            "N(T) = (T/2pi) log(T/2pi) - T/2pi + 7/8 + S(T) + O(1/T), "
            "S(T) = (1/pi) arg zeta(1/2+iT).  Unconditional pointwise: "
            "|S(T)| <= 0.10076 log T + min{0.24460 loglog T + 7.20844, "
            "1.68845 loglog T + 1.50956} for T >= e (Bellotti Cor. 1.5); "
            "|S(T)| <= 0.112 log T + 0.278 loglog T + 2.510, T >= e "
            "(Trudgian 2014 Thm 1); |S(T)| <= 2.5167 for "
            "0 <= T <= 30610046000 (Platt isolation)."
        ),
    },
    {
        "row": "A3",
        "uncond": True,
        "who": "Connes-Consani / Bombieri / Yoshida",
        "year": 2021,
        "ref": (
            "Connes-Consani arXiv:2008.10974 (2021); Bombieri, Remarks "
            "on Weil's quadratic functional, Atti Accad. Naz. Lincei 11 "
            "(2000); Yoshida 1992 Hermitian forms attached to zeta"
        ),
        "statement": (
            "If supp f subset (-L, L) with L = (log 2)/2 ~ 0.3466, then "
            "h = f * ftilde has supp h subset (-log 2, log 2), so the "
            "Weil prime sum vanishes (no prime power in the interior of "
            "the support of h).  The Weil quadratic form Q(f) = Pole + "
            "Arch is then unconditionally nonnegative, and the explicit "
            "formula gives Sigma_rho hat h(rho) >= 0 for every such f.  "
            "Off-line quadruple kernel used here: "
            "2 Re[fhat(1/2+sig+ig) conj(fhat(1/2-sig+ig))]."
        ),
    },
    {
        "row": "A4",
        "uncond": False,
        "who": "GUE / sine-kernel Gram (Alpoge-Furman s7.2(f); r616)",
        "year": 2026,
        "ref": "arXiv:2608.13637 s7.2(f); inertia_highermoment_probe r616",
        "statement": (
            "CONDITIONAL.  Ideal-input trace moments of the bandwidth-one "
            "compression against the sine process: (m1,m2,m3,m4) = "
            "(1, 4/3, 2, 13/4).  Not an unconditional input at bandwidth "
            "one (Rudnick-Sarnak needs sum |xi_j| < 2; three frequencies "
            "of size 1 overshoot).  CMS/grid LP n_+ : 3/4, 5/6, 31/36."
        ),
    },
    {
        "row": "A5",
        "uncond": False,
        "who": "Montgomery pair-correlation conjecture (strength alpha_max)",
        "year": 1973,
        "ref": "Montgomery, Proc. Sympos. Pure Math. 24 (1973), 181-193",
        "statement": (
            "On |alpha| < 1, F(alpha) ~ |alpha| is the bandwidth-one "
            "input (RH for Montgomery's original form; the A-F prime-side "
            "second moment is unconditional at support 1).  The conjecture "
            "F(alpha) = 1 for |alpha| >= 1 is CONDITIONAL.  Rows with "
            "alpha_max > 1 pin F to the GUE form factor on [-alpha_max, "
            "alpha_max] and tighten the simple-on-line floor from p0 "
            "toward the k=2 GUE CMS value 3/4.  Not a theorem."
        ),
    },
    {
        "row": "A6",
        "uncond": True,
        "who": "Ingham / Huxley zero-density",
        "year": 1972,
        "ref": (
            "Ingham, Quart. J. Math. Oxford 11 (1940); Huxley, large "
            "values of Dirichlet polynomials / zero-density N(sig,T) << "
            "T^{12(1-sig)/5} (log T)^{44}; Ivic, The Riemann Zeta-Function, "
            "Ch. 11"
        ),
        "statement": (
            "Unconditionally, writing sig for the classical abscissa in "
            "[1/2, 1], N(sig, T) << T^{12(1-sig)/5} (log T)^c (Huxley).  "
            "Ingham's form is N(sig,T) << T^{3(1-sig)/(2-sig)} (log T)^5.  "
            "The Huxley exponent is < 1 precisely when the distance to "
            "the critical line exceeds 1/12.  Implied constants are not "
            "consumed; the LP uses the T -> inf exponent sign only."
        ),
    },
)

SPEC = {
    "round": 629,
    "contract": "PRIME.CERTIFICATE.ATLAS.01",
    "parent_rounds": [267, 616, 619],
    "parent_probes": [
        "ranktrace_adjudication_probe.py",
        "inertia_highermoment_probe.py",
        "support_relay_census_probe.py",
    ],
    "p0_num": str(P0_NUM),
    "p0_den": str(P0_DEN),
    "r267_ceil_p0": R267_CEIL_P0,
    "gue_moments": list(GUE_MOMENTS),
    "L_pf": "log(2)/2",
    "L_pf_label": L_PF_LABEL,
    "n_basis_full": N_BASIS_FULL,
    "damp_power": DAMP_POWER,
    "huxley_exp": HUXLEY_EXP,
    "huxley_cut": HUXLEY_CUT,
    "alpha_max": ["1", "1.5", "2", "inf"],
    "T_rvm": T_RVM,
    "citations": [
        {
            "row": row["row"],
            "uncond": row["uncond"],
            "who": row["who"],
            "year": row["year"],
        }
        for row in CITATIONS
    ],
    "scope": "certificate-class LP atlas over discretized zero measures",
    "excluded": "RH claim; zeros as LP data; promotion; ledger/paper",
    "fence": FENCE,
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool, str]] = []
T0 = time.time()


def check(name: str, ok: bool, detail: str = "") -> bool:
    okb = bool(ok)
    CHECKS.append((name, okb, detail))
    print(
        "  [%s] %-44s %s" % ("PASS" if okb else "FAIL", name, detail),
        flush=True,
    )
    return okb


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def payload_sha(obj: object) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def firewall_audit() -> tuple[bool, str]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    forb = {
        "zeta" + "zero",
        "n" + "zeros",
        "prime" + "range",
        "is" + "prime",
        "gram" + "point",
        "mpmath",
    }
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None
        )
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), (
        "NO zero/prime oracles in the LP; r616 kernel + A-F p0 "
        "rational + Weil hats on a density weight only"
        if not bad else "; ".join(bad)
    )


# ---------------- r616 R(psi) quadrature (verbatim construction)
def _gl_map(x, w, a, b):
    xm = 0.5 * (b - a) * x + 0.5 * (a + b)
    wm = 0.5 * (b - a) * w
    return xm, wm


def r_window(psi, gl_n: int) -> float:
    """R(psi) by nested Gauss--Legendre; |u-v| kink split at u=v."""
    x, w = leggauss(gl_n)
    u, wu = _gl_map(x, w, -0.5, 0.5)
    pu = np.array([psi(t) for t in u], dtype=float)
    i_psi = float(np.sum(wu * pu))
    i_psi2 = float(np.sum(wu * pu * pu))
    dbl = 0.0
    for uk, wk, pk in zip(u, wu, pu):
        v, wv = _gl_map(x, w, -0.5, uk)
        pv = np.array([psi(t) for t in v], dtype=float)
        dbl += wk * pk * float(np.sum(wv * (uk - v) * pv))
    dbl *= 2.0
    return (i_psi2 + dbl) / (i_psi * i_psi)


def montgomery_symbol_moments(n_fft: int) -> tuple[float, ...]:
    """Eigenvalue moments of the bandwidth-one |alpha|-symbol,
    scaled to m1=1, m2=4/3 (r267 diagonal + off-diagonal prime sum).
    """
    freq = np.fft.fftfreq(n_fft)
    alpha = 2.0 * freq
    form = np.abs(alpha)
    form0 = form - float(form.mean())
    var = float(np.mean(form0 * form0))
    gain = math.sqrt((4.0 / 3.0 - 1.0) / var)
    sig = 1.0 + gain * form0
    return tuple(float(np.mean(sig ** p)) for p in range(1, 5))


def christoffel_k2(m1: float, m2: float) -> tuple[float, float]:
    lam = 1.0 - (m1 * m1) / m2
    return lam, 1.0 - lam


def christoffel_k4(
    m1: float, m2: float, m3: float, m4: float,
) -> tuple[float, float]:
    a_mat = np.array([[m2, m3], [m3, m4]], dtype=float)
    rhs = np.array([-m1, -m2], dtype=float)
    try:
        ab = np.linalg.solve(a_mat, rhs)
    except np.linalg.LinAlgError:
        return float("nan"), float("nan")
    a, b = float(ab[0]), float(ab[1])
    lam = (
        1.0 + 2.0 * a * m1 + (a * a + 2.0 * b) * m2
        + 2.0 * a * b * m3 + b * b * m4
    )
    return lam, 1.0 - lam


def inertia_lp(
    moments: tuple[float, ...],
    k: int,
    lam: np.ndarray,
    include_zero: bool = True,
) -> dict:
    """Max nonpositive mass given m_1..m_k.  Copied from r616."""
    lam = np.asarray(lam, dtype=float)
    n = int(lam.size)
    if include_zero:
        c = -np.array([1.0 if x <= 1e-14 else 0.0 for x in lam])
    else:
        c = -np.array([1.0 if x < -1e-14 else 0.0 for x in lam])
    a_eq = np.vstack([np.ones(n)] + [lam ** j for j in range(1, k + 1)])
    b_eq = np.array([1.0] + [float(moments[j - 1]) for j in range(1, k + 1)])
    res = linprog(
        c, A_eq=a_eq, b_eq=b_eq, bounds=[(0.0, None)] * n,
        method="highs",
    )
    if not res.success:
        return dict(
            ok=False, p=float("nan"), nfrac=float("nan"),
            msg=str(res.message),
        )
    nfrac = float(-res.fun)
    return dict(ok=True, p=1.0 - nfrac, nfrac=nfrac, msg="optimal")


def s_bound_bellotti(t: float) -> float:
    """Bellotti 2025 Cor. 1.5, T >= e.  Unconditional."""
    lg = math.log(t)
    llg = math.log(lg)
    branch = min(0.24460 * llg + 7.20844, 1.68845 * llg + 1.50956)
    return 0.10076 * lg + branch


def rvm_main(t: float) -> float:
    """Riemann--von Mangoldt main term (T/2pi) log(T/2pi) - T/2pi + 7/8."""
    twopi = 2.0 * math.pi
    return (t / twopi) * math.log(t / twopi) - t / twopi + 0.875


def a5_s_floor(alpha_max: float, p0: float) -> float:
    """Montgomery-strength floor: p0 at support 1, 3/4 at full GUE pairs."""
    if alpha_max <= 1.0 + 1e-15:
        return p0
    if not math.isfinite(alpha_max):
        return 0.75
    weight = 1.0 - 1.0 / float(alpha_max)
    return p0 + (0.75 - p0) * weight


def damped_legendre_basis(u: np.ndarray, length: float, n_basis: int) -> np.ndarray:
    """Edge-damped Legendre on [-L, L]: (1-(u/L)^2)^3 P_n(u/L), scaled."""
    x = np.clip(u / length, -1.0, 1.0)
    damp = (1.0 - x * x) ** DAMP_POWER
    vals = np.zeros((u.size, n_basis), dtype=float)
    vals[:, 0] = 1.0
    if n_basis > 1:
        vals[:, 1] = x
    for degree in range(1, n_basis - 1):
        vals[:, degree + 1] = (
            ((2 * degree + 1) * x * vals[:, degree] - degree * vals[:, degree - 1])
            / (degree + 1)
        )
    scales = np.sqrt((np.arange(n_basis, dtype=float) + 0.5) / length)
    return (damp[:, None] * vals) * scales[None, :]


def weil_kernel_matrix(
    length: float,
    n_basis: int,
    sigma: np.ndarray,
    gamma: np.ndarray,
    gamma_w: np.ndarray,
    gl_n: int,
) -> dict:
    """On-line 2|fhat|^2 and off-line 2 Re[fhat(sig) conj(fhat(-sig))],
    averaged in gamma against a Riemann--von Mangoldt density weight.
    No ordinates: gamma is a fixed quadrature grid.
    """
    nodes, weights = leggauss(gl_n)
    u = length * nodes
    wu = length * weights
    basis = damped_legendre_basis(u, length, n_basis)
    tilt0 = np.exp(0.5 * u)
    on_acc = np.zeros(n_basis, dtype=float)
    off_acc = np.zeros((n_basis, sigma.size), dtype=float)
    wsum = float(np.sum(gamma_w))
    wnorm = 1.0 / wsum if wsum > 0.0 else 1.0
    for g_val, g_w in zip(gamma, gamma_w):
        phase = np.exp(1j * g_val * u) * tilt0
        hat0 = (wu * phase) @ basis
        on_acc += float(g_w) * 2.0 * np.abs(hat0) ** 2
        for i_s, sig in enumerate(sigma):
            hat_p = (wu * phase * np.exp(sig * u)) @ basis
            hat_m = (wu * phase * np.exp(-sig * u)) @ basis
            off_acc[:, i_s] += float(g_w) * 2.0 * np.real(hat_p * np.conj(hat_m))
    on_acc *= wnorm
    off_acc *= wnorm
    return dict(on_line=on_acc, off_line=off_acc)


def _solve_linprog(c, a_eq, b_eq, a_ub, b_ub, n_var: int) -> dict:
    kwargs = dict(
        c=c, bounds=[(0.0, None)] * n_var, method="highs",
    )
    if a_eq is not None:
        kwargs["A_eq"] = a_eq
        kwargs["b_eq"] = b_eq
    if a_ub is not None and len(a_ub) > 0:
        kwargs["A_ub"] = np.asarray(a_ub, dtype=float)
        kwargs["b_ub"] = np.asarray(b_ub, dtype=float)
    res = linprog(**kwargs)
    if not res.success:
        return dict(
            ok=False, off=float("nan"), x=None, msg=str(res.message),
        )
    x = np.asarray(res.x, dtype=float)
    return dict(ok=True, off=float(-res.fun), x=x, msg="optimal")


def config_lp(
    n_sigma: int,
    s_floor: float,
    caps_o: np.ndarray | None = None,
    extra_ub: list | None = None,
) -> dict:
    """Max m + sum o_i  s.t. s+m+sum o = 1, s >= s_floor, 0 <= o_i <= cap."""
    n = 2 + n_sigma
    c = np.zeros(n)
    c[1:] = -1.0
    a_eq = np.ones((1, n))
    b_eq = np.array([1.0])
    a_ub = [np.zeros(n)]
    a_ub[0][0] = -1.0
    b_ub = [-float(s_floor)]
    if caps_o is not None:
        for i, cap in enumerate(caps_o):
            row = np.zeros(n)
            row[2 + i] = 1.0
            a_ub.append(row)
            b_ub.append(float(cap))
    if extra_ub:
        for row, rhs in extra_ub:
            a_ub.append(np.asarray(row, dtype=float))
            b_ub.append(float(rhs))
    out = _solve_linprog(c, a_eq, b_eq, a_ub, b_ub, n)
    if out["ok"] and out["x"] is not None:
        x = out["x"]
        out["s"] = float(x[0])
        out["m"] = float(x[1])
        out["o"] = x[2:].copy()
        out["implied"] = 1.0 - out["off"]
    return out


def config_lp_height(
    n_sigma: int,
    n_gamma: int,
    s_floor: float,
    s_rel: float,
) -> dict:
    """A2: height cells with RvM mass envelope |mass_j - 1/n_g| <= 2 S/N."""
    stride = 2 + n_sigma
    n = n_gamma * stride
    c = np.zeros(n)
    for j in range(n_gamma):
        base = j * stride
        c[base + 1:base + stride] = -1.0
    a_eq = np.ones((1, n))
    b_eq = np.array([1.0])
    a_ub = []
    b_ub = []
    row_s = np.zeros(n)
    for j in range(n_gamma):
        row_s[j * stride] = -1.0
    a_ub.append(row_s)
    b_ub.append(-float(s_floor))
    m_cell = 1.0 / float(n_gamma)
    lo = max(0.0, m_cell - 2.0 * s_rel)
    hi = min(1.0, m_cell + 2.0 * s_rel)
    for j in range(n_gamma):
        base = j * stride
        row = np.zeros(n)
        row[base:base + stride] = 1.0
        a_ub.append(row)
        b_ub.append(hi)
        a_ub.append(-row)
        b_ub.append(-lo)
    out = _solve_linprog(c, a_eq, b_eq, a_ub, b_ub, n)
    if out["ok"] and out["x"] is not None:
        x = out["x"]
        s_tot = float(sum(x[j * stride] for j in range(n_gamma)))
        out["s"] = s_tot
        out["implied"] = 1.0 - out["off"]
    return out


def huxley_caps(sigma: np.ndarray) -> np.ndarray:
    """T -> inf exponent sign: cap = 0 when 12(1/2 - sig)/5 < 1 i.e. sig > 1/12."""
    return np.array(
        [0.0 if float(sig) > HUXLEY_CUT + 1e-15 else 1.0 for sig in sigma],
        dtype=float,
    )


def row_record(
    name: str,
    uncond: bool,
    off: float,
    implied: float,
    binding: str,
    ok: bool,
) -> dict:
    return dict(
        class_id=name,
        uncond=bool(uncond),
        max_off=float(off),
        implied=float(implied),
        binding=binding,
        ok=bool(ok),
    )


def compute_atlas(smoke: bool) -> dict:
    gl_n = 24 if smoke else 64
    n_fft = 64 if smoke else 256
    n_grid = 101 if smoke else 401
    n_sigma = 8 if smoke else 16
    n_gamma = 4 if smoke else 8
    n_basis = N_BASIS_SMOKE if smoke else N_BASIS_FULL
    n_gamma_hat = 16 if smoke else 40
    lam_lo, lam_hi = -2.0, 2.0
    p0 = P0_NUM / P0_DEN
    sigma = np.geomspace(1.0e-3, 0.45, n_sigma)

    r0 = r_window(lambda t: 1.0, gl_n)
    prop0 = 2.0 - r0
    m_sym = montgomery_symbol_moments(n_fft)
    lam_cms, p2_cms = christoffel_k2(GUE_MOMENTS[0], GUE_MOMENTS[1])
    _lam4, p4_cms = christoffel_k4(*GUE_MOMENTS)
    lam = np.linspace(lam_lo, lam_hi, n_grid)
    lp2 = inertia_lp(GUE_MOMENTS, 2, lam, include_zero=True)
    lp3 = inertia_lp(GUE_MOMENTS, 3, lam, include_zero=True)
    lp4 = inertia_lp(GUE_MOMENTS, 4, lam, include_zero=True)

    a1 = config_lp(n_sigma, s_floor=p0)
    n_rvm = rvm_main(T_RVM)
    s_bar = s_bound_bellotti(T_RVM)
    s_rel = s_bar / max(n_rvm, 1.0)
    a2 = config_lp_height(n_sigma, n_gamma, s_floor=p0, s_rel=s_rel)

    g_lo, g_hi = 10.0, (80.0 if smoke else 200.0)
    g_nodes, g_wts = leggauss(n_gamma_hat)
    gamma = 0.5 * (g_hi - g_lo) * g_nodes + 0.5 * (g_hi + g_lo)
    g_scale = 0.5 * (g_hi - g_lo) * g_wts
    dens = np.log(np.maximum(gamma / (2.0 * math.pi), 1.0e-12)) / (2.0 * math.pi)
    gamma_w = np.maximum(g_scale * dens, 0.0)
    kern = weil_kernel_matrix(
        L_PF, n_basis, sigma, gamma, gamma_w, gl_n,
    )
    on_k = kern["on_line"]
    off_k = kern["off_line"]
    on_k = np.maximum(on_k, 0.0)
    extra_a3 = []
    for n in range(n_basis):
        row = np.zeros(2 + n_sigma)
        row[0] = float(on_k[n])
        row[1] = float(on_k[n])
        row[2:] = off_k[n]
        if float(np.max(np.abs(row))) <= 1.0e-14:
            continue
        extra_a3.append((-row, 1.0e-12))
    a3 = config_lp(n_sigma, s_floor=p0, extra_ub=extra_a3)
    a3_redundancy = abs(a3["off"] - a1["off"]) if (a1["ok"] and a3["ok"]) else float("nan")
    if a1["ok"] and a1["x"] is not None:
        slacks = []
        x1 = a1["x"]
        for n in range(n_basis):
            row = np.zeros(2 + n_sigma)
            row[0] = float(on_k[n])
            row[1] = float(on_k[n])
            row[2:] = off_k[n]
            slacks.append(float(row @ x1))
        a3_min_slack = min(slacks) if slacks else float("nan")
        a3_min_on = float(np.min(on_k))
        a3_min_off = float(np.min(off_k))
        a3_off_near = float(np.min(off_k[:, 0]))
        a3_cont = float(np.max(np.abs(off_k[:, 0] - on_k)))
    else:
        a3_min_slack = float("nan")
        a3_min_on = float("nan")
        a3_min_off = float("nan")
        a3_off_near = float("nan")
        a3_cont = float("nan")

    a5_rows = []
    for amax in ALPHA_MAX_LIST:
        floor = a5_s_floor(amax, p0)
        got = config_lp(n_sigma, s_floor=floor)
        label = "inf" if not math.isfinite(amax) else (
            "%g" % amax
        )
        a5_rows.append((amax, label, floor, got))

    caps = huxley_caps(sigma)
    a6 = config_lp(n_sigma, s_floor=p0, caps_o=caps)
    a6_shift = (a6["off"] - a1["off"]) if (a1["ok"] and a6["ok"]) else float("nan")
    a6_mass_far = (
        float(np.sum(a6["o"][sigma > HUXLEY_CUT]))
        if (a6["ok"] and a6.get("o") is not None)
        else float("nan")
    )
    a6_mass_near = (
        float(np.sum(a6["o"][sigma <= HUXLEY_CUT]) + a6["m"])
        if (a6["ok"] and a6.get("o") is not None)
        else float("nan")
    )

    a1_ref_hi = config_lp(max(2, int(round(n_sigma * 1.1))), s_floor=p0)
    a1_ref_lo = config_lp(max(2, int(round(n_sigma * 0.9))), s_floor=p0)
    n_grid_hi = max(11, int(round(n_grid * 1.1)))
    n_grid_lo = max(11, int(round(n_grid * 0.9)))
    lam_hi_g = np.linspace(lam_lo, lam_hi, n_grid_hi)
    lam_lo_g = np.linspace(lam_lo, lam_hi, n_grid_lo)
    lp3_hi = inertia_lp(GUE_MOMENTS, 3, lam_hi_g, include_zero=True)
    lp3_lo = inertia_lp(GUE_MOMENTS, 3, lam_lo_g, include_zero=True)
    denom = max(abs(a1["off"]), 1e-15) if a1["ok"] else 1.0
    ref_d = []
    for got in (a1_ref_hi, a1_ref_lo):
        if a1["ok"] and got["ok"]:
            ref_d.append(abs(got["off"] - a1["off"]) / denom)
    if lp3["ok"] and lp3_hi["ok"]:
        ref_d.append(abs(lp3_hi["nfrac"] - lp3["nfrac"]) / max(abs(lp3["nfrac"]), 1e-15))
    if lp3["ok"] and lp3_lo["ok"]:
        ref_d.append(abs(lp3_lo["nfrac"] - lp3["nfrac"]) / max(abs(lp3["nfrac"]), 1e-15))
    refinement = max(ref_d) if ref_d else float("nan")

    rows = [
        row_record(
            "A1", True,
            a1["off"] if a1["ok"] else float("nan"),
            a1["implied"] if a1["ok"] else float("nan"),
            "A-F LawN256 two-moment form factor |alpha|<=1; s>=p0 tight",
            a1["ok"],
        ),
        row_record(
            "A2", True,
            a2["off"] if a2["ok"] else float("nan"),
            a2["implied"] if a2["ok"] else float("nan"),
            "A1 + RvM cell mass |dN|<=2 S(T); counting not binding",
            a2["ok"],
        ),
        row_record(
            "A3", True,
            a3["off"] if a3["ok"] else float("nan"),
            a3["implied"] if a3["ok"] else float("nan"),
            "A1 + prime-free Weil hat>=0, damped Legendre N<=24; "
            "parent-redundant",
            a3["ok"],
        ),
        row_record(
            "A4k3", False,
            lp3["nfrac"] if lp3["ok"] else float("nan"),
            lp3["p"] if lp3["ok"] else float("nan"),
            "CONDITIONAL GUE (m1,m2,m3); CMS/grid spectral n_+",
            lp3["ok"],
        ),
        row_record(
            "A4k4", False,
            lp4["nfrac"] if lp4["ok"] else float("nan"),
            lp4["p"] if lp4["ok"] else float("nan"),
            "CONDITIONAL GUE (m1..m4); CMS/grid spectral n_+",
            lp4["ok"],
        ),
    ]
    for amax, label, floor, got in a5_rows:
        uncond_a5 = bool(amax <= 1.0 + 1e-15)
        rows.append(row_record(
            "A5a%s" % label, uncond_a5,
            got["off"] if got["ok"] else float("nan"),
            got["implied"] if got["ok"] else float("nan"),
            (
                "A1 (alpha_max=1, unconditional bandwidth one)"
                if uncond_a5
                else (
                    "CONDITIONAL Montgomery F pinned on |alpha|<=%s; "
                    "s-floor %.12f (model, not a theorem)"
                    % (label, floor)
                )
            ),
            got["ok"],
        ))
    rows.append(row_record(
        "A6", True,
        a6["off"] if a6["ok"] else float("nan"),
        a6["implied"] if a6["ok"] else float("nan"),
        "A1 + Huxley N(sig,T)<<T^{12(1-sig)/5}; cap sig>1/12; "
        "mass sits at sig->0",
        a6["ok"],
    ))

    uncond_implied = [
        r["implied"] for r in rows if r["uncond"] and math.isfinite(r["implied"])
    ]
    gain_rows = [
        r for r in rows
        if r["uncond"] and math.isfinite(r["implied"])
        and r["implied"] > TARGET_CEIL + 1e-4
    ]
    if not uncond_implied:
        verdict = "INCONCLUSIVE"
        why = "unconditional rows missing / infeasible"
    elif gain_rows:
        r0g = gain_rows[0]
        verdict = "ATLAS_GAIN(%s, %.7f)" % (r0g["class_id"], r0g["implied"])
        why = (
            "unconditional row %s implied proportion %.12f exceeds "
            "0.6818+1e-4"
            % (r0g["class_id"], r0g["implied"])
        )
    elif all(imp <= TARGET_CEIL + 1e-4 for imp in uncond_implied):
        verdict = "ATLAS_NO_NEW_UNCONDITIONAL_GAIN"
        why = (
            "all unconditional implied proportions <= 0.6818+1e-4 "
            "(max %.12f)"
            % max(uncond_implied)
        )
    else:
        verdict = "INCONCLUSIVE"
        why = "unconditional implied proportions incomparable"

    payload = {
        "a1_off": None if not a1["ok"] else round(a1["off"], 12),
        "a2_off": None if not a2["ok"] else round(a2["off"], 12),
        "a3_off": None if not a3["ok"] else round(a3["off"], 12),
        "a3_redundancy": (
            None if not math.isfinite(a3_redundancy)
            else round(a3_redundancy, 12)
        ),
        "a4k3": None if not lp3["ok"] else round(lp3["p"], 12),
        "a4k4": None if not lp4["ok"] else round(lp4["p"], 12),
        "a5": [
            None if not got["ok"] else round(got["implied"], 12)
            for _amax, _lab, _fl, got in a5_rows
        ],
        "a6_off": None if not a6["ok"] else round(a6["off"], 12),
        "a6_shift": (
            None if not math.isfinite(a6_shift) else round(a6_shift, 12)
        ),
        "p0": round(p0, 12),
        "r0": round(r0, 12),
        "p2_cms": round(p2_cms, 12),
        "verdict": verdict,
        "spec_sha": SPEC_SHA,
        "grids": {
            "gl_n": gl_n, "n_fft": n_fft, "n_grid": n_grid,
            "n_sigma": n_sigma, "n_gamma": n_gamma, "n_basis": n_basis,
            "n_gamma_hat": n_gamma_hat,
        },
    }
    return dict(
        payload=payload,
        rows=rows,
        verdict=verdict,
        why=why,
        a1=a1, a2=a2, a3=a3, a6=a6,
        lp2=lp2, lp3=lp3, lp4=lp4,
        p0=p0, r0=r0, prop0=prop0,
        p2_cms=p2_cms, p4_cms=p4_cms, lam_cms=lam_cms,
        m_sym=m_sym,
        a3_redundancy=a3_redundancy,
        a3_min_slack=a3_min_slack,
        a3_min_on=a3_min_on,
        a3_min_off=a3_min_off,
        a3_off_near=a3_off_near,
        a3_cont=a3_cont,
        a5_rows=a5_rows,
        a6_shift=a6_shift,
        a6_mass_far=a6_mass_far,
        a6_mass_near=a6_mass_near,
        n_rvm=n_rvm, s_bar=s_bar, s_rel=s_rel,
        refinement=refinement,
        grids=payload["grids"],
        sigma=sigma,
        n_basis=n_basis,
        n_sigma=n_sigma,
        n_gamma=n_gamma,
        n_grid=n_grid,
        gl_n=gl_n,
        n_fft=n_fft,
        n_gamma_hat=n_gamma_hat,
        lam_lo=lam_lo,
        lam_hi=lam_hi,
        caps=caps,
        on_k=on_k,
        off_k=off_k,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = bool(args.smoke)

    print("=" * 74)
    print(
        "certificate_class_atlas_probe -- PRIME.CERTIFICATE.ATLAS.01 "
        "(r629)"
    )
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("MODE %s" % ("SMOKE" if smoke else "FULL"))
    print("CLAIM_BOUNDARY %s" % FENCE)
    print("=" * 74, flush=True)

    section("S0  FIREWALL")
    fw_ok, fw_msg = firewall_audit()
    check("G1-ast-firewall", fw_ok, fw_msg)
    info("zeros of zeta are not LP data; gamma grids are quadrature")

    section("S1  CITATIONS (unconditional rows cite a theorem)")
    for row in CITATIONS:
        info(
            "%s  uncond=%s  %s %s"
            % (row["row"], row["uncond"], row["who"], row["year"])
        )
        info("  ref: %s" % row["ref"])
        info("  thm: %s" % row["statement"])
    check(
        "G2-citations-frozen",
        CITATIONS[0]["uncond"] is True
        and CITATIONS[1]["uncond"] is True
        and CITATIONS[2]["uncond"] is True
        and CITATIONS[3]["uncond"] is False
        and CITATIONS[4]["uncond"] is False
        and CITATIONS[5]["uncond"] is True
        and abs(L_PF - L_PF_LABEL) < 5.0e-5,
        "A1/A2/A3/A6 uncond; A4/A5 cond; L_pf=log2/2=%.12f vs 0.3466"
        % L_PF,
    )

    section("S2  ATLAS LP")
    atlas = compute_atlas(smoke)
    atlas2 = compute_atlas(smoke)
    p0 = atlas["p0"]
    grids = atlas["grids"]
    info(
        "grids gl_n=%d n_fft=%d n_grid=%d n_sigma=%d n_gamma=%d "
        "n_basis=%d n_gamma_hat=%d  sigma in [%.3e, %.3f]"
        % (
            grids["gl_n"], grids["n_fft"], grids["n_grid"],
            grids["n_sigma"], grids["n_gamma"], grids["n_basis"],
            grids["n_gamma_hat"],
            float(atlas["sigma"][0]), float(atlas["sigma"][-1]),
        )
    )
    info(
        "R(psi_0)=%.12f  2-R=%.12f  p0=%.12f  1-p0=%.12f"
        % (atlas["r0"], atlas["prop0"], p0, 1.0 - p0)
    )
    info(
        "RvM T=%.3e  N_main=%.6e  S_Bellotti=%.6f  S/N=%.3e"
        % (T_RVM, atlas["n_rvm"], atlas["s_bar"], atlas["s_rel"])
    )
    info(
        "A3 min_on=%.6e min_off=%.6e off_near=%.6e "
        "|off_near-on|_inf=%.6e min_slack@A1=%.6e redundancy=%.3e"
        % (
            atlas["a3_min_on"], atlas["a3_min_off"], atlas["a3_off_near"],
            atlas["a3_cont"], atlas["a3_min_slack"], atlas["a3_redundancy"],
        )
    )
    info(
        "A6 shift=%.3e  mass_far(sig>1/12)=%.6e  "
        "mass_near+multiples=%.6e"
        % (atlas["a6_shift"], atlas["a6_mass_far"], atlas["a6_mass_near"])
    )

    check(
        "G3-rpsi-four-thirds",
        abs(atlas["r0"] - 4.0 / 3.0) <= 1e-3
        and abs(atlas["prop0"] - PROP_23) <= 1e-3,
        "R=%.12f vs 4/3; 2-R=%.12f vs 2/3"
        % (atlas["r0"], atlas["prop0"]),
    )
    check(
        "G4-ceiling-p0",
        abs(p0 - TARGET_CEIL) <= 1e-3
        and abs(p0 - R267_CEIL_P0) <= 1e-6,
        "p0_exact=%s/%s = %.12f vs 0.6818; r267 CEIL_P0=%.7f"
        % (P0_NUM, P0_DEN, p0, R267_CEIL_P0),
    )
    a1 = atlas["a1"]
    check(
        "G5-A1-reproduces-1-p0",
        a1["ok"] and abs(a1["off"] - (1.0 - p0)) <= 1e-8
        and abs(a1["implied"] - p0) <= 1e-8,
        "A1 off=%.12f vs 1-p0=%.12f  implied=%.12f"
        % (
            a1["off"] if a1["ok"] else float("nan"),
            1.0 - p0,
            a1["implied"] if a1["ok"] else float("nan"),
        ),
    )
    a2 = atlas["a2"]
    a2_delta = (
        abs(a2["off"] - a1["off"]) if (a1["ok"] and a2["ok"]) else float("nan")
    )
    check(
        "G6-A2-no-shift",
        a2["ok"] and a2_delta <= 1e-6,
        "A2 off=%.12f  |A2-A1|=%.3e  S/N=%.3e (RvM does not see Re rho)"
        % (
            a2["off"] if a2["ok"] else float("nan"),
            a2_delta, atlas["s_rel"],
        ),
    )
    a3 = atlas["a3"]
    check(
        "G7-A3-redundant",
        a3["ok"]
        and atlas["a3_redundancy"] <= 1e-6
        and atlas["a3_min_slack"] >= -1e-8,
        "|A3-A1|=%.3e (<=1e-6)  min_slack=%.3e  "
        "sigma->0 |I_off-I_on|_inf=%.3e  (r619 L_det>=0.5: "
        "L=0.3466 is zero-blind)"
        % (
            atlas["a3_redundancy"], atlas["a3_min_slack"], atlas["a3_cont"],
        ),
    )
    lp3, lp4 = atlas["lp3"], atlas["lp4"]
    check(
        "G8-A4-gue-r616",
        lp3["ok"] and lp4["ok"]
        and abs(lp3["p"] - 5.0 / 6.0) <= 1e-2
        and abs(lp4["p"] - 31.0 / 36.0) <= 1e-2
        and abs(atlas["p4_cms"] - 31.0 / 36.0) <= 1e-6
        and abs(atlas["p2_cms"] - 0.75) <= 1e-12,
        "GUE n_+ k=2 CMS=%.12f (3/4); k=3 LP=%.12f (5/6); "
        "k=4 LP=%.12f CMS=%.12f (31/36) on [%g,%g]/%d"
        % (
            atlas["p2_cms"], lp3["p"], lp4["p"], atlas["p4_cms"],
            atlas["lam_lo"], atlas["lam_hi"], atlas["n_grid"],
        ),
    )
    a5_ok = all(got["ok"] for _a, _l, _f, got in atlas["a5_rows"])
    a5_a1 = atlas["a5_rows"][0][3]
    a5_inf = atlas["a5_rows"][-1][3]
    a5_seq = [
        got["implied"] if got["ok"] else float("nan")
        for _a, _l, _f, got in atlas["a5_rows"]
    ]
    mono = all(
        a5_seq[i] <= a5_seq[i + 1] + 1e-12
        for i in range(len(a5_seq) - 1)
        if math.isfinite(a5_seq[i]) and math.isfinite(a5_seq[i + 1])
    )
    check(
        "G9-A5-parametric",
        a5_ok and a5_a1["ok"] and abs(a5_a1["implied"] - p0) <= 1e-8
        and a5_inf["ok"] and abs(a5_inf["implied"] - 0.75) <= 1e-8
        and mono,
        "alpha_max=1 implied=%.12f (=A1); inf implied=%.12f (=3/4 CMS); "
        "monotone %s  sequence %s"
        % (
            a5_a1["implied"], a5_inf["implied"], mono,
            ", ".join("%.6f" % x for x in a5_seq),
        ),
    )
    a6 = atlas["a6"]
    check(
        "G10-A6-nearline",
        a6["ok"]
        and abs(atlas["a6_shift"]) <= 1e-6
        and atlas["a6_mass_far"] <= 1e-8
        and atlas["a6_mass_near"] >= (1.0 - p0) - 1e-8,
        "opt shift=%.3e  far mass=%.3e (must be 0)  "
        "near+multiples=%.12f (=1-p0).  Huxley kills sig>1/12; "
        "two-moment maximizer already sat at sig->0, so the ceiling "
        "does not move."
        % (atlas["a6_shift"], atlas["a6_mass_far"], atlas["a6_mass_near"]),
    )
    check(
        "G11-refinement-10pct",
        math.isfinite(atlas["refinement"]) and atlas["refinement"] <= 0.10,
        "max relative change under n_sigma/n_grid +/-10%% = %.3e"
        % atlas["refinement"],
    )
    sha1 = payload_sha(atlas["payload"])
    sha2 = payload_sha(atlas2["payload"])
    check(
        "G12-two-identical-runs",
        sha1 == sha2 and len(sha1) == 64,
        "PAYLOAD_SHA %s (re-run match)" % sha1,
    )
    check(
        "G13-verdict-enum",
        atlas["verdict"].startswith("ATLAS_NO_NEW_UNCONDITIONAL_GAIN")
        or atlas["verdict"].startswith("ATLAS_GAIN")
        or atlas["verdict"] == "INCONCLUSIVE",
        "%s -- %s" % (atlas["verdict"], atlas["why"]),
    )

    wall = time.time() - T0
    cap = 60.0 if smoke else 900.0
    check(
        "G14-runtime",
        wall <= cap,
        "wall %.3f s <= %.0f s" % (wall, cap),
    )
    check(
        "G15-symbol-m1m2",
        abs(atlas["m_sym"][0] - 1.0) <= 1e-9
        and abs(atlas["m_sym"][1] - 4.0 / 3.0) <= 1e-9,
        "r616 |alpha|-symbol m=(%.6f, %.6f, %.6f, %.6f)"
        % atlas["m_sym"],
    )

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    ntot = len(CHECKS)

    section("ATLAS TABLE")
    print(
        "  %-8s %-5s %14s %14s  %s"
        % ("class", "uncond", "max_off", "implied", "binding")
    )
    for rec in atlas["rows"]:
        print(
            "  %-8s %-5s %14.10f %14.10f  %s"
            % (
                rec["class_id"],
                "yes" if rec["uncond"] else "NO",
                rec["max_off"],
                rec["implied"],
                rec["binding"],
            )
        )
    print("VERDICT %s" % atlas["verdict"])
    print("FENCE %s" % FENCE)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("PAYLOAD_SHA %s" % sha1)
    print("GATES: %d/%d PASS   wall %.3f s" % (npass, ntot, wall))
    print("NO RH CLAIM IN EITHER DIRECTION.")
    print(
        "AMENDMENTS AFTER FREEZE: NONE" if npass == ntot
        else "GATE FAILURES PRESENT -- see above"
    )

    section("STATE")
    print("round r629")
    print("contract PRIME.CERTIFICATE.ATLAS.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("PAYLOAD_SHA %s" % sha1)
    print("GATES %d/%d  wall %.3f s  mode %s" % (
        npass, ntot, wall, "SMOKE" if smoke else "FULL",
    ))
    print("VERDICT %s" % atlas["verdict"])
    print("FENCE %s" % FENCE)
    print("GRID n_sigma=%d n_gamma=%d n_grid=%d N_basis=%d gl_n=%d" % (
        atlas["n_sigma"], atlas["n_gamma"], atlas["n_grid"],
        atlas["n_basis"], atlas["gl_n"],
    ))
    print("ATLAS class uncond max_off implied")
    for rec in atlas["rows"]:
        print(
            "  %s %s %.10f %.10f"
            % (
                rec["class_id"],
                "U" if rec["uncond"] else "C",
                rec["max_off"],
                rec["implied"],
            )
        )
    print("A3_REDUNDANCY %.6e  min_slack %.6e  L_det_parent >=0.5" % (
        atlas["a3_redundancy"], atlas["a3_min_slack"],
    ))
    print(
        "A6_SLICE shift %.6e  far(sig>1/12)=%.3e  "
        "near+mult=%.10f (Huxley forces sig->0; ceiling unmoved)"
        % (atlas["a6_shift"], atlas["a6_mass_far"], atlas["a6_mass_near"])
    )
    print("REFINEMENT rel=%.6e (n_sigma +/-10 pct, bar 0.10)" % (
        atlas["refinement"],
    ))
    print("AMENDMENTS NONE" if npass == ntot else "GATE FAILURES")
    print("END_STATE")
    return 0 if npass == ntot else 1


if __name__ == "__main__":
    sys.exit(main())
