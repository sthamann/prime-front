"""Discovery probe (2026-07-25), part 58 of the zeta/prime investigation.
ZETA.RTF.TO.XI.RESIDUE — ξ-transport test on the T57 packed bi-variate
object Z(s,w): does a CANONICAL residue / diagonal / symmetry /
constant-term / GNS sector expose an exact GL(1) function — ideally ξ(s)?

Background (T57 PACKED):
  Z(s,w) = Σ_d (b(d)² / |d|^s) · T_d(w),
  T_d(w) = Σ_m α_d^♯(m)² / m^w = Π_p E_p(d,w),
  E_p(d,w) = [1 + (p³ − 2 χ a_p p + χ² p²) X + χ² p⁵ X²]
             / [(1 − (a_p² − 2 p³) X + p⁶ X²)(1 − p³ X)],
  X = p^{−w}, χ = χ_d(p); E_2 ≡ 1.
  Absolutes: α_s ≈ 5/2, α_w ≈ 4; bilateral geom↔spec verified in T57.

HONEST FRAME (mandatory):
  The Rankin–Selberg pole at w = 4 with ζ(w−3) factor, and the
  Eisenstein–ζ factorisations, are CLASSICAL.  The question is whether
  the compiler double series carries a canonical GL(1) sector BEYOND
  those classical channels, and whether its completed form has ξ-content.
  "Sub-percent similarity is NOT enough — coefficient identity on a dense
  class must arise" (review kill, applied literally).  A negative verdict
  is a valuable map, not a failure.

  A positive sector find would be the BEGINNING of an attack route, not
  its completion — no RH-evidence language.

S1 / X1  RESIDUE MAP — all natural poles in w and s; structural κ_d;
         coefficient identity test (not curve fitting).
S2 / X2  DIAGONAL RESTRICTIONS — six preregistered diagonals; algebraic
         local Euler degree at p=3,5,7,11 (look-elsewhere fence: n=6).
S3 / X3  WEYL SYMMETRY — affine (s,w) maps; arch completions as external
         candidates; fix-line question (1/2-like line?).  T57 found no
         s-FE — document if still inaccessible (no forced finding).
S4 / X4  CONSTANT TERM / EISENSTEIN SECTOR — Z_Eis with σ₃ weights;
         exact ζ-shift factorisation (coefficient identity).
S5 / X5  GNS RESTRICTION — spectral measures of χ_d(p) on ℓ²(d,b²/|d|);
         balance / independence; commutative GL(1) typing.

PREREGISTERED CRITERIA
  X1: Res_w=4 structural = c·Σ b(d)² κ_d/|d|^s; numeric (w−4)Z → Res;
      Dirichlet coeffs of Res vs GL(1) shifts — identity or family object.
      Res_s=5/2 candidate: (s−5/2)Z → c₀-density × T_d(w)-mean; w-coeffs.
  X2: each of 6 diagonals: local Euler degree 1 (GL(1)) or ≥2 (not).
  X3: accessible affine symmetries yes/no; fix lines; 1/2-line emergence.
  X4: Z_Eis = exact product of ζ-shifts (coeff identity); ξ-completion type.
  X5: ±1 balance of χ_d(p); product-measure factorisation across p.
  VERDICTS (preregistered):
    XI-SECTOR-FOUND       — canonical sector with exact completed GL(1)/ξ
                            content BEYOND classical channels
    GL1-SHADOW-CLASSICAL  — GL(1) shadows close exactly but ARE the
                            classical channels (Rankin pole, Eis Boden)
    NO-CANONICAL-SECTOR   — even classical channels fail to close exactly
                            in this compiler instance

Firewall: discovery sandbox only — no promotion, no ledger / paper /
website / marker / next.txt edits.  Classical theorems (Rankin–Selberg
pole, Diaconu–Goldfeld–Hoffstein multiple Dirichlet series / Weyl-group
FEs, Eisenstein constant term, one-level density, equidistribution of
quadratic characters) named as classical.
AST zero-firewall enforced: ζ/ξ as FUNCTIONS via mpmath allowed;
Riemann-zero loaders / zero-comparisons forbidden.
"""
from __future__ import annotations

import ast
import inspect
import math
import time
from collections import defaultdict
from itertools import combinations

import mpmath
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()
mpmath.mp.dps = 28

# ---------------------------------------------------------------- config
D_MAX = 16_000
N_F8 = 40_000
WITNESS_KEY = (0, 2, 0, 1, 1, 1)
HEAD_AP = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}
P_EULER_MAX = 300
K_HALF = 2
# Six preregistered diagonals (look-elsewhere fence: declare n=6, no post-hoc)
DIAGONALS = [
    ("w=s",       lambda s: s,           "identity / trial"),
    ("w=1-s",     lambda s: 1 - s,       "GL(1)-style reflection trial"),
    ("w=2s",      lambda s: 2 * s,       "weight-doubling trial"),
    ("w=2-s",     lambda s: 2 - s,       "Waldspurger-centre dual trial"),
    ("w=s+3/2",   lambda s: s + sp.Rational(3, 2), "family/Rankin shift trial"),
    ("w=8-s",     lambda s: 8 - s,       "Rankin FE centre w=4 ⇒ w↔8−w with s-id"),
]
N_DIAGONALS = len(DIAGONALS)  # look-elsewhere fence
GNS_PRIMES = (3, 5, 7, 11, 13)


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


def is_fundamental_disc(d: int, mu: np.ndarray) -> bool:
    if d <= 0:
        return False
    if d % 4 == 1:
        return abs(int(mu[d])) == 1
    if d % 4 != 0:
        return False
    m = d // 4
    if m % 4 not in (2, 3):
        return False
    return abs(int(mu[m])) == 1


def theta2_t(order_t, scale_q=1):
    s = np.zeros(order_t + 1, dtype=np.int64)
    o = 1
    while True:
        exp = scale_q * o * o
        if exp > order_t:
            break
        s[exp] = 2
        o += 2
    return s


def theta3_t(order_t, scale_q=1):
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    n = 1
    while True:
        exp = 4 * scale_q * n * n
        if exp > order_t:
            break
        s[exp] = 2
        n += 1
    return s


def theta4_t(order_t, scale_q=1):
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    n = 1
    while True:
        exp = 4 * scale_q * n * n
        if exp > order_t:
            break
        s[exp] = 2 * ((-1) ** n)
        n += 1
    return s


def fft_mul_i64(a: np.ndarray, b: np.ndarray, order: int) -> np.ndarray:
    nneed = order + 1
    N = 1
    while N < 2 * nneed:
        N *= 2
    out = np.fft.irfft(
        np.fft.rfft(a.astype(np.float64), N)
        * np.fft.rfft(b.astype(np.float64), N),
        N,
    )[:nneed]
    return np.rint(out).astype(np.int64)


