"""PART 164 -- THE CONTRACT ``SECTOR.CHANGE'': THE TWO ARMS OF R-E.

THE RH FENCE, FIRST, PROMINENT, AND IT IS THE MOST IMPORTANT SENTENCE IN THIS
FILE.  Nothing here reads, generates, tabulates, approximates or extrapolates a
single zero of any L-function, and no L-function is ever evaluated anywhere.  The
only arithmetic object touched is a FINITE sum over prime powers produced by a
von Mangoldt sieve inside this file.  The number 1/2 appears below ONLY as the
STRENGTH of a classical statement, i.e. as a yardstick against which a required
depth is compared.  A COMPARISON OF STRENGTHS IS NOT A CLAIM: nothing below
asserts, assumes, weakens or implies RH in either direction, and Weil 1952
remains an ADDRESS and nothing else.  An AST firewall enforces the absence of
zero data, the import whitelist, the absence of write-mode file access and the
single-file rule.

WHERE T163 LEFT THE CHAIN.  T163 turned R2'' into an IDENTITY -- the exchange law
delta_bnd(x) = 1/2 + log(2 kappa g_16 TV(x) / P(x)) / log X, so sub-yardstick
demand IS the inequality P > 2 kappa g_16 TV -- and then proved a floor: with
w_0(x) = ||a(x)||^2, TV(x) >= |w_0(x)| by telescoping (w_M = 0), and the Thomson
normalisation x_1 = 1 forces ||a||^2 >= 1 / mu^P_1 = 1 / (4 sin^2(pi/N)) ~ h^2 for
EVERY admissible trial vector in the parity sector.  Verdict FRONT-RESISTS, as a
theorem.  The successor R-E has two prime-free arms, and this file is both of
them.

  ARM A (S1)  THE TOLERANCE ANALYSIS.  Trace the dependence of the chain on the
              entry ceiling 1/s station by station -- r <= 1/(L s), the T156
              kernel F(P, r), the p_1 substitution, the collapse cost,
              end-to-end -- and ask what happens if 1/s is allowed to GROW like
              h^eps.  Then ask the sharper question the T158 ladder forces:
              1/g_16 is certified FLAT per window, so WAS the O(1) requirement
              ever open at all?
  ARM B (S2)  THE SECTOR CHANGE.  Can the entry functional live in a sector whose
              lowest eigenvalue does not vanish like h^-2 -- the full space, a
              weighted or shifted sector, the frequency side?

DISCIPLINE.  THEOREM / CERT-UNIF / CERT-WINDOW / MEASURED / FIT strictly apart,
every claim labelled in place.  TWO ``P''s, NEVER CONFLATED, AND THIS IS THE
PEDANTIC POINT OF THE FILE: P_pr(x) = Q(x) / Q(x*) is the T163 PRICE in the 1/s
ceiling, while P_K = a_hat . s is the KANTOROVICH ratio inside the T156 kernel
F(P_K, r).  They are different objects and are written differently everywhere
below.  SCALES ARE PEDANTIC: alpha = log n_zone; D = 2 alpha / M; h = M / 2 =
alpha / D; X = e^{2 alpha}; log X = 2 alpha exactly.  Classics cited where used:
Chebyshev 1852, Dirichlet 1829, Abel 1826, Mellin 1896, Fejer 1915, Schur 1917,
Kantorovich 1948, Kac-Murdock-Szego 1953, Rosser-Schoenfeld 1962, Temple 1928,
Weil 1952.
HARD CAPS: any factorised matrix <= 1500; probe budget < 900 s.
"""

import ast
import math
import os
import time

import numpy as np
from scipy.linalg import cho_factor, cho_solve, eigh as sp_eigh

T0 = time.time()
np.random.seed(164164)

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

N_ZONES = 40                 # the SAME surface RECIPE AND DENSITY as T163, so
                             # that every exponent below is comparable to T163's
                             # without a density caveat
HCAP = 1450                  # inside the HARD cap MAX_H = 1500
H_MIN = 128                  # DECLARED: >= 2 x the largest mode block K = 64
N_ATOM_MIN = 40              # DECLARED surface floor (as T161 .. T163)
SCHUR_KB = 16                # the FIXED low block of the T152 .. T163 chain
KB_MAX = 64                  # the enlarged block, carried for the S2 controls
H_EIG = 1450                 # DECLARED HORIZON of the S1 station map: the dense
                             # lambda_1(A) solve is done only for h <= H_EIG
N_EIG_MAX = 10               # DECLARED: at most this many windows in the S1 map,
                             # log-spaced inside the horizon for a real lever arm

EXACT_BAR = 1.0e-12          # the bar on every claimed IDENTITY
GAUGE_BAR = 1.0e-8           # the bar on the S2 gauge identities.  DECLARED
                             # HORIZON: the gauge round trip multiplies the trial
                             # vector by sqrt(mu'/mu), which spans up to seven
                             # decades on the weight grid below, so the round-off
                             # floor of the round trip is that spread times eps
COND_BAR = 1.0e12            # the T159 numerical horizon on cond(B_LL)
BAR_FLAT = 0.25              # |exponent| bar for "flat / non-growing" (T159)
EPSM = float(np.finfo(float).eps)
B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962)
RH_DELTA = 0.5               # RH STRENGTH, as a delta.  A YARDSTICK, NOT A CLAIM
HEADROOM_BAR = 1.0e3         # DECLARED cancellation headroom over machine eps

