"""Discovery probe (2026-07-26), part 98 of the zeta/prime investigation.
Contract CROSS.LEMMA -- the ONE missing lemma of the T97 staircase induction
step, attacked head on:

        ||Q_-0 v_0||^2  <=  C * lambda_0      with an explicit C = O(1),

where (T97 block C) v_0 is the near-null mode of the PREDECESSOR zone (the E_0
block is, by the T97 self-similarity, the induction hypothesis at the smaller
window alpha' = log n_k - alpha), Q_-0 is the E_-/E_0 cross block of the Weil
form, and lambda_0 = lambda_min(Q|E_0) is the ground eigenvalue of that smaller
problem.  T97 MEASURED g_0/sqrt(lambda_0) in [0.13, 1.30] across 4.5 decades of
lambda_0; this probe asks WHY, and whether the resulting constant is small
enough to close the step.

THE CONVENTION (T93/T95/T96/T97, unchanged)
  f real, supp f subset (-alpha, alpha), ||f||_2 = 1;  h = f * f~ even,
  h(0) = 1, supp h subset (-2 alpha, 2 alpha).
      P_pole(f) = 2 (int f e^{x/2})(int f e^{-x/2})
      A_arch(f) = (1/2pi) int |fhat(t)|^2 k(t) dt,
                  k(t) = Re psi(1/4 + i t/2) - log pi,  k(0) = -5.3722...,
                  single sign change t0 = 6.28983599...
      Q_k(f)    = P_pole + A_arch - sum_{j<=k} mu_j h_f(log n_j),
                  mu_j = 2 Lambda(n_j)/sqrt(n_j)   (Weil 1952)
  Zone k is alpha in (alpha_k, alpha_{k+1}), alpha_k = log(n_k)/2, and the whole
  geometry is ONE number: the WING WIDTH delta = 2 alpha - u, u = log n_k:
      wings   I_L = (-alpha, -alpha'),  I_R = (alpha', alpha) = I_L + u,
      centre  (-alpha', alpha'),        alpha' = u - alpha,  |I_L| = delta.
  E_-/E_+ are the anti/symmetric two-bump pairs on the wings, E_0 the centre;
  S_k = diag(-1/2, 0, +1/2) there (T95-C1), and Q|E_0 is the SAME form at
  alpha' -- the induction hypothesis.  Note delta < u in every zone.

WHAT THIS PROBE ADDS
  R1  THE STRUCTURE OF Q_-0 (three exact identities, quadrature-free).
      (i)  EXTENSION-DEFECT FORM.  For v in E_0 with zero extension v~,
           (Q_-0 v)(x) = 2^{-1/2} [ (Q v~)(x) - (Q v~)(x+u) ],  x in I_L.
           The centre part of the potential w := Q v~ is pinned by the smaller
           problem's Euler-Lagrange equation, w|centre = lambda_0 v_0, so the
           cross block is exactly the part of w OUTSIDE the induction window:
           Q_-0 v_0 is the EXTENSION DEFECT of the induction hypothesis.
      (ii) ODD-PART IDENTITY.  Q_{k-1} is centro-symmetric and v_0 is even, so
           w is even, w|I_R is the mirror of w|I_L, and
                Q_-0 v_0 = sqrt(2) * ODD PART of w|I_L about the wing midpoint.
      (iii) RANK-2 POLE SPLIT (closed form).  With p = <e^{x/2}, v_0>, the pole
           part of the cross term is 2^{-1/2} p [(1-e^{u/2}) a_I +
           (1-e^{-u/2}) b_I], and on the wing ||a_I|| ||b_I|| = 2 sinh(delta/2),
           <a_I,b_I> = delta EXACTLY (new closed forms; they replace T97's
           surd sqrt(J_+ J_-) and make the rank-2 eigenvalues elementary).
  R2  X1 -- WHICH MECHANISM CARRIES THE LAW.  Candidate proxies regressed
      against lambda_0, plus three decisive audits:
        (a) BOUNDARY/EXTENSION (Rellich-flavoured): does g_0 track boundary
            data of v_0 (endpoint value, collar mass, wing slope of w)?
        (c) CANCELLATION: split the wing potential into arch / pole / OLD-ATOM
            parts and measure how much they cancel.
        (d) DOUGLAS: for a PSD block [[A,B],[B^T,D]], Douglas (1966) range
            inclusion gives B = A^{1/2} K D^{1/2}, ||K|| <= 1, hence
            ||B v_0||^2 <= R_A(xhat) lambda_0 with R_A the RAYLEIGH QUOTIENT of
            A at the coupling direction -- an identity-shaped explanation of a
            sqrt law.  Tested for validity, for sharpness, and for grid
            stability against the operator norm ||A|| (which diverges).
      plus a NON-CIRCULARITY audit (is the atom-free compression
      Q_{k-1}|(E_- (+) E_0) already PSD, so that a STRENGTHENED induction
      hypothesis would do instead of the conclusion?) and THE EXACT
      REFORMULATION that comes out of it: since the atom is mu_k/2 times the
      identity on E_-, and the Schur complement onto E_- is an E_- operator,
      the shift passes straight through the complement, so the E_-/E_0 half of
      the induction step is EXACTLY the scalar inequality
          D_k(alpha) := -lambda_min(Q|E_- - Q_-0 (Q|E_0)^{-1} Q_0-) <= mu_k/2
      -- no cross lemma, no near-null mode, no constant C.
  R3  X2 -- THE BOUND AND THE CLOSURE MAP, with the Schur object measured three
      ways (v_0 term, full Schur operator, and the exact reduced block), a
      mode-by-mode decomposition of the Schur weight, and a three-grid
      convergence study for BOTH lambda_0 and D_k -- because lambda_0 ~ 1e-5 is
      a Rayleigh-Ritz UPPER bound and every ratio with lambda_0 in the
      denominator inherits its error.
  R4  X3 -- CERTIFICATES.  Two upgrades over T97's E_- bound:
      (1) THE PROBABILITY-MEASURE IDENTITY.  For phi supported on an interval
          of length delta < u the autocorrelation h_phi(u) vanishes, hence
             (1/2pi) int (1 -+ cos(tu)) |phihat|^2 dt = ||phi||^2
          exactly, i.e. d nu_-+ := (1 -+ cos(tu)) |phihat|^2 dt / (2pi ||phi||^2)
          is a PROBABILITY measure and  A_arch|E_-+ / ||f||^2 = int k d nu.
          The E_-+ archimedean form is therefore an AVERAGE of k, and the mass
          that a narrow wing cannot keep at low frequency is forced out to
          large |t| where k(t) ~ log(t/2) - log pi is large and POSITIVE.
      (2) MULTIBAND SLEPIAN ALLOCATION.  Per-band caps
          nu(B_j) <= max_{B_j}(1 -+ cos(tu)) * Lam_j(delta) with Lam_j the top
          Slepian-Pollak-Landau concentration eigenvalue, a Lipschitz-safe
          minorant of k on each band, and the exact greedy water-filling LP
          under the total mass 1.  This is what finally certifies E_+.

PREREGISTERED VERDICTS
  CROSS-LEMMA-SHAPED         : X1 mechanism identified AND the X2 bound closes
                               on substantial delta-ranges.
  LAW-CONFIRMED-MECHANISM-OPEN: the law hardens, mechanism only partly
                               identified -- with the missing piece named.
  CROSS-BLOCKED              : no mechanism, or the law breaks.
  Element gates: el_firewall, el_kernel, el_forms, el_anchor, el_split,
  el_struct, el_fence, el_law, el_x1, el_douglas, el_x2, el_conv, el_cert.

OUTCOME OF THIS RUN  =>  LAW-CONFIRMED-MECHANISM-OPEN (with the target replaced)
  44 checks, 0 failures, 49 s, largest array 1900^2.
  X1  The law reproduces (g_0/sqrt(lam_0) in [0.05, 1.31] over 4.7 decades) and
      its mechanism is identified exactly: Douglas range inclusion on the PSD
      2x2 block, valid at all 24 samples and SATURATING to 1.6x at the tops of
      the zones.  Two refinements: the operator-norm form of the constant is
      vacuous (lambda_max(Q|E_-) grows 15-17% per grid refinement -- it diverges
      like log(1/d) because k(t) ~ log t), while the directional Rayleigh
      quotient R_A(xhat) moves <= 2.5% and IS a continuum object; and the size
      of the defect is set by a three-way wing cancellation (arch against the
      OLD ATOMS to 15%, the residue against the pole rescue to 0.6%) worth up to
      167x -- zone n=2 has no old atoms, no cancellation, and the largest ratio.
      But the identification DISSOLVES the lemma: g_0 and lambda_0 belong to the
      same discrete operator, which is PSD, so the law is forced at any
      resolution and carries no information beyond the positivity to be proved.
  X2  Three of T97's premises fail.  (1) The v_0 term carries only 0.2%..89% of
      trace(Q_-0 Q_00^{-1} Q_0-), so the missing lemma is NOT a one-vector
      statement.  (2) In zones n=3,4,5 lambda_0 Richardson-extrapolates to zero
      or below on three nested grids: the measured ~3e-6 is a discretisation
      floor (T96's exp(-49 alpha) law predicts ~1e-11 there), so most of the
      "4.5 decades" is the gap between zone 2's real margin and that floor.
      (3) Q_{k-1} is already indefinite on E_- (+) E_0 (J reaches -0.72), so no
      atom-free PSD input exists and Douglas stays circular.  What replaces them
      is an IDENTITY: lambda_min(S11) = J + mu_k/2 (to 1e-16), hence the E_-/E_0
      half of the step is exactly D_k(alpha) <= mu_k/2.  D_k is grid-stable at
      the binding end (drift 3e-3), holds in all four zones, and its margin
      collapses to +4.8e-4 (n=5), +1.9e-2 (n=3), +2.2e-2 (n=4), +3.7e-2 (n=2) at
      the top of the zone -- saturated exactly where the next atom takes over.
      The loser of the predecessor form puts only 0-2% of its mass in E_+.
  X3  The probability-measure identity (h_phi(u) = 0 for delta < u makes
      (1-+cos(tu))|phihat|^2 dt/2pi a PROBABILITY measure, so A_arch|E_-+ is an
      AVERAGE of k) plus multiband Slepian allocation lifts the E_- certificate
      from T97's 31%..55% to 73%..100% of the zones (the whole zone in three of
      four) and certifies E_+ on 25%..55% -- T97 had E_+ measured only.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit, no
    verification/ module, no next.txt edit, no .md output.
  * NO Riemann zero data of any kind; the AST firewall rejects zero-table
    tokens, network imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  A negative
    lambda_min on a genuine window direction is an IMPLEMENTATION SIGNAL,
    fenced, never reported as mathematics.
  * lambda_min^(M) on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for
    the continuum value: it can refute positivity, never prove it.  R3 measures
    how far lambda_0 still is from its limit and states which conclusions are
    resolution-limited.  The only objects pointing the other way are the R4
    certificates: closed-form except for the Slepian eigenvalues (Nystrom,
    convergence reported) and the Lipschitz-safe symbol minorant.
  * No "proved" language without a certificate.  Classical anchors cited, not
    re-derived: Weil 1952, Yoshida 1992 / Bombieri 2000 / Connes-Consani 2021,
    the digamma archimedean kernel, Rayleigh-Ritz, Nystrom collocation,
    Paley-Wiener, Schur complements, Douglas 1966 (majorization / factorisation
    / range inclusion), Slepian-Pollak-Landau prolate concentration,
    Rellich-Necas boundary identities (cited as the ANALOGUE only: the operator
    here is nonlocal, so no Rellich identity is claimed).
"""
import ast
import math
import os
import time

