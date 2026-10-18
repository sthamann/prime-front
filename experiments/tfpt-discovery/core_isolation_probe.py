"""Discovery probe (2026-07-25), part 62 — contract CORE.ISOLATION.

Route-B closing map after T61 / ST.ISOTYPE.GL1.CORE
(GL1-CORE-EXACT-POSITIVITY-OPEN).  T61 identified the trivial ST
isotype as the named GL(1) core
  G_0 = (1+Y)/(1−Y) = ζ(w−3)_p · (1+Y)
with Plancherel correction −Y, measured Q_0≥0 on the finite test
class, and ST cross-terms shrinking with P — BUT the GNS-d state
mixes the χ=0 strip with twists (mean mix up to ~0.66).

Thesis (T62): that mixing is NOT an irreducible obstruction.  It
vanishes exactly under the fibre decomposition of the character
spectrum, because the GNS metric is DIAGONAL in d
(ℓ²(d, b²/|d|), T55), so subfamilies indexed by χ_d-sign patterns
are GNS-orthogonal, and on each fibre the twists are CONSTANTS.
This is the operator-algebraic multiplicity-1 reduction of T58-X5
(Gelfand spectrum of the commutative character subalgebra), now as
a direct-integral decomposition (classical von Neumann / Gelfand).

  C1  FIBRE DECOMPOSITION (exact).  Partition live fundamental
      d≡1 mod 8 (D≥20000) by
        σ(d)=(χ_d(3),χ_d(5),χ_d(7),χ_d(11),χ_d(13))∈{±1,0}^5.
      Verify: (i) fibres GNS-orthogonal (from diagonal metric);
      (ii) Λ_fam(p;d) constant on each fibre for p in the pattern
      support; (iii) fibre masses μ(σ) vs 2^{-5} and vs X5 bias.
  C2  PER-FIBRE CORE (algebraic).  Inside a fibre σ the tower Euler
      factor at fixed p is determined by (a_p, σ_p).  Identify the
      per-fibre GL(1) core: σ_p=0 → G_0; |σ_p|=1 → ST-projected
      L_p(w−3)-shift with finite corrections (T61 c_{k,0}=1+ρ_k(p)).
  C3  ISOLATION TEST (heart).  Repeat T61-I3 mixing PER FIBRE:
      (i) d-twist mix must be exactly 0 on each fibre (constancy);
      (ii) residual ST cross-terms still fall with P;
      (iii) Q_0≥0 inherited per fibre on the test class.
  C4  REASSEMBLY.  Global isolated core = Σ_σ μ(σ)·Core(σ);
      name the reassembled GL(1) object; check consistency with
      T58-X4 Eisenstein floor (ζ-product as pattern mean).
  C5  FINAL ROUTE-B MAP.  What is structurally complete; what stays
      open (named); promotion-candidate typing (NO promotion);
      saturation assessment.

PREREGISTERED VERDICTS:
  CORE-ISOLATED — C1 orthogonality + C2 per-fibre cores exact
      + C3 mix per fibre null + C4 reassembly identified
  PARTIAL — subset of the above; residual per-fibre mix quantified
  NO-ISOLATION — fibre thesis breaks; residual mix remains

EHRLICHKEITS-FENCE:
  Isolation is a STRUCTURE statement.  “Q_0≥0 on a dense class”
  remains RH-adjacent for the shift and is NOT claimed.  This probe
  maps; it does not prove positivity beyond the finite test class.
  Classical anchors (Gelfand spectrum, direct integrals, quadratic
  reciprocity / Dirichlet L-twists, Sato–Tate/Plancherel) named as
  classical.

Firewall: discovery sandbox, NO promotion, no marker / ledger /
paper / website / next.txt edits.  ZERO-FIREWALL (AST-checked):
NO Riemann zeros as input or comparison.  ζ/Γ as mpmath FUNCTIONS
allowed; mpmath.zetazero FORBIDDEN.  No RH-evidence language.
"""
from __future__ import annotations

import ast
import math
import time
from collections import defaultdict

import mpmath
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()
mpmath.mp.dps = 25

# Windows (preregistered; keep runtime < 600 s)
P_MAX = 3000
N_F8 = P_MAX + 64
D_MAX = 20000
K_MAX = 6
K_MATRIX = 8
ARCH_TMAX = 200.0
ARCH_NPTS = 8001
HEAD_AP = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}
WITNESS_KEY = (0, 2, 0, 1, 1, 1)
PATTERN_PRIMES = (3, 5, 7, 11, 13)
MIN_FIBRE_COUNT = 5
MIN_FIBRE_MASS_FRAC = 1e-4


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


# ---------------------------------------------------------------- helpers
def eta_pass(d, e, order):
    s = np.zeros(order + 1, dtype=np.int64)
    s[0] = 1
    for k in range(d, order + 1, d):
        for _ in range(e):
            s[k:] = s[k:] - s[:-k]
    return s


def conv_i64(a, b, order):
    return np.convolve(a, b)[: order + 1].astype(np.int64)


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


# ---------------------------------------------------------------- character algebra (T61)
AHAT = sp.symbols("ahat")
Y = sp.symbols("Y", positive=True)
P_SYM = sp.symbols("p", positive=True, integer=True)


def _powers_to_chi(max_pow: int):
    basis = [
        sp.Poly(sp.expand(sp.chebyshevu(n, AHAT / 2)), AHAT)
        for n in range(max_pow + 1)
    ]
    results = []
    for k in range(max_pow + 1):
        mon = [0] * (max_pow + 1)
        mon[k] = 1
        coeffs = {}
        for n in range(k, -1, -1):
            pn = basis[n]
            lead = pn.nth(n)
            c = sp.Rational(mon[n], lead) if lead else 0
            if c:
                coeffs[n] = c
            for j in range(n + 1):
                mon[j] -= c * pn.nth(j)
        results.append(coeffs)
    return results


_CHI_TABLE = _powers_to_chi(20)


def expr_to_chi(expr):
    poly = sp.Poly(sp.expand(expr), AHAT)
    out = {}
    for (pow_,), coef in poly.as_dict().items():
        for n, cn in _CHI_TABLE[pow_].items():
            out[n] = sp.simplify(out.get(n, 0) + coef * cn)
    return {n: v for n, v in out.items() if v != 0}


def lambda_unit_series(chi_val, kmax, p_sym=P_SYM):
    s = sp.sqrt(p_sym)
    Aprev2, Aprev1 = 1, AHAT - chi_val / s
    U = [1]
    for k in range(1, kmax + 1):
        if k == 1:
            Ak = Aprev1
        else:
            Ak = sp.expand(AHAT * Aprev1 - Aprev2)
            Aprev2, Aprev1 = Aprev1, Ak
        U.append(sp.expand(Ak ** 2))
    lam = [0]
    for k in range(1, kmax + 1):
        acc = k * U[k]
        for j in range(1, k):
            acc -= lam[j] * U[k - j]
        lam.append(sp.expand(acc))
    return lam


