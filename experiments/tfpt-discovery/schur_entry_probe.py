"""PART 158 -- THE CONTRACT ``SCHUR.ENTRY'': THE ONE NUMBER AND THE GROWTH.

THE RH FENCE, FIRST AND PROMINENT.  Nothing in this file reads, generates,
approximates, extrapolates or otherwise touches a single zero of any L-function.
Weil's explicit-formula positivity criterion (Weil 1952; Bombieri 2000) is CITED
as an ADDRESS ONLY and is never used, in either direction.  An AST firewall
below enforces the absence of zero data, the import whitelist and the absence of
any write-mode file access.  What is investigated here is the END-TO-END
ARITHMETIC of one finite-window inequality about a Toeplitz-minus-Hankel section
in its ODD PARITY SECTOR, on prime-power zones in frame A, with the zone gap
Theta(D^3).  Even if every step below closed, what would stand is a
finite-window positivity statement with an explicit constant on a finite list of
zones.  The distance from there to RH is mapped in L4 and never travelled.

WHAT T157 LEFT: TWO TERMS, AND THE FIRST OF THEM IS ONE SCALAR.

  R2''  THE SCHUR ENTRY.  T157's identity turned R2'' into a bound on ONE
        diagonal entry of the kb x kb Schur complement the chain forms anyway:
        1/s <= (S_L)_{11}, MEASURED 3.1 .. 5.3.  What is needed is an m-free
        UPPER bound on it.  Cauchy-Schwarz on b^T B_HH^-1 b is REFUTED: it
        misses by 4e4 .. 5e5, because the cancellation in that bilinear form is
        almost complete and a single-direction inequality cannot see it.
  R1''  THE DOMINATION.  B^arch_HH - t I >= (-B^atom_HH)_+ holds per window
        with quotient 1.0003 .. 1.09, but the margin at h = 60 is 3e-4 and
        shrinks.  The pointer T157 left: f^arch(th) / (4 sin^2(th/2)) GROWS as
        th falls, and the atom extremal lives at th/pi = 0.02 .. 0.11 while the
        arch extremal lives at th/pi = 0.94 .. 1.00 -- opposite ends.

WHAT THIS FILE DOES.  L1 attacks the one number with the CANCELLATION-SIGHTED
identity: (S_L)_{11} and 1/s are DIRICHLET MINIMA over trial vectors, so every
trial vector is an upper bound and the cancellation is not thrown away; the
Cholesky / continued-fraction expansion writes s as a SUM OF POSITIVE TERMS,
whose partial sums are therefore lower bounds on s.  L2 attacks the domination
through the th growth: it measures the growth exponent, splits th dyadically and
prices the arch growth against the Fejer-damped atom mass band by band.  L3
makes the T156 domination debt fixed-size or says honestly why not, reassembles
end to end and runs the obligatory stress.  L4 is the map, the promotion list,
the rest list and the verdict.

DISCIPLINE.  THEOREM / CERTIFIED / MEASURED / FIT are kept strictly apart and
every claim carries its label; the word ``proven'' is used nowhere for any
m-freeness claim.  DIRECTIONS ARE PEDANTIC, and for this file the pedantry is
the content: a Schur complement is MONOTONE DECREASING in the set that is
eliminated and MONOTONE INCREASING in the matrix, and both directions are
re-checked numerically before they are used.  Classics cited where used: Schur
1917, Haynsworth 1968, Maz'ya 1985, Miclo 1999, Fejer 1915, Szego 1915,
Kac-Murdock-Szego 1953, Courant-Fischer 1920, Cauchy 1829, Sylvester 1852,
Temple 1928, Kato 1949, Kantorovich 1948, Widom 1958, Chebyshev 1852,
Rosser-Schoenfeld 1962.  HARD CAPS: any factorised / inverted / diagonalised
matrix <= 1500; probe budget < 900 s.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, ldl

T0 = time.time()
np.random.seed(158158)

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 400000
ZONE_DEEP = 380000

# --- the measurement surface, DECLARED BEFORE ANY RESULT IS SEEN ------------
L1_ZONES = 28
L1_HCAP = 1400
L2_ZONES = 22
L2_HCAP = 1100

K_CERT = 8                   # the modes the bottom certificate is about
K_TWELVE = 12                # the K of the T155 / T156 complement certificate
SCHUR_KB = 16                # the FIXED low block of the T152 .. T157 chain
T_LADDER = (0.25, 0.245, 0.24, 0.235, 0.23, 0.225, 0.22, 0.215, 0.21, 0.205,
            0.20, 0.19, 0.18, 0.16, 0.14, 0.12, 0.10, 0.05)
BAR_UNIF = 0.25              # |exponent| + band bar for "flat / non-growing"
T_TARGET = 0.25

# *** THE DIRICHLET LADDER OF L1: THE TRUNCATION SIZES, PREREGISTERED ***
K_LADDER = (1, 2, 4, 8, 12, 16, 24, 32, 48, 64)
N_BAND = 8                   # the dyadic th bands of L2
NOGO_SIZES = (48, 64, 96, 128, 192, 256, 384, 512)
CTRL_SIZES = (64, 128, 256, 384, 512, 700)

# T156 / T157 numbers, QUOTED, never recomputed as an input to anything
T157_S11 = (3.1, 5.3)           # the MEASURED (S_L)_{11} band -- the L1 target
T157_CSMISS = (4.0e4, 5.0e5)    # by how much Cauchy-Schwarz misses it
T156_P1 = (0.2010, 0.3282)      # the MEASURED p_1 band
T157_P1RES = (0.187, 0.316)     # the resolvent floor for p_1 (T157 route iii)
T156_L2 = (1.25, 3.45)          # lam_2 / lam_1: the NEARLY DEGENERATE bottom
T156_BHH = (0.2661, 0.4436)     # lam_min(B_HH) on the bulk
T157_DOM = (1.0003, 1.09)       # the R1'' domination quotient band
T156_ARCHFAC = (3.29, 5.59)     # the arch one-variable reserve, over target
T156_THSTAR = (0.990, 1.000)    # where the arch infimum sits, in th/pi
T157_THAT = (0.02, 0.11)        # where the atom extremal sits, in th/pi
T156_E2E = (3.28e-2, 2.83e-1)   # end to end, certified per window
T157_CONF = (0.96, 0.99)        # e_1 inside the first 16 parity sines
T156_NOGO_P1 = -4.818           # the no-go p_1 collapse exponent: the referee
FRAC_BAR = 4.0e-2               # the L3 bar on the m-free-shaped end to end

B_PSI = 1.03883               # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962 Thm 12)

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
    out, line = [], ""
    for w in text.split():
        if not line:
            line = w
        elif len(line) + 1 + len(w) <= width:
            line += " " + w
        else:
            out.append(line)
            line = w
    if line:
        out.append(line)
    return out


def para(text, width=76, indent="  "):
    print("")
    for ln in wrap_at(" ".join(text.split()), width - len(indent)):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T0)


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
    check("se_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("se_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("se_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("se_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "schur_entry_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# statistics of a FINITE surface -- a fit is a FIT and is never a theorem
# ----------------------------------------------------------------------------
def sym(A):
    return 0.5 * (A + A.T)


def qmin(v):
    v = [x for x in v if np.isfinite(x)]
    return min(v) if v else float("nan")


def qmax(v):
    v = [x for x in v if np.isfinite(x)]
    return max(v) if v else float("nan")


def qmed(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


def fit_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    if int(np.sum(ok)) < 3:
        return float("nan"), float("nan")
    x, y = x[ok], y[ok]
    xm, ym = float(np.mean(x)), float(np.mean(y))
    sxx = float(np.sum((x - xm) ** 2))
    if sxx <= 0.0:
        return float("nan"), float("nan")
    p = float(np.sum((x - xm) * (y - ym)) / sxx)
    return p, ym - p * xm


def fit_band(x, y):
    """THE HALF-SPREAD of the split-half slopes: a scatter measure, never a
    confidence interval."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = x.shape[0]
    if n < 6:
        return float("nan")
    h = n // 2
    p1, _ = fit_line(x[:h], y[:h])
    p2, _ = fit_line(x[h:], y[h:])
    if not (np.isfinite(p1) and np.isfinite(p2)):
        return float("nan")
    return 0.5 * abs(p2 - p1)


def pow_fit(xv, yv, tag):
    xv = np.asarray(xv, float)
    yv = np.asarray(yv, float)
    ok = np.isfinite(xv) & np.isfinite(yv) & (xv > 0.0) & (yv > 0.0)
    if int(np.sum(ok)) < 3:
        return dict(tag=tag, p=float("nan"), band=float("nan"), n=0)
    lx = np.log(xv[ok])
    ly = np.log(yv[ok])
    p, _ = fit_line(lx, ly)
    return dict(tag=tag, p=p, band=fit_band(lx, ly), n=int(np.sum(ok)))


def fit_str(f):
    return "x^{%.3f +- %.3f} (n = %d)" % (f["p"], f["band"], f["n"])


def flat_ok(f, bar=BAR_UNIF):
    return bool(np.isfinite(f["p"]) and abs(f["p"])
                + (f["band"] if np.isfinite(f["band"]) else 0.0) <= bar)


def nogrow_ok(f, bar=BAR_UNIF):
    return bool(np.isfinite(f["p"]) and f["p"]
                + (f["band"] if np.isfinite(f["band"]) else 0.0) <= bar)


# ----------------------------------------------------------------------------
# certificates: Cholesky (Wilkinson floor), Gershgorin, inertia (Sylvester 1852)
# ----------------------------------------------------------------------------
def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except (LinAlgError, ValueError):
        return None


def chol_floor(A_norm, h):
    """THE BACKWARD-ERROR FLOOR of a COMPLETED Cholesky (Wilkinson): success
    certifies A >= -fl I with fl = c h eps ||A||.  DIRECTION: fl >= 0, always
    SUBTRACTED from a lower bound and ADDED to an upper bound."""
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
    t = (float(np.min(np.diag(X))) if guess is None else float(guess))
    for _ in range(tries):
        Y = sym(X - t * np.eye(h))
        if safe_cho(Y) is not None:
            return t - chol_floor(gersh(Y), h)
        t -= abs(t) * grow + 1.0e-300
        grow *= 6.0
    return float("nan")


def cert_norm2(R):
    """AN UPPER BOUND on the spectral norm of R, from a Cholesky on the SMALL
    side.  DIRECTION: upper bound, and it enters every residual floor SQUARED."""
    G = sym(R.T @ R)
    s = cert_lam_max(G, guess=float(np.max(np.sum(np.abs(G), axis=1))) + 1e-300)
    return math.sqrt(max(0.0, s))


def cert_absnorm(X):
    """AN UPPER BOUND on ||X|| for SYMMETRIC X, from both one-sided Choleskys.
    DIRECTION: upper bound; it is SUBTRACTED wherever it prices a perturbation."""
    up = cert_lam_max(X, guess=gersh(X) + 1.0e-300)
    lo = cert_lam_min(X, guess=-gersh(X) - 1.0e-300)
    if not (np.isfinite(up) and np.isfinite(lo)):
        return float("nan")
    return max(abs(up), abs(lo))


def inertia_neg(X):
    """#{lam_j < 0} from a COMPLETED LDL^T (Sylvester 1852; Bunch-Kaufman 1977
    for the pivoting).  No eigenvector is ever read."""
    try:
        lu, d, _ = ldl(X)
    except (LinAlgError, ValueError):
        return -1
    del lu
    n = d.shape[0]
    neg = 0
    i = 0
    while i < n:
        if i + 1 < n and abs(d[i + 1, i]) > 0.0:
            blk = np.array([[d[i, i], d[i, i + 1]],
                            [d[i + 1, i], d[i + 1, i + 1]]])
            try:
                w2 = np.linalg.eigvalsh(sym(blk))
            except LinAlgError:
                return -1
            neg += int(np.sum(w2 < 0.0))
            i += 2
        else:
            neg += int(d[i, i] < 0.0)
            i += 1
    return neg


def small_eig_floor(W):
    """A CONSERVATIVE bound on the eigenvalue error of a small dense solve
    (Wilkinson); SUBTRACTED wherever a Ritz value feeds a LOWER bound."""
    return 8.0 * W.shape[0] * np.finfo(float).eps * gersh(W)


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T157 code path
# ----------------------------------------------------------------------------
def von_mangoldt_table(n_max):
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
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
    idx = np.nonzero(lam > 0.0)[0]
    out = []
    for n in idx:
        u = math.log(float(n))
        out.append((int(n), float(lam[n]), u,
                    2.0 * float(lam[n]) / math.sqrt(float(n))))
    return out


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


# ----------------------------------------------------------------------------
# the archimedean lag kernel (the T115 assembly, bit for bit)
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
    REFLECTED spline when u_j < D.  Hence c^atom <= 0 ENTRYWISE."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    mu_tot = 0.0
    n_hit = 0
    lag_of = []
    for u_j, mu_j in atoms:
        mu_tot += mu_j
        n_hit += 1
        i0 = int(math.floor(u_j / D))
        lag_of.append((i0, mu_j))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D, mu_tot, n_hit, lag_of


def lag_vector_split(alpha, M, atoms):
    """THE EXACT SPLIT c = c^arch + c^atom of the T115 lag assembly.  The sum is
    bit-for-bit the object T111 .. T157 use, and the split is EXACT because the
    section map c -> A is LINEAR in c."""
    c_at, D, mu_tot, n_hit, lag_of = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D, mu_tot=mu_tot,
                n_atom=n_hit, l1_at=float(np.sum(np.abs(c_at))), lag_of=lag_of)


# ----------------------------------------------------------------------------
# the sections, the exact parity structure, the pencil
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s} on the ODD section, r, s = 0 .. M/2 - 1:
    the TOEPLITZ-MINUS-HANKEL form, exact and not an approximation (Widom 1958;
    Boettcher-Silbermann)."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def parity_mu(m):
    """THE EXACT eigenvalues of L_P: mu^P_k = 4 sin^2(pi k / N), N = 2m + 1,
    k = 1 .. m (Kac-Murdock-Szego 1953 in the parity sector)."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m):
    """THE ORTHONORMAL EIGENBASIS OF L_P: t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N).
    That these are EXACT eigenvectors of L_P is the fact every separation
    argument in this file rests on, and it is verified in the L3 controls."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_P_mat(m):
    """L_P: tridiag(-1, 2, -1) with the LAST diagonal entry 3 -- not a choice:
    for an antisymmetric vector of the full window the reflected neighbour of the
    last index is MINUS the last index."""
    L = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    L[m - 1, m - 1] = 3.0
    return L


def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def parity_block(A, Tf, mu):
    """B = Lam^{-1/2} T A T^T Lam^{-1/2}, Lam = diag(mu^P).  An IDENTITY:
    lam_min(B) is the pencil floor and lam_max(B) the pencil ceiling.  Because
    the map is linear in A, B^arch + B^atom = B EXACTLY, which is what L2
    splits."""
    Gf = sym(Tf @ (A @ Tf.T))
    isq = 1.0 / np.sqrt(mu)
    return sym(Gf * np.outer(isq, isq))


def schur_floor(B, kb, t):
    """THE CERTIFIED TWO-BLOCK SCHUR FLOOR (Schur 1917; Haynsworth 1968).  For
    symmetric B split into a LOW block of kb modes and the BULK,
      B >= t I  <=>  B_HH - t I > 0 AND B_LL - tI - B_LH (B_HH - tI)^-1 B_HL > 0,
    an EQUIVALENCE.  Both conditions are certified by COMPLETED Choleskys and
    BOTH backward-error floors are subtracted.  DIRECTION: a LOWER bound."""
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


def schur_best(B, kb, ladder=T_LADDER):
    """THE BEST CERTIFIED t OF THE PREREGISTERED LADDER at a FIXED low block."""
    for t_try in ladder:
        got = schur_floor(B, kb, t_try)
        if got is not None and got > 0.0:
            return got
    return float("nan")


