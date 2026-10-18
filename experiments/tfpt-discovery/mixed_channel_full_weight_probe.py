"""Discovery probe (2026-07-25), part 69 — contract MIXED.CHANNEL.FULL.WEIGHT.

Continuation of the polarisation attack after T68 (GEOMETRIC.POLARIZATION,
RESHUFFLE-ONLY).  T68 established: the minus of the family is the
Rankin–Selberg / ζ(2·) structure of the SHARED kernel — the even-k
deletion [·,0,·,0] of the p^{3k}-layer weights is IDENTICAL on the family
core ([1,0,2,0]) and on the Eisenstein floor ([2,0,2,0]) and is
polarisation-invariant.  Three follow-up questions, preregistered:

 (1) THE MIXED CHANNEL Θ·g = N₊² − N₋² (Eisenstein × cusp — Rankin's
     1939 ORIGINAL method, classical) was NOT computed in T68 — which
     weight structure does it carry?
 (2) THE SIEVE READING: is the even-k deletion exactly the SQUARE SIEVE
     (Möbius over square divisors = ζ(2u)-division = the classical
     Rankin–Selberg normalisation of coefficient squaring), and do the
     two canonical COMPLETIONS to full [2,2,2,2] weights have a
     compiler carrier?
 (3) Is there ANY compiler-native channel without the deletion — or is
     the deletion UNIVERSAL on the square level?

S0  ZERO-FIREWALL (AST) + exact int64 sparse rebuild of g, Θ (T68
    technique); U4 fence; live family window (D_FAM ≥ 8000);
    N± = (Θ±g)/2 integral and ≥ 0.
M1  THE MIXED CHANNEL C = Θ·g:  (i) per-n exact C = N₊² − N₋² on ALL
    n ≤ QMAX; sign(C) = sign(b) (signed family with population
    weighting);  (ii) exact towers C(dp²) = (σ₃(p)−χp)(a_p−χp)·C(d)
    and the k=2 recurrences on the live window; ALGEBRAIC square-level
    Euler factor (sympy): S·D_mix polynomial, N_mix(χ=0) = 1−p⁶X²,
    D_mix = L_p(f₈,w)⁻¹·L_p(f₈,w−3)⁻¹ — the mixed channel is
    L_p(f₈,w)·L_p(f₈,w−3)/ζ_p(2w−6): Rankin f₈×Eisenstein, i.e.
    L_p(f₈,·)-shifts with the RS ζ(2·)-division (Rankin 1939 named
    classical);  (iii) THE WEIGHT QUESTION (heart): p^{3k}-layer
    weights of the C channel via the T68/T61 layer machinery
    (E_ST ∘ [q^{6k}]) — decided by machine: deletion, full, or other.
M2  SIEVE READING OF THE MINUS (algebraic): (i) the Cauchy–Littlewood /
    Rankin–Selberg local convolution lemma (classical):
      Σ_k h_k(s,t)h_k(u,v) X^k
        = (1−stuv X²) / [(1−suX)(1−svX)(1−tuX)(1−tvX)],
    sympy-exact with FREE Satake symbols; (ii) determinant instantiation
    st = uv = p³ ⇒ numerator 1−p⁶X² = 1/ζ_p(2w−6) INDEPENDENT of the
    pair ⇒ every coefficient-bilinear channel of two determinant-p³
    towers inherits the deletion factor; the five channels b², Θ²,
    Θ·g, N₊², N₋², N₊N₋ declined (closed forms + numeric bilinear-
    combination identities on live towers); (iii) the square sieve
    identification: [2,2,2,2] − [2,0,2,0] = [0,2,0,2] = λ-weights of
    ζ_p(2u); globally 2^{ω} = μ_□ ∗ d and d = 1_□ ∗ 2^{ω}
    coefficient-exact (Möbius square sieve; RS normalisation classical).
M3  THE TWO COMPLETIONS to [2,2,2,2]:
    (a) DIRICHLET-CONVOLUTION SQUARE (value square, not coefficient
        square): layer weights of L_amp(w)² — the Θ-side value square
        ζ_p(w)²ζ_p(w−3)² carries FULL [2,2,2,2] by construction
        (layer-exact); carrier: the pair object (m₁,m₂) — double-tower
        sums Σ Θ(dm₁²)Θ(dm₂²) verified integer-exact on live data;
        Hankel-rank decision: the convolution-square coefficient
        sequence is order-4 (degree-4 isobaric formal product, named
        classical), NOT order-2 ⇒ no single compiler-tower carrier;
        T57 Z(s,w) contains only the DIAGONAL Σ α(m)²m^{-w} ⇒ the pair
        channel is not in the existing machinery — typed FORMAL-PRODUCT.
    (b) SELBERG-POSITIVE completion (Λ²-sieve as namesake, classical):
        bookkeeping rearrangement of T63:
          fam [1,0,2,0,…] + 2·♭ [0,2,0,2,…] + Plancherel δ_{k1}
            = FULL [2,2,2,2,…]  (exact, generating functions);
        slot-disjointness: the even slots are carried 100% by the
        ♭ object; the ♭ object = index zeta of the SQUARE-CLASS
        tower points (m = r², i.e. d·r⁴): locally Σ_j Y^{2j}
        = 1/(1−Y²) = ζ_p(2u); the carrier is POPULATED and
        tower-exact on the live window (b(dr⁴) = b(d)·α♯(r²),
        Θ(dr⁴) = Θ(d)·α_E♯(r²)); prime-side identity numeric on the
        T63 test class.  Honest typing: the b²-weighted square-class
        channel is itself a bilinear channel and re-deletes (M2) —
        the resolution is INDEX/BOOKKEEPING level (inclusion–exclusion
        between fundamental family and square-class completion), not a
        positive operator completion of the full family form.
M4  SYNTHESIS: verdict over the three routes; final polarisation map;
    consequence for the remaining lever (amplitude route T67).

PREREGISTERED CRITERIA
  M1: per-n identity exact (all n ≤ QMAX); towers integer-exact
      (≥ 300 k=1, ≥ 40 k=2 pairs); N_mix degree ≤ 4 with vanishing
      tail, N_mix(χ=0) = 1−p⁶X² sympy-exact; layer signature decided
      by machine (honestly open: the C channel is NOT PSD and may
      carry weights forbidden to the PSD channels).
  M2: lemma exact k ≤ 10 (free Satake symbols); det-p³ numerator
      pair-independent; five channels declined; sieve identities
      integer-exact n ≤ 3000.
  M3a: layer lists exact; pair-carrier identities integer-exact
      (≥ 30); Hankel H3 ≠ 0 / H5 = 0 decision.
  M3b: bookkeeping identity exact (lists + generating functions);
      prime-side rel < 1e-12 (same-grid exact) and < 1e-6
      (♭-bridge, truncation); ≥ 25 populated square-class points,
      all tower-exact.
  VERDICTS (preregistered):
    FULL-WEIGHT-CARRIER — a channel with un-deleted weights AND a
        compiler carrier exists (name what it does / does not do);
    TOWER-RESOLUTION   — M3b: the ♭ content is exactly the tower
        double-counting — the minus resolved as inclusion–exclusion
        (bookkeeping, not obstruction);
    DELETION-UNIVERSAL — all square channels delete — the minus is a
        theorem-like invariant of the square level; the amplitude
        route (T67 Dirac with a non-quadratic pairing) is the only
        remaining path;
    combinations possible — named precisely.

FENCES (honest typing):
  (i)   STRUCTURE MAPPING ONLY — no RH evidence; nothing here is a
        positivity or zero statement;
  (ii)  classical results named as classical: Rankin 1939 original
        method (f × theta/Eisenstein integral), Rankin–Selberg
        ζ(2s)-normalisation of coefficient squares, Möbius / square
        sieve, Selberg Λ²-sieve (namesake of the positive completion),
        Piatetski-Shapiro–Rallis doubling (naming of the ♭/doubling
        term, per T63), Cauchy–Littlewood / SU(2) character convolution
        identity, Langlands isobaric sums, Siegel–Weil /
        Cohen–Eisenstein 5/2, Shimura correspondence, Waldspurger;
  (iii) "deletion universal" is proved on the window / local-algebraic
        level for determinant-p³ bilinear channels — a structure
        statement about the compiler family, not an RH statement.

Firewall: discovery sandbox only — no promotion, no ledger / paper /
website / next.txt / README edits.  ZERO-FIREWALL (AST-checked): no
Riemann-zero loaders; ζ/Γ as mpmath FUNCTIONS would be allowed but are
not needed (all prime sides are finite zero-free sums).  No RH-evidence
or "Weil positivity achieved" language.
"""
from __future__ import annotations

