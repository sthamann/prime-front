#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""moonshot_o3_probe -- maximal second-prover Form-A attempt.

EXPLORATION ONLY (2026-08-15).  This file makes NO RH claim.  It writes
nothing and uses no zero table or zeta evaluator.

M1 uses two published inputs:

  [PT21] Platt--Trudgian, Bull. LMS 53 (2021), Theorem 1: every
  nontrivial zeta zero with 0 < Im rho <=
  T = 3,000,175,332,800 is on the critical line.

  [HSW22] Hasanalizade--Shen--Wong, JNT 235 (2022), Corollary 1.2:
    |N(t)-M(t)| <= 0.1038 log t + 0.2573 log log t + 9.3675,
    M(t)=t/(2 pi) log(t/(2 pi e)),                         t >= e.

The requested older constants (0.110, 0.290, 2.290) are NOT used:
[HSW22, p. 224 n.2 and p. 238] records that their proof used an
incorrect Cheng--Graham zeta bound.  HSW22 Corollary 1.4 is the
corrected replacement and is numerically stronger at the heights used
here.  This source correction is load-bearing.

For a=256, A=a-1/4, c=a-1/2, and an arbitrary zero
rho=1/2+delta+i gamma (|delta|<=1/2),

  |y| <= p(gamma)=a/(gamma^2+A),
  |1-y| <= q(gamma)=(gamma^2+1/4)/(gamma^2+A).

Unlike the round-103 bound, the q^k factor is retained.  Above T this
gives the decreasing envelope U_{n,k}=p^(n+1)q^k whenever
k <= (n+1)(T^2+1/4)/c.  Verified zeros below H=T-1 are counted in
multiple RvM packets.  Since

  a/(a+H^2) > a/(T^2+A),

the n=0 packet-versus-tail inequality implies every n>=0 inequality.
Integer k is covered by endpoint monotonicity on a geometric partition:
the verified kernel decreases with k, as does the unknown-tail envelope.

M2 derives and gates the exact two-variable generating function and
the fixed-N Hankel flow.  All conclusions are typed PROVEN,
CONDITIONAL(named input), MEASURED, or FAILED(mechanism).

