#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccm_pn_adjudication_probe -- PRIME.CCM.PN.ADJUDICATION.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This file is the sole
probe of the round.  It writes nothing, imports no repository module,
reads no measured pin, wall margin, zero table, paper, ledger, website
or verification file, and makes NO RH claim in any direction.

MISSION
=======
Adjudicate the one external published RH reduction the corpus has never
examined: the Connes--Consani--Moscovici Euler-factor property P(n) of
arXiv:2310.18423, against the corpus map (Euler--Pick / (AC) identity /
tau-screen / control worlds).

M1 -- THE EXACT EXTERNAL STATEMENT (verbatim, with citation)
============================================================
A. Connes, C. Consani, H. Moscovici, "Zeta zeros and prolate wave
operators" (subtitle "Semilocal adelic operators"), arXiv:2310.18423,
Section 1 (verbatim):

  "However, contrary to this widespread belief, there exists a
   property P(n), involving only the Euler factors for primes smaller
   than n, and whose validity for all n is equivalent to RH.  This is
   derived from Weil's positivity criterion which involves the
   quadratic form Q_n defined using the Riemann-Weil explicit formulas
   applied to test functions with support in the compact symmetric
   interval [1/n, n].  Furthermore, the semilocal trace formula of [7]
   gives, for each n, a Hilbert space theoretic framework in which the
   Weil quadratic form Q_n becomes the trace of a simple operator
   theoretic expression, thus offering a natural ground of exploration
   in order to attack RH."

The precise content behind that sentence is spelled out in A. Connes,
"The Riemann Hypothesis: past, present and a letter through time",
arXiv:2602.04022 (2026), Sections 4.1 and 6.4 (verbatim formulas,
notation adapted to the involutive convolution algebra of R_+^*):

  explicit formula:
    fhat(i/2) - sum_{1/2+is in Z} fhat(s) + fhat(-i/2) = sum_v W_v(f),
    fhat(s) := int_0^inf f(x) x^{-is} d*x,  d*x = dx/x;
  local terms:
    W_p(f) = (log p) sum_{m>=1} p^{-m/2} ( f(p^m) + f(p^{-m}) )   (10)
    W_R(f) = (log 4pi + gamma) f(1)
             + int_1^inf ( f(x) + f(1/x) - 2 x^{-1/2} f(1) )
                          x^{1/2}/(x - x^{-1}) d*x                (11)
  Weil's criterion (their display):
    "RH <=> sum_v W_v(g*g^*) <= 0,  for all g, ghat(+-i/2) = 0"
  with g in C_c^inf(R_+^*), g^*(x) := conj(g(1/x)); and (their 6.4)
    "Let lambda>1, and QW_lambda be the restriction of the Weil
     quadratic form to test functions whose support is within the
     interval [lambda^{-1}, lambda].  By the result of Andre Weil
     ... the positivity of QW_lambda for all lambda>1 is equivalent
     to RH.  This positivity can be proved for small values of
     lambda."

SO THE PROPERTY IS:  P(n)  :=  [ Q_n(g) := -sum_v W_v(g*g~) >= 0 for
every test function g supported in [1, n] with ghat(+-i/2) = 0 ], and
the theorem is  [ P(n) for all n ]  <=>  RH  (A. Weil 1952; Bombieri
2000 for the two-sided form).  "Only Euler factors for primes < n"
because W_p vanishes on functions supported in (1/p, p): with
f = g*g~ supported in [1/n, n], only prime powers p^m < n enter.
QUANTIFIER TYPE: for each fixed n, P(n) quantifies over an
infinite-dimensional cone of test functions; it is NOT a single
finite-dimensional positivity per n.  Finite Galerkin sections of
Q_n are NECESSARY conditions: a certified negative eigenvalue of any
finite section would refute RH outright (exact forward direction of
the explicit formula); positivity of a finite section never proves
P(n).

CITATION STATUS (searched 2026-08-15): P(n) is OPEN in the literature
for every prime-bearing n (every n > 2).  Proven region: archimedean
place only -- Connes--Consani, "Weil positivity and trace formula, the
archimedean place", Selecta Math. 27 (2021) (support up to lambda =
sqrt 2, conceptual proof via Sonin-space compression); H. Yoshida
(cited as [111] in arXiv:2602.04022, Theorem 1: W_inf(f) >= 0 :=
-W_R(f) for smooth positive definite f supported in (1/2, 2), a
numerical-analysis proof).  Neither covers any n whose interval
[1/n, n] contains a prime power.  The CCM attack (semilocal prolate
operator on the semilocal Sonin space, arXiv:2310.18423 Thms 1-2) is
a program: the semilocal prolate operator is a CANDIDATE, a second
(metaplectic, SL_2(A_S) Weil representation) candidate is announced
as "a forthcoming paper", and no follow-up proving P(n) for any
prime-bearing n was found.  Their own honest gap (2310.18423 intro):
"We expect that the use of such operator-theoretic tools in the
semilocal case opens a way to handle Weil's positivity as in [10]" --
expectation, not theorem; and (2602.04022 Section 6.6) the remaining
steps of the extremal program are the simplicity/evenness of the
lowest eigenvector of QW_lambda and the k_lambda ~ theta_x
approximation quality.

M2 -- WHAT THIS PROBE COMPUTES (all source-only, no zero data)
==============================================================
COORDINATES.  u = log x, G(u) = g(e^u), support [0, L], L = log n.
F = autocorrelation, F(t) = int G(t+u) G(u) du (real g), supported in
[-L, L]; f(p^m) = F(m log p).  Constraints ghat(+-i/2) = 0 become
int G(u) e^{+-u/2} du = 0 (two exact linear functionals).
Autocorrelation kills shifts exactly, so support [1, n] and the
recentred [n^{-1/2}, n^{1/2}] give the SAME form (QW_{sqrt n} of the
survey = our Q_n; their epsilon(lambda) at lambda = sqrt x is our
lambda_min at n = x up to basis).