import ast
import inspect
import math
import time

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()

# ---------------------------------------------------------------- config
QMAX = 50_000                 # exact q-window for g and Theta
D_FAM = 8_000                 # live-d family window (contract: >= 8000)
HECKE_PS = (3, 5, 7, 11, 13)
HEAD_AP = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}
G_KEY = (0, 2, 0, 1, 1, 1)    # theta2(q2)^2 theta3(q2) theta4 theta4(q2)
TH_KEY = (0, 2, 1, 2, 0, 0)   # theta4 -> theta3 in both c-slots
K_MAX = 8                     # layer depth
K_SER = 12                    # sympy series depth for Euler fits
N_SIEVE = 3_000               # square-sieve coefficient window
N_LAM = 20_000                # prime-power window for zero-free prime sides
SQ_RS = (3, 5, 7)             # square-class radii r (d·r^4 <= QMAX)


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
    """Exact int64 multiplication by a sparse theta factor."""
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


def eta_pass(d, e, order):
    s = np.zeros(order + 1, dtype=np.int64)
    s[0] = 1
    for k in range(d, order + 1, d):
        for _ in range(e):
            s[k:] = s[k:] - s[:-k]
    return s


def kronecker(d: int, n: int) -> int:
    return int(sp.kronecker_symbol(d, n))


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


def sigma3(n: int) -> int:
    return int(sp.divisor_sigma(n, 3))


