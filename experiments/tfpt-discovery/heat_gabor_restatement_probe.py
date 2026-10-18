#!/usr/bin/env python3
"""Heat/Gabor restatement probe (experiment only; no RH claim).

Checks the proposed cross-term cancellation, heat equation, inverse
transformation, and heat-kernel normalization.  It also measures the
prime-side saddle budget.  The exact prime sum is deliberately reported as a
truncated lower bound whenever the requested 1e-12 relative tail would require
an infeasible cutoff; no PNT approximation is presented as an exact sum.
"""

from __future__ import annotations

import json
import math
import time
from pathlib import Path

import mpmath as mp
import sympy as sp


OUTPUT = Path(__file__).with_name("heat_gabor_restatement_probe_result.json")
A_VALUES = (0.25, 0.125, 0.0625, 0.03125)
N_CAP = 20_000_000
TAIL_RELATIVE_TARGET = 1.0e-12
MP_DPS = 60


def symbolic_checks() -> dict[str, object]:
    a, w, t = sp.symbols("a w t", positive=True)
    ap = sp.exp(-((t - w) ** 2) / (2 * a))
    am = sp.exp(-((t + w) ** 2) / (2 * a))
    cross = sp.exp(-(t**2 + w**2) / (2 * a))
    hat = sp.pi / (4 * a) * (ap + am + 2 * cross)
    hat0 = sp.pi / a * sp.exp(-(t**2) / (2 * a))
    heat_atom = a ** (-sp.Rational(1, 2)) * ap
    cancellation = sp.simplify(
        sp.sqrt(a) * (2 * hat - sp.exp(-(w**2) / (2 * a)) * hat0)
        - sp.pi / (2 * sp.sqrt(a)) * (ap + am)
    )
    heat_residual = sp.simplify(
        sp.diff(heat_atom, a) - sp.diff(heat_atom, w, 2) / 2
    )

    H, H0 = sp.symbols("H H0")
    d = sp.exp(-(w**2) / (2 * a))
    recovered_G = (H + d * H0) / (2 * sp.sqrt(a))
    # Direct substitution is clearer than relying on the degenerate solve.
    back_residual = sp.simplify(
        recovered_G.subs(H, sp.sqrt(a) * (2 * sp.Symbol("G") - d * sp.Symbol("G0")))
        .subs(H0, sp.sqrt(a) * sp.Symbol("G0"))
        - sp.Symbol("G")
    )
    kernel_constant = sp.simplify(
        (sp.pi / sp.sqrt(a) * ap)
        / ((2 * sp.pi * a) ** (-sp.Rational(1, 2)) * ap)
    )
    return {
        "cross_term_cancellation": cancellation == 0,
        "per_atom_heat_equation": heat_residual == 0,
        "back_transform": back_residual == 0,
        "heat_kernel_constant": str(kernel_constant),
        "exact_identity": (
            "H(a,w)=pi/sqrt(a) Re sum_rho m_rho exp(-(t_rho-w)^2/(2a))"
        ),
        "convolution_identity": (
            "H=pi*sqrt(2*pi)*(K_a * Re(mu_zero)), "
            "K_a(x)=(2*pi*a)^(-1/2) exp(-x^2/(2a))"
        ),
    }


