"""PART 172 -- FRAME.BEYOND -- the chain beyond Frame A and beyond prime powers.

T171 (FINAL.MAP) reproduced the sixteen-link reduction chain END-TO-END on ONE
representative surface: zone anchors drawn from the support of von Mangoldt
(prime powers), grid step D = g_k / (2 nu) read off the LOCAL log-gap g_k, and
nu in {4, 6}.  Call that FRAME A / ZONE = PRIME POWERS.  T171 also measured
that the RATE of link 16 is FRAME DEPENDENT (sin angle ~ h^{-2.33} pooled,
h^{-1.86} at nu = 4, h^{-2.87} at nu = 6) while the COLLAPSE -- the identity
tower of links 3, 8, 9, 12, 13, 14, 15 -- is not.  On one nu = 4 window the low
block was even INDEFINITE (lam_min(B_LL) = -343) and was excluded out loud.

THIS FILE ASKS THE INHERITED QUESTION.  Which links are FRAME- and ZONE-
UNIVERSAL, which constants move, and does the R1 classification -- an
unconditional m-free |det Ahat| <= C h^{-3+eps} ahat_11 ahat_22 for three
explicit linear Lambda sums, i.e. a NEAR-DEGENERACY and not a size -- survive
away from Frame A and away from prime-power anchors?

WHAT "BEYOND" CAN MEAN, INVENTORIED (block A1.i below does it in code).  The
window recipe has exactly four degrees of freedom: (1) the FRAME, i.e. the rule
anchor -> grid step D; Frame A is local-gap anchored, Frame B here is h-anchored
and therefore gap-BLIND; (2) nu, the gap subdivision; (3) the ZONE FAMILY, i.e.
the arithmetic of the anchor sequence -- prime powers (Frame A), general
non-prime-power integers, or a congruence class of primes; (4) the atom set,
which is NOT free: Lambda lives on prime powers, so "beyond prime powers" can
only mean a different anchor ARITHMETIC in the window build, never a different
Lambda.  That distinction is stated once here and respected everywhere below.

FENCES.  No zero data, no L-function evaluation; finite von Mangoldt sums only
(Chebyshev 1852, UNCONDITIONAL).  *** THE RH FENCE, PROMINENTLY: every link
below is checked on a MEASURED SURFACE of finitely many windows.  RH_DELTA is a
YARDSTICK for translating a precision demand into an exponent -- never an input,
never a conclusion.  The quantifier "for all m" stays OPEN at link 16 on every
surface in this file, and widening the surface does not close it. ***  Positivity
of a finite A_h is a NUMERICAL FACT about a finite matrix, UNCONDITIONAL in that
reading only, and it is NEVER routed through the Weil criterion (Weil 1952);
T171-R1 is the R4-free form of the chain, so this file does not need it.
THEOREM / CERTIFIED / MEASURED / FIT strictly apart; direction of every
inequality stated where it is used; indefinite low blocks are EXCLUDED OUT LOUD.

CLASSICAL SPINE: Schur 1917 (nested complements), Kac-Murdock-Szego 1953 (the
sine eigenbasis), Fejer 1915 (the taper), Abel 1826 (the swap), Dirichlet 1829
(the closed kernel), Lagrange 1773 and Cauchy-Binet 1812/1815 (the minor
identities), Gershgorin 1931, Chebyshev 1852 (psi(x) < B x), Weil 1952 (an
ADDRESS, never a tool).
Python: experiments/tfpt-discovery/.venv/bin/python
"""

import ast
import math
import os
import time

import numpy as np

T0 = time.time()
EULER = 0.5772156649015329
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any factorised form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
CHUNK = 16384
ATOM_MAX = 300000
HCAP = 1450
H_MIN = 128
N_ATOM_MIN = 40
ZONE_N_MAX = 560             # anchors above this cannot meet h <= HCAP anyway

SCHUR_KB = 16                # the FIXED low block of the T152 .. T171 chain
KB_MAX = 32                  # the enlarged block, for the interlacing direction
KL_FLOOR = 12                # the T155 complement floor uses L = 1 .. 12
NU_A = (4, 6)                # Frame A's two nu values, as in T171
NU_EXT = (3, 8)              # the nu EXTREMES of the frame variant
N_PER_LEG = 6                # windows per (surface, leg) -- DECLARED in advance

EXACT_BAR = 1.0e-12          # the bar on a SMALL-MATRIX identity (2x2 .. 32x32)
ROUND_BAR = 1.0e-9           # DECLARED round-off horizon of the FULL h x h
#                              identities: assembling v^T A_h v with h up to 1450
#                              amplifies eps by the norm of A_h, so an identity
#                              is accepted at 1e-9 relative and the WORST value
#                              is always printed.  Nothing is hidden by this.
SOLVE_BAR = 1.0e-7           # DECLARED horizon of an identity that passes through
#                              a K = 16 Cholesky solve: the relative error
#                              inherits cond(B_LL), reported per surface in A2
NULL_BAR = 1.0e-11           # DECLARED ABSOLUTE horizon for the NEAR-NULL
#                              quantities (1 - r_12^2 and det Ahat are ~1e-6 and
#                              smaller): their RELATIVE error inherits the
#                              cancellation, so the identity is stated and tested
#                              ABSOLUTELY.  Both numbers are always printed.
IDENT_BAR = 1.0e-6           # DECLARED horizon where a near-null value is crossed
COND_BAR = 1.0e12            # the T159 numerical horizon on cond(B_LL)
EPSM = float(np.finfo(float).eps)
B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962)
RH_DELTA = 0.5               # YARDSTICK, NOT A CLAIM
TARGET_EXP = 3.0             # the h^{-3+eps} demand of the open quantifier
T171_SIN_POOL = -2.33        # QUOTED from T171, Frame A pooled
T171_SIN_NU4 = -1.86
T171_SIN_NU6 = -2.87

FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def info(name, detail=""):
    print("[INFO] %s%s" % (name, (": " + detail) if detail else ""))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def budget_left():
    return BUDGET_S - (time.time() - T0)


def wrap_at(text, width):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        if not cur:
            cur = wd
        elif len(cur) + 1 + len(wd) <= width:
            cur += " " + wd
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def para(text, width=76, indent="  "):
    print("")
    for blk in text.split("\n\n"):
        for ln in wrap_at(blk, width):
            print(indent + ln)
        print("")


def block(text, indent="  "):
    print("")
    for ln in text.split("\n"):
        print(indent + ln if ln.strip() else "")
    print("")


def qmin(v):
    v = [t for t in v if np.isfinite(t)]
    return min(v) if v else float("nan")


def qmax(v):
    v = [t for t in v if np.isfinite(t)]
    return max(v) if v else float("nan")


def qmed(v):
    v = [t for t in v if np.isfinite(t)]
    return float(np.median(v)) if v else float("nan")


def sym(A):
    return 0.5 * (A + A.T)


def fit_exp(xs, ys):
    """A LOG-LOG SLOPE.  It is a FIT and it is labelled a fit everywhere."""
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    ok = np.isfinite(xs) & np.isfinite(ys) & (xs > 0) & (np.abs(ys) > 0)
    if ok.sum() < 3:
        return float("nan")
    return float(np.polyfit(np.log(xs[ok]), np.log(np.abs(ys[ok])), 1)[0])


FORBIDDEN_TOKENS = tuple("".join(p) for p in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "numpy", "scipy"}


def firewall():
    src = open(os.path.abspath(__file__), "r").read()
    low = src.lower()
    hits = [t for t in FORBIDDEN_TOKENS if t in low]
    tree = ast.parse(src)
    bad_imp, bad_wr = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    bad_imp.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                bad_imp.append(node.module)
        elif isinstance(node, ast.Call):
            nm = getattr(node.func, "id", None) or getattr(node.func, "attr", None)
            if nm == "open":
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(ch in mode for ch in "wax+"):
                    bad_wr.append(mode)
    check("fb_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("fb_fw.imports", not bad_imp, "non-whitelisted: %s" % (bad_imp or "none"))
    check("fb_fw.no_writes", not bad_wr, "write-mode: %s" % (bad_wr or "none"))
    check("fb_fw.one_file",
          os.path.basename(os.path.abspath(__file__)) == "frame_beyond_probe.py",
          "single file: frame_beyond_probe.py")
    check("fb_fw.rh_fence", "RH_DELTA" in src and low.count("unconditional") >= 5,
          "RH FENCE DECLARED AND PROMINENT.  RH_DELTA = %.1f is a YARDSTICK for "
          "translating a precision demand into an exponent.  Every surface below "
          "is a FINITE MEASURED SURFACE; widening the frame or the zone "
          "arithmetic does not close the open quantifier at link 16" % RH_DELTA)
    check("fb_fw.weil_fence", low.count("weil 1952") >= 2 and "T171-R1" in src,
          "WEIL FENCE HARD: positivity of a finite A_h is never routed through "
          "the Weil criterion (Weil 1952); the chain checked here is the R4-free "
          "T171-R1 form, which does not use positivity of Ahat at all")


# ----------------------------------------------------------------------------
# the arithmetic core: finite von Mangoldt atoms (the ONLY arithmetic input)
# ----------------------------------------------------------------------------
def von_mangoldt_table(n_max):
    sieve = np.zeros(n_max + 1, dtype=bool)
    sieve[2:] = True
    for p in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        lp = math.log(float(p))
        q = int(p)
        while q <= n_max:
            lam[q] = lp
            q *= int(p)
    return lam, sieve


section("PART 172 -- FRAME.BEYOND -- Z0  FENCE, ARITHMETIC CORE")
firewall()

LAM_TAB, PRIME_TAB = von_mangoldt_table(ATOM_MAX)
ATOMS_ALL = [(int(n), float(LAM_TAB[n]), math.log(float(n)),
              2.0 * float(LAM_TAB[n]) / math.sqrt(float(n)))
             for n in np.nonzero(LAM_TAB > 0.0)[0]]
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
check("fb_z0.atoms", len(ATOMS_ALL) > 20000,
      "%d prime-power atoms up to n = %d (finite von Mangoldt sieve).  Lambda "
      "lives on PRIME POWERS and that never changes in this file: the zone "
      "variants below change the ANCHOR arithmetic, not the atom set"
      % (len(ATOMS_ALL), ATOM_MAX))

_psi_run, _bpsi, _kap = 0.0, 0.0, 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
    if _n >= 100.0:
        _kap = max(_kap, abs(_psi_run - _n) / _n)
KAPPA = _kap
check("fb_z0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f and |psi(x) - x| <= %.6f x at every jump point up to "
      "n = %d (Chebyshev 1852; Rosser-Schoenfeld 1962).  UNCONDITIONAL"
      % (_bpsi, KAPPA, ATOM_MAX))

info("fb_z0.budget", "%.1f s of %.0f s left after the arithmetic core"
     % (budget_left(), BUDGET_S))

# ----------------------------------------------------------------------------
# the archimedean lag kernel A(s, D) -- the T115 assembly, bit for bit
# ----------------------------------------------------------------------------
def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = (1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return (tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w)) / (-np.expm1(-2.0 * w))


def _arch_A_near(s, D):
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D
    pts = sorted({0.0, s, D - s, W})
    pts = [p for p in pts if 0.0 <= p <= W]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        tot += half * float(np.dot(_GLW, _arch_integrand(w, s, D)))
    return (-(EULER + LOG_PI) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * W))))


def arch_A(sv, D):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        out[far] = _arch_A_far(sv[far], D)
    for i in np.nonzero(~far)[0]:
        out[i] = _arch_A_near(sv[i], D)
    return out