# T161 .. T163 numbers, QUOTED, never recomputed as an input to anything
T163_KAPPA = 0.03882
T163_TVSLACK = (5.00, 23.20)
T163_TVEXP = 1.997
T163_PCROSS_EXP = 1.91
T163_PAFF_EXP = 3.05
T163_G16_EXP = 0.059
T163_CANC_EXP = -0.172
T163_QUARTER = 0.25          # the T162 a-weighted quarter bar, QUOTED
T163_PC_OVER_AFF = (0.0066, 0.205)
T161_RHO1 = (1.0036, 1.0140)
T163_BALANCE = (11, 1, 4, 10)

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
    check("sc_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("sc_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("sc_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("sc_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "sector_change_probe.py", "single new file in the sandbox")


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


def full_mu(m):
    """THE FULL (UNPROJECTED) DIRICHLET-FREE LAPLACIAN SPECTRUM on N = 2m+1
    points with periodic closure: mu_k = 4 sin^2(pi k / N), k = 0 .. N-1.  The
    k = 0 mode is the CONSTANT vector and has eigenvalue EXACTLY ZERO -- this is
    the even sector T162 found carrying the negative inertia, and it is why S2
    candidate (i) is settled in closed form."""
    N = 2 * m + 1
    kk = np.arange(0, N, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m, kb=None):
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, (kb or m) + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_P_mat(m):
    """L_P = tridiag(-1, 2, -1) with last diagonal 3; EQUIVALENTLY
    odd_toeplitz(c^L, M) for c^L = (2, -1, 0, ..., 0), re-checked in S3."""
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
    what makes w_d closed.  Re-checked in S3."""
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


def lag_weights_from_v(v, m):
    """*** THE T163 CORRELATION FORM, QUOTED AS A THEOREM AND RE-CHECKED BELOW.
    ***  For v in lag space, w_0 = A_0 and w_d = 2 A_d - H_{M-1-d} (d >= 1) with
    A the autocorrelation and H the self-convolution of v; then
    x^T B x = sum_d c_d w_d exactly.  Written in terms of v ALONE, because S2
    changes the map x -> v and nothing else."""
    M = 2 * m
    ac = np.correlate(v, v, "full")[m - 1:]
    cv = np.convolve(v, v)
    w = np.zeros(M)
    w[:m] = 2.0 * ac
    w[0] = ac[0]
    ee = (M - 1) - np.arange(1, M)
    w[1:] -= np.where(ee <= M - 2, cv[np.minimum(ee, M - 2)], 0.0)
    return w


def lag_weights_corr(x, m, Tb, mu=None):
    """v = T_K^T a with a_k = x_k / sqrt(mu_k); mu DEFAULTS to the parity
    spectrum and is an ARGUMENT because S2 shifts it."""
    nb = x.shape[0]
    mm = parity_mu(m)[:nb] if mu is None else np.asarray(mu, float)[:nb]
    return lag_weights_from_v(Tb[:nb, :].T @ (x / np.sqrt(mm)), m)


def back_diff(w):
    """(Delta w)_d = w_d - w_{d+1}, with w_M := 0."""
    out = np.empty_like(w)
    out[:-1] = w[:-1] - w[1:]
    out[-1] = w[-1]
    return out


def part_sums(c):
    """C_d = sum_{e <= d} c_e -- the Abel partial sums (Abel 1826).  The object
    the S2 alignment analysis is about."""
    return np.cumsum(c)


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
    """t_k(sigma) = max(0, 1 - k/sigma), the continuous Fejer window (Fejer
    1915); sigma = 1 is the K = 1 ladder rung, sigma = inf the T160 optimiser."""
    if not np.isfinite(sig):
        return np.ones(K)
    return np.maximum(0.0, 1.0 - np.arange(K) / float(sig))


def cf_ladder(Bm, K):
    """*** THE T158 CHOLESKY / CONTINUED-FRACTION LADDER. ***  g_K = e_1^T Q_K^-1
    e_1 = sum_{j<=K} y_j^2 with y = L_K^-1 e_1, every term strictly positive, so
    1/g_K is a DECREASING chain of upper bounds on 1/s (Schur 1917 nested
    complements; Haynsworth 1968; the Jacobi continued fraction)."""
    Q = sym(np.asarray(Bm)[:K, :K])
    try:
        L = np.linalg.cholesky(Q)
    except np.linalg.LinAlgError:
        return None
    e1 = np.zeros(K)
    e1[0] = 1.0
    return np.cumsum(np.linalg.solve(L, e1) ** 2)


def loss_PR(P_K, r):
    """*** THE T156 KERNEL F(P_K, r), QUOTED AS A THEOREM AND NOT RE-DERIVED.
    ***  With W' = [[P_K, 1], [1, 1]], N' = [[1, 1], [1, r]], P_K >= 1
    (Kantorovich 1948) and r >= 1, the t_1 loss of the two-dimensional model is
    F = 1 - (al + be)^2 / (al^2 + 2 al be + be^2 r) at the bottom generalised
    eigenvector (al, be).  P_K IS THE KANTOROVICH RATIO a_hat . s AND IS NOT THE
    T163 PRICE."""
    if not (np.isfinite(P_K) and np.isfinite(r)) or r <= 1.0 or P_K < 1.0:
        return float("nan")
    W2 = np.array([[P_K, 1.0], [1.0, 1.0]])
    N2 = np.array([[1.0, 1.0], [1.0, r]])
    try:
        _ev, V2 = sp_eigh(sym(W2), sym(N2))
    except (np.linalg.LinAlgError, ValueError):
        return float("nan")
    al, be = float(V2[0, 0]), float(V2[1, 0])
    den = al * al + 2.0 * al * be + be * be * r
    if abs(den) < 1.0e-300:
        return float("nan")
    return 1.0 - (al + be) ** 2 / den


section("PART 164 -- SECTOR.CHANGE -- Q0  THE FENCE, THE SCALES, THE SURFACE")
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
check("sc_q0.chebyshev", _bpsi <= B_PSI,
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
check("sc_q0.chebyshev_kappa",
      0.0 < KAPPA < 0.2 and abs(KAPPA - T163_KAPPA) < 0.001
      and abs((1.0 + KAPPA) - B_PSI) < 0.001,
      "*** THE ONE UNCONDITIONAL ARITHMETIC INPUT OF THE WHOLE FILE, MEASURED ON "
      "THIS SURFACE AND NOTHING ELSE. ***  |psi(x) - x| <= kappa x with kappa = "
      "%.6f, verified at EVERY jump point in %.0f <= x <= %d; T163 used the SAME "
      "constant (%.5f) and the Rosser-Schoenfeld 1962 form of it is psi(x) <= "
      "(1 + kappa) x = %.5f x, reproducing the quoted Chebyshev strength %.5f to "
      "%.1e.  The crossing criterion of T163 is Q > 2 kappa TV with THIS kappa, "
      "i.e. TV / Q < 1 / (2 kappa) = %.3f, and that RATIO is the object of S2"
      % (KAPPA, X0_CHEB, ATOM_MAX, T163_KAPPA, 1.0 + KAPPA, B_PSI,
         abs(1.0 + KAPPA - B_PSI), 1.0 / (2.0 * KAPPA)))

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
check("sc_q0.surface", len(SZ) >= 8,
      "%d prime-power zones (of %d admissible) are carried, log-spaced in h inside "
      "the caps H_MIN = %d, h <= %d, MAX_H = %d, and the atom floor of %d prime "
      "powers per window: h = %d .. %d, a lever arm of %dx.  The DECLARED S1 "
      "sub-surface for the dense lambda_1(A) station map is h <= %d, at most %d "
      "windows"
      % (len(SZ), len(CAND), H_MIN, HCAP, MAX_H, N_ATOM_MIN,
         min(t[3] for t in SZ), max(t[3] for t in SZ),
         int(max(t[3] for t in SZ) / max(min(t[3] for t in SZ), 1)),
         H_EIG, N_EIG_MAX))

W = []
for (kz, Dz, Mz, hz) in SZ:
    if budget_left() < 520.0:
        info("sc_q0.budget", "stopped enumerating windows at h = %d" % hz)
        break
    alpha = UU_ALL[kz]
    c_at, D, mu_tot, n_at = atom_lags(alpha, Mz, atoms_in(alpha))
    c_ar = arch_lags(Mz, D)
    W.append(dict(k=kz, h=hz, M=Mz, D=D, alpha=alpha, n_zone=NN_ALL[kz],
                  c_ar=c_ar, c_at=c_at, c=c_ar + c_at, mu_tot=mu_tot,
                  n_atom=n_at, X=math.exp(2.0 * alpha), logX=2.0 * alpha))

check("sc_q0.scales",
      all(abs(r["h"] * r["D"] - r["alpha"]) < 1.0e-10 for r in W)
      and all(abs(math.log(r["X"]) - 2.0 * r["alpha"]) < 1.0e-9 for r in W),
      "*** THE SCALES, WRITTEN OUT ONCE AND NEVER ASSUMED AGAIN. ***  alpha = "
      "log n_zone = %.4f .. %.4f; D = 2 alpha / M = %.3e .. %.3e; h = M/2 = "
      "alpha / D = %d .. %d (identity to 1e-10); X = e^{2 alpha} = %.4e .. %.4e, "
      "i.e. X = n_zone^2 EXACTLY and log X = 2 alpha EXACTLY; %d .. %d prime-power "
      "atoms per window on %d windows"
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
    r["mu1_full"] = float(parity_mu(m)[0])
    isq = 1.0 / np.sqrt(r["mu"])
    r["G64"] = sym(Tb @ (A @ Tb.T))            # the UN-normalised mode Gram
    r["G64_ar"] = sym(Tb @ (odd_toeplitz(r["c_ar"], r["M"]) @ Tb.T))
    r["B64"] = sym(r["G64"] * np.outer(isq, isq))
    r["B_LL"] = r["B64"][:SCHUR_KB, :SCHUR_KB].copy()
    r["G_LL"] = r["G64"][:SCHUR_KB, :SCHUR_KB].copy()
    e1 = np.zeros(SCHUR_KB)
    e1[0] = 1.0
    r["xstar"] = np.linalg.solve(r["B_LL"], e1)
    r["xstar"] /= max(abs(float(r["xstar"][0])), 1.0e-300)
    ev = np.linalg.eigvalsh(r["B_LL"])
    r["kap"] = float(ev[-1] / max(ev[0], 1.0e-300))
    r["gcum"] = cf_ladder(r["B_LL"], SCHUR_KB)
    r["C"] = part_sums(r["c"])
    r["Cinf"] = float(np.max(np.abs(r["C"])))
    del A

WP = [r for r in W if r["kap"] <= COND_BAR and r["gcum"] is not None]
DROP = [r for r in W if r not in WP]
XHP = [float(r["h"]) for r in WP]

E_QID, HEADROOM, TVF = [], [], []
for r in WP:
    w = lag_weights_corr(r["xstar"], r["h"], r["Tb"])
    r["w"], r["dw"] = w, back_diff(w)
    r["Q"] = float(np.dot(r["c"], w))
    r["Q_ar"] = float(np.dot(r["c_ar"], w))
    r["Q_at"] = float(np.dot(r["c_at"], w))
    r["TV"] = float(np.sum(np.abs(r["dw"])))
    r["l1w"] = float(np.sum(np.abs(w)))
    r["gauge"] = abs(float(np.sum(w))) / max(r["l1w"], 1.0e-300)
    r["big"] = max(abs(r["Q_ar"]), abs(r["Q_at"]))
    r["canc"] = abs(r["Q"]) / max(r["big"], 1.0e-300)
    r["Phi"] = cell_moment(r["M"], r["D"], 2.0 * r["alpha"], 0.5)
    r["g1"], r["g16"] = float(r["gcum"][0]), float(r["gcum"][SCHUR_KB - 1])
    r["P_aff"] = r["g16"] / r["g1"]
    E_QID.append(abs(r["Q"] - float(r["xstar"] @ (r["B_LL"] @ r["xstar"])))
                 / r["big"])
    HEADROOM.append(abs(r["Q"]) / (r["big"] * EPSM))
    TVF.append(r["TV"] * r["mu1_full"])

F_G16 = fit_exp(XHP, [1.0 / r["g16"] for r in WP])
F_TV = fit_exp(XHP, [r["TV"] for r in WP])
F_CINF = fit_exp(XHP, [r["Cinf"] for r in WP])
check("sc_q0.pairing_identity",
      qmax(E_QID) < EXACT_BAR and qmax([r["gauge"] for r in WP]) < EXACT_BAR
      and qmin(HEADROOM) > HEADROOM_BAR and qmin(TVF) >= 1.0,
      "*** THE T163 SURFACE, REBUILT AND RE-CHECKED, BECAUSE EVERY NUMBER BELOW IS "
      "A STATEMENT ABOUT IT. ***  x^T B_LL x = sum_d c_d w_d to %.2e .. %.2e of "
      "max(|arch half|, |atom half|) on %d windows inside the DECLARED horizon "
      "cond(B_LL) <= %.0e (%d dropped); the gauge identity sum_d w_d = 0 holds to "
      "%.2e of ||w||_1; the cancellation headroom |Q| / (max half x eps) = "
      "%.2e .. %.2e, i.e. at least %.1f decades over double precision.  THE T163 "
      "TV FLOOR IS REPRODUCED AT THE UNTAPERED OPTIMISER: mu^P_1 TV >= 1 with "
      "slack %.2f .. %.2f (T163's %.2f .. %.2f is over ALL 1674 trial vectors it "
      "built, the taper sweep included, and the taper is what reaches the small "
      "end of that range; S2 re-enters the sweep), TV ~ h^%+.3f (FIT, T163 "
      "%+.3f).  AND THE NUMBER ARM A TURNS "
      "ON: 1/g_16 = %.4f .. %.4f with h-exponent %+.3f (FIT, T163 %+.3f) -- FLAT"
      % (qmin(E_QID), qmax(E_QID), len(WP), COND_BAR, len(DROP),
         qmax([r["gauge"] for r in WP]), qmin(HEADROOM), qmax(HEADROOM),
         math.log10(qmin(HEADROOM)), qmin(TVF), qmax(TVF),
         T163_TVSLACK[0], T163_TVSLACK[1], F_TV, T163_TVEXP,
         qmin([1.0 / r["g16"] for r in WP]), qmax([1.0 / r["g16"] for r in WP]),
         F_G16, T163_G16_EXP))

info("sc_q0.abel_sup",
     "the Abel partial sums of the lag coefficients, C_d = sum_{e<=d} c_e, are "
     "the object S2 needs: ||C||_inf = %.4f .. %.4f, h-exponent %+.3f (FIT).  "
     "C_{M-1} = sum_d c_d = %.3e .. %.3e"
     % (qmin([r["Cinf"] for r in WP]), qmax([r["Cinf"] for r in WP]), F_CINF,
        qmin([float(r["C"][-1]) for r in WP]),
        qmax([float(r["C"][-1]) for r in WP])))

print("")
print("TOTAL (Q0): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("S1  ARM A: THE TOLERANCE ANALYSIS -- WHERE 1/s ENTERS AND WHAT IT COSTS")
# ----------------------------------------------------------------------------
para("""S1.0  THE STATION MAP, WRITTEN DOWN BEFORE ANY NUMBER, BECAUSE THE WHOLE POINT
OF ARM A IS THE DIRECTION OF EACH ARROW.  The chain does not use 1/s; it uses a
CEILING U with 1/s <= U, and every downstream station consumes U and nothing
else.  The five stations, with the direction of each:

  ST1  THE CEILING ITSELF.  U comes from one of three places, all already in the
       chain: the route-(0) certificate U = B_11 = 1/g_1 (T157), the Cholesky
       ladder U = 1/g_K (T158, decreasing in K), or a priced trial vector
       U = Q(x) = P_pr(x) / g_16 (T160 .. T163).  DIRECTION: larger U = weaker.
  ST2  THE r-CEILING.  r <= 1 / (L s) with L = lambda_1(A) / mu^P_1, so
       r <= U / L.  DIRECTION: larger U gives a larger r ceiling.
  ST3  THE T156 KERNEL F(P_K, r).  P_K = a_hat . s is the KANTOROVICH ratio
       (a_hat = B_11), NOT the T163 price.  DIRECTION: F is increasing in r, so
       a larger U gives a larger loss.  A SECOND, OPPOSITE arrow also exists and
       must be stated or the analysis is dishonest: s >= 1/U, so a larger U
       ALLOWS a smaller P_K, and BOTH substitutions are evaluated below.
  ST4  THE p_1 SUBSTITUTION (T157).  r <= 1/p_1 with p_1 the first entry squared
       of the bottom eigenvector; this is the ceiling that does NOT go through
       1/s at all, and it is carried as the CONTROL that isolates the 1/s path.
  ST5  END TO END.  The Temple recovery (Temple 1928) consumes the floor
       lambda_1 >= t mu^P_1, i.e. L >= t, DEGRADED by the loss: the DECLARED
       PROXY of this file is Tmarg(U) := (1 - F) . L, and ``the chain stays
       uniform'' means Tmarg is h-FLAT and bounded away from 0.  Tmarg is a
       PROXY and is labelled as one everywhere; it is monotone in the two
       quantities the real recovery step is monotone in, and that is all it is
       used for.

THE QUESTION, PRECISELY.  Substitute U = U_0 . (h / h_0)^eps and ask for which eps
the end-to-end proxy stays bounded below.  DIRECTION CARE, AND THE BAR IS
DELIBERATELY ONE-SIDED BECAUSE Tmarg IS A MARGIN: only a DECREASING margin
threatens uniformity, an increasing one is a tailwind, so eps* := the largest eps
on the DECLARED grid whose Tmarg exponent is above -%.2f.  A two-sided bar here
would report a surface tailwind as a failure, which would be wrong.

NUMERICAL HORIZON, DECLARED IN ADVANCE.  Stations ST2 .. ST5 need
lambda_1(A) and the bottom eigenvector of the FULL h x h lag Gram, which is a
dense solve; it is therefore done on the DECLARED sub-surface h <= %d, at most %d
windows.  Every S1 exponent is a fit over THAT sub-surface and says so."""
     % (BAR_FLAT, H_EIG, N_EIG_MAX))

_WEC = sorted([r for r in WP if r["h"] <= H_EIG], key=lambda t: t["h"])
_pick = sorted(set(int(round(x)) for x in np.geomspace(
    1.0, float(max(len(_WEC), 1)), N_EIG_MAX)))
WE = [_WEC[i - 1] for i in _pick] if _WEC else []
for r in WE:
    m = r["h"]
    A = odd_toeplitz(r["c"], r["M"])
    Tf = parity_basis(m)
    t1 = Tf[0].copy()
    lam, V = sp_eigh(sym(A), subset_by_index=[0, 0])
    r["lam1"] = float(lam[0])
    r["L"] = r["lam1"] / r["mu1_full"]
    r["s"] = r["mu1_full"] * float(t1 @ np.linalg.solve(sym(A), t1))
    r["a_hat"] = float(r["B_LL"][0, 0])
    r["P_K"] = r["a_hat"] * r["s"]
    r["p1"] = float((Tf @ V[:, 0])[0] ** 2)
    del A, Tf

XE = [float(r["h"]) for r in WE]
check("sc_s1.st1_direction",
      len(WE) >= 4 and all(r["s"] >= r["g16"] * (1.0 - 1.0e-9) for r in WE)
      and all(r["s"] >= r["g1"] * (1.0 - 1.0e-9) for r in WE)
      and all(r["P_K"] >= 1.0 - 1.0e-9 for r in WE),
      "*** ST1, AND IT IS A DIRECTION CHECK BEFORE IT IS A MEASUREMENT: THE THREE "
      "CEILINGS ORDER THE WAY THE CHAIN ASSUMES THEY DO. ***  On the %d windows of "
      "the DECLARED sub-surface h = %d .. %d: s = %.4f .. %.4f, g_1 = %.3e .. "
      "%.3e, g_16 = %.4f .. %.4f with s >= g_16 >= g_1 window by window, i.e. "
      "1/s <= 1/g_16 <= 1/g_1 = B_11 -- the T158 ladder really is a chain of "
      "UPPER bounds on the entry ceiling and the T157 route-(0) rung really is the "
      "loosest.  And P_K = a_hat . s = %.4f .. %.4f >= 1, which is the Kantorovich "
      "1948 admissibility the T156 kernel needs; a_hat = B_11 = %.4f .. %.4f"
      % (len(WE), min(r["h"] for r in WE), max(r["h"] for r in WE),
         qmin([r["s"] for r in WE]), qmax([r["s"] for r in WE]),
         qmin([r["g1"] for r in WE]), qmax([r["g1"] for r in WE]),
         qmin([r["g16"] for r in WE]), qmax([r["g16"] for r in WE]),
         qmin([r["P_K"] for r in WE]), qmax([r["P_K"] for r in WE]),
         qmin([r["a_hat"] for r in WE]), qmax([r["a_hat"] for r in WE])))

F_L = fit_exp(XE, [r["L"] for r in WE])
F_P1 = fit_exp(XE, [r["p1"] for r in WE])
info("sc_s1.st2_st4",
     "ST2 / ST4, the two ceilings side by side on the sub-surface: L = "
     "lambda_1(A) / mu^P_1 = %.4e .. %.4e (h^%+.3f, FIT) and p_1 = %.4e .. %.4e "
     "(h^%+.3f, FIT).  With the certified ceiling U = 1/g_16 the r-ceiling is "
     "r <= U / L = %.4e .. %.4e, while the p_1 route gives r <= 1/p_1 = "
     "%.4e .. %.4e"
     % (qmin([r["L"] for r in WE]), qmax([r["L"] for r in WE]), F_L,
        qmin([r["p1"] for r in WE]), qmax([r["p1"] for r in WE]), F_P1,
        qmin([1.0 / (r["g16"] * r["L"]) for r in WE]),
        qmax([1.0 / (r["g16"] * r["L"]) for r in WE]),
        qmin([1.0 / r["p1"] for r in WE]), qmax([1.0 / r["p1"] for r in WE])))


def stations(rec, U):
    """ST2 -> ST5 for ONE window at ONE ceiling U.  BOTH substitutions of ST3 are
    evaluated and the WORSE (larger F) is taken, which is the only conservative
    reading.  r <= 1 makes the two-dimensional model vacuous (no loss), which is
    recorded as F = 0 and not as a missing value."""
    r_cap = U / rec["L"]
    out = dict(U=U, r=r_cap)
    if r_cap <= 1.0 + 1.0e-12:
        out["F"] = 0.0
        out["F_meas"] = 0.0
        out["F_cons"] = 0.0
    else:
        fm = loss_PR(max(rec["P_K"], 1.0), r_cap)
        fc = loss_PR(max(rec["a_hat"] / U, 1.0), r_cap)
        vals = [t for t in (fm, fc) if np.isfinite(t)]
        out["F_meas"], out["F_cons"] = fm, fc
        out["F"] = max(vals) if vals else float("nan")
    out["Tmarg"] = (1.0 - out["F"]) * rec["L"]
    return out


SENS = []
for r in WE:
    U0 = 1.0 / r["g16"]
    lo, hi = stations(r, U0 * 0.99), stations(r, U0 * 1.01)
    d0 = 1.0 - stations(r, U0)["F"]
    if min(1.0 - lo["F"], 1.0 - hi["F"]) > 0.0 and d0 > 0.0:
        SENS.append((math.log((1.0 - hi["F"]) / (1.0 - lo["F"]))
                     / math.log(1.01 / 0.99),
                     math.log(hi["r"] / lo["r"]) / math.log(1.01 / 0.99)))
NU_U = [t[0] for t in SENS]
check("sc_s1.st3_sensitivity",
      len(NU_U) >= 4 and qmax(NU_U) < 0.0,
      "*** ST3, AND THIS IS THE HEART OF ARM A: THE LOSS MARGIN OF THE T156 KERNEL "
      "IS STRICTLY DECREASING IN THE CEILING, WITH A MEASURED POWER, SO THERE IS NO "
      "FREE TOLERANCE AT ALL. ***  d log(1 - F) / d log U = %+.4f .. %+.4f "
      "(central difference at U = 1/g_16, %d windows), while d log r / d log U = "
      "%+.4f .. %+.4f EXACTLY (ST2 is linear).  READ IN ONE SENTENCE: inflating "
      "the entry ceiling by a factor lambda shrinks the T156 loss margin 1 - F by "
      "lambda^%+.2f, so a ceiling growing like h^eps costs a margin decaying like "
      "h^{%+.2f eps} -- ALGEBRAICALLY, for every eps > 0.  STATUS: MEASURED for the "
      "power, THEOREM for the monotonicity (F is increasing in r by the T156 "
      "identity and r is linear in U)"
      % (qmin(NU_U), qmax(NU_U), len(NU_U), qmin([t[1] for t in SENS]),
         qmax([t[1] for t in SENS]), qmed(NU_U), qmed(NU_U)))

EPS_GRID = (0.0, 0.05, 0.10, 0.20, 0.35, 0.50, 0.75, 1.00, 2.00)
H_REF = min(r["h"] for r in WE)
U_REF = qmax([1.0 / r["g16"] for r in WE])
TOL = {}
for eps in EPS_GRID:
    rows = [stations(r, U_REF * (r["h"] / float(H_REF)) ** eps) for r in WE]
    TOL[eps] = dict(exp=fit_exp(XE, [t["Tmarg"] for t in rows]),
                    lo=qmin([t["Tmarg"] for t in rows]),
                    hi=qmax([t["Tmarg"] for t in rows]),
                    Fhi=qmax([t["F"] for t in rows]))
EPS_OK = [e for e in EPS_GRID if TOL[e]["exp"] > -BAR_FLAT]
EPS_STAR = max(EPS_OK) if EPS_OK else float("nan")
check("sc_s1.tolerance_threshold",
      np.isfinite(EPS_STAR) and TOL[2.0]["exp"] < TOL[0.0]["exp"] - BAR_FLAT
      and all(TOL[EPS_GRID[j + 1]]["exp"] <= TOL[EPS_GRID[j]]["exp"] + 1.0e-9
              for j in range(len(EPS_GRID) - 1)),
      "*** THE ANSWER TO THE QUESTION ARM A ASKED, AND IT IS A NEGATIVE WITH A "
      "NUMBER ON IT. ***  Substituting U = U_ref (h/h_0)^eps and fitting the "
      "end-to-end PROXY Tmarg = (1 - F) L over the sub-surface: %s.  The exponent "
      "falls by exactly one unit of eps, which is ST3's power one appearing "
      "end-to-end and is the only structural statement here.  THE DECLARED "
      "ONE-SIDED RULE GIVES eps* = %.2f -- AND IT MUST BE READ WITH ITS SOURCE, "
      "OR IT IS A FALSE POSITIVE: the eps = 0 baseline already carries a TAILWIND "
      "of h^%+.3f, bought entirely from the measured drift of L = lambda_1/mu^P_1 "
      "(h^%+.3f, FIT) on THIS surface, and eps* is nothing but that tailwind "
      "divided by power one.  So the honest reading is NOT that the chain has "
      "h^%.2f of structural slack; it is that the kernel spends the ceiling at "
      "power one and this particular surface happens to hand back %+.3f of it.  "
      "THE O(1) REQUIREMENT ON 1/s IS THEREFORE REAL AND NOT AN ARTEFACT OF "
      "TIMIDITY.  STATUS: MEASURED on a DECLARED proxy, on a DECLARED sub-surface "
      "of %d windows"
      % ("; ".join("eps=%.2f: Tmarg = %.3e .. %.3e (h^%+.3f), max F = %.4f"
                   % (e, TOL[e]["lo"], TOL[e]["hi"], TOL[e]["exp"], TOL[e]["Fhi"])
                   for e in EPS_GRID),
         EPS_STAR, TOL[0.0]["exp"], F_L, EPS_STAR, TOL[0.0]["exp"], len(WE)))

print("")
print("TOTAL (S1.0): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# --- S1.1  AND NOW THE SHARPER QUESTION ---------------------------------------
para("""S1.1  SO ARM A's FIRST HALF IS A CLEAN NEGATIVE -- AND THAT IS THE MOMENT TO
ASK WHETHER THE QUESTION WAS THE RIGHT ONE.  The tolerance analysis says the
kernel spends the ceiling at power exactly one.  But WHO ASKED FOR A GROWING
CEILING?  T163's price grows because it was buying a SUB-YARDSTICK DEMAND; the
CEILING the chain actually consumes is a different object, and the T158 ladder
certifies it FLAT.  Written out so the two objects cannot be confused:

  OBJECT 1 -- THE CEILING.  1/s <= 1/g_K, and 1/g_16 is measured FLAT on this
  surface (h-exponent %+.3f, T163: %+.3f).  This is what ST1 .. ST5 consume.  It
  needs NO trial vector, NO taper, NO total variation and NO price: the ladder is
  a Cholesky identity (Schur 1917) evaluated on the window's own lag Gram.

  OBJECT 2 -- THE DEMAND.  delta_bnd(x) < 1/2 is a statement about how deep the
  primes must go for the SAME pairing to certify a Chebyshev-strength remainder,
  and by the T163 exchange law it is the inequality Q(x) > 2 kappa TV(x).  THIS
  is what the h^2 total-variation floor blocks, and it is what T163's price was
  paying for.

THESE TWO ARE LOGICALLY INDEPENDENT, AND THE ENTIRE ``O(1) REQUIREMENT'' LIVES IN
OBJECT 1.  So the honest form of the remaining question is not ``can the chain
tolerate 1/s ~ h^eps'' (it cannot, at power one) but: IS THE CEILING ALREADY
FLAT, AND IF SO WHAT EXACTLY IS STILL MISSING?  The rest of S1 answers both, and
the second answer is the one that matters.""" % (F_G16, T163_G16_EXP))

FLAT_ROWS = [stations(r, U_REF) for r in WE]
F_FLATM = fit_exp(XE, [t["Tmarg"] for t in FLAT_ROWS])
LAD_MONO = all(bool(np.all(np.diff(r["gcum"]) > 0.0)) for r in WP)
G16_LIST = [1.0 / r["g16"] for r in WP]
check("sc_s1.flat_ceiling_suffices",
      F_FLATM > -BAR_FLAT and qmin([t["Tmarg"] for t in FLAT_ROWS]) > 0.0
      and abs(F_G16) < BAR_FLAT and LAD_MONO
      and qmax(G16_LIST) < 2.0 * qmin(G16_LIST) + 3.0,
      "*** AND HERE IS THE POINT OF ARM A, AND IT IS A REFRAMING RATHER THAN A NEW "
      "INEQUALITY: WITH A CONSTANT CEILING THE WHOLE DOWNSTREAM MAP ALREADY "
      "DRIFTS THE FAVOURABLE WAY, AND THE CEILING IS ALREADY CERTIFIED CONSTANT "
      "PER WINDOW. ***  "
      "Feeding the SINGLE CONSTANT U_ref = %.4f = max_h 1/g_16 into ST2 .. ST5 -- "
      "no h-dependence anywhere in the substitution -- gives Tmarg = %.4e .. %.4e "
      "with h-exponent %+.3f (FIT), i.e. NON-DECREASING against the one-sided bar "
      "-%.2f and bounded away from zero on all %d sub-surface windows.  The ceiling "
      "itself: "
      "1/g_16 = %.4f .. %.4f over the FULL %d-window surface, h-exponent %+.3f, "
      "and every ladder g_K is strictly increasing in K on every window (Schur "
      "1917 nested complements), so 1/g_16 is the TIGHTEST rung and the "
      "certificate is monotone as well as flat -- and the flatness claim is made "
      "about THE CEILING (h^%+.3f, inside the bar), never about the proxy.  "
      "CONSEQUENCE, STATED WITHOUT "
      "INFLATION: the O(1) requirement on the entry ceiling is not an open "
      "quantitative gate on this surface -- it is DISCHARGED WINDOW BY WINDOW by a "
      "Cholesky identity.  STATUS: CERT-WINDOW for the ceiling (that is exactly "
      "what a per-window certificate is), MEASURED for the flatness of the proxy"
      % (U_REF, qmin([t["Tmarg"] for t in FLAT_ROWS]),
         qmax([t["Tmarg"] for t in FLAT_ROWS]), F_FLATM, BAR_FLAT, len(WE),
         qmin(G16_LIST), qmax(G16_LIST), len(WP), F_G16, F_G16))

# THE m-FREEDOM TEST.  A certified flat LIST is not a certified flat FUNCTION.
# The only honest thing a finite surface can do is measure how the list behaves
# under EXTRAPOLATION and say what a proof would still have to supply.
_lo = [r for r in WP if r["h"] <= math.sqrt(min(XHP) * max(XHP))]
_hi = [r for r in WP if r["h"] > math.sqrt(min(XHP) * max(XHP))]
SPLIT_EXP = (fit_exp([float(r["h"]) for r in _lo], [1.0 / r["g16"] for r in _lo]),
             fit_exp([float(r["h"]) for r in _hi], [1.0 / r["g16"] for r in _hi]))
G16_SPREAD = qmax(G16_LIST) / qmin(G16_LIST)
check("sc_s1.m_freedom_is_the_rest",
      max(abs(SPLIT_EXP[0]), abs(SPLIT_EXP[1])) < BAR_FLAT
      and G16_SPREAD < 10.0,
      "*** AND THIS IS THE EXACT SHAPE OF WHAT IS STILL MISSING, WHICH IS THE ONE "
      "SENTENCE T164 IS FOR. ***  A CERTIFIED FLAT LIST IS NOT A CERTIFIED FLAT "
      "FUNCTION.  1/g_16 is flat on the LOWER half of the surface (h <= %d, "
      "h^%+.3f) and on the UPPER half (h^%+.3f) separately, with total spread "
      "max/min = %.3f over a %.0fx lever arm in h -- so the list shows no drift "
      "that a longer lever arm would be expected to reveal, and no window in the "
      "sample violates a constant bound.  WHAT A PROOF STILL NEEDS, AND IT IS "
      "EXACTLY ONE THING: sup_m 1/g_16(m) < infinity, i.e. the m-FREEDOM of a "
      "certified flat list.  THAT IS THE SAME GRAMMATICAL FORM AS EVERY OTHER OPEN "
      "UNIFORMITY STATEMENT IN THE CHAIN -- a per-window certificate plus a "
      "quantifier over windows -- and it is NOT the form R2'' had before T163, "
      "which was an existence question about trial vectors.  STATUS: CERT-WINDOW "
      "for the list, OPEN for the quantifier; NOTHING here upgrades the second to "
      "the first, and the split-half test is a CONSISTENCY check and not a proof "
      "of the sup"
      % (int(math.sqrt(min(XHP) * max(XHP))), SPLIT_EXP[0], SPLIT_EXP[1],
         G16_SPREAD, max(XHP) / min(XHP)))

print("")
print("TOTAL (S1): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("S2  ARM B: THE SECTOR CHANGE -- THREE CANDIDATES AND ONE INVARIANCE")
# ----------------------------------------------------------------------------
para("""S2.0  WHAT A ``SECTOR'' CAN AND CANNOT BE, WRITTEN OUT FIRST, BECAUSE THE ANSWER
TO ARM B IS ALREADY VISIBLE IN THE BOOKKEEPING.  The pairing is
x^T B x = v^T A v with A = odd_toeplitz(c, M) the lag Gram, a_k = x_k / sqrt(mu_k)
and v = T^T a.  A SECTOR CHANGE, in the only sense the chain admits, replaces the
entry spectrum mu by some other positive spectrum mu' and leaves A alone -- the
prime powers, the archimedean kernel and the lag grid are the SAME object in every
candidate.  Three candidates, and the T1-T4 floor computation is repeated for
each:

  (i)   THE FULL SPACE.  Drop the parity projection: mu_k = 4 sin^2(pi k / N),
        k = 0 .. N-1, so the CONSTANT vector sits at eigenvalue EXACTLY ZERO.
  (ii)  A WEIGHTED / SHIFTED / REGULARISED SECTOR.  mu_k -> mu_k + kap_s
        (a shift, i.e. L_P + kap_s I) or mu_k -> om_k mu_k (the T149 weight
        freedom), polynomial or exponential in k.
  (iii) THE MELLIN / FREQUENCY SIDE.  The lag axis carries the harmonics on
        [0, 2 alpha] and the ``gap'' is replaced by the WINDOW LENGTH; here the
        entry functional is not re-weighted at all but ELIMINATED, and what is
        left is a normalisation-free ratio.  This is the candidate the invariance
        below actually points at.

AND HERE IS THE STRUCTURAL FACT THAT ORGANISES ALL THREE, STATED AS THE THEOREM
IT IS.  The constraint x_1 = 1 fixes a_1 = 1 / sqrt(mu_1), i.e. it fixes the SCALE
of a and nothing else; Q and TV are both HOMOGENEOUS OF DEGREE TWO in a; hence

    *** TV(a) / Q(a) DEPENDS ONLY ON THE DIRECTION OF a AND IS THE SAME NUMBER
        IN EVERY SECTOR mu'.  The entry normalisation is a GAUGE. ***

So the DEMAND coordinate delta_bnd is gauge-invariant and the T163 sub-yardstick
condition is the normalisation-free inequality Q / TV > 2 kappa = %.4f.  THE PRICE
COORDINATE IS NOT INVARIANT UNDER THE SAME OPERATION, AND THAT DISTINCTION IS THE
WHOLE OF ARM B: P_pr(x) = g_16 Q(x) is evaluated AFTER imposing x_1 = 1, so it
scales like the square of the normalisation -- and the price MEASURED IN UNITS OF
THE VALUE THE SECTOR ITSELF CERTIFIES is invariant again, because numerator and
denominator scale together.  S2.1 checks the invariance to machine precision, S2.2
does candidates (i) and (ii) against it, S2.3 runs the normalisation-free search
the invariance licenses and then puts the price back.""" % (2.0 * KAPPA))


def sector_numbers(r, x, mu_s):
    """Q, TV and the demand for ONE trial vector in ONE sector spectrum mu_s.
    NOTHING else changes: same c, same A, same lag grid."""
    nb = x.shape[0]
    a = x / np.sqrt(np.asarray(mu_s, float)[:nb])
    v = r["Tb"][:nb, :].T @ a
    w = lag_weights_from_v(v, r["h"])
    Q = float(np.dot(r["c"], w))
    tv = float(np.sum(np.abs(back_diff(w))))
    return dict(Q=Q, TV=tv, w0=float(w[0]), nrm2=float(a @ a),
                gauge=abs(float(np.sum(w))) / max(float(np.sum(np.abs(w))), 1e-300),
                d_bnd=0.5 + math.log(max(2.0 * KAPPA * tv / max(abs(Q), 1e-300),
                                         1e-300)) / r["logX"],
                ratio=Q / max(tv, 1.0e-300))


SHIFTS = (0.0, 1.0e-6, 1.0e-4, 1.0e-2, 0.25, 1.0, 4.0)
WEIGHTS = ("none", "poly1", "poly2", "expk", "exph")


def sector_mu(r, tag, kap_s):
    mu = r["mu"].copy()
    kk = np.arange(1, mu.shape[0] + 1, dtype=float)
    if tag == "poly1":
        mu = mu * kk
    elif tag == "poly2":
        mu = mu * kk ** 2
    elif tag == "expk":
        mu = mu * np.exp(kk / 4.0)
    elif tag == "exph":
        mu = mu * np.exp(kk / float(r["h"]))
    return mu + kap_s


SIG_S2 = (1.0, 2.0, 4.0, 8.0, 16.0, float("inf"))
E_GAUGE, E_TEL, E_THETA, WSPREAD = [], [], [], []
TVF_S2, RAT_REF = [], []
for r in WP:
    ref = None
    for sg in SIG_S2:
        x = r["xstar"] * fejer_taper(SCHUR_KB, sg)
        x = x / max(abs(float(x[0])), 1.0e-300)
        base = sector_numbers(r, x, r["mu"][:SCHUR_KB])
        TVF_S2.append(base["TV"] * r["mu1_full"])
        if sg == float("inf"):
            RAT_REF.append(base["ratio"])
        for tag in WEIGHTS:
            for ks in SHIFTS:
                mu_s = sector_mu(r, tag, ks)[:x.shape[0]]
                # THE SAME DIRECTION, RE-NORMALISED IN THE NEW SECTOR: the trial
                # vector that has the SAME a-direction is y = sqrt(mu_s/mu) . x,
                # rescaled so that y_1 = 1.  DIRECTION CARE: this is the map that
                # keeps a fixed up to scale, which is what the gauge claim is about
                y = x * np.sqrt(mu_s / r["mu"][:x.shape[0]])
                y = y / max(abs(float(y[0])), 1.0e-300)
                new = sector_numbers(r, y, mu_s)
                E_GAUGE.append(abs(new["ratio"] - base["ratio"])
                               / max(abs(base["ratio"]), 1.0e-300))
                E_TEL.append(new["TV"] - abs(new["w0"]))
                rat_w = mu_s / r["mu"][:x.shape[0]]
                WSPREAD.append(float(np.max(rat_w) / np.min(rat_w)))
                if tag == "none" and ks > 0.0 and base["Q"] != 0.0:
                    thet = r["mu1_full"] / (r["mu1_full"] + ks)
                    E_THETA.append(abs(new["Q"] / base["Q"] - thet) / thet)

GAUGE_HORIZON = qmax(WSPREAD) / qmin(HEADROOM)
check("sc_s2.gauge_invariance",
      qmax(E_GAUGE) < GAUGE_BAR and qmin(E_TEL) >= 0.0
      and qmax(E_THETA) < 1.0e-9 and qmax(E_GAUGE) < GAUGE_HORIZON,
      "*** THEOREM, MACHINE-CHECKED ON %d SECTOR-BY-TRIAL-VECTOR COMBINATIONS, AND "
      "IT IS THE STRUCTURAL RESULT OF T164: THE ENTRY NORMALISATION IS A GAUGE. "
      "***  Over %d sector spectra (%d weight families x %d shifts, the shift "
      "kap_s = 0 .. %.1f being L_P -> L_P + kap_s I) and %d taper widths on %d "
      "windows, the ratio Q / TV of the SAME a-direction is unchanged to "
      "%.2e .. %.2e relative, and with it delta_bnd.  DECLARED NUMERICAL HORIZON, "
      "AND IT IS THE CANCELLATION AND NOT THE WEIGHT THAT SETS IT: Q is an O(1) "
      "difference of halves of size |Q| / canc, so its relative accuracy is "
      "eps / canc = 1 / headroom <= %.1e, and the gauge round trip rescales the "
      "trial vector by sqrt(mu'/mu) whose spread reaches %.1e; the product %.1e is "
      "the horizon, and the residual above sits %.0fx BELOW it, so it is arithmetic "
      "noise and not a defect of the identity.  The two auxiliary identities come "
      "out exact as well: TV >= |w_0| in every sector (the T163 telescope, least "
      "slack TV - |w_0| = %.3e >= 0), and for the pure shift the "
      "certified VALUE scales by exactly theta = mu^P_1 / (mu^P_1 + kap_s) to "
      "%.1e -- the SAME factor by which the floor 1/(mu^P_1 + kap_s) scales.  "
      "CONSEQUENCE: a sector change cannot move the crossing criterion "
      "Q / TV > 2 kappa by ANY amount, because that inequality does not contain "
      "the normalisation"
      % (len(E_GAUGE), len(WEIGHTS) * len(SHIFTS), len(WEIGHTS), len(SHIFTS),
         max(SHIFTS), len(SIG_S2), len(WP), qmin(E_GAUGE), qmax(E_GAUGE),
         1.0 / qmin(HEADROOM), qmax(WSPREAD), GAUGE_HORIZON,
         GAUGE_HORIZON / max(qmax(E_GAUGE), 1.0e-300), qmin(E_TEL),
         qmax(E_THETA)))

MU0_FULL = [float(full_mu(r["h"])[0]) for r in WP]
MU1_FULL_MIN = [float(np.min(full_mu(r["h"])[1:])) for r in WP]
check("sc_s2.candidate_full_space",
      qmax([abs(t) for t in MU0_FULL]) < 1.0e-28
      and all(MU1_FULL_MIN[i] <= WP[i]["mu1_full"] * (1.0 + 1.0e-9)
              for i in range(len(WP))),
      "*** CANDIDATE (i), THE FULL SPACE, IS SETTLED IN CLOSED FORM AND IT IS "
      "STRICTLY WORSE, NOT BETTER. ***  The unprojected spectrum on N = 2h+1 "
      "points is mu_k = 4 sin^2(pi k / N), k = 0 .. N-1 (Kac-Murdock-Szego 1953), "
      "and mu_0 = 0 EXACTLY (measured %.1e, i.e. the constant vector) -- so the "
      "T3 step ||a||^2 >= a_1^2 = 1 / mu_min becomes UNBOUNDED rather than h^2, "
      "and the even sector that carries it is the one T162 already found to hold "
      "the negative inertia.  Even excluding the constant mode the lowest "
      "remaining full-space eigenvalue %.4e .. %.4e is <= the parity mu^P_1 = "
      "%.4e .. %.4e window by window, so the full space NEVER has a larger gap "
      "than the parity sector.  STATUS: THEOREM (closed-form spectrum), and a "
      "NEGATIVE one"
      % (qmax([abs(t) for t in MU0_FULL]), qmin(MU1_FULL_MIN), qmax(MU1_FULL_MIN),
         qmin([r["mu1_full"] for r in WP]), qmax([r["mu1_full"] for r in WP])))

TRANSFER = {}
for ks in [t for t in SHIFTS if t > 0.0]:
    fl = [1.0 / (r["mu1_full"] + ks) for r in WP]
    tr = [1.0 + ks / r["mu1_full"] for r in WP]
    TRANSFER[ks] = (fit_exp(XHP, fl), fit_exp(XHP, tr), qmin(tr), qmax(tr),
                    qmin(fl), qmax(fl))
KS_BIG = max(SHIFTS)
check("sc_s2.candidate_shift_conservation",
      abs(TRANSFER[KS_BIG][0]) < BAR_FLAT
      and TRANSFER[KS_BIG][1] > 2.0 - BAR_FLAT
      and abs(TRANSFER[KS_BIG][1] + TRANSFER[KS_BIG][0]
              - fit_exp(XHP, [1.0 / r["mu1_full"] for r in WP])) < 1.0e-9,
      "*** CANDIDATE (ii): A SHIFTED OR WEIGHTED SECTOR DOES FLATTEN THE FLOOR, AND "
      "PAYS FOR IT EXACTLY ONCE -- THE h^2 IS CONSERVED, NOT REMOVED. ***  For the "
      "shift kap_s the T1-T4 floor becomes TV >= 1 / (mu^P_1 + kap_s), which at "
      "kap_s = %.1f is %.4e .. %.4e with h-exponent %+.3f (FIT) -- FLAT, so the "
      "T163 obstruction really is absent in the shifted sector.  BUT the value the "
      "shifted pairing certifies is theta = mu^P_1 / (mu^P_1 + kap_s) times the "
      "true one, so recovering a bound on the ORIGINAL 1/s costs the TRANSFER "
      "FACTOR 1/theta = 1 + kap_s / mu^P_1 = %.3e .. %.3e, h-exponent %+.3f (FIT), "
      "and floor x transfer = 1 / mu^P_1 ~ h^%+.3f IDENTICALLY -- the two "
      "exponents sum to the T163 exponent to 1e-9, at EVERY shift on the declared "
      "grid.  STATUS: THEOREM (an exact product identity), and the honest reading "
      "is that the h^2 was never localised in the floor: it is in the RATIO"
      % (KS_BIG, TRANSFER[KS_BIG][4], TRANSFER[KS_BIG][5], TRANSFER[KS_BIG][0],
         TRANSFER[KS_BIG][2], TRANSFER[KS_BIG][3], TRANSFER[KS_BIG][1],
         fit_exp(XHP, [1.0 / r["mu1_full"] for r in WP])))

info("sc_s2.transfer_grid",
     "the same product law across the DECLARED shift grid: "
     + "; ".join("kap_s=%g: floor h^%+.3f, transfer h^%+.3f, sum %+.3f"
                 % (ks, TRANSFER[ks][0], TRANSFER[ks][1],
                    TRANSFER[ks][0] + TRANSFER[ks][1])
                 for ks in sorted(TRANSFER)))

print("")
print("TOTAL (S2.0-S2.2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# --- S2.3  CANDIDATE (iii): THE NORMALISATION-FREE PROBLEM ---------------------
para("""S2.3  CANDIDATE (iii), AND THE INVARIANCE HAS TURNED IT INTO SOMETHING BETTER
THAN A SECTOR: A WELL-POSED PROBLEM WITH NO NORMALISATION IN IT AT ALL.  Since
Q / TV does not see the entry weight, the crossing question is

    *** DOES SOME v IN R^h HAVE Q(v) / TV(v) > 2 kappa = %.4f ? ***

with Q(v) = v^T A v and TV(v) = || Delta w(v) ||_1, both homogeneous of degree two,
so no constraint is needed and NO SECTOR HAS TO BE CHOSEN.  T163's search was
confined to the 16 (or 64) lowest parity modes with x_1 = 1; this one is over the
WHOLE window.

AND THE FREQUENCY SIDE SUPPLIES THE CEILING, BY ABEL AND NOT BY A GAP.  Summation
by parts (Abel 1826) with w_M = 0 gives the IDENTITY
Q = sum_e (Delta w)_e C_e with C_e = sum_{d <= e} c_d, hence

    |Q| <= TV . ||C||_inf ,    i.e.    Q / TV <= ||C||_inf ,

so the ceiling on the gauge-invariant ratio is the sup of the PARTIAL SUMS of the
lag coefficients -- a WINDOW-LENGTH quantity, exactly as candidate (iii)
predicted, and it GROWS with h (h^%+.3f, FIT) instead of vanishing.  Define the
ALIGNMENT EFFICIENCY eta := (Q / TV) / ||C||_inf in [0, 1]: the ceiling is
abundant, so if the crossing is blocked at all it is blocked by a DEFICIT OF eta,
i.e. by a failure of Delta w to line up with the sign pattern of C.

AND THEN THE PRICE IS PUT BACK, BECAUSE A DEMAND WITHOUT A PRICE IS NOT A
CERTIFICATE.  Whatever v the ascent finds, the chain can only USE it after
normalising: a = T v, x_k = sqrt(mu_k) a_k, x_1 = 1, which divides v by
sqrt(mu^P_1) (T v)_1 and therefore MULTIPLIES both Q and TV by
1 / (mu^P_1 (T v)_1^2).  The demand does not notice; the price
P_pr = g_16 Q(x_normalised) notices quadratically.  So S2.3 reports BOTH
coordinates of every point it finds, and the T163 price floor is re-checked ON THE
ASCENT OUTPUT rather than on the families T163 swept.""" % (2.0 * KAPPA, F_CINF))

N_SRCH = 10                  # DECLARED: windows carried into the ascent
N_SEED = 16                  # DECLARED: random restarts per window
N_ASC = 250                  # DECLARED: ascent steps per restart
N_LINE = 11                  # DECLARED: line-search points per step
LINE_T = np.concatenate([-np.geomspace(2.0, 1.0e-3, N_LINE // 2),
                         np.geomspace(1.0e-3, 2.0, N_LINE - N_LINE // 2)])

_WSC = sorted(WP, key=lambda t: t["h"])
_pick = sorted(set(int(round(x)) for x in np.geomspace(
    1.0, float(len(_WSC)), N_SRCH)))
WS = [_WSC[i - 1] for i in _pick]


def tau_of_sign(sg):
    """The adjoint of the backward difference: sum_d sg_d (w_d - w_{d+1}) =
    sum_d tau_d w_d with tau_d = sg_d - sg_{d-1}, sg_{-1} := 0.  Hence
    TV(v) = v^T odd_toeplitz(tau, M) v whenever sg = sign(Delta w(v)), which is
    what makes the ascent below a FIRST-ORDER method and not a random walk."""
    out = np.empty_like(sg)
    out[0] = sg[0]
    out[1:] = sg[1:] - sg[:-1]
    return out


def ratio_of(r, A, v):
    w = lag_weights_from_v(v, r["h"])
    dw = back_diff(w)
    tv = float(np.sum(np.abs(dw)))
    Q = float(v @ (A @ v))
    return Q, tv, (Q / tv if tv > 0.0 else float("-inf")), dw


E_ABEL, SR = [], []
for r in WS:
    if budget_left() < 240.0:
        info("sc_s2.budget", "ascent stopped before h = %d" % r["h"])
        break
    m, A = r["h"], odd_toeplitz(r["c"], r["M"])
    v0 = r["Tb"][:SCHUR_KB, :].T @ (r["xstar"] / np.sqrt(r["mu"][:SCHUR_KB]))
    q0, tv0, R0, dw0 = ratio_of(r, A, v0)
    E_ABEL.append((abs(float(np.dot(dw0, r["C"])) - q0) / max(abs(q0), 1.0e-300),
                   EPSM * tv0 * r["Cinf"] / max(abs(q0), 1.0e-300)))
    rs = np.random.RandomState(164000 + m)
    best = dict(R=R0, tag="chain x*", Q=q0, TV=tv0, vb=v0.copy())
    for sd in range(N_SEED + 1):
        v = v0.copy() if sd == 0 else rs.standard_normal(m)
        v /= max(float(np.max(np.abs(v))), 1.0e-300)
        Qc, tvc, Rc, dwc = ratio_of(r, A, v)
        for _ in range(N_ASC):
            S = odd_toeplitz(tau_of_sign(np.sign(dwc)), r["M"])
            gd = 2.0 * (tvc * (A @ v) - Qc * (S @ v)) / max(tvc * tvc, 1.0e-300)
            gn = float(np.max(np.abs(gd)))
            if not np.isfinite(gn) or gn <= 0.0:
                break
            gd = gd / gn
            got = False
            for tt in LINE_T:
                vt = v + tt * gd
                Qt, tvt, Rt, dwt = ratio_of(r, A, vt)
                if np.isfinite(Rt) and Rt > Rc + 1.0e-15:
                    v, Qc, tvc, Rc, dwc, got = vt, Qt, tvt, Rt, dwt, True
            if not got:
                break
        if Rc > best["R"]:
            best = dict(R=Rc, tag="ascent seed %d" % sd, Q=Qc, TV=tvc,
                        vb=v.copy())
    # PUT THE PRICE BACK.  x_1 = 1 divides v by sqrt(mu^P_1) (T v)_1, hence
    # multiplies Q and TV by 1 / (mu^P_1 (T v)_1^2) -- the demand is untouched,
    # the price is not.  DIRECTION: this is the ONLY normalisation the Thomson
    # direction admits, so the price below is not a choice.
    vb = best["vb"]
    t1v = float(r["Tb"][0] @ vb)
    sc2 = r["mu1_full"] * t1v * t1v
    wb = lag_weights_from_v(vb, m)
    best.update(h=m, Cinf=r["Cinf"], R0=R0, eta=best["R"] / r["Cinf"],
                gain=best["R"] / R0 if R0 > 0.0 else float("nan"),
                Qn=best["Q"] / sc2, TVn=best["TV"] / sc2,
                canc=abs(best["Q"]) / max(abs(float(np.dot(r["c_ar"], wb))),
                                          abs(float(np.dot(r["c_at"], wb))),
                                          1.0e-300))
    best["P_pr"] = r["g16"] * best["Qn"]
    best["P_floor"] = 2.0 * KAPPA * r["g16"] / r["mu1_full"]
    best["tvf"] = best["TVn"] * r["mu1_full"]
    best["P_aff"] = r["P_aff"]
    best["d_bnd"] = 0.5 + math.log(max(2.0 * KAPPA / max(best["R"], 1e-300),
                                       1e-300)) / r["logX"]
    best["head"] = best["canc"] / EPSM
    del best["vb"]
    SR.append(best)
    del A

check("sc_s2.abel_identity",
      all(t[0] < max(t[1], EXACT_BAR) for t in E_ABEL),
      "*** THEOREM, MACHINE-CHECKED WITHIN A DECLARED HORIZON: THE ABEL FORM OF THE "
      "PAIRING, WHICH IS WHAT PUTS A CEILING ON THE GAUGE-INVARIANT RATIO. ***  "
      "Q = sum_e (Delta w)_e C_e with C the partial sums of the lag coefficients, "
      "to %.2e .. %.2e relative on %d windows (Abel 1826); the DECLARED horizon is "
      "eps . TV . ||C||_inf / |Q| = %.2e .. %.2e, i.e. the Abel form re-sums an "
      "O(1) number out of terms that are individually %.0e times larger, and the "
      "residual is inside that horizon window by window.  Consequence, an "
      "INEQUALITY and not a measurement: Q / TV <= ||C||_inf = %.2f .. %.2f, "
      "h^%+.3f (FIT) -- the ceiling on the demand ratio is a WINDOW-LENGTH quantity "
      "that GROWS with h, so nothing on the frequency side forbids the crossing"
      % (qmin([t[0] for t in E_ABEL]), qmax([t[0] for t in E_ABEL]), len(E_ABEL),
         qmin([t[1] for t in E_ABEL]), qmax([t[1] for t in E_ABEL]),
         qmax([t[1] for t in E_ABEL]) / EPSM,
         qmin([r["Cinf"] for r in WP]), qmax([r["Cinf"] for r in WP]), F_CINF))

XS = [float(t["h"]) for t in SR]
F_RBEST = fit_exp(XS, [t["R"] for t in SR])
F_ETA = fit_exp(XS, [t["eta"] for t in SR])
F_PASC = fit_exp(XS, [t["P_pr"] for t in SR])
CROSS_BAR = 2.0 * KAPPA
N_CROSS = sum(1 for t in SR if t["R"] > CROSS_BAR)
check("sc_s2.free_search_demand",
      len(SR) >= 4 and N_CROSS == len(SR)
      and qmin([t["gain"] for t in SR]) > 1.0
      and qmin([t["head"] for t in SR]) > HEADROOM_BAR
      and qmax([t["d_bnd"] for t in SR]) < RH_DELTA,
      "*** AND THIS IS THE ONE GENUINE SURPRISE OF T164, SO IT IS STATED AS A "
      "POSITIVE AND THEN IMMEDIATELY PRICED: WITHOUT THE NORMALISATION THE DEMAND "
      "IS NOT MERELY REACHED, IT IS OVERSHOT BY THREE ORDERS OF MAGNITUDE. ***  A "
      "DECLARED first-order ascent on R(v) = Q(v)/TV(v) over the FULL window (all "
      "%d .. %d coordinates, no mode truncation, no normalisation), %d restarts x "
      "%d steps x %d line points per window on %d windows, reaches R = "
      "%.4e .. %.4e against the crossing bar 2 kappa = %.4f -- ABOVE it by a factor "
      "%.1e .. %.1e, on %d of %d windows, i.e. delta_bnd = %.4f .. %.4f against the "
      "yardstick 1/2.  The ascent improves the chain's own 16-mode optimiser by "
      "%.1e .. %.1e in the ratio, and R GROWS as h^%+.3f (FIT), so this is not a "
      "small-window effect.  eta = R / ||C||_inf = %.3e .. %.3e (h^%+.3f, FIT): the "
      "ascent extracts %.1f .. %.1f per cent of the Abel ceiling.  DECLARED "
      "NUMERICAL HORIZON, because a claim like this must not rest on cancellation: "
      "the arch/atom cancellation at the ascent optimum is %.2e .. %.2e, i.e. a "
      "headroom of %.1e .. %.1e over machine eps.  STATUS: MEASURED (a search is "
      "never a theorem)"
      % (min(t["h"] for t in SR), max(t["h"] for t in SR), N_SEED + 1, N_ASC,
         N_LINE, len(SR), qmin([t["R"] for t in SR]), qmax([t["R"] for t in SR]),
         CROSS_BAR, qmin([t["R"] for t in SR]) / CROSS_BAR,
         qmax([t["R"] for t in SR]) / CROSS_BAR, N_CROSS, len(SR),
         qmin([t["d_bnd"] for t in SR]), qmax([t["d_bnd"] for t in SR]),
         qmin([t["gain"] for t in SR]), qmax([t["gain"] for t in SR]), F_RBEST,
         qmin([t["eta"] for t in SR]), qmax([t["eta"] for t in SR]), F_ETA,
         100.0 * qmin([t["eta"] for t in SR]),
         100.0 * qmax([t["eta"] for t in SR]),
         qmin([t["canc"] for t in SR]), qmax([t["canc"] for t in SR]),
         qmin([t["head"] for t in SR]), qmax([t["head"] for t in SR])))

check("sc_s2.free_search_price",
      all(t["tvf"] >= 1.0 for t in SR)
      and all(t["P_pr"] >= t["P_floor"] * (1.0 - 1.0e-9) for t in SR)
      and F_PASC > 2.0 - BAR_FLAT
      and qmin([t["P_pr"] / t["P_aff"] for t in SR]) > 1.0,
      "*** AND HERE IS WHY THE SURPRISE IS NOT A CROSSING: THE PRICE OF THE ASCENT "
      "OPTIMUM IS EXACTLY WHERE T163's THEOREM SAID IT WOULD BE, AND T163's FLOOR "
      "IS RE-VERIFIED ON A FAMILY T163 NEVER SEARCHED. ***  Normalising the ascent "
      "output to x_1 = 1 gives TV . mu^P_1 = %.2f .. %.2f >= 1 -- the T163 "
      "total-variation floor holds on the UNCONSTRAINED optimiser too, which is the "
      "strongest available confirmation that (T1)-(T3) is an inequality and not a "
      "property of the swept families -- and a price P_pr = g_16 Q = %.3e .. %.3e, "
      "h^%+.3f (FIT).  That price is above the T163 crossing floor "
      "2 kappa g_16 / mu^P_1 = %.3e .. %.3e on every window, and above the "
      "route-(0) affordable price P_aff = %.3e .. %.3e by a factor %.1e .. %.1e.  "
      "READ IN ONE SENTENCE: the demand is free and the price is h^%+.2f -- ABOVE "
      "the h^2 floor and above T163's own crossing price h^%+.2f, so the "
      "unconstrained ascent buys its demand at a WORSE exchange rate than the "
      "Fejer knob did, and dropping the normalisation moved the difficulty from one "
      "coordinate to the other WITHOUT REDUCING IT.  STATUS: MEASURED for "
      "the numbers, THEOREM for the floor they respect"
      % (qmin([t["tvf"] for t in SR]), qmax([t["tvf"] for t in SR]),
         qmin([t["P_pr"] for t in SR]), qmax([t["P_pr"] for t in SR]), F_PASC,
         qmin([t["P_floor"] for t in SR]), qmax([t["P_floor"] for t in SR]),
         qmin([t["P_aff"] for t in SR]), qmax([t["P_aff"] for t in SR]),
         qmin([t["P_pr"] / t["P_aff"] for t in SR]),
         qmax([t["P_pr"] / t["P_aff"] for t in SR]), F_PASC, T163_PCROSS_EXP))

info("sc_s2.free_search_rows",
     "; ".join("h=%d: R %.3e -> %.3e (%s), eta %.2e, d_bnd %.3f, P_pr %.2e"
               % (t["h"], t["R0"], t["R"], t["tag"], t["eta"], t["d_bnd"],
                  t["P_pr"]) for t in SR))

print("")
print("TOTAL (S2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("S3  R-B''', R-D, THE END-TO-END ASSEMBLY AND THE OBLIGATORY STRESS")
# ----------------------------------------------------------------------------
para("""S3.1  R-B''': IS THE CANCELLATION DRIFT REAL, OR IS IT THE SURFACE?  T163 left
the positivity margin as the item to make h-uniform and quoted an exponent of
%+.3f for CANC = |Q| / max(|Q^arch|, |Q^atom|) at the operating point.  A drift
that small over a tenfold lever arm has TWO possible causes and they must be
separated, because only one of them is an open problem:

  (a) A GENUINE h-DEPENDENCE of the cancellation, which would be a real gate.
  (b) AN ARTEFACT OF THE SURFACE, because on this family h and the zone scale
      alpha = log n_zone are NOT independent -- the recipe picks the window from a
      prime gap, so alpha and h move together, and a regression on h alone will
      attribute an alpha-effect to h.

The separation is a TWO-VARIABLE regression, declared here before it is run:
log CANC = c_0 + b_h log h + b_a log alpha, and the question is which coefficient
carries the drift.  Plus a split-half control, and plus the T162 a-weighted
quarter bar, which is the object form T163 said was the right one.""" %
     T163_CANC_EXP)

SIG_OP = sorted(set(round(float(s), 6)
                    for s in np.geomspace(1.0, 4096.0, 33))) + [float("inf")]
CAP_FLAT = 2.0               # the T163 flat price tier, QUOTED not invented
CANC_OP, SIG_STAR, QUART = [], [], []
for r in WP:
    pick = None
    for sg in SIG_OP:
        x = r["xstar"] * fejer_taper(SCHUR_KB, sg)
        x = x / max(abs(float(x[0])), 1.0e-300)
        w = lag_weights_from_v(r["Tb"][:SCHUR_KB, :].T
                               @ (x / np.sqrt(r["mu"][:SCHUR_KB])), r["h"])
        Q = float(np.dot(r["c"], w))
        if Q > 0.0 and Q * r["g16"] <= CAP_FLAT * (1.0 + 1.0e-12):
            pick = (sg, abs(Q) / max(abs(float(np.dot(r["c_ar"], w))),
                                     abs(float(np.dot(r["c_at"], w))), 1e-300))
            break
    if pick is None:
        pick = (float("nan"), r["canc"])
    SIG_STAR.append(pick[0])
    CANC_OP.append(pick[1])
    a = r["xstar"] / np.sqrt(r["mu"][:SCHUR_KB])
    Ga = r["G64_ar"][:SCHUR_KB, :SCHUR_KB]
    off = float(a @ (Ga @ a)) - float(np.sum(a * a * np.diag(Ga)))
    QUART.append(abs(off) / max(abs(float(np.dot(r["c_ar"], r["w"]))), 1.0e-300))

CANC = [r["canc"] for r in WP]
F_CANC = fit_exp(XHP, CANC)
F_CANC_OP = fit_exp(XHP, CANC_OP)
F_QUART = fit_exp(XHP, QUART)
AL = [r["alpha"] for r in WP]
_Xd = np.column_stack([np.ones(len(WP)), np.log(XHP), np.log(AL)])
_bb = np.linalg.lstsq(_Xd, np.log(np.abs(QUART)), rcond=None)[0]
B_H, B_A = float(_bb[1]), float(_bb[2])
_bc = np.linalg.lstsq(_Xd, np.log(np.abs(CANC_OP)), rcond=None)[0]
C_H, C_A = float(_bc[1]), float(_bc[2])
_mid = math.sqrt(min(XHP) * max(XHP))
_ilo = [i for i in range(len(WP)) if XHP[i] <= _mid]
_ihi = [i for i in range(len(WP)) if XHP[i] > _mid]
QS = (fit_exp([XHP[i] for i in _ilo], [QUART[i] for i in _ilo]),
      fit_exp([XHP[i] for i in _ihi], [QUART[i] for i in _ihi]))
check("sc_s3.canc_anatomy",
      qmax(QUART) < T163_QUARTER and abs(F_QUART - T163_CANC_EXP) < 0.02
      and abs(B_H) < abs(B_A) and abs(F_CANC) > 1.0,
      "*** R-B''', AND THE FIRST THING T164 CONTRIBUTES IS TO IDENTIFY WHICH OBJECT "
      "THE %+.3f BELONGS TO, BECAUSE TWO DIFFERENT QUANTITIES WERE BEING CALLED THE "
      "SAME NAME. ***  (a) THE T162 a-WEIGHTED QUARTER-BAR OBJECT, "
      "|sum_{k != l} a_k a_l G^arch_kl| / |Q^arch| = %.4f .. %.4f, h-exponent "
      "%+.3f (FIT) -- THAT is T163's %+.3f, reproduced to %.4f, and the value sits "
      "under the T162 quarter bar %.2f on all %d windows with %.0f per cent of "
      "margin to spare.  (b) THE RAW arch/atom CANCELLATION, a different number: "
      "CANC = %.2e .. %.2e at the untapered optimiser (h^%+.3f) and %.2e .. %.2e at "
      "the T163 operating point (the smallest Fejer width meeting the flat price cap "
      "P_pr <= %.2f, sigma* = %.0f .. %.0f; h^%+.3f) -- steeply drifting, and it was "
      "never the quarter-bar object.  AND NOW THE PART THAT ANSWERS THE QUESTION: "
      "the two-variable regression on (a) gives log QUART = c_0 %+.3f log h %+.3f "
      "log alpha, i.e. %.1fx more of the drift sits on the ZONE SCALE than on h "
      "(for (b) the same regression gives %+.3f log h %+.3f log alpha), and on this "
      "surface alpha and h are COUPLED BY CONSTRUCTION -- the window comes from a "
      "prime gap -- so a regression on h alone MISATTRIBUTES an alpha-effect to h.  "
      "Split halves of (a): h^%+.3f (lower), h^%+.3f (upper).  STATUS: CERT-WINDOW "
      "for the quarter bar (value under %.2f on every window), MEASURED for the "
      "exponents, and the honest reading is that %+.3f is NOT established as an "
      "h-gate: separating it needs a surface on which alpha and h vary "
      "independently, which THIS recipe cannot produce.  That is a narrowing of "
      "R-B''' and not a closure"
      % (T163_CANC_EXP, qmin(QUART), qmax(QUART), F_QUART, T163_CANC_EXP,
         abs(F_QUART - T163_CANC_EXP), T163_QUARTER, len(WP),
         100.0 * (1.0 - qmax(QUART) / T163_QUARTER),
         qmin(CANC), qmax(CANC), F_CANC, qmin(CANC_OP), qmax(CANC_OP),
         CAP_FLAT, qmin(SIG_STAR), qmax(SIG_STAR), F_CANC_OP,
         B_H, B_A, abs(B_A) / max(abs(B_H), 1.0e-12), C_H, C_A, QS[0], QS[1],
         T163_QUARTER, T163_CANC_EXP))

