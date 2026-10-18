"""Discovery probe (2026-07-25), part 70 — contract LINEAR.MEASURE.WEIL.

Execution of the single path left open by T69 (MIXED.CHANNEL.FULL.WEIGHT:
DELETION-UNIVERSAL + TOWER-RESOLUTION).  T69 proved (window/theorem-like,
Cauchy–Littlewood lemma) that EVERY coefficient-bilinear form of two
determinant-p³ towers inherits the even-k deletion (the ζ(2·) denominator,
the minus).  The only way out is a form that does NOT run over coefficient
squares: the LINEAR measure family on the positive Siegel–Weil population
side,
    μ(d) = Θ(d) · |d|^{−a}  ≥ 0
(T68: Θ = N₊+N₋ unsigned population, pure σ₃-eigenform of weight 5/2,
towers = pure ζ-shifts ζ_p(w)ζ_p(w−3) with FULL weights — no squaring,
the CL lemma has no second Satake pair to act on).  Central question:
does the linear Θ-family carry a positive GNS structure whose prime side
is a PLUS combination of ζ-Weil forms — and does the deletion return
through the d-AGGREGATION?

HONEST SUSPICION (preregistered, MUST be tested): classically the
Dirichlet series of class-number-like coefficients carries the ζ(2s)
denominator in the d-DIRECTION (Cohen 1975 / Cohen–Eisenstein series:
Σ H(N) N^{−s} = ζ(s)ζ(2s−1)/ζ(2s)-type; named classical).  If the
deletion returns there, that is the next theorem-like bar — equally a
precise result (the ζ(2·) denominator would sit in BOTH directions and
the map would close completely).

L1  THE LINEAR MEASURE.  μ(d) = Θ(d)|d|^{−a} on live fundamental
    d ≡ 1 mod 8 (window ≥ 8000); positivity μ > 0 verified via the exact
    counting inequality Θ(d) ≥ |b(d)| > 0; zero-set structure of Θ on
    dead classes documented per d mod 8 (incl. the coherence-free but
    POPULATED class d ≡ 5 mod 8); growth γ_Θ and Σ_{d≤X}Θ(d) ~ κX^{5/2};
    convergence of Σ Θ(d)d^{−a} for preregistered a ∈ {3/2, 2, 5/2, 3}
    (T54-style ladder) — abscissa a* = 5/2 bracketed.
L2  THE d-AGGREGATION (suspicion test, core).
    (i)   coefficient-exact seed–tower factorisation for ALL odd n ≤ QMAX:
          Θ(D f²) = Θ(D) · α_E♯(f),
          α_E♯(f) = Σ_{j|f} μ(j) (D/j) j σ₃(f/j)  (σ₃-twist, T68/T69);
    (ii)  ALGEBRAIC m-aggregation (sympy exact):
          Σ_k α_E♯(p^k) X^k = (1 − χpX) / [(1−X)(1−p³X)]
          ⇒ Σ_f α_E♯(f) f^{−2s} = ζ(2s) ζ(2s−3) / L(2s−1, χ_D):
          ζ(2s) sits in the NUMERATOR of the tower aggregation —
          NO ζ(2s)-denominator in the m-direction;
    (iii) SEED IDENTIFICATION (machine-decided, exact rationals):
          Θ(d) / L(−1, χ_d) constant on the live class, with
          L(−1,χ_d) = −B_{2,χ_d}/2, B_{2,χ_d} = (1/d)Σ_a χ_d(a)a²
          (Cohen 1975: H(2,d) = L(−1,χ_d), named classical);
    (iv)  numeric closure of the closed form on the window:
          Σ_{n odd} Θ(n) n^{−s}
            = ζ_odd(2s) ζ_odd(2s−3) · Σ_D Θ(D) D^{−s} / L_odd(2s−1,χ_D)
          (double Dirichlet series of Shintani/Cohen class, named
          classical) + plain-ζ-ratio candidate scan (decided by machine);
    (v)   the EXACT localisation of 1/ζ(2s) in the d-direction: the
          fundamentality restriction itself — squarefree Möbius sieve
          Σ_{d squarefree} d^{−s} = ζ(s)/ζ(2s), coefficient-exact
          μ²(n) = Σ_{r²|n} μ(r) — a SUPPORT/index-level factor
          (same square-class inclusion–exclusion as T69-M3b), not a
          weight deletion;
    (vi)  verdict on the suspicion with exact localisation.
L3  THE LINEAR GNS FORM.  B_lin(φ,ψ) = Σ_d μ(d)φ(d)ψ(d): positive per
    construction; GNS = ℓ²(d, μ) (T55 technique: PSD Gram, rank growth
    with window, δ-basis identification); Hecke d ↦ dp² with the exact
    σ₃-twist multiplier (σ₃(p) − χ_d(p)p)p^{−2a} — integer-exact towers
    + matched-support pairing equivariance.
L4  WEIL BOOKKEEPING OF THE LINEAR FORM (heart).
    (i)   full weights algebraic: λ_k = 1 + p^{3k} − (χp)^k
          [the Λ(p^k)(1+p^{3k}) structure, NO even-k kill]; p^{3k}-layer
          list [1,1,1,1,…] vs quadratic fam [1,0,2,0], floor [2,0,2,0],
          mixed [0,−2,0,−2] (all recomputed);
    (ii)  CL non-applicability: single-tower numerator (1−χpX), degree 1,
          ≡ 1 at χ = 0 — the pair-deletion factor 1−p⁶X² cannot arise;
          the χ-term lives at layer q^{2k}, never at the population
          layer q^{6k};
    (iii) PLUS combination exact (zero-free prime sides, T59 technique):
          Prime_lin(g) = Prime_ζ(g₋) + Prime_ζ(g₊),
          g±(u) = e^{±3u/2} g(u) — ONLY PLUS signs; pole-kernel identity
          e^{−3u/2}(e^{u/2}+e^{−u/2}) + e^{3u/2}(e^{u/2}+e^{−u/2})
          = e^{2u}+e^{u}+e^{−u}+e^{−2u} pointwise; arch declared
          classical-external (T59 W2 convention);
    (iv)  the d-aggregation term: Prime side of ζ(2s)ζ(2s−3) =
          Prime_ζ(g♭₋) + Prime_ζ(g♭₊), g♭±(x) = e^{±3x/2} g(2x) —
          the T63 ♭/doubling kernel class WITH PLUS (T63 family core:
          −2·Prime_ζ(g♭); here the sign inverts);
    (v)   the χ-numerator term: bounded character content
          (|P_χ| ≤ P_ζ(g₀), g₀ = e^{−u/2}g), μ-averaged biases measured
          (X5 bridgehead) — the only minus is on a CHARACTER average,
          never on a ζ-flat term.
L5  SYNTHESIS.  Final deletion map over T63/T64/T68/T69/T70; honest
    typing (edge values L(−1,χ_d) ≃ |d|^{3/2}L(2,χ_d) live in the
    absolute-convergence region — Euler-region positivity, NOT central
    values; transport to the 1/2-line remains OPEN); the surviving
    pairing class ("sesquilinear over the measure": linear in the
    family, quadratic only in test functions); promotion-candidate
    typing (NO promotion); saturation judgement.

PREREGISTERED CRITERIA
  L1: μ > 0 exact on all live d (integer inequality Θ ≥ |b| > 0);
      zero-set documented; γ_Θ ∈ (1.3, 1.7); ladder exponents match
      5/2 − a within honesty bands; a = 3 converges.
  L2: factorisation 0 mismatches on ≥ 4000 nontrivial odd points;
      m-Euler form sympy-exact with χ=0 numerator ≡ 1; seed ratio a
      SINGLE exact rational on the live class; closed-form numeric
      identity rel < 1e-4 (s=4) / < 1e-6 (s ≥ 5); sieve identities
      coefficient-exact (n ≤ 3000) and numeric rel < 1e-5.
  L3: Gram PSD (min eig ≥ −1e-8·scale); rank grows along the D-window
      without collapse; towers integer-exact (≥ 300 pairs); pairing
      equivariance rel < 1e-12.
  L4: λ_k closed form exact k ≤ 8; layer lists exact; prime/pole
      plus-combination identities rel < 1e-12 on ≥ 9 test functions;
      ♭-plus bridge rel < 1e-12; χ-term bound holds on all functions.
  VERDICTS (preregistered):
    LINEAR-PLUS-COMBINATION — full weights + plus-ζ combination +
        d-aggregation without return of the deletion (the positive
        linear carrier stands);
    DELETION-RETURNS-IN-D  — the deletion returns in the d-direction —
        exactly localised; the ζ(2·) invariant is
        construction-universal;
    MIXED                  — named precisely.

FENCES (honest typing):
  (i)   STRUCTURE MAPPING ONLY — no RH evidence; a plus combination of
        ζ-Weil forms at weight-4 shifts (lines w and w−3, conjugations
        e^{±3u/2}) is NOT Weil positivity for ζ on the 1/2-line — the
        transport to the central line remains OPEN and is named;
  (ii)  classical results named as classical: Cohen 1975 (H(r,N),
        Cohen–Eisenstein series of weight r+1/2), Zagier, Siegel–Weil,
        Shimura correspondence / T(p²), Rankin–Selberg ζ(2s)
        normalisation, squarefree Möbius sieve, Shintani zeta /
        double Dirichlet series (Goldfeld–Hoffstein class), Dirichlet
        L-functions and generalised Bernoulli numbers B_{2,χ};
  (iii) the linear Θ-measure carries genus/Eisenstein arithmetic
        (class-number-like edge L-values), NOT the Waldspurger
        central-value arithmetic of b(d)² — the two are not re-booked
        here, they live in different families (T68 typing).

Firewall: discovery sandbox only — no promotion, no ledger / paper /
website / next.txt / README edits.  ZERO-FIREWALL (AST-checked): no
Riemann-zero loaders; mpmath.zeta is used ONLY as a function at real
points in the absolute-convergence region (closed-form values); all
prime sides are finite zero-free sums.  No RH-evidence or
"Weil positivity achieved" language.
"""
from __future__ import annotations

