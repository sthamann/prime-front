"""Discovery probe (2026-07-25), part 49 of the zeta/prime investigation.
POSITIVITY MACHINE IN MINIATURE: the classical Rankin trick (Rankin 1939)
— the miniature of the Deligne mechanism that proved the only known RH
(function fields) — rebuilt IN-SUITE.  The suite "proves" its own
Ramanujan bound from positivity, and the missing structure over Z is
typed exactly.  Plus the Level-1 gate: Delta in the compiler theta monoid.

  M1  THE RANKIN TRICK (in-suite proof miniature).
      Classical mechanism (Rankin 1939): from (i) nonnegativity of the
      coefficients a_n^2 of D_ff(s) = sum a_n(f8)^2 n^{-s}, (ii) the
      pole at s = 4 (right edge of convergence; T38), and (iii) a
      Landau argument (Dirichlet series with nonnegative coefficients
      has its abscissa of convergence as a singularity), conclude
      a_n^2 = O(n^{4-1+eps})-style, hence |a_p| <= C p^{3/2+eps} —
      the Ramanujan bound up to eps — WITHOUT checking individual
      values.  Machine chain:
        (a) nonnegativity exact (coefficients to 10^4);
        (b) pole location via partial-sum growth
            sum_{n<=X} a_n^2 ~ C X^4/4  (fit exponent 4 +/- 0.05);
        (c) crude bound a_p^2 <= sum_{n<=p} a_n^2 <= C' p^4
            => |a_p| <= sqrt(C') p^2, and the sharpening via the
            sym^2 decomposition (T38: L(f x f) = zeta(s-3) L(sym^2);
            check positivity of sym^2 coefficients for the iterated
            trick — classical path to 3/2+eps vs crude 2).
      Every step is a check; the goal is the machine-verified
      CONCLUSION "positivity + pole location => eigenvalue bound",
      not the bound itself (already known from Deligne / T16).

  M2  TYPING THE Z-GAP (strategic deliverable).
      Exact typing of what the mechanism would need for xi(s):
        (i) a FAMILY of objects with nonnegative aggregated
            coefficients whose pole/singularity structure controls
            the LOCATION OF ZETA ZEROS (not eigenvalue magnitudes) —
            classical analogue: Weil positivity (already narrowed as
            contract ZETA.WEIL.RECOVERY);
        (ii) the function-field case has Frobenius / the family
            f^{otimes k} — over Z that object is missing (classical
            F1 problem).
      Checks: which in-suite objects CAN occupy the roles
      (family, positivity, pole) and which role is definitely vacant.
      No speculation sold as a result — the value is the exact map.

  M3  LEVEL-1 GATE.
      Exact (q-series, integer arithmetic to O(q^2000)):
        Delta = (theta2 theta3 theta4 / 2)^8 = eta^{24}
        (Jacobi identity theta2 theta3 theta4 = 2 eta^3, classical —
        both sides built independently: theta constants vs Euler
        product eta^{24});
        Delta is a Hecke eigenform (tau(mn)=tau(m)tau(n) coprime;
        tau(p^2)=tau(p)^2 - p^{11} ladder for p <= 13);
        Deligne bound |tau(p)| <= 2 p^{11/2} numerically (p <= 50);
        AND the same Rankin trick from M1 applied to
        sum tau(n)^2 n^{-s} (growth exponent 12 +/- 0.05) yields
        the tau bound mechanically — the mechanism is
        FAMILY-UNIVERSAL in-suite.
      => Level-1 cuspidal gate of the compiler monoid is open
      (functor map extended by Level 1; typed, no promotion).

PREREGISTERED CRITERIA
  M1.growth   : fitted exponent of sum_{n<=X} a_n(f8)^2 in [3.95, 4.05]
  M1.nonneg   : a_n(f8)^2 >= 0 for all n <= 10^4 (exact)
  M1.crude    : |a_p| <= sqrt(C') p^2 for odd p with p <= 200
  M1.sharp    : a_n^2 = O(n^{3+eps}) numerically (eps=0.1) on n <= 10^4
                => |a_p| = O(p^{3/2+eps})  [Landau coefficient form]
  M1.sym2pos  : typed check — whether sym^2 Dirichlet coeffs are
                nonnegative (iteration fires only if yes)
  M3.jacobi   : (th2 th3 th4 / 2)^8 == eta^{24} to O(q^2000)
  M3.growth   : fitted exponent of sum tau(n)^2 in [11.95, 12.05]
  M3.deligne  : |tau(p)| <= 2 p^{11/2} for all p <= 50
  Verdict     : MINIATURE-RUNS iff M1 chain closed AND M3 holds;
                else PARTIAL / FAIL

IMPORTANT SCOPE SENTENCE (firewall):
  This miniature proves EIGENVALUE BOUNDS from positivity + pole
  location.  It does NOT prove zero locations.  That distinction is
  the entire content of M2.  No RH-evidence language.

Firewall: discovery sandbox, NO promotion, no marker moves, no ledger /
paper / website edits; classical theorems (Rankin 1939, Landau,
Deligne, Jacobi, Weil) named as such — TFPT content is the exact
in-suite wiring of the mechanism and the typed Z-gap map.
"""