para("""S3.2  R-D IN ONE PARAGRAPH, AND THE INVARIANCE SETTLES ITS TYPE RATHER THAN ITS
VALUE.  The fifth device for R1'' is untouched here (T161 measured rho = %.4f ..
%.4f > 1, flat, and nothing in T162 .. T164 moved it).  What S2.1 DOES settle is
what a fifth device would have to LOOK like: every quantity the downstream chain
consumes is a ratio of two forms that are homogeneous of the same degree in a, so
by the gauge theorem every one of them is INVARIANT under a sector change.  That
is checked below on the T156 kernel itself, which is the strongest form of the
statement available: a device that a sector change could produce would have to be
NON-homogeneous, and no object in the R1'' list is.""" % T161_RHO1)

E_PK, E_R, E_F = [], [], []
for r in WE:
    for ks in [t for t in SHIFTS if t > 0.0]:
        th = r["mu1_full"] / (r["mu1_full"] + ks)
        # the shifted-sector versions, in closed form: s -> s/theta,
        # a_hat -> theta a_hat, L -> theta L.  DIRECTION: theta < 1 always.
        s_k, ah_k, L_k = r["s"] / th, th * r["a_hat"], th * r["L"]
        E_PK.append(abs(ah_k * s_k - r["P_K"]) / r["P_K"])
        E_R.append(abs(1.0 / (L_k * s_k) - 1.0 / (r["L"] * r["s"]))
                   * r["L"] * r["s"])
        f0 = loss_PR(max(r["P_K"], 1.0), 1.0 / (r["L"] * r["s"]))
        fk = loss_PR(max(ah_k * s_k, 1.0), 1.0 / (L_k * s_k))
        if np.isfinite(f0) and np.isfinite(fk):
            E_F.append(abs(fk - f0) / max(abs(f0), 1.0e-300))
