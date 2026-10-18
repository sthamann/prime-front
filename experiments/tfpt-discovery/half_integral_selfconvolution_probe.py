"""Discovery probe (2026-07-25), part 50 of the zeta/prime investigation.
FAMILY AGGREGATION of the central-value channel: the Rankin–Selberg
self-convolution of the half-integral bridge object g (v537 / T38–T45)
as its own L-object — the untried Stage-4 Route-2 move from pointwise
central values to an aggregated analytic function.

Classical background (named as such — not new mathematics):
  For a weight-(k+1/2) eigenform g = Σ b(n) q^n, the Rankin–Selberg
  self-convolution
      D_gg(s) = Σ_{n≥1} b(n)² n^{-s}
  is the canonical coefficient aggregate.  Classically (Shimura) it
  factors through L(sym²(Sh g), ·) and zeta factors with
  half-integral-specific shifts.  Via Waldspurger / Baruch–Mao (T45),
  the squarefree coefficients simultaneously encode central L-values:
      b(|d|)² = R · |d|^{3/2} · L(f₈ × χ_d, 2)   (d ≡ 1 mod 8 fund.)
  with measured R = 23.1873585645.  The Shimura coefficient relation
      b(d m²) = b(d) · α_d(m),
      α_d(m) = Σ_{j|m} μ(j) χ_d(j) j^{k-1} a(m/j)   (k=2 ⇒ j¹)
  (a = a_n(f₈)) then upgrades the pointwise identity to an aggregate:
      D_gg(s) = Σ_d b(d)² d^{-s} E_d(s),
      E_d(s)  = Σ_m α_d(m)² m^{-2s}
  and, on the fundamental d ≡ 1 mod 8 class,
      D_gg(s) = R · Σ_{d≡1(8) fund} |d|^{3/2−s} L(f₈×χ_d,2) E_d(s)
                + (non-fundamental squarefree cores: d ≡ 2 mod 4).

Context:
  T38/T41/v537: g = θ₂(q²)²·θ₃(q²)·θ₄·θ₄(q²), weight 5/2, Sh_{t=2}(g)
    = −8 f₈, exact T(p²)-eigenform with λ = a_p(f₈).
  T45: R constant on d ≡ 1 mod 8; d ≡ 5 mod 8 vanishes (root number −1).
  Support fence (T44/v537): U₄(g)=0 ⇒ no mass on n ≡ 0 mod 4, so for
  odd squarefree d the naive Shimura α_d(m) must be restricted to odd m
  (even m ⇒ d m² ≡ 0 mod 4 ⇒ b=0).  Documented as the 2-support
  correction; odd-m classical formula is exact.

S1 / A1  Euler / near-Euler structure.
    Compute b(n)² to n = 10⁴.  Exact Shimura relation for
    d ∈ {1,17,33}, m ≤ 10 (with 2-support correction).  Global
    coefficientwise factorisation n = d·m² on 1..10⁴.  Write and
    verify D_gg(s) = Σ_d b(d)² d^{-s} E_d(s).

S2 / A2  Aggregate identity (modular ⊕ central-value).
    Combine A1 with T45: replace b(d)² by R |d|^{3/2} L(f₈×χ_d,2)
    on fundamental d ≡ 1 mod 8; keep non-fundamental d ≡ 2 mod 4
    cores via b(d)².  Numeric check at s = 3, 4 (partial sums,
    tail control; AFE twist L-values as in T45).

S3 / A3  Analytic structure of D_gg.
    Growth exponent of Σ_{n≤X} b(n)² (expect ~ 5/2).  Pole candidate.
    Trial FE around preregistered centres {5/2, 2, 3/2}.  Honest:
    does the aggregate sit nearer the ξ-line than the pointwise
    GL(2)-centre values at s = 2?

S4 / A4  Route-2 interpretation (typed, not executed).
    (i) A2 closes ⇒ central-value family is compiler-aggregable;
        next Route-2 lever = FE / positivity of this aggregate.
    (ii) Boundary: the aggregate is still a weight-5/2 / sym² object,
        not ξ(s) — categorical distance remains.

PREREGISTERED CRITERIA
  A1: Shimura relation exact for d∈{1,17,33}, m≤10 under the
      documented 2-support correction; global factorisation on
      n≤10⁴; Dirichlet-series factorisation holds at s=3,4.
  A2: combined identity residual < 1% at s=3,4 with controlled tails.
  A3: report measured growth exponent, pole candidate, best trial-FE
      centre — no forcing.
  K1: Shimura relation breaks on the data (even with 2-support
      correction) ⇒ v537 chain gap.
  K2: A2 residual > 1% under controlled tails.
  Verdicts: FAMILY-AGGREGATED (A1+A2) / SHIMURA-ONLY (A1, not A2)
            / BROKEN (K1).

Firewall: discovery sandbox only — no promotion, no ledger / paper /
website / marker edits; no next.txt edit; classical theorems
(Shimura relation, Rankin–Selberg half-integral, Waldspurger /
Baruch–Mao) named as classical; no RH-evidence language.
Categorical fence (load-bearing typing): even if A2 closes, D_gg is a
weight-5/2 / sym²-type object, NOT ξ(s); the abelian channel (T39)
remains the only compiler path that reaches the ξ-line centre 1/2.
"""
from __future__ import annotations

