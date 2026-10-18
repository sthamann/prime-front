"""Discovery probe (2026-07-25), part 65 of the zeta/prime investigation.
Contract PI.DIGITS.PRIME.CORRELATION -- honest null-battery exploration,
NOT a TFPT claim.

Project-lead question (literal): "What happens if one looks for the same
distribution that the primes have at the places in pi -- are there
correlations?"

PREREGISTERED EXPECTATION: NULL.  The digits of pi are believed normal /
pseudorandom (normality of pi is an OPEN classical question, but
empirically extremely well supported).  The primes are deterministic with
density 1/log n (Gauss / prime-number theorem, classical).  There is NO
known mechanism for a correlation between the two.  Any positive signal
requires a look-elsewhere correction (declare the number of statistics
tested) and replication in disjoint windows.  No numerology: no hunting
of single "meaningful" digit strings.  Scientific content of this probe
is the CONTRAST: what distinguishes primes from pi-driven randomness
(arithmetic pair correlations) and what does not (density statistics).

  S1 / P1  PRIME-INDEXED DIGITS: extract decimal digits of pi at prime
      positions p <= X; chi^2 vs Uniform{0..9}, KS on cumulative
      frequencies; base-10 only (justification: classical normality
      statements for pi are base-b for integer b, and bit-extraction
      from decimals introduces artificial dependence).  Nulls: equally
      many random positions (3 seeds) and composite positions.
  S2 / P2  CROSS-CORRELATION: correlate the prime indicator 1_prime(n)
      with digit features (d_n, d_n mod 2, window sums), AFTER removing
      the 1/log n density drift (else a shared trend fakes correlation);
      Pearson + block-permutation test; replicate in four disjoint
      windows.
  S3 / P3  PI-DRIVEN CRAMER MODEL (structurally interesting): admit
      n >= 3 when a Uniform[0,1) drawn from a disjoint pi-digit stream
      is < 1/log n (Cramer model, classical).  Triple comparison
      real primes vs pi-Cramer vs PRNG-Cramer (3 seeds):
        (i)   counting fluctuations |pi(x) - Li(x)| analogue;
        (ii)  normalised gap law vs exponential (real primes: small-gap
              deflation by parity);
        (iii) HARDY-LITTLEWOOD 2-POINT TEST: pair counts N(h) for even
              h = 2..60, normalised by the singular series S(h)
              (Hardy-Littlewood constants, classical, exactly
              computable).  Real primes must show HL modulation;
              pi-Cramer and PRNG-Cramer must NOT.
  S4 / P4  VERDICT + two-sentence answer to the project-lead question.

PREREGISTERED CRITERIA
  P1  Bonferroni family m_P1 = 2 (chi^2 + KS on prime-indexed digits);
      signal declared only if min corrected p <= 0.01.  Controls
      (3 random seeds + composites) documented, not in the signal
      family.  Look-elsewhere count declared in the report.
  P2  Detrend 1_prime(n) by OLS against {1, 1/log n} BEFORE correlating.
      Block-permutation p-values; Bonferroni over
      n_windows * n_features tests.  Replication: all four windows.
  P3  HL contrast: corr(N_real(h), S(h)) > corr(N_piC(h), S(h)) and
      > mean_seed corr(N_prngC(h), S(h)); variance ratio
      var(N/S)/var(N) smaller for real than for Cramer models.
  P4  Verdict is exactly one of the three preregistered enums.

VERDICTS (preregistered)
  PI-NULL-ARITHMETIC-DISTINCT  P1/P2 null after correction AND P3
      contrast stands (pi digits = neutral randomness; HL arithmetic
      is what primes have and Cramer models lack)
  PI-ANOMALY                  replicated signal after look-elsewhere
      correction -- report conservatively (would be extraordinary)
  UNDERPOWERED                budget insufficient for sharp statements

Firewall: discovery sandbox only.  Classical named as classical
(PNT/Gauss, Cramer model, Hardy-Littlewood conjecture + singular
series, normality of pi as open).  NO TFPT link claimed.  NO
promotion, no ledger/paper/website edits.

Run:
  experiments/tfpt-discovery/.venv/bin/python \\
      experiments/tfpt-discovery/pi_digits_prime_distribution_probe.py
"""
from __future__ import annotations

import math
import time

import mpmath
import numpy as np
from scipy import stats

PASS = 0
FAIL = 0
T0 = time.time()