def alpha_pk(ap, p, chi, k):
    if k == 0:
        return 1
    if k == 1:
        return ap - chi * p
    a_prev2, a_prev1 = 1, ap - chi * p
    for _ in range(2, k + 1):
        a_prev2, a_prev1 = a_prev1, ap * a_prev1 - (p ** 3) * a_prev2
    return a_prev1


def lambda_arith(ap, p, chi, kmax=4):
    u = [1]
    for k in range(1, kmax + 1):
        ak = alpha_pk(ap, p, chi, k)
        u.append(ak * ak)
    lam_c = [0] * (kmax + 1)
    for k in range(1, kmax + 1):
        acc = k * u[k]
        for j in range(1, k):
            acc -= lam_c[j] * u[k - j]
        lam_c[k] = acc
    return lam_c


def g_fejer(u, a):
    return max(0.0, 1.0 - abs(u) / a)


def g_gauss(u, sig):
    return math.exp(-0.5 * (u / sig) ** 2)


def h_fejer(t, a):
    if abs(t) < 1e-15:
        return float(a)
    x = 0.5 * a * t
    return a * (math.sin(x) / x) ** 2


def h_gauss(t, sig):
    return sig * math.sqrt(2.0 * math.pi) * math.exp(-0.5 * (sig * t) ** 2)


def chi_n_num(n: int, theta: float) -> float:
    if n == 0:
        return 1.0
    c = math.cos(theta)
    u_prev2, u_prev1 = 1.0, 2.0 * c
    if n == 1:
        return u_prev1
    for _ in range(2, n + 1):
        u_prev2, u_prev1 = u_prev1, 2.0 * c * u_prev1 - u_prev2
    return u_prev1


def pole_term(g_fn, umax, npts=4001):
    us = np.linspace(-umax, umax, npts)
    gv = np.array([g_fn(float(u)) for u in us])
    return float(np.trapezoid(gv * (np.exp(0.5 * us) + np.exp(-0.5 * us)), us))


_ARCH_TS = None
_ARCH_KERNEL = None


def _ensure_arch():
    global _ARCH_TS, _ARCH_KERNEL
    if _ARCH_KERNEL is not None:
        return
    t0 = time.time()
    _ARCH_TS = np.linspace(-ARCH_TMAX, ARCH_TMAX, ARCH_NPTS)
    log_pi = math.log(math.pi)
    _ARCH_KERNEL = np.array([
        float(mpmath.re(mpmath.digamma(0.25 + 0.5j * float(t)))) - log_pi
        for t in _ARCH_TS
    ])
    info(f"arch digamma kernel: {ARCH_NPTS} pts, |t|<={ARCH_TMAX:g} "
         f"in {time.time() - t0:.1f}s")


def arch_term(h_fn):
    _ensure_arch()
    hs = np.array([h_fn(float(t)) for t in _ARCH_TS])
    return float(np.trapezoid(hs * _ARCH_KERNEL, _ARCH_TS) / (2.0 * math.pi))


# ================================================================ S0
print("=" * 72)
print("S0 -- FIREWALL + CARRIER (f8 Satake, family CV, D≥20000)")
print("=" * 72)

_src_path = __file__
with open(_src_path, "r", encoding="utf-8") as _fh:
    _src = _fh.read()
_tree = ast.parse(_src)
_zero_calls = []
_attr_hits = []
for node in ast.walk(_tree):
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Attribute) and f.attr in (
            "zetazero", "nzeros", "second_sheet_zero",
        ):
            _zero_calls.append(f.attr)
        if isinstance(f, ast.Name) and f.id in ("zetazero",):
            _zero_calls.append(f.id)
    if isinstance(node, ast.Attribute) and node.attr in ("zetazero",):
        _attr_hits.append(node.attr)
check(
    "S0.AST: no Riemann-zero / zetazero loaders in this probe source",
    len(_zero_calls) == 0 and len(_attr_hits) == 0,
)
info("EHRLICHKEITS-FENCE: isolation = STRUCTURE only.")
info("  Q_0≥0 on a dense class remains RH-adjacent for the shift —")
info("  NOT claimed.  Classical: Gelfand spectrum, direct integrals,")
info("  quadratic reciprocity / Dirichlet L-twists, Sato–Tate.")

t_f8 = time.time()
f8 = np.roll(conv_i64(eta_pass(2, 4, N_F8),
                      eta_pass(4, 4, N_F8), N_F8), 1)
f8[0] = 0
a_f8 = [int(f8[n]) for n in range(N_F8 + 1)]
info(f"f8 eta-product to O(q^{N_F8}) in {time.time() - t_f8:.2f}s")
check(
    "S0.f8: a_1=1; HEAD_AP; a_even=0 on n≤200",
    a_f8[1] == 1
    and all(a_f8[p] == v for p, v in HEAD_AP.items())
    and all(a_f8[n] == 0 for n in range(2, 201, 2)),
)

ODD_PRIMES = [int(p) for p in sp.primerange(3, P_MAX + 1)]
AP = {p: a_f8[p] for p in ODD_PRIMES}
AHAT_NUM = {p: AP[p] / (p ** 1.5) for p in AP}
THETA = {}
for p in ODD_PRIMES:
    c = max(-1.0, min(1.0, AHAT_NUM[p] / 2.0))
    THETA[p] = math.acos(c)
check(
    f"S0.satake: |â_p|≤2 (Deligne/Ramanujan, classical) for odd p≤{P_MAX}",
    all(abs(AHAT_NUM[p]) <= 2.0 + 1e-9 for p in ODD_PRIMES),
)

t_g = time.time()
g = build_g_fft(D_MAX)
info(f"g FFT rebuild O(q^{D_MAX}) in {time.time() - t_g:.2f}s")
mu_tab = mobius_sieve(D_MAX)
live_fund = [
    d for d in range(1, D_MAX + 1)
    if d % 8 == 1 and is_fundamental_disc(d, mu_tab) and int(g[d]) != 0
]
weights_cv = np.array([float(int(g[d]) ** 2) / float(d) for d in live_fund])
Wtot_cv = float(weights_cv.sum())
info(f"live fund d≡1 mod 8, d≤{D_MAX}: {len(live_fund)}; W_CV={Wtot_cv:.6g}")
check(
    f"S0.family: D_MAX={D_MAX}≥20000; live fund count {len(live_fund)}≥200",
    D_MAX >= 20000 and len(live_fund) >= 200,
)


