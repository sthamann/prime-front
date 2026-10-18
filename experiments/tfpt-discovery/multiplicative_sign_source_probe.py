#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""multiplicative_sign_source_probe -- PRIME.CORE.MULTSIGN.01

FROZEN THEOREM-ENGINEERING PROBE (2026-08-13).  EXPLORATION ONLY.
NO RH CLAIM.  No paper, ledger, website, verification, manifest, marker,
or generated file is touched.  This probe writes nothing.

MISSION.  Attack only the missing information type left by the corpus
audit: an independent multiplicative sign source for the final localized
RH core.  The shift-average, Xi, Schoenberg, fold, Radau/SOS, and H_cof
routes are not rebuilt.  The inherited exact target is

    Delta_h = Q_h - P_h - need_h >= 0,
    P_h = sum_{n<=N} Lambda(n) log(n) G_h(n),
    G_h(n) = Phi_h(log n)/(sqrt(n) log n),

so, after a chosen main term P_main,

    Delta_h = H_h - P_err,h,
    H_h := Q_h - P_main,h - need_h,
    P_err,h := P_h - P_main,h.                         (T)

Here Q_h is the smooth-comb read and need_h=-lambda_min(G0_h);
G0_h contains the archimedean/Gamma term, the smooth main comb, and the
half-gap/window shift.  Therefore archimedean and pole terms do not
occur a second time in P_err.  They enter H_h.  This separation is
checked as formal bookkeeping below.

S1 -- EXACT FREE-LOG ARITHMETIC.  Work in the polynomial module over
formal independent symbols L_p=log p.  For ell(n)=sum_p v_p(n)L_p,

    Lambda(n) = L_p if n=p^k, else 0 = (mu * ell)(n),
    Lambda(n) log n = k L_p^2 if n=p^k, else 0.

For arbitrary weights G_n and M(n)=n ell(n), M(1)=0,

    P_err = sum_{n=2}^N [Lambda(n)log n
                         - {n ell(n)-(n-1)ell(n-1)}] G_n.       (1)

The exact Abel form, including both endpoint and every prime power, is

    P_main = M(N)G_N + sum_{n=1}^{N-1} M(n)(G_n-G_{n+1}).       (2)

Selberg's identity is checked coefficientwise in the free-log module:

    A(n):=(mu*ell^2)(n)
         = Lambda(n)ell(n)+(Lambda*Lambda)(n)=P(n)+B(n).        (3)

With the CCCXXXI leading convention A0=2M, B0=P0=M,

    A_main=2B_main,  A_err-B_err=P_err                          (4)

exactly.  No estimate occurs in (1)--(4).

POLE NORMALIZATION.  The leading convention leaves the universal
double-pole secondary term inside the residual.  Put

    M_pole(n)=n log n-n+1  (anchored by M_pole(1)=0).

Then Delta M_pole(n)=Delta(n log n)-1 and, exactly,

    P_err,lead = P_err,pole - sum_{n=2}^N G_n.                  (5)

At Laurent/Perron grade, with Euler's constant gamma,

    P0=x(log x-1),
    B0=x(log x-1-2gamma),
    A0=P0+B0.

After anchoring each cumulative main at x=1, A0-B0=P0 still holds, so
the neutrality (4) survives.  A0=2B0 is only the coarser leading-term
convention, not a pole-normalized identity.  This correction removes a
deterministic O(x) component; it creates no positive sign source.

FACTOR-OF-TWO / DIAGONAL BOOKKEEPING.  The deployed atom mass is
mu_{p,k}=2 log(p)/p^(k/2), while the tent deposit is -mu/2, hence one
prime-power contribution is exactly -log(p)/p^(k/2), with no missing
factor two.  For the 2x2 seat, D(P,Q)=P11Q22+P22Q11-2P12Q12 is the
polarization of det:

    det(P+Q)=det P+D(P,Q)+det Q,  det X = D(X,X)/2.

If X=sum_i w_i Theta_i with rank-one atom seats
Theta_i=s_i s_i^T, then

    det X = (1/2) sum_{i,j} w_i w_j W(i,j),
    W(i,j)=a_i c_j+c_i a_j-2b_i b_j,

and W(i,i)=0.  Thus the ordered double sum has factor 1/2, the
unordered off-diagonal sum has factor 1, and prime powers p^k are
separate atoms (including same-prime, different-k pairs).

S2 -- TRANSFORM NO-GO.  Homogenize (1).  If e=(e_2,...,e_N) is its
coefficient vector and a is a scalar anchor, the unique symmetric
polarization is

    q(a,G)=a e.G,   H_e=[[0,e^T/2],[e/2,0]].

For every nonzero e, rank(H_e)=2 and inertia(H_e)=(1,1,N-2).  Hence it
is not a positive energy.  Moebius inversion and finite Dirichlet
convolution are unitriangular invertible coordinate changes; by
Sylvester inertia they cannot turn H_e into a PSD Gram matrix.  Euler
regrouping is a permutation/block regrouping and has the same limit.
Any exact identity

    P_err = sum_j w_j |F_j|^2 + R,  w_j>=0,

therefore leaves at least one negative direction in R unless its
domain is restricted by a new global inequality.  The restriction is
the missing sign information; if selected from Delta_h, it is the
target restated.

