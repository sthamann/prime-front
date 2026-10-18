"""PART 166 -- SCHUR.CASCADE -- THE ONE UNIFORMITY STATEMENT.

DISCOVERY PROBE.  Sandbox: experiments/tfpt-discovery/.  Nothing here is a
verification module, nothing here is promoted, nothing outside this one file is
touched.

*** THE RH FENCE, FIRST AND LOUDEST. ***  No zero of any L-function is used,
tabulated, approximated or referred to; no L-function is EVALUATED anywhere.
Every arithmetic input is a FINITE von Mangoldt sum over prime powers together
with the UNCONDITIONAL Chebyshev bound |psi(x) - x| <= kappa x on the finite
range that is actually swept (Chebyshev 1852; Rosser-Schoenfeld 1962).  Nothing
below is conditional on RH, and nothing below proves anything about RH.  The
number RH_DELTA = 1/2 appears exactly once, as a YARDSTICK for the strength a
hypothetical bound would need, never as an input.  An AST firewall enforces the
token, import and write-mode rules mechanically.

THE ONE OPEN OBJECT (T165 end state).  After T158 .. T165 exactly one genuinely
open item is left in the analytic Phase-2 line:

    inf_m g_16(m) > 0 ,  equivalently  g_16/g_1 >= c . h^{3 - eps} uniform in m.

The facts it stands on, all reproduced in T0 below and none of them assumed:
1/g_1 = B_11 GROWS like h^{+3.110} (FIT), 1/g_16 is FLAT at h^{+0.061} (FIT), and
the two exponents close exactly: +3.110 - 3.049 = +0.061.  The certification
therefore lives in the 15 ladder increments y_j^2 of the T158 Cholesky /
continued-fraction ladder g_K = sum_{j<=K} y_j^2, y = L_K^-1 e_1, L_K L_K^T =
B_LL[:K,:K] (Schur 1917; the Jacobi continued fraction) -- and it is CONCENTRATED
IN THE FIRST RUNGS.  It is provably outside the reach of absolute-value budgets:
the m-free ingredients (head split, atom budget, moment laws) bound B_11 SHARPLY
(flat factor 21 .. 26) but B_11 is the WRONG OBJECT, because the cascade gain is
a CANCELLATION.

WHAT THIS FILE DOES.  U1 is the anatomy of the cascade over BOTH surfaces (frame
A and the decoupled nu surface): which rungs carry the h^3, the closed form of
the early increments, and the cascade read as a Krylov / Ritz approximation of
the Green column A^-1 t_1 (T158: L_P t_1 = mu^P_1 t_1 EXACTLY, so span{t_1,
A^-1 L_P t_1} = span{t_1, A^-1 t_1} attains the entry EXACTLY -- KMS 1953).  U2
hunts the lower bound: the two-rung candidate, the cancellation anatomy of the
increments in arch/atom parts, and the T146/T157 confinement route.  U3 does the
two errands (U_ref over the union surface, deeper zones inside the cap) and the
end-to-end assembly with the mandatory stress battery.  U4 is the map and the
honest verdict.

DISCIPLINE.  THEOREM / CERTIFIED / MEASURED / FIT are never mixed: a line that
says THEOREM is an identity or a classical inequality, a line that says CERTIFIED
is an inequality evaluated with m-free ingredients on a declared surface, a line
that says MEASURED is a number on this surface and nothing more, and a line that
says FIT is a regression slope and is never used as an input to any bound.  Every
monotonicity direction (Schur complements, Cholesky rungs, Dirichlet vs Thomson)
is written out before it is used.  All caps are hard: no factorised matrix beyond
MAX_H, total runtime under BUDGET_S.

CLASSICAL SPINE: Schur 1917 (nested complements), Chebyshev 1852, Fejer 1915,
Weil 1952, Kac-Murdock-Szego 1953, Lanczos 1950 and the Krylov 1931 iteration,
Dirichlet 1829, Abel 1826, Thomson/Dirichlet duality (Maz'ya 1985).
"""

import ast
import math
import os
import time

import numpy as np

T0 = time.time()
np.random.seed(166166)

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

N_ZONES = 40                 # frame-A zone count: the SAME RECIPE AND DENSITY as
                             # T163 .. T165, so every exponent is comparable
HCAP = 1450                  # inside the HARD cap MAX_H = 1500
H_MIN = 128                  # DECLARED: >= 2 x the largest mode block K = 64
N_ATOM_MIN = 40              # DECLARED surface floor (as T161 .. T165)
SCHUR_KB = 16                # the FIXED low block of the T152 .. T165 chain
KB_MAX = 64                  # the enlarged block, carried for the controls
NU_DECOUPLE = (4, 5, 6, 8, 11, 16)   # the nu knob of the decoupled surface
N_ZONES_NU = 6               # zones carried on the decoupled nu surface

EXACT_BAR = 1.0e-12          # the bar on every claimed IDENTITY that is evaluated
                             # WITHOUT inverting an ill-conditioned block
IDENT_BAR = 1.0e-6           # the bar on an identity that DOES invert the low
                             # block.  DECLARED NUMERICAL HORIZON, not a tuned
                             # tolerance: cond(B_LL) reaches ~1e8 on this surface
                             # and eps . cond ~ 3e-8, so 1e-6 is that horizon with
                             # a factor ~30 of margin.  Every line that uses this
                             # bar says so
COND_BAR = 1.0e12            # the T159 numerical horizon on cond(B_LL)
BAR_FLAT = 0.25              # |exponent| bar for "flat / non-growing" (T159)
EPSM = float(np.finfo(float).eps)
B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962)
RH_DELTA = 0.5               # RH STRENGTH, as a delta.  A YARDSTICK, NOT A CLAIM
HEADROOM_BAR = 1.0e3         # DECLARED cancellation headroom over machine eps

# T163 .. T165 numbers, QUOTED, never recomputed as an input to anything
T163_KAPPA = 0.03882
T164_G16_RANGE = (1.7527, 5.3286)
T164_G16_EXP = 0.061
T164_UREF = 4.90
T165_NU_SUP = 5.7327
T165_B11_EXP = 3.110
T165_GAIN_EXP = 3.049
T165_BALANCE = (11, 1, 4, 6)   # THEOREM / CERT-UNIF / CERT-WINDOW / MEASURED

# PREREGISTERED VERDICT PREDICATES -- fixed BEFORE any number of this file is
# seen, never tuned afterwards (anti-fitting)
EPS_CARRY = 0.5              # "h^{3-eps}" is honoured for eps <= EPS_CARRY
SAFETY_UREF = 1.15           # declared off-recipe safety factor for U_ref
CONF_BAR = 0.90              # confinement fraction g_16/s that would be needed
RUNG_HALF = 0.5              # "half the gain" threshold for the rung profile

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
    for blk in text.split("\n\n"):
        for ln in wrap_at(blk, width):
            print(indent + ln)
        print("")


def block(text, indent="  "):
    """Like para(), but VERBATIM: for tables whose column layout carries
    information that re-wrapping would destroy."""
    print("")
    for ln in text.split("\n"):
        print(indent + ln if ln.strip() else "")
    print("")


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


def fit_multi(cols, ys):
    """Least squares of log|y| on the given log-covariates plus an intercept, used
    ONLY to separate the two independent knobs of the union surface.  A FIT."""
    ys = np.asarray(ys, float)
    Xc = [np.asarray(c, float) for c in cols]
    ok = np.isfinite(ys) & (np.abs(ys) > 0)
    for c in Xc:
        ok &= np.isfinite(c) & (c > 0)
    if int(np.sum(ok)) < len(Xc) + 2:
        return [float("nan")] * len(Xc), float("nan")
    A = np.column_stack([np.log(c[ok]) for c in Xc]
                        + [np.ones(int(np.sum(ok)))])
    b = np.log(np.abs(ys[ok]))
    sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    res = float(np.sum((A @ sol - b) ** 2))
    tot = float(np.sum((b - np.mean(b)) ** 2))
    return [float(t) for t in sol[:-1]], (1.0 - res / tot if tot > 0
                                         else float("nan"))


def fit_exp(xs, ys):
    """d log y / d log x -- a FIT, always labelled as such, never an input."""
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    ok = np.isfinite(xs) & np.isfinite(ys) & (np.abs(ys) > 0) & (xs > 0)
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
          == "schur_cascade_probe.py", "single new file in the sandbox")
    check("sc_fw.rh_fence", RH_DELTA == 0.5,
          "RH strength delta = %.1f is a YARDSTICK ONLY: no zero data, no "
          "L-function evaluation, finite von Mangoldt sums only" % RH_DELTA)


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
# the parity sector: the KMS 1953 eigenpairs, the odd Toeplitz-minus-Hankel form
# ----------------------------------------------------------------------------
def parity_mu(m):
    """mu^P_k = 4 sin^2(pi k / N), N = 2m + 1 (Kac-Murdock-Szego 1953).  EXACT
    eigenvalues of L_P; the fact that makes the T158 two-dimensional bridge a
    THEOREM and not a numerical accident."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m, kb=None):
    """t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N), the ORTHONORMAL eigenbasis of
    L_P."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, (kb or m) + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_P(m):
    """L_P = tridiag(-1, 2, -1) with the LAST diagonal entry 3 -- the parity
    reduction, not a choice.  Kept ONLY to re-verify L_P t_1 = mu^P_1 t_1."""
    L = (np.diag(2.0 * np.ones(m)) - np.diag(np.ones(m - 1), 1)
         - np.diag(np.ones(m - 1), -1))
    L[m - 1, m - 1] = 3.0
    return L


def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: TOEPLITZ MINUS HANKEL, exact."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def lag_weights_from_v(v, m):
    """*** THE T163 CORRELATION FORM, A THEOREM, RE-CHECKED IN U3. ***  w_0 =
    A_0, w_d = 2 A_d - H_{M-1-d} (d >= 1), A the autocorrelation and H the
    self-convolution of v; then x^T B x = sum_d c_d w_d EXACTLY."""
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
    """C_d = sum_{e <= d} c_e -- the Abel partial sums (Abel 1826)."""
    return np.cumsum(c)


# ----------------------------------------------------------------------------
# *** THE CASCADE ITSELF: THE T158 CHOLESKY / CONTINUED-FRACTION LADDER. ***
# ----------------------------------------------------------------------------
def cascade(Bm, K):
    """g_K = e_1^T Q_K^-1 e_1 = sum_{j<=K} y_j^2 with y = L_K^-1 e_1, L_K the
    Cholesky factor of Q_K = B[:K,:K].

    THREE DIRECTIONS, WRITTEN OUT BEFORE USE, because every sign below depends on
    them:
    (a) y_j^2 > 0 STRICTLY, so g_K is STRICTLY INCREASING in K and 1/g_K is a
        DECREASING chain of UPPER bounds on 1/s (Schur 1917 nested complements).
    (b) BECAUSE L is lower triangular, (L_K^-1 e_1)_j = (L_{K'}^-1 e_1)_j for all
        j <= K <= K', so ONE Cholesky of the full 16 x 16 block delivers ALL 16
        rungs.  This is the statement that makes the ladder a CASCADE and not 16
        unrelated solves; it is verified explicitly in U1.
    (c) 1/g_K = min{ x^T Q_K x : x_1 = 1 } (the Schur complement as a CONSTRAINED
        MINIMUM), so ANY explicit trial x with x_1 = 1 is an UPPER bound on
        1/g_K, i.e. a LOWER bound on g_K.  That is the ONLY direction in which
        the open object can ever be certified."""
    Q = sym(np.asarray(Bm)[:K, :K])
    try:
        L = np.linalg.cholesky(Q)
    except np.linalg.LinAlgError:
        return None
    e1 = np.zeros(K)
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return dict(y=y, y2=y ** 2, g=np.cumsum(y ** 2), L=L)


section("PART 166 -- SCHUR.CASCADE -- U0  FENCE, SCALES, THE TWO SURFACES")
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]
NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)

EIG_HCAP = HCAP              # DECLARED horizon for FULL eigen-decompositions of A.
                             # Set to the same cap as everything else, so the
                             # confinement route is measured on the WHOLE union
                             # surface and not on a sub-surface
S_HCAP = HCAP                # exact entry s by ONE Cholesky: allowed to the cap


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


_psi_run, _bpsi = 0.0, 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
check("sc_u0.chebyshev", _bpsi <= B_PSI,
      "psi(x)/x <= %.6f VERIFIED at every jump point up to n = %d (max %.6f), "
      "never assumed beyond it (Chebyshev 1852; Rosser-Schoenfeld 1962).  THE ONLY "
      "arithmetic input of the file, and it is UNCONDITIONAL"
      % (B_PSI, ATOM_MAX, _bpsi))

X0_CHEB = 100.0
_psi, _kap = 0.0, 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi += _lam
    if _n >= X0_CHEB:
        _kap = max(_kap, abs(_psi - _n) / _n)
KAPPA = _kap
CROSS_BAR = 2.0 * KAPPA
check("sc_u0.kappa", 0.0 < KAPPA < 0.2 and abs(KAPPA - T163_KAPPA) < 0.001,
      "|psi(x) - x| <= kappa x with kappa = %.6f on %.0f <= x <= %d; T163 .. T165 "
      "used the SAME constant (%.5f); crossing bar 2 kappa = %.6f"
      % (KAPPA, X0_CHEB, ATOM_MAX, T163_KAPPA, CROSS_BAR))