# =====================================================================
# CORRECTION OF RECORD (All-place Tate audit, 2026-09-05)
# ---------------------------------------------------------------------
# The module docstring above is preserved as the historical T49 record.
# Its M1.d/M1.d' claim is false: from nonnegative partial sums
# A(X)=sum_{n<=X} b_n=O(X^q) one gets only b_n<=A(n)=O(n^q), not
# b_n=O(n^(q-1+eps)).  The same invalid exponent drop was repeated for
# tau in M3.rankin.  The fitted finite-window constants K_need/K_tau
# make their own same-window inequalities true by construction.
# Rankin's actual 1939 argument uses a quantitative remainder in the
# Rankin--Selberg summatory asymptotic and differences that remainder;
# a pole/main-order statement alone is not that argument and does not
# give the claimed Deligne-strength exponent.
#
# The executable gates below are retyped accordingly.  They now carry
# an exact sparse counterexample, retain only the elementary exponent-2
# f8 bound (exponent 6 for tau), and label the sharp prime bounds as
# finite regressions against Deligne's external theorem.  The Jacobi,
# Hecke, Rankin--Selberg factorization, growth measurements, and typed
# zero-location gap are unchanged.  Current load-bearing record:
# verification/v1021_all_place_tate_rank_audit.py.
# NO RH CLAIM.
# =====================================================================

from __future__ import annotations

import math
import time

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()

CORRECTION_STATUS = "RANKIN_EXPONENT_DROP_FALSIFIED"

N_COEFF = 10000          # a_n(f8) / nonnegativity cutoff
N_DELTA = 2000           # Delta / Jacobi identity order
N_GROWTH_F8 = 10000      # partial-sum fit for f8
N_GROWTH_TAU = 2000      # partial-sum fit for tau
EPS_SHARP = 0.1          # Landau-style eps in O(n^{3+eps})
GROWTH_TOL = 0.05        # preregistered +/- 0.05 on exponents


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
    """prod_{n>=1} (1 - q^{d n})^e via integer in-place passes."""
    s = np.zeros(order + 1, dtype=object)
    s[0] = 1
    for k in range(d, order + 1, d):
        for _ in range(e):
            for i in range(order, k - 1, -1):
                s[i] = s[i] - s[i - k]
    return s


def conv_obj(a, b, order):
    out = np.zeros(order + 1, dtype=object)
    for i in range(order + 1):
        ai = a[i]
        if ai == 0:
            continue
        jmax = min(order - i, len(b) - 1)
        for j in range(jmax + 1):
            bj = b[j]
            if bj != 0:
                out[i + j] = out[i + j] + ai * bj
    return out


def pmul(a, b, order):
    res = [0] * (order + 1)
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j in range(min(len(b) - 1, order - i) + 1):
            if b[j]:
                res[i + j] += ai * b[j]
    return res


def fit_growth_exponent(partial_sums, x_min_frac=0.25):
    """Fit alpha in A(X) ~ C X^alpha from log-log regression on large X.

    Uses only X >= x_min_frac * X_max with A(X) > 0.
    Returns (alpha, logC, n_points).
    """
    xs = []
    ys = []
    n = len(partial_sums) - 1
    x0 = max(2, int(x_min_frac * n))
    for x in range(x0, n + 1):
        a = partial_sums[x]
        if a > 0:
            xs.append(math.log(x))
            ys.append(math.log(float(a)))
    if len(xs) < 10:
        return float("nan"), float("nan"), 0
    # least-squares: y = logC + alpha * x
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    alpha = num / den
    logC = my - alpha * mx
    return alpha, logC, len(xs)


# ================================================================ f8 table
print("=" * 72)
print("SETUP -- f8 = eta(2t)^4 eta(4t)^4  (T11/T38; S_4(Gamma0(8)))")
print("=" * 72)

f8 = np.roll(
    conv_obj(eta_pass(2, 4, N_COEFF), eta_pass(4, 4, N_COEFF), N_COEFF),
    1,
)
f8[0] = 0
a_f8 = [int(f8[n]) for n in range(N_COEFF + 1)]
HEAD_AP = {1: 1, 3: -4, 5: -2, 7: 24, 11: -44, 13: 22}
head_ok = all(a_f8[p] == v for p, v in HEAD_AP.items())
info(f"a_p(f8) head: {[(p, a_f8[p]) for p in (1, 3, 5, 7, 11, 13)]}")
check(
    "setup.f8: eta(2t)^4 eta(4t)^4 matches T11/T38 a_p head "
    "{1,3,5,7,11,13} = {1,-4,-2,24,-44,22}",
    head_ok,
)


# ################################################################ M1
print()
print("=" * 72)
print("M1 -- Rankin trick miniature (Rankin 1939, classical)")
print("=" * 72)
info("CORRECTION ACTIVE: nonnegativity + a pole/mean of order X^4 does")
info("NOT imply a pointwise n^(3+eps) coefficient bound.")
info("This run separates finite measurements, the elementary spike bound,")
info("and finite regressions against Deligne's external theorem.")

# ---- M1.a nonnegativity
print()
print("M1.a -- nonnegativity of D_ff coefficients a_n(f8)^2")
c2 = [a_f8[n] * a_f8[n] for n in range(N_COEFF + 1)]
nonneg = all(c >= 0 for c in c2)
# stronger: every coefficient is a square (hence nonnegative) by construction;
# also verify no accidental negatives from overflow (object ints)
n_pos = sum(1 for n in range(1, N_COEFF + 1) if c2[n] > 0)
n_zero = sum(1 for n in range(1, N_COEFF + 1) if c2[n] == 0)
info(f"n<= {N_COEFF}: {n_pos} positive a_n^2, {n_zero} zero (even n vanish)")
info(f"max a_n^2 on n<= {N_COEFF}: {max(c2)}")
check(
    f"M1.a nonnegativity: a_n(f8)^2 >= 0 for ALL n <= {N_COEFF} "
    f"(exact integer; {n_pos} strictly positive)",
    nonneg and c2[1] == 1 and n_pos > 0,
)

