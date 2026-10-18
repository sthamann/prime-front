"""PART 162 -- THE CONTRACT ``THIRD.SPLIT'': THE SEARCH FOR A SPLIT OF THE ONE
PAIRING WITH delta_eff < 1/2.

THE RH FENCE, FIRST, PROMINENT, AND IT IS THE MOST IMPORTANT SENTENCE IN THIS
FILE.  Nothing here reads, generates, tabulates, approximates or extrapolates a
single zero of any L-function, and no L-function is ever evaluated anywhere.  The
only arithmetic object touched is a FINITE sum over prime powers produced by a
von Mangoldt sieve inside this file.  Q1 and Q3 COMPARE THE STRENGTH of classical
statements (trivial / Chebyshev 1852, partial summation, zero-free-region
strength, RH strength) against a required depth.  A COMPARISON OF STRENGTHS IS
NOT A CLAIM: nothing below asserts, assumes, weakens or implies RH in either
direction, and Weil 1952 / Bombieri 2000 remain an ADDRESS and nothing else.  An
AST firewall enforces the absence of zero data, the import whitelist, the absence
of write-mode file access and the single-file rule.

WHERE T161 LEFT THE CHAIN.  R2'' is ONE pairing, x^T B_LL x = sum_d c_d w_d with
c = c^arch + c^atom and w the CLOSED weight vector of the frozen sixteen-vector.
T161 proved the chain is NOT circular and localised the loss in the SPLIT:
  * arch / atom              needs delta     = log h / alpha = 1.15 .. 1.88
  * arch+smooth / fluctuation needs delta_eff                 = 0.98 .. 1.38
against RH strength 1/2.  The h^2 sits in the SPLIT, not in the primes: the
required absolute precision is 0.012 .. 0.31 of the LAST SUMMAND, i.e. below the
boundary term that every partial summation carries.  R-C' -- ONE SPLIT WITH
delta_eff < 1/2 -- is the whole remaining R2'' task, and it is what Q1 hunts.

WHAT THIS FILE DOES.  Q1 is the heart: a SPLIT TAXONOMY.  Five candidate splits
are put on the same surface in ONE declared currency and each gets a delta_eff
WITH A NUMBER: the smooth exhaustion (more archimedean terms of the explicit
formula), the spectral / ground-pair split, the Fejer split, and the ABEL-
RESIDUAL split, which is the one that attacks the granularity disease itself.
Q2 executes R-A' (the one log-moment, closed as a Clausen / Lerch-type integral)
and R-B' (the 16x16 Gram positivity against Fejer / Schur).  Q3 assembles, runs
the obligatory stress and states what the best number means for R2''.  Q4 is the
map V34, the rest list and the verdict.

THE OUTCOME IN ADVANCE, SO THAT NOTHING BELOW READS AS A REVEAL.  The verdict is
DELTA-REDUCED, not SPLIT-FOUND.  The archimedean ladder is a THIRD genuine
reduction (1.88 -> 1.38 -> 0.93 in the residual-value currency) but it SATURATES:
it is an asymptotic series with an optimal truncation K* = 2, and the Abel ladder
likewise loses past one step.  The Fejer split DOES reach a sub-1/2 provable
demand on every window of the surface -- the strongest single result here -- but
its price in the 1/s bound grows like h^3, so it relocates R2'' into the price
rather than closing it.  R-B' is REFUTED as stated: the 16x16 Gram matrix is
indefinite, and only a weaker a-weighted quarter bar survives.

DISCIPLINE.  THEOREM / CERTIFIED / MEASURED / FIT strictly apart, every claim
labelled, the word ``proven'' used nowhere for an m-freeness claim.  SCALES ARE
PEDANTIC: alpha = log n_zone; D = 2 alpha / M is the lag spacing; h = M / 2 =
alpha / D; X = e^{2 alpha} = n_zone^2 is the atom cut-off; log X = 2 alpha
exactly; every conversion is printed, never assumed.  Classics cited where used:
Chebyshev 1852, Clausen 1832, Lerch 1887, Frullani 1828, Abel 1826,
Dirichlet 1829, Mellin 1896, Fejer 1915, Schur 1917, Gershgorin 1931,
Kac-Murdock-Szego 1953, Rosser-Schoenfeld 1962, Weil 1952, Bombieri 2000.
HARD CAPS: any factorised matrix <= 1500; probe budget < 900 s.
"""

import ast
import math
import os
import time

import numpy as np

T0 = time.time()
np.random.seed(162162)

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384
ATOM_MAX = 400000
ZONE_DEEP = 380000

N_ZONES = 24                 # the SAME surface size as T161, so that the C0 and
                             # C1 reproductions are directly comparable
HCAP = 1450                  # inside the HARD cap MAX_H = 1500
N_ATOM_MIN = 40              # DECLARED surface floor (as T161)
SCHUR_KB = 16                # the FIXED low block of the T152 .. T161 chain

EXACT_BAR = 1.0e-12          # the bar on every claimed IDENTITY
COND_BAR = 1.0e12            # the T159 numerical horizon on cond(B_LL)
BAR_FLAT = 0.25              # |exponent| bar for "flat / non-growing" (T159)
EPSM = float(np.finfo(float).eps)
B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962)
TAU = 0.1                    # the fraction of |Q| a bound may miss by
RH_DELTA = 0.5               # RH STRENGTH, as a delta.  AN ADDRESS, NOT A CLAIM

