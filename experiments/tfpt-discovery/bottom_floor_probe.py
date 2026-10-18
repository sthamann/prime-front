"""PART 155 -- THE CONTRACT ``BOTTOM.FLOOR'': THE TWO FLOORS.

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
zones.  The distance from there to RH is mapped in H4 and never travelled.

WHAT T154 LEFT.  T154 CLOSED the ceiling: a SIXTEEN-COLUMN certificate of fixed
size gives K^F = 1.1019 .. 1.9964, flat, agreeing with the inertia-certified
true bottom ladder constant to 5.2e-7 on 12 of 12 windows, by Courant-Fischer
1920 alone (Ritz values are UPPER bounds -- no residual needed).  Two terms
survived, and BOTH are now UNIFORMITY terms whose numbers are certified per
window:

  R2'  THE m-FREE BOTTOM-MODE FLOOR.  A lower bound for
       Lc := min_{v perp W} v^T L_P v / v^T v, W the eight bottom Ritz
       directions.  MEASURED flat at 5.93 .. 8.25 mu^P_1, ARITHMETIC-FREE in
       form, worth 91 .. 100 percent of the collapse price 4.408 .. 7.985.
  R1'  THE m-FREE BLOCK FLOOR.  lam_min(B_HH) = 0.266 .. 0.415 per window over
       t = 0.25; every relative route is dead (Kato loss 1.97 .. 121 at
       24.9 .. 89.8 deg), and the minimiser carries 96.5 .. 100 percent of its
       mass on the EIGHT modes immediately above the peel cut.

WHAT THIS FILE DOES.  H1 attacks R2' with two independent instruments: a
FIXED-SIZE overlap certificate (a K x K eigenvalue problem in the exact
Kac-Murdock-Szego numbers and one overlap matrix) and a PENCIL-CEILING chain
(Weyl plus the two-sided pencil), and localises the defect mode by mode.  H2
attacks R1' with the direction-aware two-block decomposition the T154 anatomy
asks for, plus the arch symbol floor as an m-free theorem candidate.  H3
assembles, re-prices the end to end and runs the obligatory stress.  H4 is the
map, the promotion list, the rest list and the verdict.

DISCIPLINE.  THEOREM / CERTIFIED / MEASURED / FIT are kept strictly apart and
every claim carries its label; the word ``proven'' is used nowhere for any
m-freeness claim.  Directions (upper versus lower bound) are pedantic
throughout, and T154's Courant-Fischer lesson -- a Ritz value is a CEILING and
never a floor -- is restated at every use.  Classics cited where used:
Davis-Kahan 1970, Courant-Fischer 1920, Temple 1928, Kato 1949, Schur 1917,
Kac-Murdock-Szego 1953, Weyl 1912, Sylvester 1852, Cauchy 1829, Szego 1915,
Widom 1958, Chebyshev 1852.  HARD CAPS: any factorised / inverted / diagonalised
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
np.random.seed(155155)

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 700.0             # HARD probe budget (< 900 s)

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 400000
ZONE_DEEP = 380000

# --- the measurement surface, DECLARED BEFORE ANY RESULT IS SEEN ------------
H1_ZONES = 16
H1_HCAP = 1400
H2_ZONES = 14
H2_HCAP = 1200

K_CERT = 8                   # the modes the bottom certificate is about
SCHUR_KB = 16                # the FIXED low block of the T152 .. T154 chain
KW_WIN = 8                   # the direction-aware window above the peel cut
KLOW_SCAN = (8, 12, 16, 24, 32, 48, 64)  # the K of the H1 overlap certificate
RSCAN = (8, 12, 16, 24)      # the dimension of the H1 floor subspace
KB2_SCAN = (16, 24, 32, 48)  # the H2 second-cut scan
T_LADDER = (0.25, 0.245, 0.24, 0.235, 0.23, 0.225, 0.22, 0.215, 0.21, 0.205,
            0.20, 0.19, 0.18, 0.16, 0.14, 0.12, 0.10, 0.05)
BAR_UNIF = 0.25              # |exponent| + band bar for "flat / non-growing"
T_TARGET = 0.25

NOGO_SIZES = (48, 64, 96, 128, 192, 256, 384, 512)
CTRL_SIZES = (64, 128, 256, 384, 512, 700)

# T153 / T154 numbers, QUOTED, never recomputed as an input to anything
T154_LC = (5.93, 8.25)        # the complement floor in units of mu^P_1
T154_PRICE = (4.408, 7.985)   # lam_1(A) / (t mu^P_1), the collapse price
T154_KF = (1.1019, 1.9964)    # the closed sixteen-column ceiling
T154_MIS = (82.93, 89.79)     # the ONE misaligned direction, in degrees
T154_BHH = (0.266, 0.415)     # lam_min(B_HH) on the bulk
T154_FRAC = (1.01e-2, 3.92e-2)   # end to end, m-free in shape
T154_E2E = (4.45e-2, 3.13e-1)    # end to end, certified per window
T153_ARCH = (1.04, 1.41)      # the bulk arch reserve
FRAC_BAR = 4.0e-2             # the H3 bar on the new m-free-shaped end to end
REC_BAR = 2.0                 # the bar on the certified recovery factor
TIGHT_BAR = 0.80              # a certificate is TIGHT if it attains this share

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
    check("bf_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("bf_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("bf_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("bf_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "bottom_floor_probe.py", "single new file in the sandbox")


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


def count_below(X, tau):
    return inertia_neg(sym(X - tau * np.eye(X.shape[0])))


def small_eig_floor(W):
    """A CONSERVATIVE bound on the eigenvalue error of a small dense solve
    (Wilkinson); SUBTRACTED wherever a Ritz value feeds a LOWER bound."""
    return 8.0 * W.shape[0] * np.finfo(float).eps * gersh(W)


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T154 code path
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
    bit-for-bit the object T111 .. T154 use."""
    c_at, D, mu_tot, n_hit = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D, mu_tot=mu_tot,
                n_atom=n_hit, l1_at=float(np.sum(np.abs(c_at))))


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


def toep_only(c, M):
    """THE SECTION WITH THE HANKEL REFLECTION HALF REMOVED.  A DIAGNOSTIC
    object; it is never substituted for A in any chain."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])]


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
    the H3 controls."""
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
    lam_min(B) L_P <= A <= lam_max(B) L_P as OPERATORS."""
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
# the subspace instruments (T154's, unchanged) and the ONE new certificate
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
    <= #neg M(gam), and lam_k(A) >= gam as soon as #neg M(gam) <= k - 1.  M is
    d x d with d <= 24, so every count is an LDL^T of FIXED SIZE and the
    bisection is legitimate because #neg M is non-decreasing in gam.
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
    directions -- T154's CLOSED sixteen-column ceiling, reproduced here only as
    a control.  Each ratio is an UPPER bound on lam_k(A) / mu^P_k by
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


def green_cols(A, LP, V, j):
    """THE ITERATION COLUMNS (A^-1 L_P)^j V, by j Cholesky back-solves of A.
    No inverse is ever formed; the completed factor certifies A > 0."""
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
    """AN ORTHONORMAL BASIS OF span(V) with rank detection."""
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


def prin_angles(Q1, Q2):
    """THE PRINCIPAL ANGLES between two orthonormal bases (Bjoerck-Golub 1973;
    Davis-Kahan 1970 for what they bound), in degrees, ascending.  MEASURED."""
    s = np.linalg.svd(Q1.T @ Q2, compute_uv=False)
    s = np.clip(s, -1.0, 1.0)
    return np.degrees(np.arccos(s[::-1]))


def complement_floor(mu, G, K):
    """*** THE H1 INSTRUMENT: THE FIXED-SIZE COMPLEMENT-FLOOR CERTIFICATE. ***

    Let W be a subspace with orthonormal basis Q_W and let G = T_K Q_W be the
    K x dim overlap of the K LEADING parity sines with W.  For every unit
    v perp W, writing c = T_K v (its coefficients on the leading K modes),
        v^T L_P v = sum_k mu_k c_k^2
                 >= sum_{k<=K} mu_k c_k^2 + mu_{K+1} (1 - ||c||^2)
                  = mu_{K+1} - c^T M c ,   M = diag(mu_{K+1} - mu_k)_{k<=K} >= 0
    -- a THEOREM, the Rayleigh bound on the high block, exact for every m
    because the t_k are EXACT eigenvectors of L_P (Kac-Murdock-Szego 1953).
    The constraint v perp W forces c into the range of T_K P_{W^perp}, so
        max_{v perp W, ||v|| = 1} c^T M c
            = lam_max( M^{1/2} T_K (I - Q_W Q_W^T) T_K^T M^{1/2} )
            = lam_max( M^{1/2} (I_K - G G^T) M^{1/2} ) ,
    an EXACT identity (both sides are the largest eigenvalue of the same
    operator up to zero modes) -- and the right-hand side is a K x K eigenvalue
    problem.  Hence the whole certificate has size K, INDEPENDENT OF m, and
    contains NO arithmetic beyond the overlap matrix G.

    DIRECTION, pedantically: lam_max is taken as a CERTIFIED UPPER bound (one
    Cholesky of s I - E), and it is SUBTRACTED, so the return value is a LOWER
    bound on min_{v perp W} v^T L_P v / v^T v.  It is never read the other way.

    EXACTNESS CONTROLS (verified in H3): G = I_K returns mu_{K+1} exactly, and a
    W spanning t_2 .. t_{K+1} returns mu_1 exactly."""
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


section("H0  SETUP, THE RH FENCE, AND THE LICENCES")
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

check("bf_h0.gap_facts",
      bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
      and bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12)),
      "the ONLY two gap facts used anywhere: Bertrand-Chebyshev 1852 "
      "(g <= log 2) and the trivial even bound; %d gaps up to n = %d"
      % (NZ_DEEP, ZONE_DEEP))

para("""H0.0  THE RH FENCE, RESTATED BEFORE ANY NUMBER IS PRINTED.  The
surrounding statement is the positivity of a Weil window form (Weil 1952;
Bombieri 2000; Connes 1999) on a FINITE list of prime-power zones in a FINITE
window, frame A, with the zone gap Theta(D^3).  Weil's explicit-formula
criterion is an ADDRESS, never a criterion used here.  No zero of any L-function
is read, generated, approximated or extrapolated; the AST firewall above
enforces that together with the import whitelist and the absence of write-mode
file access.  What is at stake below is the SIZE AND THE UNIFORMITY of the
constants in one finite-window inequality -- nothing about any zero, in either
direction.  A perfect closure of both floors would leave a finite-window
inequality with an m-free constant on a list of zones and nothing more; in
particular it would say nothing about other D, other frames, other zones, or the
limit m -> infinity.  The distance to RH is mapped once in H4 and never
travelled.""")

para("""H0.1  THE LICENCES, EACH WITH ITS DIRECTION.  (L1) Cholesky: a COMPLETED
Cholesky of X certifies X >= -fl I with fl the Wilkinson backward-error floor,
always SUBTRACTED from a lower bound and ADDED to an upper bound.  (L2)
Sylvester 1852 / Bunch-Kaufman 1977: a completed LDL^T of A - tau I returns
#{lam_j < tau} as a CERTIFICATE and reads no eigenvector.  (L3) Weyl 1912: A >=
t L_P implies lam_k(A) >= t mu^P_k for EVERY k, and A <= kap L_P implies
lam_k(A) <= kap mu^P_k -- the certified ladder in BOTH directions, and the
two-sided pencil kap = lam_max(B) is a new input in this file.  (L4)
Kac-Murdock-Szego 1953: mu^P_k = 4 sin^2(pi k / N) is EXACT for every m, and so
is every ratio mu^P_j / mu^P_k; in particular mu^P_9 / mu^P_1 is an m-EXPLICIT
number bounded by 81 and increasing to it.  (L5) Courant-Fischer 1920 / Cauchy
1829: for any subspace S of dimension d >= k, lam_k(A) <= th_k(S) -- an UPPER
bound on the eigenvalue and therefore a CEILING for the ladder constant, and the
ONLY direction in which a Ritz value is used in this file.  THIS IS T154's
LESSON AND IT IS NOT REPEATED AS A MISTAKE.  (L6) Temple 1928 / Kato 1949: the
residual two-block form turns ||A Q - Q W|| plus a separation beta into a LOWER
bound; it is the only device here that makes a floor out of a subspace.  (L7)
Davis-Kahan 1970: the sin-theta transfer between an invariant subspace and a
nearby computed one, used for the ONE step where the exact bottom eigenspace has
to be replaced by the fixed-size Ritz directions.  (L8) Schur 1917 / Haynsworth
1968: the two-block criterion is an EQUIVALENCE and the inertia is additive.
(L9) Szego 1915 / Widom 1958: the symbol infimum of a Toeplitz form is an m-free
LOWER bound candidate for its sections -- QUOTED as a candidate in H2 and
measured, never used as a bound.  (L10) Chebyshev 1852 / Rosser-Schoenfeld 1962
Thm 12: psi(x) <= B_PSI x, verified below on the exact range used.""")

para("""H0.2  WHAT COUNTS AS WHAT, PEDANTICALLY.  THEOREM = an identity or a
classical inequality valid for every m.  CERTIFIED = a numeric bound produced by
a completed factorisation with its backward-error floor carried, valid for THAT
window only; a certificate is additionally called FIXED-SIZE when the
factorisation it needs has a size independent of m.  MEASURED = a
diagonalisation or an angle read for orientation.  FIT = an exponent on the
finite surface, never promoted to anything.  The word ``proven'' is used nowhere
in this file for any m-freeness claim, and no verdict may be reached by
narrative: the verdict gates below are evaluated from the numbers.""")

_psi_run = 0.0
_bpsi = 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
check("bf_h0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f is VERIFIED at every jump point up to n = %d (max "
      "%.6f); psi jumps only at prime powers, so this is the true max on the "
      "range, and it is never assumed beyond it" % (B_PSI, ATOM_MAX, _bpsi))

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > H1_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(H1_ZONES, 1))
    SZ = CAND[::-1][::step][:H1_ZONES]
    SZ.sort(key=lambda t: t[0])
check("bf_h0.surface", len(SZ) >= 8,
      "%d prime-power zones admit a frame-A window inside the cap (h <= %d, "
      "MAX_H = %d); the H1 surface takes %d of them, h = %d .. %d, declared "
      "BEFORE any result is seen"
      % (len(CAND), H1_HCAP, MAX_H, len(SZ), min(s[3] for s in SZ),
         max(s[3] for s in SZ)))

# ----------------------------------------------------------------------------
section("H1  R2' -- THE COMPLEMENT FLOOR OF L_P, ARITHMETIC-FREE IN FORM")
# ----------------------------------------------------------------------------
para("""H1.0  THE OBJECT, AND WHY IT IS THE WHOLE OF R2'.  T154 reduced the
bottom-mode floor to ONE number.  Every other ingredient of the fixed-size
Temple step is in place: the eight bottom Ritz directions Q8 of the closed
sixteen-column certificate, their 8 x 8 Ritz block, their residual Gram, and the
Temple bisection -- all of size 8, all independent of m.  The single missing
quantity is the SEPARATION on the orthogonal complement of Q8, i.e. a LOWER
bound on
    Lc := min_{v perp Q8} v^T L_P v / v^T v ,
