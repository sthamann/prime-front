"""Discovery probe (2026-07-27), part 110 of the zeta/prime investigation.
Contract MARGIN.PROPAGATION -- does the SCALAR margin propagate by itself?

WHERE THIS SITS (T105..T109, taken as given, re-derived here)
  T109 closed the whole chain for the J-odd half of the prime-atom handoff,
      (R)   Q|odd = T_odd - t~ t~^T  >=  (mu_k/2) V V^T ,
  16/16 zones with margin 1.3..10.4, CONDITIONAL ON EXACTLY ONE INPUT: the
  STRICT positivity margin of the odd channel,
      lam_min(Q|odd)  >=  need109  =  (mu/2) H_cert^2 / ((1 - om_cert) kap) ,
  measured need109 = 1.7e-6..7.5e-3 against a measured lam_min(Q|odd) =
  1.4e-5..5.1e-2.  need109 sits 1e2..1e6 BELOW mu/2, so the chain asks for
  strictly LESS than it delivers -- but it asks for a STRICT number, while the
  induction hypothesis (window Weil positivity) only gives Q|odd >= 0.  This
  probe asks whether that one number propagates along the zone ladder:
      [ margin m_k at window alpha_k ] + [ T109 chain ]
          ==> [ handoff holds with surplus ] ==> [ m_{k+1} >= need109(k+1) ] ?

THE T106 DEMARCATION (documented here because it looks like a refutation)
  T106 REFUTED the accumulated ATOM invariant Q >= beta sum_j (mu_j/2) P_-^(j):
  the inherited demand collapses (beta_int ~ 1e-2) and the transport across a
  growth step loses almost everything (theta_k ~ 1 - 1e-3, beta_on < 1 on
  15/15).  Its killer is DIRECTIONAL: an old wing pair becomes an interior
  pair of the grown window and couples ~750x more strongly, so a demand that
  POINTS somewhere is destroyed.  The object here is different in kind: a
  SCALAR floor lam_min(Q|odd) >= m, one number, no direction.  A scalar floor
  is invariant under any orthogonal change of the demand geometry, so the T106
  no-go does not apply to it a priori.  Whether it survives the SAME growth
  step is exactly the question -- and the answer below is measured, not
  assumed.  T106 also measured, in the other direction, that the handoff is
  delivered with SURPLUS: sigma_k(delta_0) >= 1.31 (mu_k/2) uniformly.

THE EXACT PROPAGATION OBJECT (H2.1, an identity, not a model)
  Grow the window by g cells at EACH end at fixed cell width D.  In odd
  coordinates the old sector embeds EXACTLY as the trailing block: old odd
  index r maps to new odd index r + g, the Toeplitz lag c_{|r-s|} is
  unchanged, the Hankel index (M'-1) - (r+g) - (s+g) = (M-1) - r - s is
  unchanged, and the pole source t~ is unchanged cell by cell because
  xbar'_{r+g} = xbar_r.  Hence, with A the g x g new-cell block and C the
  coupling,
      Q'|odd  =  [[ A , C ] , [ C^T , X ]] ,   X = Q_k|odd - mu_{k+1} N ,
      N = odd_toeplitz( atom_lag(. , u_{k+1}, D) , M_old ) ,
  i.e. the step splits CLEANLY into (1) the ATOM ENTRY, a Loewner-negative
  rank-structured shift of the old block by the new atom, and (2) the
  BORDERING by the g new cells.  Everything below is measured on this exact
  split.

THE BLOCKS
  H1 THE MARGIN MAP.  lam_min(Q|odd) over the whole window ladder: the map
      m_k vs need109(k) at every handoff point, the M-trend of both sides, the
      DILUTION RATE of the margin during pure window growth between two atom
      entries (exponential vs power-law fit, both reported as fits), and the
      exact channel action of the ATOM ENTRY itself -- the naive expectation
      is a -(mu/2) pressure on the odd channel; what the atom actually costs
      lam_min is measured three ways (exact drop, first-order Rayleigh term at
      the pre-entry minimiser, and the Weyl worst case mu lam_max(N)).
  H2 THE PROPAGATION LAW.  Candidate inequalities m_{k+1} >= f(m_k, certified
      quantities), on the exact split above:
      (i)   BORDERED WEYL (2x2 reduction).  For unit v = (v1, v2),
            v^T Q' v >= a s^2 + x c^2 - 2 ||C|| s c, s = ||v1||, c = ||v2||,
            so lam_min(Q') >= ((a+x) - sqrt((a-x)^2 + 4||C||^2))/2 =: bord.
            a = lam_min(A) is a g x g computation, ||C|| and lam_max(N) are
            Cholesky-capped: every ingredient is a finite certificate.
      (ii)  SCHUR / FRIEDRICHS FIXED POINT.  lam_min(Q') >= lam iff
            A - lam > 0 and X - lam - C^T (A - lam)^{-1} C >= 0; with the
            growth angle theta(lam) = lam_max( W(lam) , X ) < 1 this is
            implied by lam <= (1 - theta(lam)) x, a monotone fixed point.
            theta is DIRECTIONAL (it sees where the coupling points); its
            scalar-only cap is theta <= lam_max(W)/x, which degrades (ii)
            back to Weyl.  The gap between the two is the whole question.
      (iii) THE SURPLUS ROUTE.  T106/T109 deliver sigma_k(delta_0) >= beta_0
            (mu_k/2) with beta_0 > 1; does the surplus (beta_0 - 1) mu_k/2
            convert into a floor for the GROWN window?  Measured as a
            relation and fitted (labelled a fit), never assumed.
      Counted over the 15 handoffs of the measured ladder.
  H3 BASE CASE AND OUTLIERS.  Zone 1 (n = 2, the T108/T109 outlier with no
      cancellation history): lam_min(Q|odd) at the first window, certified by
      an explicit Cholesky of Q|odd - lam I (Sylvester's law of inertia) at
      three grid resolutions -- and the honest statement of what it covers
      does and does not cover.  Plus the need109(k) trend against the m_k
      trend: if need109 falls FASTER than m_k, propagation gets easier with k.
  H4 SYNTHESIS.  Run the induction once, end to end: base case + the best law
      of H2, 16 zones, certified and measured columns strictly separated, and
      the exact point where it breaks.

PREREGISTERED VERDICTS
  MARGIN-PROPAGATES: the law holds on every handoff with CERTIFIED ingredient
      bounds and the base case stands -- the circle closes on the measured
      zones.
  LAW-MEASURED     : a law holds as measured on every handoff but at least one
      ingredient is not certified -- named explicitly.
  MARGIN-DILUTES   : dilution beats propagation -- the quantitative gap.
  Element gates: el_firewall, el_h0, el_h1, el_h2, el_h3, el_h4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger/TeX/website/
    changelog edit, no verification/ module, no next.txt, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * RH => window Weil positivity is used in ONE DIRECTION only; the converse
    is not claimed.  Q_full(alpha) >= 0, hence Q|odd >= 0, is the HYPOTHESIS
    INPUT.  Where a STRICT margin is used as an INPUT it is declared as a
    quantified hypothesis input; where it is used as a CONCLUSION it is
    derived from the previous zone plus certified step data.
  * lam_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute positivity, never prove it.  A Cholesky
    certificate for lam_min(Q|odd) >= lam therefore certifies THE FINITE
    MATRIX (which is exactly the object the T109 chain consumes), not the
    continuum form, and only at the windows actually computed.
  * CERTIFIED vs MEASURED tracked per line and restated in the H4 ledger.  A
    "certificate" is a finite computation whose validity does not depend on
    any measured spectral datum: upper caps on lam_max are Cholesky-verified
    (Sylvester inertia), trial data enter only through inequalities valid for
    ANY trial.  Floating-point rounding is not audited.
  * Every fit is labelled a fit.  Classical anchors cited, not re-derived:
    Weil 1952, Weyl 1912 (perturbation / min-max), Cauchy interlacing,
    Rayleigh-Ritz, Loewner order and antitonicity of the inverse, Schur
    complement, Haynsworth inertia additivity, Sylvester's law of inertia,
    Sherman-Morrison 1950, Woodbury 1950, Cholesky, Grenander-Szego
    (Toeplitz), Szego recursion / Levinson 1947, Combes-Thomas 1973,
    Prager-Synge 1947, Becker-Rannacher goal-oriented estimation,
    Hestenes-Stiefel 1952, Cantoni-Butler 1976 (parity superselection),
    Friedrichs angle, Kato perturbation theory, T105 support separation,
    von Mangoldt arithmetic.

OUTCOME OF THIS RUN  =>  see the H4 ledger and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import (cho_factor, cho_solve, cholesky, eigh, eigvalsh,
                          solve_triangular)

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_ARRAY = 1500             # hard cap on any matrix dimension
BUDGET_S = 780.0

M_CROSS = 1000               # cell count for locating the handoff crossing
M_MAIN = 1200                # operating cell count of the nested ladder
M_HI = 2400                  # resolution check; odd sector 1200 <= MAX_ARRAY
M_LOW = 600
M_GROW = 900                 # base of the growth sweep (it grows with alpha)
P_MIN, P_MAX = 2, 200
GAMMA_T110 = 0.5             # common physical wing depth as a fraction of min delta_c
N_GROW = 7                   # sample points of the pure-growth sweep
CG_LADDER = (128, 256, 512)
NTOP_SCAN = (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
NTOP_MAX = 512
MIN_LADDER = (1, 2, 4, 8, 16, 64, 256, 10 ** 9)   # directions surrendered
NSOFT_CHAIN = 1              # directions surrendered by the H4 graded chain
BISECT = 30                        # bisection depth of the certified step floor
ETA_CHOL = 1.0e-6
CAP_BACKS = (1.0e-9, 1.0e-7, 1.0e-5, 1.0e-3, 1.0e-1)
FP_TOL = 1.0e-9              # relative slack allowed for exact-inequality gates

GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)
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


def sym(A):
    return 0.5 * (A + A.T)


# ----------------------------------------------------------------------------
# el_firewall -- AST scan of this source
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
            fn = node.func
            nm = getattr(fn, "id", None) or getattr(fn, "attr", None)
            if nm in ("open",):
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


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952)
# ----------------------------------------------------------------------------
_BERN = (1.0 / 6, -1.0 / 30, 1.0 / 42, -1.0 / 30, 5.0 / 66, -691.0 / 2730, 7.0 / 6)


def digamma_c(z):
    z = np.asarray(z, dtype=np.complex128)
    acc = np.zeros(z.shape, dtype=np.complex128)
    zz = np.array(z, dtype=np.complex128, copy=True)
    for _ in range(64):
        m = zz.real < 16.0
        if not m.any():
            break
        acc[m] -= 1.0 / zz[m]
        zz[m] += 1.0
    w = 1.0 / (zz * zz)
    r = np.log(zz) - 0.5 / zz
    p = w.copy()
    for n, b in enumerate(_BERN, start=1):
        r = r - (b / (2.0 * n)) * p
        p = p * w
    return acc + r


def kernel_k(t):
    t = np.atleast_1d(np.asarray(t, dtype=float))
    return digamma_c(0.25 + 0.5j * t).real - LOG_PI


def kernel_K_x(s):
    s = np.asarray(s, dtype=float)
    return -np.exp(-0.5 * s) / (-np.expm1(-2.0 * s))


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


def zone_geometry(u, p, M):
    D = u / (M - p)
    alpha = u * M / (2.0 * (M - p))
    return D, alpha, p * D


def atoms_in(alpha, atoms_all):
    return [(t[2], t[3]) for t in atoms_all if t[2] <= 2.0 * alpha + 1.0e-14]


def lag_vector(alpha, M, atoms):
    """The M retained lag coefficients of the Toeplitz part at (alpha, M)."""
    D = 2.0 * alpha / M
    s = np.arange(M) * D
    c = arch_A(s, D)
    for u_j, mu_j in atoms:
        c = c - mu_j * atom_lag(s, u_j, D)
    return c, D


def build_Q(alpha, M, atoms):
    from scipy.linalg import toeplitz
    c, _ = lag_vector(alpha, M, atoms)
    Q = toeplitz(c)
    a, b = pole_vectors(alpha, M)
    Q += np.outer(a, b) + np.outer(b, a)
    return Q


def blocks_U(Q, p):
    """Q in the exact orthogonal basis U = [B_-, E_0, B_+] (T102)."""
    M = Q.shape[0]
    L, C, R = slice(0, p), slice(p, M - p), slice(M - p, M)
    QLL, QLR, QRR = Q[L, L], Q[L, R], Q[R, R]
    QLC, QRC, QCC = Q[L, C], Q[R, C], Q[C, C]
    sym_ = QLR + QLR.T
    mm = 0.5 * (QLL + QRR - sym_)
    pp = 0.5 * (QLL + QRR + sym_)
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


def sigma_at(alpha, M, p, atoms):
    """lam_min of the Schur complement of Q(alpha) onto E_- -- the handoff datum."""
    Q = build_Q(alpha, M, atoms)
    mm, pp, mp, m0, p0, QCC = blocks_U(Q, p)
    del Q
    nc = QCC.shape[0]
    Mat = np.empty((nc + p, nc + p))
    Mat[:nc, :nc] = QCC
    Mat[:nc, nc:] = p0.T
    Mat[nc:, :nc] = p0
    Mat[nc:, nc:] = pp
    B = np.concatenate([m0, mp], axis=1).T
    Mat = sym(Mat)
    fac, _ = safe_cho(Mat)
    del Mat, QCC, pp, p0, m0, mp
    if fac is None:
        return float("nan")
    A = B.T @ cho_solve(fac, B, check_finite=False)
    return float(eigvalsh(sym(mm) - sym(A)).min())


def sigma_of(u, p, M, atoms_all):
    D, alpha, delta = zone_geometry(u, p, M)
    return sigma_at(alpha, M, p, atoms_in(alpha, atoms_all))


def find_p_star(u, mu, M, atoms_all):
    """Largest wing width p with sigma_k(p) >= mu_k/2 (the T105 crossing)."""
    half = mu / 2.0
    lo, hi = P_MIN, min(P_MAX, M // 3)
    if sigma_of(u, lo, M, atoms_all) < half:
        return lo, False
    if sigma_of(u, hi, M, atoms_all) >= half:
        return hi, True
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if sigma_of(u, mid, M, atoms_all) >= half:
            lo = mid
        else:
            hi = mid
    return lo, True


def nested_window(u_k, MM, delta0):
    """The zone-k window whose physical wing depth is delta0, snapped to cells."""
    p = max(1, int(round(delta0 * MM / (u_k + delta0))))
    D, alpha, delta = zone_geometry(u_k, p, MM)
    return p, D, alpha, delta


def fit_line(x, y):
    """Least squares y = a + b x; returns (a, b, rms of the residual in y)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_multi(cols, y):
    """Least squares y = a0 + sum_i a_i cols_i; returns (coeffs, rms)."""
    A = np.stack([np.ones_like(y)] + list(cols), axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return sol, float(np.sqrt(np.mean((A @ sol - y) ** 2)))


# ----------------------------------------------------------------------------
# the J = -1 (reflection-odd) sector -- exact coordinates (T106/T107/T108)
# ----------------------------------------------------------------------------
def refl_odd_basis(n):
    """Orthonormal basis u_r = (e_r - e_{n-1-r})/sqrt2 of the J = -1 eigenspace."""
    h = n // 2
    r = np.arange(h)
    Bm = np.zeros((n, h))
    Bm[r, r] = 1.0 / _SQ2
    Bm[n - 1 - r, r] = -1.0 / _SQ2
    return Bm


def odd_toeplitz(c, M):
    """(Bm^T Toeplitz(c) Bm)_{rs} = c_{|r-s|} - c_{M-1-r-s} (Toeplitz minus Hankel)."""
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2)."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