def alpha_sharp(d: int, m: int, a_f8) -> int:
    """T50/T67 Shimura tower coefficient (cusp side), odd m."""
    if m % 2 == 0:
        return 0
    tot = 0
    for j in sp.divisors(m):
        j = int(j)
        tot += int(sp.mobius(j)) * kronecker(d, j) * j * int(a_f8[m // j])
    return int(tot)


def alphaE_sharp(d: int, m: int) -> int:
    """Eisenstein-side tower coefficient: sigma_3 in place of a_f8."""
    if m % 2 == 0:
        return 0
    tot = 0
    for j in sp.divisors(m):
        j = int(j)
        tot += int(sp.mobius(j)) * kronecker(d, j) * j * sigma3(m // j)
    return int(tot)


def g_fejer(u, a):
    return max(0.0, 1.0 - abs(u) / a)


def g_gauss(u, sig):
    return math.exp(-0.5 * (u / sig) ** 2)


# ================================================================ S0
print("=" * 72)
print("S0 -- ZERO-FIREWALL (AST) + exact rebuild of g, Theta")
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
info("  Rankin 1939 (f×Eisenstein), RS ζ(2s)-normalisation, Möbius/")
info("  square sieve, Selberg Λ²-sieve (namesake), PS–Rallis doubling,")
info("  Cauchy–Littlewood, isobaric sums, Siegel–Weil, Shimura,")
info("  Waldspurger — all named classical.")

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
check(
    "S0.build: g and Θ live on integer q-powers; g matches the v537/T38 "
    "witness head [0,4,-8,0,0,0,16,...]; Θ ≥ 0",
    support_ok and list(g[:7]) == [0, 4, -8, 0, 0, 0, 16]
    and bool(np.all(Th >= 0)),
)

ns = np.arange(QMAX + 1)
mass_g_mod4 = {r: int(np.abs(g[1:][ns[1:] % 4 == r]).sum()) for r in range(4)}
check(
    "S0.g-fence: U4 fence for g (difference mass only on n≡1,2 mod 4)",
    mass_g_mod4[0] == 0 and mass_g_mod4[3] == 0
    and mass_g_mod4[1] > 0 and mass_g_mod4[2] > 0,
)

f8 = np.roll(
    np.convolve(eta_pass(2, 4, 300), eta_pass(4, 4, 300))[:301].astype(
        np.int64), 1)
f8[0] = 0
a_f8 = [int(f8[n]) for n in range(301)]
check(
    "S0.f8: eta(2t)^4 eta(4t)^4 head a_p = {3:-4,5:-2,7:24,11:-44,13:22}",
    a_f8[1] == 1 and all(a_f8[p] == v for p, v in HEAD_AP.items()),
)

mu = mobius_sieve(QMAX)
live_all = [
    d for d in range(1, QMAX + 1, 2)
    if d % 8 == 1 and abs(int(mu[d])) == 1 and int(g[d]) != 0
]
live = [d for d in live_all if d <= D_FAM]
bs = {d: int(g[d]) for d in live_all}
ts = {d: int(Th[d]) for d in live_all}
info(f"live fund d≡1 mod 8, b≠0: ≤{D_FAM}: {len(live)}; "
     f"≤{QMAX}: {len(live_all)}")
check(
    f"S0.family: #{len(live)} live fundamental d ≤ {D_FAM} "
    f"(contract window ≥ 8000; need ≥ 200 live d)",
    D_FAM >= 8000 and len(live) >= 200,
)

parity_ok = bool(np.all((Th - g) % 2 == 0))
Npl = (Th + g) // 2
Nmi = (Th - g) // 2
check(
    f"S0.Npm: N± = (Θ±g)/2 integral and ≥ 0 for ALL n ≤ {QMAX} "
    "(T68 polarisation re-verified, not assumed)",
    parity_ok and bool(np.all(Npl >= 0)) and bool(np.all(Nmi >= 0)),
)


# ================================================================ M1
print("=" * 72)
print("M1 -- THE MIXED CHANNEL C = Θ·g = N₊² − N₋² (Rankin 1939)")
print("=" * 72)

# (i) per-n exact identity + sign structure
C_arr = Th.astype(object) * g.astype(object)
D_arr = Npl.astype(object) ** 2 - Nmi.astype(object) ** 2
mixed_exact = bool((C_arr == D_arr).all())
check(
    f"M1.i.a: C(n) = Θ(n)·g(n) = N₊(n)² − N₋(n)² exact as integer "
    f"identity for ALL n ≤ {QMAX} (difference of squares of the two "
    "positive populations)",
    mixed_exact,
)

th_pos = all(ts[d] > 0 for d in live)
sign_match = all((ts[d] * bs[d] > 0) == (bs[d] > 0) for d in live)
n_pos = sum(1 for d in live if bs[d] > 0)
n_neg = len(live) - n_pos
info(f"sign split on live d ≤ {D_FAM}: C>0: {n_pos}, C<0: {n_neg} "
     f"({n_pos / len(live):.4f} / {n_neg / len(live):.4f})")
check(
    "M1.i.b: Θ_d > 0 on all live d and sign(C(d)) = sign(b(d)) — the "
    f"mixed channel is the SIGNED family with population weighting "
    f"(+{n_pos}/−{n_neg}; both signs present, NOT PSD)",
    th_pos and sign_match and n_pos > 0 and n_neg > 0,
)

# (ii) exact towers of the mixed channel + bilinear combination identities
tower_ok = True
comb_ok = True
n_t1 = n_t2 = 0
slope_pts = []
for d in live:
    C_d = ts[d] * bs[d]
    for p in HECKE_PS:
        if d % p == 0:
            continue
        chi = kronecker(d, p)
        a_p = HEAD_AP[p]
        s3 = 1 + p ** 3
        al1 = a_p - chi * p
        be1 = s3 - chi * p
        if d * p * p <= QMAX:
            n_t1 += 1
            n1 = d * p * p
            C1 = int(Th[n1]) * int(g[n1])
            if C1 != al1 * be1 * C_d:
                tower_ok = False
            # five-channel bilinear combination identities per tower point
            if 2 * int(Npl[n1]) != be1 * ts[d] + al1 * bs[d]:
                comb_ok = False
            if 2 * int(Nmi[n1]) != be1 * ts[d] - al1 * bs[d]:
                comb_ok = False
            if 4 * int(Npl[n1]) * int(Nmi[n1]) != (
                    be1 * be1 * ts[d] ** 2 - al1 * al1 * bs[d] ** 2):
                comb_ok = False
            if C_d != 0 and C1 != 0:
                slope_pts.append((math.log(p), math.log(abs(C1 / C_d))))
        if d * p ** 4 <= QMAX:
            n_t2 += 1
            n2 = d * p ** 4
            al2 = a_p * al1 - p ** 3
            be2 = s3 * be1 - p ** 3
            if int(Th[n2]) * int(g[n2]) != al2 * be2 * C_d:
                tower_ok = False
info(f"towers: k=1 pairs={n_t1}, k=2 pairs={n_t2}")
check(
    "M1.ii.a: exact mixed towers on all live (d,p) pairs — "
    "C(dp²) = (σ₃(p)−χp)(a_p−χp)·C(d) and the k=2 recurrence "
    f"(α₂β₂, both from T68 single towers), integer-exact "
    f"({n_t1} k=1 + {n_t2} k=2 checks)",
    tower_ok and n_t1 >= 300 and n_t2 >= 40,
)
check(
    "M1.ii.b: bilinear-combination identities exact per tower point — "
    "2N₊(dp²) = β₁Θ_d + α₁g_d, 2N₋(dp²) = β₁Θ_d − α₁g_d, "
    "4N₊N₋(dp²) = β₁²Θ_d² − α₁²g_d² (the N±²/N₊N₋ channels ARE "
    "combinations of the three basic bilinear towers)",
    comb_ok,
)

# (ii.c) ALGEBRAIC square-level Euler factor of the mixed channel
X_s, A_s, P_s, CHI_s = sp.symbols("X a p chi")
al_sym = [sp.Integer(1), A_s - CHI_s * P_s]
be_sym = [sp.Integer(1), (1 + P_s ** 3) - CHI_s * P_s]
for _k in range(2, K_SER + 1):
    al_sym.append(sp.expand(A_s * al_sym[-1] - P_s ** 3 * al_sym[-2]))
    be_sym.append(sp.expand((1 + P_s ** 3) * be_sym[-1]
                            - P_s ** 3 * be_sym[-2]))
S_mix = sum(sp.expand(al_sym[k] * be_sym[k]) * X_s ** k
            for k in range(K_SER + 1))
D_mix = sp.expand((1 - A_s * X_s + P_s ** 3 * X_s ** 2)
                  * (1 - A_s * P_s ** 3 * X_s + P_s ** 9 * X_s ** 2))
R_mix = sp.expand(S_mix * D_mix)
tail_ok = all(sp.simplify(R_mix.coeff(X_s, k)) == 0
              for k in range(5, K_SER + 1))
N_mix = sum(sp.expand(R_mix.coeff(X_s, k)) * X_s ** k for k in range(5))
degN = sp.degree(sp.Poly(N_mix, X_s))
N_mix0 = sp.expand(N_mix.subs(CHI_s, 0))
num0_ok = sp.expand(N_mix0 - (1 - P_s ** 6 * X_s ** 2)) == 0
shift_ok = sp.expand(
    (1 - A_s * X_s + P_s ** 3 * X_s ** 2).subs(X_s, P_s ** 3 * X_s)
    - (1 - A_s * P_s ** 3 * X_s + P_s ** 9 * X_s ** 2)
) == 0
info("mixed-channel local factor (sympy exact):")
info(f"  Σ_k α_kβ_k X^k = N_mix / D_mix,  deg N_mix = {degN}")
info(f"  N_mix (χ generic) = {sp.factor(N_mix)}")
info("  χ=0:  N_mix = 1 − p⁶X² = 1/ζ_p(2w−6)")
info("  D_mix = (1−a_pX+p³X²)(1−a_pp³X+p⁹X²) "
     "= L_p(f₈,w)⁻¹·L_p(f₈,w−3)⁻¹")
info("  ⇒ C-channel (χ=0) = L_p(f₈,w)·L_p(f₈,w−3)/ζ_p(2w−6)")
info("  = Rankin f₈×Eisenstein (Rankin 1939 original method, classical)")
info("  — pure L_p(f₈,·)-shifts; the RS ζ(2·)-division is PRESENT.")
check(
    "M1.ii.c: mixed-channel Euler factor identified EXACTLY (sympy): "
    f"S·D_mix polynomial (tail k=5..{K_SER} vanishes, χ generic), "
    f"deg N_mix = {degN} ≤ 4; N_mix(χ=0) = 1−p⁶X²; "
    "D_mix = L_p(f₈,w)⁻¹L_p(f₈,w−3)⁻¹ (shift identity exact) — "
    "Rankin f₈×Eisenstein with RS ζ(2w−6)-division (classical)",
    tail_ok and degN <= 4 and num0_ok and shift_ok,
)

# (iii) THE WEIGHT QUESTION: p^{3k}-layer weights of the five channels
Q_s = sp.symbols("q", positive=True)
AH = sp.symbols("ahat")


def newton_pows(e1, e2, kmax):
    """Power sums r1^k + r2^k for the quadratic 1 - e1 X + e2 X^2."""
    P = [sp.Integer(2), sp.expand(e1)]
    for _ in range(2, kmax + 1):
        P.append(sp.expand(e1 * P[-1] - e2 * P[-2]))
    return P


def est_poly(expr):
    """E_ST of a polynomial in ahat (Catalan moments, classical)."""
    e = sp.expand(expr)
    if not e.has(AH):
        return sp.nsimplify(e)
    poly = sp.Poly(e, AH)
    tot = sp.Integer(0)
    for (m,), c in poly.as_dict().items():
        if m % 2 == 0:
            tot += c * sp.catalan(m // 2)
    return sp.simplify(tot)


PA = newton_pows(A_s, P_s ** 3, K_MAX)              # f8 at w
PB = newton_pows(A_s * P_s ** 3, P_s ** 9, K_MAX)   # f8 at w-3
PS2 = newton_pows(A_s ** 2 - 2 * P_s ** 3, P_s ** 6, K_MAX)  # (γ²,γ̄²)


def kill_term(k):
    return 2 * P_s ** (3 * k) if k % 2 == 0 else sp.Integer(0)


lam_ch = {"mixed": [], "b2": [], "th2": [], "vsqE": [], "vsqf": []}
for k in range(1, K_MAX + 1):
    lam_ch["mixed"].append(sp.expand(PA[k] + PB[k] - kill_term(k)))
    lam_ch["b2"].append(sp.expand(PS2[k] + 2 * P_s ** (3 * k)
                                  - kill_term(k)))
    lam_ch["th2"].append(sp.expand(1 + 2 * P_s ** (3 * k)
                                   + P_s ** (6 * k) - kill_term(k)))
    lam_ch["vsqE"].append(sp.expand(2 + 2 * P_s ** (3 * k)))
    lam_ch["vsqf"].append(sp.expand(2 * PA[k]))

# guard: Newton assembly vs direct log-derivative series (numeric-rational)
p_num, a_num = sp.Integer(5), sp.Integer(-2)
F_num = ((1 - p_num ** 6 * X_s ** 2)
         / ((1 - a_num * X_s + p_num ** 3 * X_s ** 2)
            * (1 - a_num * p_num ** 3 * X_s + p_num ** 9 * X_s ** 2)))
L_num = sp.series(X_s * sp.diff(sp.log(F_num), X_s), X_s, 0,
                  K_MAX + 1).removeO()
guard_ok = all(
    sp.simplify(L_num.coeff(X_s, k)
                - lam_ch["mixed"][k - 1].subs({A_s: a_num, P_s: p_num})) == 0
    for k in range(1, K_MAX + 1)
)

layers = {}
for ch, lams in lam_ch.items():
    row = []
    for k in range(1, K_MAX + 1):
        e = sp.expand(lams[k - 1].subs({A_s: AH * Q_s ** 3,
                                        P_s: Q_s ** 2}))
        row.append(est_poly(e.coeff(Q_s, 6 * k)))
    layers[ch] = row

fam_target = [1 if k == 1 else (2 if k % 2 == 1 else 0)
              for k in range(1, K_MAX + 1)]
floor_target = [2 if k % 2 == 1 else 0 for k in range(1, K_MAX + 1)]
full_target = [2] * K_MAX
mixed_target = [0 if k % 2 == 1 else -2 for k in range(1, K_MAX + 1)]
info("p^{3k}-layer weights (E_ST ∘ [q^{6k}], layer machinery T61/T68):")
info(f"  b²   (family core)   = {layers['b2']}   (T61/T63 [1,0,2,0,…])")
info(f"  Θ²   (Eisen. floor)  = {layers['th2']}   (T68 [2,0,2,0,…])")
info(f"  Θ·g  (MIXED, new)    = {layers['mixed']}")
info(f"  vsq_Θ (value square) = {layers['vsqE']}   (full [2,2,2,2,…])")
info(f"  vsq_g (value square) = {layers['vsqf']}   (no p^{{3k}} content)")
check(
    "M1.iii.a: layer machinery cross-validates T61/T63/T68 — "
    f"b²-channel layers = family core {fam_target[:4]}…, Θ²-channel "
    f"layers = floor {floor_target[:4]}… (sympy exact; Newton-assembly "
    f"guard vs direct log-derivative series: {guard_ok})",
    layers["b2"] == fam_target and layers["th2"] == floor_target
    and guard_ok,
)
mixed_layer_ok = layers["mixed"] == mixed_target
no_full = layers["mixed"] != full_target
no_positive_even = all(layers["mixed"][k] <= 0 for k in range(1, K_MAX, 2))
check(
    "M1.iii.b: THE WEIGHT ANSWER (decided by machine) — the mixed "
    f"channel carries {layers['mixed'][:4]}… : NEITHER full [2,2,2,2] "
    "NOR the PSD deletion pattern [·,0,·,0] — it carries the deletion "
    "term ISOLATED WITH MINUS ([0,−2,0,−2…] = pure 1/ζ_p(2w−6) layer; "
    "no population at the p^{3k}-layer at all).  The non-PSD freedom "
    "buys a NEGATIVE isolated deletion, not un-deleted weights",
    mixed_layer_ok and no_full and no_positive_even,
)

# leading scale of the mixed channel: p^{9k/2} Chebyshev
lead_ok = True
lead_est = []
for k in range(1, K_MAX + 1):
    e = sp.expand(lam_ch["mixed"][k - 1].subs({A_s: AH * Q_s ** 3,
                                               P_s: Q_s ** 2}))
    lead = e.coeff(Q_s, 9 * k)
    if sp.expand(lead - 2 * sp.chebyshevt(k, AH / 2)) != 0:
        lead_ok = False
    lead_est.append(est_poly(lead))
slope = float(np.polyfit([x for x, _ in slope_pts],
                         [y for _, y in slope_pts], 1)[0])
info(f"leading scale: λ_k/p^{{9k/2}} = 2cos(kθ) exactly; "
     f"E_ST = {lead_est}")
info(f"measured tower scaling (log|C(dp²)/C(d)| vs log p, "
     f"{len(slope_pts)} pts): slope = {slope:.3f} (algebraic 9/2)")
check(
    "M1.iii.c: mixed channel lives at the population×coherence scale "
    f"p^{{9k/2}} with Chebyshev weights 2cos(kθ) (sympy exact); "
    f"E_ST = {lead_est[:4]}… = [0,−1,0,0…] (no ζ-kernel at k=1); "
    f"measured slope {slope:.2f} ≈ 4.5 (±0.6)",
    lead_ok and lead_est == [0, -1] + [0] * (K_MAX - 2)
    and abs(slope - 4.5) < 0.6 and len(slope_pts) >= 300,
)


# ================================================================ M2
print("=" * 72)
print("M2 -- SIEVE READING: deletion = square sieve = ζ(2·)-division")
print("=" * 72)

# (i) Cauchy–Littlewood / RS local convolution lemma, FREE Satake symbols
s_s, t_s, u_s, v_s = sp.symbols("s t u v")
hs = [sp.Integer(1), s_s + t_s]
hu = [sp.Integer(1), u_s + v_s]
for _k in range(2, 11):
    hs.append(sp.expand((s_s + t_s) * hs[-1] - s_s * t_s * hs[-2]))
    hu.append(sp.expand((u_s + v_s) * hu[-1] - u_s * v_s * hu[-2]))
S_lem = sum(sp.expand(hs[k] * hu[k]) * X_s ** k for k in range(11))
Den_lem = sp.expand((1 - s_s * u_s * X_s) * (1 - s_s * v_s * X_s)
                    * (1 - t_s * u_s * X_s) * (1 - t_s * v_s * X_s))
Num_lem = 1 - s_s * t_s * u_s * v_s * X_s ** 2
R_lem = sp.expand(S_lem * Den_lem - Num_lem)
lemma_ok = all(sp.expand(R_lem.coeff(X_s, k)) == 0 for k in range(11))
check(
    "M2.i: Cauchy–Littlewood / Rankin–Selberg local convolution lemma "
    "(classical) — Σ h_k(s,t)h_k(u,v)X^k = (1−stuvX²)/"
    "[(1−suX)(1−svX)(1−tuX)(1−tvX)] exact for k ≤ 10, FREE Satake "
    "symbols (sympy)",
    lemma_ok,
)

# (ii) determinant instantiation: st = uv = p^3
num_det = sp.simplify(Num_lem.subs({t_s: P_s ** 3 / s_s,
                                    v_s: P_s ** 3 / u_s}))
det_ok = sp.simplify(num_det - (1 - P_s ** 6 * X_s ** 2)) == 0
info("determinant instantiation st = uv = p³:")
info("  numerator = 1 − p⁶X² = 1/ζ_p(2w−6) — INDEPENDENT of the pair")
info("  ⇒ EVERY coefficient-bilinear channel of two determinant-p³")
info("  towers inherits the RS ζ(2w−6)-division (PSD or not).")
check(
    "M2.ii.a: st = uv = p³ ⇒ lemma numerator = 1−p⁶X² independent of "
    "the Satake pair — the deletion factor is a DETERMINANT-ONLY "
    "invariant of coefficient squaring (RS normalisation, classical)",
    det_ok,
)

# instantiations reproduce the known closed forms
closed_ff = ((1 - P_s ** 6 * X_s ** 2)
             / ((1 - (A_s ** 2 - 2 * P_s ** 3) * X_s + P_s ** 6 * X_s ** 2)
                * (1 - P_s ** 3 * X_s) ** 2))
E57_chi0 = ((1 + P_s ** 3 * X_s)
            / ((1 - (A_s ** 2 - 2 * P_s ** 3) * X_s + P_s ** 6 * X_s ** 2)
               * (1 - P_s ** 3 * X_s)))
ff_ok = sp.simplify(closed_ff - E57_chi0) == 0
closed_EE = ((1 - P_s ** 6 * X_s ** 2)
             / ((1 - X_s) * (1 - P_s ** 3 * X_s) ** 2
                * (1 - P_s ** 6 * X_s)))
floor_T68 = ((1 / (1 - X_s)) * (1 / (1 - P_s ** 3 * X_s)) ** 2
             * (1 / (1 - P_s ** 6 * X_s)) * (1 - P_s ** 6 * X_s ** 2))
EE_ok = sp.simplify(closed_EE - floor_T68) == 0
closed_fE = ((1 - P_s ** 6 * X_s ** 2)
             / ((1 - A_s * X_s + P_s ** 3 * X_s ** 2)
                * (1 - A_s * P_s ** 3 * X_s + P_s ** 9 * X_s ** 2)))
fE_ok = sp.simplify(closed_fE - N_mix0 / D_mix) == 0
check(
    "M2.ii.b: lemma instantiations reproduce the known closed forms — "
    "(f₈,f₈) = T57 χ=0 b²-Euler; (E,E) = T58-X4 Eisenstein floor (T68); "
    "(f₈,E) = the M1 mixed factor (three sympy equalities exact)",
    ff_ok and EE_ok and fE_ok,
)
check(
    "M2.ii.c: FIVE CHANNELS DECLINED — b², Θ², Θ·g are lemma "
    "instantiations with numerator 1−p⁶X²; N₊², N₋², N₊N₋ are fixed "
    "bilinear combinations of these three (verified integer-exact per "
    "tower point in M1.ii.b) ⇒ the common factor 1−p⁶X² distributes: "
    "ALL FIVE compiler square-channels inherit the 1/ζ_p(2w−6) deletion",
    lemma_ok and det_ok and ff_ok and EE_ok and fE_ok and comb_ok,
)

# (iii) the square sieve identification
Y_s = sp.symbols("Y", positive=True)
full_gen = 2 * Y_s / (1 - Y_s)                 # λ of ζ_p(u)²
ratio_gen = 2 * Y_s / (1 - Y_s ** 2)           # λ of ζ_p(u)²/ζ_p(2u)
flat_gen = 2 * Y_s ** 2 / (1 - Y_s ** 2)       # λ of ζ_p(2u)
sieve_gen_ok = sp.simplify(full_gen - ratio_gen - flat_gen) == 0
flat_series = sp.series(flat_gen, Y_s, 0, K_MAX + 1).removeO()
flat_w = [int(flat_series.coeff(Y_s, k)) for k in range(1, K_MAX + 1)]
check(
    "M2.iii.a: weight algebra (sympy exact) — full [2,2,2,2] − ratio "
    f"[2,0,2,0] = {flat_w[:4]}… = λ-weights of ζ_p(2u): the even-k "
    "deletion IS the ζ(2u)-division (classical RS denominator of "
    "coefficient squaring)",
    sieve_gen_ok and flat_w == [0 if k % 2 == 1 else 2
                                for k in range(1, K_MAX + 1)],
)

# global Möbius square sieve, coefficient-exact
om = np.zeros(N_SIEVE + 1, dtype=np.int64)
dcnt = np.zeros(N_SIEVE + 1, dtype=np.int64)
for p in sp.primerange(2, N_SIEVE + 1):
    om[int(p)::int(p)] += 1
for a_i in range(1, N_SIEVE + 1):
    dcnt[a_i::a_i] += 1
mu_s = mobius_sieve(int(math.isqrt(N_SIEVE)) + 1)
sieve_fwd = True
sieve_bwd = True
for n in range(1, N_SIEVE + 1):
    acc_f = 0
    acc_b = 0
    r = 1
    while r * r <= n:
        if n % (r * r) == 0:
            acc_f += int(mu_s[r]) * int(dcnt[n // (r * r)])
            acc_b += 2 ** int(om[n // (r * r)])
        r += 1
    if acc_f != 2 ** int(om[n]):
        sieve_fwd = False
    if acc_b != int(dcnt[n]):
        sieve_bwd = False
check(
    f"M2.iii.b: SQUARE SIEVE global, coefficient-exact n ≤ {N_SIEVE} — "
    "2^ω(n) = Σ_{r²|n} μ(r)·d(n/r²) (Möbius square sieve = ζ(2u)-"
    "division) and d(n) = Σ_{r²|n} 2^{ω(n/r²)} (completion direction); "
    "the deleted core 2^ω and the full object d(n) are an EXACT "
    "inclusion–exclusion pair over square classes",
    sieve_fwd and sieve_bwd,
)


# ================================================================ M3a
print("=" * 72)
print("M3a -- COMPLETION I: the Dirichlet-convolution (value) square")
print("=" * 72)

vsq_full = layers["vsqE"] == full_target
restore = [layers["vsqE"][k] - layers["th2"][k] for k in range(K_MAX)]
restore_ok = restore == [0 if k % 2 == 1 else 2
                         for k in range(1, K_MAX + 1)]
vsqf_zero = layers["vsqf"] == [0] * K_MAX
info("value square (Dirichlet convolution square, χ=0):")
info(f"  Θ-side  ζ_p(w)²ζ_p(w−3)²: layers = {layers['vsqE']} — FULL")
info(f"  restoration vsq − Θ²-channel = {restore} = +ζ_p(2w−6) layer")
info(f"  g-side  L_p(f₈,w)²: layers = {layers['vsqf']} (scale p^{{3k/2}},")
info("  no p^{3k} content — the cusp value-square cannot carry [2,2,2,2])")
check(
    "M3a.i: the Θ-side VALUE square carries FULL [2,2,2,2] weights by "
    "construction (values squared, no coefficient squaring ⇒ no RS "
    "division); difference to the coefficient-square channel = exactly "
    "the ζ_p(2w−6)-restoration [0,2,0,2…]; the g-side value square has "
    "NO p^{3k}-layer content (sympy exact)",
    vsq_full and restore_ok and vsqf_zero,
)

# pair carrier on live data: double-tower sums = convolution square
pair_ds = [d for d in live if d <= 45][:3]
pair_checks = 0
pair_ok = True
formula_ok = True
for d in pair_ds:
    nmax_d = int(math.isqrt(QMAX // d))
    for m in range(1, nmax_d + 1, 2):
        if math.gcd(m, d) != 1:
            continue
        if int(Th[d * m * m]) != ts[d] * alphaE_sharp(d, m):
            formula_ok = False
        if int(g[d * m * m]) != bs[d] * alpha_sharp(d, m, a_f8):
            formula_ok = False
    for n in range(1, min(nmax_d, 45) + 1, 2):
        if math.gcd(n, d) != 1:
            continue
        divs = [int(x) for x in sp.divisors(n)]
        lhs_T = sum(int(Th[d * m1 * m1]) * int(Th[d * (n // m1) ** 2])
                    for m1 in divs)
        rhs_T = ts[d] ** 2 * sum(
            alphaE_sharp(d, m1) * alphaE_sharp(d, n // m1) for m1 in divs)
        lhs_g = sum(int(g[d * m1 * m1]) * int(g[d * (n // m1) ** 2])
                    for m1 in divs)
        rhs_g = bs[d] ** 2 * sum(
            alpha_sharp(d, m1, a_f8) * alpha_sharp(d, n // m1, a_f8)
            for m1 in divs)
        pair_checks += 1
        if lhs_T != rhs_T or lhs_g != rhs_g:
            pair_ok = False
info(f"pair-carrier checks on d ∈ {pair_ds}: {pair_checks} convolution "
     "points, Θ-side and g-side")
check(
    "M3a.ii: the PAIR OBJECT exists in compiler data — "
    "Σ_{m₁m₂=n} Θ(dm₁²)Θ(dm₂²) = Θ(d)²·(α_E∗α_E)(n) and the b-analog, "
    f"integer-exact on {pair_checks} points over {len(pair_ds)} live d "
    "(≥ 30); tower divisor-sum formulas (Shimura cusp side T50/T67 AND "
    "the σ₃ Eisenstein analog) verified against the raw series",
    pair_ok and formula_ok and pair_checks >= 30 and len(pair_ds) >= 2,
)

# Hankel decision: no degree-2 (compiler-tower) carrier
G_vsq = 1 / ((1 - X_s) ** 2 * (1 - P_s ** 3 * X_s) ** 2)
ser_vsq = sp.series(G_vsq, X_s, 0, 10).removeO()
c_vsq = [sp.expand(ser_vsq.coeff(X_s, k)) for k in range(9)]
H3 = sp.simplify(sp.Matrix(3, 3, lambda i, j: c_vsq[i + j + 1]).det())
H5 = sp.simplify(sp.Matrix(5, 5, lambda i, j: c_vsq[i + j]).det())
H3_at3 = H3.subs(P_s, 3)
info(f"Hankel: H3 (order-2 test) = {sp.factor(H3)}  (at p=3: {H3_at3})")
info(f"        H5 (order-4 test) = {H5}")
info("T57 Z(s,w) machinery (infinite_rtf_packing, read): inner tower is")
info("  T_d(w) = Σ_m α♯(m)² m^{-w} — the DIAGONAL coefficient square;")
info("  the value square needs the full (m₁,m₂) off-diagonal sum ⇒ the")
info("  pair channel is NOT contained in Z(s,w) — it is a FORMAL")
info("  PRODUCT (isobaric sum / Eisenstein-induced degree 4, Langlands")
info("  naming classical), with NO single-modular-form coefficient")
info("  carrier in the compiler's degree-2 tower space.")
check(
    "M3a.iii: carrier typing decided — convolution-square coefficients "
    "satisfy NO order-2 recurrence (Hankel H3 ≠ 0 symbolically and at "
    "p=3) but exactly order 4 (H5 = 0): degree-4 isobaric FORMAL "
    "PRODUCT; compiler towers are degree-2 (T50/T67/T68) and T57 "
    "Z(s,w) is diagonal-only ⇒ full weights via value-squaring have "
    "NO compiler-native single-family carrier",
    sp.simplify(H3) != 0 and H3_at3 != 0 and H5 == 0,
)


# ================================================================ M3b
print("=" * 72)
print("M3b -- COMPLETION II: Selberg-positive bookkeeping (Λ² namesake)")
print("=" * 72)

fam_w = fam_target
flat2_w = [0 if k % 2 == 1 else 2 for k in range(1, K_MAX + 1)]
delta1_w = [1] + [0] * (K_MAX - 1)
sum_w = [fam_w[k] + flat2_w[k] + delta1_w[k] for k in range(K_MAX)]
fam_gen = 2 * Y_s / (1 - Y_s ** 2) - Y_s
book_gen_ok = sp.simplify(fam_gen + flat_gen + Y_s - full_gen) == 0
info("T63 relation REARRANGED (Selberg-positive completion; PS–Rallis")
info("  doubling named classical for the ♭ term):")
info(f"  fam {fam_w} + 2♭ {flat2_w} + Plancherel δ_k1 = {sum_w}")
check(
    "M3b.i: BOOKKEEPING IDENTITY exact — family core [1,0,2,0,…] + "
    "♭ content [0,2,0,2,…] + Plancherel δ_{k1} = FULL [2,2,2,2,…] "
    "(list-exact and generating-function-exact: the minus subtracts "
    "exactly what full ζ(u)² has on the even slots)",
    sum_w == full_target and book_gen_ok,
)
slots_ok = all(
    (fam_w[k] == 0 and flat2_w[k] == full_target[k]) if (k + 1) % 2 == 0
    else (flat2_w[k] == 0 and fam_w[k] + delta1_w[k] == full_target[k])
    for k in range(K_MAX)
)
check(
    "M3b.ii: SLOT DISJOINTNESS — every even slot is carried 100% by "
    "the ♭ object, every odd slot 100% by family+Plancherel; supports "
    "are disjoint and the union fills [2,2,2,2] exactly",
    slots_ok,
)

# the ♭ object = index zeta of the square-class tower points
local_sq = sum(Y_s ** (2 * j) for j in range(7))
local_ok = all(
    sp.simplify(sp.series(1 / (1 - Y_s ** 2), Y_s, 0, 13).removeO()
                .coeff(Y_s, k) - (1 if k % 2 == 0 else 0)) == 0
    for k in range(13)
)
ind_ok = True
for m in range(1, N_SIEVE + 1, 2):
    is_sq = int(math.isqrt(m)) ** 2 == m
    x = m
    all_even = True
    for p in sp.primerange(2, int(math.isqrt(m)) + 1):
        p = int(p)
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e % 2 == 1:
            all_even = False
    if x > 1:
        all_even = False
    if is_sq != all_even:
        ind_ok = False
check(
    "M3b.iii: the ♭ object IS the square-class index zeta — locally "
    "Σ_j Y^{2j} = 1/(1−Y²) = ζ_p(2u) (series exact k ≤ 12); globally "
    "the odd-square indicator is the multiplicative family with that "
    f"local factor (coefficient-exact m ≤ {N_SIEVE}): the even-k slots "
    "are the m = r² tower indices (points d·r⁴)",
    local_ok and ind_ok,
)

# prime-side numeric identity on the T63 test class
lam_arr = np.zeros(N_LAM + 1)
pk_table = []
for p in sp.primerange(2, N_LAM + 1):
    p = int(p)
    lp = math.log(p)
    pk = p
    k = 1
    while pk <= N_LAM:
        lam_arr[pk] = lp
        pk_table.append((pk, p, k))
        pk *= p
        k += 1

TEST_FNS = []
for a in (1.5, 2.0, 2.5, 3.0, 3.5):
    TEST_FNS.append(("fejer", a, lambda u, aa=a: g_fejer(u, aa)))
for sig in (0.6, 0.8, 1.0, 1.2):
    TEST_FNS.append(("gauss", sig, lambda u, s=sig: g_gauss(u, s)))


def prime_weighted(weights, g_fn, umax):
    """2 Σ_{p,k} w_k Λ(p^k) (p^k)^{-1/2} g(k log p), zero-free."""
    s = 0.0
    for n, p, k in pk_table:
        if k > K_MAX:
            continue
        un = math.log(n)
        if un > umax + 1e-12:
            continue
        wk = weights[k - 1]
        if wk == 0:
            continue
        s += wk * lam_arr[n] * math.exp(-0.5 * un) * g_fn(un)
    return 2.0 * s


def prime_zeta(g_fn, umax):
    s = 0.0
    for n, p, k in pk_table:
        un = math.log(n)
        if un > umax + 1e-12:
            continue
        s += lam_arr[n] * math.exp(-0.5 * un) * g_fn(un)
    return 2.0 * s


def g_flat(g_fn):
    return lambda x, gf=g_fn: math.exp(-0.5 * x) * gf(2.0 * x)


ident_ok = True
bridge_ok = True
max_rel_id = 0.0
max_rel_br = 0.0
for kind, param, g_fn in TEST_FNS:
    um = float(param) if kind == "fejer" else 8.0 * float(param)
    um_b = float(param) / 2.0 + 1e-12 if kind == "fejer" else um
    lhs = prime_weighted([2] * K_MAX, g_fn, um)
    rhs = (prime_weighted(fam_w, g_fn, um)
           + prime_weighted(flat2_w, g_fn, um)
           + prime_weighted(delta1_w, g_fn, um))
    rel_id = abs(lhs - rhs) / max(abs(lhs), 1e-30)
    bl = prime_weighted(flat2_w, g_fn, um)
    br = 2.0 * prime_zeta(g_flat(g_fn), um_b)
    rel_br = abs(bl - br) / max(abs(bl), abs(br), 1e-30)
    max_rel_id = max(max_rel_id, rel_id)
    max_rel_br = max(max_rel_br, rel_br)
    if rel_id > 1e-12:
        ident_ok = False
    if rel_br > 1e-6:
        bridge_ok = False
    info(f"  [{kind},{param}]: 2Prime_ζ={lhs:.6f} "
         f"fam+2♭+Corr={rhs:.6f} relId={rel_id:.2e}; "
         f"♭-bridge rel={rel_br:.2e}")
check(
    "M3b.iv: prime-side identity numeric on the T63 test class — "
    f"2·Prime_ζ(g) = Prime_fam(g) + Prime_♭(g) + Corr_Plancherel(g) "
    f"exact on all {len(TEST_FNS)} test functions (max rel "
    f"{max_rel_id:.2e} < 1e-12); ♭ weights ↔ 2·Prime_ζ(g_♭) with "
    f"g_♭(x)=e^{{−x/2}}g(2x) (max rel {max_rel_br:.2e} < 1e-6, "
    "truncation; doubling per T63 / PS–Rallis naming)",
    ident_ok and bridge_ok and len(TEST_FNS) >= 8,
)

# populated compiler carrier: the square-class points d·r^4
sq_points = 0
sq_nonzero = 0
sq_ok = True
sq_examples = []
for r in SQ_RS:
    r4 = r ** 4
    m = r * r
    for d in live_all:
        if d * r4 > QMAX:
            break
        if d % r == 0:
            continue
        pb = bs[d] * alpha_sharp(d, m, a_f8)
        pt = ts[d] * alphaE_sharp(d, m)
        if int(g[d * r4]) != pb or int(Th[d * r4]) != pt:
            sq_ok = False
        sq_points += 1
        if pb != 0:
            sq_nonzero += 1
        if len(sq_examples) < 3:
            sq_examples.append((d, r, int(g[d * r4]), int(Th[d * r4])))
info(f"square-class points d·r⁴ ≤ {QMAX}, r ∈ {SQ_RS}: {sq_points} "
     f"points, {sq_nonzero} with b ≠ 0")
for d, r, bv, tv in sq_examples:
    info(f"  example: d={d}, r={r}: b({d}·{r}⁴)={bv}, Θ={tv}")
check(
    "M3b.v: the square-class carrier is POPULATED and tower-exact — "
    f"{sq_points} points d·r⁴ on the window ({sq_nonzero} with b ≠ 0; "
    "≥ 25), all satisfy b(dr⁴) = b(d)·α♯(r²) and "
    "Θ(dr⁴) = Θ(d)·α_E♯(r²) integer-exact (T50 tower structure)",
    sq_ok and sq_points >= 25 and sq_nonzero >= 20,
)

check(
    "M3b.vi: HONEST TYPING — the resolution is INDEX/BOOKKEEPING level: "
    "the ♭ content = counting zeta of the square-class tower indices "
    "(positive by construction, populated, M3b.iii+v), and the minus = "
    "inclusion–exclusion between the fundamental family (2^ω side) and "
    "the square-class completion (d(n) side, M2.iii.b).  It is NOT a "
    "positive operator completion of the b²-weighted form: the "
    "b²-weighted square-class channel is itself a bilinear channel and "
    "re-deletes by the M2 determinant lemma (universality applies)",
    sieve_fwd and sieve_bwd and sq_ok and det_ok and lemma_ok,
)


# ================================================================ M4
print("=" * 72)
print("M4 -- SYNTHESIS: the universality question + final map")
print("=" * 72)

full_weight_carrier = (
    (not no_positive_even)                       # mixed channel un-deleted?
    or (sp.simplify(H3) == 0)                    # single-tower value square?
)
deletion_universal = (lemma_ok and det_ok and ff_ok and EE_ok and fE_ok
                      and comb_ok and mixed_layer_ok)
tower_resolution = (sum_w == full_target and book_gen_ok and slots_ok
                    and local_ok and ind_ok and sieve_fwd and sieve_bwd
                    and sq_ok and ident_ok)

info("FINAL POLARISATION MAP (all entries machine-checked above):")
info("  (i)   MIXED CHANNEL Θ·g: Rankin f₈×Eisenstein "
     "L_p(f₈,w)L_p(f₈,w−3)/ζ_p(2w−6); layers [0,−2,0,−2…] — the")
info("        deletion isolated WITH MINUS; no full weights; the only")
info("        signed compiler channel, population×coherence scale 9k/2.")
info("  (ii)  VALUE SQUARE: full [2,2,2,2] per construction, but the")
info("        carrier is a degree-4 FORMAL PRODUCT (pair/double-tower)")
info("        — no compiler-native single family (Hankel decision).")
info("  (iii) TOWER DOUBLE-COUNTING: fam + 2♭ + δ_k1 = full, with the")
info("        ♭ slots carried EXACTLY by the square-class tower indices")
info("        (d·r⁴) — the minus resolved as inclusion–exclusion")
info("        (bookkeeping), positive at INDEX level only.")
info("  ⇒ NO compiler-native square channel escapes the ζ(2·)-division:")
info("    the deletion is a determinant-only invariant of coefficient")
info("    bilinearity (M2 lemma) — PSD-ness is irrelevant to it.")
check(
    "M4.i: polarisation map issued — three routes decided "
    f"(full_weight_carrier={full_weight_carrier}, "
    f"deletion_universal={deletion_universal}, "
    f"tower_resolution={tower_resolution})",
    deletion_universal and tower_resolution,
)

verdict_parts = []
if full_weight_carrier:
    verdict_parts.append("FULL-WEIGHT-CARRIER")
if deletion_universal:
    verdict_parts.append("DELETION-UNIVERSAL")
if tower_resolution:
    verdict_parts.append("TOWER-RESOLUTION")
verdict = " + ".join(verdict_parts) if verdict_parts else "INCONCLUSIVE"
detail = (
    "The deletion (RS ζ(2·)-division) is UNIVERSAL for compiler-native "
    "square channels: the Cauchy–Littlewood lemma makes 1−p⁶X² a "
    "determinant-only invariant of coefficient bilinearity — all five "
    "channels (b², Θ², Θ·g, N₊², N₋², N₊N₋) inherit it; the non-PSD "
    "mixed channel does not escape (it carries the deletion isolated "
    "with minus, [0,−2,0,−2…]).  SIMULTANEOUSLY the minus is RESOLVED "
    "as bookkeeping: fam + 2♭ + Plancherel = full [2,2,2,2] with the "
    "♭ slots carried exactly by the square-class tower indices d·r⁴ "
    "(inclusion–exclusion 2^ω ↔ d(n), populated carrier) — the minus "
    "subtracts precisely the square-class double counting; but this "
    "positivity lives at INDEX level, not as a b²-weighted operator "
    "completion (which re-deletes).  Full weights exist only as the "
    "VALUE square — a degree-4 formal product without a single "
    "compiler carrier.  ⇒ On the square level the minus is a "
    "theorem-like invariant; the amplitude route (T67 Dirac, "
    "non-quadratic pairing) is the only remaining full-weight path."
)
info(f"VERDICT: {verdict}")
info(detail)
check(
    f"M4.ii: verdict {verdict} assigned from computed flags "
    "(preregistered enum; combination named precisely)",
    verdict == "DELETION-UNIVERSAL + TOWER-RESOLUTION"
    or (full_weight_carrier and "FULL-WEIGHT-CARRIER" in verdict),
)

info("CONSEQUENCE for the polarisation question (typed, not executed):")
info("  the square plane is CLOSED: every compiler bilinear pairing")
info("  deletes, and the deletion is now understood twice over —")
info("  as the universal RS determinant invariant AND as square-class")
info("  inclusion–exclusion.  The open lever is EXACTLY the T67 one:")
info("  a non-quadratic (amplitude-level / Dirac) pairing whose square")
info("  reproduces the family with the ♭ term ON THE PLUS SIDE —")
info("  the mixed channel contributes the new structural datum that")
info("  sign freedom alone does NOT unlock full weights.  Sandbox only.")
check(
    "M4.iii: no promotion executed; sandbox mapping only; next lever "
    "typed (amplitude route remains the unique full-weight path)",
    True,
)


# ================================================================ end
print("=" * 72)
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print(f"VERDICT: {verdict}")
print(f"M1: C=Θ·g exact (n≤{QMAX}); towers {n_t1}+{n_t2} exact; "
      f"Euler = L_p(f₈,w)L_p(f₈,w−3)/ζ_p(2w−6); layers {layers['mixed'][:4]}")
print(f"M2: CL-lemma exact; det-p³ ⇒ 1−p⁶X² universal; 5 channels "
      f"declined; square sieve exact n≤{N_SIEVE}")
print(f"M3a: value-square layers {layers['vsqE'][:4]} full; pair carrier "
      f"{pair_checks} pts exact; Hankel H3≠0/H5=0 ⇒ formal product")
print(f"M3b: fam+2♭+δ=[2,2,2,2] exact; ♭=square-class indices; "
      f"{sq_points} points d·r⁴ tower-exact ({sq_nonzero} live)")
print(f"FILE: {__file__}")
raise SystemExit(0 if FAIL == 0 else 1)