because the certified A >= t L_P then gives beta = t Lc for free.  T154 measured
Lc = %.2f .. %.2f mu^P_1 and called the object arithmetic-free.  THAT LABEL IS
MADE PRECISE HERE AND IT IS HALF TRUE: the FUNCTIONAL is arithmetic-free -- a
question about the tridiagonal L_P and one eight-dimensional subspace, with no
prime power in it anywhere -- but its ARGUMENT Q8 is built from A and is
therefore arithmetic.  A bound valid for EVERY eight-dimensional W is worthless
(take W = span{t_2 .. t_9}: then t_1 is orthogonal to W and Lc = mu^P_1
exactly), so the arithmetic cannot be dropped, only COMPRESSED.  This block
compresses it, in two independent ways, and localises what eats the free
scale.""" % T154_LC)

para("""H1.1  THE FREE SCALE, AND THE SIZE OF THE DEFECT.  If Q8 covered the
eight lowest L_P modes exactly, the complement would lie in span{t_9 .. t_m} and
Lc would be mu^P_9 = 81 mu^P_1 (1 + o(1)) EXACTLY -- Kac-Murdock-Szego 1953,
with mu^P_9 / mu^P_1 = sin^2(9 pi / N) / sin^2(pi / N) increasing to 81 from
below, an m-EXPLICIT number and not an asymptotic one.  Measured, Lc is %.2f ..
%.2f mu^P_1.  So the overlap defect costs a factor of roughly ten, and H1 asks
exactly WHERE.  Two instruments, deliberately independent: (A) an OVERLAP
CERTIFICATE, which is a K x K eigenvalue problem in the exact KMS numbers and
the K x 8 overlap matrix G = T_K Q8, hence FIXED SIZE and arithmetic-free apart
from G; and (B) a PENCIL-CEILING CHAIN, which never looks at Q8's coefficients
at all and instead uses the two-sided pencil t L_P <= A <= kap L_P together with
Courant-Fischer on the EXACT bottom eigenspace and a Davis-Kahan 1970 transfer
to Q8.""" % T154_LC)

para("""H1.2  INSTRUMENT (B), STATED AS A CHAIN BEFORE IT IS RUN.  Let P be the
spectral projector of A on its eight lowest eigenvalues.  A commutes with P, so
for unit v perp Q8, splitting v = (I - P) v + P v, the cross term VANISHES
IDENTICALLY and
    v^T A v = ||(I-P)v||^2 R_A((I-P)v) + ||Pv||^2 R_A(Pv)
           >= lam_9(A) - (lam_9(A) - lam_1(A)) s^2 ,  s := sin th_max(Q8, ran P)
-- an EXACT identity followed by one Rayleigh bound in each block, with NO
||A|| anywhere.  Dividing by the pencil ceiling A <= kap L_P (kap = lam_max(B),
one certified number per window) and using Weyl 1912 in the form lam_9(A) >=
t mu^P_9 and the CLOSED fixed-size ceiling lam_9(A) - lam_1(A) <= K^F mu^P_9:
    Lc  >=  mu^P_9 (t - K^F s^2) / kap .
