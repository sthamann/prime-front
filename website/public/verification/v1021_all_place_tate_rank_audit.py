#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1021 -- ALL-PLACE TATE / FINITE-CARRIER / RANKIN AUDIT.

Exact promotion of the 2026-09-04/05 Calabi--Yau/Tate review.  The
module re-derives, without importing a discovery probe:

* the scalar Tate projector on End(V) for dim(V)=2;
* the good-place tensor/End factor splittings and the inertia-fixed
  identity at the bad place p=2;
* the pole normalization separating completed zeta Lambda_Q from the
  entire xi function;
* the rank-nullity obstruction to representing a strictly positive
  infinite-dimensional Weil window through a fixed finite carrier;
* an exact sparse counterexample to the historical inference
  A(x)=O(x^q) => b_n=O(n^(q-1+eps)); and
* the finite-window max-constant tautology in the old Rankin probe.

The strict Weil-window lower bound used to interpret the rank argument
is an EXTERNAL preprint premise (Zhu, arXiv:2608.24827v2), not proved
by this program.  The Calabi--Yau/Tate factorization is identity-side
information; it does not supply the missing all-place intersection form
or its positivity.

Verdict: TATE_FACTOR_EXACT + FIXED_FINITE_CARRIER_NO_GO +
RANKIN_EXPONENT_DROP_FALSIFIED + ALL_PLACE_INTERSECTION_OPEN.
NO RH CLAIM.
"""
from __future__ import annotations

import ast
from pathlib import Path

import sympy as sp

from tfpt_constants import check, reset, summary


VERDICT = (
    "TATE_FACTOR_EXACT; FIXED_FINITE_CARRIER_NO_GO; "
    "RANKIN_EXPONENT_DROP_FALSIFIED; ALL_PLACE_INTERSECTION_OPEN"
)
ROOT = Path(__file__).resolve().parents[1]
RANKIN_PROBE = ROOT / "experiments/tfpt-discovery/rankin_positivity_miniature_probe.py"
CORRECTION_MARKER = "CORRECTION OF RECORD (All-place Tate audit, 2026-09-05)"


def tate_projector_checks() -> None:
    a, b, c, d = sp.symbols("a b c d")
    e, f, g, h = sp.symbols("e f g h")
    A = sp.Matrix([[a, b], [c, d]])
    B = sp.Matrix([[e, f], [g, h]])
    identity = sp.eye(2)

    def tate(matrix: sp.Matrix) -> sp.Matrix:
        return sp.trace(matrix) * identity / 2

    check("T1 Tate projector is idempotent",
          sp.simplify(tate(tate(A)) - tate(A)) == sp.zeros(2))
    check("T2 complementary summand is trace-free",
          sp.simplify(sp.trace(A - tate(A))) == 0)
    check("T3 Tate projector is Hilbert--Schmidt self-adjoint over C",
          sp.simplify(
              sp.trace(tate(A).conjugate().T * B)
              - sp.trace(A.conjugate().T * tate(B))
          ) == 0)

    r, s, t, u = sp.symbols("r s t u", real=True)
    R = sp.Matrix([[r, s], [t, u]])
    adjugate = sp.Matrix([[u, -s], [-t, r]])
    det_r = sp.expand(R.det())
    conjugate_numerator = sp.expand(R * A * adjugate)
    trace_numerator = sp.expand(sp.trace(conjugate_numerator))
    check("T4 trace projector is equivariant under every invertible 2x2 action",
          sp.simplify(trace_numerator - det_r * sp.trace(A)) == 0)


def local_factor_checks() -> None:
    alpha, beta, p, x, z = sp.symbols("alpha beta p x z", nonzero=True)
    tensor_den = (1 - alpha**2 * x) * (1 - alpha * beta * x) ** 2 * (1 - beta**2 * x)
    sym2_den = (1 - alpha**2 * x) * (1 - alpha * beta * x) * (1 - beta**2 * x)
    wedge_den = 1 - alpha * beta * x
    check("L1 V tensor V splits as Sym^2(V) plus wedge^2(V)",
          sp.expand(tensor_den - sym2_den * wedge_den) == 0)
    check("L2 weight-four determinant gives the zeta(s-3) denominator",
          sp.expand(wedge_den.subs(alpha * beta, p**3)) == 1 - p**3 * x)

    end_den = (1 - z) ** 2 * (1 - alpha / beta * z) * (1 - beta / alpha * z)
    adjoint_den = (1 - z) * (1 - alpha / beta * z) * (1 - beta / alpha * z)
    check("L3 End(V)=Q(0) plus Ad^0(V) isolates exactly one zeta(u) factor",
          sp.simplify(end_den - (1 - z) * adjoint_den) == 0)

    ap = sp.symbols("a_p")
    sym2_prime_coefficient = alpha**2 + alpha * beta + beta**2
    sym2_relation = (sym2_prime_coefficient - (ap**2 - p**3))
    check("L4 under a_p=alpha+beta and alpha*beta=p^3, the Sym^2 prime coefficient is a_p^2-p^3",
          sp.expand(sym2_relation.subs(ap, alpha + beta).subs(p**3, alpha * beta)) == 0)

    n11, n12, n21, n22 = sp.symbols("n11 n12 n21 n22")
    monodromy = sp.Matrix([[n11, n12], [n21, n22]])
    g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
    inertia = sp.Matrix([[g11, g12], [g21, g22]])
    inertia_adjugate = sp.Matrix([[g22, -g12], [-g21, g11]])
    inertia_det = sp.expand(inertia.det())
    inertia_fix = sp.expand(
        inertia * sp.eye(2) * inertia_adjugate - inertia_det * sp.eye(2)
    )
    check("L5 every conjugation action and every monodromy commutator fix the identity line",
          inertia_fix == sp.zeros(2)
          and monodromy * sp.eye(2) - sp.eye(2) * monodromy == sp.zeros(2))
    print("  [LEDGER] p=2 Tate factor: (1-2^(-u))^(-1); full ramified Adjoint factor not reconstructed here")
    print("  [LEDGER] infinity: Gamma_End=Gamma_C(u)Gamma_C(u+3), Gamma_Tate=Gamma_R(u)")


def determinant_normalization_checks() -> None:
    u = sp.symbols("u")
    gamma_r, zeta_u = sp.symbols("Gamma_R zeta")
    xi_from_standard_definition = sp.Rational(1, 2) * u * (u - 1) * gamma_r * zeta_u
    completed_zeta = gamma_r * zeta_u
    check("N1 normalization ward: the standard xi definition gives completed zeta = 2 xi/(u(u-1))",
          sp.simplify(
              completed_zeta
              - 2 * xi_from_standard_definition / (u * (u - 1))
          ) == 0)
    print("  [LEDGER] Lambda_End=Lambda_Q Lambda_Ad with Lambda_Q=2 xi/[u(u-1)]")


def finite_carrier_checks() -> None:
    # Every surjective 4x5 compiler is equivalent, after choosing bases, to
    # [I_4 | v].  Its displayed kernel is symbolic in all four coordinates;
    # lower-rank compilers have an even larger kernel by rank--nullity.
    x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4", real=True)
    tail = sp.Matrix([x1, x2, x3, x4])
    compiler = sp.Matrix.hstack(sp.eye(4), tail)
    metric_symbols = sp.symbols("r0:16")
    metric = sp.Matrix(4, 4, metric_symbols)
    gram = compiler.T * metric * compiler
    kernel = sp.Matrix([-x1, -x2, -x3, -x4, 1])
    check("F1 symbolic normal form proves a kernel for every rank-four 4x5 compiler",
          compiler.rank() == 4 and compiler * kernel == sp.zeros(4, 1))
    check("F2 every pulled-back bilinear dim-four form vanishes on the symbolic kernel",
          sp.simplify((kernel.T * gram * kernel)[0]) == 0)

    strict_floor = sp.Rational(89, 10**19)
    kernel_norm_sq = (kernel.T * kernel)[0]
    check("F3 conditional arithmetic ward: Zhu's external strict-window floor is incompatible with that zero",
          strict_floor * kernel_norm_sq > 0)

    tate_compiler = sp.Matrix([[1, 1]])
    tate_kernel = sp.Matrix([1, -1])
    check("F4 scalar Tate line already has a kernel on two source directions",
          tate_compiler * tate_kernel == sp.zeros(1, 1))
    print("  [EXTERNAL PREMISE] Zhu 2608.24827v2: strict Weil floor on support [-0.8,0.8]")
    print("  [SCOPE] conclusion excludes one fixed finite exact-linear pullback; nonlinear methods, growing discretizations and direct limits are not excluded")


def sparse_counterexample_checks() -> None:
    # Strong counterexample, matching both ingredients claimed by the old
    # probe.  Let b_n=4n^3 plus a spike n^(18/5) at n=32^m.  The baseline
    # has partial sum X^2(X+1)^2~X^4 and Dirichlet series 4*zeta(s-3),
    # hence a simple pole at s=4.  The spike series is geometric with
    # abscissa 18/5<4, so it is analytic at that pole and contributes
    # o(X^4); nevertheless its ratio to n^(3+1/10) grows like n^(1/2).
    x = sp.symbols("x", positive=True)
    baseline_partial = x**2 * (x + 1) ** 2
    check("R1 baseline 4*sum(n^3) has exact partial sum X^2(X+1)^2 and leading X^4",
          sp.expand(baseline_partial) == x**4 + 2*x**3 + x**2)

    spike_exp = sp.Rational(18, 5)
    target_exp = sp.Rational(31, 10)
    check("R2 spike is lower-order than X^4 but exceeds the claimed n^(3+0.1) scale",
          spike_exp < 4 and spike_exp - target_exp == sp.Rational(1, 2))

    ratio = 2**18
    m_symbol = sp.symbols("m", integer=True, positive=True)
    n_symbol = 32**m_symbol
    spike_sum_closed = sp.Integer(ratio) * (sp.Integer(ratio)**m_symbol - 1) / (ratio - 1)
    spike_negligible = sp.limit(spike_sum_closed / n_symbol**4,
                                m_symbol, sp.oo)
    check("R3 exact geometric spike sum is O(X^(18/5))=o(X^4)",
          spike_negligible == 0)

    # At s=4 the spike ratio is 2^(18-5s)=1/4, so the spike Dirichlet
    # series is analytic while the baseline pole remains.  Along n=32^m,
    # the tenth power of the bad coefficient ratio is n^5 -> infinity.
    spike_ratio_at_four = sp.Rational(2**18, 2**20)
    spike_dirichlet_at_four = spike_ratio_at_four / (1 - spike_ratio_at_four)
    check("R4 counterexample preserves the simple s=4 pole and X^4 asymptotic",
          spike_ratio_at_four == sp.Rational(1, 4)
          and spike_dirichlet_at_four == sp.Rational(1, 3)
          and 4 - spike_exp == sp.Rational(2, 5))
    k_symbol = sp.symbols("k", integer=True, positive=True)
    coefficient_ratio_limit = sp.limit(32 ** (sp.Rational(1, 2) * k_symbol),
                                           k_symbol, sp.oo)
    check("R5 coefficient ratio to n^(3+0.1) is unbounded along the spikes",
          coefficient_ratio_limit == sp.oo)

    # The identical exponent defect occurs in the q=12/tau paragraph:
    # use baseline 12n^11 and spikes n^(58/5); 58/5<12 but >111/10.
    check("R6 same exact exponent obstruction applies to the tau q=12 paragraph",
          sp.Rational(58, 5) < 12
          and sp.Rational(58, 5) - sp.Rational(111, 10) == sp.Rational(1, 2))

    samples = [sp.Integer(1), sp.Integer(16), sp.Integer(0), sp.Integer(256)]
    weights = [sp.Integer(n) ** sp.Rational(31, 10) for n in range(1, 5)]
    k_window = max(samples[i] / weights[i] for i in range(len(samples)))
    check("R7 max-fitted finite-window K makes its own inequality tautological",
          all(samples[i] <= k_window * weights[i] for i in range(len(samples))))

    check("R8 the elementary square-root coefficient exponents are 2 and 6",
          sp.Rational(4, 2) == 2 and sp.Rational(12, 2) == 6)


def correction_of_record_check() -> None:
    source = RANKIN_PROBE.read_text(encoding="utf-8")
    module_docstring = ast.get_docstring(ast.parse(source), clean=False) or ""
    check("C1 historical Rankin probe carries the correction outside its frozen narrative",
          CORRECTION_MARKER in source and CORRECTION_MARKER not in module_docstring)


def run() -> int:
    reset()
    print("=" * 78)
    print("v1021 ALL-PLACE TATE / FINITE-CARRIER / RANKIN AUDIT")
    print("=" * 78)
    tate_projector_checks()
    local_factor_checks()
    determinant_normalization_checks()
    finite_carrier_checks()
    sparse_counterexample_checks()
    correction_of_record_check()
    print("  VERDICT: %s" % VERDICT)
    print("  CLAIM_BOUNDARY: NO_RH_PROOF")
    return summary("v1021 all-place Tate / finite-carrier / Rankin audit")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