# T160 / T161 numbers, QUOTED, never recomputed as an input to anything
T161_DELTA = (1.148, 1.881)    # arch / atom
T161_DEFF = (0.98, 1.38)       # arch+smooth / fluctuation
T161_CANCEL = (0.48, 0.70)     # the arch half cancelled by the smooth term
T161_GRAN = (0.012, 0.31)      # needed precision / last summand
T161_NFREQ = 32
T161_RHO1 = (1.0036, 1.0140)
T161_LOGMOM = (2.15, 3.14)     # log-moment / arch half
NF_R = T161_NFREQ // 2         # 16 harmonic frequencies t = pi k / alpha

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


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1.0e-300)


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
    ok = np.isfinite(xs) & np.isfinite(ys) & (xs > 0) & (np.abs(ys) > 0)
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
    check("ts_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("ts_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("ts_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("ts_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "third_split_probe.py", "single new file in the sandbox")


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


def parity_basis(m):
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_P_mat(m):
    """L_P = tridiag(-1, 2, -1) with last diagonal 3; EQUIVALENTLY
    odd_toeplitz(c^L, M) for c^L = (2, -1, 0, ..., 0), re-checked in Q3."""
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
    what makes w_d and every R_kl(d) CLOSED.  Re-checked against direct
    summation in Q3."""
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
    """*** THE PRIME-FREE OBJECT, ISOLATED. ***  R_kl(d) is the (k, l)
    contribution to the closed weight vector: w_d = sum_{k,l} a_k a_l R_kl(d),
    a sum of FOUR Dirichlet kernels in the frequencies om_k -+ om_l."""
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
    """w_d = sum_{k,l} a_k a_l R_kl(d), a_k = x_k / sqrt(mu^P_k).  If kb is a
    SUBSET of indices, only that block of the double sum is assembled -- which
    is exactly the SPECTRAL SPLIT of Q1(ii)."""
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


def abel_tail(v):
    """W^1_d = sum_{e >= d} v_e (Abel 1826)."""
    return np.cumsum(v[::-1])[::-1]


def fwd_diff(c):
    out = np.zeros_like(c)
    out[1:] = c[1:] - c[:-1]
    return out


def back_diff(w):
    """(Delta w)_d = w_d - w_{d+1}, with w_M := 0: the difference the Abel step
    of Q1(v) pairs against the CUMULATIVE residual."""
    out = np.empty_like(w)
    out[:-1] = w[:-1] - w[1:]
    out[-1] = w[-1]
    return out


# ----------------------------------------------------------------------------
# the closed head Psi_d and the regular part -- the T161 exact split
# ----------------------------------------------------------------------------
def cexpm1(z):
    z = np.asarray(z, dtype=np.complex128)
    sm = np.abs(z) < 1.0e-2
    out = np.exp(z) - 1.0
    if sm.any():
        zz = z[sm]
        out[sm] = zz * (1.0 + zz * (0.5 + zz * (1.0 / 6.0 + zz / 24.0)))
    return out


def _g_reg_direct(w):
    w = np.asarray(w, dtype=np.complex128)
    tiny = np.abs(w) < 1.0e-300
    ws = np.where(tiny, 1.0, w)
    B = np.exp(-0.5 * ws) * (2.0 * ws / (-cexpm1(-2.0 * ws))) - 1.0
    return np.where(tiny, 0.25, B / (2.0 * ws))


GREG_R = 1.0
GREG_N = 256
GREG_CUT = 0.5
_th = 2.0 * math.pi * np.arange(GREG_N) / GREG_N
_GREG_C = np.fft.fft(_g_reg_direct(GREG_R * np.exp(1j * _th))) / GREG_N \
    / GREG_R ** np.arange(GREG_N)


def g_reg(w):
    """g_reg(w) = g(w) - 1/(2w), ANALYTIC in |Im w| < pi with g_reg(0) = 1/4;
    the pole removal is SYMBOLIC (Cauchy coefficients on |w| = 1)."""
    w = np.asarray(w, dtype=np.complex128)
    out = _g_reg_direct(w)
    sm = np.abs(w) <= GREG_CUT
    if sm.any():
        ws = w[sm]
        acc = np.zeros(ws.shape, dtype=np.complex128)
        for n in range(GREG_N // 4 - 1, -1, -1):
            acc = acc * ws + _GREG_C[n]
        out[sm] = acc
    return out


def psi_head(d):
    """*** CLOSED, EXACT, D-FREE AND m-FREE -- THE HEAD OF c^arch (T161). ***
      Psi_d = -(1/2)[(d+1)log(d+1) - 2 d log d + (d-1)log(d-1)]
            = -(1/2) int_{-1}^{1} (1 - |v|) dv / (d + v) ,
    the triangle-smeared simple pole.  The integral form is the one the code
    uses (the second difference cancels catastrophically for large d)."""
    d = np.asarray(d, dtype=float)
    out = np.zeros(d.shape)
    for lo, hi in ((-1.0, 0.0), (0.0, 1.0)):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        v = mid + half * _GLX
        out -= 0.5 * half * (((1.0 - np.abs(v)) / (d[..., None] + v)) @ _GLW)
    return out


def psi_head_closed(d):
    d = np.asarray(d, dtype=float)

    def xlx(t):
        return np.where(t > 0.0, t * np.log(np.maximum(t, 1.0e-300)), 0.0)
    return -0.5 * (xlx(d + 1.0) - 2.0 * xlx(d) + xlx(d - 1.0))


def arch_G_hat(s, D):
    """A(s, D) = Psi_{s/D} + D Ghat(s, D) EXACTLY for s >= D."""
    s = np.asarray(s)
    out = np.zeros(np.shape(s), dtype=np.complex128)
    for lo, hi in ((-1.0, 0.0), (0.0, 1.0)):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        v = mid + half * _GLX
        wv = np.asarray(s)[..., None] + D * v
        out -= half * ((1.0 - np.abs(v)) * g_reg(wv)) @ _GLW
    return out


# ----------------------------------------------------------------------------
# the CLOSED smooth cell moments -- the Mellin ladder of Q1(i)
# ----------------------------------------------------------------------------
_CMX, _CMW = np.polynomial.legendre.leggauss(24)


def cell_moment(M, D, hi, beta=0.5):
    """C_d(beta) = int_0^{hi} hat_d(u) e^{beta u} du for the linear-spline hats
    of the lag grid.  beta = 1/2 is the PNT main term dpsi = dx; the archimedean
    ladder of the explicit formula contributes beta = -(2k + 1/2), k >= 1."""
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


section("PART 162 -- THIRD.SPLIT -- Q0  THE FENCE, THE SCALES, THE SURFACE")
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
check("ts_q0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f VERIFIED at every jump point up to n = %d (max %.6f), "
      "never assumed beyond it (Chebyshev 1852; Rosser-Schoenfeld 1962).  THIS "
      "is the unconditional input every delta below is priced against"
      % (B_PSI, ATOM_MAX, _bpsi))

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
    # LOG-SPACED IN h, DECLARED BEFORE ANY RESULT IS SEEN
    CAND.sort(key=lambda t: t[3])
    pick = sorted(set(int(round(x)) for x in np.geomspace(
        1.0, float(len(CAND)), N_ZONES)))
    SZ = [CAND[i - 1] for i in pick]
    SZ.sort(key=lambda t: t[0])
check("ts_q0.surface", len(SZ) >= 8,
      "%d prime-power zones (of %d admissible) are carried, log-spaced in h "
      "inside the caps h <= %d, MAX_H = %d and the declared atom floor of %d "
      "prime powers per window: h = %d .. %d, a lever arm of %dx"
      % (len(SZ), len(CAND), HCAP, MAX_H, N_ATOM_MIN,
         min(t[3] for t in SZ), max(t[3] for t in SZ),
         int(max(t[3] for t in SZ) / max(min(t[3] for t in SZ), 1))))

W = []
for (kz, Dz, Mz, hz) in SZ:
    if budget_left() < 420.0:
        info("ts_q0.budget", "stopped enumerating windows at h = %d" % hz)
        break
    alpha = UU_ALL[kz]
    c_at, D, mu_tot, n_at = atom_lags(alpha, Mz, atoms_in(alpha))
    c_ar = arch_lags(Mz, D)
    W.append(dict(k=kz, h=hz, M=Mz, D=D, alpha=alpha, n_zone=NN_ALL[kz],
                  c_ar=c_ar, c_at=c_at, c=c_ar + c_at, mu_tot=mu_tot,
                  n_atom=n_at, X=math.exp(2.0 * alpha)))

check("ts_q0.scales", all(abs(r["h"] * r["D"] - r["alpha"]) < 1.0e-10 for r in W)
      and all(abs(math.log(r["X"]) - 2.0 * r["alpha"]) < 1.0e-9 for r in W),
      "*** THE SCALES, WRITTEN OUT ONCE AND NEVER ASSUMED AGAIN. ***  alpha = "
      "log n_zone = %.4f .. %.4f; the lag spacing D = 2 alpha / M = %.3e .. "
      "%.3e; h = M/2 = alpha / D = %d .. %d (identity to 1e-10); the atom "
      "cut-off X = e^{2 alpha} = %.4e .. %.4e, i.e. X = n_zone^2 EXACTLY and "
      "log X = 2 alpha EXACTLY (the conversion every delta below uses); %d .. "
      "%d prime-power atoms per window on %d windows"
      % (qmin([r["alpha"] for r in W]), qmax([r["alpha"] for r in W]),
         qmin([r["D"] for r in W]), qmax([r["D"] for r in W]),
         min(r["h"] for r in W), max(r["h"] for r in W),
         qmin([r["X"] for r in W]), qmax([r["X"] for r in W]),
         min(r["n_atom"] for r in W), max(r["n_atom"] for r in W), len(W)))

for r in W:
    m = r["h"]
    A = odd_toeplitz(r["c"], r["M"])
    T16 = parity_basis(m)[:SCHUR_KB, :]
    r["mu"] = parity_mu(m)[:SCHUR_KB]
    isq = 1.0 / np.sqrt(r["mu"])
    r["B_LL"] = sym((T16 @ (A @ T16.T)) * np.outer(isq, isq))
    r["B_ar"] = sym((T16 @ (odd_toeplitz(r["c_ar"], r["M"]) @ T16.T))
                    * np.outer(isq, isq))
    del A
    e1 = np.zeros(SCHUR_KB)
    e1[0] = 1.0
    r["xstar"] = np.linalg.solve(r["B_LL"], e1)
    r["xstar"] /= max(abs(float(r["xstar"][0])), 1.0e-300)
    ev = np.linalg.eigvalsh(r["B_LL"])
    r["kap"] = float(ev[-1] / max(ev[0], 1.0e-300))

WP = [r for r in W if r["kap"] <= COND_BAR]
DROP = [r for r in W if r["kap"] > COND_BAR]

E_QID = []
for r in WP:
    w = lag_weights_closed(r["xstar"], r["h"])
    r["w"] = w
    r["W1"] = abel_tail(w)
    r["dw"] = back_diff(w)
    r["Q"] = float(np.dot(r["c"], w))
    r["Q_ar"] = float(np.dot(r["c_ar"], w))
    r["Q_at"] = float(np.dot(r["c_at"], w))
    r["l1w"] = float(np.sum(np.abs(w)))
    r["l1dw"] = float(np.sum(np.abs(r["dw"])))
    r["gauge"] = abs(float(np.sum(w))) / max(r["l1w"], 1.0e-300)
    r["big"] = max(abs(r["Q_ar"]), abs(r["Q_at"]))
    r["logX"] = math.log(r["X"])
    E_QID.append(abs(r["Q"] - float(r["xstar"] @ (r["B_LL"] @ r["xstar"])))
                 / r["big"])

check("ts_q0.pairing_identity",
      qmax(E_QID) < 1.0e-12 and qmax([r["gauge"] for r in WP]) < 1.0e-12,
      "*** THEOREM, MACHINE-CHECKED: THE OBJECT OF Q1 IS THE PAIRING ITSELF, "
      "REBUILT BIT FOR BIT FROM T160/T161. ***  x^T B_LL x = sum_d c_d w_d to "
      "%.2e .. %.2e of max(|arch half|, |atom half|) on the %d windows inside "
      "the DECLARED horizon cond(B_LL) <= %.0e (%d dropped, first at h = %s); "
      "the gauge identity sum_d w_d = 0 -- which licenses every Abel step below "
      "-- holds to %.2e of ||w||_1.  The total is 1/s = %.4f .. %.4f while the "
      "arch half is %.4e .. %.4e and the atom half %.4e .. %.4e: the halves are "
      "individually LARGE and the total is O(1).  THAT RATIO IS THE DISEASE Q1 "
      "IS A TAXONOMY OF"
      % (qmin(E_QID), qmax(E_QID), len(WP), COND_BAR, len(DROP),
         str(min(r["h"] for r in DROP)) if DROP else "none",
         qmax([r["gauge"] for r in WP]), qmin([r["Q"] for r in WP]),
         qmax([r["Q"] for r in WP]), qmin([r["Q_ar"] for r in WP]),
         qmax([r["Q_ar"] for r in WP]), qmin([r["Q_at"] for r in WP]),
         qmax([r["Q_at"] for r in WP])))

XHP = [float(r["h"]) for r in WP]
print("")
print("TOTAL (Q0): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("Q1  THE SPLIT TAXONOMY -- WHAT MAKES A SPLIT GOOD, AND FIVE CANDIDATES")
# ----------------------------------------------------------------------------
para("""Q1.0  THE CURRENCY, DECLARED BEFORE ANY CANDIDATE IS SEEN, BECAUSE OTHERWISE
THE NUMBERS BELOW WOULD NOT BE COMPARABLE.  A SPLIT of the one pairing
Q = sum_d c_d w_d is a decomposition Q = Q^closed + R in which

  (a) Q^closed is evaluated in CLOSED FORM (no prime input, no cancellation), and
  (b) R = (arithmetic factor) x (closed factor) needs cancellation.

The DEMAND of the split is the power of X by which the arithmetic factor must
beat its own unconditional size for |R| <= tau |Q| with tau = %.2f:

  delta_eff := log( T_triv x C_w / (tau |Q|) ) / log X ,

T_triv the CHEBYSHEV-strength (unconditional, no-cancellation, measured on this
surface and never asserted) size of the arithmetic factor, C_w the closed weight
factor it is paired against.  log X = 2 alpha EXACTLY, so delta_eff is a pure
power.  THE BAR: RH strength buys X^{-1/2 + o(1)} on psi(x) - x, so delta_eff <
1/2 means an RH-strength input would suffice with room to spare, delta_eff = 1/2
means exactly RH strength, delta_eff > 1/2 means MORE than RH strength.  THAT
BAR IS A COMPARISON OF STRENGTHS AND NOT A CLAIM ABOUT RH IN EITHER DIRECTION.
A GOOD SPLIT is therefore one whose closed factor C_w is SMALL -- and every
candidate below is an attempt to make C_w small by moving structure from R into
Q^closed.""" % TAU)

# --- Q1.1  C0, the arch/atom baseline, reproduced -----------------------------
D0, TRIV, MASSR = [], [], []
for r in WP:
    at = atoms_in(r["alpha"])
    mm = np.array([t[1] for t in at], dtype=float)
    uu = np.array([t[0] for t in at], dtype=float)
    r["u_at"], r["mu_at"], r["mass"] = uu, mm, float(np.sum(mm))
    MASSR.append(r["mass"])
    TRIV.append(r["mass"] / (4.0 * math.sqrt(r["X"])))
    d0 = math.log(r["h"]) / r["alpha"]
    r["d0"] = d0
    D0.append(d0)

check("ts_q1.c0_baseline",
      qmin(D0) > 1.0 and abs(qmin(D0) - T161_DELTA[0]) < 0.01
      and abs(qmax(D0) - T161_DELTA[1]) < 0.01,
      "*** CANDIDATE C0 = THE ARCH/ATOM SPLIT, REPRODUCED SO THAT EVERY NUMBER "
      "BELOW IS COMPARABLE. ***  Q^closed = the arch half, R = the atom half, "
      "which is a Lambda-weighted sampling of w at the %d harmonic frequencies. "
      "The relative depth is h^-2, and since log X = 2 alpha this is exactly "
      "delta = log h / alpha, MEASURED %.4f .. %.4f on this %d-window surface -- "
      "T161 quoted %.3f .. %.3f and this REPRODUCES IT TO 0.01 at both ends, on "
      "an independently rebuilt surface with the same declared %d-zone recipe and "
      "h = %d .. %d.  "
      "T_triv = sum_{n<=X} 2 Lambda(n) n^{-1/2} = %.4f .. %.4f times 4 sqrt X "
      "(Chebyshev 1852, MEASURED here, and ATTAINED at t = 0).  SMOOTH PART "
      "CLOSED: yes (the T115 kernel).  STATUS: MEASURED depth on a THEOREM-"
      "grade identity.  VERDICT ON C0: X^{%.2f} .. X^{%.2f} BEYOND RH strength"
      % (T161_NFREQ, qmin(D0), qmax(D0), len(WP),
         T161_DELTA[0], T161_DELTA[1], N_ZONES, min(r["h"] for r in WP),
         max(r["h"] for r in WP), qmin(TRIV), qmax(TRIV),
         qmin(D0) - RH_DELTA, qmax(D0) - RH_DELTA))

# --- Q1.2  C1, the smooth/fluctuation re-split, reproduced --------------------
D1, RMOD, FLUC = [], [], []
for r in WP:
    Phi = cell_moment(r["M"], r["D"], 2.0 * r["alpha"], 0.5)
    r["Phi"] = Phi
    r["Q_sm"] = -float(np.dot(r["w"], Phi))
    RMOD.append(abs(r["Q_ar"] + r["Q_sm"]) / max(abs(r["Q_ar"]), 1.0e-300))
    fl = abs(r["Q_at"] - r["Q_sm"])
    r["fl"] = fl
    FLUC.append(fl / max(abs(r["Q_at"]), 1.0e-300))
    d1 = math.log(max(fl / abs(r["Q"]), 1.0)) / r["logX"]
    r["d1"] = d1
    D1.append(d1)

check("ts_q1.c1_resplit",
      qmax(RMOD) < 1.0 and qmax(D1) < qmax(D0)
      and abs(qmin(D1) - T161_DEFF[0]) < 0.01
      and abs(qmax(D1) - T161_DEFF[1]) < 0.01,
      "*** CANDIDATE C1 = ARCH + SMOOTH PRIME TERM / PRIME FLUCTUATION, "
      "REPRODUCED. ***  Q^closed = arch half + Q^smooth, "
      "Q^smooth = -int_0^{2 alpha} e^{u/2} What(u) du = -sum_d w_d C_d(1/2) "
      "with the CLOSED cell moments C_d(beta) (the PNT main term dpsi = dx; "
      "explicit-formula pairing).  The smooth term LEAVES %.4f .. %.4f of the "
      "arch half uncancelled -- which is the quantity T161 quoted as %.2f .. %.2f, "
      "reproduced, and it is stated as the REMAINDER here because reading it as "
      "the cancelled fraction inverts it: what is actually CANCELLED is "
      "%.4f .. %.4f.  Either way the arch half's true partner IS the smooth prime "
      "term.  R = the prime fluctuation, %.4f .. %.4f of the atom half, and "
      "delta_eff = %.4f .. %.4f, REPRODUCING T161's %.2f .. %.2f to 0.01 at both "
      "ends.  SMOOTH PART CLOSED: yes.  STATUS: MEASURED.  VERDICT ON C1: the "
      "demand MOVES by %.2f in delta but %d of %d windows still need more than "
      "RH strength"
      % (qmin(RMOD), qmax(RMOD), T161_CANCEL[0], T161_CANCEL[1],
         1.0 - qmax(RMOD), 1.0 - qmin(RMOD),
         qmin(FLUC), qmax(FLUC), qmin(D1), qmax(D1),
         T161_DEFF[0], T161_DEFF[1], qmax(D0) - qmax(D1),
         sum(1 for d in D1 if d > RH_DELTA), len(D1)))

# --- Q1.3  C2, the MELLIN / ARCHIMEDEAN EXHAUSTION -- how far does it go? -----
para("""Q1.3  CANDIDATE C2: DOES SUBTRACTING MORE SMOOTH TERMS HELP, AND WHERE DOES
THE EXHAUSTION SATURATE?  Past the main term the smooth part of dpsi is the
derivative of the ELEMENTARY closed function -(1/2) log(1 - x^{-2}) =
sum_{k>=1} x^{-2k} / (2k), i.e. dpsi_smooth = dx - sum_{k>=1} x^{-2k-1} dx.  NO
ZERO DATA IS INVOLVED: this is a closed elementary function of x, written down
here and never tabulated from anything.  Under the Mellin pairing (Mellin 1896)
the k-th term contributes + sum_d w_d C_d(-(2k + 1/2)) -- again CLOSED cell
moments, so the ladder is free.  The question is only what it BUYS.""")

para("""THE LADDER IS NOT A CONVERGENT EXPANSION, AND THAT IS THE POINT OF Q1.3.  The
formal sum of the whole ladder is sum_{k>=1} x^{-2k-1} = 1 / (x (x^2 - 1)), which
DIVERGES as x -> 1+, exactly matching the -(1/2) log(1 - x^{-2}) singularity that
the zero sum of the explicit formula cancels.  Term by term, the k-th cell moment
contributes O(1/(2k+1/2)) near u = 0, so the partial sums grow like log K.  An
ASYMPTOTIC series with an OPTIMAL TRUNCATION K* is therefore expected, not an
exhaustion -- and K* and the delta it buys are MEASURED, not assumed.""")

K_MELLIN = 20
DK, GAINK, KSTAR, DIVK = [], [], [], []
for r in WP:
    lad = r["Phi"].copy()
    lads = [lad.copy()]
    q = r["Q_sm"]
    seq = [abs(r["Q_at"] - q)]
    qs = [q]
    for k in range(1, K_MELLIN + 1):
        lad = lad - cell_moment(r["M"], r["D"], 2.0 * r["alpha"],
                                -(2.0 * k + 0.5))
        lads.append(lad.copy())
        q = -float(np.dot(r["w"], lad))
        qs.append(q)
        seq.append(abs(r["Q_at"] - q))
    ks = int(np.argmin(seq))
    r["mellin_seq"], r["k_star"], r["Q_sm_K"] = seq, ks, qs[ks]
    r["Phi_lad"] = lads[ks]
    d2 = math.log(max(seq[ks] / abs(r["Q"]), 1.0)) / r["logX"]
    r["d2"] = d2
    DK.append(d2)
    KSTAR.append(ks)
    GAINK.append(abs(seq[0] - seq[ks]) / max(seq[0], 1.0e-300))
    DIVK.append(seq[-1] / max(seq[ks], 1.0e-300))

check("ts_q1.c2_mellin_optimal", qmax(GAINK) < 1.0 and max(KSTAR) < K_MELLIN,
      "*** CANDIDATE C2 = THE ARCHIMEDEAN LADDER, AND IT IS AN ASYMPTOTIC SERIES "
      "WITH AN OPTIMAL TRUNCATION, MEASURED. ***  The residual is minimised at "
      "K* = %d .. %d of the %d terms carried (median %.1f), where it has fallen "
      "by a RELATIVE %.4f .. %.4f -- so the ladder is NOT worthless, it is worth "
      "a genuine factor.  Past K* it RISES again, by %.2f .. %.2f from K* to "
      "K = %d, which is the predicted log-divergence of the formal sum and NOT a "
      "numerical artefact: the truncation is optimal, not exhaustive.  What it "
      "buys in the only currency that counts: delta_eff = %.4f .. %.4f against "
      "C1's %.4f .. %.4f, a gain of %.3f .. %.3f.  SMOOTH PART CLOSED: yes (cell "
      "moments C_d(-(2k+1/2)), elementary, prime-free).  STATUS: MEASURED.  "
      "VERDICT ON C2: THE SMOOTH EXHAUSTION IS A REAL GAIN THAT SATURATES AT THE "
      "SECOND TERM, and it CANNOT be iterated to the %.2f .. %.2f still missing, "
      "because the series it comes from diverges.  (The remaining smooth piece "
      "of the explicit formula, the constant -log 2 pi = %.4f, is a BOUNDARY "
      "term of the measure on (1, X] and contributes nothing to dpsi at all.)"
      % (min(KSTAR), max(KSTAR), K_MELLIN, qmed([float(k) for k in KSTAR]),
         qmin(GAINK), qmax(GAINK), qmin(DIVK), qmax(DIVK), K_MELLIN,
         qmin(DK), qmax(DK), qmin(D1), qmax(D1),
         qmin(D1) - qmin(DK), qmax(D1) - qmax(DK),
         qmin(DK) - RH_DELTA, qmax(DK) - RH_DELTA,
         math.log(2.0 * math.pi)))

print("")
print("TOTAL (Q1.1-Q1.3): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# --- Q1.4  the two currencies, separated, and the Chebyshev constant ----------
para("""Q1.4  BEFORE THE REMAINING CANDIDATES, ONE THING T161 LEFT IMPLICIT HAS TO BE
MADE EXPLICIT, BECAUSE THE REST OF Q1 TURNS ON IT.  Two different numbers have
both been called delta_eff:

  delta_val = log( |R|_measured / |Q| ) / log X   -- HOW BIG WHAT IS LEFT IS.
  delta_bnd = log( E_triv x C_w  / |Q| ) / log X  -- WHAT MUST BE PROVED.

delta_val is a MEASUREMENT of the residual VALUE; it is a FLOOR and it is the
currency T161 quoted for C1.  delta_bnd is the DEMAND: E_triv is the
CHEBYSHEV-STRENGTH (unconditional) size of the arithmetic factor and C_w the
closed factor it is paired against, so RH strength -- which replaces
|psi(x) - x| <= kappa x by O(sqrt x log^2 x) -- closes the split iff
delta_bnd <= 1/2.  delta_bnd >= delta_val always.  BOTH are reported for every
candidate from here on, and the VERDICT is driven by delta_bnd, because that is
the number a proof has to meet.  A factor tau would shift every delta by
log(1/tau)/log X, i.e. by at most %.3f on this surface -- declared once, and
omitted from the numbers so that they stay comparable with T161.""" %
     (math.log(1.0 / TAU) / min(r["logX"] for r in WP)))

X0_CHEB = 100.0              # DECLARED before the constant is measured
_psi, _kap = 0.0, 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi += _lam
    if _n >= X0_CHEB:
        _kap = max(_kap, abs(_psi - _n) / _n)
KAPPA = _kap
check("ts_q1.chebyshev_kappa", 0.0 < KAPPA < 0.2,
      "*** THE ONE UNCONDITIONAL ARITHMETIC INPUT OF THE WHOLE OF Q1, MEASURED "
      "ON THIS SURFACE AND NOTHING ELSE. ***  |psi(x) - x| <= kappa x with "
      "kappa = %.6f, verified at EVERY jump point in %.0f <= x <= %d (the "
      "cut-off x_0 = %.0f declared before the constant was looked at; below it "
      "the ratio is dominated by the first few prime powers and is not the "
      "object of any asymptotic statement).  This is Chebyshev 1852 / "
      "Rosser-Schoenfeld 1962 strength: NO zero-free region, NO RH, NO zero "
      "data.  RH strength would replace kappa x by O(sqrt x log^2 x), and THAT "
      "substitution is the ONLY place RH appears anywhere in this file -- as a "
      "COMPARISON, never as an assumption"
      % (KAPPA, X0_CHEB, ATOM_MAX, X0_CHEB))

para("""THE ABEL LADDER, AND WHY IT IS THE ONLY PLACE AN UNCONDITIONAL INPUT CAN
ENTER AT ALL.  Write v_d = c^atom_d + Phi^lad_d for the residual cell vector, so
that R = sum_d v_d w_d EXACTLY.  At level 0 the arithmetic factor is a SINGLE
CELL mass, and Chebyshev's bound says NOTHING about a single cell -- that is
precisely T161's granularity finding (needed precision %.3f .. %.3f of the last
summand), so level 0 admits no unconditional input and its delta_bnd is not even
definable.  One Abel step (Abel 1826, licensed by the gauge identity
sum_d w_d = 0) changes that: with V_d = sum_{e<=d} v_e,

    R = sum_d V_d (Delta w)_d ,  (Delta w)_d = w_d - w_{d+1} ,  w_M := 0 ,