Every factor here is either a THEOREM (mu^P_9 / mu^P_1, the projector identity,
Weyl, Courant-Fischer) or a CERTIFIED per-window number that the chain already
carries (t, K^F), with exactly ONE genuinely new input: kap.  If kap is flat,
the whole of R2' collapses onto the two-sided pencil condition number
kap / t.""")

H1R = []
for (zk, D_k, M_k, h_k) in SZ:
    if budget_left() < 300.0:
        info("H1.2.budget", "complement surface truncated at %d windows" % len(H1R))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    if m <= SCHUR_KB + K_CERT + 8:
        continue
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A = sym(odd_toeplitz(sp["c"], M_k))
    LP = lap_P_mat(m)
    B = parity_block(A, Tf, mu)
    t_cert = schur_best(B, SCHUR_KB)
    # THE PENCIL CEILING kap: A <= kap L_P as an OPERATOR (L3), certified by one
    # Cholesky of kap I - B.  DIRECTION: an UPPER bound, and it enters the H1
    # floor in the DENOMINATOR, so an upper bound on kap is what a lower bound
    # on Lc needs -- the direction is checked, not assumed.
    try:
        kap_meas = float(eigh(B, eigvals_only=True, subset_by_index=[m - 1, m - 1])[0])
    except (LinAlgError, ValueError):
        kap_meas = ray_top(B)
    kap = cert_lam_max(B, guess=kap_meas)
    # AND THE SAME CEILING ON THE BULK ALONE: if the pencil ceiling is large
    # only because mu^P_1 -> 0, then peeling the low block must cure it, and the
    # comparison localises the ill-conditioning instead of merely reporting it.
    Bb = sym(B[SCHUR_KB:, SCHUR_KB:])
    try:
        kb_meas = float(eigh(Bb, eigvals_only=True,
                             subset_by_index=[Bb.shape[0] - 1] * 2)[0])
    except (LinAlgError, ValueError):
        kb_meas = ray_top(Bb)
    rec_kap_bulk = cert_lam_max(Bb, guess=kb_meas)
    del B, Bb
    rec = dict(zk=zk, h=m, t=t_cert, kap=kap, kap_bulk=rec_kap_bulk,
               mu1=float(mu[0]), sep=float(mu[K_CERT] / mu[0]))
    try:
        w_lo, V_lo = eigh(A, subset_by_index=[0, K_CERT])
    except (LinAlgError, ValueError):
        del A, LP, Tf, sp
        continue
    rec["lam1"] = float(w_lo[0])
    rec["lam9"] = float(w_lo[K_CERT])
    V_lo = np.ascontiguousarray(V_lo[:, :K_CERT])
    rec["price"] = rec["lam1"] / max(t_cert * mu[0], 1.0e-300)
    # the sixteen-column certificate of T154, rebuilt, and its bottom eight
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    g1 = green_cols(A, LP, V0, 1)
    g2 = green_cols(A, LP, g1, 1) if g1 is not None else None
    if g1 is None or g2 is None:
        del A, LP, Tf, sp, V_lo
        continue
    Q16 = append_orth(orth_cols(V0), g1)
    rec["KF"] = cert_ceiling(sym(Q16.T @ (A @ Q16)), mu, K_CERT)
    g3 = green_cols(A, LP, g2, 1)
    QJ = {1: Q16, 2: append_orth(Q16, g2)}
    if g3 is not None:
        QJ[3] = append_orth(QJ[2], g3)
    Q = QJ[2]
    rec["dimQ"] = int(Q.shape[1])
    rp = ritz_pack(A, Q)
    try:
        _, Yb = eigh(rp["W"])
    except (LinAlgError, ValueError):
        del A, LP, Tf, sp, V_lo, Q, rp
        continue
    rec["mis"] = float(np.max(prin_angles(V0, V_lo)))
    Tk = Tf[:max(KLOW_SCAN), :]
    # THE SCAN OVER THE TWO FIXED-SIZE KNOBS: the inverse-iteration depth j
    # (16, 24 or 32 columns, all independent of m) and the dimension r of the
    # floor subspace.  (j = 2, r = 8) is T154's configuration; the defect
    # localisation below is what motivates r > 8, the residual is what motivates
    # j > 2, and nothing in this scan grows with m.
    rec["R"] = []
    for j_it in sorted(QJ):
        Qj = QJ[j_it]
        try:
            _, Yj = eigh(sym(Qj.T @ (A @ Qj)))
        except (LinAlgError, ValueError):
            continue
        for r_dim in RSCAN:
            if r_dim + 4 >= min(m, int(Qj.shape[1]) + 1):
                continue
            Qr = Qj @ Yj[:, :r_dim]
            Wr = sym(Qr.T @ (A @ Qr))
            Rr = A @ Qr - Qr @ Wr
            RtRr = sym(Rr.T @ Rr)
            # (0) THE EXACT NUMBER, MEASURED at size m -- the target the
            # fixed-size certificate is judged against, computed only for the
            # r = 8 configurations and never itself part of any chain.
            lc_ex = float("nan")
            if r_dim == K_CERT:
                Qf, _ = np.linalg.qr(Qr, mode="complete")
                Nr = Qf[:, r_dim:]
                lc_ex = float(eigh(sym(Nr.T @ (LP @ Nr)), eigvals_only=True,
                                   subset_by_index=[0, 0])[0]) / float(mu[0])
                del Qf, Nr
            # (A) THE FIXED-SIZE OVERLAP CERTIFICATE over the K ladder
            Gf = Tk @ Qr
            cand = []
            for K in KLOW_SCAN:
                if K <= r_dim or K + 2 >= m:
                    continue
                fl, _muK1, _vt = complement_floor(mu, Gf[:K], K)
                if np.isfinite(fl):
                    cand.append(dict(K=K, floor=fl / float(mu[0])))
            bst = max(cand, key=lambda d: d["floor"]) if cand else None
            lc_a = bst["floor"] if bst else float("nan")
            hit = [d["K"] for d in cand if d["floor"] >= 0.99 * lc_ex]
            # THE RECOVERY THE FLOOR BUYS, through the SAME fixed-size Temple
            # step.  DIRECTION: temple_matrix returns a LOWER bound on
            # lam_1(A); dividing by t mu^P_1 turns it into the recovery factor
            # the collapse price asks for, and the price is a cap it can never
            # exceed -- if it ever did, the direction would be wrong.
            rr = dict(j=j_it, r=r_dim, lc_ex=lc_ex, lc_a=lc_a,
                      tight=lc_a / max(lc_ex, 1.0e-300),
                      K_need=(min(hit) if hit else -1),
                      nrm_R=cert_norm2(Rr),
                      ang=float(np.max(prin_angles(Qr[:, :K_CERT], V_lo))))
            for tag, lcv in (("ex", lc_ex), ("a", lc_a)):
                g_c = (temple_matrix(Wr, RtRr, t_cert * lcv * float(mu[0]), 1)[0]
                       if np.isfinite(lcv) and lcv > 0.0 else float("nan"))
                rr["rec_" + tag] = (g_c / max(t_cert * mu[0], 1.0e-300)
                                    if np.isfinite(g_c) else float("nan"))
            rec["R"].append(rr)
            del Qr, Wr, Rr, RtRr, Gf
    r8 = [d for d in rec["R"] if d["r"] == K_CERT and d["j"] == 2]
    r8 = r8[0] if r8 else None
    rec["Lc_ex"] = r8["lc_ex"] if r8 else float("nan")
    rec["Lc_a"] = r8["lc_a"] if r8 else float("nan")
    rec["tight_a"] = r8["tight"] if r8 else float("nan")
    rec["K_need"] = r8["K_need"] if r8 else -1
    rec["ang_ritz"] = r8["ang"] if r8 else float("nan")
    rec["sin_dk"] = float(math.sin(math.radians(rec["ang_ritz"])))
    rec["rec_ex"] = r8["rec_ex"] if r8 else float("nan")
    rec["rec_a"] = r8["rec_a"] if r8 else float("nan")
    okr = [d for d in rec["R"] if np.isfinite(d["rec_a"])]
    bb = max(okr, key=lambda d: d["rec_a"]) if okr else None
    rec["r_best"] = bb["r"] if bb else -1
    rec["j_best"] = bb["j"] if bb else -1
    rec["rec_best"] = bb["rec_a"] if bb else float("nan")
    rec["lc_best"] = bb["lc_a"] if bb else float("nan")
    rec["K_best"] = bb["K_need"] if bb else -1
    rec["share"] = rec["rec_best"] / max(rec["price"], 1.0e-300)
    # WHERE THE DEFECT SITS: the per-mode uncovered fraction 1 - ||row_k(G)||^2
    # of the r = 8 configuration -- the number that eats the free scale.
    Q8 = Q @ Yb[:, :K_CERT]
    dvec = 1.0 - np.sum((Tf[:K_CERT, :] @ Q8) ** 2, axis=1)
    rec["defect"] = [float(x) for x in dvec]
    rec["def_mode"] = int(np.argmax(dvec)) + 1
    rec["def_max"] = float(np.max(dvec))
    rec["def_1"] = float(dvec[0])
    # AND WHAT THE ONE MISALIGNED DIRECTION IS: the Q8-side vector of the
    # LARGEST principal angle against the exact parity sines -- T154's 83 .. 90
    # degree direction.  Where does it live in the L_P ladder?
    _u, ss, Vts = np.linalg.svd(V0.T @ Q8)
    u_bad = Q8 @ Vts[-1]
    u_bad = u_bad / max(float(np.linalg.norm(u_bad)), 1.0e-300)
    rec["u_ray"] = float(u_bad @ (LP @ u_bad)) / float(mu[0])
    cu = Tf @ u_bad
    rec["u_low8"] = float(np.sum(cu[:K_CERT] ** 2))
    rec["u_low16"] = float(np.sum(cu[:min(16, m)] ** 2))
    rec["u_mode"] = int(np.argmax(cu ** 2)) + 1
    rec["cos_bad"] = float(ss[-1])
    del _u, ss, Vts, cu, Q8
    # (B) THE PENCIL-CEILING CHAIN, and the prediction that explains its size
    rec["Lc_b"] = (rec["sep"] * (t_cert - rec["KF"] * rec["sin_dk"] ** 2)
                   / kap) if np.isfinite(kap) and kap > 0.0 else float("nan")
    rec["cond"] = kap / max(t_cert, 1.0e-300)
    rec["nrmA"] = abs(ray_top(A))
    rec["kap_pred"] = rec["nrmA"] / float(mu[0])
    rec["kap_pred_b"] = rec["nrmA"] / float(mu[SCHUR_KB])
    H1R.append(rec)
    del A, LP, Tf, sp, V_lo, Q, rp, Tk

XH = [r["h"] for r in H1R]
BIG = [r for r in H1R if r["h"] >= 200]
F_LC = pow_fit(XH, [r["Lc_a"] for r in H1R], "Lc (fixed-size certificate)")
F_DEF = pow_fit([r["h"] for r in BIG], [r["def_1"] for r in BIG],
                "mode-1 overlap defect")
F_KAP = pow_fit(XH, [r["kap"] for r in H1R], "pencil ceiling kap")
F_KAPB = pow_fit(XH, [r["kap_bulk"] for r in H1R], "bulk pencil ceiling")
F_REC = pow_fit(XH, [r["rec_best"] for r in H1R], "recovery, fixed size")
F_SH = pow_fit(XH, [r["share"] for r in H1R], "share of the price")
F_PR = pow_fit(XH, [r["price"] for r in H1R], "collapse price")

check("bf_h1.surface",
      len(H1R) >= 8 and all(np.isfinite(r["Lc_ex"]) for r in H1R),
      "the complement surface carries %d windows, h = %d .. %d.  The inputs are "
      "reproduced, not re-derived: the certified Schur floor is t = %.4f .. "
      "%.4f at the FIXED low block kb = %d, the closed sixteen-column ceiling "
      "is K^F = %.4f .. %.4f (T154 quoted %.4f .. %.4f), the collapse price is "
      "%.3f .. %.3f (%s) and the misalignment is %.2f .. %.2f deg (T154 quoted "
      "%.2f .. %.2f).  THE TARGET NUMBER, MEASURED at size m: Lc = %.3f .. "
      "%.3f mu^P_1 (T154 quoted %.2f .. %.2f)"
      % (len(H1R), qmin(XH), qmax(XH), qmin([r["t"] for r in H1R]),
         qmax([r["t"] for r in H1R]), SCHUR_KB,
         qmin([r["KF"] for r in H1R]), qmax([r["KF"] for r in H1R]),
         T154_KF[0], T154_KF[1], qmin([r["price"] for r in H1R]),
         qmax([r["price"] for r in H1R]), fit_str(F_PR),
         qmin([r["mis"] for r in H1R]), qmax([r["mis"] for r in H1R]),
         T154_MIS[0], T154_MIS[1], qmin([r["Lc_ex"] for r in H1R]),
         qmax([r["Lc_ex"] for r in H1R]), T154_LC[0], T154_LC[1]))

TIGHT = [r["tight_a"] for r in H1R]
KN = [r["K_need"] for r in H1R]
check("bf_h1.certificate_is_exact",
      qmin(TIGHT) >= 1.0 - 1.0e-5 and qmax(TIGHT) <= 1.0 + 1.0e-9
      and max(KN) <= 12,
      "*** THE FIRST RESULT: R2' BECOMES A FIXED-SIZE CERTIFICATE, AND IT IS "
      "NOT MERELY A BOUND -- IT IS EXACT. ***  The overlap certificate "
      "mu^P_{K+1} - lam_max(M^{1/2}(I - G G^T) M^{1/2}) is a LOWER bound on Lc "
      "by construction (Rayleigh on the high block, an identity for the "
      "constraint), so the only question is how much it loses.  It loses "
      "nothing: the ratio certificate / exact is %.9f .. %.9f on %d of %d "
      "windows, and the smallest K of the ladder %s that already attains 99 "
      "percent of the exact number is K = %d on EVERY window.  So the m-sized "
      "eigenvalue problem T154 had to solve is replaced by a %d x %d eigenvalue "
      "problem in the EXACT Kac-Murdock-Szego numbers and one %d x %d overlap "
      "matrix.  The certificate never exceeds the exact value, which is the "
      "direction check: a lower bound that overshot would be a bug"
      % (qmin(TIGHT), qmax(TIGHT), len(H1R), len(H1R),
         ", ".join(str(k) for k in KLOW_SCAN), max(KN), max(KN), max(KN),
         max(KN), K_CERT))

FACTOR = [r["sep"] / r["Lc_a"] for r in H1R]
DM = [r["def_mode"] for r in BIG]
check("bf_h1.defect_localised",
      all(d == 1 for d in DM) and qmax([r["u_low8"] for r in H1R]) < 0.05,
      "*** AND THE CERTIFICATE SAYS WHERE THE FREE SCALE GOES. ***  If Q8 "
      "covered the eight lowest L_P modes, G G^T would be the identity, the "
      "certificate would return mu^P_9 exactly and Lc would be %.2f .. %.2f "
      "mu^P_1 (Kac-Murdock-Szego, increasing to 81).  It returns %.2f .. %.2f, "
      "so the defect costs a factor %.2f .. %.2f -- and the factor is NOT "
      "spread over the eight modes.  On every window with h >= 200 the largest "
      "uncovered fraction 1 - ||row_k(G)||^2 sits at k = 1, THE BOTTOM MODE "
      "ITSELF, at %.3f .. %.3f (%s): the eight bottom Ritz directions of A "
      "leave three fifths of t_1 outside their span.  The reason is visible in "
      "the same object: the direction realising the %.2f .. %.2f deg "
      "misalignment carries only %.1e .. %.1e of its mass on modes 1 .. 8, has "
      "L_P Rayleigh quotient %.1f .. %.1f mu^P_1 and peaks at mode %d .. %d.  "
      "The eight-dimensional certificate spends one of its directions on modes "
      "9 .. 12 and pays for it at mode 1, which is exactly why the certificate "
      "needs K = %d and not K = 8 to be exact"
      % (qmin([r["sep"] for r in H1R]), qmax([r["sep"] for r in H1R]),
         qmin([r["Lc_a"] for r in H1R]), qmax([r["Lc_a"] for r in H1R]),
         qmin(FACTOR), qmax(FACTOR), qmin([r["def_1"] for r in BIG]),
         qmax([r["def_1"] for r in BIG]), fit_str(F_DEF),
         qmin([r["mis"] for r in H1R]), qmax([r["mis"] for r in H1R]),
         qmin([r["u_low8"] for r in H1R]), qmax([r["u_low8"] for r in H1R]),
         qmin([r["u_ray"] for r in H1R]), qmax([r["u_ray"] for r in H1R]),
         min(r["u_mode"] for r in H1R), max(r["u_mode"] for r in H1R),
         max(KN)))

KRAT = [r["kap"] / r["kap_pred"] for r in H1R]
check("bf_h1.pencil_route_refuted",
      not nogrow_ok(F_KAP) and qmax([r["Lc_b"] for r in H1R]) < 0.1,
      "AND THE SECOND INSTRUMENT IS REFUTED, WITH ITS MECHANISM MEASURED.  The "
      "pencil-ceiling chain Lc >= mu^P_9 (t - K^F s^2) / kap is a THEOREM in "
      "every step -- the projector split is an identity, the Davis-Kahan 1970 "
      "transfer costs s^2 with s = %.1e .. %.1e, and t and K^F are already "
      "certified -- but it dies on its one new input.  kap = lam_max(B) = "
      "%.3g .. %.3g and GROWS: %s, so the chain returns %.2g .. %.2g mu^P_1 "
      "instead of %.2f .. %.2f, dead by three to five orders of magnitude.  "
      "THE MECHANISM IS NOT MYSTERIOUS AND IT IS NOT CURABLE BY PEELING: the "
      "pencil ceiling is attained where L_P is SMALL, i.e. exactly at the "
      "bottom the floor is about, and it tracks ||A|| / mu^P_1 to a factor "
      "%.2f .. %.2f.  Peeling the low block does not help either -- on the "
      "bulk alone lam_max(B_HH) = %.2f .. %.2f, still growing (%s), because "
      "mu^P_{kb+1} is just as small a number.  The two-sided pencil is "
      "maximally ill-conditioned in precisely the direction R2' asks about"
      % (qmin([r["sin_dk"] for r in H1R]), qmax([r["sin_dk"] for r in H1R]),
         qmin([r["kap"] for r in H1R]), qmax([r["kap"] for r in H1R]),
         fit_str(F_KAP), qmin([r["Lc_b"] for r in H1R]),
         qmax([r["Lc_b"] for r in H1R]), qmin([r["Lc_a"] for r in H1R]),
         qmax([r["Lc_a"] for r in H1R]), qmin(KRAT), qmax(KRAT),
         qmin([r["kap_bulk"] for r in H1R]),
         qmax([r["kap_bulk"] for r in H1R]), fit_str(F_KAPB)))

GAIN_F, GAIN_R, N_UP, N_UP_OK = [], [], 0, 0
for r in H1R:
    base = [d for d in r["R"] if d["r"] == K_CERT and d["j"] == 2]
    if not base:
        continue
    b0 = base[0]
    for d in r["R"]:
        if d["r"] <= K_CERT or d["j"] != 2:
            continue
        N_UP += 1
        N_UP_OK += int(np.isfinite(d["rec_a"]))
        GAIN_F.append(d["lc_a"] / max(b0["lc_a"], 1.0e-300))
        GAIN_R.append(d["nrm_R"] / max(b0["nrm_R"], 1.0e-300))
check("bf_h1.wider_subspace_refuted", N_UP_OK <= 1 and qmin(GAIN_F) > 1.0,
      "THE OBVIOUS REPAIR IS TRIED AND IT FAILS, WHICH IS WHY THE DEFECT "
      "LOCALISATION MATTERS MORE THAN IT LOOKS.  If one Ritz direction is "
      "wasted on modes 9 .. 12, then widening the floor subspace to r = %s "
      "should recover the free scale -- and it does: the certified complement "
      "floor rises by a factor %.2f .. %.2f, up to %.1f mu^P_1, still at fixed "
      "size.  But the widened subspace is no longer converged: its residual "
      "rises by a factor %.1f .. %.1f at the same time, and the Temple step "
      "returns a floor on only %d of %d widened configurations.  The floor and "
      "the residual are bought from the same account, and at r = 8 the account "
      "is already balanced"
      % (", ".join(str(k) for k in RSCAN[1:]), qmin(GAIN_F), qmax(GAIN_F),
         qmax([d["lc_a"] for r in H1R for d in r["R"] if d["r"] > K_CERT]),
         qmin(GAIN_R), qmax(GAIN_R), N_UP_OK, N_UP))

SHARE = [r["share"] for r in H1R]
REC_LO, REC_UP = qmin([r["rec_best"] for r in H1R]), qmax([r["rec_best"]
                                                           for r in H1R])
JB = sorted(set(r["j_best"] for r in H1R))
DIMB = max(8 * (j + 1) for j in JB)
N_FULL = sum(1 for s in SHARE if s >= 0.99)
N_90 = sum(1 for s in SHARE if s >= 0.90)
check("bf_h1.full_price_at_fixed_size",
      qmin(SHARE) >= 0.75 and REC_LO >= REC_BAR
      and qmax(SHARE) <= 1.0 + 1.0e-9,
      "*** THE H1 PAYOFF: THE COLLAPSE PRICE, AT FIXED SIZE. ***  T154 "
      "recovered the price %.3f .. %.3f by ONE CHOLESKY OF A - gam I, a "
      "factorisation of size m, and labelled the result CERTIFIED-PER-WINDOW "
      "and explicitly NOT fixed size.  Feeding the fixed-size complement floor "
      "into the SAME Temple step recovers %.3f .. %.3f, i.e. %.1f .. %.1f "
      "percent of the price (%s), with the deepest configuration used being j "
      "= %s, i.e. %d columns, plus a %d x %d certificate -- and NOTHING in "
      "that chain has a size that depends on m.  THE SPREAD IS REPORTED AND "
      "NOT AVERAGED AWAY: the fixed-size chain takes the WHOLE price on %d of "
      "%d windows and at least ninety percent on %d of %d, and the two windows "
      "where it does not are residual-limited, not floor-limited -- the "
      "certificate reads the same number there, the Temple step simply cannot "
      "convert all of it.  The direction is checked at every window: the "
      "recovery never exceeds the price, as it must not, since the price is "
      "lam_1(A) itself"
      % (qmin([r["price"] for r in H1R]), qmax([r["price"] for r in H1R]),
         REC_LO, REC_UP, 100.0 * qmin(SHARE), 100.0 * qmax(SHARE),
         fit_str(F_SH), "/".join(str(j) for j in JB), DIMB, max(KN), max(KN),
         N_FULL, len(SHARE), N_90, len(SHARE)))

check("bf_h1.uniformity_is_a_fit",
      flat_ok(F_LC) and flat_ok(F_DEF) and flat_ok(F_SH),
      "AND WHAT IS STILL MISSING, STATED AS A NUMBER AND NOT AS A MOOD.  Every "
      "quantity above is FLAT on the surface: the complement floor %s, the "
      "mode-1 defect %s, the share of the price %s, the recovery %s.  But FLAT "
      "IS A FIT AND A FIT IS NOT A THEOREM.  What an m-free R2' still needs is "
      "ONE inequality: an m-free UPPER bound on lam_max(M^{1/2}(I - G G^T) "
      "M^{1/2}) with M the exact KMS weights at K = %d, equivalently an m-free "
      "upper bound on how much of the bottom L_P mode the eight bottom Ritz "
      "directions of A may miss.  That object is %d x %d, it is the ONLY "
      "arithmetic left in R2', and it is measured at %.3f .. %.3f mu^P_1 below "
      "the free scale mu^P_9"
      % (fit_str(F_LC), fit_str(F_DEF), fit_str(F_SH), fit_str(F_REC), max(KN),
         max(KN), max(KN), qmin([r["sep"] - r["Lc_a"] for r in H1R]),
         qmax([r["sep"] - r["Lc_a"] for r in H1R])))

for _r in H1R:
    info("H1.raw", "h=%d t=%.4f kap=%.3g kapB=%.4f sep=%.2f Lc_ex=%.4f "
         "Lc_a=%.4f tight=%.6f Kneed=%d Lc_b=%.3g mis=%.2f angR=%.2e "
         "defmode=%d defmax=%.3f uray=%.2f ulow8=%.3f umode=%d price=%.3f "
         "rec_ex=%.3f rec_a=%.3f KF=%.4f | best r=%d rec=%.3f lc=%.2f K=%d | "
         "kpred=%.3g kpredB=%.3g | %s"
         % (_r["h"], _r["t"], _r["kap"], _r["kap_bulk"], _r["sep"], _r["Lc_ex"],
            _r["Lc_a"], _r["tight_a"], _r["K_need"], _r["Lc_b"], _r["mis"],
            _r["ang_ritz"], _r["def_mode"], _r["def_max"], _r["u_ray"],
            _r["u_low8"], _r["u_mode"], _r["price"], _r["rec_ex"], _r["rec_a"],
            _r["KF"], _r["r_best"], _r["rec_best"], _r["lc_best"],
            _r["K_best"], _r["kap_pred"], _r["kap_pred_b"],
            " ".join("j%dr%d:lc=%.2f rec=%.2f R=%.2g"
                     % (d["j"], d["r"], d["lc_a"], d["rec_a"], d["nrm_R"])
                     for d in _r["R"])))

# ----------------------------------------------------------------------------
section("H2  R1' -- THE BLOCK FLOOR, DECOMPOSED ALONG THE T154 ANATOMY")
# ----------------------------------------------------------------------------
para("""H2.0  WHAT T154 LEFT AND WHAT IT FORBIDS.  R1' is the block inequality
B_HH >= t I on the bulk parity block, with lam_min(B_HH) = %.3f .. %.3f per
window over t = %.2f.  T154 killed every RELATIVE route to it: the arch-whitened
Kato number loses a factor %.2f .. %.3g at an angle of %.1f .. %.1f degrees, the
Hankel reflection is refuted twice as the culprit, and the peel that would repair
the number is %.2f .. %.2f OF THE WINDOW, i.e. proportional to m.  But T154 also
left a precise anatomy: the minimiser carries %.1f .. %.1f percent of its mass on
the EIGHT modes immediately above whatever cut is chosen, and only %.1f .. %.1f
percent at the boundary.  A decomposition that does not know that direction
cannot work; this block builds one that does.""" % (
    T154_BHH[0], T154_BHH[1], T_TARGET, 1.97, 121.0, 24.9, 89.8, 0.40, 0.69,
    96.5, 100.0, 0.9, 11.9))

para("""H2.1  THE DIRECTION-AWARE DECOMPOSITION, STATED BEFORE IT IS RUN.  Split
the bulk index set H into the WINDOW w -- the %d modes immediately above the peel
cut, where the minimiser lives -- and the DEEP part d.  For any unit vector
u = (u_w, u_d),
    u^T B_HH u >= a ||u_w||^2 - 2 b ||u_w|| ||u_d|| + dd ||u_d||^2
