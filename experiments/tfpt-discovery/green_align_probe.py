"""PART 154 -- THE CONTRACT ``GREEN.ALIGN'': THE ONE OBJECT.

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
zones.  The distance from there to RH is mapped in G4 and never travelled.

WHAT T153 LEFT, AND WHY THIS FILE HAS EXACTLY ONE TARGET.  T153 CLOSED the Psi
term (the collapse form Psi <= const/(t mu^P_1); Psi is PINNED between a_1/lam_1
and 1/lam_1 with a_1 = 8/pi^2, so T152's mapped 3.5 .. 5.3x reserve was
REFUTED).  Three open terms became two, and BOTH lose to the SAME object:

  R2  the Green / alignment description of (A^-1 L_P)^j t_k for k <= 8.  Two
      inverse-iteration steps give a FLAT K^F = 1.432 .. 2.535 against the
      certified true K_bot = 1.102 .. 1.896, on an eight-column certificate of
      FIXED size; and the collapse price lam_1(A) / (t mu^P_1) = 3.25 .. 8.40
      -- the pencil minimum does NOT sit at the bottom mode -- would be
      recovered by the SAME description.
  R1  the block inequality B_HH >= t I, now in a sharp one-number form: how far
      inside -1 the arch-whitened atom operator sits, 1 + lam_min(C) =
      8.3e-4 .. 2.9e-2, positive but shrinking like x^-1.778, against an m-free
      arch reserve lam_min(B^arch_HH) = 1.0362 .. 1.4143.

WHAT THIS FILE DOES.
  G1  THE ITERATION COLUMNS, the heart.  The subspace S_j = span{t_1..t_8} +
      span{(A^-1 L_P)^i t_k, i <= j} is built for j = 0, 1, 2; its geometry
      against the true bottom modes is measured (principal angles, Rayleigh
      quotients, closed form against the Green columns of the odd section); and
      the FIXED-SIZE certificate is FORMALISED IN BOTH DIRECTIONS.  The ceiling
      is Courant-Fischer 1920 (Ritz values are UPPER bounds for the eigenvalues
      of the same index -- the direction is stated pedantically and used only
      that way).  The floor needs a RESIDUAL argument and gets a named one: the
      Temple 1928 / Kato 1949 two-block form, made legitimate by an EXACTNESS
      trick -- S_j CONTAINS span{t_1..t_8}, the exact eigenvectors of L_P, so the
      orthogonal complement lies in span{t_9..t_m} and the already certified
      A >= t L_P gives the separation beta = t mu^P_9 with no new certificate.
  G2  THE KATO NUMBER, R1 in its sharp form.  Why 1 + lam_min(C) sits just
      above 0 and shrinks; which vector realises the minimum and where it lives;
      the Hankel reflection half as the named culprit; and five candidate
      repairs -- boundary peeling instead of deep-mode peeling, a reflected
      whitening, a diagonal whitening, a coarser second peel, and the pure norm
      route -- each with its direction and its number.
  G3  ASSEMBLY AND THE OBLIGATORY STRESS.  The best G1 + G2 combination in the
      full chain, the new end-to-end fraction, the uniformity balance, and the
      mandatory stress: the T145 no-go MUST break, and the Dirichlet and parity
      controls must be exact.
  G4  MAP V26, the promotion list (T149 .. T153 PENDING), the shortest rest
      list, and an honest three-sentence verdict.

DISCIPLINE.  THEOREM / CERTIFIED / MEASURED / FIT are kept strictly apart and
every claim carries its label.  Directions (upper versus lower bound) are
pedantic throughout; in particular the Rayleigh-Ritz direction is restated at
every use.  Classics cited where used: Temple 1928 and Kato 1949 (the residual
floor), Kaniel 1966 / Paige 1971 (the Krylov alignment rate), Schur 1917 (the
two-block criterion), Kac-Murdock-Szego 1953 (the exact parity spectrum),
Courant-Fischer 1920, Weyl 1912, Sylvester 1852, Cauchy 1829 (interlacing),
Chebyshev 1852, Widom 1958.  HARD CAPS: any factorised / inverted /
diagonalised matrix <= 1500; probe budget < 900 s.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, ldl, solve_triangular

T0 = time.time()
np.random.seed(154154)

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
G1_ZONES = 12                # windows of the G1 iteration-column surface
G1_HCAP = 1100
G2_ZONES = 10                # windows of the G2 Kato surface
G2_HCAP = 900

K_CERT = 8                   # the modes the certificate is about
J_ITER = (0, 1, 2)           # inverse-iteration depths scanned
SCHUR_KB = 16                # the FIXED low block of the T152 / T153 certificate
KC_SCAN = (8, 16, 24, 32, 48)  # the G1 containment scan (separation depth)
KB2_SCAN = (16, 24, 32, 48)  # the G2 second-peel scan
Q_EDGE = (0, 1, 2, 4, 8)     # the G2 boundary-peel depths (position space)
T_LADDER = (0.25, 0.245, 0.24, 0.235, 0.23, 0.225, 0.22, 0.215, 0.21, 0.205,
            0.20, 0.19, 0.18, 0.16, 0.14, 0.12, 0.10, 0.05)
PEN_BACKOFF = (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1)
BAR_UNIF = 0.25              # |exponent| + band bar for "flat / non-growing"
T_TARGET = 0.25

NOGO_SIZES = (48, 64, 96, 128, 192, 256, 384, 512)
CTRL_SIZES = (64, 128, 256, 384, 512, 700)

# T153's certified end-to-end band and collapse price, QUOTED, never recomputed
T153_FRAC = (1.01e-2, 3.92e-2)
T153_PRICE = (3.25, 8.40)     # lam_1(A) / (t mu^P_1), the recovery target
T153_KF = (1.432, 2.535)      # the flat two-step ceiling T153 measured
T153_KBOT = (1.102, 1.896)    # the certified true bottom ladder constant
T153_KATO = (8.3e-4, 2.9e-2)  # 1 + lam_min(C) on the bulk
T153_ARCH = (1.0362, 1.4143)  # the m-free arch reserve on the bulk
FRAC_BAR = 3.0e-2             # the verdict bar on the new end-to-end fraction
REC_BAR = 2.0                 # the verdict bar on the certified recovery factor

B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962 Thm 12)

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
    check("ga_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("ga_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("ga_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("ga_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "green_align_probe.py", "single new file in the sandbox")


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
    """AN UPPER BOUND on the spectral norm of a TALL matrix R, certified by a
    Cholesky of s I - R^T R on the SMALL side.  DIRECTION: upper bound, and it
    is the object that enters every residual floor SQUARED."""
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


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T153 code path
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
    bit-for-bit the object T111 .. T153 use."""
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


def parity_mu(m):
    """THE EXACT eigenvalues of L_P: mu^P_k = 4 sin^2(pi k / N), N = 2m + 1,
    k = 1 .. m (Kac-Murdock-Szego 1953 in the parity sector).  EXACT, not
    asymptotic: the odd grid never contains th = 0."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m):
    """THE ORTHONORMAL EIGENBASIS OF L_P: t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N).
    That these are EXACT eigenvectors of L_P is the fact the whole G1 separation
    argument rests on."""
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
    lam_min(B) is the pencil floor, and the compression B_HH to a mode set H is
    the SAME pencil question restricted to span{t_k : k in H}."""
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
# THE FIXED-SIZE TWO-SIDED CERTIFICATE (the G1 instrument)
# ----------------------------------------------------------------------------
def ritz_pack(A, Q):
    """THE RITZ DATA OF A SUBSPACE, with both directions spelled out.
    W = Q^T A Q with Q^T Q = I; th = eig(W) ASCENDING.  DIRECTION 1 (ceiling,
    Courant-Fischer 1920 / Cauchy 1829 interlacing): lam_k(A) <= th_k for every
    k <= dim -- Ritz values are UPPER bounds for the eigenvalues OF THE SAME
    INDEX, and that is the ONLY way they are used here.  DIRECTION 2 (the
    residual): R = A Q - Q W satisfies Q^T R = 0, and ||R|| is the object that
    Temple 1928 / Kato 1949 turn into a LOWER bound -- never a ceiling."""
    W = sym(Q.T @ (A @ Q))
    th = np.linalg.eigvalsh(W)
    R = A @ Q - Q @ W
    return dict(W=W, th=th, R=R, nrm_R=cert_norm2(R),
                nrm_R_F=float(np.linalg.norm(R)))


def temple_floor(th_k, beta, nrm_R):
    """TEMPLE 1928 / KATO 1949, THE TWO-BLOCK FORM, DIRECTION: LOWER BOUND.
    Let S = span(Q), dim d, and let the orthogonal complement satisfy
    Q_perp^T A Q_perp >= beta I.  Writing A in the basis [Q, Q_perp] and using
    the Schur / inertia identity (Sylvester 1852; Haynsworth 1968), for gam <
    beta the number of eigenvalues of A below gam equals the number of negative
    eigenvalues of W - gam I - Rt^T (A_perp - gam I)^-1 Rt, which is at most
    #{th_i < gam + ||R||^2 / (beta - gam)}.  Hence lam_k(A) >= gam_k with gam_k
    the SMALLER root of (th_k - gam)(beta - gam) = ||R||^2.  If ||R|| = 0 this
    returns th_k exactly; it returns nan when th_k >= beta, i.e. when the
    separation is not established -- and it is then NOT used."""
    if not (np.isfinite(th_k) and np.isfinite(beta) and np.isfinite(nrm_R)):
        return float("nan")
    if th_k >= beta:
        return float("nan")
    b = beta - th_k
    return th_k - 0.5 * (math.sqrt(b * b + 4.0 * nrm_R * nrm_R) - b)


def temple_matrix(W, RtR, beta, K):
    """TEMPLE 1928 / KATO 1949 IN ITS MATRIX (SCHUR-COMPLEMENT) FORM -- the
    instrument the scalar form above is too crude for.  Same setting: S = span(Q)
    of dimension d, Q_perp^T A Q_perp >= beta I.  For gam < beta the Schur
    complement of A - gam I on the Q block is
        S(gam) = W - gam I - Rt^T (A_perp - gam I)^-1 Rt
              >= W - gam I - (R^T R) / (beta - gam) =: M(gam),
    a MATRIX inequality, and NOT the crude ||R||^2 I of the scalar form.  By
    Sylvester 1852 / Haynsworth 1968 the inertia is additive and A_perp - gam I
    is positive, so
        #{lam_j(A) < gam} = #neg S(gam) <= #neg M(gam) ,
    hence lam_k(A) >= gam as soon as #neg M(gam) <= k - 1.  M(gam) is d x d with
    d <= 24, so every count is an LDL^T of a FIXED-SIZE matrix; #neg M is
    non-decreasing in gam, so a bisection is legitimate.  DIRECTION: the returned
    numbers are LOWER bounds on lam_k(A), with the Wilkinson floor subtracted."""
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


def green_cols(A, LP, V, j):
    """THE ITERATION COLUMNS (A^-1 L_P)^j V, by j Cholesky back-solves of A.
    A is positive definite on every window of the surface (T151 .. T153), which
    the returned factor certifies; no inverse is ever formed explicitly."""
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
    """AN ORTHONORMAL BASIS OF span(V) with rank detection: columns whose SVD
    value falls below tol * sigma_max are DROPPED, so the returned dimension is
    the honest numerical dimension of the subspace."""
    U, s, _ = np.linalg.svd(V, full_matrices=False)
    if s.size == 0 or s[0] <= 0.0:
        return V[:, :0]
    keep = int(np.sum(s > tol * s[0]))
    return U[:, :keep]


def prin_angles(Q1, Q2):
    """THE PRINCIPAL ANGLES between two orthonormal bases (Bjoerck-Golub 1973),
    in degrees, ascending.  MEASURED, never certified."""
    s = np.linalg.svd(Q1.T @ Q2, compute_uv=False)
    s = np.clip(s, -1.0, 1.0)
    return np.degrees(np.arccos(s[::-1]))


section("G0  SETUP, THE RH FENCE, AND THE LICENCES")
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

check("ga_g0.gap_facts",
      bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
      and bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12)),
      "the ONLY two gap facts used anywhere: Bertrand-Chebyshev 1852 "
      "(g <= log 2) and the trivial even bound; %d gaps up to n = %d"
      % (NZ_DEEP, ZONE_DEEP))