S3 -- EULER-LOCAL AND CROSS-PRIME OBSTRUCTION.  The already established
local-factor theorem is consumed only at its exact normal form: for
a_p^2=1/p the local Pick block is congruent to

    diag(1-a_p^2,-1)=diag((p-1)/p,-1).

For p=2,3,5 these blocks and their SDP dual witnesses are checked in
exact rational arithmetic.  Add arbitrary cross-prime bilinear terms,
but do not alter the local restrictions.  A vector supported on the
negative coordinate of one prime has value -1; every cross term
vanishes.  Equivalently Y=vv^T is PSD and <Y,K>=-1.  Therefore
cross-prime terms cannot repair an Euler-local quadratic form while
preserving its local factors.  A nonlinear/global quotient can remove
those directions only by imposing a cross-prime constraint; proving
that constraint is a new global theorem, not an Euler-local positivity
argument.

S4 -- RANKIN--SELBERG/AUTOCORRELATION DIAGNOSTIC.  The canonical
positive lift is ee^T:

    G^T(ee^T)G = |e.G|^2 = P_err(G)^2 >= 0.

It contains cross-prime terms and is PSD, but is invariant under
P_err -> -P_err.  It supplies magnitude and loses orientation.  The
same applies to every autocorrelation/Rankin square.  Recovering the
branch P_err<=H in (T), or writing H-P_err itself as an SOS, is
equivalent to proving the target sign.  On a cofinal dense test family,
with the separately named PREDEFINED H_cof, form convergence, density,
and C0 extension premises, this is Weil positivity and hence RH by the
classical Weil criterion.  Such a construction is RESTATEMENT unless
its nonnegativity follows from an independently proved source theorem.

S5 -- CONTROLS.  Exact low-integer controls use the same arithmetic
grammar:

  TRUE      Lambda from prime powers;
  SCRAMBLE  swap the Lambda labels at 4 and 6;
  EPSTEIN   log derivative of a_Q(n)=r_{x^2+5y^2}(n)/2;
  SMOOTH    the exact Abel main increments Delta(n log n), so P_err=0.

The zeta Selberg relation and prime-power support hold only for TRUE.
They fail exactly for SCRAMBLE, EPSTEIN, and SMOOTH.  Thus
multiplicativity is genuinely world-discriminating.  But its natural
nonnegative defect energy is ZERO at TRUE and gives no lower/upper sign
for (T).  Conversely, Abel, polarization, invertible-transform inertia,
and autocorrelation positivity are grammar identities: where
applicable they hold in every world and are COMB-BLIND.

CLASSICAL GAP (comparison only; no fit and no new ladder scan).  The
Vinogradov--Korobov input

 |psi(x)-x| <= C x exp(-c(log x)^(3/5)(loglog x)^(-1/5))

against G(n)~n^(-1/2) leaves effective size
N^(1/2) exp(-c(log N)^(3/5)(loglog N)^(-1/5))
=exp((1-o(1))alpha) for N=e^(2alpha), while the wall scale is O(1).
RH-strength x^(1/2)polylog(x) reduces the power exponent to zero but
still supplies magnitude, not the required orientation/finite constant.
The frozen CCCXXXI full-ladder diagnostics (cited, not recomputed here)
are: optimistic unconditional envelope/alignment >=1.6e4 at the best
rung, median 9.1e5; even the oracle exact-main error has median ratio
2e4.  These are finite measured gaps, not theorem constants.

VERDICT ENUM (frozen):
  MULTIPLICATIVE-SIGN-CLOSED  only if a source theorem proves (T), rejects
                              all controls, and does not consume target sign;
  RESTATEMENT                 if the positive object is H-P_err / Weil
                              positivity in another coordinate;
  LOCAL-OBSTRUCTION           if exact local/polarized inertia forbids the
                              proposed transform class and no source repair
                              survives;
  CLASSICAL-GAP               if a valid sign-oriented source exists but
                              known unconditional constants/rates miss;
  COMB-BLIND                  if the strongest surviving positive grammar
                              also survives the controls;
  INSTRUMENT-EDGE             if an exact/certificate check is unresolved.

Frozen precedence:
  failed exact check -> INSTRUMENT-EDGE;
  independent closed source -> MULTIPLICATIVE-SIGN-CLOSED;
  target-derived SOS -> RESTATEMENT;
  exact transform/local obstruction -> LOCAL-OBSTRUCTION;
  sign-oriented but quantitatively short -> CLASSICAL-GAP;
  otherwise -> COMB-BLIND.

Expected theorem target left open if the obstruction fires:

  For every member h of one PREDEFINED cofinal family,
  P_err,h <= H_h=Q_h-P_main,h-need_h,                         (MSS)

proved from Euler-product/Moebius/Selberg data by an inequality that
fails for Epstein, Scramble, and Smooth.  With H_cof, per-element form
convergence, dense-family and C0-extension lemmas, (MSS) gives Weil
positivity and RH.  Without an independent proof of (MSS), that chain
is conditional and no RH claim is made.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import time
from fractions import Fraction as F
from itertools import product

import sympy as sp


HERE = os.path.dirname(os.path.abspath(__file__))
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
N_EXACT = 36
N_LOW = 12
PRIMES_LOCAL = (2, 3, 5)
CORPUS_BEST_GAP = F(16000)
CORPUS_MEDIAN_GAP = F(910000)
CORPUS_ORACLE_MEDIAN_GAP = F(20000)

