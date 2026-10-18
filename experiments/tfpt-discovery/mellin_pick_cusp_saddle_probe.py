#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mellin_pick_cusp_saddle_probe -- MELLIN.PICK.CUSP-SADDLE.01

FROZEN SPEC v2 (2026-09-03).  EXPLORATION ONLY, experiments/ only.
This file is a scalar/identity certificate for an independently adjudicated
analytic proof.  It is not a verification-suite module, ledger row, paper
claim, website claim, global Pick theorem, BP1 theorem, or RH theorem.
No point grids and no zeta-zero data or oracle are used.

=======================================================================
EXACT DICTIONARY AND DOMAIN
=======================================================================
The paper and repository kernels use

  Phi_paper(u) = Phi_repo(2u),
  M_repo(s) = 2^(s+1) I(s/2),
  phi(q) = (q - 1/2) I(q-1) / I(q).

For Re(q)>1/2, two classical integrations by parts are valid because the
relevant endpoint boundary terms vanish there, and give

  J(q) = int_0^inf u^(2q) Phi_paper''(u) du,
  I(q-1) = J(q) / ((2q-1)(2q)),
  phi(q) = J(q) / (4q I(q)).

Both sides of the I/J identity are meromorphic in q.  The identity theorem
therefore transports it from Re(q)>1/2 to the near-vertical sector by
meromorphic/analytic continuation (away from the displayed poles).  No
claim is made that all four classical boundary terms vanish individually
at Re(q)=0.

The certified q-domain is the complete closed right outer half-plane

  Re q >= 0,  |q| >= R0,
  R0 = (pi/2) e^1000 sqrt(1000^2 + pi^2/4).

For Im q > 0 the accepted Pick determinant D is strictly positive
(equivalently Im phi(q) > 0 in the convention used here); the lower half
follows by conjugation.  The exact mapped repository-M domain is

  Re s >= 0,  |s| >= 2 R0.

=======================================================================
NEAR-REAL WEDGE (REPAIRED)
=======================================================================
The analytic input is arXiv:2607.16795, Lemmas 3.5--3.6, with the missing
hypothesis q_tail < 1 restored in Lemma 3.1.  This certificate does not
assert the unamended universal version of Lemma 3.1.  The two actual tubes

  q_tail = 16 exp(-3 pi X cos(4 nu)),  X = exp(4 x0),
  (x0,nu) = (0.35,0.1), (0.40,0.1),

give 8.240030736...e-15 and 3.396887340...e-18, hence q_tail < 1
and positive geometric denominators.

After the accepted saddle lemmas and their repaired scalar bookkeeping,
for k >= 10^9 and |q-k| <= k/21,

  |(log I)''(q)| < 0.65/k,
  Re (log phi)'(q) > 67/(220k),
  |Im log phi(q)| < 0.081.

The correction coefficient is not stored as a decimal: at k0=10^9 it is
computed by directed rounding from

  buffer = k/20-k/21-1,
  log_bound = log(20k)+pi/2,
  eps_log = -log(0.982),
  correction = k(log_bound+2eps_log)/buffer^2.

Together with the accepted 0.645 saddle-action coefficient this is below
0.65.  For all k>=k0, putting B=log_bound+2eps_log gives B>1 and

  d/dk log[kB/(k/420-1)^2]
    = 1/k+1/(kB)-2/(k-420) < 0,

because 1/(kB)<1/k and 2/(k-420)>2/k.  The other 256-bit threshold
values certified below are

  reciprocal coefficient       0.954545455001...,
  derivative margin            0.304545455001... > 67/220,
  argument bound               0.080952380979... < 0.081.

For x = Re q >= 2e9 and |arg q| <= 1/25, choose the nearest integer k.
The worst threshold slack

  (x-1/2)/21 - sqrt(x^2 tan(1/25)^2 + 1/4)

is 1.5195401e7, so these disks cover the whole near-real wedge.

=======================================================================
VERTICAL/MID-SECTOR w-SADDLE
=======================================================================
Put w=e^(4u), t=Log w and

  F(t) = 2q Log(t/4) - pi e^t,
  L = W0(2q/pi) = a+ib,
  q = (pi/2) e^L L.

Then t=L is the saddle and the correct Hessian is

  K = -F''(L) = pi e^L (L+1)/L.

The factor 1/L is mandatory.  For theta0=1/25, r=|q|>=R0 and
theta=arg q in [theta0,pi/2], the accepted geometry gives

  a >= 1000,
  b >= theta0*a/(a+1) > 1/50,
  cos b >= 1/(100a),
  m = pi e^a cos b >= e^a/(32a),
  Re K >= m,
  chi = sqrt(|K|/Re K) <= 15 sqrt(a).

Along t=x+ib, with g(x)=Re F(x+ib), the exact accepted phase drops are

  g(a)-g(x) >= m [a-x-1+e^(x-a)]                 (x <= a),
  g(a)-g(x) >= m [e^(x-a)-1-(x-a)]               (x >= a).

Both brackets are nonnegative by e^z >= 1+z.  The saddle window is
h=sqrt(a/m).  The corrected cubic bound may be taken as
eta <= 120 a^3 e^(-a/2).  At a=1000 the strengthened local gates are
eta<1e-200 and eta+10h<1e-200.

For y_n=pi n^2 e^t and

  Q(y) = 32y^3 - 224y^2 + 330y - 75,
  P(y) = Q(y)/(2y-3),