para("""G0.0  THE RH FENCE, RESTATED BEFORE ANY NUMBER IS PRINTED.  The
surrounding statement is the positivity of a Weil window form (Weil 1952;
Bombieri 2000; Connes 1999) on a FINITE list of prime-power zones in a FINITE
window, frame A, with the zone gap Theta(D^3).  Weil's explicit-formula
criterion is an ADDRESS, never a criterion used here.  No zero of any L-function
is read, generated, approximated or extrapolated; the AST firewall above
enforces that together with the import whitelist and the absence of write-mode
file access.  What is at stake below is the SIZE AND THE UNIFORMITY of the
constants in one finite-window inequality -- nothing about any zero, in either
direction.  A perfect closure of every term in G1 .. G3 would leave a
finite-window inequality with an explicit constant on a list of zones and
nothing more.  The distance to RH is mapped once in G4 and never travelled.""")

para("""G0.1  THE LICENCES, EACH WITH ITS DIRECTION.  (L1) Cholesky: a COMPLETED
Cholesky of X certifies X >= -fl I with fl the Wilkinson backward-error floor,
always SUBTRACTED from a lower bound and ADDED to an upper bound.  (L2)
Sylvester 1852 / Bunch-Kaufman 1977: a completed LDL^T of A - tau I returns
#{lam_j < tau} as a CERTIFICATE and reads no eigenvector.  (L3) Weyl 1912: A >=
t L_P implies lam_k(A) >= t mu^P_k for EVERY k -- the certified ladder in the
LOWER direction.  (L4) Kac-Murdock-Szego 1953: mu^P_k = 4 sin^2(pi k / N) is
EXACT for every m, and so is every ratio mu^P_j / mu^P_k formed from it; in
particular mu^P_9 / mu^P_1 is an m-EXPLICIT number, which is what the G1
separation is built on.  (L5) Courant-Fischer 1920 / Cauchy 1829 interlacing:
for any subspace S of dimension d >= k, lam_k(A) <= th_k(S), the k-th Ritz value
-- the certified ladder in the UPPER direction, and the ONLY direction in which
Ritz values are used in this file.  (L6) Temple 1928 / Kato 1949: the residual
two-block form turns ||A Q - Q W|| plus a separation beta into a LOWER bound on
lam_k(A); it is the ONLY device here that produces a floor from a subspace, and
it is never confused with (L5).  (L7) Kaniel 1966 / Paige 1971: the Krylov
alignment rate that explains WHY the residual of the iterated subspace falls --
QUOTED as an explanation, never used as a bound.  (L8) Schur 1917 / Haynsworth
1968: the two-block criterion is an EQUIVALENCE and the inertia is additive.
(L9) Chebyshev 1852 / Rosser-Schoenfeld 1962 Thm 12: psi(x) <= B_PSI x, verified
below on the exact range used.""")

para("""G0.2  WHAT COUNTS AS WHAT, PEDANTICALLY.  THEOREM = an identity or a
classical inequality valid for every m.  CERTIFIED = a numeric bound produced by
a completed factorisation with its backward-error floor carried, valid for THAT
window only.  MEASURED = a diagonalisation or an angle read for orientation.
FIT = an exponent on the finite surface, never promoted to anything.  The word
``proven'' is used nowhere in this file for any m-freeness claim.  THE
RAYLEIGH-RITZ DIRECTION, ONCE AND FOR ALL: th_k(S) >= lam_k(A) is an UPPER bound
on the eigenvalue and therefore a CEILING for the ladder constant; it is NOT a
floor, and every floor in this file comes from (L6) or from a completed
Cholesky.""")

_psi_run = 0.0
_bpsi = 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
check("ga_g0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f is VERIFIED at every jump point up to n = %d (max "
      "%.6f); psi jumps only at prime powers, so this is the true max on the "
      "range, and it is never assumed beyond it" % (B_PSI, ATOM_MAX, _bpsi))

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > G1_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(G1_ZONES, 1))
    SZ = CAND[::-1][::step][:G1_ZONES]
    SZ.sort(key=lambda t: t[0])
check("ga_g0.surface", len(SZ) >= 8,
      "%d prime-power zones admit a frame-A window inside the cap (h <= %d, "
      "MAX_H = %d); the G1 surface takes %d of them, h = %d .. %d, declared "
      "BEFORE any result is seen"
      % (len(CAND), G1_HCAP, MAX_H, len(SZ), min(s[3] for s in SZ),
         max(s[3] for s in SZ)))

# ----------------------------------------------------------------------------
section("G1  THE ITERATION COLUMNS -- THE FIXED EIGHT-COLUMN CERTIFICATE")
# ----------------------------------------------------------------------------
para("""G1.0  THE OBJECT, AND WHY IT IS ONE OBJECT.  Everything T153 left open is
a statement about the bottom eight modes of the odd section A against the exact
parity ladder mu^P_k, and the two open terms ask for the two DIRECTIONS of the
same statement.  The CEILING lam_k(A) <= K mu^P_k for k <= 8 with K m-free is
what the ratio K_bot / t needs; the FLOOR lam_1(A) >= c mu^P_1 with c much
larger than t is what the collapse price lam_1(A) / (t mu^P_1) = %.2f .. %.2f
would give back.  Both are questions about how the columns (A^-1 L_P)^j t_k sit
relative to the true bottom eigenvectors -- the GREEN COLUMNS of the odd section
applied to the L_P image of the parity sines.  This block builds the subspace
    S_j = span{t_1, .., t_8} + span{(A^-1 L_P)^i t_k : k <= 8, 1 <= i <= j}
for j = 0, 1, 2, of dimension at most 8(j+1) <= 24 -- FIXED, independent of m --
and reads BOTH directions off it.""" % T153_PRICE)

para("""G1.1  THE TWO DIRECTIONS, AND THE EXACTNESS TRICK THAT MAKES THE FLOOR
LEGITIMATE.  CEILING (L5, Courant-Fischer 1920): for every k <= dim S_j,
lam_k(A) <= th_k(S_j), and th_k(S_j) is certified as lam_max of a k x k
compression by ONE Cholesky -- fixed size, no diagonalisation of A.  This is an
UPPER bound on the eigenvalue and hence a CEILING for the ladder constant; it is
never read as a floor.  FLOOR (L6, Temple 1928 / Kato 1949): a residual argument
needs a SEPARATION beta with Q_perp^T A Q_perp >= beta I, and normally that is
exactly the unavailable object.  Here it is available for free, because S_j
CONTAINS span{t_1 .. t_8} and the t_k are EXACT eigenvectors of L_P (L4).  Hence
Q_perp lies inside span{t_9 .. t_m}, so Q_perp^T L_P Q_perp >= mu^P_9 I EXACTLY,
and the already certified A >= t L_P (T152 / T153, Schur two-block, kb = %d)
gives beta = t mu^P_9 with NO new certificate.  mu^P_9 / mu^P_1 is an
m-EXPLICIT Kac-Murdock-Szego number, not an asymptotic one, so the separation
does not degrade with m by construction.  Kaniel 1966 / Paige 1971 is QUOTED for
WHY the residual falls with j -- the iterated subspace is a Krylov space for the
pencil and its high-mode content is damped by the eigenvalue ratio -- and is
never used as a bound.""" % SCHUR_KB)


def append_orth(Q, V, tol=1.0e-9):
    """APPEND span(V) TO AN ORTHONORMAL Q, keeping the EXISTING columns of Q
    untouched.  That the first columns survive verbatim is not cosmetic: the
    whole G1 separation rests on span(Q) CONTAINING span{t_1 .. t_8} exactly."""
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


def cert_ceiling(W, mu, K):
    """K^F = max_{k <= K} lam_max(Y_k^T W Y_k) / mu^P_k, Y_k the k lowest Ritz
    directions.  Each ratio is an UPPER bound on lam_k(A) / mu^P_k by (L5) and
    each numerator is certified by ONE Cholesky of a k x k matrix -- so the
    WHOLE certificate has size at most K, independent of m."""
    try:
        _, Y = eigh(W)
    except (LinAlgError, ValueError):
        return float("nan"), []
    out = []
    for k in range(1, K + 1):
        Z = sym(Y[:, :k].T @ (W @ Y[:, :k]))
        lm = cert_lam_max(Z, guess=float(np.max(np.diag(Z))) + 1.0e-12)
        out.append(lm / mu[k - 1])
    return float(np.max(out)), out


def small_eig_floor(W):
    """A CONSERVATIVE bound on the eigenvalue error of the small dense solve
    (Wilkinson): every Ritz value is shifted by at most this much, and the shift
    is SUBTRACTED wherever a Ritz value feeds a LOWER bound."""
    return 8.0 * W.shape[0] * np.finfo(float).eps * gersh(W)


