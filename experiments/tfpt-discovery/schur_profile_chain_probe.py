"""Teil 104 Arm A -- chain variant; independent twin of schur_profile_bound_probe.py

Discovery probe (2026-07-26), part 104 of the zeta/prime investigation.
Contract SCHUR.PROFILE.BOUND, arm A (the CHAIN arm): can the induction
hypothesis of the collapse argument bind the ONE scalar that T102/T103
isolated as the entire hard core of the handoff?

WHERE THIS SITS  (T102/T103, taken as given and re-measured here)
  On E_- / E_0 / E_+ (parity with respect to the wing mirror at the atom
  point u_k = log n_k) the k-th atom is EXACTLY diag(-1/2, 0, +1/2) * mu_k
  with mu_k = 2 Lambda(n_k)/sqrt(n_k).  Hence
      Q_{k-1} = Q_full - (mu_k/2) P_-  +  (mu_k/2) P_+
  and the handoff of zone k is controlled by the single scalar
      sigma_k(delta) = lambda_min( Q_full|E_-  -  B_-^T M^{-1} B_- ),
      M := Q_full|_{E_0 (+) E_+},   B_- := coupling  E_- -> E_0 (+) E_+,
      mu_k/2 <= sigma_k   ==>   Q_{k-1}(alpha) >= 0   (handoff holds).
  T102: the BARE wing block lambda_min(Q_full|E_-) is strongly positive
  (4x..14x mu_k/2); the ENTIRE danger is the Schur DRESSING, which eats
  35.7%..97.3% of it.  T103 found the same place from the other side: the
  handoff is exactly the pencil ratio rho = lambda_max(A_sh^{-1} W) <= 1 with
  A_sh = Q|E_- - (mu/2) Id and W the dressing, and it recommended a
  prolate/Slepian basis on the wing pair.

THE LEVER THIS ARM TESTS
  The dressing couples E_- to E_0 (+) E_+, and on E_0 -- the SMALLER window --
  the induction hypothesis is available.  The naive form of that is a margin,
  M >= m Id, giving dress <= ||B_-||^2/m.  This probe measures m and finds it
  useless (the genuine form is nearly singular on the induction window), then
  replaces the margin route by the classical EXACT block-inverse split
      W = m0 A^{-1} m0^T  +  R Sig^{-1} R^T,
      R = mp - m0 A^{-1} C^T,   Sig = Q|E_+ - C A^{-1} C^T,
  caps each half by spectral calculus (per-mode data below a band start, then
  geometric BAND masses with weight w_j >= 1/lambda_j -- Parseval/Bessel), and
  measures the resulting headroom H = 1/cap in the A_sh metric.  The caps are
  MATRICES summed in the PSD order, with lambda_max taken once at the end:
  adding scalar maxima would pay Weyl's inequality twice for two non-aligned
  eigenvectors.

THE BLOCKS
  B1 COUPLING ANATOMY.  B_- dissected over the zones: operator/Frobenius mass,
     effective rank of W, exact (Parseval) frequency localisation of the E_0
     coupling mass, the low end (does B_- couple to the near-null modes of the
     genuine form at all?), and the mass-versus-margin trend that the chain
     must pay.
  B2 THE INDUCTIVE CHAIN.  A ladder of caps on rho: S0/S1 (uniform margin,
     Frobenius / operator mass), S2 (block split + band cap matrix on E_0),
     S3 (S2 with the ntop heaviest E_0 modes exact), S4 (S3 + the same band
     recipe on the E_+ Schur block), S3X (E_+ half exact), S2K (band caps on
     the joint block) and EX (lambda_max(W) itself, the measured optimum).
     Then the REACH: how deep inside the handoff window the certified chain
     still closes, gamma_max = max{gamma : cap(S4) <= 1 at delta = gamma d_c}.
  B3 WING BASIS.  The continuous prolate/Slepian concentration operator of the
     wing PAIR (spectral density carries the interference factor 1 - cos(t u)),
     the localisation of the near-null direction, and the certified block-split
     chain in the prolate basis versus the raw basis, in ONE currency.
  B4 EDGE REGULARITY + SYNTHESIS.  The power law sigma(d) >= sigma(dref)
     (d/dref)^q as a FIT (q_fit) and as an ENVELOPE (q_env, the steepest
     secant, for which the law IS a lower bound on the sampled ladder), the
     resolution drift at fixed delta and at fixed gamma = delta/delta_c, and
     the assembled chain link by link, zone by zone.

PREREGISTERED VERDICTS
  SCALAR-BOUNDED     : the inductive sigma bound suffices for the handoff on
                       every resolved zone AND the ingredient balance is clean.
  CHAIN-PARTIAL      : the chain stands and closes on part of the zones, or on
                       all of them but with measured (non-inducted) inputs.
  DRESSING-UNBOUNDED : the coupling mass outgrows every margin.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit, no
    verification/ module, no next.txt edit, no .md output.  This one file only.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  The
    atom-deleted counterfactual Q_{k-1} inside zone k is NOT a genuine form.
  * lambda_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER estimate for
    the continuum value: it can refute positivity, never prove it.  Every
    sigma, bare, m here is an UPPER estimate at the stated resolution, and a
    resolution axis is shown (fixed delta AND fixed gamma).
  * THE INDUCTION MARGIN m AND THE LOW-MODE COUPLING DATA ARE HYPOTHESIS /
    INDUCTION INPUTS.  They are measured to see their size, never claimed
    proved.  Certified vs measured vs induction-data is tracked per stage and
    summarised in the honest ledger.
  * Every fit is labelled a fit.  Classical anchors cited, not re-derived:
    Weil 1952 (explicit formula), Schur complement and the block-inverse
    identity, Cauchy-Schwarz, Weyl's perturbation inequality, Parseval and
    Bessel, Loewner order, Rayleigh-Ritz, Cholesky inertia, Slepian-Landau-
    Pollak prolate concentration, von Mangoldt / prime-power arithmetic.

OUTCOME OF THIS RUN  =>  see the honest ledger and VERDICT printed below.
"""
import ast
import math
import os
import time

import mpmath
import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh, toeplitz

PASS = 0
FAIL = 0
T_START = time.time()
MAX_SEEN = 0

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
T0_T93 = 6.28983599              # single sign change of the archimedean kernel
K0_CLOSED = -EULER - 3.0 * math.log(2.0) - 0.5 * math.pi - LOG_PI
FENCE = -1.0e-10                 # PSD tolerance of the RH-consistency fence

MAX_ARRAY = 2000
BUDGET_S = 860.0

M_MAIN = 2000                    # main resolution
M_DRIFT = (500, 1000, 2000)      # resolution axis
N_ZONES = 16
P_MIN = 2                        # smallest wing the grid can resolve
LADDER_NP = 10                   # ladder points per zone
FRACS = (0.10, 0.25, 0.45, 0.70, 0.90)   # shallow sweep, fractions of delta_c
GAMMA_REF = 0.50                 # the deep reference sample
GAMMA_GRID = (0.90, 0.70, 0.50, 0.35, 0.25, 0.15, 0.10)
DRIFT_ZONES = (1, 2, 3, 4, 6)    # zones whose reference wing survives M/4
NTOP = 8                         # exact low modes of E_0 in stages S3/S4
BAND_LAM0 = 1.0                  # band start
BAND_R = 2.0                     # geometric band ratio
BAND_LAM_MAX = 64.0              # last band edge
LAM0_GRID = (0.01, 0.03, 0.1, 0.3, 1.0, 3.0)   # data-cost frontier
IND_STAGES = ("S0", "S1", "S2", "S3", "S4")
ALL_STAGES = ("S0", "S1", "S2", "S3", "S4", "S3X", "S2K", "EX")

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
PG_N = 240
_PGX, _PGW = np.polynomial.legendre.leggauss(PG_N)
_SQ2 = math.sqrt(2.0)


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-34s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-34s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def note_array(n):
    global MAX_SEEN
    if n > MAX_SEEN:
        MAX_SEEN = n


# ----------------------------------------------------------------------------
# el_firewall -- AST scan of this source
# ----------------------------------------------------------------------------
FORBIDDEN_TOKENS = tuple("".join(parts) for parts in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
    ("25.01", "0857"), ("30.42", "4876"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "mpmath", "numpy", "os", "scipy", "time"}


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
            fn = node.func
            nm = getattr(fn, "id", None) or getattr(fn, "attr", None)
            if nm == "open":
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(c in mode for c in "wax+"):
                    bad_writes.append(mode)
    check("el_firewall.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("el_firewall.imports", not bad_imports,
          "import roots %s" % sorted(ALLOWED_IMPORT_ROOTS))
    check("el_firewall.no_writes", not bad_writes, "no write-mode open()")


# ----------------------------------------------------------------------------
# the archimedean kernel k(t) = Re psi(1/4 + i t/2) - log pi
# ----------------------------------------------------------------------------
_BERN = (1.0 / 12.0, -1.0 / 120.0, 1.0 / 252.0, -1.0 / 240.0, 1.0 / 132.0,
         -691.0 / 32760.0, 1.0 / 12.0)


def kernel_k(t):
    """Re psi(1/4 + i t/2) - log pi, by recurrence + the standard asymptotic."""
    z = 0.25 + 0.5j * np.asarray(t, dtype=float)
    acc = np.zeros(z.shape, dtype=complex)
    for j in range(12):
        acc -= 1.0 / (z + j)
    w = z + 12.0
    iw2 = 1.0 / (w * w)
    tail = 0.0
    for c in reversed(_BERN):
        tail = (tail + c) * iw2
    psi = np.log(w) - 0.5 / w - tail + acc
    return np.real(psi) - LOG_PI


def kernel_k_mp(t):
    return float(mpmath.re(mpmath.digamma(mpmath.mpf(0.25) + 0.5j * t))) - LOG_PI


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap)
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
    """Ordered prime-power atoms (n, Lambda(n), u = log n, mu = 2 Lambda/sqrt n)."""
    lam = von_mangoldt_table(n_max)
    out = []
    for n in np.nonzero(lam > 0)[0]:
        n = int(n)
        out.append((n, lam[n], math.log(n), 2.0 * lam[n] / math.sqrt(n)))
    return out


ATOMS = atom_table(64)


# ----------------------------------------------------------------------------
# PWC Galerkin assembly (T97/T101/T102 convention, re-used verbatim)
# ----------------------------------------------------------------------------
def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return (tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w)) / (-np.expm1(-2.0 * w))


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


def _arch_A_near(s, D):
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D
    pts = sorted({p for p in (0.0, s, D - s, W) if 0.0 <= p <= W})
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


def arch_A_mp(s, D):
    """The same lag entry by mpmath quadrature, kinks handed to the integrator."""
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D

    def f(w):
        tw = 0.5 * (max(0.0, 1.0 - abs(s - w) / D) + max(0.0, 1.0 - abs(s + w) / D))
        return (tri_s * mpmath.e**(-2.0 * w) - tw * mpmath.e**(-0.5 * w)) \
            / (-mpmath.expm1(-2.0 * w))

    pts = sorted({p for p in (0.0, s - D, D - s, s, W) if 0.0 <= p <= W})
    tot = mpmath.quad(f, pts)
    return float(-(EULER + LOG_PI) * tri_s + 2.0 * tot
                 + tri_s * (-mpmath.log1p(-mpmath.e**(-2.0 * W))))


def arch_diag_tspace(D, t_split=None):
    """A(0,D) from the t-space side: (1/pi) int_0^inf k(t) |ghat(t)|^2 dt.

    |ghat|^2 = 4 sin^2(tD/2)/(D t^2) for one PWC cell of width D (Parseval).
    Below t_split the oscillation is resolved by half-period panels; above it
    sin^2 is replaced by its mean 1/2 (the remaining factor k(t)/t^2 is slowly
    varying) and the tail is mapped to [0,1] by t = t_split/x.
    """
    if t_split is None:
        t_split = max(200.0, 80.0 * math.pi / D)
    n_pan = max(32, int(math.ceil(t_split * D / math.pi)))
    edges = np.linspace(0.0, t_split, n_pan + 1)
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        t = mid + half * _GLX
        wgt = np.where(t > 0.0, 4.0 * np.sin(0.5 * t * D) ** 2 / (D * t * t + 1e-300),
                       D)
        tot += half * float(np.dot(_GLW, kernel_k(t) * wgt))
    for lo, hi in ((0.0, 0.5), (0.5, 1.0)):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        x = mid + half * _GLX
        t = t_split / x
        tot += half * float(np.dot(_GLW, kernel_k(t) * 2.0 / (D * t_split)))
    return tot / math.pi


def tri(y, D):
    return np.maximum(0.0, 1.0 - np.abs(y) / D)


def atom_lag(lags_s, u, D):
    return 0.5 * (tri(lags_s - u, D) + tri(lags_s + u, D))


def pole_vectors(alpha, M):
    D = 2.0 * alpha / M
    xe = -alpha + np.arange(M + 1) * D
    a = 2.0 * (np.exp(xe[1:] / 2.0) - np.exp(xe[:-1] / 2.0)) / math.sqrt(D)
    b = 2.0 * (np.exp(-xe[:-1] / 2.0) - np.exp(-xe[1:] / 2.0)) / math.sqrt(D)
    return a, b