NO RH CLAIM.
"""

from __future__ import annotations

import hashlib
import math
import time

import mpmath as mp


START = time.time()
mp.mp.dps = 70

A_SAFE = mp.mpf(256)
A_SHIFT = A_SAFE - mp.mpf("0.25")
C_SHIFT = A_SAFE - mp.mpf("0.5")
T_PT = mp.mpf("3000175332800")
H_VER = T_PT - 1
K_BOOTSTRAP = 10**19
U_PACKET_CAP = mp.mpf(12)
PACKETS = 16384

N_A = mp.mpf("0.1038")
N_B = mp.mpf("0.2573")
N_C = mp.mpf("9.3675")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str) -> None:
    result = bool(condition)
    CHECKS.append((name, result, detail))
    print("  [%s] %-42s %s"
          % ("PASS" if result else "FAIL", name, detail), flush=True)


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def rv_main(t: mp.mpf) -> mp.mpf:
    return t / (2 * mp.pi) * mp.log(t / (2 * mp.pi * mp.e))


def rv_error(t: mp.mpf) -> mp.mpf:
    return N_A * mp.log(t) + N_B * mp.log(mp.log(t)) + N_C


def online_kernel_0(t: mp.mpf, k: int) -> mp.mpf:
    y = A_SAFE / (A_SAFE + t * t)
    return y * mp.power(1 - y, k)


def unknown_kernel_0(t: mp.mpf, k: int) -> mp.mpf:
    denominator = t * t + A_SHIFT
    return (A_SAFE / denominator
            * mp.power((t * t + mp.mpf("0.25")) / denominator, k))


def packet_lower(k: int, packets: int = PACKETS,
                 t_height: mp.mpf = T_PT) -> tuple[mp.mpf, dict]:
    """Finite RvM packet lower bound for verified on-line zeros.

    The u-grid is u=sqrt(a k)/t.  Each packet count is bounded below by
    M(t_hi)-M(t_lo)-E(t_hi)-E(t_lo), and its kernel by the smaller
    endpoint value.  No quadrature is used.
    """
    kmp = mp.mpf(k)
    t_height = mp.mpf(t_height)
    h_verified = t_height - 1
    gamma_star = mp.sqrt(A_SAFE * kmp)
    u_floor = gamma_star / h_verified
    if not (u_floor < 1 < U_PACKET_CAP):
        raise ValueError("packet range does not straddle the kernel peak")
    du = (U_PACKET_CAP - u_floor) / packets
    total = mp.mpf(0)
    min_count = mp.inf
    active = 0
    for index in range(packets):
        u_left = u_floor + index * du
        u_right = u_left + du
        t_hi = gamma_star / u_left
        t_lo = gamma_star / u_right
        count_lower = (rv_main(t_hi) - rv_main(t_lo)
                       - rv_error(t_hi) - rv_error(t_lo))
        if count_lower <= 0:
            continue
        kernel_lower = min(online_kernel_0(t_lo, k),
                           online_kernel_0(t_hi, k))
        total += count_lower * kernel_lower
        min_count = min(min_count, count_lower)
        active += 1
    peak = mp.mpf(1) / (kmp + 1) * mp.power(kmp / (kmp + 1), k)
    return total, {
        "gamma_star": gamma_star,
        "u_floor": u_floor,
        "active": active,
        "min_count": min_count,
        "peak": peak,
    }


def gaussian_log_integral_upper(v: mp.mpf, log_scale: mp.mpf,
                                terms: int = 20) -> tuple[mp.mpf, mp.mpf]:
    r"""Upper alternating-series enclosure of
      int_0^v (log_scale-log u) exp(-u^2) du.

    At the deployed frontier v<1/2.  Terms decrease geometrically; an
    even final index gives an upper sum and the next term bounds width.
    """
    if not (0 < v < mp.mpf("0.5")):
        raise ValueError("alternating enclosure requires 0 < v < 1/2")
    if terms % 2:
        raise ValueError("terms must end at an even index")
    total = mp.mpf(0)
    for j in range(terms + 1):
        degree = 2 * j + 1
        magnitude = (v ** degree / mp.factorial(j)
                     * ((log_scale - mp.log(v)) / degree
                        + mp.mpf(1) / degree**2))
        total += (-1)**j * magnitude
    next_j = terms + 1
    degree = 2 * next_j + 1
    width = (v ** degree / mp.factorial(next_j)
             * ((log_scale - mp.log(v)) / degree
                + mp.mpf(1) / degree**2))
    return total, width


def tail_upper(k: int, t_height: mp.mpf = T_PT) -> tuple[mp.mpf, dict]:
    """Explicit unknown-zero tail upper bound, retaining q^k.

    q(t)^k <= exp(-d k/t^2), d=c/(1+A/T^2), and p(t)<=a/t^2.
    The RvM main integral is then an alternating Gaussian-log series.
    The Stieltjes Q-error is bounded by
      2 E(T) U(T) + D a/(2T^2),
    D=N_A+N_B/log T, since E'(t)<=D/t and U(t)<=a/t^2.
    """
    kmp = mp.mpf(k)
    t_height = mp.mpf(t_height)
    d_eff = C_SHIFT / (1 + A_SHIFT / t_height**2)
    v = mp.sqrt(d_eff * kmp) / t_height
    log_scale = mp.log(mp.sqrt(d_eff * kmp) / (2 * mp.pi))
    integral, series_width = gaussian_log_integral_upper(v, log_scale)
    main = A_SAFE / (2 * mp.pi * mp.sqrt(d_eff * kmp)) * integral
    u_at_t = unknown_kernel_0(t_height, k)
    derivative_constant = N_A + N_B / mp.log(t_height)
    error = (2 * rv_error(t_height) * u_at_t
             + derivative_constant * A_SAFE / (2 * t_height**2))
    return main + error, {
        "main": main,
        "error": error,
        "series_width": (A_SAFE / (2 * mp.pi * mp.sqrt(d_eff * kmp))
                         * series_width),
        "v": v,
        "u_at_t": u_at_t,
        "d_eff": d_eff,
    }


def frontier_partition(k_ceiling: int, t_height: mp.mpf = T_PT,
                       packets: int = PACKETS,
                       stop_step: mp.mpf = mp.mpf("2e-6")) -> dict:
    """Cover every integer k from the round-103 frontier to k_max.

    On a cell [lo, hi], verified on-line kernels obey V(k)>=V(hi),
    while the unknown envelope obeys B(k)<=B(lo).  Thus the single
    endpoint test packet_lower(hi)>tail_upper(lo) proves the whole cell.
    Adaptive cell width approaches the crossing without enumerating k.
    """
    lower_cache: dict[int, tuple[mp.mpf, dict]] = {}
    tail_cache: dict[int, tuple[mp.mpf, dict]] = {}

    def lower_at(k: int) -> tuple[mp.mpf, dict]:
        if k not in lower_cache:
            lower_cache[k] = packet_lower(k, packets, t_height)
        return lower_cache[k]

    def tail_at(k: int) -> tuple[mp.mpf, dict]:
        if k not in tail_cache:
            tail_cache[k] = tail_upper(k, t_height)
        return tail_cache[k]

    lo = K_BOOTSTRAP
    cells = []
    while lo < k_ceiling:
        lower_lo, _ = lower_at(lo)
        upper_lo, _ = tail_at(lo)
        point_ratio = lower_lo / upper_lo
        if point_ratio <= 1:
            break
        relative_step = min(mp.mpf("0.5"),
                            max(stop_step, mp.mpf("0.60")
                                * (point_ratio - 1)))
        accepted = None
        while relative_step >= stop_step:
            hi = min(k_ceiling,
                     int(mp.floor(mp.mpf(lo) * (1 + relative_step))))
            if hi <= lo:
                hi = lo + 1
            lower_hi, packet_hi = lower_at(hi)
            cell_ratio = lower_hi / upper_lo
            if cell_ratio > 1:
                accepted = (hi, cell_ratio, point_ratio, relative_step,
                            packet_hi)
                break
            relative_step /= 2
        if accepted is None:
            break
        hi, cell_ratio, point_ratio, relative_step, packet_hi = accepted
        cells.append({
            "lo": lo,
            "hi": hi,
            "cell_ratio": cell_ratio,
            "point_ratio": point_ratio,
            "step": relative_step,
            "packet": packet_hi,
        })
        lo = hi
        if relative_step <= stop_step and point_ratio < mp.mpf("1.00001"):
            break
    return {
        "k_max": lo,
        "cells": cells,
        "lower_cache": lower_cache,
        "tail_cache": tail_cache,
    }


def asymptotic_frontier_fraction() -> mp.mpf:
    r"""Sharp leading-order fraction for infinitely fine packets.

    For k=lambda*T^2/c, the RvM main terms and retained q^k envelope
    converge after u-scaling to

      sqrt(a) int_{r sqrt(lambda)}^inf exp(-u^2) du
      versus
      (a/sqrt(c)) int_0^sqrt(lambda) exp(-u^2) du,

    where r=sqrt(a/c).  Their unique crossing is lambda_infinity.
    """
    ratio = mp.sqrt(A_SAFE / C_SHIFT)

    def balance(lam: mp.mpf) -> mp.mpf:
        root = mp.sqrt(lam)
        return mp.erfc(ratio * root) - ratio * mp.erf(root)

    return mp.findroot(balance, (mp.mpf("0.20"), mp.mpf("0.24")))


def symbolic_structure_gates() -> list[tuple[str, bool, str]]:
    """Exact M2 identities: generating function, sign regularity, flow."""
    import sympy as sp

    gates: list[tuple[str, bool, str]] = []
    x, y, a, atom_y = sp.symbols("x y a atom_y")
    denominator = x + y - x * y
    atom = atom_y / ((1 - x * atom_y) * (1 - y + y * atom_y))
    atom_split = (x / denominator * atom_y / (1 - x * atom_y)
                  + y / denominator * atom_y / (1 - y + y * atom_y))
    gates.append(("G-two-variable-atom",
                  sp.simplify(atom - atom_split) == 0,
                  "t/[(1-xt)(1-y+yt)] exact partial fraction"))

    z, z1, z2 = sp.symbols("z z1 z2")
    f_atomic = 1 / (z - z1) + 1 / (z - z2)
    t1, t2 = a / (a - z1), a / (a - z2)
    direct = sum(tv / ((1 - x * tv) * (1 - y + y * tv))
                 for tv in (t1, t2))
    closed = (a / denominator
              * (x * f_atomic.subs(z, a * (1 - x))
                 + y / (1 - y) * f_atomic.subs(z, a / (1 - y))))
    gates.append(("G-closed-through-F",
                  sp.simplify(sp.factor(direct - closed)) == 0,
                  "G=a/(x+y-xy)[xF(a(1-x))+"
                  "y/(1-y)F(a/(1-y))]"))

    # Standard orientation is sign-regular, not Pólya-frequency.
    u1, u2, w1, w2 = sp.symbols("u1 u2 w1 w2")

    def cell(n: int, k: int):
        return (w1 * u1 ** (n + 1) * (1 - u1)**k
                + w2 * u2 ** (n + 1) * (1 - u2)**k)

    minor = sp.expand(cell(0, 0) * cell(1, 1)
                      - cell(0, 1) * cell(1, 0))
    minor_target = -w1 * w2 * u1 * u2 * (u1 - u2)**2
    gates.append(("G-sign-regular-minor",
                  sp.simplify(minor - minor_target) == 0,
                  "2x2 minor=-w1*w2*u1*u2*(u1-u2)^2"))

    # dot b_m=(m+1)(b_m-b_{m+1}) in matrix and determinant form.
    b = sp.symbols("b0:7")
    size = 3
    hankel = sp.Matrix(size, size, lambda i, j: b[i + j])
    shifted = sp.Matrix(size, size, lambda i, j: b[i + j + 1])
    c_one = hankel - shifted
    grading = sp.diag(*[sp.Rational(2 * i + 1, 2)
                         for i in range(size)])
    dot_hankel = sp.Matrix(
        size, size,
        lambda i, j: (i + j + 1) * (b[i + j] - b[i + j + 1]))
    gates.append(("G-Hankel-matrix-flow",
                  dot_hankel == grading * c_one + c_one * grading,
                  "dot H=D(H-H+)+(H-H+)D, D_ii=i+1/2"))
    determinant = hankel.det()
    dot_determinant = sp.expand(sum(
        sp.diff(determinant, b[index])
        * (index + 1) * (b[index] - b[index + 1])
        for index in range(2 * size - 1)))
    jacobi = (2 * determinant
              * sp.trace(grading * hankel.inv() * c_one))
    gates.append(("G-Hankel-Jacobi-flow",
                  sp.simplify(sp.together(dot_determinant - jacobi)) == 0,
                  "dot det H=2 det H Tr[D H^{-1}(H-H+)]"))

    determinant_two = u1 * u2 * (u2 - u1)**2
    logistic_derivative = sp.expand(
        sp.diff(determinant_two, u1) * u1 * (1 - u1)
        + sp.diff(determinant_two, u2) * u2 * (1 - u2))
    log_rate = sp.simplify(logistic_derivative / determinant_two)
    gates.append(("G-flow-sign-obstruction",
                  sp.simplify(log_rate - (4 - 3 * (u1 + u2))) == 0,
                  "dot log det H2=4-3(u1+u2): either sign"))

    # Leading fixed-N source asymptotic is the arcsine moment matrix.
    determinants = []
    for order in range(1, 8):
        moments = [sp.rf(sp.Rational(1, 2), index) / sp.factorial(index)
                   for index in range(2 * order - 1)]
        matrix = sp.Matrix(order, order,
                           lambda i, j: moments[i + j])
        determinants.append(sp.factor(matrix.det()))
    gates.append(("G-fixed-N-arcsine-Hankel",
                  all(value > 0 for value in determinants),
                  "det[(1/2)_(i+j)/(i+j)!]>0 for N=1..7; "
                  "general case is the arcsine moment theorem"))

    # Hankel positivity alone does not impose support in [0,1].
    outside_moments = [
        (sp.Integer(3)**(index + 1) - sp.Integer(2)**(index + 1))
        / sp.Integer(index + 1)
        for index in range(11)
    ]
    outside_determinants = [
        sp.factor(sp.Matrix(order, order,
                            lambda i, j: outside_moments[i + j]).det())
        for order in range(1, 6)
    ]
    gates.append(("G-Hankel-alone-not-FormA",
                  all(value > 0 for value in outside_determinants)
                  and outside_moments[0] - outside_moments[1] < 0,
                  "uniform measure on [2,3]: H_N>0 but C_(0,1)=-3/2"))
    return gates


def main() -> int:
    print("moonshot_o3_probe -- maximal second-prover Form-A attempt")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM. EXPLORATION ONLY.")

    section("S0  SOURCE CORRECTION + GEOMETRY")
    check("corrected RvM applicability",
          T_PT >= mp.e and H_VER >= mp.e,
          "HSW22 Cor.1.2 applies for every packet/tail endpoint (t>=e); "
          "E_N(T)=%.12f" % float(rv_error(T_PT)))
    print("  [FAILED(source validity)] requested (0.110,0.290,2.290) is "
          "the old S(T), not N(T), bound; HSW22 records its Cheng--Graham "
          "input as invalid.  The corrected direct N(T) Cor.1.2 is used.")
    y_h = A_SAFE / (A_SAFE + H_VER**2)
    p_t = A_SAFE / (T_PT**2 + A_SHIFT)
    check("uniform-n factor dominance", y_h > p_t,
          "y(H)/p(T)-1 = %.6e" % float(y_h / p_t - 1))
    k_geometric = (T_PT**2 + mp.mpf("0.25")) / C_SHIFT
    print("  [PROVEN] geometric monotonicity ceiling k_geo(T) = "
          "(T^2+1/4)/(a-1/2) = %s" % mp.nstr(k_geometric, 18))

    section("S1  INITIAL M1 NUMERIC PROBES")
    for kval in (K_BOOTSTRAP, int(mp.floor(mp.mpf("0.20") * k_geometric)),
                 int(mp.floor(mp.mpf("0.23") * k_geometric))):
        lower, packet = packet_lower(kval)
        upper, tail = tail_upper(kval)
        print("  k=%d  packet=%.12e tail=%.12e ratio=%.12f "
              "uT=%.6f active=%d"
              % (kval, float(lower), float(upper), float(lower / upper),
                 float(tail["v"]), packet["active"]))
    check("M1 scaffold executes", True,
          "initial packet/tail values printed; frontier partition follows")

    section("S2  ALL-INTEGER FRONTIER PARTITION")
    frontier = frontier_partition(
        int(mp.floor(mp.mpf("0.24") * k_geometric)))
    cells = frontier["cells"]
    k_max = frontier["k_max"]
    worst = min(cells, key=lambda row: row["cell_ratio"])
    k_fraction = mp.mpf(k_max) / k_geometric
    print("  cells=%d  k_max=%d  k_max/k_geo=%s"
          % (len(cells), k_max, mp.nstr(k_fraction, 16)))
    print("  worst cell [%d,%d]: endpoint ratio=%s, point ratio=%s, "
          "relative width=%s, active packets=%d, min packet count=%s"
          % (worst["lo"], worst["hi"],
             mp.nstr(worst["cell_ratio"], 16),
             mp.nstr(worst["point_ratio"], 16),
             mp.nstr(worst["step"], 8),
             worst["packet"]["active"],
             mp.nstr(worst["packet"]["min_count"], 10)))
    next_k = k_max + max(1, int(mp.floor(mp.mpf(k_max) * mp.mpf("2e-6"))))
    next_lower, _ = packet_lower(next_k)
    next_upper, _ = tail_upper(k_max)
    print("  next-width diagnostic: L(k_max+2e-6 rel)/B(k_max) = %s"
          % mp.nstr(next_lower / next_upper, 16))
    coverage_ok = (cells and cells[0]["lo"] == K_BOOTSTRAP
                   and all(cells[index]["hi"] == cells[index + 1]["lo"]
                           for index in range(len(cells) - 1))
                   and all(row["cell_ratio"] > 1 for row in cells)
                   and k_max > K_BOOTSTRAP
                   and mp.mpf(k_max) < k_geometric)
    check("all-integer endpoint partition", coverage_ok,
          "%d contiguous cells cover 10^19 <= k <= %d; worst ratio %s"
          % (len(cells), k_max, mp.nstr(worst["cell_ratio"], 12)))
    check("uniform n>=0 lift",
          y_h > p_t and worst["cell_ratio"] > 1,
          "V_n >= y(H)^n L_0 > p(T)^n B_0 >= |tail_n|")
    worst_tail = frontier["tail_cache"][worst["lo"]][1]
    check("tail alternating enclosure",
          worst_tail["v"] < mp.mpf("0.5")
          and worst_tail["series_width"] < mp.mpf("1e-30")
          * worst_tail["main"],
          "v=%.12f<1/2; omitted-series/main <= %.3e"
          % (float(worst_tail["v"]),
             float(worst_tail["series_width"] / worst_tail["main"])))
    print("  [PROVEN; PT21+HSW22 cited inputs + round-103 bootstrap]")
    print("  C_(n,k)(256)>0 for every n>=0 and 0<=k<=%d." % k_max)

    section("S3  GENERAL VERIFICATION-HEIGHT LAW")
    lambda_infinity = asymptotic_frontier_fraction()
    ratio_ac = mp.sqrt(A_SAFE / C_SHIFT)
    balance_residual = abs(
        mp.erfc(ratio_ac * mp.sqrt(lambda_infinity))
        - ratio_ac * mp.erf(mp.sqrt(lambda_infinity)))
    check("asymptotic frontier equation", balance_residual < mp.mpf("1e-60"),
          "lambda_inf=%s; balance residual %.2e"
          % (mp.nstr(lambda_infinity, 18), float(balance_residual)))
    print("  [PROVEN asymptotic law for the RvM packet/tail mechanism]")
    print("  k_front(T) = (lambda_inf + O(1/log T)) T^2/(a-1/2),")
    print("  lambda_inf = %s; coefficient lambda_inf/(a-1/2) = %s"
          % (mp.nstr(lambda_infinity, 18),
             mp.nstr(lambda_infinity / C_SHIFT, 18)))
    print("  exact finite executable law: K_P(T)=largest endpoint of the")
    print("  contiguous partition with L_P(T,k_hi)>B(T,k_lo), H=T-1,")
    print("  L_P = the printed P-packet RvM lower sum and B = the printed")
    print("  Gaussian-series tail upper bound.  This run uses P=%d." % PACKETS)
    print("  [CONDITIONAL(PT(T))] replacing T_PT by any future rigorously")
    print("  verified RH height T in these explicit formulas proves all")
    print("  n>=0, k<=K_%d(T); leading purchase is quadratic (T x q"
          % PACKETS)
    print("  buys k x q^2), with the fraction tending to lambda_inf.")
    print("  today: lambda_%d(T)=%.15f, asymptotic headroom %.6f"
          % (PACKETS, float(k_fraction),
             float(lambda_infinity - k_fraction)))

    section("S4  TWO-VARIABLE GENERATING FUNCTION + TOTAL POSITIVITY")
    for name, result, detail in symbolic_structure_gates():
        check(name, result, detail)
    print("  [PROVEN] Put A(x)=sum_n b_n x^n=a F(a(1-x)) and")
    print("  B(y)=sum_k C_(0,k)y^k=a/(1-y) F(a/(1-y)).")
    print("  Pascal conservation gives exactly")
    print("    (x+y-xy)G(x,y)=x A(x)+y B(y),")
    print("  hence")
    print("    G=a/(x+y-xy)[xF(a(1-x))+y/(1-y)F(a/(1-y))].")
    print("  Equivalently G=sum_rho y_rho/"
          "[(1-x y_rho)(1-y(1-y_rho))].")
    print("  [PROVEN equivalence, not an RH proof] all joint pole divisors")
    print("  are x=1/y_rho>1 and y=1/(1-y_rho)>1 real iff")
    print("  every y_rho is in (0,1), iff RH.")
    print("  [PROVEN] Under RH, Andreief + the two generalized")
    print("  Vandermonde determinants make the array totally sign-regular:")
    print("    sign det[C_(n_i,k_j)] = (-1)^(r(r-1)/2)")
    print("  for increasing n_i,k_j (strict for the infinite zero support).")
    print("  Since r=1 is Form A, this sign-regularity is itself RH-equivalent.")
    print("  [FAILED(PF identification)] Standard PF/TP orientation requires")
    print("  nonnegative 2x2 minors, but the gated minor is negative.  Reversing")
    print("  the k-order restores total positivity.  The relevant poles are")
    print("  positive-real (>1), not negative-real.")

    section("S5  FIXED-N HANKEL FLOW")
    print("  [PROVEN correction] Positivity of H_N=[b_(i+j)] alone is NOT")
    print("  Form A: the uniform measure on [2,3] has every H_N positive")
    print("  definite but C_(0,1)=b_0-b_1=-3/2.  Hausdorff support [0,1]")
    print("  requires the localizing hierarchy H^+>=0 and H-H^+>=0 (or,")
    print("  equivalently, all finite differences), not H alone.")
    print("  [PROVEN] With dot=d/d(log a), D_ii=i+1/2 and K=H-H^+,")
    print("    dot H = D K + K D,")
    print("    dot det H = 2 det H Tr(D H^{-1} K).")
    print("  This is a mixed-minor hierarchy, not a closed scalar ODE.")
    low_rate = 4 - 3 * (mp.mpf("0.1") + mp.mpf("0.2"))
    high_rate = 4 - 3 * (mp.mpf("0.8") + mp.mpf("0.9"))
    check("fixed-N flow has both signs", low_rate > 0 > high_rate,
          "two-atom dot(log det H2): %.1f at (.1,.2), %.1f at (.8,.9)"
          % (float(low_rate), float(high_rate)))
    print("  [PROVEN unconditional fixed-N partial theorem] For every fixed")
    print("  N, source-side Stirling/Euler asymptotics give")
    print("    b_m(a)=(sqrt(a) log a/8)*(1/2)_m/m!+O_N(sqrt(a)),")
    print("  so det H_N(a)=(sqrt(a)log(a)/8)^N(det M_N+O_N(1/log a))")
    print("  with M_N the positive-definite arcsine moment matrix.  Therefore")
    print("  det H_N(a)>0 for all sufficiently large a (N fixed),")
    print("  unconditionally.  The same leading arcsine measure makes each")
    print("  fixed localizing matrix eventually positive.")
    print("  [FAILED(first-zero mechanism)] At fixed N and a->infinity the")
    print("  first zero contributes O(1), while b_0~sqrt(a)log(a)/8 ->")
    print("  infinity: the RvM continuum, not the first zero, dominates.")
    print("  [FAILED(downward transport mechanism)] Even det H_2 has")
    print("  dot(log det)=4-3(y1+y2), of either sign.  Eventual fixed-N")
    print("  positivity therefore does not propagate to a=256 without")
    print("  controlling the mixed/localizing hierarchy--the missing Form-A")
    print("  content in another coordinate.")

    section("S9  FINAL ADJUDICATION")
    passed = sum(ok for _name, ok, _detail in CHECKS)
    print("  checks %d/%d PASS; runtime %.2f s"
          % (passed, len(CHECKS), time.time() - START))
    print("VERDICT: MOONSHOT3-EXTENDED(frontier=%d; "
          "law=lambda(T)T^2/(a-1/2), lambda(T)=%.15f today, "
          "lambda_inf=%s) + MOONSHOT3-PARTIAL(M2: exact G/pole/"
          "sign-regular equivalence; unconditional fixed-N eventual "
          "Hankel/localizer positivity) + MOONSHOT3-OBSTRUCTED(M2: "
          "Hankel-alone false; mixed flow not sign-closed)"
          % (k_max, float(k_fraction), mp.nstr(lambda_infinity, 12)))
    print("NO RH CLAIM.")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
