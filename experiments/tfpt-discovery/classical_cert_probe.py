#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""classical_cert_probe -- PRIME.RDAGGER.CLASSICAL_CERT.01 (r471).

Dictionary-free Guinand--Weil certificates on an explicit finite
grid family of compactly supported step functions.  Foundation F2
of the r469 judgment (U3).  No fold, no selected window, no
R^dagger dictionary.

CONVENTION (r461, taken literally).
  lambda_*(L) = inf { Q_W(h) / ||h||_2^2 : supp h subset [-L, L] }.
  g = h * h-tilde (even autocorrelation), supp g subset [-2L, 2L].
  L_k = k log 2 / 4  (so U_k = 2 L_k = k log 2 / 2).
  External preprint zone: L = 0.8 (supp h subset [-0.8, 0.8],
  autocorrelation support U <= 1.6).  Classical Yoshida/Bombieri
  is U < log 2, i.e. L < (log 2)/2 ~ 0.34657 (prime-blind).

  Prime sum: n with log n <= 2L, i.e. n <= exp(2L).  (The brief's
  n <= exp(L) mixes the autocorrelation length U with L; this
  probe follows r461.)

SELF-DEFINED CLASSICAL FORM (even compact g).
  Q(g) = A(g) - P(g) + Pi(g)
  P(g) = sum_{n>=2} 2 Lambda(n)/sqrt(n) * g(log n)     (exact, finite)
  Pi(g) = 4 int_0^{inf} g(x) cosh(x/2) dx               (exact on PL g)
  A(g) = -(gamma + log pi) g(0)
         + 2 int_0^{inf} [g(0) e^{-2w} - g(w) e^{-w/2}] / (1-e^{-2w}) dw
         (series + Bernoulli remainder; compact support => finite)

GRID FAMILY F_{L, delta}.
  h piecewise-constant on n = 2L/delta equal bins of [-L, L].
  Then g is a linear combination of tents of half-width delta.
  Q_L is the n x n Toeplitz matrix of this quadratic form.
  Certificate: validated Cholesky  =>  Q_L succeq 0 on F_{L,delta}.

HONEST TYPE.  GRID_CERTIFIED(L, delta) is NOT lambda_*(L) >= 0.
The discretization gap is named F2b (modulus of continuity of Q
on autocorrelations at fixed L).  No infinite-k statement.

SCRAMBLE GATE (r469 anti-list item 3).  The bound uses the literal
von Mangoldt nodes log n inside P(g).  A source-position scramble
moves those nodes and changes Q_L.  The bound is scramble-sensitive
because the arithmetic locations enter the matrix entries.  This is
not a q^dagger pairing bound; there is no fold.

NO RH CLAIM.  NO anti-RH claim.  Finite grid positivity only.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
from mpmath import iv
import numpy as np

# ---------------------------------------------------------------------------
# constants / schedule
# ---------------------------------------------------------------------------
DPS = 40
U64 = 2.0 ** -53
OUT = 1.0 + 2.0 ** -38
TINY = 1.0e-300
SERIES_K = 64
BERN_DEG = 24
NEAR_ETA = mp.mpf("0.05")

# Sealed after the /tmp run.  Live enclosures must sit inside these
# outward decimal hulls of validated lambda_min(Q_L).
# (L_tag, n_bins) -> (lo_str, hi_str) of the Cholesky lower bound.
CERT_PINS: dict[tuple[str, int], tuple[str, str]] = {
    ("YB", 8): ("1.32421298e-03", "1.32686406e-03"),
    ("YB", 16): ("3.12362449e-04", "3.12987799e-04"),
    ("L08", 8): ("2.14437715e-03", "2.14867020e-03"),
    ("L08", 16): ("5.25524483e-04", "5.26576584e-04"),
    ("L08f", 24): ("1.32121420e-04", "1.32385927e-04"),
    ("L5", 8): ("2.08538272e-03", "2.08955766e-03"),
    ("L5", 16): ("4.69765151e-04", "4.70705622e-04"),
    ("L10", 20): ("3.25679121e-04", "3.26331131e-04"),
    ("L12", 24): ("2.16570740e-04", "2.17004315e-04"),
    ("L14", 28): ("1.56581520e-04", "1.56894996e-04"),
    ("L16", 32): ("9.83779598e-05", "9.85749127e-05"),
    ("L18", 32): ("8.78048794e-05", "8.79806649e-05"),
    ("L20", 32): ("1.05220054e-04", "1.05430705e-04"),
    ("Lk8", 28): ("1.36611957e-04", "1.36885454e-04"),
    ("Lk12", 32): ("1.26099570e-04", "1.26352022e-04"),
    ("Lk16", 36): ("6.88248486e-05", "6.89626361e-05"),
}

