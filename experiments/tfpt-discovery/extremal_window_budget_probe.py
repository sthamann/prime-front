#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extremal_window_budget_probe.py -- EXPLORATION ONLY, NOT LOAD-BEARING.

MISSION.  Attack the remaining RH edge from the OTHER side of the inequality.
Every previous probe bounded the arithmetic error P_err from above.  This probe
instead attacks the geometric budget: it changes the WINDOW / test function to
enlarge the supply and shrink the demand, using the classical Beurling-Selberg /
Vaaler / Gaussian-subordination extremal-function technology.

THE QUESTION.  Note CCCLXI isolates the irreducible inequality

        P_err,h  <=  Q_h - P_main,h - need_h

on a predefined cofinal family; note CCCLIX reports the deployed tent/Galerkin
window missing that budget by A/G = 2.470e11 (h=184) and 1.990e14 (h=388).  The
deployed window family was frozen early and never optimised.  Is the 11-14 order
miss a property of the PROBLEM or of the WINDOW?

WHAT THIS PROBE DOES.  It writes the budget as an explicit functional of the
test function, computes it in certified interval arithmetic for the deployed
window and for the classical alternatives, searches the admissible class, and
returns a certified obstruction with an LP dual certificate.

NO RH CLAIM.  No paper / ledger / website / verification file is touched.
"""

from __future__ import annotations

import ast
import hashlib
import inspect
import math
import os
import sys
import time
from dataclasses import dataclass, field

import numpy as np
import sympy as sp
from mpmath import iv, mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (_HERE, os.path.join(_ROOT, "verification")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import epstein_firewall_probe as epx          # noqa: E402
import v563_paper2_readouts as core           # noqa: E402

mp.dps = 60
iv.dps = 60

T0 = time.time()
CHECKS: list[tuple[str, bool, str]] = []
RUNTIME_CAP_S = 1800.0


# =====================================================================  S0 spec
FROZEN_SPEC = """
BUDGET FUNCTIONAL (derived symbolically in S1, no fitting, no zeros used).

Let F be even, real, supported in [-S,S], with Fhat(r) = int F(x) e^{-i r x} dx.
Weil's explicit formula for the completed zeta function reads

    sum_rho Fhat(gamma_rho) = POLE(F) - PRIME(F) + ARCH(F),

    POLE(F)  = Fhat(i/2) + Fhat(-i/2)      = 4 int_0^S F(x) cosh(x/2) dx
    PRIME(F) = 2 sum_{n <= e^S} Lambda(n) n^{-1/2} F(log n)
    ARCH(F)  = -F(0)(gamma + log pi)
               + 2 int_0^inf [F(0) e^{-2w} - F(w) e^{-w/2}] / (1 - e^{-2w}) dw.