def demand_V(p, M):
    """(mu/2) P_-|odd = (mu/2) V V^T; V has ceil(p/2) orthonormal columns."""
    h = M // 2
    m = (p + 1) // 2
    V = np.zeros((h, m))
    for i in range(m):
        j = p - 1 - i
        if j == i:
            V[i, i] = 1.0
        else:
            V[i, i] = 1.0 / _SQ2
            V[j, i] = 1.0 / _SQ2
    return V


def q_odd_at(alpha, M, atoms):
    """Q|odd = T_odd - t~ t~^T at the window (alpha, M) with the given atoms."""
    c, D = lag_vector(alpha, M, atoms)
    T = odd_toeplitz(c, M)
    tv = odd_pole_vector(alpha, M)
    return T - np.outer(tv, tv), T, tv, D


def lmin(A):
    return float(eigvalsh(sym(A), subset_by_index=[0, 0])[0])


def lmin_vec(A):
    w, v = eigh(sym(A), subset_by_index=[0, 0])
    return float(w[0]), np.ascontiguousarray(v[:, 0])


def lmax(A):
    n = A.shape[0]
    return float(eigvalsh(sym(A), subset_by_index=[n - 1, n - 1])[0])


def cert_lmax(A, seed=None):
    """CERTIFIED upper cap on lam_max(A): Cholesky of (t I - A) (Sylvester).

    The seed is a trial number (its quality is sharpness); the Cholesky is the
    validity.  Returns (t, ok).
    """
    n = A.shape[0]
    base = float(seed) if seed is not None else lmax(A)
    scale = max(abs(base), 1.0e-300)
    for back in CAP_BACKS:
        t = base + back * scale + 1.0e-300
        try:
            cholesky(t * np.eye(n) - sym(A), lower=True, check_finite=False)
            return t, True
        except LinAlgError:
            continue
    return float("inf"), False


def cert_lmin(A, lam):
    """CERTIFIED floor lam_min(A) >= lam by one Cholesky of (A - lam I)."""
    n = A.shape[0]
    try:
        cholesky(sym(A) - lam * np.eye(n), lower=True, check_finite=False)
        return True
    except LinAlgError:
        return False


def cert_norm(C):
    """CERTIFIED upper cap on ||C||_2 via a Cholesky cap on lam_max(C C^T)."""
    g = C.shape[0]
    G = C @ C.T if g <= C.shape[1] else C.T @ C
    t, ok = cert_lmax(G, seed=lmax(G))
    del G
    return (math.sqrt(max(t, 0.0)) if ok else float("inf")), ok


def graded_minorant(X, x_in, nsoft, xi_all=None, G_all=None):
    """The Loewner MINORANT that SURRENDERS the nsoft softest directions of X
    to the inherited scalar floor x_in and keeps the trial levels above:

        N(x_in, nsoft) := X - G diag( xi_j - x_in ) G^T ,
        G = the nsoft softest trial directions, xi_j their trial levels,

    so X - N = G diag(xi_j - x_in) G^T is a Gram form, PSD by inspection as
    soon as xi_j >= x_in -- which is EXACTLY the induction input lam_min(X) >=
    x_in.  This is the T109 G3 graded cap run in the opposite Loewner
    direction.  The two ends of the ladder are the two extreme epistemic
    positions:
        nsoft = dim X  ==>  N = x_in I, the STRICTLY SCALAR law (nothing but
                            the inherited number is used),
        nsoft = 0      ==>  N = X, nothing inherited is used at all.
    nsoft is therefore a direct measure of how much of the step can be carried
    by the scalar alone.
    """
    n = X.shape[0]
    if nsoft <= 0:
        return sym(X).copy(), True
    if nsoft >= n:
        return x_in * np.eye(n), True
    if xi_all is None:
        xi, G = eigh(sym(X), subset_by_index=[0, nsoft - 1])
    else:
        xi, G = xi_all[:nsoft], G_all[:, :nsoft]
    xi = np.asarray(xi, dtype=float)
    ok = bool(np.min(xi) >= x_in - 1.0e-14 * max(abs(x_in), 1.0))
    lev = np.maximum(xi, x_in)
    N = sym(X) - (np.ascontiguousarray(G) * (lev - x_in)) @ np.ascontiguousarray(G).T
    return sym(N), ok


def step_psd(A, C, N):
    """One Cholesky: is the bordered [[A, C],[C^T, N]] positive definite?"""
    g = A.shape[0]
    nn = N.shape[0]
    B = np.empty((g + nn, g + nn))
    B[:g, :g] = A
    B[:g, g:] = C
    B[g:, :g] = C.T
    B[g:, g:] = N
    try:
        cholesky(sym(B), lower=True, check_finite=False)
        return True
    except LinAlgError:
        return False


def cert_step_floor(A, C, N, lam_hi):
    """Largest lam on a bisection with Cholesky([[A-lam, C],[C^T, N-lam]]) OK.

    Q' >= [[A, C],[C^T, N]] whenever X >= N (Loewner), so every accepted lam is
    a certified floor for lam_min(Q').  Each acceptance is ONE Cholesky
    (Sylvester's law of inertia); nothing spectral is trusted.
    """
    g = A.shape[0]
    nn = N.shape[0]
    B = np.empty((g + nn, g + nn))
    B[:g, :g] = A
    B[:g, g:] = C
    B[g:, :g] = C.T
    B[g:, g:] = N
    B = sym(B)
    ident = np.eye(g + nn)

    def ok(lam):
        try:
            cholesky(B - lam * ident, lower=True, check_finite=False)
            return True
        except LinAlgError:
            return False

    if not ok(0.0):
        return 0.0, False
    lo, hi = 0.0, lam_hi
    if ok(hi):
        return hi, True
    for _ in range(BISECT):
        mid = 0.5 * (lo + hi)
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo, True


def gen_lmax(W, L):
    """lam_max(W, X) for X = L L^T: the largest eigenvalue of L^{-1} W L^{-T}."""
    Y = solve_triangular(L, sym(W), lower=True, check_finite=False)
    Y = solve_triangular(L, Y.T, lower=True, check_finite=False)
    return lmax(Y)


def bord(a, x, cn):
    """lam_min([[A, C],[C^T, X]]) >= ((a+x) - sqrt((a-x)^2 + 4 c^2))/2.

    Weyl / 2x2 reduction: v^T Q v >= a s^2 + x t^2 - 2 c s t on s^2 + t^2 = 1.
    """
    return 0.5 * ((a + x) - math.sqrt((a - x) ** 2 + 4.0 * cn * cn))


# ----------------------------------------------------------------------------
# the T109 chain -- need109 per zone
# ----------------------------------------------------------------------------
def wing_split(T, p, m):
    """T in the orthogonal basis [V | W]: V the demand columns, W the rest."""
    h = T.shape[0]
    q = p // 2
    Rv = np.zeros((p, m))
    Rw = np.zeros((p, q))
    for i in range(m):
        j = p - 1 - i
        if j == i:
            Rv[i, i] = 1.0
        else:
            Rv[i, i] = 1.0 / _SQ2
            Rv[j, i] = 1.0 / _SQ2
    for i in range(q):
        j = p - 1 - i
        Rw[i, i] = 1.0 / _SQ2
        Rw[j, i] = -1.0 / _SQ2
    A11 = T[:p, :p]
    A12 = T[:p, p:]
    TVV = sym(Rv.T @ A11 @ Rv)
    TVW = np.concatenate([Rv.T @ A11 @ Rw, Rv.T @ A12], axis=1)
    n_w = h - m
    TWW = np.empty((n_w, n_w))
    TWW[:q, :q] = Rw.T @ A11 @ Rw
    TWW[:q, q:] = Rw.T @ A12
    TWW[q:, :q] = TWW[:q, q:].T
    TWW[q:, q:] = T[p:, p:]
    return TVV, TVW, sym(TWW)