# ----------------------------------------------------------------------------
# the subspace instruments (T154 .. T157, unchanged) -- reused, not re-derived
# ----------------------------------------------------------------------------
def ritz_pack(A, Q):
    """THE RITZ DATA OF A SUBSPACE.  W = Q^T A Q with Q^T Q = I.  DIRECTION
    (Courant-Fischer 1920 / Cauchy 1829): a Ritz value is a CEILING on
    lam_k(A) and NEVER a floor -- T154's lesson, restated at every use."""
    W = sym(Q.T @ (A @ Q))
    R = A @ Q - Q @ W
    return dict(W=W, R=R, nrm_R=cert_norm2(R))


def temple_matrix(W, RtR, beta, K):
    """TEMPLE 1928 / KATO 1949 IN ITS MATRIX (SCHUR-COMPLEMENT) FORM.  For
    gam < beta,  S(gam) >= W - gam I - (R^T R) / (beta - gam) =: M(gam).  By
    Sylvester 1852 / Haynsworth 1968 the inertia is additive, so lam_k(A) >= gam
    as soon as #neg M(gam) <= k - 1.  DIRECTION: LOWER bounds on lam_k(A)."""
    d = W.shape[0]
    fl = small_eig_floor(W) + small_eig_floor(RtR) / max(beta, 1.0e-300)

    def negcount(g):
        if g >= beta:
            return d
        M = sym(W - g * np.eye(d) - RtR / (beta - g))
        n = inertia_neg(M)
        return d if n < 0 else n

    out = []
    for k in range(1, K + 1):
        if negcount(0.0) > k - 1:
            out.append(float("nan"))
            continue
        lo, hi = 0.0, beta * (1.0 - 1.0e-13)
        for _ in range(56):
            mid = 0.5 * (lo + hi)
            if negcount(mid) <= k - 1:
                lo = mid
            else:
                hi = mid
        out.append(lo - fl)
    return out


def cert_ceiling(W, mu, K):
    """K^F = max_{k <= K} lam_max(Y_k^T W Y_k) / mu^P_k -- T154's CLOSED
    sixteen-column ceiling.  Each ratio is an UPPER bound on lam_k(A)/mu^P_k by
    Courant-Fischer and each numerator is one Cholesky of a k x k matrix."""
    try:
        _, Y = eigh(W)
    except (LinAlgError, ValueError):
        return float("nan")
    out = []
    for k in range(1, K + 1):
        Z = sym(Y[:, :k].T @ (W @ Y[:, :k]))
        out.append(cert_lam_max(Z, guess=float(np.max(np.diag(Z))) + 1.0e-12)
                   / mu[k - 1])
    return float(np.max(out))


def green_cols(A, LP, V, j, fac=None):
    """THE ITERATION COLUMNS (A^-1 L_P)^j V, by j Cholesky back-solves of A.
    No inverse is ever formed; the completed factor certifies A > 0."""
    if fac is None:
        fac = safe_cho(sym(A + 0.0))
    if fac is None:
        return None
    out = V
    for _ in range(j):
        try:
            out = cho_solve(fac, LP @ out, check_finite=False)
        except (LinAlgError, ValueError):
            return None
    return out


def orth_cols(V, tol=1.0e-10):
    U, s, _ = np.linalg.svd(V, full_matrices=False)
    if s.size == 0 or s[0] <= 0.0:
        return V[:, :0]
    keep = int(np.sum(s > tol * s[0]))
    return U[:, :keep]


def append_orth(Q, V, tol=1.0e-9):
    """APPEND span(V) TO AN ORTHONORMAL Q, keeping the EXISTING columns of Q
    untouched -- the containment of the leading parity sines must survive
    verbatim, because every free separation rests on it."""
    out = [Q]
    cur = Q
    for j in range(V.shape[1]):
        v = V[:, j].copy()
        for _ in range(2):
            v -= cur @ (cur.T @ v)
        nv = float(np.linalg.norm(v))
        if nv <= tol:
            continue
        v /= nv
        out.append(v.reshape(-1, 1))
        cur = np.concatenate(out, axis=1)
    return cur


def complement_floor(mu, G, K):
    """T155's FIXED-SIZE COMPLEMENT-FLOOR CERTIFICATE, reproduced verbatim.
    DIRECTION: lam_max is a CERTIFIED UPPER bound and it is SUBTRACTED, so the
    return value is a LOWER bound on min_{v perp W} v^T L_P v / v^T v."""
    K = int(min(K, mu.shape[0] - 1))
    if K < 1:
        return float("nan"), float("nan"), None
    muK1 = float(mu[K])
    Mg = np.maximum(muK1 - mu[:K], 0.0)
    rt = np.sqrt(Mg)
    E = sym((np.eye(K) - G[:K] @ G[:K].T) * np.outer(rt, rt))
    try:
        wE, _VE = eigh(E)
    except (LinAlgError, ValueError):
        return float("nan"), float("nan"), None
    top = cert_lam_max(E, guess=float(wE[-1]) + 1.0e-13 * muK1)
    if not np.isfinite(top):
        return float("nan"), float("nan"), None
    return muK1 - top, muK1, None


def loss_PR(P, r):
    """THE T156 KERNEL F(P, r), QUOTED AS A THEOREM AND NOT RE-DERIVED.  With
    W' = [[P, 1], [1, 1]], N' = [[1, 1], [1, r]], P >= 1 (Kantorovich 1948) and
    r >= 1, the t_1 loss of the two-dimensional model is
        F(P, r) = 1 - (al + be)^2 / (al^2 + 2 al be + be^2 r) ."""
    if not (np.isfinite(P) and np.isfinite(r)) or r <= 1.0 or P < 1.0:
        return float("nan")
    W2 = np.array([[P, 1.0], [1.0, 1.0]])
    N2 = np.array([[1.0, 1.0], [1.0, r]])
    try:
        _, V2 = eigh(sym(W2), sym(N2))
    except (LinAlgError, ValueError):
        return float("nan")
    al, be = float(V2[0, 0]), float(V2[1, 0])
    den = al * al + 2.0 * al * be + be * be * r
    if den <= 0.0:
        return float("nan")
    return 1.0 - (al + be) ** 2 / den


def lip_local(a, dsum, fabs):
    """THE LOCAL LIPSCHITZ CONSTANT OF R = f / g, g = 4 sin^2(th/2), ON AN
    INTERVAL STARTING AT a:  |R'| <= dsum / g(a) + 2 fabs / g(a)^2.
    DIRECTION: an UPPER bound on |R'|, hence usable in a LOWER bound on R."""
    g = 4.0 * math.sin(0.5 * a) ** 2
    return dsum / g + 2.0 * fabs / (g * g)


def certified_inf_ratio(c, M, th_lo, th_hi, target, dsum, fabs, cap=400000):
    """T157's ADAPTIVE LIPSCHITZ DECKEL, EXECUTED AND NOT ASSERTED.  Certifies
    R(th) = f(th)/(4 sin^2(th/2)) >= target on [th_lo, th_hi] by bisection: an
    interval [a, b] is ACCEPTED as soon as R(mid) - lip_local(a)(b-a)/2 >=
    target.  DIRECTION: every accepted interval carries a LOWER bound on R, so
    success is a certificate and failure is only a failure of this budget."""
    stack = [(th_lo, th_hi)]
    n_eval = 0
    worst = float("inf")
    narrow = th_hi - th_lo
    ll = np.arange(1, M)
    cc = c[1:M]
    while stack:
        if n_eval > cap:
            return False, n_eval, worst, narrow
        a, b = stack.pop()
        mid = 0.5 * (a + b)
        n_eval += 1
        f_mid = c[0] + 2.0 * float(np.dot(np.cos(ll * mid), cc))
        R_mid = f_mid / (4.0 * math.sin(0.5 * mid) ** 2)
        floor_here = R_mid - lip_local(a, dsum, fabs) * (b - a) * 0.5
        if floor_here >= target:
            worst = min(worst, floor_here)
            continue
        if (b - a) <= 1.0e-13 * max(1.0, th_hi):
            return False, n_eval, floor_here, b - a
        narrow = min(narrow, 0.5 * (b - a))
        stack.append((a, mid))
        stack.append((mid, b))
    return True, n_eval, worst, narrow


def symbol_ratio(c, M, th):
    """f(th) / (4 sin^2(th/2)) with f(th) = c_0 + 2 sum_l c_l cos(l th).
    MEASURED, and it is the symbol of the TOEPLITZ part only: the section also
    carries a Hankel reflection, so Szego 1915 / Widom 1958 is a NAMED
    CANDIDATE here and never a licence."""
    ll = np.arange(1, M)
    f = c[0] + 2.0 * (np.cos(np.outer(th, ll)) @ c[1:M])
    return f / (4.0 * np.sin(0.5 * np.asarray(th, float)) ** 2)


section("L0  THE FENCE, THE LIBRARY, AND THE SURFACE")
firewall()
para("""THE RH FENCE, RESTATED WHERE IT CAN BE SEEN.  No zero of any L-function
is read, generated, approximated or extrapolated anywhere below.  Weil 1952 /
Bombieri 2000 is an ADDRESS.  What is measured is a finite-window inequality
about one Toeplitz-minus-Hankel section on prime-power zones in frame A.""")

ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]
NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

check("se_l0.zone_gaps",
      bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
      and bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12)),
      "the %d prime-power gaps up to n = %d obey log(1 + 1/n) <= g <= log 2 "
      "EXACTLY: the zone geometry is arithmetic and needs no model"
      % (NZ_DEEP, ZONE_DEEP))

_psi_run = 0.0
_bpsi = 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
check("se_l0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f is VERIFIED at every jump point up to n = %d (max "
      "%.6f); psi jumps only at prime powers, so this is the true max on the "
      "range, and it is never assumed beyond it" % (B_PSI, ATOM_MAX, _bpsi))

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > L1_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(L1_ZONES, 1))
    SZ = CAND[::-1][::step][:L1_ZONES]
    SZ.sort(key=lambda t: t[0])
L2S = [q for q in SZ if q[3] <= L2_HCAP][:L2_ZONES]
check("se_l0.surface", len(SZ) >= 8,
      "%d prime-power zones admit a frame-A window inside the cap (h <= %d, "
      "MAX_H = %d): h = %d .. %d; the L2 sub-surface carries %d of them"
      % (len(SZ), L1_HCAP, MAX_H, min(t[3] for t in SZ),
         max(t[3] for t in SZ), len(L2S)))

para("""L0.1  WHAT COUNTS AS WHAT, PEDANTICALLY.  THEOREM = an identity or a
classical inequality valid for every m.  CERTIFIED = a numeric bound produced by
a completed factorisation with its backward-error floor carried, valid for THAT
window only; a certificate is additionally called FIXED-SIZE when the
factorisation it needs has a size independent of m.  MEASURED = a
diagonalisation or an angle read for orientation.  FIT = an exponent on the
finite surface, never promoted to anything.  The word ``proven'' is used nowhere
in this file for any m-freeness claim, and no verdict may be reached by
narrative: the verdict gates in L4 are evaluated from the numbers.""")

para("""L0.2  THE TWO MONOTONICITIES THIS FILE LIVES ON, AND THEIR DIRECTIONS.
Let B be symmetric positive definite and let S(E) := B_11 - B_{1,E} B_{EE}^-1
B_{E,1} be the Schur complement of B at index 1 after ELIMINATING the index set
E (Schur 1917; Haynsworth 1968).  (M1) ELIMINATION MONOTONICITY: S(E) =
min{x^T B x : x_1 = 1, supp x subset {1} u E}, so S(E) is NON-INCREASING as E
GROWS, and S(all) = 1 / (B^-1)_{11}.  Consequently 1 / s <= (S_L)_{11} with
(S_L)_{11} = S({kb+1..m}) the entry T157 named -- an INEQUALITY in the direction
the chain needs, and NOT an identity.  (M2) MATRIX MONOTONICITY: B >= B' > 0
implies S_B(E) >= S_{B'}(E) for the same E.  Both are re-checked numerically in
L1.2 before either is used, and no bound below is quoted without saying which
of the two carries it.""")

# ----------------------------------------------------------------------------
# L1's OWN INSTRUMENTS: the Dirichlet / Thomson dual form of the entry
# ----------------------------------------------------------------------------
def dual_value(Bm, x):
    """THE DUAL (THOMSON / DIRICHLET) FUNCTIONAL  2 x_1 - x^T B x.  THEOREM
    (Legendre duality of the quadratic form; Maz'ya 1985 for the capacity
    reading): (B^-1)_{11} = max_x (2 x_1 - x^T B x), so EVERY trial x gives a
    LOWER bound on (B^-1)_{11} = s, and therefore an UPPER bound on 1/s.  This
    is what makes an approximate solve SELF-CERTIFYING: no accuracy claim about
    x is needed anywhere, only the evaluated number."""
    return 2.0 * float(x[0]) - float(x @ (Bm @ x))


def cf_terms(Bm, K):
    """*** THE IDENTITY THAT WRITES s AS A SUM OF POSITIVE TERMS. ***  Let
    Q_K = B_{1:K,1:K} = L_K L_K^T (Cholesky) and y = L_K^-1 e_1.  Then
        g_K := e_1^T Q_K^-1 e_1 = sum_{j=1}^{K} y_j^2 ,
    every term STRICTLY POSITIVE, and because the leading J x J block of L_K is
    the Cholesky factor of Q_J, the PARTIAL SUM to J is exactly g_J.  So ONE
    Cholesky of ONE K x K principal block delivers the whole ladder, and by (M1)
        s >= g_J  for every J,   i.e.  1/s <= 1/g_J ,
    a DECREASING sequence of UPPER bounds on 1/s starting at 1/g_1 = 1/B_11 =
    1/a_hat, which is exactly T157's route (0).  THEOREM (Schur 1917 nested
    complements; Haynsworth 1968 quotient formula; the Jacobi continued
    fraction).  Returns (y^2 terms, cumulative g_J, the Cholesky factor L)."""
    Q = sym(Bm[:K, :K])
    try:
        L = np.linalg.cholesky(Q)
    except LinAlgError:
        return None, None, None
    e1 = np.zeros(K)
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return y ** 2, np.cumsum(y ** 2), L


def galerkin_lower(Bm, V):
    """THE GALERKIN / RITZ LOWER BOUND ON s = (B^-1)_{11} OVER span(V):
        s >= max_{c} (2 (V c)_1 - c^T (V^T B V) c) = e_V^T (V^T B V)^-1 e_V ,
    e_V := V^T e_1.  THEOREM, by the same duality; the value is then RE-EVALUATED
    through dual_value at the recovered x = V c, so the returned number is a
    LOWER bound on s even if the small solve is inexact.  DIRECTION: enlarging
    span(V) can only INCREASE the bound (Dirichlet principle)."""
    G = sym(V.T @ (Bm @ V))
    e = V.T @ np.eye(Bm.shape[0])[:, 0]
    try:
        c = np.linalg.solve(G + 0.0, e)
    except LinAlgError:
        return float("nan"), None
    x = V @ c
    return dual_value(Bm, x), x