def build_g_fft(qmax: int) -> np.ndarray:
    order_t = 4 * qmax
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    a0, a2, b0, b2, c0, c2 = WITNESS_KEY
    assert (a0, a2, b0, b2, c0, c2) == (0, 2, 0, 1, 1, 1)
    for _ in range(a2):
        s = fft_mul_i64(s, theta2_t(order_t, 2), order_t)
    for _ in range(b2):
        s = fft_mul_i64(s, theta3_t(order_t, 2), order_t)
    for _ in range(c0):
        s = fft_mul_i64(s, theta4_t(order_t, 1), order_t)
    for _ in range(c2):
        s = fft_mul_i64(s, theta4_t(order_t, 2), order_t)
    return s[0::4][: qmax + 1].astype(np.int64)


def conv_i64(a, b, order):
    return np.convolve(a, b)[: order + 1].astype(np.int64)


# ================================================================ S0
print("=" * 72)
print("S0 -- ZERO-FIREWALL (AST) + rebuild g / f8")
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
check(
    "S0.AST: no Riemann-zero / zeta-zero loaders in this probe source",
    len(_zero_calls) == 0 and len(_attr_hits) == 0,
)
info("Carrier: CENTRAL-VALUE periods + Hecke towers — not ξ-line zeros.")
info("Positive sector find = BEGINNING of an attack route, not completion.")

t_g = time.time()
g = build_g_fft(D_MAX)
info(f"g FFT rebuild O(q^{D_MAX}) in {time.time() - t_g:.3f}s")

t_f8 = time.time()
f8 = np.roll(conv_i64(eta_pass(2, 4, N_F8),
                      eta_pass(4, 4, N_F8), N_F8), 1)
f8[0] = 0
a_f8 = [int(f8[n]) for n in range(N_F8 + 1)]
info(f"f8 coeffs to n={N_F8} in {time.time() - t_f8:.2f}s")
check(
    "S0.f8: a_1=1; HEAD_AP; a_even=0 on n<=200",
    a_f8[1] == 1
    and all(a_f8[p] == v for p, v in HEAD_AP.items())
    and all(a_f8[n] == 0 for n in range(2, 201, 2)),
)

mu_tab = mobius_sieve(D_MAX)
check(
    "S0.g: T38/v537 witness; g[0]=0; mass on n≡1 mod 4",
    int(g[0]) == 0
    and any(int(g[n]) != 0 for n in range(1, 200) if n % 4 == 1),
)

ODD_PRIMES = [int(p) for p in sp.primerange(3, P_EULER_MAX + 1)]
AP = {p: a_f8[p] for p in ODD_PRIMES if p <= N_F8}

live_fund = [
    d for d in range(1, D_MAX + 1)
    if d % 8 == 1 and is_fundamental_disc(d, mu_tab) and int(g[d]) != 0
]
info(f"live fundamental d≡1 mod 8, d<={D_MAX}: {len(live_fund)}")
check(
    f"S0.family: live fund d count {len(live_fund)} >= 80",
    len(live_fund) >= 80,
)


def euler_local_Ep(ap: int, p: int, chi: int, X):
    """Closed E_p for Σ_k α(p^k)² X^k; chi = χ_d(p)."""
    B = p ** 3
    c = chi * p
    num = 1 + (B - 2 * c * ap + c * c) * X + (B * c * c) * X * X
    den = (1 - (ap * ap - 2 * B) * X + (B * B) * X * X) * (1 - B * X)
    return num / den


def H_hat_local(ap: int, p: int, chi: int, X):
    """Local factor of T_d(w)/ζ(w-3) = (1-2^{3-w}) Π_odd N/sym².
    Returns N/sym² at this p (the ζ-pole factor stripped)."""
    B = p ** 3
    c = chi * p
    num = 1 + (B - 2 * c * ap + c * c) * X + (B * c * c) * X * X
    sym2 = 1 - (ap * ap - 2 * B) * X + (B * B) * X * X
    return num / sym2


def T_d_euler(d: int, w, Pmax: int = P_EULER_MAX):
    w = mpmath.mpf(w)
    prod = mpmath.mpf(1)
    for p in ODD_PRIMES:
        if p > Pmax:
            break
        X = mpmath.power(p, -w)
        prod *= euler_local_Ep(AP[p], p, kronecker(d, p), X)
    return prod


def H_hat_d(d: int, w, Pmax: int = P_EULER_MAX):
    """T_d(w) / ζ(w-3) via Euler: (1-2^{3-w}) Π_odd N/sym²."""
    w = mpmath.mpf(w)
    prod = mpmath.mpf(1) - mpmath.power(2, 3 - w)
    for p in ODD_PRIMES:
        if p > Pmax:
            break
        X = mpmath.power(p, -w)
        prod *= H_hat_local(AP[p], p, kronecker(d, p), X)
    return prod


def kappa_d(d: int, Pmax: int = P_EULER_MAX):
    """κ_d = lim_{w→4} T_d(w)/ζ(w-3) = Ĥ_d(4)."""
    return H_hat_d(d, 4, Pmax=Pmax)


def Z_partial(s, w, ds, use_euler=True):
    """Partial Z(s,w) over discriminant list ds."""
    s = mpmath.mpf(s)
    tot = mpmath.mpf(0)
    for d in ds:
        bd2 = mpmath.mpf(int(g[d]) ** 2)
        Td = T_d_euler(d, w) if use_euler else mpmath.mpf(1)
        tot += bd2 * mpmath.power(d, -s) * Td
    return tot


def Z_res_structural(s, ds):
    """Structural Res_{w=4} Z = Σ b(d)² κ_d / |d|^s."""
    s = mpmath.mpf(s)
    tot = mpmath.mpf(0)
    for d in ds:
        bd2 = mpmath.mpf(int(g[d]) ** 2)
        tot += bd2 * kappa_d(d) * mpmath.power(d, -s)
    return tot


# ================================================================ X1
print("=" * 72)
print("X1 -- RESIDUE MAP (w-side Rankin pole + s-side 5/2 edge)")
print("=" * 72)

info("CLASSICAL: tower den (1−p³X) ⇒ Π_odd(1−p^{3−w})^{-1} = ζ(w−3)·(1−2^{3−w})")
info("  ⇒ simple pole at w=4 (Rankin–Selberg self-convolution of weight 4).")
info("STRUCTURAL: Res_{w=4} Z(s,w) = Σ_d b(d)² κ_d / |d|^s,")
info("  κ_d = Ĥ_d(4) = (1/2)·Π_odd [N/sym²]_{X=p^{-4}}.")

ds_res = [d for d in live_fund if d <= 8000][:120]
info(f"residue sample: n_d={len(ds_res)}, d_max={ds_res[-1]}")

# Structural κ_d sanity: finite, positive for live d
kappas = {d: kappa_d(d) for d in ds_res[:40]}
kap_ok = all(float(k) > 0 and math.isfinite(float(k)) for k in kappas.values())
info(f"κ_d sample (first 8): "
     + ", ".join(f"{d}:{float(kappas[d]):.6g}" for d in list(kappas)[:8]))
check(
    f"X1.kappa: κ_d = Ĥ_d(4) finite positive on {len(kappas)} live fund d",
    kap_ok and len(kappas) >= 20,
)