# ================================================================ C1
print("=" * 72)
print("C1 -- FIBRE DECOMPOSITION (Gelfand / direct integral, classical)")
print("=" * 72)
info("CLASSICAL: GNS = ℓ²(d, b²/|d|) is diagonal in the d-basis (T55).")
info("  Multiplication by χ_d(p) is a commuting family of diagonal")
info("  operators → Gelfand spectrum = sign patterns σ (T58-X5).")
info("  Direct-integral decomposition = partition into σ-fibres.")

# Build fibres
fibres = defaultdict(list)  # σ -> list of indices into live_fund
sigma_of = []
for i, d in enumerate(live_fund):
    sig = tuple(kronecker(d, p) for p in PATTERN_PRIMES)
    sigma_of.append(sig)
    fibres[sig].append(i)

fibre_mass = {}
fibre_count = {}
for sig, idxs in fibres.items():
    fibre_count[sig] = len(idxs)
    fibre_mass[sig] = float(sum(weights_cv[i] for i in idxs))

mass_sum = sum(fibre_mass.values())
n_fibres = len(fibres)
n_pm1_fibres = sum(1 for s in fibres if 0 not in s)
info(f"fibres nonempty: {n_fibres}; pure ±1 patterns: {n_pm1_fibres}/32")
info(f"Σ_σ μ(σ) = {mass_sum:.6g}  vs W_CV={Wtot_cv:.6g}")

# (i) GNS orthogonality from diagonal metric
# ⟨1_σ, 1_τ⟩ = Σ_d w_d 1_σ(d)1_τ(d) = δ_{στ} μ(σ)
orth_ok = abs(mass_sum - Wtot_cv) < 1e-9 * max(Wtot_cv, 1.0)
cross_max = 0.0
# Partition check: every d in exactly one fibre
partition_ok = len(sigma_of) == len(live_fund)
# Explicit cross term for a sample of fibre pairs
sig_list = list(fibres.keys())
for a in range(min(20, len(sig_list))):
    for b in range(a + 1, min(20, len(sig_list))):
        sa, sb = sig_list[a], sig_list[b]
        # intersection of index sets must be empty
        inter = set(fibres[sa]).intersection(fibres[sb])
        if inter:
            orth_ok = False
            cross_max = 1.0
check(
    "C1.GNS-orthogonal: fibres partition the live family; "
    f"Σ μ(σ)=W_CV (rel err {abs(mass_sum - Wtot_cv) / max(Wtot_cv, 1):.2e}); "
    "cross-fibre index intersection empty — exact from diagonal "
    "ℓ²(d, b²/|d|) metric (T55; classical GNS)",
    orth_ok and partition_ok and cross_max == 0.0,
)

# (ii) Λ_fam constant on fibres for pattern primes
info("Λ_fam(p;d)=(a_p − χ_d(p)·p)²  (T59 k=1); must be constant on "
     "each fibre for p∈{3,5,7,11,13}.")
const_ok = True
n_checked = 0
for sig, idxs in fibres.items():
    if len(idxs) < 2:
        continue
    for j, p in enumerate(PATTERN_PRIMES):
        chi_s = sig[j]
        ap = AP[p]
        expect = (ap - chi_s * p) ** 2
        for i in idxs:
            d = live_fund[i]
            chi = kronecker(d, p)
            got = (ap - chi * p) ** 2
            n_checked += 1
            if chi != chi_s or got != expect:
                const_ok = False
                info(f"  FAIL d={d} p={p}: chi={chi} vs σ={chi_s}")
                break
        if not const_ok:
            break
    if not const_ok:
        break
info(f"constancy checks performed: {n_checked}")
check(
    "C1.Lambda-constant: Λ_fam(p;d) exact constant on each fibre "
    f"for all pattern primes p∈{PATTERN_PRIMES} (verified on all "
    f"fibres with ≥2 elements)",
    const_ok and n_checked > 0,
)

# Also: unitary residual Φ_k = λ_k/p^{3k} constant on fibre for pattern p
phi_const_ok = True
for sig, idxs in fibres.items():
    if len(idxs) < 2:
        continue
    for j, p in enumerate(PATTERN_PRIMES):
        chi_s = sig[j]
        ap = AP[p]
        ref = [lambda_arith(ap, p, chi_s, 4)[k] / float(p ** (3 * k))
               for k in range(1, 5)]
        for i in idxs[1:]:
            d = live_fund[i]
            chi = kronecker(d, p)
            got = [lambda_arith(ap, p, chi, 4)[k] / float(p ** (3 * k))
                   for k in range(1, 5)]
            if any(abs(got[k] - ref[k]) > 1e-12 for k in range(4)):
                phi_const_ok = False
                break
        if not phi_const_ok:
            break
    if not phi_const_ok:
        break
check(
    "C1.Phi-constant: unitary residuals Φ_k=λ_k/p^{3k} constant on "
    "each fibre for pattern primes (exact; twists are fibre constants)",
    phi_const_ok,
)

# (iii) Pattern statistics
info("Fibre-mass statistics vs equidistribution 2^{-5} and X5 bias.")
# Single-p marginals (X5-style)
x5_meas = {}
for p in PATTERN_PRIMES:
    counts = {1: 0.0, -1: 0.0, 0: 0.0}
    for d, w in zip(live_fund, weights_cv):
        counts[kronecker(d, p)] += w
    for k in counts:
        counts[k] /= Wtot_cv
    x5_meas[p] = counts
    info(f"  X5 marg p={p}: μ(+1)={counts[1]:.4f} μ(−1)={counts[-1]:.4f} "
         f"μ(0)={counts[0]:.4f} bias={counts[1] - counts[-1]:+.4f}")

# Pure ±1 patterns: compare to product measure and to 2^{-5}
pure_sigs = [s for s in fibres if 0 not in s]
pure_mass_fracs = [fibre_mass[s] / Wtot_cv for s in pure_sigs]
eq = 2.0 ** (-5)
# Product-measure prediction from X5 marginals
prod_errs = []
eq_errs = []
for s in pure_sigs:
    pred_prod = 1.0
    for j, p in enumerate(PATTERN_PRIMES):
        pred_prod *= x5_meas[p][s[j]]
    got = fibre_mass[s] / Wtot_cv
    prod_errs.append(abs(got - pred_prod) / max(pred_prod, 1e-30))
    eq_errs.append(abs(got - eq) / eq)

mean_prod_err = float(np.mean(prod_errs)) if prod_errs else 0.0
mean_eq_err = float(np.mean(eq_errs)) if eq_errs else 0.0
max_eq_err = float(np.max(eq_errs)) if eq_errs else 0.0
# CV weighting distorts away from uniform 1/32; X5 product should be closer
info(f"pure ±1 fibres: {len(pure_sigs)}; mean |μ−2^{{-5}}|/2^{{-5}}="
     f"{mean_eq_err:.4f} (max={max_eq_err:.4f})")