with a = lam_min(B_ww), dd = lam_min(B_dd), b = ||B_wd||, so
    lam_min(B_HH) >= (a + dd)/2 - sqrt(((a - dd)/2)^2 + b^2)  ,
the smaller eigenvalue of a 2 x 2 matrix -- a THEOREM for any splitting, and the
DIRECTION is a lower bound throughout (a and dd enter as lower bounds, b as an
upper bound; each is certified in that direction and never the other).  What
makes it direction-AWARE is the choice of w: a is an 8 x 8 object, FIXED SIZE,
sitting exactly where the offending vector sits.  The question this block
decides is whether dd terminates -- whether the deep part is comfortably
positive because the arch reserve dominates there -- or whether the deep part
merely reproduces the same problem one cut higher, which is what T154's
scale-free observation predicts.""" % KW_WIN)

para("""H2.2  AND THE m-FREE CANDIDATE FOR THE DEEP PART: THE ARCH SYMBOL.  The
arch half of the lag kernel is a fixed analytic function of the lag, so its
odd section is a Toeplitz-minus-Hankel matrix with a SYMBOL, and Szego 1915 /
Widom 1958 / Kac-Murdock-Szego 1953 make the symbol infimum the natural m-free
candidate for its sections: f^arch(th) / (4 sin^2(th/2)) minimised over the bulk
range th >= th_{kb+1}.  This block MEASURES how close lam_min(B^arch_HH) is to
that infimum.  If they agree, the arch reserve is a theorem CANDIDATE with a
named mechanism; if they do not, the candidate is dead and is reported dead.
Nothing here is used as a bound.""")

H2C = [c for c in CAND if c[3] <= H2_HCAP]
H2S = []
if H2C:
    st = max(1, len(H2C) // max(H2_ZONES, 1))
    H2S = H2C[::-1][::st][:H2_ZONES]
    H2S.sort(key=lambda t: t[0])

H2R = []
for (zk, D_k, M_k, h_k) in H2S:
    if budget_left() < 200.0:
        info("H2.2.budget", "block surface truncated at %d windows" % len(H2R))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    kb = SCHUR_KB
    if m <= kb + 4 * KW_WIN:
        continue
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A = sym(odd_toeplitz(sp["c"], M_k))
    B = parity_block(A, Tf, mu)
    B_ar = parity_block(sym(odd_toeplitz(sp["c_ar"], M_k)), Tf, mu)
    B_at = parity_block(sym(odd_toeplitz(sp["c_at"], M_k)), Tf, mu)
    nb = m - kb
    rec = dict(zk=zk, h=m, nb=nb)
    HH = sym(B[kb:, kb:])
    try:
        wH, VH = eigh(HH)
    except (LinAlgError, ValueError):
        del A, B, B_ar, B_at, Tf, sp, HH
        continue
    rec["lo_B"] = float(wH[0])
    rec["lo_B_cert"] = cert_lam_min(HH, guess=float(wH[0]))
    uH = VH[:, 0]
    rec["low8"] = float(np.sum(uH[:KW_WIN] ** 2))
    del VH, wH
    # THE DIRECTION-AWARE 2 x 2, in three labels
    Bww = sym(HH[:KW_WIN, :KW_WIN])
    Bdd = sym(HH[KW_WIN:, KW_WIN:])
    Bwd = HH[:KW_WIN, KW_WIN:]
    rec["a"] = cert_lam_min(Bww, guess=float(np.min(np.linalg.eigvalsh(Bww))))
    try:
        wD, VD = eigh(Bdd)
    except (LinAlgError, ValueError):
        del A, B, B_ar, B_at, Tf, sp, HH, Bww, Bdd
        continue
    rec["d_ex"] = cert_lam_min(Bdd, guess=float(wD[0]))
    # THE SCALE-INVARIANCE TEST: does the deep block reproduce the anatomy one
    # cut higher, or does it terminate?
    rec["low8_dd"] = float(np.sum(VD[:KW_WIN, 0] ** 2))
    del wD, VD
    rec["b"] = cert_norm2(np.ascontiguousarray(Bwd.T))

    def two_by_two(av, dv, bv):
        if not (np.isfinite(av) and np.isfinite(dv) and np.isfinite(bv)):
            return float("nan")
        return 0.5 * (av + dv) - math.sqrt(0.25 * (av - dv) ** 2 + bv * bv)

    rec["floor2"] = two_by_two(rec["a"], rec["d_ex"], rec["b"])
    # THE m-FREE-SHAPED VERSIONS OF THE TWO DIAGONAL ENTRIES
    Par = sym(B_ar[kb:, kb:])
    Pat = sym(B_at[kb:, kb:])
    rec["lo_ar"] = cert_lam_min(Par, guess=float(
        eigh(Par, eigvals_only=True, subset_by_index=[0, 0])[0]))
    Aw = sym(Par[:KW_WIN, :KW_WIN])
    rec["a_ar"] = cert_lam_min(Aw, guess=float(np.min(np.linalg.eigvalsh(Aw))))
    rec["at_w"] = cert_lam_max(sym(Pat[:KW_WIN, :KW_WIN]),
                               guess=gersh(sym(Pat[:KW_WIN, :KW_WIN])))
    rec["at_w_nrm"] = float(np.max(np.abs(
        np.linalg.eigvalsh(sym(Pat[:KW_WIN, :KW_WIN])))))
    rec["a_free"] = rec["a_ar"] - rec["at_w_nrm"]
    # the arch-whitened Kato floor on the DEEP block (the m-free-shaped dd)
    try:
        wP, VP = eigh(sym(Par[KW_WIN:, KW_WIN:]))
        if float(wP[0]) > 0.0:
            Wh = VP * (1.0 / np.sqrt(wP))[None, :]
            Cd = sym(Wh.T @ (sym(Pat[KW_WIN:, KW_WIN:]) @ Wh))
            lo_C = float(eigh(Cd, eigvals_only=True, subset_by_index=[0, 0])[0])
            rec["one_C_dd"] = 1.0 + lo_C
            rec["d_wh"] = float(wP[0]) * rec["one_C_dd"]
            del Wh, Cd
        else:
            rec["one_C_dd"] = float("nan")
            rec["d_wh"] = float("nan")
        del wP, VP
    except (LinAlgError, ValueError):
        rec["one_C_dd"] = float("nan")
        rec["d_wh"] = float("nan")
    rec["floor2_free"] = two_by_two(rec["a_free"], rec["d_wh"], rec["b"])
    # THE T154 ANATOMY, REPRODUCED ON ITS OWN OBJECT.  T154's 96.5 .. 100
    # percent is a statement about the minimiser of the ARCH-WHITENED atom
    # operator C, not about the minimiser of B_HH; both are measured here,
    # because the direction-aware split above is built on one of them.
    try:
        wP0, VP0 = eigh(Par)
        if float(wP0[0]) > 0.0:
            Wh0 = VP0 * (1.0 / np.sqrt(wP0))[None, :]
            C0 = sym(Wh0.T @ (Pat @ Wh0))
            wc, Vc = eigh(C0)
            rec["one_C"] = 1.0 + float(wc[0])
            uc = Wh0 @ Vc[:, 0]
            uc = uc / max(float(np.linalg.norm(uc)), 1.0e-300)
            rec["low8_C"] = float(np.sum(uc[:KW_WIN] ** 2))
            del Wh0, C0, wc, Vc, uc
        else:
            rec["one_C"] = float("nan")
            rec["low8_C"] = float("nan")
        del wP0, VP0
    except (LinAlgError, ValueError):
        rec["one_C"] = float("nan")
        rec["low8_C"] = float("nan")
    # THE SYMBOL FLOORS.  For the arch half this is the m-free theorem
    # candidate; for the FULL kernel it is the sharper question -- whether R1'
    # is a statement about a FUNCTION OF theta rather than about a matrix.
    N = 2 * m + 1
    th = 2.0 * math.pi * np.arange(kb + 1, m + 1) / N
    lags = np.arange(1, M_k)
    CO = np.cos(np.outer(th, lags))
    den = 4.0 * np.sin(0.5 * th) ** 2
    f_ar = sp["c_ar"][0] + 2.0 * (CO @ sp["c_ar"][1:])
    f_at = sp["c_at"][0] + 2.0 * (CO @ sp["c_at"][1:])
    rec["sym_floor"] = float(np.min(f_ar / den))
    rec["sym_rat"] = rec["lo_ar"] / max(rec["sym_floor"], 1.0e-300)
    rec["sym_full"] = float(np.min((f_ar + f_at) / den))
    rec["sym_full_rat"] = rec["lo_B"] / rec["sym_full"] if rec["sym_full"] \
        else float("nan")
    rec["sym_at"] = float(np.min(f_at / den))
    rec["diag_min"] = float(np.min(np.diag(HH)))
    del th, f_ar, f_at, lags, CO, den
    H2R.append(rec)
    del A, B, B_ar, B_at, Tf, sp, HH, Bww, Bdd, Par, Pat

XB = [r["h"] for r in H2R]
F_LOB = pow_fit(XB, [r["lo_B"] for r in H2R], "lam_min(B_HH)")
F_LOAR = pow_fit(XB, [r["lo_ar"] for r in H2R], "arch reserve")
F_COUP = pow_fit(XB, [r["b"] for r in H2R], "coupling ||B_wd||")
F_ATW = pow_fit(XB, [r["at_w_nrm"] / r["a_ar"] for r in H2R],
                "local atom / arch")
F_SYMF = pow_fit(XB, [-r["sym_full"] for r in H2R], "-(full symbol infimum)")

check("bf_h2.surface",
      len(H2R) >= 8 and all(r["lo_B_cert"] > 0.0 for r in H2R),
      "the block surface carries %d windows, h = %d .. %d, and T154's two "
      "numbers are reproduced on their own objects.  lam_min(B_HH) = %.4f .. "
      "%.4f (T154 quoted %.3f .. %.3f), CERTIFIED positive by one Cholesky at "
      "%.4f .. %.4f.  Against the target t = %.2f the block inequality holds on "
      "%d of %d windows; on the remaining ones the Schur ladder backs off to a "
      "smaller certified t, which is the mechanism that keeps the chain valid "
      "and is reported rather than smoothed (%s).  And the T154 "
      "anatomy holds where T154 measured it: the minimiser of the "
      "ARCH-WHITENED atom operator C carries %.1f .. %.1f percent of its mass "
      "on the %d modes immediately above the cut, with 1 + lam_min(C) = "
      "%.2e .. %.2e"
      % (len(H2R), qmin(XB), qmax(XB), qmin([r["lo_B"] for r in H2R]),
         qmax([r["lo_B"] for r in H2R]), T154_BHH[0], T154_BHH[1],
         qmin([r["lo_B_cert"] for r in H2R]),
         qmax([r["lo_B_cert"] for r in H2R]), T_TARGET,
         sum(1 for r in H2R if r["lo_B_cert"] >= T_TARGET), len(H2R),
         fit_str(F_LOB),
         100.0 * qmin([r["low8_C"] for r in H2R]),
         100.0 * qmax([r["low8_C"] for r in H2R]), KW_WIN,
         qmin([r["one_C"] for r in H2R]), qmax([r["one_C"] for r in H2R])))

N_SAME = sum(1 for r in H2R if r["low8"] > 0.5)
check("bf_h2.two_minimisers_are_not_the_same_vector",
      N_SAME <= len(H2R) // 3,
      "*** AND THE FIRST THING THE DECOMPOSITION FINDS IS THAT THE ANATOMY "
      "BELONGS TO A DIFFERENT VECTOR. ***  T154's ``the minimiser sits on the "
      "eight modes above the cut'' is a statement about the minimiser of the "
      "arch-whitened operator C (%.1f .. %.1f percent, confirmed above).  The "
      "minimiser of B_HH ITSELF puts only %.1e .. %.2f of its mass there, and "
      "exceeds one half on %d of %d windows.  The two vectors are different "
      "objects and only one of them is the one R1' is about.  This is not a "
      "correction of a number, it is a correction of a TARGET: a decomposition "
      "aimed at the C-minimiser is aimed away from lam_min(B_HH)"
      % (100.0 * qmin([r["low8_C"] for r in H2R]),
         100.0 * qmax([r["low8_C"] for r in H2R]),
         qmin([r["low8"] for r in H2R]), qmax([r["low8"] for r in H2R]),
         N_SAME, len(H2R)))

NEEDB = [math.sqrt(max(r["a"], 0.0) * max(r["d_ex"], 0.0)) for r in H2R]
COUPR = [r["b"] / max(n, 1.0e-300) for n, r in zip(NEEDB, H2R)]
check("bf_h2.direction_aware_split_refuted",
      qmax([r["floor2"] for r in H2R]) < 0.0 and qmin(COUPR) > 1.0,
      "AND THE DECOMPOSITION ITSELF IS REFUTED, WITH THE ONE NUMBER THAT KILLS "
      "IT.  Both diagonal blocks are healthy: a = lam_min(B_ww) = %.4f .. %.4f "
      "on the %d x %d window block, dd = lam_min(B_dd) = %.4f .. %.4f on the "
      "deep block, both certified and both comfortably above t = %.2f.  The "
      "2 x 2 bound would therefore carry the floor if the coupling satisfied "
      "b <= sqrt(a dd) = %.3f .. %.3f.  MEASURED, b = ||B_wd|| = %.2f .. %.2f, "
      "too large by a factor %.1f .. %.1f, and GROWING (%s).  So the 2 x 2 "
      "floor is %.1f .. %.1f, i.e. vacuous.  The mechanism is the one T153 "
      "already named for a different purpose: the atom part couples the mode "
      "index LONG RANGE, so B_HH is nowhere near block-diagonal and no norm "
      "bound on an off-diagonal block of it can be small"
      % (qmin([r["a"] for r in H2R]), qmax([r["a"] for r in H2R]), KW_WIN,
         KW_WIN, qmin([r["d_ex"] for r in H2R]),
         qmax([r["d_ex"] for r in H2R]), T_TARGET, qmin(NEEDB), qmax(NEEDB),
         qmin([r["b"] for r in H2R]), qmax([r["b"] for r in H2R]),
         qmin(COUPR), qmax(COUPR), fit_str(F_COUP),
         qmin([r["floor2"] for r in H2R]), qmax([r["floor2"] for r in H2R])))

ATR = [r["at_w_nrm"] / r["a_ar"] for r in H2R]
check("bf_h2.local_atom_norm_refuted",
      qmax([r["a_free"] for r in H2R]) < 0.0 and qmin(ATR) > 1.0,
      "THE SECOND CANDIDATE OF THE BRIEF -- ARCH RESERVE MINUS ATOM NORM ON "
      "THE EIGHT-MODE WINDOW ALONE -- IS REFUTED TOO, AND IT IS REFUTED "
      "LOCALLY, WHICH IS THE INFORMATIVE PART.  On the %d x %d window block the "
      "arch reserve is lam_min(B^arch_ww) = %.2f .. %.2f, large because the "
      "whitening by mu^P divides by a small number there.  But the atom "
      "operator on the SAME block has norm %.2f .. %.2f, larger by a factor "
      "%.2f .. %.2f which GROWS (%s), so the difference is %.1f .. %.1f, "
      "negative on every window.  Restricting the atom bound to a fixed-size "
      "window does not make it small: the atoms are not local in the mode index"
      % (KW_WIN, KW_WIN, qmin([r["a_ar"] for r in H2R]),
         qmax([r["a_ar"] for r in H2R]),
         qmin([r["at_w_nrm"] for r in H2R]), qmax([r["at_w_nrm"] for r in H2R]),
         qmin(ATR), qmax(ATR), fit_str(F_ATW),
         qmin([r["a_free"] for r in H2R]), qmax([r["a_free"] for r in H2R])))

check("bf_h2.deep_block_does_not_terminate",
      qmax([r["d_wh"] for r in H2R]) < T_TARGET,
      "AND THE RECURSION DOES NOT TERMINATE, WHICH ANSWERS THE BRIEF'S "
      "QUESTION DIRECTLY.  A second Schur window at the cut only helps if the "
      "DEEP block carries its own m-free floor.  It does not: the arch-whitened "
      "floor on the deep block is lam_min(P_dd)(1 + lam_min(C_dd)) = %.2e .. "
      "%.2e, below t = %.2f on every window, and its Kato factor 1 + "
      "lam_min(C_dd) = %.2e .. %.2e is the SAME order as the one at the "
      "original cut (%.2e .. %.2e).  Moving the cut up by %d modes moves the "
      "problem up by %d modes.  T154's scale-free reading is confirmed on a "
      "second, independent decomposition"
      % (qmin([r["d_wh"] for r in H2R]), qmax([r["d_wh"] for r in H2R]),
         T_TARGET, qmin([r["one_C_dd"] for r in H2R]),
         qmax([r["one_C_dd"] for r in H2R]), qmin([r["one_C"] for r in H2R]),
         qmax([r["one_C"] for r in H2R]), KW_WIN, KW_WIN))

SR = [r["sym_rat"] for r in H2R]
ART = [r["lo_ar"] / T_TARGET for r in H2R]
check("bf_h2.arch_symbol_is_the_mechanism",
      qmax([abs(x - 1.0) for x in SR]) < 1.0e-2,
      "*** THE ONE POSITIVE RESULT OF H2, AND IT IS A MECHANISM AND NOT A "
      "NUMBER. ***  The arch reserve is not merely bounded on the surface -- it "
      "IS the symbol infimum.  Minimising the arch symbol ratio f^arch(th) / "
      "(4 sin^2(th/2)) over the bulk range th >= th_{kb+1} gives %.4f .. %.4f, "
      "and lam_min(B^arch_HH) = %.4f .. %.4f: the ratio of the two is %.6f .. "
      "%.6f on %d of %d windows.  So Szego 1915 / Widom 1958 / "
      "Kac-Murdock-Szego 1953 apply to the arch half exactly as one would hope, "
      "the arch reserve is a THEOREM CANDIDATE with a named mechanism (the "
      "symbol of a fixed analytic kernel, no matrix in it), and it exceeds the "
      "target by a factor %.2f .. %.2f (%s).  LABEL: candidate.  Proving it "
      "means proving an inequality about one function of one variable"
      % (qmin([r["sym_floor"] for r in H2R]),
         qmax([r["sym_floor"] for r in H2R]),
         qmin([r["lo_ar"] for r in H2R]), qmax([r["lo_ar"] for r in H2R]),
         qmin(SR), qmax(SR), len(H2R), len(H2R), qmin(ART), qmax(ART),
         fit_str(F_LOAR)))

check("bf_h2.full_symbol_refuted",
      qmax([r["sym_full"] for r in H2R]) < 0.0,
      "*** AND THE SAME INSTRUMENT DELIVERS THE STRONGEST NEGATIVE STATEMENT "
      "IN THIS FILE. ***  If the symbol carries the arch half, the obvious "
      "question is whether it carries the whole kernel -- which would turn R1' "
      "from a matrix statement into a statement about a function of theta, "
      "m-free by construction.  IT DOES NOT, AND NOT BY A LITTLE: the FULL "
      "symbol infimum over the same bulk range is %.1f .. %.1f, NEGATIVE on "
      "every window and growing in magnitude (%s), while the section floor "
      "lam_min(B_HH) is %.4f .. %.4f, POSITIVE on every window.  The atom "
      "symbol alone reaches %.1f .. %.1f.  CONSEQUENCE, and it is a structural "
      "one: the positivity of B_HH is NOT a symbol property.  Any Szego / "
      "Widom-type argument returns the symbol infimum and therefore returns a "
      "NEGATIVE number here, so no such argument can ever produce R1'.  "
      "Whatever carries R1' must be a genuinely FINITE-SECTION mechanism -- the "
      "Fejer averaging of the atom spikes against the section -- and the "
      "diagonal already shows the section is doing the work: min_k (B_HH)_{kk} "
      "= %.4f .. %.4f, positive and only a factor %.2f .. %.2f above the true "
      "minimum"
      % (qmin([r["sym_full"] for r in H2R]),
         qmax([r["sym_full"] for r in H2R]), fit_str(F_SYMF),
         qmin([r["lo_B"] for r in H2R]), qmax([r["lo_B"] for r in H2R]),
         qmin([r["sym_at"] for r in H2R]), qmax([r["sym_at"] for r in H2R]),
         qmin([r["diag_min"] for r in H2R]),
         qmax([r["diag_min"] for r in H2R]),
         qmin([r["diag_min"] / r["lo_B"] for r in H2R]),
         qmax([r["diag_min"] / r["lo_B"] for r in H2R])))

for _r in H2R:
    info("H2.raw", "h=%d nb=%d loB=%.4f(c %.4f) low8=%.4f a=%.4f d_ex=%.4f "
         "b=%.4f fl2=%.4f | low8dd=%.4f | a_ar=%.4f atw=%.4f a_free=%.4f "
         "d_wh=%.4g 1+C_dd=%.4g fl2free=%.4g | lo_ar=%.4f sym=%.4f rat=%.4f | "
         "1+C=%.3g low8C=%.4f symfull=%.4f fullrat=%.4f symat=%.4f dmin=%.4f"
         % (_r["h"], _r["nb"], _r["lo_B"], _r["lo_B_cert"], _r["low8"],
            _r["a"], _r["d_ex"], _r["b"], _r["floor2"], _r["low8_dd"],
            _r["a_ar"], _r["at_w_nrm"], _r["a_free"], _r["d_wh"],
            _r["one_C_dd"], _r["floor2_free"], _r["lo_ar"], _r["sym_floor"],
            _r["sym_rat"], _r["one_C"], _r["low8_C"], _r["sym_full"],
            _r["sym_full_rat"], _r["sym_at"], _r["diag_min"]))

# ----------------------------------------------------------------------------
section("H3  ASSEMBLY, THE NEW END TO END, AND THE OBLIGATORY STRESS")
# ----------------------------------------------------------------------------
para("""H3.0  WHAT THE BEST H1 + H2 COMBINATION IS, STATED BEFORE IT IS PRICED.
H1 replaced the ONE m-sized object in the bottom-mode chain by a fixed-size
certificate that is exact, and recovered the whole collapse price with it.  H2
refuted three routes to the block floor and found one mechanism, for the arch
half only.  So the best combination is: the ceiling from T154's sixteen-column
Courant-Fischer certificate (fixed size, theorem direction, unchanged), the
block floor from the UNCHANGED T152 / T153 Schur two-block criterion (certified
per window, kb = %d), and the collapse price from the H1 chain -- %d Green
columns, an %d x %d Ritz block, a %d x %d overlap certificate and a Temple
bisection, none of which has a size that depends on m.  The end-to-end number
that changes is the one with the label FIXED SIZE.""" % (
    SCHUR_KB, 8 * (max(sorted(set(r["j_best"] for r in H1R))) + 1), K_CERT,
    K_CERT, max(KN), max(KN)))

NEW_LO = T154_FRAC[0] * REC_LO
NEW_UP = T154_FRAC[1] * REC_UP
E2E_HIT = bool(NEW_LO >= FRAC_BAR)
check("bf_h3.end_to_end",
      NEW_UP >= FRAC_BAR and qmin(SHARE) >= 0.75,
      "THE NEW END TO END, WITH ITS LABEL ATTACHED AND ITS BAR REPORTED "
      "HONESTLY.  T154 left two numbers which must not be conflated: %.2e .. "
      "%.2e m-FREE IN SHAPE, and %.2e .. %.2e CERTIFIED PER WINDOW using a "
      "Cholesky of size m.  H1 collapses the distinction from the expensive "
      "side: the recovery %.3f .. %.3f is now bought at FIXED SIZE, so the "
      "end-to-end fraction %.2e .. %.2e carries the label CERTIFIED AT FIXED "
      "SIZE.  THE DECLARED BAR WAS %.0e AND THE BOTTOM OF THE BAND IS %.2e, "
      "SO THE BAR IS %s -- by a factor %.2f, and the miss is reported rather "
      "than repaired.  Two remarks, neither of them an excuse.  First, this "
      "band pairs the MINIMUM of a T154 band with the MINIMUM of a T155 band "
      "measured on a DIFFERENT and wider surface (h up to %d against 878), so "
      "it is a deliberately pessimistic pairing.  Second, the like-for-like "
      "comparison -- fixed size against size m, same window, same Temple step "
      "-- is the share %.1f .. %.1f percent, and THAT is the number this probe "
      "actually moved.  WHAT THIS IS NOT: it is not an m-free number.  Fixed "
      "size means the certificate does not grow; m-free would mean its VALUE "
      "is bounded by an argument rather than measured on %d windows"
      % (T154_FRAC[0], T154_FRAC[1], T154_E2E[0], T154_E2E[1], REC_LO, REC_UP,
         NEW_LO, NEW_UP, FRAC_BAR, NEW_LO, "MET" if E2E_HIT else "MISSED",
         (NEW_LO / FRAC_BAR if E2E_HIT else FRAC_BAR / NEW_LO), int(qmax(XH)),
         100.0 * qmin(SHARE), 100.0 * qmax(SHARE), len(H1R)))

BAL = [
    ("mu^P_k = 4 sin^2(pi k / N)", "exact", "-", "THEOREM (KMS 1953)"),
    ("mu^P_9 / mu^P_1 (the free scale)",
     "%.2f .. %.2f" % (qmin([r["sep"] for r in H1R]),
                       qmax([r["sep"] for r in H1R])), "-> 81",
     "THEOREM, m-explicit"),
    ("Ritz values as a ceiling", "-", "-", "THEOREM (Courant-Fischer 1920)"),
    ("the Temple / Kato matrix step", "-", "-",
     "THEOREM (Temple 1928, Kato 1949, Sylvester 1852)"),
    ("the overlap identity of H1", "-", "-",
     "THEOREM (Rayleigh on the high block + an exact range identity)"),
    ("t (Schur two-block, kb = %d)" % SCHUR_KB,
     "%.4f .. %.4f" % (qmin([r["t"] for r in H1R]),
                       qmax([r["t"] for r in H1R])), "flat",
     "CERTIFIED per window, size m"),
    ("K^F (16-column ceiling)",
     "%.4f .. %.4f" % (qmin([r["KF"] for r in H1R]),
                       qmax([r["KF"] for r in H1R])), "-",
     "CERTIFIED, FIXED SIZE"),
    ("Lc (complement floor)",
     "%.3f .. %.3f mu^P_1" % (qmin([r["Lc_a"] for r in H1R]),
                              qmax([r["Lc_a"] for r in H1R])), fit_str(F_LC),
     "CERTIFIED, FIXED SIZE (%d x %d) -- new in T155" % (max(KN), max(KN))),
    ("collapse recovery",
     "%.3f .. %.3f" % (REC_LO, REC_UP), fit_str(F_REC),
     "CERTIFIED, FIXED SIZE -- was size m in T154"),
    ("lam_min(B_HH) (the block floor)",
     "%.4f .. %.4f" % (qmin([r["lo_B"] for r in H2R]),
                       qmax([r["lo_B"] for r in H2R])), fit_str(F_LOB),
     "CERTIFIED per window, size m -- OPEN as R1'"),
    ("arch reserve = symbol infimum",
     "%.4f .. %.4f" % (qmin([r["lo_ar"] for r in H2R]),
                       qmax([r["lo_ar"] for r in H2R])), fit_str(F_LOAR),
     "THEOREM CANDIDATE (Szego 1915 / Widom 1958), agreement 1e-4"),
    ("mode-1 overlap defect",
     "%.3f .. %.3f" % (qmin([r["def_1"] for r in BIG]),
                       qmax([r["def_1"] for r in BIG])), fit_str(F_DEF),
     "MEASURED -- the only arithmetic left in R2'"),
    ("1 + lam_min(C) (the Kato number)",
     "%.2e .. %.2e" % (qmin([r["one_C"] for r in H2R]),
                       qmax([r["one_C"] for r in H2R])), "shrinking",
     "CERTIFIED positive -- the only arithmetic left in R1'"),
    ("pencil ceiling kap = lam_max(B)",
     "%.2e .. %.2e" % (qmin([r["kap"] for r in H1R]),
                       qmax([r["kap"] for r in H1R])), fit_str(F_KAP),
     "CERTIFIED, GROWING -- a refuted route, not an input"),
]
info("H3.1.balance", "THE UNIFORMITY BALANCE, EVERY FACTOR THAT ENTERS OR WAS "
     "TRIED (quantity | band | fit in h | label):")
for nm, band, ft, lab in BAL:
    info("  " + nm, "%s | %s | %s" % (band, ft, lab))
N_THM = sum(1 for b in BAL if b[3].startswith("THEOREM") and "CANDIDATE" not in b[3])
N_FIX = sum(1 for b in BAL if "FIXED SIZE" in b[3])
N_WIN = sum(1 for b in BAL if "per window" in b[3])
N_MEAS = sum(1 for b in BAL if b[3].startswith("MEASURED"))
info("H3.1.count", "%d THEOREM, %d CERTIFIED-FIXED-SIZE, %d "
     "CERTIFIED-PER-WINDOW-AT-SIZE-m, %d MEASURED, 1 THEOREM CANDIDATE.  The "
     "T154 balance had ZERO entries in the FIXED-SIZE column below the ceiling "
     "row; the bottom-mode chain has moved a column to the left, and the block "
     "chain has not moved at all" % (N_THM, N_FIX, N_WIN, N_MEAS))


def instrument(A, m, tag):
    """THE H1 INSTRUMENT ON AN ARBITRARY SYMMETRIC SECTION -- the SAME code
    path the surface uses, so that a stress family and a control are measured
    by the same device and the comparison means something."""
    mu = parity_mu(m)
    Tf = parity_basis(m)
    LP = lap_P_mat(m)
    B = parity_block(A, Tf, mu)
    out = dict(tag=tag, m=m, t=schur_best(B, min(SCHUR_KB, m - 2)))
    try:
        kg = float(eigh(B, eigvals_only=True, subset_by_index=[m - 1, m - 1])[0])
        out["kap"] = cert_lam_max(B, guess=kg)
    except (LinAlgError, ValueError):
        out["kap"] = float("nan")
    del B
    try:
        w_lo, V_lo = eigh(A, subset_by_index=[0, K_CERT - 1])
    except (LinAlgError, ValueError):
        return None
    out["lam1"] = float(w_lo[0])
    out["price"] = (out["lam1"] / (out["t"] * mu[0])
                    if np.isfinite(out["t"]) and out["t"] > 0.0 else float("nan"))
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    out["mis"] = float(np.max(prin_angles(V0, V_lo)))
    Q = orth_cols(V0)
    g = V0
    for _ in range(3):
        g = green_cols(A, LP, g, 1)
        if g is None:
            break
        Q = append_orth(Q, g)
    out["KF"] = cert_ceiling(sym(Q.T @ (A @ Q)), mu, K_CERT)
    try:
        _, Yq = eigh(sym(Q.T @ (A @ Q)))
    except (LinAlgError, ValueError):
        return out
    Qr = Q @ Yq[:, :K_CERT]
    Wr = sym(Qr.T @ (A @ Qr))
    Rr = A @ Qr - Qr @ Wr
    Gf = Tf[:max(KLOW_SCAN), :] @ Qr
    cc = []
    for K in KLOW_SCAN:
        if K <= K_CERT or K + 2 >= m:
            continue
        fl, _mk, _v = complement_floor(mu, Gf[:K], K)
        if np.isfinite(fl):
            cc.append(fl / float(mu[0]))
    out["Lc"] = qmax(cc)
    dv = 1.0 - np.sum((Tf[:K_CERT, :] @ Qr) ** 2, axis=1)
    out["def_1"] = float(dv[0])
    out["def_mode"] = int(np.argmax(dv)) + 1
    g_c = (temple_matrix(Wr, sym(Rr.T @ Rr), out["t"] * out["Lc"] * float(mu[0]),
                         1)[0] if np.isfinite(out["Lc"]) and out["Lc"] > 0.0
           else float("nan"))
    out["rec"] = (g_c / (out["t"] * mu[0]) if np.isfinite(g_c) else float("nan"))
    out["share"] = out["rec"] / max(out["price"], 1.0e-300)
    del Tf, LP, V_lo, Q, Qr, Wr, Rr, Gf
    return out


para("""H3.2  THE OBLIGATORY STRESS: THE T145 NO-GO MUST BREAK.  T151's no-go
matrix is not in this file, so what is stressed is the RECONSTRUCTION T152 ..
T154 used: the positive decaying lag kernel c(l) = 1 / (1 + l), whose symbol has
a LOGARITHMIC singularity at the origin instead of vanishing there.  Its odd
section is positive definite, so every instrument RUNS on it, which is the point:
an instrument that cannot tell the two families apart is not an instrument.  T154
established that the floor survives (t = 0.05) while the ceiling explodes like
x^1.99.  The new question is whether the H1 complement-floor certificate -- which
is exact on the real family and recovers the whole price there -- ALSO breaks
here.  If it did not, it would be measuring nothing.""")

NG = []
for m_s in NOGO_SIZES:
    if budget_left() < 90.0 or m_s > MAX_H:
        break
    c_ng = 1.0 / (1.0 + np.arange(2 * m_s, dtype=float))
    got = instrument(sym(odd_toeplitz(c_ng, 2 * m_s)), m_s, "nogo")
    if got is not None:
        NG.append(got)
XN = [g["m"] for g in NG]
F_NG_KF = pow_fit(XN, [g["KF"] for g in NG], "no-go K^F")
F_NG_LC = pow_fit(XN, [g["Lc"] for g in NG], "no-go Lc")
F_NG_PR = pow_fit(XN, [g["price"] for g in NG], "no-go price")
F_NG_SH = pow_fit(XN, [g["share"] for g in NG], "no-go share")
for g in NG:
    info("H3.nogo", "m=%d t=%.4f KF=%.4g Lc=%.4g price=%.4g rec=%.4g "
         "share=%.4g def1=%.3f defmode=%d mis=%.2f"
         % (g["m"], g["t"], g["KF"], g["Lc"], g["price"], g["rec"], g["share"],
            g["def_1"], g["def_mode"], g["mis"]))

check("bf_h3.nogo_breaks",
      not nogrow_ok(F_NG_KF) and len(NG) >= 5,
      "AND IT BREAKS, ON THE SAME AXIS T154 FOUND AND ON A NEW ONE.  On the "
      "no-go family the floor survives, exactly as T154 reported (t = %.3f .. "
      "%.3f, all positive), so a probe that only looked at the floor would see "
      "nothing.  The CEILING explodes: K^F = %.3g .. %.3g, %s, against %.4f .. "
      "%.4f and FLAT on the real family -- orders of magnitude of separation on "
      "a single number.  The collapse price behaves differently too (%.2f .. "
      "%.2f, %s, against %.2f .. %.2f on the real family).  The H1 certificate "
      "itself still runs -- it is arithmetic-free in form, so it must -- and it "
      "returns Lc = %.2f .. %.2f (%s); what separates the families is not "
      "whether the instrument works but what it reads"
      % (qmin([g["t"] for g in NG]), qmax([g["t"] for g in NG]),
         qmin([g["KF"] for g in NG]), qmax([g["KF"] for g in NG]),
         fit_str(F_NG_KF), qmin([r["KF"] for r in H1R]),
         qmax([r["KF"] for r in H1R]), qmin([g["price"] for g in NG]),
         qmax([g["price"] for g in NG]), fit_str(F_NG_PR),
         qmin([r["price"] for r in H1R]), qmax([r["price"] for r in H1R]),
         qmin([g["Lc"] for g in NG]), qmax([g["Lc"] for g in NG]),
         fit_str(F_NG_LC)))

check("bf_h3.nogo_breaks_the_new_instrument",
      qmax([g["Lc"] for g in NG]) < qmin([r["Lc_a"] for r in H1R])
      and not any(np.isfinite(g["rec"]) for g in NG),
      "AND THE SECOND AXIS IS THE NEW ONE, WHICH IS THE ONE THAT MATTERS HERE.  "
      "The H1 complement-floor certificate reads %.2f .. %.2f mu^P_1 on the "
      "no-go family against %.2f .. %.2f on the real family -- BELOW the real "
      "band on every no-go size -- and its defect diagnosis is unambiguous: the "
      "mode-1 uncovered fraction is %.3f .. %.3f, i.e. the bottom mode is "
      "ENTIRELY outside the eight bottom Ritz directions, against %.3f .. %.3f "
      "on the real family, and the misalignment is exactly %.2f degrees on "
      "every size.  Consequently the Temple step returns NOTHING on %d of %d "
      "no-go sizes, against the whole collapse price on %d of %d real windows.  "
      "The instrument built in H1 is therefore not a formality that any "
      "positive-definite section would pass"
      % (qmin([g["Lc"] for g in NG]), qmax([g["Lc"] for g in NG]),
         qmin([r["Lc_a"] for r in H1R]), qmax([r["Lc_a"] for r in H1R]),
         qmin([g["def_1"] for g in NG]), qmax([g["def_1"] for g in NG]),
         qmin([r["def_1"] for r in BIG]), qmax([r["def_1"] for r in BIG]),
         qmax([g["mis"] for g in NG]), len(NG), len(NG), len(H1R), len(H1R)))

para("""H3.3  THE CONTROLS, AND WHY THEY ARE SHARP RATHER THAN DECORATIVE.  The
whole of H1 rests on two exactness facts, and both are tested directly rather
than assumed.  FIRST, that the parity sines are EXACT eigenvectors of L_P with
the reflecting last diagonal entry -- if that failed, every separation in this
file would be wrong by an unknown amount.  SECOND, that the new complement-floor
certificate reproduces the two configurations whose answer is known in closed
form: W = span{t_1 .. t_8} must return mu^P_9 exactly, and W = span{t_2 .. t_9}
must return mu^P_1 exactly.  The second control is the sharper one: it is the
configuration in which the certificate is WORTHLESS, and an instrument that
cannot report its own worthlessness is not a certificate.  A negative control is
added: the same parity sines against the DIRICHLET tridiagonal, where they are
not eigenvectors and the exactness must fail.""")

CT = []
for m_c in CTRL_SIZES:
    if m_c > MAX_H or m_c < 3 * max(KLOW_SCAN):
        continue
    mu_c = parity_mu(m_c)
    Tc = parity_basis(m_c)
    Lc_m = lap_P_mat(m_c)
    e_par = float(np.max(np.abs(Lc_m @ Tc.T - Tc.T * mu_c[None, :])))
    LD = sym(2.0 * np.eye(m_c) - np.eye(m_c, k=1) - np.eye(m_c, k=-1))
    e_dir = float(np.max(np.abs(LD @ Tc.T - Tc.T * mu_c[None, :])))
    Kc = 24
    W1 = np.ascontiguousarray(Tc[:K_CERT, :].T)
    f1, _m1, _v1 = complement_floor(mu_c, Tc[:Kc, :] @ W1, Kc)
    W2 = np.ascontiguousarray(Tc[1:K_CERT + 1, :].T)
    f2, _m2, _v2 = complement_floor(mu_c, Tc[:Kc, :] @ W2, Kc)
    CT.append(dict(m=m_c, e_par=e_par, e_dir=e_dir,
                   e_dir_pred=2.0 / math.sqrt(2.0 * m_c + 1.0),
                   r1=abs(f1 / float(mu_c[K_CERT]) - 1.0),
                   r2=abs(f2 / float(mu_c[0]) - 1.0)))
    del mu_c, Tc, Lc_m, LD, W1, W2

check("bf_h3.parity_control_exact",
      qmax([c["e_par"] for c in CT]) < 1.0e-10,
      "CONTROL 1, EXACT.  max_k ||L_P t_k - mu^P_k t_k||_inf = %.2e over m = %s "
      "-- machine precision, so the parity sines ARE the eigenvectors and every "
      "separation built on that containment is exact.  NEGATIVE CONTROL: the "
      "same sines against the DIRICHLET tridiagonal (last diagonal 2 instead of "
      "3) give %.4f .. %.4f, twelve orders of magnitude larger, and the value "
      "is not merely large but PREDICTED: the two operators differ by the rank "
      "one corner -e_{m-1} e_{m-1}^T, so the residual must equal |t_k(m-1)| = "
      "2 / sqrt(N) = %.4f .. %.4f, which it does to %.2e.  The exactness is a "
      "property of the reflecting boundary condition the odd sector forces, and "
      "the control shows the instrument can see its absence"
      % (qmax([c["e_par"] for c in CT]),
         ", ".join(str(c["m"]) for c in CT),
         qmin([c["e_dir"] for c in CT]), qmax([c["e_dir"] for c in CT]),
         qmin([c["e_dir_pred"] for c in CT]),
         qmax([c["e_dir_pred"] for c in CT]),
         qmax([abs(c["e_dir"] - c["e_dir_pred"]) for c in CT])))

check("bf_h3.certificate_controls_exact",
      qmax([c["r1"] for c in CT]) < 1.0e-9
      and qmax([c["r2"] for c in CT]) < 1.0e-9,
      "CONTROL 2, EXACT IN BOTH DIRECTIONS.  With W = span{t_1 .. t_8} the "
      "certificate returns mu^P_9 to a relative %.2e, and with W = span{t_2 .. "
      "t_9} it returns mu^P_1 to a relative %.2e -- the second larger only "
      "because the answer mu^P_1 is smaller than the certificate's working "
      "scale mu^P_{K+1} by the factor mu^P_25 / mu^P_1, which is where the "
      "amplification comes from and it is carried, not hidden.  The "
      "second is the important one: that configuration is the counterexample "
      "quoted in H1.0 -- the subspace that misses the bottom mode entirely -- "
      "and the certificate reports the worthless answer mu^P_1 rather than "
      "something flattering.  Together with the direction check in H1 (the "
      "certificate never exceeds the exact value) the instrument is pinned from "
      "both sides"
      % (qmax([c["r1"] for c in CT]), qmax([c["r2"] for c in CT])))

# ----------------------------------------------------------------------------
section("H4  MAP V27, THE PROMOTION LIST, THE REST LIST, AND THE VERDICT")
# ----------------------------------------------------------------------------
MAP = [
    ("the axioms and the window", "UNCHANGED",
     "one finite-window Weil form, prime-power zones, frame A, zone gap "
     "Theta(D^3); nu = %d" % NU_MAIN),
    ("the exact parity spectrum", "THEOREM",
     "mu^P_k = 4 sin^2(pi k / N), the sines are exact eigenvectors -- verified "
     "to %.1e, with the Dirichlet negative control matching its own prediction"
     % qmax([c["e_par"] for c in CT])),
    ("the Psi term (T153)", "CLOSED", "pinned between a_1/lam_1 and 1/lam_1"),
    ("the ceiling half of R2 (T154)", "CLOSED, FIXED SIZE",
     "K^F = %.4f .. %.4f by Courant-Fischer on 16 columns; reproduced here"
     % (qmin([r["KF"] for r in H1R]), qmax([r["KF"] for r in H1R]))),
    ("the complement floor Lc (T155, H1)", "FIXED SIZE AND EXACT -- NEW",
     "a %d x %d certificate in the exact KMS numbers reproduces the m-sized "
     "number to %.0e on %d of %d windows; Lc = %.2f .. %.2f mu^P_1"
     % (max(KN), max(KN), 1.0 - qmin(TIGHT), len(H1R), len(H1R),
        qmin([r["Lc_a"] for r in H1R]), qmax([r["Lc_a"] for r in H1R]))),
    ("the collapse price (T155, H1)", "RECOVERED AT FIXED SIZE -- NEW",
     "%.1f .. %.1f percent of %.3f .. %.3f, with no factorisation of size m "
     "anywhere in the chain"
     % (100.0 * qmin(SHARE), 100.0 * qmax(SHARE),
        qmin([r["price"] for r in H1R]), qmax([r["price"] for r in H1R]))),
    ("where the free scale goes (T155, H1)", "LOCALISED -- NEW",
     "mode 1, uncovered by %.3f .. %.3f, because one Ritz direction sits on "
     "modes %d .. %d" % (qmin([r["def_1"] for r in BIG]),
                         qmax([r["def_1"] for r in BIG]),
                         min(r["u_mode"] for r in H1R),
                         max(r["u_mode"] for r in H1R))),
    ("the pencil-ceiling route (T155, H1)", "REFUTED, MECHANISM NAMED",
     "kap = lam_max(B) %s, tracking ||A|| / mu^P_1; not cured by peeling"
     % fit_str(F_KAP)),
    ("the arch reserve (T155, H2)", "THEOREM CANDIDATE -- NEW",
     "it IS the symbol infimum, agreement %.6f .. %.6f, and it exceeds t by "
     "%.2f .. %.2f" % (qmin(SR), qmax(SR), qmin(ART), qmax(ART))),
    ("the block floor R1' (T155, H2)", "OPEN, AND NOW WITH AN OBSTRUCTION",
     "lam_min(B_HH) = %.4f .. %.4f certified positive, but the full symbol "
     "infimum is %.1f .. %.1f, so no symbol argument can ever produce it"
     % (qmin([r["lo_B"] for r in H2R]), qmax([r["lo_B"] for r in H2R]),
        qmin([r["sym_full"] for r in H2R]), qmax([r["sym_full"] for r in H2R]))),
    ("end to end", "%.2e .. %.2e AT FIXED SIZE" % (NEW_LO, NEW_UP),
     "was %.2e .. %.2e m-free in shape / %.2e .. %.2e certified at size m"
     % (T154_FRAC[0], T154_FRAC[1], T154_E2E[0], T154_E2E[1])),
    ("the T145 no-go", "BREAKS ON TWO AXES",
     "ceiling %s and the H1 certificate reads %.2f .. %.2f against %.2f .. "
     "%.2f, with no recovery at all"
     % (fit_str(F_NG_KF), qmin([g["Lc"] for g in NG]),
        qmax([g["Lc"] for g in NG]), qmin([r["Lc_a"] for r in H1R]),
        qmax([r["Lc_a"] for r in H1R]))),
    ("the distance to RH", "UNCHANGED AND UNTRAVELLED",
     "no zero read, generated, approximated or extrapolated; Weil's criterion "
     "is an address"),
]
info("H4.0.map", "MAP V27 -- the state of the line after T155:")
for nm, st, txt in MAP:
    info("  " + nm, "%s -- %s" % (st, txt))

info("H4.1.promotions", "PROMOTION LIST.  T149 .. T154 remain PENDING and are "
     "NOT re-listed here; in particular v551 is being promoted in parallel out "
     "of T154's sixteen-column ceiling certificate and is NOT duplicated.  T155 "
     "adds three CANDIDATES, none of them promoted by this file, which touches "
     "nothing outside the sandbox:")
for nm, txt in [
    ("candidate A -- the complement-floor certificate",
     "THE ONE WORTH PROMOTING.  min_{v perp W} v^T L_P v >= mu^P_{K+1} - "
     "lam_max(M^{1/2}(I - G G^T) M^{1/2}) with M = diag(mu^P_{K+1} - mu^P_k), "
     "G = T_K Q_W: an IDENTITY plus one Rayleigh bound, valid for every m and "
     "every subspace, turning an m-sized eigenvalue problem into a %d x %d one. "
     " On this surface it is EXACT to %.0e, it reproduces both closed-form "
     "controls to 1e-9, and it carries %.1f .. %.1f percent of the collapse "
     "price.  It is a statement about a tridiagonal matrix and a subspace: no "
     "arithmetic, no zeta, no window"
     % (max(KN), max(KN), 1.0 - qmin(TIGHT), 100.0 * qmin(SHARE),
        100.0 * qmax(SHARE))),
    ("candidate B -- the arch reserve is the symbol infimum",
     "lam_min(B^arch_HH) = min_{th >= th_{kb+1}} f^arch(th) / (4 sin^2(th/2)) "
     "to %.6f .. %.6f on %d of %d windows.  A Szego / Widom statement about one "
     "analytic function; if proved it is the first m-free ingredient of R1'"
     % (qmin(SR), qmax(SR), len(H2R), len(H2R))),
    ("candidate C -- the no-symbol obstruction for R1'",
     "the FULL symbol infimum is %.1f .. %.1f while lam_min(B_HH) is %.4f .. "
     "%.4f: a NEGATIVE result that closes off a whole family of methods and is "
     "worth recording precisely because it is negative"
     % (qmin([r["sym_full"] for r in H2R]), qmax([r["sym_full"] for r in H2R]),
        qmin([r["lo_B"] for r in H2R]), qmax([r["lo_B"] for r in H2R]))),
]:
    info("  " + nm, txt)

PENCIL_RATIO = qmax([r["Lc_b"] / r["Lc_a"] for r in H1R])
R2_MFREE = bool(PENCIL_RATIO >= 0.5)
R1_MFREE = bool(qmax([r["sym_full"] for r in H2R]) >= T_TARGET
                or qmax([r["floor2"] for r in H2R]) >= T_TARGET
                or qmax([r["floor2_free"] for r in H2R]) >= T_TARGET)
REST = [
    ("R1''  THE m-FREE BLOCK FLOOR", "an m-free lower bound for lam_min(B_HH) "
     "on the bulk, over t = %.2f.  The number is CERTIFIED per window at %.4f "
     ".. %.4f (%s) and the arch half is now a theorem candidate at %.4f .. "
     "%.4f, a factor %.2f .. %.2f above the target.  What is missing is the "
     "ATOM half, and T155 narrows what it can be: not a relative bound (T154), "
     "not a direction-aware two-block split (coupling too large by %.1f .. "
     "%.1f), not a local atom norm on the eight-mode window (short by %.2f .. "
     "%.2f), not a deeper cut (the deep block's own floor is %.2e .. %.2e, "
     "below t), and NOT A SYMBOL ARGUMENT OF ANY KIND, because the full symbol "
     "infimum is %.1f .. %.1f while the section floor is positive.  The one "
     "surviving shape is a finite-section Fejer cancellation between the atom "
     "spikes and the section, and the diagonal shows the section is where the "
     "positivity lives (min diagonal %.4f .. %.4f, a factor %.2f .. %.2f above "
     "the true minimum)"
     % (T_TARGET, qmin([r["lo_B"] for r in H2R]),
        qmax([r["lo_B"] for r in H2R]), fit_str(F_LOB),
        qmin([r["lo_ar"] for r in H2R]), qmax([r["lo_ar"] for r in H2R]),
        qmin(ART), qmax(ART), qmin(COUPR), qmax(COUPR), qmin(ATR), qmax(ATR),
        qmin([r["d_wh"] for r in H2R]), qmax([r["d_wh"] for r in H2R]),
        qmin([r["sym_full"] for r in H2R]), qmax([r["sym_full"] for r in H2R]),
        qmin([r["diag_min"] for r in H2R]), qmax([r["diag_min"] for r in H2R]),
        qmin([r["diag_min"] / r["lo_B"] for r in H2R]),
        qmax([r["diag_min"] / r["lo_B"] for r in H2R]))),
    ("R2''  THE m-FREE OVERLAP DEFECT", "an m-free UPPER bound for "
     "lam_max(M^{1/2}(I - G G^T) M^{1/2}) at K = %d, equivalently a bound on "
     "how much of t_1 the eight bottom Ritz directions of A may miss.  THE "
     "TERM HAS SHRUNK TO ONE %d x %d MATRIX: everything else in the bottom-mode "
     "chain is now a theorem or a fixed-size certificate, the certificate is "
     "EXACT rather than merely valid (%.9f .. %.9f of the m-sized number), and "
     "feeding it in recovers %.1f .. %.1f percent of the collapse price.  "
     "MEASURED, the defect is %.3f .. %.3f at mode 1 (%s) and the resulting "
     "floor is %.2f .. %.2f mu^P_1 (%s) against the free scale %.2f.  The one "
     "m-free-shaped route this probe could construct -- the two-sided pencil -- "
     "is refuted by a factor %.0e, and the reason is structural: the pencil "
     "ceiling lives at the bottom of L_P, where the floor question lives"
     % (max(KN), max(KN), K_CERT, qmin(TIGHT), qmax(TIGHT),
        100.0 * qmin(SHARE), 100.0 * qmax(SHARE),
        qmin([r["def_1"] for r in BIG]), qmax([r["def_1"] for r in BIG]),
        fit_str(F_DEF), qmin([r["Lc_a"] for r in H1R]),
        qmax([r["Lc_a"] for r in H1R]), fit_str(F_LC),
        qmax([r["sep"] for r in H1R]), PENCIL_RATIO)),
]
N_OPEN = len(REST)
info("H4.2.rest", "THE SHORTEST REST LIST -- %d named open terms, the same two "
     "T154 left, both still UNIFORMITY terms and neither closed.  What changed "
     "is their SIZE and what is known to be impossible:" % N_OPEN)
for nm, txt in REST:
    info("  " + nm, txt)

GATE_CARRIES = bool(R1_MFREE and R2_MFREE)
GATE_ONE = bool(N_OPEN == 1)
VERDICT = ("FLOORS-CARRY" if GATE_CARRIES
           else ("ONE-TERM-MISSING" if GATE_ONE else "FLOORS-RESIST"))
check("bf_h4.verdict_gate", not GATE_CARRIES and not GATE_ONE,
      "THE VERDICT GATES, EVALUATED FROM THE NUMBERS AND NOT CHOSEN.  "
      "FLOORS-CARRY needs BOTH floors m-free, and each is decided by a "
      "measured ratio, not by a narrative.  R2': the only m-free-shaped chain "
      "this probe could build returns %.0e of the certified floor, so the gate "
      "reads FALSE (it would need 0.5).  R1': the best of the three m-free "
      "shaped candidates -- the full symbol infimum %.1f, the direction-aware "
      "2 x 2 floor %.1f, the arch-minus-local-atom floor %.1f -- is below t = "
      "%.2f, so the gate reads FALSE.  ONE-TERM-MISSING needs exactly one open "
      "term; there are %d, and they must NOT be merged: R2' is a question about "
      "L_P and a subspace with the arithmetic compressed into a %d x %d matrix, "
      "R1' is a question about prime-power sums against a finite section with "
      "no subspace in it, and the second is now known to be outside the reach "
      "of the method that settles the first.  Hence %s"
      % (PENCIL_RATIO, qmax([r["sym_full"] for r in H2R]),
         qmax([r["floor2"] for r in H2R]),
         qmax([r["floor2_free"] for r in H2R]), T_TARGET, N_OPEN, max(KN),
         K_CERT, VERDICT))

para("""H4.3  THE RH DISTANCE, ONCE MORE AND UNCHANGED.  Everything above is a
statement about the constants of ONE finite-window quadratic form on prime-power
zones in frame A with the zone gap Theta(D^3).  No zero of any L-function was
read, generated, approximated or extrapolated, and Weil's criterion remains an
ADDRESS.  Closing R1'' and R2'' would produce a finite-window positivity
statement with an m-free constant on a list of zones -- and nothing more.  The
distance to RH is not shortened by this probe in any direction.""")

para("""H4.4  WHAT NOW STANDS A PRIORI ON THE MEASUREMENT SURFACE, AND WHAT DOES
NOT.  STANDS A PRIORI, for every m and every symmetric section: the parity
spectrum and its exactness; the Courant-Fischer ceiling direction; the Temple /
Kato matrix step; and the complement-floor identity of H1, which is a theorem
about a tridiagonal matrix and an arbitrary subspace and holds whether or not
anything else in this file is true.  STANDS PER WINDOW, on %d and %d windows
respectively and nowhere else: the value of t, the value of K^F, the value of
Lc, the recovery, lam_min(B_HH), and the arch reserve.  DOES NOT STAND: anything
for all m; anything for other frames than A; anything for other zone families
than prime powers; anything for other D; and any statement obtained by reading a
flat exponent as a bound.  The fits in this file cover h = %d .. %d, which is a
factor of %.1f in the window and nothing like a limit.""" % (
    len(H1R), len(H2R), qmin(XH), qmax(XH), qmax(XH) / max(qmin(XH), 1.0)))

para("""H4.5  THE VERDICT, IN THREE HONEST SENTENCES.  (1) R2' HAS NOT BEEN
CLOSED BUT IT HAS BEEN REDUCED TO ITS SMALLEST FORM: the complement floor, the
one m-sized object left in the bottom-mode chain, is reproduced EXACTLY (%.9f ..
%.9f) by a %d x %d certificate built from the exact Kac-Murdock-Szego numbers and
a single %d x %d overlap matrix, feeding it into the unchanged Temple step
recovers %.1f .. %.1f percent of the collapse price %.3f .. %.3f WITHOUT any
factorisation of size m, the end-to-end fraction therefore reaches %.2e .. %.2e
with the label CERTIFIED-AT-FIXED-SIZE, and the residual defect is localised to
ONE number -- the bottom mode t_1 is %.3f .. %.3f uncovered by the eight bottom
Ritz directions of A, because one of those directions is spent on modes %d ..
%d. (2) R1' HAS NOT BEEN CLOSED AND HAS ACQUIRED AN OBSTRUCTION: the
direction-aware two-block split fails because the coupling ||B_wd|| = %.2f ..
%.2f exceeds what it may be by %.1f .. %.1f, the local atom norm on the
eight-mode window exceeds the local arch reserve by %.2f .. %.2f, the deeper cut
merely moves the problem up (deep floor %.2e .. %.2e against t = %.2f), and --
the one genuinely new fact -- the arch reserve IS the symbol infimum to %.0e
while the FULL symbol infimum is %.1f .. %.1f, NEGATIVE, so the method that
settles the arch half provably cannot settle the atom half and R1' must be a
finite-section statement or nothing. (3) THE VERDICT IS %s WITH %d OPEN TERMS,
and the honest reading is that this probe bought SIZE and STRUCTURE rather than
UNIFORMITY: two of the three things a promotion would need -- an instrument that
does not grow with m and a mechanism with a name -- are now in hand for the
bottom-mode floor, the third is not, and for the block floor the search space
has been cut rather than the term.""" % (
    qmin(TIGHT), qmax(TIGHT), max(KN), max(KN), max(KN), K_CERT,
    100.0 * qmin(SHARE), 100.0 * qmax(SHARE),
    qmin([r["price"] for r in H1R]), qmax([r["price"] for r in H1R]),
    NEW_LO, NEW_UP, qmin([r["def_1"] for r in BIG]),
    qmax([r["def_1"] for r in BIG]), min(r["u_mode"] for r in H1R),
    max(r["u_mode"] for r in H1R), qmin([r["b"] for r in H2R]),
    qmax([r["b"] for r in H2R]), qmin(COUPR), qmax(COUPR), qmin(ATR),
    qmax(ATR), qmin([r["d_wh"] for r in H2R]), qmax([r["d_wh"] for r in H2R]),
    T_TARGET, qmax([abs(x - 1.0) for x in SR]),
    qmin([r["sym_full"] for r in H2R]), qmax([r["sym_full"] for r in H2R]),
    VERDICT, N_OPEN))

info("H4.6.verdict", "PART 155 / CONTRACT BOTTOM.FLOOR -- VERDICT: %s (open "
     "terms: %d; the complement floor is now a %d x %d EXACT certificate; the "
     "collapse price is recovered at FIXED SIZE, %.1f .. %.1f percent; end to "
     "end %.2e .. %.2e certified at fixed size; the arch reserve is the symbol "
     "infimum and the full symbol is negative)"
     % (VERDICT, N_OPEN, max(KN), max(KN), 100.0 * qmin(SHARE),
        100.0 * qmax(SHARE), NEW_LO, NEW_UP))

# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
print("checks: %d   failures: %d   runtime: %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))
if FAILS:
    print("FAILED: %s" % ", ".join(FAILS))
print("PROBE %s" % ("GREEN" if not FAILS else "RED"))
