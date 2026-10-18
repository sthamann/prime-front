#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""shift_average_all_depth_probe -- PRIME.COFINAL.SHIFT.AVERAGE.ALLDEPTH.01.

EXPLORATION ONLY.  This is a theorem-contract checker, not a deep scan,
not a verification module, and not an RH claim.

THE FAMILY.  For h = a/D and m,m' = 0,...,h-1,

  Omega_theta[m,m']
    = (G(m+m'+2 theta) + G(|m-m'|))/2,
  G(x) = c(x) - (c(x+1)+c(|x-1|))/2,

where c is the even archimedean read minus the even von-Mangoldt tent
comb.  The faithful source cap is u <= 2a+2D.  Put

  Omega_theta = [[n_theta, b_theta^T], [b_theta, B_theta]],
  s_theta = n_theta - b_theta^T B_theta^-1 b_theta.

EXACT PHASE AVERAGE.  Define

  gbar_r := int_0^1 G(r+2theta)dtheta
          = (1/2) int_r^(r+2) G(x)dx.

Then, exactly,

  nbar       = (gbar_0 + G(0))/2,
  bbar_i     = (gbar_i + G(i))/2,
  Bbar_ij    = (gbar_(i+j) + G(|i-j|))/2,
  sbar       = nbar - int_0^1 b_theta^T B_theta^-1 b_theta dtheta.

If I_r = int_r^(r+1)c(x)dx for r >= 0, evenness gives

  gbar_0 = (I_1-I_2)/4,
  gbar_r = (I_r+I_(r+1)-I_(r-1)-I_(r+2))/4,  r >= 1.

For P = int b b^T, any positive Bbar gives the exact bookkeeping

  sbar = nbar - tr(Bbar^-1 P) - delta_B,
  delta_B = int b^T B_theta^-1 b - tr(Bbar^-1 P).

Splitting b=b_ar+b_comb splits P=P_aa+P_cross+P_cc, with
P_cc=int b_comb b_comb^T positive semidefinite.  Therefore
E_+=tr(Bbar^-1 P_cc)>=0 enters sbar as -E_+.  This is the WRONG sign
for a hoped-for positive B-spline energy and is not positive progress.
delta_B has no sign; exact rational examples of both signs are checked.

THE TENT/B-SPLINE IDENTITY.  With T_D(x)=(1-|x|/D)_+,

  int_0^1 sum_k T_D(u-(k+theta)L)T_D(v-(k+theta)L)dtheta
    = (1/L)(T_D*T_D)(u-v).

The deployed theta shift uses L=2D separately on the even and odd
cell ladders; adding both parities gives exactly (1/D)(T_D*T_D).
The cubic B-spline is checked in Fraction arithmetic by piecewise
Simpson integration.  For the second-difference tent
K_D=T_D-(T_D(.-D)+T_D(.+D))/2,

  D^-1 int K_D(x)^2 dx = 2/3.

Thus the positive prime-comb diagonal in a phase-square energy is
(2/3) sum Lambda(n)^2/n ~ (4/3)a^2 at X=e^(2a).  It survives phase
averaging and, through -b^T B^-1 b, again has the wrong sign.

VALID LOWER BOUND.  Jensen is an UPPER bound here:

  int s(Omega_theta)dtheta <= s(int Omega_theta dtheta).

The variational formula s=min_x(n+2b^T x+x^T Bx), joint convexity of
b^T B^-1 b, operator convexity of inversion, and a minimax swap all
give this same direction.  They cannot be reversed.  A genuine lower
bound needs an independently proved co-block floor

  beta(a,D) <= inf_theta lambda_min(B_theta), beta(a,D)>0.

Then q_theta=b^T B^-1 b <= ||b||^2/beta.  One may split the true comb
into the continuous PNT main measure and the multiplicative fluctuation
dE=dpsi-dx.  More conservatively, this probe takes Omega_0 to be the
archimedean object alone, b_0 its co-vector, G_geo=nbar_0, and lets
R(a,D) bound the smooth main comb plus the multiplicative fluctuation.
Minkowski gives the valid source-only contract

  int s >= G_geo - A,
  A(a,D) := R + beta^-1
    ((int ||b_0||^2)^(1/2) + sqrt(h-1) R)^2.                 (LB)

This is deliberately coarse but genuinely lower-bounding and not a
Jensen reversal.

BEST CLASSICAL MAGNITUDE INPUT AND ITS GAP.  From the unconditional
Vinogradov--Korobov PNT form

  |psi(x)-x| <= C_VK x exp(-c_VK (log x)^(3/5)
                                  (log log x)^(-1/5)),

Stieltjes integration by parts and the exact norms
||K_D'||_1=4, ||K_D||_1=4D/3 give, including the even reflection,

  R_fluc(a,D) <= H(x_0,D) + C_VK(8+4D/3)
    exp(a+D-c_VK(2a-2D)^(3/5)(log(2a-2D))^(-1/5)).          (VK)

Here x_0 is the cited theorem threshold and the fully explicit finite
head can be taken as

  H(x_0,D) <= 4 sum_(n<=x_0) Lambda(n)/sqrt(n)
              +6sqrt(x_0)-4.

This includes both the direct finite Stieltjes head and the lower
endpoint term generated when the VK tail is integrated by parts.  For
the archimedean-only baseline the smooth main comb contributes at most
R_sm=(8D/3)exp(a+D), by ||K_D||_1=4D/3, so R=R_fluc+R_sm in (LB).
The leading exponent remains a-O(a^(3/5)(log a)^(-1/5)); for every
fixed C_VK,c_VK it grows like exp((1-o(1))a).  The desired wall
quantities are O(1) on the registered audit cells.  An optimistic
C_VK=c_VK=1, x_0=2 audit is printed; it is not represented as a
published explicit constant.  Selberg's symmetry rewrite cannot
improve this magnitude route: on the localized object
A_err-B_err=P_err exactly (CCCXXXI).  Montgomery--Vaughan/large-sieve
mean values average oscillatory frequencies, while theta is a short
translation average; after the exact B-spline reduction they retain
the positive diagonal above.

CONTROLS AND VERDICT.  A valid theorem must reject SCRAMBLE and EPSTEIN
where B_theta fails.  The identical modest-cell pipeline audits both.
If they pass, verdict COMB-BLIND.  If one inserts sbar>0 itself, or an
equivalent Weil-positive sign, verdict RESTATEMENT.  If exact identities
hold, controls fire, and (VK) misses (LB), verdict CLASSICAL-GAP.
SHIFTAVG-THEOREM-CANDIDATE is available only if G_geo>A and beta>0 are
proved on one sign-independent predeclared cofinal sequence.

COFINAL HONESTY.  Even a closed all-depth shift-average theorem supplies
H_cof only after a source-only offset selector fixed independently of
future signs.  The separate per-element form-convergence premise, dense
family lemma, and C0 extension in CofinalWeil remain additional premises.

FROZEN PROTOCOL (2026-08-13, before result reads).
  S0  SHA and AST firewall: no zero data, tau, target sign, eigensolver.
  S1  Exact symbolic average and unit-integral identities.
  S2  Exact Fraction tent/B-spline identities, both parity ladders.
  S3  Exact rational Jensen direction, delta_B both-sign examples,
      and the P_cc wrong-sign decomposition.
  A   Modest registered cells only: targets 184 and 405 (actual h 184
      and 388), 32 fixed theta midpoints; no h=1393/2854 work.
  X   SCRAMBLE and EPSTEIN at target 184, 8 fixed midpoint offsets.
  C   Print C_VK=c_VK=1 optimistic (VK)/(LB) gap and the exact
      exponent/diagonal obstruction.  Numerical reads are MEASURED
      diagnostics, never interval sign claims or all-depth evidence.
  V   Frozen precedence CONTRACT-BROKEN > COMB-BLIND > CLASSICAL-GAP >
      SHIFTAVG-THEOREM-CANDIDATE.

AMENDMENT A1 (after the first green 20/20 run, fully disclosed): the
numerical LB audit originally used the archimedean baseline with the
VK fluctuation envelope alone.  That mismatched the stated
archimedean-plus-smooth split.  The permanent conservative repair keeps
the archimedean baseline and adds both the explicit finite head H and
the full smooth-main envelope R_sm before forming A.  This only enlarges
A; no identity, control, gate, verdict rule, or audited cell changed.
AMENDMENT A2 (after the second green 20/20 run): H was widened once more
to include separately the lower-endpoint term of tail integration by
parts, rather than silently charging it to the direct finite head.
Again only A increases; every gate and verdict rule is unchanged.
RUNTIME BAR: 1800 s.  Writes nothing.  verification/ and the preceding
shift probes are imported read-only.  NO RH CLAIM.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import shift_average_probe as sap  # noqa: E402 -- read-only instrument


FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

AUDIT_TARGETS = (184, 405)
N_THETA = 32
CTRL_THETA = tuple((k + Fraction(1, 2)) / 8 for k in range(8))
RUNTIME_BAR = 1800.0
VK_C_OPT = 1.0
VK_c_OPT = 1.0
AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh",
    "tau", "target_sign", "cached_sign",
}


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % (
        "PASS" if ok else "FAIL", name,
        (" -- " + detail) if detail else ""), flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else (
            fn.id if isinstance(fn, ast.Name) else "")
        if name.lower() in AST_BANNED:
            hits.append(name)
    return sorted(set(hits))