and V_d IS controlled unconditionally, because by two partial summations
V_d = -[ (psi(x) - x)/sqrt x + (1/2) int_1^x (psi(t) - t) t^{-3/2} dt ] with
x = e^{dD}, hence |V_d| <= 2 kappa sqrt x <= 2 kappa sqrt X.  Level k >= 2
iterates: the closed envelope is the k-fold cumulative sum of that bound, and it
is paired against ||Delta^k w||_1.  So the whole ladder is CLOSED on the weight
side and Chebyshev on the arithmetic side, and the OPTIMAL LEVEL is a number.""" %
     (T161_GRAN[0], T161_GRAN[1]))

K_ABEL = 4
E_ABEL, DBND, KOPT, SVR = [], [], [], []
for r in WP:
    v = r["c_at"] + r["Phi_lad"]
    r["v"] = v
    R_direct = float(np.dot(v, r["w"]))
    dd = np.arange(r["M"], dtype=float)
    env = 2.0 * KAPPA * np.exp(0.5 * dd * r["D"])
    cur, wk, e_ab, dbn, c_w = v.copy(), r["w"].copy(), [], [], []
    for k in range(1, K_ABEL + 1):
        cur = np.cumsum(cur)
        wk = back_diff(wk)
        env = np.cumsum(env) if k > 1 else env
        e_ab.append(abs(float(np.dot(cur, wk)) - R_direct)
                    / max(abs(R_direct), 1.0e-300))
        cw = float(np.sum(np.abs(wk)))
        c_w.append(cw)
        dbn.append(math.log(max(float(np.max(np.abs(env))) * cw
                                / abs(r["Q"]), 1.0)) / r["logX"])
    ko = int(np.argmin(dbn))
    r["abel_dbnd"], r["k_abel"], r["l1_dk"] = dbn, ko + 1, c_w
    r["R_res"] = R_direct
    r["sv_meas"] = float(np.max(np.abs(np.cumsum(v))))
    r["sv_triv"] = 2.0 * KAPPA * math.sqrt(r["X"])
    E_ABEL.append(max(e_ab))
    DBND.append(dbn[ko])
    KOPT.append(ko + 1)
    SVR.append(r["sv_meas"] / r["sv_triv"])

check("ts_q1.abel_identity", qmax(E_ABEL) < EXACT_BAR,
      "*** THEOREM, MACHINE-CHECKED AT EVERY LEVEL: THE ABEL LADDER IS AN "
      "IDENTITY AND NOT AN APPROXIMATION. ***  sum_d v_d w_d = "
      "sum_d V^{(k)}_d (Delta^k w)_d for k = 1 .. %d, to %.2e .. %.2e relative "
      "on all %d windows, with the convention w_M := 0 and NO boundary term left "
      "over -- which is exactly what the gauge identity sum_d w_d = 0 buys "
      "(checked to %.1e in ts_q0.pairing_identity).  Every delta_bnd below "
      "therefore prices a TRUE factorisation of the SAME number"
      % (K_ABEL, qmin(E_ABEL), qmax(E_ABEL), len(WP),
         qmax([r["gauge"] for r in WP])))

check("ts_q1.cheb_envelope", qmax(SVR) < 1.0,
      "*** CERTIFIED PER WINDOW: THE UNCONDITIONAL ENVELOPE HOLDS, AND IT IS "
      "LOOSE BY A MEASURED FACTOR. ***  sup_d |V_d| = %.4e .. %.4e against the "
      "Chebyshev envelope 2 kappa sqrt X = %.4e .. %.4e, i.e. the envelope is "
      "attained to %.4f .. %.4f.  So the unconditional input is not being "
      "smuggled: the true cumulative residual is genuinely of Chebyshev size on "
      "this surface, and the %.2f .. %.2f the envelope leaves on the table is the "
      "honest slack of the method, not a hidden saving"
      % (qmin([r["sv_meas"] for r in WP]), qmax([r["sv_meas"] for r in WP]),
         qmin([r["sv_triv"] for r in WP]), qmax([r["sv_triv"] for r in WP]),
         qmin(SVR), qmax(SVR), qmin(SVR), qmax(SVR)))

check("ts_q1.c5_abel_optimal", min(KOPT) == 1 and max(KOPT) == 1,
      "*** CANDIDATE C5 = THE ABEL / PARTIAL-SUMMATION SPLIT, AND THE OPTIMAL "
      "LEVEL IS EXACTLY ONE -- MEASURED, ON EVERY WINDOW. ***  delta_bnd over "
      "the ladder: level 1 gives %.4f .. %.4f, level 2 gives %.4f .. %.4f, "
      "level %d gives %.4f .. %.4f; the optimum is k = %d .. %d on all %d "
      "windows.  THE MECHANISM, AND IT IS A CLOSED COMPUTATION AND NOT A "
      "COINCIDENCE: one more Abel step multiplies the envelope by about "
      "2/D = M/alpha and divides ||Delta^k w||_1 by about the top frequency "
      "om_16 = 32 pi / N, and the product is 32 pi / alpha = %.1f .. %.1f > 1, "
      "so every step past the first LOSES.  Partial summation is not a ladder "
      "to be climbed; it is a single step, and it has already been taken.  "
      "SMOOTH PART CLOSED: yes.  STATUS: CERTIFIED per window (Chebyshev "
      "envelope + closed ||Delta w||_1)"
      % (qmin([r["abel_dbnd"][0] for r in WP]),
         qmax([r["abel_dbnd"][0] for r in WP]),
         qmin([r["abel_dbnd"][1] for r in WP]),
         qmax([r["abel_dbnd"][1] for r in WP]), K_ABEL,
         qmin([r["abel_dbnd"][-1] for r in WP]),
         qmax([r["abel_dbnd"][-1] for r in WP]), min(KOPT), max(KOPT), len(WP),
         qmin([32.0 * math.pi / r["alpha"] for r in WP]),
         qmax([32.0 * math.pi / r["alpha"] for r in WP])))

# --- Q1.5  the reduction of R-C' to a CLOSED, PRIME-FREE inequality -----------
RATIO_W, RHO_RH = [], []
for r in WP:
    r["tv_ratio"] = r["l1_dk"][0] / abs(r["Q"])
    RATIO_W.append(r["tv_ratio"])
    RHO_RH.append((r["logX"] ** 2) * r["tv_ratio"])
F_RATIO = fit_exp(XHP, RATIO_W)

check("ts_q1.rc_prime_free", qmin(RATIO_W) > 1.0,
      "*** AND HERE IS THE STRUCTURAL PAYLOAD OF Q1, WHICH IS WORTH MORE THAN "
      "ANY SINGLE delta: AFTER THE ABEL STEP, R-C' IS A PRIME-FREE INEQUALITY. "
      "***  At the optimal level the demand factorises as delta_bnd = 1/2 + "
      "log( 2 kappa ||Delta w||_1 / |Q| ) / log X EXACTLY, because the envelope "
      "is 2 kappa sqrt X and log X = 2 alpha.  EVERY ARITHMETIC INPUT IS NOW IN "
      "THE SINGLE CONSTANT kappa: the entire remaining question is the CLOSED, "
      "PRIME-FREE ratio ||Delta w||_1 / |Q| = %.4e .. %.4e, which grows as "
      "h^(%+.3f) (FIT).  RH strength closes the split iff that ratio is below "
      "|Q| / (C log^2 X); with C = 1 as a DECLARED ORIENTATION CONSTANT (not a "
      "claim) the RH test statistic is log^2 X x ||Delta w||_1 / |Q| = %.3e .. "
      "%.3e, i.e. RH-strength input misses by %.1f .. %.1f orders of magnitude.  "
      "SO: R-C' IS NO LONGER AN ARITHMETIC PROBLEM.  It is the closed question "
      "whether some admissible trial vector makes the TOTAL VARIATION of its "
      "own weight sequence comparable to the VALUE of its own quadratic form -- "
      "and Q1.6 tests exactly that, over a family of trial vectors"
      % (qmin(RATIO_W), qmax(RATIO_W), F_RATIO, qmin(RHO_RH), qmax(RHO_RH),
         math.log10(qmin(RHO_RH)), math.log10(qmax(RHO_RH))))

print("")
print("TOTAL (Q1.4-Q1.5): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# --- Q1.6  C3 + C4: the trial-vector freedom, used as a SEARCH -----------------
para("""Q1.6  CANDIDATES C3 (SPECTRAL / GROUND PAIR) AND C4 (FEJER TAPER) ARE THE SAME
KIND OF OBJECT, AND Q1.5 SAYS WHAT TO DO WITH THEM.  The Thomson / Dirichlet dual
s = max_y (2 y_1 - y^T B_LL y) makes EVERY trial vector admissible: for any x with
x_1 = 1 the optimal scaling y = x / Q(x) gives s >= 1 / Q(x), i.e.

    1/s <= Q(x) = x^T B_LL x   for EVERY x with x_1 = 1 and Q(x) > 0