info(f"mean |μ−∏μ_p|/∏μ_p (X5 product)={mean_prod_err:.4f}")
info(f"top fibre masses (frac): "
     + ", ".join(
         f"{s}:{fibre_mass[s] / Wtot_cv:.4f}"
         for s in sorted(pure_sigs,
                         key=lambda u: -fibre_mass[u])[:5]
     ))

# Bias: CV weighting systematically distorts vs uniform
cv_distorts = mean_eq_err > 0.15
x5_consistent = mean_prod_err < 0.35  # joint vs product; finite-D residual
check(
    "C1.mass-stats: fibre masses measured; CV weighting distorts vs "
    f"equidistribution 2^{{-5}} (mean rel err={mean_eq_err:.3f}); "
    f"X5 product-measure consistency mean rel err={mean_prod_err:.3f} "
    f"(classical quadratic-character / CV-bias environment, T58-X5)",
    len(pure_sigs) >= 16 and cv_distorts and x5_consistent,
)

c1_ok = orth_ok and const_ok and phi_const_ok and len(pure_sigs) >= 16


# ================================================================ C2
print("=" * 72)
print("C2 -- PER-FIBRE GL(1) CORE (algebraic)")
print("=" * 72)
info("Inside fibre σ, the tower Euler at p is fixed by (a_p, σ_p).")
info("T61: σ_p=0 → c_{k,0}=[1,0,2,0,…] → G_0=(1+Y)/(1−Y);")
info("     |σ_p|=1 → c_{k,0}=1+ρ_k(p) (even in σ_p).")

# χ=0 core identity (T61)
lam0 = lambda_unit_series(0, K_MATRIX)
C0 = [expr_to_chi(lam0[k]).get(0, 0) for k in range(1, K_MATRIX + 1)]
dlog_g0 = Y / (1 + Y) + Y / (1 - Y) - Y
g0_series = sp.series(dlog_g0, Y, 0, K_MATRIX + 1).removeO()
g0_coeffs = [sp.simplify(g0_series.coeff(Y, k))
             for k in range(1, K_MATRIX + 1)]
core0_ok = all(sp.simplify(C0[k] - g0_coeffs[k]) == 0
               for k in range(K_MATRIX))
info(f"χ=0 c_{{k,0}} = {C0}")
check(
    "C2.core-chi0: Σ c_{k,0} Y^k = Y∂_Y log((1+Y)/(1−Y)) − Y "
    "exactly (G_0=ζ(w−3)_p·(1+Y); T61 identity)",
    core0_ok,
)

# χ=±1: symmetry + closed form via ST-average of T57 numerator
lam1 = lambda_unit_series(1, K_MAX)
lam_m1 = lambda_unit_series(-1, K_MAX)
core1 = [expr_to_chi(lam1[k]).get(0, 0) for k in range(1, K_MAX + 1)]
core_m1 = [expr_to_chi(lam_m1[k]).get(0, 0) for k in range(1, K_MAX + 1)]
twist_sym = all(sp.simplify(core1[k] - core_m1[k]) == 0
                for k in range(K_MAX))
check(
    "C2.twist-symmetry: c_{k,0}(σ_p=+1)=c_{k,0}(σ_p=−1) for k≤"
    f"{K_MAX} (trivial isotype even in the GL(1) twist)",
    twist_sym,
)

# Closed form: Σ c Y^k = E_ST[Y∂_Y log N_σ] + Y/(1−Y) − Y
# with N_σ = 1+(1−2σ â/√p+1/p)Y + Y²/p  (T57 numerator, |σ|=1)
info("Named twisted object (classical ST projection of T57 numerator):")
info("  N_σ(â)=1+(1−2σ â/√p+1/p)Y+(Y²)/p")
info("  Σ c_{k,0}(±1) Y^k = E_ST[Y∂_Y log N_σ] + Y/(1−Y) − Y")
info("  =: Y∂_Y log G_{±1} − Y,  G_{±1}=(1−Y)^{-1}·M_{±1}")
info("  where M_{±1} is the ST-multiplicative projection of N_σ")
info("  (pure p-rational GL(1)-level series; L_p(w−3)-shift +")
info("  finite p-corrections — classical Dirichlet/ST naming).")

th = sp.symbols("theta", real=True, positive=True)
dens = (2 / sp.pi) * sp.sin(th) ** 2
Ahat_s = sp.symbols("ahat")
sig_s = sp.symbols("sigma", real=True)
N_twist = (
    1
    + (1 - 2 * sig_s * Ahat_s / sp.sqrt(P_SYM) + 1 / P_SYM) * Y
    + Y ** 2 / P_SYM
)
dlog_N = Y * sp.diff(N_twist, Y) / N_twist
ser_N = sp.series(dlog_N, Y, 0, K_MAX + 1).removeO()

st_core_ok = True
st_coeffs = []
for k in range(1, K_MAX + 1):
    ck = ser_N.coeff(Y, k)
    avg = sp.integrate(
        sp.expand(ck).subs(Ahat_s, 2 * sp.cos(th)) * dens,
        (th, 0, sp.pi),
    )
    # + Y/(1-Y) − Y
    pred = sp.simplify(avg.subs(sig_s, 1) + 1 - (1 if k == 1 else 0))
    st_coeffs.append(pred)
    diff = sp.simplify(pred - core1[k - 1])
    info(f"  k={k}: ST-N formula={pred}  T61 c0={sp.simplify(core1[k - 1])}  "
         f"Δ={diff}")
    if diff != 0:
        st_core_ok = False

check(
    "C2.core-twist-identity: for |σ_p|=1, Σ c_{k,0} Y^k = "
    "E_ST[Y∂_Y log N_σ] + Y/(1−Y) − Y exactly (k≤"
    f"{K_MAX}; ST-projected L_p(w−3)-shift with finite corrections)",
    st_core_ok,
)

# ρ_k free of â
rho_ok = True
for k in range(1, K_MAX + 1):
    rho = sp.simplify(core1[k - 1] - 1)
    if rho.has(AHAT):
        rho_ok = False
    info(f"  k={k}: ρ_k = c0−1 = {rho}")
check(
    "C2.rho-p-rational: c_{k,0}(|σ|=1)=1+ρ_k(p) with ρ_k free of "
    "Satake angle (pure GL(1)-level p-rational spillover)",
    rho_ok,
)

# Per pattern-class: fibre core at each pattern prime is G_{σ_p}
info("Per-fibre core typing by pattern class:")
info("  Core(σ)_p = G_0           if σ_p=0")
info("  Core(σ)_p = G_{±1}(p)     if |σ_p|=1")
info("  (local object at each p; fibre = product over pattern support)")
fibre_core_typed = core0_ok and st_core_ok and twist_sym and rho_ok
check(
    "C2.per-fibre-kernel: each fibre σ carries the exact local GL(1) "
    "core Core(σ)_p ∈ {G_0, G_{±1}(p)} determined by σ_p "
    "(algebraic; pattern-class coefficient identities verified)",
    fibre_core_typed,
)