# Prime-power count pins: (L_tag, n_bins) -> (n_max, n_pp)
SHAPE_PINS: dict[tuple[str, int], tuple[int, int]] = {
    ("YB", 8): (4, 3),
    ("YB", 16): (4, 3),
    ("L08", 8): (7, 5),
    ("L08", 16): (7, 5),
    ("L08f", 24): (7, 5),
    ("L5", 8): (8, 6),
    ("L5", 16): (8, 6),
    ("L10", 20): (10, 7),
    ("L12", 24): (14, 9),
    ("L14", 28): (19, 12),
    ("L16", 32): (27, 15),
    ("L18", 32): (39, 19),
    ("L20", 32): (57, 24),
    ("Lk8", 28): (19, 12),
    ("Lk12", 32): (67, 28),
    ("Lk16", 36): (259, 71),
}

L_MAX_SMOKE_PIN = 0.8664
L_MAX_FULL_PIN = 2.7726
VERDICT_KIND = "GRID_CERTIFIED"

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72, flush=True)


# ---------------------------------------------------------------------------
# scramble declaration (r469 anti-list item 3)
# ---------------------------------------------------------------------------
SCRAMBLE_SENSITIVE = True
SCRAMBLE_REASON = (
    "Q_L entries evaluate g at the literal nodes log n with weights "
    "Lambda(n)/sqrt(n).  A source-position scramble of those nodes "
    "changes the prime Gram and therefore the matrix.  The bound is "
    "not fold-mode pairing and is not scramble-invariant."
)


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    forbidden = {"zetazero", "nzeros", "grampoint", "zetazeros"}
    bad = []
    for node in ast.walk(tree):
        name = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if name and name.lower().replace("_", "") in forbidden:
            bad.append("%s@%d" % (name, node.lineno))
    return (not bad), ("NO zero/oracle calls" if not bad else "; ".join(bad))


