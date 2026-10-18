#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""moonshot_sol_probe -- maximal Form-A proof attempt.

EXPLORATION ONLY (2026-08-15).  This probe makes NO RH claim and writes
nothing.  It uses no zero table and calls no zeta evaluator.  Its two
external mathematical inputs are already-proved, explicitly named results:

  [PT] Platt--Trudgian, Bull. LMS 53 (2021), Theorem 1:
       every nontrivial zeta zero with
       0 < Im rho <= T = 3,000,175,332,800 is on Re rho = 1/2.
  [R]  Rosser, Amer. J. Math. 63 (1941), Theorem 19:
       |N(t)-F(t)| <= E(t), t >= 2, where
       F(t)=t/(2 pi) log(t/(2 pi e))+7/8 and
       E(t)=.137 log t+.443 log log t+1.588.

The first-zero isolation 14.1347 < gamma_1 < 14.1348 is also a classical
proved input.  Cited theorems are inputs to an unconditional theorem, not
unproved assumptions.

=======================================================================
FORM A ATTACK AND THE NEW PARTIAL THEOREM
=======================================================================
Put a=256, z_rho=(rho-1/2)^2, y_rho=a/(a-z_rho), and

  C_{n,k} = sum_{Im rho>0} y_rho^(n+1) (1-y_rho)^k.

The sum is absolutely convergent.  If rho=1/2+i gamma, its summand is

  K_{n,k}(gamma)
    = [a/(a+gamma^2)]^(n+1) [gamma^2/(a+gamma^2)]^k >= 0.

For an arbitrary zero rho=1/2+delta+i gamma, |delta|<=1/2,

  |y_rho| <= a/(gamma^2+a-1/4),             (GEO-1)
  |1-y_rho| = |z_rho|/|a-z_rho| <= 1.       (GEO-2)

Indeed Re(a-z_rho)>=a+gamma^2-1/4, and
|a-z_rho|^2-|z_rho|^2=a(a+2 gamma^2-2 delta^2)>0.

Rosser implies, for t>=T,

  N(t) <= t/(2 pi) log(t/(2 pi)).           (COUNT)

Writing A=a-1/4 and f_n(t)=[a/(A+t^2)]^(n+1), Stieltjes integration and
(COUNT) give the absolute unknown-zero tail bounds

  B_0(T) = a/pi [log(T/(2 pi))+1]/T,
  B_n(T) = a(n+1)/(2 pi n) [log(T/(2 pi))/T]
           [a/(T^2+A)]^n,                  n>=1.       (TAIL)

No location, phase, or on-line assumption is made above T.

For theta=k/(n+1), let g=sqrt(a theta), r=3/2 and I=[g/r,rg].
The on-line beta kernel is unimodal with maximum at g.  Put

  D = (1/2) min(r^2 exp(-r^2), r^-2 exp(-r^-2)).

At either endpoint gamma=cg, c in {1/r,r}, elementary
log(1+x)<=x and 1+x<=2x give

  K_{n,k}(cg) >= (D/theta)^(n+1),            theta>=25. (BETA)

For

  H(theta) = sqrt(a theta)(r-r^-1)/(2 pi)
             log(sqrt(a theta)/(2 pi r)),

Rosser gives #I >= H(theta)/2 once H(theta)>=4E(rg).  The ratio
H(theta)/(4E(rg)) is increasing for theta>=25 and already exceeds 1
at theta=25.  Every zero in I is on-line whenever rg<T, by [PT].

THEOREM [PROVEN, external-cited inputs [PT]+[R]].  At a=256,

  C_{n,k}(256) > 0  for every n>=0 and every integer 0<=k<=10^19.

Proof partition, all inequalities strict:

  (i) n=0, 0<=k<=24: the first on-line zero alone exceeds B_0.
 (ii) n=0, 25<=k<=10^19: #I times (BETA) is at least
          H(k)D/(2k).
      This lower bound decreases on [25,10^19]; at 10^19 it is
      8.913342...e-10, while B_0=7.575655...e-10.