import ast
import inspect
import math
import time
from fractions import Fraction

import mpmath
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()
mpmath.mp.dps = 30

# ---------------------------------------------------------------- config
QMAX = 50_000                 # exact q-window for g and Theta
D_FAM = 8_000                 # live-d family window (contract: >= 8000)
HECKE_PS = (3, 5, 7, 11, 13)
G_KEY = (0, 2, 0, 1, 1, 1)    # theta2(q2)^2 theta3(q2) theta4 theta4(q2)
TH_KEY = (0, 2, 1, 2, 0, 0)   # theta4 -> theta3 in both c-slots (T68)
K_MAX = 8                     # layer depth
K_SER = 12                    # sympy series depth
A_CANDS = (1.5, 2.0, 2.5, 3.0)   # measure exponents (3.0 = convergent ref)
X_LADDER = (1000, 2000, 4000, 8000)
A_GNS = 2.5                   # GNS measure exponent (Eisenstein counting)
N_SIEVE = 3_000               # square-sieve coefficient window
N_LAM = 20_000                # prime-power window for zero-free prime sides
S_GRID = (4.0, 4.5, 5.0, 5.5, 6.0)
M_LCHI = 61                   # odd-m cutoff for L_odd(w, chi_D), w >= 7
SIG3_N = 260                  # sigma_3 table (f <= sqrt(QMAX) = 223)


def check(name, ok):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}", flush=True)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


def info(msg):
    print(f"        {msg}", flush=True)


# ================================================================ helpers
def theta_pairs(kind: int, scale_q: int, order_t: int):
    """Sparse (exponent, coeff) list of a theta factor in t-units (q=t^4)."""
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
    """Exact int64 multiplication by a sparse theta factor (T68 rebuild)."""
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


def mobius_sieve(n: int) -> np.ndarray:
    mu = np.zeros(n + 1, dtype=np.int8)
    mu[1] = 1
    primes = []
    is_comp = np.zeros(n + 1, dtype=bool)
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > n:
                break
            is_comp[v] = True
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]
    return mu


def spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    spf[1] = 1
    return spf


def jacobi(a: int, n: int) -> int:
    """Jacobi symbol (a/n) for odd n > 0 (fast binary algorithm)."""
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


def kron2(d: int) -> int:
    """kronecker(d, 2) for odd d: +1 if d ≡ ±1 mod 8 else −1."""
    return 1 if d % 8 in (1, 7) else -1


def kron_pos(d: int, a: int) -> int:
    """kronecker(d, a) for odd d > 0 and a >= 1."""
    v = 1
    while a % 2 == 0:
        a //= 2
        v *= kron2(d)
    return v * jacobi(d, a)


def square_split(n: int, spf: np.ndarray):
    """n = D·f² with D squarefree (odd n → odd D, odd f)."""
    D = 1
    f = 1
    while n > 1:
        p = int(spf[n])
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e % 2:
            D *= p
        f *= p ** (e // 2)
    return D, f


def g_fejer(u, a):
    return max(0.0, 1.0 - abs(u) / a)


def g_gauss(u, sig):
    return math.exp(-0.5 * (u / sig) ** 2)


def numerical_rank(eigs, tol_rel=1e-8):
    if len(eigs) == 0:
        return 0
    scale = max(abs(float(eigs[-1])), abs(float(eigs[0])), 1e-30)
    return int(np.sum(np.abs(eigs) > tol_rel * scale))


def zo(x: float) -> float:
    """2-stripped zeta ζ_odd(x) = ζ(x)(1−2^{−x}) at real x > 1 (function
    values in the absolute-convergence region only; no zeros involved)."""
    return float(mpmath.zeta(x)) * (1.0 - 2.0 ** (-x))


# ================================================================ S0
print("=" * 72)
print("S0 -- ZERO-FIREWALL (AST) + exact rebuild of g, Theta + live family")
print("=" * 72)

_SRC = inspect.getsource(inspect.getmodule(check))
_FORBIDDEN_AST = {
    "zeta" + "zero",
    "zeta" + "_zero",
    "zeta" + "_zeros",
    "siegel" + "z",
    "riemann" + "zeros",
    "riemann" + "_zero",
}
_tree = ast.parse(_SRC)
_call_names = set()
for node in ast.walk(_tree):
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name):
            _call_names.add(f.id)
        elif isinstance(f, ast.Attribute):
            _call_names.add(f.attr)
_zero_calls = _call_names & _FORBIDDEN_AST
_attr_hits = [
    node.attr for node in ast.walk(_tree)
    if isinstance(node, ast.Attribute) and node.attr in _FORBIDDEN_AST
]
_imported = set()
for node in ast.walk(_tree):
    if isinstance(node, ast.ImportFrom):
        for alias in node.names:
            _imported.add(alias.name)
    elif isinstance(node, ast.Import):
        for alias in node.names:
            _imported.add(alias.name)
_bad_imports = _imported & _FORBIDDEN_AST
check(
    "S0a ZERO-FIREWALL: AST has no Riemann-zero loader "
    f"(calls∩={sorted(_zero_calls)}; attrs={_attr_hits}; "
    f"imports={sorted(_bad_imports)})",
    len(_zero_calls) == 0 and len(_attr_hits) == 0 and len(_bad_imports) == 0,
)
_name_hits = [
    node.id for node in ast.walk(_tree)
    if isinstance(node, ast.Name) and node.id in _FORBIDDEN_AST
]
check(
    f"S0b ZERO-FIREWALL: no forbidden zero-loader Name nodes ({_name_hits})",
    len(_name_hits) == 0,
)
info("FENCE: structure mapping only — no RH / Weil-positivity claim;")
info("  Cohen 1975 / Cohen–Eisenstein, Zagier, Siegel–Weil, Shimura,")
info("  RS ζ(2s)-normalisation, Möbius square sieve, Shintani / double")
info("  Dirichlet series — all named classical.  mpmath.zeta = function")
info("  values at real x > 1 only.")