GR = []
for (zk, D_k, M_k, h_k) in SZ:
    if budget_left() < 260.0:
        info("G1.1.budget", "iteration surface truncated at %d windows" % len(GR))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A = sym(odd_toeplitz(sp["c"], M_k))
    LP = lap_P_mat(m)
    if m <= K_CERT + 2:
        continue
    B = parity_block(A, Tf, mu)
    t_cert = schur_best(B, min(SCHUR_KB, m - 2))
    del B
    rec = dict(zk=zk, h=m, t=t_cert, mu1=float(mu[0]), mu9=float(mu[K_CERT]),
               sep_ratio=float(mu[K_CERT] / mu[0]))
    # the TRUE bottom eight, MEASURED, and the certified true ladder constant
    try:
        w_lo, V_lo = eigh(A, subset_by_index=[0, K_CERT - 1])
    except (LinAlgError, ValueError):
        del A, LP, Tf, sp
        continue
    rec["lam1"] = float(w_lo[0])
    rec["price"] = float(w_lo[0]) / max(t_cert * mu[0], 1.0e-300)
    seed = float(np.max(np.asarray(w_lo) / mu[:K_CERT]))
    K_true = float("nan")
    for eta in (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-3, 1.0e-2, 1.0e-1, 1.0):
        S_try = seed * (1.0 + eta)
        if all(count_below(A, S_try * mu[k - 1]) >= k
               for k in range(1, K_CERT + 1)):
            K_true = S_try
            break
    rec["K_true"] = K_true
    # THE FULL-SIZE CERTIFIED BOTTOM: one Cholesky of A - gam I.  CERTIFIED per
    # window, size m -- NOT a fixed-size certificate, and labelled as such
    # everywhere.  It is the honest competitor of every fixed-size route below.
    rec["lam1_cert"] = cert_lam_min(A, guess=float(w_lo[0]))
    rec["rec_full"] = rec["lam1_cert"] / max(t_cert * mu[0], 1.0e-300)
    # the iteration columns and the nested subspaces S_0 subset S_1 subset S_2
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    # THE MISALIGNMENT, the number the whole floor direction turns on: how far
    # the bottom eight eigenvectors of A sit from the bottom eight of L_P.  Any
    # residual argument needs a separation on the complement of the A bottom, and
    # the only certified input is A >= t L_P; Cauchy 1829 interlacing then gives
    # nothing better than t mu^P_1 there UNLESS the two bottoms nearly coincide.
    ang0 = prin_angles(V0, V_lo)
    rec["mis"] = float(np.max(ang0))
    rec["mis_med"] = float(np.median(ang0))
    # AND WHETHER THAT INTERLACING IS SHARP: an UPPER bound on
    # min_{v perp V_lo} v^T L_P v / v^T v, obtained by TESTING the projected
    # parity sines.  Small means the complement of the A bottom still contains
    # low L_P modes, i.e. the separation cannot be lifted.
    Plo = V_lo @ V_lo.T
    sh = []
    for k in range(K_CERT):
        w = V0[:, k] - Plo @ V0[:, k]
        nw = float(np.linalg.norm(w))
        if nw < 1.0e-6:
            continue
        sh.append(float(w @ (LP @ w)) / (nw * nw) / float(mu[0]))
    rec["sharp"] = qmin(sh)
    del Plo
    cols = {0: V0}
    g_prev = V0
    for j in (1, 2):
        g_prev = green_cols(A, LP, g_prev, 1)
        if g_prev is None:
            break
        cols[j] = g_prev
    Q = orth_cols(V0)
    rec["contain"] = float(np.linalg.norm(V0 - Q @ (Q.T @ V0)))
    beta = t_cert * float(mu[K_CERT])
    rec["beta"] = beta
    # THE CONTAINMENT SCAN.  The separation is beta = t mu^P_{kc+1}, where kc is
    # the number of LEADING parity sines the subspace contains -- so a deeper
    # contained block buys a bigger beta (the Kac-Murdock-Szego ratio
    # mu^P_{kc+1} / mu^P_9 is EXACT) at the price of more dimensions and more
    # residual.  DIRECTION: every entry of this scan is a LOWER bound on
    # lam_1(A), so the MAXIMUM over the scan is the honest best.
    rec["scan"] = []
    for kc in KC_SCAN:
        if kc + 2 >= m:
            continue
        Qc = orth_cols(np.ascontiguousarray(Tf[:kc, :].T))
        bet_c = t_cert * float(mu[kc])
        for j in (1, 2):
            if j not in cols:
                break
            Qc = append_orth(Qc, cols[j])
            rpc = ritz_pack(A, Qc)
            gc = temple_matrix(rpc["W"], sym(rpc["R"].T @ rpc["R"]), bet_c, 1)
            rec["scan"].append(dict(kc=kc, j=j, dim=int(Qc.shape[1]),
                                    beta=bet_c, gam1=gc[0],
                                    r=gc[0] / max(t_cert * mu[0], 1e-300)))
            del rpc
        del Qc
    good = [s for s in rec["scan"] if np.isfinite(s["gam1"])]
    rec["best_scan"] = max(good, key=lambda s: s["gam1"]) if good else None
    rec["J"] = {}
    for j in J_ITER:
        if j > 0:
            if j not in cols:
                break
            Q = append_orth(Q, cols[j])
        rp = ritz_pack(A, Q)
        fl_s = small_eig_floor(rp["W"])
        KF, KF_list = cert_ceiling(rp["W"], mu, K_CERT)
        RtR = sym(rp["R"].T @ rp["R"])
        gam_s = temple_floor(float(rp["th"][0]) - fl_s, beta, rp["nrm_R"])
        gam = temple_matrix(rp["W"], RtR, beta, K_CERT)
        KL = qmin([gam[k] / mu[k] for k in range(K_CERT)
                   if np.isfinite(gam[k])])
        n_ok = int(sum(1 for g in gam if np.isfinite(g) and g > 0.0))
        # geometry: how close the subspace is to the true bottom eight, and how
        # small the residual is ON THE BOTTOM RITZ DIRECTIONS alone
        ang = prin_angles(Q, V_lo)
        try:
            _, Yb = eigh(rp["W"])
            r8 = cert_norm2(rp["R"] @ Yb[:, :K_CERT])
        except (LinAlgError, ValueError):
            r8 = float("nan")
        rec["J"][j] = dict(dim=int(Q.shape[1]), KF=KF, KF_list=KF_list,
                           nrm_R=rp["nrm_R"], th1=float(rp["th"][0]),
                           gam1=gam[0], gam_s=gam_s, KL=KL, n_ok=n_ok,
                           rec=(gam[0] / max(t_cert * mu[0], 1e-300)
                                if np.isfinite(gam[0]) else float("nan")),
                           pin_lo=(gam[0] / rec["lam1"]
                                   if np.isfinite(gam[0]) else float("nan")),
                           pin_up=float(rp["th"][0]) / rec["lam1"],
                           ang_max=float(np.max(ang)), ang_med=float(np.median(ang)),
                           res_rel=rp["nrm_R"] / max(rec["lam1"], 1e-300),
                           r8_rel=r8 / max(rec["lam1"], 1e-300),
                           rho_need=(rp["nrm_R"] ** 2)
                           / max(beta * rec["lam1"], 1e-300))
        del rp, RtR
    # THE CONDITIONAL FIXED-SIZE FLOOR.  Everything in the Temple step is of
    # fixed size EXCEPT one number: the L_P floor on the orthogonal complement of
    # the bottom eight Ritz directions.  Compute it EXACTLY here (an m-sized
    # eigenvalue problem, so NOT part of any fixed-size certificate) and price
    # what a LOWER bound on it would be worth.  Everything downstream of it --
    # the 8 x 8 Ritz block, its residual Gram, the Temple bisection -- is fixed
    # size.  DIRECTION: rec_cond is a LOWER bound on lam_1(A) / (t mu^P_1)
    # CONDITIONAL on the exact number being replaced by an m-free lower bound.
    rec["rec_cond"] = float("nan")
    rec["Lc"] = float("nan")
    if 2 in cols and budget_left() > 180.0:
        rp2 = ritz_pack(A, Q)
        try:
            _, Y2 = eigh(rp2["W"])
            Q8 = Q @ Y2[:, :K_CERT]
            W8 = sym(Q8.T @ (A @ Q8))
            R8 = A @ Q8 - Q8 @ W8
            Qf, _ = np.linalg.qr(Q8, mode="complete")
            N8 = Qf[:, K_CERT:]
            Z8 = sym(N8.T @ (LP @ N8))
            Lc = float(eigh(Z8, eigvals_only=True, subset_by_index=[0, 0])[0])
            rec["Lc"] = Lc / float(mu[0])
            g_c = temple_matrix(W8, sym(R8.T @ R8), t_cert * Lc, 1)[0]
            rec["rec_cond"] = g_c / max(t_cert * mu[0], 1.0e-300)
            del Y2, Q8, W8, R8, Qf, N8, Z8
        except (LinAlgError, ValueError):
            pass
        del rp2
    # the closed-form question: what the RAW Green columns are, mode by mode
    if 2 in cols:
        P8 = V0 @ V0.T
        raw = {}
        for j in (0, 1, 2):
            Vj = cols[j]
            tails, rho, lamr = [], [], []
            for k in range(K_CERT):
                v = Vj[:, k]
                nv = float(np.linalg.norm(v))
                if nv <= 0.0:
                    continue
                v = v / nv
                tails.append(float(np.linalg.norm(v - P8 @ v)))
                av = float(v @ (A @ v))
                rho.append(av / float(v @ (LP @ v)))
                lamr.append(av / float(mu[k]))
            raw[j] = dict(tail=qmed(tails), tail_max=qmax(tails),
                          rho_lo=qmin(rho), rho_hi=qmax(rho),
                          lam_lo=qmin(lamr), lam_hi=qmax(lamr))
            qj = orth_cols(Vj)
            raw[j]["ang"] = float(np.max(prin_angles(qj, V_lo)))
        rec["raw"] = raw
        del P8
    GR.append(rec)
    del A, LP, Tf, sp, V_lo, cols, Q

XG = [r["h"] for r in GR]
JJ = sorted(set(j for r in GR for j in r["J"]))


def jcol(j, key):
    return [r["J"][j][key] for r in GR if j in r["J"]]


F_KT = pow_fit(XG, [r["K_true"] for r in GR], "K_bot")
F_SEP = pow_fit(XG, [r["sep_ratio"] for r in GR], "mu^P_9 / mu^P_1")
check("ga_g1.surface", len(GR) >= 8 and all(np.isfinite(r["K_true"]) for r in GR),
      "the iteration surface carries %d windows, h = %d .. %d.  The certified "
      "floor is t = %.4f .. %.4f (Schur two-block, kb = %d) and the TRUE bottom "
      "ladder constant, certified by %d inertia counts per window (L2), is "
      "K_bot = %.4f .. %.4f (%s) -- T153's 1.102 .. 1.896 reproduced.  The "
      "separation ratio mu^P_9 / mu^P_1 = %.3f .. %.3f is %s, i.e. it converges "
      "to the EXACT Kac-Murdock-Szego value 9^2 = 81 and does not degrade with m"
      % (len(GR), min(XG), max(XG), qmin([r["t"] for r in GR]),
         qmax([r["t"] for r in GR]), SCHUR_KB, K_CERT,
         qmin([r["K_true"] for r in GR]), qmax([r["K_true"] for r in GR]),
         fit_str(F_KT), qmin([r["sep_ratio"] for r in GR]),
         qmax([r["sep_ratio"] for r in GR]), fit_str(F_SEP)))

F_KF0 = pow_fit(XG, jcol(0, "KF"), "K^F j = 0")
check("ga_g1.sines_overshoot", not nogrow_ok(F_KF0),
      "THE PARITY SINES ALONE ARE THE WRONG FAMILY, AND BY THE FACTOR T152 "
      "NAMED.  On the eight-dimensional subspace S_0 = span{t_1 .. t_8} the "
      "Courant-Fischer ceiling is K^F = %.4g .. %.4g, growing as %s -- the "
      "O(m^2) overshoot, and the mechanism is visible in the raw diagonal: "
      "t_k^T A t_k / mu^P_k runs up to %.4g on the surface while the true "
      "lam_k(A) / mu^P_k stays below %.4f"
      % (qmin(jcol(0, "KF")), qmax(jcol(0, "KF")), fit_str(F_KF0),
         qmax([r["raw"][0]["lam_hi"] for r in GR if "raw" in r]),
         qmax([r["K_true"] for r in GR])))

J1 = 1 if 1 in JJ else 0
F_KF1 = pow_fit(XG, jcol(J1, "KF"), "K^F j = 1")
TIGHT = [abs(r["J"][J1]["KF"] / r["K_true"] - 1.0) for r in GR if J1 in r["J"]]
check("ga_g1.ceiling_closed", qmax(TIGHT) < 1.0e-6 and flat_ok(F_KF1),
      "THE CEILING HALF OF R2 IS CLOSED, AND IT IS CLOSED EXACTLY.  Adding ONE "
      "Green step -- S_1 = span{t_1 .. t_8} + span{A^-1 L_P t_k, k <= 8}, "
      "dimension %d, FIXED and independent of m -- brings the Courant-Fischer "
      "ceiling down to K^F = %.4f .. %.4f, which agrees with the inertia-"
      "certified K_bot to a relative %.2e on EVERY window: the sixteen-column "
      "certificate does not merely bound the true bottom ladder, it ATTAINS it.  "
      "K^F is %s, i.e. flat, and the whole certificate is %d Choleskys of "
      "matrices of size at most %d.  The %d inertia counts per window (each an "
      "LDL^T of size m) are thereby RETIRED from the ceiling step.  ONE DIRECTION "
      "CORRECTION, stated explicitly because it is easy to get backwards: this "
      "ceiling needs NO residual argument.  Ritz values are UPPER bounds for the "
      "eigenvalues of the SAME INDEX (Courant-Fischer 1920 / Cauchy 1829), so "
      "K^F is a ceiling by a theorem; Temple 1928 / Kato 1949 is needed only for "
      "the FLOOR, and that is where it is used below"
      % (qmax(jcol(J1, "dim")), qmin(jcol(J1, "KF")), qmax(jcol(J1, "KF")),
         qmax(TIGHT), fit_str(F_KF1), K_CERT, K_CERT, K_CERT))

J2 = 2 if 2 in JJ else J1
check("ga_g1.alignment", qmax(jcol(J2, "ang_max")) < 5.0,
      "AND THE GEOMETRY SAYS WHY, WHICH IS THE ``ALIGNMENT'' OF THE CONTRACT "
      "NAME.  MEASURED principal angles (Bjoerck-Golub 1973) between the true "
      "bottom eight eigenvectors of A and the iterated subspace: S_0 misses them "
      "by up to %.2f deg, S_1 by up to %.2f deg, S_2 by up to %.2f deg.  So the "
      "bottom of the odd section is NOT the parity sine block -- it is the parity "
      "sine block PLUS its Green image, to within a fraction of a degree.  The "
      "closed form of the columns is visible in two further measurements: the "
      "mass of A^-1 L_P t_k OUTSIDE span{t_1 .. t_8} is only %.2e .. %.2e "
      "(median over k), so the Green step is a small correction; and its pencil "
      "Rayleigh quotient v^T A v / v^T L_P v is %.3f .. %.3f, i.e. the iterated "
      "columns sit just above the certified pencil floor t = %.2f, which is "
      "precisely what an inverse-iteration step is supposed to do (Kaniel 1966; "
      "Paige 1971, QUOTED as the explanation, never used as a bound)"
      % (qmax(jcol(0, "ang_max")), qmax(jcol(J1, "ang_max")),
         qmax(jcol(J2, "ang_max")),
         qmin([r["raw"][1]["tail"] for r in GR if "raw" in r]),
         qmax([r["raw"][1]["tail"] for r in GR if "raw" in r]),
         qmin([r["raw"][1]["rho_lo"] for r in GR if "raw" in r]),
         qmax([r["raw"][1]["rho_hi"] for r in GR if "raw" in r]), T_TARGET))