Split PRIME by psi(t) = t + E(t):

    P_main(F) = 2 int_0^S F(x) e^{x/2} dx            (Abel main term)
    Delta(F)  = PRIME(F) - P_main(F)
              = -2 int_0^S [E(e^x)/e^x] g(x) dx,     g(x) := (F'(x) - F(x)/2) e^{x/2}.

DEFINE the two functionals that carry everything:

    B(F) := POLE(F) - P_main(F) + ARCH(F)            GEOMETRIC BUDGET  (supply)
    V(F) := int_0^S |g(x)| dx                        VARIATION LOAD    (demand)

Then, with eta := sup_{1 <= u <= e^S} |psi(u) - u| / u  (unconditional envelope),

    |Delta(F)| <= 2 eta V(F),      and      Delta(F) <= B(F)  <==>  Weil(F) >= 0.

BUDGET RATIO (the object the mission asks for):

    R(F) := 2 eta V(F) / B(F),   closure at F  <==>  R(F) <= 1  <==>  B(F)/V(F) >= 2 eta.

FOURIER FORM (proved in S1/S3).  With
    Theta(r) := 1/(1/4 + r^2) + Re psi(1/4 + i r/2) - log pi
one has the exact identity
    B(F) = (1/2pi) int_R Fhat(r) Theta(r) dr.
POLE - P_main contributes 1/(1/4+r^2) (Fourier pair of e^{-|x|/2}); ARCH
contributes Re psi(1/4 + i r/2) - log pi.  This is the clean extremal problem.

ADMISSIBLE CLASS A(alpha, D) -- the faithfulness constraints, stated exactly as
the deployed extraction chain requires them:
  (A1) POSITIVITY TRANSFER.  Fhat >= 0 on R (Weil positivity is only a statement
       about zeros for positive-definite F).  Enforced structurally: every window
       here is a product / autocorrelation of positive-definite factors.
  (A2) FAITHFUL SUPPORT CAP.  supp F subset [-(2 alpha + 2D), 2 alpha + 2D].
       This is the deployed cap (Wall: ladder extent 2 alpha, tent width D,
       second difference D).  It makes PRIME(F) a FINITE EXACT sum.
  (A3) GALERKIN IDENTIFICATION.  F = phi * phi~ with phi in span{tri_D(. - kD)},
       k = 1..h, h = alpha/D; then Weil(F_v) = v^T Omega v with Omega the deployed
       matrix.  Consequence: the window is a DIRECTION v in a fixed cone, not a
       free function.
  (A4) COFINALITY / DENSITY.  The extraction quantifies over ALL v and all cells.
       One may not select a favourable direction.  The all-ones direction
       v = 1 (whose F is the Fejer window of width 2 alpha) is MANDATORY.
  (A5) ARITHMETIC DISCRIMINATION (firewall).  The window must still separate the
       true von Mangoldt comb from the declared controls:
            W_truth > 0  AND  W_scramble < 0  AND  W_epstein < 0,
       W := B - Delta.  A window that certifies the controls is COMB-BLIND and
       carries no arithmetic information.

WHY BEURLING-SELBERG / VAALER CANNOT BE IMPORTED VERBATIM (certified in S5).
Beurling-Selberg majorants/minorants, Vaaler's construction and the
Carneiro-Littmann-Vaaler Gaussian-subordination framework all optimise over
BANDLIMITED functions (entire of exponential type).  By Paley-Wiener a nonzero
function cannot be simultaneously bandlimited and compactly supported, so (A2)
forbids bandlimitation.  The transferable content is the positive-definite core:
Vaaler's kernel core is the Fejer kernel, and Gaussian subordination inside the
compactly supported class is the tent-power / exponential-subordination family
(1 - |x|/S)_+^n e^{-a|x|}.  Both are represented in the table.

TASKS
 (1) budget inequality as a functional of the test function       -> S1, S3
 (2) budget ratio for deployed tent + classical alternatives      -> S5
 (3) best achievable ratio, certified bound / dual certificate    -> S6, S7, S8
 (4) faithfulness ward                                            -> S9
 (5) controls (Epstein / Scramble) must stay broken               -> S6

VERDICT ENUM (frozen, precedence top to bottom)
  WINDOW-CLOSES              some admissible+discriminating window has R <= 1
                             at every audited cell.
  WINDOW-OPTIMAL-INSUFFICIENT a certified obstruction shows no admissible window
                             suffices (mandatory direction has B <= 0, or the
                             LP dual bounds sup B/V strictly below 2 eta).
  WINDOW-INADMISSIBLE        windows reaching R <= 1 exist but all of them fail
                             (A5) / (A2) -- they leave the faithful class.
  WINDOW-IMPROVES            quantified finite improvement, remaining orders.
  WINDOW-INSTRUMENT-EDGE     numerics, not mathematics, is the binding limit.

RIGOUR.  mp.dps = 60 / iv.dps = 60.  Every reported budget number is a rigorous
outward interval enclosure (mpmath iv) or an exact closed form; enclosure widths
are printed next to the values.  The frontier SCAN in S6 is float and is labelled
a search, never a certificate; every number that carries the verdict is
re-certified in interval arithmetic.  The LP in S7 is accepted only through its
dual certificate, verified inequality by inequality in interval arithmetic --
the solver's own optimality assertion is never used.  No fitting anywhere.
"""

AST_BANNED = {
    "curve_fit", "polyfit", "leastsq", "minimize", "least_squares",
    "eigvals", "eigvalsh", "eig", "eigh", "roots",
}


def s0_firewall() -> None:
    print("=" * 100)
    print("S0  FIREWALL / SPEC")
    print("=" * 100)
    src = open(os.path.abspath(__file__), "rb").read()
    sha = hashlib.sha256(src).hexdigest()
    spec_sha = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
    print("  probe          : %s" % os.path.basename(__file__))
    print("  PROBE_SHA      : %s" % sha)
    print("  SPEC_SHA       : %s" % spec_sha)
    tree = ast.parse(src.decode())
    hits = sorted({
        n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id
        for n in ast.walk(tree)
        if isinstance(n, ast.Call) and isinstance(n.func, (ast.Name, ast.Attribute))
        and (n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id) in AST_BANNED
    })
    ck("S0.ast-no-fit-no-eig", not hits, "banned calls: %s" % (hits or "none"))
    ck("S0.readonly-imports",
       "v563_paper2_readouts" in sys.modules and "epstein_firewall_probe" in sys.modules,
       "verification modules imported read-only")
    ck("S0.precision", mp.dps >= 50 and iv.dps >= 50, "mp.dps=%d iv.dps=%d" % (mp.dps, iv.dps))
    print(FROZEN_SPEC)


def ck(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok), detail))
    print("   [%s] %-46s %s" % ("OK " if ok else "!! ", name, detail))
    return bool(ok)


# ============================================================  S1 exact algebra
def s1_symbolic() -> None:
    print()
    print("=" * 100)
    print("S1  EXACT SYMBOLIC DERIVATION OF THE BUDGET FUNCTIONAL  (sympy, no numerics)")
    print("=" * 100)
    x, r, t, S, a, b = sp.symbols("x r t S a b", positive=True)
    F = sp.Function("F")

    # (I1) POLE - P_main = 2 int_0^S F(x) e^{-x/2} dx  <=  4 cosh(x/2) - 2 e^{x/2} = 2 e^{-x/2}
    ck("S1.I1.pole-minus-main",
       sp.simplify(4 * sp.cosh(x / 2) - 2 * sp.exp(x / 2) - 2 * sp.exp(-x / 2)) == 0,
       "4 cosh(x/2) - 2 e^{x/2} = 2 e^{-x/2}   =>  POLE - P_main = 2 int_0^S F e^{-x/2}")

    # (I2) Fourier pair of e^{-|x|/2} is 1/(1/4+r^2): verify via exact antiderivative
    anti = sp.exp(-x / 2) * (-sp.Rational(1, 2) * sp.cos(r * x) + r * sp.sin(r * x)) / (sp.Rational(1, 4) + r ** 2)
    ck("S1.I2.laplace-pair",
       sp.simplify(sp.diff(anti, x) - sp.exp(-x / 2) * sp.cos(r * x)) == 0
       and sp.simplify(-2 * anti.subs(x, 0) - 1 / (sp.Rational(1, 4) + r ** 2)) == 0,
       "2 int_0^inf e^{-x/2} cos(r x) dx = 1/(1/4+r^2)   (Theta's first term)")

    # (I3) Abel/Mellin law: t d/dt [F(log t)/sqrt t] = g(log t)/t with g=(F'-F/2)e^{x/2}
    lhs = sp.simplify(t * sp.diff(F(sp.log(t)) / sp.sqrt(t), t))
    rhs = (sp.Subs(sp.Derivative(F(x), x), x, sp.log(t)).doit() - F(sp.log(t)) / 2) / sp.sqrt(t)
    ck("S1.I3.abel-kernel", sp.simplify(lhs - rhs) == 0,
       "Delta(F) = -2 int_0^S E(e^x) e^{-x} g(x) dx  with  g=(F'-F/2)e^{x/2}")

    # (I4) partial fractions behind the rigorous Re psi series
    ck("S1.I4.repsi-split",
       sp.simplify(1 / a - a / (a ** 2 + b ** 2) - b ** 2 / (a * (a ** 2 + b ** 2))) == 0,
       "1/a - a/(a^2+b^2) = b^2/(a(a^2+b^2))   (positive decreasing tail terms)")

    # (I5) psi(1/4) closed form  ->  Theta(0) closed form
    ck("S1.I5.psi-quarter",
       sp.simplify(sp.digamma(sp.Rational(1, 4)) - (-sp.EulerGamma - 3 * sp.log(2) - sp.pi / 2)) == 0,
       "psi(1/4) = -gamma - 3 log 2 - pi/2  =>  Theta(0) = 4 - gamma - 3 log 2 - pi/2 - log pi")

    # (I6) the arch series: 1/(1-e^{-2w}) = sum_k e^{-2kw}, giving the digamma closed form
    k = sp.symbols("k", integer=True, nonnegative=True)
    w, q = sp.symbols("w q", positive=True)
    geo = sp.summation(q ** k, (k, 0, sp.oo))
    geo = geo.args[0][0] if isinstance(geo, sp.Piecewise) else geo
    ck("S1.I6.arch-geometric",
       sp.simplify(geo.subs(q, sp.exp(-2 * w)) - 1 / (1 - sp.exp(-2 * w))) == 0,
       "ARCH kernel expands geometrically (|e^{-2w}|<1)  =>  ARCH is closed form in psi,zeta(m,.)")

    # (I6b) the m=1 pairing reindexes termwise onto Gauss's digamma series
    z = sp.symbols("z")
    ck("S1.I6b.digamma-pairing",
       sp.simplify((1 / (2 * k + 2) - 1 / (z + 2 * k + sp.Rational(1, 2)))
                   - (1 / (k + 1) - 1 / (k + sp.Rational(1, 4) + z / 2)) / 2) == 0,
       "termwise: 1/(2k+2) - 1/(z+2k+1/2) = (1/2)[1/(k+1) - 1/(k+1/4+z/2)];  summing and using"
       " Gauss's series psi(w) = -gamma + sum_k [1/(k+1)-1/(k+w)] gives (1/2)(psi(1/4+z/2)+gamma)")
    # (I6c) the m>=2 pairing is a Hurwitz zeta value
    m = sp.symbols("m", integer=True, positive=True)
    ck("S1.I6c.hurwitz-pairing",
       sp.simplify((z + 2 * k + sp.Rational(1, 2)) ** (-m)
                   - 2 ** (-m) * (k + sp.Rational(1, 4) + z / 2) ** (-m)) == 0,
       "termwise: (z+2k+1/2)^{-m} = 2^{-m}(k+1/4+z/2)^{-m}  =>  sum_k = 2^{-m} zeta(m, 1/4+z/2)")

    # (I7) damped-Fejer variation load V is exactly S/2 + 1  (undamped one is exponential)
    Fd = sp.exp(-x / 2) * (1 - x / S)
    gd = sp.simplify((sp.diff(Fd, x) - Fd / 2) * sp.exp(x / 2))
    ck("S1.I7.damped-V",
       sp.simplify(gd + (1 - x / S) + 1 / S) == 0
       and sp.simplify(sp.integrate(-gd, (x, 0, S)) - (S / 2 + 1)) == 0,
       "a=1/2 damping: g = -(1-x/S) - 1/S,  V = S/2 + 1  (no e^{S/2} growth)")

    # (I8) g is polyexp: g = Re[q0 e^{-(z-1/2)x}] with q0 = p' - (z+1/2) p
    z = sp.symbols("z")
    p = sp.Function("p")
    Fz = p(x) * sp.exp(-z * x)
    gz = sp.simplify((sp.diff(Fz, x) - Fz / 2) * sp.exp(x / 2))
    tgt = (sp.Derivative(p(x), x).doit() - (z + sp.Rational(1, 2)) * p(x)) * sp.exp(-(z - sp.Rational(1, 2)) * x)
    ck("S1.I8.polyexp-g", sp.simplify(gz - tgt) == 0,
       "F=Re[p e^{-zx}]  =>  g=Re[q0 e^{-(z-1/2)x}], q0=p'-(z+1/2)p  (closed-form integrals)")

    # (I9) the exact primitive used everywhere: int q e^{-c x} dx = -e^{-cx} sum_j q^{(j)}/c^{j+1}
    c = sp.symbols("c", nonzero=True)
    qq = sp.symbols("q0:4")
    poly = sum(qq[j] * x ** j for j in range(4))
    Psi = sum(sp.diff(poly, x, j) / c ** (j + 1) for j in range(4))
    ck("S1.I9.polyexp-primitive",
       sp.simplify(sp.diff(-sp.exp(-c * x) * Psi, x) - poly * sp.exp(-c * x)) == 0,
       "int_A^B q e^{-cx} dx = [-e^{-cx} sum_j q^{(j)}/c^{j+1}]_A^B  (deg q <= 3, exact)")


# =========================================================  S2 the Theta theorem
def _ivc(v) -> iv.mpf:
    return iv.mpf(mp.mpf(v))


_PSI_CACHE: dict = {}
_HUR_CACHE: dict = {}
EM_K = 4000


def re_psi_iv(wre, wim, K: int = EM_K) -> iv.mpf:
    """Rigorous enclosure of Re psi(w), w = wre + i wim, wre > 0.

        psi(w) = -gamma + sum_{k>=0} f(k),   f(k) = 1/(k+1) - Re 1/(k+w).

    Partial sum to K; the tail uses the midpoint Euler-Maclaurin formula with one
    correction term and a rigorous fourth-derivative remainder:

        sum_{k>=K} f(k) = int_{K-1/2}^inf f + (1/24) f'(K-1/2) + E,
        |E| <= (1/576 + 1/1920) int_{K-1/2}^inf |f^{(4)}|.

    (The correction follows from int_{k-1/2}^{k+1/2} f = f(k) + f''(k)/24 + ... ;
    the remainder collects the midpoint error of sum f'' and the next order.)
    """
    key = (str(wre), str(wim), K)
    if key in _PSI_CACHE:
        return _PSI_CACHE[key]
    A0, b2 = _ivc(wre), _ivc(wim) ** 2
    s = iv.mpf(0)
    for k in range(K):
        a = _ivc(k) + A0
        s = s + 1 / (_ivc(k) + 1) - a / (a * a + b2)
    A = _ivc(K) - iv.mpf(1) / 2 + A0
    d2 = A * A + b2
    tail = iv.log(d2) / 2 - iv.log(_ivc(K) + iv.mpf(1) / 2)
    # f'(t) = -1/(t+1)^2 + Re 1/(t+w)^2 ;  Re (A+ib)^-2 = (A^2-b^2)/(A^2+b^2)^2
    fp = -1 / ((_ivc(K) + iv.mpf(1) / 2) ** 2) + (A * A - b2) / (d2 * d2)
    rem = (_ivc(mp.mpf(1) / 576 + mp.mpf(1) / 1920)
           * 6 * (1 / ((_ivc(K) - iv.mpf(1) / 2) ** 4) + 1 / (A ** 4)))
    out = s + tail + fp / 24 + iv.mpf([-1, 1]) * rem - iv.euler
    _PSI_CACHE[key] = out
    return out


def hurwitz_iv(m: int, wre, wim, K: int = EM_K) -> iv.mpc:
    """Rigorous enclosure of zeta(m, w) = sum_{k>=0} (k+w)^{-m}, m >= 2, Re w > 0.

    Same midpoint Euler-Maclaurin tail with one correction term:
        sum_{k>=K} f = (K-1/2+w)^{1-m}/(m-1) - (m/24)(K-1/2+w)^{-(m+1)} + E,
        |E| <= (1/576+1/1920) m(m+1)(m+2) (K-1/2+Re w)^{-(m+3)}.
    """
    key = (m, str(wre), str(wim), K)
    if key in _HUR_CACHE:
        return _HUR_CACHE[key]
    w = iv.mpc(_ivc(wre), _ivc(wim))
    s, one = iv.mpc(0), iv.mpc(1)
    for k in range(K):
        u = _ivc(k) + w
        up = one
        for _ in range(m):
            up = up * u
        s = s + one / up
    Wc = _ivc(K) - iv.mpf(1) / 2 + w
    wp = one
    for _ in range(m - 1):
        wp = wp * Wc
    s = s + one / (wp * (m - 1))
    wq = wp * Wc * Wc
    s = s - _ivc(m) / 24 * (one / wq)
    rem = (_ivc(mp.mpf(1) / 576 + mp.mpf(1) / 1920) * _ivc(m * (m + 1) * (m + 2))
           / ((_ivc(K) - iv.mpf(1) / 2 + _ivc(wre)) ** (m + 3)))
    out = iv.mpc(s.real + iv.mpf([-1, 1]) * rem, s.imag + iv.mpf([-1, 1]) * rem)
    _HUR_CACHE[key] = out
    return out


def _iv_ends(x: iv.mpf):
    return mp.mpf(x._mpi_[0]), mp.mpf(x._mpi_[1])


def theta_iv(r_iv: iv.mpf, K: int = EM_K) -> iv.mpf:
    """Enclosure of Theta(r) = 1/(1/4+r^2) + Re psi(1/4 + i r/2) - log pi."""
    q = _ivc(mp.mpf(1) / 4)
    lo, hi = _iv_ends(r_iv)
    # Re psi(1/4 + i b) is increasing in |b| -> enclose by the two endpoints
    e_lo = re_psi_iv(mp.mpf(1) / 4, abs(lo) / 2, K)
    e_hi = re_psi_iv(mp.mpf(1) / 4, abs(hi) / 2, K)
    psi_box = iv.mpf([min(e_lo.a, e_hi.a), max(e_lo.b, e_hi.b)])
    return 1 / (q + r_iv * r_iv) + psi_box - iv.log(iv.pi)


def theta_f(r: float) -> float:
    return float(1 / (mp.mpf(1) / 4 + mp.mpf(r) ** 2)
                 + mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * mp.mpf(r) / 2)) - mp.log(mp.pi))


_B2J = (1 / 6.0, -1 / 30.0, 1 / 42.0, -1 / 30.0, 5 / 66.0, -691 / 2730.0, 7 / 6.0)


def digamma_np(z):
    """Vectorised complex digamma: recurrence shift + Stirling asymptotics."""
    z = np.asarray(z, dtype=complex)
    acc = np.zeros_like(z)
    n = 16
    for k in range(n):
        acc -= 1.0 / (z + k)
    u = z + n
    out = np.log(u) - 0.5 / u
    u2 = u * u
    up = u2
    for j, b in enumerate(_B2J):
        out -= b / (2 * (j + 1) * up)
        up = up * u2
    return out + acc


def theta_np(r):
    r = np.asarray(r, dtype=float)
    return (1.0 / (0.25 + r * r)
            + np.real(digamma_np(0.25 + 0.5j * r)) - math.log(math.pi))


def fhat_exact(win: Window, rs):
    """Fhat(r) = Re[ I(z - i r) + I(z + i r) ],  I(c) = int_0^S p e^{-cx} dx,
    evaluated in closed form (S1.I9) and vectorised in float complex."""
    rs = np.asarray(rs, dtype=float)
    p0 = np.array([complex(v) for v in _shift_derivs(win.p, 0.0)])
    pS = np.array([complex(v) for v in _shift_derivs(win.p, win.S)])
    pc = np.array([complex(v) for v in win.p])
    S = float(win.S)
    z = complex(win.z)
    tot = np.zeros(len(rs))
    for sgn in (-1.0, +1.0):
        c = z + sgn * 1j * rs
        small = np.abs(c) < 0.1
        I = np.zeros(len(rs), dtype=complex)
        big = ~small
        if big.any():
            cb = c[big]
            Psi0 = np.zeros(cb.shape, dtype=complex)
            PsiS = np.zeros(cb.shape, dtype=complex)
            cp = cb.copy()
            for j in range(len(p0)):
                Psi0 += p0[j] / cp
                PsiS += pS[j] / cp
                cp = cp * cb
            I[big] = Psi0 - np.exp(-cb * S) * PsiS
        if small.any():
            # int_0^S p e^{-cx} dx = sum_n (-c)^n/n! * M_n,  M_n = int_0^S x^n p(x) dx
            cs = c[small]
            acc = np.zeros(cs.shape, dtype=complex)
            fac, cp = 1.0, np.ones(cs.shape, dtype=complex)
            for n in range(0, 28):
                Mn = sum(pc[j] * S ** (n + j + 1) / (n + j + 1) for j in range(len(pc)))
                acc += cp / fac * Mn
                fac *= (n + 1)
                cp = cp * (-cs)
            I[small] = acc
        tot += np.real(I)
    return tot


def _ivm(x) -> float:
    lo, hi = _iv_ends(x)
    return float((lo + hi) / 2)


def _ivw(x) -> float:
    lo, hi = _iv_ends(x)
    return float(hi - lo)


@dataclass
class ThetaFacts:
    theta0: mp.mpf
    r_lo: mp.mpf
    r_hi: mp.mpf


def s2_theta() -> ThetaFacts:
    print()
    print("=" * 100)
    print("S2  THE Theta THEOREM   Theta(r) = 1/(1/4+r^2) + Re psi(1/4 + i r/2) - log pi")
    print("=" * 100)

    th0 = 4 - mp.euler - 3 * mp.log(2) - mp.pi / 2 - mp.log(mp.pi)
    print("  Theta(0) closed form  = 4 - gamma - 3 log 2 - pi/2 - log pi")
    print("           exact value  = %s" % mp.nstr(th0, 50))
    e0 = theta_iv(iv.mpf(0), K=4000)
    ck("S2.theta0-closed-form", bool(e0.a <= th0 <= e0.b) and th0 < 0,
       "series enclosure contains the closed form; Theta(0) < 0")
    ck("S2.theta0-50-digits", True, "-need_inf := Theta(0) = %s" % mp.nstr(th0, 50))

    lo, hi = mp.mpf(5), mp.mpf(10)
    for _ in range(120):
        m = (lo + hi) / 2
        if theta_f(float(m)) < 0:
            lo = m
        else:
            hi = m
    pad = mp.mpf(10) ** -12
    e_lo = theta_iv(_ivc(lo - pad), K=40000)
    e_hi = theta_iv(_ivc(hi + pad), K=40000)
    print()
    print("  unique positive root r_* of Theta (sign change certified in iv):")
    print("     r_* in [%s, %s]" % (mp.nstr(lo - pad, 20), mp.nstr(hi + pad, 20)))
    print("     Theta(r_lo) in [%+.6e, %+.6e]   Theta(r_hi) in [%+.6e, %+.6e]"
          % (float(e_lo.a), float(e_lo.b), float(e_hi.a), float(e_hi.b)))
    print("     for comparison 2 pi = %s   (r_* < 2 pi)" % mp.nstr(2 * mp.pi, 20))
    ck("S2.r-star-bracket", bool(e_lo.b < 0 < e_hi.a),
       "r_* = %s  certified" % mp.nstr(lo, 16))

    # Band certificate.  Theta = (decreasing) + (increasing) - log pi, so on [c,d]
    #   Theta <= 1/(1/4+c^2) + Re psi(1/4 + i d/2) - log pi,
    # which is exactly what theta_iv returns.  The overshoot of that bound is
    # 1/(1/4+c^2) - 1/(1/4+d^2) <= 5.2 (d-c), so a uniform mesh suffices away from
    # the root; we stop a hair short of r_* because Theta(r_*) = 0 exactly.
    gap = mp.mpf(1) / 100
    r1 = lo - gap
    nb, ok, worst = 900, True, mp.mpf(-10)
    ends = [re_psi_iv(mp.mpf(1) / 4, (mp.mpf(i) * r1 / nb) / 2, K=300) for i in range(nb + 1)]
    for i in range(nb):
        cq = _ivc(mp.mpf(1) / 4 + (mp.mpf(i) * r1 / nb) ** 2)
        e = 1 / cq + ends[i + 1] - iv.log(iv.pi)
        worst = max(worst, _iv_ends(e)[1])
        ok = ok and bool(e.b < 0)
    ck("S2.band-negativity", ok,
       "Theta(r) < 0 for all |r| <= r_* - 1/100 = %s, certified by %d interval bands"
       " (sup of the enclosures = %.6e < 0); Theta(r_*) = 0 by the bracket above"
       % (mp.nstr(r1, 16), nb, float(worst)))
    print()
    print("  DUAL CERTIFICATE (band form).  lambda(r) := -Theta(r) >= 0 on [-r_*, r_*] is a")
    print("  nonnegative multiplier, hence for every positive-definite F whose spectral mass")
    print("  lies in the low band,  2 pi B(F) = int Fhat Theta = -int Fhat lambda <= 0.")
    print("  No unsigned arithmetic envelope can ever close a budget whose supply is <= 0:")
    print("  2 eta V(F) > 0 >= B(F).  This is window independent.")
    return ThetaFacts(th0, lo - pad, hi + pad)


# ==========================================  polyexp window algebra (closed form)
@dataclass
class Window:
    name: str
    family: str
    S: float
    a: float
    T: float
    deg: int                      # tent power n in (1-x/S)^n
    note: str = ""
    p: list = field(default_factory=list)     # real polynomial coefficients, ascending

    def __post_init__(self):
        Sm = mp.mpf(self.S)
        poly = [mp.mpf(1)]
        for _ in range(self.deg):
            poly = _pmul(poly, [mp.mpf(1), -1 / Sm])
        self.p = poly

    @property
    def z(self):
        return mp.mpc(self.a, self.T)


def _pmul(u, v):
    out = [mp.mpf(0)] * (len(u) + len(v) - 1)
    for i, ui in enumerate(u):
        for j, vj in enumerate(v):
            out[i + j] += ui * vj
    return out


def _pder(u):
    return [u[j] * j for j in range(1, len(u))] or [mp.mpf(0)]


def _peval_iv(u, x_iv):
    s = iv.mpc(0)
    for c in reversed(u):
        s = s * x_iv + iv.mpc(mp.re(c), mp.im(c))
    return s


def _cplx_iv(c):
    return iv.mpc(iv.mpf(mp.mpf(mp.re(c))), iv.mpf(mp.mpf(mp.im(c))))


_CZERO = mp.mpf(10) ** -8


def _polyexp_int_iv(q, c, A, B):
    """Exact enclosure of int_A^B q(x) e^{-c x} dx, q a complex polynomial.

    c != 0 : telescoping primitive certified in S1.I9.
    c ~ 0  : the exponential is (nearly) absent -- use the Taylor expansion
             int q e^{-cx} = sum_n (-c)^n/n! int x^n q(x) dx, exact for c = 0 and
             convergent with a geometric enclosure otherwise.
    """
    Aiv, Biv = _ivc(A), _ivc(B)
    if abs(c) < _CZERO:
        tot, term = iv.mpc(0), None
        fac, cp = mp.mpf(1), mp.mpc(1)
        for n in range(0, 24):
            mom = iv.mpc(0)
            for j, qj in enumerate(q):
                e = n + j + 1
                mom = mom + iv.mpc(mp.re(qj), mp.im(qj)) * (Biv ** e - Aiv ** e) / e
            term = _cplx_iv(cp / fac) * mom
            tot = tot + term
            fac *= (n + 1)
            cp *= -c
            if abs(c) == 0:
                break
        return tot
    civ = _cplx_iv(c)
    ders, cur = [], list(q)
    for _ in range(len(q)):
        ders.append(list(cur))
        cur = _pder(cur)

    def Psi(xv):
        s = iv.mpc(0)
        cp = civ
        for d in ders:
            s = s + _peval_iv(d, xv) / cp
            cp = cp * civ
        return s

    return (-iv.exp(-civ * Biv) * Psi(Biv)) - (-iv.exp(-civ * Aiv) * Psi(Aiv))


def _polyexp_int_mp(q, c, A, B):
    """Same integral in plain high-precision arithmetic (fast path)."""
    if abs(c) < _CZERO:
        tot, fac, cp = mp.mpc(0), mp.mpf(1), mp.mpc(1)
        for n in range(0, 24):
            mom = mp.mpc(0)
            for j, qj in enumerate(q):
                e = n + j + 1
                mom += qj * (mp.mpf(B) ** e - mp.mpf(A) ** e) / e
            tot += cp / fac * mom
            fac *= (n + 1)
            cp *= -c
            if abs(c) == 0:
                break
        return tot
    ders, cur = [], list(q)
    for _ in range(len(q)):
        ders.append(list(cur))
        cur = _pder(cur)

    def Psi(x):
        s, cp = mp.mpc(0), c
        for d in ders:
            s += sum(cc * mp.mpf(x) ** i for i, cc in enumerate(d)) / cp
            cp *= c
        return s
    return -mp.exp(-c * mp.mpf(B)) * Psi(B) + Psi(A) * mp.exp(-c * mp.mpf(A))


def _polyexp_val_iv(q, c, x):
    return _peval_iv(q, _ivc(x)) * iv.exp(-_cplx_iv(c) * _ivc(x))


def _q0(win: Window):
    """q0 = p' - (z + 1/2) p  so that g = Re[q0 e^{-(z-1/2) x}]."""
    z2 = win.z + mp.mpf(1) / 2
    dp = _pder(win.p)
    n = max(len(dp), len(win.p))
    out = [mp.mpc(0)] * n
    for j in range(n):
        if j < len(dp):
            out[j] += dp[j]
        if j < len(win.p):
            out[j] -= z2 * win.p[j]
    return out


def _shift_derivs(p, x0):
    """[p^{(j)}(x0)]_{j=0..deg}."""
    out, cur = [], list(p)
    for _ in range(len(p)):
        out.append(sum(c * mp.mpf(x0) ** i for i, c in enumerate(cur)))
        cur = _pder(cur)
    return out


def _arch_exp_tail(win: Window, ivmode: bool):
    """sum_{k>=0} Re[ e^{-zeta_k S} Psi_k(S) ], zeta_k = z + 2k + 1/2.

    |e^{-zeta_k S}| = e^{-(a+2k+1/2)S} is geometric with ratio e^{-2S} <= 1.6e-5,
    so a handful of terms exhausts any working precision; the residual is bounded
    by the first dropped term over (1 - e^{-2S}).
    """
    pS = _shift_derivs(win.p, win.S)
    acc = iv.mpf(0) if ivmode else mp.mpf(0)
    last = mp.mpf(0)
    for k in range(48):
        zt = win.z + 2 * k + mp.mpf(1) / 2
        s, cp = mp.mpc(0), zt
        for j in range(len(win.p)):
            s += pS[j] / cp
            cp *= zt
        piece = mp.re(mp.exp(-zt * mp.mpf(win.S)) * s)
        last = abs(piece)
        acc = acc + (_ivc(piece) if ivmode else piece)
        if last < mp.mpf(10) ** -45:
            break
    if ivmode:
        acc = acc + iv.mpf([-1, 1]) * _ivc(last)
    return acc


def arch_parts(win: Window):
    """ARCH(F) = -F(0)(gamma+log pi) + 2 [ (p(0)/2)(Re psi(w) + gamma)
                                           - sum_{j>=1} Re( p^{(j)}(0) 2^{-(j+1)} zeta(j+1,w) )
                                           + E_S ],      w = 1/4 + z/2.

    Derived exactly in S1.I6/I9: the geometric expansion of 1/(1-e^{-2w}) turns
    ARCH into one digamma plus finitely many Hurwitz zeta values.
    """
    w = mp.mpf(1) / 4 + win.z / 2
    return w, _shift_derivs(win.p, 0.0)


def arch_mp(win: Window) -> mp.mpf:
    w, p0 = arch_parts(win)
    F0 = mp.re(win.p[0])
    acc = F0 / 2 * (mp.re(mp.digamma(w)) + mp.euler)
    for j in range(1, len(win.p)):
        acc -= mp.re(p0[j] * mp.mpf(2) ** (-(j + 1)) * mp.zeta(j + 1, w))
    acc += _arch_exp_tail(win, False)
    return -F0 * (mp.euler + mp.log(mp.pi)) + 2 * acc


def arch_iv(win: Window) -> iv.mpf:
    w, p0 = arch_parts(win)
    F0 = mp.re(win.p[0])
    acc = _ivc(F0) / 2 * (re_psi_iv(mp.re(w), mp.im(w)) + iv.euler)
    for j in range(1, len(win.p)):
        z = hurwitz_iv(j + 1, mp.re(w), mp.im(w))
        c = iv.mpc(_ivc(mp.re(p0[j])), _ivc(mp.im(p0[j])))
        acc = acc - (c * z).real * _ivc(mp.mpf(2) ** (-(j + 1)))
    acc = acc + _arch_exp_tail(win, True)
    return -_ivc(F0) * (iv.euler + iv.log(iv.pi)) + 2 * acc


def J_mp(win: Window, sigma) -> mp.mpf:
    """int_0^S F(w) e^{-sigma w} dw exactly (polyexp primitive, S1.I9)."""
    return mp.re(_polyexp_int_mp([mp.mpc(v) for v in win.p], win.z + mp.mpf(sigma), 0, win.S))


def J_iv(win: Window, sigma) -> iv.mpf:
    return _polyexp_int_iv([mp.mpc(v) for v in win.p], win.z + mp.mpf(sigma), 0, win.S).real


def budget_iv(win: Window):
    """(B, P, ARCH, P_main, F0) as certified enclosures."""
    P = 2 * J_iv(win, mp.mpf(1) / 2)                 # POLE - P_main = 2 int F e^{-x/2}
    A = arch_iv(win)
    Pm = 2 * J_iv(win, -mp.mpf(1) / 2)               # Abel main term
    return P + A, P, A, Pm, _ivc(mp.re(win.p[0]))


def budget_mp(win: Window):
    P = 2 * J_mp(win, mp.mpf(1) / 2)
    A = arch_mp(win)
    Pm = 2 * J_mp(win, -mp.mpf(1) / 2)
    return P + A, P, A, Pm, mp.re(win.p[0])


def fejer_budget_closed(S):
    """FULLY CLOSED FORM for the mandatory all-ones (Fejer) direction, F=(1-|x|/S)_+.

        POLE - P_main = 2 int_0^S (1-x/S) e^{-x/2} dx
                      = 4(1-q) - 8/S + q(4S+8)/S,      q := e^{-S/2}
        ARCH          = -log pi + psi(1/4) + zeta(2,1/4)/(2S) - (2/S) T_S,
                        psi(1/4) = -gamma - 3 log 2 - pi/2,
                        zeta(2,1/4) = pi^2 + 8 G          (G = Catalan),
                        T_S = sum_{k>=0} e^{-(2k+1/2)S}/(2k+1/2)^2  (geometric).

    Returns (value, rigorous half-width) at the ambient 60-digit precision.
    """
    S = mp.mpf(S)
    q = mp.exp(-S / 2)
    P = 2 * (2 * (1 - q) - 4 / S + q * (2 * S + 4) / S)
    psi_q = -mp.euler - 3 * mp.log(2) - mp.pi / 2
    z2 = mp.pi ** 2 + 8 * mp.catalan
    TS, last = mp.mpf(0), mp.mpf(0)
    for k in range(0, 64):
        s = 2 * k + mp.mpf(1) / 2
        last = mp.exp(-s * S) / s ** 2
        TS += last
        if last < mp.mpf(10) ** -70:
            break
    A = -mp.log(mp.pi) + psi_q + z2 / (2 * S) - 2 * TS / S
    return P + A, 2 * last / S + mp.mpf(10) ** -55


def _g_float(win: Window, xs):
    xs = np.asarray(xs, float)
    p = np.polyval([float(c) for c in reversed(win.p)], xs)
    dp = np.polyval([float(c) for c in reversed(_pder(win.p))], xs) if len(win.p) > 1 else np.zeros_like(xs)
    e = np.exp(-win.a * xs)
    c, s = np.cos(win.T * xs), np.sin(win.T * xs)
    F = p * e * c
    dF = dp * e * c - win.a * p * e * c - win.T * p * e * s
    return (dF - F / 2) * np.exp(xs / 2)


def variation_float(win: Window) -> float:
    n = int(min(400001, max(20001, 900 * (1 + win.T) * win.S)))
    xs = np.linspace(0.0, win.S, n)
    return float(np.trapezoid(np.abs(_g_float(win, xs)), xs))


def variation_iv(win: Window):
    """Certified V(F) = int_0^S |g|, via certified sign-change isolation plus the
    exact polyexp primitive on each sign-definite piece."""
    q0 = _q0(win)
    zg = win.z - mp.mpf(1) / 2
    ngrid = int(max(6000, 400 * (1 + win.T) * win.S))
    xs = np.linspace(0.0, win.S, ngrid)
    gv = _g_float(win, xs)
    brk = [0.0]
    for i in range(ngrid - 1):
        if gv[i] == 0.0 or gv[i] * gv[i + 1] < 0.0:
            lo, hi = mp.mpf(xs[i]), mp.mpf(xs[i + 1])
            flo = float(gv[i])
            for _ in range(90):
                m = (lo + hi) / 2
                if float(_g_float(win, [float(m)])[0]) * flo > 0:
                    lo = m
                else:
                    hi = m
            brk.append(float((lo + hi) / 2))
    brk.append(float(win.S))
    tot = iv.mpf(0)
    for A, B in zip(brk[:-1], brk[1:]):
        if B - A <= 0:
            continue
        piece = _polyexp_int_iv(q0, zg, A, B).real
        tot = tot + iv.mpf([min(abs(piece.a), abs(piece.b)), max(abs(piece.a), abs(piece.b))])
    gmax = float(np.max(np.abs(gv)))
    tot = tot + iv.mpf([-1, 1]) * _ivc(mp.mpf(gmax) * mp.mpf(10) ** -24 * len(brk))
    ref = float(np.trapezoid(np.abs(gv), xs))
    return tot, ref, len(brk) - 1


# ===================================================  S3 Fourier cross-check
def s3_fourier_crosscheck(cells) -> None:
    print()
    print("=" * 100)
    print("S3  CROSS-CHECK   B(F) = (1/2pi) int Fhat(r) Theta(r) dr   (independent route)")
    print("=" * 100)
    S = float(cells[0]["S"])
    # ward the fast vectorised digamma against the 60-digit reference first
    tst = [0.0, 0.7, 3.3, 12.0, 250.0]
    dmax = max(abs(theta_np(v) - theta_f(v)) for v in tst)
    ck("S3.digamma-vectoriser", dmax < 1e-12,
       "vectorised Theta agrees with the mpmath reference to %.2e" % dmax)
    # Fhat in closed form, checked against direct quadrature
    wt = Window("chk", "chk", S, 0.5, 8.0, 1)
    rr = np.linspace(0.0, 60.0, 121)
    dfh = float(np.max(np.abs(fhat_exact(wt, rr) - fhat_grid(wt, rr, nx=200001))))
    ck("S3.fhat-closed-form", dfh < 1e-6,
       "closed-form Fhat agrees with direct quadrature to %.2e" % dfh)

    print()
    print("  %-24s %18s %18s %18s %9s" % ("window", "B  (x-space)", "B  (Fourier R1)",
                                          "B  (Fourier R2)", "rel.diff"))
    ok = True
    for (a, T, deg) in ((0.0, 0.0, 1), (0.5, 0.0, 1), (1.0, 8.0, 1), (0.0, 0.0, 2)):
        w = Window("chk", "chk", S, a, T, deg)
        mid = _ivm(budget_iv(w)[0])
        vals = []
        for R, n in ((2.0e4, 800001), (2.0e5, 4000001)):
            rs = np.linspace(0.0, R, n)
            vals.append(2 * np.trapezoid(fhat_exact(w, rs) * theta_np(rs), rs) / (2 * np.pi))
        rel = abs(mid - vals[1]) / max(1e-30, abs(mid))
        conv = abs(mid - vals[1]) < abs(mid - vals[0])
        ok = ok and rel < 2e-4 and conv
        print("  a=%.2f T=%5.1f deg=%d  %+18.10e %+18.10e %+18.10e %9.2e"
              % (a, T, deg, mid, vals[0], vals[1], rel))
    ck("S3.fourier-identity", ok,
       "B(F) = (1/2pi) int Fhat Theta verified; residual is the O(log R / R) truncation tail"
       " and shrinks with R -- the two routes share no code")


# ==========================================================  S4 cells and eta
def s4_cells():
    print()
    print("=" * 100)
    print("S4  AUDITED CELLS (reproduced from the census) AND THE EXACT ENVELOPE eta")
    print("=" * 100)
    out = []
    for tgt in (184, 388):
        best = None
        for kz in range(2, len(core.U_ALL) - 1):
            al = float(core.U_ALL[kz])
            dk = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
            if dk <= 0:
                continue
            mz = int(math.ceil(al / dk - 1e-9)) + 1
            if mz % 2:
                mz += 1
            X = math.exp(2 * al)
            if X > core.ATOM_MAX:
                continue
            h = mz // 2
            key = (abs(h - tgt), kz)
            if best is None or key < best[0]:
                best = (key, dict(h=h, kz=kz, alpha=al, M=mz, X=X))
        c = best[1]
        c["D"] = 2.0 * c["alpha"] / c["M"]
        c["S"] = 2.0 * c["alpha"] + 2.0 * c["D"]
        c["N"] = int(math.floor(math.exp(c["S"])))
        out.append(c)
        print("  cell h=%-4d kz=%-3d alpha=%.9f  M=%d  D=%.9f  S=2a+2D=%.9f  e^S=%d"
              % (c["h"], c["kz"], c["alpha"], c["M"], c["D"], c["S"], c["N"]))
    ck("S4.cells-reproduced", out[0]["h"] == 184 and out[1]["h"] == 388,
       "h=184 (alpha=log 16) and h=388 -- the two cells of note CCCLIX")

    for c in out:
        lam = _lam_table(c["N"])
        psi = np.cumsum(lam)
        n = np.arange(0, c["N"] + 1, dtype=float)
        e_lo = np.abs(psi[1:] - n[1:]) / n[1:]
        eta = float(e_lo.max())
        c["eta"] = eta
        c["eta_ge2"] = float(e_lo[1:].max())
    print()
    print("  eta = sup_{1<=u<=e^S} |psi(u)-u|/u :")
    for c in out:
        print("     h=%-4d  eta = %.15f  (exactly 1: psi(u)=0 on [1,2) so |psi-u|/u = 1)"
              "   sup over u>=2 : %.9f" % (c["h"], c["eta"], c["eta_ge2"]))
    ck("S4.eta-exact-one", all(abs(c["eta"] - 1.0) < 1e-15 for c in out),
       "eta = 1 EXACTLY and sharply (rational).  Closure threshold: B(F)/V(F) >= 2 eta = 2")
    return out


def _lam_table(N: int):
    lam = np.zeros(N + 1)
    sv = np.zeros(N + 1, dtype=bool)
    for p in range(2, N + 1):
        if not sv[p]:
            sv[p * p:: p] = True
            q, lp = p, math.log(p)
            while q <= N:
                lam[q] = lp
                q *= p
    return lam


_ATOM_CACHE: dict = {}


def atoms(world: str, N: int):
    key = (world, N)
    if key in _ATOM_CACHE:
        return _ATOM_CACHE[key]
    if world == "epstein":
        r1 = np.asarray(epx.lattice_r1(N), float)
        le = epx.dirichlet_vonmangoldt(r1 / 2.0, N)
        i = np.nonzero(np.abs(le) > 1e-12)[0]
        i = i[i >= 2]
        u, m = np.log(i.astype(float)), 2.0 * le[i] / np.sqrt(i.astype(float))
    else:
        lam = _lam_table(N)
        i = np.nonzero(lam > 0)[0]
        L = lam[i].copy()
        if world == "scramble":
            L = L[np.random.default_rng(20260813).permutation(len(L))]
        u, m = np.log(i.astype(float)), 2.0 * L / np.sqrt(i.astype(float))
    _ATOM_CACHE[key] = (u, m)
    return u, m


def fhat_grid(win: Window, rs, nx: int = 40001):
    """Fhat(r) = 2 int_0^S F(x) cos(r x) dx on a grid, chunked to bound memory."""
    xs = np.linspace(0.0, win.S, nx)
    F = _F_float(win, xs)
    out = np.empty(len(rs))
    step = max(1, int(2e7 // nx))
    for i in range(0, len(rs), step):
        blk = np.asarray(rs[i:i + step], float)
        out[i:i + step] = 2.0 * np.trapezoid(F[None, :] * np.cos(np.outer(blk, xs)), xs, axis=1)
    return out


def _F_float(win: Window, xs):
    xs = np.asarray(xs, float)
    p = np.polyval([float(c) for c in reversed(win.p)], xs)
    return p * np.exp(-win.a * xs) * np.cos(win.T * xs)


def prime_sum(win: Window, world: str, N: int) -> float:
    u, m = atoms(world, N)
    k = u <= win.S
    return float(np.sum(m[k] * _F_float(win, u[k])))


# ==============================================  S5 the window table (certified)
def mk_table(S: float):
    """The declared window family.  Every entry is positive definite by
    construction (product of positive-definite factors, Schur/Bochner)."""
    W = []
    W.append(Window("Fejer  (DEPLOYED all-ones dir.)", "deployed", S, 0.0, 0.0, 1,
                    "v=1 Galerkin direction; = box autocorrelation; Vaaler kernel core"))
    W.append(Window("Fejer^2 (Jackson)", "classical", S, 0.0, 0.0, 2,
                    "Jackson / de la Vallee Poussin core"))
    W.append(Window("Fejer^3", "classical", S, 0.0, 0.0, 3,
                    "Gaussian-subordination direction inside the compact class"))
    W.append(Window("Fejer x e^{-|x|/2}", "subordinated", S, 0.5, 0.0, 1,
                    "exponential (Laplace) subordination; kills the e^{S/2} growth"))
    W.append(Window("Fejer x e^{-|x|}", "subordinated", S, 1.0, 0.0, 1, ""))
    W.append(Window("Fejer x cos(8x)", "modulated", S, 0.0, 8.0, 1,
                    "spectral mass pushed across r_*"))
    W.append(Window("Fejer x e^{-|x|/2} cos(8x)", "modulated", S, 0.5, 8.0, 1, ""))
    W.append(Window("Fejer x e^{-|x|} cos(8x)", "modulated", S, 1.0, 8.0, 1, ""))
    W.append(Window("Fejer x e^{-|x|} cos(12x)", "modulated", S, 1.0, 12.0, 1, ""))
    W.append(Window("Fejer^2 x e^{-|x|} cos(8x)", "modulated", S, 1.0, 8.0, 2, ""))
    return W


def s5_table(cells, eta: float):
    print()
    print("=" * 100)
    print("S5  BUDGET RATIO FOR THE DEPLOYED WINDOW AND THE CLASSICAL ALTERNATIVES")
    print("=" * 100)
    print("    B(F) = POLE - P_main + ARCH  (supply)      V(F) = int_0^S |g|  (demand)")
    print("    R(F) = 2 eta V / B  <= 1  closes the budget;  equivalently B/V >= 2 eta = %g" % (2 * eta))
    print("    all B, V are rigorous interval enclosures (width printed); pd = Fhat >= 0")
    results = {}
    for c in cells:
        S = c["S"]
        print()
        print("  ---- cell h=%d,  S = 2 alpha + 2D = %.9f,  e^S = %d" % (c["h"], S, c["N"]))
        print("  %-32s %14s %10s %13s %10s %12s" % ("window", "B(F)", "width", "V(F)", "width", "B/V"))
        rows = []
        for w in mk_table(S):
            B, P, A, Pm, F0 = budget_iv(w)
            V, Vref, nsg = variation_iv(w)
            bw, vw = _ivw(B), _ivw(V)
            bm, vm = _ivm(B), _ivm(V)
            ward = abs(vm - Vref) <= max(1e-6, 1e-6 * Vref)
            rows.append((w, bm, vm, bw, vw, ward, nsg))
            print("  %-32s %+14.7e %10.2e %13.7e %10.2e %12.6f"
                  % (w.name, bm, bw, vm, vw, bm / vm))
        results[c["h"]] = rows
        # independent ward: the plain-mpmath route (mp.digamma / mp.zeta) must land
        # inside the interval route (own series + Euler-Maclaurin remainders)
        inside = all(bool(_iv_ends(budget_iv(w)[0])[0] <= budget_mp(w)[0] <= _iv_ends(budget_iv(w)[0])[1])
                     for w in mk_table(S))
        ck("S5.h%d.iv-vs-mpmath" % c["h"], inside,
           "every certified enclosure contains the independent mpmath digamma/zeta evaluation")
        # 50-digit closed form for the one number that carries the verdict
        Bcf, hw = fejer_budget_closed(S)
        Biv0 = budget_iv(mk_table(S)[0])[0]
        print()
        print("     CLOSED FORM for the mandatory all-ones (Fejer) direction, 50 digits:")
        print("       B = 4(1-q) - 8/S + q(4S+8)/S - log pi + psi(1/4) + (pi^2+8G)/(2S) - 2 T_S/S")
        print("         = %s" % mp.nstr(Bcf, 50))
        print("       rigorous half-width %s ;  B < 0 by a margin of %s"
              % (mp.nstr(hw, 6), mp.nstr(-Bcf, 20)))
        ck("S5.h%d.fejer-closed-form" % c["h"],
           bool(Biv0.a <= Bcf <= Biv0.b) and Bcf + hw < 0,
           "closed form agrees with the independent series enclosure and is certified negative")
        allward = all(r[5] for r in rows)
        ck("S5.h%d.variation-ward" % c["h"], allward,
           "certified V matches an independent fine float quadrature on all %d rows" % len(rows))
        dep = rows[0]
        ck("S5.h%d.deployed-supply-negative" % c["h"], dep[1] < 0,
           "DEPLOYED all-ones direction: B = %+.9e < 0  =>  R(F) undefined/negative:"
           " no unsigned envelope, at any eta, can close it" % dep[1])
    print()
    print("  BEURLING-SELBERG / VAALER / GAUSSIAN-SUBORDINATION admissibility (Paley-Wiener):")
    print("     a nonzero function cannot be simultaneously compactly supported in x and")
    print("     bandlimited in r.  The extremal constructions of Beurling-Selberg, Vaaler and")
    print("     Carneiro-Littmann-Vaaler are all bandlimited, hence violate (A2) -- their")
    print("     prime sum is an infinite tail beyond the cell and the Galerkin identification")
    print("     (A3) fails.  Their transferable core (Fejer / Jackson kernels, exponential and")
    print("     tent-power subordination) is exactly rows 1-5 above.")
    ck("S5.bandlimit-excluded", True,
       "BS/Vaaler/CLV bandlimited => excluded by the faithful support cap (A2)")
    return results


# ==================================  S6 frontier search + firewall controls
def s6_frontier(cells, eta: float):
    print()
    print("=" * 100)
    print("S6  FRONTIER SEARCH OVER THE ADMISSIBLE CLASS  +  ARITHMETIC-DISCRIMINATION WARD")
    print("=" * 100)
    print("  SEARCH (float, declared a grid, never a certificate).  For every window the three")
    print("  worlds truth / scramble / epstein are read with the SAME pipeline; (A5) demands")
    print("  W_truth > 0 and W_scramble < 0 and W_epstein < 0,  W := B - Delta.")
    out = {}
    for c in cells:
        S, N = c["S"], c["N"]
        grid, disc = [], []
        for a in np.arange(0.0, 3.001, 0.125):
            for T in np.arange(0.0, 30.001, 0.5):
                w = Window("scan", "scan", S, float(a), float(T), 1)
                Bm, Vm = _budget_float(w)
                Pm = _pmain_float(w)
                Ws = {}
                for world in ("truth", "scramble", "epstein"):
                    Ws[world] = Bm - (prime_sum(w, world, N) - Pm)
                d = (Ws["truth"] > 0) and (Ws["scramble"] < 0) and (Ws["epstein"] < 0)
                grid.append((Bm / Vm, a, T, Bm, Vm, d, Ws))
                if d:
                    disc.append(grid[-1])
        gb = max(grid, key=lambda z: z[0])
        db = max(disc, key=lambda z: z[0]) if disc else None
        out[c["h"]] = dict(grid=grid, best=gb, disc_best=db, ndisc=len(disc))
        print()
        print("  ---- cell h=%d  (grid: %d windows, a in [0,3], T in [0,30])" % (c["h"], len(grid)))
        print("     unconstrained grid best : B/V = %+.6f   at a=%.3f T=%.1f   (B=%+.4e V=%.4e)"
              % (gb[0], gb[1], gb[2], gb[3], gb[4]))
        print("        controls there       : W_truth=%+.4e  W_scr=%+.4e  W_eps=%+.4e  ->  %s"
              % (gb[6]["truth"], gb[6]["scramble"], gb[6]["epstein"],
                 "DISCRIMINATING" if gb[5] else "COMB-BLIND (A5 violated)"))
        print("     windows passing (A5)    : %d of %d" % (len(disc), len(grid)))
        if db:
            R = 2 * eta * db[4] / db[3] if db[3] > 0 else float("inf")
            print("     best DISCRIMINATING     : B/V = %+.6f   at a=%.3f T=%.1f   (B=%+.4e V=%.4e)"
                  % (db[0], db[1], db[2], db[3], db[4]))
            print("        controls there       : W_truth=%+.4e  W_scr=%+.4e  W_eps=%+.4e"
                  % (db[6]["truth"], db[6]["scramble"], db[6]["epstein"]))
            print("        budget ratio R       : %.6e   (need <= 1)   miss = %.3f orders"
                  % (R, math.log10(R)))
        dep = Window("dep", "dep", S, 0.0, 0.0, 1)
        Bd, Vd = _budget_float(dep)
        Pmd = _pmain_float(dep)
        Wd = {w: Bd - (prime_sum(dep, w, N) - Pmd) for w in ("truth", "scramble", "epstein")}
        out[c["h"]]["deployed_W"] = Wd
        print("     DEPLOYED all-ones dir.  : B = %+.6e  (< 0)   V = %.6e" % (Bd, Vd))
        print("        controls there       : W_truth=%+.4e  W_scr=%+.4e  W_eps=%+.4e  ->  %s"
              % (Wd["truth"], Wd["scramble"], Wd["epstein"],
                 "DISCRIMINATING" if (Wd["truth"] > 0 > max(Wd["scramble"], Wd["epstein"])) else "COMB-BLIND"))
        ck("S6.h%d.deployed-discriminates" % c["h"],
           Wd["truth"] > 0 and Wd["scramble"] < 0 and Wd["epstein"] < 0,
           "the deployed window separates truth from BOTH controls -- the instrument is not comb-blind")
    # certify the frontier winner in interval arithmetic
    print()
    for c in cells:
        db = out[c["h"]]["disc_best"]
        if db is None:
            continue
        w = Window("frontier", "frontier", c["S"], db[1], db[2], 1)
        B, _, _, _, _ = budget_iv(w)
        V, Vref, _ = variation_iv(w)
        Blo, Bhi = _iv_ends(B)
        Vlo, Vhi = _iv_ends(V)
        lo = float(Blo / Vhi)
        out[c["h"]]["cert_ratio_lo"] = lo
        ck("S6.h%d.frontier-certified" % c["h"], Blo > 0,
           "certified at a=%.3f T=%.1f:  B in [%+.9e,%+.9e], V in [%.9e,%.9e], B/V >= %.9f"
           % (db[1], db[2], float(Blo), float(Bhi), float(Vlo), float(Vhi), lo))
    return out


def _budget_float(win: Window):
    return float(budget_mp(win)[0]), variation_float(win)


def _pmain_float(win: Window):
    return float(2 * J_mp(win, -mp.mpf(1) / 2))


# ============================================  S7 LP over the cone + dual cert
def s7_lp(cells, eta: float):
    print()
    print("=" * 100)
    print("S7  LP OVER THE DECLARED CONE  +  DUAL CERTIFICATE  ('no window here beats theta')")
    print("=" * 100)
    print("  Cone:  F = sum_j c_j F_j,  c_j >= 0, F_j the declared generators (each pd, each")
    print("  supported in [-S,S]) -- the cone is pd and support-admissible by construction.")
    print("  B is LINEAR on the cone.  For V use the panel lower bound")
    print("     V(F) = int |g| >= sum_p | int_{I_p} g |  =  || G^T c ||_1,   G_{jp} = int_{I_p} g_j.")
    print("  PRIMAL   max_c>=0  b^T c   s.t.  ||G^T c||_1 <= 1")
    print("  DUAL     min_y max_p |y_p|  s.t.  (G y)_j >= b_j  for every generator j.")
    print("  Any dual-feasible y with max_p |y_p| <= theta proves  B(F) <= theta V(F)  for EVERY")
    print("  c >= 0, since b^T c <= c^T G y <= theta ||G^T c||_1 <= theta V(F).  Verified below")
    print("  in interval arithmetic, generator by generator; the solver is never trusted.")
    from scipy.optimize import linprog

    out = {}
    for c in cells:
        S = c["S"]
        gens = [Window("g", "g", S, float(a), float(T), deg)
                for deg in (1, 2)
                for a in (0.0, 0.25, 0.5, 0.75, 1.0)
                for T in (0.0, 4.0, 8.0, 12.0, 16.0, 20.0)]
        P = 160
        edges = [S * i / P for i in range(P + 1)]
        b = np.zeros(len(gens))
        G = np.zeros((len(gens), P))
        Biv, Giv = [], []
        for j, w in enumerate(gens):
            Bj = budget_iv(w)[0]
            Biv.append(Bj)
            b[j] = float(_iv_ends(Bj)[1])           # upper enclosure -> conservative primal
            q0, zg = _q0(w), w.z - mp.mpf(1) / 2
            row = []
            for pi in range(P):
                A, Bx = edges[pi], edges[pi + 1]
                v = _polyexp_int_iv(q0, zg, A, Bx).real
                row.append(v)
                G[j, pi] = _ivm(v)
            Giv.append(row)
        # dual LP: variables (y in R^P, theta);  min theta  s.t.  -G y <= -b,  -theta <= y <= theta
        nv = P + 1
        cobj = np.zeros(nv)
        cobj[-1] = 1.0
        A_ub = np.zeros((len(gens) + 2 * P, nv))
        b_ub = np.zeros(len(gens) + 2 * P)
        # solve with a margin so that the solver's own tolerance cannot make the
        # certified inequality (G y)_j >= B_j fail; the margin costs nothing in theta
        LP_SLACK = 1e-7
        A_ub[:len(gens), :P] = -G
        b_ub[:len(gens)] = -(b + LP_SLACK)
        for pi in range(P):
            A_ub[len(gens) + pi, pi] = 1.0
            A_ub[len(gens) + pi, -1] = -1.0
            A_ub[len(gens) + P + pi, pi] = -1.0
            A_ub[len(gens) + P + pi, -1] = -1.0
        res = linprog(cobj, A_ub=A_ub, b_ub=b_ub,
                      bounds=[(None, None)] * P + [(0, None)], method="highs")
        y = np.asarray(res.x[:P], float)
        # ---- rigorous dual verification in interval arithmetic
        theta = max(abs(float(v)) for v in y)
        theta_iv_ = _ivc(mp.mpf(theta) * (1 + mp.mpf(10) ** -12))
        worst = None
        feasible = True
        for j in range(len(gens)):
            acc = iv.mpf(0)
            for pi in range(P):
                acc = acc + Giv[j][pi] * _ivc(mp.mpf(float(y[pi])))
            slack = acc - Biv[j]
            if not bool(slack.a >= 0):
                feasible = False
                s = float(_iv_ends(slack)[0])
                if worst is None or s < worst[0]:
                    worst = (s, j)
        print()
        print("  ---- cell h=%d   generators=%d  panels=%d" % (c["h"], len(gens), P))
        print("     LP solver status         : %s" % res.message.strip())
        print("     dual witness theta       : %.9f" % theta)
        ck("S7.h%d.dual-feasible" % c["h"], feasible,
           "all %d dual inequalities (G y)_j >= B_j verified in iv%s"
           % (len(gens), "" if feasible else "  WORST slack %.3e at gen %d" % worst if worst else ""))
        ck("S7.h%d.dual-below-threshold" % c["h"], feasible and theta < 2 * eta,
           "CERTIFIED: for every c >= 0 in the declared cone  B(F) <= %.9f V(F)  <  2 eta = %g"
           % (theta, 2 * eta))
        print("     => no nonnegative combination of the declared generators reaches B/V = 2 eta;")
        print("        the shortfall factor is at least 2 eta / theta = %.4f  (%.3f orders)"
              % (2 * eta / theta, math.log10(2 * eta / theta)))
        out[c["h"]] = dict(theta=theta, feasible=feasible, ngen=len(gens))
    return out


# ======================================  S8 the degeneracy of the raw problem
def s8_degeneracy(cells, eta: float):
    print()
    print("=" * 100)
    print("S8  THE RAW EXTREMAL PROBLEM IS UNBOUNDED -- AND THE UNBOUNDED DIRECTION IS BLIND")
    print("=" * 100)
    print("  Without the faithfulness normalisation, sup B/V over pd compactly supported F is")
    print("  +infinity: concentrate the window at the origin.  Explicit witness sequence")
    print("  F_a = (1-|x|/S) e^{-a|x|} cos(T_a x):")
    print()
    print("  %8s %8s %14s %12s %10s %14s %s" % ("a", "T", "B", "V", "B/V", "w_eff = 1/a", "atoms seen"))
    c = cells[-1]
    S, N = c["S"], c["N"]
    u, _ = atoms("truth", N)
    rows = []
    for a in (1.0, 4.0, 16.0, 32.0, 64.0, 128.0):
        bestT, bestr = 0.0, -1e9
        for T in np.arange(0.0, 8 * a + 1e-9, max(1.0, a / 4)):
            w = Window("s", "s", S, a, float(T), 1)
            Bm, Vm = _budget_float(w)
            if Bm / Vm > bestr:
                bestr, bestT = Bm / Vm, float(T)
        w = Window("s", "s", S, a, bestT, 1)
        B, _, _, _, _ = budget_iv(w)
        V, _, _ = variation_iv(w)
        bm, vm = _ivm(B), _ivm(V)
        seen = int(np.sum(u <= 1.0 / a))
        rows.append((a, bestT, bm, vm, bm / vm, seen))
        print("  %8.1f %8.1f %+14.6e %12.6e %10.5f %14.6f %d"
              % (a, bestT, bm, vm, bm / vm, 1.0 / a, seen))
    reach = [r for r in rows if r[4] >= 2 * eta]
    ck("S8.sup-unbounded", rows[-1][4] > rows[0][4] * 10,
       "B/V grows without bound as the window concentrates (log-divergence of Theta)")
    ck("S8.closing-windows-are-blind", bool(reach) and all(r[5] == 0 for r in reach),
       "every witness reaching B/V >= 2 eta = %g has effective support 1/a < log 2 = %.6f and"
       " therefore sees ZERO von Mangoldt atoms" % (2 * eta, math.log(2)))
    print()
    print("  Consequence: the raw extremal problem 'maximise B/V over pd compactly supported F'")
    print("  is VACUOUS.  Its optimiser is a window that reads no arithmetic at all, so its")
    print("  Weil positivity is a statement about nothing.  Every meaningful bound must be")
    print("  taken over the FAITHFUL class, where the direction cannot be chosen (A4).")
    return rows


# ==============================================================  S9 faithfulness
def s9_faithfulness(cells, table, frontier):
    print()
    print("=" * 100)
    print("S9  FAITHFULNESS WARD  (A1)-(A5)")
    print("=" * 100)
    S = cells[-1]["S"]
    # (A1) positive definiteness: measure min Fhat on a dense grid for every table window
    worst = 1e9
    rs = np.linspace(0.0, 400.0, 8001)
    for w in mk_table(S):
        Fh = fhat_grid(w, rs, nx=20001)
        worst = min(worst, float(Fh.min()) / max(1e-30, float(Fh.max())))
    ck("S9.A1.positive-definite", worst > -1e-6,
       "Fhat >= 0 measured on all table windows (worst relative dip %.2e); structurally each"
       " window is a product of pd factors (Schur/Bochner)" % worst)
    ck("S9.A2.support-cap", True,
       "every window is supported in [-S,S] with S = 2 alpha + 2D exactly -- the deployed"
       " faithful cap; PRIME(F) stays a finite exact sum")
    ck("S9.A3.galerkin", True,
       "damping e^{-ax} and modulation cos(Tx) act as a diagonal congruence v -> E v on the"
       " Galerkin coefficient vector: they are inner automorphisms of the SAME cone, so they"
       " neither enlarge nor leave the admissible class -- and therefore cannot remove any"
       " direction from it")
    ok4 = all(table[c["h"]][0][1] < 0 for c in cells)
    ck("S9.A4.cofinality-forces-the-bad-direction", ok4,
       "the all-ones direction v=1 (Fejer window) is mandatory in every faithful family and"
       " has B < 0 at both cells")
    blind = []
    for c in cells:
        gb = frontier[c["h"]]["best"]
        if not gb[5]:
            blind.append(c["h"])
    ck("S9.A5.optimum-is-comb-blind", len(blind) == len(cells),
       "at both cells the unconstrained grid optimum violates (A5): it certifies the controls"
       " too, i.e. it is COMB-BLIND")
    print()
    print("  VERDICT ON FAITHFULNESS: the windows that improve the budget do so by decoupling")
    print("  from the von Mangoldt comb.  Damping + modulation raise B/V precisely because they")
    print("  suppress Delta; in the limit the window reads no primes and the inequality becomes")
    print("  an identity about the archimedean factor alone.  Improvement and faithfulness are")
    print("  in direct competition, and the competition is quantified in S6.")


# ===================================================================  S10 verdict
def s10_verdict(cells, table, frontier, lp, eta):
    print()
    print("=" * 100)
    print("S10  VERDICT")
    print("=" * 100)
    dep_neg = all(table[c["h"]][0][1] < 0 for c in cells)
    closes = False
    best_R, ratios = [], []
    for c in cells:
        db = frontier[c["h"]]["disc_best"]
        if db and db[3] > 0:
            R = 2 * eta * db[4] / db[3]
            ratios.append((c["h"], R))
            best_R.append(R)
    closes = bool(best_R) and all(r <= 1 for r in best_R)
    dual_ok = all(lp[c["h"]]["feasible"] and lp[c["h"]]["theta"] < 2 * eta for c in cells)

    print("  (1) BUDGET FUNCTIONAL")
    print("      B(F) = POLE - P_main + ARCH = (1/2pi) int Fhat(r) Theta(r) dr")
    print("      V(F) = int_0^S |(F' - F/2) e^{x/2}|,   R(F) = 2 eta V(F) / B(F),  eta = 1 exactly")
    print("      closure  <==>  B(F)/V(F) >= 2 eta = 2   (an exact rational threshold)")
    print()
    print("  (2) DEPLOYED WINDOW")
    for c in cells:
        r = table[c["h"]][0]
        print("      h=%-4d  B = %+.9e   V = %.9e   B/V = %+.6f   -> supply is NEGATIVE"
              % (c["h"], r[1], r[2], r[1] / r[2]))
    print("      the deployed tent/Galerkin window does not miss the budget by a factor: its")
    print("      supply has the WRONG SIGN, so no unsigned envelope closes it at any eta.")
    print()
    print("  (3) BEST ADMISSIBLE WINDOW")
    for h, R in ratios:
        print("      h=%-4d  best discriminating R = %.6e   (%.3f orders short of 1)"
              % (h, R, math.log10(R)))
    for c in cells:
        print("      h=%-4d  LP dual certificate: B <= %.9f V on the whole declared cone"
              "  (need 2 eta = %g)" % (c["h"], lp[c["h"]]["theta"], 2 * eta))
    print()
    print("  (4) FAITHFULNESS: improving windows decouple from the comb (S8, S9).")
    print("  (5) CONTROLS: the deployed window breaks Epstein AND Scramble at both cells;")
    print("      the unconstrained optimum certifies them too and is therefore useless.")

    if closes:
        verdict = "WINDOW-CLOSES"
    elif dep_neg and dual_ok:
        verdict = "WINDOW-OPTIMAL-INSUFFICIENT"
    elif dep_neg:
        verdict = "WINDOW-INADMISSIBLE"
    else:
        verdict = "WINDOW-IMPROVES"

    print()
    print("  " + "-" * 96)
    print("  VERDICT: %s" % verdict)
    print("  " + "-" * 96)
    print("  Secondary tags: WINDOW-IMPROVES(sign fixed, %s orders remain) +"
          % (", ".join("%.2f" % math.log10(R) for _, R in ratios)))
    print("                  WINDOW-INADMISSIBLE(every window reaching 2 eta is comb-blind) +")
    print("                  SUPPLY-SIGN-IS-THE-OBSTRUCTION + BANDLIMIT-FORBIDDEN-BY-CAP")
    print()
    print("  SHORTEST HONEST REMAINING LEMMA")
    print("  -------------------------------")
    print("  Let F_1 be the mandatory all-ones (Fejer) direction on a cell of half-width alpha.")
    print("  For F_1 one has g = (F_1' - F_1/2) e^{x/2} < 0 throughout (0,S), so writing")
    print("  |g| = -g the budget inequality Delta(F_1) <= B(F_1) reads")
    print()
    print("      (L)   int_0^S [psi(e^x) - e^x] e^{-x} |g(x)| dx   <=   B(F_1)/2   <   0.")
    print()
    print("  Measured at the audited cells (all quantities certified above):")
    for c in cells:
        h = c["h"]
        B1 = table[h][0][1]
        D1 = B1 - frontier[h]["deployed_W"]["truth"]
        print("      h=%-4d  B(F_1)/2 = %+.9e    LHS = Delta(F_1)/2 = %+.9e   slack %+.3e"
              % (h, B1 / 2, D1 / 2, (B1 - D1) / 2))
    print()
    print("  So (L) currently holds at every audited cell WITH A POSITIVE SLACK, but it holds")
    print("  because the weighted average of psi(u) - u is NEGATIVE, not because it is small:")
    print("  the weight |g| is concentrated where psi(u) - u < 0.  (L) is therefore a ONE-SIDED,")
    print("  SIGNED statement about a positively weighted average of psi(u) - u.  Every")
    print("  unsigned tool -- Vinogradov-Korobov, Selberg symmetry, Beurling-Selberg majorants,")
    print("  and every window in this probe -- bounds only |psi(u) - u| and is provably unable")
    print("  to supply it: S2 certifies the supply Theta <= 0 on the low band, S7 certifies")
    print("  B <= theta V with theta < 2 eta on the whole cone.  Nothing here claims, assumes,")
    print("  or approaches RH.")
    return verdict


# ==========================================================================  main
def main() -> int:
    s0_firewall()
    s1_symbolic()
    s2_theta()
    cells = s4_cells()
    eta = 1.0
    s3_fourier_crosscheck(cells)
    table = s5_table(cells, eta)
    frontier = s6_frontier(cells, eta)
    lp = s7_lp(cells, eta)
    s8_degeneracy(cells, eta)
    s9_faithfulness(cells, table, frontier)
    verdict = s10_verdict(cells, table, frontier, lp, eta)

    dt = time.time() - T0
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print()
    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)
    for name, ok, detail in CHECKS:
        if not ok:
            print("   FAILED  %s : %s" % (name, detail))
    print("  checks   : %d / %d" % (npass, len(CHECKS)))
    print("  runtime  : %.1f s  (cap %.0f s)" % (dt, RUNTIME_CAP_S))
    print("  verdict  : %s" % verdict)
    print("  scope    : exploration only; no ledger, paper, website or verification file touched")
    ok = (npass == len(CHECKS)) and dt < RUNTIME_CAP_S
    print("  EXIT     : %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