# ---- M1.b finite growth diagnostic; the pole is a separate classical input
print()
print("M1.b -- finite partial-sum growth diagnostic (preregistered 4 +/- 0.05)")
A = [0] * (N_GROWTH_F8 + 1)
running = 0
for n in range(1, N_GROWTH_F8 + 1):
    running += c2[n]
    A[n] = running
alpha_f8, logC_f8, npt_f8 = fit_growth_exponent(A, x_min_frac=0.3)
C_f8 = math.exp(logC_f8) if npt_f8 else float("nan")
info(f"A(X)=sum_{{n<=X}} a_n^2; fit on X in [0.3 Xmax, Xmax], n_pts={npt_f8}")
info(f"fitted exponent alpha = {alpha_f8:.6f}  (target 4 +/- {GROWTH_TOL})")
info(f"fitted prefactor C in A ~ C X^alpha : C = {C_f8:.6g}")
info(f"A({N_GROWTH_F8}) = {A[N_GROWTH_F8]};  "
     f"A/X^4 = {A[N_GROWTH_F8] / (N_GROWTH_F8 ** 4):.6g}")
# The s=4 Rankin--Selberg pole is a separate classical/T38 input.  The
# following finite fit is a consistency measurement, not a pole proof.
ratios = [1000, 2000, 4000, 8000, N_GROWTH_F8]
for x in ratios:
    if x <= N_GROWTH_F8:
        info(f"  A({x})/X^4 = {A[x] / (x ** 4):.8g}")
growth_ok = abs(alpha_f8 - 4.0) <= GROWTH_TOL
check(
    f"M1.b [N] growth diagnostic: fitted exponent of sum_{{n<=X}} a_n(f8)^2 "
    f"is {alpha_f8:.4f} in [3.95, 4.05] (preregistered); "
    f"A(X)/X^4 stays positive on the finite ladder.  The s=4 pole is "
    f"cited separately from the classical T38 Rankin--Selberg identity",
    growth_ok and A[N_GROWTH_F8] > 0,
)

# ---- M1.c crude bound |a_p| <= sqrt(C') p^2
print()
print("M1.c -- crude Rankin bound |a_p| <= sqrt(C') p^2 from partial sums")
# C' = max_{X>=1} A(X)/X^4  (must include small X: A(3)/3^4 = 17/81
# already exceeds the large-X plateau ~0.08)
C_prime = max(A[x] / (x ** 4) for x in range(1, N_GROWTH_F8 + 1))
C_prime_large = max(A[x] / (x ** 4) for x in range(50, N_GROWTH_F8 + 1))
info(f"C' = max_{{X>=1}} A(X)/X^4 = {C_prime:.8g} "
     f"(large-X plateau max_{{X>=50}} = {C_prime_large:.8g})")
# Elementary spike inequality (always true for nonnegative coeffs):
#   a_p^2 <= A(p) = sum_{n<=p} a_n^2
# Growth envelope A(X) <= C' X^4 then yields |a_p| <= sqrt(C') p^2.
crude_ok = True
spike_ok = True
crude_ratios = []
for p in sp.primerange(3, 201):
    p = int(p)
    if p > N_COEFF:
        break
    ap = a_f8[p]
    if ap * ap > A[p]:
        spike_ok = False
        info(f"SPIKE FAIL p={p}: a_p^2={ap*ap} > A(p)={A[p]}")
    bound = math.sqrt(C_prime) * (p ** 2)
    ratio = abs(ap) / (p ** 2) if p else 0.0
    crude_ratios.append(ratio)
    if abs(ap) > bound + 1e-9:
        crude_ok = False
        info(f"CRUDE FAIL p={p}: |a_p|={abs(ap)} > sqrt(C') p^2={bound:.6g}")
info(f"max |a_p|/p^2 for odd p<=200: {max(crude_ratios):.6g}; "
     f"sqrt(C')={math.sqrt(C_prime):.6g}")
check(
    f"M1.c crude: a_p^2 <= A(p) <= C' p^4 with C'={C_prime:.6g} "
    f"=> |a_p| <= sqrt(C') p^2 for all odd p <= 200 "
    f"(exponent 2; elementary from positivity + growth)",
    crude_ok and spike_ok and C_prime > 0,
)

# ---- M1.d correction: the mean-to-pointwise exponent drop is invalid
print()
print("M1.d -- CORRECTED: partial-sum growth does not lower the pointwise exponent")
info("For b_n>=0, A(X)=O(X^q) gives only b_n<=A(n)=O(n^q).")
info("The claimed b_n=O(n^(q-1+eps)) needs additional structure and")
info("does not follow from Landau's singularity theorem or the measured mean.")

# Strong exact counterexample preserving both advertised inputs.  Let
# b_n=4n^3 plus n^(18/5) at n=32^m.  The baseline has partial sum
# X^2(X+1)^2~X^4 and Dirichlet series 4*zeta(s-3), hence its simple pole
# at s=4.  The spike series is analytic there (ratio 2^(18-5s)=1/4 at
# s=4) and contributes O(X^(18/5))=o(X^4), but the spike-to-n^(31/10)
# ratio is n^(1/2), unbounded.
k_sym = sp.symbols("k_sparse", integer=True, positive=True)
spike_exp = sp.Rational(18, 5)
target_exp = sp.Rational(31, 10)
spike_ratio = sp.Integer(2 ** 18)
spike_sum_closed = spike_ratio * (spike_ratio ** k_sym - 1) / (spike_ratio - 1)
spike_partial_limit = sp.limit(spike_sum_closed / (32 ** k_sym) ** 4,
                               k_sym, sp.oo)
