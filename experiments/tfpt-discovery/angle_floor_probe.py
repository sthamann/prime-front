"""PART 157 -- THE CONTRACT ``ANGLE.FLOOR'': THE TWO ANGLES.

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
zones.  The distance from there to RH is mapped in K4 and never travelled.

WHAT T156 LEFT: TWO TERMS, AND BOTH OF THEM ARE NOW SCALARS.

  R2''  THE p_1 FLOOR.  An m-free LOWER bound for
        p_1 = cos^2 angle(t_1, e_1(A)), MEASURED 0.2010 .. 0.3282 (55.1 ..
        63.4 deg) and FLAT (x^{0.054 +- 0.029}).  Everything ABOVE it is a
        theorem: the loss closes as F(P, r) in two scalars, and the chain
        r <= 1/(L s) <= 1/p_1 is sharp to 1.03 .. 1.16.  A second debt sits
        next to it: the step from the two-dimensional model to the
        eight-dimensional Ritz defect, MEASURED on 16 of 16 real windows and
        REFUTED on 8 of 8 no-go sizes.
  R1''  THE ALIGNMENT ANGLE.  An m-free LOWER bound for the arch Rayleigh
        quotient ON THE SUBSPACE WHERE THE ATOM FORM IS LARGE -- equivalently
        an m-free angle between the two extremal vectors.  The arch half is
        DONE: the one-variable grid infimum of f^arch(th) / (4 sin^2(th/2))
        clears the target by 3.29 .. 5.59, is non-decreasing in h and is
        grid-stable to 1.4e-5, with its minimum at th/pi = 0.990 .. 1.000 --
        the ALTERNATING lag sum.  What is missing is the angle: the bulk-block
        minimiser sees only 6.2e-3 .. 0.50 of the atom operator, at 52.7 ..
        90.0 deg from the atom extremal.

WHAT THIS FILE DOES.  K1 attacks the p_1 floor on three routes -- the classical
Rayleigh angle bound with certified ingredients, the BLOCK version of it (the
angle to the whole nearly degenerate bottom block instead of to e_1 alone,
which is what the T156 chain may actually need), and the T146 resolvent /
column route -- and it asks, before all three, whether the chain needs an angle
AT ALL.  K2 attacks the alignment angle: where the atom extremal lives, the
quantitative form of the cancellation, and the one-variable arch statement as a
certified grid-plus-Lipschitz claim.  K3 assembles, re-prices end to end and
runs the obligatory stress.  K4 is the map, the promotion list, the rest list
and the verdict.

DISCIPLINE.  THEOREM / CERTIFIED / MEASURED / FIT are kept strictly apart and
every claim carries its label; the word ``proven'' is used nowhere for any
m-freeness claim.  Directions (upper versus lower bound) are pedantic
throughout, and T154's Courant-Fischer lesson -- a Ritz value is a CEILING and
never a floor -- is restated at every use.  Classics cited where used:
Davis-Kahan 1970, Kantorovich 1948, Temple 1928, Kato 1949, Courant-Fischer
1920, Szego 1915, Fejer 1915, Kac-Murdock-Szego 1953, Widom 1958, Schur 1917,
Haynsworth 1968, Sylvester 1852, Cauchy 1829, Weyl 1912, Chebyshev 1852,
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
np.random.seed(157157)

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 760.0             # HARD probe budget (< 900 s)

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 400000
ZONE_DEEP = 380000

# --- the measurement surface, DECLARED BEFORE ANY RESULT IS SEEN ------------
K1_ZONES = 16
K1_HCAP = 1400
K2_ZONES = 12
K2_HCAP = 1100

K_CERT = 8                   # the modes the bottom certificate is about
K_TWELVE = 12                # the K of the T155 / T156 complement certificate
SCHUR_KB = 16                # the FIXED low block of the T152 .. T156 chain
J_LADDER = (1, 2, 3, 4, 6, 8)   # *** THE BOTTOM-BLOCK SIZES OF K1 (ii) ***
T_LADDER = (0.25, 0.245, 0.24, 0.235, 0.23, 0.225, 0.22, 0.215, 0.21, 0.205,
            0.20, 0.19, 0.18, 0.16, 0.14, 0.12, 0.10, 0.05)
BAR_UNIF = 0.25              # |exponent| + band bar for "flat / non-growing"
T_TARGET = 0.25

DOM_LADDER = (0.25, 0.22, 0.20, 0.18, 0.15, 0.10)  # the K2 domination targets
NOGO_SIZES = (48, 64, 96, 128, 192, 256, 384, 512)
CTRL_SIZES = (64, 128, 256, 384, 512, 700)

# T155 / T156 numbers, QUOTED, never recomputed as an input to anything
T156_P1 = (0.2010, 0.3282)      # the MEASURED p_1 band -- the target of K1
T156_ANG = (55.1, 63.4)         # the same, in degrees
T156_TIGHT = (1.03, 1.16)       # how sharp 1/(L s) <= 1/p_1 is
T156_CEIL = (0.672, 0.799)      # the loss AT the ceiling
T156_TRUE = (0.539, 0.632)      # the loss in truth
T156_LADS = (1.10, 2.39)        # the certified ladder constant S
T156_L2 = (1.25, 3.45)          # lam_2 / lam_1: the NEARLY DEGENERATE bottom
T156_ARCHFAC = (3.29, 5.59)     # the arch one-variable reserve, over target
T156_THSTAR = (0.990, 1.000)    # where the arch infimum sits, in th/pi
T156_AVOID = (6.2e-3, 0.50)     # what the minimiser sees of the atom operator
T156_ANGMIN = (52.7, 90.0)      # the angle between the two extremal vectors
T156_BHH = (0.2661, 0.4436)     # lam_min(B_HH) on the bulk
T156_E2E = (3.28e-2, 2.83e-1)   # end to end, certified per window
T156_NOGO_P1 = -4.818           # the no-go p_1 collapse exponent: the referee
FRAC_BAR = 4.0e-2               # the K3 bar on the m-free-shaped end to end

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
    check("af_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("af_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("af_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("af_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "angle_floor_probe.py", "single new file in the sandbox")


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
    """AN UPPER BOUND on the spectral norm of R, certified by a Cholesky of
    s I - R^T R on the SMALL side.  DIRECTION: upper bound, and it enters every
    residual floor SQUARED."""
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
# prime-power arithmetic (exact, cheap) -- the T111 .. T156 code path
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
    bit-for-bit the object T111 .. T156 use, and the split is EXACT because the
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
    k = 1 .. m (Kac-Murdock-Szego 1953 in the parity sector).  EXACT, not
    asymptotic: the odd grid never contains th = 0."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m):
    """THE ORTHONORMAL EIGENBASIS OF L_P: t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N).
    That these are EXACT eigenvectors of L_P is the fact every separation
    argument in this file rests on, and it is verified to machine precision in
    the K3 controls."""
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
    lam_min(B) is the pencil floor and lam_max(B) the pencil ceiling, i.e.
    lam_min(B) L_P <= A <= lam_max(B) L_P as OPERATORS.  Because the map is
    linear in A, B^arch + B^atom = B EXACTLY, which is what K2 splits."""
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
# the subspace instruments (T154 .. T156, unchanged) -- reused, not re-derived
# ----------------------------------------------------------------------------
def ritz_pack(A, Q):
    """THE RITZ DATA OF A SUBSPACE, both directions spelled out.  W = Q^T A Q
    with Q^T Q = I; th = eig(W) ASCENDING.  DIRECTION 1 (ceiling,
    Courant-Fischer 1920 / Cauchy 1829): lam_k(A) <= th_k for every k <= dim --
    Ritz values are UPPER bounds for the eigenvalues OF THE SAME INDEX, and that
    is the ONLY way they are used.  DIRECTION 2: R = A Q - Q W satisfies
    Q^T R = 0 and is the object Temple 1928 / Kato 1949 turn into a LOWER
    bound."""
    W = sym(Q.T @ (A @ Q))
    th = np.linalg.eigvalsh(W)
    R = A @ Q - Q @ W
    return dict(W=W, th=th, R=R, nrm_R=cert_norm2(R))


def temple_matrix(W, RtR, beta, K):
    """TEMPLE 1928 / KATO 1949 IN ITS MATRIX (SCHUR-COMPLEMENT) FORM.  S =
    span(Q) of dimension d with Q_perp^T A Q_perp >= beta I.  For gam < beta,
        S(gam) = W - gam I - Rt^T (A_perp - gam I)^-1 Rt
              >= W - gam I - (R^T R) / (beta - gam) =: M(gam) ,
    a MATRIX inequality and not the crude ||R||^2 I.  By Sylvester 1852 /
    Haynsworth 1968 the inertia is additive, so #{lam_j(A) < gam} = #neg S(gam)
    <= #neg M(gam), and lam_k(A) >= gam as soon as #neg M(gam) <= k - 1.
    DIRECTION: the returned numbers are LOWER bounds on lam_k(A)."""
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
    """K^F = max_{k <= K} lam_max(Y_k^T W Y_k) / mu^P_k, Y_k the k lowest Ritz
    directions -- T154's CLOSED sixteen-column ceiling.  Each ratio is an UPPER
    bound on lam_k(A) / mu^P_k by Courant-Fischer and each numerator is one
    Cholesky of a k x k matrix."""
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
    M = np.maximum(muK1 - mu[:K], 0.0)
    rt = np.sqrt(M)
    E = sym((np.eye(K) - G[:K] @ G[:K].T) * np.outer(rt, rt))
    try:
        wE, VE = eigh(E)
    except (LinAlgError, ValueError):
        return float("nan"), float("nan"), None
    top = cert_lam_max(E, guess=float(wE[-1]) + 1.0e-13 * muK1)
    if not np.isfinite(top):
        return float("nan"), float("nan"), None
    return muK1 - top, muK1, VE[:, -1]


def loss_PR(P, r):
    """THE T156 KERNEL F(P, r), QUOTED AS A THEOREM AND NOT RE-DERIVED.  With
        W' = [[P, 1], [1, 1]] ,   N' = [[1, 1], [1, r]] ,
        P = (t_1^T A t_1)(t_1^T A^-1 t_1) >= 1   (Kantorovich 1948; Cauchy) ,
        r = ||A^-1 t_1||^2 / (t_1^T A^-1 t_1)^2 >= 1 ,
    the t_1 loss of the two-dimensional model is
        F(P, r) = 1 - (al + be)^2 / (al^2 + 2 al be + be^2 r)
    for the bottom generalised eigenvector (al, be) of (W', N').  THEOREM: the
    reduction is an identity for every m (T156, J1.2), and it is re-checked
    against the true two-dimensional Ritz vector on every window in K1."""
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
    INTERVAL STARTING AT a.  With |f'| <= dsum := 2 sum_l l |c_l|, |g'| =
    |2 sin th| <= 2, |f| <= fabs := |c_0| + 2 sum_l |c_l| and g monotone
    increasing on (0, pi] so g >= g(a),
        |R'| = |f'/g - f g'/g^2| <= dsum / g(a) + 2 fabs / g(a)^2 .
    Using g(a) instead of g(th_lo) is the whole difference: at th near pi the
    denominator is 4 and the constant is smaller by orders of magnitude.
    DIRECTION: an UPPER bound on |R'|, hence usable in a LOWER bound on R."""
    g = 4.0 * math.sin(0.5 * a) ** 2
    return dsum / g + 2.0 * fabs / (g * g)


def certified_inf_ratio(c, M, th_lo, th_hi, target, dsum, fabs, cap=400000):
    """*** THE ADAPTIVE LIPSCHITZ DECKEL, EXECUTED AND NOT ASSERTED. ***

    Certifies  R(th) = f(th) / (4 sin^2(th/2))  >=  target  on [th_lo, th_hi]
    by interval bisection: an interval [a, b] is ACCEPTED as soon as
        R(mid) - lip_local(a) (b - a) / 2  >=  target ,
    valid because |R'| <= lip_local(a) on [a, b] by the bound above, and SPLIT
    otherwise.  DIRECTION: every accepted interval carries a LOWER bound on R,
    so success is a certificate and failure is only a failure of this budget.
    Returns (ok, n_eval, worst_certified_floor, narrowest_interval)."""
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


def symbol_min(c, M, th):
    """THE TOEPLITZ SYMBOL f(th) = c_0 + 2 sum_{l>=1} c_l cos(l th).  MEASURED,
    and it is the symbol of the TOEPLITZ part only: the section also carries a
    Hankel reflection, so Szego 1915 / Widom 1958 is a NAMED CANDIDATE here and
    never a licence."""
    ll = np.arange(1, M)
    return c[0] + 2.0 * (np.cos(np.outer(th, ll)) @ c[1:M])


section("K0  THE FENCE, THE LIBRARY, AND THE SURFACE")
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

check("af_k0.zone_gaps",
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
check("af_k0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f is VERIFIED at every jump point up to n = %d (max "
      "%.6f); psi jumps only at prime powers, so this is the true max on the "
      "range, and it is never assumed beyond it" % (B_PSI, ATOM_MAX, _bpsi))

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > K1_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(K1_ZONES, 1))
    SZ = CAND[::-1][::step][:K1_ZONES]
    SZ.sort(key=lambda t: t[0])
check("af_k0.surface", len(SZ) >= 8,
      "%d prime-power zones admit a frame-A window inside the cap (h <= %d, "
      "MAX_H = %d): h = %d .. %d"
      % (len(SZ), K1_HCAP, MAX_H, min(t[3] for t in SZ), max(t[3] for t in SZ)))

para("""K0.1  WHAT COUNTS AS WHAT, PEDANTICALLY.  THEOREM = an identity or a
classical inequality valid for every m.  CERTIFIED = a numeric bound produced by
a completed factorisation with its backward-error floor carried, valid for THAT
window only; a certificate is additionally called FIXED-SIZE when the
factorisation it needs has a size independent of m.  MEASURED = a
diagonalisation or an angle read for orientation.  FIT = an exponent on the
finite surface, never promoted to anything.  The word ``proven'' is used nowhere
in this file for any m-freeness claim, and no verdict may be reached by
narrative: the verdict gates in K4 are evaluated from the numbers.""")

N_FLOOR = 2 * H_MIN + 1
RHO_FLOOR = (4.0 * np.sin(math.pi * np.arange(1, 18) / N_FLOOR) ** 2
             / (4.0 * math.sin(math.pi / N_FLOOR) ** 2))
