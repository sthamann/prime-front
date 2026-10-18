#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weil_window_certificate_probe -- exploration of Chuk 2026 arXiv:2608.24827

Independent python-flint / Arb reproduction of the certified window-form
lower bound in Chuk, "Weil positivity in compact windows" (2026):

    R(f)  >=  c  ||f||_2^2
    for real even f with supp f subset [-0.8, 0.8],

via the one-stroke reduction (their Theorem 1.1), Bernstein-ellipse
quadrature (Lemma 5.1 / Trefethen), tail/coupling bounds (Lemma 5.2
setup), and a ball-arithmetic Cholesky residual.  Reference (non-certified)
spectra of the even and odd reduced window forms are reported for
calibration against the paper's published eigenvalues.

This is exploration-only research code.  It does not promote a ledger
row, does not assert a hypothesis about zeros, and must not be read as a
claim about the Riemann Hypothesis.  Fence: no RH claim.

Inputs (paper, L = 0.8): prime comb {2,3,4}, T# in {200, 150}, N = 200
even (resp. odd) Legendre modes, composite Gauss-Legendre panels of
width h = 1/4 with n_G = 32 (fallback 24).  Smoke: N=60, T#=60, h=1/2,
n_G=16 -- pipeline only; beta* is negative there, so no certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import sys
import time
from pathlib import Path

try:
    import flint
    from flint import acb, arb, arb_mat, ctx, fmpz_poly
except ImportError as exc:
    raise SystemExit(
        "PIPELINE-BROKEN: python-flint is required; run this probe in "
        "experiments/tfpt-discovery/.venv"
    ) from exc

import mpmath as mp

HERE = Path(__file__).resolve().parent
RESULT_JSON = HERE / "weil_window_certificate_result.json"
FENCE = "Exploration only; no RH claim."
CONTRACT = "WEIL.WINDOW.CERTIFICATE.01"
SOURCE = "arXiv:2608.24827 (Chuk 2026); independent Arb reproduction"

WORKING_BITS = 200
MP_DPS = 60
STRIP_B = 0.4
COVER_SIDE = 0.05
COVER_SPLIT_ABS = 40.0
REAL_COVER_H = 0.05
ENVELOPE_T_MIN = 15.0 / 4.0

# Paper targets (calibration only; not loaded as oracles).
PAPER_AL = 2.9419735
PAPER_BETA_200 = 0.5134667
PAPER_BETA_150 = 0.2241
PAPER_C_200 = 8.9e-18
PAPER_C_150 = 1.2e-18
PAPER_C_ODD = 8.2e-15
PAPER_EIG_150 = (1.356e-18, 2.32e-12, 2.9e-7, 2.1e-3, 0.2241)
PAPER_EIG_200_LO, PAPER_EIG_200_HI = 9e-18, 1.656e-17
PAPER_EIG_ODD = 9.1183e-15
PAPER_FLOOR_EVEN, PAPER_FLOOR_ODD = 1.65e-17, 1.57e-14


# ---------------------------------------------------------------------------
# FLINT signed-FFT regression (OpenAI PrimeGaps186; do not abort)
# ---------------------------------------------------------------------------

def check_flint_signed_fft() -> dict:
    """Known FLINT 3.6.0 signed-FFT polynomial-convolution defect.

    Same vectors as openai/PrimeGaps186 prime_gap_186_certificate.py.
    Our python-flint 0.9.0 / FLINT 3.6.0 build fails this; record WARN
    and continue — the certificate path is audited FFT-free below.
    """
    a, b = (1 << 509) - 1, (1 << 510) - 1
    p, q = fmpz_poly([a] * 16), fmpz_poly([-b] * 16)
    expected = [-min(j + 1, 31 - j, 16) * a * b for j in range(31)]
    defect = p * q != fmpz_poly(expected) or p.mul_low(q, 16) != fmpz_poly(
        expected[:16]
    )
    status = "FAIL" if defect else "PASS"
    info = {
        "flint_signed_fft_regression": status,
        "flint_version": flint.__FLINT_VERSION__,
        "python_flint": flint.__version__,
    }
    if defect:
        emit(
            f"WARN FLINT signed-FFT regression {status}  "
            f"flint={info['flint_version']} python-flint={info['python_flint']}"
        )
    else:
        emit(
            f"FLINT signed-FFT regression {status}  "
            f"flint={info['flint_version']} python-flint={info['python_flint']}"
        )
    return info


# ---------------------------------------------------------------------------
# Small utilities
# ---------------------------------------------------------------------------

def emit(msg: str = "") -> None:
    print(msg, flush=True)


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def arb_json(x: arb) -> dict:
    return {
        "mid": str(x.mid()),
        "rad": str(x.rad()),
        "abs_upper": str(x.abs_upper()),
        "float": float(x.mid()),
    }


def ffloat(x: arb | mp.mpf | float) -> float:
    if isinstance(x, arb):
        return float(x.mid())
    return float(x)


def add_radius(x: arb, rad: arb) -> arb:
    return x + arb("0", rad.abs_upper())


def inf_norm_from_abs_upper(M: arb_mat) -> arb:
    n = M.nrows()
    worst = arb(0)
    for i in range(n):
        row = arb(0)
        for j in range(n):
            row += M[i, j].abs_upper()
        if row > worst:
            worst = row
    return worst


def double_fac_odd(n: int) -> arb:
    """(2n+1)!! = (2n+1)! / (2^n n!)."""
    return arb.fac_ui(2 * n + 1) / (arb(2) ** n * arb.fac_ui(n))