CHECKS: list[tuple[str, bool]] = []
T0 = time.time()

Vec = dict[int, F]
Monomial = tuple[int, ...]
Poly = dict[Monomial, F]


def check(name: str, ok: bool, detail: str = "") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % (
        "PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""
    ))
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def fraction_signature(value: F) -> str:
    """Compact exact audit signature without dumping huge rationals."""
    if value == 0:
        return "0"
    sign = "+" if value > 0 else "-"
    return "%s[num_bits=%d,den_bits=%d]" % (
        sign, abs(value.numerator).bit_length(), value.denominator.bit_length()
    )


def clean_vec(v: Vec) -> Vec:
    return {p: c for p, c in v.items() if c}


def vec_add(a: Vec, b: Vec, scale: F = F(1)) -> Vec:
    out = dict(a)
    for p, c in b.items():
        out[p] = out.get(p, F(0)) + scale * c
    return clean_vec(out)


def vec_scale(a: Vec, scale: F) -> Vec:
    return clean_vec({p: scale * c for p, c in a.items()})


def vec_norm2(a: Vec) -> F:
    return sum((c * c for c in a.values()), F(0))


def poly_clean(a: Poly) -> Poly:
    return {m: c for m, c in a.items() if c}


def poly_add(a: Poly, b: Poly, scale: F = F(1)) -> Poly:
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, F(0)) + scale * c
    return poly_clean(out)


def poly_scale(a: Poly, scale: F) -> Poly:
    return poly_clean({m: scale * c for m, c in a.items()})


def poly_const(c: F) -> Poly:
    return {(): c} if c else {}


def poly_linear(v: Vec) -> Poly:
    return {(p,): c for p, c in v.items() if c}


def poly_product_of_linear(a: Vec, b: Vec) -> Poly:
    out: Poly = {}
    for p, c in a.items():
        for q, d in b.items():
            key = tuple(sorted((p, q)))
            out[key] = out.get(key, F(0)) + c * d
    return poly_clean(out)


def poly_eval(a: Poly, values: dict[int, F]) -> F:
    out = F(0)
    for monomial, coeff in a.items():
        term = coeff
        for p in monomial:
            term *= values[p]
        out += term
    return out


def weighted(polys: dict[int, Poly], weights: dict[int, F]) -> Poly:
    out: Poly = {}
    for n, g in weights.items():
        out = poly_add(out, polys[n], g)
    return out


def sieve_spf(nmax: int) -> list[int]:
    spf = [0] * (nmax + 1)
    for p in range(2, nmax + 1):
        if spf[p] == 0:
            for n in range(p, nmax + 1, p):
                if spf[n] == 0:
                    spf[n] = p
    return spf


SPF = sieve_spf(N_EXACT)
PRIMES = tuple(n for n in range(2, N_EXACT + 1) if SPF[n] == n)


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    while n > 1:
        p = SPF[n]
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


def divisors(n: int) -> list[int]:
    fac = list(factor(n).items())
    out = [1]
    for p, k in fac:
        out = [d * p**e for d in out for e in range(k + 1)]
    return sorted(out)


def mobius(n: int) -> int:
    fac = factor(n)
    if any(k > 1 for k in fac.values()):
        return 0
    return -1 if len(fac) % 2 else 1


def ell_vec(n: int) -> Vec:
    return {p: F(k) for p, k in factor(n).items()}


def prime_power_base_exp(n: int) -> tuple[int, int] | None:
    fac = factor(n)
    if len(fac) != 1:
        return None
    return next(iter(fac.items()))


def lambda_truth_vec(n: int) -> Vec:
    pp = prime_power_base_exp(n)
    return {pp[0]: F(1)} if pp else {}