para("""K0.2  THE ONE UNIFORM ARITHMETIC INGREDIENT, STATED ONCE.  Every m-free
form below uses the KMS ratios rho_k = mu^P_k / mu^P_1 = sin^2(pi k/N) /
sin^2(pi/N), N = 2m + 1 (Kac-Murdock-Szego 1953), and it uses them ONLY from
BELOW.  THEOREM: sin(k x) / sin(x) is decreasing in x on (0, pi/k), so rho_k is
INCREASING in N and its infimum over the admissible range m >= %d is attained at
N = %d.  The floors used everywhere below are therefore rho_2 >= %.4f, rho_3 >=
%.4f, rho_5 >= %.4f, rho_9 >= %.4f, rho_13 >= %.4f, rho_17 >= %.4f, and the
direction of every one of them is re-checked per window in K1.1.""" % (
    H_MIN, N_FLOOR, RHO_FLOOR[1], RHO_FLOOR[2], RHO_FLOOR[4], RHO_FLOOR[8],
    RHO_FLOOR[12], RHO_FLOOR[16]))

print("")
print("TOTAL (K0): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("K1  THE p_1 FLOOR -- AND WHETHER THE CHAIN NEEDS AN ANGLE AT ALL")
# ----------------------------------------------------------------------------
para("""K1.0  WHAT R2'' STILL OWES, AND WHERE EXACTLY.  T156 closed the loss into
F(P, r), a function of TWO Rayleigh scalars of A at the single vector t_1, and
boxed P by the certified pencil.  The ONLY place an angle entered was the r
CEILING: the theorem is r <= 1 / (L s) with L s = lam_1(A) t_1^T A^-1 t_1, and
T156 bounded L s from below by p_1 = cos^2 angle(t_1, e_1(A)), MEASURED %.4f ..
%.4f.  So the debt is ONE floor on ONE Rayleigh quantity.  Before asking for the
angle, K1 asks the question T156 did not: does L s need an angle at all?""" % (
    T156_P1[0], T156_P1[1]))

para("""K1.1  ROUTE (0), THE ANGLE-FREE ONE, AND IT IS A THEOREM.  In the
eigenbasis of A, with p_j the squared overlaps of t_1 and sum_j p_j = 1,
    L s = lam_1 sum_j p_j / lam_j ,     RQ(t_1) = t_1^T A t_1 = sum_j p_j lam_j .
CAUCHY-SCHWARZ (equivalently the arithmetic-harmonic inequality on the weights
p_j, i.e. Kantorovich 1948 read in the other direction) gives
    (sum_j p_j / lam_j) (sum_j p_j lam_j)  >=  (sum_j p_j)^2 = 1 ,
hence the ANGLE-FREE floor
    *** L s  >=  lam_1(A) / RQ(t_1)  =  L / a_hat ***
with a_hat = RQ(t_1) / mu^P_1.  Both L and a_hat are boxed by the CERTIFIED
two-sided pencil t L_P <= A <= kap L_P: L >= t (Courant-Fischer applied to the
pencil floor) and a_hat <= kap (the pencil ceiling at t_1).  Therefore
    L s >= t / kap  and  r <= 1 / (L s) <= a_hat / L <= kap / t ,
a THEOREM in which no eigenvector of A appears anywhere.  DIRECTION, pedantically:
L s is bounded BELOW, so 1/(L s) is bounded ABOVE, so r is bounded ABOVE, which
is the direction F needs.  Route (0) is compared against the p_1 route on every
window below, and the comparison is the point of K1.""")

K1R = []
for (zk, D_k, M_k, h_k) in SZ:
    if budget_left() < 360.0:
        info("K1.1.budget", "K1 surface truncated at %d windows" % len(K1R))
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
    try:
        kap_meas = float(eigh(B, eigvals_only=True,
                              subset_by_index=[m - 1, m - 1])[0])
    except (LinAlgError, ValueError):
        kap_meas = ray_top(B)
    kap = cert_lam_max(B, guess=kap_meas)
    fac = safe_cho(sym(A + 0.0))
    if fac is None or not np.isfinite(t_cert) or not np.isfinite(kap):
        del A, LP, Tf, sp, B
        continue
    rec = dict(zk=zk, h=m, t=t_cert, kap=kap, mu1=float(mu[0]))
    rec["rho"] = [float(mu[k] / mu[0]) for k in range(min(17, m))]
    rec["rho_dir"] = all(rec["rho"][k] >= RHO_FLOOR[k] - 1.0e-12
                         for k in range(len(rec["rho"])))
    # --- the two T156 scalars, and the bottom spectrum -----------------------
    t1 = np.ascontiguousarray(Tf[0, :])
    try:
        Ainv_t1 = cho_solve(fac, t1, check_finite=False)
        w_lo, V_lo = eigh(A, subset_by_index=[0, 9])
    except (LinAlgError, ValueError):
        del A, LP, Tf, sp, B
        continue
    a_hat = float(t1 @ (A @ t1)) / rec["mu1"]
    s_sc = rec["mu1"] * float(t1 @ Ainv_t1)
    g_sc = rec["mu1"] ** 2 * float(Ainv_t1 @ Ainv_t1)
    rec.update(a_hat=a_hat, s=s_sc, g=g_sc, P=a_hat * s_sc,
               r=g_sc / max(s_sc * s_sc, 1.0e-300))
    rec["lam"] = [float(x) for x in w_lo]
    rec["lam1"] = rec["lam"][0]
    rec["L"] = rec["lam1"] / rec["mu1"]
    rec["Ls"] = rec["L"] * s_sc
    rec["lam2_over_lam1"] = rec["lam"][1] / rec["lam1"]
    gam = Tf @ V_lo[:, 0]
    rec["p1"] = float(gam[0] ** 2)
    rec["th1"] = math.degrees(math.acos(min(1.0, math.sqrt(rec["p1"]))))
    ov = Tf[:, :] @ V_lo                       # parity content of e_1 .. e_10
    rec["gam_low16"] = float(np.sum(ov[:SCHUR_KB, 0] ** 2))
    # ---- THE CERTIFIED LADDER CEILING S: lam_k(A) <= S mu^P_k --------------
    # T154's closed sixteen-column ceiling.  IT AND NOT kap IS THE RIGHT UPPER
    # BOUND ON lam_1: kap is the pencil ceiling at the TOP of the spectrum and
    # grows with the atom mass, while S is a bound on the BOTTOM ladder only.
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    g1 = green_cols(A, LP, V0, 1, fac=fac)
    if g1 is None:
        del A, LP, Tf, sp, B
        continue
    Q16 = append_orth(orth_cols(V0), g1)
    WQ = sym(Q16.T @ (A @ Q16))
    rec["S_lad"] = cert_ceiling(WQ, mu, K_CERT)
    try:
        _, Yq = eigh(WQ)
    except (LinAlgError, ValueError):
        del A, LP, Tf, sp, B
        continue
    QW = Q16 @ Yq[:, :K_CERT]
    Gk = Tf[:K_TWELVE, :] @ QW
    rec["d1_true"] = float(1.0 - np.sum(Gk[0] ** 2))
    rec["dk"] = [float(1.0 - np.sum(Gk[k] ** 2)) for k in range(K_TWELVE)]
    fl12, mu13, _v = complement_floor(mu, Gk, K_TWELVE)
    rec["Lc12"] = fl12 / rec["mu1"]
    del WQ, QW, V0
    # ---- ROUTE (0): the angle-free Cauchy-Schwarz floor, and its price -----
    rec["Ls_cs"] = rec["L"] / a_hat
    rec["Ls_cs_mfree"] = t_cert / kap
    rec["r_ceil_cs"] = a_hat / rec["L"]
    rec["r_ceil_cs_mfree"] = kap / t_cert
    # ---- ROUTE (0b): THE SCHUR-COMPLEMENT ROUTE ---------------------------
    # IDENTITY: s = mu^P_1 t_1^T A^-1 t_1 = (B^-1)_{11}, because A^-1 =
    # T^T Lam^{-1/2} B^-1 Lam^{-1/2} T and t_1 is the FIRST parity sine.  Hence
    #   1 / s = (S_L)_{11} ,  S_L := B_LL - B_LH B_HH^-1 B_HL ,
    # the (1,1) entry of the SAME fixed-size kb x kb Schur complement the
    # T152 .. T156 chain already forms, and therefore
    #   L s = L / (S_L)_{11} >= t / (S_L)_{11} .
    # A CERTIFIED UPPER BOUND on that one entry needs NO inversion: with
    # b = B_{H,1}, Cauchy-Schwarz on the positive definite B_HH gives
    #   b^T B_HH^-1 b >= ||b||^4 / (b^T B_HH b) ,  so
    #   (S_L)_{11} = B_11 - b^T B_HH^-1 b <= a_hat - ||b||^4 / (b^T B_HH b) .
    b_col = np.ascontiguousarray(B[SCHUR_KB:, 0])
    bb = float(b_col @ b_col)
    bqb = float(b_col @ (B[SCHUR_KB:, SCHUR_KB:] @ b_col))
    rec["S11_exact"] = 1.0 / max(s_sc, 1.0e-300)
    rec["S11_cert"] = a_hat - (bb * bb / bqb if bqb > 0.0 else 0.0)
    rec["Ls_schur"] = (rec["L"] / rec["S11_cert"] if rec["S11_cert"] > 0.0
                       else float("nan"))
    rec["Ls_schur_mfree"] = (t_cert / rec["S11_cert"]
                             if rec["S11_cert"] > 0.0 else float("nan"))
    rec["schur_tight"] = (rec["S11_cert"] / rec["S11_exact"]
                          if rec["S11_exact"] > 0.0 else float("nan"))
    del b_col
    rec["Ls_p1"] = rec["p1"]
    rec["r_ceil_p1"] = 1.0 / max(rec["p1"], 1.0e-300)
    rec["cs_beats_p1"] = rec["Ls_cs"] >= rec["p1"]
    # ---- ROUTE (i): the classical Rayleigh angle bound --------------------
    # p_1 >= (lam_2 - RQ) / (lam_2 - lam_1), the one-block Temple/Davis-Kahan
    # form.  MEASURED ingredients first, then the m-free substitution.
    RQ = a_hat * rec["mu1"]
    rec["RQ_over_lam2"] = RQ / rec["lam"][1]
    den1 = rec["lam"][1] - rec["lam1"]
    rec["ray1_meas"] = ((rec["lam"][1] - RQ) / den1 if den1 > 0.0
                        else float("nan"))
    num_mf = t_cert * rec["rho"][1] - kap
    den_mf = kap * rec["rho"][1] - t_cert
    rec["ray1_mfree"] = num_mf / den_mf if den_mf > 0.0 else float("nan")
    # ---- ROUTE (ii): the BLOCK version, over the preregistered J ladder ----
    # p_blk(J) = sum_{j<=J} p_j >= (lam_{J+1} - RQ) / (lam_{J+1} - lam_1) and
    # L s >= p_blk(J) lam_1 / lam_J -- the price of widening the block.
    rec["blk"] = {}
    for J in J_LADDER:
        if J + 1 > len(rec["lam"]):
            continue
        p_blk = float(np.sum(gam[:J] ** 2))
        dJ = rec["lam"][J] - rec["lam1"]
        b_meas = ((rec["lam"][J] - RQ) / dJ if dJ > 0.0 else float("nan"))
        nm = t_cert * rec["rho"][J] - kap
        dm = kap * rec["rho"][J] - t_cert
        b_mfree = nm / dm if dm > 0.0 else float("nan")
        ls_meas = p_blk * rec["lam1"] / rec["lam"][J - 1]
        ls_mfree = ((b_mfree if np.isfinite(b_mfree) and b_mfree > 0.0 else 0.0)
                    * t_cert / (kap * rec["rho"][J - 1]))
        rec["blk"][J] = dict(p_blk=p_blk, b_meas=b_meas, b_mfree=b_mfree,
                             ls_meas=ls_meas, ls_mfree=ls_mfree,
                             price=rec["lam"][J - 1] / rec["lam1"])
    # ---- ROUTE (iii): the T146 resolvent / column route -------------------
    # C = T A T^T = Lam^{1/2} B Lam^{1/2}; partition at kb.  The eigen-equation
    # C gam = lam_1 gam gives gam_L = -(C_LL - lam_1)^-1 C_LH gam_H and the
    # FIXED-SIZE Schur null problem [C_LL - lam_1 - C_LH (C_HH - lam_1)^-1
    # C_HL] gam_L = 0.  THE TAIL IS A THEOREM: A >= t L_P gives
    #   lam_1 = e_1^T A e_1 >= t sum_k mu^P_k gam_k^2 >= t mu^P_{kb+1} ||gam_H||^2
    # so ||gam_H||^2 <= lam_1 / (t mu^P_{kb+1}) <= (kap / t) / rho_{kb+1}, and
    #   p_1 = gam_1^2 = ghat_1^2 (1 - ||gam_H||^2) >= ghat_1^2 (1 - that) .
    kb = SCHUR_KB
    rt_mu = np.sqrt(mu)
    C_LL = sym(B[:kb, :kb] * np.outer(rt_mu[:kb], rt_mu[:kb]))
    C_HL = (B[kb:, :kb] * np.outer(rt_mu[kb:], rt_mu[:kb]))
    HHmat = sym(B[kb:, kb:] * np.outer(rt_mu[kb:], rt_mu[kb:])
                - rec["lam1"] * np.eye(m - kb))
    rec["tail_thm"] = rec["lam1"] / (t_cert * float(mu[kb]))
    rec["tail_mfree"] = (rec["S_lad"] / t_cert) / rec["rho"][kb]
    rec["tail_mfree_kap"] = (kap / t_cert) / rec["rho"][kb]
    rec["tail_meas"] = 1.0 - rec["gam_low16"]
    f_hh = safe_cho(HHmat)
    if f_hh is not None:
        Xc = cho_solve(f_hh, C_HL, check_finite=False)
        S16 = sym(C_LL - rec["lam1"] * np.eye(kb) - C_HL.T @ Xc)
        try:
            wS, VS = eigh(S16)
            ghat = VS[:, int(np.argmin(np.abs(wS)))]
            rec["ghat1_sq"] = float(ghat[0] ** 2)
            rec["S16_resid"] = float(np.min(np.abs(wS))) / max(gersh(S16), 1e-300)
            rec["tau_meas"] = cert_norm2(Xc @ ghat.reshape(-1, 1))
        except (LinAlgError, ValueError):
            rec["ghat1_sq"] = float("nan")
        del Xc, S16
    else:
        rec["ghat1_sq"] = float("nan")
    rec["p1_res_thm"] = rec.get("ghat1_sq", float("nan")) * (
        1.0 - min(1.0, rec["tail_thm"]))
    rec["p1_res_mfree"] = rec.get("ghat1_sq", float("nan")) * (
        1.0 - min(1.0, rec["tail_mfree"]))
    # ---- THE END TO END, ASSEMBLED LIKE FOR LIKE WITH T156 ----------------
    # d_1 <= F(P, r) with r <= 1 / p_1^{route (iii)}: the ONE substitution that
    # makes the first row of G m-free-shaped.  DIRECTION CHECK: shrinking
    # ||G_1|| can only INCREASE lam_max(M^{1/2}(I - G G^T)M^{1/2}) and therefore
    # only LOWER the complement floor, so the substitution is conservative.
    rec["d1_bound"] = loss_PR(rec["P"], 1.0 / max(rec["p1_res_mfree"], 1e-300))
    Gs = Gk.copy()
    n1 = float(np.sum(Gs[0] ** 2))
    if np.isfinite(rec["d1_bound"]) and n1 > 0.0:
        tgt = max(0.0, 1.0 - rec["d1_bound"])
        Gs[0] *= math.sqrt(tgt / n1) if tgt < n1 else 1.0
    fl_s, _m13, _vs = complement_floor(mu, Gs, K_TWELVE)
    rec["Lc12_sub"] = fl_s / rec["mu1"]
    Q3 = append_orth(Q16, green_cols(A, LP, g1, 1, fac=fac))
    try:
        W3 = sym(Q3.T @ (A @ Q3))
        _, Y3 = eigh(W3)
        Qr = Q3 @ Y3[:, :K_CERT]
        rp = ritz_pack(A, Qr)
        rec["res3"] = rp["nrm_R"] / rec["mu1"]
        RtR = sym(rp["R"].T @ rp["R"])
        for tag, flv in (("true", fl12), ("sub", fl_s)):
            beta = t_cert * flv
            rec["temple_%s" % tag] = (
                temple_matrix(rp["W"], RtR, beta, 1)[0]
                if np.isfinite(beta) and beta > 0.0 else float("nan"))
            rec["share_%s" % tag] = rec["temple_%s" % tag] / max(
                rec["lam1"], 1.0e-300)
        del W3, Y3, Qr, rp, RtR
    except (LinAlgError, ValueError):
        rec["share_true"] = rec["share_sub"] = float("nan")
    del C_LL, C_HL, HHmat, A, LP, Tf, sp, B, V_lo, ov, Q16, g1, Gk, Gs, Q3
    K1R.append(rec)

check("af_k1.surface", len(K1R) >= 8,
      "%d windows carry the full K1 instrument, h = %d .. %d"
      % (len(K1R), qmin([r["h"] for r in K1R]), qmax([r["h"] for r in K1R])))
XH = [r["h"] for r in K1R]
P1 = [r["p1"] for r in K1R]
F_P1 = pow_fit(XH, P1, "p_1")
check("af_k1.rho_floors", all(r["rho_dir"] for r in K1R),
      "the KMS ratio floors of K0.2 hold on %d of %d windows, in the LOWER "
      "direction, as the monotonicity theorem says they must" % (len(K1R),
                                                                len(K1R)))
check("af_k1.reproduces_t156",
      qmin(P1) >= T156_P1[0] - 5.0e-3 and qmax(P1) <= T156_P1[1] + 5.0e-3
      and flat_ok(F_P1),
      "T156 REPRODUCED: p_1 = %.4f .. %.4f (%.1f .. %.1f deg), %s, against the "
      "quoted %.4f .. %.4f.  lam_2 / lam_1 = %.2f .. %.2f -- the bottom block "
      "IS nearly degenerate, quoted %.2f .. %.2f"
      % (qmin(P1), qmax(P1), qmin([r["th1"] for r in K1R]),
         qmax([r["th1"] for r in K1R]), fit_str(F_P1), T156_P1[0], T156_P1[1],
         qmin([r["lam2_over_lam1"] for r in K1R]),
         qmax([r["lam2_over_lam1"] for r in K1R]), T156_L2[0], T156_L2[1]))

# --- the direction checks of route (0), ON REAL WINDOWS ---------------------
D0 = [r["Ls"] >= r["Ls_cs"] - 1.0e-12 for r in K1R]
D0b = [r["Ls"] >= r["p1"] - 1.0e-12 for r in K1R]
D0c = [r["r"] <= 1.0 / max(r["Ls"], 1e-300) + 1.0e-9 for r in K1R]
D0d = [r["Ls_cs"] >= r["Ls_cs_mfree"] - 1.0e-12 for r in K1R]
check("af_k1.route0_directions", all(D0) and all(D0b) and all(D0c) and all(D0d),
      "EVERY DIRECTION OF ROUTE (0) HOLDS ON EVERY WINDOW: L s >= L / a_hat on "
      "%d of %d, L s >= p_1 on %d of %d, r <= 1/(L s) on %d of %d, and "
      "L / a_hat >= t / kap on %d of %d.  So the two floors on L s are both "
      "valid and can be compared like for like"
      % (sum(D0), len(D0), sum(D0b), len(D0b), sum(D0c), len(D0c),
         sum(D0d), len(D0d)))

LSCS = [r["Ls_cs"] for r in K1R]
KAP = [r["kap"] for r in K1R]
AHAT = [r["a_hat"] for r in K1R]
F_LSCS = pow_fit(XH, LSCS, "L/a_hat")
F_KAP = pow_fit(XH, KAP, "kap")
F_AHAT = pow_fit(XH, AHAT, "a_hat")
NBEAT = sum(1 for r in K1R if r["cs_beats_p1"])
check("af_k1.route0_refuted",
      NBEAT == 0 and not flat_ok(F_LSCS) and qmax(KAP) > 1.0e3,
      "*** ROUTE (0) IS VALID AND WORTHLESS, AND THE REASON IS EXACTLY THE "
      "FACTOR P. ***  L s / (L / a_hat) = a_hat s = P identically, so the "
      "Cauchy-Schwarz floor loses precisely the Kantorovich product -- and "
      "T156 measured P at 10^3 .. 10^6, because A and L_P differ by orders of "
      "magnitude at t_1.  Numerically: L / a_hat = %.3e .. %.3e (%s, "
      "COLLAPSING like h^-2.85), against the measured L s = %.4f .. %.4f, a "
      "factor %.3e .. %.3e short; the m-free substitution t / kap is worse "
      "still because kap = %.3e .. %.3e (%s) is the pencil ceiling at the TOP "
      "of the spectrum and carries the whole atom mass (a_hat = %.3e .. %.3e, "
      "%s).  It beats the p_1 floor on %d of %d windows.  SO THE ANGLE CANNOT "
      "BE AVOIDED BY CAUCHY-SCHWARZ, AND kap IS THE WRONG CEILING FOR ANY "
      "BOTTOM QUANTITY"
      % (qmin(LSCS), qmax(LSCS), fit_str(F_LSCS),
         qmin([r["Ls"] for r in K1R]), qmax([r["Ls"] for r in K1R]),
         qmin([r["Ls"] / r["Ls_cs"] for r in K1R]),
         qmax([r["Ls"] / r["Ls_cs"] for r in K1R]), qmin(KAP), qmax(KAP),
         fit_str(F_KAP), qmin(AHAT), qmax(AHAT), fit_str(F_AHAT),
         NBEAT, len(K1R)))

SLAD = [r["S_lad"] for r in K1R]
F_SLAD = pow_fit(XH, SLAD, "S")
check("af_k1.ladder_is_the_right_ceiling",
      qmax(SLAD) < 3.0 and flat_ok(F_SLAD)
      and all(r["L"] <= r["S_lad"] + 1.0e-9 for r in K1R),
      "AND THE RIGHT CEILING IS THE CERTIFIED LADDER, NOT THE PENCIL.  S = "
      "%.4f .. %.4f (%s, FLAT), quoted %.2f .. %.2f, and lam_1 <= S mu^P_1 "
      "holds on %d of %d windows with L = %.4f .. %.4f.  S is smaller than kap "
      "by a factor %.2e .. %.2e: every upper bound on a BOTTOM eigenvalue below "
      "uses S, and the direction is checked each time"
      % (qmin(SLAD), qmax(SLAD), fit_str(F_SLAD), T156_LADS[0], T156_LADS[1],
         sum(1 for r in K1R if r["L"] <= r["S_lad"] + 1.0e-9), len(K1R),
         qmin([r["L"] for r in K1R]), qmax([r["L"] for r in K1R]),
         qmin([r["kap"] / r["S_lad"] for r in K1R]),
         qmax([r["kap"] / r["S_lad"] for r in K1R])))

para("""K1.1b  ROUTE (0b), THE SCHUR-COMPLEMENT ROUTE, AND IT CHANGES THE SHAPE OF
THE DEBT.  There is an IDENTITY nobody used before T157: because A^-1 = T^T
Lam^{-1/2} B^-1 Lam^{-1/2} T and t_1 is the FIRST parity sine,
    s = mu^P_1 t_1^T A^-1 t_1 = (B^-1)_{11} ,   hence   1 / s = (S_L)_{11}
with S_L = B_LL - B_LH B_HH^-1 B_HL THE VERY kb x kb SCHUR COMPLEMENT the
T152 .. T156 chain already forms for its floor certificate.  So
    L s = L / (S_L)_{11}  >=  t / (S_L)_{11} ,
and R2'' becomes an m-free UPPER bound on ONE DIAGONAL ENTRY OF A FIXED-SIZE
MATRIX instead of a lower bound on an angle between two m-sized vectors.  A
certified upper bound on that entry costs no inversion at all: with b = B_{H,1},
Cauchy-Schwarz on the positive definite B_HH gives b^T B_HH^-1 b >= ||b||^4 /
(b^T B_HH b) and therefore
    (S_L)_{11} <= a_hat - ||b||^4 / (b^T B_HH b) ,
three quadratic forms of B and nothing else.  DIRECTION: the entry is bounded
ABOVE, so L s is bounded BELOW, which is the direction F needs.""")

S11E = [r["S11_exact"] for r in K1R]
S11C = [r["S11_cert"] for r in K1R]
LSS = [r["Ls_schur"] for r in K1R]
F_S11E = pow_fit(XH, S11E, "1/s")
F_S11C = pow_fit(XH, S11C, "S11 cert")
F_LSS = pow_fit(XH, LSS, "Ls schur")
SC_DIR = [np.isfinite(r["Ls_schur"]) and r["Ls_schur"] <= r["Ls"] + 1.0e-9
          for r in K1R]
SC_BEAT = sum(1 for r in K1R if np.isfinite(r["Ls_schur"])
              and r["Ls_schur"] >= r["p1"])
check("af_k1.route0b_changes_the_shape",
      all(SC_DIR) and flat_ok(F_S11E) and qmax(S11E) < 10.0 and SC_BEAT == 0,
      "*** ROUTE (0b) DOES NOT CLOSE R2'' AND IT CHANGES ITS SHAPE, WHICH IS "
      "THE MORE USEFUL OF THE TWO. ***  THE GOOD HALF, and it is an identity: "
      "1 / s = (S_L)_{11} = %.4f .. %.4f (%s, FLAT) is an O(1) NUMBER, and it "
      "is a DIAGONAL ENTRY OF THE FIXED-SIZE %d x %d SCHUR COMPLEMENT THE CHAIN "
      "ALREADY FORMS -- no eigenvector of A occurs in it, and no angle.  So the "
      "T156 debt can be restated as: an m-free UPPER BOUND ON ONE DIAGONAL "
      "ENTRY OF A %d x %d MATRIX, against a_hat = %.3e .. %.3e which is what "
      "the same entry would be WITHOUT the Schur subtraction.  THE BAD HALF: "
      "the inversion-free Cauchy-Schwarz ceiling on that entry is %.3e .. "
      "%.3e (%s), too large by a factor %.2e .. %.2e, so the resulting floor "
      "L s >= %.3e .. %.3e (%s) beats the p_1 floor on %d of %d windows -- "
      "i.e. NEVER.  THE CANCELLATION IN b^T B_HH^-1 b IS ALMOST COMPLETE AND "
      "CAUCHY-SCHWARZ CANNOT SEE IT, exactly the T155 lesson about the atom "
      "block repeated one level up"
      % (qmin(S11E), qmax(S11E), fit_str(F_S11E), SCHUR_KB, SCHUR_KB,
         SCHUR_KB, SCHUR_KB, qmin(AHAT), qmax(AHAT), qmin(S11C), qmax(S11C),
         fit_str(F_S11C), qmin([r["schur_tight"] for r in K1R]),
         qmax([r["schur_tight"] for r in K1R]), qmin(LSS), qmax(LSS),
         fit_str(F_LSS), SC_BEAT, len(K1R)))

para("""K1.2  ROUTE (i), THE CLASSICAL RAYLEIGH ANGLE BOUND, AND WHY THE NEARLY
DEGENERATE BOTTOM BLOCK EMPTIES IT.  For a unit vector x with RQ = x^T A x, the
expansion RQ = sum_j p_j lam_j >= p_1 lam_1 + (1 - p_1) lam_2 gives
    p_1  >=  (lam_2 - RQ) / (lam_2 - lam_1) ,
the one-block form behind Temple 1928 and behind the Davis-Kahan 1970 sin-theta
transfer.  Its ingredients are exactly the ones T156 certified: RQ(t_1) = a_hat
mu^P_1 from ABOVE by the pencil ceiling, lam_2 from BELOW by t mu^P_2, lam_1 from
BELOW by t mu^P_1 -- but note the DIRECTIONS: the numerator needs lam_2 from
BELOW and RQ from ABOVE, while the denominator needs lam_2 from ABOVE and lam_1
from BELOW, so the m-free substitution is (t rho_2 - kap) / (kap rho_2 - t).  It
is positive only if kap < t rho_2, i.e. only if the pencil ceiling is smaller
than four times the pencil floor.  THE MEASURED FORM IS TESTED FIRST, so that no
part of the emptiness can be blamed on the substitution.""")

R1M = [r["ray1_meas"] for r in K1R]
R1F = [r["ray1_mfree"] for r in K1R]
N1M = sum(1 for r in K1R if np.isfinite(r["ray1_meas"]) and r["ray1_meas"] > 0.0)
N1F = sum(1 for r in K1R if np.isfinite(r["ray1_mfree"]) and r["ray1_mfree"] > 0.0)
check("af_k1.route1_is_empty", N1M == 0 and N1F == 0,
      "*** ROUTE (i) IS EMPTY, AND IT IS EMPTY ALREADY IN ITS MEASURED FORM. "
      "***  RQ(t_1) EXCEEDS lam_2 by a factor %.2f .. %.2f on every window, so "
      "the numerator lam_2 - RQ is NEGATIVE and the classical one-block bound "
      "returns %.3f .. %.3f -- a lower bound below zero, i.e. no information.  "
      "It is positive on %d of %d windows measured and %d of %d m-free.  THE "
      "REASON IS THE NEARLY DEGENERATE BOTTOM: with lam_2 / lam_1 = %.2f .. "
      "%.2f the whole one-block gap (lam_2 - lam_1) is of the same order as "
      "lam_1 itself, while RQ(t_1) / mu^P_1 = %.3f .. %.3f sits far above both. "
      " NO amount of certification of the ingredients can rescue this route: it "
      "is the SHAPE of the bound that fails, exactly as the T156 pointer warned"
      % (qmin([r["RQ_over_lam2"] for r in K1R]),
         qmax([r["RQ_over_lam2"] for r in K1R]), qmin(R1M), qmax(R1M),
         N1M, len(K1R), N1F, len(K1R),
         qmin([r["lam2_over_lam1"] for r in K1R]),
         qmax([r["lam2_over_lam1"] for r in K1R]),
         qmin([r["a_hat"] for r in K1R]), qmax([r["a_hat"] for r in K1R])))

para("""K1.3  ROUTE (ii), THE BLOCK VERSION, AND THE PRICE OF WIDENING.  The same
expansion with the bottom block of size J instead of e_1 alone reads
    p_blk(J) := sum_{j <= J} p_j  >=  (lam_{J+1} - RQ) / (lam_{J+1} - lam_1) ,
and the T156 chain DOES admit it, because what the chain needs is a floor on
L s = sum_j p_j lam_1 / lam_j and not on p_1: dropping every term outside the
block,
    L s  >=  p_blk(J) lam_1 / lam_J
-- so the block version costs exactly the factor lam_J / lam_1, and that factor
is what has to be paid back.  Both halves are run over the preregistered ladder
J = %s, measured and m-free.""" % (", ".join(str(J) for J in J_LADDER)))

BLK_ROWS = []
for J in J_LADDER:
    have = [r for r in K1R if J in r["blk"]]
    if not have:
        continue
    row = dict(J=J,
               p_lo=qmin([r["blk"][J]["p_blk"] for r in have]),
               p_hi=qmax([r["blk"][J]["p_blk"] for r in have]),
               bm_lo=qmin([r["blk"][J]["b_meas"] for r in have]),
               bm_hi=qmax([r["blk"][J]["b_meas"] for r in have]),
               bf_lo=qmin([r["blk"][J]["b_mfree"] for r in have]),
               bf_hi=qmax([r["blk"][J]["b_mfree"] for r in have]),
               ls_lo=qmin([r["blk"][J]["ls_meas"] for r in have]),
               lsf_lo=qmin([r["blk"][J]["ls_mfree"] for r in have]),
               pr_lo=qmin([r["blk"][J]["price"] for r in have]),
               pr_hi=qmax([r["blk"][J]["price"] for r in have]),
               n_pos=sum(1 for r in have if np.isfinite(r["blk"][J]["b_meas"])
                         and r["blk"][J]["b_meas"] > 0.0))
    BLK_ROWS.append(row)
    info("K1.3.block",
         "J = %2d: p_blk = %.4f .. %.4f, block Rayleigh bound (measured) "
         "%.4f .. %.4f positive on %d of %d, m-free %.4f .. %.4f; price "
         "lam_J/lam_1 = %.2f .. %.2f; resulting L s floor: measured >= %.4f, "
         "m-free >= %.4g"
         % (J, row["p_lo"], row["p_hi"], row["bm_lo"], row["bm_hi"],
            row["n_pos"], len(have), row["bf_lo"], row["bf_hi"], row["pr_lo"],
            row["pr_hi"], row["ls_lo"], row["lsf_lo"]))

BEST_BLK = max(BLK_ROWS, key=lambda q: (q["ls_lo"] if np.isfinite(q["ls_lo"])
                                        else -1.0)) if BLK_ROWS else None
N_RAY_POS = max(q["n_pos"] for q in BLK_ROWS) if BLK_ROWS else 0
BLK2 = [q for q in BLK_ROWS if q["J"] == 2]
check("af_k1.route2_answers_the_t156_question",
      BEST_BLK is not None and N_RAY_POS == 0 and bool(BLK2)
      and BLK2[0]["p_lo"] > 0.9,
      "*** ROUTE (ii): THE ANSWER TO THE T156 QUESTION IS YES FOR THE CHAIN AND "
      "NO FOR THE BOUND. ***  (a) THE CHAIN ALLOWS THE BLOCK: L s >= p_blk(J) "
      "lam_1 / lam_J needs only the block mass and never e_1, and the block mass "
      "is spectacular -- p_blk(2) = %.4f .. %.4f, i.e. t_1 sits almost ENTIRELY "
      "in the bottom nearly degenerate PAIR of A, and p_blk(4) = %.4f .. %.4f.  "
      "(b) THE BLOCK RAYLEIGH BOUND IS STILL EMPTY: it is positive on %d of %d "
      "windows at EVERY J of the ladder, because RQ(t_1) exceeds lam_9 as badly "
      "as it exceeds lam_2.  (c) The best block floor is L s >= %.4f at J = %d, "
      "paying the price lam_J / lam_1 = %.2f .. %.2f -- a factor %.2f below the "
      "direct p_1 floor %.4f, so widening the block LOSES against e_1 alone.  "
      "The near degeneracy therefore helps the SHAPE and hurts the CONSTANT"
      % (BLK2[0]["p_lo"], BLK2[0]["p_hi"],
         qmin([r["blk"][4]["p_blk"] for r in K1R if 4 in r["blk"]]),
         qmax([r["blk"][4]["p_blk"] for r in K1R if 4 in r["blk"]]),
         N_RAY_POS, len(K1R), BEST_BLK["ls_lo"], BEST_BLK["J"],
         BEST_BLK["pr_lo"], BEST_BLK["pr_hi"],
         qmin(P1) / max(BEST_BLK["ls_lo"], 1.0e-300), qmin(P1)))

para("""K1.4  ROUTE (iii), THE T146 RESOLVENT / COLUMN ROUTE, AND ITS ONE
THEOREM.  Write gam = T e_1 for the parity coordinates of the bottom
eigenvector, C = T A T^T = Lam^{1/2} B Lam^{1/2}, and split the modes at kb = %d.
The eigen-equation C gam = lam_1 gam gives the FIXED-SIZE null problem
    [ C_LL - lam_1 - C_LH (C_HH - lam_1)^-1 C_HL ] gam_L = 0 ,
a kb x kb object whose size does NOT grow with m, and p_1 = gam_1^2 =
ghat_1^2 ||gam_L||^2 with ghat the unit bottom vector of that problem.  THE TAIL
IS A THEOREM, one line from the pencil floor alone: A >= t L_P gives
    lam_1 = e_1^T A e_1 >= t sum_k mu^P_k gam_k^2 >= t mu^P_{kb+1} ||gam_H||^2 ,
so ||gam_H||^2 <= lam_1 / (t mu^P_{kb+1}) <= (kap / t) / rho_{kb+1} -- the ``98
per cent in the sine block'' fact of T146, now with a proof and an m-free
number.  DIRECTION: the tail is bounded ABOVE and is SUBTRACTED, so
p_1 >= ghat_1^2 (1 - tail) is a LOWER bound.""" % SCHUR_KB)

TAILT = [r["tail_thm"] for r in K1R]
TAILF = [r["tail_mfree"] for r in K1R]
TAILK = [r["tail_mfree_kap"] for r in K1R]
F_TAILF = pow_fit(XH, TAILF, "tail m-free")
TL_DIR = [r["tail_meas"] <= r["tail_thm"] + 1.0e-12 for r in K1R]
TL_DIR2 = [r["tail_thm"] <= r["tail_mfree"] + 1.0e-12 for r in K1R]
check("af_k1.route3_tail_is_a_theorem",
      all(TL_DIR) and all(TL_DIR2) and qmax(TAILF) < 0.10 and flat_ok(F_TAILF),
      "*** THE TAIL BOUND IS A THEOREM, IT IS m-FREE, AND IT IS WORTH A FEW PER "
      "CENT. ***  The measured tail 1 - ||gam_L||^2 is %.3e .. %.3e, the "
      "certified bound lam_1 / (t mu^P_%d) is %.4f .. %.4f, and its m-free "
      "substitution (S/t) / rho_%d is %.4f .. %.4f (%s, FLAT); both directions "
      "hold on %d of %d and %d of %d windows.  Substituting kap for the LADDER "
      "S would give %.1f .. %.1f, i.e. vacuum -- the choice of ceiling is the "
      "whole difference.  SO e_1(A) LIVES TO %.1f .. %.1f PER CENT INSIDE THE "
      "FIRST %d PARITY SINES, m-FREELY: T146's ``98 per cent in the sine "
      "block'' now has a one-line proof from the pencil floor alone"
      % (qmin([r["tail_meas"] for r in K1R]),
         qmax([r["tail_meas"] for r in K1R]), SCHUR_KB + 1, qmin(TAILT),
         qmax(TAILT), SCHUR_KB + 1, qmin(TAILF), qmax(TAILF),
         fit_str(F_TAILF), sum(TL_DIR), len(TL_DIR), sum(TL_DIR2),
         len(TL_DIR2), qmin(TAILK), qmax(TAILK), 100.0 * (1.0 - qmax(TAILF)),
         100.0 * (1.0 - qmin(TAILF)), SCHUR_KB))

P1RES = [r["p1_res_mfree"] for r in K1R]
GH = [r["ghat1_sq"] for r in K1R]
F_GH = pow_fit(XH, GH, "ghat_1^2")
RES_DIR = [r["p1_res_mfree"] <= r["p1"] + 1.0e-9 for r in K1R]
check("af_k1.route3_reduces",
      all(RES_DIR) and qmin(P1RES) > 0.15 and flat_ok(F_GH),
      "AND THE REDUCTION IS FAITHFUL: ghat_1^2 = %.4f .. %.4f (%s, FLAT), the "
      "resolvent floor ghat_1^2 (1 - tail) = %.4f .. %.4f is BELOW the measured "
      "p_1 = %.4f .. %.4f on %d of %d windows, and the fixed-size null problem "
      "is solved to a relative residual %.1e.  ROUTE (iii) THEREFORE MOVES THE "
      "p_1 DEBT FROM AN m-SIZED EIGENVECTOR TO A %d x %d MATRIX -- it does not "
      "close it, because the entries of that matrix are still MEASURED"
      % (qmin(GH), qmax(GH), fit_str(F_GH), qmin(P1RES), qmax(P1RES),
         qmin(P1), qmax(P1), sum(RES_DIR), len(RES_DIR),
         qmax([r.get("S16_resid", float("nan")) for r in K1R]),
         SCHUR_KB, SCHUR_KB))

# --- the four routes, side by side, against the one number that matters -----
for r in K1R:
    r["r_ceil_schur"] = (1.0 / r["Ls_schur"] if np.isfinite(r["Ls_schur"])
                         and r["Ls_schur"] > 0.0 else float("nan"))
    r["d1_at_p1"] = loss_PR(r["P"], r["r_ceil_p1"])
    r["d1_at_schur"] = loss_PR(r["P"], r["r_ceil_schur"])
    r["d1_true_r"] = loss_PR(r["P"], r["r"])
check("af_k1.best_route_is_the_resolvent",
      qmin(P1RES) > qmin(LSS) and qmin(P1RES) > qmin(LSCS)
      and qmin(P1RES) / qmin(P1) > 0.90,
      "*** THE K1 SCOREBOARD, AND THE WINNER IS ROUTE (iii). ***  Against the "
      "measurement p_1 >= %.4f (L s = %.4f .. %.4f): route (0) Cauchy-Schwarz "
      "%.3e, REFUTED, loses exactly the factor P; route (i) one-block Rayleigh "
      "EMPTY, numerator negative on every window; route (ii) block Rayleigh "
      "EMPTY at every J of the ladder, its block-mass form valid at %.4f (J = "
      "%d) but losing to e_1; route (0b) the Schur entry -- RIGHT SHAPE, O(1) "
      "and flat, WRONG certificate, floor %.3e; route (iii) THE RESOLVENT, "
      "p_1 >= %.4f .. %.4f, which is %.1f per cent of the measured p_1 and the "
      "ONLY route whose loss against the measurement is a few per cent instead "
      "of orders of magnitude.  ITS ANATOMY: one THEOREM (the %.1f .. %.1f per "
      "cent sine-block confinement, from the pencil floor alone) times ONE "
      "FIXED-SIZE MEASURED NUMBER (ghat_1^2, the first coordinate of the "
      "bottom vector of a %d x %d Schur null problem)"
      % (qmin(P1), qmin([r["Ls"] for r in K1R]), qmax([r["Ls"] for r in K1R]),
         qmin(LSCS), BEST_BLK["ls_lo"] if BEST_BLK else float("nan"),
         BEST_BLK["J"] if BEST_BLK else -1, qmin(LSS), qmin(P1RES),
         qmax(P1RES), 100.0 * qmin(P1RES) / qmin(P1),
         100.0 * (1.0 - qmax(TAILF)), 100.0 * (1.0 - qmin(TAILF)),
         SCHUR_KB, SCHUR_KB))
info("K1.5.loss_at_the_ceilings",
     "and what each ceiling costs in the loss F(P, r): r measured %.4f .. "
     "%.4f gives F = %.4f .. %.4f (T156 truth %.3f .. %.3f); r <= 1/p_1 gives "
     "F = %.4f .. %.4f (T156 ceiling %.3f .. %.3f); r <= (S_L)_{11}/L gives "
     "F = %.4f .. %.4f -- the Schur route costs %.4f .. %.4f MORE loss than "
     "the angle route, and every one of them stays strictly below 1"
     % (qmin([r["r"] for r in K1R]), qmax([r["r"] for r in K1R]),
        qmin([r["d1_true_r"] for r in K1R]),
        qmax([r["d1_true_r"] for r in K1R]), T156_TRUE[0], T156_TRUE[1],
        qmin([r["d1_at_p1"] for r in K1R]), qmax([r["d1_at_p1"] for r in K1R]),
        T156_CEIL[0], T156_CEIL[1], qmin([r["d1_at_schur"] for r in K1R]),
        qmax([r["d1_at_schur"] for r in K1R]),
        qmin([r["d1_at_schur"] - r["d1_at_p1"] for r in K1R]),
        qmax([r["d1_at_schur"] - r["d1_at_p1"] for r in K1R])))

print("")
print("TOTAL (K1): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("K2  THE ALIGNMENT ANGLE -- WHERE THE ATOM EXTREMAL LIVES")
# ----------------------------------------------------------------------------
para("""K2.0  WHAT R1'' OWES.  T155 refuted every symbol argument and T156
identified the mechanism: on the bulk block the arch form and the atom form are
BOTH enormous on the minimiser (arch %.2f .. %.2f, atom %.2f .. %.2f) and they
CANCEL to lam_min(B_HH) = %.4f .. %.4f.  So the positivity is an ALIGNMENT fact.
The arch half is DONE as a one-variable statement: inf f^arch(th) / (4 sin^2
(th/2)) clears the target by %.2f .. %.2f with its minimum at th/pi = %.3f ..
%.3f -- the ALTERNATING lag sum.  What is owed is an m-free floor on the arch
Rayleigh quotient ON THE SUBSPACE WHERE THE ATOM FORM IS LARGE.""" % (
    1.47, 91.71, -91.27, -1.12, T156_BHH[0], T156_BHH[1], T156_ARCHFAC[0],
    T156_ARCHFAC[1], T156_THSTAR[0], T156_THSTAR[1]))

K2C = [c for c in CAND if c[3] <= K2_HCAP]
K2S = []
if K2C:
    _st = max(1, len(K2C) // max(K2_ZONES, 1))
    K2S = K2C[::-1][::_st][:K2_ZONES]
    K2S.sort(key=lambda t: t[0])

K2R = []
for (zk, D_k, M_k, h_k) in K2S:
    if budget_left() < 200.0:
        info("K2.0.budget", "K2 surface truncated at %d windows" % len(K2R))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    if m <= 3 * SCHUR_KB:
        continue
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A_ar = sym(odd_toeplitz(sp["c_ar"], M_k))
    A_at = sym(odd_toeplitz(sp["c_at"], M_k))
    B_ar = parity_block(A_ar, Tf, mu)
    B_at = parity_block(A_at, Tf, mu)
    B = sym(B_ar + B_at)
    kb = SCHUR_KB
    N_win = 2 * m + 1
    rec = dict(zk=zk, h=m, n_atom=sp["n_atom"], l1_at=sp["l1_at"],
               x_zone=math.exp(2.0 * alpha))
    HH = sym(B[kb:, kb:])
    HH_ar = sym(B_ar[kb:, kb:])
    HH_at = sym(B_at[kb:, kb:])
    try:
        w_hh, V_hh = eigh(HH, subset_by_index=[0, 0])
        w_ar, V_ar = eigh(HH_ar, subset_by_index=[0, 0])
        w_at, V_at = eigh(HH_at, subset_by_index=[0, 0])
    except (LinAlgError, ValueError):
        del A_ar, A_at, B_ar, B_at, B, HH, HH_ar, HH_at, Tf, sp
        continue
    rec["lo_B"] = cert_lam_min(HH, guess=float(w_hh[0]))
    rec["lo_ar"] = cert_lam_min(HH_ar, guess=float(w_ar[0]))
    rec["nrm_at"] = cert_absnorm(HH_at)
    rec["t"] = schur_best(B, kb)
    # --- (i) WHERE THE THREE EXTREMAL VECTORS LIVE, IN th ------------------
    # A bulk index j corresponds to the parity mode k = kb + 1 + j and hence to
    # the KMS symbol argument th_k = 2 pi k / N -- EXACT, because the t_k are
    # exact eigenvectors of L_P (KMS 1953).  So a bulk vector HAS a th profile
    # and the question ``where does it live'' has an exact answer.
    th_mode = 2.0 * math.pi * (np.arange(kb + 1, m + 1, dtype=float)) / N_win
    for tag, vv in (("min", V_hh[:, 0]), ("ar", V_ar[:, 0]), ("at", V_at[:, 0])):
        w2 = vv ** 2
        w2 = w2 / max(float(np.sum(w2)), 1.0e-300)
        rec["th_peak_%s" % tag] = float(th_mode[int(np.argmax(w2))]) / math.pi
        rec["th_cent_%s" % tag] = float(np.dot(th_mode, w2)) / math.pi
        rec["th_spread_%s" % tag] = math.sqrt(max(0.0, float(
            np.dot((th_mode / math.pi) ** 2, w2)) - rec["th_cent_%s" % tag] ** 2))
    rec["ang_min_at"] = math.degrees(math.acos(min(1.0, abs(float(
        V_hh[:, 0] @ V_at[:, 0])))))
    rec["ang_min_ar"] = math.degrees(math.acos(min(1.0, abs(float(
        V_hh[:, 0] @ V_ar[:, 0])))))
    rec["ang_ar_at"] = math.degrees(math.acos(min(1.0, abs(float(
        V_ar[:, 0] @ V_at[:, 0])))))
    # the decisive number: how big is the ARCH form ON THE ATOM EXTREMAL?
    rec["q_ar_on_min"] = float(V_hh[:, 0] @ (HH_ar @ V_hh[:, 0]))
    rec["q_at_on_min"] = float(V_hh[:, 0] @ (HH_at @ V_hh[:, 0]))
    rec["q_ar_on_at"] = float(V_at[:, 0] @ (HH_ar @ V_at[:, 0]))
    rec["q_at_on_at"] = float(V_at[:, 0] @ (HH_at @ V_at[:, 0]))
    rec["q_sum_on_at"] = rec["q_ar_on_at"] + rec["q_at_on_at"]
    rec["avoid"] = abs(rec["q_at_on_min"]) / max(rec["nrm_at"], 1.0e-300)
    rec["arch_pays"] = (rec["q_ar_on_at"] / max(abs(rec["q_at_on_at"]), 1e-300))
    # --- (ii) THE DOMINATION FORM: does arch - t dominate the NEGATIVE PART
    # of the atom operator?  If  B^arch_HH - t I  >=  (-B^atom_HH)_+  then
    # lam_min(B_HH) >= t follows at once, because B^atom >= -(-B^atom)_+.
    # The ratio is a GENERALISED Rayleigh quotient on the range of the
    # positive part, and it is the exact quantitative form of R1''.
    rec["dom_lad"] = {}
    try:
        w_neg, V_neg = eigh(-HH_at)
        keep = w_neg > 1.0e-10 * max(float(w_neg[-1]), 1.0e-300)
        rec["rank_neg"] = int(np.sum(keep))
        Wn = V_neg[:, keep]
        sg = 1.0 / np.sqrt(w_neg[keep])
        Mid_ar = sym((Wn.T @ (HH_ar @ Wn)) * np.outer(sg, sg))
        Gm = np.diag(sg * sg)
        for t_try in DOM_LADDER:
            Mt = sym(Mid_ar - t_try * Gm)
            v0 = float(eigh(Mt, eigvals_only=True, subset_by_index=[0, 0])[0])
            rec["dom_lad"][t_try] = cert_lam_min(Mt, guess=v0)
        rec["dom_cert"] = rec["dom_lad"][T_TARGET]
        del Wn, Mid_ar, Gm, V_neg, Mt
    except (LinAlgError, ValueError):
        rec["dom_cert"] = float("nan")
        rec["rank_neg"] = -1
    # --- (iii) THE ONE-VARIABLE ARCH STATEMENT, WITH A LIPSCHITZ DECKEL -----
    th_lo = 2.0 * math.pi * (kb + 1) / N_win
    for tag, ng in (("g", 2048), ("f", 8192)):
        th_g = np.linspace(th_lo, math.pi, ng)
        R_ar = symbol_min(sp["c_ar"], M_k, th_g) / (4.0 * np.sin(0.5 * th_g) ** 2)
        rec["sym_arch_%s" % tag] = float(np.min(R_ar))
        rec["th_star_%s" % tag] = float(th_g[int(np.argmin(R_ar))]) / math.pi
    rec["grid_drift"] = abs(rec["sym_arch_f"] - rec["sym_arch_g"])
    ll = np.arange(1, M_k, dtype=float)
    rec["dsum_ar"] = 2.0 * float(np.dot(ll, np.abs(sp["c_ar"][1:M_k])))
    rec["fabs_ar"] = abs(float(sp["c_ar"][0])) + 2.0 * float(
        np.sum(np.abs(sp["c_ar"][1:M_k])))
    rec["lip_lo"] = lip_local(th_lo, rec["dsum_ar"], rec["fabs_ar"])
    rec["lip_pi"] = lip_local(0.5 * math.pi, rec["dsum_ar"], rec["fabs_ar"])
    rec["lip_need"] = rec["lip_lo"] * (math.pi - th_lo) / (
        2.0 * max(rec["sym_arch_f"] - T_TARGET, 1.0e-300))
    ok_c, ne_c, wf_c, nw_c = certified_inf_ratio(
        sp["c_ar"], M_k, th_lo, math.pi, T_TARGET, rec["dsum_ar"],
        rec["fabs_ar"])
    rec.update(cert_ok=ok_c, cert_n=ne_c, cert_floor=wf_c, cert_narrow=nw_c)
    rec["sym_full"] = float(np.min(symbol_min(sp["c"], M_k, np.linspace(
        th_lo, math.pi, 2048)) / (4.0 * np.sin(0.5 * np.linspace(
            th_lo, math.pi, 2048)) ** 2)))
    # --- the ALTERNATING structure at th = pi, exactly ---------------------
    sgn = (-1.0) ** np.arange(M_k)
    rec["alt_ar"] = float(sp["c_ar"][0] + 2.0 * np.dot(sgn[1:], sp["c_ar"][1:]))
    rec["alt_at"] = float(sp["c_at"][0] + 2.0 * np.dot(sgn[1:], sp["c_at"][1:]))
    del A_ar, A_at, B_ar, B_at, B, HH, HH_ar, HH_at, Tf, sp, V_hh, V_ar, V_at
    K2R.append(rec)

check("af_k2.surface", len(K2R) >= 6,
      "%d windows carry the full K2 instrument, h = %d .. %d"
      % (len(K2R), qmin([r["h"] for r in K2R]), qmax([r["h"] for r in K2R])))
XH2 = [r["h"] for r in K2R]
check("af_k2.reproduces_t156",
      qmin([r["lo_B"] for r in K2R]) > 0.0
      and qmax([r["sym_full"] for r in K2R]) < 0.0,
      "T156 REPRODUCED ON THE BULK: lam_min(B_HH) = %.4f .. %.4f (quoted %.4f "
      ".. %.4f) is POSITIVE while the FULL pencil symbol infimum is %.1f .. "
      "%.1f, NEGATIVE on every window -- so the finite-section cancellation, "
      "and not any symbol bound, is still what carries the block"
      % (qmin([r["lo_B"] for r in K2R]), qmax([r["lo_B"] for r in K2R]),
         T156_BHH[0], T156_BHH[1], qmin([r["sym_full"] for r in K2R]),
         qmax([r["sym_full"] for r in K2R])))

para("""K2.1  WHERE THE THREE EXTREMAL VECTORS LIVE, IN th, EXACTLY.  Because the
parity sines are EXACT eigenvectors of L_P (KMS 1953), a bulk index j is the
parity mode k = kb + 1 + j and hence the exact symbol argument th_k = 2 pi k / N.
So the question ``where does the atom extremal live'' has an exact answer in the
same variable in which the arch infimum sits, and the two can be compared
without any asymptotics.  The arch infimum sits at th / pi = %.3f .. %.3f -- the
ALTERNATING lag sum.  If the atom extremal sat elsewhere, the separation would
be a statement about LAG SUPPORTS and therefore a theorem candidate.""" % (
    T156_THSTAR[0], T156_THSTAR[1]))

for tag, nm in (("min", "the bulk minimiser"), ("ar", "the arch extremal"),
                ("at", "the atom extremal")):
    info("K2.1.where",
         "%-20s th_peak/pi = %.4f .. %.4f, th_centroid/pi = %.4f .. %.4f, "
         "spread %.4f .. %.4f"
         % (nm, qmin([r["th_peak_%s" % tag] for r in K2R]),
            qmax([r["th_peak_%s" % tag] for r in K2R]),
            qmin([r["th_cent_%s" % tag] for r in K2R]),
            qmax([r["th_cent_%s" % tag] for r in K2R]),
            qmin([r["th_spread_%s" % tag] for r in K2R]),
            qmax([r["th_spread_%s" % tag] for r in K2R])))

TH_AT = [r["th_peak_at"] for r in K2R]
TH_AR = [r["th_peak_ar"] for r in K2R]
TH_MIN = [r["th_peak_min"] for r in K2R]
SEP = [abs(r["th_peak_at"] - r["th_peak_ar"]) for r in K2R]
check("af_k2.the_atom_extremal_lives_at_low_theta",
      qmax(TH_AT) < 0.5 and qmin(TH_AR) > 0.95 and qmin(SEP) > 0.5
      and qmin([r["ang_min_ar"] for r in K2R]) > 85.0,
      "*** AND THE ANSWER IS SHARP: THE TWO EXTREMALS ARE AT OPPOSITE ENDS OF "
      "THE BAND. ***  The arch extremal sits at th/pi = %.4f .. %.4f -- the "
      "ALTERNATING end, where the one-variable infimum lives, with a th spread "
      "of only %.1e.  The ATOM extremal sits at th/pi = %.4f .. %.4f, i.e. at "
      "the LOW end, and the separation is %.4f .. %.4f in th/pi.  THE BULK "
      "MINIMISER GOES WITH THE ATOM, NOT WITH THE ARCH: it peaks at th/pi = "
      "%.4f .. %.4f and stands %.1f .. %.1f deg away from the arch extremal "
      "while being only %.1f .. %.1f deg from the atom extremal.  THIS IS THE "
      "MECHANISM, AND IT IS THE OPPOSITE OF WHAT AN INFIMUM ARGUMENT ASSUMES: "
      "the arch Rayleigh quotient f^arch/(4 sin^2(th/2)) is SMALLEST at th = pi "
      "and GROWS as th falls, because the denominator vanishes there -- so on "
      "the low-th region where the atom form is large the arch form is large "
      "too, and THAT is what pays for it.  A proof of R1'' must therefore use "
      "the GROWTH of the arch ratio at small th and not its infimum, and the "
      "T156 one-variable infimum at th = pi is the WRONG number to feed it"
      % (qmin(TH_AR), qmax(TH_AR), qmax([r["th_spread_ar"] for r in K2R]),
         qmin(TH_AT), qmax(TH_AT), qmin(SEP), qmax(SEP), qmin(TH_MIN),
         qmax(TH_MIN), qmin([r["ang_min_ar"] for r in K2R]),
         qmax([r["ang_min_ar"] for r in K2R]),
         qmin([r["ang_min_at"] for r in K2R]),
         qmax([r["ang_min_at"] for r in K2R])))

para("""K2.2  THE QUANTITATIVE FASSUNG, AND IT IS NOT A cos^2 phi.  The shape
    lam_min(B_HH) >= inf_arch cos^2 phi - ||atom on the minimiser||
CANNOT be the right one, and the reason is a number: on the minimiser the arch
form is NOT near its infimum, it is ENORMOUS, and that is exactly how the atom
is paid for.  The honest sufficient condition is a DOMINATION statement,
    B^arch_HH - t I  >=  (- B^atom_HH)_+ ,
which implies lam_min(B_HH) >= t at once because B^atom >= -(-B^atom)_+ .  Its
exact strength is the generalised Rayleigh quotient of the pair on the range of
the positive part, and that single number IS R1'' in quantitative form.
DIRECTION: the quotient must be >= 1, and it is a LOWER bound that is
certified by one Cholesky after the whitening.""")

DOM = [r["dom_cert"] for r in K2R]
ARCHPAY = [r["arch_pays"] for r in K2R]
DOM_ROWS = []
for t_try in DOM_LADDER:
    vals = [r["dom_lad"].get(t_try, float("nan")) for r in K2R]
    f_t = pow_fit(XH2, vals, "dom %.2f" % t_try)
    row = dict(t=t_try, lo=qmin(vals), hi=qmax(vals), fit=f_t,
               n_ok=sum(1 for v in vals if np.isfinite(v) and v >= 1.0),
               nogrow=nogrow_ok(f_t), rising=bool(np.isfinite(f_t["p"])
                                                 and f_t["p"] > 0.0))
    DOM_ROWS.append(row)
    info("K2.2.ladder",
         "target t = %.2f: domination quotient %.4f .. %.4f (%s), clears 1 on "
         "%d of %d windows, margin at the largest window %.4f"
         % (t_try, row["lo"], row["hi"], fit_str(f_t), row["n_ok"], len(K2R),
            K2R[-1]["dom_lad"].get(t_try, float("nan")) - 1.0))
DOM_SAFE = [q for q in DOM_ROWS if q["n_ok"] == len(K2R) and q["lo"] >= 1.05
            and q["rising"]]
BEST_DOM = DOM_SAFE[0] if DOM_SAFE else None
check("af_k2.domination_is_the_right_form",
      all(np.isfinite(r["dom_cert"]) for r in K2R)
      and DOM_ROWS[0]["n_ok"] == len(K2R),
      "*** THE DOMINATION NUMBER, AND IT DECIDES R1'' -- WITH A MARGIN THAT HAS "
      "TO BE READ CAREFULLY. ***  At the chain target t = %.2f the certified "
      "generalised quotient min x^T (B^arch_HH - t I) x / x^T (-B^atom_HH)_+ x, "
      "taken over the range of the positive part (rank %d .. %d of the bulk), "
      "is %.4f .. %.4f (%s) and clears 1 on %d of %d windows.  SO THE "
      "SUFFICIENT CONDITION HOLDS ON THE WHOLE SURFACE -- and the margin at the "
      "largest window is only %.1e, with the trend %s, so this is a CERTIFIED "
      "PER-WINDOW statement and NOT a uniform one: at t = %.2f the domination "
      "is a coin flip one window further out.  %s  On the atom extremal the "
      "arch form pays %.3f .. %.3f times the atom form it must cover"
      % (T_TARGET, min(r["rank_neg"] for r in K2R),
         max(r["rank_neg"] for r in K2R), qmin(DOM), qmax(DOM),
         fit_str(DOM_ROWS[0]["fit"]), DOM_ROWS[0]["n_ok"], len(K2R),
         K2R[-1]["dom_lad"].get(T_TARGET, float("nan")) - 1.0,
         fit_str(DOM_ROWS[0]["fit"]), T_TARGET,
         ("THE LADDER RESCUES IT AT A SMALLER CONSTANT: at t = %.2f the "
          "quotient is %.4f .. %.4f, above 1.05 on every window and RISING in "
          "h, which is a certified UNIFORM statement of the same kind as the "
          "arch one-variable infimum" % (BEST_DOM["t"], BEST_DOM["lo"],
                                        BEST_DOM["hi"])) if BEST_DOM else
         "AND NO TARGET OF THE LADDER TURNS IT INTO A RISING, COMFORTABLE "
         "STATEMENT: every target either fails on a window or has a shrinking "
         "margin, so R1'' stays a per-window certificate.",
         qmin(ARCHPAY), qmax(ARCHPAY)))

info("K2.2.anatomy",
     "the anatomy on the minimiser, reproduced: arch %.2f .. %.2f and atom "
     "%.2f .. %.2f cancel to %.4f .. %.4f; the minimiser sees a fraction "
     "%.2e .. %.2e of the atom operator norm %.2f .. %.2f (T156 quoted "
     "%.1e .. %.2f), at %.1f .. %.1f deg from the atom extremal and %.1f .. "
     "%.1f deg from the arch extremal"
     % (qmin([r["q_ar_on_min"] for r in K2R]),
        qmax([r["q_ar_on_min"] for r in K2R]),
        qmin([r["q_at_on_min"] for r in K2R]),
        qmax([r["q_at_on_min"] for r in K2R]),
        qmin([r["lo_B"] for r in K2R]), qmax([r["lo_B"] for r in K2R]),
        qmin([r["avoid"] for r in K2R]), qmax([r["avoid"] for r in K2R]),
        qmin([r["nrm_at"] for r in K2R]), qmax([r["nrm_at"] for r in K2R]),
        T156_AVOID[0], T156_AVOID[1],
        qmin([r["ang_min_at"] for r in K2R]),
        qmax([r["ang_min_at"] for r in K2R]),
        qmin([r["ang_min_ar"] for r in K2R]),
        qmax([r["ang_min_ar"] for r in K2R])))

para("""K2.3  THE ARCH HALF AS A CERTIFIED STATEMENT: GRID PLUS LIPSCHITZ DECKEL.
The recipe is known and it is the only honest way to turn a grid minimum into a
bound.  For R(th) = f^arch(th) / (4 sin^2(th/2)) on [th_lo, pi],
    |R'(th)| <= (|f'| + R |g'|) / g  <=  (2 sum_l l |c^arch_l| + 2 max R) /
                4 sin^2(th_lo / 2) =: Lip ,
using |f'| <= 2 sum_l l |c_l| and |g'| = |2 sin th| <= 2 and g >= g(th_lo).  A
grid of spacing d then certifies inf R >= min_grid - Lip d / 2, so the number of
points needed to certify inf R >= t is Lip (pi - th_lo) / (2 (min_grid - t)).
THAT NUMBER IS REPORTED, and it is reported whether or not it is affordable.""")

SYA = [r["sym_arch_f"] for r in K2R]
F_SYA = pow_fit(XH2, SYA, "arch infimum")
ARCHFAC = [r["sym_arch_f"] / T_TARGET for r in K2R]
check("af_k2.arch_half_reproduces",
      qmin(ARCHFAC) > 1.0 and nogrow_ok(pow_fit(XH2, [1.0 / a for a in ARCHFAC],
                                                "inv"))
      and qmax([r["grid_drift"] for r in K2R]) < 1.0e-3,
      "THE ARCH HALF, REPRODUCED: inf f^arch / (4 sin^2(th/2)) = %.4f .. %.4f "
      "(%s), clearing the target %.2f by a factor %.2f .. %.2f (T156 quoted "
      "%.2f .. %.2f), grid-stable to %.1e between %d and %d points, with the "
      "minimum at th/pi = %.4f .. %.4f (quoted %.3f .. %.3f).  The value at "
      "th = pi is the ALTERNATING lag sum exactly: c^arch alternating sum = "
      "%.4f .. %.4f, against the atom alternating sum %.4f .. %.4f at the same "
      "point -- the two halves of the th = pi value, and the atom half is the "
      "one that is NOT small"
      % (qmin(SYA), qmax(SYA), fit_str(F_SYA), T_TARGET, qmin(ARCHFAC),
         qmax(ARCHFAC), T156_ARCHFAC[0], T156_ARCHFAC[1],
         qmax([r["grid_drift"] for r in K2R]), 2048, 8192,
         qmin([r["th_star_f"] for r in K2R]), qmax([r["th_star_f"] for r in K2R]),
         T156_THSTAR[0], T156_THSTAR[1], qmin([r["alt_ar"] for r in K2R]),
         qmax([r["alt_ar"] for r in K2R]), qmin([r["alt_at"] for r in K2R]),
         qmax([r["alt_at"] for r in K2R])))

LIPN = [r["lip_need"] for r in K2R]
F_LIPN = pow_fit(XH2, LIPN, "grid needed")
N_CERT = sum(1 for r in K2R if r["cert_ok"])
F_CN = pow_fit(XH2, [r["cert_n"] for r in K2R], "adaptive evals")
check("af_k2.lipschitz_deckel_executed",
      N_CERT == len(K2R) and qmin([r["cert_floor"] for r in K2R]) >= T_TARGET,
      "*** AND THE LIPSCHITZ DECKEL IS EXECUTED, NOT ASSERTED -- SO THE ARCH "
      "HALF IS NOW A CERTIFICATE. ***  The certified Lipschitz constant of R on "
      "[th_lo, pi] is %.3e at th_lo and %.3e at pi/2, driven by sum_l l "
      "|c^arch_l| = %.3e .. %.3e; a UNIFORM grid at the th_lo constant would "
      "need %.3e .. %.3e points (%s), which is why the deckel is run "
      "ADAPTIVELY with the LOCAL constant: interval bisection accepting [a, b] "
      "as soon as R(mid) - lip(a) (b-a)/2 >= %.2f.  IT SUCCEEDS ON %d OF %d "
      "WINDOWS "
      "with %d .. %d symbol evaluations (%s), a certified floor of %.4f .. "
      "%.4f, and a narrowest interval of %.2e.  The 1.4e-5 grid stability T156 "
      "reported was EVIDENCE; this is a CERTIFICATE, and it is the first time "
      "the arch half carries one"
      % (qmax([r["lip_lo"] for r in K2R]), qmax([r["lip_pi"] for r in K2R]),
         qmin([r["dsum_ar"] for r in K2R]), qmax([r["dsum_ar"] for r in K2R]),
         qmin(LIPN), qmax(LIPN), fit_str(F_LIPN), T_TARGET, N_CERT, len(K2R),
         min(r["cert_n"] for r in K2R), max(r["cert_n"] for r in K2R),
         fit_str(F_CN), qmin([r["cert_floor"] for r in K2R]),
         qmax([r["cert_floor"] for r in K2R]),
         qmin([r["cert_narrow"] for r in K2R])))

print("")
print("TOTAL (K2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("K3  THE ASSEMBLY, THE UNIFORMITY BALANCE, AND THE OBLIGATORY STRESS")
# ----------------------------------------------------------------------------
para("""K3.1  THE END TO END, PRICED LIKE FOR LIKE.  The chain is unchanged from
T156 except in ONE place: the first row of G is replaced by what route (iii)
gives it, i.e. ||G_1||^2 >= 1 - F(P, 1/p_1^{(iii)}).  DIRECTION CHECK, and it is
the one that matters: shrinking ||G_1|| can only INCREASE
lam_max(M^{1/2}(I - G G^T) M^{1/2}) and therefore only LOWER the complement
floor, so the substitution is CONSERVATIVE and the resulting number is a valid
lower bound.  Everything else -- the eleven other rows of G, the Temple residual,
the Schur floor t -- is carried over verbatim, so the two end-to-end numbers can
be compared.""")

SH_T = [r["share_true"] for r in K1R]
SH_S = [r["share_sub"] for r in K1R]
D1B = [r["d1_bound"] for r in K1R]
D1T = [r["d1_true"] for r in K1R]
LC_T = [r["Lc12"] for r in K1R]
LC_S = [r["Lc12_sub"] for r in K1R]
F_SHS = pow_fit(XH, SH_S, "share sub")
DIR_SUB = [r["Lc12_sub"] <= r["Lc12"] + 1.0e-9 for r in K1R]
check("af_k3.substitution_direction", all(DIR_SUB),
      "the conservative direction holds on %d of %d windows: the substituted "
      "complement floor %.4f .. %.4f never exceeds the measured one %.4f .. "
      "%.4f, so no part of the end to end below is bought by a wrong sign"
      % (sum(DIR_SUB), len(DIR_SUB), qmin(LC_S), qmax(LC_S), qmin(LC_T),
         qmax(LC_T)))

check("af_k3.end_to_end",
      qmin(SH_S) >= FRAC_BAR and all(DIR_SUB),
      "*** THE END TO END, WITH ROUTE (iii) IN PLACE OF THE MEASURED ANGLE. "
      "***  d_1 is MEASURED %.4f .. %.4f and BOUNDED by %.4f .. %.4f through "
      "F(P, 1/p_1^{(iii)}); the complement floor goes from %.4f .. %.4f to "
      "%.4f .. %.4f mu^P_1; the Temple step then recovers %.3e .. %.3e of "
      "lam_1(A) against %.3e .. %.3e unsubstituted, %s by the bar %.1e, with "
      "the trend %s.  SO THE SUBSTITUTION COSTS A FACTOR %.2f .. %.2f AND DOES "
      "NOT DESTROY THE CHAIN.  WHAT THIS NUMBER IS NOT: it is the Temple "
      "recovery of THIS three-space chain and NOT the fully assembled T155 / "
      "T156 end to end (%.2e .. %.2e), which carries collapse pricing this file "
      "does not rebuild; only the substituted and unsubstituted forms HERE are "
      "compared, and the Temple step saturates at beta = t times the complement "
      "floor on the wider windows"
      % (qmin(D1T), qmax(D1T), qmin(D1B), qmax(D1B), qmin(LC_T), qmax(LC_T),
         qmin(LC_S), qmax(LC_S), qmin(SH_S), qmax(SH_S), qmin(SH_T),
         qmax(SH_T), "SURVIVING" if qmin(SH_S) >= FRAC_BAR else "BELOW",
         FRAC_BAR, fit_str(F_SHS),
         qmin([r["share_true"] / max(r["share_sub"], 1e-300) for r in K1R]),
         qmax([r["share_true"] / max(r["share_sub"], 1e-300) for r in K1R]),
         T156_E2E[0], T156_E2E[1]))

para("""K3.2  THE COMPLETE UNIFORMITY BALANCE.  Every step of the chain is listed
with its label, and the label is the one the numbers earn and not the one the
narrative would like.  THEOREM = valid for every m.  CERT-UNIF = a certified
statement whose value is bounded on the whole surface AND whose trend is flat or
improving, i.e. the strongest thing short of a theorem.  CERT-WINDOW = certified
for that window only, with no uniform statement.  MEASURED = read from a
diagonalisation.  The goal T157 was set is MEASURED <= 1.""")

BAL_ROWS = [
    ("the zone geometry: log(1+1/n) <= g <= log 2", "THEOREM",
     "arithmetic, %d gaps" % NZ_DEEP),
    ("psi(x) <= %.5f x on the range used" % B_PSI, "THEOREM",
     "Chebyshev 1852 / RS 1962, verified at every jump"),
    ("mu^P_k = 4 sin^2(pi k/N) and the t_k are exact eigenvectors", "THEOREM",
     "KMS 1953, machine-exact in K3.4"),
    ("rho_k increasing in N, floors of K0.2", "THEOREM",
     "sin(kx)/sin(x) decreasing, checked on %d windows" % len(K1R)),
    ("F(P, r) closes the loss in two scalars", "THEOREM",
     "T156 identity, re-checked here"),
    ("r <= 1/(L s)", "THEOREM", "||A^-1|| = 1/lam_1"),
    ("L s >= L / a_hat (Cauchy-Schwarz)", "THEOREM",
     "valid, and WORTHLESS: loses the factor P = 10^3 .. 10^6"),
    ("1/s = (S_L)_{11}, one entry of the fixed-size Schur complement",
     "THEOREM", "%.4f .. %.4f, FLAT" % (qmin(S11E), qmax(S11E))),
    ("||gam_H||^2 <= lam_1/(t mu^P_{kb+1}) <= (S/t)/rho_{kb+1}", "THEOREM",
     "%.4f .. %.4f: the sine-block confinement" % (qmin(TAILF), qmax(TAILF))),
    ("the pencil floor t on the bulk (Schur 1917)", "CERT-WINDOW",
     "%.4f .. %.4f" % (qmin([r["t"] for r in K1R]),
                       qmax([r["t"] for r in K1R]))),
    ("the ladder ceiling S: lam_k <= S mu^P_k", "CERT-UNIF",
     "%.4f .. %.4f, %s" % (qmin(SLAD), qmax(SLAD), fit_str(F_SLAD))),
    ("inf f^arch/(4 sin^2(th/2)) >= %.2f, Lipschitz deckel EXECUTED" % T_TARGET,
     "CERT-UNIF", "%d of %d windows, %d .. %d evaluations"
     % (N_CERT, len(K2R), min(r["cert_n"] for r in K2R),
        max(r["cert_n"] for r in K2R))),
    ("B^arch_HH - t I >= (-B^atom_HH)_+  (the R1'' domination)", "CERT-WINDOW",
     "%.4f .. %.4f, margin %.1e at the largest window, trend %s"
     % (qmin(DOM), qmax(DOM),
        K2R[-1]["dom_lad"].get(T_TARGET, float("nan")) - 1.0,
        fit_str(DOM_ROWS[0]["fit"]))),
    ("ghat_1^2, the first coordinate of the %d x %d Schur null vector"
     % (SCHUR_KB, SCHUR_KB), "MEASURED",
     "%.4f .. %.4f, %s" % (qmin(GH), qmax(GH), fit_str(F_GH))),
    ("d_2 .. d_12, the other eleven rows of G", "MEASURED",
     "median d_2 = %.3f, median d_12 = %.3f"
     % (qmed([r["dk"][1] for r in K1R]), qmed([r["dk"][11] for r in K1R]))),
    ("the 2-dim model dominating the 8-dim defect (T156)", "MEASURED",
     "REFUTED as a theorem by the T156 no-go stress; carried over unchanged"),
]
for nm, lab, det in BAL_ROWS:
    info("K3.2.balance", "%-11s %-62s %s" % (lab, nm, det))
N_MEAS = sum(1 for _n, lab, _d in BAL_ROWS if lab == "MEASURED")
N_CW = sum(1 for _n, lab, _d in BAL_ROWS if lab == "CERT-WINDOW")
N_CU = sum(1 for _n, lab, _d in BAL_ROWS if lab == "CERT-UNIF")
N_TH = sum(1 for _n, lab, _d in BAL_ROWS if lab == "THEOREM")
check("af_k3.balance_counted", N_TH >= 8,
      "*** THE BALANCE: %d THEOREM steps, %d CERT-UNIF, %d CERT-WINDOW, %d "
      "MEASURED. ***  T156 had 2 terms and both were MEASURED angles.  T157 "
      "turns ONE of them (the sine-block confinement) into a THEOREM and ONE "
      "grid observation (the arch infimum) into an executed CERTIFICATE, and it "
      "leaves %d MEASURED steps -- above the target of 1.  The MEASURED steps "
      "are now all FIXED-SIZE, which is a change of shape and not a change of "
      "status" % (N_TH, N_CU, N_CW, N_MEAS, N_MEAS))

para("""K3.3  THE OBLIGATORY STRESS.  THE T145 NO-GO FAMILY is c_l = 1/(1 + l),
the lag vector of a kernel with a LOGARITHMIC singularity at the origin instead
of a vanishing one.  Its odd section is positive definite, so every instrument
RUNS on it -- which is the point.  T156 established the reference: p_1 collapses
like x^{%.3f} there while it is FLAT on the real family.  THE NEW QUESTION IS
WHETHER T157's NEW INSTRUMENTS BREAK TOO: the ladder ceiling S, the sine-block
confinement, the Schur entry (S_L)_{11} and the resolvent floor.  An instrument
that looked the same on both families would be measuring nothing.""" % (
    T156_NOGO_P1,))


def instrument(A, m, tag):
    """THE WHOLE K1 CHAIN ON AN ARBITRARY POSITIVE SECTION -- the stress
    instrument.  Every K1 number is recomputed here from scratch."""
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
        w_lo, V_lo = eigh(A, subset_by_index=[0, 1])
        t1 = np.ascontiguousarray(Tf[0, :])
        Ai = cho_solve(fac, t1, check_finite=False)
    except (LinAlgError, ValueError):
        return None
    out["lam1"] = float(w_lo[0])
    out["L"] = out["lam1"] / out["mu1"]
    out["a_hat"] = float(t1 @ (A @ t1)) / out["mu1"]
    out["s"] = out["mu1"] * float(t1 @ Ai)
    out["S11"] = 1.0 / max(out["s"], 1.0e-300)
    out["p1"] = float(t1 @ V_lo[:, 0]) ** 2
    out["Ls"] = out["L"] * out["s"]
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    g1 = green_cols(A, LP, V0, 1, fac=fac)
    if g1 is None:
        return None
    Q16 = append_orth(orth_cols(V0), g1)
    out["S_lad"] = cert_ceiling(sym(Q16.T @ (A @ Q16)), mu, K_CERT)
    out["rho17"] = float(mu[SCHUR_KB] / mu[0])
    out["tail_thm"] = out["lam1"] / (out["t"] * float(mu[SCHUR_KB]))
    out["tail_mfree"] = (out["S_lad"] / out["t"]) / out["rho17"]
    gam = Tf @ V_lo[:, 0]
    out["tail_meas"] = 1.0 - float(np.sum(gam[:SCHUR_KB] ** 2))
    kb = SCHUR_KB
    rt = np.sqrt(mu)
    HHm = sym(B[kb:, kb:] * np.outer(rt[kb:], rt[kb:])
              - out["lam1"] * np.eye(m - kb))
    fh = safe_cho(HHm)
    if fh is not None:
        CHL = B[kb:, :kb] * np.outer(rt[kb:], rt[:kb])
        S16 = sym(B[:kb, :kb] * np.outer(rt[:kb], rt[:kb])
                  - out["lam1"] * np.eye(kb) - CHL.T @ cho_solve(
                      fh, CHL, check_finite=False))
        wS, VS = eigh(S16)
        out["ghat1_sq"] = float(VS[:, int(np.argmin(np.abs(wS)))][0] ** 2)
        del CHL, S16
    else:
        out["ghat1_sq"] = float("nan")
    out["p1_res"] = out["ghat1_sq"] * (1.0 - min(1.0, out["tail_mfree"]))
    del Tf, LP, B, V_lo, Q16, g1, HHm
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
F_NG_S = pow_fit(XN, [g["S_lad"] for g in NG], "no-go S")
F_NG_TL = pow_fit(XN, [g["tail_mfree"] for g in NG], "no-go tail")
F_NG_RES = pow_fit(XN, [g["p1_res"] for g in NG], "no-go resolvent")
F_NG_S11 = pow_fit(XN, [g["S11"] for g in NG], "no-go (S_L)_11")
for g in NG:
    info("K3.3.nogo",
         "m=%4d t=%.4g S=%.4g p1=%.3e Ls=%.4g (S_L)11=%.4g tail(thm)=%.3g "
         "tail(m-free)=%.3g ghat1^2=%.3e p1(res)=%.3e"
         % (g["m"], g["t"], g["S_lad"], g["p1"], g["Ls"], g["S11"],
            g["tail_thm"], g["tail_mfree"], g["ghat1_sq"], g["p1_res"]))

check("af_k3.nogo_breaks_on_every_new_axis",
      len(NG) >= 5 and qmax([g["p1"] for g in NG]) < qmin(P1)
      and not nogrow_ok(F_NG_S) and not nogrow_ok(F_NG_TL)
      and qmax([g["p1_res"] for g in NG]) < qmin(P1RES),
      "*** AND THE NO-GO BREAKS ON EVERY AXIS T157 ADDED. ***  (1) THE T156 "
      "REFERENCE, REPRODUCED: p_1 = %.2e .. %.2e on the no-go family against "
      "%.4f .. %.4f on the real one, COLLAPSING as %s (T156 quoted x^{%.3f}).  "
      "(2) NEW: the LADDER CEILING explodes, S = %.3g .. %.3g (%s) against "
      "%.4f .. %.4f FLAT on the real family -- so the very ceiling T157 uses "
      "in place of kap is the ceiling that separates the families.  (3) NEW: "
      "the SINE-BLOCK CONFINEMENT dies, (S/t)/rho_17 = %.3g .. %.3g (%s) "
      "against %.4f .. %.4f -- the no-go bottom eigenvector is NOT confined to "
      "the first %d parity sines, and the m-free tail bound correctly reports "
      "vacuum there.  (4) NEW: the RESOLVENT FLOOR is IDENTICALLY ZERO there "
      "(%.2e .. %.2e, %s -- the tail bound clips and the product vanishes) "
      "against %.4f .. %.4f on the real family; the route reports its own "
      "vacuum, which is the behaviour a certificate must have.  (5) The Schur "
      "entry (S_L)_{11} = %.3g .. "
      "%.3g (%s) against %.4f .. %.4f flat.  THE FLOOR t = %.3g .. %.3g "
      "SURVIVES on the no-go family, so a probe that looked only at floors "
      "would again have seen nothing"
      % (qmin([g["p1"] for g in NG]), qmax([g["p1"] for g in NG]), qmin(P1),
         qmax(P1), fit_str(F_NG_P1), T156_NOGO_P1,
         qmin([g["S_lad"] for g in NG]), qmax([g["S_lad"] for g in NG]),
         fit_str(F_NG_S), qmin(SLAD), qmax(SLAD),
         qmin([g["tail_mfree"] for g in NG]),
         qmax([g["tail_mfree"] for g in NG]), fit_str(F_NG_TL), qmin(TAILF),
         qmax(TAILF), SCHUR_KB, qmin([g["p1_res"] for g in NG]),
         qmax([g["p1_res"] for g in NG]),
         "ghat_1^2 itself is only %.1e .. %.1e there"
         % (qmin([g["ghat1_sq"] for g in NG]),
            qmax([g["ghat1_sq"] for g in NG])), qmin(P1RES),
         qmax(P1RES), qmin([g["S11"] for g in NG]),
         qmax([g["S11"] for g in NG]), fit_str(F_NG_S11), qmin(S11E),
         qmax(S11E), qmin([g["t"] for g in NG]), qmax([g["t"] for g in NG])))

para("""K3.4  THE EXACTNESS CONTROLS, IN BOTH DIRECTIONS.  The complement
certificate must be EXACT in the two configurations whose answer is known
without it: W = span{t_1..t_8} must return mu^P_{K+1} exactly, and W =
span{t_2..t_13} must return mu^P_1 exactly -- the second is the sharper control,
because it is the configuration in which the certificate is WORTHLESS, and an
instrument that cannot report its own worthlessness is not a certificate.  The
negative control is the DIRICHLET tridiagonal, for which the parity sines are
NOT eigenvectors and the exactness must FAIL, by the predicted 2/sqrt(N).""")

CT = []
for m_c in CTRL_SIZES:
    if m_c > MAX_H or m_c < 3 * K_TWELVE:
        continue
    mu_c = parity_mu(m_c)
    Tc = parity_basis(m_c)
    e_par = float(np.max(np.abs(lap_P_mat(m_c) @ Tc.T - Tc.T * mu_c[None, :])))
    LD = sym(2.0 * np.eye(m_c) - np.eye(m_c, k=1) - np.eye(m_c, k=-1))
    e_dir = float(np.max(np.abs(LD @ Tc.T - Tc.T * mu_c[None, :])))
    W1 = np.ascontiguousarray(Tc[:K_CERT, :].T)
    f1, _m1, _v1 = complement_floor(mu_c, Tc[:K_TWELVE, :] @ W1, K_TWELVE)
    W2 = np.ascontiguousarray(Tc[1:K_TWELVE + 1, :].T)
    f2, _m2, _v2 = complement_floor(mu_c, Tc[:K_TWELVE, :] @ W2, K_TWELVE)
    # THE PARITY CONTROL OF THE K1 IDENTITY: s = (B^-1)_{11} must be EXACT
    Ac = sym(lap_P_mat(m_c) + 0.0)
    Bc = parity_block(Ac, Tc, mu_c)
    fc = safe_cho(Ac)
    t1c = np.ascontiguousarray(Tc[0, :])
    s_c = float(mu_c[0]) * float(t1c @ cho_solve(fc, t1c, check_finite=False))
    Binv11 = float(np.linalg.inv(Bc)[0, 0])
    CT.append(dict(m=m_c, e_par=e_par, e_dir=e_dir,
                   e_pred=2.0 / math.sqrt(2.0 * m_c + 1.0),
                   r1=abs(f1 / float(mu_c[K_CERT]) - 1.0),
                   r2=abs(f2 / float(mu_c[0]) - 1.0),
                   r3=abs(s_c / Binv11 - 1.0), r4=abs(s_c - 1.0)))
    del Ac, Bc, Tc
check("af_k3.controls_exact",
      len(CT) >= 4 and qmax([c["e_par"] for c in CT]) < 1.0e-12
      and qmax([c["r1"] for c in CT]) < 1.0e-9
      and qmax([c["r2"] for c in CT]) < 1.0e-9
      and qmax([c["r3"] for c in CT]) < 1.0e-9
      and qmax([c["r4"] for c in CT]) < 1.0e-9,
      "PARITY EXACTNESS to %.1e on %d sizes; the complement certificate returns "
      "mu^P_9 to a relative %.1e when W = span{t_1..t_8} and mu^P_1 to a "
      "relative %.1e in the WORTHLESS configuration W = span{t_2..t_13}.  AND "
      "THE NEW K1 IDENTITY IS CONTROLLED TOO: s = (B^-1)_{11} to a relative "
      "%.1e, and for A = L_P it returns s = 1 exactly to %.1e -- the "
      "configuration in which t_1 IS the bottom eigenvector and (S_L)_{11} must "
      "equal 1"
      % (qmax([c["e_par"] for c in CT]), len(CT),
         qmax([c["r1"] for c in CT]), qmax([c["r2"] for c in CT]),
         qmax([c["r3"] for c in CT]), qmax([c["r4"] for c in CT])))
check("af_k3.dirichlet_negative",
      qmax([abs(c["e_dir"] / c["e_pred"] - 1.0) for c in CT]) < 0.05,
      "AND THE NEGATIVE CONTROL FAILS AS PREDICTED: against the DIRICHLET "
      "tridiagonal the parity sines are not eigenvectors and the residual is "
      "%.4f .. %.4f against the predicted 2/sqrt(N) = %.4f .. %.4f, agreeing "
      "to a relative %.2e on every size.  The exactness above is therefore a "
      "property of the PARITY boundary condition and not of trigonometry"
      % (qmin([c["e_dir"] for c in CT]), qmax([c["e_dir"] for c in CT]),
         qmin([c["e_pred"] for c in CT]), qmax([c["e_pred"] for c in CT]),
         qmax([abs(c["e_dir"] / c["e_pred"] - 1.0) for c in CT])))

print("")
print("TOTAL (K3): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("K4  MAP V29, THE PROMOTION LIST, THE REST LIST, AND THE VERDICT")
# ----------------------------------------------------------------------------
MAP = [
    ("the pencil floor t on the bulk", "CERT-WINDOW",
     "%.4f .. %.4f, at or above the target %.2f"
     % (qmin([r["t"] for r in K1R]), qmax([r["t"] for r in K1R]), T_TARGET)),
    ("the ladder ceiling S: lam_k(A) <= S mu^P_k", "CERT-UNIF",
     "%.4f .. %.4f, %s -- and NOT kap, which grows like h^2.8"
     % (qmin(SLAD), qmax(SLAD), fit_str(F_SLAD))),
    ("the pencil ceiling kap", "CERT-WINDOW, USELESS AT THE BOTTOM",
     "%.3e .. %.3e, %s: it carries the whole atom mass"
     % (qmin(KAP), qmax(KAP), fit_str(F_KAP))),
    ("F(P, r): the loss in two scalars", "THEOREM",
     "T156, re-checked; P = %.3e .. %.3e so F is effectively F(inf, r)"
     % (qmin([r["P"] for r in K1R]), qmax([r["P"] for r in K1R]))),
    ("r <= 1/(L s)", "THEOREM", "and it is sharp to %.2f .. %.2f against the "
     "measured r" % (qmin([r["r_ceil_p1"] / r["r"] for r in K1R]),
                     qmax([r["r_ceil_p1"] / r["r"] for r in K1R]))),
    ("L s >= L / a_hat: the angle-free route", "THEOREM BUT REFUTED",
     "%.3e .. %.3e, short by the factor P" % (qmin(LSCS), qmax(LSCS))),
    ("p_1 >= (lam_2 - RQ)/(lam_2 - lam_1): the classical angle bound",
     "EMPTY", "negative on %d of %d windows, measured AND m-free" % (len(K1R),
                                                                    len(K1R))),
    ("the BLOCK version of the same bound", "EMPTY AT EVERY J",
     "and the block mass is p_blk(2) = %.4f .. %.4f: t_1 lives in the bottom "
     "PAIR" % (BLK2[0]["p_lo"], BLK2[0]["p_hi"]) if BLK2 else "no data"),
    ("1/s = (S_L)_{11}: R2'' as one entry of a fixed-size matrix", "THEOREM",
     "%.4f .. %.4f, %s -- the NEW SHAPE of the debt"
     % (qmin(S11E), qmax(S11E), fit_str(F_S11E))),
    ("a certified ceiling for that entry without inversion",
     "REFUTED", "Cauchy-Schwarz on b^T B_HH^-1 b is off by %.1e .. %.1e"
     % (qmin([r["schur_tight"] for r in K1R]),
        qmax([r["schur_tight"] for r in K1R]))),
    ("||gam_H||^2 <= (S/t)/rho_17: the sine-block confinement", "THEOREM",
     "%.4f .. %.4f, i.e. e_1(A) is %.1f .. %.1f per cent inside the first %d "
     "sines -- T146's fact, now proved" % (qmin(TAILF), qmax(TAILF),
                                          100.0 * (1.0 - qmax(TAILF)),
                                          100.0 * (1.0 - qmin(TAILF)),
                                          SCHUR_KB)),
    ("p_1 >= ghat_1^2 (1 - tail): the resolvent route", "THEOREM x MEASURED",
     "%.4f .. %.4f, %.1f per cent of the measurement -- THE BEST p_1 ROUTE"
     % (qmin(P1RES), qmax(P1RES), 100.0 * qmin(P1RES) / qmin(P1))),
    ("where the atom extremal lives", "MEASURED, AND IT IS THE MECHANISM",
     "th/pi = %.4f .. %.4f against the arch extremal at %.4f .. %.4f: opposite "
     "ends" % (qmin(TH_AT), qmax(TH_AT), qmin(TH_AR), qmax(TH_AR))),
    ("inf f^arch/(4 sin^2(th/2)) >= t, Lipschitz deckel EXECUTED", "CERT-UNIF",
     "%.4f .. %.4f certified on %d of %d windows in %d .. %d evaluations"
     % (qmin([r["cert_floor"] for r in K2R]),
        qmax([r["cert_floor"] for r in K2R]), N_CERT, len(K2R),
        min(r["cert_n"] for r in K2R), max(r["cert_n"] for r in K2R))),
    ("B^arch_HH - t I >= (-B^atom_HH)_+: R1'' quantified", "CERT-WINDOW",
     "%.4f .. %.4f, holds on %d of %d, margin %.1e at the largest window"
     % (qmin(DOM), qmax(DOM), DOM_ROWS[0]["n_ok"], len(K2R),
        K2R[-1]["dom_lad"].get(T_TARGET, float("nan")) - 1.0)),
    ("lam_min(B_HH) >= inf_arch cos^2 phi - ||atom||", "REFUTED AS A SHAPE",
     "on the minimiser the arch form is %.2f .. %.2f, i.e. NOT near its "
     "infimum" % (qmin([r["q_ar_on_min"] for r in K2R]),
                  qmax([r["q_ar_on_min"] for r in K2R]))),
    ("the additive split ||B^atom_HH||", "REFUTED (T155/T156)",
     "%.2f .. %.2f, divergent in h" % (qmin([r["nrm_at"] for r in K2R]),
                                       qmax([r["nrm_at"] for r in K2R]))),
    ("the full pencil symbol infimum", "REFUTED (T155)",
     "%.1f .. %.1f, negative on every window"
     % (qmin([r["sym_full"] for r in K2R]),
        qmax([r["sym_full"] for r in K2R]))),
    ("the T145 no-go discriminator", "STRESS PASSED ON FIVE AXES",
     "p_1 %s, S %s, tail %s, resolvent identically zero, (S_L)_{11} %s"
     % (fit_str(F_NG_P1), fit_str(F_NG_S), fit_str(F_NG_TL),
        fit_str(F_NG_S11))),
    ("the parity / Dirichlet controls", "EXACT / FAILING AS PREDICTED",
     "%.1e and 2/sqrt(N) to %.1e" % (qmax([c["e_par"] for c in CT]),
                                     qmax([abs(c["e_dir"] / c["e_pred"] - 1.0)
                                           for c in CT]))),
]
for nm, lab, det in MAP:
    info("K4.map", "%-46s %-30s %s" % (nm, lab, det))

para("""K4.1  THE PROMOTION LIST.  T149 .. T156 remain PENDING; nothing in this
file changes their status and nothing here is promoted by this file, which writes
no ledger row, no TeX and no website entry.  T155's 12 x 12 complement
certificate stays noted as an INSTRUMENT candidate.  T157 adds THREE instrument
candidates of the same kind, all fixed-size and all with their directions
checked here: (a) the IDENTITY 1/s = (S_L)_{11}, which restates R2'' as a bound
on one diagonal entry of the Schur complement the chain already forms; (b) the
SINE-BLOCK CONFINEMENT ||gam_H||^2 <= (S/t)/rho_{kb+1}, a one-line theorem from
the pencil floor that replaces T146's measured 98 per cent; (c) the ADAPTIVE
LIPSCHITZ DECKEL, which turns the arch one-variable infimum from a grid
observation into an executed certificate at a cost growing only like h^0.85.
None of the three is a claim about m-freeness of the end to end.""")

REST = [
    "an m-free UPPER bound on ONE number: (S_L)_{11} = %.4f .. %.4f, the (1,1) "
    "entry of the %d x %d Schur complement of B.  Equivalently an m-free LOWER "
    "bound on ghat_1^2 = %.4f .. %.4f.  Cauchy-Schwarz on b^T B_HH^-1 b is "
    "refuted here, so what is needed is a bound that SEES the cancellation in "
    "that one bilinear form"
    % (qmin(S11E), qmax(S11E), SCHUR_KB, SCHUR_KB, qmin(GH), qmax(GH)),
    "an m-free version of the R1'' domination with a margin that does NOT "
    "shrink.  The certified quotient is %.4f .. %.4f with trend %s and a margin "
    "of %.1e at h = %d; the ladder over the target does not help, so the "
    "binding direction is one where BOTH forms are large.  The pointer K2.1 "
    "gives the shape: use the GROWTH of f^arch/(4 sin^2(th/2)) as th falls, not "
    "its infimum at th = pi"
    % (qmin(DOM), qmax(DOM), fit_str(DOM_ROWS[0]["fit"]),
       K2R[-1]["dom_lad"].get(T_TARGET, float("nan")) - 1.0, K2R[-1]["h"]),
    "the T156 debt that T157 did not touch: the 2-dimensional model dominating "
    "the 8-dimensional defect, MEASURED on the real family and REFUTED on the "
    "no-go family.  It is the only remaining MEASURED step that is not "
    "fixed-size in its statement",
]
for i, txt in enumerate(REST, 1):
    para("K4.2.rest %d.  %s" % (i, txt))

# --- THE VERDICT GATES, EVALUATED FROM THE NUMBERS AND NOT FROM THE NARRATIVE
GATE_P1_HONEST = bool(all(RES_DIR) and qmin(P1RES) > 0.15)
# GATE_P1_MFREE: an m-free floor on p_1 would need one on ghat_1^2, and K1
# established that no route on the list supplies one.  The gate is therefore
# FALSE by the K1 numbers and not by assumption -- the two candidate suppliers
# (the Rayleigh angle bound and the Cauchy-Schwarz ceiling on (S_L)_{11}) were
# both refuted with a number.
GATE_P1_MFREE = bool(N1F > 0 or SC_BEAT > 0)
GATE_AL_ARCH = bool(N_CERT == len(K2R))
GATE_AL_MFREE = bool(DOM_ROWS[0]["n_ok"] == len(K2R)
                     and any(q["rising"] and q["lo"] >= 1.05 for q in DOM_ROWS))
N_TERMS = int(not GATE_P1_MFREE) + int(not GATE_AL_MFREE)
if N_TERMS == 0:
    VERDICT = "ANGLES-CARRY"
elif N_TERMS == 1:
    VERDICT = "ONE-TERM-MISSING"
else:
    VERDICT = "ANGLES-RESIST"

check("af_k4.gates_evaluated", True,
      "GATE p_1 m-free = %s (the resolvent route is a THEOREM times a MEASURED "
      "fixed-size number, so NO); GATE p_1 non-trivial = %s (%.4f .. %.4f, "
      "%.1f per cent of the measurement); GATE arch half certified = %s (%d of "
      "%d windows, deckel EXECUTED); GATE alignment m-free = %s (the domination "
      "holds on %d of %d windows but with a %.1e margin and a shrinking trend). "
      " TERMS = %d"
      % (GATE_P1_MFREE, GATE_P1_HONEST, qmin(P1RES), qmax(P1RES),
         100.0 * qmin(P1RES) / qmin(P1), GATE_AL_ARCH, N_CERT, len(K2R),
         GATE_AL_MFREE, DOM_ROWS[0]["n_ok"], len(K2R),
         K2R[-1]["dom_lad"].get(T_TARGET, float("nan")) - 1.0, N_TERMS))

section("VERDICT: %s" % VERDICT)
para("""THE THREE-SENTENCE FAZIT, HONESTLY.  (1) TERMS: still TWO, and neither
angle became m-free -- the p_1 floor is now a THEOREM (the %.1f .. %.1f per cent
sine-block confinement, from the pencil floor alone) TIMES ONE MEASURED
FIXED-SIZE NUMBER ghat_1^2 = %.4f .. %.4f, which is %.1f per cent of the
measurement and therefore tight but not free; and the alignment term is a
CERTIFIED PER-WINDOW domination %.4f .. %.4f whose margin at the largest window
is %.1e and whose trend shrinks, which is a certificate and not a uniform
statement.  (2) MEASURED STEPS: %d -- ghat_1^2, the eleven other rows of G, and
the T156 model-domination step -- above the target of one, but all three are now
FIXED-SIZE in their statement, which is the change T157 bought.  (3) WHAT STANDS
A PRIORI ON THE MEASUREMENT SURFACE, PRECISELY: for every prime-power zone in
frame A with h <= %d, WITHOUT looking at any window, the following hold --
the KMS spectrum and the exactness of the parity sines, the ratio floors rho_k,
the identity F(P, r) with r <= 1/(L s), the identity 1/s = (S_L)_{11}, the
sine-block confinement ||gam_H||^2 <= (S/t)/rho_%d, and the classical
inequalities of Cauchy-Schwarz, Kantorovich, Courant-Fischer, Temple and Schur
that the chain is assembled from; the arch one-variable infimum holds with an
EXECUTED Lipschitz certificate per window; and NOTHING ELSE -- in particular
neither p_1 nor the alignment margin is available before the window is built.""" % (
    100.0 * (1.0 - qmax(TAILF)), 100.0 * (1.0 - qmin(TAILF)), qmin(GH),
    qmax(GH), 100.0 * qmin(P1RES) / qmin(P1), qmin(DOM), qmax(DOM),
    K2R[-1]["dom_lad"].get(T_TARGET, float("nan")) - 1.0, N_MEAS,
    qmax([r["h"] for r in K1R]), SCHUR_KB + 1))

para("""K4.3  THE RH FENCE, LAST AND PROMINENT AGAIN.  Nothing above reads,
generates, approximates or extrapolates a single zero of any L-function; the AST
firewall at the top enforces it and re-passed in K0.  Weil 1952 / Bombieri 2000
was cited as an ADDRESS and never used.  Even if BOTH remaining terms closed
tomorrow, what would stand is a finite-window positivity statement with an
explicit constant on a finite list of prime-power zones in one frame -- not a
statement about zeros, not a statement about all m, and not RH.  The distance
from there to RH is not travelled in this file and is not shortened by it.""")

print("")
print("=" * 78)
print("TOTAL: %d checks, %d failures, %.1f s, verdict %s"
      % (N_CHK, len(FAILS), time.time() - T0, VERDICT))
print("=" * 78)
if FAILS:
    print("FAILURES: %s" % ", ".join(FAILS))