(iii) n>=1 and theta<=40: the first zero gives
          [y_lo q_lo^40]^(n+1).
      Relative to B_n the ratio increases with n; its minimum is
      n=1, theta=40, where it is >335.
 (iv) n>=1 and 40<=theta<=10^19/(n+1): #I and (BETA) give
          H(theta)/2 [D/theta]^(n+1).
      Since D/(theta r_T)>833 on this rectangle, its ratio to B_n
      increases with n.  At n=1 it decreases with theta, so its
      minimum is theta=5e18, where the ratio is >1416.

Thus the theorem covers an infinite half-strip in n and ten quintillion
complete k-columns.  It does not touch the k->infinity quantifier and
therefore does not prove RH.  The same n=0 counted-zero mechanism reaches
only k<1.40544e19 with these deliberately elementary constants; that is a
failure of this bound, not a negative cell.

=======================================================================
THE EXACT PRIME-SIDE TRANSMUTATION AND WHY THE POSITIVE-WINDOW IDEA DIES
=======================================================================
The source formula is

  F(z)=F_arch(z)-sum_q Lambda(q)q^(-1/2) h_{log q}(z),
  h_u(z)=exp(-u sqrt(z))/(2 sqrt(z)).

Directly from C_{n,k}=sum_{j=0}^k(-1)^j binom(k,j)b_{n+j},

  C_{n,k}=(-1)^n a^(n+1) sum_{j=0}^k binom(k,j)
           a^j F^(n+j)(a)/(n+j)!.

Subordination,

  h_u(z)=1/(2 sqrt(pi)) int_0^inf t^(-1/2)
         exp(-zt-u^2/(4t)) dt,

turns each prime-power contribution into

  P_{n,k}(u;a)=a^(n+1)/(2 sqrt(pi)n!) int_0^inf
    t^(n-1/2)e^(-at-u^2/(4t)) Q_{n,k}(at) dt,

  Q_{n,k}(x) = _1F_1(-k;n+1;x)
             = n!k!/(n+k)! L_k^(n)(x).

STATUS [PROVEN]: the formula is exact.  STATUS [FAILED(mechanism)]:
for every k>=1, Q has k positive simple roots (the classical Laguerre
zero theorem); already Q_{n,1}(x)=1-x/(n+1).  Hence the positive spectral
Beta window becomes an oscillatory Laguerre window on the prime side.
There is no termwise-positive prime expansion to which one can compare
the Gamma term.  A domination argument could still exist, but positivity
of the Beta kernel alone supplies none.

=======================================================================
THE OTHER TWO SUGGESTED ROUTES
=======================================================================
STATUS [FAILED(Killip--Simon/Szego direction)].  For a normalized OPUC
measure dmu=w dm+dmu_s,

  product_j (1-|alpha_j|^2) = exp(int log w dm)

with both sides allowed to be zero.  The zero comb is pure point, so
w=0 a.e., the entropy is -infinity, and the only lower energy bound is
e>=0.  Riemann--von Mangoldt counting density is not the a.c. density w.
The probe prints a finite same-support witness: changing only positive
weights on 64 fixed atoms moves the depth-32 prediction energy from 1
to about 5.28e-5.  This measurement illustrates the structural theorem;
it is not used in the Form-A proof.

STATUS [PROVEN conditional statement, FAILED(proof route)].  Once all
Toeplitz/Krein sections are positive, compact-circle moment determinacy
forces each fixed interior Weyl disk to contract to a point.  But
"all sections positive" is localized Weil positivity itself.  The
contraction therefore consumes the whole open input and cannot prove it.

STATUS [FAILED(asymptotic transport)].  Complete monotonicity at any
finite a transports by the Moebius map for every finite a'>0 (both
directions after the Hausdorff representation).  Pointwise positivity
as a->infinity is not uniform in (n,k), however; the detecting indices
escape.  Infinity is not a finite base point from which the flow can be
inverted.