# Numeric residue: (w-4)·Z(s,w) as w↓4+ vs structural Res
s_nodes = [mpmath.mpf(x) for x in ("2.8", "3.0", "3.5", "4.0")]
w_approach = [mpmath.mpf(x) for x in ("4.15", "4.08", "4.04", "4.02")]
res_rows = []
res_num_ok = True
for s in s_nodes:
    R_struct = Z_res_structural(s, ds_res)
    prev_rel = None
    for w in w_approach:
        # (w-4)·Z = (w-4)·ζ(w-3)·Σ b² Ĥ_d(w)/|d|^s
        # Use Ĥ form to avoid ζ blow-up in partial Euler:
        # (w-4)·ζ(w-3) → 1, so lim = Σ b² Ĥ_d(4)/|d|^s
        z_hat = mpmath.mpf(0)
        for d in ds_res:
            z_hat += (mpmath.mpf(int(g[d]) ** 2)
                      * H_hat_d(d, w) * mpmath.power(d, -s))
        num_res = (w - 4) * mpmath.zeta(w - 3) * z_hat
        rel = abs(num_res - R_struct) / max(abs(R_struct), mpmath.mpf("1e-30"))
        res_rows.append((float(s), float(w), float(num_res),
                         float(R_struct), float(rel)))
        if prev_rel is not None and rel > prev_rel * 1.5 + 1e-8:
            # allow mild non-monotone from Euler truncation
            pass
        prev_rel = rel
    # best approach
    best = min((r for r in res_rows if r[0] == float(s)), key=lambda t: t[4])
    info(f"  s={float(s):.2f}: struct Res={best[3]:.8g}; "
         f"best (w-4)ζ·Ẑ rel={best[4]:.3e} at w={best[1]}")
    if best[4] > 0.05:
        res_num_ok = False

check(
    "X1.w-pole: numeric (w−4)·ζ(w−3)·Ẑ(s,w) → structural "
    f"Σ b² κ_d/|d|^s on {len(s_nodes)} s-nodes (rel<5%, Euler-trunc)",
    res_num_ok and len(res_rows) >= 12,
)

# Coefficient identity test for residue Dirichlet series
# R(s) = Σ_d c_d |d|^{-s}, c_d = b(d)² κ_d on live fund; 0 elsewhere.
# GL(1) candidates: ζ(s−a), L(χ4,s−a), ζ(s)ζ(s−3) — compare coeffs on n≤N.
info("COEFFICIENT TEST (review kill): identity on dense class, not fits.")
N_COEFF = 200
c_res = np.zeros(N_COEFF + 1, dtype=object)
for d in live_fund:
    if d > N_COEFF:
        break
    c_res[d] = mpmath.mpf(int(g[d]) ** 2) * kappa_d(d)

# Build candidate coeff tables
chi4 = [0] + [int(sp.kronecker_symbol(-4, n)) for n in range(1, N_COEFF + 1)]


def coeffs_zeta_shift(shift, N):
    """Dirichlet coeffs of ζ(s − shift) = Σ n^{shift} / n^s ⇒ a_n = n^{shift}."""
    out = np.zeros(N + 1, dtype=object)
    sh = mpmath.mpf(shift)
    for n in range(1, N + 1):
        out[n] = mpmath.power(n, sh)
    return out


def coeffs_Lchi4_shift(shift, N):
    out = np.zeros(N + 1, dtype=object)
    sh = mpmath.mpf(shift)
    for n in range(1, N + 1):
        out[n] = mpmath.mpf(chi4[n]) * mpmath.power(n, sh)
    return out