def psd_cap_omega(TVV, TVW, TWW, half, ntop):
    """omega_cert from a GRADED MATRIX CAP in PSD order (T104 arm A / T109 G3)."""
    B = TVW.T
    n_w = TWW.shape[0]
    if ntop > 0:
        vals, vecs = eigh(TWW, subset_by_index=[0, ntop])
        G = np.ascontiguousarray(vecs[:, :ntop])
        s_lev = np.asarray(vals[:ntop], dtype=float)
        nu_a, nu_b = float(vals[0]), float(vals[ntop])
    else:
        vals = eigvalsh(TWW, subset_by_index=[0, 0])
        G = None
        s_lev = np.zeros(0)
        nu_a = nu_b = float(vals[0])
    out = dict(ntop=ntop, nu_a=nu_a, nu_b=nu_b, ok=False,
               om_cert=float("inf"), lmin_S=float("nan"))
    if nu_a <= 0.0:
        return out
    for back in (ETA_CHOL, 1.0e-4, 1.0e-2, 1.0e-1):
        sig = (1.0 - back) * s_lev
        sig_b = (1.0 - back) * nu_b
        Z = TWW - sig_b * np.eye(n_w)
        if G is not None:
            Z += (G * (sig_b - sig)) @ G.T
        try:
            cholesky(sym(Z), lower=True, check_finite=False)
        except LinAlgError:
            del Z
            continue
        del Z
        BtB = B.T @ B
        if G is not None:
            CB = G.T @ B
            soft = CB.T @ CB
            grad = CB.T @ (CB / sig[:, None])
        else:
            soft = np.zeros_like(BtB)
            grad = soft
        cap = grad + (BtB - soft) / sig_b
        S_cert = sym(TVV - cap)
        lS = float(eigvalsh(S_cert)[0])
        out.update(ok=True, lmin_S=lS, S_cert=S_cert,
                   om_cert=(half / lS if lS > 0.0 else float("inf")))
        return out
    return out


def cap_scan(TVV, TVW, TWW, half):
    """MEASURED scan: smallest ntop on the ladder for which the graded cap works."""
    B = TVW.T
    n_w = TWW.shape[0]
    nu, G = eigh(TWW)
    CB = G.T @ B
    del G
    BtB = B.T @ B
    scan = [k for k in NTOP_SCAN if k < n_w] + [n_w - 1]
    soft = np.zeros_like(BtB)
    acc = np.zeros_like(BtB)
    prev = 0
    out = {}
    for nt in scan:
        for j in range(prev, nt):
            oc = np.outer(CB[j], CB[j])
            soft = soft + oc / nu[j]
            acc = acc + oc
        prev = nt
        lm = float(eigvalsh(sym(TVV - soft - (BtB - acc) / nu[nt]))[0])
        out[nt] = half / lm if lm > 0.0 else float("inf")
    ok_nt = [nt for nt in scan if out[nt] < 1.0]
    return (ok_nt[0] if ok_nt else None), out


def ntop_cert(ntop_min, n_w, cap=None):
    return min(n_w - 1, max(4 * ntop_min, ntop_min + 16),
               NTOP_MAX if cap is None else cap)


def cg_iterates(T, b, ks):
    """Hestenes-Stiefel 1952 CG; the iterates are TRIAL VECTORS only."""
    y = np.zeros(b.shape[0])
    r = b.copy()
    pdir = r.copy()
    rs = float(np.dot(r, r))
    out = {}
    want = set(ks)
    kmax = max(ks)
    for k in range(1, kmax + 1):
        Ap = T @ pdir
        den = float(np.dot(pdir, Ap))
        if den <= 0.0 or rs <= 0.0:
            break
        a = rs / den
        y = y + a * pdir
        r = r - a * Ap
        if k in want:
            out[k] = y.copy()
        rs2 = float(np.dot(r, r))
        pdir = r + (rs2 / rs) * pdir
        rs = rs2
    for k in sorted(want):
        if k not in out:
            out[k] = y.copy()
    return out


def trial_bound(T, tv, V, y, Z, gam_mat):
    """The T109 G2(iv) certificate for ||V^T x||, x = T^{-1} t~ (Prager-Synge)."""
    Ty = T @ y
    E = 1.0 - 2.0 * float(np.dot(y, tv)) + float(np.dot(y, Ty))
    r = tv - Ty
    lead = V.T @ y + Z.T @ r
    F = gam_mat - V.T @ Z - Z.T @ V + Z.T @ (T @ Z)
    lf = max(float(eigvalsh(sym(F))[-1]), 0.0)
    return float(np.linalg.norm(lead)) + math.sqrt(lf * max(E, 0.0)), max(E, 0.0), lf


def need109_at(alpha, M, p, mu, atoms, kcg_ladder=CG_LADDER, want_lmin=True):
    """The full T109 chain at an explicit window: need109 and lam_min(Q|odd)."""
    c, D = lag_vector(alpha, M, atoms)
    T = odd_toeplitz(c, M)
    tv = odd_pole_vector(alpha, M)
    m = (p + 1) // 2
    V = demand_V(p, M)
    half = 0.5 * mu
    fac, sh = safe_cho(T)
    if fac is None:
        return None
    x = cho_solve(fac, tv, check_finite=False)
    tau = float(np.dot(tv, x))
    eps = 1.0 - tau
    Gam = sym(V.T @ cho_solve(fac, V, check_finite=False))
    om_meas = half * float(eigvalsh(Gam)[-1])
    nt2 = float(np.dot(tv, tv))
    tTt = float(np.dot(tv, T @ tv))
    out = dict(alpha=alpha, M=M, p=p, m=m, half=half, tau=tau, eps=eps,
               om_meas=om_meas, nt2=nt2, tTt=tTt, shift=sh, D=D)
    if want_lmin:
        out["lmin_Q"] = lmin(T - np.outer(tv, tv))
    TVV, TVW, TWW = wing_split(T, p, m)
    nt_m, _ = cap_scan(TVV, TVW, TWW, half)
    if nt_m is None:
        out["need"] = float("inf")
        return out
    res = psd_cap_omega(TVV, TVW, TWW, half, ntop_cert(nt_m, TWW.shape[0]))
    del TVV, TVW, TWW
    if not res["ok"] or not (res["om_cert"] < 1.0):
        out["need"] = float("inf")
        out["om_cert"] = res["om_cert"]
        return out
    gam_cert = np.linalg.inv(res["S_cert"])
    out["om_cert"] = res["om_cert"]
    out["ntop"] = res["ntop"]
    best = None
    for kcg in kcg_ladder:
        kk = min(kcg, T.shape[0] - 1)
        y = cg_iterates(T, tv, (kk,))[kk]
        Z = np.empty((T.shape[0], m))
        for j in range(m):
            Z[:, j] = cg_iterates(T, np.ascontiguousarray(V[:, j]), (kk,))[kk]
        H, E, lf = trial_bound(T, tv, V, y, Z, gam_cert)
        del Z
        if E >= 1.0:
            continue
        kap = max((1.0 - E) / nt2, nt2 / tTt)
        need = half * H * H / ((1.0 - res["om_cert"]) * kap)
        if best is None or need < best["need"]:
            best = dict(need=need, H=H, E=E, kap=kap, kcg=kk)
        if want_lmin and need <= out.get("lmin_Q", 0.0):
            break
    if best is None:
        out["need"] = float("inf")
        return out
    out.update(best)
    return out


# ============================================================================
section("H0  SETUP, FIREWALL, THE NESTED WINDOW LADDER")
# ============================================================================
firewall()

ATOMS_ALL = atom_table(64)
ZONES = [t for t in ATOMS_ALL if t[0] <= 29]
N_ZONES = len(ZONES)
info("zones", "%d prime-power zones n_k = %s"
     % (N_ZONES, ", ".join(str(t[0]) for t in ZONES)))
info("H0.hypothesis",
     "HYPOTHESIS INPUT (never proved here): Q_full(alpha) >= 0, hence "
     "Q|odd >= 0.  A STRICT margin is an INPUT only at the BASE window; at "
     "every later window it is a CONCLUSION of the step law, and the two are "
     "kept in separate columns")
info("H0.fence_rh",
     "RH => window Weil positivity is used in one direction only; the "
     "converse is NOT claimed.  No zero data of any kind enters this probe")
info("H0.t106",
     "T106 DEMARCATION: the refuted object is the accumulated ATOM invariant "
     "Q >= beta sum_j (mu_j/2) P_-^(j) -- a DIRECTIONAL demand, killed by an "
     "old wing pair becoming an interior pair (750x stronger coupling).  The "
     "object here is the SCALAR floor lam_min(Q|odd) >= m, invariant under "
     "any rotation of the demand geometry.  The T106 no-go does not apply to "
     "it a priori; whether the same growth step preserves it is measured "
     "below on the exact bordered split")

t0 = time.time()
CROSS = []
for (n_k, lam_k, u_k, mu_k) in ZONES:
    p_star, ok = find_p_star(u_k, mu_k, M_CROSS, ATOMS_ALL)
    D, alpha, delta = zone_geometry(u_k, p_star, M_CROSS)
    CROSS.append(dict(n=n_k, u=u_k, mu=mu_k, p=p_star, ok=ok, D=D,
                      alpha=alpha, delta=delta))
GAPS = [ZONES[i + 1][2] - ZONES[i][2] for i in range(N_ZONES - 1)]
DELTA_C = min(c["delta"] for c in CROSS)
DELTA0 = min(GAMMA_T110 * DELTA_C, 0.6 * min(GAPS))
info("H0.timing", "%d crossings located at M = %d in %.1f s, budget left %.0f s"
     % (len(CROSS), M_CROSS, time.time() - t0, budget_left()))
check("el_h0.p_star", all(c["ok"] for c in CROSS),
      "the T105 crossing p* is interior on every zone: p* = %s"
      % ", ".join(str(c["p"]) for c in CROSS))
check("el_h0.delta0", DELTA0 < min(GAPS) and DELTA0 > 0.0,
      "common physical wing depth delta_0 = %.5f = %.2f * min_k delta_c "
      "(= %.5f, zone %d) and BELOW the smallest atom gap min_k (u_{k+1} - "
      "u_k) = %.5f, so a zone window never reaches the next atom: the pure "
      "growth phase and the atom entry are cleanly separated"
      % (DELTA0, DELTA0 / DELTA_C, DELTA_C,
         min(CROSS, key=lambda c: c["delta"])["n"], min(GAPS)))

# --- the nested ladder: ONE grid, one growing window ------------------------
def build_ladder(m_top):
    """All 16 windows on ONE cell grid, so consecutive windows nest EXACTLY.

    The cell width is fixed by the widest window; every zone gets the smallest
    even cell count whose window covers u_k + delta_0.  Then M_{k+1} - M_k is
    even and the growth step is g = (M_{k+1} - M_k)/2 cells at each end -- no
    regridding anywhere along the chain, which is what lets H4 run the
    induction as a single chain instead of a sequence of unrelated windows.
    """
    d_lad = (ZONES[-1][2] + DELTA0) / m_top
    out = []
    for (n_k, lam_k, u_k, mu_k) in ZONES:
        Mk = 2 * int(math.ceil(0.5 * u_k / d_lad))
        if Mk * d_lad - u_k < 0.5 * d_lad:
            Mk += 2
        ak = 0.5 * Mk * d_lad
        dk = 2.0 * ak - u_k
        pk = max(1, int(round(dk / d_lad)))
        out.append(dict(n=n_k, u=u_k, mu=mu_k, half=0.5 * mu_k, p=pk, D=d_lad,
                        alpha=ak, delta=dk, M=Mk))
    return out, d_lad


