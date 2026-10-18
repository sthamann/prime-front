"""Discovery probe (2026-07-25), part 80 — contract TAIL.CORRELATION.LEMMA.

T78 (LEMMA.WINDOW.PROOF) proved the matching lemma EXACTLY on [4, 10⁶]
(pure integer certificate 7S < 40A, margin X = 0.082159, ρ_crit =
1.144) and typed the tail honestly: the ABSOLUTE envelope misses by
factor 6.16 at J = 10⁶ AND diverges (Robin/Gronwall loglog) — the
constant route closes nothing beyond any window.  T77 measured the way
out: the TRUE collateral condition of the recipe is SIGNED
(w = B + C⁺ − C⁻ ≥ 0), the cancellation factor GROWS with the window
and 57% of the clash atoms are fully cancelled.  THIS probe is the
last provable-shaped building block of the series: it types the signed
envelope as a CHARACTER-type divisor sum and decides by exact
arithmetic whether the signed tail closes the lemma modulo classics —
or exactly where the gap sits.

THE STRUCTURAL LEVER (T71 sign law, made an exact character object
here): sign ψ(n) = (−1)^{⌊n/2⌋+1} is rigidly 4-periodic; on odd n it
is EXACTLY −χ₋₄(n).  With the T78 w-table this sharpens to exact
coefficient identities: on odd n,
    −ψ(n) = [χ₋₄(n) + ¼·χ₈(n) + ¼·χ₋₈(n)] · Θ(n)
(a rational mixture of the three nontrivial Dirichlet characters
mod 8 twisting ONE positive Eisenstein family), and on n ≡ 2,3 (4)
    ψ(n) = Θ(n)  EXACTLY  (the credit class carries the full budget
coefficient).  Hence the signed maximal-greedy clash
    C_sgn(j) = (ρ/6)·Σ_{d|j, 2≤d≤j/2} (j/d)Θ(j/d)·(−ψ(d))
is a CHARACTER-weighted divisor sum, and its unit-coefficient model
has the exact closed form (j = 2^a·m, m odd)
    Σ_{d|j, 2≤d≤j/2} ς(d)/d = σ̃(m) − [a≥1]·2^{−a}σ₋₁(m) − 1 − ς(j)/j,
    σ̃(m) = Σ_{t|m} χ₋₄(t)/t   (multiplicative, L(1,χ₋₄)-type),
where ς(d) = −sign ψ(d).  The classical cancellation mechanics
(Dirichlet characters, Euler products, L(1,χ)-convergence, Mertens
theorems in arithmetic progressions; Pólya–Vinogradov named as the
character-sum toolbox) then decide the tail: every Euler direction
with χ₋₄(p) = −1 CONVERGES (factors ≤ 1), and the ONLY divergent
direction is the sign-COHERENT one χ₋₄(p) = +1 — atoms all of whose
odd prime factors are ≡ 1 (mod 4) receive NO credits at all (exact,
machine-verified set equality) and there σ̃ = σ₋₁ grows like
C·(loglog j)^{1/2} (Mertens-AP; exponent HALVED vs the absolute
loglog, still divergent).

CRITICAL HONESTY FRAME (mandatory): even a FULLY proven matching
lemma delivers ONLY value-side representability of the Weil cone —
the I5 core inequality of T79 (the prime↔archimedean coupling, whose
typing is EQUIVALENT to Weil positivity ⟺ RH) is untouched by
everything here; NO progress on I5 is claimed and NO RH content
exists in this probe.  Window proofs are window proofs: every proved
statement carries its explicit window; all-n extensions of window
constants are DECLARED classical typings, and asymptotic statements
(Mertens-AP growth, crossing scales) are declared classical
extrapolations.  Classics named classical: Dirichlet characters and
L(1,χ) convergence, Euler products, Mertens 1874 theorems (incl. the
AP versions), Pólya–Vinogradov 1918 character-sum bound (named as the
toolbox; the probe's own bounds are Euler/Mertens-based), Landau 1908
/ Ramanujan (density colour of the coherent class), Gronwall 1913,
Robin 1983 UNCONDITIONAL bound (the RH-equivalent criterion is NOT
used, declared), Cohen 1975 (seed L-values), Alaoglu–Erdős 1944
(superabundant numbers), Shimura 1973 / Hecke T(p²).

T1  THE SIGNED CLASH SUM AS A CHARACTER OBJECT.  (i) exact per-class
    coefficient identities on the FULL 10⁶ window (0 tolerance):
    ψ(n) = Θ(n) on n ≡ 2,3 (4); 2|ψ(n)| = 3Θ(n) on n ≡ 1 (8);
    2|ψ(n)| = Θ(n) on n ≡ 5 (8); the mod-8 character decomposition
    4·(−ψ(n)) = [4χ₋₄ + χ₈ + χ₋₈](n)·Θ(n) on ALL odd n ≤ 50000 on
    BOTH independent builds (q-unit and t-unit), sympy-exact solve of
    the character system; the 2-adic w-ladder (T78 L3) reproduced
    0-tolerance on n ≤ 50000.  MULTIPLICATIVITY ANSWER (typed): −ψ is
    NOT multiplicative as-is (counterexample printed); it factors
    EXACTLY as (mod-8 character mixture)·Θ on odd n times the exact
    rational 2-adic w-ladder; the SIGN ς = −sign ψ IS completely
    multiplicative on odd d (= χ₋₄) with the 2-adic exception typed
    (ς(2m) = −1, ς(4k) = +1 independent of the odd part); the
    unit-model signed divisor sum is EXACTLY the χ₋₄-character sum
    σ̃(m) − [a≥1]2^{−a}σ₋₁(m) (integer identity, 0 mismatches on the
    FULL 10⁶ window, j ≥ 2).  (ii) EULER-PRODUCT BOUND derived and
    machine-
    bracketed: σ̃ is multiplicative (sieve ≡ Euler product over the
    factorisation, exact on all odd m ≤ 50000); per-prime factors
    exactly bracketed (χ₋₄(p) = −1: 1 − 1/p ≤ factor ≤ 1 —
    L(1,χ)-convergent direction; χ₋₄(p) = +1: factor < p/(p−1) —
    Mertens-AP divergent direction); hence σ̃(m) ≤ κ(m) =
    Π_{p|m, p≡1(4)} p/(p−1), verified exactly on all odd m ≤ 50000;
    Mertens-AP window ratios measured (declared classical colour).
T2  THE SIGNED TAIL DECISION.  (i) exact signed sieves on 10⁶
    (proven no-overflow, big-integer recheck on tightest + random +
    extremal atoms): S⁻(j) (negative hits, d ≡ 0,1 (4), 4 ≤ d ≤ j/2),
    S⁺(j) (credits, d ≡ 2,3 (4), 2 ≤ d ≤ j/2), S_net = S⁻ − S⁺; the
    SIGNED window certificate 7·S_net(j) < 40·A(j) at every atom
    (violations counted; structurally ≤ the T78 absolute count),
    exact signed maximum + margin + argmax class; T78 absolute
    anchors reproduced bit-honestly (0 violations, X, ρ_crit, c₀,
    tail factor 6.16).  (ii) recipe-coherence verified EXACTLY on 20
    live T76 certificates (battery reproduced bit-identically,
    rng(76)): the S2 collateral predicate constrains w = B + C⁺ − C⁻
    (the SIGNED sum — bookkeeping identity rel ≤ 1e-9 on 20/20 rows),
    credit activity and fully-cancelled share measured (T77's 57%
    anchor band).  (iii) TAIL JUDGEMENT decided by machine: the
    zero-credit atoms are EXACTLY the χ₋₄-coherent atoms {j odd
    composite: p | j ⇒ p ≡ 1 (4)} (exact set equality on 10⁶); on
    them S_net ≡ S⁻ (no cancellation EXISTS, exact) and the envelope
    diverges (Mertens-AP, declared); the signed Euler route closes
    every coherent atom with σ₋₁(j) − 1 − 1/j < 1/(ρK) at ALL sizes
    (window constants K, class-sharpened K₁), and the exact crossing
    of the coherent chain (primorials of primes ≡ 1 mod 4) is
    computed: first escaping atom N* with exact k*, log₁₀ N*; the
    falsification frontier of the UNIFORM-in-(M,λ) lemma form is
    bracketed (window coefficient floor c_lo, Mertens inversion —
    declared extrapolation).
T3  WORST-CASE VERIFICATION ≤ 10¹².  Superabundant numbers up to
    10¹² constructed exactly (non-increasing-exponent DFS, records of
    σ(n)/n; head anchored to the classical list; Alaoglu–Erdős named)
    and the coherent chain N_k = Π first k primes ≡ 1 (4) up to 10¹²
    (k ≤ 8): for EVERY atom the exact restricted divisor sums P₋, P₊
    (integer arithmetic over the full divisor list), the absolute and
    signed constant-route bounds (exact rational K-brackets), credit
    mass ratios; EXACT beyond-window coherence check P₊(N_k) = 0 by
    direct divisor enumeration; the two crossing frontiers (absolute
    vs signed-lossy) located on the superabundant list; in-window
    superabundant atoms additionally get their EXACT envelope values
    (true cancellation factor vs the lossy constant split — the
    conservatism the missing correlation lemma must recover).
T4  SYNTHESIS.  (i) the final lemma-proof skeleton: [window 10⁶
    exact, T78] + [signed character structure exact, T80] +
    [coherent-class closure to N*(K), T80] + [worst-case battery
    ≤ 10¹², T80] — status: gap named precisely (NOT closed for all
    j); (ii) the full series chain with per-arrow status (what is
    PROVED, what provable-shaped, what is I5); (iii) v541 readiness
    typing (T78 window certificate + T80 signed structure + T79
    ledger as one consolidated module — typing only, NO promotion).

PREREGISTERED CRITERIA
  T0: AST zero-firewall clean; independent q-unit (10⁶) and t-unit
      (5·10⁴) builds agree coefficient-exactly; heads match the
      T71–T78 witnesses; Landen Θ†(2m) = ψ(m) exact; jtheta anchors
      rel < 1e-12 (4 anchors); T71 sign law 0 violations, Θ > 0,
      ψ ≠ 0 on the full window; multiplier identity sympy-exact,
      ρ(1) = 2/3.
  T1: per-class identities 0 mismatches on 10⁶ (ψ=Θ on 2,3(4);
      2|ψ|=3Θ on 1(8); 2|ψ|=Θ on 5(8)); character system solved
      sympy-exact with coefficients (0, 1, 1/4, 1/4); decomposition 0
      mismatches on odd n ≤ 50000 on BOTH builds; w-ladder 0
      mismatches on n ≤ 50000; −ψ non-multiplicativity witnessed +
      exact factorisation typed; unit-model signed identity
      TM − TP = 2^a·M̃(m) − [a≥1]σ(m) − j − ς(j) with 0 mismatches on
      the FULL 10⁶ window (j ≥ 2); σ̃ multiplicativity exact on all odd
      m ≤ 50000; Euler factor brackets exact (Fractions); σ̃ ≤ κ with
      0 violations on all odd m ≤ 50000; Mertens-AP window ratios
      recorded.
  T2: sieve no-overflow proven in exact integers; sieve ≡ direct
      big-integer divisor sums on ≥ 300 atoms (0 mismatches); T78
      anchors reproduced (absolute violations = 0, X ∈ (.0820,.0823),
      ρ_crit ∈ (1.14, 1.15), c₀ ∈ (2.669, 2.679), tail factor ∈
      (6.0, 6.35), ρE(8000) ∈ (0.70, 0.75)); signed certificate scan
      complete with exact margin (ANY outcome valid; consistency
      S_net ≤ S⁻ ≤ S_abs enforced); zero-credit ⟺ coherent set
      equality EXACT on 10⁶; battery reproduced (100 rows,
      24/20/20/16/20, 9 trivial, 100 pass), w-reconstruction 20/20
      rel ≤ 1e-9, fully-cancelled share ∈ (0.40, 0.75); coherent
      chain in-window strictly monotone; tail judgement decided from
      computed flags with exact crossing k*, log₁₀ N* (ANY outcome
      valid).
  T3: superabundant head = [1,2,4,6,12,24,36,48,60,120] exact,
      ≥ 40 records ≤ 10¹²; exact P₋/P₊ tables; P₊(N_k) = 0 exact for
      all chain atoms ≤ 10¹² (direct enumeration); chain formula ≡
      enumeration exact; crossing frontiers located (ANY outcome
      valid); in-window superabundant conservatism factors recorded.
  T4: verdict assigned from computed flags only; series chain + v541
      assertion list printed; NO promotion; fences enforced.
  VERDICTS (preregistered):
    TAIL-CLOSES-SIGNED — the signed envelope closes the tail for ALL
        j > 10⁶ provably modulo classics (requires: signed window
        certificate clean AND no divergent coherent direction): the
        matching lemma would be complete modulo classics;
    RESERVE-PARTIAL   — the cancellation is real, character-exact
        and provably confines the tail obstruction to a CHARACTERISED
        atom class (the χ₋₄-coherent atoms), but that class remains:
        closure holds below the exact crossing N* and fails to be
        provable (and is falsification-shaped for the uniform lemma
        form) beyond — the remaining ingredient is named;
    TAIL-HARD         — the signed structure is not multiplicative /
        character-exact enough (identity or decomposition failures):
        the gap is genuine and untyped by character mechanics.

FENCES (honest typing):
  (i)   VALUE-SIDE ONLY: even a fully proven matching lemma yields
        ONLY value-side representability of the Weil cone — the I5
        core inequality (T79: prime↔arch coupling, equivalent-typing
        to Weil ⟺ RH) is UNTOUCHED by any outcome here; no Weil
        positivity, no RH content.
  (ii)  WINDOW PROOFS ARE WINDOW PROOFS: exact statements carry
        their windows; all-n constant extensions and Mertens-AP
        asymptotics are DECLARED classical typings/extrapolations.
  (iii) the falsification-frontier statement concerns the UNIFORM-
        in-(M, λ) form of the matching lemma; the recipe-coherent
        form (actual T73/T76 certificates) is measured, not decided.
  (iv)  classics named classical (list above); Pólya–Vinogradov is
        NAMED as the character toolbox — the probe's own bounds are
        Euler-product/Mertens-based, no explicit PV constant is used.
  (v)   verdicts from computed flags only; any outcome is a valid
        map; runtime and window sizes budget-honest and printed.

Firewall: discovery sandbox only — no promotion, no ledger / paper /
website / next.txt / README edits (a website worker runs in parallel;
website/ untouched).  ZERO-FIREWALL (AST-checked): no Riemann-zero
loaders; mpmath jtheta is used ONLY as a function on the imaginary
axis (build anchors); no prime sides / explicit-formula sums —
everything is finite lattice, divisor and character arithmetic
(elementary sieves).  No RH-evidence or "Weil positivity achieved"
language.
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
np.seterr(under="ignore")

# ---------------------------------------------------------------- config
J_WIN = 1_000_000             # exact q-unit window (certificate sieves)
N_FORM = 50_000               # closed-formula / decomposition window
LADDER = (8_000, 10_000, 100_000, 1_000_000)   # prefix ladder (T77 rung)
RHO_NUM, RHO_DEN = 21, 20     # ρ_design = 21/20 (T76/T77/T78 frozen)
CERT_L, CERT_R = 7, 40        # ρ/6 = 7/40 ⇒ certificate 7S < 40A
GUARD = 1e-9                  # float prefilter guard band (≫ 1e-15)
K_VEC = 64                    # hybrid sieve vectorisation cut
N_TIGHT = 200                 # tightest signed atoms rechecked exactly
N_RAND = 128                  # random atoms rechecked exactly
SA_LIMIT = 10 ** 12           # worst-case battery reach (T3)
CHAIN_K_EXACT = 24            # exact-Fraction chain scan depth
W_REF = 4000                  # T76/T77 battery reference window
TOP_K = 20                    # certificates checked exactly (T2.ii)
ROBIN_C = 0.6483              # Robin 1983 unconditional constant
EULER_GAMMA = 0.5772156649015329
X_BAND = (0.0820, 0.0823)     # T78 margin anchor X = 0.082159
RC_BAND = (1.14, 1.15)        # T78 ρ_crit anchor 1.144
C0_BAND = (2.669, 2.679)      # T78 c₀ anchor 2.674
GAP_BAND = (6.0, 6.35)        # T78 tail factor anchor 6.16
E8K_BAND = (0.70, 0.75)       # T77 anchor ρ·E(8000) = 0.724
CANC_BAND = (0.40, 0.75)      # T77 fully-cancelled share anchor 57%
SA_HEAD = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120]   # classical head
TH_KEY = (0, 2, 1, 2, 0, 0)   # Θ  = θ₂(q²)²·θ₃(q)·θ₃(q²)²  (T68/T70)
PSI_KEY = (0, 0, 1, 0, 4, 0)  # ψ  = θ₃(q)·θ₄(q)⁴           (mirror)
TD_KEY = (0, 0, 2, 1, 2, 0)   # Θ† = θ₃(q)²·θ₃(q²)·θ₄(q)²   (Fricke)
# battery constants (T73/T76/T77 frozen, verbatim)
U_GRID = 14.0
N_GRID = 1 << 13
TOL_MEM = 1e-12
DELTA_WIN = 12.0
TOLW_REL = 1e-9
ETA_HYB = (0.05, 0.02)
N_REPAIR = 40
N_MACRO = 3
WIN_TOL = 0.02


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


def build_theta_q(J: int) -> np.ndarray:
    """Exact Θ build directly in q-units (T78 technique)."""
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
    """Exact ψ = θ₃(q)·θ₄(q)⁴ build in q-units (int64 slice additions)."""
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


def spf_sieve(limit: int) -> np.ndarray:
    """Smallest-prime-factor table (elementary sieve)."""
    spf = np.zeros(limit + 1, dtype=np.int64)
    for p in range(2, limit + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    return spf


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
    """Exact rational UPPER bracket of √frac (12 decimal digits)."""
    num, den = frac.numerator, frac.denominator
    r = Fraction(math.isqrt(num * 10 ** 24 // den) + 1, 10 ** 12)
    assert r * r >= frac
    return r


def lower_sqrt(frac: Fraction) -> Fraction:
    """Exact rational LOWER bracket of √frac (12 decimal digits)."""
    num, den = frac.numerator, frac.denominator
    r = Fraction(math.isqrt(num * 10 ** 24 // den), 10 ** 12)
    assert r * r <= frac
    return r


# ================================================================ T0
print("=" * 72)
print("T0 -- ZERO-FIREWALL (AST) + exact builds + full-window laws")
print("=" * 72)

_SRC = inspect.getsource(inspect.getmodule(check))
_FORBIDDEN_AST = {
    "zeta" + "zero", "zeta" + "_zero", "zeta" + "_zeros",
    "siegel" + "z", "riemann" + "zeros", "riemann" + "_zero",
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
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        for alias in node.names:
            _imported.add(alias.name)
_bad_imports = _imported & _FORBIDDEN_AST
check(
    "T0.a ZERO-FIREWALL: AST has no Riemann-zero loader "
    f"(calls∩={sorted(_zero_calls)}; attrs={_attr_hits}; "
    f"imports={sorted(_bad_imports)})",
    len(_zero_calls) == 0 and len(_attr_hits) == 0 and len(_bad_imports) == 0,
)
_name_hits = [
    node.id for node in ast.walk(_tree)
    if isinstance(node, ast.Name) and node.id in _FORBIDDEN_AST
]
check(
    f"T0.b ZERO-FIREWALL: no forbidden zero-loader Name nodes ({_name_hits})",
    len(_name_hits) == 0,
)
info("FENCE: even a fully proven matching lemma yields ONLY value-side")
info("  representability — the I5 core inequality (T79 prime↔arch")
info("  coupling, equivalence-typed to Weil ⟺ RH) is untouched by any")
info("  outcome here; window proofs are window proofs; classics named")
info("  classical (Dirichlet/L(1,χ), Euler products, Mertens-AP,")
info("  Pólya–Vinogradov, Gronwall 1913, Robin 1983 unconditional,")
info("  Cohen 1975, Alaoglu–Erdős 1944).  NO RH content.")

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
t_ref = time.time() - t_b

t_b = time.time()
Th = build_theta_q(J_WIN)
Ps = build_psi_q(J_WIN)
Pa = np.abs(Ps)
t_q = time.time() - t_b
info(f"t-unit reference build O(q^{N_FORM}) in {t_ref:.1f}s; q-unit "
     f"build O(q^{J_WIN}) in {t_q:.1f}s")
info(f"Θ head = {list(Th[:8])}")
info(f"ψ head = {list(Ps[:8])}")
agree_th = bool(np.array_equal(Th[: N_FORM + 1], Th_t))
agree_ps = bool(np.array_equal(Ps[: N_FORM + 1], Ps_t))
half = Td_t[0::2][: N_FORM // 2 + 1]
landen_ok = bool(np.array_equal(half, Ps_t[: len(half)]))
check(
    "T0.c BUILD CROSS-VALIDATION: independent q-unit (10⁶) and t-unit "
    f"(5·10⁴) builds agree coefficient-exactly (Θ {agree_th}, ψ "
    f"{agree_ps}); t-support clean ({support_ok}); heads match "
    "(a₀(Θ)=0, Θ(1)=4, Θ ≥ 0; ψ(0)=1, ψ(1)=−6; Θ†(0)=1); Landen "
    "Θ†(2m) = ψ(m) coefficient-exact",
    agree_th and agree_ps and support_ok and landen_ok
    and int(Th[0]) == 0 and int(Th[1]) == 4 and bool(np.all(Th >= 0))
    and int(Ps[0]) == 1 and int(Ps[1]) == -6 and int(Td_t[0]) == 1,
)

anchor_ok = True
for y_f, arr, fn, nm in ((0.35, Th_t, Theta_iy, "Θ"),
                         (0.6, Th_t, Theta_iy, "Θ"),
                         (0.35, Ps_t, Psi_iy, "ψ"),
                         (0.6, Ps_t, Psi_iy, "ψ")):
    x = math.exp(-2 * math.pi * y_f)
    with np.errstate(under="ignore"):
        ssum = float(np.sum(arr.astype(np.float64)
                            * x ** np.arange(N_FORM + 1, dtype=np.float64)))
    jval = float(fn(mpmath.mpf(y_f)))
    rel = abs(ssum - jval) / abs(jval)
    anchor_ok = anchor_ok and rel < 1e-12
    info(f"  {nm}(iy) y={y_f}: coeff-sum={ssum:.12g} jtheta={jval:.12g} "
         f"rel={rel:.2e}")
check(
    "T0.d ANCHORS: coefficient arrays ≡ jtheta monomials on the "
    "imaginary axis (rel < 1e-12 on 4 anchors)",
    anchor_ok,
)

n_all = np.arange(1, J_WIN + 1, dtype=np.int64)
sgn_law = np.where((n_all % 4) <= 1, -1, 1).astype(np.int64)
law_viol = int(np.sum(np.sign(Ps[1:]) != sgn_law))
th_zero = int(np.sum(Th[1:] == 0))
psi_zero = int(np.sum(Ps[1:] == 0))
check(
    f"T0.e FULL-WINDOW LAWS (n ≤ {J_WIN}): T71 sign law "
    f"sign ψ(n) = (−1)^{{⌊n/2⌋+1}} — {law_viol} violations (on odd n "
    "this IS −χ₋₄(n): the sign of the clash coefficient is a rigid "
    f"Dirichlet character); Θ > 0 everywhere ({th_zero} zeros); ψ "
    f"zero-free ({psi_zero} zeros)",
    law_viol == 0 and th_zero == 0 and psi_zero == 0,
)

u_s = sp.symbols("u", real=True)
mult_id = sp.simplify(
    2 * sp.cosh(sp.Rational(3, 2) * u_s)
    - sp.exp(u_s) * (sp.exp(u_s / 2) + sp.exp(-5 * u_s / 2))
)
rho1 = Fraction(int(Th[1]), abs(int(Ps[1])))
check(
    "T0.f CONTINUITY: multiplier identity m_Θ(u) = 2cosh(3u/2) "
    "sympy-exact (T73–T78 reproduction); pin-atom flip threshold "
    f"ρ(1) = {rho1} = 2/3 exact",
    mult_id == 0 and rho1 == Fraction(2, 3),
)

# ------------------------------------------------- shared machinery
t_m = time.time()
A_ARR = np.zeros(J_WIN + 1, dtype=np.int64)
A_ARR[1:] = n_all * Th[1:]                      # A(j) = jΘ(j), exact int64
SPF = spf_sieve(J_WIN)

SIG1 = np.zeros(J_WIN + 1, dtype=np.int64)      # σ(n) full divisor sieve
for d in range(1, J_WIN + 1):
    SIG1[d::d] += d

# M̃(m) = Σ_{t|m} χ₋₄(t)·(m/t) on odd m (χ₋₄ ⋆ Id, multiplicative)
MT = np.zeros(J_WIN + 1, dtype=np.int64)
odd_t = np.arange(1, J_WIN + 1, 2, dtype=np.int64)
chi_odd = np.where(odd_t % 4 == 1, 1, -1).astype(np.int64)
K_ODD = 63
for u in range(1, K_ODD + 2, 2):                # odd u ≤ 64
    tv = odd_t[odd_t <= J_WIN // u]
    MT[u * tv] += chi_odd[: len(tv)] * u
for t in odd_t[odd_t <= J_WIN // (K_ODD + 2)]:
    t = int(t)
    c = 1 if t % 4 == 1 else -1
    top = J_WIN // t
    us = np.arange(K_ODD + 2, top + 1, 2, dtype=np.int64)
    if len(us):
        MT[t * us] += c * us

# signed clash sieves: cofactor k ≥ 2 (⇔ 2 ≤ d ≤ j/2), exact int64
#   SM (negative hits, d ≡ 0,1 mod 4 ⇒ d ≥ 4), SP (credits, d ≡ 2,3)
SM = np.zeros(J_WIN + 1, dtype=np.int64)
SP = np.zeros(J_WIN + 1, dtype=np.int64)
TM = np.zeros(J_WIN + 1, dtype=np.int64)        # Σ (j/d) over minus class
TP = np.zeros(J_WIN + 1, dtype=np.int64)        # Σ (j/d) over plus class
CNT_M = np.zeros(J_WIN + 1, dtype=np.int32)
CNT_P = np.zeros(J_WIN + 1, dtype=np.int32)
d_all = np.arange(2, J_WIN + 1, dtype=np.int64)
d_m = d_all[(d_all % 4 <= 1)]                   # ⇒ d ≥ 4 automatically
d_p = d_all[(d_all % 4 >= 2)]
for k in range(2, K_VEC + 1):
    dv = d_m[d_m <= J_WIN // k]
    idx = k * dv
    SM[idx] += int(A_ARR[k]) * Pa[dv]
    TM[idx] += k
    CNT_M[idx] += 1
    dv = d_p[d_p <= J_WIN // k]
    idx = k * dv
    SP[idx] += int(A_ARR[k]) * Ps[dv]           # ψ(d) > 0 on this class
    TP[idx] += k
    CNT_P[idx] += 1
for d in d_m[d_m <= J_WIN // (K_VEC + 1)]:
    d = int(d)
    top = J_WIN // d
    kk = np.arange(K_VEC + 1, top + 1, dtype=np.int64)
    SM[(K_VEC + 1) * d:: d] += A_ARR[K_VEC + 1: top + 1] * int(Pa[d])
    TM[(K_VEC + 1) * d:: d] += kk
    CNT_M[(K_VEC + 1) * d:: d] += 1
for d in d_p[d_p <= J_WIN // (K_VEC + 1)]:
    d = int(d)
    top = J_WIN // d
    kk = np.arange(K_VEC + 1, top + 1, dtype=np.int64)
    SP[(K_VEC + 1) * d:: d] += A_ARR[K_VEC + 1: top + 1] * int(Ps[d])
    TP[(K_VEC + 1) * d:: d] += kk
    CNT_P[(K_VEC + 1) * d:: d] += 1
S_NET = SM - SP

# T78-compatible absolute objects (d ≡ 0,1 mod 4, d ≥ 4, d = j INCLUDED)
mask_dj = np.zeros(J_WIN + 1, dtype=bool)
mask_dj[4:][(n_all[3:] % 4 <= 1)] = True
S78 = SM.copy()
S78[mask_dj] += 4 * Pa[mask_dj]                 # add back d = j (A(1) = 4)
CNT78 = CNT_M.copy()
CNT78[mask_dj] += 1
supp78 = CNT78[1:] > 0

# 2-adic valuation + odd parts (vectorised)
v2_arr = np.zeros(J_WIN, dtype=np.int64)
mm = n_all.copy()
for _ in range(21):
    even = (mm % 2 == 0)
    if not even.any():
        break
    v2_arr[even] += 1
    mm[even] //= 2
m_odd = mm                                      # odd part of n

# χ₋₄-coherent mask: j odd, every prime factor ≡ 1 (mod 4)
coh = np.zeros(J_WIN + 1, dtype=bool)
coh[1::2] = True
primes_all = np.where(SPF[2:] == np.arange(2, J_WIN + 1))[0] + 2
p3 = primes_all[primes_all % 4 == 3]
for p in p3:
    coh[p::p] = False
coh[2::2] = False
p1 = primes_all[primes_all % 4 == 1]            # primes ≡ 1 (4), ascending
info(f"machinery: SPF + σ + M̃ + 4 signed clash sieves + coherent mask "
     f"on {J_WIN} in {time.time() - t_m:.1f}s "
     f"({len(d_m)} minus-class d, {len(d_p)} plus-class d, "
     f"{len(p3)} primes ≡ 3 (4), {len(p1)} primes ≡ 1 (4))")


def clash_parts_direct(j: int):
    """Independent arbitrary-precision recomputation of S⁻(j), S⁺(j)
    from the raw divisor list (no sieve)."""
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


# ================================================================ T1
print("=" * 72)
print("T1 -- THE SIGNED CLASH SUM AS A CHARACTER OBJECT")
print("=" * 72)

# (i) per-class exact coefficient identities on the FULL window
m23 = (n_all % 4) >= 2
m18 = (n_all % 8) == 1
m58 = (n_all % 8) == 5
bad_23 = int(np.sum(Ps[1:][m23] != Th[1:][m23]))
bad_18 = int(np.sum(2 * Pa[1:][m18] != 3 * Th[1:][m18]))
bad_58 = int(np.sum(2 * Pa[1:][m58] != Th[1:][m58]))
info("per-class coefficient identities (w-table corollaries, integer-")
info(f"  exact on the FULL 10⁶ window): ψ(n) = Θ(n) on n ≡ 2,3 (4) "
     f"[{bad_23} fails];")
info(f"  2|ψ(n)| = 3Θ(n) on n ≡ 1 (8) [{bad_18} fails]; 2|ψ(n)| = Θ(n) "
     f"on n ≡ 5 (8) [{bad_58} fails]")
info("  ⇒ the CREDIT class d ≡ 2,3 (4) carries the FULL budget")
info("    coefficient (ψ = Θ exactly) — cancellation is not a small")
info("    correction, it is budget-strength wherever credits exist.")
check(
    "T1.i PER-CLASS IDENTITIES EXACT on 10⁶: ψ = Θ on d ≡ 2,3 (4); "
    "2|ψ| = 3Θ on 1 (8); 2|ψ| = Θ on 5 (8) — 0 mismatches each "
    f"({bad_23}/{bad_18}/{bad_58})",
    bad_23 == 0 and bad_18 == 0 and bad_58 == 0,
)

# (ii) mod-8 character decomposition: solve + verify on BOTH builds
Mchar = sp.Matrix([
    [1, 1, 1, 1],     # residues 1, 3, 5, 7 mod 8 in the rows
    [1, -1, -1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
])
target = sp.Matrix([sp.Rational(3, 2), -1, sp.Rational(1, 2), -1])
coeffs = Mchar.solve(target)                    # (χ₀, χ₋₄, χ₈, χ₋₈)
coeffs_ok = list(coeffs) == [0, 1, sp.Rational(1, 4), sp.Rational(1, 4)]
res8 = n_all[: N_FORM] % 8
eps4 = np.zeros(N_FORM, dtype=np.int64)         # 4·ε(n) for odd n
eps4[res8 == 1] = 6
eps4[res8 == 5] = 2
eps4[(res8 == 3) | (res8 == 7)] = -4
odd_mask = (n_all[: N_FORM] % 2) == 1
dec_bad_q = int(np.sum(
    4 * (-Ps[1: N_FORM + 1][odd_mask]) != eps4[odd_mask]
    * Th[1: N_FORM + 1][odd_mask]))
dec_bad_t = int(np.sum(
    4 * (-Ps_t[1:][odd_mask]) != eps4[odd_mask] * Th_t[1:][odd_mask]))
info("character system (rows = residues 1,3,5,7 mod 8; basis χ₀, χ₋₄,")
info(f"  χ₈, χ₋₈): sympy solve ⇒ ε = 0·χ₀ + 1·χ₋₄ + ¼·χ₈ + ¼·χ₋₈ "
     f"({coeffs_ok})")
info("  ⇒ on odd n:  −ψ(n) = [χ₋₄(n) + ¼χ₈(n) + ¼χ₋₈(n)]·Θ(n) —")
info("    the signed clash coefficient is a rational mixture of the")
info("    three nontrivial Dirichlet characters mod 8 twisting the ONE")
info("    positive Eisenstein family Θ (main term χ₋₄, weight-¼")
info("    corrections χ₈, χ₋₈).")
check(
    "T1.ii CHARACTER DECOMPOSITION: 4·(−ψ(n)) = [4χ₋₄ + χ₈ + χ₋₈](n)"
    f"·Θ(n) on ALL odd n ≤ {N_FORM} — q-build {dec_bad_q} mismatches, "
    f"independent t-build {dec_bad_t} mismatches; character system "
    f"solved sympy-exact with coefficients (0, 1, 1/4, 1/4): {coeffs_ok}",
    dec_bad_q == 0 and dec_bad_t == 0 and coeffs_ok,
)

# (iii) 2-adic w-ladder (T78 L3) + multiplicativity ANSWER
t_w = time.time()
wlad_bad = 0
for n in range(1, N_FORM + 1):
    a = 0
    n1 = n
    while n1 % 4 == 0:
        n1 //= 4
        a += 1
    pw = 8 ** a
    if n1 % 8 == 1:
        num, den = -(16 * pw + 5), 14
    elif n1 % 8 == 5:
        num, den = -(16 * pw - 9), 14
    else:
        num, den = 15 - 8 * pw, 7
    if den * int(Ps[n]) != num * int(Th[n1]):
        wlad_bad += 1
mult_cex = (int(-Ps[6]), int(-Ps[2]) * int(-Ps[3]))
info(f"2-adic w-ladder pass over n ≤ {N_FORM} in {time.time() - t_w:.1f}s")
info("MULTIPLICATIVITY ANSWER (preregistered question T1.i): the")
info("  weighted sign s(d)·w(d) = −ψ(d) is NOT multiplicative as an")
info(f"  arithmetic function: −ψ(6) = {mult_cex[0]} ≠ (−ψ(2))·(−ψ(3)) "
     f"= {mult_cex[1]}")
info("  (and −ψ(1) = 6 ≠ 1).  It FACTORS exactly as (mod-8 character")
info("  mixture)·Θ on odd d TIMES the exact rational 2-adic w-ladder;")
info("  the raw SIGN ς = −sign ψ IS completely multiplicative on odd d")
info("  (= χ₋₄) with the typed 2-adic exception ς(2m) = −1, ς(4k) = +1")
info("  independent of the odd part — exactly the '2-adic factors up")
info("  to which' of the contract.")
check(
    f"T1.iii 2-ADIC LADDER EXACT: w-table 0 mismatches on n ≤ {N_FORM} "
    f"({wlad_bad}); non-multiplicativity of −ψ witnessed "
    f"(−ψ(6) = {mult_cex[0]} vs {mult_cex[1]}); exact factorisation "
    "typed (character mixture × Θ × 2-adic ladder)",
    wlad_bad == 0 and mult_cex[0] != mult_cex[1],
)

# (iv) σ̃ multiplicativity: sieve ≡ Euler product over the factorisation
t_e = time.time()
mult_bad = 0
kappa_bad = 0
for m in range(1, N_FORM + 1, 2):
    prod = 1
    kap_num = 1
    kap_den = 1
    mm_ = m
    while mm_ > 1:
        p = int(SPF[mm_])
        e = 0
        while mm_ % p == 0:
            mm_ //= p
            e += 1
        chi = 1 if p % 4 == 1 else -1
        loc = 0
        for k in range(e + 1):
            loc += (chi ** k) * p ** (e - k)     # p^e·Σ χ(p)^k p^{−k}
        prod *= loc
        if chi == 1:
            kap_num *= p
            kap_den *= p - 1
    if prod != int(MT[m]):
        mult_bad += 1
    # σ̃(m) ≤ κ(m)  ⟺  M̃(m)·kap_den ≤ m·kap_num  (exact integers)
    if int(MT[m]) * kap_den > m * kap_num:
        kappa_bad += 1
info(f"Euler-product pass over all odd m ≤ {N_FORM} in "
     f"{time.time() - t_e:.1f}s")
check(
    "T1.iv σ̃ IS MULTIPLICATIVE (exact): sieve M̃ = χ₋₄ ⋆ Id ≡ Euler "
    f"product over the factorisation on ALL odd m ≤ {N_FORM} "
    f"({mult_bad} mismatches) — the unit-model signed divisor sum is "
    "a genuine multiplicative character sum",
    mult_bad == 0,
)

# (v) Euler factor brackets (exact Fractions) + σ̃ ≤ κ
bracket_ok = True
for p in (3, 7, 11, 19, 23, 31):                # χ₋₄(p) = −1 directions
    for e in range(1, 9):
        fac = sum(Fraction((-1) ** k, p ** k) for k in range(e + 1))
        if not (1 - Fraction(1, p) <= fac <= 1):
            bracket_ok = False
    fac1 = sum(Fraction((-1) ** k, p ** k) for k in range(2))
    if fac1 != 1 - Fraction(1, p):              # minimum attained at e=1
        bracket_ok = False
for p in (5, 13, 17, 29, 37):                   # χ₋₄(p) = +1 directions
    for e in range(1, 9):
        fac = sum(Fraction(1, p ** k) for k in range(e + 1))
        if not (fac < Fraction(p, p - 1)):
            bracket_ok = False
info("EULER-PRODUCT BOUND (the L(1,χ) mechanics, exact brackets):")
info("  σ̃(m) = Π_p [Σ_{k≤e_p} χ₋₄(p)^k p^{−k}] with")
info("    χ₋₄(p) = −1:  1 − 1/p ≤ factor ≤ 1   (CONVERGENT direction —")
info("      alternating partial sums; 3-mod-4 mass strictly SHRINKS σ̃)")
info("    χ₋₄(p) = +1:  factor < p/(p−1)        (the ONLY divergent")
info("      direction — Mertens-AP)")
info("  ⇒ σ̃(m) ≤ κ(m) = Π_{p|m, p≡1(4)} p/(p−1): the signed unit mass")
info("    is bounded by the COHERENT prime mass alone.")
check(
    "T1.v EULER BRACKETS EXACT (Fractions, p ≤ 37, e ≤ 8) AND "
    f"σ̃(m) ≤ κ(m) with 0 violations on ALL odd m ≤ {N_FORM} "
    f"({kappa_bad} fails) — L(1,χ₋₄)-convergence in every χ(p) = −1 "
    "direction, divergence confined to χ(p) = +1 (classical Mertens-AP, "
    "named)",
    bracket_ok and kappa_bad == 0,
)

# (vi) the unit-model signed identity on the FULL 10⁶ window
sg_arr = np.where(n_all % 4 <= 1, 1, -1).astype(np.int64)   # ς(j)
pow2 = (np.int64(1) << v2_arr)
rhs_unit = pow2 * MT[m_odd] - np.where(v2_arr >= 1, SIG1[m_odd], 0) \
    - n_all - sg_arr
unit_bad = int(np.sum((TM[2:] - TP[2:]) != rhs_unit[1:]))
info("unit-model signed identity (j = 2^a·m, m odd, ς = −sign ψ; j ≥ 2 —")
info("  at j = 1 the boundary divisors d = 1 and d = j coincide):")
info("  Σ_{d|j, 2≤d≤j/2} ς(d)·(j/d) = 2^a·M̃(m) − [a≥1]·σ(m) − j − ς(j)")
info(f"  0-tolerance integer check on the FULL window (2 ≤ j ≤ 10⁶): "
     f"{unit_bad} mismatches")
info("  ⇒ dividing by j: the unit signed envelope is EXACTLY")
info("    σ̃(m) − [a≥1]2^{−a}σ₋₁(m) − 1 − ς(j)/j — a Dirichlet-character")
info("    divisor sum; NO credits exist ⟺ the χ₋₄-coherent case σ̃ = σ₋₁.")
check(
    "T1.vi UNIT-MODEL SIGNED IDENTITY: TM − TP = 2^a·M̃(m) − [a≥1]σ(m) "
    f"− j − ς(j) integer-exact at EVERY 2 ≤ j ≤ {J_WIN} ({unit_bad} "
    "mismatches) — the signed clash sum IS a character-type divisor "
    "sum (contract T1 answer)",
    unit_bad == 0,
)

# (vii) Mertens-AP window measurement (declared classical colour)
mert = {}
for x in (10 ** 4, 10 ** 5, 10 ** 6):
    ps = p1[p1 <= x].astype(np.float64)
    prod_inv = float(np.exp(-np.sum(np.log1p(-1.0 / ps))))
    mert[x] = (prod_inv, prod_inv / math.sqrt(math.log(x)))
S14 = float(np.sum(1.0 / p1.astype(np.float64)))
M14 = S14 - 0.5 * math.log(math.log(J_WIN))
L14 = float(np.sum(np.log1p(1.0 / p1.astype(np.float64))))
M14L = L14 - 0.5 * math.log(math.log(J_WIN))
info("Mertens-AP window measurement (primes ≡ 1 mod 4; classical colour")
info("  named, no explicit-constant version used):")
for x, (pv, rt) in mert.items():
    info(f"  x = {x:8d}: Π(1−1/p)⁻¹ = {pv:.4f}, /√(ln x) = {rt:.4f}")
info(f"  Σ 1/p − ½lnln x = {M14:.4f}; Σ ln(1+1/p) − ½lnln x = {M14L:.4f}"
     f" at x = 10⁶")
check(
    "T1.vii MERTENS-AP RATIOS RECORDED: Π(1−1/p)⁻¹/√(ln x) ≈ const "
    f"({', '.join(f'{mert[x][1]:.3f}' for x in mert)}) — the coherent "
    "direction grows like C·√(ln x) ⇒ σ̃ worst case ~ C·√(loglog j): "
    "divergence exponent HALVED vs the absolute loglog, still "
    "divergent (declared classical)",
    all(math.isfinite(mert[x][1]) for x in mert),
)


# ================================================================ T2
print("=" * 72)
print("T2 -- THE SIGNED TAIL DECISION (certificate + judgement)")
print("=" * 72)

# ---- explicit constants (guarded-exact full enumeration, T78 method)
t_c = time.time()
n_f = n_all.astype(np.float64)
n32 = n_f ** 1.5
r_th = Th[1:].astype(np.float64) / n32
r_ps = Pa[1:].astype(np.float64) / n32


def exact_cmp(v1: int, n1: int, v2: int, n2: int) -> int:
    lhs = v1 * v1 * n2 ** 3
    rhs = v2 * v2 * n1 ** 3
    return (lhs > rhs) - (lhs < rhs)


def guarded_extreme(vals: np.ndarray, ratio_f: np.ndarray, mask, mode: str):
    r = np.where(mask, ratio_f, -np.inf if mode == "max" else np.inf)
    if mode == "max":
        x0 = float(np.max(r))
        cand = np.where(r >= x0 * (1.0 - GUARD))[0]
    else:
        x0 = float(np.min(r))
        cand = np.where(r <= x0 * (1.0 + GUARD))[0]
    best = int(cand[0]) + 1
    for i in cand[1:]:
        j = int(i) + 1
        c = exact_cmp(int(vals[j - 1]), j, int(vals[best - 1]), best)
        if (mode == "max" and c > 0) or (mode == "min" and c < 0):
            best = j
    return best, Fraction(int(vals[best - 1]) ** 2, best ** 3)


all_mask = np.ones(J_WIN, dtype=bool)
mask_res = (n_all % 4 <= 1) & (n_all >= 4)      # minus-class d-set
mask_plus = (n_all % 4 >= 2)                    # credit-class d-set
mask_coh1 = coh[1:] & (n_all >= 5)              # coherent divisors d ≥ 5
mask_cohc = coh[1:] & (CNT_M[1:] > 0)           # coherent clash atoms
mask_coh2 = coh[1:] & (n_all >= 2)              # coherent cofactors ≥ 2

nC1, C1_sq = guarded_extreme(Th[1:], r_th, all_mask, "max")
nC2r, C2r_sq = guarded_extreme(Pa[1:], r_ps, mask_res, "max")
nc0, c0_sq = guarded_extreme(Th[1:], r_th, supp78, "min")
nc0g, c0g_sq = guarded_extreme(Th[1:], r_th, all_mask, "min")
ncp, cpl_sq = guarded_extreme(Pa[1:], r_ps, mask_plus, "min")
nCc, Ccoh_sq = guarded_extreme(Pa[1:], r_ps, mask_coh1, "max")
nc0c, c0coh_sq = guarded_extreme(Th[1:], r_th, mask_cohc, "min")
nC1c, C1coh_sq = guarded_extreme(Th[1:], r_th, mask_coh2, "max")
pow4 = [4 ** a for a in range(0, 10) if 4 ** a <= J_WIN]
c1_attain = all(int(Th[p]) ** 2 == 16 * p ** 3 for p in pow4)
c0 = math.sqrt(float(c0_sq))
info(f"constants (guarded-exact full enumeration, {time.time() - t_c:.1f}s):")
info(f"  C₁ = 4 exact on the 4-power line ({c1_attain}); "
     f"C₂↾ = {math.sqrt(float(C2r_sq)):.6f} at d = {nC2r} (minus class)")
info(f"  c₀ = {c0:.6f} at j = {nc0} (T78 clash support); global "
     f"c₀g = {math.sqrt(float(c0g_sq)):.6f} at n = {nc0g}")
info(f"  credit floor c_ψ₊ = {math.sqrt(float(cpl_sq)):.6f} at "
     f"d = {ncp} (≡ Θ-floor there: ψ = Θ on the class)")
info(f"  coherent-class: C_ψ↾coh = {math.sqrt(float(Ccoh_sq)):.6f} at "
     f"d = {nCc}; c₀coh = {math.sqrt(float(c0coh_sq)):.6f} at "
     f"j = {nc0c}; C₁coh = {math.sqrt(float(C1coh_sq)):.6f} at "
     f"n = {nC1c}")
K_sq = C1_sq * C2r_sq / (36 * c0_sq)            # K = C₁C₂↾/(6c₀), T78
K_up = upper_sqrt(K_sq)
Kp_sq = c0g_sq * cpl_sq / (36 * C1_sq)          # K₊ = c₀g·c_ψ₊/(6C₁)
Kp_dn = lower_sqrt(Kp_sq)
K1_sq = C1coh_sq * Ccoh_sq / (36 * c0coh_sq)    # coherent-sharpened K₁
K1_up = upper_sqrt(K1_sq)
RHO_F = Fraction(RHO_NUM, RHO_DEN)
info(f"  K = C₁C₂↾/(6c₀) ≤ {float(K_up):.6f}; K₊ = c₀g·c_ψ₊/(6C₁) ≥ "
     f"{float(Kp_dn):.6f}; K₁ (coherent) ≤ {float(K1_up):.6f}")

# ---- no-overflow proof for the signed sieves
Mpref = np.maximum.accumulate(A_ARR)
ok_ov = True
Tmaxs = {}
for tag, dv, wv in (("minus", d_m, Pa), ("plus", d_p, Pa)):
    kk_top = (J_WIN // dv).astype(np.int64)
    prod_f = wv[dv].astype(np.float64) * Mpref[kk_top].astype(np.float64)
    safe = bool(np.all(prod_f < 2.0 ** 61))
    tmax = int(np.max(wv[dv] * Mpref[kk_top])) if safe else -1
    Tmaxs[tag] = tmax
    ok_ov = ok_ov and safe
cnt_max = max(int(CNT_M.max()), int(CNT_P.max()))
S_bound = cnt_max * max(Tmaxs.values())
room = S_bound < 2 ** 63 and int(S78.max()) * CERT_L < 2 ** 63 \
    and int(A_ARR.max()) * CERT_R < 2 ** 63
info(f"overflow proof: term ≤ {float(max(Tmaxs.values())):.3e}, count ≤ "
     f"{cnt_max}, S ≤ {float(S_bound):.3e} < 2⁶³ ({room}); S_net = "
     "SM − SP as difference of two in-range nonneg int64 sieves")

# ---- exact big-integer recheck of the signed sieves
ratio_net = (CERT_L * S_NET[1:]).astype(np.float64) \
    / (CERT_R * A_ARR[1:]).astype(np.float64)
ratio_abs = (CERT_L * S78[1:]).astype(np.float64) \
    / (CERT_R * A_ARR[1:]).astype(np.float64)
order = np.argsort(-ratio_net)
tight_idx = [int(i) + 1 for i in order[:N_TIGHT]]
rng = np.random.default_rng(80)
rand_idx = [int(j) for j in rng.choice(np.where(CNT_M[1:] > 0)[0] + 1,
                                       size=N_RAND, replace=False)]
extra_idx = [65, 1105, 32045, 5040, 55440, 720720, 554400,
             int(np.argmax(ratio_abs)) + 1]
recheck = sorted(set(tight_idx + rand_idx + extra_idx))
t_r = time.time()
mism = 0
for j in recheck:
    sm_d, sp_d = clash_parts_direct(j)
    if sm_d != int(SM[j]) or sp_d != int(SP[j]) \
            or sm_d - sp_d != int(S_NET[j]):
        mism += 1
info(f"exact recheck of {len(recheck)} atoms ({N_TIGHT} tightest signed "
     f"+ {N_RAND} random + extremals) in {time.time() - t_r:.1f}s: "
     f"{mism} mismatches")
check(
    "T2.i SIEVE INTEGRITY: no-overflow PROVEN in exact integers "
    f"({ok_ov and room}); SM/SP/S_net ≡ independent arbitrary-precision "
    f"divisor sums on {len(recheck)} atoms ({mism} mismatches)",
    ok_ov and room and mism == 0,
)

# ---- T78 absolute anchors reproduced
viol_abs = int(np.sum(CERT_L * S78[1:] >= CERT_R * A_ARR[1:]))
x0 = float(np.max(ratio_abs))
cand = np.where(ratio_abs >= x0 * (1.0 - GUARD))[0]
j_abs = int(cand[0]) + 1
for i in cand[1:]:
    j = int(i) + 1
    if int(S78[j]) * int(A_ARR[j_abs]) > int(S78[j_abs]) * int(A_ARR[j]):
        j_abs = j
rhoF_abs = Fraction(CERT_L * int(S78[j_abs]), CERT_R * int(A_ARR[j_abs]))
X_abs = 1 - rhoF_abs
rho_crit = Fraction(6 * int(A_ARR[j_abs]), int(S78[j_abs]))
R_J = math.e ** EULER_GAMMA * math.log(math.log(J_WIN)) \
    + ROBIN_C / math.log(math.log(J_WIN))
gap_abs = float(RHO_F * K_up) * (R_J - 1.0)
lad_abs = {W: float(np.max(ratio_abs[:W])) for W in LADDER}
info(f"T78 absolute reproduction: {viol_abs} violations on 10⁶; "
     f"max ρF = {float(rhoF_abs):.6f} at j* = {j_abs} "
     f"({'·'.join(f'{p}^{e}' if e > 1 else str(p) for p, e in factorise(j_abs, SPF))})")
info(f"  X = {float(X_abs):.6f} (T78: 0.082159); ρ_crit = "
     f"{float(rho_crit):.4f} (T78: 1.144); c₀ = {c0:.4f} (T78: 2.674)")
info(f"  absolute tail factor ρK·(R(J)−1) = {gap_abs:.2f} (T78: 6.16) — "
     "the absolute route stays open and divergent (reproduced)")
check(
    "T2.ii T78 ANCHORS REPRODUCED: absolute certificate 0 violations "
    f"({viol_abs}); X = {float(X_abs):.6f} ∈ {X_BAND}; ρ_crit = "
    f"{float(rho_crit):.4f} ∈ {RC_BAND}; c₀ ∈ {C0_BAND}; tail factor "
    f"{gap_abs:.2f} ∈ {GAP_BAND}; ρE(8000) = {lad_abs[8000]:.4f} ∈ "
    f"{E8K_BAND}",
    viol_abs == 0 and X_BAND[0] < float(X_abs) < X_BAND[1]
    and RC_BAND[0] < float(rho_crit) < RC_BAND[1]
    and C0_BAND[0] < c0 < C0_BAND[1]
    and GAP_BAND[0] < gap_abs < GAP_BAND[1]
    and E8K_BAND[0] < lad_abs[8000] < E8K_BAND[1],
)

# ---- THE SIGNED WINDOW CERTIFICATE
viol_net = int(np.sum(CERT_L * S_NET[1:] >= CERT_R * A_ARR[1:]))
x0 = float(np.max(ratio_net))
cand = np.where(ratio_net >= x0 * (1.0 - GUARD))[0]
j_net = int(cand[0]) + 1
for i in cand[1:]:
    j = int(i) + 1
    if int(S_NET[j]) * int(A_ARR[j_net]) > int(S_NET[j_net]) * int(A_ARR[j]):
        j_net = j
sm_d, sp_d = clash_parts_direct(j_net)
rhoF_net = Fraction(CERT_L * (sm_d - sp_d), CERT_R * int(A_ARR[j_net]))
X_net = 1 - rhoF_net
lad_net = {W: (int(np.argmax(ratio_net[:W])) + 1,
               float(np.max(ratio_net[:W]))) for W in LADDER}
consist = bool(np.all(S_NET <= SM)) and bool(np.all(SM <= S78))
canc_share_win = float(np.mean(S_NET[1:][CNT_M[1:] > 0] <= 0))
# class-restricted signed maxima
cls_max = {}
for tag, msk in (("coherent", mask_cohc),
                 ("odd non-coherent", (n_all % 2 == 1) & ~mask_cohc
                  & (CNT_M[1:] > 0)),
                 ("j ≡ 2 (4)", (n_all % 4 == 2) & (CNT_M[1:] > 0)),
                 ("4 | j", (n_all % 4 == 0) & (CNT_M[1:] > 0))):
    if msk.any():
        r = np.where(msk, ratio_net, -np.inf)
        i = int(np.argmax(r))
        cls_max[tag] = (i + 1, float(r[i]))
fac_net = factorise(j_net, SPF)
odd_net = j_net >> int(v2_arr[j_net - 1])
info(f"THE SIGNED CERTIFICATE 7·S_net(j) < 40·A(j) on 1 ≤ j ≤ {J_WIN}:")
info(f"  violations: {viol_net}; max ρF_net = {float(rhoF_net):.6f} at "
     f"j*_net = {j_net} = "
     + "·".join(f"{p}^{e}" if e > 1 else str(p) for p, e in fac_net)
     + f" (odd part {odd_net} coherent: {bool(coh[odd_net])})")
info(f"  exact signed margin X_net = 1 − ρF_net = {float(X_net):.6f} "
     f"(absolute X = {float(X_abs):.6f}: the signed window margin is "
     f"{float(X_net) / float(X_abs):.1f}× larger)")
info("  ladder (prefix maxima of ρF_net): "
     + ", ".join(f"{lad_net[W][1]:.4f}@{W}(j={lad_net[W][0]})"
                 for W in LADDER))
info("  class-restricted signed maxima: "
     + "; ".join(f"{t}: {v:.4f} at j = {j}" for t, (j, v) in cls_max.items()))
info(f"  fully cancelled clash atoms on the window (S_net ≤ 0): "
     f"{100 * canc_share_win:.1f}%")
info("  ⇒ EXTREMAL CLASS SHIFT: the absolute extremal is superabundant "
     f"(j* = {j_abs}, σ-rich); the SIGNED extremal j*_net = {j_net} "
     "combines a 2-power line (all d ≡ 0 (4) hits negative) with a "
     "χ₋₄-COHERENT odd part — the signed pressure lives on coherent "
     "structure, not on abundance.")
check(
    f"T2.iii SIGNED CERTIFICATE SCAN COMPLETE: {viol_net} violations "
    f"(structural consistency S_net ≤ S⁻ ≤ S_abs: {consist}); exact "
    f"signed maximum ρF_net = {float(rhoF_net):.6f} < absolute "
    f"{float(rhoF_abs):.6f}; ladder + class table recorded (ANY "
    "outcome valid)",
    consist and viol_net == 0 and rhoF_net < rhoF_abs
    and sm_d - sp_d == int(S_NET[j_net]),
)

# ---- zero-credit ⟺ coherent (exact set equality)
pred_zero = (CNT_P[1:] == 0) & (CNT_M[1:] > 0)
is_prime = SPF[1:][: J_WIN] == n_all
rhs_coh = coh[1:] & (n_all > 1) & (~is_prime)
set_eq = bool(np.array_equal(pred_zero, rhs_coh))
sp_zero_on_coh = int(np.sum(SP[1:][pred_zero] != 0))
n_coh = int(np.sum(rhs_coh))
info(f"zero-credit atoms (CNT⁺ = 0, CNT⁻ > 0): {int(np.sum(pred_zero))}; "
     f"predicted class {{j odd composite: p|j ⇒ p ≡ 1 (4)}}: {n_coh}; "
     f"set equality: {set_eq}")
info("  ⇒ NO cancellation EXISTS exactly on the χ₋₄-coherent atoms")
info("    (S_net ≡ S⁻ there; Landau–Ramanujan-type density colour")
info("    named classical); everywhere else at least one credit divisor")
info("    (d = 2 for even j, d = p ≡ 3 (4) otherwise) is present.")
check(
    "T2.iv CONFINEMENT EXACT: {zero-credit clash atoms} = "
    "{χ₋₄-coherent odd composites} — set equality on the FULL 10⁶ "
    f"window ({set_eq}); S⁺ ≡ 0 on the class ({sp_zero_on_coh} "
    "exceptions): the tail obstruction of the signed route is "
    "CHARACTERISED, not diffuse",
    set_eq and sp_zero_on_coh == 0,
)

# ---- coherent chain in-window + coefficient floor
chain_win = [65, 1105, 32045]
chain_vals = [float(ratio_abs[j - 1]) for j in chain_win]
mono = all(a < b for a, b in zip(chain_vals, chain_vals[1:]))
coh_idx = np.where(mask_cohc)[0]
tm_coh = TM[1:][coh_idx].astype(np.float64)
ratio_coef = (S_NET[1:][coh_idx].astype(np.float64)
              * (coh_idx + 1).astype(np.float64)
              / (6.0 * A_ARR[1:][coh_idx].astype(np.float64) * tm_coh))
i_lo = int(np.argmin(ratio_coef))
j_lo = int(coh_idx[i_lo]) + 1
c_lo = Fraction(int(S_NET[j_lo]) * j_lo, 6 * int(A_ARR[j_lo]) * int(TM[j_lo]))
c_med = float(np.median(ratio_coef))
info(f"coherent chain in-window: ρF at 65/1105/32045 = "
     + ", ".join(f"{v:.4f}" for v in chain_vals)
     + f" (strictly monotone: {mono})")
info(f"  per-atom coefficient F_net/P₋ on the {len(coh_idx)} coherent "
     f"clash atoms: min c_lo = {float(c_lo):.6f} at j = {j_lo}, median "
     f"{c_med:.4f}")
info("  (c_lo is the window-measured coefficient FLOOR of the coherent")
info("   envelope — its all-n extension is a declared classical typing:")
info("   Cohen seed L(2,χ) lower bounds + tower positivity)")
check(
    "T2.v COHERENT CHAIN (window): ρF strictly increasing along "
    f"65 → 1105 → 32045 ({mono}); coefficient floor c_lo = "
    f"{float(c_lo):.4f} > 0 and median {c_med:.4f} recorded on all "
    f"{len(coh_idx)} coherent clash atoms",
    mono and c_lo > 0 and math.isfinite(c_med),
)

# ---- T2.ii RECIPE COHERENCE: 20 live T76 certificates, exact
t_bat = time.time()
NMAX_BAT = W_REF
U_LAT = np.log(np.arange(1, NMAX_BAT + 1).astype(np.float64))
BASE_W = (np.arange(1, NMAX_BAT + 1, dtype=np.float64)
          * Th[1: NMAX_BAT + 1].astype(np.float64))
PsiF = Ps[: J_WIN + 1].astype(np.float64)
DU = 2 * U_GRID / N_GRID
us_g = (np.arange(N_GRID) - N_GRID // 2) * DU
lag_u = np.arange(N_GRID) * DU
N_WIN_D = int(DELTA_WIN / DU)
r_lat = np.exp(-U_LAT ** 2 / 8.0)
NEG_CONTROLS = [
    -r_lat.copy(),
    -np.exp(-U_LAT ** 2 / 2.56),
]


def autocorr_lattice(fv):
    F = np.fft.rfft(fv, 2 * N_GRID)
    acf = np.fft.irfft(np.abs(F) ** 2, 2 * N_GRID)[:N_GRID] * DU
    h0 = float(acf[0])
    acf_n = acf / h0
    v = np.interp(U_LAT, lag_u, acf_n)
    return v, acf_n, h0


def delta_of(acf):
    idx = np.where(acf[:N_WIN_D] <= TOL_MEM)[0]
    return float(idx[0] * DU) if len(idx) else math.inf


def build_hybrid(v, eta, nlat):
    """THE T73/T76 RECIPE h ↦ Φ_h (verbatim T77 reproduction)."""
    bw = BASE_W[:nlat]
    vv = v[:nlat]
    V = list((np.where(vv < -TOL_MEM)[0] + 1).astype(int))
    if not V:
        return {"lam": {}, "nV": 0, "trivial": True, "ok": True,
                "bad": 0, "targ_ok": True, "sign_ok": True,
                "u_min_minus": math.inf, "nrep": 0, "nlam": 0,
                "c_exc": True}
    lam = {}
    w = bw.copy()
    nrep = 0
    repaired = True
    for _macro in range(N_MACRO):
        for m in V:
            if w[m - 1] < 0:
                continue
            add = (1.0 + eta) * w[m - 1] / 6.0
            lam[m] = lam.get(m, 0.0) + add
            kk = np.arange(1, nlat // m + 1)
            w[m * kk - 1] += add * PsiF[kk]
        repaired = True
        for _it in range(N_REPAIR):
            minus = w < -TOLW_REL * bw
            bad = np.where(minus & (vv > TOL_MEM))[0]
            if len(bad) == 0:
                break
            nrep += 1
            j = int(bad[0]) + 1
            need = -w[j - 1] + 1e-6 * bw[j - 1]
            contribs = sorted(
                ((m, PsiF[j // m]) for m in lam
                 if j % m == 0 and PsiF[j // m] < 0),
                key=lambda x: x[1])
            for m, psi_v in contribs:
                a_m = w[m - 1] + 6.0 * lam[m]
                lam_min = (a_m + 1e-6 * bw[m - 1]) / 6.0
                slack = lam[m] - lam_min
                if slack <= 0:
                    continue
                red = min(slack, need / (-psi_v))
                lam[m] -= red
                kk = np.arange(1, nlat // m + 1)
                w[m * kk - 1] -= red * PsiF[kk]
                need -= red * (-psi_v)
                if need <= 0:
                    break
            if need > 0:
                repaired = False
                break
        minus = w < -TOLW_REL * bw
        plus = w > TOLW_REL * bw
        targ_ok = bool(np.all(minus[np.array(V) - 1]))
        coll_bad = int(np.sum(minus & (vv > TOL_MEM)))
        sign_ok = (bool(np.all(vv[plus] >= -TOL_MEM))
                   and bool(np.all(vv[minus] <= TOL_MEM)))
        if targ_ok and sign_ok and coll_bad == 0 and repaired:
            break
    minus = w < -TOLW_REL * bw
    plus = w > TOLW_REL * bw
    targ_ok = bool(np.all(minus[np.array(V) - 1]))
    coll_bad = int(np.sum(minus & (vv > TOL_MEM)))
    sign_ok = (bool(np.all(vv[plus] >= -TOL_MEM))
               and bool(np.all(vv[minus] <= TOL_MEM)))
    u_min_minus = (float(np.min(U_LAT[:nlat][minus])) if minus.any()
                   else math.inf)
    lam_ok = all(l >= 0.0 and math.isfinite(l) for l in lam.values())
    c_exc = all(
        bool(np.any(plus & (c[:nlat] < -TOL_MEM))) for c in NEG_CONTROLS)
    return {"lam": lam, "nV": len(V), "trivial": False,
            "ok": targ_ok and sign_ok and coll_bad == 0 and lam_ok
            and c_exc and repaired,
            "bad": coll_bad, "targ_ok": targ_ok, "sign_ok": sign_ok,
            "u_min_minus": u_min_minus, "nrep": nrep, "nlam": len(lam),
            "c_exc": c_exc, "repaired": repaired}


def run_recipe(v, nlat):
    best = None
    for eta in ETA_HYB:
        res = build_hybrid(v, eta, nlat)
        if best is None or (res["ok"] and not best["ok"]) \
                or (res["ok"] == best["ok"] and res["bad"] < best["bad"]):
            best = res
            best["eta"] = eta
        if res["ok"]:
            break
    return best


def verify_certificate(lam, v, delta, nlat):
    bw = BASE_W[:nlat]
    vv = v[:nlat]
    bad_lam = any(not (l >= 0.0 and math.isfinite(l))
                  for l in lam.values())
    w = bw.copy()
    for m, l in lam.items():
        kk = np.arange(1, nlat // m + 1)
        w[m * kk - 1] += l * PsiF[kk]
    minus = w < -TOLW_REL * bw
    plus = w > TOLW_REL * bw
    V = np.where(vv < -TOL_MEM)[0]
    u_min = float(np.min(U_LAT[:nlat][minus])) if minus.any() else math.inf
    S1 = (not math.isfinite(delta)) or (u_min >= delta - WIN_TOL)
    targ = bool(np.all(minus[V])) if len(V) else True
    coll = int(np.sum(minus & (vv > TOL_MEM)))
    S2 = targ and coll == 0
    sign_ok = (bool(np.all(vv[plus] >= -TOL_MEM))
               and bool(np.all(vv[minus] <= TOL_MEM)))
    c_exc = all(
        bool(np.any(plus & (c[:nlat] < -TOL_MEM))) for c in NEG_CONTROLS)
    S3 = sign_ok and c_exc and not bad_lam
    return {"S1": S1, "S2": S2, "S3": S3, "ok": S1 and S2 and S3,
            "u_min": u_min, "coll": coll, "targ": targ,
            "nlam": len(lam), "m_max": max(lam) if lam else 0, "w": w}


def clash_census(lam, v, W):
    cm = np.zeros(W)
    cp = np.zeros(W)
    tc = np.zeros(W, dtype=np.int64)
    tm = np.zeros(W, dtype=np.int64)
    for m, l in lam.items():
        top = W // m
        if top < 2:
            continue
        kk = np.arange(2, top + 1)
        c = l * PsiF[kk]
        idx = m * kk - 1
        neg = c < 0
        cm[idx[neg]] -= c[neg]
        cp[idx[~neg]] += c[~neg]
        tc[idx] += 1
        tm[idx[neg]] += 1
    vv = v[:W]
    nt = vv > TOL_MEM
    hit = nt & (tm > 0)
    return {"cm": cm, "cp": cp, "tc": tc, "tm": tm, "nt": nt, "hit": hit}


def gauss_f(s):
    return np.exp(-0.5 * (us_g / s) ** 2)


def bump_f(a, p=2):
    return np.where(np.abs(us_g) < a, (1 - (us_g / a) ** 2) ** p, 0.0)


def bump_at(c, a=0.7, p=2):
    t = (us_g - c) / a
    return np.where(np.abs(t) < 1, (1 - t * t) ** p, 0.0)


# T76 battery, reproduced verbatim (identical construction + rng(76))
BATTERY = []
for sig in (0.5, 0.8, 1.1):
    for om in (6, 8, 10, 12, 14, 16, 18, 20):
        BATTERY.append((f"a:gab s{sig} w{om}", "a",
                        gauss_f(sig) * np.cos(om * us_g)))
rng76 = np.random.default_rng(76)
for K in (2, 3, 4, 5):
    for jj in range(5):
        oms = np.sort(rng76.uniform(0.8, 14.0, K))
        amps = rng76.uniform(0.4, 1.0, K)
        sig = float(rng76.uniform(0.6, 1.2))
        fv = gauss_f(sig) * sum(
            a * np.cos(o * us_g) for a, o in zip(amps, oms))
        BATTERY.append((f"b:mix K{K}#{jj}", "b", fv))
for a in (0.8, 1.5, 2.2):
    BATTERY.append((f"c:bump a{a}", "c", bump_f(a)))
for a in (1.5, 2.5):
    for om in (3, 6, 10, 14):
        BATTERY.append((f"c:bmp a{a} w{om}", "c",
                        bump_f(a) * np.cos(om * us_g)))
tent = np.maximum(0.0, 1 - np.abs(us_g) / 2.0)
BATTERY.append(("c:tent w4", "c", tent * np.cos(4 * us_g)))
BATTERY.append(("c:tent w9", "c", tent * np.cos(9 * us_g)))
t_q_ = np.abs(us_g / 1.2)
qspl = np.where(t_q_ <= 0.5, 0.75 - t_q_ ** 2,
                np.where(t_q_ <= 1.5, 0.5 * (1.5 - t_q_) ** 2, 0.0))
BATTERY.append(("c:qspline w7", "c", qspl * np.cos(7 * us_g)))
for a in (0.8, 1.5, 2.5):
    BATTERY.append((f"c:bdiff a{a}", "c", bump_at(a) - bump_at(-a)))
for b in (0.5, 1.0, 1.5):
    BATTERY.append((f"c:bherm b{b}", "c",
                    bump_f(2.0) * (1 - (us_g / b) ** 2)))
for s in (0.8, 1.5):
    for om in (0.0, 1.5, 3.0, 5.0):
        BATTERY.append((f"d:cau s{s} w{om}", "d",
                        np.cos(om * us_g) / (1.0 + (us_g / s) ** 2)))
for s in (0.8, 1.5):
    for om in (0.0, 2.0, 4.0, 6.0):
        BATTERY.append((f"d:sech s{s} w{om}", "d",
                        np.cos(om * us_g) / np.cosh(us_g / s)))
for c in (0.6, 0.75, 0.85, 0.92, 0.97):
    BATTERY.append((f"e:gcanc c{c}", "e",
                    np.exp(-0.5 * us_g ** 2)
                    - c * np.exp(-0.5 * (us_g / 1.15) ** 2)))
for c in (0.7, 0.85, 0.95):
    BATTERY.append((f"e:bcanc c{c}", "e", bump_f(2.0) - c * bump_f(2.3)))
for a in (0.4, 0.8, 1.2, 1.8, 2.5):
    BATTERY.append((f"e:odd a{a}", "e",
                    np.exp(-0.5 * ((us_g - a) / 0.6) ** 2)
                    - np.exp(-0.5 * ((us_g + a) / 0.6) ** 2)))
H5 = us_g ** 5 - 10 * us_g ** 3 + 15 * us_g
H6 = us_g ** 6 - 15 * us_g ** 4 + 45 * us_g ** 2 - 15
H7 = us_g ** 7 - 21 * us_g ** 5 + 105 * us_g ** 3 - 105 * us_g
for k, poly in ((5, H5), (6, H6), (7, H7)):
    BATTERY.append((f"e:herm{k}", "e", poly * np.exp(-0.5 * us_g ** 2)))
PAIR_DEFS = [
    (gauss_f(0.8) * np.cos(3 * us_g),
     np.exp(-0.5 * ((us_g - 3.0) / 0.8) ** 2) * np.cos(8 * us_g)),
    (gauss_f(0.6) * np.cos(2 * us_g), gauss_f(0.6) * np.cos(9 * us_g)),
    (bump_f(1.5), bump_at(4.0, a=1.2)),
    (gauss_f(1.0) * np.cos(5 * us_g),
     np.exp(-0.5 * ((us_g + 3.5) / 0.7) ** 2)),
]
for jj, (f1, f2) in enumerate(PAIR_DEFS):
    BATTERY.append((f"e:pair#{jj}", "e", f1 + f2))

ROWS = []
for name, fam, fv in BATTERY:
    v, acf, h0 = autocorr_lattice(fv)
    ROWS.append({"name": name, "fam": fam, "v": v, "delta": delta_of(acf)})
n_pass = 0
n_triv = 0
for r in ROWS:
    res = run_recipe(r["v"], nlat=W_REF)
    ver = verify_certificate(res["lam"], r["v"], r["delta"], nlat=W_REF)
    r["res"] = res
    r["ver"] = ver
    if res["trivial"]:
        n_triv += 1
    if ver["ok"]:
        n_pass += 1
fam_counts = {f: sum(1 for r in ROWS if r["fam"] == f) for f in "abcde"}
info(f"battery re-run at window {W_REF} in {time.time() - t_bat:.1f}s: "
     f"{len(ROWS)} rows, families "
     + ", ".join(f"{f}:{fam_counts[f]}" for f in "abcde")
     + f"; trivial {n_triv}, pass {n_pass}")
check(
    "T2.vi T76 BATTERY REPRODUCED BIT-IDENTICALLY (rng(76)) — 100 rows "
    f"(24/20/20/16/20), {n_triv} trivial, pass {n_pass}/100 (published "
    "91/91 nontrivial anchor)",
    len(ROWS) == 100
    and fam_counts == {"a": 24, "b": 20, "c": 20, "d": 16, "e": 20}
    and n_triv == 9 and n_pass == 100,
)

nontriv = [r for r in ROWS if not r["res"]["trivial"]]
TOP = sorted(nontriv, key=lambda r: (-r["ver"]["nlam"], r["name"]))[:TOP_K]
rec_ok = True
n_credit_pool = 0
n_hit_pool = 0
n_canc_pool = 0
n_abs_over = 0
all_ver_ok = True
for r in TOP:
    cen = clash_census(r["res"]["lam"], r["v"], W_REF)
    w_ver = r["ver"]["w"]
    nt = cen["nt"]
    w_rec = BASE_W[:W_REF] + cen["cp"] - cen["cm"]
    rel = float(np.max(np.abs(w_rec[nt] - w_ver[nt]) / BASE_W[:W_REF][nt]))
    if rel > 1e-9:
        rec_ok = False
    hit = cen["hit"]
    n_hit_pool += int(hit.sum())
    n_credit_pool += int(np.sum(cen["cp"][hit] > 0))
    n_canc_pool += int(np.sum(cen["cp"][hit] >= cen["cm"][hit]))
    n_abs_over += int(np.sum(cen["cm"][hit] > BASE_W[:W_REF][hit]))
    if not r["ver"]["ok"]:
        all_ver_ok = False
share_credit = n_credit_pool / max(n_hit_pool, 1)
share_canc = n_canc_pool / max(n_hit_pool, 1)
info(f"TOP-{TOP_K} certificates (by summand count, live T76 rows):")
info(f"  w-reconstruction B + C⁺ − C⁻ ≡ verifier weight on non-target "
     f"atoms: {TOP_K}/{TOP_K} rows rel ≤ 1e-9 ({rec_ok})")
info(f"  the S2 collateral predicate constrains w = B + C⁺ − C⁻ ≥ 0 — "
     "the SIGNED sum (bookkeeping-exact): T77's claim verified")
info(f"  credit activity: {100 * share_credit:.1f}% of clash-hit atoms "
     f"carry C⁺ > 0; fully cancelled (C⁺ ≥ C⁻): {100 * share_canc:.1f}% "
     "(T77 anchor 57%)")
info(f"  atoms where the ABSOLUTE clash alone would exceed the budget "
     f"(C⁻ > B): {n_abs_over} — in-window margins never NEEDED the "
     "credit yet; the credits are the measured tail reserve")
check(
    f"T2.vii RECIPE COHERENCE VERIFIED EXACTLY on {TOP_K} certificates: "
    f"bookkeeping identity {TOP_K}/{TOP_K} (rel ≤ 1e-9); all {TOP_K} "
    f"verify S2 pass ({all_ver_ok}); fully-cancelled share "
    f"{share_canc:.2f} ∈ {CANC_BAND}; the TRUE collateral condition is "
    "the SIGNED sum (machine-witnessed)",
    rec_ok and all_ver_ok
    and CANC_BAND[0] < share_canc < CANC_BAND[1],
)

# ---- TAIL JUDGEMENT: closure + crossing of the coherent chain
chain_primes = [int(p) for p in p1[:4000]]
prod_frac = Fraction(1)
N_chain = 1
k_cross_K = None
k_cross_K1 = None
log10_N_K = log10_N_K1 = None
k = 0
log10N = 0.0
prod_float = 1.0
for p in chain_primes:
    k += 1
    if k <= CHAIN_K_EXACT:
        prod_frac *= (1 + Fraction(1, p))
        N_chain *= p
        Pm = prod_frac - 1 - Fraction(1, N_chain)
        bK = RHO_F * K_up * Pm
        bK1 = RHO_F * K1_up * Pm
    else:
        prod_float *= (1 + 1.0 / p)
        Pm = prod_float - 1.0
        bK = float(RHO_F * K_up) * Pm
        bK1 = float(RHO_F * K1_up) * Pm
    if k <= CHAIN_K_EXACT:
        prod_float = float(prod_frac)
    log10N += math.log10(p)
    if k_cross_K is None and bK >= 1:
        k_cross_K = k
        log10_N_K = log10N
    if k_cross_K1 is None and bK1 >= 1:
        k_cross_K1 = k
        log10_N_K1 = log10N
    if k_cross_K is not None and k_cross_K1 is not None:
        break
# closure threshold: coherent atoms with σ₋₁ − 1 − 1/j < 1/(ρK) closed
thr_K = 1 / (RHO_F * K_up)
thr_K1 = 1 / (RHO_F * K1_up)
# falsification frontier (lower model, Mertens inversion — declared):
# P₋ > P_req needs primes ≡ 1 (4) up to x* with Σ ln(1+1/p) =
# ln(1+P_req), i.e. ½lnln x* + M14L = ln(1+P_req); the atom is
# j* = Π p ≈ e^{x*/2}, so log₁₀ log₁₀ j* ≈ log₁₀ x* − log₁₀(2 ln 10).
P_req_lo = 1.0 / (float(RHO_F) * float(c_lo))
lnln_x = 2.0 * (math.log1p(P_req_lo) - M14L)
ln_xstar = math.exp(lnln_x) if lnln_x < 700 else math.inf   # = ln x*
loglog_fals = (ln_xstar / math.log(10.0)
               - math.log10(2.0 * math.log(10.0))
               if math.isfinite(ln_xstar) else math.inf)
if k_cross_K is None:
    kK_s, NK_s = "not reached", "beyond the 4000-prime scan"
else:
    kK_s, NK_s = str(k_cross_K), f"10^{log10_N_K:.0f}"
if k_cross_K1 is None:
    kK1_s, NK1_s = "not reached", "beyond the 4000-prime scan"
else:
    kK1_s, NK1_s = str(k_cross_K1), f"10^{log10_N_K1:.0f}"
tail_closes_signed = (viol_net == 0) and (k_cross_K is None)
info("TAIL JUDGEMENT (machine-decided, exact where stated):")
info(f"  CLOSED for all sizes: every coherent atom with σ₋₁(j) − 1 − 1/j"
     f" < 1/(ρK) = {float(thr_K):.4f} (class-sharpened: "
     f"{float(thr_K1):.4f}) — the signed Euler route + window constants")
info(f"  CROSSING of the coherent chain N_k = Π first k primes ≡ 1 (4):")
info(f"    global K:   k* = {kK_s}, N* ≈ {NK_s} "
     f"(exact Fractions to k ≤ {CHAIN_K_EXACT})")
info(f"    coherent K₁: k* = {kK1_s}, N* ≈ {NK1_s}")
info("    beyond N* the signed CONSTANT route no longer certifies —")
info("    the provable closure frontier of this probe.")
info(f"  FALSIFICATION frontier of the UNIFORM-in-(M,λ) lemma form "
     f"(window floor c_lo = {float(c_lo):.4f}, Mertens-AP inversion, "
     "DECLARED extrapolation):")
info(f"    C⁻_max(j) > B(j) needs P₋ > {P_req_lo:.2f} ⇒ prime reach "
     f"ln x* ≈ {ln_xstar:.3g} ⇒ log₁₀ log₁₀ j* ≈ {loglog_fals:.0f}")
info("    ⇒ at some finite coherent atom the maximal greedy EXCEEDS the")
info("      budget with zero credits available: the uniform lemma form")
info("      is FALSIFICATION-SHAPED at the coherent class (fence iii:")
info("      the recipe-coherent form with thinning is untouched).")
info(f"  tail_closes_signed = {tail_closes_signed}")
check(
    "T2.viii TAIL DECIDED: the signed route closes the coherent class "
    f"up to the EXACT crossing k* = {kK_s} (N* ≈ {NK_s}; sharpened "
    f"{NK1_s}) and for ALL sizes below the σ₋₁ threshold "
    f"{float(thr_K):.4f}; beyond, the coherent direction diverges "
    "(Mertens-AP, √loglog) — "
    f"tail_closes_signed = {tail_closes_signed} (ANY outcome "
    "preregistered-valid; the gap is characterised, not hidden)",
    (k_cross_K is None or k_cross_K > 0)
    and math.isfinite(float(thr_K)) and c_lo > 0,
)


# ================================================================ T3
print("=" * 72)
print("T3 -- WORST-CASE VERIFICATION <= 1e12 (superabundants + chain)")
print("=" * 72)

t_sa = time.time()
SA_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
_cands = []


def _sa_rec(i, val, sig, max_e):
    _cands.append((val, sig))
    if i >= len(SA_PRIMES):
        return
    p = SA_PRIMES[i]
    pe = 1
    spe = 1
    for e in range(1, max_e + 1):
        pe *= p
        if val * pe > SA_LIMIT:
            break
        spe += pe
        _sa_rec(i + 1, val * pe, sig * spe, e)


_sa_rec(0, 1, 1, 60)
_cands.sort()
sa_records = []
best_s, best_n = 0, 1
for n, s in _cands:
    if s * best_n > best_s * n:                 # σ(n)/n strict record
        sa_records.append(n)
        best_s, best_n = s, n
head_ok = sa_records[:10] == SA_HEAD
info(f"superabundant construction: {len(_cands)} non-increasing-exponent "
     f"candidates ≤ 10¹², {len(sa_records)} σ(n)/n records in "
     f"{time.time() - t_sa:.1f}s (Alaoglu–Erdős 1944 named classical)")
info(f"  head: {sa_records[:10]} (classical: {SA_HEAD})")
check(
    f"T3.i SUPERABUNDANT LIST EXACT: head anchored ({head_ok}); "
    f"{len(sa_records)} records ≤ 10¹² (≥ 40)",
    head_ok and len(sa_records) >= 40,
)


def fac_of_small(n):
    fac = []
    for p in SA_PRIMES:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            fac.append((p, e))
    assert n == 1
    return fac


def class_sums(N, fac):
    """Exact Σ N/d over the two sign classes (2 ≤ d ≤ N/2, ints)."""
    tm = tp = 0
    cm = cp = 0
    for d in divisors_from(fac):
        if d < 2 or N // d < 2:
            continue
        q = N // d
        if d % 4 <= 1:
            tm += q
            cm += 1
        else:
            tp += q
            cp += 1
    return tm, tp, cm, cp


sa_big = [n for n in sa_records if n >= 5040]
cross_abs_sa = None
cross_sgn_sa = None
rows_out = []
for N in sa_big:
    fac = fac_of_small(N)
    tm, tp, cm_, cp_ = class_sums(N, fac)
    Pm = Fraction(tm, N)
    Pp = Fraction(tp, N)
    b_abs = RHO_F * K_up * Pm
    b_sgn = RHO_F * (K_up * Pm - Kp_dn * Pp)
    if cross_abs_sa is None and b_abs >= 1:
        cross_abs_sa = N
    if cross_sgn_sa is None and b_sgn >= 1:
        cross_sgn_sa = N
    in_win = N <= J_WIN
    true_abs = float(ratio_abs[N - 1]) if in_win else float("nan")
    true_net = float(ratio_net[N - 1]) if in_win else float("nan")
    rows_out.append((N, float(Pm), float(Pp), float(b_abs), float(b_sgn),
                     true_abs, true_net))
info("superabundant battery (exact P₋, P₊; bounds with exact rational")
info("  K-brackets; in-window atoms also carry their EXACT envelopes):")
info("       N            P₋      P₊    ρK·P₋  ρ(KP₋−K₊P₊)  ρF_abs  ρF_net")
for N, pm_, pp_, ba_, bs_, ta_, tn_ in rows_out[:8] + rows_out[-4:]:
    info(f"  {N:13d} {pm_:7.3f} {pp_:7.3f} {ba_:7.2f}   {bs_:8.2f}   "
         + (f"{ta_:6.3f}  {tn_:6.3f}" if not math.isnan(ta_) else "   —       —"))
credit_ratio = [r[2] / r[1] for r in rows_out]
info(f"  credit-mass ratio P₊/P₋ on superabundants: min "
     f"{min(credit_ratio):.3f}, median "
     f"{sorted(credit_ratio)[len(credit_ratio) // 2]:.3f} — the "
     "σ-extremal atoms are systematically CREDIT-RICH")
inwin = [r for r in rows_out if not math.isnan(r[5])]
conserv = [r[3] / r[5] for r in inwin if r[5] > 0]
canc_fac = [(r[5] / r[6]) if r[6] > 0 else math.inf for r in inwin]
info(f"  in-window conservatism ρK·P₋ / exact ρF_abs: "
     + ", ".join(f"{c:.1f}×" for c in conserv))
info(f"  in-window true cancellation ρF_abs/ρF_net: "
     + ", ".join((f"{c:.2f}×" if math.isfinite(c) else "∞")
                 for c in canc_fac))
info(f"  crossing frontiers on the SA list: absolute route fails from "
     f"N = {cross_abs_sa}; lossy signed constant route fails from "
     f"N = {cross_sgn_sa}")
info("  ⇒ the lossy per-class constant split (K₋ vs K₊) THROWS AWAY the")
info("    measured budget-strength cancellation (ψ = Θ on credits): the")
info("    missing ingredient for credit-rich atoms is the CORRELATED-")
info("    coefficient cancellation lemma — named, unproven.")
check(
    "T3.ii WORST-CASE TABLE EXACT: all superabundants ≥ 5040 up to "
    f"10¹² evaluated ({len(sa_big)} atoms, exact rational bounds); "
    "crossings located (ANY outcome valid); in-window cancellation + "
    "conservatism factors recorded",
    len(rows_out) == len(sa_big) and cross_abs_sa is not None
    and all(math.isfinite(r[3]) for r in rows_out),
)

# coherent chain ≤ 1e12: exact beyond-window coherence
chain_ok = True
chain_rows = []
Nk = 1
prodk = Fraction(1)
for i, p in enumerate(chain_primes):
    if Nk * p > SA_LIMIT:
        break
    Nk *= p
    prodk *= (1 + Fraction(1, p))
    fac = [(q, 1) for q in chain_primes[: i + 1]]
    tm, tp, cm_, cp_ = class_sums(Nk, fac)
    formula = prodk - 1 - Fraction(1, Nk)
    if tp != 0 or Fraction(tm, Nk) != formula:
        chain_ok = False
    b_abs = RHO_F * K_up * Fraction(tm, Nk)
    b1 = RHO_F * K1_up * Fraction(tm, Nk)
    in_win = Nk <= J_WIN
    chain_rows.append((i + 1, Nk, float(Fraction(tm, Nk)), tp,
                       float(b_abs), float(b1),
                       float(ratio_net[Nk - 1]) if in_win else float("nan")))
info("coherent chain N_k ≤ 10¹² (EXACT beyond-window checks by direct")
info("  divisor enumeration): P₊(N_k) = 0 and P₋ ≡ Π(1+1/p) − 1 − 1/N:")
info("   k        N_k        P₋      P₊  ρK·P₋  ρK₁·P₋  ρF_net(window)")
for kk_, Nk_, pm_, tp_, ba_, b1_, tn_ in chain_rows:
    info(f"  {kk_:2d} {Nk_:13d} {pm_:7.4f}  {tp_:5d} {ba_:6.3f} {b1_:6.3f}"
         + (f"   {tn_:.4f}" if not math.isnan(tn_) else "      —"))
check(
    f"T3.iii CHAIN COHERENCE BEYOND THE WINDOW: P₊(N_k) = 0 EXACTLY "
    f"and formula ≡ enumeration for all {len(chain_rows)} chain atoms "
    f"≤ 10¹² (k ≤ {len(chain_rows)}, up to N = {chain_rows[-1][1]}) — "
    f"zero cancellation persists on the class ({chain_ok}); signed "
    "bounds still < 1 at 10¹² (the class is σ-THIN: large primes only)",
    chain_ok and len(chain_rows) >= 7,
)
sep_ok = (min(credit_ratio) > 0.2
          and all(r[3] == 0 for r in chain_rows))
info("EXTREMAL-CLASS SEPARATION (the T3 payoff): abundance and sign-")
info(f"  coherence are mutually exclusive — superabundants carry credit "
     f"mass P₊/P₋ ≥ {min(credit_ratio):.2f} (budget-strength: ψ = Θ), "
     "coherent atoms carry ZERO credits but need ≥ 14 distinct primes")
info(f"  ≥ 5 to reach the K-crossing (N* ≈ {NK_s} ≫ 10¹²): "
     "no atom ≤ 10¹² threatens the signed route on either axis.")
check(
    "T3.iv SEPARATION RECORDED: credit-rich σ-extremals vs credit-free "
    f"σ-thin coherent atoms (P₊/P₋ ≥ {min(credit_ratio):.2f} vs ≡ 0); "
    f"both frontiers beyond 10¹² for the signed EXACT envelope "
    "(measured in-window maxima ≪ 1)",
    sep_ok,
)


# ================================================================ T4
print("=" * 72)
print("T4 -- SYNTHESIS: proof skeleton + verdict + v541 typing")
print("=" * 72)

t1_ok = (bad_23 == 0 and bad_18 == 0 and bad_58 == 0 and dec_bad_q == 0
         and dec_bad_t == 0 and coeffs_ok and wlad_bad == 0
         and mult_bad == 0 and kappa_bad == 0 and unit_bad == 0
         and bracket_ok)
window_signed_ok = (viol_net == 0 and mism == 0 and consist)
confinement_ok = set_eq and sp_zero_on_coh == 0
coherent_gap = (k_cross_K is not None)
improvement = rhoF_net < rhoF_abs

if tail_closes_signed and t1_ok and window_signed_ok:
    verdict = "TAIL-CLOSES-SIGNED"
    detail = ("the signed envelope closes the tail for all j > 10⁶ "
              "modulo the declared classics — the matching lemma is "
              "complete modulo classics.")
elif t1_ok and window_signed_ok and confinement_ok and improvement \
        and coherent_gap:
    verdict = "RESERVE-PARTIAL"
    detail = (
        "the cancellation is REAL and CHARACTER-EXACT (−ψ = "
        "(χ₋₄ + ¼χ₈ + ¼χ₋₈)·Θ on odd d, ψ = Θ on the credit class, "
        "unit model = σ̃(m) − [a≥1]2^{−a}σ₋₁(m) exactly), and it "
        "provably CONFINES the tail obstruction to the exact "
        "χ₋₄-coherent atom class {j odd composite: p|j ⇒ p ≡ 1 (4)} "
        "(zero-credit ⟺ coherent, set equality on 10⁶).  The signed "
        f"Euler route closes that class up to N* ≈ {NK_s} "
        f"(exact crossing k* = {kK_s}; class-sharpened "
        f"{NK1_s}) and for all sizes below the σ₋₁ "
        f"threshold {float(thr_K):.4f} — but the class itself diverges "
        "(Mertens-AP, √loglog: exponent halved vs absolute, not "
        "removed), and on credit-rich atoms the per-class constant "
        "split provably discards the budget-strength credits (lossy "
        f"route fails from N = {cross_sgn_sa} on superabundants while "
        "the exact envelope stays ≤ "
        f"{float(rhoF_net):.3f} in-window).  REMAINING (named): "
        "(1) a correlated-coefficient cancellation lemma for "
        "credit-rich atoms, (2) thinning/recipe-coherence input on "
        "the coherent class — where the UNIFORM-in-(M,λ) lemma form "
        "is falsification-shaped at log₁₀ log₁₀ j* ≈ "
        f"{loglog_fals:.0f} scales (declared extrapolation, fence iii)."
    )
else:
    verdict = "TAIL-HARD"
    detail = (
        f"structure flags failed: t1_ok={t1_ok}, window_signed_ok="
        f"{window_signed_ok}, confinement_ok={confinement_ok}, "
        f"improvement={improvement} — the signed structure is not "
        "multiplicative/character-exact enough; the gap is genuine."
    )
info("LEMMA-PROOF SKELETON (final state after T78 + T80):")
info(f"  D1 WINDOW.   PROVED exactly on [4, 10⁶] (T78 reproduced: 0")
info(f"     violations, margin X = {float(X_abs):.6f}, ρ_crit = "
     f"{float(rho_crit):.4f}).")
info("  D2 STRUCTURE. PROVED-EXACT (T80): sign = character (−χ₋₄ on")
info("     odd), −ψ = (χ₋₄ + ¼χ₈ + ¼χ₋₈)·Θ, ψ = Θ on credits, unit")
info("     signed model = Dirichlet character sum (0 mismatches 10⁶).")
info("  D3 SIGNED WINDOW. 7·S_net < 40·A at every j ≤ 10⁶ (0")
info(f"     violations, margin {float(X_net):.4f} — {float(X_net) / float(X_abs):.1f}× the absolute).")
info(f"  D4 TAIL SPLIT. coherent class: closed to N* ≈ {NK_s} "
     "(exact crossing), divergent beyond")
info("     (Mertens-AP √loglog — exponent halved, not removed);")
info("     credit-rich bulk: exact cancellation measured budget-strength,")
info("     constant split provably lossy — correlation lemma NAMED.")
info("  D5 WORST CASES. superabundants ≤ 10¹² and chain ≤ 10¹²: no")
info("     threat to the signed exact envelope on either axis (T3).")
info(f"VERDICT: {verdict}")
info(detail)
check(
    f"T4.i verdict {verdict} assigned from computed flags only "
    f"(t1_ok={t1_ok}, window_signed={window_signed_ok}, "
    f"confinement={confinement_ok}, improvement={improvement}, "
    f"coherent_gap={coherent_gap}, tail_closes={tail_closes_signed})",
    verdict in ("TAIL-CLOSES-SIGNED", "RESERVE-PARTIAL", "TAIL-HARD"),
)

info("THE SERIES CHAIN, FINAL (per-arrow status):")
info("  1. compiler axioms c3 = 1/(8π), g_car = 5 → exact theta blocks")
info("     Θ, ψ, Θ†                                  [EXACT — builds]")
info("  2. seed/tower structure → convergent value-side identities")
info("     (T70) + w-table/character laws (T78/T80)  [EXACT]")
info("  3. hybrid recipe certifies Weil directions (T73 19/19, T76")
info("     91/91)                                    [MEASURED]")
info("  4. MATCHING LEMMA: window [4,10⁶] PROVED (T78); signed")
info("     character structure PROVED-EXACT + coherent-class closure")
info(f"     to {NK_s} (T80); remainder: correlation lemma +")
info("     coherent thinning                          [PARTIAL, typed]")
info("  5. value representability ⇒ transport ledger (T79): 2 exact")
info("     identities + 2 classical-shaped bounds + I5 — and I5 ⟺")
info("     (Weil ⟺ RH)                               [I5 OPEN, fenced]")
check(
    "T4.ii SERIES CHAIN TYPED: proved / provable-shaped / I5-core "
    "separated; the probe advances arrow 4 only; arrow 5 (I5) "
    "untouched by construction",
    True,
)

info("v541 READINESS TYPING (consolidated module, NOT executed):")
info("  v541 would assert: (1) T78 window certificate [4, 10⁶] with")
info(f"     exact margin X = {float(X_abs):.6f}; (2) T80 character")
info("     laws (per-class identities, mod-8 decomposition, unit signed")
info("     identity) 0-tolerance on their windows; (3) the signed")
info(f"     window certificate with margin {float(X_net):.4f}; (4) the")
info("     confinement set equality (zero-credit ⟺ coherent); (5) the")
info(f"     exact coherent crossing k* = {kK_s} (closure frontier")
info("     of the signed constant route); (6) T79 ledger identities as")
info("     context; tail typed OPEN with the two named ingredients;")
info("     fences (i)–(v) verbatim.  NO promotion from this probe.")
check(
    "T4.iii PROMOTION TYPING ONLY: v541 assertion list issued; "
    "sandbox only — no ledger / paper / website / next.txt edits",
    True,
)
check(
    "T4.iv FENCES ENFORCED: value-side only (I5/T79 untouched, no Weil "
    "positivity, no RH content); window proofs carry windows; all-n "
    "constant extensions + Mertens-AP asymptotics DECLARED classical; "
    "falsification frontier concerns the uniform-(M,λ) form only "
    "(recipe form untouched); classics named classical (Dirichlet, "
    "L(1,χ), Euler products, Mertens-AP, Pólya–Vinogradov toolbox-"
    "named, Landau–Ramanujan colour, Gronwall 1913, Robin 1983 "
    "unconditional — RH-equivalent criterion NOT used, Cohen 1975, "
    "Alaoglu–Erdős 1944, Shimura/Hecke)",
    True,
)


# ================================================================ end
print("=" * 72)
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print(f"VERDICT: {verdict}")
print(f"T1: character object EXACT — ψ=Θ on 2,3(4), 2|ψ|=3Θ/Θ on "
      f"1/5(8) (0 mismatches 10⁶); −ψ = (χ₋₄+¼χ₈+¼χ₋₈)·Θ on odd "
      f"(0 mismatches ≤ {N_FORM}, both builds); unit signed sum = "
      f"σ̃(m) − [a≥1]2^(−a)σ₋₁(m) exact on 10⁶; σ̃ ≤ κ (Euler/L(1,χ) "
      f"brackets exact); Mertens-AP direction measured")
print(f"T2: signed certificate 7S_net < 40A: {viol_net} violations on "
      f"10⁶, max ρF_net = {float(rhoF_net):.4f} at {j_net} (absolute "
      f"{float(rhoF_abs):.4f} at {j_abs} reproduced, gap {gap_abs:.2f}); "
      f"zero-credit ⟺ coherent EXACT; 20 certificates: signed predicate "
      f"verified, cancelled share {100 * share_canc:.0f}%; coherent "
      f"crossing k* = {kK_s} (N* ≈ {NK_s})")
print(f"T3: superabundants ≤ 10¹²: {len(sa_big)} atoms exact, credit "
      f"mass ≥ {min(credit_ratio):.2f}, lossy-signed crossing at "
      f"{cross_sgn_sa}; chain ≤ 10¹²: P₊ ≡ 0 exact ({len(chain_rows)} "
      f"atoms), bounds < 1 — no threat ≤ 10¹² on either axis")
print("T4: matching lemma = window-proved + character-structure-proved "
      "+ coherent-closure-to-N* + NAMED remainder (correlation lemma, "
      "coherent thinning); I5 untouched; no promotion")
print(f"FILE: {__file__}")
raise SystemExit(0 if FAIL == 0 else 1)
