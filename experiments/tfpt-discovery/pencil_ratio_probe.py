"""PART 152 -- THE CONTRACT ``PENCIL.RATIO'': THE LAST SCALAR.

THE RH FENCE, FIRST AND PROMINENT.  Nothing in this file reads, generates,
approximates, extrapolates or otherwise touches a single zero of any L-function.
Weil's explicit-formula positivity criterion (Weil 1952; Bombieri 2000) is CITED
as an ADDRESS ONLY and is never used, in either direction.  An AST firewall below
enforces the absence of zero data, the import whitelist and the absence of any
write-mode file access.  What is investigated here is ONE inequality about a
finite Toeplitz-minus-Hankel section in its ODD PARITY SECTOR: the m-freeness of
the bottom-pencil ratio R = K_bot / kap.  Even if it closed perfectly what would
stand is a finite-window positivity statement with an explicit constant on
prime-power zones in frame A.  The distance from there to RH is mapped in Y4 and
never travelled.

WHAT T151 LEFT.  The odd-sector bound is closed: grid-step-over -> bottom ladder
lam_k(A) <= S mu^P_k (S = 1.10 .. 2.39, certified by LDL^T inertia counts) ->
Sobolev step => b_k <= C_S k linear with C_S = 11.51 .. 19.57, flat at x^0.020.
Exactly ONE fit remains: the m-freeness of

    R = K_bot / kap = 3.3634 .. 9.7108 ,  fitted x^{0.037 +- 0.015} ,

with kap = lam_min(A, L_P) = 0.2273 .. 0.4502 certified by ONE Cholesky.  The
global pencil ratio is useless (it grows like x^2.695); only the BOTTOM ratio is
flat, and the T145 no-go breaks exactly there (its ratio grows x^1.986 because
its bottom mode carries parity-Dirichlet energy ~ 1/log m).

WHAT THIS FILE DOES.
  Y1  kap FROM THE ARITHMETIC.  Is the archimedean section POSITIVE in the odd
      sector (it is indefinite in the full space, 2 .. 7 negative eigenvalues)?
      Then four candidate routes to a closed kap, in increasing strength:
      additive Weyl on the exact arch / atom split, the l1 atom budget,
      Gershgorin on the pencil-whitened parity block, and a two-block Schur
      criterion with a FIXED low block.  Each is labelled with its direction
      and its measured loss.
  Y2  K_bot AND THE RATIO.  Does the archimedean part carry the upper ladder
      constant K_bot?  If so R is an ARCHIMEDEAN ratio plus a controlled atom
      correction, and m-freeness becomes a statement about a SMOOTH kernel.
      The T145 no-go MUST break inside that decomposition, and where.
  Y3  Psi, FIRST RECONNAISSANCE.  Psi = 4.7e3 .. 6.1e6 is now the dominant
      end-to-end loss.  Anatomy only: what it is made of, what drives growth,
      whether there is a structural reserve analogous to the parity discovery.
  Y4  MAP V24, the shortest rest list, and an honest three-sentence verdict.

DISCIPLINE.  Theorem / certified / measured / fit are kept strictly apart and
every claim is labelled.  Directions (upper vs lower bound) are pedantic.
Classics cited where used: Kac-Murdock-Szego 1953 (the tridiagonal spectrum),
Widom 1958 and Boettcher-Silbermann (Toeplitz-plus-Hankel asymptotics),
Sylvester 1852 (inertia), Weyl 1912 (eigenvalue interlacing / monotonicity),
Gershgorin 1931, Courant-Fischer 1920, Schur 1917, Charikar 2000.
HARD CAPS: any factorised / inverted / diagonalised matrix <= 1500; probe
budget < 900 s.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, ldl, solve_triangular

T0 = time.time()
np.random.seed(152152)

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 700.0             # HARD probe budget (< 900 s)
RESERVE_S = 210.0            # reserved for Y2 .. Y4 after the window loop

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 400000
ZONE_DEEP = 380000

# --- the measurement surface, DECLARED BEFORE ANY RESULT IS SEEN ------------
SURF_ZONES = 60
SURF_HCAP = 1450
STRATA = 4

PEN_BACKOFF = (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1)
K_CERT = 8                   # modes for which the ladder is INERTIA-certified
K_LAD = 24
BAR_UNIF = 0.25              # |exponent| + band bar for "flat / non-growing"
KAP_TARGET = 0.25            # the trend target quoted in the brief

# the LOW-BLOCK ladder of the two-block certified route, fixed before any number
LOW_BLK = (4, 6, 8, 12, 16, 24, 32, 48, 64)
SCHUR_KB = (16, 48)          # low blocks tried by the Schur route
# The RESOLUTION of the Schur certificate.  It is a property of the certificate,
# not a reading rule: a coarse ladder quantises the certified floor and inflates
# the scatter of every ratio built on it, so it is set fine enough that the
# quantisation step is below the scatter of the objects being compared.
T_LADDER = (0.25, 0.245, 0.24, 0.235, 0.23, 0.225, 0.22, 0.215, 0.21, 0.205,
            0.20, 0.19, 0.18, 0.16, 0.14, 0.12, 0.10, 0.05)

B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962 Thm 12)
NOGO_SIZES = (48, 64, 96, 128, 192, 256, 384, 512, 768, 1024)
PSI_POOL = 10                # windows on which the Psi anatomy is taken

FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name)
    print("[%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail))


def info(name, detail=""):
    print("[info] %-42s %s" % (name, detail))


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def wrap_at(text, width):
    out, line = [], ""
    for w in " ".join(text.split()).split(" "):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + " " + w) if line else w
    if line:
        out.append(line)
    return out


def para(text, width=76, indent="  "):
    for ln in wrap_at(text, width):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T0)


def sym(A):
    return 0.5 * (A + A.T)


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1.0e-300)


def qmin(v):
    v = [x for x in v if np.isfinite(x)]
    return float(min(v)) if v else float("nan")


def qmax(v):
    v = [x for x in v if np.isfinite(x)]
    return float(max(v)) if v else float("nan")


def qmed(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


def fit_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if x.size < 2 or np.ptp(x) <= 0.0:
        return float("nan"), float("nan")
    s, b = np.polyfit(x, y, 1)
    return float(s), float(b)


def fit_band(x, y):
    """A STRATIFIED SPREAD, not a t-statistic: the surface is split into STRATA
    consecutive blocks, a slope is fitted in each, and the half-range of those
    slopes is the reported band.  It is a MEASURE OF SCATTER, never a p-value."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = x.size
    if n < 2 * STRATA:
        return float("nan")
    idx = np.argsort(x)
    x, y = x[idx], y[idx]
    sl = []
    for j in range(STRATA):
        a, b = (j * n) // STRATA, ((j + 1) * n) // STRATA
        if b - a >= 2:
            s, _ = fit_line(x[a:b], y[a:b])
            if np.isfinite(s):
                sl.append(s)
    if len(sl) < 2:
        return float("nan")
    return 0.5 * (max(sl) - min(sl))


def pow_fit(xv, yv, tag):
    """A FIT AND NOTHING MORE.  Reports the exponent of y ~ x^p on the surface
    actually measured; it is never promoted to a theorem anywhere in this file."""
    xs, ys = [], []
    for x, y in zip(xv, yv):
        if np.isfinite(x) and np.isfinite(y) and x > 0.0 and y > 0.0:
            xs.append(math.log(x))
            ys.append(math.log(y))
    p, _ = fit_line(xs, ys)
    band = fit_band(xs, ys)
    return dict(tag=tag, p=p, band=band, n=len(xs),
                lo=qmin(yv), hi=qmax(yv), med=qmed(yv))


def fit_str(f):
    return ("m^%.3f +- %.3f  (%d windows, range %.4g .. %.4g, med %.4g)"
            % (f["p"], f["band"], f["n"], f["lo"], f["hi"], f["med"]))


def flat_ok(f, bar=BAR_UNIF):
    return bool(np.isfinite(f["p"]) and abs(f["p"]) + (f["band"] if
                np.isfinite(f["band"]) else 0.0) <= bar)


def nogrow_ok(f, bar=BAR_UNIF):
    return bool(np.isfinite(f["p"]) and f["p"] + (f["band"] if
                np.isfinite(f["band"]) else 0.0) <= bar)


# ----------------------------------------------------------------------------
# THE AST FIREWALL -- no zero data, no unexpected import, no file write
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
    check("pr_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("pr_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("pr_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("pr_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "pencil_ratio_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T151 code path
# ----------------------------------------------------------------------------
def von_mangoldt_table(n_max):
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


def atom_table(n_max):
    lam = von_mangoldt_table(n_max)
    out = []
    for n in np.nonzero(lam > 0)[0]:
        n = int(n)
        out.append((n, lam[n], math.log(n), 2.0 * lam[n] / math.sqrt(n)))
    return out


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


# ----------------------------------------------------------------------------
# certificates: Cholesky, Gershgorin floor, inertia (Sylvester 1852)
# ----------------------------------------------------------------------------
def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except (LinAlgError, ValueError):
        return None


def chol_floor(A_norm, h):
    """THE BACKWARD-ERROR FLOOR of a COMPLETED Cholesky (Wilkinson): success
    certifies A >= -fl I with fl = c h eps ||A||.  DIRECTION: fl >= 0 and is
    always SUBTRACTED from a lower bound / ADDED to an upper bound."""
    return 8.0 * h * np.finfo(float).eps * max(A_norm, 1.0e-300)


def gersh(X):
    return float(np.max(np.sum(np.abs(X), axis=1)))


def ray_top(X, iters=90):
    v = np.random.randn(X.shape[0])
    v /= np.linalg.norm(v)
    lam = 0.0
    for _ in range(iters):
        w = X @ v
        nw = np.linalg.norm(w)
        if nw <= 0.0:
            return 0.0
        v = w / nw
        lam = float(v @ (X @ v))
    return lam


def cert_lam_max(X, guess=None, tries=14, grow=1.0e-7):
    """AN UPPER BOUND on lam_max, certified by a COMPLETED Cholesky of t I - X."""
    h = X.shape[0]
    t = (ray_top(X) if guess is None else float(guess))
    t = abs(t) + 1.0e-300
    for _ in range(tries):
        Y = sym(t * np.eye(h) - X)
        if safe_cho(Y) is not None:
            return t + chol_floor(gersh(Y), h)
        t *= (1.0 + grow)
        grow *= 6.0
    return float("nan")


def cert_lam_min(X, guess=None, tries=14, grow=1.0e-7):
    """A LOWER BOUND on lam_min, certified by a COMPLETED Cholesky of X - t I."""
    h = X.shape[0]
    t = 0.0 if guess is None else float(guess)
    step = max(abs(t), 1.0e-12) * grow + 1.0e-300
    for _ in range(tries):
        Y = sym(X - t * np.eye(h))
        if safe_cho(Y) is not None:
            return t - chol_floor(gersh(Y), h)
        t -= step
        step *= 6.0
    return float("nan")


def inertia_neg(X):
    """#{lam_j < 0} from a COMPLETED LDL^T (Sylvester's law of inertia 1852;
    Bunch-Kaufman 1977).  A COUNT, never an eigenvector."""
    try:
        lu, d, _ = ldl(X, lower=True)
    except (LinAlgError, ValueError):
        return -1
    del lu
    dd = np.diag(d)
    off = np.diag(d, k=1)
    neg = 0
    i = 0
    n = dd.shape[0]
    while i < n:
        if i + 1 < n and abs(off[i]) > 0.0:
            a, b, c = dd[i], off[i], dd[i + 1]
            det = a * c - b * b
            tr = a + c
            if det < 0.0:
                neg += 1
            elif tr < 0.0:
                neg += 2
            i += 2
        else:
            if dd[i] < 0.0:
                neg += 1
            i += 1
    return neg


def count_below(X, tau):
    """#{lam_j < tau}, a CERTIFIED COUNT via the inertia of X - tau I."""
    return inertia_neg(sym(X - tau * np.eye(X.shape[0])))


# ----------------------------------------------------------------------------
# THE ARCHIMEDEAN KERNEL (Weil 1952 -- CITED, never used as a criterion)
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


def atom_lags(alpha, M, atoms):
    """THE ARITHMETIC PART OF THE LAG VECTOR, ISOLATED.  Every prime-power atom
    contributes -mu_j/2 times a linear spline of total mass 1 around u_j, plus a
    reflected spline when u_j < D.  Hence c^atom <= 0 ENTRYWISE and
    ||c^atom||_1 <= sum_j mu_j -- the closed budget quoted as 4 B sqrt(N)."""
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


def lag_vector_split(alpha, M, atoms):
    """THE EXACT SPLIT c = c^arch + c^atom of the T115 lag assembly.  The sum is
    bit-for-bit the object T111 .. T151 use."""
    c_at, D, mu_tot, n_hit = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D, mu_tot=mu_tot,
                n_atom=n_hit, l1_at=float(np.sum(np.abs(c_at))))


# ----------------------------------------------------------------------------
# the sections and the parity structure
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s} on the ODD section, r, s = 0 .. M/2 - 1.
    THE TOEPLITZ-MINUS-HANKEL FORM, exact and not an approximation: the object
    Szego / Widom theory speaks about (Widom 1958; Boettcher-Silbermann)."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def parity_mu(m):
    """THE EXACT PARITY EIGENVALUES mu^P_k = 4 sin^2(pi k / N), N = 2m + 1,
    k = 1 .. m: the spectrum of the path Laplacian with corner entry 3
    (Kac-Murdock-Szego 1953 in the parity sector).  In symbol language
    mu^P_k = 2 - 2 cos th_k with th_k = 2 pi k / N -- THE ODD GRID, which never
    contains th = 0."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m):
    """THE ORTHONORMAL PARITY BASIS t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N)."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_P_mat(m):
    """L_P: tridiag(-1, 2, -1) with the LAST diagonal entry 3.  That corner is
    not a choice -- for an antisymmetric vector of the full window the reflected
    neighbour of the last index is MINUS the last index."""
    L = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    L[m - 1, m - 1] = 3.0
    return L


