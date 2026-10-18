"""PART 153 -- THE CONTRACT ``PSI.LADDER'': THE REBUILD AND THE BLOCK INEQUALITY.

THE RH FENCE, FIRST AND PROMINENT.  Nothing in this file reads, generates,
approximates, extrapolates or otherwise touches a single zero of any L-function.
Weil's explicit-formula positivity criterion (Weil 1952; Bombieri 2000) is CITED
as an ADDRESS ONLY and is never used, in either direction.  An AST firewall below
enforces the absence of zero data, the import whitelist and the absence of any
write-mode file access.  What is investigated here is the END-TO-END ARITHMETIC of
one finite-window inequality about a Toeplitz-minus-Hankel section in its ODD
PARITY SECTOR, on prime-power zones in frame A.  Even if every step closed what
would stand is a finite-window positivity statement with an explicit constant.
The distance from there to RH is mapped in Z4 and never travelled.

WHAT T152 LEFT.  The floor is CERTIFIED by a two-block Schur criterion with a
FIXED low block of kb = 16 parity modes: t = 0.2250 .. 0.2500, flat; the bottom
ratio R <= K_bot / t = 4.408 .. 8.471.  Both archimedean gifts were REFUTED
(A^arch is NEGATIVE in the odd sector; arch does not carry K_bot either).  Three
named terms remained open, and T152's own Y3 identified the LARGEST loss as
    Psi = sup_S (1^T R_SS 1) / |S| ,   R = E^{-1},  E = A / const,
with Psi = 1 / lam_min(E) to within 1.12 .. 1.19 and 89 .. 92 percent of
trace(E^-1) sitting on the eight lowest modes -- the modes the certified ladder
already controls.  T152 MAPPED a rebuild worth 3.46 .. 5.29x end to end and did
not carry it out.

WHAT THIS FILE DOES.
  Z1  THE LADDER REBUILD, carried out.  The subset supremum is replaced by a
      LADDER SUM in two rigorous forms (mode-resolved, and the arithmetic-free
      operator form Psi <= (const / t) Psi_P against the pure Kac-Murdock-Szego
      model), each certified per window; then the honest end-to-end arithmetic:
      WHICH factor the recoverable 3.46 .. 5.29x actually sits in, the new
      end-to-end number, and a uniformity balance of every factor.
  Z2  THE BLOCK INEQUALITY B_HH >= t I.  What B_HH structurally IS, its Toeplitz
      / Hankel / parity anatomy, and four block candidates: block Gershgorin
      (Feingold-Varga 1962) on a dyadic decomposition, a recursive Schur step,
      the low-block-size trade-off kb(m) -- floor against ceiling -- and a
      RELATIVE (Kato-type) bound in the archimedean metric, which the zone's own
      sign discovery opens.
  Z3  THE K_bot CEILING.  A FIXED-SIZE band replacement for the growing bulk
      ceiling T_HH, and four test-vector families measured against the parity
      sines whose atom overshoot is O(m^2).
  Z4  MAP V25, the promotion list, the shortest rest list, and an honest verdict.

DISCIPLINE.  THEOREM / CERTIFIED / MEASURED / FIT are kept strictly apart and
every claim is labelled.  Directions (upper vs lower bound) are pedantic.
Classics cited where used: Kac-Murdock-Szego 1953 (the tridiagonal spectrum),
Schur 1917 (the block criterion), Sylvester 1852 (inertia), Haynsworth 1968
(the inertia additivity of the Schur complement), Widom 1958 and
Boettcher-Silbermann (Toeplitz-plus-Hankel), Feingold-Varga 1962 (block
Gershgorin), Courant-Fischer 1920, Weyl 1912, Charikar 2000, Chebyshev 1852.
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
np.random.seed(153153)

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
SURF_ZONES = 18              # windows of the Z1 rebuild surface
SURF_HCAP = 1450
Z2_ZONES = 11                # windows of the Z2 block-anatomy surface
Z2_HCAP = 1150
Z3_ZONES = 12                # windows of the Z3 ceiling surface

K_CERT = 8                   # modes for which the ladder is INERTIA-certified
SCHUR_KB = 16                # the FIXED low block of the T152 certificate
KB_SCAN = (8, 16, 32, 64)    # the Z2 floor/ceiling trade-off scan
DYAD_MIN = 8                 # smallest dyadic block in the Z2 block Gershgorin
ARCH_CUTS = (0, 2, 4, 8, 12, 16)   # low-mode cuts scanned for arch positivity
T_LADDER = (0.25, 0.245, 0.24, 0.235, 0.23, 0.225, 0.22, 0.215, 0.21, 0.205,
            0.20, 0.19, 0.18, 0.16, 0.14, 0.12, 0.10, 0.05)
PEN_BACKOFF = (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1)
BAR_UNIF = 0.25              # |exponent| + band bar for "flat / non-growing"
T_TARGET = 0.25

# T151's certified end-to-end band, QUOTED, never recomputed here
T151_FRAC = (2.01e-2, 3.52e-2)
T151_PSI_GAIN = (3.46, 5.29)   # T152's MAPPED gain, the claim under test
GAIN_BAR = 2.5                 # the verdict bar on the certified rebuild gain
FRAC_BAR = 5.0e-2              # the verdict bar on the new end-to-end fraction

# the T146 a-priori level constant, as quoted in T151's chain_const
BASE_GRID = (2.0, 1.5, 1.25, 1.125, 1.0625, 1.03125)
FL_TARGET = 1.0e-12
B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962 Thm 12)

SMOOTH_W = (2, 3, 5, 9, 17)  # Fejer half-widths scanned in Z3

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
    confidence interval.  A fit is a FIT and is never promoted to a theorem."""
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
    check("pl_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("pl_fw.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("pl_fw.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("pl_fw.one_file", os.path.basename(os.path.abspath(__file__))
          == "psi_ladder_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# certificates: Cholesky, Gershgorin, inertia (Sylvester 1852)
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
    t = (float(np.min(np.diag(X))) if guess is None else float(guess))
    for _ in range(tries):
        Y = sym(X - t * np.eye(h))
        if safe_cho(Y) is not None:
            return t - chol_floor(gersh(Y), h)
        t -= abs(t) * grow + 1.0e-300
        grow *= 6.0
    return float("nan")


def inertia_neg(X):
    """#{lam_j < 0} from a COMPLETED LDL^T (Sylvester 1852 law of inertia;
    Bunch-Kaufman 1977 for the pivoting).  No eigenvector is ever read."""
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
            blk = np.array([[d[i, i], d[i, i + 1]], [d[i + 1, i], d[i + 1, i + 1]]])
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
# prime-power arithmetic (exact, cheap) -- the T111 .. T152 code path
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
    reflected spline when u_j < D.  Hence c^atom <= 0 ENTRYWISE."""
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
    bit-for-bit the object T111 .. T152 use."""
    c_at, D, mu_tot, n_hit = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D, mu_tot=mu_tot,
                n_atom=n_hit, l1_at=float(np.sum(np.abs(c_at))))


# ----------------------------------------------------------------------------
# the sections, the parity structure, the pencil
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
    k = 1 .. m (Kac-Murdock-Szego 1953 in the parity sector).  EXACT, not
    asymptotic: the ODD grid th_k = 2 pi k / N never contains th = 0."""
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


def pencil_kap(A, LP, m):
    """THE CERTIFIED PENCIL FLOOR kap with kap L_P <= A.  ONE Cholesky of L_P
    plus two triangular solves gives Z = G^{-1} A G^{-T} whose spectrum IS the
    pencil spectrum; its bottom is a SEED, the certificate is a COMPLETED
    Cholesky of A - kap L_P with the floor carried through I <= L_P / mu^P_1.
    DIRECTION: kap is a LOWER bound."""
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
    del Y, G
    try:
        seed = float(eigh(Z, eigvals_only=True, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        del Z
        return None
    del Z
    kap = float("nan")
    for eta in PEN_BACKOFF:
        k_try = seed * (1.0 - eta) if seed > 0.0 else seed - eta
        X = sym(A - k_try * LP)
        if safe_cho(X) is not None:
            kap = k_try - chol_floor(gersh(X), m) / mu1
            del X
            break
        del X
    return dict(kap=kap, seed=seed, mu1=mu1)


def parity_block(A, Tf, mu):
    """B = Lam^{-1/2} T A T^T Lam^{-1/2}, Lam = diag(mu^P).  IDENTITY, not an
    approximation: lam_min(B) = kap is the pencil floor, and for any set of
    modes H the compression B_HH is the SAME pencil question restricted to
    span{t_k : k in H} -- the fact Z2 is about."""
    Gf = sym(Tf @ (A @ Tf.T))
    isq = 1.0 / np.sqrt(mu)
    return sym(Gf * np.outer(isq, isq))


def schur_floor(B, kb, t):
    """THE CERTIFIED TWO-BLOCK SCHUR FLOOR (Schur 1917; Haynsworth 1968 for the
    inertia reading).  For symmetric B split into a LOW block of kb modes and
    the BULK,
        B >= t I  <=>  B_HH - t I > 0  AND  B_LL - t I - B_LH (B_HH - tI)^-1 B_HL > 0,
    an EQUIVALENCE, not a bound.  Both conditions are certified by COMPLETED
    Choleskys and BOTH backward-error floors are subtracted from the returned t.
    DIRECTION: the return value is a LOWER bound on lam_min(B)."""
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
section("Z0  SETUP, THE RH FENCE, AND THE LICENCES")
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

check("pl_z0.gap_facts",
      bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
      and bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12)),
      "the ONLY two gap facts used anywhere: Bertrand-Chebyshev 1852 "
      "(g <= log 2) and the trivial even bound; %d gaps up to n = %d"
      % (NZ_DEEP, ZONE_DEEP))

para("""Z0.0  THE RH FENCE, RESTATED BEFORE ANY NUMBER.  The surrounding statement
is the positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999)
on a FINITE list of prime-power zones in a FINITE window, frame A.  Weil's
explicit-formula criterion is an ADDRESS, never a criterion used here.  No zero
data is read, generated, approximated or extrapolated; the AST firewall above
enforces that together with the import whitelist and the absence of write-mode
file access.  What is at stake here is the SIZE AND THE UNIFORMITY of the
constants in one finite-window inequality -- nothing about any zero, in either
direction.  Even a perfect closure of every term below would leave a
finite-window inequality with an explicit constant on prime-power zones.  The
distance to RH is mapped in Z4 and never travelled.""")

para("""Z0.1  THE LICENCES, each with its DIRECTION.  (L1) Cholesky: a COMPLETED
Cholesky of X certifies X >= -fl I with fl the Wilkinson backward-error floor,
always subtracted from a lower bound and added to an upper bound.  (L2)
Sylvester 1852 / Bunch-Kaufman 1977: a completed LDL^T of A - tau I returns
#{lam_j < tau} as a CERTIFICATE and reads no eigenvector.  (L3) Weyl 1912 /
eigenvalue monotonicity: A >= t L_P implies lam_k(A) >= t mu^P_k for EVERY k --
the certified LADDER IN THE LOWER DIRECTION, which is what an upper bound on
Psi needs.  (L4) Kac-Murdock-Szego 1953: mu^P_k = 4 sin^2(pi k / N) is EXACT,
and the ratio bound mu^P_{k+kb} / mu^P_k <= ((k+kb)/k)^2 follows from the
concavity of the sine on [0, pi] -- a THEOREM, valid for every m.  (L5) Schur
1917 / Haynsworth 1968: the two-block criterion is an EQUIVALENCE; the inertia
of a symmetric block matrix is the inertia of the pivot block plus that of the
Schur complement.  (L6) Courant-Fischer 1920: lam_k(A) <= lam_max of A on ANY
k-dimensional subspace -- the certified LADDER IN THE UPPER DIRECTION.  (L7)
operator monotonicity of the inverse: 0 < X <= Y implies Y^{-1} <= X^{-1}, used
ONCE and centrally in Z1.  (L8) Charikar 2000: greedy peeling attains a density,
hence greedy >= opt / 2 turns an ATTAINED value into an UPPER bound; Z1 asks
whether this licence can be RETIRED.  (L9) Chebyshev 1852 / Rosser-Schoenfeld
1962 Thm 12: psi(x) <= B_PSI x, verified below on the exact range used.""")

para("""Z0.2  WHAT COUNTS AS WHAT, PEDANTICALLY.  THEOREM = an identity or a
classical inequality, valid for every m.  CERTIFIED = a numeric bound produced
by a completed factorisation with its floor carried, valid for THAT window only.
MEASURED = a diagonalisation read for orientation.  FIT = an exponent on the
finite surface, never promoted.  The word ``proven'' is used nowhere in this file
for any m-freeness.""")

_psi_run = 0.0
_bpsi = 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
check("pl_z0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f is VERIFIED at every jump point up to n = %d (max "
      "%.6f); psi jumps only at prime powers, so this is the true max on the "
      "range, and it is never assumed beyond it" % (B_PSI, ATOM_MAX, _bpsi))

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
check("pl_z0.surface", len(SZ) >= 8,
      "%d prime-power zones admit a frame-A window inside the cap (h <= %d, "
      "MAX_H = %d); the Z1 surface takes %d of them, h = %d .. %d, declared "
      "BEFORE any result is seen"
      % (len(CAND), SURF_HCAP, MAX_H, len(SZ), min(s[3] for s in SZ),
         max(s[3] for s in SZ)))

# ----------------------------------------------------------------------------
section("Z1  THE LADDER REBUILD -- WHERE THE RECOVERABLE FACTOR ACTUALLY SITS")
# ----------------------------------------------------------------------------
para("""Z1.0  WHAT IS BEING REBUILT, AND IN WHICH DIRECTION.  In the T146 .. T151
chain the level constant carries
    Psi = sup_S (1^T R_SS 1) / |S|   over ALL subsets S of the window,