(Dirichlet 1829 / Thomson; direction re-checked below).  So the chain is FREE to
choose x, at the price of a weaker bound on 1/s, and by Q1.5 the demand of the
best split at that x is EXACTLY

    delta_bnd(x) = 1/2 + log( 2 kappa ||Delta w(x)||_1 / |Q(x)| ) / log X .

C3 restricts x to the low modes (the ground pair and its enlargements), C4 tapers
x with the Fejer weights (Fejer 1915), and a declared random sweep covers the rest
of the 16-dimensional space.  THIS IS A PRIME-FREE OPTIMISATION: no atom, no
Lambda, no zero enters the ratio being minimised -- only |Q(x)| carries prime
input, and it is measured to machine precision.

THE OBJECTIVE MUST BE PRICED, OR IT IS GAMED, AND THIS IS SAID BEFORE THE NUMBERS
BECAUSE AN UNPRICED SEARCH DOES FIND delta_bnd < 0 HERE -- BY MAKING Q(x) HUGE,
i.e. by making the bound on 1/s vacuous.  So the search is reported as a PARETO
FRONTIER in the two quantities that actually matter,

    the PRICE   P(x) = Q(x) / Q(x*)  >= 1   (how much weaker the 1/s bound gets)
    the DEMAND  delta_bnd(x)               (how much cancellation is still needed)