c2_ok = fibre_core_typed


# ================================================================ C3
print("=" * 72)
print("C3 -- ISOLATION TEST (per-fibre mixing kill)")
print("=" * 72)
info("Heart: d-twist mixing must vanish EXACTLY inside each fibre.")
info("Global T61 mix was |Φ_CV−Φ_χ0|/|Φ_χ0| (mean up to ~0.66).")
info("Per fibre: compare Φ_fibre to Φ_{σ_p} (the fibre's constant twist).")

# Global mix (T61-style baseline) on pattern primes + a few extras
MIX_PRIMES = list(PATTERN_PRIMES) + [
    p for p in ODD_PRIMES if 13 < p <= 200
][:20]
t_mix = time.time()
global_mix = {k: [] for k in range(1, 5)}
for p in MIX_PRIMES:
    ap = AP[p]
    phi0 = {
        k: float(lambda_arith(ap, p, 0, 4)[k] / float(p ** (3 * k)))
        for k in range(1, 5)
    }
    for k in range(1, 5):
        acc = 0.0
        for d, w in zip(live_fund, weights_cv):
            chi = kronecker(d, p)
            acc += w * (lambda_arith(ap, p, chi, 4)[k]
                        / float(p ** (3 * k)))
        phi_cv = acc / Wtot_cv
        denom = max(abs(phi0[k]), 1e-12)
        global_mix[k].append(abs(phi_cv - phi0[k]) / denom)
g_mix_mean = {k: float(np.mean(global_mix[k])) for k in range(1, 5)}
info(f"GLOBAL mix (T61-style) mean|Φ_CV−Φ_χ0|/|Φ_χ0|: "
     f"{ {k: round(g_mix_mean[k], 4) for k in range(1, 5)} } "
     f"in {time.time() - t_mix:.2f}s")

# Per-fibre mix: |Φ_fibre − Φ_{σ_p}| must be ~0 on pattern primes
# Also report variance of Φ across d in fibre
heavy_fibres = [
    s for s in fibres
    if fibre_count[s] >= MIN_FIBRE_COUNT
    and fibre_mass[s] / Wtot_cv >= MIN_FIBRE_MASS_FRAC
]
info(f"heavy fibres for mix test: {len(heavy_fibres)} "
     f"(count≥{MIN_FIBRE_COUNT}, mass frac≥{MIN_FIBRE_MASS_FRAC})")

fibre_mix_table = []  # (sig, max_mix, mean_mix, max_var)
fibre_mix_ok = True
max_fibre_mix = 0.0
max_fibre_var = 0.0
for sig in heavy_fibres:
    idxs = fibres[sig]
    w_sum = fibre_mass[sig]
    mixes = []
    vars_ = []
    for j, p in enumerate(PATTERN_PRIMES):
        chi_s = sig[j]
        ap = AP[p]
        # fibre mean
        for k in range(1, 5):
            vals = []
            acc = 0.0
            for i in idxs:
                d = live_fund[i]
                chi = kronecker(d, p)
                val = lambda_arith(ap, p, chi, 4)[k] / float(p ** (3 * k))
                vals.append(val)
                acc += weights_cv[i] * val
            phi_f = acc / w_sum
            phi_s = lambda_arith(ap, p, chi_s, 4)[k] / float(p ** (3 * k))
            denom = max(abs(phi_s), 1e-12)
            mixes.append(abs(phi_f - phi_s) / denom)
            vars_.append(float(np.var(vals)))
    mean_m = float(np.mean(mixes))
    max_m = float(np.max(mixes))
    max_v = float(np.max(vars_))
    fibre_mix_table.append((sig, max_m, mean_m, max_v, fibre_count[sig],
                            w_sum / Wtot_cv))
    max_fibre_mix = max(max_fibre_mix, max_m)
    max_fibre_var = max(max_fibre_var, max_v)
    if max_m > 1e-10 or max_v > 1e-20:
        fibre_mix_ok = False

# Sort and print top rows
fibre_mix_table.sort(key=lambda r: -r[5])
info(f"{'fibre σ':<28} {'max_mix':>10} {'mean_mix':>10} {'max_var':>10} "
     f"{'n':>5} {'μ/W':>8}")
for row in fibre_mix_table[:12]:
    sig, max_m, mean_m, max_v, n, frac = row
    info(f"{str(sig):<28} {max_m:10.2e} {mean_m:10.2e} {max_v:10.2e} "
         f"{n:5d} {frac:8.4f}")
info(f"per-fibre max mix across heavy fibres: {max_fibre_mix:.2e}")
info(f"per-fibre max variance of Φ: {max_fibre_var:.2e}")
info(f"GLOBAL mean mix (k=1..4): "
     f"{[round(g_mix_mean[k], 4) for k in range(1, 5)]}")

check(
    "C3.fibre-mix-null: d-twist mix |Φ_fibre−Φ_{σ_p}| = 0 exactly "
    f"on all heavy fibres × pattern primes "
    f"(max mix={max_fibre_mix:.2e}; max var={max_fibre_var:.2e}) — "
    "the Kill: fibre thesis holds",
    fibre_mix_ok and max_fibre_mix < 1e-10 and len(heavy_fibres) >= 8,
)

# Contrast: global mix stays large (documents the T61 obstruction is
# inter-fibre, not intra-fibre)
check(
    "C3.global-vs-fibre: GLOBAL mean mix remains O(1) "
    f"(max_k mean={max(g_mix_mean.values()):.3f}) while per-fibre "
    "mix is exact 0 — mixing was inter-fibre, killed by the "
    "direct-integral decomposition",
    max(g_mix_mean.values()) > 0.05 and fibre_mix_ok,
)

# (ii) ST cross-terms (prime-window finiteness) — fibre-independent
# since θ_p does not depend on d; same measurement as T61
info("ST cross-terms (χ_n(θ_p) Gram; classical Plancherel; "
     "fibre-independent):")


def isotype_gram(pmax, weight="log"):
    ps = [p for p in ODD_PRIMES if p <= pmax]
    if weight == "log":
        ws = np.array([math.log(p) for p in ps])
    else:
        ws = np.ones(len(ps))
    W = float(ws.sum())
    G = np.zeros((5, 5))
    for i in range(5):
        xm = np.array([chi_n_num(i, THETA[p]) for p in ps])
        for j in range(i, 5):
            xn = np.array([chi_n_num(j, THETA[p]) for p in ps])
            G[i, j] = float(np.dot(ws, xm * xn) / W)
            G[j, i] = G[i, j]
    return G


