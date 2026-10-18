#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Numerical stress test for the semilocal trace-convergence contract.

The operator is the finite Connes--van Suijlekom operator (CMP 406
(2025), 312, Lemmas 5.1--5.3 and Theorem 5.6), specialized to the
smallest even Galerkin eigenvector of the semilocal Weil form.

For x > 1 put a = log(x)/2 and use the orthonormal even basis

  e_0(u) = 1/sqrt(2a),  e_k(u) = cos(k*pi*u/a)/sqrt(a),  |u| <= a.

The matrix Q_{x,K} is assembled directly from POLE + ARCH - PRIME.
If c is its simple bottom eigenvector, its full complex Fourier
coefficient vector xi on {-K+1,...,K-1} is normalized by <1,xi> = 1.
    Transporting the centered coefficients to [0,2a] multiplies mode j
    by (-1)^j.  Writing D e_j = (j*pi/a)e_j in that transported basis,
    the rank-one operator

  D_x,K^sharp = D - |D xi><1|

annihilates xi and descends to a self-adjoint operator H_{x,K} on the
Q_{x,K}-orthogonal separated quotient.  The nonzero eigenvalues of
D_x,K^sharp are spec(H_{x,K}); they are the non-lattice zeros of the
Fourier transform of the Galerkin minimizer.  This real-root mechanism
uses no positivity of the unshifted Weil form: Q-min(Q) I is positive
semidefinite tautologically.

The script:
  * compares ordinary, UNWEIGHTED Tr h(H_{x,K}) with the source side
    for four even Paley--Wiener tests;
  * sends scrambled and Epstein data through the identical construction;
  * prints inverse-square tails and finite-ladder error slopes;
  * audits that construction code contains no zero oracle or cache read.

This is an experiment, not a proof and not an RH claim.  Its verdict is
STC-OPEN unless an instrument identity fails, in which case it is
STC-INSTRUMENT-FAIL.  The analytic missing lemma is stated in the final
printout.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import time

import mpmath as mp
import numpy as np


DEFAULT_LADDER = ((3, 12, 70), (5, 18, 90), (8, 26, 120))
QUICK_LADDER = ((3, 10, 55), (5, 14, 70))
BATTERY = ((0.7, 2), (0.7, 4), (1.0, 2), (1.0, 4))
TAIL_RADII = (10.0, 20.0, 40.0)
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
EULER_FLOAT = 0.57721566490153286061
BANNED_CALLS = {
    "zetazero", "zetazeros", "nzeros", "zero_cache", "load_zero",
    "verified_zeros",
}

CHECKS: list[tuple[str, bool, str]] = []
GL_CACHE: dict[tuple[int, int], tuple[list[mp.mpf], list[mp.mpf]]] = {}


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-43s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def prime_power_atoms(cap: int) -> tuple[list[mp.mpf], list[mp.mpf], list[int]]:
    """Own Eratosthenes sieve: (log n, Lambda(n)/sqrt(n), n)."""
    cap = int(cap)
    composite = [False] * (cap + 1)
    us: list[mp.mpf] = []
    ws: list[mp.mpf] = []
    ns: list[int] = []
    for p in range(2, cap + 1):
        if composite[p]:
            continue
        for q0 in range(p * p, cap + 1, p):
            composite[q0] = True
        lp = mp.log(p)
        q = p
        while q <= cap:
            us.append(mp.log(q))
            ws.append(lp / mp.sqrt(q))
            ns.append(q)
            q *= p
    order = sorted(range(len(ns)), key=lambda i: ns[i])
    return ([us[i] for i in order], [ws[i] for i in order],
            [ns[i] for i in order])