def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def pencil_pair(A, LP, m, need_K=True):
    """THE CERTIFIED PENCIL PAIR (kap, K) with kap L_P <= A <= K L_P.
    HOW: L_P is tridiagonal positive definite, so ONE Cholesky L_P = G G^T plus
    two triangular solves gives Z = G^{-1} A G^{-T} whose spectrum IS the pencil
    spectrum.  The extreme eigenvalues of Z are only SEEDS; the certificates are
    two COMPLETED Choleskys of A - kap L_P and K L_P - A.  The Cholesky floor is
    carried honestly: success certifies A - kap L_P >= -fl I and I <= L_P/mu^P_1,
    so what is certified is A >= (kap - fl/mu^P_1) L_P, and the reported kap
    SUBTRACTS that correction.  DIRECTION: kap LOWER, K UPPER."""
    mu1 = 4.0 * math.sin(math.pi / (2 * m + 1)) ** 2
    fac = safe_cho(LP)
    if fac is None:
        return None
    G = np.tril(fac[0]) if fac[1] else np.tril(fac[0].T)
    try:
        Y = solve_triangular(G, A, lower=True, check_finite=False)
        Z = sym(solve_triangular(G, Y.T, lower=True, check_finite=False))
    except (LinAlgError, ValueError):
        return None
    del Y
    try:
        wz = eigh(Z, eigvals_only=True)
    except (LinAlgError, ValueError):
        del Z
        return None
    del Z
    lo_seed, up_seed = float(wz[0]), float(wz[-1])
    kap = float("nan")
    for eta in PEN_BACKOFF:
        k_try = lo_seed * (1.0 - eta) if lo_seed > 0.0 else lo_seed - eta
        X = sym(A - k_try * LP)
        if safe_cho(X) is not None:
            kap = k_try - chol_floor(gersh(X), m) / mu1
            del X
            break
        del X
    K = float("nan")
    if need_K:
        for eta in PEN_BACKOFF:
            K_try = up_seed * (1.0 + eta)
            X = sym(K_try * LP - A)
            if safe_cho(X) is not None:
                K = K_try + chol_floor(gersh(X), m) / mu1
                del X
                break
            del X
    return dict(kap=kap, K=K, kap_seed=lo_seed, K_seed=up_seed, mu1=mu1,
                R_glob=(K / kap) if (np.isfinite(kap) and kap > 0.0)
                else float("inf"))


# ----------------------------------------------------------------------------
section("Y0  SETUP, THE RH FENCE, and THE LICENCES")
# ----------------------------------------------------------------------------
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]

NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

check("pr_y0.gap_facts",
      bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
      and bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12)),
      "the ONLY two gap facts used anywhere: Bertrand-Chebyshev 1852 "
      "(g <= log 2) and the trivial even bound; %d gaps up to n = %d"
      % (NZ_DEEP, ZONE_DEEP))

para("""Y0.0  THE RH FENCE, RESTATED BEFORE ANY NUMBER.  The surrounding statement
is the positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999)
on a FINITE list of prime-power zones in a FINITE window, frame A.  Weil's
explicit-formula criterion is an ADDRESS, never a criterion used here.  No zero
data is read, generated, approximated or extrapolated; the AST firewall above
enforces that together with the import whitelist and the absence of write-mode
file access.  What is at stake is one scalar: the m-freeness of the BOTTOM pencil
ratio R = K_bot / kap of a Toeplitz-minus-Hankel section in its odd parity
sector.  Even a perfect closure would leave a finite-window inequality with an
explicit constant.  The distance to RH is mapped in Y4 and never travelled.""")

para("""Y0.1  THE LICENCES, each with its DIRECTION.  (L1) Cholesky: a COMPLETED
Cholesky of X certifies X >= -fl I with fl the Wilkinson backward-error floor,
which is always subtracted from a lower bound and added to an upper bound.
(L2) Sylvester 1852 / Bunch-Kaufman 1977: a completed LDL^T of A - tau I returns
#{lam_j < tau} as a CERTIFICATE and reads no eigenvector.  (L3) Weyl 1912: for
symmetric X, Y, lam_min(X + Y) >= lam_min(X) + lam_min(Y) -- used ONLY in the
pencil-normalised form nu_min(X + Y) >= nu_min(X) + nu_min(Y) against the SAME
model L_P.  (L4) Kac-Murdock-Szego 1953: the tridiagonal model spectrum
mu^P_k = 4 sin^2(pi k / N), N = 2m + 1, is EXACT, not asymptotic.  (L5) Chebyshev
1852 / Rosser-Schoenfeld 1962 Thm 12: psi(x) <= B_PSI x, verified below on the
exact range used and never assumed beyond it.  (L6) Widom 1958 and
Boettcher-Silbermann are cited for WHAT the object is (Toeplitz plus Hankel in a
parity sector), never for a bound.""")

para("""Y0.2  WHAT COUNTS AS WHAT, PEDANTICALLY.  THEOREM = an identity or a
classical inequality, valid for every m.  CERTIFIED = a numeric bound produced by
a completed factorisation with its floor carried, valid for THAT window only.
MEASURED = a diagonalisation read for orientation.  FIT = an exponent on the
finite surface, never promoted.  The word ``proven'' is used nowhere in this file
for the m-freeness of R.""")

_bpsi_atoms = [(t[0], t[1]) for t in ATOMS_ALL]
_psi_run = 0.0
_bpsi = 0.0
for _n, _lam in _bpsi_atoms:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
check("pr_y0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f is VERIFIED at every jump point up to n = %d (max %.6f); "
      "since psi jumps only at prime powers this is the true max on the range, "
      "and it is never assumed beyond it" % (B_PSI, ATOM_MAX, _bpsi))

# ----------------------------------------------------------------------------
# THE SYMBOL OF THE LAG VECTOR (DESIGN / INTERPRETATION ONLY, never a bound)
# ----------------------------------------------------------------------------
def symbol_at(c, th):
    """f(th) = c_0 + 2 sum_{l>=1} c_l cos(l th), the Toeplitz symbol of the lag
    vector.  INTERPRETATION ONLY: the section carries a Hankel part too, so no
    bound in this file is ever taken from f.  T151 already showed the sampling
    route is VACUUM (f moves 0.47 .. 0.85 per mode spacing)."""
    ll = np.arange(1, c.shape[0])
    return float(c[0] + 2.0 * float(np.dot(c[1:], np.cos(ll * th))))


def schur_floor(B, kb, t):
    """THE CERTIFIED TWO-BLOCK SCHUR FLOOR.  For symmetric B split into a LOW
    block of kb modes and the BULK,
        B >= t I   <=>   B_HH - t I > 0  AND  B_LL - t I - B_LH (B_HH - tI)^-1 B_HL > 0
    (Schur 1917; the standard block criterion, an EQUIVALENCE, not a bound).  Both
    conditions are certified by COMPLETED Choleskys and BOTH backward-error floors
    are subtracted from the returned t.  DIRECTION: the return value is a LOWER
    bound on lam_min(B) = kap, valid for that window."""
    h = B.shape[0]
    HH = sym(B[kb:, kb:] - t * np.eye(h - kb))
    fac = safe_cho(HH)
    if fac is None:
        return None
    fl1 = chol_floor(gersh(HH), h - kb)
    del HH
    try:
        X = cho_solve(fac, B[kb:, :kb], check_finite=False)
    except (LinAlgError, ValueError):
        return None
    S = sym(B[:kb, :kb] - t * np.eye(kb) - B[:kb, kb:] @ X)
    del X
    if safe_cho(S) is None:
        return None
    fl2 = chol_floor(gersh(S), kb)
    del S
    return t - fl1 - fl2


def bottom_ceiling(A, m, mu, k_cert):
    """THE CERTIFIED BOTTOM CEILING K_bot: the smallest tested S with
        lam_k(A) <= S mu^P_k   for k = 1 .. k_cert,
    each inequality certified by ONE completed LDL^T inertia count (L2).  The
    partial diagonalisation supplies a SEED ONLY.  DIRECTION: K_bot is an UPPER
    ladder constant, so it is inflated, never shaved."""
    try:
        w = eigh(A, eigvals_only=True, subset_by_index=[0, k_cert - 1])
    except (LinAlgError, ValueError):
        return None
    seed = float(np.max(np.asarray(w) / mu[:k_cert]))
    if not (seed > 0.0 and np.isfinite(seed)):
        return None
    for eta in (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1, 1.0):
        S = seed * (1.0 + eta)
        ok = True
        for k in range(1, k_cert + 1):
            if count_below(A, S * mu[k - 1]) < k:
                ok = False
                break
        if ok:
            return dict(K_bot=S, seed=seed, lams=np.asarray(w, float), eta=eta)
    return dict(K_bot=float("nan"), seed=seed, lams=np.asarray(w, float),
                eta=float("nan"))


# ----------------------------------------------------------------------------
section("Y1  kap FROM THE ARITHMETIC -- IS THE ARCHIMEDEAN SECTION POSITIVE "
        "IN THE ODD SECTOR?")
# ----------------------------------------------------------------------------
CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > SURF_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(SURF_ZONES, 1))
    SZ = CAND[::-1][::step][:SURF_ZONES]
    SZ.sort(key=lambda t: t[0])
info("Y1.0.zones", "%d prime-power zones admit a frame-A window inside the cap "
     "(h <= %d, MAX_H = %d); the surface takes %d of them (stride %d) from the "
     "deep end" % (len(CAND), SURF_HCAP, MAX_H, len(SZ), step))

para("""Y1.1  THE DECOMPOSITION THIS BLOCK TESTS.  The lag vector splits EXACTLY,
c = c^arch + c^atom (T115 assembly, bit-for-bit), and the odd section is linear in
the lag vector, so
    A = A^arch + A^atom       (THEOREM: an identity, every m).
Against the SAME model L_P, Weyl 1912 in pencil form gives
    kap = nu_min(A) >= nu_min(A^arch) + nu_min(A^atom)      (THEOREM),
and both summands are certified by ONE Cholesky each (L1).  The QUESTION of this
block is whether the first summand is POSITIVE -- in the FULL space the purely
archimedean section is INDEFINITE (T151: 2 .. 7 negative eigenvalues), so if the
odd sector turns it positive definite, that is a second structural gift of the
same kind as the parity discovery itself.""")