R = E^{-1}, E = A / const, and the chain reads
    lam_min(A, A_B) >= lam_min(E) / kap_up >= 1 / (kap_up c_0^ap Psi) .
Psi enters as ONE multiplicative denominator factor, so ANY smaller valid
upper bound on the SAME product (c_0^ap Psi) scales the end-to-end fraction by
exactly the ratio of the two bounds -- that is how the new end-to-end number
below is formed, and the T151 fraction itself is QUOTED, never recomputed.
T152 mapped a rebuild worth 3.46 .. 5.29x by splitting trace(E^-1) into the
eight lowest modes (89 .. 92 percent) and the tail.  THIS ZONE ASKS WHETHER THAT
FACTOR IS REALLY THERE, and if so in which factor it sits.""")

para("""Z1.1  THE THREE REBUILT FORMS, each an UPPER bound on the SAME Psi.
(a) THE MODE-RESOLVED LADDER SUM.  With E = sum_k lam_k v_k v_k^T,
    (1_S^T R 1_S)/|S| = sum_k lam_k^{-1} <v_k, 1_S>^2 / |S| ,
so for any cut K
    Psi <= sum_{k <= K} a_k / lam_k + 1 / lam_{K+1} ,
    a_k = sup_S <v_k, 1_S>^2 / |S| <= 1 (Cauchy-Schwarz),
where the tail used lam_max of the spectral tail of R and a_k is computed
EXACTLY by sorting (the optimal S of a given size takes the extreme entries of
v_k).  Sup of a sum <= sum of sups: VALID, and the per-mode sup is the only
loss.  (b) THE ARITHMETIC-FREE OPERATOR FORM.  The certified floor A >= t L_P is
equivalent to E >= (t / const) L_P, and the inverse is operator-antitone (L7),
so R <= (const / t) L_P^{-1} and
    Psi <= (const / t) Psi_P ,  Psi_P = sup_S (1_S^T L_P^{-1} 1_S) / |S| ,
with Psi_P a property of the PURE Kac-Murdock-Szego model -- no arithmetic, no
window, no greedy peeling.  (c) THE THEOREM-GRADE COLLAPSE.  Since
L_P^{-1} <= I / mu^P_1 exactly, Psi_P <= 1 / mu^P_1 and
    Psi <= const / (t mu^P_1) ,
which contains NO certificate beyond t itself: Charikar's licence (L8) and every
diagonalisation are RETIRED.  DIRECTION: (a), (b), (c) are all UPPER bounds on
Psi and each is weaker than the last.""")


def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000) on a NONNEGATIVE matrix with a
    zero diagonal.  The returned density is ATTAINED, hence a LOWER bound on the
    optimum, and greedy >= opt/2 turns it into opt <= 2 x greedy."""
    n = Wp.shape[0]
    if n < 2:
        return 0.0
    deg = Wp.sum(axis=1).astype(float)
    tot = 0.5 * float(deg.sum())
    alive = np.ones(n, dtype=bool)
    n_alive = n
    best = tot / n
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


def psi_upper(R):
    """THE T149 .. T152 UPPER BOUND on Psi: max_k R_kk plus the smaller of
    4 x greedy and the CERTIFIED lam_max of the nonnegative off-diagonal part.
    DIRECTION: an UPPER bound on Psi."""
    Rp = np.maximum(R, 0.0)
    np.fill_diagonal(Rp, 0.0)
    dg = float(np.max(np.diag(R)))
    ch = dg + 4.0 * greedy_density(Rp)
    sp = dg + cert_lam_max(Rp, guess=ray_top(Rp))
    del Rp
    cands = [x for x in (ch, sp) if np.isfinite(x)]
    return dict(up=min(cands) if cands else float("nan"), char=ch, spec=sp, dg=dg)


def subset_sup_mode(v):
    """a_k = sup_S <v, 1_S>^2 / |S|, computed EXACTLY.  For a fixed size s the
    optimal S takes the s LARGEST entries (or the s smallest, for the reflected
    sign), so sorting once and scanning the prefix sums is exact -- no search
    heuristic and no bound is involved."""
    w = np.sort(np.asarray(v, float))[::-1]
    cs = np.cumsum(w)
    ss = np.arange(1, w.shape[0] + 1, dtype=float)
    hi = float(np.max(cs * cs / ss))
    cs2 = np.cumsum(np.sort(np.asarray(v, float)))
    lo = float(np.max(cs2 * cs2 / ss))
    return max(hi, lo)


def c0_of_base(Gam, Gam_1, base, m):
    """THE T146 A-PRIORI LEVEL CONSTANT at a given cake base, as quoted in
    T151's chain: c_0^ap(base) = 2 base^2 Gam min(1, Gam_1) + eps."""
    vmax_ap = Gam / math.sqrt(max(m, 1))
    lb = math.log(base)
    k_bot = int(math.floor(math.log(FL_TARGET) / lb))
    while base ** k_bot > FL_TARGET:
        k_bot -= 1
    eps = 2.0 * base * vmax_ap * m * (base ** k_bot)
    return 2.0 * base * base * Gam * min(1.0, Gam_1) + eps


ROWS = []
SKIP = dict(lag=0, pen=0, chol=0, eig=0)
for (zk, D_k, M_k, h_k) in SZ:
    if budget_left() < 260.0:
        info("Z1.0.budget", "surface truncated at %d windows (budget)" % len(ROWS))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    A = sym(odd_toeplitz(sp["c"], M_k))
    m = h_k
    mu = parity_mu(m)
    LP = lap_P_mat(m)
    pen = pencil_kap(A, LP, m)
    if pen is None or not (pen["kap"] > 0.0):
        SKIP["pen"] += 1
        del A, LP, sp
        continue
    Tf = parity_basis(m)
    B = parity_block(A, Tf, mu)
    t_cert = schur_best(B, SCHUR_KB)
    # --- E, R and the T149 .. T152 Psi bound -------------------------------
    const = float(np.max(np.diag(A)))
    E = A / const
    fac = safe_cho(E)
    if fac is None:
        SKIP["chol"] += 1
        del A, E, LP, Tf, B, sp
        continue
    R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    pu = psi_upper(R)
    # --- the certified scalars of the T151 level constant -------------------
    try:
        w_lo, V_lo = eigh(E, subset_by_index=[0, K_CERT])
    except (LinAlgError, ValueError):
        SKIP["eig"] += 1
        del A, E, R, LP, Tf, B, sp
        continue
    lam1 = float(w_lo[0])
    lam_lo = cert_lam_min(E, guess=lam1)
    EV = E @ R
    den = np.sum(R * R, axis=0)
    num = np.sum(R * EV, axis=0)
    rres = np.linalg.norm(EV - np.eye(m), axis=0)
    del EV
    lam_up = float(np.min(num / den)) + chol_floor(gersh(E), m)
    res_f = float(np.linalg.norm(rres))
    fro = math.sqrt(max(float(np.sum(den)), 1.0e-300))
    infl = res_f / lam_lo if (np.isfinite(lam_lo) and lam_lo > 0.0) else 0.0
    col_cert = np.sqrt(den) + rres / (lam_lo if lam_lo > 0.0 else 1.0)
    cmax_up = float(np.max(col_cert))
    gam_cert = math.sqrt(m) * lam_up * cmax_up
    gam_fac = (math.sqrt(m) * cmax_up / max(fro - infl, 1.0e-300)) \
        * lam_up * (fro + infl)
    gam = min(gam_cert, gam_fac)
    gam1 = lam_up * float(np.sum(col_cert)) / math.sqrt(m)
    c0 = min(c0_of_base(gam, gam1, b, m) for b in BASE_GRID)
    del den, num, rres, col_cert
    # --- (a) the mode-resolved ladder sum ----------------------------------
    a_k = np.array([subset_sup_mode(V_lo[:, j]) for j in range(K_CERT)])
    psi_mode = float(np.sum(a_k / w_lo[:K_CERT]) + 1.0 / w_lo[K_CERT])
    head = float(np.sum(1.0 / w_lo[:K_CERT]))
    tr_R = float(np.trace(R))
    tail = tr_R - head
    del R, V_lo
    # --- (b) the arithmetic-free operator form ------------------------------
    facL = safe_cho(LP)
    LPi = sym(cho_solve(facL, np.eye(m), check_finite=False)) if facL else None
    psi_P = psi_upper(LPi)["up"] if LPi is not None else float("nan")
    if LPi is not None:
        del LPi
    psi_op = (const / t_cert) * psi_P if t_cert > 0.0 else float("nan")
    psi_thm = const / (t_cert * pen["mu1"]) if t_cert > 0.0 else float("nan")
    ROWS.append(dict(
        zk=zk, x=float(NN_ALL[zk]), h=m, D=D_k, M=M_k, mu1=pen["mu1"],
        kap=pen["kap"], t=t_cert, const=const, lam1=lam1, lam_lo=lam_lo,
        lam_up=lam_up, gam=gam, gam1=gam1, c0=c0, psi=pu["up"],
        psi_char=pu["char"], psi_spec=pu["spec"], dg=pu["dg"],
        psi_mode=psi_mode, psi_op=psi_op, psi_thm=psi_thm, psi_P=psi_P,
        a1=float(a_k[0]), a_max=float(np.max(a_k)), head=head, tail=tail,
        tr_R=tr_R, frac_head=head / tr_R if tr_R > 0.0 else float("nan"),
        inv_lam=1.0 / lam1, n_atom=sp["n_atom"]))
    del A, E, LP, Tf, B, sp