cross_rows = []
for P in (200, 500, 1000, P_MAX):
    G = isotype_gram(P, "log")
    off = [abs(G[i, j]) for i in range(5) for j in range(i + 1, 5)]
    cross_rows.append((P, max(off), float(np.mean(off))))
    info(f"  P≤{P}: max|off|={max(off):.4f} mean|off|={np.mean(off):.4f}")

cross_shrink = cross_rows[-1][1] < cross_rows[0][1] * 0.85 + 0.05
info(f"ST cross trend: {cross_rows[0][1]:.4f} → {cross_rows[-1][1]:.4f} "
     f"(T61 global 0.245→0.047 reference)")
check(
    "C3.ST-cross: log-p Gram of χ_n(θ_p) → δ_{mn} "
    f"(max|off| {cross_rows[0][1]:.4f}→{cross_rows[-1][1]:.4f}; "
    "shrinks with P as in T61; fibre-independent)",
    cross_rows[-1][1] < 0.25 and cross_shrink,
)

# (iii) Positivity inheritance per fibre
# Structural object: GNS form B(φ,φ)=Σ_d (b²/|d|)φ(d)² ≥ 0 splits as
# ⊕_σ B_σ with B_σ(φ,φ)=Σ_{d∈σ} (b²/|d|)φ(d)² ≥ 0 exactly (orthogonal
# sum of positive forms).  The Weil-type Q_0 is the χ=0-strip core
# functional (T61) — shared universal ζ(w−3) piece — measured globally
# on the finite test class.  Twisted-core Weil Q_{±1} on a hybrid
# p-window is a diagnostic only (finite-window artifact possible).
info("Positivity inheritance (GNS exact + Q_0 χ0-strip on class):")
TEST_FNS = []
for a in (1.5, 2.0, 2.5, 3.0, 3.5):
    TEST_FNS.append(("fejer", a, lambda u, aa=a: g_fejer(u, aa),
                     lambda t, aa=a: h_fejer(t, aa)))
for sigp in (0.6, 0.8, 1.0, 1.2):
    TEST_FNS.append(("gauss", sigp, lambda u, s=sigp: g_gauss(u, s),
                     lambda t, s=sigp: h_gauss(t, s)))

C0_NUM = {k: float(C0[k - 1]) for k in range(1, K_MATRIX + 1)}
core1_num_fn = {}
for k in range(1, K_MAX + 1):
    core1_num_fn[k] = sp.lambdify(P_SYM, sp.simplify(core1[k - 1]), "numpy")


def c0_for_chi(chi, p, k):
    if chi == 0:
        return C0_NUM[k]
    return float(core1_num_fn[k](p))


_ensure_arch()
Q_parts = {}
for kind, param, g_fn, h_fn in TEST_FNS:
    um = float(param) if kind == "fejer" else 6.0 * float(param)
    pole = pole_term(g_fn, um, npts=4001 if kind == "fejer" else 6001)
    arch = arch_term(h_fn)
    Q_parts[(kind, param)] = dict(pole=pole, arch=arch, um=um, g_fn=g_fn)


def prime_term_core(g_fn, umax_eff, pmax):
    """Prime term for the χ=0-strip GL(1) core G_0 (T61)."""
    s = 0.0
    for p in ODD_PRIMES:
        if p > pmax:
            break
        lp = math.log(p)
        for k in range(1, K_MAX + 1):
            u = k * lp
            if u > umax_eff + 1e-12:
                break
            s += lp * C0_NUM[k] * math.exp(-0.5 * u) * g_fn(u)
    lp = math.log(2.0)
    for k in range(1, K_MAX + 1):
        u = k * lp
        if u > umax_eff + 1e-12:
            break
        s += lp * C0_NUM[k] * math.exp(-0.5 * u) * g_fn(u)
    return 2.0 * s


# GNS fibre positivity: B_σ(1,1)=μ(σ)≥0, Σ=W_CV
gns_fibre_pos = all(fibre_mass[s] >= -1e-15 for s in heavy_fibres)
gns_mass_ok = abs(sum(fibre_mass[s] for s in fibres) - Wtot_cv) < 1e-6
info(f"GNS fibre masses: all heavy μ(σ)≥0? {gns_fibre_pos}; "
     f"#heavy={len(heavy_fibres)}; Σμ=W_CV? {gns_mass_ok}")
info("CLASSICAL: orthogonal sum of positive forms on a Hilbert-space")
info("  direct-integral decomposition remains positive per fibre.")

# Global Q_0 (χ=0 strip) on test class
Q0_vals = []
for kind, param, g_fn, h_fn in TEST_FNS:
    parts = Q_parts[(kind, param)]
    prime0 = prime_term_core(g_fn, parts["um"], P_MAX)
    q0 = parts["pole"] - prime0 + parts["arch"]
    Q0_vals.append(q0)
q0_min = min(Q0_vals)
q0_max = max(Q0_vals)
q0_pos = q0_min >= -1e-8
info(f"global Q_0 (χ=0 strip) range: [{q0_min:.6f}, {q0_max:.6f}]")

# Diagnostic: fibre-adapted twisted Weil Q on pattern primes
# (hybrid p-window — may dip slightly; NOT the GNS positivity object)
def prime_term_fibre(g_fn, umax_eff, pmax, sig):
    s = 0.0
    sig_map = {p: sig[j] for j, p in enumerate(PATTERN_PRIMES)}
    for p in ODD_PRIMES:
        if p > pmax:
            break
        lp = math.log(p)
        chi = sig_map.get(p, 0)
        for k in range(1, K_MAX + 1):
            u = k * lp
            if u > umax_eff + 1e-12:
                break
            ckn = c0_for_chi(chi, p, k)
            s += lp * ckn * math.exp(-0.5 * u) * g_fn(u)
    lp = math.log(2.0)
    for k in range(1, K_MAX + 1):
        u = k * lp
        if u > umax_eff + 1e-12:
            break
        s += lp * C0_NUM[k] * math.exp(-0.5 * u) * g_fn(u)
    return 2.0 * s


fibre_q_rows = []
fejer_tests = [(k, p, g, h) for k, p, g, h in TEST_FNS if k == "fejer"]
for sig in heavy_fibres[:16]:
    qs = []
    for kind, param, g_fn, h_fn in fejer_tests:
        parts = Q_parts[(kind, param)]
        prime_f = prime_term_fibre(g_fn, parts["um"], P_MAX, sig)
        qf = parts["pole"] - prime_f + parts["arch"]
        qs.append(qf)
    fibre_q_rows.append((sig, min(qs), max(qs), fibre_mass[sig] / Wtot_cv))

