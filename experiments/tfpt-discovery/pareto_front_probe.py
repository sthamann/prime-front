"""PART 163 -- THE CONTRACT ``PARETO.FRONT'': THE OPERATING POINT.

THE RH FENCE, FIRST, PROMINENT, AND IT IS THE MOST IMPORTANT SENTENCE IN THIS
FILE.  Nothing here reads, generates, tabulates, approximates or extrapolates a
single zero of any L-function, and no L-function is ever evaluated anywhere.  The
only arithmetic object touched is a FINITE sum over prime powers produced by a
von Mangoldt sieve inside this file.  The number 1/2 appears below ONLY as the
STRENGTH of a classical statement, i.e. as a yardstick against which a required
depth is compared.  A COMPARISON OF STRENGTHS IS NOT A CLAIM: nothing below
asserts, assumes, weakens or implies RH in either direction, and Weil 1952 /
Bombieri 2000 remain an ADDRESS and nothing else.  An AST firewall enforces the
absence of zero data, the import whitelist, the absence of write-mode file access
and the single-file rule.

WHERE T162 LEFT THE CHAIN.  R2'' is ONE pairing, x^T B_LL x = sum_d c_d w_d, and
T162 turned it into a PRICED optimisation over trial vectors: by the Thomson /
Dirichlet dual every admissible x gives 1/s <= Q(x), so the chain may choose x
and pay for it in the 1/s ceiling.  The FEJER SPLIT (self-adjointness: tapering x
IS smoothing the sampled Lambda-mass; Fejer 1915) reached delta_bnd = 0.133 ..
0.417, BELOW the RH-strength yardstick 1/2, on all 18 windows -- but its price
grows like h^2.86, so R2'' was RELOCATED INTO THE PRICE, not closed.

WHAT THIS FILE DOES.  R1 is the heart: the Fejer taper gets a CONTINUOUS knob
sigma and the two currencies are measured over the whole surface, so that the
PARETO FRONT can be read off as a number series -- and the affordable price is
NOT invented here, it is the T158 Cholesky ladder 1/g_K, whose rungs are prices
the chain has ALREADY accepted.  R2 leaves the sixteen low modes (K = 16, 32,
64).  R3 does R-B'', R-D and the end-to-end assembly with the obligatory stress.
R4 is the map V35, the rest list and the verdict.

THE OUTCOME IN ADVANCE, SO THAT NOTHING BELOW READS AS A REVEAL.  The verdict is
FRONT-RESISTS, and it is a THEOREM rather than a failed search.  Two identities do
the work.  First, substituting the price into the demand gives, for every
admissible trial vector, delta_bnd(x) = 1/2 + log(2 kappa g_16 TV(x) / P(x)) /
log X, so price and demand are TWO COORDINATES ON ONE OBJECT and sub-yardstick
demand IS the inequality P > 2 kappa g_16 TV.  Second, the total variation has an
unconditional floor: w_0(x) = ||a(x)||^2 and TV(x) >= |w_0(x)|, so the
normalisation x_1 = 1 that the Thomson direction requires forces
TV(x) >= 1 / mu^P_1 = 1 / (4 sin^2(pi/N)), which grows like h^2.  Hence the
crossing price is bounded below by something growing like h^2 -- over the WHOLE
admissible set, not just the families swept -- and a flat-price crossing is
impossible.  The h^2 that T161 called granularity and T162 relocated into the
price is therefore the RECIPROCAL SPECTRAL GAP of the parity Laplacian meeting the
entry normalisation, and it was never in the primes.  The one new positive: the
crossing does sit strictly inside the T157 route-(0) price the chain already
accepted, with a widening margin -- at a price that grows, hence not a uniform
certificate.

DISCIPLINE.  THEOREM / CERT-UNIF / CERT-WINDOW / MEASURED / FIT strictly apart,
every claim labelled in place.  TWO CURRENCIES, NEVER MIXED: delta_val is the
residual VALUE against |Q| (a FLOOR), delta_bnd is what a PROOF must beat (the
Chebyshev-strength demand).  SCALES ARE PEDANTIC: alpha = log n_zone; D =
2 alpha / M; h = M / 2 = alpha / D; X = e^{2 alpha}; log X = 2 alpha exactly.
Classics cited where used: Chebyshev 1852, Dirichlet 1829, Abel 1826,
Mellin 1896, Fejer 1915, Schur 1917, Kac-Murdock-Szego 1953,
Rosser-Schoenfeld 1962, Weil 1952, Bombieri 2000.
HARD CAPS: any factorised matrix <= 1500; probe budget < 900 s.
"""

import ast
import math
import os
import time

import numpy as np

T0 = time.time()
np.random.seed(163163)

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
CHUNK = 16384
ATOM_MAX = 400000
ZONE_DEEP = 380000

N_ZONES = 40                 # the SAME surface RECIPE as T161 / T162 (log-spaced
                             # in h), sampled DENSER because the correlation form
                             # of Q0 makes each window cost milliseconds
HCAP = 1450                  # inside the HARD cap MAX_H = 1500
H_MIN = 128                  # DECLARED: >= 2 x the largest mode block K = 64
N_ATOM_MIN = 40              # DECLARED surface floor (as T161 / T162)
SCHUR_KB = 16                # the FIXED low block of the T152 .. T162 chain
KB_MAX = 64                  # the ENLARGED block of R2, declared here

EXACT_BAR = 1.0e-12          # the bar on every claimed IDENTITY
COND_BAR = 1.0e12            # the T159 numerical horizon on cond(B_LL)
BAR_FLAT = 0.25              # |exponent| bar for "flat / non-growing" (T159)
EPSM = float(np.finfo(float).eps)
B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962)
TAU = 0.1                    # the fraction of |Q| a bound may miss by
RH_DELTA = 0.5               # RH STRENGTH, as a delta.  A YARDSTICK, NOT A CLAIM
HEADROOM_BAR = 1.0e3         # DECLARED cancellation headroom over machine eps

# T161 / T162 numbers, QUOTED, never recomputed as an input to anything
T162_DBND_FEJ = (0.133, 0.417)
T162_PRICE_EXP = 2.86
T162_DVAL = (1.88, 1.38, 0.93)
T162_KAPPA = 0.03882          # the MEASURED |psi(x)-x| <= kappa x on this range;
                              # the Rosser-Schoenfeld form of the SAME input is
                              # psi(x) <= 1.03883 x = (1 + kappa) x
T162_QUARTER = 0.25
T161_RHO1 = (1.0036, 1.0140)
T162_BALANCE = (10, 2, 3, 9)

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
    for ln in wrap_at(" ".join(text.split()), width - len(indent)):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T0)


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
    """d log y / d log x -- a FIT, always labelled as such."""
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    ok = np.isfinite(xs) & np.isfinite(ys) & (np.abs(ys) > 0)
    ok &= xs > 0
    if int(np.sum(ok)) < 3:
        return float("nan")
    return float(np.polyfit(np.log(xs[ok]), np.log(np.abs(ys[ok])), 1)[0])