def prime_powers(limit: int) -> list[tuple[int, float]]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    root = math.isqrt(limit)
    for p in range(2, root + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    terms: list[tuple[int, float]] = []
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        logp = math.log(p)
        power = p
        while power <= limit:
            terms.append((power, logp))
            if power > limit // p:
                break
            power *= p
    return terms


def normal_tail_fraction(a: float, log_cutoff: float) -> float:
    mean = 1.0 / (2.0 * a)
    z = math.sqrt(a) * (log_cutoff - mean)
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def required_log_cutoff(a: float) -> float:
    mean = 1.0 / (2.0 * a)
    lo, hi = mean, mean + 20.0 / math.sqrt(a)
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if normal_tail_fraction(a, mid) > TAIL_RELATIVE_TARGET:
            lo = mid
        else:
            hi = mid
    return hi


def prime_budget(terms: list[tuple[int, float]]) -> list[dict[str, object]]:
    rows = []
    log_cap = math.log(N_CAP)
    for a in A_VALUES:
        exact_partial = math.fsum(
            logp
            * n ** (-0.5)
            * math.exp(-0.5 * a * math.log(n) ** 2)
            for n, logp in terms
        )
        pnt = math.sqrt(2.0 * math.pi / a) * math.exp(1.0 / (8.0 * a))
        slack = math.exp(1.0 / math.sqrt(a))
        pnt_tail = normal_tail_fraction(a, log_cap)
        req_log = required_log_cutoff(a)
        rows.append(
            {
                "a": a,
                "N_exact": N_CAP,
                "B_prime_exact_partial": exact_partial,
                "pnt_full_saddle": pnt,
                "slack": slack,
                "log_B_over_slack": math.log(exact_partial / slack),
                "log_pnt_over_slack": math.log(pnt / slack),
                "partial_over_pnt": exact_partial / pnt,
                "pnt_tail_fraction_after_cap": pnt_tail,
                "required_log_N_for_1e-12_pnt_tail": req_log,
                "requested_exact_tail_feasible": req_log <= log_cap,
            }
        )
    return rows


def source_terms_and_zero_sanity(
    budget_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    mp.mp.dps = MP_DPS
    gamma1 = mp.im(mp.zetazero(1))
    rows = []
    for budget in budget_rows:
        a = mp.mpf(str(budget["a"]))
        B_partial = mp.mpf(str(budget["B_prime_exact_partial"]))
        pole = 2 * mp.pi / a * mp.exp(1 / (8 * a))
        prime_partial = mp.sqrt(2 * mp.pi / a) * B_partial

        def integrand(x: mp.mpf) -> mp.mpf:
            kernel = mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * x)) - mp.log(mp.pi)
            hat0 = mp.pi / a * mp.exp(-(x * x) / (2 * a))
            return kernel * hat0 / mp.pi

        arch = mp.quad(integrand, [0, 1, 3, 6, mp.inf])
        first_zero_pair = 2 * mp.pi / a * mp.exp(-(gamma1 * gamma1) / (2 * a))
        rows.append(
            {
                "a": float(a),
                "pole": mp.nstr(pole, 18),
                "prime_exact_partial": mp.nstr(prime_partial, 18),
                "archimedean": mp.nstr(arch, 18),
                "source_partial_residual": mp.nstr(pole + arch - prime_partial, 18),
                "first_zero_pair_positive_sanity": mp.nstr(first_zero_pair, 18),
                "sanity_note": (
                    "The zero-side value uses the first known critical-line zero only. "
                    "It is a positive magnitude sanity check, not an RH argument. "
                    "The source residual is not a full G value when the prime tail is unresolved."
                ),
            }
        )
    return rows


def main() -> int:
    started = time.time()
    symbolic = symbolic_checks()
    terms = prime_powers(N_CAP)
    budget = prime_budget(terms)
    source = source_terms_and_zero_sanity(budget)
    all_symbolic = all(
        symbolic[key]
        for key in (
            "cross_term_cancellation",
            "per_atom_heat_equation",
            "back_transform",
        )
    )
    result = {
        "claim_boundary": "Experiment only; no RH claim.",
        "verdict": "RESTATED" if all_symbolic else "INSTRUMENT_FAILURE",
        "symbolic": symbolic,
        "prime_budget": budget,
        "source_terms": source,
        "interpretation": (
            "H is exactly a Gaussian heat-kernel smoothing of the real part "
            "of the transformed zero measure. Positivity is the existing "
            "Gabor/Weil criterion in heat coordinates. The arithmetic side "
            "contains exp(1/(8a))-scale saddle terms, while the proposed slack "
            "is only exp(1/sqrt(a)); controlling the cancellation is not a "
            "weaker task. r608's cross-lobe residual was a normalization artifact."
        ),
        "cutoff_fence": (
            "At small a, an exact 1e-12-relative prime tail is incompatible "
            "with the two-minute finite-sieve constraint; rows are explicitly "
            "typed exact_partial and paired with a PNT Gaussian-tail diagnostic."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("VERDICT", result["verdict"])
    print("heat-kernel constant", symbolic["heat_kernel_constant"])
    for row in budget:
        print(
            "a={a:.5f} B_partial={B_prime_exact_partial:.12g} "
            "PNT={pnt_full_saddle:.12g} slack={slack:.12g} "
            "log(PNT/slack)={log_pnt_over_slack:.6f} "
            "tail~{pnt_tail_fraction_after_cap:.3e} feasible={requested_exact_tail_feasible}".format(
                **row
            )
        )
    print(f"runtime={time.time() - started:.3f}s result={OUTPUT}")
    return 0 if all_symbolic else 1


if __name__ == "__main__":
    raise SystemExit(main())