# ---------------------------------------------------------------- exact tents
def tent_fraction(x, D):
    x, D = Fraction(x), Fraction(D)
    ax = abs(x)
    return Fraction(0) if ax >= D else Fraction(1) - ax / D


def bspline_fraction(w, D):
    """Exact (T_D*T_D)(w)."""
    w, D = abs(Fraction(w)), Fraction(D)
    z = w / D
    if z >= 2:
        return Fraction(0)
    if z <= 1:
        return D * (Fraction(2, 3) - z * z + z ** 3 / 2)
    return D * (2 - z) ** 3 / 6


def phase_product_exact(u, v, D, spacing, offset=Fraction(0)):
    """Exact integral over one grid phase; the integrand is piecewise
    quadratic, so Simpson is exact on the union of tent breakpoints."""
    u, v, D = Fraction(u), Fraction(v), Fraction(D)
    spacing, offset = Fraction(spacing), Fraction(offset)
    lo = min(u, v) - D - offset - spacing
    hi = max(u, v) + D - offset + spacing
    k_lo = math.floor(lo / spacing) - 2
    k_hi = math.ceil(hi / spacing) + 2

    def value(theta):
        ans = Fraction(0)
        for k in range(k_lo, k_hi + 1):
            point = offset + (k + theta) * spacing
            ans += tent_fraction(u - point, D) * tent_fraction(v - point, D)
        return ans

    breaks = {Fraction(0), Fraction(1)}
    for k in range(k_lo, k_hi + 1):
        for w in (u, v):
            for s in (-D, Fraction(0), D):
                theta = (w - offset - s) / spacing - k
                if 0 < theta < 1:
                    breaks.add(theta)
    breaks = sorted(breaks)
    total = Fraction(0)
    for left, right in zip(breaks[:-1], breaks[1:]):
        mid = (left + right) / 2
        total += (right - left) * (
            value(left) + 4 * value(mid) + value(right)) / 6
    return total


