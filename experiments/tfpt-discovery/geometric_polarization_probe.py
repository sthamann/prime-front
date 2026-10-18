"""Discovery probe (2026-07-25), part 68 — contract GEOMETRIC.POLARIZATION.

Attack on the polarisation question left open by T67 (AMPLITUDE.DIRAC.SQRT):
the amplitude phase has a GEOMETRIC origin.  By T53/R3 (promoted v538),
b(n) is the signed count of the quinary form
    n = (x²+y²)/2 + 2z² + u² + 2w²   (x,y odd; z,u,w ∈ Z)
with sign (−1)^{|u|+|w|} — a CHARACTER ON THE LATTICE, coming from the
θ₄(q) (u-slot) and θ₄(q²) (w-slot) factors of the theta monomial
    g = θ₂(q²)²·θ₃(q²)·θ₄(q)·θ₄(q²)      (v537 witness key).
This yields a canonical, compiler-native polarisation
    b = N₊ − N₋,   N± = UNSIGNED counts of the even/odd (u+w) class,
    Θ = N₊ + N₋   (unsigned theta series, weight 5/2, positive),
with the central structure equation (per coefficient, exact integers)
    b² = Θ² − 4·N₊N₋.
The family is the DIFFERENCE OF TWO POSITIVE FAMILIES — the minus is made
geometrically explicit.  Question: does the ζ-kernel sit WITH PLUS in the
Θ²-family, and does the cross family 4N₊N₋ carry the doubling/♭ part?
(Gupta–Bleuler ANALOGY, name only: Θ = "populations", g = "coherence".)

S0  ZERO-FIREWALL (AST) + exact integer rebuild of g, Θ (sparse theta
    convolution, no FFT rounding); U4 fence; live family window.
G1  THE POLARISATION EXACT: (i) lattice enumeration with parity split
    reproduces b = N₊−N₋ (n ≤ 2400 ⊇ contract window 300, exact);
    (ii) predicted monomial Θ = θ₂(q²)²·θ₃(q²)·θ₃(q)·θ₃(q²) equals the
    unsigned count coefficientwise (n ≤ 2400 ≥ 2000);
    (iii) N± = (Θ±g)/2 integral and ≥ 0 for ALL n ≤ QMAX;
    (iv) support/congruence analysis mod 4/8/16: 2-adic glue selection
    (difference mass lives only on n ≡ 1,2 mod 4; fundamental
    d ≡ 5 mod 8 are exactly BALANCED populations N₊ = N₋).
G2  THE CHARACTER OF THE Θ SIDE: (i) growth exponents γ_Θ vs γ_|b|
    (Eisenstein 3/2 vs Waldspurger 3/4 density); (ii) Hecke: T(p²)-
    eigenform test for Θ (preregistered guess NO — decided by machine),
    eigenvalue vs σ₃(p) = 1+p³ and vs a_p(f8); cusp component of Θ;
    exact d↦dp², dp⁴ towers for Θ and g; (iii) Θ_d/|b_d| distribution.
G3  THE THREE RANKIN CHANNELS (heart): per-n exact split
    Θ² = b² + 4N₊N₋ on the live window (≥ 3000); coherence fraction
    ladder; tower scaling exponents (p³ vs p⁶) and empirical Λ-weight
    signatures λ₁, λ₂ of the three channels; ALGEBRAIC identification
    of the Θ²-channel local factor with the T58-X4 Eisenstein floor
    ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6) (sympy exact, χ ∈ {−1,0,+1}); Dirichlet
    coefficient positivity of the floor (n ≤ 2000); the p^{3k}-layer
    weights of the floor vs the family core weights (T61/T63).
G4  WEIL BOOKKEEPING OF THE POLARISED FORMS: (i) Gram-level exact
    K_{Θ²} = K_{b²} + 4K_× on live d ⊗ odd m (and on ≥ 8 test vectors);
    (ii) Q_{Θ²} ≥ 0 and Q_× ≥ 0 (positive coefficients — PSD measured);
    (iii) zero-free prime sides: Prime_ratio − Prime_fam = Corr_Plancherel
    exact on the T63 test class; Prime_ratio = 2·Prime_ζ − 2·Prime_ζ(g_♭)
    (T63 relation re-verified) ⇒ the ♭/doubling minus is SHARED by the
    Θ²-core and the family core (coefficient level, not just values).
G5  SYNTHESIS: polarisation diagram, honest typing of the re-booking
    (Waldspurger central values stay in b²; the Θ²-side carries
    Siegel–Weil/Eisenstein arithmetic), verdict + next lever.

PREREGISTERED CRITERIA
  G1: (i)+(ii) coefficient-exact; (iii) exact on all n ≤ QMAX;
      (iv) difference mass exactly zero outside n ≡ 1,2 mod 4.
  G2: eigenform decision by exact residual; towers exact integers;
      growth separation γ_Θ − γ_b > 0.3.
  G3: per-n identity exact; Θ²-floor identity sympy-exact; floor
      Dirichlet coefficients > 0 (n ≤ 2000); λ₂-separation between
      Θ²-channel (≈1, no even kill) and b²-channel core (E_ST[Φ₂]=0).
  G4: Gram decomposition rel < 1e-10; PSD min-eig ≥ −1e-8·scale;
      prime-side identities rel < 1e-12 (exact) / < 1e-6 (♭, truncation).
  VERDICTS (preregistered):
    POLARIZATION-SPLITS — G1–G2 exact AND the ♭/minus part sits
        ISOLATED in the positive cross channel while the Θ²-side
        carries the ζ-content plus-side (Gupta–Bleuler structure holds).
    RESHUFFLE-ONLY     — decomposition exact, but the minus structure
        travels along (no positivity gain); document precisely WHERE.
    BREAKS             — G1/G2 break (theta identification or
        positivity fails).

FENCES (honest typing):
  (i)   STRUCTURE MAPPING ONLY — no RH evidence; even on success,
        dense-class positivity is NOT established;
  (ii)  classical results named as classical: theta series of definite
        quadratic forms, Siegel–Weil / mass formula (genus Eisenstein),
        Cohen–Eisenstein series of weight 5/2, Rankin–Selberg squares,
        Shimura correspondence / T(p²), Waldspurger; Gupta–Bleuler is
        an ANALOGY NAME only (no physics claim);
  (iii) the Θ-side arithmetic is genus/Eisenstein data (class-number
        like) — it is NOT the Waldspurger central-value arithmetic;
        any re-booking between the sides is named explicitly.

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
from collections import defaultdict

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()

# ---------------------------------------------------------------- config
QMAX = 50_000                 # exact q-window for g and Theta
N_ENUM = 2_400                # lattice enumeration window (>= 2000)
D_FAM = 8_000                 # live-d family window (>= 3000 required)
D_GRAM = 3_000                # Gram-form d-window
M_GRAM = 401                  # odd m <= M_GRAM (Gram columns)
HECKE_PS = (3, 5, 7, 11, 13)
HEAD_AP = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}
G_KEY = (0, 2, 0, 1, 1, 1)    # theta2(q2)^2 theta3(q2) theta4 theta4(q2)
TH_KEY = (0, 2, 1, 2, 0, 0)   # theta4 -> theta3 in both c-slots
N_LAM = 20_000                # prime-power window for zero-free prime sides
N_FLOOR = 2_000               # Dirichlet positivity window for the floor
K_MAX = 8
COHERENCE_LADDER = (1000, 2000, 4000, 8000)


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
info("  Siegel–Weil, Cohen–Eisenstein 5/2, Rankin–Selberg, Shimura,")
info("  Waldspurger named classical; Gupta–Bleuler = analogy name only.")

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
     f"(int64, no FFT rounding)")
info(f"g  head = {list(g[:12])}")
info(f"Th head = {list(Th[:12])}")
check(
    "S0.build: monomials live on integer q-powers (t-support ≡ 0 mod 4) "
    "and g matches the v537/T38 witness head [0,4,-8,0,0,0,16,...]",
    support_ok and list(g[:7]) == [0, 4, -8, 0, 0, 0, 16],
)

ns = np.arange(QMAX + 1)
mass_g_mod4 = {r: int(np.abs(g[1:][ns[1:] % 4 == r]).sum()) for r in range(4)}
mass_t_mod4 = {r: int(Th[1:][ns[1:] % 4 == r].sum()) for r in range(4)}
info(f"|g| mass mod 4: {mass_g_mod4}")
info(f" Θ  mass mod 4: {mass_t_mod4}")
check(
    "S0.g-fence: U4 fence for g (mass only on n≡1,2 mod 4); Θ positive "
    "with mass on ALL classes mod 4 (unsigned counting sees everything)",
    mass_g_mod4[0] == 0 and mass_g_mod4[3] == 0
    and mass_g_mod4[1] > 0 and mass_g_mod4[2] > 0
    and all(mass_t_mod4[r] > 0 for r in range(4))
    and bool(np.all(Th >= 0)),
)

f8 = np.roll(
    np.convolve(eta_pass(2, 4, 300), eta_pass(4, 4, 300))[:301].astype(
        np.int64), 1)
f8[0] = 0
check(
    "S0.f8: eta(2t)^4 eta(4t)^4 head a_p = {3:-4,5:-2,7:24,11:-44,13:22}",
    int(f8[1]) == 1 and all(int(f8[p]) == v for p, v in HEAD_AP.items()),
)

mu = mobius_sieve(QMAX)
live = [
    d for d in range(1, D_FAM + 1, 2)
    if d % 8 == 1 and abs(int(mu[d])) == 1 and int(g[d]) != 0
]
live_all = [
    d for d in range(1, QMAX + 1, 2)
    if d % 8 == 1 and abs(int(mu[d])) == 1 and int(g[d]) != 0
]
bs = {d: int(g[d]) for d in live_all}
ts = {d: int(Th[d]) for d in live_all}
info(f"live fund d≡1 mod 8, b≠0: ≤{D_FAM}: {len(live)}; "
     f"≤{QMAX}: {len(live_all)}")
check(
    f"S0.family: #{len(live)} live fundamental d ≤ {D_FAM} "
    f"(window ≥ 3000 required; need ≥ 200 live d)",
    D_FAM >= 3000 and len(live) >= 200,
)


# ================================================================ G1
print("=" * 72)
print("G1 -- THE POLARISATION EXACT (b = N+ − N−, Θ = N+ + N−)")
print("=" * 72)
info("quinary form n = (x²+y²)/2 + 2z² + u² + 2w², x,y odd (T53/v538);")
info("sign (−1)^{|u|+|w|} = character on the lattice from θ₄(q)·θ₄(q²)")

t_e = time.time()
xy = np.zeros(N_ENUM + 1, dtype=np.int64)
max_o = int(math.isqrt(2 * N_ENUM)) + 2
for x in range(-max_o, max_o + 1):
    if x % 2 == 0:
        continue
    for y in range(-max_o, max_o + 1):
        if y % 2 == 0:
            continue
        m = (x * x + y * y) // 2
        if m <= N_ENUM:
            xy[m] += 1

zuw_even = np.zeros(N_ENUM + 1, dtype=np.int64)
zuw_odd = np.zeros(N_ENUM + 1, dtype=np.int64)
max_u = int(math.isqrt(N_ENUM))
for u in range(-max_u, max_u + 1):
    u2 = u * u
    if u2 > N_ENUM:
        continue
    max_w = int(math.isqrt((N_ENUM - u2) // 2))
    for w in range(-max_w, max_w + 1):
        base = u2 + 2 * w * w
        if base > N_ENUM:
            continue
        par = (abs(u) + abs(w)) % 2
        max_z = int(math.isqrt((N_ENUM - base) // 2))
        for z in range(-max_z, max_z + 1):
            idx = base + 2 * z * z
            if idx <= N_ENUM:
                if par == 0:
                    zuw_even[idx] += 1
                else:
                    zuw_odd[idx] += 1

N_plus = np.convolve(xy, zuw_even)[: N_ENUM + 1].astype(np.int64)
N_minus = np.convolve(xy, zuw_odd)[: N_ENUM + 1].astype(np.int64)
info(f"parity-split enumeration n ≤ {N_ENUM} in {time.time() - t_e:.2f}s")
info(f"N+ head = {list(N_plus[:10])}")
info(f"N− head = {list(N_minus[:10])}")

sig_ok = bool(np.array_equal(N_plus - N_minus, g[: N_ENUM + 1]))
uns_ok = bool(np.array_equal(N_plus + N_minus, Th[: N_ENUM + 1]))
check(
    f"G1.i: b(n) = N₊(n) − N₋(n) by direct lattice count, exact for all "
    f"n ≤ {N_ENUM} (⊇ contract window n ≤ 300); sign class = parity of "
    "u+w (lattice character)",
    sig_ok,
)
check(
    "G1.ii: predicted monomial Θ = θ₂(q²)²·θ₃(q²)·θ₃(q)·θ₃(q²) equals "
    f"the UNSIGNED count N₊+N₋ coefficientwise for all n ≤ {N_ENUM} "
    "(≥ 2000; θ₄→θ₃ in exactly the u,w slots)",
    uns_ok,
)
check(
    "G1.ii.b: monomial keys differ only in the θ₄→θ₃ slots "
    f"(g key {G_KEY} → Θ key {TH_KEY}; sign origin = u,w characters)",
    G_KEY == (0, 2, 0, 1, 1, 1) and TH_KEY == (0, 2, 1, 2, 0, 0)
    and G_KEY[:2] == TH_KEY[:2],
)

parity_ok = bool(np.all((Th - g) % 2 == 0))
Npl_full = (Th + g) // 2
Nmi_full = (Th - g) // 2
pos_ok = bool(np.all(Npl_full >= 0)) and bool(np.all(Nmi_full >= 0))
check(
    f"G1.iii: N± = (Θ±g)/2 are integers (Θ ≡ g mod 2) and ≥ 0 for ALL "
    f"n ≤ {QMAX} (counting positivity — verified, not assumed)",
    parity_ok and pos_ok,
)

# (iv) support / 2-adic glue selection
diff_dead = ns[1:][(ns[1:] % 4 == 0) | (ns[1:] % 4 == 3)]
balanced_ok = bool(np.all(g[diff_dead] == 0))
mod8 = {r: (int(N_plus[1:][np.arange(1, N_ENUM + 1) % 8 == r].sum()),
            int(N_minus[1:][np.arange(1, N_ENUM + 1) % 8 == r].sum()))
        for r in range(8)}
info("mod-8 masses (N₊, N₋) on n ≤ N_ENUM:")
for r in range(8):
    npv, nmv = mod8[r]
    info(f"  n≡{r} (8): N₊={npv:>9}  N₋={nmv:>9}  diff={npv - nmv:>8}")
mod16_live = sorted({
    int(r) for r in range(16)
    if int(np.abs(g[1:][ns[1:] % 16 == r]).sum()) > 0
})
info(f"mod-16 classes with difference mass: {mod16_live}")
d5_class = [d for d in range(5, QMAX + 1, 8)
            if abs(int(mu[d])) == 1]
d5_balanced = all(int(g[d]) == 0 for d in d5_class)
check(
    "G1.iv: 2-adic glue selection — difference mass EXACTLY zero on "
    "n ≡ 0,3 mod 4 (N₊ = N₋ there); live difference classes mod 16 "
    f"⊆ {{1,2,5,6,9,10,13,14}} (found {mod16_live})",
    balanced_ok and all(r % 4 in (1, 2) for r in mod16_live),
)
check(
    f"G1.iv.b: fundamental d ≡ 5 mod 8 (root number −1, v538) are "
    f"exactly BALANCED populations N₊ = N₋ ({len(d5_class)} d checked) — "
    "the ε = −1 class is coherence-free, not population-free",
    d5_balanced and len(d5_class) >= 500,
)
g1_ok = (sig_ok and uns_ok and parity_ok and pos_ok and balanced_ok
         and d5_balanced)


# ================================================================ G2
print("=" * 72)
print("G2 -- THE CHARACTER OF THE THETA SIDE")
print("=" * 72)

# (i) growth exponents
ld = np.log([float(d) for d in live])
lt = np.log([float(ts[d]) for d in live])
lb = np.log([abs(float(bs[d])) for d in live])
gam_t = float(np.polyfit(ld, lt, 1)[0])
gam_b = float(np.polyfit(ld, lb, 1)[0])
info(f"growth on {len(live)} live d ≤ {D_FAM}: "
     f"γ_Θ = {gam_t:.4f} (Eisenstein density target 3/2), "
     f"γ_|b| = {gam_b:.4f} (Waldspurger target 3/4)")
check(
    f"G2.i: growth separation γ_Θ − γ_|b| = {gam_t - gam_b:.4f} > 0.3; "
    f"γ_Θ = {gam_t:.3f} ∈ (1.3, 1.7), γ_|b| = {gam_b:.3f} ∈ (0.4, 1.1) "
    "(Eisenstein 3/2-density vs cusp 3/4-density, measured)",
    (gam_t - gam_b) > 0.3 and 1.3 < gam_t < 1.7 and 0.4 < gam_b < 1.1,
)

# (ii) Hecke: T(p^2) eigenform test (Shimura T(p^2), k=2, trivial nebentypus)
def T_p2(arr, p, n):
    """(T(p²)f)(n) = a(p²n) + (n/p)·p·a(n) + p³·a(n/p²)  (v537 formula)."""
    t = int(arr[p * p * n]) + kronecker(n, p) * p * int(arr[n])
    if n % (p * p) == 0:
        t += p ** 3 * int(arr[n // (p * p)])
    return t


eigen_ok = True
eig_rows = []
for p in HECKE_PS:
    sig3 = 1 + p ** 3
    n2 = QMAX // (p * p)
    bad_sig = 0
    max_res_ap = 0
    for n in range(1, n2 + 1):
        t = T_p2(Th, p, n)
        if t != sig3 * int(Th[n]):
            bad_sig += 1
        r_ap = abs(t - HEAD_AP[p] * int(Th[n]))
        if r_ap > max_res_ap:
            max_res_ap = r_ap
    eig_rows.append((p, n2, bad_sig, max_res_ap))
    info(f"  p={p}: T(p²)Θ = σ₃(p)Θ on n ≤ {n2}: mismatches={bad_sig}; "
         f"a_p-eigenvalue residual max={max_res_ap}")
    eigen_ok = eigen_ok and (bad_sig == 0) and (max_res_ap > 0)
check(
    "G2.ii.a: preregistered guess 'Θ not an eigenform' REFUTED by machine "
    "— Θ is an EXACT T(p²)-eigenform with Eisenstein eigenvalue "
    f"σ₃(p) = 1+p³ for p ∈ {HECKE_PS} (0 mismatches on full windows)",
    eigen_ok,
)
check(
    "G2.ii.b: eigenvalue is σ₃(p), NOT a_p(f8) (residual > 0 for every p) "
    "⇒ cusp component of Θ is ZERO — Θ is PURE genus-Eisenstein "
    "(Siegel–Weil / one-class-genus reading, classical; Cohen–Eisenstein "
    "weight 5/2 named classical)",
    all(r[3] > 0 for r in eig_rows) and eigen_ok,
)

# (ii.d) exact d -> d p^2, d p^4 towers for Theta and g
tower_ok = True
n_t1 = n_t2 = 0
for d in live:
    for p in HECKE_PS:
        if d % p == 0:
            continue
        chi = kronecker(d, p)
        aE1 = (1 + p ** 3) - chi * p
        ag1 = HEAD_AP[p] - chi * p
        if d * p * p <= QMAX:
            n_t1 += 1
            if int(Th[d * p * p]) != aE1 * ts[d]:
                tower_ok = False
            if int(g[d * p * p]) != ag1 * bs[d]:
                tower_ok = False
        if d * p ** 4 <= QMAX:
            n_t2 += 1
            aE2 = (1 + p ** 3) * aE1 - p ** 3
            ag2 = HEAD_AP[p] * ag1 - p ** 3
            if int(Th[d * p ** 4]) != aE2 * ts[d]:
                tower_ok = False
            if int(g[d * p ** 4]) != ag2 * bs[d]:
                tower_ok = False
info(f"towers: k=1 pairs={n_t1}, k=2 pairs={n_t2}")
check(
    "G2.ii.d: exact towers on all live (d,p) pairs — "
    "Θ(dp²) = (σ₃(p)−χ_d(p)p)·Θ(d), g(dp²) = (a_p−χ_d(p)p)·g(d), and the "
    f"k=2 recurrences (α₂ = a·α₁ − p³), integer-exact "
    f"({n_t1} k=1 + {n_t2} k=2 checks)",
    tower_ok and n_t1 >= 300 and n_t2 >= 40,
)

# (iii) Theta_d / |b_d| distribution
ratios = np.array([ts[d] / abs(bs[d]) for d in live])
lr = np.log(ratios)
gam_r = float(np.polyfit(ld, lr, 1)[0])
q1, q2, q3 = np.percentile(ratios, [25, 50, 75])
info(f"Θ_d/|b_d| on live d: min={ratios.min():.3f}, q1={q1:.2f}, "
     f"median={q2:.2f}, q3={q3:.2f}, max={ratios.max():.1f}")
info(f"slope of log(Θ/|b|) vs log d: {gam_r:.4f} (target ≈ 3/4)")
check(
    "G2.iii: population/coherence strength Θ_d/|b_d| ≥ 1 on all live d "
    f"(min {ratios.min():.3f}), median {q2:.2f}, growing with slope "
    f"{gam_r:.3f} ∈ (0.3, 1.2) — populations dominate coherence",
    bool(np.all(ratios >= 1.0)) and 0.3 < gam_r < 1.2,
)
g2_ok = eigen_ok and tower_ok and (gam_t - gam_b) > 0.3


# ================================================================ G3
print("=" * 72)
print("G3 -- THE THREE RANKIN CHANNELS (b², Θ², 4N₊N₋)")
print("=" * 72)

# (0) per-n exact split + coherence ladder
cross_full = (Th.astype(object) ** 2 - g.astype(object) ** 2)
split_exact = bool(np.all(cross_full % 4 == 0))
cross_full = cross_full // 4
npnm = Npl_full.astype(object) * Nmi_full.astype(object)
split_exact = split_exact and bool(np.all(cross_full == npnm))
check(
    f"G3.0: central structure equation b² = Θ² − 4·N₊N₋ exact as integer "
    f"identity for ALL n ≤ {QMAX} (cross channel = N₊N₋ ≥ 0)",
    split_exact,
)

coh_rows = []
for D in COHERENCE_LADDER:
    sub = [d for d in live if d <= D]
    num = sum((bs[d] ** 2) / d for d in sub)
    den = sum((ts[d] ** 2) / d for d in sub)
    coh_rows.append((D, len(sub), num / den))
    info(f"  coherence fraction f(D≤{D}): {num / den:.5f}  (N={len(sub)})")
coh_decreasing = all(coh_rows[i][2] > coh_rows[i + 1][2]
                     for i in range(len(coh_rows) - 1))
check(
    "G3.0.b: coherence fraction f = Σw b²/Σw Θ² DECREASES along the "
    f"window ladder ({coh_rows[0][2]:.4f} → {coh_rows[-1][2]:.5f}) — "
    "the family is an asymptotically THIN difference of two large "
    "positive families (cancellation depth measured)",
    coh_decreasing,
)

# (i)+(ii) tower scaling and empirical Lambda-weight signatures
lam_rows = {"b2": [], "th2": [], "cross": []}
scale_pts = {"b2": [], "th2": [], "cross": []}
n_zero_cross = 0
for d in live:
    cr_d = (ts[d] ** 2 - bs[d] ** 2) // 4
    if cr_d == 0:
        n_zero_cross += 1
        continue
    for p in HECKE_PS:
        if d % p == 0 or d * p * p > QMAX:
            continue
        n1 = d * p * p
        u1 = {
            "b2": (int(g[n1]) ** 2) / (bs[d] ** 2),
            "th2": (int(Th[n1]) ** 2) / (ts[d] ** 2),
            "cross": ((int(Th[n1]) ** 2 - int(g[n1]) ** 2) / 4) / cr_d,
        }
        for ch, gam in (("b2", 3), ("th2", 6), ("cross", 6)):
            if u1[ch] > 0:
                scale_pts[ch].append((math.log(p), math.log(u1[ch])))
        if d * p ** 4 <= QMAX:
            n2v = d * p ** 4
            u2 = {
                "b2": (int(g[n2v]) ** 2) / (bs[d] ** 2),
                "th2": (int(Th[n2v]) ** 2) / (ts[d] ** 2),
                "cross": ((int(Th[n2v]) ** 2 - int(g[n2v]) ** 2) / 4) / cr_d,
            }
            for ch, gam in (("b2", 3), ("th2", 6), ("cross", 6)):
                l1 = u1[ch] / p ** gam
                l2 = 2 * (u2[ch] / p ** (2 * gam)) - l1 * l1
                lam_rows[ch].append((d, p, l1, l2))

info(f"zero-cross live d skipped: {n_zero_cross}")
gam_meas = {}
for ch in ("b2", "th2", "cross"):
    xs = np.array([a for a, _ in scale_pts[ch]])
    ys = np.array([b for _, b in scale_pts[ch]])
    gam_meas[ch] = float(np.polyfit(xs, ys, 1)[0])
info(f"measured tower scaling exponents (log u₁ vs log p): "
     f"b²: {gam_meas['b2']:.2f} (alg 3), Θ²: {gam_meas['th2']:.2f} (alg 6), "
     f"cross: {gam_meas['cross']:.2f} (alg 6)")

# algebraic scaling: alpha_E(p)^2 has exact p-degree 6; alpha(p)^2 = O(p^3)
P_s, AHAT_s = sp.symbols("p ahat", positive=True)
degE = sp.degree(sp.expand(((1 + P_s ** 3) - P_s) ** 2), P_s)
lim_b2 = sp.limit(((AHAT_s * P_s ** sp.Rational(3, 2)
                    - P_s) ** 2) / P_s ** 6, P_s, sp.oo)
check(
    "G3.i: channel scaling — Θ²/cross towers live at p⁶ "
    f"(deg α_E(p)² = {degE}; measured {gam_meas['th2']:.2f}/"
    f"{gam_meas['cross']:.2f}), b² tower at p³ (α(p)²/p⁶ → 0 exactly; "
    f"measured {gam_meas['b2']:.2f}) — the polarised channels live at "
    "the POPULATION scale, the family at the coherence scale",
    degE == 6 and lim_b2 == 0
    and abs(gam_meas["th2"] - 6) < 0.4 and abs(gam_meas["cross"] - 6) < 0.5
    and abs(gam_meas["b2"] - 3) < 1.0,
)

stats = {}
for ch in ("b2", "th2", "cross"):
    l1s = np.array([r[2] for r in lam_rows[ch]])
    l2s = np.array([r[3] for r in lam_rows[ch]])
    stats[ch] = (l1s, l2s)
    info(f"  λ-signature {ch:>5}: n={len(l1s)}; "
         f"λ₁ ∈ [{l1s.min():.3f}, {l1s.max():.3f}] mean={l1s.mean():.3f}; "
         f"λ₂ ∈ [{l2s.min():.3f}, {l2s.max():.3f}] mean={l2s.mean():.3f}")

l1_t, l2_t = stats["th2"]
l1_x, l2_x = stats["cross"]
l1_b, l2_b = stats["b2"]
spread_b = l1_b.max() / max(l1_b.min(), 1e-12)
spread_t = l1_t.max() / max(l1_t.min(), 1e-12)
# algebraic even-kill of the b^2 core: E_ST[Phi_2] = 0 (T60/T61 classical)
th_s = sp.symbols("theta", positive=True)
dens_st = (2 / sp.pi) * sp.sin(th_s) ** 2
Phi2 = AHAT_s ** 4 - 4 * AHAT_s ** 2 + 2
est_phi2 = sp.integrate(Phi2.subs(AHAT_s, 2 * sp.cos(th_s)) * dens_st,
                        (th_s, 0, sp.pi))
check(
    "G3.ii: Λ-weight signatures — Θ²-channel has NO even-power kill "
    f"(λ₂ ∈ [{l2_t.min():.3f}, {l2_t.max():.3f}] ≈ 1 on all pairs; "
    f"cross λ₂ ∈ [{l2_x.min():.3f}, {l2_x.max():.3f}]); b²-channel core "
    f"kills even powers (E_ST[Φ₂] = {est_phi2} exact; empirical λ₂ wild: "
    f"[{l2_b.min():.2f}, {l2_b.max():.2f}]); population channels tight "
    f"(λ₁ spread {spread_t:.2f}×) vs coherence wild ({spread_b:.0f}×)",
    est_phi2 == 0
    and bool(np.all(l2_t > 0.85)) and bool(np.all(l2_t < 1.10))
    and bool(np.all(l2_x > 0.60)) and bool(np.all(l2_x < 1.10))
    and bool(np.all(l1_t > 0.80)) and bool(np.all(l1_t < 1.40))
    and spread_b > 5 * spread_t
    and len(l2_t) >= 35 and len(l2_b) >= 35,
)

# (iii) ALGEBRAIC identification: Theta^2 channel local factor = X4 floor
X_s = sp.symbols("X")
chi_s = sp.symbols("chi")
aE_s = 1 + P_s ** 3
N_E = (1 + (P_s ** 3 - 2 * chi_s * aE_s * P_s + chi_s ** 2 * P_s ** 2) * X_s
       + chi_s ** 2 * P_s ** 5 * X_s ** 2)
D_E = ((1 - (aE_s ** 2 - 2 * P_s ** 3) * X_s + P_s ** 6 * X_s ** 2)
       * (1 - P_s ** 3 * X_s))
fac_ok = sp.expand(
    (1 - X_s) * (1 - P_s ** 6 * X_s)
    - (1 - (aE_s ** 2 - 2 * P_s ** 3) * X_s + P_s ** 6 * X_s ** 2)
) == 0
al_sym = [sp.Integer(1), sp.expand(aE_s - chi_s * P_s)]
for _k in range(2, 8):
    al_sym.append(sp.expand(aE_s * al_sym[-1] - P_s ** 3 * al_sym[-2]))
S_sym = sum(sp.expand(al_sym[k] ** 2) * X_s ** k for k in range(8))
ser_diff = sp.expand(S_sym * D_E - N_E)
series_ok = all(sp.simplify(ser_diff.coeff(X_s, k)) == 0 for k in range(7))
E0 = (N_E / D_E).subs(chi_s, 0)
floor_local = ((1 / (1 - X_s)) * (1 / (1 - P_s ** 3 * X_s)) ** 2
               * (1 / (1 - P_s ** 6 * X_s)) * (1 - P_s ** 6 * X_s ** 2))
floor_ok = sp.simplify(E0 - floor_local) == 0
info("Θ²-channel local factor (a = σ₃(p), T57 closed form):")
info("  Σ_k α_E(p^k)² X^k = N_E / [(1−X)(1−p³X)(1−p⁶X)]  (χ generic)")
info("  χ=0:  = ζ_p(w)·ζ_p(w−3)²·ζ_p(w−6) / ζ_p(2w−6)")
info("  = the T58-X4 EISENSTEIN FLOOR Z_Eis, local — the T63 ζ-kernel")
info("  ζ(u)²/ζ(2u) (u=w−3) sits INSIDE WITH PLUS as a factor.")
check(
    "G3.iii: Θ²-channel local Euler factor identified EXACTLY (sympy): "
    "denominator (1−X)(1−p³X)(1−p⁶X) [ζ-shift product, a²−2p³ split "
    "exact]; series = closed form for k ≤ 6, χ generic; χ=0 factor "
    "= T58-X4 Eisenstein floor ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6) local — "
    "ζ-kernel WITH PLUS in the Θ²-family (Rankin–Selberg/Siegel–Weil "
    "named classical)",
    fac_ok and series_ok and floor_ok,
)

# linear level: Theta-amplitude tower is a pure zeta-shift GL(1) object
lin_ok = sp.expand((1 - X_s) * (1 - P_s ** 3 * X_s)
                   - (1 - aE_s * X_s + P_s ** 3 * X_s ** 2)) == 0
check(
    "G3.iii.b: LINEAR level — Θ-amplitude tower G_E = (1−χpX)/"
    "[(1−X)(1−p³X)] = ζ_p(w)ζ_p(w−3)·(Dirichlet numerator): pure GL(1) "
    "ζ-shifts (vs cuspidal degree-2 for g, T67) — the polarisation "
    "splits ζ-content (Θ side) from Hecke-cusp content (g side) "
    "already at amplitude level",
    lin_ok,
)

# Dirichlet coefficient positivity of the global floor, n <= N_FLOOR
om = np.zeros(N_FLOOR + 1, dtype=np.int64)
for p in sp.primerange(2, N_FLOOR + 1):
    p = int(p)
    om[p::p] += 1
B_arr = [0] * (N_FLOOR + 1)
for n in range(1, N_FLOOR + 1):
    B_arr[n] = (2 ** int(om[n])) * n ** 3
floor_coeff = [0] * (N_FLOOR + 1)
for a_i in range(1, N_FLOOR + 1):          # zeta(w): coeff 1
    for b_i in range(1, N_FLOOR // a_i + 1):
        ab = a_i * b_i
        vb = B_arr[b_i]
        for c_i in range(1, N_FLOOR // ab + 1):
            floor_coeff[ab * c_i] += vb * c_i ** 6
floor_pos = all(c > 0 for c in floor_coeff[1:])
info(f"floor Dirichlet coefficients head: {floor_coeff[1:8]}")
check(
    f"G3.iii.c: global floor ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6) has strictly "
    f"POSITIVE Dirichlet coefficients for all n ≤ {N_FLOOR} "
    "(2^ω-convolution — plus-side ζ-content, coefficient level)",
    floor_pos,
)

# (iv) layer algebra: p^{3k} layer of the floor vs family core weights
L_floor = sp.series(X_s * sp.diff(sp.log(floor_local), X_s), X_s, 0,
                    K_MAX + 1).removeO()
layer3 = []
for k in range(1, K_MAX + 1):
    lam_k = sp.expand(L_floor.coeff(X_s, k))
    layer3.append(int(lam_k.coeff(P_s, 3 * k)))
Y_s = sp.symbols("Y", positive=True)
G0 = (1 + Y_s) / (1 - Y_s)
ratio_ser = sp.series(Y_s * sp.diff(sp.log(G0), Y_s), Y_s, 0,
                      K_MAX + 1).removeO()
ratio_w = [int(ratio_ser.coeff(Y_s, k)) for k in range(1, K_MAX + 1)]
fam_w = [ratio_w[0] - 1] + ratio_w[1:]
info(f"floor p^(3k)-layer weights  = {layer3}")
info(f"ratio core weights (T63)    = {ratio_w}")
info(f"family core weights (T61)   = {fam_w}")
diff_w = [layer3[k] - fam_w[k] for k in range(K_MAX)]
info(f"difference (floor − family) = {diff_w}  (Plancherel δ_k1 only)")
flat_even_floor = [layer3[k] for k in range(1, K_MAX, 2)]
flat_even_fam = [fam_w[k] for k in range(1, K_MAX, 2)]
minus_isolated = flat_even_floor != flat_even_fam
check(
    "G3.iv: layer algebra (sympy exact) — the p^{3k}-layer of the "
    f"Θ²-floor is {layer3[:4]}… = T63 ratio weights [2,0,2,0,…]; family "
    f"core = [1,0,2,0,…]; difference = δ_k1 (Plancherel, PLUS side); "
    f"even-k kill IDENTICAL on both sides ({flat_even_floor[:3]} vs "
    f"{flat_even_fam[:3]}) ⇒ the ♭/doubling minus is SHARED, it does "
    "NOT migrate into the cross channel",
    ratio_w == [2 if k % 2 == 1 else 0 for k in range(1, K_MAX + 1)]
    and fam_w == [1 if k == 1 else (2 if k % 2 == 1 else 0)
                  for k in range(1, K_MAX + 1)]
    and layer3 == ratio_w
    and diff_w == [1] + [0] * (K_MAX - 1)
    and not minus_isolated,
)
g3_alg_ok = fac_ok and series_ok and floor_ok and lin_ok and floor_pos \
    and (layer3 == ratio_w) and split_exact


# ================================================================ G4
print("=" * 72)
print("G4 -- WEIL BOOKKEEPING OF THE POLARISED FORMS")
print("=" * 72)

# (i) Gram-level exact decomposition
live_gram = [d for d in live if d <= D_GRAM]
ms = list(range(1, M_GRAM + 1, 2))
nd, nm = len(live_gram), len(ms)
t_gram = time.time()
Xmat = np.zeros((nd, nm))
for j, d in enumerate(live_gram):
    for i, m in enumerate(ms):
        Xmat[j, i] = float(kronecker(d, m))
w_arr = np.array([1.0 / d for d in live_gram])
c_b2 = np.array([float(bs[d] ** 2) for d in live_gram])
c_t2 = np.array([float(ts[d] ** 2) for d in live_gram])
c_x4 = np.array([float(ts[d] ** 2 - bs[d] ** 2) / 4.0 for d in live_gram])
K_b2 = Xmat.T @ (Xmat * (w_arr * c_b2)[:, None])
K_t2 = Xmat.T @ (Xmat * (w_arr * c_t2)[:, None])
K_x4 = Xmat.T @ (Xmat * (w_arr * c_x4)[:, None])
rel_K = float(np.linalg.norm(K_t2 - (K_b2 + 4.0 * K_x4), "fro")
              / np.linalg.norm(K_t2, "fro"))
info(f"Gram: #d={nd} (≤{D_GRAM}), #m={nm} (odd ≤ {M_GRAM}); "
     f"built in {time.time() - t_gram:.1f}s")
info(f"K_Θ² = K_b² + 4K_× rel Frobenius error = {rel_K:.3e}")
cancel_ratio = float(np.linalg.norm(K_b2, "fro")
                     / np.linalg.norm(K_t2, "fro"))
info(f"cancellation depth ‖K_b²‖/‖K_Θ²‖ = {cancel_ratio:.3e} "
     "(family = thin difference of two large positive forms)")
rng = np.random.default_rng(538)
test_vecs = [np.eye(nm)[i] for i in (0, 1, 2, 3)]
test_vecs.append(np.ones(nm))
test_vecs.append(np.array([(-1.0) ** i for i in range(nm)]))
test_vecs.append(np.exp(-np.arange(nm) / 50.0))
test_vecs.append(rng.choice([-1.0, 1.0], size=nm))
q_ok = True
q_pos = True
for v in test_vecs:
    qt = float(v @ K_t2 @ v)
    qb = float(v @ K_b2 @ v)
    qx = float(v @ K_x4 @ v)
    if abs(qt - (qb + 4 * qx)) > 1e-10 * max(abs(qt), 1.0):
        q_ok = False
    if qt < -1e-8 or qx < -1e-8 or qb < -1e-8:
        q_pos = False
check(
    f"G4.i: polarised Weil bookkeeping EXACT at Gram level — "
    f"Q_Θ²(v) = Q_b²(v) + 4·Q_×(v) on {len(test_vecs)} test vectors and "
    f"K-matrix identity rel {rel_K:.2e} < 1e-12 (deviation = "
    "implementation only)",
    rel_K < 1e-12 and q_ok and len(test_vecs) >= 8,
)
eig_t2 = float(np.linalg.eigvalsh(K_t2).min())
eig_x4 = float(np.linalg.eigvalsh(K_x4).min())
scale_t2 = float(np.abs(K_t2).max())
info(f"min eig K_Θ² = {eig_t2:.3e}, min eig K_× = {eig_x4:.3e} "
     f"(scale {scale_t2:.3e})")
check(
    "G4.ii: POSITIVITY of the polarised forms — K_Θ² and K_× are PSD "
    f"(min eigs ≥ −1e-8·scale; Q ≥ 0 on the vector class) — both are "
    "positive combinations of rank-1 characters (structural, measured)",
    eig_t2 > -1e-8 * scale_t2 and eig_x4 > -1e-8 * scale_t2 and q_pos,
)

# (iii) zero-free prime sides on the T63 test-function class
lam_arr = np.zeros(N_LAM + 1)
pk_table = []                    # (n, p, k)
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
        u = math.log(n)
        if u > umax + 1e-12:
            continue
        wk = weights[k - 1]
        if wk == 0:
            continue
        s += wk * lam_arr[n] * math.exp(-0.5 * u) * g_fn(u)
    return 2.0 * s


def corr_plancherel(g_fn, umax):
    s = 0.0
    for n, p, k in pk_table:
        if k != 1:
            continue
        u = math.log(n)
        if u > umax + 1e-12:
            continue
        s += lam_arr[n] * math.exp(-0.5 * u) * g_fn(u)
    return 2.0 * s


def prime_zeta(g_fn, umax):
    s = 0.0
    for n, p, k in pk_table:
        u = math.log(n)
        if u > umax + 1e-12:
            continue
        s += lam_arr[n] * math.exp(-0.5 * u) * g_fn(u)
    return 2.0 * s


def g_flat(g_fn):
    return lambda x, gf=g_fn: math.exp(-0.5 * x) * gf(2.0 * x)


ident_ok = True
flat_ok = True
corr_pos = True
max_rel_id = 0.0
max_rel_fl = 0.0
for kind, param, g_fn in TEST_FNS:
    um = float(param) if kind == "fejer" else 8.0 * float(param)
    um_b = float(param) / 2.0 + 1e-12 if kind == "fejer" else um
    pr_ratio = prime_weighted(ratio_w, g_fn, um)
    pr_fam = prime_weighted(fam_w, g_fn, um)
    corr = corr_plancherel(g_fn, um)
    rel_id = abs((pr_ratio - pr_fam) - corr) / max(abs(corr), 1e-30)
    pz = prime_zeta(g_fn, um)
    pz_b = prime_zeta(g_flat(g_fn), um_b)
    rhs = 2.0 * pz - 2.0 * pz_b
    rel_fl = abs(pr_ratio - rhs) / max(abs(pr_ratio), abs(rhs), 1e-30)
    max_rel_id = max(max_rel_id, rel_id)
    max_rel_fl = max(max_rel_fl, rel_fl)
    if rel_id > 1e-12:
        ident_ok = False
    if rel_fl > 1e-6:
        flat_ok = False
    if corr <= 0:
        corr_pos = False
    info(f"  [{kind},{param}]: Prime_ratio={pr_ratio:.6f} "
         f"Prime_fam={pr_fam:.6f} Corr={corr:.6f} "
         f"relId={rel_id:.2e} rel♭={rel_fl:.2e}")
check(
    "G4.iii.a: Prime_ratio(g) − Prime_fam(g) = Corr_Plancherel(g) EXACT "
    f"on all {len(TEST_FNS)} test functions (max rel {max_rel_id:.2e}) "
    "and Corr > 0 on the class ⇒ Q_fam = Q_Θ²core + Corr with SHARED "
    "pole/arch (T63 assembly) — the cross content at core level is the "
    "PLUS-side Plancherel term",
    ident_ok and corr_pos and len(TEST_FNS) >= 8,
)
check(
    "G4.iii.b: Prime_ratio(g) = 2·Prime_ζ(g) − 2·Prime_ζ(g_♭) with "
    f"g_♭(x) = e^(−x/2) g(2x) (max rel {max_rel_fl:.2e} < 1e-6, "
    "truncation) — the ♭/doubling MINUS is present in the Θ²-core in "
    "exactly the T63 form; combined with G3.iv: the minus stays in the "
    "SHARED core ζ(u)²/ζ(2u), the polarisation does not move it",
    flat_ok,
)
check(
    "G4.iii.c: DECISIVE sign bilance — Q_Θ² does contain a 2Q_ζ-type "
    "component, but WITH the same −2Q_ζ(♭) partner as the family "
    "(coefficient level: even-k kill identical, G3.iv); the extra "
    "content of the polarised side is strictly positive (Plancherel "
    "δ_k1 + populations ζ(w), ζ(w−6)) ⇒ the problem does NOT gain "
    "positivity — it is re-booked, and the re-booking is now explicit",
    (not minus_isolated) and ident_ok and corr_pos and floor_pos,
)
g4_ok = (rel_K < 1e-12 and q_ok and q_pos and eig_t2 > -1e-8 * scale_t2
         and eig_x4 > -1e-8 * scale_t2 and ident_ok and flat_ok
         and corr_pos)


# ================================================================ G5
print("=" * 72)
print("G5 -- SYNTHESIS: polarisation diagram + honest typing + verdict")
print("=" * 72)

info("POLARISATION DIAGRAM (all entries machine-checked above):")
info("  [Θ = N₊+N₋]  populations: POSITIVE, pure genus-Eisenstein")
info("      T(p²)-eigenform with σ₃(p) (Siegel–Weil reading, classical);")
info("      towers = pure ζ-shift GL(1); Θ²-channel = X4 floor")
info("      ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6), Dirichlet coeffs > 0 — the")
info("      ζ-kernel ζ(u)²/ζ(2u) sits here WITH PLUS (as a factor).")
info("  [g = N₊−N₋]  coherence: SIGNED, cuspidal (a_p towers, T67);")
info("      Waldspurger b(d)² = R|d|^{3/2}L(f8×χ_d,2) (v537/v538);")
info("      metaplectic sign = lattice character (−1)^{u+w} — the T67")
info("      phase now has an explicit GEOMETRIC carrier.")
info("  [4N₊N₋]      cross: POSITIVE, Θ²-scale (p⁶), Eisenstein²-")
info("      dominated; core-level content = Plancherel δ_k1 (+Y) plus")
info("      population shifts — NOT the ♭ term.")
check(
    "G5.i: polarisation diagram issued — populations (Eisenstein, plus-"
    "side ζ) ↔ coherence (cuspidal, Waldspurger, signed) ↔ cross "
    "(positive, Plancherel + populations)",
    g1_ok and g2_ok and g3_alg_ok,
)

info("HONEST TYPING (what the polarisation achieves / does not):")
info("  ACHIEVES: (1) the minus of the family is made geometric and")
info("    EXACT: b² = Θ² − 4N₊N₋ with both partners positive counting")
info("    families (Gupta–Bleuler-style population/coherence split —")
info("    analogy name only); (2) the T67 metaplectic sign datum gets a")
info("    geometric carrier (lattice character); (3) the ζ-kernel DOES")
info("    appear plus-side on the Θ-side — but as the CLASSICAL")
info("    Siegel–Weil/Eisenstein floor (genus arithmetic, class-number")
info("    like), NOT as a new positive carrier of the family core.")
info("  DOES NOT: (1) the Waldspurger central values live in b² and")
info("    stay there — the Θ²-side carries DIFFERENT arithmetic (the")
info("    re-booking is explicit); (2) the ♭/doubling minus (even-k")
info("    kill of ζ(u)²/ζ(2u)) is IDENTICAL in the Θ²-core and the")
info("    family core — it is polarisation-INVARIANT; the cross channel")
info("    carries only Plancherel + population terms; (3) the coherence")
info("    fraction decays (f ≈ "
     f"{coh_rows[-1][2]:.4f} at D={coh_rows[-1][0]}) — the family is an")
info("    asymptotically thin difference: no positivity transport.")
info("  FENCE: dense-class positivity NOT established; no RH content.")
check(
    "G5.ii: honest typing issued — re-booking named (Waldspurger vs "
    "genus/Eisenstein arithmetic); ♭ invariance named; no positivity "
    "gain claimed",
    True,
)

# ---------------- verdict (preregistered enum)
zeta_plus_side = floor_ok and floor_pos
if not g1_ok:
    verdict = "BREAKS"
    detail = "G1 broke: theta identification or counting positivity failed."
elif g2_ok and g3_alg_ok and zeta_plus_side and minus_isolated:
    verdict = "POLARIZATION-SPLITS"
    detail = ("G1–G2 exact; ♭/minus isolated in the cross channel; "
              "Θ² side plus-side — Gupta–Bleuler structure stands.")
else:
    verdict = "RESHUFFLE-ONLY"
    detail = (
        "The decomposition is EXACT (G1 coefficient-exact; G2: Θ is a "
        "pure σ₃-eigenform, towers integer-exact; G3/G4: Gram split and "
        "prime-side identities exact) and the Θ²-side does carry the "
        "ζ-kernel plus-side (X4 floor, positive Dirichlet coefficients) "
        "— BUT the ♭/doubling minus does NOT migrate: the even-k kill "
        "of ζ(u)²/ζ(2u) sits IDENTICALLY in the Θ²-core (p^{3k} layer "
        "[2,0,2,0]) and in the family core ([1,0,2,0]); their difference "
        "is only the positive Plancherel δ_k1 + population shifts "
        "ζ(w), ζ(w−6).  WHERE THE MINUS LIVES: in the shared core "
        "ζ(u)²/ζ(2u) — polarisation-invariant.  No positivity gain; "
        "the re-booking (Waldspurger ↔ genus/Eisenstein arithmetic) is "
        "now explicit and machine-checked."
    )
info(f"VERDICT: {verdict}")
info(detail)
check(
    f"G5.iii: verdict {verdict} assigned from computed flags "
    f"(g1={g1_ok}, g2={g2_ok}, g3_alg={g3_alg_ok}, g4={g4_ok}, "
    f"zeta_plus={zeta_plus_side}, minus_isolated={minus_isolated})",
    verdict in ("POLARIZATION-SPLITS", "RESHUFFLE-ONLY", "BREAKS")
    and (verdict != "POLARIZATION-SPLITS" or minus_isolated)
    and (verdict != "BREAKS" or not g1_ok),
)

info("NEXT LEVER (typed, not executed): the polarisation fixes the")
info("  geometric carrier of the T67 phase — the remaining question is")
info("  NOT where the minus sits (answer: shared core, invariant) but")
info("  whether the CROSS channel admits its own period/RTF reading")
info("  (N₊N₋ as a theta-pairing of the two parity classes) — a")
info("  Rankin–Selberg pairing of the polarised halves; sandbox only.")
check(
    "G5.iv: no promotion executed; sandbox mapping only; next lever "
    "typed (cross-channel period reading)",
    True,
)


# ================================================================ end
print("=" * 72)
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print(f"VERDICT: {verdict}")
print(f"G1: b=N₊−N₋ / Θ=N₊+N₋ exact (n≤{N_ENUM}); N±≥0 (n≤{QMAX}); "
      f"glue classes mod16 {mod16_live}")
print(f"G2: Θ pure σ₃-eigenform (p∈{HECKE_PS}); γ_Θ={gam_t:.3f} vs "
      f"γ_b={gam_b:.3f}; Θ/|b| median {q2:.1f}")
print(f"G3: Θ²-floor = ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6) exact; layers "
      f"{layer3[:4]} vs fam {fam_w[:4]}; coherence f={coh_rows[-1][2]:.5f}")
print(f"G4: Gram split rel {rel_K:.1e}; PSD; Prime identities exact "
      f"(id {max_rel_id:.1e}, ♭ {max_rel_fl:.1e})")
print(f"FILE: {__file__}")
raise SystemExit(0 if FAIL == 0 else 1)