def basis_sign(n: int) -> int:
    """Sign so That_n is real: (-1)^{n/2} even, (-1)^{(n-1)/2} odd."""
    if n % 2 == 0:
        return 1 if (n // 2) % 2 == 0 else -1
    return 1 if ((n - 1) // 2) % 2 == 0 else -1


def nu_of(n: int) -> arb:
    return arb(n) + arb("0.5")


def that_scale(n: int, L: arb) -> arb:
    return arb(2) * (L * nu_of(n)).sqrt()


def T_basis(n: int, x: acb, L: acb) -> acb:
    pref = (acb(2 * n + 1) / (acb(2) * L)).sqrt()
    return pref * (x / L).legendre_p(n)


# ---------------------------------------------------------------------------
# Special functions (rigorous balls)
# ---------------------------------------------------------------------------

def sph_j(n: int, z: acb) -> acb:
    """Library j_n; reliable only for modest n or n < |z|.  Entire."""
    if z == 0:
        return acb(1) if n == 0 else acb(0)
    if n == 0:
        return z.sinc()
    if z.contains(acb(0)):
        return acb("nan")
    return (acb.pi() / (acb(2) * z)).sqrt() * z.bessel_j(acb(n) + acb("0.5"))


def sph_j_series(n: int, x: arb, work_prec: int) -> arb:
    """Rigorous power series for j_n(x) on a real Arb ball.

    j_n(x) = x^n/(2n+1)!! * sum_k (-1)^k (x^2/2)^k
             / (k! * prod_{i=1..k} (2n+2i+1)).
    Tail radius is |first omitted term| / (1-r) once consecutive-term
    magnitude ratio r < 1/2 (geometric remainder).
    """
    if x == 0:
        return arb(1) if n == 0 else arb(0)
    pref = (x ** n) / double_fac_odd(n)
    half_x2 = (x * x) / arb(2)
    s = arb(1)
    term = arb(1)
    tol = arb(2) ** -(work_prec + 20)
    for k in range(400):
        den = arb(k + 1) * arb(2 * n + 2 * k + 3)
        ratio = half_x2 / den
        nxt = -term * ratio
        ratio_ub = ratio.abs_upper()
        mag_nxt = nxt.abs_upper()
        mag_term = term.abs_upper()
        scale = s.abs_upper()
        if scale == 0:
            scale = arb(1)
        if mag_nxt <= mag_term and mag_nxt <= tol * scale:
            if not (ratio_ub < arb("0.5")):
                raise RuntimeError(
                    f"j_{n} series: tail ratio {float(ratio_ub)} >= 1/2 at k={k}"
                )
            tail = mag_nxt / (arb(1) - ratio_ub)
            return pref * add_radius(s, tail)
        s += nxt
        term = nxt
    raise RuntimeError(f"j_{n} series did not reach a geometric tail (n={n})")


def _rel_radius(x: arb) -> arb | None:
    """Relative radius rad/|mid| when the ball does not contain 0."""
    if x.contains(arb(0)):
        return None
    mag = abs(x.mid())
    if mag == 0:
        return None
    return x.rad() / mag


def sph_j_miller(
    n_max: int, x: arb, extra: int = 40, work_prec: int = 512
) -> tuple[list[arb], dict]:
    """j_0..j_{n_max}(x) from series seeds plus a downward recurrence.

    Seeds j_N, j_{N+1} are the rigorous power series (truncation is in
    the tail radius).  Direct recurrence *on the node ball* inflates by
    wrapping (j_0 ~ 10^8 at a 200-bit Gauss node); the same is true of
    the low-n series.  The recurrence is therefore run at the 512-bit
    midpoint (no (0,1) seed, no sin(x)/x rescaling, no renormalisation)
    and the original ball radius is re-injected by the spherical-Bessel
    DE + mean-value remainder
        j_n(x) ∈ j_n(mid) + j_n'(mid)[-r,r] + (1/2) M2 r^2,
    with |j_n'| ≤ 1 + n/x_min and the DE bound on |j_n''|.  For those n
    where the MVT relative radius exceeds 1e-40, the same power series
    is re-evaluated on the original x-ball and used when it overlaps
    and is tighter (valid for n ≫ |x|).
    """
    prev = ctx.prec
    ctx.prec = max(prev, work_prec)
    try:
        if x == 0 or (x.contains(arb(0)) and x.abs_upper() < arb("1e-30")):
            out = [arb(1)] + [arb(0)] * n_max
            return out, {
                "j0_ok": True,
                "worst_rel": arb(0),
                "N": n_max,
                "seeds": "rigorous_power_series",
            }
        x_mid = arb(x.mid().str(max(80, work_prec // 3), radius=False))
        if x_mid == 0:
            x_mid = arb("1e-30")
        N = max(n_max, int(float(x_mid.abs_upper())) + 1) + extra
        j_np1 = sph_j_series(N + 1, x_mid, work_prec)
        j_n = sph_j_series(N, x_mid, work_prec)
        stored: list[arb | None] = [None] * (n_max + 1)
        for n in range(N, 0, -1):
            j_nm1 = (arb(2 * n + 1) / x_mid) * j_n - j_np1
            if n - 1 <= n_max:
                stored[n - 1] = j_nm1
            j_np1 = j_n
            j_n = j_nm1
        point = list(stored)
        sinc_mid = x_mid.sin() / x_mid
        if not point[0].overlaps(sinc_mid):
            raise RuntimeError(
                f"j_0(mid) does not overlap sin(mid)/mid: {point[0]} vs {sinc_mid}"
            )
        r = x.rad()
        xmin = x.abs_lower()
        if xmin <= arb(0):
            xmin = arb("1e-18")
        out: list[arb] = []
        for n in range(n_max + 1):
            jn = point[n]
            jnp1 = (
                point[n + 1]
                if n < n_max
                else sph_j_series(n + 1, x_mid, work_prec)
            )
            jp = (arb(n) / x_mid) * jn - jnp1
            yp_b = arb(n) / xmin + arb(1)
            ypp_b = (
                arb(2) / xmin * yp_b
                + arb(1)
                + arb(n) * arb(n + 1) / (xmin * xmin)
            )
            extra_r = abs(jp) * r + ypp_b * r * r / arb(2)
            out.append(add_radius(jn, extra_r))
        # High-n MVT remainder is ~ M2 r^2 (tiny absolute, large relative).
        # The same power series on the original x-ball is tight for n >> |x|
        # and is a fully rigorous enclosure of j_n(x); take it when it
        # overlaps the MVT ball and is strictly smaller.
        for n in range(n_max + 1):
            rel = _rel_radius(out[n])
            if rel is not None and rel.abs_upper() < arb("1e-40"):
                continue
            ser = sph_j_series(n, x, work_prec)
            if out[n].overlaps(ser) and ser.rad() < out[n].rad():
                out[n] = ser
        sinc = x.sin() / x
        if not out[0].overlaps(sinc):
            raise RuntimeError(
                f"j_0 enclosure does not overlap sin(x)/x: {out[0]} vs {sinc}"
            )
        # Taylor ball can be slightly tighter than Arb's sinc(x) enclosure;
        # enlarge so j_0 contains sinc at both work_prec and ambient prec.
        save_prec = ctx.prec
        ctx.prec = prev
        sinc_amb = x.sin() / x
        ctx.prec = save_prec
        for sc in (sinc, sinc_amb):
            if not out[0].overlaps(sc):
                raise RuntimeError(
                    f"j_0 enclosure does not overlap sin(x)/x: {out[0]} vs {sc}"
                )
            need = abs(out[0].mid() - sc.mid()) + sc.rad()
            out[0] = add_radius(out[0], need)
            if not out[0].contains(sc):
                raise RuntimeError(
                    f"j_0 enclosure does not contain sin(x)/x: {out[0]} vs {sc}"
                )
        worst = arb(0)
        for val in out:
            rel = _rel_radius(val)
            if rel is not None and rel > worst:
                worst = rel
        info = {
            "j0_ok": True,
            "j0_contains_sinc": True,
            "worst_rel": worst,
            "N": N,
            "seeds": "rigorous_power_series",
        }
    finally:
        ctx.prec = prev
    return out, info


def sph_j_real(n: int, t: arb, L: arb) -> arb:
    js, _ = sph_j_miller(n, t * L)
    return js[n]


def sph_i(n: int, x: arb) -> arb:
    """Modified spherical Bessel i_n(x) = sqrt(pi/(2x)) I_{n+1/2}(x)."""
    z = acb(x)
    val = (acb.pi() / (acb(2) * z)).sqrt() * z.bessel_i(acb(n) + acb("0.5"))
    return val.real


def jn_bound_real(n: int, x: arb) -> arb:
    """|j_n(x)| <= min(1, x^n / (2n+1)!!)  on the real half-line."""
    if n == 0:
        return arb(1)
    raw = (x ** n) / double_fac_odd(n)
    return raw if raw.abs_upper() < arb(1) else arb(1)


def jn_bound_complex(n: int, zabs: arb) -> arb:
    """|j_n(z)| <= (|z|^n / (2n+1)!!) exp(|z|^2 / 2)."""
    return (zabs ** n) / double_fac_odd(n) * (zabs * zabs / arb(2)).exp()


# ---------------------------------------------------------------------------
# Comb, symbol, envelope
# ---------------------------------------------------------------------------

def comb_terms(L: arb) -> list[tuple[int, arb, arb]]:
    """n in {2,3,4} for L=0.8 (log n < 2L). Lambda(2)=log 2, Lambda(4)=log 2."""
    two = arb(2)
    log2 = two.log()
    log3 = arb(3).log()
    out = []
    for n, lam in ((2, log2), (3, log3), (4, log2)):
        if arb(n).log() < two * L:
            coeff = two * lam / arb(n).sqrt()
            out.append((n, lam, coeff))
    return out


def A_L_of(terms: list[tuple[int, arb, arb]]) -> arb:
    s = arb(0)
    for _n, _lam, coeff in terms:
        s += coeff
    return s


def beta_star_of(Tsharp: arb, A_L: arb) -> arb:
    return (Tsharp / (arb(2) * arb.pi())).log() - arb(1) / Tsharp - A_L


def psi_L_real(t: arb, terms: list[tuple[int, arb, arb]]) -> arb:
    z = acb("0.25") + acb(0, 1) * acb(t) / acb(2)
    s = z.digamma().real - arb.pi().log()
    for n, _lam, coeff in terms:
        s -= coeff * (t * arb(n).log()).cos()
    return s


def psi_L_analytic(t: acb, terms: list[tuple[int, arb, arb]]) -> acb:
    """Half-sum analytic continuation of Re psi(1/4 + i t/2) minus comb."""
    half = acb("0.25")
    z1 = half + acb(0, 1) * t / acb(2)
    z2 = half - acb(0, 1) * t / acb(2)
    s = (z1.digamma() + z2.digamma()) / acb(2) - acb.pi().log()
    for n, _lam, coeff in terms:
        s -= acb(coeff) * (t * acb(n).log()).cos()
    return s


def envelope_minorant(t: arb, A_L: arb) -> arb:
    return (t / (arb(2) * arb.pi())).log() - arb(1) / t - A_L


# ---------------------------------------------------------------------------
# Coverings
# ---------------------------------------------------------------------------

def _acb_rect(cx: float, cy: float, hx: float, hy: float) -> acb:
    """Axis-aligned complex rectangle as a product of two real Arb balls."""
    return acb(arb(str(cx), str(hx)), arb(str(cy), str(hy)))


def cover_M_psi(
    Tsharp: float,
    beta: arb,
    terms: list[tuple[int, arb, arb]],
    side: float = COVER_SIDE,
) -> tuple[arb, int, int]:
    """Rigorous max of |Psi~_L(t) - beta*| on the Bernstein rectangle."""
    re_lo, re_hi = -0.45, Tsharp + 0.45
    im_lo, im_hi = -STRIP_B, STRIP_B
    half = side / 2.0
    xs = []
    x = re_lo + half
    while x < re_hi + 1e-15:
        xs.append(x)
        x += side
    ys = []
    y = im_lo + half
    while y < im_hi + 1e-15:
        ys.append(y)
        y += side

    worst = arb(0)
    n_eval = 0
    n_split = 0
    split_abs = arb(str(COVER_SPLIT_ABS))
    stack = [(cx, cy, half, 0) for cy in ys for cx in xs]
    while stack:
        cx, cy, hlf, depth = stack.pop()
        tball = _acb_rect(cx, cy, hlf, hlf)
        val = psi_L_analytic(tball, terms) - acb(beta)
        n_eval += 1
        finite = bool(val.is_finite())
        au = abs(val).abs_upper() if finite else None
        tight = finite and au <= split_abs
        if tight or (finite and depth >= 8):
            if au > worst:
                worst = au
            continue
        if depth >= 8:
            raise RuntimeError(
                "M_Psi covering: non-finite ball after 8 splits at "
                f"({cx}, {cy})"
            )
        n_split += 1
        nh = hlf / 2.0
        for dx in (-nh, nh):
            for dy in (-nh, nh):
                stack.append((cx + dx, cy + dy, nh, depth + 1))
    return worst, n_eval, n_split


def cover_real_sup(
    Tsharp: float,
    beta: arb,
    terms: list[tuple[int, arb, arb]],
    h: float = REAL_COVER_H,
) -> arb:
    """Rigorous max of |Psi_L(t) - beta*| on [0, T#] by real Arb balls."""
    worst = arb(0)
    rad = h / 2.0
    t = rad
    while t <= Tsharp + 1e-15:
        ball = arb(str(min(t, Tsharp)), str(rad))
        val = psi_L_real(ball, terms) - beta
        au = val.abs_upper()
        if au > worst:
            worst = au
        t += h
    return worst


# ---------------------------------------------------------------------------
# Quadrature nodes and Bernstein budget
# ---------------------------------------------------------------------------

def gauss_legendre(n_g: int) -> tuple[list[arb], list[arb]]:
    xs, ws = [], []
    for k in range(n_g):
        x, w = arb.legendre_p_root(n_g, k, weight=True)
        xs.append(x)
        ws.append(w)
    return xs, ws


def bernstein_rho(h: float, b: float = STRIP_B) -> arb:
    bp = arb(str(2.0 * b / h))
    return bp + (arb(1) + bp * bp).sqrt()


def panel_quad_factor(h: arb, n_g: int, rho: arb) -> arb:
    """(h/2) * (64/15) * rho^{-2 n_G} / (rho^2 - 1)  (Trefethen, [-1,1])."""
    return (h / arb(2)) * (arb(64) / arb(15)) * (rho ** (-2 * n_g)) / (
        rho * rho - arb(1)
    )


def entry_M(n: int, m: int, L: arb, M_psi: arb) -> arb:
    """M on the ellipse for |(Psi-beta*) That_n That_m| (no 1/pi)."""
    return (
        M_psi
        * arb(4)
        * L
        * (nu_of(n) * nu_of(m)).sqrt()
        * (arb(2) * L * arb(str(STRIP_B))).exp()
    )


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def pole_vector(orders: list[int], L: arb) -> list[arb]:
    half = L / arb(2)
    return [that_scale(n, L) * sph_i(n, half) for n in orders]


def assemble_C(
    orders: list[int],
    L: arb,
    Tsharp: float,
    h: float,
    n_g: int,
    beta: arb,
    terms: list[tuple[int, arb, arb]],
    nodes: list[arb],
    weights: list[arb],
    label: str,
    only_pairs: list[tuple[int, int]] | None = None,
    audit_pairs: list[tuple[int, int]] | None = None,
) -> tuple[arb_mat | dict, dict]:
    n_modes = len(orders)
    n_panels = int(round(Tsharp / h))
    scales = {n: that_scale(n, L) * arb(basis_sign(n)) for n in orders}
    pi_inv = arb(1) / arb.pi()
    h_arb = arb(str(h))
    n_max = max(orders) if only_pairs is None else max(max(p) for p in only_pairs)
    t0 = time.time()
    miller_rel_worst = arb(0)
    n_j0 = 0
    n_j0_ok = 0
    C: arb_mat | dict
    if only_pairs is None:
        C = arb_mat(n_modes, n_modes)
    else:
        C = {p: arb(0) for p in only_pairs}
    audit_acc: dict[tuple[int, int], arb] | None = (
        {p: arb(0) for p in audit_pairs} if audit_pairs else None
    )
    for p in range(n_panels):
        a = arb(str(p * h))
        mid = a + h_arb / arb(2)
        if only_pairs is None:
            V = arb_mat(n_modes, n_g)
            W = arb_mat(n_g, n_g)
        for g in range(n_g):
            t = mid + (h_arb / arb(2)) * nodes[g]
            wpan = (h_arb / arb(2)) * weights[g]
            symb = psi_L_real(t, terms) - beta
            weight = wpan * symb * pi_inv
            js, minfo = sph_j_miller(n_max, t * L)
            n_j0 += 1
            if minfo["j0_ok"]:
                n_j0_ok += 1
            if minfo["worst_rel"] > miller_rel_worst:
                miller_rel_worst = minfo["worst_rel"]
            if only_pairs is None:
                W[g, g] = weight
                for k, n in enumerate(orders):
                    V[k, g] = scales[n] * js[n]
                if audit_acc is not None:
                    for n, m in audit_pairs:
                        audit_acc[(n, m)] = (
                            audit_acc[(n, m)]
                            + weight * scales[n] * js[n] * scales[m] * js[m]
                        )
            else:
                for n, m in only_pairs:
                    C[(n, m)] = C[(n, m)] + weight * scales[n] * js[n] * scales[m] * js[m]
        if only_pairs is None:
            C += (V * W) * V.transpose()
        if (p + 1) % 50 == 0 or p + 1 == n_panels:
            emit(
                f"    {label}: panel {p + 1}/{n_panels}  "
                f"({time.time() - t0:.1f}s)  miller_rel<={float(miller_rel_worst.abs_upper()):.2e}"
            )
    if miller_rel_worst.abs_upper() > arb("1e-40"):
        raise RuntimeError(
            f"{label}: Miller rel radius "
            f"{float(miller_rel_worst.abs_upper()):.3e} exceeds 1e-40"
        )
    stats = {
        "worst_rel": miller_rel_worst,
        "j0_ok": n_j0_ok == n_j0 and n_j0 > 0,
        "j0_checks": n_j0,
        "j0_passed": n_j0_ok,
        "seeds": "rigorous_power_series",
        "rel_below_1e40": bool(miller_rel_worst.abs_upper() < arb("1e-40")),
        "fft_free_C_acc": audit_acc,
    }
    return C, stats


def _overlap_audit(
    pairs: list[tuple[int, int]],
    mat_ball,
    scalar_ball,
) -> dict:
    """Compare arb_mat entries to FFT-free scalar balls; require overlap."""
    n_ov = 0
    max_disc = arb(0)
    max_mat_rad = arb(0)
    max_sc_rad = arb(0)
    for n, m in pairs:
        mb = mat_ball(n, m)
        sb = scalar_ball(n, m)
        ov = bool(mb.overlaps(sb))
        disc = abs(mb.mid() - sb.mid())
        if disc > max_disc:
            max_disc = disc
        if mb.rad() > max_mat_rad:
            max_mat_rad = mb.rad()
        if sb.rad() > max_sc_rad:
            max_sc_rad = sb.rad()
        if ov:
            n_ov += 1
        else:
            raise RuntimeError(
                f"fft-free audit mismatch at ({n},{m}): mat={mb} scalar={sb}"
            )
    return {
        "n_pairs": len(pairs),
        "n_overlap": n_ov,
        "max_discrepancy": float(max_disc.mid()),
        "max_mat_rad": float(max_mat_rad.mid()),
        "max_scalar_rad": float(max_sc_rad.mid()),
    }


def audit_C_fft_free(
    C: arb_mat,
    orders: list[int],
    audit_acc: dict[tuple[int, int], arb],
) -> dict:
    idx = {n: i for i, n in enumerate(orders)}
    pairs = list(audit_acc.keys())
    return _overlap_audit(
        pairs,
        lambda n, m: C[idx[n], idx[m]],
        lambda n, m: audit_acc[(n, m)],
    )


def audit_llt_fft_free(
    Ltilde: arb_mat,
    LLT: arb_mat,
    pairs: list[tuple[int, int]],
) -> dict:
    n = Ltilde.nrows()

    def scalar(i: int, j: int) -> arb:
        s = arb(0)
        for k in range(n):
            s += Ltilde[i, k] * Ltilde[j, k]
        return s

    return _overlap_audit(
        pairs,
        lambda i, j: LLT[i, j],
        scalar,
    )


def cholesky_llt(M: arb_mat, lambda0: float) -> tuple[arb_mat, arb_mat]:
    """Ltilde and the arb_mat product Ltilde Ltilde^T at the certified shift."""
    prev = mp.mp.dps
    mp.mp.dps = MP_DPS
    try:
        A = mid_mp_matrix(M)
        shift = mp.mpf(str(lambda0))
        for i in range(A.rows):
            A[i, i] -= shift
        Lmp = mp.cholesky(A)
        Ltilde = mp_to_arb_mat(Lmp)
        LLT = Ltilde * Ltilde.transpose()
        return Ltilde, LLT
    finally:
        mp.mp.dps = prev


def apply_quad_radii(
    C: arb_mat,
    orders: list[int],
    L: arb,
    M_psi: arb,
    n_panels: int,
    panel_fac: arb,
) -> tuple[arb, arb]:
    """Add per-entry Trefethen remainder as ball radius.  Returns (max eps_Q, ||E_Q||_inf)."""
    n_modes = len(orders)
    max_eps = arb(0)
    inf_norm = arb(0)
    for i, n in enumerate(orders):
        row = arb(0)
        for j, m in enumerate(orders):
            # integrand of C is (1/pi) * (Psi-beta) That_n That_m
            Mnm = entry_M(n, m, L, M_psi) / arb.pi()
            eps = arb(n_panels) * panel_fac * Mnm
            C[i, j] = add_radius(C[i, j], eps)
            row += eps
            if eps > max_eps:
                max_eps = eps
        if row > inf_norm:
            inf_norm = row
    return max_eps, inf_norm


def form_M(
    C: arb_mat,
    poles: list[arb],
    beta: arb,
    pole_sign: int,
) -> arb_mat:
    n = C.nrows()
    M = arb_mat(n, n)
    two = arb(2) * arb(pole_sign)
    for i in range(n):
        for j in range(n):
            M[i, j] = C[i, j] + two * poles[i] * poles[j]
        M[i, i] = M[i, i] + beta
    return M


# ---------------------------------------------------------------------------
# Tail / coupling (orders >= n_cut)
# ---------------------------------------------------------------------------

def that_max_bound(n: int, L: arb, Tsharp: arb) -> arb:
    return that_scale(n, L) * jn_bound_real(n, Tsharp * L)


def pole_abs_bound(n: int, L: arb) -> arb:
    half = L / arb(2)
    return that_scale(n, L) * jn_bound_complex(n, half)


def tail_constants(
    lead_orders: list[int],
    L: arb,
    Tsharp: arb,
    S_real: arb,
    n_cut: int,
    parity: int,
    max_tail: int = 2000,
) -> tuple[arb, arb, dict]:
    """eps_D (Gershgorin tail), eps_B (Schur leading-tail).  Infinite tail summed."""
    tail = list(range(n_cut, n_cut + max_tail, 2 if parity == 0 else 2))
    if parity == 1:
        if n_cut % 2 == 0:
            n_cut = n_cut + 1
        tail = list(range(n_cut, n_cut + max_tail, 2))

    that_t = [that_max_bound(n, L, Tsharp) for n in tail]
    pole_t = [pole_abs_bound(n, L) for n in tail]
    that_l = [that_max_bound(n, L, Tsharp) for n in lead_orders]
    pole_l = [pole_abs_bound(n, L) for n in lead_orders]

    pref = (Tsharp / arb.pi()) * S_real
    sum_that_t = sum(that_t, arb(0))
    sum_pole_t = sum(pole_t, arb(0))
    last = that_t[-1]
    # remainder of a super-exponential series: last * 2 is safe (ratio << 1/2)
    sum_that_t += last * arb(2)
    sum_pole_t += pole_t[-1] * arb(2)

    # eps_D: max tail-row of sum_j (2|p_i p_j| + |C_ij|)
    eps_D = arb(0)
    for thi, pi in zip(that_t, pole_t):
        row = pref * thi * sum_that_t + arb(2) * pi * sum_pole_t
        if row > eps_D:
            eps_D = row

    # ||B||_inf = max_lead sum_tail |B|,  ||B||_1 = max_tail sum_lead |B|
    b_inf = arb(0)
    for thl, pl in zip(that_l, pole_l):
        row = pref * thl * sum_that_t + arb(2) * pl * sum_pole_t
        if row > b_inf:
            b_inf = row
    sum_that_l = sum(that_l, arb(0))
    sum_pole_l = sum(pole_l, arb(0))
    b_one = arb(0)
    for thi, pi in zip(that_t, pole_t):
        col = pref * thi * sum_that_l + arb(2) * pi * sum_pole_l
        if col > b_one:
            b_one = col
    eps_B = (b_inf * b_one).sqrt()
    info = {
        "n_cut": n_cut,
        "n_tail_summed": len(tail),
        "that_cut_abs_upper": float(that_t[0].abs_upper()),
        "pole_cut_abs_upper": float(pole_t[0].abs_upper()),
    }
    return eps_D, eps_B, info


# ---------------------------------------------------------------------------
# Midpoint linear algebra (non-certified spectra; certified residual)
# ---------------------------------------------------------------------------

def arb_to_mp(x: arb) -> mp.mpf:
    return mp.mpf(x.mid().str(int(mp.mp.dps) + 12, radius=False))


def mid_mp_matrix(M: arb_mat) -> mp.matrix:
    n = M.nrows()
    A = mp.matrix(n)
    Md = M.mid()
    for i in range(n):
        for j in range(n):
            A[i, j] = arb_to_mp(Md[i, j])
    return A


def mp_to_arb_mat(A: mp.matrix) -> arb_mat:
    n = A.rows
    M = arb_mat(n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = arb(str(A[i, j]))
    return M


def reference_eigs(M: arb_mat, k: int) -> list[float]:
    prev = mp.mp.dps
    mp.mp.dps = MP_DPS
    try:
        A = mid_mp_matrix(M)
        ev = mp.eigsy(A, eigvals_only=True)
        vals = sorted(float(ev[i]) for i in range(A.rows))
        return vals[:k]
    finally:
        mp.mp.dps = prev


def identity_arb(n: int) -> arb_mat:
    I = arb_mat(n, n)
    for i in range(n):
        I[i, i] = arb(1)
    return I


def cholesky_residual_fixed(M: arb_mat, lambda0: float) -> tuple[bool, arb, str]:
    prev = mp.mp.dps
    mp.mp.dps = MP_DPS
    try:
        A = mid_mp_matrix(M)
        n = A.rows
        shift = mp.mpf(str(lambda0))
        for i in range(n):
            A[i, i] -= shift
        try:
            Lmp = mp.cholesky(A)
        except ValueError as exc:
            return False, arb(0), f"cholesky_failed:{exc}"
        Ltilde = mp_to_arb_mat(Lmp)
        I = identity_arb(n)
        E = M - arb(str(lambda0)) * I - (Ltilde * Ltilde.transpose())
        r = inf_norm_from_abs_upper(E)
        return True, r, "ok"
    finally:
        mp.mp.dps = prev


def certify_lambda(
    M: arb_mat,
    lambda0: float,
    beta: arb,
    eps_D: arb,
    eps_B: arb,
) -> dict:
    ok, r, reason = cholesky_residual_fixed(M, lambda0)
    out = {
        "lambda0": lambda0,
        "cholesky_ok": ok,
        "reason": reason,
        "r": arb_json(r) if ok else None,
    }
    if not ok:
        out["lambda_min_lower"] = None
        out["certified"] = None
        return out
    lmin = arb(str(lambda0)) - r
    floor = beta - eps_D
    certified = (lmin if lmin < floor else floor) - eps_B
    out["lambda_min_lower"] = arb_json(lmin)
    out["certified"] = arb_json(certified)
    return out


def bisect_certified(
    M: arb_mat,
    start: float,
    beta: arb,
    eps_D: arb,
    eps_B: arb,
    hi_hint: float,
    steps: int = 10,
) -> dict:
    lo_fail = start
    # search downward if start fails
    attempts = []
    cur = start
    rec = certify_lambda(M, cur, beta, eps_D, eps_B)
    attempts.append(rec)
    if not rec["cholesky_ok"]:
        for _ in range(12):
            cur *= 0.5
            if cur < 1e-40:
                break
            rec = certify_lambda(M, cur, beta, eps_D, eps_B)
            attempts.append(rec)
            if rec["cholesky_ok"]:
                break
        if not rec["cholesky_ok"]:
            return {"best": rec, "attempts": attempts, "largest_lambda0": None}
        lo_ok = cur
        hi = lo_fail
    else:
        lo_ok = cur
        hi = min(hi_hint, ffloat(beta) * 0.9)
        if hi <= lo_ok * 1.01:
            hi = lo_ok * 4.0
    for _ in range(steps):
        mid = math.sqrt(lo_ok * hi) if hi > 0 and lo_ok > 0 else 0.5 * (lo_ok + hi)
        rec = certify_lambda(M, mid, beta, eps_D, eps_B)
        attempts.append(rec)
        if rec["cholesky_ok"]:
            lo_ok = mid
        else:
            hi = mid
    best = certify_lambda(M, lo_ok, beta, eps_D, eps_B)
    attempts.append(best)
    return {"best": best, "attempts_count": len(attempts), "largest_lambda0": lo_ok}


# ---------------------------------------------------------------------------
# Quadrature-refinement sanity check (not the certificate)
# ---------------------------------------------------------------------------

def refinement_pairs(
    orders: list[int], n_spot: int, rng: random.Random
) -> list[tuple[int, int]]:
    n = len(orders)
    small = orders[: max(5, n // 10)]
    mid = orders[n // 4 : n // 4 + max(5, n // 10)]
    large = orders[-max(5, n // 10) :]
    pairs: list[tuple[int, int]] = [
        (orders[0], orders[0]),
        (orders[0], orders[n // 2]),
        (orders[n // 2], orders[n // 2]),
        (orders[0], orders[-1]),
        (orders[-1], orders[-1]),
    ]
    bands = [small, mid, large]
    while len(pairs) < n_spot:
        band = rng.choice(bands)
        a, b = rng.choice(band), rng.choice(band)
        if a > b:
            a, b = b, a
        if (a, b) not in pairs:
            pairs.append((a, b))
    return pairs


def spotcheck_refinement(
    C: arb_mat,
    orders: list[int],
    L: arb,
    Tsharp: float,
    beta: arb,
    terms: list[tuple[int, arb, arb]],
    pairs: list[tuple[int, int]],
    M_psi: arb,
) -> dict:
    """Recompute selected C_nm at h=1/8, n_G=32; require ball overlap."""
    h_fine = 0.125
    n_g_fine = 32
    nodes, weights = gauss_legendre(n_g_fine)
    idx = {n: i for i, n in enumerate(orders)}
    emit(f"  refinement assemble h={h_fine} n_G={n_g_fine} pairs={len(pairs)}")
    fine, _st = assemble_C(
        orders,
        L,
        Tsharp,
        h_fine,
        n_g_fine,
        beta,
        terms,
        nodes,
        weights,
        "refine",
        only_pairs=pairs,
    )
    n_panels = int(round(Tsharp / h_fine))
    rho = bernstein_rho(h_fine)
    panel_fac = panel_quad_factor(arb(str(h_fine)), n_g_fine, rho)
    discrepancies = []
    overlaps = 0
    max_disc = arb(0)
    max_rad_coarse = arb(0)
    max_rad_fine = arb(0)
    for n, m in pairs:
        entry = fine[(n, m)]
        Mnm = entry_M(n, m, L, M_psi) / arb.pi()
        eps = arb(n_panels) * panel_fac * Mnm
        entry = add_radius(entry, eps)
        coarse = C[idx[n], idx[m]]
        ov = bool(coarse.overlaps(entry))
        disc = abs(coarse.mid() - entry.mid())
        if disc > max_disc:
            max_disc = disc
        if coarse.rad() > max_rad_coarse:
            max_rad_coarse = coarse.rad()
        if entry.rad() > max_rad_fine:
            max_rad_fine = entry.rad()
        discrepancies.append(
            {
                "n": n,
                "m": m,
                "coarse_mid": float(coarse.mid()),
                "fine_mid": float(entry.mid()),
                "coarse_rad": float(coarse.rad()),
                "fine_rad": float(entry.rad()),
                "discrepancy": float(disc.mid()),
                "overlap": ov,
            }
        )
        if ov:
            overlaps += 1
    return {
        "kind": "quadrature_refinement",
        "h_fine": h_fine,
        "n_G_fine": n_g_fine,
        "n_pairs": len(pairs),
        "n_overlap": overlaps,
        "max_discrepancy": float(max_disc.mid()),
        "max_coarse_rad": float(max_rad_coarse.mid()),
        "max_fine_rad": float(max_rad_fine.mid()),
        "pairs": discrepancies,
    }


# ---------------------------------------------------------------------------
# Validations
# ---------------------------------------------------------------------------

def validate_constants(L: arb, terms, A_L: arb) -> dict:
    checks = {}
    al = ffloat(A_L)
    checks["A_L"] = {
        "value": arb_json(A_L),
        "paper": PAPER_AL,
        "rel_err": abs(al - PAPER_AL) / PAPER_AL,
        "ok": abs(al - PAPER_AL) < 1e-6,
    }
    b200 = beta_star_of(arb(200), A_L)
    b150 = beta_star_of(arb(150), A_L)
    checks["beta_200"] = {
        "value": arb_json(b200),
        "paper": PAPER_BETA_200,
        "ok": abs(ffloat(b200) - PAPER_BETA_200) < 1e-6,
    }
    checks["beta_150"] = {
        "value": arb_json(b150),
        "paper": PAPER_BETA_150,
        "ok": abs(ffloat(b150) - PAPER_BETA_150) < 5e-4,
    }

    p0_closed = arb(4) * arb("0.4").sinh() / arb("1.6").sqrt()
    p0_bessel = that_scale(0, L) * sph_i(0, L / arb(2))
    checks["p0_closed_vs_bessel"] = {
        "closed": arb_json(p0_closed),
        "bessel": arb_json(p0_bessel),
        "ok": bool(p0_closed.overlaps(p0_bessel)),
    }

    # n=0 quadrature vs closed form
    Lacb = acb(L)

    def f0(x, analytic):
        return T_basis(0, x, Lacb) * (x / acb(2)).cosh()

    I0 = acb.integral(f0, -Lacb, Lacb, abs_tol=arb("1e-40"))
    checks["p0_integral"] = {
        "integral": arb_json(I0.real),
        "closed": arb_json(p0_closed),
        "ok": bool(I0.real.overlaps(p0_closed)),
    }

    def f2(x, analytic):
        return T_basis(2, x, Lacb) * (x / acb(2)).cosh()

    I2 = acb.integral(f2, -Lacb, Lacb, abs_tol=arb("1e-40"))
    p2 = that_scale(2, L) * sph_i(2, L / arb(2))
    checks["p2_integral_vs_bessel"] = {
        "integral": arb_json(I2.real),
        "bessel": arb_json(p2),
        "ok": bool(I2.real.overlaps(p2)),
    }

    def g1(x, analytic):
        return T_basis(1, x, Lacb) * (x / acb(2)).sinh()

    I1 = acb.integral(g1, -Lacb, Lacb, abs_tol=arb("1e-40"))
    q1 = that_scale(1, L) * sph_i(1, L / arb(2))
    checks["q1_integral_vs_bessel"] = {
        "integral": arb_json(I1.real),
        "bessel": arb_json(q1),
        "ok": bool(I1.real.overlaps(q1)),
    }

    # spherical Bessel identities
    x = arb("1.3")
    j0 = sph_j_real(0, x / L, L)  # j_0(x) with t = x/L so tL = x
    # call directly
    j0 = sph_j(0, acb(x)).real
    j0c = x.sin() / x
    j1 = sph_j(1, acb(x)).real
    j1c = x.sin() / (x * x) - x.cos() / x
    checks["j0_identity"] = {"ok": bool(j0.overlaps(j0c))}
    checks["j1_identity"] = {"ok": bool(j1.overlaps(j1c))}
    i0 = sph_i(0, arb("0.4"))
    i0c = arb("0.4").sinh() / arb("0.4")
    checks["i0_identity"] = {"ok": bool(i0.overlaps(i0c))}

    # Miller: series seeds, j_0 contains sinc, no pointizing
    miller_ok = True
    miller_rel = arb(0)
    for xv in (arb("0.4"), arb("1.3"), arb(8), arb(40), arb(160)):
        js, inf = sph_j_miller(20 if float(xv.mid()) < 20 else 80, xv)
        if not inf["j0_ok"]:
            miller_ok = False
        if inf["worst_rel"] > miller_rel:
            miller_rel = inf["worst_rel"]
        if not js[0].contains(xv.sin() / xv):
            miller_ok = False
    checks["miller_j0_and_series_seed"] = {
        "ok": miller_ok,
        "worst_rel": arb_json(miller_rel),
    }
    return checks


def envelope_grid(terms, A_L: arb, t_hi: float = 400.0, npts: int = 80) -> dict:
    ts = [ENVELOPE_T_MIN]
    if npts > 2:
        geo = [
            ENVELOPE_T_MIN * (t_hi / ENVELOPE_T_MIN) ** (k / (npts - 2))
            for k in range(npts - 1)
        ]
        ts = [ENVELOPE_T_MIN] + geo
    n_ok = 0
    min_margin = None
    worst_t = None
    for t in ts:
        ta = arb(str(t))
        gap = psi_L_real(ta, terms) - envelope_minorant(ta, A_L)
        # lemma claims gap >= 0
        ok = bool(gap.lower() >= 0 or (gap.lower() < 0 and gap.abs_upper() < arb("1e-20")))
        if gap.lower() >= 0:
            n_ok += 1
            m = float(gap.lower())
        else:
            m = float(gap.lower())
            if abs(m) < 1e-20:
                n_ok += 1
        if min_margin is None or m < min_margin:
            min_margin = m
            worst_t = t
    return {
        "n_points": len(ts),
        "n_ok": n_ok,
        "min_margin": min_margin,
        "worst_t": worst_t,
        "ok": n_ok == len(ts),
    }


# ---------------------------------------------------------------------------
# One sector
# ---------------------------------------------------------------------------

def run_sector(
    *,
    name: str,
    orders: list[int],
    L: arb,
    Tsharp: float,
    h: float,
    n_g: int,
    beta: arb,
    terms,
    A_L: arb,
    M_psi: arb,
    S_real: arb,
    nodes,
    weights,
    lambda0_start: float,
    n_eigs: int,
    pole_sign: int,
    n_cut: int,
    do_spot: bool,
    n_spot: int,
    n_audit: int,
    rng: random.Random,
) -> dict:
    emit(f"\n== sector {name}  T#={Tsharp}  modes={len(orders)}  n_G={n_g} ==")
    t_sec = time.time()
    n_panels = int(round(Tsharp / h))
    rho = bernstein_rho(h)
    panel_fac = panel_quad_factor(arb(str(h)), n_g, rho)
    emit(f"  rho={float(rho.mid()):.6f}  panels={n_panels}")

    poles = pole_vector(orders, L)
    emit(f"  pole[0]={float(poles[0].mid()):.12e}  |p_last|={float(abs(poles[-1]).mid()):.3e}")

    C_audit_pairs = refinement_pairs(orders, n_audit, rng)
    C, miller_stats = assemble_C(
        orders,
        L,
        Tsharp,
        h,
        n_g,
        beta,
        terms,
        nodes,
        weights,
        name,
        audit_pairs=C_audit_pairs,
    )
    emit(
        f"  miller seeds={miller_stats['seeds']}  "
        f"j0={miller_stats['j0_passed']}/{miller_stats['j0_checks']}  "
        f"worst_rel={float(miller_stats['worst_rel'].abs_upper()):.3e}  "
        f"lt_1e40={miller_stats['rel_below_1e40']}"
    )
    acc = miller_stats.get("fft_free_C_acc")
    c_audit = (
        audit_C_fft_free(C, orders, acc)
        if acc
        else {"n_pairs": 0, "n_overlap": 0}
    )
    emit(
        f"  fft-free C_nm {c_audit.get('n_overlap', 0)}/{c_audit.get('n_pairs', 0)}  "
        f"max disc={c_audit.get('max_discrepancy')}  "
        f"rad mat/scalar={c_audit.get('max_mat_rad')}/{c_audit.get('max_scalar_rad')}"
    )
    max_eps, eq_inf = apply_quad_radii(C, orders, L, M_psi, n_panels, panel_fac)
    emit(
        f"  max eps_Q={float(max_eps.abs_upper()):.3e}  "
        f"||E_Q||_inf={float(eq_inf.abs_upper()):.3e}"
    )

    M = form_M(C, poles, beta, pole_sign)
    eps_D, eps_B, tail_info = tail_constants(
        orders, L, arb(str(Tsharp)), S_real, n_cut, orders[0] % 2
    )
    emit(
        f"  eps_D={float(eps_D.abs_upper()):.3e}  "
        f"eps_B={float(eps_B.abs_upper()):.3e}  "
        f"that_cut={tail_info['that_cut_abs_upper']:.3e}"
    )

    emit("  reference spectrum (mpmath eigsy, midpoint, non-certified)...")
    t_e = time.time()
    eigs = reference_eigs(M, n_eigs)
    emit(f"  eigs={eigs}  ({time.time() - t_e:.1f}s)")

    hi_hint = max(abs(eigs[0]) * 1.2, lambda0_start * 2) if eigs else lambda0_start * 2
    emit(f"  certificate starting at lambda0={lambda0_start:.3e}")
    paper_try = certify_lambda(M, lambda0_start, beta, eps_D, eps_B)
    emit(
        f"  paper-target chol_ok={paper_try['cholesky_ok']}  "
        f"certified={None if paper_try['certified'] is None else paper_try['certified']['float']}"
    )
    bis = bisect_certified(M, lambda0_start, beta, eps_D, eps_B, hi_hint)
    best = bis["best"]
    emit(
        f"  largest lambda0={bis['largest_lambda0']}  "
        f"best certified={None if best.get('certified') is None else best['certified']['float']}"
    )

    llt_audit = {"n_pairs": 0, "n_overlap": 0}
    if bis["largest_lambda0"] is not None and ffloat(beta) > 0:
        Ltilde, LLT = cholesky_llt(M, bis["largest_lambda0"])
        nM = Ltilde.nrows()
        llt_pairs = refinement_pairs(list(range(nM)), n_audit, rng)
        llt_audit = audit_llt_fft_free(Ltilde, LLT, llt_pairs)
        emit(
            f"  fft-free LLT {llt_audit['n_overlap']}/{llt_audit['n_pairs']}  "
            f"max disc={llt_audit.get('max_discrepancy')}  "
            f"rad mat/scalar={llt_audit.get('max_mat_rad')}/{llt_audit.get('max_scalar_rad')}"
        )

    spot = None
    if do_spot:
        emit("  quadrature-refinement spot-check...")
        pairs = refinement_pairs(orders, n_spot, rng)
        spot = spotcheck_refinement(
            C, orders, L, Tsharp, beta, terms, pairs, M_psi
        )
        emit(
            f"  refine overlap {spot['n_overlap']}/{spot['n_pairs']}  "
            f"max disc={spot['max_discrepancy']}  "
            f"rad coarse/fine={spot['max_coarse_rad']:.3e}/{spot['max_fine_rad']:.3e}"
        )

    certified_val = None
    if best.get("certified") is not None:
        certified_val = best["certified"]["float"]
    elif paper_try.get("certified") is not None:
        certified_val = paper_try["certified"]["float"]

    verdict = "INCONCLUSIVE(cholesky_failed)"
    if ffloat(beta) <= 0:
        verdict = "INCONCLUSIVE(beta_star_nonpositive)"
    elif certified_val is not None and certified_val > 0:
        verdict = f"CERTIFIED({certified_val:.6e})"
    elif certified_val is not None:
        verdict = f"INCONCLUSIVE(certified_nonpositive:{certified_val:.3e})"

    return {
        "name": name,
        "Tsharp": Tsharp,
        "n_modes": len(orders),
        "orders_first_last": [orders[0], orders[-1]],
        "h": h,
        "n_G": n_g,
        "n_panels": n_panels,
        "rho": arb_json(rho),
        "beta_star": arb_json(beta),
        "pole0": arb_json(poles[0]),
        "max_eps_Q": arb_json(max_eps),
        "E_Q_inf": arb_json(eq_inf),
        "eps_D": arb_json(eps_D),
        "eps_B": arb_json(eps_B),
        "tail": tail_info,
        "reference_eigenvalues": eigs,
        "paper_target": paper_try,
        "bisection": {
            "largest_lambda0": bis["largest_lambda0"],
            "best": best,
            "attempts_count": bis.get("attempts_count"),
        },
        "spotcheck": spot,
        "fft_free_audit": {"C_nm": c_audit, "LLT": llt_audit},
        "miller": {
            "seeds": miller_stats["seeds"],
            "worst_rel_radius": arb_json(miller_stats["worst_rel"]),
            "rel_below_1e40": miller_stats["rel_below_1e40"],
            "j0_consistency": {
                "ok": miller_stats["j0_ok"],
                "checks": miller_stats["j0_checks"],
                "passed": miller_stats["j0_passed"],
            },
        },
        "certified_constant": certified_val,
        "verdict": verdict,
        "runtime_sec": time.time() - t_sec,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=FENCE)
    p.add_argument("--smoke", action="store_true", help="N=60, T#=60, h=1/2, n_G=16")
    p.add_argument("--full", action="store_true", help="paper configuration (default)")
    p.add_argument("--n-g", type=int, default=None, help="Gauss nodes (32 or 24)")
    p.add_argument("--n-modes", type=int, default=None)
    p.add_argument(
        "--tsharp",
        type=float,
        action="append",
        default=None,
        help="Override T# list (repeatable). Default full: 200 and 150.",
    )
    p.add_argument("--skip-odd", action="store_true")
    p.add_argument("--skip-spotcheck", action="store_true")
    p.add_argument("--n-spot", type=int, default=30)
    p.add_argument("--n-audit", type=int, default=40)
    p.add_argument("--out", type=Path, default=RESULT_JSON)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    smoke = bool(args.smoke)
    t_all = time.time()
    ctx.prec = WORKING_BITS
    mp.mp.dps = MP_DPS
    rng = random.Random(20260904)
    flint_fft = check_flint_signed_fft()

    L = arb("0.8")
    if smoke:
        n_modes = args.n_modes or 60
        T_list_even = [60.0]
        h = 0.5
        n_g = args.n_g or 16
        do_odd = False
        n_cut_even = 2 * n_modes
        lambda0_map = {60.0: 1e-20}
        n_eigs_even = 5
    else:
        n_modes = args.n_modes or 200
        T_list_even = args.tsharp if args.tsharp else [200.0, 150.0]
        h = 0.25
        n_g = args.n_g or 32
        do_odd = not args.skip_odd
        n_cut_even = 2 * n_modes  # first discarded even order
        lambda0_map = {200.0: 9e-18, 150.0: 1.2e-18}
        n_eigs_even = 5
        for T in T_list_even:
            lambda0_map.setdefault(T, 1.2e-18)

    emit(f"weil_window_certificate_probe  {FENCE}")
    emit(f"prec={WORKING_BITS} bits  n_modes={n_modes}  n_G={n_g}  h={h}  smoke={smoke}")

    terms = comb_terms(L)
    A_L = A_L_of(terms)
    emit(f"comb n={[n for n,_,_ in terms]}  A_L={float(A_L.mid()):.10f}")

    emit("validating constants / pole / Bessel identities...")
    checks = validate_constants(L, terms, A_L)
    env = envelope_grid(terms, A_L, t_hi=400.0 if not smoke else 80.0)
    checks["envelope_lemma_grid"] = env
    for k, v in checks.items():
        if k == "envelope_lemma_grid":
            emit(f"  [{('PASS' if v['ok'] else 'FAIL')}] {k}  {v['n_ok']}/{v['n_points']}  min_margin={v['min_margin']}")
        elif isinstance(v, dict) and "ok" in v:
            emit(f"  [{('PASS' if v['ok'] else 'FAIL')}] {k}")

    emit("covering M_Psi on the Bernstein rectangle...")
    T_cover = max(T_list_even)
    t_c = time.time()
    # M_Psi is independent of beta* at leading order; use T#=200 beta for the
    # shift, then inflate by |beta_200 - beta_other| when needed.
    beta_cover = beta_star_of(arb(str(T_cover)), A_L)
    M_psi, n_cov, n_spl = cover_M_psi(T_cover, beta_cover, terms)
    emit(
        f"  M_Psi <= {float(M_psi.abs_upper()):.6f}  "
        f"evals={n_cov} splits={n_spl} ({time.time() - t_c:.2f}s)"
    )

    nodes, weights = gauss_legendre(n_g)
    even_orders = list(range(0, 2 * n_modes, 2))
    odd_orders = list(range(1, 2 * n_modes, 2))

    sectors = []
    for T in T_list_even:
        beta = beta_star_of(arb(str(T)), A_L)
        emit(f"real-line covering of |Psi-beta*| on [0, {T}]...")
        S_real = cover_real_sup(T, beta, terms)
        # rectangle was covered at beta_cover; inflate M_Psi for this beta
        M_use = M_psi + (beta - beta_cover).abs_upper()
        emit(f"  S_real <= {float(S_real.abs_upper()):.6f}  M_use={float(M_use.abs_upper()):.6f}")
        sec = run_sector(
            name=f"even_T{int(T)}",
            orders=even_orders,
            L=L,
            Tsharp=T,
            h=h,
            n_g=n_g,
            beta=beta,
            terms=terms,
            A_L=A_L,
            M_psi=M_use,
            S_real=S_real,
            nodes=nodes,
            weights=weights,
            lambda0_start=lambda0_map[T],
            n_eigs=n_eigs_even,
            pole_sign=+1,
            n_cut=n_cut_even,
            do_spot=not args.skip_spotcheck,
            n_spot=args.n_spot if not smoke else min(args.n_spot, 8),
            n_audit=args.n_audit if not smoke else min(args.n_audit, 8),
            rng=rng,
        )
        sectors.append(sec)

    if do_odd:
        T = 150.0
        beta = beta_star_of(arb(150), A_L)
        S_real = cover_real_sup(T, beta, terms)
        M_use = M_psi + (beta - beta_cover).abs_upper()
        sec = run_sector(
            name="odd_T150",
            orders=odd_orders,
            L=L,
            Tsharp=T,
            h=h,
            n_g=n_g,
            beta=beta,
            terms=terms,
            A_L=A_L,
            M_psi=M_use,
            S_real=S_real,
            nodes=nodes,
            weights=weights,
            lambda0_start=8.2065e-15,
            n_eigs=3,
            pole_sign=-1,
            n_cut=2 * n_modes + 1,
            do_spot=not args.skip_spotcheck,
            n_spot=args.n_spot if not smoke else min(args.n_spot, 8),
            n_audit=args.n_audit if not smoke else min(args.n_audit, 8),
            rng=rng,
        )
        sectors.append(sec)

    # overall verdict: primary is even T#=200 (or the only even sector in smoke)
    primary = sectors[0]
    for s in sectors:
        if s["name"] == "even_T200":
            primary = s
            break
    verdict = primary["verdict"]

    # calibration vs paper
    calib = {}
    for s in sectors:
        if s["name"] == "even_T150" and s["reference_eigenvalues"]:
            ev = s["reference_eigenvalues"]
            calib["even_T150"] = {
                "ours": ev,
                "paper": list(PAPER_EIG_150),
                "rel_err0": abs(ev[0] - PAPER_EIG_150[0]) / PAPER_EIG_150[0],
            }
        if s["name"] == "even_T200" and s["reference_eigenvalues"]:
            ev = s["reference_eigenvalues"]
            calib["even_T200"] = {
                "ours": ev,
                "paper_interval": [PAPER_EIG_200_LO, PAPER_EIG_200_HI],
                "in_interval": PAPER_EIG_200_LO <= ev[0] <= PAPER_EIG_200_HI * 1.1,
            }
        if s["name"] == "odd_T150" and s["reference_eigenvalues"]:
            ev = s["reference_eigenvalues"]
            calib["odd_T150"] = {
                "ours": ev,
                "paper": PAPER_EIG_ODD,
                "rel_err0": abs(ev[0] - PAPER_EIG_ODD) / PAPER_EIG_ODD,
            }

    payload = {
        "contract": CONTRACT,
        "fence": FENCE,
        "source": SOURCE,
        "smoke": smoke,
        "parameters": {
            "L": 0.8,
            "n_modes": n_modes,
            "h": h,
            "n_G": n_g,
            "working_bits": WORKING_BITS,
            "mpmath_dps": MP_DPS,
            "strip_b": STRIP_B,
            "cover_side": COVER_SIDE,
            "comb_n": [n for n, _, _ in terms],
        },
        "A_L": arb_json(A_L),
        "beta_star": {s["name"]: s["beta_star"] for s in sectors},
        "M_Psi": arb_json(M_psi),
        "M_Psi_cover": {"n_eval": n_cov, "n_split": n_spl},
        "validations": {
            k: (
                {kk: vv for kk, vv in v.items() if kk != "pairs"}
                if k == "envelope_lemma_grid"
                else v
            )
            for k, v in checks.items()
        },
        "sectors": sectors,
        "calibration": calib,
        "flint_signed_fft_regression": flint_fft["flint_signed_fft_regression"],
        "flint_version": flint_fft["flint_version"],
        "python_flint": flint_fft["python_flint"],
        "fft_free_audit": {s["name"]: s.get("fft_free_audit") for s in sectors},
        "miller_seeds": "rigorous_power_series",
        "miller_node_radius": (
            "mean_value_DE_remainder_plus_series_on_original_ball; "
            "raw-ball recurrence wraps (dominant solution)"
        ),
        "miller_worst_rel_radius": max(
            (
                s.get("miller", {}).get("worst_rel_radius", {}).get("float", 0.0)
                for s in sectors
            ),
            default=0.0,
        ),
        "miller_j0_consistency": {
            s["name"]: s.get("miller", {}).get("j0_consistency") for s in sectors
        },
        "runtime_sec": time.time() - t_all,
        "sha256": file_sha256(Path(__file__)),
        "verdict": verdict,
    }

    args.out.write_text(json.dumps(payload, indent=2, default=str) + "\n")
    emit("")
    emit(f"wrote {args.out}")
    emit(f"verdict {verdict}")
    emit(f"runtime {payload['runtime_sec']:.1f}s")
    emit("== report ==")
    emit(f"A_L = {float(A_L.mid()):.10f}  (paper {PAPER_AL})")
    for s in sectors:
        emit(
            f"{s['name']}: beta*={s['beta_star']['float']:.10f}  "
            f"eigs={s['reference_eigenvalues']}  "
            f"cert={s['certified_constant']}  {s['verdict']}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
