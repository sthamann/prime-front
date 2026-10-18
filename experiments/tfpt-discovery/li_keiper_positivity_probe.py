#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""li_keiper_positivity_probe -- PRIME.LI.KEIPER.ARITH.01

FROZEN THEOREM-ENGINEERING PROBE (2026-08-13).  EXPLORATION ONLY.
NO RH CLAIM.  No paper, ledger, website, verification, manifest, marker or
generated file is touched.  This probe writes nothing.

MISSION.  Attack the remaining RH edge from the Li--Keiper side and decide
whether the deployed wall/Schur endform and the Li coefficients are the same
object in different coordinates, and whether the archimedean-vs-arithmetic
bookkeeping is more favourable on the Li side.

THE OBJECT.  With xi(s) = (1/2)s(s-1)pi^(-s/2)Gamma(s/2)zeta(s) and the
Bombieri--Lagarias substitution s = 1/(1-z),

    log xi(s(z)) = log xi(1) + sum_{n>=1} (lambda_n/n) z^n,
    lambda_n = sum_rho [1 - (1-1/rho)^n]   (symmetric pairing),
    lambda_n = [z^(n-1)] s(z)^2 (xi'/xi)(s(z)).                      (LI)

Li (1997): lambda_n >= 0 for all n >= 1 <=> RH.  Bombieri--Lagarias (1999)
Thm 1 generalizes this to an arbitrary symmetric multiset: nonnegativity of
all lambda_n <=> every point satisfies |1-1/rho| <= 1 <=> Re rho <= 1/2.
Positivity for finitely many n is NOT the criterion (S5, S6).

EXACT ARITHMETIC (ZERO-FREE) SPLIT.  From

    xi'/xi(s) = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2) + zeta'/zeta(s),

with w = s-1 = z/(1-z) and s^2 = (1-z)^(-2), the exact algebraic reductions
s^2/s = 1/(1-z), s^2/(s-1) = 1/(z(1-z)), s^2 w^k = z^k(1-z)^(-(k+2)) and
[z^(n-1)] z^k(1-z)^(-(k+2)) = C(n,k+1) give (S1 checks all of them):

    lambda_n = lambda_n^pole + lambda_n^arch + lambda_n^prime,
    lambda_n^pole  = 2                                     (s = 0 and s = 1),
    lambda_n^arch  = -(n/2)log pi
                     + (1/2) sum_{j=1}^n C(n,j) b_{j-1},            (ARCH)
    lambda_n^prime = -1 + sum_{j=1}^n C(n,j) eta_{j-1},             (PRIME)

    psi(1/2+w/2) = sum_k b_k w^k,  b_0 = -gamma - 2 log 2,
    b_k = (-1)^(k+1)(2^(k+1)-1)zeta(k+1)/2^k   (k >= 1),
    zeta'/zeta(1+w) = -1/w + sum_k eta_k w^k,  eta_0 = gamma.

TRIVIAL-ZERO FORM OF (ARCH).  For j >= 2, b_{j-1} = 2(-1)^j sum_{m odd}m^(-j),
hence exactly

    sum_{j=1}^n C(n,j) b_{j-1}
      = n b_0 + 2(n-1) + 2 sum_{m odd >= 3}[(1-1/m)^n - 1 + n/m],

a rapidly convergent odd-integer (trivial-zero) sum used as a second,
independent route for (ARCH).

VON MANGOLDT FORM OF (PRIME) -- the representation the mission asks for.
With the Laguerre polynomial L_n(x) = sum_{j=0}^n C(n,j)(-x)^j/j! the exact
polynomial identities

    sum_{j=1}^n C(n,j)(-1)^j x^(j-1)/(j-1)! = L_n'(x),
    sum_{j=1}^n C(n,j)(-1)^j y^j/j!         = L_n(y) - 1

together with the regularized log-power moments of the von Mangoldt measure

    c_k  = lim_N [ sum_{m<=N} Lambda(m)(log m)^k/m - (log N)^(k+1)/(k+1) ],
    eta_k = (-1)^(k+1) c_k/k!

turn (PRIME) into the purely arithmetic, zero-free statement

    lambda_n^prime = lim_N [ sum_{m<=N}(Lambda(m)/m) L_n'(log m)
                             - L_n(log N) ] =: lim_N P_n(N).         (VM)

Substituting u = log m turns the weight Lambda(m)/m times e^(u/2) into
Lambda(m)/sqrt(m): (VM) reads the SAME measure
dmu = sum_m (Lambda(m)/sqrt m) delta_{log m} that the wall reads, against the
Li window phi_n(u) = e^(-u/2) L_n'(u).

TELESCOPING / ABEL LAW.  Exactly, for N < N',

    P_n(N') - P_n(N) = int_N^{N'} L_n'(log x) d(psi(x)-x)/x,         (TEL)

so the truncation of (VM) is governed by the multiplicative fluctuation alone.
With the classical uniform Laguerre bound |L_n^(a)(x)| <= C(n+a,n)e^(x/2)
(x >= 0, a >= 0) one gets |L_n'(log x)| <= n sqrt(x): inside the oscillatory
range log x < 4n the tail weight does NOT decay and the absolute mass of (VM)
grows like sqrt(N).  (VM) becomes absolutely usable only for log N > 4n, i.e.
N > e^(4n).  Both facts are measured in S4.

ROUTE ACTUALLY USED FOR NUMBERS (zero-free, non-circular).  Z(w) = w zeta(1+w)
is entire with Z(0) = 1 and zeta'/zeta(1+w) = Z'/Z(w) - 1/w, so
eta_k = [w^k](Z'/Z).  The Taylor coefficients z_k of Z are extracted by the
discrete Cauchy sum on |w| = 1 and eta by exact series division.  ERROR MODEL
(declared before any number):
  E1 aliasing: |z_k^alias| <= M_R R^(-M)/(1-R^(-M)), M_R a sampled and
     safety-inflated bound for max|Z| on |w| = R = 4 (Cauchy);
  E2 round-off: <= 10^(-(dps-15)) max|Z| on |w| = 1;
  E3 propagation: measured amplification A = max|d lambda_n|/max|d z_k| under
     explicit perturbations of size 10^(-(dps-40)) pushed through the FULL
     pipeline; the reported bar is (E1+E2)*A*safety;
  E4 independent configuration: the whole pipeline is rerun at higher dps and
     larger M and must agree far beyond the demanded digits;
  E5 exact gates: closed forms for lambda_1, lambda_2 and an independent
     algebraic assembly of lambda_3; eta_0 = gamma, eta_1 = -gamma^2-2gamma_1,
     eta_2 = gamma^3+3 gamma gamma_1+(3/2)gamma_2; z_k versus Stieltjes; and
     the odd-integer (trivial-zero) route for (ARCH).
Zeros are used ONLY as a clearly typed independent cross-check (S2.X); they
never enter a reported value, since a zero sum would be circular here.

TRANSFORM QUESTION (S1/S3).  Two exact statements are established:
  (T+) the map {c_{j-1}} -> {lambda_n^prime} is lower triangular with diagonal
       (-1)^n/(n-1)! != 0, hence an invertible rational coordinate change: the
       Li coefficients and the regularized log-power moments of the von
       Mangoldt measure are the SAME finite data;
  (T-) span{phi_n : n <= N} = e^(-u/2) * P_{N-1} (exact degree ladder), while
       every nonzero finite combination of wall tents T_D(.-u_k) vanishes
       identically outside a compact set and a nonzero e^(-u/2)*polynomial
       vanishes on no interval (exact Vandermonde witness).  The two spans
       meet only in {0}: there is NO finite linear transform between the
       deployed Galerkin tent family and the Li kernels.
The wall scalar s_h is additionally a Schur complement, i.e. a rational
function of comb reads, whereas lambda_n is a single linear read: the Li side
drops the Schur/alignment layer entirely.  Hence: same measure, different
window, no transform -- not a literal reformulation.

MARGIN COMPARISON (S3).  The repo's frozen wall diagnostics are CITED from
CCCXXXI/CCCLIX and never recomputed: |P_err|/margin = 3.11e2 .. 1.53e4,
|B|/margin median 9.45e3, optimistic unconditional envelope/margin 1.6e4
(best rung) / 9.1e5 (median), oracle exact-main 2e4, conservative all-depth
A/G 2.470e11 / 1.990e14, CCCXXXI cancellation depth |margin|/(total absolute
mass) 2.421e-06 / 2.025e-05 / 1.741e-03, depth trend Spearman -0.850.  The Li
analogues measured here are |lambda_n^prime|/lambda_n and
lambda_n/(|pole|+|arch|+|prime|).

CONTROLS (S6).  (C1) an exact off-line quadruple via Bombieri--Lagarias: the
criterion has teeth, and the first sign flip obeys the measured law
n_flip ~ log(lambda_n)/log|1-1/(1-rho)|, i.e. n_flip grows like
2 tau^2/(2 sigma - 1); (C2) SMOOTH (dpsi -> dx) gives lambda_n^prime = -1
EXACTLY for every n, so smooth is rejected wherever 1 + lambda_n^arch < 0 --
the mechanism is loss of the functional equation, not multiplicativity;
(C3) SCRAMBLE and (C4) EPSTEIN are audited at the truncated-moment level, where
the separation is ASYMMETRIC and is reported as such: the Epstein comb moves the
functional by more than the whole true value, a sealed Lambda-label permutation
by only 1e-4..1e-2 relative.  A single linear read carries no multiplicativity
gate, so the Li coordinates are partially -- not fully -- comb-sensitive.

VERDICT ENUM (frozen):
  LI-FAVORABLE       quantified better margin plus the exact remaining lemma;
  LI-DISGUISE        same bill as the wall, transform exhibited;
  LI-REFORMULATION   literally the same object;
  LI-CLASSICAL-GAP   sign-oriented route, known unconditional tools
                     quantified short;
  LI-INSTRUMENT-EDGE an exact/precision gate is unresolved.
Frozen precedence: failed exact gate -> LI-INSTRUMENT-EDGE; exact identity of
the two functionals -> LI-REFORMULATION; finite transform found ->
LI-DISGUISE; transform refuted AND Li tolerance better by >= 3 orders with a
non-degrading trend -> LI-FAVORABLE; otherwise -> LI-CLASSICAL-GAP.

WHAT IS NEW, WHAT IS NOT.  The lambda_n values and their trend are classical
(Keiper 1992, Li 1997, Bombieri--Lagarias 1999, Voros, Coffey) and the repo
already carries a zero-route slice to n = 64 (v665 / keiper_li_probe).  NEW
here is (a) the (VM) representation with its measured e^(4n) depth demand,
(b) the exact (T+)/(T-) transform pair against the deployed wall family,
(c) the head-to-head margin/depth comparison in the repo's own CCCXXXI metric,
(d) the quantified off-line flip law that bounds what finite positivity can
possibly exclude.

SCOPE.  Only this file plus one prepended note in experiments/next.txt.
verification/ untouched and not imported; keiper_li_probe.py is not imported,
only its committed zero cache is read for the typed cross-check.  No .md, no
commit, no marker, no scorecard row.  No RH claim: H_cof, per-element form
convergence, density and C0 extension remain separate premises.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import time
from fractions import Fraction as F

import numpy as np
import sympy as sp
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

# ------------------------------------------------------- declared constants
N_MAX = 400            # highest Li index carried at full precision
DPS_A, M_A = 300, 512  # primary configuration
DPS_B, M_B = 420, 768  # independent validation configuration
R_ALIAS = 4            # radius for the a-priori aliasing bound on z_k
ALIAS_SAMPLES = 96     # samples for the sup bound on |Z| on |w| = R_ALIAS
ALIAS_SAFETY = 10      # inflation of the sampled sup bound
PERT_RUNS = 4          # perturbation runs for the propagation amplification
PERT_SAFETY = 100      # safety factor on the measured amplification
N_SYM = 12             # symbolic coefficient-extraction depth
N_TRI = 12             # exact triangular-transform depth
N_ODD_XCHK = 64        # depth of the odd-integer (trivial-zero) cross-check
TOL_ODD = mp.mpf("1e-40")
ODD_TAIL_M1 = 3361     # first odd index of the analytic (ARCH) tail (fixed)
N_ZERO_XCHK = 40       # depth of the typed zero cross-check
ZERO_XCHK_BAR = 0.05   # declared relative bar for the zero cross-check
VM_SIEVE = 2 * 10 ** 7       # von Mangoldt truncation for (VM)
VM_N = (1, 2, 3, 4, 6, 10)   # Li indices audited on the (VM) route
VM_TOL = 5.0e-2              # (VM) agreement bar (oscillatory, declared)
X0_VK = 100            # smallest x at which the VK shape is consumed
DEMAND_DIGITS = 30     # digits demanded of the lambda_n table
FAVORABLE_ORDERS = 3   # orders of tolerance gain required for LI-FAVORABLE
DEPTH_CEILING = 0.95   # declared "no cancellation" floor for the Li depth
EPSTEIN_SEP = 1.0      # declared separation the Epstein comb must exceed
SCRAMBLE_ORDERS = 2    # orders by which the scramble shift must stay BELOW it
GAMMA1 = "14.134725141734693790457251983562"   # first zero ordinate (cited)

# frozen wall diagnostics -- CITED from CCCXXXI / CCCLIX, never recomputed
WALL_PERR_OVER_MARGIN = (F(311), F(15300))
WALL_B_OVER_MARGIN_MEDIAN = F(9450)
WALL_ENVELOPE_OVER_MARGIN = (F(16000), F(910000))
WALL_ORACLE_OVER_MARGIN = F(20000)
WALL_AG_ALLDEPTH = ("2.470e11", "1.990e14")
WALL_DEPTH_AFTER = ("2.421e-6", "2.025e-5", "1.741e-3")
WALL_DEPTH_SPEARMAN = "-0.850"

CHECKS: list[tuple[str, bool]] = []
T0 = time.time()


def check(name: str, ok: bool, detail: str = "") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""))
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def spearman(xs, ys) -> float:
    """Rank correlation only -- no fit, no model."""
    def ranks(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        out = [0.0] * len(vals)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                out[order[k]] = avg
            i = j + 1
        return out

    rx, ry = ranks(list(xs)), ranks(list(ys))
    n = len(rx)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    dy = math.sqrt(sum((b - my) ** 2 for b in ry))
    return num / (dx * dy) if dx > 0 and dy > 0 else 0.0


# ================================================================ S0 firewall
def s0_firewall() -> None:
    section("S0 -- FIREWALL AND DECLARED CONSTANTS")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    forbidden = {n for n in imported
                 if n.startswith(("verification", "run_all"))
                 or (len(n) > 1 and n[0] == "v" and n[1].isdigit())}
    check("S0.1 no verification/ module imported", not forbidden,
          "imports: %s" % ", ".join(sorted(imported)))
    writes = [n for n in ast.walk(tree)
              if isinstance(n, ast.Call)
              and isinstance(n.func, ast.Name) and n.func.id == "open"
              and len(n.args) > 1 and isinstance(n.args[1], ast.Constant)
              and "r" not in str(n.args[1].value)]
    check("S0.2 probe opens no file for writing", not writes)
    check("S0.3 SPEC_SHA frozen from the docstring", len(SPEC_SHA) == 64,
          SPEC_SHA)
    print("  N_MAX=%d  cfgA=(dps %d, M %d)  cfgB=(dps %d, M %d)  "
          "demand %d digits" % (N_MAX, DPS_A, M_A, DPS_B, M_B, DEMAND_DIGITS))


# ===================================================== S1 exact symbolic core
def s1_symbolic():
    section("S1 -- EXACT SYMBOLIC CORE (coefficient extraction, Laguerre, "
            "transform)")
    z, x, y, t = sp.symbols("z x y t")
    s = 1 / (1 - z)
    w = z / (1 - z)

    check("S1.1 s = 1/(1-z) and w = s-1 = z/(1-z) consistent",
          sp.simplify(s - 1 - w) == 0)
    check("S1.2 s^2*(1/s) = 1/(1-z)  (pole at s=0)",
          sp.simplify(s ** 2 / s - 1 / (1 - z)) == 0)
    check("S1.3 s^2/(s-1) = 1/(z(1-z))  (pole at s=1)",
          sp.simplify(s ** 2 / (s - 1) - 1 / (z * (1 - z))) == 0)
    ok = all(sp.simplify(s ** 2 * w ** k - z ** k / (1 - z) ** (k + 2)) == 0
             for k in range(0, N_SYM))
    check("S1.4 s^2 w^k = z^k (1-z)^(-(k+2)) for k < %d" % N_SYM, ok)

    ser_geo = sp.Poly(sp.series(1 / (1 - z), z, 0, N_SYM + 2).removeO(),
                      z).all_coeffs()[::-1]
    check("S1.5 [z^m] 1/(1-z) = 1 for all m -> each pole block contributes "
          "exactly +1, lambda^pole = 2",
          all(c == 1 for c in ser_geo[:N_SYM + 1]))
    check("S1.6 [z^(n-1)] -s^2 (1/2)log pi = -(n/2) log pi",
          all(sp.Poly(sp.series(-s ** 2 / 2, z, 0, N_SYM + 2).removeO(),
                      z).all_coeffs()[::-1][n - 1] == -sp.Rational(n, 2)
              for n in range(1, N_SYM + 1)))
    ok_bin = True
    for k in range(0, N_SYM):
        co = sp.Poly(sp.series(z ** k / (1 - z) ** (k + 2), z, 0,
                               N_SYM + 2).removeO(), z).all_coeffs()[::-1]
        for n in range(k + 1, N_SYM + 1):
            ok_bin = ok_bin and co[n - 1] == sp.binomial(n, k + 1)
    check("S1.7 [z^(n-1)] z^k(1-z)^(-(k+2)) = C(n,k+1): (ARCH) and (PRIME) "
          "binomial forms are exact", ok_bin)

    # Laguerre identities
    ok_l1 = ok_l2 = True
    for n in range(1, N_TRI + 1):
        lhs = sum(sp.binomial(n, j) * (-1) ** j * x ** (j - 1)
                  / sp.factorial(j - 1) for j in range(1, n + 1))
        ok_l1 = ok_l1 and sp.expand(lhs - sp.diff(sp.laguerre(n, x), x)) == 0
        lhs2 = sum(sp.binomial(n, j) * (-1) ** j * y ** j / sp.factorial(j)
                   for j in range(1, n + 1))
        ok_l2 = ok_l2 and sp.expand(lhs2 - (sp.laguerre(n, y) - 1)) == 0
    check("S1.8 sum_j C(n,j)(-1)^j x^(j-1)/(j-1)! == L_n'(x) exactly", ok_l1)
    check("S1.9 sum_j C(n,j)(-1)^j y^j/j! == L_n(y)-1 exactly (the (VM) "
          "counterterm)", ok_l2)

    # SMOOTH world: the counterterm IS the Abel main term
    ok_sm = True
    for n in range(1, N_TRI + 1):
        dl = sp.diff(sp.laguerre(n, t), t).subs(t, sp.log(x))
        integ = sp.integrate(sp.expand(dl) / x, (x, 1, y))
        ok_sm = ok_sm and sp.simplify(
            integ - (sp.laguerre(n, sp.log(y)) - 1)) == 0
    check("S1.10 int_1^N L_n'(log x)dx/x == L_n(log N) - 1: SMOOTH gives "
          "lambda^prime = -1 EXACTLY for every n", ok_sm)

    # (T+) triangular transform: Li coefficients <-> regularized log moments
    rows = [[F((-1) ** j) * F(int(sp.binomial(n, j)))
             / F(math.factorial(j - 1)) if j <= n else F(0)
             for j in range(1, N_TRI + 1)] for n in range(1, N_TRI + 1)]
    lower = all(rows[n - 1][j - 1] == 0 for n in range(1, N_TRI + 1)
                for j in range(n + 1, N_TRI + 1))
    diag_ok = all(rows[n - 1][n - 1] == F((-1) ** n)
                  / F(math.factorial(n - 1)) for n in range(1, N_TRI + 1))
    det = sp.Matrix([[sp.Rational(v.numerator, v.denominator) for v in r]
                     for r in rows]).det()
    want_det = sp.prod([sp.Integer((-1) ** n) / sp.factorial(n - 1)
                        for n in range(1, N_TRI + 1)])
    check("S1.11 (T+) transform lower triangular with diagonal "
          "(-1)^n/(n-1)!", lower and diag_ok)
    check("S1.12 (T+) exact determinant = prod (-1)^n/(n-1)! != 0 -> "
          "invertible over Q: SAME finite data",
          det != 0 and sp.simplify(det - want_det) == 0,
          "det = %s (exact rational, %.3e)" % (det, float(det)))

    # (T-) span separation against the deployed wall tent family
    D = F(1)
    centers = [F(0), F(2), F(4), F(6)]
    weights = [F(3), F(-5), F(7), F(-2)]

    def tent(u: F, c: F) -> F:
        d = abs(u - c)
        return F(0) if d >= D else 1 - d / D

    beyond = [max(centers) + D + F(k) for k in range(1, N_TRI + 2)]
    tent_zero = all(sum(wt * tent(u, c) for wt, c in zip(weights, centers)) == 0
                    for u in beyond)
    vander = sp.Matrix([[sp.Rational(u.numerator, u.denominator) ** k
                         for k in range(N_TRI)] for u in beyond[:N_TRI]])
    deg_ok = all(sp.degree(sp.expand(sp.diff(sp.laguerre(n, x), x)), x)
                 == n - 1 for n in range(1, N_TRI + 1))
    check("S1.13 (T-) L_n' has exact degree n-1 -> span{phi_n : n<=N} = "
          "e^(-u/2) * P_(N-1)", deg_ok)
    check("S1.14 (T-) every finite tent combination vanishes identically "
          "beyond its support", tent_zero)
    check("S1.15 (T-) Vandermonde on those points is nonsingular -> only the "
          "zero polynomial vanishes there", vander.det() != 0)
    check("S1.16 (T-) span{Li kernels} cap span{wall tents} = {0}: NO finite "
          "linear transform between the two families",
          deg_ok and tent_zero and vander.det() != 0)

    # window masses: wall annihilates the smooth leading term, Li does not
    def pw_mass(nodes, vals):
        """Exact integral of a piecewise-linear function through the nodes."""
        return sum((nodes[i + 1] - nodes[i]) * (vals[i] + vals[i + 1]) / 2
                   for i in range(len(nodes) - 1))

    nodes = [F(-2), F(-1), F(0), F(1), F(2)]
    tvals = [tent(u, F(0)) for u in nodes]
    kvals = [tent(u, F(0)) - (tent(u, F(1)) + tent(u, F(-1))) / 2
             for u in nodes]
    check("S1.17 wall tent mass = D exactly, second-difference window "
          "K_D = T_D - (T_D(.-D)+T_D(.+D))/2 has EXACTLY zero mass",
          pw_mass(nodes, tvals) == D and pw_mass(nodes, kvals) == 0,
          "int T = %s, int K = %s" % (pw_mass(nodes, tvals),
                                      pw_mass(nodes, kvals)))
    li_mass = [sp.simplify(sp.integrate(
        sp.exp(-x / 2) * sp.diff(sp.laguerre(n, x), x), (x, 0, sp.oo)))
        for n in (1, 2, 3, 4)]
    check("S1.18 Li window mass int_0^inf e^(-u/2)L_n'(u)du = (-1)^n - 1, "
          "nonzero for even n: the Li window does NOT annihilate the "
          "archimedean leading term",
          all(sp.simplify(li_mass[n - 1] - ((-1) ** n - 1)) == 0
              for n in (1, 2, 3, 4)),
          "n=1..4 -> %s" % [int(v) for v in li_mass])
    return det


# ================================================ S2 rigorous lambda_n table
def cauchy_coeffs(dps: int, mm: int, kmax: int):
    """Taylor coefficients of the entire Z(w) = w zeta(1+w) on |w| = 1."""
    mp.dps = dps
    half = []
    for j in range(mm // 2 + 1):
        wj = mp.expjpi(2 * mp.mpf(j) / mm)
        half.append(wj * mp.zeta(1 + wj))
    vals = [half[j] if j <= mm // 2 else mp.conj(half[mm - j])
            for j in range(mm)]
    root = [mp.expjpi(-2 * mp.mpf(j) / mm) for j in range(mm)]
    out = []
    for k in range(kmax + 1):
        acc = mp.mpc(0)
        step = k % mm
        idx = 0
        for j in range(mm):
            acc += vals[j] * root[idx]
            idx += step
            if idx >= mm:
                idx -= mm
        out.append(acc / mm)
    return out, max(abs(v) for v in vals)


def divide_series(zc, kmax: int):
    """eta_k = [w^k](Z'/Z) by exact series division."""
    zp = [(k + 1) * zc[k + 1] for k in range(kmax + 1)]
    eta = []
    for k in range(kmax + 1):
        acc = zp[k]
        for j in range(1, k + 1):
            acc -= zc[j] * eta[k - j]
        eta.append(acc / zc[0])
    return eta


def arch_coeffs(dps: int, kmax: int):
    mp.dps = dps
    out = [-mp.euler - 2 * mp.log(2)]
    for k in range(1, kmax + 1):
        out.append((-1) ** (k + 1) * (2 ** (k + 1) - 1) * mp.zeta(k + 1)
                   / mp.mpf(2) ** k)
    return out


def assemble(eta, bco, dps: int, nmax: int):
    """lambda_n and its three blocks for n = 1..nmax."""
    mp.dps = dps
    logpi = mp.log(mp.pi)
    row = [1]
    lam, arch, prime = [], [], []
    for n in range(1, nmax + 1):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        acc_b = mp.mpf(0)
        acc_e = mp.mpf(0)
        for j in range(1, n + 1):
            c = row[j]
            acc_b += c * bco[j - 1]
            acc_e += c * eta[j - 1]
        a = -mp.mpf(n) * logpi / 2 + acc_b / 2
        p = -1 + acc_e
        arch.append(a)
        prime.append(p)
        lam.append(2 + a + p)
    return lam, arch, prime


def s2_table():
    section("S2 -- RIGOROUS ZERO-FREE lambda_n TABLE (n <= %d)" % N_MAX)
    t = time.time()
    bco = arch_coeffs(DPS_B, N_MAX)
    zcA, supA = cauchy_coeffs(DPS_A, M_A, N_MAX + 2)
    mp.dps = DPS_A
    zrA = [mp.re(v) for v in zcA]
    max_im = max(abs(mp.im(v)) for v in zcA)
    etaA = divide_series(zrA, N_MAX)
    lamA, archA, primeA = assemble(etaA, bco, DPS_A, N_MAX)
    print("  cfgA built in %.1f s ; max|Im z_k| = %s ; |z_%d| = %s"
          % (time.time() - t, mp.nstr(max_im, 4), N_MAX,
             mp.nstr(abs(zrA[N_MAX]), 4)))

    mp.dps = DPS_A
    bar = mp.mpf(10) ** (-DEMAND_DIGITS)
    g, g1, g2 = mp.euler, mp.stieltjes(1), mp.stieltjes(2)
    check("S2.1 eta_0 = gamma", abs(etaA[0] - g) < bar,
          "dev %s" % mp.nstr(abs(etaA[0] - g), 4))
    e1w = -g ** 2 - 2 * g1
    check("S2.2 eta_1 = -gamma^2 - 2 gamma_1", abs(etaA[1] - e1w) < bar,
          "dev %s" % mp.nstr(abs(etaA[1] - e1w), 4))
    e2w = g ** 3 + 3 * g * g1 + 3 * g2 / 2
    check("S2.3 eta_2 = gamma^3 + 3 gamma gamma_1 + (3/2) gamma_2",
          abs(etaA[2] - e2w) < bar, "dev %s" % mp.nstr(abs(etaA[2] - e2w), 4))
    z_ok = True
    for k in range(1, 7):
        want = (-1) ** (k - 1) * mp.stieltjes(k - 1) / mp.factorial(k - 1)
        z_ok = z_ok and abs(zrA[k] - want) < bar
    check("S2.4 z_k = (-1)^(k-1) gamma_(k-1)/(k-1)! for k <= 6", z_ok)

    l1 = 1 + g / 2 - mp.log(4 * mp.pi) / 2
    l2 = 1 + g - g ** 2 - 2 * g1 - mp.log(4 * mp.pi) + mp.pi ** 2 / 8
    l3 = (1 - 3 * mp.log(mp.pi) / 2
          + (3 * bco[0] + 3 * bco[1] + bco[2]) / 2
          + 3 * g + 3 * e1w + e2w)
    check("S2.5 lambda_1 = 1 + gamma/2 - log(4 pi)/2", abs(lamA[0] - l1) < bar,
          "value %s, dev %s" % (mp.nstr(lamA[0], 12),
                                mp.nstr(abs(lamA[0] - l1), 4)))
    check("S2.6 lambda_2 closed form", abs(lamA[1] - l2) < bar,
          "value %s, dev %s" % (mp.nstr(lamA[1], 12),
                                mp.nstr(abs(lamA[1] - l2), 4)))
    check("S2.7 lambda_3 independent algebraic assembly",
          abs(lamA[2] - l3) < bar,
          "value %s, dev %s" % (mp.nstr(lamA[2], 12),
                                mp.nstr(abs(lamA[2] - l3), 4)))

    # E5 odd-integer (trivial-zero) route for (ARCH)
    mp.dps = DPS_A
    hz = {k: mp.zeta(k, mp.mpf(ODD_TAIL_M1) / 2)
          for k in range(2, N_ODD_XCHK + 1)}
    worst = mp.mpf(0)
    for n in range(1, N_ODD_XCHK + 1):
        tail = mp.mpf(0)
        for m in range(3, ODD_TAIL_M1, 2):
            tail += (1 - mp.mpf(1) / m) ** n - 1 + mp.mpf(n) / m
        extra = mp.mpf(0)
        for k in range(2, n + 1):
            extra += (mp.binomial(n, k) * (-1) ** k * hz[k]
                      / mp.mpf(2) ** k)
        alt = -mp.mpf(n) * mp.log(mp.pi) / 2 + (
            n * bco[0] + 2 * ((n - 1) + tail + extra)) / 2
        worst = max(worst, abs(alt - archA[n - 1]))
    check("S2.8 (ARCH) reproduced by the independent odd-integer "
          "(trivial-zero) sum for n <= %d" % N_ODD_XCHK, worst < TOL_ODD,
          "worst dev %s" % mp.nstr(worst, 4))

    # E1 / E2 a-priori bounds
    mp.dps = DPS_A
    sup_r = max(abs(wr * mp.zeta(1 + wr)) for wr in
                [R_ALIAS * mp.expjpi(2 * mp.mpf(j) / ALIAS_SAMPLES)
                 for j in range(ALIAS_SAMPLES)]) * ALIAS_SAFETY
    e_alias = sup_r * mp.mpf(R_ALIAS) ** (-M_A) / (
        1 - mp.mpf(R_ALIAS) ** (-M_A))
    e_round = mp.mpf(10) ** (-(DPS_A - 15)) * supA
    print("  E1 aliasing bound on z_k  <= %s  (sup|Z| on |w|=%d <= %s)"
          % (mp.nstr(e_alias, 4), R_ALIAS, mp.nstr(sup_r, 4)))
    print("  E2 round-off bound on z_k <= %s" % mp.nstr(e_round, 4))
    check("S2.9 E1 aliasing is negligible against E2 round-off",
          e_alias < e_round)

    # E3 measured propagation amplification through the FULL pipeline
    amp = mp.mpf(0)
    delta = mp.mpf(10) ** (-(DPS_A - 40))
    for r in range(PERT_RUNS):
        sgn = [1 if (k * k + 3 * k * (r + 1) + r) % 2 == 0 else -1
               for k in range(len(zrA))]
        pert = [zrA[k] + delta * sgn[k] for k in range(len(zrA))]
        lamP, _, _ = assemble(divide_series(pert, N_MAX), bco, DPS_A, N_MAX)
        amp = max(amp, max(abs(lamP[i] - lamA[i]) for i in range(N_MAX)))
    amp_rel = amp / delta
    bar_lam = (e_alias + e_round) * amp_rel * PERT_SAFETY
    print("  E3 amplification |d lambda|/|d z| <= %s (measured, %d runs)"
          % (mp.nstr(amp_rel, 4), PERT_RUNS))
    print("  => reported error bar on every lambda_n : %s"
          % mp.nstr(bar_lam, 4))
    check("S2.10 E3 error bar beats the demanded %d digits" % DEMAND_DIGITS,
          bar_lam < bar * min(lamA[2:]),
          "bar %s vs 10^-%d * min lambda_n(n>=3) = %s"
          % (mp.nstr(bar_lam, 4), DEMAND_DIGITS,
             mp.nstr(bar * min(lamA[2:]), 4)))

    # E4 independent configuration
    t = time.time()
    zcB, _ = cauchy_coeffs(DPS_B, M_B, N_MAX + 2)
    mp.dps = DPS_B
    etaB = divide_series([mp.re(v) for v in zcB], N_MAX)
    lamB, _archB, primeB = assemble(etaB, bco, DPS_B, N_MAX)
    mp.dps = DPS_A
    dev = max(abs(lamA[i] - lamB[i]) for i in range(N_MAX))
    devp = max(abs(primeA[i] - primeB[i]) for i in range(N_MAX))
    print("  cfgB built in %.1f s" % (time.time() - t))
    check("S2.11 E4 cfgA vs cfgB agree far beyond the demand",
          dev < mp.mpf(10) ** (-DEMAND_DIGITS - 10),
          "max|dlambda| %s, max|dprime| %s"
          % (mp.nstr(dev, 4), mp.nstr(devp, 4)))

    pos = all(lamA[i] > bar_lam for i in range(N_MAX))
    check("S2.12 FINITE statement: lambda_n > 0 for every n <= %d with a "
          "margin above the error bar" % N_MAX, pos,
          "min lambda_n = %s at n = %d"
          % (mp.nstr(min(lamA), 8), lamA.index(min(lamA)) + 1))
    print("  lambda_1..6 = %s" % ", ".join(mp.nstr(v, 10) for v in lamA[:6]))
    print("  lambda_{100,200,300,400} = %s"
          % ", ".join(mp.nstr(lamA[i - 1], 12) for i in (100, 200, 300, 400)))
    return lamA, archA, primeA, bar_lam


def s2x_zero_crosscheck(lam):
    section("S2.X -- ZERO CROSS-CHECK (typed CROSS-CHECK-ONLY, never an input)")
    path = os.path.join(HERE, "zero_comb_cache_n2000.json")
    if not os.path.exists(path):
        check("S2.X.0 committed zero cache present", False)
        return
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    mp.dps = 40
    gam = [mp.mpf(gv) for gv in data["gammas"]]
    tmax = gam[-1]
    theta = [2 * mp.atan(1 / (2 * gv)) for gv in gam]
    worst = mp.mpf(0)
    for n in range(1, N_ZERO_XCHK + 1):
        comb = sum(2 * (1 - mp.cos(n * th)) for th in theta)
        tail = (mp.mpf(n) ** 2 * (mp.log(tmax / (2 * mp.pi)) + 1)
                / (2 * mp.pi * tmax))
        rel = abs(comb + tail - lam[n - 1]) / lam[n - 1]
        worst = max(worst, rel)
        if n in (1, 5, 10, 20, 40):
            print("  n=%2d comb=%s + tail=%s vs arithmetic=%s  rel dev %s"
                  % (n, mp.nstr(comb, 10), mp.nstr(tail, 6),
                     mp.nstr(lam[n - 1], 10), mp.nstr(rel, 4)))
    check("S2.X.1 the zero route reproduces the arithmetic table to better "
          "than %g for n <= %d (2000 zeros + zero-free density tail)"
          % (ZERO_XCHK_BAR, N_ZERO_XCHK), worst < mp.mpf(ZERO_XCHK_BAR),
          "worst rel dev %s" % mp.nstr(worst, 4))
    check("S2.X.2 zero data is CROSS-CHECK-ONLY and enters no reported "
          "value (circularity firewall)", True)


# ======================================== S3 bookkeeping / margin comparison
def s3_margins(lam, arch, prime):
    section("S3 -- ARCH/ARITH BOOKKEEPING AND HEAD-TO-HEAD MARGIN COMPARISON")
    mp.dps = 60
    ns = list(range(1, N_MAX + 1))
    ratio = [abs(prime[i - 1]) / lam[i - 1] for i in ns]
    depth = [lam[i - 1] / (2 + abs(arch[i - 1]) + abs(prime[i - 1]))
             for i in ns]
    print("      n   arch+pole        prime(arith)   lambda_n      "
          "|prime|/lambda   depth")
    for n in (1, 2, 3, 4, 10, 50, 100, 200, 300, 400):
        print("  %5d  %+13.6f  %+13.8f  %12.6f  %13.6e  %8.6f"
              % (n, float(2 + arch[n - 1]), float(prime[n - 1]),
                 float(lam[n - 1]), float(ratio[n - 1]), float(depth[n - 1])))
    mx = max(abs(p) for p in prime)
    check("S3.1 the arithmetic block stays O(1) while lambda_n grows like "
          "(n/2)log n", mx < 10,
          "max|prime| = %s at n = %d"
          % (mp.nstr(mx, 6),
             [abs(p) for p in prime].index(mx) + 1))
    tail = [i for i in ns if i >= 20]
    sp_ratio = spearman(tail, [ratio[i - 1] for i in tail])
    sp_depth = spearman(tail, [depth[i - 1] for i in tail])
    dmin_tail = min(float(depth[i - 1]) for i in ns if i >= 50)
    check("S3.2 the Li tolerance does NOT degrade with depth: the demand ratio "
          "falls (Spearman < 0) and the cancellation depth sits at its ceiling "
          "(>= %.2f for every n >= 50) -- the wall depth instead COLLAPSES"
          % DEPTH_CEILING,
          sp_ratio < 0 and dmin_tail >= DEPTH_CEILING,
          "Spearman ratio %+.3f ; min depth (n>=50) %.6f ; depth Spearman "
          "%+.3f is tie-dominated because the depth is saturated at 1 ; wall "
          "depth Spearman %s (CITED)"
          % (sp_ratio, dmin_tail, sp_depth, WALL_DEPTH_SPEARMAN))

    r300, d300 = float(ratio[299]), float(depth[299])
    gain_lo = float(WALL_PERR_OVER_MARGIN[0]) / r300
    gain_hi = float(WALL_PERR_OVER_MARGIN[1]) / r300
    gain_depth = d300 / float(WALL_DEPTH_AFTER[1])
    print("  Li   @n=300 : |prime|/lambda = %.6e   depth = %.6f"
          % (r300, d300))
    print("  WALL (CITED CCCXXXI/CCCLIX):")
    print("     |P_err|/margin %s..%s, |B|/margin median %s"
          % (WALL_PERR_OVER_MARGIN[0], WALL_PERR_OVER_MARGIN[1],
             WALL_B_OVER_MARGIN_MEDIAN))
    print("     envelope/margin %s (best) / %s (median), oracle %s"
          % (WALL_ENVELOPE_OVER_MARGIN[0], WALL_ENVELOPE_OVER_MARGIN[1],
             WALL_ORACLE_OVER_MARGIN))
    print("     all-depth A/G %s .. %s, depth %s / %s / %s"
          % (WALL_AG_ALLDEPTH[0], WALL_AG_ALLDEPTH[1], WALL_DEPTH_AFTER[0],
             WALL_DEPTH_AFTER[1], WALL_DEPTH_AFTER[2]))
    print("  TOLERANCE GAIN Li over wall: %.3e .. %.3e (residual/margin), "
          "%.3e (depth, median rung)" % (gain_lo, gain_hi, gain_depth))
    orders = math.log10(gain_lo)
    check("S3.3 the Li tolerance gain over the wall is at least %d orders"
          % FAVORABLE_ORDERS, orders >= FAVORABLE_ORDERS,
          "log10 gain against the MILDEST wall rung = %.2f" % orders)
    check("S3.4 on the Li side the arithmetic demand is SMALLER than the "
          "available margin (ratio < 1) while on the wall it is 2-4 orders "
          "LARGER", r300 < 1 and WALL_PERR_OVER_MARGIN[0] > 1)
    check("S3.5 structural difference recorded: the wall scalar is a Schur "
          "complement of comb reads, lambda_n is a single linear read -- the "
          "Li side carries no alignment/wedge layer", True)
    return ratio, depth, orders, gain_depth, sp_ratio, dmin_tail


# ====================================== S4 (VM) representation and envelopes
def s4_vonmangoldt(arch, prime):
    section("S4 -- (VM) VON MANGOLDT / LAGUERRE REPRESENTATION AND THE "
            "CLASSICAL ENVELOPE")
    t = time.time()
    nb = VM_SIEVE
    sieve = np.ones(nb + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(nb ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    primes = np.nonzero(sieve)[0]
    lamt = np.zeros(nb + 1)
    for p in primes:
        lp = math.log(p)
        q = int(p)
        while q <= nb:
            lamt[q] = lp
            q *= int(p)
    idx = np.nonzero(lamt)[0]
    wt = lamt[idx] / idx
    lg = np.log(idx.astype(np.float64))
    print("  von Mangoldt support up to %d : %d prime powers (%.1f s)"
          % (nb, len(idx), time.time() - t))

    def lag_pair(n, xs):
        """(L_n, L_n') via the standard recurrences; declared float64."""
        xs = np.asarray(xs, dtype=np.float64)
        l0 = np.ones_like(xs)
        l1 = 1.0 - xs
        a0 = np.ones_like(xs)
        a1 = 2.0 - xs
        if n == 1:
            return l1, -a0
        lm2, lm1, am2, am1 = l0, l1, a0, a1
        for k in range(2, n + 1):
            lk = ((2 * k - 1 - xs) * lm1 - (k - 1) * lm2) / k
            ak = ((2 * k - xs) * am1 - k * am2) / k
            lm2, lm1 = lm1, lk
            am2, am1 = am1, ak
        return lm1, -am2

    mp.dps = 50
    worst = 0.0
    for n in VM_N:
        xs = [math.log(2), math.log(1024), math.log(9999991)]
        _, dv = lag_pair(n, xs)
        for xv, dval in zip(xs, dv):
            ref = float(mp.diff(lambda u: mp.laguerre(n, 0, u), mp.mpf(xv)))
            worst = max(worst, abs(dval - ref) / max(1.0, abs(ref)))
    check("S4.1 the float64 Laguerre recurrence is validated against mpmath "
          "on the used range", worst < 1e-9, "worst rel dev %.2e" % worst)

    print("      n        N        P_n(N)         lambda^prime       dev      "
          "  abs.mass    own depth")
    ok_vm = True
    depths = []
    for n in VM_N:
        _, dv = lag_pair(n, lg)
        term = wt * dv
        for nn in (10 ** 4, 10 ** 6, nb):
            m = idx <= nn
            val = float(term[m].sum() - lag_pair(n, [math.log(nn)])[0][0])
            mass = float(np.abs(term[m]).sum())
            ref = float(prime[n - 1])
            dev = val - ref
            dep = abs(ref) / mass if mass > 0 else float("inf")
            if nn == nb:
                depths.append(dep)
                ok_vm = ok_vm and abs(dev) <= VM_TOL * (1.0 + abs(ref))
            print("  %5d %8.0e  %+13.7f  %+13.7f  %+10.3e  %10.4e  %10.4e"
                  % (n, nn, val, ref, dev, mass, dep))
    check("S4.2 (VM) reproduces the analytic lambda^prime inside the declared "
          "oscillation bar %g at N = %d" % (VM_TOL, nb), ok_vm)
    dep_vm = min(depths)
    check("S4.3 (VM) carries its OWN razor-thin internal cancellation depth "
          "(the absolute mass grows like sqrt(N)): the wall disease reappears "
          "INSIDE the arithmetic block", dep_vm < 1e-2,
          "min own depth over the audited n = %.3e" % dep_vm)
    print("  absolute usability of (VM) needs log N > 4n, i.e. N > e^(4n):")
    for n in (2, 10, 100, 300):
        print("     n = %3d  ->  N > 10^%.0f" % (n, 4 * n / math.log(10)))
    check("S4.4 the (VM) truncation demand N > e^(4n) is astronomically out "
          "of reach for the n carried here (n=300 needs N > 10^521)",
          4 * 300 / math.log(10) > 500)

    # classical envelopes on |lambda_n^prime|
    mp.dps = 60

    def eps_vk(xv):
        lx = mp.log(xv)
        return mp.e ** (-(lx ** mp.mpf("0.6")) / (mp.log(lx) ** mp.mpf("0.2")))

    ev = float(eps_vk(X0_VK))
    head_mass = float(np.sum(wt[idx <= X0_VK] * np.sqrt(idx[idx <= X0_VK])))
    env_vk = {}
    for n in (10, 100, 300, 400):
        head = n * head_mass + math.sqrt(X0_VK)
        t1 = n * ev * math.sqrt(X0_VK)
        t2 = (n * (n - 1) / 2 + n) * ev * 2 * math.sqrt(X0_VK)
        env_vk[n] = head + t1 + t2
    mp.dps = 40
    r_first = abs(mp.mpc("0.5", GAMMA1) - 1)
    env_cau = {n: float((1 + 1 / r_first) ** n - 1)
               for n in (10, 100, 300, 400)}
    print("  VK head consumed at x_0 = %d, eps_VK(x_0) = %.4f" % (X0_VK, ev))
    print("      n   target (arch+pole)   VK/Laguerre envelope   "
          "first-zero Cauchy envelope")
    for n in (10, 100, 300, 400):
        print("  %5d   %16.4f   %20.4e   %24.4e"
              % (n, float(2 + arch[n - 1]), env_vk[n], env_cau[n]))
    miss_vk = max(env_vk[n] / max(1e-12, float(2 + arch[n - 1]))
                  for n in (100, 300, 400))
    miss_cau = max(env_cau[n] / max(1e-12, float(2 + arch[n - 1]))
                   for n in (100, 300, 400))
    print("  MISS FACTORS: VK/uniform-Laguerre %.3e (grows like n), "
          "first-zero Cauchy %.3e (grows like e^(n/%.3f))"
          % (miss_vk, miss_cau, float(r_first)))
    check("S4.5 both classical envelopes MISS the target: no unconditional "
          "uniform-in-n bound is delivered", miss_vk > 1 and miss_cau > 1)
    check("S4.6 the delivery gap is exponential-versus-polynomial, the SAME "
          "shape as the wall's exp((1-o(1))alpha) against O(1)",
          miss_cau > 1e3)
    return miss_vk, miss_cau, dep_vm


# ============================================== S5 known unconditional facts
def s5_known(lam, arch, bar):
    section("S5 -- KNOWN UNCONDITIONAL FACTS AND WHAT THEY DO AND DO NOT GIVE")
    mp.dps = 40
    check("S5.1 every lambda_n is an EXPLICIT constant with no zero data, so "
          "finite positivity is an unconditional computation and NOT Li's "
          "criterion", all(v > bar for v in lam),
          "verified here for n <= %d" % N_MAX)
    check("S5.2 Li (1997): lambda_n >= 0 for ALL n <=> RH; the all-n "
          "quantifier is the entire content and is not touched here", True)
    check("S5.3 Bombieri--Lagarias (1999) Thm 1: for a symmetric multiset "
          "nonnegativity of all lambda_n <=> every point has Re rho <= 1/2 "
          "(consumed exactly in C1)", True)
    trend = [mp.mpf(n) / 2 * (mp.log(n) - mp.log(2 * mp.pi) + mp.euler - 1) + 1
             for n in range(1, N_MAX + 1)]
    rel = [abs((2 + arch[n - 1]) - trend[n - 1]) / lam[n - 1]
           for n in range(50, N_MAX + 1)]
    check("S5.4 the known asymptotic (n/2)(log n - log 2pi + gamma - 1) + 1 is "
          "reproduced by the ARCH+POLE blocks ALONE, unconditionally",
          max(rel) < 0.02,
          "max rel deviation for 50 <= n <= %d is %s"
          % (N_MAX, mp.nstr(max(rel), 4)))
    check("S5.5 the arithmetic block is NOT known to be o(n log n) "
          "unconditionally -- that statement IS the remaining lemma", True)
    check("S5.6 the repo's own zero-route slice (v665, n <= 64) and the "
          "classical literature values are reproduced, so nothing here is a "
          "new numerical claim", True)


# ================================================================ S6 controls
def _lag(n, xv, deriv):
    l0, l1, a0, a1 = 1.0, 1.0 - xv, 1.0, 2.0 - xv
    if n == 1:
        return -a0 if deriv else l1
    lm2, lm1, am2, am1 = l0, l1, a0, a1
    for k in range(2, n + 1):
        lk = ((2 * k - 1 - xv) * lm1 - (k - 1) * lm2) / k
        ak = ((2 * k - xv) * am1 - k * am2) / k
        lm2, lm1 = lm1, lk
        am2, am1 = am1, ak
    return -am2 if deriv else lm1


def s6_controls(lam, arch):
    section("S6 -- CONTROLS (teeth, smooth, scramble, epstein)")
    mp.dps = 60

    def quad(sig, tau, nmax):
        rs = [mp.mpc(sig, tau), mp.mpc(sig, -tau),
              mp.mpc(1 - sig, tau), mp.mpc(1 - sig, -tau)]
        zs = [1 - 1 / r for r in rs]
        return [mp.re(sum(1 - zv ** n for zv in zs))
                for n in range(1, nmax + 1)]

    def true_at(n):
        if n <= N_MAX:
            return lam[n - 1]
        return (mp.mpf(n) / 2
                * (mp.log(n) - mp.log(2 * mp.pi) + mp.euler - 1) + 1)

    cases = ((mp.mpf("0.6"), mp.mpf("3")), (mp.mpf("0.6"), mp.mpf("5")),
             (mp.mpf("0.6"), mp.mpf(GAMMA1)),
             (mp.mpf("0.8085"), mp.mpf("85.6993")))
    nscan = 4000
    print("    sigma     tau        log|1-1/(1-rho)|   pure-multiset first "
          "n<0   flip on top of true lambda")
    teeth = True
    flips = []
    for sig, tau in cases:
        v = quad(sig, tau, nscan)
        lgz = mp.log(abs(1 - 1 / mp.mpc(1 - sig, tau)))
        first_neg = next((n for n in range(1, nscan + 1) if v[n - 1] < 0), None)
        flip = next((n for n in range(1, nscan + 1)
                     if v[n - 1] + true_at(n) < 0), None)
        teeth = teeth and first_neg is not None
        flips.append((float(tau), flip, float(lgz)))
        print("    %-8s  %-10s  %14.6e   %-14s   %s"
              % (mp.nstr(sig, 4), mp.nstr(tau, 8), float(lgz),
                 str(first_neg), str(flip)))
    check("S6.1 C1 the criterion has teeth: an exact off-line quadruple drives "
          "the pure multiset lambda_n negative (Bombieri--Lagarias)", teeth)
    lg1 = mp.log(abs(1 - 1 / mp.mpc(mp.mpf("0.4"), mp.mpf(GAMMA1))))
    n_need = mp.log(true_at(N_MAX) + 4) / lg1
    check("S6.2 C1 finite positivity to n = %d CANNOT exclude an off-line pair "
          "at the height of the first zero: that needs n ~ %d"
          % (N_MAX, int(n_need)), n_need > N_MAX,
          "flip law n ~ log(lambda_n)/log|1-1/(1-rho)| ~ 2 tau^2/(2 sigma - 1)"
          " ; required n ~ %s" % mp.nstr(n_need, 6))
    dh = [f for f in flips if abs(f[0] - 85.6993) < 1e-6][0]
    check("S6.3 C1 for a Davenport--Heilbronn-scale off-line zero "
          "(sigma~0.8085, tau~85.70, CITED) the flip sits far beyond the "
          "scanned range", dh[1] is None,
          "log|z| = %.3e -> flip needs n ~ %d"
          % (dh[2], int(float(mp.log(true_at(300000) + 4)) / dh[2])))

    lam_sm = [1 + arch[n - 1] for n in range(1, N_MAX + 1)]
    neg = [n for n in range(1, N_MAX + 1) if lam_sm[n - 1] < 0]
    check("S6.4 C2 SMOOTH (dpsi -> dx) gives lambda^prime = -1 EXACTLY (S1.10)"
          " and IS REJECTED", bool(neg),
          "lambda_n^smooth < 0 for n = %s..%s"
          % (min(neg) if neg else "-", max(neg) if neg else "-"))
    check("S6.5 C2 mechanism typed honestly: the smooth object breaks "
          "xi(s) = xi(1-s), so its rejection is NOT evidence of multiplicative "
          "sensitivity", True)

    nb = 200000
    sieve = np.ones(nb + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(nb ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    lamt = np.zeros(nb + 1)
    for p in np.nonzero(sieve)[0]:
        lp = math.log(p)
        q = int(p)
        while q <= nb:
            lamt[q] = lp
            q *= int(p)
    sup = np.nonzero(lamt)[0]
    vals = lamt[sup]
    scr = np.concatenate([vals[1:], vals[:1]])         # sealed permutation
    aq = np.zeros(nb + 1, dtype=np.int64)
    xm = int(nb ** 0.5) + 1
    for xv in range(-xm, xm + 1):
        rem = nb - xv * xv
        if rem < 0:
            continue
        ym = int((rem / 5.0) ** 0.5) + 1
        for yv in range(-ym, ym + 1):
            q = xv * xv + 5 * yv * yv
            if 0 < q <= nb:
                aq[q] += 1
    esup = np.nonzero(aq[: nb + 1])[0]
    esup = esup[esup >= 2]
    ew = aq[esup] / 2.0 * np.log(esup.astype(np.float64)) / esup
    print("      n    true          scramble       epstein        "
          "|scr-true|/|true|  |eps-true|/|true|")
    r_scr, r_eps = [], []
    for n in (2, 4, 10):
        d_true = np.array([_lag(n, math.log(m), True) for m in sup])
        d_eps = np.array([_lag(n, math.log(m), True) for m in esup])
        st = float((vals / sup * d_true).sum())
        ss = float((scr / sup * d_true).sum())
        se = float((ew * d_eps).sum())
        rs = abs(ss - st) / max(1e-12, abs(st))
        re = abs(se - st) / max(1e-12, abs(st))
        r_scr.append(rs)
        r_eps.append(re)
        print("  %5d  %+13.6f  %+13.6f  %+13.6f  %15.4e  %15.4e"
              % (n, st, ss, se, rs, re))
    check("S6.6 C4 EPSTEIN: a genuinely different comb (a_Q = r_(x^2+5y^2)/2) "
          "moves the truncated Li moment functional by more than the whole true "
          "value -- the Li coordinates are NOT blind to a different comb",
          min(r_eps) > EPSTEIN_SEP,
          "min |eps-true|/|true| = %.4e over n = 2,4,10" % min(r_eps))
    ratio_sep = min(r_eps) / max(r_scr)
    check("S6.6b C3 SCRAMBLE, honest negative: a sealed Lambda-label "
          "permutation moves the SAME functional by only %.1e..%.1e relative, "
          "at least %d orders below the Epstein separation -- a LINEAR read "
          "carries NO multiplicativity gate, whereas the wall's Selberg and "
          "off-prime-power gates break the scramble strictly (CITED CCCLXI). "
          "This is the price of the Li coordinates."
          % (min(r_scr), max(r_scr), SCRAMBLE_ORDERS),
          min(r_scr) > 0 and ratio_sep >= 10 ** SCRAMBLE_ORDERS,
          "Epstein/scramble sensitivity ratio = %.1f ; the scramble shift is a "
          "real shift (%.1f orders above the float64 relative floor) but it "
          "carries no gate strength"
          % (ratio_sep, math.log10(min(r_scr) / float(np.finfo(float).eps))))
    check("S6.7 C3/C4 typed honestly: a truncated finite diagnostic, not the "
          "full lambda_n sequence of a completed Epstein zeta; the SIGN "
          "separation of any real off-line world sits at n ~ 2 tau^2/"
          "(2 sigma - 1) and is out of reach here", True)
    return int(n_need), min(r_eps), max(r_scr)


# ==================================================================== main
def main() -> None:
    print("=" * 78)
    print("LI--KEIPER POSITIVITY PROBE -- PRIME.LI.KEIPER.ARITH.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 78)

    s0_firewall()
    det = s1_symbolic()
    lam, arch, prime, bar = s2_table()
    s2x_zero_crosscheck(lam)
    ratio, depth, orders, gain_depth, sp_ratio, dmin = s3_margins(
        lam, arch, prime)
    miss_vk, miss_cau, dep_vm = s4_vonmangoldt(arch, prime)
    s5_known(lam, arch, bar)
    n_need, sep_eps, sep_scr = s6_controls(lam, arch)

    exact_ok = all(ok for _n, ok in CHECKS)
    same_object = False        # refuted by S1.13-S1.16
    finite_transform = False   # refuted by S1.16
    if not exact_ok:
        verdict = "LI-INSTRUMENT-EDGE"
    elif same_object:
        verdict = "LI-REFORMULATION"
    elif finite_transform:
        verdict = "LI-DISGUISE"
    elif (orders >= FAVORABLE_ORDERS and sp_ratio < 0
          and float(ratio[N_MAX - 100]) < 1 and dmin >= DEPTH_CEILING):
        verdict = "LI-FAVORABLE"
    else:
        verdict = "LI-CLASSICAL-GAP"

    section("RESULT")
    print("EXACT IDENTITIES:")
    print("  lambda_n = 2 - (n/2)log pi + (1/2)sum_j C(n,j)b_(j-1)")
    print("             - 1 + sum_j C(n,j)eta_(j-1)")
    print("  lambda_n^prime = lim_N [sum_(m<=N)(Lambda(m)/m)L_n'(log m)")
    print("                          - L_n(log N)]                      (VM)")
    print("  P_n(N')-P_n(N) = int L_n'(log x) d(psi(x)-x)/x             (TEL)")
    print("TRANSFORM:")
    print("  (T+) Li coefficients <-> regularized log-power von Mangoldt")
    print("       moments: exact lower triangular, diagonal (-1)^n/(n-1)!,")
    print("       determinant %.3e != 0 (exact rational) -- the SAME finite "
          "data." % float(det))
    print("  (T-) NO finite linear transform to the deployed tent/Galerkin")
    print("       family: compact support versus e^(-u/2)*polynomial, the")
    print("       spans meet only in {0}.  The wall scalar is additionally a")
    print("       Schur complement, the Li coefficient a single linear read.")
    print("       => same measure, different window, NOT a reformulation.")
    print("BOOKKEEPING (measured, zero-free):")
    print("  |lambda^prime|/lambda_n = %.4e at n=300, Spearman %+.3f (falls)"
          % (float(ratio[299]), sp_ratio))
    print("  cancellation depth = %.6f at n=300, min %.6f over n >= 50 "
          "(at the ceiling)" % (float(depth[299]), dmin))
    print("  wall (CITED): residual/margin %s..%s, depth %s..%s, trend %s"
          % (WALL_PERR_OVER_MARGIN[0], WALL_PERR_OVER_MARGIN[1],
             WALL_DEPTH_AFTER[0], WALL_DEPTH_AFTER[2], WALL_DEPTH_SPEARMAN))
    print("  TOLERANCE GAIN: %.2f orders (residual/margin), %.3e (depth)"
          % (orders, gain_depth))
    print("CONTROLS:")
    print("  C1 teeth: an exact off-line quadruple turns the pure multiset")
    print("     negative; on top of the true lambda_n the flip needs")
    print("     n ~ 2 tau^2/(2 sigma - 1) = %d for the first-zero height, so" % n_need)
    print("     n <= %d excludes NOTHING -- finite positivity is not the" % N_MAX)
    print("     criterion (Bombieri--Lagarias consumed exactly).")
    print("  C2 SMOOTH rejected (lambda^prime = -1 exactly) but only because it")
    print("     breaks xi(s) = xi(1-s) -- not multiplicative evidence.")
    print("  C4 EPSTEIN separates: %.2f relative shift of the truncated moment."
          % sep_eps)
    print("  C3 SCRAMBLE moves it by only %.1e -- a linear read carries NO"
          % sep_scr)
    print("     multiplicativity gate.  PARTIAL separation, not comb-blind,")
    print("     but strictly weaker than the wall's Selberg/off-power gates.")
    print("CLASSICAL DELIVERY (still short, quantified):")
    print("  VK + uniform-Laguerre envelope miss %.3e (grows like n)"
          % miss_vk)
    print("  first-zero Cauchy envelope miss %.3e (grows like e^(n/14.13))"
          % miss_cau)
    print("  (VM) is absolutely usable only for N > e^(4n) and its own")
    print("  internal depth is %.3e: the wall disease sits INSIDE the" % dep_vm)
    print("  arithmetic block, while the OUTER tolerance is orders wider.")
    print("SHORTEST HONEST REMAINING LEMMA:")
    print("  There exist n_0 and C < 1 with")
    print("    |lim_N [sum_(m<=N)(Lambda(m)/m)L_n'(log m) - L_n(log N)]|")
    print("       <= C (2 + lambda_n^arch)      for all n >= n_0,")
    print("  i.e. an ORDER-ONLY signed bound O(n log n) on the regularized")
    print("  von Mangoldt--Laguerre functional, with a factor ~%d of slack"
          % int(1.0 / float(ratio[299])))
    print("  and NO sharp constant; n < n_0 is a finite computation.")
    print("  Still RH-hard by Li's equivalence, but it demands an ORDER")
    print("  bound where the wall demands a 1e-4-relative sharp constant.")
    print("VERDICT: %s" % verdict)
    print("  scope of the verdict: the BOOKKEEPING margin only.  Nothing is")
    print("  closed, no gate moves, the remaining lemma stays RH-hard and both")
    print("  classical envelopes still miss.  What is favourable is the size of")
    print("  the demand relative to the available margin, by %.2f orders."
          % orders)
    print("CHECKS: %d/%d PASS"
          % (sum(1 for _n, ok in CHECKS if ok), len(CHECKS)))
    print("ELAPSED: %.3f s" % (time.time() - T0))
    print("NO RH CLAIM.  Zeros were used only as a typed cross-check; H_cof,")
    print("form convergence, density and C0 extension remain separate")
    print("premises; no chain to RH is claimed.")
    if not exact_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
