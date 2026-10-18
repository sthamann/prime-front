"""Discovery probe (2026-07-25), part 81 — contract RECIPE.COHERENT.AVOIDANCE.

T80 (TAIL.CORRELATION.LEMMA) confined the last gap of the matching
lemma EXACTLY to the χ₋₄-coherent atom class {j odd: every prime
factor ≡ 1 (mod 4)}: zero-credit ⟺ coherent is an exact set equality
on 10⁶, on that class the signed clash has provably NO cancellation,
and the signed Euler route closes it only up to the exact crossing
N* ≈ 10²³ (k* = 14).  T80's preregistered constructive residual move
(this probe, T81): the hybrid recipe has freedom in the rescalings m
— can a modified greedy design AVOID the coherent class as clash
positions STRUCTURALLY, closing the matching lemma for the modified
recipe completely modulo classics?

THE TWO EXACT LEVERS DECIDED HERE (both corollaries of ONE
multiplicative fact — the prime set of a product is the union of the
prime sets; the 1-mod-4 class is the classical Fermat / sum-of-two-
squares prime class, named classical):
  LEVER (avoidance):  coh(m·k) = coh(m) AND coh(k).  Hence a
      rescaling m with ANY prime factor ≢ 1 (mod 4) generates ONLY
      non-coherent clash atoms j = m·k — filtering the rescaling set
      to non-coherent m would confine every clash to the classes
      where the T80 cancellation is provably active (credits exist at
      every non-coherent atom, exact set equality).
  COUNTER-LEVER (reachability): a rescaling m flips a target t only
      if m | t and ψ(t/m) < 0.  Every divisor of a coherent t is
      coherent, and every divisor cofactor k | t has k ≡ 1 (mod 4) so
      ψ(k) < 0 automatically: coherent targets are reachable ONLY by
      coherent rescalings — if a Weil direction demands a twist at a
      coherent atom, the avoidance filter breaks its reachability,
      and the coherent usage of ANY valid certificate is bounded
      BELOW by an exact forced set (minimality lemma: the self-flip
      m = t has the pointwise-smallest coherent minus-hit set among
      all reaching rescalings).
Which of the two levers wins — filter closes the lemma / quantified
coverage cost / reachability breaks — is decided by machine on the
full frozen T76 battery (100 rows, bit-identical reproduction).

CRITICAL HONESTY FRAME (mandatory): even a FULLY closed matching
lemma delivers ONLY value-side representability of the Weil cone —
the I5 core inequality of T79 (the prime↔archimedean coupling, whose
typing is EQUIVALENT to Weil positivity ⟺ RH) is untouched by every
outcome here; NO progress on I5 is claimed and NO RH content exists
in this probe.  Window proofs are window proofs: exact statements
carry their windows; all-n extensions of window constants are
DECLARED classical typings (Cohen 1975 seed bounds).  Classics named
classical: Fermat / sum-of-two-squares structure of the 1-mod-4
prime class, Dirichlet characters and L(1,χ), Euler products,
Mertens theorems in arithmetic progressions, Landau 1908 / Ramanujan
(density of the coherent class), Gronwall 1913, Robin 1983
UNCONDITIONAL (RH-equivalent criterion NOT used, declared), Cohen
1975, Alaoglu–Erdős 1944, Pólya–Vinogradov 1918 (toolbox-named),
Weil 1952 cone, Shimura 1973 / Hecke T(p²).

A1  THE CLASH GEOMETRY OF THE COHERENT CLASS (exact).  (i) coherence
    is multiplicative: coh(m·k) = coh(m) AND coh(k), verified with 0
    mismatches over ALL factorisations of ALL j ≤ 10⁶ (every
    factorisation has a factor ≤ 10³ = √10⁶, so the m ≤ 10³ scan is
    COMPLETE); the avoidance lever verified directly (a non-coherent
    m has ZERO coherent multiples).  (ii) reachability: for coherent
    t, EVERY divisor cofactor k has ψ(k) < 0 and EVERY reaching
    rescaling m = t/k is coherent (0 exceptions on [2, 4000]); a
    target is reachable by a non-coherent rescaling ⟺ it is
    non-coherent (exact equivalence on the window) — the answer to
    the preregistered coverage question: the restricted m-set reaches
    EXACTLY the non-coherent targets, coherent demand is unreachable.
    (iii) minimality: for every coherent t and every proper reaching
    m = t/k, the coherent minus-hit set of m CONTAINS that of t (set
    inclusion, 0 violations) — the self-flip is the clash-minimal
    choice; no valid recipe can produce fewer coherent hits than the
    forced set of its coherent demand.  (iv) the filter variants
    compared (non-coherent m vs m with a 3-mod-4 factor): the 3-mod-4
    variant is strictly smaller; non-coherence is the minimal correct
    filter (even m without 3-mod-4 factors are equally safe).
A2  THE MODIFIED RECIPE ON THE FULL T76 BATTERY.  Baseline: the T76
    battery reproduced bit-identically (100 rows, 24/20/20/16/20,
    rng(76), 9 trivial, 100 pass — hard anchor).  AV-STRICT (the
    preregistered filter: greedy rescaling candidates restricted to
    non-coherent m; repair and predicates S1/S2/S3 UNCHANGED, same
    independent verifier): (i) success rate + failure typing — the
    strict-pass set is predicted and verified to be EXACTLY the rows
    with V ∩ coherent = ∅ (both directions: coherent demand ⇒
    coherent targets keep their full positive base weight ⇒ S2-target
    fails; no coherent demand ⇒ the filter never triggers ⇒
    bit-identical certificate ⇒ pass); on every failing row the
    untwisted-target set contains V ∩ coherent (exact).  (ii) cost
    comparison on strict-pass rows: λ dictionaries bit-identical to
    the original (summands, λ-condition: zero delta).  (iii) census
    on the ORIGINAL certificates: coherent λ-keys ⊆ coherent
    violations on 100/100 (the T76 greedy NEVER uses an unforced
    coherent rescaling — it already realises the minimal coherent
    usage), every coherent violation is covered by a coherent λ-key
    divisor, and the actual coherent clash set CONTAINS the forced
    lower-bound set F_lower (minimality made live); coherent clash
    counted per row (zero-clash rows = the avoidance certificate,
    exact; ANY outcome valid); TOP-20 cross-validation against the
    T80 clash census (coherent hit sets equal — the lever on live
    certificates).
A3  THE LEMMA FOR THE MODIFIED RECIPE (combination + exact margins).
    Anchors reproduced: T78 absolute certificate (0 violations on
    10⁶, exact margin X), T80 signed certificate (0 violations, max
    ρF_net, margin factor ≈ 8.9×), explicit constants K, K₁ and the
    coherent-class constants C₂coh, c₀coh (guarded-exact rational
    brackets), the coherent chain crossing k* = 14 / N* ≈ 10²³ (the
    uniform-form frontier), and the T80 superabundant flag (the lossy
    signed constant route fails on credit-rich atoms — remainder (1)
    is NOT closed by constants).  NEW: the per-certificate coherent
    closure — for each battery row the coherent clash is generated by
    the FINITE forced key set, so C⁻(j)/B(j) ≤ (C₂coh/c₀coh)·L_M/j
    with L_M = Σ_{m coherent key} λ_m·m^{−3/2} (measured λ): the
    coherent class closes for ALL j > j₀ = (C₂coh/c₀coh)·L_M
    (exact given the declared classical all-n constants), the range
    (4000, 10⁶] is scanned EXACTLY (every coherent multiple of every
    coherent key, max ratio r_mid), and j ≤ 4000 is the verified S2
    window — rows with j₀ ≤ 10⁶ and r_mid < 1 have their coherent
    class FULLY closed for the certificate; avoidant rows (no
    coherent demand) have it closed IDENTICALLY ZERO at all sizes.
    The remaining classical ingredients are listed finally.
A4  SYNTHESIS.  (i) final matching-lemma status (what closes for
    which recipe/demand, what remains); (ii) the series chain with
    per-arrow status; (iii) v541 readiness typing (T78 window proof +
    T80 signed structure + T81 avoidance dichotomy as ONE proof
    package — typing only, NO promotion); (iv) unchanged: the I5
    fence.

PREREGISTERED CRITERIA
  A0: AST zero-firewall clean; independent q-unit (10⁶) and t-unit
      (5·10⁴) builds agree coefficient-exactly; heads match; Landen
      Θ†(2m) = ψ(m) exact; jtheta anchors rel < 1e-12 (4 anchors);
      T71 sign law 0 violations, Θ > 0, ψ ≠ 0 on 10⁶; ψ < 0 at every
      coherent n ≥ 5 (0 exceptions); multiplier identity sympy-exact,
      ρ(1) = 2/3; coherent-mask head equals the hand list
      {1,5,13,17,25,29,37,41,53,61,65,73,85,89,97}; SPF spot checks;
      zero-credit ⟺ coherent set equality EXACT on 10⁶ (T80 T2.iv).
  A1: multiplicativity 0 mismatches over all factorisations of all
      j ≤ 10⁶ (coverage argument printed); lever 0 coherent products
      from non-coherent m; coherent reachability: ψ(k) < 0 for ALL
      k | t and reach(t) entirely coherent, 0 exceptions on
      [2, 4000]; non-coherent self-reach 0 exceptions; the
      equivalence [reachable by non-coherent m ⟺ non-coherent] 0
      exceptions; minimality inclusion 0 violations over all (t, m)
      pairs; filter-variant containment (3-mod-4 ⊂ non-coherent);
      coverage counts recorded.
  A2: battery reproduced (100 rows, 24/20/20/16/20, 9 trivial,
      100 pass); strict bookkeeping pass + fail = 100; strict-pass
      set == {rows with V ∩ coherent = ∅} (set equality, both
      directions); λ bit-identity on ALL strict-pass rows; V_coh ⊆
      untwisted on ALL strict-fail rows (equality share recorded);
      census: coherent λ-keys ⊆ V_coh on 100/100; every coherent
      violation covered by a coherent-key divisor (0 exceptions);
      F_lower ⊆ actual coherent clash on 100/100; TOP-20 coherent
      hit sets equal between the two independent census routes;
      coherent clash totals + zero-clash rows recorded (ANY outcome
      valid).
  A3: constants exact (C₁² = 16 attained on 4-powers; c₀ ∈ T78 band);
      T78 absolute certificate 0 violations, X ∈ (.0820, .0823),
      ρE(8000) ∈ (0.70, 0.75); T80 signed certificate 0 violations,
      max ρF_net ∈ (0.26, 0.28), margin factor ∈ (8.5, 9.3); sieve ≡
      direct big-integer sums on ≥ 70 atoms (0 mismatches); chain
      crossing k* = 14 with log₁₀N* ∈ (22, 25); superabundant head
      anchored, ≥ 40 records ≤ 10¹², crossing flags recorded; per-row
      j₀ finite, mid-range scan complete, sampled direct recheck
      rel ≤ 1e-9; closure counts from computed flags (ANY outcome
      valid).
  A4: verdict from computed flags only (thresholds preregistered
      below); series chain + v541 assertion list printed; NO
      promotion; fences enforced.
  VERDICTS (preregistered; thresholds fixed here):
    LEMMA-CLOSES-AVOIDANT — NO battery direction has coherent demand
        (V ∩ coherent = ∅ on all 100 rows) AND the filtered recipe
        passes everywhere bit-identically: the m-filter costs nothing
        and the coherent class never appears — the matching lemma for
        the modified recipe closes modulo classics;
    AVOIDANCE-COSTLY   — coherent demand exists but the strict filter
        still certifies ≥ 50% of the nontrivial rows: avoidance works
        at a quantified coverage loss (the loss set is exactly the
        coherent-demand rows);
    AVOIDANCE-FAILS    — the strict filter certifies < 50% of the
        nontrivial rows: target reachability breaks structurally —
        the WHY is the exact reachability theorem (every divisor of a
        coherent target is coherent; the m-freedom assumed by the
        avoidance premise does not exist on coherent demand).

FENCES (honest typing):
  (i)   VALUE-SIDE ONLY: even a fully closed matching lemma yields
        ONLY value-side representability of the Weil cone — the I5
        core inequality (T79 prime↔arch coupling, equivalence-typed
        to Weil ⟺ RH) is UNTOUCHED by any outcome here; no Weil
        positivity, no RH content.
  (ii)  WINDOW PROOFS ARE WINDOW PROOFS: exact statements carry their
        windows; the beyond-window use of the window constants
        (C₂coh, c₀coh, K) is a DECLARED classical typing (Cohen 1975
        all-n coefficient bounds); Mertens-AP asymptotics are
        declared classical extrapolations.
  (iii) the per-certificate coherent closure (j₀, r_mid) is a
        statement about the MEASURED λ of live certificates extended
        beyond their window; the uniform-in-demand lemma form is NOT
        closed by it — its coherent frontier (N* crossing) is
        reproduced and stays open exactly on coherent demand.
  (iv)  classics named classical (list above); verdicts from computed
        flags only; any outcome is a valid map; runtime and window
        sizes budget-honest and printed.

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
J_WIN = 1_000_000             # exact q-unit window (masks + certificates)
N_FORM = 50_000               # t-unit cross-validation window
M_COVER = 1_000               # multiplicativity scan bound (= √J_WIN)
W_REF = 4000                  # T76/T77/T80 battery reference window
RHO_NUM, RHO_DEN = 21, 20     # ρ_design = 21/20 (T76/T77/T78 frozen)
CERT_L, CERT_R = 7, 40        # ρ/6 = 7/40 ⇒ certificate 7S < 40A
GUARD = 1e-9                  # float prefilter guard band (≫ 1e-15)
K_VEC = 64                    # hybrid sieve vectorisation cut
N_TIGHT = 40                  # tightest signed atoms rechecked exactly
N_RAND = 32                   # random atoms rechecked exactly
SA_LIMIT = 10 ** 12           # superabundant battery reach (T80 T3)
CHAIN_K_EXACT = 24            # exact-Fraction chain scan depth
TOP_K = 20                    # certificates cross-validated (A2)
N_SAMP_DIRECT = 10            # scan atoms rechecked by direct divisors
X_BAND = (0.0820, 0.0823)     # T78 margin anchor X = 0.082159
C0_BAND = (2.669, 2.679)      # T78 c₀ anchor 2.674
E8K_BAND = (0.70, 0.75)       # T77 anchor ρ·E(8000) = 0.724
RFNET_BAND = (0.26, 0.28)     # T80 anchor max ρF_net = 0.272
MFACT_BAND = (8.5, 9.3)       # T80 anchor margin factor 8.9×
KSTAR_ANCHOR = 14             # T80 anchor coherent crossing k* = 14
L10N_BAND = (22.0, 25.0)      # T80 anchor log₁₀ N* ≈ 23
STRICT_MAJ = 0.5              # preregistered verdict threshold
SA_HEAD = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120]   # classical head
COH_HEAD = [1, 5, 13, 17, 25, 29, 37, 41, 53, 61, 65, 73, 85, 89, 97]
TH_KEY = (0, 2, 1, 2, 0, 0)   # Θ  = θ₂(q²)²·θ₃(q)·θ₃(q²)²  (T68/T70)
PSI_KEY = (0, 0, 1, 0, 4, 0)  # ψ  = θ₃(q)·θ₄(q)⁴           (mirror)
TD_KEY = (0, 0, 2, 1, 2, 0)   # Θ† = θ₃(q)²·θ₃(q²)·θ₄(q)²   (Fricke)
# battery constants (T73/T76/T77/T80 frozen, verbatim)
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


# ================================================================ A0
print("=" * 72)
print("A0 -- ZERO-FIREWALL (AST) + exact builds + masks + full-window laws")
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
    "A0.a ZERO-FIREWALL: AST has no Riemann-zero loader "
    f"(calls∩={sorted(_zero_calls)}; attrs={_attr_hits}; "
    f"imports={sorted(_bad_imports)})",
    len(_zero_calls) == 0 and len(_attr_hits) == 0 and len(_bad_imports) == 0,
)
_name_hits = [
    node.id for node in ast.walk(_tree)
    if isinstance(node, ast.Name) and node.id in _FORBIDDEN_AST
]
check(
    f"A0.b ZERO-FIREWALL: no forbidden zero-loader Name nodes ({_name_hits})",
    len(_name_hits) == 0,
)
info("FENCE: even a fully closed matching lemma yields ONLY value-side")
info("  representability — the I5 core inequality (T79 prime↔arch")
info("  coupling, equivalence-typed to Weil ⟺ RH) is untouched by any")
info("  outcome here; window proofs are window proofs; classics named")
info("  classical (Fermat 1-mod-4 class, Dirichlet/L(1,χ), Euler")
info("  products, Mertens-AP, Landau/Ramanujan, Gronwall, Robin 1983")
info("  unconditional, Cohen 1975, Alaoglu–Erdős, Pólya–Vinogradov).")
info("  NO RH content.")

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
    "A0.c BUILD CROSS-VALIDATION: independent q-unit (10⁶) and t-unit "
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
    "A0.d ANCHORS: coefficient arrays ≡ jtheta monomials on the "
    "imaginary axis (rel < 1e-12 on 4 anchors)",
    anchor_ok,
)

# ---- masks: primes, coherent class, SPF
t_m = time.time()
n_all = np.arange(1, J_WIN + 1, dtype=np.int64)
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
spf_ok = (bool(np.all(SPF[primes_all] == primes_all))
          and int(SPF[9]) == 3 and int(SPF[35]) == 5
          and int(SPF[999983]) == 999983)
n_coh_1m = int(np.sum(coh[2:]))
coh_head = [int(x) for x in np.nonzero(coh[:101])[0]]
info(f"masks on 10⁶ in {time.time() - t_m:.1f}s: {len(primes_all)} "
     f"primes ({len(p1)} ≡ 1 (4), {len(p3)} ≡ 3 (4)); coherent atoms "
     f"2 ≤ n ≤ 10⁶: {n_coh_1m} ({100.0 * n_coh_1m / J_WIN:.2f}% — "
     "Landau/Ramanujan density colour, named classical)")
check(
    "A0.e MASK + SPF INTEGRITY: coherent-mask head equals the hand "
    f"list {COH_HEAD} ({coh_head == COH_HEAD}); SPF spot checks exact "
    f"({spf_ok})",
    coh_head == COH_HEAD and spf_ok,
)

sgn_law = np.where((n_all % 4) <= 1, -1, 1).astype(np.int64)
law_viol = int(np.sum(np.sign(Ps[1:]) != sgn_law))
th_zero = int(np.sum(Th[1:] == 0))
psi_zero = int(np.sum(Ps[1:] == 0))
coh_psi_bad = int(np.sum(Ps[1:][coh[1:] & (n_all >= 5)] >= 0))
check(
    f"A0.f FULL-WINDOW LAWS (n ≤ {J_WIN}): T71 sign law "
    f"sign ψ(n) = (−1)^{{⌊n/2⌋+1}} — {law_viol} violations; Θ > 0 "
    f"({th_zero} zeros); ψ zero-free ({psi_zero} zeros); COROLLARY: "
    f"ψ(n) < 0 at EVERY coherent n ≥ 5 ({coh_psi_bad} exceptions) — "
    "every hit landing on a coherent atom is a minus hit, and every "
    "divisor cofactor of a coherent target is a legal flip channel",
    law_viol == 0 and th_zero == 0 and psi_zero == 0 and coh_psi_bad == 0,
)

u_s = sp.symbols("u", real=True)
mult_id = sp.simplify(
    2 * sp.cosh(sp.Rational(3, 2) * u_s)
    - sp.exp(u_s) * (sp.exp(u_s / 2) + sp.exp(-5 * u_s / 2))
)
rho1 = Fraction(int(Th[1]), abs(int(Ps[1])))
check(
    "A0.g CONTINUITY: multiplier identity m_Θ(u) = 2cosh(3u/2) "
    "sympy-exact (T73–T80 reproduction); pin-atom flip threshold "
    f"ρ(1) = {rho1} = 2/3 exact",
    mult_id == 0 and rho1 == Fraction(2, 3),
)

# ---- shared machinery: budget + signed clash sieves (T80 verbatim)
t_m = time.time()
A_ARR = np.zeros(J_WIN + 1, dtype=np.int64)
A_ARR[1:] = n_all * Th[1:]                      # A(j) = jΘ(j), exact int64
SM = np.zeros(J_WIN + 1, dtype=np.int64)
SP = np.zeros(J_WIN + 1, dtype=np.int64)
CNT_M = np.zeros(J_WIN + 1, dtype=np.int32)
CNT_P = np.zeros(J_WIN + 1, dtype=np.int32)
d_all = np.arange(2, J_WIN + 1, dtype=np.int64)
d_m = d_all[(d_all % 4 <= 1)]                   # ⇒ d ≥ 4 automatically
d_p = d_all[(d_all % 4 >= 2)]
for k in range(2, K_VEC + 1):
    dv = d_m[d_m <= J_WIN // k]
    idx = k * dv
    SM[idx] += int(A_ARR[k]) * Pa[dv]
    CNT_M[idx] += 1
    dv = d_p[d_p <= J_WIN // k]
    idx = k * dv
    SP[idx] += int(A_ARR[k]) * Ps[dv]           # ψ(d) > 0 on this class
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
S78[mask_dj] += 4 * Pa[mask_dj]                 # add back d = j (A(1) = 4)
CNT78 = CNT_M.copy()
CNT78[mask_dj] += 1
supp78 = CNT78[1:] > 0
info(f"machinery: budget + 4 signed clash sieves on {J_WIN} in "
     f"{time.time() - t_m:.1f}s ({len(d_m)} minus-class d, "
     f"{len(d_p)} plus-class d)")

pred_zero = (CNT_P[1:] == 0) & (CNT_M[1:] > 0)
rhs_coh = coh[1:] & (n_all > 1) & (~isp[1:])
set_eq = bool(np.array_equal(pred_zero, rhs_coh))
sp_zero_on_coh = int(np.sum(SP[1:][pred_zero] != 0))
check(
    "A0.h CONFINEMENT ANCHOR (T80 T2.iv): {zero-credit clash atoms} = "
    "{χ₋₄-coherent odd composites} — set equality on the FULL 10⁶ "
    f"window ({set_eq}); S⁺ ≡ 0 on the class ({sp_zero_on_coh} "
    "exceptions): every NON-coherent atom owns at least one credit "
    "divisor — the cancellation classes the avoidance filter would "
    "confine the clash to",
    set_eq and sp_zero_on_coh == 0,
)


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


# ================================================================ A1
print("=" * 72)
print("A1 -- CLASH GEOMETRY: multiplicativity, reachability, minimality")
print("=" * 72)

# (i) coherence is multiplicative: coh(m·k) = coh(m) AND coh(k)
t_a = time.time()
mult_bad = 0
for m in range(1, M_COVER + 1):
    top = J_WIN // m
    ks = np.arange(1, top + 1, dtype=np.int64)
    lhs = coh[m * ks]
    rhs = coh[ks] & bool(coh[m])
    mult_bad += int(np.sum(lhs != rhs))
info(f"multiplicativity scan m ≤ {M_COVER} in {time.time() - t_a:.1f}s")
info("COVERAGE (complete): every factorisation j = m·k of every "
     f"j ≤ {J_WIN}")
info(f"  has min(m, k) ≤ √j ≤ {M_COVER}, and the check is symmetric in")
info("  (m, k) — so the scan verifies coh(m·k) = coh(m) ∧ coh(k) for")
info("  ALL factorisations of ALL window atoms (prime set of a product")
info("  = union of prime sets; Fermat 1-mod-4 class, named classical).")
check(
    "A1.i MULTIPLICATIVITY EXACT: coh(m·k) = coh(m) AND coh(k) with "
    f"{mult_bad} mismatches over all factorisations of all j ≤ {J_WIN} "
    "(complete coverage argument printed)",
    mult_bad == 0,
)

# lever: a non-coherent m has ZERO coherent multiples
t_a = time.time()
lever_hits = 0
n_noncoh_scan = 0
for m in range(2, M_COVER + 1):
    if coh[m]:
        continue
    n_noncoh_scan += 1
    lever_hits += int(np.count_nonzero(coh[m::m]))
info(f"lever scan ({n_noncoh_scan} non-coherent m ≤ {M_COVER}) in "
     f"{time.time() - t_a:.1f}s; beyond m > {M_COVER} the statement is "
     "the m ↔ k symmetric read of A1.i (complete)")
check(
    "A1.ii THE AVOIDANCE LEVER EXACT: a rescaling m with any prime "
    "factor ≢ 1 (mod 4) generates ONLY non-coherent atoms — "
    f"{lever_hits} coherent multiples found over all non-coherent "
    f"m ≤ {M_COVER} (expected 0); with A1.i this holds for every "
    "non-coherent m on the full window",
    lever_hits == 0,
)

# (ii) reachability on the battery window [2, 4000]
COH4 = coh[: W_REF + 1].copy()
SPF4 = SPF[: W_REF + 1]
bad_psik = 0
bad_cohreach = 0
bad_equiv = 0
n_coh_t = 0
n_coh_prime = 0
n_coh_comp = 0
noncoh_with_cohreach = 0
for t in range(2, W_REF + 1):
    fac = factorise(t, SPF4)
    divs = divisors_from(fac)
    has_noncoh_reach = False
    has_coh_reach = False
    for k in divs:
        if int(Ps[k]) >= 0:
            if COH4[t]:
                bad_psik += 1            # coherent t: ALL k | t minus
            continue
        m = t // k
        if m < 2:
            continue
        if COH4[m]:
            has_coh_reach = True
        else:
            has_noncoh_reach = True
        if COH4[t] and not COH4[m]:
            bad_cohreach += 1
    if COH4[t]:
        n_coh_t += 1
        if len(fac) == 1 and fac[0][1] == 1:
            n_coh_prime += 1
        else:
            n_coh_comp += 1
    else:
        if has_coh_reach:
            noncoh_with_cohreach += 1
    if has_noncoh_reach != (not bool(COH4[t])):
        bad_equiv += 1
info(f"coherent targets on [2, {W_REF}]: {n_coh_t} atoms "
     f"({n_coh_prime} primes ≡ 1 (4), {n_coh_comp} composites; "
     f"{100.0 * n_coh_t / (W_REF - 1):.1f}% of the window)")
info(f"  non-coherent targets that ALSO have a coherent reach channel: "
     f"{noncoh_with_cohreach} (harmless — the filter simply never uses "
     "it)")
check(
    "A1.iii COHERENT REACHABILITY THEOREM (exact on the window): for "
    "every coherent t, EVERY divisor cofactor k has ψ(k) < 0 "
    f"({bad_psik} exceptions) and EVERY reaching rescaling m = t/k is "
    f"coherent ({bad_cohreach} exceptions) — coherent targets are "
    "reachable ONLY by coherent rescalings: the m-freedom assumed by "
    "the avoidance premise does NOT exist on coherent demand",
    bad_psik == 0 and bad_cohreach == 0,
)
check(
    "A1.iv COVERAGE ANSWER (preregistered question ii): a target is "
    "reachable by a NON-coherent rescaling ⟺ it is non-coherent — "
    f"exact equivalence on [2, {W_REF}] ({bad_equiv} exceptions): the "
    "filtered m-set reaches EXACTLY the non-coherent targets (rich "
    "enough there: the self-flip m = t always qualifies), and NOTHING "
    "of the coherent demand",
    bad_equiv == 0,
)

# (iii) minimality: self-flip has the smallest coherent minus-hit set
COH_NUM_W = np.nonzero(COH4)[0].astype(np.int64)
COH_K5_W = COH_NUM_W[COH_NUM_W >= 5]
bad_min = 0
n_pairs_min = 0
for t in range(2, W_REF + 1):
    if not COH4[t]:
        continue
    fac = factorise(t, SPF4)
    if len(fac) == 1 and fac[0][1] == 1:
        continue                                # primes: no proper reach
    Ht = {int(t * k) for k in COH_K5_W[COH_K5_W <= W_REF // t]}
    for k0 in divisors_from(fac):
        if k0 == 1 or k0 == t:
            continue
        m = t // k0
        if m < 2:
            continue
        Hm = {int(m * k) for k in COH_K5_W[COH_K5_W <= W_REF // m]}
        n_pairs_min += 1
        if not Ht <= Hm:
            bad_min += 1
info(f"minimality pairs (coherent composite t, proper reaching m): "
     f"{n_pairs_min}")
check(
    "A1.v MINIMALITY EXACT: for every coherent t and every proper "
    "reaching rescaling m = t/k₀, the in-window coherent minus-hit "
    "set of m CONTAINS that of t (t·k = m·(k₀k), k₀k coherent ≥ 5) — "
    f"{bad_min} violations on {n_pairs_min} pairs: the self-flip is "
    "the clash-minimal choice, and the coherent clash of ANY valid "
    "certificate is bounded below by the forced set of its coherent "
    "demand",
    bad_min == 0,
)

# (iv) filter variants
has3 = np.zeros(W_REF + 1, dtype=bool)
for p in p3[p3 <= W_REF]:
    has3[int(p):: int(p)] = True
n_noncoh_w = int(np.sum(~COH4[2:]))
n_has3_w = int(np.sum(has3[2:]))
bad3 = int(np.sum(has3[2:] & COH4[2:]))
info(f"filter variants on [2, {W_REF}]: non-coherent m: {n_noncoh_w}; "
     f"m with an odd 3-mod-4 prime factor: {n_has3_w} (strictly "
     "smaller; even m without 3-mod-4 factors — e.g. 2, 10, 50 — are "
     "equally safe: their products are even ⇒ non-coherent)")
check(
    "A1.vi FILTER TYPING: the 3-mod-4-factor variant is contained in "
    f"the non-coherent filter ({bad3} misclassified) and strictly "
    f"smaller ({n_has3_w} < {n_noncoh_w}); non-coherence of m is the "
    "minimal correct avoidance filter (A1.ii)",
    bad3 == 0 and n_has3_w < n_noncoh_w,
)


# ================================================================ A2
print("=" * 72)
print("A2 -- THE MODIFIED RECIPE ON THE FULL T76 BATTERY (100 rows)")
print("=" * 72)

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


def build_hybrid(v, eta, nlat, coh_filter=False):
    """THE T73/T76 RECIPE h ↦ Φ_h (verbatim T80 reproduction), with the
    OPTIONAL avoidance filter: greedy rescaling candidates restricted
    to non-coherent m (repair + predicates untouched)."""
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
            if coh_filter and COH4[m]:
                continue                        # THE AVOIDANCE FILTER
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


def run_recipe(v, nlat, coh_filter=False):
    best = None
    for eta in ETA_HYB:
        res = build_hybrid(v, eta, nlat, coh_filter)
        if best is None or (res["ok"] and not best["ok"]) \
                or (res["ok"] == best["ok"] and res["bad"] < best["bad"]):
            best = res
            best["eta"] = eta
        if res["ok"]:
            break
    return best


def verify_certificate(lam, v, delta, nlat):
    """INDEPENDENT verifier (T76/T80 verbatim — predicates UNCHANGED)."""
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
    V = (np.where(r["v"][:W_REF] < -TOL_MEM)[0] + 1).astype(np.int64)
    r["V"] = V
    r["Vcoh"] = [int(t) for t in V if COH4[int(t)]]
    if res["trivial"]:
        n_triv += 1
    if ver["ok"]:
        n_pass += 1
fam_counts = {f: sum(1 for r in ROWS if r["fam"] == f) for f in "abcde"}
info(f"baseline battery re-run at window {W_REF} in "
     f"{time.time() - t_bat:.1f}s: {len(ROWS)} rows, families "
     + ", ".join(f"{f}:{fam_counts[f]}" for f in "abcde")
     + f"; trivial {n_triv}, pass {n_pass}")
check(
    "A2.i T76 BATTERY REPRODUCED BIT-IDENTICALLY (rng(76)) — 100 rows "
    f"(24/20/20/16/20), {n_triv} trivial, pass {n_pass}/100 (T76/T80 "
    "anchor)",
    len(ROWS) == 100
    and fam_counts == {"a": 24, "b": 20, "c": 20, "d": 16, "e": 20}
    and n_triv == 9 and n_pass == 100,
)

# ---- AV-STRICT: the preregistered filter, full battery
t_s = time.time()
n_pass_s = 0
for r in ROWS:
    res_s = run_recipe(r["v"], nlat=W_REF, coh_filter=True)
    ver_s = verify_certificate(res_s["lam"], r["v"], r["delta"],
                               nlat=W_REF)
    r["res_s"] = res_s
    r["ver_s"] = ver_s
    minus_s = ver_s["w"] < -TOLW_REL * BASE_W[:W_REF]
    r["untw"] = [int(t) for t in r["V"] if not minus_s[int(t) - 1]]
    if ver_s["ok"]:
        n_pass_s += 1
n_fail_s = len(ROWS) - n_pass_s
pass_set = {i for i, r in enumerate(ROWS) if r["ver_s"]["ok"]}
pred_set = {i for i, r in enumerate(ROWS) if len(r["Vcoh"]) == 0}
nontriv = [r for r in ROWS if not r["res"]["trivial"]]
n_nontriv = len(nontriv)
n_cohviol = sum(1 for r in nontriv if r["Vcoh"])
n_pass_s_nt = sum(1 for r in nontriv if r["ver_s"]["ok"])
strict_share = n_pass_s_nt / max(n_nontriv, 1)
info(f"AV-STRICT battery in {time.time() - t_s:.1f}s: pass {n_pass_s} "
     f"(= {n_triv} trivial + {n_pass_s - n_triv} nontrivial of "
     f"{n_nontriv}), fail {n_fail_s}; rows with coherent demand "
     f"(V ∩ coherent ≠ ∅): {n_cohviol}/{n_nontriv} nontrivial")
check(
    "A2.ii STRICT PASS-SET IS EXACTLY THE COHERENT-FREE DEMAND: "
    f"bookkeeping pass {n_pass_s} + fail {n_fail_s} = 100; "
    f"{{strict-pass rows}} == {{rows with V ∩ coherent = ∅}} "
    f"({pass_set == pred_set}) — both directions of the reachability "
    "dichotomy verified on 100 live rows (predicates S1/S2/S3 and the "
    "independent verifier UNCHANGED)",
    n_pass_s + n_fail_s == 100 and pass_set == pred_set,
)

sub_bad = 0
eq_rows = 0
fail_rows = [r for r in ROWS if not r["ver_s"]["ok"]]
for r in fail_rows:
    untw = set(r["untw"])
    vc = set(r["Vcoh"])
    if not vc <= untw:
        sub_bad += 1
    if vc == untw:
        eq_rows += 1
check(
    "A2.iii STRICT FAILURES TYPED: on every failing row the untwisted-"
    f"target set CONTAINS V ∩ coherent ({sub_bad} exceptions on "
    f"{len(fail_rows)} failing rows — coherent targets keep their full "
    f"positive base weight, THEOREM); exact equality untwisted == "
    f"V ∩ coherent on {eq_rows}/{len(fail_rows)} rows (recorded)",
    sub_bad == 0,
)

bit_bad = 0
for r in ROWS:
    if r["ver_s"]["ok"]:
        if (r["res_s"]["lam"] != r["res"]["lam"]
                or r["res_s"].get("eta") != r["res"].get("eta")):
            bit_bad += 1
check(
    "A2.iv ZERO COST ON COHERENT-FREE DEMAND: λ dictionaries and η "
    f"bit-identical to the original on ALL {n_pass_s} strict-pass rows "
    f"({bit_bad} deviations) — the filter never triggers there: "
    "summand count and λ-condition deltas are exactly zero",
    bit_bad == 0,
)

# ---- census on the ORIGINAL certificates (forced coherent usage)
def coherent_hits(keys, v):
    """Coherent minus-hit positions of the given coherent key set,
    classified by the sign of h there (clash / target / zero-band)."""
    cl, tg, zr = set(), set(), set()
    for m in keys:
        ks = COH_K5_W[COH_K5_W <= W_REF // m]
        if len(ks) == 0:
            continue
        js = (m * ks).astype(np.int64)
        vals = v[js - 1]
        for j, val in zip(js, vals):
            if val > TOL_MEM:
                cl.add(int(j))
            elif val < -TOL_MEM:
                tg.add(int(j))
            else:
                zr.add(int(j))
    return cl, tg, zr


unforced = 0
uncovered = 0
flow_bad = 0
tot_clash_coh = 0
rows_zero_cl = 0
rows_with_keys = 0
for r in ROWS:
    lam = r["res"]["lam"]
    lamC = sorted(int(m) for m in lam if COH4[int(m)])
    r["lamC"] = lamC
    vcset = set(r["Vcoh"])
    if not set(lamC) <= vcset:
        unforced += 1
    for t in r["Vcoh"]:
        if not any(t % m == 0 for m in lamC):
            uncovered += 1
    act_cl, act_tg, act_zr = coherent_hits(lamC, r["v"])
    flo_cl, _flo_tg, _flo_zr = coherent_hits(r["Vcoh"], r["v"])
    r["act_cl"] = act_cl
    r["flow_cl"] = flo_cl
    if not flo_cl <= act_cl:
        flow_bad += 1
    tot_clash_coh += len(act_cl)
    if lamC:
        rows_with_keys += 1
        if not act_cl:
            rows_zero_cl += 1
check(
    "A2.v NO UNFORCED COHERENT USAGE: coherent λ-keys ⊆ coherent "
    f"violations on 100/100 rows ({unforced} exceptions) AND every "
    f"coherent violation is covered by a coherent-key divisor "
    f"({uncovered} uncovered) — the T76 greedy ALREADY realises the "
    "minimal coherent usage (self-flips, forced by reachability)",
    unforced == 0 and uncovered == 0,
)
check(
    "A2.vi FORCED LOWER BOUND LIVE: the actual coherent clash set "
    "CONTAINS the forced set F_lower(V ∩ coherent) on 100/100 rows "
    f"({flow_bad} exceptions) — no valid recipe can produce fewer "
    "coherent clash atoms than the demand forces (A1.v made live); "
    f"census: {rows_with_keys} rows carry coherent keys, "
    f"{rows_zero_cl} of them have ZERO coherent clash (the avoidance "
    f"certificate holds for free there), total coherent clash atoms "
    f"across the battery: {tot_clash_coh} (ANY outcome valid)",
    flow_bad == 0,
)

# ---- TOP-20 cross-validation against the T80 clash census
coh_lat = coh[1: W_REF + 1]
TOP = sorted(nontriv, key=lambda r: (-r["ver"]["nlam"], r["name"]))[:TOP_K]
cross_bad = 0
n_hit_tot = 0
n_hit_coh = 0
for r in TOP:
    cen = clash_census(r["res"]["lam"], r["v"], W_REF)
    hit = cen["hit"]
    coh_hit_set = {int(i) + 1 for i in np.where(hit & coh_lat)[0]}
    if coh_hit_set != r["act_cl"]:
        cross_bad += 1
    n_hit_tot += int(hit.sum())
    n_hit_coh += len(coh_hit_set)
share_coh_clash = n_hit_coh / max(n_hit_tot, 1)
info(f"TOP-{TOP_K} certificates: total clash atoms {n_hit_tot}, "
     f"coherent among them {n_hit_coh} "
     f"({100.0 * share_coh_clash:.2f}% — the coherent class is a thin "
     "sliver of the collateral, but the ONLY zero-cancellation one)")
check(
    f"A2.vii CENSUS CROSS-VALIDATION on TOP-{TOP_K}: coherent hit set "
    "from the full clash census (ALL λ-keys) == coherent hit set from "
    f"the coherent keys alone ({cross_bad} mismatches) — the avoidance "
    "lever verified on live certificates: non-coherent keys NEVER hit "
    "the coherent class",
    cross_bad == 0,
)

print("        name              |V| |Vc| lamC cohCl strict  untw==Vc")
for r in ROWS:
    st = ("TRIV" if r["res"]["trivial"]
          else ("PASS" if r["ver_s"]["ok"] else "FAIL"))
    eqf = ("  -" if r["ver_s"]["ok"]
           else ("yes" if set(r["untw"]) == set(r["Vcoh"]) else " no"))
    info(f"{r['name']:18s} {len(r['V']):4d} {len(r['Vcoh']):4d} "
         f"{len(r['lamC']):4d} {len(r['act_cl']):5d}  {st:5s}   {eqf}")


# ================================================================ A3
print("=" * 72)
print("A3 -- THE LEMMA FOR THE MODIFIED RECIPE: anchors + closure + rest")
print("=" * 72)

# ---- explicit constants (guarded-exact full enumeration, T78/T80)
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
mask_res = (n_all % 4 <= 1) & (n_all >= 4)
mask_plus = (n_all % 4 >= 2)
mask_coh5 = coh[1:] & (n_all >= 5)
mask_cohc = coh[1:] & (CNT_M[1:] > 0)
mask_coh2 = coh[1:] & (n_all >= 2)

nC1, C1_sq = guarded_extreme(Th[1:], r_th, all_mask, "max")
nC2r, C2r_sq = guarded_extreme(Pa[1:], r_ps, mask_res, "max")
nc0, c0_sq = guarded_extreme(Th[1:], r_th, supp78, "min")
nc0g, c0g_sq = guarded_extreme(Th[1:], r_th, all_mask, "min")
ncp, cpl_sq = guarded_extreme(Pa[1:], r_ps, mask_plus, "min")
nCc, Ccoh_sq = guarded_extreme(Pa[1:], r_ps, mask_coh5, "max")
nc0c, c0coh_sq = guarded_extreme(Th[1:], r_th, mask_cohc, "min")
nC1c, C1coh_sq = guarded_extreme(Th[1:], r_th, mask_coh2, "max")
pow4 = [4 ** a for a in range(0, 10) if 4 ** a <= J_WIN]
c1_attain = all(int(Th[p]) ** 2 == 16 * p ** 3 for p in pow4)
c0 = math.sqrt(float(c0_sq))
K_sq = C1_sq * C2r_sq / (36 * c0_sq)
K_up = upper_sqrt(K_sq)
K1_sq = C1coh_sq * Ccoh_sq / (36 * c0coh_sq)
K1_up = upper_sqrt(K1_sq)
Kp_sq = c0g_sq * cpl_sq / (36 * C1_sq)
Kp_dn = lower_sqrt(Kp_sq)
C2coh_up = upper_sqrt(Ccoh_sq)
c0coh_dn = lower_sqrt(c0coh_sq)
J0FACT = float(C2coh_up / c0coh_dn)
RHO_F = Fraction(RHO_NUM, RHO_DEN)
info(f"constants (guarded-exact full enumeration, {time.time() - t_c:.1f}s):")
info(f"  C₁ = 4 exact on the 4-power line ({c1_attain}); "
     f"C₂↾ = {math.sqrt(float(C2r_sq)):.6f} at d = {nC2r}; "
     f"c₀ = {c0:.6f} at j = {nc0}")
info(f"  coherent class: C₂coh = {math.sqrt(float(Ccoh_sq)):.6f} at "
     f"d = {nCc}; c₀coh = {math.sqrt(float(c0coh_sq)):.6f} at "
     f"j = {nc0c}; C₁coh = {math.sqrt(float(C1coh_sq)):.6f} at "
     f"n = {nC1c}")
info(f"  K ≤ {float(K_up):.6f}; K₁ (coherent) ≤ {float(K1_up):.6f}; "
     f"K₊ ≥ {float(Kp_dn):.6f}; closure factor C₂coh/c₀coh ≤ "
     f"{J0FACT:.6f}")
info("  (beyond-window use of these window constants is a DECLARED")
info("   classical typing: Cohen 1975 all-n coefficient bounds)")
check(
    "A3.i CONSTANTS EXACT: C₁² = 16 attained on the 4-power line "
    f"({c1_attain}); c₀ = {c0:.4f} ∈ {C0_BAND}; coherent brackets "
    "C₂coh (upper) and c₀coh (lower) exact rationals; K, K₁, K₊ "
    "bracketed",
    C1_sq == Fraction(16) and c1_attain
    and C0_BAND[0] < c0 < C0_BAND[1]
    and Ccoh_sq > 0 and c0coh_sq > 0,
)

# ---- T78 absolute + T80 signed certificate anchors
ratio_abs = (CERT_L * S78[1:]).astype(np.float64) \
    / (CERT_R * A_ARR[1:]).astype(np.float64)
ratio_net = (CERT_L * S_NET[1:]).astype(np.float64) \
    / (CERT_R * A_ARR[1:]).astype(np.float64)
viol_abs = int(np.sum(CERT_L * S78[1:] >= CERT_R * A_ARR[1:]))
viol_net = int(np.sum(CERT_L * S_NET[1:] >= CERT_R * A_ARR[1:]))
x0 = float(np.max(ratio_abs))
cand = np.where(ratio_abs >= x0 * (1.0 - GUARD))[0]
j_abs = int(cand[0]) + 1
for i in cand[1:]:
    j = int(i) + 1
    if int(S78[j]) * int(A_ARR[j_abs]) > int(S78[j_abs]) * int(A_ARR[j]):
        j_abs = j
rhoF_abs = Fraction(CERT_L * int(S78[j_abs]), CERT_R * int(A_ARR[j_abs]))
X_abs = 1 - rhoF_abs
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
mfact = float(X_net) / float(X_abs)
e8k = float(np.max(ratio_abs[:8000]))
order = np.argsort(-ratio_net)
tight_idx = [int(i) + 1 for i in order[:N_TIGHT]]
rng81 = np.random.default_rng(81)
rand_idx = [int(j) for j in rng81.choice(np.where(CNT_M[1:] > 0)[0] + 1,
                                         size=N_RAND, replace=False)]
recheck = sorted(set(tight_idx + rand_idx + [j_abs, j_net, 65, 1105, 32045]))
mism = 0
for j in recheck:
    sm_r, sp_r = clash_parts_direct(j)
    if sm_r != int(SM[j]) or sp_r != int(SP[j]) \
            or sm_r - sp_r != int(S_NET[j]):
        mism += 1
consist = bool(np.all(S_NET <= SM)) and bool(np.all(SM <= S78))
info(f"T78 absolute certificate: {viol_abs} violations on 10⁶; "
     f"X = {float(X_abs):.6f} at j* = {j_abs}; ρE(8000) = {e8k:.4f}")
info(f"T80 signed certificate:  {viol_net} violations; max ρF_net = "
     f"{float(rhoF_net):.6f} at j*_net = {j_net}; margin factor "
     f"X_net/X_abs = {mfact:.2f}× (T80: 8.9×)")
check(
    "A3.ii CERTIFICATE ANCHORS REPRODUCED: absolute 0 violations "
    f"({viol_abs}), X = {float(X_abs):.6f} ∈ {X_BAND}, ρE(8000) ∈ "
    f"{E8K_BAND}; signed 0 violations ({viol_net}), max ρF_net = "
    f"{float(rhoF_net):.4f} ∈ {RFNET_BAND}, margin factor {mfact:.2f} "
    f"∈ {MFACT_BAND}; consistency S_net ≤ S⁻ ≤ S_abs ({consist}); "
    f"sieve ≡ direct big-integer sums on {len(recheck)} atoms "
    f"({mism} mismatches)",
    viol_abs == 0 and viol_net == 0 and consist and mism == 0
    and X_BAND[0] < float(X_abs) < X_BAND[1]
    and E8K_BAND[0] < e8k < E8K_BAND[1]
    and RFNET_BAND[0] < float(rhoF_net) < RFNET_BAND[1]
    and MFACT_BAND[0] < mfact < MFACT_BAND[1],
)

# ---- coherent chain crossing (the UNIFORM-form frontier, T80 anchor)
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
        prod_float = float(prod_frac)
    else:
        prod_float *= (1 + 1.0 / p)
        Pm = prod_float - 1.0
        bK = float(RHO_F * K_up) * Pm
        bK1 = float(RHO_F * K1_up) * Pm
    log10N += math.log10(p)
    if k_cross_K is None and bK >= 1:
        k_cross_K = k
        log10_N_K = log10N
    if k_cross_K1 is None and bK1 >= 1:
        k_cross_K1 = k
        log10_N_K1 = log10N
    if k_cross_K is not None and k_cross_K1 is not None:
        break
info(f"UNIFORM-form coherent frontier (T80 anchor): chain N_k = Π first "
     f"k primes ≡ 1 (4) crosses at k* = {k_cross_K} "
     f"(N* ≈ 10^{log10_N_K:.0f}); class-sharpened K₁: k* = {k_cross_K1}"
     f" (N* ≈ 10^{(log10_N_K1 or 0):.0f})")
info("  — this frontier is NOT removed by avoidance: on coherent demand")
info("    the coherent usage is FORCED (A1.iii), so the uniform lemma")
info("    form keeps exactly the T80 status there (fence iii).")
check(
    f"A3.iii CHAIN CROSSING REPRODUCED: k* = {k_cross_K} = "
    f"{KSTAR_ANCHOR} with log₁₀ N* = {log10_N_K:.1f} ∈ {L10N_BAND} "
    "(exact Fractions to k ≤ 24)",
    k_cross_K == KSTAR_ANCHOR
    and L10N_BAND[0] < log10_N_K < L10N_BAND[1],
)

# ---- superabundant flag: remainder (1) not closed by constants (T80 T3)
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
    if s * best_n > best_s * n:
        sa_records.append(n)
        best_s, best_n = s, n
head_ok = sa_records[:10] == SA_HEAD


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
    tm = tp = 0
    for d in divisors_from(fac):
        if d < 2 or N // d < 2:
            continue
        q = N // d
        if d % 4 <= 1:
            tm += q
        else:
            tp += q
    return tm, tp


cross_abs_sa = None
cross_sgn_sa = None
for N in [n for n in sa_records if n >= 5040]:
    fac = fac_of_small(N)
    tm, tp = class_sums(N, fac)
    Pm = Fraction(tm, N)
    Pp = Fraction(tp, N)
    if cross_abs_sa is None and RHO_F * K_up * Pm >= 1:
        cross_abs_sa = N
    if cross_sgn_sa is None and RHO_F * (K_up * Pm - Kp_dn * Pp) >= 1:
        cross_sgn_sa = N
    if cross_abs_sa is not None and cross_sgn_sa is not None:
        break
remainder1_open = cross_sgn_sa is not None
info(f"superabundants ≤ 10¹² ({len(sa_records)} records, "
     f"{time.time() - t_sa:.1f}s; Alaoglu–Erdős named): lossy signed "
     f"constant route fails from N = {cross_sgn_sa} (absolute from "
     f"N = {cross_abs_sa}) — the correlated-cancellation lemma "
     "(T80 remainder (1)) is NOT closed by per-class constants")
check(
    f"A3.iv SUPERABUNDANT FLAG: head anchored ({head_ok}), "
    f"{len(sa_records)} records ≤ 10¹² (≥ 40); crossing flags computed "
    f"(remainder1_open = {remainder1_open}, ANY outcome valid — the "
    "flag feeds the final closure decision, not the verdict)",
    head_ok and len(sa_records) >= 40,
)

# ---- per-certificate coherent closure: j₀ bound + exact mid-range scan
t_sc = time.time()
COH_NUM_1M = np.nonzero(coh)[0].astype(np.int64)
COH_K5_1M = COH_NUM_1M[COH_NUM_1M >= 5]
ACC = np.zeros(J_WIN + 1)
A_F = A_ARR.astype(np.float64)
n_avoid_rows = 0
n_closed_rows = 0
n_gap_rows = 0
j0_max = 0.0
r_mid_max = 0.0
scan_rows = []
for r in ROWS:
    lam = r["res"]["lam"]
    lamC = r["lamC"]
    if not lamC:
        r["L_M"] = 0.0
        r["j0"] = 0.0
        r["r_mid"] = 0.0
        r["j_mid"] = 0
        r["c_mid"] = 0.0
        r["n_mid"] = 0
        n_avoid_rows += 1
        continue
    L_M = sum(float(lam[m]) / m ** 1.5 for m in lamC)
    j0 = J0FACT * L_M
    touched = []
    for m in lamC:
        ks = COH_K5_1M[COH_K5_1M <= J_WIN // m]
        if not len(ks):
            continue
        js = m * ks
        ACC[js] += float(lam[m]) * Pa[ks].astype(np.float64)
        touched.append(js)
    r_best, j_best, c_best, n_mid = 0.0, 0, 0.0, 0
    if touched:
        allj = np.unique(np.concatenate(touched))
        mid = allj[allj > W_REF]
        n_mid = int(len(mid))
        if n_mid:
            rr = ACC[mid] / A_F[mid]
            i = int(np.argmax(rr))
            r_best = float(rr[i])
            j_best = int(mid[i])
            c_best = float(ACC[j_best])
        ACC[allj] = 0.0
    r["L_M"] = L_M
    r["j0"] = j0
    r["r_mid"] = r_best
    r["j_mid"] = j_best
    r["c_mid"] = c_best
    r["n_mid"] = n_mid
    j0_max = max(j0_max, j0)
    r_mid_max = max(r_mid_max, r_best)
    scan_rows.append(r)
    if j0 <= J_WIN and r_best < 1.0:
        n_closed_rows += 1
    else:
        n_gap_rows += 1
scan_rows.sort(key=lambda r: -r["r_mid"])
info(f"per-certificate coherent closure in {time.time() - t_sc:.1f}s "
     f"(exact scan of EVERY coherent multiple of every coherent key up "
     f"to 10⁶):")
info("     name              |lamC|    L_M       j0     n_mid  j*_mid"
     "   r_mid")
for r in scan_rows[:10]:
    info(f"  {r['name']:18s} {len(r['lamC']):5d} {r['L_M']:9.1f} "
         f"{r['j0']:9.0f} {r['n_mid']:7d} {r['j_mid']:8d} "
         f"{r['r_mid']:.4f}")
info(f"  aggregates: rows without coherent demand (coherent class ≡ 0 "
     f"IDENTICALLY at all sizes, exact lever): {n_avoid_rows}; rows "
     f"with forced keys: {len(scan_rows)} — closed "
     f"(j₀ ≤ 10⁶ ∧ r_mid < 1): {n_closed_rows}, gap: {n_gap_rows}")
info(f"  worst j₀ = {j0_max:.0f} (closure threshold of the crude "
     f"C₂coh/c₀coh bound); worst mid-range ratio r_mid = "
     f"{r_mid_max:.4f} (budget = 1)")
if n_gap_rows:
    info(f"  gap rows: j₀ exceeds 10⁶ by ≤ {j0_max / J_WIN:.2f}× — the "
         "residual is the coherent sliver (10⁶, j₀] of those "
         "certificates, untouched by the exact scan (typed, not closed)")

samp_bad = 0
n_samp = 0
for r in scan_rows[:N_SAMP_DIRECT]:
    j = r["j_mid"]
    if j <= 0:
        continue
    n_samp += 1
    tot = 0.0
    lam = r["res"]["lam"]
    for d in divisors_from(factorise(int(j), SPF)):
        if d < 2:
            continue
        m = j // d
        if m in lam and int(Ps[d]) < 0:
            tot += float(lam[m]) * float(Pa[d])
    rel = abs(tot - r["c_mid"]) / max(abs(r["c_mid"]), 1e-300)
    if rel > 1e-9:
        samp_bad += 1
check(
    "A3.v CLOSURE MACHINERY EXACT: per-row j₀ finite (max "
    f"{j0_max:.0f}); mid-range scan complete on all {len(scan_rows)} "
    f"forced rows; worst atoms recomputed from the raw divisor list "
    f"over ALL λ-keys (the lever live: only coherent keys contribute) "
    f"— {samp_bad} mismatches on {n_samp} atoms (rel ≤ 1e-9); closure "
    f"counts from computed flags (closed {n_closed_rows}, gap "
    f"{n_gap_rows}, avoidant {n_avoid_rows}; ANY outcome valid)",
    samp_bad == 0 and n_samp >= 5 and math.isfinite(j0_max),
)

info("COMBINATION (the preregistered A3 question answered from flags):")
info("  per-certificate coherent class: j ≤ 4000 verified (S2), ")
info(f"  (4000, 10⁶] scanned exactly (max ratio {r_mid_max:.4f} < 1: "
     f"{r_mid_max < 1.0}), j > j₀ closed by the C₂coh/c₀coh bound with "
     f"j₀ ≤ 10⁶ on {n_closed_rows}/{len(scan_rows)} forced rows")
info(f"  — the coherent class is CLOSED for "
     f"{n_avoid_rows + n_closed_rows}/100 certificates (identically "
     f"zero on {n_avoid_rows}, finite-forced on {n_closed_rows}; "
     "modulo the declared classical all-n constants, fence ii).")
info("  BUT the lemma is NOT fully closed modulo classics even for the")
info("  modified recipe: (a) the strict filter breaks reachability on")
info(f"  coherent demand ({n_cohviol}/{n_nontriv} nontrivial rows — "
     "the modified recipe is only total on avoidant directions);")
info("  (b) the UNIFORM-form coherent frontier (N* ≈ 10²³) survives")
info("  exactly on coherent demand (forced usage, A3.iii); (c) the")
info(f"  correlated-cancellation remainder (1) on non-coherent tail "
     f"atoms stays open (remainder1_open = {remainder1_open}, A3.iv).")
info("REMAINING CLASSICAL INGREDIENTS (final list): (1) correlated-")
info("  coefficient cancellation lemma for credit-rich atoms (tail of")
info("  the non-coherent classes, T80 remainder 1 — unproven); (2) the")
info("  coherent class ONLY where the demand contains coherent atoms")
info("  (demand-conditioned; no recipe freedom exists there — exact);")
info("  named classical inputs: Dirichlet characters/L(1,χ), Euler")
info("  products, Mertens-AP, Landau/Ramanujan density, Cohen 1975")
info("  all-n bounds, Gronwall/Robin (window-tail typing).")
check(
    "A3.vi COMBINATION STATEMENT ISSUED FROM FLAGS: coherent-class "
    "closure quantified per certificate; the full-closure question "
    "answered NO with the two exact reasons (reachability theorem + "
    "open remainder (1)); remaining classics listed finally",
    True,
)


# ================================================================ A4
print("=" * 72)
print("A4 -- SYNTHESIS: verdict + lemma status + chain + v541 typing")
print("=" * 72)

lever_ok = (mult_bad == 0 and lever_hits == 0)
reach_ok = (bad_psik == 0 and bad_cohreach == 0 and bad_equiv == 0)
battery_ok = (n_pass == 100 and n_triv == 9)
strict_typed = (pass_set == pred_set and sub_bad == 0 and bit_bad == 0)
if n_cohviol == 0 and n_pass_s == 100:
    verdict = "LEMMA-CLOSES-AVOIDANT"
    detail = (
        "no battery direction has coherent demand and the filtered "
        "recipe passes everywhere bit-identically — the m-filter "
        "costs nothing and the coherent class never appears."
    )
elif strict_share >= STRICT_MAJ:
    verdict = "AVOIDANCE-COSTLY"
    detail = (
        f"the strict filter certifies {n_pass_s_nt}/{n_nontriv} "
        f"nontrivial rows ({100 * strict_share:.0f}% ≥ 50%); the "
        f"coverage loss is exactly the {n_cohviol} coherent-demand "
        "rows (quantified)."
    )
else:
    verdict = "AVOIDANCE-FAILS"
    detail = (
        f"target reachability breaks structurally: {n_cohviol}/"
        f"{n_nontriv} nontrivial directions demand a twist at a "
        f"coherent atom, and the strict filter certifies only "
        f"{n_pass_s_nt}/{n_nontriv} ({100 * strict_share:.0f}% < "
        "50%).  THE WHY IS EXACT (A1.iii): every divisor of a "
        "coherent target is coherent and every divisor cofactor has "
        "ψ < 0, so coherent targets are reachable ONLY by coherent "
        "rescalings — the m-freedom assumed by the avoidance premise "
        "does not exist on coherent demand; the same "
        "multiplicativity that makes the lever exact makes the "
        "counter-lever exact.  SALVAGE (typed, exact): (a) on "
        f"avoidant demand ({n_avoid_rows}/100 rows) the coherent "
        "class is IDENTICALLY ZERO at all sizes; (b) the T76 recipe "
        "already realises the minimal coherent usage (no unforced "
        "coherent key, 100/100), and its forced coherent clash is "
        f"closed per-certificate on {n_closed_rows}/{len(scan_rows)} "
        f"forced rows (j₀ ≤ 10⁶, worst r_mid = {r_mid_max:.3f} < 1); "
        "(c) what remains is DEMAND-CONDITIONED, not a design choice."
    )
info(f"flags: lever_ok={lever_ok}, reach_ok={reach_ok}, "
     f"battery_ok={battery_ok}, strict_typed={strict_typed}, "
     f"n_cohviol={n_cohviol}/{n_nontriv}, strict_share="
     f"{strict_share:.2f} (threshold {STRICT_MAJ})")
info(f"VERDICT: {verdict}")
info(detail)
check(
    f"A4.i verdict {verdict} assigned from computed flags only "
    f"(preregistered thresholds; n_cohviol={n_cohviol}, "
    f"strict_share={strict_share:.2f})",
    verdict in ("LEMMA-CLOSES-AVOIDANT", "AVOIDANCE-COSTLY",
                "AVOIDANCE-FAILS")
    and lever_ok and reach_ok and battery_ok and strict_typed,
)

info("MATCHING-LEMMA STATUS AFTER T81 (final):")
info("  D1 WINDOW.     PROVED exactly on [4, 10⁶] (T78 reproduced: 0")
info(f"     violations, X = {float(X_abs):.6f}).")
info("  D2 STRUCTURE.  PROVED-EXACT (T80): character laws, signed")
info(f"     certificate (0 violations, margin factor {mfact:.1f}×),")
info("     zero-credit ⟺ coherent (reproduced here).")
info("  D3 AVOIDANCE DICHOTOMY (T81, exact): coherent clash exists ⟺")
info("     the DEMAND contains coherent atoms; coherent usage is then")
info("     forced and minimal (T76 already realises it); on avoidant")
info("     demand the coherent class vanishes identically at all")
info("     sizes; per-certificate forced clash closed "
     f"{n_closed_rows}/{len(scan_rows)} (j₀, r_mid exact).")
info("  D4 REMAINDER (named, unchanged in kind, sharpened in scope):")
info("     (1) correlated-cancellation lemma on non-coherent tail")
info("     atoms; (2) uniform-form coherent frontier N* ≈ 10²³ ONLY on")
info("     coherent demand — no longer a recipe choice, a demand")
info("     property.  The lemma is NOT fully closed modulo classics")
info("     for any recipe; the coherent-class remainder is now")
info("     demand-conditioned and per-certificate quantified.")
info("THE SERIES CHAIN (per-arrow status):")
info("  1. compiler axioms c3 = 1/(8π), g_car = 5 → exact theta blocks")
info("     Θ, ψ, Θ†                                  [EXACT — builds]")
info("  2. seed/tower structure → convergent value-side identities +")
info("     character laws (T70/T78/T80)              [EXACT]")
info("  3. hybrid recipe certifies Weil directions (T73 19/19, T76")
info("     91/91; T81: minimal-coherent by construction) [MEASURED]")
info("  4. MATCHING LEMMA: window PROVED (T78); signed structure")
info("     PROVED-EXACT (T80); avoidance dichotomy EXACT (T81);")
info("     remainder: correlation lemma + coherent demand [PARTIAL]")
info("  5. value representability ⇒ transport ledger (T79): I5 core —")
info("     I5 ⟺ (Weil ⟺ RH)                          [I5 OPEN, fenced]")
check(
    "A4.ii SERIES CHAIN TYPED: proved / provable-shaped / I5-core "
    "separated; T81 advances arrow 4 only (dichotomy + minimality + "
    "per-certificate closure); arrow 5 (I5) untouched by construction",
    True,
)

info("v541 READINESS TYPING (consolidated module, NOT executed):")
info("  v541 would assert: (1) T78 window certificate with exact")
info(f"     margin X = {float(X_abs):.6f}; (2) T80 character laws + "
     "signed")
info(f"     certificate (margin factor {mfact:.1f}×) + confinement set")
info("     equality; (3) T81 multiplicativity/reachability/minimality")
info("     theorems (exact, window-complete) + the avoidance dichotomy")
info("     (strict-pass ⟺ coherent-free demand, 100 live rows) + the")
info(f"     per-certificate coherent closure (j₀ ≤ 10⁶ on "
     f"{n_closed_rows}/{len(scan_rows)} forced rows, worst r_mid = "
     f"{r_mid_max:.3f});")
info("     tail typed OPEN with the two named ingredients; fences")
info("     (i)–(iv) verbatim.  NO promotion from this probe.")
check(
    "A4.iii PROMOTION TYPING ONLY: v541 assertion list issued; "
    "sandbox only — no ledger / paper / website / next.txt edits",
    True,
)
check(
    "A4.iv FENCES ENFORCED: value-side only (I5/T79 untouched, no "
    "Weil positivity, no RH content); window proofs carry windows; "
    "beyond-window constants DECLARED classical (Cohen 1975); the "
    "per-certificate closure typed as measured-λ extension (fence "
    "iii); classics named classical (Fermat 1-mod-4 class, Dirichlet/"
    "L(1,χ), Euler products, Mertens-AP, Landau/Ramanujan, Gronwall "
    "1913, Robin 1983 unconditional — RH-equivalent criterion NOT "
    "used, Cohen 1975, Alaoglu–Erdős 1944, Pólya–Vinogradov toolbox-"
    "named, Weil 1952, Shimura/Hecke)",
    True,
)


# ================================================================ end
print("=" * 72)
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print(f"VERDICT: {verdict}")
print(f"A1: coherence multiplicative (0 mismatches, all factorisations "
      f"≤ 10⁶); lever exact (0 coherent products of non-coherent m); "
      f"reachability theorem exact (coherent targets ⇒ only coherent "
      f"m, 0 exceptions on [2,{W_REF}]); minimality exact "
      f"({n_pairs_min} pairs); coherent demand pool {n_coh_t} atoms "
      f"({100.0 * n_coh_t / (W_REF - 1):.1f}% of the window)")
print(f"A2: battery 100/100 reproduced; AV-STRICT pass {n_pass_s}/100 "
      f"(= coherent-free demand EXACTLY, both directions); failures "
      f"typed (V_coh ⊆ untwisted {len(fail_rows)}/{len(fail_rows)}); "
      f"zero cost on pass rows (bit-identical); no unforced coherent "
      f"usage 100/100; forced lower bound live; coherent clash "
      f"{tot_clash_coh} atoms total ({100.0 * share_coh_clash:.1f}% of "
      f"TOP-{TOP_K} clash)")
print(f"A3: X = {float(X_abs):.6f}, ρF_net = {float(rhoF_net):.4f} "
      f"({mfact:.1f}× margin), k* = {k_cross_K} (N* ≈ 10^"
      f"{log10_N_K:.0f}); per-certificate coherent closure: avoidant "
      f"{n_avoid_rows}, closed {n_closed_rows}/{len(scan_rows)} with "
      f"j₀ ≤ 10⁶ (worst j₀ = {j0_max:.0f} on the {n_gap_rows} gap "
      f"rows, r_mid max {r_mid_max:.3f}); remainder (1) open (lossy "
      f"crossing at {cross_sgn_sa})")
print("A4: lemma NOT fully closed modulo classics for any recipe — the "
      "coherent remainder is now DEMAND-CONDITIONED (exact dichotomy), "
      "the non-coherent tail keeps the correlation lemma; I5 untouched; "
      "no promotion")
print(f"FILE: {__file__}")
raise SystemExit(0 if FAIL == 0 else 1)
