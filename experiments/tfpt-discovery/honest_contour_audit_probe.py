#!/usr/bin/env python3
"""EXPERIMENT-ONLY / NO RH CLAIM / NO LOAD-BEARING STATUS.

External numerical audit of RH/ExternalBridges.lean r534:

  * FullWeilTest, lines 75-89: even continuous compactly supported
    autocorrelations of compactly supported Lipschitz L2 witnesses.
  * FullWeilTest.hat, lines 2699-2700: unshifted bilateral Laplace transform
        hat_g(s) = integral_R g(u) exp(s u) du.
  * standardExplicitFormula, lines 14028-14030:
        Re(sum_{zeta(rho)=0, 0<=Re rho<=1} m_rho hat_g(rho) - hat_g(1)).
    The subtype contains every critical-strip zero, both signs of Im rho, with
    riemannZetaMultiplicity (lines 2660-2673, 13392-13409).
  * primeEval, lines 14225-14226: sum Lambda(n) g(log n).
  * rightVerticalIntegral_eq_prime_sum, lines 14540-14544: the ACTUAL right
    contour edge Re(s)=2 gives -2 pi primeEval.  Re(s)=17/16 is not a contour
    boundary; it is 1-(-1/16), used by the reflected left-edge Dirichlet
    series (lines 14770-14780).  This probe also checks Re(s)=17/16 because
    the same Fourier-inversion identity holds for every sigma>1.
  * logDeriv_zetaFEFactor_left_edge, lines 14757-14763:
        chi'/chi(s) = -log(2 pi) + digamma(s) - (pi/2) tan(pi s/2).
  * leftEdgeArchIntegral, lines 15295-15299: integral (chi'/chi)(s) hat_g(s).
  * leftVerticalIntegral_eq_reflected_prime_sub_arch, lines 15322-15329:
        left edge = 2 pi sum Lambda(n)n^-1 g(-log n) - arch.
  * contourExplicitFormula_honest[_complex], lines 15396-15441:
        2 pi (sum m_rho hat_g(rho) - hat_g(1))
          = arch - 2 pi sum Lambda(n)(1+n^-1)g(log n).
  * combMass, RH/Elementwise.lean lines 798-809, and fullWeilForm,
    ExternalBridges.lean lines 953-999:
        combMass(n)=2 Lambda(n)/sqrt(n);
        fullWeilForm=fullWeilArchSide-fullWeilCombSide+fullWeilPoleSide.

Tests use the admissible Lipschitz witness
    h_a(t)=max(1-|t|/a,0),  R=2a,
and its autocorrelation g_a=h_a star h_a~.  Its exact transforms are
    H_a(s)=2(cosh(a s)-1)/(a s^2),  hat_g(s)=H_a(s)H_a(-s).
This O(|Im s|^-4) family makes numerical contour tails controllable.

Tail budgets are explicit numerical envelopes, not formal bounds on zeta:
the right edge uses |zeta'/zeta(sigma+it)| <= -zeta'/zeta(sigma) and the
closed-form |hat_g| envelope.  Left/arch tails use the same transform
envelope times a tenfold sampled bound on logarithmic growth over [T,2T].
The zero tail uses the standard N(T)~T log(T/2pi)/(2pi) density envelope
with a tenfold safety factor.  Reported errors must fit quadrature plus tail
budgets.  mpmath.zetazero enumerates known critical-line zeros only; it
cannot certify that Lean's all-critical-strip subtype contains no additional
off-line zeros.  That unavoidable RH-independent limitation is printed.

Dictionary audited:
    Lambda(n)(1+n^-1)g(log n)
      = 2 Lambda(n)n^-1/2 [g(log n) cosh(log n/2)].
Thus g_tilde(u)=g(u)cosh(u/2) resolves the coefficient convention pointwise.
But multiplication by cosh(u/2) does not preserve the autocorrelation class:
its Fourier transform is Re(hat_g(1/2+i xi)), which is negative for the
triangle autocorrelations used here.  Therefore this is not a universal
same-domain dictionary lemma.

Verdict enum:
  AUDIT_CLEAN(max_rel_err=...)
  DEFINITION_BUG(which=..., evidence=...)
  DICTIONARY_RESOLVES(map=...)
or '+'-joined combinations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import mpmath as mp
from scipy.integrate import quad


SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
RIGHT_REQUESTED = mp.mpf(17) / 16
RIGHT_ACTUAL = mp.mpf(2)
LEFT_EDGE = -mp.mpf(1) / 16
TAIL_SAFETY = mp.mpf(10)


@dataclass(frozen=True)
class TestFunction:
    name: str
    radius: mp.mpf

    @property
    def a(self) -> mp.mpf:
        return self.radius / 2

    def h_transform(self, s: mp.mpc) -> mp.mpc:
        if abs(s) < mp.mpf("1e-18"):
            return self.a
        return 2 * (mp.cosh(self.a * s) - 1) / (self.a * s * s)

    def hat(self, s: mp.mpc) -> mp.mpc:
        return self.h_transform(s) * self.h_transform(-s)

    def g(self, u: mp.mpf) -> mp.mpf:
        x = abs(u)
        a = self.a
        if x > 2 * a:
            return mp.mpf(0)
        if x <= a:
            return 2 * a / 3 - x * x / a + x**3 / (2 * a * a)
        return (2 * a - x) ** 3 / (6 * a * a)

    def hat_envelope_coefficient(self, sigma: mp.mpf) -> mp.mpf:
        # |H(+-sigma+it)| <= 2(cosh(a sigma)+1)/(a |s|^2).
        return (2 * (mp.cosh(self.a * abs(sigma)) + 1) / self.a) ** 2


def von_mangoldt(n: int) -> mp.mpf:
    if n < 2:
        return mp.mpf(0)
    for p in range(2, n + 1):
        if any(p % q == 0 for q in range(2, int(math.sqrt(p)) + 1)):
            continue
        power = p
        while power < n:
            power *= p
        if power == n:
            return mp.log(p)
    return mp.mpf(0)


def prime_sums(test: TestFunction) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    bare = mp.mpf(0)
    reflected = mp.mpf(0)
    corpus = mp.mpf(0)
    for n in range(2, int(mp.floor(mp.e ** test.radius)) + 1):
        lam = von_mangoldt(n)
        value = test.g(mp.log(n))
        bare += lam * value
        reflected += lam * value / n
        corpus += 2 * lam * value / mp.sqrt(n)
    return bare, reflected, corpus


def log_deriv_zeta(s: mp.mpc) -> mp.mpc:
    return mp.zeta(s, derivative=1) / mp.zeta(s)


def chi_log_deriv(s: mp.mpc) -> mp.mpc:
    return -mp.log(2 * mp.pi) + mp.digamma(s) - (mp.pi / 2) * mp.tan(mp.pi * s / 2)


def symmetric_real_integral(
    integrand: Callable[[mp.mpf], mp.mpc],
    cutoff: float,
    eps: float,
) -> tuple[mp.mpf, mp.mpf]:
    # f(-t)=conj(f(t)); the full integral is real.
    points = [float(x) for x in range(4, int(cutoff), 4)]

    def real_integrand(t: float) -> float:
        return float(mp.re(integrand(mp.mpf(t))))

    value, error = quad(
        real_integrand,
        0.0,
        cutoff,
        epsabs=eps,
        epsrel=eps,
        limit=1200,
        points=points,
    )
    return 2 * mp.mpf(value), 2 * mp.mpf(error)


def right_tail_budget(test: TestFunction, sigma: mp.mpf, cutoff: mp.mpf) -> mp.mpf:
    coefficient = test.hat_envelope_coefficient(sigma)
    log_deriv_bound = -mp.re(log_deriv_zeta(mp.mpc(sigma, 0)))
    return 2 * log_deriv_bound * coefficient / (3 * cutoff**3)


def sampled_log_growth_bound(
    factor: Callable[[mp.mpc], mp.mpc],
    sigma: mp.mpf,
    cutoff: mp.mpf,
) -> mp.mpf:
    samples = []
    for k in range(17):
        t = cutoff * (1 + mp.mpf(k) / 16)
        samples.append(abs(factor(mp.mpc(sigma, t))) / (mp.log(t + 2) + 1))
    return TAIL_SAFETY * max(samples)


def logarithmic_tail_budget(
    test: TestFunction,
    factor: Callable[[mp.mpc], mp.mpc],
    sigma: mp.mpf,
    cutoff: mp.mpf,
) -> mp.mpf:
    coefficient = test.hat_envelope_coefficient(sigma)
    growth = sampled_log_growth_bound(factor, sigma, cutoff)
    log_integral_envelope = (mp.log(cutoff + 2) + 2) / (3 * cutoff**3)
    return 2 * coefficient * growth * log_integral_envelope


def known_zero_sum(test: TestFunction, positive_zero_count: int) -> tuple[mp.mpf, mp.mpf]:
    total = mp.mpc(0)
    last_height = mp.mpf(0)
    for index in range(1, positive_zero_count + 1):
        zero = mp.zetazero(index)
        last_height = mp.im(zero)
        # Lean's rectangle/subtype includes rho and conjugate(rho), once each
        # for a simple zero.  Known computed zeros are simple.
        total += test.hat(zero) + test.hat(mp.conj(zero))
    return mp.re(total), last_height


def zero_tail_budget(test: TestFunction, height: mp.mpf) -> mp.mpf:
    coefficient = test.hat_envelope_coefficient(mp.mpf("0.5"))
    density = (mp.log(max(height / (2 * mp.pi), mp.mpf(1))) + 2) / (2 * mp.pi)
    return TAIL_SAFETY * 2 * coefficient * density / (3 * height**3)


def relative_error(lhs: mp.mpf, rhs: mp.mpf) -> mp.mpf:
    return abs(lhs - rhs) / max(abs(lhs), abs(rhs), mp.mpf("1e-40"))


def row(
    rows: list[dict[str, str]],
    identity: str,
    lhs: mp.mpf,
    rhs: mp.mpf,
    budget_abs: mp.mpf,
) -> bool:
    rel = relative_error(lhs, rhs)
    scale = max(abs(lhs), abs(rhs), mp.mpf("1e-40"))
    budget_rel = budget_abs / scale
    rows.append(
        {
            "identity": identity,
            "lhs": mp.nstr(lhs, 15),
            "rhs": mp.nstr(rhs, 15),
            "rel_err": mp.nstr(rel, 8),
            "budget": mp.nstr(budget_rel, 8),
        }
    )
    return abs(lhs - rhs) <= budget_abs


def dictionary_audit(test: TestFunction) -> dict[str, str | bool]:
    bare, reflected, corpus = prime_sums(test)
    honest = bare + reflected
    mapped = mp.mpf(0)
    for n in range(2, int(mp.floor(mp.e ** test.radius)) + 1):
        lam = von_mangoldt(n)
        u = mp.log(n)
        mapped += 2 * lam / mp.sqrt(n) * test.g(u) * mp.cosh(u / 2)

    minimum = mp.inf
    minimizer = mp.mpf(0)
    # Fourier transform of g*cosh(u/2) is
    # (hat_g(1/2+i xi)+hat_g(-1/2+i xi))/2 = Re hat_g(1/2+i xi).
    for k in range(2001):
        xi = mp.mpf(k) / 100
        value = mp.re(test.hat(mp.mpc(mp.mpf("0.5"), xi)))
        if value < minimum:
            minimum = value
            minimizer = xi
    return {
        "weight_identity": abs(honest - mapped) < mp.mpf("1e-25"),
        "honest": mp.nstr(honest, 15),
        "mapped_corpus": mp.nstr(mapped, 15),
        "corpus_same_g": mp.nstr(corpus, 15),
        "fourier_min": mp.nstr(minimum, 12),
        "fourier_argmin": mp.nstr(minimizer, 8),
        "class_preserved": minimum >= 0,
    }


def audit_test(
    test: TestFunction,
    cutoff: mp.mpf,
    positive_zero_count: int,
    eps: float,
) -> tuple[list[dict[str, str]], dict[str, str | bool], bool]:
    bare, reflected, _ = prime_sums(test)
    rows: list[dict[str, str]] = []
    all_pass = True

    requested_integral, requested_quad = symmetric_real_integral(
        lambda t: log_deriv_zeta(mp.mpc(RIGHT_REQUESTED, t))
        * test.hat(mp.mpc(RIGHT_REQUESTED, t)),
        float(cutoff),
        eps,
    )
    requested_tail = right_tail_budget(test, RIGHT_REQUESTED, cutoff)
    all_pass &= row(
        rows,
        "A requested Re=17/16 right inversion",
        requested_integral,
        -2 * mp.pi * bare,
        requested_quad + requested_tail,
    )

    actual_integral, actual_quad = symmetric_real_integral(
        lambda t: log_deriv_zeta(mp.mpc(RIGHT_ACTUAL, t))
        * test.hat(mp.mpc(RIGHT_ACTUAL, t)),
        float(cutoff),
        eps,
    )
    actual_tail = right_tail_budget(test, RIGHT_ACTUAL, cutoff)
    all_pass &= row(
        rows,
        "A2 actual Lean Re=2 right edge",
        actual_integral,
        -2 * mp.pi * bare,
        actual_quad + actual_tail,
    )

    left_integral, left_quad = symmetric_real_integral(
        lambda t: log_deriv_zeta(mp.mpc(LEFT_EDGE, t))
        * test.hat(mp.mpc(LEFT_EDGE, t)),
        float(cutoff),
        eps,
    )
    left_tail = logarithmic_tail_budget(test, log_deriv_zeta, LEFT_EDGE, cutoff)

    arch_integral, arch_quad = symmetric_real_integral(
        lambda t: chi_log_deriv(mp.mpc(LEFT_EDGE, t))
        * test.hat(mp.mpc(LEFT_EDGE, t)),
        float(cutoff),
        eps,
    )
    arch_tail = logarithmic_tail_budget(test, chi_log_deriv, LEFT_EDGE, cutoff)
    all_pass &= row(
        rows,
        "B left edge = 2pi reflected - arch",
        left_integral,
        2 * mp.pi * reflected - arch_integral,
        left_quad + left_tail + arch_quad + arch_tail,
    )

    zero_sum, zero_height = known_zero_sum(test, positive_zero_count)
    spectral_lhs = 2 * mp.pi * (zero_sum - mp.re(test.hat(mp.mpc(1, 0))))
    contour_rhs = arch_integral - 2 * mp.pi * (bare + reflected)
    spectral_tail = 2 * mp.pi * zero_tail_budget(test, zero_height)
    all_pass &= row(
        rows,
        "F full spectral/contour assembly",
        spectral_lhs,
        contour_rhs,
        spectral_tail + arch_quad + arch_tail,
    )

    details: dict[str, str | bool] = {
        "name": test.name,
        "R": mp.nstr(test.radius, 8),
        "T": mp.nstr(cutoff, 8),
        "positive_zeros": positive_zero_count,
        "last_zero_height": mp.nstr(zero_height, 12),
        "prime_bare": mp.nstr(bare, 15),
        "prime_reflected": mp.nstr(reflected, 15),
        "arch_integral": mp.nstr(arch_integral, 15),
        "hat_1": mp.nstr(test.hat(mp.mpc(1, 0)), 15),
    }
    return rows, details, all_pass


def print_table(test_name: str, rows: list[dict[str, str]]) -> None:
    print("\nIDENTITY TABLE -- %s" % test_name)
    print("%-43s %18s %18s %12s %12s" % (
        "identity", "LHS", "RHS", "rel_err", "budget"))
    for item in rows:
        print("%-43s %18s %18s %12s %12s" % (
            item["identity"],
            item["lhs"],
            item["rhs"],
            item["rel_err"],
            item["budget"],
        ))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="fast non-verdict-bearing run")
    parser.add_argument("--cutoff", type=float)
    parser.add_argument("--zeros", type=int)
    args = parser.parse_args()

    start = time.time()
    mp.mp.dps = 30 if args.smoke else 40
    cutoff = mp.mpf(args.cutoff if args.cutoff is not None else (28 if args.smoke else 80))
    zero_count = args.zeros if args.zeros is not None else (12 if args.smoke else 200)
    tests = [TestFunction("triangle-acf-R1", mp.mpf(1))]
    if not args.smoke:
        tests.append(TestFunction("triangle-acf-R2", mp.mpf(2)))
    eps = 2e-7 if args.smoke else 2e-9

    print("CLAIM_BOUNDARY EXPERIMENT_ONLY NO_RH_CLAIM")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("LEAN_EDGE_FACT actual_right=2 reflected_dual=17/16 left=-1/16")
    print("ZERO_SCOPE known critical-line zeros +/-; no claim excluding off-line zeros")

    all_rows: dict[str, list[dict[str, str]]] = {}
    all_details: list[dict[str, str | bool]] = []
    all_pass = True
    dictionaries: list[dict[str, str | bool]] = []
    for test in tests:
        rows, details, passed = audit_test(test, cutoff, zero_count, eps)
        all_rows[test.name] = rows
        all_details.append(details)
        all_pass &= passed
        dictionaries.append(dictionary_audit(test))
        print_table(test.name, rows)

    print("\nDICTIONARY")
    for test, result in zip(tests, dictionaries):
        print("%s %s" % (test.name, json.dumps(result, sort_keys=True)))
    weight_pass = all(bool(item["weight_identity"]) for item in dictionaries)
    class_failure = all(not bool(item["class_preserved"]) for item in dictionaries)

    print("\nSURPLUS SIGN")
    print("H(g)=C(g)+S(g), S(g)=sum Lambda(n)(1-n^-1/2)^2 g(log n).")
    print("standard(g)=arch/(2pi)-H(g)=arch/(2pi)-C(g)-S(g).")
    print("For these nonnegative triangle ACFs, S(g)>=0: the surplus is subtracted "
          "and HURTS positivity relative to the corpus comb.")
    print("For general FullWeilTest, autocorrelation means positive-definite, "
          "not pointwise nonnegative; g(log n) may have either sign.  Therefore "
          "the Lean class admits no universal helps/hurts conclusion.")

    canonical = json.dumps(
        {
            "details": all_details,
            "dictionary": dictionaries,
            "rows": all_rows,
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    deterministic = canonical == json.dumps(
        json.loads(canonical.decode("utf-8")),
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")

    max_rel = max(
        mp.mpf(item["rel_err"])
        for rows in all_rows.values()
        for item in rows
    )
    verdict_parts = []
    if all_pass:
        verdict_parts.append("AUDIT_CLEAN(max_rel_err=%s)" % mp.nstr(max_rel, 8))
    else:
        failed = [
            item["identity"]
            for rows in all_rows.values()
            for item in rows
            if mp.mpf(item["rel_err"]) > mp.mpf(item["budget"])
        ]
        verdict_parts.append(
            "DEFINITION_BUG(which=contour_identity,evidence=%s)" % "|".join(failed)
        )
    if weight_pass:
        verdict_parts.append(
            "DICTIONARY_RESOLVES(map=g_tilde(u)=g(u)*cosh(u/2);"
            "class_not_preserved=%s)" % str(class_failure).lower()
        )
    verdict = "+".join(verdict_parts)

    smoke_ok = (not args.smoke) or (time.time() - start < 30)
    print("\nGATES")
    print("G1 identity checks within truncation budget: %s" % ("PASS" if all_pass else "FAIL"))
    print("G2 deterministic canonical report bytes: %s sha256=%s" % (
        "PASS" if deterministic else "FAIL",
        hashlib.sha256(canonical).hexdigest(),
    ))
    print("G3 smoke runtime under 30s: %s%s" % (
        "PASS" if smoke_ok else "FAIL",
        " (not exercised)" if not args.smoke else "",
    ))
    print("VERDICT %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    return 0 if all_pass and deterministic and smoke_ok else 1


if __name__ == "__main__":
    sys.exit(main())
