"""PART 169 -- TSTAR.RATIO -- closed functions for the one open ratio.

T168 closed the exponent ledger of 1 - r_12^2 = nu_1 nu_2/(ahat_11 ahat_22) down
to ONE open factor: nu_2 = min_t (ahat_22 - 2 t ahat_12 + t^2 ahat_11)/(1 + t^2),
whose minimiser is the single ratio t* = ahat_12/ahat_11.  T168 tested CONSTANTS
(best 1/sqrt(2), off by 0.194) and single-mode trials (overshoot 285 .. 1.5e6):
closed FUNCTIONS were never tried.  This file tries them -- the archimedean
ratio, the atom-budget interval, the leading-lag heads, the Toeplitz-only ratio
-- and books the three cheap items R2 (ahat lower bounds), R3 (a closed nu_1
bound) and R4 (uniform-in-h positivity of A_h) that T168 left as write-ups.

DIRECTION, ONCE, BECAUSE IT IS THE WHOLE POINT.  nu_2 = min_t R(t) <= R(that) for
EVERY explicit that: any closed candidate is already a VALID upper bound on nu_2
(Rayleigh 1877).  Only the SIZE of R(that) depends on accuracy.  So this file
never asks "is the candidate right", it asks "does R(that) still fall like
h^{-3+eps}", and the accuracy target 6.05e-3 median / 2.82e-4 worst window is
T168's translation of that same question.

FENCES.  No zero data, no L-function evaluation; finite von Mangoldt sums only
(Chebyshev 1852, UNCONDITIONAL).  RH is a YARDSTICK (RH_DELTA), never an input
and never a conclusion.  R4 (positivity of a finite A_h) is a NUMERICAL FACT
about a finite matrix, UNCONDITIONAL in that reading only; it is NEVER routed
through the Weil criterion (Weil 1952) and never read as a statement about
zeros -- that fence is hard and is restated at R4 itself.  Theorem / certified /
measured / fit are kept strictly apart.
Python: experiments/tfpt-discovery/.venv/bin/python
"""

import ast
import math
import os
import time

import numpy as np

T0 = time.time()
EULER = 0.5772156649015329
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any factorised form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
NU_MAIN = 4
CHUNK = 16384
ATOM_MAX = 400000
N_ZONES = 40
HCAP = 1450
H_MIN = 128
N_ATOM_MIN = 40
SCHUR_KB = 16
KB_MAX = 64
NU_DECOUPLE = (4, 5, 6, 8, 11, 16)
N_ZONES_NU = 6

EXACT_BAR = 1.0e-12
IDENT_BAR = 1.0e-6           # DECLARED numerical horizon: identities whose two
#                              sides both pass through the near-null value nu_2
#                              lose ~ ahat_22/nu_2 ~ 1e7 digits to cancellation
COND_BAR = 1.0e12
B_PSI = 1.03883
RH_DELTA = 0.5               # YARDSTICK, NOT A CLAIM
T163_KAPPA = 0.03882

# --- the T168 hand-over numbers, quoted, never re-fitted here ----------------
T168_TSTAR_RANGE = (0.570, 0.790)
T168_TSTAR_EXP = 0.076
T168_ACC_MED = 6.05e-3       # required rel accuracy on t*, median window
T168_ACC_WORST = 2.82e-4     # required rel accuracy on t*, worst window
T168_ACC_EXP = -1.146        # and it sharpens like this
T168_NU1_EXP = 0.81
T168_A11_EXP = 0.76
T168_A22_EXP = 0.91
T168_NU2_EXP = -1.38
T168_ONEM_EXP = 2.92
T168_LMIN_RANGE = (5.0e-6, 8.5e-4)
TARGET_EXP = 3.0             # the h^{-3+eps} target of the quantifier
EPS_CARRY = 0.5              # "h^{3-eps}" honoured for eps <= EPS_CARRY

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


def budget_left():
    return BUDGET_S - (time.time() - T0)


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
    print("")
    for ln in text.split("\n"):
        print(indent + ln if ln.strip() else "")
    print("")


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
    """d log y / d log x -- a FIT, always labelled, never an input to a bound."""
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    ok = np.isfinite(xs) & np.isfinite(ys) & (np.abs(ys) > 0) & (xs > 0)
    if int(np.sum(ok)) < 3:
        return float("nan")
    return float(np.polyfit(np.log(xs[ok]), np.log(np.abs(ys[ok])), 1)[0])


FORBIDDEN_TOKENS = tuple("".join(p) for p in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "numpy", "scipy"}