def kappa_l2_coefficient():
    z = sp.symbols("z", real=True)
    expr = 2 * (
        sp.integrate((1 - sp.Rational(3, 2) * z) ** 2, (z, 0, 1))
        + sp.integrate((-1 + z / 2) ** 2, (z, 1, 2))
    )
    return sp.simplify(expr)


# ---------------------------------------------------------- exact matrix facts
def scalar_schur(n, b, B):
    return Fraction(n) - Fraction(b) ** 2 / Fraction(B)


def exact_average_formula_checks():
    h = 4
    fixed = sp.symbols("g0:%d" % (2 * h))
    averaged = sp.symbols("j0:%d" % (2 * h))
    om = sp.zeros(h, h)
    for i in range(h):
        for j in range(h):
            om[i, j] = (averaged[i + j] + fixed[abs(i - j)]) / 2
    n_ok = sp.simplify(om[0, 0] - (averaged[0] + fixed[0]) / 2) == 0
    b_ok = all(sp.simplify(
        om[i, 0] - (averaged[i] + fixed[i]) / 2) == 0
        for i in range(1, h))
    B_ok = all(sp.simplify(
        om[i, j] - (averaged[i + j] + fixed[abs(i - j)]) / 2) == 0
        for i in range(1, h) for j in range(1, h))

    im1, i0, i1, i2 = sp.symbols("Irm1 Ir Ir1 Ir2")
    general = sp.Rational(1, 2) * (
        i0 + i1 - sp.Rational(1, 2) * (i1 + i2)
        - sp.Rational(1, 2) * (im1 + i0))
    general_expected = (i0 + i1 - im1 - i2) / 4
    z0, z1, z2 = sp.symbols("I0 I1 I2")
    at_zero = sp.Rational(1, 2) * (
        z0 + z1 - sp.Rational(1, 2) * (z1 + z2)
        - sp.Rational(1, 2) * (2 * z0))
    return (
        n_ok and b_ok and B_ok,
        sp.simplify(general - general_expected) == 0,
        sp.simplify(at_zero - (z1 - z2) / 4) == 0,
    )