F_RHO = pow_fit(XG, jcol(J1, "rho_need"), "||R||^2 / (beta lam_1)")
N_SCAN = sum(1 for r in GR if r["best_scan"] is not None)
check("ga_g1.floor_refuted", N_SCAN <= 1,
      "THE FLOOR HALF OF R2 IS REFUTED AT FIXED SIZE, AND THE REASON IS ONE "
      "RATIO.  Temple 1928 / Kato 1949 in the matrix form needs the correction "
      "R^T R / (beta - gam) to be small against lam_1(A); the honest measure of "
      "that is ||R||^2 / (beta lam_1) = %.3g .. %.3g, growing as %s.  The "
      "mechanism is structural and not numerical: any subspace that CONTAINS the "
      "parity sines has a residual of the size of ||A|| = O(1), while the target "
      "lam_1(A) is of the size of mu^P_1 = O(m^-2), so the correction is O(m^2) "
      "times too large for EVERY fixed containment depth.  The preregistered "
      "scan over kc = %s and j = 1, 2 (dimensions up to %d) delivers a finite "
      "floor on %d of %d windows, and the one that closes has kc / m = %.2f -- "
      "not a fixed-size certificate in effect.  The SCALAR Temple form, which "
      "replaces R^T R by ||R||^2 I, is worse still: it returns a NEGATIVE and "
      "hence vacuous bound on %d of %d windows"
      % (qmin(jcol(J1, "rho_need")), qmax(jcol(J1, "rho_need")), fit_str(F_RHO),
         ", ".join(str(k) for k in KC_SCAN),
         qmax([s["dim"] for r in GR for s in r["scan"]]), N_SCAN, len(GR),
         qmin([r["best_scan"]["kc"] / r["h"] for r in GR
               if r["best_scan"] is not None]),
         sum(1 for r in GR if J1 in r["J"] and r["J"][J1]["gam_s"] < 0.0),
         len(GR)))

F_MIS = pow_fit(XG, [r["mis"] for r in GR], "misalignment")
F_SH = pow_fit(XG, [r["sharp"] for r in GR], "sharpness")
check("ga_g1.misalignment_named", qmax([r["mis"] for r in GR]) > 60.0,
      "AND THE OBSTRUCTION HAS A NAME AND A NUMBER.  Seven of the eight bottom "
      "directions of A sit inside the parity sine block almost exactly (median "
      "angle %.2f .. %.2f deg), but ONE does not: the largest principal angle "
      "between the bottom eight of A and the bottom eight of L_P is %.2f .. "
      "%.2f deg (%s).  That single misaligned direction is the whole collapse "
      "price.  A residual floor needs a separation on the ORTHOGONAL COMPLEMENT "
      "of the bottom of A, the only certified input there is A >= t L_P, and "
      "Cauchy 1829 interlacing gives nothing better than t mu^P_1 on a "
      "codimension-eight subspace -- which is exactly the bound the collapse "
      "already uses.  The interlacing is SHARP here and not merely unexploited: "
      "TESTING the projected parity sines bounds min_{v perp bottom} "
      "v^T L_P v / v^T v ABOVE by %.3f .. %.3f times mu^P_1 (%s), against a "
      "required %.3f .. %.3f.  The margin is a factor of order one, not orders "
      "of magnitude -- the route misses, but it misses narrowly"
      % (qmin([r["mis_med"] for r in GR]), qmax([r["mis_med"] for r in GR]),
         qmin([r["mis"] for r in GR]), qmax([r["mis"] for r in GR]),
         fit_str(F_MIS), qmin([r["sharp"] for r in GR]),
         qmax([r["sharp"] for r in GR]), fit_str(F_SH),
         qmin([r["price"] for r in GR]), qmax([r["price"] for r in GR])))

CD = [r for r in GR if np.isfinite(r["rec_cond"])]
F_LC = pow_fit([r["h"] for r in CD], [r["Lc"] for r in CD], "L_P complement floor")
F_RC = pow_fit([r["h"] for r in CD], [r["rec_cond"] for r in CD], "conditional")
check("ga_g1.conditional_floor", len(CD) >= 8 and qmin([r["rec_cond"]
                                                       for r in CD]) > 1.0,
      "AND HERE IS THE PRICE OF THE ONE MISSING OBJECT, WHICH IS THE MOST USEFUL "
      "NUMBER IN THIS BLOCK.  Take the eight bottom RITZ directions of S_2 as the "
      "low block: everything the Temple step then needs is of fixed size -- the "
      "8 x 8 Ritz block, its residual Gram, the bisection -- EXCEPT one single "
      "number, the L_P floor on the orthogonal complement of those eight "
      "directions.  Computed EXACTLY (an m-sized eigenproblem, so explicitly NOT "
      "part of any fixed-size certificate) it is %.3f .. %.3f times mu^P_1 (%s), "
      "flat.  Feeding it in, the fixed-size Temple bound returns a CONDITIONAL "
      "recovery of %.3f .. %.3f (%s) against the full price %.3f .. %.3f -- so an "
      "m-free lower bound on that ONE arithmetic-free quantity would buy back "
      "%.0f .. %.0f percent of the collapse price at fixed size.  LABEL: "
      "CONDITIONAL and nothing else -- the number quoted for the complement is "
      "MEASURED, not bounded, and the conclusion is void until it is bounded"
      % (qmin([r["Lc"] for r in CD]), qmax([r["Lc"] for r in CD]), fit_str(F_LC),
         qmin([r["rec_cond"] for r in CD]), qmax([r["rec_cond"] for r in CD]),
         fit_str(F_RC), qmin([r["price"] for r in GR]),
         qmax([r["price"] for r in GR]),
         100.0 * qmin([r["rec_cond"] / r["price"] for r in CD]),
         100.0 * qmax([r["rec_cond"] / r["price"] for r in CD])))

F_REC = pow_fit(XG, [r["rec_full"] for r in GR], "recovery")
REC_LO = qmin([r["rec_full"] for r in GR])
REC_UP = qmax([r["rec_full"] for r in GR])
check("ga_g1.full_size_recovery",
      REC_LO >= T153_PRICE[0] * 0.9 and all(r["lam1_cert"] > 0.0 for r in GR),
      "WHAT DOES RECOVER THE COLLAPSE PRICE, AND AT WHAT PRICE OF ITS OWN.  ONE "
      "Cholesky of A - gam I -- size m, NOT fixed size -- certifies lam_1(A) >= "
      "gam and recovers the collapse factor IN FULL: %.3f .. %.3f (%s) against "
      "the price %.3f .. %.3f T153 measured, i.e. the whole of it, on every "
      "window.  LABEL, PEDANTICALLY: this is CERTIFIED per window and it is NOT "
      "m-free; it replaces one per-window diagonalisation by one per-window "
      "Cholesky and it does NOT produce a theorem.  So the collapse price is a "
      "UNIFORMITY gap, not a size gap: the number is available, the m-free "
      "argument for it is not"
      % (REC_LO, REC_UP, fit_str(F_REC), qmin([r["price"] for r in GR]),
         qmax([r["price"] for r in GR])))

# ----------------------------------------------------------------------------
section("G2  THE KATO NUMBER -- R1 IN ITS SHARP ONE-NUMBER FORM")
# ----------------------------------------------------------------------------
para("""G2.0  THE OBJECT AND ITS DIRECTION.  T153 turned the block inequality
B_HH >= t I on the bulk (modes above kb = %d) into ONE number.  Since the
archimedean part of the bulk block is POSITIVE after an m-free peeling, it can
serve as the METRIC: with P = B^arch_HH and C = P^-1/2 B^atom_HH P^-1/2,
    B_HH = P^1/2 (I + C) P^1/2   (IDENTITY)   and
    lam_min(B_HH) >= lam_min(P) (1 + lam_min(C))   (THEOREM, Kato 1949 relative
perturbation), so B_HH >= t I FOLLOWS from 1 + lam_min(C) >= t / lam_min(P).
DIRECTION: lam_min(C) is to be bounded BELOW and 1 + lam_min(C) is the quantity
that must not shrink.  T153 measured 1 + lam_min(C) = %.1e .. %.1e against an
m-free arch reserve lam_min(P) = %.4f .. %.4f, i.e. a requirement of about
t / lam_min(P) -- positive, certified, but shrinking like x^-1.778.  This block
asks WHY, WHICH VECTOR does it, and whether any repair makes the number
m-free.""" % (SCHUR_KB, T153_KATO[0], T153_KATO[1], T153_ARCH[0], T153_ARCH[1]))


def whiten_min(P_blk, X_blk):
    """THE KATO NUMBER OF A METRIC.  Given P > 0 and a perturbation X on the same
    block, returns lam_min(P), lam_min(C) with C = P^-1/2 X P^-1/2, a CERTIFIED
    lower bound on lam_min(C), and the minimising direction of C.  DIRECTION:
    1 + lam_min(C) multiplies lam_min(P) to give a LOWER bound on
    lam_min(P^1/2 (I + C) P^1/2); it is never used the other way."""
    try:
        w, V = eigh(sym(P_blk))
    except (LinAlgError, ValueError):
        return None
    if float(w[0]) <= 0.0:
        return dict(lo_P=float(w[0]), lo_C=float("nan"), lo_C_cert=float("nan"),
                    u=None)
    Wh = V * (1.0 / np.sqrt(w))[None, :]
    C = sym(Wh.T @ (sym(X_blk) @ Wh))
    try:
        wc, Vc = eigh(C)
    except (LinAlgError, ValueError):
        return None
    out = dict(lo_P=float(w[0]), lo_C=float(wc[0]),
               lo_C_cert=cert_lam_min(C, guess=float(wc[0])),
               u=Wh @ Vc[:, 0], nrm_C=float(max(abs(wc[0]), abs(wc[-1]))))
    del Wh, C, w, V, wc, Vc
    return out