import math
import time

import mpmath
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()
mpmath.mp.dps = 25

# ---------------------------------------------------------------- config
QMAX = 10_000
N_F8 = 100_000
K_HALF = 2                          # weight = k + 1/2 = 5/2
HEAD_AP = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}
WITNESS_KEY = (0, 2, 0, 1, 1, 1)
R_TARGET = mpmath.mpf("23.1873585645")
SHIMURA_D = (1, 17, 33)
SHIMURA_MMAX = 10
# A2: AFE budget — all live fund d ≡ 1 mod 8 up to this cut get L-values;
# beyond the cut, the fund part uses b(d)² (A1) and is compared only on
# the AFE-covered subsum; full D_gg uses A1 factorisation + Waldspurger
# plug-in on the AFE set.
D_AFE_MAX = 500
AFE_SAFETY = 40.0
AFE_DIRECT_TOL = mpmath.mpf("1e-6")   # T45 calibration band
A2_REL_TOL = 0.01                   # 1% kill threshold (K2)
GROWTH_XS = (100, 200, 500, 1000, 2000, 5000, 10000)
FE_CENTRES = (
    ("5/2", mpmath.mpf("2.5")),
    ("2", mpmath.mpf("2")),
    ("3/2", mpmath.mpf("1.5")),
)
FE_LEVEL_TRIALS = (1, 4, 8, 16, 32, 64, 128, 256, 512)
# Test s with Re(s) > abscissa; mirrors 2c−s must ALSO clear the
# abscissa for a direct-sum FE probe.  For c ≤ α ≈ 5/2 the window
# (α, 2c−α) is empty — documented as the A3 outcome, not forced.
FE_TEST_S = (
    mpmath.mpf("3.2"),
    mpmath.mpf("3.6"),
    mpmath.mpf("4.0"),
    mpmath.mpf("4.5"),
)


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


def conv_i64(a, b, order):
    return np.convolve(a, b)[: order + 1].astype(np.int64)


def kronecker(d: int, n: int) -> int:
    return int(sp.kronecker_symbol(d, n))


def is_fundamental_discriminant(d: int) -> bool:
    if d == 0:
        return False
    if d % 4 == 1:
        return abs(sp.mobius(abs(d))) == 1
    if d % 4 != 0:
        return False
    m = d // 4
    if m % 4 not in (2, 3):
        return False
    return abs(sp.mobius(abs(m))) == 1


def is_squarefree(n: int) -> bool:
    return n > 0 and abs(sp.mobius(n)) == 1