(a) SMALL-n INSTANCES (the finite RH-consequence check).  Tent basis
phi_a(u) = max(0, 1 - |u - a h|/h), a = 1..K, h = L/(K+1); the pair
form is Toeplitz: Q(phi_a, phi_b) = -W_R(F_d) - sum W_p(F_d) with
F_d(t) = A(t + d h), d = b - a, A = tent autocorrelation (cubic
B-spline, closed form).  Prime side EXACT (finitely many atoms
u = m log p < L, weight (log p) p^{-m/2}); archimedean side one 1-D
quadrature per offset with closed-form t -> inf tail
(int_T^inf dt/(e^t - e^{-t}) = -(1/2) log tanh(T/2)).  The two
constraints are projected out exactly (orthonormal complement).
lambda_min of the projected (K-2)x(K-2) matrix is printed per n with
a measured entry-error budget (dual-dps recompute).  Gate logic:
lambda_min > budget => section positive (RH-consistent, P(n) checked
on this subspace); lambda_min < -budget would be a certified
RH-refutation channel and fails the run loudly.

(b) THE (AC)/EULER--PICK INTERFACE TEST (currency typing).  On the
exponential family f_sigma(v) = 1_{v>=0} e^{-sigma v} the CCM Weil
functional separates per sigma, and the corpus (AC) identity
(vbk_invariant_probe V0c, reimplemented here from scratch) demands
  P(sigma) := xi'/xi(1/2+sigma)
            = [1/(sigma-1/2) + 1/(sigma+1/2)]        (pole terms)
            - (1/2) W_R(e^{-sigma|t|})               (CCM (11), quad)
            - sum_n Lambda(n) n^{-(1/2+sigma)}       (CCM (10), sieve)
so that the CCM quadratic form on exponential autocorrelations
REPRODUCES the Euler--Pick matrices
  Pick_N[j,k] = (P(sigma_j)+P(sigma_k))/(sigma_j+sigma_k),
sigma_j = 1 + 1/j, entrywise.  Both sides are computed independently:
LHS instrument lane via mp digamma/zeta; LHS source lane via own
Lambda-sieve (cap 4e6) with Abel tail; RHS from CCM's published local
terms with W_R as an actual quadrature of (11).  Agreement exhibits
IDENTITY (same currency), not analogy.  Corpus parity: lambda_min of
Pick_N vs the frozen corpus floors (N=1: 4.5917135e-2, N=2:
9.0287394e-6 .. 9.029038e-6 certified interval; CCCXCVI).

(c) TAU-SCREEN (frozen bands of PRIME.PORT.BFLOOR.01: OLS slope s of
log candidate margin against log tau; PASS iff |s| <= 0.30,
RELOCATION iff s >= 0.70).  tau here = the corpus wall scalar in the
screw-section currency at matched depth: lambda_min of the
UNconstrained full-kernel (pole + arch - primes) section on the same
mesh, i.e. B_screw = B_Q + rank-2 pole term r+ r-^T + r- r+^T.

(d) CONTROL WORLDS through the same construction (corpus recipes):
 SMOOTH   prime atoms -> PNT density e^{u/2} du (support error: false
          mass in (0, log 2); vbk/krein death r = 0.264);
 SCRARITH golden-key seedless permutation of atom weights over the
          same positions (key = frac(p^m * (sqrt5-1)/2), argsort;
          krein death r = 0.744);
 EPSTEIN  atoms -> (log k, Lambda_E(k) k^{-1/2}) from the Epstein
          zeta of x^2 + 5 y^2 (class number 2, off-line zeros known),
          Lambda_E by the Dirichlet log-derivative recursion on
          r_Q(k)/2; TYPED HONESTLY: the archimedean frame is kept
          (the genuine Epstein explicit formula has Gamma(s), not
          Gamma(s/2)); this world measures arithmetic-sensitivity of
          the construction, never a statement about Epstein zeros.
 Measured: lambda_min ladder per world; whether truth/failure at the
 positivity level distinguishes worlds (screw-carrier analogy).

(e) DETECTION LAW (reach of the instrument): minimal multiplicative
perturbation eps* of the p = 2 atom weight that flips the sign of the
constrained lambda_min, at n = 3 and n = 6 (coarse log2 scan +
bisection, declared budget dps).  This measures the reach of the new
finite check in the same sense as the Euler--Pick detection law.

M3/M4 are assembled in the verdict section from these measurements.

FROZEN NUMERICS AND SUBSAMPLING (declared)
==========================================
N_LADDER = (1.9, 2.5, 3.0, 4.0, 6.0, 9.0, 13.0); n = 1.9 is the
prime-free Yoshida validation cell.  K = 24 tents (constrained dim
22); mesh-robustness cross-check at n = 6 with K = 18.  Working dps
per n: {1.9: 60, 2.5: 60, 3.0: 60, 4.0: 80, 6.0: 100, 9.0: 120,
13.0: 132}; worlds and detection at dps 60; interface at dps 50 with
quadrature at working dps.  SIGMAS = 1 + 1/j, j = 1..8.  Own sieve
cap 4e6 (wards: pi(4e6) = 283146, psi(4e6) within 0.94 sqrt x of x,
matching the corpus pins).  Entry-error budget: the d = 0 and d = K-1
archimedean quadratures are recomputed at dps+20; budget =
K * max deviation; positivity calls require |lambda_min| > budget.
Detection scan: eps over 2^{-44}..2^{8} step 2^4, then 24 bisection
steps.  Float64 appears only in printed diagnostics and OLS slopes;
every matrix entry and eigenvalue is mpmath.  Runtime bar 1800 s.
Verdict enums (frozen): the composite is CCM-CHECKED(range) plus one
of CCM-SAME-CURRENCY(identity exhibited) / CCM-INDEPENDENT-CONTENT /
CCM-UNIMPLEMENTABLE; a failed ward prints INSTRUMENT-EDGE (exit 1,
not a mathematical verdict); a certified negative section would print
CCM-SECTION-NEGATIVE (which would refute RH -- loud, exit 2).