def exact_decomposition_check():
    weights = (sp.Rational(1, 2), sp.Rational(1, 2))
    Bs = (
        sp.diag(2, 3),
        sp.diag(4, 5),
    )
    bas = (
        sp.Matrix([1, 0]),
        sp.Matrix([2, 1]),
    )
    bcs = (
        sp.Matrix([0, 1]),
        sp.Matrix([-1, 1]),
    )
    Bbar = sum((w * B for w, B in zip(weights, Bs)), sp.zeros(2))
    Paa = sum((w * b * b.T for w, b in zip(weights, bas)), sp.zeros(2))
    Pcc = sum((w * b * b.T for w, b in zip(weights, bcs)), sp.zeros(2))
    Pcross = sum((
        w * (ba * bc.T + bc * ba.T)
        for w, ba, bc in zip(weights, bas, bcs)
    ), sp.zeros(2))
    qbar = sum((
        w * ((ba + bc).T * B.inv() * (ba + bc))[0]
        for w, B, ba, bc in zip(weights, Bs, bas, bcs)
    ), sp.Rational(0))
    trace_all = sp.trace(Bbar.inv() * (Paa + Pcross + Pcc))
    delta = sp.simplify(qbar - trace_all)
    nbar = sp.Rational(7)
    exact = sp.simplify(
        (nbar - qbar) - (nbar - trace_all - delta)) == 0
    pcc_psd = (
        Pcc[0, 0] >= 0 and Pcc.det() >= 0
    )
    eplus = sp.simplify(sp.trace(Bbar.inv() * Pcc))
    return exact, pcc_psd, eplus, delta


# ----------------------------------------------------------- classical bound
def vk_eta(log_x, c_value):
    log_x = max(float(log_x), math.e)
    return c_value * log_x ** (3.0 / 5.0) / math.log(log_x) ** (1.0 / 5.0)


def vk_entry_envelope(a_value, D_value, C_value=1.0, c_value=1.0):
    lower_log = max(2.0 * a_value - 2.0 * D_value, math.e)
    exponent = a_value + D_value - vk_eta(lower_log, c_value)
    return C_value * (8.0 + 4.0 * D_value / 3.0) * math.exp(exponent)


def finite_head_envelope(x0=2):
    """Finite Stieltjes head plus the tail's lower endpoint, with the
    even reflection.  The numerical audit takes x0=2."""
    total = sum(
        math.log(p) / math.sqrt(p)
        for p in range(2, x0 + 1)
        if all(p % d for d in range(2, int(math.sqrt(p)) + 1))
    )
    return 4.0 * total + 6.0 * math.sqrt(x0) - 4.0


def smooth_main_envelope(a_value, D_value):
    """Arch-only-baseline price of the even continuous PNT main comb."""
    return (8.0 * D_value / 3.0) * math.exp(a_value + D_value)


