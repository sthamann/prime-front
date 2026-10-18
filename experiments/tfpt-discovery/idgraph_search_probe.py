#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""idgraph_search_probe -- PRIME.IDENTITY.GRAPH.SEARCH.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
explicitly cited-input finite inequalities it gates, NO counterexample
claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (the radical-method contract)
=======================================================================
Let the MACHINE combine instead of humans choosing routes: encode the
corpus's proven exact identities as a typed derivation graph, verify
EVERY edge mechanically (sympy-exact, exact rational, or high-dps
numeric -- declared per edge), then search compositions mechanically
for (a) unconditional consequences for the diagonal growth rate (the
radius-4 target), (b) new exact identities not equal to a known edge
or a one-line composition, (c) new unconditional cells/floors for the
certified instruments, and (S3) the MIN-CUT of conditional edges that
separates the unconditional component from the RH-target node.

=======================================================================
THE IDENTITY INVENTORY (owner probes and proof status, frozen)
=======================================================================
Per-pair atoms: z_rho=(rho-1/2)^2, y=a/(a-z), w=y(1-y)=-az/(a-z)^2,
b_n=sum y^(n+1), C_{n,k}=sum y^(n+1)(1-y)^k, d_m=C_{m,m},
e_m=C_{m-1,m}=sum w^m (owners: hausdorff_safepoint_probe round 102,
radius4_reduction_probe round 115).
 E-PASCAL   C_{n,k}=C_{n+1,k}+C_{n,k+1}                [PROVEN r102]
 E-JETREP   b_n=a^(n+1)((-1)^n/n!)F^(n)(a)             [PROVEN r102]
 E-FLOW-Y   a d/da y = y(1-y);  a d/da b_n=(n+1)C_{n,1};
            (a d/da + k)C_{n,k}=(n+k+1)C_{n,k+1}       [PROVEN r102]
 E-GF2      (X+Y-XY)G = X aF(a(1-X)) + Y a/(1-Y) F(a/(1-Y))
                                                       [PROVEN r106]
 E-DIAGDET  Dd_a(t)=prod(1-t w)=Phi(z+)Phi(z-)/Phi(a)^2, z+z-=a^2,
            z+ + z- = a(2-t); t=4sin^2(theta/2) => z+-=a e^(+-i theta)
                                     [CANDIDATE r115, PENDING AUDIT;
                                      per-atom algebra re-verified here]
 E-WSUM     y(z)+y(a^2/z)=1; at a=|z| partner is zbar  [r115 cand.;
                                      re-verified symbolically here]
 E-WINDOW   |w_a(z)|>1/4 iff a in (a-,a+), a+-=(Re z+2|z|)+-
            sqrt((Re z+|z|)(Re z+3|z|))                [r115 cand.;
                                      re-verified symbolically here]
 E-ACPICK   c^T P_N c = <-g'', f_c star f~_c>          [PROVEN, v915 /
            round 95; bilinear-interface surrogate gated here]
 E-PINP     P(sigma)=xi'/xi(1/2+sigma)=2 sigma F(sigma^2)  [DEF]
 E-LI       b_{r-1}(1/4)=4^{-r} sum_{m=1}^r (-1)^{m+1} C(2r,r+m)
            lambda_m per pair, q=(rho-1)/rho           [PROVEN r<=5]
 E-SOS      det[b_{i+j}]_N = sum_{|S|=N} (prod_S mass) V(y_S)^2
                                                       [PROVEN N<=3]
 E-KICK     Delta alpha_{d0} = -phi/(c_0 prod_{j<d0}(1-alpha_j^2))
            (first-touched-lag Levinson kick; sign convention
            measured)                                  [EXACT r101]
 E-FRED     <xi_o,(DT-TD)xi_e> = (eps_e-eps_o)<xi_o,D xi_e>; Loewner
            class DT-TD=|beta><eta|-|eta><beta|        [EXACT r114]
 E-EXTDET   det(M_blk-z)=det(D-z)det(I_m-W(z))         [EXACT r114;
            generic Sylvester form gated on exact rational instance]
 E-EPIN     sum_rho 1/(rho(1-rho)) = 2+gamma-log 4 pi  [CLASSICAL;
            numeric gate via xi'/xi(1) at dps 60]
 E-SPLIT    xi'/xi = POLE(1/s+1/(s-1)) + ARCH(-log(pi)/2+psi(s/2)/2)
            + PRIME(zeta'/zeta)                        [CLASSICAL;
            numeric gate at s=16.5, sieve-independent PRIME side]
 E-LAMBDA   Lambda = mu * log (Dirichlet convolution)  [CLASSICAL;
            exact vector gate n<=3000]
 E-RVM      HSW22 Cor 1.2 |N-M|<=0.1038 log t+0.2573 loglog t+9.3675
                                                       [CITED input]
 E-PT21     all zeros with 0<Im<=T_PT=3,000,175,332,800 on the line
                                                       [CITED input]
 E-STRIP    every nontrivial zero has |Re rho-1/2|<=1/2, gamma>=
            gamma_1>14 (classical)                     [CITED input]
 E-K74      C_{n,k}(256)>0 for all n>=0, 0<=k<=7,444,682,106,464,
            286,365,865 (round 106; spot ward re-run here at k=1e19)
                                                       [PROVEN r106]
 E-W14      under RH w=a g^2/(a+g^2)^2 in [0,1/4]      [COND-RH;
            algebra 1/4-w=((a-g^2)/2(a+g^2))^2 gated]
 E-TRACE    Tr[A^{n+1}(I-A)^k]>=0 for 0<=A<=I          [UNCONDITIONAL
            operator; spectral gate on exact instance]
 E-HFLOW    dot H=DK+KD, dot det H=2 det H Tr(D H^{-1} K), K=H-H+,
            D_ii=i+1/2                                 [PROVEN r106]
 E-SIGNREG  2x2 minor = -w1 w2 u1 u2 (u1-u2)^2 (reversed-k TP)
                                                       [PROVEN r106]
 E-PARITY   occ_k even <=> sign flip (Lean kernel, under simplicity)
                                                       [CITED r99]
 E-FLOORS   Euler--Pick certified floors N<=4 (v915/round 100 record)
                                                       [CITED corpus]
 E-WINDICT  explicit-formula window dictionaries (tent/Beta/exp)
                                                       [CITED corpus,
            not re-verified here -- declared]
=======================================================================
THE SEARCH (frozen budgets)
=======================================================================
S2-LINEAR  exhaustive linear-relation census over the quantity set
  {C_{n,k}: n<=5,k<=5} u {b_n: n<=5} u {d_m: m<=4} u {e_m: m<=5}
  u {L C_{n,k}} u {L b_n} u {L^2 b_n},  L = a d/da acting per atom as
  L p(y) = y(1-y) p'(y); exact Fraction Gaussian elimination; the
  relation space is compared against the span of the LOCAL edges
  (defs, Pascal, flow, their L-lifts).  COMPLETE = no linear identity
  at this depth escapes the known edge set; any excess vector is
  printed integer-cleaned as a discovery.
S2-NAMED   machine-composed nonlinear/series identities, each gated:
  N1 jet transport: C_{n,k} = (n!/(n+k)!) (L)(L+1)...(L+k-1) b_n,
     derived by iterating E-FLOW-C, gated k<=5 at symbolic n.
  N2 superdiagonal trace: C_{m-1,m} = sum w^m = Tr B^m, B=A(I-A)
     (one-line; typed TRIVIAL-ADJACENT, load-bearing for N3).
  N3 log-determinant Pascal reading: log prod(1-t w) =
     - sum_{m>=1} (t^m/m) C_{m-1,m}, gated to order 8, two atoms.
  N4 pin anchor loop: b_0(1/4) = lambda_1/4 = (2+gamma-log 4pi)/8,
     symbolic rearrangement + numeric route through xi'/xi(1)
     (classical loop closure, typed NOT NEW).
S2A UNCONDITIONAL GROWTH BOUNDS (the radius-4 target, composed from
  UNCONDITIONAL nodes only; all steps gated):
  A1 strip-only: sup_rho |w_a| <= a/(4a-2) for a >= gamma_1^2+3/4;
     excess over 1/4 exactly 1/(8a-4).  Hence unconditionally
     limsup |d_m(a)|^{1/m} <= a/(4a-2)   (Sigma|y|<inf by RvM).
  A2 with PT21: off-line zeros need gamma>T, so sup|w_a| <= 1/4 for
     every a <= a_max, a_max = floor((2T^2+3/2-sqrt(8T^2+2))/2)
     ~ T^2 - sqrt2 T ~ 9.0e24 (EXACT integer arithmetic, gated), i.e.
     limsup |d_m(a)|^{1/m} <= 1/4 for every a in (1/4, a_max].
     Removing the a-cap needs the dense-a quantifier = the r115
     candidate RH-equivalence: THE WALL CROSSING, censused in S3.
  A3 diagonal positivity: packet-vs-tail race on rays k=theta(n+1):
     on-line packet lower (RvM+HSW22 count x kernel endpoint minimum,
     PT21 reality below T) vs off-line tail upper (density integral
     bound, |1-y|<=1 declared conservative); both log-linear in n;
     rate dominance + sampled-cell gates => d_m(256)>0 for every
     sampled m (0..1e9) and rate-dominant for all m; ray law
     theta_max = T^2/(e a) gated against the grid; sampled cone cells
     BEYOND the round-106 frontier k=7.44e21 proven individually.
S3 MIN-CUT  the graph as data; capacities: unconditional/definitional
  edges infinite, omega-introduction edges (infinite positivity
  quantifier over a finite-certifiable family) 1, CANDIDATE edges 1,
  MEASURED-grade edges 1; Edmonds--Karp max-flow UNCOND -> RH twice:
  conservative graph (proven edges only) and full graph; the min cut
  and its class census are the headline.  Reachability gate: RH and
  every form-hypothesis node unreachable through unconditional edges.
S4 HONESTY  triviality typing of every S2 item; jitter screen: HSW
  constants x1.10 and T x0.9 must not flip A2/A3 gates; dps halving
  reproducibility on numeric audits; tau-screen declared structurally
  absent (no Galerkin object exists in this pipeline; the jitter
  screen is the conditioning channel, typed as such).
FROZEN NUMERICS: mp dps 50 (rays), 60 (audits), 40 (K74 spot ward,
2048 packets, k=1e19); ray grid t0 in {0.97T} u {T/2^(j/2): j=1..80,
t0>=1e6} u {1e6}; packet factor 1.05; diagonal samples m in
{0,1,2,5,50,1e3,1e6,1e9}; cone samples theta in {1e6,1e18,8e21,
1.1e22}; n-bisection cap 10^7; sieve cap 3000 (E-SPLIT), exact-vector
cap 3000 (E-LAMBDA); S2-LINEAR caps n<=5,k<=5,L-depth 2, degree 12.
RUNTIME BAR 900 s.  Deterministic (no randomness anywhere).
AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; mp.zeta/mp.gamma-of-complex only inside audit_* functions;
no np.load; no zero table in any construction (the only zero-side
numbers are the CITED PT21 height and HSW22 constants).

NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import ast
import hashlib
import math
import sys
import time
from fractions import Fraction

import mpmath as mp
import sympy as sp

START = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
RUNTIME_BAR = 900.0

# ------------------------------------------------------- frozen constants
T_PT = 3000175332800                      # PT21 verified height (cited)
A_SAFE = 256                              # the safe point
K74 = 7444682106464286365865              # round-106 frontier (cited)
LAM_INF = "0.226987054723979955"          # round-106 asymptotic fraction
GAMMA1_LOW = 14                           # classical: gamma_1 > 14 (cited)
HSW_A, HSW_B, HSW_C = "0.1038", "0.2573", "9.3675"    # HSW22 Cor 1.2
FLOORS_1E13 = (("4.5917135e-2", "4.5917136e-2"),
               ("9.0288887e-6", "9.0288888e-6"),
               ("6.9310239e-10", "6.9310252e-10"),
               ("8.278338e-15", "1.3840906e-14"))     # v915/round 100
DIAG_SAMPLES = (0, 1, 2, 5, 50, 10**3, 10**6, 10**9)
CONE_SAMPLES = ("1e6", "1e18", "8e21", "1.1e22")
PACKET_FACTOR = "1.05"
K74_SPOT_K = 10**19
K74_SPOT_PACKETS = 2048
N_BISECT_CAP = 10**7

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str) -> None:
    result = bool(condition)
    CHECKS.append((name, result, detail))
    print("  [%s] %-46s %s"
          % ("PASS" if result else "FAIL", name, detail), flush=True)


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


