#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mangoldt_incidence_probe -- PRIME.RELATION.MANGOLDT.01
(EXPLORATION ONLY, experiments/; module 4 of the 2026-08-07 evening
code-complex: the VON MANGOLDT COMMUTATOR THEOREM -- Lambda as the
commutator of the divisibility operator, verified exactly, powered,
generalized along the four-comb discipline, and bridged to the
deployed relational carrier of PRIME.RELATION.MULT.01).

THE THEOREM (verify exactly, then generalize): for 1 <= a, b <= N
with the divisibility incidence Z_{a,b} = 1_{a|b} (unitriangular,
det 1), its integer inverse M = Z^{-1} = [1_{a|b} mu(b/a)], and
D = diag(log 1, ..., log N):

    L_N := -M [D, Z]     has entries    (L_N)_{a,b} = Lambda(b/a)

for a | b and 0 otherwise (Lambda(1) = 0 covers a = b).  The one-line
proof IS the Moebius-log identity: (M[D,Z])_{a,an} = sum_{e|n} mu(e)
(log(ae) - log(an)) = sum_{e|n} mu(e)(log e - log n) = -Lambda(n):
the generic log a cancels TERMWISE, and the classical pair
sum_{e|n} mu(e) log e = -Lambda(n), sum_{e|n} mu(e) = delta_{n,1}
finishes.  This is classical incidence-algebra arithmetic (mu * log
= Lambda in matrix clothes) -- typed as such, NOT claimed as new
mathematics.  The probe's content is the exact operator packaging:

  S1  the exact verification -- sympy entrywise at N = 60 in the
      formal log-prime basis (log n = sum_p v_p(n) L_p: exact
      "log-integers") AND with literal sympy.log; the one-line proof
      reproduced as exact algebra (generic symbol for log a, termwise
      cancellation); the exact integer layer at N = 360 (M Z = I and
      the per-prime commutator [V_p, Z] = -Z E_p, which IS Chebyshev
      1 * Lambda = log prime by prime); the float ward at N = 10^4.
  S2  the power/chain formula (L^k)_{a,b} = sum over ordered
      factorization chains b/a = r_1 ... r_k (prime powers) of
      prod_j Lambda(r_j), k = 2, 3 exact vs independent enumeration;
      nilpotency L^k = 0 for 2^k > N; the log: W := log Z =
      sum (-1)^{k+1} (Z - I)^k / k is RATIONAL with entries 1/k at
      ratio p^k (Lambda with the log stripped), exp(W) = Z exactly,
      and L = [W, D] = -[D, log Z] EXACTLY -- the BCH series for
      -Z^{-1}[D,Z] truncates because [W, [W, D]] = 0; the Chebyshev
      operator identity [D, Z] = -Z L; the semigroup anchor
      Z^2 = T(d).
  S3  the four-comb discipline at operator level: TRUE zeta / the
      chi4 twist (Z^chi = T(chi4): the commutator produces the
      twisted Lambda_chi = chi4 * Lambda -- Selberg-class-correct) /
      zeta_{Q(i)} at the IDEAL level (Z[i] ideal poset, norm <= 300,
      canonical generators x >= 1, y >= 0: the commutator produces
      ITS Lambda_K, and the norm-aggregation equals (1 + chi4)
      Lambda) / the EPSTEIN h = 2 form x^2 + 5y^2: the operator
      identity itself STILL holds (T is an algebra iso from Dirichlet
      convolution -- the machine never breaks) but the produced
      Lambda_A is NOT a consistent von Mangoldt function: its support
      LEAKS off the prime powers exactly at the class-group
      obstruction (first site 6 = 2 x 3, first UNRAMIFIED site
      21 = 3 x 7), the h = 2 class-convolution law
      a_A(mk) = a_A(m) a_A(k) + a_B(m) a_B(k) is verified exactly,
      and the class-average a_A + a_B = 1 * chi_{-20} REPAIRS the
      Euler product (off-prime-power support empty): the defect is
      exactly the class group.
  S4  the bridge: the deployed relational carrier's Moebius-pairing
      reconstruction sum_{d|m} mu(d) U(m/d) at true positions is
      LITERALLY the first row of L_N (per-divisor term equality);
      the pairing matrix B[k,j] = mu(m_k/m_j) on the deployed comb
      support (prime powers in [2, 256]) is a sub-block of Z^{-1};
      every row of L is the first row on the shifted sub-poset; the
      higher rows/powers are the untapped structure -- (L^k)_{1,n}
      enumerates ordered factorization chains, and the second
      Selberg function obeys T(mu * log^2) = L^2 - [D, L] exactly.