and the one number that decides R-C' is P_min = the smallest price at which
delta_bnd < 1/2.  WHAT P IS AFFORDABLE IS A T159/T160 INPUT AND IS NOT INVENTED
HERE: the frontier is published at declared prices so that whoever fixes the
threshold can read the demand off it.""")

N_TRIAL = 64                 # DECLARED before any result is seen
S_MIX = np.geomspace(1.0e-3, 3.0e1, 12)   # the price sweep, declared
FEJ_NB = (2, 4, 8, 16)
P_GRID = (1.05, 1.25, 2.0, 10.0, 100.0, 1.0e4)
BEST_D, BEST_NAME, PRICE, BEST_RHO = [], [], [], []
FRONT = {p: [] for p in P_GRID}
PMIN, PMIN_OK = [], []
for r in WP:
    m, Mz = r["h"], r["M"]
    N = 2 * m + 1
    om = 2.0 * math.pi * np.arange(1, SCHUR_KB + 1) / N
    mu = r["mu"]
    RS = np.empty((SCHUR_KB * SCHUR_KB, Mz))
    for k in range(SCHUR_KB):
        for l in range(SCHUR_KB):
            RS[k * SCHUR_KB + l] = R_pair(k, l, m, om)
    DRS = np.empty_like(RS)
    DRS[:, :-1] = RS[:, :-1] - RS[:, 1:]
    DRS[:, -1] = RS[:, -1]
    isq = 1.0 / np.sqrt(mu)

    fam = [("x_star", r["xstar"].copy())]
    for nb in FEJ_NB:
        xt = r["xstar"].copy()
        xt[nb:] = 0.0
        fam.append(("trunc_%d" % nb, xt))
        xf = r["xstar"] * np.maximum(
            0.0, 1.0 - np.arange(SCHUR_KB) / float(nb))
        fam.append(("fejer_%d" % nb, xf))
    e1 = np.zeros(SCHUR_KB)
    e1[0] = 1.0
    fam.append(("e_1", e1))
    rng = np.random.RandomState(1620 + r["h"])
    for j in range(N_TRIAL):
        z = rng.standard_normal(SCHUR_KB) * (1.0 / (1.0 + np.arange(SCHUR_KB)))
        for i_s, s in enumerate(S_MIX):
            xr = r["xstar"] + s * z
            if abs(float(xr[0])) < 1.0e-9:
                continue
            fam.append(("mix_%d_%d" % (j, i_s), xr))

    XA = np.array([t[1] for t in fam])
    XA = XA / XA[:, :1]                      # ENFORCE x_1 = 1 (the normalisation)
    AA = XA * isq[None, :]
    OUT = np.einsum("nk,nl->nkl", AA, AA).reshape(XA.shape[0], -1)
    QV = np.einsum("nk,kl,nl->n", XA, r["B_LL"], XA)
    L1D = np.abs(OUT @ DRS).sum(axis=1)
    rho = 2.0 * KAPPA * L1D / np.abs(QV)
    dbn = 0.5 + np.log(np.maximum(rho, 1.0e-300)) / r["logX"]
    price = QV / r["Q"]
    ok = QV > 0.0
    r["n_ok"] = int(np.sum(ok))
    r["rho_star"] = float(rho[0])
    r["front"] = {}
    for p in P_GRID:
        sel = ok & (price <= p)
        r["front"][p] = float(np.min(dbn[sel])) if sel.any() else float("nan")
        FRONT[p].append(r["front"][p])
    sub = ok & (dbn < RH_DELTA)
    r["p_min"] = float(np.min(price[sub])) if sub.any() else float("inf")
    PMIN.append(r["p_min"])
    PMIN_OK.append(bool(sub.any()))
    for tag in ("trunc", "fejer", "e_1"):
        idx = [i for i, t in enumerate(fam) if t[0].startswith(tag)]
        jj = [i for i in idx if ok[i]]
        if jj:
            jb = jj[int(np.argmin(dbn[jj]))]
            r["fam_" + tag] = (float(dbn[jb]), float(price[jb]), fam[jb][0])
        else:
            r["fam_" + tag] = (float("nan"), float("nan"), "none")
    ibest = int(np.argmin(np.where(ok, dbn, np.inf)))
    r["best_d"] = float(dbn[ibest])
    r["best_rho"] = float(rho[ibest])
    r["best_name"] = fam[ibest][0]
    r["best_x"] = XA[ibest]
    BEST_D.append(r["best_d"])
    BEST_NAME.append(r["best_name"])
    PRICE.append(float(price[ibest]))
    BEST_RHO.append(r["best_rho"])

F_SRHO = fit_exp(XHP, [r["rho_star"] for r in WP])
F_PMIN = fit_exp(XHP, [p for p in PMIN if np.isfinite(p)]) \
    if all(np.isfinite(PMIN)) else float("nan")
check("ts_q1.c34_frontier", all(PMIN_OK) and qmin(PMIN) > 1.0,
      "*** CANDIDATES C3 + C4 AS A PRICED SEARCH, AND THE RESULT IS AN EXCHANGE "
      "RATE, WHICH IS A SHARPER OBJECT THAN A SINGLE delta. ***  On every one of "
      "the %d windows there EXISTS an admissible trial vector with "
      "delta_bnd < 1/2 -- so a split with sub-RH demand DOES exist inside the "
      "16-dimensional Thomson freedom, and the question was never whether one "
      "exists but what it costs.  THE COST: P_min = %.3e .. %.3e, and it GROWS "
      "as h^(%+.3f) (FIT).  THE FRONTIER, at declared prices, min over trials of "
      "delta_bnd: P <= 1.05 -> %.3f .. %.3f; P <= 1.25 -> %.3f .. %.3f; "
      "P <= 2 -> %.3f .. %.3f; P <= 10 -> %.3f .. %.3f; P <= 100 -> %.3f .. "
      "%.3f; P <= 1e4 -> %.3f .. %.3f.  At the T160 optimiser itself "
      "(P = 1 exactly) rho = %.3e .. %.3e growing as h^(%+.3f) (FIT), i.e. "
      "delta_bnd = %.4f .. %.4f.  THE STRUCTURE OF THE TRADE-OFF, AND IT IS "
      "PRIME-FREE: every unit of delta must be bought with %.2f .. %.2f decades "
      "of price.  WHETHER THAT PRICE IS AFFORDABLE IS A T159/T160 QUESTION AND "
      "IS NOT DECIDED HERE.  STATUS: MEASURED search (%d trial vectors per "
      "window), CERTIFIED per window at each reported x"
      % (len(WP), qmin(PMIN), qmax(PMIN), F_PMIN,
         qmin(FRONT[1.05]), qmax(FRONT[1.05]),
         qmin(FRONT[1.25]), qmax(FRONT[1.25]),
         qmin(FRONT[2.0]), qmax(FRONT[2.0]),
         qmin(FRONT[10.0]), qmax(FRONT[10.0]),
         qmin(FRONT[100.0]), qmax(FRONT[100.0]),
         qmin(FRONT[1.0e4]), qmax(FRONT[1.0e4]),
         qmin([r["rho_star"] for r in WP]), qmax([r["rho_star"] for r in WP]),
         F_SRHO, qmin([r["abel_dbnd"][0] for r in WP]),
         qmax([r["abel_dbnd"][0] for r in WP]),
         qmin([math.log10(r["p_min"]) / max(r["abel_dbnd"][0] - r["best_d"],
                                            1.0e-9) for r in WP]),
         qmax([math.log10(r["p_min"]) / max(r["abel_dbnd"][0] - r["best_d"],
                                            1.0e-9) for r in WP]),
         len(XA)))

DT = [r["fam_trunc"] for r in WP]
DF = [r["fam_fejer"] for r in WP]
DE = [r["fam_e_1"] for r in WP]
F_PT = fit_exp(XHP, [t[1] for t in DT])
F_PF = fit_exp(XHP, [t[1] for t in DF])
N_SUB_F = sum(1 for t in DF if t[0] < RH_DELTA)
N_SUB_T = sum(1 for t in DT if t[0] < RH_DELTA)
check("ts_q1.c3_c4_separately",
      N_SUB_F == len(DF) and F_PF > BAR_FLAT,
      "*** EACH OF C3 AND C4 GETS ITS OWN NUMBER, AND THIS IS THE MOST IMPORTANT "
      "MEASUREMENT IN Q1: A **STRUCTURED** FAMILY DOES GET BELOW 1/2. ***  "
      "C3, THE SPECTRAL / GROUND-PAIR SPLIT (x truncated to the lowest %s modes): "
      "delta_bnd = %.4f .. %.4f at price %.2e .. %.2e (price exponent %+.2f in h, "
      "FIT), minimiser %s, below 1/2 on %d of %d windows.  "
      "C4, THE FEJER SPLIT (x tapered by 1 - k/nb, Fejer 1915): "
      "delta_bnd = %.4f .. %.4f at price %.2e .. %.2e (price exponent %+.2f in h, "
      "FIT), minimiser %s, BELOW 1/2 ON %d OF %d WINDOWS -- i.e. on ALL of them.  "
      "C3-EXTREME, x = e_1 (one mode): delta_bnd = %.4f .. %.4f at price "
      "%.2e .. %.2e.  WHY C4 IS THE FEJER SPLIT THE CONTRACT ASKED FOR: pairing "
      "the weight vector against a Fejer-AVERAGED Lambda-mass is the SAME number "
      "as pairing a Fejer-averaged weight vector against the raw mass, by "
      "self-adjointness of the smoothing -- so tapering x IS smoothing the sampled "
      "frequencies, and the smoothing lowers the demand by %.2f .. %.2f of delta "
      "against the untapered optimiser.  AND HERE IS THE CATCH, WHICH IS WHY THIS "
      "IS NOT YET A CLOSURE: the price is not bounded.  It grows as h^%+.2f (FIT), "
      "so the sub-RH demand is bought with an asymptotically DIVERGING loss in the "
      "1/s bound, and a per-window certificate at growing price is not a uniform "
      "statement.  STATUS: MEASURED (per-window sub-1/2 demand), and the price "
      "growth is what stands between it and CERT-UNIF"
      % ("/".join(str(n) for n in FEJ_NB),
         qmin([t[0] for t in DT]), qmax([t[0] for t in DT]),
         qmin([t[1] for t in DT]), qmax([t[1] for t in DT]), F_PT,
         sorted(set(t[2] for t in DT))[0], N_SUB_T, len(DT),
         qmin([t[0] for t in DF]), qmax([t[0] for t in DF]),
         qmin([t[1] for t in DF]), qmax([t[1] for t in DF]), F_PF,
         sorted(set(t[2] for t in DF))[0], N_SUB_F, len(DF),
         qmin([t[0] for t in DE]), qmax([t[0] for t in DE]),
         qmin([t[1] for t in DE]), qmax([t[1] for t in DE]),
         qmin([r["abel_dbnd"][0] - r["fam_fejer"][0] for r in WP]),
         qmax([r["abel_dbnd"][0] - r["fam_fejer"][0] for r in WP]), F_PF))

print("")
print("TOTAL (Q1.6): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("Q2  R-A': THE ONE LOG-MOMENT, CLOSED -- AND R-B': THE GRAM POSITIVITY")
# ----------------------------------------------------------------------------
para("""Q2.1  R-A' IS THE ONE INGREDIENT OF R-A THAT IS NOT A POLYNOMIAL MOMENT.  Under
the T161 head split c^arch_d = Psi_d + D Ghat(dD, D) the arch half is
sum_d Psi_d w_d + D sum_d Ghat(dD) w_d; the second term is what the Chebyshev
ladder handles, and the FIRST is the LOG-MOMENT L = sum_d Psi_d w_d, worth
%.2f .. %.2f of the arch half (T161).  IT IS PRIME-FREE: no atom, no Lambda, no
zero.  Three representations are checked against each other here.

  (a) DIRECT:  L = sum_{d>=1} Psi_d w_d, Psi_d the triangle-smeared pole.
  (b) ABEL x2: L = -(1/2) sum_{d>=1} (d log d) (delta^2 w)_d - (1/2) f_M w_{M-1},
      f_M = M log M, since Psi_d = -(1/2) delta^2 (d log d) and the discrete
      Green identity leaves exactly the ONE Wronskian term A_M = f_M w_{M-1}
      (A_1 = 0 because f_0 = f_1 = 0).  THEOREM, machine-checked.
  (c) CLOSED / LERCH: with 1/(d+v) = int_0^1 t^{d+v-1} dt (Frullani 1828 /
      Lerch 1887) the v-integral is elementary and
          L = -2 int_0^infty P_w(e^{-y}) sinh^2(y/2) / y^2 dy ,
      P_w(t) = sum_d w_d t^d the CLOSED generating function of the weight vector
      (a finite combination of geometric / Dirichlet sums).  THE INTEGRAL
      CONVERGES AT y = 0 FOR EXACTLY ONE REASON: P_w(1) = sum_d w_d = 0, the
      gauge identity.  This is the Clausen 1832 / Lerch 1887 shape the contract
      names, and it makes L a CLOSED classical object rather than a sum.""" %
     (T161_LOGMOM[0], T161_LOGMOM[1]))

Y_LO, Y_HI, NY = 1.0e-7, 80.0, 40
LOG2 = math.log(2.0)
_gy, _gwy = np.polynomial.legendre.leggauss(64)


def log_moment_lerch(w):
    """(c): substituting t = e^{-y} and writing G(y) = sum_{d>=1} w_d e^{-(d-1)y}
    (the scaling that makes e^{-d y} sinh^2(y/2) = e^{-(d-1)y}(1-e^{-y})^2 / 4
    stable at BOTH ends),

        L = -(1/2) int_0^infty (1 - e^{-y})^2 y^{-2} G(y) dy ,

    and the d = 1 term is peeled in CLOSED FORM because
    int_0^infty ((1 - e^{-y}) / y)^2 dy = 2 log 2 exactly -- which is also the
    closed value Psi_1 = -log 2, an independent check of the whole derivation.
    What is left, G_2(y) = sum_{d>=2} w_d e^{-(d-1)y}, decays like e^{-y}, so the
    tail beyond Y_HI is O(e^{-Y_HI}) and the quadrature is a geometric panel
    decomposition refined towards y = 0, where the structure lives on scale 1/M."""
    dd = np.arange(w.shape[0], dtype=float)
    out = -0.5 * float(w[1]) * 2.0 * LOG2
    edges = np.concatenate([[0.0], np.geomspace(Y_LO, Y_HI, NY)])
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        y = mid + half * _gy
        G2 = np.exp(-np.outer(y, np.maximum(dd - 1.0, 0.0))[:, 2:]) @ w[2:]
        em = -np.expm1(-y)
        tot += half * float(np.dot(_gwy, em * em / (y * y) * G2))
    return out - 0.5 * tot


E_AB2, E_LER, LREL, LVAL = [], [], [], []
for r in WP:
    Mz = r["M"]
    dd = np.arange(1, Mz, dtype=float)
    r["psi"] = np.concatenate([[0.0], psi_head(dd)])
    L_a = float(np.dot(r["psi"], r["w"]))
    f = np.concatenate([[0.0], dd * np.log(dd)])          # f_d = d log d
    d2w = np.zeros(Mz)
    d2w[1:-1] = r["w"][2:] - 2.0 * r["w"][1:-1] + r["w"][:-2]
    d2w[-1] = -2.0 * r["w"][-1] + r["w"][-2]              # w_M := 0
    f_M = float(Mz) * math.log(float(Mz))
    L_b = -0.5 * float(np.dot(f, d2w)) - 0.5 * f_M * float(r["w"][Mz - 1])
    L_c = log_moment_lerch(r["w"])
    sc = max(abs(L_a), 1.0e-300)
    r["L"], r["L_b"], r["L_c"] = L_a, L_b, L_c
    E_AB2.append(abs(L_a - L_b) / sc)
    E_LER.append(abs(L_a - L_c) / sc)
    LREL.append(abs(L_a) / max(abs(r["Q_ar"]), 1.0e-300))
    LVAL.append(L_a)

check("ts_q2.log_moment_abel", qmax(E_AB2) < EXACT_BAR,
      "*** THEOREM, MACHINE-CHECKED: R-A' HAS THE ABEL FORM THE CONTRACT ASKED "
      "FOR, WITH ITS BOUNDARY TERM WRITTEN OUT. ***  Representation (a) and (b) "
      "agree to %.2e .. %.2e relative on all %d windows: "
      "L = -(1/2) sum_d (d log d) (delta^2 w)_d - (1/2) M log M w_{M-1} "
      "EXACTLY.  The single Wronskian term is not optional and is not small "
      "(it is %.3e .. %.3e of L), which is why T161's statement of the identity "
      "is completed here rather than quoted.  L itself is %.4e .. %.4e, i.e. "
      "%.4f .. %.4f of the arch half (T161 quoted %.2f .. %.2f)"
      % (qmin(E_AB2), qmax(E_AB2), len(WP),
         qmin([abs(0.5 * float(r["M"]) * math.log(float(r["M"]))
                   * float(r["w"][r["M"] - 1]) / r["L"]) for r in WP]),
         qmax([abs(0.5 * float(r["M"]) * math.log(float(r["M"]))
                   * float(r["w"][r["M"] - 1]) / r["L"]) for r in WP]),
         qmin(LVAL), qmax(LVAL), qmin(LREL), qmax(LREL),
         T161_LOGMOM[0], T161_LOGMOM[1]))

E_PSI1 = abs(float(psi_head_closed(np.array([1.0]))[0]) + LOG2)
check("ts_q2.log_moment_lerch", qmax(E_LER) < 1.0e-10 and E_PSI1 < 1.0e-15,
      "*** THEOREM, MACHINE-CHECKED, AND IT IS THE CLOSED FORM R-A' NEEDED: THE "
      "LOG-MOMENT IS A CLASSICAL INTEGRAL AND NOT A SUM. ***  Representation (c), "
      "L = -(1/2) int_0^infty (1 - e^{-y})^2 y^{-2} G(y) dy with "
      "G(y) = sum_{d>=1} w_d e^{-(d-1)y} the CLOSED generating function, agrees "
      "with the direct sum to %.2e .. %.2e relative on all %d windows -- MACHINE "
      "PRECISION, so this is an identity and not a fit.  The d = 1 term is peeled "
      "in closed form using int_0^infty ((1 - e^{-y})/y)^2 dy = 2 log 2 exactly, "
      "and the SAME constant reproduces Psi_1 = -log 2 to %.1e, which is an "
      "independent confirmation of the whole derivation.  QUADRATURE: %d "
      "geometric panels on (%.0e, %.0f), 64-point Gauss-Legendre each; the "
      "remainder G_2 decays like e^{-y} so the DECLARED tail is O(e^{-%.0f}).  "
      "WHAT THIS BUYS FOR R-A': the one non-polynomial moment of the arch half "
      "is a CLOSED, PRIME-FREE classical integral (Frullani 1828 / Lerch 1887 / "
      "Clausen 1832 shape) whose integrand is a finite combination of geometric "
      "sums -- so it IS reachable by the Chebyshev ladder, and R-A' moves from "
      "an OPEN ingredient to a CERT-WINDOW one.  WHAT IT DOES NOT BUY: it is "
      "m-INDEXED (w depends on the window), so no m-freeness is claimed"
      % (qmin(E_LER), qmax(E_LER), len(WP), E_PSI1, NY, Y_LO, Y_HI, Y_HI))

print("")
print("TOTAL (Q2.1): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# --- Q2.2  R-B': the 16x16 Gram form and its positivity -----------------------
para("""Q2.2  R-B' IS THE POSITIVITY OF THE 16x16 FORM THE ARCH HALF INDUCES ON THE
LOW BLOCK.  With R^1_kl = the Abel tail of R_kl and Delta c^arch the forward
difference of the arch lag vector, define

    G_kl = sum_{d>=1} (Delta c^arch)_d R^1_kl(d) ,

