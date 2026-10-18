"""Discovery probe (2026-07-26), part 94 — contract PRIME.BLIND.DEMO.

THE HONEST "TFPT PREDICTS PRIMES" DEMONSTRATOR: primality PREDICTION on a
BLIND WINDOW the construction has never seen, from pure compiler geometry
(lattice shell counting / theta towers), with NO divisibility tests, NO
sieve and NO primality calls anywhere in the prediction path (AST-enforced).

HONESTY FRAME (read first — this bounds the claim):
  * The demonstrator shows that the compiler counting structures CARRY the
    prime information COMPLETELY and reproduce it blind.  It is NOT a new
    or faster primality algorithm: the lattice counting costs O(N) exact
    multiply-adds PER candidate (~5·10^9 for the window) while a sieve
    settles the whole range in O(N log log N); the measured cost factor is
    reported below and the sieve wins by orders of magnitude — exactly as
    expected, and said plainly.
  * It is NOT a spectral prediction.  Predicting primes from the ZERO side
    (explicit formula, zero sums) would require the archimedean/GL(1)
    layer = I5/RH — that fence stays closed; no Riemann zeros are loaded
    anywhere (AST zero-firewall as in T68).
  * CLASSICAL MATHEMATICS NAMED AS CLASSICAL: Jacobi's four-square theorem
    (1834) theta3(q)^4 = 1 + 8 sum_{n>=1} (sum_{d|n, 4 nmid d} d) q^n,
    i.e. r4(n) = 8 sigma(n) for odd n (weight-2 Eisenstein structure of
    the theta tower); the divisor reading sigma(n) = n+1 <=> n prime is
    elementary number theory.  Primality readability from representation
    numbers is classical.  NEW here is only the compiler-native pipeline
    (theta3 = theta_Z is the elementary factor of the v535/v536 census
    theta stack; Z^4 is the rank-|mu4| = 4 tower axis; the Eisenstein
    channel of the mu4 glue census carries the sigma-twists — v535:
    Eisenstein eigenvalue sigma3(p) = 1 + p^3, census split
    c(p) = -8 a_p; here the same sigma-readability one weight down,
    sigma1(p) = 1 + p) and the strict BLIND PROTOCOL.

THE EXACT GEOMETRIC CRITERION (derived in P1, one line):
    odd n is prime  <=>  r4(n) = 8 (n + 1),
    where r4(n) = #{x in Z^4 : |x|^2 = n} is the Z^4 shell count
    (theta3^4 coefficient) — because r4(n) = 8 sigma(n) for odd n (Jacobi)
    and sigma(n) >= n + 1 with equality iff the divisor structure is
    minimal {1, n}, i.e. iff n is prime.  No learning, no fit: exact.

SECTIONS
  P0  FIREWALLS (both AST-checked on this file's own source):
      (a) zero-firewall — no Riemann-zero loaders anywhere (T68 pattern);
      (b) PREDICTION-PATH firewall — the named prediction functions
          contain no call to isprime/primerange/factorint/divisor_sigma/
          sieve/gcd & co., no sympy reference, and NO '%', '//' or '/'
          operator at all (no modulo division by test candidates, no
          divisibility logic; math.isqrt and integer +,-,* only).
  P1  THE GEOMETRIC CLASSIFIER (training window n <= 20000 — the ONLY
      window the construction ever sees):
      (i)   sympy symbolic Jacobi check: theta3(q)^4 coefficients equal
            8 sum_{d|n, 4 nmid d} d for all n <= 64 (exact Poly algebra);
      (ii)  exact lattice route (the SAME prediction-path code used in
            P2): r4(n) = 8 sigma1(n) for ALL odd n <= 20000;
      (iii) criterion equivalence on training: r4(n) == 8(n+1) <=>
            sympy.isprime(n) for ALL odd n <= 20000 (n = 1 correctly
            excluded since r4(1) = 8 != 16);
      (iv)  teeth: offset placebo — among r4(n) == 8(n+c), c in [-8..8],
            ONLY c = +1 classifies the training window perfectly;
      (v)   rank honesty: the rank-2 counter r2 = theta3^2 alone (Gauss
            chi4 divisor CHARACTER, not divisor mass) cannot decide
            primality — explicit collision exhibited; rank 4 = |mu4| is
            the minimal theta power with full sigma-readability.
  P2  THE BLIND WINDOW (PREREGISTERED): predict primality on
      [1_000_001, 1_010_000] (10^4 integers, disjoint from training).
      Prediction path = pure lattice counting: exact int64 r2 table by
      Z x Z shell enumeration (T68 int64-theta discipline, no FFT
      rounding in the decision route), then r4(n) as exact BLAS dot
      products (all intermediates are integers < 2^53 => float64 exact;
      int64 spot re-summation + independent isqrt-enumeration r2 spot
      checks + FFT cross-route as guards).  The odd grid is enumerated
      arithmetically (1_000_001 + 2k — parity by construction, never
      computed); even window members are composite by protocol (the only
      even prime is 2, not in the window).  The prediction (count +
      MD5 hash) is FROZEN and printed BEFORE any truth is computed.
  P3  EVALUATION (truth side — sympy/sieve now allowed): compare the
      frozen prediction against sympy.primerange + an independent
      Eratosthenes sieve; hit rate MUST be 100.00% (the criterion is
      exact — any deviation is a bug); report #primes (~726 expected),
      false positives/negatives, and the COST HONESTY factor
      (lattice-path wall time vs simple sieve wall time).
  P4  SYNTHESIS + verdict.

PREREGISTERED CRITERIA
  P0: both firewalls pass (zero hits).
  P1: (i)-(iii) exact on the full training window; (iv) offset c = +1
      unique; (v) collision exists.
  P2: window completed within budget (< 900 s total), prediction frozen
      before truth; exactness guards (int64 spot, r2 direct spot, FFT
      cross-route) all agree.
  P3: 0 false positives AND 0 false negatives (hit rate 100.00%).
  VERDICTS (preregistered):
    BLIND-100     — 100% on the blind window, protocol held.
    CRITERION-GAP — the criterion is not exactly derivable / training
                    equivalence breaks (report which residue classes).
    PIPELINE-FAIL — implementation misses the window/budget (then a
                    smaller window, declared honestly).

FENCES (honest typing)
  * Structure-completeness demonstration ONLY — no algorithmic-advance
    claim (sieve wins the cost race; factor quantified), no RH evidence,
    no spectral (zeros -> primes) claim: that route stays bound to
    I5/RH and is NOT touched here.
  * Jacobi/theta divisor identities, sigma-functions, Eisenstein weight-2
    structure: classical.  New: compiler-native pipeline + blind protocol.

Firewall: discovery sandbox only — no promotion, no ledger / paper /
website / next.txt / README edits.  ZERO-FIREWALL (AST): no Riemann-zero
loaders.  PREDICTION-PATH FIREWALL (AST): sympy.isprime & co. and all
division/modulo operators are FORBIDDEN in the prediction path.
"""
from __future__ import annotations