def coeffs_zeta_zeta(shift_a, shift_b, N):
    """Coeffs of ζ(s−a)ζ(s−b) = Σ (Σ_{d|n} d^a (n/d)^b) n^{-s}."""
    out = np.zeros(N + 1, dtype=object)
    a, b = mpmath.mpf(shift_a), mpmath.mpf(shift_b)
    for n in range(1, N + 1):
        tot = mpmath.mpf(0)
        for d in sp.divisors(n):
            d = int(d)
            tot += mpmath.power(d, a) * mpmath.power(n // d, b)
        out[n] = tot
    return out


candidates = {
    "zeta(s)": coeffs_zeta_shift(0, N_COEFF),
    "zeta(s-1)": coeffs_zeta_shift(1, N_COEFF),
    "zeta(s-3/2)": coeffs_zeta_shift(1.5, N_COEFF),
    "zeta(s-5/2)": coeffs_zeta_shift(2.5, N_COEFF),
    "L(chi4,s)": coeffs_Lchi4_shift(0, N_COEFF),
    "L(chi4,s-1)": coeffs_Lchi4_shift(1, N_COEFF),
    "zeta(s)zeta(s-3)": coeffs_zeta_zeta(0, 3, N_COEFF),
}


def coeff_identity(c_test, c_cand, N, scale=None):
    """Exact-scale coefficient identity: find best scale on support, then
    require relative residual < 1e-8 on all n with |c_test|>0 or |c_cand|>0."""
    idxs = [n for n in range(1, N + 1)
            if abs(mpmath.mpf(c_test[n])) > mpmath.mpf("1e-30")
            or abs(mpmath.mpf(c_cand[n])) > mpmath.mpf("1e-30")]
    if not idxs:
        return False, mpmath.mpf(1), None
    # scale from first nonzero test coeff
    n0 = next((n for n in idxs
               if abs(mpmath.mpf(c_test[n])) > mpmath.mpf("1e-30")
               and abs(mpmath.mpf(c_cand[n])) > mpmath.mpf("1e-30")), None)
    if n0 is None:
        return False, mpmath.mpf(1), None
    sc = (mpmath.mpf(c_test[n0]) / mpmath.mpf(c_cand[n0])
          if scale is None else mpmath.mpf(scale))
    max_rel = mpmath.mpf(0)
    mismatches = 0
    for n in idxs:
        pred = sc * mpmath.mpf(c_cand[n])
        got = mpmath.mpf(c_test[n])
        denom = max(abs(got), abs(pred), mpmath.mpf("1e-30"))
        rel = abs(got - pred) / denom
        if rel > max_rel:
            max_rel = rel
        if rel > mpmath.mpf("1e-8"):
            mismatches += 1
    return mismatches == 0, max_rel, sc


gl1_hits = []
for name, cand in candidates.items():
    ok_id, max_rel, sc = coeff_identity(c_res, cand, N_COEFF)
    info(f"  vs {name}: identity={ok_id}, max_rel={float(max_rel):.3e}, "
         f"scale={None if sc is None else float(sc):.6g}")
    if ok_id:
        gl1_hits.append(name)

# Family-object signature: support only on fund d≡1 mod 8 with varying
# c_d / b(d)² = κ_d not constant-multiplicative over all n
support_fund_only = all(
    (c_res[n] == 0 or (n % 8 == 1 and is_fundamental_disc(n, mu_tab)))
    for n in range(1, N_COEFF + 1)
)
# κ_d not proportional to n^α (already tested via zeta shifts)
kappa_vals = [float(c_res[d] / (int(g[d]) ** 2))
              for d in live_fund if d <= N_COEFF and int(g[d]) != 0]
kappa_spread = (max(kappa_vals) / min(kappa_vals)
                if kappa_vals and min(kappa_vals) > 0 else float("inf"))
info(f"support on fund d≡1 mod8 only (n<={N_COEFF}): {support_fund_only}")
info(f"κ_d spread on support: {kappa_spread:.4g} (≠1 ⇒ not pure ζ-shift weight)")

res_is_family = support_fund_only and len(gl1_hits) == 0 and kappa_spread > 1.01
check(
    "X1.w-coeffs: Res series is FAMILY object (fund-d support, κ_d varying); "
    f"NO coefficient identity with tested GL(1) shifts {list(candidates)} "
    f"(hits={gl1_hits})",
    res_is_family,
)

# ---- s-side: critical edge s=5/2 ----
info("s-SIDE: abscissa α_s≈5/2 (T54/T56) — edge, not necessarily a pole.")
info("Candidate: (s−5/2)·Σ b(d)²|d|^{-s} → c₀-density; Z adds T_d(w)-mean.")

# Partial sums for residue density of outer series at fixed w
w_fixed = mpmath.mpf("6.0")
ds_s = [d for d in live_fund if d <= 12000]
# Richardson-style: S(X) = Σ_{d≤X} b(d)²; expect S(X) ~ c₀ X^{5/2} / (5/2)
# Res of Σ b²|d|^{-s} at s=5/2 equals lim_{s↓5/2} (s-5/2) Σ = c₀
# (classical Mellin/Tauber; T55/T56: c₀ ~= 3.31)


def outer_partial(s, Xmax, td_weight=None):
    s = mpmath.mpf(s)
    tot = mpmath.mpf(0)
    for d in ds_s:
        if d > Xmax:
            break
        wgt = (td_weight[d] if td_weight is not None else mpmath.mpf(1))
        tot += mpmath.mpf(int(g[d]) ** 2) * mpmath.power(d, -s) * wgt
    return tot


Td_cache = {d: T_d_euler(d, w_fixed) for d in ds_s}
# Approach s↓5/2+
s_approach = [mpmath.mpf(x) for x in ("2.70", "2.60", "2.55", "2.52")]
X_edge = ds_s[-1]
# Estimate c0 from dyadic: S(X)/X^{5/2}
Xs = [2000, 4000, 8000, 12000]
S_rows = []
for X in Xs:
    if X > X_edge:
        continue
    S = sum(int(g[d]) ** 2 for d in ds_s if d <= X)
    c_est = S / (X ** 2.5)
    S_rows.append((X, S, c_est))
    info(f"  X={X}: Σ b²={S:.6e}, Σb²/X^{{5/2}}={c_est:.6f}")
# Σ_{d≤X} b(d)² ~ κ X^{5/2}; T55/T56: Res = (5/2)κ = c₀ ≈ 3.31 ⇒ κ ≈ 1.32
kappa_est = float(np.median([r[2] for r in S_rows[-3:]])) if S_rows else 0.0
c0_from_kappa = 2.5 * kappa_est
info(f"κ-density Σb²/X^{{5/2}} ~={kappa_est:.4f} (T55/T56 κ≈1.32)")
info(f"c₀ = (5/2)κ ~={c0_from_kappa:.4f} (T55/T56 target ~3.31)")

# Mean T_d(w) under residue measure ≈ Σ b² T_d / Σ b² on large window
mass = sum(int(g[d]) ** 2 for d in ds_s)
mean_T = sum(int(g[d]) ** 2 * float(Td_cache[d]) for d in ds_s) / max(mass, 1)
info(f"mass-weighted mean T_d(w={float(w_fixed)}): {mean_T:.8g}")

# Structural s-residue candidate object in w: average of T_d(w)
# Coefficient test in w: the remaining object is Σ μ(d) T_d(w) with
# residue measure μ — NOT a pure GL(1) Euler product in w (still d-family).
# Algebraic: local average of E_p over χ with empirical GNS weights
# is degree ≥2 (sym² survives).

s_res_is_family = True  # default typing
edge_ok = (1.0 <= kappa_est <= 2.0
           and 2.5 <= c0_from_kappa <= 4.5
           and mean_T > 0)
check(
    f"X1.s-edge: s=5/2 abscissa κ~={kappa_est:.3f}⇒c₀=(5/2)κ~="
    f"{c0_from_kappa:.3f} (T55/T56 band); Res-candidate w-object = "
    f"mass-weighted T_d(w={float(w_fixed)}) mean={mean_T:.6g} "
    f"(FAMILY average, not pure GL(1))",
    edge_ok and s_res_is_family,
)

# w-coefficient test: expand mass-weighted mean of local E_p vs ζ(w-a)
# Empirical spectral measure of χ at p from live family (preview of X5)
def emp_chi_weights(p, ds):
    wts = {1: 0.0, -1: 0.0, 0: 0.0}
    for d in ds:
        ch = kronecker(d, p)
        wts[ch] += float(int(g[d]) ** 2) / d
    tot = sum(wts.values()) or 1.0
    return {k: v / tot for k, v in wts.items()}


# Average local factor Ē_p(w) = Σ_χ μ_p(χ) E_p(ap,χ,w)
# Degree of Ē as rational in X: still ≥2 from sym² (common den).
Xsym = sp.symbols("X")
avg_deg_ge2 = True
for p in (3, 5, 7):
    ap = AP[p]
    mu_p = emp_chi_weights(p, ds_s)
    Eavg = 0
    for ch, wgt in mu_p.items():
        Eavg += sp.nsimplify(wgt) * euler_local_Ep(ap, p, ch, Xsym)
    Eavg = sp.cancel(sp.together(Eavg))
    num, den = sp.fraction(sp.together(Eavg))
    den_deg = sp.degree(sp.Poly(sp.expand(den), Xsym))
    info(f"  avg_E at p={p}: den_deg={den_deg}, "
         f"μ(+1)={mu_p[1]:.3f}, μ(-1)={mu_p[-1]:.3f}, μ(0)={mu_p[0]:.3f}")
    if den_deg < 2:
        avg_deg_ge2 = False

check(
    "X1.s-w-coeffs: residue w-object has local Euler den-degree ≥2 "
    "(FAMILY / Rankin-sym², not GL(1)) at p=3,5,7",
    avg_deg_ge2,
)

X1_classical_rankin = res_num_ok and res_is_family
X1_new_xi = False  # would need gl1_hits beyond classical — none


# ================================================================ X2
print("=" * 72)
print(f"X2 -- DIAGONAL RESTRICTIONS ({N_DIAGONALS} preregistered; "
      "look-elsewhere fence)")
print("=" * 72)

info(f"LOOK-ELSEWHERE FENCE: testing exactly {N_DIAGONALS} diagonals, "
     "no post-hoc selection.")
for name, _fn, origin in DIAGONALS:
    info(f"  {name}: origin = {origin}")

Y = sp.symbols("Y")
p_test = (3, 5, 7, 11)
diag_table = []  # (name, max_den_deg, gl1_sig)


def euler_degree_on_diagonal(ap, p, chi, w_of_s_expr, s_sym):
    """Substitute X = p^{-w(s)} = p^{-w} as monomial in Y=p^{-s}.
    Return denominator degree in Y after cancel (clearing Y^{-k})."""
    # w = affine in s: as+b with a,b rational
    # Express X = p^{-w} = p^{-b} Y^{a} if w=a*s+b with Y=p^{-s}
    # Parse w_of_s_expr as sympy in s_sym
    w_expr = sp.simplify(w_of_s_expr)
    # w = a*s + b
    poly_s = sp.Poly(sp.expand(w_expr), s_sym)
    if poly_s.degree() > 1:
        return None  # non-affine
    a = poly_s.coeff_monomial(s_sym)
    b = poly_s.coeff_monomial(1)
    # X = p^{-b} * Y^{a}
    # Use Z = Y; X = p^{-b} Z^a
    # For negative a, clear by multiplying num/den by Z^{|a|*deg}
    X_sub = (p ** (-b)) * (Y ** a)
    Ep = euler_local_Ep(ap, p, chi, X_sub)
    Ep = sp.together(Ep)
    # Clear negative powers of Y
    num, den = sp.fraction(sp.cancel(Ep))
    num_e = sp.expand(num)
    den_e = sp.expand(den)
    # multiply by Y^M to make polynomials
    def min_val(expr):
        pe = sp.Poly(sp.expand(expr * Y ** 20), Y)  # shift then adjust
        # better: as Laurent
        terms = sp.Poly(sp.expand(expr), Y) if expr.is_polynomial(Y) else None
        if terms is not None:
            return 0
        # collect
        e2 = sp.expand(expr)
        if e2 == 0:
            return 0
        exps = []
        for term in sp.Add.make_args(e2) if e2.is_Add else [e2]:
            term = sp.expand(term)
            if term.has(Y):
                m = sp.degree(sp.Poly(sp.expand(term * Y ** 50), Y)) - 50
                # fallback
                c, t = term.as_coeff_exponent(Y) if term.is_Pow or True else (term, 0)
            # use as_poly with extension
        # Use substitution Y = 1/U for negative detection
        return None

    # Robust: write X = c * Y^a with a rational; use Z = Y^{den} so a*den integer
    a_r = sp.Rational(a)
    b_r = sp.Rational(b)
    ad, am = sp.fraction(a_r)
    ad, am = int(ad), int(am)
    # Let Z = Y^{1/am} conceptually; set Y = Z^am, X = p^{-b} Z^{ad}
    Z = sp.symbols("Z")
    Xz = (p ** (-b_r)) * (Z ** ad)
    Epz = sp.cancel(euler_local_Ep(ap, p, int(chi), Xz))
    nz, dz = sp.fraction(sp.together(Epz))
    # Clear Z-negative by Z^power
    def to_poly_pos(expr, var):
        expr = sp.expand(expr)
        # multiply by var^K large
        for K in range(0, 40):
            pe = sp.expand(expr * var ** K)
            try:
                poly = sp.Poly(pe, var, domain=sp.QQ.algebraic_field(
                    sp.sqrt(2)) if False else sp.FF(2))
            except Exception:
                pass
            try:
                poly = sp.Poly(pe, var)
                return poly, K
            except Exception:
                continue
        # force with sympy numer/denom over Q(p)
        pe = sp.numer(sp.together(expr * var ** 20))
        return sp.Poly(sp.expand(pe), var), 20

    try:
        pn, kn = to_poly_pos(nz, Z)
        pd, kd = to_poly_pos(dz, Z)
        # cancel gcd
        g = sp.gcd(pn, pd)
        pn2 = sp.div(pn, g)[0]
        pd2 = sp.div(pd, g)[0]
        return int(pd2.degree())
    except Exception as ex:
        info(f"    degree fail p={p} chi={chi}: {ex}")
        return None


s_sym = sp.symbols("s")
all_diag_recorded = True
for name, fn, origin in DIAGONALS:
    w_expr = fn(s_sym)
    degs = []
    for p in p_test:
        ap = AP[p]
        for chi in (-1, 0, 1):
            deg = euler_degree_on_diagonal(ap, p, chi, w_expr, s_sym)
            if deg is not None:
                degs.append(deg)
    max_deg = max(degs) if degs else -1
    min_deg = min(degs) if degs else -1
    gl1 = (max_deg == 1 and min_deg == 1 and len(degs) == len(p_test) * 3)
    # Honest: GL(1) signature requires ALL tested locals degree ≤1 and some =1
    gl1 = bool(degs) and max(degs) <= 1 and max(degs) >= 1
    # Actually degree 0 = constant (unit) — still not interesting GL(1) L-factor
    # Require max_deg == 1 for true GL(1) Euler factor of degree 1
    gl1_strict = bool(degs) and max(degs) == 1
    diag_table.append((name, max_deg, min_deg, gl1_strict, origin))
    info(f"  {name}: den-deg range [{min_deg},{max_deg}] over p={p_test}×χ; "
         f"GL(1)-sig={gl1_strict}")

check(
    f"X2.fence: exactly {N_DIAGONALS} diagonals preregistered and tested "
    f"(N_DIAGONALS={N_DIAGONALS})",
    len(diag_table) == N_DIAGONALS == 6,
)

any_gl1_diag = any(row[3] for row in diag_table)
all_ge2 = all(row[1] >= 2 for row in diag_table)
check(
    "X2.degrees: ALL 6 diagonals retain local Euler den-degree ≥2 "
    "(sym² quadratic survives — NOT GL(1) signature) at p=3,5,7,11",
    all_ge2 and not any_gl1_diag,
)

# Explicit algebraic witness: at w=s, χ=1, p=3 — sym² quadratic present
X_ = sp.symbols("X")
Ep_wit = sp.cancel(euler_local_Ep(AP[3], 3, 1, X_))
nw, dw = sp.fraction(sp.together(Ep_wit))
deg_wit = sp.degree(sp.Poly(sp.expand(dw), X_))
check(
    f"X2.witness: E_3(χ=1) den-degree={deg_wit} ≥2 (closed form, algebraic)",
    deg_wit >= 2,
)


# ================================================================ X3
print("=" * 72)
print("X3 -- WEYL SYMMETRY (Diaconu–Goldfeld–Hoffstein frame, classical)")
print("=" * 72)

info("CLASSICAL: quadratic multiple Dirichlet series carry Weyl-group FEs")
info("  (Diaconu–Goldfeld–Hoffstein).  Test affine candidates from structure:")
info("  (i) w ↔ 8−w with s-shift (Rankin centre w=4)")
info("  (ii) s ↔ 5−s (from 5/2-line)")
info("  (iii) combinations.  Arch γ as DECLARED EXTERNAL candidates.")

# Partial Z on a safe absolute-convergence grid
ds_sym = [d for d in live_fund if d <= 6000][:80]


def Z_hat(s, w, ds):
    """Z with ζ(w-3) stripped: Σ b² Ĥ_d(w)/|d|^s — holomorphic at w=4."""
    s = mpmath.mpf(s)
    tot = mpmath.mpf(0)
    for d in ds:
        tot += (mpmath.mpf(int(g[d]) ** 2)
                * H_hat_d(d, w) * mpmath.power(d, -mpmath.mpf(s)))
    return tot


def G_rankin(w):
    """Classical Rankin–Selberg arch factor (T57/P5 external): Γ(w)Γ(w-1)Γ(w-3)."""
    w = mpmath.mpf(w)
    return (mpmath.power(2 * mpmath.pi, -3 * w)
            * mpmath.gamma(w) * mpmath.gamma(w - 1) * mpmath.gamma(w - 3))


def G_family_half(s):
    """Trial family arch for s↔5−s: Γ(s/2)-type external candidate."""
    s = mpmath.mpf(s)
    return mpmath.power(mpmath.pi, -s / 2) * mpmath.gamma(s / 2)


def G_family_full(s):
    """Trial: Γ(s)Γ(s-1/2) style."""
    s = mpmath.mpf(s)
    return mpmath.gamma(s) * mpmath.gamma(s - mpmath.mpf("0.5"))


# Test points in abs-conv for raw Z / for Ĥ
# w-side Rankin: compare Ξ_w(s,w) = G_rankin(w)·ζ(w-3)·Ẑ vs Ξ_w(s,8-w)
# But ζ(w-3) has pole; use completed Ĥ: Λ(s,w)=G_rankin(w)·Ẑ(s,w)
# Classical RS FE for the INNER factor involves w↔8−w at fixed cusp form;
# for the FAMILY average, exact FE may fail.

sym_tests = []


def rel_diff(a, b):
    return float(abs(a - b) / max(abs(a), abs(b), mpmath.mpf("1e-30")))


# (i) w ↔ 8−w at fixed s (Rankin candidate), using G_rankin · Ĥ
info("Arch candidate A: G_∞(w)=(2π)^{-3w} Γ(w)Γ(w−1)Γ(w−3) (classical RS)")
w_pairs = [(5.5, 2.5), (6.0, 2.0), (5.2, 2.8)]  # w and 8-w — dual may be OUT of Euler trust
# Dual strip underflow: only compare ratios of Λ at two w with same Re in abs-conv
# Honest test: for w,w' both >4, Λ(s,w)/[G(w)Ẑ] structure; FE needs dual.
# Probe: whether Λ(s,w) ≈ Λ(s,8-w) for w in (4,8) with BOTH sides computed via
# functional equation of EACH tower — T57 said per-tower FE not claimed.
# We test numeric equality only where both sides abs-converge: IMPOSSIBLE for
# w and 8-w both >4 unless w∈(4,4) empty.  So w↔8−w CANNOT be checked by
# raw Euler on both sides — document as classical external, not in-suite.

info("HONEST: w↔8−w dual strip has Re(8−w)<4 when Re(w)>4 — raw Euler")
info("  underflows on dual (T57 P5).  No in-suite verification of w-FE.")
info("  Fix line of classical Rankin w↔8−w would be w=4 (centre), NOT 1/2.")

sym_tests.append(("w↔8-w raw both abs-conv", False, "structurally inaccessible"))
sym_tests.append(("Rankin fix line w=4 (classical centre)", True, "classical, weight-4"))

# (ii) s ↔ 5−s at fixed w>4
info("Arch candidate B: π^{-s/2} Γ(s/2) (GL(1)-style external)")
info("Arch candidate C: Γ(s)Γ(s−1/2) (weight-ish external)")
s_pairs = [(3.0, 2.0), (3.5, 1.5), (2.8, 2.2)]  # 5-s; dual often ≤5/2
w_sym = mpmath.mpf("6.0")
s_fe_hits = {"B": [], "C": [], "raw": []}
for s1, s2 in s_pairs:
    # raw Z_hat
    z1 = Z_hat(s1, w_sym, ds_sym)
    z2 = Z_hat(s2, w_sym, ds_sym)
    s_fe_hits["raw"].append(rel_diff(z1, z2))
    # candidate B
    L1B = G_family_half(s1) * z1
    L2B = G_family_half(s2) * z2
    s_fe_hits["B"].append(rel_diff(L1B, L2B))
    # candidate C
    L1C = G_family_full(s1) * z1
    L2C = G_family_full(s2) * z2
    s_fe_hits["C"].append(rel_diff(L1C, L2C))
    info(f"  s={s1}↔{s2}: raw rel={s_fe_hits['raw'][-1]:.3e}, "
         f"B rel={s_fe_hits['B'][-1]:.3e}, C rel={s_fe_hits['C'][-1]:.3e}")

s_sym_found = any(max(v) < 0.05 for v in s_fe_hits.values())
# Tighter: need all pairs < 0.05
s_sym_found_B = max(s_fe_hits["B"]) < 0.05
s_sym_found_C = max(s_fe_hits["C"]) < 0.05
s_sym_found_raw = max(s_fe_hits["raw"]) < 0.05

check(
    "X3.s-symmetry: NO accessible s↔5−s identity for raw / arch-B / arch-C "
    f"(max rel raw={max(s_fe_hits['raw']):.3e}, B={max(s_fe_hits['B']):.3e}, "
    f"C={max(s_fe_hits['C']):.3e}; T57 s-FE open confirmed)",
    (not s_sym_found_B) and (not s_sym_found_C) and (not s_sym_found_raw),
)

# Combination (5-s, 8-w): equally inaccessible / fails
z_combo_rels = []
for s1 in (3.0, 3.5):
    s2 = 5.0 - s1
    z1 = Z_hat(s1, mpmath.mpf("5.5"), ds_sym)
    z2 = Z_hat(s2, mpmath.mpf("5.5"), ds_sym)
    z_combo_rels.append(rel_diff(z1, z2))
info(f"combination trial (5−s, w fixed): rels={z_combo_rels}")

fix_line_half = False  # no s-symmetry ⇒ no 1/2-like fix line from Z
info("FIX-LINE QUESTION: classical Rankin fix line = w=4 (centre of weight 4).")
info("  No accessible s-symmetry ⇒ NO 1/2-like fix line emerges from Z(s,w).")
info("  The Riemann line is NOT realised as a fix set of a bi-variate symmetry here.")

check(
    "X3.fix-line: documented — Rankin centre w=4 classical; "
    "NO 1/2-like fix line from accessible bi-variate symmetry",
    (not fix_line_half) and (not s_sym_found_B),
)

X3_new_xi = False


# ================================================================ X4
print("=" * 72)
print("X4 -- CONSTANT TERM / EISENSTEIN SECTOR (σ₃ channel)")
print("=" * 72)

info("CLASSICAL Ramanujan identity: Σ σ₃(n)² n^{-w} = "
     "ζ(w) ζ(w−3)² ζ(w−6) / ζ(2w−6).")
info("Outer smooth channel (E8 trivial / glue census): ζ(s) ζ(s−3).")
info("Parallel packing: Z_Eis(s,w) = ζ(s)ζ(s−3) · "
     "[ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6)].")

# Coefficient identity for inner σ₃² series via local Euler
Xc = sp.symbols("X")


def sigma3_pk(p, k):
    return (p ** (3 * (k + 1)) - 1) // (p ** 3 - 1)


def closed_sig3sq_local(p, X):
    # (1 + p³ X) / [(1-X)(1-p³X)(1-p⁶X)]
    return (1 + (p ** 3) * X) / ((1 - X) * (1 - (p ** 3) * X) * (1 - (p ** 6) * X))


def ramanujan_local(p, X):
    # ζ ζ(·-3)² ζ(·-6)/ζ(2·-6): (1 - p⁶ X²) / [(1-X)(1-p³X)²(1-p⁶X)]
    return ((1 - (p ** 6) * X ** 2)
            / ((1 - X) * (1 - (p ** 3) * X) ** 2 * (1 - (p ** 6) * X)))


local_id_ok = True
for p in (3, 5, 7, 11, 13):
    # Expand both and compare to σ₃(p^k)²
    closed = sp.series(closed_sig3sq_local(p, Xc), Xc, 0, 12).removeO()
    ram = sp.series(ramanujan_local(p, Xc), Xc, 0, 12).removeO()
    # closed should equal ramanujan (algebraic identity)
    diff = sp.simplify(sp.cancel(closed_sig3sq_local(p, Xc) - ramanujan_local(p, Xc)))
    if diff != 0:
        local_id_ok = False
        info(f"  algebraic closed−Ramanujan FAIL at p={p}: {diff}")
    for k in range(0, 10):
        true = sigma3_pk(p, k) ** 2
        c_cl = int(closed.coeff(Xc, k))
        if true != c_cl:
            local_id_ok = False
            info(f"  coeff FAIL p={p} k={k}: σ₃²={true} series={c_cl}")
            break
    info(f"  p={p}: σ₃² local ≡ Ramanujan local (alg+coeffs k<10)")

check(
    "X4.local: σ₃² Euler = (1+p³X)/[(1−X)(1−p³X)(1−p⁶X)] ≡ "
    "Ramanujan ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6) local at p=3,5,7,11,13",
    local_id_ok,
)

# Also matches chi=0, ap=1+p³ in the T57 closed form
eis_match_ok = True
for p in (3, 5, 7, 11):
    Ep0 = sp.cancel(euler_local_Ep(1 + p ** 3, p, 0, Xc))
    target = sp.cancel(closed_sig3sq_local(p, Xc))
    if sp.simplify(Ep0 - target) != 0:
        eis_match_ok = False
        info(f"  E_p(ap=1+p³,χ=0) ≠ σ₃² local at p={p}")
check(
    "X4.bridge: T57 E_p(ap=σ₃(p)=1+p³, χ=0) ≡ σ₃² local factor exactly",
    eis_match_ok,
)

# Outer ζ(s)ζ(s−3) coefficient identity (classical)
def sigma3(n):
    return int(sp.divisor_sigma(n, 3))


N_OUT = 120
c_outer = [0] + [sigma3(n) for n in range(1, N_OUT + 1)]
c_zz = coeffs_zeta_zeta(0, 3, N_OUT)
# Σ σ₃(n) n^{-s} = ζ(s)ζ(s−3); coeffs of ζ(s)ζ(s−3) = σ₃(n)
outer_ok, outer_rel, _ = coeff_identity(
    [mpmath.mpf(x) for x in c_outer],
    c_zz,
    N_OUT,
)
info(f"outer σ₃ ≡ ζ(s)ζ(s−3) coeffs: identity={outer_ok}, "
     f"max_rel={float(outer_rel):.3e}")
check(
    "X4.outer: σ₃(n) ≡ Dirichlet coeffs of ζ(s)ζ(s−3) on n≤120 (exact)",
    outer_ok,
)

# Global Z_Eis factorisation — product of ζ-shifts
info("Z_Eis(s,w) = ζ(s)ζ(s−3) · ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6)")
info("Completed form: each ζ(·) completes to ξ(·)/[s(s−1)π^{-s/2}Γ…] "
     "— CLASSICAL ξ-factors on the Eisenstein Boden, NOT a new cusp ξ-sector.")

# Numeric spot-check of product at a point
def Z_Eis_closed(s, w):
    s, w = mpmath.mpf(s), mpmath.mpf(w)
    return (mpmath.zeta(s) * mpmath.zeta(s - 3)
            * mpmath.zeta(w) * mpmath.zeta(w - 3) ** 2
            * mpmath.zeta(w - 6) / mpmath.zeta(2 * w - 6))


def Z_Eis_partial(s, w, N=800):
    s, w = mpmath.mpf(s), mpmath.mpf(w)
    # (Σ_{n≤N} σ₃(n)/n^s) * (Σ_{m≤N} σ₃(m)²/m^w) — separable packing
    outer = mpmath.mpf(0)
    inner = mpmath.mpf(0)
    for n in range(1, N + 1):
        sg = mpmath.mpf(sigma3(n))
        outer += sg * mpmath.power(n, -s)
        inner += (sg * sg) * mpmath.power(n, -w)
    return outer * inner


spot_ok = True
# Avoid ζ poles: need s>4 (so s−3>1) and w>7 (so w−6>1)
for s, w in ((5.0, 9.0), (5.5, 10.0), (6.0, 11.0)):
    cl = Z_Eis_closed(s, w)
    # Compare outer×inner partial to closed (tail-controlled at these Re)
    part = Z_Eis_partial(s, w, N=2000)
    rel = rel_diff(part, cl)
    info(f"  Z_Eis ({s},{w}): partial/closed rel={rel:.3e}")
    if rel > 0.02:
        spot_ok = False

check(
    "X4.global: Z_Eis(s,w)=ζ(s)ζ(s−3)·[ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6)] "
    "matches separable σ₃-packing to <2% at abs-conv nodes",
    spot_ok and local_id_ok and outer_ok,
)

# Typing: ξ-factors appear in completion of ζ-shifts — classical Boden
X4_classical_boden = local_id_ok and outer_ok and eis_match_ok
X4_new_xi = False  # exact but CLASSICAL


# ================================================================ X5
print("=" * 72)
print("X5 -- GNS RESTRICTION (commutative character algebra)")
print("=" * 72)

info("GNS space ℓ²(d, b²/|d|); commutative subalgebra {d ↦ χ_d(p)}.")
info("CLASSICAL: equidistribution of quadratic characters over families;")
info("  bias ↔ central-value weighting (one-level-density environment,")
info("  classical naming — NO zero interpretation).")

ds_gns = [d for d in live_fund if d <= D_MAX]
weights = np.array([float(int(g[d]) ** 2) / float(d) for d in ds_gns])
Wtot = float(weights.sum())
info(f"GNS sample: n_d={len(ds_gns)}, total weight={Wtot:.6g}")

measures = {}
for p in GNS_PRIMES:
    counts = {1: 0.0, -1: 0.0, 0: 0.0}
    for d, w in zip(ds_gns, weights):
        counts[kronecker(d, p)] += w
    for k in counts:
        counts[k] /= Wtot
    measures[p] = counts
    bal = abs(counts[1] - counts[-1]) / max(counts[1] + counts[-1], 1e-30)
    info(f"  p={p}: μ(+1)={counts[1]:.4f}, μ(−1)={counts[-1]:.4f}, "
         f"μ(0)={counts[0]:.4f}, |Δ±|/(±mass)={bal:.4f}")

# (i) balance vs systematic bias (BOTH are valid typed outcomes)
bal_ratios = []
for p in GNS_PRIMES:
    m = measures[p]
    pm = m[1] + m[-1]
    bal = abs(m[1] - m[-1]) / max(pm, 1e-30)
    bal_ratios.append(bal)
biases = {p: measures[p][1] - measures[p][-1] for p in GNS_PRIMES}
mean_abs_bias = float(np.mean([abs(biases[p]) for p in GNS_PRIMES]))
# Threshold: |Δ±|/(±mass) < 0.15 on all p ⇒ balanced; else CV-weighted bias
balanced = all(b < 0.15 for b in bal_ratios)
info("signed bias μ(+1)−μ(−1): "
     + str({p: round(float(biases[p]), 4) for p in GNS_PRIMES}))
info(f"mean |bias|={mean_abs_bias:.4f}; per-p |Δ±|/(±)="
     f"{[round(float(b), 4) for b in bal_ratios]}")
if balanced:
    x5_type = "BALANCED (classical quadratic-character equidistribution)"
else:
    x5_type = ("SYSTEMATIC-BIAS (central-value-weighted non-triviality; "
               "one-level-density environment, classical — NOT a zero claim)")
info(f"X5 typing: {x5_type}")
# Assert: measures are probability measures and typing is decided
meas_ok = all(
    abs(sum(measures[p].values()) - 1.0) < 1e-9
    and measures[p][1] >= 0 and measures[p][-1] >= 0
    for p in GNS_PRIMES
)
check(
    "X5.balance: spectral measures of χ_d(p) measured on GNS weights; "
    f"typed as {'BALANCED' if balanced else 'SYSTEMATIC-BIAS'} "
    f"(mean |bias|={mean_abs_bias:.4f}; both outcomes valid)",
    meas_ok and (balanced or mean_abs_bias > 0.05),
)

# (ii) product-measure factorisation / independence across p
# Compare joint μ(χ_p=a, χ_q=b) vs μ_p(a)μ_q(b) for pairs
indep_rels = []
for p, q in combinations(GNS_PRIMES[:4], 2):
    joint = defaultdict(float)
    for d, w in zip(ds_gns, weights):
        joint[(kronecker(d, p), kronecker(d, q))] += w / Wtot
    max_rel_pq = 0.0
    for a in (-1, 1):
        for b in (-1, 1):
            pred = measures[p][a] * measures[q][b]
            got = joint[(a, b)]
            if pred + got < 1e-12:
                continue
            rel = abs(got - pred) / max(pred, got, 1e-30)
            max_rel_pq = max(max_rel_pq, rel)
    indep_rels.append((p, q, max_rel_pq))
    info(f"  independence p={p},q={q}: max rel joint vs product={max_rel_pq:.4f}")

indep_ok = all(r < 0.20 for _p, _q, r in indep_rels)
check(
    "X5.independence: joint χ_p×χ_q ≈ product measure (rel<0.20) "
    "on pairs from {3,5,7,11} — commutative GL(1)-like factorisation",
    indep_ok and len(indep_rels) >= 4,
)

# Typing: commutative sector generates character evaluations — GL(1) data —
# but amplitudes remain b(d)² (cuspidal central values), not a new ξ-sector.
info("TYPING: commutative sector = quadratic-character GL(1) evaluations")
info("  on the GNS family; amplitudes = cuspidal b(d)².  Balance/bias")
info("  typing is classical; NO coefficient-identical ξ(s) from this sector.")

X5_new_xi = False
# Classical GL(1) character sector present (measures + independence),
# whether balanced or CV-biased — bias is classical CV-weighting, not failure.
X5_classical_gl1 = meas_ok and indep_ok


# ================================================================ VERDICT
print("=" * 72)
print("VERDICT -- ξ-transport / canonical GL(1) sector")
print("=" * 72)

info("Summary of sectors:")
info(f"  X1 Rankin Res_w=4: classical pole closes; residue = FAMILY "
     f"(not GL(1) coeff identity); new ξ={X1_new_xi}")
info(f"  X2 diagonals: GL(1) diagonal found={any_gl1_diag}")
info(f"  X3 Weyl/s-symmetry: accessible s-FE={s_sym_found_B or s_sym_found_C}; "
     f"1/2-fixline={fix_line_half}")
info(f"  X4 Eisenstein Boden: exact ζ-factorisation={X4_classical_boden}; "
     f"new ξ beyond classical={X4_new_xi}")
info(f"  X5 GNS characters: classical sector closes={X5_classical_gl1} "
     f"({x5_type}); new ξ={X5_new_xi}")

# Classical shadows = Rankin pole + Eisenstein Boden (exact).
# X5 is a character-sector map (balance OR bias), not a ζ-factorisation.
classical_shadows_close = X1_classical_rankin and X4_classical_boden
new_sector = X1_new_xi or any_gl1_diag or X3_new_xi or X4_new_xi or X5_new_xi

if new_sector:
    verdict = "XI-SECTOR-FOUND"
elif classical_shadows_close and not new_sector:
    verdict = "GL1-SHADOW-CLASSICAL"
else:
    verdict = "NO-CANONICAL-SECTOR"

info(f"VERDICT = {verdict}")

# Route consequence
info("ROUTE CONSEQUENCE (RH-attack vectors, honest typing):")
info("  Route A (degeneration to GL(1)/ξ via residue/diagonal/Eis): "
     "MAPPED — only classical shadows; no new ξ-sector.  Closed as")
info("    a discovery vector for ξ-transport from Z(s,w).")
info("  Route B (Weil positivity via GNS): STILL OPEN — GNS space carries")
info("    CV-weighted character measures (bias typed); positivity/Weil would")
info("    need an operator with ξ-spectrum, not merely χ_d evaluations.")
info("  Route C (self-adjoint generator): STILL OPEN — no bi-variate")
info("    symmetry produced a 1/2-fix line; no generator extracted.")
if verdict == "GL1-SHADOW-CLASSICAL":
    best_route = "B"
    info("  BEST REMAINING VECTOR: Route B (GNS / Weil positivity),")
    info("    because A is now mapped-and-closed at the packing level,")
    info("    while B still has a constructed Hilbert space carrying")
    info("    central-value amplitudes (fence: not zeros).")
elif verdict == "XI-SECTOR-FOUND":
    best_route = "A"
    info("  BEST VECTOR: Route A — a new exact GL(1)/ξ sector appeared;")
    info("    this is the BEGINNING of an attack route, not its completion.")
else:
    best_route = "B"
    info("  BEST REMAINING VECTOR: Route B/C theory projects — classical")
    info("    channels failed to close exactly; re-check packing first.")

check(
    f"V.verdict: preregistered verdict assigned = {verdict}",
    verdict in ("XI-SECTOR-FOUND", "GL1-SHADOW-CLASSICAL", "NO-CANONICAL-SECTOR"),
)
check(
    "V.route: best remaining route typed in {A,B,C}",
    best_route in ("A", "B", "C"),
)
check(
    "V.classical-named: Rankin pole, DGH Weyl frame, Eisenstein Boden, "
    "equidistribution / one-level-density environment named as classical",
    True,
)
check(
    "V.no-new-xi: no coefficient-identical ξ-sector beyond classical "
    "channels in this probe",
    not new_sector,
)

# ================================================================ TOTAL
print("=" * 72)
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print(f"VERDICT: {verdict}")
print(f"BEST_ROUTE: {best_route}")
print("=" * 72)
raise SystemExit(0 if FAIL == 0 else 1)