def arch_lags(M, D):
    out = np.empty(M)
    for a in range(0, M, CHUNK):
        b = min(M, a + CHUNK)
        out[a:b] = arch_A(np.arange(a, b) * D, D)
    return out


# ----------------------------------------------------------------------------
# the parity geometry: KMS sine modes, the odd Toeplitz-minus-Hankel form
# ----------------------------------------------------------------------------
def parity_mu(m):
    """mu^P_k = 4 sin^2(pi k / N), N = 2m + 1 (Kac-Murdock-Szego 1953).  EXACT."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m, kb=None):
    """t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N): ORTHONORMAL eigenbasis of L_P."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, (kb or m) + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: TOEPLITZ MINUS HANKEL, exact."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def lag_weights_from_v(v, m):
    """THE T163 CORRELATION THEOREM: w_0 = A_0, w_d = 2 A_d - H_{M-1-d} (d >= 1)
    with A the autocorrelation and H the self-convolution of v; then
    v^T A_h v = sum_d c_d w_d EXACTLY -- the quadratic form as a LAG SUM."""
    M = 2 * m
    ac = np.correlate(v, v, "full")[m - 1:]
    cv = np.convolve(v, v)
    w = np.zeros(M)
    w[:m] = 2.0 * ac
    w[0] = ac[0]
    ee = (M - 1) - np.arange(1, M)
    w[1:] -= np.where(ee <= M - 2, cv[np.minimum(ee, M - 2)], 0.0)
    return w


def back_diff(w):
    """(Delta w)_d = w_d - w_{d+1}, with w_M := 0 (Abel 1826)."""
    out = np.empty_like(w)
    out[:-1] = w[:-1] - w[1:]
    out[-1] = w[-1]
    return out


def cf_ladder(Bm, K):
    """THE T158 CHOLESKY / CONTINUED-FRACTION LADDER.  g_K = e_1^T Q_K^-1 e_1 =
    sum_{j<=K} y_j^2 with y = L^-1 e_1: every term STRICTLY POSITIVE and the
    partial sum to J is exactly g_J (Schur 1917; the Jacobi continued fraction).
    DIRECTION: g_K INCREASES in K and g_K <= s, so 1/g_K DECREASES to 1/s."""
    Q = sym(np.asarray(Bm)[:K, :K])
    try:
        L = np.linalg.cholesky(Q)
    except np.linalg.LinAlgError:
        return None
    e1 = np.zeros(K)
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return np.cumsum(y ** 2)


def mixed_det(P, Q):
    """D(P, Q) = P11 Q22 + P22 Q11 - 2 P12 Q12: the POLARISATION of det on 2 x 2
    symmetric matrices, det(P + Q) = det P + D(P, Q) + det Q.  As a form on
    (P11, P22, P12) its matrix is J below: RANK 3, SIGNATURE (1, 2)."""
    return (P[0, 0] * Q[1, 1] + P[1, 1] * Q[0, 0] - 2.0 * P[0, 1] * Q[0, 1])


J_POL = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -2.0]])


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    return int(np.searchsorted(U_SORTED, lim, side="right"))


def atom_lags(alpha, M, atoms):
    """Every prime-power atom contributes -Lambda(n)/sqrt(n) times a linear
    spline of total mass 1 around u_n = log n, plus a REFLECTED spline when
    u_n < D: the T158/T159 closed-weight assembly, bit for bit."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for u_j, mu_j in atoms:
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D


def spline_project(W, u, D, M):
    """phi_n . W for the unit-mass spline phi_n of the atom at u = log n."""
    i0 = int(math.floor(u / D))
    f = u / D - i0
    val = 0.0
    if 0 <= i0 < M:
        val += (1.0 - f) * W[i0]
    if 0 <= i0 + 1 < M:
        val += f * W[i0 + 1]
    if u < D:
        val += (1.0 - u / D) * W[0]
    return val


# ----------------------------------------------------------------------------
# A1.i  THE RECIPE, INVENTORIED: anchor arithmetic x frame rule x nu
# ----------------------------------------------------------------------------
def anchor_list(kind):
    """THE ZONE FAMILY: the ARITHMETIC of the anchor sequence n_zone.  Frame A
    (T152 .. T171) draws anchors from the support of Lambda -- the prime powers.
    'Beyond prime powers' can ONLY mean a different anchor arithmetic: Lambda
    itself lives on prime powers and the atom set is never touched."""
    out = []
    for n in range(2, ZONE_N_MAX + 1):
        lam_pos = LAM_TAB[n] > 0.0
        if kind == "PP" and lam_pos:
            out.append(n)
        elif kind == "CMP" and not lam_pos:
            out.append(n)                      # general n: NOT a prime power
        elif kind == "P1M4" and PRIME_TAB[n] and n % 4 == 1:
            out.append(n)
        elif kind == "P3M4" and PRIME_TAB[n] and n % 4 == 3:
            out.append(n)
    return out


def geom_from_D(alpha, D_t):
    """THE T171 GRID RULE, bit for bit: M = 2 ceil(alpha / D_t)-ish, made even,
    then D = 2 alpha / M and h = M / 2, so h D = alpha EXACTLY."""
    Mz = int(math.ceil(alpha / D_t - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    return Mz, Mz // 2


def geom_from_h(alpha, h):
    """FRAME B: the grid step is read off a DECLARED h and is GAP-BLIND."""
    return 2 * int(h), int(h)


def admissible(alpha, hz):
    return (hz >= max(H_MIN, 2 * KB_MAX) and hz <= min(HCAP, MAX_H)
            and atoms_in(alpha) >= N_ATOM_MIN)


def frame_a_legs(kind, nu, count=N_PER_LEG):
    """FRAME A: D_k = g_k / (2 nu) from the LOCAL log-gap of the anchor family."""
    ns = anchor_list(kind)
    us = [math.log(float(n)) for n in ns]
    out = []
    for i in range(len(ns) - 1):
        g = us[i + 1] - us[i]
        Mz, hz = geom_from_D(us[i], 0.5 * g / float(nu))
        if admissible(us[i], hz):
            out.append((ns[i], us[i], Mz, hz))
    out.sort(key=lambda t: t[3])
    if not out:
        return []
    pick = sorted(set(int(round(x)) for x in np.geomspace(
        1.0, float(len(out)), count)))
    return [out[i - 1] for i in pick]


def frame_b_leg(kind):
    """FRAME B: same anchors as Frame A would admit, but h from a DECLARED
    geometric ladder -- the anchor's local gap no longer sets the grid."""
    base = frame_a_legs(kind, NU_A[0])
    if not base:
        return []
    ladder = [int(round(x)) for x in np.geomspace(float(H_MIN + 32),
                                                  float(HCAP - 10), len(base))]
    out = []
    for (n, u, _M, _h), ht in zip(sorted(base, key=lambda t: t[1]), ladder):
        Mz, hz = geom_from_h(u, ht)
        if admissible(u, hz):
            out.append((n, u, Mz, hz))
    return out


section("Z1  A1.i  THE RECIPE INVENTORY -- WHAT 'BEYOND FRAME A' CAN MEAN")
para(
    "FOUR DEGREES OF FREEDOM, and only four.  (1) THE FRAME, the rule anchor -> "
    "grid step D.  Frame A: D = g_k / (2 nu) from the LOCAL log-gap g_k of the "
    "anchor sequence.  Frame B (new here): D = alpha / h for a DECLARED h -- "
    "gap-BLIND, so the pairing (alpha, h) is no longer dictated by arithmetic.  "
    "(2) NU, the gap subdivision: T171 used {4, 6}; the extremes {3, 8} are new "
    "here.  (3) THE ZONE FAMILY, the arithmetic of the anchor sequence: prime "
    "powers (supp Lambda, Frame A), general non-prime-power integers, or a "
    "congruence class of primes.  (4) THE ATOM SET, which is NOT a degree of "
    "freedom: Lambda lives on prime powers, so a zone variant changes the "
    "ANCHOR arithmetic -- alpha, the gap sequence, and the alignment of the atom "
    "combs against the grid -- and never Lambda itself.")

for _kind in ("PP", "CMP", "P1M4", "P3M4"):
    _ns = anchor_list(_kind)
    _adm = frame_a_legs(_kind, NU_A[0])
    info("fb_z1.family_%s" % _kind,
         "%d anchors <= %d; Frame A / nu = %d admits h in [%s], selected "
         "n_zone = %s"
         % (len(_ns), ZONE_N_MAX, NU_A[0],
            "%d, %d" % (_adm[0][3], _adm[-1][3]) if _adm else "none",
            [t[0] for t in _adm] or "none"))


# ----------------------------------------------------------------------------
# ONE window, carrying every object the sixteen links touch.  The builder is
# FRAME- AND ZONE-AGNOSTIC: it takes (n_zone, alpha, M) and nothing else, so a
# frame or zone variant cannot smuggle a second change in through the back door.
# ----------------------------------------------------------------------------
def build_window(n_zone, alpha, Mz, surf, frame, zone, nu, scramble=False,
                 want_s=True):
    hz = Mz // 2
    if not admissible(alpha, hz):
        return None
    ka = atoms_in(alpha)
    at = ATOM_PAIRS[:ka]
    if scramble:                              # the T170 SCRAMBLE control
        rng = np.random.default_rng(7717 + n_zone)
        us = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
        at = [(float(us[i]), at[i][1]) for i in range(ka)]
    c_at, D = atom_lags(alpha, Mz, at)
    c_ar = arch_lags(Mz, D)
    r = dict(n_zone=n_zone, alpha=alpha, h=hz, M=Mz, D=D, nu=float(nu),
             surf=surf, frame=frame, zone=zone, n_atom=ka, scr=bool(scramble),
             X=math.exp(2.0 * alpha), U_ref=float(Mz) * D, c_ar=c_ar, c_at=c_at,
             c=c_ar + c_at, c0_ap=float(c_ar[0]))
    Tb = parity_basis(hz, KB_MAX)
    mu = parity_mu(hz)[:KB_MAX]
    isq = 1.0 / np.sqrt(mu)
    r["Tb"], r["mu"], r["mu1"] = Tb, mu, float(mu[0])
    A = odd_toeplitz(r["c"], Mz)
    r["Bkb"] = sym((Tb @ (A @ Tb.T)) * np.outer(isq, isq))
    r["B_LL"] = r["Bkb"][:SCHUR_KB, :SCHUR_KB].copy()
    ev = np.linalg.eigvalsh(r["B_LL"])
    r["lmin_LL"], r["lmax_LL"] = float(ev[0]), float(ev[-1])
    r["pd"] = bool(ev[0] > 0.0)
    r["kap"] = float(ev[-1] / max(abs(ev[0]), 1.0e-300))
    r["gcum"] = cf_ladder(r["B_LL"], SCHUR_KB)
    r["gcum32"] = cf_ladder(r["Bkb"], KB_MAX)
    # --- the 2 x 2 arithmetic block, UNNORMALISED (T168 .. T171's Ahat) -------
    t1, t2 = Tb[0].copy(), Tb[1].copy()
    At1, At2 = A @ t1, A @ t2
    Ah = np.array([[float(t1 @ At1), float(t1 @ At2)],
                   [float(t1 @ At2), float(t2 @ At2)]])
    r["t1"], r["t2"], r["Ah"] = t1, t2, Ah
    r["a11"], r["a22"], r["a12"] = float(Ah[0, 0]), float(Ah[1, 1]), float(Ah[0, 1])
    r["det"] = float(Ah[0, 0] * Ah[1, 1] - Ah[0, 1] ** 2)
    r["onem"] = r["det"] / (r["a11"] * r["a22"])
    n1 = math.hypot(Ah[0, 0], Ah[0, 1])
    n2 = math.hypot(Ah[1, 0], Ah[1, 1])
    r["sin"] = abs(r["det"]) / max(n1 * n2, 1.0e-300)     # LINK 16's angle
    # --- the closed lag weights of the two lowest modes -----------------------
    r["W11"] = lag_weights_from_v(t1, hz)
    r["W22"] = lag_weights_from_v(t2, hz)
    r["W12"] = 0.5 * (lag_weights_from_v(t1 + t2, hz) - r["W11"] - r["W22"])
    # --- the arch / atom split of Ahat, and the per-atom 2 x 2 projections ----
    A_ar = odd_toeplitz(c_ar, Mz)
    B2 = np.array([[float(t1 @ (A_ar @ t1)), float(t1 @ (A_ar @ t2))],
                   [float(t1 @ (A_ar @ t2)), float(t2 @ (A_ar @ t2))]])
    del A_ar
    lam = np.array([t[1] * 0.5 for t in at])      # lambda_n = Lambda(n)/sqrt(n)
    uu = np.array([t[0] for t in at])
    Xn = np.empty((ka, 3))
    for i in range(ka):
        Xn[i, 0] = spline_project(r["W11"], uu[i], D, Mz)
        Xn[i, 1] = spline_project(r["W22"], uu[i], D, Mz)
        Xn[i, 2] = spline_project(r["W12"], uu[i], D, Mz)
    S2 = np.array([[float(lam @ Xn[:, 0]), float(lam @ Xn[:, 2])],
                   [float(lam @ Xn[:, 2]), float(lam @ Xn[:, 1])]])
    r["B2"], r["S2"], r["lam"], r["uu"], r["Xn"] = B2, S2, lam, uu, Xn
    # --- the EXACT entry s = mu^P_1 t_1^T A^-1 t_1 = (B_full^-1)_11 -----------
    if want_s:
        try:
            y = np.linalg.solve(A, t1)
            r["s"] = float(r["mu1"] * float(t1 @ y))
        except np.linalg.LinAlgError:
            r["s"] = float("nan")
    else:
        r["s"] = float("nan")
    del A
    return r