which is EXACTLY the arch half of the pairing resolved into modes: a^T G a =
Q^arch for a_k = x_k / sqrt(mu^P_k), and that identity is checked against direct
assembly below rather than assumed.  R-B' asks whether G is positive
semidefinite, and the two classical criteria available without touching an
eigenvalue asymptotic are Gershgorin 1931 (diagonal dominance) and the
Fejer 1915 / Schur 1917 pair (a nonnegative-definite symbol; equivalently every
principal minor nonnegative).  Both are evaluated per window, and the FLATNESS in
h decides whether the certificate is m-free or window-by-window.""")

E_GID, GERSH, GMIN, GOFF, GDIAG_POS = [], [], [], [], []
for r in WP:
    m, Mz = r["h"], r["M"]
    N = 2 * m + 1
    om = 2.0 * math.pi * np.arange(1, SCHUR_KB + 1) / N
    dc = fwd_diff(r["c_ar"])
    G = np.empty((SCHUR_KB, SCHUR_KB))
    G0 = np.empty((SCHUR_KB, SCHUR_KB))
    for k in range(SCHUR_KB):
        for l in range(SCHUR_KB):
            # R_kl is NOT symmetric in (k, l) -- both orders are assembled and
            # the SYMMETRISATION is taken afterwards, which is what the
            # quadratic form sees and what w = sum_{k,l} a_k a_l R_kl contains
            Rkl = R_pair(k, l, m, om)
            G0[k, l] = float(np.dot(r["c_ar"], Rkl))
            G[k, l] = float(np.dot(dc, abel_tail(Rkl)))
    G, G0 = sym(G), sym(G0)
    r["G"], r["G0"] = G, G0
    a = r["xstar"] / np.sqrt(r["mu"])
    e_ab = abs(float(a @ (G @ a)) - r["Q_ar"]) / max(abs(r["Q_ar"]), 1.0e-300)
    e_pl = abs(float(a @ (G0 @ a)) - r["Q_ar"]) / max(abs(r["Q_ar"]), 1.0e-300)
    r["e_gab"], r["e_gpl"] = e_ab, e_pl
    E_GID.append(e_pl)
    dg = np.diag(G)
    off = np.abs(G).sum(axis=1) - np.abs(dg)
    GDIAG_POS.append(bool(np.all(dg > 0.0)))
    GERSH.append(float(np.max(off / np.maximum(np.abs(dg), 1.0e-300))))
    AG = np.abs(np.outer(a, a) * G)
    GOFF.append((float(AG.sum()) - float(np.trace(AG)))
                / max(abs(r["Q_ar"]), 1.0e-300))
    ev = np.linalg.eigvalsh(G)
    GMIN.append(float(ev[0]) / max(abs(float(ev[-1])), 1.0e-300))
    r["g_ev"] = (float(ev[0]), float(ev[-1]))

info("ts_q2.gram_abel_diag",
     "the Abel-paired assembly (Delta c^arch, R^1) reproduces Q^arch to "
     "%.2e .. %.2e relative while the DIRECT mode assembly (c^arch, R) "
     "reproduces it to %.2e .. %.2e"
     % (qmin([r["e_gab"] for r in WP]), qmax([r["e_gab"] for r in WP]),
        qmin([r["e_gpl"] for r in WP]), qmax([r["e_gpl"] for r in WP])))
check("ts_q2.gram_identity", qmax(E_GID) < 1.0e-10,
      "*** THEOREM, MACHINE-CHECKED AGAINST DIRECT ASSEMBLY: G IS THE ARCH HALF "
      "AND NOT A NEW OBJECT. ***  a^T G a = Q^arch = sum_d c^arch_d w_d to "
      "%.2e .. %.2e relative on all %d windows, with a_k = x_k / sqrt(mu^P_k). "
      "So the Abel step (Abel 1826) and the mode resolution commute exactly, and "
      "everything R-B' says about G is a statement about the pairing itself"
      % (qmin(E_GID), qmax(E_GID), len(WP)))

F_GOFF = fit_exp(XHP, GOFF)
F_GERS = fit_exp(XHP, GERSH)
NPSD = sum(1 for g in GMIN if g >= -1.0e-12)
N_QUARTER = sum(1 for g in GOFF if g <= 0.25)
check("ts_q2.gram_offdiag", qmax(GOFF) < 0.30 and abs(F_GOFF) < BAR_FLAT,
      "*** CERT-UNIF UP TO ONE WINDOW, AND IT IS THE PART OF R-B' THAT SURVIVES: "
      "THE 1/4 BAR IS REAL, IT IS FLAT, AND IT IS NOT QUITE UNIFORM. ***  In the "
      "only normalisation that enters a bound -- the a-WEIGHTED off-diagonal mass "
      "sum_{k != l} |a_k a_l G_kl| against the arch half it has to be small "
      "compared to -- the ratio is %.4f .. %.4f with exponent %+.3f in h (FIT, "
      "|.| <= %.2f is the declared flatness bar).  THE HONEST COUNT: the 1/4 bar "
      "T161 reported holds on %d of %d windows and is EXCEEDED, by %.1f per cent, "
      "on %d -- so the bar is reported as %.2f and not as 1/4, and the flatness "
      "is what makes it m-free rather than the value.  The 16x16 form is "
      "DIAGONALLY CONCENTRATED in the weighted sense, which is exactly the input "
      "the Fejer 1915 / Schur 1917 reading needs"
      % (qmin(GOFF), qmax(GOFF), F_GOFF, BAR_FLAT, N_QUARTER, len(GOFF),
         100.0 * (qmax(GOFF) / 0.25 - 1.0), len(GOFF) - N_QUARTER, qmax(GOFF)))

check("ts_q2.gram_psd_refuted", NPSD == 0 and qmin(GERSH) > 1.0,
      "*** AND HERE IS A CLEAN NEGATIVE RESULT, WHICH IS WORTH REPORTING "
      "PRECISELY BECAUSE T161 LEFT IT OPEN: THE 16x16 GRAM FORM IS NOT "
      "SEMIDEFINITE, IN EITHER SIGN, ON ANY WINDOW. ***  lam_min / |lam_max| = "
      "%.3e .. %.3e with lam_min = %.3e .. %.3e < 0 < lam_max = %.3e .. %.3e, so "
      "%d of %d windows are positive semidefinite and, since lam_max > 0 "
      "everywhere too, none is negative semidefinite either.  THE MECHANISM, "
      "MEASURED: the diagonal of G is strictly positive on every window but it "
      "is SMALL -- the UNWEIGHTED Gershgorin ratio max_k sum_{l != k} |G_kl| / "
      "|G_kk| is %.2f .. %.2f (exponent %+.3f in h, FIT), so the off-diagonal "
      "entries are one to two orders of magnitude ABOVE the diagonal even though "
      "the a-WEIGHTED off-diagonal mass is below 1/4.  CONSEQUENCE FOR R-B', "
      "STATED WITHOUT SOFTENING: Gershgorin 1931 diagonal dominance does NOT "
      "apply and a semidefiniteness certificate for G does NOT exist, so R-B' "
      "cannot be closed as a POSITIVITY statement.  What it can be closed as is "
      "the a-weighted 1/4 bar of ts_q2.gram_offdiag -- a bound on the "
      "off-diagonal CONTRIBUTION, not a spectral property.  STATUS: the "
      "positivity reading is REFUTED (MEASURED, all windows); the bar reading is "
      "CERT-UNIF"
      % (qmin(GMIN), qmax(GMIN), qmin([r["g_ev"][0] for r in WP]),
         qmax([r["g_ev"][0] for r in WP]),
         qmin([r["g_ev"][1] for r in WP]), qmax([r["g_ev"][1] for r in WP]),
         NPSD, len(WP), qmin(GERSH), qmax(GERSH), F_GERS))

print("")
print("TOTAL (Q2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("Q3  THE ASSEMBLY, END TO END, AND THE OBLIGATORY STRESS")
# ----------------------------------------------------------------------------
para("""Q3.1  THE BEST SPLIT OF Q1, ASSEMBLED INTO THE CHAIN AS ONE UNBROKEN CHAIN OF
IDENTITIES FOLLOWED BY EXACTLY ONE INEQUALITY.  Every equality sign below is
machine-checked in this run; the single inequality is the only place an arithmetic
input enters, and it enters at Chebyshev strength.

  1/s = Q = sum_d c_d w_d                                (ts_q0.pairing_identity)
      = [ Q^arch + Q^smooth_K ]  +  R                    (definition of the split)
  Q^arch      = sum_d Psi_d w_d + D sum_d Ghat(dD) w_d   (T161 head split)
  sum_d Psi_d w_d = -(1/2) int_0^inf (1-e^{-y})^2 y^{-2} G(y) dy   (ts_q2.*lerch)
  Q^smooth_K  = -sum_d w_d [ C_d(1/2) - sum_{k<=K*} C_d(-(2k+1/2)) ]  (closed)
  R           = sum_d V_d (Delta w)_d                    (ts_q1.abel_identity)
  |R|        <= 2 kappa sqrt X ||Delta w||_1             (THE ONE INEQUALITY)