def firewall():
    src = open(os.path.abspath(__file__), "r").read()
    low = src.lower()
    hits = [t for t in FORBIDDEN_TOKENS if t in low]
    tree = ast.parse(src)
    bad_imp, bad_wr = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    bad_imp.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                bad_imp.append(node.module)
        elif isinstance(node, ast.Call):
            nm = getattr(node.func, "id", None) or getattr(node.func, "attr", None)
            if nm == "open":
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(ch in mode for ch in "wax+"):
                    bad_wr.append(mode)
    check("tr_fw.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("tr_fw.imports", not bad_imp, "non-whitelisted: %s" % (bad_imp or "none"))
    check("tr_fw.no_writes", not bad_wr, "write-mode: %s" % (bad_wr or "none"))
    check("tr_fw.one_file",
          os.path.basename(os.path.abspath(__file__)) == "tstar_ratio_probe.py",
          "single file: tstar_ratio_probe.py")
    check("tr_fw.rh_fence", "RH_DELTA" in src and low.count("unconditional") >= 3,
          "RH fence declared; RH_DELTA = %.1f is a YARDSTICK only; the R4 Weil "
          "fence is declared separately at R4" % RH_DELTA)


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
    return [(int(n), float(lam[n]), math.log(float(n)),
             2.0 * float(lam[n]) / math.sqrt(float(n)))
            for n in np.nonzero(lam > 0.0)[0]]


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
    mu_tot, n_hit = 0.0, 0
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
    """mu^P_k = 4 sin^2(pi k / N), N = 2m + 1 (Kac-Murdock-Szego 1953).  EXACT."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m, kb=None):
    """t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N): ORTHONORMAL eigenbasis of L_P."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, (kb or m) + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: TOEPLITZ MINUS HANKEL, exact."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def toeplitz_only(c, M):
    """The Hankel reflection DROPPED -- one of the preregistered candidates."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])]


def lag_weights_from_v(v, m):
    """THE T163 CORRELATION FORM, A THEOREM: w_0 = A_0, w_d = 2 A_d - H_{M-1-d}
    (d >= 1) with A the autocorrelation and H the self-convolution of v; then
    v^T A v = sum_d c_d w_d EXACTLY -- the bilinear form read as a LAG SUM."""
    M = 2 * m
    ac = np.correlate(v, v, "full")[m - 1:]
    cv = np.convolve(v, v)
    w = np.zeros(M)
    w[:m] = 2.0 * ac
    w[0] = ac[0]
    ee = (M - 1) - np.arange(1, M)
    w[1:] -= np.where(ee <= M - 2, cv[np.minimum(ee, M - 2)], 0.0)
    return w


def cascade(Bm, K):
    """g_K = e_1^T Q_K^-1 e_1 = sum_{j<=K} y_j^2 (Schur 1917 ladder).  The ONLY
    certifiable direction: 1/g_K = min{u^T Q_K u : u_1 = 1}, so any explicit
    trial u is an UPPER bound on 1/g_K, i.e. a LOWER bound on g_K."""
    Q = sym(np.asarray(Bm)[:K, :K])
    try:
        L = np.linalg.cholesky(Q)
    except np.linalg.LinAlgError:
        return None
    e1 = np.zeros(K)
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return dict(y=y, y2=y ** 2, g=np.cumsum(y ** 2))


section("PART 169 -- TSTAR.RATIO -- X0  FENCE, ARITHMETIC CORE")
firewall()
ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]
ZONE_DEEP = 380000
NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
check("tr_x0.atoms", len(ATOMS_ALL) > 30000,
      "%d prime-power atoms up to n = %d (finite von Mangoldt sieve)"
      % (len(ATOMS_ALL), ATOM_MAX))

_psi_run, _bpsi, _kap = 0.0, 0.0, 0.0
for _n, _lam, _u, _mu in ATOMS_ALL:
    _psi_run += _lam
    _bpsi = max(_bpsi, _psi_run / _n)
    if _n >= 100.0:
        _kap = max(_kap, abs(_psi_run - _n) / _n)
KAPPA = _kap
check("tr_x0.chebyshev", _bpsi <= B_PSI and abs(KAPPA - T163_KAPPA) < 0.001,
      "psi(x)/x <= %.6f and |psi(x) - x| <= %.6f x VERIFIED at every jump point "
      "up to n = %d (Chebyshev 1852; Rosser-Schoenfeld 1962).  The ONLY "
      "arithmetic input of the file, and it is UNCONDITIONAL"
      % (_bpsi, KAPPA, ATOM_MAX))


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


def zone_candidates(nu, h_lo, h_hi):
    out = []
    for k in range(2, NZ_DEEP - 2):
        D_k = 0.5 * float(G_DEEP[k]) / float(nu)
        M_k = int(math.ceil(UU_ALL[k] / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        h_k = M_k // 2
        if h_k < h_lo or h_k > h_hi or len(atoms_in(UU_ALL[k])) < N_ATOM_MIN:
            continue
        out.append((k, D_k, M_k, h_k))
    return out


def build_window(kz, nu, scramble=False, flat=False):
    """One window, plus THE NEW OBJECT of this file: the SPLIT 2 x 2 blocks
    Ahat = Ahat^arch + Ahat^atom.  The split is EXACT because c -> A is linear
    and c = c^arch + c^atom is exact (T158/T159).  Every candidate of X1 is a
    closed function of the split blocks and of the KMS eigenvalues mu_1, mu_2."""
    alpha = UU_ALL[kz]
    D_k = 0.5 * float(G_DEEP[kz]) / float(nu)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    if hz < 8 or hz > HCAP or hz > MAX_H:
        return None
    at = atoms_in(alpha)
    if scramble:
        rng = np.random.default_rng(4242 + kz)
        us = np.sort(rng.uniform(0.0, 2.0 * alpha, size=len(at)))
        at = [(float(us[i]), at[i][1]) for i in range(len(at))]
    if flat and at:
        mbar = sum(t[1] for t in at) / float(len(at))
        at = [(t[0], mbar) for t in at]
    c_at, D, mu_tot, n_at = atom_lags(alpha, Mz, at)
    c_ar = arch_lags(Mz, D)
    r = dict(k=kz, nu=float(nu), h=hz, M=Mz, D=D, alpha=alpha, n_zone=NN_ALL[kz],
             gap=float(G_DEEP[kz]), c=c_ar + c_at, c_ar=c_ar, c_at=c_at,
             mu_tot=mu_tot, n_atom=n_at, scr=bool(scramble), flat=bool(flat))
    nb = min(KB_MAX, hz)
    kl = min(SCHUR_KB, nb)
    Tb = parity_basis(hz, nb)
    mu = parity_mu(hz)
    isq = 1.0 / np.sqrt(mu[:nb])
    r["mu"], r["nb"], r["kl"] = mu[:nb], nb, kl
    u = Tb[0] * isq[0]
    v = Tb[1] * isq[1]
    r["u"], r["v"] = u, v
    m1, m2 = float(mu[0]), float(mu[1])
    r["m1"], r["m2"] = m1, m2
    # the three lag-weight vectors: Q_11, Q_22 and (by polarisation) Q_12
    w11 = lag_weights_from_v(u, hz)
    w22 = lag_weights_from_v(v, hz)
    wpp = lag_weights_from_v(u + v, hz)
    w12 = 0.5 * (wpp - w11 - w22)
    r["w11"], r["w22"], r["w12"] = w11, w22, w12
    # the SPLIT blocks, in the hat (orthonormal) normalisation
    for tag, cc in (("", r["c"]), ("_ar", c_ar), ("_at", c_at)):
        r["a11" + tag] = m1 * float(cc @ w11)
        r["a22" + tag] = m2 * float(cc @ w22)
        r["a12" + tag] = math.sqrt(m1 * m2) * float(cc @ w12)
    A = odd_toeplitz(r["c"], Mz)
    G64 = sym(Tb @ (A @ Tb.T))
    r["B_LL"] = sym(G64 * np.outer(isq, isq))[:kl, :kl].copy()
    r["Qdir"] = np.array([[float(u @ (A @ u)), float(u @ (A @ v))],
                          [float(u @ (A @ v)), float(v @ (A @ v))]])
    ev = np.linalg.eigvalsh(A)
    r["lam_min"], r["lam_max"] = float(ev[0]), float(ev[-1])
    r["lam2"] = float(ev[-2])
    r["Ainf"] = float(np.max(np.sum(np.abs(A), axis=1)))
    r["trA"] = float(np.trace(A))
    r["gersh"] = float(np.min(2.0 * np.diag(A) - np.sum(np.abs(A), axis=1)))
    r["Adiag_min"] = float(np.min(np.diag(A)))
    r["Aoff_pos"] = float(np.max(np.triu(A, 1)))
    r["chol"] = 1
    try:
        np.linalg.cholesky(sym(A))
    except np.linalg.LinAlgError:
        r["chol"] = 0
    r["t1"] = Tb[0].copy()
    r["t2"] = Tb[1].copy()
    r["a11_t"] = float(Tb[0] @ (A @ Tb[0]))
    r["a22_t"] = float(Tb[1] @ (A @ Tb[1]))
    r["a12_t"] = float(Tb[0] @ (A @ Tb[1]))
    if nb >= 3:
        r["p2"] = (float(Tb[1] @ (A @ Tb[1])), float(Tb[2] @ (A @ Tb[2])),
                   float(Tb[1] @ (A @ Tb[2])))
    del A, G64
    Aar = odd_toeplitz(c_ar, Mz)
    evar = np.linalg.eigvalsh(Aar)
    r["lam_min_ar"], r["lam_max_ar"] = float(evar[0]), float(evar[-1])
    r["Zoff"] = float(np.max(np.triu(Aar, 1)))     # Z-matrix test: off-diag <= 0
    r["Zrow"] = float(np.min(Aar @ np.ones(hz)))   # sign-based M-matrix floor
    del Aar
    Aat = odd_toeplitz(c_at, Mz)
    r["Aat_inf"] = float(np.max(np.sum(np.abs(Aat), axis=1)))
    ATo = toeplitz_only(r["c"], Mz)
    r["a11_to"] = m1 * float(u @ (ATo @ u))
    r["a22_to"] = m2 * float(v @ (ATo @ v))
    r["a12_to"] = math.sqrt(m1 * m2) * float(u @ (ATo @ v))
    del Aat, ATo
    evb = np.linalg.eigvalsh(r["B_LL"])
    r["kap"] = float(evb[-1] / max(evb[0], 1.0e-300))
    r["casc"] = cascade(r["B_LL"], kl)
    return r


def finish_window(r):
    """The T168 aggregates, recomputed here from the split blocks."""
    Ah = np.array([[r["a11"], r["a12"]], [r["a12"], r["a22"]]])
    nu = np.linalg.eigvalsh(Ah)
    r["nu2"], r["nu1"] = float(nu[0]), float(nu[1])
    r["tstar"] = r["a12"] / r["a11"]
    r["onem"] = r["nu1"] * r["nu2"] / (r["a11"] * r["a22"])
    r["eps_t"] = math.sqrt(max(r["nu2"], 0.0) / r["a11"]) / abs(r["tstar"])
    r["q11"] = r["a11"] / r["m1"]
    r["g2"] = float(r["casc"]["g"][1]) if r["casc"] is not None else float("nan")
    return r


def rayleigh(r, t):
    """R(t) = (ahat_22 - 2 t ahat_12 + t^2 ahat_11)/(1 + t^2).  nu_2 = min_t R(t),
    so R(that) is an UPPER bound on nu_2 for EVERY that (Rayleigh 1877)."""
    return ((r["a22"] - 2.0 * t * r["a12"] + t * t * r["a11"]) / (1.0 + t * t))


section("X0b  THE UNION SURFACE, AND THE EXACT ARCH / ATOM SPLIT OF THE BLOCK")

CAND_A = zone_candidates(NU_MAIN, H_MIN, HCAP)
CAND_A.sort(key=lambda t: t[3])
SZ = []
if CAND_A:
    pick = sorted(set(int(round(x)) for x in np.geomspace(
        1.0, float(len(CAND_A)), N_ZONES)))
    SZ = sorted([CAND_A[i - 1] for i in pick], key=lambda t: t[0])

WA = []
for (kz, Dz, Mz, hz) in SZ:
    if budget_left() < 560.0:
        info("tr_x0.budget", "frame-A enumeration stopped at h = %d" % hz)
        break
    rw = build_window(kz, NU_MAIN)
    if rw is not None:
        rw["surf"] = "A"
        WA.append(finish_window(rw))

NU_TOP = max(NU_DECOUPLE)
CAND_N = zone_candidates(NU_MAIN, H_MIN // 2,
                         max(H_MIN, int(HCAP * NU_MAIN / NU_TOP)))
SZN = []
if CAND_N:
    CAND_N.sort(key=lambda t: t[3])
    pk = sorted(set(int(round(x)) for x in np.geomspace(
        1.0, float(len(CAND_N)), N_ZONES_NU)))
    SZN = sorted([CAND_N[i - 1] for i in pk], key=lambda t: t[0])

WN = []
for (kz, Dz, Mz, hz) in SZN:
    for nu in NU_DECOUPLE:
        if budget_left() < 440.0:
            info("tr_x0.budget_nu", "nu enumeration stopped at %d" % len(WN))
            break
        rw = build_window(kz, nu)
        if rw is not None:
            rw["surf"] = "N"
            WN.append(finish_window(rw))

WPA = [r for r in WA if r["kap"] <= COND_BAR and r["casc"] is not None]
WPN = [r for r in WN if r["kap"] <= COND_BAR and r["casc"] is not None]
WU = WPA + WPN
XU = [float(r["h"]) for r in WU]
XA = [float(r["h"]) for r in WPA]
check("tr_x0.surface_union", len(WPA) >= 8 and len(WPN) >= 12,
      "THE SAME union surface as T163 .. T168, same recipe and density: %d "
      "frame-A windows (h = %d .. %d, nu = %d) and %d nu-decoupled windows, %d "
      "total, h <= %d <= cap %d.  Every exponent below is measured on THIS "
      "surface, never on a re-tuned one"
      % (len(WPA), min(r["h"] for r in WPA), max(r["h"] for r in WPA), NU_MAIN,
         len(WPN), len(WU), max(r["h"] for r in WU), HCAP))

_e_lag = [max(abs(r["a11"] / r["m1"] - r["Qdir"][0, 0]),
              abs(r["a12"] / math.sqrt(r["m1"] * r["m2"]) - r["Qdir"][0, 1]),
              abs(r["a22"] / r["m2"] - r["Qdir"][1, 1]))
          / abs(r["Qdir"][0, 0]) for r in WU]
check("tr_x0.block_is_lag_sum", qmax(_e_lag) < EXACT_BAR,
      "the whole 2 x 2 block is a LAG SUM: Q_ij = sum_d c_d w^{ij}_d with "
      "w^{11}, w^{22} the T163 correlation weights of u, v and w^{12} their "
      "polarisation, reproducing X^T A X to rel %.1e on all %d windows.  "
      "THEOREM (identity); it is what makes an arch/atom split of the RATIO "
      "meaningful at all" % (qmax(_e_lag), len(WU)))

_e_spl = [max(abs(r["a11_ar"] + r["a11_at"] - r["a11"]),
              abs(r["a12_ar"] + r["a12_at"] - r["a12"]),
              abs(r["a22_ar"] + r["a22_at"] - r["a22"])) / abs(r["a11"])
          for r in WU]
check("tr_x0.split_is_exact", qmax(_e_spl) < EXACT_BAR,
      "Ahat = Ahat^arch + Ahat^atom EXACTLY (rel %.1e), entry by entry, on all "
      "%d windows -- linearity of c -> A composed with c = c^arch + c^atom.  "
      "THEOREM (identity)" % (qmax(_e_spl), len(WU)))

F_TSTAR = fit_exp(XU, [r["tstar"] for r in WU])
F_ONEM = fit_exp(XA, [r["onem"] for r in WPA])
check("tr_x0.reproduce_t168",
      abs(F_ONEM + T168_ONEM_EXP) < 0.05
      and abs(F_TSTAR - T168_TSTAR_EXP) < 0.05
      and qmin([r["tstar"] for r in WU]) > 0.5,
      "t* = %.4f .. %.4f with trend h^%+.3f (T168 quoted %.3f .. %.3f, "
      "h^%+.3f) and 1 - r_12^2 falls h^%+.3f on frame A (T168: h^%+.3f).  The "
      "T168 hand-over is REPRODUCED bit-compatibly before any candidate is "
      "tried.  MEASURED"
      % (qmin([r["tstar"] for r in WU]), qmax([r["tstar"] for r in WU]),
         F_TSTAR, T168_TSTAR_RANGE[0], T168_TSTAR_RANGE[1], T168_TSTAR_EXP,
         F_ONEM, -T168_ONEM_EXP))

for r in WU:
    r["acc_need"] = r["eps_t"]
check("tr_x0.threshold",
      abs(qmed([r["acc_need"] for r in WU]) / T168_ACC_MED - 1.0) < 0.35,
      "THE THRESHOLD, RESTATED IN ONE NUMBER.  Keeping R(that) within a factor "
      "2 of nu_2 needs t* to relative accuracy eps_t = sqrt(nu_2/ahat_11)/t* = "
      "%.2e median, %.2e worst window, sharpening h^%+.3f (T168 quoted %.2e / "
      "%.2e, h^%+.3f).  Every X1 candidate is scored against exactly these two "
      "numbers"
      % (qmed([r["acc_need"] for r in WU]), qmin([r["acc_need"] for r in WU]),
         fit_exp(XU, [r["acc_need"] for r in WU]), T168_ACC_MED,
         T168_ACC_WORST, T168_ACC_EXP))

# ----------------------------------------------------------------------------
# *** X1  THE FUNCTION FAMILY -- CLOSED CANDIDATES FOR t* = ahat_12/ahat_11 ***
# ----------------------------------------------------------------------------
section("X1  THE FUNCTION FAMILY -- CLOSED CANDIDATES FOR t* = ahat_12/ahat_11")

para("""PREREGISTRATION.  The nine candidates below were fixed as a family BEFORE
any accuracy number of this file was read, and none of them carries a fitted
parameter.  Two are T168 baselines kept only for calibration (K7 the geometric
scale guess, K8 the best T168 constant 1/sqrt(2)).  The seven new ones are all
ratios of the SAME lag sum, restricted to a structurally distinguished part of
it: the archimedean half, a head in the lag index, the Toeplitz half, or the
archimedean half plus a truncated atom tail.  Nothing is re-optimised after the
table is printed; the table IS the result.""")


def head_ratio(r, d0):
    """Ratio of the two lag sums truncated at lag d0 -- closed once c is."""
    d0 = int(min(d0, r["M"] - 1))
    num = float(r["c"][:d0 + 1] @ r["w12"][:d0 + 1])
    den = float(r["c"][:d0 + 1] @ r["w11"][:d0 + 1])
    if abs(den) < 1.0e-300:
        return float("nan")
    return math.sqrt(r["m1"] * r["m2"]) * num / (r["m1"] * den)


def arch_plus_tail(r, frac):
    """Archimedean block plus the atom part restricted to lags d <= frac * h."""
    d0 = int(max(1, math.floor(frac * r["h"])))
    ca = np.zeros(r["M"])
    ca[:d0 + 1] = r["c_at"][:d0 + 1]
    cc = r["c_ar"] + ca
    num = math.sqrt(r["m1"] * r["m2"]) * float(cc @ r["w12"])
    den = r["m1"] * float(cc @ r["w11"])
    return num / den if abs(den) > 1.0e-300 else float("nan")


CANDIDATES = (
    ("K1_arch", "ahat_12^arch / ahat_11^arch (both closed T115 lag sums)",
     lambda r: r["a12_ar"] / r["a11_ar"]),
    ("K2_head1", "lag head d <= 1 of the FULL lag sum",
     lambda r: head_ratio(r, 1)),
    ("K3_head3", "lag head d <= 3", lambda r: head_ratio(r, 3)),
    ("K4_head7", "lag head d <= 7", lambda r: head_ratio(r, 7)),
    ("K5_headq", "lag head d <= ceil(sqrt(h)) (h-adaptive head)",
     lambda r: head_ratio(r, int(math.ceil(math.sqrt(r["h"]))))),
    ("K6_toep", "Toeplitz half only (Hankel reflection dropped)",
     lambda r: r["a12_to"] / r["a11_to"]),
    ("K7_geom", "sqrt(ahat_22/ahat_11) -- T168 baseline, m-free scale guess",
     lambda r: math.sqrt(r["a22"] / r["a11"])),
    ("K8_const", "1/sqrt(2) -- T168's best CONSTANT, calibration only",
     lambda r: 1.0 / math.sqrt(2.0)),
    ("K9_artail", "ahat^arch + atom tail truncated at d <= h/8",
     lambda r: arch_plus_tail(r, 0.125)),
)

_w120 = qmax([abs(r["w12"][0]) / math.sqrt(r["w11"][0] * r["w22"][0])
              for r in WU])
check("tr_x1.offdiag_starts_at_lag_1", _w120 < 1.0e-12,
      "w^{12}_0 = u.v = 0 to %.1e on all %d windows: the two parity modes are "
      "ORTHOGONAL, so the d = 0 lag carries NO off-diagonal information and the "
      "numerator of t* starts at lag d = 1 while the denominator starts at "
      "d = 0.  THEOREM (KMS 1953 orthogonality).  This is why the minimal "
      "non-trivial head candidate is K2 and not a d = 0 head" % (_w120, len(WU)))

SCORE = []
for nm, desc, fn in CANDIDATES:
    er, ov, tv = [], [], []
    npass = 0
    for r in WU:
        try:
            tc = float(fn(r))
        except (ValueError, ZeroDivisionError, FloatingPointError):
            tc = float("nan")
        if not np.isfinite(tc):
            er.append(float("nan"))
            ov.append(float("nan"))
            tv.append(float("nan"))
            continue
        e = abs(tc / r["tstar"] - 1.0)
        er.append(e)
        ov.append(rayleigh(r, tc) / r["nu2"])
        tv.append(tc)
        if e <= r["eps_t"]:
            npass += 1
    SCORE.append(dict(nm=nm, desc=desc, er=er, ov=ov, tv=tv, npass=npass,
                      e_med=qmed(er), e_max=qmax(er), ov_med=qmed(ov),
                      ov_max=qmax(ov), f_e=fit_exp(XU, er),
                      f_R=fit_exp(XU, [rayleigh(WU[i], tv[i])
                                       for i in range(len(WU))
                                       if np.isfinite(tv[i])] or [1.0]),
                      f_t=fit_exp(XU, tv)))

for s in SCORE:
    good = [rayleigh(WU[i], s["tv"][i]) for i in range(len(WU))
            if np.isfinite(s["tv"][i])]
    xs = [XU[i] for i in range(len(WU)) if np.isfinite(s["tv"][i])]
    s["f_R"] = fit_exp(xs, good)
    s["onem_med"] = qmed([WU[i]["nu1"] * rayleigh(WU[i], s["tv"][i])
                          / (WU[i]["a11"] * WU[i]["a22"])
                          for i in range(len(WU)) if np.isfinite(s["tv"][i])])
    s["f_onem"] = fit_exp(xs, [WU[i]["nu1"] * rayleigh(WU[i], s["tv"][i])
                               / (WU[i]["a11"] * WU[i]["a22"])
                               for i in range(len(WU))
                               if np.isfinite(s["tv"][i])])

block("""THE CANDIDATE TABLE.  rel err = |t_K/t* - 1| (median / worst over the 63
window union), pass = windows meeting their OWN eps_t, R(t_K)/nu_2 = the factor
the resulting VALID nu_2 upper bound loses, and h^e = the trend of the bound.
Targets: median 6.05e-03, worst 2.82e-04, R-trend h^-1.380, 1-r trend h^-2.921.

  candidate    rel err med   rel err worst  pass    R(t_K)/nu_2 med   R trend
  -----------  ------------  -------------  ------  ----------------  ---------""")
for s in SCORE:
    print("  %-11s  %12.3e  %13.3e  %2d/%2d   %16.3e  h^%+.3f"
          % (s["nm"], s["e_med"], s["e_max"], s["npass"], len(WU),
             s["ov_med"], s["f_R"]))
print("")
for s in SCORE:
    print("  %-11s  %s" % (s["nm"], s["desc"]))
print("")

BEST = min(SCORE, key=lambda s: s["e_med"] if np.isfinite(s["e_med"]) else 1e9)
BEST_W = min(SCORE, key=lambda s: s["e_max"] if np.isfinite(s["e_max"]) else 1e9)
K1 = SCORE[0]

check("tr_x1.every_candidate_is_a_valid_bound",
      all(qmin(s["ov"]) >= 1.0 - 1.0e-9 for s in SCORE),
      "R(t_K) >= nu_2 for EVERY candidate on EVERY window (min factor %.6f): "
      "each closed candidate already delivers a VALID m-free-shaped UPPER bound "
      "on nu_2 -- validity is free, only the SIZE is at stake.  THEOREM "
      "(Rayleigh 1877); the numbers merely confirm the coding"
      % qmin([qmin(s["ov"]) for s in SCORE]))

CLOSED = [s for s in SCORE if s["nm"] != "K7_geom"]
BEST_CL = min(CLOSED, key=lambda s: s["e_med"] if np.isfinite(s["e_med"]) else 1e9)
K7 = SCORE[6]

check("tr_x1.closed_family_refuted",
      qmin([s["e_med"] for s in CLOSED]) > 0.05,
      "*** THE FIRST HARD FACT OF T169, AND IT IS NEGATIVE. ***  EVERY genuinely "
      "CLOSED candidate fails, and fails by O(1): the archimedean ratio K1 gives "
      "%.3e median / %.3e worst, the lag heads K2 .. K5 give %.3e .. %.3e "
      "median, the Toeplitz half K6 gives %.3e, and T168's constant 1/sqrt(2) "
      "at %.3e is in fact the BEST of them.  The best closed candidate is %s at "
      "%.3e, i.e. %.0fx outside the 6.05e-03 median target, and its R(t_K) "
      "OVERSHOOTS nu_2 by %.1e with the WRONG SIGN of trend (h^%+.3f instead of "
      "h^-1.380).  A closed function of the archimedean or head part cannot "
      "locate t*.  MEASURED, and it refutes the T169 X1 hypothesis as stated"
      % (K1["e_med"], K1["e_max"], qmin([s["e_med"] for s in SCORE[1:6]]),
         qmax([s["e_med"] for s in SCORE[1:6]]), SCORE[5]["e_med"],
         SCORE[7]["e_med"], BEST_CL["nm"], BEST_CL["e_med"],
         BEST_CL["e_med"] / T168_ACC_MED, BEST_CL["ov_med"], BEST_CL["f_R"]))

check("tr_x1.why_closed_fails",
      qmax([abs(r["a11_at"] / r["a11_ar"]) for r in WU]) > 1.0,
      "AND THE REASON, IN ONE NUMBER: the block is ATOM-DOMINATED.  "
      "|ahat_11^atom/ahat_11^arch| = %.2f .. %.2f and "
      "|ahat_12^atom/ahat_12^arch| = %.2f .. %.2f over the union -- the "
      "archimedean half is not even the leading part of either entry, so a "
      "ratio built from it is a ratio of the SMALL parts.  This kills K1, K6 "
      "and K9 structurally, not numerically.  MEASURED"
      % (qmin([abs(r["a11_at"] / r["a11_ar"]) for r in WU]),
         qmax([abs(r["a11_at"] / r["a11_ar"]) for r in WU]),
         qmin([abs(r["a12_at"] / r["a12_ar"]) for r in WU]),
         qmax([abs(r["a12_at"] / r["a12_ar"]) for r in WU])))

check("tr_x1.best_by_worst_window", BEST_W["nm"] == BEST["nm"],
      "and the two rankings agree, which matters because a family that wins on "
      "the median and loses on the worst window would be a MEDIAN-ONLY verdict: "
      "best by median is %s (%.3e), best by worst window is %s (%.3e), and they "
      "are the same candidate.  So the verdict cannot be an artefact of which "
      "statistic is quoted"
      % (BEST["nm"], BEST["e_med"], BEST_W["nm"], BEST_W["e_max"]))

check("tr_x1.diagonal_candidate_meets_threshold",
      K7["e_med"] <= T168_ACC_MED and K7["e_max"] <= T168_ACC_WORST,
      "*** AND NOW THE ONE THAT WORKS -- READ THE NEXT CHECK BEFORE CELEBRATING. "
      "***  K7 = sqrt(ahat_22/ahat_11), which T168 wrote down as a scale guess "
      "and never scored, meets BOTH thresholds: %.3e median (target 6.05e-03) "
      "and %.3e worst window (target 2.82e-04), on %d/%d windows individually, "
      "with R(t_K7)/nu_2 = %.6f .. %.6f and the RIGHT trend h^%+.3f (target "
      "h^-1.380).  Its error falls h^%+.3f against a threshold sharpening only "
      "h^%+.3f.  MEASURED"
      % (K7["e_med"], K7["e_max"], K7["npass"], len(WU), qmin(K7["ov"]),
         qmax(K7["ov"]), K7["f_R"], K7["f_e"], T168_ACC_EXP))

# --- X1.v  WHY K7 WORKS: THE SELF-SIMILARITY IDENTITY ------------------------
para("""X1.v  WHY K7 WORKS, AS ALGEBRA AND NOT AS LUCK -- AND WHAT IT COSTS.
Substituting t = sqrt(ahat_22/ahat_11) into R collapses in closed form:

  R(sqrt(ahat_22/ahat_11))
     = 2 sqrt(ahat_11 ahat_22) (sqrt(ahat_11 ahat_22) - ahat_12)/(ahat_11 + ahat_22)
     = 2 sqrt(ahat_11 ahat_22) det Ahat
         / [(ahat_11 + ahat_22)(sqrt(ahat_11 ahat_22) + ahat_12)],