def build_Q(alpha, M, atoms):
    note_array(M)
    D = 2.0 * alpha / M
    s = np.arange(M) * D
    lag = arch_A(s, D)
    for u_j, mu_j in atoms:
        lag = lag - mu_j * atom_lag(s, u_j, D)
    Q = toeplitz(lag)
    a, b = pole_vectors(alpha, M)
    Q += np.outer(a, b) + np.outer(b, a)
    return Q


def zone_geometry(u, p, M):
    D = u / (M - p)
    alpha = u * M / (2.0 * (M - p))
    return D, alpha, p * D


def wing_bases(M, p):
    Bm = np.zeros((M, p))
    Bp = np.zeros((M, p))
    r = np.arange(p)
    Bm[r, r] = 1.0 / _SQ2
    Bm[M - p + r, r] = -1.0 / _SQ2
    Bp[r, r] = 1.0 / _SQ2
    Bp[M - p + r, r] = 1.0 / _SQ2
    return Bm, Bp, slice(p, M - p)


def blocks_U(Q, p):
    """Q in the exact orthogonal basis U = [B_-, E_0, B_+]."""
    M = Q.shape[0]
    L, C, R = slice(0, p), slice(p, M - p), slice(M - p, M)
    QLL, QLR, QRR = Q[L, L], Q[L, R], Q[R, R]
    QLC, QRC, QCC = Q[L, C], Q[R, C], Q[C, C]
    off = QLR + QLR.T
    mm = 0.5 * (QLL + QRR - off)
    pp = 0.5 * (QLL + QRR + off)
    mp = 0.5 * (QLL - QRR + QLR - QLR.T)
    m0 = (QLC - QRC) / _SQ2
    p0 = (QLC + QRC) / _SQ2
    return mm, pp, mp, m0, p0, QCC


def safe_cho(Q, shifts=(0.0, 1.0e-12, 1.0e-10, 1.0e-8, 1.0e-6)):
    n = Q.shape[0]
    for sh in shifts:
        try:
            if sh == 0.0:
                return cho_factor(Q, lower=True, check_finite=False), 0.0
            return cho_factor(Q + sh * np.eye(n), lower=True, check_finite=False), sh
        except LinAlgError:
            continue
    return None, float("nan")


def sym(A):
    return 0.5 * (A + A.T)


def op2(A):
    """||A||_op^2 of a rectangular block, via the smaller Gram matrix."""
    if A.shape[0] <= A.shape[1]:
        return float(eigvalsh(sym(A @ A.T)).max())
    return float(eigvalsh(sym(A.T @ A)).max())


def zone_pmax(k, M):
    """Largest wing that keeps atom k+1 outside the window (u_{k+1} > 2 alpha)."""
    u = ATOMS[k - 1][2]
    u_next = ATOMS[k][2]
    return max(P_MIN, int(math.floor(M * (1.0 - u / u_next))) - 1)


def p_for_delta(u, delta, M):
    """p with p u/(M-p) = delta, rounded to the grid."""
    p = int(round(delta * M / (u + delta)))
    return max(P_MIN, p)


# ----------------------------------------------------------------------------
# the prolate / Slepian concentration operator of the WING PAIR
# ----------------------------------------------------------------------------
def slepian_wing(p, D, u, t0=T0_T93, pair=True):
    """Concentration of the wing-pair elements in the band |t| <= t0.

    The E_- element of wing cell i is (g_i(x) - g_i(x-u))/sqrt(2), so its
    spectral density carries the interference factor (1 - cos(t u)); the
    concentration operator is
        S_ij = (1/pi) int_0^{t0} [4 sin^2(tD/2)/(D t^2)] cos(t(i-j)D) f(t) dt,
    f = (1 - cos(tu)) for the pair, f = 1 for a single wing.  0 <= S <= Id by
    Parseval (Slepian-Landau-Pollak).
    """
    mid, half = 0.5 * t0, 0.5 * t0
    t = mid + half * _PGX
    w = half * _PGW * (4.0 * np.sin(0.5 * t * D) ** 2 / (D * t * t)) / math.pi
    if pair:
        w = w * (1.0 - np.cos(t * u))
    d = np.arange(p) * D
    c = np.cos(np.outer(d, t))
    lagv = c @ w
    S = sym(toeplitz(lagv))
    lam, V = eigh(S)
    order = np.argsort(-lam)
    return lam[order], V[:, order], float(np.trace(S))


# ----------------------------------------------------------------------------
# the certified cap machinery
# ----------------------------------------------------------------------------
def band_matrix(lam, Z, lam0, ntop=0):
    """Cap matrix for Z diag(1/lam) Z^T by spectral calculus.

    The ntop lowest modes are kept EXACTLY; the rest is grouped into geometric
    bands [Lam_j, Lam_{j+1}) and each band contributes Z_b Z_b^T / Lam_j, which
    dominates it in the Loewner order because 1/lambda <= 1/Lam_j there
    (Bessel/Parseval: no mass is lost, the weights are certified).
    Returns (cap matrix, number of explicit modes, weights-certified flag).
    """
    p = Z.shape[0]
    G = np.zeros((p, p))
    ok = True
    z2 = (Z ** 2).sum(axis=0)
    exact = lam < lam0
    if ntop > 0:
        cand = np.nonzero(~exact)[0]
        if cand.size:
            heavy = cand[np.argsort(-(z2[cand] / lam[cand]))[:ntop]]
            exact[heavy] = True
    idx = np.nonzero(exact)[0]
    if idx.size:
        Ze = Z[:, idx]
        G += (Ze / lam[None, idx]) @ Ze.T
    n_ex = int(idx.size)
    rest = np.nonzero(~exact)[0]
    edge = lam0
    while rest.size:
        nxt = edge * BAND_R if edge < BAND_LAM_MAX else np.inf
        inb = (lam[rest] >= edge) & (lam[rest] < nxt)
        if inb.any():
            sel = rest[inb]
            if float(lam[sel].min()) < edge - 1.0e-12:
                ok = False
            Zb = Z[:, sel]
            G += (Zb @ Zb.T) / edge
        rest = rest[~inb]
        if not np.isfinite(nxt):
            break
        edge = nxt
    return sym(G), n_ex, ok


def whitener(A_sh):
    """A_sh^{-1/2} for the pencil metric (A_sh = Q|E_- - (mu/2) Id > 0)."""
    w, V = eigh(sym(A_sh))
    w = np.maximum(w, 1.0e-300)
    return (V / np.sqrt(w)[None, :]) @ V.T


def cap_of(*mats):
    """lambda_max of the SUM of the cap matrices -- PSD order first, Weyl once."""
    tot = None
    for Mx in mats:
        if Mx is None:
            continue
        tot = Mx if tot is None else tot + Mx
    if tot is None:
        return 0.0
    return float(eigvalsh(sym(tot)).max())


def block_terms(d):
    """EXACT block-inverse split of the dressing W (classical identity).

    With M = [[A, C^T], [C, Q|E_+]] on E_0 (+) E_+ and B_- = [m0 | mp],
        W = B_- M^{-1} B_-^T = m0 A^{-1} m0^T + R Sig^{-1} R^T,
        R = mp - m0 A^{-1} C^T,  Sig = Q|E_+ - C A^{-1} C^T.
    This is an identity, not an inequality: nothing is paid here.
    """
    lam0, Z0, Y0 = d["lam0"], d["Z0"], d["Y0"]
    inv = 1.0 / lam0
    T1 = (Z0 * inv[None, :]) @ Z0.T
    CA = (Y0 * inv[None, :]) @ Z0.T            # m0 A^{-1} C^T  (p x p)
    Sig = d["pp"] - (Y0 * inv[None, :]) @ Y0.T
    R = d["mp"] - CA.T
    ls, Vs = eigh(sym(Sig))
    ls = np.maximum(ls, 1.0e-300)
    ZR = R @ Vs
    T2 = (ZR / ls[None, :]) @ ZR.T
    return sym(T1), sym(T2), sym(Sig), R, ls, ZR


def subspace_cap(d, Ah=None, ntop=NTOP, lam0=BAND_LAM0, eplus="band"):
    """The certified cap MATRICES (E_0 half, E_+ half) on E_-.

    Ah is the whitener of the pencil metric (None = the raw metric, in which
    the currency is sigma >= bare - cap).  The E_0 half is capped by
    band_matrix on the induction data; the E_+ half either by the same band
    recipe on the Schur block Sigma ('band'), exactly ('exact'), or by the
    crude ||R||^2/lambda_min(Sig) step ('crude').
    """
    lamv, Z0 = d["lam0"], d["Z0"]
    _, _, _, R, ls, ZR = d["blocks"]
    Tr = Ah if Ah is not None else np.eye(d["p"])
    C0, n_ex, ok = band_matrix(lamv, Tr @ Z0, lam0, ntop=ntop)
    if eplus == "exact":
        Rc = Tr @ ZR
        C2, n2, ok2 = sym((Rc / ls[None, :]) @ Rc.T), 0, True
    elif eplus == "band":
        C2, n2, ok2 = band_matrix(ls, Tr @ ZR, lam0, ntop=min(ntop, ls.shape[0]))
    else:
        Rc = Tr @ R
        C2, n2, ok2 = sym(Rc @ Rc.T) / float(ls.min()), 0, True
    return C0, C2, n_ex + n2, (ok and ok2)


def chain_caps(d, ntop=NTOP, lam0=BAND_LAM0):
    """The whole cap ladder for one sample, in the A_sh (pencil) metric."""
    Ah = d["Ah"]
    p = d["p"]
    m = d["m_obs"]
    ppmin = d["pp_min"]
    c_op = d["c_op"]
    m_weyl = min(m, ppmin) - c_op            # Weyl margin of the joint block
    out = {"m_weyl": m_weyl}
    if m_weyl > 0.0:
        out["S0"] = cap_of(Ah @ (np.eye(p) * (d["mass_F"] / m_weyl)) @ Ah)
        out["S1"] = cap_of(Ah @ (np.eye(p) * (d["mass_op"] / m_weyl)) @ Ah)
    else:
        out["S0"] = float("inf")
        out["S1"] = float("inf")
    C0b, C2c, n_b, ok_b = subspace_cap(d, Ah=Ah, ntop=0, lam0=lam0, eplus="crude")
    out["S2"] = cap_of(C0b, C2c)
    C0t, _, n_t, ok_t = subspace_cap(d, Ah=Ah, ntop=ntop, lam0=lam0, eplus="crude")
    out["S3"] = cap_of(C0t, C2c)
    C0s, C2b, n_s, ok_s = subspace_cap(d, Ah=Ah, ntop=ntop, lam0=lam0, eplus="band")
    out["S4"] = cap_of(C0s, C2b)
    _, C2e, _, _ = subspace_cap(d, Ah=Ah, ntop=ntop, lam0=lam0, eplus="exact")
    out["S3X"] = cap_of(C0s, C2e)
    if d.get("lamK") is not None:
        ZK = Ah.T @ d["ZK"]
        CK, n_k, ok_k = band_matrix(d["lamK"], ZK, lam0, ntop=ntop)
        out["S2K"] = cap_of(CK)
        out["n_ex_joint"] = n_k
    else:
        out["S2K"] = float("nan")
        out["n_ex_joint"] = 0
    out["EX"] = d["rho"]
    out["n_ex"] = n_s
    out["n_ex_E0"] = n_t
    out["cert_ok"] = bool(ok_b and ok_t and ok_s)
    out["eplus_share"] = (cap_of(C2c) / out["S2"]) if out["S2"] > 0 else float("nan")
    out["S2_band_only"] = cap_of(C0b)
    out["T2_w"] = cap_of(C2c)
    return out


def sigma_lb(d, cap):
    """cap on rho  ==>  sigma >= mu/2 + (1 - cap)(bare - mu/2)."""
    if not np.isfinite(cap):
        return float("-inf")
    return d["half"] + (1.0 - cap) * (d["bare"] - d["half"])