FINAL ENUM: MOONSHOT-PARTIAL(Form A; the 10^19-column Hausdorff theorem).
"""

from __future__ import annotations

import hashlib
import math
import time

import mpmath as mp
import sympy as sp


START = time.time()
mp.mp.dps = 80

A_SAFE = mp.mpf(256)
A_SHIFT = A_SAFE - mp.mpf("0.25")
T_PT = mp.mpf("3000175332800")
GAMMA1_LO = mp.mpf("14.1347")
GAMMA1_HI = mp.mpf("14.1348")
R_INTERVAL = mp.mpf(3) / 2
K_RECT = 10**19
THETA_SPLIT = mp.mpf(40)
ROSSER_A = mp.mpf("0.137")
ROSSER_B = mp.mpf("0.443")
ROSSER_C = mp.mpf("1.588")
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str) -> None:
    result = bool(condition)
    CHECKS.append((name, result, detail))
    print("  [%s] %-45s %s"
          % ("PASS" if result else "FAIL", name, detail))


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def rosser_error(t: mp.mpf) -> mp.mpf:
    return ROSSER_A * mp.log(t) + ROSSER_B * mp.log(mp.log(t)) + ROSSER_C


def count_half_lower(theta: mp.mpf) -> mp.mpf:
    gamma_star = mp.sqrt(A_SAFE * theta)
    return (gamma_star * (R_INTERVAL - 1 / R_INTERVAL) / (2 * mp.pi)
            * mp.log(gamma_star / (2 * mp.pi * R_INTERVAL)) / 2)


def count_main(theta: mp.mpf) -> mp.mpf:
    return 2 * count_half_lower(theta)


def tail_bound(n: int) -> mp.mpf:
    log_scale = mp.log(T_PT / (2 * mp.pi))
    if n == 0:
        return A_SAFE / mp.pi * (log_scale + 1) / T_PT
    ratio = A_SAFE / (T_PT**2 + A_SHIFT)
    return (A_SAFE * (n + 1) / (2 * mp.pi * n)
            * log_scale / T_PT * ratio**n)


def beta_endpoint_constant() -> mp.mpf:
    r = R_INTERVAL
    return mp.mpf("0.5") * min(r**2 * mp.exp(-r**2),
                               r**-2 * mp.exp(-r**-2))


def first_zero_lower(n: int, k: int) -> mp.mpf:
    y_lower = A_SAFE / (A_SAFE + GAMMA1_HI**2)
    q_lower = GAMMA1_LO**2 / (A_SAFE + GAMMA1_LO**2)
    return y_lower**(n + 1) * q_lower**k


def h_source(z: mp.mpf, u: mp.mpf) -> mp.mpf:
    return mp.exp(-u * mp.sqrt(z)) / (2 * mp.sqrt(z))


def h_cell_derivative(n: int, k: int, u: mp.mpf) -> mp.mpf:
    values = []
    for order in range(n, n + k + 1):
        derivative = mp.diff(lambda z: h_source(z, u), A_SAFE, order)
        values.append(A_SAFE**(order + 1) * (-1)**order
                      * derivative / mp.factorial(order))
    return mp.fsum((-1)**j * mp.binomial(k, j) * values[j]
                   for j in range(k + 1))


def h_cell_integral(n: int, k: int, u: mp.mpf) -> mp.mpf:
    prefactor = (A_SAFE**(n + 1)
                 / (2 * mp.sqrt(mp.pi) * mp.factorial(n)))

    def integrand(t: mp.mpf) -> mp.mpf:
        if t == 0:
            return mp.mpf(0)
        qpoly = mp.hyp1f1(-k, n + 1, A_SAFE * t)
        return (t**(mp.mpf(n) - mp.mpf("0.5"))
                * mp.exp(-A_SAFE * t - u**2 / (4 * t)) * qpoly)

    return prefactor * mp.quad(integrand,
                               [0, mp.mpf("0.005"), mp.mpf("0.02"),
                                mp.mpf("0.08"), mp.mpf("0.3"), mp.inf])


def levinson_energy(atom_count: int, tilt: float, depth: int) -> tuple[float, float]:
    angles = [2 * math.pi * j / atom_count for j in range(atom_count)]
    weights = [math.exp(tilt * math.cos(theta)) for theta in angles]
    total_weight = sum(weights)
    weights = [weight / total_weight for weight in weights]
    moments = [sum(weight * math.cos(order * theta)
                   for weight, theta in zip(weights, angles))
               for order in range(depth + 2)]
    phi = [1.0] + [0.0] * (depth + 1)
    phi_star = [1.0] + [0.0] * (depth + 1)
    energy = 1.0
    max_alpha = 0.0
    for order in range(depth):
        numerator = sum(phi[j] * moments[j + 1]
                        for j in range(order + 1))
        denominator = sum(phi_star[j] * moments[j]
                          for j in range(order + 1))
        alpha = numerator / denominator
        max_alpha = max(max_alpha, abs(alpha))
        energy *= 1.0 - alpha * alpha
        zphi = [0.0] + phi[:order + 1]
        padded_star = phi_star[:order + 1] + [0.0]
        phi[:order + 2] = [zphi[j] - alpha * padded_star[j]
                           for j in range(order + 2)]
        phi_star[:order + 2] = [padded_star[j] - alpha * zphi[j]
                                for j in range(order + 2)]
    return energy, max_alpha


def main() -> int:
    print("moonshot_sol_probe -- FORM A maximal proof attempt")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM. EXPLORATION ONLY.")

    section("S1  EXTERNAL-INPUT ARITHMETIC + UNKNOWN-ZERO TAIL")
    error_t = rosser_error(T_PT)
    count_gap = T_PT / (2 * mp.pi) - mp.mpf(7) / 8 - error_t
    count_gap_derivative = (1 / (2 * mp.pi) - ROSSER_A / T_PT
                            - ROSSER_B / (T_PT * mp.log(T_PT)))
    check("COUNT from Rosser",
          count_gap > 0 and count_gap_derivative > 0,
          "gap(T)=%.12e; derivative(T)=%.12e (both increase thereafter)"
          % (float(count_gap), float(count_gap_derivative)))

    geometry_ok = True
    worst_y_ratio = mp.mpf(0)
    worst_one_minus = mp.mpf(0)
    for delta in (mp.mpf("-0.5"), mp.mpf("-0.25"), mp.mpf(0),
                  mp.mpf("0.25"), mp.mpf("0.5")):
        for gamma in (mp.mpf(14), mp.mpf(1000), T_PT, 10 * T_PT):
            z = (delta + 1j * gamma)**2
            y = A_SAFE / (A_SAFE - z)
            y_bound = A_SAFE / (A_SHIFT + gamma**2)
            worst_y_ratio = max(worst_y_ratio, abs(y) / y_bound)
            worst_one_minus = max(worst_one_minus, abs(1 - y))
            geometry_ok &= abs(y) <= y_bound * (1 + mp.mpf("1e-60"))
            geometry_ok &= abs(1 - y) <= 1
    check("GEO arbitrary-zero envelope", geometry_ok,
          "sample max |y|/bound=%.15f; max |1-y|=%.15f"
          % (float(worst_y_ratio), float(worst_one_minus)))

    b0 = tail_bound(0)
    b1 = tail_bound(1)
    print("  [PROVEN] B_0(T) = %s" % mp.nstr(b0, 18))
    print("  [PROVEN] B_1(T) = %s; r_T = %s"
          % (mp.nstr(b1, 18),
             mp.nstr(A_SAFE / (T_PT**2 + A_SHIFT), 18)))

    section("S2  PROVEN 10^19-COLUMN HAUSDORFF HALF-STRIP")
    d_constant = beta_endpoint_constant()
    y_lower = A_SAFE / (A_SAFE + GAMMA1_HI**2)
    q_lower = GAMMA1_LO**2 / (A_SAFE + GAMMA1_LO**2)
    first_bridge = first_zero_lower(0, 24) / b0
    first_next = first_zero_lower(0, 25) / b0
    check("row n=0, k=0..24 first-zero bridge",
          first_bridge > 1,
          "ratio at k=24 %.12f; same bound at k=25 %.12f"
          % (float(first_bridge), float(first_next)))

    count_ratio_25 = (count_main(mp.mpf(25))
                      / (4 * rosser_error(
                          R_INTERVAL * mp.sqrt(A_SAFE * 25))))
    count_ratio_40 = (count_main(THETA_SPLIT)
                      / (4 * rosser_error(
                          R_INTERVAL * mp.sqrt(A_SAFE * THETA_SPLIT))))
    check("Rosser interval count starts",
          count_ratio_25 > 1 and count_ratio_40 > 1,
          "H/(4E): theta=25 %.12f; theta=40 %.12f"
          % (float(count_ratio_25), float(count_ratio_40)))

    row0_lower = count_half_lower(mp.mpf(K_RECT)) * d_constant / K_RECT
    row0_ratio = row0_lower / b0
    row0_mechanism_root = mp.findroot(
        lambda kval: count_half_lower(kval) * d_constant / kval - b0,
        (mp.mpf("1e19"), mp.mpf("2e19")))
    check("row n=0 counted-beta range to 10^19",
          row0_ratio > 1,
          "lower=%.12e tail=%.12e ratio=%.12f"
          % (float(row0_lower), float(b0), float(row0_ratio)))
    print("  [FAILED(bound mechanism), not a negative cell] elementary "
          "n=0 bound equality at k = %s"
          % mp.nstr(row0_mechanism_root, 16))

    low_ratio_lower = y_lower**2 * q_lower**80
    low_ratio = low_ratio_lower / b1
    check("n>=1 low-ratio region theta<=40",
          low_ratio > 1,
          "worst n=1,k=80 ratio %.12f" % float(low_ratio))

    theta_max = mp.mpf(K_RECT) / 2
    high_lower = (count_half_lower(theta_max)
                  * (d_constant / theta_max)**2)
    high_ratio = high_lower / b1
    max_interval_top = (R_INTERVAL
                        * mp.sqrt(A_SAFE * theta_max))
    check("n>=1 counted-beta region theta>=40",
          high_ratio > 1 and max_interval_top < T_PT,
          "worst n=1 theta=5e18 ratio %.12f; interval top %.6e < T"
          % (float(high_ratio), float(max_interval_top)))

    theorem_ok = all(ok for name, ok, _detail in CHECKS
                     if name in {
                         "COUNT from Rosser",
                         "GEO arbitrary-zero envelope",
                         "row n=0, k=0..24 first-zero bridge",
                         "Rosser interval count starts",
                         "row n=0 counted-beta range to 10^19",
                         "n>=1 low-ratio region theta<=40",
                         "n>=1 counted-beta region theta>=40",
                     })
    check("FORM-A partial theorem arithmetic", theorem_ok,
          "C_(n,k)(256)>0 for all n>=0 and 0<=k<=10^19")
    print("  [PROVEN; PT+Rosser cited inputs] D = %s, y_lo = %s, q_lo = %s"
          % (mp.nstr(d_constant, 16), mp.nstr(y_lower, 16),
             mp.nstr(q_lower, 16)))

    section("S3  EXACT PRIME-SIDE LAGUERRE TRANSMUTATION")
    x = sp.symbols("x")
    symbolic_ok = True
    for n in range(5):
        for k in range(6):
            coefficient_form = sum(
                (-1)**j * sp.binomial(k, j) * sp.factorial(n)
                / sp.factorial(n + j) * x**j
                for j in range(k + 1))
            laguerre_form = (sp.factorial(n) * sp.factorial(k)
                             / sp.factorial(n + k)
                             * sp.assoc_laguerre(k, n, x))
            symbolic_ok &= sp.simplify(coefficient_form
                                       - laguerre_form) == 0
    check("Laguerre coefficient identity", symbolic_ok,
          "exact SymPy identity for 0<=n<=4, 0<=k<=5")

    u_two = mp.log(2)
    integral_deviation = mp.mpf(0)
    for n, k in ((0, 0), (0, 1), (1, 2), (2, 3)):
        derivative_value = h_cell_derivative(n, k, u_two)
        integral_value = h_cell_integral(n, k, u_two)
        deviation = abs(derivative_value - integral_value) \
            / max(abs(derivative_value), mp.mpf("1e-80"))
        integral_deviation = max(integral_deviation, deviation)
    check("subordination integral identity",
          integral_deviation < mp.mpf("1e-40"),
          "max relative deviation %.3e (q=2 samples)"
          % float(integral_deviation))

    q_left = mp.hyp1f1(-1, 1, mp.mpf("0.5"))
    q_right = mp.hyp1f1(-1, 1, mp.mpf(2))
    check("prime kernel sign change", q_left > 0 and q_right < 0,
          "Q_(0,1)(0.5)=%.1f, Q_(0,1)(2)=%.1f; root x=1"
          % (float(q_left), float(q_right)))
    print("  [FAILED(mechanism)] positive Beta spectral windows become "
          "sign-changing generalized-Laguerre source windows.")

    section("S4  SZEGO/KILLIP--SIMON DIRECTION TEST")
    energy_uniform, alpha_uniform = levinson_energy(64, 0.0, 32)
    energy_tilted, alpha_tilted = levinson_energy(64, 12.0, 32)
    support_witness = (energy_uniform > 0.999999
                       and energy_tilted < 1e-4
                       and energy_uniform / energy_tilted > 1e4)
    check("same-support weight sensitivity", support_witness,
          "64 fixed atoms: e32 uniform=%.12e, tilted=%.12e "
          "(factor %.3e); max|alpha| %.3e/%.6f"
          % (energy_uniform, energy_tilted,
             energy_uniform / energy_tilted,
             alpha_uniform, alpha_tilted))
    print("  [PROVEN structural obstruction] pure-point w=0 a.e. gives "
          "Szego entropy -infinity and only e>=0.")
    print("  [MEASURED illustration] the same support/count with positive "
          "weights changes e32 by the factor printed above.")
    print("  [FAILED(KS direction)] RvM counting density is not an a.c. "
          "entropy density and supplies no upper bound on sum |alpha|^2.")

    section("S5  ADJUDICATION")
    elapsed = time.time() - START
    passed = sum(ok for _name, ok, _detail in CHECKS)
    print("  checks %d/%d PASS; runtime %.3f s; SPEC_SHA %s"
          % (passed, len(CHECKS), elapsed, SPEC_SHA[:16]))
    print("  [PROVEN] FORM A partial theorem: C_(n,k)(256)>0 for every "
          "n>=0, 0<=k<=10^19.")
    print("  [FAILED(mechanism)] prime-side Beta positivity: exact "
          "Laguerre kernel has sign changes.")
    print("  [FAILED(mechanism)] KS/Szego floor: pure-point entropy is "
          "-infinity, yielding e>=0 only.")
    print("  [FAILED(mechanism)] asymptotic-a transport is nonuniform in "
          "(n,k); infinity is not a finite flow base point.")
    print("  [FAILED(route)] Weyl contraction after all-section positivity "
          "consumes localized Weil positivity itself.")
    print("\nVERDICT: MOONSHOT-PARTIAL(Form A; "
          "C_(n,k)(256)>0 for all n>=0 and 0<=k<=10^19)")
    print("NO RH CLAIM.")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