import mpmath
import numpy as np
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh

PASS = 0
FAIL = 0
T_START = time.time()
mpmath.mp.dps = 30

EULER = float(mpmath.euler)
LOG_PI = math.log(math.pi)
K0_CLOSED = -EULER - 3.0 * math.log(2.0) - math.pi / 2.0 - LOG_PI
T0_REF = 6.28983599
MAX_ARRAY = 2000
M_CAP = 1900          # main sweep
FENCE = -1e-9

# (n, log n, mu_n = 2 Lambda(n)/sqrt(n))
ATOMS = (
    (2, math.log(2.0), 2.0 * math.log(2.0) / math.sqrt(2.0)),
    (3, math.log(3.0), 2.0 * math.log(3.0) / math.sqrt(3.0)),
    (4, math.log(4.0), 2.0 * math.log(2.0) / 2.0),
    (5, math.log(5.0), 2.0 * math.log(5.0) / math.sqrt(5.0)),
)
ALPHA_NEXT_ATOM = math.log(7.0) / 2.0
T96_HANDOFF = (0.0250, 0.0094, 0.0114, 0.0067)
T97_RATIO_LO, T97_RATIO_HI = 0.13, 1.30

GLX, GLW = np.polynomial.legendre.leggauss(24)
SQ2 = math.sqrt(2.0)


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-32s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-32s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------------
# el_firewall -- AST scan of this source
# ----------------------------------------------------------------------------
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
# PWC Galerkin assembly on (-alpha, alpha) with M cells
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


def arch_matrix(alpha, M):
    return arch_symbol(alpha, M)[index_matrix(M)]


def atom_matrix(u, alpha, M):
    return atom_symbol(u, alpha, M)[index_matrix(M)]


def prime_free_matrix(alpha, M):
    A = arch_matrix(alpha, M)
    a, b = pole_vectors(alpha, M)
    P = np.outer(a, b)
    return A + P + P.T


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
    # monotonicity of k beyond t0 (used by the R4 tail term)
    tg = np.concatenate([np.linspace(t0, 200.0, 40000), np.geomspace(200.0, 1e7, 40000)])
    dk = np.diff(kernel_k(tg))
    check("el_kernel.tail_monotone", float(dk.min()) >= -1e-15,
          "k increasing on [t0, 1e7]: min increment %.1e, k(1e7) = %.3f"
          % (float(dk.min()), kernel_k_scalar(1e7)))
    return t0


def arch_flat_uspace(alpha):
    """A_arch of the flat window by mpmath quadrature of the exact u-identity."""
    b = 2 * mpmath.mpf(alpha)
    w = lambda u: 2 * mpmath.e ** (-u / 2) / (1 - mpmath.e ** (-2 * u))
    hh = lambda u: 1 - u / b
    Cb = -mpmath.euler - mpmath.log(mpmath.pi) - mpmath.log(1 - mpmath.e ** (-2 * b))
    integ = lambda u: w(u) * (mpmath.e ** (mpmath.mpf(-3) * u / 2) - hh(u))
    return float(Cb + mpmath.quad(integ, [0, b / 8, b / 2, b]))


def gate_forms():
    alpha, M = 0.31, 400
    t = arch_symbol(alpha, M)
    c = np.full(M, 1.0 / math.sqrt(M))
    A_disc = float(c @ (t[index_matrix(M)] @ c))
    A_u = arch_flat_uspace(alpha)
    check("el_forms.arch_uspace", abs(A_disc - A_u) <= 1e-10,
          "PWC %.12f vs mpmath %.12f (d=%.2e)" % (A_disc, A_u, abs(A_disc - A_u)))
    rng = np.random.default_rng(9701)
    v = rng.normal(size=M)
    v /= np.linalg.norm(v)
    d = 2.0 * alpha / M
    worst = 0.0
    for u in (0.2, 0.37, 2.0 * alpha - 0.031):
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
# wing-aligned grid and the exact E_- / E_0 / E_+ splitting
#   cells  [0, nI) = I_L,  [nI, m) = centre,  [m, m+nI) = I_R = I_L + u
# ----------------------------------------------------------------------------
def wing_grid(u, delta_target, m_cap, n_wing_min=6):
    """Grid with d = u/m EXACTLY and delta = nI d exactly; alpha = (u+delta)/2."""
    m = max(8, int(m_cap * u / (u + delta_target)))
    d = u / m
    nI = max(n_wing_min, int(round(delta_target / d)))
    while m + nI > m_cap and m > 16:
        m -= 8
        d = u / m
        nI = max(n_wing_min, int(round(delta_target / d)))
    M = m + nI
    return 0.5 * M * d, M, m, nI, nI * d


def split_basis(M, m):
    """Orthonormal U = [E_- | E_0 | E_+]; nI = M-m anti/sym pairs."""
    nI = M - m
    n0 = M - 2 * nI
    U = np.zeros((M, M))
    r = 1.0 / SQ2
    j = np.arange(nI)
    U[j, j] = r
    U[j + m, j] = -r
    U[np.arange(nI, m), np.arange(nI, nI + n0)] = 1.0
    U[j, nI + n0 + j] = r
    U[j + m, nI + n0 + j] = r
    return U, nI, n0


def fast_blocks(Q, m, nI):
    """The six blocks of U^T Q U without forming U (verified in el_split)."""
    QLL = Q[0:nI, 0:nI]
    QLR = Q[0:nI, m:m + nI]
    QRR = Q[m:m + nI, m:m + nI]
    QLC = Q[0:nI, nI:m]
    QRC = Q[m:m + nI, nI:m]
    Qmm = 0.5 * (QLL - QLR - QLR.T + QRR)
    Qpp = 0.5 * (QLL + QLR + QLR.T + QRR)
    Qmp = 0.5 * (QLL + QLR - QLR.T - QRR)
    Qm0 = (QLC - QRC) / SQ2
    Q0p = ((QLC + QRC) / SQ2).T
    Q00 = Q[nI:m, nI:m]
    return Qmm, Q00, Qpp, Qm0, Qmp, Q0p


# ----------------------------------------------------------------------------
# R4 machinery -- Slepian band concentration + the probability-measure bound
# ----------------------------------------------------------------------------
_GLC = {}


def _gl(N):
    if N not in _GLC:
        _GLC[N] = np.polynomial.legendre.leggauss(N)
    return _GLC[N]


def band_concentration(a, b, delta, N=110):
    """Slepian-Pollak-Landau: the largest energy fraction inside {a<=|t|<=b} of
    a function supported on an interval of length delta.  Nystrom (Gauss-
    Legendre) for the smooth PSD kernel [sin(b s) - sin(a s)]/(pi s)."""
    if b <= a or delta <= 0.0:
        return 0.0
    if (b - a) * delta / math.pi >= 1.0:
        return 1.0
    x, w = _gl(N)
    x = 0.5 * delta * x
    w = 0.5 * delta * w
    D = x[:, None] - x[None, :]
    np.fill_diagonal(D, 1.0)
    K = (np.sin(b * D) - np.sin(a * D)) / (math.pi * D)
    np.fill_diagonal(K, (b - a) / math.pi)
    sw = np.sqrt(w)
    Ks = sw[:, None] * K * sw[None, :]
    lam = float(eigvalsh(Ks, subset_by_index=[N - 1, N - 1])[0])
    return min(1.0, max(0.0, lam))


def safe_extremes(fun, a, b, ngrid=800):
    """Lipschitz-safe (min, max) of a smooth fun on [a,b] from a grid."""
    tt = np.linspace(a, b, ngrid)
    vals = np.asarray(fun(tt), dtype=float)
    step = tt[1] - tt[0]
    lip = float(np.max(np.abs(np.diff(vals)))) / step
    return float(vals.min()) - 0.5 * lip * step, float(vals.max()) + 0.5 * lip * step


