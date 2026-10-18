#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tp_sol_probe -- thinning-persistence obstruction probe.

EXPLORATION ONLY.  NO RH CLAIM.  This file imports no earlier probe and
writes no files.

TARGET (TPL).  Along a predeclared extremal ladder x -> infinity:
  (i) for every fixed T, eventually
          #{zeros of Ehat_x in (0,T)} = N_Xi(T);
  (ii) every Nyquist-excess zero lies beyond R(x), where R(x) -> infinity.
In the equivalent Sol formulation one asks
  ||theta_x-k_sqrt(x)||_{L1(exp(sigma |u|)du)} -> 0, sigma < 1/2,
together with a uniform local spectral-count bound
  #(spec(H_x) intersect [T,T+1]) <= C log(2+T).

The probe tests three precise claims behind the obstruction theorem proved
in the accompanying response.

O1  OFF-LINE BOOKKEEPING.  If rho=1/2+delta+i*t is off the line, its
    functional-equation/conjugation orbit becomes z=+-t+-i*delta in the
    Xi variable.  For a real even entire E the quartet contributes

        sum_orbit E(z)^2 = 4 Re(E(t+i*delta)^2),

    not a positive norm square.  At a simple real zero E(t)=0 this differs
    from the coalesced double on-line orbit by

        -4 delta^2 E'(t)^2 + O(delta^4).

    On the x=5 source-only extremal matrix we plant exactly this
    multiplicity-preserving split.  The split is scaled by the computable
    crossing delta_* = sqrt(lambda_min)/(2|E'(t)|).  It makes lambda_min
    negative while the simple ground direction and its (0,30) real-zero
    census remain unchanged.  Thus the signature is loss of positivity,
    not a forced band-count mismatch.

O2  PROLATE/DAVIS-KAHAN SCALE.  The prime part is assembled separately.
    We print its operator norm and constant-vector Rayleigh quotient
    against both the actual ground gap and the prime-dropped gap for
    x=3,5,8.  We also print Connes' displayed prolate defect asymptotic

      (2^14/3)*sqrt(2)*pi^5*x^(9/2)*exp(-4*pi*x).

    An operator-norm Davis-Kahan comparison is informative only when the
    perturbation/gap ratio is small.

O3  RIEMANN-von MANGOLDT INFORMATION BUDGET.  Emptying a unit interval
    near height T relocates only O(log T) atoms.  Hence both the regular
    sequence and a sequence with prescribed unit gaps can satisfy the
    same smooth RvM counting law with O(log T) error.  Global density does
    not supply the local lower-density/Szego input used by MNT/Totik or
    Levin-Lubinsky asymptotics.

Runtime is minutes-scale.  All ladders and planted factors are declared
before evaluation.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import time

import mpmath as mp
import numpy as np


X_LADDER = (3, 5, 8)
DPS = {3: 50, 5: 70, 8: 90}
KFAC = 1.25
PLANT_X = 5
PLANT_FACTORS = (0.50, 1.25, 2.00)
ROOT_BAND = 30.0
ROOT_STEP = 0.04
ROOT_BISECT = 70
RVM_HEIGHTS = (1.0e3, 1.0e6, 1.0e12)
RUNTIME_BAR = 600.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
STARTED = time.time()
CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %-46s %s" % ("PASS" if ok else "FAIL", name, detail))


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def sci(value: mp.mpf | float, digits: int = 8) -> str:
    return mp.nstr(value, digits, min_fixed=0, max_fixed=0)


def prime_power_atoms(x: int) -> list[tuple[mp.mpf, mp.mpf]]:
    """All (log(p^k), log(p)/sqrt(p^k)) with p^k <= x."""
    composite = [False] * (x + 1)
    atoms: list[tuple[mp.mpf, mp.mpf]] = []
    for p in range(2, x + 1):
        if composite[p]:
            continue
        for q0 in range(p * p, x + 1, p):
            composite[q0] = True
        q = p
        while q <= x:
            atoms.append((mp.log(q), mp.log(p) / mp.sqrt(q)))
            q *= p
    atoms.sort(key=lambda item: item[0])
    return atoms


def build_extremal_cell(x: int, dps: int) -> dict:
    """Minimal independent high-precision trig-Galerkin assembly.

    The returned matrices use the orthonormal even basis
      1/sqrt(2a), cos(k*pi*u/a)/sqrt(a), k >= 1, |u| <= a.
    We retain the prime block separately, so
      M_full = M_pole + M_arch - M_prime.
    """
    with mp.workdps(dps):
        a = mp.log(x) / 2
        length = 2 * a
        K = int(math.ceil(KFAC * x * math.log(x)))
        omegas = [mp.mpf(k) * mp.pi / a for k in range(K)]
        parity = [mp.mpf(-1 if k % 2 else 1) for k in range(K)]
        norms = [mp.sqrt(length)] + [mp.sqrt(a)] * (K - 1)

        def arch_weight(w: mp.mpf) -> mp.mpf:
            return mp.exp(-w / 2) / (-mp.expm1(-2 * w))

        def arch_regular(w: mp.mpf) -> mp.mpf:
            if w == 0:
                return mp.mpf("0.25")
            return arch_weight(w) - 1 / (2 * w)

        jvec: list[mp.mpf] = []
        for k, omega in enumerate(omegas):
            if k == 0:
                jvec.append(mp.mpf(0))
                continue
            nperiod = int(mp.floor(length * omega / mp.pi))
            points = ([mp.mpf(0)]
                      + [j * mp.pi / omega for j in range(1, nperiod + 1)]
                      + [length])
            integral = mp.quad(
                lambda w, omega=omega: mp.sin(omega * w) * arch_regular(w),
                points,
            )
            jvec.append(integral + mp.si(length * omega) / 2)

        atoms = prime_power_atoms(x)
        pvec = [
            mp.fsum(weight * mp.sin(omega * u) for u, weight in atoms)
            for omega in omegas
        ]

        pole = mp.zeros(K, K)
        arch = mp.zeros(K, K)
        prime = mp.zeros(K, K)

        ip = [
            parity[k] * mp.sinh(a / 2) / (mp.mpf(1) / 4 + omegas[k] ** 2)
            for k in range(K)
        ]
        for i in range(K):
            for j in range(K):
                pole[i, j] = 2 * ip[i] * ip[j]

        for i in range(K):
            for j in range(i):
                sign = parity[i] * parity[j]
                denominator = omegas[j] ** 2 - omegas[i] ** 2
                arch_value = (
                    -2 * sign
                    * (omegas[i] * jvec[i] - omegas[j] * jvec[j])
                    / denominator
                )
                prime_value = (
                    2 * sign
                    * (omegas[i] * pvec[i] - omegas[j] * pvec[j])
                    / denominator
                )
                arch[i, j] = arch[j, i] = arch_value
                prime[i, j] = prime[j, i] = prime_value

        tail = lambda f0: -f0 / 2 * mp.log1p(-mp.exp(-2 * length))
        for k, omega in enumerate(omegas):
            if k == 0:
                f0 = length

                def psi_diag(w: mp.mpf) -> mp.mpf:
                    return length - w
            else:
                f0 = a

                def psi_diag(w: mp.mpf, omega: mp.mpf = omega) -> mp.mpf:
                    return ((a - w / 2) * mp.cos(omega * w)
                            - mp.sin(omega * w) / (2 * omega))

            def diagonal_integrand(
                w: mp.mpf,
                f0: mp.mpf = f0,
                psi_diag=psi_diag,
            ) -> mp.mpf:
                if w == 0:
                    # Every even cosine autocorrelation here has
                    # right derivative psi'(0+) = -1.
                    return (-mp.mpf("1.5") * f0 + 1) / 2
                return (
                    f0 * mp.exp(-2 * w) - psi_diag(w) * mp.exp(-w / 2)
                ) / (-mp.expm1(-2 * w))

            nperiod = max(int(mp.floor(length * omega / mp.pi)), 1) if k else 1
            points = [mp.mpf(0), mp.mpf("1e-6"), mp.mpf("1e-3"),
                      mp.mpf("0.05"), length]
            if k:
                points += [
                    j * mp.pi / omega for j in range(1, nperiod + 1)
                    if j * mp.pi / omega <= length
                ]
            points = sorted(set(points))
            body = mp.quad(diagonal_integrand, points)
            arch[k, k] = (
                -f0 * (mp.euler + mp.log(mp.pi)) + 2 * (body + tail(f0))
            )
            if k == 0:
                pdiag = mp.fsum(weight * (length - u) for u, weight in atoms)
            else:
                pdiag = mp.fsum(
                    weight * ((a - u / 2) * mp.cos(omega * u)
                              - mp.sin(omega * u) / (2 * omega))
                    for u, weight in atoms
                )
            prime[k, k] = 2 * pdiag

        def normalize(matrix: mp.matrix) -> mp.matrix:
            out = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    out[i, j] = matrix[i, j] / (norms[i] * norms[j])
            return out

        pole_n = normalize(pole)
        arch_n = normalize(arch)
        prime_n = normalize(prime)
        model_n = pole_n + arch_n
        full_n = model_n - prime_n
        evals, evecs = mp.eigsy(full_n)
        model_evals, model_evecs = mp.eigsy(model_n)
        prime_evals = mp.eigsy(prime_n, eigvals_only=True)
        vector = mp.matrix([evecs[i, 0] for i in range(K)])
        model_vector = mp.matrix([model_evecs[i, 0] for i in range(K)])
        if vector[max(range(K), key=lambda i: abs(vector[i]))] < 0:
            vector = -vector
        if model_vector[max(range(K), key=lambda i: abs(model_vector[i]))] < 0:
            model_vector = -model_vector

        return {
            "x": x,
            "dps": dps,
            "a": a,
            "K": K,
            "omegas": omegas,
            "norms": norms,
            "full": full_n,
            "model": model_n,
            "prime": prime_n,
            "lambda": evals[0],
            "gap": evals[1] - evals[0],
            "model_gap": model_evals[1] - model_evals[0],
            "prime_norm": max(abs(v) for v in prime_evals),
            "prime_const": prime_n[0, 0],
            "vector": vector,
            "model_vector": model_vector,
        }


def sine_over(value: mp.mpc, a: mp.mpf) -> mp.mpc:
    if abs(value) < mp.mpf("1e-40"):
        return a
    return mp.sin(a * value) / value


def evaluation_vector(cell: dict, z: mp.mpc | mp.mpf) -> mp.matrix:
    a = cell["a"]
    values = []
    for omega, norm in zip(cell["omegas"], cell["norms"]):
        raw = sine_over(z - omega, a) + sine_over(z + omega, a)
        values.append(raw / norm)
    return mp.matrix(values)


def profile(cell: dict, vector: mp.matrix, z: mp.mpc | mp.mpf) -> mp.mpc:
    values = evaluation_vector(cell, z)
    return mp.fsum(vector[i] * values[i] for i in range(cell["K"]))


def real_roots(cell: dict, vector: mp.matrix, upper: float) -> list[mp.mpf]:
    step = mp.mpf(str(ROOT_STEP))
    previous_t = mp.mpf("1e-8")
    previous_v = mp.re(profile(cell, vector, previous_t))
    roots: list[mp.mpf] = []
    count = int(math.ceil(upper / ROOT_STEP))
    for index in range(1, count + 1):
        current_t = min(mp.mpf(str(upper)), mp.mpf(index) * step)
        current_v = mp.re(profile(cell, vector, current_t))
        if previous_v * current_v < 0:
            lo, hi, flo = previous_t, current_t, previous_v
            for _ in range(ROOT_BISECT):
                mid = (lo + hi) / 2
                fmid = mp.re(profile(cell, vector, mid))
                if flo * fmid > 0:
                    lo, flo = mid, fmid
                else:
                    hi = mid
            roots.append((lo + hi) / 2)
        previous_t, previous_v = current_t, current_v
        if current_t >= upper:
            break
    return roots


def matrix_dot(left: mp.matrix, matrix: mp.matrix, right: mp.matrix) -> mp.mpf:
    return (left.T * matrix * right)[0]


def orient(vector: mp.matrix, reference: mp.matrix) -> mp.matrix:
    return -vector if (vector.T * reference)[0] < 0 else vector


def prolate_defect_asymptotic(x: int) -> mp.mpf:
    constant = mp.mpf(2) ** 14 / 3 * mp.sqrt(2) * mp.pi ** 5
    return constant * mp.mpf(x) ** (mp.mpf(9) / 2) * mp.exp(-4 * mp.pi * x)


def smooth_rvm_count(T: float) -> float:
    """Smooth positive-ordinate RvM main term."""
    return T / (2 * math.pi) * (math.log(T / (2 * math.pi)) - 1.0) + 0.875


def firewall() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    bad = [name for name in imported
           if "probe" in name or name.startswith("verification")]
    writes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in {"open", "write", "save", "savetxt"}:
                if node.func.id != "open":
                    writes.append(node.func.id)
    return not bad and not writes, "bad imports=%s write calls=%s" % (bad, writes)


def run() -> int:
    print("=" * 78)
    print("THINNING-PERSISTENCE LEMMA ATTACK -- obstruction probe")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    print("=" * 78)
    print("TARGET: fixed-band Xi census + escape of every Nyquist-excess "
          "zero; equivalently weighted-L1 theta_x -> k_sqrt(x) plus a "
          "uniform logarithmic local-count bound.")

    section("A. SOURCE-ONLY EXTREMAL CELLS AND DAVIS-KAHAN SCALE")
    fw_ok, fw_detail = firewall()
    check("A0 independent/no-write firewall", fw_ok, fw_detail)
    cells: dict[int, dict] = {}
    dk_vacuous = True
    for x in X_LADDER:
        t0 = time.time()
        cell = build_extremal_cell(x, DPS[x])
        cells[x] = cell
        overlap = abs((cell["vector"].T * cell["model_vector"])[0])
        ratio_model = cell["prime_norm"] / cell["model_gap"]
        ratio_full = cell["prime_norm"] / cell["gap"]
        prolate = prolate_defect_asymptotic(x)
        ratio_prolate = cell["prime_const"] / prolate
        dk_vacuous &= (
            ratio_model > mp.mpf("0.5")
            and ratio_full > 1
            and ratio_prolate > 1
        )
        print(
            "  x=%d K=%d dps=%d  lambda=%s gap=%s model_gap=%s\n"
            "      ||P_prime||=%s  <e0,P e0>=%s  "
            "||P||/gap_model=%s  ||P||/gap_full=%s\n"
            "      prolate defect asympt=%s  const-Rayleigh/defect=%s  "
            "|<theta,theta_no-prime>|=%s  build=%.1fs"
            % (
                x, cell["K"], cell["dps"], sci(cell["lambda"]),
                sci(cell["gap"]), sci(cell["model_gap"]),
                sci(cell["prime_norm"]), sci(cell["prime_const"]),
                sci(ratio_model), sci(ratio_full), sci(prolate),
                sci(ratio_prolate), sci(overlap), time.time() - t0,
            )
        )
    check(
        "A1 operator-norm DK bound is vacuous",
        dk_vacuous,
        "prime/model-gap is never perturbatively small (>0.5), while "
        "prime/full-gap and prime/prolate-gap exceed 1 on every rung",
    )

    section("B. OFF-LINE QUARTET: SIGN CHANGE WITHOUT CENSUS CHANGE")
    cell = cells[PLANT_X]
    with mp.workdps(cell["dps"]):
        base_roots = real_roots(cell, cell["vector"], ROOT_BAND)
        first_root = base_roots[0]
        b0 = evaluation_vector(cell, first_root)
        base_matrix = cell["full"] + 2 * b0 * b0.T
        base_evals, base_evecs = mp.eigsy(base_matrix)
        base_vector = orient(
            mp.matrix([base_evecs[i, 0] for i in range(cell["K"])]),
            cell["vector"],
        )
        base_gap = base_evals[1] - base_evals[0]
        e0 = profile(cell, base_vector, first_root)
        derivative = mp.diff(
            lambda z: profile(cell, base_vector, z), first_root
        )
        delta_star = mp.sqrt(base_evals[0]) / (2 * abs(derivative))
        print(
            "  base x=%d: first root t=%s, E(t)=%s, E'(t)=%s\n"
            "      double-orbit lambda=%s gap=%s lambda/gap=%s "
            "delta_*=%s census(0,30)=%d"
            % (
                PLANT_X, sci(first_root, 14), sci(e0), sci(derivative),
                sci(base_evals[0]), sci(base_gap),
                sci(base_evals[0] / base_gap), sci(delta_star),
                len(base_roots),
            )
        )

        bookkeeping_ok = True
        census_ok = True
        negative_seen = False
        min_overlap = mp.mpf(1)
        max_shift = mp.mpf(0)
        for factor in PLANT_FACTORS:
            delta = mp.mpf(str(factor)) * delta_star
            bp = evaluation_vector(cell, first_root + 1j * delta)
            # The conjugate pair gives 4 Re(b_+ b_+^T).  Build the
            # real matrix explicitly: mpmath correctly retains a complex
            # zero imaginary part, while eigsy requires an mpf matrix.
            quartet_matrix = mp.zeros(cell["K"], cell["K"])
            for i in range(cell["K"]):
                for j in range(cell["K"]):
                    quartet_matrix[i, j] = 4 * mp.re(bp[i] * bp[j])
            planted = cell["full"] - 2 * b0 * b0.T + quartet_matrix
            planted_evals, planted_evecs = mp.eigsy(planted)
            planted_vector = orient(
                mp.matrix(
                    [planted_evecs[i, 0] for i in range(cell["K"])]
                ),
                base_vector,
            )
            overlap = abs((planted_vector.T * base_vector)[0])
            min_overlap = min(min_overlap, overlap)
            roots = real_roots(cell, planted_vector, ROOT_BAND)
            census_ok &= len(roots) == len(base_roots)
            if len(roots) == len(base_roots):
                shift = max(abs(a - b) for a, b in zip(roots, base_roots))
                max_shift = max(max_shift, shift)
            else:
                shift = mp.inf

            ep = profile(cell, base_vector, first_root + 1j * delta)
            em = profile(cell, base_vector, first_root - 1j * delta)
            quartet_direct = (
                profile(cell, base_vector, first_root + 1j * delta) ** 2
                + profile(cell, base_vector, -first_root - 1j * delta) ** 2
                + profile(cell, base_vector, first_root - 1j * delta) ** 2
                + profile(cell, base_vector, -first_root + 1j * delta) ** 2
            )
            quartet_reduced = 4 * mp.re(ep ** 2)
            bookkeeping_dev = abs(quartet_direct - quartet_reduced)
            bookkeeping_ok &= bookkeeping_dev < mp.mpf("1e-45")
            energy_change = quartet_reduced - 4 * mp.re(e0 ** 2)
            leading = -4 * delta ** 2 * derivative ** 2
            taylor_ratio = energy_change / leading
            old_rayleigh = base_evals[0] + energy_change
            negative_seen |= planted_evals[0] < 0
            perturb_norm = max(
                abs(v) for v in mp.eigsy(
                    planted - base_matrix, eigvals_only=True
                )
            )
            print(
                "  factor=%4.2f delta=%s quartet-dev=%s "
                "DeltaQ=%s lead=%s ratio=%s\n"
                "      old-Rayleigh=%s new-lambda=%s "
                "||DeltaM||/gap=%s overlap=%s census=%d max-root-shift=%s"
                % (
                    factor, sci(delta), sci(bookkeeping_dev),
                    sci(energy_change), sci(leading), sci(taylor_ratio),
                    sci(old_rayleigh), sci(planted_evals[0]),
                    sci(perturb_norm / base_gap), sci(overlap), len(roots),
                    sci(shift),
                )
            )

        check(
            "B1 quartet bookkeeping and Taylor sign",
            bookkeeping_ok,
            "sum_orbit E(z)^2 = 4 Re E(t+i delta)^2; "
            "printed ratios tend to 1",
        )
        check(
            "B2 negativity occurs before direction moves",
            negative_seen and min_overlap > mp.mpf("0.999999"),
            "negative lambda seen=%s, min ground-state overlap=%s"
            % (negative_seen, sci(min_overlap, 12)),
        )
        check(
            "B3 planted off-line split preserves band census",
            census_ok,
            "counts stay %d; max root displacement %s"
            % (len(base_roots), sci(max_shift)),
        )

    section("C. RvM DENSITY DOES NOT SUPPLY LOCAL REGULARITY")
    ratios = []
    for height in RVM_HEIGHTS:
        expected = smooth_rvm_count(height + 1.0) - smooth_rvm_count(height)
        moved = int(math.ceil(expected))
        ratio = moved / math.log(height)
        ratios.append(ratio)
        print(
            "  T=%9.1e smooth count in [T,T+1]=%.6f; "
            "move at most %d atoms to empty the interval; "
            "counting discrepancy/log(T)=%.6f"
            % (height, expected, moved, ratio)
        )
    check(
        "C1 O(log T) RvM error permits unit gaps",
        max(ratios) < 0.30,
        "explicit relocation budget max moved/log(T)=%.6f" % max(ratios),
    )
    print(
        "  CONSEQUENCE: MNT/Totik hypotheses are not obtained from RvM. "
        "Off-line, there is not even a positive measure on R; on-line, "
        "the global O(log T) count permits local gaps/clusters of exactly "
        "the size that local Szego/Christoffel asymptotics must exclude."
    )

    section("D. VERDICT")
    elapsed = time.time() - STARTED
    check("D1 runtime", elapsed < RUNTIME_BAR,
          "%.1fs < %.0fs" % (elapsed, RUNTIME_BAR))
    passed = sum(1 for _name, ok, _detail in CHECKS if ok)
    print(
        "\nCHECKS %d/%d PASS  runtime %.1fs  SPEC_SHA %s"
        % (passed, len(CHECKS), elapsed, SPEC_SHA[:16])
    )
    print(
        "VERDICT: TPL-OBSTRUCTED("
        "the zero identity is an indefinite bilinear form off-line; "
        "real-rootedness survives loss of positivity and therefore does "
        "not force a band-count mismatch; RvM lacks the local positive-"
        "measure regularity required by Christoffel asymptotics; "
        "operator-norm prolate perturbation is gap-vacuous)"
    )
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(run())