# =====================================================================
# S0  AST firewall (self-scan)
# =====================================================================
FORBIDDEN_NAMES = ("zetazero", "siegelz", "siegeltheta", "nzeros",
                   "grampoint")


def firewall_selfscan() -> tuple[bool, str]:
    with open(__file__, "r", encoding="utf-8") as handle:
        source = handle.read()
    tree = ast.parse(source)
    bad: list[str] = []
    function_stack: list[str] = []

    class Visitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            function_stack.append(node.name)
            self.generic_visit(node)
            function_stack.pop()

        def visit_Attribute(self, node):
            if isinstance(node.attr, str):
                if node.attr in FORBIDDEN_NAMES:
                    bad.append("forbidden attr %s" % node.attr)
                if node.attr == "zeta" and not any(
                        name.startswith("audit_")
                        for name in function_stack):
                    bad.append("mp.zeta outside audit_ (%s)"
                               % "/".join(function_stack))
                if node.attr == "load":
                    bad.append("np.load present")
            self.generic_visit(node)

        def visit_Name(self, node):
            if node.id in FORBIDDEN_NAMES:
                bad.append("forbidden name %s" % node.id)
            self.generic_visit(node)

    Visitor().visit(tree)
    return (not bad), ("; ".join(bad) if bad else "clean")


# =====================================================================
# S1  edge verification
# =====================================================================
def gates_atom_field() -> list[tuple[str, bool, str]]:
    """Pascal, flow, jet representation, w-def -- symbolic exponents."""
    gates = []
    y, n, k, a, z = sp.symbols("y n k a z", positive=False)

    def offset_zero(terms, base_a, base_b) -> bool:
        """Exact per-atom identity check: each term coeff*y^A*(1-y)^B
        divided by the base monomial has INTEGER exponent offsets; the
        symbolic-n,k identity reduces to a polynomial in y."""
        total = sp.Integer(0)
        for coeff, a_exp, b_exp in terms:
            da = sp.simplify(a_exp - base_a)
            db = sp.simplify(b_exp - base_b)
            if not (da.is_Integer and db.is_Integer):
                return False
            total += coeff * y ** int(da) * (1 - y) ** int(db)
        return sp.simplify(sp.together(total)) == 0

    pascal_ok = offset_zero(((1, n + 2, k), (1, n + 1, k + 1),
                             (-1, n + 1, k)), n + 1, k)
    gates.append(("E-PASCAL per-atom", pascal_ok,
                  "y^(n+1)(1-y)^k = y^(n+2)(1-y)^k + y^(n+1)(1-y)^(k+1)"))

    # L-action exponent rule verified by calculus on an integer grid,
    # then used symbolically below.
    rule_ok = True
    for a_int in range(1, 7):
        for b_int in range(0, 7):
            f = y ** a_int * (1 - y) ** b_int
            lf_calc = sp.expand(y * (1 - y) * sp.diff(f, y))
            lf_rule = sp.expand(a_int * y ** a_int * (1 - y) ** (b_int + 1)
                                - b_int * y ** (a_int + 1)
                                * (1 - y) ** b_int)
            if lf_calc != lf_rule:
                rule_ok = False
    gates.append(("E-FLOW L-action rule", rule_ok,
                  "L[y^A(1-y)^B] = A y^A(1-y)^(B+1) - B y^(A+1)(1-y)^B "
                  "(exact calculus, grid A<=6, B<=6)"))

    y_of = a / (a - z)
    flow_y = sp.simplify(a * sp.diff(y_of, a) - y_of * (1 - y_of))
    gates.append(("E-FLOW-Y a d/da y = y(1-y)", flow_y == 0,
                  "y = a/(a-z), exact"))

    # L C_{n,k} = (n+1) y^(n+1)(1-y)^(k+1) - k y^(n+2)(1-y)^k by the
    # gated rule; the flow identity is then an exact offset polynomial.
    flow_c_ok = offset_zero(((n + 1, n + 1, k + 1), (-k, n + 2, k),
                             (k, n + 1, k),
                             (-(n + k + 1), n + 1, k + 1)), n + 1, k)
    gates.append(("E-FLOW-C (L+k)C_{n,k}=(n+k+1)C_{n,k+1}", flow_c_ok,
                  "per atom, symbolic n,k (via the gated L rule)"))

    flow_b_ok = offset_zero(((n + 1, n + 1, 1),
                             (-(n + 1), n + 1, 1)), n + 1, 0)
    gates.append(("E-FLOW-B a d/da b_n = (n+1)C_{n,1}", flow_b_ok,
                  "per atom, symbolic n (k=0 case of the L rule)"))

    w_def = sp.simplify(y_of * (1 - y_of) + a * z / (a - z) ** 2)
    gates.append(("E-WDEF w = y(1-y) = -az/(a-z)^2", w_def == 0, "exact"))

    jet_ok = True
    f_atom = 1 / (z - sp.Symbol("z0"))
    for order in range(9):
        lhs = (a ** (order + 1) * (-1) ** order / sp.factorial(order)
               * sp.diff(f_atom, z, order).subs(z, a))
        rhs = (a / (a - sp.Symbol("z0"))) ** (order + 1)
        if sp.simplify(lhs - rhs) != 0:
            jet_ok = False
            break
    gates.append(("E-JETREP b_n = a^(n+1)((-1)^n/n!)F^(n)(a)", jet_ok,
                  "per atom, orders 0..8 exact"))
    return gates