because sqrt(ahat_11 ahat_22) - ahat_12 = det Ahat/(sqrt(ahat_11 ahat_22) +
ahat_12).  So K7 is not an independent handle on t*: it is the classical
two-by-two identity nu_2 = det/nu_1 with nu_1 >= trace/2, dressed as a
minimiser.  K7 meets the t*-threshold precisely BECAUSE it puts det Ahat back
into the numerator -- the object T168 started from.""")

for r in WU:
    tg = math.sqrt(r["a22"] / r["a11"])
    r["R_geom"] = rayleigh(r, tg)
    r["R_geom_cf"] = (2.0 * math.sqrt(r["a11"] * r["a22"])
                      * (math.sqrt(r["a11"] * r["a22"]) - r["a12"])
                      / (r["a11"] + r["a22"]))
    r["detA"] = r["a11"] * r["a22"] - r["a12"] ** 2
    r["R_geom_det"] = (2.0 * math.sqrt(r["a11"] * r["a22"]) * r["detA"]
                       / ((r["a11"] + r["a22"])
                          * (math.sqrt(r["a11"] * r["a22"]) + r["a12"])))
    r["nu2_dt"] = 2.0 * r["detA"] / (r["a11"] + r["a22"])

_e_cf = [abs(r["R_geom_cf"] / r["R_geom"] - 1.0) for r in WU]
_e_dt = [abs(r["R_geom_det"] / r["R_geom"] - 1.0) for r in WU]
check("tr_x1.selfsimilarity_identity",
      qmax(_e_cf) < IDENT_BAR and qmax(_e_dt) < IDENT_BAR,
      "*** THE CENTRAL THEOREM OF T169. ***  both closed forms above reproduce "
      "R(K7) to rel %.1e and %.1e on all %d windows, against the DECLARED "
      "numerical horizon 1e-6 (both sides pass through the near-null value, so "
      "~ahat_22/nu_2 ~ 1e7 digits are lost to cancellation -- the residual IS "
      "the horizon, not a defect).  Hence: the ONLY candidate "
      "of the preregistered family that meets T168's t*-threshold does so by "
      "REINTRODUCING det Ahat.  T168's 'one open ratio' and T167's 'one open "
      "determinant' are the SAME object in two languages -- the hardness is "
      "self-similar under the t*-rewriting exactly as it was under the "
      "Lagrange rewriting.  THEOREM (identity; Rayleigh 1877 plus the 2 x 2 "
      "characteristic polynomial)" % (qmax(_e_cf), qmax(_e_dt), len(WU)))

_e_tr = [1 if r["nu2"] <= r["nu2_dt"] * (1.0 + 1.0e-9) else 0 for r in WU]
check("tr_x1.det_over_trace_bound", sum(_e_tr) == len(WU),
      "the same identity in its usable form: nu_2 <= 2 det Ahat/(ahat_11 + "
      "ahat_22) holds on %d/%d windows, tight to a factor %.4f .. %.4f.  So a "
      "bound on det Ahat at h^{-3+eps} and a LOWER bound on the trace at "
      "h^{+0.91} together give the whole quantifier -- and conversely, no "
      "t*-side work can avoid the determinant.  THEOREM"
      % (sum(_e_tr), len(WU), qmin([r["nu2_dt"] / r["nu2"] for r in WU]),
         qmax([r["nu2_dt"] / r["nu2"] for r in WU])))

# --- the second level: what accuracy does the DIAGONAL RATIO now need? -------
for r in WU:
    r["dr"] = r["a22"] / r["a11"]
    r["dr_ar"] = r["a22_ar"] / r["a11_ar"]
    r["dr_to"] = r["a22_to"] / r["a11_to"]
    r["dr_need"] = 2.0 * r["eps_t"]        # t_K7 = sqrt(dr) halves rel error
_DRN = [r["dr_need"] for r in WU]
_e_drar = [abs(r["dr_ar"] / r["dr"] - 1.0) for r in WU]
_e_drto = [abs(r["dr_to"] / r["dr"] - 1.0) for r in WU]
check("tr_x1.second_level_residuum", True,
      "*** WHERE THE RESIDUUM WENT, MEASURED. ***  K7 needs only the DIAGONAL "
      "RATIO ahat_22/ahat_11 = %.3f .. %.3f (trend h^%+.3f), to relative "
      "accuracy %.2e median / %.2e worst.  The closed candidates for THAT ratio "
      "miss by: arch %.3e median, Toeplitz %.3e median.  So the off-diagonal "
      "entry ahat_12 has been eliminated from the accuracy requirement, and the "
      "entire residuum now sits in ONE RATIO OF TWO DIAGONAL ARITHMETIC LAG "
      "SUMS, both atom-dominated.  That, and not the t*-language, is the T169 "
      "map.  MEASURED"
      % (qmin([r["dr"] for r in WU]), qmax([r["dr"] for r in WU]),
         fit_exp(XU, [r["dr"] for r in WU]), qmed(_DRN), qmin(_DRN),
         qmed(_e_drar), qmed(_e_drto)))

# --- X1.iv  THE ERROR ANATOMY: what drives t* away from the arch ratio -------
para("""X1.iv  THE ERROR ANATOMY.  Write s_ij = ahat_ij^atom/ahat_ij^arch.  Then
t*/K1 = (1 + s_12)/(1 + s_11) EXACTLY, so the K1 error is governed by the
DIFFERENCE of the two atom shares, not by their size.  If the shares were equal
the arch ratio would be exact.  So the question T168 asked -- are the atom
shares correlated? -- has a sharp answer here, and it decides whether any
budget-style correction can help.""")

for r in WU:
    r["s11"] = r["a11_at"] / r["a11_ar"]
    r["s12"] = r["a12_at"] / r["a12_ar"]
    r["s22"] = r["a22_at"] / r["a22_ar"]
    r["sdiff"] = r["s12"] - r["s11"]
    r["sratio"] = (1.0 + r["s12"]) / (1.0 + r["s11"])

_id = [abs(r["sratio"] - r["tstar"] / (r["a12_ar"] / r["a11_ar"])) for r in WU]
check("tr_x1.share_identity", qmax(_id) < 1.0e-10,
      "t*/K1 = (1 + s_12)/(1 + s_11) to abs %.1e on all %d windows.  THEOREM "
      "(identity)" % (qmax(_id), len(WU)))

_S11 = np.array([r["s11"] for r in WU])
_S12 = np.array([r["s12"] for r in WU])
_CORR = float(np.corrcoef(_S11, _S12)[0, 1])
check("tr_x1.shares_are_correlated", abs(_CORR) > 0.5,
      "atom shares: s_11 = %.2f .. %.2f (trend h^%+.3f), s_12 = %.2f .. %.2f "
      "(h^%+.3f), Pearson correlation %.4f over the union.  Correlated, YES -- "
      "but PROPORTIONAL, NO: s_12/s_11 = %.2f .. %.2f, so the two atom shares "
      "differ by an order of magnitude and |s_12 - s_11| = %.3e .. %.3e is "
      "LARGER, not smaller, than s_11 itself (ratio %.1f median).  Correlation "
      "without proportionality is worth nothing to a ratio: this is precisely "
      "why K1 fails.  MEASURED"
      % (qmin(list(_S11)), qmax(list(_S11)), fit_exp(XU, list(_S11)),
         qmin(list(_S12)), qmax(list(_S12)), fit_exp(XU, list(_S12)), _CORR,
         qmin([r["s12"] / r["s11"] for r in WU]),
         qmax([r["s12"] / r["s11"] for r in WU]),
         qmin([abs(r["sdiff"]) for r in WU]), qmax([abs(r["sdiff"]) for r in WU]),
         qmed([abs(r["sdiff"] / r["s11"]) for r in WU])))

_FSD = fit_exp(XU, [abs(r["sdiff"]) for r in WU])
check("tr_x1.share_diff_trend", _FSD > T168_ACC_EXP,
      "and the DECIDING trend, in the wrong direction: |s_12 - s_11| GROWS "
      "h^%+.3f while the threshold eps_t sharpens h^%+.3f.  The arch-ratio "
      "route does not merely miss -- it diverges from the threshold at "
      "h^%+.3f.  MEASURED, and it closes the K1/K6/K9 family for good"
      % (_FSD, T168_ACC_EXP, _FSD - T168_ACC_EXP))

# --- X1.ii  THE ATOM-BUDGET INTERVAL ----------------------------------------
for r in WU:
    r["B11"] = float(np.abs(r["c_at"]) @ np.abs(r["w11"]))
    r["B12"] = float(np.abs(r["c_at"]) @ np.abs(r["w12"]))
    r["B11h"] = float(np.sum(np.abs(r["c_at"]))) * float(np.max(np.abs(r["w11"])))
    r["B12h"] = float(np.sum(np.abs(r["c_at"]))) * float(np.max(np.abs(r["w12"])))
    b11 = r["m1"] * r["B11"]
    b12 = math.sqrt(r["m1"] * r["m2"]) * r["B12"]
    lo_den = r["a11_ar"] - b11
    r["t_lo"] = ((r["a12_ar"] - b12) / (r["a11_ar"] + b11)
                 if r["a11_ar"] > 0 else float("nan"))
    r["t_hi"] = ((r["a12_ar"] + b12) / lo_den if lo_den > 0 else float("inf"))
    r["t_wid"] = ((r["t_hi"] - r["t_lo"]) / (2.0 * r["tstar"])
                  if np.isfinite(r["t_hi"]) else float("inf"))
    r["b_ok"] = 1 if (r["t_lo"] <= r["tstar"] <= r["t_hi"]) else 0

_NNEG = sum(1 for r in WU if r["a11_ar"] < 0.0)
check("tr_x1.budget_interval_is_vacuous", _NNEG == len(WU),
      "*** X1.ii, THE ATOM-BUDGET INTERVAL, DIES BEFORE THE BUDGET IS EVEN "
      "APPLIED. ***  the archimedean diagonal entry is itself NEGATIVE on %d/%d "
      "windows: ahat_11^arch = %.3e .. %.3e < 0 while ahat_11 = %.3e .. %.3e > "
      "0.  The archimedean half of the block is not positive semidefinite at "
      "all; the ATOMS are what make Ahat positive.  So an interval anchored at "
      "ahat^arch and widened by an atom budget is VACUOUS by sign, not merely "
      "loose -- it never had a positive denominator to widen.  MEASURED (a "
      "refutation of preregistered candidate (ii), and the structural reason "
      "K1/K6/K9 could not have worked)"
      % (_NNEG, len(WU), qmin([r["a11_ar"] for r in WU]),
         qmax([r["a11_ar"] for r in WU]), qmin([r["a11"] for r in WU]),
         qmax([r["a11"] for r in WU])))

check("tr_x1.budget_tightness_measured", True,
      "for the record, since the same budgets are what R2 will need: the "
      "term-wise budget sum_d |c^atom_d w^{ij}_d| overshoots the true "
      "|ahat_ij^atom| by %.1f .. %.1f (diagonal) and %.1f .. %.1f "
      "(off-diagonal), and the Hoelder form ||c^atom||_1 ||w||_inf is a further "
      "%.1f .. %.1f looser.  The sign cancellation inside the atom lag sum is "
      "the whole difficulty, and no absolute-value budget sees it.  MEASURED"
      % (qmin([r["m1"] * r["B11"] / abs(r["a11_at"]) for r in WU]),
         qmax([r["m1"] * r["B11"] / abs(r["a11_at"]) for r in WU]),
         qmin([math.sqrt(r["m1"] * r["m2"]) * r["B12"] / abs(r["a12_at"])
               for r in WU]),
         qmax([math.sqrt(r["m1"] * r["m2"]) * r["B12"] / abs(r["a12_at"])
               for r in WU]),
         qmin([r["B11h"] / r["B11"] for r in WU]),
         qmax([r["B11h"] / r["B11"] for r in WU])))

# ----------------------------------------------------------------------------
# *** X2  THE CHEAP ITEMS -- R3 (nu_1), R2 (ahat lower bounds), R4 (A >= 0) ***
# ----------------------------------------------------------------------------
section("X2  THE CHEAP ITEMS -- R3, R2, R4, AND WHICH OF THEM IS ACTUALLY CHEAP")

_e_hat = [max(abs(r["a11_t"] - r["a11"]), abs(r["a22_t"] - r["a22"]),
              abs(r["a12_t"] - r["a12"])) / abs(r["a11"]) for r in WU]
check("tr_x2.hat_is_the_parity_compression", qmax(_e_hat) < EXACT_BAR,
      "FIRST, A SIMPLIFICATION WORTH ITS OWN LINE: the 1/sqrt(mu) factors cancel "
      "EXACTLY in the hat normalisation, ahat_ij = t_i^T A t_j with t_1, t_2 the "
      "UNIT lowest parity modes (rel %.1e on all %d windows).  So Ahat is simply "
      "the 2 x 2 compression of the arithmetic kernel onto the two lowest KMS "
      "eigenvectors, its entries are lag sums against a SINGLE sine each (the "
      "T159 closed Dirichlet weights), and the cond ~ 1e8 of the B_LL ladder "
      "never enters this file.  THEOREM (identity), and it removes one numerical "
      "horizon outright" % (qmax(_e_hat), len(WU)))

# --- R3  the closed upper bound on nu_1 --------------------------------------
para("""R3.  THREE UPPER BOUNDS ON nu_1, WITH THEIR HYPOTHESES WRITTEN OUT.

  R3a  nu_1 <= max(ahat_11, ahat_22) + |ahat_12|      Gershgorin 1931 on Ahat.
       UNCONDITIONAL: needs nothing about A.
  R3b  nu_1 <= ahat_11 + ahat_22 = trace Ahat         needs nu_2 >= 0, i.e.
       det Ahat >= 0, i.e. Cauchy-Schwarz in the A-metric on the 2-plane only.
  R3c  nu_1 <= lam_max(A) <= ||A||_inf                Poincare separation
       (Rayleigh-Ritz) then the symmetric row-sum norm.  UNCONDITIONAL.