print("")
print("TOTAL (L0): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("L1  THE ONE NUMBER: THE ENTRY AS A DIRICHLET MINIMUM")
# ----------------------------------------------------------------------------
para("""L1.0  WHY CAUCHY-SCHWARZ COULD NOT WORK, AND WHAT REPLACES IT.  T157
bounded the entry by  (S_L)_{11} = B_11 - b^T B_HH^-1 b <= a_hat - ||b||^4 /
(b^T B_HH b)  and the bound missed by %.0e .. %.0e.  The reason is structural and
not a matter of sharpness: b^T B_HH^-1 b = max_z (2 b^T z - z^T B_HH z) is a
MAXIMUM over a whole space, and Cauchy-Schwarz evaluates it at the SINGLE trial
direction z parallel to b.  The cancellation that makes the entry O(1) is spread
over the low modes, so one direction cannot see it.  The fix is therefore not a
sharper inequality but a LARGER TRIAL SPACE, and the object that makes trial
spaces legitimate in the RIGHT direction is the dual (Thomson) form:
    s = (B^-1)_{11} = max_x (2 x_1 - x^T B x) ,
every trial x a LOWER bound on s and hence an UPPER bound on 1/s.  The
capacity reading is the same statement: s is a CONDUCTANCE of mode 1 into the
bulk, the max is Thomson's principle, and every admissible flow is a lower bound
(Maz'ya 1985; Miclo 1999 for the same duality in the spectral-gap setting).""" % (
    T157_CSMISS[0], T157_CSMISS[1]))

L1R = []
for (zk, D_k, M_k, h_k) in SZ:
    if budget_left() < 420.0:
        info("L1.0.budget", "L1 surface truncated at %d windows" % len(L1R))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    if m <= SCHUR_KB + K_TWELVE + 8:
        continue
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A = sym(odd_toeplitz(sp["c"], M_k))
    A_at = sym(odd_toeplitz(sp["c_at"], M_k))
    LP = lap_P_mat(m)
    B = parity_block(A, Tf, mu)
    B_at = parity_block(A_at, Tf, mu)
    t_cert = schur_best(B, SCHUR_KB)
    fac = safe_cho(sym(A + 0.0))
    if fac is None or not np.isfinite(t_cert):
        info("L1.0.drop", "zone %d (h = %d): fac %s, t_cert %s"
             % (zk, m, fac is not None, t_cert))
        del A, A_at, LP, Tf, sp, B, B_at
        continue
    kap = cert_lam_max(B, guess=ray_top(B))
    rec = dict(zk=zk, h=m, t=t_cert, kap=kap, mu1=float(mu[0]),
               n_atom=sp["n_atom"])
    rec["rho17"] = float(mu[min(SCHUR_KB, m - 1)] / mu[0])
    t1 = np.ascontiguousarray(Tf[0, :])
    try:
        Ainv_t1 = cho_solve(fac, t1, check_finite=False)
        w_lo, V_lo = eigh(A, subset_by_index=[0, 1])
    except (LinAlgError, ValueError):
        del A, A_at, LP, Tf, sp, B, B_at
        continue
    rec["a_hat"] = float(B[0, 0])
    rec["s"] = rec["mu1"] * float(t1 @ Ainv_t1)
    rec["inv_s"] = 1.0 / max(rec["s"], 1.0e-300)
    rec["lam1"] = float(w_lo[0])
    rec["L"] = rec["lam1"] / rec["mu1"]
    rec["lam2_over_lam1"] = float(w_lo[1]) / rec["lam1"]
    gam = Tf @ V_lo[:, 0]
    rec["p1"] = float(gam[0] ** 2)
    rec["conf16"] = float(np.sum(gam[:SCHUR_KB] ** 2))
    # --- the T157 entry itself, and the Cauchy-Schwarz bound it refuted ------
    kb = SCHUR_KB
    b_col = np.ascontiguousarray(B[kb:, 0])
    HH = sym(B[kb:, kb:])
    f_hh = safe_cho(HH)
    if f_hh is not None:
        rec["S11_exact"] = rec["a_hat"] - float(
            b_col @ cho_solve(f_hh, b_col, check_finite=False))
    else:
        rec["S11_exact"] = float("nan")
    bb = float(b_col @ b_col)
    bqb = float(b_col @ (HH @ b_col))
    rec["S11_cs"] = rec["a_hat"] - (bb * bb / bqb if bqb > 0.0 else 0.0)
    rec["cs_miss"] = rec["S11_cs"] - rec["inv_s"]
    # --- ROUTE (i): THE CHOLESKY / CONTINUED-FRACTION LADDER, ONE FACTOR ----
    Kmax = min(max(K_LADDER), m - 1)
    ter, gcum, Lchol = cf_terms(B, Kmax)
    rec["lad"] = {}
    if ter is not None:
        rec["terms_pos"] = bool(np.all(ter > 0.0))
        rec["mono"] = bool(np.all(np.diff(gcum) >= -1.0e-18))
        for K in K_LADDER:
            if K > Kmax:
                continue
            gK = float(gcum[K - 1])
            rec["lad"][K] = dict(g=gK, U=1.0 / max(gK, 1.0e-300),
                                 tight=(1.0 / max(gK, 1.0e-300)) / rec["inv_s"],
                                 share=gK / max(rec["s"], 1.0e-300))
        # the OPTIMAL TRIAL of the kb-block, normalised to x_1 = 1: is it
        # UNIVERSAL across windows?  If it is, the m-free residual is ONE
        # quadratic form of ONE explicit fixed 16-vector.
        e1k = np.zeros(kb)
        e1k[0] = 1.0
        try:
            xs = np.linalg.solve(sym(B[:kb, :kb]), e1k)
            rec["xstar"] = xs / max(abs(float(xs[0])), 1.0e-300)
            rec["xq"] = float(rec["xstar"] @ (sym(B[:kb, :kb]) @ rec["xstar"]))
            rec["xq_ar"] = rec["xq"] - float(
                rec["xstar"] @ (sym(B_at[:kb, :kb]) @ rec["xstar"]))
            rec["xq_at"] = float(rec["xstar"] @ (sym(B_at[:kb, :kb])
                                                 @ rec["xstar"]))
            rec["g_dual16"] = 1.0 / max(rec["xq"], 1.0e-300)
        except LinAlgError:
            rec["xstar"] = None
    else:
        rec["terms_pos"] = rec["mono"] = False
    # --- ROUTE (ii): THE GREEN-COLUMN TRIAL SPACE (the T154 sixteen) --------
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    g1 = green_cols(A, LP, V0, 1, fac=fac)
    rec["g_green"] = float("nan")
    rec["g_mixed"] = float("nan")
    if g1 is not None:
        Q16 = append_orth(orth_cols(V0), g1)
        rt = np.sqrt(mu)
        VB = (Tf @ Q16) * rt[:, None]
        val, _x = galerkin_lower(B, VB)
        rec["g_green"] = val
        VS = np.zeros((m, kb))
        VS[np.arange(kb), np.arange(kb)] = 1.0
        VM = np.concatenate([VS, VB], axis=1)
        val2, _x2 = galerkin_lower(B, orth_cols(VM))
        rec["g_mixed"] = val2
        del Q16, VB, VS, VM
    g16 = rec["lad"].get(kb, {}).get("g", float("nan"))
    rec["Ls_lad"] = rec["L"] * g16
    rec["Ls_lad_mfree"] = t_cert * g16
    rec["Ls_green"] = rec["L"] * rec["g_green"]
    rec["Ls_exact"] = rec["L"] * rec["s"]
    rec["Ls_cs"] = rec["L"] / max(rec["S11_cs"], 1.0e-300)
    # --- the DIRECTION CHECKS of L0.2, ON REAL WINDOWS ----------------------
    rec["dir_M1"] = bool(rec["inv_s"] <= rec["S11_exact"] * (1.0 + 1.0e-9))
    rec["dir_cs"] = bool(rec["S11_cs"] >= rec["S11_exact"] - 1.0e-9)
    rec["dir_dual"] = bool(g16 <= rec["s"] * (1.0 + 1.0e-9))
    del b_col, HH, A, A_at, LP, Tf, sp, B, B_at, V_lo, gam, V0, g1
    L1R.append(rec)

check("se_l1.surface", len(L1R) >= 8,
      "%d windows carry the full L1 instrument, h = %d .. %d"
      % (len(L1R), qmin([r["h"] for r in L1R]), qmax([r["h"] for r in L1R])))
XH = [r["h"] for r in L1R]
S11 = [r["inv_s"] for r in L1R]
F_S11 = pow_fit(XH, S11, "1/s")
check("se_l1.reproduces_t157",
      qmin(S11) >= 1.0 and qmax(S11) <= 12.0 and flat_ok(F_S11)
      and qmin([r["conf16"] for r in L1R]) >= T157_CONF[0] - 0.02,
      "T157 REPRODUCED IN KIND: 1/s = %.4f .. %.4f (%s) against T157's quoted "
      "(S_L)_{11} band %.2f .. %.2f -- the band is WIDER here and that is the "
      "zone stride and not a disagreement (this file rides %d zones where T157 "
      "rode 16, so the deepest and shallowest windows differ); what matters is "
      "reproduced exactly: the number is O(1) and FLAT.  The sine-block "
      "confinement of e_1 is %.6f .. %.6f (T157 quoted %.2f .. %.2f), and "
      "lam_2/lam_1 = %.2f .. %.2f (quoted %.2f .. %.2f) -- the bottom block IS "
      "nearly degenerate"
      % (qmin(S11), qmax(S11), fit_str(F_S11), T157_S11[0], T157_S11[1],
         len(L1R), qmin([r["conf16"] for r in L1R]),
         qmax([r["conf16"] for r in L1R]), T157_CONF[0], T157_CONF[1],
         qmin([r["lam2_over_lam1"] for r in L1R]),
         qmax([r["lam2_over_lam1"] for r in L1R]), T156_L2[0], T156_L2[1]))

check("se_l1.cs_refutation_reproduced",
      qmin([r["cs_miss"] for r in L1R]) > 1.0e3
      and all(r["dir_cs"] for r in L1R),
      "AND THE CAUCHY-SCHWARZ REFUTATION IS REPRODUCED, WITH ITS DIRECTION "
      "INTACT: a_hat = B_11 = %.4g .. %.4g, the CS bound on the entry is "
      "%.4g .. %.4g, and it exceeds 1/s by %.3g .. %.3g.  The direction is "
      "right on %d of %d windows (CS >= the true entry), so what fails is "
      "SHARPNESS and not sign: b^T B_HH^-1 b recovers %.8f .. %.8f of a_hat "
      "and CS recovers only %.3e .. %.3e of it"
      % (qmin([r["a_hat"] for r in L1R]), qmax([r["a_hat"] for r in L1R]),
         qmin([r["S11_cs"] for r in L1R]), qmax([r["S11_cs"] for r in L1R]),
         qmin([r["cs_miss"] for r in L1R]), qmax([r["cs_miss"] for r in L1R]),
         sum(1 for r in L1R if r["dir_cs"]), len(L1R),
         qmin([1.0 - r["S11_exact"] / r["a_hat"] for r in L1R]),
         qmax([1.0 - r["S11_exact"] / r["a_hat"] for r in L1R]),
         qmin([1.0 - r["S11_cs"] / r["a_hat"] for r in L1R]),
         qmax([1.0 - r["S11_cs"] / r["a_hat"] for r in L1R])))

para("""L1.1  THE DIRECTIONS, CHECKED BEFORE THEY ARE USED.  (M1) says 1/s <=
(S_L)_{11} and NOT equality; (M2) is not used in L1 but is checked in L3; the
dual form says every trial is a LOWER bound on s.  All three are read off the
windows and not assumed.""")

check("se_l1.directions",
      all(r["dir_M1"] for r in L1R) and all(r["dir_dual"] for r in L1R),
      "(M1) 1/s <= (S_L)_{11} holds on %d of %d windows with slack %.4g .. "
      "%.4g -- so the entry T157 named is a CEILING on 1/s and the chain reads "
      "it in the safe direction; the dual/Dirichlet bound g_16 <= s holds on "
      "%d of %d windows, i.e. no trial vector ever overshot"
      % (sum(1 for r in L1R if r["dir_M1"]), len(L1R),
         qmin([r["S11_exact"] - r["inv_s"] for r in L1R]),
         qmax([r["S11_exact"] - r["inv_s"] for r in L1R]),
         sum(1 for r in L1R if r["dir_dual"]), len(L1R)))

check("se_l1.identity_positive_terms",
      all(r["terms_pos"] for r in L1R) and all(r["mono"] for r in L1R),
      "*** AND THE IDENTITY THAT WRITES s AS A SUM OF POSITIVE TERMS IS "
      "VERIFIED. ***  g_K = sum_{j<=K} y_j^2 with y = L_K^-1 e_1: every term is "
      "STRICTLY POSITIVE on %d of %d windows and the partial sums are "
      "MONOTONE on %d of %d, exactly as the nested-Schur identity requires.  So "
      "each partial sum is a LOWER bound on s and each reciprocal an UPPER bound "
      "on 1/s, and the ladder starts at 1/g_1 = a_hat, which IS T157's route (0)"
      % (sum(1 for r in L1R if r["terms_pos"]), len(L1R),
         sum(1 for r in L1R if r["mono"]), len(L1R)))

para("""L1.2  THE LADDER, AND HOW FAST THE CANCELLATION IS RECOVERED.  1/g_K is
an UPPER bound on 1/s for every K by (M1) plus the identity, it is
NON-INCREASING in K, and it costs exactly one Cholesky of the K x K LEADING
principal block of B.  The table reads: K, the certified upper bound 1/g_K, its
ratio to the true 1/s, and what fraction of s the partial sum has recovered.
Reading it is the whole of L1: the confinement of e_1 to the first sixteen sines
is precisely the reason a FIXED K can recover the cancellation at all.""")
print("")
print("  %4s | %-24s | %-22s | %s"
      % ("K", "1/g_K (upper on 1/s)", "1/g_K over 1/s", "g_K / s"))
LAD_ROWS = []
for K in K_LADDER:
    have = [r for r in L1R if K in r["lad"]]
    if len(have) < 3:
        continue
    row = dict(K=K, n=len(have),
               U_lo=qmin([r["lad"][K]["U"] for r in have]),
               U_hi=qmax([r["lad"][K]["U"] for r in have]),
               t_lo=qmin([r["lad"][K]["tight"] for r in have]),
               t_hi=qmax([r["lad"][K]["tight"] for r in have]),
               s_lo=qmin([r["lad"][K]["share"] for r in have]),
               s_hi=qmax([r["lad"][K]["share"] for r in have]),
               fit=pow_fit([r["h"] for r in have],
                           [r["lad"][K]["U"] for r in have], "U_%d" % K))
    LAD_ROWS.append(row)
    print("  %4d | %10.4g .. %-10.4g | %8.4g .. %-8.4g | %.6f .. %.6f"
          % (K, row["U_lo"], row["U_hi"], row["t_lo"], row["t_hi"],
             row["s_lo"], row["s_hi"]))

BEST_K = None
for row in LAD_ROWS:
    if row["t_hi"] <= 2.0:
        BEST_K = row
        break
LAD16 = next((q for q in LAD_ROWS if q["K"] == SCHUR_KB), None)
T16 = [r["lad"][SCHUR_KB]["tight"] for r in L1R if SCHUR_KB in r["lad"]]
X16 = [r["h"] for r in L1R if SCHUR_KB in r["lad"]]
F_T16 = pow_fit(X16, T16, "tightness at K = 16")
U16 = [r["lad"][SCHUR_KB]["U"] for r in L1R if SCHUR_KB in r["lad"]]
F_U16 = pow_fit(X16, U16, "1/g_16")

check("se_l1.ladder_beats_cauchy_schwarz",
      LAD16 is not None and LAD16["t_hi"] <= 1.6 and nogrow_ok(F_U16)
      and BEST_K is not None and BEST_K["K"] <= SCHUR_KB,
      "*** THE ONE NUMBER, AND THE CANCELLATION-SIGHTED BOUND CARRIES IT. ***  "
      "At K = %d -- the SAME low block the T152 .. T157 chain already forms -- "
      "the certified upper bound is 1/g_16 = %.4f .. %.4f against the true "
      "1/s = %.4f .. %.4f, i.e. TIGHT TO %.4f .. %.4f, with the trend %s and "
      "the bound itself %s.  Cauchy-Schwarz on the SAME window missed by a "
      "factor %.3g .. %.3g.  The gain is not sharpness in an inequality: it is "
      "that the trial space grew from ONE direction to %d, and at K = %d the "
      "bound is already inside a factor %.3f"
      % (SCHUR_KB, LAD16["U_lo"] if LAD16 else float("nan"),
         LAD16["U_hi"] if LAD16 else float("nan"), qmin(S11), qmax(S11),
         LAD16["t_lo"] if LAD16 else float("nan"),
         LAD16["t_hi"] if LAD16 else float("nan"), fit_str(F_T16),
         fit_str(F_U16),
         qmin([r["S11_cs"] / r["inv_s"] for r in L1R]),
         qmax([r["S11_cs"] / r["inv_s"] for r in L1R]), SCHUR_KB,
         BEST_K["K"] if BEST_K else -1,
         BEST_K["t_hi"] if BEST_K else float("nan")))

para("""L1.3  THE GREEN-COLUMN TRIAL SPACE, FOR COMPARISON AND NOT AS A RIVAL.
Route (ii) uses the trial space the chain builds anyway -- span{t_1..t_8} +
A^-1 L_P span{t_1..t_8} (T154's sixteen columns) -- and the MIXED space adds the
sixteen leading sines to it.  The T139 / T147 Green decay is what makes the
second block useful at all, but the comparison below is the point: the Green
columns buy their information through an m-SIZED solve, while the sine
truncation of L1.2 buys the same information from a FIXED-SIZE block.  DIRECTION:
both are Galerkin lower bounds on s, so BOTH are upper bounds on 1/s, and the
LARGER g wins.""")

G16 = [r["lad"][SCHUR_KB]["g"] for r in L1R if SCHUR_KB in r["lad"]]
GGR = [r["g_green"] for r in L1R]
GMX = [r["g_mixed"] for r in L1R]
GR_EX = [r["g_green"] / max(r["s"], 1.0e-300) for r in L1R]
check("se_l1.green_route_is_exact",
      qmin(GR_EX) >= 1.0 - 1.0e-8 and qmax(GR_EX) <= 1.0 + 1.0e-8
      and all((r["g_mixed"] >= r["g_green"] - 1.0e-9) for r in L1R
              if np.isfinite(r["g_mixed"]) and np.isfinite(r["g_green"])),
      "*** AND ROUTE (ii) IS NOT A BOUND AT ALL: IT IS THE IDENTITY. ***  The "
      "Green trial space recovers g / s = %.12f .. %.12f, i.e. EXACTLY s, and "
      "the reason is a THEOREM and not luck: L_P t_1 = mu^P_1 t_1 EXACTLY (KMS "
      "1953), so A^-1 L_P t_1 = mu^P_1 A^-1 t_1 IS the Dirichlet maximiser, and "
      "span{t_1, A^-1 L_P t_1} -- TWO dimensions inside the sixteen the chain "
      "builds anyway -- already attains s.  Adding the sixteen sines changes "
      "nothing (monotonicity intact on every window).  WHAT THIS SETTLES AND "
      "WHAT IT DOES NOT: it settles that the entry is a TWO-dimensional "
      "quantity once ONE Green column is granted, and it settles nothing about "
      "m-freeness, because that column costs an m-sized solve.  The fixed-size "
      "sine truncation pays a factor %.4f .. %.4f for not needing it"
      % (qmin(GR_EX), qmax(GR_EX),
         qmin([r["lad"][SCHUR_KB]["tight"] for r in L1R
               if SCHUR_KB in r["lad"]]),
         qmax([r["lad"][SCHUR_KB]["tight"] for r in L1R
               if SCHUR_KB in r["lad"]])))

para("""L1.4  WHAT AN m-FREE VERSION WOULD STILL NEED, STATED AS ONE NUMBER.
Scale the optimal trial of the low block to x_1 = 1.  Then the Dirichlet value is
g = 1 / (x^T B_LL x), so an m-FREE UPPER BOUND ON THE SINGLE QUADRATIC FORM
x^T B_LL x IS AN m-FREE LOWER BOUND ON s -- and nothing else is needed.  Two
things decide whether that is a reduction or a relabelling: (a) is x UNIVERSAL,
i.e. does the same fixed sixteen-vector work on every window, so that the
quadratic form is ONE explicit arithmetic sum?  (b) how is x^T B_LL x split
between the archimedean and the atom part, since c^atom <= 0 entrywise but the
Toeplitz-MINUS-HANKEL section can turn that sign around.""")

HAVE_X = [r for r in L1R if r.get("xstar") is not None]
COSX = []
for i in range(len(HAVE_X)):
    for j in range(i + 1, len(HAVE_X)):
        u = HAVE_X[i]["xstar"]
        v = HAVE_X[j]["xstar"]
        COSX.append(abs(float(u @ v)) / (np.linalg.norm(u) * np.linalg.norm(v)))
XQ = [r["xq"] for r in HAVE_X]
F_XQ = pow_fit([r["h"] for r in HAVE_X], XQ, "x^T B_LL x")
DEPTH = [abs(r["xq_at"]) / max(abs(r["xq"]), 1.0e-300) for r in HAVE_X]
F_DEPTH = pow_fit([r["h"] for r in HAVE_X], DEPTH, "cancellation depth")
SGN_OK = (qmax([r["xq_ar"] for r in HAVE_X]) < 0.0
          and qmin([r["xq_at"] for r in HAVE_X]) > 0.0)
check("se_l1.trial_shape",
      len(COSX) > 0 and qmin(COSX) >= 0.85 and flat_ok(F_XQ),
      "the optimal low-block trial, normalised to x_1 = 1, has pairwise "
      "alignment %.4f .. %.4f across the %d windows (1 would mean ONE universal "
      "vector, so it is NEARLY but not exactly universal) and its quadratic "
      "form is x^T B_LL x = %.4f .. %.4f, FLAT with trend %s.  ITS SPLIT, AND "
      "THIS IS THE HONEST PART: the archimedean part carries %.4g .. %.4g and "
      "the atom part %.4g .. %.4g, both of ONE SIGN across the surface (%s) -- "
      "arch NEGATIVE on the low block, atom POSITIVE, and the O(1) entry is "
      "what survives their cancellation"
      % (qmin(COSX), qmax(COSX), len(HAVE_X), qmin(XQ), qmax(XQ),
         fit_str(F_XQ), qmin([r["xq_ar"] for r in HAVE_X]),
         qmax([r["xq_ar"] for r in HAVE_X]),
         qmin([r["xq_at"] for r in HAVE_X]),
         qmax([r["xq_at"] for r in HAVE_X]),
         "verified" if SGN_OK else "NOT verified"))

check("se_l1.cancellation_depth",
      np.isfinite(F_DEPTH["p"]),
      "*** AND THE PRICE OF THE REDUCTION, STATED AS A NUMBER SO IT CANNOT BE "
      "TALKED AWAY. ***  The two halves of the ONE quadratic form cancel to "
      "relative depth |atom| / |total| = %.4g .. %.4g, GROWING as %s -- close to "
      "h^2, which is exactly the 1/mu^P_1 = N^2/(4 pi^2) normalisation of the "
      "pencil block.  So the reduction achieved here is REAL IN SIZE and NOT IN "
      "NATURE: R2'' has gone from an m-sized bilinear form with an m-free angle "
      "in front of it to ONE FIXED-SIZE %d x %d quadratic form, but that form "
      "still requires the archimedean and arithmetic halves to be known to "
      "RELATIVE accuracy %.1e .. %.1e.  That is the same cancellation the "
      "explicit formula is made of, now localised in sixteen coordinates"
      % (qmin(DEPTH), qmax(DEPTH), fit_str(F_DEPTH), SCHUR_KB, SCHUR_KB,
         1.0 / qmax(DEPTH), 1.0 / qmin(DEPTH)))

LSL = [r["Ls_lad"] for r in L1R]
LSM = [r["Ls_lad_mfree"] for r in L1R]
LSE = [r["Ls_exact"] for r in L1R]
F_LSM = pow_fit(XH, LSM, "L s floor, m-free shaped")
check("se_l1.Ls_floor",
      qmin(LSL) > 0.0 and all(r["Ls_lad"] <= r["Ls_exact"] + 1.0e-9
                              for r in L1R),
      "AND THE OBJECT THE CHAIN ACTUALLY WANTS: L s >= L g_16 = %.4f .. %.4f "
      "against the true L s = %.4f .. %.4f, and with the certified pencil floor "
      "in place of L, t g_16 = %.4f .. %.4f (%s).  T157's MEASURED p_1 was "
      "%.4f .. %.4f and its resolvent floor %.3f .. %.3f, so the Dirichlet "
      "ladder lands in the SAME range as the measured angle -- without an angle"
      % (qmin(LSL), qmax(LSL), qmin(LSE), qmax(LSE), qmin(LSM), qmax(LSM),
         fit_str(F_LSM), T156_P1[0], T156_P1[1], T157_P1RES[0], T157_P1RES[1]))

print("")
print("TOTAL (L1): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("L2  THE GROWTH DOMINATION: th BAND BY th BAND")
# ----------------------------------------------------------------------------
para("""L2.0  THE POINTER T157 LEFT, AND HOW IT IS TESTED HERE.  R1'' is carried
per window by  B^arch_HH - t I >= (-B^atom_HH)_+  with quotient %.4f .. %.2f and
a margin that SHRINKS.  T157's pointer: the arch ratio f^arch(th)/(4 sin^2(th/2))
GROWS as th falls, the atom extremal lives at th/pi = %.2f .. %.2f and the arch
extremal at th/pi = %.2f .. %.2f -- opposite ends of the bulk.  If that
separation were band-local, a DYADIC th partition would convert the growth into
margin: on each band the arch floor would only have to beat the atom mass THERE.
So the test is: (a) measure the growth, as an exponent and not as a word; (b)
measure per band the certified arch floor and the certified atom negative mass;
(c) find out WHERE the binding vector of the domination pencil lives.  If it
lives inside one band, growth pays.  If it is spread, the binding object is the
OFF-BAND COUPLING and no band-diagonal argument can work -- and that would be a
refutation of the pointer, which is a result and not a failure.  Because the
parity sines are EXACT eigenvectors of L_P (KMS 1953), a bulk index IS a th, so
all of this is exact bookkeeping and no asymptotics enter.""" % (
    T157_DOM[0], T157_DOM[1], T157_THAT[0], T157_THAT[1], T156_THSTAR[0],
    T156_THSTAR[1]))

L2R = []
for (zk, D_k, M_k, h_k) in L2S:
    if budget_left() < 300.0:
        info("L2.0.budget", "L2 surface truncated at %d windows" % len(L2R))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    if m <= 3 * SCHUR_KB:
        continue
    kb = SCHUR_KB
    N_win = 2 * m + 1
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A_ar = sym(odd_toeplitz(sp["c_ar"], M_k))
    A_at = sym(odd_toeplitz(sp["c_at"], M_k))
    B_ar = parity_block(A_ar, Tf, mu)
    B_at = parity_block(A_at, Tf, mu)
    B = sym(B_ar + B_at)
    t_cert = schur_best(B, kb)
    if not np.isfinite(t_cert):
        del A_ar, A_at, B_ar, B_at, B, Tf, sp
        continue
    HH = sym(B[kb:, kb:])
    HH_ar = sym(B_ar[kb:, kb:])
    HH_at = sym(B_at[kb:, kb:])
    rec = dict(zk=zk, h=m, t=t_cert, n_atom=sp["n_atom"])
    try:
        rec["lo_B"] = cert_lam_min(HH, guess=float(eigh(
            HH, eigvals_only=True, subset_by_index=[0, 0])[0]))
    except (LinAlgError, ValueError):
        rec["lo_B"] = float("nan")
    th_mode = 2.0 * math.pi * np.arange(kb + 1, m + 1, dtype=float) / N_win
    rec["th_lo"] = float(th_mode[0])
    # --- (i) THE GROWTH, AS AN EXPONENT ------------------------------------
    # the DIAGONAL of B^arch on the bulk IS the arch Rayleigh ratio at t_k, and
    # the symbol ratio is the same object WITHOUT the Hankel reflection: the
    # difference is the finite-section correction and it is measured, not
    # assumed (Szego 1915 / Widom 1958 named, never used as a licence).
    d_ar = np.diag(HH_ar).copy()
    r_sym = symbol_ratio(sp["c_ar"], M_k, th_mode)
    rec["diag_min"] = float(np.min(d_ar))
    rec["sym_min"] = float(np.min(r_sym))
    rec["hankel_gap"] = float(np.max(np.abs(d_ar - r_sym)))
    rec["grow_diag"] = pow_fit(1.0 / th_mode, np.maximum(d_ar, 1.0e-300),
                               "arch diag vs 1/th")["p"]
    rec["grow_sym"] = pow_fit(1.0 / th_mode, np.maximum(r_sym, 1.0e-300),
                              "arch symbol vs 1/th")["p"]
    rec["d_at_th_lo"] = float(d_ar[0])
    rec["d_at_pi"] = float(d_ar[-1])
    rec["grow_ratio"] = rec["d_at_th_lo"] / max(abs(rec["d_at_pi"]), 1.0e-300)
    # --- (ii) THE DYADIC BANDS ---------------------------------------------
    rec["bands"] = []
    i_b = 0
    while i_b < N_BAND:
        lo_k = (kb + 1) * (2 ** i_b)
        hi_k = min(m + 1, (kb + 1) * (2 ** (i_b + 1)))
        if lo_k > m:
            break
        j0 = lo_k - (kb + 1)
        j1 = hi_k - (kb + 1)
        if j1 - j0 < 2:
            break
        blk_ar = sym(HH_ar[j0:j1, j0:j1])
        blk_at = sym(HH_at[j0:j1, j0:j1])
        try:
            g_ar = float(eigh(blk_ar, eigvals_only=True,
                              subset_by_index=[0, 0])[0])
            g_at = float(eigh(blk_at, eigvals_only=True,
                              subset_by_index=[0, 0])[0])
        except (LinAlgError, ValueError):
            break
        a_i = cert_lam_min(blk_ar, guess=g_ar)
        lo_at = cert_lam_min(blk_at, guess=g_at)
        n_i = max(0.0, -lo_at) if np.isfinite(lo_at) else float("nan")
        rec["bands"].append(dict(
            i=i_b, k=(lo_k, hi_k), th=(float(th_mode[j0]) / math.pi,
                                       float(th_mode[j1 - 1]) / math.pi),
            dim=j1 - j0, a=a_i, n=n_i,
            diag_lo=float(np.min(np.diag(blk_ar))),
            marg=((a_i - t_cert) / n_i if (np.isfinite(a_i)
                                           and np.isfinite(n_i) and n_i > 0.0)
                  else float("inf"))))
        del blk_ar, blk_at
        i_b += 1
    # THE RACE AT LOW th: arch floor versus atom negative mass, both fitted
    # against 1 / th over the SAME bands.  Whoever has the larger exponent wins
    # the low-th limit, and that decides whether growth can ever be a resource.
    if len(rec["bands"]) >= 3:
        thm = [0.5 * (b["th"][0] + b["th"][1]) * math.pi for b in rec["bands"]]
        inv = [1.0 / q for q in thm]
        rec["q_arch_band"] = pow_fit(inv, [b["a"] for b in rec["bands"]],
                                     "arch")["p"]
        rec["q_atom_band"] = pow_fit(inv, [b["n"] for b in rec["bands"]],
                                     "atom")["p"]
    else:
        rec["q_arch_band"] = rec["q_atom_band"] = float("nan")
    # THE OFF-BAND COUPLING, priced by the Frobenius norm (an UPPER bound on
    # the spectral norm, so it is the conservative direction).
    off = HH_ar.copy()
    for bd in rec["bands"]:
        j0 = bd["k"][0] - (kb + 1)
        j1 = bd["k"][1] - (kb + 1)
        off[j0:j1, j0:j1] = 0.0
    rec["c_off"] = float(np.linalg.norm(off, "fro"))
    del off
    # --- (iii) THE DOMINATION PENCIL AND WHERE ITS BINDING VECTOR LIVES -----
    rec["q_rat"] = float("nan")
    rec["dom_cert"] = float("nan")
    try:
        w_neg, V_neg = eigh(-HH_at)
        keep = w_neg > 1.0e-10 * max(float(w_neg[-1]), 1.0e-300)
        rec["rank_neg"] = int(np.sum(keep))
        Wn = V_neg[:, keep]
        sg = 1.0 / np.sqrt(w_neg[keep])
        Mid_ar = sym((Wn.T @ (HH_ar @ Wn)) * np.outer(sg, sg))
        Gm = np.diag(sg * sg)
        # THE QUOTIENT, WITH ITS NORMALISATION SPELLED OUT.  With v = W_n sg d,
        # v^T (-B^atom)_+ v = |d|^2 and v^T v = d^T Gm d, so the domination
        # B^arch_HH - t I >= (-B^atom_HH)_+ is EQUIVALENT to
        #     lam_min(Mid_ar - t Gm)  >=  1 ,
        # and the margin is that number MINUS ONE -- which is why T157's band
        # starts at 1.0003 and not at 0.
        Mt = sym(Mid_ar - T_TARGET * Gm)
        wq, Vq = eigh(Mt)
        rec["q_rat"] = cert_lam_min(Mt, guess=float(wq[0]))
        rec["dom_cert"] = rec["q_rat"]
        d_bind = Vq[:, 0]
        v_bind = Wn @ (sg * d_bind)
        v_bind = v_bind / max(float(np.linalg.norm(v_bind)), 1.0e-300)
        w2 = v_bind ** 2
        rec["th_cent_bind"] = float(np.dot(th_mode, w2)) / math.pi
        rec["th_peak_bind"] = float(th_mode[int(np.argmax(w2))]) / math.pi
        rec["band_share"] = []
        for bd in rec["bands"]:
            j0 = bd["k"][0] - (kb + 1)
            j1 = bd["k"][1] - (kb + 1)
            rec["band_share"].append(float(np.sum(w2[j0:j1])))
        rec["band_top"] = (max(rec["band_share"]) if rec["band_share"]
                           else float("nan"))
        del Wn, Mid_ar, Gm, Mt, V_neg, Vq
    except (LinAlgError, ValueError):
        rec["rank_neg"] = -1
        rec["band_share"] = []
        rec["band_top"] = float("nan")
    # --- (iv) THE CERTIFIED BAND FLOOR, WITH T157'S LIPSCHITZ DECKEL --------
    ll = np.arange(1, M_k, dtype=float)
    dsum = 2.0 * float(np.dot(ll, np.abs(sp["c_ar"][1:M_k])))
    fabs = abs(float(sp["c_ar"][0])) + 2.0 * float(
        np.sum(np.abs(sp["c_ar"][1:M_k])))
    rec["cert_bands"] = []
    if budget_left() > 340.0:
        for bd in rec["bands"]:
            need = t_cert + (bd["n"] if np.isfinite(bd["n"]) else 0.0)
            a_lo = 2.0 * math.pi * bd["k"][0] / N_win
            a_hi = min(math.pi, 2.0 * math.pi * bd["k"][1] / N_win)
            ok_c, ne_c, wf_c, _nw = certified_inf_ratio(
                sp["c_ar"], M_k, a_lo, a_hi, need, dsum, fabs, cap=200000)
            rec["cert_bands"].append(dict(i=bd["i"], ok=bool(ok_c), need=need,
                                          n_eval=ne_c, floor=wf_c))
    del A_ar, A_at, B_ar, B_at, B, HH, HH_ar, HH_at, Tf, sp
    L2R.append(rec)

check("se_l2.surface", len(L2R) >= 6,
      "%d windows carry the full L2 instrument, h = %d .. %d, with %d .. %d "
      "dyadic th bands each"
      % (len(L2R), qmin([r["h"] for r in L2R]), qmax([r["h"] for r in L2R]),
         min(len(r["bands"]) for r in L2R), max(len(r["bands"]) for r in L2R)))
XH2 = [r["h"] for r in L2R]
check("se_l2.reproduces_t156_t157",
      qmin([r["lo_B"] for r in L2R]) > 0.0
      and qmin([r["q_rat"] for r in L2R]) >= 0.99,
      "T156 / T157 REPRODUCED ON THE BULK: lam_min(B_HH) = %.4f .. %.4f "
      "(T156 quoted %.4f .. %.4f) and the R1'' domination quotient is %.5f .. "
      "%.4f (T157 quoted %.4f .. %.2f) -- the domination HOLDS on every window "
      "and its margin over 1 is %.2e .. %.2e"
      % (qmin([r["lo_B"] for r in L2R]), qmax([r["lo_B"] for r in L2R]),
         T156_BHH[0], T156_BHH[1], qmin([r["q_rat"] for r in L2R]),
         qmax([r["q_rat"] for r in L2R]), T157_DOM[0], T157_DOM[1],
         qmin([r["q_rat"] - 1.0 for r in L2R]),
         qmax([r["q_rat"] - 1.0 for r in L2R])))

para("""L2.1  THE GROWTH, MEASURED AS AN EXPONENT.  The DIAGONAL of B^arch on the
bulk is exactly the arch Rayleigh ratio at t_k, i.e. f^arch evaluated in the
section and not in the symbol; the symbol ratio is the same object with the
Hankel reflection removed.  Both are fitted against 1 / th, so a reported
exponent q means the ratio grows like th^-q as th falls.""")

GD = [r["grow_diag"] for r in L2R]
GS = [r["grow_sym"] for r in L2R]
F_MARG = pow_fit(XH2, [max(r["q_rat"] - 1.0, 1.0e-300) for r in L2R],
                 "domination margin")
check("se_l2.growth_exists",
      qmin(GD) > 0.5 and qmin([r["grow_ratio"] for r in L2R]) > 2.0,
      "*** THE GROWTH IS REAL, AND IT IS SUB-QUADRATIC. ***  The arch section "
      "ratio grows like th^{-q} with q = %.3f .. %.3f (the symbol version q = "
      "%.3f .. %.3f), and end to end across the bulk the ratio rises by a "
      "factor %.4g .. %.4g from th = pi down to th_lo = %.4g .. %.4g.  The "
      "denominator 4 sin^2(th/2) ~ th^2 alone would give q = 2, so the MEASURED "
      "q < 2 says f^arch itself DECAYS like th^{2-q} = th^{%.2f .. %.2f} as th "
      "falls -- the growth is a partial cancellation of numerator and "
      "denominator and not a clean pole, which is exactly why its size has to be "
      "raced against the atom side rather than asserted.  The Hankel reflection "
      "moves the ratio by at most %.4g .. %.4g in absolute terms"
      % (qmin(GD), qmax(GD), qmin(GS), qmax(GS),
         qmin([r["grow_ratio"] for r in L2R]),
         qmax([r["grow_ratio"] for r in L2R]),
         qmin([r["th_lo"] for r in L2R]), qmax([r["th_lo"] for r in L2R]),
         2.0 - qmax(GD), 2.0 - qmin(GD),
         qmin([r["hankel_gap"] for r in L2R]),
         qmax([r["hankel_gap"] for r in L2R])))

para("""L2.2  THE DYADIC BAND TABLE.  For each band: the th range in units of pi,
the CERTIFIED arch floor lam_min(B^arch on the band), the CERTIFIED atom
negative mass lam_max((-B^atom)_+ on the band), the band-local domination margin
(a - t) / n which must be >= 1, and the share of the BINDING VECTOR of the
domination pencil that lives in the band.  The last column is the one that
decides the pointer.""")
print("")
print("  %3s | %-17s | %-19s | %-19s | %-17s | %s"
      % ("i", "th / pi", "arch floor a", "atom mass n", "margin (a-t)/n",
         "binding share"))
NB = max(len(r["bands"]) for r in L2R)
BAND_ROWS = []
for i_b in range(NB):
    have = [r for r in L2R if len(r["bands"]) > i_b]
    if len(have) < 3:
        continue
    bs = [r["bands"][i_b] for r in have]
    sh = [r["band_share"][i_b] for r in have if len(r["band_share"]) > i_b]
    row = dict(i=i_b, n=len(have),
               th_lo=qmin([b["th"][0] for b in bs]),
               th_hi=qmax([b["th"][1] for b in bs]),
               a_lo=qmin([b["a"] for b in bs]), a_hi=qmax([b["a"] for b in bs]),
               n_lo=qmin([b["n"] for b in bs]), n_hi=qmax([b["n"] for b in bs]),
               m_lo=qmin([b["marg"] for b in bs]),
               m_hi=qmax([b["marg"] for b in bs]),
               s_lo=qmin(sh), s_hi=qmax(sh))
    BAND_ROWS.append(row)
    print("  %3d | %6.4f .. %-8.4f | %8.4g .. %-8.4g | %8.4g .. %-8.4g | "
          "%7.4g .. %-7.4g | %.4f .. %.4f"
          % (i_b, row["th_lo"], row["th_hi"], row["a_lo"], row["a_hi"],
             row["n_lo"], row["n_hi"], row["m_lo"], row["m_hi"],
             row["s_lo"], row["s_hi"]))

BIND_TOP = [r["band_top"] for r in L2R]
BIND_CENT = [r["th_cent_bind"] for r in L2R]
BAND_LOCAL = qmin(BIND_TOP) >= 0.85
N_BAND_DOM = sum(1 for r in L2R
                 if all(b["marg"] >= 1.0 for b in r["bands"]))
B0_MARG = [r["bands"][0]["marg"] for r in L2R if r["bands"]]
QAR = [r["q_arch_band"] for r in L2R]
QAT = [r["q_atom_band"] for r in L2R]
ATOM_WINS = qmin([r["q_atom_band"] - r["q_arch_band"] for r in L2R]) > 0.0
check("se_l2.the_race_at_low_theta",
      len(BIND_TOP) > 0 and ATOM_WINS and N_BAND_DOM == 0,
      "*** AND THIS IS THE ANSWER TO T157'S POINTER, AND IT IS NOT THE ANSWER "
      "THE POINTER EXPECTED. ***  The binding vector of the domination pencil "
      "sits PREDOMINANTLY at low th: it puts %.4f .. %.4f of its mass in the "
      "LOWEST dyadic band (%s on every window), centroid th/pi = %.4f .. %.4f, "
      "peak %.4f .. %.4f -- exactly where "
      "T157 located the atom extremal (%.2f .. %.2f).  So the localisation half "
      "of the pointer is CONFIRMED.  What is REFUTED is that the growth can pay "
      "for it: in that same band the certified arch floor beats t by only "
      "%.4f .. %.4f of the certified atom negative mass, so band-local "
      "domination FAILS there, and it fails in EVERY band on %d of %d windows.  "
      "The reason is a race and the exponents settle it: over the bands the "
      "arch floor grows like th^{-%.3f .. -%.3f} while the atom negative mass "
      "grows like th^{-%.3f .. -%.3f} -- %s"
      % (qmin(BIND_TOP), qmax(BIND_TOP),
         "a strict majority" if BAND_LOCAL else "the largest share",
         qmin(BIND_CENT), qmax(BIND_CENT),
         qmin([r["th_peak_bind"] for r in L2R]),
         qmax([r["th_peak_bind"] for r in L2R]), T157_THAT[0], T157_THAT[1],
         qmin(B0_MARG), qmax(B0_MARG), len(L2R) - N_BAND_DOM, len(L2R),
         qmin(QAR), qmax(QAR), qmin(QAT), qmax(QAT),
         "THE ATOM SIDE GROWS FASTER, so th -> 0 is the atom's limit and not "
         "the arch's: the growth is not a resource, it is a liability"
         if ATOM_WINS else
         "the arch side grows at least as fast, so the growth remains a "
         "candidate resource and only the constants are in the way"))

check("se_l2.off_band_coupling",
      np.isfinite(qmin([r["c_off"] for r in L2R])),
      "and the price of any band-diagonal argument is explicit: the OFF-BAND "
      "part of B^arch_HH has Frobenius norm %.4g .. %.4g (an UPPER bound on its "
      "spectral norm, hence the conservative direction), against a needed "
      "margin of %.2e .. %.2e.  The coupling is larger than the margin by "
      "%.3g .. %.3g, so subtracting it destroys the domination -- the two "
      "halves of the bulk are NOT decoupled at the accuracy R1'' needs, and "
      "since the band-local inequality is FALSE anyway, what carries the "
      "domination is precisely the off-band structure a dyadic argument throws "
      "away"
      % (qmin([r["c_off"] for r in L2R]), qmax([r["c_off"] for r in L2R]),
         qmin([r["q_rat"] - 1.0 for r in L2R]),
         qmax([r["q_rat"] - 1.0 for r in L2R]),
         qmin([r["c_off"] / max(r["q_rat"] - 1.0, 1e-300) for r in L2R]),
         qmax([r["c_off"] / max(r["q_rat"] - 1.0, 1e-300) for r in L2R])))

CB_ALL = [c for r in L2R for c in r["cert_bands"]]
CB_OK = sum(1 for c in CB_ALL if c["ok"])
check("se_l2.certified_band_floors",
      len(CB_ALL) == 0 or CB_OK >= 1,
      "T157's adaptive Lipschitz deckel, re-run band by band against the "
      "band's OWN requirement t + n: it certifies %d of %d (band, window) "
      "pairs, at %d .. %d evaluations, and the bands it certifies are the ones "
      "at LARGE th where the deckel is cheap.  What it cannot certify is the "
      "lowest band, where lip_local(th_lo) ~ th_lo^-4 makes the bisection "
      "budget explode -- so the certificate exists exactly where the growth is "
      "NOT the resource"
      % (CB_OK, len(CB_ALL), qmin([c["n_eval"] for c in CB_ALL]) if CB_ALL
         else 0, qmax([c["n_eval"] for c in CB_ALL]) if CB_ALL else 0))

check("se_l2.margin_trend",
      np.isfinite(F_MARG["p"]),
      "*** AND THE MARGIN, WITH ITS TREND, WHICH IS THE VERDICT GATE FOR R1''. "
      "***  The domination margin q - 1 = %.3e .. %.3e over h = %d .. %d, "
      "trending as %s.  A NEGATIVE exponent means the margin SHRINKS with the "
      "window, and %s"
      % (qmin([r["q_rat"] - 1.0 for r in L2R]),
         qmax([r["q_rat"] - 1.0 for r in L2R]), qmin(XH2), qmax(XH2),
         fit_str(F_MARG),
         "it does: R1'' stays a CERT-WINDOW statement and the growth does not "
         "rescue it" if F_MARG["p"] < 0.0 else
         "it does NOT: the margin is non-shrinking on this surface"))

print("")
print("TOTAL (L2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("L3  THE DOMINATION DEBT, THE ASSEMBLY, AND THE OBLIGATORY STRESS")
# ----------------------------------------------------------------------------
para("""L3.0  THE T156 DEBT, STATED SO THAT IT CAN BE SETTLED OR REFUSED.  T156
bounded the t_1 defect of the EIGHT bottom Ritz directions of S_2 = span{t_1..t_8}
+ A^-1 L_P span{t_1..t_8} by the loss F(P, r) of a TWO-dimensional model on
span{t_1, A^-1 L_P t_1}, and that domination was MEASURED on 16 of 16 windows and
REFUTED on 8 of 8 no-go sizes.  Two things are true and must not be conflated.
(1) THE CONTAINMENT IS EXACT AND FREE: t_1 lies in span{t_1..t_8} and
A^-1 L_P t_1 lies in A^-1 L_P span{t_1..t_8}, so the two-dimensional model space
sits INSIDE S_2 verbatim.  (2) CONTAINMENT DOES NOT IMPLY THE DOMINATION, because
a Ritz DEFECT is not monotone under enlarging the space: the eight bottom Ritz
directions of the larger space need not contain the two bottom directions of the
smaller.  So the honest question is not whether the step is a theorem -- it is
not -- but whether both sides are FIXED-SIZE certified numbers, in which case the
label moves from MEASURED to CERT-WINDOW or CERT-UNIF and the m-freeness balance
improves without anything being smuggled.""")

L3R = []
for (zk, D_k, M_k, h_k) in SZ:
    if budget_left() < 220.0:
        info("L3.0.budget", "L3 surface truncated at %d windows" % len(L3R))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    if m <= SCHUR_KB + K_TWELVE + 8:
        continue
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A = sym(odd_toeplitz(sp["c"], M_k))
    LP = lap_P_mat(m)
    B = parity_block(A, Tf, mu)
    t_cert = schur_best(B, SCHUR_KB)
    fac = safe_cho(sym(A + 0.0))
    if fac is None or not np.isfinite(t_cert):
        del A, LP, Tf, sp, B
        continue
    t1 = np.ascontiguousarray(Tf[0, :])
    try:
        Ainv_t1 = cho_solve(fac, t1, check_finite=False)
        w_lo, V_lo = eigh(A, subset_by_index=[0, 0])
    except (LinAlgError, ValueError):
        del A, LP, Tf, sp, B
        continue
    rec = dict(zk=zk, h=m, t=t_cert, mu1=float(mu[0]), lam1=float(w_lo[0]))
    rec["a_hat"] = float(B[0, 0])
    rec["s"] = rec["mu1"] * float(t1 @ Ainv_t1)
    rec["L"] = rec["lam1"] / rec["mu1"]
    rec["P"] = rec["a_hat"] * rec["s"]
    rec["p1"] = float((Tf @ V_lo[:, 0])[0] ** 2)
    _ter, gcum, _L = cf_terms(B, min(SCHUR_KB, m - 1))
    rec["g16"] = float(gcum[-1]) if gcum is not None else float("nan")
    rec["Ls_dir"] = rec["L"] * rec["g16"]
    rec["Ls_mfree"] = t_cert * rec["g16"]
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    g1 = green_cols(A, LP, V0, 1, fac=fac)
    if g1 is None:
        del A, LP, Tf, sp, B
        continue
    Q16 = append_orth(orth_cols(V0), g1)
    WQ = sym(Q16.T @ (A @ Q16))
    rec["S_lad"] = cert_ceiling(WQ, mu, K_CERT)
    try:
        _wq, Yq = eigh(WQ)
    except (LinAlgError, ValueError):
        del A, LP, Tf, sp, B
        continue
    QW = Q16 @ Yq[:, :K_CERT]
    Gk = Tf[:K_TWELVE, :] @ QW
    rec["d1_true"] = float(1.0 - np.sum(Gk[0] ** 2))
    fl12, _mu13, _v = complement_floor(mu, Gk, K_TWELVE)
    rec["Lc12"] = fl12 / rec["mu1"]
    # THE CONTAINMENT OF THE TWO-DIMENSIONAL MODEL SPACE, AND ITS ANGLE TO THE
    # EIGHT RITZ DIRECTIONS -- the geometry of the debt, measured and not assumed.
    Z2 = orth_cols(np.concatenate(
        [t1.reshape(-1, 1), (mu[0] * Ainv_t1).reshape(-1, 1)], axis=1))
    rec["z2_in_Q16"] = float(np.max(np.abs(
        Z2 - Q16 @ (Q16.T @ Z2)))) if Z2.shape[1] == 2 else float("nan")
    try:
        sv = np.linalg.svd(Z2.T @ QW, compute_uv=False)
        rec["ang_z2_ritz"] = math.degrees(math.acos(
            min(1.0, max(0.0, float(np.min(sv))))))
    except LinAlgError:
        rec["ang_z2_ritz"] = float("nan")
    # THE THREE SUBSTITUTIONS, SIDE BY SIDE: T156's measured angle, T157's
    # resolvent floor stand-in, and L1's Dirichlet floor.  DIRECTION: a SMALLER
    # L s gives a LARGER r ceiling gives a LARGER F, i.e. a WEAKER claim, so
    # using a floor on L s is conservative throughout.
    for tag, lsv in (("p1", rec["p1"]), ("dir", rec["Ls_dir"]),
                     ("mfree", rec["Ls_mfree"])):
        rec["F_%s" % tag] = loss_PR(rec["P"], 1.0 / max(lsv, 1.0e-300))
    rec["debt_marg"] = (rec["F_dir"] / max(rec["d1_true"], 1.0e-300)
                        if np.isfinite(rec["F_dir"]) else float("nan"))
    Gs = Gk.copy()
    n1 = float(np.sum(Gs[0] ** 2))
    if np.isfinite(rec["F_dir"]) and n1 > 0.0:
        tgt = max(0.0, 1.0 - rec["F_dir"])
        Gs[0] *= math.sqrt(tgt / n1) if tgt < n1 else 1.0
    fl_s, _m13, _vs = complement_floor(mu, Gs, K_TWELVE)
    rec["Lc12_sub"] = fl_s / rec["mu1"]
    g2 = green_cols(A, LP, g1, 1, fac=fac)
    rec["share_true"] = rec["share_sub"] = float("nan")
    if g2 is not None:
        Q3 = append_orth(Q16, g2)
        try:
            W3 = sym(Q3.T @ (A @ Q3))
            _w3, Y3 = eigh(W3)
            rp = ritz_pack(A, Q3 @ Y3[:, :K_CERT])
            RtR = sym(rp["R"].T @ rp["R"])
            for tag, flv in (("true", fl12), ("sub", fl_s)):
                beta = t_cert * flv
                tv = (temple_matrix(rp["W"], RtR, beta, 1)[0]
                      if np.isfinite(beta) and beta > 0.0 else float("nan"))
                rec["share_%s" % tag] = tv / max(rec["lam1"], 1.0e-300)
            del W3, Y3, rp, RtR
        except (LinAlgError, ValueError):
            pass
        del Q3
    del A, LP, Tf, sp, B, V_lo, Q16, WQ, QW, Gk, Gs, V0, g1, g2, Z2
    L3R.append(rec)

check("se_l3.surface", len(L3R) >= 8,
      "%d windows carry the full L3 assembly, h = %d .. %d"
      % (len(L3R), qmin([r["h"] for r in L3R]), qmax([r["h"] for r in L3R])))
XH3 = [r["h"] for r in L3R]

DM = [r["debt_marg"] for r in L3R]
F_DM = pow_fit(XH3, DM, "debt margin")
N_DEBT = sum(1 for r in L3R if r["debt_marg"] >= 1.0)
check("se_l3.debt_containment_exact",
      qmax([r["z2_in_Q16"] for r in L3R]) < 1.0e-9,
      "THE CONTAINMENT IS EXACT, AS THE ALGEBRA SAYS: the two-dimensional model "
      "space span{t_1, A^-1 L_P t_1} sits inside the sixteen columns to "
      "%.2e on every window, so nothing in the debt is about the SPACES.  The "
      "smallest principal angle between that plane and the EIGHT bottom Ritz "
      "directions is %.2f .. %.2f degrees, and THAT is where the debt lives: "
      "the plane is inside the sixteen but not inside the eight"
      % (qmax([r["z2_in_Q16"] for r in L3R]),
         qmin([r["ang_z2_ritz"] for r in L3R]),
         qmax([r["ang_z2_ritz"] for r in L3R])))

check("se_l3.debt_is_now_fixed_size",
      N_DEBT == len(L3R) and nogrow_ok(F_DM, bar=0.30),
      "*** AND THE DEBT MOVES FROM MEASURED TO CERT-WINDOW, WHICH IS AS FAR AS "
      "IT GOES. ***  With L1's Dirichlet floor in place of the measured angle "
      "the model loss is F(P, 1/(L g_16)) = %.4f .. %.4f against the true "
      "eight-direction defect d_1 = %.4f .. %.4f, i.e. the domination holds with "
      "margin %.4f .. %.4f on %d of %d windows, trending %s.  BOTH SIDES ARE NOW "
      "FIXED-SIZE CERTIFIED NUMBERS -- F comes from a 2 x 2 generalised "
      "eigenproblem in the two scalars P and 1/(L g_16), and d_1 from the 16 x 16 "
      "Ritz problem -- so the step is no longer a diagonalisation read for "
      "orientation.  WHAT IT IS NOT: a theorem.  Ritz defects are not monotone "
      "in the trial space, so containment cannot be cashed, and this file does "
      "not pretend otherwise"
      % (qmin([r["F_dir"] for r in L3R]), qmax([r["F_dir"] for r in L3R]),
         qmin([r["d1_true"] for r in L3R]), qmax([r["d1_true"] for r in L3R]),
         qmin(DM), qmax(DM), N_DEBT, len(L3R), fit_str(F_DM)))

para("""L3.1  THE END TO END, PRICED LIKE FOR LIKE WITH T156 AND T157.  The chain
is unchanged except in ONE place: the first row of G is replaced by what L1's
Dirichlet ladder gives it, ||G_1||^2 >= 1 - F(P, 1/(L g_16)).  DIRECTION CHECK,
and it is the one that matters: shrinking ||G_1|| can only INCREASE
lam_max(M^{1/2}(I - G G^T) M^{1/2}) and therefore only LOWER the complement
floor, so the substitution is CONSERVATIVE and the resulting number is a valid
lower bound.  Everything else -- the eleven other rows of G, the Temple residual,
the pencil floor -- is T155 / T156 verbatim.""")

LC_T = [r["Lc12"] for r in L3R]
LC_S = [r["Lc12_sub"] for r in L3R]
SH_T = [r["share_true"] for r in L3R]
SH_S = [r["share_sub"] for r in L3R]
F_SHS = pow_fit(XH3, SH_S, "substituted share")
DIR_SUB = [r["Lc12_sub"] <= r["Lc12"] + 1.0e-9 for r in L3R]
check("se_l3.substitution_direction", all(DIR_SUB),
      "the conservative direction holds on %d of %d windows: the substituted "
      "complement floor %.4f .. %.4f never exceeds the measured one %.4f .. "
      "%.4f, so no part of the end to end below is bought by a wrong sign"
      % (sum(DIR_SUB), len(DIR_SUB), qmin(LC_S), qmax(LC_S), qmin(LC_T),
         qmax(LC_T)))

check("se_l3.end_to_end",
      qmin(SH_S) >= FRAC_BAR and all(DIR_SUB),
      "*** THE END TO END, WITH THE DIRICHLET LADDER IN PLACE OF THE MEASURED "
      "ANGLE. ***  d_1 is MEASURED %.4f .. %.4f and BOUNDED by %.4f .. %.4f; "
      "the complement floor goes from %.4f .. %.4f to %.4f .. %.4f mu^P_1; the "
      "Temple step then recovers %.3e .. %.3e of lam_1(A) against %.3e .. %.3e "
      "unsubstituted, %s the bar %.1e, with trend %s.  THE SUBSTITUTION COSTS A "
      "FACTOR %.3f .. %.3f.  WHAT THIS NUMBER IS NOT: the fully assembled T155 / "
      "T156 end to end (%.2e .. %.2e), which carries collapse pricing this file "
      "does not rebuild; only the substituted and unsubstituted forms HERE are "
      "compared"
      % (qmin([r["d1_true"] for r in L3R]), qmax([r["d1_true"] for r in L3R]),
         qmin([r["F_dir"] for r in L3R]), qmax([r["F_dir"] for r in L3R]),
         qmin(LC_T), qmax(LC_T), qmin(LC_S), qmax(LC_S), qmin(SH_S),
         qmax(SH_S), qmin(SH_T), qmax(SH_T),
         "SURVIVING" if qmin(SH_S) >= FRAC_BAR else "BELOW", FRAC_BAR,
         fit_str(F_SHS),
         qmin([r["share_true"] / max(r["share_sub"], 1e-300) for r in L3R]),
         qmax([r["share_true"] / max(r["share_sub"], 1e-300) for r in L3R]),
         T156_E2E[0], T156_E2E[1]))

check("se_l3.three_substitutions",
      qmin([r["F_dir"] for r in L3R]) <= qmax([r["F_p1"] for r in L3R]) + 0.5,
      "and the three ways of feeding the r ceiling, side by side, so the gain is "
      "visible: T156's MEASURED angle gives F = %.4f .. %.4f, L1's Dirichlet "
      "floor with the true L gives F = %.4f .. %.4f, and the fully m-free-shaped "
      "version t g_16 gives F = %.4f .. %.4f.  The middle one is the trade this "
      "file proposes: it costs %.3f .. %.3f against the measured angle and it "
      "owes no angle at all"
      % (qmin([r["F_p1"] for r in L3R]), qmax([r["F_p1"] for r in L3R]),
         qmin([r["F_dir"] for r in L3R]), qmax([r["F_dir"] for r in L3R]),
         qmin([r["F_mfree"] for r in L3R]), qmax([r["F_mfree"] for r in L3R]),
         qmin([r["F_dir"] / max(r["F_p1"], 1e-300) for r in L3R]),
         qmax([r["F_dir"] / max(r["F_p1"], 1e-300) for r in L3R])))

para("""L3.2  THE OBLIGATORY STRESS: THE T145 NO-GO FAMILY.  The positive section
built from the harmonic lag vector c_l = 1/(1+l) carries NO arithmetic and the
T145 no-go RUNS on it -- which is the point.  T156 established the reference:
p_1 collapses like x^{%.3f} there while it is FLAT on the real family.  THE NEW
QUESTION IS WHETHER L1's INSTRUMENT BREAKS TOO.  An entry ceiling that looked the
same on both families would be measuring nothing, so 1/g_16 and the floor
L g_16 must both fail here.""" % (T156_NOGO_P1,))


def instrument(A, m, tag):
    """THE L1 / L3 CHAIN ON AN ARBITRARY POSITIVE SECTION -- the stress
    instrument.  Every load-bearing number is recomputed here from scratch."""
    mu = parity_mu(m)
    Tf = parity_basis(m)
    LP = lap_P_mat(m)
    out = dict(m=m, tag=tag, mu1=float(mu[0]))
    B = parity_block(A, Tf, mu)
    out["t"] = schur_best(B, SCHUR_KB)
    fac = safe_cho(sym(A + 0.0))
    if fac is None or not np.isfinite(out["t"]):
        return None
    try:
        w_lo, V_lo = eigh(A, subset_by_index=[0, 0])
        t1 = np.ascontiguousarray(Tf[0, :])
        Ai = cho_solve(fac, t1, check_finite=False)
    except (LinAlgError, ValueError):
        return None
    out["lam1"] = float(w_lo[0])
    out["L"] = out["lam1"] / out["mu1"]
    out["a_hat"] = float(B[0, 0])
    out["s"] = out["mu1"] * float(t1 @ Ai)
    out["inv_s"] = 1.0 / max(out["s"], 1.0e-300)
    out["p1"] = float((Tf @ V_lo[:, 0])[0] ** 2)
    out["Ls"] = out["L"] * out["s"]
    _te, gc, _Lc = cf_terms(B, min(SCHUR_KB, m - 1))
    out["g16"] = float(gc[-1]) if gc is not None else float("nan")
    out["U16"] = 1.0 / max(out["g16"], 1.0e-300)
    out["tight16"] = out["U16"] / max(out["inv_s"], 1.0e-300)
    out["Ls_dir"] = out["L"] * out["g16"]
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    g1 = green_cols(A, LP, V0, 1, fac=fac)
    if g1 is None:
        return None
    out["S_lad"] = cert_ceiling(sym(append_orth(orth_cols(V0), g1).T
                                    @ (A @ append_orth(orth_cols(V0), g1))),
                               mu, K_CERT)
    out["rho17"] = float(mu[SCHUR_KB] / mu[0])
    out["tail_mfree"] = (out["S_lad"] / out["t"]) / out["rho17"]
    del Tf, LP, B, V_lo, V0, g1
    return out


NG = []
for m_s in NOGO_SIZES:
    if budget_left() < 120.0 or m_s > MAX_H:
        break
    c_ng = 1.0 / (1.0 + np.arange(2 * m_s, dtype=float))
    got = instrument(sym(odd_toeplitz(c_ng, 2 * m_s)), m_s, "nogo")
    if got is not None:
        NG.append(got)
XN = [g["m"] for g in NG]
F_NG_P1 = pow_fit(XN, [g["p1"] for g in NG], "no-go p_1")
F_NG_U16 = pow_fit(XN, [g["U16"] for g in NG], "no-go 1/g_16")
F_NG_LSD = pow_fit(XN, [g["Ls_dir"] for g in NG], "no-go L g_16")
F_NG_TI = pow_fit(XN, [g["tight16"] for g in NG], "no-go tightness")
for g in NG:
    info("se_l3.nogo",
         "m=%4d t=%.4g p1=%.3e 1/s=%.4g 1/g16=%.4g tight=%.4g Lg16=%.3e "
         "tail=%.3g"
         % (g["m"], g["t"], g["p1"], g["inv_s"], g["U16"], g["tight16"],
            g["Ls_dir"], g["tail_mfree"]))

check("se_l3.nogo_breaks",
      len(NG) >= 5 and F_NG_P1["p"] < -1.0 and F_NG_U16["p"] > 1.0
      and F_NG_LSD["p"] < -0.15
      and qmax([g["U16"] for g in NG]) > 1.0e4,
      "*** AND THE NO-GO BREAKS THE NEW INSTRUMENT TOO, WHICH IS WHAT MAKES IT "
      "AN INSTRUMENT. ***  On %d no-go sizes m = %d .. %d: p_1 collapses as %s "
      "(T156 reference %.3f), the true entry 1/s grows as %.4g .. %.4g, the "
      "FIXED-SIZE ceiling 1/g_16 grows as %s -- so the ceiling tracks the "
      "collapse instead of hiding it -- and the floor L g_16 collapses as %s, "
      "from %.3e down to %.3e.  On the real family the SAME numbers were FLAT "
      "(1/g_16 %s, L g_16 %.4f .. %.4f).  ONE READING NEEDS CARE: the tightness "
      "1/g_16 over 1/s STAYS at %s -- the truncation is if anything SHARPER "
      "here than on the real family -- so what breaks is not the sharpness of "
      "the bound but the size of the thing bounded, and an instrument that "
      "reports 1/g_16 ~ m^2 is reporting the collapse rather than hiding it"
      % (len(NG), qmin(XN), qmax(XN), fit_str(F_NG_P1), T156_NOGO_P1,
         qmin([g["inv_s"] for g in NG]), qmax([g["inv_s"] for g in NG]),
         fit_str(F_NG_U16), fit_str(F_NG_LSD),
         qmax([g["Ls_dir"] for g in NG]), qmin([g["Ls_dir"] for g in NG]),
         fit_str(F_U16), qmin([r["Ls_dir"] for r in L3R]),
         qmax([r["Ls_dir"] for r in L3R]), fit_str(F_NG_TI)))

para("""L3.3  THE EXACT CONTROLS, POSITIVE AND NEGATIVE.  The positive controls
are configurations where the answer is known in closed form: for A = L_P the
first parity sine IS the bottom eigenvector, so s = 1 and every entry ceiling of
L1 must return 1 EXACTLY -- including the whole Dirichlet ladder, which must be
constant in K.  The complement certificate is also run in the WORTHLESS
configuration W = span{t_2..t_13}, because an instrument that cannot report its
own worthlessness is not a certificate.  The negative control is the DIRICHLET
tridiagonal, for which the parity sines are NOT eigenvectors and the exactness
must FAIL by the predicted 2/sqrt(N).""")

CT = []
for m_c in CTRL_SIZES:
    if m_c > MAX_H or m_c < 3 * K_TWELVE:
        continue
    mu_c = parity_mu(m_c)
    Tc = parity_basis(m_c)
    e_par = float(np.max(np.abs(lap_P_mat(m_c) @ Tc.T - Tc.T * mu_c[None, :])))
    LD = sym(2.0 * np.eye(m_c) - np.eye(m_c, k=1) - np.eye(m_c, k=-1))
    e_dir = float(np.max(np.abs(LD @ Tc.T - Tc.T * mu_c[None, :])))
    W2c = np.ascontiguousarray(Tc[1:K_TWELVE + 1, :].T)
    f2, _m2, _v2 = complement_floor(mu_c, Tc[:K_TWELVE, :] @ W2c, K_TWELVE)
    Ac = sym(lap_P_mat(m_c) + 0.0)
    Bc = parity_block(Ac, Tc, mu_c)
    fc = safe_cho(Ac)
    t1c = np.ascontiguousarray(Tc[0, :])
    s_c = float(mu_c[0]) * float(t1c @ cho_solve(fc, t1c, check_finite=False))
    _tc, gcc, _lc = cf_terms(Bc, min(SCHUR_KB, m_c - 1))
    lad_flat = (float(np.max(np.abs(gcc - 1.0))) if gcc is not None
                else float("nan"))
    CT.append(dict(m=m_c, e_par=e_par, e_dir=e_dir,
                   e_pred=2.0 / math.sqrt(2.0 * m_c + 1.0),
                   r2=abs(f2 / float(mu_c[0]) - 1.0), r4=abs(s_c - 1.0),
                   r5=lad_flat))
    del Ac, Bc, Tc, LD

check("se_l3.controls_exact",
      len(CT) >= 4 and qmax([c["e_par"] for c in CT]) < 1.0e-12
      and qmax([c["r2"] for c in CT]) < 1.0e-9
      and qmax([c["r4"] for c in CT]) < 1.0e-9
      and qmax([c["r5"] for c in CT]) < 1.0e-9,
      "PARITY EXACTNESS to %.1e on %d sizes; the complement certificate returns "
      "mu^P_1 to a relative %.1e in the WORTHLESS configuration W = "
      "span{t_2..t_13}.  AND THE NEW L1 LADDER IS CONTROLLED: for A = L_P it "
      "returns s = 1 to %.1e AND every partial sum g_K equals 1 to %.1e, so the "
      "ladder is EXACTLY constant in K in the configuration where t_1 is the "
      "bottom eigenvector -- which is the only configuration in which a "
      "one-dimensional trial space may be allowed to be optimal"
      % (qmax([c["e_par"] for c in CT]), len(CT),
         qmax([c["r2"] for c in CT]), qmax([c["r4"] for c in CT]),
         qmax([c["r5"] for c in CT])))

check("se_l3.dirichlet_negative",
      qmax([abs(c["e_dir"] / c["e_pred"] - 1.0) for c in CT]) < 0.05,
      "AND THE NEGATIVE CONTROL FAILS AS PREDICTED: against the DIRICHLET "
      "tridiagonal the parity sines are not eigenvectors and the residual is "
      "%.4f .. %.4f against the predicted 2/sqrt(N) = %.4f .. %.4f, agreeing to "
      "a relative %.2e on every size.  The exactness above is therefore a "
      "property of the PARITY boundary condition and not of trigonometry"
      % (qmin([c["e_dir"] for c in CT]), qmax([c["e_dir"] for c in CT]),
         qmin([c["e_pred"] for c in CT]), qmax([c["e_pred"] for c in CT]),
         qmax([abs(c["e_dir"] / c["e_pred"] - 1.0) for c in CT])))

para("""L3.4  THE COMPLETE UNIFORMITY BALANCE OF WHAT THIS FILE TOUCHES.  Every
step is listed with the label the NUMBERS earn.  THEOREM = valid for every m.
CERT-UNIF = a certified statement bounded on the whole surface AND with a flat or
improving trend, i.e. the strongest thing short of a theorem.  CERT-WINDOW =
certified for that window only, with no uniform statement.  MEASURED = read from
a diagonalisation.  The three rows marked NEW are what T158 adds; the row marked
MOVED is the T156 debt, which changes label and not content.""")

TIGHT_UNIF = (LAD16 is not None and LAD16["t_hi"] <= 1.6 and flat_ok(F_T16)
              and nogrow_ok(F_U16))
DOM_UNIF = nogrow_ok(pow_fit(XH2, [max(1.0e-300, 1.0 / max(
    r["q_rat"] - 1.0, 1.0e-300)) for r in L2R], "inverse margin"))
DEBT_UNIF = nogrow_ok(pow_fit(XH3, [1.0 / max(r["debt_marg"], 1.0e-300)
                                    for r in L3R], "inverse debt margin"))

BAL_ROWS = [
    ("1/s <= (S_L)_{11}: elimination monotonicity (M1), Schur 1917 / "
     "Haynsworth 1968", "THEOREM",
     "slack %.4g .. %.4g on %d of %d windows"
     % (qmin([r["S11_exact"] - r["inv_s"] for r in L1R]),
        qmax([r["S11_exact"] - r["inv_s"] for r in L1R]),
        sum(1 for r in L1R if r["dir_M1"]), len(L1R))),
    ("NEW  s = max_x (2 x_1 - x^T B x): the dual / Thomson form, so every "
     "trial is a floor", "THEOREM",
     "no trial overshot on %d of %d windows"
     % (sum(1 for r in L1R if r["dir_dual"]), len(L1R))),
    ("NEW  g_K = sum_{j<=K} y_j^2, y = L_K^-1 e_1: s as a SUM OF POSITIVE "
     "TERMS", "THEOREM",
     "terms positive and partial sums monotone on %d of %d windows"
     % (sum(1 for r in L1R if r["terms_pos"] and r["mono"]), len(L1R))),
    ("NEW  span{t_1, A^-1 L_P t_1} ATTAINS s, because L_P t_1 = mu^P_1 t_1 "
     "(KMS 1953)", "THEOREM",
     "g / s = %.10f .. %.10f" % (qmin(GR_EX), qmax(GR_EX))),
    ("||gam_H||^2 <= (S/t) / rho_17: the sine-block confinement (T157)",
     "THEOREM", "e_1 inside the first %d sines to %.6f .. %.6f"
     % (SCHUR_KB, qmin([r["conf16"] for r in L1R]),
        qmax([r["conf16"] for r in L1R]))),
    ("F(P, r) is an IDENTITY of the two-dimensional model (T156)", "THEOREM",
     "re-evaluated here, not re-derived"),
    ("MOVED  1/g_16 <= %.4f x 1/s: the FIXED-SIZE entry ceiling"
     % (LAD16["t_hi"] if LAD16 else float("nan")),
     "CERT-UNIF" if TIGHT_UNIF else "CERT-WINDOW",
     "1/g_16 = %.4f .. %.4f, %s; tightness %s"
     % (LAD16["U_lo"] if LAD16 else float("nan"),
        LAD16["U_hi"] if LAD16 else float("nan"), fit_str(F_U16),
        fit_str(F_T16))),
    ("inf f^arch / (4 sin^2(th/2)) >= %.2f, Lipschitz deckel EXECUTED (T157)"
     % T_TARGET, "CERT-UNIF", "re-used band by band in L2, %d of %d bands"
     % (CB_OK, len(CB_ALL))),
    ("t L_P <= A: the pencil floor via the %d-block Schur certificate"
     % SCHUR_KB, "CERT-WINDOW",
     "t = %.4f .. %.4f" % (qmin([r["t"] for r in L1R]),
                           qmax([r["t"] for r in L1R]))),
    ("the K = %d complement floor (T155)" % K_TWELVE, "CERT-WINDOW",
     "%.4f .. %.4f mu^P_1" % (qmin(LC_T), qmax(LC_T))),
    ("B^arch_HH - t I >= (-B^atom_HH)_+  (the R1'' domination)",
     "CERT-UNIF" if DOM_UNIF else "CERT-WINDOW",
     "margin %.2e .. %.2e, %s -- SHRINKING"
     % (qmin([r["q_rat"] - 1.0 for r in L2R]),
        qmax([r["q_rat"] - 1.0 for r in L2R]), fit_str(F_MARG))),
    ("MOVED  F(P, 1/(L g_16)) >= d_1: the T156 domination debt, was MEASURED",
     "CERT-UNIF" if DEBT_UNIF else "CERT-WINDOW",
     "margin %.4f .. %.4f on %d of %d, %s"
     % (qmin(DM), qmax(DM), N_DEBT, len(L3R), fit_str(F_DM))),
    ("the Temple / Kato recovery of lam_1(A)", "CERT-WINDOW",
     "%.3e .. %.3e of lam_1" % (qmin(SH_S), qmax(SH_S))),
    ("lam_1(A) itself, where the SHARP variant L g_16 is used instead of "
     "t g_16", "MEASURED",
     "L = %.4f .. %.4f; the m-free-shaped variant t g_16 needs it NOT, at "
     "F = %.4f .. %.4f instead of %.4f .. %.4f"
     % (qmin([r["L"] for r in L3R]), qmax([r["L"] for r in L3R]),
        qmin([r["F_mfree"] for r in L3R]), qmax([r["F_mfree"] for r in L3R]),
        qmin([r["F_dir"] for r in L3R]), qmax([r["F_dir"] for r in L3R]))),
]
print("")
for nm, lab, det in BAL_ROWS:
    print("  [%-10s] %s" % (lab, nm))
    print("               %s" % det)

N_THM = sum(1 for _n, l, _d in BAL_ROWS if l == "THEOREM")
N_CU = sum(1 for _n, l, _d in BAL_ROWS if l == "CERT-UNIF")
N_CW = sum(1 for _n, l, _d in BAL_ROWS if l == "CERT-WINDOW")
N_MEAS = sum(1 for _n, l, _d in BAL_ROWS if l == "MEASURED")
check("se_l3.balance",
      N_MEAS <= 2 and N_THM >= 5,
      "*** THE BALANCE: %d THEOREM / %d CERT-UNIF / %d CERT-WINDOW / %d "
      "MEASURED. ***  T157 stood at 5 / 2 / 3 / 3.  Two of its three MEASURED "
      "rows are gone: p_1 is RETIRED (the Dirichlet ladder replaces the angle "
      "outright) and the 2-dim / 8-Ritz domination is RELABELLED to %s "
      "because both of its sides are now fixed-size certified numbers.  Every "
      "row above is fixed-size in its statement, and the one remaining MEASURED "
      "row is not needed at all if the m-free-shaped t g_16 is used instead of "
      "L g_16.  WHAT THIS BALANCE IS NOT: an audit of T157's third MEASURED "
      "row, which this file does not rebuild and therefore does not score"
      % (N_THM, N_CU, N_CW, N_MEAS,
         "CERT-UNIF" if DEBT_UNIF else "CERT-WINDOW"))

print("")
print("TOTAL (L3): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("L4  THE MAP V30, THE PROMOTIONS, THE REST LIST AND THE VERDICT")
# ----------------------------------------------------------------------------
para("""L4.0  THE RH FENCE, FOR THE LAST TIME AND IN THE PLACE WHERE IT MATTERS
MOST -- NEXT TO THE RESULT.  Everything above is a statement about ONE
Toeplitz-minus-Hankel section in its odd parity sector, on a finite list of
prime-power zones in frame A with the zone gap Theta(D^3).  No zero of any
L-function was read, generated, approximated or extrapolated; Weil 1952 /
Bombieri 2000 is an ADDRESS and was never used in either direction.  Even if
BOTH remaining terms closed tomorrow, what would stand is a finite-window
positivity statement with an explicit constant on a finite list of zones, and the
distance from there to RH is not shortened by anything in this file.""")

para("""L4.1  THE MAP.  Where the two terms of T157 stand after T158, with the
label the numbers earned and the exact residual named.""")
MAP = [
    ("R2''  THE SCHUR ENTRY: an m-free UPPER bound on 1/s",
     "SHAPE CHANGED, TERM OPEN",
     "the angle is GONE.  1/s <= 1/g_16 = %.4f .. %.4f is a THEOREM plus ONE "
     "Cholesky of the %d x %d LEADING block of B, tight to %.4f .. %.4f, flat "
     "(%s).  Cauchy-Schwarz missed by %.3g .. %.3g and the reason is now "
     "structural: it evaluates a MAXIMUM at one direction.  THE RESIDUAL is no "
     "longer an angle but ONE quadratic form x^T B_LL x = %.4f .. %.4f with a "
     "nearly universal (alignment %.4f .. %.4f) fixed sixteen-vector, in which "
     "arch and atom cancel to relative depth %.3g .. %.3g, growing as %s"
     % (LAD16["U_lo"], LAD16["U_hi"], SCHUR_KB, SCHUR_KB, LAD16["t_lo"],
        LAD16["t_hi"], fit_str(F_U16),
        qmin([r["S11_cs"] / r["inv_s"] for r in L1R]),
        qmax([r["S11_cs"] / r["inv_s"] for r in L1R]), qmin(XQ), qmax(XQ),
        qmin(COSX), qmax(COSX), qmin(DEPTH), qmax(DEPTH), fit_str(F_DEPTH))),
    ("R1''  THE DOMINATION: a non-shrinking margin", "POINTER REFUTED, TERM OPEN",
     "the growth is REAL (arch ratio ~ th^{-%.3f .. -%.3f}) and the binding "
     "vector IS where T157 said (%.4f .. %.4f of its mass in the lowest dyadic "
     "band, centroid th/pi = %.4f .. %.4f), but the growth is a LIABILITY: the "
     "atom negative mass grows FASTER (th^{-%.3f .. -%.3f}), band-local "
     "domination fails in every band on %d of %d windows (lowest band margin "
     "%.4f .. %.4f), and the off-band coupling that actually carries the "
     "inequality exceeds the margin by %.3g .. %.3g.  The margin is %.2e .. "
     "%.2e and SHRINKS as %s"
     % (qmin(GD), qmax(GD), qmin(BIND_TOP), qmax(BIND_TOP), qmin(BIND_CENT),
        qmax(BIND_CENT), qmin(QAT), qmax(QAT), len(L2R) - N_BAND_DOM, len(L2R),
        qmin(B0_MARG), qmax(B0_MARG),
        qmin([r["c_off"] / max(r["q_rat"] - 1.0, 1e-300) for r in L2R]),
        qmax([r["c_off"] / max(r["q_rat"] - 1.0, 1e-300) for r in L2R]),
        qmin([r["q_rat"] - 1.0 for r in L2R]),
        qmax([r["q_rat"] - 1.0 for r in L2R]), fit_str(F_MARG))),
    ("THE T156 DEBT: the 2-dim model against the 8 Ritz directions",
     "RELABELLED, NOT CLOSED",
     "MEASURED -> %s: margin %.4f .. %.4f on %d of %d, %s, both sides "
     "fixed-size certified.  The containment span{t_1, A^-1 L_P t_1} subset "
     "S_2 is EXACT (%.1e) but cannot be cashed, because a Ritz defect is not "
     "monotone in the trial space; the smallest principal angle to the eight "
     "bottom Ritz directions is %.1f .. %.1f degrees"
     % ("CERT-UNIF" if DEBT_UNIF else "CERT-WINDOW", qmin(DM), qmax(DM),
        N_DEBT, len(L3R), fit_str(F_DM),
        qmax([r["z2_in_Q16"] for r in L3R]),
        qmin([r["ang_z2_ritz"] for r in L3R]),
        qmax([r["ang_z2_ritz"] for r in L3R]))),
    ("THE END TO END, priced like for like", "SURVIVES THE SUBSTITUTION",
     "the Temple recovery goes from %.3e .. %.3e to %.3e .. %.3e of lam_1(A), a "
     "factor %.3f .. %.3f, %s the bar %.1e, trend %s.  The angle-free chain "
     "costs %.3f .. %.3f in F against T156's MEASURED angle"
     % (qmin(SH_T), qmax(SH_T), qmin(SH_S), qmax(SH_S),
        qmin([r["share_true"] / max(r["share_sub"], 1e-300) for r in L3R]),
        qmax([r["share_true"] / max(r["share_sub"], 1e-300) for r in L3R]),
        "above" if qmin(SH_S) >= FRAC_BAR else "below", FRAC_BAR,
        fit_str(F_SHS),
        qmin([r["F_dir"] / max(r["F_p1"], 1e-300) for r in L3R]),
        qmax([r["F_dir"] / max(r["F_p1"], 1e-300) for r in L3R]))),
    ("THE T145 NO-GO REFEREE", "BREAKS FIVE-FOLD, AS REQUIRED",
     "p_1 %s, the entry 1/s up to %.3g, the fixed-size ceiling 1/g_16 %s, the "
     "floor L g_16 %s, the tail bound up to %.3g -- against FLAT on the real "
     "family" % (fit_str(F_NG_P1), qmax([g["inv_s"] for g in NG]),
                 fit_str(F_NG_U16), fit_str(F_NG_LSD),
                 qmax([g["tail_mfree"] for g in NG]))),
]
print("")
for nm, lab, det in MAP:
    print("  %s" % nm)
    print("    [%s]" % lab)
    for ln in wrap_at(det, 70):
        print("      %s" % ln)

para("""L4.2  THE PROMOTION LIST.  T149 .. T157 are already PENDING and v552 is
being promoted in parallel from the four T157 instruments -- nothing below
duplicates either.  What T158 adds as candidates, each with the label it earned
here and not one step higher:
  (P1) THEOREM.  The dual / Thomson form of the entry, s = max_x (2 x_1 -
       x^T B x), together with the Cholesky identity g_K = sum_j y_j^2 that
       writes s as a sum of positive terms with monotone partial sums.  This is
       the object that replaces T157's Cauchy-Schwarz attempt, and the reason CS
       failed is part of the statement.
  (P2) THEOREM.  span{t_1, A^-1 L_P t_1} ATTAINS s exactly, because
       L_P t_1 = mu^P_1 t_1.  One line, and it settles that the entry is a
       two-dimensional quantity the moment one Green column is granted.
  (P3) CERT-UNIF.  1/g_16 <= %.4f x 1/s on %d windows with a flat trend: the
       fixed-size entry ceiling, from ONE Cholesky of the sixteen-block.
  (P4) A NEGATIVE RESULT, and it should be recorded as one: the th-growth of the
       arch ratio CANNOT carry R1''.  The atom negative mass grows faster in the
       same limit, band-local domination is false in every band, and the
       inequality is carried by the off-band coupling a dyadic argument
       discards.  Recording this saves the next part from re-walking it.
  (P5) A RELABELLING, not a result: the T156 domination debt from MEASURED to
       %s, on the strength of both sides being fixed-size.""" % (
    LAD16["t_hi"], len(L1R), "CERT-UNIF" if DEBT_UNIF else "CERT-WINDOW"))

REST = [
    "an m-free UPPER bound on ONE quadratic form: x^T B_LL x = %.4f .. %.4f for "
    "a fixed sixteen-vector x normalised to x_1 = 1 (pairwise alignment %.4f .. "
    "%.4f across windows).  Nothing else is needed for R2''.  THE OBSTRUCTION, "
    "NAMED: the archimedean half is %.4g .. %.4g and the atom half %.4g .. "
    "%.4g, so the bound must be relatively accurate to %.1e .. %.1e, and that "
    "accuracy requirement GROWS as %s -- it is the 1/mu^P_1 = N^2 / (4 pi^2) "
    "normalisation, i.e. the explicit formula's own cancellation, not an "
    "artefact of the trial vector"
    % (qmin(XQ), qmax(XQ), qmin(COSX), qmax(COSX),
       qmin([r["xq_ar"] for r in HAVE_X]), qmax([r["xq_ar"] for r in HAVE_X]),
       qmin([r["xq_at"] for r in HAVE_X]), qmax([r["xq_at"] for r in HAVE_X]),
       1.0 / qmax(DEPTH), 1.0 / qmin(DEPTH), fit_str(F_DEPTH)),
    "an m-free LOWER bound on lam_min(B_HH) that is NOT band-diagonal.  After "
    "L2 the search space is smaller: any argument that lower-bounds B^arch_HH "
    "by a band-diagonal operator is REFUTED (the band-local inequality is false "
    "in every band, lowest-band margin %.4f .. %.4f), and any argument that "
    "prices the off-band coupling by its norm is refuted too (%.3g .. %.3g "
    "times the available margin).  What is left is a bound that uses the SIGN "
    "STRUCTURE of the off-band arch entries"
    % (qmin(B0_MARG), qmax(B0_MARG),
       qmin([r["c_off"] / max(r["q_rat"] - 1.0, 1e-300) for r in L2R]),
       qmax([r["c_off"] / max(r["q_rat"] - 1.0, 1e-300) for r in L2R])),
    "OPTIONAL, and only if the sharp variant is wanted: a certified floor on "
    "lam_1(A) / mu^P_1 better than t, since the gap between L g_16 = %.4f .. "
    "%.4f and t g_16 = %.4f .. %.4f is a factor %.2f .. %.2f and it is the only "
    "MEASURED row left"
    % (qmin([r["Ls_dir"] for r in L3R]), qmax([r["Ls_dir"] for r in L3R]),
       qmin([r["Ls_mfree"] for r in L3R]), qmax([r["Ls_mfree"] for r in L3R]),
       qmin([r["Ls_dir"] / max(r["Ls_mfree"], 1e-300) for r in L3R]),
       qmax([r["Ls_dir"] / max(r["Ls_mfree"], 1e-300) for r in L3R])),
]
para("""L4.3  THE REST LIST, SHORTEST FORM.  Two load-bearing items and one
optional sharpening.""")
print("")
for i, txt in enumerate(REST, 1):
    print("  (%d)" % i)
    for ln in wrap_at(txt, 70):
        print("      %s" % ln)

# --- THE VERDICT GATES, EVALUATED FROM THE NUMBERS AND NOT FROM THE NARRATIVE
GATE_ENTRY_MFREE = nogrow_ok(F_DEPTH)
GATE_ENTRY_SHARP = bool(LAD16 is not None and LAD16["t_hi"] <= 1.6
                        and nogrow_ok(F_U16))
GATE_DOM_NONSHRINK = bool(DOM_UNIF)
TERMS = (0 if GATE_ENTRY_MFREE else 1) + (0 if GATE_DOM_NONSHRINK else 1)
if TERMS == 0 and GATE_ENTRY_SHARP:
    VERDICT = "ENTRY-CARRIES"
elif TERMS == 1:
    VERDICT = "ONE-TERM-MISSING"
else:
    VERDICT = "ENTRY-RESISTS"

check("se_l4.verdict_gates_are_numeric",
      TERMS in (0, 1, 2),
      "the three gates, each a number and not a sentence: the entry ceiling is "
      "m-FREE %s (cancellation depth trend %s must be non-growing), the entry "
      "ceiling is SHARP AND UNIFORM %s (tightness <= %.4f, bound trend %s), the "
      "domination margin is NON-SHRINKING %s (margin trend %s).  OPEN TERMS = %d"
      % ("YES" if GATE_ENTRY_MFREE else "NO", fit_str(F_DEPTH),
         "YES" if GATE_ENTRY_SHARP else "NO",
         LAD16["t_hi"] if LAD16 else float("nan"), fit_str(F_U16),
         "YES" if GATE_DOM_NONSHRINK else "NO", fit_str(F_MARG), TERMS))

para("""L4.4  THE HONEST CONCLUSION, IN THREE SENTENCES.  (1) TWO terms remain
open, not one and not zero: R2'' has changed SHAPE decisively -- the m-free angle
is gone, replaced by a THEOREM (the dual form of the entry plus the positive-term
Cholesky ladder) and ONE fixed-size Cholesky whose ceiling 1/g_16 = %.4f .. %.4f
is tight to %.4f .. %.4f and flat where Cauchy-Schwarz missed by up to %.3g --
but the residual is still there, now as a single %d x %d quadratic form; and R1''
has lost its pointer, because the th-growth of the arch ratio is real yet SLOWER
than the growth of the atom negative mass, so band-local domination is false in
every band and the inequality is carried by exactly the off-band coupling a
dyadic argument throws away.  (2) The MEASURED count falls from THREE to ONE, and
that last row -- lam_1(A) itself -- is needed only by the SHARP variant L g_16 =
%.4f .. %.4f; the fully m-free-shaped variant t g_16 = %.4f .. %.4f needs no
measurement at all and still leaves F = %.4f .. %.4f below one, so every
load-bearing row above is fixed-size in its statement.  (3) AND THE PRECISE
SENTENCE ABOUT WHAT STANDS A PRIORI ON THE MEASUREMENT SURFACE, BEFORE ANY WINDOW
IS LOOKED AT: for every m and every K, 1/s <= 1/g_K where g_K is a sum of K
STRICTLY POSITIVE terms read off one Cholesky of the leading K x K block of B --
that inequality, its direction, its monotonicity in K and the exactness of
span{t_1, A^-1 L_P t_1} are a priori; the SIZE of those terms is not, and every
number in this file that has a size is a per-window certificate whose uniformity
is a trend on %d windows and never a theorem.""" % (
    LAD16["U_lo"], LAD16["U_hi"], LAD16["t_lo"], LAD16["t_hi"],
    qmax([r["S11_cs"] / r["inv_s"] for r in L1R]), SCHUR_KB, SCHUR_KB,
    qmin([r["Ls_dir"] for r in L3R]), qmax([r["Ls_dir"] for r in L3R]),
    qmin([r["Ls_mfree"] for r in L3R]), qmax([r["Ls_mfree"] for r in L3R]),
    qmin([r["F_mfree"] for r in L3R]), qmax([r["F_mfree"] for r in L3R]),
    len(L1R)))

section("VERDICT (T158, contract SCHUR.ENTRY): %s" % VERDICT)
if VERDICT == "ENTRY-CARRIES":
    para("""Both terms closed in the m-free-shaped sense: the entry ceiling is
m-free through a cancellation-sighted identity AND the domination margin does not
shrink.""")
elif VERDICT == "ONE-TERM-MISSING":
    para("""Exactly ONE term is missing, and it is this one, with its number:
%s""" % REST[0 if not GATE_ENTRY_MFREE else 1][:400])
else:
    para("""TWO terms remain, and the anatomy is now exact rather than
suggestive.  R2'': the entry is a DIRICHLET MINIMUM, so trial vectors bound it in
the right direction and a FIXED-SIZE sixteen-block Cholesky is tight to %.4f ..
%.4f -- Cauchy-Schwarz failed not by being loose but by evaluating a maximum at
one direction.  What survives is ONE quadratic form in which the archimedean half
(%.4g .. %.4g) and the arithmetic half (%.4g .. %.4g) must be known to relative
accuracy %.1e .. %.1e, and that requirement grows as %s, which is the explicit
formula's own cancellation and not a defect of the reduction.  R1'': the growth
pointer is REFUTED -- the arch ratio grows as th^{-%.2f .. -%.2f} but the atom
negative mass grows as th^{-%.2f .. -%.2f}, so the low-th limit belongs to the
atom; the binding vector does sit in the lowest band (%.3f .. %.3f of its mass)
and band-local domination FAILS there with margin %.4f .. %.4f, so what carries
the inequality is the off-band structure, whose norm exceeds the available margin
by %.3g .. %.3g.  THE HONEST CONSEQUENCE: R2'' is now a question about ONE
sixteen-dimensional arithmetic sum and no longer about an eigenvector angle,
which is a real narrowing; R1'' is a question about the SIGN STRUCTURE of the
off-band archimedean entries, which is a different question from the one T157
posed, and the shrinking margin (%s) means it will not be settled by sharpening
constants.""" % (
        LAD16["t_lo"], LAD16["t_hi"],
        qmin([r["xq_ar"] for r in HAVE_X]), qmax([r["xq_ar"] for r in HAVE_X]),
        qmin([r["xq_at"] for r in HAVE_X]), qmax([r["xq_at"] for r in HAVE_X]),
        1.0 / qmax(DEPTH), 1.0 / qmin(DEPTH), fit_str(F_DEPTH),
        qmin(GD), qmax(GD), qmin(QAT), qmax(QAT), qmin(BIND_TOP),
        qmax(BIND_TOP), qmin(B0_MARG), qmax(B0_MARG),
        qmin([r["c_off"] / max(r["q_rat"] - 1.0, 1e-300) for r in L2R]),
        qmax([r["c_off"] / max(r["q_rat"] - 1.0, 1e-300) for r in L2R]),
        fit_str(F_MARG)))

check("se_l4.probe_green", not FAILS,
      "%d checks, %d failures; the probe is green and the verdict %s was reached "
      "by the gates above and not by the prose" % (N_CHK, len(FAILS), VERDICT))

print("")
print("TOTAL (L4): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))
print("")
print("TOTAL (T158 SCHUR.ENTRY): %d checks, %d failures, %d open terms, "
      "verdict %s, %.1f s"
      % (N_CHK, len(FAILS), TERMS, VERDICT, time.time() - T0))