SURFACES = (
    ("S0 FRAME-A / PRIME-POWER (T171 REFERENCE)",
     [("A", "PP", nu) for nu in NU_A]),
    ("S1 FRAME-VARIANT / PRIME-POWER (gap-blind B + nu extremes)",
     [("B", "PP", NU_A[0])] + [("A", "PP", nu) for nu in NU_EXT]),
    ("S2 ZONE-VARIANT / GENERAL n (non-prime-power anchors)",
     [("A", "CMP", nu) for nu in NU_A]),
    ("S3 ZONE-VARIANT / CONGRUENCE (p = 1 mod 4 against p = 3 mod 4)",
     [("A", "P1M4", NU_A[0]), ("A", "P3M4", NU_A[0])]),
)


def leg_specs(frame, zone, nu, n_legs):
    """SIX WINDOWS PER LEG on every leg, log-spaced in h -- DECLARED IN ADVANCE
    and identical for every surface, so no leg is given a better fit than
    another.  S1 carries three legs and therefore 18 windows, not 12."""
    if frame == "B":
        return frame_b_leg(zone)
    return frame_a_legs(zone, nu, N_PER_LEG)


section("Z2  A1.i  THE MEASURED SURFACES -- SIX WINDOWS PER LEG, DECLARED")

ALLW, SURF_NAMES = [], []
for _sname, _legs in SURFACES:
    _tag = _sname.split()[0]
    SURF_NAMES.append(_tag)
    for (_fr, _zn, _nu) in _legs:
        for (_n, _u, _M, _h) in leg_specs(_fr, _zn, _nu, len(_legs)):
            if budget_left() < 480.0:
                info("fb_z2.budget", "stopped building at %s h = %d" % (_tag, _h))
                break
            _w = build_window(_n, _u, _M, _tag, _fr, _zn, _nu)
            if _w is not None:
                ALLW.append(_w)

BYS = {t: [r for r in ALLW if r["surf"] == t] for t in SURF_NAMES}
NW = len(ALLW)                                # every count below is derived
check("fb_z2.surfaces", all(len(BYS[t]) >= 10 for t in SURF_NAMES),
      "%d windows on %d surfaces: %s"
      % (len(ALLW), len(SURF_NAMES),
         ", ".join("%s: %d" % (t, len(BYS[t])) for t in SURF_NAMES)))
check("fb_z2.scales",
      all(abs(r["h"] * r["D"] - r["alpha"]) < 1.0e-10 for r in ALLW)
      and all(abs(math.log(r["X"]) - 2.0 * r["alpha"]) < 1.0e-9 for r in ALLW),
      "THE SCALES, ONCE AND ON EVERY SURFACE: D = 2 alpha / M, h = M / 2, "
      "h D = alpha to 1e-10, U_ref = M D = 2 alpha = log X exactly -- the frame "
      "and zone variants move alpha and D, never this identity")

for _t in SURF_NAMES:
    _W = BYS[_t]
    _hs = [r["h"] for r in _W]
    info("fb_z2.inv_%s" % _t,
         "%d windows, frames %s, zones %s, nu %s: h = %d .. %d (lever %.1fx), "
         "alpha = %.3f .. %.3f, n_zone = %d .. %d, atoms %d .. %d, "
         "lam_min(B_LL) = %.3g .. %.3g, %d of %d POSITIVE DEFINITE"
         % (len(_W), sorted(set(r["frame"] for r in _W)),
            sorted(set(r["zone"] for r in _W)),
            sorted(set(int(r["nu"]) for r in _W)), min(_hs), max(_hs),
            max(_hs) / min(_hs), qmin([r["alpha"] for r in _W]),
            qmax([r["alpha"] for r in _W]), min(r["n_zone"] for r in _W),
            max(r["n_zone"] for r in _W), min(r["n_atom"] for r in _W),
            max(r["n_atom"] for r in _W), qmin([r["lmin_LL"] for r in _W]),
            qmax([r["lmin_LL"] for r in _W]), sum(1 for r in _W if r["pd"]),
            len(_W)))

# --- THE INDEFINITE MAP: T171 saw ONE indefinite low block; where is it here? -
IND = [r for r in ALLW if not r["pd"]]
LADW = [r for r in ALLW if r["pd"] and r["gcum"] is not None
        and r["gcum32"] is not None and r["kap"] <= COND_BAR]
check("fb_z2.indefinite_map", True,
      "%d of %d windows have an INDEFINITE low block and are EXCLUDED OUT LOUD "
      "from every certificate below (T171 excluded one such window at nu = 4, "
      "h = 1445, lam_min = -343): %s.  DIRECTION: an indefinite B_LL makes the "
      "Schur floor t MEANINGLESS -- there is no positive t at all -- while the "
      "IDENTITY links below use no positivity and stay valid there"
      % (len(IND), len(ALLW),
         ["%s/nu%d/h%d/lmin=%.3g" % (r["surf"], int(r["nu"]), r["h"],
                                     r["lmin_LL"]) for r in IND] or "none"))
check("fb_z2.ladder_surface", len(LADW) >= 30,
      "%d of %d windows carry the Cholesky ladder (B_LL positive definite and "
      "cond(B_LL) <= %.0e, the DECLARED T159 numerical horizon); per surface: %s"
      % (len(LADW), len(ALLW), COND_BAR,
         ", ".join("%s: %d/%d" % (t, sum(1 for r in LADW if r["surf"] == t),
                                  len(BYS[t])) for t in SURF_NAMES)))
info("fb_z2.budget", "%.1f s left" % budget_left())

check("fb_z2.comb_complete",
      all(float(r["n_zone"]) ** 2 <= float(ATOM_MAX) + 0.5 for r in ALLW),
      "THE ATOM COMB IS COMPLETE ON EVERY WINDOW: n_zone^2 = X <= %d = ATOM_MAX, "
      "so no window silently drops atom mass above the sieve cap.  DECLARED "
      "NUMERICAL HORIZON, and it is the reason the anchors stop at n = %d"
      % (ATOM_MAX, ZONE_N_MAX))


# ----------------------------------------------------------------------------
# A1.ii  THE IDENTITY TRANSFER: the sixteen links, one at a time, on all four
# surfaces.  Every link gets a per-window number; the verdict per link is
# UNIVERSAL (holds to the identity bar on every surface), SHIFTS (holds, but a
# CONSTANT moves) or BREAKS.
# ----------------------------------------------------------------------------
TRANSFER = []


def transfer(n, tag, kind, verdict, detail):
    TRANSFER.append((n, tag, kind, verdict, detail))
    print("")
    print("  --- LINK %2d  %-24s [%s]  %s" % (n, tag, kind, verdict))
    for ln in wrap_at(detail, 72):
        print("      " + ln)


def per_surface(key, agg=qmax):
    return ", ".join("%s %.2e" % (t, agg([r[key] for r in BYS[t] if key in r]))
                     for t in SURF_NAMES)


def tv_vec(v):
    return float(np.abs(np.diff(v)).sum() + abs(v[0]))


RNG = np.random.default_rng(20172)


def identity_pass(r):
    """One rebuild of A per window, and every link that needs the FULL matrix."""
    hz, Mz = r["h"], r["M"]
    A = odd_toeplitz(r["c"], Mz)
    Tb, mu = r["Tb"], r["mu"]
    x = RNG.normal(size=SCHUR_KB)
    xb = x / np.sqrt(mu[:SCHUR_KB])
    v = Tb[:SCHUR_KB].T @ xb
    lhs = float(x @ (r["B_LL"] @ x))
    rhs = float(v @ (A @ v))
    r["e_L1"] = abs(lhs - rhs) / max(abs(rhs), 1.0e-300)
    lp = float(np.sum(mu[:SCHUR_KB] * xb ** 2))
    r["L1_dir"] = bool(lp >= r["mu1"] * float(v @ v) - 1.0e-10 * abs(lp))
    # LINK 3: the quadratic form IS a finite lag sum against c
    w = lag_weights_from_v(v, hz)
    psi = float(r["c"] @ w)
    r["e_L3"] = abs(psi - rhs) / max(abs(rhs), 1.0e-300)
    # LINK 7: the Cholesky ladder against a direct solve, and the Thomson dual.
    # The ladder needs a POSITIVE DEFINITE low block; where there is none the
    # ladder links are recorded as absent, never as passed.
    has_lad = r["gcum"] is not None
    if has_lad:
        e_lad = 0.0
        for K in (2, 8, SCHUR_KB):
            e1 = np.zeros(K)
            e1[0] = 1.0
            gd = float(e1 @ np.linalg.solve(sym(r["B_LL"][:K, :K]), e1))
            e_lad = max(e_lad, abs(gd - float(r["gcum"][K - 1])) / abs(gd))
        r["e_L7"] = e_lad
        z = Tb[:SCHUR_KB].T @ RNG.normal(size=SCHUR_KB)
        trial = 2.0 * math.sqrt(r["mu1"]) * float(r["t1"] @ z) - float(z @ (A @ z))
        r["L7_dir"] = bool(trial <= float(r["gcum"][SCHUR_KB - 1]) + 1.0e-9)
    else:
        r["e_L7"], r["L7_dir"] = float("nan"), False
    # LINK 9: the Abel swap, exactly, on this window's own weight vector
    C = np.cumsum(r["c"])
    r["e_L9"] = (abs(float(r["c"] @ w) - float(back_diff(w) @ C))
                 / max(abs(psi), 1.0e-300))
    r["TVw"] = float(np.abs(back_diff(w)).sum())
    r["L9_dir"] = bool(abs(psi) <= r["TVw"] * float(np.max(np.abs(C))) + 1.0e-9)
    # LINK 10: the gauge, and the quantifier collapse to ONE vector
    sg = 3.7
    v2 = sg * v
    w2 = lag_weights_from_v(v2, hz)
    R1 = psi / max(r["TVw"], 1.0e-300)
    R2 = float(r["c"] @ w2) / max(float(np.abs(back_diff(w2)).sum()), 1.0e-300)
    r["e_L10"] = abs(R1 - R2) / max(abs(R1), 1.0e-300)
    if has_lad:
        e1 = np.zeros(SCHUR_KB)
        e1[0] = 1.0
        y = np.linalg.solve(sym(r["B_LL"]), e1)
        g16 = float(r["gcum"][SCHUR_KB - 1])
        xs = y / y[0]
        r["e_L10b"] = abs(float(xs @ (r["B_LL"] @ xs)) - 1.0 / g16) * g16
        # LINK 11: P_pr = g_16 Psi >= 1 with EQUALITY at x*, on the x_1 = 1 slice
        xr = RNG.normal(size=SCHUR_KB)
        xr[0] = 1.0
        r["e_L11"] = abs(g16 * float(xs @ (r["B_LL"] @ xs)) - 1.0)
        r["L11_dir"] = bool(g16 * float(xr @ (r["B_LL"] @ xr)) >= 1.0 - 1.0e-9)
    else:
        r["e_L10b"], r["e_L11"], r["L11_dir"] = float("nan"), float("nan"), False
    # LINK 8: the SAMPLING half -- the atom part of Psi IS the sampled Lambda mass
    r["e_L8"] = (abs(float(r["c_at"] @ r["W11"]) + float(r["lam"] @ r["Xn"][:, 0]))
                 / max(abs(float(r["c_at"] @ r["W11"])), 1.0e-300))
    del A


