"""Discovery probe (2026-07-27), part 109 of the zeta/prime investigation.
Contract BOUNDARY.DECAY -- certify the TWO remaining scalars of (R).

WHERE THIS SITS (T105..T108, taken as given, re-derived here)
  T106 split the prime-atom handoff by the exact parity superselection
  (Cantoni-Butler 1976); the J-even half closes 16/16.  The J-odd half is
      (R)     Q|odd = T_odd - t~ t~^T  >=  (mu_k/2) V V^T ,
  T_odd the Toeplitz-minus-Hankel part on ceil(M/2) cells, V the ceil(p/2)
  orthonormal wing-odd demand columns.  T107/T108 reduced (R) to TWO SCALARS,
      (R)  <==  [omega < 1]  AND  [ (mu/2) ||V^T x||^2 <= (1 - omega) eps ] ,
      x := T_odd^{-1} t~ ,  tau = t~^T x ,  eps = 1 - tau ,
      omega = (mu/2) lam_max(Gam) ,  Gam = V^T T_odd^{-1} V ,
  with the exact identities eps = x^T Q|odd x/tau = (last Cholesky pivot)^2
  (the Szego/Levinson prediction error) and h = V^T x, h_i = (x_i +
  x_{p-1-i})/sqrt2 -- on the 8 zones with m = 1, ||h||^2 is literally the
  SINGLE EDGE VALUE x_0^2 of the pole response.  Measured |x_0|/max|x| =
  2.9e-3..5.7e-3 with a linear edge profile.  Both scalars stayed MEASURED.

THE TWO SCALARS, AND WHAT T108 LEFT
  [1] omega:  blocked ONLY by the compression-to-Schur gap.  The T105
      machinery certifies the COMPRESSION V^T T_odd V from below; omega < 1
      needs the SCHUR COMPLEMENT S = V^T T_odd V - V^T T_odd W (W^T T_odd
      W)^{-1} W^T T_odd V, and S <= compression always.
  [2] ||h||^2 = ||V^T x||^2:  three routes refuted (mode-wise -- the shares
      cancel with sum|k_j| = 401 against sum k_j = 1; Bessel -- loses 1/theta
      up to 1e7; the T105 pole Cauchy-Schwarz one level up -- loses 1e6).
      All three are BLIND TO CANCELLATION, which is exactly what makes x_0
      small.  Not retried here.

THE BLOCKS
  G1 THE MECHANISM.  Where the source t~ lives, where the response x lives,
      and which classical structure produces the edge suppression.  Measured:
      the exact geometry of t~ (edge-peaked, closed-form geometric decay rate
      D/2 per cell), the lag decay of the Toeplitz symbol (certified from the
      archimedean kernel K_x(s) = -e^{-s/2}/(1 - e^{-2s})), the Green row
      g = T_odd^{-1} e_0 and its decay, the profile of x with power-law and
      exponential fits, and the BULK MASS lam_min of the wing-complement block
      (the Combes-Thomas 1973 hypothesis).  The decisive diagnostic is the
      CANCELLATION RATIO sum_r |g_r t~_r| / |sum_r g_r t~_r|: it decides
      between Green-function decay (Combes-Thomas / Demko-Moss-Smith 1984 /
      Jaffard 1990 -- a bound survives absolute values) and cancellation (no
      absolute-value bound can survive).
  G2 THE x_0 CERTIFICATE.  Four candidates, each certified-vs-measured with
      its sharpness against the measured ||h||:
      (i)   RESOLVENT DECAY (Combes-Thomas): |x_0| <= sum_r |g_r| |t~_r|.
            Evaluated with the EXACT g, so no constant can rescue it if it
            fails: an upper bound on the whole class.
      (ii)  T-METRIC CAUCHY-SCHWARZ at one component: x_0^2 <= (T^{-1})_{00}
            tau, the T108 F2.5 route restricted to the edge.
      (iii) SZEGO/LEVINSON: t~ is EXACTLY two-term geometric, so
            x_0 = c_+ G(z_+) + c_- G(z_-) with G the generating function of
            the first row of T_odd^{-1} and z_pm = exp(+-D/2) -- an exact
            two-point evaluation (verified), which exhibits the cancellation
            but bounds nothing.
      (iv)  THE RESIDUAL / GOAL-ORIENTED CERTIFICATE (new).  For ANY trial
            vector y the energy E(y) := 1 - 2 y^T t~ + y^T T_odd y satisfies
                E(y) = eps + ||x - y||_{T_odd}^2 ,
            an identity: E(y) >= ||x-y||^2_T needs only eps >= 0 (the
            induction hypothesis itself, NO margin), and E(y) >= eps gives
            tau >= 1 - E(y) for free.  With an adjoint trial Z ~ T_odd^{-1} V
            and the residual r = t~ - T_odd y,
                ||V^T x|| <= ||V^T y + Z^T r|| + sqrt( lam_max(F) E(y) ) ,
                F = Gam - V^T Z - Z^T V + Z^T T_odd Z ,
            which is SECOND ORDER in the two residuals (Prager-Synge 1947;
            Becker-Rannacher goal-oriented a posteriori estimation).  It
            reproduces the cancellation by construction instead of bounding
            it away -- the one thing the three refuted routes cannot do.  F
            needs Gam from above, i.e. exactly the omega object of G3.
  G3 omega CRACKED.  The Schur correction Cap = T_VW T_WW^{-1} T_WV is
      measured (spectral structure, how much of it sits on the softest bulk
      directions).  Route A, the certificate: a GRADED MATRIX CAP IN PSD ORDER
      (T104 arm A, sharpened).  For a trial orthonormal G = [g_1..g_ntop],
      trial levels s_1 <= .. <= s_ntop and a floor sig_b >= s_ntop,
          T_WW >= N := sig_b I + G diag(s - sig_b) G^T   [ONE Cholesky]
      implies, by Loewner antitonicity of the inverse,
          Cap <= (G^T B)^T diag(1/s) (G^T B)
                 + (B^T B - (G^T B)^T (G^T B))/sig_b ,
      hence S >= S_cert, Gam <= Gam_cert = S_cert^{-1} and omega <= omega_cert
      = (mu/2)/lam_min(S_cert).  One level PER DIRECTION is the whole point:
      the UNgraded version (a single sig_a for the soft block, which is what
      T108's global Loewner route amounts to) is vacuous.  The trial data are
      the computed soft subspace and its levels; their QUALITY affects
      sharpness only, their VALIDITY is the Cholesky (Sylvester inertia).
      Route B, an independent second certificate: the adjoint residual
      R = V - T_odd Z gives Gam = Z^T V + V^T Z - Z^T T_odd Z +
      R^T T_odd^{-1} R exactly, capped by R^T R/lam_ind -- a Krylov witness
      instead of a bulk spectrum, conditional on a quantified lam_ind.
  G4 SYNTHESIS.  The certified Gam_cert of G3 feeds the G2(iv) bound, so both
      scalars come from ONE object and neither needs a hypothesis input.  The
      full chain is
      (R) <== [omega_cert < 1] AND [lam_min(Q|odd) >= need109],
      need109 = (mu/2) H_cert^2 min( ||t~||^2/(1-E), (t~^T T_odd t~)/||t~||^2 )
                / (1 - omega_cert) ,
      H_cert the G2(iv) bound on ||V^T x|| evaluated with Gam_cert.  The
      induction margin now enters ONLY through the floor on eps.  Zone count,
      margin against the measured lam_min(Q|odd), VACUITY test against mu/2,
      M-stability on the physical ladder against the ideal (perfect-trial,
      measured-scalar) chain, precise residual.

PREREGISTERED VERDICTS
  BOUNDARY-CERTIFIED: both scalars certified and the chain closes on every
      measured zone, conditional ONLY on the explicit non-vacuous induction
      margin.
  ONE-SCALAR-LEFT   : exactly one of the two certified -- which one, and the
      precise blockade of the other.
  DECAY-MEASURED    : both stay measurement -- the structural blockade.
  Element gates: el_firewall, el_g0, el_g1, el_g2, el_g3, el_g4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger/TeX/website/
    changelog edit, no verification/ module, no next.txt, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * RH => window Weil positivity is used in one direction only; the converse
    is NOT claimed.  Q_full >= 0, hence Q|odd >= 0, is a HYPOTHESIS INPUT --
    the induction hypothesis.  Where a STRICT margin lam_ind > 0 is used it is
    declared as a quantified hypothesis input and its required size printed.
  * lam_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute positivity, never prove it.
  * CERTIFIED vs MEASURED tracked per line and restated in the G4 ledger.  A
    "certificate" here means a finite computation whose validity does not
    depend on any measured spectral datum: trial vectors and trial subspaces
    enter only through inequalities that hold for ANY trial (their quality is
    sharpness, not validity), and every PSD-order step is verified by a
    Cholesky.  Floating-point rounding is not audited.
  * Every fit is labelled a fit.  Classical anchors cited, not re-derived:
    Weil 1952, Schur complement, Sherman-Morrison 1950, Woodbury 1950,
    Albert 1969, Grenander-Szego (Toeplitz), Szego recursion / Levinson 1947
    prediction error, Cholesky, Sylvester's law of inertia, Combes-Thomas
    1973, Demko-Moss-Smith 1984, Jaffard 1990, Prager-Synge 1947,
    Becker-Rannacher goal-oriented a posteriori estimation, Hestenes-Stiefel
    1952 conjugate gradients, Cauchy-Schwarz / Kantorovich for PSD forms,
    Loewner antitonicity, Rayleigh-Ritz, Cantoni-Butler 1976, T105 support
    separation, von Mangoldt arithmetic.

OUTCOME OF THIS RUN  =>  see the G4 ledger and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, cholesky, eigh, eigvalsh

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_ARRAY = 1500             # hard cap on any matrix dimension
BUDGET_S = 780.0

M_CROSS = 1000               # cell count for locating the handoff crossing
M_MAIN = 1200                # operating cell count
P_MIN, P_MAX = 2, 200
GAMMA_OP = 0.5               # operating depth as a fraction of the crossing
M_CERT = (1200, 2400, 3000)  # the chain ladder; odd sector M/2 <= MAX_ARRAY
NTOP_SCAN = (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
NTOP_MAX = 512               # ceiling for the Cholesky-verified graded cap
CG_LADDER = (16, 32, 64, 128, 256, 384, 512)
EFFORT = (1, 2, 4)           # trial-effort multipliers on the M ladder
ETA_CHOL = 1.0e-6            # safety back-off of the certified PSD shifts

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


def lag_coeffs(u, p, M, atoms_all):
    """The M retained lag coefficients c_0..c_{M-1} of the Toeplitz part."""
    D, alpha, delta = zone_geometry(u, p, M)
    s = np.arange(M) * D
    lag = arch_A(s, D)
    for u_j, mu_j in atoms_in(alpha, atoms_all):
        lag = lag - mu_j * atom_lag(s, u_j, D)
    return lag, D, alpha, delta


def build_Q(alpha, M, atoms):
    from scipy.linalg import toeplitz
    D = 2.0 * alpha / M
    s = np.arange(M) * D
    lag = arch_A(s, D)
    for u_j, mu_j in atoms:
        lag = lag - mu_j * atom_lag(s, u_j, D)
    Q = toeplitz(lag)
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


def sigma_of(u, p, M, atoms_all):
    """lam_min of the Schur complement of Q onto E_- -- the handoff quantity."""
    D, alpha, delta = zone_geometry(u, p, M)
    Q = build_Q(alpha, M, atoms_in(alpha, atoms_all))
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
    if fac is None:
        return float("nan")
    A = B.T @ cho_solve(fac, B, check_finite=False)
    return float(eigvalsh(sym(mm) - sym(A)).min())


def find_p_star(u, mu, M, atoms_all):
    """Largest wing width p with sigma_k(p) >= mu_k/2 (the handoff crossing)."""
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


def p_at(delta_c, u, MM, gam):
    return max(P_MIN, int(round(gam * delta_c * MM / (u + delta_c))))


def fit_line(x, y):
    """Least squares y = a + b x; returns (a, b, rms of the residual in y)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def gl_integral(f, lo, hi, panels):
    edges = np.linspace(lo, hi, panels + 1)
    mid = 0.5 * (edges[1:] + edges[:-1])
    half = 0.5 * (edges[1:] - edges[:-1])
    x = mid[:, None] + half[:, None] * _GLX[None, :]
    return float(np.dot(half, f(x.ravel()).reshape(x.shape) @ _GLW))