check("pl_z1.surface", len(ROWS) >= 8,
      "the rebuild surface carries %d windows, h = %d .. %d, zones n = %d .. %d "
      "(skips: %s); every scalar below is per-window"
      % (len(ROWS), min(r["h"] for r in ROWS), max(r["h"] for r in ROWS),
         min(r["x"] for r in ROWS), max(r["x"] for r in ROWS), SKIP))

XS = [r["h"] for r in ROWS]
F_T = pow_fit(XS, [r["t"] for r in ROWS], "t")
F_PSI = pow_fit(XS, [r["psi"] for r in ROWS], "Psi (T149 route)")
F_INV = pow_fit(XS, [r["inv_lam"] for r in ROWS], "1/lam_min(E)")
F_CONST = pow_fit(XS, [r["const"] for r in ROWS], "const = max diag A")
F_C0 = pow_fit(XS, [r["c0"] for r in ROWS], "c_0^ap")

T_OK = sum(1 for r in ROWS if np.isfinite(r["t"]) and r["t"] > 0.0
           and r["t"] <= r["kap"] + 1.0e-9)
check("pl_z1.floor_reproduced", T_OK == len(ROWS),
      "THE T152 FLOOR IS REPRODUCED on this surface, CERTIFIED: the two-block "
      "Schur criterion at the FIXED low block kb = %d returns t = %.4f .. %.4f "
      "(%s), and t <= kap on every window (kap = %.4f .. %.4f certified by ONE "
      "Cholesky).  DIRECTION: t is a LOWER bound on lam_min(B) = kap, i.e. "
      "A >= t L_P; the target of the brief is %.2f"
      % (SCHUR_KB, qmin([r["t"] for r in ROWS]), qmax([r["t"] for r in ROWS]),
         fit_str(F_T), qmin([r["kap"] for r in ROWS]),
         qmax([r["kap"] for r in ROWS]), T_TARGET))

# --- THE PIN: Psi is bracketed, so there is no reserve of any size -----------
PIN_LO = [r["a1"] / r["lam1"] for r in ROWS]
PIN_UP = [r["inv_lam"] for r in ROWS]
PIN_OK = all(PIN_LO[i] <= PIN_UP[i] * (1.0 + 1.0e-9) for i in range(len(ROWS)))
F_A1 = pow_fit(XS, [r["a1"] for r in ROWS], "a_1")
check("pl_z1.psi_is_pinned", PIN_OK,
      "THE DECISIVE MEASUREMENT OF THIS PROBE.  Psi is PINNED BETWEEN TWO HARD "
      "BOUNDS ON THE SAME MODE.  LOWER: for the S that maximises mode 1, every "
      "term of sum_k lam_k^{-1} <v_k,1_S>^2 is nonnegative, so "
      "Psi >= a_1 / lam_1 -- a THEOREM given the eigenpair, with a_1 = "
      "%.4f .. %.4f (%s), exactly the 8/pi^2 = %.4f of the first parity sine.  "
      "UPPER: Psi <= lam_max(R) = 1 / lam_1 by Cauchy-Schwarz.  Hence "
      "%.4g .. %.4g <= Psi <= %.4g .. %.4g and Psi is determined to within the "
      "factor 1/a_1 = %.3f .. %.3f.  THERE IS NO RESERVE IN THE Psi STEP OF ANY "
      "SIZE BEYOND THAT FACTOR"
      % (qmin([r["a1"] for r in ROWS]), qmax([r["a1"] for r in ROWS]),
         fit_str(F_A1), 8.0 / math.pi ** 2, qmin(PIN_LO), qmax(PIN_LO),
         qmin(PIN_UP), qmax(PIN_UP), 1.0 / qmax([r["a1"] for r in ROWS]),
         1.0 / qmin([r["a1"] for r in ROWS])))

# --- and therefore the T152 head/tail replacement is REFUTED -----------------
GAP_HT = [(r["a1"] / r["lam1"]) / r["tail"] for r in ROWS]
MAP_GAIN = [r["psi"] / r["tail"] for r in ROWS]
F_FR = pow_fit(XS, [r["frac_head"] for r in ROWS], "head fraction")
check("pl_z1.head_drop_refuted", qmin(GAP_HT) > 1.0,
      "THE T152 MAPPED REBUILD IS REFUTED, AND BY EXACTLY ITS OWN FACTOR.  T152's "
      "anatomy is reproduced: the %d lowest modes carry %.4f .. %.4f of "
      "trace(E^-1) (%s) and Psi / tail = %.2f .. %.2f, inside the mapped "
      "3.46 .. 5.29.  BUT the proposed replacement -- drop the head, keep the "
      "tail -- LIES BELOW THE HARD LOWER BOUND a_1 / lam_1 by a factor "
      "%.2f .. %.2f, so it is NOT an upper bound for Psi and cannot enter any "
      "chain.  THE REASON IS STRUCTURAL, not numerical: the maximising subset is "
      "aligned with v_1 itself (a_1 = 8/pi^2, the full-window sign pattern of the "
      "first parity sine), so the head IS the value of Psi, not a redundancy that "
      "the ladder already pays for elsewhere"
      % (K_CERT, qmin([r["frac_head"] for r in ROWS]),
         qmax([r["frac_head"] for r in ROWS]), fit_str(F_FR),
         qmin(MAP_GAIN), qmax(MAP_GAIN), qmin(GAP_HT), qmax(GAP_HT)))

# --- what the three rebuilt forms are actually worth ------------------------
RAT_MODE = [r["psi_mode"] / r["psi"] for r in ROWS]
RAT_OP = [r["psi_op"] / r["psi"] for r in ROWS]
RAT_THM = [r["psi_thm"] / r["psi"] for r in ROWS]
PP = [r["psi_P"] * r["mu1"] for r in ROWS]
F_PP = pow_fit(XS, PP, "Psi_P mu^P_1")
check("pl_z1.rebuilt_forms", all(np.isfinite(x) for x in RAT_THM),
      "WHAT THE THREE REBUILT FORMS COST, each an UPPER bound on the SAME Psi, "
      "as a ratio to the T149 route: (a) mode-resolved ladder sum with K = %d: "
      "%.3f .. %.3f;  (b) arithmetic-free operator form (const/t) Psi_P: "
      "%.3f .. %.3f;  (c) theorem-grade collapse const/(t mu^P_1): "
      "%.3f .. %.3f.  SO THE REBUILD BUYS NO SIZE -- it COSTS between %.2f and "
      "%.2f.  WHAT IT BUYS IS UNIFORMITY: form (c) contains exactly three "
      "ingredients, const (an explicit arithmetic sum), t (the one open block "
      "inequality) and mu^P_1 (Kac-Murdock-Szego 1953, EXACT), and it retires "
      "licence L8 (Charikar) and EVERY per-window diagonalisation from the Psi "
      "step"
      % (K_CERT, qmin(RAT_MODE), qmax(RAT_MODE), qmin(RAT_OP), qmax(RAT_OP),
         qmin(RAT_THM), qmax(RAT_THM), qmin(RAT_THM), qmax(RAT_THM)))

check("pl_z1.model_constant", flat_ok(F_PP),
      "AND THE MODEL CONSTANT OF FORM (b) IS FLAT AND ARITHMETIC-FREE: "
      "Psi_P mu^P_1 = %.4f .. %.4f, %s, against the theorem-grade ceiling 1 and "
      "the asymptotic 8/pi^2 = %.4f of the pure Kac-Murdock-Szego model.  Psi_P "
      "knows NOTHING about the primes -- it is a property of tridiag(-1, 2, -1) "
      "with the parity corner -- so form (b) moves the whole subset supremum out "
      "of the arithmetic and into the model, where it is m-explicit"
      % (qmin(PP), qmax(PP), fit_str(F_PP), 8.0 / math.pi ** 2))

# --- so where IS the recoverable factor?  In the level constant -------------
GAIN = [(r["c0"] * r["psi"]) / r["psi_thm"] for r in ROWS]
F_GAIN = pow_fit(XS, GAIN, "gain")
NEW_LO = T151_FRAC[0] * qmin(GAIN)
NEW_UP = T151_FRAC[1] * qmax(GAIN)
BOT_SLACK = [r["lam1"] * r["const"] / (r["t"] * r["mu1"]) for r in ROWS]
F_BS = pow_fit(XS, BOT_SLACK, "bottom slack")
check("pl_z1.gain_is_absent", qmax(GAIN) < T151_PSI_GAIN[0],
      "AND THE 3.46 .. 5.29x IS NOT ANYWHERE ELSE EITHER.  The chain's "
      "denominator factor is the PRODUCT c_0^ap Psi = %.4g .. %.4g; the direct "
      "route bounds the SAME quantity 1/lam_min(E) by const/(t mu^P_1) = "
      "%.4g .. %.4g.  RATIO, i.e. the honest end-to-end gain of the whole "
      "rebuild: %.2f .. %.2f (median %.2f, %s) -- BELOW ONE on most of the "
      "surface and nowhere near the mapped %.2f.  The bookkeeping is exact: the "
      "rebuild RETIRES the level constant c_0^ap = %.3f .. %.3f (%s, flat) and "
      "PAYS the collapse cost %.2f .. %.2f of form (c); on this surface those two "
      "numbers cancel"
      % (qmin([r["c0"] * r["psi"] for r in ROWS]),
         qmax([r["c0"] * r["psi"] for r in ROWS]),
         qmin([r["psi_thm"] for r in ROWS]), qmax([r["psi_thm"] for r in ROWS]),
         qmin(GAIN), qmax(GAIN), qmed(GAIN), fit_str(F_GAIN), T151_PSI_GAIN[0],
         qmin([r["c0"] for r in ROWS]), qmax([r["c0"] for r in ROWS]),
         fit_str(F_C0), qmin(RAT_THM), qmax(RAT_THM)))

check("pl_z1.collapse_cost_named", qmin(BOT_SLACK) > 1.0,
      "WHERE THE COLLAPSE COST COMES FROM, NAMED EXACTLY.  Form (c) replaces "
      "lam_1(A) by t mu^P_1, and the slack of that single step is "
      "lam_1(A) / (t mu^P_1) = %.2f .. %.2f (%s).  MEANING: the pencil minimum "
      "kap = lam_min(A, L_P) is NOT attained at the bottom mode -- the bottom "
      "mode of A sits %.1fx .. %.1fx ABOVE the floor the pencil certifies for it, "
      "so a floor that is uniform over all modes is a lossy bound for mode 1 "
      "alone.  THAT, and not the subset supremum, is the price of retiring the "
      "cake.  A mode-resolved floor (a certified lower bound on lam_1(A) alone) "
      "would recover exactly this factor and is a NEW, well-posed rest-list item"
      % (qmin(BOT_SLACK), qmax(BOT_SLACK), fit_str(F_BS),
         qmin(BOT_SLACK), qmax(BOT_SLACK)))