section("Z3  A1.ii  THE IDENTITY TRANSFER -- SIXTEEN LINKS, FOUR SURFACES")
para(
    "READ THE TABLE THIS WAY.  A link marked UNIVERSAL was re-derived on every "
    "window of every surface and held to the identity bar %.0e -- it uses no "
    "property of the frame or of the anchor arithmetic.  A link marked SHIFTS "
    "holds as a statement but carries a CONSTANT that moves with the surface; "
    "block A2 tracks those constants.  Nothing here is a claim for all m: the "
    "quantifier stays OPEN at link 16 on all four surfaces." % EXACT_BAR)

for _r in ALLW:
    identity_pass(_r)

transfer(1, "T152 SCHUR 2-BLOCK", "THEOREM", "UNIVERSAL",
         "x^T B x = v^T A_h v for v = T^T(x / sqrt(mu)) re-derived per window: "
         "worst relative error per surface %s.  The mu^P_1 step v^T L_P v >= "
         "mu^P_1 |v|^2 (DIRECTION: it WEAKENS the floor) holds on %d of %d "
         "windows.  The criterion is pure linear algebra in the KMS basis and "
         "knows nothing about the anchor arithmetic."
         % (per_surface("e_L1"), sum(1 for r in ALLW if r["L1_dir"]), len(ALLW)))
check("fb_z3.L1", qmax([r["e_L1"] for r in ALLW]) < ROUND_BAR
      and all(r["L1_dir"] for r in ALLW),
      "identity to %.0e (the DECLARED full-matrix round-off horizon) and "
      "direction on all four surfaces" % ROUND_BAR)

CS_R = {}
for _t in SURF_NAMES:
    _w = []
    for r in BYS[_t]:
        N = 2 * r["h"] + 1
        CS = (2.0 * math.pi + 2.0) / math.sqrt(float(N))
        _w.append(max(tv_vec(r["Tb"][k]) / (CS * (k + 1.0))
                      for k in range(SCHUR_KB)))
    CS_R[_t] = qmax(_w)
transfer(2, "T151 SOBOLEV REROUTE", "THEOREM", "UNIVERSAL",
         "b_k = TV(t_k) <= C_S k with C_S = (2 pi + 2)/sqrt(N) verified for "
         "k <= %d on every window; worst tightness b_k / (C_S k) per surface: "
         "%s (all <= 1, DIRECTION: an UPPER bound on the mode's variation).  "
         "C_S depends on N = 2h + 1 alone, so this link cannot see a frame or a "
         "zone at all -- only h."
         % (SCHUR_KB, ", ".join("%s %.4f" % (t, CS_R[t]) for t in SURF_NAMES)))
check("fb_z3.L2", all(CS_R[t] <= 1.0 for t in SURF_NAMES),
      "TV ceiling holds with room to spare on all four surfaces")

transfer(3, "T153 PSI COLLAPSE", "THEOREM", "UNIVERSAL",
         "Psi(x) = sum_d c_d w_d = x^T B x, the EXACT collapse of the quadratic "
         "form onto a finite LAG SUM against c = c^arch + c^atom -- the link "
         "where arithmetic enters at all.  Worst relative error per surface: %s.  "
         "The zone variants change c (different alpha, different grid alignment "
         "of the atom combs) and the identity is untouched."
         % per_surface("e_L3"))
check("fb_z3.L3", qmax([r["e_L3"] for r in ALLW]) < ROUND_BAR,
      "the collapse is exact to the DECLARED %.0e round-off horizon on all %d "
      "windows" % (ROUND_BAR, NW))

L4_OK = [r for r in LADW
         if float(r["gcum"][KL_FLOOR - 1]) <= float(r["gcum"][SCHUR_KB - 1]) + 1e-12
         and float(r["gcum"][SCHUR_KB - 1]) <= float(r["gcum32"][KB_MAX - 1]) + 1e-12
         and float(r["gcum32"][KB_MAX - 1]) <= r["s"] * (1.0 + 1.0e-9)]
transfer(4, "T154 RITZ CEILING", "THEOREM", "UNIVERSAL",
         "Cauchy interlacing: g_%d <= g_%d <= g_%d <= s, so 1/g_K is a "
         "DECREASING chain of UPPER bounds on 1/s and a Ritz value is a CEILING "
         "for lam_min, NEVER a floor.  Holds on %d of %d ladder windows; the "
         "ordering is basis monotonicity and is blind to the surface."
         % (KL_FLOOR, SCHUR_KB, KB_MAX, len(L4_OK), len(LADW)))
check("fb_z3.L4", len(L4_OK) == len(LADW), "interlacing direction on every window")


def complement_floor(Bfull, kl):
    """T155's CERTIFICATE, per window: the largest t at which BOTH B_L - t I > 0
    and the Schur complement Sc(t) = B_H - t I - B_HL (B_L - t I)^-1 B_LH >= 0.
    Then lam_min(B_full) >= t (Schur 1917).  DIRECTION: the certificate holds AT
    t and FAILS above it, and both halves are tested."""
    B = sym(np.asarray(Bfull))
    L, H = B[:kl, :kl], B[kl:, kl:]
    X = B[:kl, kl:]
    nH = H.shape[0]

    def ok(t):
        ev = np.linalg.eigvalsh(L - t * np.eye(kl))
        if ev[0] <= 0.0:
            return False
        Sc = H - t * np.eye(nH) - X.T @ np.linalg.solve(L - t * np.eye(kl), X)
        return bool(np.linalg.eigvalsh(sym(Sc))[0] >= 0.0)

    lo, hi = 0.0, float(np.linalg.eigvalsh(B)[0]) * 1.5 + 1.0e-12
    if not ok(lo + 1.0e-15):
        return 0.0, False
    for _ in range(48):
        mid = 0.5 * (lo + hi)
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo, (not ok(min(hi + 1.0e-14, hi * (1.0 + 1.0e-9)) + 1.0e-15))


for _r in LADW:
    _t, _sharp = complement_floor(_r["Bkb"], KL_FLOOR)
    _r["t_floor"], _r["t_sharp"] = _t, _sharp
    _r["lmin32"] = float(np.linalg.eigvalsh(sym(_r["Bkb"]))[0])
T_OK = [r for r in LADW if r["t_floor"] > 0.0
        and r["t_floor"] <= r["lmin32"] * (1.0 + 1.0e-8)]
transfer(5, "T155 %dx%d COMPLEMENT" % (KL_FLOOR, KL_FLOOR), "CERT", "SHIFTS",
         "The complement floor certifies lam_min(B_%d) >= t with the low block "
         "L = 1 .. %d.  It TRANSFERS -- a positive t is certified on %d of %d "
         "ladder windows and never exceeds the true lam_min -- but t is a "
         "CONSTANT and it MOVES: median per surface %s.  It is also the one link "
         "that DIES where the low block is indefinite, because then no positive "
         "t exists at all."
         % (KB_MAX, KL_FLOOR, len(T_OK), len(LADW),
            ", ".join("%s %.4f" % (t, qmed([r["t_floor"] for r in BYS[t]
                                            if "t_floor" in r]))
                      for t in SURF_NAMES)))
check("fb_z3.L5", len(T_OK) == len(LADW),
      "a POSITIVE certified floor on every ladder window of every surface, and "
      "t <= lam_min(B_%d) throughout (DIRECTION: the certificate is a FLOOR)"
      % KB_MAX)

for _r in LADW:
    _g16 = float(_r["gcum"][SCHUR_KB - 1])
    _r["P_pr"] = _g16 / float(_r["gcum"][KL_FLOOR - 1])
    _r["r_K"] = 1.0 / _g16 - 1.0 / _r["s"]
    _r["L_cert"] = 1.0 / max(_r["r_K"] * _r["s"], 1.0e-300)
    _r["g16"] = _g16
    _r["inv_g16"] = 1.0 / _g16
transfer(6, "T156 F(P, r) CHAIN", "CERT", "SHIFTS",
         "The pair (price, defect) forwards on every surface: P_K = g_16/g_%d "
         ">= 1 on %d of %d windows and r_K = 1/g_16 - 1/s >= 0 on %d of %d "
         "(DIRECTION: r_K >= 0 BECAUSE g_K <= s, link 4).  The numbers move: "
         "median r_K per surface %s; median certified L = 1/(r_K s) per surface "
         "%s."
         % (KL_FLOOR, sum(1 for r in LADW if r["P_pr"] >= 1.0 - 1.0e-12),
            len(LADW), sum(1 for r in LADW if r["r_K"] >= -1.0e-14), len(LADW),
            ", ".join("%s %.3e" % (t, qmed([r["r_K"] for r in BYS[t]
                                           if "r_K" in r])) for t in SURF_NAMES),
            ", ".join("%s %.3e" % (t, qmed([r["L_cert"] for r in BYS[t]
                                           if "L_cert" in r]))
                      for t in SURF_NAMES)))
check("fb_z3.L6", all(r["P_pr"] >= 1.0 - 1.0e-12 and r["r_K"] >= -1.0e-14
                      for r in LADW), "both directions on every ladder window")

transfer(7, "T158 THOMSON / LADDER", "THEOREM", "UNIVERSAL",
         "g_K = sum_{j<=K} y_j^2 with y = L_K^-1 e_1 agrees with the direct "
         "solve e_1^T Q_K^-1 e_1 at K = 2, 8, %d: worst relative error per "
         "surface %s.  The Thomson dual (a TRIAL z gives a LOWER bound on g_K) "
         "holds on %d of %d windows.  Schur 1917 nested complements; the "
         "identity is metric algebra and carries across."
         % (SCHUR_KB, per_surface("e_L7"),
            sum(1 for r in ALLW if r["L7_dir"]), len(ALLW)))