def nu_band_table(u, sign, t0, delta, n_in=60, n_out=320):
    """Bands on [0, T_max] with (min k, max weight) per band.  sign = -1 for
    E_- (weight 1-cos(tu)), +1 for E_+ (weight 1+cos(tu))."""
    tmax = t0 + 4.0 * math.pi / delta
    e_in = t0 * (np.linspace(0.0, 1.0, n_in + 1) ** 1.5)
    e_out = t0 + (tmax - t0) * (np.linspace(0.0, 1.0, n_out + 1) ** 2.0)
    edges = np.concatenate([e_in, e_out[1:]])
    wfun = (lambda t: 1.0 - np.cos(t * u)) if sign < 0 else (lambda t: 1.0 + np.cos(t * u))
    rows = []
    for j in range(len(edges) - 1):
        a, b = max(edges[j], 1e-9), edges[j + 1]
        kmin, _ = safe_extremes(kernel_k, a, b)
        _, wmax = safe_extremes(wfun, a, b)
        rows.append((a, b, kmin, min(2.0, max(0.0, wmax))))
    ktail = kernel_k_scalar(tmax) - 1e-9
    return rows, ktail


def nu_bound(rows, ktail, delta):
    """int k d nu >= water-filling minimum, nu a probability measure with
    nu(B_j) <= wmax_j * Lam_j(delta) (Slepian) and k >= ktail beyond T_max."""
    caps, ks = [], []
    for (a, b, kmin, wmax) in rows:
        caps.append(min(1.0, wmax * band_concentration(a, b, delta)))
        ks.append(kmin)
    caps = np.array(caps)
    ks = np.array(ks)
    order = np.argsort(ks)
    rem, tot = 1.0, 0.0
    for j in order:
        if rem <= 0.0 or ks[j] >= ktail:
            break
        take = min(caps[j], rem)
        tot += ks[j] * take
        rem -= take
    return tot + ktail * max(rem, 0.0)


def trace_bound(kmin_w, delta, t0):
    """The T97 route: one band, mass bounded by the TRACE t0 delta/pi, symbol by
    its global infimum inf_t (1-cos(tu)) k(t)."""
    return kmin_w * min(1.0, t0 * delta / math.pi)


def old_atom_penalty(kidx, u, delta):
    """T95-C1: ||S_{u_j}|| <= 1/2, so -mu_j S_j >= -mu_j/2.  Old atoms vanish on
    E_-/E_+ unless u_j <= delta or |u - u_j| <= delta (autocorrelation support)."""
    pen = 0.0
    for (_nj, uj, muj) in ATOMS[:kidx]:
        if uj <= delta or abs(u - uj) <= delta:
            pen += 0.5 * muj
    return pen


def cert_block(kidx, u, delta, sign, rows, ktail):
    """Explicit lower bound for lambda_min(Q_{k-1}|E_-+).  Pole part is the exact
    rank-2 eigenvalue with the closed forms ||a_I|| ||b_I|| = 2 sinh(delta/2) and
    <a_I,b_I> = delta; arch part is the probability-measure multiband bound."""
    ch = math.cosh(0.5 * u)
    sh = 2.0 * math.sinh(0.5 * delta)
    pole = (1.0 - ch) * (delta + sh) if sign < 0 else (1.0 + ch) * (delta - sh)
    return pole + nu_bound(rows, ktail, delta) - old_atom_penalty(kidx, u, delta)


# ----------------------------------------------------------------------------
# the per-sample computation
# ----------------------------------------------------------------------------
NMODE = 12


def sample(kidx, delta_target, m_cap, fence=True, loser=False):
    n, u, mu = ATOMS[kidx]
    alpha, M, m, nI, delta = wing_grid(u, delta_target, m_cap)
    n0 = M - 2 * nI
    A = arch_matrix(alpha, M)
    av, bv = pole_vectors(alpha, M)
    P = np.outer(av, bv)
    Q = A + P + P.T
    atom_ops = []
    for (_nj, uj, muj) in ATOMS[:kidx]:
        Sj = atom_matrix(uj, alpha, M)
        Q -= muj * Sj
        atom_ops.append((muj, Sj))
    Sk = atom_matrix(u, alpha, M)

    Qmm, Q00, Qpp, Qm0, Qmp, Q0p = fast_blocks(Q, m, nI)

    # near-null modes of the SMALLER problem (the induction hypothesis)
    ev, V0 = eigh(Q00, subset_by_index=[0, min(NMODE - 1, n0 - 1)])
    lam0 = float(ev[0])
    v0 = np.ascontiguousarray(V0[:, 0])
    if float(v0.sum()) < 0.0:
        v0 = -v0
    vt = np.zeros(M)
    vt[nI:m] = v0

    # potential, extension defect, the three R1 identities
    w = Q @ vt
    wL, wC, wR = w[0:nI], w[nI:m], w[m:m + nI]
    cross = Qm0 @ v0
    g0 = float(np.linalg.norm(cross))
    res_el = float(np.linalg.norm(wC - lam0 * v0))
    id_ext = float(np.max(np.abs(cross - (wL - wR) / SQ2)))
    even_v0 = float(np.linalg.norm(v0 - v0[::-1]))
    id_odd = float(np.max(np.abs((wL - wR) / SQ2 - (wL - wL[::-1]) / SQ2)))

    # component split of the wing coupling (arch / pole / OLD atoms)
    wA = A @ vt
    qa, qb = float(av @ vt), float(bv @ vt)
    wP = qb * av + qa * bv
    c_arch = (wA[0:nI] - wA[m:m + nI]) / SQ2
    c_pole = (wP[0:nI] - wP[m:m + nI]) / SQ2
    watom = np.zeros(M)
    for (muj, Sj) in atom_ops:
        watom -= muj * (Sj @ vt)
    c_atom = (watom[0:nI] - watom[m:m + nI]) / SQ2
    pole_cf = (qb * (1.0 - math.exp(0.5 * u)) * av[0:nI]
               + qa * (1.0 - math.exp(-0.5 * u)) * bv[0:nI]) / SQ2
    id_pole = float(np.max(np.abs(c_pole - pole_cf)))
    nA = float(np.linalg.norm(c_arch))
    nP = float(np.linalg.norm(c_pole))
    nS = float(np.linalg.norm(c_atom))
    n_AS = float(np.linalg.norm(c_arch + c_atom))

    # spectral picture in E_-
    tau, Y = eigh(Qmm)
    coef = Y.T @ cross
    p2 = coef ** 2
    tot = float(p2.sum())
    srt = np.sort(p2)[::-1]
    n90 = int(np.searchsorted(np.cumsum(srt), 0.9 * tot) + 1) if tot > 0 else 0
    A_shift = tau + 0.5 * mu
    ray = float((p2 @ A_shift) / tot) if tot > 0 else 0.0
    lam_mm, lam_mx = float(tau[0]), float(tau[-1])

    # Schur objects
    wv0 = g0 * g0 / lam0
    cf = cho_factor(Q00, lower=True, check_finite=False)
    X = cho_solve(cf, Qm0.T, check_finite=False)
    Wm = Qm0 @ X
    Wm = 0.5 * (Wm + Wm.T)
    wsp = eigvalsh(Wm)
    wfull = float(wsp[-1])
    wtrace = float(np.trace(Wm))
    S11 = Qmm + 0.5 * mu * np.eye(nI) - Wm
    lam_S11 = lam_min(S11)
    lam_J = lam_min(Qmm - Wm)          # atom-free: the strengthened hypothesis
    modes = [float(np.linalg.norm(Qm0 @ V0[:, j]) ** 2 / ev[j]) for j in range(len(ev))]
    share_top = sum(modes) / wtrace if wtrace > 0 else float("nan")

    lam_pp = float(eigvalsh(Qpp, subset_by_index=[0, 0])[0])
    lam_fence = lam_min(Q - mu * Sk) if fence else 0.0
    wts = None
    if loser:
        e1, V1 = eigh(Q, subset_by_index=[0, 0])
        z = V1[:, 0]
        zL, zC, zR = z[0:nI], z[nI:m], z[m:m + nI]
        cm = (zL - zR) / SQ2
        cp = (zL + zR) / SQ2
        wts = (float(e1[0]), float(cm @ cm), float(zC @ zC), float(cp @ cp))

    # boundary data of v_0 (physical values: coefficient / sqrt(d))
    d = 2.0 * alpha / M
    v_end = abs(float(v0[-1])) / math.sqrt(d)
    collar = max(2, int(round(0.02 / d)))
    v_collar = float(np.linalg.norm(v0[-collar:]))
    xw = np.arange(nI) - 0.5 * (nI - 1)
    nrm = float(xw @ xw)
    slope = float(xw @ wL) / nrm if nrm > 0 else 0.0
    g_lin = SQ2 * abs(slope) * math.sqrt(nrm)

    return dict(n=n, kidx=kidx, u=u, mu=mu, alpha=alpha, delta=delta, M=M, m=m,
                nI=nI, n0=n0, d=d, lam0=lam0, g0=g0, ratio=g0 / math.sqrt(lam0),
                wv0=wv0, wfull=wfull, wtrace=wtrace, share_top=share_top,
                modes=modes, lam_S11=lam_S11, lam_J=lam_J,
                lam_mm=lam_mm, lam_mx=lam_mx, lam_pp=lam_pp, ray=ray, n90=n90,
                need=lam_mm + 0.5 * mu, lam_fence=lam_fence, wts=wts,
                res_el=res_el, id_ext=id_ext, id_odd=id_odd, id_pole=id_pole,
                even_v0=even_v0, qa=qa, qb=qb, nA=nA, nP=nP, nS=nS, n_AS=n_AS,
                nwL=float(np.linalg.norm(wL)), v_end=v_end, v_collar=v_collar,
                g_lin=g_lin, cross=cross)