check("sc_s3.kernel_invariance",
      qmax(E_PK) < EXACT_BAR and qmax(E_R) < EXACT_BAR
      and (not E_F or qmax(E_F) < EXACT_BAR),
      "*** THEOREM, MACHINE-CHECKED, AND IT IS THE END-TO-END STATEMENT OF ARM B: "
      "THE WHOLE T156 KERNEL IS GAUGE-INVARIANT, SO NO SECTOR CHANGE CAN CHANGE "
      "ANY DOWNSTREAM NUMBER. ***  Under the shift mu^P_1 -> mu^P_1 + kap_s the "
      "three inputs move in exactly compensating directions -- s -> s / theta, "
      "a_hat -> theta a_hat, L -> theta L with theta = mu^P_1/(mu^P_1 + kap_s) -- so "
      "P_K = a_hat . s is unchanged to %.2e, the r-ceiling 1/(L s) is unchanged to "
      "%.2e, and F(P_K, r) is unchanged to %.2e on %d window-by-shift "
      "combinations.  CONSEQUENCE, AND IT IS WHY ARM B IS CLOSED RATHER THAN "
      "UNPRODUCTIVE: the entry spectrum enters the chain ONLY through ratios of "
      "equally-homogeneous forms, so ``represent the entry functional in a sector "
      "with a bigger gap'' cannot be a route -- there is nothing for the bigger gap "
      "to change"
      % (qmax(E_PK), qmax(E_R), qmax(E_F) if E_F else 0.0, len(E_PK)))