import ast
import hashlib
import inspect
import math
import time

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()

# ---------------------------------------------------------------- config
TRAIN_MAX = 20_000          # P1 training window (construction sees ONLY this)
W_LO = 1_000_001            # preregistered blind window, inclusive
W_HI = 1_010_000
NMAX = W_HI                 # lattice tables must reach the window top
BUDGET_S = 900.0
N_SPOT_INT64 = 32           # int64 re-summation spot checks in the window
N_SPOT_R2 = 200             # direct isqrt-enumeration r2 spot checks
PREDICTION_PATH_FUNCS = (
    "r2_table_lattice",
    "r4_shell_dot",
    "r4_shell_dot_int64",
    "predict_window_blind",
)
FORBIDDEN_PRED_CALLS = {
    "isprime", "primerange", "primepi", "nextprime", "prevprime",
    "primefactors", "factorint", "factor", "divisors", "divisor_count",
    "divisor_sigma", "totient", "sieve", "primorial", "gcd", "igcd",
    "ilcm", "mod", "fmod", "divmod", "remainder", "mod_inverse",
}


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


# ==================================================== prediction path
# The four functions below ARE the prediction path.  AST-enforced in P0:
# no primality/divisor/sieve calls, no sympy, no %, //, / operators —
# integer +,-,* lattice counting and exact dot products only.
def r2_table_lattice(nmax):
    """Exact r2(m) = #{(x,y) in Z^2 : x^2+y^2 = m} for all 0 <= m <= nmax.

    Pure Z x Z lattice shell enumeration (theta3^2 tower), int64.  Sign
    multiplicity: weight 1 for a zero coordinate, 2 otherwise."""
    xmax = math.isqrt(nmax)
    sq = np.arange(xmax + 1, dtype=np.int64) ** 2
    w = np.full(xmax + 1, 2, dtype=np.int64)
    w[0] = 1
    r2 = np.zeros(nmax + 1, dtype=np.int64)
    for x in range(xmax + 1):
        rest = nmax - int(sq[x])
        k = int(np.searchsorted(sq, rest, side="right"))
        # distinct y => distinct indices => fancy += is exact here
        r2[int(sq[x]) + sq[:k]] += w[x] * w[:k]
    return r2