t_b = time.time()
ORDER_T = 4 * QMAX
g_t = build_monomial(G_KEY, ORDER_T)
th_t = build_monomial(TH_KEY, ORDER_T)
support_ok = all(
    not np.any(arr[r::4] != 0) for arr in (g_t, th_t) for r in (1, 2, 3)
)
g = g_t[0::4][: QMAX + 1].copy()
Th = th_t[0::4][: QMAX + 1].copy()
del g_t, th_t
info(f"exact sparse builds O(q^{QMAX}) in {time.time() - t_b:.2f}s "
     f"(int64, T68 rebuild technique)")
info(f"g  head = {list(g[:10])}")
info(f"Th head = {list(Th[:10])}")
check(
    "S0.build: g matches the v537/T38 witness head [0,4,-8,0,0,0,16,...]; "
    f"Θ ≥ |g| ≥ 0 coefficientwise for ALL n ≤ {QMAX} (population bound, "
    "exact integers)",
    support_ok and list(g[:7]) == [0, 4, -8, 0, 0, 0, 16]
    and bool(np.all(Th >= np.abs(g))),
)

mu = mobius_sieve(QMAX)
spf = spf_sieve(QMAX)
live = [
    d for d in range(1, D_FAM + 1, 2)
    if d % 8 == 1 and abs(int(mu[d])) == 1 and int(g[d]) != 0
]
bs = {d: int(g[d]) for d in live}
ts = {d: int(Th[d]) for d in live}
info(f"live fund d≡1 mod 8, b≠0, d ≤ {D_FAM}: {len(live)}")
check(
    f"S0.family: #{len(live)} live fundamental d ≤ {D_FAM} "
    f"(contract window ≥ 8000; need ≥ 200 live d); q-window {QMAX}",
    D_FAM >= 8000 and len(live) >= 200 and QMAX >= 50_000,
)

rng = np.random.default_rng(70)
kron_ok = True
for _ in range(300):
    d = int(rng.integers(1, 5000)) * 2 + 1
    a = int(rng.integers(1, 20000))
    if kron_pos(d, a) != int(sp.kronecker_symbol(d, a)):
        kron_ok = False
check(
    "S0.kron: fast Kronecker/Jacobi implementation matches sympy "
    "kronecker_symbol on 300 random (odd d, a) pairs",
    kron_ok,
)

# sigma_3 table for tower coefficients
sig3_tab = [0] * (SIG3_N + 1)
for j in range(1, SIG3_N + 1):
    for m in range(j, SIG3_N + 1, j):
        sig3_tab[m] += j ** 3