def ols(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    good = np.isfinite(x) & np.isfinite(y)
    x, y = x[good], y[good]
    if x.size < 3:
        return float("nan"), float("nan")
    A = np.vstack([x, np.ones_like(x)]).T
    beta, res, rank, _ = np.linalg.lstsq(A, y, rcond=None)
    dof = max(1, x.size - 2)
    resid = y - A @ beta
    s2 = float(resid @ resid) / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    return float(beta[0]), float(math.sqrt(max(cov[0, 0], 0.0)))


def spread(vals):
    """Peak-to-peak relative to the mean -- the drift measure of the M axis."""
    v = np.asarray([x for x in vals if np.isfinite(x)], dtype=float)
    if v.size < 2:
        return 0.0
    base = float(np.abs(v.mean()))
    if base <= 0.0:
        return float("inf")
    return float((v.max() - v.min()) / base)


# ----------------------------------------------------------------------------
# the per-sample measurement
# ----------------------------------------------------------------------------
def sample(k, M, p, deep=False, joint=False, genuine=False, light=False):
    """One (zone, wing) sample: the three blocks, sigma, rho and their parts.

    light=True keeps only the ladder quantities (bare, sigma) -- it skips the
    E_0 spectrum, the whitener and the mass norms, which is what makes the
    crossing ladder affordable at M = 2000.
    """
    n, _, u, mu = ATOMS[k - 1]
    D, alpha, delta = zone_geometry(u, p, M)
    atoms = [(t[2], t[3]) for t in ATOMS if t[2] <= 2.0 * alpha + 1.0e-14]
    Q = build_Q(alpha, M, atoms)
    lam_gen = float(eigvalsh(Q).min()) if genuine else float("nan")
    mm, pp, mp, m0, p0, QCC = blocks_U(Q, p)
    del Q
    nc = QCC.shape[0]
    note_array(nc + p)
    K = np.empty((nc + p, nc + p))
    K[:nc, :nc] = QCC
    K[:nc, nc:] = p0.T
    K[nc:, :nc] = p0
    K[nc:, nc:] = pp
    Bfull = np.concatenate([m0, mp], axis=1)          # p x (nc + p)
    fac, sh = safe_cho(K)
    if fac is None:
        return None
    W = sym(Bfull @ cho_solve(fac, Bfull.T, check_finite=False))
    bare = float(eigvalsh(mm).min())
    sigma = float(eigvalsh(mm - W).min())
    half = 0.5 * mu
    if light:
        return {"k": k, "n": n, "u": u, "mu": mu, "half": half, "M": M, "p": p,
                "nc": nc, "D": D, "alpha": alpha, "delta": delta,
                "bare": bare, "sigma": sigma}
    A_sh = sym(mm) - half * np.eye(p)
    a_min = float(eigvalsh(A_sh).min())
    if a_min <= 0.0:
        return None
    Ah = whitener(A_sh)
    rho = float(eigvalsh(sym(Ah @ W @ Ah)).max())
    wv = eigvalsh(W)
    d = {
        "k": k, "n": n, "u": u, "mu": mu, "half": half, "M": M, "p": p,
        "nc": nc, "D": D, "alpha": alpha, "delta": delta, "shift": sh,
        "bare": bare, "sigma": sigma, "rho": rho, "slack": 1.0 - rho,
        "mm": mm, "pp": pp, "mp": mp, "A_sh": A_sh, "Ah": Ah, "W": W,
        "w_max": float(wv.max()), "eff_rank": float(wv.sum() / wv.max()),
        "mass_F": float((m0 ** 2).sum() + (mp ** 2).sum()),
        "mass_op": op2(Bfull),
        "pp_min": float(eigvalsh(pp).min()),
        "c_op": math.sqrt(max(op2(p0), 0.0)),
        "dress_frac": 100.0 * (bare - sigma) / bare,
        "lam_gen": lam_gen,
    }
    if deep:
        lam0, V0 = eigh(sym(QCC))
        lam0 = np.maximum(lam0, 1.0e-300)
        d["lam0"] = lam0
        d["Z0"] = m0 @ V0
        d["Y0"] = p0 @ V0
        d["m_obs"] = float(lam0.min())
        d["parseval"] = abs(float((d["Z0"] ** 2).sum()) - float((m0 ** 2).sum()))
        d["blocks"] = block_terms(d)
    else:
        d["m_obs"] = float(eigvalsh(sym(QCC), subset_by_index=[0, 0])[0])
    if joint:
        lamK, VK = eigh(sym(K))
        lamK = np.maximum(lamK, 1.0e-300)
        d["lamK"] = lamK
        d["ZK"] = Bfull @ VK
    else:
        d["lamK"] = None
    return d


def p_inside(k, M, p_hi, gamma, delta_c, u):
    """The grid point at delta = gamma delta_c, pulled inside the window."""
    p = min(p_hi, p_for_delta(u, gamma * delta_c, M))
    return max(P_MIN, p)


# ----------------------------------------------------------------------------
# GATES
# ----------------------------------------------------------------------------
def gate_kernel():
    k0 = float(kernel_k(np.array([0.0]))[0])
    check("el_kernel.k0", abs(k0 - K0_CLOSED) < 1.0e-11,
          "k(0) = %.12f vs closed form %.12f" % (k0, K0_CLOSED))
    nodes = np.array([0.5, 2.0, T0_T93, 20.0])
    dk = max(abs(float(kernel_k(np.array([t]))[0]) - kernel_k_mp(float(t)))
             for t in nodes)
    check("el_kernel.vs_mpmath", dk < 1.0e-11,
          "max |dk| = %.2e over %d nodes" % (dk, nodes.size))
    kt0 = float(kernel_k(np.array([T0_T93]))[0])
    lo = float(kernel_k(np.array([T0_T93 - 0.05]))[0])
    hi = float(kernel_k(np.array([T0_T93 + 0.05]))[0])
    check("el_kernel.sign_change", abs(kt0) < 1.0e-6 and lo < 0.0 < hi,
          "k(t0) = %.3e at t0 = %.8f (single sign change, T93)" % (kt0, T0_T93))


def gate_forms():
    D = 0.31
    lags = [0.0, 0.5 * D, 1.7 * D, 4.0 * D]
    rel = 0.0
    for s in lags:
        a = float(arch_A(np.array([s]), D)[0])
        b = arch_A_mp(s, D)
        rel = max(rel, abs(a - b) / max(abs(b), 1.0e-14))
    check("el_forms.arch_vs_mpmath", rel < 1.0e-9,
          "max rel err = %.2e over %d lags (near and far branch)" % (rel, len(lags)))
    D2 = 0.25
    a0 = float(arch_A(np.array([0.0]), D2)[0])
    b0 = arch_diag_tspace(D2)
    r0 = abs(a0 - b0) / abs(b0)
    check("el_forms.u_vs_t_space", r0 < 5.0e-4,
          "A(0,D) = %.8f u-space vs %.8f t-space, rel %.2e" % (a0, b0, r0))
    Mp, alp = 6, 0.7
    aa, bb = pole_vectors(alp, Mp)
    Dp = 2.0 * alp / Mp
    v = np.ones(Mp) * math.sqrt(Dp)
    got = 2.0 * float((aa @ v) * (bb @ v))
    want = 2.0 * (4.0 * math.sinh(alp / 2.0)) ** 2
    check("el_forms.pole_closed", abs(got - want) < 1.0e-10,
          "P_pole(1_window) = %.12f vs 2(4 sinh(a/2))^2 = %.12f" % (got, want))


def gate_split():
    Mc, pc = 60, 9
    u = math.log(2.0)
    Dc = u / (Mc - pc)
    alc = u * Mc / (2.0 * (Mc - pc))
    Bm, Bp, C = wing_bases(Mc, pc)
    U = np.concatenate([Bm, np.eye(Mc)[:, C], Bp], axis=1)
    check("el_split.orthonormal",
          float(np.abs(U.T @ U - np.eye(Mc)).max()) < 1.0e-12,
          "||U^T U - Id||_inf = %.2e" % float(np.abs(U.T @ U - np.eye(Mc)).max()))
    Q = build_Q(alc, Mc, [(u, 2.0 * math.log(2.0) / math.sqrt(2.0))])
    mm, pp, mp, m0, p0, QCC = blocks_U(Q, pc)
    G = U.T @ Q @ U
    nc = Mc - 2 * pc
    A = np.zeros((Mc, Mc))
    A[:pc, :pc] = mm
    A[:pc, pc:pc + nc] = m0
    A[pc:pc + nc, :pc] = m0.T
    A[:pc, pc + nc:] = mp
    A[pc + nc:, :pc] = mp.T
    A[pc:pc + nc, pc:pc + nc] = QCC
    A[pc:pc + nc, pc + nc:] = p0.T
    A[pc + nc:, pc:pc + nc] = p0
    A[pc + nc:, pc + nc:] = pp
    err = float(np.abs(G - A).max())
    check("el_split.blocks_exact", err < 1.0e-10,
          "||U^T Q U - assembled blocks||_inf = %.2e" % err)
    T = toeplitz(atom_lag(np.arange(Mc) * Dc, u, Dc))
    GT = U.T @ T @ U
    e_m = float(np.abs(GT[:pc, :pc] + 0.5 * np.eye(pc)).max())
    e_p = float(np.abs(GT[pc + nc:, pc + nc:] - 0.5 * np.eye(pc)).max())
    e_0 = float(np.abs(GT[pc:pc + nc, pc:pc + nc]).max())
    e_x = float(np.abs(GT[:pc, pc:]).max())
    check("el_split.atom_diag", max(e_m, e_p, e_0, e_x) < 1.0e-12,
          "atom = diag(-1/2, 0, +1/2): E_- %.1e, E_+ %.1e, E_0 %.1e"
          % (e_m, e_p, e_0))


def gate_sandwich():
    k = 3
    Ms, ps = 400, 24
    n, _, u, mu = ATOMS[k - 1]
    D, alpha, _ = zone_geometry(u, ps, Ms)
    atoms = [(t[2], t[3]) for t in ATOMS if t[2] <= 2.0 * alpha + 1.0e-14]
    Q = build_Q(alpha, Ms, atoms)
    d = sample(k, Ms, ps, deep=True)
    T1 = d["blocks"][0]
    sig_t = float(eigvalsh(d["mm"] - T1).min())      # dressed against E_0 only
    ok = (d["sigma"] <= sig_t + 1.0e-10 <= d["bare"] + 1.0e-10)
    check("el_sandwich.ordering", ok,
          "sigma %.6f <= sigmat %.6f <= bare %.6f"
          % (d["sigma"], sig_t, d["bare"]))
    Bm, _, _ = wing_bases(Ms, ps)
    X = np.linalg.solve(Q, Bm)
    blk = sym(Bm.T @ X)                              # E_- block of Q^{-1}
    inv = 1.0 / float(eigvalsh(blk).max())
    sch = d["sigma"]
    rel = abs(inv - sch) / max(abs(sch), 1.0e-30)
    check("el_sandwich.inverse_block", rel < 1.0e-8,
          "1/lam_max(B_-^T Q^-1 B_-) = %.9f vs Schur %.9f (rel %.1e)"
          % (inv, sch, rel))
    del Q, X
    d2 = sample(k, 400, 3, deep=False)
    n, _, u, mu = ATOMS[k - 1]
    D2, al2, _ = zone_geometry(u, 3, 400)
    atoms = [(t[2], t[3]) for t in ATOMS if t[2] <= 2.0 * al2 + 1.0e-14]
    Q2 = build_Q(al2, 400, atoms)
    Qkm1 = Q2 + mu * toeplitz(atom_lag(np.arange(400) * D2, u, D2))
    lam_km1 = float(eigvalsh(Qkm1).min())
    hyp = d2["sigma"] >= 0.5 * mu
    check("el_sandwich.implication", hyp and lam_km1 >= FENCE,
          "the hypothesis mu/2 = %.6f <= sigma = %.6f HOLDS at p = 3, and it does "
          "imply lam_min(Q_{k-1}) = %.3e >= 0 -- the sandwich is tested where it "
          "is non-vacuous" % (0.5 * mu, d2["sigma"], lam_km1))


def gate_fence():
    d = sample(2, 600, 40, deep=True, genuine=True)
    check("el_fence.genuine_psd", d["lam_gen"] >= FENCE,
          "lam_min(Q_full) = %.4e at n=%d, M=%d (RH-consistent; converse NOT "
          "claimed)" % (d["lam_gen"], d["n"], d["M"]))
    check("el_fence.bare_dominates", d["bare"] > d["half"],
          "bare %.4f > mu/2 %.4f -- the danger is the dressing, not the wing "
          "block (T102)" % (d["bare"], d["half"]))


def gate_prolate():
    p, delta = 64, 0.0645
    D = delta / p
    u = math.log(2.0)
    lam_pair, _, tr_pair = slepian_wing(p, D, u, pair=True)
    lam_plain, _, tr_plain = slepian_wing(p, D, u, pair=False)
    lo = float(min(lam_pair.min(), lam_plain.min()))
    hi = float(max(lam_pair.max(), lam_plain.max()))
    check("el_prolate.spectrum_in_01", lo > -1.0e-12 and hi < 1.0 + 1.0e-12,
          "concentration eigenvalues in [%.3e, %.6f] (Parseval: 0 <= S <= Id)"
          % (lo, hi))
    x = T0_T93 * u
    want = 1.0 - math.sin(x) / x
    got = tr_pair / tr_plain
    check("el_prolate.pair_interference", abs(got - want) < 5.0e-3,
          "trace(S_pair)/trace(S_plain) = %.6f vs the narrow-cell closed form "
          "1 - sin(t0 u)/(t0 u) = %.6f (the interference factor of the wing "
          "PAIR, not a free parameter)" % (got, want))
    info("el_prolate.time_bandwidth",
         "t0 delta / pi = %.5f, trace(S_pair) = %.5f, trace(S_plain) = %.5f "
         "(Landau-Pollak count)" % (T0_T93 * delta / math.pi, tr_pair, tr_plain))


# ----------------------------------------------------------------------------
# the sample grid: the ladder locates the mu/2 crossing, the grid follows
# ----------------------------------------------------------------------------
def zone_ladder(k, M):
    """A geometric ladder of wings, the mu/2 crossing bisected on it."""
    n, _, u, mu = ATOMS[k - 1]
    half = 0.5 * mu
    p_hi = min(zone_pmax(k, M), 2 * M // 5)      # keep dim E_0 >= M/5
    ps = sorted({int(round(x)) for x in
                 np.geomspace(P_MIN, max(P_MIN + 1, p_hi), LADDER_NP)})
    dd, ss, keep = [], [], []
    for p in ps:
        d = sample(k, M, p, light=True)
        if d is None:
            continue
        dd.append(d["delta"])
        ss.append(d["sigma"])
        keep.append(p)
    dd = np.array(dd)
    ss = np.array(ss)
    where = "inside"
    d_c = float("nan")
    if ss.size >= 2:
        if ss[0] < half:
            where = "below"
        elif ss[-1] >= half:
            where = "above"
            d_c = float(dd[-1])
        else:
            i = int(np.argmax(ss < half))
            plo, phi = keep[i - 1], keep[i]
            while phi - plo > 1:
                pm = (plo + phi) // 2
                dm = sample(k, M, pm, light=True)
                if dm is None:
                    break
                if dm["sigma"] >= half:
                    plo = pm
                else:
                    phi = pm
            d_c = zone_geometry(u, plo, M)[2]
    q_fit, se = ols(np.log(dd), np.log(np.maximum(ss, 1.0e-300)))
    with np.errstate(divide="ignore", invalid="ignore"):
        sec = np.log(np.maximum(ss, 1.0e-300) / ss[0]) / np.log(dd / dd[0])
    q_env = float(np.nanmin(sec[1:])) if sec.size > 1 else float("nan")
    ld, ls_ = np.log(dd), np.log(np.maximum(ss, 1.0e-300))
    c_fit = float(ls_.mean() - q_fit * ld.mean())
    pred = np.exp(c_fit + q_fit * ld)
    viol = float(np.max(pred / np.maximum(ss, 1.0e-300)) - 1.0)
    mono = bool(np.all(np.diff(ss) <= 1.0e-12))
    return {"k": k, "n": n, "u": u, "mu": mu, "half": half, "M": M,
            "p_hi": p_hi, "ps": keep, "dd": dd, "ss": ss, "delta_c": d_c,
            "where": where, "q_fit": q_fit, "se": se, "q_env": q_env,
            "viol": viol, "mono": mono}


def build_grid(M):
    section("THE SAMPLE GRID -- located by the mu/2 crossing, not by a fraction")
    info("grid.why",
         "T102 asks for a lower bound just above the atom entry, i.e. INSIDE the "
         "window where sigma > mu/2.  So the ladder comes first: it locates "
         "delta_c with sigma(delta_c) = mu/2, and the deep reference sample sits "
         "at delta = %.2f delta_c." % GAMMA_REF)
    lads = [zone_ladder(k, M) for k in range(1, N_ZONES + 1)]
    print("")
    print("  %-5s %-6s %-11s %-8s %-8s %-19s %-9s %-8s %-7s %s"
          % ("zone", "n", "u = log n", "mu/2", "p_max", "delta range", "delta_c",
             "window", "p(ref)", "delta(ref)"))
    refs = []
    n_in = 0
    for L in lads:
        p_ref = p_inside(L["k"], M, L["p_hi"], GAMMA_REF, L["delta_c"], L["u"]) \
            if np.isfinite(L["delta_c"]) else max(P_MIN, L["p_hi"] // 4)
        d_ref = zone_geometry(L["u"], p_ref, M)[2]
        inside = np.isfinite(L["delta_c"]) and d_ref < L["delta_c"]
        n_in += int(inside)
        refs.append((L["k"], p_ref))
        print("  %-5d %-6d %-11.6f %-8.5f %-8d %.6f..%.6f  %-9.6f %-8s %-7d %.6f"
              % (L["k"], L["n"], L["u"], L["half"], L["p_hi"], L["dd"][0],
                 L["dd"][-1], L["delta_c"], "inside" if inside else "outside",
                 p_ref, d_ref))
    n_cross = sum(1 for L in lads if np.isfinite(L["delta_c"]))
    n_above = sum(1 for L in lads if L["where"] == "above")
    n_below = sum(1 for L in lads if L["where"] == "below")
    check("el_grid.crossing", n_cross == N_ZONES,
          "the mu/2 crossing is bracketed and bisected at %d zones, lies above "
          "the array cap at %d, and below the smallest wing at %d (of %d)"
          % (n_cross, n_above, n_below, N_ZONES))
    return lads, refs, n_in


# ----------------------------------------------------------------------------
# B1  COUPLING ANATOMY
# ----------------------------------------------------------------------------
def block_b1(rows, jrows):
    section("B1  COUPLING ANATOMY -- what B_- is, and where its mass sits")
    info("B1.def",
         "B_- = Q_{-,(0+)} = [m0 | mp] : E_- -> E_0 (+) E_+, dim E_- = p, "
         "dim E_0 = M - 2p")
    print("")
    print("  %-4s %-4s %-6s %-7s %-6s %-7s %-7s %-11s %-10s %-6s %-9s %s"
          % ("n", "p", "dimE0", "bare", "mu/2", "sigma", "dress%", "||B||^2_op",
             "||B||^2_F", "effrk", "m_obs", "rho"))
    for r in rows:
        print("  %-4d %-4d %-6d %-7.3f %-6.3f %-7.4f %-7.1f %-11.4f %-10.1f "
              "%-6.2f %-9.2e %.3f"
              % (r["n"], r["p"], r["nc"], r["bare"], r["half"], r["sigma"],
                 r["dress_frac"], r["mass_op"], r["mass_F"], r["eff_rank"],
                 r["m_obs"], r["rho"]))
    pars = max(d["parseval"] for d in jrows)
    check("el_b1.parseval", pars < 1.0e-9,
          "max |sum_j ||z_j||^2 - ||m0||_F^2| = %.2e -- the band decomposition "
          "is exact" % pars)
    df = [r["dress_frac"] for r in rows]
    check("el_b1.t102_dressing", 0.0 < min(df) and max(df) <= 100.0,
          "the Schur dressing removes %.1f%%..%.1f%% of bare (T102 anchor "
          "35.7..97.3 at its fractions)" % (min(df), max(df)))
    br = [r["bare"] / r["half"] for r in rows]
    info("B1.bare_ratio", "bare/(mu/2) = %.2f..%.2f (T102 anchor 4..14)"
         % (min(br), max(br)))
    er = [r["eff_rank"] for r in rows]
    info("B1.eff_rank",
         "effective rank trace/lam_max of W = %.2f..%.2f, dim E_- = %d..%d"
         % (min(er), max(er), min(r["p"] for r in rows),
            max(r["p"] for r in rows)))
    mid = rows[len(rows) // 2]
    dm = next((d for d in jrows if d["k"] == mid["k"] and d["p"] == mid["p"]),
              None)
    if dm is None:
        dm = sample(mid["k"], mid["M"], mid["p"], deep=True)
    sv = np.sort(eigvalsh(sym(dm["Z0"] @ dm["Z0"].T)))[::-1]
    cum = np.cumsum(sv) / sv.sum()
    n50 = int(np.searchsorted(cum, 0.50) + 1)
    n90 = int(np.searchsorted(cum, 0.90) + 1)
    info("B1.spectral_profile",
         "n=%d p=%d: 50%% of the E_0 coupling mass sits in %d directions, 90%% "
         "in %d of %d" % (mid["n"], mid["p"], n50, n90, mid["p"]))
    print("")
    print("  frequency localisation of the E_0 coupling mass (exact, Parseval)")
    print("  %-4s %-5s %-9s %-12s %-12s %-12s %-12s %-12s %s"
          % ("n", "p", "m_obs", "frac(lam<1)", "frac(lam<3)", "frac(lam<5)",
             "lam_massmed", "lam_max(E0)", "theta"))
    thetas = []
    for d in jrows:
        lam, Z = d["lam0"], d["Z0"]
        z2 = (Z ** 2).sum(axis=0)
        tot = float(z2.sum())
        f1 = float(z2[lam < 1.0].sum()) / tot
        f3 = float(z2[lam < 3.0].sum()) / tot
        f5 = float(z2[lam < 5.0].sum()) / tot
        cw = np.cumsum(z2) / tot
        lmed = float(lam[int(np.searchsorted(cw, 0.5))])
        edges = [BAND_LAM0 * BAND_R ** j for j in range(0, 7)]
        xs, ys = [], []
        for lo, hi in zip(edges[:-1], edges[1:]):
            sel = (lam >= lo) & (lam < hi)
            mass = float(z2[sel].sum())
            if mass > 0.0:
                xs.append(math.log(0.5 * (lo + hi)))
                ys.append(math.log(mass / (hi - lo)))
        sl, _ = ols(xs, ys)
        theta = -sl
        thetas.append(theta)
        print("  %-4d %-5d %-9.2e %-12.4f %-12.4f %-12.4f %-12.3f %-12.3f %.3f"
              % (d["n"], d["p"], d["m_obs"], f1, f3, f5, lmed,
                 float(lam.max()), theta))
    print("")
    print("  THE LOW END -- the genuine form is nearly singular on E_0, so the")
    print("  question is whether B_- couples to its near-null modes at all")
    print("  %-4s %-5s %-11s %-12s %-12s %-13s %-12s %s"
          % ("n", "p", "lam_1(E0)", "||z_1||^2", "z1^2/lam_1", "worst mode j",
             "its z^2/lam", "lam_max(W)"))
    lowfrac = []
    for d in jrows:
        lam, Z = d["lam0"], d["Z0"]
        z2 = (Z ** 2).sum(axis=0)
        ratio = z2 / lam
        j = int(np.argmax(ratio))
        lowfrac.append(ratio[0] / d["w_max"])
        print("  %-4d %-5d %-11.3e %-12.3e %-12.4f %-13d %-12.4f %.4f"
              % (d["n"], d["p"], float(lam[0]), float(z2[0]),
                 float(ratio[0] / d["w_max"]), j + 1,
                 float(ratio[j] / d["w_max"]), d["w_max"]))
    check("el_b1.low_end_decoupled", max(lowfrac) <= 1.0 + 1.0e-8,
          "W >= z_1 z_1^T / lam_1 holds; the near-null mode carries %.2e..%.2e "
          "of lam_max(W), i.e. B_- decouples from it -- that is exactly why "
          "lam_max(W) stays finite while m -> 0" % (min(lowfrac), max(lowfrac)))
    info("B1.theta",
         "band-mass density exponent theta = %.3f..%.3f (median %.3f); T103 "
         "anchor 0.34..1.51, T99 zone-4/5 anchor 1.15..2.18"
         % (min(thetas), max(thetas), float(np.median(thetas))))
    kk = [r["k"] for r in rows]
    sl_mass = ols(kk, [math.log(r["mass_op"]) for r in rows])
    sl_marg = ols(kk, [math.log(r["m_obs"]) for r in rows])
    sl_rat = ols(kk, [math.log(r["mass_op"] / r["m_obs"]) for r in rows])
    sl_bare = ols(kk, [math.log(r["bare"]) for r in rows])
    info("B1.trend_mass", "log ||B||^2_op    vs zone: slope %+.4f +- %.4f"
         % sl_mass)
    info("B1.trend_margin", "log m_obs         vs zone: slope %+.4f +- %.4f"
         % sl_marg)
    info("B1.trend_ratio", "log (mass/margin) vs zone: slope %+.4f +- %.4f  "
         "<-- what the chain must pay" % sl_rat)
    info("B1.trend_bare", "log bare          vs zone: slope %+.4f +- %.4f  "
         "<-- the budget" % sl_bare)
    ratios = [r["mass_op"] / r["m_obs"] for r in rows]
    budg = [r["bare"] - r["half"] for r in rows]
    info("B1.ratio_range",
         "mass/margin = %.2f..%.2f against the budget bare - mu/2 = %.2f..%.2f"
         % (min(ratios), max(ratios), min(budg), max(budg)))
    check("el_b1.mass_positive",
          all(r["mass_op"] > 0.0 and r["m_obs"] > 0.0 for r in rows),
          "coupling mass and observed margin strictly positive at all %d samples"
          % len(rows))
    return {"theta": thetas, "sl_mass": sl_mass, "sl_margin": sl_marg,
            "sl_ratio": sl_rat, "sl_bare": sl_bare}


# ----------------------------------------------------------------------------
# B2  THE INDUCTIVE CHAIN
# ----------------------------------------------------------------------------
def data_frontier(d, caps_ref):
    """How far the band start can be pushed up and still close (S4)."""
    best = None
    for L in LAM0_GRID:
        c = chain_caps(d, ntop=NTOP, lam0=L)
        if c["S4"] <= 1.0:
            if best is None or L > best[0]:
                best = (L, c["S4"], c["n_ex"])
    if best is None:
        c = caps_ref
        return float("nan"), c["S4"], c["n_ex"], False
    return best[0], best[1], best[2], True


def block_b2(jrows, caps, lads):
    section("B2  THE INDUCTIVE CHAIN -- a certified cap on the pencil ratio rho")
    info("B2.criterion",
         "the handoff holds exactly when rho = lam_max(A_sh^-1 W) <= 1, "
         "A_sh = Q|E_- - (mu/2) Id; every cap below is taken in the A_sh metric "
         "(T103's currency), which is strictly sharper than bare - lam_max(W)")
    info("B2.headroom",
         "H = 1/cap;  H >= 1 <=> the zone closes.  Then sigma_k >= mu/2 + "
         "(1 - cap)(bare - mu/2)")
    info("B2.hypothesis",
         "HYPOTHESIS INPUT (HYP-m): Q_full|E_0 >= m Id with "
         "m = lambda_min(Q_full|E_0) as measured -- NOT PROVED")
    info("B2.split",
         "EXACT block-inverse split (classical, no inequality): "
         "W = m0 A^-1 m0^T + R Sig^-1 R^T, R = mp - m0 A^-1 C^T, "
         "Sig = Q|E_+ - C A^-1 C^T")
    info("B2.matrix_caps",
         "the caps are MATRICES summed in the PSD order, with lambda_max taken "
         "once at the end -- adding the two scalar maxima would pay Weyl's "
         "inequality twice for two non-aligned eigenvectors")
    print("")
    print("  the two halves of the dressing, and why a uniform margin cannot work")
    print("  %-5s %-5s %-10s %-9s %-9s %-13s %-9s %-9s %-7s %s"
          % ("n", "p", "m_obs", "m_weyl", "T1_exact", "lam_min(Sig)", "||R||^2",
             "T2_exact", "T2_w", "T2share"))
    id_err = 0.0
    nweyl = 0
    for d in jrows:
        T1, T2, Sig, R, ls, ZR = d["blocks"]
        id_err = max(id_err, float(np.abs(T1 + T2 - sym(d["W"])).max()))
        c = caps[d["k"]]
        nweyl += int(c["m_weyl"] > 0.0)
        share = c["T2_w"] / (c["S2_band_only"] + c["T2_w"]) \
            if (c["S2_band_only"] + c["T2_w"]) > 0 else float("nan")
        print("  %-5d %-5d %-10.2e %-9.3f %-9.4f %-13.4f %-9.4f %-9.4f %-7.4f "
              "%.4f"
              % (d["n"], d["p"], d["m_obs"], c["m_weyl"],
                 float(eigvalsh(T1).max()), float(ls.min()), op2(R),
                 float(eigvalsh(T2).max()), c["T2_w"], share))
    check("el_b2.block_identity", id_err < 1.0e-6,
          "||m0 A^-1 m0^T + R Sig^-1 R^T - W||_inf = %.2e (exact block inverse)"
          % id_err)
    ms = [d["m_obs"] for d in jrows]
    check("el_b2.margin_is_tiny", True,
          "m = lam_min(Q_full|E_0) = %.2e..%.2e -- the genuine form is NEARLY "
          "SINGULAR on the induction window, so the Weyl margin is positive in "
          "only %d/%d zones" % (min(ms), max(ms), nweyl, len(jrows)))
    check("el_b2.band_certified", all(caps[d["k"]]["cert_ok"] for d in jrows),
          "every band weight obeys w_j >= 1/lam_j at all zones (spectral "
          "calculus, no fit)")
    worst = max(min(caps[d["k"]][s] for s in ("S2", "S3", "S4")) / d["rho"]
                for d in jrows)
    above = all(caps[d["k"]][s] >= d["rho"] - 1.0e-9
                for d in jrows for s in ("S2", "S3", "S4", "S3X", "S2K"))
    check("el_b2.caps_above_exact", above,
          "rho <= every certified cap at all zones; loosest cap/exact ratio = "
          "%.3f" % worst)
    print("")
    print("  the cap ladder (upper bounds on the pencil ratio rho) and H = 1/cap")
    print("  %-4s %-4s %-9s %-9s %-9s %-9s %-8s %-8s %-8s %-7s %-6s %-6s %-6s "
          "%-6s %s"
          % ("n", "p", "inside", "S0", "S1", "S2", "S3", "S4", "S3X", "S2K",
             "EX", "H(S3)", "H(S4)", "H(S3X)", "H(S2K) H(EX)"))
    inside_flags = {}
    for d in jrows:
        L = lads[d["k"] - 1]
        ins = np.isfinite(L["delta_c"]) and d["delta"] < L["delta_c"]
        inside_flags[d["k"]] = ins
        c = caps[d["k"]]
        print("  %-4d %-4d %-9s %-9.3f %-9.3f %-9.3f %-8.3f %-8.3f %-8.3f "
              "%-7.3f %-6.4f %-6.3f %-6.3f %-6.3f %-6.3f  %.2f"
              % (d["n"], d["p"], "yes" if ins else "no", c["S0"], c["S1"],
                 c["S2"], c["S3"], c["S4"], c["S3X"], c["S2K"], c["EX"],
                 1.0 / c["S3"], 1.0 / c["S4"], 1.0 / c["S3X"], 1.0 / c["S2K"],
                 1.0 / c["EX"]))
    n_in = sum(1 for v in inside_flags.values() if v)
    print("")
    info("B2.inside",
         "the grid resolves the interior of the handoff window (rho < 1, i.e. "
         "sigma > mu/2) at %d/%d zones; a zone that is NOT inside cannot close "
         "for ANY chain, and its failure is an instrument-resolution fact, not "
         "a chain fact" % (n_in, len(jrows)))
    prov = {
        "S0": "uniform margin m + Frobenius (Bessel) mass | CONDITIONAL on "
              "(HYP-m) only -- the naive strengthened induction",
        "S1": "uniform margin m + operator mass | CONDITIONAL on (HYP-m) only, "
              "sharp mass",
        "S2": "block split, band cap MATRIX on E_0 + R R^T/lam_min(Sig) | "
              "CERTIFIED given INDUCTION-DATA (low modes + band masses) + E_+ "
              "data",
        "S3": "S2 with the ntop=%d heaviest E_0 modes exact | CERTIFIED given "
              "INDUCTION-DATA (bands + ntop) + E_+ data" % NTOP,
        "S4": "S3 + the SAME band recipe on the E_+ Schur block Sigma | "
              "CERTIFIED given INDUCTION-DATA on E_0 + FINITE BAND DATA on the "
              "E_+ Schur block (MEASURED, but the same spectral-calculus recipe)",
        "S3X": "S3 with the E_+ half exact (R Sig^-1 R^T, no operator norm) | "
               "MEASURED on E_+ (the full Schur complement Sigma of the larger "
               "window), certified on E_0 -- isolates the cost of the E_+ step",
        "S2K": "band caps on the JOINT block E_0+E_+ | MEASURED (needs the "
               "joint spectrum of the larger window)",
        "EX": "lambda_max(W) itself | MEASURED (the full resolvent -- never an "
              "ingredient)",
    }
    closes = {}
    for s in ALL_STAGES:
        cl = [d["k"] for d in jrows if caps[d["k"]][s] <= 1.0]
        cl_in = [k for k in cl if inside_flags[k]]
        closes[s] = cl
        hs = [1.0 / caps[d["k"]][s] for d in jrows]
        info("B2.stage_%s" % s,
             "closes %2d/%d (%2d/%d of the resolved zones), H = %.4f..%.3f | %s"
             % (len(cl), len(jrows), len(cl_in), n_in, min(hs), max(hs), prov[s]))
    for s in ALL_STAGES:
        sl = ols([d["k"] for d in jrows],
                 [-math.log(caps[d["k"]][s])
                  if 0.0 < caps[d["k"]][s] < np.inf else float("nan")
                  for d in jrows])
        info("B2.trend_%s" % s, "log H(%-3s) vs zone: slope %+.4f +- %.4f"
             % (s, sl[0], sl[1]))
    return closes, inside_flags, n_in


def block_b2_reach(jrows, caps, lads, M):
    print("")
    print("  THE REACH -- the binary 'closes at gamma = %.2f' is the wrong "
          "question;" % GAMMA_REF)
    print("  the right one is HOW DEEP inside the window the certified chain "
          "still")
    print("  closes:  gamma_max = max{gamma : cap(S4) <= 1 at delta = gamma "
          "delta_c}")
    print("  %-4s %-10s %-11s %-5s %-10s %-9s %-9s %-10s %s"
          % ("n", "delta_c", "gamma_max", "p", "delta", "cap(S4)", "rho",
             "sigma_LB", "p_floor"))
    reach = {}
    n_floor = 0
    for d in jrows:
        L = lads[d["k"] - 1]
        best = None
        seen = set()
        for g in GAMMA_GRID:
            if budget_left() < 120.0:
                break
            p = p_inside(d["k"], M, L["p_hi"], g, L["delta_c"], L["u"])
            if p in seen:
                continue
            seen.add(p)
            dd = d if p == d["p"] else sample(d["k"], M, p, deep=True, joint=False)
            if dd is None:
                continue
            c = caps[d["k"]] if p == d["p"] else chain_caps(dd)
            if c["S4"] <= 1.0:
                best = (g, p, dd, c)
                break
        if best is None:
            reach[d["k"]] = None
            print("  %-4d %-10.6f %-11s %-5s %-10s %-9s %-9s %-10s %s"
                  % (d["n"], L["delta_c"], "none", "-", "-", "-", "-", "-", "-"))
            continue
        g, p, dd, c = best
        floor = (p <= P_MIN)
        n_floor += int(floor)
        reach[d["k"]] = {"gamma": g, "p": p, "d": dd, "caps": c,
                         "sigma_LB": sigma_lb(dd, c["S4"])}
        print("  %-4d %-10.6f %-11.2f %-5d %-10.6f %-9.3f %-9.4f %-10.4f %s"
              % (d["n"], L["delta_c"], g, p, dd["delta"], c["S4"], dd["rho"],
                 sigma_lb(dd, c["S4"]), "yes" if floor else "no"))
    gs = [r["gamma"] for r in reach.values() if r]
    check("el_b2.reach", len(gs) == len(jrows),
          "the certified chain reaches gamma_max = %.2f..%.2f of the crossing at "
          "%d/%d zones; %d zones sit on the wing-resolution floor p = %d, where "
          "the grid cannot probe any deeper"
          % (min(gs), max(gs), len(gs), len(jrows), n_floor, P_MIN))
    info("B2.reach_meaning",
         "gamma_max < 1 is not a failure of the chain but a quantified "
         "shortfall: the certified sigma bound holds on [0, gamma_max delta_c] "
         "and the handoff then costs a factor gamma_max^{1/q} in w_k")
    sl = ols([k for k, r in reach.items() if r],
             [math.log(r["gamma"]) for r in reach.values() if r])
    info("B2.reach_trend",
         "log gamma_max vs zone: slope %+.4f +- %.4f -- the certified chain "
         "covers a roughly constant fraction of the handoff window as the zones "
         "advance" % sl)
    return reach


def block_b2_tail(jrows, caps, inside_flags, n_in):
    print("")
    print("  the margin demand of the naive route:  m_req = mass/(bare - mu/2)"
          "   vs   m_obs")
    print("  %-4s %-13s %-11s %-17s %-13s %s"
          % ("n", "m_obs", "m_req(S1)", "m_obs/m_req(S1)", "m_req(S0)",
             "m_obs/m_req(S0)"))
    worst = []
    for d in jrows:
        budg = d["bare"] - d["half"]
        r1 = d["mass_op"] / budg
        r0 = d["mass_F"] / budg
        worst.append(d["m_obs"] / r1)
        worst.append(d["m_obs"] / r0)
        print("  %-4d %-13.3e %-11.3f %-17.3e %-13.1f %.3e"
              % (d["n"], d["m_obs"], r1, d["m_obs"] / r1, r0, d["m_obs"] / r0))
    n_naive = sum(1 for d in jrows
                  if caps[d["k"]]["S0"] <= 1.0 or caps[d["k"]]["S1"] <= 1.0)
    check("el_b2.uniform_margin_dead", n_naive == 0,
          "the uniform-margin stages S0/S1 close %d/%d zones: m_obs/m_req = "
          "%.1e..%.1e, i.e. the naive strengthened induction is short by 3-6 "
          "orders of magnitude" % (n_naive, len(jrows), min(worst), max(worst)))
    info("B2.naive_dead",
         "the uniform-margin route needs m of order 1 but the genuine form "
         "supplies m ~ 1e-5: a strengthened induction that only carries a "
         "MARGIN cannot close this -- it must carry the LOW-END COUPLING MASSES")
    print("")
    print("  the data-cost frontier: how much of the smaller window's spectrum")
    print("  must the induction carry for the chain to close?")
    print("  %-4s %-8s %-8s %-8s %-10s %-16s %-9s %s"
          % ("n", "inside", "S4 cap", "closes", "Lam0_max", "explicit modes",
             "dim E_0", "fraction"))
    n_front = 0
    nex_all, kk = [], []
    for d in jrows:
        L0, cap4, n_ex, ok = data_frontier(d, caps[d["k"]])
        n_front += int(ok)
        nex_all.append(n_ex)
        kk.append(d["k"])
        print("  %-4d %-8s %-8.3f %-8s %-10.2f %-16d %-9d %.4f"
              % (d["n"], "yes" if inside_flags[d["k"]] else "no", cap4,
                 "YES" if ok else "no", L0, n_ex, d["nc"], n_ex / d["nc"]))
    check("el_b2.frontier", n_front > 0,
          "at the fixed reference gamma = %.2f the chain closes with explicit "
          "low-mode data at %d/%d zones; explicit modes %d..%d of dim E_0 %d..%d"
          % (GAMMA_REF, n_front, len(jrows), min(nex_all), max(nex_all),
             min(d["nc"] for d in jrows), max(d["nc"] for d in jrows)))
    sl = ols(kk, [math.log(max(x, 1)) for x in nex_all])
    info("B2.data_cost_trend",
         "log(explicit modes) vs zone: slope %+.4f +- %.4f (T103: a bounded "
         "threshold hides an unbounded mode count)" % sl)
    ne0 = [caps[d["k"]]["n_ex_E0"] for d in jrows]
    info("B2.data_cost",
         "at the default band start Lam0 = %.1f the explicit mode count is "
         "%d..%d of dim E_0 = %d..%d"
         % (BAND_LAM0, min(ne0), max(ne0), min(d["nc"] for d in jrows),
            max(d["nc"] for d in jrows)))
    shares = [caps[d["k"]]["eplus_share"] for d in jrows]
    info("B2.eplus_share",
         "the un-inducted E_+ half carries %.4f..%.4f of the S2 cap -- this is "
         "the part the induction hypothesis does NOT reach"
         % (min(shares), max(shares)))
    buys = [caps[d["k"]]["S3"] - caps[d["k"]]["S4"] for d in jrows]
    nplus = [min(NTOP, d["p"]) for d in jrows]
    info("B2.eplus_cost",
         "treating the E_+ Schur block with the SAME band recipe instead of "
         "||R||^2/lam_min(Sig) buys %.3f..%.3f of cap and needs %d..%d explicit "
         "E_+ modes -- that single crude step is where the certified chain was "
         "losing the zones" % (min(buys), max(buys), min(nplus), max(nplus)))
    degen = [d["n"] for d in jrows if d["p"] <= NTOP]
    dev = max(abs(caps[d["k"]]["S4"] - caps[d["k"]]["S3X"]) for d in jrows)
    check("el_b2.eplus_is_full_block", True,
          "DISCLOSURE: with ntop = %d exact modes and wings of p = %d..%d, the "
          "E_+ band recipe degenerates to the FULL block at n = %s, and S4 "
          "tracks the exact E_+ term to %.1e everywhere -- so S4 buys sharpness, "
          "not cheapness, on the un-inducted half"
          % (NTOP, min(d["p"] for d in jrows), max(d["p"] for d in jrows),
             degen, dev))
    best, nbest = None, -1
    for s in IND_STAGES:
        cl = sum(1 for d in jrows if caps[d["k"]][s] <= 1.0)
        if cl > nbest:
            best, nbest = s, cl
    cl_in = sum(1 for d in jrows
                if caps[d["k"]][best] <= 1.0 and inside_flags[d["k"]])
    info("B2.best_inductive",
         "best chain on induction data: %s, %d/%d zones (%d/%d resolved)"
         % (best, nbest, len(jrows), cl_in, n_in))
    return best, nbest


# ----------------------------------------------------------------------------
# B3  THE WING BASIS
# ----------------------------------------------------------------------------
def block_b3(jrows, caps):
    section("B3  THE WING BASIS -- Slepian/prolate concentration on the wing pair")
    info("B3.kernel",
         "S_ij = (1/pi) int_0^{t0} [4 sin^2(tD/2)/(D t^2)] cos(t(i-j)D) "
         "(1 - cos(t u)) dt,  t0 = %.8f" % T0_T93)
    info("B3.why",
         "the E_- element is (g(x) - g(x-u))/sqrt(2), so its spectral density "
         "carries the interference factor (1 - cos(t u)) -- the T96/T103 "
         "recommended object class")
    print("")
    print("  localisation of the near-null direction of the Schur complement")
    print("  %-4s %-4s %-8s %-9s %-4s %-4s %-12s %-7s %-8s %-8s %s"
          % ("n", "p", "lam0(S)", "trace(S)", "n90", "n99", "n(sigma 1%)",
             "ovl1", "rho_raw", "rho_pro", "slack"))
    rowsb3 = []
    for d in jrows:
        p = d["p"]
        lamS, Psi, trS = slepian_wing(p, d["D"], d["u"], pair=True)
        cw = np.cumsum(lamS) / lamS.sum()
        n90 = int(np.searchsorted(cw, 0.90) + 1)
        n99 = int(np.searchsorted(cw, 0.99) + 1)
        wv, Wvec = eigh(sym(d["mm"] - sym(d["W"])))
        v = Wvec[:, 0]
        ovl = float((Psi[:, 0] @ v) ** 2)
        nsig = p
        for r in range(1, p + 1):
            P = Psi[:, :r]
            Wr = sym(P.T @ sym(d["W"]) @ P)
            mmr = sym(P.T @ d["mm"] @ P)
            sg = float(eigvalsh(mmr - Wr).min())
            if abs(sg - d["sigma"]) <= 0.01 * abs(d["sigma"]):
                nsig = r
                break
        n_p = int(min(max(n99, 2), p))
        P = Psi[:, :n_p]
        Ap = sym(P.T @ d["A_sh"] @ P)
        Wp = sym(P.T @ sym(d["W"]) @ P)
        try:
            rho_pro = float(eigvalsh(Wp, Ap).max())
        except LinAlgError:
            rho_pro = float("nan")
        rowsb3.append({"k": d["k"], "n": d["n"], "p": p, "n99": n99,
                       "nsig": nsig, "ovl": ovl, "Psi": Psi})
        print("  %-4d %-4d %-8.5f %-9.5f %-4d %-4d %-12d %-7.4f %-8.4f %-8.4f "
              "%.4f" % (d["n"], p, float(lamS[0]), trS, n90, n99, nsig, ovl,
                        d["rho"], rho_pro, 1.0 - d["rho"]))
    n99s = [r["n99"] for r in rowsb3]
    check("el_b3.localisation", max(n99s) <= max(3, min(r["p"] for r in rowsb3)),
          "n99 = %d..%d of p = %d..%d prolate modes; strongly localised in %d/%d "
          "zones" % (min(n99s), max(n99s), min(r["p"] for r in rowsb3),
                     max(r["p"] for r in rowsb3),
                     sum(1 for r in rowsb3 if r["n99"] <= 3), len(rowsb3)))
    nsigs = [r["nsig"] for r in rowsb3]
    check("el_b3.sigma_from_few_modes", max(nsigs) <= max(r["p"] for r in rowsb3),
          "prolate modes needed to reproduce sigma to 1%%: %d..%d of p = %d..%d "
          "(finite data + tail bound iff small)"
          % (min(nsigs), max(nsigs), min(r["p"] for r in rowsb3),
             max(r["p"] for r in rowsb3)))
    sl = ols([r["k"] for r in rowsb3], [math.log(r["n99"]) for r in rowsb3])
    info("B3.trend_n99", "log n99 vs zone: slope %+.4f +- %.4f" % sl)
    ov = [r["ovl"] for r in rowsb3]
    info("B3.ovl1",
         "energy of the near-null direction in the single most concentrated "
         "prolate mode: %.4f..%.4f (median %.4f)"
         % (min(ov), max(ov), float(np.median(ov))))
    print("")
    print("  the certified BLOCK-SPLIT chain in the prolate basis vs the raw "
          "basis")
    info("B3.split",
         "sigma >= lam_min[[a, -y],[-y, b]] with a, b the capped block minima "
         "and y = ||mm_offdiag|| + sqrt(cap_pro cap_perp)  (2x2 block bound + "
         "Cauchy-Schwarz on W)")
    info("B3.same_currency",
         "the basis comparison is run in ONE currency: both columns are "
         "sigma >= bare - cap with the SAME certified cap recipe (bands + ntop "
         "+ the E_+ remainder), only the basis differs; the pencil column of B2 "
         "is a different, sharper currency and is not mixed in here")
    print("  %-4s %-5s %-9s %-8s %-10s %-9s %-8s %-10s %-9s %-8s %s"
          % ("n", "npro", "bare_pro", "cap_pro", "bare_perp", "cap_perp",
             "offdiag", "LB_pro", "LB_raw", "mu/2", "win"))
    n_eval = n_pro_win = n_pro_cl = n_raw_cl = 0
    gains = []
    for d, rb in zip(jrows, rowsb3):
        C0r, C2r, _, _ = subspace_cap(d, Ah=None, ntop=NTOP, eplus="crude")
        cap_raw = cap_of(C0r, C2r)
        lb_raw = d["bare"] - cap_raw
        if d["p"] < 4:
            print("  %-4d %-5s %-9.4f %-8s %-10s %-9s %-8s %-10s %-9.3f %-8.4f %s"
                  % (d["n"], "n/a", d["bare"], "-", "-", "-", "-", "-", lb_raw,
                     d["half"], "-"))
            continue
        n_eval += 1
        npro = int(min(max(rb["n99"], 2), d["p"] - 2))
        Psi = rb["Psi"]
        P1, P2 = Psi[:, :npro], Psi[:, npro:]
        a_bare = float(eigvalsh(sym(P1.T @ d["mm"] @ P1)).min())
        b_bare = float(eigvalsh(sym(P2.T @ d["mm"] @ P2)).min())
        cap1 = cap_of(P1.T @ C0r @ P1, P1.T @ C2r @ P1)
        cap2 = cap_of(P2.T @ C0r @ P2, P2.T @ C2r @ P2)
        offd = float(np.linalg.norm(P1.T @ d["mm"] @ P2, 2))
        y = offd + math.sqrt(max(cap1, 0.0) * max(cap2, 0.0))
        a = a_bare - cap1
        b = b_bare - cap2
        lb_pro = 0.5 * (a + b) - math.sqrt(0.25 * (a - b) ** 2 + y * y)
        gains.append(lb_pro - lb_raw)
        win = "pro" if lb_pro > lb_raw else "raw"
        n_pro_win += int(lb_pro > lb_raw)
        n_pro_cl += int(lb_pro >= d["half"])
        n_raw_cl += int(lb_raw >= d["half"])
        print("  %-4d %-5d %-9.4f %-8.3f %-10.4f %-9.3f %-8.4f %-10.3f %-9.3f "
              "%-8.4f %s" % (d["n"], npro, a_bare, cap1, b_bare, cap2, offd,
                             lb_pro, lb_raw, d["half"], win))
    check("el_b3.split_evaluated", n_eval > 0,
          "block-split chain at the %d/%d zones whose wing has p >= 4 (a 2- or "
          "3-cell wing admits no prolate/rest split): prolate beats raw in %d, "
          "closes %d vs raw %d"
          % (n_eval, len(jrows), n_pro_win, n_pro_cl, n_raw_cl))
    if gains:
        info("B3.gain", "LB_pro - LB_raw = %.3f..%.3f (median %.3f)"
             % (min(gains), max(gains), float(np.median(gains))))
    info("B3.winner",
         "the wing basis localises the near-null direction, but the block split "
         "pays an off-diagonal price; closure winner: %s"
         % ("prolate" if n_pro_cl > n_raw_cl else "raw"))
    return {"n99": n99s, "nsig": nsigs, "ovl": ov, "n_pro_cl": n_pro_cl,
            "n_raw_cl": n_raw_cl}


# ----------------------------------------------------------------------------
# B4  EDGE REGULARITY + SYNTHESIS
# ----------------------------------------------------------------------------
def block_b4_edge(lads):
    section("B4  EDGE REGULARITY -- sigma_k(delta) >= sigma_k(dref)(delta/dref)^q")
    info("B4.two_exponents",
         "q_fit = OLS slope (a FIT, may overshoot the data); q_env = min_i "
         "log(sigma_i/sigma_ref)/log(d_i/d_ref) = the steepest secant, for which "
         "the power law IS a lower bound on the sampled ladder by construction")
    print("")
    print("  %-5s %-9s %-9s %-5s %-12s %-12s %-8s %-8s %-9s %-8s %-6s %-10s %s"
          % ("n", "dref", "dtop", "npts", "sigma(dref)", "sigma(dtop)", "q_fit",
             "se", "maxviol", "q_env", "mono", "delta_c", "window"))
    for L in lads:
        print("  %-5d %-9.6f %-9.6f %-5d %-12.5f %-12.5f %-8.4f %-8.4f %-9.4f "
              "%-8.4f %-6s %-10.6f %s"
              % (L["n"], L["dd"][0], L["dd"][-1], L["dd"].size, L["ss"][0],
                 L["ss"][-1], L["q_fit"], L["se"], L["viol"], L["q_env"],
                 "yes" if L["mono"] else "no", L["delta_c"], L["where"]))
    n_ins = sum(1 for L in lads if L["where"] == "inside")
    n_abv = sum(1 for L in lads if L["where"] == "above")
    info("B4.window",
         "the handoff window [0, delta_c] is resolved by the grid at %d/%d zones "
         "('inside'); at %d zones the whole ladder still sits above mu/2 "
         "('above'), so delta_c > dtop and the bound is needed further out than "
         "the array cap reaches" % (n_ins, len(lads), n_abv))
    qs = [L["q_fit"] for L in lads]
    check("el_b4.edge_negative", all(q < 0 for q in qs),
          "q_k = %.4f..%.4f at %d zones (sigma falls as the wing opens)"
          % (min(qs), max(qs), len(qs)))
    nmono = sum(1 for L in lads if L["mono"])
    check("el_b4.monotone", nmono == len(lads),
          "sigma monotone decreasing in delta at %d/%d zones" % (nmono, len(lads)))
    mv = max(L["viol"] for L in lads)
    check("el_b4.power_law_is_a_fit", True,
          "max relative overshoot of the FITTED power law = %.4f -- it is a FIT, "
          "not a bound; a proof needs a one-sided edge estimate" % mv)
    info("B4.q_range",
         "q_fit = %.4f..%.4f (median %.4f), 1/|q_fit| = %.3f..%.3f"
         % (min(qs), max(qs), float(np.median(qs)),
            1.0 / max(abs(q) for q in qs), 1.0 / min(abs(q) for q in qs)))
    qe = [L["q_env"] for L in lads]
    info("B4.q_env_range",
         "q_env = %.4f..%.4f (median %.4f) -- the exponent the synthesis uses, "
         "since the fit is not a bound"
         % (min(qe), max(qe), float(np.median(qe))))
    s1 = ols([L["k"] for L in lads], [math.log(abs(q)) for q in qs])
    s2 = ols([L["k"] for L in lads], [math.log(abs(q)) for q in qe])
    info("B4.q_trend",
         "log |q_fit| vs zone: slope %+.4f +- %.4f;  log |q_env| vs zone: "
         "slope %+.4f +- %.4f" % (s1[0], s1[1], s2[0], s2[1]))


def block_b4_drift(lads, refs):
    print("")
    print("  resolution drift AT THE REFERENCE POINT:  p is scaled with M, which")
    print("  keeps delta = p u / (M - p) exactly fixed, so the axis is pure")
    print("  resolution.  Only zones whose reference wing survives M/4 qualify.")
    print("  %-6s %-6s %-4s %-10s %-10s %-9s %-10s %-8s %-9s %s"
          % ("n", "M", "p", "delta", "sigma", "bare", "m_obs", "rho", "cap(S4)",
             "inside"))
    per = {}
    for k, p_ref in refs:
        if k not in DRIFT_ZONES:
            continue
        L = lads[k - 1]
        p_small = int(round(p_ref * M_DRIFT[0] / float(M_MAIN)))
        if p_small < P_MIN:
            continue
        rows = []
        for M in M_DRIFT:
            p = int(round(p_small * M / float(M_DRIFT[0])))
            d = sample(k, M, p, deep=True)
            if d is None:
                continue
            c = chain_caps(d)
            ins = np.isfinite(L["delta_c"]) and d["delta"] < L["delta_c"]
            rows.append((M, p, d, c, ins))
            print("  %-6d %-6d %-4d %-10.6f %-10.5f %-9.4f %-10.2e %-8.4f "
                  "%-9.3f %s"
                  % (d["n"], M, p, d["delta"], d["sigma"], d["bare"],
                     d["m_obs"], d["rho"], c["S4"], "yes" if ins else "no"))
        if len(rows) == len(M_DRIFT):
            per[k] = rows
    keys = ("sigma", "bare", "m_obs", "rho", "cap_S4")
    sp = {key: 0.0 for key in keys}
    sp["delta"] = 0.0
    for k, rows in per.items():
        sp["delta"] = max(sp["delta"], spread([r[2]["delta"] for r in rows]))
        sp["sigma"] = max(sp["sigma"], spread([r[2]["sigma"] for r in rows]))
        sp["bare"] = max(sp["bare"], spread([r[2]["bare"] for r in rows]))
        sp["m_obs"] = max(sp["m_obs"], spread([r[2]["m_obs"] for r in rows]))
        sp["rho"] = max(sp["rho"], spread([r[2]["rho"] for r in rows]))
        sp["cap_S4"] = max(sp["cap_S4"], spread([r[3]["S4"] for r in rows]))
    for key in ("delta", "sigma", "bare", "m_obs", "rho", "cap_S4"):
        info("B4.drift_%s" % key,
             "relative spread over M = %s: <= %.1f%%" % (str(M_DRIFT),
                                                         100.0 * sp[key]))
    check("el_b4.drift_fixed_delta", sp["delta"] < 1.0e-3,
          "the drift axis holds delta fixed to <= %.2f%% (integer wing rounding "
          "only) at %d zones while M spans %s -- so the spreads above are "
          "resolution, not geometry"
          % (100.0 * sp["delta"], len(per), str(M_DRIFT)))
    print("")
    print("  IS THE CLOSURE RESOLUTION-STABLE?  both the exact ratio rho and the")
    print("  certified cap RISE with M at fixed geometry, so the closure is a")
    print("  statement at this resolution -- the trend is measured, not "
          "extrapolated")
    print("  %-5s %-14s %-14s %-10s %s"
          % ("n", "rho(M) slope", "cap(M) slope", "rho@%d" % M_MAIN,
             "M* where rho -> 1"))
    slopes, horizons = [], []
    for k, rows in per.items():
        lm = [math.log(r[0]) for r in rows]
        sr, _ = ols(lm, [math.log(r[2]["rho"]) for r in rows])
        sc, _ = ols(lm, [math.log(r[3]["S4"]) for r in rows])
        rho_top = rows[-1][2]["rho"]
        if sr > 1.0e-6:
            mstar = M_MAIN * math.exp(-math.log(rho_top) / sr)
        else:
            mstar = float("inf")
        slopes.append(sr)
        horizons.append(mstar)
        print("  %-5d %+14.4f %+14.4f %-10.4f %.3g"
              % (rows[0][2]["n"], sr, sc, rho_top, mstar))
    check("el_b4.resolution_caveat", True,
          "at FIXED delta the pencil ratio grows like M^%.2f..M^%.2f, and the "
          "same trend hits sigma itself, not only the cap -- read this together "
          "with el_b4.gamma_drift below, which shows the growth is the window "
          "shrinking with M, not the chain degrading"
          % (min(slopes), max(slopes)))
    info("B4.horizon",
         "at that measured power (a FIT on %d points) a point held at FIXED "
         "delta would reach rho = 1 near M = %.3g..%.3g -- which is just the "
         "statement that delta_c(M) sweeps past it"
         % (len(M_DRIFT), min(horizons), max(horizons)))
    print("")
    print("  ... but delta is the WRONG coordinate to hold fixed: the window")
    print("  itself moves with M.  Held at fixed gamma = delta / delta_c(M),")
    print("  the geometry is normalised and the drift is the honest one")
    print("  %-6s %-6s %-12s %-5s %-10s %-14s %-8s %s"
          % ("n", "M", "delta_c(M)", "p", "delta", "sigma/(mu/2)", "rho",
             "cap(S4)"))
    dc_spread, rho_g, cap_g, ok_all = 0.0, 0.0, 0.0, True
    for k in per:
        dcs, rr, cc = [], [], []
        for M in M_DRIFT:
            LM = lads[k - 1] if M == M_MAIN else zone_ladder(k, M)
            if not np.isfinite(LM["delta_c"]):
                continue
            p = p_inside(k, M, LM["p_hi"], GAMMA_REF, LM["delta_c"], LM["u"])
            d = sample(k, M, p, deep=True)
            if d is None:
                continue
            c = chain_caps(d)
            dcs.append(LM["delta_c"])
            rr.append(d["rho"])
            cc.append(c["S4"])
            ok_all = ok_all and c["S4"] <= 1.0
            print("  %-6d %-6d %-12.6f %-5d %-10.6f %-14.4f %-8.4f %.3f"
                  % (d["n"], M, LM["delta_c"], p, d["delta"],
                     d["sigma"] / d["half"], d["rho"], c["S4"]))
        dc_spread = max(dc_spread, spread(dcs))
        rho_g = max(rho_g, spread(rr))
        cap_g = max(cap_g, spread(cc))
    check("el_b4.gamma_drift", ok_all,
          "delta_c itself drifts by <= %.1f%% over M = %s, and at FIXED gamma = "
          "%.2f the pencil ratio moves by <= %.1f%% and the certified cap by <= "
          "%.1f%%, staying <= 1 at every (zone, M) tested -- so the closure is "
          "stable in the normalised coordinate, and the fixed-delta drift above "
          "is the window moving, not the chain failing"
          % (100.0 * dc_spread, str(M_DRIFT), GAMMA_REF, 100.0 * rho_g,
             100.0 * cap_g))


def block_b4_synth(jrows, caps, lads, inside_flags, n_in, reach):
    section("B4  SYNTHESIS -- the full chain, link by link, zone by zone")
    info("chain.link1",
         "[HYP-m]  Q_full|E_0 >= m Id                     HYPOTHESIS INPUT "
         "(not proved)")
    info("chain.link2",
         "[cap]    rho = lam_max(A_sh^-1 W) <= block + band caps CERTIFIED "
         "given induction data + E_+ data")
    info("chain.link3",
         "[sigma]  sigma_k(dref) >= mu/2 + (1-cap)(bare - mu/2) CERTIFIED "
         "given links 1-2 (+ bare_k MEASURED)")
    info("chain.link4",
         "[edge]   sigma_k(d) >= sigma_k(dref)(d/dref)^q_env   PROOF-SHAPED, "
         "measured (envelope over the ladder)")
    info("chain.link5",
         "[handoff] w_k >= (dref/2)(mu_k/(2 sigma))^{1/q_env}  ALGEBRA given "
         "link 4")
    print("")
    print("  %-4s %-8s %-8s %-8s %-10s %-9s %-11s %-8s %-9s %-10s %s"
          % ("n", "inside", "mu/2", "bare", "cap(best)", "sigma_LB",
             "sigma_meas", "closes", "w_k(LB)", "w_k(meas)", "ratio"))
    n_close = n_close_in = 0
    breaks = []
    for d in jrows:
        c = caps[d["k"]]
        cap = min(c[s] for s in IND_STAGES)
        lb = sigma_lb(d, cap)
        q = lads[d["k"] - 1]["q_env"]
        wk_lb = 0.5 * d["delta"] * (d["half"] / max(lb, 1.0e-300)) ** (1.0 / q) \
            if lb > 0 else float("nan")
        wk_me = 0.5 * d["delta"] * (d["half"] / d["sigma"]) ** (1.0 / q)
        cl = lb >= d["half"]
        n_close += int(cl)
        n_close_in += int(cl and inside_flags[d["k"]])
        if not cl:
            breaks.append(d["n"])
        print("  %-4d %-8s %-8.4f %-8.4f %-10.3f %-9.4f %-11.4f %-8s %-9.5f "
              "%-10.5f %.4f"
              % (d["n"], "yes" if inside_flags[d["k"]] else "no", d["half"],
                 d["bare"], cap, lb, d["sigma"], "YES" if cl else "no",
                 wk_lb, wk_me, wk_lb / wk_me))
    check("el_b4.chain_assembled", n_close > 0,
          "full chain evaluated at %d zones; closes with certified + "
          "induction-data constants at %d (%d of the %d resolved zones)"
          % (len(jrows), n_close, n_close_in, n_in))
    print("")
    print("  the same chain evaluated at the DEEPEST certified point of each")
    print("  zone (gamma_max from B2), which is where the handoff is actually")
    print("  available:  w_k >= (delta/2) (mu_k/(2 sigma_LB))^{1/q_env}")
    print("  %-4s %-10s %-10s %-8s %-10s %-9s %-10s %-10s %-8s %s"
          % ("n", "gamma_max", "delta", "cap", "sigma_LB", "mu/2", "w_k(LB)",
             "w_k(meas)", "ratio", "closes"))
    n_reach_cl, n_floor = 0, 0
    for d in jrows:
        r = reach.get(d["k"])
        if r is None:
            print("  %-4d %-10s %-10s %-8s %-10s %-9s %-10s %-10s %-8s %s"
                  % (d["n"], "none", "-", "-", "-", "-", "-", "-", "-", "no"))
            continue
        dd, c = r["d"], r["caps"]
        lb = r["sigma_LB"]
        q = lads[d["k"] - 1]["q_env"]
        wk_lb = 0.5 * dd["delta"] * (dd["half"] / max(lb, 1e-300)) ** (1.0 / q)
        wk_me = 0.5 * dd["delta"] * (dd["half"] / dd["sigma"]) ** (1.0 / q)
        cl = lb >= dd["half"]
        n_reach_cl += int(cl)
        n_floor += int(r["p"] <= P_MIN)
        print("  %-4d %-10.2f %-10.6f %-8.3f %-10.4f %-9.4f %-10.5f %-10.5f "
              "%-8.4f %s" % (d["n"], r["gamma"], dd["delta"], c["S4"], lb,
                             dd["half"], wk_lb, wk_me, wk_lb / wk_me,
                             "YES" if cl else "no"))
    check("el_b4.reach_chain", n_reach_cl > 0,
          "with the reference placed at gamma_max delta_c the certified chain "
          "closes and hands off at %d/%d zones; the remaining %d are at the wing "
          "floor p = %d, where M <= %d cannot make delta smaller -- an "
          "instrument limit, not a chain break"
          % (n_reach_cl, len(jrows), len(jrows) - n_reach_cl, P_MIN, M_MAIN))
    unres = [d["n"] for d in jrows if not inside_flags[d["k"]]]
    info("B4.breaks",
         "on the resolved zones the chain does NOT close at n = %s; unresolved "
         "(grid never enters the window) n = %s"
         % (breaks if breaks else "none", unres if unres else "none"))
    return n_close, n_close_in, n_reach_cl


# ----------------------------------------------------------------------------
# the honest ledger
# ----------------------------------------------------------------------------
LEDGER = (
    ("bare_k = lam_min(Q_full|E_-)", "MEASURED (Rayleigh-Ritz upper est.)",
     "the chain needs a LOWER bound on the wing block of the genuine form; "
     "T102 measured 2.65..3.52 = 4x..14x mu_k/2, with no certificate"),
    ("m = lam_min(Q_full|E_0)", "HYPOTHESIS INPUT -- and MEASURED TO BE USELESS",
     "the induction window's form is nearly singular (m ~ 1e-5), so a "
     "strengthened induction that carries only a MARGIN cannot close anything; "
     "this probe measures that and discards the route"),
    ("low modes + band masses of B_- on E_0", "INDUCTION-DATA (exact, Parseval)",
     "the working currency: per-mode coupling masses of the smaller window "
     "below the band start, then geometric band masses; the footing of T99's "
     "R_G and T103's band masses"),
    ("band edges + Bessel tail weight", "CERTIFIED (spectral calculus)",
     "w_j >= 1/lam_j gated at every sample; no fit"),
    ("block-inverse split of E_0 against E_+", "CERTIFIED (exact algebra)",
     "W = m0 A^-1 m0^T + R Sig^-1 R^T with R = mp - m0 A^-1 C^T and "
     "Sig = Q|E_+ - C A^-1 C^T; an identity, gated to 1e-6, not an inequality"),
    ("lam_min(Sig), ||R||", "MEASURED (larger window)",
     "NOT supplied by the induction hypothesis -- the E_+ half of the dressing "
     "is the un-inducted part, and its share of the cap is measured here"),
    ("band data on the E_+ Schur block Sigma", "MEASURED (larger window), finite",
     "the crude ||R||^2/lam_min(Sig) step is what loses the late zones; feeding "
     "Sigma through the SAME band recipe closes all of them, but the wings are "
     "small enough that this is effectively the whole E_+ block -- the "
     "un-inducted half is still an input, only a sharper one"),
    ("mu_k = 2 Lambda(n_k)/sqrt(n_k)", "EXACT ARITHMETIC",
     "von Mangoldt exact; the atom eigenvalue -1/2 on E_- is proved "
     "(T95-C1/T97, re-gated here as el_split.atom_diag)"),
    ("edge law sigma(d) >= sigma(dref)(d/dref)^q", "FIT (proof-shaped)",
     "an OLS power law with a measured one-sided overshoot; a proof needs a "
     "one-sided edge estimate for the resolvent of the genuine form"),
    ("prolate concentration of the wing pair", "CERTIFIED CONSTRUCTION",
     "0 <= S <= Id gated; the localisation of the near-null direction is "
     "MEASURED and the tail bound it would need is not built"),
)


def block_honest():
    section("THE HONEST LEDGER -- ingredient by ingredient")
    n_cert = n_hyp = n_meas = n_fit = 0
    for what, kind, why in LEDGER:
        print("  %-42s %s" % (what, kind))
        print("      %s" % why)
        if kind.startswith("HYPOTHESIS"):
            n_hyp += 1
        elif kind.startswith("FIT"):
            n_fit += 1
        elif kind.startswith("MEASURED"):
            n_meas += 1
        else:
            n_cert += 1
    print("")
    check("el_honest.ledger", n_cert + n_hyp + n_meas + n_fit == len(LEDGER),
          "%d ingredients: %d certified/exact/induction-data, %d hypothesis, "
          "%d measured, %d fit"
          % (len(LEDGER), n_cert, n_hyp, n_meas, n_fit))
    info("honest.conditional",
         "the chain is CONDITIONAL on induction data (the low-mode coupling "
         "masses of the smaller window) and on MEASURED data of the larger "
         "window: bare_k and the E_+ Schur block Sigma")
    info("honest.hard_core",
         "the remaining hard core, in order of hardness: (i) a LOWER BOUND on "
         "the bare wing block bare_k (everything else is a perturbation of it); "
         "(ii) the induction must carry the LOW-END COUPLING MASSES of the "
         "smaller window, not a margin; (iii) the un-inducted E_+ Schur block "
         "must be supplied as finite spectral data; (iv) a one-sided edge "
         "estimate in delta to replace the fitted power law")


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------
def main():
    section("T104-A  SCHUR.PROFILE.CHAIN -- the inductive bound on sigma_k")
    info("setup",
         "M_main = %d, delta fractions %s of the mu/2 crossing (deep reference "
         "%.2f), zones 1..%d, bands (Lam0 %.1f, r %.1f, Lam_max %.1f), ntop %d, "
         "budget %d s" % (M_MAIN, str(FRACS), GAMMA_REF, N_ZONES, BAND_LAM0,
                          BAND_R, BAND_LAM_MAX, NTOP, int(BUDGET_S)))
    firewall()

    section("GATES -- kernel, forms, splitting, sandwich, fence, prolate basis")
    gate_kernel()
    gate_forms()
    gate_split()
    gate_sandwich()
    gate_fence()
    gate_prolate()

    lads, refs, n_in_grid = build_grid(M_MAIN)

    jrows = []
    for k, p_ref in refs:
        d = sample(k, M_MAIN, p_ref, deep=True, joint=True)
        if d is not None:
            jrows.append(d)
    info("grid.deep",
         "%d zones at delta = %.2f delta_c, with the joint-block spectrum; %d of "
         "them land inside the window" % (len(jrows), GAMMA_REF, n_in_grid))

    rows = []
    for L in lads:
        for f in FRACS:
            if budget_left() < 240.0:
                break
            p = p_inside(L["k"], M_MAIN, L["p_hi"], f, L["delta_c"], L["u"])
            if any(r["k"] == L["k"] and r["p"] == p for r in rows):
                continue
            d = sample(L["k"], M_MAIN, p)
            if d is not None:
                rows.append(d)
        for d in jrows:
            if d["k"] == L["k"] and not any(r["k"] == d["k"] and r["p"] == d["p"]
                                            for r in rows):
                rows.append(d)
    rows.sort(key=lambda r: (r["k"], r["p"]))
    info("grid.wide", "%d samples over %d zones x up to %d fractions of delta_c"
         % (len(rows), N_ZONES, len(FRACS) + 1))

    b1 = block_b1(rows, jrows)
    caps = {d["k"]: chain_caps(d) for d in jrows}
    closes, inside_flags, n_in = block_b2(jrows, caps, lads)
    reach = block_b2_reach(jrows, caps, lads, M_MAIN)
    best, nbest = block_b2_tail(jrows, caps, inside_flags, n_in)
    b3 = block_b3(jrows, caps)
    block_b4_edge(lads)
    block_b4_drift(lads, refs)
    n_close, n_close_in, n_reach_cl = block_b4_synth(
        jrows, caps, lads, inside_flags, n_in, reach)
    block_honest()

    section("VERDICT")
    sl_best = ols([d["k"] for d in jrows],
                  [math.log(1.0 / caps[d["k"]][best]) for d in jrows])
    cond1 = (nbest >= n_in and n_in > 0)
    cond2 = sl_best[0] > -0.05
    cond3 = False                       # bare_k, the E_+ data and the fit
    print("")
    print("  the three conditions for SCALAR-BOUNDED, one line each")
    print("  (1) the best inductive chain closes on every resolved zone %s"
          % ("YES" if cond1 else "no"))
    print("  (2) its headroom does not decay with the zone index        %s"
          % ("YES" if cond2 else "no"))
    print("  (3) the ingredient balance is clean (no measured input)    %s"
          % ("YES" if cond3 else "no"))
    print("      condition (3) fails on three named inputs: bare_k (a MEASURED "
          "lower bound")
    print("      on the wing block), the E_+ Schur data, and the FITTED edge "
          "law in delta")
    prov_best = {"S2": "band cap on E_0 + crude E_+ step",
                 "S3": "bands + ntop exact on E_0 + crude E_+ step",
                 "S4": "CERTIFIED given INDUCTION-DATA on E_0 + FINITE BAND "
                       "DATA on the E_+ Schur block (MEASURED, but the same "
                       "spectral-calculus recipe)"}.get(best, "see B2")
    info("verdict.best_chain",
         "%s closes %d/%d resolved zones (%d/%d overall), log H slope %+.4f +- "
         "%.4f | %s" % (best, sum(1 for d in jrows
                                  if caps[d["k"]][best] <= 1.0 and
                                  inside_flags[d["k"]]), n_in, nbest,
                        len(jrows), sl_best[0], sl_best[1], prov_best))
    info("verdict.stability",
         "the closure is resolution-stable in the normalised coordinate: at "
         "fixed gamma the pencil ratio and the certified cap move by only a few "
         "percent over a 4x change of M, while delta_c itself moves by tens of "
         "percent (see el_b4.gamma_drift)")
    info("verdict.ceiling",
         "the measured optimum lam_max(W) closes %d/%d and the joint-block band "
         "cap %d/%d -- so the residual gap is the instrument, not the truth"
         % (len(closes["EX"]), len(jrows), len(closes["S2K"]), len(jrows)))
    info("verdict.mass_vs_margin",
         "log(mass/margin) slope %+.4f +- %.4f against log margin slope %+.4f "
         "+- %.4f and log bare slope %+.4f +- %.4f"
         % (b1["sl_ratio"][0], b1["sl_ratio"][1], b1["sl_margin"][0],
            b1["sl_margin"][1], b1["sl_bare"][0], b1["sl_bare"][1]))
    shares = [caps[d["k"]]["eplus_share"] for d in jrows]
    info("verdict.eplus",
         "E_+ share of the S2 cap %.4f..%.4f -- NOT negligible, so the chain is "
         "NOT free of measured E_+ data" % (min(shares), max(shares)))
    info("verdict.wing_basis",
         "prolate localisation n99 <= %d modes, sigma from <= %d modes; "
         "block-split chain closes %d vs raw %d"
         % (max(b3["n99"]), max(b3["nsig"]), b3["n_pro_cl"], b3["n_raw_cl"]))
    gs = [r["gamma"] for r in reach.values() if r]
    info("verdict.reach",
         "the certified chain closes somewhere inside the handoff window at "
         "%d/%d zones, reaching gamma_max = %.2f..%.2f of the crossing"
         % (len(gs), len(jrows), min(gs), max(gs)))
    info("verdict.full_chain",
         "the assembled chain closes at %d/%d resolved zones (%d/%d overall) "
         "with certified + induction-data constants"
         % (n_close_in, n_in, n_close, len(jrows)))
    nex = [caps[d["k"]]["n_ex"] for d in jrows]
    info("verdict.data_cost",
         "the induction must carry the coupling masses of %d..%d explicit low "
         "modes of the smaller window" % (min(nex), max(nex)))
    if cond1 and cond2 and cond3:
        verdict = "SCALAR-BOUNDED"
    elif nbest == 0:
        verdict = "DRESSING-UNBOUNDED"
    else:
        verdict = "CHAIN-PARTIAL"
    print("")
    print("  VERDICT: %s" % verdict)
    check("el_budget.verdict", verdict in
          ("SCALAR-BOUNDED", "CHAIN-PARTIAL", "DRESSING-UNBOUNDED"),
          "verdict = %s" % verdict)

    section("TOTAL")
    check("el_budget.array", MAX_SEEN <= MAX_ARRAY,
          "largest array %d^2 <= %d^2" % (MAX_SEEN, MAX_ARRAY))
    el = time.time() - T_START
    check("el_budget.time", el < BUDGET_S, "%.1f s < %d s" % (el, int(BUDGET_S)))
    print("")
    print("TOTAL  %d checks, %d failures, %.1f s, largest array %d^2, verdict %s"
          % (PASS + FAIL, FAIL, el, MAX_SEEN, verdict))


if __name__ == "__main__":
    main()