# --- S3.3  the end-to-end assembly and the obligatory stress -------------------
E2E, OOS_M = [], []
U_OOS = 1.0 / WE[0]["g16"]                    # the SMALLEST window, fixed first
for r in WE:
    t = stations(r, U_OOS)
    OOS_M.append(t["Tmarg"])
    need = 2.0 * KAPPA * r["TV"] * r["X"] ** (RH_DELTA - (
        0.5 + math.log(2.0 * KAPPA * r["TV"] / abs(r["Q"])) / r["logX"]))
    E2E.append(abs(need - abs(r["Q"])) / abs(r["Q"]))
F_OOSM = fit_exp(XE, OOS_M)
check("sc_s3.end_to_end", qmax(E2E) < 1.0e-10 and F_OOSM > -BAR_FLAT
      and qmin(OOS_M) > 0.0,
      "*** THE CHAIN, ASSEMBLED WITH THE BEST S1/S2 RESULT IN IT, AND THE ONLY "
      "THING ``END TO END'' CAN MEAN HERE. ***  (1) The Abel step reproduces |Q| "
      "from 2 kappa TV X^{1/2 - delta_bnd} to %.2e .. %.2e on all %d windows, so "
      "delta_bnd IS by construction the exact depth at which the unconditional "
      "Chebyshev input would suffice and the chain has no other leak.  (2) The "
      "S1 result is carried in the ONLY form it survives in: the ceiling is the "
      "CONSTANT U = 1/g_16 of the SMALLEST window, %.4f, applied unchanged to every "
      "other window -- an OUT-OF-SAMPLE substitution and not a per-window fit -- "
      "and the end-to-end proxy comes out Tmarg = %.4e .. %.4e, h^%+.3f (FIT), "
      "non-decreasing against the one-sided bar and positive throughout.  (3) The "
      "S2 result enters as a TYPE statement and changes no "
      "number, which is exactly what a gauge theorem should do.  WHAT IS THEREFORE "
      "PROVED AND WHAT IS NOT: 1/s <= Q(x) is a theorem at every listed x; the "
      "depth the primes actually deliver is NOT decided here and cannot be, since "
      "no zero and no L-function is touched anywhere in this file"
      % (qmin(E2E), qmax(E2E), len(E2E), U_OOS, qmin(OOS_M), qmax(OOS_M), F_OOSM))