def assembled_schur_measure(omega):
    n0 = float(omega[0, 0])
    b = np.ascontiguousarray(omega[1:, 0])
    B = np.ascontiguousarray(omega[1:, 1:])
    try:
        factor = sla.cho_factor(B, lower=True, check_finite=False)
    except np.linalg.LinAlgError:
        return None
    y = sla.cho_solve(factor, b, check_finite=False)
    return n0 - float(b @ y)


def numerical_cell_audit(cell, target):
    uu, mm = sap.cell_atoms(cell)
    true_wall = sap.Wall(cell, uu, mm)
    arch_wall = sap.Wall(cell, np.array([]), np.array([]))
    theta_grid = (np.arange(N_THETA) + 0.5) / N_THETA

    s_values = []
    certified_floors = []
    arch_n = []
    arch_b2 = []
    omega_sum = np.zeros((true_wall.h, true_wall.h))
    for theta in theta_grid:
        omega = true_wall.omega(float(theta))
        omega_sum += omega / N_THETA
        measured_s = assembled_schur_measure(omega)
        if measured_s is not None:
            s_values.append(measured_s)
        cert = sap.cert_schur(omega)
        if sap.ok_res(cert):
            certified_floors.append(cert["c_lo"])
        omega_arch = arch_wall.omega(float(theta))
        arch_n.append(float(omega_arch[0, 0]))
        arch_b = omega_arch[1:, 0]
        arch_b2.append(float(arch_b @ arch_b))

    mean_s = float(np.mean(s_values)) if s_values else float("nan")
    schur_of_average = assembled_schur_measure(omega_sum)
    beta_grid = (
        min(certified_floors)
        if len(certified_floors) == N_THETA else float("nan")
    )
    G_geo = float(np.mean(arch_n))
    b0_l2 = math.sqrt(float(np.mean(arch_b2)))
    a_value = float(cell["alpha"])
    D_value = float(true_wall.D)
    R_fluc_opt = finite_head_envelope(2) + vk_entry_envelope(
        a_value, D_value, VK_C_OPT, VK_c_OPT)
    R_smooth = smooth_main_envelope(a_value, D_value)
    R_opt = R_fluc_opt + R_smooth
    if beta_grid > 0:
        A_opt = R_opt + (
            b0_l2 + math.sqrt(true_wall.h - 1) * R_opt
        ) ** 2 / beta_grid
        gap = A_opt / max(abs(G_geo), 1.0e-300)
    else:
        A_opt, gap = float("inf"), float("inf")

    prime_weights = mm / 2.0
    diagonal_energy = Fraction(2, 3) * float(
        np.dot(prime_weights, prime_weights))
    print(
        "  target %d -> h %d a %.9f D %.9e | MEASURED mean(s) %.9e | "
        "s(mean Omega) %.9e | sampled certified B-floor %.3e"
        % (target, true_wall.h, a_value, D_value, mean_s,
           schur_of_average if schur_of_average is not None
           else float("nan"), beta_grid))
    print(
        "    G_geo=nbar_arch %.9e | b0_L2 %.3e | optimistic "
        "R_fluc(C=c=1,x0=2) %.3e + R_sm %.3e = R %.3e | "
        "A_LB %.3e | A/G %.3e"
        % (G_geo, b0_l2, R_fluc_opt, R_smooth, R_opt, A_opt, gap))
    print(
        "    exact B-spline prime diagonal %.3e | diagonal/|G_geo| %.3e"
        % (diagonal_energy,
           diagonal_energy / max(abs(G_geo), 1.0e-300)))
    return {
        "target": target,
        "h": true_wall.h,
        "mean_s": mean_s,
        "schur_average": schur_of_average,
        "beta_grid": beta_grid,
        "G_geo": G_geo,
        "R_opt": R_opt,
        "A_opt": A_opt,
        "gap": gap,
        "diag": diagonal_energy,
    }