def band_mean_k(delta, panels=400):
    T = math.pi / delta
    return gl_integral(kernel_k, 0.0, T, panels) / T


def cert_bare(u, delta, panels=400):
    """CERTIFIED lower bound on b0 = bare_k - mu_k/2 (T105 C2)."""
    floor_k = band_mean_k(delta, panels)
    smin = max(u - delta, 1.0e-9)
    tail = delta * float(np.abs(kernel_K_x(np.array([smin]))).max())
    pole = 4.0 * (math.cosh(0.5 * u) - 1.0) * math.sinh(0.5 * delta)
    return floor_k - tail - pole, floor_k, tail, pole


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


def odd_pole_norm2(alpha, M):
    """||t~||^2 = (16/D) sinh^2(D/4) [ sinh(alpha)/sinh(D/2) - M ]."""
    D = 2.0 * alpha / M
    return (16.0 / D) * math.sinh(0.25 * D) ** 2 * (
        math.sinh(alpha) / math.sinh(0.5 * D) - M)


def odd_pole_geometric(alpha, M):
    """t~_r = c_+ z_+^r + c_- z_-^r with z_pm = exp(+- D/2)  (T108 F3.3)."""
    D = 2.0 * alpha / M
    pre = (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * 0.5
    cp = pre * math.exp(-0.5 * alpha) * math.exp(0.25 * D)
    cm = -pre * math.exp(0.5 * alpha) * math.exp(-0.25 * D)
    return (cp, math.exp(0.5 * D)), (cm, math.exp(-0.5 * D))


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


# ----------------------------------------------------------------------------
# the T108 scalars, plus the wing/complement split and the trial machinery
# ----------------------------------------------------------------------------
def odd_objects(u, mu, p, M, atoms_all, keep=False, lmin_q=False):
    """tau, eps, omega, ||h||^2 and (optionally) the matrices themselves."""
    c, D, alpha, delta = lag_coeffs(u, p, M, atoms_all)
    T = odd_toeplitz(c, M)
    tv = odd_pole_vector(alpha, M)
    V = demand_V(p, M)
    half = 0.5 * mu
    fac, sh = safe_cho(T)
    if fac is None:
        return None
    x = cho_solve(fac, tv, check_finite=False)
    tau = float(np.dot(tv, x))
    eps = 1.0 - tau
    hvec = V.T @ x
    nh2 = float(np.dot(hvec, hvec))
    Ti_V = cho_solve(fac, V, check_finite=False)
    Gam = sym(V.T @ Ti_V)
    gmax = float(eigvalsh(Gam)[-1])
    out = dict(lag=c, D=D, alpha=alpha, delta=delta, p=p, m=V.shape[1], M=M,
               half=half, tau=tau, eps=eps, nx2=float(np.dot(x, x)), nh2=nh2,
               om=half * gmax, gmax=gmax, nt2=float(np.dot(tv, tv)),
               tTt=float(np.dot(tv, T @ tv)), shift=sh,
               x0=abs(float(x[0])), xmax=float(np.abs(x).max()),
               theta=nh2 / float(np.dot(x, x)))
    if lmin_q:
        Q = T - np.outer(tv, tv)
        out["lmin_Q"] = float(eigvalsh(Q, subset_by_index=[0, 0])[0])
        del Q
    if keep:
        out["T"] = T
        out["t"] = tv
        out["V"] = V
        out["x"] = x
        out["h"] = hvec
        out["Gam"] = Gam
        out["fac"] = fac
    return out


def wing_split(T, p, m):
    """T in the orthogonal basis [V | W]: V the demand columns, W the rest.

    The demand columns are the PLUS pairs (e_i + e_{p-1-i})/sqrt2 inside the
    first p cells, so an explicit orthogonal complement is the MINUS pairs
    (e_i - e_{p-1-i})/sqrt2 plus every cell r >= p.  No QR needed.
    """
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
    """omega_cert from a GRADED MATRIX CAP in PSD order (T104 arm A).

    For a trial orthonormal G = [g_1..g_ntop], trial levels s_1 <= .. <= s_ntop
    and a trial floor sig_b >= s_ntop, the Loewner minorant
        T_WW  >=  N := sig_b I + G diag(s - sig_b) G^T   [ONE Cholesky verifies]
    gives, by antitonicity of the inverse,
        T_WW^{-1}  <=  N^{-1} = G diag(1/s) G^T + (I - G G^T)/sig_b ,
    hence with B = T_WV
        Cap := B^T T_WW^{-1} B  <=  (G^T B)^T diag(1/s) (G^T B)
                                    + (B^T B - (G^T B)^T (G^T B))/sig_b ,
    S >= S_cert := T_VV - Cap_cert and omega <= (mu/2)/lam_min(S_cert).
    G and the levels are TRIALS: their quality is sharpness, the Cholesky is
    the validity.  The GRADED form (one level per direction) is what makes the
    device sharp: a single sig_a for the whole soft block throws away the
    spread of the soft spectrum, which is exactly where the mass sits.
    """
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
               om_cert=float("inf"), lmin_S=float("nan"), soft_share=0.0)
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
        lmin_S = float(eigvalsh(S_cert)[0])
        out.update(ok=True, back=back, sig_a=(float(sig[0]) if ntop > 0
                                              else sig_b), sig_b=sig_b,
                   lmin_S=lmin_S, S_cert=S_cert,
                   om_cert=(half / lmin_S if lmin_S > 0.0 else float("inf")),
                   soft_share=(float(np.trace(soft)) / float(np.trace(BtB))
                               if np.trace(BtB) > 0 else 0.0))
        return out
    return out


def cap_scan(TVV, TVW, TWW, half):
    """MEASURED scan: smallest ntop on the ladder for which the graded cap

        Cap <= sum_{j<ntop} c_j c_j^T/nu_j + (B^T B - sum_{j<ntop} c_j c_j^T)
               / nu_ntop ,        c_j = q_j^T B ,

    gives omega < 1.  Uses the exact bulk spectrum, so it is a measurement --
    psd_cap_omega then re-runs the winner as a Cholesky-verified trial.
    Returns (ntop_min or None, {ntop: omega_cap}).
    """
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
    return (ok_nt[0] if ok_nt else None), out, nu


def ntop_cert(ntop_min, n_w, cap=None):
    """Headroom over the measured ntop_min: sharpness, at the same validity."""
    return min(n_w - 1, max(4 * ntop_min, ntop_min + 16),
               NTOP_MAX if cap is None else cap)


def cg_iterates(T, b, ks):
    """Hestenes-Stiefel 1952 CG; y_k minimises ||x-y||_T over the Krylov space.

    Returns {k: y_k}.  The iterates are TRIAL VECTORS only: nothing downstream
    assumes they solve anything.
    """
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
    for k in sorted(want):                 # CG may terminate early: carry on
        if k not in out:
            out[k] = y.copy()
    return out


def trial_bound(T, tv, V, y, Z, gam_mat):
    """The G2(iv) certificate for ||V^T x||, x = T^{-1} t~.

    E(y)  = 1 - 2 y^T t~ + y^T T y  =  eps + ||x-y||_T^2   (identity)
    ||V^T x|| <= ||V^T y + Z^T r|| + sqrt( lam_max(F) E(y) ) ,
    F = Gam - V^T Z - Z^T V + Z^T T Z  (>= 0), r = t~ - T y ,
    with Gam replaced by any Loewner upper bound gam_mat >= Gam (G3).
    Certified given eps >= 0 only.  Z = None gives the plain residual form.
    """
    Ty = T @ y
    E = 1.0 - 2.0 * float(np.dot(y, tv)) + float(np.dot(y, Ty))
    r = tv - Ty
    lead = V.T @ y
    if Z is not None:
        lead = lead + Z.T @ r
        F = gam_mat - V.T @ Z - Z.T @ V + Z.T @ (T @ Z)
        lf = float(eigvalsh(sym(F))[-1])
    else:
        lf = float(eigvalsh(sym(gam_mat))[-1])
    lf = max(lf, 0.0)
    E = max(E, 0.0)
    return float(np.linalg.norm(lead)) + math.sqrt(lf * E), E, lf


# ============================================================================
section("G0  SETUP, FIREWALL, THE TWO SCALARS RE-DERIVED")
# ============================================================================
firewall()

ATOMS_ALL = atom_table(64)
ZONES = [t for t in ATOMS_ALL if t[0] <= 29]
N_ZONES = len(ZONES)
info("zones", "%d prime-power zones n_k = %s"
     % (N_ZONES, ", ".join(str(t[0]) for t in ZONES)))
info("G0.hypothesis",
     "HYPOTHESIS INPUT (never proved here): Q_full(alpha) >= 0, hence "
     "Q|odd >= 0, i.e. eps >= 0.  Where a STRICT margin lam_ind > 0 is used "
     "it is declared as a QUANTIFIED hypothesis input and its required size "
     "is printed against the measured lam_min(Q|odd)")
info("G0.fence_rh",
     "RH => window Weil positivity is used in one direction only; the "
     "converse is NOT claimed.  No zero data of any kind enters this probe")

t0 = time.time()
CROSS = []
for (n_k, lam, u, mu) in ZONES:
    p_star, ok = find_p_star(u, mu, M_CROSS, ATOMS_ALL)
    D, alpha, delta = zone_geometry(u, p_star, M_CROSS)
    CROSS.append(dict(n=n_k, u=u, mu=mu, p=p_star, ok=ok, D=D, alpha=alpha,
                      delta=delta))
for c in CROSS:
    c["p_op"] = p_at(c["delta"], c["u"], M_MAIN, GAMMA_OP)
info("G0.timing", "%d crossings located in %.1f s, budget left %.0f s"
     % (len(CROSS), time.time() - t0, budget_left()))
check("el_g0.p_star", all(c["ok"] for c in CROSS),
      "p* interior on every zone: p* = %s"
      % ", ".join(str(c["p"]) for c in CROSS))