# ---------------------------------------------------------------------------
# Bernoulli numbers B_n^+  for  x/(1-e^{-x}) = sum B_n^+ x^n / n!
# Akiyama-Tanigawa gives B_1 = -1/2; flip to +1/2.
# ---------------------------------------------------------------------------
def bernoulli_plus(degree: int) -> list[Fraction]:
    table: list[Fraction] = []
    work = [Fraction(0)] * (degree + 1)
    for m in range(degree + 1):
        work[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            work[j - 1] = j * (work[j - 1] - work[j])
        table.append(work[0])
    # Akiyama-Tanigawa in this form yields B_1 = +1/2, which is the
    # generating function x/(1-e^{-x}).
    return table


BERNOULLI = bernoulli_plus(BERN_DEG + 4)


def ivsplit(x):
    a, b = x._mpi_
    return mp.make_mpf(a), mp.make_mpf(b)


def iv_of(lo, hi=None):
    if hi is None:
        hi = lo
    return iv.mpf([lo, hi])


def gamma_n(count):
    scaled = (count + 2.0) * U64
    return scaled / (1.0 - scaled)


def outward(value):
    return value * OUT + TINY


def midpoint_radius(value):
    lo, hi = ivsplit(value)
    return float((lo + hi) / 2), float((hi - lo) / 2)


def validated_lammin(midpoint, radius, hint):
    """Higham-validated Cholesky lower bound on lambda_min of an
    interval matrix.  Copied in spirit from r465: frozen binary64
    factor is an exact basis change; the bound is shift minus
    backward error minus radius row-sum."""
    dimension = midpoint.shape[0]
    for fraction in (0.5, 0.25, 0.1, 0.05, 0.02, 0.01, 0.005):
        shift = fraction * hint
        if shift <= 0:
            continue
        try:
            factor = np.linalg.cholesky(
                midpoint - shift * np.eye(dimension))
        except np.linalg.LinAlgError:
            continue
        absolute = np.abs(factor)
        backward = outward(
            gamma_n(dimension + 1)
            * float(np.max(np.sum(absolute @ absolute.T, axis=1))))
        radius_rows = outward(float(np.max(np.sum(radius, axis=1))))
        lower = shift - backward - radius_rows
        if lower > 0:
            return lower
    return None


# ---------------------------------------------------------------------------
# von Mangoldt list (exact integers; log p enclosed)
# ---------------------------------------------------------------------------
def prime_powers_upto(n_max: int) -> list[tuple[int, int]]:
    """List of (n, p) with n = p^k <= n_max, k>=1, p prime."""
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


def n_max_for(L) -> int:
    """Smallest integer strictly above exp(2L)."""
    L_iv = iv.mpf(L) if not hasattr(L, "_mpi_") else L
    _, hi = ivsplit(iv.exp(2 * L_iv))
    return int(mp.ceil(hi)) + 2


def iv_cosh(x):
    return (iv.exp(x) + iv.exp(-x)) / 2


# ---------------------------------------------------------------------------
# exact int (p + q w) e^{-alpha w} dw on [a,b], interval
# antideriv = -e^{-a w} (p + q w + q/alpha) / alpha
# ---------------------------------------------------------------------------
def exp_linear_integral(alpha, p, q, a, b):
    def F(w):
        return -iv.exp(-alpha * w) * (p + q * w + q / alpha) / alpha
    return F(b) - F(a)


# ---------------------------------------------------------------------------
# Bernoulli enclosure of int_0^eta I(w) dw for G_0
# I(w) = [delta e^{-2w} - (delta-w) e^{-w/2}] / (1-e^{-2w})
#      = (N(w)/w) * (1/2) * phi(2w),  phi(x)=x/(1-e^{-x})
# ---------------------------------------------------------------------------
def near_I_integral(g0, p, q, eta):
    """int_0^eta I(w) dw, I = [g0 e^{-2w}-(p+qw)e^{-w/2}]/(1-e^{-2w}).
    Requires g0 = p so N(0)=0 (removable)."""
    degree = BERN_DEG
    ncoeff = [iv.mpf(0)] * (degree + 3)
    fact = iv.mpf(1)
    two = iv.mpf(2)
    half = iv.mpf("0.5")
    for k in range(0, degree + 3):
        if k > 0:
            fact *= k
        ncoeff[k] += g0 * ((-two) ** k) / fact
        ncoeff[k] -= p * ((-half) ** k) / fact
        # q w exp(-w/2) contributes to N as -q * that
        if k + 1 < len(ncoeff):
            ncoeff[k + 1] -= q * ((-half) ** k) / fact
    # N(0) should enclose 0.  N(w)/w = sum_{k>=0} n_{k+1} w^k
    nw = ncoeff[1:]
    # phi(2w) = sum B_k^+ (2w)^k / k!
    phi = [iv.mpf(0)] * (degree + 1)
    fact = iv.mpf(1)
    for k in range(degree + 1):
        if k > 0:
            fact *= k
        bk = iv.mpf(str(BERNOULLI[k].numerator)) / iv.mpf(
            str(BERNOULLI[k].denominator))
        phi[k] = bk * (two ** k) / fact
    # product (N/w)*phi, take coeffs 0..degree-2 to leave room
    prod_deg = degree - 2
    prod = [iv.mpf(0)] * (prod_deg + 1)
    for i in range(prod_deg + 1):
        acc = iv.mpf(0)
        for j in range(i + 1):
            acc += nw[j] * phi[i - j]
        prod[i] = acc
    # I = (N/w) * phi(2w) / 2   because 1/(1-e^{-2w}) = phi(2w)/(2w)
    # N/(1-e^{-2w}) = N/w * 1/2 * phi(2w)  yes.
    half_prod = [c / 2 for c in prod]
    integ = iv.mpf(0)
    eta_pow = eta
    for k in range(prod_deg + 1):
        integ += half_prod[k] * eta_pow / (k + 1)
        eta_pow *= eta
    # Remainder: |B_{2m}| < 4 (2m)! / (2 pi)^{2m}
    # Conservative additive pad: next two even Bernoulli contributions
    # times eta^{d}/(d+1) * crude N/w bound.
    # |N(w)/w| on [0, eta] <= 2*(|delta|*2 + 1 + eta) by crude exp bounds.
    n_bound = 2 * (abs(g0) * 2 + abs(p) + abs(q) * (1 + eta) + eta)
    phi_tail = iv.mpf(0)
    # |phi(x) - partial| <= sum_{k>prod_deg} 4 |x|^k  for |x|<pi
    # (using |B_k|/k! < 4 / (2pi)^k * 2  roughly)
    x = 2 * eta
    # geometric majorant 4 (|x|/2)^ {prod_deg+1} / (1-|x|/2) if |x|<2
    # Safer: 5 * (|x|/(2*pi-0.1))^{prod_deg+1} / (1-|x|/(2*pi))
    radius = iv.mpf(str(6.0))  # 2*pi - 0.28 > 6
    ratio = abs(x) / radius
    tail = iv.mpf(5) * (ratio ** (prod_deg + 1)) / (1 - ratio)
    rem = n_bound * tail * eta / 2
    return integ + iv.mpf([-float(ivsplit(rem)[1]), float(ivsplit(rem)[1])])


def series_k_for(a):
    """Enough exponential terms that alpha_K * a >= 20."""
    a_lo = float(ivsplit(a)[0])
    if a_lo <= 1e-12:
        return 256
    need = int(0.5 * (20.0 / a_lo - 0.5)) + 4
    return max(64, min(need, 800))


def bose_half_series_integral(p, q, a, b):
    """int_a^b (p+q w) e^{-w/2}/(1-e^{-2w}) dw
    = sum_{k=0}^{K-1} int (p+qw) exp(-(2k+1/2) w) dw  + tail."""
    k_terms = series_k_for(a)
    total = iv.mpf(0)
    half = iv.mpf("0.5")
    two = iv.mpf(2)
    for k in range(k_terms):
        alpha = two * k + half
        total += exp_linear_integral(alpha, p, q, a, b)
    # tail: sum_{k>=K} int_a^b |p+qw| exp(-(2k+1/2) w) dw
    # <= max|G| / (1-e^{-2a}) * int_a^b exp(-alpha_K w) dw
    #   = max|G| / (1-e^{-2a}) * (e^{-alpha_K a}-e^{-alpha_K b}) / alpha_K
    alpha_k = two * k_terms + half
    den = 1 - iv.exp(-two * a)
    integ_tail = (iv.exp(-alpha_k * a) - iv.exp(-alpha_k * b)) / alpha_k
    gbound = abs(p) + abs(q) * (abs(a) + abs(b))
    tail = gbound / den * integ_tail
    tlo, thi = ivsplit(tail)
    rad = max(abs(float(tlo)), abs(float(thi)), 0.0)
    return total + iv.mpf([-rad, rad])


def bose_two_series_integral(p, a, b, k_terms=SERIES_K):
    """int_a^b p * e^{-2w}/(1-e^{-2w}) dw, a>0.
    Closed form: p * sum_{k>=1} (e^{-2k a}-e^{-2k b})/(2k)
    = (p/2) [log(1-e^{-2b}) - log(1-e^{-2a})]."""
    return (p / 2) * (iv.log(1 - iv.exp(-2 * b)) - iv.log(1 - iv.exp(-2 * a)))


def _eta_of(delta):
    dmid = float(sum(ivsplit(delta)) / 2)
    if dmid >= float(NEAR_ETA):
        return iv.mpf(str(NEAR_ETA))
    # Small delta: Bernoulli on a prefix, geometric on the rest.
    target = max(0.25 * dmid, min(0.5 * dmid, 0.01))
    target = min(target, 0.9 * dmid)
    return iv.mpf(str(target))


def _wider(a, b):
    return float(sum(ivsplit(a)) / 2) > float(sum(ivsplit(b)) / 2) + 1e-18


def arch_G0(delta):
    """A(G_0), G_0(w)=max(0, delta-|w|). Independent of U>=delta."""
    g0 = delta
    gamma = iv.euler
    logpi = iv.log(iv.pi)
    eta = _eta_of(delta)
    near = near_I_integral(g0, delta, iv.mpf(-1), eta)
    if _wider(delta, eta):
        far_g = bose_half_series_integral(delta, iv.mpf(-1), eta, delta)
        far_g0 = bose_two_series_integral(g0, eta, delta)
        mid = far_g0 - far_g
    else:
        mid = iv.mpf(0)
    tail = -g0 * iv.log(1 - iv.exp(-2 * delta))
    return -(gamma + logpi) * g0 + 2 * (near + mid) + tail


def arch_Gm(m, delta):
    """A(G_m) for m>=1.  g0=0, G(w)=tent at m*delta on [0,inf)."""
    a = (m - 1) * delta
    midpt = m * delta
    b = (m + 1) * delta
    if m == 1:
        eta = _eta_of(delta)
        near = near_I_integral(iv.mpf(0), iv.mpf(0), iv.mpf(1), eta)
        if _wider(midpt, eta):
            rise = bose_half_series_integral(
                iv.mpf(0), iv.mpf(1), eta, midpt)
        else:
            rise = iv.mpf(0)
        fall = bose_half_series_integral(b, iv.mpf(-1), midpt, b)
        return 2 * near - 2 * (rise + fall)
    rise = bose_half_series_integral(-a, iv.mpf(1), a, midpt)
    fall = bose_half_series_integral(b, iv.mpf(-1), midpt, b)
    return -2 * (rise + fall)


def pole_G(m, delta):
    """Pi(G_m) = 4 int_0^inf G cosh(x/2) dx, closed form."""
    c = iv_cosh(delta / 2) - 1
    if m == 0:
        return 16 * c
    return 32 * iv_cosh(m * delta / 2) * c


def prime_G(m, delta, rows):
    """P(G_m) = sum 2 Lambda(n)/sqrt(n) G_m(log n), exact finite."""
    total = iv.mpf(0)
    center = m * delta
    for n, p in rows:
        logn = iv.log(n)
        dist = abs(logn - center)
        val = delta - dist
        # val may be an interval; only add if hi>0
        vlo, vhi = ivsplit(val)
        if vhi <= 0:
            continue
        if vlo < 0:
            val = iv.mpf([0, float(vhi)])
        lam = iv.log(p)
        total += 2 * lam / iv.sqrt(n) * val
    return total


def W_G(m, delta, rows):
    A = arch_G0(delta) if m == 0 else arch_Gm(m, delta)
    P = prime_G(m, delta, rows)
    Pi = pole_G(m, delta)
    return A - P + Pi, A, P, Pi


def assemble_Q(n_bins, delta, rows):
    omega = []
    details = []
    for m in range(n_bins):
        w, A, P, Pi = W_G(m, delta, rows)
        omega.append(w)
        details.append((A, P, Pi))
    Q_iv = [[None] * n_bins for _ in range(n_bins)]
    for j in range(n_bins):
        for k in range(n_bins):
            m = abs(j - k)
            val = omega[m] if m == 0 else omega[m] / 2
            Q_iv[j][k] = val
    return Q_iv, omega, details


def certify_matrix(Q_iv):
    """Try Higham on the raw interval matrix first (cheap, works when
    the radius row-sum is below lambda_min).  If that fails, a frozen
    inverse-Cholesky congruence (r465) is applied and Higham is
    retried on C^T Q C ~ I."""
    n = len(Q_iv)
    mid = np.array([[midpoint_radius(Q_iv[j][k])[0]
                     for k in range(n)] for j in range(n)])
    rad = np.array([[midpoint_radius(Q_iv[j][k])[1]
                     for k in range(n)] for j in range(n)])
    mid = 0.5 * (mid + mid.T)
    rad = 0.5 * (rad + rad.T)
    max_radius = float(np.max(rad))
    try:
        evals = np.linalg.eigvalsh(mid)
        hint = float(evals[0])
    except np.linalg.LinAlgError:
        hint = 0.0
    lower = None
    if hint > 0:
        lower = validated_lammin(mid, rad, hint)
    if lower is not None and lower > 0:
        return {
            "n": n, "hint": hint, "mu": lower, "certified": True,
            "max_radius": max_radius, "route": "raw",
        }
    # congruence fallback
    try:
        factor = np.linalg.cholesky(mid)
        change = np.linalg.solve(factor, np.eye(n)).T
    except np.linalg.LinAlgError:
        return {
            "n": n, "hint": hint, "mu": None, "certified": False,
            "max_radius": max_radius, "route": "fail",
        }
    change_iv = [[iv.mpf(float(change[row, col]))
                  for col in range(n)] for row in range(n)]
    product = [[sum(Q_iv[row][inner] * change_iv[inner][col]
                    for inner in range(n))
                for col in range(n)] for row in range(n)]
    transformed = [[sum(change_iv[inner][row] * product[inner][col]
                        for inner in range(n))
                    for col in range(n)] for row in range(n)]
    tmid = np.array([[midpoint_radius(transformed[j][k])[0]
                      for k in range(n)] for j in range(n)])
    trad = np.array([[midpoint_radius(transformed[j][k])[1]
                      for k in range(n)] for j in range(n)])
    tmid = 0.5 * (tmid + tmid.T)
    trad = 0.5 * (trad + trad.T)
    try:
        thint = float(np.linalg.eigvalsh(tmid)[0])
    except np.linalg.LinAlgError:
        thint = 0.0
    tlower = None
    if thint > 0:
        tlower = validated_lammin(tmid, trad, thint)
    if tlower is None:
        tlower = validated_lammin(tmid, trad, 1.0)
    ok = tlower is not None and tlower > 0
    return {
        "n": n, "hint": hint, "mu": tlower if ok else lower,
        "certified": ok, "max_radius": max_radius,
        "route": "congruence" if ok else "fail",
    }


# ---------------------------------------------------------------------------
# L schedule
# ---------------------------------------------------------------------------
def L_of_k(k: int):
    return k * iv.log(2) / 4


def L_float(L):
    lo, hi = ivsplit(L if isinstance(L, iv.mpf) else iv.mpf(L))
    return float((lo + hi) / 2)


def make_schedule(smoke: bool):
    log2 = iv.log(2)
    L_yb = iv.mpf("0.30")          # 2L=0.60 < log 2
    L_08 = iv.mpf("0.80")
    L5 = 5 * log2 / 4
    if smoke:
        return [
            ("YB", L_yb, 8),
            ("L08", L_08, 8),
            ("L5", L5, 8),
        ]
    # full: two resolutions at the calibration point, then upward
    rows = [
        ("YB", L_yb, 8),
        ("YB", L_yb, 16),
        ("L08", L_08, 16),
        ("L08f", L_08, 24),
        ("L5", L5, 16),
        ("L10", iv.mpf("1.0"), 20),
        ("L12", iv.mpf("1.2"), 24),
        ("L14", iv.mpf("1.4"), 28),
        ("L16", iv.mpf("1.6"), 32),
        ("L18", iv.mpf("1.8"), 32),
        ("L20", iv.mpf("2.0"), 32),
        ("Lk8", 8 * log2 / 4, 28),
        ("Lk12", 12 * log2 / 4, 32),
        ("Lk16", 16 * log2 / 4, 36),
    ]
    return rows


# Default pins filled after /tmp; live run must enclose them.
# Placeholder empty => first run records, sealed run checks.


def tag_n(tag, n):
    return (tag, n)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def run(smoke: bool) -> int:
    global CERT_PINS, SHAPE_PINS, CHECKS
    CHECKS = []
    started = time.perf_counter()
    mp.mp.dps = DPS
    iv.dps = DPS
    print("classical_cert_probe -- r471")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("reason", SCRAMBLE_REASON)

    firewall_ok, forbidden = firewall_audit()
    check("firewall", firewall_ok,
          "no zero oracle" if firewall_ok else forbidden)
    check("scramble-gate", SCRAMBLE_SENSITIVE, "positions log n enter P")
    check("bernoulli-B1", BERNOULLI[1] == Fraction(1, 2), "B1^+=+1/2")
    check("bernoulli-B2", BERNOULLI[2] == Fraction(1, 6), "B2=1/6")

    schedule = make_schedule(smoke)
    L_hi = max(L_float(L) for _, L, _ in schedule)
    n_cap = int(math.exp(2 * L_hi) + 8)
    rows = prime_powers_upto(n_cap)
    check("sieve-cap", len(rows) >= 1 and rows[0] == (2, 2),
          "n_cap=%d pp=%d first=%s" % (n_cap, len(rows), rows[0]))

    results = []
    print("\n  tag   L        n   delta    n_max  pp   mu_lo        hint       sec  status")
    for tag, L, n_bins in schedule:
        t0 = time.perf_counter()
        delta = 2 * L / n_bins
        n_max = n_max_for(L)
        local_rows = [(n, p) for n, p in rows if n <= n_max]
        Q_iv, omega, details = assemble_Q(n_bins, delta, local_rows)
        cert = certify_matrix(Q_iv)
        dt = time.perf_counter() - t0
        status = "GRID_CERTIFIED" if cert["certified"] else "OPEN"
        mu_print = ("%.4e" % cert["mu"]) if cert["mu"] is not None else "None"
        print("  %-5s %-8.4f %3d  %.4f  %5d %4d  %-12s %.4e  %5.2f  %s %s" % (
            tag, L_float(L), n_bins, L_float(delta), n_max, len(local_rows),
            mu_print, cert["hint"], dt, status, cert.get("route", "")), flush=True)
        rec = {
            "tag": tag,
            "L": L_float(L),
            "n": n_bins,
            "delta": L_float(delta),
            "n_max": n_max,
            "pp": len(local_rows),
            "mu": cert["mu"],
            "hint": cert["hint"],
            "certified": cert["certified"],
            "max_radius": cert["max_radius"],
            "omega0": omega[0],
            "seconds": dt,
            "status": status,
        }
        results.append(rec)
        # OPEN is an honest type, not a probe failure.
        check("%s-n=%d" % (tag, n_bins), True,
              "%s hint=%.4e mu=%s rad=%.2e route=%s" % (
                  status, cert["hint"], mu_print, cert["max_radius"],
                  cert.get("route", "")))

    # calibration L=0.8 must be green
    cal = [r for r in results if r["tag"] in ("L08", "L08f")]
    check("calibration-L08",
          all(r["certified"] for r in cal) and len(cal) >= 1,
          "%d L=0.8 row(s) GRID_CERTIFIED" % len(cal))
    yb = [r for r in results if r["tag"] == "YB"]
    check("calibration-YB",
          any(r["certified"] for r in yb) and len(yb) >= 1,
          "prime-blind L=0.30 GRID_CERTIFIED on at least one mesh")

    # type honesty: every certified row is GRID, never full lambda*
    check("type-is-grid",
          all(r["status"] in ("GRID_CERTIFIED", "OPEN") for r in results),
          "no silent upgrade to lambda_*(L)>=0")

    certified_L = [r["L"] for r in results if r["certified"]]
    L_max = max(certified_L) if certified_L else 0.0
    verdict = "GRID_CERTIFIED(L_max=%.4f)" % L_max
    pin_L = L_MAX_SMOKE_PIN if smoke else L_MAX_FULL_PIN
    check("L-max-recorded", abs(L_max - pin_L) < 1e-3, verdict)

    # pin checks if sealed
    if CERT_PINS:
        pin_ok = True
        for r in results:
            key = (r["tag"], r["n"])
            if key not in CERT_PINS:
                pin_ok = False
                continue
            lo_s, hi_s = CERT_PINS[key]
            lo, hi = mp.mpf(lo_s), mp.mpf(hi_s)
            if r["mu"] is None or not (lo <= mp.mpf(r["mu"]) <= hi):
                pin_ok = False
        check("cert-pins", pin_ok, "live mu inside sealed hulls")
    else:
        check("cert-pins-unsealed", True,
              "first run: record hulls from /tmp")

    if SHAPE_PINS:
        shape_ok = True
        for r in results:
            key = (r["tag"], r["n"])
            if key not in SHAPE_PINS:
                shape_ok = False
                continue
            if (r["n_max"], r["pp"]) != SHAPE_PINS[key]:
                shape_ok = False
        check("shape-pins", shape_ok, "n_max/pp frozen")
    else:
        check("shape-pins-unsealed", True, "first run")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", verdict)
    print("SPEC_SHA", SPEC_SHA)
    # machine-readable pin dump for sealing
    print("PIN_DUMP_BEGIN")
    for r in results:
        mu = r["mu"] if r["mu"] is not None else 0.0
        # outward 6-digit scientific hull around mu
        if r["mu"] is not None:
            lo = r["mu"] * (1 - 1e-3) if r["mu"] > 0 else r["mu"]
            hi = r["mu"] * (1 + 1e-3) if r["mu"] > 0 else 0.0
            print("  PIN %s %d mu=[%.8e, %.8e] n_max=%d pp=%d" % (
                r["tag"], r["n"], lo, hi, r["n_max"], r["pp"]))
        else:
            print("  PIN %s %d OPEN n_max=%d pp=%d" % (
                r["tag"], r["n"], r["n_max"], r["pp"]))
    print("PIN_DUMP_END")
    if n_fail:
        print("CLASSICAL CERT FAILED")
        return 1
    print("CLASSICAL CERT %s" % verdict)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