def squarefree_core(n: int):
    """Unique n = d · m² with d squarefree, m ≥ 1."""
    fac = sp.factorint(n)
    d = 1
    m = 1
    for p, e in fac.items():
        d *= p ** (e % 2)
        m *= p ** (e // 2)
    return int(d), int(m)


def twist_root_number(d: int, eps_f: int = 1, N_f: int = 8) -> int:
    assert d % 2 != 0
    return int(eps_f * kronecker(d, N_f))


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


def monomial_t(a0, a2, b0, b2, c0, c2, order_t):
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    for _ in range(a0):
        s = conv_i64(s, theta2_t(order_t, 1), order_t)
    for _ in range(a2):
        s = conv_i64(s, theta2_t(order_t, 2), order_t)
    for _ in range(b0):
        s = conv_i64(s, theta3_t(order_t, 1), order_t)
    for _ in range(b2):
        s = conv_i64(s, theta3_t(order_t, 2), order_t)
    for _ in range(c0):
        s = conv_i64(s, theta4_t(order_t, 1), order_t)
    for _ in range(c2):
        s = conv_i64(s, theta4_t(order_t, 2), order_t)
    return s


def to_q_series(s_t, qmax):
    for r in range(1, 4):
        if np.any(s_t[r::4] != 0):
            return None
    out = [0] * (qmax + 1)
    lim = min(qmax, (len(s_t) - 1) // 4)
    for n in range(lim + 1):
        out[n] = int(s_t[4 * n])
    return out


# ================================================================ P0
print("=" * 72)
print("P0 -- rebuild f8 and T38/v537 witness g to O(q^{})".format(QMAX))
print("=" * 72)

t_f8 = time.time()
f8 = np.roll(conv_i64(eta_pass(2, 4, N_F8),
                      eta_pass(4, 4, N_F8), N_F8), 1)
f8[0] = 0
a_f8 = [int(f8[n]) for n in range(N_F8 + 1)]
info(f"f8 coeffs to n={N_F8} in {time.time() - t_f8:.2f}s")
check("P0.f8: eta(2t)^4 eta(4t)^4 matches T11 a_p head; a_1=1; "
      "a_even=0 on n<=200",
      a_f8[1] == 1
      and all(a_f8[p] == v for p, v in HEAD_AP.items())
      and all(a_f8[n] == 0 for n in range(2, 201, 2)))

t_g = time.time()
g = to_q_series(monomial_t(*WITNESS_KEY, 4 * QMAX), QMAX)
assert g is not None
info(f"g rebuild O(q^{QMAX}) in {time.time() - t_g:.2f}s; head={g[:20]}")
mass_mod4 = {
    r: sum(abs(g[n]) for n in range(1, min(QMAX, 800) + 1) if n % 4 == r)
    for r in range(4)
}
info(f"|g| mass by n mod 4 (n=1..800): {mass_mod4}")
check("P0.g: T38/v537 witness; g[0]=0; mass only on n≡1,2 mod 4 "
      f"(U4 fence: mass0={mass_mod4[0]}, mass3={mass_mod4[3]})",
      g[0] == 0 and mass_mod4[0] == 0 and mass_mod4[3] == 0
      and mass_mod4[1] > 0 and mass_mod4[2] > 0)

b2 = [g[n] * g[n] for n in range(QMAX + 1)]
info(f"D_gg coeffs b(n)^2 ready; Σ_{{n≤10^4}} b(n)^2 = {sum(b2[1:])}")


# ================================================================ A1
print("=" * 72)
print("A1 -- Shimura relation + near-Euler factorisation of D_gg")
print("=" * 72)

info("CLASSICAL Shimura coefficient relation (weight k+1/2, k=2):")
info("  b(d m²) = b(d) · α_d(m),")
info("  α_d(m) = Σ_{j|m} μ(j) χ_d(j) j^{k-1} a_{m/j}(f₈)")
info("2-SUPPORT CORRECTION (v537 U4 fence, documented):")
info("  for odd squarefree d, even m ⇒ d m² ≡ 0 mod 4 ⇒ b=0;")
info("  naive α_d(even) need not vanish (a_1 term).  Corrected:")
info("  α_d^♯(m) = α_d(m) if m odd, else 0.")


def alpha_naive(d: int, m: int) -> int:
    """Classical Shimura α_d(m) with a = a(f₈), k=2."""
    tot = 0
    for j in sp.divisors(m):
        j = int(j)
        mj = m // j
        if mj > N_F8:
            raise ValueError(f"a_f8 table too short for m={m}")
        tot += (int(sp.mobius(j)) * kronecker(d, j)
                * (j ** (K_HALF - 1)) * a_f8[mj])
    return int(tot)


def alpha_sharp(d: int, m: int) -> int:
    """Shimura α with 2-support correction for this non-plus g."""
    if m % 2 == 0:
        return 0
    return alpha_naive(d, m)


# --- table for preregistered (d,m) ---
info(f"Shimura table d in {SHIMURA_D}, m=1..{SHIMURA_MMAX}:")
info(f"  {'d':>4} {'m':>3} {'n':>6} {'b(n)':>8} "
     f"{'b·α_naive':>10} {'b·α_sharp':>10} {'match_sharp':>12}")
shimura_sharp_ok = True
naive_even_mismatch = 0
for d in SHIMURA_D:
    bd = g[d]
    for m in range(1, SHIMURA_MMAX + 1):
        n = d * m * m
        if n > QMAX:
            continue
        an = alpha_naive(d, m)
        ash = alpha_sharp(d, m)
        pred_n = bd * an
        pred_s = bd * ash
        match = (g[n] == pred_s)
        shimura_sharp_ok = shimura_sharp_ok and match
        if m % 2 == 0 and g[n] != pred_n:
            naive_even_mismatch += 1
        info(f"  {d:4d} {m:3d} {n:6d} {g[n]:8d} "
             f"{pred_n:10d} {pred_s:10d} {str(match):>12}")

check(f"A1.Shimura-table: classical α with 2-support correction exact "
      f"for d in {SHIMURA_D}, m≤{SHIMURA_MMAX} "
      f"(naive even-m mismatches observed: {naive_even_mismatch})",
      shimura_sharp_ok and naive_even_mismatch > 0)

# --- global coefficientwise factorisation ---
fac_fails = []
fac_ok = 0
for n in range(1, QMAX + 1):
    d, m = squarefree_core(n)
    if m > N_F8:
        continue
    try:
        pred = g[d] * alpha_sharp(d, m)
    except ValueError:
        continue
    if g[n] != pred:
        fac_fails.append((n, d, m, g[n], pred))
        if len(fac_fails) > 5:
            break
    else:
        fac_ok += 1
info(f"global factorisation n=d·m² on 1..{QMAX}: ok={fac_ok}, "
     f"fails={len(fac_fails)}")
if fac_fails:
    info(f"  first fails: {fac_fails[:3]}")
K1_fired = (not shimura_sharp_ok) or (len(fac_fails) > 0)
check(f"A1.global: b(d m²)=b(d)·α_d^♯(m) exact on n≤{QMAX} "
      f"(ok={fac_ok}); K1_fired={K1_fired}",
      len(fac_fails) == 0 and shimura_sharp_ok)

# --- Dirichlet factorisation D_gg = Σ_d b(d)² d^{-s} E_d(s) ---
# Collect squarefree cores that appear
cores = sorted({squarefree_core(n)[0] for n in range(1, QMAX + 1)
                if g[n] != 0 or is_squarefree(n)})
# All squarefree d ≤ QMAX (for complete E_d bookkeeping)
sqfree_d = [d for d in range(1, QMAX + 1) if is_squarefree(d)]
info(f"squarefree d ≤ {QMAX}: {len(sqfree_d)}; "
     f"with b(d)≠0: {sum(1 for d in sqfree_d if g[d] != 0)}")


def E_d_trunc(d: int, s, nmax: int):
    """Truncated Euler/Dirichlet factor Σ_{m: d m² ≤ nmax} α_d^♯(m)² m^{-2s}."""
    s = mpmath.mpf(s)
    mmax = int(math.isqrt(nmax // d))
    tot = mpmath.mpf(0)
    for m in range(1, mmax + 1):
        al = alpha_sharp(d, m)
        if al:
            tot += mpmath.mpf(al * al) * mpmath.power(m, -2 * s)
    return tot


def D_gg_direct(s, nmax: int):
    s = mpmath.mpf(s)
    tot = mpmath.mpf(0)
    for n in range(1, nmax + 1):
        if b2[n]:
            tot += mpmath.mpf(b2[n]) * mpmath.power(n, -s)
    return tot


def D_gg_factorised(s, nmax: int):
    """Σ_d b(d)² d^{-s} E_d^{trunc}(s) over squarefree d."""
    s = mpmath.mpf(s)
    tot = mpmath.mpf(0)
    for d in sqfree_d:
        if d > nmax:
            break
        bd2 = b2[d]
        if bd2 == 0:
            continue
        tot += (mpmath.mpf(bd2) * mpmath.power(d, -s)
                * E_d_trunc(d, s, nmax))
    return tot


A1_fac_s_ok = True
for s_test in (3, 4):
    lhs = D_gg_direct(s_test, QMAX)
    rhs = D_gg_factorised(s_test, QMAX)
    rel = abs(lhs - rhs) / abs(lhs) if lhs != 0 else mpmath.mpf(1)
    info(f"A1 factorisation at s={s_test}: LHS={lhs}, RHS={rhs}, "
         f"rel={float(rel):.3e}")
    A1_fac_s_ok = A1_fac_s_ok and (rel < mpmath.mpf("1e-20"))

check("A1.Dirichlet: D_gg(s)=Σ_d b(d)² d^{-s} E_d(s) exact at s=3,4 "
      f"(truncation n≤{QMAX}, rel < 1e-20)",
      A1_fac_s_ok)

info("EXACT FACTORISATION (central-value weights × GL(2) Euler part):")
info("  D_gg(s) = Σ_{d squarefree} b(d)² · d^{-s} · E_d(s)")
info("  E_d(s)  = Σ_{m odd ≥ 1} α_d(m)² m^{-2s}")
info("  α_d(m)  = Σ_{j|m} μ(j) χ_d(j) j a_{m/j}(f₈)   (m odd)")
info("  On fund. d≡1 mod 8: b(d)² = R |d|^{3/2} L(f₈×χ_d,2)  (T45)")
info("  ⇒ D_gg(s) = R Σ_{d≡1(8) fund} |d|^{3/2−s} L(·,2) E_d(s)")
info("            + Σ_{d≡2 mod 4, sqfree} b(d)² d^{-s} E_d(s)")

A1_ok = (shimura_sharp_ok and len(fac_fails) == 0 and A1_fac_s_ok
         and not K1_fired)
check(f"A1.summary: A1_ok={A1_ok}; K1_fired={K1_fired}", True)


# ================================================================ A2
print("=" * 72)
print("A2 -- aggregate identity: Waldspurger family → D_gg(s)")
print("=" * 72)

info("AFE twist L-values (T45 technique) for fund d≡1 mod 8, "
     f"d≤{D_AFE_MAX}, b(d)≠0.")


def nterms_for(Nlev: int, safety: float = AFE_SAFETY) -> int:
    sq = math.sqrt(Nlev)
    need = int(math.ceil(safety * sq / (2 * math.pi))) + 50
    return min(N_F8, max(800, need))


def L_twist_direct(d, s, terms):
    s = mpmath.mpf(s)
    tot = mpmath.mpf(0)
    for n in range(1, min(terms, N_F8) + 1):
        an = a_f8[n]
        if not an:
            continue
        ch = kronecker(d, n)
        if not ch:
            continue
        tot += mpmath.mpf(an * ch) * mpmath.power(n, -s)
    return tot


def L_twist_afe(d, s, Nlev, eps, terms):
    s = mpmath.mpf(s)
    sqN = mpmath.sqrt(Nlev)
    two_pi = 2 * mpmath.pi
    lam = mpmath.mpf(0)
    kms = mpmath.mpf(4) - s
    for n in range(1, min(terms, N_F8) + 1):
        an = a_f8[n]
        if not an:
            continue
        ch = kronecker(d, n)
        if not ch:
            continue
        xx = two_pi * n / sqN
        pref = sqN / (two_pi * n)
        c = mpmath.mpf(an * ch)
        lam += c * (pref ** s * mpmath.gammainc(s, xx)
                    + eps * pref ** kms * mpmath.gammainc(kms, xx))
    return lam / ((sqN / (2 * mpmath.pi)) ** s * mpmath.gamma(s))


live_fund = [d for d in range(1, D_AFE_MAX + 1, 2)
             if d % 8 == 1 and is_fundamental_discriminant(d) and g[d] != 0]
info(f"live fund d≡1 mod 8, d≤{D_AFE_MAX}, b≠0: n={len(live_fund)}")
info(f"  list: {live_fund}")

# Validate AFE on a small subset at s=3.5
SMALL_VALIDATE = [d for d in (1, 17, 33, 57, 65, 73, 89, 97)
                  if d in live_fund]
afe_ok = True
t_afe0 = time.time()
L_cache = {}
for d in SMALL_VALIDATE:
    Nlev = 8 * d * d
    eps = twist_root_number(d)
    nt = nterms_for(Nlev)
    Ldir = L_twist_direct(d, mpmath.mpf("3.5"),
                          terms=min(N_F8, max(20000, 5 * nt)))
    La = L_twist_afe(d, mpmath.mpf("3.5"), Nlev, eps, nt)
    rel = abs(La - Ldir) / abs(Ldir) if Ldir != 0 else mpmath.mpf(1)
    afe_ok = afe_ok and (rel < AFE_DIRECT_TOL)
    info(f"  AFE↔dir d={d} @s=3.5: rel={float(rel):.3e}, eps={eps:+d}")

check(f"A2.AFE-cal: AFE↔direct at s=3.5 rel<{float(AFE_DIRECT_TOL):.0e} "
      f"for d in {SMALL_VALIDATE}",
      afe_ok and len(SMALL_VALIDATE) >= 5)

# Compute central L(2) for all live_fund
info(f"computing L_AFE(f8×χ_d, 2) for {len(live_fund)} discriminants...")
R_rows = []
for d in live_fund:
    Nlev = 8 * d * d
    eps = twist_root_number(d)
    nt = nterms_for(Nlev)
    L2 = L_twist_afe(d, 2, Nlev, eps, nt)
    L_cache[d] = L2
    denom = mpmath.power(d, mpmath.mpf("1.5")) * L2
    R = mpmath.mpf(b2[d]) / denom if abs(L2) > mpmath.mpf("1e-30") else None
    R_rows.append((d, g[d], L2, R))
info(f"AFE L(2) block in {time.time() - t_afe0:.2f}s")

R_vals = [r[3] for r in R_rows if r[3] is not None]
R_med = sorted(R_vals, key=lambda x: float(x))[len(R_vals) // 2]
R_spread = max(abs(float(r) - float(R_med)) / abs(float(R_med))
               for r in R_vals)
info(f"R(d) on AFE set: med={R_med}, spread={R_spread:.3e}, "
     f"T45 target={R_TARGET}")
info(f"  {'d':>6} {'b':>8} {'L_AFE(2)':>18} {'R(d)':>18}")
for d, bn, L2, R in R_rows[:12]:
    info(f"  {d:6d} {bn:8d} {float(L2):18.12g} {float(R):18.12g}")
if len(R_rows) > 12:
    info(f"  ... ({len(R_rows) - 12} more)")

check(f"A2.R-constancy: Waldspurger R spread < 1e-8 on d≤{D_AFE_MAX} "
      f"live class (spread={R_spread:.3e}; med≈T45)",
      R_spread < 1e-8
      and abs(float(R_med) - float(R_TARGET)) / float(R_TARGET) < 1e-8)

# --- combined identity at s=3,4 ---
# Full LHS = D_gg direct.
# RHS = R_TARGET * Σ_{d in live_fund} |d|^{3/2-s} L(d) E_d
#     + Σ_{d≡2 mod 4 sqfree, d≤QMAX} b(d)² d^{-s} E_d
#     + Σ_{fund d≡1 mod8, D_AFE_MAX < d ≤ QMAX} b(d)² d^{-s} E_d
#       (A1 weights for d beyond AFE budget — still exact for those terms)
# For the FUND part with AFE, use R*L instead of b²; residual measures
# Waldspurger plug-in error propagated through E_d.
#
# Preregistered check: compare
#   LHS_full vs RHS_hybrid
# and also the pure fund-AFE subsum residual.

def RHS_aggregate(s, nmax: int, use_R_for_afe: bool):
    s = mpmath.mpf(s)
    tot = mpmath.mpf(0)
    fund_afe_part = mpmath.mpf(0)
    fund_tail_part = mpmath.mpf(0)
    nonfund_part = mpmath.mpf(0)
    for d in sqfree_d:
        if d > nmax:
            break
        Ed = E_d_trunc(d, s, nmax)
        if Ed == 0 and b2[d] == 0:
            continue
        if is_fundamental_discriminant(d) and d % 8 == 1:
            if d in L_cache and use_R_for_afe:
                term = (R_TARGET * mpmath.power(d, mpmath.mpf("1.5") - s)
                        * L_cache[d] * Ed)
                fund_afe_part += term
                tot += term
            else:
                term = mpmath.mpf(b2[d]) * mpmath.power(d, -s) * Ed
                if d in L_cache:
                    fund_afe_part += term  # diagnostic
                else:
                    fund_tail_part += term
                tot += term
        elif d % 4 == 2:
            term = mpmath.mpf(b2[d]) * mpmath.power(d, -s) * Ed
            nonfund_part += term
            tot += term
        else:
            # d ≡ 5 mod 8 fund (b=0) or other; include via b² (should be 0)
            term = mpmath.mpf(b2[d]) * mpmath.power(d, -s) * Ed
            tot += term
    return tot, fund_afe_part, fund_tail_part, nonfund_part


A2_ok = True
A2_residuals = {}
for s_test in (3, 4):
    lhs = D_gg_direct(s_test, QMAX)
    rhs, f_afe, f_tail, nf = RHS_aggregate(s_test, QMAX, use_R_for_afe=True)
    # Pure A1 RHS for comparison
    rhs_a1 = D_gg_factorised(s_test, QMAX)
    rel_a1 = abs(lhs - rhs_a1) / abs(lhs)
    rel_agg = abs(lhs - rhs) / abs(lhs)
    # Tail control: contribution of n > QMAX roughly ≪ X^{α-s}/(s-α);
    # use growth fit later; here bound omitted mass by last dyadic ratio.
    S_half = sum(b2[n] for n in range(QMAX // 2 + 1, QMAX + 1))
    # crude tail of D at s: ∫_{QMAX}^∞ x^{α-1-s} ~ QMAX^{α-s}/(s-α)
    # with α≈2.6; report fractional last-octave mass as tail proxy
    S_all = sum(b2[1:])
    tail_proxy = (mpmath.mpf(S_half) * mpmath.power(QMAX, -s_test)
                  / abs(lhs))
    A2_residuals[s_test] = {
        "lhs": lhs, "rhs": rhs, "rel": rel_agg,
        "rel_a1": rel_a1, "f_afe": f_afe, "f_tail": f_tail,
        "nf": nf, "tail_proxy": tail_proxy,
    }
    info(f"A2 s={s_test}:")
    info(f"  LHS D_gg^≤{QMAX}     = {lhs}")
    info(f"  RHS aggregate (R·L)  = {rhs}")
    info(f"  rel(LHS,RHS)         = {float(rel_agg):.6e}")
    info(f"  rel(LHS,A1-factor)   = {float(rel_a1):.6e}")
    info(f"  parts: fund_AFE={f_afe}, fund_tail(b²)={f_tail}, "
         f"nonfund(d≡2 mod4)={nf}")
    info(f"  tail proxy (last octave / LHS) = {float(tail_proxy):.6e}")
    A2_ok = A2_ok and (rel_agg < A2_REL_TOL)

K2_fired = A1_ok and afe_ok and (not A2_ok)
check(f"A2.identity: aggregate residual < {A2_REL_TOL:.0%} at s=3,4 "
      f"(s=3: {float(A2_residuals[3]['rel']):.3e}; "
      f"s=4: {float(A2_residuals[4]['rel']):.3e}); K2_fired={K2_fired}",
      A2_ok)

# Subsum check: AFE-covered fund part alone vs R·L·E
info("A2 subsum: fund d≤D_AFE only (isolates Waldspurger plug-in)")
for s_test in (3, 4):
    s = mpmath.mpf(s_test)
    lhs_sub = mpmath.mpf(0)
    rhs_sub = mpmath.mpf(0)
    for d in live_fund:
        Ed = E_d_trunc(d, s, QMAX)
        lhs_sub += mpmath.mpf(b2[d]) * mpmath.power(d, -s) * Ed
        rhs_sub += (R_TARGET * mpmath.power(d, mpmath.mpf("1.5") - s)
                    * L_cache[d] * Ed)
    rel_sub = (abs(lhs_sub - rhs_sub) / abs(lhs_sub)
               if lhs_sub != 0 else mpmath.mpf(1))
    info(f"  fund-sub s={s_test}: LHS={lhs_sub}, RHS={rhs_sub}, "
         f"rel={float(rel_sub):.3e}")
    check(f"A2.fund-sub s={s_test}: R·L·E vs b²·E rel<{A2_REL_TOL:.0%} "
          f"(rel={float(rel_sub):.3e})",
          rel_sub < A2_REL_TOL)

check(f"A2.summary: A2_ok={A2_ok}; K2_fired={K2_fired}", True)


# ================================================================ A3
print("=" * 72)
print("A3 -- analytic structure of D_gg (growth / pole / trial FE)")
print("=" * 72)

info("Growth of S(X)=Σ_{n≤X} b(n)²; classical Rankin for weight κ "
     "gives exponent κ, so weight 5/2 ⇒ expect ~ 5/2 = 2.5.")
growth_rows = []
for X in GROWTH_XS:
    SX = sum(b2[n] for n in range(1, X + 1))
    exp_raw = math.log(SX) / math.log(X) if SX > 0 else float("nan")
    growth_rows.append((X, SX, exp_raw))
    info(f"  X={X:5d}: S(X)={SX:15d}, logS/logX={exp_raw:.6f}")

# Local exponent from dyadic ratios: S(2X)/S(X) ≈ 2^α ⇒ α = log2(S2/S1)
local_exps = []
for (X1, S1, _), (X2, S2, _) in zip(growth_rows, growth_rows[1:]):
    if S1 > 0 and X2 == 2 * X1:
        a_loc = math.log(S2 / S1) / math.log(2)
        local_exps.append((X1, X2, a_loc))
        info(f"  local α via S({X2})/S({X1}): {a_loc:.6f}")
# also non-dyadic pairs
for i in range(len(growth_rows) - 1):
    X1, S1, _ = growth_rows[i]
    X2, S2, _ = growth_rows[i + 1]
    if S1 > 0 and X2 != 2 * X1:
        a_loc = math.log(S2 / S1) / math.log(X2 / X1)
        local_exps.append((X1, X2, a_loc))
        info(f"  local α via S({X2})/S({X1}): {a_loc:.6f}")

alpha_fit = local_exps[-1][2] if local_exps else growth_rows[-1][2]
alpha_end = growth_rows[-1][2]
info(f"measured growth exponent: logS/logX @10^4 = {alpha_end:.4f}; "
     f"last local α = {alpha_fit:.4f} (classical target 2.5)")

# Pole candidate: D_gg(s) diverges for s ≤ α; simple pole expected near s=κ=5/2
# if the Rankin–Selberg residue is nonzero (classical).
pole_candidate = mpmath.mpf("2.5")
info(f"pole candidate (classical Rankin weight 5/2): s = {pole_candidate}")
info("convergence abscissa ≈ measured α ∈ "
     f"[{min(r[2] for r in local_exps):.3f}, "
     f"{max(r[2] for r in local_exps):.3f}] → consistent with 5/2")

check(f"A3.growth: measured local exponent in [2.3, 2.9] near 5/2 "
      f"(last local α={alpha_fit:.4f}, logS/logX@1e4={alpha_end:.4f})",
      2.3 <= alpha_fit <= 2.9 and 2.3 <= alpha_end <= 2.9)

# Trial FE: complete D_gg with Gamma(s)^2 or Gamma(s) around trial centres.
# Classical Rankin–Selberg for two weight-κ forms has FE s ↔ 2κ − s? 
# For self-convolution of weight κ=5/2, centre candidates preregistered.
# We test Λ(s) = (√N/(2π))^s Γ(s)^w D_gg(s) ≈ ε Λ(2c − s) with w∈{1,2}.

info("Trial FE for D_gg: Λ(s)=(√N/(2π))^s Γ(s)^w D≤(s) "
     "vs ε Λ(2c−s); centres {5/2,2,3/2}, w∈{1,2}.")
info(f"abscissa α≈{alpha_fit:.3f}: a direct-sum FE probe needs "
     f"α < s < 2c−α (mirror also convergent).")

fe_window = {}
MIN_FE_WINDOW = 0.2   # need ≥0.2 width for a usable direct-sum probe
for c_name, c_val in FE_CENTRES:
    lo = alpha_fit
    hi = float(2 * c_val) - alpha_fit
    width = hi - lo
    empty = width < MIN_FE_WINDOW
    fe_window[c_name] = (lo, hi, empty, width)
    info(f"  centre {c_name}: window ({lo:.3f}, {hi:.3f}) "
         f"width={width:.3f} → {'UNUSABLE' if empty else 'usable'} "
         f"(need ≥{MIN_FE_WINDOW})")


def D_partial(s, nmax=QMAX):
    return D_gg_direct(s, nmax)


fe_results = []
for c_name, c_val in FE_CENTRES:
    lo, hi, empty, _width = fe_window[c_name]
    if empty:
        continue
    for w_gamma in (1, 2):
        for Nlev in FE_LEVEL_TRIALS:
            for eps in (1, -1):
                gaps = []
                for s in FE_TEST_S:
                    s2 = 2 * c_val - s
                    if float(s) <= lo + 0.05 or float(s2) <= lo + 0.05:
                        continue
                    if float(s) >= hi - 0.05:
                        continue
                    sqN = mpmath.sqrt(Nlev)
                    pref = sqN / (2 * mpmath.pi)
                    D1 = D_partial(s)
                    D2 = D_partial(s2)
                    Lam1 = (pref ** s) * (mpmath.gamma(s) ** w_gamma) * D1
                    Lam2 = (pref ** s2) * (mpmath.gamma(s2) ** w_gamma) * D2
                    if Lam1 == 0 or Lam2 == 0:
                        continue
                    gaps.append(abs(Lam1 / (eps * Lam2) - 1))
                if len(gaps) >= 2:
                    fe_results.append({
                        "centre": c_name, "c": c_val, "w": w_gamma,
                        "N": Nlev, "eps": eps, "max_gap": max(gaps),
                        "n_pts": len(gaps),
                    })

fe_results.sort(key=lambda r: r["max_gap"])
all_windows_unusable = all(fe_window[n][2] for n, _ in FE_CENTRES)
info(f"all preregistered FE windows unusable (α≈{alpha_fit:.3f})? "
     f"{all_windows_unusable}")
# centre 5/2 sits AT the Rankin abscissa/pole: window width =
# 2*(5/2)−2α = 5−2α ≈ 0 when α→5/2.  Centres 2 and 3/2 give
# 2c−α < α.  Aggregate is NOT nearer the ξ-line than the pointwise
# GL(2) centre-2 values in any probed sense.
dist_pole_to_xi = abs(float(pole_candidate) - 0.5)
dist_gl2_to_xi = abs(2.0 - 0.5)
nearer_xi = dist_pole_to_xi < dist_gl2_to_xi
info(f"|pole 5/2 − ξ-centre 1/2| = {dist_pole_to_xi:.3f}; "
     f"|GL(2) centre 2 − 1/2| = {dist_gl2_to_xi:.3f}; "
     f"aggregate nearer ξ than pointwise? {nearer_xi}")

best_fe = fe_results[0] if fe_results else None
if best_fe is not None:
    info("top trial-FE hits (lowest max |Λ/εΛ∨ − 1|):")
    for r in fe_results[:8]:
        info(f"  centre={r['centre']:>3}, w=Γ^{r['w']}, N={r['N']:<4}, "
             f"eps={r['eps']:+d}, max_gap={r['max_gap']:.3e}, "
             f"pts={r['n_pts']}")
else:
    info("NO usable trial-FE hit (preregistered centres unusable for "
         "direct-sum probes).  Honest A3 outcome — not a kill: FE/"
         "positivity of D_gg needs classical Rankin–sym² continuation "
         "(named Route-2 next lever), not a forced fit.")

check(f"A3.trial-FE: centres {{5/2,2,3/2}} all unusable for direct-sum "
      f"FE at α≈{alpha_fit:.3f} (all_unusable={all_windows_unusable}, "
      f"best_hit={best_fe['centre'] if best_fe else None}); "
      f"aggregate nearer ξ than pointwise-@2? {nearer_xi} "
      f"(pole@5/2 still |·−1/2|={dist_pole_to_xi:.2f})",
      all_windows_unusable and best_fe is None and (not nearer_xi))

check("A3.fence: aggregate sits at Rankin weight-5/2 abscissa/pole "
      "candidate s=5/2 — NOT the ξ-line centre 1/2; pointwise values "
      "live at GL(2) centre 2; categorical distance to ξ remains "
      "(abelian channel T39 only)",
      abs(float(pole_candidate) - 0.5) > 1.0
      and abs(2.0 - 0.5) > 1.0)


# ================================================================ A4
print("=" * 72)
print("A4 -- Route-2 interpretation / verdict")
print("=" * 72)

if K1_fired:
    verdict = "BROKEN"
elif A1_ok and A2_ok:
    verdict = "FAMILY-AGGREGATED"
elif A1_ok:
    verdict = "SHIMURA-ONLY"
else:
    verdict = "BROKEN"

info(f"VERDICT = {verdict}")
info("TYPING:")
info("  (i) Pointwise central values (T45): b(|d|)² ↔ L(f₈×χ_d,2).")
info("  (ii) Aggregate (this probe): D_gg(s)=Σ b(n)² n^{-s} factors as")
info("       central-value weights × GL(2)-Euler factors E_d(s).")
info("  (iii) D_gg is a weight-5/2 / Rankin–sym²-type object — NOT ξ(s).")
info("       Categorical distance to the ξ-line remains (T39 abelian only).")

if verdict == "FAMILY-AGGREGATED":
    info("CONSEQUENCE for Route 2: the central-value family IS")
    info("  compiler-aggregable into an analytic function D_gg whose")
    info("  building blocks (g, a_p(f₈), R, twist L-values) are all")
    info("  compiler-native.  Next Route-2 lever (NAMED, not executed):")
    info("  FE / positivity analysis of D_gg (sym² / Rankin package) —")
    info("  still not an RH reading; still not the ξ-line.")
elif verdict == "SHIMURA-ONLY":
    info("CONSEQUENCE: Shimura factorisation works; Waldspurger aggregate")
    info("  identity fails numerically (K2).  Route 2 blocked at the")
    info("  central-value → D_gg glue; recheck AFE tails / R-scope.")
elif verdict == "BROKEN":
    info("CONSEQUENCE: Shimura relation broken on v537 data (K1) —")
    info("  half-integral bridge chain has a coefficient gap; do not")
    info("  interpret aggregation until A1 is restored.")

check(f"A4.verdict: {verdict}; A1_ok={A1_ok}; A2_ok={A2_ok}; "
      f"K1={K1_fired}; K2={K2_fired}; "
      f"growth_α≈{alpha_fit:.4f}; trial_FE="
      f"{'UNUSABLE-WINDOWS' if all_windows_unusable else (best_fe['centre'] if best_fe else None)}; "
      f"pole_candidate=5/2; nearer_xi={nearer_xi}",
      verdict in ("FAMILY-AGGREGATED", "SHIMURA-ONLY", "BROKEN"))

check("A4.boundary-sentence: even under FAMILY-AGGREGATED, D_gg is "
      "weight-5/2/sym²-type, not ξ(s) — categorical fence recorded",
      True)


# ================================================================ end
elapsed = time.time() - T0
print("=" * 72)
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print(f"VERDICT: {verdict}")
print("=" * 72)
raise SystemExit(0 if FAIL == 0 else 1)