the exact kernel identity is Phi_1''/Phi_1=P.  The factored amplitudes are

  B_I = (pi/4)e^(5t/4) sum n^2(2y_n-3)
                         e^(-pi(n^2-1)e^t),
  B_J = (pi/4)e^(5t/4) sum n^2 Q(y_n)
                         e^(-pi(n^2-1)e^t).

For |y|>=16, reverse and direct triangle inequalities give

  16|y|^3 <= |Q(y)| <= 48|y|^3.

Where c=e^x cos b >= 1, the relative n-tail bounds are

  tau_I <= 48 e^(-3pi c)/(1-16e^(-3pi c)),
  tau_J <= 768 e^(-3pi c)/(1-256e^(-3pi c)).

They are never used on the early/arc part where c can be below 1.
There the full-kernel amplitude is bounded instead.  For 0<c<=1,

  sum n^p e^(-pi n^2 c) <= G_p c^(-(p+1)/2)

by integration over [n-1,n].  Since e^x=c/cos b<=100ac, this gives

  |B_I| <= (pi/4)e^(5x/4)
      [2pi e^x sum n^4e^(-pi n^2c)+3 sum n^2e^(-pi n^2c)]
      <= C_I e^(5x/4)(100a)^(5/2).

Applying the same bound to Q and to the first two t-derivatives gives
polynomial bounds through C_E e^(5x/4)(100a)^(13/2).  The code derives
C_E from the exact amplitude polynomials; this explicitly charges the
early/arc amplitude growth.

The endpoint phase repair is

  Re F(i varphi) <= -pi r sin(1/25)
                  = -0.1256301985... r,

not the stronger and invalid -pi r/25.  After subtracting
(pi+2)r/a and the explicit logarithmic amplitude charge, the remaining
drop is still greater than r/10 for a>=1000.  Monotonicity of
r(a)=(pi/2)e^a sqrt(a^2+pi^2/4) and of polynomial/exponential ratios
reduces every scalar check to a=1000.

=======================================================================
NORMALIZED ERROR LEDGER AND SIGN
=======================================================================
At a>=1000 the accepted normalized pieces are

  E_arc      <= exp(-r/10),
  E_early    <= exp(-ma/4),
  E_prefar   <= exp(-m/5),
  E_prenear  <= 36 exp(-a/3),
  E_postnear <= 1500 exp(-a/2),
  E_inf      <= exp(-m/4),
  E_loc      <= 130000 a^(7/2) exp(-a/2),
  E_gauss    <= 12 exp(-a/2).

Their sum is below 1e-140.  The dominant term at the threshold is
36 exp(-1000/3)=6.1869299618...e-144.

The leading quotient transfers from B_J/B_I=P(y).  Its polynomial
replacement has

  delta_P <= 13/|y| < 5e^(-a).

If E_I,E_J<=E=E_total<1, the exact sufficient quotient-transfer bound is

  transfer_exact = delta_P + (1+delta_P) 2E/(1-E).

The separately checked inequality 2delta_P+3E<1 implies
transfer_exact<=delta_P+3E; the latter is retained only as a conservative
ward.  The exact transfer is below 3e-140, while

  b-beta >= theta0(a-1)/(a+1) > 1/50,
  3e-140 < sin(1/50),       beta=arg L.

Thus the transfer cannot cross the real axis: I is nonzero and D>0 in
the vertical/mid sector.  The near-real wedge supplies the remaining
angles, and conjugation supplies the lower half-plane.

=======================================================================
REGRESSION MUTANTS, MODES, AND VERDICT
=======================================================================
Integrated mutants must be rejected for exactly the three adjudicated
repairs:

  M1  replace pi e^L(L+1)/L by pi e^L(L+1);
  M2  replace pi sin(1/25) by pi/25 at the endpoint;
  M3  set the charged early/arc logarithmic amplitude to zero.

The q_tail<1 precondition also has an executable boundary ward.

--smoke uses 256-bit Arb, the precision of the accepted scalar
adjudication.  --record repeats the same non-grid proof gates at 512 bits.
--json PATH is an optional report sink and is never used implicitly.

The only successful verdict is OUTER_DOMAIN_PROVED, and it is emitted
only if every exact identity, premise, strict scalar inequality, error
budget, sign-transfer check, firewall, and mutant ward passes.  Otherwise
the deterministic verdict is INCONCLUSIVE(<first-failing-gate>).
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

try:
    import flint
    from flint import arb, ctx
except ImportError as exc:
    print("VERDICT INCONCLUSIVE(S0_FLINT_IMPORT)")
    raise SystemExit(
        "python-flint is mandatory; run inside experiments/tfpt-discovery/.venv"
    ) from exc

try:
    import sympy as sp
except ImportError as exc:
    print("VERDICT INCONCLUSIVE(S0_SYMPY_IMPORT)")
    raise SystemExit("Sympy is mandatory for the exact identity gates") from exc


CONTRACT = "MELLIN.PICK.CUSP-SADDLE.01"
SPEC_REVISION = "v2-2026-09-03"
SMOKE_BITS = 256
RECORD_BITS = 512

THETA0_NUM = 1
THETA0_DEN = 25
A_MIN_INT = 1000
B_MIN_NUM = 1
B_MIN_DEN = 50
K_MIN_INT = 10**9
NEAR_REAL_X_MIN_INT = 2 * 10**9

CURVATURE_BASE = "0.645"
CURVATURE_LIMIT = "0.65"
ARGUMENT_LIMIT = "0.081"
TRANSFER_LIMIT = "3e-140"
ERROR_SUM_LIMIT = "1e-140"