spike_ratio_limit = sp.limit(32 ** (sp.Rational(1, 2) * k_sym), k_sym, sp.oo)
rankin_exponent_drop_falsified = (
    spike_partial_limit == 0
    and spike_exp < 4
    and spike_exp - target_exp == sp.Rational(1, 2)
    and sp.Rational(2 ** 18, 2 ** 20) == sp.Rational(1, 4)
    and spike_ratio_limit == sp.oo
)
check(
    "M1.d.i exact sparse counterexample preserves A(X)~X^4 and the "
    "simple s=4 pole but violates b_n=O(n^(3+0.1))",
    rankin_exponent_drop_falsified,
)

# This finite-window K is retained only as a regression statistic.  Since it
# is defined as the maximum over the same window, the following inequality is
# an identity of the construction and has no asymptotic content.
K_need = 0.0
for n in range(1, N_COEFF + 1):
    if c2[n] == 0:
        continue
    K_need = max(K_need, c2[n] / (n ** (3.0 + EPS_SHARP)))
all_window_fit = all(
    c2[n] <= K_need * (n ** (3.0 + EPS_SHARP)) + 1e-9
    for n in range(1, N_COEFF + 1)
)
info(f"finite-window K_eps=max a_n^2/n^{{3+{EPS_SHARP}}} on n<={N_COEFF}: "
     f"{K_need:.6g} (descriptive only)")
check(
    "M1.d.ii finite-window max-K inequality is recorded as tautological, "
    "not as an asymptotic theorem",
    all_window_fit and K_need > 0,
)

# The sharp prime bound is Deligne's theorem.  This finite computation is a
# regression against that external theorem, not a proof or Rankin extraction.
deligne_f8_ratios = []
deligne_f8_ok = True
for p in sp.primerange(3, 201):
    p = int(p)
    ratio = abs(a_f8[p]) / (p ** 1.5)
    deligne_f8_ratios.append(ratio)
    if ratio > 2.0 + 1e-9:
        deligne_f8_ok = False
info(f"max |a_p|/p^{{3/2}} for odd p<=200: {max(deligne_f8_ratios):.6g}")
check(
    "M1.d.iii finite regression agrees with Deligne |a_p|<=2p^(3/2) "
    "for odd p<=200 (external theorem; not proved by this window)",
    deligne_f8_ok,
)
info("HONEST EXPONENT LEDGER: conditional on the global A(X)=O(X^4) "
     "Rankin--Selberg bound, positivity -> exponent 2; the finite fit "
     "does not prove that global input.  Deligne externally -> exponent 3/2.")

# ---- M1.e sym^2 positivity (iteration test)
print()
print("M1.e -- sym^2 coefficient positivity (iteration of the trick?)")
info("T38: L(f x f, s) = zeta(s-3) L(sym^2 f, s).")
info("Classical: for cusp forms L(sym^2) is ENTIRE (no pole at s=4);")
info("the RS pole of L(f x f) at s=4 is exactly the zeta(s-3) factor.")
info("Dirichlet coeff at p: A_p(sym^2)=alpha^2+alpha*beta+beta^2 "
     "= a_p^2-p^3.")

sym2_p = {}
n_neg = 0
n_pos_s = 0
n_zero_s = 0
for p in sp.primerange(3, 201):
    p = int(p)
    if p > N_COEFF:
        break
    Ap = a_f8[p] * a_f8[p] - p ** 3
    sym2_p[p] = Ap
    if Ap < 0:
        n_neg += 1
    elif Ap > 0:
        n_pos_s += 1
    else:
        n_zero_s += 1
info(f"A_p(sym^2)=a_p^2-p^3 for odd p<=200: "
     f"{n_pos_s} positive, {n_neg} negative, {n_zero_s} zero")
info(f"sample: p=3 -> {sym2_p.get(3)}; p=5 -> {sym2_p.get(5)}; "
     f"p=7 -> {sym2_p.get(7)}")
sym2_all_nonneg = (n_neg == 0)
# Build Dirichlet coeffs of L(sym^2) up to 200 via Euler factors (multiplicative)
# Local: 1 / [(1 - alpha^2 X)(1 - alpha beta X)(1 - beta^2 X)]
# with X = p^{-s}; Dirichlet series coeffs via power products.
# For typing we only need the prime coeffs + a few composites.


def sym2_dirichlet_coeffs(N):
    """Coefficients A(n) of L(sym^2 f8, s) for n <= N (odd part)."""
    A = [0] * (N + 1)
    A[1] = 1
    # multiplicative: for p^k use recurrence from local Euler factor
    # 1/[(1-s1 X + p^6 X^2)(1 - p^3 X)] with s1 = a_p^2 - 2 p^3
    # Generate via: expand prod_p local as Dirichlet series
    for n in range(2, N + 1):
        if n % 2 == 0:
            A[n] = 0  # f8 newform at level 8; sym^2 odd-supported proxy
            continue
        # factor n
        fac = sp.factorint(n)
        val = 1
        ok = True
        for p, e in fac.items():
            p = int(p)
            if p == 2 or p > N_COEFF:
                ok = False
                break
            ap = a_f8[p]
            s1 = ap * ap - 2 * (p ** 3)
            # coeffs of 1/[(1 - s1 X + p^6 X^2)(1 - p^3 X)] = sum b_k X^k
            # recurrence: let den = 1 - (s1+p^3)X + (p^6 + s1 p^3)X^2 - p^9 X^3
            b = [0] * (e + 1)
            b[0] = 1
            c1 = s1 + p ** 3
            c2 = p ** 6 + s1 * (p ** 3)
            c3 = p ** 9
            for k in range(1, e + 1):
                bk = c1 * b[k - 1]
                if k >= 2:
                    bk -= c2 * b[k - 2]
                if k >= 3:
                    bk += c3 * b[k - 3]
                b[k] = bk
            val *= b[e]
        A[n] = int(val) if ok else 0
    return A