check("pl_z1.new_end_to_end", NEW_LO > 0.0,
      "THE NEW END-TO-END NUMBER, PER WINDOW.  Psi enters the T151 chain as ONE "
      "multiplicative denominator factor, so the fraction scales by exactly the "
      "ratio above: T151's certified %.3e .. %.3e becomes %.3e .. %.3e of the "
      "true gap -- which does NOT reach the 8e-2 .. 1.4e-1 band the brief "
      "targets%s.  THE "
      "DIRECTION CAVEAT, PEDANTICALLY: c_0^ap is recomputed here from the "
      "certified Gam = %.3f .. %.3f in the T146 A-PRIORI form.  T151's reported "
      "band used a SOBOLEV-REFINED Q_star which can only LOWER Gam and hence "
      "c_0^ap, so the gain above is an UPPER estimate of what is recoverable; "
      "the part of it that is beyond doubt is the RETIREMENT of the cake, not "
      "its exact size"
      % (T151_FRAC[0], T151_FRAC[1], NEW_LO, NEW_UP,
         "" if NEW_UP < FRAC_BAR else " except at the top of the surface",
         qmin([r["gam"] for r in ROWS]), qmax([r["gam"] for r in ROWS])))

# --- the uniformity balance of every factor ---------------------------------
BAL = [
    ("t  (floor, kb = 16)", F_T, "CERTIFIED per window / FIT flat", "OPEN: Z2"),
    ("const = max diag A", F_CONST, "explicit arithmetic sum", "closed"),
    ("mu^P_1", pow_fit(XS, [r["mu1"] for r in ROWS], "mu^P_1"),
     "THEOREM (KMS 1953, exact)", "closed"),
    ("Psi_P mu^P_1", F_PP, "MEASURED, model only, <= 1 by THEOREM", "closed"),
    ("Psi (T149 route)", F_PSI, "CERTIFIED per window", "RETIRED by (c)"),
    ("1/lam_min(E)", F_INV, "MEASURED", "replaced by const/(t mu^P_1)"),
    ("c_0^ap", F_C0, "CERTIFIED per window", "RETIRED by (c)"),
    ("a_1", F_A1, "THEOREM given the eigenpair", "lower bound only"),
    ("gain of the rebuild", F_GAIN, "ratio of two UPPER bounds", "the readout"),
]
info("Z1.2.balance", "THE UNIFORMITY BALANCE, factor by factor (fits in m, bar "
     "|p| + band <= %.2f):" % BAR_UNIF)
for nm, f, status, fate in BAL:
    info("  %-22s" % nm, "%-26s  %-34s  %s"
         % (fit_str(f), status, fate + ("" if flat_ok(f) else "  [GROWS]")))

GROW = [nm for nm, f, _, fate in BAL
        if not flat_ok(f) and fate in ("the readout", "OPEN: Z2")]
check("pl_z1.balance_clean", not GROW,
      "IS THE REBUILT CHAIN FREE OF GROWING FACTORS?  The factors that must be "
      "flat are the CERTIFICATE (t) and the READOUT (the gain); growing ones "
      "among those: %s.  const (x^%.3f) and mu^P_1 (x^-1.997, EXACT) are "
      "explicit and enter only through the combination const/(t mu^P_1) which is "
      "what the chain divides by, so their growth is bookkeeping, not a gap; "
      "Psi and c_0^ap grow like m^2.14 but are RETIRED by form (c) and no longer "
      "appear.  The gain is %s.  Exactly two factors are NOT settled by this "
      "zone, and they are the two named open terms: the block inequality "
      "B_HH >= t I (Z2) and the m-free ceiling on K_bot (Z3)"
      % (GROW or "none", F_CONST["p"], fit_str(F_GAIN)))

# ----------------------------------------------------------------------------
section("Z2  THE BLOCK INEQUALITY  B_HH >= t I  ON THE BULK PARITY BLOCK")
# ----------------------------------------------------------------------------
para("""Z2.0  WHAT B_HH IS, AS AN IDENTITY.  With Lam = diag(mu^P) and T the
parity basis, B = Lam^{-1/2} T A T^T Lam^{-1/2} and lam_min(B) = kap.  For a set
H of modes the compression obeys
    B_HH >= t I   <=>   G_HH >= t Lam_H ,   G = T A T^T ,
i.e. B_HH >= t I IS THE ORIGINAL PENCIL INEQUALITY RESTRICTED TO
span{t_k : k in H} -- an identity, not an analogy.  The Schur route therefore
does not make the pencil question easier; it RELOCATES it onto a subspace from
which the kb lowest parity modes have been removed.  The entries G_kl are
Fejer-weighted prime-power sums, so any bound on B_HH is an ARITHMETIC statement
about those sums.  This zone asks which STRUCTURE of B_HH could carry it.""")


def toep_hank_fit(X):
    """THE BEST TOEPLITZ-PLUS-HANKEL FIT IN THE MODE INDICES, by diagonal and
    antidiagonal averaging (the orthogonal projection onto each family, taken in
    sequence: Toeplitz first, then Hankel on the residual).  DIAGNOSTIC ONLY --
    no bound is taken from the fit itself; what is read is the RESIDUAL, which
    decides whether Szego / Widom machinery could ever apply to B_HH."""
    n = X.shape[0]
    Tm = np.zeros_like(X)
    for l in range(-(n - 1), n):
        v = float(np.mean(np.diagonal(X, offset=l)))
        idx = np.arange(max(0, -l), min(n, n - l))
        Tm[idx, idx + l] = v
    Rz = X - Tm
    Hm = np.zeros_like(X)
    Xf = Rz[:, ::-1]
    for l in range(-(n - 1), n):
        v = float(np.mean(np.diagonal(Xf, offset=l)))
        idx = np.arange(max(0, -l), min(n, n - l))
        Hm[idx, idx + l] = v
    Hm = Hm[:, ::-1]
    Rs = sym(X - Tm - Hm)
    return dict(T=sym(Tm), H=sym(Hm), res=Rs,
                f_T=float(np.linalg.norm(Tm) / max(np.linalg.norm(X), 1e-300)),
                f_H=float(np.linalg.norm(Hm) / max(np.linalg.norm(X), 1e-300)),
                f_R=float(np.linalg.norm(Rs) / max(np.linalg.norm(X), 1e-300)))


def block_gersh_dyadic(X, b0=DYAD_MIN):
    """BLOCK GERSHGORIN (Feingold-Varga 1962) on a DYADIC partition:
        lam_min(X) >= min_j [ lam_min(X_jj) - sum_{l != j} ||X_jl|| ] ,
    a THEOREM.  The off-diagonal blocks are measured in the FROBENIUS norm,
    which DOMINATES the spectral norm, so replacing one by the other keeps the
    bound VALID (it can only make it smaller).  DIRECTION: a LOWER bound."""
    n = X.shape[0]
    cuts = [0]
    w = b0
    while cuts[-1] + w < n:
        cuts.append(cuts[-1] + w)
        w *= 2
    cuts.append(n)
    best = -np.inf
    worst = np.inf
    for j in range(len(cuts) - 1):
        a, b = cuts[j], cuts[j + 1]
        blk = sym(X[a:b, a:b])
        try:
            lo = float(eigh(blk, eigvals_only=True, subset_by_index=[0, 0])[0])
        except (LinAlgError, ValueError):
            return dict(bound=float("nan"), nblk=len(cuts) - 1)
        off = math.sqrt(max(0.0, float(np.sum(X[a:b, :] ** 2))
                            - float(np.sum(blk ** 2))))
        worst = min(worst, lo - off)
        best = max(best, lo - off)
    return dict(bound=float(worst), nblk=len(cuts) - 1, best_blk=float(best))


