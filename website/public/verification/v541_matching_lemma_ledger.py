"""v541 -- RTF.GNS.LEDGER.01: matching lemma and transport ledger package.
The proof package of the discovery series T78--T85, consolidated into
ONE load-bearing module with every core check RECOMPUTED from scratch
(no citation of sandbox output).  Companion to HECKE.GEOM.RTF.01
(v538), RTF.GNS.WEIL.01 (v539) and RTF.GNS.AMP.01 (v540).

[E] (A) WINDOW PROOF OF THE MATCHING LEMMA (T78).  The matching lemma
    of the hybrid certificate recipe is PROVED exact-integer on
    [4, 10^6]: certificate 7*S(j) < 40*A(j) (i.e. rho_design*F(j) < 1
    with rho = 21/20) at EVERY atom j <= 10^6 -- full enumeration,
    exact int64 sieves with PROVEN no-overflow, big-integer recheck on
    tightest + random + extremal atoms, exact Fraction margin
    X = 1 - max rho*F and exact rho_crit > 21/20; the maximal-greedy
    identity (envelope = worst case over every target set M and every
    greedy weight system) verified by independent divisor loops.
    Structure laws at 0 tolerance: 8-LAW Theta(4n) = 8 Theta(n)
    (n <= 250000); SEED-TOWER Theta(4^a s f^2) = 8^a Theta(s)
    alpha_s(f) (all n <= 50000); psi w-table (exact rational 2-adic
    ladder, recursion w(a+1) = 9w(a) - 8w(a-1) sympy-exact); COHEN
    SEEDS Theta(s) = c*L(-1,chi_Delta) with ONE constant per class
    {1 mod 8: -48, 5 mod 8: -80, 3 mod 4: -8, even: -8} exact-rational
    on all squarefree s <= 2000; bracket Theta <= 2|psi| <= 3 Theta on
    the full 10^6 window.
[E] (B) TRANSPORT LEDGER CLOSES EXACTLY (T79).
    Q_Weil(h) = Q_cert(h) + Delta_arch(h) + Delta_2(h) with
    Delta_pole == 0 and Delta_conv == 0 as PROVEN IDENTITIES (sympy
    kernel collapse + quadrature < 1e-13; scale-invariance audit);
    ledger identity residual rel < 1e-10 on a >= 20-row battery of
    exact autocorrelations (measured ~1e-13); the odd-prime side of
    the full Weil functional equals the certified plus combination
    P_zeta^odd(h) = P_lin(g) = P_zeta(g_-) + P_zeta(g_+) EXACTLY
    (three-way, rel < 1e-12 on the 10-function catalogue).
[E] (C) SIGNED ENVELOPE IS CHARACTER-EXACT (T80).
    -psi = (chi_-4 + 1/4 chi_8 + 1/4 chi_-8) * Theta coefficient-exact
    on ALL odd n <= 50000 on BOTH independent builds (character system
    solved sympy-exact with coefficients (0, 1, 1/4, 1/4)); per-class
    identities psi = Theta on n = 2,3 mod 4, 2|psi| = 3 Theta on
    1 mod 8, 2|psi| = Theta on 5 mod 8 with 0 mismatches on 10^6; the
    signed window certificate 7*S_net < 40*A holds with 0 violations
    and a margin factor ~8.9x over the absolute one; confinement is a
    SET EQUALITY on 10^6: {zero-credit clash atoms} = {chi_-4-coherent
    odd composites}.
[E] (D) THE ARCHIMEDEAN TERM IS INTERNAL (T82).  The Legendre
    duplication bridge (2 pi)^{-s} Gamma(s) = (1/2) Gamma_R(s)
    Gamma_R(s+1) is sympy-exact and < 1e-30 on 6 complex points; the
    kernel identity k_zeta(t) = K_fam(t) - K_shift(t) holds POINTWISE
    (< 1e-25 on a 51-point grid + Gauss digamma closed-form anchor at
    t = 0); exponent-ladder partition {n+1/2} = {2n+1/2} u {2n+3/2}
    exact (Fractions); Delta_arch(h) = A_fam(h) - A_shift(h) on a
    10-row battery subset at rel < 1e-10 (three independent exact
    u-space routes, pinned against t-space digamma quadratures).
[E] (E) THE COHERENT CLASS IS CLOSED BY THE lambda-EQUIVARIANT
    CHANNEL (T81/T85).  The CM carrier g_lambda = Sum_a lambda_1(a)
    q^{N(a)} exists exactly in TWO INDEPENDENT ROUTES (Z[i] lattice
    sum of z^4 vs multiplicative Cornacchia reconstruction, 0
    mismatches n <= 10^4, imaginary parts == 0); Hecke CM laws exact
    (split T(p) recursion, inert vanishing c(p) = 0 / c(p^2) = p^4,
    ramified c(2^r) = (-4)^r); support(c_1) == {Z[i] norms} as a SET
    EQUALITY with c_1 /= 0 at every coherent atom; theta_3^2 == r_2
    exact on 10^6 (the mu4-glue core counts Z[i] ideals); the
    canonical phase mean mu_1(d) = c_1(d)/(c_0(d) d^2) in [-1, 1]
    exact (|c_1| <= c_0 d^2 integer-exact; ideal counts == r_2/4;
    ideal-average identity); the lambda-window certificate over ALL
    j <= 10^6: max 7|S_lambda|/(40A) strictly below the unlifted
    max 7 S_coh/(40A) < 1, with exact Fraction rechecks (integer c_1
    route) at the extremal and sampled atoms.
[C] (F) FRONTIER FACTS (window constants, declared all-n extension).
    The unlifted coherent chain (primorials of primes = 1 mod 4)
    crosses the constant-route budget at k* = 14 (exact Fractions;
    log10 N* ~ 23); the lambda-window margin is ~0.065 vs ~0.236
    unlifted (factor ~3.6); the absolute Robin/constant tail route
    misses by factor ~6.2 at J = 10^6 and diverges (Gronwall) -- the
    constant route closes nothing beyond the window (recorded, open).

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)  ONE classically-shaped OPEN lemma remains: the CORRELATED-
       CANCELLATION lemma on credit-rich NON-coherent tail atoms
       (uniform-in-(M, lambda) form only) -- provably-shaped is NOT a
       formal proof; the tail of the uniform matching lemma is typed
       open, not closed.
  (ii) I5 in ONE-FAMILY form -- Q_cert(h) + Delta_2(h) + A_fam(h)
       - A_shift(h) >= 0 -- is the single remaining TFPT-specific
       object; BY the closed ledger it is verbatim Q_Weil(h) >= 0,
       i.e. EQUIVALENT to Weil positivity <=> RH (Weil 1952).  This
       is an EQUIVALENCE TYPING, not a progress claim: no step toward
       proving I5 is made or implied anywhere in this module.

HONEST FENCES (load-bearing typing):
  * Classics named CLASSICAL: Gronwall 1913, Robin 1983 UNCONDITIONAL
    (the RH-equivalent criterion is NOT used), Cohen 1975 (H(2,d),
    generalised Bernoulli B_{2,chi}), Hecke 1918/1920
    (Grossencharacters, CM theta lifts, L(1,lambda) /= 0), Cornacchia,
    Fermat/Gauss two squares, Dirichlet characters / L(1,chi),
    Mertens-AP, Landau 1908, Legendre duplication / Gamma_C =
    Gamma_R(s)Gamma_R(s+1), Weil 1952 / Guinand 1948 / Bombieri
    explicit formula, Cauchy-Schwarz autocorrelation bound,
    Alaoglu-Erdos 1944, Shimura 1973 / Hecke T(p^2), Jacobi/Landen
    theta identities -- NEW is the compiler-native consolidation and
    the machine-checked window proofs / exact identities.
  * WINDOW PROOFS ARE WINDOW PROOFS: every proved statement carries
    its explicit window; all-n extensions of window constants are
    DECLARED classical typings (Cohen 1975); asymptotic frontier
    statements are declared extrapolations, typed [C].
  * NO RH-EVIDENCE LANGUAGE: value-side representability of the Weil
    cone only; the value->spectral transport (I5) is untouched; NOT
    "almost RH".
  * ZETA.HP.CARRIER untouched; NO marker upgrades of any pre-existing
    contract.
  * ZERO-FIREWALL: AST-checked; no zetazero; all prime sides are
    finite zero-free sums over prime powers; mpmath is used for
    jtheta/Gamma/digamma/erfc/quad only (no zeta values needed).

Status: [E] exact integer / Fraction / sympy identities, full-window
enumeration certificates, zero-free prime relations, and mpmath
identities at rel < 1e-25..1e-10 as stated; [C] frontier facts
(window constants with declared classical all-n extension).  Python;
Wolfram-mirrored (exact algebraic identities -- integer sieves, FFT
autocorrelations, Cornacchia tables and quadratures stay
Python-only), counted per GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/lemma_window_proof_probe.py        (T78)
  experiments/tfpt-discovery/transport_ledger_probe.py          (T79)
  experiments/tfpt-discovery/tail_correlation_lemma_probe.py    (T80)
  experiments/tfpt-discovery/recipe_coherent_avoidance_probe.py (T81)
  experiments/tfpt-discovery/heat_arch_probe.py                 (T82)
  experiments/tfpt-discovery/lambda_equivariant_design_probe.py (T85)
"""
from __future__ import annotations

import ast
import math
import time
from fractions import Fraction

import mpmath
import numpy as np
import sympy as sp

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
J_WIN = 1_000_000             # full-enumeration certificate window
N_FORM = 50_000               # structure-law / decomposition window
SEED_MAX = 2_000              # Cohen-seed scan window (squarefree s)
N_CFORM = 10_000              # exact CM-carrier coefficient window
N_JAC = 200_000               # Jacobi r_2/4 = sum chi_-4 window
RHO_NUM, RHO_DEN = 21, 20     # rho_design = 21/20 (T76..T85 frozen)
CERT_L, CERT_R = 7, 40        # rho/6 = 21/120 = 7/40  =>  7S < 40A
GUARD = 1e-9                  # float prefilter guard (>> 1e-15 error)
K_VEC = 64                    # hybrid sieve vectorisation cut
N_TIGHT = 200                 # tightest atoms rechecked big-integer
N_RAND = 64                   # random atoms rechecked big-integer
N_GREEDY = 200                # maximal-greedy identity sample
CHAIN_K_EXACT = 24            # exact-Fraction coherent-chain depth
ROBIN_C = 0.6483              # Robin 1983 unconditional (n >= 3)
EULER_GAMMA = 0.5772156649015329
ANCHOR_8K = (0.70, 0.75)      # T77 anchor rho*E(8000) = 0.724
MFACT_BAND = (8.5, 9.3)       # signed/absolute margin factor ~8.9
KSTAR_ANCHOR = 14             # coherent-chain crossing anchor
L10N_BAND = (22.0, 25.0)      # log10 N* ~ 23 anchor band
# ledger battery (T79 machinery, reduced row set >= 20)
N_GRID = 1 << 13
U_GRID = 14.0
DU = 2 * U_GRID / N_GRID
PADN = 4 * N_GRID
N_PP = 1_200_000              # prime-power window (zero-free sums)
T_ASYM = 40.0                 # digamma kernel: mpmath below, Stirling above
REL_LEDGER = 1e-10            # preregistered ledger residual target
REL_PRIME = 1e-12             # odd-prime three-way identity target
N_EXP_U = 600                 # T82 u-route series length
T_KERN_MAX = 60.0             # kernel-identity t-grid reach
N_KERN = 51                   # kernel-identity points (>= 50)
REL_ARCH_BAT = 1e-10          # T82 battery subset target
LN2 = math.log(2.0)
TH_KEY = (0, 2, 1, 2, 0, 0)   # Theta = th2(q2)^2 th3(q) th3(q2)^2
PSI_KEY = (0, 0, 1, 0, 4, 0)  # psi   = th3(q) th4(q)^4
TD_KEY = (0, 0, 2, 1, 2, 0)   # Theta+ = th3^2 th3(q2) th4^2 (Landen ref)
COH_HEAD = [1, 5, 13, 17, 25, 29, 37, 41, 53, 61, 65, 73, 85, 89, 97]
PI4 = math.pi / 4.0