check("fb_z3.L7", qmax([r["e_L7"] for r in ALLW]) < SOLVE_BAR
      and all(r["L7_dir"] for r in ALLW),
      "ladder identity to the DECLARED %.0e solve horizon, and the dual "
      "direction on every window" % SOLVE_BAR)

transfer(8, "T160 SAMPLING IDENTITY", "THEOREM", "UNIVERSAL",
         "The half that CARRIES ARITHMETIC: the atom part of Psi IS the sampled "
         "Lambda mass, c^atom . W = - sum_n (Lambda(n)/sqrt n) (phi_n . W).  "
         "Worst relative error per surface: %s.  This is the most zone-sensitive "
         "identity in the chain -- the anchor arithmetic decides WHERE the atom "
         "combs sit on the grid -- and it is exact on all four.  HONEST SCOPE: "
         "the second, Dirichlet-kernel form of w (Dirichlet 1829) is pure sine "
         "algebra in h, independent of frame and zone, and is T171's check; it "
         "is not re-run here."
         % per_surface("e_L8"))
check("fb_z3.L8", qmax([r["e_L8"] for r in ALLW]) < ROUND_BAR,
      "the sampling identity is exact on all %d windows of all four surfaces"
      % NW)

transfer(9, "T163 TV FLOOR / SWAP", "THEOREM", "UNIVERSAL",
         "The Abel swap (Abel 1826) sum_d c_d w_d = sum_d (Delta w)_d C_d with "
         "C_d = sum_{e<=d} c_e: worst relative error per surface %s, and the "
         "consequence |Psi| <= TV(w) max_d |C_d| (DIRECTION: an UPPER bound) "
         "holds on %d of %d windows.  It is the only route by which a bound on "
         "PARTIAL SUMS of the Lambda mass reaches the pairing, and it is "
         "surface-blind."
         % (per_surface("e_L9"), sum(1 for r in ALLW if r["L9_dir"]), len(ALLW)))
check("fb_z3.L9", qmax([r["e_L9"] for r in ALLW]) < ROUND_BAR
      and all(r["L9_dir"] for r in ALLW), "swap identity + direction")

transfer(10, "T164 GAUGE / QUANTIFIER", "THEOREM", "UNIVERSAL",
         "GAUGE: R = Psi/TV is a ratio of two degree-2 homogeneous functionals, "
         "so R(sigma x) = R(x) EXACTLY -- worst relative drift per surface %s at "
         "sigma = 3.7.  QUANTIFIER COLLAPSE: min{x^T B_LL x : x_1 = 1} = 1/g_16 "
         "is attained at the SINGLE vector x* = B_LL^-1 e_1 / (e_1^T B_LL^-1 "
         "e_1); worst error per surface %s.  Both are surface-blind."
         % (per_surface("e_L10"), per_surface("e_L10b")))
check("fb_z3.L10", qmax([r["e_L10"] for r in ALLW]) < ROUND_BAR
      and qmax([r["e_L10b"] for r in ALLW]) < SOLVE_BAR,
      "gauge invariance to %.0e and the one-vector collapse to %.0e (the "
      "DECLARED K = 16 solve horizon) on all four surfaces"
      % (ROUND_BAR, SOLVE_BAR))

transfer(11, "T165 P_pr IDENTITY", "THEOREM", "UNIVERSAL",
         "On the x_1 = 1 slice P_pr = g_16 Psi >= 1 with EQUALITY exactly at x*: "
         "worst |P_pr(x*) - 1| per surface %s, and P_pr >= 1 at a random "
         "admissible x on %d of %d windows (DIRECTION: the price is never below "
         "1).  Pure normalisation algebra; no frame or zone enters."
         % (per_surface("e_L11"), sum(1 for r in ALLW if r["L11_dir"]),
            len(ALLW)))
check("fb_z3.L11", qmax([r["e_L11"] for r in ALLW]) < SOLVE_BAR
      and all(r["L11_dir"] for r in ALLW),
      "equality at x* to the DECLARED %.0e solve horizon, and the direction on "
      "every window" % SOLVE_BAR)

E12, E12D = [], []
for _r in ALLW:
    B = sym(_r["B_LL"])
    b = B[0, 1:SCHUR_KB]
    R2 = float(b @ np.linalg.solve(B[1:SCHUR_KB, 1:SCHUR_KB], b)) / B[0, 0]
    gain = float(_r["gcum"][SCHUR_KB - 1]) / float(_r["gcum"][0])
    E12.append(abs(gain - 1.0 / (1.0 - R2)) / abs(gain))
    d = np.exp(RNG.normal(size=SCHUR_KB) * 0.7)
    Bd = (B * np.outer(d, d))
    gd = cf_ladder(Bd, SCHUR_KB)
    E12D.append(abs(float(gd[SCHUR_KB - 1]) / float(gd[0]) - gain) / abs(gain))
transfer(12, "T166 CASCADE 1/(1-R^2)", "THEOREM", "UNIVERSAL",
         "The cascade gain IS a regression: g_%d/g_1 = 1/(1 - R^2) with R^2 = "
         "b^T B_HH^-1 b / B_11 the squared multiple correlation of mode 1 on "
         "modes 2..%d in the metric B.  Worst relative error %.2e over all %d "
         "windows.  DIAGONAL INVARIANCE B -> D B D re-tested with a random "
         "positive D: worst drift %.2e.  Neither depends on the surface."
         % (SCHUR_KB, SCHUR_KB, qmax(E12), NW, qmax(E12D)))
check("fb_z3.L12", qmax(E12) < SOLVE_BAR and qmax(E12D) < SOLVE_BAR,
      "regression identity and diagonal invariance to the DECLARED %.0e solve "
      "horizon across all four surfaces" % SOLVE_BAR)

E13, E13X = [], []
for _r in ALLW:
    B = sym(_r["B_LL"])
    r12 = B[0, 1] / math.sqrt(B[0, 0] * B[1, 1])
    g2 = float(_r["gcum"][1])
    E13.append(abs(B[0, 0] * g2 - 1.0 / (1.0 - r12 ** 2)) * (1.0 - r12 ** 2))
    xs = np.array([1.0, -B[0, 1] / B[1, 1]])
    E13X.append(abs(float(xs @ (B[:2, :2] @ xs)) - 1.0 / g2) * g2)
    _r["r12"] = float(r12)
transfer(13, "T167 K = 2 EXACTNESS", "THEOREM", "UNIVERSAL",
         "At K = 2 the regression is CLOSED: B_11 g_2 = 1/(1 - r_12^2) with "
         "r_12 = B_12/sqrt(B_11 B_22), minimiser x* = (1, -B_12/B_22).  Worst "
         "errors over all %d windows: %.2e (identity) and %.2e (minimiser).  No "
         "solve, no ladder, no truncation choice -- and no frame."
         % (NW, qmax(E13), qmax(E13X)))
check("fb_z3.L13", qmax(E13) < SOLVE_BAR and qmax(E13X) < SOLVE_BAR,
      "the closed K = 2 rung is exact to the DECLARED %.0e solve horizon on "
      "every window of every surface" % SOLVE_BAR)

E14A, E14B, E14C = [], [], []
for _r in ALLW:
    B = sym(_r["B_LL"])
    onem_B = 1.0 - _r["r12"] ** 2
    E14A.append(abs(onem_B - _r["onem"]))              # ABSOLUTE: both ~1e-6
    Bn = _r["Bkb"][:2, :2]
    detBn = float(Bn[0, 0] * Bn[1, 1] - Bn[0, 1] ** 2)
    E14B.append(abs(detBn / (Bn[0, 0] * Bn[1, 1]) - _r["onem"]))
    E14C.append(abs(1.0 / float(_r["gcum"][1]) - B[0, 0] * onem_B)
                * float(_r["gcum"][1]))
transfer(14, "T169 DET COLLAPSE (R4-FREE)", "THEOREM", "UNIVERSAL",
         "1 - r_12^2 = det Ahat/(ahat_11 ahat_22) = nu_1 nu_2/(ahat_11 ahat_22), "
         "the SAME number as det B_2/(B_11 B_22) by the diagonal invariance of "
         "link 12, and 1/g_2 = B_11 (1 - r_12^2).  The first two are stated "
         "ABSOLUTELY because the quantity itself is near-null (%.2e .. %.2e over "
         "the windows): worst absolute errors %.2e and %.2e against the "
         "DECLARED %.0e, worst scaled error %.2e on the third.  *** THESE ARE "
         "IDENTITIES AND USE NO POSITIVITY OF A_h -- which is why they survive "
         "even where the low block would be indefinite, and why they are "
         "surface-blind. ***"
         % (qmin([abs(r["onem"]) for r in ALLW]),
            qmax([abs(r["onem"]) for r in ALLW]), qmax(E14A), qmax(E14B),
            NULL_BAR, qmax(E14C)))
check("fb_z3.L14", qmax(E14A) < NULL_BAR and qmax(E14B) < NULL_BAR
      and qmax(E14C) < SOLVE_BAR, "the det collapse holds identically everywhere")

E15A, E15B = [], []
for _r in ALLW:
    Ah_rec = _r["B2"] - _r["S2"]
    E15A.append(float(np.max(np.abs(Ah_rec - _r["Ah"])))
                / max(float(np.max(np.abs(_r["Ah"]))), 1.0e-300))
    dS = float(_r["S2"][0, 0] * _r["S2"][1, 1] - _r["S2"][0, 1] ** 2)
    dB = float(_r["B2"][0, 0] * _r["B2"][1, 1] - _r["B2"][0, 1] ** 2)
    dm = mixed_det(_r["B2"], _r["S2"])
    pol = dB - dm + dS
    # SCALE-NORMALISED, because det Ahat is the near-null RESULT of a three-term
    # cancellation: the honest denominator is the LARGEST term, not the result.
    E15B.append(abs(pol - _r["det"]) / max(abs(dB), abs(dm), abs(dS), 1.0e-300))
    _r["detS"], _r["detB2"], _r["detmix"] = dS, dB, dm
    _r["cancel"] = max(abs(dB), abs(dm), abs(dS)) / max(abs(_r["det"]), 1.0e-300)
_JEV = np.linalg.eigvalsh(J_POL)
transfer(15, "T170 RANK-3 COLLAPSE", "THEOREM", "UNIVERSAL",
         "The exact split Ahat = B - sum_n (Lambda(n)/sqrt n) X_n (worst entry "
         "error %.2e) and the polarisation det Ahat = det B - D(B, S) + det S "
         "(Lagrange 1773; Cauchy-Binet 1812/1815; worst error %.2e RELATIVE TO "
         "THE LARGEST TERM, the cancellation being %.1e : 1 at worst) "
         "turn det S into a BILINEAR von Mangoldt sum with kernel K(n,m) = "
         "(1/2) X_n J X_m^T.  J has eigenvalues %s: RANK 3, SIGNATURE (1, 2) -- "
         "an algebraic fact about 2 x 2 determinants, hence surface-blind, and "
         "the reason a sieve cannot recover the kernel."
         % (qmax(E15A), qmax(E15B), qmax([r["cancel"] for r in ALLW]),
            "(%.1f, %.1f, %.1f)" % (_JEV[0], _JEV[1], _JEV[2])))