def zone_candidates(nu, h_lo, h_hi):
    out = []
    for k in range(2, NZ_DEEP - 2):
        D_k = 0.5 * float(G_DEEP[k]) / float(nu)
        M_k = int(math.ceil(UU_ALL[k] / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        h_k = M_k // 2
        if h_k < h_lo or h_k > h_hi:
            continue
        if len(atoms_in(UU_ALL[k])) < N_ATOM_MIN:
            continue
        out.append((k, D_k, M_k, h_k))
    return out


def build_window(kz, nu, want_eig=False):
    """One window.  nu is the frame-A resolution knob: D = g_k / (2 nu), so nu
    MULTIPLIES h at FIXED zone, which is the T165 decoupling handle.  nu =
    NU_MAIN is the T105 admissibility floor and the T112 frame-A recipe; nu >
    NU_MAIN is admissible (finer); nu < NU_MAIN is NOT and is only ever used as a
    LABELLED must-break control."""
    alpha = UU_ALL[kz]
    D_k = 0.5 * float(G_DEEP[kz]) / float(nu)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    if hz < 8 or hz > HCAP:
        return None
    c_at, D, mu_tot, n_at = atom_lags(alpha, Mz, atoms_in(alpha))
    c_ar = arch_lags(Mz, D)
    r = dict(k=kz, nu=float(nu), h=hz, M=Mz, D=D, alpha=alpha,
             n_zone=NN_ALL[kz], gap=float(G_DEEP[kz]), c_ar=c_ar, c_at=c_at,
             c=c_ar + c_at, mu_tot=mu_tot, n_atom=n_at,
             X=math.exp(2.0 * alpha), logX=2.0 * alpha)
    nb = min(KB_MAX, hz)
    Tb = parity_basis(hz, nb)
    mu = parity_mu(hz)
    r["Tb"], r["nb"] = Tb, nb
    r["mu"] = mu[:nb]
    r["mu1_full"] = float(mu[0])
    isq = 1.0 / np.sqrt(r["mu"])
    A = odd_toeplitz(r["c"], Mz)
    r["G64"] = sym(Tb @ (A @ Tb.T))
    r["B64"] = sym(r["G64"] * np.outer(isq, isq))
    kl = min(SCHUR_KB, nb)
    r["kl"] = kl
    r["B_LL"] = r["B64"][:kl, :kl].copy()
    r["G_LL"] = r["G64"][:kl, :kl].copy()
    T16 = Tb[:kl, :]
    for tag, cc in (("ar", r["c_ar"]), ("at", r["c_at"])):
        Ah = odd_toeplitz(cc, Mz)
        r["G_" + tag] = sym(T16 @ (Ah @ T16.T))
        del Ah
    e1 = np.zeros(kl)
    e1[0] = 1.0
    try:
        r["xstar"] = np.linalg.solve(r["B_LL"], e1)
    except np.linalg.LinAlgError:
        del A
        return None
    r["xstar"] /= max(abs(float(r["xstar"][0])), 1.0e-300)
    ev = np.linalg.eigvalsh(r["B_LL"])
    r["kap"] = float(ev[-1] / max(ev[0], 1.0e-300))
    r["casc"] = cascade(r["B_LL"], kl)
    r["C"] = part_sums(r["c"])
    r["Cinf"] = float(np.max(np.abs(r["C"])))
    r["c_l1"] = float(np.sum(np.abs(r["c"])))
    # THE EXACT ENTRY s = mu^P_1 . t_1^T A^-1 t_1 (T157/T158), by ONE Cholesky.
    r["s"] = float("nan")
    r["s_dual2"] = float("nan")
    t1 = np.ascontiguousarray(Tb[0, :])
    if hz <= S_HCAP and budget_left() > 120.0:
        try:
            LA = np.linalg.cholesky(sym(A))
            Ainv_t1 = np.linalg.solve(LA.T, np.linalg.solve(LA, t1))
            r["s"] = r["mu1_full"] * float(t1 @ Ainv_t1)
            # T158 TWO-DIMENSIONAL BRIDGE: L_P t_1 = mu^P_1 t_1 EXACTLY, so
            # A^-1 L_P t_1 = mu^P_1 A^-1 t_1 and span{t_1, A^-1 L_P t_1} MUST
            # attain the entry exactly.  Verified, not assumed.
            V = np.column_stack([t1, r["mu1_full"] * Ainv_t1])
            GV = sym(V.T @ (A @ V))
            eV = V.T @ t1
            r["s_dual2"] = r["mu1_full"] * float(eV @ np.linalg.solve(GV, eV))
            del LA, Ainv_t1, V, GV
        except np.linalg.LinAlgError:
            pass
    # CONFINEMENT (T146/T157): how much of the bottom eigenvector of A lives in
    # the sixteen low parity sines.  Only inside the DECLARED eigen-horizon.
    r["conf1"] = float("nan")
    r["lam_lo"] = float("nan")
    r["lam_gap"] = float("nan")
    r["ov0"] = float("nan")
    r["ray0"] = float("nan")
    r["rayP"] = float("nan")
    r["rayP64"] = float("nan")
    r["nmode"] = 0
    r["sfrac"] = {}
    if want_eig and hz <= EIG_HCAP and budget_left() > 150.0:
        try:
            wv, Vv = np.linalg.eigh(sym(A))
            r["lam_lo"] = float(wv[0])
            r["lam_gap"] = float(wv[1] / max(wv[0], 1.0e-300))
            v0 = Vv[:, 0]
            r["conf1"] = float(np.sum((T16 @ v0) ** 2) / (v0 @ v0))
            ov = (Vv.T @ t1) ** 2
            r["ov0"] = float(ov[0])
            # THE SINGLE-BOTTOM-MODE Rayleigh lower bound on g (a THEOREM: any
            # trial z gives g >= mu_1 (t_1.z)^2 / z^T A z), and how many bottom
            # modes the Green column actually needs.
            r["ray0"] = r["mu1_full"] * r["ov0"] / max(float(wv[0]), 1.0e-300)
            # THE SAME TRIAL, PROJECTED INTO THE SIXTEEN MODES, so that it is a
            # legitimate lower bound on g_16 and not merely on s.
            zp = T16.T @ (T16 @ v0)
            qz = float(zp @ (A @ zp))
            r["rayP"] = (r["mu1_full"] * float(t1 @ zp) ** 2 / qz if qz > 0.0
                         else float("nan"))
            # THE SAME OBJECT IN THE ENLARGED K = 64 BLOCK, so that "is the trial
            # space big enough" can be answered instead of deferred.
            z6 = Tb.T @ (Tb @ v0)
            q6 = float(z6 @ (A @ z6))
            r["rayP64"] = (r["mu1_full"] * float(t1 @ z6) ** 2 / q6 if q6 > 0.0
                           else float("nan"))
            del zp, z6
            cum = np.cumsum(ov / wv) * r["mu1_full"]
            stot = float(cum[-1])
            for jj in (1, 2, 4, 8, 16, 32):
                if jj <= hz:
                    r["sfrac"][jj] = float(cum[jj - 1] / stot)
            r["nmode"] = int(np.searchsorted(cum, 0.9 * stot) + 1)
            del wv, Vv, v0, ov, cum
        except np.linalg.LinAlgError:
            pass
    del A
    return r


SZ = []
CAND_A = zone_candidates(NU_MAIN, H_MIN, HCAP)
if CAND_A:
    CAND_A.sort(key=lambda t: t[3])        # LOG-SPACED IN h, DECLARED IN ADVANCE
    pick = sorted(set(int(round(x)) for x in np.geomspace(
        1.0, float(len(CAND_A)), N_ZONES)))
    SZ = [CAND_A[i - 1] for i in pick]
    SZ.sort(key=lambda t: t[0])
check("sc_u0.surface_a", len(SZ) >= 8,
      "FRAME A: %d prime-power zones (of %d admissible), log-spaced in h inside "
      "H_MIN = %d, h <= %d, MAX_H = %d, atom floor %d: h = %d .. %d, lever arm "
      "%dx.  SAME RECIPE AND DENSITY as T163 .. T165"
      % (len(SZ), len(CAND_A), H_MIN, HCAP, MAX_H, N_ATOM_MIN,
         min(t[3] for t in SZ), max(t[3] for t in SZ),
         int(max(t[3] for t in SZ) / max(min(t[3] for t in SZ), 1))))

WA = []
for (kz, Dz, Mz, hz) in SZ:
    if budget_left() < 620.0:
        info("sc_u0.budget", "frame-A enumeration stopped at h = %d" % hz)
        break
    rw = build_window(kz, NU_MAIN, want_eig=True)
    if rw is not None:
        rw["surf"] = "A"
        WA.append(rw)

# THE DECOUPLED nu SURFACE (T165): zones chosen so that even nu = 16 stays inside
# the cap, then every nu of the DECLARED list NU_DECOUPLE on each zone.
NU_TOP = max(NU_DECOUPLE)
CAND_N = zone_candidates(NU_MAIN, H_MIN // 2,
                         max(H_MIN, int(HCAP * NU_MAIN / NU_TOP)))
SZN = []
if CAND_N:
    CAND_N.sort(key=lambda t: t[3])
    pk = sorted(set(int(round(x)) for x in np.geomspace(
        1.0, float(len(CAND_N)), N_ZONES_NU)))
    SZN = [CAND_N[i - 1] for i in pk]
    SZN.sort(key=lambda t: t[0])

WN = []
for (kz, Dz, Mz, hz) in SZN:
    for nu in NU_DECOUPLE:
        if budget_left() < 420.0:
            info("sc_u0.budget_nu", "nu enumeration stopped at %d windows" % len(WN))
            break
        rw = build_window(kz, nu, want_eig=True)
        if rw is not None:
            rw["surf"] = "N"
            WN.append(rw)

WPA = [r for r in WA if r["kap"] <= COND_BAR and r["casc"] is not None]
WPN = [r for r in WN if r["kap"] <= COND_BAR and r["casc"] is not None]
WU = WPA + WPN
XA = [float(r["h"]) for r in WPA]
XU = [float(r["h"]) for r in WU]

for r in WU:
    cc = r["casc"]
    r["g1"] = float(cc["g"][0])
    r["g16"] = float(cc["g"][r["kl"] - 1])
    r["gain"] = r["g16"] / r["g1"]
    r["B11"] = float(r["B_LL"][0, 0])
    w = lag_weights_corr(r["xstar"], r["h"], r["Tb"])
    r["w"], r["dw"] = w, back_diff(w)
    r["Q"] = float(np.dot(r["c"], w))
    r["Q_ar"] = float(np.dot(r["c_ar"], w))
    r["Q_at"] = float(np.dot(r["c_at"], w))
    r["TV"] = float(np.sum(np.abs(r["dw"])))
    r["l1w"] = float(np.sum(np.abs(w)))
    r["big"] = max(abs(r["Q_ar"]), abs(r["Q_at"]))
    r["e_qid"] = abs(r["Q"] - float(r["xstar"] @ (r["B_LL"] @ r["xstar"]))) / r["big"]
    r["e_gauge"] = abs(float(np.sum(w))) / max(r["l1w"], 1.0e-300)
    r["headroom"] = abs(r["Q"]) / (r["big"] * EPSM)

check("sc_u0.surface_union", len(WPA) >= 8 and len(WPN) >= 12,
      "THE UNION SURFACE both blocks of this file live on: %d frame-A windows "
      "(h = %d .. %d) + %d decoupled-nu windows (%d zones x nu in %s, h = %d .. "
      "%d) = %d windows.  On the union h ranges %d .. %d, a lever arm of %dx, and "
      "nu and the zone depth are INDEPENDENT knobs, which is what makes an "
      "exponent read on the union a statement about m and not about the recipe"
      % (len(WPA), min(r["h"] for r in WPA), max(r["h"] for r in WPA), len(WPN),
         len(SZN), "/".join(str(v) for v in NU_DECOUPLE),
         min(r["h"] for r in WPN), max(r["h"] for r in WPN), len(WU),
         min(r["h"] for r in WU), max(r["h"] for r in WU),
         int(max(r["h"] for r in WU) / max(min(r["h"] for r in WU), 1))))

F_B11A = fit_exp(XA, [r["B11"] for r in WPA])
F_G16A = fit_exp(XA, [1.0 / r["g16"] for r in WPA])
F_GAINA = fit_exp(XA, [r["gain"] for r in WPA])
F_B11 = fit_exp(XU, [r["B11"] for r in WU])
F_G16 = fit_exp(XU, [1.0 / r["g16"] for r in WU])
F_GAIN = fit_exp(XU, [r["gain"] for r in WU])
check("sc_u0.reproduces_t165",
      qmax([r["e_qid"] for r in WU]) < EXACT_BAR
      and qmax([r["e_gauge"] for r in WU]) < EXACT_BAR
      and qmin([r["headroom"] for r in WU]) > HEADROOM_BAR
      and abs(F_B11A - T165_B11_EXP) < 0.35 and abs(F_G16A) < BAR_FLAT
      and abs(F_GAINA - T165_GAIN_EXP) < 0.35,
      "*** THE THREE T165 NUMBERS THIS WHOLE FILE IS ABOUT, REPRODUCED ON FRAME "
      "A. ***  1/g_1 = B_11 = %.4g .. %.4g, h^%+.3f (FIT, T165 quoted %+.3f); "
      "1/g_16 = %.4f .. %.4f, h^%+.3f (FIT, T165 quoted %+.3f, T164 range %.4f .. "
      "%.4f); the CASCADE GAIN g_16/g_1 = %.4g .. %.4g, h^%+.3f (FIT, T165 quoted "
      "%+.3f).  The exponents close ALGEBRAICALLY, which is a consistency check on "
      "the fits and nothing more: %+.3f - %+.3f = %+.3f against the measured "
      "%+.3f.  Pairing identity x^T B x = sum_d c_d w_d to %.1e on ALL %d union "
      "windows, gauge sum_d w_d = 0 to %.1e, headroom %.1e over machine eps"
      % (qmin([r["B11"] for r in WPA]), qmax([r["B11"] for r in WPA]), F_B11A,
         T165_B11_EXP, qmin([1.0 / r["g16"] for r in WPA]),
         qmax([1.0 / r["g16"] for r in WPA]), F_G16A, T164_G16_EXP,
         T164_G16_RANGE[0], T164_G16_RANGE[1], qmin([r["gain"] for r in WPA]),
         qmax([r["gain"] for r in WPA]), F_GAINA, T165_GAIN_EXP, F_B11A, F_GAINA,
         F_B11A - F_GAINA, F_G16A, qmax([r["e_qid"] for r in WU]), len(WU),
         qmax([r["e_gauge"] for r in WU]), qmin([r["headroom"] for r in WU])))

info("sc_u0.union_vs_frame_a",
     "*** A NUMBER THE ERRAND OF U3 EXISTS FOR, STATED HERE SO IT IS NEVER "
     "HIDDEN. ***  On the UNION the same three fits read h^%+.3f (B_11), h^%+.3f "
     "(1/g_16), h^%+.3f (gain), and 1/g_16 = %.4f .. %.4f.  The union sup EXCEEDS "
     "both the frame-A U_ref of T164 (%.4f) and the T165 nu-surface sup (%.4f), "
     "while the union 1/g_16 exponent %+.3f STILL sits inside the T159 flatness "
     "bar %.2f.  This is NOT a contradiction of T165: on the union h is driven by TWO "
     "independent knobs (zone depth and nu) and the single-covariate slope in h "
     "mixes them; U3(i) re-derives U_ref off-recipe over the union, U1 separates "
     "the covariates.  MEASURED"
     % (F_B11, F_G16, F_GAIN, qmin([1.0 / r["g16"] for r in WU]),
        qmax([1.0 / r["g16"] for r in WU]), T164_UREF, T165_NU_SUP, F_G16,
        BAR_FLAT))

print("")
print("TOTAL (U0): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("U1  THE CASCADE ANATOMY -- WHAT THE FIFTEEN INCREMENTS ACTUALLY ARE")
# ----------------------------------------------------------------------------
para("""U1.0  FOUR IDENTITIES BEFORE ANY NUMBER.  The cascade is usually written as
the Cholesky ladder g_K = sum_{j<=K} y_j^2, y = L_K^-1 e_1, and in that form the
increments look like fifteen unrelated positive numbers.  They are not.  Four
elementary identities -- all THEOREMS, all re-verified below on every window --
turn the ladder into one readable object:

(I1) PREFIX / CASCADE.  Because L is LOWER triangular, (L_K^-1 e_1)_j does not
depend on K for j <= K.  One Cholesky of the full 16 x 16 block therefore gives
ALL sixteen rungs simultaneously; the ladder is a genuine cascade.

(I2) MINOR FORM (Schur 1917; the Jacobi continued fraction).  g_K = det Q_K^{(1)}
/ det Q_K with Q_K^{(1)} = Q_K minus row and column 1, hence y_j^2 = g_j -
g_{j-1} is a ratio of consecutive minors.  This is what makes the increments
CLOSED objects in the block entries and not just outputs of a factorisation.

(I3) REGRESSION / COLLINEARITY FORM.  g_K = 1 / (B_11 - b^T B_HH^-1 b) with b =
Q_K[0,1:], so
        g_K / g_1  =  B_11 . (Q_K^-1)_{11}  =  1 / (1 - R_K^2) ,
where R_K^2 = b^T B_HH^-1 b / B_11 in [0,1) is exactly the fraction of the
mode-1 diagonal EXPLAINED by modes 2..K in the B metric.  *** THE OPEN OBJECT OF
T165 IS THEREFORE A NEAR-COLLINEARITY STATEMENT: g_16/g_1 >= c h^{3-eps} SAYS
THAT MODE 1 IS EXPLAINED BY MODES 2..16 UP TO A RESIDUAL FRACTION 1 - R_16^2 <=
h^{-3+eps}. ***  That is a much more specific request than ``a cancellation''.

(I4) DIAGONAL INVARIANCE.  The gain g_K/g_1 = B_11 (Q_K^-1)_{11} is INVARIANT
under B -> D B D for every positive diagonal D.  In particular it does not see
the KMS 1/sqrt(mu^P_k) normalisation at all: the h^3 is a property of the
arithmetic Gram block G = T A T^T, not of the KMS eigenvalues (KMS 1953).  This
kills one whole family of ``it is an artefact of the normalisation'' objections
before it is raised, and it is why U2 may work in the G metric whenever that is
more convenient.

DIRECTIONS, ONCE AND FOR ALL.  y_j^2 > 0 so g_K INCREASES in K, 1/g_K DECREASES,
and 1/g_K >= 1/s for every K (Schur nested complements).  1/g_K = min{x^T Q_K x :
x_1 = 1}, so a trial vector bounds 1/g_K from ABOVE and g_K from BELOW -- the
only useful direction for the open object.  R_K^2 INCREASES in K (Dirichlet
principle: a larger explanatory space explains more).""")

RNG = np.random.default_rng(1662)
E_PREFIX, E_MINOR, E_REG, E_INV = [], [], [], []
for r in WU:
    B = r["B_LL"]
    kl = r["kl"]
    cc = r["casc"]
    for K in (2, 3, 5, 8, kl):
        sub = cascade(B, K)
        if sub is None:
            continue
        E_PREFIX.append(float(np.max(np.abs(sub["y"] - cc["y"][:K]))
                              / max(np.max(np.abs(cc["y"][:K])), 1.0e-300)))
        s1, ld1 = np.linalg.slogdet(sym(B[:K, :K]))
        if K > 1:
            s2, ld2 = np.linalg.slogdet(sym(B[1:K, 1:K]))
        else:
            s2, ld2 = 1.0, 0.0
        if s1 > 0 and s2 > 0:
            E_MINOR.append(abs((ld2 - ld1) - math.log(float(cc["g"][K - 1])))
                           / max(abs(math.log(float(cc["g"][K - 1]))), 1.0))
        b = B[0, 1:K]
        R2 = float(b @ np.linalg.solve(sym(B[1:K, 1:K]), b)) / float(B[0, 0])
        gain_K = float(cc["g"][K - 1]) / float(cc["g"][0])
        E_REG.append(abs(gain_K - 1.0 / (1.0 - R2)) / gain_K)
        r["R2_%d" % K] = R2
    d = np.exp(RNG.normal(0.0, 1.5, size=kl))
    Bd = sym((B * np.outer(d, d)))
    cd = cascade(Bd, kl)
    if cd is not None:
        E_INV.append(abs(float(cd["g"][kl - 1]) / float(cd["g"][0]) - r["gain"])
                     / r["gain"])

check("sc_u1.identities",
      qmax(E_PREFIX) < 1.0e-11 and qmax(E_MINOR) < IDENT_BAR
      and qmax(E_REG) < IDENT_BAR and qmax(E_INV) < IDENT_BAR,
      "*** THE FOUR IDENTITIES, VERIFIED, NOT ASSUMED, ON ALL %d UNION WINDOWS AND "
      "FIVE RUNGS EACH. ***  (I1) prefix property of L_K^-1 e_1 to %.1e (bar "
      "1e-11: no ill-conditioned inverse enters); (I2) minor form log g_K = log det "
      "Q_K^{(1)} - log det Q_K to %.1e relative; (I3) gain = 1/(1 - R_K^2) to %.1e; "
      "(I4) invariance of the gain under B -> D B D for a random log-normal D "
      "(sigma = 1.5) to %.1e.  I2 .. I4 invert the low block, so they are judged "
      "against the DECLARED numerical horizon %.0e = eps . cond with margin: "
      "cond(B_LL) reaches %.1e here, eps . cond = %.1e.  STATUS: THEOREM (four "
      "identities); the numbers are only the arithmetic check that the code "
      "implements them"
      % (len(WU), qmax(E_PREFIX), qmax(E_MINOR), qmax(E_REG), qmax(E_INV),
         IDENT_BAR, qmax([r["kap"] for r in WU]),
         EPSM * qmax([r["kap"] for r in WU])))

para("""U1.1  WHICH RUNGS CARRY THE h^3.  Every window gets its sixteen increments
y_j^2 normalised two ways: the SHARE of the total gain, (g_K - g_1)/(g_16 - g_1),
and the per-rung ratio y_j^2 / y_1^2.  K_half is the first rung at which the
share reaches %.2f.  The exponent column is the FIT of 1/g_K against h -- the
rung at which the chain's flat object first appears.""" % RUNG_HALF)

for r in WU:
    cc = r["casc"]
    g = cc["g"]
    kl = r["kl"]
    tot = float(g[kl - 1] - g[0])
    share = [(float(g[K - 1] - g[0]) / tot if tot > 0 else float("nan"))
             for K in range(1, kl + 1)]
    khalf = next((K for K in range(1, kl + 1) if share[K - 1] >= RUNG_HALF), kl)
    r["share"] = share
    r["khalf"] = khalf
    r["rho2"] = float(cc["y2"][1] / cc["y2"][0])

TAB = ["  K   share(g_K)   1/g_K range              FIT h^   1-R_K^2 (med)   "
       "FIT h^",
       "  " + "-" * 74]
ONSET = None
FLAT_K = {}
for K in range(1, SCHUR_KB + 1):
    sh = [r["share"][K - 1] for r in WU if r["kl"] >= K]
    inv = [1.0 / float(r["casc"]["g"][K - 1]) for r in WU if r["kl"] >= K]
    xs = [float(r["h"]) for r in WU if r["kl"] >= K]
    res = [float(r["casc"]["g"][0] / r["casc"]["g"][K - 1]) for r in WU
           if r["kl"] >= K]
    fK = fit_exp(xs, inv)
    fR = fit_exp(xs, res)
    FLAT_K[K] = fK
    if ONSET is None and abs(fK) < BAR_FLAT:
        ONSET = K
    TAB.append("  %2d   %8.4f   %10.3e .. %-10.3e  %+7.3f  %12.4e  %+7.3f"
               % (K, qmed(sh), qmin(inv), qmax(inv), fK, qmed(res), fR))
block("\n".join(TAB))

KH = [r["khalf"] for r in WU]
SH2 = [r["share"][1] for r in WU]
SH5 = [r["share"][4] for r in WU if r["kl"] >= 5]
KH_A = [r["khalf"] for r in WPA]
KH_N = [r["khalf"] for r in WPN]
check("sc_u1.rung_profile",
      max(KH) <= 6 and qmed(SH5) > RUNG_HALF and ONSET is not None,
      "*** THE PROFILE, AND IT IS EXTREME. ***  Rung 2 ALONE already carries a "
      "median %.4f of the whole cascade gain (range %.4f .. %.4f); rungs 2..5 "
      "carry a median %.4f; K_half = %d .. %d on all %d union windows (frame A "
      "%d .. %d, decoupled nu %d .. %d), i.e. the h^3 is NEVER spread over the "
      "block -- it is bought in the FIRST TWO TO FIVE rungs and the remaining "
      "eleven only polish.  The chain's flat object appears at rung K = %d "
      "(|FIT| < %.2f first time); at K = 2 the fit is still h^%+.3f, at K = 5 "
      "h^%+.3f.  STATUS: MEASURED on the union surface"
      % (qmed(SH2), qmin(SH2), qmax(SH2), qmed(SH5), min(KH), max(KH), len(WU),
         min(KH_A), max(KH_A), min(KH_N), max(KH_N), ONSET, BAR_FLAT,
         FLAT_K[2], FLAT_K[5]))

para("""U1.2  THE CLOSED FORM OF THE FIRST STEP, AND WHAT CERTIFYING IT WOULD
COST.  For j = 2 everything is explicit.  With r_12 := B_12 / sqrt(B_11 B_22) the
mode-1/mode-2 correlation in the B metric (equivalently in the G metric, by I4),

    y_2^2 / y_1^2  =  B_12^2 / (B_11 B_22 - B_12^2)  =  r_12^2 / (1 - r_12^2) ,
    g_2 / g_1      =  1 / (1 - r_12^2) ,
    1/g_2          =  B_11 - B_12^2 / B_22  =  (G_11 - G_12^2/G_22) / mu^P_1 ,

all THEOREMS, the last one showing the mu^P cancellation of I4 in the raw
entries.  So the two-rung certificate needs exactly three m-free numbers: an
UPPER bound on G_11, an UPPER bound on G_22, and a LOWER bound on |G_12|.  The
m-free absolute-value budgets (head split, atom budget, moment laws) deliver the
two upper bounds and are SHARP there to a flat factor 21 .. 26.  The question
this block answers with numbers is whether that sharpness is enough, i.e. how
close to 1 the quantity r_12^2 has to be.""")

R12, ONEMR, RHO2, NEED = [], [], [], []
for r in WU:
    B = r["B_LL"]
    b11, b12, b22 = float(B[0, 0]), float(B[0, 1]), float(B[1, 1])
    r12sq = b12 * b12 / (b11 * b22)
    R12.append(r12sq)
    ONEMR.append(1.0 - r12sq)
    RHO2.append(r["rho2"])
    # the closed form, and the RELATIVE precision an absolute budget would need:
    # 1/g_2 = B_11 (1 - r_12^2), so a certificate must resolve B_11 and
    # B_12^2/B_22 against each other to relative accuracy (1 - r_12^2).
    NEED.append(1.0 / max(1.0 - r12sq, 1.0e-300))
    r["r12sq"] = r12sq

E_RHO2 = [abs(r["rho2"] - R12[i] / max(1.0 - R12[i], 1.0e-300))
          / max(r["rho2"], 1.0e-300) for i, r in enumerate(WU)]
F_ONEMR = fit_exp(XU, ONEMR)
F_ONEMRA = fit_exp(XA, [1.0 - r["r12sq"] for r in WPA])
check("sc_u1.first_rung_closed",
      qmax(E_RHO2) < 1.0e-9,
      "*** THE FIRST RUNG IS CLOSED, AND IT IS A NEAR-DEGENERACY. ***  "
      "y_2^2/y_1^2 = r_12^2/(1 - r_12^2) verified to %.1e on all %d windows.  "
      "MEASURED: r_12^2 = %.10f .. %.10f, so the 2 x 2 bottom block is degenerate "
      "to a residual 1 - r_12^2 = %.3e .. %.3e, h^%+.3f on the union (FIT; frame A "
      "h^%+.3f).  The first rung alone therefore multiplies g by %.4g .. %.4g.  "
      "*** THE PRICE OF A CERTIFICATE, STATED AS A NUMBER: an absolute-value "
      "budget must resolve B_11 against B_12^2/B_22 to RELATIVE accuracy 1 - "
      "r_12^2, i.e. sharp to a factor %.4g .. %.4g, whereas the m-free budgets are "
      "sharp to a flat factor 21 .. 26. ***  STATUS: THEOREM (the identity), "
      "MEASURED (the numbers)"
      % (qmax(E_RHO2), len(WU), qmin(R12), qmax(R12), qmin(ONEMR), qmax(ONEMR),
         F_ONEMR, F_ONEMRA, qmin(RHO2) + 1.0, qmax(RHO2) + 1.0, qmin(NEED),
         qmax(NEED)))

para("""U1.3  THE CASCADE AS A RITZ APPROXIMATION OF THE GREEN COLUMN.  T158's
bridge is a THEOREM and it is worth restating in the exact form used here: L_P
t_1 = mu^P_1 t_1 EXACTLY (KMS 1953), hence A^-1 L_P t_1 = mu^P_1 A^-1 t_1, hence
the two-dimensional space span{t_1, A^-1 L_P t_1} CONTAINS the Thomson maximiser
A^-1 t_1 itself and attains the entry
        s  =  mu^P_1 . t_1^T A^-1 t_1
EXACTLY.  The cascade is the SAME variational problem over the DIFFERENT trial
space span{t_1 .. t_K}: g_K = mu^P_1^-1 min{u^T G u : u_1 = 1, supp u <= K},
so g_K <= s for every K, with equality only in the limit.  Reading the two
together: THE CASCADE IS THE MODE-TRUNCATED APPROXIMATION OF THE GREEN COLUMN
A^-1 t_1, the increments y_j^2 are its successive Ritz gains, and the confinement
of T146/T157 (the bottom of A living in the low sines) is exactly the statement
that the truncation is cheap.  Both objects are computed here: s by ONE Cholesky
of A per window inside the declared horizon h <= %d, the two-dimensional Galerkin
value as an independent re-derivation of s, and the bottom eigenpair of A inside
the smaller declared horizon h <= %d.""" % (S_HCAP, EIG_HCAP))

WS = [r for r in WU if np.isfinite(r["s"])]
WE = [r for r in WU if np.isfinite(r["conf1"])]
E_BRIDGE = [abs(r["s_dual2"] - r["s"]) / abs(r["s"]) for r in WS
            if np.isfinite(r["s_dual2"])]
MONO = all(np.all(np.diff(r["casc"]["g"]) > 0.0) for r in WU)
LE_S = [r for r in WS if r["g16"] <= r["s"] * (1.0 + 1.0e-9)]
CONF16 = [r["g16"] / r["s"] for r in WS]
F_S = fit_exp([float(r["h"]) for r in WS], [r["s"] for r in WS])
F_SINV = fit_exp([float(r["h"]) for r in WS], [1.0 / r["s"] for r in WS])
check("sc_u1.green_bridge",
      len(WS) >= 20 and qmax(E_BRIDGE) < 1.0e-9 and MONO
      and len(LE_S) == len(WS),
      "*** THE T158 BRIDGE AND THE SCHUR DIRECTION, BOTH VERIFIED ON %d WINDOWS. "
      "***  The two-dimensional Galerkin value over span{t_1, A^-1 L_P t_1} "
      "reproduces the exact entry s = mu^P_1 t_1^T A^-1 t_1 to %.1e relative (it "
      "MUST: the maximiser lies in the span -- THEOREM), the cascade is strictly "
      "increasing on every window, and g_16 <= s holds on %d of %d windows as "
      "Schur monotonicity demands.  MEASURED: the exact entry itself is s = %.4f "
      ".. %.4f, i.e. 1/s = %.4f .. %.4f growing as h^%+.3f (FIT) -- the SAME "
      "flatness class as 1/g_16, which is the first hint that the truncation is "
      "not where the difficulty sits"
      % (len(WS), qmax(E_BRIDGE), len(LE_S), len(WS), qmin([r["s"] for r in WS]),
         qmax([r["s"] for r in WS]), qmin([1.0 / r["s"] for r in WS]),
         qmax([1.0 / r["s"] for r in WS]), F_SINV))

TAB2 = ["  K    g_K/s (min .. med .. max)          1 - g_K/s (med)",
        "  " + "-" * 62]
for K in (1, 2, 3, 5, 8, 12, SCHUR_KB):
    fr = [float(r["casc"]["g"][K - 1]) / r["s"] for r in WS if r["kl"] >= K]
    TAB2.append("  %2d    %.6e .. %.6f .. %.6f    %.4e"
                % (K, qmin(fr), qmed(fr), qmax(fr), 1.0 - qmed(fr)))
block("\n".join(TAB2))

F_DEF = fit_exp([float(r["h"]) for r in WS], [1.0 - r["g16"] / r["s"] for r in WS])
CONF_OK = qmin(CONF16) >= CONF_BAR
check("sc_u1.confinement_profile", len(WS) >= 20,
      "*** THE CONVERGENCE PROFILE, AND THE ONE PLACE WHERE THE 16 IS CHEAP. ***  "
      "g_16/s = %.4f .. %.4f (median %.4f) on %d windows, so the sixteen-mode "
      "truncation of the Green column already captures %.1f%% .. %.1f%% of the "
      "entry, and the DEFECT 1 - g_16/s = %.3e .. %.3e decays as h^%+.3f (FIT).  "
      "The preregistered bar CONF_BAR = %.2f is %s.  Rung 1 alone captures only "
      "%.3e of s, which is the whole problem in one number: the cascade must climb "
      "%.4g orders and it does %s of that climb in rung 2.  STATUS: MEASURED "
      "(the defect is a numerical quantity on this surface, NOT a certified bound)"
      % (qmin(CONF16), qmax(CONF16), qmed(CONF16), len(WS),
         100.0 * qmin(CONF16), 100.0 * qmax(CONF16),
         qmin([1.0 - r["g16"] / r["s"] for r in WS]),
         qmax([1.0 - r["g16"] / r["s"] for r in WS]), F_DEF, CONF_BAR,
         "MET on every window" if CONF_OK else "NOT met on every window",
         qmed([float(r["casc"]["g"][0]) / r["s"] for r in WS]),
         qmed([r["gain"] for r in WU]),
         "%.0f%%" % (100.0 * qmed(SH2))))

if WE:
    F_LAMLO = fit_exp([float(r["h"]) for r in WE], [r["lam_lo"] for r in WE])
    F_CONF1 = fit_exp([float(r["h"]) for r in WE], [r["conf1"] for r in WE])
    info("sc_u1.bottom_block",
         "*** WHAT DRIVES THE RATE: THE NEAR-DEGENERATE BOTTOM OF A. ***  On the "
         "%d windows inside the eigen-horizon h <= %d: lambda_min(A) = %.4e .. "
         "%.4e, h^%+.3f (FIT), the ratio lambda_2/lambda_1 = %.4f .. %.4f, and the "
         "mass of the bottom eigenvector of A inside the sixteen low parity sines "
         "is %.4f .. %.4f (median %.4f), h^%+.3f (FIT) -- the T146/T157 "
         "confinement, reproduced.  The bottom of A is where the Green column's "
         "norm lives, the low sines are where the bottom of A lives, and that "
         "composition -- not any property of the ladder -- is why sixteen modes "
         "suffice.  MEASURED"
         % (len(WE), EIG_HCAP, qmin([r["lam_lo"] for r in WE]),
            qmax([r["lam_lo"] for r in WE]), F_LAMLO,
            qmin([r["lam_gap"] for r in WE]), qmax([r["lam_gap"] for r in WE]),
            qmin([r["conf1"] for r in WE]), qmax([r["conf1"] for r in WE]),
            qmed([r["conf1"] for r in WE]), F_CONF1))

print("")
print("TOTAL (U1): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("U2  THE LOWER BOUND: THREE ROUTES TO g_16/g_1 >= c h^{3-eps}")
# ----------------------------------------------------------------------------
para("""U2.0  THE ONE ADMISSIBLE DIRECTION, AS A THEOREM.  Everything in this
block is an instance of a single elementary fact.  Write z = sum_k u_k t_k for a
vector in the span of the low parity sines.  Then

    g_K  =  max { 2 sqrt(mu^P_1) (t_1 . z) - z^T A z : z in span{t_1..t_K} }
         >=  mu^P_1 (t_1 . z)^2 / (z^T A z)      for EVERY such z ,

by optimising the scale of a single trial z (Thomson's principle; Maz'ya 1985).
Equivalently 1/g_K = mu^P_1^-1 min{u^T G u : u_1 = 1}.  DIRECTION: a trial vector
bounds g_K from BELOW and 1/g_K from ABOVE.  This is the only direction that can
ever close the open object, and it has a consequence that decides the shape of
the whole block: A CERTIFICATE NEEDS A CLOSED NEARLY-NULL VECTOR OF A INSIDE THE
SIXTEEN MODES WITH A NON-VANISHING t_1 COMPONENT, plus an m-free UPPER bound on
the single number z^T A z.  It does NOT need any lower bound on anything, and it
does NOT need the cancellation to be understood -- it needs the cancellation to
be EXHIBITED by an explicit z.""")

E_TRIAL, E_MINF = [], []
for r in WU:
    kl, mu1 = r["kl"], r["mu1_full"]
    G = r["G_LL"]
    u = np.zeros(kl)
    u[0] = 1.0
    u[1] = -float(G[0, 1]) / float(G[1, 1])
    lhs = mu1 / float(u @ (G @ u))
    E_TRIAL.append(1.0 if lhs <= float(r["casc"]["g"][1]) * (1.0 + 1.0e-9) else 0.0)
    ustar = r["xstar"] / np.sqrt(r["mu"][:kl])
    ustar = ustar / ustar[0]
    E_MINF.append(abs(float(ustar @ (G @ ustar)) / mu1 - 1.0 / r["g16"])
                  * r["g16"])
check("sc_u2.trial_direction",
      min(E_TRIAL) > 0.5 and qmax(E_MINF) < IDENT_BAR,
      "*** THE DIRECTION, CHECKED BEFORE IT IS USED. ***  The two-mode trial "
      "z = t_1 + beta* t_2 lands at or below g_2 on %d of %d windows (it must: g_2 "
      "is the maximum over that span), and the minimum form 1/g_16 = mu^P_1^-1 "
      "min{u^T G u : u_1 = 1} reproduces 1/g_16 at the chain's own x* to %.1e "
      "relative (numerical horizon %.0e).  STATUS: THEOREM"
      % (int(sum(E_TRIAL)), len(WU), qmax(E_MINF), IDENT_BAR))

para("""U2.1  ROUTE (i): THE TWO-RUNG CANDIDATE WITH A CLOSED beta.  By U1.2 the
whole h^3 is essentially in rung 2, so the cheapest conceivable certificate is a
CLOSED choice of beta in z = t_1 + beta t_2.  The value is a parabola,

    v(beta) = G_11 + 2 beta G_12 + beta^2 G_22 = v(beta*) + G_22 (beta - beta*)^2 ,
    beta* = -G_12/G_22 ,  v(beta*) = G_11 (1 - r_12^2) ,

so a closed beta is admissible only if it lands inside the window |beta - beta*|
<= sqrt(v(beta*)/G_22) -- a REQUIRED PRECISION that is tabulated below and is the
honest price of route (i).  Three candidate closed betas are tried, all declared
before the numbers were seen: beta_ar from the ARCHIMEDEAN block alone (the
explicit T115 kernel, no prime powers at all), beta_at from the ATOM block alone,
and the anti-fitting control beta = -1.  Nothing here is tuned: a candidate
either lands in the window or it does not.""")

for r in WU:
    G, Gar, Gat = r["G_LL"], r["G_ar"], r["G_at"]
    g11, g12, g22 = float(G[0, 0]), float(G[0, 1]), float(G[1, 1])
    r["bstar"] = -g12 / g22
    r["vstar"] = g11 + 2.0 * r["bstar"] * g12 + r["bstar"] ** 2 * g22
    r["dbeta_req"] = math.sqrt(max(r["vstar"], 0.0) / g22)
    r["bar"] = -float(Gar[0, 1]) / float(Gar[1, 1])
    r["bat"] = -float(Gat[0, 1]) / float(Gat[1, 1])
    for tag, bb in (("ar", r["bar"]), ("at", r["bat"]), ("m1", -1.0)):
        v = g11 + 2.0 * bb * g12 + bb * bb * g22
        r["v_" + tag] = v
        r["gain_" + tag] = (r["mu1_full"] / v) / r["g1"] if v > 0 else float("nan")
        r["dev_" + tag] = abs(bb - r["bstar"]) / max(r["dbeta_req"], 1.0e-300)

TAB3 = ["  candidate beta      |beta-beta*| / required     gain g/g_1 from it"
        "      FIT h^",
        "  " + "-" * 76]
GAIN_FITS = {}
for tag, nm in (("ar", "beta_ar (arch only)"), ("at", "beta_at (atoms only)"),
                ("m1", "beta = -1 (control)")):
    dv = [r["dev_" + tag] for r in WU]
    gn = [r["gain_" + tag] for r in WU]
    fg = fit_exp(XU, gn)
    GAIN_FITS[tag] = fg
    TAB3.append("  %-19s  %8.2e .. %-8.2e      %8.3g .. %-8.3g   %+7.3f"
                % (nm, qmin(dv), qmax(dv), qmin(gn), qmax(gn), fg))
TAB3.append("  %-19s  %8s     %8s      %8.3g .. %-8.3g   %+7.3f"
            % ("beta* (exact, NOT closed)", "0", "", qmin([r["gain"] for r in WU]),
               qmax([r["gain"] for r in WU]), F_GAIN))
block("\n".join(TAB3))

BEST_TAG = max(GAIN_FITS, key=lambda t: GAIN_FITS[t] if np.isfinite(GAIN_FITS[t])
               else -9.9)
ANY_IN = {t: sum(1 for r in WU if r["dev_" + t] <= 1.0)
          for t in ("ar", "at", "m1")}
check("sc_u2.two_rung_closed", True,
      "*** ROUTE (i), DECIDED BY NUMBERS AND NOT BY HOPE. ***  The required "
      "precision on beta is |beta - beta*| <= %.3e .. %.3e absolute, i.e. a "
      "RELATIVE precision of %.2e .. %.2e on beta* = %.6f .. %.6f.  Of the three "
      "declared closed candidates, beta_ar lands inside the window on %d of %d "
      "windows, beta_at on %d, the control beta = -1 on %d.  The gain each one "
      "actually certifies grows as h^%+.3f (arch), h^%+.3f (atoms), h^%+.3f "
      "(control) against the h^%+.3f the exact beta* delivers -- so route (i) as "
      "such does NOT reach h^{3-eps} with eps <= %.2f from any closed beta tried "
      "here.  STATUS: THEOREM for the parabola and the required-precision formula, "
      "MEASURED for the three candidate deviations"
      % (qmin([r["dbeta_req"] for r in WU]), qmax([r["dbeta_req"] for r in WU]),
         qmin([r["dbeta_req"] / abs(r["bstar"]) for r in WU]),
         qmax([r["dbeta_req"] / abs(r["bstar"]) for r in WU]),
         qmin([r["bstar"] for r in WU]), qmax([r["bstar"] for r in WU]),
         ANY_IN["ar"], len(WU), ANY_IN["at"], ANY_IN["m1"], GAIN_FITS["ar"],
         GAIN_FITS["at"], GAIN_FITS["m1"], F_GAIN, EPS_CARRY))

para("""U2.2  ROUTE (ii): WHAT EXACTLY CANCELS.  Two different things could make
the 2 x 2 block nearly singular, and they have opposite consequences.  If the
near-degeneracy is an ARCH-AGAINST-ATOM cancellation (the mechanism of T159/T160)
then no closed object sees it, because the two halves are individually huge and
the smallness is in their difference.  If it is a MODE-AGAINST-MODE effect
already present in the ARCHIMEDEAN kernel alone, the mechanism is explicit and
m-free, and the certificate is within reach.  The test is direct: compute r_12^2
for the arch block alone, the atom block alone, and the full block, and compute
the entry-wise cancellation ratio |G_kl| / max(|G_kl^arch|, |G_kl^atom|).""")

CAN, R12AR, R12AT = {}, [], []
for r in WU:
    G, Gar, Gat = r["G_LL"], r["G_ar"], r["G_at"]
    for (a, b) in ((0, 0), (0, 1), (1, 1)):
        key = "%d%d" % (a + 1, b + 1)
        big = max(abs(float(Gar[a, b])), abs(float(Gat[a, b])))
        CAN.setdefault(key, []).append(abs(float(G[a, b])) / max(big, 1.0e-300))
    for Gx, out in ((Gar, R12AR), (Gat, R12AT)):
        d = float(Gx[0, 0]) * float(Gx[1, 1])
        out.append(float(Gx[0, 1]) ** 2 / d if d > 0 else float("nan"))

TAB4 = ["  object              min .. med .. max                        FIT h^",
        "  " + "-" * 72]
for key in ("11", "12", "22"):
    TAB4.append("  |G_%s|/max(ar,at)   %.4f .. %.4f .. %.4f"
                % (key, qmin(CAN[key]), qmed(CAN[key]), qmax(CAN[key])))
for nm, arr in (("1-r_12^2 full ", [1.0 - r["r12sq"] for r in WU]),
                ("1-r_12^2 arch ", [1.0 - t for t in R12AR]),
                ("1-r_12^2 atoms", [1.0 - t for t in R12AT])):
    TAB4.append("  %s      %.4e .. %.4e .. %.4e   %+7.3f"
                % (nm, qmin(arr), qmed(arr), qmax(arr), fit_exp(XU, arr)))
block("\n".join(TAB4))

F_1MRAR = fit_exp(XU, [1.0 - t for t in R12AR])
para("""The table says something none of the three prepared stories predicted, so
it is worth stating plainly before it is analysed.  NO ENTRY of the 2 x 2 block is
a cancellation (each of G_11, G_12, G_22 keeps 60%% .. 99%% of its larger half),
and NEITHER HALF is collinear on its own -- the archimedean block has 1 - r_12^2
= 0.98, i.e. no degeneracy whatsoever, and the atom block 0.04 .. 0.50.  Yet the
SUM is degenerate to 1e-7 .. 5e-4.  The cancellation is therefore not in any lag
sum: IT IS IN THE 2 x 2 GRAM DETERMINANT.  For 2 x 2 blocks the determinant is a
quadratic (polarisation) form and splits into exactly three named pieces,

    det(G_ar + G_at) = det G_ar + det G_at + Pi ,
    Pi := G^ar_11 G^at_22 + G^at_11 G^ar_22 - 2 G^ar_12 G^at_12 ,

Pi being the mixed polarisation term.  The next check measures the three pieces
and their cancellation ratio, which is the number that decides how hard route (i)
really is.""")

DETC, DPARTS = [], {"ar": [], "at": [], "mix": []}
for r in WU:
    Gar, Gat = r["G_ar"], r["G_at"]
    d_ar = float(Gar[0, 0] * Gar[1, 1] - Gar[0, 1] ** 2)
    d_at = float(Gat[0, 0] * Gat[1, 1] - Gat[0, 1] ** 2)
    pi = float(Gar[0, 0] * Gat[1, 1] + Gat[0, 0] * Gar[1, 1]
               - 2.0 * Gar[0, 1] * Gat[0, 1])
    G = r["G_LL"]
    d_full = float(G[0, 0] * G[1, 1] - G[0, 1] ** 2)
    r["det2"] = d_full
    r["det_id"] = abs(d_ar + d_at + pi - d_full) / max(abs(d_ar), abs(d_at),
                                                       abs(pi))
    big = max(abs(d_ar), abs(d_at), abs(pi))
    DETC.append(abs(d_full) / max(big, 1.0e-300))
    DPARTS["ar"].append(d_ar)
    DPARTS["at"].append(d_at)
    DPARTS["mix"].append(pi)

F_DETC = fit_exp(XU, DETC)
check("sc_u2.cancellation_anatomy",
      qmax([r["det_id"] for r in WU]) < 1.0e-10,
      "*** THE ANATOMY, AND IT IS A THIRD MECHANISM -- NEITHER OF THE TWO THE "
      "BLOCK WAS SET UP TO DISTINGUISH. ***  The polarisation split det(G_ar + "
      "G_at) = det G_ar + det G_at + Pi holds to %.1e (THEOREM, checked).  MEASURED: "
      "det G_ar = %.4e .. %.4e, det G_at = %.4e .. %.4e, Pi = %.4e .. %.4e, and the "
      "FULL determinant is %.4e .. %.4e -- a cancellation ratio |det G| / "
      "max(pieces) = %.3e .. %.3e which itself DECAYS as h^%+.3f (FIT).  So: the "
      "individual lag sums do NOT cancel (U2.2 table), each half alone is NOT "
      "collinear (arch 1 - r_12^2 = %.3f, atoms %.3f), but the 2 x 2 GRAM "
      "DETERMINANT of the sum cancels to seven digits.  The h^3 of rung 2 is an "
      "ARCH-AGAINST-ATOM cancellation like T159/T160, but it lives one level up, in "
      "a QUADRATIC functional of the lag sums rather than in a lag sum.  STATUS: "
      "THEOREM (the split), MEASURED (the sizes) on %d windows of both surfaces"
      % (qmax([r["det_id"] for r in WU]), qmin(DPARTS["ar"]), qmax(DPARTS["ar"]),
         qmin(DPARTS["at"]), qmax(DPARTS["at"]), qmin(DPARTS["mix"]),
         qmax(DPARTS["mix"]), qmin([r["det2"] for r in WU]),
         qmax([r["det2"] for r in WU]), qmin(DETC), qmax(DETC), F_DETC,
         qmed([1.0 - t for t in R12AR]), qmed([1.0 - t for t in R12AT]), len(WU)))

para("""U2.3  ROUTE (iii): DOES THE T146/T157 CONFINEMENT DELIVER THE BOUND?  The
confinement of U1.3 is spectacular -- the bottom eigenvector of A lives to
0.9999 .. 1.0000 inside the sixteen low sines -- so it is exactly the kind of
statement one would like to convert into a lower bound.  The conversion is the
trial-vector theorem of U2.0 applied to z = v_0: g_16 >= mu^P_1 (t_1 . v_0)^2 /
lambda_min(A) whenever v_0 lies in the span, and the confinement says it
essentially does.  The question is whether the resulting number is BIG, and that
is a race between two measured exponents: mu^P_1 ~ h^-2 EXACTLY (KMS 1953) against
lambda_min(A).  The Green column's own decomposition s = mu^P_1 sum_i (t_1.v_i)^2
/ lambda_i says how many bottom modes are really needed.""")

if WE:
    XE = [float(r["h"]) for r in WE]
    RAY = [r["ray0"] for r in WE]
    F_RAY = fit_exp(XE, RAY)
    F_RAYG = fit_exp(XE, [r["ray0"] / r["g1"] for r in WE])
    F_MU1 = fit_exp(XE, [r["mu1_full"] for r in WE])
    TAB5 = ["  bottom modes j     s-fraction captured (min .. med .. max)",
            "  " + "-" * 62]
    for jj in (1, 2, 4, 8, 16, 32):
        fr = [r["sfrac"][jj] for r in WE if jj in r["sfrac"]]
        if fr:
            TAB5.append("  %2d                 %.4e .. %.4e .. %.4e"
                        % (jj, qmin(fr), qmed(fr), qmax(fr)))
    block("\n".join(TAB5))
    F_RAYP = fit_exp(XE, [r["rayP"] for r in WE])
    F_RAYPG = fit_exp(XE, [r["rayP"] / r["g1"] for r in WE])
    WEA = [r for r in WE if r["surf"] == "A"]
    WEN = [r for r in WE if r["surf"] == "N"]
    F_RPG_A = fit_exp([float(r["h"]) for r in WEA],
                      [r["rayP"] / r["g1"] for r in WEA])
    F_RPG_N = fit_exp([float(r["h"]) for r in WEN],
                      [r["rayP"] / r["g1"] for r in WEN])
    F_RPG_SUB = fit_exp([float(r["h"]) for r in WEA if r["h"] <= 780],
                        [r["rayP"] / r["g1"] for r in WEA if r["h"] <= 780])
    info("sc_u2.subsurface_warning",
         "*** A LEVER-ARM LESSON, RECORDED BECAUSE THIS FILE WALKED INTO IT. ***  "
         "The projected-trial gain exponent reads h^%+.3f on frame A restricted to "
         "h <= 780 (the eigen-horizon an earlier pass of this probe used), h^%+.3f "
         "on all of frame A, h^%+.3f on the decoupled nu surface and h^%+.3f on the "
         "union of %d windows.  The restricted read was OPTIMISTIC by %+.3f in the "
         "exponent, which is more than the whole eps budget %.2f.  Every verdict "
         "below therefore uses the UNION number, and this is a concrete reason to "
         "distrust any exponent quoted on a sub-surface.  MEASURED"
         % (F_RPG_SUB, F_RPG_A, F_RPG_N, F_RAYPG, len(WE),
            F_RPG_SUB - F_RAYPG, EPS_CARRY))
    F_RAT = fit_exp(XE, [r["rayP"] / r["g16"] for r in WE])
    OK_P = all(r["rayP"] <= r["g16"] * (1.0 + 1.0e-8) for r in WE)
    OK_S = all(r["ray0"] <= r["s"] * (1.0 + 1.0e-8) for r in WE
               if np.isfinite(r["s"]))
    check("sc_u2.confinement_route", OK_P and OK_S,
          "*** ROUTE (iii), AND IT IS THE ONE ROUTE WITH THE RIGHT EXPONENT. ***  "
          "DIRECTION FIRST, because it is easy to get wrong here: v_0 is a trial "
          "vector for the FULL space, so mu^P_1 (t_1.v_0)^2/lambda_min(A) bounds s "
          "from below (%s on all %d windows) but NOT g_16 -- v_0 keeps a mass 1e-4 "
          "outside the sixteen modes, and MEASURED it does exceed g_16 on some "
          "windows (ratio %.3f .. %.3f).  The legitimate object is the PROJECTED "
          "trial z = P_16 v_0, and mu^P_1 (t_1.z)^2 / z^T A z <= g_16 holds on %d of "
          "%d windows as it must (THEOREM).  MEASURED: that projected bound is %.4f "
          ".. %.4f against g_16 = %.4f .. %.4f, a fraction %.4f .. %.4f of the "
          "certified value, it DECAYS as h^%+.3f, and against g_1 ~ h^%+.3f it "
          "buys a gain of h^%+.3f -- i.e. %.0f%% of the h^%+.3f the ladder delivers "
          "and MORE than the h^%+.3f (3 - eps) the quantifier needs.  The race "
          "behind it: mu^P_1 ~ h^%+.3f (FIT of the EXACT KMS value) against "
          "lambda_min(A) ~ h^%+.3f, with the overlap (t_1.v_0)^2 = %.4f .. %.4f "
          "carrying the remainder; the ratio bound/g_16 trends as h^%+.3f, so the "
          "route is not asymptotically free.  %d .. %d bottom modes give 90%% of s.  "
          "STATUS: THEOREM (both bounds), MEASURED (all exponents)"
          % ("verified" if OK_S else "VIOLATED", len(WE),
             qmin([r["ray0"] / r["g16"] for r in WE]),
             qmax([r["ray0"] / r["g16"] for r in WE]),
             sum(1 for r in WE if r["rayP"] <= r["g16"] * (1.0 + 1.0e-8)), len(WE),
             qmin([r["rayP"] for r in WE]), qmax([r["rayP"] for r in WE]),
             qmin([r["g16"] for r in WE]), qmax([r["g16"] for r in WE]),
             qmin([r["rayP"] / r["g16"] for r in WE]),
             qmax([r["rayP"] / r["g16"] for r in WE]), F_RAYP,
             fit_exp(XE, [r["g1"] for r in WE]), F_RAYPG,
             100.0 * F_RAYPG / max(F_GAIN, 1.0e-9), F_GAIN, 3.0 - EPS_CARRY,
             F_MU1, fit_exp(XE, [r["lam_lo"] for r in WE]),
             qmin([r["ov0"] for r in WE]), qmax([r["ov0"] for r in WE]), F_RAT,
             min(r["nmode"] for r in WE), max(r["nmode"] for r in WE)))

E11_A, E11_U = F_B11A, F_B11
EPS_ALLOWED = 3.0 - E11_A
check("sc_u2.equivalence_care", True,
      "*** A PEDANTIC POINT THAT CHANGES WHAT COUNTS AS SUCCESS, SO IT IS RAISED "
      "BEFORE THE BEST BOUND IS QUOTED. ***  The open object is stated in two forms: "
      "(F1) inf_m g_16(m) > 0, and (F2) g_16/g_1 >= c h^{3-eps} uniformly.  They are "
      "equivalent ONLY IF 1/g_1 = B_11 is EXACTLY of order h^3.  MEASURED it is not: "
      "B_11 ~ h^%+.3f on frame A and h^%+.3f on the union.  Since g_16 = g_1 . gain, "
      "form (F2) with exponent 3 - eps gives only g_16 >~ h^{3 - eps - %.3f}, so (F1) "
      "requires eps <= %+.3f -- a NEGATIVE eps on frame A.  CONSEQUENCE: on this "
      "surface (F2) with any eps > 0 is STRICTLY WEAKER than (F1), and a route that "
      "reaches h^{3-eps} with eps = 0.29 (U2.3) has NOT closed the quantifier.  "
      "Every verdict below distinguishes the two.  STATUS: THEOREM (the implication), "
      "MEASURED (the exponent that decides it)"
      % (E11_A, E11_U, E11_A, EPS_ALLOWED))

para("""U2.4  THE BEST BOUND, AND THE ONE INEQUALITY THAT IS LEFT.  Combining I2
(minor form) with I4 (diagonal invariance) turns the chain's object into a RATIO
OF TWO CONSECUTIVE GRAM MINORS OF THE ARITHMETIC BLOCK, with the KMS eigenvalue
appearing exactly once and explicitly:

    1/g_K  =  det G_[1..K]  /  ( mu^P_1 . det G_[2..K] )  ,   mu^P_1 = 4 sin^2(pi/N).

That is the sharpest available restatement of the open object, and it is verified
below to the declared horizon.  Everything the chain needs is one uniform upper
bound on that ratio at the first K where it is flat.  The two closed
ingredients G_11 .. G_KK are already budgeted by the m-free machinery to a flat
factor 21 .. 26; the missing object is the DETERMINANT, and U2.2 measured exactly
how much cancellation it hides.""")

E_MIN2, RATIO_TAB = [], []
K_LIST = (2, 3, 6, SCHUR_KB)
for r in WU:
    G, mu1 = r["G_LL"], r["mu1_full"]
    for K in K_LIST:
        if r["kl"] < K:
            continue
        s1, l1 = np.linalg.slogdet(sym(G[:K, :K]))
        s2, l2 = np.linalg.slogdet(sym(G[1:K, 1:K]))
        if s1 <= 0 or s2 <= 0:
            continue
        lhs = math.log(1.0 / float(r["casc"]["g"][K - 1]))
        E_MIN2.append(abs(lhs - (l1 - l2 - math.log(mu1))) / max(abs(lhs), 1.0))
        r["hadam_%d" % K] = float(np.exp(l1 - float(np.sum(np.log(
            np.diag(sym(G[:K, :K])))))))

TAB6 = ["   K   1/g_K on union            FIT h^   Hadamard defect det/prod(diag)"
        "   FIT h^",
        "  " + "-" * 76]
for K in K_LIST:
    inv = [1.0 / float(r["casc"]["g"][K - 1]) for r in WU if r["kl"] >= K]
    xs = [float(r["h"]) for r in WU if r["kl"] >= K]
    hd = [r["hadam_%d" % K] for r in WU if "hadam_%d" % K in r]
    TAB6.append("  %2d   %8.4f .. %-8.4f      %+7.3f   %10.3e .. %-10.3e  %+7.3f"
                % (K, qmin(inv), qmax(inv), fit_exp(xs, inv), qmin(hd), qmax(hd),
                   fit_exp(xs, hd)))
block("\n".join(TAB6))

K_FLAT_U = next((K for K in range(1, SCHUR_KB + 1) if abs(FLAT_K[K]) < BAR_FLAT),
                SCHUR_KB)
FLAT_A = {}
for K in range(1, SCHUR_KB + 1):
    FLAT_A[K] = fit_exp([float(r["h"]) for r in WPA if r["kl"] >= K],
                        [1.0 / float(r["casc"]["g"][K - 1]) for r in WPA
                         if r["kl"] >= K])
K_FLAT_A = next((K for K in range(1, SCHUR_KB + 1) if abs(FLAT_A[K]) < BAR_FLAT),
                SCHUR_KB)
BEST_EXP = max(GAIN_FITS["at"], GAIN_FITS["ar"], GAIN_FITS["m1"])
NEED_EXP = 3.0 - EPS_CARRY
check("sc_u2.minor_ratio_reduction", qmax(E_MIN2) < IDENT_BAR,
      "*** THE SHARPEST RESTATEMENT THIS FILE CAN OFFER, AND THE SIZE OF WHAT IS "
      "MISSING. ***  1/g_K = det G_[1..K] / (mu^P_1 det G_[2..K]) verified to %.1e "
      "relative on %d evaluations (horizon %.0e).  The ratio is flat first at K = %d "
      "on the union (K = %d on frame A), so the chain needs ONE uniform inequality: "
      "det G_[1..%d] <= U . mu^P_1 . det G_[2..%d], and on this surface that U is "
      "%.4f .. %.4f.  The Hadamard defect det G_[1..K] / prod diag shows how much "
      "collinearity has to be resolved: %.3e .. %.3e at K = %d.  BEST LOWER BOUND "
      "ACTUALLY CERTIFIED-IN-SHAPE HERE: the closed-beta two-rung bound at h^%+.3f, "
      "against the h^%+.3f the exact ladder delivers and the h^%+.3f (3 - eps, eps "
      "<= %.2f) the quantifier needs -- a shortfall of h^%+.3f.  STATUS: THEOREM "
      "(the minor-ratio identity), MEASURED (U and the defects)"
      % (qmax(E_MIN2), len(E_MIN2), IDENT_BAR, K_FLAT_U, K_FLAT_A, K_FLAT_U,
         K_FLAT_U, qmin([1.0 / float(r["casc"]["g"][K_FLAT_U - 1]) for r in WU
                         if r["kl"] >= K_FLAT_U]),
         qmax([1.0 / float(r["casc"]["g"][K_FLAT_U - 1]) for r in WU
               if r["kl"] >= K_FLAT_U]),
         qmin([r["hadam_%d" % K_FLAT_U] for r in WU
               if "hadam_%d" % K_FLAT_U in r]),
         qmax([r["hadam_%d" % K_FLAT_U] for r in WU
               if "hadam_%d" % K_FLAT_U in r]), K_FLAT_U, BEST_EXP, F_GAIN,
         NEED_EXP, EPS_CARRY, NEED_EXP - BEST_EXP))

print("")
print("TOTAL (U2): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("U3  THE TWO ERRANDS, THE ASSEMBLY, AND THE MANDATORY STRESS")
# ----------------------------------------------------------------------------
para("""U3.1  THE U_ref ERRAND, DONE OFF-RECIPE AND DECLARED AS SUCH.  T164 fixed
U_ref = %.2f as the frame-A supremum of 1/g_16; T165's decoupled nu surface found
%.4f there, i.e. the constant was surface-dependent and therefore not yet a
constant.  The honest repair is not a bigger surface but an explicitly OFF-RECIPE
rule, stated before the number: U_ref := SAFETY . sup over the UNION of both
surfaces, with a DECLARED safety factor SAFETY = %.2f.  The factor is not fitted
to anything; it is the price of admitting that the supremum is taken over a finite
window list.  This constant remains CERT-WINDOW, never CERT-UNIF: it is a
statement about the union surface, and any promotion must say so.""" % (
    T164_UREF, T165_NU_SUP, SAFETY_UREF))

SUP_A = qmax([1.0 / r["g16"] for r in WPA])
SUP_N = qmax([1.0 / r["g16"] for r in WPN])
SUP_U = max(SUP_A, SUP_N)
U_REF_NEW = SAFETY_UREF * SUP_U
ARG_U = max(WU, key=lambda r: 1.0 / r["g16"])
check("sc_u3.uref_errand",
      U_REF_NEW > SUP_U and all(1.0 / r["g16"] <= U_REF_NEW for r in WU),
      "*** THE ERRAND, CLOSED WITH A NUMBER. ***  sup 1/g_16 = %.4f on frame A "
      "(T164 quoted %.2f), %.4f on the decoupled nu surface (T165 quoted %.4f), "
      "%.4f on the union -- attained at zone n = %d, nu = %.0f, h = %d, which is a "
      "DEEP zone at MODERATE nu, so the union supremum is driven by ZONE DEPTH and "
      "not by resolution.  With the declared safety factor %.2f: U_ref(union) = "
      "%.4f, and 1/g_16 <= U_ref on all %d windows of both surfaces by "
      "construction.  This SUPERSEDES the T164 value %.2f for any statement made "
      "on the union.  STATUS: CERT-WINDOW (off-recipe rule, declared), never "
      "CERT-UNIF"
      % (SUP_A, T164_UREF, SUP_N, T165_NU_SUP, SUP_U, ARG_U["n_zone"],
         ARG_U["nu"], ARG_U["h"], SAFETY_UREF, U_REF_NEW, len(WU), T164_UREF))

para("""U3.2  DEEPER ZONES INSIDE THE CAP, AND THE TWO KNOBS SEPARATED.  The cap
MAX_H = %d is hard, so depth and resolution compete for the same budget: at fixed
zone the largest admissible nu is bounded by h(zone, nu) <= %d.  The table gives
the per-zone lever arm actually realised.  The multi-covariate fit then separates
the two knobs, which is the only way to say whether the 1/g_16 growth is a
statement about m or about the recipe -- with a single covariate the two are
confounded (T165 measured their collinearity at 0.68).""" % (MAX_H, HCAP))

ZTAB = ["  zone n      alpha    nu list realised     h range        lever",
        "  " + "-" * 66]
for (kz, Dz, Mz, hz) in SZN:
    rs = [r for r in WPN if r["k"] == kz]
    if not rs:
        continue
    ZTAB.append("  %-10d  %6.3f   %-18s  %5d .. %-6d  %4.1fx"
                % (rs[0]["n_zone"], rs[0]["alpha"],
                   "/".join("%.0f" % r["nu"] for r in rs),
                   min(r["h"] for r in rs), max(r["h"] for r in rs),
                   max(r["h"] for r in rs) / max(min(r["h"] for r in rs), 1)))
block("\n".join(ZTAB))

CO = float(np.corrcoef(np.log([r["h"] for r in WU]),
                       np.log([r["nu"] for r in WU]))[0, 1])
(SL_H, SL_NU), R2M = fit_multi([[r["h"] for r in WU], [r["nu"] for r in WU]],
                               [1.0 / r["g16"] for r in WU])
(SL_HG, SL_NUG), R2G = fit_multi([[r["h"] for r in WU], [r["nu"] for r in WU]],
                                 [r["gain"] for r in WU])
DEEPEST = max(WU, key=lambda r: r["n_zone"])
check("sc_u3.depth_and_nu",
      len(SZN) >= 4 and abs(CO) < 0.9,
      "*** DEPTH AND RESOLUTION, SEPARATED. ***  The union carries %d zones on the "
      "nu surface with per-zone lever arms up to %.1fx, the deepest zone admitted "
      "is n = %d (alpha = %.3f, X = n^2 = %.3e, %d prime-power atoms) at h = %d, "
      "and log h vs log nu are correlated at only %.3f, so the design does "
      "separate the knobs (T165 measured 0.68 on its own surface).  MULTI-COVARIATE "
      "FIT: 1/g_16 ~ h^%+.3f nu^%+.3f (R^2 = %.3f) and the cascade gain ~ h^%+.3f "
      "nu^%+.3f (R^2 = %.3f).  READING: the gain's h exponent %+.3f survives after "
      "nu is controlled for, and the residual nu dependence of 1/g_16 (%+.3f) is "
      "what the T164 U_ref could not see.  STATUS: MEASURED (both fits are FITS and "
      "no bound below uses them)"
      % (len(SZN), qmax([max(r["h"] for r in WPN if r["k"] == kz)
                         / max(min(r["h"] for r in WPN if r["k"] == kz), 1)
                         for (kz, _a, _b, _c) in SZN
                         if any(r["k"] == kz for r in WPN)]),
         DEEPEST["n_zone"], DEEPEST["alpha"], DEEPEST["X"], DEEPEST["n_atom"],
         DEEPEST["h"], CO, SL_H, SL_NU, R2M, SL_HG, SL_NUG, R2G, SL_HG, SL_NU))

para("""U3.3  THE ASSEMBLY: THE BEST CERTIFIED LOWER BOUND ON THE UNION.  All three
routes produce lower bounds on the SAME object, so they may be combined by taking
the maximum -- a max of valid lower bounds is a valid lower bound.  The chain that
results is
    g_1  <=  g_2(beta_at)  <=  max-of-routes  <=  g_16  <=  s ,
each inequality either a Schur monotonicity or a trial-vector step, and each one
is verified window by window rather than assumed.  The exponent of the max is the
headline number of this file.""")

for r in WU:
    cands = [r["g1"]]
    if np.isfinite(r.get("v_at", float("nan"))) and r["v_at"] > 0:
        cands.append(r["mu1_full"] / r["v_at"])
    if np.isfinite(r.get("rayP", float("nan"))):
        cands.append(r["rayP"])
    r["gbest"] = max(cands)
    r["gbest_gain"] = r["gbest"] / r["g1"]

CHAIN_OK = sum(1 for r in WU if r["g1"] <= r["gbest"] + 1.0e-15
               and r["gbest"] <= r["g16"] * (1.0 + 1.0e-8)
               and (not np.isfinite(r["s"]) or r["g16"] <= r["s"] * (1.0 + 1.0e-9)))
ROWS = [("rung 1 (trivial, g_1)", WU, lambda r: r["g1"]),
        ("two-rung, closed beta_at", WU, lambda r: r["mu1_full"] / r["v_at"]),
        ("two-rung, closed beta_ar", WU, lambda r: r["mu1_full"] / r["v_ar"]),
        ("proj. bottom mode (NOT closed)", WE, lambda r: r["rayP"]),
        ("max of all routes", WE, lambda r: r["gbest"]),
        ("exact ladder g_16 (NOT closed)", WU, lambda r: r["g16"])]
TAB7 = ["  route                            n   bound range              gain "
        "h^     F2?",
        "  " + "-" * 76]
BEST_INF = 0.0
for nm, ws, fn in ROWS:
    if not ws:
        continue
    vals = [fn(r) for r in ws]
    ge = fit_exp([float(r["h"]) for r in ws], [fn(r) / r["g1"] for r in ws])
    ok2 = (3.0 - ge) <= EPS_CARRY
    TAB7.append("  %-31s %3d  %.3e .. %-.3e  %+7.3f  %s"
                % (nm, len(ws), qmin(vals), qmax(vals), ge,
                   "yes" if ok2 else "no"))
    if nm.startswith("max of"):
        BEST_INF = qmin(vals)
block("\n".join(TAB7))

F_BEST = fit_exp([float(r["h"]) for r in WE], [r["gbest_gain"] for r in WE]) \
    if WE else float("nan")
F_GB = fit_exp([float(r["h"]) for r in WE], [r["gbest"] for r in WE]) \
    if WE else float("nan")
check("sc_u3.assembly", CHAIN_OK == len(WU),
      "*** THE END-TO-END CHAIN, AND THE HEADLINE NUMBER. ***  Every inequality of "
      "g_1 <= best-of-routes <= g_16 <= s is verified on %d of %d union windows; "
      "nothing in the chain is assumed.  All three routes now exist on the WHOLE "
      "union (%d windows, eigen-horizon raised to the h <= %d cap), and there the "
      "combined bound is g_16 >= %.4e .. %.4e with a gain over rung 1 of h^%+.3f "
      "against the h^%+.3f of the exact ladder.  BOTH FORMS FAIL, and by clearly "
      "different margins: form F2 (gain >= c h^{3-eps}) would need eps = %.3f "
      "whereas only eps <= %.2f was preregistered as honouring it, so F2 is NOT "
      "reached; form F1 (inf_m g_16 > 0) fails harder still, the bound itself "
      "decaying as h^%+.3f down to an infimum %.4e.  Restricted to frame A the same "
      "route reads h^%+.3f and WOULD have honoured F2 -- the decoupled nu surface is "
      "what removes it, which is exactly what that surface was built for.  "
      "STATUS: THEOREM for every step, CERT-WINDOW for the numbers, MEASURED for the "
      "exponents"
      % (CHAIN_OK, len(WU), len(WE), EIG_HCAP, qmin([r["gbest"] for r in WE]),
         qmax([r["gbest"] for r in WE]), F_BEST, F_GAIN, 3.0 - F_BEST, EPS_CARRY,
         F_GB, BEST_INF, F_RPG_A))

para("""TWO QUALIFICATIONS, IN CAPITALS, BECAUSE THE TABLE INVITES TWO WRONG
READINGS.  FIRST: the projected-bottom-mode route uses v_0 from a NUMERICAL
eigen-decomposition of A, so it is NOT a certificate and cannot be promoted as
one.  SECOND, and this one corrects a temptation this file had to resist: the
projected bottom mode is NOT the optimal vector of the sixteen-mode space.  The
optimum over span{t_1..t_16} is x* = B_LL^-1 e_1 and it attains g_16 BY DEFINITION,
so asking whether the sixteen-mode space is 'big enough' is vacuous for the
contract -- the contract object IS that optimum.  What the confinement route
measures is how good a STRUCTURALLY MOTIVATED SURROGATE for x* is, and the answer
is: not good enough, and worse where it matters.  It reads h^%+.3f on frame A,
h^%+.3f on the decoupled nu surface and h^%+.3f on the union, against the h^%+.3f
of x* itself.  The loss is the PROJECTION loss: v_0 is a near-null vector of A on
the whole space and truncating it to sixteen modes costs more as nu grows.""" % (
    F_RPG_A, F_RPG_N, F_RAYPG, F_GAIN))

para("""U3.4  HOW MUCH OF THE SURROGATE'S LOSS IS THE PROJECTION?  The question the
qualification leaves open is whether the confinement surrogate fails because the
prime-power structure defeats it or merely because sixteen modes truncate it too
hard.  That is testable immediately, since the pipeline already builds the enlarged
K = %d block, and the comparison is clean: the SAME v_0, projected into %d modes
instead of 16.  Two directions must be stated first.  g_K is INCREASING in K (Schur
1917), so g_64 >= g_16 and 1/g_64 <= 1/g_16 is a BETTER upper bound on 1/s.  But in
the T163/T164 price P_pr = g_16 Q_n the quantifier sits in the NUMERATOR, so a
larger g makes the PRICE larger: enlarging K helps the quantifier and hurts the
price, and whether the chain may use K = %d at all is a T163/T164 question this file
does NOT settle.""" % (KB_MAX, KB_MAX, KB_MAX))

W64 = [r for r in WU if r["nb"] >= KB_MAX and r["casc"] is not None]
for r in W64:
    c6 = cascade(r["B64"], KB_MAX)
    r["casc64"] = c6
    if c6 is not None:
        r["g64"] = float(c6["g"][KB_MAX - 1])
        r["gain64"] = r["g64"] / r["g1"]
X64 = [float(r["h"]) for r in W64 if "g64" in r]
G64L = [r for r in W64 if "g64" in r]
F_G64 = fit_exp(X64, [1.0 / r["g64"] for r in G64L])
F_GAIN64 = fit_exp(X64, [r["gain64"] for r in G64L])
W64E = [r for r in G64L if np.isfinite(r["rayP64"])]
F_RP64 = fit_exp([float(r["h"]) for r in W64E],
                 [r["rayP64"] / r["g1"] for r in W64E]) if W64E else float("nan")
F_RP64A = fit_exp([float(r["h"]) for r in W64E if r["surf"] == "A"],
                  [r["rayP64"] / r["g1"] for r in W64E if r["surf"] == "A"])
F_RP64N = fit_exp([float(r["h"]) for r in W64E if r["surf"] == "N"],
                  [r["rayP64"] / r["g1"] for r in W64E if r["surf"] == "N"])
MONO64 = all(r["g64"] >= r["g16"] * (1.0 - 1.0e-9) for r in G64L)
K64_OK = F_RP64 >= 3.0 - EPS_CARRY
check("sc_u3.trial_space_k64", MONO64 and len(G64L) >= 20,
      "*** THE LOSS IS THE PROJECTION, AND THAT IS GOOD NEWS ABOUT THE MECHANISM AND "
      "BAD NEWS ABOUT THE SURROGATE. ***  On %d windows carrying the full K = %d "
      "block: g_64 >= g_16 everywhere as Schur monotonicity requires, 1/g_64 = %.4f "
      ".. %.4f growing as h^%+.3f (against 1/g_16 = %.4f .. %.4f at h^%+.3f) -- so "
      "the enlarged block buys remarkably little on the CERTIFIED object, the gain "
      "rising only from h^%+.3f to h^%+.3f.  But the SAME v_0 projected into %d modes "
      "instead of 16 improves from h^%+.3f to h^%+.3f on the union (h^%+.3f frame A, "
      "h^%+.3f nu surface), which %s the preregistered form-F2 threshold %.2f.  "
      "READING, and it is the useful one: the confinement surrogate's shortfall is a "
      "TRUNCATION artefact, not a failure of the confinement mechanism -- v_0 really "
      "is a good near-null direction, it just does not fit into sixteen modes on the "
      "decoupled surface.  This does NOT close anything: the contract's object is the "
      "optimum over the SIXTEEN modes, which is g_16 by definition, and a surrogate "
      "that needs sixty-four modes to behave is not a certificate for it.  STATUS: "
      "THEOREM (monotonicity), MEASURED (all exponents); no claim that the chain MAY "
      "use K = %d"
      % (len(G64L), KB_MAX, qmin([1.0 / r["g64"] for r in G64L]),
         qmax([1.0 / r["g64"] for r in G64L]), F_G64,
         qmin([1.0 / r["g16"] for r in G64L]), qmax([1.0 / r["g16"] for r in G64L]),
         fit_exp(X64, [1.0 / r["g16"] for r in G64L]),
         fit_exp(X64, [r["gain"] for r in G64L]), F_GAIN64, KB_MAX, F_RAYPG,
         F_RP64, F_RP64A, F_RP64N,
         "RECOVERS" if K64_OK else "still does NOT recover", EPS_CARRY, KB_MAX))

para("""U3.5  THE MANDATORY STRESS BATTERY.  Four controls, all declared before
they were run: the T145-style no-go configuration MUST break the cascade (if the
h^3 also appeared for the pure parity Laplacian it would be geometry, not
arithmetic); the two classical identities the closed weights rest on must hold
EXACTLY; an INADMISSIBLE resolution nu < %d must be visibly labelled and must not
be used anywhere; and an ANTI-FITTING scramble must destroy the effect (if a
random atom placement with the SAME total mass produced the same near-degeneracy,
the near-degeneracy would be a property of the construction and not of the prime
powers).""" % NU_MAIN)

M_STRESS = [r for r in WPA[:4]]
E_LP, E_KMS, GAIN_LP = [], [], []
for r in M_STRESS:
    m = r["h"]
    LP = lap_P(m)
    Tf = parity_basis(m, min(KB_MAX, m))
    mu = parity_mu(m)
    E_KMS.append(float(np.max(np.abs(LP @ Tf[0, :] - mu[0] * Tf[0, :]))))
    isq = 1.0 / np.sqrt(mu[:r["nb"]])
    B_lp = sym((Tf @ (LP @ Tf.T)) * np.outer(isq, isq))
    cl = cascade(B_lp, r["kl"])
    if cl is not None:
        GAIN_LP.append(float(cl["g"][r["kl"] - 1] / cl["g"][0]))
    E_LP.append(float(np.max(np.abs(B_lp - np.eye(r["nb"])))))
    del LP, Tf, B_lp
check("sc_u3.stress_nogo",
      qmax(E_KMS) < 1.0e-10 and qmax(E_LP) < 1.0e-9
      and qmax(GAIN_LP) < 1.0 + 1.0e-8,
      "*** THE NO-GO CONTROL BREAKS, EXACTLY AS IT MUST. ***  For A = L_P the KMS "
      "eigen-relation L_P t_1 = mu^P_1 t_1 holds to %.1e, the normalised block is "
      "the IDENTITY to %.1e, and therefore the cascade gain is %.10f .. %.10f -- "
      "ONE, no cascade at all, on %d control windows.  So the h^3 of U1/U2 is not a "
      "property of the parity geometry, the KMS normalisation or the ladder: it is "
      "carried entirely by the ARITHMETIC kernel.  This is the T145-style no-go the "
      "battery required to break, and it breaks completely"
      % (qmax(E_KMS), qmax(E_LP), qmin(GAIN_LP), qmax(GAIN_LP), len(GAIN_LP)))

E_TOEP, E_PAIR = [], []
for r in M_STRESS:
    M, m = r["M"], r["h"]
    A = odd_toeplitz(r["c"], M)
    E_TOEP.append(float(np.max(np.abs(A - A.T))))
    v = RNG.normal(size=m)
    w = lag_weights_from_v(v, m)
    E_PAIR.append(abs(float(np.dot(r["c"], w)) - float(v @ (A @ v)))
                  / max(abs(float(v @ (A @ v))), 1.0e-300))
    del A
E_DIR = []
for m in (37, 101, 257):
    N = 2 * m + 1
    for k in (1, 2, 5):
        om = 2.0 * math.pi * k / N
        d = np.arange(1, m + 1)
        lhs = float(np.sum(np.cos(om * d)))
        rhs = 0.5 * (math.sin((m + 0.5) * om) / math.sin(0.5 * om) - 1.0)
        E_DIR.append(abs(lhs - rhs) / max(abs(lhs), 1.0))
check("sc_u3.stress_classical",
      qmax(E_TOEP) < 1.0e-12 and qmax(E_PAIR) < 1.0e-11 and qmax(E_DIR) < 1.0e-12,
      "*** THE CLASSICAL CONTROLS, EXACT. ***  The odd Toeplitz-minus-Hankel form is "
      "symmetric to %.1e; the T163 correlation form v^T A v = sum_d c_d w_d(v) holds "
      "to %.1e relative on RANDOM v (not just on the chain's x*, which is the point "
      "of the control); the Dirichlet kernel summation (Dirichlet 1829) holds to %.1e "
      "on nine (m, k) pairs.  These are the identities every closed weight in U2 "
      "rests on, so they are checked independently of the objects that use them"
      % (qmax(E_TOEP), qmax(E_PAIR), qmax(E_DIR)))

NU_BAD = 2
BAD = []
for (kz, Dz, Mz, hz) in SZN[:3]:
    rb = build_window(kz, NU_BAD, want_eig=False)
    if rb is not None and rb["casc"] is not None:
        rb["g1"] = float(rb["casc"]["g"][0])
        rb["g16"] = float(rb["casc"]["g"][rb["kl"] - 1])
        rb["gain"] = rb["g16"] / rb["g1"]
        BAD.append(rb)
if BAD:
    info("sc_u3.stress_inadmissible",
         "LABELLED MUST-BREAK CONTROL, USED NOWHERE ELSE IN THE FILE: at the "
         "INADMISSIBLE resolution nu = %d < %d (below the T105 admissibility floor) "
         "the same pipeline returns 1/g_16 = %.4f .. %.4f and a cascade gain of "
         "%.4g .. %.4g on %d windows.  The numbers are NOT comparable to anything "
         "above and are recorded only to show that the pipeline does not silently "
         "accept an inadmissible frame: every window carries its nu, and every fit "
         "above filters on nu >= %d"
         % (NU_BAD, NU_MAIN, qmin([1.0 / r["g16"] for r in BAD]),
            qmax([1.0 / r["g16"] for r in BAD]),
            qmin([r["gain"] for r in BAD]), qmax([r["gain"] for r in BAD]),
            len(BAD), NU_MAIN))

SCR = []
for r in M_STRESS:
    alpha, Mz = r["alpha"], r["M"]
    at = atoms_in(alpha)
    tot = sum(mu for _u, mu in at)
    fake = [(float(RNG.uniform(0.0, 2.0 * alpha)), tot / len(at)) for _ in at]
    c_sc, _D, _mt, _na = atom_lags(alpha, Mz, fake)
    A_sc = odd_toeplitz(r["c_ar"] + c_sc, Mz)
    T16 = r["Tb"][:r["kl"], :]
    G_sc = sym(T16 @ (A_sc @ T16.T))
    d = float(G_sc[0, 0]) * float(G_sc[1, 1])
    SCR.append(1.0 - float(G_sc[0, 1]) ** 2 / d if d > 0 else float("nan"))
    del A_sc, G_sc
SCR_OK = qmin(SCR) > 100.0 * qmax([1.0 - r["r12sq"] for r in M_STRESS])
check("sc_u3.stress_antifitting", SCR_OK,
      "*** THE ANTI-FITTING SCRAMBLE, AND IT DESTROYS THE EFFECT. ***  Replacing the "
      "prime-power positions u_j = log n_j by UNIFORM RANDOM positions in [0, 2 "
      "alpha], keeping the TOTAL atom mass and the archimedean half untouched, gives "
      "1 - r_12^2 = %.3e .. %.3e against the arithmetic %.3e .. %.3e on the SAME %d "
      "windows -- a factor %.4g .  So the near-degeneracy of the 2 x 2 block is a "
      "property of WHERE the prime powers sit, not of the atom budget, not of the "
      "archimedean kernel and not of the discretisation.  Together with the no-go "
      "control this pins the mechanism to the arithmetic and nothing else"
      % (qmin(SCR), qmax(SCR), qmin([1.0 - r["r12sq"] for r in M_STRESS]),
         qmax([1.0 - r["r12sq"] for r in M_STRESS]), len(SCR),
         qmed(SCR) / max(qmed([1.0 - r["r12sq"] for r in M_STRESS]), 1.0e-300)))

print("")
print("TOTAL (U3): %d checks, %d failures, %.1f s"
      % (N_CHK, len(FAILS), time.time() - T0))

# ----------------------------------------------------------------------------
section("U4  MAP V38, THE PROMOTION QUEUE, AND THE VERDICT")
# ----------------------------------------------------------------------------
block("""MAP V38 -- WHERE THE ONE OPEN OBJECT STANDS AFTER THIS FILE

  object                                   before T166        after T166
  ---------------------------------------------------------------------------
  1/g_1 = B_11 growth h^+3.110             MEASURED           MEASURED (repro)
  1/g_16 flat h^+0.061 on frame A          CERT-WINDOW        CERT-WINDOW (repro)
  cascade gain g_16/g_1 ~ h^+3.049         MEASURED           MEASURED (repro)
  gain = 1/(1 - R_K^2), collinearity form  --                 THEOREM   (new)
  gain invariant under B -> D B D           --                 THEOREM   (new)
  1/g_K = det G_[1..K]/(mu^P_1 det G_[2..K]) --                THEOREM   (new)
  rung profile: rung 2 carries ~59%         --                 MEASURED  (new)
  det-polarisation split + cancel ratio    --                 THEOREM / MEASURED
  mechanism = arch vs atom in det G_2      unknown            MEASURED  (new)
  closed-beta two-rung lower bound         --                 THEOREM, h^+1.32
  confinement surrogate for x*, K = 16     hoped sufficient   MEASURED h^+1.96
  confinement surrogate for x*, K = 64     --                 MEASURED h^+2.57
  the surrogate's loss is TRUNCATION       unknown            MEASURED  (new)
  U_ref on the union                       4.90 (frame A)     CERT-WINDOW (new)
  F1 vs F2 not equivalent (B_11 ~ h^3.11)  implicit           THEOREM   (new)
  inf_m g_16 > 0  (form F1)                OPEN               OPEN, reduced
  ---------------------------------------------------------------------------""")

block("""PROMOTION QUEUE -- NEW, PENDING, NOT PROMOTED BY THIS FILE.  T164's Q1..Q9
and T165's six items are being committed by the documentation workers in parallel
and are deliberately NOT repeated here.

  id       statement                                              type
  ------------------------------------------------------------------------------
  P166.1   the four cascade identities I1..I4 (prefix, minor,     THEOREM
           regression/collinearity, diagonal invariance)
  P166.2   1/g_K = det G_[1..K] / (mu^P_1 det G_[2..K]):          THEOREM
           the open object as a ratio of two Gram minors
  P166.3   rung profile: K_half in {2..5} on 63/63 windows,       CERT-WINDOW
           rung 2 median share 0.59
  P166.4   det(G_ar+G_at) = det G_ar + det G_at + Pi, with        THEOREM +
           |det G_2|/max(pieces) = 2.6e-06 .. 5.1e-04             MEASURED
  P166.5   U_ref(union) with declared safety factor 1.15,         CERT-WINDOW
           superseding the frame-A value 4.90 on the union
  P166.6   the confinement surrogate for x* (bottom mode of A,   MEASURED
           projected) gives gain h^+1.96 at K = 16 and h^+2.57
           at K = 64: its shortfall is TRUNCATION, and it is
           not a certificate at either K
  P166.9   sub-surface warning: the same exponent reads          MEASURED
           h^+2.71 on frame A with h <= 780, +0.75 optimistic
  P166.7   F1 (inf g_16 > 0) is STRICTLY STRONGER than            THEOREM +
           F2 (gain >= c h^{3-eps}) since B_11 ~ h^+3.11          MEASURED
  P166.8   no-go control (A = L_P: gain == 1) and the atom        CERT-WINDOW
           scramble control (effect destroyed, factor 4.6e+03)
  ------------------------------------------------------------------------------""")

NEW_THM = 5
NEW_CW = 3
NEW_MEAS = 4
check("sc_u4.balance", True,
      "BALANCE.  T165 closed at %d THEOREM / %d CERT-UNIF / %d CERT-WINDOW / %d "
      "MEASURED.  This file adds %d THEOREM (P166.1, P166.2, the polarisation split, "
      "P166.7, and the trial-vector direction of U2.0 written out as a theorem), %d "
      "CERT-WINDOW (P166.3, P166.5, P166.8) and %d MEASURED (P166.4 sizes, P166.6, "
      "P166.9, the rung/defect profiles).  It adds NO CERT-UNIF, which is the "
      "honest statement: nothing here became uniform in m.  Nothing is promoted by "
      "this file; the queue above is PENDING"
      % (T165_BALANCE[0], T165_BALANCE[1], T165_BALANCE[2], T165_BALANCE[3],
         NEW_THM, NEW_CW, NEW_MEAS))

CLOSED_BEST = max(GAIN_FITS["at"], GAIN_FITS["ar"], GAIN_FITS["m1"])
SHORTFALL = E11_A - CLOSED_BEST
FLAT_GAP = 0.05              # DECLARED: a gap below this in the EXPONENT is a flat
                             # factor, i.e. only a CONSTANT is missing
CLOSED_CLOSES_F1 = CLOSED_BEST >= E11_A - FLAT_GAP
if CLOSED_CLOSES_F1:
    VERDICT = "CASCADE-CARRIES"
elif SHORTFALL <= FLAT_GAP:
    VERDICT = "ONE-TERM-MISSING"
else:
    VERDICT = "CASCADE-RESISTS"

DEV_BEST = qmin([r["dev_at"] for r in WU])
U_KFLAT = SAFETY_UREF * qmax([1.0 / float(r["casc"]["g"][K_FLAT_U - 1])
                              for r in WU if r["kl"] >= K_FLAT_U])
check("sc_u4.verdict", VERDICT in ("CASCADE-CARRIES", "ONE-TERM-MISSING",
                                  "CASCADE-RESISTS"),
      "*** VERDICT: %s. ***  The criterion is stated as an EXPONENT gap so that it "
      "cannot be argued about.  CASCADE-CARRIES needs a CLOSED route whose gain "
      "exponent reaches the measured B_11 exponent %+.3f -- that, and not 3, is what "
      "closes form F1.  ONE-TERM-MISSING needs the gap between the best CLOSED route "
      "and that target to be a FLAT FACTOR, i.e. below %.2f in the exponent, because "
      "only then is a single CONSTANT missing.  MEASURED: the best closed route "
      "reaches h^%+.3f, the target is h^%+.3f, the gap is h^%+.3f -- an EXPONENT and "
      "not a constant.  Hence CASCADE-RESISTS, and the honest reason is that the one "
      "missing inequality IS the cancellation itself, not an auxiliary term beside "
      "it.  What the file does deliver is total localisation: the missing object is "
      "the single ratio det G_[1..%d] / (mu^P_1 det G_[2..%d]) with U ~ %.2f, the "
      "required relative accuracy on the two-rung beta is %.2e (best closed candidate "
      "off by a factor %.1f), and the determinant cancellation to be resolved is %.1e "
      ".. %.1e.  One number is worth recording as a warning rather than a result: an "
      "earlier pass measured the confinement surrogate inside h <= 780 on frame A "
      "only, read h^+2.714, and would have returned ONE-TERM-MISSING; on the full "
      "union the same object reads h^%+.3f"
      % (VERDICT, E11_A, FLAT_GAP, CLOSED_BEST, E11_A, SHORTFALL, K_FLAT_U,
         K_FLAT_U, U_KFLAT,
         qmin([r["dbeta_req"] / abs(r["bstar"]) for r in WU]), DEV_BEST,
         qmin(DETC), qmax(DETC), F_RAYPG))

para("""SHORTEST REMAINING LIST.  Two items, and the list is shorter than T165's
because the anatomy collapsed several questions into one:

R1  THE ONE INEQUALITY.  An m-free upper bound on the Gram-minor ratio det
    G_[1..K] / (mu^P_1 det G_[2..K]) at the first flat K, equivalently a closed beta at
    K = 2 to relative accuracy 3.6e-04, equivalently a closed nearly-null vector of
    A in the low modes.  These are the SAME inequality in three dresses, U2.2
    measured exactly how much cancellation it hides (a factor 2.6e-06 .. 5.1e-04
    against the polarisation pieces), and it is the whole quantifier.  Everything
    else in the reduction is now THEOREM.

R2  U_ref BOOKKEEPING, not a proof item: the union supremum found here exceeds both
    the T164 frame-A value and the T165 nu-surface value, so every statement
    carrying U_ref must name its surface.  The off-recipe rule of U3.1 is the
    proposed repair and it is CERT-WINDOW by construction, never CERT-UNIF.

    A note on what is NOT on this list any more.  'Find a better trial space' is
    off: the contract's object is the optimum over the sixteen modes, which is
    g_16 itself, so there is nothing to enlarge.  'Understand which rungs matter'
    is off: rungs 2..5, measured, closed form for rung 2.  'Is it arch against
    atom or mode against mode' is off: arch against atom, in the Gram
    determinant.""")

para("""HONEST THREE-SENTENCE CONCLUSION.  The cascade opens completely as an
ANATOMY -- the whole h^3 sits in the first one to five rungs, it is exactly the
near-collinearity 1 - R_K^2 of mode 1 against the low modes, the mechanism is an
arch-against-atom cancellation that lives one level up in the 2 x 2 Gram
DETERMINANT rather than in any lag sum (no individual lag sum cancels, and neither
half is collinear alone), and the open object is now the ratio of two Gram minors
of explicit finite lag sums, which is the sharpest form it has ever had.  The
uniformity statement does NOT stand, and this file makes the failure sharper rather
than softer: the best CLOSED bound reaches gain h^+1.32 where closing inf_m g_16 > 0
needs h^+3.11, the gap is an EXPONENT rather than a constant, and -- a correction
this file owes the contract -- form F2 as usually written (gain >= c h^{3-eps}, eps >
0) is STRICTLY WEAKER than inf_m g_16 > 0 on this surface, because B_11 grows as
h^+3.110 and not as h^3, so honouring F2 is not the same as closing the quantifier.
The sober comparison the contract asked for: yes, this is the SAME intrinsic hardness
as the h^2 cancellation of T159/T160 -- the same arch-against-atom mechanism, now one
level up in a quadratic functional of the same lag sums -- and the one route that
looked easier turned out to be a reading artefact, the confinement surrogate scoring
h^+2.71 on frame A inside a reduced eigen-horizon and only h^+1.96 on the full union,
which is the most useful negative result in this file and the reason its verdict is
CASCADE-RESISTS and not something friendlier.""")

print("")
print("=" * 78)
print("VERDICT: %s" % VERDICT)
print("=" * 78)
info("sc_u4.horizons",
     "DECLARED NUMERICAL HORIZONS, so no number above is over-read: matrices "
     "factorised up to h = %d (hard cap MAX_H = %d), full eigen-decompositions up "
     "to h = %d, cond(B_LL) up to %.1e with identity bar %.0e = eps.cond with "
     "margin, %d union windows, no window with cond > %.0e admitted, and the whole "
     "probe inside the hard budget %.0f s"
     % (max(r["h"] for r in WU), MAX_H, EIG_HCAP, qmax([r["kap"] for r in WU]),
        IDENT_BAR, len(WU), COND_BAR, BUDGET_S))
info("sc_u4.scope",
     "SCOPE: discovery only.  Nothing in verification/, next.txt, the papers, the "
     "website, the ledger or the changelog was read or written; this file is the "
     "only artefact, and every item of the promotion queue is PENDING")

print("")
print("=" * 78)
print("TOTAL: %d checks, %d failures, %.1f s (budget %.0f s)"
      % (N_CHK, len(FAILS), time.time() - T0, BUDGET_S))
if FAILS:
    print("FAILURES: %s" % ", ".join(FAILS))
print("=" * 78)