# ---------------------------------------------------------------- helpers
def theta_pairs(kind: int, scale_q: int, order_t: int):
    """Sparse (exponent, coeff) list of a theta factor in t-units."""
    pairs = []
    if kind == 2:
        o = 1
        while scale_q * o * o <= order_t:
            pairs.append((scale_q * o * o, 2))
            o += 2
    else:
        pairs.append((0, 1))
        n = 1
        while 4 * scale_q * n * n <= order_t:
            c = 2 if kind == 3 else 2 * ((-1) ** n)
            pairs.append((4 * scale_q * n * n, c))
            n += 1
    return pairs


def sparse_mul(s: np.ndarray, pairs, order_t: int) -> np.ndarray:
    out = np.zeros(order_t + 1, dtype=np.int64)
    for e, c in pairs:
        if e == 0:
            out += c * s
        else:
            out[e:] += c * s[:-e]
    return out


def build_monomial(key, order_t: int) -> np.ndarray:
    a0, a2, b0, b2, c0, c2 = key
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    for _ in range(a0):
        s = sparse_mul(s, theta_pairs(2, 1, order_t), order_t)
    for _ in range(a2):
        s = sparse_mul(s, theta_pairs(2, 2, order_t), order_t)
    for _ in range(b0):
        s = sparse_mul(s, theta_pairs(3, 1, order_t), order_t)
    for _ in range(b2):
        s = sparse_mul(s, theta_pairs(3, 2, order_t), order_t)
    for _ in range(c0):
        s = sparse_mul(s, theta_pairs(4, 1, order_t), order_t)
    for _ in range(c2):
        s = sparse_mul(s, theta_pairs(4, 2, order_t), order_t)
    return s