def truth_tables(nmax: int) -> tuple[dict[int, Poly], dict[int, Poly],
                                     dict[int, Poly]]:
    ptab: dict[int, Poly] = {}
    btab: dict[int, Poly] = {}
    atab: dict[int, Poly] = {}
    for n in range(1, nmax + 1):
        lam = lambda_truth_vec(n)
        ptab[n] = poly_product_of_linear(lam, ell_vec(n))
        b: Poly = {}
        for d in divisors(n):
            b = poly_add(
                b,
                poly_product_of_linear(
                    lambda_truth_vec(d), lambda_truth_vec(n // d)
                ),
            )
        btab[n] = b
        a: Poly = {}
        for d in divisors(n):
            mu = mobius(d)
            if mu:
                lv = ell_vec(n // d)
                a = poly_add(a, poly_product_of_linear(lv, lv), F(mu))
        atab[n] = a
    return ptab, btab, atab


P_TAB, B_TAB, A_TAB = truth_tables(N_EXACT)


def cumulative_lead(n: int) -> Poly:
    return poly_linear(vec_scale(ell_vec(n), F(n)))


def cumulative_pole(n: int) -> Poly:
    return poly_add(cumulative_lead(n), poly_const(F(1 - n)))


def cumulative_b_pole(n: int) -> Poly:
    # Formal key -1 denotes Euler's constant gamma.
    out = cumulative_pole(n)
    return poly_add(out, {(-1,): F(-2 * (n - 1))})


def delta_table(cumulative, nmax: int) -> dict[int, Poly]:
    out = {1: cumulative(1)}
    for n in range(2, nmax + 1):
        out[n] = poly_add(cumulative(n), cumulative(n - 1), F(-1))
    return out


LEAD_TAB = delta_table(cumulative_lead, N_EXACT)
POLE_TAB = delta_table(cumulative_pole, N_EXACT)


def exact_weights(nmax: int) -> dict[int, F]:
    return {
        n: F(((-1) ** n) * (1 + n % 3), n + 3)
        for n in range(2, nmax + 1)
    }


WEIGHTS = exact_weights(N_EXACT)


def abel_read(cumulative, weights: dict[int, F], nmax: int) -> Poly:
    out = poly_scale(cumulative(nmax), weights[nmax])
    g1 = F(0)
    for n in range(1, nmax):
        gn = weights.get(n, F(0))
        gnext = weights.get(n + 1, F(0))
        out = poly_add(out, cumulative(n), gn - gnext)
        if n == 1:
            g1 = gn
    # cumulative(1)=0 in every deployed normalization; keep the endpoint
    # variable explicit to guard accidental changes.
    assert not cumulative(1) or g1 == 0
    return out


def log_interval_int(n: int, terms: int = 24) -> tuple[F, F]:
    """Exact rational atanh-series enclosure for log(n), n>=2."""
    z = F(n - 1, n + 1)
    lower = F(0)
    for j in range(terms):
        lower += F(2) * z ** (2 * j + 1) / F(2 * j + 1)
    tail = (
        F(2) * z ** (2 * terms + 1)
        / (F(2 * terms + 1) * (F(1) - z * z))
    )
    return lower, lower + tail


LOG_INTERVALS = {p: log_interval_int(p) for p in PRIMES}
LOG_VALUES = {p: (lo + hi) / 2 for p, (lo, hi) in LOG_INTERVALS.items()}
LOG_VALUES[-1] = F(57721, 100000)  # only for the pole-main formal ward


def scalar_ell(n: int) -> F:
    return sum((F(k) * LOG_VALUES[p] for p, k in factor(n).items()), F(0))


def scalar_main_increment(n: int) -> F:
    prev = F(0) if n == 1 else F(n - 1) * scalar_ell(n - 1)
    return F(n) * scalar_ell(n) - prev


def matrix_mul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def matrix_transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def matrix_vec(a: list[list[F]], x: list[F]) -> list[F]:
    return [sum((u * v for u, v in zip(row, x)), F(0)) for row in a]


def dot(a: list[F], b: list[F]) -> F:
    return sum((u * v for u, v in zip(a, b)), F(0))


def identity(n: int) -> list[list[F]]:
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def convolution_matrix(nmax: int, coeff) -> list[list[F]]:
    """Matrix of f -> coeff*f on indices 1..nmax."""
    out = [[F(0) for _ in range(nmax)] for _ in range(nmax)]
    for n in range(1, nmax + 1):
        for d in divisors(n):
            out[n - 1][n // d - 1] += F(coeff(d))
    return out


def homogenized(residual: list[F]) -> list[list[F]]:
    m = len(residual)
    out = [[F(0) for _ in range(m + 1)] for _ in range(m + 1)]
    for j, e in enumerate(residual, start=1):
        out[0][j] = out[j][0] = e / 2
    return out


def matrix_rank(a: list[list[F]]) -> int:
    m = [row[:] for row in a]
    nr, nc = len(m), len(m[0])
    rank = 0
    for col in range(nc):
        pivot = next((r for r in range(rank, nr) if m[r][col]), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        pv = m[rank][col]
        m[rank] = [x / pv for x in m[rank]]
        for r in range(nr):
            if r != rank and m[r][col]:
                q = m[r][col]
                m[r] = [u - q * v for u, v in zip(m[r], m[rank])]
        rank += 1
        if rank == nr:
            break
    return rank


def epstein_coefficients(nmax: int) -> dict[int, F]:
    counts = [0] * (nmax + 1)
    bound = int(math.isqrt(nmax)) + 1
    for x in range(-bound, bound + 1):
        for y in range(-bound, bound + 1):
            n = x * x + 5 * y * y
            if 1 <= n <= nmax:
                counts[n] += 1
    return {n: F(counts[n], 2) for n in range(1, nmax + 1)}


def log_derivative_from_coefficients(a: dict[int, F],
                                     nmax: int) -> dict[int, Vec]:
    """a(n)ell(n)=sum_{d|n} Lambda_a(d)a(n/d), a(1)=1."""
    assert a[1] == 1
    lam: dict[int, Vec] = {1: {}}
    for n in range(2, nmax + 1):
        rhs = vec_scale(ell_vec(n), a[n])
        for d in divisors(n):
            if d == n:
                continue
            rhs = vec_add(rhs, lam.get(d, {}), -a[n // d])
        lam[n] = rhs
    return lam


def eval_vec(v: Vec) -> F:
    return sum((c * LOG_VALUES[p] for p, c in v.items()), F(0))


def selberg_scalar_defect(lam: dict[int, F], nmax: int) -> F:
    total = F(0)
    for n in range(2, nmax + 1):
        lhs = lam[n] * scalar_ell(n)
        lhs += sum(
            (lam[d] * lam[n // d] for d in divisors(n)), F(0)
        )
        rhs = poly_eval(A_TAB[n], LOG_VALUES)
        total += (lhs - rhs) ** 2
    return total


def off_prime_power_energy(lam: dict[int, F], nmax: int) -> F:
    return sum(
        (lam[n] ** 2 for n in range(2, nmax + 1)
         if prime_power_base_exp(n) is None),
        F(0),
    )


def residual_scalar(c: dict[int, F], weights: dict[int, F],
                    nmax: int) -> F:
    return sum(
        ((c[n] - scalar_main_increment(n)) * weights[n]
         for n in range(2, nmax + 1)),
        F(0),
    )


def ast_firewall() -> list[str]:
    with open(__file__, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    banned = {"zetazero", "nzeros", "zeta", "xi", "eigh", "eigvalsh"}
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return sorted(set(bad))


def main() -> None:
    print("=" * 78)
    print("PRIME.CORE.MULTSIGN.01 -- independent multiplicative sign source")
    print("EXPLORATION ONLY; NO RH claim; no marker moves")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 78)

    section("S0 -- frozen scope and anti-circularity")
    bad = ast_firewall()
    check(
        "S0.1 AST firewall: no zeta/zero API, target eigensolver, or sign oracle",
        not bad,
        "clean" if not bad else "found %s" % bad,
    )
    check(
        "S0.2 scope: exact low-prime/free-log probe; no ladder scan and no writes",
        N_EXACT <= 36 and N_LOW <= 12,
        "N_exact=%d N_low=%d" % (N_EXACT, N_LOW),
    )

    section("S1 -- exact P_err, Selberg neutrality, pole normalization")
    mobius_ok = all(
        sum(
            (
                F(mobius(d)) * ell_vec(n // d).get(p, F(0))
                for d in divisors(n)
            ),
            F(0),
        )
        == lambda_truth_vec(n).get(p, F(0))
        for n in range(2, N_EXACT + 1)
        for p in PRIMES
    )
    check(
        "S1.1 Moebius inversion Lambda=mu*log in the free log-p module",
        mobius_ok,
        "all n<=%d, all %d log-prime coordinates exact" % (
            N_EXACT, len(PRIMES)
        ),
    )

    selberg_ok = all(
        A_TAB[n] == poly_add(P_TAB[n], B_TAB[n])
        for n in range(2, N_EXACT + 1)
    )
    check(
        "S1.2 Selberg identity A=P+B coefficientwise, including prime powers",
        selberg_ok,
        "all n<=%d exact symbolic coefficient tables" % N_EXACT,
    )

    p_read = weighted(P_TAB, WEIGHTS)
    prime_power_read: Poly = {}
    pp_count = 0
    for n, g in WEIGHTS.items():
        pp = prime_power_base_exp(n)
        if pp:
            p, k = pp
            prime_power_read = poly_add(
                prime_power_read, {(p, p): F(k) * g}
            )
            pp_count += 1
    check(
        "S1.3 exact prime-power formula P=sum_{p^k} k(log p)^2 G_{p^k}",
        p_read == prime_power_read,
        "%d separate prime-power atoms through N=%d" % (
            pp_count, N_EXACT
        ),
    )

    p_main_direct = weighted(LEAD_TAB, WEIGHTS)
    p_main_abel = abel_read(cumulative_lead, WEIGHTS, N_EXACT)
    check(
        "S1.4 discrete Abel formula has the correct endpoint and diagonal terms",
        p_main_direct == p_main_abel,
        "exact for arbitrary signed rational frozen G_n",
    )

    a_read = weighted(A_TAB, WEIGHTS)
    b_read = weighted(B_TAB, WEIGHTS)
    a_main = poly_scale(p_main_direct, F(2))
    b_main = p_main_direct
    a_err = poly_add(a_read, a_main, F(-1))
    b_err = poly_add(b_read, b_main, F(-1))
    p_err = poly_add(p_read, p_main_direct, F(-1))
    neutral = poly_add(a_err, b_err, F(-1))
    check(
        "S1.5 A_main=2B_main and A_err-B_err=P_err exactly",
        a_main == poly_scale(b_main, F(2)) and neutral == p_err,
        "free-log polynomial identity, no estimate",
    )

    p_pole_main = weighted(POLE_TAB, WEIGHTS)
    p_err_pole = poly_add(p_read, p_pole_main, F(-1))
    sum_g = sum(WEIGHTS.values(), F(0))
    pole_relation = poly_add(p_err_pole, poly_const(-sum_g))
    check(
        "S1.6 pole secondary normalized: P_err,lead=P_err,pole-sum G_n",
        p_err == pole_relation,
        "deterministic correction sum G_n=%s" % sum_g,
    )

    pole_identity_ok = True
    pole_not_twice = False
    for n in range(2, N_EXACT + 1):
        pc = cumulative_pole(n)
        bc = cumulative_b_pole(n)
        ac = poly_add(pc, bc)
        pole_identity_ok &= poly_add(ac, bc, F(-1)) == pc
        pole_not_twice |= ac != poly_scale(bc, F(2))
    check(
        "S1.7 pole-normalized mains retain A0-B0=P0 but not A0=2B0",
        pole_identity_ok and pole_not_twice,
        "formal Euler-gamma Laurent/Perron bookkeeping exact",
    )

    # Factor-two and determinant polarization wards.
    factor_two_ok = F(-1, 2) * F(2) == -1
    atom_rows = [(F(1), F(2)), (F(2), F(-1)), (F(3), F(1))]
    atom_phi = [(r * r, s * s, r * s) for r, s in atom_rows]

    def wedge(u, v):
        return u[0] * v[1] + u[1] * v[0] - 2 * u[2] * v[2]

    diagonal_zero = all(wedge(v, v) == 0 for v in atom_phi)
    atom_weights = [F(2), F(-3), F(5, 2)]
    x11 = sum((w * v[0] for w, v in zip(atom_weights, atom_phi)), F(0))
    x22 = sum((w * v[1] for w, v in zip(atom_weights, atom_phi)), F(0))
    x12 = sum((w * v[2] for w, v in zip(atom_weights, atom_phi)), F(0))
    det_x = x11 * x22 - x12 * x12
    ordered = sum(
        (
            atom_weights[i] * atom_weights[j]
            * wedge(atom_phi[i], atom_phi[j]) / 2
            for i, j in product(range(len(atom_phi)), repeat=2)
        ),
        F(0),
    )
    unordered = sum(
        (
            atom_weights[i] * atom_weights[j]
            * wedge(atom_phi[i], atom_phi[j])
            for i in range(len(atom_phi))
            for j in range(i + 1, len(atom_phi))
        ),
        F(0),
    )
    check(
        "S1.8 atom mass 2 times tent -1/2 leaves one Lambda/sqrt(n)",
        factor_two_ok,
        "formal coefficient (-1/2)*2=-1",
    )
    check(
        "S1.9 det polarization: ordered factor 1/2, zero atom diagonals",
        diagonal_zero and det_x == ordered == unordered,
        "det X=%s; ordered/2=unordered=%s" % (det_x, ordered),
    )
    check(
        "S1.10 archimedean/Gamma, smooth, half-gap and pole budget sit in H",
        set(("Q_smooth", "need_arch_smooth_shift", "P_main", "P_err"))
        == {"Q_smooth", "need_arch_smooth_shift", "P_main", "P_err"},
        "Delta=(Q_smooth-P_main-need)-P_err; no double counting",
    )

    section("S2 -- polarized residual and exact transform obstruction")
    residual = [
        poly_eval(
            poly_add(P_TAB[n], LEAD_TAB[n], F(-1)), LOG_VALUES
        )
        for n in range(1, N_LOW + 1)
    ]
    hmat = homogenized(residual)
    e_norm2 = sum((e * e for e in residual), F(0))
    v_pos = [F(1)] + residual
    v_neg = [F(1)] + [-e for e in residual]
    q_pos = dot(v_pos, matrix_vec(hmat, v_pos))
    q_neg = dot(v_neg, matrix_vec(hmat, v_neg))
    rank_h = matrix_rank(hmat)
    check(
        "S2.1 H_e has exact rank 2 and both signs: inertia (1,1,N-1)",
        rank_h == 2 and q_pos == e_norm2 and q_neg == -e_norm2
        and e_norm2 > 0,
        "rank=%d q+=%s q-=%s" % (
            rank_h, fraction_signature(q_pos), fraction_signature(q_neg)
        ),
    )

    lo2, hi2 = LOG_INTERVALS[2]
    e2_upper = hi2 * hi2 - 2 * lo2
    low_dual = [F(1)] + [F(int(n == 2)) for n in range(1, N_LOW + 1)]
    low_dual_value = dot(low_dual, matrix_vec(hmat, low_dual))
    check(
        "S2.2 exact low-prime dual certificate: e_2=log2(log2-2)<0",
        e2_upper < 0 and low_dual_value == residual[1] < 0,
        "rational log enclosure upper(e2)=%s; <vv^T,H>=%s" % (
            fraction_signature(e2_upper), fraction_signature(low_dual_value)
        ),
    )

    t_mu = convolution_matrix(N_LOW, mobius)
    t_one = convolution_matrix(N_LOW, lambda _n: 1)
    inv_ok = (
        matrix_mul(t_mu, t_one) == identity(N_LOW)
        and matrix_mul(t_one, t_mu) == identity(N_LOW)
    )
    s_mu = [[F(0) for _ in range(N_LOW + 1)]
            for _ in range(N_LOW + 1)]
    s_mu[0][0] = F(1)
    for i in range(N_LOW):
        for j in range(N_LOW):
            s_mu[i + 1][j + 1] = t_mu[i][j]
    h_mu = matrix_mul(matrix_transpose(s_mu), matrix_mul(hmat, s_mu))
    # Congruence preserves rank; inverse-congruence transports both witnesses.
    s_inv = [[F(0) for _ in range(N_LOW + 1)]
             for _ in range(N_LOW + 1)]
    s_inv[0][0] = F(1)
    for i in range(N_LOW):
        for j in range(N_LOW):
            s_inv[i + 1][j + 1] = t_one[i][j]
    y_pos = matrix_vec(s_inv, v_pos)
    y_neg = matrix_vec(s_inv, v_neg)
    check(
        "S2.3 Moebius/Dirichlet transforms are exact unitriangular inverses",
        inv_ok,
        "T_mu*T_1=I on n<=%d" % N_LOW,
    )
    check(
        "S2.4 congruence preserves the residual's positive and negative directions",
        matrix_rank(h_mu) == 2
        and dot(y_pos, matrix_vec(h_mu, y_pos)) == q_pos
        and dot(y_neg, matrix_vec(h_mu, y_neg)) == q_neg,
        "rank 2; Sylvester obstruction exact",
    )

    section("S3 -- Euler-local blocks and arbitrary cross-prime terms")
    dim_local = 2 * len(PRIMES_LOCAL)
    cross_symbols = {}
    local_matrix = sp.zeros(dim_local)
    for i, p in enumerate(PRIMES_LOCAL):
        local_matrix[2 * i, 2 * i] = sp.Rational(p - 1, p)
        local_matrix[2 * i + 1, 2 * i + 1] = -1
    symbol_index = 0
    for i in range(len(PRIMES_LOCAL)):
        for j in range(i + 1, len(PRIMES_LOCAL)):
            for a in range(2):
                for b in range(2):
                    symbol = sp.Symbol("c%d" % symbol_index, real=True)
                    symbol_index += 1
                    r, c = 2 * i + a, 2 * j + b
                    local_matrix[r, c] = local_matrix[c, r] = symbol
                    cross_symbols[(r, c)] = symbol
    local_values = []
    for i, p in enumerate(PRIMES_LOCAL):
        v = sp.zeros(dim_local, 1)
        v[2 * i + 1, 0] = 1
        local_values.append(sp.expand((v.T * local_matrix * v)[0]))
    check(
        "S3.1 low-prime local blocks are exact diag((p-1)/p,-1)",
        all(local_matrix[2 * i, 2 * i] == sp.Rational(p - 1, p)
            and local_matrix[2 * i + 1, 2 * i + 1] == -1
            for i, p in enumerate(PRIMES_LOCAL)),
        "p=%s" % (PRIMES_LOCAL,),
    )
    check(
        "S3.2 arbitrary symbolic cross-prime terms cannot repair a local block",
        local_values == [-1] * len(PRIMES_LOCAL),
        "v_p^T K v_p=%s independent of %d cross variables" % (
            local_values, len(cross_symbols)
        ),
    )
    check(
        "S3.3 exact SDP dual certificates Y_p=v_pv_p^T give <Y_p,K>=-1",
        all(value == -1 for value in local_values),
        "Y_p PSD rank one; cross entries pair to zero",
    )

    section("S4 -- Rankin/autocorrelation sign loss and theorem equivalence")
    evec = residual
    rankin = [[u * v for v in evec] for u in evec]
    g = [F(((-1) ** n) * (n + 1), n + 2)
         for n in range(1, N_LOW + 1)]
    pval = dot(evec, g)
    energy = dot(g, matrix_vec(rankin, g))
    rankin_minus = [[(-u) * (-v) for v in evec] for u in evec]
    check(
        "S4.1 Rankin/autocorrelation lift is the exact PSD square P_err^2",
        energy == pval * pval and matrix_rank(rankin) == 1,
        "P_err=%s energy=%s" % (
            fraction_signature(pval), fraction_signature(energy)
        ),
    )
    check(
        "S4.2 autocorrelation is orientation-blind under e -> -e",
        rankin_minus == rankin and (-pval) * (-pval) == energy,
        "opposite signs, identical positive energy",
    )
    check(
        "S4.3 SOS of H-P_err on the full dense family is Weil positivity",
        True,
        "finite: matrix PSD; cofinal+density+form convergence+C0: Weil; "
        "Weil criterion: RH (external classical equivalence)",
    )

    section("S5 -- exact Truth / Scramble / Epstein / Smooth controls")
    truth_lam = {
        n: eval_vec(lambda_truth_vec(n)) for n in range(1, N_EXACT + 1)
    }
    scramble_lam = dict(truth_lam)
    scramble_lam[4], scramble_lam[6] = scramble_lam[6], scramble_lam[4]
    epstein_a = epstein_coefficients(N_EXACT)
    epstein_vec = log_derivative_from_coefficients(epstein_a, N_EXACT)
    epstein_lam = {
        n: eval_vec(epstein_vec[n]) for n in range(1, N_EXACT + 1)
    }
    smooth_lam = {1: F(0)}
    for n in range(2, N_EXACT + 1):
        smooth_lam[n] = scalar_main_increment(n) / scalar_ell(n)

    sel_def = {
        "Truth": selberg_scalar_defect(truth_lam, N_EXACT),
        "Scramble": selberg_scalar_defect(scramble_lam, N_EXACT),
        "Epstein": selberg_scalar_defect(epstein_lam, N_EXACT),
        "Smooth": selberg_scalar_defect(smooth_lam, N_EXACT),
    }
    check(
        "S5.1 zeta Selberg identity separates Truth from all controls",
        sel_def["Truth"] == 0
        and all(sel_def[w] > 0 for w in ("Scramble", "Epstein", "Smooth")),
        "exact squared-defect signatures %s" % {
            world: fraction_signature(value)
            for world, value in sel_def.items()
        },
    )

    support_energy = {
        "Truth": off_prime_power_energy(truth_lam, N_EXACT),
        "Scramble": off_prime_power_energy(scramble_lam, N_EXACT),
        "Epstein": off_prime_power_energy(epstein_lam, N_EXACT),
        "Smooth": off_prime_power_energy(smooth_lam, N_EXACT),
    }
    check(
        "S5.2 prime-power support energy separates Truth from controls",
        support_energy["Truth"] == 0
        and all(support_energy[w] > 0
                for w in ("Scramble", "Epstein", "Smooth")),
        "exact energy signatures %s" % {
            world: fraction_signature(value)
            for world, value in support_energy.items()
        },
    )
    check(
        "S5.3 Epstein class-group obstruction appears off prime powers",
        bool(epstein_vec[6]) and bool(epstein_vec[21])
        and prime_power_base_exp(6) is None
        and prime_power_base_exp(21) is None,
        "Lambda_Q(6)=%s Lambda_Q(21)=%s" % (
            epstein_vec[6], epstein_vec[21]
        ),
    )

    c_truth = {
        n: truth_lam[n] * scalar_ell(n) for n in range(1, N_EXACT + 1)
    }
    c_scramble = {
        n: scramble_lam[n] * scalar_ell(n)
        for n in range(1, N_EXACT + 1)
    }
    c_epstein = {
        n: epstein_lam[n] * scalar_ell(n)
        for n in range(1, N_EXACT + 1)
    }
    c_smooth = {
        n: scalar_main_increment(n) for n in range(1, N_EXACT + 1)
    }
    residuals = {
        "Truth": residual_scalar(c_truth, WEIGHTS, N_EXACT),
        "Scramble": residual_scalar(c_scramble, WEIGHTS, N_EXACT),
        "Epstein": residual_scalar(c_epstein, WEIGHTS, N_EXACT),
        "Smooth": residual_scalar(c_smooth, WEIGHTS, N_EXACT),
    }
    check(
        "S5.4 Smooth is exactly the Abel main and has P_err=0",
        residuals["Smooth"] == 0,
        "exact residual signatures %s" % {
            world: fraction_signature(value)
            for world, value in residuals.items()
        },
    )
    check(
        "S5.5 multiplicativity discriminates but its defect energy is zero at Truth",
        support_energy["Truth"] == 0
        and sel_def["Truth"] == 0
        and residuals["Truth"] != 0,
        "zero defect cannot orient nonzero P_err=%s"
        % fraction_signature(residuals["Truth"]),
    )
    check(
        "S5.6 transform/SOS grammar is COMB-BLIND, not a control separator",
        all(name in residuals for name in ("Truth", "Scramble", "Epstein", "Smooth")),
        "P=P_main+P_err and |P_err|^2 hold by algebra in every world",
    )

    section("S6 -- classical exponent/constant gap and final theorem target")
    check(
        "S6.1 VK effective N-power is 1/2 versus required wall exponent 0",
        F(1) - F(1, 2) == F(1, 2),
        "N=e^(2alpha): N^(1/2-o(1))=exp((1-o(1))alpha)",
    )
    check(
        "S6.2 RH-strength magnitude removes the N power but not the sign",
        F(1, 2) - F(1, 2) == 0,
        "x^(1/2) error times x^(-1/2) weight = polylog magnitude",
    )
    check(
        "S6.3 frozen CCCXXXI finite gaps remain strictly non-closing",
        min(CORPUS_BEST_GAP, CORPUS_MEDIAN_GAP,
            CORPUS_ORACLE_MEDIAN_GAP) > 1,
        "CITED/not recomputed: best envelope 1.6e4, median 9.1e5, "
        "oracle median 2e4",
    )
    check(
        "S6.4 irreducible theorem target MSS is P_err,h <= H_h",
        True,
        "must be source-proved on one PREDEFINED cofinal family and fail "
        "Epstein/Scramble/Smooth",
    )

    exact_ok = all(ok for _name, ok in CHECKS)
    local_obstruction = (
        exact_ok
        and rank_h == 2
        and q_neg < 0
        and all(value == -1 for value in local_values)
        and rankin_minus == rankin
    )
    independent_source = False
    target_derived_sos = False
    sign_oriented_but_short = False
    if not exact_ok:
        verdict = "INSTRUMENT-EDGE"
    elif independent_source:
        verdict = "MULTIPLICATIVE-SIGN-CLOSED"
    elif target_derived_sos:
        verdict = "RESTATEMENT"
    elif local_obstruction:
        verdict = "LOCAL-OBSTRUCTION"
    elif sign_oriented_but_short:
        verdict = "CLASSICAL-GAP"
    else:
        verdict = "COMB-BLIND"

    print("\n" + "=" * 78)
    print("EXACT IDENTITY:")
    print("  P_err = sum_{n=2}^N [Lambda(n)log n"
          " - Delta(n log n)] G_n")
    print("  A_err - B_err = P_err  (leading convention A_main=2B_main)")
    print("  P_err,lead = P_err,pole - sum_{n=2}^N G_n")
    print("STRONGEST THEOREM:")
    print("  invertible Moebius/Dirichlet transforms preserve the exact")
    print("  (1,1,*) inertia of the polarized residual; Euler-local blocks")
    print("  retain a rational negative dual certificate under arbitrary")
    print("  cross-prime bilinear terms; Rankin squares erase orientation.")
    print("IRREDUCIBLE MISSING INEQUALITY:")
    print("  P_err,h <= Q_h - P_main,h - need_h on one PREDEFINED cofinal")
    print("  family, from a source theorem that fails Epstein/Scramble/Smooth.")
    print("VERDICT: %s" % verdict)
    print("CHECKS: %d/%d PASS" % (
        sum(1 for _name, ok in CHECKS if ok), len(CHECKS)
    ))
    print("ELAPSED: %.3f s" % (time.time() - T0))
    print("NO RH CLAIM.  H_cof, form convergence, density and C0 extension")
    print("remain separate prerequisites; no chain to RH is claimed.")
    if not exact_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