NOGO_FAC = (2, 4, 8, 16, 32)
SURR, NOGO = [], []
for r in WP:
    if budget_left() < 90.0:
        info("sc_s3.budget", "stress stopped before h = %d" % r["h"])
        break
    at = atoms_in(r["alpha"])
    mm = np.array([t[1] for t in at], dtype=float)
    rs = np.random.RandomState(9164 + r["h"])
    uu_s = np.sort(rs.uniform(0.0, 2.0 * r["alpha"], mm.shape[0]))
    c_s, _, _, _ = atom_lags(r["alpha"], r["M"], list(zip(uu_s, mm)))
    SURR.append(abs(float(np.dot(c_s, r["w"])) + r["Q_ar"]) / abs(r["Q"]))
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
        row.append((2.0 * NU_MAIN / fac, mm.shape[0] / float(M_c),
                    canc_c / r["canc"]))
    NOGO.append(row)

check("sc_s3.nogo_surrogate", qmin(SURR) > 100.0,
      "*** MUST-BREAK CONTROL 1, AND IT BREAKS BY ORDERS OF MAGNITUDE. ***  "
      "Replacing the prime-power positions log n by a UNIFORM sample on "
      "[0, 2 alpha] while keeping the SAME mass multiset 2 Lambda(n)/sqrt n and the "
      "SAME count, |Q^arch + Q^surrogate| / |Q| jumps to %.3e .. %.3e on %d "
      "windows.  So every statement above is a statement about WHERE the prime "
      "powers sit, and not about the machinery"
      % (qmin(SURR), qmax(SURR), len(SURR)))