HONESTY: NO RH claim.  EXPLORATION ONLY: writes nothing, commits
nothing, nothing outside experiments/.  Firewall: no zeta zeros, no
prime-table symbols (own sieves; AST-checked).  The context probe
multiplicative_relation_probe.py is read-only context; its Moebius-
pairing design and measured support ward are re-declared here.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mangoldt_incidence_probe.py
"""

import ast
import hashlib
import math
import os
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sps
import sympy as sp

FROZEN_SPEC = """\
PRIME.RELATION.MANGOLDT.01 spec v1 (2026-08-07, frozen before the
run).  THE THEOREM on {1..N}: Z = [1_{a|b}], M = Z^{-1} =
[mu(b/a) 1_{a|b}], D = diag(log a); L_N := -M[D,Z] == T(Lambda)
(entries Lambda(b/a) on a|b, else 0).  NO RH claim; classical
incidence-algebra content, verified as exact operator algebra, then
generalized and bridged.
S1 EXACT VERIFICATION: (a) sympy entrywise at N_SYM = 60 -- formal
log-prime basis (log n = sum v_p(n) L_p, exact log-integers) over
ALL 60^2 pairs, plus literal sympy.log with expand_log(force) on all
divisor pairs; (b) the one-line proof as exact algebra: matrix
entries == sum_{e|n} mu(e)(log(ae) - log(an)) for all (a, n) with
an <= 60; generic-La termwise cancellation for all n <= 60;
sum_{e|n} mu(e) log e == -Lambda(n) and sum_{e|n} mu(e) ==
delta_{n,1}; (c) exact integer layer at N_INT = 360: M Z == I,
per-prime [V_p, Z] == -Z E_p for ALL primes p <= 360 (V_p = diag
v_p, E_p = indicator of p-power ratio; Chebyshev 1*Lambda = log per
prime), and -M[D,Z] == T(Lambda) entrywise in the log-p module
(Fractions); (d) float ward at N_FLT = 10^4 (scipy sparse):
max |M[D,Z] + T(Lambda)| <= BAR_FLT = 1e-8.
S2 POWERS / NILPOTENCY / LOG: (L^k)_{a,b} == sum over ordered chains
b/a = r_1...r_k (prime powers >= 2) of prod Lambda(r_j), exact sympy
at N_SYM for k = 2, 3 vs independent chain enumeration; nilpotency:
L^6 == 0 at N_SYM with L^5 != 0 and (L^5)_{1,32} == L2^5; at N_FLT
nnz(L^13) == 1 (single entry (1, 8192) == (log 2)^13 to rel 1e-9)
and nnz(L^14) == 0 (2^14 > 10^4).  THE LOG: W := log Z =
sum_{k>=1} (-1)^{k+1} (Z-I)^k / k is RATIONAL: entries 1/k at ratio
p^k, 0 else (kappa = Lambda/log); (Z-I)^9 == 0 at N_INT; exp(W) == Z
exact (Fractions); L == [W, D] == -[D, log Z] EXACTLY, and
[W, [W, D]] == 0 (so the BCH series of -Z^{-1}[D, Z] truncates at
its first term: the sign-fixed relationship is L = -Z^{-1}[D,Z] =
-[D, log Z]); [L, Z] == 0 and [L, W] == 0; Chebyshev operator form
[D, Z] == -(Z L) == -(L Z); semigroup anchor Z^2 == T(d), d = 1*1.
S3 FOUR-COMB OPERATOR TABLE (exact; scalar Lambda_f by the frozen
recursion Lambda_f(n) = f(n) log n - sum_{d|n, 1<d<n} Lambda_f(d)
f(n/d), all n <= 360; T(f) is an algebra iso, so the commutator
ALWAYS produces T(Lambda_f); Selberg-consistency criterion = support
of Lambda_f inside the prime powers): (a) TRUE f = 1: Lambda_f ==
Lambda exactly, off-pp support EMPTY; (b) chi4 TWIST f = chi4 (the
twisted incidence Z^chi = T(chi4)): M^chi Z^chi == I,
-M^chi[D, Z^chi] == T(chi4 Lambda) exact, off-pp EMPTY,
Lambda_f == chi4 * Lambda pointwise; (c) zeta_{Q(i)} at IDEAL level:
ideals of Z[i] with norm <= NK = 300, canonical generators x >= 1,
y >= 0, poset = ideal divisibility, D_K = diag(log N); own Gaussian
factorization; ward #ideals(norm n) == r2(n)/4; M_K == [mu_K] with
M_K Z_K == I; -M_K[D_K, Z_K] == T(Lambda_K) exact (Lambda_K =
log N(P) on prime-ideal powers); norm aggregation
sum_{N(A)=n} Lambda_K(A) == (1 + chi4(n)) Lambda(n) for all
n <= 300; scalar comb f = r2/4 == 1 * chi4 (ward), off-pp EMPTY,
Lambda_f == (1 + chi4) Lambda; functoriality T(1) T(chi4) ==
T(r2/4) and L_{r2/4} == L_zeta + L_chi (the log-derivative is
additive over the always-commuting Dirichlet product); (d) EPSTEIN
h = 2, f = a_A = r_{x^2+5y^2}/2 (own double loop; a_A(1) = 1):
M_A Z_A == I and -M_A[D, Z_A] == T(Lambda_A) STILL hold (the
operator identity never breaks) but Lambda_A LEAKS off the prime
powers: first three sites == [6, 14, 21], min site coprime to 10 ==
21 (= 3 x 7: the unramified class-group obstruction; 6 = 2 x 3 and
14 = 2 x 7 involve the ramified prime 2), exact values
Lambda_A(6) == 2 log 6, Lambda_A(14) == 2 log 14, Lambda_A(21) ==
4 log 21; prime-power values may differ from zeta's (Lambda_A(4) ==
2 log 2, Lambda_A(9) == 6 log 3: own Euler factors at good local
slots -- NOT the discriminator); the h = 2 CLASS-CONVOLUTION LAW
a_A(mk) == a_A(m) a_A(k) + a_B(m) a_B(k) AND a_B(mk) ==
a_A(m) a_B(k) + a_B(m) a_A(k) for ALL coprime pairs with mk <= 360
(a_B = r_{2x^2+2xy+3y^2}/2, a_B(1) = 0: the class-B comb is not
unital -- only the principal class gives an invertible incidence
operator); the CLASS-AVERAGE REPAIR b = a_A + a_B == 1 * chi_{-20}
(Kronecker character, own Euler criterion) with off-pp support
EMPTY: the leak is exactly the class group.
S4 THE BRIDGE to the deployed relational carrier (PRIME.RELATION.
MULT.01, read-only context): (a) the Moebius-pairing reconstruction
Lambdahat(m) = sum_{d|m} mu(d) U(m/d) at TRUE positions U = log is
LITERALLY the first row of L_N: per-divisor term equality
mu(d) log(m/d) == -M_{1,d} [D,Z]_{d,m} for EVERY d | m <= 360, and
the sums == L[1, m]; (b) the pairing matrix B[k, j] = mu(m_k/m_j)
on the deployed comb support (prime powers in [2, 256] plus the
unit, the context probe's measured support ward) == the sub-block
of M = Z^{-1}; (c) row self-similarity L[a, ab] == L[1, b] for all
ab <= 360 (every row is the first row on the shifted sub-poset);
(d) the untapped structure: (L^k)_{1,n} = ordered k-chain
correlations (S2), and the second Selberg function: scalar
mu * log^2 == Lambda log + Lambda*Lambda for all n <= 60 AND
operator T(mu * log^2) == L^2 - [D, L] entrywise at N_SYM.
BUDGETS: BAR_FLT = 1e-8; nilpotent-entry relative bar 1e-9; runtime
<= 20 min.  FIREWALL: no zeta zeros, no prime-table symbols (own
sieves, AST-checked), no target data, writes nothing, nothing
outside experiments/.  VERDICTS (frozen): MANGOLDT-COMMUTATOR-EXACT
(S1, S2, S3, S4 all pass as frozen) / MANGOLDT-COMMUTATOR-PARTIAL
(S1 passes, a later section fails -- typed where) / FAIL (S1
fails).  NO RH claim.
"""

N_SYM = 60
N_INT = 360
N_FLT = 10_000
NK = 300
X_SUPPORT = 256
BAR_FLT = 1.0e-8
BAR_REL = 1.0e-9
RUNTIME_BUDGET_S = 1200.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


# ===================================================== arithmetic layer
SPF = None      # smallest prime factor, own sieve
MU = None       # Moebius
ISPP = None     # prime-power indicator (n >= 2)
PPRIME = None   # the prime p for prime powers, else 0
CHI4 = None     # chi4(n)
DIVS = None     # divisor lists up to N_INT
LOGD = None     # exact log n in the log-p basis: {p: Fr(v_p(n))}
LAMLD = None    # exact Lambda(n) logdict: {p: Fr(1)} on prime powers


def sieve_spf(n_max):
    spf = np.zeros(n_max + 1, dtype=np.int64)
    for p in range(2, n_max + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    return spf


def factorize(n):
    out = {}
    while n > 1:
        p = int(SPF[n])
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        out[p] = k
    return out


def build_arithmetic():
    global SPF, MU, ISPP, PPRIME, CHI4, DIVS, LOGD, LAMLD
    SPF = sieve_spf(N_FLT)
    MU = np.zeros(N_FLT + 1, dtype=np.int64)
    MU[1] = 1
    ISPP = np.zeros(N_FLT + 1, dtype=bool)
    PPRIME = np.zeros(N_FLT + 1, dtype=np.int64)
    CHI4 = np.zeros(N_FLT + 1, dtype=np.int64)
    for n in range(2, N_FLT + 1):
        f = factorize(n)
        MU[n] = 0 if any(k > 1 for k in f.values()) else (-1) ** len(f)
        if len(f) == 1:
            ISPP[n] = True
            PPRIME[n] = next(iter(f))
    for n in range(1, N_FLT + 1):
        if n % 2 == 1:
            CHI4[n] = 1 if n % 4 == 1 else -1
    DIVS = {n: [] for n in range(1, N_INT + 1)}
    for d in range(1, N_INT + 1):
        for m in range(d, N_INT + 1, d):
            DIVS[m].append(d)
    LOGD = {1: {}}
    for n in range(2, N_INT + 1):
        LOGD[n] = {p: Fr(k) for p, k in factorize(n).items()}
    LAMLD = {n: ({int(PPRIME[n]): Fr(1)} if ISPP[n] else {})
             for n in range(1, N_INT + 1)}
    LAMLD[1] = {}


# ---------------------------------------------- exact log-p dict values
def ld_clean(v):
    return {p: c for p, c in v.items() if c != 0}


def ld_axpy(acc, s, v):
    for p, c in v.items():
        acc[p] = acc.get(p, Fr(0)) + s * c
    return acc


def ld_scale(v, s):
    return {} if s == 0 else {p: s * c for p, c in v.items()}


def ld_eq(u, v):
    return ld_clean(u) == ld_clean(v)


def ld_norm1(v):
    return sum(abs(c) for c in v.values())


def ld_str(v):
    v = ld_clean(v)
    if not v:
        return "0"
    return " + ".join("%s*log%d" % (c, p) for p, c in sorted(v.items()))


# --------------------------------------- sparse matrices (dict keyed ij)
def mm(A, B, expand=False):
    """Scalar sparse product (values: int / Fraction / sympy)."""
    rows = {}
    for (c, b), v in B.items():
        rows.setdefault(c, []).append((b, v))
    out = {}
    for (a, c), u in A.items():
        lst = rows.get(c)
        if not lst:
            continue
        for b, v in lst:
            k = (a, b)
            out[k] = out.get(k, 0) + u * v
    res = {}
    for k, v in out.items():
        if expand:
            v = sp.expand(v)
        if v != 0:
            res[k] = v
    return res


def mmL(A, B):
    """A scalar-valued, B logdict-valued."""
    rows = {}
    for (c, b), v in B.items():
        rows.setdefault(c, []).append((b, v))
    out = {}
    for (a, c), u in A.items():
        lst = rows.get(c)
        if not lst:
            continue
        for b, v in lst:
            ld_axpy(out.setdefault((a, b), {}), u, v)
    return {k: w for k, w in ((k, ld_clean(v)) for k, v in out.items())
            if w}


def mmLs(A, B):
    """A logdict-valued, B scalar-valued."""
    rows = {}
    for (c, b), v in B.items():
        rows.setdefault(c, []).append((b, v))
    out = {}
    for (a, c), u in A.items():
        lst = rows.get(c)
        if not lst:
            continue
        for b, v in lst:
            ld_axpy(out.setdefault((a, b), {}), v, u)
    return {k: w for k, w in ((k, ld_clean(v)) for k, v in out.items())
            if w}


def mat_eq(A, B):
    for k in set(A) | set(B):
        if A.get(k, 0) != B.get(k, 0):
            return False, k
    return True, None


def mat_eq_ld(A, B):
    for k in set(A) | set(B):
        if not ld_eq(A.get(k, {}), B.get(k, {})):
            return False, k
    return True, None


def mat_neg_ld(A):
    return {k: ld_scale(v, -1) for k, v in A.items()}


def mat_add_ld(A, B):
    out = {}
    for k in set(A) | set(B):
        acc = dict(A.get(k, {}))
        ld_axpy(acc, 1, B.get(k, {}))
        acc = ld_clean(acc)
        if acc:
            out[k] = acc
    return out


# ------------------------------------------- incidence-operator builders
def build_Z(n_top, f=None):
    """T(f): entries f(b/a) on divisor pairs a | b (f defaults to 1)."""
    Z = {}
    for a in range(1, n_top + 1):
        for b in range(a, n_top + 1, a):
            v = 1 if f is None else f[b // a]
            if v != 0:
                Z[(a, b)] = v
    return Z


def build_commDZ(n_top, f=None):
    """[D, T(f)]: entries (log a - log b) f(b/a) = -log(b/a) f(b/a)."""
    C = {}
    for a in range(1, n_top + 1):
        for b in range(2 * a, n_top + 1, a):
            v = 1 if f is None else f[b // a]
            if v != 0:
                C[(a, b)] = ld_scale(LOGD[b // a], -v)
    return C


def build_TLam(n_top, lam):
    """T(Lambda_f) from a logdict array lam[n]."""
    out = {}
    for a in range(1, n_top + 1):
        for b in range(2 * a, n_top + 1, a):
            v = lam[b // a]
            if v:
                out[(a, b)] = v
    return out


def dirichlet_inverse(a, n_top):
    b = [0] * (n_top + 1)
    assert a[1] == 1
    b[1] = 1
    for n in range(2, n_top + 1):
        s = 0
        for d in DIVS[n]:
            if d < n and b[d] != 0 and a[n // d] != 0:
                s += b[d] * a[n // d]
        b[n] = -s
    return b


def dirichlet_conv(a, b, n_top):
    c = [0] * (n_top + 1)
    for n in range(1, n_top + 1):
        s = 0
        for d in DIVS[n]:
            s += a[d] * b[n // d]
        c[n] = s
    return c


def lambda_of_comb(a, n_top):
    """Frozen recursion Lambda_f(n) = a(n) log n
       - sum_{d|n, 1<d<n} Lambda_f(d) a(n/d); logdict values."""
    G = {1: {}}
    for n in range(2, n_top + 1):
        acc = {}
        if a[n] != 0:
            ld_axpy(acc, Fr(a[n]), LOGD[n])
        for d in DIVS[n]:
            if 1 < d < n and G[d] and a[n // d] != 0:
                ld_axpy(acc, -Fr(a[n // d]), G[d])
        G[n] = ld_clean(acc)
    return G


# ================================================= S1 exact verification
def s1_exact():
    section("S1 -- THE EXACT VERIFICATION: L_N = -M[D,Z] == T(Lambda)")
    ok_all = True

    # S1.1 arithmetic wards
    mu_ok = all(sum(int(MU[d]) for d in DIVS[n]) == (1 if n == 1 else 0)
                for n in range(1, N_INT + 1))
    lam_ok = True
    for n in range(2, N_INT + 1):
        acc = {}
        for d in DIVS[n]:
            if MU[d]:
                ld_axpy(acc, Fr(int(MU[d])), LOGD[n // d])
        lam_ok &= ld_eq(acc, LAMLD[n])
    ok_all &= check("S1.1 [EXACT] arithmetic wards on own sieves: "
                    "(mu * 1)(n) == delta_1 and (mu * log)(n) == "
                    "Lambda(n) in the log-p basis for ALL n <= %d"
                    % N_INT, mu_ok and lam_ok)

    # S1.2 sympy, formal log-prime basis, entrywise at N_SYM
    primes60 = [p for p in range(2, N_SYM + 1) if ISPP[p] and p == PPRIME[p]]
    LS = {p: sp.Symbol("L%d" % p) for p in primes60}

    def lsym(n):
        return sp.Add(*[int(k) * LS[p] for p, k in LOGD[n].items()])

    Z60 = build_Z(N_SYM)
    M60 = {(a, b): int(MU[b // a]) for (a, b) in Z60
           if MU[b // a] != 0}
    C60 = {}
    for (a, b) in Z60:
        if a != b:
            C60[(a, b)] = lsym(a) - lsym(b)
    L60 = {k: sp.expand(-v) for k, v in mm(M60, C60, expand=True).items()}
    exp60 = {}
    for (a, b) in Z60:
        r = b // a
        if ISPP[r]:
            exp60[(a, b)] = LS[int(PPRIME[r])]
    ok_ent = True
    n_pairs = 0
    for a in range(1, N_SYM + 1):
        for b in range(1, N_SYM + 1):
            got = L60.get((a, b), sp.Integer(0))
            want = exp60.get((a, b), sp.Integer(0))
            if b % a == 0:
                n_pairs += 1
            if sp.expand(got - want) != 0:
                ok_ent = False
    ok_all &= check("S1.2 [EXACT -- sympy, log-integer basis] "
                    "(-M[D,Z])_{a,b} == Lambda(b/a) entrywise for ALL "
                    "%d^2 pairs (%d divisor pairs) at N = %d"
                    % (N_SYM, n_pairs, N_SYM), ok_ent)
    print("      sample exact entries: L[2,24] = %s (= Lambda(12)),  "
          "L[3,24] = %s (= Lambda(8)),  L[1,32] = %s (= Lambda(32))"
          % (sp.expand(L60.get((2, 24), sp.Integer(0))),
             L60.get((3, 24), 0), L60.get((1, 32), 0)))

    # S1.3 sympy, literal logs (own log-integer rewrite, no
    # dependence on expand_log internals)
    logsubs = {}
    for m in range(2, N_SYM + 1):
        f = factorize(m)
        if not (len(f) == 1 and next(iter(f.values())) == 1):
            logsubs[sp.log(m)] = sp.Add(*[k * sp.log(p)
                                          for p, k in f.items()])
    ok_lit = True
    for (a, b) in Z60:
        if a == b:
            continue
        r = b // a
        expr = sp.Integer(0)
        for c in range(a, b + 1, a):
            if b % c == 0 and MU[c // a] != 0:
                expr += int(MU[c // a]) * (sp.log(c) - sp.log(b))
        want = sp.log(int(PPRIME[r])) if ISPP[r] else sp.Integer(0)
        diff = sp.expand((-expr - want).xreplace(logsubs))
        if diff != 0:
            ok_lit = False
    ok_all &= check("S1.3 [EXACT -- sympy, literal logs] the same "
                    "identity with sympy.log integers, rewritten to "
                    "the log-prime basis by own factorization, on "
                    "all divisor pairs at N = %d" % N_SYM, ok_lit)

    # S1.4 the one-line proof as exact algebra
    ok_match = True
    for a in range(1, N_SYM + 1):
        for n in range(1, N_SYM // a + 1):
            ssum = sp.Integer(0)
            for e in DIVS[n]:
                if MU[e]:
                    ssum += int(MU[e]) * (lsym(a * e) - lsym(a * n))
            mdz = -L60.get((a, a * n), sp.Integer(0))
            if sp.expand(ssum - mdz) != 0:
                ok_match = False
    La = sp.Symbol("La")
    ok_generic = True
    ok_classic = True
    for n in range(1, N_SYM + 1):
        terms = []
        for e in DIVS[n]:
            if MU[e]:
                t = sp.expand(int(MU[e]) * ((La + lsym(e))
                                            - (La + lsym(n))))
                if t.has(La):
                    ok_generic = False
                terms.append(t)
        total = sp.expand(sp.Add(*terms))
        lam_n = (LS[int(PPRIME[n])] if (n > 1 and ISPP[n])
                 else sp.Integer(0))
        if sp.expand(total + lam_n) != 0:
            ok_generic = False
        s_mulog = sp.expand(sp.Add(*[int(MU[e]) * lsym(e)
                                     for e in DIVS[n] if MU[e]]))
        s_mu = sum(int(MU[e]) for e in DIVS[n])
        if sp.expand(s_mulog + lam_n) != 0 or s_mu != (1 if n == 1
                                                       else 0):
            ok_classic = False
    ok_all &= check("S1.4 [EXACT -- THE ONE-LINE PROOF] (M[D,Z])_{a,an} "
                    "== sum_{e|n} mu(e)(log(ae) - log(an)) for all "
                    "an <= %d; with GENERIC symbol La = log a the "
                    "cancellation is TERMWISE and the sum == -Lambda(n) "
                    "for all n; the classical pair sum mu(e) log e == "
                    "-Lambda(n), sum mu(e) == delta_{n,1}" % N_SYM,
                    ok_match and ok_generic and ok_classic)

    # S1.5 / S1.6 / S1.7 exact integer layer at N_INT
    Z = build_Z(N_INT)
    M = {(a, b): int(MU[b // a]) for (a, b) in Z if MU[b // a] != 0}
    ident = {(a, a): 1 for a in range(1, N_INT + 1)}
    okI, bad = mat_eq(mm(M, Z), ident)
    ok_all &= check("S1.5 [EXACT] M Z == I at N = %d (M = [mu(b/a)] is "
                    "the integer inverse of the unitriangular Z)"
                    % N_INT, okI, "" if okI else "first bad %s" % (bad,))

    primes360 = [p for p in range(2, N_INT + 1)
                 if ISPP[p] and p == PPRIME[p]]
    ok_cheb = True
    for p in primes360:
        Ep = {}
        for a in range(1, N_INT + 1):
            q = p
            while a * q <= N_INT:
                Ep[(a, a * q)] = 1
                q *= p
        lhs = {}
        for (a, b) in Z:
            v = int(LOGD[a].get(p, 0)) - int(LOGD[b].get(p, 0))
            if v:
                lhs[(a, b)] = v
        rhs = {k: -v for k, v in mm(Z, Ep).items()}
        okp, _ = mat_eq(lhs, rhs)
        ok_cheb &= okp
    ok_all &= check("S1.6 [EXACT] per-prime commutator [V_p, Z] == "
                    "-Z E_p for ALL %d primes p <= %d -- prime by "
                    "prime this IS Chebyshev's identity 1 * Lambda = "
                    "log (v_p(n) = #{k >= 1 : p^k | n})"
                    % (len(primes360), N_INT), ok_cheb)

    C = build_commDZ(N_INT)
    L360 = mat_neg_ld(mmL(M, C))
    TL360 = build_TLam(N_INT, LAMLD)
    okL, bad = mat_eq_ld(L360, TL360)
    ok_all &= check("S1.7 [EXACT] -M[D,Z] == T(Lambda) entrywise at "
                    "N = %d in the log-p module (%d divisor pairs; "
                    "includes the first-row control L[1,n] == "
                    "Lambda(n))" % (N_INT, len(Z)), okL,
                    "" if okL else "first bad %s" % (bad,))

    # S1.8 float ward at N_FLT
    rows, cols, ratio = [], [], []
    for a in range(1, N_FLT + 1):
        for b in range(a, N_FLT + 1, a):
            rows.append(a - 1)
            cols.append(b - 1)
            ratio.append(b // a)
    rows = np.array(rows, dtype=np.int64)
    cols = np.array(cols, dtype=np.int64)
    ratio = np.array(ratio, dtype=np.int64)
    shape = (N_FLT, N_FLT)
    logs = np.log(np.arange(0, N_FLT + 1, dtype=float))
    Zf = sps.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=shape)
    Mf = sps.csr_matrix((MU[ratio].astype(float), (rows, cols)),
                        shape=shape)
    Cf = sps.csr_matrix((logs[rows + 1] - logs[cols + 1], (rows, cols)),
                        shape=shape)
    lamv = np.where(ISPP[ratio], logs[PPRIME[ratio]], 0.0)
    TLf = sps.csr_matrix((lamv, (rows, cols)), shape=shape)
    R = (Mf @ Cf) + TLf
    mx = float(np.max(np.abs(R.data))) if R.nnz else 0.0
    ok_all &= check("S1.8 [FLOAT WARD] max |M[D,Z] + T(Lambda)| = "
                    "%.2e <= %.0e at N = %d (%d divisor pairs, scipy "
                    "sparse)" % (mx, BAR_FLT, N_FLT, len(rows)),
                    mx <= BAR_FLT)
    return ok_all, dict(Z=Z, M=M, C=C, L360=L360, TL360=TL360,
                        Z60=Z60, M60=M60, C60=C60, L60=L60, LS=LS,
                        lsym_primes=primes60, TLf=TLf)


# ============================== S2 powers, nilpotency, log Z, resolvents
def ordered_pp_chains(n, k):
    if k == 0:
        return [()] if n == 1 else []
    out = []
    for r in DIVS[n]:
        if r >= 2 and ISPP[r]:
            for tail in ordered_pp_chains(n // r, k - 1):
                out.append((r,) + tail)
    return out


def s2_powers_log(env):
    section("S2 -- THE POWER/CHAIN FORMULA, NILPOTENCY, AND log Z")
    ok_all = True
    L60, LS = env["L60"], env["LS"]
    Z, M, C, L360 = env["Z"], env["M"], env["C"], env["L360"]

    # S2.1 / S2.2 power formula vs independent chain enumeration
    Lp = {1: L60}
    for k in (2, 3):
        Lp[k] = mm(Lp[k - 1], L60, expand=True)
        ok_k = True
        for a in range(1, N_SYM + 1):
            for b in range(a, N_SYM + 1, a):
                want = sp.Integer(0)
                for chain in ordered_pp_chains(b // a, k):
                    want += sp.Mul(*[LS[int(PPRIME[r])] for r in chain])
                got = Lp[k].get((a, b), sp.Integer(0))
                if sp.expand(got - want) != 0:
                    ok_k = False
        nz = len(Lp[k])
        ok_all &= check("S2.%d [EXACT -- sympy] (L^%d)_{a,b} == sum over "
                        "ordered chains b/a = r_1...r_%d (prime powers) "
                        "of prod Lambda(r_j), all pairs at N = %d "
                        "(%d nonzero entries)"
                        % (k - 1, k, k, N_SYM, nz), ok_k)
    print("      sample: (L^2)[1,12] = %s (chains 3*4 and 4*3);  "
          "(L^3)[1,8] = %s (chain 2*2*2)"
          % (sp.expand(Lp[2].get((1, 12), 0)), Lp[3].get((1, 8), 0)))

    # S2.3 nilpotency
    Lp[4] = mm(Lp[3], L60, expand=True)
    Lp[5] = mm(Lp[4], L60, expand=True)
    Lp[6] = mm(Lp[5], L60, expand=True)
    ok_nil60 = (len(Lp[6]) == 0 and len(Lp[5]) > 0
                and sp.expand(Lp[5].get((1, 32), sp.Integer(0))
                              - LS[2] ** 5) == 0)
    TLf = env["TLf"]
    P = TLf.copy()
    nnz = {1: P.nnz}
    for k in range(2, 15):
        P = P @ TLf
        P.eliminate_zeros()
        nnz[k] = P.nnz
        if k == 13:
            v13 = float(P[0, 8191])
    rel13 = abs(v13 - math.log(2.0) ** 13) / math.log(2.0) ** 13
    ok_nilf = (nnz[13] == 1 and nnz[14] == 0 and rel13 <= BAR_REL)
    ok_all &= check("S2.3 [EXACT + FLOAT] nilpotency L^k = 0 for 2^k > "
                    "N: at N = %d L^6 == 0 with L^5 != 0 and "
                    "(L^5)_{1,32} == L2^5; at N = %d nnz(L^13) == 1 "
                    "(only (1, 8192), value == (log 2)^13 to rel "
                    "%.1e) and nnz(L^14) == 0"
                    % (N_SYM, N_FLT, rel13), ok_nil60 and ok_nilf)

    # S2.4 W = log Z is rational with entries 1/k at p^k
    S = {k: 1 for k in Z if k[0] != k[1]}
    Spow = {1: S}
    for k in range(2, 10):
        Spow[k] = mm(Spow[k - 1], S)
    W = {}
    for k in range(1, 9):
        s = Fr((-1) ** (k + 1), k)
        for key, v in Spow[k].items():
            W[key] = W.get(key, Fr(0)) + s * v
    W = {k: v for k, v in W.items() if v != 0}
    Wexp = {}
    for (a, b) in Z:
        r = b // a
        if r > 1 and ISPP[r]:
            kk = sum(int(c) for c in LOGD[r].values())
            Wexp[(a, b)] = Fr(1, kk)
    okW, bad = mat_eq(W, Wexp)
    ok_all &= check("S2.4 [EXACT -- RATIONAL] W := log Z = sum (-1)^"
                    "{k+1} (Z-I)^k / k has entries 1/k at ratio p^k "
                    "and 0 elsewhere at N = %d ((Z-I)^9 == 0: %s) -- "
                    "log Z is Lambda with the log stripped: kappa = "
                    "Lambda/log, a RATIONAL matrix"
                    % (N_INT, len(Spow[9]) == 0),
                    okW and len(Spow[9]) == 0,
                    "" if okW else "first bad %s" % (bad,))

    # S2.5 exp(W) == Z exactly
    Wpow = {1: W}
    for k in range(2, 9):
        Wpow[k] = mm(Wpow[k - 1], W)
    expW = {(a, a): Fr(1) for a in range(1, N_INT + 1)}
    for k in range(1, 9):
        s = Fr(1, math.factorial(k))
        for key, v in Wpow[k].items():
            expW[key] = expW.get(key, Fr(0)) + s * v
    expW = {k: v for k, v in expW.items() if v != 0}
    Zfr = {k: Fr(v) for k, v in Z.items()}
    okE, _ = mat_eq(expW, Zfr)
    ok_all &= check("S2.5 [EXACT] exp(W) == Z (Fraction arithmetic; "
                    "the nilpotent log/exp pair is exact on the "
                    "incidence algebra)", okE)

    # S2.6 L == [W, D] == -[D, log Z]
    WD = {}
    for (a, b), v in W.items():
        WD[(a, b)] = ld_clean(ld_scale(LOGD[b // a], v))
    WD = {k: v for k, v in WD.items() if v}
    okWD, bad = mat_eq_ld(WD, L360)
    ok_all &= check("S2.6 [EXACT] L == [W, D] == -[D, log Z] entrywise "
                    "at N = %d: the commutator with D multiplies the "
                    "1/k weight of log Z by k log p, restoring Lambda "
                    "-- the honest structural map between L and log Z"
                    % N_INT, okWD,
                    "" if okWD else "first bad %s" % (bad,))

    # S2.7 BCH truncation: [W, [W, D]] == 0
    WL = mmL(W, L360)
    LW = mmLs(L360, W)
    okB, _ = mat_eq_ld(WL, LW)
    ok_all &= check("S2.7 [EXACT] [W, [W, D]] == 0 (W L == L W): the "
                    "BCH series of -Z^{-1}[D,Z] = -(e^{-W} D e^{W} - "
                    "D) truncates at its first term, so the sign-fixed "
                    "relationship L = -Z^{-1}[D,Z] = -[D, log Z] is "
                    "EXACT, not first-order", okB)

    # S2.8 Chebyshev operator identity + semigroup anchor
    ZL = mmL(Zfr, L360)
    LZ = mmLs(L360, Zfr)
    negC = mat_neg_ld(C)
    ok1, _ = mat_eq_ld(ZL, negC)
    ok2, _ = mat_eq_ld(LZ, negC)
    d_arr = dirichlet_conv([0] + [1] * N_INT, [0] + [1] * N_INT, N_INT)
    Td = build_Z(N_INT, d_arr)
    okZ2, _ = mat_eq(mm(Z, Z), Td)
    ok_all &= check("S2.8 [EXACT] the Chebyshev operator identity "
                    "[D, Z] == -(Z L) == -(L Z) (i.e. 1 * Lambda = "
                    "log and [L, Z] == 0) and the semigroup anchor "
                    "Z^2 == T(d), d = 1*1, at N = %d" % N_INT,
                    ok1 and ok2 and okZ2)
    return ok_all


# ===================== S3 the four-comb discipline at the operator level
def gconj(u):
    return (u[0], -u[1])


def gmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def gnorm(u):
    return u[0] * u[0] + u[1] * u[1]


def gdiv_exact(u, v):
    n = gnorm(v)
    w = gmul(u, gconj(v))
    if w[0] % n or w[1] % n:
        return None
    return (w[0] // n, w[1] // n)


def gcanon(z):
    cands = [z, (-z[1], z[0]), (-z[0], -z[1]), (z[1], -z[0])]
    picks = [c for c in cands if c[0] >= 1 and c[1] >= 0]
    assert len(picks) == 1, z
    return picks[0]


def gaussian_primes(p_max):
    """Canonical Gaussian primes above each rational prime <= p_max."""
    gp = {}
    for p in range(2, p_max + 1):
        if SPF[p] != p:
            continue
        if p == 2:
            gp[2] = ((1, 1), None)
        elif p % 4 == 3:
            gp[p] = ((p, 0), None)
        else:
            g = 2
            while pow(g, (p - 1) // 2, p) != p - 1:
                g += 1
            s = pow(g, (p - 1) // 4, p)
            u, v = (p, 0), (s, 1)
            while gnorm(v):
                n = gnorm(v)
                w = gmul(u, gconj(v))
                q = (round(w[0] / n), round(w[1] / n))
                u, v = v, (u[0] - (q[0] * v[0] - q[1] * v[1]),
                           u[1] - (q[0] * v[1] + q[1] * v[0]))
            pi = gcanon(u)
            assert gnorm(pi) == p
            gp[p] = (pi, gcanon(gconj(pi)))
    return gp


def gfactor(z, gp):
    """Exponents of canonical Gaussian primes in z (canonical, != 0)."""
    ex = {}
    m = gnorm(z)
    for p, k in factorize(m).items():
        if p == 2:
            pi = (1, 1)
            for _ in range(k):
                z = gdiv_exact(z, pi)
                assert z is not None
            ex[pi] = ex.get(pi, 0) + k
        elif p % 4 == 3:
            assert k % 2 == 0
            pi = (p, 0)
            for _ in range(k // 2):
                z = gdiv_exact(z, pi)
                assert z is not None
            ex[pi] = ex.get(pi, 0) + k // 2
        else:
            pi, pib = gp[p]
            i = 0
            while True:
                w = gdiv_exact(z, pi)
                if w is None:
                    break
                z, i = w, i + 1
            j = k - i
            for _ in range(j):
                z = gdiv_exact(z, pib)
                assert z is not None
            if i:
                ex[pi] = i
            if j:
                ex[pib] = j
    assert gnorm(z) == 1
    return ex


def rep_counts(n_top):
    r2 = np.zeros(n_top + 1, dtype=np.int64)
    rq = np.zeros(n_top + 1, dtype=np.int64)
    rb = np.zeros(n_top + 1, dtype=np.int64)
    s = int(math.isqrt(n_top)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + y * y
            if 1 <= v <= n_top:
                r2[v] += 1
            v = x * x + 5 * y * y
            if 1 <= v <= n_top:
                rq[v] += 1
            v = 2 * x * x + 2 * x * y + 3 * y * y
            if 1 <= v <= n_top:
                rb[v] += 1
    return r2, rq, rb


def kron_m20(n_top):
    """Completely multiplicative Kronecker character chi_{-20}."""
    val = {2: 0, 5: 0}
    k = np.zeros(n_top + 1, dtype=np.int64)
    k[1] = 1
    for n in range(2, n_top + 1):
        out = 1
        for p, e in factorize(n).items():
            if p not in val:
                val[p] = 1 if pow(-20 % p, (p - 1) // 2, p) == 1 else -1
            out *= val[p] ** e
        k[n] = out
    return k


def offpp_report(lam, n_top):
    sites = [n for n in range(2, n_top + 1)
             if not ISPP[n] and lam.get(n)]
    mass = sum(ld_norm1(lam[n]) for n in sites)
    return sites, mass


def s3_four_combs():
    section("S3 -- THE FOUR-COMB DISCIPLINE AT OPERATOR LEVEL")
    ok_all = True
    r2, rq, rb = rep_counts(N_INT)

    ok_r = (r2[1] == 4 and rq[1] == 2 and rb[1] == 0 and rq[3] == 0
            and rq[7] == 0 and rq[21] == 8 and rb[2] == 2 and rb[3] == 4
            and int(np.max(rq[1:] % 2)) == 0 and int(np.max(rb[1:] % 2))
            == 0 and int(np.max(r2[1:] % 4)) == 0)
    ok_all &= check("S3.1 [EXACT] representation counts (own double "
                    "loops): r2(1)=4, rQ(1)=2, rB(1)=0; rQ(3)=rQ(7)=0 "
                    "but rQ(21)=8 (h=2 signature); all parities for "
                    "the normalizations r2/4, rQ/2, rB/2", ok_r)

    one = [0] + [1] * N_INT
    chi = [0] + [int(CHI4[n]) for n in range(1, N_INT + 1)]
    aqi = [0] + [int(r2[n]) // 4 for n in range(1, N_INT + 1)]
    aA = [0] + [int(rq[n]) // 2 for n in range(1, N_INT + 1)]
    aB = [0] + [int(rb[n]) // 2 for n in range(1, N_INT + 1)]
    k20 = kron_m20(N_INT)
    rep = [0] + [aA[n] + aB[n] for n in range(1, N_INT + 1)]

    combs = [("TRUE zeta (a=1)", one),
             ("chi4 twist (a=chi4)", chi),
             ("zeta_Q(i) scalar (a=r2/4)", aqi),
             ("EPSTEIN h=2 (a=rQ/2)", aA),
             ("class-average repair (a_A+a_B)", rep)]
    lam_of = {}
    print("    THE FOUR-COMB OPERATOR TABLE (Lambda_f = f^{-1} * "
          "(f log), exact; off-pp = support off prime powers):")
    for name, arr in combs:
        lam_of[name] = lambda_of_comb(arr, N_INT)
        sites, mass = offpp_report(lam_of[name], N_INT)
        print("      %-32s off-pp sites: %3d %-18s  off-pp L1 = %s"
              % (name, len(sites),
                 (str(sites[:5]) + ("..." if len(sites) > 5 else ""))
                 if sites else "[]",
                 "0 (EXACT)" if mass == 0 else "%.4f" % float(mass)))

    # scalar identities for the three multiplicative combs
    lam_true = lam_of["TRUE zeta (a=1)"]
    ok_t = all(ld_eq(lam_true[n], LAMLD[n]) for n in range(2, N_INT + 1))
    lam_chi = lam_of["chi4 twist (a=chi4)"]
    ok_c = all(ld_eq(lam_chi[n], ld_scale(LAMLD[n], int(CHI4[n])))
               for n in range(2, N_INT + 1))
    lam_qi = lam_of["zeta_Q(i) scalar (a=r2/4)"]
    ok_q = all(ld_eq(lam_qi[n], ld_scale(LAMLD[n], 1 + int(CHI4[n])))
               for n in range(2, N_INT + 1))
    st_t, _ = offpp_report(lam_true, N_INT)
    st_c, _ = offpp_report(lam_chi, N_INT)
    st_q, _ = offpp_report(lam_qi, N_INT)
    st_r, _ = offpp_report(lam_of["class-average repair (a_A+a_B)"],
                           N_INT)
    ok_all &= check("S3.2 [EXACT] the three multiplicative combs are "
                    "Selberg-consistent: off-pp support EMPTY and "
                    "Lambda_f == Lambda / chi4*Lambda / (1+chi4)*"
                    "Lambda for TRUE / twist / zeta_Q(i) on all "
                    "n <= %d" % N_INT,
                    ok_t and ok_c and ok_q
                    and not st_t and not st_c and not st_q)

    # matrix level: the commutator produces T(Lambda_f) for every
    # unital comb, Epstein included -- T is an algebra iso
    ident = {(a, a): 1 for a in range(1, N_INT + 1)}
    mats = {}
    ok_mat = True
    for name, arr in [c for c in combs if c[0] != "class-average "
                      "repair (a_A+a_B)"]:
        Zf = build_Z(N_INT, arr)
        Minv = dirichlet_inverse(arr, N_INT)
        Mf = build_Z(N_INT, Minv)
        okI, _ = mat_eq(mm(Mf, Zf), ident)
        Lf = mat_neg_ld(mmL(Mf, build_commDZ(N_INT, arr)))
        TLf = build_TLam(N_INT, lam_of[name])
        okL, _ = mat_eq_ld(Lf, TLf)
        ok_mat &= okI and okL
        mats[name] = (Zf, Mf, Lf)
    ok_all &= check("S3.3 [EXACT] operator level, all four unital "
                    "combs (EPSTEIN INCLUDED): M_f Z_f == I and "
                    "-M_f[D, Z_f] == T(Lambda_f) entrywise at N = %d "
                    "-- the commutator machine NEVER breaks (T(f) is "
                    "an algebra iso from Dirichlet convolution); what "
                    "breaks for h = 2 is the SUPPORT of its output"
                    % N_INT, ok_mat)

    # functoriality: T(1) T(chi4) == T(r2/4), L additive
    okF1, _ = mat_eq(mm(mats["TRUE zeta (a=1)"][0],
                        mats["chi4 twist (a=chi4)"][0]),
                     mats["zeta_Q(i) scalar (a=r2/4)"][0])
    okF2 = (dirichlet_conv(one, chi, N_INT) == aqi)
    okF3, _ = mat_eq_ld(mat_add_ld(mats["TRUE zeta (a=1)"][2],
                                   mats["chi4 twist (a=chi4)"][2]),
                        mats["zeta_Q(i) scalar (a=r2/4)"][2])
    ok_all &= check("S3.4 [EXACT] Selberg functoriality at operator "
                    "level: T(1) T(chi4) == T(r2/4) (zeta_K = zeta "
                    "L(chi4); Dirichlet-series operators always "
                    "commute) and L_{zeta_K} == L_zeta + L_chi -- the "
                    "log-derivative is additive over the product",
                    okF1 and okF2 and okF3)

    # ---- (c) zeta_{Q(i)} at the IDEAL level
    gp = gaussian_primes(NK)
    ideals = [(x, y) for x in range(1, int(math.isqrt(NK)) + 1)
              for y in range(0, int(math.isqrt(NK)) + 1)
              if x * x + y * y <= NK]
    ideals.sort(key=lambda z: (gnorm(z), z))
    idx = {z: i for i, z in enumerate(ideals)}
    norms = [gnorm(z) for z in ideals]
    cnt = np.zeros(NK + 1, dtype=np.int64)
    for z in ideals:
        cnt[gnorm(z)] += 1
    ok_cnt = all(int(cnt[n]) == int(r2[n]) // 4 for n in range(1, NK + 1))

    ZK, MK, CK, TLK = {}, {}, {}, {}
    lamK = {}
    for i, zi in enumerate(ideals):
        for j, zj in enumerate(ideals):
            if norms[j] % norms[i]:
                continue
            q = gdiv_exact(zj, zi)
            if q is None:
                continue
            ZK[(i, j)] = 1
            if i != j:
                CK[(i, j)] = ld_scale(LOGD[norms[j] // norms[i]], -1)
                ex = gfactor(gcanon(q), gp)
                muK = 0 if any(e > 1 for e in ex.values()) \
                    else (-1) ** len(ex)
                if muK:
                    MK[(i, j)] = muK
                if len(ex) == 1:
                    pi = next(iter(ex))
                    npi = gnorm(pi)
                    pr = int(SPF[npi]) if npi > 1 else 0
                    lam = {pr: Fr(2 if npi == pr * pr else 1)}
                    TLK[(i, j)] = lam
                    lamK[(i, j)] = lam
            else:
                MK[(i, j)] = 1
    identK = {(i, i): 1 for i in range(len(ideals))}
    okKI, _ = mat_eq(mm(MK, ZK), identK)
    LK = mat_neg_ld(mmL(MK, CK))
    okKL, badK = mat_eq_ld(LK, TLK)
    ok_all &= check("S3.5 [EXACT] zeta_{Q(i)} at the IDEAL level "
                    "(%d ideals of Z[i], norm <= %d, canonical "
                    "generators x>=1, y>=0): #ideals(norm n) == "
                    "r2(n)/4 (%s); M_K == [mu_K] with M_K Z_K == I; "
                    "-M_K[D_K, Z_K] == T(Lambda_K) entrywise -- the "
                    "commutator produces the DEDEKIND von Mangoldt "
                    "(log N(P) on prime-ideal powers) because ideals "
                    "factor uniquely" % (len(ideals), NK, ok_cnt),
                    ok_cnt and okKI and okKL,
                    "" if okKL else "first bad %s" % (badK,))

    unit = idx[(1, 0)]
    agg = {n: {} for n in range(2, NK + 1)}
    for (i, j), v in LK.items():
        if i == unit:
            ld_axpy(agg[norms[j]], 1, v)
    ok_agg = all(ld_eq(agg[n], ld_scale(LAMLD[n], 1 + int(CHI4[n])))
                 for n in range(2, NK + 1))
    ok_all &= check("S3.6 [EXACT] norm aggregation of the ideal-level "
                    "first row: sum_{N(A)=n} Lambda_K(A) == "
                    "(1 + chi4(n)) Lambda(n) for all n <= %d -- the "
                    "ideal operator descends to the scalar zeta_K "
                    "comb (zeta_K = zeta L(chi4))" % NK, ok_agg)
    print("      sample: Lambda_K((2+i)) = %s;  Lambda_K((1+i)^2) = %s"
          % (ld_str(LK.get((unit, idx[(2, 1)]), {})),
             ld_str(LK.get((unit, idx[(2, 0)] if (2, 0) in idx else
                            (1, 1)), {}))))

    # ---- (d) EPSTEIN h = 2: the leak localized
    lam_A = lam_of["EPSTEIN h=2 (a=rQ/2)"]
    sites, mass = offpp_report(lam_A, N_INT)
    cop = [n for n in sites if math.gcd(n, 10) == 1]
    ok_sites = (len(sites) > 0 and sites[:3] == [6, 14, 21]
                and cop and min(cop) == 21)
    ok_vals = (ld_eq(lam_A[6], {2: Fr(2), 3: Fr(2)})
               and ld_eq(lam_A[14], {2: Fr(2), 7: Fr(2)})
               and ld_eq(lam_A[21], {3: Fr(4), 7: Fr(4)})
               and ld_eq(lam_A[4], {2: Fr(2)})
               and ld_eq(lam_A[9], {3: Fr(6)}))
    heavy = sorted(((float(ld_norm1(lam_A[n])), n) for n in sites),
                   reverse=True)[:3]
    ok_all &= check("S3.7 THE EPSTEIN BREAK LOCALIZED [EXACT]: "
                    "Lambda_A leaks off the prime powers on %d sites "
                    "<= %d, first three == [6, 14, 21], min site "
                    "coprime to 10 == 21 == 3 x 7 (the UNRAMIFIED "
                    "class-group obstruction: both factors sit in the "
                    "non-principal class, their product returns to "
                    "the principal form); exact values Lambda_A(6) == "
                    "2 log 6, Lambda_A(14) == 2 log 14, Lambda_A(21) "
                    "== 4 log 21; prime-power slots differ from "
                    "zeta's (Lambda_A(4) == 2 log 2, Lambda_A(9) == "
                    "6 log 3) and are NOT leaks -- own Euler factors "
                    "are allowed, cross-prime locality is what fails"
                    % (len(sites), N_INT), ok_sites and ok_vals,
                    "sites %s..., heaviest %s"
                    % (sites[:6], [(n, round(w, 3)) for w, n in heavy]))

    ok_law = True
    for m in range(1, N_INT + 1):
        for k in range(1, N_INT // m + 1):
            if math.gcd(m, k) != 1:
                continue
            ok_law &= (aA[m * k] == aA[m] * aA[k] + aB[m] * aB[k])
            ok_law &= (aB[m * k] == aA[m] * aB[k] + aB[m] * aA[k])
    ok_rep = (rep == [0] + list(dirichlet_conv(
        one, [0] + [int(k20[n]) for n in range(1, N_INT + 1)],
        N_INT))[1:]) and not st_r
    ok_all &= check("S3.8 [EXACT] the h = 2 CLASS-CONVOLUTION LAW "
                    "a_A(mk) == a_A a_A + a_B a_B and a_B(mk) == "
                    "a_A a_B + a_B a_A on ALL coprime pairs mk <= %d "
                    "(the coefficients are a Z/2-group-ring-valued "
                    "multiplicative function; the principal slice is "
                    "not), and the CLASS-AVERAGE REPAIR a_A + a_B == "
                    "1 * chi_{-20} with off-pp support EMPTY -- the "
                    "leak is exactly the class group" % N_INT,
                    ok_law and ok_rep)
    return ok_all, lam_A, sites


# ============================ S4 the bridge to the relational carrier
def s4_bridge(env):
    section("S4 -- THE BRIDGE: the relational carrier is the first "
            "row of the incidence operator")
    ok_all = True
    M, C, L360 = env["M"], env["C"], env["L360"]
    L60, LS = env["L60"], env["LS"]

    def lsym(n):
        return sp.Add(*[int(k) * LS[p] for p, k in LOGD[n].items()])

    # S4.1 per-divisor term equality + sums
    ok_row = True
    for m in range(2, N_INT + 1):
        acc = {}
        for d in DIVS[m]:
            t_car = ld_scale(LOGD[m // d], int(MU[d]))
            t_mat = ld_scale(C.get((d, m), {}), -M.get((1, d), 0))
            if not ld_eq(t_car, t_mat):
                ok_row = False
            ld_axpy(acc, 1, t_car)
        if not ld_eq(acc, L360.get((1, m), {})):
            ok_row = False
    ok_all &= check("S4.1 [EXACT] the deployed Moebius-pairing "
                    "reconstruction sum_{d|m} mu(d) U(m/d) at TRUE "
                    "positions U = log is LITERALLY the first row of "
                    "L_N: per-divisor term equality mu(d) log(m/d) == "
                    "-M_{1,d}[D,Z]_{d,m} for EVERY d | m and every "
                    "m <= %d, and the sums == L[1, m]" % N_INT, ok_row)

    # S4.2 the pairing matrix B is a sub-block of Z^{-1}
    events = [1] + [n for n in range(2, X_SUPPORT + 1) if ISPP[n]]
    ok_B = True
    n_sub = 0
    for u in events:
        for v in events:
            if v % u:
                continue
            n_sub += 1
            if int(MU[v // u]) != M.get((u, v), 0):
                ok_B = False
    ok_all &= check("S4.2 [EXACT] the pairing matrix B[k,j] = "
                    "mu(m_k/m_j) on the deployed comb support (prime "
                    "powers in [2, %d] + unit; %d divisor pairs) == "
                    "the sub-block of M = Z^{-1} -- the deployed "
                    "design was already reading the inverse incidence "
                    "operator" % (X_SUPPORT, n_sub), ok_B)

    # S4.3 row self-similarity
    ok_shift = True
    for a in range(1, N_INT + 1):
        for b in range(a, N_INT + 1, a):
            if not ld_eq(L360.get((a, b), {}),
                         L360.get((1, b // a), {})):
                ok_shift = False
    ok_all &= check("S4.3 [EXACT] row self-similarity L[a, ab] == "
                    "L[1, b] for all ab <= %d: every row is the first "
                    "row on the shifted sub-poset -- the carrier "
                    "generalizes verbatim to all rows" % N_INT,
                    ok_shift)

    # S4.4 untapped structure: Selberg Lambda_2 scalar + operator
    ok_l2s = True
    for n in range(1, N_SYM + 1):
        lam2 = sp.Integer(0)
        for d in DIVS[n]:
            if MU[d]:
                lam2 += int(MU[d]) * lsym(n // d) ** 2
        lamn = LS[int(PPRIME[n])] if (n > 1 and ISPP[n]) else \
            sp.Integer(0)
        conv = sp.Integer(0)
        for d in DIVS[n]:
            e = n // d
            ld_ = LS[int(PPRIME[d])] if (d > 1 and ISPP[d]) else None
            le_ = LS[int(PPRIME[e])] if (e > 1 and ISPP[e]) else None
            if ld_ is not None and le_ is not None:
                conv += ld_ * le_
        if sp.expand(lam2 - (lamn * lsym(n) + conv)) != 0:
            ok_l2s = False
    L2mat = mm(L60, L60, expand=True)
    ok_l2o = True
    for a in range(1, N_SYM + 1):
        for b in range(a, N_SYM + 1, a):
            r = b // a
            lam2 = sp.Integer(0)
            for d in DIVS[r]:
                if MU[d]:
                    lam2 += int(MU[d]) * lsym(r // d) ** 2
            got = (L2mat.get((a, b), sp.Integer(0))
                   - (lsym(a) - lsym(b))
                   * L60.get((a, b), sp.Integer(0)))
            if sp.expand(got - lam2) != 0:
                ok_l2o = False
    ok_all &= check("S4.4 [EXACT -- sympy] the untapped structure is "
                    "the Selberg hierarchy: mu * log^2 == Lambda log "
                    "+ Lambda*Lambda scalar for all n <= %d AND "
                    "T(mu * log^2) == L^2 - [D, L] entrywise -- the "
                    "carrier read row 1 of L; rows are shifts (S4.3), "
                    "powers are ordered factorization chains (S2), "
                    "and the power/bracket combinations are the "
                    "higher von Mangoldt functions" % N_SYM,
                    ok_l2s and ok_l2o)
    return ok_all


# ================================================================= main
def main():
    section("PRIME.RELATION.MANGOLDT.01 -- the von Mangoldt commutator "
            "theorem (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    L_N := -M[D,Z] with Z = [1_{a|b}], M = Z^{-1}, "
          "D = diag(log a).  Classical incidence-algebra content, "
          "typed as such.  NO RH claim; writes nothing.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbols; own "
          "sieves; the divisor/mu arithmetic is admissible input "
          "(it IS the Euler-product datum)", not bad,
          "found %s" % bad if bad else "clean")

    build_arithmetic()
    ok1, env = s1_exact()
    ok2 = s2_powers_log(env)
    ok3, lam_A, sites = s3_four_combs()
    ok4 = s4_bridge(env)

    section("V -- FROZEN VERDICT")
    if ok1 and ok2 and ok3 and ok4:
        verdict = "MANGOLDT-COMMUTATOR-EXACT"
    elif ok1:
        verdict = "MANGOLDT-COMMUTATOR-PARTIAL"
    else:
        verdict = "FAIL"
    print("\n  VERDICT: %s   [S1 exact: %s | S2 powers/log: %s | "
          "S3 four-comb: %s | S4 bridge: %s]"
          % (verdict, "OK" if ok1 else "FAIL", "OK" if ok2 else "FAIL",
             "OK" if ok3 else "FAIL", "OK" if ok4 else "FAIL"))
    if verdict == "MANGOLDT-COMMUTATOR-EXACT":
        print("""
  THE FINDING (typed honestly): the von Mangoldt commutator theorem
  L_N = -M[D,Z] = T(Lambda) is verified EXACTLY (sympy log-integer
  basis at N = 60, integer/Fraction layer at N = 360, float ward at
  N = 10^4) -- it is classical incidence-algebra arithmetic (mu*log
  = Lambda in matrix clothes), NOT new mathematics; its measured
  operator packaging delivers:
    (1) the power formula: L^k enumerates ordered factorization
        chains into prime powers with weight prod Lambda(r_j);
        nilpotency degree = floor(log2 N) + 1;
    (2) the log: log Z is RATIONAL (1/k at ratio p^k) and
        L = -Z^{-1}[D,Z] = -[D, log Z] EXACTLY (the BCH series
        truncates: [log Z, [log Z, D]] = 0); [D,Z] = -Z L is
        Chebyshev's 1*Lambda = log at operator level;
    (3) the four-comb discipline transported to operator level: the
        commutator machine ALWAYS outputs T(Lambda_f) (T is an
        algebra iso) -- Selberg consistency is a SUPPORT statement;
        TRUE / chi4-twist / zeta_{Q(i)} (scalar AND ideal-level,
        with norm aggregation (1+chi4) Lambda) are exactly prime-
        power-supported; the h = 2 Epstein comb x^2+5y^2 leaks at
        [6, 14, 21, ...], first unramified site 21 = 3x7, values
        pinned exactly, and the leak is REPAIRED by the class
        average (a_A + a_B = 1 * chi_{-20}): the operator-level
        discriminator localizes the class-group obstruction;
    (4) the bridge: the deployed relational carrier's mu-pairing
        reconstruction IS the first row of L_N (per-divisor term
        equality); rows are shifts, powers are chain correlations,
        and L^2 - [D, L] = T(mu * log^2) -- the untapped structure
        is the Selberg hierarchy.
  NO RH claim: nothing here bounds zeros; the deliverable is the
  exact operator identity + the typed discriminator + the carrier
  bridge, exploration-grade only.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    dt = time.time() - T0
    check("V.1 runtime %.1f s within budget %.0f s" % (dt,
          RUNTIME_BUDGET_S), dt <= RUNTIME_BUDGET_S)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (dt, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(main())