def r4_shell_dot(r2f, revf, nmax, ns):
    """Exact r4(n) = sum_{k=0..n} r2(k) r2(n-k) via float64 BLAS dots.

    Exactness proof: all r2 >= 0 are integers <= ~10^3, every product is
    an integer <= ~10^6 and every partial sum is an integer <= r4(n)
    < 2^53, so each float64 operation (any summation order, FMA or not)
    is exact.  revf[j] = r2f[nmax - j]."""
    out = np.empty(len(ns), dtype=np.int64)
    for i, n in enumerate(ns):
        out[i] = int(round(float(np.dot(r2f[: n + 1], revf[nmax - n:]))))
    return out


def r4_shell_dot_int64(r2, n):
    """Pure-int64 re-summation of the same shell dot (spot-check guard)."""
    return int(np.dot(r2[: n + 1], r2[n::-1]))


def predict_window_blind(r2f, revf, nmax, lo, hi):
    """THE BLIND PREDICTION.  Odd grid lo, lo+2, ..., hi-1 enumerated
    arithmetically (parity by construction — never computed); criterion
    r4(n) == 8 (n + 1) applied to exact lattice counts.  Even window
    members are composite by protocol (2 is not in the window)."""
    odd_ns = list(range(lo, hi + 1, 2))
    r4_vals = r4_shell_dot(r2f, revf, nmax, odd_ns)
    predicted = [n for n, v in zip(odd_ns, r4_vals) if v == 8 * (n + 1)]
    return odd_ns, r4_vals, predicted


# ==================================================== evaluation helpers
def r2_direct(m):
    """Independent r2 via isqrt perfect-square detection (guard only)."""
    c = 0
    x = 0
    while x * x <= m:
        y2 = m - x * x
        y = math.isqrt(y2)
        if y * y == y2:
            c += (1 if x == 0 else 2) * (1 if y == 0 else 2)
        x += 1
    return c


def simple_sieve(n):
    """Plain Eratosthenes (EVALUATION side only — the cost baseline)."""
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if is_p[p]:
            is_p[p * p:: p] = False
    return is_p


# ================================================================ P0
print("=" * 72)
print("P0 -- FIREWALLS (AST on this file's own source)")
print("=" * 72)

_SRC = inspect.getsource(inspect.getmodule(check))
_TREE = ast.parse(_SRC)

# (a) zero-firewall (T68 pattern): no Riemann-zero loaders anywhere
_FORBIDDEN_ZERO = {
    "zeta" + "zero", "zeta" + "_zero", "zeta" + "_zeros",
    "siegel" + "z", "riemann" + "zeros", "riemann" + "_zero",
}
_hits_zero = set()
for node in ast.walk(_TREE):
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name) and f.id in _FORBIDDEN_ZERO:
            _hits_zero.add(f.id)
        elif isinstance(f, ast.Attribute) and f.attr in _FORBIDDEN_ZERO:
            _hits_zero.add(f.attr)
    elif isinstance(node, ast.Attribute) and node.attr in _FORBIDDEN_ZERO:
        _hits_zero.add(node.attr)
    elif isinstance(node, ast.Name) and node.id in _FORBIDDEN_ZERO:
        _hits_zero.add(node.id)
check(f"P0a ZERO-FIREWALL: no Riemann-zero loader in the whole file "
      f"(hits = {sorted(_hits_zero)})", len(_hits_zero) == 0)