# ---- budget (preregistered) -----------------------------------------
N_DIGITS = 500_000          # decimal places of pi
X = 100_000                 # analysis horizon (positions / Cramer cutoff)
CRAMER_DIGITS_PER_U = 4     # digits -> Uniform[0,1) for Cramer stream
CRAMER_STREAM_OFFSET = X    # disjoint from positions 1..X used in P1/P2
N_PERM = 400                # block-permutation draws (P2)
BLOCK = 200                 # block length for permutation
WIN_SUM = 5                 # digit window-sum width
RANDOM_SEEDS = (41, 42, 43)
PRNG_CRAMER_SEEDS = (101, 202, 303)
WINDOWS = (
    (2, 25_000),
    (25_000, 50_000),
    (50_000, 75_000),
    (75_000, 100_000),
)
HL_H = tuple(range(2, 61, 2))   # even distances 2..60
ALPHA = 0.01


def check(name: str, ok: bool) -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}", flush=True)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


def info(msg: str) -> None:
    print(f"        {msg}", flush=True)


# ================================================================ utils
def sieve_primes(n: int) -> np.ndarray:
    """Boolean prime indicator on 0..n inclusive."""
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_p[p]:
            is_p[p * p::p] = False
    return is_p


def chi2_uniform_digits(digs: np.ndarray) -> tuple[float, float, np.ndarray]:
    counts = np.bincount(digs, minlength=10).astype(float)
    n = float(digs.size)
    exp = n / 10.0
    chi2 = float(np.sum((counts - exp) ** 2 / exp))
    p = float(stats.chi2.sf(chi2, 9))
    return chi2, p, counts.astype(int)


def ks_digit_uniform(digs: np.ndarray) -> tuple[float, float]:
    """KS distance of empirical digit CDF vs discrete Uniform{0..9}.

    p-value via the continuous KS survival function (conservative for
    discrete support -- classical caveat, documented).
    """
    n = digs.size
    D = 0.0
    for k in range(10):
        F_emp = float(np.mean(digs <= k))
        F_th = (k + 1) / 10.0
        D = max(D, abs(F_emp - F_th))
    p = float(stats.kstwo.sf(D, n))
    return D, p


def pearson_r(a: np.ndarray, b: np.ndarray) -> float:
    a = a.astype(float)
    b = b.astype(float)
    a = a - a.mean()
    b = b - b.mean()
    denom = float(np.sqrt(np.dot(a, a) * np.dot(b, b)))
    if denom < 1e-30:
        return 0.0
    return float(np.dot(a, b) / denom)