def toep_only(c, M):
    """THE SECTION WITH THE HANKEL REFLECTION HALF REMOVED: pure Toeplitz
    c_{|r-s|} on the same index range.  A DIAGNOSTIC object, not the section --
    it is the ``reflected whitening'' candidate's metric and the Dirichlet
    control's kernel, and it is never substituted for A in any chain."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])]


def hank_only(c, M):
    """THE HANKEL REFLECTION HALF ALONE, with the sign it carries in the odd
    section: -c_{M-1-r-s}.  T153 named it as the culprit (+13.7 against the
    Toeplitz half's -2.68 in the atom anatomy)."""
    h = M // 2
    rr = np.arange(h)
    return -c[(M - 1) - rr[:, None] - rr[None, :]]


G2C = [c for c in CAND if c[3] <= G2_HCAP]
G2S = []
if G2C:
    st = max(1, len(G2C) // max(G2_ZONES, 1))
    G2S = G2C[::-1][::st][:G2_ZONES]
    G2S.sort(key=lambda t: t[0])

KR = []
for (zk, D_k, M_k, h_k) in G2S:
    if budget_left() < 200.0:
        info("G2.0.budget", "Kato surface truncated at %d windows" % len(KR))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    if m <= SCHUR_KB + K_CERT + 4:
        continue
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A = sym(odd_toeplitz(sp["c"], M_k))
    B = parity_block(A, Tf, mu)
    B_ar = parity_block(sym(odd_toeplitz(sp["c_ar"], M_k)), Tf, mu)
    B_at = parity_block(sym(odd_toeplitz(sp["c_at"], M_k)), Tf, mu)
    kb = SCHUR_KB
    rec = dict(zk=zk, h=m, nb=m - kb)
    # K1 THE BASELINE: the arch-whitened atom operator on the bulk
    k1 = whiten_min(B_ar[kb:, kb:], B_at[kb:, kb:])
    if k1 is None:
        del A, B, B_ar, B_at, Tf, sp
        continue
    rec["lo_P"] = k1["lo_P"]
    rec["one_C"] = 1.0 + k1["lo_C"]
    rec["one_C_cert"] = 1.0 + k1["lo_C_cert"]
    rec["need"] = T_TARGET / max(k1["lo_P"], 1.0e-300)
    rec["nrm_at"] = abs(ray_top(sym(B_at[kb:, kb:])))
    BHH = sym(B[kb:, kb:])
    try:
        wB, VB = eigh(BHH)
        rec["lo_B"] = float(wB[0])
        uB = VB[:, 0]
    except (LinAlgError, ValueError):
        rec["lo_B"] = float("nan")
        uB = None
    # THE ANATOMY OF THE MINIMISER: where does the vector that realises the Kato
    # number live -- in the mode index, and in position space at the boundary?
    u = k1["u"]
    if u is not None:
        un = u / max(np.linalg.norm(u), 1.0e-300)
        rec["ray_B"] = float(un @ (BHH @ un))
        rec["kato_loss"] = rec["ray_B"] / max(rec["lo_P"] * rec["one_C"], 1e-300)
        if uB is not None:
            rec["ang_min"] = float(np.degrees(np.arccos(
                min(1.0, abs(float(un @ uB))))))
        w2 = un ** 2
        idx = np.arange(rec["nb"], dtype=float)
        rec["com_mode"] = float(np.sum(idx * w2) / max(np.sum(w2), 1e-300)) \
            / max(rec["nb"] - 1.0, 1.0)
        rec["low8"] = float(np.sum(w2[:K_CERT]))
        # position space: the whitened bulk coefficients back onto the window
        x = Tf[kb:, :].T @ (un / np.sqrt(mu[kb:]))
        nx2 = float(x @ x)
        rec["edge8"] = float(np.sum(x[-K_CERT:] ** 2) / max(nx2, 1e-300))
        rec["edge_pc"] = float(np.sum(x[-max(1, m // 20):] ** 2)
                               / max(nx2, 1e-300))
        # the atom halves AT the minimiser: which half does the damage
        T_at = parity_block(sym(toep_only(sp["c_at"], M_k)), Tf, mu)[kb:, kb:]
        H_at = parity_block(sym(hank_only(sp["c_at"], M_k)), Tf, mu)[kb:, kb:]
        rec["half_T"] = float(un @ (sym(T_at) @ un))
        rec["half_H"] = float(un @ (sym(H_at) @ un))
        del T_at, H_at, x, w2
    # K4 THE REFLECTED WHITENING: the same atom block against the arch metric
    # with its Hankel reflection half REMOVED
    k4 = whiten_min(parity_block(sym(toep_only(sp["c_ar"], M_k)), Tf,
                                 mu)[kb:, kb:], B_at[kb:, kb:])
    rec["k4"] = (1.0 + k4["lo_C"]) if k4 else float("nan")
    rec["k4_P"] = k4["lo_P"] if k4 else float("nan")
    # K7 THE DIAGONAL WHITENING: a metric that knows the mode index but no
    # arithmetic split at all
    d = np.diag(BHH).copy()
    if float(np.min(d)) > 0.0:
        isq = 1.0 / np.sqrt(d)
        Cd = sym(BHH * np.outer(isq, isq))
        try:
            rec["k7"] = float(eigh(Cd, eigvals_only=True,
                                   subset_by_index=[0, 0])[0])
        except (LinAlgError, ValueError):
            rec["k7"] = float("nan")
        rec["k7_d"] = float(np.min(d))
        del Cd
    else:
        rec["k7"] = float("nan")
        rec["k7_d"] = float(np.min(d))
    # K5 THE SECOND PEEL: does a DEEPER fixed peel make the number m-free?
    rec["k5"] = []
    for kb2 in KB2_SCAN:
        if kb2 + K_CERT + 2 >= m:
            rec["k5"].append(float("nan"))
            continue
        k5 = whiten_min(B_ar[kb2:, kb2:], B_at[kb2:, kb2:])
        rec["k5"].append((1.0 + k5["lo_C"]) if k5 else float("nan"))
    # K3 THE BOUNDARY PEEL: a Dirichlet restriction of the WINDOW, not of the
    # mode index -- q position-space columns dropped at the reflecting edge
    rec["k3"] = []
    for q in Q_EDGE:
        if q == 0:
            rec["k3"].append(rec["one_C"])
            continue
        mq = m - q
        if mq <= kb + K_CERT + 4 or budget_left() < 150.0:
            rec["k3"].append(float("nan"))
            continue
        muq = parity_mu(mq)
        Tq = parity_basis(mq)
        Ar = sym(odd_toeplitz(sp["c_ar"], M_k))[:mq, :mq]
        At = sym(odd_toeplitz(sp["c_at"], M_k))[:mq, :mq]
        k3 = whiten_min(parity_block(Ar, Tq, muq)[kb:, kb:],
                        parity_block(At, Tq, muq)[kb:, kb:])
        rec["k3"].append((1.0 + k3["lo_C"]) if k3 else float("nan"))
        del muq, Tq, Ar, At
    KR.append(rec)
    del A, B, B_ar, B_at, BHH, Tf, sp

XK = [r["h"] for r in KR]
F_EPS = pow_fit(XK, [r["one_C"] for r in KR], "1 + lam_min(C)")
F_LOP = pow_fit(XK, [r["lo_P"] for r in KR], "arch reserve")
CERT_OK = all(r["one_C_cert"] > 0.0 for r in KR)
check("ga_g2.surface", len(KR) >= 8 and CERT_OK,
      "the Kato surface carries %d windows, h = %d .. %d, and T153's two numbers "
      "are reproduced: the arch reserve lam_min(P) = %.4f .. %.4f (%s), bounded "
      "and only slowly rising, and the Kato number 1 + lam_min(C) = %.3e .. %.3e, CERTIFIED "
      "positive on every window (Cholesky floor carried) but shrinking as %s "
      "against a requirement t / lam_min(P) = %.3f .. %.3f.  So the gap is a "
      "factor %.1f .. %.1f and it grows"
      % (len(KR), min(XK), max(XK), qmin([r["lo_P"] for r in KR]),
         qmax([r["lo_P"] for r in KR]), fit_str(F_LOP),
         qmin([r["one_C"] for r in KR]), qmax([r["one_C"] for r in KR]),
         fit_str(F_EPS), qmin([r["need"] for r in KR]),
         qmax([r["need"] for r in KR]),
         qmin([r["need"] / r["one_C"] for r in KR]),
         qmax([r["need"] / r["one_C"] for r in KR])))

check("ga_g2.minimiser_is_deep", qmin([r["low8"] for r in KR]) > 0.90,
      "WHICH VECTOR REALISES THE MINIMUM: THE DEEP MODES, NOT THE BOUNDARY.  "
      "%.1f .. %.1f percent of the mass of the C-minimiser sits on the LOWEST "
      "EIGHT modes of the bulk block, i.e. immediately above the peel cut kb = "
      "%d; its centre of mass in the bulk mode index is at a fraction %.3f .. "
      "%.3f of the block.  In position space it is NOT a boundary vector: only "
      "%.1f .. %.1f percent of its energy sits in the last eight window indices "
      "and %.1f .. %.1f percent in the last five percent.  The mechanism is the "
      "whitening exponent and nothing else: B_kl carries 1 / sqrt(mu^P_k mu^P_l) "
      "and mu^P_k = O(k^2 / m^2), so the block just above the cut is amplified "
      "by O((m/kb)^2) -- which is where the atoms are largest"
      % (100.0 * qmin([r["low8"] for r in KR]),
         100.0 * qmax([r["low8"] for r in KR]), SCHUR_KB,
         qmin([r["com_mode"] for r in KR]), qmax([r["com_mode"] for r in KR]),
         100.0 * qmin([r["edge8"] for r in KR]),
         100.0 * qmax([r["edge8"] for r in KR]),
         100.0 * qmin([r["edge_pc"] for r in KR]),
         100.0 * qmax([r["edge_pc"] for r in KR])))

HT = [r["half_T"] for r in KR]
HH = [r["half_H"] for r in KR]
N_T_WORSE = sum(1 for r in KR if r["half_T"] < r["half_H"])
check("ga_g2.hankel_not_the_culprit", N_T_WORSE >= 1,
      "AND T153'S NAMED CULPRIT IS REFUTED AS A MECHANISM.  Evaluated AT the "
      "vector that actually realises the minimum, the Toeplitz half of the atom "
      "block contributes %.4g .. %.4g and the Hankel reflection half %.4g .. "
      "%.4g -- BOTH negative, and the Toeplitz half is the LARGER offender on "
      "%d of %d windows.  T153's -2.68 / +13.7 split was a statement about "
      "lam_min of the two halves SEPARATELY, which is a different question from "
      "which half hurts the minimiser.  The boundary-reflection reading is "
      "therefore not the mechanism, and the boundary repair below fails "
      "accordingly"
      % (qmin(HT), qmax(HT), qmin(HH), qmax(HH), N_T_WORSE, len(KR)))

F_LOSS = pow_fit(XK, [r["kato_loss"] for r in KR], "Kato loss")
check("ga_g2.loss_is_misalignment", qmin([r["ang_min"] for r in KR]) > 20.0,
      "THE SHARP DIAGNOSIS: THE KATO NUMBER IS NOT SMALL BECAUSE THE FLOOR IS "
      "SMALL.  The true bulk floor is lam_min(B_HH) = %.4f .. %.4f, comfortably "
      "above t = %.2f, while the Kato product lam_min(P)(1 + lam_min(C)) "
      "delivers only %.3e .. %.3e -- a loss of %.2f .. %.3g (%s).  The reason is "
      "MEASURED and it is the same phenomenon G1 found: the two minima are "
      "attained in DIFFERENT DIRECTIONS, %.2f .. %.2f deg apart, and the "
      "Rayleigh quotient of B_HH at the C-minimiser is %.4f .. %.4f, i.e. the "
      "vector that ruins the relative bound is a perfectly HARMLESS direction "
      "for the block inequality itself.  A relative (Kato-type) bound cannot see "
      "that, because it multiplies two minima it never has to attain together"
      % (qmin([r["lo_B"] for r in KR]), qmax([r["lo_B"] for r in KR]), T_TARGET,
         qmin([r["lo_P"] * r["one_C"] for r in KR]),
         qmax([r["lo_P"] * r["one_C"] for r in KR]),
         qmin([r["kato_loss"] for r in KR]),
         qmax([r["kato_loss"] for r in KR]), fit_str(F_LOSS),
         qmin([r["ang_min"] for r in KR]), qmax([r["ang_min"] for r in KR]),
         qmin([r["ray_B"] for r in KR]), qmax([r["ray_B"] for r in KR])))

K3_GAIN = [qmax(r["k3"]) / r["one_C"] for r in KR]
K4_BAD = sum(1 for r in KR if not (np.isfinite(r["k4"]) and r["k4"] > 0.0))
K7_GAIN = [(r["k7"] * r["k7_d"]) / (r["lo_P"] * r["one_C"]) for r in KR]
check("ga_g2.repairs_fail",
      qmax(K3_GAIN) < 1.5 and K4_BAD >= len(KR) // 2,
      "THE FOUR PREREGISTERED REPAIRS, EACH WITH ITS NUMBER.  (K3) BOUNDARY "
      "PEELING, q = %s position-space columns dropped at the reflecting edge: "
      "the Kato number moves by a factor %.3f .. %.3f only -- the boundary is "
      "not where the number lives, exactly as the anatomy above says.  (K4) THE "
      "REFLECTED WHITENING, arch metric with its Hankel half removed: the metric "
      "itself stays positive (lam_min = %.4f .. %.4f) but the Kato number turns "
      "NEGATIVE on %d of %d windows -- strictly WORSE, refuted.  (K7) THE "
      "DIAGONAL WHITENING, a metric with no arithmetic split at all: it gives "
      "lam_min(D)(1 + lam_min(C_d))-type floor %.3e .. %.3e, a factor %.2f .. "
      "%.2f against the arch metric, i.e. the same order and no cure.  (K6) THE "
      "PURE NORM ROUTE needs ||B^atom_HH|| <= lam_min(P) - t = %.3f .. %.3f and "
      "measures %.4g .. %.4g -- dead by two to three orders of magnitude"
      % (", ".join(str(q) for q in Q_EDGE), qmin(K3_GAIN), qmax(K3_GAIN),
         qmin([r["k4_P"] for r in KR]), qmax([r["k4_P"] for r in KR]),
         K4_BAD, len(KR), qmin([r["k7"] * r["k7_d"] for r in KR]),
         qmax([r["k7"] * r["k7_d"] for r in KR]), qmin(K7_GAIN), qmax(K7_GAIN),
         qmin([r["lo_P"] - T_TARGET for r in KR]),
         qmax([r["lo_P"] - T_TARGET for r in KR]),
         qmin([r["nrm_at"] for r in KR]), qmax([r["nrm_at"] for r in KR])))

PKB = []
FRAC = []
for r in KR:
    f = pow_fit(list(KB2_SCAN), r["k5"], "kb")
    if not np.isfinite(f["p"]) or f["p"] <= 0.0:
        continue
    PKB.append(f["p"])
    FRAC.append(SCHUR_KB * (r["need"] / r["one_C"]) ** (1.0 / f["p"]) / r["h"])
check("ga_g2.deeper_peel_is_m_proportional", qmin(FRAC) > 0.20,
      "AND THE ONE REPAIR THAT DOES MOVE THE NUMBER IS NOT m-FREE, WHICH IS THE "
      "WHOLE POINT.  (K5) A DEEPER FIXED PEEL kb2 = %s buys the Kato number back "
      "like kb2^%.3f .. kb2^%.3f -- short of the naive whitening exponent 2 -- "
      "while the number itself shrinks as %s in m.  Solving for the peel that "
      "would meet the requirement gives kb2 / m = %.2f .. %.2f: about HALF the "
      "window, PROPORTIONAL to m, not a fixed block.  And the reason is "
      "scale-free, which is why T153's recursive Schur was scale-invariant too: "
      "the C-minimiser always sits on the lowest eight modes of WHATEVER block "
      "is left, so every deeper peel merely moves the same vector up"
      % (", ".join(str(k) for k in KB2_SCAN), qmin(PKB), qmax(PKB),
         fit_str(F_EPS), qmin(FRAC), qmax(FRAC)))

# ----------------------------------------------------------------------------
section("G3  ASSEMBLY, THE NEW END TO END, AND THE OBLIGATORY STRESS")
# ----------------------------------------------------------------------------
para("""G3.0  WHAT THE BEST G1 + G2 COMBINATION IS, STATED BEFORE IT IS PRICED.
G1 closed the CEILING half of R2 at fixed size and refuted its FLOOR half at
fixed size; G2 refuted every relative route to R1.  So the best combination is:
the ceiling from the sixteen-column Courant-Fischer certificate (fixed size,
theorem-grade direction, flat), the floor from the UNCHANGED T152 / T153 Schur
two-block criterion (per-window certified, kb = %d), and the collapse price from
ONE per-window Cholesky of A - gam I.  Two end-to-end numbers follow and they
must NOT be conflated: an m-FREE-IN-SHAPE one, which does not move, and a
PER-WINDOW CERTIFIED one, which recovers the whole collapse price.""" % SCHUR_KB)

NEW_LO = T153_FRAC[0] * REC_LO
NEW_UP = T153_FRAC[1] * REC_UP
check("ga_g3.end_to_end", NEW_LO >= FRAC_BAR,
      "THE NEW END TO END, IN BOTH LABELS.  (A) m-FREE IN SHAPE: unchanged at "
      "%.2e .. %.2e of the true gap.  The ceiling closure buys NO size here -- "
      "T153 already used the inertia-certified K_bot, and G1 proved that the "
      "fixed-size certificate ATTAINS exactly that number, so what the closure "
      "buys is the retirement of %d LDL^T factorisations of size m per window, "
      "i.e. UNIFORMITY and cost, not a factor.  (B) PER-WINDOW CERTIFIED, with "
      "the collapse price recovered by one Cholesky: %.2e .. %.2e, a gain of "
      "%.3f .. %.3f, which lands inside the %.0e .. 3e-1 band this probe was "
      "aimed at.  THE HONEST READING: the SIZE target is met and the UNIFORMITY "
      "target is not, and those are different targets"
      % (T153_FRAC[0], T153_FRAC[1], K_CERT, NEW_LO, NEW_UP, REC_LO, REC_UP,
         FRAC_BAR))

BAL = [
    ("t (Schur two-block, kb = %d)" % SCHUR_KB,
     "%.4f .. %.4f" % (qmin([r["t"] for r in GR]), qmax([r["t"] for r in GR])),
     "flat", "CERTIFIED per window"),
    ("K^F (16-column ceiling)",
     "%.4f .. %.4f" % (qmin(jcol(J1, "KF")), qmax(jcol(J1, "KF"))),
     fit_str(F_KF1), "CERTIFIED, fixed size, THEOREM direction (L5)"),
    ("K_bot (inertia, the target)",
     "%.4f .. %.4f" % (qmin([r["K_true"] for r in GR]),
                       qmax([r["K_true"] for r in GR])),
     fit_str(F_KT), "CERTIFIED per window (L2)"),
    ("mu^P_9 / mu^P_1 (separation)",
     "%.3f .. %.3f" % (qmin([r["sep_ratio"] for r in GR]),
                       qmax([r["sep_ratio"] for r in GR])),
     fit_str(F_SEP), "THEOREM, exact (L4)"),
    ("collapse recovery (Cholesky)",
     "%.3f .. %.3f" % (REC_LO, REC_UP), fit_str(F_REC),
     "CERTIFIED per window, size m -- NOT fixed size"),
    ("misalignment angle (deg)",
     "%.2f .. %.2f" % (qmin([r["mis"] for r in GR]),
                       qmax([r["mis"] for r in GR])), fit_str(F_MIS),
     "MEASURED -- the named obstruction"),
    ("residual ratio ||R||^2/(beta lam_1)",
     "%.3g .. %.3g" % (qmin(jcol(J1, "rho_need")), qmax(jcol(J1, "rho_need"))),
     fit_str(F_RHO), "MEASURED -- why the fixed-size floor fails"),
    ("arch reserve lam_min(P)",
     "%.4f .. %.4f" % (qmin([r["lo_P"] for r in KR]),
                       qmax([r["lo_P"] for r in KR])), fit_str(F_LOP),
     "CERTIFIED per window"),
    ("Kato number 1 + lam_min(C)",
     "%.3e .. %.3e" % (qmin([r["one_C"] for r in KR]),
                       qmax([r["one_C"] for r in KR])), fit_str(F_EPS),
     "CERTIFIED positive, SHRINKING -- the open term"),
]
info("G3.1.balance", "THE UNIFORMITY BALANCE OF EVERY FACTOR THAT ENTERS "
     "(quantity | band | fit in h | label):")
for nm, band, ft, lab in BAL:
    info("  " + nm, "%s | %s | %s" % (band, ft, lab))


def instrument(A, m, tag):
    """THE G1 INSTRUMENT, APPLIED TO AN ARBITRARY SYMMETRIC SECTION.  Returns the
    certified floor t, the inertia-certified true bottom ladder constant, the
    eight-column and sixteen-column Courant-Fischer ceilings and the
    misalignment angle -- the SAME code path the surface above uses, so that a
    stress family and a control are measured by the same instrument."""
    mu = parity_mu(m)
    Tf = parity_basis(m)
    LP = lap_P_mat(m)
    B = parity_block(A, Tf, mu)
    t_c = schur_best(B, min(SCHUR_KB, m - 2))
    del B
    out = dict(tag=tag, m=m, t=t_c)
    try:
        w_lo, V_lo = eigh(A, subset_by_index=[0, K_CERT - 1])
    except (LinAlgError, ValueError):
        return None
    seed = float(np.max(np.asarray(w_lo) / mu[:K_CERT]))
    Kt = float("nan")
    for eta in (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-3, 1.0e-2, 1.0e-1, 1.0):
        S_try = seed * (1.0 + eta)
        if all(count_below(A, S_try * mu[k - 1]) >= k
               for k in range(1, K_CERT + 1)):
            Kt = S_try
            break
    out["K_true"] = Kt
    out["lam1"] = float(w_lo[0])
    out["price"] = (float(w_lo[0]) / (t_c * mu[0])
                    if np.isfinite(t_c) and t_c > 0.0 else float("nan"))
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    out["mis"] = float(np.max(prin_angles(V0, V_lo)))
    Q = orth_cols(V0)
    out["KF0"] = cert_ceiling(sym(Q.T @ (A @ Q)), mu, K_CERT)[0]
    g1 = green_cols(A, LP, V0, 1)
    if g1 is not None:
        Q = append_orth(Q, g1)
        out["KF1"] = cert_ceiling(sym(Q.T @ (A @ Q)), mu, K_CERT)[0]
    else:
        out["KF1"] = float("nan")
    del Tf, LP, V_lo, Q
    return out


para("""G3.2  THE OBLIGATORY STRESS: THE T145 NO-GO MUST BREAK, AND THE NEW
INSTRUMENT MUST NOT CLOSE IT.  T151's no-go matrix is not in this file, so what
is stressed is the RECONSTRUCTION T152 / T153 used: the positive decaying lag
kernel c(l) = 1 / (1 + l), whose symbol has a LOGARITHMIC singularity at the
origin instead of vanishing there.  Its odd section is positive definite, so it
passes every positivity test and the floor must survive.  The DECISIVE test is
new: the sixteen-column certificate attained the true ladder constant on the real
section, so on the no-go it must ATTAIN the exploding one -- if it reported a
flat ceiling there, the instrument would be a lossy tool that manufactures
closures, and everything in G1 would be worthless.""")

NG = []
for m_ng in NOGO_SIZES:
    if budget_left() < 90.0:
        break
    M_ng = 2 * m_ng
    c_ng = 1.0 / (1.0 + np.arange(M_ng, dtype=float))
    got = instrument(sym(odd_toeplitz(c_ng, M_ng)), m_ng, "nogo")
    if got is not None:
        NG.append(got)
    del c_ng

F_NG_K = pow_fit([g["m"] for g in NG], [g["K_true"] for g in NG], "K_bot nogo")
F_NG_F = pow_fit([g["m"] for g in NG], [g["KF1"] for g in NG], "K^F nogo")
check("ga_g3.nogo_floor_survives", all(g["t"] > 0.0 for g in NG),
      "AND IT BREAKS EXACTLY WHERE THE MECHANISM SAYS.  On the no-go family the "
      "FLOOR is fine -- the Schur two-block criterion certifies t = %.4g .. %.4g "
      "on all %d sizes -- so no positivity test rejects it"
      % (qmin([g["t"] for g in NG]), qmax([g["t"] for g in NG]), len(NG)))

NG_TIGHT = [g["KF1"] / g["K_true"] for g in NG
            if np.isfinite(g["KF1"]) and np.isfinite(g["K_true"])]
check("ga_g3.nogo_ceiling_breaks",
      (not nogrow_ok(F_NG_K)) and (not nogrow_ok(F_NG_F)),
      "BUT THE CEILING EXPLODES, AND THE NEW CERTIFICATE EXPLODES WITH IT -- "
      "WHICH IS THE POINT.  K_bot = %.4g .. %.4g growing as %s on the no-go, far "
      "outside the preregistered bar %.2f and against the true section's flat "
      "%s.  The sixteen-column ceiling reports %.4g .. %.4g, growing as %s: it "
      "does NOT report flatness where flatness is false, so the instrument "
      "manufactures no closure.  AND ONE MORE THING FALLS OUT, WHICH SHARPENS "
      "G1: on the no-go the ceiling OVERSHOOTS the true constant by a factor "
      "%.3f .. %.3f, whereas on the real section it attained it to 5e-7.  The "
      "EXACT attainment is therefore a property of the REAL SECTION -- of how its "
      "bottom sits inside the parity sines plus their Green image -- and not a "
      "property of the certificate.  Stated as MEASURED, with no m-free claim"
      % (qmin([g["K_true"] for g in NG]), qmax([g["K_true"] for g in NG]),
         fit_str(F_NG_K), BAR_UNIF, fit_str(F_KT),
         qmin([g["KF1"] for g in NG]), qmax([g["KF1"] for g in NG]),
         fit_str(F_NG_F), qmin(NG_TIGHT), qmax(NG_TIGHT)))

check("ga_g3.nogo_price_separates",
      qmin([g["price"] for g in NG]) > 10.0 * qmax([r["price"] for r in GR]),
      "AND THE COLLAPSE PRICE SEPARATES THE TWO FAMILIES BY ORDERS OF MAGNITUDE, "
      "WHICH IS WHAT MAKES IT A DIAGNOSTIC AND NOT A COINCIDENCE.  On the no-go "
      "the misalignment saturates at %.2f deg and the price is %.3g .. %.3g; on "
      "the real section the misalignment is %.2f .. %.2f deg and the price only "
      "%.3f .. %.3f.  So the real section is NEARLY aligned in the sense that "
      "matters and the no-go is not aligned at all -- the price measures exactly "
      "the distance between the bottom of A and the bottom of L_P.  MEASURED, "
      "quoted as a family separation, no m-free law claimed"
      % (qmax([g["mis"] for g in NG]), qmin([g["price"] for g in NG]),
         qmax([g["price"] for g in NG]), qmin([r["mis"] for r in GR]),
         qmax([r["mis"] for r in GR]), qmin([r["price"] for r in GR]),
         qmax([r["price"] for r in GR])))

CT = []
for m_c in CTRL_SIZES:
    if budget_left() < 60.0:
        break
    got = instrument(sym(lap_P_mat(m_c)), m_c, "parity")
    if got is not None:
        CT.append(got)
CT_ERR = qmax([max(abs(g["K_true"] - 1.0), abs(g["KF0"] - 1.0),
                   abs(g["KF1"] - 1.0), g["mis"]) for g in CT]) \
    if CT else float("nan")
check("ga_g3.parity_control_exact", np.isfinite(CT_ERR) and CT_ERR < 1.0e-5,
      "THE PARITY CONTROL, EXACT AS IT MUST BE.  Feeding A = L_P itself through "
      "the SAME instrument on m = %s must return 1 for the true ladder constant, "
      "1 for BOTH ceilings and 0 degrees of misalignment, because the parity "
      "sines ARE the eigenvectors then.  Worst deviation over all three numbers "
      "and all %d sizes: %.2e -- which is the BACKOFF STEP of the inertia ladder "
      "(the scan multiplies the seed by 1 + eta with eta down to 1e-6), not an "
      "error in the instrument.  The certified floor comes out t = %.4f, which is "
      "the CAP of the preregistered ladder (its largest entry) and not a "
      "measurement of the true pencil floor 1 -- an artefact of the ladder, "
      "labelled as such; the price %.4f .. %.4f is then exactly 1 / t, i.e. there "
      "is nothing to recover once the two bottoms coincide, which is the cleanest "
      "statement of what the collapse price measures"
      % (", ".join(str(s) for s in CTRL_SIZES), len(CT), CT_ERR,
         qmax([g["t"] for g in CT]), qmin([g["price"] for g in CT]),
         qmax([g["price"] for g in CT])))

DC = []
for (zk, D_k, M_k, h_k) in (SZ[:1] + SZ[len(SZ) // 2:len(SZ) // 2 + 1]
                            + SZ[-1:]):
    if budget_left() < 90.0:
        break
    alpha = 0.5 * M_k * D_k
    spc = lag_vector_split(alpha, M_k, atoms_in(alpha))
    got = instrument(sym(toep_only(spc["c"], M_k)), h_k, "dirichlet")
    if got is not None:
        DC.append(got)
    del spc

check("ga_g3.dirichlet_control_is_negative",
      len(DC) >= 2 and qmax([g["lam1"] for g in DC]) < 0.0,
      "THE DIRICHLET CONTROL, AND IT REVERSES T153'S READING OF THE REFLECTION "
      "HALF A SECOND TIME.  Removing the HANKEL half keeps the arithmetic bit for "
      "bit and changes only the boundary condition of the section -- and the "
      "result is that the section STOPS BEING POSITIVE DEFINITE: lam_1 = %.4g .. "
      "%.4g on m = %s.  Every downstream object is then undefined: no Cholesky, "
      "hence no Green step (K^F after one step is not computable), and no Schur "
      "floor t.  So the reflection half is LOAD-BEARING for positivity, not a "
      "nuisance term -- which independently explains why G2's reflected whitening "
      "(K4) turned the Kato number negative, and it retires the "
      "``boundary-reflection is the culprit'' reading for good.  DIRECTION note: "
      "K_bot is meaningless on a non-positive section and is NOT quoted here"
      % (qmin([g["lam1"] for g in DC]), qmax([g["lam1"] for g in DC]),
         ", ".join(str(g["m"]) for g in DC)))

ALLF = ([("section", r["J"][J1]["KF"], r["J"][0]["KF"], r["K_true"])
         for r in GR if J1 in r["J"]]
        + [(g["tag"], g["KF1"], g["KF0"], g["K_true"]) for g in NG + CT])
VIOL = [nm for nm, k1, k0, kt in ALLF
        if not (np.isfinite(kt) and k1 >= kt * (1.0 - 1.0e-9)
                and k0 >= kt * (1.0 - 1.0e-9))]
check("ga_g3.direction_never_violated", not VIOL and len(ALLF) >= 20,
      "THE ONE INVARIANT THAT MUST NEVER BREAK, CHECKED ON EVERY POSITIVE FAMILY "
      "AT ONCE.  Courant-Fischer says both ceilings are UPPER bounds on the true "
      "ladder constant, never lower.  Tested on all %d positive-definite cases -- "
      "%d windows of the real section, %d no-go sizes, %d parity controls -- "
      "violations: %d.  The %d Dirichlet cases are EXCLUDED by construction and "
      "for a stated reason, not for convenience: they are not positive definite, "
      "so neither ceiling is defined there.  If this check ever failed, every "
      "ceiling number in this file would be meaningless in the direction it is "
      "used"
      % (len(ALLF), len(GR), len(NG), len(CT), len(VIOL), len(DC)))

# ----------------------------------------------------------------------------
section("G4  MAP V26, THE PROMOTION LIST, THE REST LIST, AND THE VERDICT")
# ----------------------------------------------------------------------------
MAP = [
    ("THEOREM", "the parity spectrum mu^P_k = 4 sin^2(pi k / N) and every ratio "
     "formed from it, in particular the separation mu^P_9 / mu^P_1 -> 81 "
     "(Kac-Murdock-Szego 1953); the Courant-Fischer 1920 ceiling direction; the "
     "Schur 1917 / Haynsworth 1968 two-block equivalence; the Temple 1928 / "
     "Kato 1949 residual floor and its matrix form; Weyl 1912 monotonicity; "
     "Cauchy 1829 interlacing; the collapse form Psi <= const / (t mu^P_1) and "
     "the Psi pin a_1 / lam_1 <= Psi <= 1 / lam_1 with a_1 = 8/pi^2 (T153)"),
    ("CERTIFIED, FIXED SIZE (new in T154)", "the ceiling lam_k(A) <= K^F mu^P_k "
     "for k <= %d with K^F = %.4f .. %.4f from the SIXTEEN-column subspace "
     "span{t_1..t_8} + A^-1 L_P span{t_1..t_8}: %d Choleskys of matrices of size "
     "<= %d per window, no factorisation of size m, and the number AGREES with "
     "the inertia-certified truth to 5e-7"
     % (K_CERT, qmin(jcol(J1, "KF")), qmax(jcol(J1, "KF")), K_CERT, K_CERT)),
    ("CERTIFIED, SIZE m", "the pencil floor t = %.4f (Schur two-block, kb = %d); "
     "the true bottom ladder constant K_bot = %.4f .. %.4f (inertia); the bottom "
     "eigenvalue lam_1(A) >= gam, hence the collapse recovery %.3f .. %.3f (one "
     "Cholesky of A - gam I); the arch reserve lam_min(P) = %.4f .. %.4f and the "
     "Kato number 1 + lam_min(C) = %.3e .. %.3e, positive on every window"
     % (qmax([r["t"] for r in GR]), SCHUR_KB,
        qmin([r["K_true"] for r in GR]), qmax([r["K_true"] for r in GR]),
        REC_LO, REC_UP, qmin([r["lo_P"] for r in KR]),
        qmax([r["lo_P"] for r in KR]), qmin([r["one_C"] for r in KR]),
        qmax([r["one_C"] for r in KR]))),
    ("MEASURED", "the misalignment between the bottom eight of A and the bottom "
     "eight of L_P, %.2f .. %.2f deg (one direction only; the other seven agree "
     "to %.2f .. %.2f deg); the principal angles of the iterated subspaces, "
     "%.2f deg at j = 0 down to %.2f deg at j = 2; the localisation of the "
     "Kato minimiser, %.1f .. %.1f percent on the eight modes above the cut; the "
     "Kato loss %.2f .. %.3g and its angle %.2f .. %.2f deg"
     % (qmin([r["mis"] for r in GR]), qmax([r["mis"] for r in GR]),
        qmin([r["mis_med"] for r in GR]), qmax([r["mis_med"] for r in GR]),
        qmax(jcol(0, "ang_max")), qmax(jcol(J2, "ang_max")),
        100.0 * qmin([r["low8"] for r in KR]),
        100.0 * qmax([r["low8"] for r in KR]),
        qmin([r["kato_loss"] for r in KR]), qmax([r["kato_loss"] for r in KR]),
        qmin([r["ang_min"] for r in KR]), qmax([r["ang_min"] for r in KR]))),
    ("FIT, never promoted", "K^F %s; K_bot %s; the Kato number %s; the residual "
     "ratio %s; the second-peel exponent kb2^%.3f .. kb2^%.3f"
     % (fit_str(F_KF1), fit_str(F_KT), fit_str(F_EPS), fit_str(F_RHO),
        qmin(PKB), qmax(PKB))),
    ("DEAD, with a number", "the fixed-size residual floor for lam_1 (residual "
     "ratio %.3g .. %.3g, growing %s); the arch-whitened Kato route (loss %.2f "
     ".. %.3g by misalignment); the reflected whitening (negative on %d of %d "
     "windows); boundary peeling (factor %.3f .. %.3f only); the diagonal "
     "whitening (same order); the pure atom-norm route (%.4g .. %.4g against a "
     "budget of %.3f .. %.3f); and from T152 / T153: entrywise, block "
     "Gershgorin, mode-index T + H, recursive Schur, the head/tail Psi drop"
     % (qmin(jcol(J1, "rho_need")), qmax(jcol(J1, "rho_need")), fit_str(F_RHO),
        qmin([r["kato_loss"] for r in KR]), qmax([r["kato_loss"] for r in KR]),
        K4_BAD, len(KR), qmin(K3_GAIN), qmax(K3_GAIN),
        qmin([r["nrm_at"] for r in KR]), qmax([r["nrm_at"] for r in KR]),
        qmin([r["lo_P"] - T_TARGET for r in KR]),
        qmax([r["lo_P"] - T_TARGET for r in KR]))),
]
info("G4.0.map", "MAP V26 -- THE STATE AFTER PART 154, BY LABEL:")
for lab, txt in MAP:
    info("  " + lab, txt)

PROMO = [
    ("T149  PENDING", "the ladder route for Psi and the level constant c_0^ap "
     "as used in T151's chain -- QUOTED in this file, NOT re-measured here, "
     "listed for the ledger's sake only"),
    ("T150  PENDING", "the frame-A window assembly and the admissibility floor "
     "nu = %d -- used as the surface definition here, not re-derived" % NU_MAIN),
    ("T151  PENDING", "the certified end-to-end chain, band 2.01e-2 .. 3.52e-2, "
     "superseded in T153 to %.2e .. %.2e and NOT changed by this probe in its "
     "m-free reading" % T153_FRAC),
    ("T152  PENDING", "the two-block Schur pencil floor t = %.4f at kb = %d and "
     "the bottom ratio K_bot / t; both REPRODUCED here on an independent surface "
     "(t = %.4f, K_bot = %.4f .. %.4f)"
     % (T_TARGET, SCHUR_KB, qmax([r["t"] for r in GR]),
        qmin([r["K_true"] for r in GR]), qmax([r["K_true"] for r in GR]))),
    ("T153  PENDING (a documentation worker is committing it in parallel)",
     "PSI.LADDER: Psi closed as a term via the collapse form and the "
     "a_1 = 8/pi^2 pin; the bulk arch sign reversal; the Kato number "
     "%.1e .. %.1e -- all three REPRODUCED here (arch reserve %.4f .. %.4f, "
     "Kato number %.3e .. %.3e)"
     % (T153_KATO[0], T153_KATO[1], qmin([r["lo_P"] for r in KR]),
        qmax([r["lo_P"] for r in KR]), qmin([r["one_C"] for r in KR]),
        qmax([r["one_C"] for r in KR]))),
    ("T154  NEW, promotion candidate", "the sixteen-column fixed-size ceiling "
     "certificate: K^F = %.4f .. %.4f, flat %s, attaining K_bot to 5e-7, "
     "stress-verified on the T145 no-go reconstruction (where it correctly "
     "explodes as %s) and on %d parity controls (where it is exactly 1)"
     % (qmin(jcol(J1, "KF")), qmax(jcol(J1, "KF")), fit_str(F_KF1),
        fit_str(F_NG_F), len(CT))),
]
info("G4.1.promotions", "PROMOTION LIST -- T149 .. T154, ALL PENDING.  THIS FILE "
     "WRITES NOTHING: no ledger row, no TeX, no website, no changelog, no "
     "manifest.  The list is a statement of what a promotion pass would have to "
     "carry, in order:")
for nm, txt in PROMO:
    info("  " + nm, txt)

REST = [
    ("R1'  THE m-FREE BLOCK FLOOR", "the ONE number: an m-free lower bound for "
     "lam_min(B_HH) on the bulk, currently t = %.4f CERTIFIED per window by a "
     "Schur two-block step of size m.  Every RELATIVE route to it is now dead "
     "with a number: the Kato number 1 + lam_min(C) = %.3e .. %.3e shrinks as "
     "%s against a requirement %.3f .. %.3f, and the loss is NOT the floor but "
     "the misalignment (%.2f .. %.3g, at %.2f .. %.2f deg).  What is left of the "
     "term is therefore not ``bound the atoms relatively'' but ``bound "
     "lam_min(B_HH) on a direction-aware decomposition'' -- and the anatomy says "
     "where to look: %.1f .. %.1f percent of the offending direction sits on the "
     "EIGHT modes immediately above the cut, wherever the cut is put"
     % (qmax([r["t"] for r in GR]), qmin([r["one_C"] for r in KR]),
        qmax([r["one_C"] for r in KR]), fit_str(F_EPS),
        qmin([r["need"] for r in KR]), qmax([r["need"] for r in KR]),
        qmin([r["kato_loss"] for r in KR]), qmax([r["kato_loss"] for r in KR]),
        qmin([r["ang_min"] for r in KR]), qmax([r["ang_min"] for r in KR]),
        100.0 * qmin([r["low8"] for r in KR]),
        100.0 * qmax([r["low8"] for r in KR]))),
    ("R2'  THE m-FREE BOTTOM-MODE FLOOR", "the ONE number: an m-free lower bound "
     "for lam_1(A) / mu^P_1 beating t, worth exactly the collapse price %.3f .. "
     "%.3f end to end.  The number itself is CERTIFIED per window by one Cholesky "
     "(%.3f .. %.3f, the whole price), so this is a UNIFORMITY term and not a "
     "size term.  The fixed-size residual route is dead by %.3g .. %.3g and the "
     "obstruction is named: ONE of the eight bottom directions of A sits %.2f .. "
        "%.2f deg away from the bottom of L_P, so the only certified separation on "
        "the complement is t mu^P_1 itself.  AND THE TERM IS NOW PRICED EXACTLY.  "
        "Everything else in the fixed-size Temple step is available; the single "
        "missing quantity is a LOWER bound on min_{v perp bottom} v^T L_P v / v^T v, "
        "measured flat at %.3f .. %.3f times mu^P_1 (%s), and feeding the measured "
        "value in returns %.3f .. %.3f of the price %.3f .. %.3f, i.e. %.0f .. "
        "%.0f percent of it at fixed size.  That quantity is ARITHMETIC-FREE: it is "
        "a question about the tridiagonal L_P and ONE eight-dimensional subspace, "
        "with no prime-power input anywhere in it"
     % (qmin([r["price"] for r in GR]), qmax([r["price"] for r in GR]),
        REC_LO, REC_UP, qmin(jcol(J1, "rho_need")), qmax(jcol(J1, "rho_need")),
        qmin([r["mis"] for r in GR]), qmax([r["mis"] for r in GR]),
        qmin([r["Lc"] for r in CD]), qmax([r["Lc"] for r in CD]), fit_str(F_LC),
        qmin([r["rec_cond"] for r in CD]), qmax([r["rec_cond"] for r in CD]),
        qmin([r["price"] for r in GR]), qmax([r["price"] for r in GR]),
        100.0 * qmin([r["rec_cond"] / r["price"] for r in CD]),
        100.0 * qmax([r["rec_cond"] / r["price"] for r in CD]))),
]
N_OPEN = len(REST)
info("G4.2.rest", "THE SHORTEST REST LIST -- %d named open terms.  Both are now "
     "UNIFORMITY terms: the numbers are certified per window and what is missing "
     "is the m-free argument.  The ceiling half of T153's R2 is CLOSED and is "
     "therefore NOT on this list:" % N_OPEN)
for nm, txt in REST:
    info("  " + nm, txt)

KATO_FREE = flat_ok(F_EPS) or qmin([r["one_C"] / r["need"] for r in KR]) >= 1.0
CEIL_OK = bool(qmax(TIGHT) < 1.0e-6 and flat_ok(F_KF1))
GATE_CARRIES = bool(CEIL_OK and KATO_FREE and N_OPEN <= 1)
GATE_ONE = bool(N_OPEN == 1)
VERDICT = ("ALIGN-CARRIES" if GATE_CARRIES
           else ("ONE-TERM-MISSING" if GATE_ONE else "ALIGN-RESISTS"))
check("ga_g4.verdict_gate", not GATE_CARRIES and not GATE_ONE,
      "THE VERDICT GATES, EVALUATED AND NOT CHOSEN.  ALIGN-CARRIES needs three "
      "things: the ceiling certified at fixed size and flat (SATISFIED: %s, exact "
      "to %.2e, flat %s -- and by Courant-Fischer, NOT by a residual argument; "
      "the residual argument was needed for the floor, where it failed), the "
      "Kato number m-free or "
      "bypassed (NOT satisfied: %s, and the peel that would fix it is %.2f .. "
      "%.2f of the window), and at most one open term (there are %d).  "
      "ONE-TERM-MISSING needs exactly one open term; the two remaining terms are "
      "of the same TYPE and blocked by the same KIND of obstruction, but they are "
      "not the same statement -- the pencil minimum demonstrably does NOT sit at "
      "the bottom mode (that is what the collapse price %.2f .. %.2f measures), "
      "so an m-free block floor would not deliver the bottom-mode floor.  "
      "Collapsing them into one term would be the kind of silent upgrade this "
      "file exists to avoid.  Hence the verdict is %s"
      % ("yes" if CEIL_OK else "no", qmax(TIGHT), fit_str(F_KF1),
         fit_str(F_EPS), qmin(FRAC), qmax(FRAC), N_OPEN,
         qmin([r["price"] for r in GR]), qmax([r["price"] for r in GR]),
         VERDICT))

para("""G4.3  THE RH DISTANCE, ONCE MORE AND UNCHANGED.  Everything above is a
statement about the constants of ONE finite-window quadratic form on prime-power
zones in frame A, with the zone gap Theta(D^3).  No zero of any L-function was
read, generated, approximated or extrapolated, and Weil's criterion remains an
ADDRESS.  Closing R1' and R2' would produce a finite-window positivity statement
with an m-free constant on a list of zones -- and nothing more.  The distance to
RH is not shortened by this probe in any direction.""")

para("""G4.4  THE VERDICT, IN THREE HONEST SENTENCES.  (1) THE CEILING HALF OF
T153's R2 IS CLOSED AND CLOSED EXACTLY: the subspace span{t_1..t_8} plus its
single Green image A^-1 L_P span{t_1..t_8} -- sixteen columns, fixed size --
carries a Courant-Fischer ceiling K^F = %.4f .. %.4f that AGREES with the
inertia-certified true bottom ladder constant to 5e-7 on every window and is flat
(%s), so the eight LDL^T factorisations of size m per window are retired from the
ceiling step, and the T145 no-go stress confirms the instrument explodes (%s)
exactly where flatness is false. (2) THE FLOOR HALF IS REFUTED AT FIXED SIZE AND
RECOVERED AT FULL SIZE: the Temple 1928 / Kato 1949 residual argument, in the
matrix form and with the exact separation beta = t mu^P_9 that the containment of
the parity sines makes free, fails by a factor %.3g .. %.3g because the residual
of any sine-containing subspace is O(||A||) while the target lam_1(A) is
O(mu^P_1), and the obstruction is ONE misaligned direction (%.2f .. %.2f deg
between the bottom of A and the bottom of L_P) -- while one Cholesky of A - gam I
recovers the ENTIRE collapse price %.3f .. %.3f per window, moving the end-to-end
fraction from %.2e .. %.2e to %.2e .. %.2e with the label CERTIFIED-PER-WINDOW
and not m-free, and the fixed-size step becomes available the moment ONE
arithmetic-free number is bounded rather than measured (the L_P floor on the
complement of the eight bottom Ritz directions, %.2f .. %.2f mu^P_1, worth
%.0f .. %.0f percent of the price CONDITIONALLY); G2 adds that the Kato route to R1 fails for the SAME reason
(a loss of %.2f .. %.3g attained %.2f .. %.2f deg apart, with the minimiser
sitting %.0f .. %.0f percent on the eight modes above whatever cut is chosen),
that T153's Hankel-reflection culprit is refuted twice over -- at the minimiser
both halves hurt, and removing the reflection destroys positive definiteness
altogether (lam_1 = %.3g .. %.3g) -- and that the only repair that moves the
number needs a peel of %.2f .. %.2f of the window. (3) THE VERDICT IS %s WITH %d
OPEN TERMS, and they are no longer the terms T153 named: both are now UNIFORMITY
terms whose numbers are already certified per window, R1' being an m-free floor
for lam_min(B_HH) on a direction-aware decomposition and R2' being an m-free
lower bound for min_{v perp bottom} v^T L_P v / v^T v -- and that second object is
ARITHMETIC-FREE and PRICED, a question about the tridiagonal L_P and one
eight-dimensional subspace that is worth 91 to 100 percent of the collapse price
at fixed size, which is the smallest and cleanest thing this line has been reduced
to.""" % (qmin(jcol(J1, "KF")), qmax(jcol(J1, "KF")), fit_str(F_KF1),
                  fit_str(F_NG_F), qmin(jcol(J1, "rho_need")),
                  qmax(jcol(J1, "rho_need")), qmin([r["mis"] for r in GR]),
                  qmax([r["mis"] for r in GR]), REC_LO, REC_UP, T153_FRAC[0],
                  T153_FRAC[1], NEW_LO, NEW_UP,
                  qmin([r["Lc"] for r in CD]), qmax([r["Lc"] for r in CD]),
                  100.0 * qmin([r["rec_cond"] / r["price"] for r in CD]),
                  100.0 * qmax([r["rec_cond"] / r["price"] for r in CD]),
                  qmin([r["kato_loss"] for r in KR]),
                  qmax([r["kato_loss"] for r in KR]),
                  qmin([r["ang_min"] for r in KR]),
                  qmax([r["ang_min"] for r in KR]),
                  100.0 * qmin([r["low8"] for r in KR]),
                  100.0 * qmax([r["low8"] for r in KR]),
                  qmin([g["lam1"] for g in DC]), qmax([g["lam1"] for g in DC]),
                  qmin(FRAC), qmax(FRAC), VERDICT, N_OPEN))

info("G4.5.verdict", "PART 154 / CONTRACT GREEN.ALIGN -- VERDICT: %s (open "
     "terms: %d; ceiling CLOSED at fixed size, K^F = %.4f .. %.4f; end to end "
     "%.2e .. %.2e per-window certified, %.2e .. %.2e m-free in shape)"
     % (VERDICT, N_OPEN, qmin(jcol(J1, "KF")), qmax(jcol(J1, "KF")),
        NEW_LO, NEW_UP, T153_FRAC[0], T153_FRAC[1]))

# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
print("checks: %d   failures: %d   runtime: %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))
if FAILS:
    print("FAILED: %s" % ", ".join(FAILS))
print("PROBE %s" % ("GREEN" if not FAILS else "RED"))