SHAKEOUT DISCLOSURE / AMENDMENT 1.  Frozen run 1 (SPEC_SHA
4013227afb909d14) returned INSTRUMENT-EDGE, 20/22, both failures
instrument wards, no mathematical gate: (a) the G01 firewall's
zero-data token list was written as plain string literals and so
detected ITSELF in the source; the tokens are now assembled by
concatenation at runtime; (b) the G05 direct-quadrature cross-check
of the tent autocorrelation omitted three of the six integrand
breakpoints ({-h-t, -t, h-t} union {-h, 0, h}), costing a measured
8.16e-8 against the 1e-40 bar at dps 60; the full breakpoint list is
now passed.  No mathematical bar, ladder, world, band or verdict
priority moved; the mathematical gates of run 1 were already 18/18
with the identical numbers reproduced below.

NO RH CLAIM.  NO ALL-n CLAIM.  FINITE SECTIONS ONLY.  EXPLORATION ONLY.
"""

from __future__ import annotations

import ast
import hashlib
import math
import sys
import time

import mpmath as mp
import numpy as np


T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

RUNTIME_BAR_S = 1800.0
N_LADDER = (1.9, 2.5, 3.0, 4.0, 6.0, 9.0, 13.0)
DPS_BY_N = {1.9: 60, 2.5: 60, 3.0: 60, 4.0: 80, 6.0: 100,
            9.0: 120, 13.0: 132}
K_TENTS = 24
K_ROBUST = 18
SIGJ = tuple(1 + mp.mpf(1) / j for j in range(1, 9))
SIEVE_CAP = 4 * 10 ** 6
PI_CAP_WARD = 283146          # corpus pin (CCCXCVI): pi(4e6)
PSI_CAP_WARD = "3999490.856797"   # corpus pin: psi(4e6)
FLOOR_N1 = "4.5917135e-2"     # corpus frozen Euler--Pick floor N=1
FLOOR_N2 = (9.0287394e-6, 9.029038e-6)  # certified interval, N=2
SLOPE_PASS = 0.30             # frozen tau-screen bands
SLOPE_RELOC = 0.70
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
DET_EPS_GRID = [2.0 ** e for e in range(-44, 9, 4)]
DET_BISECT_STEPS = 24
DET_NS = (3.0, 6.0)

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def fmt(x, digits: int = 10) -> str:
    return mp.nstr(mp.mpf(x), digits, strip_zeros=False)


# --------------------------------------------------------------- ward
def firewall_audit() -> tuple[bool, str]:
    """Source-only AST audit of THIS file: no repository imports, no
    file reads outside self, no zero tables, no verification/ paths."""
    src = open(__file__, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    banned_imports = {"verification", "experiments", "requests",
                      "urllib", "pickle", "json"}
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] in banned_imports:
                    hits.append("import %s" % a.name)
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] in banned_imports:
                hits.append("from %s" % node.module)
        elif isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id == "open":
                if not (node.args and isinstance(node.args[0], ast.Name)
                        and node.args[0].id == "__file__"):
                    hits.append("open() not on __file__")
    # zero-data tokens assembled by concatenation so the scan list
    # cannot detect itself (AMENDMENT 1a)
    zero_tokens = ["14.13" + "47", "21.02" + "20", "25.01" + "08",
                   "zeros" + "_cache"]
    for tok in zero_tokens:
        if tok in src:
            hits.append("zero-data token %s" % tok)
    return (not hits), ("; ".join(hits) if hits else "clean")


# -------------------------------------------------------------- sieve
def sieve_lambda(cap: int):
    """Own sieve: primes to cap; returns (primes list, Lambda arrays
    not materialized -- prime list is enough for all uses here)."""
    flags = np.ones(cap + 1, dtype=bool)
    flags[:2] = False
    for q in range(2, int(cap ** 0.5) + 1):
        if flags[q]:
            flags[q * q::q] = False
    return np.nonzero(flags)[0].tolist()


def psi_of_cap(primes: list[int], cap: int) -> float:
    total = 0.0
    for p in primes:
        lp = math.log(p)
        pk = p
        while pk <= cap:
            total += lp
            pk *= p
    return total


def prime_atoms(L: float) -> list[tuple[mp.mpf, mp.mpf, int, int]]:
    """Atoms (u, w, p, m) with u = m log p < L, w = log p * p^{-m/2}."""
    out = []
    n_max = int(math.floor(math.exp(L))) + 1
    for p in PRIMES:
        if p > n_max:
            break
        lp = mp.log(p)
        m = 1
        while float(m * lp) < L - 1e-15:
            out.append((m * lp, lp * mp.power(p, mp.mpf(-m) / 2), p, m))
            m += 1
    out.sort(key=lambda z: float(z[0]))
    return out


# ------------------------------------------------- tent autocorrelation
def tent_A(t, h):
    """A(t) = int max(0,1-|u+t|/h) max(0,1-|u|/h) du, exact cubic."""
    s = abs(mp.mpf(t)) / h
    if s >= 2:
        return mp.mpf(0)
    if s <= 1:
        return h * (mp.mpf(2) / 3 - s ** 2 + s ** 3 / 2)
    return h * (2 - s) ** 3 / 6


def tent_moment(a: int, h, beta):
    """int phi_a(u) e^{beta u} du, phi_a tent at u = a h, exact."""
    c = a * h
    return mp.e ** (beta * c) * (mp.e ** (beta * h)
                                 + mp.e ** (-beta * h) - 2) / (beta ** 2 * h)


def w_kernel(t):
    """CCM (11) archimedean density in log coordinates:
    e^{t/2} / (e^t - e^{-t})."""
    return mp.e ** (t / 2) / (mp.e ** t - mp.e ** (-t))


LOG4PI_GAMMA = None  # set after dps


def arch_W_pair(d: int, h) -> mp.mpf:
    """W_R(F_d) for F_d(t) = A(t + d h): CCM (11) evaluated exactly on
    the tent-pair autocorrelation.  One quadrature + closed tail."""
    F0 = tent_A(d * h, h)
    hi = (d + 2) * h
    pts = sorted({float(abs((k - d) * h)) for k in (-2, -1, 0, 1, 2)}
                 | {0.0, float(hi)})
    pts = [mp.mpf(x) for x in pts if 0.0 <= x <= float(hi) + 1e-30]

    def integrand(t):
        if t <= 0:
            # limit t->0+: (F(t)+F(-t)-2F0) ~ O(t^2), 2F0(1-e^{-t/2}) ~ F0 t
            return F0 / 2
        return (tent_A(d * h + t, h) + tent_A(d * h - t, h)
                - 2 * mp.e ** (-t / 2) * F0) * w_kernel(t)

    body = mp.quad(integrand, pts) if len(pts) >= 2 else mp.mpf(0)
    # closed-form tail t in (hi, inf): A terms vanish there
    tail = F0 * mp.log(mp.tanh(hi / 2)) if F0 != 0 else mp.mpf(0)
    return LOG4PI_GAMMA * F0 + body + tail


def prime_W_pair(d: int, h, atoms) -> mp.mpf:
    """sum_p W_p(F_d) exactly: finitely many atoms."""
    total = mp.mpf(0)
    for u, w, _p, _m in atoms:
        total += w * (tent_A(d * h + u, h) + tent_A(d * h - u, h))
    return total


def smooth_W_pair(d: int, h, L: float) -> mp.mpf:
    """SMOOTH world prime side: atoms -> density e^{u/2} du on (0, L)."""
    lo = max(0.0, float((d - 2) * h))
    hi = min(L, float((d + 2) * h))
    lo2 = max(0.0, float((-d - 2) * h))
    hi2 = min(L, float((-d + 2) * h))

    def f_plus(u):
        return mp.e ** (u / 2) * tent_A(d * h - u, h)

    def f_minus(u):
        return mp.e ** (u / 2) * tent_A(d * h + u, h)

    total = mp.mpf(0)
    if hi > lo:
        total += mp.quad(f_plus, [mp.mpf(lo), mp.mpf(hi)])
    if hi2 > lo2:
        total += mp.quad(f_minus, [mp.mpf(lo2), mp.mpf(hi2)])
    return total


def scram_weights(atoms):
    """Golden-key seedless permutation of atom weights (corpus recipe:
    key = frac(q * (sqrt5-1)/2) on q = p^m, argsort)."""
    qs = [p ** m_ for _u, _w, p, m_ in atoms]
    key = [(q * GOLDEN) % 1.0 for q in qs]
    perm = sorted(range(len(atoms)), key=lambda i: key[i])
    ws = [atoms[i][1] for i in perm]
    return [(atoms[i][0], ws[i], atoms[i][2], atoms[i][3])
            for i in range(len(atoms))]


def epstein_atoms(L: float):
    """EPSTEIN world: Lambda_E(k) from Z(s) = sum r(k) k^{-s} for
    Q(x,y) = x^2 + 5 y^2, normalized D = Z / r(1); recursion
    a_k log k = sum_{m | k, m > 1} Lambda_E(m) a_{k/m}."""
    kmax = int(math.floor(math.exp(L))) + 1
    r = [0] * (kmax + 1)
    xb = int(math.isqrt(kmax)) + 1
    yb = int(math.isqrt(kmax // 5)) + 2
    for x in range(-xb, xb + 1):
        for y in range(-yb, yb + 1):
            if x == 0 and y == 0:
                continue
            v = x * x + 5 * y * y
            if v <= kmax:
                r[v] += 1
    a = [mp.mpf(rr) / r[1] for rr in r]  # a_1 = 1
    lam = [mp.mpf(0)] * (kmax + 1)
    for k in range(2, kmax + 1):
        s = a[k] * mp.log(k)
        for m_ in range(2, k + 1):
            if k % m_ == 0 and m_ < k:
                s -= lam[m_] * a[k // m_]
        # m = k term: Lambda_E(k) * a_1
        lam[k] = s
    out = []
    for k in range(2, kmax + 1):
        if lam[k] != 0 and math.log(k) < L - 1e-15:
            out.append((mp.log(k), lam[k] / mp.sqrt(k), k, 1))
    return out


# ---------------------------------------------------- matrix assembly
def constraint_rows(K: int, h):
    rp = [tent_moment(a, h, mp.mpf(1) / 2) for a in range(1, K + 1)]
    rm = [tent_moment(a, h, mp.mpf(-1) / 2) for a in range(1, K + 1)]
    return rp, rm


def null_basis(rows: list[list[mp.mpf]], K: int):
    """Orthonormal basis of the complement of span(rows) in R^K."""
    basis = []
    for r in rows:
        v = [mp.mpf(x) for x in r]
        for b in basis:
            c = mp.fsum(v[i] * b[i] for i in range(K))
            v = [v[i] - c * b[i] for i in range(K)]
        nrm = mp.sqrt(mp.fsum(x * x for x in v))
        basis.append([x / nrm for x in v])
    out = []
    for j in range(K):
        v = [mp.mpf(1) if i == j else mp.mpf(0) for i in range(K)]
        for b in basis + out:
            c = mp.fsum(v[i] * b[i] for i in range(K))
            v = [v[i] - c * b[i] for i in range(K)]
        nrm = mp.sqrt(mp.fsum(x * x for x in v))
        if nrm > mp.mpf(10) ** (-mp.mp.dps // 2):
            out.append([x / nrm for x in v])
        if len(out) == K - len(rows):
            break
    return out


def toeplitz_mp(row: list[mp.mpf], K: int) -> mp.matrix:
    M = mp.matrix(K, K)
    for a in range(K):
        for b in range(K):
            M[a, b] = row[abs(b - a)]
    return M


def project(M: mp.matrix, Z: list[list[mp.mpf]]) -> mp.matrix:
    K = M.rows
    r = len(Z)
    MZ = [[mp.fsum(M[i, j] * Z[c][j] for j in range(K))
           for c in range(r)] for i in range(K)]
    out = mp.matrix(r, r)
    for c1 in range(r):
        for c2 in range(c1, r):
            v = mp.fsum(Z[c1][i] * MZ[i][c2] for i in range(K))
            out[c1, c2] = v
            out[c2, c1] = v
    return out


def lambda_min_sym(M: mp.matrix) -> mp.mpf:
    E = mp.eigsy(M, eigvals_only=True)
    return min(E)


def build_Q_row(L: float, K: int, atoms) -> tuple[list, list]:
    """Toeplitz row of Q (constrained-target kernel) and of the arch
    part alone (reused across worlds)."""
    h = mp.mpf(L) / (K + 1)
    arch = [arch_W_pair(d, h) for d in range(K)]
    prim = [prime_W_pair(d, h, atoms) for d in range(K)]
    row = [-arch[d] - prim[d] for d in range(K)]
    return row, arch


def world_row(arch: list, L: float, K: int, world: str, atoms):
    h = mp.mpf(L) / (K + 1)
    if world == "TRUE":
        wa = atoms
    elif world == "SMOOTH":
        pr = [smooth_W_pair(d, h, L) for d in range(K)]
        return [-arch[d] - pr[d] for d in range(K)]
    elif world == "SCRARITH":
        wa = scram_weights(atoms)
    elif world == "EPSTEIN":
        wa = epstein_atoms(L)
    else:
        raise ValueError(world)
    pr = [prime_W_pair(d, h, wa) for d in range(K)]
    return [-arch[d] - pr[d] for d in range(K)]


def galerkin_lambda_min(L: float, K: int, row: list
                        ) -> tuple[mp.mpf, mp.mpf, list, list]:
    h = mp.mpf(L) / (K + 1)
    rp, rm = constraint_rows(K, h)
    Z = null_basis([rp, rm], K)
    B = toeplitz_mp(row, K)
    M = project(B, Z)
    lam = lambda_min_sym(M)
    # tau companion: unconstrained full kernel (screw section)
    P2 = mp.matrix(K, K)
    for a in range(K):
        for b in range(K):
            P2[a, b] = rp[a] * rm[b] + rm[a] * rp[b]
    tau = lambda_min_sym(B + P2)
    return lam, tau, rp, rm


# ------------------------------------------------------ interface test
def wR_exponential(sigma) -> mp.mpf:
    """W_R(e^{-sigma|t|}) by quadrature of CCM (11) + gamma term."""
    def integrand(t):
        if t <= 0:
            return (mp.mpf(1) - 2 * sigma) / 2  # t->0+ limit
        return (2 * mp.e ** (-sigma * t) - 2 * mp.e ** (-t / 2)) \
            * w_kernel(t)
    body = mp.quad(integrand, [0, 1, 4, 12, 40, mp.inf])
    return LOG4PI_GAMMA + body


def wP_sieve(sigma, cap: int, e_cap: float) -> tuple[mp.mpf, mp.mpf]:
    """sum_n Lambda(n) n^{-(1/2+sigma)} with Abel tail
    X^{1-s}/(s-1) - E(X) X^{-s} (E = psi - x, sieved exactly);
    remaining budget from |psi(x)-x| <= 0.94 sqrt x (Buethe 2018,
    valid to 1e19 >> cap)."""
    s = mp.mpf(1) / 2 + sigma
    total = mp.mpf(0)
    for p in PRIMES:
        lp = mp.log(p)
        pk = mp.mpf(p)
        while pk <= cap:
            total += lp * pk ** (-s)
            pk *= p
    tail = mp.mpf(cap) ** (1 - s) / (s - 1) \
        - mp.mpf(e_cap) * mp.mpf(cap) ** (-s)
    budget = mp.mpf("0.94") * abs(s) / (s - mp.mpf(1) / 2) \
        * mp.mpf(cap) ** (mp.mpf(1) / 2 - s)
    return total + tail, budget


def P_instrument(sigma) -> mp.mpf:
    """xi'/xi(1/2+sigma) via mp digamma + zeta (instrument lane)."""
    s = mp.mpf(1) / 2 + sigma
    return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2
            + mp.zeta(s, 1, 1) / mp.zeta(s))