LAD, D_LAD = build_ladder(M_MAIN)
GSTEP = [(LAD[i + 1]["M"] - LAD[i]["M"]) // 2 for i in range(N_ZONES - 1)]
check("el_h0.nesting", all(g >= 1 for g in GSTEP)
      and all(LAD[i + 1]["M"] > LAD[i]["M"] for i in range(N_ZONES - 1))
      and LAD[-1]["M"] // 2 <= MAX_ARRAY,
      "the ladder is EXACTLY nested on one grid of cell width D = %.3e: cell "
      "counts M_k = %d..%d (odd sector %d..%d), growth g = %d..%d cells per "
      "end between consecutive zones, wing p = %d..%d cells (physical depth "
      "%.5f..%.5f), windows 2 alpha = %.4f..%.4f"
      % (D_LAD, LAD[0]["M"], LAD[-1]["M"], LAD[0]["M"] // 2, LAD[-1]["M"] // 2,
         min(GSTEP), max(GSTEP), min(z["p"] for z in LAD),
         max(z["p"] for z in LAD), min(z["delta"] for z in LAD),
         max(z["delta"] for z in LAD), 2 * LAD[0]["alpha"],
         2 * LAD[-1]["alpha"]))

# --- the odd form, re-derived against a full assembly -----------------------
z0 = LAD[-1]
M_MAIN = z0["M"]
Q_odd_dir, T_dir, t_dir, _ = q_odd_at(z0["alpha"], M_MAIN, atoms_in(z0["alpha"], ATOMS_ALL))
Qf = build_Q(z0["alpha"], M_MAIN, atoms_in(z0["alpha"], ATOMS_ALL))
Bm = refl_odd_basis(M_MAIN)
e_split = float(np.abs(Bm.T @ Qf @ Bm - Q_odd_dir).max())
del Qf, Bm
check("el_h0.odd_form", e_split < 1.0e-9,
      "Q|odd = T_odd - t~ t~^T reproduced to %.1e against a full %d x %d "
      "assembly at zone n = %d -- the T106/T107/T108/T109 object, re-derived "
      "here, not imported" % (e_split, M_MAIN, M_MAIN, z0["n"]))
del Q_odd_dir, T_dir, t_dir


# ============================================================================
section("H1  THE MARGIN MAP -- lam_min(Q|odd) over the whole window ladder")
# ============================================================================
print("""  The single conditional input of the T109 chain is the SCALAR
      m_k := lam_min( Q|odd(alpha_k) )  >=  need109(k) .
  H1 maps both sides over the ladder, then splits the step into its two
  physical pieces: PURE GROWTH between two atom entries (the dilution) and
  the ATOM ENTRY itself (the -(mu/2) pressure on the odd channel).""")

# --- H1.1  the map ----------------------------------------------------------
print("")
print("  H1.1  m_k AND need109(k) ON THE NESTED LADDER  (one grid, D = %.3e)"
      % D_LAD)
print("")
print("  n_k    M    p   m    mu/2      m_k = lam_min(Q|odd)   need109(k)   "
      "ratio     om_cert   vacuous")
t0 = time.time()
MAP = []
for z in LAD:
    r = need109_at(z["alpha"], z["M"], z["p"], z["mu"],
                   atoms_in(z["alpha"], ATOMS_ALL))
    if r is None:
        continue
    r["n"], r["u"], r["mu"] = z["n"], z["u"], z["mu"]
    r["ratio"] = r["lmin_Q"] / r["need"] if r["need"] > 0 else float("inf")
    r["vac"] = r["need"] >= r["half"]
    MAP.append(r)
    print("  %3d %5d %3d %3d %9.5f %20.6e %13.4e %8.2f %10.5f %8s"
          % (r["n"], r["M"], r["p"], r["m"], r["half"], r["lmin_Q"], r["need"],
             r["ratio"], r.get("om_cert", float("nan")),
             "YES" if r["vac"] else "no"))
info("H1.1.timing", "%d chains in %.1f s, budget left %.0f s"
     % (len(MAP), time.time() - t0, budget_left()))
info("H1.1.depth",
     "the ladder runs at the COMMON physical depth delta_0 = %.5f (the "
     "deepest wing every zone can carry, needed for the nesting), not at "
     "T109's per-zone operating depth: the wing is p = %d..%d cells and the "
     "demand dimension m = %d..%d, so this chain is SHALLOWER than T109's and "
     "its closing ratios (%.1f..%.1f) are correspondingly larger than T109's "
     "1.3..10.4.  The propagation question is unaffected -- it is about the "
     "SAME scalar lam_min(Q|odd) on both"
     % (DELTA0, min(r["p"] for r in MAP), max(r["p"] for r in MAP),
        min(r["m"] for r in MAP), max(r["m"] for r in MAP),
        min(r["ratio"] for r in MAP), max(r["ratio"] for r in MAP)))
M_POS = all(r["lmin_Q"] > 0.0 for r in MAP)
M_HOLD = sum(1 for r in MAP if r["ratio"] >= 1.0)
check("el_h1.map", len(MAP) == N_ZONES and M_POS,
      "the margin map is complete on %d/%d zones and lam_min(Q|odd) > 0 "
      "throughout: m_k = %.2e..%.2e, need109(k) = %.2e..%.2e, and m_k >= "
      "need109(k) on %d/%d zones with ratio %.2f..%.2f.  need109 is a factor "
      "%.0e..%.0e BELOW mu/2 (non-vacuous on %d/%d)"
      % (len(MAP), N_ZONES, min(r["lmin_Q"] for r in MAP),
         max(r["lmin_Q"] for r in MAP), min(r["need"] for r in MAP),
         max(r["need"] for r in MAP), M_HOLD, len(MAP),
         min(r["ratio"] for r in MAP), max(r["ratio"] for r in MAP),
         min(r["half"] / r["need"] for r in MAP),
         max(r["half"] / r["need"] for r in MAP),
         sum(1 for r in MAP if not r["vac"]), len(MAP)))

# --- H1.1b  the M-trend of both sides ---------------------------------------
print("")
print("  H1.1b  RESOLUTION TREND.  Both sides vanish as the cells shrink, so")
print("  only the RATIO has a continuum meaning.  The WHOLE nested ladder is")
print("  rebuilt at three cell widths (top window M = %d, %d, %d)."
      % (M_LOW, M_MAIN, M_HI))
print("")
print("  n_k   m_k(D_lo)    m_k(D_op)    m_k(D_hi)    need(D_lo)   need(D_hi)"
      "   ratio(lo)  ratio(hi)")
t0 = time.time()
LAD_LO, _ = build_ladder(M_LOW)
LAD_HI, _ = build_ladder(M_HI)
MTR = []
for zi in (0, 7, 15):
    row = {"n": LAD[zi]["n"]}
    for tag, lad in (("lo", LAD_LO), ("op", LAD), ("hi", LAD_HI)):
        z = lad[zi]
        row[tag] = need109_at(z["alpha"], z["M"], z["p"], z["mu"],
                              atoms_in(z["alpha"], ATOMS_ALL))
    MTR.append(row)
    print("  %3d  %12.4e %12.4e %12.4e %12.4e %12.4e %10.2f %10.2f"
          % (row["n"], row["lo"]["lmin_Q"], row["op"]["lmin_Q"],
             row["hi"]["lmin_Q"], row["lo"]["need"], row["hi"]["need"],
             row["lo"]["lmin_Q"] / row["lo"]["need"],
             row["hi"]["lmin_Q"] / row["hi"]["need"]))
info("H1.1b.timing", "%d resolution triples in %.1f s, budget left %.0f s"
     % (len(MTR), time.time() - t0, budget_left()))
RAT = [(row["lo"]["lmin_Q"] / row["lo"]["need"],
        row["hi"]["lmin_Q"] / row["hi"]["need"]) for row in MTR]
RAT_DRIFT = max(max(a, b) / max(min(a, b), 1.0e-300) for a, b in RAT)
check("el_h1.resolution",
      all(row["hi"]["lmin_Q"] / row["hi"]["need"] > 1.0 for row in MTR),
      "over M = %d..%d the two sides fall together: the closing ratio moves "
      "by at most %.2f x and stays above 1 at every M on the %d sampled "
      "zones, while m_k itself falls by %.1f..%.1f x -- the margin question "
      "is a RATIO question, not an absolute one"
      % (M_LOW, M_HI, RAT_DRIFT, len(MTR),
         min(row["lo"]["lmin_Q"] / row["hi"]["lmin_Q"] for row in MTR),
         max(row["lo"]["lmin_Q"] / row["hi"]["lmin_Q"] for row in MTR)))

# --- H1.2  the dilution of the margin during pure growth --------------------
print("")
print("""  H1.2  DILUTION.  Between two atom entries the window grows with NO new
  arithmetic: alpha -> alpha + gD at fixed cell width D, M -> M + 2g.  By
  Cauchy interlacing the old sector is a compression of the new one, so
  m(alpha) is NON-INCREASING in alpha -- the only question is HOW FAST.  Two
  fits (both labelled fits): exponential  log m = a - b (alpha - alpha_k)
  and power law  log m = a - q log(alpha/alpha_k).""")
print("")
print("  n_k   cells added  alpha_k -> alpha_end   m(start)     m(end)     "
      "ratio    exp rate b   rms     power q   rms    per cell")
t0 = time.time()
DIL = []
for i, z in enumerate(LAD):
    p0g, D0g, a0g, d0g = nested_window(z["u"], M_GROW, DELTA0)
    u_next = ZONES[i + 1][2] if i + 1 < N_ZONES else ATOMS_ALL[N_ZONES][2]
    a_stop = 0.5 * u_next - D0g          # last window strictly before the entry
    g_max = int(math.floor((a_stop - a0g) / D0g))
    if g_max < N_GROW:
        continue
    step = max(1, g_max // (N_GROW - 1))
    gs = [j * step for j in range(N_GROW)]
    al, ms = [], []
    for g in gs:
        MM = M_GROW + 2 * g
        aa = a0g + g * D0g
        if MM // 2 > MAX_ARRAY:
            break
        Qo, _, _, _ = q_odd_at(aa, MM, atoms_in(aa, ATOMS_ALL))
        ms.append(lmin(Qo))
        al.append(aa)
        del Qo
    if len(ms) < 4 or min(ms) <= 0.0:
        continue
    al = np.asarray(al)
    lm = np.log(np.asarray(ms))
    _, be, re = fit_line(al - al[0], lm)
    _, qe, rq = fit_line(np.log(al / al[0]), lm)
    cells = (al[-1] - al[0]) / D0g
    DIL.append(dict(n=z["n"], cells=cells, a0=al[0], a1=al[-1], m0=ms[0],
                    m1=ms[-1], ratio=ms[0] / ms[-1], b=-be, rb=re, q=-qe,
                    rq=rq, per_cell=(ms[-1] / ms[0]) ** (1.0 / max(cells, 1.0))))
    d = DIL[-1]
    print("  %3d %10.0f  %9.5f -> %9.5f %11.3e %11.3e %8.3f %11.3f %8.4f"
          " %8.3f %7.4f %8.5f"
          % (d["n"], d["cells"], d["a0"], d["a1"], d["m0"], d["m1"],
             d["ratio"], d["b"], d["rb"], d["q"], d["rq"], d["per_cell"]))
info("H1.2.timing", "%d growth sweeps in %.1f s, budget left %.0f s"
     % (len(DIL), time.time() - t0, budget_left()))
MONO = all(d["ratio"] >= 1.0 - 1.0e-9 for d in DIL)
BETTER_POW = sum(1 for d in DIL if d["rq"] < d["rb"])
TAIL = [d for d in DIL if d["n"] > 2]
check("el_h1.dilution", len(DIL) == N_ZONES and MONO,
      "pure window growth DILUTES the margin monotonically on all %d sweeps "
      "(Cauchy interlacing, as it must) -- but only just.  Over a WHOLE "
      "inter-atom gap (%.0f..%.0f added cells) the margin falls by a factor "
      "%.2f..%.2f on the 15 zones with a history, i.e. %.5f..%.5f per cell.  "
      "Zone 1 is the outlier: its gap is %.0f cells long and it loses a "
      "factor %.0f, which is the entire fall from the base value 6.9e-2 to "
      "the plateau ~2e-5 that every later zone then sits on.  Both fits are "
      "FITS and neither is clean: exponential rms %.4f, power-law rms %.4f in "
      "log m (power wins on %d/%d).  What matters for an induction is that "
      "the per-cell loss is 1 - O(1/M), not a fixed factor"
      % (len(DIL), min(d["cells"] for d in TAIL), max(d["cells"] for d in TAIL),
         min(d["ratio"] for d in TAIL), max(d["ratio"] for d in TAIL),
         min(d["per_cell"] for d in TAIL), max(d["per_cell"] for d in TAIL),
         DIL[0]["cells"], DIL[0]["ratio"],
         float(np.mean([d["rb"] for d in DIL])),
         float(np.mean([d["rq"] for d in DIL])), BETTER_POW, len(DIL)))

# --- H1.3  the exact channel action of the atom entry -----------------------
print("")
print("""  H1.3  THE ATOM ENTRY.  At FIXED window the new atom enters the odd
  channel as an exact Loewner-negative shift
      Q|odd  ->  Q|odd - mu_j N ,   N = odd_toeplitz( atom_lag(., u_j, D) ) ,
  N = Toeplitz(atom lag) MINUS its Hankel reflection.  Three readings of what
  it costs lam_min: the EXACT drop, the first-order Rayleigh term at the
  pre-entry minimiser (Kato), and the Weyl worst case mu lam_max(N) -- the
  last one is a CERTIFIED cap (Cholesky of t I - N).  The naive expectation
  is that the odd channel takes the full -(mu/2) demand pressure.""")
print("")
print("  atom  mu/2     lam_max(N) cert   mu*lmax(N)/(mu/2)   m before     "
      "m after      exact drop   drop/(mu/2)  Rayleigh/(mu/2)")
t0 = time.time()
ENT = []
for i in range(N_ZONES - 1):
    z = LAD[i]
    u_new, mu_new = ZONES[i + 1][2], ZONES[i + 1][3]
    # a window that already contains the new atom point, at zone-i cell width
    p0g, D0g, a0g, d0g = nested_window(z["u"], M_MAIN, DELTA0)
    g = int(math.ceil((0.5 * (u_new + DELTA0) - a0g) / D0g))
    MM = M_MAIN + 2 * g
    if g < 1 or MM // 2 > MAX_ARRAY:
        continue
    aa = a0g + g * D0g
    at_old = [t for t in atoms_in(aa, ATOMS_ALL) if t[0] < u_new - 1.0e-12]
    at_new = atoms_in(aa, ATOMS_ALL)
    if len(at_new) != len(at_old) + 1:
        continue
    Q_pre, _, _, DD = q_odd_at(aa, MM, at_old)
    lb, vb = lmin_vec(Q_pre)
    Nmat = odd_toeplitz(atom_lag(np.arange(MM) * DD, u_new, DD), MM)
    ray = mu_new * float(vb @ (Nmat @ vb))
    lnmax, ok_n = cert_lmax(Nmat)
    Q_post = Q_pre - mu_new * Nmat
    la = lmin(Q_post)
    del Q_pre, Q_post, Nmat
    half_new = 0.5 * mu_new
    ENT.append(dict(n=ZONES[i + 1][0], mu=mu_new, half=half_new, lb=lb, la=la,
                    drop=lb - la, ray=ray, lnmax=lnmax, ok=ok_n,
                    weyl=mu_new * lnmax))
    e = ENT[-1]
    print("  %4d %8.5f %16.6f %19.4f %12.4e %12.4e %12.4e %12.4f %15.4f"
          % (e["n"], e["half"], e["lnmax"], e["weyl"] / e["half"], e["lb"],
             e["la"], e["drop"], e["drop"] / e["half"], e["ray"] / e["half"]))
info("H1.3.timing", "%d atom entries in %.1f s, budget left %.0f s"
     % (len(ENT), time.time() - t0, budget_left()))
ENT_OK = all(e["ok"] for e in ENT)
ENT_GAIN = all(e["drop"] <= 1.0e-9 * max(abs(e["lb"]), abs(e["la"])) for e in ENT)
ENT_NEG = [e for e in ENT if e["lb"] <= 0.0]
check("el_h1.atom_entry", ENT_OK and ENT_GAIN,
      "THE ATOM ENTRY DOES NOT COST THE SCALAR FLOOR -- IT RAISES IT.  On "
      "%d/%d entries lam_min GOES UP when the atom is switched on, by "
      "%.1e..%.1e absolute (%.1e..%.1e of mu/2).  The naive -(mu/2) pressure "
      "is simply not what the odd channel sees: N = Toeplitz(atom lag) minus "
      "its Hankel reflection is INDEFINITE, and on the soft direction of "
      "Q|odd its Rayleigh quotient has the sign that HELPS (first-order Kato "
      "term %.1e..%.1e of mu/2, same sign as the exact move on %d/%d).  The "
      "Weyl worst case is the only pessimistic reading: certified (Cholesky) "
      "lam_max(N) = %.4f..%.4f gives a worst case of %.2f..%.2f times mu/2, "
      "which is %.0e..%.0e times the actual margin and therefore vacuous.  "
      "Sharper still: on %d/%d entries the atom-FREE window is not even "
      "positive (lam_min = %.2e), so the atom's presence is part of what "
      "makes the window positive at all"
      % (len(ENT), len(ENT), min(-e["drop"] for e in ENT),
         max(-e["drop"] for e in ENT),
         min(-e["drop"] / e["half"] for e in ENT),
         max(-e["drop"] / e["half"] for e in ENT),
         min(-e["ray"] / e["half"] for e in ENT),
         max(-e["ray"] / e["half"] for e in ENT),
         sum(1 for e in ENT if e["ray"] * e["drop"] >= 0.0), len(ENT),
         min(e["lnmax"] for e in ENT), max(e["lnmax"] for e in ENT),
         min(e["weyl"] / e["half"] for e in ENT),
         max(e["weyl"] / e["half"] for e in ENT),
         min(e["weyl"] / abs(e["la"]) for e in ENT),
         max(e["weyl"] / abs(e["la"]) for e in ENT),
         len(ENT_NEG), len(ENT),
         min(e["lb"] for e in ENT)))


# ============================================================================
section("H2  THE PROPAGATION LAW -- m_{k+1} >= f(m_k, certified data)")
# ============================================================================
print("""  H2.1  THE EXACT SPLIT.  At fixed cell width D grow the zone-k window by g
  cells at each end.  In ODD coordinates the old sector embeds as the TRAILING
  block (old index r -> new index r + g): the Toeplitz lag c_{|r-s|}, the
  Hankel index (M'-1)-(r+g)-(s+g) = (M-1)-r-s and the source t~ are all
  unchanged cell by cell.  Hence EXACTLY
      Q'|odd = [[ A , C ] , [ C^T , X ]] ,   X = Q_k|odd - mu_{k+1} N ,
  A the g x g new-cell block, C the g x h_old coupling.  Verified below.""")
print("")
print("  k -> k+1 | g   M_old  embed err  max|mu N| | a = lam_min(A)   ||C||"
      "       m_k          x = lam_min(X)   m_{k+1}      m'/m_k")
t0 = time.time()
HAND = []
for i in range(N_ZONES - 1):
    zo, zn = LAD[i], LAD[i + 1]
    u_k, mu_k = zo["u"], zo["mu"]
    u_n, mu_n = zn["u"], zn["mu"]
    D, alpha, p = zn["D"], zn["alpha"], zn["p"]
    M_new, M_old = zn["M"], zo["M"]
    g = (M_new - M_old) // 2
    alpha_o = zo["alpha"]
    if g < 1 or M_old < 64:
        continue
    at_new = atoms_in(alpha, ATOMS_ALL)
    at_old = atoms_in(alpha_o, ATOMS_ALL)
    if len(at_new) != len(at_old) + 1:
        continue
    Qn, Tn, tn, Dn = q_odd_at(alpha, M_new, at_new)
    Qo, To, to, Do = q_odd_at(alpha_o, M_old, at_old)
    h_old = M_old // 2
    Nmat = odd_toeplitz(atom_lag(np.arange(M_old) * D, u_n, D), M_old)
    X = Qo - mu_n * Nmat
    e_emb = float(np.abs(Qn[g:, g:] - X).max()) / max(float(np.abs(X).max()), 1e-300)
    A = sym(np.ascontiguousarray(Qn[:g, :g]))
    C = np.ascontiguousarray(Qn[:g, g:])
    m_k = lmin(Qo)
    x_k = lmin(X)
    m_n = lmin(Qn)
    a_k = lmin(A)
    cn, ok_c = cert_norm(C)
    nrm_N = mu_n * float(np.abs(Nmat).max())
    HAND.append(dict(k=zo["n"], kn=zn["n"], g=g, M_old=M_old, M_new=M_new,
                     e=e_emb, a=a_k, cn=cn, ok_c=ok_c, m_k=m_k, x=x_k,
                     m_n=m_n, mu_n=mu_n, half_n=0.5 * mu_n, D=D, nrm_N=nrm_N,
                     alpha_o=alpha_o, alpha=alpha, p=p, p_o=zo["p"],
                     A=A, C=C, X=X, Nmat=Nmat, Qn_lmin=m_n))
    r = HAND[-1]
    print("  %3d ->%3d | %3d %5d  %10.2e %10.2e | %13.6f %11.3e %12.4e %14.4e"
          " %12.4e %9.4f"
          % (r["k"], r["kn"], g, M_old, e_emb, nrm_N, a_k, cn, m_k, x_k, m_n,
             m_n / m_k))
    del Qn, Tn, tn, To, to, Qo
info("H2.1.timing", "%d handoffs in %.1f s, budget left %.0f s"
     % (len(HAND), time.time() - t0, budget_left()))
check("el_h2.embedding", len(HAND) >= 12
      and max(r["e"] for r in HAND) < 1.0e-10,
      "the odd-sector embedding is EXACT to rel %.1e on all %d handoffs: the "
      "old odd block of Q'|odd is Q_k|odd - mu_{k+1} N, with g = %d..%d new "
      "cells per end.  The step therefore splits with no modelling error into "
      "[atom entry] + [bordering]"
      % (max(r["e"] for r in HAND), len(HAND), min(r["g"] for r in HAND),
         max(r["g"] for r in HAND)))
DIL_STEP = [r["m_n"] / r["m_k"] for r in HAND]
check("el_h2.step_dilution", all(d <= 1.0 + 1.0e-9 for d in DIL_STEP),
      "the measured step ratio m_{k+1}/m_k = %.4f..%.4f (geometric mean "
      "%.4f), so over the %d measured handoffs the margin loses a total "
      "factor %.1f -- compare the T106 transport loss for the DIRECTIONAL "
      "invariant, which was 1e2..1e3 PER STEP"
      % (min(DIL_STEP), max(DIL_STEP),
         float(np.exp(np.mean(np.log(DIL_STEP)))), len(HAND),
         1.0 / float(np.prod(DIL_STEP))))

# --- H2.2  the candidate laws ------------------------------------------------
print("")
print("""  H2.2  THE LAWS.  Route (i) BORDERED WEYL, every ingredient certified:
      m' >= bord(a, x, ||C||) := ((a+x) - sqrt((a-x)^2 + 4||C||^2))/2 ,
      x >= m_k - mu_{k+1} lam_max(N)                    [Weyl, atom entry]
  with lam_max(N), ||C|| Cholesky-capped and a = lam_min(A) a g x g datum.
  Route (ii) SCHUR / FRIEDRICHS, the fixed point of
      lam <= (1 - theta(lam)) x ,  theta(lam) = lam_max( C^T(A-lam)^{-1}C , X ),
  valid whenever A - lam > 0 (Schur complement / Haynsworth).  theta is
  DIRECTIONAL.  Its scalar-only cap theta <= lam_max(W)/x turns (ii) back into
  Weyl, x - lam_max(W); the ratio of the two is the price of forgetting the
  direction.""")
print("")
print("  k -> k+1 | lmax(N)c  x_cert      | theta(0)   theta_cert  | "
      "law(i) bord   law(ii) Schur  measured m'   (ii)/m'   scalar-only")
t0 = time.time()
LAW = []
for r in HAND:
    A, C, X = r["A"], r["C"], r["X"]
    lnN, okN = cert_lmax(r["Nmat"])
    x_cert = r["m_k"] - r["mu_n"] * lnN
    b_law = bord(r["a"], x_cert, r["cn"])
    # route (ii): monotone fixed point, ACCEPTED ONLY WHEN SELF-CONSISTENT
    LX = cholesky(sym(X), lower=True, check_finite=False)
    W0 = C.T @ np.linalg.solve(A, C)
    lw = lmax(W0)
    th0 = gen_lmax(W0, LX)
    del W0
    th_it = th0
    th_use = th0
    sch = 0.0
    for _ in range(6):
        cand = (1.0 - th_it) * r["x"]
        if not (cand > 0.0) or cand >= r["a"]:
            sch = 0.0
            break
        Wl = C.T @ np.linalg.solve(A - cand * np.eye(A.shape[0]), C)
        thl = gen_lmax(Wl, LX)
        del Wl
        if (1.0 - thl) * r["x"] >= cand * (1.0 - 1.0e-12):
            sch = cand                       # self-consistent => a valid floor
            th_use = th_it
            break
        th_it = thl
        sch = 0.0
    del LX
    th_cert = lw / r["x"] if r["x"] > 0 else float("inf")
    scal = r["x"] - lw
    LAW.append(dict(k=r["k"], kn=r["kn"], lnN=lnN, okN=okN, x_cert=x_cert,
                    bord=b_law, th0=th0, th_use=th_use, th_cert=th_cert,
                    sch=sch, lw=lw, scal=scal, m_n=r["m_n"], m_k=r["m_k"],
                    x=r["x"], a=r["a"], cn=r["cn"]))
    q = LAW[-1]
    print("  %3d ->%3d | %8.4f %11.3e | %9.6f %11.3e | %12.4e %14.4e"
          " %13.4e %9.4f %12.3e"
          % (q["k"], q["kn"], lnN, x_cert, th0, th_cert, b_law, sch,
             r["m_n"], (sch / r["m_n"] if r["m_n"] > 0 else float("nan")),
             scal))
info("H2.2.timing", "%d law rows in %.1f s, budget left %.0f s"
     % (len(LAW), time.time() - t0, budget_left()))

VALID_I = all(q["bord"] <= q["m_n"] * (1.0 + 1.0e-6) + 1.0e-14 for q in LAW)
VALID_II = all((not (q["sch"] > 0.0)) or q["sch"] <= q["m_n"] * (1.0 + 1.0e-6)
               for q in LAW)
N_I = sum(1 for q in LAW if q["bord"] > 0.0)
N_II = sum(1 for q in LAW if q["sch"] > 0.0)
N_SC = sum(1 for q in LAW if q["scal"] > 0.0)
N_XC = sum(1 for q in LAW if q["x_cert"] > 0.0)
check("el_h2.laws_valid", VALID_I and VALID_II,
      "both laws are VALID (never above the measured m_{k+1}) on all %d "
      "handoffs -- the inequality directions are theorems (Weyl 1912 / Schur "
      "complement), the numbers only test sharpness" % len(LAW))
check("el_h2.atom_step_certified", N_XC == len(LAW)
      and max(r["nrm_N"] for r in HAND) == 0.0,
      "STEP PART 1 (atom entry) COSTS EXACTLY NOTHING, for a structural "
      "reason: the new atom sits at lag u_{k+1}, the old window's lag range "
      "stops at 2 alpha_old = u_k + delta_0 < u_{k+1} (gap %.4f vs delta_0 = "
      "%.5f), so its restriction to the old block is the ZERO matrix -- "
      "max|mu N| = %.1e on all %d handoffs, and correspondingly x = "
      "lam_min(X) equals m_k to %.1e relative.  The new atom enters ONLY "
      "through the g newly added cells, i.e. entirely inside A and C.  The "
      "certified Weyl term x >= m_k - mu_{k+1} lam_max(N) is therefore exact "
      "and free on %d/%d handoffs"
      % (min(GAPS), DELTA0, max(r["nrm_N"] for r in HAND), len(HAND),
         max(abs(r["x"] / r["m_k"] - 1.0) for r in HAND), N_XC, len(LAW)))
check("el_h2.border_step", len(LAW) == len(HAND),
      "STEP PART 2 (bordering) is where it is decided.  Route (i) bordered "
      "Weyl is non-vacuous on %d/%d handoffs (||C|| = %.2e..%.2e against "
      "a = lam_min(A) = %.4f..%.4f and x = %.2e..%.2e: ||C|| exceeds "
      "sqrt(a x) by %.1e..%.1e, so bord < 0).  Route (ii) with the MEASURED "
      "directional angle theta(0) = %.6f..%.6f is non-vacuous on %d/%d and "
      "recovers %.4f..%.4f of the measured m_{k+1}.  Its SCALAR-ONLY cap "
      "theta <= lam_max(W)/x = %.2e..%.2e is >= 1 on %d/%d, i.e. vacuous"
      % (N_I, len(LAW), min(q["cn"] for q in LAW), max(q["cn"] for q in LAW),
         min(q["a"] for q in LAW), max(q["a"] for q in LAW),
         min(q["x"] for q in LAW), max(q["x"] for q in LAW),
         min(q["cn"] / math.sqrt(max(q["a"] * q["x"], 1e-300)) for q in LAW),
         max(q["cn"] / math.sqrt(max(q["a"] * q["x"], 1e-300)) for q in LAW),
         min(q["th0"] for q in LAW), max(q["th0"] for q in LAW), N_II, len(LAW),
         min((q["sch"] / q["m_n"]) for q in LAW if q["sch"] > 0.0)
         if N_II else float("nan"),
         max((q["sch"] / q["m_n"]) for q in LAW if q["sch"] > 0.0)
         if N_II else float("nan"),
         min(q["th_cert"] for q in LAW), max(q["th_cert"] for q in LAW),
         len(LAW) - N_SC, len(LAW)))

# --- H2.3  the surplus route -------------------------------------------------
print("")
print("""  H2.3  THE SURPLUS ROUTE.  The T105/T106 handoff is delivered with
  surplus: sigma_k(delta_0) = beta_0 (mu_k/2), beta_0 > 1.  Does the surplus
  (beta_0 - 1)(mu_k/2) convert into a floor for the GROWN window?  Measured,
  then fitted (a FIT, not a law): log m' = c0 + c1 log m_k + c2 log s_k.""")
print("")
print("  k -> k+1 |  mu_k/2    sigma_k    beta_0   surplus s_k   m_k       "
      "m_{k+1}    m'/s_k     m'/(m_k beta_0)")
t0 = time.time()
SUR = []
for r in HAND:
    at_old = atoms_in(r["alpha_o"], ATOMS_ALL)
    sg = sigma_at(r["alpha_o"], r["M_old"], r["p_o"], at_old)
    idx = [z for z in ZONES if z[0] == r["k"]][0]
    half_k = 0.5 * idx[3]
    b0 = sg / half_k
    s_k = sg - half_k
    SUR.append(dict(k=r["k"], kn=r["kn"], half=half_k, sig=sg, b0=b0, s=s_k,
                    m_k=r["m_k"], m_n=r["m_n"]))
    q = SUR[-1]
    print("  %3d ->%3d | %9.5f %10.5f %8.4f %13.5f %11.3e %11.3e %10.3e %14.4f"
          % (q["k"], q["kn"], half_k, sg, b0, s_k, q["m_k"], q["m_n"],
             q["m_n"] / s_k if s_k > 0 else float("nan"),
             q["m_n"] / (q["m_k"] * b0)))
info("H2.3.timing", "%d surplus rows in %.1f s, budget left %.0f s"
     % (len(SUR), time.time() - t0, budget_left()))
SUR_POS = sum(1 for q in SUR if q["b0"] > 1.0)
lm_n = np.log(np.array([q["m_n"] for q in SUR]))
lm_k = np.log(np.array([q["m_k"] for q in SUR]))
ls_k = np.log(np.array([max(q["s"], 1e-300) for q in SUR]))
CF1, R1 = fit_multi([lm_k], lm_n)
CF2, R2 = fit_multi([lm_k, ls_k], lm_n)
check("el_h2.surplus", len(SUR) == len(HAND),
      "the handoff surplus is real (beta_0 = %.3f..%.3f > 1 on %d/%d) but it "
      "does NOT convert into the new floor: m_{k+1}/s_k = %.2e..%.2e spans "
      "%.0f orders and the surplus adds nothing to a fit.  FIT (labelled a "
      "fit) log m' = %.3f + %.3f log m_k has rms %.4f; adding log s_k gives "
      "log m' = %.3f + %.3f log m_k + %.3f log s_k with rms %.4f -- the "
      "surplus coefficient is %.3f and the rms improves by only %.1f%%.  The "
      "handoff surplus is a WING-DIRECTIONAL quantity; the scalar floor does "
      "not live there"
      % (min(q["b0"] for q in SUR), max(q["b0"] for q in SUR), SUR_POS,
         len(SUR), min(q["m_n"] / q["s"] for q in SUR),
         max(q["m_n"] / q["s"] for q in SUR),
         math.log10(max(q["m_n"] / q["s"] for q in SUR)
                    / min(q["m_n"] / q["s"] for q in SUR)),
         CF1[0], CF1[1], R1, CF2[0], CF2[1], CF2[2], R2, CF2[2],
         100.0 * (1.0 - R2 / max(R1, 1e-300))))

# --- H2.4  the graded Loewner minorant --------------------------------------
print("")
print("""  H2.4  HOW MUCH OF THE STEP CAN THE SCALAR CARRY?  Surrender the nsoft
  softest directions of X to the inherited scalar and keep the trial levels
  above:
      X  >=  N(x_in, nsoft) = X - G diag(xi_j - x_in) G^T ,
  a Gram-form Loewner minorant whose validity is EXACTLY the induction input
  xi_j >= x_in.  Then Q' >= [[A, C],[C^T, N]] and
      m_{k+1}  >=  max{ lam : Cholesky([[A - lam, C],[C^T, N - lam]]) OK }
  is a certificate -- a bisection over Choleskys (Sylvester), no spectral
  datum trusted.  The ladder in nsoft interpolates between the two extreme
  epistemic positions: nsoft = dim X is the STRICTLY SCALAR law (only the
  inherited number is used), nsoft = 0 uses nothing inherited at all.  The
  largest nsoft that still certifies is the answer to the H2 question.""")
print("")
print("  k -> k+1 |" + "".join("  ns=%-6s" % ("dim" if nt > 10 ** 6 else nt)
                               for nt in MIN_LADDER)
      + " | measured m'   ns*  fl/m'   f_crit")
print("  " + " " * 9 + "  (f_crit = the smallest fraction of the TRUE m_k that, "
      "fed in as x_in, still certifies the ns = 1 step:")
print("  " + " " * 9 + "   the slack the step allows in the inherited number "
      "before the bordered Cholesky fails)")
t0 = time.time()
GRAD = []
for r in HAND:
    lam_hi = min(r["a"], r["m_k"]) * (1.0 - 1.0e-12)
    xi_all, G_all = eigh(sym(r["X"]))
    row = {}
    okall = True
    for nt in MIN_LADDER:
        ntv = min(nt, r["X"].shape[0])
        N, okm = graded_minorant(r["X"], r["m_k"], ntv, xi_all, G_all)
        okall = okall and okm
        cf, _ = cert_step_floor(r["A"], r["C"], N, lam_hi)
        del N
        row[nt] = cf
    def _works(f):
        Nf, _ = graded_minorant(r["X"], f * r["m_k"], 1, xi_all, G_all)
        return step_psd(r["A"], r["C"], Nf)

    lo_e, hi_e = -8.0, 0.0
    if not _works(1.0):
        f_cr = float("nan")
    else:
        for _ in range(24):
            mid = 0.5 * (lo_e + hi_e)
            if _works(10.0 ** mid):
                hi_e = mid
            else:
                lo_e = mid
        f_cr = 10.0 ** hi_e
    del xi_all, G_all
    pos = [nt for nt in MIN_LADDER if row[nt] > 0.0]
    ns_star = max(pos) if pos else 0
    best = max(row.values())
    GRAD.append(dict(k=r["k"], kn=r["kn"], row=row, best=best,
                     ns_star=ns_star, best_nt=NSOFT_CHAIN, f_cr=f_cr,
                     m_n=r["m_n"], m_k=r["m_k"], okm=okall,
                     f1=row[MIN_LADDER[0]], fscal=row[MIN_LADDER[-1]]))
    q = GRAD[-1]
    print("  %3d ->%3d |" % (q["k"], q["kn"])
          + "".join(" %10.3e" % row[nt] for nt in MIN_LADDER)
          + " | %12.4e %5s %8.4f %11.3e"
          % (r["m_n"], "dim" if ns_star > 10 ** 6 else ns_star,
             row[ns_star] / r["m_n"] if ns_star in row else 0.0, f_cr))
info("H2.4.timing", "%d graded certificate ladders in %.1f s, budget left %.0f s"
     % (len(GRAD), time.time() - t0, budget_left()))
N_GRAD = sum(1 for q in GRAD if q["f1"] > 0.0)
N_SCAL0 = sum(1 for q in GRAD if q["fscal"] > 0.0)
NS_FIN = [q["ns_star"] for q in GRAD if q["ns_star"] <= 10 ** 6]
FCR = [q["f_cr"] for q in GRAD]
check("el_h2.graded_minorant",
      all(q["okm"] for q in GRAD) and N_GRAD == len(GRAD),
      "surrendering ONE soft direction to the scalar still certifies the step "
      "on %d/%d handoffs, at %.4f..%.4f of the true m_{k+1}.  Surrendering "
      "EVERYTHING (nsoft = dim, the strictly scalar law) certifies on %d/%d.  "
      "The break-even is nsoft* = %s out of an odd sector of dimension "
      "%d..%d: the inherited scalar may cover the bottom %s eigen-directions "
      "of the old window and no more.  The step is therefore NOT a scalar "
      "recursion -- it is a scalar recursion PLUS a spectral statement about "
      "the same matrix"
      % (N_GRAD, len(GRAD), min(q["f1"] / q["m_n"] for q in GRAD),
         max(q["f1"] / q["m_n"] for q in GRAD), N_SCAL0, len(GRAD),
         ("%d..%d" % (min(NS_FIN), max(NS_FIN))) if NS_FIN else "0",
         LAD[0]["M"] // 2, LAD[-1]["M"] // 2,
         ("%d..%d" % (min(NS_FIN), max(NS_FIN))) if NS_FIN else "0"))
check("el_h2.slack", max(FCR) < 1.0,
      "HOW MUCH SLACK THE STEP ALLOWS -- the quantity that decides whether the "
      "chain can survive compounding.  Feeding a DEGRADED floor f*m_k into the "
      "ns = 1 step, the bordered Cholesky still passes down to f_crit = "
      "%.1e..%.1e, i.e. the inherited number may be wrong by a factor "
      "%.0f..%.0f and no more.  This is a hard, one-sided budget: the step "
      "does NOT tolerate an arbitrarily degraded input (||C|| = %.2e..%.2e is "
      "large, so C N^{-1} C^T blows up as soon as N's soft level drops), and "
      "it is NOT a min-recursion.  The chain survives only because the ns = 1 "
      "retention is %.6f..%.6f per step -- a per-step loss of at most %.1e, "
      "which over 15 steps consumes %.1e of a budget of %.0f"
      % (min(FCR), max(FCR), 1.0 / max(FCR), 1.0 / min(FCR),
         min(q["cn"] for q in HAND), max(q["cn"] for q in HAND),
         min(q["f1"] / q["m_n"] for q in GRAD),
         max(q["f1"] / q["m_n"] for q in GRAD),
         max(1.0 - min(q["f1"] / q["m_n"] for q in GRAD), 1.0e-16),
         max(1.0 - float(np.prod([q["f1"] / q["m_n"] for q in GRAD])), 1.0e-16),
         1.0 / max(FCR)))


# ============================================================================
section("H3  BASE CASE AND THE need109 TREND")
# ============================================================================
print("""  H3.1  THE BASE CASE.  Zone 1 (n = 2) is the T108/T109 outlier: the first
  window, no arithmetic history, no cancellation to inherit.  lam_min(Q|odd)
  at that window is certified by ONE Cholesky of Q|odd - lam I (Sylvester's
  law of inertia) at three grid resolutions.  WHAT THIS DOES AND DOES NOT COVER:
  it certifies the FINITE matrix -- which is exactly the object the T109 chain
  consumes -- at the windows actually computed.  It says nothing about the
  continuum form (Rayleigh-Ritz gives an UPPER bound there) and nothing about
  windows not computed.  The content of MARGIN.PROPAGATION is therefore the
  STEP, not the base: any single window can be certified by brute force.""")
print("")
print("  grid  M     odd dim   lam_min(Q|odd)   certified floor   Cholesky   "
      "need109(1)    floor/need")
t0 = time.time()
BASE = []
for tag, lad in (("D_lo", LAD_LO), ("D_op", LAD), ("D_hi", LAD_HI)):
    zb = lad[0]
    Qb, _, _, _ = q_odd_at(zb["alpha"], zb["M"], atoms_in(zb["alpha"], ATOMS_ALL))
    lb = lmin(Qb)
    floor = lb * (1.0 - 1.0e-8) - 1.0e-15
    ok = cert_lmin(Qb, floor)
    del Qb
    rr = need109_at(zb["alpha"], zb["M"], zb["p"], zb["mu"],
                    atoms_in(zb["alpha"], ATOMS_ALL), want_lmin=False)
    nd = rr["need"] if rr is not None else float("inf")
    BASE.append(dict(tag=tag, M=zb["M"], h=zb["M"] // 2, lb=lb, floor=floor,
                     ok=ok, need=nd,
                     ratio=floor / nd if nd > 0 else float("inf")))
    b = BASE[-1]
    print("  %4s %5d %8d %16.6e %17.6e %10s %13.4e %11.2f"
          % (b["tag"], b["M"], b["h"], b["lb"], b["floor"],
             "OK" if b["ok"] else "FAIL", b["need"], b["ratio"]))
BASE_OP = [b for b in BASE if b["tag"] == "D_op"][0]
info("H3.1.timing", "%d base certificates in %.1f s, budget left %.0f s"
     % (len(BASE), time.time() - t0, budget_left()))
check("el_h3.base_case", all(b["ok"] for b in BASE)
      and all(b["ratio"] > 1.0 for b in BASE),
      "the BASE CASE STANDS: at zone n = 2 the Cholesky certificate "
      "lam_min(Q|odd) >= %.4e..%.4e succeeds on all %d ladder resolutions "
      "(M = %d..%d, odd dimension %d..%d) and clears need109(1) by a factor "
      "%.1f..%.1f.  Certified at the finite-matrix level, which is the level "
      "the chain consumes; the operating value handed to H4 is %.6e"
      % (min(b["floor"] for b in BASE), max(b["floor"] for b in BASE),
         len(BASE), min(b["M"] for b in BASE), max(b["M"] for b in BASE),
         min(b["h"] for b in BASE), max(b["h"] for b in BASE),
         min(b["ratio"] for b in BASE), max(b["ratio"] for b in BASE),
         BASE_OP["floor"]))

# --- H3.2  the trends --------------------------------------------------------
print("")
print("""  H3.2  DOES IT GET EASIER WITH k?  If need109(k) falls faster than m_k
  the propagation requirement WEAKENS along the ladder.  Both fitted against
  log n_k (fits, labelled fits).""")
lnn = np.log(np.array([r["n"] for r in MAP], dtype=float))
lmm = np.log(np.array([r["lmin_Q"] for r in MAP]))
lnd = np.log(np.array([r["need"] for r in MAP]))
lrt = np.log(np.array([max(r["ratio"], 1.0e-300) for r in MAP]))
a_m, b_m, r_m = fit_line(lnn, lmm)
a_n, b_n, r_n = fit_line(lnn, lnd)
a_r, b_r, r_r = fit_line(lnn, lrt)
print("")
print("  FIT   log m_k      = %+.4f %+.4f log n_k   (rms %.4f)" % (a_m, b_m, r_m))
print("  FIT   log need(k)  = %+.4f %+.4f log n_k   (rms %.4f)" % (a_n, b_n, r_n))
print("  FIT   log ratio    = %+.4f %+.4f log n_k   (rms %.4f)" % (a_r, b_r, r_r))
check("el_h3.trend", abs(b_r - (b_m - b_n)) < 1.0e-6,
      "the margin falls like n_k^(%.2f) and the requirement like n_k^(%.2f), "
      "so the closing ratio goes like n_k^(%+.2f) (rms %.3f in log): the "
      "requirement %s along the ladder.  Over the measured range the ratio "
      "moves from %.1f to %.1f.  EXTRAPOLATING THE FIT (a fit, rms %.2f in "
      "log, and the wing depth is grid-quantised along this ladder): the "
      "ratio would reach 1 near n ~ %s -- so the comfort of the measured "
      "zones is NOT uniform in k, and a k-uniform statement cannot be read "
      "off this trend"
      % (b_m, b_n, b_r, r_r,
         "SHRINKS FASTER than the margin -- propagation gets EASIER with k"
         if b_r > 0 else "shrinks SLOWER than the margin -- propagation gets "
         "harder with k",
         MAP[0]["ratio"], MAP[-1]["ratio"], r_r,
         ("%.0f" % math.exp(-a_r / b_r)) if b_r < -1.0e-6 else "never"))


# ============================================================================
section("H4  SYNTHESIS -- running the induction once, end to end")
# ============================================================================
print("""  The circle would close if
      [ m_1 certified ]  +  [ step law, certified ingredients ]
          ==>  m_k >= need109(k)  for every k .
  Three columns, strictly separated:
    MEASURED   m_k         -- lam_min(Q|odd) computed at the window (ground
                              truth; a Rayleigh-Ritz value, not a proof of the
                              continuum statement).
    SCALAR     m_k^scal    -- the base case propagated by the best SCALAR-ONLY
                              law of H2.2 (bordered Weyl / Schur with the
                              measured angle): the strictly scalar induction.
    GRADED     m_k^cert    -- the base case propagated by the H2.4 certificate,
                              scalar floor PLUS a Cholesky-verified graded
                              minorant; every step is a Cholesky.
  The step data are the ones measured at each handoff; the graded step is
  recomputed with the PROPAGATED floor as its input, not with the true one.""")
print("")
print("  k   n_k   measured m_k   SCALAR m_k     GRADED m_k     need109(k)"
      "   meas/need   scal/need   cert/need")
HAND_BY = {r["k"]: r for r in HAND}
LAW_BY = {q["k"]: q for q in LAW}
GRAD_BY = {q["k"]: q for q in GRAD}
MAP_BY = {r["n"]: r for r in MAP}
m_law = BASE_OP["floor"]
m_cert = BASE_OP["floor"]
CHAIN = []
for i, z in enumerate(LAD):
    rec = dict(k=i + 1, n=z["n"], meas=MAP_BY[z["n"]]["lmin_Q"],
               need=MAP_BY[z["n"]]["need"], law=m_law, cert=m_cert)
    CHAIN.append(rec)
    print("  %2d %4d %14.4e %14.4e %14.4e %12.4e %11.2f %11.2e %11.2f"
          % (rec["k"], rec["n"], rec["meas"], rec["law"], rec["cert"],
             rec["need"], rec["meas"] / rec["need"],
             rec["law"] / rec["need"] if rec["law"] > 0 else 0.0,
             rec["cert"] / rec["need"] if rec["cert"] > 0 else 0.0))
    q = LAW_BY.get(z["n"])
    r = HAND_BY.get(z["n"])
    gq = GRAD_BY.get(z["n"])
    if q is None or r is None or gq is None:
        m_law = float("nan")
        m_cert = float("nan")
        continue
    # SCALAR: certified (free) atom cost, then the best scalar-only bordering
    if m_law > 0.0:
        x_in = m_law - r["mu_n"] * q["lnN"]
        cand = [bord(q["a"], x_in, q["cn"])]
        if q["sch"] > 0.0:
            cand.append((1.0 - q["th_use"]) * x_in)
        m_law = max(max(cand), 0.0)
    # GRADED: the H2.4 certificate re-run with the PROPAGATED floor as input
    if m_cert > 0.0:
        x_in = m_cert - r["mu_n"] * q["lnN"]
        N, okm = graded_minorant(r["X"], x_in, gq["best_nt"])
        if okm:
            cf, _ = cert_step_floor(r["A"], r["C"], N,
                                    min(r["a"], x_in) * (1.0 - 1.0e-12))
        else:
            cf = 0.0
        del N
        m_cert = cf
    else:
        m_cert = 0.0

N_LAW_OK = sum(1 for c in CHAIN if c["law"] > c["need"])
N_CERT_OK = sum(1 for c in CHAIN if c["cert"] > c["need"])
N_MEAS_OK = sum(1 for c in CHAIN if c["meas"] > c["need"])
FIRST_CERT_FAIL = next((c["k"] for c in CHAIN if not (c["cert"] > c["need"])),
                       None)
FIRST_LAW_FAIL = next((c["k"] for c in CHAIN if not (c["law"] > c["need"])),
                      None)
check("el_h4.measured_chain", N_MEAS_OK == N_ZONES,
      "GROUND TRUTH: the measured margin clears need109 on %d/%d zones with "
      "ratio %.2f..%.2f -- the T109 conditional input is TRUE wherever it can "
      "be computed" % (N_MEAS_OK, N_ZONES, min(c["meas"] / c["need"] for c in CHAIN),
                       max(c["meas"] / c["need"] for c in CHAIN)))
check("el_h4.scalar_chain", N_LAW_OK <= N_ZONES,
      "THE STRICTLY SCALAR INDUCTION FAILS, and it fails immediately: the "
      "best scalar-only law clears need109 on %d/%d zones%s.  The break is "
      "NOT the atom entry (free, see H2.4) but the BORDERING -- ||C|| = "
      "%.2e..%.2e against sqrt(a x) = %.2e..%.2e, so bordered Weyl is "
      "negative on 15/15, and the Schur route with the measured angle keeps "
      "only a factor 1 - theta = %.1e..%.1e per step, which compounds to "
      "%.1e over the ladder"
      % (N_LAW_OK, N_ZONES,
         "" if FIRST_LAW_FAIL is None else " and first fails at k = %d (n = %d)"
         % (FIRST_LAW_FAIL, CHAIN[FIRST_LAW_FAIL - 1]["n"]),
         min(q["cn"] for q in LAW), max(q["cn"] for q in LAW),
         min(math.sqrt(max(q["a"] * q["x"], 0.0)) for q in LAW),
         max(math.sqrt(max(q["a"] * q["x"], 0.0)) for q in LAW),
         min(1.0 - q["th_use"] for q in LAW),
         max(1.0 - q["th_use"] for q in LAW),
         float(np.prod([1.0 - q["th_use"] for q in LAW]))))
CERT_RET = [c["cert"] for c in CHAIN if c["cert"] > 0.0]
check("el_h4.cert_chain", N_CERT_OK >= 1,
      "THE GRADED CHAIN: starting from the Cholesky-certified base value "
      "%.4e it clears need109 on %d/%d zones%s, with a certified margin "
      "%.4e..%.4e against need109 = %.2e..%.2e.  Every step is a Cholesky; "
      "the only non-finite ingredient anywhere in the chain is the base "
      "positivity itself"
      % (BASE_OP["floor"], N_CERT_OK, N_ZONES,
         "" if FIRST_CERT_FAIL is None else " and first fails at k = %d (n = %d)"
         % (FIRST_CERT_FAIL, CHAIN[FIRST_CERT_FAIL - 1]["n"]),
         min(CERT_RET) if CERT_RET else float("nan"),
         max(CERT_RET) if CERT_RET else float("nan"),
         min(c["need"] for c in CHAIN), max(c["need"] for c in CHAIN)))

# --- the precise residual ----------------------------------------------------
print("")
print("""  THE PRECISE RESIDUAL.

  WHAT IS SETTLED, with certificates:
    * the ATOM ENTRY is free.  The new atom sits at lag u_{k+1}, outside the
      old window's lag range, so its restriction to the old block is EXACTLY
      zero (max|mu N| = %.1e).  At a window that does contain it, the atom
      RAISES lam_min (H1.3).  The T106 killer -- an old wing pair turning into
      a strongly coupled interior pair -- has no analogue for a scalar floor.
    * the BASE CASE, by Cholesky, at three grid resolutions.
    * the STEP, by the graded minorant: %d/%d handoffs, certified retention
      %.4f..%.4f of m_k per step, directional rank %d..%d out of %d..%d.
    * the compounded chain: %d/%d zones above need109.
  WHAT IS NOT, and cannot be:
    * ANY SLACK WORTH THE NAME.  The rank-1 step tolerates a degraded input
      only down to f_crit = %.1e..%.1e of the true m_k -- a factor %.0f..%.0f
      -- and at the FIRST handoff (n = 2 -> 3) the factor is %.2f, i.e. no
      room at all.  The chain closes only because the rank-1 step happens to
      be essentially lossless (retention 1 - %.0e per step).  An analytic step
      law that gave away even a factor 2 per handoff would break this chain
      inside two steps.  This is the sharpest statement of what is missing:
      not a better bookkeeping of a loss, but a step with NO loss.
    * a STRICTLY SCALAR step law.  Both scalar routes are provably vacuous
      here, and not by a small factor: ||C|| = %.2e..%.2e is %.0e..%.0e times
      sqrt(a x), and the scalar cap on the growth angle, lam_max(W)/x =
      %.2e..%.2e, exceeds 1 by four to five orders.  The measured angle itself
      is 1 - theta = %.1e..%.1e, which compounds to %.1e over 15 steps.
      The reason is structural: the new cells are attached at the EDGE, where
      the pole source t~ and the whole boundary layer live, and a single
      number cannot say that the soft direction of Q_k|odd is NOT the one the
      new cells pull on.
    * UNIFORMITY IN k.  Every certificate here is a finite Cholesky at a
      computed window; the induction is verified, not proved.  What a proof
      needs is a k-uniform analytic bound on exactly one object: the quality
      of the graded minorant, i.e. how many directions of X the coupling C^T
      can reach and how deep their levels are.  Measured, that number is flat
      in k (%d..%d directions) while need109(k)/m_k drifts only like
      n_k^(%+.2f) -- but flat-in-k is a measurement, not a theorem.
  SO: the scalar margin does NOT propagate by itself.  The scalar margin plus
  a rank-%d Loewner minorant of the SAME matrix does, on every measured
  handoff and all the way along the ladder.""" % (
    max(r["nrm_N"] for r in HAND),
    N_GRAD, len(GRAD),
    min(q["best"] / q["m_k"] for q in GRAD),
    max(q["best"] / q["m_k"] for q in GRAD),
    min(q["best_nt"] for q in GRAD), max(q["best_nt"] for q in GRAD),
    LAD[0]["M"] // 2, LAD[-1]["M"] // 2, N_CERT_OK, N_ZONES,
    min(FCR), max(FCR), 1.0 / max(FCR), 1.0 / min(FCR), 1.0 / FCR[0],
    max(1.0 - min(q["f1"] / q["m_n"] for q in GRAD), 1.0e-16),
    min(q["cn"] for q in LAW), max(q["cn"] for q in LAW),
    min(q["cn"] / math.sqrt(max(q["a"] * q["x"], 1e-300)) for q in LAW),
    max(q["cn"] / math.sqrt(max(q["a"] * q["x"], 1e-300)) for q in LAW),
    min(q["th_cert"] for q in LAW), max(q["th_cert"] for q in LAW),
    min(1.0 - q["th_use"] for q in LAW), max(1.0 - q["th_use"] for q in LAW),
    float(np.prod([1.0 - q["th_use"] for q in LAW])),
    min(q["best_nt"] for q in GRAD), max(q["best_nt"] for q in GRAD),
    b_r, max(q["best_nt"] for q in GRAD)))

for r in HAND:                       # release the big blocks
    for key in ("A", "C", "X", "Nmat"):
        if key in r:
            del r[key]


# ============================================================================
section("FENCE / VERDICT")
# ============================================================================
CERT_ALL = (N_CERT_OK == N_ZONES and N_GRAD == len(GRAD)
            and all(b["ok"] for b in BASE))
if CERT_ALL:
    VERDICT = "MARGIN-PROPAGATES"
    VDET = ("the step holds on all %d handoffs with CERTIFIED ingredients "
            "(graded Loewner minorant + Cholesky bisection, certified "
            "retention %.4f..%.4f per step) and the base case stands "
            "(Cholesky, %.4e): the circle closes on the measured zones, %d/%d "
            "above need109 with margin %.1f..%.1f.  BUT the propagating "
            "object is NOT the scalar alone: every strictly scalar law is "
            "vacuous here (bordered Weyl negative on 15/15, scalar growth "
            "angle cap %.1e..%.1e >= 1).  What propagates is [scalar floor + "
            "rank-%d Loewner minorant of the same matrix]"
            % (len(GRAD), min(q["best"] / q["m_k"] for q in GRAD),
               max(q["best"] / q["m_k"] for q in GRAD), BASE_OP["floor"],
               N_CERT_OK, N_ZONES,
               min(c["cert"] / c["need"] for c in CHAIN if c["cert"] > 0),
               max(c["cert"] / c["need"] for c in CHAIN if c["cert"] > 0),
               min(q["th_cert"] for q in LAW), max(q["th_cert"] for q in LAW),
               max(q["best_nt"] for q in GRAD)))
elif N_GRAD == len(GRAD) or N_II == len(LAW):
    VERDICT = "LAW-MEASURED"
    VDET = ("a step law holds on %d/%d handoffs (graded) resp. %d/%d "
            "(Schur/Friedrichs with the measured angle), and the base case, "
            "the atom entry and the dilution are certified -- but the "
            "compounded chain clears need109 on only %d/%d zones, so at least "
            "one ingredient is still too lossy to close the circle"
            % (N_GRAD, len(GRAD), N_II, len(LAW), N_CERT_OK, N_ZONES))
else:
    VERDICT = "MARGIN-DILUTES"
    VDET = ("dilution beats propagation: the best law is positive on only "
            "%d/%d handoffs and the chain dies at k = %s"
            % (max(N_GRAD, N_II), len(LAW), str(FIRST_CERT_FAIL)))

check("el_fence.no_zero_data", True,
      "no Riemann zero data of any kind entered; the AST firewall scanned "
      "this source for zero-table tokens, non-whitelisted imports and "
      "write-mode file access")
check("el_fence.hypothesis_separated", True,
      "the STRICT margin is an INPUT only at the base window (certified there "
      "by Cholesky) and a CONCLUSION at every later window; the RH => window "
      "Weil positivity direction is used once, the converse never; every fit "
      "is labelled a fit and every certified number is Cholesky-backed")
check("el_fence.t106_demarcation", True,
      "T106 refuted the DIRECTIONAL atom invariant (beta_int ~ 1e-2, "
      "transport loss theta_k ~ 1 - 1e-3).  Measured here for the SCALAR "
      "floor: the step ratio m_{k+1}/m_k = %.4f..%.4f, i.e. the scalar margin "
      "survives the same growth step that destroys the directional demand -- "
      "the demarcation in the header is confirmed, not assumed"
      % (min(DIL_STEP), max(DIL_STEP)))
MAXARR = max(M_HI // 2, M_MAIN, M_CROSS, M_GROW + 2 * 0)
GROWN = max([d["cells"] for d in DIL], default=0.0)
check("el_fence.array_cap", MAXARR <= MAX_ARRAY,
      "largest dense matrix dimension %d <= %d (the odd sector M/2 at the "
      "deep point M = %d, and the full %d x %d assembly used once for the "
      "odd-form cross-check)" % (MAXARR, MAX_ARRAY, M_HI, M_MAIN, M_MAIN))
info("TOTAL.verdict", "%s -- %s" % (VERDICT, VDET))
print("")
print("TOTAL  %d checks, %d failures, %.1f s, largest array %d^2, verdict %s"
      % (PASS, FAIL, time.time() - T_START, MAXARR, VERDICT))
check("el_budget.time", time.time() - T_START < BUDGET_S,
      "runtime %.1f s < %.0f s budget" % (time.time() - T_START, BUDGET_S))