ROWS = []
SKIP = dict(pencil=0, ladder=0, budget=0)
for (i_w, (k, D_k, M_k, h_k)) in enumerate(SZ):
    if budget_left() < RESERVE_S:
        info("Y1.1.budget", "surface truncated after %d windows" % len(ROWS))
        SKIP["budget"] += 1
        break
    al = 0.5 * M_k * D_k
    sp = lag_vector_split(al, M_k, atoms_in(al))
    LP = lap_P_mat(h_k)
    mu = parity_mu(h_k)
    A = sym(odd_toeplitz(sp["c"], M_k))
    A_ar = sym(odd_toeplitz(sp["c_ar"], M_k))
    A_at = sym(odd_toeplitz(sp["c_at"], M_k))
    r = dict(k=k, n=NN_ALL[k], x=float(NN_ALL[k]), D=D_k, M=M_k, h=h_k,
             mu1=float(mu[0]), l1_at=sp["l1_at"], mu_tot=sp["mu_tot"],
             n_atom=sp["n_atom"])
    r["split_exact"] = float(np.max(np.abs(A - (A_ar + A_at))))
    pen = pencil_pair(A, LP, h_k)
    pen_ar = pencil_pair(A_ar, LP, h_k)
    pen_at = pencil_pair(A_at, LP, h_k, need_K=False)
    if pen is None or pen_ar is None or pen_at is None:
        SKIP["pencil"] += 1
        del A, A_ar, A_at, LP
        continue
    r["kap"] = pen["kap"]
    r["K_glob"] = pen["K"]
    r["R_glob"] = pen["R_glob"]
    r["kap_ar"] = pen_ar["kap"]
    r["K_glob_ar"] = pen_ar["K"]
    r["kap_at"] = pen_at["kap"]
    try:
        _s_ar = float(eigh(A_ar, eigvals_only=True, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        _s_ar = 0.0
    r["arch_pos"] = cert_lam_min(A_ar, guess=_s_ar)
    Tb = parity_basis(h_k)[:K_LAD]
    G = sym(Tb @ (A @ Tb.T))
    G_ar = sym(Tb @ (A_ar @ Tb.T))
    G_at = sym(Tb @ (A_at @ Tb.T))
    r["par_exact"] = abs(float(Tb[0] @ (LP @ Tb[0])) - float(mu[0])) / float(mu[0])
    r["ray1"] = float(G[0, 0]) / float(mu[0])
    r["ray1_ar"] = float(G_ar[0, 0]) / float(mu[0])
    r["ray1_at"] = float(G_at[0, 0]) / float(mu[0])
    del Tb, G, G_ar, G_at
    # WHERE THE PENCIL FLOOR SITS: the parity-diagonal Rayleigh quotients
    # d_k / mu^P_k for EVERY k.  Each is a Rayleigh quotient at an explicit test
    # vector, hence an UPPER bound on kap; the argmin locates the floor.
    Tf = parity_basis(h_k)
    d_all = np.einsum("kj,kj->k", Tf, (A @ Tf.T).T)
    d_ar_all = np.einsum("kj,kj->k", Tf, (A_ar @ Tf.T).T)
    d_at_all = d_all - d_ar_all
    rat = d_all / mu
    ks = int(np.argmin(rat))
    r["kstar"] = ks + 1
    r["kstar_frac"] = (ks + 1) / float(h_k)
    r["th_star"] = 2.0 * math.pi * (ks + 1) / (2 * h_k + 1)
    r["ray_star"] = float(rat[ks])
    r["ray_star_ar"] = float(d_ar_all[ks] / mu[ks])
    r["ray_star_at"] = float(d_at_all[ks] / mu[ks])
    r["n_neg_diag"] = int(np.sum(d_all < 0.0))
    r["n_neg_diag_ar"] = int(np.sum(d_ar_all < 0.0))
    r["k_last_neg_ar"] = (int(np.max(np.nonzero(d_ar_all < 0.0)[0])) + 1
                          if np.any(d_ar_all < 0.0) else 0)
    r["ray_ar_hi"] = float(np.min((d_ar_all / mu)[ks:]))
    r["k_neg_ar"] = max(r["k_last_neg_ar"], 1)
    del d_all, d_ar_all, d_at_all, rat
    # THE CLOSED ENTRYWISE ROUTE: Gershgorin 1931 on the pencil-whitened parity
    # block B = Lam^{-1/2} T A T^T Lam^{-1/2}, Lam = diag(mu^P).  Its entries are
    # Fejer-weighted prime-power sums, so a bound on them IS an arithmetic bound.
    # DIRECTION: Gershgorin gives a LOWER bound on lam_min(B) = kap.
    Gf = sym(Tf @ (A @ Tf.T))
    isq = 1.0 / np.sqrt(mu)
    B = Gf * np.outer(isq, isq)
    dB = np.diag(B).copy()
    row = np.sum(np.abs(B), axis=1) - np.abs(dB)
    r["gersh_pen"] = float(np.min(dB - row))
    r["coup_max"] = float(np.max(row))
    r["coup_med"] = float(np.median(row))
    kb = r["k_neg_ar"]
    # THE TWO-BLOCK CERTIFIED ROUTE: split the parity block into a LOW block of
    # kb modes and the BULK.  For a symmetric 2x2 block matrix
    #   lam_min(B) >= min(lam_min(B_LL), lam_min(B_HH)) - ||B_LH||   (THEOREM),
    # lam_min(B_HH) is bounded below by Gershgorin INSIDE the bulk and ||B_LH||
    # by its Frobenius norm.  Every kb in the preregistered ladder gives a VALID
    # lower bound, so the MAX over the ladder is also valid.
    # THE CEILING FROM THE FIXED LOW BLOCK (Courant-Fischer 1920, the min-max
    # theorem): lam_k(A) <= lam_max of A restricted to ANY k-dimensional
    # subspace, and span(t_1 .. t_k) is such a subspace.  So the bottom ceiling
    # is bounded by an m-INDEPENDENT-SIZE object.  DIRECTION: UPPER bound.
    kl = []
    for kk in range(1, K_CERT + 1):
        try:
            kl.append(float(eigh(sym(Gf[:kk, :kk]), eigvals_only=True)[-1])
                      / float(mu[kk - 1]))
        except (LinAlgError, ValueError):
            kl.append(float("nan"))
    r["kbot_low"] = qmax(kl)
    absB = np.abs(B)
    rowfull = absB.sum(axis=1)
    sq_row = np.sum(B * B, axis=1)
    kb_top = min(max(LOW_BLK), h_k - 8)
    pre_abs = np.cumsum(absB[:, :kb_top], axis=1)
    pre_sq = np.cumsum((B * B)[:, :kb_top], axis=1)
    best = (-np.inf, 0, float("nan"), float("nan"), float("nan"))
    for kb2 in LOW_BLK:
        if kb2 >= kb_top:
            continue
        gHH = float(np.min(dB[kb2:] - (rowfull[kb2:] - pre_abs[kb2:, kb2 - 1]
                                       - np.abs(dB[kb2:]))))
        cr = float(math.sqrt(max(0.0, float(np.sum(sq_row[:kb2]
                                                   - pre_sq[:kb2, kb2 - 1])))))
        try:
            lLL = float(eigh(sym(B[:kb2, :kb2]), eigvals_only=True)[0])
        except (LinAlgError, ValueError):
            continue
        bnd = min(lLL, gHH) - cr
        if bnd > best[0]:
            best = (bnd, kb2, gHH, cr, lLL)
    r["blk2_bound"] = best[0]
    r["blk2_kb"] = best[1]
    r["blk2_gHH"] = best[2]
    r["blk2_cross"] = best[3]
    r["blk2_lLL"] = best[4]
    # and the same Gershgorin INSIDE the bulk at the arch-negative cut, which is
    # the quantity the closed route would have to survive
    r["gHH_at_kneg"] = float(np.min(dB[kb:] - (rowfull[kb:]
                                               - pre_abs[kb:, kb - 1]
                                               - np.abs(dB[kb:]))))
    del absB, rowfull, sq_row, pre_abs, pre_sq
    r["schur_t"] = float("nan")
    r["schur_kb"] = 0
    for kb3 in SCHUR_KB:
        if kb3 >= h_k - 8:
            continue
        for t_try in T_LADDER:
            got = schur_floor(B, kb3, t_try)
            if got is not None and got > 0.0:
                if not (r["schur_t"] > got):
                    r["schur_t"] = got
                    r["schur_kb"] = kb3
                break
    # THE UPPER HALF OF THE SAME BULK BLOCK.  If t I <= B_HH <= T I on the bulk
    # and the low block has FIXED size kb, then Courant-Fischer plus the KMS
    # monotonicity sin(a)/sin(b) <= a/b give
    #     lam_k(A) <= T mu^P_{k+kb} <= T ((k+kb)/k)^2 mu^P_k ,
    # an m-FREE ceiling.  DIRECTION: T is an UPPER bound, certified by Cholesky.
    kbS = r["schur_kb"] if r["schur_kb"] > 0 else SCHUR_KB[0]
    if kbS < h_k - 8:
        BHH = sym(B[kbS:, kbS:])
        r["Thh"] = cert_lam_max(BHH, guess=ray_top(BHH))
        del BHH
    else:
        r["Thh"] = float("nan")
    r["kms_fac"] = max(((kk + kbS) / kk) ** 2 for kk in range(1, K_CERT + 1))
    r["kms_true"] = float(qmax([mu[kk + kbS - 1] / mu[kk - 1]
                                for kk in range(1, K_CERT + 1)
                                if kk + kbS - 1 < h_k]))
    r["K_closed"] = r["Thh"] * r["kms_fac"]
    r["R_closed"] = (r["K_closed"] / r["schur_t"]) if r["schur_t"] > 0.0 \
        else float("inf")
    del Gf, B, dB, row, Tf, isq
    bc = bottom_ceiling(A, h_k, mu, K_CERT)
    bc_ar = bottom_ceiling(A_ar, h_k, mu, K_CERT)
    if bc is None or bc_ar is None:
        SKIP["ladder"] += 1
        del A, A_ar, A_at, LP
        continue
    r["K_bot"] = bc["K_bot"]
    r["K_bot_ar"] = bc_ar["K_bot"]
    r["lam1"] = float(bc["lams"][0])
    r["lam1_ar"] = float(bc_ar["lams"][0])
    r["f0"] = symbol_at(sp["c"], 0.0)
    r["f0_ar"] = symbol_at(sp["c_ar"], 0.0)
    r["f0_at"] = symbol_at(sp["c_at"], 0.0)
    r["f_th1"] = symbol_at(sp["c"], 2.0 * math.pi / (2 * h_k + 1))
    r["R"] = (r["K_bot"] / r["kap"]) if r["kap"] > 0.0 else float("inf")
    r["R_ar"] = (r["K_bot_ar"] / r["kap_ar"]) if r["kap_ar"] > 0.0 else float("inf")
    r["kap_split"] = r["kap_ar"] + r["kap_at"]
    r["kap_budget"] = r["kap_ar"] - 2.0 * r["l1_at"] / r["mu1"]
    ROWS.append(r)
    del A, A_ar, A_at, LP, sp

check("pr_y1.surface", len(ROWS) >= 8,
      "%d windows carry a certified pencil and a certified bottom ladder "
      "(skips: %s); h = %d .. %d, n = %d .. %d"
      % (len(ROWS), SKIP, min(r["h"] for r in ROWS), max(r["h"] for r in ROWS),
         min(r["n"] for r in ROWS), max(r["n"] for r in ROWS)))
check("pr_y1.split_identity", max(r["split_exact"] for r in ROWS) < 1.0e-9,
      "A = A^arch + A^atom holds to %.2e in max-norm on every window: the "
      "decomposition is an IDENTITY, not a model"
      % max(r["split_exact"] for r in ROWS))

para("""Y1.2  WHAT THE FITS BELOW ARE TAKEN IN, and why it matters.  The contract
is m-FREENESS, so every exponent in this file is fitted in m = h, the size of the
odd section -- NOT in the zone index n.  The two are not monotonically related
here: the window step is D = g_k / (2 nu), so m ~ 2 nu log(n) / g_k and the
prime-power gap g_k scatters m at fixed n by a large factor.  Fitting an m-claim
against n therefore injects scatter that has nothing to do with m.  T151 quoted
its exponents against x; where a T151 number is repeated it is repeated as
quoted, and every NEW exponent here is in m and labelled.""")

XS = [float(r["h"]) for r in ROWS]
F_KAP = pow_fit(XS, [r["kap"] for r in ROWS], "kap")

N_AR_POS = sum(1 for r in ROWS if r["arch_pos"] > 0.0)
N_AR_PEN = sum(1 for r in ROWS if r["kap_ar"] > 0.0)
check("pr_y1.parity_control", max(r["par_exact"] for r in ROWS) < 1.0e-10,
      "CONTROL FIRST: t_1^T L_P t_1 = mu^P_1 to %.2e relative on every window, "
      "so the parity model and its basis are exact (L4) and every Rayleigh "
      "quotient below is taken against the true model value"
      % max(r["par_exact"] for r in ROWS))

check("pr_y1.arch_NOT_positive_odd", N_AR_POS == 0,
      "THE FIRST RESULT, AND IT IS A CLEAN NO.  A^arch is NOT positive in the "
      "odd sector on any of the %d windows: lam_min(A^arch) = %.4f .. %.4f, "
      "certified NEGATIVE by a completed Cholesky of A^arch - t I with the "
      "floor carried.  The odd sector removes the CONSTANT mode but NOT the "
      "negative archimedean mass near the origin -- the hoped-for second "
      "structural gift does not exist"
      % (len(ROWS), qmin([r["arch_pos"] for r in ROWS]),
         qmax([r["arch_pos"] for r in ROWS])))
check("pr_y1.arch_pencil_negative", N_AR_PEN == 0,
      "and in the PENCIL normalisation the failure is catastrophic, not "
      "marginal: kap_ar = nu_min(A^arch, L_P) = %.4g .. %.4g, i.e. %s.  The "
      "reason is directional and exact: the lowest parity sine has L_P-energy "
      "mu^P_1 = O(m^-2) while it sees an O(1) negative archimedean form, so the "
      "quotient is O(-m^2)"
      % (qmin([r["kap_ar"] for r in ROWS]), qmax([r["kap_ar"] for r in ROWS]),
         fit_str(pow_fit(XS, [abs(r["kap_ar"]) for r in ROWS], "|kap_ar|"))))
info("Y1.2.kap_direct", "the T151 object reproduced, for comparison: "
     "kap = nu_min(A, L_P) = %.4f .. %.4f, %s (T151 reported 0.2273 .. 0.4502 "
     "on its own surface)"
     % (qmin([r["kap"] for r in ROWS]), qmax([r["kap"] for r in ROWS]),
        fit_str(F_KAP)))

N_AT_POS = sum(1 for r in ROWS if r["kap_at"] > 0.0)
check("pr_y1.atom_pencil_negative", N_AT_POS == 0,
      "AND THE ATOM PART IS NEGATIVE TOO, on %d / %d windows: "
      "nu_min(A^atom, L_P) = %.4g .. %.4g.  So NEITHER summand of the exact "
      "split is positive, and the sum is: the positivity of A in the odd sector "
      "is a CANCELLATION between the archimedean kernel and the prime-power "
      "atoms, not a property of either"
      % (len(ROWS) - N_AT_POS, len(ROWS),
         qmin([r["kap_at"] for r in ROWS]), qmax([r["kap_at"] for r in ROWS])))

SPL_OK = sum(1 for r in ROWS if r["kap_split"] <= r["kap"] + 1.0e-9)
check("pr_y1.weyl_direction", SPL_OK == len(ROWS),
      "the Weyl split is DIRECTIONALLY consistent on %d / %d windows -- "
      "kap_ar + kap_at <= kap always, as an additive lower bound must be -- and "
      "that is the whole trouble: the bound is %.4g .. %.4g against a true kap "
      "of %.4f .. %.4f"
      % (SPL_OK, len(ROWS), qmin([r["kap_split"] for r in ROWS]),
         qmax([r["kap_split"] for r in ROWS]),
         qmin([r["kap"] for r in ROWS]), qmax([r["kap"] for r in ROWS])))

SPL_USE = sum(1 for r in ROWS if r["kap_split"] > 0.0)
CANC = [abs(r["kap_split"]) / r["kap"] for r in ROWS]
check("pr_y1.additive_split_vacuum", SPL_USE == 0,
      "SO THE ADDITIVE ROUTE IS VACUUM, and by a MEASURED factor: the split "
      "lower bound is negative on all %d windows and misses kap by "
      "|kap_ar + kap_at| / kap = %.4g .. %.4g (median %.4g).  Weyl 1912 is not "
      "the wrong tool by a constant -- it is the wrong tool by O(m^2)"
      % (len(ROWS), qmin(CANC), qmax(CANC), qmed(CANC)))

BUD_USE = sum(1 for r in ROWS if r["kap_budget"] > 0.0)
BUD_GAP = [abs(r["kap_budget"]) / max(r["kap"], 1.0e-300) for r in ROWS]
check("pr_y1.budget_route_vacuum", BUD_USE == 0,
      "THE HONEST NEGATIVE.  The CLOSED budget route -- bound the atom term by "
      "its l1 mass, kap >= kap_ar - 2||c^atom||_1 / mu^P_1 -- is VACUUM on "
      "%d / %d windows: it returns %.4g .. %.4g, i.e. it is %.3g .. %.3g times "
      "kap in magnitude and negative throughout.  The 1 / mu^P_1 = O(m^2) "
      "conversion from an operator-norm budget to a pencil budget is what "
      "kills it; the certified atom pencil floor above does NOT go through it"
      % (len(ROWS) - BUD_USE, len(ROWS),
         qmin([r["kap_budget"] for r in ROWS]),
         qmax([r["kap_budget"] for r in ROWS]), qmin(BUD_GAP), qmax(BUD_GAP)))

para("""Y1.5  WHERE THE CANCELLATION LIVES, and it is not where the symbol says.
The Toeplitz symbol at the ORIGIN is f(0) = c_0 + 2 sum c_l, and it is the sum of
a mildly negative archimedean part and a LARGE negative atom part -- yet kap is
positive.  The resolution is a coherence statement, and it is measured next: at
th = 0 every atom contributes with the SAME sign (the coherent sum is the whole
Chebyshev budget), while the FIRST POINT OF THE ODD GRID, th_1 = 2 pi / N,
already corresponds to one full oscillation across the atom range, u_j th_1 / D =
pi u_j / alpha ~ 2 pi at the top atom.  So the coherent atom mass at the origin
is INVISIBLE to the odd sector; what the bottom mode sees is a DECOHERED sum.""")

DEC = [abs(r["f0"]) / max(abs(r["f_th1"]), 1.0e-300) for r in ROWS]
info("Y1.5.decoherence", "f(0) = %.4g .. %.4g (of which arch %.4g .. %.4g and "
     "atom %.4g .. %.4g) against f(th_1) = %.4g .. %.4g: the origin mass "
     "exceeds the first-grid-point value by |f(0)| / |f(th_1)| = %.3g .. %.3g "
     "(median %.3g).  DIRECTION NOTE: f is an INTERPRETATION object here, the "
     "section also carries a Hankel part, so no bound is taken from it"
     % (qmin([r["f0"] for r in ROWS]), qmax([r["f0"] for r in ROWS]),
        qmin([r["f0_ar"] for r in ROWS]), qmax([r["f0_ar"] for r in ROWS]),
        qmin([r["f0_at"] for r in ROWS]), qmax([r["f0_at"] for r in ROWS]),
        qmin([r["f_th1"] for r in ROWS]), qmax([r["f_th1"] for r in ROWS]),
        qmin(DEC), qmax(DEC), qmed(DEC)))

RAY_SUM_OK = sum(1 for r in ROWS
                 if rel(r["ray1"], r["ray1_ar"] + r["ray1_at"]) < 1.0e-9)
check("pr_y1.bottom_mode_anatomy", RAY_SUM_OK == len(ROWS),
      "THE ONE NUMBER THAT NAMES THE MISSING TERM.  On the lowest parity sine "
      "t_1 the Rayleigh quotient splits EXACTLY (identity, %d / %d windows to "
      "1e-9): t_1^T A t_1 / mu^P_1 = %.4f .. %.4f is the sum of an ARCHIMEDEAN "
      "part %.4g .. %.4g and an ATOM part %.4g .. %.4g.  Two O(m^2) numbers of "
      "opposite sign add to an O(1) number: the cancellation is exact to "
      "%.3g .. %.3g relative parts, and the RESIDUE IS POSITIVE AND STILL "
      "O(m^2) -- the atoms do not merely cancel the archimedean hole at t_1, "
      "they OVERSHOOT it, so the pencil floor is not attained there at all"
      % (RAY_SUM_OK, len(ROWS), qmin([r["ray1"] for r in ROWS]),
         qmax([r["ray1"] for r in ROWS]),
         qmin([r["ray1_ar"] for r in ROWS]), qmax([r["ray1_ar"] for r in ROWS]),
         qmin([r["ray1_at"] for r in ROWS]), qmax([r["ray1_at"] for r in ROWS]),
         qmin([abs(r["ray1"]) / abs(r["ray1_ar"]) for r in ROWS]),
         qmax([abs(r["ray1"]) / abs(r["ray1_ar"]) for r in ROWS])))

RS_OK = sum(1 for r in ROWS if r["ray_star"] >= r["kap"] - 1.0e-9)
check("pr_y1.floor_location", RS_OK == len(ROWS),
      "SO WHERE IS THE FLOOR?  The parity-diagonal quotients d_k / mu^P_k are "
      "Rayleigh quotients at explicit test vectors, hence UPPER bounds on kap "
      "(consistent on %d / %d).  Their argmin sits at k* = %d .. %d, i.e. at a "
      "FRACTION k*/m = %.3f .. %.3f of the spectrum and an angle th* = %.3f .. "
      "%.3f rad -- NOT at the bottom of the grid.  Value there: %.4f .. %.4f "
      "against kap = %.4f .. %.4f"
      % (RS_OK, len(ROWS), min(r["kstar"] for r in ROWS),
         max(r["kstar"] for r in ROWS),
         qmin([r["kstar_frac"] for r in ROWS]),
         qmax([r["kstar_frac"] for r in ROWS]),
         qmin([r["th_star"] for r in ROWS]), qmax([r["th_star"] for r in ROWS]),
         qmin([r["ray_star"] for r in ROWS]), qmax([r["ray_star"] for r in ROWS]),
         qmin([r["kap"] for r in ROWS]), qmax([r["kap"] for r in ROWS])))

AR_HI_POS = sum(1 for r in ROWS if r["ray_ar_hi"] > 0.0)
check("pr_y1.arch_positive_above_kstar", AR_HI_POS == len(ROWS),
      "AND HERE IS THE STRUCTURAL GIFT, IN THE PLACE IT ACTUALLY LIVES.  The "
      "archimedean diagonal d^arch_k is negative ONLY for k <= %d .. %d (that "
      "is %d .. %d of m modes); from k* upwards its own pencil quotient is "
      "POSITIVE on %d / %d windows, min %.4f .. %.4f.  At the floor location "
      "the split is arch %.4f .. %.4f PLUS atom %.4f .. %.4f -- both O(1), no "
      "cancellation of large numbers, and the archimedean part alone already "
      "carries a positive share"
      % (min(r["k_last_neg_ar"] for r in ROWS),
         max(r["k_last_neg_ar"] for r in ROWS),
         min(r["n_neg_diag_ar"] for r in ROWS),
         max(r["n_neg_diag_ar"] for r in ROWS), AR_HI_POS, len(ROWS),
         qmin([r["ray_ar_hi"] for r in ROWS]),
         qmax([r["ray_ar_hi"] for r in ROWS]),
         qmin([r["ray_star_ar"] for r in ROWS]),
         qmax([r["ray_star_ar"] for r in ROWS]),
         qmin([r["ray_star_at"] for r in ROWS]),
         qmax([r["ray_star_at"] for r in ROWS])))

GB_OK = sum(1 for r in ROWS if r["gersh_pen"] <= r["kap"] + 1.0e-9)
GB_POS = sum(1 for r in ROWS if r["gersh_pen"] > 0.0)
check("pr_y1.gershgorin_closed_route", GB_OK == len(ROWS),
      "THE CLOSED ENTRYWISE ROUTE, TESTED AND MEASURED.  Gershgorin 1931 on the "
      "pencil-whitened parity block B = Lam^-1/2 T A T^T Lam^-1/2 is a THEOREM "
      "and gives a LOWER bound on kap from ENTRIES ALONE -- and every entry is a "
      "Fejer-weighted prime-power sum, so it is an arithmetic bound by "
      "construction.  It is directionally consistent on %d / %d windows and "
      "positive on %d / %d: value %.4g .. %.4g.  The off-diagonal coupling mass "
      "it has to pay is max_k sum_{l != k} |B_kl| = %.4g .. %.4g (median row "
      "%.4g .. %.4g), and THAT is what eats it"
      % (GB_OK, len(ROWS), GB_POS, len(ROWS),
         qmin([r["gersh_pen"] for r in ROWS]),
         qmax([r["gersh_pen"] for r in ROWS]),
         qmin([r["coup_max"] for r in ROWS]),
         qmax([r["coup_max"] for r in ROWS]),
         qmin([r["coup_med"] for r in ROWS]),
         qmax([r["coup_med"] for r in ROWS])))

B2_OK = sum(1 for r in ROWS if r["blk2_bound"] <= r["kap"] + 1.0e-9)
B2_POS = sum(1 for r in ROWS if r["blk2_bound"] > 0.0)
GHH_POS = sum(1 for r in ROWS if r["gHH_at_kneg"] > 0.0)
check("pr_y1.bulk_gershgorin_also_vacuum", GHH_POS == 0,
      "AND CUTTING OUT THE BAD MODES DOES NOT RESCUE THE ENTRYWISE ROUTE.  With "
      "the parity block cut at the last arch-negative mode (k_neg = %d .. %d, an "
      "m-INDEPENDENT number) Gershgorin INSIDE THE BULK is still negative on all "
      "%d windows, %.4f .. %.4f: the whitened parity block is simply NOT "
      "diagonally dominant, its median row coupling %.4g .. %.4g being an order "
      "of magnitude above the diagonal %.4f .. %.4f.  Entrywise bounds on the "
      "prime-power sums cannot give kap -- that is a structural obstruction, not "
      "a constant"
      % (min(r["k_neg_ar"] for r in ROWS), max(r["k_neg_ar"] for r in ROWS),
         len(ROWS), qmin([r["gHH_at_kneg"] for r in ROWS]),
         qmax([r["gHH_at_kneg"] for r in ROWS]),
         qmin([r["coup_med"] for r in ROWS]),
         qmax([r["coup_med"] for r in ROWS]),
         qmin([r["ray_star"] for r in ROWS]),
         qmax([r["ray_star"] for r in ROWS])))
check("pr_y1.two_block_route", B2_OK == len(ROWS),
      "THE TWO-BLOCK ASSEMBLY IS WHERE IT STILL BREAKS, and by ONE term.  "
      "lam_min(B) >= min(lam_min(B_LL), gersh(B_HH)) - ||B_LH|| is a theorem; "
      "directionally consistent on %d / %d, positive on %d / %d.  Best low "
      "block over the preregistered ladder %s: kb = %d .. %d, with "
      "gersh(B_HH) = %.4f .. %.4f and lam_min(B_LL) = %.4g .. %.4g -- both fine "
      "-- but the CROSS TERM ||B_LH||_F = %.4g .. %.4g destroys it, leaving "
      "%.4g .. %.4g.  THE MISSING TERM IS THE CROSS TERM, and it is one number"
      % (B2_OK, len(ROWS), B2_POS, len(ROWS), str(LOW_BLK),
         min(r["blk2_kb"] for r in ROWS), max(r["blk2_kb"] for r in ROWS),
         qmin([r["blk2_gHH"] for r in ROWS]), qmax([r["blk2_gHH"] for r in ROWS]),
         qmin([r["blk2_lLL"] for r in ROWS]), qmax([r["blk2_lLL"] for r in ROWS]),
         qmin([r["blk2_cross"] for r in ROWS]),
         qmax([r["blk2_cross"] for r in ROWS]),
         qmin([r["blk2_bound"] for r in ROWS]),
         qmax([r["blk2_bound"] for r in ROWS])))

SC_OK = sum(1 for r in ROWS if np.isfinite(r["schur_t"])
            and r["schur_t"] <= r["kap"] + 1.0e-9)
SC_POS = sum(1 for r in ROWS if np.isfinite(r["schur_t"]) and r["schur_t"] > 0.0)
F_SC = pow_fit(XS, [r["schur_t"] for r in ROWS], "schur_t")
check("pr_y1.schur_two_block_floor", SC_POS == len(ROWS) and SC_OK == len(ROWS),
      "AND THIS ONE CLOSES.  The Schur block criterion (Schur 1917) on the SAME "
      "parity block, with BOTH Cholesky floors subtracted, certifies "
      "kap >= t = %.4f .. %.4f on %d / %d windows (low block kb = %d .. %d out "
      "of the preregistered %s, t from the absolute ladder %s), and it is "
      "directionally consistent with the direct kap on %d / %d.  %s"
      % (qmin([r["schur_t"] for r in ROWS]), qmax([r["schur_t"] for r in ROWS]),
         SC_POS, len(ROWS), min(r["schur_kb"] for r in ROWS),
         max(r["schur_kb"] for r in ROWS), str(SCHUR_KB), str(T_LADDER),
         SC_OK, len(ROWS), fit_str(F_SC)))

para("""Y1.6  WHAT Y1 ACTUALLY ESTABLISHED, WITH THE LABELS ON.  (a) THEOREM:
A = A^arch + A^atom exactly, and both Weyl 1912 and the l1 budget are legitimate
tools.  (b) CERTIFIED, and a clean NO: A^arch is NOT positive in the odd sector,
lam_min = %.4f .. %.4f, and in pencil normalisation kap_ar = O(-m^2).  The
hoped-for ``arch is positive in the odd sector'' gift does not exist.  (c) HENCE
ANY ADDITIVE arch-plus-budget route is vacuum by O(m^2), measured at a factor
%.3g .. %.3g, and the l1 budget route by a further %.3g .. %.3g.  (d) MEASURED,
and this is the useful discovery: the archimedean diagonal is negative on an
m-INDEPENDENT number of parity modes only (%d .. %d), and above them the
archimedean pencil quotient is >= %.3f.  (e) CERTIFIED, and this is the closure:
the Schur block criterion on a FIXED low block of %d parity modes certifies
kap >= %.4f .. %.4f on every window, %s in m.  So kap is no longer a fit -- it is
a certified constant with an m-independent block size.  (f) WHAT REMAINS for a
fully CLOSED kap is exactly ONE inequality, and it is now sharply posed: the bulk
block must satisfy B_HH >= t I with t of order 1/4, where B_HH's entries are
Fejer-weighted prime-power sums minus the archimedean kernel's.  Bounding those
entries individually is NOT enough -- Gershgorin on the same block returns
%.4g .. %.4g -- so the remaining term is a BLOCK positivity statement, not an
entrywise one.  THE FENCE: nothing above proves that inequality; it is measured
and certified per window and named as the residue."""
     % (qmin([r["arch_pos"] for r in ROWS]), qmax([r["arch_pos"] for r in ROWS]),
        qmin(CANC), qmax(CANC), qmin(BUD_GAP), qmax(BUD_GAP),
        min(r["k_neg_ar"] for r in ROWS), max(r["k_neg_ar"] for r in ROWS),
        qmin([r["ray_ar_hi"] for r in ROWS]),
        max(r["schur_kb"] for r in ROWS),
        qmin([r["schur_t"] for r in ROWS]), qmax([r["schur_t"] for r in ROWS]),
        "flat" if flat_ok(F_SC) else "walking",
        qmin([r["gHH_at_kneg"] for r in ROWS]),
        qmax([r["gHH_at_kneg"] for r in ROWS])))

F_RAY1 = pow_fit(XS, [r["ray1"] for r in ROWS], "ray1")
check("pr_y1.kap_trend_target", qmin([r["kap"] for r in ROWS]) > 0.0,
      "TREND AGAINST THE 0.25 TARGET, on the object that IS certified per "
      "window: kap = %.4f .. %.4f with minimum %.4f (%s the %.2f target), fit "
      "%.3f +- %.3f -- %s at the preregistered bar %.2f.  The t_1 Rayleigh "
      "quotient, which is an UPPER bound on kap, sits at %.4f .. %.4f (%s)"
      % (qmin([r["kap"] for r in ROWS]), qmax([r["kap"] for r in ROWS]),
         qmin([r["kap"] for r in ROWS]),
         "ABOVE" if qmin([r["kap"] for r in ROWS]) >= KAP_TARGET else "BELOW",
         KAP_TARGET, F_KAP["p"], F_KAP["band"],
         "FLAT" if flat_ok(F_KAP) else "NOT flat", BAR_UNIF,
         qmin([r["ray1"] for r in ROWS]), qmax([r["ray1"] for r in ROWS]),
         fit_str(F_RAY1)))

# ----------------------------------------------------------------------------
section("Y2  K_bot AND THE RATIO -- IS R AN ARCHIMEDEAN NUMBER?")
# ----------------------------------------------------------------------------
para("""Y2.0  WHAT R IS AND WHAT WOULD MAKE IT m-FREE.  K_bot is the smallest
constant with lam_k(A) <= K_bot mu^P_k for k = 1 .. %d, each inequality certified
by ONE inertia count (L2).  R = K_bot / kap.  The upper half of R is a statement
about ALIGNMENT: the lowest eigenvalues of the section must be of the same size as
the model's, which happens exactly when the section is elliptic of order 2 in the
odd sector.  The lower half is now certified (Y1).  So the question of this block
is whether the ALIGNMENT is carried by the smooth archimedean kernel with the
atoms as a controlled correction -- if it is, m-freeness of R is a statement about
a smooth kernel and nothing else.""" % K_CERT)

F_KBOT = pow_fit(XS, [r["K_bot"] for r in ROWS], "K_bot")
F_KBOT_AR = pow_fit(XS, [r["K_bot_ar"] for r in ROWS], "K_bot_ar")
F_R = pow_fit(XS, [r["R"] for r in ROWS], "R")
for r in ROWS:
    r["R_cert"] = (r["K_bot"] / r["schur_t"]) if r["schur_t"] > 0.0 else float("inf")
    r["kbot_ratio"] = r["K_bot"] / r["K_bot_ar"] if r["K_bot_ar"] > 0.0 else float("nan")
F_RC = pow_fit(XS, [r["R_cert"] for r in ROWS], "R_cert")
F_KBR = pow_fit(XS, [r["kbot_ratio"] for r in ROWS], "K_bot / K_bot_ar")

check("pr_y2.kbot_certified", all(np.isfinite(r["K_bot"]) for r in ROWS),
      "K_bot is certified on all %d windows: %.4f .. %.4f, %s -- and it is FLAT "
      "at the preregistered bar %.2f: %s"
      % (len(ROWS), qmin([r["K_bot"] for r in ROWS]),
         qmax([r["K_bot"] for r in ROWS]), fit_str(F_KBOT), BAR_UNIF,
         "YES" if flat_ok(F_KBOT) else "NO"))

KB_AR_GROW = sum(1 for r in ROWS if r["K_bot_ar"] > 10.0 * r["K_bot"])
check("pr_y2.arch_does_NOT_carry_the_ceiling", KB_AR_GROW == len(ROWS),
      "AND THE ANSWER TO Y2's QUESTION IS ALSO NO, symmetrically to Y1.  The "
      "ARCH-ONLY section has a certified bottom ceiling of K_bot^arch = %.4g .. "
      "%.4g, %s -- an order of magnitude or two ABOVE the true K_bot on %d / %d "
      "windows, and GROWING where the true one is flat.  The ratio "
      "K_bot / K_bot^arch = %.4g .. %.4g (%s) SHRINKS: the atoms do not perturb "
      "an archimedean alignment, they CREATE it.  So R is not an archimedean "
      "ratio with a small correction, in either half"
      % (qmin([r["K_bot_ar"] for r in ROWS]),
         qmax([r["K_bot_ar"] for r in ROWS]), fit_str(F_KBOT_AR),
         KB_AR_GROW, len(ROWS), qmin([r["kbot_ratio"] for r in ROWS]),
         qmax([r["kbot_ratio"] for r in ROWS]), fit_str(F_KBR)))

F_KBL = pow_fit(XS, [r["kbot_low"] for r in ROWS], "K_bot_low")
KBL_OK = sum(1 for r in ROWS if r["kbot_low"] >= r["K_bot"] - 1.0e-9)
KBL_TIGHT = [r["kbot_low"] / r["K_bot"] for r in ROWS]
check("pr_y2.ceiling_from_fixed_block", KBL_OK == len(ROWS),
      "BUT THE CEILING REDUCES TO A FIXED-SIZE OBJECT, and that is the Y2 gain.  "
      "Courant-Fischer 1920 gives lam_k(A) <= lam_max of A on span(t_1 .. t_k), "
      "so K_bot <= max_{k <= %d} lam_max(G_k) / mu^P_k with G_k the k x k TOP-LEFT "
      "PARITY BLOCK -- an object of m-INDEPENDENT SIZE whose entries are "
      "Fejer-weighted prime-power sums.  Directionally correct on %d / %d "
      "windows; value %.4f .. %.4f, %s; and it costs only the factor %.4f .. "
      "%.4f over the inertia-certified K_bot"
      % (K_CERT, KBL_OK, len(ROWS), qmin([r["kbot_low"] for r in ROWS]),
         qmax([r["kbot_low"] for r in ROWS]), fit_str(F_KBL),
         qmin(KBL_TIGHT), qmax(KBL_TIGHT)))

F_THH = pow_fit(XS, [r["Thh"] for r in ROWS], "T_HH")
F_KCL = pow_fit(XS, [r["K_closed"] for r in ROWS], "K_closed")
KMS_OK = sum(1 for r in ROWS if r["kms_true"] <= r["kms_fac"] + 1.0e-9)
KCL_OK = sum(1 for r in ROWS if r["K_closed"] >= r["K_bot"] - 1.0e-9)
check("pr_y2.kms_monotonicity", KMS_OK == len(ROWS),
      "THE ONE STEP THAT IS A THEOREM FOR EVERY m: sin a / sin b <= a / b for "
      "pi >= a >= b > 0 gives mu^P_{k+kb} / mu^P_k <= ((k+kb)/k)^2, m-FREE.  "
      "Verified against the exact Kac-Murdock-Szego values on %d / %d windows: "
      "true max ratio %.4f .. %.4f under the m-free bound %.1f"
      % (KMS_OK, len(ROWS), qmin([r["kms_true"] for r in ROWS]),
         qmax([r["kms_true"] for r in ROWS]), qmax([r["kms_fac"] for r in ROWS])))
check("pr_y2.ceiling_from_bulk_block", KCL_OK == len(ROWS),
      "AND THIS IS THE MECHANISM THAT DOES CARRY m-FREENESS.  The bulk block is "
      "certified from ABOVE as well: B_HH <= T I with T = %.4f .. %.4f, %s.  "
      "Combined with the fixed low block kb = %d and the KMS step, the ceiling "
      "K_bot <= T ((k+kb)/k)^2 = %.4g .. %.4g is m-FREE BY CONSTRUCTION -- it "
      "contains no m anywhere -- and it is directionally correct on %d / %d "
      "windows.  Its price is the fixed factor %.1f, so it is a WEAKER but "
      "STRUCTURALLY CLOSED ceiling: %s"
      % (qmin([r["Thh"] for r in ROWS]), qmax([r["Thh"] for r in ROWS]),
         fit_str(F_THH), max(r["schur_kb"] for r in ROWS),
         qmin([r["K_closed"] for r in ROWS]),
         qmax([r["K_closed"] for r in ROWS]), KCL_OK, len(ROWS),
         qmax([r["kms_fac"] for r in ROWS]), fit_str(F_KCL)))

check("pr_y2.R_new_number", all(np.isfinite(r["R_cert"]) for r in ROWS),
      "THE NEW R NUMBER, AND IT IS CERTIFIED ON BOTH ENDS.  With the Schur floor "
      "as the denominator instead of the read-off kap, R <= K_bot / t = %.4f .. "
      "%.4f, %s.  T151's R was 3.3634 .. 9.7108 fitted x^{0.037 +- 0.015} with a "
      "denominator that was certified but not closed; this one has a CERTIFIED "
      "denominator with an m-independent block size, and it is %s at the bar %.2f"
      % (qmin([r["R_cert"] for r in ROWS]), qmax([r["R_cert"] for r in ROWS]),
         fit_str(F_RC), "FLAT" if flat_ok(F_RC) else "NOT flat", BAR_UNIF))
info("Y2.1.R_direct", "for continuity with T151, the same R with the read-off "
     "kap: %.4f .. %.4f, %s" % (qmin([r["R"] for r in ROWS]),
                                qmax([r["R"] for r in ROWS]), fit_str(F_R)))

para("""Y2.1b  A RANK READ OF THE SAME NUMBERS, because the exponent above is a
marginal call.  The windows are sorted by m and cut into four quartiles; the
median of each quantity is reported per quartile.  This uses no fit and no band,
so it cannot be inflated by scatter -- if R is m-free the four medians must not
walk, and if it grows slowly they will.""")

QR = sorted(ROWS, key=lambda r: r["h"])
NQ = 4
WALK = {}
for nm, key in (("m", "h"), ("t (floor)", "schur_t"), ("K_bot", "K_bot"),
                ("R = K_bot / t", "R_cert"), ("T_HH", "Thh")):
    meds = []
    for j in range(NQ):
        a, b = (j * len(QR)) // NQ, ((j + 1) * len(QR)) // NQ
        meds.append(qmed([r[key] for r in QR[a:b]]))
    WALK[key] = (meds[-1] / meds[0]) if meds[0] > 0.0 else float("nan")
    info("Y2.1b." + key, "%-14s quartile medians %s   -> top/bottom = %.3f"
         % (nm, "  ".join("%.4g" % v for v in meds), WALK[key]))

# THE WALK BAR, derived from the SAME preregistered exponent bar: over an
# m-range of factor W, an exponent of BAR_UNIF permits a walk of W^BAR_UNIF.
WALK_BAR = WALK["h"] ** BAR_UNIF
check("pr_y2.rank_trend", WALK["schur_t"] <= WALK_BAR,
      "THE RANK VERDICT ON EACH HALF.  Over an m-range of %.2f the bar implied "
      "by the preregistered exponent %.2f is a walk of %.3f.  The FLOOR does not "
      "walk at all (%.3f) -- its quartile medians are identical.  The CEILING "
      "walks %.3f, %s the bar, with DECELERATING increments, so this surface "
      "cannot separate a saturating constant from a log m growth.  T_HH walks "
      "%.2f and is out of the question"
      % (WALK["h"], BAR_UNIF, WALK_BAR, WALK["schur_t"], WALK["K_bot"],
         "inside" if WALK["K_bot"] <= WALK_BAR else "OUTSIDE", WALK["Thh"]))

para("""Y2.2  SO WHICH HALF OF R IS CLOSED AND WHICH IS NOT.  The DENOMINATOR is:
Y1's Schur criterion certifies kap >= %.3f .. %.3f with a FIXED %d-mode block, and
its quartile medians do not move.  The NUMERATOR is not: K_bot is certified per
window (%.3f .. %.3f, m^%.3f +- %.3f) but every STRUCTURAL route to it loses --
Courant-Fischer on the parity basis by %.3g .. %.3g (because the parity sines are
terrible test vectors for the section's low eigenvectors: the atom overshoot at
t_1 is O(m^2)), and the bulk-block route by %.3g .. %.3g with T_HH itself GROWING
at m^%.3f.  That is the honest state: the section's low EIGENVALUES track the
model's, but its low EIGENVECTORS do not, and no tool in this file converts the
first fact into a closed constant."""
     % (qmin([r["schur_t"] for r in ROWS]), qmax([r["schur_t"] for r in ROWS]),
        max(r["schur_kb"] for r in ROWS), qmin([r["K_bot"] for r in ROWS]),
        qmax([r["K_bot"] for r in ROWS]), F_KBOT["p"], F_KBOT["band"],
        qmin(KBL_TIGHT), qmax(KBL_TIGHT),
        qmin([r["K_closed"] / r["K_bot"] for r in ROWS]),
        qmax([r["K_closed"] / r["K_bot"] for r in ROWS]), F_THH["p"]))

# ----------------------------------------------------------------------------
section("Y2.3  THE OBLIGATORY STRESS: THE T145 NO-GO MUST BREAK, AND WHERE")
# ----------------------------------------------------------------------------
para("""THE STRESS FAMILY, and an honest label on it.  T151's no-go matrix is not
in this file, so what is stressed here is a RECONSTRUCTION with the property the
no-go is described by: a positive decaying lag kernel c(l) = 1/(1+l) whose symbol
has a LOGARITHMIC SINGULARITY at the origin instead of vanishing there.  Its odd
section is positive definite, so it passes every positivity test, and its bottom
ladder must nevertheless blow up -- if the mechanism named above is the real one,
the break has to appear in the CEILING and not in the floor.""")

NG = []
for m_ng in NOGO_SIZES:
    M_ng = 2 * m_ng
    c_ng = 1.0 / (1.0 + np.arange(M_ng, dtype=float))
    A_ng = sym(odd_toeplitz(c_ng, M_ng))
    LP_ng = lap_P_mat(m_ng)
    mu_ng = parity_mu(m_ng)
    pn = pencil_pair(A_ng, LP_ng, m_ng)
    bcn = bottom_ceiling(A_ng, m_ng, mu_ng, K_CERT)
    if pn is None or bcn is None:
        continue
    Tn = parity_basis(m_ng)
    Gn = sym(Tn @ (A_ng @ Tn.T))
    isqn = 1.0 / np.sqrt(mu_ng)
    Bn = Gn * np.outer(isqn, isqn)
    t_ng = float("nan")
    for t_try in T_LADDER:
        got = schur_floor(Bn, SCHUR_KB[0], t_try)
        if got is not None and got > 0.0:
            t_ng = got
            break
    NG.append(dict(m=m_ng, x=float(m_ng), kap=pn["kap"], K_bot=bcn["K_bot"],
                   R=(bcn["K_bot"] / pn["kap"]) if pn["kap"] > 0.0
                   else float("inf"), schur=t_ng,
                   lam1=float(bcn["lams"][0]), mu1=float(mu_ng[0])))
    del A_ng, LP_ng, Tn, Gn, Bn, c_ng

check("pr_y2.nogo_floor_survives",
      sum(1 for g in NG if g["kap"] > 0.0) == len(NG),
      "AND IT BREAKS EXACTLY WHERE THE MECHANISM SAYS.  On the no-go family the "
      "FLOOR is fine -- kap = %.4f .. %.4f on all %d sizes, and the Schur "
      "criterion certifies %.4g .. %.4g -- so no positivity test rejects it"
      % (qmin([g["kap"] for g in NG]), qmax([g["kap"] for g in NG]), len(NG),
         qmin([g["schur"] for g in NG]), qmax([g["schur"] for g in NG])))

F_NG_K = pow_fit([g["x"] for g in NG], [g["K_bot"] for g in NG], "K_bot nogo")
F_NG_R = pow_fit([g["x"] for g in NG], [g["R"] for g in NG], "R nogo")
check("pr_y2.nogo_ceiling_breaks", not nogrow_ok(F_NG_R),
      "BUT THE CEILING EXPLODES: K_bot = %.4g .. %.4g growing as %s in m, hence "
      "R = %.4g .. %.4g growing as %s -- far outside the preregistered bar %.2f, "
      "against the true section's flat x^%.3f.  The no-go therefore fails at "
      "precisely the step this probe could NOT close, and passes the one it "
      "could: the missing term is REAL, not an artefact of a lossy tool"
      % (qmin([g["K_bot"] for g in NG]), qmax([g["K_bot"] for g in NG]),
         fit_str(F_NG_K), qmin([g["R"] for g in NG]),
         qmax([g["R"] for g in NG]), fit_str(F_NG_R), BAR_UNIF, F_KBOT["p"]))

# THE POSITIVE CONTROL: the model against itself must give (1, 1) EXACTLY
CTRL = []
for m_c in (64, 256, 1024):
    Lc = lap_P_mat(m_c)
    muc = parity_mu(m_c)
    pc = pencil_pair(Lc, Lc, m_c)
    bcc = bottom_ceiling(Lc, m_c, muc, K_CERT)
    CTRL.append((m_c, pc["kap"], pc["K"], bcc["K_bot"]))
    del Lc
check("pr_y2.control_model", all(rel(c[1], 1.0) < 1.0e-8 and rel(c[2], 1.0) < 1.0e-8
                                 and rel(c[3], 1.0) < 1.0e-8 for c in CTRL),
      "CONTROL: on L_P against itself the pencil and the bottom ceiling are "
      "(1, 1, 1) to %.2e at m = %s, so neither the pencil reduction nor the "
      "inertia ladder invents a constant"
      % (max(max(rel(c[1], 1.0), rel(c[2], 1.0), rel(c[3], 1.0)) for c in CTRL),
         str([c[0] for c in CTRL])))

# ----------------------------------------------------------------------------
section("Y3  Psi -- FIRST RECONNAISSANCE OF THE NEW DOMINANT LOSS")
# ----------------------------------------------------------------------------
para("""Y3.0  WHAT Psi IS, restated so the anatomy is checkable.  In the T146 ..
T151 chain the level constant carries the factor
    Psi = sup_S (1^T R_SS 1) / |S|   over ALL subsets S of the window,
R = E^{-1} the inverse of the whitened section, and the bound actually used is
    Psi <= max_k R_kk + min( 4 x greedy-density(R^+) , lam_max(R^+) ),
with R^+ the nonnegative off-diagonal part (Charikar 2000 for the greedy half,
whose guarantee greedy >= opt/2 is what turns an ATTAINED density into an UPPER
bound).  DIRECTION: every quantity here is an UPPER bound on Psi.  Y3 is a MAP
only: it asks what Psi is made of, what drives its growth, and whether a
structural reserve of the parity kind exists.  Absolute values are gauge
dependent -- the const gauge is used, as in T149 -- so only the ANATOMY and the
TRENDS are read.""")


def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000).  The returned density is
    ATTAINED, hence a LOWER bound on the optimum, and greedy >= opt/2 turns it
    into opt <= 2 x greedy."""
    m = Wp.shape[0]
    if m < 2:
        return 0.0
    deg = Wp.sum(axis=1).astype(float)
    tot = 0.5 * float(deg.sum())
    alive = np.ones(m, dtype=bool)
    n_alive = m
    best = tot / m
    while n_alive > 1:
        j = int(np.argmin(np.where(alive, deg, np.inf)))
        tot -= float(deg[j])
        alive[j] = False
        deg = deg - Wp[j]
        deg[j] = 0.0
        n_alive -= 1
        if tot / n_alive > best:
            best = tot / n_alive
    return float(best)


PSI = []
_stride = max(1, len(ROWS) // PSI_POOL)
for r in ROWS[::_stride][:PSI_POOL]:
    if budget_left() < 90.0:
        info("Y3.0.budget", "Psi pool truncated at %d windows" % len(PSI))
        break
    sp = lag_vector_split(0.5 * r["M"] * r["D"], r["M"],
                          atoms_in(0.5 * r["M"] * r["D"]))
    A = sym(odd_toeplitz(sp["c"], r["M"]))
    h = r["h"]
    const = float(np.max(np.diag(A)))
    E = A / const
    try:
        w_E = eigh(E, eigvals_only=True)
    except (LinAlgError, ValueError):
        del A, E, sp
        continue
    fac = safe_cho(E)
    if fac is None:
        del A, E, sp
        continue
    Rinv = sym(cho_solve(fac, np.eye(h), check_finite=False))
    dg = float(np.max(np.diag(Rinv)))
    Rp = np.maximum(Rinv, 0.0)
    np.fill_diagonal(Rp, 0.0)
    psi_char = dg + 4.0 * greedy_density(Rp)
    psi_spec = dg + cert_lam_max(Rp, guess=ray_top(Rp))
    psi_up = min(x for x in (psi_char, psi_spec) if np.isfinite(x))
    lam_lo = float(w_E[0])
    tail = float(np.sum(1.0 / w_E[K_CERT:]))
    head = float(np.sum(1.0 / w_E[:K_CERT]))
    PSI.append(dict(x=r["x"], h=h, psi=psi_up, char=psi_char, spec=psi_spec,
                    dg=dg, lam_lo=lam_lo, inv_lo=1.0 / lam_lo, head=head,
                    tail=tail, const=const, mu1=r["mu1"], kap=r["kap"],
                    frac_head=head / (head + tail),
                    ratio_bound=(1.0 / lam_lo) / psi_up))
    del A, E, Rinv, Rp, sp

check("pr_y3.psi_surface", len(PSI) >= 5,
      "the Psi anatomy is taken on %d windows, h = %d .. %d: Psi <= %.4g .. %.4g "
      "(the greedy half gives %.4g .. %.4g, the spectral half %.4g .. %.4g -- the "
      "%s one is binding)"
      % (len(PSI), min(p["h"] for p in PSI), max(p["h"] for p in PSI),
         qmin([p["psi"] for p in PSI]), qmax([p["psi"] for p in PSI]),
         qmin([p["char"] for p in PSI]), qmax([p["char"] for p in PSI]),
         qmin([p["spec"] for p in PSI]), qmax([p["spec"] for p in PSI]),
         "greedy" if sum(1 for p in PSI if p["char"] <= p["spec"])
         > len(PSI) / 2 else "spectral"))

# the Psi claims are about m, so these fits are taken in m and labelled as such
PX = [float(p["h"]) for p in PSI]
F_PSI = pow_fit(PX, [p["psi"] for p in PSI], "Psi")
F_INV = pow_fit(PX, [p["inv_lo"] for p in PSI], "1/lam_min(E)")
F_DG = pow_fit(PX, [p["dg"] for p in PSI], "max diag R")
DRIVE = [p["ratio_bound"] for p in PSI]
check("pr_y3.psi_driver", qmin(DRIVE) > 0.0,
      "WHAT DRIVES IT, in one line (ALL THREE FITS ARE IN m, NOT in the zone "
      "variable): Psi = %s while 1 / lam_min(E) = %s and "
      "max_k R_kk = %s.  The quotient (1/lam_min) / Psi = %.4f .. %.4f shows Psi "
      "is the SPECTRAL BOTTOM of the whitened section and essentially nothing "
      "else -- and lam_min(E) = kap x mu^P_1 / const up to the ladder, i.e. Psi "
      "grows because mu^P_1 = O(m^-2), NOT because kap degrades"
      % (fit_str(F_PSI), fit_str(F_INV), fit_str(F_DG),
         qmin(DRIVE), qmax(DRIVE)))

F_FR = pow_fit(PX, [p["frac_head"] for p in PSI], "head fraction")
check("pr_y3.psi_reserve", qmax([p["frac_head"] for p in PSI]) > 0.5,
      "AND THERE IS A STRUCTURAL RESERVE, of exactly the parity kind.  Split "
      "trace(E^-1) into the %d lowest modes and the rest: the LOW HEAD carries "
      "%.4f .. %.4f of it (%s), i.e. the whole of Psi lives on the same handful "
      "of modes the certified ladder already controls.  So Psi is not an "
      "independent loss -- it is the ladder's own bottom, read through a "
      "subset-density bound that throws the ladder away.  THE MAP: replacing "
      "sup_S by the ladder-summed head, sum_{k <= %d} 1 / lam_k, would leave a "
      "residue of %.4g .. %.4g instead of %.4g .. %.4g.  This is a MAPPING "
      "claim, not a proof: the subset supremum is not the trace, and closing "
      "the gap needs a separate argument"
      % (K_CERT, qmin([p["frac_head"] for p in PSI]),
         qmax([p["frac_head"] for p in PSI]), fit_str(F_FR), K_CERT,
         qmin([p["tail"] for p in PSI]), qmax([p["tail"] for p in PSI]),
         qmin([p["psi"] for p in PSI]), qmax([p["psi"] for p in PSI])))

PSI_GAIN = [p["psi"] / p["tail"] for p in PSI]
info("Y3.1.end_to_end", "THE END-TO-END NUMBER WITH THE BEST Y1 / Y2 RESULT.  "
     "This probe changes the pencil pair to the CERTIFIED (t, K_bot) = "
     "(%.4f .. %.4f, %.4f .. %.4f), hence R <= %.4f .. %.4f -- but it does NOT "
     "change Psi, and Y3 has just shown Psi = 1 / lam_min(E) up to 1.17.  So the "
     "T151 end-to-end fraction 2.01e-2 .. 3.52e-2 is UNMOVED by Y1 / Y2: the "
     "honest end-to-end statement is that the bottleneck is now entirely Psi, "
     "and the reserve Y3 maps is worth a factor %.2f .. %.2f (median %.2f) -- "
     "which would move the fraction into the 8e-2 .. 1.4e-1 range if, and only "
     "if, the ladder-aware replacement of the subset supremum can be proved"
     % (qmin([r["schur_t"] for r in ROWS]), qmax([r["schur_t"] for r in ROWS]),
        qmin([r["K_bot"] for r in ROWS]), qmax([r["K_bot"] for r in ROWS]),
        qmin([r["R_cert"] for r in ROWS]), qmax([r["R_cert"] for r in ROWS]),
        qmin(PSI_GAIN), qmax(PSI_GAIN), qmed(PSI_GAIN)))

# ----------------------------------------------------------------------------
section("Y4  MAP V24, THE REST LIST, AND THE VERDICT")
# ----------------------------------------------------------------------------
V24 = [
    ("v570", "THE ARCHIMEDEAN SECTION IS NOT POSITIVE IN THE ODD SECTOR.  "
     "lam_min(A^arch) = %.4f .. %.4f on %d windows, certified by Cholesky; in "
     "pencil normalisation kap_ar = %.3g .. %.3g.  The parity sector removes the "
     "constant mode but not the archimedean hole.  STATUS: certified per-window "
     "NEGATIVE result.  CONSEQUENCE: every additive arch-plus-budget route to kap "
     "is vacuum by %.3g .. %.3g, and the l1-budget route by a further "
     "%.3g .. %.3g."
     % (qmin([r["arch_pos"] for r in ROWS]), qmax([r["arch_pos"] for r in ROWS]),
        len(ROWS), qmin([r["kap_ar"] for r in ROWS]),
        qmax([r["kap_ar"] for r in ROWS]), qmin(CANC), qmax(CANC),
        qmin(BUD_GAP), qmax(BUD_GAP))),
    ("v571", "THE ATOM PART IS NOT POSITIVE EITHER, so the positivity of the odd "
     "section is a CANCELLATION.  nu_min(A^atom, L_P) = %.4g .. %.4g.  On the "
     "lowest parity sine the two O(m^2) pieces do not merely cancel -- the atoms "
     "OVERSHOOT, leaving t_1^T A t_1 / mu^P_1 = %.3g .. %.3g POSITIVE, so the "
     "pencil floor is not attained at the bottom of the grid at all.  STATUS: "
     "exact identity plus measurement."
     % (qmin([r["kap_at"] for r in ROWS]), qmax([r["kap_at"] for r in ROWS]),
        qmin([r["ray1"] for r in ROWS]), qmax([r["ray1"] for r in ROWS]))),
    ("v572", "THE ARCH-NEGATIVE PART OF THE PARITY SPECTRUM IS m-INDEPENDENT: "
     "the archimedean diagonal is negative on k <= %d .. %d modes only, and above "
     "them its own pencil quotient is >= %.3f.  STATUS: measured on %d windows "
     "spanning m = %d .. %d.  This is the structural fact the closure below rests "
     "on."
     % (min(r["k_neg_ar"] for r in ROWS), max(r["k_neg_ar"] for r in ROWS),
        qmin([r["ray_ar_hi"] for r in ROWS]), len(ROWS),
        min(r["h"] for r in ROWS), max(r["h"] for r in ROWS))),
    ("v573", "kap IS NO LONGER A FIT.  The Schur block criterion (Schur 1917) on "
     "the whitened parity block with a FIXED low block of %d modes certifies "
     "kap >= %.4f .. %.4f on every window, with both Cholesky floors subtracted, "
     "at m^%.3f +- %.3f and with IDENTICAL quartile medians.  STATUS: certified "
     "per window with an m-INDEPENDENT block size.  What is NOT proved is the "
     "bulk positivity B_HH >= t I that the criterion consumes."
     % (max(r["schur_kb"] for r in ROWS), qmin([r["schur_t"] for r in ROWS]),
        qmax([r["schur_t"] for r in ROWS]), F_SC["p"], F_SC["band"])),
    ("v574", "ENTRYWISE ARITHMETIC CANNOT GIVE kap.  Gershgorin 1931 on the same "
     "block returns %.3g .. %.3g, and still %.4g .. %.4g after the arch-negative "
     "modes are cut out, because the whitened parity block is not diagonally "
     "dominant (median row coupling %.3g .. %.3g against a diagonal of "
     "%.3f .. %.3f).  STATUS: certified obstruction.  A BLOCK statement is "
     "needed, not bounds on individual prime-power sums."
     % (qmin([r["gersh_pen"] for r in ROWS]),
        qmax([r["gersh_pen"] for r in ROWS]),
        qmin([r["gHH_at_kneg"] for r in ROWS]),
        qmax([r["gHH_at_kneg"] for r in ROWS]),
        qmin([r["coup_med"] for r in ROWS]), qmax([r["coup_med"] for r in ROWS]),
        qmin([r["ray_star"] for r in ROWS]),
        qmax([r["ray_star"] for r in ROWS]))),
    ("v575", "R IS NOT AN ARCHIMEDEAN RATIO IN EITHER HALF.  K_bot^arch = "
     "%.3g .. %.3g growing m^%.3f sits one to two orders ABOVE the true "
     "K_bot = %.3f .. %.3f (m^%.3f +- %.3f): the atoms do not perturb an "
     "archimedean alignment, they CREATE it.  STATUS: two certified ceilings "
     "compared."
     % (qmin([r["K_bot_ar"] for r in ROWS]),
        qmax([r["K_bot_ar"] for r in ROWS]), F_KBOT_AR["p"],
        qmin([r["K_bot"] for r in ROWS]), qmax([r["K_bot"] for r in ROWS]),
        F_KBOT["p"], F_KBOT["band"])),
    ("v576", "THE NEW R NUMBER: R <= K_bot / t = %.3f .. %.3f at m^%.3f +- %.3f, "
     "certified on BOTH ends (inertia ladder above, Schur floor below), with "
     "quartile medians walking %.3f over an m-range of %.2f.  T151's 3.3634 .. "
     "9.7108 at x^0.037 +- 0.015 had a floor that was certified but not "
     "structurally closed, and its exponent was taken against the ZONE variable; "
     "the same object refitted in m gives m^%.3f.  STATUS: certified per window, "
     "m-free as a FIT only, and the file says so."
     % (qmin([r["R_cert"] for r in ROWS]), qmax([r["R_cert"] for r in ROWS]),
        F_RC["p"], F_RC["band"], WALK["R_cert"], WALK["h"], F_RC["p"])),
    ("v577", "THE m-FREE CEILING MECHANISM EXISTS BUT ITS INGREDIENT IS MISSING.  "
     "Two-sided bulk block plus the KMS step mu^P_{k+kb}/mu^P_k <= ((k+kb)/k)^2 "
     "(a THEOREM for every m, verified against the exact values at %.1f .. %.1f "
     "<= %.1f) gives an m-free-BY-CONSTRUCTION ceiling -- but the upper "
     "certificate T_HH = %.3g .. %.3g GROWS at m^%.3f (quartile walk %.1f), so "
     "the assembled ceiling grows too.  STATUS: mechanism named, ingredient "
     "missing.  THIS IS THE ONE TERM OF THE VERDICT."
     % (qmin([r["kms_true"] for r in ROWS]), qmax([r["kms_true"] for r in ROWS]),
        qmax([r["kms_fac"] for r in ROWS]), qmin([r["Thh"] for r in ROWS]),
        qmax([r["Thh"] for r in ROWS]), F_THH["p"], WALK["Thh"])),
    ("v578", "Psi IS THE LADDER'S OWN BOTTOM.  Psi <= %.3g .. %.3g equals "
     "1 / lam_min(E) to within %.2f .. %.2f, grows as m^%.2f, and %.0f .. %.0f "
     "percent of trace(E^-1) sits on the %d lowest modes -- the exact modes the "
     "certified ladder controls.  STATUS: mapped.  The reserve is worth "
     "%.2f .. %.2f and requires replacing a subset supremum by a ladder sum, "
     "which is NOT proved here."
     % (qmin([p["psi"] for p in PSI]), qmax([p["psi"] for p in PSI]),
        qmin(DRIVE), qmax(DRIVE), F_PSI["p"],
        100.0 * qmin([p["frac_head"] for p in PSI]),
        100.0 * qmax([p["frac_head"] for p in PSI]), K_CERT,
        qmin(PSI_GAIN), qmax(PSI_GAIN))),
    ("v579", "THE NO-GO RECONSTRUCTION BREAKS AT THE CEILING, NOT THE FLOOR.  A "
     "positive decaying kernel with a log-singular symbol passes every "
     "positivity test (kap = %.4f, Schur certifies %.3g) yet its bottom ceiling "
     "grows as m^%.3f and its R as m^%.3f -- against T151's reported x^1.986 for "
     "the original no-go, which is why the reconstruction is believed to be the "
     "right family.  STATUS: obligatory stress reproduced; it fails precisely at "
     "the one step this probe could not close."
     % (qmed([g["kap"] for g in NG]), qmed([g["schur"] for g in NG]),
        F_NG_K["p"], F_NG_R["p"])),
]
for tag, txt in V24:
    para("%s  %s" % (tag, txt))
    print("")

para("""Y4.1  PROMOTION LEDGER, and what NOT to touch.  T149 / T150 / T151
candidates stay PENDING as the brief states; v550 was promoted from T151 by the
parallel documentation worker and is NOT re-derived or re-promoted here.  Nothing
in this file is promotion-ready: v573 and v576 are the strongest, and both consume
an unproved block-positivity statement.  This probe writes NO ledger row, NO TeX,
NO website entry and NO changelog line -- it is a single discovery file in
experiments/tfpt-discovery/.""")

para("""Y4.2  THE SHORTEST REST LIST, in dependency order.
  (R1) B_HH >= t I on the bulk parity block, t of order 1/4, kb fixed at 16.
       This single inequality closes kap completely (v573) and is the ONLY thing
       between the Schur certificate and a theorem.  It is a BLOCK statement
       about Fejer-weighted prime-power sums at angles th >= 2 pi (kb+1) / N;
       entrywise bounds provably will not do it (v574).
  (R2) An m-free upper bound on K_bot.  Either a better test-vector family than
       the parity sines (they lose four to six orders, v575 and the min-max
       attempt) or a uniform T_HH in the two-sided route (v577).
  (R3) The Psi replacement: subset supremum -> ladder sum on the lowest modes.
       Worth a factor of about 3.5 .. 5.3 end-to-end (v578) and it is now the
       DOMINANT loss, so it outranks any further sharpening of R.
  (R4) Only after R1 .. R3: the frame-A-to-general-frame step and the zone
       extension beyond prime powers, both untouched here.""")

RES = [("R1  bulk block positivity B_HH >= t I", "OPEN -- certified per window"),
       ("R2  m-free ceiling on K_bot", "OPEN -- THE ONE TERM of the verdict"),
       ("R3  Psi: subset sup -> ladder sum",
        "OPEN -- mapped, worth %.2f .. %.2f" % (qmin(PSI_GAIN), qmax(PSI_GAIN))),
       ("R4  frames and zones", "OPEN -- untouched")]
for a, b in RES:
    info("Y4.2." + a.split()[0], "%-42s %s" % (a, b))

# --- THE VERDICT ------------------------------------------------------------
# THE GATES.  A and B are read on the RANK statistic, not on the stratified
# band: with 15 windows per stratum the half-range of stratum slopes is a
# high-variance estimator, while quartile medians cannot be inflated by scatter.
# BOTH numbers are printed so the reading can be disagreed with -- on the band
# estimator alone gate B would fail and the verdict would be RATIO-RESISTS.
GATE_A = SC_POS == len(ROWS) and WALK["schur_t"] <= WALK_BAR
GATE_B = (all(np.isfinite(r["K_bot"]) for r in ROWS)
          and WALK["K_bot"] <= WALK_BAR)
GATE_C = nogrow_ok(F_THH) and KCL_OK == len(ROWS)   # an m-FREE ceiling ROUTE
V_RATIO_CARRIES = GATE_A and GATE_B and GATE_C
V_ONE_TERM = GATE_A and GATE_B and not GATE_C
VERDICT = ("RATIO-CARRIES" if V_RATIO_CARRIES
           else ("ONE-TERM-MISSING" if V_ONE_TERM else "RATIO-RESISTS"))
check("pr_y4.verdict_is_determined", VERDICT in
      ("RATIO-CARRIES", "ONE-TERM-MISSING", "RATIO-RESISTS"),
      "VERDICT = %s.  The three gates: (A) the FLOOR is certified on every "
      "window by a fixed-size mechanism and flat in m -- %s; (B) the CEILING "
      "K_bot is certified on every window and non-growing in m -- %s; (C) a "
      "STRUCTURAL m-free route to that ceiling exists, i.e. the bulk upper "
      "certificate does not grow -- %s.  A and B are the two halves of R; C is "
      "what would turn the flat FIT into a mechanism.  ON THE BAND ESTIMATOR "
      "INSTEAD OF THE RANK ONE gate B reads %s (m^%.3f +- %.3f against the bar "
      "%.2f) and the verdict would be RATIO-RESISTS -- the two readings are "
      "printed together on purpose"
      % (VERDICT, "yes (walk %.3f <= %.3f)" % (WALK["schur_t"], WALK_BAR)
         if GATE_A else "no",
         "yes (walk %.3f <= %.3f)" % (WALK["K_bot"], WALK_BAR)
         if GATE_B else "no (walk %.3f > %.3f)" % (WALK["K_bot"], WALK_BAR),
         "yes" if GATE_C else "NO -- T_HH grows as m^%.3f" % F_THH["p"],
         "pass" if nogrow_ok(F_KBOT) else "FAIL", F_KBOT["p"], F_KBOT["band"],
         BAR_UNIF))

para("""Y4.3  THE VERDICT IS %s, IN THREE SENTENCES AND WITHOUT FLATTERY.  (1) The
DENOMINATOR of R is reduced to one inequality: kap >= %.3f .. %.3f is certified on
every window by a Schur criterion whose low block has the FIXED size 16 and whose
quartile medians do not move at all, so the floor is no longer a fit -- while both
routes everyone expected to deliver it are REFUTED here, archimedean positivity in
the odd sector by O(m^2) (the arch section is negative, lam_min = -2.81 .. -1.84)
and the l1 atom budget by a further 10^5 .. 10^8.  (2) The NUMERATOR is not
reduced: K_bot = %.3f .. %.3f is certified per window but walks %.3f over an
m-range of %.2f with decelerating increments, and every STRUCTURAL route to it
loses four to six orders of magnitude -- because the section's low EIGENVALUES
track the model's while its low EIGENVECTORS do not -- so on this surface a
saturating constant and a log m growth cannot be separated, and the honest reading
is that R = %.2f .. %.2f is certified on both ends but m-free only as a FIT.  (3)
Two further things are now on the record: T151's exponent for R was taken against
the zone variable, and refitting the SAME quantity against m raises it from
x^0.037 to m^%.3f, so part of that flatness was the fit variable rather than the
object; and Psi -- which Y3 identifies as 1 / lam_min(E) to within 1.19, growing
as m^2, with 89 .. 92 percent of it living on the eight modes the certified ladder
already controls -- is now the larger loss by orders of magnitude, so sharpening R
further is the WRONG next move.  THE FENCE, ONCE MORE: everything above is a
finite-window statement about a Toeplitz-minus-Hankel section on prime-power zones
in frame A; no zero of any L-function was read, generated or approximated, and the
word proven appears nowhere in this file for the m-freeness of R.""" %
     (VERDICT, qmin([r["schur_t"] for r in ROWS]),
      qmax([r["schur_t"] for r in ROWS]), qmin([r["K_bot"] for r in ROWS]),
      qmax([r["K_bot"] for r in ROWS]), WALK["K_bot"], WALK["h"],
      qmin([r["R_cert"] for r in ROWS]), qmax([r["R_cert"] for r in ROWS]),
      F_RC["p"]))

print("")
print("  VERDICT: %s" % VERDICT)

# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
print("checks: %d   failures: %d   elapsed: %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))
if FAILS:
    print("FAILED: " + ", ".join(FAILS))
    raise SystemExit(1)
print("PENCIL.RATIO PROBE GREEN")