# (b) prediction-path firewall: isprime & co. + division operators banned
_fn_nodes = {
    node.name: node for node in ast.walk(_TREE)
    if isinstance(node, ast.FunctionDef) and node.name in PREDICTION_PATH_FUNCS
}
_bad_calls, _bad_ops, _bad_sympy = [], [], []
_DIV_OPS = (ast.Mod, ast.FloorDiv, ast.Div)
for fname in PREDICTION_PATH_FUNCS:
    fn = _fn_nodes.get(fname)
    if fn is None:
        _bad_calls.append(f"{fname}:MISSING")
        continue
    for node in ast.walk(fn):
        if isinstance(node, ast.Call):
            f = node.func
            cname = f.id if isinstance(f, ast.Name) else (
                f.attr if isinstance(f, ast.Attribute) else "")
            if cname in FORBIDDEN_PRED_CALLS:
                _bad_calls.append(f"{fname}:{cname}")
        if isinstance(node, (ast.BinOp, ast.AugAssign)) and isinstance(
                node.op, _DIV_OPS):
            _bad_ops.append(f"{fname}:{type(node.op).__name__}")
        if isinstance(node, ast.Name) and node.id in ("sp", "sympy"):
            _bad_sympy.append(f"{fname}:{node.id}")
        if isinstance(node, ast.Attribute) and node.attr in ("sympy",):
            _bad_sympy.append(f"{fname}:{node.attr}")
check("P0b PREDICTION-PATH FIREWALL: all 4 prediction functions present; "
      "no isprime/primerange/factorint/divisor/sieve/gcd calls, no sympy "
      "reference, and NO '%', '//', '/' operator inside them "
      f"(calls = {_bad_calls}; ops = {_bad_ops}; sympy = {_bad_sympy})",
      len(_fn_nodes) == 4 and not _bad_calls and not _bad_ops
      and not _bad_sympy)
firewall_ok = (FAIL == 0)
info("prediction path = pure lattice counting: math.isqrt + int +,-,* "
     "+ exact dots; parity by arithmetic grid construction only.")

# ================================================================ P1
print()
print("=" * 72)
print("P1 -- THE GEOMETRIC CLASSIFIER (training window n <= "
      f"{TRAIN_MAX}; sympy allowed HERE)")
print("=" * 72)

# (i) symbolic Jacobi: theta3^4 coefficients == 8 sum_{d|n, 4 nmid d} d
q = sp.symbols("q")
M_SYM = 64
th3_sym = 1 + 2 * sum(q ** (k * k) for k in range(1, math.isqrt(M_SYM) + 1))
poly4 = sp.Poly(sp.expand(th3_sym ** 4), q)
jac_ok = True
for n in range(1, M_SYM + 1):
    lhs = int(poly4.coeff_monomial(q ** n))
    rhs = 8 * sum(d for d in sp.divisors(n) if d % 4 != 0)
    if lhs != rhs:
        jac_ok = False
        break
check(f"P1i  Jacobi four-square (symbolic, sympy Poly): [q^n] theta3^4 == "
      f"8*sum(d | n, 4 nmid d) for ALL 1 <= n <= {M_SYM}", jac_ok)
info("for odd n every divisor is odd => r4(n) = 8 sigma1(n)  (weight-2 "
     "Eisenstein reading of the rank-|mu4| = 4 theta tower).")

# build the big lattice table ONCE (timed — this is the prediction path)
t_pred0 = time.time()
r2 = r2_table_lattice(NMAX)
t_table = time.time() - t_pred0
r2f = r2.astype(np.float64)
revf = r2f[::-1].copy()
info(f"exact int64 r2 table to N = {NMAX} built by Z x Z shell "
     f"enumeration in {t_table:.2f} s (max r2 = {int(r2.max())}, "
     f"sum = {int(r2.sum())} ~ pi*N = {math.pi * NMAX:.0f})")

# (ii) lattice route == 8*sigma1 on ALL odd training n (same code as P2)
train_odds = list(range(1, TRAIN_MAX + 1, 2))
r4_train = r4_shell_dot(r2f, revf, NMAX, train_odds)
sig_ok = all(int(v) == 8 * int(sp.divisor_sigma(n, 1))
             for n, v in zip(train_odds, r4_train))
check(f"P1ii r4(n) from the PREDICTION-PATH lattice code == 8*sigma1(n) "
      f"for ALL odd n <= {TRAIN_MAX} ({len(train_odds)} shells)", sig_ok)