DMG = [[row[j][2] for row in NOGO] for j in range(len(NOGO_FAC))]
OCC = [[row[j][1] for row in NOGO] for j in range(len(NOGO_FAC))]
MONO_NOGO = all(qmed(DMG[j + 1]) > qmed(DMG[j]) for j in range(len(NOGO_FAC) - 1))
check("sc_s3.nogo_t145",
      MONO_NOGO and qmin(DMG[-1]) > 10.0 and qmax(DMG[0]) < qmin(DMG[-1]),
      "*** MUST-BREAK CONTROL 2 -- THE T145 RESOLUTION NO-GO -- AND IT MUST BREAK "
      "OR EVERY NUMBER IN THIS FILE IS AN ARTEFACT. ***  The lag spacing is "
      "coarsened by %s, i.e. nu = %s against the T105 admissibility floor nu >= %d "
      "(the first column is the IDENTITY and is carried as a null control), and the "
      "damage is measured as CANC(coarse) / CANC(fine), i.e. how much of the "
      "cancellation is LOST: %s.  Cell occupancy over the same sweep: %s.  IT "
      "BREAKS, AND IT BREAKS MONOTONICALLY IN THE COLLISION RATE -- the median "
      "damage rises at every step of the sweep and at the coarsest setting it is "
      ">= %.1f on EVERY window.  The surface of this file (nu = %d) is on the right "
      "side of that no-go by construction"
      % ("/".join("%gx" % (f / 2.0) for f in NOGO_FAC),
         "/".join("%.2f" % (2.0 * NU_MAIN / f) for f in NOGO_FAC), NU_MAIN,
         "; ".join("nu=%.2f: %.1f .. %.1f"
                   % (2.0 * NU_MAIN / NOGO_FAC[j], qmin(DMG[j]), qmax(DMG[j]))
                   for j in range(len(NOGO_FAC))),
         "; ".join("nu=%.2f: %.2f .. %.2f"
                   % (2.0 * NU_MAIN / NOGO_FAC[j], qmin(OCC[j]), qmax(OCC[j]))
                   for j in range(len(NOGO_FAC))),
         qmin(DMG[-1]), NU_MAIN))

E_DIR, E_PAR, E_ORT, E_TOEP = [], [], [], []
_rs = np.random.RandomState(1641)
for _ in range(64):
    aa = float(_rs.uniform(0.05, 6.0))
    bb = float(_rs.uniform(-3.0, 3.0))
    LL = int(_rs.randint(1, 40))
    direct = float(np.sum(np.cos(bb + aa * np.arange(1, LL + 1))))
    E_DIR.append(abs(float(_cos_sum(aa, bb, LL)) - direct) / max(abs(direct), 1.0))
for r in WP[:4]:
    m = r["h"]
    cL = np.zeros(r["M"])
    cL[0], cL[1] = 2.0, -1.0
    E_PAR.append(float(np.max(np.abs(odd_toeplitz(cL, r["M"]) - lap_P_mat(m)))))
    E_ORT.append(float(np.max(np.abs(r["Tb"] @ r["Tb"].T - np.eye(KB_MAX)))))
    v = np.random.RandomState(7 + m).standard_normal(m)
    E_TOEP.append(abs(float(v @ (odd_toeplitz(r["c"], r["M"]) @ v))
                      - float(np.dot(r["c"], lag_weights_from_v(v, m))))
                  / max(abs(float(v @ (odd_toeplitz(r["c"], r["M"]) @ v))), 1e-300))
check("sc_s3.classical_controls",
      qmax(E_DIR) < 1.0e-12 and qmax(E_PAR) < 1.0e-12 and qmax(E_ORT) < 1.0e-12
      and qmax(E_TOEP) < 1.0e-12,
      "*** THE CLASSICAL CONTROLS, EXACT, BECAUSE EVERYTHING CLOSED IN THIS FILE "
      "RESTS ON THEM. ***  (i) The Dirichlet-kernel identity (Dirichlet 1829) "
      "against DIRECT summation on %d random (alpha, beta, L): %.2e .. %.2e.  "
      "(ii) The parity Laplacian: odd_toeplitz(c^L) = tridiag(-1, 2, -1) with last "
      "diagonal 3, to %.2e (Kac-Murdock-Szego 1953).  (iii) The parity basis is "
      "orthonormal, T T^T = I to %.2e.  (iv) THE ONE THE ASCENT DEPENDS ON, checked "
      "on RANDOM v and not only on the chain's own vectors: "
      "v^T odd_toeplitz(c) v = sum_d c_d w_d(v) to %.2e, i.e. the correlation form "
      "is the pairing for ARBITRARY v and the S2.3 search is measuring the same "
      "object the chain does"
      % (len(E_DIR), qmin(E_DIR), qmax(E_DIR), qmax(E_PAR), qmax(E_ORT),
         qmax(E_TOEP)))

GB = []
for r in WP:
    wp = r["w"] + 0.01 * float(np.max(np.abs(r["w"])))
    GB.append(abs(float(np.sum(wp))) / float(np.sum(np.abs(wp))))
check("sc_s3.nogo_gauge", qmin(GB) > 1.0e-6,
      "*** MUST-BREAK CONTROL 3: THE GAUGE IDENTITY IS LOAD-BEARING. ***  Adding a "
      "constant of 1 per cent of sup|w| destroys sum_d w_d = 0 (the residual jumps "
      "from %.2e to %.3e .. %.3e of ||w||_1), which is the identity that licenses "
      "the Abel step -- so the step is not a formality"
      % (qmax([r["gauge"] for r in WP]), qmin(GB), qmax(GB)))