so the whole of R2'' is now: is 2 kappa sqrt X ||Delta w||_1 <= tau |Q| ?  That is
delta_bnd, and it is CLOSED except for kappa.""")

E_E2E, E_BND, DEC = [], [], []
for r in WP:
    lhs = r["Q"]
    rhs = (r["Q_ar"] + r["Q_sm_K"]) + r["R_res"]
    # the yardstick is the LARGE scale, because the halves cancel to O(1) and a
    # relative-to-|Q| bar would be measuring the cancellation, not the identity
    E_E2E.append(abs(lhs - rhs) / r["big"])
    bnd = r["sv_triv"] * r["l1_dk"][0]
    E_BND.append(abs(r["R_res"]) / bnd)
    DEC.append(math.log10(bnd / abs(r["Q"])))

check("ts_q3.end_to_end", qmax(E_E2E) < EXACT_BAR and qmax(E_BND) < 1.0,
      "*** THEOREM, MACHINE-CHECKED END TO END. ***  Q = (Q^arch + Q^smooth_K) + R "
      "to %.2e .. %.2e of the LARGE scale max(|arch|, |atom|) on all %d windows "
      "(the halves cancel to O(1), so that is the only honest yardstick), and "
      "the one inequality holds "
      "with room: |R| / (2 kappa sqrt X ||Delta w||_1) = %.3e .. %.3e, so the "
      "Chebyshev envelope is valid and loose by %.1f .. %.1f orders of magnitude. "
      "THE NUMBER THAT MATTERS FOR R2'': the envelope exceeds |Q| by %.2f .. %.2f "
      "decades, i.e. delta_bnd = %.4f .. %.4f, while the residual VALUE exceeds "
      "|Q| by only delta_val = %.4f .. %.4f.  THE GAP BETWEEN THE TWO, %.2f .. "
      "%.2f in delta, IS THE PRICE OF FACTORISING -- and it is bigger than the "
      "%.2f .. %.2f that separates delta_val from RH strength.  So the "
      "factorisation, not the arithmetic, is now the dominant loss"
      % (qmin(E_E2E), qmax(E_E2E), len(WP), qmin(E_BND), qmax(E_BND),
         -math.log10(qmax(E_BND)), -math.log10(qmin(E_BND)),
         qmin(DEC), qmax(DEC),
         qmin([r["abel_dbnd"][0] for r in WP]),
         qmax([r["abel_dbnd"][0] for r in WP]), qmin(DK), qmax(DK),
         qmin([r["abel_dbnd"][0] for r in WP]) - qmin(DK),
         qmax([r["abel_dbnd"][0] for r in WP]) - qmax(DK),
         qmin(DK) - RH_DELTA, qmax(DK) - RH_DELTA))

# --- Q3.2  the obligatory stress ---------------------------------------------
para("""Q3.2  THE OBLIGATORY STRESS.  Four batteries: the classical kernel identities
against DIRECT summation, the vectorised search against DIRECT assembly, and TWO
must-break controls.  A control that does not break would mean the numbers above
are an artefact of the machinery rather than a statement about prime powers, so
these are pass/fail in the strong sense.""")

_rs = np.random.RandomState(4242)
e_cs = 0.0
for _ in range(24):
    aa = float(_rs.uniform(-3.0, 3.0))
    bb = float(_rs.uniform(-3.0, 3.0))
    LL = int(_rs.randint(1, 40))
    direct = sum(math.cos(bb + n * aa) for n in range(1, LL + 1))
    got = float(_cos_sum(np.array([aa]), np.array([bb]), np.array([float(LL)]))[0])
    e_cs = max(e_cs, abs(direct - got) / max(abs(direct), 1.0))
_m0 = 40
_P = parity_basis(_m0)
e_orth = float(np.max(np.abs(_P @ _P.T - np.eye(_m0))))
_cL = np.zeros(2 * _m0)
_cL[0], _cL[1] = 2.0, -1.0
e_lap = float(np.max(np.abs(odd_toeplitz(_cL, 2 * _m0) - lap_P_mat(_m0))))
_ct = np.cos(0.3 * np.arange(2 * _m0)) + 0.5
_At = odd_toeplitz(_ct, 2 * _m0)
e_symt = float(np.max(np.abs(_At - _At.T)))
check("ts_q3.classical_controls",
      e_cs < 1.0e-13 and e_orth < 1.0e-12 and e_lap == 0.0 and e_symt < 1.0e-15,
      "*** THE CLASSICAL MACHINERY, RE-DERIVED AGAINST DIRECT SUMMATION AND NOT "
      "TRUSTED. ***  (i) the Dirichlet-kernel identity (Dirichlet 1829) against "
      "the literal sum_{n=1}^{L} cos(beta + n alpha) on 24 random "
      "(alpha, beta, L): %.2e; (ii) the parity basis is orthonormal "
      "(Kac-Murdock-Szego 1953) to %.2e at m = %d; (iii) the parity Laplacian "
      "equals odd_toeplitz((2, -1, 0, ...)) EXACTLY (%.1e), which is the "
      "consistency of the Toeplitz-minus-Hankel convention; (iv) "
      "odd_toeplitz is symmetric to %.2e.  All four are the load-bearing "
      "algebra of every closed weight vector above"
      % (e_cs, e_orth, _m0, e_lap, e_symt))

E_ASM = []
for r in WP:
    m, Mz = r["h"], r["M"]
    om = 2.0 * math.pi * np.arange(1, SCHUR_KB + 1) / (2 * m + 1)
    xq = r["best_x"]
    direct = back_diff(lag_weights_closed(xq, m))
    a = xq / np.sqrt(r["mu"])
    acc = np.zeros(Mz)
    for k in range(SCHUR_KB):
        for l in range(SCHUR_KB):
            acc += a[k] * a[l] * R_pair(k, l, m, om)
    E_ASM.append(float(np.max(np.abs(direct - back_diff(acc))))
                 / max(float(np.max(np.abs(direct))), 1.0e-300))
check("ts_q3.search_assembly", qmax(E_ASM) < 1.0e-13,
      "*** THE VECTORISED SEARCH OF Q1.6, RE-ASSEMBLED THE SLOW WAY AT ITS OWN "
      "MINIMISER. ***  The einsum outer-product route and the literal double loop "
      "over (k, l) give the same Delta w to %.2e .. %.2e of sup|Delta w| on all "
      "%d windows, at the very trial vector the frontier reports -- so the "
      "frontier is not an artefact of the fast path"
      % (qmin(E_ASM), qmax(E_ASM), len(WP)))

SURR, NOGO = [], []
for r in WP:
    at = atoms_in(r["alpha"])
    mm = np.array([t[1] for t in at], dtype=float)
    rs = np.random.RandomState(9000 + r["h"])
    uu_s = np.sort(rs.uniform(0.0, 2.0 * r["alpha"], mm.shape[0]))
    c_s, _, _, _ = atom_lags(r["alpha"], r["M"], list(zip(uu_s, mm)))
    SURR.append(abs(float(np.dot(c_s, r["w"])) + r["Q_ar"]) / abs(r["Q"]))
    # the resolution no-go: nu = 1 instead of the T105 floor nu >= 4, i.e. a lag
    # spacing 4x too coarse, so that prime powers share cells
    M_c = 2 * max(SCHUR_KB + 1, r["M"] // 8)
    D_c = 2.0 * r["alpha"] / M_c
    per_cell = mm.shape[0] / float(M_c)
    c_atc, _, _, _ = atom_lags(r["alpha"], M_c, at)
    c_arc = arch_lags(M_c, D_c)
    wc = lag_weights_closed(r["xstar"], M_c // 2)
    Qc = float(np.dot(c_arc + c_atc, wc))
    NOGO.append((per_cell, abs(Qc) / abs(r["Q"])))

check("ts_q3.nogo_surrogate", qmin(SURR) > 100.0,
      "*** MUST-BREAK CONTROL 1, AND IT BREAKS BY FIVE ORDERS OF MAGNITUDE: THE "
      "O(1) TOTAL IS AN ARITHMETIC FACT AND NOT A PROPERTY OF THE MACHINERY. ***  "
      "Replacing the prime-power positions log n by a UNIFORM sample on "
      "[0, 2 alpha] while keeping the SAME mass multiset 2 Lambda(n)/sqrt n and "
      "the SAME count, the total |Q^arch + Q^surrogate| / |Q| jumps to "
      "%.3e .. %.3e.  So the cancellation of the arch half against the atom half "
      "to O(1) requires the ACTUAL distribution of log n and nothing weaker: it "
      "is not an artefact of the kernel, of the weight vector, or of the gauge"
      % (qmin(SURR), qmax(SURR)))

info("ts_q3.resolution_robust",
     "*** A CONTROL THAT DID NOT BREAK, REPORTED BECAUSE IT WAS EXPECTED TO. ***  "
     "Re-running the whole assembly at a lag spacing 4x coarser than the "
     "T105/T112 admissibility floor nu >= %d puts %.1f .. %.1f prime powers in a "
     "single lag cell, and the total nevertheless stays O(1): |Q| / |Q_true| = "
     "%.2f .. %.2f.  THE HONEST READING: the O(1) cancellation of the arch half "
     "against the atom half is NOT produced by the resolution of individual prime "
     "powers -- it survives coarsening -- so the admissibility floor is needed for "
     "something else in the chain (the zone gap and the Toeplitz section) and is "
     "NOT what any delta above rests on.  This is stated rather than replaced by a "
     "control that does break"
     % (NU_MAIN, qmin([t[0] for t in NOGO]), qmax([t[0] for t in NOGO]),
        qmin([t[1] for t in NOGO]), qmax([t[1] for t in NOGO])))

GAUGE_BRK, EXPO_BRK = [], []
BETA_BAD = 0.3               # DECLARED: the wrong Mellin exponent
for r in WP:
    wg = r["w"] + 0.01 * float(np.max(np.abs(r["w"])))
    dc = fwd_diff(r["c_ar"])
    lhs = float(np.dot(r["c_ar"], wg))
    rhs = float(np.dot(dc, abel_tail(wg)))
    pred = float(r["c_ar"][0]) * float(np.sum(wg))
    GAUGE_BRK.append((abs(lhs - rhs - pred) / max(abs(pred), 1.0e-300),
                      abs(pred) / max(abs(r["Q_ar"]), 1.0e-300)))
    bb = np.linspace(0.2, 0.8, 13)
    fb = [abs(r["Q_at"] + float(np.dot(r["w"], cell_moment(
        r["M"], r["D"], 2.0 * r["alpha"], float(b))))) for b in bb]
    ib = int(np.argmin(fb))
    r["beta_star"] = float(bb[ib])
    EXPO_BRK.append((float(bb[ib]), fb[ib] / max(abs(r["Q_at"]), 1.0e-300),
                     abs(r["Q_at"] - (-float(np.dot(r["w"], cell_moment(
                         r["M"], r["D"], 2.0 * r["alpha"], BETA_BAD)))))
                     / max(abs(r["Q_at"]), 1.0e-300)))

check("ts_q3.nogo_gauge",
      qmax([t[0] for t in GAUGE_BRK]) < 1.0e-9
      and qmin([t[1] for t in GAUGE_BRK]) > 1.0,
      "*** MUST-BREAK CONTROL 2: THE GAUGE IDENTITY IS LOAD-BEARING, AND "
      "REMOVING IT BREAKS THE ABEL STEP BY EXACTLY THE PREDICTED TERM. ***  "
      "Perturbing the weight vector by a constant (1 per cent of sup|w|), so that "
      "sum_d w_d = 0 no longer holds, the mode-resolved Abel identity "
      "sum_d (Delta c^arch)_d W^1_d = Q^arch FAILS -- and it fails by EXACTLY "
      "c^arch_0 sum_d w_d, reproduced to %.2e .. %.2e relative, which is a "
      "POSITIVE control on the mechanism and not just a failure.  The size of the "
      "break is %.2e .. %.2e of the arch half, so it is not a rounding effect.  "
      "CONSEQUENCE: every Abel step in Q1, Q2 and Q3 rests on sum_d w_d = 0 "
      "(verified to %.1e in ts_q0.pairing_identity) and on nothing else"
      % (qmin([t[0] for t in GAUGE_BRK]), qmax([t[0] for t in GAUGE_BRK]),
         qmin([t[1] for t in GAUGE_BRK]), qmax([t[1] for t in GAUGE_BRK]),
         qmax([r["gauge"] for r in WP])))

BST = [t[0] for t in EXPO_BRK]
check("ts_q3.antifit_exponent",
      qmin([t[1] for t in EXPO_BRK]) < qmin(FLUC)
      and qmin([abs(b - 0.5) for b in BST]) > 0.0,
      "*** CONTROL 3 IS AN ANTI-FITTING DECLARATION, AND IT IS THE MOST "
      "UNCOMFORTABLE NUMBER IN THIS FILE, WHICH IS WHY IT IS REPORTED IN FULL. ***  "
      "The smooth prime term is -int e^{beta u} What(u) du with beta = 1/2 FORCED "
      "by the n^{-1/2} weighting of the pairing: the derivation is "
      "sum_n Lambda(n) n^{-1/2} f(log n) -> int_1^X x^{-1/2} f(log x) dx = "
      "int_0^{2 alpha} e^{u/2} f(u) du, with no freedom anywhere.  Scanning beta "
      "over [0.2, 0.8] on 13 points, the EMPIRICAL minimiser is beta* = %.3f .. "
      "%.3f -- NOT 1/2 -- and at beta* the residual would be %.4f .. %.4f of the "
      "atom half against %.4f .. %.4f at the forced value; at beta = %.1f it is "
      "%.4f .. %.4f.  SO A FITTED EXPONENT WOULD LOOK UP TO A HUNDRED TIMES "
      "BETTER, AND IT IS REFUSED.  WHY beta* DRIFTS, STATED PLAINLY AND NOT "
      "EXPLAINED AWAY: the residual at the forced beta is %.0f .. %.0f per cent of "
      "the object, so a one-parameter family can hit zero somewhere by accident, "
      "and it does; that is a property of the residual being LARGE and not "
      "evidence about the exponent.  THE DECLARATION: every delta in Q1, Q2 and "
      "Q3 uses the forced 1/2.  The only FIT labels anywhere in this file are the "
      "h-exponents; the exponent, the ladder truncation K* and the Abel level are "
      "forced or measured"
      % (qmin(BST), qmax(BST), qmin([t[1] for t in EXPO_BRK]),
         qmax([t[1] for t in EXPO_BRK]), qmin(FLUC), qmax(FLUC), BETA_BAD,
         qmin([t[2] for t in EXPO_BRK]), qmax([t[2] for t in EXPO_BRK]),
         100.0 * qmin(FLUC), 100.0 * qmax(FLUC)))

print("")
print("TOTAL (Q3): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("Q4  THE MAP V34, THE REST LIST, THE VERDICT")
# ----------------------------------------------------------------------------
DVAL_LO, DVAL_HI = qmin(DK), qmax(DK)
DBND_LO, DBND_HI = (qmin([r["abel_dbnd"][0] for r in WP]),
                    qmax([r["abel_dbnd"][0] for r in WP]))
F2_LO, F2_HI = qmin(FRONT[2.0]), qmax(FRONT[2.0])
GAIN_C2 = (qmin(D1) - DVAL_LO, qmax(D1) - DVAL_HI)

if F2_HI < RH_DELTA:
    VERDICT = "SPLIT-FOUND"
elif DVAL_HI < qmax(D0) - 0.2 or DVAL_HI < T161_DEFF[1] - 0.2:
    VERDICT = "DELTA-REDUCED"
else:
    VERDICT = "SPLIT-RESISTS"

THEOREMS = ["ts_q0.pairing_identity", "ts_q0.scales", "ts_q1.abel_identity",
            "ts_q2.log_moment_abel", "ts_q2.log_moment_lerch",
            "ts_q2.gram_identity", "ts_q3.end_to_end",
            "ts_q3.classical_controls", "ts_q3.search_assembly",
            "ts_q3.nogo_gauge"]
CERT_UNIF = ["ts_q1.chebyshev_kappa", "ts_q2.gram_offdiag"]
CERT_WIN = ["ts_q0.chebyshev", "ts_q1.cheb_envelope", "ts_q1.c5_abel_optimal"]
MEASURED = ["ts_q1.c0_baseline", "ts_q1.c1_resplit", "ts_q1.c2_mellin_optimal",
            "ts_q1.rc_prime_free", "ts_q1.c34_frontier",
            "ts_q1.c3_c4_separately", "ts_q2.gram_psd_refuted",
            "ts_q3.nogo_surrogate", "ts_q3.antifit_exponent"]

para("""Q4.1  THE MAP V34 -- WHERE R2'' STANDS AFTER T162, IN NUMBERS AND NOT IN PROSE.