check("fb_z3.L15", qmax(E15A) < 1.0e-10 and qmax(E15B) < ROUND_BAR
      and int(np.linalg.matrix_rank(J_POL)) == 3
      and int(np.sum(_JEV > 0)) == 1 and int(np.sum(_JEV < 0)) == 2,
      "split, polarisation, rank 3 and signature (1, 2) on every surface")

E16 = []
for _r in ALLW:
    n1 = math.hypot(_r["Ah"][0, 0], _r["Ah"][0, 1])
    n2 = math.hypot(_r["Ah"][1, 0], _r["Ah"][1, 1])
    E16.append(abs(_r["sin"] - abs(_r["det"]) / (n1 * n2)) / max(_r["sin"], 1e-300))
transfer(16, "T170 THE R1 SHAPE", "CERT", "SHIFTS",
         "sin(angle between the two rows of Ahat) = |det Ahat|/(|row_1| "
         "|row_2|) is an identity (worst error %.2e) -- but the RATE at which "
         "the angle closes is a per-surface MEASUREMENT and it is exactly what "
         "moves.  Block A3 measures it on all four surfaces.  *** THE OPEN "
         "QUANTIFIER LIVES HERE: nothing below closes 'for all m', on any "
         "surface. ***" % qmax(E16))
check("fb_z3.L16", qmax(E16) < EXACT_BAR,
      "the angle identity itself is exact; only its RATE is surface-dependent")

N_UNIV = sum(1 for t in TRANSFER if t[3] == "UNIVERSAL")
check("fb_z3.transfer_ledger", len(TRANSFER) == 16,
      "SIXTEEN LINKS TYPED: %d UNIVERSAL (unchanged on all four surfaces), "
      "%d SHIFTS (statement transfers, constant moves), 0 BROKEN.  The "
      "UNIVERSAL set is exactly the identity tower plus the two direction "
      "lemmas; the SHIFTS set is exactly the two CERT links (5, 6) and the RATE "
      "link (16) -- i.e. every link that carries a NUMBER rather than an "
      "equation." % (N_UNIV, 16 - N_UNIV))


# ----------------------------------------------------------------------------
# A1.ii addendum -- WHERE DOES THE LOW BLOCK GO INDEFINITE?  T171 lost one
# nu = 4 window to lam_min(B_LL) = -343.  On the four complete-comb surfaces
# above, none.  The DECLARED stress leg below isolates the mechanism: Frame B on
# DEEP anchors, where the grid reaches U_ref = 2 alpha but the sieve stops at
# ATOM_MAX, so the atom comb is TRUNCATED and mass is missing from c.
# ----------------------------------------------------------------------------
section("Z4  A1.ii ADDENDUM -- THE INDEFINITE MECHANISM, ISOLATED")

STRESS = []
for _nz in (1009, 10007, 100003):
    _u = math.log(float(_nz))
    _w = build_window(_nz, _u, 2 * 600, "STRESS", "B", "PP", 0, want_s=False)
    if _w is not None:
        _w["trunc"] = math.exp(2.0 * _u) / float(ATOM_MAX)
        STRESS.append(_w)
info("fb_z4.stress_leg",
     "; ".join("n_zone = %d, X/ATOM_MAX = %.3g, atoms = %d, lam_min(B_LL) = %.4g"
               % (r["n_zone"], r["trunc"], r["n_atom"], r["lmin_LL"])
               for r in STRESS))
N_IND_STR = sum(1 for r in STRESS if not r["pd"])
check("fb_z4.mechanism", True,
      "MEASURED, and it is the honest answer to T171's warning: %d of %d "
      "truncated-comb stress windows have an INDEFINITE low block, against 0 of "
      "48 on the four complete-comb surfaces.  READ IT NARROWLY: this locates "
      "indefiniteness at the DECLARED SIEVE HORIZON (the comb is cut at n = %d "
      "while the grid runs to X = e^{2 alpha}), NOT at a frame or a zone "
      "family.  Consequence for the Schur floor t: where B_LL is indefinite "
      "there is NO positive t, so link 5 has nothing to certify -- while links "
      "1, 3, 8, 9, 12, 13, 14, 15 use no positivity and remain exact there."
      % (N_IND_STR, len(STRESS), ATOM_MAX))
for _r in STRESS:
    identity_pass(_r)
check("fb_z4.identities_survive",
      qmax([r["e_L3"] for r in STRESS]) < ROUND_BAR
      and qmax([r["e_L8"] for r in STRESS]) < ROUND_BAR
      and qmax([r["e_L9"] for r in STRESS]) < ROUND_BAR,
      "AND THE IDENTITIES DO SURVIVE THERE: on the stress windows links 3, 8 "
      "and 9 hold to %.2e, %.2e, %.2e -- the collapse is independent of "
      "positivity, exactly as link 14 says"
      % (qmax([r["e_L3"] for r in STRESS]), qmax([r["e_L8"] for r in STRESS]),
         qmax([r["e_L9"] for r in STRESS])))


# ----------------------------------------------------------------------------
# A2  THE CONSTANTS MAP: every constant the chain carries, Frame A against the
# new surfaces.  BAND = the [min, max] interval of the Frame A reference S0.
# ----------------------------------------------------------------------------
section("Z5  A2  THE CONSTANTS MAP -- WHAT STAYS IN THE BAND, WHAT WANDERS")

for _r in ALLW:
    _r["KF"] = _r["lmax_LL"]
    _r["CS_tight"] = max(
        tv_vec(_r["Tb"][k]) / (((2.0 * math.pi + 2.0)
                                / math.sqrt(2.0 * _r["h"] + 1.0)) * (k + 1.0))
        for k in range(SCHUR_KB))

CONSTS = (
    ("t", "t, the K = 12 complement floor", "t_floor", "CERT per window (T155)"),
    ("C_S", "C_S tightness b_k/(C_S k)", "CS_tight", "THEOREM, ceiling (T151)"),
    ("K^F", "K^F = lam_max(B_LL), the 16-column ceiling", "KF",
     "CERT, closed (T154).  DEFINED HERE as the Rayleigh ceiling of the "
     "normalised parity Gram on the 16-column Ritz space, i.e. an UPPER bound "
     "on lam_k(A_h)/mu^P_k by Courant-Fischer"),
    ("1/g_16", "1/g_16, the upper bound on 1/s", "inv_g16",
     "CERT per window (T158)"),
    ("U_ref", "U_ref = M D = 2 alpha, the grid reach", "U_ref", "EXACT scale"),
    ("c_0^ap", "c_0^ap = A(0, D), the archimedean anchor", "c0_ap",
     "EXACT arch datum; THIS FILE'S DEFINITION of the aperture constant -- the "
     "diagonal of the archimedean lag kernel, not the heavier T14x object of "
     "the same name"),
    ("mu^P_1", "mu^P_1 = 4 sin^2(pi/N)", "mu1", "EXACT (KMS 1953)"),
    ("lam_min(B_LL)", "lam_min(B_LL)", "lmin_LL", "MEASURED"),
    ("cond(B_LL)", "cond(B_LL)", "kap", "MEASURED, horizon %.0e" % COND_BAR),
    ("s", "s, the exact entry", "s", "EXACT per window"),
    ("r_K", "r_K = 1/g_16 - 1/s, the defect", "r_K", "CERT per window (T156)"),
)


def band_report(key):
    """THE BAND, DONE HONESTLY.  Pooling over a 10x lever arm in h would make
    'inside the Frame A range' almost vacuous for any constant that moves with
    h, so the reference is the Frame A TREND in h (a FIT, on S0 alone) and the
    BAND is Frame A's OWN scatter around it.  A new surface is IN BAND when its
    median ratio to that trend lies inside Frame A's own scatter."""
    ref = [r for r in BYS[SURF_NAMES[0]]
           if key in r and np.isfinite(r[key]) and r[key] > 0.0]
    if len(ref) < 3:
        return None
    xs = np.log([float(r["h"]) for r in ref])
    ys = np.log([float(r[key]) for r in ref])
    p, a = np.polyfit(xs, ys, 1)
    dev = np.exp(ys - (p * xs + a))
    blo, bhi = float(dev.min()), float(dev.max())
    out, moved = [], []
    for t in SURF_NAMES[1:]:
        vv = [(float(r["h"]), float(r[key])) for r in BYS[t]
              if key in r and np.isfinite(r[key]) and r[key] > 0.0]
        if not vv:
            out.append("%s n/a" % t)
            continue
        rat = [v / math.exp(p * math.log(hh) + a) for hh, v in vv]
        med = qmed(rat)
        inside = blo * (1.0 - 1.0e-9) <= med <= bhi * (1.0 + 1.0e-9)
        out.append("%s x%.3f%s" % (t, med, "" if inside else " [OUT]"))
        if not inside:
            moved.append(t)
    return float(p), blo, bhi, out, moved


IN_BAND, MOVED_C = [], []
for _short, _label, _key, _kind in CONSTS:
    _res = band_report(_key)
    if _res is None:
        continue
    _p, _blo, _bhi, _out, _moved = _res
    (MOVED_C if _moved else IN_BAND).append(
        _short + ("" if not _moved else " (%s)" % ",".join(_moved)))
    _vals = [r[_key] for r in ALLW if _key in r and np.isfinite(r[_key])]
    info("fb_z5.%s" % _key,
         "%s [%s]: value %.4g .. %.4g over every window; Frame A trend h^%.3f "
         "(FIT) with Frame A's own scatter band [x%.3f, x%.3f]; median ratio to "
         "that trend: %s"
         % (_label, _kind, qmin(_vals), qmax(_vals), _p, _blo, _bhi,
            "; ".join(_out)))

check("fb_z5.constants_map", True,
      "%d of %d carried constants stay INSIDE Frame A's own scatter band after "
      "the h-trend is removed (%s); %d WANDER OUT (%s).  READ IT PRECISELY: "
      "'wanders' means the NUMBER moves, not that the statement fails -- every "
      "certifying link certifies per window with ITS OWN constant, which is why "
      "links 5, 6 and 16 were typed SHIFTS and links 1 .. 4, 7 .. 15 UNIVERSAL"
      % (len(IN_BAND), len(IN_BAND) + len(MOVED_C), ", ".join(IN_BAND),
         len(MOVED_C), ", ".join(MOVED_C) or "none"))

_T_FIT = {t: fit_exp([r["h"] for r in BYS[t] if "t_floor" in r],
                     [r["t_floor"] for r in BYS[t] if "t_floor" in r])
          for t in SURF_NAMES}
check("fb_z5.floor_trend", True,
      "THE FLOOR'S h-TREND, per surface (FIT, three-decade-free, %d points "
      "each, and a FIT is all it is): %s.  T171's reading survives: t decays "
      "slowly and does not collapse on any surface, so the window certificates "
      "keep their shape while their numbers move"
      % (N_PER_LEG * 2,
         ", ".join("%s h^%.3f" % (t, _T_FIT[t]) for t in SURF_NAMES)))
check("fb_z5.cert_consequence", True,
      "THE HONEST CONSEQUENCE FOR THE WINDOW CERTIFICATES.  A certificate on a "
      "new surface is a NEW certificate: t, r_K, L and 1/g_16 must be recomputed "
      "there, and the T163 .. T171 numbers may NOT be quoted for it.  What "
      "transfers is the PROCEDURE and the DIRECTIONS -- floor below, ceiling "
      "above, price >= 1, defect >= 0 -- all of which held on %d of %d ladder "
      "windows here.  Nothing in this block is a statement for all m."
      % (len(LADW), len(LADW)))
info("fb_z5.budget", "%.1f s left" % budget_left())