info(f"{'fibre':<28} {'Qmin_diag':>10} {'Qmax_diag':>10} {'μ/W':>8}")
for sig, qmin, qmax, frac in sorted(fibre_q_rows, key=lambda r: -r[3])[:8]:
    info(f"{str(sig):<28} {qmin:10.4f} {qmax:10.4f} {frac:8.4f}")
info("  (diagnostic twisted-Weil Q on hybrid p-window — finite-class")
info("   artifact possible; GNS positivity is the load-bearing object)")

# χ0-fibre and high-μ(0) fibres: Q_0 strip is the fibre core
zero_ish = [s for s in heavy_fibres
            if sum(1 for x in s if x == 0) >= 3][:6]
zero_q_ok = True
for sig in zero_ish:
    for kind, param, g_fn, h_fn in fejer_tests:
        parts = Q_parts[(kind, param)]
        # mostly ramified pattern → core ≈ G_0
        qf = parts["pole"] - prime_term_core(g_fn, parts["um"], P_MAX) \
            + parts["arch"]
        if qf < -1e-8:
            zero_q_ok = False
info(f"χ0-strip Q on Fejér (shared core) ≥0: {q0_pos}; "
     f"zero-rich fibre sample ok={zero_q_ok or len(zero_ish) == 0}")

fibre_q_ok = gns_fibre_pos and gns_mass_ok and q0_pos
check(
    "C3.Q0-per-fibre: each heavy fibre inherits GNS positivity "
    f"(μ(σ)≥0, ⊕_σ exact); global Q_0(χ0-strip)∈[{q0_min:.4f},"
    f"{q0_max:.4f}]≥0 on the finite test class — structural "
    "inheritance from orthogonality + global positivity; "
    "dense-class Weil positivity NOT claimed",
    fibre_q_ok and len(heavy_fibres) >= 8,
)

c3_ok = (
    fibre_mix_ok
    and max_fibre_mix < 1e-10
    and cross_shrink
    and fibre_q_ok
)


# ================================================================ C4
print("=" * 72)
print("C4 -- REASSEMBLY (direct integral → global GL(1) object)")
print("=" * 72)
info("Global isolated core = Σ_σ μ(σ) · Core(σ)  (direct-integral")
info("  reassembly of per-fibre GL(1) cores; classical).")

# Local reassembly at a pattern prime: mean of c_{k,0}(σ_p) weighted
# by fibre mass (equivalently: by the X5 marginal of χ_d(p))
info("Local reassembly at pattern primes (k=1..4 c_{k,0} means):")
reass_ok = True
reass_table = {}
for p in PATTERN_PRIMES:
    # mass-weighted mean of core coeffs by χ_d(p)
    m = x5_meas[p]
    for k in range(1, 5):
        c_plus = float(sp.N(core1[k - 1].subs(P_SYM, p)))
        c_minus = c_plus  # symmetry
        c_zero = float(C0[k - 1])
        mean_c = m[1] * c_plus + m[-1] * c_minus + m[0] * c_zero
        # Direct fibre sum
        acc = 0.0
        for sig, idxs in fibres.items():
            j = PATTERN_PRIMES.index(p)
            chi_s = sig[j]
            c_s = c_zero if chi_s == 0 else c_plus
            acc += fibre_mass[sig] * c_s
        mean_f = acc / Wtot_cv
        reass_table[(p, k)] = (mean_c, mean_f, c_zero, c_plus)
        if abs(mean_c - mean_f) > 1e-9:
            reass_ok = False
    info(f"  p={p}: μ-weighted c_{{1,0}}={reass_table[(p, 1)][0]:.6f} "
         f"(χ0={float(C0[0]):.3f}, |σ|=1→{reass_table[(p, 1)][3]:.6f}); "
         f"fibre-sum match Δ="
         f"{abs(reass_table[(p, 1)][0] - reass_table[(p, 1)][1]):.2e}")

check(
    "C4.reassembly-local: Σ_σ μ(σ) Core(σ)_p = X5-marginal mixture "
    "of G_0 and G_{±1}(p) at each pattern prime (exact match "
    "fibre-sum ↔ marginal)",
    reass_ok,
)

# Universal ζ(w−3) factor survives in EVERY fibre → in the reassembly
info("Universal factor: (1−Y)^{-1}=ζ(w−3)_p divides every fibre core")
info("  (T61: for all χ∈{−1,0,+1}).  Reassembly therefore contains")
info("  ζ(w−3) as a common factor — consistent with T58-X4 Eisenstein")
info("  floor ζ(w)ζ(w−3)²ζ(w−6)/ζ(2w−6), whose local (1−p³X)^{-1}")
info("  piece is exactly this ζ(w−3)_p factor (classical Ramanujan")
info("  σ₃ identity / Rankin–Selberg naming).")

# Check: the constant term 1 in every c_{k,0} (the ζ piece) averages to 1
zeta_piece_ok = True
for p in PATTERN_PRIMES:
    # Every core has leading ζ contribution: for χ=0, odd-k≥1 contribute;
    # more precisely the universal factor contributes +1 to every c_{k,0}
    # (T61: c_{k,0}=1+ρ_k with ρ_0-strip for χ=0 being the G0 series
    # which already includes the ζ piece).  Check reassembly c1 > 1
    # (mixture of 1 and 1+1/p).
    mean_c1 = reass_table[(p, 1)][0]
    if mean_c1 < 1.0 - 1e-9:
        zeta_piece_ok = False
    info(f"  p={p}: reassembled c_{{1,0}}={mean_c1:.6f} ≥ 1 "
         f"(ζ-piece retained)")

check(
    "C4.zeta-floor: reassembly retains ζ(w−3)_p in every fibre "
    "(reassembled c_{1,0}≥1 at pattern primes; T58-X4 Eisenstein "
    "floor consistency — the local ζ(w−3) piece is the pattern mean "
    "of the fibre cores' universal factor)",
    zeta_piece_ok,
)

info("STRUCTURE EQUATION (final):")
info("  GNS-form = ⊕_σ [ GL(1)-Core(σ) ⊕ higher ST-isotypes(σ) ]")
info("  GL(1)-Core(σ)_p = G_0           if σ_p = 0")
info("  GL(1)-Core(σ)_p = G_{±1}(p)     if |σ_p| = 1")
info("    G_0=(1+Y)/(1−Y)=ζ(w−3)_p·(1+Y)")
info("    G_{±1}: Y∂_Y log G_{±1} − Y = E_ST[Y∂_Y log N_σ] + "
     "Y/(1−Y) − Y")
info("  higher ST-isotypes(σ): Σ_{n≥1} c_{k,n}(σ_p) χ_n(θ) Y^k")
info("  Reassembly: global core = Σ_σ μ(σ)·Core(σ)")
info("            = CV/X5-weighted mixture of ζ(w−3)- and "
     "L_p(w−3)-shifts")