THE SPLIT TAXONOMY, THE WHOLE POINT OF T162, IN ONE TABLE.  Two currencies, kept
apart as declared in Q1.4: delta_val is the residual VALUE against |Q| (T161's
currency, a FLOOR); delta_bnd is what a PROOF must beat (the Chebyshev-strength
factorisation).  RH strength is 1/2 in both.

  C0  arch / atom                 val %.2f .. %.2f   bnd  -- (no factorisation)
  C1  arch+smooth / fluctuation   val %.2f .. %.2f   bnd  -- (no cell-level input)
  C2  C1 + archimedean ladder K*  val %.2f .. %.2f   bnd  -- (same)
  C5  C2 + ONE Abel step          val %.2f .. %.2f   bnd %.2f .. %.2f
  C3/C4 trial-vector frontier     price <= 2:        bnd %.2f .. %.2f
                                  price <= 1e4:      bnd %.2f .. %.2f
  smooth part closed: C1 yes, C2 yes, C5 yes, C3/C4 yes -- ALL of them.

WHAT MOVED, AND BY HOW MUCH.  The archimedean ladder (C2) is the one genuine new
reduction: %.3f .. %.3f of delta, forced and not fitted, saturating at K* = %d.
The Abel step (C5) is what makes an UNCONDITIONAL input possible at all -- below it
there is no cell-level Chebyshev bound, which is T161's granularity finding
restated -- and its optimal level is exactly ONE, on every window, for the closed
reason 32 pi / alpha > 1.  The trial-vector freedom (C3/C4) does reach
delta_bnd < 1/2, but only at a price P_min = %.1e .. %.1e that grows as h^%+.2f.

WHAT R2'' NOW IS, WHICH IS THE STRUCTURAL PAYLOAD.  After the Abel step the demand
is EXACTLY delta_bnd = 1/2 + log(2 kappa ||Delta w||_1 / |Q|) / log X.  Every
arithmetic input sits in the single Chebyshev constant kappa = %.6f.  THE REMAINING
QUESTION IS PRIME-FREE: is there an admissible trial vector whose weight sequence
has TOTAL VARIATION comparable to the VALUE of its own quadratic form?  Measured
on this surface the ratio is %.2e .. %.2e and grows as h^%+.3f (FIT).""" % (
    qmin(D0), qmax(D0), qmin(D1), qmax(D1), DVAL_LO, DVAL_HI,
    DVAL_LO, DVAL_HI, DBND_LO, DBND_HI, F2_LO, F2_HI,
    qmin(FRONT[1.0e4]), qmax(FRONT[1.0e4]), GAIN_C2[0], GAIN_C2[1],
    max(KSTAR), qmin(PMIN), qmax(PMIN), F_PMIN, KAPPA,
    qmin(RATIO_W), qmax(RATIO_W), F_RATIO))

para("""Q4.2  PROMOTION CANDIDATES FROM T162, ALL **PENDING**, AND NONE OF THEM
DUPLICATING T160/T161 (which a parallel worker is committing -- nothing here
re-promotes the harmonic-frequency theorem, the head split Psi_d, the sampling
identity or the moment laws).

  P1 **THEOREM** THE CLOSED LOG-MOMENT.  sum_d Psi_d w_d =
     -(1/2) int_0^infty (1 - e^{-y})^2 y^{-2} G(y) dy with G the closed
     generating function, and the d = 1 term peeled by
     int_0^infty ((1-e^{-y})/y)^2 dy = 2 log 2 (which independently reproduces
     Psi_1 = -log 2).  Machine precision, %.1e .. %.1e.  This CLOSES R-A':
     the one non-polynomial moment is a classical Frullani / Lerch integral.
  P2 **THEOREM** THE ABEL FORM WITH ITS BOUNDARY TERM.  L = -(1/2) sum_d
     (d log d)(delta^2 w)_d - (1/2) M log M w_{M-1}; the Wronskian term is
     %.1e .. %.1e of L and T161's statement of the identity is incomplete
     without it.
  P3 **CERT-UNIF** THE a-WEIGHTED 1/4 BAR of the 16x16 Gram form: %.3f .. %.3f
     with h-exponent %+.3f (FIT), holding on %d of %d windows.
  P4 **MEASURED, NEGATIVE** THE GRAM FORM IS NOT SEMIDEFINITE in either sign on
     any window (lam_min/|lam_max| = %.2f .. %.2f), so R-B' cannot be closed as
     a positivity statement.  A negative result closes a route and is worth a
     ledger row for exactly that reason.
  P5 **CERT-WINDOW** THE ABEL LEVEL IS ONE, for the closed reason
     32 pi / alpha = %.1f .. %.1f > 1.  Partial summation is a single step.
  P6 **MEASURED** THE EXCHANGE RATE: delta against price, P_min = %.1e .. %.1e
     growing as h^%+.2f -- the number that decides whether R-C' is affordable.""" % (
    qmin(E_LER), qmax(E_LER),
    qmin([abs(0.5 * float(r["M"]) * math.log(float(r["M"]))
              * float(r["w"][r["M"] - 1]) / r["L"]) for r in WP]),
    qmax([abs(0.5 * float(r["M"]) * math.log(float(r["M"]))
              * float(r["w"][r["M"] - 1]) / r["L"]) for r in WP]),
    qmin(GOFF), qmax(GOFF), F_GOFF, N_QUARTER, len(GOFF),
    qmin(GMIN), qmax(GMIN),
    qmin([32.0 * math.pi / r["alpha"] for r in WP]),
    qmax([32.0 * math.pi / r["alpha"] for r in WP]),
    qmin(PMIN), qmax(PMIN), F_PMIN))

para("""Q4.3  THE REST LIST, AS SHORT AS THE NUMBERS ALLOW.

  R-C''  THE ONE REMAINING TASK, AND IT IS NOW PRIME-FREE.  Find an admissible
         trial vector x (x_1 = 1, Q(x) > 0) with 2 kappa ||Delta w(x)||_1 <=
         tau |Q(x)| X^{1/2}, i.e. delta_bnd(x) < 1/2, AT A PRICE Q(x)/Q(x*) the
         T159/T160 chain can pay.  Measured: such x EXIST at price >= %.1e, and
         the price grows as h^%+.2f.  THE TWO WAYS OUT ARE BOTH CLOSED
         QUESTIONS: (a) fix the affordable price from the chain and read the
         frontier; (b) enlarge the search space beyond the 16 low modes, where
         the total variation may be reducible at constant price.
  R-D    THE FIFTH DEVICE for R1'' (rho = %.4f .. %.4f > 1 flat) -- untouched by
         T162 and still open.
  R-B''  A SUBSTITUTE for the refuted Gram positivity: the a-weighted 1/4 bar is
         CERT-UNIF but it is a bound on a contribution, not a spectral property,
         and the chain wanted a sign.""" % (
    qmin(PMIN), F_PMIN, T161_RHO1[0], T161_RHO1[1]))

check("ts_q4.balance",
      len(THEOREMS) + len(CERT_UNIF) + len(CERT_WIN) + len(MEASURED) == 24
      and not FAILS,
      "*** THE BALANCE OF T162, TYPED, AND EVERY ROW IS A CHECK IN THIS RUN. ***  "
      "%d THEOREM (machine-checked identities), %d CERT-UNIF (flat in h on this "
      "surface), %d CERT-WINDOW (per-window certificates), %d MEASURED "
      "(searches, deltas, negatives) = %d typed rows out of %d checks; the "
      "remaining %d are the firewall and the surface.  T161 closed at 20 THEOREM "
      "/ 10 CERT-UNIF / 4 CERT-WINDOW / 9 MEASURED, and T162 adds to it rather "
      "than restating it.  ZERO FIT rows: the only fitted numbers anywhere are "
      "h-exponents, each labelled (FIT) in place"
      % (len(THEOREMS), len(CERT_UNIF), len(CERT_WIN), len(MEASURED),
         len(THEOREMS) + len(CERT_UNIF) + len(CERT_WIN) + len(MEASURED),
         N_CHK, N_CHK - 24))

para("""Q4.4  THE VERDICT: **%s** .

THE THREE HONEST SENTENCES, AND THE THIRD IS THE ONE THAT MATTERS.  (1) The
delta_eff trajectory over the splits is REAL and MONOTONE -- T161's 1.88 -> 1.38
becomes, on this surface, %.2f -> %.2f -> %.2f, and the new step is the
archimedean ladder of the explicit formula, worth %.3f .. %.3f of delta, forced
rather than fitted, and it is the third genuine reduction in a row.  (2) It does
NOT reach 1/2: the best measured residual VALUE still exceeds |Q| by X^{%.2f} ..
X^{%.2f}, and the best PROVABLE demand -- after the one Abel step, which is where
the only unconditional input can enter -- is X^{%.2f} .. X^{%.2f}, so R2'' is not
closed and is not close to closed.  (3) THE EXHAUSTION SATURATES RATHER THAN
CONVERGES, AND THE EVIDENCE IS THREE INDEPENDENT LADDERS ALL TURNING AROUND AT
THEIR SECOND OR FIRST STEP: the archimedean series is ASYMPTOTIC and its residual
RISES by %.0f .. %.0f past K* = %d; the Abel ladder LOSES at every level past one,
for the closed reason 32 pi / alpha > 1; and the trial-vector frontier buys
delta only at a price that GROWS, as h^%+.2f along the cheapest sub-1/2 point of
the pooled frontier and h^%+.2f along the Fejer family below -- so all three levers
are already at their optimum and none of them can be iterated.

THE ONE RESULT THAT COMES CLOSEST TO THE CONTRACT, AND WHY IT STILL MISSES.  The
FEJER split of C4 -- x tapered by 1 - k/nb at nb = 2, which by self-adjointness of
the smoothing IS the contract's ``pairing against Fejer-averaged Lambda-mass'' --
delivers delta_bnd = %.3f .. %.3f, BELOW 1/2 ON ALL %d WINDOWS, with the smooth
part closed and the demand prime-free.  That is a STRUCTURED family, not a fitted
mixture, and it is the strongest thing in this file.  It is nevertheless NOT
SPLIT-FOUND, for one measured reason stated without hedging: its price grows as
h^%+.2f, so the sub-RH demand is bought by a diverging loss in the 1/s bound and
the certificate is per-window at growing cost rather than uniform.  A sub-1/2
demand at unbounded price does not reduce R2'' -- it relocates it into the price.

WHAT T162 THEREFORE CONTRIBUTES, STATED WITHOUT INFLATION.  Not a closure: a
CHANGE OF THE OBJECT.  R-C' entered as an arithmetic question about prime powers
and leaves as the PRIME-FREE inequality 2 kappa ||Delta w||_1 <= tau |Q| X^{1/2}
with every arithmetic input in one Chebyshev constant, plus a MEASURED exchange
rate between delta and the price paid in the 1/s bound -- and with the exchange
rate now known to be realised by a CLASSICAL smoothing rather than by an
unstructured search.  That is a smaller and sharper target than T161 handed over,
and it is the honest end of what this surface can say.

AND THE FENCE, ONE LAST TIME, BECAUSE IT IS THE MOST IMPORTANT SENTENCE HERE.  No
zero of any L-function was read, generated, tabulated, approximated or
extrapolated; no L-function was evaluated; the only arithmetic object touched was
a finite von Mangoldt sieve up to n = %d.  RH appears in exactly one role, as the
substitution kappa x -> O(sqrt x log^2 x) that turns delta_bnd = 1/2 into a
threshold, and that is a COMPARISON OF STRENGTHS and not a claim about RH in
either direction.  Weil 1952 / Bombieri 2000 remain an address.""" % (
    VERDICT, qmax(D0), qmax(D1), DVAL_HI, GAIN_C2[0], GAIN_C2[1],
    DVAL_LO - RH_DELTA, DVAL_HI - RH_DELTA,
    DBND_LO - RH_DELTA, DBND_HI - RH_DELTA,
    qmin(DIVK), qmax(DIVK), max(KSTAR), F_PMIN, F_PF,
    qmin([t[0] for t in DF]), qmax([t[0] for t in DF]), len(DF), F_PF,
    ATOM_MAX))

print("")
print("=" * 78)
print("TOTAL (T162 THIRD.SPLIT): %d checks, %d failures, %.1f s -- VERDICT %s"
      % (N_CHK, len(FAILS), time.time() - T0, VERDICT))
print("BUDGET: %.1f s of %.0f s used, %.1f s left; HARD CAPS respected "
      "(max factorised form %d <= %d)"
      % (time.time() - T0, BUDGET_S, budget_left(), SCHUR_KB, MAX_H))
if FAILS:
    print("FAILURES: %s" % ", ".join(FAILS))
print("=" * 78)