def epstein_atoms(cap: int) -> tuple[list[mp.mpf], list[mp.mpf], list[int]]:
    """Log-derivative coefficients of sum r_{x^2+5y^2}(n)n^-s/2."""
    cap = int(cap)
    reps = [0] * (cap + 1)
    xmax = math.isqrt(cap) + 1
    ymax = math.isqrt(cap // 5) + 1
    for xx in range(-xmax, xmax + 1):
        for yy in range(-ymax, ymax + 1):
            n = xx * xx + 5 * yy * yy
            if 1 <= n <= cap:
                reps[n] += 1
    coeff = [mp.mpf(r) / 2 for r in reps]
    lam = [mp.mpf(0)] * (cap + 1)
    for n in range(2, cap + 1):
        value = coeff[n] * mp.log(n)
        for d in range(2, n):
            if n % d == 0:
                value -= lam[d] * coeff[n // d]
        lam[n] = value
    ns = [n for n in range(2, cap + 1) if abs(lam[n]) > mp.mpf("1e-60")]
    return ([mp.log(n) for n in ns],
            [lam[n] / mp.sqrt(n) for n in ns], ns)


def world_atoms(x: int, world: str) -> tuple[list[mp.mpf], list[mp.mpf], list[int]]:
    us, ws, ns = prime_power_atoms(x)
    if world == "MAIN":
        return us, ws, ns
    if world == "SCRAMBLED":
        length = mp.log(x)
        pos = []
        for n in ns:
            frac = (float(n) * GOLDEN) % 1.0
            pos.append(length * mp.mpf(0.08 + 0.84 * frac))
        return pos, list(reversed(ws)), ns
    if world == "EPSTEIN":
        return epstein_atoms(x)
    raise ValueError(world)


def legendre_rule(order: int) -> tuple[list[mp.mpf], list[mp.mpf]]:
    key = (order, mp.mp.dps)
    if key not in GL_CACHE:
        nodes, weights = mp.gauss_quadrature(order, "legendre")
        GL_CACHE[key] = ([nodes[i] for i in range(order)],
                         [weights[i] for i in range(order)])
    return GL_CACHE[key]


def panel_rule(length: mp.mpf, modes: int,
               order: int = 24) -> tuple[list[mp.mpf], list[mp.mpf]]:
    """High-order composite Gauss rule; max phase per panel <= pi/2."""
    panels = max(24, 4 * modes)
    nodes0, weights0 = legendre_rule(order)
    nodes: list[mp.mpf] = []
    weights: list[mp.mpf] = []
    step = length / panels
    for panel in range(panels):
        lo = panel * step
        mid = lo + step / 2
        half = step / 2
        for node, weight in zip(nodes0, weights0):
            nodes.append(mid + half * node)
            weights.append(half * weight)
    return nodes, weights


def psi_matrix(v: mp.mpf, a: mp.mpf, modes: int) -> mp.matrix:
    """Autocorrelation matrix of the normalized even trig basis."""
    omegas = [mp.mpf(k) * mp.pi / a for k in range(modes)]
    norms = [mp.sqrt(2 * a)] + [mp.sqrt(a)] * (modes - 1)
    sins = [mp.sin(omega * v) for omega in omegas]
    terms = [omega * sine for omega, sine in zip(omegas, sins)]
    out = mp.matrix(modes)
    for i in range(modes):
        oi = omegas[i]
        for j in range(i, modes):
            oj = omegas[j]
            if i == j:
                if i == 0:
                    raw = 2 * a - v
                else:
                    raw = ((a - v / 2) * mp.cos(oi * v)
                           - mp.sin(oi * v) / (2 * oi))
            else:
                raw = ((-1) ** (i + j) * (terms[j] - terms[i])
                       / (oi * oi - oj * oj))
            value = raw / (norms[i] * norms[j])
            out[i, j] = value
            out[j, i] = value
    return out


def base_form(x: int, modes: int) -> tuple[mp.matrix, mp.mpf]:
    """POLE+ARCH matrix before the finite arithmetic atoms."""
    a = mp.log(x) / 2
    length = 2 * a
    nodes, weights = panel_rule(length, modes)
    form = mp.matrix(modes)
    for v, weight in zip(nodes, weights):
        psi = psi_matrix(v, a, modes)
        pole_factor = 4 * weight * mp.cosh(v / 2)
        arch_factor = 2 * weight / (1 - mp.exp(-2 * v))
        e2 = mp.exp(-2 * v)
        eh = mp.exp(-v / 2)
        for i in range(modes):
            for j in range(i, modes):
                value = (pole_factor * psi[i, j]
                         + arch_factor
                         * ((e2 if i == j else 0) - eh * psi[i, j]))
                form[i, j] += value
                if i != j:
                    form[j, i] += value
    diagonal = (-(mp.euler + mp.log(mp.pi))
                - mp.log(1 - mp.exp(-2 * length)))
    for i in range(modes):
        form[i, i] += diagonal
    return form, a


def build_form(base: mp.matrix, a: mp.mpf, x: int, modes: int,
               world: str) -> tuple[mp.matrix, int]:
    form = base.copy()
    us, weights, ns = world_atoms(x, world)
    length = 2 * a
    kept = 0
    for u, atom_weight in zip(us, weights):
        if not (0 < u <= length):
            continue
        kept += 1
        psi = psi_matrix(u, a, modes)
        for i in range(modes):
            for j in range(i, modes):
                value = -2 * atom_weight * psi[i, j]
                form[i, j] += value
                if i != j:
                    form[j, i] += value
    return form, kept


def finite_connes_operator(form: mp.matrix, a: mp.mpf) -> dict:
    """Return the quotient spectrum from Theorem 5.6."""
    evals, evecs = mp.eigsy(form)
    modes = form.rows
    c = [evecs[i, 0] for i in range(modes)]
    if c[max(range(modes), key=lambda i: abs(c[i]))] < 0:
        c = [-value for value in c]

    nmax = modes - 1
    xi_mp: list[mp.mpf] = []
    root_two = mp.sqrt(2)
    for j in range(-nmax, nmax + 1):
        centered_coefficient = c[0] if j == 0 else c[abs(j)] / root_two
        # Theorem 5.6 is written on [0,L].  Our Galerkin basis is on
        # [-L/2,L/2], and translation by L/2 contributes exp(-i*pi*j).
        xi_mp.append(((-1) ** j) * centered_coefficient)
    total = mp.fsum(xi_mp)
    xi_mp = [value / total for value in xi_mp]

    indices = list(range(-nmax, nmax + 1))
    diag_mp = [mp.mpf(j) * mp.pi / a for j in indices]
    dsharp = mp.matrix(len(indices))
    for i in range(len(indices)):
        for j in range(len(indices)):
            dsharp[i, j] = ((diag_mp[i] if i == j else 0)
                            - diag_mp[i] * xi_mp[i])
    roots_mp = list(mp.eig(dsharp, left=False, right=False))
    zero_index = min(range(len(roots_mp)), key=lambda i: abs(roots_mp[i]))
    roots_mp.pop(zero_index)
    imag_max = max(float(abs(mp.im(root))) for root in roots_mp)
    spectrum = np.sort(np.array([float(mp.re(root)) for root in roots_mp]))
    symmetry = float(np.max(np.abs(spectrum + spectrum[::-1])))
    return {
        "spectrum": spectrum,
        "tau": float(evals[0]),
        "gap": float(evals[1] - evals[0]),
        "imag_max": imag_max,
        "symmetry": symmetry,
        "normalization": float(total),
    }


def test_f(v: mp.mpf, bandwidth: float, power: int) -> mp.mpf:
    av = abs(v)
    b = mp.mpf(bandwidth)
    if av > b:
        return mp.mpf(0)
    return (1 - (av / b) ** 2) ** power


def h_value(t: float, bandwidth: float, power: int) -> float:
    mu = abs(mp.mpf(bandwidth) * mp.mpf(t))
    if mu < mp.mpf("1e-30"):
        return float(2 * bandwidth * (4 ** power)
                     * math.factorial(power) ** 2
                     / math.factorial(2 * power + 1))
    value = (mp.mpf(bandwidth) * mp.sqrt(mp.pi)
             * mp.factorial(power) * (2 / mu) ** (power + mp.mpf("0.5"))
             * mp.besselj(power + mp.mpf("0.5"), mu))
    return float(value)


def source_value(bandwidth: float, power: int) -> float:
    """POLE+ARCH-PRIME for the compactly supported Fourier-side test."""
    b = mp.mpf(bandwidth)

    def fv(v: mp.mpf) -> mp.mpf:
        return test_f(v, bandwidth, power)

    pole = 4 * mp.quad(lambda v: fv(v) * mp.cosh(v / 2), [0, b])

    def arch_integrand(v: mp.mpf) -> mp.mpf:
        if v == 0:
            return -mp.mpf(3) / 4
        return ((mp.exp(-2 * v) - fv(v) * mp.exp(-v / 2))
                / (1 - mp.exp(-2 * v)))

    arch = (-(mp.euler + mp.log(mp.pi))
            + 2 * mp.quad(arch_integrand, [0, b])
            - mp.log(1 - mp.exp(-2 * b)))
    cap = int(mp.floor(mp.exp(b) + mp.mpf("1e-30")))
    us, weights, _ns = prime_power_atoms(cap)
    prime = 2 * mp.fsum(weight * fv(u) for u, weight in zip(us, weights))
    return float(pole + arch - prime)


def trace_h(spectrum: np.ndarray, bandwidth: float, power: int) -> float:
    return math.fsum(h_value(float(value), bandwidth, power)
                     for value in spectrum)


def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    bad: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            modules = ([alias.name for alias in node.names]
                       if isinstance(node, ast.Import)
                       else [node.module or ""])
            for module in modules:
                if module.startswith("verification"):
                    bad.add("import:" + module)
        if isinstance(node, ast.Call):
            target = node.func
            name = (target.id if isinstance(target, ast.Name)
                    else target.attr if isinstance(target, ast.Attribute)
                    else "")
            if name.lower() in BANNED_CALLS:
                bad.add("call:" + name)
    return not bad, "violations=%s" % (sorted(bad) if bad else "none")


def log_slope(xs: list[float], ys: list[float]) -> float:
    x = np.asarray(xs, float)
    y = np.asarray(ys, float)
    live = np.isfinite(y) & (y > 0)
    if int(np.sum(live)) < 2:
        return float("nan")
    return float(np.polyfit(np.log(x[live]), np.log(y[live]), 1)[0])


def run(quick: bool) -> int:
    started = time.time()
    ladder = QUICK_LADDER if quick else DEFAULT_LADDER
    spec_hash = hashlib.sha256(
        (repr(ladder) + repr(BATTERY) + __doc__).encode("utf-8")
    ).hexdigest()

    print("=" * 78)
    print("STC finite Connes operator stress test")
    print("SPEC_SHA %s%s" % (spec_hash[:16], "  QUICK" if quick else ""))
    print("=" * 78)

    section("I. SOURCE-ONLY FIREWALL AND TEST TARGETS")
    firewall_ok, firewall_detail = firewall_audit()
    check("A1 no target-zero access/import", firewall_ok, firewall_detail)
    max_dps = max(row[2] for row in ladder)
    mp.mp.dps = max_dps
    targets = {test: source_value(*test) for test in BATTERY}
    for test, target in targets.items():
        print("  B=%.1f m=%d  SOURCE=%+.12e  prime cap=%d"
              % (test[0], test[1], target, math.floor(math.exp(test[0]))))
    check("A2 every arithmetic test is tower-complete",
          all(math.exp(b) <= ladder[0][0] for b, _m in BATTERY),
          "max exp(B)=%.6f <= x_min=%d"
          % (max(math.exp(b) for b, _m in BATTERY), ladder[0][0]))

    section("II. FINITE SELF-ADJOINT QUOTIENT OPERATORS")
    cells: dict[tuple[str, int], dict] = {}
    construction_ok = True
    for x, modes, dps in ladder:
        mp.mp.dps = dps
        base, a = base_form(x, modes)
        for world in ("MAIN", "SCRAMBLED", "EPSTEIN"):
            form, atom_count = build_form(base, a, x, modes, world)
            cell = finite_connes_operator(form, a)
            cell.update({"x": x, "modes": modes, "dps": dps,
                         "atoms": atom_count})
            cell["valid_selfadjoint"] = (
                cell["gap"] > 0
                and cell["imag_max"] <= 2e-7
                and cell["symmetry"] <= 2e-7
            )
            cells[(world, x)] = cell
            if world == "MAIN":
                construction_ok &= cell["valid_selfadjoint"]
            positives = cell["spectrum"][cell["spectrum"] > 1e-8]
            print("  %-9s x=%d K=%d dps=%d atoms=%d dimH=%d "
                  "tau=%+.4e gap=%.3e im=%.1e sym=%.1e first+=%s%s"
                  % (world, x, modes, dps, atom_count,
                     len(cell["spectrum"]), cell["tau"], cell["gap"],
                     cell["imag_max"], cell["symmetry"],
                     ",".join("%.4f" % value for value in positives[:3]),
                     ("" if cell["valid_selfadjoint"]
                      else " REFUSED(non-real quotient)")))
    check("A3 MAIN CvS hypotheses/instrument", construction_ok,
          "simple bottom; MAIN quotient roots real/even within 2e-7")

    section("III. ORDINARY TRACE ERRORS epsilon_x(h)")
    errors: dict[tuple[str, tuple[float, int]], list[float]] = {}
    traces: dict[tuple[str, tuple[float, int]], list[float]] = {}
    xs = [float(row[0]) for row in ladder]
    for world in ("MAIN", "SCRAMBLED", "EPSTEIN"):
        print("  " + world)
        for test in BATTERY:
            values = [
                (trace_h(cells[(world, x)]["spectrum"], *test)
                 if cells[(world, x)]["valid_selfadjoint"] else float("nan"))
                for x, _modes, _dps in ladder
            ]
            errs = [abs(value - targets[test]) for value in values]
            traces[(world, test)] = values
            errors[(world, test)] = errs
            print("    B=%.1f m=%d target=%+.6e  %s  slope=%+.3f"
                  % (test[0], test[1], targets[test],
                     "  ".join(("x%d tr=%+.6e eps=%.3e"
                               % (row[0], value, err))
                              if math.isfinite(value)
                              else "x%d REFUSED" % row[0]
                              for row, value, err
                              in zip(ladder, values, errs)),
                     log_slope(xs, errs)))

    section("IV. CONTROL SEPARATION AND R4 METER")
    main_last = np.array([errors[("MAIN", test)][-1] for test in BATTERY])
    control_medians = {}
    for world in ("SCRAMBLED", "EPSTEIN"):
        ctrl_last = np.array([errors[(world, test)][-1] for test in BATTERY])
        ratios = ctrl_last / np.maximum(main_last, 1e-300)
        trace_sep = np.array([
            abs(traces[(world, test)][-1] - traces[("MAIN", test)][-1])
            for test in BATTERY
        ])
        valid_ratios = ratios[np.isfinite(ratios)]
        valid_sep = trace_sep[np.isfinite(trace_sep)]
        control_medians[world] = (
            float(np.median(valid_ratios)) if len(valid_ratios)
            else float("nan")
        )
        refused = not cells[(world, ladder[-1][0])]["valid_selfadjoint"]
        print("  %-9s eps/main ratios %s  median=%s; "
              "median |Tr_ctrl-Tr_main|=%s%s"
              % (world,
                 " ".join("%.3f" % value if math.isfinite(value)
                          else "REFUSED" for value in ratios),
                 ("%.3f" % control_medians[world]
                  if math.isfinite(control_medians[world]) else "n/a"),
                 ("%.3e" % float(np.median(valid_sep))
                  if len(valid_sep) else "n/a"),
                 "; control operator REFUSED at final rung"
                 if refused else ""))
    separated = all(
        (not cells[(world, ladder[-1][0])]["valid_selfadjoint"])
        or any(abs(traces[(world, test)][-1]
                   - traces[("MAIN", test)][-1]) > 1e-5
               for test in BATTERY)
        for world in ("SCRAMBLED", "EPSTEIN")
    )
    check("C1 altered Euler worlds do not match MAIN", separated,
          "median eps/main SCR=%.3f EPS=%.3f"
          % (control_medians["SCRAMBLED"], control_medians["EPSTEIN"]))

    print("  R4 finite-ladder tails sum_{|lambda|>R} lambda^-2:")
    for world in ("MAIN", "SCRAMBLED", "EPSTEIN"):
        for x, _modes, _dps in ladder:
            cell = cells[(world, x)]
            if not cell["valid_selfadjoint"]:
                print("    %-9s x=%d  REFUSED(non-real quotient)"
                      % (world, x))
                continue
            spectrum = cell["spectrum"]
            row = []
            for radius in TAIL_RADII:
                tail = float(np.sum(
                    1.0 / spectrum[np.abs(spectrum) > radius] ** 2
                ))
                row.append("R%d=%.6e" % (radius, tail))
            print("    %-9s x=%d  %s" % (world, x, "  ".join(row)))

    section("V. VERDICT")
    elapsed = time.time() - started
    all_checks = all(ok for _name, ok, _detail in CHECKS)
    verdict = "STC-OPEN" if all_checks else "STC-INSTRUMENT-FAIL"
    print("""\
MINIMAL MISSING LEMMA (ordinary trace, not a weighted quadrature identity).
For one source-only cofinal choice x_n -> infinity and K_n/log(x_n) ->
infinity, let H_n be the Connes--van Suijlekom separated-quotient
operator built above.  Prove simultaneously

  (L1)  for every even f in C_c^infinity(R), with h = Fourier(f),
        Tr h(H_n) -> W_zeta(f) = POLE(f)+ARCH(f)-PRIME(f);
  (L2)  sup_n sum_{lambda in spec(H_n), |lambda|>R} lambda^-2 -> 0.

Caratheodory--Fejer/CvS proves only reality of each finite spectrum.
Kac--Akhiezer--Szego and Landau--Widom control background/plunge
asymptotics, not the arithmetic spectral-shift cancellation in (L1).
Krein's trace formula would apply after proving a common self-adjoint
reference and trace-class resolvent convergence; that is exactly the
missing semilocal statement, not a consequence of rank-one notation.
No convergence RATE or target ordinate is used by this probe.""")
    print("CHECKS %d/%d PASS  runtime %.1fs  SPEC_SHA %s"
          % (sum(ok for _n, ok, _d in CHECKS), len(CHECKS),
             elapsed, spec_hash[:16]))
    print("VERDICT: %s" % verdict)
    print("NO RH CLAIM. EXPLORATION ONLY.")
    return 0 if all_checks else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    return run(bool(args.quick))


if __name__ == "__main__":
    raise SystemExit(main())