A_sym = sym2_dirichlet_coeffs(min(400, N_COEFF))
sym_neg_ns = [n for n in range(1, len(A_sym)) if A_sym[n] < 0]
sym_pos_ns = [n for n in range(1, len(A_sym)) if A_sym[n] > 0]
info(f"L(sym^2) Dirichlet coeffs n<= {len(A_sym)-1}: "
     f"{len(sym_pos_ns)} positive, {len(sym_neg_ns)} negative")
info(f"first negative n: {sym_neg_ns[:8]}")

# Typed checks: (1) sym^2 NOT nonnegative — iteration does NOT fire;
# (2) the local coefficient identity is checked symbolically.  Entireness
# of L(sym^2) and the global pole attribution remain declared classical
# external inputs, not executable checks of this finite probe.
check(
    "M1.e.i sym2-positivity TYPED: A_p(sym^2)=a_p^2-p^3 takes BOTH "
    f"signs on odd p<=200 ({n_neg} negative, {n_pos_s} positive) — "
    "raw sym^2 Dirichlet coefficients are NOT nonnegative; the "
    "ITERATED Rankin positivity trick does NOT fire on L(sym^2)",
    (not sym2_all_nonneg) and n_neg > 0 and len(sym_neg_ns) > 0,
)
alpha_sym, beta_sym = sp.symbols("alpha_sym beta_sym")
sym2_local_identity = sp.expand(
    alpha_sym**2 + alpha_sym * beta_sym + beta_sym**2
    - ((alpha_sym + beta_sym)**2 - alpha_sym * beta_sym)
)
check(
    "M1.e.ii local identity EXACT: alpha^2+alpha*beta+beta^2 "
    "=(alpha+beta)^2-alpha*beta.  The global entireness of L(sym^2), "
    "the s=4 pole attribution and Deligne's sharp bound are classical "
    "external inputs, not machine-proved by this finite probe",
    sym2_local_identity == 0,
)

# ---- M1 corrected audit closure
print()
print("M1 -- corrected audit closure")
m1_audit_ok = (
    nonneg and growth_ok and crude_ok and rankin_exponent_drop_falsified
    and all_window_fit and deligne_f8_ok
    and (not sym2_all_nonneg) and n_neg > 0
)
check(
    "M1 CORRECTED AUDIT: conditional on a global A(X)=O(X^4) bound, "
    "nonnegativity implies only the crude exponent-2 spike bound; the "
    "finite fitted growth is a regression, not that proof.  The claimed exponent drop is "
    "falsified by an exact sparse sequence; finite sharp data agree with "
    "Deligne externally; sym^2 positivity iteration does not fire",
    m1_audit_ok,
)


# ################################################################ M2
print()
print("=" * 72)
print("M2 -- typing the Z-gap (what xi(s) would need)")
print("=" * 72)
info("The Rankin mechanism has three ROLES:")
info("  R-FAMILY : a family of objects producing aggregated coeffs")
info("  R-POS    : nonnegativity of those aggregated coefficients")
info("  R-POLE   : pole/singularity structure controlling the TARGET")
info("For eigenvalue bounds the TARGET is |a_p|; for RH the TARGET")
info("would be the LOCATION OF ZETA ZEROS — a different target.")
info("Conditional on the classical global Rankin--Selberg summatory "
     "bound, this corrected audit derives only the elementary "
     "|a_n|=O(n^2) bound from positivity.  The finite fitted growth is "
     "diagnostic only; the sharp 3/2 bound is Deligne-external.  It "
     "proves no zero-location statement.")

# Role occupancy for EIGENVALUE side (occupied in-suite)
check(
    "M2.eig.FAMILY OCCUPIED: in-suite Hecke eigenforms f8 "
    "(eta(2t)^4 eta(4t)^4, T11) and Delta=eta^{24} (M3) sit in the "
    "compiler theta monoid and supply a_n / tau(n)",
    head_ok,  # f8 wired; Delta checked in M3 but role exists
)
check(
    "M2.eig.POS OCCUPIED: aggregated coefficients a_n(f8)^2 and "
    "tau(n)^2 are nonnegative by construction (squares) — the "
    "Rankin positivity hypothesis holds in-suite (M1.a)",
    nonneg,
)
check(
    "M2.eig.POLE OCCUPIED: D_ff has abscissa/pole at s=k=4 (T38 RS; "
    "M1.b growth alpha=4+/-0.05); for Delta the abscissa is s=12.  "
    "This controls the mean, not the sharp individual coefficients",
    growth_ok,
)

# Role occupancy for ZERO-LOCATION side (xi / zeta over Z)
info("")
info("ZERO-LOCATION SIDE (xi(s) over Z) — role map:")
info("  Classical analogue of R-POS for zeros: Weil positivity of the")
info("  explicit-formula quadratic form (Weil 1952; already narrowed")
info("  in-suite as contract ZETA.WEIL.RECOVERY — T40).")
info("  Classical analogue of R-FAMILY over function fields: Frobenius")
info("  conjugacy classes / the tensor powers f^{otimes k} (Deligne).")
info("  No corresponding over-Z family is constructed in this corpus;")
info("  this is an open F1-style realization problem, not a uniqueness claim.")