def build_theta_q(J: int) -> np.ndarray:
    """Exact Theta build directly in q-units (pair enumeration for
    th2(q^2)^2, then th3(q) th3(q^2)^2 by int64 slice additions)."""
    omax = math.isqrt(2 * J) + 2
    odds = np.arange(1, omax, 2, dtype=np.int64)
    exps = ((odds[:, None] ** 2 + odds[None, :] ** 2) // 2).ravel()
    exps = exps[exps <= J]
    arr = np.bincount(exps, minlength=J + 1).astype(np.int64) * 4
    for scale in (1, 2, 2):
        out = arr.copy()
        n = 1
        while scale * n * n <= J:
            e = scale * n * n
            out[e:] += 2 * arr[: J + 1 - e]
            n += 1
        arr = out
    return arr


def build_psi_q(J: int) -> np.ndarray:
    """Exact psi = th3(q) th4(q)^4 build in q-units."""
    arr = np.zeros(J + 1, dtype=np.int64)
    arr[0] = 1
    for kind in (3, 4, 4, 4, 4):
        out = arr.copy()
        n = 1
        while n * n <= J:
            c = 2 if kind == 3 else 2 * ((-1) ** n)
            e = n * n
            out[e:] += c * arr[: J + 1 - e]
            n += 1
        arr = out
    return arr


def Theta_iy(y):
    q1 = mpmath.exp(-2 * mpmath.pi * y)
    q2 = q1 * q1
    return (mpmath.jtheta(2, 0, q2) ** 2 * mpmath.jtheta(3, 0, q1)
            * mpmath.jtheta(3, 0, q2) ** 2)


def Psi_iy(y):
    q1 = mpmath.exp(-2 * mpmath.pi * y)
    return mpmath.jtheta(3, 0, q1) * mpmath.jtheta(4, 0, q1) ** 4


def jacobi(a: int, n: int) -> int:
    """Jacobi symbol (a/n) for odd n > 0 (binary algorithm)."""
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def factorise(n: int, spf: np.ndarray):
    out = []
    while n > 1:
        p = int(spf[n])
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out


def divisors_from(fac):
    ds = [1]
    for p, e in fac:
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def upper_sqrt(frac: Fraction) -> Fraction:
    num, den = frac.numerator, frac.denominator
    r = Fraction(math.isqrt(num * 10 ** 24 // den) + 1, 10 ** 12)
    assert r * r >= frac
    return r


def exact_cmp(v1: int, n1: int, v2: int, n2: int) -> int:
    """sign of v1^2/n1^3 - v2^2/n2^3 in exact integers."""
    lhs = v1 * v1 * n2 ** 3
    rhs = v2 * v2 * n1 ** 3
    return (lhs > rhs) - (lhs < rhs)


def cornacchia(p: int):
    """Exact a^2 + b^2 = p for prime p = 1 mod 4; returns a > b >= 1."""
    c = 2
    while pow(c, (p - 1) // 2, p) != p - 1:
        c += 1
    x = pow(c, (p - 1) // 4, p)
    r0, r1 = p, x
    sq = math.isqrt(p)
    while r1 > sq:
        r0, r1 = r1, r0 % r1
    a = r1
    b2 = p - a * a
    b = math.isqrt(b2)
    if b * b != b2 or a * a + b * b != p:
        return None
    return (max(a, b), min(a, b))


def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gpow(z, e: int):
    out = (1, 0)
    base = z
    while e > 0:
        if e & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        e >>= 1
    return out


def dker(e: int, phi: float) -> float:
    """Dirichlet-kernel average D_e(phi) = Sum_{l<=e} cos((e-2l)phi)/(e+1)."""
    return sum(math.cos((e - 2 * lv) * phi) for lv in range(e + 1)) / (e + 1)


def ast_zero_firewall(src_path: str) -> bool:
    with open(src_path, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)
    zero_calls = []
    attr_hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr in (
                "zetazero", "nzeros", "second_sheet_zero",
            ):
                zero_calls.append(f.attr)
            if isinstance(f, ast.Name) and f.id in ("zetazero",):
                zero_calls.append(f.id)
        if isinstance(node, ast.Attribute) and node.attr in ("zetazero",):
            attr_hits.append(node.attr)
    return len(zero_calls) == 0 and len(attr_hits) == 0


# ---- T79 ledger machinery (h-side Weil kernels vs g-side linear kernels)
def h_fejer(u, a):
    return np.maximum(0.0, 1.0 - np.abs(u) / a)


def h_gauss(u, s):
    return np.exp(-0.5 * (u / s) ** 2)


def hhat_gauss(t, s):
    return s * math.sqrt(2 * math.pi) * np.exp(-0.5 * (s * t) ** 2)


# ---- T82 arch kernels + exact u-space routes
def Gamma_R(s):
    return mpmath.pi ** (-s / 2) * mpmath.gamma(s / 2)


def kern_zeta(t):
    return (mpmath.re(mpmath.digamma(mpmath.mpc(mpmath.mpf(1) / 4, t / 2)))
            - mpmath.log(mpmath.pi))


def kern_shift(t):
    return (mpmath.re(mpmath.digamma(mpmath.mpc(mpmath.mpf(3) / 4, t / 2)))
            - mpmath.log(mpmath.pi))


def kern_fam(t):
    return (2 * mpmath.re(mpmath.digamma(mpmath.mpc(mpmath.mpf(1) / 2, t)))
            - 2 * mpmath.log(2 * mpmath.pi))


def run():
    reset()
    mpmath.mp.dps = 30
    t0 = time.time()
    np.seterr(under="ignore")
    print("v541 RTF.GNS.LEDGER.01 -- matching lemma and transport ledger "
          "package (two NAMED limits as content)")

    # ============================================================ S0
    print("S0 -- AST zero-firewall + exact builds + full-window laws")
    check("S0.AST: no Riemann-zero / zetazero loaders in this module",
          ast_zero_firewall(__file__))

    t_b = time.time()
    Th = build_theta_q(J_WIN)
    Ps = build_psi_q(J_WIN)
    Pa = np.abs(Ps)
    t_q = time.time() - t_b
    t_b = time.time()
    ORDER_T = 4 * N_FORM
    _th_t = build_monomial(TH_KEY, ORDER_T)
    _ps_t = build_monomial(PSI_KEY, ORDER_T)
    _td_t = build_monomial(TD_KEY, ORDER_T)
    support_ok = all(
        not np.any(arr[r::4] != 0)
        for arr in (_th_t, _ps_t, _td_t) for r in (1, 2, 3)
    )
    Th_t = _th_t[0::4][: N_FORM + 1].copy()
    Ps_t = _ps_t[0::4][: N_FORM + 1].copy()
    Td_t = _td_t[0::4][: N_FORM + 1].copy()
    del _th_t, _ps_t, _td_t
    print(f"        q-unit builds O(q^{J_WIN}) in {t_q:.1f}s; independent "
          f"t-unit builds O(q^{N_FORM}) in {time.time() - t_b:.1f}s")
    agree_th = bool(np.array_equal(Th[: N_FORM + 1], Th_t))
    agree_ps = bool(np.array_equal(Ps[: N_FORM + 1], Ps_t))
    half = Td_t[0::2][: N_FORM // 2 + 1]
    landen_ok = bool(np.array_equal(half, Ps_t[: len(half)]))
    check("S0.build: independent q-unit (10^6) and t-unit (5*10^4) builds "
          f"agree coefficient-exactly (Theta {agree_th}, psi {agree_ps}); "
          f"t-support clean ({support_ok}); Landen Theta+(2m) = psi(m) "
          "coefficient-exact; heads a0(Theta)=0, Theta(1)=4, Theta >= 0; "
          "psi(0)=1, psi(1)=-6",
          agree_th and agree_ps and support_ok and landen_ok
          and int(Th[0]) == 0 and int(Th[1]) == 4 and bool(np.all(Th >= 0))
          and int(Ps[0]) == 1 and int(Ps[1]) == -6)

    anchor_ok = True
    for y_f, arr, fn in ((0.35, Th_t, Theta_iy), (0.6, Th_t, Theta_iy),
                         (0.35, Ps_t, Psi_iy), (0.6, Ps_t, Psi_iy)):
        x = math.exp(-2 * math.pi * y_f)
        with np.errstate(under="ignore"):
            ssum = float(np.sum(arr.astype(np.float64)
                                * x ** np.arange(N_FORM + 1,
                                                 dtype=np.float64)))
        jval = float(fn(mpmath.mpf(y_f)))
        if abs(ssum - jval) / abs(jval) >= 1e-12:
            anchor_ok = False
    check("S0.anchor: coefficient arrays == jtheta monomials on the "
          "imaginary axis (rel < 1e-12 on 4 anchors)",
          anchor_ok)

    n_all = np.arange(1, J_WIN + 1, dtype=np.int64)
    sgn_law = np.where((n_all % 4) <= 1, -1, 1).astype(np.int64)
    law_viol = int(np.sum(np.sign(Ps[1:]) != sgn_law))
    th_zero = int(np.sum(Th[1:] == 0))
    psi_zero = int(np.sum(Ps[1:] == 0))

    # primes + coherent mask + SPF (shared machinery)
    t_m = time.time()
    isp = np.ones(J_WIN + 1, dtype=bool)
    isp[:2] = False
    for p in range(2, math.isqrt(J_WIN) + 1):
        if isp[p]:
            isp[p * p:: p] = False
    primes_all = np.nonzero(isp)[0].astype(np.int64)
    p3 = primes_all[primes_all % 4 == 3]
    p1 = primes_all[primes_all % 4 == 1]
    coh = np.zeros(J_WIN + 1, dtype=bool)
    coh[1::2] = True
    for p in p3:
        coh[int(p):: int(p)] = False
    SPF = np.zeros(J_WIN + 1, dtype=np.int64)
    for p in primes_all:
        p = int(p)
        sl = SPF[p::p]
        SPF[p::p] = np.where(sl == 0, p, sl)
    SPF[1] = 1
    coh_head = [int(x) for x in np.nonzero(coh[:101])[0]]
    coh_psi_bad = int(np.sum(Ps[1:][coh[1:] & (n_all >= 5)] >= 0))
    print(f"        masks/SPF on 10^6 in {time.time() - t_m:.1f}s: "
          f"{len(primes_all)} primes ({len(p1)} split, {len(p3)} inert); "
          f"coherent atoms <= 10^6: {int(np.sum(coh[1:]))}")
    check(f"S0.law: T71 sign law sign psi(n) = (-1)^(floor(n/2)+1) with "
          f"{law_viol} violations on 10^6; Theta > 0 ({th_zero} zeros); "
          f"psi zero-free ({psi_zero} zeros); psi(n) < 0 at EVERY coherent "
          f"n >= 5 ({coh_psi_bad} exceptions); coherent-mask head == hand "
          f"list ({coh_head == COH_HEAD})",
          law_viol == 0 and th_zero == 0 and psi_zero == 0
          and coh_psi_bad == 0 and coh_head == COH_HEAD)

    # ============================================================ A
    print("A -- the window proof of the matching lemma (T78, recomputed)")
    n_q = J_WIN // 4
    law8_bad = int(np.sum(Th[4:: 4][: n_q] != 8 * Th[1: n_q + 1]))
    check(f"A.i (8-LAW): Theta(4n) = 8 Theta(n) integer-exact for ALL "
          f"n <= {n_q} ({law8_bad} mismatches) -- pure geometric U(4)-line "
          "of the level-8 Eisenstein form",
          law8_bad == 0)

    t_f = time.time()
    F_MAX = math.isqrt(N_FORM) + 1
    SIG3_TAB = [0] * (F_MAX + 1)
    for f in range(1, F_MAX + 1):
        SIG3_TAB[f] = sum(d ** 3 for d in divisors_from(factorise(f, SPF)))

    def alpha_tower(s: int, f: int) -> int:
        tot = 0
        for j in divisors_from(factorise(f, SPF)):
            sq = False
            m = j
            mu = 1
            while m > 1:
                p = int(SPF[m])
                if m % (p * p) == 0:
                    sq = True
                    break
                mu = -mu
                m //= p
            if sq:
                continue
            tot += mu * (jacobi(s, j) if j > 1 else 1) * j * SIG3_TAB[f // j]
        return tot

    form_bad = 0
    form_nontrivial = 0
    psi_bad = 0
    for n in range(1, N_FORM + 1):
        a = 0
        n1 = n
        while n1 % 4 == 0:
            n1 //= 4
            a += 1
        e = 0
        m = n1
        if m % 2 == 0:
            m //= 2
            e = 1
        D = 1
        f = 1
        mm = m
        while mm > 1:
            p = int(SPF[mm])
            c = 0
            while mm % p == 0:
                mm //= p
                c += 1
            if c % 2:
                D *= p
            f *= p ** (c // 2)
        s = (2 ** e) * D
        if a > 0 or f > 1:
            form_nontrivial += 1
        if (8 ** a) * int(Th[s]) * alpha_tower(s, f) != int(Th[n]):
            form_bad += 1
        pw = 8 ** a
        if n1 % 8 == 1:
            num, den = -(16 * pw + 5), 14
        elif n1 % 8 == 5:
            num, den = -(16 * pw - 9), 14
        else:
            num, den = 15 - 8 * pw, 7
        if den * int(Ps[n]) != num * int(Th[n1]):
            psi_bad += 1
    X_s, P_s, CHI_s = sp.symbols("X p chi")
    K_SER = 10
    sig3_sym = [sp.Integer(1)]
    for _k in range(1, K_SER + 1):
        sig3_sym.append(sp.expand(1 + P_s ** 3 * sig3_sym[-1]))
    alpha_sym = [sp.Integer(1)]
    for _k in range(1, K_SER + 1):
        alpha_sym.append(sp.expand(sig3_sym[_k]
                                   - CHI_s * P_s * sig3_sym[_k - 1]))
    S_m = sum(alpha_sym[k] * X_s ** k for k in range(K_SER + 1))
    R_m = sp.expand(S_m * (1 - X_s) * (1 - P_s ** 3 * X_s)
                    - (1 - CHI_s * P_s * X_s))
    euler_ok = all(sp.expand(R_m.coeff(X_s, k)) == 0
                   for k in range(K_SER + 1))
    x_s = sp.symbols("x", positive=True)
    W_FAMS = {
        "1(8)": -(16 * x_s + 5) / 14,
        "5(8)": -(16 * x_s - 9) / 14,
        "2,3(4)": (15 - 8 * x_s) / 7,
    }
    rec_ok = all(
        sp.simplify(w.subs(x_s, 8 * x_s) - 9 * w
                    + 8 * w.subs(x_s, x_s / 8)) == 0
        for w in W_FAMS.values()
    )
    first_ok = (W_FAMS["1(8)"].subs(x_s, 1) == sp.Rational(-3, 2)
                and W_FAMS["5(8)"].subs(x_s, 1) == sp.Rational(-1, 2)
                and W_FAMS["2,3(4)"].subs(x_s, 1) == 1)
    print(f"        structure-law pass over ALL n <= {N_FORM} in "
          f"{time.time() - t_f:.1f}s ({form_nontrivial} nontrivial points)")
    check(f"A.ii (SEED-TOWER + w-TABLE): Theta(4^a s f^2) = 8^a Theta(s) "
          f"alpha_s(f) integer-exact for ALL n <= {N_FORM} ({form_bad} "
          f"mismatches, {form_nontrivial} nontrivial >= 19000); psi "
          f"w-table 0-tolerance ({psi_bad} mismatches); local Euler "
          "factor Sum alpha(p^k) X^k = (1 - chi p X)/[(1-X)(1-p^3 X)] "
          f"sympy-exact ({euler_ok}); w-recursion w(a+1) = 9w(a) - 8w(a-1) "
          f"sympy-exact ({rec_ok}) with first steps -3/2 / -1/2 / +1 "
          f"({first_ok})",
          form_bad == 0 and form_nontrivial >= 19000 and psi_bad == 0
          and euler_ok and rec_ok and first_ok)

    t_s = time.time()

    def bernoulli_S2(delta: int) -> int:
        chi = np.zeros(delta, dtype=np.int64)
        chi[1] = 1
        for a in range(2, delta):
            p = int(SPF[a])
            if p == a:
                if delta % p == 0:
                    v = 0
                elif p == 2:
                    v = 1 if delta % 8 in (1, 7) else -1
                else:
                    v = jacobi(delta % p, p)
                chi[a] = v
            else:
                chi[a] = chi[p] * chi[a // p]
        aa = np.arange(delta, dtype=np.int64)
        return int(np.dot(chi, aa * aa))

    seed_bad = 0
    seed_counts = {"1(8)": 0, "5(8)": 0, "3(4)": 0, "even": 0}
    for s in range(2, SEED_MAX + 1):
        if any(e > 1 for _p, e in factorise(s, SPF)):
            continue
        if s % 4 == 1:
            delta = s
            cst = -48 if s % 8 == 1 else -80
            cls = "1(8)" if s % 8 == 1 else "5(8)"
        else:
            delta = 4 * s
            cst = -8
            cls = "3(4)" if s % 2 else "even"
        s2 = bernoulli_S2(delta)
        seed_counts[cls] += 1
        if Fraction(int(Th[s])) != cst * Fraction(-s2, 2 * delta):
            seed_bad += 1
    anchor1 = Fraction(int(Th[1])) == Fraction(-48) * Fraction(-1, 12)
    print(f"        Cohen seed scan s <= {SEED_MAX} in "
          f"{time.time() - t_s:.1f}s: "
          + ", ".join(f"{k}: {v}" for k, v in seed_counts.items()))
    check("A.iii (COHEN SEEDS): Theta(s) = c*L(-1,chi_Delta) with ONE "
          "exact-rational constant per class {1 mod 8: -48, 5 mod 8: -80, "
          f"3 mod 4: -8, even: -8}} on ALL squarefree 2 <= s <= {SEED_MAX} "
          f"({seed_bad} mismatches; all classes >= 50 populated: "
          f"{all(v >= 50 for v in seed_counts.values())}); d = 1 anchor "
          f"Theta(1) = -48 zeta(-1) = 4 ({anchor1}) -- Cohen 1975 "
          "H(2,d) = L(-1,chi_d), generalised Bernoulli, named classical",
          seed_bad == 0 and anchor1
          and all(v >= 50 for v in seed_counts.values()))

    brk_lo = int(np.sum(2 * Pa[1:] < Th[1:]))
    brk_hi = int(np.sum(2 * Pa[1:] > 3 * Th[1:]))
    check(f"A.iv (BRACKET): Theta(n) <= 2|psi(n)| <= 3 Theta(n) "
          f"integer-exact on ALL n <= {J_WIN} ({brk_lo}/{brk_hi} "
          "violations) -- the two coefficient systems are ONE Eisenstein "
          "object up to the rational w-table",
          brk_lo == 0 and brk_hi == 0)

    # ---- certificate sieves (T80 signed machinery; S78 = T78 absolute)
    t_v = time.time()
    A_ARR = np.zeros(J_WIN + 1, dtype=np.int64)
    A_ARR[1:] = n_all * Th[1:]
    A_F = A_ARR.astype(np.float64)
    SM = np.zeros(J_WIN + 1, dtype=np.int64)
    SP = np.zeros(J_WIN + 1, dtype=np.int64)
    CNT_M = np.zeros(J_WIN + 1, dtype=np.int32)
    CNT_P = np.zeros(J_WIN + 1, dtype=np.int32)
    d_all = np.arange(2, J_WIN + 1, dtype=np.int64)
    d_m = d_all[(d_all % 4 <= 1)]               # => d >= 4 automatically
    d_p = d_all[(d_all % 4 >= 2)]
    for k in range(2, K_VEC + 1):
        dv = d_m[d_m <= J_WIN // k]
        idx = k * dv
        SM[idx] += int(A_ARR[k]) * Pa[dv]
        CNT_M[idx] += 1
        dv = d_p[d_p <= J_WIN // k]
        idx = k * dv
        SP[idx] += int(A_ARR[k]) * Ps[dv]       # psi(d) > 0 on this class
        CNT_P[idx] += 1
    for d in d_m[d_m <= J_WIN // (K_VEC + 1)]:
        d = int(d)
        top = J_WIN // d
        SM[(K_VEC + 1) * d:: d] += A_ARR[K_VEC + 1: top + 1] * int(Pa[d])
        CNT_M[(K_VEC + 1) * d:: d] += 1
    for d in d_p[d_p <= J_WIN // (K_VEC + 1)]:
        d = int(d)
        top = J_WIN // d
        SP[(K_VEC + 1) * d:: d] += A_ARR[K_VEC + 1: top + 1] * int(Ps[d])
        CNT_P[(K_VEC + 1) * d:: d] += 1
    S_NET = SM - SP
    mask_dj = np.zeros(J_WIN + 1, dtype=bool)
    mask_dj[4:][(n_all[3:] % 4 <= 1)] = True
    S78 = SM.copy()
    S78[mask_dj] += 4 * Pa[mask_dj]             # add back d = j (A(1) = 4)
    CNT78 = CNT_M.copy()
    CNT78[mask_dj] += 1
    supp78 = CNT78[1:] > 0
    print(f"        budget + 4 signed clash sieves on {J_WIN} in "
          f"{time.time() - t_v:.1f}s ({len(d_m)} minus-class d, "
          f"{len(d_p)} plus-class d)")

    # no-overflow proof (exact integers, float-guarded products)
    Mpref = np.maximum.accumulate(A_ARR)
    ok_ov = True
    Tmax = 0
    for dv in (d_m, d_p):
        kk_top = (J_WIN // dv).astype(np.int64)
        prod_f = (Pa[dv].astype(np.float64)
                  * Mpref[kk_top].astype(np.float64))
        if not bool(np.all(prod_f < 2.0 ** 61)):
            ok_ov = False
        else:
            Tmax = max(Tmax, int(np.max(Pa[dv] * Mpref[kk_top])))
    cnt_max = max(int(CNT78.max()), int(CNT_P.max()))
    room = (cnt_max * Tmax < 2 ** 63
            and int(S78.max()) * CERT_L < 2 ** 63
            and int(A_ARR.max()) * CERT_R < 2 ** 63)

    def clash_parts_direct(j: int):
        sm = sp_ = 0
        for d in divisors_from(factorise(j, SPF)):
            if d < 2 or j // d < 2:
                continue
            a = int(A_ARR[j // d])
            if d % 4 <= 1:
                sm += a * int(Pa[d])
            else:
                sp_ += a * int(Ps[d])
        return sm, sp_

    def S78_direct(j: int) -> int:
        tot = 0
        for d in divisors_from(factorise(j, SPF)):
            if d >= 4 and d % 4 <= 1:
                tot += int(Pa[d]) * int(A_ARR[j // d])
        return tot

    ratio_abs = (CERT_L * S78[1:]).astype(np.float64) \
        / (CERT_R * A_F[1:])
    ratio_net = (CERT_L * S_NET[1:]).astype(np.float64) \
        / (CERT_R * A_F[1:])
    order = np.argsort(-ratio_abs)
    tight_idx = [int(i) + 1 for i in order[:N_TIGHT]]
    rng = np.random.default_rng(541)
    rand_idx = [int(j) for j in rng.choice(np.where(supp78)[0] + 1,
                                           size=N_RAND, replace=False)]
    extra_idx = [65, 1105, 32045, 5040, 55440, 554400, 720720]
    recheck = sorted(set(tight_idx + rand_idx + extra_idx))
    t_r = time.time()
    mism = 0
    for j in recheck:
        sm_d, sp_d = clash_parts_direct(j)
        if (S78_direct(j) != int(S78[j]) or sm_d != int(SM[j])
                or sp_d != int(SP[j]) or sm_d - sp_d != int(S_NET[j])):
            mism += 1
    print(f"        big-integer recheck of {len(recheck)} atoms in "
          f"{time.time() - t_r:.1f}s: {mism} mismatches")
    check("A.v (SIEVE INTEGRITY): no-overflow PROVEN in exact integers "
          f"(cnt_max*T_max < 2^63: {room}; term products < 2^61 "
          f"float-guarded: {ok_ov}); S78/SM/SP/S_net == independent "
          f"arbitrary-precision divisor sums on {len(recheck)} atoms "
          f"({mism} mismatches) incl. tightest + random + extremals",
          ok_ov and room and mism == 0)

    viol_abs = int(np.sum(CERT_L * S78[1:] >= CERT_R * A_ARR[1:]))
    n_clash = int(np.sum(supp78))
    x0 = float(np.max(ratio_abs))
    cand = np.where(ratio_abs >= x0 * (1.0 - GUARD))[0]
    j_abs = int(cand[0]) + 1
    for i in cand[1:]:
        j = int(i) + 1
        if int(S78[j]) * int(A_ARR[j_abs]) > int(S78[j_abs]) * int(A_ARR[j]):
            j_abs = j
    S_star = S78_direct(j_abs)
    rhoF_abs = Fraction(CERT_L * S_star, CERT_R * int(A_ARR[j_abs]))
    X_abs = 1 - rhoF_abs
    rho_crit = Fraction(6 * int(A_ARR[j_abs]), S_star)
    anch8k = float(np.max(ratio_abs[:8000]))
    print(f"        certificate: {viol_abs} violations over {n_clash} "
          f"clash atoms; max rhoF = {float(rhoF_abs):.6f} at j* = {j_abs}")
    print(f"        MARGIN X = {X_abs} = {float(X_abs):.9f}; rho_crit = "
          f"{float(rho_crit):.6f}; rho*E(8000) = {anch8k:.4f}")
    check(f"A.vi (THE WINDOW CERTIFICATE): 7 S(j) < 40 A(j) -- i.e. "
          f"rho_design*F(j) < 1 with rho = 21/20 -- at EVERY atom "
          f"1 <= j <= {J_WIN} ({viol_abs} violations over {n_clash} clash "
          f"atoms; full enumeration, exact integer comparison); exact "
          f"margin X = {float(X_abs):.6f} > 0 (Fraction recorded) at the "
          f"exact argmax j* = {j_abs}; rho_crit = {float(rho_crit):.4f} > "
          f"21/20 exact; T77 anchor rho*E(8000) = {anch8k:.4f} in "
          f"{ANCHOR_8K}",
          viol_abs == 0 and X_abs > 0
          and rho_crit > Fraction(RHO_NUM, RHO_DEN)
          and S_star == int(S78[j_abs])
          and ANCHOR_8K[0] < anch8k < ANCHOR_8K[1])

    t_g = time.time()
    greedy_pool = [int(j) for j in rng.choice(np.where(supp78)[0] + 1,
                                              size=N_GREEDY, replace=False)]
    greedy_pool[:1] = [j_abs]
    greedy_bad = 0
    for j in greedy_pool:
        tot = 0
        for m in divisors_from(factorise(j, SPF)):
            if m < 2:
                continue
            d = j // m
            if d >= 4 and int(Ps[d]) < 0:
                tot += int(A_ARR[m]) * int(Pa[d])
        if tot != int(SM[j]):
            greedy_bad += 1
    check("A.vii (IMPLICATION CHAIN): the maximal-greedy clash "
          "(lambda_m = (rho/6) m Theta(m) for ALL m >= 2) reproduces the "
          f"envelope numerator EXACTLY ({greedy_bad} mismatches on "
          f"{len(greedy_pool)} atoms, independent divisor loop, "
          f"{time.time() - t_g:.1f}s) -- the certificate proves the lemma "
          "UNIFORMLY in the target set M and the greedy weights "
          "(sign law => hits land on d = 0,1 mod 4, d >= 4; greedy law "
          "=> per-term majorisation; enumeration => rho F < 1)",
          greedy_bad == 0)

    # Robin tail typing (declared classical; the constant route is OPEN)
    t_rb = time.time()
    SIG1 = np.zeros(J_WIN + 1, dtype=np.int64)
    for d in range(1, J_WIN + 1):
        SIG1[d::d] += d
    n3 = n_all[2:].astype(np.float64)
    ll = np.log(np.log(n3))
    robin_rhs = math.e ** EULER_GAMMA * ll + ROBIN_C / ll
    slack = robin_rhs - SIG1[3:].astype(np.float64) / n3
    robin_ok = bool(np.all(slack > 0))
    n32 = n_all.astype(np.float64) ** 1.5
    r_th = Th[1:].astype(np.float64) / n32
    r_ps = Pa[1:].astype(np.float64) / n32

    def guarded_extreme(vals, ratio_f, mask, mode):
        r = np.where(mask, ratio_f, -np.inf if mode == "max" else np.inf)
        if mode == "max":
            v0 = float(np.max(r))
            cnd = np.where(r >= v0 * (1.0 - GUARD))[0]
        else:
            v0 = float(np.min(r))
            cnd = np.where(r <= v0 * (1.0 + GUARD))[0]
        best = int(cnd[0]) + 1
        for i in cnd[1:]:
            j = int(i) + 1
            c = exact_cmp(int(vals[j - 1]), j, int(vals[best - 1]), best)
            if (mode == "max" and c > 0) or (mode == "min" and c < 0):
                best = j
        return best, Fraction(int(vals[best - 1]) ** 2, best ** 3)

    all_mask = np.ones(J_WIN, dtype=bool)
    mask_res = (n_all % 4 <= 1) & (n_all >= 4)
    _nC1, C1_sq = guarded_extreme(Th[1:], r_th, all_mask, "max")
    _nC2r, C2r_sq = guarded_extreme(Pa[1:], r_ps, mask_res, "max")
    nc0, c0_sq = guarded_extreme(Th[1:], r_th, supp78, "min")
    pow4 = [4 ** a for a in range(0, 10) if 4 ** a <= J_WIN]
    c1_attain = all(int(Th[p]) ** 2 == 16 * p ** 3 for p in pow4)
    K_up = upper_sqrt(C1_sq * C2r_sq / (36 * c0_sq))
    RHO_F = Fraction(RHO_NUM, RHO_DEN)
    rhoK = RHO_F * K_up
    R_J = math.e ** EULER_GAMMA * math.log(math.log(J_WIN)) \
        + ROBIN_C / math.log(math.log(J_WIN))
    gap_abs = float(rhoK) * (R_J - 1.0)
    print(f"        Robin anchor pass in {time.time() - t_rb:.1f}s; "
          f"constants C1 = 4 exact ({c1_attain}), c0 = "
          f"{math.sqrt(float(c0_sq)):.4f} at j = {nc0}, K <= "
          f"{float(K_up):.4f}; tail factor rhoK (R(J)-1) = {gap_abs:.2f}")
    check("A.viii (TAIL TYPED OPEN): Robin 1983 UNCONDITIONAL anchor "
          f"sigma(n)/n < e^gamma loglog n + {ROBIN_C}/loglog n verified "
          f"on ALL 3 <= n <= {J_WIN} (consistency only; RH-equivalent "
          f"criterion NOT used); the constant route MISSES: rhoK*(R(J)-1) "
          f"= {gap_abs:.2f} >= 1 at J = 10^6 and diverges (Gronwall) -- "
          "the tail of the uniform lemma stays OPEN and is carried by "
          "the named limits (fences), not closed here",
          robin_ok and c1_attain and C1_sq == Fraction(16)
          and gap_abs > 1.0 and math.isfinite(gap_abs))

    # ============================================================ B
    print("B -- the transport ledger (T79, recomputed)")
    u_s = sp.symbols("u", real=True)
    xx_s = sp.symbols("xpos", positive=True)
    id_kernel = sp.expand(
        (2 * sp.cosh(sp.Rational(3, 2) * u_s)
         * (sp.exp(u_s / 2) + sp.exp(-u_s / 2))).rewrite(sp.exp)
        - (sp.exp(2 * u_s) + sp.exp(u_s) + sp.exp(-u_s) + sp.exp(-2 * u_s))
    )
    id_atom = sp.simplify(
        (xx_s + xx_s ** -2)
        - xx_s ** sp.Rational(-1, 2)
        * (xx_s ** sp.Rational(3, 2) + xx_s ** sp.Rational(-3, 2))
    )
    id_split = sp.simplify(
        sp.exp(sp.Rational(3, 2) * u_s) + sp.exp(-sp.Rational(3, 2) * u_s)
        - 2 * sp.cosh(sp.Rational(3, 2) * u_s)
    )
    psi_q = mpmath.digamma(mpmath.mpf(1) / 4)
    psi_q_cf = -mpmath.euler - mpmath.pi / 2 - 3 * mpmath.log(2)
    c2_cf = 2 * mpmath.log(2) * (1 + mpmath.sqrt(2))
    c2_sum = 2 * mpmath.log(2) * mpmath.nsum(
        lambda k: mpmath.mpf(2) ** (-k / 2), [1, mpmath.inf])
    check("B.i (KERNEL IDENTITIES + CONSTANTS): pole collapse "
          "m_Theta(u)(e^{u/2}+e^{-u/2}) = e^{2u}+e^u+e^{-u}+e^{-2u}, "
          "prime atom (n+n^{-2}) = n^{-1/2} m_Theta(log n), plus-split "
          "m_Theta = e^{3u/2}+e^{-3u/2} all sympy-exact; classical "
          "constants psi(1/4) = -gamma - pi/2 - 3 log 2 and c_2 = "
          "2 log 2 (1+sqrt 2) anchored < 1e-25 (Gauss digamma, geometric "
          "sum) -- Delta_pole == 0 and the L2 key observation ARE this "
          "algebra",
          id_kernel == 0 and id_atom == 0 and id_split == 0
          and abs(psi_q - psi_q_cf) < mpmath.mpf("1e-25")
          and abs(c2_cf - c2_sum) < mpmath.mpf("1e-25"))

    # prime-power tables (zero-free finite sums)
    t_tab = time.time()
    _is_p = np.ones(N_PP + 1, dtype=bool)
    _is_p[:2] = False
    for p in range(2, int(N_PP ** 0.5) + 1):
        if _is_p[p]:
            _is_p[p * p::p] = False
    _primes = np.nonzero(_is_p)[0]
    pp_odd_n, pp_odd_l = [], []
    for p in _primes:
        p = int(p)
        if p == 2:
            continue
        lp = math.log(p)
        q = p
        while q <= N_PP:
            pp_odd_n.append(q)
            pp_odd_l.append(lp)
            q *= p
    PPO_N = np.array(pp_odd_n, dtype=np.float64)
    PPO_U = np.log(PPO_N)
    PPO_LAM = np.array(pp_odd_l)
    PPO_MTH = PPO_N ** 1.5 + PPO_N ** -1.5
    PPO_W_WEIL = PPO_LAM * PPO_N ** -0.5
    PPO_W_LIN = PPO_LAM * (PPO_N + PPO_N ** -2.0)
    K2MAX = int(math.log(N_PP) / LN2)
    U2 = LN2 * np.arange(1, K2MAX + 1)
    W2 = LN2 * 2.0 ** (-0.5 * np.arange(1, K2MAX + 1))
    UCUT = math.log(N_PP)
    print(f"        odd prime-power table <= {N_PP}: {len(PPO_N)} atoms, "
          f"p=2 depth {K2MAX} in {time.time() - t_tab:.1f}s")

    CATALOGUE = []
    for a in (1.5, 2.0, 2.5, 3.0, 3.5):
        CATALOGUE.append((f"fejer a={a}", "fejer", float(a),
                          (lambda uu, aa=a: h_fejer(uu, aa)), float(a)))
    for s in (0.6, 0.8, 1.0, 1.2, 1.4):
        CATALOGUE.append((f"gauss s={s}", "gauss", float(s),
                          (lambda uu, ss=s: h_gauss(uu, ss)),
                          min(10.0 * float(s), 12.0)))

    def prime_odd_exact(h_fn, umax):
        m = PPO_U <= umax + 1e-12
        return 2.0 * float(np.sum(PPO_W_WEIL[m] * h_fn(PPO_U[m])))

    def prime_lin_exact(h_fn, umax):
        m = PPO_U <= umax + 1e-12
        g = h_fn(PPO_U[m]) / PPO_MTH[m]
        return 2.0 * float(np.sum(PPO_W_LIN[m] * g))

    def prime_legs_exact(h_fn, umax):
        m = PPO_U <= umax + 1e-12
        g = h_fn(PPO_U[m]) / PPO_MTH[m]
        leg_m = 2.0 * float(np.sum(PPO_LAM[m] * PPO_N[m] ** -2.0 * g))
        leg_p = 2.0 * float(np.sum(PPO_LAM[m] * PPO_N[m] * g))
        return leg_m, leg_p

    l2_ok = True
    max_l2 = 0.0
    for name, kind, par, h_fn, umax in CATALOGUE:
        p_odd = prime_odd_exact(h_fn, umax)
        p_lin = prime_lin_exact(h_fn, umax)
        leg_m, leg_p = prime_legs_exact(h_fn, umax)
        rel1 = abs(p_odd - p_lin) / max(abs(p_odd), 1e-30)
        rel2 = abs(p_lin - (leg_m + leg_p)) / max(abs(p_lin), 1e-30)
        max_l2 = max(max_l2, rel1, rel2)
        if rel1 > REL_PRIME or rel2 > REL_PRIME:
            l2_ok = False
    check("B.ii (ODD-PRIME MATCH): the odd-n prime side of the FULL Weil "
          "functional equals the certified plus combination EXACTLY -- "
          "P_zeta^odd(h) = P_lin(g) = P_zeta(g_-) + P_zeta(g_+), "
          f"g_+- = e^(+-3u/2) g (three-way, max rel {max_l2:.1e} < "
          f"{REL_PRIME:g} on 10/10 catalogue functions; zero-free finite "
          "sums) -- the prime side was never the wall",
          l2_ok)

    pole_ok = True
    max_pole = 0.0
    for name, kind, par, h_fn, umax in CATALOGUE:
        us = np.linspace(0.0, umax, 24001)
        hv = h_fn(us)
        kph = np.exp(0.5 * us) + np.exp(-0.5 * us)
        kpl = (np.exp(2 * us) + np.exp(us) + np.exp(-us) + np.exp(-2 * us))
        mth = np.exp(1.5 * us) + np.exp(-1.5 * us)
        pw = 2.0 * float(np.trapezoid(hv * kph, us))
        pl = 2.0 * float(np.trapezoid((hv / mth) * kpl, us))
        rel = abs(pw - pl) / max(abs(pw), 1e-30)
        max_pole = max(max_pole, rel)
        if rel > 1e-13:
            pole_ok = False
        if kind == "fejer":
            cf = 16.0 * (math.cosh(par / 2) - 1.0) / par
        else:
            cf = 2.0 * par * math.sqrt(2 * math.pi) * math.exp(par * par / 8)
        if abs(pw - cf) / abs(cf) > 1e-8:
            pole_ok = False
    check("B.iii (Delta_pole == 0): Pole_Weil(h) = Pole_lin(g) at "
          f"quadrature level (max rel {max_pole:.1e} < 1e-13 on 10/10; "
          "closed-form anchors < 1e-8) with the sympy-exact kernel "
          "collapse behind it -- an IDENTITY, not a small number",
          pole_ok)

    # arch double route (t-quadrature vs exact u-space series)
    def arch_u_gauss(sh):
        mpmath.mp.dps = 25
        sh_m = mpmath.mpf(sh)
        tot = mpmath.mpf(0)
        for n in range(N_EXP_U):
            b = 2 * n + mpmath.mpf(1) / 2
            I_n = (mpmath.sqrt(2 * mpmath.pi) * sh_m
                   * mpmath.exp(b * b * sh_m * sh_m / 2)
                   * mpmath.erfc(b * sh_m / mpmath.sqrt(2)))
            tot += mpmath.mpf(1) / (n + 1) - I_n
        Nq = N_EXP_U + mpmath.mpf(1) / 4
        tot += mpmath.digamma(Nq) - mpmath.digamma(N_EXP_U + 1)
        tot += -mpmath.polygamma(2, Nq) / (8 * sh_m ** 2)
        tot += mpmath.polygamma(4, Nq) / (128 * sh_m ** 4)
        res = float(-(mpmath.euler + mpmath.log(mpmath.pi)) + tot)
        mpmath.mp.dps = 30
        return res

    t_ak = time.time()
    ts_a = np.linspace(0.0, 15.0, 1501)
    K_CAT = np.array([
        float(mpmath.re(mpmath.digamma(mpmath.mpc(0.25, 0.5 * float(t)))))
        for t in ts_a
    ]) - math.log(math.pi)
    ar_ok = True
    max_ar = 0.0
    for sig in (0.6, 0.8, 1.0, 1.2):
        a_t = 2.0 * float(np.trapezoid(K_CAT * hhat_gauss(ts_a, sig),
                                       ts_a)) / (2 * math.pi)
        a_u = arch_u_gauss(sig)
        rel = abs(a_t - a_u) / max(abs(a_u), 1e-30)
        max_ar = max(max_ar, rel)
        if rel > 1e-8:
            ar_ok = False
    print(f"        arch double route in {time.time() - t_ak:.1f}s "
          f"(max rel {max_ar:.1e})")
    check("B.iv (ARCH DOUBLE-ROUTED): t-space digamma quadrature == "
          "u-space exponential-series representation -(gamma+log pi)h(0) "
          "+ Sum [h(0)/(n+1) - int h e^{-(2n+1/2)|u|}du] "
          f"(max rel {max_ar:.1e} < 1e-8 on 4 Gaussians; digamma series "
          "+ Poisson-kernel pair, classical) -- the external arch "
          "normalisation is pinned by two independent routes",
          ar_ok)

    # ---- the ledger battery (>= 20 exact autocorrelation rows)
    us_g = (np.arange(N_GRID) - N_GRID // 2) * DU

    def gauss_f(s):
        return np.exp(-0.5 * (us_g / s) ** 2)

    def bump_f(a, pw=2):
        return np.where(np.abs(us_g) < a, (1 - (us_g / a) ** 2) ** pw, 0.0)

    BAT = []
    for sig in (0.5, 0.8, 1.1):
        for om in (6, 10, 14, 18):
            BAT.append((f"gab s{sig} w{om}",
                        gauss_f(sig) * np.cos(om * us_g)))
    rng76 = np.random.default_rng(76)
    for Kmix in (2, 3):
        for _j in range(3):
            oms = np.sort(rng76.uniform(0.8, 14.0, Kmix))
            amps = rng76.uniform(0.4, 1.0, Kmix)
            sig = float(rng76.uniform(0.6, 1.2))
            BAT.append((f"mix K{Kmix}#{_j}",
                        gauss_f(sig) * sum(a * np.cos(o * us_g)
                                           for a, o in zip(amps, oms))))
    for a in (0.8, 1.5, 2.2):
        BAT.append((f"bump a{a}", bump_f(a)))
    for c in (0.75, 0.92):
        BAT.append((f"gcanc c{c}",
                    np.exp(-0.5 * us_g ** 2)
                    - c * np.exp(-0.5 * (us_g / 1.15) ** 2)))
    H5 = us_g ** 5 - 10 * us_g ** 3 + 15 * us_g
    BAT.append(("herm5", H5 * np.exp(-0.5 * us_g ** 2)))

    U_LAGS = np.arange(N_GRID) * DU
    KPH_LAG = np.exp(0.5 * U_LAGS) + np.exp(-0.5 * U_LAGS)
    MTH_LAG = np.exp(1.5 * U_LAGS) + np.exp(-1.5 * U_LAGS)
    KPL_LAG = (np.exp(2 * U_LAGS) + np.exp(U_LAGS)
               + np.exp(-U_LAGS) + np.exp(-2 * U_LAGS))
    DT_BAT = 2 * math.pi / (PADN * DU)
    T_BAT = DT_BAT * np.arange(2 * N_GRID + 1)
    W_BAT = np.full(len(T_BAT), 2.0)
    W_BAT[0] = 1.0
    W_BAT[-1] = 1.0
    t_kb = time.time()
    z_bat = 0.25 + 0.5j * T_BAT.astype(np.complex128)
    psi_asym = (np.log(z_bat) - 1.0 / (2 * z_bat)
                - 1.0 / (12 * z_bat ** 2) + 1.0 / (120 * z_bat ** 4)
                - 1.0 / (252 * z_bat ** 6))
    K_BAT = psi_asym.real - math.log(math.pi)
    n_mp = int(np.searchsorted(T_BAT, T_ASYM))
    for i in range(n_mp):
        K_BAT[i] = float(mpmath.re(mpmath.digamma(
            mpmath.mpc(0.25, 0.5 * float(T_BAT[i]))))) - math.log(math.pi)
    splice_rel = 0.0
    for i in (n_mp, n_mp + 200, len(T_BAT) - 1):
        ex = float(mpmath.re(mpmath.digamma(
            mpmath.mpc(0.25, 0.5 * float(T_BAT[i]))))) - math.log(math.pi)
        splice_rel = max(splice_rel, abs(K_BAT[i] - ex) / abs(ex))
    print(f"        battery arch kernel ({len(K_BAT)} pts, mpmath below "
          f"t={T_ASYM:g}, splice rel {splice_rel:.1e}) in "
          f"{time.time() - t_kb:.1f}s")

    def ledger_row(fv):
        F = np.fft.rfft(fv, PADN)
        acf = np.fft.irfft(np.abs(F) ** 2, PADN)[:N_GRID] * DU
        h0 = float(acf[0])
        v_full = acf / h0
        v = np.where(U_LAGS <= UCUT, v_full, 0.0)
        S = np.zeros(PADN)
        S[:N_GRID] = v
        S[PADN - N_GRID + 1:] = v[1:][::-1]
        hhat = DU * np.fft.rfft(S).real
        par = DT_BAT / (2 * math.pi) * float(np.dot(W_BAT, hhat))
        arch = DT_BAT / (2 * math.pi) * float(np.dot(W_BAT * K_BAT, hhat))
        pole_w = 2.0 * float(np.trapezoid(v * KPH_LAG, U_LAGS))
        g_lag = v / MTH_LAG
        pole_l = 2.0 * float(np.trapezoid(g_lag * KPL_LAG, U_LAGS))
        hp = np.interp(PPO_U, U_LAGS, v, right=0.0)
        gp = hp / PPO_MTH
        p_odd = 2.0 * float(np.dot(PPO_W_WEIL, hp))
        p_lin = 2.0 * float(np.dot(PPO_W_LIN, gp))
        h2 = np.interp(U2, U_LAGS, v, right=0.0)
        p_two = 2.0 * float(np.dot(W2, h2))
        q_cert = pole_l - p_lin
        d_pole = pole_w - pole_l
        q_weil = pole_w - (p_odd + p_two) + arch
        resid = q_weil - (q_cert + d_pole + arch - p_two)
        return dict(h0=h0, parseval=par, q_cert=q_cert, d_pole=d_pole,
                    d_arch=arch, d_two=-p_two, q_weil=q_weil, resid=resid,
                    pole_w=pole_w, maxabs=float(np.max(np.abs(v_full))))

    # pipeline validation on synthetic Gaussians (closed forms known)
    val_ok = True
    for sig in (0.5, 0.8):
        r = ledger_row(gauss_f(sig))
        sh = sig * math.sqrt(2.0)
        pole_cf = 2.0 * sh * math.sqrt(2 * math.pi) * math.exp(sh * sh / 8)
        arch_cf = arch_u_gauss(sh)
        rel_pole = abs(r["pole_w"] - pole_cf) / pole_cf
        rel_arch = abs(r["d_arch"] - arch_cf) / abs(arch_cf)
        rel_par = abs(r["parseval"] - 1.0)
        if rel_pole > 1e-9 or rel_arch > 1e-6 or rel_par > 1e-10:
            val_ok = False
    check("B.v (PIPELINE VALIDATED): synthetic Gaussian autocorrelations "
          "vs closed forms -- pole < 1e-9, arch (FFT spectrum + spliced "
          "digamma kernel) < 1e-6 vs the exact u-route, Parseval "
          f"(1/2pi) int hhat = h(0) < 1e-10; splice rel {splice_rel:.1e} "
          "< 1e-9",
          val_ok and splice_rel < 1e-9)

    t_bat = time.time()
    ROWS = []
    for name, fv in BAT:
        r = ledger_row(fv)
        r["name"] = name
        ROWS.append(r)
    res_rel_max = 0.0
    dpole_rel_max = 0.0
    maxabs_max = 0.0
    for r in ROWS:
        scale = max(1.0, abs(r["q_weil"]), abs(r["q_cert"]),
                    abs(r["pole_w"]))
        res_rel_max = max(res_rel_max, abs(r["resid"]) / scale)
        dpole_rel_max = max(dpole_rel_max,
                            abs(r["d_pole"]) / max(1.0, abs(r["pole_w"])))
        maxabs_max = max(maxabs_max, r["maxabs"])
    h0s = [r["h0"] for r in ROWS]
    # Delta_conv == 0: exact scale invariance of the normalised ledger
    conv_ok = True
    for name, fv in BAT[:3]:
        r1 = ledger_row(fv)
        r10 = ledger_row(10.0 * fv)
        for kkey in ("q_cert", "d_arch", "d_two", "q_weil"):
            if abs(r1[kkey] - r10[kkey]) > 1e-12 * max(1.0, abs(r1[kkey])):
                conv_ok = False
    print(f"        ledger battery: {len(ROWS)} rows in "
          f"{time.time() - t_bat:.1f}s; residual max rel "
          f"{res_rel_max:.1e}; Delta_pole max rel {dpole_rel_max:.1e}; "
          f"h0 range [{min(h0s):.3f}, {max(h0s):.3f}] "
          f"({max(h0s) / min(h0s):.0f}x)")
    check(f"B.vi (THE LEDGER CLOSES): Q_Weil = Q_cert + Delta_pole + "
          f"Delta_arch + Delta_2 + Delta_conv on {len(ROWS)} (>= 20) "
          "exact-autocorrelation battery rows with residual max rel "
          f"{res_rel_max:.1e} < {REL_LEDGER:g} (independent h-side Weil "
          f"kernels vs g-side linear kernels); Delta_pole rel <= "
          f"{dpole_rel_max:.1e} < 1e-10 (identity); Delta_conv == 0 "
          f"(exact 10x scale invariance {conv_ok}; no offset over a "
          f"{max(h0s) / min(h0s):.0f}x h0-mass range); Cauchy-Schwarz "
          f"|h| <= h(0) holds (max ratio {maxabs_max:.6f} <= 1+1e-9)",
          len(ROWS) >= 20 and res_rel_max < REL_LEDGER
          and dpole_rel_max < 1e-10 and conv_ok
          and maxabs_max <= 1.0 + 1e-9)

    # ============================================================ C
    print("C -- the signed envelope is character-exact (T80, recomputed)")
    m23 = (n_all % 4) >= 2
    m18 = (n_all % 8) == 1
    m58 = (n_all % 8) == 5
    bad_23 = int(np.sum(Ps[1:][m23] != Th[1:][m23]))
    bad_18 = int(np.sum(2 * Pa[1:][m18] != 3 * Th[1:][m18]))
    bad_58 = int(np.sum(2 * Pa[1:][m58] != Th[1:][m58]))
    check("C.i (PER-CLASS IDENTITIES on 10^6): psi = Theta on n = 2,3 "
          f"mod 4 ({bad_23} fails); 2|psi| = 3 Theta on 1 mod 8 "
          f"({bad_18} fails); 2|psi| = Theta on 5 mod 8 ({bad_58} fails) "
          "-- the credit class carries the FULL budget coefficient",
          bad_23 == 0 and bad_18 == 0 and bad_58 == 0)

    Mchar = sp.Matrix([
        [1, 1, 1, 1],
        [1, -1, -1, 1],
        [1, 1, -1, -1],
        [1, -1, 1, -1],
    ])
    target = sp.Matrix([sp.Rational(3, 2), -1, sp.Rational(1, 2), -1])
    coeffs = Mchar.solve(target)
    coeffs_ok = list(coeffs) == [0, 1, sp.Rational(1, 4),
                                 sp.Rational(1, 4)]
    res8 = n_all[: N_FORM] % 8
    eps4 = np.zeros(N_FORM, dtype=np.int64)
    eps4[res8 == 1] = 6
    eps4[res8 == 5] = 2
    eps4[(res8 == 3) | (res8 == 7)] = -4
    odd_mask = (n_all[: N_FORM] % 2) == 1
    dec_bad_q = int(np.sum(
        4 * (-Ps[1: N_FORM + 1][odd_mask]) != eps4[odd_mask]
        * Th[1: N_FORM + 1][odd_mask]))
    dec_bad_t = int(np.sum(
        4 * (-Ps_t[1:][odd_mask]) != eps4[odd_mask] * Th_t[1:][odd_mask]))
    check("C.ii (CHARACTER DECOMPOSITION): -psi(n) = [chi_-4 + 1/4 chi_8 "
          "+ 1/4 chi_-8](n) * Theta(n) -- i.e. 4(-psi) = [4 chi_-4 + "
          f"chi_8 + chi_-8] Theta -- on ALL odd n <= {N_FORM}: q-build "
          f"{dec_bad_q} mismatches, independent t-build {dec_bad_t} "
          "mismatches; character system solved sympy-exact with "
          f"coefficients (0, 1, 1/4, 1/4) ({coeffs_ok})",
          dec_bad_q == 0 and dec_bad_t == 0 and coeffs_ok)

    viol_net = int(np.sum(CERT_L * S_NET[1:] >= CERT_R * A_ARR[1:]))
    x0 = float(np.max(ratio_net))
    cand = np.where(ratio_net >= x0 * (1.0 - GUARD))[0]
    j_net = int(cand[0]) + 1
    for i in cand[1:]:
        j = int(i) + 1
        if int(S_NET[j]) * int(A_ARR[j_net]) \
                > int(S_NET[j_net]) * int(A_ARR[j]):
            j_net = j
    sm_d, sp_d = clash_parts_direct(j_net)
    rhoF_net = Fraction(CERT_L * (sm_d - sp_d),
                        CERT_R * int(A_ARR[j_net]))
    X_net = 1 - rhoF_net
    mfact = float(X_net) / float(X_abs)
    consist = bool(np.all(S_NET <= SM)) and bool(np.all(SM <= S78))
    print(f"        signed certificate: {viol_net} violations; max "
          f"rhoF_net = {float(rhoF_net):.6f} at j*_net = {j_net}; margin "
          f"factor X_net/X_abs = {mfact:.2f}")
    check(f"C.iii (SIGNED CERTIFICATE): 7 S_net(j) < 40 A(j) at EVERY "
          f"atom j <= {J_WIN} ({viol_net} violations; consistency "
          f"S_net <= S- <= S_abs: {consist}); exact signed margin "
          f"X_net = {float(X_net):.4f} -- factor {mfact:.2f} in "
          f"{MFACT_BAND} over the absolute margin",
          viol_net == 0 and consist
          and MFACT_BAND[0] < mfact < MFACT_BAND[1]
          and sm_d - sp_d == int(S_NET[j_net]))

    pred_zero = (CNT_P[1:] == 0) & (CNT_M[1:] > 0)
    rhs_coh = coh[1:] & (n_all > 1) & (~isp[1:])
    set_eq = bool(np.array_equal(pred_zero, rhs_coh))
    sp_zero_on_coh = int(np.sum(SP[1:][pred_zero] != 0))
    check("C.iv (CONFINEMENT SET EQUALITY): {zero-credit clash atoms} = "
          "{chi_-4-coherent odd composites} -- exact set equality on the "
          f"FULL 10^6 window ({set_eq}); S+ == 0 on the class "
          f"({sp_zero_on_coh} exceptions): the tail obstruction is "
          "CHARACTERISED, not diffuse (Landau 1908 density colour, "
          "named classical)",
          set_eq and sp_zero_on_coh == 0)

    # ============================================================ D
    print("D -- the archimedean term is internal (T82, recomputed)")
    z_s = sp.symbols("z")
    dup_sym = sp.simplify(
        sp.expand_func(sp.gamma(2 * z_s))
        - 2 ** (2 * z_s - 1) / sp.sqrt(sp.pi) * sp.gamma(z_s)
        * sp.gamma(z_s + sp.Rational(1, 2))
    )
    mpmath.mp.dps = 40
    dup_pts = [mpmath.mpc(a, b) for a, b in
               ((0.31, 0.7), (1.2, -2.3), (0.5, 5.0), (2.7, 0.4),
                (0.25, 11.0), (3.9, -7.7))]
    max_dup = mpmath.mpf(0)
    max_fac = mpmath.mpf(0)
    for zz in dup_pts:
        lhs = mpmath.gamma(2 * zz)
        rhs = (2 ** (2 * zz - 1) / mpmath.sqrt(mpmath.pi)
               * mpmath.gamma(zz) * mpmath.gamma(zz + mpmath.mpf(1) / 2))
        max_dup = max(max_dup, abs(lhs - rhs) / abs(lhs))
        s2 = 2 * zz
        lhs2 = (2 * mpmath.pi) ** (-s2) * mpmath.gamma(s2)
        rhs2 = mpmath.mpf(1) / 2 * Gamma_R(s2) * Gamma_R(s2 + 1)
        max_fac = max(max_fac, abs(lhs2 - rhs2) / abs(lhs2))
    mpmath.mp.dps = 30
    check("D.i (DUPLICATION BRIDGE): Legendre duplication Gamma(2z) = "
          "2^{2z-1} pi^{-1/2} Gamma(z) Gamma(z+1/2) sympy-exact "
          f"({dup_sym} == 0) and mpmath max rel {mpmath.nstr(max_dup, 3)} "
          "< 1e-30; the bridge (2 pi)^{-s} Gamma(s) = (1/2) Gamma_R(s) "
          f"Gamma_R(s+1) max rel {mpmath.nstr(max_fac, 3)} < 1e-30 on 6 "
          "complex points (= Gamma_C = Gamma_R Gamma_R, classical)",
          dup_sym == 0 and max_dup < mpmath.mpf("1e-30")
          and max_fac < mpmath.mpf("1e-30"))

    t_grid = [mpmath.mpf(T_KERN_MAX) * k / (N_KERN - 1)
              for k in range(N_KERN)]
    max_kid = mpmath.mpf(0)
    for t in t_grid:
        v = kern_fam(t) - kern_shift(t) - kern_zeta(t)
        max_kid = max(max_kid, abs(v))
    psi14 = -mpmath.euler - mpmath.pi / 2 - 3 * mpmath.log(2)
    psi12 = -mpmath.euler - 2 * mpmath.log(2)
    psi34 = -mpmath.euler + mpmath.pi / 2 - 3 * mpmath.log(2)
    anchor0 = abs((2 * psi12 - 2 * mpmath.log(2 * mpmath.pi))
                  - (psi34 - mpmath.log(mpmath.pi))
                  - (psi14 - mpmath.log(mpmath.pi)))
    check(f"D.ii (KERNEL IDENTITY POINTWISE): K_fam(t) - K_shift(t) = "
          f"k_zeta(t) on {N_KERN} points t in [0, {T_KERN_MAX:g}] "
          f"(max abs {mpmath.nstr(max_kid, 3)} < 1e-25); closed-form "
          "anchor at t = 0 via Gauss digamma values psi(1/4), psi(1/2), "
          f"psi(3/4) (|Delta| = {mpmath.nstr(anchor0, 3)} < 1e-30)",
          max_kid < mpmath.mpf("1e-25")
          and anchor0 < mpmath.mpf("1e-30"))

    fam_ladder = {Fraction(n, 1) + Fraction(1, 2) for n in range(200)}
    zeta_ladder = {Fraction(2 * n, 1) + Fraction(1, 2) for n in range(100)}
    shift_ladder = {Fraction(2 * n, 1) + Fraction(3, 2)
                    for n in range(100)}
    part_ok = (zeta_ladder | shift_ladder == fam_ladder
               and not (zeta_ladder & shift_ladder))
    check("D.iii (EXPONENT-LADDER PARTITION): the family u-space ladder "
          "{n+1/2} is the DISJOINT union of the zeta-ladder {2n+1/2} and "
          "the shift-ladder {2n+3/2} (200 rungs, exact Fractions) -- the "
          "duplication formula seen as a partition of heat exponents",
          part_ok)

    mpmath.mp.dps = 25
    GAMMA_E = mpmath.euler
    LOG_PI = mpmath.log(mpmath.pi)
    LOG_2PI = mpmath.log(2 * mpmath.pi)
    SQ2 = mpmath.sqrt(2)
    SQPI2 = mpmath.sqrt(mpmath.pi / 2)

    def I_fejer(b, a):
        b = mpmath.mpf(b)
        return 2 * (1 / b - (1 - mpmath.exp(-a * b)) / (a * b * b))

    def I_modgauss(b, sig, om):
        c = mpmath.mpc(b, -om)
        return 2 * mpmath.re(sig * SQPI2
                             * mpmath.exp(c * c * sig * sig / 2)
                             * mpmath.erfc(c * sig / SQ2))

    def arch_route(I_fn, derivs, cpar, alpha, gam0, const, nterms):
        h0, h1, h2, h3, h4, h6 = [mpmath.mpf(d) for d in derivs]
        alpha = mpmath.mpf(alpha)
        gam0 = mpmath.mpf(gam0)
        tot = mpmath.mpf(0)
        for n in range(nterms):
            b = alpha * (n + gam0)
            tot += cpar * h0 / (n + 1) - I_fn(b)
        Nq = nterms + gam0
        tot += cpar * h0 * (mpmath.digamma(Nq)
                            - mpmath.digamma(nterms + 1))
        tot += -2 * h1 / alpha ** 2 * mpmath.polygamma(1, Nq)
        tot += h2 / alpha ** 3 * mpmath.polygamma(2, Nq)
        tot += -h3 / (3 * alpha ** 4) * mpmath.polygamma(3, Nq)
        tot += h4 / (12 * alpha ** 5) * mpmath.polygamma(4, Nq)
        tot += h6 / (360 * alpha ** 7) * mpmath.polygamma(6, Nq)
        return const + tot

    def routes_for_row(kind, par, nterms=N_EXP_U):
        if kind == "fejer":
            a = mpmath.mpf(par)
            I_fn = lambda b: I_fejer(b, a)
            derivs = (1, -1 / a, 0, 0, 0, 0)
        else:
            sig, om = [mpmath.mpf(x) for x in par]
            I_fn = lambda b: I_modgauss(b, sig, om)
            h2 = -(1 / sig ** 2 + om ** 2)
            h4 = 3 / sig ** 4 + 6 * om ** 2 / sig ** 2 + om ** 4
            h6 = -(15 / sig ** 6 + 45 * om ** 2 / sig ** 4
                   + 15 * om ** 4 / sig ** 2 + om ** 6)
            derivs = (1, 0, h2, 0, h4, h6)
        r_z = arch_route(I_fn, derivs, 1, 2, mpmath.mpf(1) / 4,
                         -(GAMMA_E + LOG_PI), nterms)
        r_f = arch_route(I_fn, derivs, 2, 1, mpmath.mpf(1) / 2,
                         -2 * (GAMMA_E + LOG_2PI), nterms)
        r_s = arch_route(I_fn, derivs, 1, 2, mpmath.mpf(3) / 4,
                         -(GAMMA_E + LOG_PI), nterms)
        return r_z, r_f, r_s

    def arch_quad(sig, kern):
        sig = mpmath.mpf(sig)
        hhat = lambda t: sig * mpmath.sqrt(2 * mpmath.pi) \
            * mpmath.exp(-sig * sig * t * t / 2)
        return mpmath.quad(lambda t: hhat(t) * kern(t),
                           [0, 4, 12, 40]) / mpmath.pi

    t_rt = time.time()
    pin_ok = True
    max_pin = 0.0
    for sig in (0.8, 1.2):
        r_z, r_f, r_s = routes_for_row("gauss", (sig, 0.0))
        for rv, kern in ((r_z, kern_zeta), (r_f, kern_fam),
                         (r_s, kern_shift)):
            qv = arch_quad(sig, kern)
            rel = float(abs(rv - qv) / abs(qv))
            max_pin = max(max_pin, rel)
            if rel > 1e-8:
                pin_ok = False
    ARCH_BAT = ([(f"fejer a={a}", "fejer", a) for a in (1.5, 2.5, 3.0,
                                                        3.5)]
                + [(f"gauss s={s}", "gauss", (s, 0.0))
                   for s in (0.6, 1.0, 1.4)]
                + [(f"modg s={s} w={w}", "gauss", (s, w))
                   for s, w in ((0.8, 2.0), (0.8, 8.0), (1.2, 5.0))])
    bat_ok = True
    max_bat = 0.0
    for name, kind, par in ARCH_BAT:
        r_z, r_f, r_s = routes_for_row(kind, par)
        rel = float(abs(r_f - r_s - r_z)
                    / max(abs(r_z), abs(r_f), abs(r_s)))
        max_bat = max(max_bat, rel)
        if rel > REL_ARCH_BAT:
            bat_ok = False
    mpmath.mp.dps = 30
    print(f"        arch routes in {time.time() - t_rt:.1f}s: pins "
          f"{max_pin:.1e}, battery subset {max_bat:.1e}")
    check(f"D.iv (Delta_arch = A_fam - A_shift): battery subset "
          f"{len(ARCH_BAT)}/10 rows (Fejer/Gauss/modulated-Gauss) with "
          f"max rel {max_bat:.1e} < {REL_ARCH_BAT:g} via three "
          "independent exact u-space routes (disjoint exponent ladders "
          "{2n+1/2} / {n+1/2} / {2n+3/2}; digamma series + Poisson pair "
          "+ Watson tails); routes pinned vs independent t-quadratures "
          f"(max rel {max_pin:.1e} < 1e-8 on 2 Gaussians x 3 kernels) "
          "-- the T79 arch term IS the internal family Gamma-structure "
          "minus the odd-Gaussian duplication complement",
          bat_ok and pin_ok and len(ARCH_BAT) >= 10)

    # ============================================================ E
    print("E -- the lambda-equivariant channel (T81/T85, recomputed)")
    t_c = time.time()
    p1_list = [int(p) for p in p1]
    A_arr = np.zeros(len(p1_list), dtype=np.int64)
    B_arr = np.zeros(len(p1_list), dtype=np.int64)
    corn_fail = 0
    for i, p in enumerate(p1_list):
        ab = cornacchia(p)
        if ab is None:
            corn_fail += 1
            continue
        A_arr[i], B_arr[i] = ab
    norm_ok = bool(np.all(A_arr * A_arr + B_arr * B_arr == p1))
    order_ok = bool(np.all(A_arr > B_arr)) and bool(np.all(B_arr >= 1))
    gcd_ok = bool(np.all(np.gcd(A_arr, B_arr) == 1))
    THETA = np.arctan2(B_arr.astype(np.float64),
                       A_arr.astype(np.float64))
    PH1 = 4.0 * THETA
    COS1 = np.cos(PH1)
    PIDX = np.full(J_WIN + 1, -1, dtype=np.int32)
    PIDX[p1] = np.arange(len(p1_list), dtype=np.int32)
    print(f"        Cornacchia over {len(p1_list)} split primes <= 10^6 "
          f"in {time.time() - t_c:.1f}s")
    check(f"E.i (CORNACCHIA EXACT): p = a^2 + b^2 at EVERY split prime "
          f"<= 10^6 ({corn_fail} fails; norms {norm_ok}, a > b >= 1 "
          f"{order_ok}, gcd = 1 {gcd_ok}) -- the exact phase material of "
          "the design (Fermat/Gauss two squares + Cornacchia descent, "
          "named classical)",
          corn_fail == 0 and norm_ok and order_ok and gcd_ok)

    # r2 = theta3^2 on 10^6 (lattice count) + Jacobi on 2*10^5
    t_t = time.time()
    avf = np.arange(-1000, 1001, dtype=np.int64)
    NNf = (avf[:, None] ** 2 + avf[None, :] ** 2).ravel()
    r2 = np.bincount(NNf[NNf <= J_WIN],
                     minlength=J_WIN + 1).astype(np.int64)
    th3 = np.zeros(J_WIN + 1, dtype=np.int64)
    th3[0] = 1
    n = 1
    while n * n <= J_WIN:
        th3[n * n] = 2
        n += 1
    th3sq = th3.copy()
    n = 1
    while n * n <= J_WIN:
        e = n * n
        th3sq[e:] += 2 * th3[: J_WIN + 1 - e]
        n += 1
    theta_eq = bool(np.array_equal(th3sq, r2))
    RS = np.zeros(N_JAC + 1, dtype=np.int64)
    for d in range(1, N_JAC + 1, 2):
        RS[d::d] += 1 if d % 4 == 1 else -1
    jac_bad = int(np.sum(4 * RS[1:] != r2[1: N_JAC + 1]))
    print(f"        theta3^2 == r2 lattice count in "
          f"{time.time() - t_t:.1f}s")

    # g_lambda: two independent exact routes
    def c_recon(nrm: int, k4: int) -> int:
        prod = 1
        for p, e in factorise(nrm, SPF):
            if p == 2:
                prod *= (-4) ** ((k4 // 4) * e)
            elif p % 4 == 3:
                if e % 2 == 1:
                    return 0
                prod *= p ** (k4 * (e // 2))
            else:
                i = int(PIDX[p])
                pi4 = gpow((int(A_arr[i]), int(B_arr[i])), k4)
                pib = (pi4[0], -pi4[1])
                lre = 0
                lim = 0
                for j in range(e + 1):
                    t = gmul(gpow(pi4, j), gpow(pib, e - j))
                    lre += t[0]
                    lim += t[1]
                assert lim == 0
                prod *= lre
        return prod

    t_c2 = time.time()
    C1E = [0] * (N_CFORM + 1)
    I1E = [0] * (N_CFORM + 1)
    ICNT = np.zeros(N_CFORM + 1, dtype=np.int64)
    IAVG = np.zeros(N_CFORM + 1)
    amax = math.isqrt(N_CFORM)
    for a in range(1, amax + 1):
        for b in range(0, amax + 1):
            nrm = a * a + b * b
            if nrm > N_CFORM:
                break
            z4 = gpow((a, b), 4)
            C1E[nrm] += z4[0]
            I1E[nrm] += z4[1]
            IAVG[nrm] += math.cos(4.0 * math.atan2(b, a))
            ICNT[nrm] += 1
    imag_ok = all(v == 0 for v in I1E)
    rec_bad = sum(1 for nrm in range(1, N_CFORM + 1)
                  if C1E[nrm] != c_recon(nrm, 4))
    hecke_bad = 0
    inert_bad = 0
    ram_bad = 0
    for p in primes_all[primes_all <= N_CFORM]:
        p = int(p)
        chi = 0 if p == 2 else (1 if p % 4 == 1 else -1)
        r = 1
        while p ** (r + 1) <= N_CFORM:
            lhs = C1E[p ** (r + 1)]
            prev = C1E[p ** (r - 1)] if r >= 1 else 1
            if lhs != C1E[p] * C1E[p ** r] - chi * (p ** 4) * prev:
                hecke_bad += 1
            r += 1
        if p % 4 == 3:
            if C1E[p] != 0:
                inert_bad += 1
            if p * p <= N_CFORM and C1E[p * p] != p ** 4:
                inert_bad += 1
        if p == 2:
            r = 1
            while 2 ** r <= N_CFORM:
                if C1E[2 ** r] != (-4) ** r:
                    ram_bad += 1
                r += 1
    print(f"        g_lambda coefficients to n = {N_CFORM} (two routes) "
          f"in {time.time() - t_c2:.1f}s; head c1[1..8] = {C1E[1:9]}")
    check("E.ii (CM CARRIER, TWO ROUTES): g_lambda = Sum_a lambda_1(a) "
          "q^{N(a)} -- integer Z[i]-lattice sum of z^4 == multiplicative "
          f"Cornacchia reconstruction on ALL n <= {N_CFORM} ({rec_bad} "
          f"mismatches); imaginary parts == 0 ({imag_ok}); CM laws "
          f"exact: split T(p) recursion ({hecke_bad} fails), inert "
          f"c(p) = 0 / c(p^2) = p^4 ({inert_bad} fails), ramified "
          f"c(2^r) = (-4)^r ({ram_bad} fails) -- conductor-(1) "
          "Grossencharacter of Q(i), Hecke 1918, named classical",
          rec_bad == 0 and imag_ok and hecke_bad == 0
          and inert_bad == 0 and ram_bad == 0)

    supp_eq_bad = 0
    coh_nz_bad = 0
    icnt_bad = 0
    avg_bad = 0
    bound_bad = 0
    for nn in range(1, N_CFORM + 1):
        is_norm = True
        for p, e in factorise(nn, SPF):
            if p % 4 == 3 and e % 2 == 1:
                is_norm = False
                break
        if (C1E[nn] != 0) != is_norm:
            supp_eq_bad += 1
        if coh[nn] and C1E[nn] == 0:
            coh_nz_bad += 1
        if int(r2[nn]) != 0:
            if int(ICNT[nn]) != int(r2[nn]) // 4:
                icnt_bad += 1
            if abs(float(nn) ** 2 * IAVG[nn] - C1E[nn]) \
                    > 1e-9 * max(1.0, abs(C1E[nn])):
                avg_bad += 1
            if 4 * abs(C1E[nn]) > int(r2[nn]) * nn * nn:
                bound_bad += 1
    c1_min = min(C1E[1:])
    check("E.iii (CARRIER + CANONICAL WEIGHT): support(c_1) == "
          "{Z[i]-norms: 3-mod-4 part a perfect square} -- set equality "
          f"({supp_eq_bad} mismatches on 1..{N_CFORM}); c_1 /= 0 at "
          f"EVERY coherent atom ({coh_nz_bad} exceptions); theta_3^2 == "
          f"r_2 EXACT on 0..10^6 ({theta_eq}) and r_2/4 = "
          f"Sum_{{d|n}} chi_-4(d) with {jac_bad} mismatches on "
          f"1..{N_JAC} (Jacobi, classical); ideal counts == r_2/4 exact "
          f"({icnt_bad} fails); ideal-average identity d^2 * "
          f"Sum Re lambda_1 == c_1 ({avg_bad} fails); |c_1(d)| <= "
          f"c_0(d) d^2 integer-exact ({bound_bad} violations) => "
          f"mu_1 = c_1/(c_0 d^2) in [-1, 1] exact; min c_1 = {c1_min} "
          "< 0 (cuspidal section outside the positive monoid)",
          supp_eq_bad == 0 and coh_nz_bad == 0 and theta_eq
          and jac_bad == 0 and icnt_bad == 0 and avg_bad == 0
          and bound_bad == 0 and c1_min < 0)

    # mu_1 table on all coherent atoms <= 10^6 + lambda-window sieves
    t_mu = time.time()
    coh_idx_all = np.nonzero(coh)[0].astype(np.int64)
    coh_ge5 = coh_idx_all[coh_idx_all >= 5]
    MU1F = np.zeros(J_WIN + 1)
    MU1F[1] = 1.0
    for m in coh_ge5:
        m = int(m)
        val = 1.0
        mm = m
        while mm > 1:
            p = int(SPF[mm])
            e = 0
            while mm % p == 0:
                mm //= p
                e += 1
            i = int(PIDX[p])
            if e == 1:
                val *= float(COS1[i])
            else:
                val *= dker(e, float(PH1[i]))
        MU1F[m] = val
    mu_def_bad = 0
    for m in coh_ge5[coh_ge5 <= N_CFORM]:
        m = int(m)
        ex = C1E[m] / ((int(r2[m]) // 4) * float(m) ** 2)
        if abs(MU1F[m] - ex) > 1e-9 * max(1.0, abs(ex)):
            mu_def_bad += 1
    S_C = np.zeros(J_WIN + 1)
    S_L = np.zeros(J_WIN + 1)
    CNT_C = np.zeros(J_WIN + 1, dtype=np.int32)
    for d in coh_ge5[coh_ge5 <= J_WIN // 2]:
        d = int(d)
        top = J_WIN // d
        w0 = float(Pa[d])
        S_C[2 * d:: d] += A_F[2: top + 1] * w0
        S_L[2 * d:: d] += A_F[2: top + 1] * (w0 * MU1F[d])
        CNT_C[2 * d:: d] += 1
    hitm = CNT_C[1:] > 0
    rc_arr = np.where(hitm, (CERT_L * S_C[1:]) / (CERT_R * A_F[1:]),
                      -np.inf)
    rl_arr = np.where(hitm,
                      (CERT_L * np.abs(S_L[1:])) / (CERT_R * A_F[1:]),
                      -np.inf)
    i_c = int(np.argmax(rc_arr))
    i_l = int(np.argmax(rl_arr))
    rc_max = float(rc_arr[i_c])
    rl_max = float(rl_arr[i_l])
    j_l = i_l + 1
    canc_fact = rc_max / max(rl_max, 1e-300)
    print(f"        mu_1 table on {len(coh_ge5)} coherent atoms + "
          f"lambda sieves in {time.time() - t_mu:.1f}s; unlifted max "
          f"{rc_max:.4f} at j = {i_c + 1}, lambda max {rl_max:.4f} at "
          f"j = {j_l} ({canc_fact:.1f}x)")

    def mu1_exact(d: int) -> Fraction:
        c0v = int(r2[d]) // 4
        return Fraction(c_recon(d, 4), c0v * d * d)

    order_l = np.argsort(-rl_arr)
    rech_atoms = sorted(set(
        [int(i) + 1 for i in order_l[:6]]
        + [int(j) for j in rng.choice(np.where(hitm)[0] + 1, size=6,
                                      replace=False)]
        + [65, 1105, 32045]))
    rech_bad = 0
    cons_bad = 0
    for j in rech_atoms:
        sc_e = 0
        sl_e = Fraction(0)
        for d in divisors_from(factorise(j, SPF)):
            if d < 5 or j // d < 2 or not coh[d]:
                continue
            a = int(A_ARR[j // d])
            sc_e += a * int(Pa[d])
            sl_e += a * int(Pa[d]) * mu1_exact(d)
        if abs(sc_e - S_C[j]) > 1e-9 * max(1.0, abs(sc_e)):
            rech_bad += 1
        if abs(float(sl_e) - S_L[j]) > 1e-9 * max(1.0, abs(float(sl_e))):
            rech_bad += 1
        if sc_e > int(SM[j]):
            cons_bad += 1
    check("E.iv (THE lambda-WINDOW CERTIFICATE): mu_1 float table == "
          f"exact rationals on coherent d <= {N_CFORM} ({mu_def_bad} "
          "fails); the unlifted coherent-restricted certificate holds "
          f"everywhere (max 7 S_coh/40A = {rc_max:.4f} < 1, inherited "
          f"from the window proof; S_coh <= S-: {cons_bad} fails) AND "
          "the maximal lambda-design is STRICTLY stronger: "
          f"max 7|S_lambda|/40A = {rl_max:.4f} < {rc_max:.4f} "
          f"(cancellation factor {canc_fact:.1f}x); exact Fraction "
          f"rechecks (integer c_1 route + exact rational mu_1) on "
          f"{len(rech_atoms)} atoms ({rech_bad} mismatches) -- the "
          "sign-mixing of the phases IS the cancellation channel "
          "(amplitudes on forced keys, phases on the cofactor object "
          "g_lambda; T81 reachability: coherent targets are reachable "
          "ONLY by coherent rescalings)",
          mu_def_bad == 0 and rc_max < 1.0 and rl_max < rc_max
          and rech_bad == 0 and cons_bad == 0)

    # ============================================================ F
    print("F -- frontier facts [C] + the two NAMED limits")
    prod_frac = Fraction(1)
    N_chain = 1
    k_cross = None
    log10_N = 0.0
    log10_N_cross = None
    for h, p in enumerate(p1_list[:60], start=1):
        assert h <= CHAIN_K_EXACT
        prod_frac *= (1 + Fraction(1, p))
        N_chain *= p
        Pm = prod_frac - 1 - Fraction(1, N_chain)
        log10_N += math.log10(p)
        if rhoK * Pm >= 1:
            k_cross = h
            log10_N_cross = log10_N
            break
    check(f"F.i [C] (COHERENT-CHAIN CROSSING): the unlifted coherent "
          f"chain N_k = prod first k primes = 1 mod 4 crosses "
          f"rhoK * P- >= 1 at EXACTLY k* = {k_cross} = {KSTAR_ANCHOR} "
          f"(exact Fractions; log10 N* = {log10_N_cross:.1f} in "
          f"{L10N_BAND}) -- the constant-route frontier the "
          "lambda-channel replaces; K is a WINDOW constant (all-n "
          "extension DECLARED classical, Cohen 1975)",
          k_cross == KSTAR_ANCHOR
          and L10N_BAND[0] < log10_N_cross < L10N_BAND[1])

    check(f"F.ii [C] (LAMBDA-WINDOW MARGIN): lambda-channel decade "
          f"anchor max 7|S_lambda|/40A = {rl_max:.4f} vs unlifted "
          f"{rc_max:.4f} (factor {canc_fact:.1f}x, window-measured); "
          f"absolute Robin tail factor {gap_abs:.2f} at J = 10^6 "
          "(constant route OPEN, recorded) -- frontier facts are "
          "window-measured [C], beyond-window convergence is the "
          "DECLARED classical L(1, lambda_1) /= 0 (Hecke 1918/1920)",
          0.05 < rl_max < 0.08 and 0.20 < rc_max < 0.26
          and canc_fact > 3.0)

    check("FENCE: Gronwall 1913 / Robin 1983 UNCONDITIONAL / Cohen 1975 "
          "/ Hecke 1918/1920 / Cornacchia / Fermat-Gauss / Dirichlet "
          "L(1,chi) / Mertens-AP / Landau 1908 / Legendre duplication / "
          "Weil 1952-Guinand-Bombieri / Cauchy-Schwarz / Alaoglu-Erdos "
          "1944 / Shimura-Hecke T(p^2) / Jacobi-Landen named CLASSICAL; "
          "window proofs carry their windows; provably-shaped != formal "
          "proof; the TWO NAMED LIMITS are load-bearing content: "
          "(i) the correlated-cancellation lemma (credit-rich "
          "non-coherent uniform tail) stays a classically-shaped OPEN "
          "lemma; (ii) I5 in one-family form (Q_cert + Delta_2 + A_fam "
          "- A_shift >= 0) is the single remaining TFPT-specific object "
          "-- by the closed ledger EQUIVALENT to Weil positivity <=> RH "
          "(EQUIVALENCE TYPING, no progress claim); NO RH-evidence "
          "language; NOT 'almost RH'; ZETA.HP.CARRIER untouched; no "
          "marker moves",
          True)

    elapsed = time.time() - t0
    print(f"\nv541 runtime: {elapsed:.1f}s")
    print(f"  A window proof: 0 violations on {n_clash} clash atoms; "
          f"X = {float(X_abs):.6f} exact at j* = {j_abs}; rho_crit = "
          f"{float(rho_crit):.4f}; laws 0-tolerance "
          f"(8-law/{n_q}, tower+w/{N_FORM}, seeds -48/-80/-8)")
    print(f"  B ledger: residual max rel {res_rel_max:.1e} on "
          f"{len(ROWS)} rows; odd-prime match {max_l2:.1e}; "
          f"Delta_pole {max_pole:.1e}; arch double route {max_ar:.1e}")
    print(f"  C character: -psi = (chi_-4 + 1/4 chi_8 + 1/4 chi_-8) "
          f"Theta exact (odd n <= {N_FORM}); signed cert 0 violations, "
          f"margin factor {mfact:.2f}x; confinement set equality "
          f"{set_eq}")
    print(f"  D arch internal: bridge {mpmath.nstr(max_fac, 2)}; kernel "
          f"id {mpmath.nstr(max_kid, 2)}; battery subset {max_bat:.1e}")
    print(f"  E lambda channel: two-route carrier 0 mismatches "
          f"<= {N_CFORM}; lambda cert {rl_max:.4f} vs {rc_max:.4f} "
          f"({canc_fact:.1f}x)")
    print(f"  F frontier [C]: k* = {k_cross} (10^{log10_N_cross:.1f}); "
          f"Robin gap {gap_abs:.2f}; named limits: correlation lemma "
          "OPEN + I5 one-family (equivalence typing)")
    return summary("RTF.GNS.LEDGER.01 matching lemma and transport "
                   "ledger package")


if __name__ == "__main__":
    raise SystemExit(run())