# (iii) criterion equivalence on training
train_primes = set(sp.primerange(2, TRAIN_MAX + 1))
mism = [n for n, v in zip(train_odds, r4_train)
        if (int(v) == 8 * (n + 1)) != (n in train_primes)]
check(f"P1iii criterion r4(n) == 8(n+1) <=> isprime(n) for ALL odd "
      f"n <= {TRAIN_MAX} (mismatches = {mism[:5]}; n = 1 excluded since "
      f"r4(1) = {int(r4_train[0])} != 16)", len(mism) == 0)
criterion_exact = (len(mism) == 0 and sig_ok and jac_ok)
info("one-line derivation: sigma(n) >= n + 1 + (any proper divisor) with "
     "equality iff divisors = {1, n} iff n prime; Jacobi lifts sigma to "
     "the Z^4 shell count => odd n prime <=> r4(n) = 8(n+1).  EXACT.")

# (iv) teeth: offset placebo — only c = +1 classifies perfectly
perfect_cs = []
for c_off in range(-8, 9):
    bad = sum(1 for n, v in zip(train_odds, r4_train)
              if (int(v) == 8 * (n + c_off)) != (n in train_primes))
    if bad == 0:
        perfect_cs.append(c_off)
check(f"P1iv offset placebo: among r4 == 8(n+c), c in [-8, 8], ONLY "
      f"c = +1 is a perfect training classifier (perfect set = "
      f"{perfect_cs})", perfect_cs == [1])

# (v) rank honesty: r2 alone cannot decide primality
coll = None
for p_ in (3, 7, 11):
    for c_ in (21, 33, 57, 77):
        if int(r2[p_]) == int(r2[c_]) and c_ not in train_primes:
            coll = (p_, c_, int(r2[p_]))
            break
    if coll:
        break
check("P1v  rank honesty: the rank-2 counter alone (r2 = 4*sum chi4(d), "
      "divisor CHARACTER, no divisor mass) cannot decide primality — "
      f"collision prime/composite with equal r2: {coll}; rank 4 = |mu4| "
      "is the minimal theta power with full sigma-readability",
      coll is not None)

# ================================================================ P2
print()
print("=" * 72)
print(f"P2 -- THE BLIND WINDOW [{W_LO}, {W_HI}] (prediction path only; "
      "prediction frozen BEFORE truth)")
print("=" * 72)

check(f"P2a preregistration: window [{W_LO}, {W_HI}] is disjoint from the "
      f"training window (W_LO > {TRAIN_MAX}); odd grid start {W_LO} is "
      "odd by preregistered constant",
      W_LO > TRAIN_MAX and W_LO == 1_000_001 and W_HI == 1_010_000)

t_blind0 = time.time()
odd_ns, r4_blind, predicted = predict_window_blind(r2f, revf, NMAX, W_LO,
                                                   W_HI)
t_dots = time.time() - t_blind0
t_pred = t_table + t_dots
n_window = W_HI - W_LO + 1
info(f"prediction path timing: r2 table {t_table:.2f} s + "
     f"{len(odd_ns)} shell dots {t_dots:.2f} s = {t_pred:.2f} s "
     f"(~{len(odd_ns) * (NMAX + 1) / 1e9:.1f}e9 exact multiply-adds)")

# freeze the prediction BEFORE any truth is computed
_pred_blob = ",".join(str(n) for n in predicted).encode()
_pred_md5 = hashlib.md5(_pred_blob).hexdigest()
print(f"        FROZEN PREDICTION: {len(predicted)} primes claimed in "
      f"[{W_LO}, {W_HI}]  (md5 = {_pred_md5})")
info(f"head = {predicted[:5]}")
info(f"tail = {predicted[-5:]}")

# exactness guards (still zero truth content)
rng = np.random.default_rng(42)
spot_ns = sorted(rng.choice(odd_ns, size=N_SPOT_INT64, replace=False)
                 .tolist())
spot_ok = all(r4_shell_dot_int64(r2, n)
              == int(r4_blind[odd_ns.index(n)]) for n in spot_ns)
check(f"P2b exactness guard: pure-int64 re-summation == float64 BLAS dot "
      f"on {N_SPOT_INT64} random window shells", spot_ok)

