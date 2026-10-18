"""Discovery probe (2026-07-26), part 97 of the zeta/prime investigation.
Contract RELAY.INDUCTION -- the induction STEP of the staircase as an
ALIGNMENT STATEMENT, tested on the robust O(0.1) quantities of the T96
counterfactual instead of the O(1e-6) margin itself.

THE T93/T95/T96 CONVENTION (declared once, used everywhere)
  f real, supp f subset (-alpha, alpha), ||f||_2 = 1;  h = f * f~ even,
  h(0) = 1, supp h subset (-2 alpha, 2 alpha), h(u) = int f(x) f(x-u) dx.
      P_pole(f) = 2 (int f e^{x/2})(int f e^{-x/2})
      A_arch(f) = (1/2pi) int |fhat(t)|^2 k(t) dt,
                  k(t) = Re psi(1/4 + i t/2) - log pi,  k(0) = -5.3722...,
                  single sign change t0 = 6.28983599...
      Q_k(f)    = P_pole + A_arch - sum_{j<=k} mu_j h_f(log n_j),
                  mu_j = 2 Lambda(n_j) / sqrt(n_j)   (Weil 1952)
  Atoms n = 2,3,4,5 enter the h-support at alpha_k = log(n_k)/2:
      n=2 alpha=0.3465736 mu=0.9802581 | n=3 alpha=0.5493061 mu=1.2685013
      n=4 alpha=0.6931472 mu=0.6931472 | n=5 alpha=0.8047190 mu=1.4395636
  (n=6 carries no von Mangoldt weight; next atom n=7 at alpha=0.9729551.)
  ZONE k := (alpha_free^(k), alpha_{k+1}), the part of the k-th relay zone
  where the atom-k-free form Q_{k-1} is genuinely INDEFINITE.

WHAT T95/T96 LEFT AND WHY THE STRATEGY MOVES
  T95-C1 (proved): the window-truncated shift S_u has ||S_u|| = 1/2 exactly
  when I = (-alpha, alpha-u) and J = I+u are disjoint (alpha <= u), with the
  +-1/2 eigenspaces the symmetric / antisymmetric two-bumps at distance u.
  T96 (measured): deleting atom k sends lambda_min into the -0.4 range, the
  counterfactual loser carries h(log n_k) -> -0.41, the rescue identity holds
  to 5e-15, and every handoff window alpha_free^(k) - alpha_k is positive
  (+0.025/+0.009/+0.011/+0.007) -- but the surviving FULL margin decays like
  exp(-49 alpha), so no lossy induction can ever be closed on it.  Hence this
  probe never chases lambda_min; it works with the O(0.1) objects (mu_k,
  |h| ~ 0.4, block norms) and asks whether "atom k lifts the loser of zone
  k-1" has PROOF SHAPE as an operator statement.

THE BLOCKS
  A  ALIGNMENT.  Sharp constant  c_k := sup{ -Q_{k-1}(f)/|h_f(log n_k)| :
     Q_{k-1}(f) < 0 }.  Two elementary lemmas are stated, proved in the
     docstring of the code and then verified numerically:
       (L1) if the admissible coupling set {mu : Q_{k-1} - mu S_k >= 0} is
            nonempty then EVERY f with Q_{k-1}(f) < 0 has h_f(log n_k) < 0
            (sign alignment is equivalent to a nonempty coupling window);
       (L2) c_k = mu_-^(k) := min{mu >= 0 : Q_{k-1} - mu S_k >= 0}, i.e. the
            sharp alignment constant IS the lower edge of the T95-C2
            admissible coupling window, and c_k <= mu_k^phys is EQUIVALENT
            to lambda_min(Q_k) >= 0 on the loser cone.
     Measured per zone: the pair cloud (Q_{k-1}(f), h_f) on the lowest 16
     eigendirections plus random negative-cone mixtures, the line test
     Q >= -c|h|, mu_-^(k) by bisection, and the two-sided sandwich
     -lambda_min(Q_{k-1})/|h_loser| <= c_k <= mu_k^phys.
  B  REDUCTION.  The atom is DIAGONAL in the exact orthogonal splitting
     L^2(-alpha,alpha) = E_- (+) E_0 (+) E_+ (anti two-bumps / middle /
     symmetric two-bumps): S_k = -1/2 on E_-, 0 on E_0, +1/2 on E_+.  Three
     structural identities are derived and verified exactly on the aligned
     grid: (i) all OLD atoms vanish identically on E_- whenever
     delta = 2 alpha - log n_k < min_j |log n_k - log n_j|, (ii) the pole
     form on E_- is (1 - cosh(u/2)) P_pole(phi) -- the pole RESCUE FLIPS
     SIGN on E_-, (iii) |fhat|^2 = 2(1-cos(t u))|ghat|^2, so the archimedean
     kernel on E_- is k_eff(t) = (1 - cos(t u)) k(t): the t=0 killer k(0) =
     -5.372 is quadratically suppressed.  From this an EXPLICIT lower bound
     is derived (Paley-Wiener mass bound |phihat| <= sqrt(delta) plus the
     classical sign change t0) and its certified sub-zone is reported.
  C  LEDGER.  The exact 3-block picture of the induction step, the E_0 self
     similarity (Q_{k-1}|E_0 is the SAME form at alpha' = log n_k - alpha,
     verified to 1e-12 -- this is the induction hypothesis, at a strictly
     smaller window), the cross-block norms, the 3x3 comparison matrix, and
     the precise reason a norm-based cross-term argument cannot close.

PREREGISTERED VERDICTS
  INDUCTION-SHAPED : (A) sharp numerically + (B) the reduced form provably
                     loses the t=0 killer + the gaps small and named.
  ALIGNMENT-ONLY   : (A) holds, (B) breaks -- with the break located.
  NO-LAW           : no c-law; the alignment is not quantitatively stable.
  Element gates:
    el_firewall : AST scan of this source -- no zero tables, no network, no
                  write-mode file access.
    el_kernel   : vectorised Re psi(1/4+it/2) vs mpmath <= 1e-12, k(0)
                  closed form <= 1e-13, t0 vs the T93 value <= 1e-8.
    el_forms    : PWC arch assembly vs the exact u-space identity by mpmath
                  quadrature <= 1e-10 and vs the t-space digamma integral
                  <= 1e-8; atom Toeplitz vs direct autocorrelation <= 1e-12;
                  pole rank-2 vs direct cell integrals <= 1e-12.
    el_split    : U orthonormal, S_k diagonal (-1/2,0,+1/2) on the split,
                  old atoms vanish on E_-, pole factor (1-cosh(u/2)),
                  Fourier identity |fhat|^2 = 2(1-cos)|ghat|^2, and the E_0
                  self-similarity Q|E_0 = Q at alpha' = log n_k - alpha.
    el_fence    : lambda_min(Q_k) >= -1e-9 at every alpha and every M (an RH
                  fence, never a result).
    el_align    : sign alignment (h_f < 0 on every sampled negative
                  direction), the line test at c = mu_-^(k), the strict
                  window mu_- < mu_phys <= mu_+, and the c-law.
    el_cert     : the explicit E_- bound is a valid lower bound at every
                  tested alpha, and its certified sub-zone is non-trivial.
    el_ledger   : the three atom-shifted diagonal conditions, the failure of
                  the norm-based cross bound, and the sqrt law for the
                  near-null coupling g_0 = ||Q_-0 v_0||.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit,
    no verification/ module, no next.txt edit, no .md output.
  * NO Riemann zero data of any kind; the AST firewall rejects zero-table
    tokens, network imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  A negative
    lambda_min on a genuine window direction is an IMPLEMENTATION SIGNAL,
    fenced, never reported as mathematics.
  * lambda_min^(M) on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound
    for the continuum value: it can refute positivity, never prove it.  The
    explicit E_- bound in block B is the only object here that points the
    other way, and it is quadrature-free (closed-form pole/Cauchy-Schwarz
    plus a 1-D minimisation of an explicit kernel).
  * No "proved" language without a certificate.  Classical anchors cited,
    not re-derived: Weil 1952 (explicit formula), Yoshida 1992 / Bombieri
    2000 / Connes-Consani 2021 (unconditional positivity up to h-support
    log 2), the digamma archimedean kernel, Rayleigh-Ritz, Nystrom
    collocation, Paley-Wiener, Schur/Cauchy-Schwarz block bounds.

OUTCOME OF THIS RUN  =>  ALIGNMENT-ONLY (with a certified E_- half-step)
  105 checks, 0 failures, 37 s, largest array 1400^2.  R1 reproduces the T96
  handoff windows independently (+0.0250/+0.0109/+0.0136/+0.0078 at M = 1400
  against T96's +0.0250/+0.0094/+0.0114/+0.0067 at M = 2400, the drift in the
  direction T96 predicted).
  A  THE ALIGNMENT IS TRUE, SHARP, AND HAS A REAL C-LAW.  Sign alignment
     holds without exception: at all 16 tested alphas every negative
     eigendirection AND every random negative-cone mixture has h_f < 0.  The
     sharp constant is the lower coupling edge, c_k = mu_-^(k) (L2), and the
     physical coupling sits STRICTLY inside the admissible window,
     mu_- < mu_k^phys <= mu_+, in every zone.  The c-law is the SLACK
     s(alpha) = 1 - c_k/mu_k: it is a healthy O(0.1) quantity just past the
     handoff (0.24/0.21/0.28/0.061) and collapses across the zone like
     exp(-44 .. -66 alpha) -- the same exponential scale as T96's exp(-49
     alpha) margin law -- to 1.4e-4 .. 1.3e-3 at the zone top, i.e. the
     alignment is exactly saturated where the next atom takes over.  The
     robust O(0.1) counterfactual data behave as T96 reported: |h_loser| =
     0.09 .. 0.47, -lambda_min(Q_{k-1}) = 0.029 .. 0.63, and the loser's own
     ratio r_k reaches only 0.47 .. 0.95 of mu_k -- the loser is NOT the
     extremal direction for the alignment ratio.
  B  THE REDUCTION DOES WHAT WAS HOPED, AND IT IS THE WRONG TARGET.  All
     three structural identities hold exactly: old atoms vanish on E_- (to
     0.0e+00, under the stated condition delta < min_j |log n_k - log n_j|),
     the pole rescue FLIPS SIGN with factor 1 - cosh(u/2) = -0.061/-0.155/
     -0.250/-0.342 (to 6e-16), and |fhat|^2 = 2(1-cos(tu))|ghat|^2 (to
     3e-15).  So k_eff = (1-cos(tu)) k(t), with inf = -1.110/-1.858/-2.293/
     -2.594 at t = 2.88/2.16/1.79/1.57 against k(0) = -5.372: the t=0 killer
     is provably gone, gain x2.07 .. x4.84.  The explicit bound (that inf,
     the Paley-Wiener mass bound |phihat| <= sqrt(delta), the classical sign
     change t0, and a Cauchy-Schwarz pole bound -- no quadrature anywhere)
     certifies the E_- half-step Q_{k-1}|E_- + mu_k/2 >= 0 on 52%/55%/31%/
     36% of the four zones.  But E_- is not the seat of the negativity:
     Q_{k-1}|E_- is POSITIVE over most of every zone, turns negative only
     near the top, and reaches at most 68% of the sharp constant.
  C  THE OBSTRUCTION IS NAMED, AND IT IS NOT WHERE T96 EXPECTED.  Because
     S_k is diagonal in the splitting, the step is "three diagonal
     conditions + three cross blocks".  All three ATOM-SHIFTED diagonal
     conditions hold at every tested alpha (m_- = 0.15 .. 1.95, m_0 = 6e-6
     .. 0.23, m_+ = 0.013 .. 1.24), so the entire difficulty is in the cross
     blocks -- which the atom cannot touch.  Two diagonal conditions are
     essentially free: E_- is certified in B, and E_0 is the SAME form at
     alpha' = log n_k - alpha < alpha_k (exact to 7e-14) -- literally the
     induction hypothesis at a strictly smaller window.  The cross norms are
     large (||Q_-0|| = 0.83 .. 1.27, ||Q_0+|| = 0.77 .. 1.18), so the 3x3
     comparison matrix is negative in every zone (-0.84 .. -1.74): a lossy,
     norm-based cross bound is dead, as T96 already suspected on other
     grounds.  What is new is the replacement object.  With Q|E_0 > 0 the
     step is a SCHUR statement, dominated by the near-null mode v_0 of the
     smaller problem with weight g_0^2/lambda_0, g_0 = ||Q_-0 v_0||, and the
     measurement gives a clean law: g_0/sqrt(lambda_0) stays in [0.13, 1.30]
     while lambda_0 sweeps 4.5 decades (6e-6 .. 2e-1).  The Schur weight is
     therefore O(1) -- 0.02 .. 1.68, the same size as the atom's own gain
     mu_k/2 = 0.35 .. 0.72 on E_-.  THE MISSING LEMMA IS EXACTLY THIS: an
     explicit constant C with ||Q_-0 v_0||^2 <= C lambda_0 and C small
     enough that mu_k/2 + lambda_min(Q|E_-) beats it.  That is a statement
     about one vector (the near-null mode of the previous zone) and one
     block, not about the whole form -- and it is lossless by construction,
     which is what the exponentially decaying margin demands.
"""
import ast
import math
import os
import time