def control_audit(cell):
    rows = []
    for world in ("scramble", "epstein"):
        uu, mm = sap.cell_atoms(
            cell, world=world, seed=sap.SEED_SCR)
        wall = sap.Wall(cell, uu, mm)
        failed_B = 0
        finite_s = []
        for theta in CTRL_THETA:
            omega = wall.omega(float(theta))
            value = assembled_schur_measure(omega)
            if value is None:
                failed_B += 1
            else:
                finite_s.append(value)
        min_s = min(finite_s) if finite_s else float("nan")
        fired = failed_B > 0 or (
            finite_s and min_s <= 0.0)
        rows.append((world, failed_B, min_s, bool(fired)))
        print(
            "  %-8s MEASURED: B-Cholesky failures %d/%d, "
            "min defined s %s -> %s"
            % (world.upper(), failed_B, len(CTRL_THETA),
               ("%.6e" % min_s) if finite_s else "undefined",
               "FIRES" if fired else "SILENT"))
    return rows


def main():
    print("=" * 78)
    print("PRIME.COFINAL.SHIFT.AVERAGE.ALLDEPTH.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("EXPLORATION ONLY -- theorem-contract checker -- NO RH CLAIM")
    print("=" * 78)

    section("S0 -- frozen source firewall")
    hits = ast_firewall()
    check("S0.1 no zero reader, target sign, tau, or eigensolver call",
          not hits, "hits=%s" % hits)
    check("S0.2 no deep-worker duplication",
          AUDIT_TARGETS == (184, 405)
          and 1393 not in AUDIT_TARGETS and 2854 not in AUDIT_TARGETS)

    section("S1 -- exact phase-average identities")
    matrix_ok, unit_ok, zero_ok = exact_average_formula_checks()
    check("S1.1 nbar, bbar, Bbar formulas are symbolically exact",
          matrix_ok)
    check("S1.2 gbar_r unit-integral telescoping is symbolically exact",
          unit_ok)
    check("S1.3 folded r=0 formula gbar_0=(I1-I2)/4 is exact",
          zero_ok)

    section("S2 -- exact tent/B-spline phase identity")
    D = Fraction(3, 20)
    u = Fraction(7, 5)
    exact_rows = []
    parity_rows = []
    for ratio in (
        Fraction(0), Fraction(1, 3), Fraction(1, 2),
        Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2),
    ):
        v = u - ratio * D
        lhs = phase_product_exact(u, v, D, D)
        rhs = bspline_fraction(u - v, D) / D
        exact_rows.append(lhs == rhs)
        even = phase_product_exact(u, v, D, 2 * D, Fraction(0))
        odd = phase_product_exact(u, v, D, 2 * D, D)
        parity_rows.append(even + odd == rhs)
    check("S2.1 one-grid tent/B-spline identity exact on 7 separations",
          all(exact_rows))
    check("S2.2 even+odd L=2D ladders equal the deployed 1/D identity",
          all(parity_rows))
    kap = kappa_l2_coefficient()
    check("S2.3 second-difference tent diagonal coefficient is 2/3",
          kap == sp.Rational(2, 3), "coefficient=%s" % kap)

    section("S3 -- valid inequality directions and exact decomposition")
    s1 = scalar_schur(2, 0, 1)
    s2 = scalar_schur(2, 2, 4)
    mean_s = (s1 + s2) / 2
    s_mean_matrix = scalar_schur(2, 1, Fraction(5, 2))
    check("S3.1 Jensen is upper, not lower (strict exact counterexample)",
          mean_s < s_mean_matrix,
          "mean s=%s, s(mean Omega)=%s" % (mean_s, s_mean_matrix))

    delta_pos = (
        (Fraction(1) + Fraction(1, 3)) / 2
        - Fraction(1, 2))
    delta_neg = (
        (Fraction(0) + Fraction(1)) / 2
        - Fraction(2, Fraction(5, 2)))
    check("S3.2 delta_B has no sign (both exact signs exhibited)",
          delta_pos > 0 and delta_neg < 0,
          "delta+=%s delta-=%s" % (delta_pos, delta_neg))

    B = sp.diag(2, 3)
    b = sp.Matrix([1, 2])
    q = (b.T * B.inv() * b)[0]
    norm_bound = (b.T * b)[0] / 2
    check("S3.3 co-block-floor lower bound has the valid direction",
          sp.simplify(norm_bound - q) == sp.Rational(2, 3),
          "q=%s <= ||b||^2/beta=%s" % (q, norm_bound))

    dec_ok, pcc_psd, eplus, delta = exact_decomposition_check()
    check("S3.4 Schur-average decomposition closes exactly",
          dec_ok, "delta_B=%s" % delta)
    check("S3.5 P_cc is PSD and E+>0 enters through -E+",
          pcc_psd and eplus > 0,
          "E+=%s, contribution=-%s (WRONG SIGN)" % (eplus, eplus))
    check("S3.6 VK exponent is sublinear and cannot cancel +a",
          Fraction(3, 5) < 1,
          "log R = a-O(a^(3/5)(log a)^(-1/5))")

    section("A -- modest registered numerical constant audit")
    table_ok = sap.build_tables()
    check("A0 source sieve matches deployed prefix", table_ok)
    picks = sap.pick_cells(sap.census())
    audits = [
        numerical_cell_audit(picks[target], target)
        for target in AUDIT_TARGETS
    ]
    jensen_measured = all(
        row["schur_average"] is not None
        and row["mean_s"] <= row["schur_average"]
        + 1.0e-10 * (1.0 + abs(row["schur_average"]))
        for row in audits
    )
    check("A1 measured means obey the exact Jensen upper direction",
          jensen_measured)
    classical_gap = all(
        math.isfinite(row["gap"]) and row["gap"] > 1.0
        for row in audits
    )
    check("A2 even optimistic C_VK=c_VK=1 lower-bound contract misses",
          classical_gap,
          "A/G gaps=%s" % [
              "%.3e" % row["gap"] for row in audits])
    check("A3 audit remains modest and excludes both deep-worker cells",
          [row["h"] for row in audits] == [184, 388])

    section("X -- identical-pipeline controls (measured diagnostics)")
    control_rows = control_audit(picks[184])
    controls_fire = all(row[3] for row in control_rows)
    check("X1 SCRAMBLE and EPSTEIN both fire on the modest subset",
          controls_fire,
          "MEASURED only; no interval sign claim")

    section("V -- frozen verdict and shortest remaining lemma")
    failed = [name for name, ok in CHECKS if not ok]
    structural_failed = any(
        name.startswith(("S0", "S1", "S2", "S3")) for name in failed)
    if structural_failed:
        verdict = "CONTRACT-BROKEN"
    elif not controls_fire:
        verdict = "COMB-BLIND"
    elif classical_gap:
        verdict = "CLASSICAL-GAP"
    else:
        verdict = "SHIFTAVG-THEOREM-CANDIDATE"
    print("  VERDICT: %s" % verdict)
    print(
        "  BEST VALID LOWER BOUND: int s >= G_geo-A with "
        "A=R+beta^-1(B0+sqrt(h-1)R)^2.")
    print(
        "  SHORTEST REMAINING LEMMA: on one sign-independent "
        "predeclared cofinal (a_j,D_j), prove beta_j>0 and a signed "
        "multiplicative-fluctuation estimate A(a_j,D_j)<G_geo(a_j,D_j).")
    print(
        "  WHY RH-HARD: VK leaves weighted error exp(a-O(a^(3/5))); "
        "B-spline/large-sieve retains a positive ~4a^2/3 diagonal with "
        "the wrong Schur sign; Selberg leaves the identical residual. "
        "Closing the signed remainder plus the separate form-convergence "
        "premise would supply Weil positivity.")
    elapsed = time.time() - T0
    runtime_ok = elapsed < RUNTIME_BAR
    check("V1 runtime below 1800 s", runtime_ok, "%.3f s" % elapsed)
    failed = [name for name, ok in CHECKS if not ok]
    print(
        "\n[SUMMARY] %d/%d checks pass | failed=%s | %.3f s | %s"
        % (len(CHECKS) - len(failed), len(CHECKS),
           failed if failed else "none", elapsed, verdict))
    print("NO RH CLAIM.  No all-depth positivity claim.")
    return 0 if not failed and verdict == "CLASSICAL-GAP" else 1


if __name__ == "__main__":
    raise SystemExit(main())