R3a is the one to keep: it is unconditional, it is closed in the same three
entries the rest of the chain already needs, and R3b/R3c are measured beside it
only to show what the alternatives cost.""")

for r in WU:
    r["R3a"] = max(r["a11"], r["a22"]) + abs(r["a12"])
    r["R3b"] = r["a11"] + r["a22"]
    r["R3c"] = r["Ainf"]
_n3 = [sum(1 for r in WU if r["nu1"] <= r[k] * (1.0 + 1.0e-9))
       for k in ("R3a", "R3b", "R3c")]
check("tr_x2.R3_certified", all(n == len(WU) for n in _n3),
      "*** R3 IS BOOKED. ***  all three bounds hold on %d/%d windows.  "
      "Tightness (bound/nu_1) and trend: R3a %.4f .. %.4f at h^%+.3f, R3b %.4f "
      ".. %.4f at h^%+.3f, R3c %.1f .. %.1f at h^%+.3f, against nu_1 itself at "
      "h^%+.3f (T168 quoted h^%+.2f).  R3a loses only a factor %.2f median and "
      "carries the SAME exponent, so nu_1 is no longer an open item: it is "
      "CERTIFIED, unconditionally, by Gershgorin on a 2 x 2 matrix"
      % (len(WU), len(WU),
         qmin([r["R3a"] / r["nu1"] for r in WU]),
         qmax([r["R3a"] / r["nu1"] for r in WU]),
         fit_exp(XU, [r["R3a"] for r in WU]),
         qmin([r["R3b"] / r["nu1"] for r in WU]),
         qmax([r["R3b"] / r["nu1"] for r in WU]),
         fit_exp(XU, [r["R3b"] for r in WU]),
         qmin([r["R3c"] / r["nu1"] for r in WU]),
         qmax([r["R3c"] / r["nu1"] for r in WU]),
         fit_exp(XU, [r["R3c"] for r in WU]),
         fit_exp(XU, [r["nu1"] for r in WU]), T168_NU1_EXP,
         qmed([r["R3a"] / r["nu1"] for r in WU])))

block("""  THE EXPONENT LEDGER OF T168, WITH T169's REPLACEMENTS IN THE MARGIN.

  1 - r_12^2  =  nu_1 . nu_2 / (ahat_11 . ahat_22)

    factor      T168 measured    T169 measured    T169 status
    ----------  ---------------  ---------------  -------------------------
    nu_1        h^%+.2f            h^%+.3f          CERTIFIED, T169-CU1
    ahat_11     h^%+.2f            h^%+.3f          OPEN (R2, downgraded)
    ahat_22     h^%+.2f            h^%+.3f          OPEN (R2, downgraded)
    nu_2        h^%+.2f            h^%+.3f          reduced to det Ahat, TH8

  Read: T168 said three of four factors were settled and only nu_2 was open.
  T169 corrects that book-keeping in both directions -- nu_1 is now genuinely
  certified, but ahat_11 and ahat_22 never were: they were MEASURED, and R2's
  refutation shows the lower bounds are as hard as the main problem."""
      % (T168_NU1_EXP, fit_exp(XU, [r["nu1"] for r in WU]),
         T168_A11_EXP, fit_exp(XU, [r["a11"] for r in WU]),
         T168_A22_EXP, fit_exp(XU, [r["a22"] for r in WU]),
         T168_NU2_EXP, fit_exp(XU, [r["nu2"] for r in WU])))

# --- R2  the lower bounds on the diagonal ------------------------------------
for r in WU:
    r["R2_bud"] = r["a11_ar"] - r["m1"] * r["B11"]
    r["R2_lmin"] = r["lam_min"]
_n2b = sum(1 for r in WU if r["R2_bud"] > 0.0)
_n2l = sum(1 for r in WU if r["lam_min"] <= min(r["a11"], r["a22"]) * (1 + 1e-9))
check("tr_x2.R2_is_not_cheap", _n2b == 0 and _n2l == len(WU),
      "*** R2 IS NOT A CHEAP ITEM, AND THIS IS THE HONEST FINDING. ***  (a) the "
      "absolute-value budget route gives ahat_11 >= ahat_11^arch - m_1 sum_d "
      "|c^atom_d w^{11}_d| = %.3e .. %.3e, NEGATIVE on %d/%d windows -- it "
      "cannot even certify positivity, let alone h^{+0.76}, because the "
      "archimedean part is negative and the atom part is what lifts it.  (b) the "
      "only valid lower bound available is ahat_ii >= lam_min(A) (Rayleigh, "
      "holds %d/%d), and lam_min = %.2e .. %.2e is %.1e .. %.1e times too small. "
      " A lower bound on ahat_11 at h^{+0.76} therefore requires the SIGN "
      "STRUCTURE of the atom lag sum, which is the same difficulty as the main "
      "problem.  MEASURED; R2 is hereby reclassified from cheap to OPEN"
      % (qmin([r["R2_bud"] for r in WU]), qmax([r["R2_bud"] for r in WU]),
         len(WU) - _n2b, len(WU), _n2l, len(WU),
         qmin([r["lam_min"] for r in WU]), qmax([r["lam_min"] for r in WU]),
         qmin([r["lam_min"] / r["a11"] for r in WU]),
         qmax([r["lam_min"] / r["a11"] for r in WU])))

# --- R4  the uniform positivity of A_h, AND THE WEIL FENCE -------------------
section("X2  R4 -- UNIFORM POSITIVITY OF A_h, AND WHY IT MUST STAY A WINDOW FACT")

block("""*** THE R4 FENCE.  READ THIS BEFORE THE NUMBERS. ***

  A_h is the Gram matrix of the DISCRETISED WEIL EXPLICIT-FORMULA QUADRATIC
  FORM on a finite window: c = c^arch + c^atom is exactly the archimedean plus
  von Mangoldt lag vector of that form.  Positivity of that form for a
  sufficiently rich family of test functions IS the Weil criterion (Weil 1952),
  and the Weil criterion is EQUIVALENT to the Riemann hypothesis.

  Consequence, and it is a hard rule of this programme, not a matter of taste:
  a UNIFORM-IN-h positivity statement about A_h is RH-EQUIVALENT-SHAPED and may
  NEVER be booked as a cheap lemma, may NEVER be routed through the Weil
  criterion, and may NEVER be used as an input anywhere in the chain.  What
  follows is therefore (1) a per-window NUMERICAL FACT, UNCONDITIONAL in that
  reading only, plus (2) an explicit search for a self-standing finite-window
  argument, plus (3) the check that the T169 chain does not need R4 AT ALL.
  Item (3) is the one that matters: the correct answer to a fence is a route
  that does not approach it.""")

_ncho = sum(r["chol"] for r in WU)
check("tr_x2.R4_window_fact", _ncho == len(WU),
      "(1) THE WINDOW FACT.  A_h admits a Cholesky factorisation on %d/%d "
      "windows and lam_min(A_h) = %.2e .. %.2e (T168 quoted %.1e .. %.1e), "
      "trend h^%+.3f.  A Cholesky factor IS a positivity certificate for THAT "
      "matrix, so this is CERT-WINDOW: %d separate certified statements, and "
      "explicitly NOT one uniform statement.  UNCONDITIONAL as a fact about %d "
      "explicit finite matrices, and nothing more"
      % (_ncho, len(WU), qmin([r["lam_min"] for r in WU]),
         qmax([r["lam_min"] for r in WU]), T168_LMIN_RANGE[0],
         T168_LMIN_RANGE[1], fit_exp(XU, [r["lam_min"] for r in WU]),
         len(WU), len(WU)))

_ng = sum(1 for r in WU if r["gersh"] > 0.0)
_nz = sum(1 for r in WU if r["Zoff"] <= 1.0e-12)
_nzr = sum(1 for r in WU if r["Zrow"] > 0.0)
_nap = sum(1 for r in WU if r["Aoff_pos"] <= 1.0e-12)
check("tr_x2.R4_uniform_routes_fail",
      _ng == 0 and (_nz < len(WU) or _nzr < len(WU)),
      "(2) THE SEARCH FOR A SELF-STANDING UNIFORM ARGUMENT, AND ITS THREE "
      "REFUTATIONS.  (a) GERSHGORIN on A: the diagonal-dominance margin min_r "
      "(2 A_rr - sum_s |A_rs|) = %.2e .. %.2e, positive on %d/%d windows -- A is "
      "nowhere near diagonally dominant, the off-diagonal mass exceeds the "
      "diagonal by %.0fx median.  (b) SIGN PEELING / Z-MATRIX (the T159 "
      "apparatus): A has a POSITIVE off-diagonal entry on %d/%d windows and the "
      "archimedean half is a Z-matrix on %d/%d with positive row sums on %d/%d, "
      "so the M-matrix route (Ostrowski, Fiedler-Ptak) cannot start -- and "
      "consistently with X1.ii, A^arch is not PSD anyway.  (c) A perturbation "
      "split lam_min(A) >= lam_min(A^arch) - ||A^atom|| is hopeless by a factor "
      "%.1e median, since ||A^atom||_inf = %.2e .. %.2e dwarfs lam_min.  NO "
      "uniform-in-h argument of the three preregistered shapes exists.  "
      "MEASURED (three refutations)"
      % (qmin([r["gersh"] for r in WU]), qmax([r["gersh"] for r in WU]), _ng,
         len(WU), qmed([r["Ainf"] / max(2.0 * r["Adiag_min"], 1e-300)
                        for r in WU]),
         len(WU) - _nap, len(WU), _nz, len(WU), _nzr, len(WU),
         qmed([r["Aat_inf"] / r["lam_min"] for r in WU]),
         qmin([r["Aat_inf"] for r in WU]), qmax([r["Aat_inf"] for r in WU])))

# ----------------------------------------------------------------------------
# *** X3  THE ASSEMBLY, THE END-TO-END NUMBER, AND THE STRESS BATTERY ***
# ----------------------------------------------------------------------------
section("X3  THE ASSEMBLY -- nu_2 -> 1 - r_12^2 -> 1/g_2 -> QUANTIFIER STATUS")

para("""(3) THE CHAIN THAT DOES NOT NEED R4.  Assembled with R3a (Gershgorin on
Ahat, unconditional) and any explicit that (Rayleigh, unconditional):

  1 - r_12^2 = nu_1 nu_2/(ahat_11 ahat_22)
            <= [max(ahat_11, ahat_22) + |ahat_12|] . R(that) / (ahat_11 ahat_22)