spot_m = sorted(rng.integers(1, NMAX + 1, size=N_SPOT_R2).tolist())
r2_ok = all(r2_direct(m) == int(r2[m]) for m in spot_m)
check(f"P2c exactness guard: independent isqrt-enumeration r2(m) == "
      f"lattice table on {N_SPOT_R2} random m <= {NMAX}", r2_ok)

L = 1
while L < 2 * NMAX + 1:
    L *= 2
F = np.fft.rfft(r2f, L)
r4_fft = np.rint(np.fft.irfft(F * F, L)[: NMAX + 1]).astype(np.int64)
fft_ok = (all(int(r4_fft[n]) == int(v) for n, v in zip(odd_ns, r4_blind))
          and all(int(r4_fft[n]) == int(v)
                  for n, v in zip(train_odds, r4_train)))
check(f"P2d exactness guard: FFT cross-route (size {L}) reproduces every "
      "dot-route r4 on training AND window shells", fft_ok)
pipeline_ok = spot_ok and r2_ok and fft_ok

# ================================================================ P3
print()
print("=" * 72)
print("P3 -- EVALUATION (truth side: sympy/sieve NOW allowed)")
print("=" * 72)

truth = set(sp.primerange(W_LO, W_HI + 1))
t_sv0 = time.time()
is_p = simple_sieve(W_HI)
t_sieve = time.time() - t_sv0
truth_sieve = set(np.nonzero(is_p[W_LO: W_HI + 1])[0] + W_LO)
check("P3a truth cross-check: sympy.primerange == Eratosthenes sieve on "
      f"the window ({len(truth)} primes)", truth == truth_sieve)

pred_set = set(predicted)
fp = sorted(pred_set - truth)
fn = sorted(truth - pred_set)
hits = n_window - len(fp) - len(fn)
hit_rate = 100.0 * hits / n_window
est = n_window / math.log((W_LO + W_HI) / 2)
check(f"P3b BLIND RESULT: {len(truth)} primes in the window (log-density "
      f"heuristic ~{est:.0f}); false positives = {len(fp)}, false "
      f"negatives = {len(fn)}, hit rate = {hit_rate:.2f}% over all "
      f"{n_window} integers — MUST be 100.00%",
      len(fp) == 0 and len(fn) == 0)
if fp or fn:
    info(f"FP head = {fp[:10]}; FN head = {fn[:10]}")
blind_100 = (len(fp) == 0 and len(fn) == 0)

cost_factor = t_pred / max(t_sieve, 1e-9)
check("P3c COST HONESTY: the sieve settles the whole range faster than "
      f"the lattice path predicts the window — lattice {t_pred:.2f} s vs "
      f"sieve {t_sieve * 1e3:.1f} ms, factor ~{cost_factor:,.0f}x in "
      "favour of the sieve (this is a STRUCTURE demonstration, not an "
      "algorithm)", cost_factor > 10.0)
info("asymptotics: lattice O(N) multiply-adds PER candidate vs sieve "
     "O(N log log N) TOTAL — the sieve wins by design; said plainly.")

# ================================================================ P4
print()
print("=" * 72)
print("P4 -- SYNTHESIS + VERDICT")
print("=" * 72)

runtime = time.time() - T0
budget_ok = runtime < BUDGET_S
check(f"P4a budget: total runtime {runtime:.1f} s < {BUDGET_S:.0f} s "
      "(window completed, no fallback needed)", budget_ok)

if criterion_exact and blind_100 and firewall_ok and pipeline_ok \
        and budget_ok:
    verdict = "BLIND-100"
elif not criterion_exact:
    verdict = "CRITERION-GAP"
else:
    verdict = "PIPELINE-FAIL"
check(f"P4b VERDICT (preregistered): {verdict}", verdict == "BLIND-100")
info("THE STATEMENT: the compiler predicts the primes of a never-seen "
     "window exactly — from pure geometry (Z^4 shell counts of the "
     "rank-|mu4| theta tower), with no divisibility test in the "
     "prediction path.  This is STRUCTURE COMPLETENESS, not an "
     "algorithmic advance (the sieve wins the cost race, factor "
     f"~{cost_factor:,.0f}x); the SPECTRAL prediction (zeros -> primes "
     "in the blind window) stays bound to I5/RH — fence, not claimed.")

print()
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({time.time() - T0:.1f}s)")
raise SystemExit(0 if FAIL == 0 else 1)