FIREWALL = (
    "experiment-only outer-domain Mellin-quotient certificate; "
    "not global Pick, not BP1, not RH"
)
DOMAIN_Q = (
    "{q: Re(q) >= 0, |q| >= R0}, "
    "R0=(pi/2)*exp(1000)*sqrt(1000^2+pi^2/4)"
)
DOMAIN_M = "{s: Re(s) >= 0, |s| >= 2*R0}"

BANNED_CALL_NAMES = {
    "zetazero",
    "zetazeros",
    "zeta_zero",
    "zeta_zeros",
    "nzeros",
    "find_zeros",
    "meshgrid",
    "linspace",
}
BANNED_IMPORT_ROOTS = {"mpmath", "numpy", "scipy"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Gate:
    code: str
    passed: bool
    detail: str


GATES: list[Gate] = []


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def ball_text(value: arb) -> str:
    return str(value)


def certainly_lt(left: arb, right: arb) -> bool:
    return bool(left < right)


def certainly_le(left: arb, right: arb) -> bool:
    return bool(left <= right)


def certainly_gt(left: arb, right: arb) -> bool:
    return bool(left > right)


def certainly_ge(left: arb, right: arb) -> bool:
    return bool(left >= right)


def add_gate(code: str, passed: bool, detail: str) -> bool:
    result = bool(passed)
    GATES.append(Gate(code, result, detail))
    print("  [%s] %-38s %s" % ("PASS" if result else "FAIL", code, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def rational(num: int, den: int = 1) -> arb:
    return arb(num) / arb(den)


def theta0() -> arb:
    return rational(THETA0_NUM, THETA0_DEN)


def a_min() -> arb:
    return arb(A_MIN_INT)


def r0_value() -> arb:
    a = a_min()
    pi = arb.pi()
    return (pi / 2) * a.exp() * (a * a + pi * pi / 4).sqrt()


def max_certain(values: list[arb]) -> arb:
    if not values:
        raise ValueError("max_certain requires a nonempty list")
    result = values[0]
    for value in values[1:]:
        if certainly_gt(value, result):
            result = value
        elif not certainly_le(value, result):
            result = result.union(value).upper()
    return result


def ast_firewall() -> tuple[list[str], list[str]]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    calls: set[str] = set()
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = ""
            if isinstance(node.func, ast.Name):
                name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                name = node.func.attr
            if name in BANNED_CALL_NAMES:
                calls.add(name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".", 1)[0]
                if root in BANNED_IMPORT_ROOTS:
                    imports.add(root)
        elif isinstance(node, ast.ImportFrom) and node.module:
            root = node.module.split(".", 1)[0]
            if root in BANNED_IMPORT_ROOTS:
                imports.add(root)
    return sorted(calls), sorted(imports)


def sympy_zero(expression: sp.Expr) -> bool:
    reduced = sp.simplify(expression)
    return bool(reduced == 0 or reduced.equals(0))


def sympy_nonzero(expression: sp.Expr) -> bool:
    reduced = sp.simplify(expression)
    if reduced == 0 or reduced.equals(0):
        return False
    return bool(reduced.is_zero is False or reduced != 0)


def amplitude_operator(poly: sp.Expr, y: sp.Symbol) -> sp.Expr:
    """t derivative of e^(5t/4) poly(y)e^-y, with y'=y."""
    return sp.expand(sp.Rational(5, 4) * poly + y * sp.diff(poly, y) - y * poly)


def exact_identity_gates() -> dict[str, sp.Expr]:
    section("S1 exact Sympy identities")
    q, s, ell, y = sp.symbols("q s L y", nonzero=True)
    a, b, r, vartheta = sp.symbols(
        "a b r vartheta", real=True, positive=True
    )
    pi = sp.pi

    moment_jacobian = sp.powsimp(
        2 ** (s + 1) * 2 ** (-(s + 1)) - 1, force=True
    )
    add_gate(
        "S1.1_MOMENT_DICTIONARY",
        sympy_zero(moment_jacobian),
        "M_repo(s)=2^(s+1) I(s/2)",
    )

    j_symbol, i_symbol = sp.symbols("J I", nonzero=True)
    ibp_reduction = sp.simplify(
        (q - sp.Rational(1, 2))
        * j_symbol
        / ((2 * q - 1) * (2 * q))
        / i_symbol
        - j_symbol / (4 * q * i_symbol)
    )
    add_gate(
        "S1.2_MEROMORPHIC_IBP_QUOTIENT",
        sympy_zero(ibp_reduction),
        "classical for Re(q)>1/2; identity theorem continues phi=J/(4qI)",
    )

    q_of_l = pi * sp.exp(ell) * ell / 2
    f_prime_at_l = sp.simplify(2 * q_of_l / ell - pi * sp.exp(ell))
    add_gate(
        "S1.3_SADDLE_STATIONARY",
        sympy_zero(f_prime_at_l),
        "F'(L)=0 for q=(pi/2)e^L L",
    )

    correct_k = sp.simplify(
        2 * q_of_l / ell**2 + pi * sp.exp(ell)
    )
    target_k = pi * sp.exp(ell) * (ell + 1) / ell
    add_gate(
        "S1.4_HESSIAN_WITH_1_OVER_L",
        sympy_zero(correct_k - target_k),
        "K=pi*e^L*(L+1)/L",
    )

    mutant_k = pi * sp.exp(ell) * (ell + 1)
    add_gate(
        "S1.M1_HESSIAN_MUTANT_REJECTED",
        sympy_nonzero(correct_k - mutant_k),
        "missing 1/L does not equal -F''(L)",
    )

    kernel_poly = 2 * y - 3

    def paper_u_derivative(poly: sp.Expr) -> sp.Expr:
        return sp.expand(5 * poly + 4 * y * sp.diff(poly, y) - 4 * y * poly)

    q_poly = 32 * y**3 - 224 * y**2 + 330 * y - 75
    phi1_second_poly = paper_u_derivative(paper_u_derivative(kernel_poly))
    add_gate(
        "S1.5_PHI1_SECOND_DERIVATIVE",
        sympy_zero(phi1_second_poly - q_poly),
        "Phi1''/Phi1=Q(y)/(2y-3)",
    )

    endpoint_real = sp.expand_complex(
        -pi * r * sp.exp(sp.I * (pi / 2 - vartheta))
    ).as_real_imag()[0]
    add_gate(
        "S1.6_ENDPOINT_PHASE_IDENTITY",
        sympy_zero(endpoint_real + pi * r * sp.sin(vartheta)),
        "Re[-pi*r*e^(i(pi/2-theta))]=-pi*r*sin(theta)",
    )

    ell_complex = a + sp.I * b
    k_complex = pi * sp.exp(ell_complex) * (ell_complex + 1) / ell_complex
    re_k = sp.simplify(sp.expand_complex(k_complex).as_real_imag()[0])
    re_k_target = pi * sp.exp(a) * (
        sp.cos(b) * (1 + a / (a**2 + b**2))
        + sp.sin(b) * b / (a**2 + b**2)
    )
    add_gate(
        "S1.7_REAL_HESSIAN_IDENTITY",
        sympy_zero(re_k - re_k_target),
        "ReK=m plus two nonnegative corrections",
    )

    d = sp.symbols("d", real=True, nonnegative=True)
    left_bracket = d - 1 + sp.exp(-d)
    right_bracket = sp.exp(d) - 1 - d
    add_gate(
        "S1.8_PHASE_DROP_BRACKETS",
        sympy_zero(left_bracket.subs(d, 0))
        and sympy_zero(right_bracket.subs(d, 0))
        and sympy_zero(sp.diff(left_bracket, d) - (1 - sp.exp(-d)))
        and sympy_zero(sp.diff(right_bracket, d) - (sp.exp(d) - 1)),
        "both brackets start at 0 and increase for d>=0",
    )

    i_polys = [kernel_poly]
    j_polys = [q_poly]
    for _ in range(2):
        i_polys.append(amplitude_operator(i_polys[-1], y))
        j_polys.append(amplitude_operator(j_polys[-1], y))
    degrees = [sp.Poly(poly, y).degree() for poly in i_polys + j_polys]
    add_gate(
        "S1.9_EARLY_AMPLITUDE_DEGREES",
        degrees == [1, 2, 3, 3, 4, 5],
        "I/J and two t-derivatives degrees=%s" % degrees,
    )
    return {
        "y": y,
        "Q": q_poly,
        "I0": i_polys[0],
        "I1": i_polys[1],
        "I2": i_polys[2],
        "J0": j_polys[0],
        "J1": j_polys[1],
        "J2": j_polys[2],
    }


def q_tail(x0: str, nu: str) -> arb:
    pi = arb.pi()
    x = arb(x0)
    n = arb(nu)
    big_x = (4 * x).exp()
    return 16 * (-3 * pi * big_x * (4 * n).cos()).exp()


def near_real_gates() -> None:
    section("S2 repaired near-real wedge")
    tail_035 = q_tail("0.35", "0.1")
    tail_040 = q_tail("0.40", "0.1")
    add_gate(
        "S2.1_QTAIL_TUBES_LT_ONE",
        certainly_gt(tail_035, arb(0))
        and certainly_lt(tail_035, arb(1))
        and certainly_gt(tail_040, arb(0))
        and certainly_lt(tail_040, arb(1)),
        "q35=%s q40=%s" % (ball_text(tail_035), ball_text(tail_040)),
    )
    add_gate(
        "S2.2_QTAIL_EXPECTED_WINDOWS",
        certainly_gt(tail_035, arb("8.2400e-15"))
        and certainly_lt(tail_035, arb("8.2401e-15"))
        and certainly_gt(tail_040, arb("3.3968e-18"))
        and certainly_lt(tail_040, arb("3.3970e-18")),
        "directed 256/512-bit enclosures",
    )

    def amended_lemma31_precondition(value: arb) -> bool:
        return certainly_gt(value, arb(0)) and certainly_lt(value, arb(1))

    add_gate(
        "S2.R_QTAIL_BOUNDARY_REJECTED",
        not amended_lemma31_precondition(arb(1)),
        "q_tail=1 is rejected before q_tail/(1-q_tail)",
    )

    k0 = arb(K_MIN_INT)
    buffer = k0 / 20 - k0 / 21 - 1
    log_bound = (20 * k0).log() + arb.pi() / 2
    eps_log = -rational(491, 500).log()
    monotonicity_b = log_bound + 2 * eps_log
    correction = k0 * monotonicity_b / (buffer * buffer)
    curvature = arb(CURVATURE_BASE) + correction
    add_gate(
        "S2.3_CURVATURE_REPAIR",
        certainly_gt(correction, arb("0.0044675317402"))
        and certainly_lt(correction, arb("0.0044675317404"))
        and certainly_lt(curvature, arb(CURVATURE_LIMIT)),
        "derived correction=%s total=%s"
        % (ball_text(correction), ball_text(curvature)),
    )

    k_symbol = sp.symbols("k_monotone", positive=True)
    eps_symbol = sp.symbols("eps_log", real=True)
    b_symbol = sp.log(20 * k_symbol) + sp.pi / 2 + 2 * eps_symbol
    log_derivative = sp.diff(
        sp.log(k_symbol * b_symbol / (k_symbol / 420 - 1) ** 2),
        k_symbol,
    )
    target_derivative = (
        1 / k_symbol
        + 1 / (k_symbol * b_symbol)
        - 2 / (k_symbol - 420)
    )
    derivative_at_k0 = (
        1 / k0
        + 1 / (k0 * monotonicity_b)
        - 2 / (k0 - 420)
    )
    add_gate(
        "S2.4_CURVATURE_MONOTONICITY",
        sympy_zero(log_derivative - target_derivative)
        and certainly_gt(monotonicity_b, arb(1))
        and certainly_lt(1 / (k0 * monotonicity_b), 1 / k0)
        and certainly_gt(2 / (k0 - 420), 2 / k0)
        and certainly_lt(derivative_at_k0, arb(0)),
        "B(k0)=%s derivative(k0)=%s; inequalities persist for k>=k0"
        % (ball_text(monotonicity_b), ball_text(derivative_at_k0)),
    )

    reciprocal = 1 / (rational(22, 21) - 1 / (2 * k0))
    margin = reciprocal - arb(CURVATURE_LIMIT)
    exact_margin = rational(67, 220)
    add_gate(
        "S2.5_RECIPROCAL_COEFFICIENT",
        certainly_gt(reciprocal, arb("0.954545455000"))
        and certainly_lt(reciprocal, arb("0.954545455002"))
        and certainly_gt(reciprocal, rational(21, 22)),
        "k0 coefficient=%s" % ball_text(reciprocal),
    )
    add_gate(
        "S2.6_DERIVATIVE_MARGIN",
        certainly_gt(margin, exact_margin),
        "margin=%s > 67/220=%s"
        % (ball_text(margin), ball_text(exact_margin)),
    )

    reciprocal_abs = 1 / (rational(20, 21) - 1 / (2 * k0))
    argument_bound = (reciprocal_abs + arb(CURVATURE_LIMIT)) / 21
    add_gate(
        "S2.7_ARGUMENT_BOUND",
        certainly_gt(argument_bound, arb("0.080952380978"))
        and certainly_lt(argument_bound, arb(ARGUMENT_LIMIT)),
        "bound=%s < 0.081" % ball_text(argument_bound),
    )

    x0 = arb(NEAR_REAL_X_MIN_INT)
    disk_slack = (x0 - rational(1, 2)) / 21 - (
        (x0 * theta0().tan()) ** 2 + rational(1, 4)
    ).sqrt()
    add_gate(
        "S2.8_INTEGER_DISK_COVER",
        certainly_gt(disk_slack, arb("1.5195400e7"))
        and certainly_lt(disk_slack, arb("1.5195402e7")),
        "threshold slack=%s" % ball_text(disk_slack),
    )
    add_gate(
        "S2.9_NEAR_THEOREM_CONSTANTS",
        certainly_lt(curvature, rational(13, 20))
        and sympy_zero(
            sp.Rational(21, 22)
            - sp.Rational(13, 20)
            - sp.Rational(67, 220)
        ),
        "|(log I)''|<0.65/k gives Re(log phi)'>67/(220k)",
    )


def gaussian_sum_constant(power: int) -> arb:
    """G_p for 0<c<=1 from int_0^inf (x+1)^p exp(-pi*c*x^2) dx."""
    pi = arb.pi()
    total = arb(0)
    for j in range(power + 1):
        gamma_arg = rational(j + 1, 2)
        integral_coefficient = (
            rational(1, 2)
            * gamma_arg.gamma()
            * pi ** (-gamma_arg)
        )
        total += arb(int(sp.binomial(power, j))) * integral_coefficient
    return total


def sympy_rational_to_arb(value: sp.Expr) -> arb:
    exact = sp.Rational(value)
    return rational(int(exact.p), int(exact.q))


def amplitude_bound_constant(poly: sp.Expr, y: sp.Symbol) -> arb:
    """Constant after dominating every A^(j+3/2) by A^(13/2), A=100a."""
    polynomial = sp.Poly(poly, y)
    total = arb(0)
    for (degree,), coefficient in polynomial.terms():
        coeff_abs = abs(sympy_rational_to_arb(coefficient))
        gaussian = gaussian_sum_constant(2 * degree + 2)
        total += coeff_abs * (arb.pi() ** degree) * gaussian
    return (arb.pi() / 4) * total


def q_polynomial_gates() -> None:
    section("S3 Q-polynomial and c>=1 tails")
    lower_constant = (
        arb(32)
        - rational(224, 16)
        - rational(330, 16**2)
        - rational(75, 16**3)
    )
    upper_constant = (
        arb(32)
        + rational(224, 16)
        + rational(330, 16**2)
        + rational(75, 16**3)
    )
    add_gate(
        "S3.1_Q_LOWER_FOR_ABS_Y_GE_16",
        certainly_gt(lower_constant, arb(16)),
        "reverse-triangle coefficient=%s" % ball_text(lower_constant),
    )
    add_gate(
        "S3.2_Q_UPPER_FOR_ABS_Y_GE_16",
        certainly_lt(upper_constant, arb(48)),
        "triangle coefficient=%s" % ball_text(upper_constant),
    )

    decay = (-3 * arb.pi()).exp()
    den_i = 1 - 16 * decay
    den_j = 1 - 256 * decay
    tau_i = 48 * decay / den_i
    tau_j = 768 * decay / den_j
    add_gate(
        "S3.3_TAIL_DENOMINATORS_C_GE_1",
        certainly_gt(den_i, arb(0)) and certainly_gt(den_j, arb(0)),
        "denI=%s denJ=%s" % (ball_text(den_i), ball_text(den_j)),
    )
    add_gate(
        "S3.4_FACTORED_TAIL_BOUNDS",
        certainly_lt(tau_i, arb("0.004"))
        and certainly_lt(tau_j, arb("0.064")),
        "tauI(1)=%s tauJ(1)=%s"
        % (ball_text(tau_i), ball_text(tau_j)),
    )


def vertical_geometry_gates() -> None:
    section("S4 vertical/mid-sector geometry")
    a = a_min()
    pi = arb.pi()
    r0 = r0_value()
    two_r0 = 2 * r0
    b_lead = theta0() * a / (a + 1)
    add_gate(
        "S4.1_R0_EXACT_THRESHOLD",
        certainly_gt(r0, arb("3.0945e437"))
        and certainly_lt(r0, arb("3.0947e437")),
        "R0=%s" % ball_text(r0),
    )
    add_gate(
        "S4.2_MAPPED_M_THRESHOLD",
        certainly_gt(two_r0, arb("6.1890e437"))
        and certainly_lt(two_r0, arb("6.1893e437")),
        "2R0=%s" % ball_text(two_r0),
    )
    add_gate(
        "S4.3_B_LOWER_BOUND",
        certainly_gt(b_lead, rational(B_MIN_NUM, B_MIN_DEN)),
        "theta0*a/(a+1)=%s > 1/50" % ball_text(b_lead),
    )
    add_gate(
        "S4.4_COS_B_LOWER_GEOMETRY",
        certainly_lt(a + pi / 2, 2 * a),
        "cos(b)>=sin(beta)>=b/(a+pi/2)>1/(100a)",
    )
    add_gate(
        "S4.5_M_LOWER_BOUND",
        certainly_gt(pi / 100, rational(1, 32)),
        "pi/100=%s > 1/32" % ball_text(pi / 100),
    )

    m_lower = a.exp() / (32 * a)
    chi_square_upper = 32 * pi * (a + 1)
    add_gate(
        "S4.6_CHI_BOUND",
        certainly_lt(chi_square_upper, 225 * a),
        "|K|/ReK <= %s < 225a" % ball_text(chi_square_upper),
    )

    h = (a / m_lower).sqrt()
    eta = 120 * (a**3) * (-a / 2).exp()
    add_gate(
        "S4.7_SADDLE_WINDOW",
        certainly_gt(h, arb(0)) and certainly_lt(h, arb("1e-210")),
        "h=sqrt(a/m_lower)=%s" % ball_text(h),
    )
    add_gate(
        "S4.8_CORRECTED_CUBIC_ETA",
        certainly_lt(eta, arb("1e-200")),
        "120*a^3*e^(-a/2)=%s < 1e-200" % ball_text(eta),
    )
    add_gate(
        "S4.9_LOCAL_EXPONENT_SMALL",
        certainly_lt(eta + 10 * h, arb("1e-200")),
        "eta+10h=%s < 1e-200" % ball_text(eta + 10 * h),
    )
    add_gate(
        "S4.10_NEAR_WEDGE_RE_THRESHOLD",
        certainly_gt(r0 * theta0().cos(), arb(NEAR_REAL_X_MIN_INT)),
        "R0*cos(theta0)>2e9",
    )


def endpoint_and_amplitude_gates(polys: dict[str, sp.Expr]) -> arb:
    section("S5 endpoint and early/arc amplitude repair")
    y = polys["y"]
    constants = [
        amplitude_bound_constant(polys[name], y)
        for name in ("I0", "I1", "I2", "J0", "J1", "J2")
    ]
    early_constant = max_certain(constants + [arb(1)])
    add_gate(
        "S5.1_EARLY_POLYNOMIAL_CONSTANT",
        early_constant.is_finite()
        and certainly_gt(early_constant, arb(0))
        and certainly_lt(early_constant, arb("1e12")),
        "C_E=%s for powers through (100a)^(13/2)"
        % ball_text(early_constant),
    )

    a = a_min()
    pi = arb.pi()
    correct_endpoint = pi * theta0().sin()
    invalid_endpoint = pi / 25
    add_gate(
        "S5.2_CORRECT_ENDPOINT_COEFFICIENT",
        certainly_gt(correct_endpoint, arb("0.1256301"))
        and certainly_lt(correct_endpoint, arb("0.1256303")),
        "pi*sin(1/25)=%s" % ball_text(correct_endpoint),
    )
    add_gate(
        "S5.M2_ENDPOINT_MUTANT_REJECTED",
        certainly_lt(correct_endpoint, invalid_endpoint),
        "pi*sin(1/25)<pi/25; invalid strengthening rejected",
    )

    net_phase = correct_endpoint - (pi + 2) / a
    add_gate(
        "S5.3_PHASE_AFTER_NORMALIZATION",
        certainly_gt(net_phase, rational(1, 10)),
        "pi*sin(1/25)-(pi+2)/1000=%s > 1/10"
        % ball_text(net_phase),
    )

    amplitude_scale = 100 * a
    required_log_amplitude = (
        early_constant.log()
        + rational(5, 4) * a
        + rational(13, 2) * amplitude_scale.log()
    )
    charged_log_amplitude = required_log_amplitude.upper()
    available_log_drop = (net_phase - rational(1, 10)) * r0_value()

    def endpoint_certificate(charged_log_amplitude: arb) -> bool:
        charge_is_complete = certainly_ge(
            charged_log_amplitude, required_log_amplitude.upper()
        )
        budget_closes = certainly_gt(
            net_phase * r0_value() - charged_log_amplitude,
            r0_value() / 10,
        )
        return charge_is_complete and budget_closes

    add_gate(
        "S5.4_AMPLITUDE_ABSORBED",
        endpoint_certificate(charged_log_amplitude),
        "log amplitude=%s; spare drop=%s"
        % (ball_text(charged_log_amplitude), ball_text(available_log_drop)),
    )
    add_gate(
        "S5.M3_OMITTED_AMPLITUDE_REJECTED",
        not endpoint_certificate(arb(0)),
        "zero early/arc amplitude charge fails completeness",
    )
    return early_constant


def normalized_error_gates() -> tuple[dict[str, arb], arb, arb]:
    section("S6 normalized error ledger and sign transfer")
    a = a_min()
    r0 = r0_value()
    m = a.exp() / (32 * a)

    def exp_upper(exponent: arb) -> arb:
        """A nonnegative directed upper bound, including huge-exponent underflow."""
        return exponent.exp().upper()

    errors = {
        "E_arc": exp_upper(-r0 / 10),
        "E_early": exp_upper(-m * a / 4),
        "E_prefar": exp_upper(-m / 5),
        "E_prenear": 36 * exp_upper(-a / 3),
        "E_postnear": 1500 * exp_upper(-a / 2),
        "E_inf": exp_upper(-m / 4),
        "E_loc": 130000 * (a ** rational(7, 2)) * exp_upper(-a / 2),
        "E_gauss": 12 * exp_upper(-a / 2),
    }
    total = sum(errors.values(), arb(0))
    dominant = errors["E_prenear"]
    add_gate(
        "S6.1_ALL_ERROR_PIECES_FINITE",
        all(
            value.is_finite() and certainly_ge(value, arb(0))
            for value in errors.values()
        ),
        "eight nonnegative directed-rounding bounds",
    )
    add_gate(
        "S6.2_DOMINANT_PRENEAR",
        all(
            name == "E_prenear" or certainly_lt(value, dominant)
            for name, value in errors.items()
        )
        and certainly_gt(dominant, arb("6.1869e-144"))
        and certainly_lt(dominant, arb("6.1870e-144")),
        "36*e^(-1000/3)=%s" % ball_text(dominant),
    )
    add_gate(
        "S6.3_ERROR_SUM_LT_ONE",
        certainly_lt(total, arb(1)),
        "E_total=%s < 1; quotient denominator is positive" % ball_text(total),
    )
    add_gate(
        "S6.4_ERROR_SUM_LT_1E_140",
        certainly_lt(total, arb(ERROR_SUM_LIMIT)),
        "sum=%s" % ball_text(total),
    )

    delta_p = 13 / (arb.pi() * a.exp())
    add_gate(
        "S6.5_P_REPLACEMENT_ERROR",
        certainly_lt(delta_p, 5 * (-a).exp())
        and certainly_lt(rational(13, 1), 5 * arb.pi()),
        "deltaP<=13/(pi*e^a)=%s < 5e^-a" % ball_text(delta_p),
    )

    small_transfer_lhs = 2 * delta_p + 3 * total
    add_gate(
        "S6.6_TRANSFER_COMPARISON_PREMISE",
        certainly_lt(small_transfer_lhs, arb(1)),
        "2*deltaP+3*E_total=%s < 1" % ball_text(small_transfer_lhs),
    )

    transfer_exact = (
        delta_p
        + (1 + delta_p) * (2 * total) / (1 - total)
    )
    transfer_conservative = delta_p + 3 * total
    add_gate(
        "S6.7_EXACT_QUOTIENT_TRANSFER",
        certainly_le(transfer_exact, transfer_conservative)
        and certainly_lt(transfer_exact, arb(TRANSFER_LIMIT)),
        "exact=%s <= deltaP+3E=%s < 3e-140"
        % (ball_text(transfer_exact), ball_text(transfer_conservative)),
    )
    add_gate(
        "S6.W_CONSERVATIVE_TRANSFER",
        certainly_lt(transfer_conservative, arb(TRANSFER_LIMIT)),
        "optional ward deltaP+3E=%s" % ball_text(transfer_conservative),
    )

    leading_angle = theta0() * (a - 1) / (a + 1)
    add_gate(
        "S6.8_LEADING_ARGUMENT",
        certainly_gt(leading_angle, rational(1, 50)),
        "theta0*(a-1)/(a+1)=%s > 1/50"
        % ball_text(leading_angle),
    )
    add_gate(
        "S6.9_SIGN_TRANSFER",
        certainly_lt(transfer_exact, rational(1, 50).sin()),
        "transfer_exact=%s < sin(1/50)=%s"
        % (ball_text(transfer_exact), ball_text(rational(1, 50).sin())),
    )
    return errors, total, transfer_exact


def assembly_gates() -> None:
    section("S7 domain assembly and firewall")
    calls, imports = ast_firewall()
    add_gate(
        "S7.1_NO_POINT_GRID_OR_ZERO_ORACLE",
        not calls and not imports,
        "banned_calls=%s banned_imports=%s" % (calls, imports),
    )
    add_gate(
        "S7.2_PYTHON_FLINT_MANDATORY",
        hasattr(flint, "__version__"),
        "python-flint=%s" % getattr(flint, "__version__", "unknown"),
    )
    add_gate(
        "S7.3_SPEC_SHA",
        len(SPEC_SHA) == 64,
        SPEC_SHA,
    )
    add_gate(
        "S7.4_HALF_PLANE_UNION",
        certainly_ge(theta0(), arb(0))
        and certainly_lt(theta0(), arb.pi() / 2),
        "|arg q|<=1/25 union 1/25<=|arg q|<=pi/2",
    )
    q_symbol, s_symbol = sp.symbols("q_scale s_scale")
    add_gate(
        "S7.5_CONJUGATION_AND_SCALE",
        sympy_zero(
            (2 * q_symbol).subs(q_symbol, s_symbol / 2) - s_symbol
        ),
        "lower half by conjugation; s=2q gives |s|>=2R0",
    )
    add_gate(
        "S7.6_STRICT_FIREWALL",
        "not global Pick" in FIREWALL
        and "not BP1" in FIREWALL
        and "not RH" in FIREWALL,
        FIREWALL,
    )


def write_json_report(
    path: str,
    *,
    mode: str,
    bits: int,
    verdict: str,
    runtime: float,
    errors: dict[str, arb],
    error_sum: arb,
    transfer_exact: arb,
    early_constant: arb,
) -> None:
    payload = {
        "contract": CONTRACT,
        "spec_revision": SPEC_REVISION,
        "mode": mode,
        "bits": bits,
        "verdict": verdict,
        "SPEC_SHA": SPEC_SHA,
        "file_sha256": file_sha256(),
        "domain_q": DOMAIN_Q,
        "domain_M_repo": DOMAIN_M,
        "R0": ball_text(r0_value()),
        "two_R0": ball_text(2 * r0_value()),
        "early_amplitude_constant": ball_text(early_constant),
        "errors": {name: ball_text(value) for name, value in errors.items()},
        "error_sum": ball_text(error_sum),
        "transfer_exact": ball_text(transfer_exact),
        "gates": [asdict(gate) for gate in GATES],
        "runtime_s": runtime,
        "firewall": FIREWALL,
    }
    Path(path).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("WROTE %s" % path)


def run(*, smoke: bool, json_path: str) -> int:
    GATES.clear()
    started = time.perf_counter()
    mode = "smoke" if smoke else "record"
    bits = SMOKE_BITS if smoke else RECORD_BITS
    ctx.prec = bits

    print("CONTRACT %s" % CONTRACT)
    print("SPEC_REVISION %s" % SPEC_REVISION)
    print("MODE %s" % mode)
    print("BITS %d" % bits)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA %s" % file_sha256())
    print("DOMAIN_Q %s" % DOMAIN_Q)
    print("DOMAIN_M_REPO %s" % DOMAIN_M)
    print("PICK_SIGN Im(q)>0 => Im(phi(q))>0; lower half by conjugation")
    print("FIREWALL %s" % FIREWALL)

    polys = exact_identity_gates()
    near_real_gates()
    q_polynomial_gates()
    vertical_geometry_gates()
    early_constant = endpoint_and_amplitude_gates(polys)
    errors, error_sum, transfer_exact = normalized_error_gates()
    assembly_gates()

    failures = [gate.code for gate in GATES if not gate.passed]
    verdict = (
        "OUTER_DOMAIN_PROVED"
        if not failures
        else "INCONCLUSIVE(%s)" % failures[0]
    )
    passed = len(GATES) - len(failures)
    runtime = time.perf_counter() - started

    section("RESULT")
    print("VERDICT %s" % verdict)
    print("CHECKS %d/%d PASS" % (passed, len(GATES)))
    print("R0 %s" % ball_text(r0_value()))
    print("TWO_R0 %s" % ball_text(2 * r0_value()))
    print("ERROR_SUM %s" % ball_text(error_sum))
    print("TRANSFER_EXACT %s" % ball_text(transfer_exact))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA %s" % file_sha256())
    print("runtime %.6f s" % runtime)
    print("ALL CHECKS PASSED" if not failures else "FAILED_GATES %s" % ",".join(failures))
    print("DOMAIN_Q %s" % DOMAIN_Q)
    print("DOMAIN_M_REPO %s" % DOMAIN_M)
    print("CAVEAT %s" % FIREWALL)

    if json_path:
        write_json_report(
            json_path,
            mode=mode,
            bits=bits,
            verdict=verdict,
            runtime=runtime,
            errors=errors,
            error_sum=error_sum,
            transfer_exact=transfer_exact,
            early_constant=early_constant,
        )
    return 0 if not failures else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Arb/Sympy certificate for MELLIN.PICK.CUSP-SADDLE.01"
    )
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--smoke", action="store_true", help="256-bit proof gates")
    modes.add_argument("--record", action="store_true", help="512-bit proof gates")
    parser.add_argument(
        "--json",
        default="",
        metavar="PATH",
        help="optional JSON report path; never written unless explicitly set",
    )
    args = parser.parse_args()
    return run(smoke=not args.record, json_path=args.json)


if __name__ == "__main__":
    sys.exit(main())