import mpmath
import numpy as np
from scipy.linalg import eigh, eigvalsh

PASS = 0
FAIL = 0
T_START = time.time()
mpmath.mp.dps = 30

EULER = float(mpmath.euler)
LOG_PI = math.log(math.pi)
K0_CLOSED = -EULER - 3.0 * math.log(2.0) - math.pi / 2.0 - LOG_PI
T0_REF = 6.28983599
MAX_ARRAY = 2400

# (n, log n, mu_n = 2 Lambda(n)/sqrt(n))
ATOMS = (
    (2, math.log(2.0), 2.0 * math.log(2.0) / math.sqrt(2.0)),
    (3, math.log(3.0), 2.0 * math.log(3.0) / math.sqrt(3.0)),
    (4, math.log(4.0), 2.0 * math.log(2.0) / 2.0),
    (5, math.log(5.0), 2.0 * math.log(5.0) / math.sqrt(5.0)),
)
ALPHA_NEXT_ATOM = math.log(7.0) / 2.0
T96_HANDOFF = (0.0250, 0.0094, 0.0114, 0.0067)
FENCE = -1e-9

GLX, GLW = np.polynomial.legendre.leggauss(24)


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-30s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-30s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------------
# el_firewall -- AST scan of this source
# ----------------------------------------------------------------------------
# assembled from fragments so that the scan cannot trip over its own blacklist
FORBIDDEN_TOKENS = tuple("".join(parts) for parts in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
    ("25.01", "0857"), ("30.42", "4876"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "mpmath", "numpy", "scipy"}


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
    check("el_firewall.imports", not bad_imports, "non-whitelisted: %s" % (bad_imports or "none"))
    check("el_firewall.writes", not bad_writes, "write-mode open calls: %d" % len(bad_writes))


# ----------------------------------------------------------------------------
# archimedean kernel
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


def kernel_k_scalar(t):
    return float(kernel_k(np.array([float(t)]))[0])


# ----------------------------------------------------------------------------
# PWC Nystrom/Galerkin assembly on (-alpha, alpha) with M cells
#   basis  phi_i = 1_{cell i} / sqrt(d),  d = 2 alpha / M   (orthonormal)
# ----------------------------------------------------------------------------
_IDX_CACHE = {}


def index_matrix(M):
    if M not in _IDX_CACHE:
        if len(_IDX_CACHE) > 3:
            _IDX_CACHE.clear()
        i = np.arange(M, dtype=np.int32)
        _IDX_CACHE[M] = np.abs(i[:, None] - i[None, :])
    return _IDX_CACHE[M]


def arch_symbol(alpha, M):
    """Symmetric-Toeplitz symbol t[p] of A_arch in the PWC basis (exact)."""
    assert M <= MAX_ARRAY
    d = 2.0 * alpha / M
    b = 2.0 * alpha
    s = (GLX + 1.0) / 2.0
    wq = GLW / 2.0 * d
    U = (np.arange(M)[:, None] + s[None, :]) * d
    W = 2.0 * np.exp(-U / 2.0) / (-np.expm1(-2.0 * U))
    S = np.broadcast_to(s[None, :], U.shape)
    rise = (wq[None, :] * W * S).sum(axis=1)
    fall = (wq[None, :] * W * (1.0 - S)).sum(axis=1)
    lam = np.zeros(M + 1)
    lam[0] = fall[0]
    lam[1:M] = rise[0:M - 1] + fall[1:M]
    reg0 = float((wq * W[0] * (np.expm1(-1.5 * U[0]) + s)).sum())
    rest = float((wq[None, :] * W[1:] * np.exp(-1.5 * U[1:])).sum())
    Cb = -EULER - LOG_PI - math.log(-np.expm1(-2.0 * b))
    t = np.zeros(M)
    t[0] = Cb + reg0 + rest
    t[1:] = -0.5 * lam[1:M]
    return t


def atom_symbol(u, alpha, M):
    """Symmetric-Toeplitz symbol of f -> h_f(u) in the PWC basis (exact)."""
    d = 2.0 * alpha / M
    q = u / d
    qr = round(q)
    if abs(q - qr) < 1e-9:
        m, th = int(qr), 0.0
    else:
        m, th = int(math.floor(q)), q - math.floor(q)
    t = np.zeros(M)
    if m == 0:
        t[0] = 1.0 - th
        if M > 1:
            t[1] += 0.5 * th
    else:
        if m < M:
            t[m] += 0.5 * (1.0 - th)
        if m + 1 < M:
            t[m + 1] += 0.5 * th
    return t


def pole_vectors(alpha, M):
    d = 2.0 * alpha / M
    x = -alpha + d * np.arange(M + 1)
    a = 2.0 * (np.exp(x[1:] / 2.0) - np.exp(x[:-1] / 2.0)) / math.sqrt(d)
    b = 2.0 * (np.exp(-x[:-1] / 2.0) - np.exp(-x[1:] / 2.0)) / math.sqrt(d)
    return a, b


def prime_free_matrix(alpha, M):
    idx = index_matrix(M)
    A = arch_symbol(alpha, M)[idx]
    a, b = pole_vectors(alpha, M)
    P = np.outer(a, b)
    return A + P + P.T


def atom_matrix(u, alpha, M):
    return atom_symbol(u, alpha, M)[index_matrix(M)]


def zone_forms(kidx, alpha, M):
    """Q_{k-1} (atoms j<k) and S_k for zone kidx (0-based)."""
    Q = prime_free_matrix(alpha, M)
    for (_n, u, mu) in ATOMS[:kidx]:
        Q -= mu * atom_matrix(u, alpha, M)
    Sk = atom_matrix(ATOMS[kidx][1], alpha, M)
    return Q, Sk


def lam_min(Mx):
    return float(eigvalsh(Mx, subset_by_index=[0, 0])[0])


# ----------------------------------------------------------------------------
# el_kernel / el_forms
# ----------------------------------------------------------------------------
def gate_kernel():
    ts = np.array([0.0, 0.37, 1.0, 2.5, 6.28983599, 13.7, 41.0, 260.0])
    ref = np.array([float(mpmath.re(mpmath.digamma(mpmath.mpf(0.25) + 0.5j * mpmath.mpf(t))))
                    - LOG_PI for t in ts])
    err = float(np.max(np.abs(kernel_k(ts) - ref)))
    check("el_kernel.digamma", err <= 1e-12, "max |k - mpmath| = %.2e" % err)
    e0 = abs(kernel_k_scalar(0.0) - K0_CLOSED)
    check("el_kernel.k0", e0 <= 1e-13, "k(0) = %.10f, |err| = %.2e" % (K0_CLOSED, e0))
    lo, hi = 6.0, 7.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if kernel_k_scalar(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    t0 = 0.5 * (lo + hi)
    check("el_kernel.t0", abs(t0 - T0_REF) <= 1e-8, "t0 = %.9f" % t0)
    return t0


def arch_flat_uspace(alpha):
    """A_arch of the flat window by mpmath quadrature of the exact u-identity."""
    b = 2 * mpmath.mpf(alpha)
    w = lambda u: 2 * mpmath.e ** (-u / 2) / (1 - mpmath.e ** (-2 * u))
    hh = lambda u: 1 - u / b
    Cb = -mpmath.euler - mpmath.log(mpmath.pi) - mpmath.log(1 - mpmath.e ** (-2 * b))
    integ = lambda u: w(u) * (mpmath.e ** (mpmath.mpf(-3) * u / 2) - hh(u))
    val = Cb + mpmath.quad(integ, [0, b / 8, b / 2, b])
    return float(val)


def arch_flat_tspace(alpha, T=2000.0, sub=4):
    """Same quantity in t-space: (1/(pi alpha)) int_0^inf (1-cos(2 a t)) k/t^2.
    The endpoint is snapped to a full period of cos(2 alpha t) so that the
    leading oscillatory tail term sin(2 alpha T) k(T)/(2 alpha T^2) vanishes."""
    per = math.pi / alpha
    nper = int(math.ceil(T / per))
    nseg = nper * sub
    edges = np.linspace(0.0, nper * per, nseg + 1)
    tot = 0.0
    for i in range(nseg):
        lo, hi = edges[i], edges[i + 1]
        tt = 0.5 * (hi - lo) * GLX + 0.5 * (hi + lo)
        ww = 0.5 * (hi - lo) * GLW
        val = (1.0 - np.cos(2.0 * alpha * tt)) * kernel_k(tt) / (tt * tt)
        tot += float((ww * val).sum())
    Te = edges[-1]
    tail = (math.log(Te / 2.0) - LOG_PI + 1.0) / Te
    return (tot + tail) / (math.pi * alpha)


def gate_forms():
    alpha, M = 0.31, 400
    t = arch_symbol(alpha, M)
    c = np.full(M, 1.0 / math.sqrt(M))          # flat window, ||f|| = 1
    A_disc = float(c @ (t[index_matrix(M)] @ c))
    A_u = arch_flat_uspace(alpha)
    A_t = arch_flat_tspace(alpha)
    check("el_forms.arch_uspace", abs(A_disc - A_u) <= 1e-10,
          "PWC %.12f vs mpmath %.12f (d=%.2e)" % (A_disc, A_u, abs(A_disc - A_u)))
    check("el_forms.arch_tspace", abs(A_u - A_t) <= 1e-8,
          "u-space vs t-space  d = %.2e" % abs(A_u - A_t))
    rng = np.random.default_rng(9701)
    v = rng.normal(size=M)
    v /= np.linalg.norm(v)
    d = 2.0 * alpha / M
    worst = 0.0
    for u in (0.2, 0.37, 2.0 * alpha - 0.031):   # inside the h-support 2 alpha
        q = u / d
        m0 = int(math.floor(q))
        th = q - m0
        direct = (1.0 - th) * float(v[m0:] @ v[:M - m0])
        if m0 + 1 < M:
            direct += th * float(v[m0 + 1:] @ v[:M - m0 - 1])
        mat = float(v @ (atom_matrix(u, alpha, M) @ v))
        worst = max(worst, abs(direct - mat))
    check("el_forms.atom_toeplitz", worst <= 1e-12, "max |Toeplitz - direct| = %.2e" % worst)
    a, b = pole_vectors(alpha, M)
    xs = -alpha + d * np.arange(M + 1)
    a_ref = np.array([float(mpmath.quad(lambda x: mpmath.e ** (x / 2), [xs[i], xs[i + 1]]))
                      for i in range(0, M, 97)]) / math.sqrt(d)
    e_pole = float(np.max(np.abs(a[::97] - a_ref)))
    check("el_forms.pole_cells", e_pole <= 1e-12, "max |cell int - mpmath| = %.2e" % e_pole)


# ----------------------------------------------------------------------------
# aligned grid + the exact E_- / E_0 / E_+ splitting
# ----------------------------------------------------------------------------
def aligned_grid(alpha_target, u, cells_target=1200):
    """d = u/m exactly, M cells; returns (alpha_snapped, M, m)."""
    d0 = 2.0 * alpha_target / cells_target
    m = max(4, int(round(u / d0)))
    d = u / m
    M = int(round(2.0 * alpha_target / d))
    M = min(M, MAX_ARRAY, 2 * m - 2)
    return 0.5 * M * d, M, m


def split_basis(M, m):
    """Orthonormal U = [E_- | E_0 | E_+]; nI = M-m anti/sym pairs."""
    nI = M - m
    n0 = M - 2 * nI
    U = np.zeros((M, M))
    r = 1.0 / math.sqrt(2.0)
    j = np.arange(nI)
    U[j, j] = r
    U[j + m, j] = -r
    U[np.arange(nI, m), np.arange(nI, nI + n0)] = 1.0
    U[j, nI + n0 + j] = r
    U[j + m, nI + n0 + j] = r
    return U, nI, n0


# ----------------------------------------------------------------------------
# block A -- the alignment statement
# ----------------------------------------------------------------------------
def coupling_edge(Q, S, lo, hi, steps):
    """bisect for the mu where lam_min(Q - mu S) changes sign (lam(lo)<0<=lam(hi))."""
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        if lam_min(Q - mid * S) < 0.0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def alpha_free(kidx, M, alo, ahi, steps=15):
    """largest alpha with lam_min(Q_{k-1}) >= 0, by bisection."""
    for _ in range(steps):
        mid = 0.5 * (alo + ahi)
        Q, _S = zone_forms(kidx, mid, M)
        if lam_min(Q) >= 0.0:
            alo = mid
        else:
            ahi = mid
    return 0.5 * (alo + ahi)


def main():
    section("RELAY.INDUCTION -- part 97 -- gates")
    firewall()
    t0 = gate_kernel()
    gate_forms()

    # ---------------------------------------------------------------- R1 map
    section("R1  ZONE MAP -- where Q_{k-1} is genuinely indefinite")
    zones = []
    for kidx, (n, u, mu) in enumerate(ATOMS):
        ak = 0.5 * u
        anext = 0.5 * ATOMS[kidx + 1][1] if kidx + 1 < len(ATOMS) else ALPHA_NEXT_ATOM
        af = {}
        for M in (800, 1400):
            af[M] = alpha_free(kidx, M, ak + 2e-4, anext - 1e-3)
        hand = af[1400] - ak
        zones.append(dict(kidx=kidx, n=n, u=u, mu=mu, ak=ak, anext=anext, af=af[1400]))
        info("zone n=%d" % n,
             "alpha_k=%.6f  alpha_free(M=800/1400)=%.6f/%.6f  handoff=%+.4f (T96 %+.4f)"
             % (ak, af[800], af[1400], hand, T96_HANDOFF[kidx]))
        check("el_anchor.handoff n=%d" % n, hand > 0.0 and abs(hand - T96_HANDOFF[kidx]) < 0.02,
              "window %+.4f, drift vs M %.1e" % (hand, abs(af[800] - af[1400])))

    # ---------------------------------------------------------------- R2 (A)
    section("R2  (A) ALIGNMENT -- sharp constant c_k = mu_-^(k)")
    print("  L1  {mu : Q - mu S >= 0} nonempty  =>  Q(f)<0 implies h_f<0.")
    print("      (Q >= mu S pointwise; h_f>0 would force Q(f) >= mu h_f > 0.)")
    print("  L2  c_k := sup{-Q(f)/|h_f| : Q(f)<0} = mu_- = min{mu: Q - mu S >= 0}.")
    print("      (<=: at mu_-, Q(f) >= mu_- h_f = -mu_-|h_f| on the cone;  >=: at the")
    print("       edge dlam/dmu = -h > 0, so directions just below mu_- realise it.)")
    print("      Hence  c_k <= mu_k^phys  <=>  atom k lifts every loser of zone k-1.")
    align_rows = []
    rng = np.random.default_rng(31337)
    for z in zones:
        kidx, u, mu, n = z["kidx"], z["u"], z["mu"], z["n"]
        lo_a, hi_a = z["af"] + 0.15 * (z["anext"] - z["af"]), z["anext"] - 0.02 * (z["anext"] - z["af"])
        for frac in (0.0, 0.35, 0.7, 1.0):
            alpha = lo_a + frac * (hi_a - lo_a)
            M = min(MAX_ARRAY, int(round(2.0 * alpha / 1.4e-3)))
            Q, S = zone_forms(kidx, alpha, M)
            Qk = Q - mu * S
            lk = lam_min(Qk)
            check("el_fence n=%d a=%.3f" % (n, alpha), lk >= FENCE, "lam_min(Q_k) = %+.3e" % lk)
            w, V = eigh(Q, subset_by_index=[0, 15])
            if w[0] >= 0.0:
                info("  n=%d a=%.4f" % (n, alpha), "not indefinite at M=%d -- skipped" % M)
                continue
            hs = np.einsum("ij,ij->j", V, S @ V)
            neg = w < 0.0
            ratios = -w[neg] / np.abs(hs[neg])
            sgn_ok = bool(np.all(hs[neg] < 0.0))
            # random negative-cone mixtures inside the lowest block
            C = rng.normal(size=(V.shape[1], 400))
            C /= np.linalg.norm(C, axis=0)
            F = V @ C
            qf = np.einsum("ij,ij->j", F, Q @ F)
            hf = np.einsum("ij,ij->j", F, S @ F)
            sel = qf < 0.0
            sgn_ok = sgn_ok and bool(np.all(hf[sel] < 0.0))
            rat_mix = -qf[sel] / np.abs(hf[sel]) if sel.any() else np.array([0.0])
            cmax = float(max(ratios.max() if neg.any() else 0.0, rat_mix.max()))
            mlo, mhi = coupling_edge(Q, S, 0.0, mu, 16)
            plo, phi_ = mu, mu
            while lam_min(Q - phi_ * S) >= 0.0 and phi_ < mu + 8.0:
                plo, phi_ = phi_, phi_ + 0.5
            mplo, mphi = coupling_edge(Q, S, phi_, plo, 10) if phi_ > plo else (mu, mu)
            hloser = float(hs[0])
            rk = -float(w[0]) / abs(hloser)
            align_rows.append((n, alpha, float(w[0]), hloser, rk, mhi, mu, mphi, lk,
                               int(neg.sum())))
            check("el_align.sign n=%d a=%.3f" % (n, alpha), sgn_ok,
                  "%d neg eigendirs + %d mixtures, all h<0" % (int(neg.sum()), int(sel.sum())))
            check("el_align.line n=%d a=%.3f" % (n, alpha), cmax <= mhi + 1e-6 and cmax <= mu,
                  "max ratio %.6f <= mu_- %.6f <= mu_phys %.6f" % (cmax, mhi, mu))
            info("  n=%d a=%.4f" % (n, alpha),
                 "lam(Q_{k-1})=%+.4f h_loser=%+.4f r_k=%.6f mu_-=%.6f mu_+=%.3f dim_neg>=%d"
                 % (w[0], hloser, rk, mhi, mphi, int(neg.sum())))
    print("")
    print("  c-law over the zones (sandwich  r_k <= c_k = mu_- <= mu_phys):")
    print("   n   alpha    -lam(Q_{k-1})  |h_loser|   r_k/mu    1-mu_-/mu   lam_min(Q_k)")
    for (n, alpha, lam1, hl, rk, mhi, mu, mphi, lk, nneg) in align_rows:
        print("  %2d  %.4f   %11.6f  %9.6f  %8.6f  %10.2e  %+.3e"
              % (n, alpha, -lam1, abs(hl), rk / mu, 1.0 - mhi / mu, lk))
    print("")
    print("  the c-law: the alignment SLACK  s(alpha) = 1 - c_k/mu_k^phys  per zone")
    slack_top, rates = {}, {}
    for z in zones:
        rows = [r for r in align_rows if r[0] == z["n"]]
        sl = [1.0 - r[5] / r[6] for r in rows]
        aa = [r[1] for r in rows]
        rates[z["n"]] = math.log(sl[0] / sl[-1]) / (aa[-1] - aa[0])
        slack_top[z["n"]] = sl[-1]
        info("c-law n=%d" % z["n"],
             "s = %.3e -> %.3e over alpha %.4f..%.4f  =>  s ~ exp(-%.1f alpha)"
             % (sl[0], sl[-1], aa[0], aa[-1], rates[z["n"]]))
    check("el_align.window", all(0.0 < r[5] < r[6] <= r[7] for r in align_rows),
          "mu_- < mu_phys <= mu_+ strictly at every tested alpha")
    check("el_align.claw", all(v < 2e-3 for v in slack_top.values())
          and all(v > 20.0 for v in rates.values()),
          "slack at the zone top %.1e .. %.1e, decay rates %.0f .. %.0f"
          % (min(slack_top.values()), max(slack_top.values()),
             min(rates.values()), max(rates.values())))

    # ---------------------------------------------------------------- R3 (B)
    section("R3  (B) REDUCTION -- the exact splitting and the loss of the t=0 killer")
    kmins = {}
    tg = np.linspace(1e-6, t0, 40000)
    kt = kernel_k(tg)
    for (n, u, mu) in ATOMS:
        vals = (1.0 - np.cos(tg * u)) * kt
        i = int(np.argmin(vals))
        lo, hi = tg[max(i - 1, 0)], tg[min(i + 1, len(tg) - 1)]
        for _ in range(200):
            m1 = lo + (hi - lo) / 3.0
            m2 = hi - (hi - lo) / 3.0
            f1 = (1.0 - math.cos(m1 * u)) * kernel_k_scalar(m1)
            f2 = (1.0 - math.cos(m2 * u)) * kernel_k_scalar(m2)
            if f1 < f2:
                hi = m2
            else:
                lo = m1
        tm = 0.5 * (lo + hi)
        kmins[n] = ((1.0 - math.cos(tm * u)) * kernel_k_scalar(tm), tm)
        info("k_eff n=%d" % n,
             "inf_t (1-cos(t log n)) k(t) = %+.6f at t = %.4f   (k(0) = %+.6f, gain x%.2f)"
             % (kmins[n][0], tm, K0_CLOSED, abs(K0_CLOSED / kmins[n][0])))
    print("")
    print("  E_- lower bound (explicit, quadrature-free):")
    print("    Q_{k-1}|E_-(phi) = (1-cosh(u/2)) P_pole(phi) + (1/2pi) int k_eff |phihat|^2")
    print("    >= -(cosh(u/2)-1) 2 sqrt(J_+ J_-)  +  K_min(u) min(1, t0 delta/pi) =: B(alpha)")
    print("    J_+- = int_I e^{+-x}dx,  |phihat| <= sqrt(delta) (Cauchy-Schwarz),  k>=0 for")
    print("    |t|>=t0 (classical single sign change).  Target: B >= -mu_k/2.")
    ledger = []
    for z in zones:
        kidx, u, mu, n = z["kidx"], z["u"], z["mu"], z["n"]
        lo_a = z["af"] + 0.15 * (z["anext"] - z["af"])
        hi_a = z["anext"] - 0.02 * (z["anext"] - z["af"])
        for frac in (0.0, 0.5, 1.0):
            at = lo_a + frac * (hi_a - lo_a)
            alpha, M, m = aligned_grid(at, u, 1150)
            Q, S = zone_forms(kidx, alpha, M)
            U, nI, n0 = split_basis(M, m)
            delta = 2.0 * alpha - u
            # structural gates
            e_orth = float(np.max(np.abs(U.T @ U - np.eye(M))))
            Sb = U.T @ (S @ U)
            diag_ref = np.concatenate([-0.5 * np.ones(nI), np.zeros(n0), 0.5 * np.ones(nI)])
            e_diag = float(np.max(np.abs(Sb - np.diag(diag_ref))))
            QB = U.T @ (Q @ U)
            Qmm = QB[:nI, :nI]
            Q00 = QB[nI:nI + n0, nI:nI + n0]
            Qpp = QB[nI + n0:, nI + n0:]
            Qm0 = QB[:nI, nI:nI + n0]
            Qmp = QB[:nI, nI + n0:]
            Q0p = QB[nI:nI + n0, nI + n0:]
            if frac == 0.0:
                check("el_split.orth n=%d" % n, e_orth <= 1e-13, "|U^T U - I| = %.1e" % e_orth)
                check("el_split.atom_diag n=%d" % n, e_diag <= 1e-13,
                      "S = diag(-1/2, 0, +1/2) to %.1e" % e_diag)
                # old atoms vanish on E_-
                gap = min([abs(u - uj) for (_nj, uj, _mj) in ATOMS[:kidx]] + [ATOMS[0][1]]) \
                    if kidx else ATOMS[0][1]
                worst = 0.0
                for (_nj, uj, _mj) in ATOMS[:kidx]:
                    Sj = atom_matrix(uj, alpha, M)
                    worst = max(worst, float(np.max(np.abs(U[:, :nI].T @ (Sj @ U[:, :nI])))))
                check("el_split.old_atoms n=%d" % n, worst <= 1e-13 or delta >= gap,
                      "delta=%.4f < gap=%.4f, max |S_j|E_-| = %.1e" % (delta, gap, worst))
                # pole factor
                a_v, b_v = pole_vectors(alpha, M)
                Pm = U[:, :nI].T @ (np.outer(a_v, b_v) + np.outer(b_v, a_v)) @ U[:, :nI]
                aI, bI = a_v[:nI], b_v[:nI]
                PI = np.outer(aI, bI) + np.outer(bI, aI)
                e_pole = float(np.max(np.abs(Pm - (1.0 - math.cosh(u / 2.0)) * PI)))
                check("el_split.pole_flip n=%d" % n, e_pole <= 1e-11,
                      "P|E_- = (1-cosh(u/2)) P_I  to %.1e  [factor %+.4f]"
                      % (e_pole, 1.0 - math.cosh(u / 2.0)))
                # Fourier identity |fhat|^2 = 2(1-cos(tu)) |ghat|^2
                d = 2.0 * alpha / M
                gg = rng.normal(size=nI)
                ff = np.zeros(M)
                ff[:nI] += gg
                ff[m:m + nI] -= gg
                tt = np.linspace(0.05, 60.0, 250)
                xs = -alpha + d * (np.arange(M) + 0.5)
                cell = 2.0 * np.sin(tt * d / 2.0) / (tt * math.sqrt(d))
                Fg = cell * np.abs(np.exp(-1j * np.outer(tt, xs[:nI])) @ gg)
                Ff = cell * np.abs(np.exp(-1j * np.outer(tt, xs)) @ ff)
                e_four = float(np.max(np.abs(Ff ** 2 - 2.0 * (1.0 - np.cos(tt * u)) * Fg ** 2)))
                check("el_split.fourier n=%d" % n, e_four <= 1e-10,
                      "|fhat|^2 = 2(1-cos) |ghat|^2 to %.1e" % e_four)
                # E_0 self-similarity: Q|E_0 is the same form at alpha' = u - alpha
                ap = u - alpha
                Qs = prime_free_matrix(ap, n0)
                for (_nj, uj, muj) in ATOMS[:kidx]:
                    Qs -= muj * atom_matrix(uj, ap, n0)
                e_self = float(np.max(np.abs(Qs - Q00)))
                check("el_split.self_similar n=%d" % n, e_self <= 1e-11,
                      "Q|E_0 = Q_{k-1}(alpha'=%.5f) to %.1e  [alpha_k=%.5f]"
                      % (ap, e_self, z["ak"]))
            # certified bound on E_-
            Jp = math.exp(alpha - u) - math.exp(-alpha)
            Jm = math.exp(alpha) - math.exp(u - alpha)
            Kmin = kmins[n][0]
            B = -(math.cosh(u / 2.0) - 1.0) * 2.0 * math.sqrt(Jp * Jm) \
                + Kmin * min(1.0, t0 * delta / math.pi)
            lmm = lam_min(Qmm)
            check("el_cert n=%d a=%.3f" % (n, alpha), B <= lmm + 1e-12,
                  "B = %+.5f <= lam_min(Q|E_-) = %+.5f" % (B, lmm))
            cE = -2.0 * lmm
            l00 = lam_min(Q00)
            lpp = lam_min(Qpp)
            nm0 = float(np.linalg.norm(Qm0, 2))
            nmp = float(np.linalg.norm(Qmp, 2))
            n0p = float(np.linalg.norm(Q0p, 2))
            ledger.append(dict(n=n, alpha=alpha, delta=delta, M=M, nI=nI, n0=n0, B=B,
                               lmm=lmm, cE=cE, l00=l00, lpp=lpp, mu=mu,
                               nm0=nm0, nmp=nmp, n0p=n0p, cert=(-2.0 * B <= mu)))
            info("  n=%d a=%.4f" % (n, alpha),
                 "delta=%.4f M=%d dimE_-=%d dimE_0=%d  B=%+.4f  lam|E_-=%+.4f  "
                 "c_E/mu=%.3f  cert=%s" % (delta, M, nI, n0, B, lmm, cE / mu,
                                           "yes" if -2.0 * B <= mu else "no"))
    print("")
    print("  certified sub-zone per zone (largest delta with -2B <= mu_k):")
    cert_frac = {}
    for z in zones:
        n, u, mu = z["n"], z["u"], z["mu"]
        Kmin = kmins[n][0]
        lo_d, hi_d = 0.0, 2.0 * z["anext"] - u
        for _ in range(60):
            md = 0.5 * (lo_d + hi_d)
            al = 0.5 * (u + md)
            Jp = math.exp(al - u) - math.exp(-al)
            Jm = math.exp(al) - math.exp(u - al)
            Bv = -(math.cosh(u / 2.0) - 1.0) * 2.0 * math.sqrt(Jp * Jm) \
                + Kmin * min(1.0, t0 * md / math.pi)
            if -2.0 * Bv <= mu:
                lo_d = md
            else:
                hi_d = md
        a_cert = 0.5 * (u + lo_d)
        span = z["anext"] - z["ak"]
        frac = max(0.0, min(1.0, (a_cert - z["ak"]) / span))
        cert_frac[n] = frac
        info("cert n=%d" % n, "alpha <= %.4f (delta <= %.4f) = %.0f%% of the zone (%.4f..%.4f)"
             % (a_cert, lo_d, 100.0 * frac, z["ak"], z["anext"]))
    check("el_cert.subzone", all(v > 0.25 for v in cert_frac.values()),
          "explicit E_- certificate covers %.0f%%..%.0f%% of the four zones"
          % (100.0 * min(cert_frac.values()), 100.0 * max(cert_frac.values())))

    # ---------------------------------------------------------------- R4 (C)
    section("R4  (C) GAP LEDGER -- the 3-block form of the induction step")
    print("  S_k is DIAGONAL in the splitting, so  Q_k = Q_{k-1} - mu_k S_k  is")
    print("    E_- block : Q|E_- + mu_k/2      (certified above on a sub-zone)")
    print("    E_0 block : Q|E_0               (= the SAME form at alpha' < alpha_k:")
    print("                                     the induction hypothesis, verified)")
    print("    E_+ block : Q|E_+ - mu_k/2      (T95-C1's sharp necessary condition)")
    print("    + three cross blocks, untouched by the atom.")
    print("")
    print("   n   alpha   delta   m_-=lam|E_-+mu/2  m_0=lam|E_0  m_+=lam|E_+-mu/2 "
          " ||Q_-0||  ||Q_-+||  ||Q_0+||  lam_min(3x3)")
    worst_cmp = 1.0
    for r in ledger:
        mm = r["lmm"] + 0.5 * r["mu"]
        m0 = r["l00"]
        mp = r["lpp"] - 0.5 * r["mu"]
        C = np.array([[mm, -r["nm0"], -r["nmp"]],
                      [-r["nm0"], m0, -r["n0p"]],
                      [-r["nmp"], -r["n0p"], mp]])
        lc = float(np.linalg.eigvalsh(C)[0])
        worst_cmp = min(worst_cmp, lc)
        print("  %2d  %.4f  %.4f  %14.5f  %11.3e  %14.5f  %8.4f  %8.4f  %8.4f  %+.4f"
              % (r["n"], r["alpha"], r["delta"], mm, m0, mp,
                 r["nm0"], r["nmp"], r["n0p"], lc))
    check("el_ledger.diagonal", all(r["lmm"] + 0.5 * r["mu"] > 0.0 for r in ledger)
          and all(r["l00"] >= FENCE for r in ledger)
          and all(r["lpp"] - 0.5 * r["mu"] > 0.0 for r in ledger),
          "all three diagonal conditions hold at every tested alpha")
    check("el_ledger.norm_route_fails", worst_cmp < 0.0,
          "min lam(3x3 comparison matrix) = %+.4f -- the lossy route cannot close"
          % worst_cmp)

    print("")
    print("  All three ATOM-SHIFTED diagonal blocks above are positive, so whatever")
    print("  negativity Q_k could still have must come from the cross blocks -- and the")
    print("  cross blocks are untouched by the atom.  Hence the step is a SCHUR")
    print("  statement: with Q|E_0 > 0 invertible, Q_k >= 0 is equivalent to")
    print("     [Q|E_- + mu/2 ,  Q_-+ ; Q_+- , Q|E_+ - mu/2]  -  X^T (Q|E_0)^{-1} X >= 0,")
    print("  X = [Q_0- , Q_0+].  lambda_min(Q|E_0) is the margin of the SMALLER problem")
    print("  (~1e-5), so the near-null mode v_0 dominates the correction with weight")
    print("  g_0^2/lambda_0, g_0 = ||Q_-0 v_0||.  Finiteness forces g_0 = O(sqrt(lambda_0)).")
    print("")
    print("  (diag / cross = the block-diagonal and cross-block parts of Q_{k-1} at its")
    print("   own loser; lam_0 = margin of the SMALLER problem, g_0 = ||Q_-0 v_0||.)")
    print("   n   alpha   w(E_-)  w(E_0)  w(E_+)   diag     cross    lam_0      g_0"
          "      g_0^2/lam_0  g_0/sqrt(lam_0)")
    schur_ratio, schur_ratio_lo, cross_ok, pure_off = 0.0, 1e9, True, 0
    schur_w = []
    for z in zones:
        kidx, u, mu, n = z["kidx"], z["u"], z["mu"], z["n"]
        lo_a = z["af"] + 0.15 * (z["anext"] - z["af"])
        hi_a = z["anext"] - 0.02 * (z["anext"] - z["af"])
        for frac in (0.0, 1.0):
            at = lo_a + frac * (hi_a - lo_a)
            alpha, M, m = aligned_grid(at, u, 1150)
            Q, _S = zone_forms(kidx, alpha, M)
            U, nI, n0 = split_basis(M, m)
            w1, V1 = eigh(Q, subset_by_index=[0, 0])
            cB = U.T @ V1[:, 0]
            fm, f0, fp = cB[:nI], cB[nI:nI + n0], cB[nI + n0:]
            wm, w0, wp = float(fm @ fm), float(f0 @ f0), float(fp @ fp)
            QB = U.T @ (Q @ U)
            Qmm = QB[:nI, :nI]
            Q00 = QB[nI:nI + n0, nI:nI + n0]
            Qpp = QB[nI + n0:, nI + n0:]
            Qm0 = QB[:nI, nI:nI + n0]
            diag = float(fm @ (Qmm @ fm) + f0 @ (Q00 @ f0) + fp @ (Qpp @ fp))
            cross = float(w1[0]) - diag
            e0, v0 = eigh(Q00, subset_by_index=[0, 0])
            lam0 = float(e0[0])
            g0 = float(np.linalg.norm(Qm0 @ v0[:, 0]))
            cross_ok = cross_ok and cross < 0.0
            pure_off += 1 if diag > 0.0 else 0
            schur_ratio = max(schur_ratio, g0 / math.sqrt(lam0))
            schur_ratio_lo = min(schur_ratio_lo, g0 / math.sqrt(lam0))
            schur_w.append(g0 * g0 / lam0)
            print("  %2d  %.4f  %.4f  %.4f  %.4f  %+.4f  %+.4f  %.3e  %.3e  %10.4f  %10.3f"
                  % (n, alpha, wm, w0, wp, diag, cross, lam0, g0, g0 * g0 / lam0,
                     g0 / math.sqrt(lam0)))
    check("el_ledger.cross_carries", cross_ok,
          "cross part < 0 at all 8 alphas; diagonal part still > 0 at %d of them "
          "(there the negativity is PURELY off-diagonal)" % pure_off)
    check("el_ledger.sqrt_law", 0.1 < schur_ratio_lo and schur_ratio < 2.0,
          "g_0/sqrt(lam_0) in [%.2f, %.2f] while lam_0 sweeps 6e-6..2e-1: the near-null "
          "coupling obeys g_0 = O(sqrt(lam_0))" % (schur_ratio_lo, schur_ratio))

    # ---------------------------------------------------------------- verdict
    section("VERDICT")
    a_ok = all(0.0 < r[5] < r[6] <= r[7] for r in align_rows)
    b_gain = min(abs(K0_CLOSED / kmins[n][0]) for (n, _u, _m) in ATOMS)
    b_full = all(v >= 0.999 for v in cert_frac.values())
    e_share = max(r["cE"] / r["mu"] for r in ledger)
    print("  (A) alignment  : the sharp constant is c_k = mu_-^(k) (L1/L2), it exists in")
    print("      all four zones, and the physical coupling sits strictly inside the")
    print("      admissible window.  The c-law is the SLACK s = 1 - c_k/mu_k: it starts")
    print("      at 0.06..0.28 just past the handoff and collapses like exp(-%.0f alpha)"
          % (sum(rates.values()) / len(rates)))
    print("      to %.0e at the top of the zone, where the next atom takes over."
          % max(slack_top.values()))
    print("  (B) reduction  : the t=0 killer is provably lost on E_- (gain >= x%.2f) and"
          % b_gain)
    print("      the explicit bound certifies the E_- half-step on %.0f%%..%.0f%% of each"
          % (100.0 * min(cert_frac.values()), 100.0 * max(cert_frac.values())))
    print("      zone.  But E_- is not the seat of the negativity: Q|E_- is POSITIVE over")
    print("      most of every zone and reaches at most %.0f%% of the sharp constant."
          % (100.0 * e_share))
    print("  (C) gaps       : the splitting is exact and the atom is diagonal in it.  All")
    print("      three ATOM-SHIFTED diagonal blocks are positive at every tested alpha, so")
    print("      the step reduces to the cross blocks -- which the atom cannot touch.  E_0")
    print("      is the SAME form at alpha' = log n_k - alpha < alpha_k (the induction")
    print("      hypothesis, exact to 1e-13) with margin lam_0 ~ 1e-5, and its near-null")
    print("      mode couples into E_- with g_0/sqrt(lam_0) in [%.2f, %.2f] over 4.5"
          % (schur_ratio_lo, schur_ratio))
    print("      decades of lam_0.  A norm-based cross bound is dead (3x3 comparison matrix")
    print("      %+.2f); the live object is the Schur weight g_0^2/lam_0 = %.2f..%.2f,"
          % (worst_cmp, min(schur_w), max(schur_w)))
    print("      the same size as the atom's own gain mu_k/2 on E_-.")
    if not a_ok:
        verdict = "NO-LAW"
    elif b_full and worst_cmp >= 0.0:
        verdict = "INDUCTION-SHAPED"
    else:
        verdict = "ALIGNMENT-ONLY"
    print("")
    print("  VERDICT: %s" % verdict)
    print("    (A) holds, sharply and with a quantitative c-law.  (B) delivers a genuine,")
    print("    certified E_- half-step -- the t=0 killer really is gone -- but breaks as a")
    print("    ROUTE: the loser is not an E_- vector, and once the atom is added no")
    print("    diagonal block is negative at all, so the diagonal route cannot be the")
    print("    mechanism.  The break is located exactly: the E_-/E_0 cross block against")
    print("    the near-null mode of the smaller problem.  The step has a proof SKELETON")
    print("    (three diagonal conditions, two of them discharged) and one missing lemma.")

    print("")
    print("TOTAL  checks=%d  pass=%d  fail=%d  runtime=%.1fs"
          % (PASS + FAIL, PASS, FAIL, time.time() - T_START))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