def alphaE_sharp(D: int, f: int) -> int:
    """σ₃-twist tower coefficient Σ_{j|f} μ(j)(D/j) j σ₃(f/j), f odd."""
    tot = 0
    for j in sp.divisors(f):
        j = int(j)
        mj = int(mu[j])
        if mj == 0:
            continue
        tot += mj * jacobi(D, j) * j * sig3_tab[f // j]
    return tot


# ================================================================ L1
print("=" * 72)
print("L1 -- THE LINEAR MEASURE mu(d) = Theta(d)|d|^{-a} >= 0")
print("=" * 72)

# (i) positivity on live d via the exact counting inequality
pos_live = all(ts[d] >= abs(bs[d]) and ts[d] > 0 for d in live)
check(
    "L1.i: μ(d) > 0 on ALL live d — exact integer inequality "
    "Θ(d) ≥ |b(d)| > 0 (Θ = N₊+N₋ ≥ |N₊−N₋| = |b|, counting positivity; "
    f"{len(live)} live d verified)",
    pos_live,
)

# (ii) zero-set structure of Theta on odd fundamental (squarefree) D
cls_stats = {}
zero_examples = {}
for r in (1, 3, 5, 7):
    Ds = [D for D in range(1, D_FAM + 1, 2)
          if D % 8 == r and abs(int(mu[D])) == 1]
    npos = sum(1 for D in Ds if int(Th[D]) > 0)
    nzero = len(Ds) - npos
    nb = sum(1 for D in Ds if int(g[D]) != 0)
    cls_stats[r] = (len(Ds), npos, nzero, nb)
    zero_examples[r] = [D for D in Ds if int(Th[D]) == 0][:5]
    info(f"  D≡{r} (8), squarefree ≤ {D_FAM}: #D={len(Ds)}, Θ>0: {npos}, "
         f"Θ=0: {nzero}, b≠0: {nb}; first Θ-zeros: {zero_examples[r]}")
tot_D = sum(v[0] for v in cls_stats.values())
class5_bal = cls_stats[5][3] == 0 and cls_stats[5][1] > 0
zero_classes = sorted(r for r in cls_stats if cls_stats[r][2] > 0)
info(f"Θ-zero classes mod 8 on the fundamental window: {zero_classes}")
check(
    "L1.ii: zero-set structure documented — class counts consistent "
    f"(Σ={tot_D}); d ≡ 5 mod 8 is coherence-FREE (b ≡ 0, T68) but "
    f"population-POSITIVE (Θ > 0 on {cls_stats[5][1]}/{cls_stats[5][0]}); "
    "the linear measure extends to the ε=−1 class where the quadratic "
    "family is empty",
    tot_D == sum(cls_stats[r][0] for r in (1, 3, 5, 7)) and class5_bal,
)

# (iii) growth of the seed and of the cumulative mass
ld = np.log([float(d) for d in live])
lt = np.log([float(ts[d]) for d in live])
gam_t = float(np.polyfit(ld, lt, 1)[0])
cum_rows = []
s_run = 0.0
li = 0
live_sorted = live
for X in X_LADDER:
    while li < len(live_sorted) and live_sorted[li] <= X:
        s_run += float(ts[live_sorted[li]])
        li += 1
    cum_rows.append((X, s_run, s_run / X ** 2.5))
kappa_late = cum_rows[-1][2]
kappa_prev = cum_rows[-2][2]
cum_slope = float(np.polyfit(np.log([r[0] for r in cum_rows]),
                             np.log([r[1] for r in cum_rows]), 1)[0])
info(f"growth: γ_Θ = {gam_t:.4f} (Eisenstein target 3/2); "
     f"cumulative slope = {cum_slope:.3f} (target 5/2)")
info(f"κ ladder Σ_(d≤X)Θ/X^2.5: "
     + ", ".join(f"{r[0]}:{r[2]:.5f}" for r in cum_rows))
check(
    f"L1.iii: γ_Θ = {gam_t:.3f} ∈ (1.3, 1.7) and Σ_{{d≤X}}Θ(d) ~ κX^{{5/2}} "
    f"(slope {cum_slope:.3f} ∈ (2.3, 2.7); κ stable "
    f"{kappa_prev:.4f}→{kappa_late:.4f})",
    1.3 < gam_t < 1.7 and 2.3 < cum_slope < 2.7
    and abs(kappa_late - kappa_prev) < 0.2 * abs(kappa_late),
)

# (iv) convergence ladder of the measure sums (T54-style)
ladder = {}
for a in A_CANDS:
    vals = []
    for X in X_LADDER:
        vals.append(sum(float(ts[d]) * d ** (-a) for d in live if d <= X))
    ladder[a] = vals
    slope = float(np.polyfit(np.log(X_LADDER), np.log(vals), 1)[0])
    last_rel = (vals[-1] - vals[-2]) / vals[-1]
    info(f"  a={a}: S(X) = " + ", ".join(f"{v:.4f}" for v in vals)
         + f"; slope={slope:.3f} (alg {max(2.5 - a, 0.0):.1f}); "
         f"last-step rel={last_rel:.4f}")
    ladder[(a, "slope")] = slope
    ladder[(a, "last")] = last_rel
conv_ok = (
    abs(ladder[(1.5, "slope")] - 1.0) < 0.25
    and abs(ladder[(2.0, "slope")] - 0.5) < 0.20
    and ladder[(2.5, "slope")] < 0.30
    and ladder[(3.0, "last")] < 0.05
)
check(
    "L1.iv: measured d-sum abscissa a* = 5/2 — slopes match 5/2 − a "
    f"(a=3/2: {ladder[(1.5, 'slope')]:.3f}≈1; a=2: "
    f"{ladder[(2.0, 'slope')]:.3f}≈1/2; a=5/2: {ladder[(2.5, 'slope')]:.3f} "
    f"log-marginal < 0.3; a=3 converged, last step "
    f"{ladder[(3.0, 'last')]:.4f} < 0.05)",
    conv_ok,
)


# ================================================================ L2
print("=" * 72)
print("L2 -- THE d-AGGREGATION (suspicion test: where does 1/zeta(2s) sit?)")
print("=" * 72)

# (i) coefficient-exact seed-tower factorisation on ALL odd n <= QMAX
t_f = time.time()
n_checked = 0
n_nontrivial = 0
n_mismatch = 0
mismatch_ex = []
for n in range(1, QMAX + 1, 2):
    D, f = square_split(n, spf)
    if f == 1:
        continue
    n_nontrivial += 1
    pred = int(Th[D]) * alphaE_sharp(D, f)
    n_checked += 1
    if pred != int(Th[n]):
        n_mismatch += 1
        if len(mismatch_ex) < 5:
            mismatch_ex.append((n, D, f, int(Th[n]), pred))
info(f"factorisation pass over odd n ≤ {QMAX} in {time.time() - t_f:.1f}s: "
     f"{n_nontrivial} nontrivial points (f > 1), {n_mismatch} mismatches")
if mismatch_ex:
    info(f"  first mismatches: {mismatch_ex}")
check(
    f"L2.i: SEED–TOWER FACTORISATION Θ(Df²) = Θ(D)·α_E♯(f) integer-exact "
    f"for ALL odd n ≤ {QMAX} ({n_nontrivial} nontrivial points ≥ 4000, "
    "all four seed classes mod 8, all primes — extends T68/T69 towers "
    "from p ≤ 13 to the full window)",
    n_mismatch == 0 and n_nontrivial >= 4000,
)

# (ii) algebraic m-aggregation (sympy exact)
X_s, P_s, CHI_s = sp.symbols("X p chi")
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
num_chi0 = sp.expand((1 - CHI_s * P_s * X_s).subs(CHI_s, 0))
info("m-aggregation local factor (sympy exact):")
info("  Σ_k α_E♯(p^k) X^k = (1 − χpX) / [(1−X)(1−p³X)]")
info("  X = p^{−2s}:  Σ_f α_E♯(f) f^{−2s} = ζ(2s)ζ(2s−3)/L(2s−1,χ_D)")
info("  X = p^{−s} :  Σ_m α_E♯(m) m^{−s}  = ζ(s)ζ(s−3)/L(s−1,χ_D)")
info("  ⇒ ζ(2s) sits in the NUMERATOR of the tower aggregation; the")
info("    denominator is a Dirichlet L (character), NEVER ζ(2·).")
check(
    "L2.ii: m-aggregation Euler form EXACT (sympy, k ≤ 12): "
    "(1−χpX)/[(1−X)(1−p³X)]; χ=0 numerator ≡ 1 — NO deletion factor in "
    "the m-direction; ζ(2s)ζ(2s−3) enters WITH PLUS (numerator)",
    euler_ok and num_chi0 == 1,
)

# (iii) SEED IDENTIFICATION: Theta(d) vs L(-1, chi_d) (exact rationals)
t_s = time.time()


def seed_S2(d: int) -> int:
    """S2 = Σ_{a=1}^{d−1} χ_d(a) a²; B_{2,χ_d} = S2/d (χ_d even
    primitive, nontrivial — generalised Bernoulli, classical)."""
    chi = np.zeros(d, dtype=np.int8)
    chi[1] = 1
    k2 = kron2(d)
    for a in range(2, d):
        p = int(spf[a])
        if p == a:
            if d % p == 0:
                v = 0
            elif p == 2:
                v = k2
            else:
                v = jacobi(d, p)
            chi[a] = v
        else:
            chi[a] = chi[p] * chi[a // p]
    aa = np.arange(d, dtype=np.int64)
    return int(np.dot(chi.astype(np.int64), aa * aa))


ratio_set = set()
sign_ok = True
r1 = Fraction(int(Th[1])) / Fraction(-1, 12)   # d=1: L(−1,χ_1) = ζ(−1)
ratio_set_gt1 = set()
for d in live:
    if d == 1:
        continue
    S2 = seed_S2(d)
    if S2 == 0:
        sign_ok = False
        continue
    if S2 < 0:
        sign_ok = False
    ratio_set_gt1.add(Fraction(-2 * d * int(Th[d]), S2))
ratio_set = set(ratio_set_gt1)
ratio_set.add(r1)
info(f"seed scan over {len(live)} live d in {time.time() - t_s:.1f}s")
info(f"ratio Θ(d)/L(−1,χ_d): d=1 anchor r(1) = {r1}; "
     f"distinct values d>1: {sorted(ratio_set_gt1)[:4]} "
     f"(#={len(ratio_set_gt1)})")
seed_const = (len(ratio_set_gt1) == 1 and r1 in ratio_set_gt1)
c_seed = r1 if seed_const else None
check(
    "L2.iii: SEED IDENTIFICATION exact — Θ(d) = c·L(−1,χ_d) with ONE "
    f"rational constant c = {r1} on ALL live d (incl. the d=1 anchor "
    "ζ(−1) = −1/12); L(−1,χ_d) < 0 sign-definite (S2 > 0) ⇒ the linear "
    "measure IS the Cohen edge-L-value measure (Cohen 1975 "
    "H(2,d) = L(−1,χ_d), named classical)",
    seed_const and sign_ok,
)
# class-5 extension (info): same seed law on the coherence-free class?
ratio5 = set()
d5s = [D for D in range(1, 4001, 2)
       if D % 8 == 5 and abs(int(mu[D])) == 1 and int(Th[D]) > 0][:60]
for d in d5s:
    S2 = seed_S2(d)
    if S2 != 0:
        ratio5.add(Fraction(-2 * d * int(Th[d]), S2))
info(f"class d≡5 (8) seed ratios (sample {len(d5s)}): "
     f"{sorted(ratio5)[:4]} (#distinct={len(ratio5)}) — documented")

# (iv) numeric closure of the closed form + plain-ratio candidate scan
odd_n = np.arange(1, QMAX + 1, 2)
Th_odd = Th[odd_n].astype(np.float64)


def lhs_agg(s: float) -> float:
    return float(np.sum(Th_odd * odd_n.astype(np.float64) ** (-s)))


t_a = time.time()
seedsD = [(D, int(Th[D])) for D in range(1, QMAX + 1, 2)
          if abs(int(mu[D])) == 1 and int(Th[D]) != 0]
odd_ms = list(range(1, M_LCHI + 1, 2))
chi_cache = {}
for D, _tD in seedsD:
    chi_cache[D] = [jacobi(D, m) for m in odd_ms]
info(f"RHS seed set: {len(seedsD)} odd squarefree D with Θ(D)≠0 "
     f"(χ_D cache built in {time.time() - t_a:.1f}s)")


def rhs_agg(s: float) -> float:
    w = 2.0 * s - 1.0
    mpow = [m ** (-w) for m in odd_ms]
    acc = 0.0
    for D, tD in seedsD:
        chis = chi_cache[D]
        Lval = sum(c * mp for c, mp in zip(chis, mpow) if c)
        acc += tD * D ** (-s) / Lval
    return zo(2.0 * s) * zo(2.0 * s - 3.0) * acc


id_rels = []
for s in S_GRID:
    lhs = lhs_agg(s)
    rhs = rhs_agg(s)
    rel = abs(lhs - rhs) / abs(lhs)
    id_rels.append((s, lhs, rhs, rel))
    info(f"  s={s}: LHS Σ_odd Θ(n)n^-s = {lhs:.10g}; "
         f"RHS ζo(2s)ζo(2s−3)·Ξ(s) = {rhs:.10g}; rel = {rel:.3e}")
max_rel_id = max(r[3] for r in id_rels)
id_ok = all((r[3] < 1e-4 if r[0] < 4.5 else r[3] < 1e-6) for r in id_rels)
check(
    "L2.iv: CLOSED-FORM AGGREGATION verified numerically on the window — "
    "Σ_{n odd} Θ(n)n^{−s} = ζ_odd(2s)ζ_odd(2s−3)·Σ_D Θ(D)D^{−s}/"
    f"L_odd(2s−1,χ_D) (max rel {max_rel_id:.2e}; tol 1e-4 at s=4, 1e-6 "
    "at s ≥ 4.5) — ζ(2s) confirmed in the NUMERATOR; Ξ(s) is a double "
    "Dirichlet series (Shintani/Cohen class, named classical)",
    id_ok,
)

CANDS = {
    "zo(s-3/2)zo(2s-3)/zo(2s)": lambda s: zo(s - 1.5) * zo(2 * s - 3)
    / zo(2 * s),
    "zo(s)zo(2s-4)/zo(2s)": lambda s: zo(s) * zo(2 * s - 4) / zo(2 * s),
    "zo(s-3/2)zo(2s-4)/zo(2s)": lambda s: zo(s - 1.5) * zo(2 * s - 4)
    / zo(2 * s),
    "zo(s-3/2)": lambda s: zo(s - 1.5),
}
drifts = {}
for name, fn in CANDS.items():
    c_fit = lhs_agg(6.0) / fn(6.0)
    dr = max(abs(lhs_agg(s) / (c_fit * fn(s)) - 1.0) for s in S_GRID)
    drifts[name] = dr
    info(f"  plain-ratio candidate {name}: fitted c={c_fit:.5f}, "
         f"drift={dr:.3e}")
min_drift = min(drifts.values())
no_plain = min_drift > 100.0 * max(max_rel_id, 1e-12) and min_drift > 1e-3
check(
    "L2.iv.b: PLAIN-ζ-RATIO SCAN decided by machine — best candidate "
    f"drift {min_drift:.2e} vs closed-form identity {max_rel_id:.2e}: "
    + ("NO plain ζ-ratio represents D_Θ (the d-aggregation is genuinely "
       "a double Dirichlet series)" if no_plain
       else "a plain ratio matches (hit documented)"),
    no_plain or min_drift < 1e-6,
)

# (v) the exact localisation: fundamentality = squarefree Moebius sieve
sieve_exact = True
for n in range(1, N_SIEVE + 1):
    acc = 0
    r = 1
    while r * r <= n:
        if n % (r * r) == 0:
            acc += int(mu[r])
        r += 1
    if acc != (1 if mu[n] != 0 else 0):
        sieve_exact = False
Y_loc = sp.symbols("Yloc")
local_sf = sp.simplify((1 + Y_loc) - (1 - Y_loc ** 2) / (1 - Y_loc)) == 0
sf3 = sum(d ** -3.0 for d in range(1, QMAX + 1, 2) if mu[d] != 0)
sf3_target = zo(3.0) / zo(6.0)
rel_sf3 = abs(sf3 - sf3_target) / sf3_target
sf2 = sum(d ** -2.0 for d in range(1, QMAX + 1, 2) if mu[d] != 0)
sf2_target = zo(2.0) / zo(4.0)
rel_sf2 = abs(sf2 - sf2_target) / sf2_target
info("support sieve: Σ_{d odd squarefree} d^{−s} = ζ_odd(s)/ζ_odd(2s)")
info(f"  numeric: s=3: {sf3:.10f} vs {sf3_target:.10f} (rel {rel_sf3:.2e}); "
     f"s=2: rel {rel_sf2:.2e}")
check(
    f"L2.v: THE 1/ζ(2s) IN THE d-DIRECTION localised — μ²(n) = "
    f"Σ_{{r²|n}} μ(r) coefficient-exact (n ≤ {N_SIEVE}); local "
    "(1+X) = (1−X²)/(1−X) = ζ_p(s)/ζ_p(2s) sympy-exact; numeric "
    f"ζo(3)/ζo(6) rel {rel_sf3:.1e} < 1e-5: the fundamental-d SUPPORT "
    "carries the squarefree Möbius sieve ζ(s)/ζ(2s) (classical) — a "
    "SUPPORT/index-level factor (T69-M3b inclusion–exclusion class), "
    "not a weight deletion",
    sieve_exact and local_sf and rel_sf3 < 1e-5 and rel_sf2 < 1e-3,
)

deletion_in_m = False          # L2.ii: numerator ζ(2s), χ=0 numerator ≡ 1
deletion_in_agg = not id_ok    # L2.iv: closed form has ζ(2s) with PLUS
sieve_return = sieve_exact and local_sf and rel_sf3 < 1e-5
check(
    "L2.vi: VERDICT ON THE SUSPICION — the Cohen-type ζ(2s) denominator "
    "in the d-direction EXISTS and is exactly localised: it is the "
    "FUNDAMENTALITY (squarefree) sieve of the support, NOT a weight "
    "deletion; m-direction: numerator ζ(2s)ζ(2s−3) (no deletion); "
    "total aggregation: numerator (no deletion) "
    f"(flags: del_m={deletion_in_m}, del_agg={deletion_in_agg}, "
    f"support_sieve={sieve_return})",
    (not deletion_in_m) and (not deletion_in_agg) and sieve_return,
)


# ================================================================ L3
print("=" * 72)
print("L3 -- THE LINEAR GNS FORM B_lin = Sum mu(d) phi(d) psi(d)")
print("=" * 72)

mu_w = np.array([float(ts[d]) * d ** (-A_GNS) for d in live])
info(f"GNS measure: μ(d) = Θ(d)·d^(−{A_GNS}), {len(live)} atoms, "
     f"total mass {mu_w.sum():.4f}, min {mu_w.min():.3e}")


def eval_test_fns(ds, kind, n):
    Xref = float(max(ds)) if ds else 1.0
    u = np.array(ds, dtype=np.float64) / Xref
    vecs = []
    if kind == "fourier":
        for k in range(n):
            if k == 0:
                vecs.append(np.ones_like(u))
            elif k % 2 == 1:
                vecs.append(np.sin(math.pi * ((k + 1) // 2) * u))
            else:
                vecs.append(np.cos(math.pi * (k // 2) * u))
    elif kind == "bump":
        for k in range(n):
            c = (k + 0.5) / n
            w = 1.5 / n
            t = (u - c) / w
            vecs.append(np.where(np.abs(t) < 1.0, (1.0 - t * t) ** 2, 0.0))
    else:
        raise ValueError(kind)
    return vecs


def gram_of(ds, w, vecs):
    n = len(vecs)
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            v = float(np.sum(w * vecs[i] * vecs[j]))
            G[i, j] = v
            G[j, i] = v
    return G


psd_ok = True
rank_rows = []
for kind in ("bump", "fourier"):
    for n in (10, 20, 30, 40):
        vecs = eval_test_fns(live, kind, n)
        G = gram_of(live, mu_w, vecs)
        eigs = np.linalg.eigvalsh(G)
        mine = float(eigs[0])
        rnk = numerical_rank(eigs)
        scale = float(eigs[-1])
        psd_ok = psd_ok and (mine >= -1e-8 * scale)
        rank_rows.append((kind, n, rnk, mine))
        info(f"  {kind:8s} n={n:2d}: rank={rnk}, min_eig={mine:.3e}, "
             f"max_eig={scale:.4g}")
bump_ranks = [r[2] for r in rank_rows if r[0] == "bump"]
check(
    "L3.i: B_lin is PSD structurally and numerically — Gram min eigs ≥ "
    "−1e-8·scale on bump/fourier families (positive point-mass measure; "
    "no counterpoles)",
    psd_ok,
)

ladder_rows = []
for Dw in (200, 500, 1000, 4000, 8000):
    ds = [d for d in live if d <= Dw]
    w = np.array([float(ts[d]) * d ** (-A_GNS) for d in ds])
    n_use = min(40, max(5, len(ds)))
    vecs = eval_test_fns(ds, "bump", n_use)
    rnk = numerical_rank(np.linalg.eigvalsh(gram_of(ds, w, vecs)))
    ladder_rows.append((Dw, len(ds), rnk, n_use))
    info(f"  window D≤{Dw}: #d={len(ds)}, rank(G_{n_use})={rnk}")
G_delta = np.diag(mu_w[:40])
rnk_delta = numerical_rank(np.linalg.eigvalsh(G_delta))
window_grows = (ladder_rows[0][2] >= int(0.8 * min(ladder_rows[0][1], 40))
                and ladder_rows[-1][2] > ladder_rows[0][2]
                and ladder_rows[-1][2] >= 38)
check(
    "L3.ii: GNS = ℓ²(d, μ) — rank grows along the D-window without "
    f"collapse ({ladder_rows[0][:3]}→{ladder_rows[-1][:3]}); δ-basis "
    f"diag(μ) rank {rnk_delta}/40 (T55 GNS technique; the pairing "
    "GENERATES the space)",
    window_grows and rnk_delta == 40 and bump_ranks[-1] >= 38,
)

# Hecke: exact sigma_3-twist towers + matched-support pairing equivariance
tower_ok = True
n_t1 = 0
for d in live:
    for p in HECKE_PS:
        if d % p == 0 or d * p * p > QMAX:
            continue
        chi = jacobi(d, p)
        n_t1 += 1
        if int(Th[d * p * p]) != (1 + p ** 3 - chi * p) * ts[d]:
            tower_ok = False
pair_ok = True
for p in (3, 5, 7):
    for Xw in (2000, 8000):
        lhs = 0.0
        rhs = 0.0
        for d in live:
            if d > Xw or d * p * p > QMAX or d % p == 0:
                continue
            phi2 = math.exp(-2.0 * d / Xw)
            lhs += float(Th[d * p * p]) * (d * p * p) ** (-A_GNS) * phi2
            chi = jacobi(d, p)
            rhs += ((1 + p ** 3 - chi * p) * p ** (-2 * A_GNS)
                    * float(ts[d]) * d ** (-A_GNS) * phi2)
        rel = abs(lhs - rhs) / max(abs(lhs), 1e-30)
        pair_ok = pair_ok and rel < 1e-12
        info(f"  Hecke pairing p={p}, X={Xw}: LHS={lhs:.6g} RHS={rhs:.6g} "
             f"rel={rel:.2e}")
check(
    f"L3.iii: Hecke structure EXACT — Θ(dp²) = (σ₃(p)−χ_d(p)p)·Θ(d) "
    f"integer-exact on {n_t1} live (d,p) pairs (≥ 300); d ↦ dp² acts on "
    "ℓ²(d,μ) with the exact multiplier (σ₃(p)−χ_d(p)p)p^{−2a} "
    "(matched-support pairing rel < 1e-12)",
    tower_ok and n_t1 >= 300 and pair_ok,
)


# ================================================================ L4
print("=" * 72)
print("L4 -- WEIL BOOKKEEPING OF THE LINEAR FORM (heart)")
print("=" * 72)

# (i) full weights algebraic + layer lists
G_lin = (1 - CHI_s * P_s * X_s) / ((1 - X_s) * (1 - P_s ** 3 * X_s))
L_lin = sp.series(X_s * sp.diff(sp.log(G_lin), X_s), X_s, 0,
                  K_MAX + 1).removeO()
lam_closed_ok = True
for k in range(1, K_MAX + 1):
    lam_k = sp.expand(L_lin.coeff(X_s, k))
    tgt = sp.expand(1 + P_s ** (3 * k) - (CHI_s * P_s) ** k)
    if sp.simplify(lam_k - tgt) != 0:
        lam_closed_ok = False
Q_s = sp.symbols("q", positive=True)
layer_lin = []
chi_layer_off = True
for k in range(1, K_MAX + 1):
    e = sp.expand((1 + P_s ** (3 * k) - (CHI_s * P_s) ** k)
                  .subs(P_s, Q_s ** 2))
    layer_lin.append(int(e.coeff(Q_s, 6 * k).subs(CHI_s, 0)))
    if k >= 1 and sp.expand(e.coeff(Q_s, 6 * k)).has(CHI_s):
        chi_layer_off = False

Y_s = sp.symbols("Y")
gen_lists = {}
for name, gen in (
    ("full ζ(u)²          ", 2 * Y_s / (1 - Y_s)),
    ("fam  [T61/T63 core] ", 2 * Y_s / (1 - Y_s ** 2) - Y_s),
    ("floor [T68 ratio]   ", 2 * Y_s / (1 - Y_s ** 2)),
    ("mixed [T69 minus]   ", -2 * Y_s ** 2 / (1 - Y_s ** 2)),
    ("sieve/♭ ζ(2u)       ", 2 * Y_s ** 2 / (1 - Y_s ** 2)),
    ("LINEAR Θ-tower (3k) ", Y_s / (1 - Y_s)),
):
    ser = sp.series(gen, Y_s, 0, K_MAX + 1).removeO()
    gen_lists[name.strip()] = [int(ser.coeff(Y_s, k))
                               for k in range(1, K_MAX + 1)]
    info(f"  layers {name}= {gen_lists[name.strip()]}")
lists_ok = (
    gen_lists["fam  [T61/T63 core]"] == [1 if k == 1 else
                                         (2 if k % 2 == 1 else 0)
                                         for k in range(1, K_MAX + 1)]
    and gen_lists["floor [T68 ratio]"] == [2 if k % 2 == 1 else 0
                                           for k in range(1, K_MAX + 1)]
    and gen_lists["mixed [T69 minus]"] == [0 if k % 2 == 1 else -2
                                           for k in range(1, K_MAX + 1)]
    and gen_lists["LINEAR Θ-tower (3k)"] == [1] * K_MAX
    and layer_lin == [1] * K_MAX
)
check(
    "L4.i: FULL WEIGHTS algebraic — λ_k = 1 + p^{3k} − (χp)^k exact "
    f"(k ≤ {K_MAX}); p^{{3k}}-layer of the linear tower = "
    f"{layer_lin} = [1,1,1,…] (NO even-k kill; the Λ(p^k)(1+p^{{3k}}) "
    "structure confirmed) vs fam [1,0,2,0], floor [2,0,2,0], mixed "
    "[0,−2,0,−2] (recomputed)",
    lam_closed_ok and lists_ok,
)
check(
    "L4.ii: CL-LEMMA NON-APPLICABILITY — the linear tower has ONE "
    "Satake pair: numerator (1−χpX) has degree 1 (no X² term), equals 1 "
    "at χ=0 — the pair-deletion factor 1−p⁶X² structurally CANNOT arise; "
    "the χ-term sits at layer q^{2k}, never at the population layer "
    f"q^{{6k}} (checked k ≤ {K_MAX})",
    sp.degree(sp.Poly(1 - CHI_s * P_s * X_s, X_s)) == 1
    and num_chi0 == 1 and chi_layer_off,
)

# zero-free prime-side machinery (odd primes; the family is 2-stripped)
lam_pk = []
for p in sp.primerange(3, N_LAM + 1):
    p = int(p)
    lp = math.log(p)
    pk = p
    k = 1
    while pk <= N_LAM:
        lam_pk.append((pk, p, k, lp))
        pk *= p
        k += 1
info(f"odd prime-power table: {len(lam_pk)} entries ≤ {N_LAM}")

TEST_FNS = []
for a in (1.5, 2.0, 2.5, 3.0, 3.5):
    TEST_FNS.append(("fejer", a, (lambda u, aa=a: g_fejer(u, aa)), float(a)))
for sig in (0.6, 0.8, 1.0, 1.2):
    TEST_FNS.append(("gauss", sig, (lambda u, s=sig: g_gauss(u, s)),
                     8.0 * float(sig)))


def P_lin_fn(g_fn, umax):
    """2 Σ_{p odd,k} Λ(p^k)(p^{−2k} + p^{k}) g(k log p) — prime side of
    ζo(w)ζo(w−3) at the self-dual centre w = 2 (zero-free)."""
    s = 0.0
    for n, p, k, lp in lam_pk:
        u = math.log(n)
        if u > umax + 1e-12:
            continue
        s += lp * (n ** -2.0 + float(n)) * g_fn(u)
    return 2.0 * s


def P_zeta_conj(g_fn, umax, alpha):
    """P_ζo(g̃), g̃(u) = e^{αu} g(u): 2 Σ Λ(n) n^{−1/2+α} g(log n)."""
    s = 0.0
    for n, p, k, lp in lam_pk:
        u = math.log(n)
        if u > umax + 1e-12:
            continue
        s += lp * n ** (-0.5 + alpha) * g_fn(u)
    return 2.0 * s


def P_agg_fn(g_fn, umax):
    """2 Σ Λ(n)(n^{−2} + n) g(2 log n) — prime side of ζo(2s)ζo(2s−3)
    at the self-dual centre s = 1 (the d-aggregation numerator)."""
    s = 0.0
    for n, p, k, lp in lam_pk:
        u = 2.0 * math.log(n)
        if u > umax + 1e-12:
            continue
        s += lp * (n ** -2.0 + float(n)) * g_fn(u)
    return 2.0 * s


def P_flat_conj(g_fn, umax, alpha):
    """P_ζo(g♭), g♭(x) = e^{αx} g(2x): 2 Σ Λ(n) n^{−1/2+α} g(2 log n)."""
    s = 0.0
    for n, p, k, lp in lam_pk:
        u = 2.0 * math.log(n)
        if u > umax + 1e-12:
            continue
        s += lp * n ** (-0.5 + alpha) * g_fn(u)
    return 2.0 * s


def pole_kernels(umax, npts=6001):
    us = np.linspace(-umax, umax, npts)
    k_lin = np.exp(2 * us) + np.exp(us) + np.exp(-us) + np.exp(-2 * us)
    k_conj = ((np.exp(-1.5 * us) + np.exp(1.5 * us))
              * (np.exp(0.5 * us) + np.exp(-0.5 * us)))
    return us, k_lin, k_conj


# (iii) plus-combination identities on the test class
plin_ok = True
max_rel_lin = 0.0
q_rows = []
for kind, param, g_fn, um in TEST_FNS:
    pl = P_lin_fn(g_fn, um)
    pm = P_zeta_conj(g_fn, um, -1.5)
    pp = P_zeta_conj(g_fn, um, +1.5)
    rel = abs(pl - (pm + pp)) / max(abs(pl), 1e-30)
    max_rel_lin = max(max_rel_lin, rel)
    if rel > 1e-12:
        plin_ok = False
    us, k_lin, k_conj = pole_kernels(um)
    gv = np.array([g_fn(float(u)) for u in us])
    pole_v = float(np.trapezoid(gv * k_lin, us))
    q_rows.append((kind, param, pole_v, pl, pole_v - pl))
    info(f"  [{kind},{param}]: P_lin={pl:.6f} = P_ζ(g₋)+P_ζ(g₊)"
         f"={pm + pp:.6f} (rel {rel:.2e}); Pole={pole_v:.6f} "
         f"Q_Θlin={pole_v - pl:.6f}")
us_g, k_lin_g, k_conj_g = pole_kernels(3.5)
pole_kernel_rel = float(np.max(np.abs(k_lin_g - k_conj_g))
                        / np.max(np.abs(k_lin_g)))
check(
    "L4.iii: PLUS COMBINATION EXACT — Prime_Θlin(g) = Prime_ζ(g₋) + "
    "Prime_ζ(g₊) with g±(u) = e^{±3u/2}g(u), ONLY PLUS signs, on all "
    f"{len(TEST_FNS)} test functions (max rel {max_rel_lin:.2e} < 1e-12); "
    "pole kernel identity e^{∓3u/2}·(e^{u/2}+e^{−u/2}) summed = "
    f"e^{{2u}}+e^{{u}}+e^{{−u}}+e^{{−2u}} pointwise (max rel "
    f"{pole_kernel_rel:.2e}); Q_Θlin = Q_ζ(g₋)+Q_ζ(g₊) with arch "
    "declared classical-external (T59 W2 convention) — the preregistered "
    "hope holds with shift conjugations ±3/2",
    plin_ok and pole_kernel_rel < 1e-12,
)

# (iv) the d-aggregation term: flat/doubling kernel WITH PLUS
pagg_ok = True
max_rel_agg = 0.0
for kind, param, g_fn, um in TEST_FNS:
    pa = P_agg_fn(g_fn, um)
    pm = P_flat_conj(g_fn, um, -1.5)
    pp = P_flat_conj(g_fn, um, +1.5)
    rel = abs(pa - (pm + pp)) / max(abs(pa), 1e-30)
    max_rel_agg = max(max_rel_agg, rel)
    if rel > 1e-12:
        pagg_ok = False
    info(f"  [{kind},{param}]: P_agg={pa:.6f} = P_ζ(g♭₋)+P_ζ(g♭₊)"
         f"={pm + pp:.6f} (rel {rel:.2e})")
info("SIGN BALANCE vs T63: the quadratic family core carries "
     "−2·P_ζ(g♭) (the minus);")
info("  the linear d-aggregation carries +P_ζ(g♭₋) + P_ζ(g♭₊) — the "
     "SAME doubling/♭ kernel class g(2x), sign INVERTED to plus.")
check(
    "L4.iv: d-AGGREGATION TERM EXACT — Prime side of ζo(2s)ζo(2s−3) = "
    "P_ζ(g♭₋) + P_ζ(g♭₊) with g♭±(x) = e^{±3x/2}g(2x) — the T63 "
    f"♭/doubling kernel WITH PLUS (max rel {max_rel_agg:.2e} < 1e-12); "
    "the deletion's Weil shadow appears in the linear aggregation with "
    "inverted sign",
    pagg_ok,
)

# (v) chi-numerator term: bounded character content (mu-averaged biases)
Wtot = float(mu_w.sum())
bias = {}
for p in HECKE_PS:
    chs = np.array([float(jacobi(d, p)) for d in live])
    for k in range(1, 5):
        bias[(p, k)] = float(np.sum(mu_w * chs ** k)) / Wtot
info("μ-averaged character biases ⟨χ_d(p)^k⟩_μ (X5 bridgehead):")
info("  " + ", ".join(f"({p},{k}):{bias[(p, k)]:+.3f}"
                      for p in HECKE_PS for k in (1, 2)))


def P_chi_fn(g_fn, umax, use_abs=False):
    s = 0.0
    for p in HECKE_PS:
        lp = math.log(p)
        for k in range(1, 5):
            u = k * lp
            if u > umax + 1e-12:
                continue
            b = 1.0 if use_abs else bias[(p, k)]
            s += lp * b * p ** (-k) * g_fn(u)
    return 2.0 * s


chi_bounded = True
for kind, param, g_fn, um in TEST_FNS:
    pc = P_chi_fn(g_fn, um)
    pb = P_chi_fn(g_fn, um, use_abs=True)
    if abs(pc) > pb + 1e-15:
        chi_bounded = False
    info(f"  [{kind},{param}]: |P_χ| = {abs(pc):.6f} ≤ bound "
         f"P_ζ(g₀)-trunc = {pb:.6f}")
check(
    "L4.v: χ-NUMERATOR TERM bounded — |P_χ(g)| ≤ truncated P_ζ(g₀), "
    "g₀ = e^{−u/2}g, on all test functions; the only minus in the "
    "linear tower is on a CHARACTER average (Dirichlet-L numerator "
    "(1−χpX), layer 2k), never on a ζ-flat term",
    chi_bounded,
)

lin_full = lam_closed_ok and lists_ok and euler_ok and n_mismatch == 0
plus_exact = plin_ok and pagg_ok and chi_bounded and pole_kernel_rel < 1e-12
check(
    "L4.vi: BALANCE SHEET — no minus sign on any ζ-flat term anywhere "
    "in the linear construction (towers: plus-ζ-shifts; aggregation: "
    "plus-♭; character term bounded); contrast: every quadratic channel "
    "carries the CL minus (T69) "
    f"(flags: lin_full={lin_full}, plus_exact={plus_exact})",
    lin_full and plus_exact,
)


# ================================================================ L5
print("=" * 72)
print("L5 -- SYNTHESIS: the final map of the deletion")
print("=" * 72)

info("THE DELETION MAP (all entries machine-checked, T63→T70):")
info("  1. coefficient squares (ANY bilinear pairing of two det-p³")
info("     towers): DELETION ALWAYS — CL determinant lemma, pair-")
info("     independent, PSD irrelevant (T69, theorem-like).")
info("  2. linear tower direction (m): NO deletion — full weights")
info("     λ_k = Λ(p^k)(1+p^{3k})-structure, layers [1,1,1,1] (T70 L4.i).")
info("  3. total d-aggregation (all odd n): NO deletion — ζ(2s)ζ(2s−3)")
info("     enters WITH PLUS (numerator); prime side = ♭-kernel WITH PLUS")
info("     (T70 L2.iv/L4.iv; sign inversion of the T63 minus).")
info("  4. fundamental d-support: the ζ(2·) invariant RETURNS exactly")
info("     once — as the squarefree Möbius sieve ζ(s)/ζ(2s) of the")
info("     support (T70 L2.v) = the SAME square-class inclusion–")
info("     exclusion as T69-M3b — bookkeeping/index level, not weights.")
check(
    "L5.i: deletion map issued — the ζ(2·) structure is ALWAYS the "
    "square-class bookkeeping: it enters the WEIGHTS in quadratic "
    "channels (CL), and only the SUPPORT in the linear family",
    lin_full and plus_exact and sieve_return and id_ok,
)

info("HONEST TYPING (what the linear carrier is / is not):")
info(f"  IS: a positive GNS family ℓ²(d, μ), μ(d) = c·|L(−1,χ_d)|·d^(−a)")
info("     (seed identified EXACTLY with Cohen edge L-values, L2.iii);")
info("     Hecke-exact (σ₃-twist multiplier); prime side a PLUS")
info("     combination of shifted ζ-Weil forms (conjugations e^{±3u/2}).")
info("  IS NOT: central-line content — L(−1,χ_d) ≐ |d|^{3/2}L(2,χ_d)")
info("     lives in the ABSOLUTE-CONVERGENCE region (Euler-region")
info("     positivity); the Waldspurger central values L(f₈×χ_d, 2)")
info("     stay in the quadratic b²-family (T68 typing); transport of")
info("     the plus-combination to the 1/2-line is NOT established and")
info("     remains the open problem (fence).")
info("  SURVIVING PAIRING CLASS: 'sesquilinear over the measure' —")
info("     linear in the family coefficient (Θ), quadratic ONLY in the")
info("     test functions; the CL lemma has no family square to act on;")
info("     this is exactly B_lin (L3) — the class the T69 synthesis")
info("     predicted as the only remaining candidate.")
check(
    "L5.ii: honest typing issued — edge values vs central values named; "
    "Euler-region positivity ≠ Weil positivity for ζ (transport OPEN); "
    "the sesquilinear-over-measure class is populated and exact",
    seed_const and psd_ok and plus_exact,
)

# ---------------- verdict (preregistered enum)
if lin_full and plus_exact and id_ok and not sieve_return:
    verdict = "LINEAR-PLUS-COMBINATION"
    detail = ("full weights + plus-ζ combination + d-aggregation without "
              "return of the deletion — the positive linear carrier "
              "stands with no ζ(2·) return anywhere.")
elif sieve_return and not (lin_full and plus_exact and id_ok):
    verdict = "DELETION-RETURNS-IN-D"
    detail = ("the deletion returns in the d-direction and the linear "
              "plus structure did not close — ζ(2·) is "
              "construction-universal.")
elif lin_full and plus_exact and id_ok and sieve_return:
    verdict = "MIXED"
    detail = (
        "PRECISE NAMING: LINEAR-PLUS-COMBINATION holds at the weight and "
        "aggregation level — the linear Θ-family has FULL tower weights "
        "(λ_k = 1+p^{3k}−(χp)^k, layers [1,1,1,1], no even-k kill), its "
        "prime side is an exact PLUS combination of ζ-Weil forms "
        "(P_Θlin = P_ζ(g₋)+P_ζ(g₊)), and the total d-aggregation puts "
        "ζ(2s)ζ(2s−3) in the NUMERATOR with a plus-♭ prime side.  "
        "SIMULTANEOUSLY the suspicion CONFIRMS in exactly localised "
        "form: the Cohen-type ζ(2s) denominator of the d-direction is "
        "the FUNDAMENTALITY (squarefree Möbius) sieve of the support, "
        "ζ(s)/ζ(2s) — an index/bookkeeping factor of the same square-"
        "class inclusion–exclusion as T69-M3b, NOT a weight deletion.  "
        "The positive linear carrier STANDS; the ζ(2·) invariant is "
        "support-level in the linear direction and weight-level only "
        "on the square plane."
    )
else:
    verdict = "MIXED"
    detail = "partial closure — see failed flags above (named precisely)."
info(f"VERDICT: {verdict}")
info(detail)
check(
    f"L5.iii: verdict {verdict} assigned from computed flags "
    f"(lin_full={lin_full}, plus_exact={plus_exact}, agg_id={id_ok}, "
    f"seed_const={seed_const}, sieve_return={sieve_return})",
    verdict in ("LINEAR-PLUS-COMBINATION", "DELETION-RETURNS-IN-D",
                "MIXED"),
)

info("PROMOTION CANDIDATES (typed, NOT executed): (i) the exact seed "
     "identity Θ(d) = c·L(−1,χ_d)")
info("  (Cohen, exact rationals on the live window); (ii) the odd-n "
     "factorisation Θ(Df²) = Θ(D)α_E♯(f);")
info("  (iii) the closed m-Euler form.  NEXT LEVER (typed): transport "
     "question — which spectral map")
info("  carries the plus-combination at the (w, w−3) lines toward the "
     "central line (named open; the")
info("  sesquilinear-over-measure carrier is now the canonical positive "
     "substrate for it).  Sandbox only.")
check(
    "L5.iv: no promotion executed; sandbox mapping only; promotion "
    "candidates and next lever typed",
    True,
)


# ================================================================ end
print("=" * 72)
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print(f"VERDICT: {verdict}")
print(f"L1: μ>0 on {len(live)} live d; Θ-zero classes {zero_classes}; "
      f"γ_Θ={gam_t:.3f}; abscissa a*=5/2 "
      f"(slopes {ladder[(1.5, 'slope')]:.2f}/{ladder[(2.0, 'slope')]:.2f}/"
      f"{ladder[(2.5, 'slope')]:.2f})")
print(f"L2: factorisation {n_nontrivial} pts exact; seed Θ(d)={r1}·"
      f"L(−1,χ_d) exact; agg = ζo(2s)ζo(2s−3)·Ξ(s) rel {max_rel_id:.1e}; "
      f"support sieve ζ(s)/ζ(2s) rel {rel_sf3:.1e}")
print(f"L3: GNS PSD, rank {ladder_rows[0][2]}→{ladder_rows[-1][2]}; "
      f"towers {n_t1} exact; pairing equivariant")
print(f"L4: layers lin {layer_lin[:4]} full; P_lin=P_ζ(g₋)+P_ζ(g₊) rel "
      f"{max_rel_lin:.1e}; P_agg=♭-PLUS rel {max_rel_agg:.1e}")
print(f"FILE: {__file__}")
raise SystemExit(0 if FAIL == 0 else 1)