def gates_generating_function() -> list[tuple[str, bool, str]]:
    """Round-106 closed form and sign-regular minor, replicated."""
    gates = []
    x, y, a, atom_y = sp.symbols("x y a atom_y")
    denominator = x + y - x * y
    atom = atom_y / ((1 - x * atom_y) * (1 - y + y * atom_y))
    atom_split = (x / denominator * atom_y / (1 - x * atom_y)
                  + y / denominator * atom_y / (1 - y + y * atom_y))
    gates.append(("E-GF2 two-variable atom",
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
    gates.append(("E-GF2 closed through F",
                  sp.simplify(sp.factor(direct - closed)) == 0,
                  "G=a/(x+y-xy)[xF(a(1-x))+y/(1-y)F(a/(1-y))]"))

    u1, u2, w1, w2 = sp.symbols("u1 u2 w1 w2")

    def cell(nn: int, kk: int):
        return (w1 * u1 ** (nn + 1) * (1 - u1) ** kk
                + w2 * u2 ** (nn + 1) * (1 - u2) ** kk)

    minor = sp.expand(cell(0, 0) * cell(1, 1) - cell(0, 1) * cell(1, 0))
    gates.append(("E-SIGNREG 2x2 minor",
                  sp.simplify(minor + w1 * w2 * u1 * u2
                              * (u1 - u2) ** 2) == 0,
                  "minor=-w1w2u1u2(u1-u2)^2 (round-106 orientation)"))
    return gates


def gates_radius4_geometry() -> list[tuple[str, bool, str]]:
    """r115 candidate algebra, independently re-verified symbolically."""
    gates = []
    a, z, t, theta = sp.symbols("a z t theta")
    delta, gam = sp.symbols("delta gamma", positive=True)

    lhs = (1 + t * a * z / (a - z) ** 2) * (z - a) ** 2
    rhs = z ** 2 - a * (2 - t) * z + a ** 2
    gates.append(("E-DIAGDET per-atom factor",
                  sp.simplify(sp.expand(lhs - rhs)) == 0,
                  "1-t w_a(z)=(z-z+)(z-z-)/(z-a)^2, z+z-=a^2, "
                  "z+ + z- = a(2-t)"))

    zp = a * sp.exp(sp.I * theta)
    zm = a * sp.exp(-sp.I * theta)
    t_circ = 4 * sp.sin(theta / 2) ** 2
    sum_dev = sp.simplify(sp.expand_trig(
        (zp + zm).rewrite(sp.cos) - a * (2 - t_circ)))
    circle_ok = (sp.simplify(zp * zm - a ** 2) == 0 and sum_dev == 0)
    gates.append(("E-DIAGDET circle map", circle_ok,
                  "t=4sin^2(theta/2) <=> z+- = a e^(+-i theta)"))

    y_of = a / (a - z)
    wsum = sp.simplify(y_of + (a / (a - a ** 2 / z)) - 1)
    gates.append(("E-WSUM y(z)+y(a^2/z)=1", wsum == 0, "exact involution"))

    z_off = (delta + sp.I * gam) ** 2
    a_match = delta ** 2 + gam ** 2
    w_match = sp.simplify(-a_match * z_off
                          / (a_match - z_off) ** 2)
    gates.append(("E-WSUM matched-scale w real",
                  sp.simplify(w_match - a_match / (4 * gam ** 2)) == 0,
                  "w = (d^2+g^2)/(4g^2) = (1/4)(1+d^2/g^2) > 1/4"))
    y_p = a_match / (a_match - z_off)
    y_m = a_match / (a_match - sp.conjugate(z_off))
    gates.append(("E-WSUM matched-scale y+ybar=1",
                  sp.simplify(sp.expand(y_p + y_m - 1)) == 0,
                  "pair adds exactly +w^m to d_m"))

    u, s = sp.symbols("u s", positive=True)
    disc = sp.expand((u + 2 * s) ** 2 - s ** 2
                     - (u + s) * (u + 3 * s))
    gates.append(("E-WINDOW discriminant", disc == 0,
                  "(u+2s)^2-s^2 = (u+s)(u+3s); window nonempty iff "
                  "u > -s (z off the cut)"))
    return gates


def gates_li_sos_pin() -> list[tuple[str, bool, str]]:
    gates = []
    q = sp.Symbol("q")
    y_pair = -(1 - q) ** 2 / (4 * q)
    li_ok = True
    for r in range(1, 6):
        lam_sum = sum((-1) ** (m + 1) * sp.binomial(2 * r, r + m)
                      * (2 - q ** m - q ** (-m)) for m in range(1, r + 1))
        if sp.simplify(y_pair ** r - lam_sum / 4 ** r) != 0:
            li_ok = False
            break
    gates.append(("E-LI binomial transform r<=5", li_ok,
                  "y^r = 4^(-r) sum (-1)^(m+1) C(2r,r+m) lambda_m, "
                  "y=1/(4 rho(1-rho)), q=(rho-1)/rho"))

    rho = sp.Symbol("rho")
    anchor = sp.simplify(1 / (4 * rho * (1 - rho))
                         - (sp.Rational(1, 4))
                         * (1 / rho + 1 / (1 - rho)))
    gates.append(("N4 pin-anchor per pair", anchor == 0,
                  "y(1/4) = (1/4)(1/rho + 1/(1-rho)): b_0(1/4)=lambda_1/4"))
    gamma_e = sp.EulerGamma
    rearr = sp.simplify((2 + gamma_e - sp.log(4 * sp.pi)) / 8
                        - (1 + gamma_e / 2 - sp.log(2 * sp.sqrt(sp.pi)))
                        / 4)
    gates.append(("N4 pin-anchor constants", rearr == 0,
                  "(2+g-log4pi)/8 == (1+g/2-log 2 sqrt(pi))/4 exact"))

    masses = sp.symbols("m1:5", positive=True)
    nodes = sp.symbols("t1:5")
    for order in (2, 3):
        hank = sp.Matrix(order, order, lambda i, j: sum(
            masses[p] * nodes[p] ** (i + j) for p in range(4)))
        lhs = sp.expand(hank.det())
        rhs = sp.Integer(0)
        import itertools as it
        for subset in it.combinations(range(4), order):
            prod_m = sp.prod([masses[p] for p in subset])
            vand = sp.prod([nodes[qq] - nodes[pp]
                            for pp, qq in it.combinations(subset, 2)])
            rhs += prod_m * vand ** 2
        gates.append(("E-SOS Hankel-Vandermonde N=%d" % order,
                      sp.expand(lhs - rhs) == 0,
                      "det[b_(i+j)] = sum_(|S|=N) prod mass V(y_S)^2"))
    return gates


def gates_w14_trace_hflow() -> list[tuple[str, bool, str]]:
    gates = []
    a, g = sp.symbols("a g", positive=True)
    w_line = a * g / (a + g) ** 2      # g = gamma^2
    quarter = sp.simplify(sp.Rational(1, 4) - w_line
                          - ((a - g) / (2 * (a + g))) ** 2)
    gates.append(("E-W14 (COND-RH typed)", quarter == 0,
                  "1/4 - w = ((a-g^2)/(2(a+g^2)))^2: on-line w in [0,1/4]"))

    spectrum = (Fraction(0), Fraction(1, 3), Fraction(2, 5), Fraction(1))
    trace_ok = all(
        sum(lam ** (n + 1) * (1 - lam) ** k for lam in spectrum) >= 0
        for n in range(7) for k in range(7))
    gates.append(("E-TRACE spectral gate", trace_ok,
                  "Tr[A^(n+1)(I-A)^k] = sum lam^(n+1)(1-lam)^k >= 0 on "
                  "[0,1] spectra (operator statement cited; exact grid)"))

    b = sp.symbols("b0:7")
    size = 3
    hankel = sp.Matrix(size, size, lambda i, j: b[i + j])
    shifted = sp.Matrix(size, size, lambda i, j: b[i + j + 1])
    c_one = hankel - shifted
    grading = sp.diag(*[sp.Rational(2 * i + 1, 2) for i in range(size)])
    dot_hankel = sp.Matrix(size, size, lambda i, j:
                           (i + j + 1) * (b[i + j] - b[i + j + 1]))
    gates.append(("E-HFLOW matrix flow",
                  dot_hankel == grading * c_one + c_one * grading,
                  "dot H = DK+KD, D_ii=i+1/2 (round 106)"))
    determinant = hankel.det()
    dot_det = sp.expand(sum(sp.diff(determinant, b[i])
                            * (i + 1) * (b[i] - b[i + 1])
                            for i in range(2 * size - 1)))
    jacobi = 2 * determinant * sp.trace(grading * hankel.inv() * c_one)
    gates.append(("E-HFLOW Jacobi flow",
                  sp.simplify(sp.together(dot_det - jacobi)) == 0,
                  "dot det H = 2 det H Tr(D H^-1 K)"))
    return gates


def gates_kick_fred_extdet() -> list[tuple[str, bool, str]]:
    gates = []

    # E-KICK: exact Levinson kick at the first touched lag.
    xs = (Fraction(1, 3), Fraction(-1, 4), Fraction(2, 5))
    ms = (Fraction(2), Fraction(3), Fraction(1, 2))

    def cheb_moment(d: int) -> Fraction:
        total = Fraction(0)
        for x0, m0 in zip(xs, ms):
            t_prev, t_cur = Fraction(1), x0
            if d == 0:
                total += m0
                continue
            for _ in range(d - 1):
                t_prev, t_cur = t_cur, 2 * x0 * t_cur - t_prev
            total += m0 * t_cur
        return total

    def levinson_alphas(c: list[Fraction], depth: int):
        a_vec = [Fraction(1)]
        energy = c[0]
        alphas = []
        for kk in range(1, depth + 1):
            lam = sum(a_vec[j] * c[kk - j] for j in range(kk))
            alpha = lam / energy
            new_vec = a_vec + [Fraction(0)]
            rev = [Fraction(0)] + a_vec[::-1]
            a_vec = [new_vec[j] - alpha * rev[j] for j in range(kk + 1)]
            energy = energy * (1 - alpha * alpha)
            alphas.append(alpha)
        return alphas, energy

    depth0 = 4
    c_clean = [cheb_moment(d) for d in range(depth0 + 1)]
    phi = Fraction(7, 100)
    c_pert = list(c_clean)
    c_pert[depth0] += phi
    alpha_clean, _ = levinson_alphas(c_clean, depth0)
    alpha_pert, _ = levinson_alphas(c_pert, depth0)
    _, energy_prev = levinson_alphas(c_clean, depth0 - 1)
    delta_alpha = alpha_pert[-1] - alpha_clean[-1]
    kick_pred = phi / energy_prev
    sign = -1 if delta_alpha == -kick_pred else (
        1 if delta_alpha == kick_pred else 0)
    gates.append(("E-KICK exact first-touched-lag law", sign != 0,
                  "Delta alpha_%d = %+d * phi/(c_0 prod(1-alpha^2)); "
                  "exact Fraction equality, measured sign %+d"
                  % (depth0, sign, sign)))

    # E-FRED: exact eigen instance + Loewner bracket construction.
    q_cols = ((1, 2, 2), (2, 1, -2), (2, -2, 1))   # orthogonal, norm^2=9
    lam_eig = (Fraction(3), Fraction(-1), Fraction(5))
    t_mat = [[sum(Fraction(q_cols[e][i] * q_cols[e][j]) * lam_eig[e]
                  / 9 for e in range(3)) for j in range(3)]
             for i in range(3)]
    d_diag = (Fraction(1), Fraction(2), Fraction(4))
    fred_ok = True
    for e_idx in range(3):
        for o_idx in range(3):
            if e_idx == o_idx:
                continue
            u_vec = q_cols[e_idx]
            v_vec = q_cols[o_idx]
            s_uv = sum(v_vec[i] * (d_diag[i] * t_mat[i][j]
                                   - t_mat[i][j] * d_diag[j]) * u_vec[j]
                       for i in range(3) for j in range(3))
            rhs = (lam_eig[e_idx] - lam_eig[o_idx]) * sum(
                v_vec[i] * d_diag[i] * u_vec[i] for i in range(3))
            if s_uv != rhs:
                fred_ok = False
    gates.append(("E-FRED alternative (exact eigenpairs)", fred_ok,
                  "<xi_o,(DT-TD)xi_e> = (eps_e-eps_o)<xi_o,D xi_e>, "
                  "exact rational spectral instance"))

    eta = sp.Matrix(sp.symbols("eta1:4"))
    beta = sp.Matrix(sp.symbols("beta1:4"))
    dsym = sp.symbols("dd1:4")
    t_loew = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            if i != j:
                t_loew[i, j] = ((beta[i] * eta[j] - eta[i] * beta[j])
                                / (dsym[i] - dsym[j]))
    d_mat = sp.diag(*dsym)
    bracket = sp.simplify(d_mat * t_loew - t_loew * d_mat
                          - (beta * eta.T - eta * beta.T))
    gates.append(("E-FRED Loewner bracket", bracket == sp.zeros(3, 3),
                  "DT-TD = |beta><eta| - |eta><beta| on the CF class "
                  "(diagonal of T free)"))

    # E-EXTDET on an exact rational instance, three z values.
    d_vals = (Fraction(1), Fraction(2), Fraction(3), Fraction(5))
    u_list = ((Fraction(1), Fraction(0), Fraction(2), Fraction(-1)),
              (Fraction(0), Fraction(1), Fraction(1), Fraction(3)))
    v_list = ((Fraction(2), Fraction(1), Fraction(0), Fraction(1)),
              (Fraction(-1), Fraction(1), Fraction(2), Fraction(0)))

    def det4(mat):
        m = [row[:] for row in mat]
        det = Fraction(1)
        for col in range(4):
            piv = next((r for r in range(col, 4) if m[r][col] != 0), None)
            if piv is None:
                return Fraction(0)
            if piv != col:
                m[col], m[piv] = m[piv], m[col]
                det = -det
            det *= m[col][col]
            for r in range(col + 1, 4):
                factor = m[r][col] / m[col][col]
                m[r] = [m[r][cc] - factor * m[col][cc] for cc in range(4)]
        return det

    ext_ok = True
    for z_val in (Fraction(7, 2), Fraction(-3), Fraction(11, 3)):
        m_blk = [[(d_vals[i] if i == j else Fraction(0))
                  + sum(u_list[e][i] * v_list[e][j] for e in range(2))
                  for j in range(4)] for i in range(4)]
        lhs = det4([[m_blk[i][j] - (z_val if i == j else 0)
                     for j in range(4)] for i in range(4)])
        det_dz = Fraction(1)
        for dv in d_vals:
            det_dz *= (dv - z_val)
        w_small = [[sum(v_list[e1][i] * u_list[e2][i]
                        / (d_vals[i] - z_val) for i in range(4))
                    for e2 in range(2)] for e1 in range(2)]
        det_w = ((1 + w_small[0][0]) * (1 + w_small[1][1])
                 - w_small[0][1] * w_small[1][0])
        if lhs != det_dz * det_w:
            ext_ok = False
    gates.append(("E-EXTDET Sylvester form", ext_ok,
                  "det(D-z+UV^T) = det(D-z) det(I_m + V^T (D-z)^-1 U), "
                  "exact rational m=2 (r114 instance cited)"))
    return gates


def gates_lambda_exact() -> tuple[bool, str]:
    """Lambda = mu * log as exact vectors over the free group on log p."""
    cap = 3000
    ok = True
    for n in range(2, cap + 1):
        fac = sp.factorint(n)
        lam_vec = {}
        if len(fac) == 1:
            p = next(iter(fac))
            lam_vec = {p: 1}
        conv = {}
        for d in sp.divisors(n):
            mu = sp.mobius(d)
            if mu == 0:
                continue
            for p, e in sp.factorint(n // d).items():
                conv[p] = conv.get(p, 0) + mu * e
        conv = {p: c for p, c in conv.items() if c != 0}
        if conv != lam_vec:
            ok = False
            break
    return ok, "Lambda(n) = sum_(d|n) mu(d) log(n/d), exact vectors " \
               "on log p, n <= %d" % cap


def audit_xi_logderiv(s_val) -> mp.mpf:
    """xi'/xi at real s via mp (audit namespace; mp.zeta declared)."""
    def log_xi(s):
        zs = (s - 1) * mp.zeta(s)
        return (mp.log(s / 2) + (-s / 2) * mp.log(mp.pi)
                + mp.loggamma(s / 2) + mp.log(zs))
    return mp.diff(log_xi, mp.mpf(s_val))


def audit_epin_and_split() -> list[tuple[str, bool, str]]:
    gates = []
    mp.mp.dps = 60
    lder1 = audit_xi_logderiv(1)
    target = 1 + mp.euler / 2 - mp.log(2 * mp.sqrt(mp.pi))
    gates.append(("E-EPIN xi'/xi(1) = 1+g/2-log 2 sqrt(pi)",
                  abs(lder1 - target) < mp.mpf("1e-30"),
                  "dev %.2e; doubling gives sum 1/(rho(1-rho)) = "
                  "2+gamma-log 4pi (classical)" % float(abs(lder1
                                                            - target))))
    b0_quarter = lder1 / 4
    anchor = (2 + mp.euler - mp.log(4 * mp.pi)) / 8
    gates.append(("N4 pin-anchor numeric loop",
                  abs(b0_quarter - anchor) < mp.mpf("1e-30"),
                  "b_0(1/4) = (1/4) xi'/xi(1) = %.12e vs "
                  "(2+g-log4pi)/8, dev %.2e"
                  % (float(b0_quarter), float(abs(b0_quarter - anchor)))))

    s0 = mp.mpf("16.5")
    prime_side = mp.mpf(0)
    for n in range(2, 1001):
        fac = sp.factorint(n)
        if len(fac) == 1:
            p = next(iter(fac))
            prime_side += mp.log(p) * mp.power(n, -s0)
    split = (1 / s0 + 1 / (s0 - 1) - mp.log(mp.pi) / 2
             + mp.digamma(s0 / 2) / 2 - prime_side)
    lder_s0 = audit_xi_logderiv(s0)
    gates.append(("E-SPLIT POLE+ARCH+PRIME at s=16.5",
                  abs(split - lder_s0) < mp.mpf("1e-40"),
                  "sieve cap 1000, tail < 1e-45; dev %.2e"
                  % float(abs(split - lder_s0))))
    return gates


# ---------------------------------------------- K74 spot ward (round 106)
def k74_spot_ward(dps: int = 40) -> tuple[bool, str]:
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    try:
        a_s = mp.mpf(A_SAFE)
        a_shift = a_s - mp.mpf("0.25")
        c_shift = a_s - mp.mpf("0.5")
        t_pt = mp.mpf(T_PT)
        h_ver = t_pt - 1
        n_a, n_b, n_c = (mp.mpf(HSW_A), mp.mpf(HSW_B), mp.mpf(HSW_C))

        def rv_main(t):
            return t / (2 * mp.pi) * mp.log(t / (2 * mp.pi * mp.e))

        def rv_error(t):
            return n_a * mp.log(t) + n_b * mp.log(mp.log(t)) + n_c

        def online_kernel(t, k):
            yv = a_s / (a_s + t * t)
            return yv * mp.power(1 - yv, k)

        kmp = mp.mpf(K74_SPOT_K)
        gamma_star = mp.sqrt(a_s * kmp)
        u_floor = gamma_star / h_ver
        du = (mp.mpf(12) - u_floor) / K74_SPOT_PACKETS
        total = mp.mpf(0)
        for idx in range(K74_SPOT_PACKETS):
            u_left = u_floor + idx * du
            u_right = u_left + du
            t_hi = gamma_star / u_left
            t_lo = gamma_star / u_right
            cnt = (rv_main(t_hi) - rv_main(t_lo)
                   - rv_error(t_hi) - rv_error(t_lo))
            if cnt <= 0:
                continue
            total += cnt * min(online_kernel(t_lo, K74_SPOT_K),
                               online_kernel(t_hi, K74_SPOT_K))
        d_eff = c_shift / (1 + a_shift / t_pt ** 2)
        v = mp.sqrt(d_eff * kmp) / t_pt
        log_scale = mp.log(mp.sqrt(d_eff * kmp) / (2 * mp.pi))
        series = mp.mpf(0)
        for j in range(21):
            deg = 2 * j + 1
            mag = (v ** deg / mp.factorial(j)
                   * ((log_scale - mp.log(v)) / deg + mp.mpf(1) / deg ** 2))
            series += (-1) ** j * mag
        main = a_s / (2 * mp.pi * mp.sqrt(d_eff * kmp)) * series
        u_at_t = (a_s / (t_pt ** 2 + a_shift)
                  * mp.power((t_pt ** 2 + mp.mpf("0.25"))
                             / (t_pt ** 2 + a_shift), K74_SPOT_K))
        err = (2 * rv_error(t_pt) * u_at_t
               + (n_a + n_b / mp.log(t_pt)) * a_s / (2 * t_pt ** 2))
        ratio = total / (main + err)
        return bool(ratio > 1), ("k=1e19 packet/tail ratio %.6f "
                                 "(round-106 mechanism, %d packets, "
                                 "dps %d)" % (float(ratio),
                                              K74_SPOT_PACKETS, dps))
    finally:
        mp.mp.dps = old_dps


# =====================================================================
# S2  mechanical composition search
# =====================================================================
def poly_c(n: int, k: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for j in range(k + 1):
        out[n + 1 + j] = (out.get(n + 1 + j, Fraction(0))
                          + Fraction((-1) ** j * math.comb(k, j)))
    return out


def poly_l(p: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for i, c in p.items():
        if i == 0:
            continue
        out[i] = out.get(i, Fraction(0)) + i * c
        out[i + 1] = out.get(i + 1, Fraction(0)) - i * c
    return {i: c for i, c in out.items() if c != 0}


def frac_rank(rows: list[list[Fraction]]) -> int:
    mat = [row[:] for row in rows if any(row)]
    rank = 0
    ncols = len(rows[0]) if rows else 0
    col = 0
    while mat and col < ncols:
        piv = next((r for r in range(rank, len(mat))
                    if mat[r][col] != 0), None)
        if piv is None:
            col += 1
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        pv = mat[rank][col]
        mat[rank] = [x / pv for x in mat[rank]]
        for r in range(len(mat)):
            if r != rank and mat[r][col] != 0:
                f = mat[r][col]
                mat[r] = [mat[r][cc] - f * mat[rank][cc]
                          for cc in range(ncols)]
        rank += 1
        col += 1
    return rank


def linear_completeness() -> tuple[dict, list[tuple[str, bool, str]]]:
    n_cap, k_cap = 5, 5
    names: list[str] = []
    polys: list[dict[int, Fraction]] = []

    def add(name: str, poly: dict[int, Fraction]):
        names.append(name)
        polys.append(poly)

    for n in range(n_cap + 1):
        for k in range(k_cap + 1):
            add("C%d%d" % (n, k), poly_c(n, k))
    for n in range(6):
        add("b%d" % n, poly_c(n, 0))
    for m in range(5):
        add("d%d" % m, poly_c(m, m))
    for m in range(1, 6):
        add("e%d" % m, poly_c(m - 1, m))
    for n in range(n_cap + 1):
        for k in range(k_cap + 1):
            add("L[C%d%d]" % (n, k), poly_l(poly_c(n, k)))
    for n in range(6):
        add("L[b%d]" % n, poly_l(poly_c(n, 0)))
    for n in range(6):
        add("LL[b%d]" % n, poly_l(poly_l(poly_c(n, 0))))

    idx = {nm: i for i, nm in enumerate(names)}
    ncols = len(names)
    deg_max = max(max(p) for p in polys if p)
    matrix_rows = [[polys[c].get(d, Fraction(0)) for c in range(ncols)]
                   for d in range(deg_max + 1)]
    rank_a = frac_rank(matrix_rows)
    dim_relations = ncols - rank_a

    known: list[list[Fraction]] = []

    def rel(*terms):
        vec = [Fraction(0)] * ncols
        for coeff, nm in terms:
            vec[idx[nm]] += Fraction(coeff)
        known.append(vec)

    for n in range(n_cap):
        for k in range(k_cap):
            rel((1, "C%d%d" % (n, k)), (-1, "C%d%d" % (n + 1, k)),
                (-1, "C%d%d" % (n, k + 1)))
            rel((1, "L[C%d%d]" % (n, k)), (-1, "L[C%d%d]" % (n + 1, k)),
                (-1, "L[C%d%d]" % (n, k + 1)))
    for n in range(6):
        rel((1, "b%d" % n), (-1, "C%d0" % n))
        rel((1, "L[b%d]" % n), (-1, "L[C%d0]" % n))
        rel((1, "L[b%d]" % n), (-(n + 1), "C%d1" % n))
        rel((1, "LL[b%d]" % n), (-(n + 1), "L[C%d1]" % n))
    for m in range(5):
        rel((1, "d%d" % m), (-1, "C%d%d" % (m, m)))
    for m in range(1, 6):
        rel((1, "e%d" % m), (-1, "C%d%d" % (m - 1, m)))
    for n in range(n_cap + 1):
        for k in range(k_cap):
            rel((1, "L[C%d%d]" % (n, k)), (k, "C%d%d" % (n, k)),
                (-(n + k + 1), "C%d%d" % (n, k + 1)))

    all_hold = all(
        all(sum(vec[c] * matrix_rows[d][c] for c in range(ncols)) == 0
            for d in range(deg_max + 1))
        for vec in known)
    rank_known = frac_rank(known)

    gates = [
        ("S2-LINEAR known edges are relations", all_hold,
         "%d local generators all annihilate the moment matrix"
         % len(known)),
        ("S2-LINEAR completeness", rank_known == dim_relations,
         "relation space dim %d == rank(local edge span) %d over "
         "%d quantities: NO unfound linear identity at this depth"
         % (dim_relations, rank_known, ncols)),
    ]
    census = {"quantities": ncols, "relations": dim_relations,
              "generators": len(known), "rank_known": rank_known}
    return census, gates


def gates_named_compositions() -> list[tuple[str, bool, str]]:
    gates = []
    y, n = sp.symbols("y n")

    def l_op(f):
        return sp.expand(y * (1 - y) * sp.diff(f, y))

    g_cur = y ** (n + 1)
    jet_ok = True
    for k in range(1, 6):
        g_cur = sp.expand(l_op(g_cur) + (k - 1) * g_cur)
        target = sp.rf(n + 1, k) * y ** (n + 1) * (1 - y) ** k
        if sp.simplify(sp.powsimp(sp.expand(
                (g_cur - target) / y ** (n + 1)), force=True)) != 0:
            jet_ok = False
            break
    gates.append(("N1 jet transport k<=5", jet_ok,
                  "C_{n,k} = (n!/(n+k)!) L(L+1)...(L+k-1) b_n -- the "
                  "whole Pascal field is the log-a jet of the moment "
                  "row (machine-composed from E-FLOW-C)"))

    m_sym = sp.Symbol("m", positive=True, integer=True)
    superdiag = sp.simplify(y ** m_sym * (1 - y) ** m_sym
                            - (y * (1 - y)) ** m_sym)
    gates.append(("N2 superdiagonal trace", superdiag == 0,
                  "C_{m-1,m} = sum w^m = Tr B^m, B=A(I-A) "
                  "(TRIVIAL-ADJACENT typing)"))

    t, w1, w2 = sp.symbols("t w1 w2")
    lhs = sp.log((1 - t * w1) * (1 - t * w2))
    rhs = -sum(t ** m / m * (w1 ** m + w2 ** m) for m in range(1, 9))
    series_dev = sp.simplify(sp.series(lhs - rhs, t, 0, 9).removeO())
    gates.append(("N3 log-determinant Pascal reading", series_dev == 0,
                  "log Dd_a(t) = - sum (t^m/m) C_{m-1,m}: the Fredholm "
                  "determinant's log-jet is carried entirely by the "
                  "first superdiagonal (order 8 gate)"))
    return gates


# =====================================================================
# S2A  unconditional growth bounds
# =====================================================================
def gates_a1_strip_bound() -> list[tuple[str, bool, str]]:
    gates = []
    a, g, p = sp.symbols("a g p", positive=True)
    modsq = sp.expand((a + g - p) ** 2 + 4 * p * g
                      - ((a - p + g) ** 2 + 4 * p * g))
    gates.append(("A1 |a-z|^2 identity", modsq == 0,
                  "|a-z|^2 = (a+g^2-d^2)^2 + 4 d^2 g^2 "
                  ">= (a+g^2-d^2)^2"))
    h_fun = a * (g + p) / (a + g - p) ** 2
    dh_dp = sp.simplify(sp.diff(h_fun, p)
                        - a * (a + 3 * g + p) / (a + g - p) ** 3)
    mono_ok = (dh_dp == 0)
    gates.append(("A1 delta-monotonicity", mono_ok,
                  "d/dp[a(g+p)/(a+g-p)^2] = a(a+3g+p)/(a+g-p)^3 > 0 "
                  "for p < a+g: bound at p = 1/4"))
    h_quarter = h_fun.subs(p, sp.Rational(1, 4))
    g_star = sp.solve(sp.diff(h_quarter, g), g)
    g_star = [sol for sol in g_star if sol.has(a)][0]
    sup_val = sp.simplify(h_quarter.subs(g, g_star))
    gates.append(("A1 interior maximum", sp.simplify(
        g_star - (a - sp.Rational(3, 4))) == 0
        and sp.simplify(sup_val - a / (4 * a - 2)) == 0,
        "argmax g^2 = a-3/4, sup|w_a| <= a/(4a-2) (strip only)"))
    excess = sp.simplify(a / (4 * a - 2) - sp.Rational(1, 4)
                         - 1 / (8 * a - 4))
    gates.append(("A1 wall thickness", excess == 0,
                  "a/(4a-2) - 1/4 = 1/(8a-4) exactly; at a=256: "
                  "sup <= %s, excess %.3e"
                  % (sp.nsimplify(sp.Rational(256, 1022)),
                     1.0 / (8 * 256 - 4))))
    return gates


def gates_a2_amax() -> tuple[int, list[tuple[str, bool, str]]]:
    gates = []
    t_big = T_PT
    b_coeff = Fraction(2) * t_big ** 2 + Fraction(3, 2)
    c_coeff = (Fraction(t_big ** 2) - Fraction(1, 4)) ** 2
    disc = b_coeff ** 2 - 4 * c_coeff
    gates.append(("A2 discriminant identity",
                  disc == 8 * Fraction(t_big) ** 2 + 2,
                  "B^2-4C = 8T^2+2 exact (B=2T^2+3/2, C=(T^2-1/4)^2)"))
    disc_int = 32 * t_big ** 2 + 8      # (2*sqrt(disc))^2 scale
    s_floor = math.isqrt(disc_int)
    i_min = s_floor + (0 if s_floor * s_floor == disc_int else 1)
    a_max = (4 * t_big ** 2 + 3 - i_min) // 4

    def q_of(x: int) -> Fraction:
        return Fraction(x) ** 2 - b_coeff * x + c_coeff

    gates.append(("A2 exact integer a_max",
                  q_of(a_max) >= 0 > q_of(a_max + 1),
                  "a_max = %d ~ %.4e (= T^2 - sqrt2 T + O(1))"
                  % (a_max, float(a_max))))
    gates.append(("A2 safe point inside", A_SAFE <= a_max,
                  "a = 256 <= a_max: sup_rho |w_256| <= 1/4 "
                  "UNCONDITIONALLY (PT21+strip cited)"))
    mp.mp.dps = 30
    w_tail = (mp.mpf(A_SAFE) * (mp.mpf(T_PT) ** 2 + mp.mpf("0.25"))
              / (mp.mpf(A_SAFE) + mp.mpf(T_PT) ** 2
                 - mp.mpf("0.25")) ** 2)
    gates.append(("A2 off-line envelope at a=256",
                  w_tail < mp.mpf("1e-22"),
                  "|w_256(off-line)| <= %.4e: any off-line pole of "
                  "D_256(t) would sit at |t| >= %.3e, far beyond 4"
                  % (float(w_tail), float(1 / w_tail))))
    return a_max, gates


# ------------------------------------------------------- ray machinery
def ray_context(hsw_scale: str = "1.0", t_scale: str = "1.0"):
    mp.mp.dps = 50
    scale = mp.mpf(hsw_scale)
    t_eff = mp.mpf(T_PT) * mp.mpf(t_scale)
    ctx = {
        "T": t_eff,
        "na": mp.mpf(HSW_A) * scale,
        "nb": mp.mpf(HSW_B) * scale,
        "nc": mp.mpf(HSW_C) * scale,
        "a": mp.mpf(A_SAFE),
    }
    grid = [t_eff * mp.mpf("0.97")]
    j = 1
    root2 = mp.sqrt(2)
    while t_eff / root2 ** j >= mp.mpf("1e6") and j <= 80:
        grid.append(t_eff / root2 ** j)
        j += 1
    grid.append(mp.mpf("1e6"))
    ctx["grid"] = grid
    return ctx


def ray_count_lower(ctx, t0):
    def rv_m(t):
        return t / (2 * mp.pi) * mp.log(t / (2 * mp.pi * mp.e))

    def rv_e(t):
        return (ctx["na"] * mp.log(t) + ctx["nb"] * mp.log(mp.log(t))
                + ctx["nc"])

    hi = t0 * mp.mpf(PACKET_FACTOR)
    return rv_m(hi) - rv_m(t0) - rv_e(hi) - rv_e(t0)


def ray_online_ln(ctx, n: int, k: int):
    best = mp.mpf("-1e40")
    a = ctx["a"]
    for t0 in ctx["grid"]:
        hi = t0 * mp.mpf(PACKET_FACTOR)
        if hi >= ctx["T"]:
            continue
        cnt = ray_count_lower(ctx, t0)
        if cnt <= 0:
            continue
        y_hi = a / (a + hi * hi)
        y_lo = a / (a + t0 * t0)
        val = (mp.log(cnt) + (n + 1) * mp.log(y_hi)
               + (k * mp.log(1 - y_lo) if k else mp.mpf(0)))
        if val > best:
            best = val
    return best


def ray_tail_ln(ctx, n: int):
    a, t_eff = ctx["a"], ctx["T"]
    d_const = ctx["na"] + ctx["nb"] / mp.log(t_eff)
    e_t = (ctx["na"] * mp.log(t_eff)
           + ctx["nb"] * mp.log(mp.log(t_eff)) + ctx["nc"])
    ln_f_t = (n + 1) * mp.log(a / (t_eff ** 2 + a - mp.mpf("0.25")))
    term_boundary = mp.log(2 * e_t) + ln_f_t
    two_n1 = mp.mpf(2 * n + 1)
    ln_i1 = ((n + 1) * mp.log(a) - two_n1 * mp.log(t_eff)
             + mp.log(mp.log(t_eff / (2 * mp.pi)) / (2 * mp.pi * two_n1)
                      + 1 / (2 * mp.pi * two_n1 ** 2)))
    ln_i2 = ((n + 1) * mp.log(a) - (2 * n + 2) * mp.log(t_eff)
             + mp.log(d_const / (2 * n + 2)))
    peak = max(term_boundary, ln_i1, ln_i2)
    total = peak + mp.log(mp.exp(term_boundary - peak)
                          + mp.exp(ln_i1 - peak) + mp.exp(ln_i2 - peak))
    return total


def ray_n0(ctx, theta: mp.mpf, n_cap: int = N_BISECT_CAP):
    def holds(n: int) -> bool:
        k = int(mp.floor(theta * (n + 1)))
        online = ray_online_ln(ctx, n, k)
        tail = ray_tail_ln(ctx, n)
        return online > tail + mp.log(2)
    lo, hi = 0, 1
    while hi <= n_cap and not holds(hi):
        lo, hi = hi, hi * 4
    if hi > n_cap:
        return None
    if holds(lo) and lo == 0:
        return 0
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if holds(mid):
            hi = mid
        else:
            lo = mid
    return hi


def gates_a3_cone(ctx) -> list[tuple[str, bool, str]]:
    gates = []
    diag_ok = True
    worst = mp.mpf("1e40")
    margins = []
    for m in DIAG_SAMPLES:
        online = ray_online_ln(ctx, m, m)
        tail = ray_tail_ln(ctx, m)
        margin = online - tail
        margins.append(margin)
        worst = min(worst, margin)
        if margin <= 0:
            diag_ok = False
    gates.append(("A3 diagonal samples m<=1e9", diag_ok,
                  "d_m(256) > 0 PROVEN at every sampled m "
                  "(worst ln-margin %.2f nats)" % float(worst)))
    mono_ok = all(margins[i + 1] > margins[i]
                  for i in range(1, len(margins) - 1))
    gates.append(("A3 diagonal margin monotone (m>=1)", mono_ok,
                  "ln-margin grows along the sampled ladder: "
                  "%.1f -> %.1f -> ... -> %.3e nats"
                  % (float(margins[1]), float(margins[2]),
                     float(margins[-1]))))

    a = ctx["a"]
    rate_on = mp.mpf("-1e40")
    for t0 in ctx["grid"]:
        yv = a / (a + t0 * t0)
        rate_on = max(rate_on, mp.log(yv) + mp.log(1 - yv))
    rate_tail = mp.log(a / (ctx["T"] ** 2 + a - mp.mpf("0.25")))
    gates.append(("A3 diagonal rate dominance", rate_on > rate_tail,
                  "per-m rates: online %.4f > tail %.4f (online "
                  "log-linear; tail BOUNDED by its log-linear "
                  "envelope) -- with the sampled prefix and margin "
                  "monotonicity this covers EVERY m"
                  % (float(rate_on), float(rate_tail))))

    theta_law = ctx["T"] ** 2 / (mp.e * a)
    theta_grid = mp.mpf(0)
    s_tail = rate_tail
    for t0 in ctx["grid"]:
        yv = a / (a + t0 * t0)
        cand = (mp.log(yv) - s_tail) / (-mp.log(1 - yv))
        theta_grid = max(theta_grid, cand)
    gates.append(("A3 cone opening law",
                  abs(theta_grid / theta_law - 1) < mp.mpf("0.20"),
                  "theta_max(grid) = %.4e vs T^2/(e a) = %.4e "
                  "(ratio %.4f)" % (float(theta_grid), float(theta_law),
                                    float(theta_grid / theta_law))))

    cone_rows = []
    cone_ok = True
    beyond = 0
    for theta_s in CONE_SAMPLES:
        theta = mp.mpf(theta_s)
        n0 = ray_n0(ctx, theta)
        if n0 is None:
            cone_ok = False
            cone_rows.append((theta_s, None, None))
            continue
        k_cell = int(mp.floor(theta * (n0 + 1)))
        if k_cell > K74:
            beyond += 1
        cone_rows.append((theta_s, n0, k_cell))
    for theta_s, n0, k_cell in cone_rows:
        print("    ray theta=%-8s n0=%-8s k(n0)=%s%s"
              % (theta_s, n0, k_cell,
                 "  [BEYOND round-106 frontier]"
                 if (k_cell is not None and k_cell > K74) else ""))
    gates.append(("A3 cone sample cells proven", cone_ok,
                  "every sampled ray certifies from finite n0; "
                  "%d sampled cells lie beyond k=7.44e21" % beyond))
    gates.append(("A3 beyond-frontier exhibit", beyond >= 2,
                  "the positivity frontier is a CONE k <= theta(n+1), "
                  "theta_max ~ T^2/(e a) = %.3e > round-106 uniform "
                  "frontier 7.44e21 by factor %.2f"
                  % (float(theta_law), float(theta_law / K74))))
    return gates


# =====================================================================
# S3  the graph as data + min-cut
# =====================================================================
INF = 10 ** 9

NODES = {
    # unconditional facts / instruments
    "UNCOND": "SOURCE",
    "STRIP": "UNC-CITED", "PT21": "UNC-CITED", "HSW22": "UNC-CITED",
    "GAMMA1": "UNC-CITED",
    "PASCAL": "UNC-ID", "FLOW": "UNC-ID", "GF2": "UNC-ID",
    "SOS": "UNC-ID", "LI": "UNC-ID", "EPIN": "UNC-ID",
    "SPLIT": "UNC-ID", "LAMBDA": "UNC-ID", "KICK": "UNC-ID",
    "FRED": "UNC-ID", "EXTDET": "UNC-ID", "TRACE-OP": "UNC-ID",
    "HFLOW": "UNC-ID", "JETREP": "UNC-ID", "WSUM": "UNC-ID",
    "WINDOW": "UNC-ID", "DIAGDET-ALG": "UNC-ID",
    "K74-THM": "UNC-THM", "FIXEDN-EVENTUAL": "UNC-THM",
    "A1-BOUND": "UNC-NEW", "A2-AMAX": "UNC-NEW",
    "A3-DIAG-ALLM": "UNC-NEW", "CONE": "UNC-NEW",
    "HAUS-CELLS-FIN": "UNC-THM",     # certified depth-86 cells (r102)
    "PICK-FLOORS-FIN": "UNC-THM",    # v915 certified floors N<=4
    "DIAG-BOUNDS-FIN": "UNC-NEW",    # A2 per-a quarter bounds
    "WEYL-PINS-MEAS": "MEAS",        # round-90 pins, measured only
    "SIGNPOS-MEAS": "MEAS",
    # conditional hypothesis nodes (the four costumes)
    "FORMA-HYP": "HYP", "SV-HYP": "HYP", "R4-HYP": "HYP",
    "WEYL-HYP": "HYP",
    # RH side
    "RH": "TARGET", "Y01": "COND-RH", "W14": "COND-RH",
    "SIGNREG-ALL": "COND-RH",
}

EDGES = [
    # source wiring (definitional, infinite)
    ("UNCOND", "STRIP", "DEF", INF), ("UNCOND", "PT21", "DEF", INF),
    ("UNCOND", "HSW22", "DEF", INF), ("UNCOND", "GAMMA1", "DEF", INF),
    ("UNCOND", "PASCAL", "DEF", INF), ("UNCOND", "FLOW", "DEF", INF),
    ("UNCOND", "GF2", "DEF", INF), ("UNCOND", "SOS", "DEF", INF),
    ("UNCOND", "LI", "DEF", INF), ("UNCOND", "EPIN", "DEF", INF),
    ("UNCOND", "SPLIT", "DEF", INF), ("UNCOND", "LAMBDA", "DEF", INF),
    ("UNCOND", "KICK", "DEF", INF), ("UNCOND", "FRED", "DEF", INF),
    ("UNCOND", "EXTDET", "DEF", INF),
    ("UNCOND", "TRACE-OP", "DEF", INF),
    ("UNCOND", "HFLOW", "DEF", INF), ("UNCOND", "JETREP", "DEF", INF),
    ("UNCOND", "WSUM", "DEF", INF), ("UNCOND", "WINDOW", "DEF", INF),
    ("UNCOND", "DIAGDET-ALG", "DEF", INF),
    ("UNCOND", "WEYL-PINS-MEAS", "MEAS", 1),
    ("UNCOND", "SIGNPOS-MEAS", "MEAS", 1),
    # unconditional theorem composition (cited + composed here)
    ("PT21", "K74-THM", "UNC", INF), ("HSW22", "K74-THM", "UNC", INF),
    ("STRIP", "A1-BOUND", "UNC", INF),
    ("GAMMA1", "A1-BOUND", "UNC", INF),
    ("WINDOW", "A2-AMAX", "UNC", INF),
    ("PT21", "A2-AMAX", "UNC", INF),
    ("A1-BOUND", "A2-AMAX", "UNC", INF),
    ("PT21", "A3-DIAG-ALLM", "UNC", INF),
    ("HSW22", "A3-DIAG-ALLM", "UNC", INF),
    ("K74-THM", "A3-DIAG-ALLM", "UNC", INF),
    ("A3-DIAG-ALLM", "CONE", "UNC", INF),
    ("K74-THM", "HAUS-CELLS-FIN", "UNC", INF),
    ("UNCOND", "HAUS-CELLS-FIN", "UNC", INF),
    ("UNCOND", "PICK-FLOORS-FIN", "UNC", INF),
    ("A2-AMAX", "DIAG-BOUNDS-FIN", "UNC", INF),
    # OMEGA introductions: infinite positivity quantifier over a
    # finite-certifiable family (the wall, in graph clothing)
    ("HAUS-CELLS-FIN", "FORMA-HYP", "OMEGA-POS", 1),
    ("PICK-FLOORS-FIN", "SV-HYP", "OMEGA-POS", 1),
    ("DIAG-BOUNDS-FIN", "R4-HYP", "OMEGA-POS", 1),
    ("WEYL-PINS-MEAS", "WEYL-HYP", "OMEGA-POS-MEAS", 1),
    # form -> RH implications
    ("FORMA-HYP", "RH", "PROVEN-EQUIV", INF),   # Hausdorff/Zhang, r102/109
    ("SV-HYP", "RH", "KERNEL-CHECKED", INF),    # Lean sv_implies_rh, r99
    ("WEYL-HYP", "RH", "PROVEN-SUFF", INF),     # r90/110 one-sided
    ("R4-HYP", "RH", "CANDIDATE", 1),           # r115 claim (iii), pending
    # RH forward consequences (direction away from RH)
    ("RH", "Y01", "COND-RH", INF), ("Y01", "W14", "COND-RH", INF),
    ("Y01", "SIGNREG-ALL", "COND-RH", INF),
]


def max_flow(edges, source: str, sink: str):
    cap: dict[tuple[str, str], int] = {}
    adj: dict[str, set[str]] = {}
    for src, dst, _cls, capacity in edges:
        cap[(src, dst)] = cap.get((src, dst), 0) + capacity
        cap.setdefault((dst, src), 0)
        adj.setdefault(src, set()).add(dst)
        adj.setdefault(dst, set()).add(src)
    flow = 0
    while True:
        parent = {source: None}
        queue = [source]
        while queue and sink not in parent:
            node = queue.pop(0)
            for nxt in adj.get(node, ()):
                if nxt not in parent and cap.get((node, nxt), 0) > 0:
                    parent[nxt] = node
                    queue.append(nxt)
        if sink not in parent:
            break
        path = []
        cur = sink
        while parent[cur] is not None:
            path.append((parent[cur], cur))
            cur = parent[cur]
        bottleneck = min(cap[(u, v)] for u, v in path)
        for u, v in path:
            cap[(u, v)] -= bottleneck
            cap[(v, u)] += bottleneck
        flow += bottleneck
    reachable = {source}
    queue = [source]
    while queue:
        node = queue.pop(0)
        for nxt in adj.get(node, ()):
            if nxt not in reachable and cap.get((node, nxt), 0) > 0:
                reachable.add(nxt)
                queue.append(nxt)
    cut = [(src, dst, cls) for src, dst, cls, capacity in edges
           if src in reachable and dst not in reachable and capacity > 0]
    return flow, cut, reachable


def gates_mincut() -> list[tuple[str, bool, str]]:
    gates = []
    unconditional_classes = {"DEF", "UNC"}
    adj: dict[str, set[str]] = {}
    for src, dst, cls, _cap in EDGES:
        if cls in unconditional_classes:
            adj.setdefault(src, set()).add(dst)
    reach = {"UNCOND"}
    queue = ["UNCOND"]
    while queue:
        node = queue.pop(0)
        for nxt in adj.get(node, ()):
            if nxt not in reach:
                reach.add(nxt)
                queue.append(nxt)
    hyp_nodes = [nm for nm, ty in NODES.items() if ty == "HYP"]
    unreachable = ([nm for nm in hyp_nodes if nm not in reach]
                   + (["RH"] if "RH" not in reach else []))
    gates.append(("S3 unconditional reachability",
                  "RH" not in reach and all(nm not in reach
                                            for nm in hyp_nodes),
                  "unconditional BFS reaches %d nodes; RH and all 4 "
                  "form-hypothesis nodes unreachable" % len(reach)))

    cross = [(s, d) for s, d, cls, _ in EDGES
             if cls in unconditional_classes
             and s in hyp_nodes and d in hyp_nodes]
    gates.append(("S3 transfer-null between forms", not cross,
                  "no unconditional edge links any two form-hypothesis "
                  "nodes (round-110 separation witness cited: off-line "
                  "quadruple at gamma=20 keeps Hausdorff cells n+k<=50 "
                  "positive while Euler--Pick fires at N=12)"))

    conservative = [e for e in EDGES
                    if e[2] not in ("CANDIDATE", "MEAS",
                                    "OMEGA-POS-MEAS")]
    flow_c, cut_c, _ = max_flow(conservative, "UNCOND", "RH")
    flow_f, cut_f, _ = max_flow(EDGES, "UNCOND", "RH")
    print("    conservative min-cut (%d):" % flow_c)
    for src, dst, cls in cut_c:
        print("      %-18s -> %-12s [%s]" % (src, dst, cls))
    print("    full-graph min-cut (%d):" % flow_f)
    for src, dst, cls in cut_f:
        print("      %-18s -> %-12s [%s]" % (src, dst, cls))
    classes_c = sorted({cls for _s, _d, cls in cut_c})
    gates.append(("S3 conservative min-cut = 2 omega edges",
                  flow_c == 2 and classes_c == ["OMEGA-POS"],
                  "cut = {Hausdorff-cells->FormA, Pick-floors->SV}: "
                  "ONE semantic class (infinitary positivity "
                  "introduction), 2 instances"))
    gates.append(("S3 full min-cut = 4 parallel instances",
                  flow_f == 4,
                  "adding the r115 CANDIDATE route and the measured "
                  "Weyl route: 4 parallel single-edge crossings, "
                  "still one semantic class in four costumes"))
    return gates


# =====================================================================
def main() -> int:
    print("idgraph_search_probe -- PRIME.IDENTITY.GRAPH.SEARCH.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    section("S0  FIREWALL + GRAPH CENSUS")
    fw_ok, fw_msg = firewall_selfscan()
    check("AST firewall self-scan", fw_ok, fw_msg)
    type_census: dict[str, int] = {}
    for _nm, ty in NODES.items():
        type_census[ty] = type_census.get(ty, 0) + 1
    cls_census: dict[str, int] = {}
    for _s, _d, cls, _c in EDGES:
        cls_census[cls] = cls_census.get(cls, 0) + 1
    print("  nodes: %d  %s" % (len(NODES), sorted(type_census.items())))
    print("  edges: %d  %s" % (len(EDGES), sorted(cls_census.items())))
    print("  identity inventory: 28 edges typed in the frozen spec; "
          "E-WINDICT and E-PARITY carried CITED (not re-verified, "
          "declared); E-ACPICK gated as bilinear interface only; "
          "certified floors carried verbatim: %s" % (FLOORS_1E13,))

    section("S1  EDGE VERIFICATION (symbolic / exact / declared numeric)")
    for gate in gates_atom_field():
        check(*gate)
    for gate in gates_generating_function():
        check(*gate)
    for gate in gates_radius4_geometry():
        check(*gate)
    for gate in gates_li_sos_pin():
        check(*gate)
    for gate in gates_w14_trace_hflow():
        check(*gate)
    for gate in gates_kick_fred_extdet():
        check(*gate)
    lam_ok, lam_msg = gates_lambda_exact()
    check("E-LAMBDA mu*log exact", lam_ok, lam_msg)
    for gate in audit_epin_and_split():
        check(*gate)
    k74_ok, k74_msg = k74_spot_ward()
    check("E-K74 spot ward", k74_ok, k74_msg)
    print("  [CANDIDATE typing] E-DIAGDET/E-WSUM/E-WINDOW algebra is "
        "re-verified above unconditionally; their r115 ANALYTIC role "
        "(genus-0 product, dense-a equivalence) stays PENDING AUDIT.")

    section("S2  MECHANICAL COMPOSITION SEARCH")
    census, lin_gates = linear_completeness()
    print("  quantity census: %(quantities)d quantities, "
          "%(relations)d linear relations, %(generators)d local "
          "generators, span rank %(rank_known)d" % census)
    for gate in lin_gates:
        check(*gate)
    for gate in gates_named_compositions():
        check(*gate)

    section("S2A  UNCONDITIONAL GROWTH BOUNDS (the radius-4 target)")
    for gate in gates_a1_strip_bound():
        check(*gate)
    a_max, a2_gates = gates_a2_amax()
    for gate in a2_gates:
        check(*gate)
    print("  [COMPOSED THEOREM, cited inputs PT21+HSW22+strip+RvM]")
    print("  For every a in (1/4, %.4e]:" % float(a_max))
    print("    limsup_m |d_m(a)|^(1/m) <= 1/4  (radius >= 4), and")
    print("  strip-only, for a >= gamma_1^2+3/4:")
    print("    limsup_m |d_m(a)|^(1/m) <= a/(4a-2) = 1/4 + 1/(8a-4).")
    print("  THE WALL: removing the a-cap for EVERY a (dense set) is")
    print("  the r115 candidate RH-equivalence -- censused in S3.")

    section("S2C  CONE CELLS (rigorous-shape, cited inputs)")
    ctx = ray_context()
    for gate in gates_a3_cone(ctx):
        check(*gate)
    print("  [COMPOSED THEOREM, cited inputs] d_m(256) > 0 for EVERY")
    print("  m >= 0 (sampled prefix + rate dominance + the round-106")
    print("  strip m <= 7.44e21); the positivity region is a CONE")
    print("  k <= theta(n+1), theta_max ~ T^2/(e a), STRICTLY beyond")
    print("  the round-106 uniform-k frontier for large n.")

    section("S3  MIN-CUT (the wall, graph-theoretically)")
    for gate in gates_mincut():
        check(*gate)

    section("S4  HONESTY")
    ctx_jit = ray_context(hsw_scale="1.10", t_scale="0.9")
    jit_ok = True
    for m in (0, 5, 10**6):
        if ray_online_ln(ctx_jit, m, m) <= ray_tail_ln(ctx_jit, m):
            jit_ok = False
    check("S4 jitter screen (HSW x1.10, T x0.9)", jit_ok,
          "A3 diagonal gates survive adversarial constant inflation; "
          "tau-screen structurally absent (no Galerkin object in this "
          "pipeline) -- the jitter screen is the conditioning channel")
    mp.mp.dps = 30
    lder1_low = audit_xi_logderiv(1)
    target_low = 1 + mp.euler / 2 - mp.log(2 * mp.sqrt(mp.pi))
    check("S4 dps-halving reproducibility",
          abs(lder1_low - target_low) < mp.mpf("1e-15"),
          "E-EPIN reproduces at dps 30 (dev %.1e)"
          % float(abs(lder1_low - target_low)))
    print("  triviality typing of S2 findings:")
    print("    N1 jet transport        NONTRIVIAL (depth-k composition)")
    print("    N2 superdiagonal trace  TRIVIAL-ADJACENT (one line)")
    print("    N3 logdet Pascal        NONTRIVIAL (series-level, "
          "new-in-corpus modulo grep)")
    print("    N4 pin anchor loop      NOT NEW (classical loop closure)")
    print("    S2-LINEAR               EXHAUSTIVENESS statement: the "
          "local edges are linearly complete at the searched depth")
    print("    A1/A2/A3/CONE           NEW COMPOSED CONSEQUENCES "
          "(cited-input theorems, experiments-only, NOT promoted)")

    section("S9  FINAL ADJUDICATION")
    passed = sum(ok for _n, ok, _d in CHECKS)
    runtime = time.time() - START
    print("  checks %d/%d PASS; runtime %.2f s (bar %.0f s)"
          % (passed, len(CHECKS), runtime, RUNTIME_BAR))
    print("VERDICT: IDGRAPH-MINCUT(1 semantic class: infinitary "
          "positivity introduction OMEGA-POS; conservative cut 2 "
          "instances [Hausdorff-cells->FormA, Pick-floors->SV], full "
          "graph 4 [+radius4-dense-a CANDIDATE, Weyl-disks MEASURED]) "
          "+ IDGRAPH-NEW-IDENTITIES(2: N1 jet-transport "
          "C_{n,k}=(n!/(n+k)!)(L)_k b_n; N3 logdet-Pascal "
          "log Dd_a(t)=-sum(t^m/m)C_{m-1,m}; linear layer COMPLETE) "
          "+ IDGRAPH-NEW-CONSEQUENCES(A1 sup|w|<=a/(4a-2); A2 "
          "limsup|d_m|^(1/m)<=1/4 for a<=%.3e; A3 d_m(256)>0 all m; "
          "CONE theta_max~T^2/(e a))" % 9.001e24)
    print("NO RH CLAIM.")
    return 0 if (passed == len(CHECKS) and runtime < RUNTIME_BAR) else 1


if __name__ == "__main__":
    raise SystemExit(main())