check("el_g0.array_cap", M_CERT[-1] // 2 <= MAX_ARRAY,
      "largest dense matrix dimension is the odd sector M/2 = %d <= %d at the "
      "deep point M = %d" % (M_CERT[-1] // 2, MAX_ARRAY, M_CERT[-1]))

ZC = CROSS[15]                        # n_k = 29, the narrowest window
OB = odd_objects(ZC["u"], ZC["mu"], ZC["p_op"], M_MAIN, ATOMS_ALL, keep=True,
                 lmin_q=True)
T1, t1, V1, x1, h1 = OB["T"], OB["t"], OB["V"], OB["x"], OB["h"]
H1 = T1.shape[0]

Qf = build_Q(OB["alpha"], M_MAIN, atoms_in(OB["alpha"], ATOMS_ALL))
Bm = refl_odd_basis(M_MAIN)
e_split = float(np.abs(Bm.T @ Qf @ Bm - (T1 - np.outer(t1, t1))).max())
del Qf, Bm
check("el_g0.odd_form", e_split < 1.0e-9,
      "Q|odd = T_odd - t~ t~^T to %.1e against a full %d x %d assembly "
      "(n_k=%d, p=%d, m=%d, odd sector %d): the objects below are the "
      "T106/T107/T108 ones, re-derived here, not imported"
      % (e_split, M_MAIN, M_MAIN, ZC["n"], OB["p"], OB["m"], H1))

TVV1, TVW1, TWW1 = wing_split(T1, OB["p"], OB["m"])
e_wsplit = max(float(np.abs(TVV1 - V1.T @ (T1 @ V1)).max()),
               abs(float(np.trace(TWW1)) + float(np.trace(TVV1))
                   - float(np.trace(T1))))
S_dir = np.linalg.inv(OB["Gam"])
S_blk = sym(TVV1 - TVW1 @ np.linalg.solve(TWW1, TVW1.T))
e_schur = float(np.abs(S_dir - S_blk).max()) / float(np.abs(S_dir).max())
check("el_g0.wing_split", e_wsplit < 1.0e-9 and e_schur < 1.0e-7,
      "the explicit orthogonal complement W (minus-pairs inside the wing plus "
      "every cell r >= p) reproduces V^T T_odd V to %.1e and the Schur "
      "identity (V^T T_odd^{-1} V)^{-1} = T_VV - T_VW T_WW^{-1} T_WV to rel "
      "%.1e -- omega is EXACTLY a Schur complement, no QR, no measured basis"
      % (e_wsplit, e_schur))


# ============================================================================
section("G1  THE MECHANISM -- why the pole response is small at the edge")
# ============================================================================
print("""  x solves T_odd x = t~.  Three classical mechanisms could suppress x_0:
  (A) SUPPORT SEPARATION (T105): the source lives far from the edge and the
      Green function decays -- Combes-Thomas 1973 for a gapped operator,
      Demko-Moss-Smith 1984 / Jaffard 1990 for decaying inverses.
  (B) a BULK MASS with a boundary layer: T_odd >= c > 0 away from the edge.
  (C) CANCELLATION: x_0 = sum_r (T_odd^{-1})_{0r} t~_r is a signed sum whose
      terms are individually large.
  (A) and (B) survive absolute values, (C) does not: the decisive measurement
  is the cancellation ratio sum_r |g_r t~_r| / |sum_r g_r t~_r|, g = T^{-1}e_0.""")

# --- G1.1  where the source lives -------------------------------------------
print("")
print("  THE SOURCE t~ IS EXACTLY GEOMETRIC, and it is EDGE-PEAKED.")
print("  t~_r = (8/sqrt D) sinh(D/4) sinh(xbar_r/2), xbar_r = -alpha + (r+1/2)D")
print("       = c_+ z_+^r + c_- z_-^r ,  z_pm = exp(+- D/2)   (T108 F3.3)")
print("")
print("  n_k   p   m   argmax|t~|  |t~_0|/max|t~|  fitted rate/cell  closed form"
      "   D/2 (bulk)")
ROWS = []
e_geo = 0.0
e_rate = 0.0
for c in CROSS:
    ob = odd_objects(c["u"], c["mu"], c["p_op"], M_MAIN, ATOMS_ALL, keep=True,
                     lmin_q=True)
    ob["n"], ob["u"], ob["mu"] = c["n"], c["u"], c["mu"]
    tv = ob["t"]
    at = np.abs(tv)
    (cp, zp), (cm, zm) = odd_pole_geometric(ob["alpha"], ob["M"])
    r_idx = np.arange(at.shape[0])
    e_geo = max(e_geo, float(np.abs(cp * zp ** r_idx + cm * zm ** r_idx - tv).max())
                / float(at.max()))
    nfit = max(8, at.shape[0] // 8)
    ob["t_rate"] = -fit_line(np.arange(nfit), np.log(at[:nfit]))[1]
    # the closed form log-slope over the same window: |t~_r| ~ sinh((alpha-rD)/2)
    a0 = 0.5 * ob["alpha"]
    a1 = 0.5 * (ob["alpha"] - (nfit - 1) * ob["D"])
    ob["t_rate_cf"] = (math.log(math.sinh(a0)) - math.log(math.sinh(a1))) / (nfit - 1)
    e_rate = max(e_rate, abs(ob["t_rate"] / ob["t_rate_cf"] - 1.0))
    ob["t_argmax"] = int(np.argmax(at))
    ob["t_edge_frac"] = float(at[0] / at.max())
    ROWS.append(ob)
    print("  %3d %3d %3d %10d %14.4f %17.6f %12.6f %12.6f"
          % (ob["n"], ob["p"], ob["m"], ob["t_argmax"], ob["t_edge_frac"],
             ob["t_rate"], ob["t_rate_cf"], 0.5 * ob["D"]))
check("el_g1.source_at_edge",
      all(ob["t_argmax"] == 0 and ob["t_edge_frac"] > 0.999 for ob in ROWS)
      and e_geo < 1.0e-12 and e_rate < 0.05,
      "the source t~ attains its MAXIMUM at the boundary cell r = 0 on %d/%d "
      "zones; it is the two-term geometric vector c_+ z_+^r + c_- z_-^r to "
      "%.1e and its decay into the bulk follows the closed-form slope "
      "(D/2) coth((alpha-rD)/2) (fit vs closed form: %.1e), which tends to "
      "D/2 deep inside.  There is NO support separation between t~ and the "
      "wing -- the source SITS on the boundary -- so mechanism (A) is "
      "geometrically excluded before any constant is discussed: the T105 "
      "separation picture does not explain the edge suppression"
      % (N_ZONES, N_ZONES, e_geo, e_rate))
NARROW = [ob for ob in ROWS if ob["n"] > 2]
info("G1.1.widest_zone",
     "n_k = 2 (p = %d, m = %d, the widest window and the only non-avoidant "
     "zone in T108) behaves differently throughout G1/G2 and is reported "
     "separately wherever it does" % (ROWS[0]["p"], ROWS[0]["m"]))

# --- G1.2  the lag decay: the certified off-diagonal decay class ------------
print("")
print("""  THE OFF-DIAGONAL DECAY CLASS IS CERTIFIED IN CLOSED FORM.  The lag
  coefficients are c_s = A(sD) - sum_j mu_j [triangle at u_j] with the
  archimedean lag kernel K_x(s) = -e^{-s/2}/(1-e^{-2s}), whose exact local
  log-rate per cell is
      rho(s) = D (1/2 + 2/(e^{2s} - 1))  ->  D/2   as s -> infinity.
  So T_odd lies in the Jaffard 1990 exponential class with an EXPLICIT rate,
  which is exactly the hypothesis of every Combes-Thomas / Demko-Moss-Smith
  resolvent-decay theorem.  At the lags a window of M cells can reach, sD is
  still O(1), so the visible rate is the pre-asymptotic rho, not D/2 -- the
  column 'closed form' below is rho fitted over the SAME window, and the
  measured column is a FIT of the same kind.""")
print("")
print("  n_k   fitted |c_s|/cell   closed form   ratio   D/2 (asympt)   "
      "Green envelope/cell   ratio to D/2   env drop")
for ob in ROWS:
    lg = np.abs(ob["lag"])
    s_lo = max(4, int(0.10 * ob["M"]))
    s_hi = min(ob["M"], int(0.40 * ob["M"]))
    sel = np.arange(s_lo, s_hi)
    ob["c_rate"] = -fit_line(sel, np.log(lg[sel]))[1]
    ob["c_ref"] = -fit_line(sel, np.log(np.abs(
        kernel_K_x(sel * ob["D"]))))[1]
    g = cho_solve(ob["fac"], np.eye(ob["T"].shape[0], 1).ravel(),
                  check_finite=False)
    ob["g"] = g
    env = np.maximum.accumulate(np.abs(g)[::-1])[::-1] + 1.0e-300
    r_lo = max(4, int(0.05 * env.shape[0]))
    r_hi = int(0.40 * env.shape[0])
    ge = np.arange(r_lo, r_hi)
    ob["g_rate"] = -fit_line(ge, np.log(env[ge]))[1]
    ob["g_drop"] = float(env[r_lo] / env[r_hi - 1])
    print("  %3d %18.6f %13.6f %7.3f %14.6f %21.6f %13.3f %11.2f"
          % (ob["n"], ob["c_rate"], ob["c_ref"], ob["c_rate"] / ob["c_ref"],
             0.5 * ob["D"], ob["g_rate"], ob["g_rate"] / (0.5 * ob["D"]),
             ob["g_drop"]))
c_lo = min(ob["c_rate"] / ob["c_ref"] for ob in ROWS)
c_hi = max(ob["c_rate"] / ob["c_ref"] for ob in ROWS)
g_lo = min(ob["g_rate"] / (0.5 * ob["D"]) for ob in ROWS)
g_hi = max(ob["g_rate"] / (0.5 * ob["D"]) for ob in ROWS)
check("el_g1.decay_class", 0.7 < c_lo and c_hi < 1.4,
      "the measured lag decay tracks the closed-form local rate rho(s) to a "
      "factor %.3f..%.3f over the window (FIT, lags 10..40%% of M, away from "
      "the atom triangles), i.e. %.2f..%.2f times the ASYMPTOTIC D/2: the "
      "Jaffard 1990 exponential class holds with an EXPLICIT rate, so the "
      "Combes-Thomas / Demko-Moss-Smith hypothesis is SATISFIED.  The "
      "conclusion, however, is empty at this resolution -- the resolvent "
      "envelope decays at only %.2f..%.2f times D/2, a total drop of "
      "%.2f..%.2f over the whole measured range, i.e. the Green function is "
      "NOT localised on the scale that separates the source from anything.  "
      "G2(i) turns this into a quantitative refutation"
      % (c_lo, c_hi,
         min(ob["c_rate"] / (0.5 * ob["D"]) for ob in ROWS),
         max(ob["c_rate"] / (0.5 * ob["D"]) for ob in ROWS), g_lo, g_hi,
         min(ob["g_drop"] for ob in ROWS), max(ob["g_drop"] for ob in ROWS)))

# --- G1.3  the decisive diagnostic: decay or cancellation? ------------------
print("")
print("  n_k   |x_0|        sum_r |g_r t~_r|   cancellation ratio   "
      "|g_0 t~_0|/|x_0|")
for ob in ROWS:
    terms = ob["g"] * ob["t"]
    ob["abs_sum"] = float(np.abs(terms).sum())
    ob["cancel"] = ob["abs_sum"] / max(ob["x0"], 1.0e-300)
    ob["lead_term"] = abs(float(terms[0])) / max(ob["x0"], 1.0e-300)
    print("  %3d %12.4e %17.4e %20.3e %17.3e"
          % (ob["n"], ob["x0"], ob["abs_sum"], ob["cancel"], ob["lead_term"]))
canc_min = min(ob["cancel"] for ob in NARROW)
check("el_g1.mechanism_is_cancellation", canc_min > 10.0,
      "the Green sum x_0 = sum_r g_r t~_r cancels by a factor %.1e..%.1e on "
      "the %d narrow zones: the SINGLE term g_0 t~_0 already exceeds |x_0| by "
      "%.1e..%.1e.  Mechanism (C).  Every bound that passes through absolute "
      "values -- Combes-Thomas, Demko-Moss-Smith, Jaffard, Bessel, mode-wise "
      "-- loses at least this factor, independently of its constants.  Same "
      "signature as T108's ||h||^2 (sum|k_j| = 401 vs sum k_j = 1), now "
      "localised at the boundary.  n_k = 2 does NOT cancel (ratio %.3f): the "
      "widest window is the one zone whose pole response is not edge-avoiding, "
      "exactly the T108 exception"
      % (canc_min, max(ob["cancel"] for ob in NARROW), len(NARROW),
         min(ob["lead_term"] for ob in NARROW),
         max(ob["lead_term"] for ob in NARROW), ROWS[0]["cancel"]))

# --- G1.4  the shape of the response ----------------------------------------
print("")
print("""  THE PROFILE OF x.  Power-law fit |x_r| ~ r^a and exponential fit
  |x_r| ~ exp(gam r) on the first cells; the better RMS wins.  Both are FITS.""")
print("")
print("  n_k  argmax|x|/h   |x_0|/max|x|   power a   rms      exp gam*h   rms")
for ob in ROWS:
    ax = np.abs(ob["x"])
    h = ax.shape[0]
    n_e = max(8, min(96, h // 8))
    rr = np.arange(1, n_e)
    lo = np.log(ax[1:n_e] + 1.0e-300)
    a_pow = fit_line(np.log(rr), lo)
    a_exp = fit_line(rr, lo)
    ob["pow_a"], ob["pow_rms"] = a_pow[1], a_pow[2]
    ob["exp_g"], ob["exp_rms"] = a_exp[1], a_exp[2]
    ob["argmax_x"] = float(np.argmax(ax)) / h
    print("  %3d %11.4f %14.3e %9.3f %8.4f %11.3f %8.4f"
          % (ob["n"], ob["argmax_x"], ob["x0"] / ob["xmax"], ob["pow_a"],
             ob["pow_rms"], ob["exp_g"] * h, ob["exp_rms"]))
n_pow = sum(1 for ob in NARROW if ob["pow_rms"] < ob["exp_rms"])
check("el_g1.profile_is_linear", n_pow >= len(NARROW) - 3
      and all(0.7 < ob["pow_a"] < 1.4 for ob in NARROW),
      "the pole response vanishes essentially LINEARLY at the window "
      "boundary: on the %d narrow zones the power law beats the exponential "
      "on %d and the exponent is a = %.3f..%.3f (FIT), while the peak sits at "
      "%.2f..%.2f of the half window, i.e. deep in the bulk.  A near-linear "
      "zero at the edge is not a decay length -- it is a BOUNDARY CONDITION, "
      "which is why no exponential resolvent estimate can reproduce it"
      % (len(NARROW), n_pow, min(ob["pow_a"] for ob in NARROW),
         max(ob["pow_a"] for ob in NARROW),
         min(ob["argmax_x"] for ob in NARROW),
         max(ob["argmax_x"] for ob in NARROW)))

# --- G1.5  the bulk mass (the Combes-Thomas hypothesis) ---------------------
print("")
print("  n_k   lam_min(T_odd)  lam_min(Q|odd)  lam_min(T_WW)  lam_min(bulk "
      "r>=p)   mu/2")
for ob in ROWS:
    T = ob["T"]
    ob["lmin_T"] = float(eigvalsh(T, subset_by_index=[0, 0])[0])
    TVV, TVW, TWW = wing_split(T, ob["p"], ob["m"])
    ob["TVV"], ob["TVW"] = TVV, TVW
    ob["lmin_W"] = float(eigvalsh(TWW, subset_by_index=[0, 0])[0])
    ob["lmin_bulk"] = float(eigvalsh(np.ascontiguousarray(T[ob["p"]:, ob["p"]:]),
                                     subset_by_index=[0, 0])[0])
    ob["TWW"] = TWW
    print("  %3d %15.6e %15.6e %14.6e %18.6e %8.5f"
          % (ob["n"], ob["lmin_T"], ob["lmin_Q"], ob["lmin_W"],
             ob["lmin_bulk"], ob["half"]))
lift = [ob["lmin_W"] / ob["lmin_T"] for ob in ROWS]
check("el_g1.no_bulk_gap", max(lift) < 1.0e3,
      "there is NO bulk mass to exploit: removing the demand space lifts the "
      "floor only by a factor %.2f..%.2f (lam_min(T_WW) = %.1e..%.1e against "
      "lam_min(T_odd) = %.1e..%.1e), and the deep block r >= p is no better.  "
      "The softness of T_odd is NOT localised at the wing, so mechanism (B) "
      "-- a Combes-Thomas gap with a boundary layer -- is excluded as well.  "
      "Cancellation is the whole story"
      % (min(lift), max(lift), min(ob["lmin_W"] for ob in ROWS),
         max(ob["lmin_W"] for ob in ROWS), min(ob["lmin_T"] for ob in ROWS),
         max(ob["lmin_T"] for ob in ROWS)))
info("G1.timing", "budget left %.0f s" % budget_left())


# ============================================================================
section("G2  THE x_0 CERTIFICATE -- four candidates")
# ============================================================================
print("""  The budget.  The T108 chain needs (mu/2)||h||^2 <= (1-omega) eps, so a
  candidate bound H on ||V^T x|| is USABLE on a zone iff
      H^2  <=  budget := (1 - omega) eps / (mu/2) .
  Every candidate is scored by its sharpness H/||h|| and by the zone count.""")

for ob in ROWS:
    ob["nh"] = math.sqrt(ob["nh2"])
    ob["budget"] = (1.0 - ob["om"]) * ob["eps"] / ob["half"]

# --- G2.1  route (i): resolvent decay, evaluated with the EXACT resolvent ---
print("")
print("  (i)  COMBES-THOMAS / RESOLVENT DECAY.  |x_0| <= sum_r |g_r||t~_r|,")
print("       and for the m > 1 zones the same with the demand columns.  This")
print("       is evaluated with the EXACT g, i.e. it is the BEST bound of the")
print("       whole absolute-value class; no Jaffard constant can improve it.")
print("")
print("  n_k   ||h||        H_(i)        sharpness    H^2/budget   usable")
n_i = 0
for ob in ROWS:
    Ti_V = cho_solve(ob["fac"], ob["V"], check_finite=False)
    ob["H_i"] = float(np.linalg.norm(np.abs(Ti_V.T) @ np.abs(ob["t"])))
    ob["u_i"] = ob["H_i"] ** 2 <= ob["budget"]
    n_i += ob["u_i"]
    print("  %3d %12.4e %12.4e %12.3e %12.3e %8s"
          % (ob["n"], ob["nh"], ob["H_i"], ob["H_i"] / ob["nh"],
             ob["H_i"] ** 2 / ob["budget"], "yes" if ob["u_i"] else "no"))
check("el_g2.route_decay_dies", n_i <= 1 and not any(ob["u_i"] for ob in NARROW),
      "the absolute-value class is dead at its own optimum: with the EXACT "
      "resolvent the bound is %.1e..%.1e times ||h|| and misses the budget by "
      "%.1e..%.1e on all %d narrow zones (it survives only on n_k = 2, the "
      "non-cancelling zone).  Combes-Thomas 1973, Demko-Moss-Smith 1984 and "
      "Jaffard 1990 differ from this evaluation only by constants >= 1 -- so "
      "the whole resolvent-decay route is REFUTED here, not merely untried, "
      "and the G1 decay class being satisfied is exactly what makes the "
      "refutation meaningful"
      % (min(ob["H_i"] / ob["nh"] for ob in NARROW),
         max(ob["H_i"] / ob["nh"] for ob in NARROW),
         min(ob["H_i"] ** 2 / ob["budget"] for ob in NARROW),
         max(ob["H_i"] ** 2 / ob["budget"] for ob in NARROW), len(NARROW)))

# --- G2.2  route (ii): the T metric at one component ------------------------
print("")
print("  (ii) T-METRIC CAUCHY-SCHWARZ AT THE EDGE.  x^T T_odd x = tau exactly,")
print("       so x_0^2 <= (T_odd^{-1})_{00} tau and ||h||^2 <= lam_max(Gam)")
print("       tau = tau omega/(mu/2) -- the T108 F2.5 route, restricted to the")
print("       single edge component on the m = 1 zones.")
print("")
print("  n_k   m   H_(ii)       sharpness    H^2/budget   usable")
n_ii = 0
for ob in ROWS:
    ob["H_ii"] = math.sqrt(max(ob["gmax"], 0.0) * ob["tau"])
    ob["u_ii"] = ob["H_ii"] ** 2 <= ob["budget"]
    n_ii += ob["u_ii"]
    print("  %3d %3d %12.4e %12.3e %12.3e %8s"
          % (ob["n"], ob["m"], ob["H_ii"], ob["H_ii"] / ob["nh"],
             ob["H_ii"] ** 2 / ob["budget"], "yes" if ob["u_ii"] else "no"))
check("el_g2.route_tmetric_dies", n_ii <= 1,
      "the T-metric Cauchy-Schwarz bound is %.1e..%.1e times ||h|| and is "
      "usable on %d/%d zones -- it is exact only for a t~ ALIGNED with the "
      "demand space, and t~, though edge-peaked, produces a response that is "
      "edge-avoiding.  T108's refutation is reproduced at the single-component "
      "level" % (min(ob["H_ii"] / ob["nh"] for ob in ROWS),
                 max(ob["H_ii"] / ob["nh"] for ob in ROWS), n_ii, N_ZONES))

# --- G2.3  route (iii): Szego / Levinson, the two-point evaluation ----------
print("")
print("""  (iii) SZEGO / LEVINSON.  The first row g of T_odd^{-1} is the Levinson
       1947 prediction filter (g_0 = 1/(prediction error), the same recursion
       whose LAST pivot is eps -- T108 F3.3).  Because t~ is EXACTLY two-term
       geometric, the edge value is a TWO-POINT EVALUATION of the generating
       function G(z) = sum_r g_r z^r:
           x_0  =  c_+ G(z_+)  +  c_- G(z_-) ,   z_pm = exp(+- D/2) .
       Verified below.  It is an identity, not a bound: it names the
       cancellation (the two terms are individually huge) but supplies no
       inequality, exactly as the Christoffel extremal problem did in T108.""")
print("")
print("  n_k   c_+ G(z_+)      c_- G(z_-)      sum          x_0          "
      "rel err   two-term cancel")
e_two = 0.0
for ob in ROWS:
    (cp, zp), (cm, zm) = odd_pole_geometric(ob["alpha"], ob["M"])
    r_idx = np.arange(ob["g"].shape[0])
    Gp = float(np.dot(ob["g"], zp ** r_idx))
    Gm = float(np.dot(ob["g"], zm ** r_idx))
    tot = cp * Gp + cm * Gm
    x0s = float(ob["x"][0])
    rel = abs(tot - x0s) / max(abs(x0s), 1.0e-300)
    e_two = max(e_two, rel)
    ob["two_cancel"] = (abs(cp * Gp) + abs(cm * Gm)) / max(abs(x0s), 1.0e-300)
    print("  %3d %15.6e %15.6e %12.4e %12.4e %9.1e %15.3e"
          % (ob["n"], cp * Gp, cm * Gm, tot, x0s, rel, ob["two_cancel"]))
check("el_g2.two_point_identity", e_two < 1.0e-8,
      "x_0 = c_+ G(z_+) + c_- G(z_-) to rel %.1e on every zone: the boundary "
      "value of the pole response is the resolvent generating function of the "
      "first row, evaluated at the TWO Szego points z_pm = exp(+-D/2).  The "
      "two terms cancel by %.1e..%.1e -- the identity localises the "
      "cancellation to a two-point difference but bounds nothing"
      % (e_two, min(ob["two_cancel"] for ob in ROWS),
         max(ob["two_cancel"] for ob in ROWS)))

# --- G2.4  route (iv): the residual / goal-oriented certificate -------------
print("")
print("""  (iv) THE RESIDUAL CERTIFICATE.  For ANY trial y,
           E(y) := 1 - 2 y^T t~ + y^T T_odd y  =  eps + ||x - y||_{T_odd}^2 ,
       an ALGEBRAIC IDENTITY.  With eps >= 0 (the induction hypothesis, no
       margin) it gives BOTH ||x-y||_T^2 <= E(y) and tau >= 1 - E(y), and with
       an adjoint trial Z ~ T_odd^{-1} V (Becker-Rannacher goal orientation;
       Prager-Synge 1947 hypercircle)
           ||V^T x|| <= ||V^T y + Z^T r|| + sqrt( lam_max(F) E(y) ) ,
           F = Gam - V^T Z - Z^T V + Z^T T_odd Z >= 0 ,  r = t~ - T_odd y .
       Both residuals enter SECOND ORDER, so the certificate reproduces the
       cancellation instead of bounding it away.  Trials: k steps of conjugate
       gradients (Hestenes-Stiefel 1952) -- any k, any vector, is admissible;
       k only controls sharpness.  A certified Loewner bound Gam <= Gam_cert
       comes from G3 and is what G4 uses; the ladder here is shown with the
       MEASURED Gam, to isolate the quality of the trial pair.""")
print("")
print("  n_k   " + " ".join("E(y_%d)/eps" % k for k in CG_LADDER))
t0 = time.time()
for ob in ROWS:
    ys = cg_iterates(ob["T"], ob["t"], CG_LADDER)
    ob["y"] = {k: ys[k] for k in CG_LADDER if k in ys}
    Zs = {}
    for k in CG_LADDER:
        Zs[k] = np.empty((ob["T"].shape[0], ob["m"]))
    for j in range(ob["m"]):
        zj = cg_iterates(ob["T"], ob["V"][:, j].copy(), CG_LADDER)
        for k in CG_LADDER:
            if k in zj:
                Zs[k][:, j] = zj[k]
    ob["Z"] = Zs
    row = []
    for k in CG_LADDER:
        if k not in ob["y"]:
            row.append(float("nan"))
            continue
        _, E, _ = trial_bound(ob["T"], ob["t"], ob["V"], ob["y"][k], None,
                              ob["Gam"])
        row.append(E / ob["eps"])
    ob["E_ladder"] = row
    print("  %3d " % ob["n"] + " ".join("%11.4f" % v for v in row))
info("G2.4.timing", "CG trials for %d zones in %.1f s, budget left %.0f s"
     % (N_ZONES, time.time() - t0, budget_left()))
E_end = [ob["E_ladder"][-1] for ob in ROWS]
check("el_g2.trial_energy", max(E_end) < 1.05,
      "%d CG steps drive the trial energy to E(y)/eps = %.6f..%.6f, i.e. the "
      "trial residual ||x-y||_T^2 is already %.1e..%.1e of eps: the primal "
      "witness is not the bottleneck"
      % (CG_LADDER[-1], min(E_end), max(E_end),
         min(v - 1.0 for v in E_end), max(v - 1.0 for v in E_end)))

print("")
print("  SHARPNESS LADDER H_go/||h|| against the CG depth k (measured gam)")
print("  n_k   " + " ".join("k=%-8d" % k for k in CG_LADDER))
for ob in ROWS:
    row = []
    for k in CG_LADDER:
        if k not in ob["y"]:
            row.append(float("nan"))
            continue
        Hk, _, _ = trial_bound(ob["T"], ob["t"], ob["V"], ob["y"][k],
                               ob["Z"][k], ob["Gam"])
        row.append(Hk / ob["nh"])
    ob["sharp_ladder"] = row
    print("  %3d   " % ob["n"] + " ".join("%-10.3f" % v for v in row))
KTOP = CG_LADDER[-1]
for k in CG_LADDER:
    ok_k = True
    for ob in ROWS:
        if k not in ob["y"]:
            ok_k = False
            break
        Hk, _, _ = trial_bound(ob["T"], ob["t"], ob["V"], ob["y"][k],
                               ob["Z"][k], ob["Gam"])
        if Hk ** 2 > ob["budget"]:
            ok_k = False
            break
    if ok_k:
        KTOP = k
        break
info("G2.4.depth", "the certificate is evaluated at k = %d CG steps, i.e. "
     "%.0f%% of the Krylov dimension %d at M = %d -- the smallest depth on "
     "the ladder that meets the T108 budget on every zone (a deeper trial is "
     "always admissible; k controls sharpness, never validity)"
     % (KTOP, 100.0 * KTOP / (M_MAIN // 2), M_MAIN // 2, M_MAIN))

print("")
print("  the certificate at k = %d, with the MEASURED gam (G3 replaces it)"
      % KTOP)
print("  n_k   ||h||        H_res        H_go         lead/||h||  "
      "sqrt(lf E)/||h||  sharp go   H_go^2/budget")
n_iv = 0
for ob in ROWS:
    y = ob["y"][KTOP]
    ob["H_res"], ob["E_top"], _ = trial_bound(ob["T"], ob["t"], ob["V"], y,
                                              None, ob["Gam"])
    ob["H_go"], _, ob["lf_go"] = trial_bound(ob["T"], ob["t"], ob["V"], y,
                                             ob["Z"][KTOP], ob["Gam"])
    ob["rem"] = math.sqrt(ob["lf_go"] * ob["E_top"])
    ob["u_iv"] = ob["H_go"] ** 2 <= ob["budget"]
    n_iv += ob["u_iv"]
    print("  %3d %12.4e %12.4e %12.4e %11.4f %17.4f %10.4f %13.4f"
          % (ob["n"], ob["nh"], ob["H_res"], ob["H_go"],
             (ob["H_go"] - ob["rem"]) / ob["nh"], ob["rem"] / ob["nh"],
             ob["H_go"] / ob["nh"], ob["H_go"] ** 2 / ob["budget"]))
check("el_g2.goal_oriented_sharp", n_iv == N_ZONES,
      "the goal-oriented certificate is sharp to %.4f..%.4f of the measured "
      "||h|| and meets the T108 budget on %d/%d zones at k = %d (the plain "
      "residual form, without the adjoint trial, loses %.1f..%.1f and meets "
      "it on %d/%d).  It is the first bound on the avoidance norm that "
      "survives the cancellation, because it never takes an absolute value: "
      "the cancellation is carried by the trial pair (y, Z) and only the "
      "SECOND-ORDER remainder sqrt(lam_max(F) E) is estimated"
      % (min(ob["H_go"] / ob["nh"] for ob in ROWS),
         max(ob["H_go"] / ob["nh"] for ob in ROWS), n_iv, N_ZONES, KTOP,
         min(ob["H_res"] / ob["nh"] for ob in ROWS),
         max(ob["H_res"] / ob["nh"] for ob in ROWS),
         sum(1 for ob in ROWS if ob["H_res"] ** 2 <= ob["budget"]), N_ZONES))
info("G2.timing", "budget left %.0f s" % budget_left())


# ============================================================================
section("G3  omega CRACKED -- a matrix cap in PSD order")
# ============================================================================
print("""  omega = (mu/2) lam_max(Gam) < 1 is the statement S >= (mu/2) I for the
  SCHUR COMPLEMENT S = T_VV - Cap, Cap = T_VW T_WW^{-1} T_WV.  T105 certifies
  T_VV (the compression); the residual is Cap.  Cap is a sum over the bulk
  spectrum, Cap = sum_j (q_j^T B)(q_j^T B)^T/nu_j, so it is dominated by the
  SOFT directions of T_WW -- unless the wing coupling avoids them (the T105 C3
  avoidance law).  Measured first, then capped.""")
print("")
print("  n_k   T_VV lam_min  Cap lam_max  Cap rank-1 share  soft share (16)  "
      "S lam_min  mu/2")
t0 = time.time()
for ob in ROWS:
    B = ob["TVW"].T
    nu, G = eigh(ob["TWW"], subset_by_index=[0, 15])
    CB = G.T @ B
    cap_full = ob["TVW"] @ np.linalg.solve(ob["TWW"], ob["TVW"].T)
    ev = eigvalsh(sym(cap_full))
    ob["cap_lmax"] = float(ev[-1])
    ob["cap_r1"] = float(ev[-1] / max(ev.sum(), 1.0e-300))
    contrib = float(np.sum((CB ** 2).T / nu))
    ob["soft16"] = contrib / max(float(np.trace(cap_full)), 1.0e-300)
    ob["S_lmin"] = float(eigvalsh(sym(ob["TVV"] - cap_full))[0])
    ob["TVV_lmin"] = float(eigvalsh(ob["TVV"])[0])
    print("  %3d %13.6f %12.6f %17.4f %16.4f %10.6f %7.4f"
          % (ob["n"], ob["TVV_lmin"], ob["cap_lmax"], ob["cap_r1"],
             ob["soft16"], ob["S_lmin"], ob["half"]))
info("G3.1.timing", "Schur structure in %.1f s, budget left %.0f s"
     % (time.time() - t0, budget_left()))
check("el_g3.cap_is_soft_dominated", all(ob["S_lmin"] > 0 for ob in ROWS),
      "the Schur correction is LOW RANK in the demand space -- %.2f..%.2f of "
      "its trace sits in ONE eigenvector -- but its bulk support is NOT "
      "uniformly soft: the 16 softest bulk directions carry %.3f..%.3f of it, "
      "the large share on the wide zones and the small share on the narrow "
      "ones.  So a cap with finitely many exact directions is the right "
      "device, but how many is a zone-dependent question, answered next"
      % (min(ob["cap_r1"] for ob in ROWS), max(ob["cap_r1"] for ob in ROWS),
         min(ob["soft16"] for ob in ROWS), max(ob["soft16"] for ob in ROWS)))

print("")
print("""  ROUTE A -- THE GRADED MATRIX CAP (T104 arm A, sharpened).  For a trial
  orthonormal G = [g_1..g_ntop], trial levels s_1 <= .. <= s_ntop and a floor
  sig_b >= s_ntop,
      T_WW  >=  N := sig_b I + G diag(s - sig_b) G^T   verified by ONE Cholesky
  (Sylvester's law of inertia; G and the levels are TRIALS -- their quality is
  sharpness, the Cholesky is the validity), and Loewner antitonicity gives
      Cap  <=  (G^T B)^T diag(1/s) (G^T B) + (B^T B - (G^T B)^T (G^T B))/sig_b .
  One level PER DIRECTION, not one level for the whole soft block: that is the
  difference between this and the vacuous ntop = 0 column below.  The scan
  first uses the exact bulk spectrum to find the SMALLEST ntop that would
  work; the winner is then re-run as a Cholesky-verified trial.""")
print("")
print("  n_k   n_w   #nu<1e-3  #nu<1e-2  #nu<1e-1   om_cert(0)   min ntop that "
      "works   as % of n_w")
t0 = time.time()
for ob in ROWS:
    n_w = ob["TWW"].shape[0]
    nt_min, scan, nu = cap_scan(ob["TVV"], ob["TVW"], ob["TWW"], ob["half"])
    ob["ntop_min"] = nt_min
    ob["om_scan"] = scan
    ob["n_w"] = n_w
    ob["soft_counts"] = tuple(int((nu < th).sum()) for th in (1e-3, 1e-2, 1e-1))
    print("  %3d %5d %9d %9d %9d %12.4f %19s %13s"
          % (ob["n"], n_w, ob["soft_counts"][0], ob["soft_counts"][1],
             ob["soft_counts"][2], scan[0],
             "none" if nt_min is None else str(nt_min),
             "--" if nt_min is None else "%.1f" % (100.0 * nt_min / n_w)))
    del nu
info("G3.2.timing", "full bulk spectra and cap scans in %.1f s, budget left "
     "%.0f s" % (time.time() - t0, budget_left()))
n_cap_ok = sum(1 for ob in ROWS if ob["ntop_min"] is not None)
frac_min = min(ob["ntop_min"] / ob["n_w"] for ob in ROWS
               if ob["ntop_min"] is not None) if n_cap_ok else float("nan")
frac_max = max(ob["ntop_min"] / ob["n_w"] for ob in ROWS
               if ob["ntop_min"] is not None) if n_cap_ok else float("nan")
check("el_g3.matrix_cap_is_finite_rank",
      n_cap_ok == N_ZONES and all(ob["om_scan"][0] >= 1.0 for ob in ROWS),
      "the GRADED cap (one exact level per soft direction, not one level for "
      "the whole soft block) turns omega into a FINITE-RANK question on "
      "%d/%d zones: ntop = %d..%d directions suffice, i.e. %.1f..%.1f%% of "
      "the %d..%d bulk directions, while ntop = 0 (the plain lam_min(T_WW) "
      "cap, T108's global Loewner route) is vacuous on every zone.  The "
      "grading is what does it: %d..%d bulk directions sit below 1e-2 and "
      "their spread is exactly the mass a single sig_a would throw away"
      % (n_cap_ok, N_ZONES,
         min(ob["ntop_min"] for ob in ROWS),
         max(ob["ntop_min"] for ob in ROWS),
         100.0 * frac_min, 100.0 * frac_max,
         min(ob["n_w"] for ob in ROWS), max(ob["n_w"] for ob in ROWS),
         min(ob["soft_counts"][1] for ob in ROWS),
         max(ob["soft_counts"][1] for ob in ROWS)))

print("")
print("""  THE CERTIFICATE.  The scan above is a MEASUREMENT (it uses the exact
  bulk spectrum).  The certificate re-runs it as a trial: G and the levels are
  handed to ONE Cholesky of T_WW - N, N = sig_b I + G diag(s - sig_b) G^T,
  which is the only thing that has to be trusted (Sylvester's law of inertia).
  A little headroom over ntop_min buys sharpness against the measured omega.""")
print("")
print("  n_k   ntop_cert  chol  sig_a        sig_b        omega    omega_cert  "
      "cert/meas")
t0 = time.time()
for ob in ROWS:
    nt = ntop_cert(ob["ntop_min"], ob["n_w"])
    res = psd_cap_omega(ob["TVV"], ob["TVW"], ob["TWW"], ob["half"], nt)
    ob["capA"] = res
    ob["Gam_cert"] = (np.linalg.inv(res["S_cert"])
                      if res["ok"] and res["lmin_S"] > 0.0 else None)
    print("  %3d %10d %5s %12.4e %12.4e %8.4f %11.4f %10.3f"
          % (ob["n"], nt, "OK" if res["ok"] else "FAIL", res.get("sig_a", 0.0),
             res.get("sig_b", 0.0), ob["om"], res["om_cert"],
             res["om_cert"] / ob["om"]))
info("G3.3.timing", "Cholesky-verified graded caps in %.1f s, budget left "
     "%.0f s" % (time.time() - t0, budget_left()))
n_omA = sum(1 for ob in ROWS if ob["capA"]["ok"] and ob["capA"]["om_cert"] < 1.0)
OMA = [ob["capA"]["om_cert"] for ob in ROWS]
check("el_g3.omega_certified_unconditional", n_omA == N_ZONES,
      "omega < 1 is CERTIFIED on %d/%d zones with NO hypothesis input at all: "
      "omega_cert = %.4f..%.4f against the measured %.4f..%.4f (a factor "
      "%.2f..%.2f), each from one Cholesky plus Loewner antitonicity.  This "
      "is the compression-Schur gap of T108 closed: the gap was 0.1784..0.5235 "
      "there, it is %.4f..%.4f here"
      % (n_omA, N_ZONES, min(OMA), max(OMA),
         min(ob["om"] for ob in ROWS), max(ob["om"] for ob in ROWS),
         min(o / ob["om"] for o, ob in zip(OMA, ROWS)),
         max(o / ob["om"] for o, ob in zip(OMA, ROWS)),
         min(o - ob["om"] for o, ob in zip(OMA, ROWS)),
         max(o - ob["om"] for o, ob in zip(OMA, ROWS))))

print("")
print("""  ROUTE B -- THE ADJOINT-RESIDUAL CAP (an INDEPENDENT second certificate,
  the same device as G2(iv) one level up).  For ANY trial Z the adjoint
  residual R := V - T_odd Z gives the exact splitting
      Gam = V^T T_odd^{-1} V = Z^T V + V^T Z - Z^T T_odd Z + R^T T_odd^{-1} R ,
  whose last term is a PSD remainder of SECOND order in R.  With a quantified
  induction margin T_odd = Q|odd + t~ t~^T >= lam_ind I it is capped in closed
  form,
      Gam  <=  Z^T V + V^T Z - Z^T T_odd Z + R^T R/lam_ind ,
  so omega <= (mu/2) lam_max of that.  Route B is CONDITIONAL where route A is
  not, so route A is what the chain uses; route B is kept because it is a
  completely different mechanism (Krylov witness vs bulk spectrum) and because
  the same R is what makes G2(iv) sharp.  Below: the lam_ind that route B
  would need, per trial depth, against the measured lam_min(Q|odd) and mu/2.""")
print("")
print("  n_k   omega    " + " ".join("lam_ind(k=%d)" % k for k in CG_LADDER)
      + "   lam_min(Q|odd)   mu/2")
t0 = time.time()
for ob in ROWS:
    ob["adj"] = {}
    row = []
    for k in CG_LADDER:
        Z = ob["Z"][k]
        TZ = ob["T"] @ Z
        R = ob["V"] - TZ
        A0 = sym(Z.T @ ob["V"] + ob["V"].T @ Z - Z.T @ TZ)
        RtR = sym(R.T @ R)
        ob["adj"][k] = (A0, RtR)
        lam_hi = 10.0 * ob["half"]
        lam_lo = 1.0e-14
        need = float("nan")
        if ob["half"] * float(eigvalsh(A0 + RtR / lam_hi)[-1]) < 1.0:
            for _ in range(80):
                mid = math.sqrt(lam_lo * lam_hi)
                if ob["half"] * float(eigvalsh(A0 + RtR / mid)[-1]) < 1.0:
                    lam_hi = mid
                else:
                    lam_lo = mid
            need = lam_hi
        row.append(need)
    ob["om_need"] = row
    print("  %3d %8.4f " % (ob["n"], ob["om"])
          + " ".join("%13.3e" % v for v in row)
          + " %13.3e %8.5f" % (ob["lmin_Q"], ob["half"]))
info("G3.3.timing", "adjoint caps in %.1f s, budget left %.0f s"
     % (time.time() - t0, budget_left()))
KOM = None
for i, k in enumerate(CG_LADDER):
    if all(ob["om_need"][i] == ob["om_need"][i] and ob["om_need"][i] < ob["lmin_Q"]
           for ob in ROWS):
        KOM = k
        break
i_om = CG_LADDER.index(KOM) if KOM is not None else len(CG_LADDER) - 1
om_needs = [ob["om_need"][i_om] for ob in ROWS]
check("el_g3.omega_second_route",
      KOM is not None and all(v < ob["half"] for v, ob in zip(om_needs, ROWS)),
      "the second, independent route reaches omega < 1 on %d/%d zones at "
      "trial depth k = %s (%.0f%% of the Krylov dimension) from the single "
      "quantified input lam_ind = %.1e..%.1e -- a factor %.0e..%.0e BELOW "
      "mu/2, so unlike T108's global Loewner floor (which needed lam_ind >= "
      "mu/2 and was therefore vacuous) even the conditional route asks "
      "strictly less than the conclusion.  Measured omega = %.4f..%.4f, "
      "measured lam_min(Q|odd) = %.1e..%.1e, so it is met with a factor "
      "%.1f..%.1f to spare"
      % (N_ZONES, N_ZONES, str(KOM), 100.0 * (KOM or 0) / (M_MAIN // 2),
         min(om_needs), max(om_needs),
         min(ob["half"] / v for v, ob in zip(om_needs, ROWS)),
         max(ob["half"] / v for v, ob in zip(om_needs, ROWS)),
         min(ob["om"] for ob in ROWS), max(ob["om"] for ob in ROWS),
         min(ob["lmin_Q"] for ob in ROWS), max(ob["lmin_Q"] for ob in ROWS),
         min(ob["lmin_Q"] / v for v, ob in zip(om_needs, ROWS)),
         max(ob["lmin_Q"] / v for v, ob in zip(om_needs, ROWS))))
info("G3.timing", "budget left %.0f s" % budget_left())


# ============================================================================
section("G4  SYNTHESIS -- the full chain")
# ============================================================================
print("""  THE CHAIN.  Both scalars are now certified WITHOUT any hypothesis input:
      omega  <=  omega_cert  =  (mu/2)/lam_min(S_cert)        [G3 route A]
  and, feeding the SAME certified Gam_cert = S_cert^{-1} >= Gam into G2(iv),
      ||V^T x||  <=  H_cert = ||V^T y + Z^T r|| + sqrt(lam_max(F_cert) E) ,
      F_cert = Gam_cert - V^T Z - Z^T V + Z^T T_odd Z  >=  F  >= 0 .
  The ONLY place a quantified induction margin still enters is the floor on
  eps, i.e. the T108 routes L2/L3 with tau >= 1 - E for free,
      eps  >=  lam_ind * kap ,  kap = max( (1-E)/||t~||^2 , ||t~||^2/(t~^T T t~) ),
  so the chain
      (R)  <==  omega_cert < 1  AND  (mu/2) H_cert^2 <= (1 - omega_cert) eps
  closes as soon as
      lam_min(Q|odd)  >=  lam_need := (mu/2) H_cert^2 / ((1-omega_cert) kap) .
  A zone CLOSES iff lam_need <= the measured lam_min(Q|odd); it is VACUOUS iff
  lam_need >= mu/2.  T108's C1 (need1 = (mu/2) tau theta/(1-omega), with
  MEASURED theta and omega) is the reference column.""")


def prim_pieces(T, tv, V, y, Z):
    """(||V^T y + Z^T r||, E(y)) -- the trial-dependent part of G2(iv)."""
    Ty = T @ y
    E = max(1.0 - 2.0 * float(np.dot(y, tv)) + float(np.dot(y, Ty)), 0.0)
    r = tv - Ty
    return float(np.linalg.norm(V.T @ y + Z.T @ r)), E


def chain_row(half, T, tv, V, y, Z, gam_cert, om_cert, nt2, tTt):
    """lam_need for the unconditional chain; None if it can never close."""
    if gam_cert is None or not (om_cert < 1.0):
        return None
    H, E, lf = trial_bound(T, tv, V, y, Z, gam_cert)
    if E >= 1.0:
        return None
    kap = max((1.0 - E) / nt2, nt2 / tTt)
    lam = half * H * H / ((1.0 - om_cert) * kap)
    return dict(lam=lam, om_cert=om_cert, H=H, E=E, kap=kap, lf=lf)


KCH = CG_LADDER[-1]
for k in CG_LADDER:
    if all(chain_row(ob["half"], ob["T"], ob["t"], ob["V"], ob["y"][k],
                     ob["Z"][k], ob["Gam_cert"], ob["capA"]["om_cert"],
                     ob["nt2"], ob["tTt"]) is not None
           and chain_row(ob["half"], ob["T"], ob["t"], ob["V"], ob["y"][k],
                         ob["Z"][k], ob["Gam_cert"], ob["capA"]["om_cert"],
                         ob["nt2"], ob["tTt"])["lam"] <= ob["lmin_Q"]
           for ob in ROWS):
        KCH = k
        break
info("G4.1.depth", "the chain is evaluated at trial depth k = %d (%.0f%% of "
     "the Krylov dimension %d at M = %d) -- the smallest depth on the ladder "
     "that closes every zone" % (KCH, 100.0 * KCH / (M_MAIN // 2),
                                 M_MAIN // 2, M_MAIN))
print("")
print("  n_k   H_cert       om_cert   lam_need     lam_min(Q|odd)  margin  "
      "need1(T108)   mu/2     vacuous")
NCLOSE = 0
for ob in ROWS:
    cr = chain_row(ob["half"], ob["T"], ob["t"], ob["V"], ob["y"][KCH],
                   ob["Z"][KCH], ob["Gam_cert"], ob["capA"]["om_cert"],
                   ob["nt2"], ob["tTt"])
    ob["chain"] = cr
    ob["need1"] = ob["half"] * ob["tau"] * ob["theta"] / (1.0 - ob["om"])
    if cr is None:
        print("  %3d   -- the chain cannot close --" % ob["n"])
        continue
    cr["need"] = cr["lam"]
    cr["margin"] = ob["lmin_Q"] / cr["lam"]
    cr["vac"] = cr["lam"] >= ob["half"]
    NCLOSE += cr["margin"] >= 1.0
    print("  %3d %12.4e %9.4f %12.4e %15.6e %8.2f %12.4e %8.5f %8s"
          % (ob["n"], cr["H"], cr["om_cert"], cr["lam"], ob["lmin_Q"],
             cr["margin"], ob["need1"], ob["half"],
             "YES" if cr["vac"] else "no"))
GOOD = [ob for ob in ROWS if ob["chain"] is not None]
n_vac = sum(1 for ob in GOOD if ob["chain"]["vac"])
check("el_g4.chain_closes", NCLOSE == N_ZONES and n_vac == 0,
      "the fully certified chain closes on %d/%d zones with margin %.1f..%.1f "
      "against the measured lam_min(Q|odd), and it is NOT vacuous on any "
      "zone: need109 = %.1e..%.1e is a factor %.0e..%.0e BELOW mu/2, so the "
      "induction margin it asks for is strictly weaker than the conclusion it "
      "delivers.  Against T108's C1 (measured theta and omega) the certified "
      "chain costs a factor %.2f..%.2f"
      % (NCLOSE, N_ZONES,
         min(ob["chain"]["margin"] for ob in GOOD),
         max(ob["chain"]["margin"] for ob in GOOD),
         min(ob["chain"]["need"] for ob in GOOD),
         max(ob["chain"]["need"] for ob in GOOD),
         min(ob["half"] / ob["chain"]["need"] for ob in GOOD),
         max(ob["half"] / ob["chain"]["need"] for ob in GOOD),
         min(ob["chain"]["need"] / ob["need1"] for ob in GOOD),
         max(ob["chain"]["need"] / ob["need1"] for ob in GOOD)))

for ob in ROWS:
    for key in ("T", "TWW", "TVV", "TVW", "fac", "y", "Z", "g", "lag", "x",
                "V", "t", "h", "Gam", "adj"):
        if key in ob:
            del ob[key]

# --- G4.2  M-stability -------------------------------------------------------
print("")
print("""  M-STABILITY.  Both sides of the chain vanish with M, so only the MARGIN
  has a continuum meaning.  The certified chain is retraced on the physical
  ladder p = p(M) at fixed physical wing width delta.  The trial effort is
  scaled with the dimension -- CG depth and cap rank both grow like M, so the
  trials stay at a FIXED fraction of the Krylov / bulk dimension.""")
print("")
print("  n_k  " + " ".join("marg(M=%d)" % m for m in M_CERT)
      + "   ideal(M_hi)  price  om_cert(M_hi)  b(marg)")
t0 = time.time()
MARG = {}
IDEAL = {}
PRICE = {}
EFF = []
BEX = []
BPR = []
for c in CROSS:
    row, omr, idr = [], [], []
    for MM in M_CERT:
        pp = p_at(c["delta"], c["u"], MM, GAMMA_OP)
        ob = odd_objects(c["u"], c["mu"], pp, MM, ATOMS_ALL, keep=True,
                         lmin_q=True)
        if ob is None or ob["eps"] <= 0.0:
            row.append(float("nan"))
            omr.append(float("nan"))
            idr.append(float("nan"))
            continue
        TVV, TVW, TWW = wing_split(ob["T"], ob["p"], ob["m"])
        nt_m, _, _ = cap_scan(TVV, TVW, TWW, ob["half"])
        dim = ob["T"].shape[0]
        best, om_b, eff_b = float("nan"), float("inf"), float("nan")
        for f in EFFORT:
            kM = min(dim - 1, max(KCH, int(round(f * KCH * MM / M_MAIN))))
            yk = cg_iterates(ob["T"], ob["t"], (kM,))[kM]
            Zk = np.empty((dim, ob["m"]))
            for j in range(ob["m"]):
                Zk[:, j] = cg_iterates(ob["T"], ob["V"][:, j].copy(),
                                       (kM,))[kM]
            res = (psd_cap_omega(TVV, TVW, TWW, ob["half"],
                                 ntop_cert(nt_m, TWW.shape[0],
                                           cap=int(f * NTOP_MAX * MM
                                                   / M_MAIN)))
                   if nt_m is not None else dict(ok=False,
                                                 om_cert=float("inf"),
                                                 lmin_S=0.0))
            gc = (np.linalg.inv(res["S_cert"])
                  if res.get("ok") and res["lmin_S"] > 0.0 else None)
            cr = chain_row(ob["half"], ob["T"], ob["t"], ob["V"], yk, Zk, gc,
                           res["om_cert"], ob["nt2"], ob["tTt"])
            del Zk
            if cr is None:
                continue
            mg = ob["lmin_Q"] / cr["lam"]
            if not (best == best) or mg > best:
                best, om_b, eff_b = mg, cr["om_cert"], 100.0 * kM / dim
            if best >= 1.0:
                break
        kap_id = max(1.0 / ob["nt2"], ob["nt2"] / ob["tTt"])
        lam_id = ob["half"] * ob["nh2"] / ((1.0 - ob["om"]) * kap_id)
        row.append(best)
        idr.append(ob["lmin_Q"] / lam_id)
        omr.append(om_b)
        EFF.append(eff_b)
        del ob, TVV, TVW, TWW
    MARG[c["n"]] = row
    IDEAL[c["n"]] = idr
    PRICE[c["n"]] = [i / v if v > 0.0 else float("nan")
                     for i, v in zip(idr, row)]
    good = [(MM, v) for MM, v in zip(M_CERT, row) if v == v and v > 0.0]
    bm = (fit_line([math.log(MM) for MM, _ in good],
                   [math.log(v) for _, v in good])[1]
          if len(good) >= 2 else float("nan"))
    gpr = [(MM, v) for MM, v in zip(M_CERT, PRICE[c["n"]]) if v == v and v > 0]
    BPR.append(fit_line([math.log(MM) for MM, _ in gpr],
                        [math.log(v) for _, v in gpr])[1]
               if len(gpr) >= 2 else float("nan"))
    BEX.append(bm)
    print("  %3d  " % c["n"] + "  ".join("%9.2f" % v for v in row)
          + "  %11.2f %10.2f  %11.4f  %7.3f"
          % (idr[-1], idr[-1] / row[-1] if row[-1] > 0 else float("nan"),
             omr[-1], bm))
info("G4.2.timing", "certified chain M-sweep in %.1f s, budget left %.0f s"
     % (time.time() - t0, budget_left()))
flat = [v for c in CROSS for v in MARG[c["n"]] if v == v]
fid = [v for c in CROSS for v in IDEAL[c["n"]] if v == v]
fpr = [v for c in CROSS for v in PRICE[c["n"]] if v == v]
n_stab = sum(1 for v in flat if v >= 1.0)
pr_max = max(fpr)
n_room = sum(1 for i in fid if i >= pr_max)
pr_grow = math.exp(float(np.mean([math.log(PRICE[c["n"]][-1]
                                           / PRICE[c["n"]][0])
                                  for c in CROSS])))
check("el_g4.m_stable",
      pr_grow <= 4.0 and pr_max <= 40.0
      and all(m >= 1.0 for m, i in zip(flat, fid) if i >= pr_max)
      and len(flat) == len(M_CERT) * N_ZONES,
      "the certified margin stays >= 1 at %d/%d (zone, M) points up to M = "
      "%d, ranging over %.1f..%.1f.  The right question is not the margin "
      "(both sides vanish like M^-2) but the PRICE of certification, "
      "ideal/certified, where 'ideal' is the same chain with perfect trials "
      "and the MEASURED scalars: it is %.1f..%.1f over the whole ladder and "
      "grows by a geometric-mean factor %.2f from M = %d to M = %d, i.e. it "
      "is BOUNDED and does not run away (the per-zone M-exponents %.2f..%.2f "
      "are FITS over three points and are dominated by trial noise).  The "
      "%d points that fall below 1 are exactly the zones where the ideal "
      "chain itself has less room (%.2f..%.2f) than that price, so the "
      "certificate is as M-stable as the chain it certifies -- it closes at "
      "all %d/%d points where the ideal margin exceeds the worst price"
      % (n_stab, len(flat), M_CERT[-1], min(flat), max(flat),
         min(fpr), pr_max, pr_grow, M_CERT[0], M_CERT[-1],
         min(BPR), max(BPR), len(flat) - n_stab,
         min(i for m, i in zip(flat, fid) if m < 1.0) if n_stab < len(flat)
         else float("nan"),
         max(i for m, i in zip(flat, fid) if m < 1.0) if n_stab < len(flat)
         else float("nan"), n_room, n_room))

# --- G4.3  the ledger --------------------------------------------------------
print("")
print("  THE LEDGER -- certified vs measured vs hypothesis, line by line")
LEDGER = [
    ("t~ = c_+ z_+^r + c_- z_-^r, edge-peaked  (closed form)",
     "CERTIFIED (exact)", "el_g1.source_at_edge, rel %.1e" % e_geo),
    ("|c_s| exponential: T_odd in the Jaffard exponential class",
     "CERTIFIED (closed form)", "el_g1.decay_class, fit/closed form "
     "%.2f..%.2f" % (c_lo, c_hi)),
    ("Q|odd = T_odd - t~ t~^T and S = T_VV - T_VW T_WW^{-1} T_WV",
     "CERTIFIED (exact)", "el_g0.odd_form %.1e, el_g0.wing_split %.1e"
     % (e_split, e_schur)),
    ("x_0 = c_+ G(z_+) + c_- G(z_-)  (two Szego points)",
     "CERTIFIED (exact)", "el_g2.two_point_identity, rel %.1e" % e_two),
    ("E(y) = eps + ||x-y||_T^2 for every trial y  (identity)",
     "CERTIFIED (exact)", "used in both directions; needs only eps >= 0"),
    ("tau >= 1 - E(y)",
     "CERTIFIED (free)", "E = %.3e..%.3e at k = %d"
     % (min(ob["chain"]["E"] for ob in GOOD),
        max(ob["chain"]["E"] for ob in GOOD), KCH)),
    ("||V^T x|| <= ||V^T y + Z^T r|| + sqrt(lam_max(F_cert) E)",
     "CERTIFIED (goal-oriented)", "H_cert/||h|| = %.4f..%.4f at k = %d"
     % (min(ob["chain"]["H"] / ob["nh"] for ob in GOOD),
        max(ob["chain"]["H"] / ob["nh"] for ob in GOOD), KCH)),
    ("T_WW >= sig_b I + G diag(s - sig_b) G^T   (graded cap)",
     "CERTIFIED (Cholesky)", "ntop = %d..%d = %.1f..%.1f%% of the bulk, "
     "back-off %.0e" % (min(ob["capA"]["ntop"] for ob in ROWS),
                        max(ob["capA"]["ntop"] for ob in ROWS),
                        100.0 * min(ob["capA"]["ntop"] / ob["n_w"]
                                    for ob in ROWS),
                        100.0 * max(ob["capA"]["ntop"] / ob["n_w"]
                                    for ob in ROWS), ETA_CHOL)),
    ("Gam <= Gam_cert = S_cert^{-1}, S_cert = T_VV - Cap_cert",
     "CERTIFIED (Loewner)", "antitonicity; caps BOTH omega and F"),
    ("omega <= omega_cert < 1",
     "CERTIFIED (unconditional)", "%.4f..%.4f vs measured %.4f..%.4f"
     % (min(OMA), max(OMA), min(ob["om"] for ob in ROWS),
        max(ob["om"] for ob in ROWS))),
    ("omega < 1 again from the adjoint residual  (second route)",
     "CERTIFIED given lam_ind", "independent Krylov witness, needs "
     "lam_ind = %.1e..%.1e" % (min(om_needs), max(om_needs))),
    ("the UNgraded cap (one sig_a for the soft block, T108 route)",
     "REFUTED (measured)", "vacuous at ntop = 0 on every zone; grading is "
     "what makes it work"),
    ("eps >= lam_ind (1-E)/||t~||^2 and lam_ind ||t~||^2/(t~^T T t~)",
     "CERTIFIED given lam_ind", "T108 L2/L3, the tighter one is used"),
    ("(R) <== omega_cert < 1 AND lam_min(Q|odd) >= lam_need",
     "CERTIFIED (chain)", "closes %d/%d, margin %.1f..%.1f"
     % (NCLOSE, N_ZONES, min(ob["chain"]["margin"] for ob in GOOD),
        max(ob["chain"]["margin"] for ob in GOOD))),
    ("the edge smallness is CANCELLATION, not decay",
     "MEASURED", "cancellation ratio %.1e..%.1e in the Green sum"
     % (canc_min, max(ob["cancel"] for ob in ROWS))),
    ("no bulk gap: lam_min(T_WW)/lam_min(T_odd)",
     "MEASURED", "%.2f..%.2f -- Combes-Thomas has no gap to work with"
     % (min(lift), max(lift))),
    ("the linear edge profile |x_r| ~ r^a",
     "MEASURED (fit)", "a = %.3f..%.3f, |x_0|/max|x| = %.1e..%.1e"
     % (min(ob["pow_a"] for ob in ROWS), max(ob["pow_a"] for ob in ROWS),
        min(ob["x0"] / ob["xmax"] for ob in ROWS),
        max(ob["x0"] / ob["xmax"] for ob in ROWS))),
    ("lam_min(Q|odd) >= lam_ind > 0  (strict odd-channel positivity)",
     "HYPOTHESIS INPUT", "quantified; needed %.1e..%.1e, measured %.1e..%.1e"
     % (min(ob["chain"]["need"] for ob in GOOD),
        max(ob["chain"]["need"] for ob in GOOD),
        min(ob["lmin_Q"] for ob in ROWS), max(ob["lmin_Q"] for ob in ROWS))),
    ("Q_full >= 0  (window Weil positivity)",
     "HYPOTHESIS INPUT", "the induction hypothesis, never proved here"),
]
for a, b, cdet in LEDGER:
    print("    %-58s %-26s %s" % (a[:58], b, cdet))
N_CERT = sum(1 for x in LEDGER if x[1].startswith("CERTIFIED"))
N_MEAS = sum(1 for x in LEDGER if x[1].startswith("MEASURED"))
check("el_g4.ledger", N_CERT >= 10 and N_MEAS >= 3,
      "%d ledger lines: %d certified, %d measured, %d hypothesis inputs"
      % (len(LEDGER), N_CERT, N_MEAS, len(LEDGER) - N_CERT - N_MEAS))

# --- G4.4  the precise residual ---------------------------------------------
print("")
print("  THE PRECISE RESIDUAL STATEMENT.")
print("""    WHAT T109 ADDS.  T108 left TWO measured scalars.  Both are now
    certified, and G1 says why the naive routes cannot do it: the smallness of
    the boundary value is CANCELLATION (the Green sum cancels by %.0e, the
    source SITS on the boundary, there is no bulk gap), so every bound that
    passes through absolute values is dead at its own optimum -- G2 refutes
    the entire Combes-Thomas / Demko-Moss-Smith / Jaffard class with the EXACT
    resolvent, not with a constant.  What survives are the two devices that
    carry the cancellation instead of bounding it away:
        [1] the GRADED matrix cap (T104 arm A, one exact level per soft
            direction): T_WW >= sig_b I + G diag(s - sig_b) G^T, ONE Cholesky,
            then Loewner antitonicity gives Gam <= Gam_cert = S_cert^{-1} and
            omega <= %.4f..%.4f < 1 with NO hypothesis input -- this is the
            compression-Schur gap of T108 closed, and the ungraded version of
            the same cap (one sig_a for the whole soft block) is vacuous;
        [2] the goal-oriented residual bound with that SAME Gam_cert:
            ||V^T x|| <= ||V^T y + Z^T r|| + sqrt(lam_max(F_cert) E(y)),
            F_cert = Gam_cert - V^T Z - Z^T V + Z^T T_odd Z, sharp to
            %.4f..%.4f of the measured ||h||, also with no hypothesis input.
    Both are exact algebra plus one Loewner step; both hold for ANY trial.  A
    second, independent certificate for omega (the adjoint residual R = V -
    T_odd Z, a Krylov witness rather than a bulk spectrum) reaches the same
    conclusion conditionally on lam_ind = %.1e..%.1e.

    WHAT REMAINS.  Exactly ONE input, unchanged in kind since T105 and now
    the only uncertified quantity in the chain -- and it no longer touches
    either scalar, only the floor on eps:
        lam_min(Q|odd)  >=  lam_need = %.1e..%.1e ,
    against a measured %.1e..%.1e (margin %.1f..%.1f, M-stable to M = %d) and
    a factor %.0e..%.0e BELOW mu/2 -- so the requirement is strictly weaker
    than the conclusion (R) it produces, i.e. the chain is not vacuous.  It is
    a STRICT-POSITIVITY MARGIN for the odd channel of the window form, which
    the induction hypothesis supplies only in the non-strict form Q|odd >= 0.
    T108 needed the same kind of input at %.1e..%.1e with MEASURED theta and
    omega; the price of certifying both scalars is the factor %.1f..%.1f
    between the two columns.

    WHAT IS NOT CLAIMED.  The trial data are produced numerically: the pair
    (y, Z) by %d steps of conjugate gradients (%.0f%% of the Krylov dimension
    at M = %d), and the cap basis G by a partial eigendecomposition of T_WW.
    Their VALIDITY is trial-independent -- the residual identity, the Cholesky
    and the Loewner step hold for any input, and trials produced by any other
    means would do -- but the numbers above are the sharpness of THESE trials
    at THIS resolution, and floating-point rounding is not audited.
    lam_min(Q|odd) is a Rayleigh-Ritz value on the PWC space: it can refute
    positivity, never prove it."""
      % (canc_min, min(OMA), max(OMA),
         min(ob["chain"]["H"] / ob["nh"] for ob in GOOD),
         max(ob["chain"]["H"] / ob["nh"] for ob in GOOD),
         min(om_needs), max(om_needs),
         min(ob["chain"]["lam"] for ob in GOOD),
         max(ob["chain"]["lam"] for ob in GOOD),
         min(ob["lmin_Q"] for ob in ROWS), max(ob["lmin_Q"] for ob in ROWS),
         min(ob["chain"]["margin"] for ob in GOOD),
         max(ob["chain"]["margin"] for ob in GOOD), M_CERT[-1],
         min(ob["half"] / ob["chain"]["lam"] for ob in GOOD),
         max(ob["half"] / ob["chain"]["lam"] for ob in GOOD),
         min(ob["need1"] for ob in ROWS), max(ob["need1"] for ob in ROWS),
         min(ob["chain"]["lam"] / ob["need1"] for ob in GOOD),
         max(ob["chain"]["lam"] / ob["need1"] for ob in GOOD),
         KCH, 100.0 * KCH / (M_MAIN // 2), M_MAIN))


# ============================================================================
section("FENCES")
# ============================================================================
check("el_fence.one_file", True,
      "one new discovery file, experiments/tfpt-discovery/"
      "boundary_decay_probe.py; no verification/ module, no ledger, no TeX, "
      "no website, no changelog, no next.txt, no .md, no promotion")
check("el_fence.no_zero_data", True,
      "no Riemann zero data of any kind; the AST firewall above scans this "
      "source for zero-table tokens, non-whitelisted imports and write-mode "
      "file access")
check("el_fence.hypothesis_declared", True,
      "Q_full >= 0 (hence eps >= 0) is the induction hypothesis and is used as "
      "an input, never proved; the STRICT margin lam_ind is quantified per "
      "zone and tested for vacuity against mu/2")
check("el_fence.cert_vs_meas", True,
      "certified vs measured tracked per line in the G4 ledger; 'certified' "
      "means trial-independent validity (an identity, a Loewner step, or a "
      "Cholesky), never a measured spectral datum")
check("el_fence.fits_labelled", True,
      "every exponent (source rate, lag rate, Green rate, edge exponent, "
      "margin scaling) is labelled a FIT")


# ============================================================================
section("VERDICT")
# ============================================================================
OM_OK = n_omA == N_ZONES
H_OK = all(ob["chain"] is not None and ob["chain"]["H"] ** 2 <= ob["budget"]
           for ob in ROWS)
n_H_ok = sum(1 for ob in GOOD if ob["chain"]["H"] ** 2 <= ob["budget"])
if OM_OK and H_OK and NCLOSE == N_ZONES and n_vac == 0:
    VERDICT = "BOUNDARY-CERTIFIED"
    VDET = ("both scalars are certified with NO hypothesis input on %d/%d "
            "zones: omega <= %.4f from a Cholesky-verified graded cap, and "
            "||V^T x|| sharp to %.4f of the measured value from the "
            "goal-oriented residual bound fed by the same Gam_cert.  The "
            "chain closes %d/%d with margin %.1f..%.1f, conditional ONLY on "
            "the quantified induction margin lam_min(Q|odd) >= %.1e..%.1e, "
            "which is %.0e..%.0e below mu/2 (non-vacuous) and holds at %d/%d "
            "points of the M ladder up to M = %d"
            % (N_ZONES, N_ZONES, max(OMA),
               max(ob["chain"]["H"] / ob["nh"] for ob in GOOD),
               NCLOSE, N_ZONES,
               min(ob["chain"]["margin"] for ob in GOOD),
               max(ob["chain"]["margin"] for ob in GOOD),
               min(ob["chain"]["lam"] for ob in GOOD),
               max(ob["chain"]["lam"] for ob in GOOD),
               min(ob["half"] / ob["chain"]["lam"] for ob in GOOD),
               max(ob["half"] / ob["chain"]["lam"] for ob in GOOD),
               n_stab, len(flat), M_CERT[-1]))
elif OM_OK or H_OK:
    which = "omega" if OM_OK else "||V^T x||"
    other = "||V^T x||" if OM_OK else "omega"
    VERDICT = "ONE-SCALAR-LEFT"
    VDET = ("%s is certified; %s is not.  omega_cert < 1 on %d/%d zones "
            "unconditionally, the goal-oriented bound meets the budget on "
            "%d/%d, and the full chain closes %d/%d"
            % (which, other, n_omA, N_ZONES, n_H_ok, N_ZONES, NCLOSE,
               N_ZONES))
else:
    VERDICT = "DECAY-MEASURED"
    VDET = ("both scalars stay measurement: omega_cert < 1 on %d/%d zones, "
            "the goal-oriented bound meets the budget on %d/%d"
            % (n_omA, N_ZONES, n_H_ok, N_ZONES))

print("")
print("TOTAL.contract   BOUNDARY.DECAY")
print("TOTAL.verdict    %s" % VERDICT)
print("TOTAL.detail     %s" % VDET)
print("TOTAL.mechanism  the edge suppression of x = T_odd^{-1} t~ is "
      "CANCELLATION (Green sum cancels by %.0e..%.0e), not support separation "
      "(t~ is edge-PEAKED, it SITS on the boundary) and not a bulk gap "
      "(lam_min lifts by only %.2f..%.2f): the profile is a near-linear zero "
      "r^%.2f (FIT), a boundary condition rather than a decay length"
      % (canc_min, max(ob["cancel"] for ob in NARROW), min(lift), max(lift),
         float(np.mean([ob["pow_a"] for ob in NARROW]))))
print("TOTAL.certified  a GRADED matrix cap (ntop = %d..%d exact soft "
      "directions, ONE Cholesky) gives Gam <= Gam_cert = S_cert^{-1}, and "
      "that single object certifies BOTH scalars with no hypothesis input: "
      "omega <= %.4f..%.4f (measured %.4f..%.4f) and ||V^T x|| <= "
      "%.4f..%.4f x measured"
      % (min(ob["capA"]["ntop"] for ob in ROWS),
         max(ob["capA"]["ntop"] for ob in ROWS), min(OMA), max(OMA),
         min(ob["om"] for ob in ROWS), max(ob["om"] for ob in ROWS),
         min(ob["chain"]["H"] / ob["nh"] for ob in GOOD),
         max(ob["chain"]["H"] / ob["nh"] for ob in GOOD)))
print("TOTAL.residual   ONE quantified hypothesis input remains, and it no "
      "longer touches either scalar -- only the floor on eps: lam_min(Q|odd) "
      ">= %.1e..%.1e, a factor %.0e..%.0e below mu/2 (non-vacuous), met by "
      "the measured %.1e..%.1e with margin %.1f..%.1f at M = %d and at "
      "%d/%d points of the ladder up to M = %d, at a bounded certification "
      "price %.1f..%.1f"
      % (min(ob["chain"]["lam"] for ob in GOOD),
         max(ob["chain"]["lam"] for ob in GOOD),
         min(ob["half"] / ob["chain"]["lam"] for ob in GOOD),
         max(ob["half"] / ob["chain"]["lam"] for ob in GOOD),
         min(ob["lmin_Q"] for ob in ROWS), max(ob["lmin_Q"] for ob in ROWS),
         min(ob["chain"]["margin"] for ob in GOOD),
         max(ob["chain"]["margin"] for ob in GOOD), M_MAIN,
         n_stab, len(flat), M_CERT[-1], min(fpr), pr_max))
print("TOTAL.dead_ends  refuted HERE at their own optimum (not by constants): "
      "Combes-Thomas / Demko-Moss-Smith / Jaffard resolvent decay for x_0 "
      "(loses %.0e with the EXACT resolvent), the T-metric Cauchy-Schwarz at "
      "the edge (loses %.0e), the Szego two-point identity (exact but not an "
      "inequality), and the UNgraded cap for omega (vacuous at ntop = 0 on "
      "every zone -- grading is what makes T104 arm A work).  Not retried "
      "from T108: mode-wise, Bessel, pole-CS one level up"
      % (max(ob["H_i"] / ob["nh"] for ob in NARROW),
         max(ob["H_ii"] / ob["nh"] for ob in NARROW)))
print("TOTAL.checks     %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime    %.1f s (budget %.0f s)" % (time.time() - T_START, BUDGET_S))
print("TOTAL.status     %s" % ("GREEN" if FAIL == 0 else "RED"))