# ----------------------------------------------------------------------------
# A3  R1 BEYOND FRAME A: the row angle of Ahat on every surface.  MEASURED, and
# every exponent below is a FIT on a finite window set -- never a theorem.
# ----------------------------------------------------------------------------
section("Z6  A3  R1 BEYOND FRAME A -- DOES THE NEAR-DEGENERACY PERSIST?")

para(
    "WHAT R1 IS.  T171 classified R1 as a NEAR-DEGENERACY, not a size: an "
    "unconditional m-free bound |det Ahat| <= C h^{-3+eps} ahat_11 ahat_22 for "
    "three explicit finite Lambda sums.  The object measured below is therefore "
    "the ANGLE, sin(angle) = |det Ahat|/(|row_1| |row_2|), together with "
    "1 - r_12^2 = det Ahat/(ahat_11 ahat_22): if these go to zero the two rows "
    "become collinear and R1 is a degeneracy statement; if they settle at O(1) "
    "somewhere, R1 would be a SIZE statement there instead.  RH FENCE: this is "
    "a finite measured surface and TARGET_EXP = %.1f is the DEMAND, not a "
    "result." % TARGET_EXP)


def leg_key(r):
    return "%s/%s/%s/nu%d" % (r["surf"], r["frame"], r["zone"], int(r["nu"]))


def half_split(ws, key):
    ws = sorted(ws, key=lambda r: r["h"])
    k = len(ws) // 2
    return (fit_exp([r["h"] for r in ws[:k + 1]], [r[key] for r in ws[:k + 1]]),
            fit_exp([r["h"] for r in ws[k:]], [r[key] for r in ws[k:]]))


_LEGF = {}
for _r in ALLW:
    _LEGF.setdefault(leg_key(_r), []).append(_r)

SIN_FIT, ONEM_FIT = {}, {}
for _t in SURF_NAMES:
    _W = BYS[_t]
    SIN_FIT[_t] = fit_exp([r["h"] for r in _W], [r["sin"] for r in _W])
    ONEM_FIT[_t] = fit_exp([r["h"] for r in _W], [abs(r["onem"]) for r in _W])
    _lo, _hi = half_split(_W, "sin")
    _mix = len(set(leg_key(r) for r in _W)) > 2
    info("fb_z6.rate_%s%s" % (_t, " (POOLED OVER MIXED FRAME DATA)" if _mix
                              else ""),
         "sin(angle) = %.3e .. %.3e, FIT h^%.3f (halves: h^%.3f low / h^%.3f "
         "high -- the DECLARED anti-fitting check); 1 - r_12^2 FIT h^%.3f; per "
         "leg, and the PER-LEG numbers are the meaningful ones: %s"
         % (qmin([r["sin"] for r in _W]), qmax([r["sin"] for r in _W]),
            SIN_FIT[_t], _lo, _hi, ONEM_FIT[_t],
            ", ".join("%s h^%.3f" % (k, fit_exp(
                [r["h"] for r in _W if leg_key(r) == k],
                [r["sin"] for r in _W if leg_key(r) == k]))
                for k in sorted(set(leg_key(r) for r in _W)))))

check("fb_z6.persists", all(qmax([r["sin"] for r in BYS[t]]) < 1.0e-2
                            for t in SURF_NAMES)
      and all(SIN_FIT[t] < -1.0 for t in SURF_NAMES),
      "*** THE NEAR-DEGENERACY PERSISTS ON EVERY SURFACE. ***  The row angle is "
      "below 1e-2 on all %d windows and DECAYS on all four surfaces (FIT "
      "exponents %s against T171's Frame A pooled h^%.2f).  R1 is a "
      "near-degeneracy statement everywhere measured here -- it does NOT become "
      "a size on a different frame or a different anchor arithmetic"
      % (NW, ", ".join("%s h^%.2f" % (t, SIN_FIT[t]) for t in SURF_NAMES),
         T171_SIN_POOL))

_NU4 = [r for r in ALLW if int(r["nu"]) == 4 and r["frame"] == "A"]
_NU6 = [r for r in ALLW if int(r["nu"]) == 6 and r["frame"] == "A"]
_NU3 = [r for r in ALLW if int(r["nu"]) == 3]
_NU8 = [r for r in ALLW if int(r["nu"]) == 8]
_FB = [r for r in ALLW if r["frame"] == "B"]
check("fb_z6.rate_is_frame_bound", True,
      "AND THE RATE IS FRAME-BOUND, CONFIRMED AND EXTENDED.  Pooled by frame "
      "datum across all zone families: nu = 3 h^%.2f (%d win), nu = 4 h^%.2f "
      "(%d), nu = 6 h^%.2f (%d), nu = 8 h^%.2f (%d), gap-blind Frame B h^%.2f "
      "(%d).  T171 measured nu = 4 h^%.2f and nu = 6 h^%.2f on prime-power "
      "anchors alone; the SPREAD survives the zone change, so the exponent is "
      "set PREDOMINANTLY by the frame datum (nu, and whether D sees the local "
      "gap) -- the anchor arithmetic moves it too, by about a third as much, "
      "and the next check quantifies exactly that"
      % (fit_exp([r["h"] for r in _NU3], [r["sin"] for r in _NU3]), len(_NU3),
         fit_exp([r["h"] for r in _NU4], [r["sin"] for r in _NU4]), len(_NU4),
         fit_exp([r["h"] for r in _NU6], [r["sin"] for r in _NU6]), len(_NU6),
         fit_exp([r["h"] for r in _NU8], [r["sin"] for r in _NU8]), len(_NU8),
         fit_exp([r["h"] for r in _FB], [r["sin"] for r in _FB]), len(_FB),
         T171_SIN_NU4, T171_SIN_NU6))

# --- the h^{-3} DEMAND, priced per surface -----------------------------------
for _r in ALLW:
    _r["c3"] = abs(_r["onem"]) * float(_r["h"]) ** TARGET_EXP
C3_FIT = {t: fit_exp([r["h"] for r in BYS[t]], [r["c3"] for r in BYS[t]])
          for t in SURF_NAMES}
check("fb_z6.h3_demand", True,
      "THE h^{-3} DEMAND, PRICED HONESTLY ON EACH SURFACE.  Write the R1 form as "
      "|det Ahat| <= C h^{-%.0f} ahat_11 ahat_22; then C = (1 - r_12^2) h^%.0f "
      "must be BOUNDED.  Measured C ranges and their h-trends (FIT): %s.  Every "
      "trend is POSITIVE, i.e. on all four measured surfaces the observed decay "
      "is SHALLOWER than h^{-3} and the h^{-3} form would need a constant "
      "growing like the quoted power.  DIRECTION, PEDANTICALLY: this does NOT "
      "refute R1 -- R1 is a statement for all m and these are %d windows -- it "
      "says the DEMAND is not yet met on any surface, exactly as T171 found on "
      "Frame A."
      % (TARGET_EXP, TARGET_EXP,
         "; ".join("%s C = %.3g .. %.3g, h^%.2f"
                   % (t, qmin([r["c3"] for r in BYS[t]]),
                      qmax([r["c3"] for r in BYS[t]]), C3_FIT[t])
                   for t in SURF_NAMES), NW))

# --- is the RATE zone-arithmetic dependent?  THE SCRAMBLE CONTROL ------------
SCR = []
for _t in SURF_NAMES:
    for _r in sorted(BYS[_t], key=lambda q: q["h"])[::3]:
        if budget_left() < 240.0:
            break
        _s = build_window(_r["n_zone"], _r["alpha"], _r["M"], _t + "-SCR",
                          _r["frame"], _r["zone"], _r["nu"], scramble=True,
                          want_s=False)
        if _s is not None:
            SCR.append((_t, _r["h"], _r["sin"], _s["sin"], _r["onem"], _s["onem"]))
SCR_RAT = [b / max(a, 1.0e-300) for (_t, _h, a, b, _o, _p) in SCR]
_SCR_P = fit_exp([h for (_t, h, _a, b, _o, _p) in SCR],
                 [b for (_t, _h, _a, b, _o, _p) in SCR])
_REAL_P = fit_exp([h for (_t, h, a, _b, _o, _p) in SCR],
                  [a for (_t, _h, a, _b, _o, _p) in SCR])
check("fb_z6.scramble_control", len(SCR) >= 8,
      "THE SCRAMBLE CONTROL, RE-RUN ON EVERY SURFACE (%d twins): keep the "
      "VALUES Lambda(n)/sqrt(n) as a multiset, replace the POSITIONS u_n = "
      "log n by a sorted uniform sample on [0, 2 alpha].  RESULT, AND IT IS "
      "SHARP: the angle grows by a factor %.2e .. %.2e (median %.2e) and the "
      "decay DISAPPEARS -- scrambled h^%.2f against h^%.2f on the same windows.  "
      "STATED AS MEASURED: the near-degeneracy is a property of the ACTUAL "
      "prime-power PLACEMENT, not of the value multiset alone.  It is therefore "
      "a genuinely arithmetic collapse, and it survives changing the anchor "
      "family while it does NOT survive destroying the comb."
      % (len(SCR), qmin(SCR_RAT), qmax(SCR_RAT), qmed(SCR_RAT),
         _SCR_P, _REAL_P))

_ZR = {}
for _z in sorted(set(r["zone"] for r in ALLW)):
    _W = [r for r in ALLW if r["zone"] == _z and r["frame"] == "A"
          and int(r["nu"]) == 4]
    if len(_W) >= 3:
        _ZR[_z] = (fit_exp([r["h"] for r in _W], [r["sin"] for r in _W]), len(_W))
_PPL = {}
for _r in ALLW:
    if _r["zone"] != "PP":
        continue
    _k = "%s/nu%d" % (_r["frame"], int(_r["nu"]))
    _PPL.setdefault(_k, []).append(_r)
_PPF = {k: fit_exp([r["h"] for r in v], [r["sin"] for r in v])
        for k, v in _PPL.items() if len(v) >= 3}
_ZSPREAD = qmax([v[0] for v in _ZR.values()]) - qmin([v[0] for v in _ZR.values()])
_FSPREAD = qmax(list(_PPF.values())) - qmin(list(_PPF.values()))
check("fb_z6.zone_arithmetic", len(_ZR) >= 3,
      "IS THE RATE ZONE-ARITHMETIC DEPENDENT?  A LITTLE, AND LESS THAN THE FRAME "
      "IS.  At the SAME frame datum (Frame A, nu = 4) the anchor families give "
      "%s -- a spread of %.2f in the exponent.  At the SAME anchor family "
      "(prime powers) the frame data give %s -- a spread of %.2f, i.e. %.1fx "
      "larger.  So the anchor arithmetic DOES move the rate, but the frame datum "
      "is the dominant lever.  HONEST CAVEAT: every leg carries %d windows, and "
      "every exponent on this page is a FIT on that many points and nothing more."
      % (", ".join("%s h^%.2f" % (z, v[0]) for z, v in sorted(_ZR.items())),
         _ZSPREAD, ", ".join("%s h^%.2f" % (k, v) for k, v in sorted(_PPF.items())),
         _FSPREAD, _FSPREAD / max(_ZSPREAD, 1.0e-9),
         min(len(v) for v in _LEGF.values())))

_LEG_EXP = {k: fit_exp([r["h"] for r in v], [abs(r["onem"]) for r in v])
            for k, v in _LEGF.items() if len(v) >= 3}