# What CAN occupy roles in-suite (candidates, not claims)
check(
    "M2.zero.POS CANDIDATE: Weil-positivity / explicit-formula Gram "
    "is the classical positivity role for zero locations; in-suite it "
    "is already narrowed as ZETA.WEIL.RECOVERY (T40) — a recovery "
    "contract, NOT a proof.  Role typed as CANDIDATE (occupied as "
    "contract, not as theorem)",
    True,
)
check(
    "M2.zero.POLE/SING CANDIDATE: the xi completed function has "
    "trivial zeros / archimedean Gamma factors as known singularities; "
    "critical zeros are the TARGET, not the controlling pole.  "
    "No in-suite object supplies a Rankin-style 'pole at the edge "
    "controls zero location' — role typed as STRUCTURALLY DIFFERENT "
    "(zeros are targets, not controlling poles)",
    True,
)
check(
    "M2.zero.FAMILY OPEN HERE (F1-style): over function fields the controlling "
    "family is Frobenius / f^{otimes k} (Deligne's proof of RH for "
    "varieties over finite fields, classical).  Over Z no inspected in-suite "
    "compiler object supplies an analogous family whose aggregated "
    "nonnegative coefficients have singularity structure controlling "
    "zeta-zero locations.  This is a corpus-status statement, not a proof "
    "that no such mathematical object can exist",
    True,
)

# Fence: do not sell speculation
check(
    "M2.fence: the corrected eigenvalue-side audit separates the proved "
    "mean/crude bound from Deligne's external sharp theorem; the "
    "no corresponding zero-location family is constructed in this corpus.  No bridge from "
    "M1 to RH is claimed",
    m1_audit_ok,
)

m2_map_ok = True  # all typing checks are structural PASS above


# ################################################################ M3
print()
print("=" * 72)
print("M3 -- Level-1 gate: Delta = (theta2 theta3 theta4 / 2)^8 = eta^{24}")
print("=" * 72)

# ---- build Delta from eta^{24}
eta24 = eta_pass(1, 24, N_DELTA)
Delta = [0] * (N_DELTA + 1)
for i in range(N_DELTA):
    Delta[i + 1] = int(eta24[i])
tau = Delta[:]  # tau(n) = coeff of q^n in Delta
info(f"Delta = q prod (1-q^n)^24 head: {tau[:10]}")
tau_head = [0, 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643]
check(
    "M3.eta: Delta = eta^{24} via Euler product matches classical "
    "tau head (1,-24,252,-1472,4830,-6048,-16744,84480,-113643)",
    tau[:10] == tau_head,
)

# ---- Jacobi side in t = q^{1/8}
print()
print("M3.jacobi -- (theta2 theta3 theta4 / 2)^8 vs eta^{24}")
TMAX = 8 * N_DELTA
th2 = [0] * (TMAX + 1)
m = 0
while True:
    e = (2 * m + 1) ** 2
    if e > TMAX:
        break
    th2[e] += 2
    m += 1
th3 = [0] * (TMAX + 1)
th3[0] = 1
n = 1
while True:
    e = 4 * n * n
    if e > TMAX:
        break
    th3[e] += 2
    n += 1
th4 = [0] * (TMAX + 1)
th4[0] = 1
n = 1
while True:
    e = 4 * n * n
    if e > TMAX:
        break
    th4[e] += 2 * ((-1) ** n)
    n += 1