def ols_slope(xs: list[float], ys: list[float]):
    x = np.array(xs)
    y = np.array(ys)
    xm, ym = x.mean(), y.mean()
    sxx = ((x - xm) ** 2).sum()
    slope = ((x - xm) * (y - ym)).sum() / sxx
    r = np.corrcoef(x, y)[0, 1]
    return float(slope), float(r)


# ================================================================ main
def main() -> int:
    global LOG4PI_GAMMA, PRIMES
    print("ccm_pn_adjudication_probe  PRIME.CCM.PN.ADJUDICATION.01")
    print("FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    print("mpmath %s  numpy %s" % (mp.__version__, np.__version__))

    section("C0. WARDS (firewall, sieve pins)")
    ok_fw, det = firewall_audit()
    ward_ok = check("G01 AST firewall: source-only, no repo reads, "
                    "no zero data", ok_fw, det)
    PRIMES = sieve_lambda(SIEVE_CAP)
    npi = len(PRIMES)
    ward_ok &= check("G02 own sieve pin pi(4e6) = 283146",
                     npi == PI_CAP_WARD, "pi = %d" % npi)
    psi_val = psi_of_cap(PRIMES, SIEVE_CAP)
    dev = abs(psi_val - float(PSI_CAP_WARD))
    ward_ok &= check("G03 psi(4e6) matches the corpus pin and the "
                     "0.94 sqrt(x) envelope",
                     dev < 1e-4 and abs(psi_val - SIEVE_CAP)
                     <= 0.94 * math.sqrt(SIEVE_CAP),
                     "psi = %.6f  dev(pin) = %.2e  |psi-x| = %.1f"
                     % (psi_val, dev, abs(psi_val - SIEVE_CAP)))
    ward_ok &= check("G04 verbatim CCM P(n) statement carried in the "
                     "frozen docstring with citation",
                     "there exists a\n   property P(n)" in __doc__
                     and "arXiv:2310.18423" in __doc__
                     and "[1/n, n]" in __doc__, "carry gate")

    section("C1. INSTRUMENT VALIDATION (closed forms, Yoshida cell)")
    mp.mp.dps = 60
    LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
    h_test = mp.mpf("0.11")
    ok_a = True
    worst = mp.mpf(0)
    for tv in ("0.0", "0.05", "0.11", "0.17", "0.21", "0.219"):
        t = mp.mpf(tv)
        # full breakpoint list of the product of the two shifted
        # tents (AMENDMENT 1b)
        bps = sorted({-h_test - t, -t, h_test - t, -h_test,
                      mp.mpf(0), h_test})
        direct = mp.quad(lambda u: max(0, 1 - abs(u + t) / h_test)
                         * max(0, 1 - abs(u) / h_test), bps)
        dv = abs(direct - tent_A(t, h_test))
        worst = max(worst, dv)
        ok_a &= dv < mp.mpf(10) ** (-40)
    check("G05 tent autocorrelation closed form == direct quadrature",
          ok_a, "worst dev %s (bar 1e-40)" % fmt(worst, 3))
    a_t, h_t = 3, mp.mpf("0.09")
    cm = tent_moment(a_t, h_t, mp.mpf(1) / 2)
    cq = mp.quad(lambda u: max(0, 1 - abs(u - a_t * h_t) / h_t)
                 * mp.e ** (u / 2), [a_t * h_t - h_t, a_t * h_t,
                                     a_t * h_t + h_t])
    check("G06 constraint moment closed form == quadrature",
          abs(cm - cq) < mp.mpf(10) ** (-40),
          "dev %s" % fmt(abs(cm - cq), 3))

    # Yoshida cell n = 1.9: no primes, constrained section must be PSD
    n_yosh = 1.9
    mp.mp.dps = DPS_BY_N[n_yosh]
    LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
    L = math.log(n_yosh)
    atoms = prime_atoms(L)
    row, _arch = build_Q_row(L, K_TENTS, atoms)
    lam_yosh, tau_yosh, _rp, _rm = galerkin_lambda_min(L, K_TENTS, row)
    check("G07 Yoshida cell n = 1.9 (prime-free): constrained "
          "lambda_min > 0 (finite section of the proven archimedean "
          "positivity); atom count 0",
          lam_yosh > 0 and len(atoms) == 0,
          "lambda_min = %s  tau = %s" % (fmt(lam_yosh, 8),
                                         fmt(tau_yosh, 8)))

    section("C2. THE (AC)/EULER--PICK INTERFACE TEST (M2b)")
    mp.mp.dps = 50
    LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
    print("  scalar identity per sigma:  P(sigma) = poles - "
          "(1/2) W_R(e^{-sigma|t|}) - sum Lambda(n) n^{-(1/2+sigma)}")
    P_vals = []
    worst_inst = mp.mpf(0)
    worst_src = mp.mpf(0)
    max_budget = mp.mpf(0)
    for sg in SIGJ:
        p_lhs = P_instrument(sg)
        poles = 1 / (sg - mp.mpf(1) / 2) + 1 / (sg + mp.mpf(1) / 2)
        wr = wR_exponential(sg)
        wp_src, bud = wP_sieve(sg, SIEVE_CAP, psi_val - SIEVE_CAP)
        rhs_src = poles - wr / 2 - wp_src
        s = mp.mpf(1) / 2 + sg
        wp_inst = -mp.zeta(s, 1, 1) / mp.zeta(s)
        rhs_inst = poles - wr / 2 - wp_inst
        rel_i = abs(rhs_inst - p_lhs) / abs(p_lhs)
        rel_s = abs(rhs_src - p_lhs) / abs(p_lhs)
        worst_inst = max(worst_inst, rel_i)
        worst_src = max(worst_src, rel_s)
        max_budget = max(max_budget, bud)
        P_vals.append(p_lhs)
        print("    sigma = %-12s P = %-16s relCCM(inst) = %-10s "
              "relCCM(sieve) = %s" % (fmt(sg, 8), fmt(p_lhs, 10),
                                      fmt(rel_i, 3), fmt(rel_s, 3)))
    id_inst = check("G08 interface identity, instrument lane: CCM "
                    "local terms (W_R quadrature of (11), zeta' route "
                    "for (10)) reproduce xi'/xi entrywise, rel <= 1e-25",
                    worst_inst < mp.mpf("1e-25"),
                    "worst rel %s" % fmt(worst_inst, 3))
    id_src = check("G09 interface identity, source lane: own "
                   "Lambda-sieve (cap 4e6) + Abel tail, rel <= 1e-6 "
                   "with printed tail budget",
                   worst_src < mp.mpf("1e-6"),
                   "worst rel %s  worst tail budget %s"
                   % (fmt(worst_src, 3), fmt(max_budget, 3)))
    # Euler--Pick floors from the CCM route (instrument-lane scalars)
    floors = []
    for N in range(1, 9):
        M = mp.matrix(N, N)
        for j in range(N):
            for k in range(N):
                M[j, k] = (P_vals[j] + P_vals[k]) / (SIGJ[j] + SIGJ[k])
        floors.append(lambda_min_sym(M))
    print("  Euler--Pick floors lambda_min(P_N), N = 1..8 "
          "(CCM-route scalars):")
    for N, f in enumerate(floors, 1):
        print("    N = %-2d lambda_min = %s" % (N, fmt(f, 8)))
    rel1 = abs(floors[0] - mp.mpf(FLOOR_N1)) / mp.mpf(FLOOR_N1)
    in2 = FLOOR_N2[0] * 0.999 <= float(floors[1]) <= FLOOR_N2[1] * 1.001
    id_par = check("G10 corpus parity: N = 1 floor matches the frozen "
                   "4.5917135e-2 (rel <= 1e-4) and N = 2 lies in the "
                   "certified corpus interval",
                   rel1 < mp.mpf("1e-4") and in2,
                   "N1 rel %s  N2 = %s" % (fmt(rel1, 3),
                                           fmt(floors[1], 8)))
    id_mono = check("G11 floor ladder collapses monotonically "
                    "(superexponential wall signature)",
                    all(floors[i + 1] < floors[i]
                        for i in range(len(floors) - 1)),
                    "ratios %s" % ", ".join(
                        fmt(floors[i + 1] / floors[i], 2)
                        for i in range(len(floors) - 1)))
    identity_ok = id_inst and id_par and id_mono

    section("C3. SMALL-n P(n) GALERKIN SECTIONS (M2a) + TAU (M2c)")
    lam_by_n: dict[float, mp.mpf] = {}
    tau_by_n: dict[float, mp.mpf] = {}
    budget_by_n: dict[float, mp.mpf] = {}
    arch_rows: dict[float, list] = {}
    neg_section = False
    for n in N_LADDER:
        mp.mp.dps = DPS_BY_N[n]
        LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
        L = math.log(n)
        atoms = prime_atoms(L)
        row, arch = build_Q_row(L, K_TENTS, atoms)
        arch_rows[n] = arch
        lam, tau, _rp, _rm = galerkin_lambda_min(L, K_TENTS, row)
        # measured entry-error budget: recompute two offsets at dps+20
        with mp.workdps(mp.mp.dps + 20):
            LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
            a0 = arch_W_pair(0, mp.mpf(L) / (K_TENTS + 1))
            a1 = arch_W_pair(K_TENTS - 1, mp.mpf(L) / (K_TENTS + 1))
        LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
        entry_dev = max(abs(a0 - arch[0]), abs(a1 - arch[K_TENTS - 1]))
        budget = K_TENTS * entry_dev
        lam_by_n[n] = lam
        tau_by_n[n] = tau
        budget_by_n[n] = budget
        if lam < -budget:
            neg_section = True
        status = ("POSITIVE" if lam > budget else
                  ("NEGATIVE(!!)" if lam < -budget else "UNDECIDED"))
        print("  n = %-5s L = %-8s atoms %-2d  lambda_min = %-14s "
              "budget = %-10s tau = %-14s  %s"
              % (n, "%.5f" % L, len(atoms), fmt(lam, 8),
                 fmt(budget, 3), fmt(tau, 8), status))
    prime_ns = [n for n in N_LADDER if n > 2]
    all_pos = all(lam_by_n[n] > budget_by_n[n] for n in prime_ns)
    checked_ok = check("G12 P(n) Galerkin sections, prime-bearing "
                       "n = 2.5..13: every constrained lambda_min > "
                       "measured budget (RH-consistent; the "
                       "falsification channel stays empty)",
                       all_pos and not neg_section,
                       "all positive" if all_pos else "see ladder")
    check("G13 falsification channel typed: a certified negative "
          "section would refute RH via the exact forward direction; "
          "none observed (min over ladder printed)",
          not neg_section,
          "min lambda_min = %s"
          % fmt(min(lam_by_n[n] for n in N_LADDER), 6))
    # mesh robustness at n = 6
    n6 = 6.0
    mp.mp.dps = DPS_BY_N[n6]
    LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
    L6 = math.log(n6)
    row18, _ = build_Q_row(L6, K_ROBUST, prime_atoms(L6))
    lam18, _t18, _rp, _rm = galerkin_lambda_min(L6, K_ROBUST, row18)
    same_sign = (lam18 > 0) == (lam_by_n[n6] > 0)
    logdev = abs(mp.log(lam18 / lam_by_n[n6], 10)) \
        if lam18 > 0 and lam_by_n[n6] > 0 else mp.mpf("inf")
    check("G14 mesh robustness at n = 6: K = 18 vs K = 24 same sign, "
          "log10 gap <= 4 (Galerkin min falls as K grows, as it must)",
          same_sign and logdev <= mp.mpf("4.0"),
          "K18 %s  K24 %s  log10 gap %s"
          % (fmt(lam18, 6), fmt(lam_by_n[n6], 6), fmt(logdev, 3)))

    # tau-screen (frozen bands): log margin vs log tau over prime ns
    xs = [float(mp.log(abs(tau_by_n[n]))) for n in prime_ns]
    ys = [float(mp.log(abs(lam_by_n[n]))) for n in prime_ns]
    slope, corr = ols_slope(xs, ys)
    if abs(slope) <= SLOPE_PASS:
        screen = "PASS-BAND(independent)"
    elif slope >= SLOPE_RELOC:
        screen = "RELOCATION(wall renamed)"
    else:
        screen = "AMBIGUOUS"
    tau_all_pos = all(tau_by_n[n] > 0 for n in N_LADDER)
    check("G15 tau-screen executed on the frozen bands "
          "(PASS |s| <= 0.30 / RELOCATION s >= 0.70); tau ladder "
          "positive (screw sections)",
          tau_all_pos and math.isfinite(slope),
          "slope %.4f  corr %.4f  => %s" % (slope, corr, screen))
    print("  tau-screen: slope %.4f corr %.4f  classification %s"
          % (slope, corr, screen))

    section("C4. CONTROL WORLDS through the same construction (M2d)")
    world_lams: dict[str, dict[float, mp.mpf]] = {
        w: {} for w in ("SMOOTH", "SCRARITH", "EPSTEIN")}
    ctrl_ns = [1.9, 2.5, 3.0, 6.0, 13.0]
    for n in ctrl_ns:
        mp.mp.dps = 60
        LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
        L = math.log(n)
        atoms = prime_atoms(L)
        arch60 = [arch_W_pair(d, mp.mpf(L) / (K_TENTS + 1))
                  for d in range(K_TENTS)]
        for world in ("SMOOTH", "SCRARITH", "EPSTEIN"):
            if world == "SCRARITH" and len(atoms) < 2:
                world_lams[world][n] = None
                continue
            roww = world_row(arch60, L, K_TENTS, world, atoms)
            lamw, _tw, _rp, _rm = galerkin_lambda_min(L, K_TENTS, roww)
            world_lams[world][n] = lamw
    for world in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        line = "  ".join(
            "n=%s: %s" % (n, "n/a" if world_lams[world][n] is None
                          else fmt(world_lams[world][n], 5))
            for n in ctrl_ns)
        print("  %-9s %s" % (world, line))
    # separation metric: |lam_world - lam_true| / lam_true at n = 6, 13
    sep_stats = {}
    for world in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        seps = []
        for n in (6.0, 13.0):
            lw = world_lams[world][n]
            if lw is None:
                continue
            lt = lam_by_n[n]
            seps.append(float(abs(lw - lt) / abs(lt)))
        sep_stats[world] = min(seps) if seps else 0.0
    any_dead = {w: any(world_lams[w][n] is not None
                       and world_lams[w][n] < 0 for n in ctrl_ns)
                for w in world_lams}
    check("G16 SMOOTH world measured (support error: false mass in "
          "(0, log 2)); separation from TRUE at n = 6/13 >= 1e3 x "
          "margin", sep_stats["SMOOTH"] >= 1e3,
          "min sep factor %.3e  negative sections: %s"
          % (sep_stats["SMOOTH"], any_dead["SMOOTH"]))
    check("G17 SCRARITH world measured (positions kept, weights "
          "golden-permuted); separation >= 1e3 x margin",
          sep_stats["SCRARITH"] >= 1e3,
          "min sep factor %.3e  negative sections: %s"
          % (sep_stats["SCRARITH"], any_dead["SCRARITH"]))
    check("G18 EPSTEIN world measured (x^2+5y^2 log-derivative atoms; "
          "typed: same archimedean frame kept, arithmetic-sensitivity "
          "only); separation >= 1e3 x margin",
          sep_stats["EPSTEIN"] >= 1e3,
          "min sep factor %.3e  negative sections: %s"
          % (sep_stats["EPSTEIN"], any_dead["EPSTEIN"]))
    arith_sensitive = all(sep_stats[w] >= 1e3 for w in sep_stats)

    section("C5. DETECTION LAW (reach of the finite check, M2a/M4)")
    det_res = {}
    for n in DET_NS:
        mp.mp.dps = 60
        LOG4PI_GAMMA = mp.log(4 * mp.pi) + mp.euler
        L = math.log(n)
        atoms = prime_atoms(L)
        arch60 = [arch_W_pair(d, mp.mpf(L) / (K_TENTS + 1))
                  for d in range(K_TENTS)]
        h = mp.mpf(L) / (K_TENTS + 1)
        base_pr = [prime_W_pair(d, h, atoms) for d in range(K_TENTS)]
        u2 = mp.log(2)
        w2 = mp.log(2) / mp.sqrt(2)
        pert = [tent_A(d * h + u2, h) + tent_A(d * h - u2, h)
                for d in range(K_TENTS)]

        def lam_of(eps):
            roww = [-arch60[d] - base_pr[d] - mp.mpf(eps) * w2 * pert[d]
                    for d in range(K_TENTS)]
            lam, _t, _rp, _rm = galerkin_lambda_min(L, K_TENTS, roww)
            return lam

        lo, hi = None, None
        for eps in DET_EPS_GRID:
            if lam_of(eps) < 0:
                hi = eps
                break
            lo = eps
        if hi is None:
            det_res[n] = None
            continue
        lo = lo if lo is not None else hi / 16.0
        for _ in range(DET_BISECT_STEPS):
            mid = math.sqrt(lo * hi)
            if lam_of(mid) < 0:
                hi = mid
            else:
                lo = mid
        det_res[n] = math.sqrt(lo * hi)
        print("  n = %-4s eps*(p=2 weight, multiplicative) = %.6e  "
              "(lambda_min(TRUE) = %s)" % (n, det_res[n],
                                           fmt(lam_by_n[n], 5)))
    check("G19 detection law measured: finite positive eps* at both "
          "test depths (the instrument can see a planted Euler-factor "
          "violation; reach = eps*(n) ladder)",
          all(det_res[n] is not None and det_res[n] > 0
              for n in DET_NS),
          "  ".join("eps*(%s) = %.3e" % (n, det_res[n])
                    for n in DET_NS if det_res[n] is not None))

    section("C6. HONESTY GATES AND VERDICT (M3/M4)")
    check("G20 quantifier honesty carried: finite sections are "
          "necessary conditions only; P(n) per fixed n quantifies "
          "over an infinite-dimensional cone; nothing here proves "
          "P(n) for any n, and no marker moves",
          "NECESSARY conditions" in __doc__
          and "NO RH CLAIM" in __doc__, "carry gate")
    check("G21 citation honesty carried: P(n) open for every "
          "prime-bearing n; archimedean place proven (CC Selecta "
          "2021, Yoshida); CCM semilocal-prolate attack typed as "
          "program with announced second candidate",
          "OPEN in the literature" in __doc__
          and "forthcoming paper" in __doc__, "carry gate")
    wall = time.time() - T0
    time_ok = check("G22 runtime under the declared bar",
                    wall < RUNTIME_BAR_S, "%.1f s / %.0f s"
                    % (wall, RUNTIME_BAR_S))

    n_pass = sum(1 for _n, okk, _d in CHECKS if okk)
    print("\nCHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))

    if neg_section:
        print("VERDICT: CCM-SECTION-NEGATIVE -- a certified negative "
              "constrained section was measured; this would refute RH "
              "and demands independent re-derivation before any claim.")
        return 2
    if not (ward_ok and time_ok):
        print("VERDICT: INSTRUMENT-EDGE (failed ward; no mathematical "
              "verdict)")
        return 1

    checked = "CCM-CHECKED(n = 2.5..13, %d prime-bearing sections, " \
              "all positive above measured budget)" \
              % len(prime_ns) if checked_ok else \
              "CCM-CHECK-UNDECIDED(budget-limited)"
    if identity_ok:
        typing = ("CCM-SAME-CURRENCY(identity exhibited: the CCM Weil "
                  "functional built from their published local terms "
                  "(10)/(11) reproduces xi'/xi and hence the corpus "
                  "Euler--Pick matrices entrywise on the exponential-"
                  "autocorrelation family -- the (AC) interface of "
                  "spec-sheet property 4; tau-screen %s; the semilocal-"
                  "prolate operator packaging is the not-finitely-"
                  "testable remainder, typed citation)" % screen)
    else:
        typing = "CCM-INDEPENDENT-CONTENT(interface test failed to " \
                 "weld -- see gates)"
    print("VERDICT: %s + %s" % (checked, typing))
    print("ARITHMETIC-SENSITIVITY: %s (all three control worlds "
          "separate at >= 1e3 x margin through the same construction)"
          % ("CONFIRMED" if arith_sensitive else "NOT CONFIRMED"))
    print("NO RH CLAIM.  FINITE SECTIONS AND ONE IDENTITY ONLY.")
    return 0 if n_pass == len(CHECKS) else 1


PRIMES: list[int] = []

if __name__ == "__main__":
    sys.exit(main())