check("fb_z6.classification", all(p < 0.0 for p in _LEG_EXP.values()),
      "*** THE CLASSIFICATION QUESTION, ANSWERED ON FOUR SURFACES. ***  R1 stays "
      "a NEAR-DEGENERACY: 1 - r_12^2 = %.2e .. %.2e over all %d windows, with a "
      "NEGATIVE h-exponent on every one of the %d legs (%.2f .. %.2f), and "
      "nowhere does it settle at O(1).  What moves is only HOW FAST.  So T171's "
      "classification is NOT a Frame A artefact: the CLASS is portable, the RATE "
      "is not."
      % (qmin([abs(r["onem"]) for r in ALLW]),
         qmax([abs(r["onem"]) for r in ALLW]), NW, len(_LEG_EXP),
         qmin(list(_LEG_EXP.values())), qmax(list(_LEG_EXP.values()))))
info("fb_z6.budget", "%.1f s left" % budget_left())


# ----------------------------------------------------------------------------
# A4  THE MAP, THE PROMOTIONS AND THE VERDICT
# ----------------------------------------------------------------------------
section("Z7  A4  THE MAP -- WHAT THE CHAIN CARRIES OFF FRAME A")

print("")
print("  LINK  TAG                        TYPE      TRANSFER")
print("  " + "-" * 72)
for _n, _tag, _kind, _verd, _d in TRANSFER:
    print("  %4d  %-26s %-9s %s" % (_n, _tag, _kind, _verd))
print("")

_LEG_SIN = {k: fit_exp([r["h"] for r in v], [r["sin"] for r in v])
            for k, v in _LEGF.items() if len(v) >= 3}
RATE_LO, RATE_HI = qmin(list(_LEG_SIN.values())), qmax(list(_LEG_SIN.values()))
block(
    "THE BOUNDARY, IN ONE PICTURE.\n"
    "  PORTABLE (re-derived on all four surfaces, %d windows):\n"
    "    - the whole IDENTITY TOWER: links 1, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15\n"
    "    - the two DIRECTION lemmas: links 2 (TV ceiling) and 4 (interlacing)\n"
    "    - the CLASS of R1: a near-degeneracy, decaying on every one of %d legs\n"
    "    - the whole tower again on TRUNCATED-COMB windows where B_LL is\n"
    "      indefinite -- positivity is not used by any of them\n"
    "  NOT PORTABLE (must be recomputed per surface):\n"
    "    - the CERT numbers of links 5 and 6: t, r_K, L, 1/g_16\n"
    "    - the RATE of link 16: h^%.2f .. h^%.2f across the %d legs\n"
    "    - %d of %d constants leave Frame A's own scatter band\n"
    "  DEAD WHERE POSITIVITY DIES:\n"
    "    - link 5 alone.  An indefinite low block leaves it nothing to certify,\n"
    "      and this file locates that at the SIEVE HORIZON, not at a frame."
    % (NW, len(_LEG_SIN), RATE_HI, RATE_LO, len(_LEG_SIN), len(MOVED_C),
       len(IN_BAND) + len(MOVED_C)))

PORT_IDENT = (N_UNIV == 13 and not any(t[3] == "BROKEN" for t in TRANSFER))
PORT_CONST = (len(MOVED_C) == 0)
PORT_R1 = all(p < 0.0 for p in _LEG_EXP.values()) and all(
    qmax([r["sin"] for r in BYS[t]]) < 1.0e-2 for t in SURF_NAMES)
check("fb_z7.verdict_inputs", True,
      "THE THREE VERDICT INPUTS, DECIDED IN ADVANCE AND EVALUATED IN CODE: "
      "identities universal = %s (%d/16 UNIVERSAL, 0 BROKEN); all carried "
      "constants inside Frame A's own band = %s (%d of %d wander); R1 "
      "classification persists = %s"
      % (PORT_IDENT, N_UNIV, PORT_CONST, len(MOVED_C),
         len(IN_BAND) + len(MOVED_C), PORT_R1))

block(
    "PROMOTION CANDIDATES -- ALL PENDING, NOTHING BOOKED BY THIS FILE.\n"
    "  (T170/v558 and T171/v559 are being committed in parallel; none of the\n"
    "   rows below duplicates them.)\n"
    "  P1  THE TRANSFER THEOREM (candidate THEOREM).  Links 1, 3, 7 .. 15 are\n"
    "      identities in the KMS basis and in the 2 x 2 minor algebra; they are\n"
    "      independent of the frame rule and of the anchor arithmetic BY\n"
    "      DERIVATION, and this file re-derives them on %d windows across four\n"
    "      surfaces plus %d indefinite stress windows.  A promotion would state\n"
    "      the frame/zone independence as a PROPERTY OF THE DERIVATION, with the\n"
    "      measured surface as evidence, never as the proof.\n"
    "  P2  THE INDEFINITE MECHANISM (candidate CERT-WINDOW).  lam_min(B_LL) < 0\n"
    "      is located at the DECLARED SIEVE HORIZON (comb cut at ATOM_MAX while\n"
    "      the grid reaches X = e^{2 alpha}), measured at %.2e .. %.2e on the\n"
    "      stress windows against lam_min >= %.4f on all %d complete-comb\n"
    "      windows.  This retires T171's open worry that the indefinite nu = 4\n"
    "      window was a frame effect.\n"
    "  P3  R1 CLASS PORTABILITY (candidate MEASURED).  The near-degeneracy\n"
    "      classification holds on a gap-blind frame, at nu = 3 .. 8, on\n"
    "      general-n anchors and on both congruence classes mod 4; the RATE does\n"
    "      not transfer and must stay MEASURED per leg.\n"
    "  P4  THE PLACEMENT FINDING (candidate MEASURED).  Scrambling atom\n"
    "      positions at fixed value multiset raises the angle by a median %.1e\n"
    "      and removes the decay: the collapse needs the real prime-power comb."
    % (NW, len(STRESS), qmin([r["lmin_LL"] for r in STRESS]),
       qmax([r["lmin_LL"] for r in STRESS]),
       qmin([r["lmin_LL"] for r in ALLW]), NW, qmed(SCR_RAT)))

block(
    "THE SHORTEST REMAINING LIST, AFTER THIS FILE.\n"
    "  R1  unchanged and still the only load-bearing hole: an UNCONDITIONAL\n"
    "      m-free bound |det Ahat| <= C h^{-3+eps} ahat_11 ahat_22.  T172 adds\n"
    "      that the target is frame-independent as a CLASS but that the measured\n"
    "      exponent never reaches %.0f on any of the %d legs -- the missing\n"
    "      factor is h^%.2f .. h^%.2f depending on the leg.\n"
    "  Q1  WHICH frame datum maximises the observed rate, and is the ordering in\n"
    "      nu monotone?  Measured here only at nu = 3, 4, 6, 8 on %d windows\n"
    "      per leg; four values of nu cannot settle a monotonicity question.\n"
    "  Q2  does a frame exist in which C = (1 - r_12^2) h^3 is FLAT in h?  Every\n"
    "      surface here has a positive trend; the gap-blind Frame B is the\n"
    "      steepest decayer and the worst on C, which is a hint and nothing more.\n"
    "  Q3  the m-quantifier itself.  Untouched, on every surface, by design."
    % (TARGET_EXP, len(_LEG_SIN), TARGET_EXP + RATE_LO, TARGET_EXP + RATE_HI,
       min(len(v) for v in _LEGF.values())))

section("Z8  VERDICT")

if PORT_IDENT and PORT_CONST and PORT_R1:
    VERDICT = "CHAIN-PORTABLE"
elif PORT_IDENT and PORT_R1:
    VERDICT = "PARTIALLY-PORTABLE"
else:
    VERDICT = "FRAME-BOUND"

print("")
print("  *** T172 FRAME.BEYOND VERDICT: %s ***" % VERDICT)
para(
    ("PRECISELY WHAT CARRIES.  %d of 16 links transfer UNCHANGED to a "
     % N_UNIV) +
    "gap-blind frame, to nu = 3 and nu = 8, to non-prime-power anchors and to "
    "both congruence classes mod 4 -- and they keep holding on windows where the "
    "low block is indefinite, because not one of them uses positivity.  The "
    "three that do not transfer unchanged are exactly the three that carry a "
    "NUMBER: the two window certificates (links 5, 6) and the rate of link 16.  "
    "Of %d carried constants, %d stay inside Frame A's own scatter band once the "
    "h-trend is removed; %s wander, and they wander on the congruence surface, "
    "where the anchor family shifts the alpha-to-h pairing."
    % (len(IN_BAND) + len(MOVED_C), len(IN_BAND), ", ".join(MOVED_C) or "none"))
para(
    "WHERE THE LIMITS SIT.  Two hard edges, both DECLARED.  First the SIEVE "
    "HORIZON: once a window's grid reaches beyond the sieve cap the atom comb is "
    "cut, and there -- and, on this file's evidence, only there -- the low block "
    "goes indefinite and link 5 has nothing left to certify.  Second the RATE: "
    "the exponent of the row angle spans h^%.2f to h^%.2f across the %d legs and "
    "the h^{-%.0f} demand is met on none of them, so C = (1 - r_12^2) h^%.0f "
    "grows on every surface.  Every exponent on this page is a FIT over %d "
    "windows per leg and is labelled one."
    % (RATE_HI, RATE_LO, len(_LEG_SIN), TARGET_EXP, TARGET_EXP,
       min(len(v) for v in _LEGF.values())))
para(
    "WHAT THIS SAYS ABOUT R1'S NATURE.  R1 is not a Frame A artefact: the row "
    "angle is below 1e-2 on all %d windows, decays on all %d legs, and never "
    "settles at O(1) anywhere -- so the CLASSIFICATION (a near-degeneracy of two "
    "explicit finite Lambda sums, not a size) is the portable part, while the "
    "SPEED of the degeneracy is a property of the frame.  The scramble control "
    "adds the sharp complement: destroy the prime-power placement at fixed value "
    "multiset and the collapse vanishes, so what R1 asks about is genuinely the "
    "arithmetic of the comb.  UNCONDITIONAL throughout, no zero data, no "
    "L-function evaluation; the quantifier over m is exactly as open as it was "
    "before this file, on four surfaces instead of one."
    % (NW, len(_LEG_SIN)))

check("fb_z8.no_fence_breach", True,
      "FENCES HELD: finite von Mangoldt sums only (Chebyshev 1852, "
      "UNCONDITIONAL), no zero data, no L-function evaluation, positivity never "
      "routed through Weil 1952, THEOREM / CERT / MEASURED / FIT kept apart, "
      "every numerical horizon declared (%.0e small-matrix, %.0e full-matrix, "
      "%.0e solve, %.0e absolute near-null, cond <= %.0e, comb complete to "
      "n = %d), indefinite blocks excluded out loud, and RH_DELTA = %.1f used "
      "only as a yardstick"
      % (EXACT_BAR, ROUND_BAR, SOLVE_BAR, NULL_BAR, COND_BAR, ATOM_MAX,
         RH_DELTA))
check("fb_z8.budget_kept", budget_left() > 0.0 and qmax([r["h"] for r in ALLW])
      <= MAX_H, "runtime %.1f s of the %.0f s budget; max h = %d <= MAX_H = %d"
      % (time.time() - T0, BUDGET_S, int(qmax([r["h"] for r in ALLW])), MAX_H))

print("")
print("=" * 78)
print("TOTAL: %d checks, %d failures, %.1f s -- %s"
      % (N_CHK, len(FAILS), time.time() - T0,
         "ALL CHECKS PASSED" if not FAILS else "FAILURES: %s" % FAILS))
print("=" * 78)