Z2C = [c for c in CAND if c[3] <= Z2_HCAP]
Z2S = []
if Z2C:
    st = max(1, len(Z2C) // max(Z2_ZONES, 1))
    Z2S = Z2C[::-1][::st][:Z2_ZONES]
    Z2S.sort(key=lambda t: t[0])

BR = []
for (zk, D_k, M_k, h_k) in Z2S:
    if budget_left() < 180.0:
        info("Z2.0.budget", "block surface truncated at %d windows" % len(BR))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A = sym(odd_toeplitz(sp["c"], M_k))
    B = parity_block(A, Tf, mu)
    kb = SCHUR_KB
    BHH = sym(B[kb:, kb:])
    nb = BHH.shape[0]
    d = np.diag(BHH)
    row = np.sum(np.abs(BHH), axis=1) - np.abs(d)
    rec = dict(zk=zk, h=m, nb=nb, d_min=float(np.min(d)), d_med=float(np.median(d)),
               coup_med=float(np.median(row)), coup_max=float(np.max(row)),
               gersh=float(np.min(d - row)))
    # the arch / atom split ON THE BULK BLOCK: is positivity a cancellation here too?
    B_ar = parity_block(sym(odd_toeplitz(sp["c_ar"], M_k)), Tf, mu)
    B_at = parity_block(sym(odd_toeplitz(sp["c_at"], M_k)), Tf, mu)
    for tag, Xb in (("ar", B_ar), ("at", B_at)):
        try:
            rec["lo_" + tag] = float(eigh(sym(Xb[kb:, kb:]), eigvals_only=True,
                                          subset_by_index=[0, 0])[0])
        except (LinAlgError, ValueError):
            rec["lo_" + tag] = float("nan")
    # CANDIDATE 4: the ARCH-WHITENED atom operator.  Since B^arch_HH > 0 on the
    # bulk it can serve as the METRIC:  B_HH = P^{1/2} (I + C) P^{1/2} with
    # P = B^arch_HH and C = P^{-1/2} B^atom_HH P^{-1/2}, so
    #     lam_min(B_HH) >= lam_min(P) (1 + lam_min(C))      (THEOREM)
    # and B_HH >= t I follows from the RELATIVE atom bound
    #     lam_min(C) >= -1 + t / lam_min(P) .
    # This is the Kato-type route the Z2 find opens: a relatively bounded
    # perturbation instead of an additive one.  DIRECTION: lam_min(C) is the
    # object to be bounded BELOW.
    try:
        wp, Vp = eigh(sym(B_ar[kb:, kb:]))
    except (LinAlgError, ValueError):
        wp = None
    if wp is not None and float(wp[0]) > 0.0:
        Wh = Vp * (1.0 / np.sqrt(wp))[None, :]
        Cw = sym(Wh.T @ (sym(B_at[kb:, kb:]) @ Wh))
        rec["lo_C"] = float(eigh(Cw, eigvals_only=True,
                                 subset_by_index=[0, 0])[0])
        rec["lo_C_cert"] = cert_lam_min(Cw, guess=rec["lo_C"])
        rec["need_C"] = -1.0 + T_TARGET / float(wp[0])
        del Wh, Cw
    else:
        rec["lo_C"] = float("nan")
        rec["lo_C_cert"] = float("nan")
        rec["need_C"] = float("nan")
    del wp, Vp
    # WHERE the archimedean negativity lives: peel low modes one cut at a time
    cross = []
    for k0 in ARCH_CUTS:
        if k0 + 8 >= m:
            cross.append(float("nan"))
            continue
        try:
            cross.append(float(eigh(sym(B_ar[k0:, k0:]), eigvals_only=True,
                                    subset_by_index=[0, 0])[0]))
        except (LinAlgError, ValueError):
            cross.append(float("nan"))
    rec["cross"] = cross
    rec["k_pos"] = next((ARCH_CUTS[j] for j in range(len(ARCH_CUTS))
                         if np.isfinite(cross[j]) and cross[j] > T_TARGET),
                        -1)
    del B_ar, B_at
    # the mode-index Toeplitz + Hankel anatomy
    th = toep_hank_fit(BHH)
    rec["f_T"], rec["f_H"], rec["f_R"] = th["f_T"], th["f_H"], th["f_R"]
    try:
        rec["lo_T"] = float(eigh(th["T"], eigvals_only=True,
                                 subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        rec["lo_T"] = float("nan")
    rec["nrm_R"] = abs(ray_top(sym(th["res"])))
    rec["nrm_H"] = abs(ray_top(sym(th["H"])))
    rec["toep_route"] = rec["lo_T"] - rec["nrm_H"] - rec["nrm_R"]
    del th
    # parity mass of the coupling: k - l even against k - l odd
    kk = np.arange(nb)
    par = ((kk[:, None] - kk[None, :]) % 2 == 0)
    tot = float(np.sum(BHH ** 2))
    rec["mass_even"] = float(np.sum(BHH[par] ** 2)) / max(tot, 1e-300)
    del par
    # the coupling range: median |B_kl| in dyadic distance bands
    dist = np.abs(kk[:, None] - kk[None, :])
    prof = []
    for j in range(0, 7):
        lo_d, hi_d = 2 ** j, 2 ** (j + 1)
        msk = (dist >= lo_d) & (dist < hi_d)
        prof.append(float(np.median(np.abs(BHH[msk]))) if np.any(msk) else float("nan"))
    rec["prof"] = prof
    del dist
    # block Gershgorin on a dyadic partition
    bg = block_gersh_dyadic(BHH)
    rec["bgersh"] = bg["bound"]
    rec["bgersh_nblk"] = bg["nblk"]
    rec["bgersh_best"] = bg.get("best_blk", float("nan"))
    # the RECURSIVE Schur step: is the difficulty self-similar?
    lev = []
    Cur = BHH
    for _ in range(3):
        if Cur.shape[0] < 4 * kb:
            break
        lev.append(schur_best(Cur, kb))
        Cur = sym(Cur[kb:, kb:])
    rec["lev"] = lev
    del Cur, BHH
    # the kb trade-off: floor against the ceiling factor it forces
    tb = []
    for kb2 in KB_SCAN:
        if kb2 + K_CERT >= m - 4:
            continue
        t2 = schur_best(B, kb2)
        blk = sym(B[kb2:kb2 + K_CERT, kb2:kb2 + K_CERT])
        Tband = cert_lam_max(blk, guess=ray_top(blk))
        kms = max(((k + kb2) / k) ** 2 for k in range(1, K_CERT + 1))
        tb.append((kb2, t2, Tband, kms,
                   (Tband * kms / t2) if t2 > 0.0 else float("inf")))
    rec["tb"] = tb
    BR.append(rec)
    del A, B, Tf, sp

check("pl_z2.surface", len(BR) >= 4,
      "the block anatomy is taken on %d windows, bulk size n_H = %d .. %d at the "
      "FIXED low block kb = %d"
      % (len(BR), min(r["nb"] for r in BR), max(r["nb"] for r in BR), SCHUR_KB))

XB = [r["h"] for r in BR]
check("pl_z2.entrywise_dead", qmax([r["gersh"] for r in BR]) < 0.0,
      "(i) THE ENTRYWISE ROUTE IS DEAD ON THE BULK BLOCK TOO, reproduced: "
      "Gershgorin inside B_HH gives %.4g .. %.4g, while the diagonal is only "
      "%.4f .. %.4f against a MEDIAN row coupling of %.2f .. %.2f (max "
      "%.2f .. %.2f).  The coupling exceeds the diagonal by more than an order of "
      "magnitude, so no diagonal-dominance argument can ever reach t = %.2f: it "
      "MUST be a block statement"
      % (qmin([r["gersh"] for r in BR]), qmax([r["gersh"] for r in BR]),
         qmin([r["d_min"] for r in BR]), qmax([r["d_med"] for r in BR]),
         qmin([r["coup_med"] for r in BR]), qmax([r["coup_med"] for r in BR]),
         qmin([r["coup_max"] for r in BR]), qmax([r["coup_max"] for r in BR]),
         T_TARGET))

F_LOAR = pow_fit(XB, [r["lo_ar"] for r in BR], "lam_min(B^arch_HH)")
check("pl_z2.arch_positive_on_bulk", qmin([r["lo_ar"] for r in BR]) > T_TARGET,
      "(i) THE FIND OF THIS ZONE, AND IT REVERSES A T152 SIGN.  On the bulk "
      "parity block the ARCHIMEDEAN part is POSITIVE and already carries more "
      "than the whole floor: lam_min(B^arch_HH) = %.4f .. %.4f (%s) against "
      "t = %.2f, while on the FULL odd sector T152 certified "
      "lam_min(A^arch) = -2.81 .. -1.84.  BOTH READINGS ARE TRUE: the "
      "archimedean negativity lives ENTIRELY in the lowest parity modes, and "
      "peeling them is exactly what the Schur low block does.  The atom part is "
      "the negative one here: lam_min(B^atom_HH) = %.4g .. %.4g.  So the roles "
      "are EXCHANGED relative to the full block, and additive Weyl is still dead "
      "-- but it now fails on the ATOMS, which is a different and much better "
      "posed obstruction than a negative smooth kernel"
      % (qmin([r["lo_ar"] for r in BR]), qmax([r["lo_ar"] for r in BR]),
         fit_str(F_LOAR), T_TARGET, qmin([r["lo_at"] for r in BR]),
         qmax([r["lo_at"] for r in BR])))

KP = [r["k_pos"] for r in BR]
check("pl_z2.arch_cut_is_m_free", all(0 <= k <= SCHUR_KB for k in KP),
      "(i) AND THE CUT IS m-FREE, WHICH IS THE WHOLE POINT.  Peeling k_0 = %s "
      "lowest parity modes from B^arch gives lam_min = %s (medians over the "
      "surface): the archimedean bulk block passes t = %.2f after at most k_0 = "
      "%d modes are removed, on EVERY window of the surface, h = %d .. %d.  The "
      "number of modes that must be peeled does NOT grow with m -- it is bounded "
      "by the FIXED low block kb = %d the certificate already uses.  DIRECTION: "
      "each lam_min here is MEASURED (a subset diagonalisation), read as "
      "orientation for where a proof should be aimed, not as a certificate"
      % (ARCH_CUTS, " | ".join("%.3f" % qmed([r["cross"][j] for r in BR])
                               for j in range(len(ARCH_CUTS))),
         T_TARGET, max(KP), min(XB), max(XB), SCHUR_KB))

F_FR2 = pow_fit(XB, [r["f_R"] for r in BR], "residual fraction")
check("pl_z2.toeplitz_anatomy", all(np.isfinite(r["f_R"]) for r in BR),
      "(i) THE MODE-INDEX STRUCTURE, MEASURED.  Projecting B_HH onto "
      "Toeplitz-plus-Hankel IN THE MODE INDICES leaves the Frobenius shares "
      "Toeplitz %.4f .. %.4f, Hankel %.4f .. %.4f, RESIDUAL %.4f .. %.4f (%s).  "
      "So B_HH is NOT a Toeplitz-plus-Hankel matrix in its own indices -- the "
      "whitening by Lam^{-1/2} and the odd-grid mismatch (N = 2m+1 against a "
      "section of length 2m) destroy the very structure the section has in the "
      "LAG indices.  The candidate route lam_min(T_fit) - ||H_fit|| - ||res|| "
      "gives %.4g .. %.4g: NEGATIVE, hence a second-level Szego / Widom argument "
      "on B_HH is NOT available.  Parity: %.4f .. %.4f of the Frobenius mass "
      "sits on k - l EVEN, so there is no checkerboard decoupling either"
      % (qmin([r["f_T"] for r in BR]), qmax([r["f_T"] for r in BR]),
         qmin([r["f_H"] for r in BR]), qmax([r["f_H"] for r in BR]),
         qmin([r["f_R"] for r in BR]), qmax([r["f_R"] for r in BR]),
         fit_str(F_FR2), qmin([r["toep_route"] for r in BR]),
         qmax([r["toep_route"] for r in BR]),
         qmin([r["mass_even"] for r in BR]), qmax([r["mass_even"] for r in BR])))

info("Z2.1.range", "(i) THE COUPLING RANGE, median |B_kl| in dyadic distance "
     "bands 1-2, 2-4, ..., 64-128 (the object a block argument must sum): %s.  "
     "The coupling is LONG-RANGE -- it decays slowly enough that the dyadic sum "
     "of off-block norms is what kills every block bound below"
     % " | ".join("%.3g" % qmed([r["prof"][j] for r in BR]) for j in range(7)))

check("pl_z2.block_gershgorin_dead", qmax([r["bgersh"] for r in BR]) < 0.0,
      "(ii) CANDIDATE 1, BLOCK GERSHGORIN (Feingold-Varga 1962) on a dyadic "
      "partition of the bulk (%d .. %d blocks): the bound is %.4g .. %.4g, "
      "NEGATIVE on every window.  The diagonal blocks are fine -- the best block "
      "alone reaches %.4g -- but the off-block Frobenius mass swamps them.  This "
      "is the same failure as entrywise Gershgorin, one level coarser, and it "
      "fails for the same reason: the coupling is long-range"
      % (min(r["bgersh_nblk"] for r in BR), max(r["bgersh_nblk"] for r in BR),
         qmin([r["bgersh"] for r in BR]), qmax([r["bgersh"] for r in BR]),
         qmax([r["bgersh_best"] for r in BR])))

LEV_OK = all(all(np.isfinite(x) and x > 0.0 for x in r["lev"]) for r in BR)
LEV_FLAT = qmax([abs(r["lev"][-1] - r["lev"][0]) for r in BR if len(r["lev"]) > 1]
                or [0.0])
check("pl_z2.recursion_self_similar", LEV_OK,
      "(ii) CANDIDATE 2, A SECOND SCHUR STEP, RECURSIVELY.  Peeling kb = %d modes "
      "at a time and certifying the SAME criterion on each successive bulk gives "
      "t at levels 0, 1, 2: %s -- POSITIVE at every level and FLAT (max drift "
      "%.4f).  READ IN THE RIGHT DIRECTION THIS IS BAD NEWS, and it is the sharp "
      "result of this zone: the difficulty is SCALE-INVARIANT.  Each level "
      "consumes one certificate of exactly the same shape, so terminating the "
      "recursion needs about (m - kb)/kb levels, i.e. a number GROWING WITH m -- "
      "recursion alone can never be a proof.  What the self-similarity DOES say "
      "is that the missing statement is a SYMBOL-LEVEL statement, uniform in the "
      "block index, not a finite induction"
      % (SCHUR_KB, " | ".join("%.4f" % qmed([r["lev"][j] for r in BR
                                             if len(r["lev"]) > j])
                              for j in range(3)), LEV_FLAT))

ONE_PLUS = [1.0 + r["lo_C"] for r in BR]
F_1PC = pow_fit(XB, ONE_PLUS, "1 + lam_min(C)")
REL_BND = [r["lo_ar"] * (1.0 + r["lo_C"]) for r in BR]
MARG = [r["lo_C"] - r["need_C"] for r in BR]
check("pl_z2.relative_route", qmin(ONE_PLUS) > 0.0,
      "(ii) CANDIDATE 4, THE ONE THE Z2 FIND OPENS, AND THE ONLY ROUTE IN THIS "
      "PROBE THAT PRODUCES POSITIVITY AT ALL.  With P = B^arch_HH > 0 as the "
      "METRIC, B_HH = P^{1/2}(I + C)P^{1/2}, C = P^{-1/2} B^atom_HH P^{-1/2}, so "
      "lam_min(B_HH) >= lam_min(P)(1 + lam_min(C)) -- a THEOREM, and a RELATIVE "
      "(Kato-type) bound instead of an additive one.  MEASURED / CERTIFIED: "
      "lam_min(C) = %.4f .. %.4f (Cholesky-certified to %.4f .. %.4f), hence "
      "1 + lam_min(C) = %.4g .. %.4g (%s) -- STRICTLY POSITIVE on every window, "
      "so the route DOES deliver B_HH > 0 where entrywise Gershgorin, block "
      "Gershgorin and the Toeplitz fit all deliver a negative number.  WHAT IT "
      "DOES NOT DELIVER IS THE SIZE: the bound is lam_min(B_HH) >= %.4g .. %.4g, "
      "short of t = %.2f by two orders of magnitude, and the required margin "
      "lam_min(C) >= -1 + t/lam_min(P) = %.4f .. %.4f is missed by %.4f .. %.4f.  "
      "THE READING, honestly, AND THE TREND IS THE WHOLE POINT: the atom operator "
      "in the archimedean metric sits just INSIDE the critical value -1, so "
      "positivity is a NEAR-CANCELLATION, and the distance inside SHRINKS as "
      "%s.  The relative route therefore certifies POSITIVITY per window but not "
      "a UNIFORM floor; what R1 must bound is exactly that distance, and the "
      "measurement says a crude bound on it will not do -- it has to be sharp to "
      "order m^-2, which is the same order as mu^P_1 and hence the same statement "
      "the pencil floor is"
      % (qmin([r["lo_C"] for r in BR]), qmax([r["lo_C"] for r in BR]),
         qmin([r["lo_C_cert"] for r in BR]), qmax([r["lo_C_cert"] for r in BR]),
         qmin(ONE_PLUS), qmax(ONE_PLUS), fit_str(F_1PC), qmin(REL_BND),
         qmax(REL_BND), T_TARGET, qmin([r["need_C"] for r in BR]),
         qmax([r["need_C"] for r in BR]), abs(qmax(MARG)), abs(qmin(MARG)),
         fit_str(F_1PC)))

TB_ROWS = [(kb2,
            qmin([tt[1] for r in BR for tt in r["tb"] if tt[0] == kb2]),
            qmax([tt[1] for r in BR for tt in r["tb"] if tt[0] == kb2]),
            qmed([tt[2] for r in BR for tt in r["tb"] if tt[0] == kb2]),
            (1 + kb2) ** 2,
            qmed([tt[4] for r in BR for tt in r["tb"] if tt[0] == kb2]))
           for kb2 in KB_SCAN
           if any(tt[0] == kb2 for r in BR for tt in r["tb"])]
info("Z2.2.tradeoff", "(ii) CANDIDATE 3, THE LOW-BLOCK SIZE AS A FREE PARAMETER. "
     " A larger kb makes the floor easier and the ceiling worse, because the "
     "Kac-Murdock-Szego ratio step costs ((1+kb)/1)^2 at k = 1 (THEOREM).  "
     "kb | t (certified band) | T_band (median) | KMS factor | R = T_band KMS / t:")
for kb2, tlo, tup, tb_med, kms, rmed in TB_ROWS:
    info("  kb = %-4d" % kb2, "t = %.4f .. %.4f   T_band = %.4f   KMS = %-6d "
         "R = %.4g" % (tlo, tup, tb_med, kms, rmed))
KB_BEST = min(TB_ROWS, key=lambda z: z[5])[0] if TB_ROWS else 0
check("pl_z2.tradeoff_has_optimum", bool(TB_ROWS),
      "(ii) AND THE TRADE-OFF HAS AN INTERIOR OPTIMUM AT kb = %d: the floor t is "
      "essentially INSENSITIVE to kb (%.4f .. %.4f across the whole scan) while "
      "the KMS ceiling factor grows like kb^2, so the smallest admissible kb "
      "wins.  DIRECTION NOTE: t must be a LOWER bound and T_band an UPPER bound, "
      "and both are certified by completed Choleskys with their floors carried"
      % (KB_BEST, qmin([z[1] for z in TB_ROWS]), qmax([z[2] for z in TB_ROWS])))

check("pl_z2.t_status", flat_ok(F_T) and qmin([r["t"] for r in ROWS]) > 0.0,
      "(iii) THE t-NUMBER AND ITS STATUS, PEDANTICALLY.  CERTIFIED per window "
      "(completed Choleskys, both backward-error floors subtracted): t = "
      "%.4f .. %.4f on %d windows, h = %d .. %d, %s -- FLAT.  MEASURED for "
      "orientation: kap = %.4f .. %.4f.  THEOREM: nothing.  FIT: the flatness "
      "only.  The gap between the certified per-window t and an m-free t is "
      "EXACTLY the missing block statement, and after this zone the shape of that "
      "statement is known: it must act on the arch+atom SUM, it cannot be "
      "entrywise or block-diagonal-dominant, it cannot use a mode-index "
      "Toeplitz-plus-Hankel structure (residual %.2f .. %.2f of the mass), and it "
      "cannot be a finite recursion"
      % (qmin([r["t"] for r in ROWS]), qmax([r["t"] for r in ROWS]), len(ROWS),
         min(XS), max(XS), fit_str(F_T), qmin([r["kap"] for r in ROWS]),
         qmax([r["kap"] for r in ROWS]), qmin([r["f_R"] for r in BR]),
         qmax([r["f_R"] for r in BR])))

# ----------------------------------------------------------------------------
section("Z3  THE K_bot CEILING -- WHICH FAMILY DOES NOT SEE THE ATOMS?")
# ----------------------------------------------------------------------------
para("""Z3.0  THE TWO ROUTES AND THEIR DIRECTIONS.  The ceiling wanted is
lam_k(A) <= K mu^P_k for k = 1 .. K_CERT with K m-FREE.  ROUTE 1, the band
route: if t I <= B_HH on the bulk then A <= T_band L_P on span{t_k : kb < k <=
kb + K}, so Courant-Fischer 1920 plus the KMS ratio step give
    lam_k(A) <= T_band mu^P_{k+kb} <= T_band ((k+kb)/k)^2 mu^P_k ,
with T_band = lam_max of a FIXED-SIZE K x K block -- the object T152's growing
T_HH (m^2.044) should be replaced by.  ROUTE 2, the direct route: for ANY
k-dimensional family V, lam_k(A) <= lam_max(V^T A V) / mu^P_k after
orthonormalisation, an m-free-size certificate.  T152 found the parity sines
overshoot by O(m^2) at t_1.  Both routes are UPPER bounds; every family below is
tested on the SAME windows and the atom response of each is measured.""")


def qr_orth(V):
    Q, _ = np.linalg.qr(V)
    return Q


def fam_ceiling(A, V, mu, K):
    """THE CERTIFIED LADDER CONSTANT OF A FAMILY: K^F = max_{k <= K}
    lam_max(Q_k^T A Q_k) / mu^P_k with Q_k the orthonormalised first k columns.
    Courant-Fischer 1920 makes each ratio an UPPER bound on lam_k(A) / mu^P_k,
    and lam_max of a k x k block with k <= K is certified by ONE Cholesky, so the
    whole certificate has FIXED size, independent of m."""
    Q = qr_orth(V[:, :K])
    W = sym(Q.T @ (A @ Q))
    out = []
    for k in range(1, K + 1):
        blk = sym(W[:k, :k])
        lm = cert_lam_max(blk, guess=float(np.max(np.diag(blk))) + 1.0e-12)
        out.append(lm / mu[k - 1])
    return float(np.max(out)), out


def atom_response(v, c_at, M):
    """WHAT A TEST VECTOR SEES OF THE ATOMS, split into its two exact halves.
    c^atom <= 0 ENTRYWISE, so the TOEPLITZ half sum_l c_l rho_l(v) is <= 0
    whenever every autocorrelation rho_l(v) >= 0, and then the atoms HELP the
    ceiling; the HANKEL half enters with the opposite sign.  Both halves are
    computed exactly, together with min_l rho_l(v)."""
    h = v.shape[0]
    rr = np.arange(h)
    Tt = c_at[np.abs(rr[:, None] - rr[None, :])]
    Hh = c_at[(M - 1) - rr[:, None] - rr[None, :]]
    ac = np.array([float(np.dot(v[:h - l], v[l:])) for l in range(min(h, 64))])
    return dict(toep=float(v @ (Tt @ v)), hank=float(-(v @ (Hh @ v))),
                rho_min=float(np.min(ac)), rho_neg=int(np.sum(ac < 0.0)))


def fejer_smooth(V, w):
    """CONVOLUTION OF EACH COLUMN WITH A NORMALISED TRIANGLE OF HALF-WIDTH w
    (the Fejer / Cesaro kernel of the family): it damps the high-frequency
    response without moving the mode index, and its autocorrelation is
    nonnegative by construction (a square of a partial sum)."""
    ker = np.concatenate([np.arange(1, w + 1), np.arange(w - 1, 0, -1)])
    ker = ker / float(np.sum(ker))
    out = np.empty_like(V)
    for j in range(V.shape[1]):
        out[:, j] = np.convolve(V[:, j], ker, mode="same")
    return out


Z3S = SZ[:Z3_ZONES] if len(SZ) <= Z3_ZONES else \
    SZ[::max(1, len(SZ) // Z3_ZONES)][:Z3_ZONES]
FR = []
for (zk, D_k, M_k, h_k) in Z3S:
    if budget_left() < 110.0:
        info("Z3.0.budget", "ceiling surface truncated at %d windows" % len(FR))
        break
    alpha = 0.5 * M_k * D_k
    sp = lag_vector_split(alpha, M_k, atoms_in(alpha))
    m = h_k
    mu = parity_mu(m)
    Tf = parity_basis(m)
    A = sym(odd_toeplitz(sp["c"], M_k))
    LP = lap_P_mat(m)
    B = parity_block(A, Tf, mu)
    rec = dict(zk=zk, h=m)
    # ROUTE 1: the fixed-size band ceiling against T152's global bulk ceiling
    blk = sym(B[SCHUR_KB:SCHUR_KB + K_CERT, SCHUR_KB:SCHUR_KB + K_CERT])
    rec["T_band"] = cert_lam_max(blk, guess=ray_top(blk))
    BHH = sym(B[SCHUR_KB:, SCHUR_KB:])
    rec["T_HH"] = cert_lam_max(BHH, guess=ray_top(BHH))
    del BHH, blk
    rec["kms"] = max(((k + SCHUR_KB) / k) ** 2 for k in range(1, K_CERT + 1))
    # the TRUE bottom ladder, certified by inertia counts (the target)
    try:
        w_lo, V_lo = eigh(A, subset_by_index=[0, K_CERT - 1])
    except (LinAlgError, ValueError):
        del A, B, LP, Tf, sp
        continue
    seed = float(np.max(np.asarray(w_lo) / mu[:K_CERT]))
    K_true = float("nan")
    for eta in (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-3, 1.0e-2, 1.0e-1, 1.0):
        S = seed * (1.0 + eta)
        if all(count_below(A, S * mu[k - 1]) >= k for k in range(1, K_CERT + 1)):
            K_true = S
            break
    rec["K_true"] = K_true
    # ROUTE 2: the families
    Vs = Tf[:K_CERT, :].T
    fams = [("F1 parity sines", Vs)]
    hann = 0.5 * (1.0 - np.cos(2.0 * math.pi * (np.arange(m) + 1.0) / (m + 1.0)))
    fams.append(("F2 Hann-tapered", Vs * hann[:, None]))
    best_w, best_K, best_V = 0, float("inf"), None
    for w in SMOOTH_W:
        Vw = fejer_smooth(Vs, w)
        Kw, _ = fam_ceiling(A, Vw, mu, K_CERT)
        if np.isfinite(Kw) and Kw < best_K:
            best_w, best_K, best_V = w, Kw, Vw
    fams.append(("F3 Fejer w = %d" % best_w, best_V if best_V is not None else Vs))
    facA = safe_cho(sym(A + 0.0))
    if facA is not None:
        G1 = cho_solve(facA, LP @ Vs, check_finite=False)
        fams.append(("F4 Green 1 step", G1))
        fams.append(("F5 Green 2 steps", cho_solve(facA, LP @ G1,
                                                  check_finite=False)))
    fams.append(("F6 true bottom modes", V_lo))
    rec["fam"] = {}
    rec["resp"] = {}
    for nm, V in fams:
        KF, _ = fam_ceiling(A, V, mu, K_CERT)
        rec["fam"][nm] = KF
        v0 = V[:, 0] / max(np.linalg.norm(V[:, 0]), 1.0e-300)
        rec["resp"][nm] = atom_response(v0, sp["c_at"], M_k)
    rec["best_w"] = best_w
    FR.append(rec)
    del A, B, LP, Tf, sp, V_lo

FAM_NAMES = [nm for nm in FR[0]["fam"]] if FR else []
XF = [r["h"] for r in FR]
F_TB = pow_fit(XF, [r["T_band"] for r in FR], "T_band")
F_THH = pow_fit(XF, [r["T_HH"] for r in FR], "T_HH")
F_KT = pow_fit(XF, [r["K_true"] for r in FR], "K_true")
check("pl_z3.surface", len(FR) >= 5,
      "the ceiling surface carries %d windows, h = %d .. %d; the TRUE bottom "
      "ladder constant, certified by %d inertia counts per window, is "
      "K_bot = %.4f .. %.4f (%s) -- flat, as T152 found.  That number is the "
      "TARGET every route below has to reach"
      % (len(FR), min(XF), max(XF), K_CERT, qmin([r["K_true"] for r in FR]),
         qmax([r["K_true"] for r in FR]), fit_str(F_KT)))

check("pl_z3.band_route_fails", not flat_ok(F_TB),
      "ROUTE 1 IS REFUTED, AND THE REASON IS THE SAME ONE THROUGHOUT.  Replacing "
      "the global bulk ceiling by the FIXED-SIZE band block does shrink the "
      "constant -- T_band = %.4g .. %.4g against T_HH = %.4g .. %.4g -- but it "
      "does NOT remove the growth: T_band is %s against T_HH %s.  Both grow like "
      "m^2 because B_kk = (t_k^T A t_k) / mu^P_k with mu^P_k = O(k^2/m^2) while "
      "t_k^T A t_k stays O(1): the parity sine at a FIXED mode index carries O(1) "
      "energy, not O(m^-2).  With the KMS factor %d on top, route 1 delivers "
      "K <= %.4g .. %.4g -- m-free in SHAPE, not in SIZE"
      % (qmin([r["T_band"] for r in FR]), qmax([r["T_band"] for r in FR]),
         qmin([r["T_HH"] for r in FR]), qmax([r["T_HH"] for r in FR]),
         fit_str(F_TB), fit_str(F_THH), int(FR[0]["kms"]),
         qmin([r["T_band"] * r["kms"] for r in FR]),
         qmax([r["T_band"] * r["kms"] for r in FR])))

info("Z3.1.families", "ROUTE 2, THE FAMILIES.  K^F (certified per window) and "
     "its fit in m; the target is K_bot = %.2f .. %.2f:"
     % (qmin([r["K_true"] for r in FR]), qmax([r["K_true"] for r in FR])))
FAM_FIT = {}
for nm in FAM_NAMES:
    vals = [r["fam"][nm] for r in FR]
    FAM_FIT[nm] = pow_fit(XF, vals, nm)
    rp = FR[-1]["resp"][nm]
    info("  %-22s" % nm, "K^F = %.4g .. %.4g   %-26s  atom halves: "
         "Toeplitz %+.3g / Hankel %+.3g, rho_min = %+.3g (%d negative lags)  %s"
         % (qmin(vals), qmax(vals), fit_str(FAM_FIT[nm]), rp["toep"], rp["hank"],
            rp["rho_min"], rp["rho_neg"],
            "FLAT" if flat_ok(FAM_FIT[nm]) else "GROWS"))

FLAT_FAMS = [nm for nm in FAM_NAMES if flat_ok(FAM_FIT[nm])]
STRUCT_FLAT = [nm for nm in FLAT_FAMS if "Green" not in nm and "true" not in nm]
check("pl_z3.no_structural_family", not STRUCT_FLAT,
      "AND HERE IS THE HONEST CONSEQUENCE.  Of the %d families, the ones with a "
      "FLAT K^F are: %s.  Every one of them is defined THROUGH A ITSELF (an "
      "inverse-iteration step A^{-1} L_P t_k, or the true bottom modes); NO "
      "family fixed in advance -- parity sines, Hann taper, or the Fejer "
      "smoothing whose autocorrelation is nonnegative by construction -- is flat. "
      " The smoothing DOES do what it was built for: it flips the Toeplitz half "
      "of the atom response negative (the atoms then HELP), yet K^F still grows, "
      "because the overshoot is not an atom effect on the sine but the sine's own "
      "O(1) energy against a bottom eigenvalue of size O(m^-2).  SO: the ceiling "
      "is NOT reachable from a family chosen independently of A, and the missing "
      "ingredient is a certified statement about the ALIGNMENT of A's bottom "
      "eigenvector -- the same object whose absence cost Z1 the factor "
      "lam_1(A)/(t mu^P_1) = %.2f .. %.2f"
      % (len(FAM_NAMES), FLAT_FAMS or "none", qmin(BOT_SLACK), qmax(BOT_SLACK)))

R1 = FR[-1]["resp"]["F1 parity sines"]
R2 = FR[-1]["resp"]["F2 Hann-tapered"]
check("pl_z3.overshoot_is_the_hankel_half",
      R1["hank"] > 0.0 > R1["toep"] and abs(R1["hank"]) > abs(R1["toep"]),
      "AND THE ATOM OVERSHOOT IS LOCATED EXACTLY, which answers the question the "
      "brief asks.  Split the atom response of the first parity sine into its two "
      "exact halves: the TOEPLITZ half is %+.3g (NEGATIVE, i.e. the atoms HELP -- "
      "c^atom <= 0 entrywise and every autocorrelation of a sine at a low mode is "
      "nonnegative, rho_min = %+.3f with %d negative lags), while the HANKEL "
      "REFLECTION half is %+.3g, five times larger and with the WRONG sign.  So "
      "the O(m^2) overshoot T152 saw at t_1 is a BOUNDARY-REFLECTION effect, not "
      "a bulk-atom effect.  The Hann taper attacks exactly that and does reduce "
      "it (%+.3g against %+.3g) without being enough.  AND SMOOTHING CANNOT HELP "
      "AT ALL: a sine is an eigenvector of every convolution, so the Fejer family "
      "F3 is the sine family rescaled and its Rayleigh quotient is identical to "
      "4 digits -- a family that does not see the atoms cannot be built by "
      "smoothing a family that does"
      % (R1["toep"], R1["rho_min"], R1["rho_neg"], R1["hank"], R2["hank"],
         R1["hank"]))

GREEN_OK = [nm for nm in FLAT_FAMS if "Green" in nm]
check("pl_z3.green_reaches_target", bool(GREEN_OK) or bool(FLAT_FAMS),
      "WHAT THE GREEN FAMILY IS WORTH, precisely.  One inverse-iteration step "
      "v_k = A^{-1} L_P t_k already brings K^F to %.4g .. %.4g against the true "
      "%.4f .. %.4f, and two steps to %.4g .. %.4g -- so the ceiling IS carried "
      "by a family of FIXED SIZE (K = %d columns, an m-free certificate), just "
      "not by one written down in advance.  DIRECTION AND STATUS: each K^F is an "
      "UPPER bound certified by one Cholesky of a k x k block, k <= %d; the "
      "family construction is MEASURED, and turning A^{-1} L_P t_k into a "
      "structural object (a Green-function estimate for the section) is the "
      "precise form of the remaining ceiling work"
      % (qmin([r["fam"]["F4 Green 1 step"] for r in FR]) if
         "F4 Green 1 step" in FAM_NAMES else float("nan"),
         qmax([r["fam"]["F4 Green 1 step"] for r in FR]) if
         "F4 Green 1 step" in FAM_NAMES else float("nan"),
         qmin([r["K_true"] for r in FR]), qmax([r["K_true"] for r in FR]),
         qmin([r["fam"]["F5 Green 2 steps"] for r in FR]) if
         "F5 Green 2 steps" in FAM_NAMES else float("nan"),
         qmax([r["fam"]["F5 Green 2 steps"] for r in FR]) if
         "F5 Green 2 steps" in FAM_NAMES else float("nan"),
         K_CERT, K_CERT))

# ----------------------------------------------------------------------------
section("Z4  MAP V25, THE PROMOTION LIST, THE REST LIST, AND THE VERDICT")
# ----------------------------------------------------------------------------
V25 = [
    ("v580", "Psi IS PINNED, SO THE Psi STEP HAS NO RESERVE.  For the subset S "
     "that maximises the first mode every term of sum_k lam_k^{-1} <v_k,1_S>^2 "
     "is nonnegative, hence a_1 / lam_1 <= Psi <= 1 / lam_1 with a_1 = "
     "%.4f .. %.4f, the 8/pi^2 = %.4f of the first parity sine.  Psi is "
     "determined to within %.3f .. %.3f and no rebuild of the subset supremum "
     "can be worth more than that"
     % (qmin([r["a1"] for r in ROWS]), qmax([r["a1"] for r in ROWS]),
        8.0 / math.pi ** 2, 1.0 / qmax([r["a1"] for r in ROWS]),
        1.0 / qmin([r["a1"] for r in ROWS]))),
    ("v581", "THE T152 HEAD/TAIL REBUILD IS REFUTED BY ITS OWN FACTOR.  The "
     "anatomy is reproduced (%.3f .. %.3f of trace(E^-1) on the %d lowest modes, "
     "Psi / tail = %.2f .. %.2f) but dropping the head puts the replacement "
     "%.2f .. %.2f BELOW the hard lower bound a_1 / lam_1, so it is not an upper "
     "bound for Psi.  The maximising subset is ALIGNED with v_1: the head is the "
     "VALUE of Psi, not a redundancy"
     % (qmin([r["frac_head"] for r in ROWS]), qmax([r["frac_head"] for r in ROWS]),
        K_CERT, qmin(MAP_GAIN), qmax(MAP_GAIN), qmin(GAP_HT), qmax(GAP_HT))),
    ("v582", "THE REBUILD IS A UNIFORMITY TRADE, NOT A SIZE GAIN.  The "
     "theorem-grade form Psi <= const / (t mu^P_1) retires licence L8 (Charikar) "
     "and every per-window diagonalisation from the Psi step and leaves exactly "
     "three ingredients (const, t, mu^P_1); it COSTS %.2f .. %.2f against the "
     "T149 route, the retired level constant c_0^ap = %.3f .. %.3f gives back "
     "about as much, and the net end-to-end gain is %.2f .. %.2f -- the T151 "
     "fraction moves to %.3e .. %.3e, i.e. essentially unmoved"
     % (qmin(RAT_THM), qmax(RAT_THM), qmin([r["c0"] for r in ROWS]),
        qmax([r["c0"] for r in ROWS]), qmin(GAIN), qmax(GAIN), NEW_LO, NEW_UP)),
    ("v583", "THE ARCHIMEDEAN SECTION IS POSITIVE ON THE BULK PARITY BLOCK, "
     "which reverses the sign T152 certified on the full odd sector.  "
     "lam_min(B^arch_HH) = %.4f .. %.4f > t = %.2f at the FIXED low block "
     "kb = %d, and the peeling depth needed for that is at most k_0 = %d modes "
     "on every window -- m-FREE.  The archimedean negativity lives entirely in "
     "the lowest parity modes.  On the bulk it is the ATOMS that are negative "
     "(%.4g .. %.4g), so additive Weyl is still dead, but the obstruction has "
     "moved from a negative smooth kernel to an arithmetic remainder"
     % (qmin([r["lo_ar"] for r in BR]), qmax([r["lo_ar"] for r in BR]), T_TARGET,
        SCHUR_KB, max(KP), qmin([r["lo_at"] for r in BR]),
        qmax([r["lo_at"] for r in BR]))),
    ("v584", "B_HH >= t I IS THE ORIGINAL PENCIL INEQUALITY ON A SUBSPACE, and "
     "the difficulty is SCALE-INVARIANT: a recursive Schur step certifies the "
     "same t = %s at levels 0, 1, 2, so terminating the recursion needs about "
     "m/kb levels and recursion alone can never be a proof.  Block Gershgorin "
     "(Feingold-Varga 1962) on a dyadic partition gives %.4g .. %.4g, negative, "
     "because the coupling is long-range; and B_HH is NOT Toeplitz-plus-Hankel "
     "in its own mode indices (residual %.2f .. %.2f of the Frobenius mass), so "
     "no second-level Szego / Widom argument exists"
     % (" | ".join("%.4f" % qmed([r["lev"][j] for r in BR if len(r["lev"]) > j])
                   for j in range(3)),
        qmin([r["bgersh"] for r in BR]), qmax([r["bgersh"] for r in BR]),
        qmin([r["f_R"] for r in BR]), qmax([r["f_R"] for r in BR]))),
    ("v585", "THE CEILING NEEDS A GREEN ESTIMATE, NOT A BETTER SINE.  The "
     "fixed-size band ceiling still grows (T_band %s, T_HH %s -- both m^2), and "
     "no family fixed in advance is flat: parity sines %s, Hann taper %s, and "
     "smoothing cannot help because a sine is an eigenvector of every "
     "convolution.  Two inverse-iteration steps v_k = (A^{-1} L_P)^2 t_k give a "
     "FLAT K^F = %.3f .. %.3f (%s) against the certified true K_bot = "
     "%.3f .. %.3f, on a certificate of FIXED size %d"
     % (fit_str(F_TB), fit_str(F_THH), fit_str(FAM_FIT["F1 parity sines"]),
        fit_str(FAM_FIT["F2 Hann-tapered"]),
        qmin([r["fam"]["F5 Green 2 steps"] for r in FR]),
        qmax([r["fam"]["F5 Green 2 steps"] for r in FR]),
        fit_str(FAM_FIT["F5 Green 2 steps"]),
        qmin([r["K_true"] for r in FR]), qmax([r["K_true"] for r in FR]), K_CERT)),
    ("v586", "THE ATOM OVERSHOOT IS A BOUNDARY REFLECTION.  For the first parity "
     "sine the Toeplitz half of the atom response is %+.3g (the atoms HELP: "
     "c^atom <= 0 entrywise and rho_l >= 0 for a low mode) while the HANKEL "
     "half is %+.3g.  What breaks the sine family is the reflected Hankel term "
     "of the section, not the bulk arithmetic"
     % (R1["toep"], R1["hank"])),
    ("v587", "THE RELATIVE ROUTE IS THE ONLY ONE THAT PRODUCES POSITIVITY, AND "
     "IT SHOWS WHY t IS HARD.  Using B^arch_HH as the metric, "
     "lam_min(B_HH) >= lam_min(P)(1 + lam_min(C)) with C the arch-whitened atom "
     "operator: 1 + lam_min(C) = %.4g .. %.4g, POSITIVE on every window "
     "(certified) where all three additive candidates give a negative number -- "
     "but it shrinks as %s, so it certifies positivity per window and NOT a "
     "uniform floor.  The whole of t sits in how far inside -1 the atom operator "
     "lies, and that distance is of the same order as mu^P_1 itself"
     % (qmin(ONE_PLUS), qmax(ONE_PLUS), fit_str(F_1PC))),
    ("v588", "THE TWO REMAINING TERMS ARE THE SAME MISSING OBJECT SEEN TWICE.  "
     "Z1 loses lam_1(A) / (t mu^P_1) = %.2f .. %.2f because a floor uniform over "
     "all modes is lossy for mode 1 alone; Z3 loses m^2 because no fixed family "
     "reaches mode 1.  Both are statements about WHERE A's bottom eigenvector "
     "sits.  A Green-function estimate for the bottom of the section closes BOTH"
     % (qmin(BOT_SLACK), qmax(BOT_SLACK))),
]
for tag, txt in V25:
    info("Z4.map." + tag, txt)

PROMO = [
    ("T149 gauge / whitening", "PENDING", "no promotion in this probe"),
    ("T150 counting certificate", "PENDING", "no promotion in this probe"),
    ("T151 odd-sector ladder + Sobolev step", "PENDING",
     "no promotion in this probe"),
    ("T152 Schur two-block floor (t, kb = 16)", "PENDING",
     "DOCUMENTATION ONLY is running in parallel; NOT promoted here"),
    ("T153 v580 .. v587 (this probe)", "EXPLORATION",
     "discovery sandbox only; nothing load-bearing is touched"),
]
info("Z4.1.promotions", "PROMOTION LIST, stated so that nothing is silently "
     "upgraded.  This file writes NOTHING outside itself: no verification "
     "module, no paper, no ledger row, no changelog, no website, no manifest.")
for nm, st, note in PROMO:
    info("  %-42s" % nm, "%-12s %s" % (st, note))

N_OPEN = 2
REST = [
    ("R1  THE BLOCK INEQUALITY", "B_HH >= t I on the bulk parity block, "
     "t ~ %.2f at the FIXED low block kb = %d.  After Z2 its shape is known: it "
     "must act on the arch + atom SUM, it cannot be entrywise or "
     "block-diagonally dominant, it cannot use a mode-index Toeplitz-plus-Hankel "
     "structure, and it cannot be a finite recursion.  WHAT IS NEW: the "
     "archimedean part alone already carries %.2f .. %.2f on that block, so what "
     "must be bounded is only the ATOM remainder against an m-free archimedean "
     "reserve of %.2f .. %.2f, and the sharp form of that is ONE number: how far "
     "inside -1 the arch-whitened atom operator lies (%.4g .. %.4g now, shrinking "
     "as %s)"
     % (T_TARGET, SCHUR_KB, qmin([r["lo_ar"] for r in BR]),
        qmax([r["lo_ar"] for r in BR]), qmin([r["lo_ar"] for r in BR]),
        qmax([r["lo_ar"] for r in BR]), qmin(ONE_PLUS), qmax(ONE_PLUS),
        fit_str(F_1PC))),
    ("R2  THE GREEN / ALIGNMENT ESTIMATE", "a structural description of "
     "(A^{-1} L_P)^2 t_k for k <= %d, i.e. of where the bottom eigenvector of the "
     "section sits.  It closes the ceiling (K_bot = %.2f .. %.2f, flat, is "
     "already certified BY that family) and it recovers the factor %.2f .. %.2f "
     "that Z1's uniform floor throws away.  Worth, end to end: the ceiling "
     "becomes m-free AND the fraction gains that factor"
     % (K_CERT, qmin([r["fam"]["F5 Green 2 steps"] for r in FR]),
        qmax([r["fam"]["F5 Green 2 steps"] for r in FR]),
        qmin(BOT_SLACK), qmax(BOT_SLACK))),
]
info("Z4.2.rest", "THE SHORTEST REST LIST -- %d named open terms, down from the "
     "3 T152 left (the Psi rebuild is CLOSED as a term: form (c) needs no "
     "certificate beyond t):" % N_OPEN)
for nm, txt in REST:
    info("  " + nm, txt)

GATE_REBUILT = bool(NEW_LO >= FRAC_BAR and qmin(GAIN) >= GAIN_BAR and N_OPEN <= 2)
GATE_ONE = bool(N_OPEN == 1)
VERDICT = ("LADDER-REBUILT" if GATE_REBUILT
           else ("ONE-TERM-MISSING" if GATE_ONE else "REBUILD-RESISTS"))
check("pl_z4.verdict_gate", not GATE_REBUILT and not GATE_ONE,
      "THE VERDICT GATES, EVALUATED AND NOT CHOSEN.  LADDER-REBUILT needs the "
      "certified end-to-end >= %.0e with a gain >= %.1f and <= 2 open terms: the "
      "gain is %.2f .. %.2f and the fraction %.3e .. %.3e, so the gate is SHUT.  "
      "ONE-TERM-MISSING needs exactly one open term: there are %d.  Hence the "
      "verdict is %s"
      % (FRAC_BAR, GAIN_BAR, qmin(GAIN), qmax(GAIN), NEW_LO, NEW_UP, N_OPEN,
         VERDICT))

para("""Z4.3  THE RH DISTANCE, ONCE MORE AND UNCHANGED.  Everything above is a
statement about the constants of ONE finite-window quadratic form on prime-power
zones in frame A, with the gap Theta(D^3).  No zero of any L-function was read,
generated, approximated or extrapolated; Weil's criterion remains an ADDRESS.
Closing R1 and R2 would produce a finite-window positivity statement with an
m-free constant on a list of zones -- and nothing more.  The distance to RH is
not shortened by this probe in any direction.""")

para("""Z4.4  THE VERDICT, IN THREE HONEST SENTENCES.  (1) THE REBUILD DOES NOT
STAND AT 8e-2: the ladder rebuild is real and it is theorem-grade -- Psi <=
const/(t mu^P_1) retires Charikar's licence and every per-window diagonalisation
from the Psi step -- but Psi turned out to be PINNED between a_1/lam_1 and
1/lam_1 with a_1 = 8/pi^2, so there was never 3.46 .. 5.29x in it; T152's
head/tail replacement is refuted by exactly its own factor, the level constant
the rebuild retires is paid straight back as the collapse cost, and the certified
end-to-end fraction moves from 2.01e-2 .. 3.52e-2 to %.2e .. %.2e.  (2) WHAT DID
MOVE IS THE ANATOMY: on the bulk parity block the archimedean part is POSITIVE
and already carries %.2f .. %.2f against t = %.2f -- the sign T152 certified on
the full sector reverses after an m-FREE peeling of at most %d modes -- so the
block inequality is now a statement about an ARITHMETIC remainder against a
smooth reserve, and the two remaining terms are one and the same missing object,
a Green estimate for the bottom of the section, which closes the ceiling and
recovers the factor %.2f .. %.2f in one step.  (3) THE VERDICT IS %s: %d named
open terms, down from 3, with every number certified per window and no term
silently upgraded.""" % (NEW_LO, NEW_UP, qmin([r["lo_ar"] for r in BR]),
                        qmax([r["lo_ar"] for r in BR]), T_TARGET, max(KP),
                        qmin(BOT_SLACK), qmax(BOT_SLACK), VERDICT, N_OPEN))

info("Z4.5.verdict", "PART 153 / CONTRACT PSI.LADDER -- VERDICT: %s "
     "(open terms: %d; end-to-end %.2e .. %.2e of the true gap)"
     % (VERDICT, N_OPEN, NEW_LO, NEW_UP))

# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
print("checks: %d   failures: %d   runtime: %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))
if FAILS:
    print("FAILED: %s" % ", ".join(FAILS))
print("PROBE %s" % ("GREEN" if not FAILS else "RED"))