def block_perm_pvalue(
    y: np.ndarray,
    x: np.ndarray,
    n_perm: int,
    block: int,
    seed: int,
) -> tuple[float, float]:
    """Two-sided block-permutation p for |corr(y,x)|; blocks of y shuffled."""
    r_obs = pearson_r(y, x)
    rng = np.random.default_rng(seed)
    n = y.size
    n_blocks = max(1, n // block)
    usable = n_blocks * block
    y_use = y[:usable].copy()
    x_use = x[:usable].copy()
    count = 0
    for _ in range(n_perm):
        blocks = y_use.reshape(n_blocks, block).copy()
        rng.shuffle(blocks, axis=0)
        r = pearson_r(blocks.ravel(), x_use)
        if abs(r) >= abs(r_obs) - 1e-15:
            count += 1
    p = (count + 1) / (n_perm + 1)
    return r_obs, float(p)


def ols_resid_against_density(indicator: np.ndarray, ns: np.ndarray) -> np.ndarray:
    """Remove 1/log n density drift by OLS of 1_prime on {1, 1/log n}."""
    dens = 1.0 / np.log(ns.astype(float))
    A = np.column_stack([np.ones(ns.size), dens])
    coef, _, _, _ = np.linalg.lstsq(A, indicator.astype(float), rcond=None)
    return indicator.astype(float) - A @ coef


def li_approx(x: float) -> float:
    """Offset logarithmic integral Li(x) ~ Ei(log x) (classical)."""
    if x <= 2:
        return 0.0
    return float(mpmath.ei(math.log(x)))


def twin_prime_constant(pmax: int = 5000) -> float:
    """Product_{p>2} (1 - 1/(p-1)^2), truncated (classical C_2)."""
    is_p = sieve_primes(pmax)
    c = 1.0
    for p in range(3, pmax + 1):
        if is_p[p]:
            c *= (1.0 - 1.0 / (p - 1) ** 2)
    return c


def singular_series(h: int, C2: float, is_p: np.ndarray) -> float:
    """Hardy-Littlewood singular series S(h) for even h (classical).

    S(h) = 2 C_2 * prod_{p|h, p>2} (p-1)/(p-2);  S(odd) = 0.
    """
    if h % 2 == 1:
        return 0.0
    s = 2.0 * C2
    # factor h
    m = h
    p = 3
    while p * p <= m:
        if m % p == 0:
            if p < is_p.size and is_p[p]:
                s *= (p - 1) / (p - 2)
            while m % p == 0:
                m //= p
        p += 2
    if m > 2:
        s *= (m - 1) / (m - 2)
    return s


def pair_counts(S: np.ndarray, hs: tuple[int, ...], xmax: int) -> np.ndarray:
    sset = set(int(v) for v in S if 2 <= v <= xmax)
    out = np.zeros(len(hs), dtype=float)
    for i, h in enumerate(hs):
        out[i] = sum(1 for v in sset if v + h <= xmax and (v + h) in sset)
    return out


def cramer_from_uniforms(u: np.ndarray, xmax: int) -> np.ndarray:
    """Cramer model: admit n in 3..xmax iff u[n-3] < 1/log n."""
    assert u.size >= xmax - 2
    ns = np.arange(3, xmax + 1, dtype=np.int64)
    return ns[u[: ns.size] < 1.0 / np.log(ns.astype(float))]


def uniforms_from_digits(digs: np.ndarray, n_needed: int, k: int) -> np.ndarray:
    need = n_needed * k
    assert digs.size >= need, f"need {need} digits, have {digs.size}"
    chunk = digs[:need].reshape(n_needed, k)
    # value in {0, ..., 10^k - 1} / 10^k
    weights = 10.0 ** np.arange(k - 1, -1, -1)
    vals = chunk @ weights
    return vals / (10.0 ** k)


def counting_fluctuation(S: np.ndarray, xs: np.ndarray) -> dict:
    """|pi_S(x) - Li(x)| at probe points; return max and value at X."""
    S = np.sort(S.astype(np.int64))
    errs = []
    for x in xs:
        pi_x = int(np.searchsorted(S, x, side="right"))
        li = li_approx(float(x))
        errs.append(abs(pi_x - li))
    return {
        "err_at_X": float(errs[-1]),
        "max_err": float(max(errs)),
        "pi_X": int(np.searchsorted(S, int(xs[-1]), side="right")),
        "Li_X": float(li_approx(float(xs[-1]))),
    }


def gap_stats(S: np.ndarray) -> dict:
    """Normalised gaps g / log p_n; fraction of odd gaps; mean vs Exp(1)."""
    S = np.sort(S.astype(np.int64))
    if S.size < 3:
        return {"n_gaps": 0, "odd_frac": float("nan"), "mean_norm": float("nan"),
                "frac_below_0.5": float("nan")}
    # skip leading 2 if present for parity discussion among odd primes
    if S[0] == 2:
        S = S[1:]
    gaps = np.diff(S).astype(float)
    # normalised by log of left endpoint
    norms = gaps / np.log(S[:-1].astype(float))
    odd_frac = float(np.mean(gaps % 2 == 1))
    return {
        "n_gaps": int(gaps.size),
        "odd_frac": odd_frac,
        "mean_norm": float(np.mean(norms)),
        "frac_below_0.5": float(np.mean(norms < 0.5)),
        "median_norm": float(np.median(norms)),
    }


# ================================================================ data
print("=" * 72)
print("PI.DIGITS.PRIME.CORRELATION -- part 65 null battery")
print("=" * 72)

info(f"budget: N_DIGITS={N_DIGITS}, X={X}, CRAMER_DIGITS_PER_U="
     f"{CRAMER_DIGITS_PER_U}, stream_offset={CRAMER_STREAM_OFFSET}")

t_pi = time.time()
mpmath.mp.dps = N_DIGITS + 10
pi_str = str(+mpmath.pi)
assert pi_str.startswith("3.")
digit_chars = pi_str.split(".", 1)[1][:N_DIGITS]
DIGITS = np.frombuffer(digit_chars.encode("ascii"), dtype=np.uint8) - ord("0")
assert DIGITS.shape == (N_DIGITS,)
assert DIGITS.min() >= 0 and DIGITS.max() <= 9
# Drop working precision: Ei/Li later must NOT inherit N_DIGITS dps
# (that stalls for minutes).  Digits are already materialised as ints.
mpmath.mp.dps = 25
del pi_str, digit_chars
t_pi = time.time() - t_pi
info(f"pi digits generated in {t_pi:.2f}s; head={''.join(map(str, DIGITS[:20]))}")
check(
    f"pi digit generation: N={N_DIGITS} decimals in {t_pi:.2f}s "
    f"(<300s budget; head 14159265358979323846)",
    t_pi < 300.0
    and "".join(map(str, DIGITS[:20])) == "14159265358979323846"
    and DIGITS.size == N_DIGITS,
)

is_prime = sieve_primes(X)
primes = np.nonzero(is_prime)[0].astype(np.int64)
n_primes = int(primes.size)
composites = np.array([n for n in range(2, X + 1) if not is_prime[n]],
                      dtype=np.int64)
info(f"primes <= {X}: {n_primes}; composites in [2,{X}]: {composites.size}")
check(
    f"sieve: pi({X}) matches sympy-free known anchors "
    f"(pi(100)=25, pi(1000)=168, first primes 2,3,5,7,11)",
    int(is_prime[:101].sum()) == 25
    and int(is_prime[:1001].sum()) == 168
    and list(primes[:5]) == [2, 3, 5, 7, 11],
)

# 1-indexed positions: DIGITS[0] = d_1, DIGITS[p-1] = d_p
prime_digs = DIGITS[primes - 1]
comp_digs = DIGITS[composites - 1]


# ================================================================ S1/P1
print("\nS1 / P1 -- prime-indexed digits vs uniform + nulls")
chi2_p, p_chi2_p, counts_p = chi2_uniform_digits(prime_digs)
D_p, p_ks_p = ks_digit_uniform(prime_digs)
info(f"prime-indexed digits: n={prime_digs.size}")
info(f"  counts[0..9]={list(counts_p)}")
info(f"  chi2={chi2_p:.4f}  p={p_chi2_p:.6g}")
info(f"  KS D={D_p:.6f}  p={p_ks_p:.6g}")

# Bonferroni family m_P1 = 2 (preregistered)
M_P1 = 2
p_chi2_corr = min(1.0, M_P1 * p_chi2_p)
p_ks_corr = min(1.0, M_P1 * p_ks_p)
p1_signal = min(p_chi2_corr, p_ks_corr) <= ALPHA
info(f"Bonferroni m_P1={M_P1}: p_chi2_corr={p_chi2_corr:.6g}, "
     f"p_ks_corr={p_ks_corr:.6g}; signal={p1_signal}")

# random-position nulls
rng_null_ps = []
for seed in RANDOM_SEEDS:
    rng = np.random.default_rng(seed)
    pos = rng.choice(np.arange(1, X + 1), size=n_primes, replace=False)
    digs = DIGITS[pos - 1]
    c2, pv, _ = chi2_uniform_digits(digs)
    rng_null_ps.append(pv)
    info(f"  random positions seed={seed}: chi2={c2:.4f} p={pv:.6g}")

c2_c, p_comp, counts_c = chi2_uniform_digits(comp_digs)
info(f"  composite positions: n={comp_digs.size} chi2={c2_c:.4f} "
     f"p={p_comp:.6g}")

check(
    "P1 prime-digit chi^2 and KS computed; Bonferroni m_P1=2 applied; "
    f"corrected p-values both documented (chi2_corr={p_chi2_corr:.4g}, "
    f"ks_corr={p_ks_corr:.4g})",
    math.isfinite(p_chi2_p) and math.isfinite(p_ks_p)
    and 0.0 <= p_chi2_corr <= 1.0 and 0.0 <= p_ks_corr <= 1.0
    and counts_p.sum() == prime_digs.size,
)
check(
    "P1 null controls computed: 3 random seeds + composites all have "
    "finite chi^2 p-values (contrast panel, not signal family)",
    len(rng_null_ps) == 3 and all(math.isfinite(p) for p in rng_null_ps)
    and math.isfinite(p_comp) and counts_c.sum() == comp_digs.size,
)
check(
    "P1 base-10 only (no bit extraction): classical normality statements "
    "for pi are for integer bases; digit alphabet {0..9} is the native "
    "test -- documented",
    DIGITS.dtype == np.uint8 and int(DIGITS.max()) <= 9,
)

P1_NULL = not p1_signal
info(f"P1_NULL (no signal after Bonferroni @ alpha={ALPHA}) = {P1_NULL}")


# ================================================================ S2/P2
print("\nS2 / P2 -- cross-correlation after 1/log n detrend + block perm")
FEATURES = ("digit", "parity", "win_sum")
p2_rows = []  # (window, feature, r, p_perm)
for (lo, hi) in WINDOWS:
    ns = np.arange(lo, hi + 1, dtype=np.int64)
    # need win_sum headroom
    if hi + WIN_SUM - 1 > X:
        hi_eff = X - WIN_SUM + 1
        ns = np.arange(lo, hi_eff + 1, dtype=np.int64)
    ind = is_prime[ns].astype(float)
    y = ols_resid_against_density(ind, ns)
    d_n = DIGITS[ns - 1].astype(float)
    parity = (d_n % 2)
    # window sum of WIN_SUM consecutive digits starting at n
    win = np.lib.stride_tricks.sliding_window_view(
        DIGITS[: ns[-1] + WIN_SUM - 1], WIN_SUM
    )
    # win[i] corresponds to position i+1; take rows for ns
    wsum = win[ns - 1].sum(axis=1).astype(float)
    feats = {"digit": d_n, "parity": parity, "win_sum": wsum}
    # document detrend: mean residual ~ 0
    info(f"window [{lo},{hi}]: n={ns.size}, mean residual="
         f"{y.mean():.4e}, coef-density removed by OLS")
    for fi, fname in enumerate(FEATURES):
        r, pperm = block_perm_pvalue(
            y, feats[fname], N_PERM, BLOCK, seed=1000 + 10 * lo + fi
        )
        p2_rows.append((lo, hi, fname, r, pperm))
        info(f"  {fname:7s}: r={r:+.5f}  block-perm p={pperm:.4f}")

M_P2 = len(WINDOWS) * len(FEATURES)  # look-elsewhere count
p2_min_raw = min(row[4] for row in p2_rows)
p2_min_corr = min(1.0, M_P2 * p2_min_raw)
p2_signal = p2_min_corr <= ALPHA
# replication: a "signal" that appears in only one window is not replicated
per_window_min = []
for (lo, hi) in WINDOWS:
    ps = [row[4] for row in p2_rows if row[0] == lo and row[1] == hi]
    per_window_min.append(min(ps))
n_windows_raw_lt = sum(1 for p in per_window_min if p <= ALPHA)
info(f"P2 look-elsewhere m_P2={M_P2}; min raw p={p2_min_raw:.4f}; "
     f"corr p={p2_min_corr:.4f}; windows with raw p<={ALPHA}: "
     f"{n_windows_raw_lt}/4")
P2_NULL = not p2_signal
check(
    f"P2 detrend+block-perm complete: {len(p2_rows)} tests "
    f"(= {len(WINDOWS)} windows x {len(FEATURES)} features = m_P2); "
    f"min corrected p={p2_min_corr:.4g}; P2_NULL={P2_NULL}",
    len(p2_rows) == M_P2 and math.isfinite(p2_min_corr),
)
# sanity: without detrend, 1_prime vs constant feature can pick up density
# drift -- verify residuals have near-zero correlation with 1/log n
ns_all = np.arange(2, X + 1, dtype=np.int64)
y_all = ols_resid_against_density(is_prime[ns_all].astype(float), ns_all)
r_dens = pearson_r(y_all, 1.0 / np.log(ns_all.astype(float)))
info(f"post-detrend corr(residual, 1/log n) = {r_dens:.3e} (expect ~0)")
check(
    "P2 detrend sanity: |corr(residual 1_prime, 1/log n)| < 1e-10 "
    "(OLS residual orthogonal to density regressor)",
    abs(r_dens) < 1e-10,
)


# ================================================================ S3/P3
print("\nS3 / P3 -- pi-Cramer vs PRNG-Cramer vs real primes (HL heart)")
n_u = X - 2  # uniforms for n=3..X
need_stream = n_u * CRAMER_DIGITS_PER_U
stream = DIGITS[CRAMER_STREAM_OFFSET: CRAMER_STREAM_OFFSET + need_stream]
check(
    f"P3 digit stream disjoint from P1/P2 positions: offset="
    f"{CRAMER_STREAM_OFFSET}, need={need_stream}, available="
    f"{N_DIGITS - CRAMER_STREAM_OFFSET}",
    CRAMER_STREAM_OFFSET >= X
    and stream.size == need_stream
    and CRAMER_STREAM_OFFSET + need_stream <= N_DIGITS,
)

u_pi = uniforms_from_digits(stream, n_u, CRAMER_DIGITS_PER_U)
S_real = primes[(primes >= 3) & (primes <= X)]
S_piC = cramer_from_uniforms(u_pi, X)
S_prng = []
for seed in PRNG_CRAMER_SEEDS:
    rng = np.random.default_rng(seed)
    u = rng.random(n_u)
    S_prng.append(cramer_from_uniforms(u, X))

info(f"|S_real|={S_real.size}, |S_piC|={S_piC.size}, "
     f"|S_prng|={[s.size for s in S_prng]}")

# (i) counting fluctuations
xs_probe = np.array([X // 4, X // 2, 3 * X // 4, X], dtype=float)
fl_real = counting_fluctuation(S_real, xs_probe)
fl_pi = counting_fluctuation(S_piC, xs_probe)
fl_prng = [counting_fluctuation(s, xs_probe) for s in S_prng]
info(f"counting |pi(X)-Li(X)|: real={fl_real['err_at_X']:.1f} "
     f"(pi={fl_real['pi_X']}, Li={fl_real['Li_X']:.1f}); "
     f"piC={fl_pi['err_at_X']:.1f}; "
     f"prng={[f['err_at_X'] for f in fl_prng]}")
check(
    "P3(i) counting fluctuations computed for real / pi-Cramer / "
    "3x PRNG-Cramer at X (Li via Ei(log x), classical)",
    fl_real["pi_X"] == S_real.size
    and fl_pi["pi_X"] == S_piC.size
    and all(math.isfinite(f["err_at_X"]) for f in [fl_real, fl_pi] + fl_prng),
)

# (ii) gap law
g_real = gap_stats(S_real)
g_pi = gap_stats(S_piC)
g_prng = [gap_stats(s) for s in S_prng]
info(f"gaps: real odd_frac={g_real['odd_frac']:.4f} "
     f"frac(<0.5)={g_real['frac_below_0.5']:.4f} "
     f"mean_norm={g_real['mean_norm']:.4f}")
info(f"      piC  odd_frac={g_pi['odd_frac']:.4f} "
     f"frac(<0.5)={g_pi['frac_below_0.5']:.4f} "
     f"mean_norm={g_pi['mean_norm']:.4f}")
info(f"      prng odd_frac means="
     f"{np.mean([g['odd_frac'] for g in g_prng]):.4f}")
# Real primes (after 2): ALL gaps even => odd_frac = 0.
# Cramer models: ~50% odd gaps.
parity_contrast = (
    g_real["odd_frac"] < 0.01
    and g_pi["odd_frac"] > 0.3
    and all(g["odd_frac"] > 0.3 for g in g_prng)
)
check(
    "P3(ii) gap parity contrast: real primes (n>2) have odd_frac~0 "
    "(parity obstruction); pi-Cramer and PRNG-Cramer have odd_frac~1/2 "
    f"(measured real={g_real['odd_frac']:.4f}, piC={g_pi['odd_frac']:.4f})",
    parity_contrast,
)

# (iii) Hardy-Littlewood 2-point
C2 = twin_prime_constant(5000)
S_h = np.array([singular_series(h, C2, sieve_primes(max(HL_H))) for h in HL_H])
info(f"twin-prime constant C2 ~= {C2:.8f} (classical; ~0.6601618)")
info(f"S(2)={S_h[0]:.6f} (= 2 C2); S(6)={S_h[2]:.6f}")

N_real = pair_counts(S_real, HL_H, X)
N_piC = pair_counts(S_piC, HL_H, X)
N_prngs = [pair_counts(s, HL_H, X) for s in S_prng]

# correlations with singular series
corr_real = pearson_r(N_real, S_h)
corr_piC = pearson_r(N_piC, S_h)
corr_prng = [pearson_r(N, S_h) for N in N_prngs]
corr_prng_mean = float(np.mean(corr_prng))

# variance ratio: var(N/S) / var(N) -- small when N tracks S
def var_ratio(N: np.ndarray, S: np.ndarray) -> float:
    Ns = N / S
    vN = float(np.var(N))
    vNs = float(np.var(Ns))
    return vNs / vN if vN > 0 else float("inf")

vr_real = var_ratio(N_real, S_h)
vr_piC = var_ratio(N_piC, S_h)
vr_prng = [var_ratio(N, S_h) for N in N_prngs]
vr_prng_mean = float(np.mean(vr_prng))

info("HL pair counts N(h) for even h=2..60:")
info(f"  corr(N, S): real={corr_real:+.4f}  piC={corr_piC:+.4f}  "
     f"prng_mean={corr_prng_mean:+.4f}  prng={['%+.3f' % c for c in corr_prng]}")
info(f"  var(N/S)/var(N): real={vr_real:.4e}  piC={vr_piC:.4e}  "
     f"prng_mean={vr_prng_mean:.4e}")
info(f"  N_real head (h=2,4,6,8,10)={list(N_real[:5].astype(int))}")
info(f"  N_piC  head (h=2,4,6,8,10)={list(N_piC[:5].astype(int))}")
info(f"  S(h)   head (h=2,4,6,8,10)={list(np.round(S_h[:5], 4))}")

# HL contrast stands if real correlates with S more than Cramer models
hl_contrast = (
    corr_real > corr_piC + 0.15
    and corr_real > corr_prng_mean + 0.15
    and vr_real < vr_piC
    and vr_real < vr_prng_mean
)
# also: real N(h)/S(h) flatter relative to raw than Cramer
Ns_real = N_real / S_h
Ns_piC = N_piC / S_h
cv_raw_real = float(np.std(N_real) / np.mean(N_real))
cv_norm_real = float(np.std(Ns_real) / np.mean(Ns_real))
cv_raw_piC = float(np.std(N_piC) / np.mean(N_piC))
cv_norm_piC = float(np.std(Ns_piC) / np.mean(Ns_piC))
info(f"  CV raw/norm: real {cv_raw_real:.4f}/{cv_norm_real:.4f}; "
     f"piC {cv_raw_piC:.4f}/{cv_norm_piC:.4f}")
# For real primes, normalisation by S should REDUCE relative spread.
# For Cramer, dividing by S should INCREASE relative spread.
hl_cv_contrast = (cv_norm_real < cv_raw_real) and (cv_norm_piC > cv_raw_piC)
info(f"HL contrast (corr+var)={hl_contrast}; CV contrast={hl_cv_contrast}")

check(
    f"P3(iii) singular series: S(2)=2*C2 exact-formula match "
    f"(|S(2)-2*C2|<1e-12); C2 in (0.65, 0.67)",
    abs(S_h[0] - 2.0 * C2) < 1e-12 and 0.65 < C2 < 0.67,
)
check(
    "P3(iii) HARDY-LITTLEWOOD contrast stands: real primes track S(h) "
    f"(corr={corr_real:+.3f}) while pi-Cramer (corr={corr_piC:+.3f}) and "
    f"PRNG-Cramer (mean corr={corr_prng_mean:+.3f}) stay flat; "
    f"var(N/S)/var(N) real={vr_real:.3e} < piC={vr_piC:.3e}",
    hl_contrast and hl_cv_contrast,
)

# density-stat agreement: |S| scales like Li(X) for all three
dens_ok = (
    abs(fl_real["pi_X"] - fl_real["Li_X"]) / fl_real["Li_X"] < 0.05
    and abs(fl_pi["pi_X"] - fl_pi["Li_X"]) / fl_pi["Li_X"] < 0.15
)
info(f"density-stat relative error at X: real="
     f"{abs(fl_real['pi_X'] - fl_real['Li_X']) / fl_real['Li_X']:.4f}, "
     f"piC={abs(fl_pi['pi_X'] - fl_pi['Li_X']) / fl_pi['Li_X']:.4f}")
check(
    "P3 density statistics: real and pi-Cramer both reproduce Li(X) "
    "count scale (rel err real<5%, piC<15%) -- pi digits work as a "
    "neutral Cramer randomness source for DENSITY, not for arithmetic",
    dens_ok,
)


# ================================================================ S4/P4
print("\nS4 / P4 -- verdict + answer to the project-lead question")
# look-elsewhere total declared
N_STATS_DECLARED = M_P1 + M_P2  # signal-family stats; P3 is contrast not null hunt
info(f"declared look-elsewhere count (P1+P2 signal families) = "
     f"{N_STATS_DECLARED} (m_P1={M_P1}, m_P2={M_P2})")
info(f"P1_NULL={P1_NULL}, P2_NULL={P2_NULL}, HL_contrast={hl_contrast}")

# UNDERPOWERED only if we could not run the preregistered X or HL
underpowered = (X < 100_000) or (N_DIGITS < 100_000) or (S_real.size < 1000)

if underpowered:
    VERDICT = "UNDERPOWERED"
elif (not P1_NULL or not P2_NULL) and n_windows_raw_lt >= 2:
    # replicated anomaly across windows after seeing raw hits in >=2 windows
    # and corrected signal
    VERDICT = "PI-ANOMALY"
elif P1_NULL and P2_NULL and hl_contrast and hl_cv_contrast and parity_contrast:
    VERDICT = "PI-NULL-ARITHMETIC-DISTINCT"
elif not P1_NULL or not P2_NULL:
    # single-window / unreplicated wiggle -- still type as anomaly if
    # corrected signal, else fall through to null-with-caveat via ANOMALY
    VERDICT = "PI-ANOMALY" if (not P1_NULL or not P2_NULL) else "UNDERPOWERED"
else:
    VERDICT = "UNDERPOWERED"

info(f"VERDICT = {VERDICT}")

check(
    f"P4 verdict is one of the three preregistered enums: got {VERDICT}",
    VERDICT in {
        "PI-NULL-ARITHMETIC-DISTINCT",
        "PI-ANOMALY",
        "UNDERPOWERED",
    },
)

# Two-sentence answer (German, simple) -- also print English machine line
if VERDICT == "PI-NULL-ARITHMETIC-DISTINCT":
    ANSWER_DE = (
        "Nein — die π-Ziffern an Primstellen sind uniform, und die "
        "Kreuzkorrelationen mit dem Primindikator sind nach Entfernen der "
        "1/log-n-Dichte null. "
        "Der Unterschied zwischen echten Primzahlen und π-getriebenem Zufall "
        "ist genau die arithmetische Paarkorrelation (Hardy–Littlewood), die "
        "kein Zufallsmodell trägt."
    )
elif VERDICT == "PI-ANOMALY":
    ANSWER_DE = (
        "Unerwartetes Signal nach Look-elsewhere-Korrektur in P1/P2 — "
        "konservativ als PI-ANOMALY typisiert, Replikation nötig. "
        "Der Hardy–Littlewood-Kontrast in P3 bleibt separat zu lesen."
    )
else:
    ANSWER_DE = (
        "Budget oder Trennschärfe reichten nicht für eine scharfe Aussage. "
        "Die gemessenen Teilstücke sind dokumentiert; keine Numerologie."
    )

print("\n--- Zwei-Satz-Antwort (Projektleiter-Frage) ---")
print(ANSWER_DE)

check(
    "P4 two-sentence answer emitted and non-empty",
    len(ANSWER_DE) > 40 and (("—" in ANSWER_DE) or ("Budget" in ANSWER_DE)),
)

# Final consistency: for the expected path, assert the null+contrast package
if VERDICT == "PI-NULL-ARITHMETIC-DISTINCT":
    check(
        "P4 package PI-NULL-ARITHMETIC-DISTINCT: P1 null, P2 null, "
        "parity gap contrast, HL contrast all hold together",
        P1_NULL and P2_NULL and parity_contrast
        and hl_contrast and hl_cv_contrast,
    )


# ================================================================ summary
print("\n" + "=" * 72)
print("SUMMARY TABLES")
print("=" * 72)
print("P1 p-values:")
print(f"  {'test':40s} {'p_raw':>12s} {'p_corr':>12s}")
print(f"  {'chi2 prime digits':40s} {p_chi2_p:12.6g} {p_chi2_corr:12.6g}")
print(f"  {'KS   prime digits':40s} {p_ks_p:12.6g} {p_ks_corr:12.6g}")
for seed, pv in zip(RANDOM_SEEDS, rng_null_ps):
    print(f"  {f'chi2 random seed={seed} (control)':40s} {pv:12.6g} {'--':>12s}")
print(f"  {'chi2 composites (control)':40s} {p_comp:12.6g} {'--':>12s}")

print("\nP2 correlations (block-perm):")
print(f"  {'window':16s} {'feat':8s} {'r':>10s} {'p_perm':>10s}")
for lo, hi, fname, r, pperm in p2_rows:
    print(f"  [{lo},{hi}]{'':3s} {fname:8s} {r:+10.5f} {pperm:10.4f}")

print("\nP3 triple comparison:")
print(f"  {'model':12s} {'|S|':>8s} {'|pi-Li|':>10s} {'odd_gap':>8s} "
      f"{'corr(N,S)':>10s} {'varR':>10s}")
print(f"  {'real':12s} {S_real.size:8d} {fl_real['err_at_X']:10.1f} "
      f"{g_real['odd_frac']:8.4f} {corr_real:+10.4f} {vr_real:10.4e}")
print(f"  {'pi-Cramer':12s} {S_piC.size:8d} {fl_pi['err_at_X']:10.1f} "
      f"{g_pi['odd_frac']:8.4f} {corr_piC:+10.4f} {vr_piC:10.4e}")
for i, (s, f, g, c, vr) in enumerate(
    zip(S_prng, fl_prng, g_prng, corr_prng, vr_prng)
):
    print(f"  {f'PRNG-{PRNG_CRAMER_SEEDS[i]}':12s} {s.size:8d} "
          f"{f['err_at_X']:10.1f} {g['odd_frac']:8.4f} {c:+10.4f} "
          f"{vr:10.4e}")

elapsed = time.time() - T0
print(f"\nVERDICT: {VERDICT}")
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
raise SystemExit(0 if FAIL == 0 else 1)