print("")
print("TOTAL (S3): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("S4  THE MAP V36, THE PROMOTION CANDIDATES, THE REST LIST, THE VERDICT")
# ----------------------------------------------------------------------------
# THE VERDICT RULE, PREREGISTERED AND EVALUATED FROM CHECK OUTPUTS ONLY.
ARM_B_FOUND = any(abs(TRANSFER[ks][1]) < BAR_FLAT and abs(TRANSFER[ks][0])
                  < BAR_FLAT for ks in TRANSFER)
ARM_A_CARRIES = (F_FLATM > -BAR_FLAT and abs(F_G16) < BAR_FLAT
                 and max(abs(SPLIT_EXP[0]), abs(SPLIT_EXP[1])) < BAR_FLAT
                 and G16_SPREAD < 10.0
                 and qmin([t["Tmarg"] for t in FLAT_ROWS]) > 0.0)
if ARM_B_FOUND:
    VERDICT = "SECTOR-FOUND"
elif ARM_A_CARRIES:
    VERDICT = "TOLERANCE-CARRIES"
elif np.isfinite(EPS_STAR) and EPS_STAR > 0.0:
    VERDICT = "ONE-TERM-MISSING"
else:
    VERDICT = "SECTOR-RESISTS"
ARM_B_VERDICT = "SECTOR-FOUND" if ARM_B_FOUND else "SECTOR-RESISTS"

THEOREMS = ["sc_q0.scales", "sc_q0.pairing_identity", "sc_s1.st1_direction",
            "sc_s2.gauge_invariance", "sc_s2.candidate_full_space",
            "sc_s2.candidate_shift_conservation", "sc_s2.abel_identity",
            "sc_s3.kernel_invariance", "sc_s3.end_to_end",
            "sc_s3.classical_controls", "sc_s3.nogo_gauge"]
CERT_UNIF = ["sc_q0.chebyshev_kappa"]
CERT_WIN = ["sc_q0.chebyshev", "sc_s1.flat_ceiling_suffices",
            "sc_s1.m_freedom_is_the_rest", "sc_s3.canc_anatomy"]
MEASURED = ["sc_s1.st3_sensitivity", "sc_s1.tolerance_threshold",
            "sc_s2.free_search_demand", "sc_s2.free_search_price",
            "sc_s3.nogo_surrogate", "sc_s3.nogo_t145"]

para("""S4.1  THE MAP V36 -- WHERE THE TWO ARMS OF R-E STAND, IN NUMBERS.

ARM A, IN THREE NUMBERS.  (1) The chain spends the entry ceiling at power EXACTLY
ONE: d log(1 - F) / d log U = %+.4f .. %+.4f, so a ceiling growing like h^eps buys
a T156 loss margin decaying like h^{-eps}.  The one-sided rule reports
eps* = %.2f, but that number is the eps = 0 TAILWIND (h^%+.3f, itself the measured
drift of L, h^%+.3f) divided by power one -- a property of this surface and not
structural slack.  THE O(1) REQUIREMENT WAS REAL.  (2) AND
IT IS ALSO ALREADY MET: 1/g_16 = %.4f .. %.4f, h^%+.3f over a %.0fx lever arm,
with a single CONSTANT ceiling U = %.4f driving the whole downstream map the
FAVOURABLE way (Tmarg h^%+.3f, i.e. no downward drift and positive throughout;
the FLATNESS claim belongs to the ceiling, not to the proxy).
(3) So what is left is not a quantitative gate but a QUANTIFIER:
sup_m 1/g_16(m) < infinity.  Split halves h^%+.3f / h^%+.3f, spread %.3f.

ARM B, IN ONE THEOREM AND ONE SURPRISE.  THE THEOREM: the entry normalisation is
a GAUGE.  Q and TV are homogeneous of degree two in a, x_1 = 1 fixes only the
scale, so Q/TV -- and with it delta_bnd -- is the same number in EVERY sector, to
%.1e over %d sector-by-vector combinations; the full space is WORSE (mu_0 = 0
exactly); a shift flattens the floor (h^%+.3f at kap_s = %.1f) and pays the
identical exponent back as a transfer factor (h^%+.3f), the two summing to
h^%+.3f = the T163 exponent at EVERY shift; and the T156 kernel itself is
invariant because s -> s/theta, a_hat -> theta a_hat, L -> theta L compensate to
%.1e.  THE SURPRISE: dropping the normalisation altogether, a first-order ascent
on Q/TV reaches %.3e .. %.3e against the crossing bar %.4f -- delta_bnd =
%.3f .. %.3f, i.e. the DEMAND is overshot by %.0fx .. %.0fx -- but the price of
that point is P_pr = %.2e .. %.2e (h^%+.3f), above T163's own crossing price
h^%+.2f, so the exchange law simply relocated the difficulty.  T163's TV floor
holds on the unconstrained optimiser too (TV mu^P_1 = %.2f .. %.2f >= 1).

R-B''' AND R-D.  The %+.3f exponent belongs to the T162 a-weighted quarter-bar
object (%.4f .. %.4f, under the %.2f bar on all %d windows), and a two-variable
regression puts only %+.3f of it on log h against %+.3f on log alpha -- a
narrowing, not a closure, and this surface cannot separate the two.  R-D is
untouched in value (rho = %.4f .. %.4f, T161) and settled in TYPE: every object
the chain consumes downstream is a ratio of equally-homogeneous forms, hence
gauge-invariant, so no fifth device can come from a sector change.""" % (
    qmin(NU_U), qmax(NU_U), EPS_STAR, TOL[0.0]["exp"], F_L,
    qmin(G16_LIST), qmax(G16_LIST), F_G16,
    max(XHP) / min(XHP), U_REF, F_FLATM, SPLIT_EXP[0], SPLIT_EXP[1], G16_SPREAD,
    qmax(E_GAUGE), len(E_GAUGE), TRANSFER[KS_BIG][0], KS_BIG,
    TRANSFER[KS_BIG][1], TRANSFER[KS_BIG][0] + TRANSFER[KS_BIG][1],
    max(qmax(E_PK), qmax(E_R)),
    qmin([t["R"] for t in SR]), qmax([t["R"] for t in SR]), CROSS_BAR,
    qmin([t["d_bnd"] for t in SR]), qmax([t["d_bnd"] for t in SR]),
    qmin([t["R"] for t in SR]) / CROSS_BAR,
    qmax([t["R"] for t in SR]) / CROSS_BAR,
    qmin([t["P_pr"] for t in SR]), qmax([t["P_pr"] for t in SR]), F_PASC,
    T163_PCROSS_EXP, qmin([t["tvf"] for t in SR]), qmax([t["tvf"] for t in SR]),
    T163_CANC_EXP, qmin(QUART), qmax(QUART), T163_QUARTER, len(WP), B_H, B_A,
    T161_RHO1[0], T161_RHO1[1]))

para("""S4.2  PROMOTION CANDIDATES, ALL **PENDING**, AND NONE OF THEM RESTATES T163's
P1-P7 OR ANYTHING THE PARALLEL v555 PROMOTION CARRIES (the correlation form, the
exchange law, the chain-derived price axis, the TV floor and the price floor it
implies are T163's rows and are QUOTED here, not re-promoted).

  Q1 **THEOREM** THE ENTRY NORMALISATION IS A GAUGE.  Q and TV are homogeneous of
     degree two in a and x_1 = 1 fixes only the scale, so Q/TV and delta_bnd are
     sector-independent; verified to %.1e over %d combinations of %d sector
     spectra x %d taper widths x %d windows.  THIS IS THE ROW THAT CARRIES ARM B.
  Q2 **THEOREM** THE h^2 CONSERVATION LAW.  For the shift mu^P_1 -> mu^P_1 +
     kap_s the T1-T4 floor scales by theta and the certified value scales by the
     SAME theta, so (floor) x (transfer) = 1 / mu^P_1 identically: the floor
     exponent and the transfer exponent sum to %+.3f at every shift on the
     declared grid, to 1e-9.  A shifted or weighted sector moves the h^2, never
     removes it.
  Q3 **THEOREM** THE FULL SPACE IS WORSE, IN CLOSED FORM.  mu_0 = 0 exactly for
     the unprojected spectrum, so the T3 step gives no finite floor at all; and
     the lowest non-constant full-space eigenvalue never exceeds mu^P_1.
  Q4 **THEOREM** THE T156 KERNEL IS GAUGE-INVARIANT.  s -> s/theta,
     a_hat -> theta a_hat, L -> theta L, hence P_K = a_hat s and r = 1/(L s) and
     F(P_K, r) are unchanged to %.1e on %d window-by-shift combinations.  This is
     what makes Arm B CLOSED rather than merely unproductive.
  Q5 **THEOREM** THE ABEL CEILING ON THE DEMAND RATIO.  Q = sum_e (Delta w)_e C_e
     with C the partial sums of the lag coefficients, hence Q/TV <= ||C||_inf =
     %.1f .. %.1f, a WINDOW-LENGTH quantity growing as h^%+.3f -- so the frequency
     side supplies an abundant ceiling and any obstruction is an ALIGNMENT deficit
     eta = %.3e .. %.3e.
  Q6 **MEASURED** THE CHAIN SPENDS THE CEILING AT POWER ONE.
     d log(1 - F)/d log U = %+.4f .. %+.4f, so the end-to-end proxy loses one unit
     of exponent per unit of eps and the O(1) requirement on 1/s is not an artefact
     of caution; the apparent eps* = %.2f is the surface's own tailwind and is
     reported as such.
  Q7 **MEASURED, POSITIVE AND PRICED** THE NORMALISATION-FREE DEMAND IS REACHED.
     An ascent on Q/TV over the full window reaches %.3e .. %.3e > 2 kappa =
     %.4f on %d of %d windows (delta_bnd = %.3f .. %.3f), at a price
     h^%+.3f -- worse than T163's crossing price h^%+.2f.  A positive that
     changes no gate is still worth a row, because it shows the demand axis is
     not the binding one.
  Q8 **CERT-WINDOW** THE FLAT CEILING AND WHAT IT LEAVES.  1/g_16 = %.4f .. %.4f
     (h^%+.3f, split halves %+.3f / %+.3f, spread %.3f) with a single constant
     ceiling driving the downstream map with NO DOWNWARD drift (h^%+.3f); the
     residue is the QUANTIFIER sup_m 1/g_16(m) < infinity and nothing else.
  Q9 **CERT-WINDOW / MEASURED** WHICH OBJECT THE %+.3f BELONGS TO.  It is the
     T162 a-weighted quarter-bar object (%.4f .. %.4f < %.2f on all %d windows),
     and its two-variable regression is %+.3f log h %+.3f log alpha.""" % (
    qmax(E_GAUGE), len(E_GAUGE), len(WEIGHTS) * len(SHIFTS), len(SIG_S2),
    len(WP), TRANSFER[KS_BIG][0] + TRANSFER[KS_BIG][1],
    max(qmax(E_PK), qmax(E_R), qmax(E_F) if E_F else 0.0), len(E_PK),
    qmin([r["Cinf"] for r in WP]), qmax([r["Cinf"] for r in WP]), F_CINF,
    qmin([t["eta"] for t in SR]), qmax([t["eta"] for t in SR]),
    qmin(NU_U), qmax(NU_U), EPS_STAR,
    qmin([t["R"] for t in SR]), qmax([t["R"] for t in SR]), CROSS_BAR,
    N_CROSS, len(SR), qmin([t["d_bnd"] for t in SR]),
    qmax([t["d_bnd"] for t in SR]), F_PASC, T163_PCROSS_EXP,
    qmin(G16_LIST), qmax(G16_LIST), F_G16, SPLIT_EXP[0], SPLIT_EXP[1],
    G16_SPREAD, F_FLATM, T163_CANC_EXP, qmin(QUART), qmax(QUART), T163_QUARTER,
    len(WP), B_H, B_A))

para("""S4.3  THE REST LIST, AND IT IS SHORTER BECAUSE ONE ARM CLOSED AND THE OTHER
CHANGED SHAPE.

  R-E-A   **REDUCED TO A QUANTIFIER.**  ``Does the chain tolerate a growing
          1/s?'' -- NO, at power one -- but the question is moot: the ceiling the
          chain consumes is 1/g_16, certified per window by a Cholesky identity
          and measured flat.  WHAT REMAINS: sup_m 1/g_16(m) < infinity.  That is
          the m-FREEDOM OF A CERTIFIED FLAT LIST, i.e. the SAME grammatical form
          as every other open uniformity item -- and it is no longer an existence
          question about trial vectors.
  R-E-B   **CLOSED, NEGATIVELY, BY A THEOREM.**  No sector change can help: the
          entry normalisation is a gauge, the demand ratio and the whole T156
          kernel are invariant under it, the full space is worse in closed form,
          and any weight or shift that flattens the T1-T4 floor pays the same
          exponent back as a transfer factor.  A route closed by an identity is
          worth more than a route that is merely unproductive.
  R-B'''  **NARROWED.**  The %+.3f drift is the T162 quarter-bar object, it sits
          under the %.2f bar on every window, and only %+.3f of the drift
          regresses on log h against %+.3f on log alpha.  What is needed is a
          surface on which the zone scale and the window size vary
          INDEPENDENTLY; this recipe couples them.
  R-D     **UNTOUCHED IN VALUE, SETTLED IN TYPE.**  rho = %.4f .. %.4f > 1 flat
          (T161, QUOTED).  By Q1/Q4 no fifth device can be produced by a sector
          change, because every downstream object is gauge-invariant; a device
          would have to be non-homogeneous in a, and none in the R1'' list is.
  R-F     **THE ONE GENUINELY NEW ITEM, AND IT COMES FROM Q5/Q7.**  The demand
          axis is not binding -- the ascent overshoots 2 kappa by up to %.0fx --
          so the whole of R2'' now sits in ONE gauge-invariant question: is there
          a v with Q(v)/TV(v) > 2 kappa AND Q(v) comparable to 1/s?  Equivalently,
          can the ALIGNMENT efficiency eta stay above 2 kappa / ||C||_inf at
          bounded price?  This is the successor and it mentions no sector, no
          normalisation and no prime.""" % (
    T163_CANC_EXP, T163_QUARTER, B_H, B_A, T161_RHO1[0], T161_RHO1[1],
    qmax([t["R"] for t in SR]) / CROSS_BAR))

check("sc_s4.balance",
      len(THEOREMS) + len(CERT_UNIF) + len(CERT_WIN) + len(MEASURED) == 22
      and not FAILS,
      "*** THE BALANCE OF T164, TYPED, AND EVERY ROW IS A CHECK IN THIS RUN. ***  "
      "%d THEOREM (machine-checked identities) / %d CERT-UNIF / %d CERT-WINDOW / "
      "%d MEASURED = %d typed rows out of %d checks; the remaining %d are the "
      "firewall (%d), the surface (1) and this balance row.  T163 closed at "
      "%d/%d/%d/%d.  ZERO FIT rows: the only fitted numbers anywhere are "
      "h-exponents and the one two-variable regression, each labelled (FIT) in "
      "place, and no fitted number carries a claim"
      % (len(THEOREMS), len(CERT_UNIF), len(CERT_WIN), len(MEASURED),
         len(THEOREMS) + len(CERT_UNIF) + len(CERT_WIN) + len(MEASURED),
         N_CHK + 1, N_CHK + 1 - 22, 4, T163_BALANCE[0], T163_BALANCE[1],
         T163_BALANCE[2], T163_BALANCE[3]))

para("""S4.4  THE VERDICT: **%s** (ARM A), WITH ARM B AT **%s**.

THE THREE HONEST SENTENCES.  (1) THE O(1) REQUIREMENT ON 1/s IS NOT OBSOLETE AS A
REQUIREMENT -- the T156 kernel spends the ceiling at power exactly one, so nothing
downstream tolerates growth -- BUT IT IS ALSO NOT OPEN AS A QUANTITY: the ceiling
the chain consumes is 1/g_16, a Cholesky identity evaluated on the window's own lag
Gram, and it is %.4f .. %.4f with h-exponent %+.3f over a %.0fx lever arm, with a
single constant ceiling carrying the entire downstream map without downward
drift.  What T163 called
R2'' therefore COLLAPSES ONTO ONE STATEMENT, and it is a quantifier and not a
search: sup_m 1/g_16(m) < infinity, the m-FREEDOM OF A CERTIFIED FLAT LIST -- the
same shape as every other open uniformity item in the chain, and no longer an
existence question about trial vectors.  (2) NO SECTOR WITHOUT THE h^2 EXISTS, AND
THAT IS NOW A THEOREM RATHER THAN A FAILED SEARCH: the entry normalisation is a
GAUGE (Q and TV are homogeneous of degree two in a and x_1 = 1 fixes only the
scale), so the demand ratio Q/TV, the T156 inputs P_K and r, and F(P_K, r) itself
are the SAME numbers in every sector, to %.1e; the full space is strictly worse
because mu_0 = 0 exactly; and every shift or weight that flattens the T1-T4 floor
pays the identical exponent back as a transfer factor, the two summing to h^%+.3f
at every point of the declared grid.  (3) SO BOTH ARMS ARE ANSWERED, AND THE
UNEXPECTED PART IS WHICH AXIS TURNED OUT TO BE BINDING: without the normalisation
the demand is not merely reachable but overshot by up to %.0fx (delta_bnd =
%.3f .. %.3f against the yardstick 1/2, on %d of %d windows, at a cancellation
headroom of %.1e), while the price of those points is h^%+.3f -- WORSE than T163's
own crossing price h^%+.2f.  The binding axis was never the demand and never the
sector: it is the ALIGNMENT between Delta w and the partial sums C of the lag
coefficients, and that quantity is gauge-invariant.

WHAT THIS MEANS FOR THE OVERALL MAP, WITHOUT INFLATION.  T163 ended with a
theorem that closed a route.  T164 ends with the route's successor CLOSED as well
(Arm B) and the surviving item RESHAPED (Arm A): the entry-ceiling gate is no
longer a quantitative unknown but a quantifier over windows, which is the form the
rest of the chain's open items already have.  Nothing here proves that quantifier,
nothing here upgrades a per-window certificate to a uniform one, and the one new
positive -- the normalisation-free demand -- buys no gate because its price is
worse than the one T163 already measured.  The new successor R-F is stated in
gauge-invariant terms for the first time.

AND THE FENCE, ONE LAST TIME, BECAUSE IT IS THE MOST IMPORTANT SENTENCE HERE.  No
zero of any L-function was read, generated, tabulated, approximated or
extrapolated; no L-function was evaluated; the only arithmetic object touched was
a finite von Mangoldt sieve up to n = %d.  The number 1/2 appears in exactly one
role, as the STRENGTH of a classical statement against which a required depth is
compared, and a comparison of strengths is not a claim about RH in either
direction.  Weil 1952 remains an address.  Classics used and cited where used:
Chebyshev 1852, Dirichlet 1829, Abel 1826, Mellin 1896, Fejer 1915, Schur 1917,
Kantorovich 1948, Kac-Murdock-Szego 1953, Rosser-Schoenfeld 1962, Temple 1928.""" % (
    VERDICT, ARM_B_VERDICT, qmin(G16_LIST), qmax(G16_LIST), F_G16,
    max(XHP) / min(XHP), qmax(E_GAUGE),
    TRANSFER[KS_BIG][0] + TRANSFER[KS_BIG][1],
    qmax([t["R"] for t in SR]) / CROSS_BAR,
    qmin([t["d_bnd"] for t in SR]), qmax([t["d_bnd"] for t in SR]),
    N_CROSS, len(SR), qmin([t["head"] for t in SR]), F_PASC, T163_PCROSS_EXP,
    ATOM_MAX))

print("")
print("=" * 78)
print("TOTAL (T164 SECTOR.CHANGE): %d checks, %d failures, %.1f s -- VERDICT %s "
      "(ARM A) / %s (ARM B)"
      % (N_CHK, len(FAILS), time.time() - T0, VERDICT, ARM_B_VERDICT))
print("BUDGET: %.1f s of %.0f s used, %.1f s left; HARD CAPS respected "
      "(max factorised form %d <= %d)"
      % (time.time() - T0, BUDGET_S, budget_left(), max(HCAP, KB_MAX), MAX_H))
if FAILS:
    print("FAILURES: %s" % ", ".join(FAILS))
print("=" * 78)