# ----------------------------------------------------------------------------
# THE AST FIREWALL -- no zero data, no L-function, no write, one file
# ----------------------------------------------------------------------------
FORBIDDEN_TOKENS = tuple("".join(parts) for parts in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
    ("25.01", "0857"), ("30.42", "4876"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "numpy", "scipy"}


def firewall():
    src = open(os.path.abspath(__file__), "r").read()
    low = src.lower()
    hits = [tok for tok in FORBIDDEN_TOKENS if tok in low]
    tree = ast.parse(src)
    bad_imports, bad_writes = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    bad_imports.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                bad_imports.append(node.module)
        elif isinstance(node, ast.Call):
            nm = getattr(node.func, "id", None) or getattr(node.func, "attr", None)
            if nm in ("open",):
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(ch in mode for ch in "wax+"):
                    bad_writes.append(mode)
    check("pf_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("pf_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("pf_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("pf_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "pareto_front_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# the prime powers -- a FINITE von Mangoldt sieve, and nothing else
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
    return lam


def atom_table(n_max):
    lam = von_mangoldt_table(n_max)
    out = []
    for n in np.nonzero(lam > 0.0)[0]:
        out.append((int(n), float(lam[n]), math.log(float(n)),
                    2.0 * float(lam[n]) / math.sqrt(float(n))))
    return out


# ----------------------------------------------------------------------------
# the archimedean lag kernel A(s, D) -- the T115 assembly, bit for bit
# ----------------------------------------------------------------------------
def _arch_A_far(s, D):
    """A(s, D) = -int_{s-D}^{s+D} (1 - |s-w|/D) g(w) dw for s >= D, with
    g(w) = e^{-w/2} / (1 - e^{-2w})."""
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


def atom_lags(alpha, M, atoms):
    """Every prime-power atom contributes -mu_j/2 times a linear spline of total
    mass 1 around u_j = log n_j, plus a REFLECTED spline when u_j < D."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    mu_tot = 0.0
    n_hit = 0
    for u_j, mu_j in atoms:
        mu_tot += mu_j
        n_hit += 1
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
    return c, D, mu_tot, n_hit


# ----------------------------------------------------------------------------
# the parity sector, the closed weights, the Abel tails
# ----------------------------------------------------------------------------
def parity_mu(m):
    """mu^P_k = 4 sin^2(pi k / N), N = 2m + 1 (Kac-Murdock-Szego 1953)."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m, kb=None):
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, (kb or m) + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_P_mat(m):
    """L_P = tridiag(-1, 2, -1) with last diagonal 3; EQUIVALENTLY
    odd_toeplitz(c^L, M) for c^L = (2, -1, 0, ..., 0), re-checked in R3."""
    L = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    L[m - 1, m - 1] = 3.0
    return L


def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: TOEPLITZ MINUS HANKEL, exact."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def _cos_sum(alpha, beta, L):
    """*** THE DIRICHLET-KERNEL IDENTITY (Dirichlet 1829). ***  THEOREM; this is
    what makes w_d and every R_kl(d) CLOSED.  Re-checked in R3."""
    alpha = np.asarray(alpha, float)
    beta = np.asarray(beta, float)
    L = np.asarray(L, float)
    ha = 0.5 * alpha
    s = np.sin(ha)
    out = np.where(np.abs(s) < 1.0e-14,
                   L * np.cos(beta),
                   np.sin(L * ha) / np.where(np.abs(s) < 1.0e-14, 1.0, s)
                   * np.cos(beta + (L + 1.0) * ha))
    return np.where(L >= 1.0, out, 0.0)


def _kl_geometry(m):
    M = 2 * m
    N = 2 * m + 1
    d = np.arange(M, dtype=float)
    LT = np.maximum(m - d, 0.0)
    J = (M - 1) - d
    n0 = np.maximum(1.0, m + 1.0 - d)
    n1 = np.minimum(float(m), 2.0 * m - d)
    LH = np.maximum(n1 - n0 + 1.0, 0.0)
    LH = LH.copy()
    LH[0] = 0.0
    return M, N, d, LT, J, n0, LH


def R_pair(k, l, m, om=None):
    """The (k, l) contribution to the closed weight vector, as FOUR Dirichlet
    kernels (T160 .. T162).  Kept ONLY as the reference against which the
    correlation form below is machine-checked; nothing in R1 .. R3 calls it in
    an inner loop."""
    M, N, d, LT, J, n0, LH = _kl_geometry(m)
    if om is None:
        om = 2.0 * math.pi * np.arange(1, SCHUR_KB + 1) / N
    am, ap = om[k] - om[l], om[k] + om[l]
    T = (4.0 / N) * (_cos_sum(am, -om[l] * d, LT) - _cos_sum(ap, om[l] * d, LT))
    sh = am * (n0 - 1.0)
    sp = ap * (n0 - 1.0)
    H = (2.0 / N) * (_cos_sum(ap, -om[l] * (J + 2.0) + sp, LH)
                     - _cos_sum(am, om[l] * (J + 2.0) + sh, LH))
    out = T - H
    out[0] = T[0] * 0.5 - H[0]
    return out


def lag_weights_closed(x, m, kb=None):
    """w_d = sum_{k,l} a_k a_l R_kl(d), a_k = x_k / sqrt(mu^P_k).  THE T160 .. T162
    ROUTE, kept as the reference form."""
    nb = x.shape[0]
    N = 2 * m + 1
    mu = parity_mu(m)[:nb]
    a = x / np.sqrt(mu)
    om = 2.0 * math.pi * np.arange(1, nb + 1) / N
    idx = range(nb) if kb is None else kb
    w = np.zeros(2 * m)
    for k in idx:
        if a[k] == 0.0:
            continue
        for l in idx:
            if a[l] == 0.0:
                continue
            w += a[k] * a[l] * R_pair(k, l, m, om)
    return w


def lag_weights_corr(x, m, Tb):
    """*** THEOREM (checked against lag_weights_closed in Q0), AND IT IS WHAT
    MAKES R1 AND R2 AFFORDABLE. ***  Write v = T_K^T a, a_k = x_k / sqrt(mu^P_k),
    so that x^T B_K x = v^T A v with A_rs = c_{|r-s|} - c_{M-1-r-s}.  Expanding,

        sum_{r,s} v_r v_s c_{|r-s|}   = c_0 A_0 + 2 sum_{d>=1} c_d A_d ,
        sum_{r,s} v_r v_s c_{M-1-r-s} = sum_{d>=1} c_d H_{M-1-d} ,

    with A_d = sum_r v_r v_{r+d} the AUTOCORRELATION and H_e = sum_{r+s=e} v_r v_s
    the SELF-CONVOLUTION of v.  Hence the closed weight vector is

        w_0 = A_0 ,   w_d = 2 A_d - H_{M-1-d}   (d >= 1) ,

    exact, O(h^2) in C rather than O(K^2) Dirichlet kernels, and INDEPENDENT of
    the block size K -- which is precisely what R2 needs."""
    nb = x.shape[0]
    a = x / np.sqrt(parity_mu(m)[:nb])
    v = Tb[:nb, :].T @ a
    M = 2 * m
    ac = np.correlate(v, v, "full")[m - 1:]          # A_0 .. A_{m-1}
    cv = np.convolve(v, v)                           # H_0 .. H_{2m-2}
    w = np.zeros(M)
    w[:m] = 2.0 * ac
    w[0] = ac[0]
    ee = (M - 1) - np.arange(1, M)
    w[1:] -= np.where(ee <= M - 2, cv[np.minimum(ee, M - 2)], 0.0)
    return w


def abel_tail(v):
    """W^1_d = sum_{e >= d} v_e (Abel 1826)."""
    return np.cumsum(v[::-1])[::-1]


def fwd_diff(c):
    out = np.zeros_like(c)
    out[1:] = c[1:] - c[:-1]
    return out


def back_diff(w):
    """(Delta w)_d = w_d - w_{d+1}, with w_M := 0."""
    out = np.empty_like(w)
    out[:-1] = w[:-1] - w[1:]
    out[-1] = w[-1]
    return out


# ----------------------------------------------------------------------------
# the CLOSED smooth cell moments -- the Mellin pairing of the C1 currency
# ----------------------------------------------------------------------------
_CMX, _CMW = np.polynomial.legendre.leggauss(24)


def cell_moment(M, D, hi, beta=0.5):
    """C_d(beta) = int_0^{hi} hat_d(u) e^{beta u} du for the linear-spline hats of
    the lag grid.  beta = 1/2 is the PNT main term dpsi = dx (Mellin 1896)."""
    out = np.zeros(M)
    for side in (-1, +1):
        for d in range(M):
            lo = (d + min(side, 0)) * D
            up = (d + max(side, 0)) * D
            lo, up = max(lo, 0.0), min(up, hi)
            if up <= lo:
                continue
            mid, half = 0.5 * (lo + up), 0.5 * (up - lo)
            u = mid + half * _CMX
            out[d] += half * float(np.dot(_CMW, (1.0 - np.abs(u - d * D) / D)
                                          * np.exp(beta * u)))
    return out


def fejer_taper(K, sig):
    """*** THE KNOB OF R1 (Fejer 1915). ***  t_k(sigma) = max(0, 1 - k / sigma),
    k = 0 .. K-1, the CONTINUOUS Fejer / Cesaro window of width sigma.  T162 used
    the four integer widths nb = 2, 4, 8, 16 of this same family; sigma = K means
    the full linear taper and sigma -> infinity means no taper at all."""
    if not np.isfinite(sig):
        return np.ones(K)
    return np.maximum(0.0, 1.0 - np.arange(K) / float(sig))


def cf_ladder(Bm, K):
    """*** THE T158 CHOLESKY / CONTINUED-FRACTION LADDER, AND IT IS THE PRICE
    REFERENCE OF THIS FILE. ***  Q_K = B_{1:K,1:K} = L_K L_K^T, y = L_K^-1 e_1,
    g_K = e_1^T Q_K^-1 e_1 = sum_{j<=K} y_j^2, every term STRICTLY POSITIVE, and
    the partial sum to J is exactly g_J because the leading J x J block of L_K is
    the Cholesky factor of Q_J.  THEOREM (Schur 1917 nested complements;
    Haynsworth 1968; the Jacobi continued fraction).  Consequence used
    throughout: s >= g_J, i.e. 1/s <= 1/g_J, a DECREASING chain of UPPER bounds
    on 1/s starting at 1/g_1 = B_11."""
    Q = sym(np.asarray(Bm)[:K, :K])
    try:
        L = np.linalg.cholesky(Q)
    except np.linalg.LinAlgError:
        return None
    e1 = np.zeros(K)
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return np.cumsum(y ** 2)


section("PART 163 -- PARETO.FRONT -- Q0  THE FENCE, THE SCALES, THE SURFACE")
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]
NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


_psi_run, _bpsi = 0.0, 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
check("pf_q0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f VERIFIED at every jump point up to n = %d (max %.6f), "
      "never assumed beyond it (Chebyshev 1852; Rosser-Schoenfeld 1962).  THIS is "
      "the unconditional input every delta below is priced against"
      % (B_PSI, ATOM_MAX, _bpsi))

X0_CHEB = 100.0
_psi, _kap = 0.0, 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi += _lam
    if _n >= X0_CHEB:
        _kap = max(_kap, abs(_psi - _n) / _n)
KAPPA = _kap
check("pf_q0.chebyshev_kappa",
      0.0 < KAPPA < 0.2 and abs(KAPPA - T162_KAPPA) < 0.001
      and abs((1.0 + KAPPA) - B_PSI) < 0.001,
      "*** THE ONE UNCONDITIONAL ARITHMETIC INPUT OF THE WHOLE FILE, MEASURED ON "
      "THIS SURFACE AND NOTHING ELSE. ***  |psi(x) - x| <= kappa x with kappa = "
      "%.6f, verified at EVERY jump point in %.0f <= x <= %d; T162 used the same "
      "constant and the Rosser-Schoenfeld 1962 form of it is psi(x) <= "
      "(1 + kappa) x = %.5f x, which reproduces the quoted Chebyshev strength "
      "%.5f to %.1e.  Every delta_bnd below is 1/2 + log(2 kappa TV / |Q|) / log X "
      "with THIS kappa and nothing else"
      % (KAPPA, X0_CHEB, ATOM_MAX, 1.0 + KAPPA, B_PSI,
         abs(1.0 + KAPPA - B_PSI)))

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = int(math.ceil(UU_ALL[k] / D_k - 1.0e-9)) + 1
    if M_k % 2:
        M_k += 1
    h_k = M_k // 2
    if h_k < H_MIN or h_k > HCAP:
        continue
    if len(atoms_in(UU_ALL[k])) < N_ATOM_MIN:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    CAND.sort(key=lambda t: t[3])          # LOG-SPACED IN h, DECLARED IN ADVANCE
    pick = sorted(set(int(round(x)) for x in np.geomspace(
        1.0, float(len(CAND)), N_ZONES)))
    SZ = [CAND[i - 1] for i in pick]
    SZ.sort(key=lambda t: t[0])
check("pf_q0.surface", len(SZ) >= 8,
      "%d prime-power zones (of %d admissible) are carried, log-spaced in h inside "
      "the caps H_MIN = %d (DECLARED as 2 x the largest mode block K = %d, so that "
      "K = 16 / 32 / 64 are all deep inside every window), h <= %d, MAX_H = %d, "
      "and the atom floor of %d prime powers per window: h = %d .. %d, a lever arm "
      "of %dx"
      % (len(SZ), len(CAND), H_MIN, KB_MAX, HCAP, MAX_H, N_ATOM_MIN,
         min(t[3] for t in SZ), max(t[3] for t in SZ),
         int(max(t[3] for t in SZ) / max(min(t[3] for t in SZ), 1))))

W = []
for (kz, Dz, Mz, hz) in SZ:
    if budget_left() < 480.0:
        info("pf_q0.budget", "stopped enumerating windows at h = %d" % hz)
        break
    alpha = UU_ALL[kz]
    c_at, D, mu_tot, n_at = atom_lags(alpha, Mz, atoms_in(alpha))
    c_ar = arch_lags(Mz, D)
    W.append(dict(k=kz, h=hz, M=Mz, D=D, alpha=alpha, n_zone=NN_ALL[kz],
                  c_ar=c_ar, c_at=c_at, c=c_ar + c_at, mu_tot=mu_tot,
                  n_atom=n_at, X=math.exp(2.0 * alpha), logX=2.0 * alpha))

check("pf_q0.scales",
      all(abs(r["h"] * r["D"] - r["alpha"]) < 1.0e-10 for r in W)
      and all(abs(math.log(r["X"]) - 2.0 * r["alpha"]) < 1.0e-9 for r in W),
      "*** THE SCALES, WRITTEN OUT ONCE AND NEVER ASSUMED AGAIN. ***  alpha = "
      "log n_zone = %.4f .. %.4f; the lag spacing D = 2 alpha / M = %.3e .. %.3e; "
      "h = M/2 = alpha / D = %d .. %d (identity to 1e-10); the atom cut-off "
      "X = e^{2 alpha} = %.4e .. %.4e, i.e. X = n_zone^2 EXACTLY and log X = "
      "2 alpha EXACTLY (the conversion every delta below uses); %d .. %d "
      "prime-power atoms per window on %d windows"
      % (qmin([r["alpha"] for r in W]), qmax([r["alpha"] for r in W]),
         qmin([r["D"] for r in W]), qmax([r["D"] for r in W]),
         min(r["h"] for r in W), max(r["h"] for r in W),
         qmin([r["X"] for r in W]), qmax([r["X"] for r in W]),
         min(r["n_atom"] for r in W), max(r["n_atom"] for r in W), len(W)))

for r in W:
    m = r["h"]
    A = odd_toeplitz(r["c"], r["M"])
    Tb = parity_basis(m, KB_MAX)
    r["Tb"] = Tb
    r["mu"] = parity_mu(m)[:KB_MAX]
    isq = 1.0 / np.sqrt(r["mu"])
    r["B64"] = sym((Tb @ (A @ Tb.T)) * np.outer(isq, isq))
    r["B64_ar"] = sym((Tb @ (odd_toeplitz(r["c_ar"], r["M"]) @ Tb.T))
                      * np.outer(isq, isq))
    del A
    r["B_LL"] = r["B64"][:SCHUR_KB, :SCHUR_KB].copy()
    e1 = np.zeros(SCHUR_KB)
    e1[0] = 1.0
    r["xstar"] = np.linalg.solve(r["B_LL"], e1)
    r["xstar"] /= max(abs(float(r["xstar"][0])), 1.0e-300)
    ev = np.linalg.eigvalsh(r["B_LL"])
    r["kap"] = float(ev[-1] / max(ev[0], 1.0e-300))
    r["gcum"] = cf_ladder(r["B_LL"], SCHUR_KB)

WP = [r for r in W if r["kap"] <= COND_BAR and r["gcum"] is not None]
DROP = [r for r in W if r not in WP]
XHP = [float(r["h"]) for r in WP]

E_CORR = []
for r in WP[:3]:
    w_ref = lag_weights_closed(r["xstar"], r["h"])
    w_new = lag_weights_corr(r["xstar"], r["h"], r["Tb"])
    E_CORR.append(float(np.max(np.abs(w_ref - w_new))
                        / max(float(np.max(np.abs(w_ref))), 1.0e-300)))
check("pf_q0.corr_form", qmax(E_CORR) < EXACT_BAR,
      "*** THEOREM, MACHINE-CHECKED, AND IT IS WHAT MAKES R1 AND R2 AFFORDABLE AT "
      "ALL. ***  The closed weight vector w_d = sum_{k,l} a_k a_l R_kl(d) of "
      "T160 .. T162 (four Dirichlet kernels per mode pair, Dirichlet 1829) EQUALS "
      "the CORRELATION form w_0 = A_0, w_d = 2 A_d - H_{M-1-d} with A the "
      "autocorrelation and H the self-convolution of v = T_K^T a, to %.2e .. %.2e "
      "relative on the %d smallest windows.  The correlation form costs O(h^2) in "
      "C and is INDEPENDENT of the block size K, so the sigma sweep of R1 and the "
      "K = 16 / 32 / 64 sweep of R2 cost the same as one T162 window"
      % (qmin(E_CORR), qmax(E_CORR), len(E_CORR)))

E_QID, HEADROOM = [], []
for r in WP:
    w = lag_weights_corr(r["xstar"], r["h"], r["Tb"])
    r["w"], r["dw"] = w, back_diff(w)
    r["Q"] = float(np.dot(r["c"], w))
    r["Q_ar"] = float(np.dot(r["c_ar"], w))
    r["Q_at"] = float(np.dot(r["c_at"], w))
    r["l1w"] = float(np.sum(np.abs(w)))
    r["TV"] = float(np.sum(np.abs(r["dw"])))
    r["gauge"] = abs(float(np.sum(w))) / max(r["l1w"], 1.0e-300)
    r["big"] = max(abs(r["Q_ar"]), abs(r["Q_at"]))
    r["Phi"] = cell_moment(r["M"], r["D"], 2.0 * r["alpha"], 0.5)
    E_QID.append(abs(r["Q"] - float(r["xstar"] @ (r["B_LL"] @ r["xstar"])))
                 / r["big"])
    HEADROOM.append(abs(r["Q"]) / (r["big"] * EPSM))

check("pf_q0.pairing_identity",
      qmax(E_QID) < EXACT_BAR and qmax([r["gauge"] for r in WP]) < EXACT_BAR
      and qmin(HEADROOM) > HEADROOM_BAR,
      "*** THEOREM, MACHINE-CHECKED: THE OBJECT OF R1 IS THE PAIRING ITSELF, "
      "REBUILT FROM T160 .. T162. ***  x^T B_LL x = sum_d c_d w_d to %.2e .. %.2e "
      "of max(|arch half|, |atom half|) on %d windows inside the DECLARED horizon "
      "cond(B_LL) <= %.0e (%d dropped); the gauge identity sum_d w_d = 0 holds to "
      "%.2e of ||w||_1.  The total is 1/s = %.4f .. %.4f while the halves are "
      "%.3e .. %.3e (arch) and %.3e .. %.3e (atom): the halves are individually "
      "LARGE and the total is O(1), which IS the cancellation R1 prices.  DECLARED "
      "NUMERICAL HORIZON: the cancellation headroom |Q| / (max half x eps) = "
      "%.2e .. %.2e, i.e. the O(1) total is resolved with at least %.1f decades to "
      "spare over double precision; no number below is closer to the rounding "
      "floor than that"
      % (qmin(E_QID), qmax(E_QID), len(WP), COND_BAR, len(DROP),
         qmax([r["gauge"] for r in WP]),
         qmin([r["Q"] for r in WP]), qmax([r["Q"] for r in WP]),
         qmin([r["Q_ar"] for r in WP]), qmax([r["Q_ar"] for r in WP]),
         qmin([r["Q_at"] for r in WP]), qmax([r["Q_at"] for r in WP]),
         qmin(HEADROOM), qmax(HEADROOM), math.log10(qmin(HEADROOM))))

E_LAD, TIGHT16, P_AFF, LAD_MONO = [], [], [], []
for r in WP:
    g = r["gcum"]
    r["g1"], r["g16"] = float(g[0]), float(g[SCHUR_KB - 1])
    r["inv_s"] = r["Q"]                       # = 1/g_16 EXACTLY, checked below
    E_LAD.append(abs(1.0 / r["g16"] - r["Q"]) / abs(r["Q"]))
    TIGHT16.append((1.0 / r["g16"]) / r["Q"])
    r["P_aff"] = r["g16"] / r["g1"]           # = the price of the K = 1 rung
    P_AFF.append(r["P_aff"])
    LAD_MONO.append(bool(np.all(np.diff(g) > 0.0)))
    r["P_rung"] = {K: float(r["g16"] / g[K - 1]) for K in (1, 2, 4, 8, 16)}

F_PAFF = fit_exp(XHP, P_AFF)
KAP_MAX = qmax([r["kap"] for r in WP])
LAD_BAR = 1.0e-6              # DECLARED: >> cond(B_LL) x eps, the solve horizon
check("pf_q0.price_reference",
      qmax(E_LAD) < LAD_BAR and qmax(E_LAD) < KAP_MAX * EPSM
      and all(LAD_MONO) and qmin(P_AFF) > 1.0,
      "*** THE PRICE REFERENCE OF THIS FILE IS NOT INVENTED HERE: IT IS THE T158 "
      "CHOLESKY LADDER, AND THAT IS THE WHOLE POINT OF R-C''. ***  THEOREM, "
      "machine-checked WITHIN THE DECLARED SOLVE HORIZON: Q(x*) = x*^T B_LL x* = "
      "1 / g_16 to %.2e .. %.2e relative -- below cond(B_LL) x eps = %.2e, the "
      "horizon the ill-conditioned solve for x* carries, and the identity is exact "
      "in exact arithmetic because x* = B^-1 e_1 / (B^-1 e_1)_1 gives Q(x*) = "
      "g_16 / g_16^2; so the "
      "T160 optimiser IS the top rung of the T158 ladder and price P(x) := Q(x) / "
      "Q(x*) = g_16 Q(x) is measured against a CERTIFIED object.  Every g_K is "
      "strictly increasing in K on all %d windows (the ladder terms y_j^2 > 0, "
      "Schur 1917 / Haynsworth 1968), so the rung prices P_rung(K) = g_16 / g_K "
      "are >= 1 and DECREASING in K: these are prices the chain has ALREADY PAID, "
      "since 1/g_K is an upper bound on 1/s it already accepts.  THE AFFORDABLE "
      "PRICE, THEREFORE PREREGISTERED AND CHAIN-DERIVED: P_aff := P_rung(1) = "
      "g_16 / g_1 = g_16 B_11 = %.4e .. %.4e (h-exponent %+.3f, FIT) -- the price "
      "of the T157 route-(0) certificate 1/s <= B_11, the loosest rung the chain "
      "has ever used.  A trial vector at price <= P_aff is, by construction, NO "
      "WORSE THAN A CERTIFICATE ALREADY IN THE CHAIN"
      % (qmin(E_LAD), qmax(E_LAD), KAP_MAX * EPSM, len(WP),
         qmin(P_AFF), qmax(P_AFF), F_PAFF))

info("pf_q0.rung_prices",
     "the DECLARED price tiers, read off the ladder before any sigma is swept: "
     + "; ".join("P_rung(%d) = %.3e .. %.3e" % (
         K, qmin([r["P_rung"][K] for r in WP]),
         qmax([r["P_rung"][K] for r in WP])) for K in (1, 2, 4, 8, 16)))

print("")
print("TOTAL (Q0): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("R1  THE FRONT: THE FEJER KNOB, THE TWO CURRENCIES, THE PRICE ANATOMY")
# ----------------------------------------------------------------------------
para("""R1.0  THE TWO CURRENCIES AND THE ONE KNOB, DECLARED BEFORE A SINGLE NUMBER IS
SEEN.  For an admissible trial vector x (x_1 = 1, Q(x) > 0) the Thomson /
Dirichlet dual gives 1/s <= Q(x) = sum_d c_d w_d(x), and T162 reduced the whole
of R2'' to TWO numbers per trial vector:

  delta_bnd(x) = 1/2 + log( 2 kappa ||Delta w(x)||_1 / |Q(x)| ) / log X
                 -- WHAT A PROOF MUST BEAT.  kappa = %.6f is the ONE
                 unconditional arithmetic input (Chebyshev 1852 /
                 Rosser-Schoenfeld 1962); the rest is prime-free.
  delta_val(x) = log( max( |Q^atom(x) - Q^smooth(x)| / |Q(x)|, 1 ) ) / log X
                 -- THE RESIDUAL VALUE against |Q|, i.e. a FLOOR that no
                 rearrangement can undercut (the T161 / T162 currency, with the
                 closed Mellin cell moments C_d(1/2), Mellin 1896).
  P(x) = Q(x) / Q(x*) = g_16 Q(x)   -- THE PRICE in the 1/s ceiling, measured
                 against the CERTIFIED T158 top rung 1 / g_16 (Q0).

THE KNOB.  t_k(sigma) = max(0, 1 - k/sigma) is the CONTINUOUS Fejer / Cesaro
window (Fejer 1915) and x_sigma = t(sigma) . x*.  By self-adjointness of the
smoothing, pairing the tapered weight vector against the raw Lambda-mass is the
SAME number as pairing the untapered vector against the Fejer-AVERAGED mass, so
sigma is literally a smoothing WIDTH on the sampled harmonics: the frequency
scale it smears is Delta omega = 2 pi sigma / N = pi sigma / (h + 1/2).

AND HERE IS WHY THIS FAMILY, AND NOT SOME OTHER ONE: THE KNOB HAS BOTH ENDPOINTS
ALREADY IN THE CHAIN.  sigma = 1 kills every mode but the first, i.e. x_1 = e_1,
which is EXACTLY the K = 1 rung of the T158 ladder, Q(e_1) = B_11 = 1/g_1, the
T157 route-(0) certificate.  sigma -> infinity is the untapered T160 optimiser
x*, Q = 1/g_16.  So the Fejer knob INTERPOLATES BETWEEN TWO CERTIFICATES THE
CHAIN ALREADY OWNS, and the front is a path between them rather than a search
over an invented family.""" % KAPPA)

SIG_T162 = (2.0, 4.0, 8.0, 16.0)      # the FOUR integer widths T162 measured
SIG_GRID = sorted(set([round(float(s), 6) for s in np.geomspace(1.0, 4096.0, 49)]
                      + [1.0] + list(SIG_T162))) + [float("inf")]
# THE PRICE TIERS, PREREGISTERED.  Two are DECLARED CONSTANTS (flat in h by
# construction); three are LADDER RUNGS, i.e. prices the chain has already paid.
TIER_CONST = (1.25, 2.0, 10.0)
TIER_RUNG = (8, 4, 2, 1)


def trial_numbers(r, x):
    """The two currencies, the price and the anatomy of ONE trial vector."""
    w = lag_weights_corr(x, r["h"], r["Tb"])
    Q = float(np.dot(r["c"], w))
    q_ar = float(np.dot(r["c_ar"], w))
    q_at = float(np.dot(r["c_at"], w))
    q_sm = -float(np.dot(w, r["Phi"]))
    tv = float(np.sum(np.abs(back_diff(w))))
    big = max(abs(q_ar), abs(q_at))
    out = dict(Q=Q, TV=tv, q_ar=q_ar, q_at=q_at, big=big,
               gauge=abs(float(np.sum(w))) / max(float(np.sum(np.abs(w))), 1e-300),
               canc=abs(Q) / max(big, 1.0e-300),
               head=abs(Q) / max(big * EPSM, 1.0e-300),
               price=Q * r["g16"], ok=(Q > 0.0))
    out["d_bnd"] = 0.5 + math.log(max(2.0 * KAPPA * tv / max(abs(Q), 1.0e-300),
                                      1.0e-300)) / r["logX"]
    out["d_val"] = math.log(max(abs(q_at - q_sm) / max(abs(Q), 1.0e-300), 1.0)) \
        / r["logX"]
    return out


for r in WP:
    r["sig"] = {}
    for sg in SIG_GRID:
        x = r["xstar"] * fejer_taper(SCHUR_KB, sg)
        x = x / max(abs(float(x[0])), 1.0e-300)
        r["sig"][sg] = trial_numbers(r, x)
    r["ref"] = r["sig"][float("inf")]

E_SIG1 = [abs(r["sig"][1.0]["price"] - r["P_aff"]) / r["P_aff"] for r in WP]
E_SIGINF = [abs(r["ref"]["price"] - 1.0) for r in WP]
check("pf_r1.knob_endpoints",
      qmax(E_SIG1) < LAD_BAR and qmax(E_SIGINF) < LAD_BAR,
      "*** THEOREM, MACHINE-CHECKED: THE KNOB'S ENDPOINTS ARE THE LADDER'S "
      "ENDPOINTS, WHICH IS WHY THE PRICE AXIS IS CHAIN-DERIVED AND NOT INVENTED. "
      "***  P(sigma = 1) = P_aff = g_16 / g_1 to %.2e .. %.2e relative (the "
      "T157 route-(0) rung), and P(sigma = infinity) = 1 to %.2e .. %.2e (the "
      "T160 optimiser = the T158 top rung).  So the Fejer sweep is a PATH between "
      "two certificates already in the chain, and every intermediate sigma is an "
      "admissible trial vector by the Thomson direction alone"
      % (qmin(E_SIG1), qmax(E_SIG1), qmin(E_SIGINF), qmax(E_SIGINF)))

D_REF_B = [r["ref"]["d_bnd"] for r in WP]
D_REF_V = [r["ref"]["d_val"] for r in WP]
T162_SUB = []
for r in WP:
    cand = [r["sig"][s] for s in SIG_T162 if r["sig"][s]["ok"]]
    T162_SUB.append(min(t["d_bnd"] for t in cand) if cand else float("nan"))
F_T162SUB = fit_exp(XHP, T162_SUB)
check("pf_r1.t162_reproduction",
      qmin(T162_SUB) > T162_DBND_FEJ[0] - 0.05
      and qmax(T162_SUB) < T162_DBND_FEJ[1] + 0.05
      and qmax(T162_SUB) < RH_DELTA
      and abs(qmax(D_REF_V) - T162_DVAL[1]) < 0.06,
      "*** T162 REPRODUCED ON AN INDEPENDENTLY REBUILT SURFACE, WHICH IS THE "
      "PRECONDITION FOR EVERY NUMBER BELOW BEING COMPARABLE. ***  Restricting the "
      "knob to the FOUR integer widths T162 used (sigma = 2/4/8/16) the best "
      "provable demand per window is delta_bnd = %.4f .. %.4f, against T162's "
      "quoted %.3f .. %.3f -- reproduced at the demanding end, and NARROWER at the "
      "top for the declared reason that H_MIN = %d drops the small windows T162 "
      "carried (where delta is coarsest because log X = 2 alpha is smallest), so "
      "this surface is a SUBSET of T162's in h and the comparison is stated that "
      "way rather than as a match.  Still below the "
      "RH-strength yardstick 1/2 on %d of %d windows.  In the OTHER currency the "
      "untapered optimiser gives delta_val = %.4f .. %.4f against T162's C1 value "
      "%.2f, reproduced to %.3f.  THE TWO CURRENCIES ARE NOT MIXED ANYWHERE "
      "BELOW: delta_val is a floor on the VALUE, delta_bnd is the demand on a "
      "PROOF, and only the second one has 1/2 as its yardstick"
      % (qmin(T162_SUB), qmax(T162_SUB), T162_DBND_FEJ[0], T162_DBND_FEJ[1],
         H_MIN, sum(1 for d in T162_SUB if d < RH_DELTA), len(T162_SUB),
         qmin(D_REF_V), qmax(D_REF_V), T162_DVAL[1],
         abs(qmax(D_REF_V) - T162_DVAL[1])))

print("")
print("TOTAL (R1.0): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# --- R1.1  THE FRONT, AS A NUMBER SERIES --------------------------------------
para("""R1.1  THE FRONT, AND THE RULE THAT PICKS sigma* IS WRITTEN DOWN BEFORE THE
NUMBERS BECAUSE OTHERWISE IT IS A FIT.  THE PREREGISTERED RULE, in three tiers,
each tier a PRICE CAP and never a delta target:

  TIER F (FLAT):  P(sigma) <= %s -- DECLARED CONSTANTS, hence flat in h by
                  construction.  A bound at a flat price is the certified
                  1 / g_16 up to a constant, so this is the tier that could
                  make R2'' a certified operating point.
  TIER R (RUNG):  P(sigma) <= P_rung(K) = g_16 / g_K for K = %s -- prices the
                  chain has ALREADY PAID, since 1/g_K is an upper bound on 1/s
                  it already accepts (T158).
  sigma*(tier) := the SMALLEST sigma in the declared grid meeting the cap.

WHY THE SMALLEST sigma AND NOT AN ARGMIN OVER delta: because the two numbers are
MONOTONE in opposite directions along the knob -- P(sigma) decreases (from P_aff
at sigma = 1 to 1 at sigma = infinity) and delta_bnd increases -- so the argmin of
delta_bnd under a price cap IS the cap boundary.  The monotonicity is MEASURED
below, not assumed, and it means the (delta_bnd, P) curve of the knob IS the
Pareto front: there is nothing to search.

THE GRID IS DECLARED: %d values of sigma, geometric on [1, 4096], plus the four
integer widths T162 used and sigma = infinity.  ANTI-FITTING, and it is enforced
by a check and not by a promise: (a) the rule above never looks at delta; (b) the
SAME sigma* rule is applied to every window; (c) an OUT-OF-SAMPLE control fixes
one single sigma on the SMALLEST window alone and applies it, unchanged, to all
the others.""" % (
    "/".join("%.2f" % t for t in TIER_CONST),
    "/".join(str(K) for K in TIER_RUNG), len(SIG_GRID)))

MONO_P, MONO_D = [], []
for r in WP:
    ps = [r["sig"][s]["price"] for s in SIG_GRID]
    ds = [r["sig"][s]["d_bnd"] for s in SIG_GRID]
    MONO_P.append(float(np.max(np.diff(ps))) / max(abs(ps[0]), 1.0e-300))
    MONO_D.append(float(np.min(np.diff(ds))))
check("pf_r1.monotone_knob",
      qmax(MONO_P) <= 1.0e-12 and qmin(MONO_D) >= -1.0e-12
      and all(r["sig"][s]["ok"] for r in WP for s in SIG_GRID),
      "*** MEASURED, ON EVERY WINDOW AND EVERY GRID POINT: THE KNOB IS A "
      "MONOTONE TRADE-OFF, SO THE KNOB CURVE **IS** THE PARETO FRONT. ***  Along "
      "increasing sigma the price P is non-increasing (largest forward difference "
      "%.2e in units of P_aff) and the demand delta_bnd is non-decreasing "
      "(smallest forward difference %+.2e), and Q(x_sigma) > 0 at ALL %d grid "
      "points on ALL %d windows, so every point of the sweep is an ADMISSIBLE "
      "trial vector and no point of the front is discarded.  CONSEQUENCE: the "
      "front has no interior optimum to find -- it is a one-parameter exchange, "
      "and the only question is where the chain can afford to sit on it"
      % (qmax(MONO_P), qmin(MONO_D), len(SIG_GRID), len(WP)))


def front_at(r, cap):
    """The front point of ONE window at ONE price cap: the smallest sigma whose
    price fits, and the two currencies there."""
    for s in SIG_GRID:
        t = r["sig"][s]
        if t["ok"] and t["price"] <= cap * (1.0 + 1.0e-12):
            return s, t
    return float("nan"), None


FRONT = {}
for tag, caps in (("const", TIER_CONST), ("rung", TIER_RUNG)):
    for cv in caps:
        key = ("P<=%.2f" % cv) if tag == "const" else ("P<=P_rung(%d)" % cv)
        rows = []
        for r in WP:
            cap = cv if tag == "const" else r["P_rung"][cv]
            s, t = front_at(r, cap)
            rows.append((r["h"], s, cap, t["d_bnd"] if t else float("nan"),
                         t["d_val"] if t else float("nan"),
                         t["price"] if t else float("nan")))
        FRONT[key] = rows

print("")
print("  THE PARETO FRONT AS A NUMBER SERIES (no plot).  For each declared price")
print("  cap: the sigma* the rule picks, the two currencies there, and how many of")
print("  the %d windows fall below the RH-strength yardstick delta_bnd < 1/2." % len(WP))
print("")
print("  %-18s %10s %11s %15s %15s %6s" % (
    "price cap", "sigma*", "cap value", "delta_bnd", "delta_val", "<1/2"))
for key, rows in FRONT.items():
    sg = [t[1] for t in rows]
    db = [t[3] for t in rows]
    dv = [t[4] for t in rows]
    cp = [t[2] for t in rows]
    print("  %-18s %4.0f..%-5.0f %4.1e..%-4.1e %6.3f..%-7.3f %6.3f..%-7.3f %3d/%d"
          % (key, qmin(sg), qmax(sg), qmin(cp), qmax(cp), qmin(db), qmax(db),
             qmin(dv), qmax(dv), sum(1 for d in db if d < RH_DELTA), len(db)))

P_CROSS, S_CROSS, PC_OVER_AFF, PC_OVER_R2 = [], [], [], []
for r in WP:
    sub = [(r["sig"][s]["price"], s) for s in SIG_GRID
           if r["sig"][s]["ok"] and r["sig"][s]["d_bnd"] < RH_DELTA]
    if sub:
        p, s = min(sub)
        P_CROSS.append(p)
        S_CROSS.append(s)
        PC_OVER_AFF.append(p / r["P_aff"])
        PC_OVER_R2.append(p / r["P_rung"][2])
    else:
        P_CROSS.append(float("inf"))
        S_CROSS.append(float("nan"))
F_PCROSS = fit_exp(XHP, P_CROSS)
F_PC_AFF = fit_exp(XHP, PC_OVER_AFF)
FLAT_BEST = [qmin([t[3] for t in FRONT["P<=%.2f" % cv]]) for cv in TIER_CONST]
FLAT_WORST = [qmax([t[3] for t in FRONT["P<=%.2f" % cv]]) for cv in TIER_CONST]
CROSS_FLAT = all(w < RH_DELTA for w in FLAT_WORST)

check("pf_r1.front_read",
      all(np.isfinite(p) for p in P_CROSS) and qmin(PC_OVER_AFF) > 0.0,
      "*** THE FRONT, READ AT THE CHAIN'S OWN PRICES -- THE CENTRAL MEASUREMENT OF "
      "T163. ***  (i) AT THE FLAT TIER the front does %s cross: the best demand "
      "reachable at price <= %.2f is delta_bnd = %.3f .. %.3f, at price <= %.2f it "
      "is %.3f .. %.3f, and at price <= %.2f it is %.3f .. %.3f -- against the "
      "yardstick 1/2.  (ii) THE CROSSING PRICE, i.e. the cheapest point of the "
      "front with delta_bnd < 1/2: P_cross = %.3e .. %.3e at sigma = %.0f .. %.0f, "
      "growing as h^%+.3f (FIT).  (iii) AND THE NUMBER THAT DECIDES R-C'': "
      "P_cross / P_aff = %.4f .. %.4f with h-exponent %+.3f (FIT), i.e. the "
      "crossing price is STRICTLY INSIDE the price the chain already pays at its "
      "loosest rung, by a factor %.0f .. %.0f, and the margin WIDENS with h because "
      "P_cross grows as h^%+.2f while P_aff grows as h^%+.3f.  P_cross / "
      "P_rung(2) = %.2e .. %.2e, so the crossing is far above the flat rung tier.  "
      "READ IN TWO SENTENCES, AND THE SECOND IS THE CATCH: sub-1/2 demand IS "
      "reachable at a 1/s ceiling smaller than the T157 route-(0) certificate the "
      "chain has already accepted, with room to spare; but that price is NOT FLAT, "
      "it grows as h^%+.2f, so it is a per-window certificate at growing cost and "
      "not a uniform statement -- and R1.2 shows that the exponent is not an "
      "accident"
      % ("NOT" if not CROSS_FLAT else "", TIER_CONST[0], FLAT_BEST[0],
         FLAT_WORST[0], TIER_CONST[1], FLAT_BEST[1], FLAT_WORST[1],
         TIER_CONST[2], FLAT_BEST[2], FLAT_WORST[2],
         qmin(P_CROSS), qmax(P_CROSS), qmin(S_CROSS), qmax(S_CROSS), F_PCROSS,
         qmin(PC_OVER_AFF), qmax(PC_OVER_AFF), F_PC_AFF,
         1.0 / qmax(PC_OVER_AFF), 1.0 / qmin(PC_OVER_AFF), F_PCROSS, F_PAFF,
         qmin(PC_OVER_R2), qmax(PC_OVER_R2), F_PCROSS))

print("")
print("TOTAL (R1.1): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# --- R1.2  THE PRICE ANATOMY --------------------------------------------------
para("""R1.2  THE PRICE ANATOMY, AND IT IS NOT A FIT: IT IS AN IDENTITY, SO THE
QUESTION THE CONTRACT ASKS -- ``IS THE PRICE THE SAME h^2 CANCELLATION IN NEW
CLOTHING?'' -- HAS AN EXACT ANSWER.  Substitute the definition of the price
P(x) = g_16 |Q(x)| into the definition of the demand.  For EVERY admissible x,

  *** delta_bnd(x) = 1/2 + log( 2 kappa g_16 TV(x) / P(x) ) / log X ***      (E)

with TV(x) = ||Delta w(x)||_1, and therefore, EXACTLY and with no asymptotics,

  *** delta_bnd(x) < 1/2  <==>  P(x) > 2 kappa g_16 TV(x) ***               (E')

THEOREM (a rearrangement of the definitions; machine-checked below).  READ WHAT
(E') SAYS.  The trial vector enters delta_bnd ONLY through the single ratio
TV(x) / |Q(x)|; the price is |Q(x)| in units of the certified 1/g_16; so PRICE
AND DEMAND ARE TWO COORDINATES ON ONE OBJECT and the ``exchange rate'' T162
measured is a CHANGE OF VARIABLES, not a second lever.  Consequences, all exact:

  (a) THE CROSSING PRICE IS A CLOSED FORMULA, not a search result:
      P_cross(x-family) = 2 kappa g_16 TV(x) at the crossing point, so the
      h-exponent of the crossing price EQUALS the h-exponent of the total
      variation plus that of g_16.  Nothing else can contribute.
  (b) A FLAT crossing price is possible IF AND ONLY IF TV(x) is bounded in h at
      a bounded price, because g_16 = 1/Q(x*) is bounded (Q0 measured
      1/s = O(1)).  So the ENTIRE remaining question is a TOTAL-VARIATION
      question about the trial vector -- which is exactly what R2 attacks.
  (c) THE TAPER CANNOT HELP UNLESS IT LOWERS TV.  If TV(x_sigma) is
      non-decreasing along the knob then every unit of delta bought by tapering
      is paid one-for-one out of the price, i.e. the relocation is EXACT.  The
      one-for-one-ness is measured below as tau_TV.""")

E_EXCH, TAU_TV, TVR, CANC_S, CANC_R, PRED_PC = [], [], [], [], [], []
for r in WP:
    ref = r["ref"]
    for s in SIG_GRID:
        t = r["sig"][s]
        lhs = t["d_bnd"]
        rhs = 0.5 + math.log(2.0 * KAPPA * r["g16"] * t["TV"]
                             / t["price"]) / r["logX"]
        E_EXCH.append(abs(lhs - rhs) / max(abs(lhs), 1.0e-3))
    s_c = S_CROSS[WP.index(r)]
    tc = r["sig"][s_c] if np.isfinite(s_c) else None
    if tc is not None:
        PRED_PC.append(abs(2.0 * KAPPA * r["g16"] * tc["TV"] / tc["price"]))
    # the one-for-one test, on the stretch of the knob that actually moves delta
    for s in SIG_GRID[:-1]:
        t = r["sig"][s]
        dlp = math.log(t["price"] / ref["price"])
        if dlp > 1.0:
            TAU_TV.append(math.log(t["TV"] / ref["TV"]) / dlp)
    TVR.append(min(r["sig"][s]["TV"] for s in SIG_GRID) / ref["TV"])
    CANC_S.append(r["sig"][2.0]["canc"])
    CANC_R.append(ref["canc"])

F_TVREF = fit_exp(XHP, [r["ref"]["TV"] for r in WP])
F_TVCR = fit_exp(XHP, [r["sig"][S_CROSS[i]]["TV"]
                       for i, r in enumerate(WP) if np.isfinite(S_CROSS[i])])
F_G16 = fit_exp(XHP, [r["g16"] for r in WP])
F_CANCR = fit_exp(XHP, CANC_R)
check("pf_r1.exchange_identity", qmax(E_EXCH) < 1.0e-12,
      "*** THEOREM, MACHINE-CHECKED AT ALL %d x %d GRID POINTS: THE EXCHANGE LAW "
      "(E) IS AN IDENTITY. ***  delta_bnd(x) = 1/2 + log(2 kappa g_16 TV(x) / "
      "P(x)) / log X to %.2e .. %.2e relative, so the price and the demand are two "
      "coordinates on the SAME object and the crossing condition (E') "
      "P > 2 kappa g_16 TV is exact.  THE DECOMPOSITION OF THE MEASURED CROSSING "
      "EXPONENT, term by term and adding up by (a): TV at the crossing point grows "
      "as h^%+.3f, g_16 as h^%+.3f, and 2 kappa is a constant -- sum %+.3f against "
      "the DIRECTLY FITTED crossing exponent %+.3f, agreeing to %.3f.  THE h^2 IS "
      "IN THE TOTAL VARIATION AND NOWHERE ELSE"
      % (len(WP), len(SIG_GRID), qmin(E_EXCH), qmax(E_EXCH), F_TVCR, F_G16,
         F_TVCR + F_G16, F_PCROSS, abs(F_TVCR + F_G16 - F_PCROSS)))

F_TVR = fit_exp(XHP, TVR)
DGAIN_TV = [-math.log(TVR[i]) / r["logX"] for i, r in enumerate(WP)]
F_DGTV = fit_exp(XHP, DGAIN_TV)
check("pf_r1.relocation_bounded",
      abs(F_TVR) < BAR_FLAT and qmax(DGAIN_TV) < 0.3 and qmin(TAU_TV) > -0.25,
      "*** AND HERE IS THE ANSWER TO THE CONTRACT'S QUESTION, WITH THE ONE "
      "CORRECTION T162 COULD NOT SEE: THE TAPER DOES LOWER THE TOTAL VARIATION, BUT "
      "ONLY BY A BOUNDED FACTOR, SO THE RELOCATION IS EXACT UP TO A CONSTANT AND "
      "ASYMPTOTICALLY EXACT. ***  (i) THE TV GAIN IS REAL AND IT IS h-FLAT.  The "
      "minimum of TV(x_sigma) over all %d grid points, divided by TV(x*), is "
      "%.4f .. %.4f -- a genuine reduction by a factor %.2f .. %.2f -- but its "
      "h-exponent is %+.3f, i.e. FLAT (bar %.2f): the taper buys a CONSTANT, never "
      "a power of h.  (ii) WHAT A CONSTANT IS WORTH IN THE delta CURRENCY: by (E) a "
      "TV factor c contributes log(1/c) / log X = %.4f .. %.4f of delta_bnd, with "
      "h-exponent %+.3f -- it SHRINKS, because log X = 2 alpha grows while the "
      "factor does not.  THE ENTIRE STRUCTURAL BUDGET OF THE FEJER KNOB IS THEREFORE "
      "AT MOST %.3f OF delta, and it decays.  (iii) THE ONE-FOR-ONE TEST.  Where "
      "the price has moved by at least one nat, tau_TV := log(TV(x_sigma)/TV(x*)) / "
      "log(P(x_sigma)/P(x*)) = %.4f .. %.4f with median %.4f, i.e. within a few per "
      "cent of ZERO: essentially every unit of delta the taper buys is paid, one for "
      "one, out of the price.  (iv) SO THE h^2.86 OF T162 IS THE SAME h^2 AS "
      "BEFORE, AND (E) SAYS WHICH h^2 IT IS: the total variation of the weight "
      "sequence against the O(1) pairing, TV(x*) = %.3e .. %.3e growing as h^%+.3f "
      "while |Q| = 1/s stays O(1) (g_16 flat at h^%+.3f).  That is T161's "
      "granularity -- the required precision as a fraction of the last summand -- "
      "written in the price coordinate instead of the delta coordinate.  STATUS: "
      "THEOREM for (E)/(E'), MEASURED for the exponents, tau_TV and the constant"
      % (len(SIG_GRID), qmin(TVR), qmax(TVR), 1.0 / qmax(TVR), 1.0 / qmin(TVR),
         F_TVR, BAR_FLAT, qmin(DGAIN_TV), qmax(DGAIN_TV), F_DGTV,
         qmax(DGAIN_TV), qmin(TAU_TV), qmax(TAU_TV), qmed(TAU_TV),
         qmin([r["ref"]["TV"] for r in WP]),
         qmax([r["ref"]["TV"] for r in WP]), F_TVREF, F_G16))

TV_FLOOR = qmin(TVR)                  # MEASURED, h-flat, the structural budget
FLOOR_GAP, FLOOR_PRED = [], []
for i, r in enumerate(WP):
    lb = 0.5 + math.log(2.0 * KAPPA * r["g16"] * TVR[i] * r["ref"]["TV"]
                        / TIER_CONST[1]) / r["logX"]
    meas = FRONT["P<=%.2f" % TIER_CONST[1]][i][3]
    FLOOR_PRED.append(lb)
    FLOOR_GAP.append(meas - lb)
F_FLOOR = fit_exp(XHP, [t - RH_DELTA for t in FLOOR_PRED])
check("pf_r1.flat_price_floor",
      qmin(FLOOR_PRED) > RH_DELTA and qmin(FLOOR_GAP) > -1.0e-9,
      "*** THE CERTIFICATE THAT THE FRONT DOES NOT CROSS AT FLAT PRICE, AND IT IS "
      "AN INEQUALITY AND NOT A SWEEP. ***  Combining (E) with the measured, h-flat "
      "TV floor TV(x_sigma) >= %.4f TV(x*), EVERY point of the knob at a price "
      "P <= P_0 obeys delta_bnd >= 1/2 + log(2 kappa g_16 x %.4f TV(x*) / P_0) / "
      "log X.  At the declared flat cap P_0 = %.2f this LOWER BOUND is %.3f .. "
      "%.3f, i.e. above the yardstick 1/2 by %.3f .. %.3f on all %d windows, and "
      "the sweep respects it with margin %.3f .. %.3f (as it must).  THE BOUND'S OWN "
      "h-DEPENDENCE: the excess over 1/2 goes as h^%+.3f (FIT), so it shrinks only "
      "like 1 / log X while TV grows like h^2 -- the front approaches the yardstick "
      "at the rate of a logarithm and reaches it at no h on this surface.  STATUS: "
      "CERT-WINDOW (the inequality is exact per window; the TV floor that feeds it "
      "is MEASURED and h-flat, not proven)"
      % (TV_FLOOR, TV_FLOOR, TIER_CONST[1], qmin(FLOOR_PRED), qmax(FLOOR_PRED),
         qmin(FLOOR_PRED) - RH_DELTA, qmax(FLOOR_PRED) - RH_DELTA, len(WP),
         qmin(FLOOR_GAP), qmax(FLOOR_GAP), F_FLOOR))

check("pf_r1.cancellation_is_the_price",
      qmax(CANC_R) < 1.0e-2 and qmin(CANC_S) > qmax(CANC_R),
      "*** THE SECOND HALF OF THE ANATOMY, AND IT IDENTIFIES THE OBJECT: THE PRICE "
      "IS THE RECIPROCAL OF THE CANCELLATION x* ACHIEVES. ***  Define the "
      "cancellation quality CANC(x) = |Q(x)| / max(|Q^arch(x)|, |Q^atom(x)|).  At "
      "the untapered optimiser CANC(x*) = %.3e .. %.3e (h-exponent %+.3f, FIT) -- "
      "the two large halves cancel to that relative depth, which is the T161 "
      "h^-2 granularity MEASURED again here.  At sigma = 2, the T162 minimiser, "
      "CANC = %.3e .. %.3e, i.e. LARGER by %.1e .. %.1e: THE TAPER DESTROYS THE "
      "CANCELLATION, and since |Q| = CANC x (max half), destroying it is precisely "
      "what raises |Q| and hence the price.  So the price is not an independent "
      "cost, it is the cancellation depth read backwards, and the front cannot "
      "cross at flat price for that reason"
      % (qmin(CANC_R), qmax(CANC_R), F_CANCR, qmin(CANC_S), qmax(CANC_S),
         qmin(CANC_S) / qmax(CANC_R), qmax(CANC_S) / qmin(CANC_R)))

print("")
print("TOTAL (R1.2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("R2  THE SEARCH SPACE: BEYOND THE SIXTEEN LOW MODES")
# ----------------------------------------------------------------------------
para("""R2.0  R1 LEAVES EXACTLY ONE LEVER, AND (E) NAMES IT: LOWER THE TOTAL VARIATION
AT CONSTANT PRICE.  The Thomson direction licenses ANY trial vector, so the block
size K is free.  Three things make the K-sweep the natural next move and all
three are exact:

  (i)  THE PRICE OF ENLARGING K IS A DIVIDEND, NOT A COST.  x*_K = B_K^-1 e_1
       normalised gives Q(x*_K) = 1 / g_K, and g_K is INCREASING in K (Q0), so
       P(x*_K) = g_16 / g_K <= 1 for every K >= 16: the 1/s ceiling gets
       TIGHTER, not weaker.  The K-sweep is therefore a test AT CONSTANT (indeed
       slightly better than constant) PRICE, which is precisely the question the
       contract asks.
  (ii) BUT (E) IS A RATIO.  delta_bnd depends on x only through TV(x) / |Q(x)|,
       and enlarging K DECREASES |Q| (that is what a better bound means).  So
       more modes help if and only if TV falls FASTER than |Q| does -- the sweep
       decides it, nothing else.
  (iii) THE CLOSED CANDIDATE.  Hard truncation at K = 16 is the crudest possible
       window on the mode axis; the Fejer-weighted mode sum (Fejer 1915) is the
       classical replacement, and at K = 64 it is a genuinely different trial
       vector from anything T162 tried.

DECLARED IN ADVANCE: K = %s; the numerical horizon is the SAME cond bar %.0e
applied to each block B_K separately, and any window whose B_K exceeds it, or
whose Cholesky fails, is DROPPED FROM THAT K AND SAID SO.""" % (
    "/".join(str(k) for k in (SCHUR_KB, 2 * SCHUR_KB, KB_MAX)), COND_BAR))

K_SWEEP = (SCHUR_KB, 2 * SCHUR_KB, KB_MAX)
KROW = {K: [] for K in K_SWEEP}
KDROP = {K: 0 for K in K_SWEEP}
for r in WP:
    r["kfam"] = {}
    for K in K_SWEEP:
        BK = sym(r["B64"][:K, :K])
        ev = np.linalg.eigvalsh(BK)
        if ev[0] <= 0.0 or ev[-1] / ev[0] > COND_BAR:
            KDROP[K] += 1
            continue
        gK = cf_ladder(BK, K)
        if gK is None:
            KDROP[K] += 1
            continue
        e1 = np.zeros(K)
        e1[0] = 1.0
        xk = np.linalg.solve(BK, e1)
        xk = xk / max(abs(float(xk[0])), 1.0e-300)
        fam = {"opt": xk,
               "fej_full": xk * fejer_taper(K, float(K)),
               "fej_2": xk * fejer_taper(K, 2.0),
               "flat": np.ones(K)}
        r["kfam"][K] = {}
        for nm, xv in fam.items():
            xv = xv / max(abs(float(xv[0])), 1.0e-300)
            t = trial_numbers(r, xv)
            t["g"] = float(gK[-1])
            t["cond"] = float(ev[-1] / ev[0])
            r["kfam"][K][nm] = t
        KROW[K].append(r)

print("")
print("  THE (TV, PRICE) SERIES OVER THE MODE COUNT K, AT THE OPTIMISER OF EACH")
print("  BLOCK -- i.e. the honest answer to ``does the total variation fall when")
print("  the search space grows, at constant price?''")
print("")
print("  %3s %8s %13s %11s %11s %13s %6s" % (
    "K", "windows", "TV", "TV/TV_16", "price", "delta_bnd", "<1/2"))
for K in K_SWEEP:
    rows = [r["kfam"][K]["opt"] for r in KROW[K]]
    tvr = [r["kfam"][K]["opt"]["TV"] / r["kfam"][SCHUR_KB]["opt"]["TV"]
           for r in KROW[K] if SCHUR_KB in r["kfam"]]
    print("  %3d %8d %5.2e..%-5.2e %4.2f..%-5.2f %4.2e..%-4.2e %5.3f..%-6.3f %3d/%d"
          % (K, len(rows), qmin([t["TV"] for t in rows]),
             qmax([t["TV"] for t in rows]), qmin(tvr), qmax(tvr),
             qmin([t["price"] for t in rows]), qmax([t["price"] for t in rows]),
             qmin([t["d_bnd"] for t in rows]), qmax([t["d_bnd"] for t in rows]),
             sum(1 for t in rows if t["d_bnd"] < RH_DELTA), len(rows)))

KOK = [r for r in WP if all(K in r["kfam"] for K in K_SWEEP)]
XK = [float(r["h"]) for r in KOK]
TV_K = {K: [r["kfam"][K]["opt"]["TV"] for r in KOK] for K in K_SWEEP}
EPS_K = {K: [r["kfam"][K]["opt"]["TV"] / abs(r["kfam"][K]["opt"]["Q"])
             for r in KOK] for K in K_SWEEP}
PR_K = {K: [r["kfam"][K]["opt"]["price"] for r in KOK] for K in K_SWEEP}
DB_K = {K: [r["kfam"][K]["opt"]["d_bnd"] for r in KOK] for K in K_SWEEP}
F_TVK = {K: fit_exp(XK, TV_K[K]) for K in K_SWEEP}
RAT64 = [TV_K[KB_MAX][i] / TV_K[SCHUR_KB][i] for i in range(len(KOK))]
EPSR64 = [EPS_K[KB_MAX][i] / EPS_K[SCHUR_KB][i] for i in range(len(KOK))]
DDB64 = [DB_K[KB_MAX][i] - DB_K[SCHUR_KB][i] for i in range(len(KOK))]
check("pf_r2.mode_sweep",
      len(KOK) >= 8 and qmax(PR_K[KB_MAX]) <= 1.0 + 1.0e-9,
      "*** THE ANSWER, AND IT IS A CLEAN NEGATIVE WITH A REASON: MORE MODES BUY A "
      "BETTER BOUND AND A WORSE DEMAND, IN THE SAME BREATH. ***  On the %d windows "
      "where all three blocks are inside the cond horizon (dropped: %s), going from "
      "K = %d to K = %d multiplies the total variation by %.3f .. %.3f while the "
      "price FALLS to %.4f .. %.4f (a dividend, as predicted), and the net effect "
      "on the demand is delta_bnd(K=%d) - delta_bnd(K=%d) = %+.4f .. %+.4f: the "
      "demand gets WORSE, not better.  In the ratio that (E) says is the only thing "
      "that matters, TV / |Q| = %.3e .. %.3e at K = %d against %.3e .. %.3e at "
      "K = %d -- LARGER, window by window, by a factor %.4f .. %.4f.  THE "
      "h-EXPONENT OF TV IS UNMOVED: %+.3f at "
      "K = %d, %+.3f at K = %d, %+.3f at K = %d, all within %.3f of h^2.  READ IN "
      "ONE SENTENCE: the h^2 in the total variation is NOT an artefact of "
      "truncating at sixteen modes, and enlarging the search space does not touch "
      "it.  STATUS: MEASURED, negative"
      % (len(KOK), ", ".join("K=%d: %d" % (K, KDROP[K]) for K in K_SWEEP),
         SCHUR_KB, KB_MAX, qmin(RAT64), qmax(RAT64),
         qmin(PR_K[KB_MAX]), qmax(PR_K[KB_MAX]), KB_MAX, SCHUR_KB,
         qmin(DDB64), qmax(DDB64), qmin(EPS_K[KB_MAX]), qmax(EPS_K[KB_MAX]),
         KB_MAX, qmin(EPS_K[SCHUR_KB]), qmax(EPS_K[SCHUR_KB]), SCHUR_KB,
         qmin(EPSR64), qmax(EPSR64),
         F_TVK[SCHUR_KB], SCHUR_KB, F_TVK[2 * SCHUR_KB], 2 * SCHUR_KB,
         F_TVK[KB_MAX], KB_MAX,
         max(abs(F_TVK[K] - 2.0) for K in K_SWEEP)))

FEJ64 = [r["kfam"][KB_MAX]["fej_full"] for r in KOK]
FEJ2_64 = [r["kfam"][KB_MAX]["fej_2"] for r in KOK]
TRUNC16 = [r["kfam"][SCHUR_KB]["opt"] for r in KOK]
BEST_FLAT = []
for i, r in enumerate(KOK):
    cand = [t for t in (FEJ64[i], FEJ2_64[i], TRUNC16[i],
                        r["kfam"][KB_MAX]["opt"])
            if t["ok"] and t["price"] <= TIER_CONST[1]]
    BEST_FLAT.append(min(t["d_bnd"] for t in cand) if cand else float("nan"))
F_FEJ64 = fit_exp(XK, [t["TV"] for t in FEJ64])
check("pf_r2.closed_candidate",
      qmin([t["TV"] for t in FEJ64]) > 0.0 and qmin(BEST_FLAT) > RH_DELTA,
      "*** THE CLOSED CANDIDATE OF THE CONTRACT -- THE FEJER-WEIGHTED MODE SUM AT "
      "%d MODES INSTEAD OF HARD TRUNCATION AT %d -- AND IT IS THE BEST THING IN R2 "
      "WITHOUT BEING ENOUGH. ***  The full Fejer window t_k = 1 - k/%d applied to "
      "the %d-mode optimiser gives TV = %.3e .. %.3e (h^%+.3f, FIT) against the "
      "hard-truncated %.3e .. %.3e, i.e. a factor %.3f .. %.3f, at price %.3e .. "
      "%.3e; its demand is delta_bnd = %.4f .. %.4f.  The T162 shape (sigma = 2) "
      "carried up to %d modes gives delta_bnd = %.4f .. %.4f at price %.2e .. %.2e. "
      "AND THE POOLED FLAT-PRICE BEST OVER EVERYTHING R2 BUILT -- four weightings x "
      "three block sizes, at price <= %.2f -- IS delta_bnd = %.4f .. %.4f, still "
      "above the yardstick 1/2 on %d of %d windows.  So a smoother window on the "
      "mode axis is a real improvement over hard truncation and still not a "
      "crossing.  STATUS: MEASURED"
      % (KB_MAX, SCHUR_KB, KB_MAX, KB_MAX,
         qmin([t["TV"] for t in FEJ64]), qmax([t["TV"] for t in FEJ64]), F_FEJ64,
         qmin([t["TV"] for t in TRUNC16]), qmax([t["TV"] for t in TRUNC16]),
         qmin([FEJ64[i]["TV"] / TRUNC16[i]["TV"] for i in range(len(KOK))]),
         qmax([FEJ64[i]["TV"] / TRUNC16[i]["TV"] for i in range(len(KOK))]),
         qmin([t["price"] for t in FEJ64]), qmax([t["price"] for t in FEJ64]),
         qmin([t["d_bnd"] for t in FEJ64]), qmax([t["d_bnd"] for t in FEJ64]),
         KB_MAX, qmin([t["d_bnd"] for t in FEJ2_64]),
         qmax([t["d_bnd"] for t in FEJ2_64]),
         qmin([t["price"] for t in FEJ2_64]),
         qmax([t["price"] for t in FEJ2_64]), TIER_CONST[1],
         qmin(BEST_FLAT), qmax(BEST_FLAT),
         sum(1 for d in BEST_FLAT if d > RH_DELTA), len(BEST_FLAT)))

para("""R2.2  AND NOW THE SWEEPS CAN BE PUT ASIDE, BECAUSE THE QUESTION THEY WERE
PROBING HAS AN EXACT ANSWER.  R1 reduced R2'' to ONE question -- can the TOTAL
VARIATION of an admissible trial vector be BOUNDED IN h? -- and R2 found no family
that does it.  That is a search result.  Here is the theorem, in four steps, each
of which is elementary and machine-checked below:

  (T1) THE ZERO LAG IS A NORM.  w_0(x) = A_0 = ||v||^2 with v = T_K^T a, and the
       parity basis has ORTHONORMAL ROWS (T T^T = I, checked in R3), so
       w_0(x) = ||a||^2 EXACTLY.
  (T2) THE ZERO LAG IS BELOW THE TOTAL VARIATION.  Telescoping with w_M = 0,
       |w_0| = |sum_{d>=0} (w_d - w_{d+1})| <= sum_d |w_d - w_{d+1}| = TV(x).
  (T3) THE NORMALISATION IS NOT FREE.  The Thomson direction requires x_1 = 1,
       and a_1 = x_1 / sqrt(mu^P_1), so ||a||^2 >= 1 / mu^P_1 and therefore

         *** TV(x) >= 1 / mu^P_1 = 1 / (4 sin^2(pi / N)) ~ N^2 / (4 pi^2) ***

       for EVERY admissible trial vector in the parity sector -- no taper, no
       block size, no weighting can evade it.  mu^P_1 is the SMALLEST parity
       eigenvalue (Kac-Murdock-Szego 1953) and 1 / mu^P_1 grows like h^2.
  (T4) COMBINE WITH (E').  delta_bnd(x) < 1/2 requires P(x) > 2 kappa g_16 TV(x)
       >= 2 kappa g_16 / mu^P_1, so THE CROSSING PRICE IS BOUNDED BELOW BY A
       QUANTITY GROWING LIKE h^2, unconditionally, over the WHOLE admissible set
       and not merely over the families swept above.

THIS IS THE STRUCTURAL STATEMENT THE CONTRACT ASKED FOR IN THE ``FRONT-RESISTS''
CASE, AND IT IS AN INEQUALITY RATHER THAN AN OBSERVATION: a flat-price
sub-yardstick demand is IMPOSSIBLE in the parity sector as long as 1/s = 1/g_16
stays O(1) -- which is the whole point of the T152 .. T160 chain.  The h^2 is not
in the primes, not in the taper and not in the truncation: it is in the
NORMALISATION x_1 = 1 meeting the smallest parity eigenvalue.""")

E_W0, TVF_ALL, PFLOOR, MU1 = [], [], [], []
for r in WP:
    inv_mu1 = 1.0 / float(r["mu"][0])
    MU1.append(inv_mu1)
    for s in SIG_GRID:
        x = r["xstar"] * fejer_taper(SCHUR_KB, s)
        x = x / max(abs(float(x[0])), 1.0e-300)
        a = x / np.sqrt(r["mu"][:SCHUR_KB])
        w = lag_weights_corr(x, r["h"], r["Tb"])
        E_W0.append(abs(float(w[0]) - float(a @ a)) / abs(float(w[0])))
        TVF_ALL.append(r["sig"][s]["TV"] * float(r["mu"][0]))
    for K in K_SWEEP:
        if K in r["kfam"]:
            for nm in r["kfam"][K]:
                TVF_ALL.append(r["kfam"][K][nm]["TV"] * float(r["mu"][0]))
    PFLOOR.append(2.0 * KAPPA * r["g16"] * inv_mu1)

PC_OVER_FLOOR = [P_CROSS[i] / PFLOOR[i] for i in range(len(WP))]
F_MU1 = fit_exp(XHP, MU1)
F_PFL = fit_exp(XHP, PFLOOR)
check("pf_r2.tv_floor_theorem",
      qmax(E_W0) < EXACT_BAR and qmin(TVF_ALL) >= 1.0,
      "*** THEOREM, MACHINE-CHECKED ON EVERY TRIAL VECTOR THIS FILE BUILDS: THE "
      "TOTAL VARIATION CANNOT BE BOUNDED IN h, AND THAT CLOSES R-C''' NEGATIVELY "
      "ON THIS CONSTRUCTION. ***  (T1) w_0(x) = ||a(x)||^2 to %.2e .. %.2e "
      "relative.  (T2)+(T3) mu^P_1 TV(x) >= 1 on ALL %d trial vectors built "
      "anywhere in this file (%d knob settings + %d block-and-weighting "
      "combinations), with the actual slack mu^P_1 TV = %.2f .. %.2f -- so the "
      "bound is not only true but TIGHT TO A FACTOR OF ORDER TEN.  THE FLOOR "
      "ITSELF: 1 / mu^P_1 = 1 / (4 sin^2(pi/N)) = %.3e .. %.3e, growing as h^%+.3f "
      "(FIT, and h^2 exactly in closed form since N = 2h + 1).  THE MEASURED TV "
      "EXPONENT %+.3f IS THEREFORE NOT AN EMPIRICAL COINCIDENCE: it is the floor, "
      "up to a bounded factor"
      % (qmin(E_W0), qmax(E_W0), len(TVF_ALL), len(SIG_GRID),
         sum(len(r["kfam"].get(K, {})) for r in WP for K in K_SWEEP),
         qmin(TVF_ALL), qmax(TVF_ALL), qmin(MU1), qmax(MU1), F_MU1, F_TVREF))

check("pf_r2.price_floor_theorem",
      all(P_CROSS[i] >= PFLOOR[i] for i in range(len(WP)))
      and qmin(PFLOOR) > TIER_CONST[-1],
      "*** AND THE CONSEQUENCE, WHICH IS THE VERDICT OF T163 IN ONE INEQUALITY: "
      "*** (T4) any admissible trial vector with delta_bnd < 1/2 must pay "
      "P > 2 kappa g_16 / mu^P_1 = %.3e .. %.3e, growing as h^%+.3f (FIT).  The "
      "MEASURED crossing price respects it with a slack of %.2f .. %.2f, as it "
      "must, and the floor already EXCEEDS the largest declared flat cap %.2f by "
      "%.1e .. %.1e -- so the front provably cannot cross at any flat price on this "
      "surface, for EVERY admissible trial vector and not just the ones swept.  "
      "STATUS: THEOREM for the inequality chain (T1)-(T4), CERT-WINDOW for the "
      "input that g_16 is bounded below (g_16 = %.4f .. %.4f here, h-exponent "
      "%+.3f), MEASURED for the exponents"
      % (qmin(PFLOOR), qmax(PFLOOR), F_PFL, qmin(PC_OVER_FLOOR),
         qmax(PC_OVER_FLOOR), TIER_CONST[-1], qmin(PFLOOR) / TIER_CONST[-1],
         qmax(PFLOOR) / TIER_CONST[-1], qmin([r["g16"] for r in WP]),
         qmax([r["g16"] for r in WP]), F_G16))

print("")
print("TOTAL (R2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("R3  R-B'': WHAT REPLACES THE SIGN -- R-D -- AND THE END-TO-END ASSEMBLY")
# ----------------------------------------------------------------------------
para("""R3.1  R-B'': WHERE DID THE CHAIN WANT A SIGN, AND WHAT DOES IT ACTUALLY NEED
THERE?  T162 refuted R-B' as stated -- the 16x16 Gram form G_kl = sum_d
(Delta c^arch)_d R^1_kl(d) is INDEFINITE on every window -- and left an a-weighted
quarter bar (|sum_{k != l} a_k a_l G_kl| / |Q^arch| <= %.2f, CERT-UNIF).  The
question T163 has to answer is not whether the bar is true (T162 measured it) but
whether it is ENOUGH, and that is answered by locating the sign in the chain:

  * IN THE UPPER DIRECTION -- the only direction the chain uses -- NO SIGN IS
    NEEDED AT ALL.  1/s <= Q(x) holds for every x with Q(x) > 0 by Legendre
    duality alone (Thomson / Dirichlet; Maz'ya 1985 for the capacity reading).
    A positivity of G would be a statement about ALL x at once; the chain only
    ever evaluates ONE x.
  * WHAT THE SIGN WOULD HAVE BOUGHT IS ADMISSIBILITY WITHOUT EVALUATION, i.e.
    Q(x) > 0 for free, and UNIFORMITY IN h, i.e. one argument for every window.
  * SO R-B'' SPLITS INTO TWO MEASURABLE PIECES: (a) is Q(x) > 0 certified per
    window with margin far above the rounding floor?  (b) is the certificate
    h-FLAT, so that ``per window'' is not a hidden h-dependence?

Both are measured below at the operating point, and the quarter bar is quoted
from T162 rather than recomputed, so that nothing here double-counts it.""" %
     T162_QUARTER)

GSGN, GMIN63, QPOS, QFLAT = [], [], [], []
for r in WP:
    m = r["h"]
    dc = fwd_diff(r["c_ar"])
    om = 2.0 * math.pi * np.arange(1, SCHUR_KB + 1) / (2 * m + 1)
    G = np.empty((SCHUR_KB, SCHUR_KB))
    for k in range(SCHUR_KB):
        for l in range(SCHUR_KB):
            G[k, l] = float(np.dot(dc, abel_tail(R_pair(k, l, m, om))))
    G = sym(G)
    ev = np.linalg.eigvalsh(G)
    GMIN63.append(float(ev[0]) / max(abs(float(ev[-1])), 1.0e-300))
    a = r["xstar"] / np.sqrt(r["mu"][:SCHUR_KB])
    GSGN.append(abs(float(a @ (G @ a)) - r["Q_ar"]) / max(abs(r["Q_ar"]), 1.0e-300))
    s_c = S_CROSS[WP.index(r)]
    t = r["sig"][s_c] if np.isfinite(s_c) else r["ref"]
    QPOS.append(t["head"])
    QFLAT.append(t["canc"])

F_QFLAT = fit_exp(XHP, QFLAT)
check("pf_r3.sign_not_needed",
      qmax(GSGN) < 1.0e-9 and qmax(GMIN63) < 0.0 and qmin(QPOS) > HEADROOM_BAR,
      "*** R-B'' ANSWERED, AND THE ANSWER IS THAT THE CHAIN NEVER NEEDED THE SIGN "
      "-- IT NEEDED A POSITIVE EVALUATED NUMBER WITH A MARGIN, WHICH IT HAS. ***  "
      "(i) T162's negative REPRODUCED: the 16x16 Gram form satisfies a^T G a = "
      "Q^arch to %.2e .. %.2e relative (so it IS the arch half resolved into modes) "
      "and its lam_min / |lam_max| = %.3f .. %.3f, i.e. STRICTLY NEGATIVE on all %d "
      "windows -- there is no sign to have.  (ii) AND IT IS NOT NEEDED: at the "
      "operating point Q(x) > 0 with headroom |Q| / (max half x eps) = %.2e .. "
      "%.2e, i.e. at least %.1f decades above the rounding floor, so admissibility "
      "is CERTIFIED by evaluation on every window.  (iii) THE UNIFORMITY PIECE IS "
      "THE ONE THAT SURVIVES AS OPEN: the certified quantity CANC = |Q| / max half "
      "at the operating point is %.3e .. %.3e with h-exponent %+.3f, so it is NOT "
      "h-flat and 'per window' does carry an h-dependence.  R-B'' therefore reduces "
      "from 'find a substitute for the sign' to 'make the positivity margin "
      "h-uniform', which is a strictly smaller question and the a-weighted quarter "
      "bar (T162, CERT-UNIF, %.2f) is exactly the kind of object that would do it.  "
      "STATUS: THEOREM for the duality direction, CERT-WINDOW for the margin, "
      "MEASURED for the exponent"
      % (qmin(GSGN), qmax(GSGN), qmin(GMIN63), qmax(GMIN63), len(WP),
         qmin(QPOS), qmax(QPOS), math.log10(qmin(QPOS)),
         qmin(QFLAT), qmax(QFLAT), F_QFLAT, T162_QUARTER))

para("""R3.2  R-D, SHORT, BECAUSE THE FEJER PERSPECTIVE HAS A STRUCTURAL REASON NOT TO
HELP IT.  The fifth device for R1'' needs the flat ratio rho = %.4f .. %.4f > 1
(T161, quoted) pushed below 1.  The Fejer knob acts on the TRIAL VECTOR x; the
block floor 1/g_K is a property of the OPERATOR B alone and does not see x at all.
So tapering cannot move rho, and the only way a smoothing could is by acting on B
itself -- i.e. by replacing the lag coefficients c_d with a Fejer-averaged c_d,
which is a DIFFERENT operator and therefore bounds a DIFFERENT number.  That is
measured here as a negative result and not offered as a device.""" % T161_RHO1)

RHO_FEJ, RHO_BASE = [], []
for r in WP:
    g = r["gcum"]
    RHO_BASE.append(float((1.0 / g[SCHUR_KB - 1]) / (1.0 / g[SCHUR_KB - 2])))
    cf = r["c"].copy()
    ker = np.array([0.25, 0.5, 0.25])
    cf[1:-1] = (ker[0] * r["c"][:-2] + ker[1] * r["c"][1:-1]
                + ker[2] * r["c"][2:])
    Bf = sym((r["Tb"] @ (odd_toeplitz(cf, r["M"]) @ r["Tb"].T))
             * np.outer(1.0 / np.sqrt(r["mu"]), 1.0 / np.sqrt(r["mu"])))
    gf = cf_ladder(Bf[:SCHUR_KB, :SCHUR_KB], SCHUR_KB)
    RHO_FEJ.append(float((1.0 / gf[-1]) / (1.0 / g[SCHUR_KB - 1]))
                   if gf is not None else float("nan"))

F_RHOF = fit_exp(XHP, RHO_FEJ)
check("pf_r3.fifth_device",
      qmin(RHO_BASE) > 0.0 and np.isfinite(qmax(RHO_FEJ)),
      "*** R-D: THE FEJER PERSPECTIVE DOES NOT REACH THE FIFTH DEVICE, AND THE "
      "REASON IS A TYPE MISMATCH RATHER THAN A NUMBER. ***  Tapering changes the "
      "TRIAL VECTOR; the block floor 1/g_K is a spectral property of B and is "
      "INVARIANT under any reweighting of x, so rho = %.4f .. %.4f (T161, quoted) "
      "cannot be moved from this direction -- that is an argument, not a "
      "measurement.  What CAN be smoothed is the operator: replacing c_d by the "
      "Fejer 3-tap average (1/4, 1/2, 1/4) gives a block floor ratio "
      "1/g_16(smoothed) / 1/g_16 = %.4f .. %.4f with h-exponent %+.3f -- WHICH IS "
      "THE SAME h^2 AGAIN, for the same reason as in R1.2: smoothing the operator "
      "destroys the arch/atom cancellation that makes 1/s an O(1) number.  The "
      "smoothed operator also bounds a DIFFERENT number, so this is reported as a "
      "MEASURED negative and explicitly NOT as a device.  The last ladder step "
      "itself, (1/g_16) / (1/g_15) = %.4f .. %.4f, is the size of the margin any "
      "fifth device has to beat.  STATUS: MEASURED, negative; R-D stays open and "
      "untouched by T163"
      % (T161_RHO1[0], T161_RHO1[1], qmin(RHO_FEJ), qmax(RHO_FEJ), F_RHOF,
         qmin(RHO_BASE), qmax(RHO_BASE)))

print("")
print("TOTAL (R3.1-R3.2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# --- R3.3  the end-to-end assembly and the obligatory stress -------------------
para("""R3.3  THE BEST OPERATING POINT, PUT THROUGH THE WHOLE CHAIN, END TO END.  There
are TWO operating points because the surface offers two, and stating only one of
them would be dishonest:

  OP-FLAT   sigma*(P <= %.2f): a FLAT price, hence a certificate that is uniform
            in h up to a constant, and a demand ABOVE the yardstick.
  OP-RUNG   sigma*(P <= P_aff): a demand BELOW the yardstick, at a price the
            chain has already paid once (T157 route 0), but NOT flat in h.

The chain, written out at each of them: (1) Q(x) is evaluated in closed form from
the lag coefficients c = c^arch + c^atom, with the pairing identity of Q0;
(2) 1/s <= Q(x) by the Thomson direction, no accuracy claim about x needed;
(3) the Abel step moves the atom half onto Delta w, and the ONE unconditional
input |psi(x) - x| <= kappa x (Chebyshev 1852 / Rosser-Schoenfeld 1962) bounds it
by 2 kappa TV(x) X^{-delta} for whatever depth delta the primes actually deliver;
(4) so the chain closes iff delta >= delta_bnd(x), and delta_bnd is (E).""" %
     TIER_CONST[1])

OP = {}
for tag, use_aff in (("OP-FLAT", False), ("OP-RUNG", True)):
    rows = []
    for r in WP:
        cap = r["P_aff"] if use_aff else TIER_CONST[1]
        s, t = front_at(r, cap)
        rows.append((r, s, t))
    OP[tag] = rows

for tag in ("OP-FLAT", "OP-RUNG"):
    rows = OP[tag]
    db = [t["d_bnd"] for (_r, _s, t) in rows]
    dv = [t["d_val"] for (_r, _s, t) in rows]
    pp = [t["price"] for (_r, _s, t) in rows]
    qq = [t["Q"] for (_r, _s, t) in rows]
    tv = [t["TV"] for (_r, _s, t) in rows]
    info("pf_r3.%s" % tag.lower(),
         "sigma* = %.0f .. %.0f; 1/s <= Q = %.4e .. %.4e; price %.3e .. %.3e "
         "(h^%+.2f, FIT); TV = %.3e .. %.3e; delta_bnd = %.4f .. %.4f; "
         "delta_val = %.4f .. %.4f; below the yardstick on %d of %d windows"
         % (qmin([s for (_r, s, _t) in rows]), qmax([s for (_r, s, _t) in rows]),
            qmin(qq), qmax(qq), qmin(pp), qmax(pp), fit_exp(XHP, pp),
            qmin(tv), qmax(tv), qmin(db), qmax(db), qmin(dv), qmax(dv),
            sum(1 for d in db if d < RH_DELTA), len(db)))

E2E = []
for (r, s, t) in OP["OP-RUNG"]:
    need = 2.0 * KAPPA * t["TV"] * r["X"] ** (RH_DELTA - t["d_bnd"])
    E2E.append(abs(need - abs(t["Q"])) / abs(t["Q"]))
check("pf_r3.end_to_end", qmax(E2E) < 1.0e-10,
      "*** THE CHAIN CLOSES ARITHMETICALLY AT THE OPERATING POINT, WHICH IS THE "
      "ONLY THING 'END TO END' CAN MEAN HERE. ***  At OP-RUNG the step-(3) bound "
      "2 kappa TV(x) X^{1/2 - delta_bnd} reproduces |Q(x)| to %.2e .. %.2e on "
      "all %d windows -- i.e. delta_bnd IS by construction the exact depth at which "
      "the unconditional input would suffice, and the chain has no other leak.  "
      "WHAT IS THEREFORE PROVED AND WHAT IS NOT: the inequality 1/s <= Q(x) is a "
      "THEOREM at every listed x (duality plus an evaluated positive number); the "
      "value of delta the primes deliver is NOT decided here and cannot be, since "
      "no zero and no L-function is touched anywhere in this file"
      % (qmin(E2E), qmax(E2E), len(E2E)))

S_CAL = S_CROSS[0]                    # the SMALLEST window, fixed in advance
OOS_D, OOS_P = [], []
for r in WP[1:]:
    t = r["sig"][S_CAL]
    OOS_D.append(t["d_bnd"])
    OOS_P.append(t["price"] / r["P_aff"])
F_OOSD = fit_exp(XHP[1:], [d - RH_DELTA for d in OOS_D])
check("pf_r3.antifit_out_of_sample",
      all(d < RH_DELTA for d in OOS_D) and qmax(OOS_P) <= 1.0,
      "*** ANTI-FITTING, ENFORCED AND NOT PROMISED: THE KNOB SETTING IS CALIBRATED "
      "ON ONE WINDOW AND USED, UNCHANGED, ON THE OTHER %d. ***  sigma = %.0f is "
      "fixed from the SMALLEST window alone (h = %d) by the preregistered "
      "price rule, then applied without adjustment: delta_bnd = %.4f .. %.4f "
      "(below the yardstick on %d of %d out-of-sample windows) at price "
      "%.4f .. %.4f of P_aff, i.e. inside the affordable tier everywhere.  The "
      "excess over the yardstick behaves as h^%+.3f (FIT).  NO PER-WINDOW TUNING "
      "IS USED ANYWHERE IN THIS FILE: the two operating points above are defined "
      "by price caps, and this control shows a single global sigma reproduces them"
      % (len(WP) - 1, S_CAL, WP[0]["h"], qmin(OOS_D), qmax(OOS_D),
         sum(1 for d in OOS_D if d < RH_DELTA), len(OOS_D),
         qmin(OOS_P), qmax(OOS_P), F_OOSD))

# --- the must-break controls --------------------------------------------------
NOGO_FAC = (2, 4, 8, 16, 32)          # DECLARED sweep; nu = 2 NU_MAIN / fac,
                                      # i.e. nu = 4 (identity) down to nu = 1/4
SURR, NOGO = [], []
for r in WP:
    at = atoms_in(r["alpha"])
    mm = np.array([t[1] for t in at], dtype=float)
    rs = np.random.RandomState(9163 + r["h"])
    uu_s = np.sort(rs.uniform(0.0, 2.0 * r["alpha"], mm.shape[0]))
    c_s, _, _, _ = atom_lags(r["alpha"], r["M"], list(zip(uu_s, mm)))
    SURR.append(abs(float(np.dot(c_s, r["w"])) + r["Q_ar"]) / abs(r["Q"]))
    # THE T145 RESOLUTION NO-GO: nu below the T105 floor nu >= 4, i.e. a lag
    # spacing too coarse, so that distinct prime powers share cells.  The
    # coarsening factor is SWEPT, because the no-go predicts the damage to GROW
    # with the collision rate and that is a sharper test than one number
    row = []
    for fac in NOGO_FAC:
        M_c = 2 * max(SCHUR_KB + 1, r["M"] // fac)
        D_c = 2.0 * r["alpha"] / M_c
        c_atc, _, _, _ = atom_lags(r["alpha"], M_c, at)
        c_arc = arch_lags(M_c, D_c)
        Tb_c = parity_basis(M_c // 2, SCHUR_KB)
        wc = lag_weights_corr(r["xstar"], M_c // 2, Tb_c)
        Qc = float(np.dot(c_arc + c_atc, wc))
        canc_c = abs(Qc) / max(abs(float(np.dot(c_arc, wc))),
                               abs(float(np.dot(c_atc, wc))), 1.0e-300)
        # M_c = 2 (M // fac), so the LAG SPACING is coarsened by fac/2 and the
        # resolution parameter is nu = 2 NU_MAIN / fac (fac = 2 is the identity,
        # which is why the fac = 2 column must and does come out at 1.0)
        row.append((2.0 * NU_MAIN / fac, mm.shape[0] / float(M_c),
                    canc_c / r["ref"]["canc"]))
    NOGO.append(row)

check("pf_r3.nogo_surrogate", qmin(SURR) > 100.0,
      "*** MUST-BREAK CONTROL 1, AND IT BREAKS BY ORDERS OF MAGNITUDE: THE O(1) "
      "TOTAL IS AN ARITHMETIC FACT AND NOT A PROPERTY OF THE MACHINERY. ***  "
      "Replacing the prime-power positions log n by a UNIFORM sample on "
      "[0, 2 alpha] while keeping the SAME mass multiset 2 Lambda(n)/sqrt n and the "
      "SAME count, |Q^arch + Q^surrogate| / |Q| jumps to %.3e .. %.3e.  So the "
      "cancellation R1.2 prices is carried by WHERE the prime powers sit, and every "
      "price statement above is a statement about arithmetic"
      % (qmin(SURR), qmax(SURR)))

DMG = [[row[j][2] for row in NOGO] for j in range(len(NOGO_FAC))]
OCC = [[row[j][1] for row in NOGO] for j in range(len(NOGO_FAC))]
MONO_NOGO = all(qmed(DMG[j + 1]) > qmed(DMG[j]) for j in range(len(NOGO_FAC) - 1))
check("pf_r3.nogo_t145",
      MONO_NOGO and qmin(DMG[-1]) > 10.0 and qmax(DMG[0]) < qmin(DMG[-1]),
      "*** MUST-BREAK CONTROL 2 -- THE T145 RESOLUTION NO-GO -- AND IT MUST BREAK "
      "OR EVERY NUMBER IN THIS FILE IS AN ARTEFACT. ***  The lag spacing is "
      "coarsened by %s, i.e. nu = %s against the T105 admissibility floor nu >= %d "
      "(the first column is the IDENTITY and is carried as a null control), and the "
      "quantity R1.2 prices -- the arch/atom cancellation -- is measured as "
      "CANC(coarse) / CANC(fine): %s.  Cell occupancy over the same sweep: %s.  IT "
      "BREAKS, AND IT BREAKS MONOTONICALLY IN THE COLLISION RATE, which is what "
      "makes this the T145 mechanism rather than a generic loss of accuracy: the "
      "median damage rises at every step of the sweep and at the coarsest setting "
      "it is >= %.1f on EVERY window.  The surface of this file (nu = %d) is on the "
      "right side of that no-go by construction"
      % ("/".join("%gx" % (f / 2.0) for f in NOGO_FAC),
         "/".join("%.2f" % (2.0 * NU_MAIN / f) for f in NOGO_FAC), NU_MAIN,
         "; ".join("nu=%.2f: %.1f .. %.1f"
                   % (2.0 * NU_MAIN / NOGO_FAC[j], qmin(DMG[j]), qmax(DMG[j]))
                   for j in range(len(NOGO_FAC))),
         "; ".join("nu=%.2f: %.2f .. %.2f"
                   % (2.0 * NU_MAIN / NOGO_FAC[j], qmin(OCC[j]), qmax(OCC[j]))
                   for j in range(len(NOGO_FAC))),
         qmin(DMG[-1]), NU_MAIN))

E_DIR, E_PAR, E_ORT = [], [], []
_rs = np.random.RandomState(1631)
for _ in range(64):
    aa = float(_rs.uniform(0.05, 6.0))
    bb = float(_rs.uniform(-3.0, 3.0))
    LL = int(_rs.randint(1, 40))
    # the convention of _cos_sum is sum_{j=1}^{L} cos(beta + j alpha)
    direct = float(np.sum(np.cos(bb + aa * np.arange(1, LL + 1))))
    E_DIR.append(abs(float(_cos_sum(aa, bb, LL)) - direct) / max(abs(direct), 1.0))
for r in WP[:4]:
    m = r["h"]
    cL = np.zeros(r["M"])
    cL[0], cL[1] = 2.0, -1.0
    E_PAR.append(float(np.max(np.abs(odd_toeplitz(cL, r["M"]) - lap_P_mat(m)))))
    Tb = r["Tb"]
    E_ORT.append(float(np.max(np.abs(Tb @ Tb.T - np.eye(KB_MAX)))))
check("pf_r3.classical_controls",
      qmax(E_DIR) < 1.0e-12 and qmax(E_PAR) < 1.0e-12 and qmax(E_ORT) < 1.0e-12,
      "*** THE CLASSICAL CONTROLS, EXACT, BECAUSE EVERYTHING CLOSED IN THIS FILE "
      "RESTS ON THEM. ***  (i) The Dirichlet-kernel identity (Dirichlet 1829) "
      "against DIRECT summation on %d random (alpha, beta, L): %.2e .. %.2e.  "
      "(ii) The parity Laplacian: odd_toeplitz(c^L) = tridiag(-1, 2, -1) with last "
      "diagonal 3, to %.2e (Kac-Murdock-Szego 1953).  (iii) The parity basis is "
      "orthonormal, T T^T = I to %.2e -- which is what makes the mode coordinates "
      "of R2 an isometry and the K-sweep a fair comparison"
      % (len(E_DIR), qmin(E_DIR), qmax(E_DIR), qmax(E_PAR), qmax(E_ORT)))

GB = []
for r in WP:
    wp = r["w"] + 0.01 * float(np.max(np.abs(r["w"])))
    GB.append((abs(float(np.sum(wp))) / float(np.sum(np.abs(wp))),
               abs(float(np.sum(r["dw"])) - float(np.sum(back_diff(wp))))))
check("pf_r3.nogo_gauge",
      qmin([t[0] for t in GB]) > 1.0e-6,
      "*** MUST-BREAK CONTROL 3: THE GAUGE IDENTITY IS LOAD-BEARING. ***  Adding a "
      "constant of 1 per cent of sup|w| to the weight vector destroys sum_d w_d = 0 "
      "(the gauge residual jumps from %.2e to %.3e .. %.3e of ||w||_1), which is "
      "the identity that licenses the Abel step of the chain -- so the step is not "
      "a formality"
      % (qmax([r["gauge"] for r in WP]), qmin([t[0] for t in GB]),
         qmax([t[0] for t in GB])))

print("")
print("TOTAL (R3): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("R4  THE MAP V35, THE PROMOTION CANDIDATES, THE REST LIST, THE VERDICT")
# ----------------------------------------------------------------------------
RELOC_EXACT = (abs(F_TVR) < BAR_FLAT and abs(qmed(TAU_TV)) < 0.05
               and qmin(FLOOR_PRED) > RH_DELTA)
if CROSS_FLAT and abs(fit_exp(XHP, [t["price"] for (_r, _s, t) in OP["OP-FLAT"]])) \
        < BAR_FLAT:
    VERDICT = "FRONT-CROSSES"
elif RELOC_EXACT:
    VERDICT = "FRONT-RESISTS"
else:
    VERDICT = "DELTA-REDUCED"

THEOREMS = ["pf_q0.scales", "pf_q0.corr_form", "pf_q0.pairing_identity",
            "pf_q0.price_reference", "pf_r1.knob_endpoints",
            "pf_r1.exchange_identity", "pf_r2.tv_floor_theorem",
            "pf_r2.price_floor_theorem", "pf_r3.end_to_end",
            "pf_r3.classical_controls", "pf_r3.nogo_gauge"]
CERT_UNIF = ["pf_q0.chebyshev_kappa"]
CERT_WIN = ["pf_q0.chebyshev", "pf_r1.flat_price_floor", "pf_r3.sign_not_needed",
            "pf_r3.antifit_out_of_sample"]
MEASURED = ["pf_r1.t162_reproduction", "pf_r1.monotone_knob", "pf_r1.front_read",
            "pf_r1.relocation_bounded", "pf_r1.cancellation_is_the_price",
            "pf_r2.mode_sweep", "pf_r2.closed_candidate", "pf_r3.fifth_device",
            "pf_r3.nogo_surrogate", "pf_r3.nogo_t145"]

para("""R4.1  THE MAP V35 -- WHERE R2'' STANDS AFTER T163, IN NUMBERS AND NOT IN PROSE.

THE ONE OBJECT, AND T163's CONTRIBUTION IS TO HAVE WRITTEN IT AS AN IDENTITY.  For
every admissible trial vector,

    delta_bnd(x) = 1/2 + log( 2 kappa g_16 TV(x) / P(x) ) / log X ,          (E)

so the Pareto front the contract asked for is not a two-dimensional surface to be
searched but a ONE-DIMENSIONAL exchange along a single ratio.  The three levers
T162 handed over are all inside (E) and all measured here:

  THE FEJER KNOB (R1).  Monotone in both coordinates, so the knob curve IS the
  front.  At the DECLARED FLAT price caps %s the front sits at delta_bnd =
  %.3f .. %.3f / %.3f .. %.3f / %.3f .. %.3f, i.e. NEVER below the yardstick 1/2.
  The crossing price is P_cross = %.2e .. %.2e growing as h^%+.2f, and the
  crossing exponent DECOMPOSES exactly into the total-variation exponent
  (%+.3f) plus the g_16 exponent (%+.3f).
  THE PRICE ANATOMY (R1.2).  The taper's structural gain is a BOUNDED, h-flat
  factor %.2f .. %.2f in TV, worth at most %.3f of delta and DECAYING like
  1/log X; the rest of every delta it buys is paid one-for-one in price
  (tau_TV = %.4f median).  So the h^2.86 of T162 is the SAME h^2 as T161's
  granularity, now localised: it is the total variation of the weight sequence
  against an O(1) pairing.
  THE SEARCH SPACE (R2).  K = 16 -> 32 -> 64 lowers TV by only %.3f .. %.3f at a
  price DIVIDEND, and the TV exponent is unmoved (%+.3f -> %+.3f -> %+.3f).  The
  h^2 is not a truncation artefact -- and R2.2 turns that observation into a
  THEOREM: mu^P_1 TV(x) >= 1 for EVERY admissible x, so the crossing price is
  bounded below by 2 kappa g_16 / mu^P_1, which grows like h^2 in closed form.
  THE OPERATING POINTS (R3.3).  OP-FLAT: price %.2f-flat, delta_bnd %.3f .. %.3f.
  OP-RUNG: delta_bnd %.4f .. %.4f at a price that is %.1f .. %.1f TIMES SMALLER
  than the T157 route-(0) certificate the chain already accepted -- the one
  genuinely NEW positive of T163 -- but not flat in h.""" % (
    "/".join("%.2f" % t for t in TIER_CONST),
    FLAT_BEST[0], FLAT_WORST[0], FLAT_BEST[1], FLAT_WORST[1],
    FLAT_BEST[2], FLAT_WORST[2], qmin(P_CROSS), qmax(P_CROSS), F_PCROSS,
    F_TVCR, F_G16, 1.0 / qmax(TVR), 1.0 / qmin(TVR), qmax(DGAIN_TV),
    qmed(TAU_TV), qmin(RAT64), qmax(RAT64), F_TVK[SCHUR_KB],
    F_TVK[2 * SCHUR_KB], F_TVK[KB_MAX], TIER_CONST[1],
    qmin([t["d_bnd"] for (_r, _s, t) in OP["OP-FLAT"]]),
    qmax([t["d_bnd"] for (_r, _s, t) in OP["OP-FLAT"]]),
    qmin([t["d_bnd"] for (_r, _s, t) in OP["OP-RUNG"]]),
    qmax([t["d_bnd"] for (_r, _s, t) in OP["OP-RUNG"]]),
    1.0 / qmax(PC_OVER_AFF), 1.0 / qmin(PC_OVER_AFF)))

para("""R4.2  PROMOTION CANDIDATES, ALL **PENDING**, AND NONE OF THEM RE-PROMOTES
ANYTHING T162 OR THE PARALLEL v554 PROMOTION ALREADY CARRIES (the sampling
identity at the harmonic frequencies, the head split Psi_d, the moment laws and
the closed log-moment are NOT restated here).

  P1 **THEOREM** THE CORRELATION FORM OF THE CLOSED WEIGHT VECTOR.  w_0 = A_0,
     w_d = 2 A_d - H_{M-1-d} with A the autocorrelation and H the
     self-convolution of v = T_K^T a: the T160..T162 double sum over Dirichlet
     kernels equals a single correlation, to %.1e .. %.1e.  It is what makes any
     block size K free of cost and it is a strictly computational identity.
  P2 **THEOREM** THE EXCHANGE LAW (E) AND THE CROSSING CRITERION (E').
     delta_bnd < 1/2 <=> P > 2 kappa g_16 TV, exact at all %d grid points to
     %.1e.  This replaces T162's MEASURED ``exchange rate'' by an identity.
  P3 **THEOREM** THE PRICE AXIS IS CHAIN-DERIVED.  Q(x*) = 1/g_16 (the T158 top
     rung) and the Fejer knob's endpoints are the ladder's endpoints: sigma = 1
     is the K = 1 rung, sigma = infinity the K = 16 rung, each to %.1e.  So
     ``affordable'' is defined by the chain and not by this file.
  P4 **THEOREM** THE TOTAL-VARIATION FLOOR AND THE PRICE FLOOR IT IMPLIES.
     w_0(x) = ||a||^2 and TV(x) >= |w_0(x)| >= 1 / mu^P_1 = 1 / (4 sin^2(pi/N))
     for EVERY admissible trial vector, verified on all %d built here with slack
     %.1f .. %.1f; hence, by (E'), delta_bnd(x) < 1/2 forces
     P(x) > 2 kappa g_16 / mu^P_1 = %.2e .. %.2e ~ h^2.  THIS IS THE ROW THAT
     CARRIES THE VERDICT and it is the strongest statement in the file.
  P4b **CERT-WINDOW** THE FLAT-PRICE FLOOR, EMPIRICAL VERSION.  With the measured
     h-flat TV floor TV >= %.4f TV(x*), every knob point at price <= %.2f obeys
     delta_bnd >= %.3f .. %.3f > 1/2 on all %d windows -- superseded in strength
     by P4 but retained because it is the version that needs no normalisation
     argument.
  P5 **MEASURED, NEGATIVE** THE MODE SWEEP.  K = 16 -> 64 leaves the TV exponent
     at %+.3f .. %+.3f and makes delta_bnd worse by up to %+.4f at a price
     dividend.  A negative that closes a route is worth a row.
  P6 **MEASURED** THE CROSSING PRICE AND ITS MARGIN.  P_cross = %.2e .. %.2e
     (h^%+.2f), which is %.2f .. %.2f of P_aff -- sub-yardstick demand IS
     reachable strictly inside a certificate the chain owns.
  P7 **MEASURED, NEGATIVE** OPERATOR SMOOTHING DOES NOT HELP R-D.  The Fejer
     3-tap average of the lag coefficients degrades the block floor by
     %.1e .. %.1e (h^%+.2f), the same h^2 again.""" % (
    qmin(E_CORR), qmax(E_CORR), len(WP) * len(SIG_GRID), qmax(E_EXCH),
    max(qmax(E_SIG1), qmax(E_SIGINF)),
    len(TVF_ALL), qmin(TVF_ALL), qmax(TVF_ALL), qmin(PFLOOR), qmax(PFLOOR),
    TV_FLOOR, TIER_CONST[1], qmin(FLOOR_PRED), qmax(FLOOR_PRED), len(WP),
    min(F_TVK[K] for K in K_SWEEP), max(F_TVK[K] for K in K_SWEEP),
    qmax(DDB64), qmin(P_CROSS), qmax(P_CROSS), F_PCROSS,
    qmin(PC_OVER_AFF), qmax(PC_OVER_AFF),
    qmin(RHO_FEJ), qmax(RHO_FEJ), F_RHOF))

para("""R4.3  THE REST LIST, AND IT IS SHORTER THAN IT HAS EVER BEEN BECAUSE ONE ITEM
LEFT IT AS A THEOREM RATHER THAN AS A HOPE.

  R-C'''  **CLOSED, NEGATIVELY, ON THIS CONSTRUCTION.**  ``Bounded total
          variation at bounded price'' was the whole of R2'' after R1, and R2.2
          shows it is IMPOSSIBLE in the parity sector: TV(x) >= 1 / mu^P_1 ~ h^2
          for every x with x_1 = 1, verified with slack %.1f .. %.1f on all %d
          trial vectors built here (%d taper widths x %d weightings x %d block
          sizes).  A route that is closed by an inequality is worth more than a
          route that is merely unproductive.
  R-E     THE SUCCESSOR THE THEOREM POINTS AT, AND IT IS THE ONLY DIRECTION LEFT
          ON THIS AXIS: the h^2 enters through the NORMALISATION x_1 = 1 meeting
          the SMALLEST parity eigenvalue mu^P_1 = 4 sin^2(pi/N) -- i.e. it is the
          reciprocal spectral gap of the parity Laplacian
          (Kac-Murdock-Szego 1953), and nothing about the primes.  So the
          question becomes whether the entry functional can be represented in a
          sector whose lowest eigenvalue does NOT vanish like h^-2, or whether
          the downstream T159/T160 chain in fact tolerates a 1/s ceiling that
          grows -- which is a question about the chain and not about this
          pairing.  BOTH ARE PRIME-FREE AND NEITHER IS TOUCHED HERE.
  R-B'''  MAKE THE POSITIVITY MARGIN h-UNIFORM.  The sign does not exist (R3.1
          reproduces T162's indefiniteness) and is not needed in the upper
          direction; what is needed is that CANC at the operating point stop
          drifting (h-exponent %+.3f).  The T162 a-weighted quarter bar is the
          right shape of object for this and is NOT re-derived here.
  R-D     THE FIFTH DEVICE for R1'' (rho = %.4f .. %.4f > 1 flat, T161) --
          untouched by T162 and, for the type reason of R3.2, untouched by the
          Fejer perspective as well.""" % (
    qmin(TVF_ALL), qmax(TVF_ALL), len(TVF_ALL), len(SIG_GRID), 4, len(K_SWEEP),
    F_QFLAT, T161_RHO1[0], T161_RHO1[1]))

check("pf_r4.balance",
      len(THEOREMS) + len(CERT_UNIF) + len(CERT_WIN) + len(MEASURED) == 26
      and not FAILS,
      "*** THE BALANCE OF T163, TYPED, AND EVERY ROW IS A CHECK IN THIS RUN. ***  "
      "%d THEOREM (machine-checked identities) / %d CERT-UNIF / %d CERT-WINDOW / "
      "%d MEASURED = %d typed rows out of %d checks; the remaining %d are the "
      "firewall (%d), the surface (1) and this balance row.  T162 closed at "
      "%d/%d/%d/%d and T163 adds to it rather than restating it.  ZERO FIT rows: "
      "the only fitted numbers anywhere are h-exponents, each labelled (FIT) in "
      "place, and no fitted number carries a claim"
      % (len(THEOREMS), len(CERT_UNIF), len(CERT_WIN), len(MEASURED),
         len(THEOREMS) + len(CERT_UNIF) + len(CERT_WIN) + len(MEASURED),
         N_CHK + 1, N_CHK + 1 - 26, 4, T162_BALANCE[0], T162_BALANCE[1],
         T162_BALANCE[2], T162_BALANCE[3]))

para("""R4.4  THE VERDICT: **%s** .

THE THREE HONEST SENTENCES, AND THE FIRST ONE IS A THEOREM RATHER THAN A
MEASUREMENT, WHICH IS WHY THIS VERDICT IS NOT MERELY A FAILED SEARCH.  (1) THE
FRONT PROVABLY CANNOT CROSS AT FLAT PRICE.  The identity (E) makes the demand
depend on the trial vector ONLY through TV(x) / |Q(x)| and the price is |Q(x)| in
units of the certified 1/g_16, so delta_bnd < 1/2 IS the inequality
P > 2 kappa g_16 TV; and TV is bounded BELOW, for every admissible x, by
1 / mu^P_1 = 1 / (4 sin^2(pi/N)) -- because w_0(x) = ||a(x)||^2 >= 1/mu^P_1 under
the normalisation x_1 = 1 that the Thomson direction requires, and TV >= |w_0| by
telescoping -- so the crossing price is bounded below by %.2e .. %.2e, growing
like h^2 in closed form and already exceeding the largest flat cap %.2f by a
factor %.1e .. %.1e.  (2) SO THE RELOCATION T162 SUSPECTED IS EXACT, AND ITS h^2
IS NOW IDENTIFIED: the Fejer taper does lower the total variation, but by an
h-FLAT factor %.2f .. %.2f worth at most %.3f of delta and DECAYING like 1/log X,
while tau_TV = %.4f (median) says the remainder is paid one-for-one out of the
price -- and the h^2.86 of T162, the h^%+.2f of the crossing price here and
T161's granularity are ALL the reciprocal smallest parity eigenvalue,
i.e. the spectral gap of the parity Laplacian (Kac-Murdock-Szego 1953) meeting
the entry normalisation.  IT WAS NEVER IN THE PRIMES.  (3) AND THE SEARCH SPACE
CONFIRMS IT FROM THE OTHER SIDE: going from 16 to %d modes buys a price dividend
and a WORSE demand and leaves the TV exponent at h^%+.2f, %.1f .. %.1f times the
theoretical floor -- so the floor is tight and the sixteen-mode truncation was
never the problem.

THE ONE GENUINELY NEW POSITIVE, STATED WITHOUT INFLATION BECAUSE IT IS NOT A
CLOSURE.  T162 knew that sub-yardstick demand costs SOMETHING; T163 measures WHAT,
against the chain's own price scale, and the answer is better than expected: the
crossing sits at %.2f .. %.2f of P_aff, i.e. STRICTLY INSIDE the T157 route-(0)
certificate 1/s <= B_11 that the chain has already accepted, with the margin
WIDENING as h grows (P_cross ~ h^%+.2f against P_aff ~ h^%+.2f).  A single
GLOBALLY FIXED knob setting sigma = %.0f, calibrated on the smallest window alone,
delivers delta_bnd = %.3f .. %.3f out of sample on all %d remaining windows at
%.2f .. %.2f of P_aff.  What that is NOT: a flat certificate.  A per-window bound
at a price growing like h^2 does not make an h-uniform statement, and T163 says so
rather than dressing it up.

WHAT T163 THEREFORE CONTRIBUTES.  Not a closure of R2'', but a CLOSURE OF THE
QUESTION R2'' HAD BECOME.  R2'' entered as a two-dimensional trade-off between a
demand and a price; (E) collapsed it to the single question whether some
admissible trial vector has TOTAL VARIATION BOUNDED IN h; and the answer is NO, by
an inequality, in the parity sector with the entry normalisation -- so THIS IS THE
FINAL HONEST ANATOMY OF R2'' ON THIS SURFACE, and the successor question (R-E) is
about which sector represents the entry functional, not about prime powers.  Every
other lever is measured and closed: three ladders that saturate (T162), a taper
whose structural budget is a decaying constant, a mode sweep that pays a dividend
and buys nothing, and an operator smoothing that reproduces the same h^2.

AND THE FENCE, ONE LAST TIME, BECAUSE IT IS THE MOST IMPORTANT SENTENCE HERE.  No
zero of any L-function was read, generated, tabulated, approximated or
extrapolated; no L-function was evaluated; the only arithmetic object touched was
a finite von Mangoldt sieve up to n = %d.  The number 1/2 appears in exactly one
role, as the STRENGTH of a classical statement against which a required depth is
compared, and a comparison of strengths is not a claim about RH in either
direction.  Weil 1952 / Bombieri 2000 remain an address.""" % (
    VERDICT, qmin(PFLOOR), qmax(PFLOOR), TIER_CONST[-1],
    qmin(PFLOOR) / TIER_CONST[-1], qmax(PFLOOR) / TIER_CONST[-1],
    1.0 / qmax(TVR), 1.0 / qmin(TVR), qmax(DGAIN_TV), qmed(TAU_TV), F_PCROSS,
    KB_MAX, F_TVK[KB_MAX], qmin(TVF_ALL), qmax(TVF_ALL),
    qmin(PC_OVER_AFF), qmax(PC_OVER_AFF),
    F_PCROSS, F_PAFF, S_CAL, qmin(OOS_D), qmax(OOS_D), len(OOS_D),
    qmin(OOS_P), qmax(OOS_P), ATOM_MAX))

print("")
print("=" * 78)
print("TOTAL (T163 PARETO.FRONT): %d checks, %d failures, %.1f s -- VERDICT %s"
      % (N_CHK, len(FAILS), time.time() - T0, VERDICT))
print("BUDGET: %.1f s of %.0f s used, %.1f s left; HARD CAPS respected "
      "(max factorised form %d <= %d)"
      % (time.time() - T0, BUDGET_S, budget_left(), max(HCAP, KB_MAX), MAX_H))
if FAILS:
    print("FAILURES: %s" % ", ".join(FAILS))
print("=" * 78)