P = pmul(pmul(th2, th3, TMAX), th4, TMAX)
# Jacobi: th2 th3 th4 = 2 eta^3  => half = eta^3 in matching units
half = [x // 2 for x in P]
assert all(x % 2 == 0 for x in P[: TMAX + 1])

# Also build 2 eta^3 in s = q^{1/24} and compare product identity
# (full O(q^2000) Delta identity is the 8th-power check below; here
# verify Jacobi itself to O(q^500) — same convention, lighter budget)
SMAX = 24 * 500
eta_s = eta_pass(24, 1, SMAX)  # prod (1 - s^{24n}) = prod (1-q^n) in s
eta_full = [0] * (SMAX + 1)
for i in range(SMAX):
    eta_full[i + 1] = int(eta_s[i])  # q^{1/24} * prod
eta3 = [0] * (SMAX + 1)
eta3[0] = 1
for _ in range(3):
    eta3 = pmul(eta3, eta_full, SMAX)
th2s = [0] * (SMAX + 1)
m = 0
while True:
    e = 3 * (2 * m + 1) ** 2
    if e > SMAX:
        break
    th2s[e] += 2
    m += 1
th3s = [0] * (SMAX + 1)
th3s[0] = 1
n = 1
while True:
    e = 12 * n * n
    if e > SMAX:
        break
    th3s[e] += 2
    n += 1
th4s = [0] * (SMAX + 1)
th4s[0] = 1
n = 1
while True:
    e = 12 * n * n
    if e > SMAX:
        break
    th4s[e] += 2 * ((-1) ** n)
    n += 1
Ps = pmul(pmul(th2s, th3s, SMAX), th4s, SMAX)
jacobi_id = all(Ps[i] == 2 * eta3[i] for i in range(SMAX + 1))
info(f"Jacobi identity th2 th3 th4 = 2 eta^3 in q^{{1/24}}-units "
     f"to O(q^{SMAX // 24}): {jacobi_id}")
check(
    f"M3.jacobi.i: theta2 theta3 theta4 = 2 eta^3 (Jacobi, classical) "
    f"exact in q^{{1/24}}-units to O(q^{SMAX // 24})",
    jacobi_id,
)

# Raise half = (th2 th3 th4)/2 to 8th power in t-units; extract q^n
pow8 = [0] * (TMAX + 1)
pow8[0] = 1
for _ in range(8):
    pow8 = pmul(pow8, half, TMAX)
side_theta = [pow8[8 * n] for n in range(N_DELTA + 1)]
delta_match = side_theta == Delta
n_mismatch = sum(1 for n in range(N_DELTA + 1) if side_theta[n] != Delta[n])
info(f"Delta vs (th2 th3 th4 / 2)^8 mismatches on n<= {N_DELTA}: {n_mismatch}")
info(f"theta-side head: {side_theta[:10]}")
check(
    f"M3.jacobi.ii: Delta = (theta2 theta3 theta4 / 2)^8 = eta^{{24}} "
    f"exact as q-series to O(q^{N_DELTA}) (both sides independent: "
    f"theta constants in t=q^{{1/8}} vs Euler product)",
    delta_match,
)
check(
    "M3.monoid: Delta lies in the compiler theta monoid "
    "(built from theta2, theta3, theta4 — Level-1 cuspidal gate open; "
    "typed, no promotion)",
    delta_match and jacobi_id,
)

# ---- Hecke eigenform
print()
print("M3.hecke -- Delta is a Hecke eigenform (tau multiplicative)")
hecke_coprime_ok = True
bad_cop = []
for m in range(1, 80):
    for n in range(1, 80):
        if math.gcd(m, n) != 1:
            continue
        if m * n > N_DELTA:
            continue
        if tau[m * n] != tau[m] * tau[n]:
            hecke_coprime_ok = False
            bad_cop.append((m, n))
            if len(bad_cop) >= 5:
                break
    if len(bad_cop) >= 5:
        break
info(f"coprime multiplicativity failures (m,n<=80): {len(bad_cop)}")

hecke_ladder_ok = True
ladder_bad = []
for p in sp.primerange(2, 14):
    p = int(p)
    # tau(p^2) = tau(p)^2 - p^{11}  (weight 12: p^{k-1} = p^{11})
    if p * p > N_DELTA:
        continue
    lhs = tau[p * p]
    rhs = tau[p] * tau[p] - (p ** 11) * tau[1]
    if lhs != rhs:
        hecke_ladder_ok = False
        ladder_bad.append((p, lhs, rhs))
    info(f"  p={p}: tau(p^2)={lhs}; tau(p)^2 - p^{{11}}={rhs}")
check(
    "M3.hecke.i: tau(mn)=tau(m)tau(n) for coprime m,n with mn<= "
    f"{N_DELTA} (checked m,n<=80)",
    hecke_coprime_ok and tau[1] == 1,
)
check(
    "M3.hecke.ii: tau(p^2)=tau(p)^2 - p^{11} for all primes p<=13 "
    "(Hecke ladder, weight 12; classical)",
    hecke_ladder_ok and len(ladder_bad) == 0,
)

# ---- Deligne bound for tau
print()
print("M3.deligne -- |tau(p)| <= 2 p^{11/2} for p <= 50 (classical)")
deligne_ok = True
deligne_ratios = []
for p in sp.primerange(2, 51):
    p = int(p)
    if p > N_DELTA:
        break
    bound = 2.0 * (p ** 5.5)
    ratio = abs(tau[p]) / (p ** 5.5)
    deligne_ratios.append((p, abs(tau[p]), ratio))
    if abs(tau[p]) > bound + 1e-9:
        deligne_ok = False
        info(f"DELIGNE FAIL p={p}: |tau|={abs(tau[p])} > {bound:.6g}")
info("p |tau(p)| |tau|/p^{11/2}:")
for p, at, r in deligne_ratios[:12]:
    info(f"  p={p}: |tau|={at}; ratio={r:.6f}")
info(f"max |tau(p)|/p^{{11/2}} for p<=50: "
     f"{max(r for _, _, r in deligne_ratios):.6f} (Deligne <= 2)")
check(
    "M3.deligne: |tau(p)| <= 2 p^{11/2} for ALL primes p <= 50 "
    "(Deligne bound, classical; numerical check)",
    deligne_ok and max(r for _, _, r in deligne_ratios) <= 2.0 + 1e-9,
)

# ---- Rankin mean diagnostic on tau (sharp step corrected)
print()
print("M3.rankin -- corrected mean/pointwise audit for sum tau(n)^2 n^{-s}")
c2_tau = [tau[n] * tau[n] for n in range(N_GROWTH_TAU + 1)]
A_tau = [0] * (N_GROWTH_TAU + 1)
run = 0
for n in range(1, N_GROWTH_TAU + 1):
    run += c2_tau[n]
    A_tau[n] = run
alpha_tau, logC_tau, npt_tau = fit_growth_exponent(A_tau, x_min_frac=0.3)
info(f"A_tau(X)=sum_{{n<=X}} tau(n)^2; n_pts={npt_tau}")
info(f"fitted exponent alpha_tau = {alpha_tau:.6f} "
     f"(target 12 +/- {GROWTH_TOL})")
info(f"A_tau({N_GROWTH_TAU})/{N_GROWTH_TAU}^{{12}} = "
     f"{A_tau[N_GROWTH_TAU] / (N_GROWTH_TAU ** 12):.6g}")
tau_growth_ok = abs(alpha_tau - 12.0) <= GROWTH_TOL
tau_nonneg = all(c >= 0 for c in c2_tau)

# Same-window descriptive constant only.  It cannot establish an
# asymptotic coefficient bound because it is fitted on the tested window.
K_tau = 0.0
for n in range(1, N_GROWTH_TAU + 1):
    if c2_tau[n] == 0:
        continue
    val = c2_tau[n] / (n ** (11.0 + EPS_SHARP))
    if val > K_tau:
        K_tau = val
info(f"finite-window K_tau=max tau(n)^2/n^{{11+{EPS_SHARP}}}: "
     f"{K_tau:.6g} (descriptive only)")
tau_window_fit_ok = True
for p in sp.primerange(2, 51):
    p = int(p)
    if p > N_GROWTH_TAU:
        break
    bound = math.sqrt(K_tau) * (p ** (5.5 + 0.5 * EPS_SHARP))
    if abs(tau[p]) > bound + 1e-9:
        tau_window_fit_ok = False
        info(f"TAU WINDOW-FIT FAIL p={p}")

# Exact q=12 analogue: baseline 12n^11 plus spikes n^(58/5) at
# n=32^m.  The baseline carries the s=12 pole/leading X^12 mean; the
# spike series is analytic there (geometric ratio 1/4) and lower-order,
# but exceeds n^(11+0.1) by n^(1/2).
tau_spike_exp = sp.Rational(58, 5)
tau_target_exp = sp.Rational(111, 10)
tau_spike_ratio = sp.Integer(2 ** 58)
tau_spike_sum_closed = (
    tau_spike_ratio * (tau_spike_ratio ** k_sym - 1) / (tau_spike_ratio - 1)
)
tau_spike_partial_limit = sp.limit(
    tau_spike_sum_closed / (32 ** k_sym) ** 12, k_sym, sp.oo
)
tau_ratio_limit = sp.limit(32 ** (sp.Rational(1, 2) * k_sym), k_sym, sp.oo)
tau_exponent_drop_falsified = (
    tau_spike_partial_limit == 0
    and tau_spike_exp < 12
    and tau_spike_exp - tau_target_exp == sp.Rational(1, 2)
    and sp.Rational(2 ** 58, 2 ** 60) == sp.Rational(1, 4)
    and tau_ratio_limit == sp.oo
)

check(
    f"M3.rankin.i: tau(n)^2 >= 0 for all n <= {N_GROWTH_TAU} "
    f"(positivity hypothesis)",
    tau_nonneg,
)
check(
    f"M3.rankin.ii [N]: fitted growth exponent of sum tau(n)^2 is "
    f"{alpha_tau:.4f} in [11.95, 12.05] (preregistered; weight-12 "
    f"finite diagnostic; the Rankin--Selberg pole is a separate classical input)",
    tau_growth_ok,
)
check(
    f"M3.rankin.iii: finite-window K_tau inequality on n<={N_GROWTH_TAU} "
    "is a descriptive same-window identity, not an asymptotic theorem",
    tau_window_fit_ok and K_tau > 0,
)
check(
    "M3.rankin.iv exact sparse counterexample preserves A(X)~X^12 and "
    "the s=12 pole but violates b_n=O(n^(11+0.1)); Deligne is external",
    tau_exponent_drop_falsified,
)

m3_ok = (
    delta_match and jacobi_id and hecke_coprime_ok and hecke_ladder_ok
    and deligne_ok and tau_nonneg and tau_growth_ok and tau_window_fit_ok
    and tau_exponent_drop_falsified
)
check(
    "M3 LEVEL-1 GATE OPEN: Delta = (th2 th3 th4 / 2)^8 = eta^{24} "
    "in the compiler theta monoid; Hecke eigenform; Deligne bound "
    "numerically as an external-theorem regression; mean growth measured; "
    "the former Rankin exponent extraction is explicitly falsified "
    "(functor map extended by Level 1 — typed, no promotion)",
    m3_ok,
)


# ################################################################ VERDICT
print()
print("=" * 72)
print("VERDICT")
print("=" * 72)

if m1_audit_ok and m3_ok:
    verdict = "RANKIN-EXPONENT-DROP-FALSIFIED; FINITE-IDENTITIES-SURVIVE"
elif m1_audit_ok or m3_ok:
    verdict = "PARTIAL"
else:
    verdict = "FAIL"

info(f"M1 corrected audit: {m1_audit_ok}")
info(f"M3 level-1 gate: {m3_ok}")
info(f"M2 role map: eig{{FAMILY,POS,POLE}}=OCCUPIED; "
     f"zero{{POS}}=CANDIDATE(Weil/ZETA.WEIL.RECOVERY); "
     f"zero{{FAMILY}}=NOT-CONSTRUCTED-IN-CORPUS(F1-style open)")
info(f"f8 growth alpha = {alpha_f8:.6f}; tau growth alpha = {alpha_tau:.6f}")
info(f"crude C' = {C_prime:.6g}; finite K_eps(f8) = {K_need:.6g}; "
     f"finite K_tau = {K_tau:.6g}")
info("CORRECTION: partial-sum growth controls the mean; no q->q-1+eps "
     "pointwise exponent drop follows.  Sharp prime bounds are Deligne-external.")
info("Open direction: construct an over-Z all-place object whose independently")
info("positive pairing represents the Weil form; this audit does not claim")
info("that a single missing family cell is sufficient or unique.")
info("Not a promotion candidate — role map / mechanism miniature only.")

check(
    f"VERDICT = {verdict} (M1 corrected={m1_audit_ok}, M3={m3_ok})",
    verdict == "RANKIN-EXPONENT-DROP-FALSIFIED; FINITE-IDENTITIES-SURVIVE"
    and CORRECTION_STATUS == "RANKIN_EXPONENT_DROP_FALSIFIED",
)

elapsed = time.time() - T0
print(f"\nTOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)", flush=True)
raise SystemExit(0 if FAIL == 0 else 1)