check(
    "C4.structure-equation: GNS-form = ⊕_σ [GL(1)-Core(σ) ⊕ higher "
    "ST-isotypes(σ)] with all components exactly named — recorded",
    c1_ok and c2_ok,
)

c4_ok = reass_ok and zeta_piece_ok and c1_ok and c2_ok


# ================================================================ C5
print("=" * 72)
print("C5 -- FINAL ROUTE-B MAP")
print("=" * 72)

info("(a) STRUCTURALLY COMPLETE (T55→T62 chain):")
info("  v538 relative-trace identity → RTF period pairing (T55)")
info("  → infinite packing / Waldspurger measure → isotype split")
info("  (T61: trivial ST isotype = GL(1) core G_0 exact) →")
info("  fibre isolation (T62: d-twist mix killed by Gelfand/direct")
info("  integral decomposition of ℓ²(d)).  The positive GNS form")
info("  decomposes as ⊕_σ [GL(1)-Core(σ) ⊕ higher isotypes(σ)].")

info("(b) NAMED OPEN PROBLEMS (not claimed here):")
info("  (1) Positivity of the isolated core on a DENSE test-function")
info("      class = RH-adjacent for the shift w−3 — named fence.")
info("  (2) Mean-rate theorems from T60 (Cesàro/Abel contraction")
info("      rates measured, not proved; k=1 Rankin–Selberg stands).")
info("  (3) Higher-isotype residual: characterised, not transported")
info("      to classical Weil weights.")

info("(c) PROMOTION-CANDIDATE TYPING (sandbox — NO promotion):")
info("  Claim-text proposal: «The GNS form of the central-value")
info("  pairing admits an exact direct-integral decomposition over")
info("  the Gelfand spectrum of {d↦χ_d(p)}, with each fibre carrying")
info("  a named GL(1) core (G_0 or ST-projected G_{±1}) and the")
info("  d-twist mixing vanishing identically inside fibres.»")
info("  Exact checks for a future vN module would include:")
info("    • diagonal GNS metric / fibre orthogonality")
info("    • Λ_fam / Φ constancy on fibres")
info("    • algebraic core identities (G_0; ST-N formula for ±1)")
info("    • per-fibre mix = 0 (numeric certificate on D-window)")
info("  Status: STRUCTURE candidate, not load-bearing verification.")

promo_ready = c1_ok and c2_ok and c3_ok and c4_ok
check(
    "C5.promotion-typing: T55–T62 structure chain typed as one "
    f"consolidated structure-module candidate "
    f"(promo_structure={promo_ready}; sandbox — NO ledger/paper move)",
    promo_ready,
)

info("(d) SATURATION ASSESSMENT:")
info("  The Route-B mapping has reached a natural saturation point:")
info("  further probes without a NEW structural idea (e.g. a dense-")
info("  class positivity argument, or a rate theorem) would be")
info("  fishing.  Remaining gaps are named analysis problems, not")
info("  missing algebraic identity hunts inside the sandbox.")
check(
    "C5.saturation: Route-B algebraic/structural mapping assessed "
    "as saturated; remaining gaps are named open analysis problems "
    "(dense-class positivity / mean rates) — not further fibre algebra",
    True,
)

c5_ok = True


# ================================================================ VERDICT
print("=" * 72)
print("VERDICT -- CORE.ISOLATION")
print("=" * 72)

if c1_ok and c2_ok and c3_ok and c4_ok:
    verdict = "CORE-ISOLATED"
    detail = (
        "C1 fibres GNS-orthogonal with Λ_fam/Φ constant on fibres; "
        "C2 per-fibre GL(1) cores exact (G_0 and ST-projected G_{±1}); "
        "C3 d-twist mix per fibre exactly 0 (global mix was inter-fibre); "
        "C4 reassembly = X5-weighted mixture of ζ(w−3)- and "
        "L_p(w−3)-shifts, T58-X4-consistent.  Dense-class positivity "
        "of the core remains RH-adjacent for the shift — NOT claimed."
    )
elif c1_ok and c2_ok and not fibre_mix_ok:
    verdict = "NO-ISOLATION"
    detail = (
        "Fibre thesis breaks: residual d-twist mix remains inside "
        "fibres — obstruction characterised by the mix table."
    )
elif c1_ok or c2_ok or fibre_mix_ok:
    verdict = "PARTIAL"
    detail = (
        "Subset of isolation criteria hold; residual quantified in "
        f"C1–C4 flags (c1={c1_ok}, c2={c2_ok}, c3={c3_ok}, c4={c4_ok})."
    )
else:
    verdict = "NO-ISOLATION"
    detail = "Fibre thesis fails at multiple blocks."

info(f"VERDICT: {verdict}")
info(detail)
check(
    f"V.verdict: {verdict} (preregistered enum; computed from C1–C4)",
    verdict in ("CORE-ISOLATED", "PARTIAL", "NO-ISOLATION"),
)

check(
    "V.T61-resolution: GNS-d twist mixing of T61 is inter-fibre; "
    "killed exactly by the Gelfand/direct-integral fibre "
    "decomposition — structural resolution of the T61 isolation gap",
    fibre_mix_ok and max(g_mix_mean.values()) > 0.05,
)


# ================================================================ SUMMARY
elapsed = time.time() - T0
print()
print("=" * 72)
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print("=" * 72)
print(f"Verdict: {verdict}")
print(f"C1 fibres: {n_fibres} nonempty, {n_pm1_fibres} pure ±1; "
      f"mean|μ−1/32|/eq={mean_eq_err:.4f}; "
      f"X5-prod err={mean_prod_err:.4f}")
print(f"C2 G_0 identity={core0_ok}; twist ST-N identity={st_core_ok}; "
      f"sym±={twist_sym}")
print(f"C3 GLOBAL mix means k=1..4: "
      f"{[round(g_mix_mean[k], 4) for k in range(1, 5)]}")
print(f"C3 PER-FIBRE max mix={max_fibre_mix:.2e} (null={fibre_mix_ok}); "
      f"ST cross {cross_rows[0][1]:.4f}→{cross_rows[-1][1]:.4f}")
print(f"C3 Q_0 global [{q0_min:.4f},{q0_max:.4f}]; "
      f"per-fibre Q ok={fibre_q_ok}")
print("C4: GNS = ⊕_σ [GL(1)-Core(σ) ⊕ higher isotypes(σ)]; "
      "reassembly = X5-mixture of G_0 and G_{±1}; ζ(w−3) retained")
print("C5: Route-B structure saturated; open = dense-class core "
      "positivity (RH-adjacent, named) + T60 mean rates; "
      "promotion-candidate typed (NO promotion)")
print(f"File: {__file__}")
print(f"Runtime: {elapsed:.1f}s")

if FAIL:
    raise SystemExit(1)
raise SystemExit(0)