def loglog_fit(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    ok = (x > 0) & (y > 0)
    if ok.sum() < 3:
        return float("nan"), float("nan")
    lx, ly = np.log(x[ok]), np.log(y[ok])
    s, b = np.polyfit(lx, ly, 1)
    ss = float(np.sum((ly - (s * lx + b)) ** 2))
    st = float(np.sum((ly - ly.mean()) ** 2))
    return float(s), (1.0 - ss / st if st > 0 else float("nan"))


def median_frequency(vec, d, nI, frac=0.5, npts=2500):
    """|t| holding `frac` of the energy of the wing function (PWC: ~10% of the
    energy of ANY cell function sits above the Nyquist frequency pi/d, so only
    the low quantiles are meaningful)."""
    nrm2 = float(vec @ vec) / 2.0
    if nrm2 <= 0.0:
        return float("nan")
    tt = np.linspace(1e-6, math.pi / d, npts)
    xs = (np.arange(nI) + 0.5) * d
    cellf = 2.0 * np.sin(tt * d / 2.0) / (tt * math.sqrt(d))
    Fm = np.exp(-1j * np.outer(tt, xs)) @ (vec / SQ2)
    dens = (cellf ** 2) * np.abs(Fm) ** 2 / (2.0 * math.pi)
    cum = 2.0 * np.concatenate([[0.0], np.cumsum(0.5 * (dens[1:] + dens[:-1])
                                                 * np.diff(tt))]) / nrm2
    if cum[-1] < frac:
        return float("inf")
    return float(np.interp(frac, cum, tt))


def richardson(ds, vals):
    """Fitted convergence order and limit for vals = lim + C d^p (3 nested d)."""
    (d1, d2, d3), (l1, l2, l3) = ds, vals
    if not (l1 > l2 > l3) and not (l1 < l2 < l3):
        return float("nan"), float("nan")
    lo, hi = 0.05, 6.0
    tgt = (l1 - l2) / (l2 - l3)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        val = (d1 ** mid - d2 ** mid) / (d2 ** mid - d3 ** mid)
        if val < tgt:
            lo = mid
        else:
            hi = mid
    p = 0.5 * (lo + hi)
    return p, l3 - (l2 - l3) / ((d2 / d3) ** p - 1.0)


def converge3(kidx, delta_target, caps=(700, 1200, 1900)):
    """lambda_0 and the wing Schur complement D = -lambda_min(Q|E_- -
    Q_-0 Q_00^{-1} Q_0-) on three nested grids, with Richardson limits."""
    ds, l0s, Ds, delta = [], [], [], 0.0
    for c in caps:
        r = sample(kidx, delta_target, c, fence=False)
        ds.append(r["d"])
        l0s.append(r["lam0"])
        Ds.append(-r["lam_J"])
        delta = r["delta"]
    p0, lim0 = richardson(ds, l0s)
    pD, limD = richardson(ds, Ds)
    return delta, l0s, p0, lim0, Ds, pD, limD


# ----------------------------------------------------------------------------
def main():
    section("CROSS.LEMMA -- part 98 -- gates")
    firewall()
    t0 = gate_kernel()
    gate_forms()

    # ------------------------------------------------------------- R0 anchors
    section("R0  ANCHORS -- zone map and the exact block algebra")
    zones = []
    for kidx, (n, u, mu) in enumerate(ATOMS):
        ak = 0.5 * u
        anext = 0.5 * ATOMS[kidx + 1][1] if kidx + 1 < len(ATOMS) else ALPHA_NEXT_ATOM
        alo, ahi = ak + 2e-4, anext - 1e-3
        for _ in range(15):
            mid = 0.5 * (alo + ahi)
            Qz, _S = zone_forms(kidx, mid, 800)
            if lam_min(Qz) >= 0.0:
                alo = mid
            else:
                ahi = mid
        af = 0.5 * (alo + ahi)
        dmax = 2.0 * anext - u
        gap = min([abs(u - uj) for (_nj, uj, _mj) in ATOMS[:kidx]]
                  + [uj for (_nj, uj, _mj) in ATOMS[:kidx]] + [u])
        zones.append(dict(kidx=kidx, n=n, u=u, mu=mu, ak=ak, anext=anext, af=af,
                          dmax=dmax, gap=gap))
        info("zone n=%d" % n,
             "alpha_k=%.6f  alpha_free=%.6f  handoff=%+.4f (T96 %+.4f)  delta_max=%.4f"
             "  atom-gap=%.4f  mu/2=%.3f" % (ak, af, af - ak, T96_HANDOFF[kidx], dmax,
                                             gap, 0.5 * mu))
        check("el_anchor.handoff n=%d" % n,
              af - ak > 0.0 and abs(af - ak - T96_HANDOFF[kidx]) < 0.02,
              "independent handoff window %+.4f" % (af - ak))

    al, M, m, nI, dl = wing_grid(ATOMS[1][1], 0.06, 500)
    Qs, Ss = zone_forms(1, al, M)
    U, nI2, n0 = split_basis(M, m)
    QB = U.T @ (Qs @ U)
    fb = fast_blocks(Qs, m, nI)
    e_blk = max(float(np.max(np.abs(fb[0] - QB[:nI, :nI]))),
                float(np.max(np.abs(fb[1] - QB[nI:nI + n0, nI:nI + n0]))),
                float(np.max(np.abs(fb[2] - QB[nI + n0:, nI + n0:]))),
                float(np.max(np.abs(fb[3] - QB[:nI, nI:nI + n0]))),
                float(np.max(np.abs(fb[4] - QB[:nI, nI + n0:]))),
                float(np.max(np.abs(fb[5] - QB[nI:nI + n0, nI + n0:]))))
    check("el_split.fast_blocks", e_blk <= 1e-13 and nI2 == nI,
          "fast block extraction == U^T Q U to %.1e" % e_blk)
    SB = U.T @ (Ss @ U)
    dref = np.concatenate([-0.5 * np.ones(nI), np.zeros(n0), 0.5 * np.ones(nI)])
    e_diag = float(np.max(np.abs(SB - np.diag(dref))))
    check("el_split.atom_diag", e_diag <= 1e-13, "S_k = diag(-1/2,0,+1/2) to %.1e" % e_diag)
    ap = ATOMS[1][1] - al
    Qsm = prime_free_matrix(ap, n0) - ATOMS[0][2] * atom_matrix(ATOMS[0][1], ap, n0)
    e_self = float(np.max(np.abs(Qsm - fb[1])))
    check("el_split.self_similar", e_self <= 1e-11,
          "Q|E_0 = Q_{k-1}(alpha'=%.5f) to %.1e -- the induction hypothesis" % (ap, e_self))
    av, bv = pole_vectors(al, M)
    e_cf = max(abs(float(av[:nI] @ av[:nI]) - 2.0 * math.exp(-0.5 * ATOMS[1][1])
                   * math.sinh(0.5 * dl)),
               abs(float(bv[:nI] @ bv[:nI]) - 2.0 * math.exp(0.5 * ATOMS[1][1])
                   * math.sinh(0.5 * dl)),
               abs(float(av[:nI] @ bv[:nI]) - dl))
    check("el_struct.pole_closed_forms", e_cf <= 5e-7,
          "||a_I||^2 = 2 e^{-u/2} sinh(d/2), ||b_I||^2 = 2 e^{u/2} sinh(d/2), "
          "<a_I,b_I> = delta  to %.1e" % e_cf)
    info("closed form", "||a_I|| ||b_I|| = 2 sinh(delta/2) exactly, independent of u "
         "-- replaces the T97 surd sqrt(J_+ J_-)")

    # ------------------------------------------------------------- R1 samples
    section("R1  STRUCTURE -- Q_-0 v_0 is the EXTENSION DEFECT of the hypothesis")
    print("  (i)   (Q_-0 v)(x) = 2^{-1/2} [ (Q v~)(x) - (Q v~)(x+u) ],  x in I_L,")
    print("        with v~ the zero extension.  The CENTRE part of w = Q v~ is pinned")
    print("        by the smaller problem, w|centre = lambda_0 v_0, so the cross block")
    print("        is exactly the part of the potential OUTSIDE the induction window.")
    print("  (ii)  w is even, so w|I_R mirrors w|I_L and Q_-0 v_0 = sqrt(2) x ODD PART")
    print("        of w|I_L about the wing midpoint: the coupling is blind to the even")
    print("        part of the wing potential.")
    print("  (iii) the rank-2 pole part splits off in closed form.")
    print("")
    rows = []
    for z in zones:
        for i, dt in enumerate(np.geomspace(0.007, 0.97 * z["dmax"], 6)):
            rows.append(sample(z["kidx"], float(dt), M_CAP, loser=(i >= 4)))
    print("   n   delta    M   nI    n0     lam_0      g_0     g_0/sqrt(lam_0)"
          "   |w|I_L|   ext-id   odd-id  pole-id  |v0-rev|")
    for r in rows:
        print("  %2d  %.4f %5d %4d %5d  %.3e  %.3e %11.3f  %9.3e  %.0e  %.0e  %.0e  %.0e"
              % (r["n"], r["delta"], r["M"], r["nI"], r["n0"], r["lam0"], r["g0"],
                 r["ratio"], r["nwL"], r["id_ext"], r["id_odd"], r["id_pole"],
                 r["even_v0"]))
    check("el_struct.extension", max(r["id_ext"] for r in rows) <= 1e-11,
          "Q_-0 v = 2^{-1/2}(w(x) - w(x+u)) to %.1e" % max(r["id_ext"] for r in rows))
    check("el_struct.euler_lagrange", max(r["res_el"] for r in rows) <= 1e-10,
          "||w|centre - lambda_0 v_0|| <= %.1e (the hypothesis' EL equation)"
          % max(r["res_el"] for r in rows))
    check("el_struct.odd_part", max(r["id_odd"] for r in rows) <= 1e-11
          and max(r["even_v0"] for r in rows) <= 1e-7,
          "v_0 even to %.1e, Q_-0 v_0 = sqrt(2) x odd part to %.1e"
          % (max(r["even_v0"] for r in rows), max(r["id_odd"] for r in rows)))
    check("el_struct.rank2_pole", max(r["id_pole"] for r in rows) <= 1e-10,
          "closed-form rank-2 pole cross term to %.1e" % max(r["id_pole"] for r in rows))
    check("el_fence.zone", all(r["lam_fence"] >= FENCE for r in rows),
          "min lambda_min(Q_k) over %d samples = %+.2e (RH fence, not a result)"
          % (len(rows), min(r["lam_fence"] for r in rows)))

    # ------------------------------------------------------------- R2  X1
    section("R2  X1 -- WHICH MECHANISM CARRIES THE LAW")
    rat_lo = min(r["ratio"] for r in rows)
    rat_hi = max(r["ratio"] for r in rows)
    l0_lo = min(r["lam0"] for r in rows)
    l0_hi = max(r["lam0"] for r in rows)
    l0 = np.array([r["lam0"] for r in rows])
    g0a = np.array([r["g0"] for r in rows])
    s_g0, r2_g0 = loglog_fit(l0, g0a)
    print("  FIRST, WHAT THE LAW ACTUALLY IS.  Pooled over all zones and widths the")
    print("  ratio g_0/sqrt(lam_0) stays in [%.2f, %.2f] while lam_0 sweeps %.1f decades"
          % (rat_lo, rat_hi, math.log10(l0_hi / l0_lo)))
    print("  (T97: [%.2f, %.2f]).  But the pooled log-log slope is %+.3f (R^2 %.3f), not"
          % (T97_RATIO_LO, T97_RATIO_HI, s_g0, r2_g0))
    print("  1/2, and the decades are a BETWEEN-zone effect:")
    for z in zones:
        rr = [r for r in rows if r["n"] == z["n"]]
        s_z, r2_z = loglog_fit([r["lam0"] for r in rr], [r["g0"] for r in rr])
        info("law n=%d" % z["n"],
             "lam_0 %.2e..%.2e (%.2f decades), g_0 %.2e..%.2e, ratio %.3f..%.3f, "
             "within-zone slope %+.2f" % (min(r["lam0"] for r in rr),
                                          max(r["lam0"] for r in rr),
                                          math.log10(max(r["lam0"] for r in rr)
                                                     / min(r["lam0"] for r in rr)),
                                          min(r["g0"] for r in rr), max(r["g0"] for r in rr),
                                          min(r["ratio"] for r in rr),
                                          max(r["ratio"] for r in rr), s_z))
    check("el_law.bounded", 0.02 < rat_lo and rat_hi < 3.0,
          "the law is a BOUNDEDNESS statement: g_0/sqrt(lam_0) in [%.2f, %.2f] over "
          "%.1f decades of lam_0 -- reproduced independently of T97's sampling"
          % (rat_lo, rat_hi, math.log10(l0_hi / l0_lo)))

    print("")
    print("  PROXY REGRESSION (slope vs lam_0; a proxy explains the law only if it has")
    print("  the same slope AND a stable ratio to g_0).")
    print("   quantity                              slope   R^2    ratio to g_0 (min..max)")
    cands = [("g_0 = ||Q_-0 v_0||", g0a),
             ("(a) |v_0| at the window endpoint", np.array([r["v_end"] for r in rows])),
             ("(a) collar mass of v_0", np.array([r["v_collar"] for r in rows])),
             ("(a) ||w|I_L|| wing potential", np.array([r["nwL"] for r in rows])),
             ("(a) linear-slope model of odd part", np.array([r["g_lin"] for r in rows])),
             ("(c) arch part of the coupling", np.array([r["nA"] for r in rows])),
             ("(c) old-atom part of the coupling", np.array([max(r["nS"], 1e-300)
                                                             for r in rows])),
             ("(c) pole part of the coupling", np.array([r["nP"] for r in rows])),
             ("(d) sqrt(R_A(xhat) lam_0)  Douglas",
              np.array([math.sqrt(max(r["ray"], 0.0) * r["lam0"]) for r in rows]))]
    for nm, arr in cands:
        s, r2 = loglog_fit(l0, arr)
        rr = arr / g0a
        print("   %-38s %+.3f  %.3f   %.3f .. %.3f" % (nm, s, r2, rr.min(), rr.max()))
    print("   -> no boundary functional of v_0 tracks g_0 (ratios spread by an order of")
    print("      magnitude): the Rellich/boundary reading is the right STRUCTURE (R1)")
    print("      but does not set the SIZE.")

    print("")
    print("  (c) CANCELLATION AUDIT -- the wing coupling split into arch, OLD-ATOM and")
    print("      pole continuations (they sum exactly to Q_-0 v_0).")
    print("   n   delta   ||arch||   ||old atoms||  ||pole||  ||arch+atoms||    g_0"
          "     total cancellation")
    canc = []
    for r in rows:
        c = (r["nA"] + r["nS"] + r["nP"]) / r["g0"]
        canc.append(c)
        print("  %2d  %.4f  %.3e  %.3e  %.3e  %.3e  %.3e  %10.1f x"
              % (r["n"], r["delta"], r["nA"], r["nS"], r["nP"], r["n_AS"], r["g0"], c))
    canc_by_zone = {z["n"]: max(c for c, r in zip(canc, rows) if r["n"] == z["n"])
                    for z in zones}
    check("el_x1.cancellation", canc_by_zone[2] < 1.1
          and min(canc_by_zone[k] for k in (3, 4, 5)) > 5.0,
          "zone n=2 has NO old atoms and NO cancellation (%.2fx: the defect simply IS the "
          "archimedean continuation); zones n=3,4,5 cancel by %.0f..%.0fx -- the "
          "already-installed primes are what makes the extension defect small"
          % (canc_by_zone[2], min(canc_by_zone[k] for k in (3, 4, 5)),
             max(canc_by_zone[k] for k in (3, 4, 5))))
    narrow = [r for r in rows if r["n"] in (3, 4, 5) and r["delta"] < 0.02]
    e_pair = max(abs(r["nA"] - r["nS"]) / max(r["nA"], r["nS"]) for r in narrow)
    wide = [max((r for r in rows if r["n"] == nn), key=lambda r: r["delta"])
            for nn in (4, 5)]
    e_res = max(abs(r["n_AS"] - r["nP"]) / max(r["n_AS"], r["nP"]) for r in wide)
    check("el_x1.three_way", e_pair < 0.15 and e_res < 0.05,
          "the cancellation is THREE-way and ordered: at narrow wings the arch and "
          "old-atom continuations match to %.0f%% and cancel each other; at the widest "
          "wings of zones 4 and 5 the surviving residue matches the POLE continuation to "
          "%.1f%% and is cancelled by it -- the pole rescue reappears in the cross block "
          "as the last term standing" % (100.0 * e_pair, 100.0 * e_res))

    print("")
    print("  (d) DOUGLAS.  For [[A,B],[B^T,D]] >= 0, Douglas (1966) gives B = A^{1/2} K")
    print("      D^{1/2} with ||K|| <= 1, hence ||B v_0||^2 <= <xhat,A xhat> lambda_0 for")
    print("      xhat = B v_0/||B v_0||.  A = Q|E_- + mu/2, D = Q|E_0.  This DERIVES a")
    print("      sqrt law from positivity alone -- no boundary estimate needed.")
    print("   n   delta  modes@90%  lam_min(Q|E_-)  lam_max(Q|E_-)  R_A(xhat)  g_0^2/lam_0"
          "   Douglas slack  T_50(xhat)")
    doug_ok, tight = True, 1e9
    for r in rows:
        r["T50"] = median_frequency(r["cross"], r["d"], r["nI"])
        sl = r["ray"] / r["wv0"] if r["wv0"] > 0 else float("inf")
        tight = min(tight, sl)
        doug_ok = doug_ok and (r["wv0"] <= r["ray"] * (1.0 + 1e-9) + 1e-12)
        print("  %2d  %.4f %8d  %14.4f  %14.4f  %9.4f  %11.4f  %13.1f  %9.1f"
              % (r["n"], r["delta"], r["n90"], r["lam_mm"], r["lam_mx"], r["ray"],
                 r["wv0"], sl, r["T50"]))
    check("el_douglas.directional", doug_ok,
          "g_0^2/lam_0 <= R_A(xhat) at all %d samples; tightest slack %.2fx (the bound "
          "SATURATES exactly at the tops of the zones, where the step is hard)"
          % (len(rows), tight))

    print("")
    drift = []
    for z in zones[:2]:
        for dt in (0.03, 0.5 * z["dmax"]):
            a1 = sample(z["kidx"], float(dt), 700, fence=False)
            a2 = sample(z["kidx"], float(dt), M_CAP, fence=False)
            drift.append((a1, a2))
            info("M-drift n=%d d=%.3f" % (z["n"], a1["delta"]),
                 "M %d->%d : lam_max(Q|E_-) %.3f -> %.3f (%+.0f%%),  R_A(xhat) %.4f -> "
                 "%.4f (%+.1f%%)" % (a1["M"], a2["M"], a1["lam_mx"], a2["lam_mx"],
                                     100.0 * (a2["lam_mx"] / a1["lam_mx"] - 1.0),
                                     a1["ray"], a2["ray"],
                                     100.0 * (a2["ray"] / a1["ray"] - 1.0)))
    grow = min(b["lam_mx"] / a["lam_mx"] for a, b in drift)
    ray_st = max(abs(b["ray"] / a["ray"] - 1.0) for a, b in drift)
    check("el_douglas.norm_diverges", grow > 1.05 and ray_st < 0.05,
          "lambda_max(Q|E_-) grows >= %.0f%% under refinement (arch symbol k(t) ~ log t "
          "is unbounded above, so the OPERATOR-NORM Douglas constant is +inf in the "
          "continuum) while R_A(xhat) moves only %.1f%%: the DIRECTIONAL constant is a "
          "genuine continuum object" % (100.0 * (grow - 1.0), 100.0 * ray_st))

    print("")
    print("  NON-CIRCULARITY AUDIT.  Douglas needs a PSD input, and the natural one is")
    print("  Q_k >= 0 -- the conclusion.  The weaker candidate would be the ATOM-FREE")
    print("  compression: is Q_{k-1} already PSD on E_- (+) E_0?  Equivalently, is")
    print("      J := lambda_min( Q|E_- - Q_-0 (Q|E_0)^{-1} Q_0- )   >=  0 ?")
    print("  If it were, the E_-/E_0 half of the step would need only a STRENGTHENED")
    print("  induction hypothesis and the atom's mu_k/2 would be pure surplus.")
    print("   n   delta        J        D = -J     mu_k/2    margin mu/2 - D"
          "   loser weights (E_-,E_0,E_+)")
    for r in rows:
        wt = ("   %.2f / %.2f / %.2f  [lam_min(Q_{k-1}) = %+.4f]"
              % (r["wts"][1], r["wts"][2], r["wts"][3], r["wts"][0])) if r["wts"] else ""
        print("  %2d  %.4f  %+9.5f  %+9.5f  %8.5f  %14.5f%s"
              % (r["n"], r["delta"], r["lam_J"], -r["lam_J"], 0.5 * r["mu"],
                 r["lam_S11"], wt))
    jmin = min(r["lam_J"] for r in rows)
    check("el_x1.strengthened_hypothesis_fails", jmin < -0.1,
          "IT IS NOT: J reaches %+.3f, so Q_{k-1} is INDEFINITE already on "
          "E_- (+) E_0 and the atom is genuinely needed there.  No atom-free PSD "
          "input exists, and the Douglas explanation of the law stays circular" % jmin)
    wE = [r["wts"][3] for r in rows if r["wts"]]
    check("el_x1.loser_lives_low", max(wE) < 0.05,
          "the loser of the predecessor form carries only %.0f%%..%.0f%% of its mass in "
          "E_+: the negativity lives in E_- (+) E_0, exactly where the atom acts"
          % (100.0 * min(wE), 100.0 * max(wE)))

    print("")
    print("  THE EXACT REFORMULATION.  The atom is mu_k/2 times the IDENTITY on E_-, and")
    print("  the Schur complement onto E_- is an E_- operator, so the shift passes")
    print("  straight through:")
    print("      lambda_min( (Q|E_- + mu/2) - Q_-0 (Q|E_0)^{-1} Q_0- )  =  J + mu_k/2.")
    print("  Hence the E_-/E_0 half of the induction step is EXACTLY the scalar")
    print("  inequality")
    print("      D_k(alpha) := -lambda_min( Q_{k-1}|E_- - Q_-0 (Q_{k-1}|E_0)^{-1} Q_0- )")
    print("                 <=  mu_k/2 ,")
    print("  with NO cross lemma, NO near-null mode and NO constant C: the wing Schur")
    print("  complement of the predecessor form against the atom's own E_- gain.  T97's")
    print("  ||Q_-0 v_0||^2 <= C lambda_0 is a lossy sufficient condition for this.")
    e_id = max(abs(r["lam_S11"] - (r["lam_J"] + 0.5 * r["mu"])) for r in rows)
    check("el_x2.schur_shift_identity", e_id <= 1e-11,
          "lambda_min(S11) = J + mu_k/2 to %.1e -- the reformulation is an identity, "
          "not an estimate" % e_id)
    print("")
    for z in zones:
        rr = [r for r in rows if r["n"] == z["n"]]
        info("D_k n=%d" % z["n"],
             "D_k = %+.4f .. %+.4f across the zone against mu_k/2 = %.4f; tightest "
             "margin %+.2e at delta = %.4f"
             % (min(-r["lam_J"] for r in rr), max(-r["lam_J"] for r in rr),
                0.5 * z["mu"], min(r["lam_S11"] for r in rr),
                [r["delta"] for r in rr if r["lam_S11"] == min(x["lam_S11"] for x in rr)][0]))
    check("el_x2.reformulation_holds", min(r["lam_S11"] for r in rows) >= FENCE,
          "D_k <= mu_k/2 at every sampled alpha (tightest margin %+.2e): the atom's own "
          "E_- gain covers the wing Schur complement of the predecessor -- but only just, "
          "at the top of every zone" % min(r["lam_S11"] for r in rows))

    # ------------------------------------------------------------- R3  X2
    section("R3  X2 -- THE BOUND, THE SCHUR ANATOMY AND THE CLOSURE MAP")
    print("  The lossy target inequality T97 named:")
    print("      mu_k/2 + lambda_min(Q|E_-)  >  Schur weight,")
    print("  with the Schur weight either the v_0 term g_0^2/lam_0 or the operator norm")
    print("  lambda_max(Q_-0 Q_00^{-1} Q_0-).  (The SHARP condition is lam_min(S11) >= 0")
    print("  above, which holds everywhere -- the lossy version is what a certificate")
    print("  would have to reach.)")
    print("")
    print("   n   delta   mu/2+lam_min(E_-)  g_0^2/lam_0  lam_max(Schur)  trace(Schur)"
          "  v_0 share  top-12 share  closes(v0)  closes(op)")
    close_v, close_f = {}, {}
    for r in rows:
        okv = r["wv0"] <= r["need"]
        okf = r["wfull"] <= r["need"]
        close_v.setdefault(r["n"], []).append((r["delta"], okv))
        close_f.setdefault(r["n"], []).append((r["delta"], okf))
        print("  %2d  %.4f  %17.4f  %11.4f  %14.4f  %12.4f  %9.3f  %12.3f  %9s  %9s"
              % (r["n"], r["delta"], r["need"], r["wv0"], r["wfull"], r["wtrace"],
                 r["wv0"] / r["wtrace"], r["share_top"],
                 "yes" if okv else "no", "yes" if okf else "no"))
    share_max = max(r["wv0"] / r["wtrace"] for r in rows)
    share_min = min(r["wv0"] / r["wtrace"] for r in rows)
    check("el_x2.not_one_vector", share_min < 0.05,
          "the v_0 term carries only %.1f%%..%.0f%% of trace(Q_-0 Q_00^{-1} Q_0-) and the "
          "lowest %d modes only %.0f%%..%.0f%%: the missing lemma is NOT a one-vector "
          "statement -- T97's reading of its own measurement was too optimistic"
          % (100.0 * share_min, 100.0 * share_max, NMODE,
             100.0 * min(r["share_top"] for r in rows),
             100.0 * max(r["share_top"] for r in rows)))

    def frac_closed(lst, dmax):
        lst = sorted(lst)
        if all(f for _d, f in lst):
            return 1.0
        if not lst[0][1]:
            return 0.0
        i = max(i for i in range(len(lst)) if lst[i][1])
        d_hi = lst[i + 1][0] if i + 1 < len(lst) else dmax
        return min(1.0, 0.5 * (lst[i][0] + d_hi) / dmax)

    print("")
    fv, ff = {}, {}
    for z in zones:
        fv[z["n"]] = frac_closed(close_v[z["n"]], z["dmax"])
        ff[z["n"]] = frac_closed(close_f[z["n"]], z["dmax"])
        info("closure n=%d" % z["n"],
             "v_0 term closes on %.0f%% of the zone, operator norm on %.0f%% "
             "(delta_max = %.4f)" % (100.0 * fv[z["n"]], 100.0 * ff[z["n"]], z["dmax"]))
    check("el_x2.closes_somewhere", min(ff.values()) > 0.0,
          "the lossy 2-block inequality closes on %.0f%%..%.0f%% of every zone"
          % (100.0 * min(ff.values()), 100.0 * max(ff.values())))

    print("")
    print("  RESOLUTION AUDIT -- the decisive one.  lambda_0 is a Rayleigh-Ritz UPPER")
    print("  bound, and T96's margin law exp(-49 alpha) predicts a CONTINUUM lambda_0")
    print("  of order 1e-11 at the alpha' reached here -- far below any Galerkin floor.")
    print("  Three nested grids for lambda_0 and for the reformulated object D_k:")
    print("   n   delta     lam_0(M1)  lam_0(M2)  lam_0(M3)  order  Richardson limit"
          "  |  D(M1)     D(M2)     D(M3)    order   limit")
    conv = {"small": [], "bind": []}
    for z in zones:
        for tag, dt in (("small", 0.03), ("bind", 0.6 * z["dmax"])):
            dl_, l0s, p0, lim0, Ds, pD, limD = converge3(z["kidx"], float(dt))
            dlim = limD if limD == limD else max(Ds)
            conv[tag].append(dict(n=z["n"], delta=dl_, l0s=l0s, lim0=lim0, Ds=Ds,
                                  dlim=dlim, half=0.5 * z["mu"]))
            print("  %2d  %.4f  %.3e  %.3e  %.3e  %5.2f  %+.3e  |  %+.5f  %+.5f  %+.5f"
                  "  %5.2f  %+.5f" % (z["n"], dl_, l0s[0], l0s[1], l0s[2], p0, lim0,
                                      Ds[0], Ds[1], Ds[2], pD, dlim))
    allc = conv["small"] + conv["bind"]
    rel = {}
    for c in allc:
        rel[c["n"]] = max(rel.get(c["n"], 0.0), abs(c["l0s"][0] / c["l0s"][2] - 1.0))
    check("el_conv.lambda0_floor", rel[2] < 0.02 and min(rel[k] for k in (3, 4, 5)) > 2.0,
          "zone n=2 has a genuine lambda_0 (it moves %.1f%% between the coarsest and "
          "finest grid); in zones n=3,4,5 it moves by a factor %.1f..%.1f and Richardson "
          "extrapolates to zero or below -- the measured 3e-6 there is a DISCRETISATION "
          "FLOOR, not a physical margin, so T97's '4.5 decades of lambda_0' is mostly the "
          "gap between zone 2's real margin and that floor"
          % (100.0 * rel[2], 1.0 + min(rel[k] for k in (3, 4, 5)),
             1.0 + max(rel[k] for k in (3, 4, 5))))
    marg_b = min(c["half"] - c["dlim"] for c in conv["bind"])
    drift_b = max(abs(c["Ds"][2] - c["Ds"][0]) for c in conv["bind"])
    check("el_conv.D_binding", marg_b > 0.0,
          "at the BINDING end of every zone the Richardson-extrapolated D_k still "
          "satisfies D_k <= mu_k/2, margin %+.4f .. %+.4f, with a grid drift of only "
          "%.1e -- unlike lambda_0, D_k is well conditioned exactly where the step is "
          "tight" % (marg_b, max(c["half"] - c["dlim"] for c in conv["bind"]), drift_b))
    slack_s = min(c["half"] - c["Ds"][2] for c in conv["small"])
    step_s = max(max(abs(c["Ds"][1] - c["Ds"][0]), abs(c["Ds"][2] - c["Ds"][1]))
                 for c in conv["small"])
    check("el_conv.D_small_delta", slack_s > 0.3 and step_s < 0.06,
          "at the narrow-wing end D_k is still drifting (largest refinement step %.3f, "
          "the E_- space itself only has O(10) dimensions there) but the inequality is "
          "slack by >= %.2f, so the drift cannot reach mu_k/2" % (step_s, slack_s))
    Ddrift = drift_b
    print("")
    print("  CONSEQUENCE.  g_0 and lambda_0 are quantities of the SAME discrete operator,")
    print("  and the discrete Q_k is PSD, so Douglas forces g_0^2 <= R_A lambda_0 at any")
    print("  resolution whatever lambda_0 happens to be.  The sqrt law therefore carries")
    print("  NO information beyond positivity: it is a tautology of the thing to be")
    print("  proved, which is exactly why its constant band is so stable.  The object")
    print("  that does carry information is D_k, and it needs no division by lambda_0.")

    print("")
    print("  THE CONSTANT.  C = R_A(xhat) is the sharp Douglas constant.  It is a")
    print("  continuum object (M-stable to %.1f%%) but it is NOT bounded by anything"
          % (100.0 * ray_st))
    print("  explicit yet: the coupling direction xhat is corner-concentrated (T_50")
    print("  above is a large fraction of the grid Nyquist frequency), so no low-")
    print("  frequency argument caps it.  Measured per zone:")
    for z in zones:
        rr = [r for r in rows if r["n"] == z["n"]]
        info("C n=%d" % z["n"],
             "R_A(xhat) = %.2f..%.2f;  needed for the lossy route: <= %.2f..%.2f;  "
             "achieved g_0^2/lam_0 = %.3f..%.3f"
             % (min(r["ray"] for r in rr), max(r["ray"] for r in rr),
                min(r["need"] for r in rr), max(r["need"] for r in rr),
                min(r["wv0"] for r in rr), max(r["wv0"] for r in rr)))

    # ------------------------------------------------------------- R4  X3
    section("R4  X3 -- CERTIFICATES FOR THE E_- AND E_+ DIAGONAL CONDITIONS")
    print("  KEY IDENTITY.  delta < u in every zone, so the autocorrelation of a wing")
    print("  function vanishes at u and")
    print("      (1/2pi) int (1 -+ cos(tu)) |phihat(t)|^2 dt = ||phi||^2   EXACTLY.")
    print("  Hence d nu = (1 -+ cos(tu))|phihat|^2 dt / (2pi||phi||^2) is a PROBABILITY")
    print("  measure and  A_arch|E_-+ / ||f||^2 = int k d nu.  A narrow wing cannot keep")
    print("  its mass at low frequency (Slepian), so the mass is FORCED out to large |t|")
    print("  where k(t) = Re psi(1/4+it/2) - log pi is large and positive.  T97's trace")
    print("  bound threw that positive tail away; this is what certifies E_+.")
    e_ny = 0.0
    for (a_, b_, dl_) in ((0.0, 6.28, 0.20), (1.0, 3.0, 0.40), (3.0, 60.0, 0.05)):
        e_ny = max(e_ny, abs(band_concentration(a_, b_, dl_, 110)
                             - band_concentration(a_, b_, dl_, 200)))
    check("el_cert.nystrom", e_ny <= 1e-9,
          "band concentration eigenvalue N=110 vs N=200 agrees to %.1e" % e_ny)
    lt = band_concentration(0.0, t0, 0.3)
    check("el_cert.trace_bound", lt <= min(1.0, t0 * 0.3 / math.pi) and lt > 0.5,
          "Slepian lam_0 = %.4f < trace bound %.4f (strict improvement)"
          % (lt, min(1.0, t0 * 0.3 / math.pi)))

    print("")
    tables = {}
    for z in zones:
        u, n = z["u"], z["n"]
        kw_m = min(safe_extremes(lambda t: (1.0 - np.cos(t * u)) * kernel_k(t),
                                 1e-9, t0, 20000)[0], 0.0)
        kw_p = min(safe_extremes(lambda t: (1.0 + np.cos(t * u)) * kernel_k(t),
                                 1e-9, t0, 20000)[0], 0.0)
        tables[n] = dict(kw_m=kw_m, kw_p=kw_p)
        info("symbol n=%d" % n,
             "inf_[0,t0] (1-cos(tu))k = %+.4f, inf (1+cos(tu))k = %+.4f  (k(0) = %+.4f: "
             "the t=0 killer is quadratically suppressed on E_-, DOUBLED on E_+)"
             % (kw_m, kw_p, K0_CLOSED))

    print("")
    print("  certificates at the sampled widths (must not exceed the measured value):")
    print("   n   delta   B_-(T97 trace)  B_-(nu bound)  lam_min(Q|E_-)   B_+(nu bound)"
          "  lam_min(Q|E_+)   mu/2")
    val_m, val_p, gain = True, True, []
    for r in rows:
        c = tables[r["n"]]
        rows_m, kt_m = nu_band_table(r["u"], -1, t0, r["delta"])
        rows_p, kt_p = nu_band_table(r["u"], +1, t0, r["delta"])
        Bm = cert_block(r["kidx"], r["u"], r["delta"], -1, rows_m, kt_m)
        Bp = cert_block(r["kidx"], r["u"], r["delta"], +1, rows_p, kt_p)
        Bm97 = ((1.0 - math.cosh(0.5 * r["u"])) * (r["delta"]
                                                   + 2.0 * math.sinh(0.5 * r["delta"]))
                + trace_bound(c["kw_m"], r["delta"], t0)
                - old_atom_penalty(r["kidx"], r["u"], r["delta"]))
        val_m = val_m and Bm <= r["lam_mm"] + 1e-9
        val_p = val_p and Bp <= r["lam_pp"] + 1e-9
        gain.append(Bm - Bm97)
        print("  %2d  %.4f  %14.4f  %13.4f  %14.4f  %14.4f  %14.4f  %6.3f"
              % (r["n"], r["delta"], Bm97, Bm, r["lam_mm"], Bp, r["lam_pp"], 0.5 * r["mu"]))
    check("el_cert.valid_minus", val_m,
          "the E_- certificate is a valid lower bound at all %d samples" % len(rows))
    check("el_cert.valid_plus", val_p,
          "the E_+ certificate is a valid lower bound at all %d samples" % len(rows))
    check("el_cert.improves", min(gain) > 0.0,
          "the nu bound beats the T97 trace bound by %+.3f .. %+.3f at every sample"
          % (min(gain), max(gain)))

    print("")
    print("  certified sub-zones (largest delta at which the condition still holds):")
    fr_m97, fr_m, fr_p = {}, {}, {}
    for z in zones:
        c = tables[z["n"]]
        u, mu, kidx, dmax = z["u"], z["mu"], z["kidx"], z["dmax"]

        def bisect(fn):
            lo, hi = 1e-4, dmax
            if not fn(lo):
                return 0.0
            if fn(hi):
                return dmax
            for _ in range(16):
                md = 0.5 * (lo + hi)
                if fn(md):
                    lo = md
                else:
                    hi = md
            return lo

        def f97(dd):
            return ((1.0 - math.cosh(0.5 * u)) * (dd + 2.0 * math.sinh(0.5 * dd))
                    + trace_bound(c["kw_m"], dd, t0)
                    - old_atom_penalty(kidx, u, dd) + 0.5 * mu) >= 0.0

        def fm(dd):
            rw, kt = nu_band_table(u, -1, t0, dd)
            return (cert_block(kidx, u, dd, -1, rw, kt) + 0.5 * mu) >= 0.0

        def fp(dd):
            rw, kt = nu_band_table(u, +1, t0, dd)
            return (cert_block(kidx, u, dd, +1, rw, kt) - 0.5 * mu) >= 0.0

        d97, dmb, dpl = bisect(f97), bisect(fm), bisect(fp)
        fr_m97[z["n"]], fr_m[z["n"]], fr_p[z["n"]] = d97 / dmax, dmb / dmax, dpl / dmax
        info("cert n=%d" % z["n"],
             "E_-: trace %.0f%% -> nu bound %.0f%% of the zone (delta <= %.4f);  "
             "E_+: %.0f%% (delta <= %.4f)"
             % (100.0 * fr_m97[z["n"]], 100.0 * fr_m[z["n"]], dmb,
                100.0 * fr_p[z["n"]], dpl))
    check("el_cert.subzone_minus", all(fr_m[k] >= fr_m97[k] - 1e-12 for k in fr_m)
          and min(fr_m.values()) > 0.4,
          "E_- certified sub-zone %.0f%%..%.0f%% (T97 route: %.0f%%..%.0f%%)"
          % (100.0 * min(fr_m.values()), 100.0 * max(fr_m.values()),
             100.0 * min(fr_m97.values()), 100.0 * max(fr_m97.values())))
    check("el_cert.subzone_plus", min(fr_p.values()) > 0.0,
          "E_+ condition CERTIFIED (previously only measured) on %.0f%%..%.0f%% of the "
          "zones" % (100.0 * min(fr_p.values()), 100.0 * max(fr_p.values())))

    # ------------------------------------------------------------- R5 skeleton
    section("R5  THE INDUCTION SKELETON -- status of every building block")
    mean_ff = sum(ff.values()) / len(ff)
    mean_fv = sum(fv.values()) / len(fv)
    mean_fm = sum(fr_m.values()) / len(fr_m)
    mean_fm97 = sum(fr_m97.values()) / len(fr_m97)
    mean_fp = sum(fr_p.values()) / len(fr_p)
    skel = [
        ("1  splitting L^2 = E_- (+) E_0 (+) E_+ exact, S_k = diag(-1/2,0,1/2)",
         "PROVED", "T95-C1; re-verified to %.0e" % e_diag),
        ("2  old atoms vanish on E_-/E_+ for delta < atom gap, else -mu_j/2",
         "PROVED", "autocorrelation support + T95-C1 norm bound"),
        ("3  pole restriction (1 -+ cosh(u/2)) P_I with the closed forms",
         "PROVED", "a(x+u) = e^{u/2}a(x); ||a_I|| ||b_I|| = 2 sinh(delta/2) to %.0e" % e_cf),
        ("4  E_0 block = the SAME form at alpha' = log n_k - alpha",
         "PROVED", "self-similarity to %.0e -- this IS the induction hypothesis" % e_self),
        ("5  nu is a probability measure: A_arch|E_-+ = int k d nu",
         "PROVED", "h_phi(u) = 0 for delta < u; the whole R4 certificate rests on it"),
        ("6  E_- diagonal condition lam_min(Q|E_-) + mu_k/2 > 0",
         "CERTIFICATE", "%.0f%% of the zones (T97 trace route: %.0f%%)"
         % (100.0 * mean_fm, 100.0 * mean_fm97)),
        ("7  E_+ diagonal condition lam_min(Q|E_+) - mu_k/2 > 0",
         "CERTIFICATE", "%.0f%% of the zones; NEW -- T97 had this measured only"
         % (100.0 * mean_fp)),
        ("8  Q_-0 v_0 = extension defect = sqrt(2) x odd part of the wing potential",
         "PROVED", "three identities to 1e-11 (R1)"),
        ("9  the law g_0 = O(sqrt(lam_0))",
         "LAW-MEASURED", "boundedness, not a power law: ratio %.2f..%.2f, pooled slope "
         "%+.2f, within-zone slopes far from 1/2" % (rat_lo, rat_hi, s_g0)),
        ("10 MECHANISM of the law: Douglas range inclusion on the PSD block",
         "PROVED-CONDITIONAL", "g_0^2 <= R_A(xhat) lam_0 at every sample, saturating "
         "(%.1fx) at the zone tops; but the PSD input is the conclusion" % tight),
        ("11 the constant C = R_A(xhat)",
         "OPEN", "M-stable to %.1f%% (a continuum object) but not bounded by anything "
         "explicit: xhat is corner-concentrated, so no bandwidth argument caps it"
         % (100.0 * ray_st)),
        ("12 T97's one-vector reading of the Schur weight",
         "REFUTED", "the v_0 term is only %.1f%%..%.0f%% of trace(Schur); the weight is "
         "carried by the bulk of the E_0 spectrum"
         % (100.0 * share_min, 100.0 * share_max)),
        ("13 lam_0 as a physical margin in zones n=3,4,5",
         "REFUTED", "Richardson limit <= 0 on three nested grids: the measured 3e-6 is a "
         "discretisation floor, so g_0^2/lam_0 is not a resolvable object there"),
        ("14 strengthened hypothesis Q_{k-1}|(E_- (+) E_0) >= 0",
         "REFUTED", "J reaches %+.3f: the predecessor is indefinite already on the "
         "wings-plus-centre, so no atom-free PSD input exists" % jmin),
        ("15 THE EXACT REFORMULATION  D_k(alpha) <= mu_k/2",
         "IDENTITY+MEASURED", "lam_min(S11) = J + mu_k/2 to %.0e; D_k <= mu_k/2 at every "
         "sampled alpha (tightest margin %+.1e) and it survives Richardson extrapolation "
         "at the binding end (margin >= %+.4f, drift %.1e) -- this REPLACES the cross "
         "lemma for the E_-/E_0 half of the step"
         % (e_id, min(r["lam_S11"] for r in rows), marg_b, Ddrift)),
        ("16 the E_+ blocks: diagonal certified above, cross blocks Q_-+ , Q_0+",
         "OPEN", "untouched by the atom and not covered by the E_-/E_0 reduction; the "
         "loser puts only %.0f%% of its mass there, so this is the smaller gap"
         % (100.0 * max(wE))),
    ]
    for (what, status, detail) in skel:
        print("  [%-18s] %s" % (status, what))
        print("      %s" % detail)

    # ------------------------------------------------------------- verdict
    section("VERDICT")
    print("  X1  MECHANISM.  The sqrt law is FORCED, not accidental: Douglas (1966)")
    print("      range inclusion applied to the PSD 2x2 block [[Q|E_-+mu/2, Q_-0],")
    print("      [Q_0-, Q|E_0]] gives g_0^2 <= R_A(xhat) lambda_0 identically, and the")
    print("      bound saturates (to %.1fx) exactly at the tops of the zones.  Two" % tight)
    print("      further facts fix the SIZE of the constant: (i) the operator-norm")
    print("      version of Douglas is vacuous (lam_max(Q|E_-) diverges like log(1/d)),")
    print("      while the directional R_A(xhat) is M-stable to %.1f%%; (ii) in every"
          % (100.0 * ray_st))
    print("      zone with predecessors the extension defect is small only because of a")
    print("      three-way cancellation on the wings -- arch against the OLD ATOMS, and")
    print("      the residue against the pole rescue -- worth up to %.0fx; in zone n=2,"
          % max(canc_by_zone.values()))
    print("      which has no old atoms, there is no cancellation and the ratio is")
    print("      largest.  The boundary/Rellich reading is the correct STRUCTURE")
    print("      (identities R1) but does not set the size.")
    print("      But the mechanism is a TAUTOLOGY: g_0 and lambda_0 belong to the same")
    print("      discrete operator, which is PSD, so the law is forced at any resolution")
    print("      and carries no information beyond the positivity being proved.")
    print("  X2  BOUND AND CLOSURE.  The lossy inequality a certificate would have to")
    print("      reach closes on %.0f%% of the zone area (v_0-only reading: %.0f%%), and"
          % (100.0 * mean_ff, 100.0 * mean_fv))
    print("      three of T97's premises do not survive: the Schur weight is not carried")
    print("      by v_0 (%.1f%%..%.0f%% of the trace), lambda_0 is a discretisation floor"
          % (100.0 * share_min, 100.0 * share_max))
    print("      in zones 3-5, and Q_{k-1} is indefinite already on E_- (+) E_0.  What")
    print("      replaces them is an IDENTITY: because the atom is mu_k/2 times the")
    print("      identity on E_-, the E_-/E_0 half of the step is exactly")
    print("          D_k(alpha) = -lam_min(Q|E_- - Q_-0 (Q|E_0)^{-1} Q_0-)  <=  mu_k/2,")
    print("      no constant C and no near-null mode.  D_k is grid-stable (%.0e), it is"
          % Ddrift)
    print("      satisfied in all four zones, and the margin collapses to %+.0e at the"
          % min(r["lam_S11"] for r in rows))
    print("      top of the zone, i.e. exactly where the next atom takes over.")
    print("  X3  UPGRADES.  The probability-measure identity plus multiband Slepian")
    print("      allocation lifts the E_- certificate from %.0f%% to %.0f%% of the zones"
          % (100.0 * mean_fm97, 100.0 * mean_fm))
    print("      and certifies E_+ on %.0f%% -- previously measured only." % (100.0 * mean_fp))
    mech = doug_ok and grow > 1.05 and ray_st < 0.05
    if not (0.02 < rat_lo and rat_hi < 3.0):
        verdict = "CROSS-BLOCKED"
    elif mech and mean_ff >= 0.4:
        verdict = "CROSS-LEMMA-SHAPED"
    else:
        verdict = "LAW-CONFIRMED-MECHANISM-OPEN"
    print("")
    print("  VERDICT: %s" % verdict)
    if verdict == "CROSS-LEMMA-SHAPED":
        print("    Mechanism identified, sharp constant named, and the composed")
        print("    inequality closes on the lower part of every zone.")
    elif verdict == "LAW-CONFIRMED-MECHANISM-OPEN":
        print("    The law reproduces and its mechanism is identified exactly -- Douglas")
        print("    range inclusion -- but that identification DISSOLVES the lemma rather")
        print("    than proving it: the law is a consequence of the positivity it was")
        print("    supposed to help establish, its constant is the Rayleigh quotient")
        print("    R_A(xhat) with no a-priori bound, and the one-vector reading of the")
        print("    Schur weight is refuted.  T97's cross lemma is therefore the wrong")
        print("    target.  What the probe buys instead is a correct target: the E_-/E_0")
        print("    half of the induction step IS the identity-backed scalar inequality")
        print("    D_k(alpha) <= mu_k/2, which is grid-stable, holds in all four zones,")
        print("    and needs no constant at all.  Together with the two diagonal")
        print("    conditions -- now certificates rather than measurements -- the step is")
        print("    reduced to bounding ONE explicit spectral quantity of the predecessor")
        print("    form, plus the E_+ cross blocks.")
    else:
        print("    The law did not reproduce under independent sampling.")

    print("")
    print("TOTAL  checks=%d  pass=%d  fail=%d  runtime=%.1fs"
          % (PASS + FAIL, PASS, FAIL, time.time() - T_START))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