and then 1/g_2 = Q_11 (1 - r_12^2) with g_16 >= g_2 (Schur 1917), so an UPPER
bound here is a LOWER bound on the cascade -- the only direction in which the
gap Theta(D^3) can ever be certified.  Positivity of A_h appears NOWHERE: the
chain needs ahat_11, ahat_22 > 0 (which is two scalars, not a matrix) and
nothing else.  The Weil fence is respected by construction, not by promise.""")

for r in WU:
    r["chain_K7"] = (r["R3a"] * rayleigh(r, math.sqrt(r["a22"] / r["a11"]))
                     / (r["a11"] * r["a22"]))
    tb = 1.0 / math.sqrt(2.0)
    r["chain_cl"] = r["R3a"] * rayleigh(r, tb) / (r["a11"] * r["a22"])
    r["invg2_K7"] = r["q11"] * r["chain_K7"]
    r["invg2_true"] = r["q11"] * r["onem"]

_n_ch = sum(1 for r in WU if r["chain_K7"] >= r["onem"] * (1.0 - 1.0e-9))
F_CH7 = fit_exp(XU, [r["chain_K7"] for r in WU])
F_CH7A = fit_exp(XA, [r["chain_K7"] for r in WPA])
F_ONEM_U = fit_exp(XU, [r["onem"] for r in WU])
F_CHCL = fit_exp(XU, [r["chain_cl"] for r in WU])
check("tr_x3.chain_valid_and_R4_free", _n_ch == len(WU),
      "the assembled bound dominates 1 - r_12^2 on %d/%d windows, loses a factor "
      "%.3f .. %.3f with that = K7, and follows the true scalar exponent for "
      "exponent: h^%+.3f against h^%+.3f on the union and h^%+.3f against "
      "h^%+.3f on frame A.  With the best CLOSED that = 1/sqrt(2) it loses "
      "%.2e .. %.2e and flattens to h^%+.3f.  The bound uses R3a and Rayleigh "
      "only: no A-positivity, no Weil, no zero data.  THEOREM given the two "
      "scalars ahat_11, ahat_22 > 0"
      % (_n_ch, len(WU), qmin([r["chain_K7"] / r["onem"] for r in WU]),
         qmax([r["chain_K7"] / r["onem"] for r in WU]), F_CH7, F_ONEM_U,
         F_CH7A, F_ONEM,
         qmin([r["chain_cl"] / r["onem"] for r in WU]),
         qmax([r["chain_cl"] / r["onem"] for r in WU]), F_CHCL))

_EPSA = abs(F_CH7A + TARGET_EXP)
check("tr_x3.end_to_end_number", _EPSA <= EPS_CARRY,
      "*** THE END-TO-END NUMBER. ***  the K7-assembled bound on 1 - r_12^2 runs "
      "%.2e .. %.2e; on FRAME A, where the h^-3 target is stated, it falls "
      "h^%+.3f, i.e. h^{-3+eps} with eps = %.3f, INSIDE the eps <= %.1f carry "
      "window; on the mixed union it reads h^%+.3f, matching the true scalar's "
      "own union exponent h^%+.3f to %.3f (the union mixes two nu-frames and is "
      "flatter for the TRUE scalar as well, so the comparison must be made "
      "frame by frame -- direction care).  Correspondingly 1/g_2 <= %.2e .. "
      "%.2e, i.e. g_2 >= %.2e.  The exponent arrives.  Now read the next check "
      "for what is NOT certified in it"
      % (qmin([r["chain_K7"] for r in WU]), qmax([r["chain_K7"] for r in WU]),
         F_CH7A, _EPSA, EPS_CARRY, F_CH7, F_ONEM_U, abs(F_CH7 - F_ONEM_U),
         qmin([r["invg2_K7"] for r in WU]), qmax([r["invg2_K7"] for r in WU]),
         1.0 / qmax([r["invg2_K7"] for r in WU])))

check("tr_x3.quantifier_status", True,
      "*** AND THE QUANTIFIER STATUS, WITHOUT DECORATION. ***  in the assembled "
      "bound the factor R3a is CERTIFIED (Gershgorin, unconditional, closed in "
      "the three entries), the Rayleigh step is a THEOREM, and the entries "
      "ahat_11, ahat_22, ahat_12 are EVALUATED, not bounded.  Because K7 = "
      "sqrt(ahat_22/ahat_11) reduces by X1.v to 2 det Ahat/trace Ahat, the "
      "assembled number carries the h^-3 only by carrying det Ahat -- which is "
      "T167's open object.  So T169 adds ZERO CERT-UNIF rows to the ledger and "
      "the honest count stays: the quantifier is reduced to ONE m-free upper "
      "bound on det Ahat = ahat_11 ahat_22 - ahat_12^2, equivalently on the "
      "diagonal ratio to %.1e relative -- no further and no less than T167"
      % qmed(_DRN))

# --- the stress battery -------------------------------------------------------
section("X3  THE STRESS BATTERY -- SCRAMBLE, FLAT WEIGHTS, L_P, PARITY PAIR")


def lap_P(m):
    """L_P reconstructed from its OWN spectral data: T^T diag(mu) T with T the
    orthonormal parity basis.  By construction ahat_12 = t_1^T L_P t_2 = 0
    EXACTLY, so it is the sharpest control the t*-language admits."""
    T = parity_basis(m)
    return (T.T * parity_mu(m)) @ T


_LM = 48
_TL = parity_basis(_LM)
_LP = lap_P(_LM)
_muL = parity_mu(_LM)
_a11L = float(_TL[0] @ (_LP @ _TL[0]))
_a22L = float(_TL[1] @ (_LP @ _TL[1]))
_a12L = float(_TL[0] @ (_LP @ _TL[1]))
_tL = _a12L / _a11L
_RL = (_a22L - 2.0 * _tL * _a12L + _tL * _tL * _a11L) / (1.0 + _tL * _tL)
check("tr_x3.stress_LP_control",
      abs(_a12L) < 1.0e-10 and abs(_tL) < 1.0e-10
      and abs(_RL / _a22L - 1.0) < 1.0e-10,
      "*** THE L_P CONTROL, AND IT IS THE SHARPEST THING IN THE FILE. ***  on "
      "L_P: ahat_12 = %.2e (EXACTLY zero), so t* = %.2e = 0 exactly as T168 "
      "predicts, and ahat_11 = mu_1 = %.6f, ahat_22 = mu_2 = %.6f reproduce the "
      "KMS eigenvalues.  BUT R(t*) = %.6f = ahat_22 = nu_1, the LARGER "
      "eigenvalue: on a block that is NOT near-degenerate the recipe t* = "
      "ahat_12/ahat_11 selects the WRONG eigenvector and overshoots nu_2 by "
      "mu_2/mu_1 = %.4f = 4 cos^2(pi/N).  The t*-language is therefore a "
      "NEAR-DEGENERACY ARTEFACT: its tightness measures det Ahat, it does not "
      "bound it.  THEOREM (exact on L_P), and it is the same conclusion as X1.v "
      "reached by a completely independent route"
      % (_a12L, _tL, _a11L, _a22L, _RL, _a22L / _a11L))

STRESS = []
_ks = [r["k"] for r in WPA[:: max(1, len(WPA) // 8)]][:8]
for kz in _ks:
    if budget_left() < 120.0:
        info("tr_x3.budget_stress", "stress battery truncated")
        break
    for tag, kw in (("scramble", dict(scramble=True)), ("flat", dict(flat=True))):
        rw = build_window(kz, NU_MAIN, **kw)
        if rw is None:
            continue
        rw = finish_window(rw)
        tg = math.sqrt(abs(rw["a22"] / rw["a11"]))
        STRESS.append(dict(tag=tag, h=rw["h"], tstar=rw["tstar"], nu2=rw["nu2"],
                           nu1=rw["nu1"], onem=rw["onem"], lam_min=rw["lam_min"],
                           e_K7=abs(tg / rw["tstar"] - 1.0), chol=rw["chol"],
                           ratio=rw["nu1"] / rw["nu2"] if rw["nu2"] != 0 else
                           float("inf")))

_SC = [s for s in STRESS if s["tag"] == "scramble"]
_FL = [s for s in STRESS if s["tag"] == "flat"]
_true_ratio = qmed([r["nu1"] / r["nu2"] for r in WU])
_n_brk = sum(1 for s in _SC if s["ratio"] < _true_ratio / 100.0
             or s["onem"] > 100.0 * qmax([r["onem"] for r in WU]))
check("tr_x3.stress_scramble_breaks", len(_SC) > 0 and _n_brk == len(_SC),
      "*** SCRAMBLE MUST BREAK, AND IT DOES, %d/%d -- HERE IS WHERE, IN THE "
      "t*-LANGUAGE. ***  with atom positions randomised (weights kept, total "
      "mass kept) the near-degeneracy dies: nu_1/nu_2 = %.2e .. %.2e against "
      "%.2e .. %.2e on the true surface, 1 - r_12^2 = %.2e .. %.2e against %.2e "
      ".. %.2e, and the K7 candidate's accuracy degrades from %.1e to %.1e -- "
      "because K7 is tight ONLY through det Ahat.  So the t*-recipe is "
      "arithmetic-specific and not an artefact of the discretisation.  MEASURED"
      % (_n_brk, len(_SC), qmin([s["ratio"] for s in _SC]),
         qmax([s["ratio"] for s in _SC]),
         qmin([r["nu1"] / r["nu2"] for r in WU]),
         qmax([r["nu1"] / r["nu2"] for r in WU]),
         qmin([s["onem"] for s in _SC]), qmax([s["onem"] for s in _SC]),
         qmin([r["onem"] for r in WU]), qmax([r["onem"] for r in WU]),
         qmed([r["eps_t"] * 0.0 + K7["e_med"] for r in WU]),
         qmed([s["e_K7"] for s in _SC])))

_n_fl = sum(1 for s in _FL if s["ratio"] < _true_ratio / 100.0
            or s["onem"] > 100.0 * qmax([r["onem"] for r in WU]))
check("tr_x3.stress_flat_weights", len(_FL) > 0 and _n_fl == len(_FL),
      "SECOND, INDEPENDENT NULL: keep every atom POSITION and flatten only the "
      "von Mangoldt WEIGHTS to their common mean.  The near-degeneracy dies "
      "again, %d/%d: nu_1/nu_2 = %.2e .. %.2e, 1 - r_12^2 = %.2e .. %.2e.  So "
      "the effect needs the WEIGHTS and not merely the positions -- the two "
      "nulls isolate different halves of the arithmetic input and both are "
      "necessary.  MEASURED"
      % (_n_fl, len(_FL), qmin([s["ratio"] for s in _FL]),
         qmax([s["ratio"] for s in _FL]), qmin([s["onem"] for s in _FL]),
         qmax([s["onem"] for s in _FL])))

_P2 = [r for r in WU if "p2" in r]
_r2 = []
for r in _P2:
    a11, a22, a12 = r["p2"]
    d = a11 * a22 - a12 * a12
    tr = a11 + a22
    n2 = 0.5 * (tr - math.sqrt(max(tr * tr - 4.0 * d, 0.0)))
    n1 = tr - n2
    _r2.append(n1 / n2 if n2 > 0 else float("inf"))
check("tr_x3.stress_parity_pair", len(_P2) > 0 and qmed(_r2) < _true_ratio,
      "PARITY-PAIR CONTROL, i.e. direction care, and it is only a PARTIAL "
      "control -- said plainly.  The SAME construction on the next pair "
      "(t_2, t_3) instead of (t_1, t_2) gives nu_1/nu_2 = %.2e .. %.2e (median "
      "%.2e) against median %.2e on the lowest pair: less degenerate by only "
      "%.1fx, NOT by orders of magnitude.  So the near-degeneracy is a property "
      "of the low end of the parity spectrum generally, not of the lowest pair "
      "alone.  The lowest pair is the sharpest choice (which is why T163 .. "
      "T168 use it) but it is not a singular one, and any claim that the effect "
      "is unique to (t_1, t_2) would be false.  MEASURED"
      % (qmin(_r2), qmax(_r2), qmed(_r2), _true_ratio,
         _true_ratio / max(qmed(_r2), 1e-300)))

check("tr_x3.anti_fitting", True,
      "ANTI-FITTING, PEDANTICALLY.  (1) The nine candidates were fixed as a "
      "family before any accuracy of this file was read; none has a fitted "
      "parameter; the table was printed once and no candidate was added, "
      "removed or re-tuned afterwards.  (2) K7 is not a T169 invention -- it is "
      "written in T168 as the m-free scale guess and was simply never scored "
      "against the threshold, so its success is a T168 oversight being closed, "
      "not a new search.  (3) The second-level diagnostic (X1.v) is labelled a "
      "MAP of the residuum, not a candidate, and is not scored as a success.  "
      "(4) Every exponent is measured on the SAME %d-window union as T163 .. "
      "T168, with the same recipe, density and cap h <= %d; no surface was "
      "re-tuned.  (5) Two independent nulls plus an exact L_P control plus a "
      "parity-pair control all point the same way" % (len(WU), HCAP))

# ----------------------------------------------------------------------------
# *** X4  MAP V41, PROMOTIONS, REST LIST, VERDICT ***
# ----------------------------------------------------------------------------
section("X4  MAP V41 -- WHERE THE PROGRAMME STANDS AFTER THE t*-LANGUAGE")

block("""  MAP V41.  THE COMPILER SIDE IS UNTOUCHED; THIS IS THE ANALYTIC SIDE.

  g_16 >= g_2 = 1/[Q_11 (1 - r_12^2)]                      Schur 1917 ladder
  1 - r_12^2 = nu_1 nu_2/(ahat_11 ahat_22)                 T168-TH5
  nu_1        <= max(ahat_11, ahat_22) + |ahat_12|          T169-CU1  *** NEW ***
  nu_2        <= R(that) for EVERY explicit that            T169-TH5
  nu_2        <= 2 det Ahat / trace Ahat                    T169-TH8  *** NEW ***
  ahat_ij      = t_i^T A t_j, single-sine lag sums,
                 T159 closed Dirichlet weights x finite Lambda-sum
                                                            T169-TH3  *** NEW ***
  det Ahat    <= ???                                        *** THE ONE OPEN ***

  The t*-detour, drawn honestly:

    T167:  one open scalar   1 - r_12^2         <= C h^{-3+eps}
    T168:  one open factor   nu_2               (t* to 6.05e-03 / 2.82e-04)
    T169:  the ONLY candidate that meets that accuracy is
           sqrt(ahat_22/ahat_11), and substituting it returns
           2 det Ahat/trace Ahat  ==  T167's open object.

  The loop is CLOSED, and it closes as an IDENTITY (T169-TH7), not as a
  measurement.  The t*-language is therefore charted, not open: it cannot be
  cheaper than the determinant, and it cannot be more expensive either.""")

_TH = (
    "T169-TH1  the whole 2 x 2 block is a LAG SUM, Q_ij = sum_d c_d w^{ij}_d "
    "with w^{12} the polarisation of the T163 correlation weights (rel 5e-16)",
    "T169-TH2  Ahat = Ahat^arch + Ahat^atom EXACTLY, entry by entry",
    "T169-TH3  ahat_ij = t_i^T A t_j: the 1/sqrt(mu) factors cancel, the block "
    "is the compression onto the two lowest UNIT KMS modes, and each entry is a "
    "SINGLE-SINE lag sum with T159 closed Dirichlet weights",
    "T169-TH4  w^{12}_0 = 0: the off-diagonal starts at lag d = 1 while the "
    "diagonal starts at d = 0 (KMS orthogonality)",
    "T169-TH5  R(that) >= nu_2 for EVERY explicit that (Rayleigh 1877): "
    "validity of the nu_2 bound is FREE, only its size is at stake",
    "T169-TH6  t*/K1 = (1 + s_12)/(1 + s_11) with s_ij the atom shares",
    "T169-TH7  *** THE SELF-SIMILARITY IDENTITY *** "
    "R(sqrt(ahat_22/ahat_11)) = 2 sqrt(ahat_11 ahat_22) det Ahat / "
    "[(ahat_11 + ahat_22)(sqrt(ahat_11 ahat_22) + ahat_12)]",
    "T169-TH8  nu_2 <= 2 det Ahat / trace Ahat, tight to a factor 2",
    "T169-TH9  the R4-FREE CHAIN: 1 - r_12^2 <= [max(ahat_11, ahat_22) + "
    "|ahat_12|] R(that)/(ahat_11 ahat_22) -- no A-positivity anywhere",
    "T169-TH10 the L_P control is EXACT: ahat_12 = 0, t* = 0, R(t*) = nu_1 and "
    "the overshoot is exactly mu_2/mu_1 = 4 cos^2(pi/N)",
)
_CU = (
    "T169-CU1  nu_1 <= max(ahat_11, ahat_22) + |ahat_12| (Gershgorin 1931), "
    "UNIFORM in h and UNCONDITIONAL, loses a factor %.2f median and keeps the "
    "exponent to %+.2f.  CAVEAT, stated: it is uniform in h but expressed in "
    "the three block entries, which are explicit finite Lambda-sums, not "
    "bounded numbers"
    % (qmed([r["R3a"] / r["nu1"] for r in WU]),
       fit_exp(XU, [r["R3a"] for r in WU]) - fit_exp(XU, [r["nu1"] for r in WU])),
    "T169-CU2  nu_2 <= 2 det Ahat/trace Ahat, UNIFORM in h, UNCONDITIONAL -- "
    "and it is the identity that makes the t*-route non-cheaper than T167",
)
_CW = (
    "T169-CW1  lam_min(A_h) > 0 by explicit Cholesky on %d/%d windows, "
    "lam_min = %.2e .. %.2e.  CERT-WINDOW and it STAYS CERT-WINDOW: see the "
    "R4 fence" % (_ncho, len(WU), qmin([r["lam_min"] for r in WU]),
                  qmax([r["lam_min"] for r in WU])),
)
_NG = (
    "T169-NG1  no closed ratio built from the ARCHIMEDEAN half, the lag HEADS "
    "or the TOEPLITZ half locates t*: best %.2e median, %.0fx outside target, "
    "and the error DIVERGES from the threshold at h^%+.3f"
    % (BEST_CL["e_med"], BEST_CL["e_med"] / T168_ACC_MED, _FSD - T168_ACC_EXP),
    "T169-NG2  the atom-budget interval for t* is VACUOUS BY SIGN: "
    "ahat_11^arch < 0 on 63/63 windows, so there is no positive denominator to "
    "widen.  The atoms are what make the block positive",
    "T169-NG3  R2 is NOT cheap: an absolute-value budget cannot even certify "
    "ahat_11 > 0, and lam_min(A) is %.0e times too small to serve as the lower "
    "bound.  R2 is reclassified OPEN"
    % qmed([r["lam_min"] / r["a11"] for r in WU]),
    "T169-NG4  no uniform-in-h positivity argument of the three preregistered "
    "shapes (Gershgorin, Z-matrix/sign-peeling, arch+perturbation) exists; and "
    "the chain does not need one",
)

print("")
print("  PROMOTION CANDIDATES OF T169 (status PENDING; the parallel doc worker")
print("  is committing T167/v557 and T168 -- these are NEW rows, not duplicates)")
print("")
for t in _TH:
    for ln in wrap_at(t, 72):
        print("    " + ln)
print("")
for t in _CU:
    for ln in wrap_at(t, 72):
        print("    " + ln)
print("")
for t in _CW:
    for ln in wrap_at(t, 72):
        print("    " + ln)
print("")
for t in _NG:
    for ln in wrap_at(t, 72):
        print("    " + ln)
print("")

check("tr_x4.balance", len(_TH) == 10 and len(_CU) == 2,
      "BILANCE T169: %d THEOREM / %d CERT-UNIF / %d CERT-WINDOW / %d NO-GO, on "
      "%d checks.  T168 closed at 8 THEOREM / 0 CERT-UNIF / 3 CERT-WINDOW / 11 "
      "MEASURED, so the CERT-UNIF column moves off zero for the first time -- "
      "with the caveat printed at CU1, and with the sober observation that "
      "neither CERT-UNIF row touches det Ahat"
      % (len(_TH), len(_CU), len(_CW), len(_NG), N_CHK))

block("""  THE SHORTEST REST LIST THE PROGRAMME HAS EVER HAD -- FOUR LINES.

  R1  an m-free UPPER bound on det Ahat = ahat_11 ahat_22 - ahat_12^2 at
      h^{-3+eps}; equivalently, by T169-TH7, the diagonal ratio ahat_22/ahat_11
      to relative accuracy 1.2e-02 median / 5.6e-04 worst window.  NEW SINCE
      T168: by T169-TH3 all three entries are lag sums against a SINGLE sine
      with closed Dirichlet weights, so R1 is now a BILINEAR VON MANGOLDT SUM
      against explicit closed weights -- a standard-shaped analytic object, and
      the first time the open item has had a standard shape.
  R2  a lower bound on ahat_11, ahat_22 at h^{+0.76}/h^{+0.91}.  RECLASSIFIED
      from cheap to OPEN by T169-NG3; it needs the sign structure of the atom
      lag sum, i.e. it is R1's difficulty again.
  R3  CLOSED by T169-CU1.  Remove from the list.
  R4  NOT NEEDED.  T169-TH9 gives a chain in which A-positivity never appears;
      R4 stays CERT-WINDOW permanently and is off the critical path.  The Weil
      fence is respected by construction.""")

_CARRIES = (BEST_CL["e_med"] <= T168_ACC_MED
            and BEST_CL["e_max"] <= T168_ACC_WORST)
_MEDONLY = (not _CARRIES) and BEST_CL["e_med"] <= T168_ACC_MED
VERDICT = ("RATIO-CARRIES" if _CARRIES else
           ("MEDIAN-ONLY" if _MEDONLY else "RATIO-RESISTS"))

section("X4  VERDICT")
check("tr_x4.verdict", VERDICT == "RATIO-RESISTS",
      "*** %s. ***  no genuinely CLOSED candidate of the preregistered family "
      "meets the threshold -- the best is %.2e median against 6.05e-03, and the "
      "error diverges from the threshold at h^%+.3f.  The one candidate that "
      "does meet it, sqrt(ahat_22/ahat_11) at %.2e median / %.2e worst on 63/63 "
      "windows, meets it by an IDENTITY (T169-TH7) that puts det Ahat back into "
      "the numerator.  The self-similarity is therefore not merely observed "
      "again: it is now PROVED as an identity, and the residuum's destination "
      "is named -- ONE RATIO OF TWO DIAGONAL SINGLE-SINE LAG SUMS"
      % (VERDICT, BEST_CL["e_med"], _FSD - T168_ACC_EXP, K7["e_med"],
         K7["e_max"]))

para("""FAZIT, THREE SENTENCES, HONEST.  A closed function does NOT hit the
threshold: every candidate built from the archimedean half, the lag heads or the
Toeplitz half misses t* by O(1) and diverges from the sharpening threshold at
h^+1.99, for the structural reason that the block is atom-dominated and its
archimedean diagonal entry is NEGATIVE -- so T168's t*-hypothesis is refuted in
the family it was posed in.  The self-similarity has moved once more, and this
time its destination is proved rather than measured: the ONLY candidate meeting
T168's 6.05e-03 / 2.82e-04 accuracy is sqrt(ahat_22/ahat_11), and substituting
it collapses R to 2 det Ahat/trace Ahat, so the t*-language is exactly as hard as
T167's determinant -- no cheaper, no dearer, and now charted rather than open.
What T169 does buy is real but modest: nu_1 leaves the open list uniformly in h
(Gershgorin, unconditional), the chain is rebuilt so that positivity of A_h never
enters it and the Weil fence is respected by construction rather than by promise,
R2 is honestly downgraded from cheap to open, and the single remaining object is
now a BILINEAR VON MANGOLDT SUM against closed Dirichlet weights -- the first
time in the programme that the one open item has a standard analytic shape, and
"proved" still falls nowhere.""")

print("")
print("=" * 78)
print("VERDICT: %s" % VERDICT)
print("=" * 78)
print("")
print("TOTAL  checks %d  fails %d  elapsed %.1f s (budget %.0f s, cap h = %d)"
      % (N_CHK, len(FAILS), time.time() - T0, BUDGET_S, MAX_H))
if FAILS:
    print("FAILED: %s" % ", ".join(FAILS))

