"""Discovery probe (2026-07-26), part 99 of the zeta/prime investigation.
Contract DK.RECURSION -- the a priori structure behind the T98 target

        D_k(alpha) := -lambda_min( Q_{k-1}|E_-  -  Q_-0 (Q_{k-1}|E_0)^{-1} Q_0- )
                   <=  mu_k / 2,          mu_k = 2 Lambda(n_k) / sqrt(n_k),

attacked with the RECURSION LEVER: by the T97/T98 self-similarity the E_0 block
IS the same form at the smaller window alpha' = log n_k - alpha, so D_k hangs on
the ALREADY SOLVED smaller problem.  The question is whether that dependence is
lawful enough to give a recursive inequality that closes the staircase
induction, and whether the recursion terminates.

THE CONVENTION (T93/T95/T96/T97/T98, unchanged)
  f real, supp f subset (-alpha, alpha), ||f||_2 = 1;  h = f * f~ even.
      P_pole(f) = 2 (int f e^{x/2})(int f e^{-x/2})
      A_arch(f) = (1/2pi) int |fhat(t)|^2 k(t) dt,
                  k(t) = Re psi(1/4 + i t/2) - log pi,  k(0) = -5.3722...
      Q_k(f)    = P_pole + A_arch - sum_{j<=k} mu_j h_f(log n_j)   (Weil 1952)
  Zone k is alpha in (alpha_k, alpha_{k+1}), alpha_k = log(n_k)/2; the geometry
  is one number, the WING WIDTH delta = 2 alpha - u, u = log n_k:
      wings I_L = (-alpha, -alpha'), I_R = I_L + u,  centre (-alpha', alpha'),
      alpha' = u - alpha,  |I_L| = delta,  delta < u in every zone.
  E_-/E_+ are the anti/symmetric two-bump wing pairs, E_0 the centre; the k-th
  atom is diag(-1/2, 0, +1/2) there (T95-C1), so the E_-/E_0 half of the
  induction step is EXACTLY the scalar inequality D_k(alpha) <= mu_k/2 (T98),
  and Q|E_0 = Q_{k-1}(alpha') is the induction hypothesis itself.

WHAT THIS PROBE ADDS
  D1  THE RECURSION STRUCTURE, and the exact selection rule that governs it.
      Every block here is CENTRO-SYMMETRIC (arch and atoms are Toeplitz, the
      pole part a b^T + b a^T is swapped by reflection), so with the reflection
      operators J_- (on E_-) and J_0 (on E_0)
              J_- Q|E_- J_- = Q|E_- ,  J_0 Q|E_0 J_0 = Q|E_0 ,
              J_- Q_-0 J_0  = - Q_-0                          (machine-checked),
      i.e. the CROSS BLOCK ANTICOMMUTES with reflection.  Hence the Schur
      complement is reflection-block-diagonal and the whole problem splits into
      TWO DECOUPLED PARITY CHANNELS,
              D_k = max( D_k^even , D_k^odd ),
      in which the reflection-even half of E_- sees ONLY the reflection-ODD
      spectrum of the smaller window and vice versa.  In particular the near
      null ground mode v_0 of the smaller window -- the fragile floor that T98
      showed to be discretisation-limited -- is reflection-EVEN and is therefore
      EXACTLY ABSENT from the channel that binds.  Inside each channel the
      Schur weight  x^T W x = sum_j |<phi_j, Q_0- x>|^2 / lambda_j  is resolved
      over the eigenbasis of the smaller problem and the decay law
      |<phi_j, Q_0- x>|^2 ~ lambda_j^theta is fitted on the low-lambda end (the
      only end where 1/lambda_j can hurt).  theta > 1 means the Schur sum is
      carried by the BULK, not by the floor -- the Sobolev-flavoured statement
      that a boundary-localised extension defect is nearly orthogonal to the
      near-null modes of the smaller window.
  D2  THE RECURSIVE INEQUALITY.  Since the k-th atom is (mu_k/2) I on E_-, the
      target is the operator statement  W <= A_sh := Q|E_- + (mu_k/2) I, i.e.
          rho := lambda_max(A_sh^{-1/2} W A_sh^{-1/2}) <= 1   (A_sh > 0),
      and the elementary chain
          x^T W x = (Q_0- x)^T Q_00^{-1} (Q_0- x) <= J_sup ||Q_0- x||^2
                                                  <= J_sup R_G (x^T A_sh x)
      gives the VALID two-factor bound  rho <= R_G * J_sup, per channel, with
          R_G   = sup ||Q_0- x||^2 / (x^T A_sh x)        [wing / defect side]
          J_sup = lambda_max( P_R Q_00^{-1} P_R |_R )    [smaller window]
      -- the first factor a delta-local Rayleigh quotient fed by the exact
      extension identity and the three-way arch/pole/old-atom cancellation, the
      second a pure INDUCTION-DATA object of the smaller window seen through
      the defect subspace.  J_sup <= 1/lambda_1(channel) always; the parity rule
      and the decay law are what make it smaller, and the two gains
      lambda_1^odd/lambda_1^even and 1/(lambda_1^chan J_sup) measure exactly
      that.  TERMINATION: alpha' = u_k - alpha < u_k/2 = alpha_k, so every
      recursion step drops STRICTLY into a lower zone and the chain reaches the
      classical prime-free window alpha < log 2 / 2 in at most k steps.
  D3  THE TOP OF THE ZONE.  The margin mu_k/2 - D_k(alpha) is tracked on an
      epsilon-ladder into the zone top alpha_{k+1} (where the next atom takes
      over, T96/T97 saturation) to ask whether the handoff is an EQUALITY in
      the limit, with power-law fits, grid drift, and cross-zone universality.
  D4  SYNTHESIS -- the induction skeleton, per-brick status, and the honest
      answer about what is still missing.

PREREGISTERED VERDICTS
  RECURSION-CLOSES : the law + a valid recursive inequality that closes with
                     margin over the zone map + verified termination.
  DECAY-LAW-FOUND  : the law stands and the inequality closes only in part --
                     with the failing part named.
  NO-RECURSION     : no law; the bulk dependence is unstructured.
  The law is scored in its FIT-FREE form (floor avoidance: gain 1/(lam_1 J_sup)
  >= 10 in every zone that has a near-null tail, with J_sup grid-stable while
  1/lam_1 is not), because that is the form the inequality actually uses; the
  power-law exponent theta is reported alongside and is only meaningful in
  zones that have a tail at all.
  Element gates: el_firewall, el_kernel, el_forms, el_split, el_selfsim,
  el_parity, el_schur, el_target, el_chain, el_classic, el_valid, el_cert.

OUTCOME OF THIS RUN  =>  DECAY-LAW-FOUND
  23 checks, 0 failures, 11 s, largest array 1900^2.
  D1  The governing structure is not a soft law but an EXACT SELECTION RULE:
      J_- Q_-0 J_0 = -Q_-0 to 2e-15, so D_k = max(D_even, D_odd) (to 1e-11) and
      the reflection-even half of E_- -- which binds at 24/24 map samples --
      couples only to the reflection-ODD spectrum of the smaller window.  The
      near-null EVEN ground mode v_0, the discretisation-limited floor of T98,
      is therefore exactly absent from the binding channel; the parity gap
      lam_1^odd/lam_1^even is 3.0..111.5.  On top of that the coupling avoids
      the remaining odd tail: the fit-free gain 1/(lam_1 J_sup) is 43..71262 in
      the three zones that have a tail (zone n=2 has none -- its smaller window
      is the classical one, lam_1 = 0.17..0.72), and the power-law form
      |<phi_j, Q_0- x>|^2 ~ lambda_j^theta holds with theta = 1.15..2.18 at
      R2 = 0.89..1.00 in zones n=4, 5 and only theta = 0.22..0.90 in n=3.
      The extension defect itself is reproduced exactly by arch + pole + old
      atoms with a three-way cancellation worth 1.4x..2.0x (zone n=2 has no old
      atoms and no cancellation).
  D2  The target is the operator statement W <= A_sh, i.e. rho <= 1 (verified
      equivalent to D_k <= mu_k/2 at every sample), and the recursive chain
      rho <= R_G * J_sup is valid at all 24 samples with a separation loss of
      only 1.01x..1.20x once the spectrum of the smaller window is split at a
      threshold.  R_G (0.30..1.40) and J_sup drift 0.3% and 2.9% over three
      nested grids while 1/lam_1 drifts 74%: the two factors of the inequality
      are continuum objects even though the floor they replace is not.  Where
      the bound closes it needs only the smaller-window modes below Lam_ok =
      0.97..3.69 -- 1..16 modes, 0.1%..4.2% of the spectrum.  It closes on the
      LOWER part of every zone (11/24 samples, 6/6 in zone n=2) and fails on
      the upper part of zones n=3,4,5 for a single named reason: the uniform
      bulk remainder R_G/lam_top = 0.04..0.19 exceeds the true slack 1 - rho,
      which falls to 1e-3 there.  The bound closes at EXACTLY the 11 samples
      where rho <= 1 - R_G/lam_top, so it is optimal within its family.
      Termination is arithmetic: alpha' = u_k - alpha < alpha_k drops the zone
      index strictly, so 240/240 starting windows reach the classical
      prime-free window in at most 4 steps (zone n=5: 0.8888 -> 0.7206 ->
      0.6657 -> 0.4329 -> 0.2602 classical).
  D3  The zone tops are NOT a universal equality.  Extrapolating the margin to
      eps = 0 gives +2.7e-2 (n=2), +1.4e-2 (n=3), +1.7e-2 (n=4) -- 2.2%..5.5%
      of mu_k/2 -- but -2.0e-4 at n=5, and at fixed eps = 0.002 the n=5 margin
      Richardson-extrapolates over three grids to -1.1e-5.  So D_k(alpha_top) =
      mu_k/2 is a zone-5 phenomenon; elsewhere the handoff has slack.  The
      approach exponents q = 0.20..0.67 are not universal either (R2 down to
      0.63) and the eps-ladder near the top is grid-limited at 1e-2 for n=4.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit, no
    verification/ module, no next.txt edit, no .md output.
  * NO Riemann zero data of any kind; the AST firewall rejects zero-table
    tokens, network imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  A negative
    lambda_min on a genuine window direction is an IMPLEMENTATION SIGNAL,
    fenced, never reported as mathematics.
  * lambda_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute positivity, never prove it.  Every ratio
    with a near-null lambda_1 in the denominator inherits the discretisation
    floor that T98 documented; the probe therefore reports grid drift for every
    object it proposes as a continuum quantity.
  * No "proved" language without a certificate.  Classical anchors cited, not
    re-derived: Weil 1952, Yoshida 1992 / Bombieri 2000 / Connes-Consani 2021,
    the digamma archimedean kernel, Rayleigh-Ritz, Paley-Wiener, Schur
    complements, Douglas 1966 range inclusion, centrosymmetric-matrix block
    diagonalisation (Cantoni-Butler 1976), Slepian-Pollak-Landau prolate
    concentration, and the Sobolev/spectral-decay heuristic (cited as the
    ANALOGUE only: the operator here is nonlocal, so no Sobolev embedding is
    claimed -- the decay exponent is measured, not derived).
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
M_CAP = 1900                 # main sweep
CAPS3 = (900, 1300, 1900)    # nested grids
FENCE = -1e-9
GRID_BAND = 5.0e-3           # T98 grid drift of D_k at the binding end
MAXN_SEEN = 0

# (n, log n, mu_n = 2 Lambda(n)/sqrt(n))
ATOMS = (
    (2, math.log(2.0), 2.0 * math.log(2.0) / math.sqrt(2.0)),
    (3, math.log(3.0), 2.0 * math.log(3.0) / math.sqrt(3.0)),
    (4, math.log(4.0), 2.0 * math.log(2.0) / 2.0),
    (5, math.log(5.0), 2.0 * math.log(5.0) / math.sqrt(5.0)),
)
ALPHA_NEXT_ATOM = math.log(7.0) / 2.0
ALPHA_CLASSIC = math.log(2.0) / 2.0
T98_TOP_MARGIN = {2: 3.7e-2, 3: 1.9e-2, 4: 2.2e-2, 5: 4.8e-4}

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
    check("el_firewall.imports", not bad_imports,
          "import roots %s" % sorted(ALLOWED_IMPORT_ROOTS))
    check("el_firewall.no_writes", not bad_writes, "no write-mode open()")


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
#   basis phi_i = 1_{cell i} / sqrt(d),  d = 2 alpha / M   (orthonormal)
# ----------------------------------------------------------------------------
_IDX_CACHE = {}


def index_matrix(M):
    global MAXN_SEEN
    MAXN_SEEN = max(MAXN_SEEN, M)
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
    Q = prime_free_matrix(alpha, M)
    for (_n, u, mu) in ATOMS[:kidx]:
        Q -= mu * atom_matrix(u, alpha, M)
    return Q


def lam_min(Mx):
    return float(eigvalsh(Mx, subset_by_index=[0, 0])[0])


def lam_max(Mx):
    return float(eigvalsh(Mx, subset_by_index=[Mx.shape[0] - 1, Mx.shape[0] - 1])[0])


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
    rng = np.random.default_rng(9901)
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
    check("el_forms.atom_toeplitz", worst <= 1e-12,
          "max |Toeplitz - direct| = %.2e" % worst)


# ----------------------------------------------------------------------------
# wing-aligned grid, the E_-/E_0/E_+ splitting, and the reflection parity bases
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
    """The four blocks of U^T Q U needed here, without forming U."""
    QLL = Q[0:nI, 0:nI]
    QLR = Q[0:nI, m:m + nI]
    QRR = Q[m:m + nI, m:m + nI]
    QLC = Q[0:nI, nI:m]
    QRC = Q[m:m + nI, nI:m]
    Qmm = 0.5 * (QLL - QLR - QLR.T + QRR)
    Qpp = 0.5 * (QLL + QLR + QLR.T + QRR)
    Qm0 = (QLC - QRC) / SQ2
    Q00 = Q[nI:m, nI:m]
    return Qmm, Q00, Qpp, Qm0


def parity_basis(n):
    """Orthonormal bases of the reflection-even / -odd subspaces (J v = v[::-1])."""
    ke, ko = (n + 1) // 2, n // 2
    Be = np.zeros((n, ke))
    Bo = np.zeros((n, ko))
    r = 1.0 / SQ2
    for i in range(n // 2):
        Be[i, i] = r
        Be[n - 1 - i, i] = r
        Bo[i, i] = r
        Bo[n - 1 - i, i] = -r
    if n % 2:
        Be[n // 2, ke - 1] = 1.0
    return Be, Bo


# ----------------------------------------------------------------------------
# zone bookkeeping and the recursion map alpha -> alpha' = u_k - alpha
# ----------------------------------------------------------------------------
def alpha_top(kidx):
    return 0.5 * ATOMS[kidx + 1][1] if kidx + 1 < len(ATOMS) else ALPHA_NEXT_ATOM


def delta_max(kidx):
    return 2.0 * alpha_top(kidx) - ATOMS[kidx][1]


def zone_of(alpha):
    """-1 = classical prime-free window; len(ATOMS) = beyond the modelled table."""
    if alpha < ALPHA_CLASSIC:
        return -1
    if alpha >= ALPHA_NEXT_ATOM:
        return len(ATOMS)
    k = -1
    for i, (_n, u, _mu) in enumerate(ATOMS):
        if alpha > 0.5 * u:
            k = i
    return k


def recursion_chain(alpha, maxstep=16):
    """alpha -> alpha' = u_{zone(alpha)} - alpha until the classical window."""
    chain = []
    a = alpha
    for _ in range(maxstep):
        k = zone_of(a)
        if k < 0 or k >= len(ATOMS):
            chain.append((a, k, None))
            return chain, True
        a2 = ATOMS[k][1] - a
        chain.append((a, k, a2))
        a = a2
    return chain, False


# ----------------------------------------------------------------------------
# the per-sample computation
# ----------------------------------------------------------------------------
def build_blocks(kidx, delta_target, m_cap):
    n, u, mu = ATOMS[kidx]
    alpha, M, m, nI, delta = wing_grid(u, delta_target, m_cap)
    A = arch_matrix(alpha, M)
    av, bv = pole_vectors(alpha, M)
    P = np.outer(av, bv)
    Q = A + P + P.T
    atom_ops = []
    for (_nj, uj, muj) in ATOMS[:kidx]:
        Sj = atom_matrix(uj, alpha, M)
        Q -= muj * Sj
        atom_ops.append((muj, Sj))
    Qmm, Q00, Qpp, Qm0 = fast_blocks(Q, m, nI)
    return dict(n=n, u=u, mu=mu, alpha=alpha, M=M, m=m, nI=nI, delta=delta,
                n0=M - 2 * nI, d=2.0 * alpha / M, Q=Q, A=A, av=av, bv=bv,
                atom_ops=atom_ops, Qmm=Qmm, Q00=Q00, Qpp=Qpp, Qm0=Qm0)


def dk_only(kidx, delta_target, m_cap):
    """D_k and the margin only -- Cholesky route, no eigendecomposition."""
    b = build_blocks(kidx, delta_target, m_cap)
    cf = cho_factor(b["Q00"], lower=True, check_finite=False)
    W = b["Qm0"] @ cho_solve(cf, b["Qm0"].T, check_finite=False)
    W = 0.5 * (W + W.T)
    Dk = -lam_min(b["Qmm"] - W)
    return dict(n=b["n"], alpha=b["alpha"], delta=b["delta"], d=b["d"], nI=b["nI"],
                n0=b["n0"], Dk=Dk, half_mu=0.5 * b["mu"], margin=0.5 * b["mu"] - Dk)


def loglog_fit(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    ok = (x > 0) & (y > 0) & np.isfinite(x) & np.isfinite(y)
    if int(ok.sum()) < 3:
        return float("nan"), float("nan")
    lx, ly = np.log(x[ok]), np.log(y[ok])
    s, b = np.polyfit(lx, ly, 1)
    ss = float(np.sum((ly - (s * lx + b)) ** 2))
    st = float(np.sum((ly - ly.mean()) ** 2))
    return float(s), (1.0 - ss / st if st > 0 else float("nan"))


TAIL_GAP = 1e-3          # lam_1 < TAIL_GAP * lam_top  =>  a genuine near-null tail


def tail_fit(lam, wgt, kmax=14, lam_frac=0.10, kmin=6):
    """Log-log fit of the coupling weight over the LOW-lambda tail of a channel.

    The bulk of the smaller window's spectrum is a dense cluster near the top;
    only a handful of modes sit below it, and those are the only ones whose
    1/lambda can hurt.  The fit therefore runs over the individual tail modes,
    not over lambda-bins -- and it is only reported when a tail EXISTS: where
    lambda_1 is already O(lambda_top) there is no floor to avoid and the
    exponent would be fitted to the bottom of the bulk, which is meaningless."""
    idx = np.argsort(lam)
    l, w = lam[idx], wgt[idx]
    if l[0] >= TAIL_GAP * l[-1]:
        return float("nan"), float("nan"), 0
    ntail = int((l <= lam_frac * l[-1]).sum())
    ntail = min(max(ntail, kmin), kmax, l.size)
    th, r2 = loglog_fit(l[:ntail], w[:ntail])
    return th, r2, ntail


def channel(Amm, Q00c, Gc, mu):
    """One reflection channel: Schur weight, target, and the two bound factors.

    Gc has shape (dim E_0 channel) x (dim E_- channel); its columns are Q_0- x."""
    nI = Gc.shape[1]
    lam, Phi = eigh(Q00c)
    C = Phi.T @ Gc
    W = (C / lam[:, None]).T @ C
    W = 0.5 * (W + W.T)
    S = Amm - W
    evS, XS = eigh(S)
    Dk = -float(evS[0])
    x = np.ascontiguousarray(XS[:, 0])
    Ash = Amm + 0.5 * mu * np.eye(nI)
    lamA = float(eigvalsh(Ash, subset_by_index=[0, 0])[0])

    cx = C @ x
    G2 = float(cx @ cx)
    wg = cx * cx / lam
    tot = float(wg.sum())
    Jx = tot / G2 if G2 > 0 else float("nan")
    px = cx * cx / G2 if G2 > 0 else np.zeros_like(cx)
    cw = np.cumsum(wg) / tot if tot > 0 else np.zeros_like(wg)
    lam_med = float(lam[int(np.searchsorted(cw, 0.5))]) if tot > 0 else float("nan")
    frac_floor = float(wg[lam < 10.0 * lam[0]].sum()) / tot if tot > 0 else float("nan")

    Qr, _ = np.linalg.qr(Gc)
    CR = Phi.T @ Qr
    Msub = (CR / lam[:, None]).T @ CR
    Jsup = lam_max(0.5 * (Msub + Msub.T))

    th_x, r2_x, nt = tail_fit(lam, px)
    sden = (CR * CR).sum(axis=1)
    th_s, r2_s, _ = tail_fit(lam, sden)
    # spectral integral of the smaller window under the fitted law
    if np.isfinite(th_x):
        num = float(np.sum(lam ** (th_x - 1.0)))
        den = float(np.sum(lam ** th_x))
        J_law = num / den if den > 0 else float("nan")
    else:
        J_law = float("nan")

    GG = Gc.T @ Gc
    B_rk, J_star = float("nan"), -1
    if lamA > 1e-12:
        rho = float(eigh(W, Ash, eigvals_only=True)[-1])
        R_G = float(eigh(GG, Ash, eigvals_only=True)[-1])
        # FINITE-RANK + BULK refinement (also fit-free and valid):
        #   Q_00^{-1} <= sum_{j<J} lam_j^{-1} phi_j phi_j^T + lam_J^{-1} P_{>=J}
        #   => rho <= ||Z_J||_op^2 + R_G / lam_J,  Z_J = [A_sh^{-1/2} G^T phi_j
        #      / sqrt(lam_j)]_{j<J}
        # so only FINITELY MANY modes of the smaller window enter explicitly.
        aw, AV = eigh(Ash)
        Zr = C @ ((AV / np.sqrt(aw)) @ AV.T)
        ladder = [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256,
                  384, 512, 768, lam.size - 1]
        best, bestJ, J_ok = float("inf"), 0, -1
        for J in sorted({j for j in ladder if 0 <= j <= lam.size - 1}):
            val = R_G / lam[J]
            if J > 0:
                T = Zr[:J] / np.sqrt(lam[:J])[:, None]
                s1 = float(np.linalg.svd(T, compute_uv=False)[0])
                val += s1 * s1
            if val < best:
                best, bestJ = val, J
            if val <= 1.0 and J_ok < 0:
                J_ok = J
        B_rk, J_star = best, bestJ
    else:
        rho = R_G = float("nan")
    return dict(lam1=float(lam[0]), lam_top=float(lam[-1]), Dk=Dk, lamA=lamA,
                x=x, G2=G2, Jx=Jx, Jsup=Jsup, J_law=J_law, rho=rho, R_G=R_G,
                prod=R_G * Jsup, B_rk=B_rk, J_star=J_star, J_ok=J_ok,
                lam_ok=float(lam[J_ok]) if J_ok >= 0 else float("nan"),
                frac_ok=J_ok / float(lam.size) if J_ok >= 0 else float("nan"),
                lam_Jstar=float(lam[J_star]) if J_star >= 0 else float("nan"),
                frac_Jstar=J_star / float(lam.size) if J_star >= 0 else float("nan"),
                B_floor=R_G / float(lam[-1]) if np.isfinite(R_G) else float("nan"),
                Bmin=min(R_G * Jsup, B_rk), has_tail=float(lam[0]) < TAIL_GAP * float(lam[-1]),
                gain=1.0 / (float(lam[0]) * Jsup) if Jsup > 0 else float("nan"),
                th_x=th_x, r2_x=r2_x, th_s=th_s, r2_s=r2_s, ntail=nt,
                lam_med=lam_med, frac_floor=frac_floor, W=W, Ash=Ash, dim=nI)


def rec_sample(kidx, delta_target, m_cap, want_split=False, want_audit=False):
    """The parity-resolved recursion picture at one (zone, delta) sample."""
    b = build_blocks(kidx, delta_target, m_cap)
    nI, n0, mu = b["nI"], b["n0"], b["mu"]
    Qmm, Q00, Qm0 = b["Qmm"], b["Q00"], b["Qm0"]

    e_par = max(float(np.max(np.abs(Qmm - Qmm[::-1, ::-1]))),
                float(np.max(np.abs(Q00 - Q00[::-1, ::-1]))),
                float(np.max(np.abs(Qm0 + Qm0[::-1, ::-1]))))
    Be, Bo = parity_basis(nI)
    Ce, Co = parity_basis(n0)
    e_cross = max(float(np.max(np.abs(Be.T @ Qm0 @ Ce))),
                  float(np.max(np.abs(Bo.T @ Qm0 @ Co)))) if nI > 1 else 0.0

    chans = {}
    # reflection-even E_- couples to the reflection-ODD spectrum of the window
    chans["even"] = channel(Be.T @ Qmm @ Be, Co.T @ Q00 @ Co,
                            np.ascontiguousarray((Be.T @ Qm0 @ Co).T), mu)
    chans["odd"] = channel(Bo.T @ Qmm @ Bo, Ce.T @ Q00 @ Ce,
                           np.ascontiguousarray((Bo.T @ Qm0 @ Ce).T), mu)
    binder = "even" if chans["even"]["Dk"] >= chans["odd"]["Dk"] else "odd"
    ch = chans[binder]
    Dk = ch["Dk"]

    lam_e = float(eigvalsh(Ce.T @ Q00 @ Ce, subset_by_index=[0, 0])[0])
    lam_o = float(eigvalsh(Co.T @ Q00 @ Co, subset_by_index=[0, 0])[0])

    out = dict(n=b["n"], kidx=kidx, u=b["u"], mu=mu, alpha=b["alpha"], delta=b["delta"],
               alpha_p=b["u"] - b["alpha"], M=b["M"], nI=nI, n0=n0, d=b["d"],
               half_mu=0.5 * mu, Dk=Dk, margin=0.5 * mu - Dk, binder=binder,
               lam1_even=lam_e, lam1_odd=lam_o, parity_gap=lam_o / lam_e,
               e_par=e_par, e_cross=e_cross, chans=chans)
    for key in ("lam1", "lam_top", "lamA", "G2", "Jx", "Jsup", "J_law", "rho", "R_G",
                "prod", "B_rk", "J_star", "J_ok", "lam_ok", "frac_ok", "lam_Jstar",
                "frac_Jstar", "B_floor", "Bmin", "has_tail", "gain", "th_x", "r2_x",
                "th_s", "r2_s", "ntail", "lam_med", "frac_floor"):
        out[key] = ch[key]

    if want_audit:
        # the unsplit reference: same D_k, and the T98 target identity
        cf = cho_factor(Q00, lower=True, check_finite=False)
        Wf = Qm0 @ cho_solve(cf, Qm0.T, check_finite=False)
        Wf = 0.5 * (Wf + Wf.T)
        out["Dk_full"] = -lam_min(Qmm - Wf)
        out["lam_S11"] = lam_min(Qmm + 0.5 * mu * np.eye(nI) - Wf)

    if want_split:
        # exact extension identity + three-way cancellation at the binding vector
        Bx = Be if binder == "even" else Bo
        xfull = Bx @ ch["x"]
        M, m = b["M"], b["m"]
        xt = np.zeros(M)
        xt[0:nI] = xfull / SQ2
        xt[m:m + nI] = -xfull / SQ2
        gA = (b["A"] @ xt)[nI:m]
        qa = float(b["av"] @ xt)
        qb = float(b["bv"] @ xt)
        gP = (qb * b["av"] + qa * b["bv"])[nI:m]
        gS = np.zeros(n0)
        for (muj, Sj) in b["atom_ops"]:
            gS -= muj * (Sj @ xt)[nI:m]
        gtot = gA + gP + gS
        gref = Qm0.T @ xfull
        out["id_ext"] = float(np.max(np.abs(gtot - gref)))
        parts = (float(np.linalg.norm(gA)), float(np.linalg.norm(gP)),
                 float(np.linalg.norm(gS)))
        out["parts"] = parts
        out["gnorm"] = float(np.linalg.norm(gtot))
        out["cancel"] = sum(parts) / max(1e-300, out["gnorm"])
    return out


def richardson(ds, vals):
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


def drift(vals):
    v = [x for x in vals if np.isfinite(x)]
    if len(v) < 2 or abs(v[-1]) < 1e-300:
        return float("nan")
    return abs(v[-1] - v[0]) / abs(v[-1])


# ----------------------------------------------------------------------------
def main():
    section("DK.RECURSION -- part 99 -- gates")
    firewall()
    gate_kernel()
    gate_forms()

    # -------------------------------------------------------- R0  the anchors
    section("R0  ANCHORS -- block algebra, self-similarity, classical floor")
    al, M, m, nI, dl = wing_grid(ATOMS[1][1], 0.06, 500)
    Qs = zone_forms(1, al, M)
    U, nI2, n0 = split_basis(M, m)
    QB = U.T @ (Qs @ U)
    fb = fast_blocks(Qs, m, nI)
    e_blk = max(float(np.max(np.abs(fb[0] - QB[:nI, :nI]))),
                float(np.max(np.abs(fb[1] - QB[nI:nI + n0, nI:nI + n0]))),
                float(np.max(np.abs(fb[2] - QB[nI + n0:, nI + n0:]))),
                float(np.max(np.abs(fb[3] - QB[:nI, nI:nI + n0]))))
    check("el_split.fast_blocks", e_blk <= 1e-13 and nI2 == nI,
          "fast block extraction == U^T Q U to %.1e" % e_blk)
    Sk = atom_matrix(ATOMS[1][1], al, M)
    SB = U.T @ (Sk @ U)
    dref = np.concatenate([-0.5 * np.ones(nI), np.zeros(n0), 0.5 * np.ones(nI)])
    e_diag = float(np.max(np.abs(SB - np.diag(dref))))
    check("el_split.atom_diag", e_diag <= 1e-13,
          "S_k = diag(-1/2, 0, +1/2) to %.1e -- the mu_k/2 shift on E_-" % e_diag)

    ap = ATOMS[1][1] - al
    Qsm = prime_free_matrix(ap, n0) - ATOMS[0][2] * atom_matrix(ATOMS[0][1], ap, n0)
    e_self = float(np.max(np.abs(Qsm - fb[1])))
    check("el_selfsim.E0_block", e_self <= 1e-11,
          "Q|E_0 = Q_{k-1}(alpha' = %.5f) to %.1e -- the recursion lever" % (ap, e_self))

    # probability-measure identity: h_phi(u) = 0 for a single wing (delta < u)
    rng = np.random.default_rng(9902)
    phi = np.zeros(M)
    phi[0:nI] = rng.normal(size=nI)
    phi /= np.linalg.norm(phi)
    hphi = float(phi @ (Sk @ phi))
    check("el_cert.prob_measure", abs(hphi) <= 1e-14,
          "h_phi(u) = %.1e for supp phi = one wing (|I| = %.4f < u = %.4f) => "
          "(1 -+ cos(tu))|phihat|^2 dt/2pi is a PROBABILITY measure, A_arch|E_-+ "
          "= int k dnu" % (hphi, dl, ATOMS[1][1]))

    worst_cl = 1e9
    for a in (0.10, 0.20, 0.30, ALPHA_CLASSIC - 1e-3):
        worst_cl = min(worst_cl, lam_min(prime_free_matrix(a, 600)))
    check("el_classic.floor", worst_cl >= FENCE,
          "min lambda_min(P_pole + A_arch) = %+.3e for alpha < log2/2 = %.4f "
          "(classical prime-free window; Yoshida 1992 / Bombieri 2000)"
          % (worst_cl, ALPHA_CLASSIC))

    for kidx, (n, u, mu) in enumerate(ATOMS):
        info("zone n=%d" % n,
             "alpha in (%.4f, %.4f)  delta_max = %.4f  mu_k/2 = %.4f  "
             "alpha' in (%.4f, %.4f)"
             % (0.5 * u, alpha_top(kidx), delta_max(kidx), 0.5 * mu,
                u - alpha_top(kidx), 0.5 * u))

    # -------------------------------------------------------- R1  D1 the law
    section("R1  D1 -- THE RECURSION STRUCTURE: parity rule + spectral profile")
    print("  Reflection algebra:  J Q|E_- J = Q|E_-,  J Q|E_0 J = Q|E_0,")
    print("  J Q_-0 J = -Q_-0  =>  the Schur complement is parity block diagonal,")
    print("  D_k = max(D_even, D_odd), and each E_- parity sees ONLY the OPPOSITE")
    print("  parity of the smaller window's spectrum (Cantoni-Butler 1976 shape).")
    print("")
    d1_rows = []
    for kidx, (n, u, mu) in enumerate(ATOMS):
        for fr in (0.15, 0.45, 0.80):
            d1_rows.append(rec_sample(kidx, fr * delta_max(kidx), M_CAP,
                                      want_split=True, want_audit=True))
    e_par = max(r["e_par"] for r in d1_rows)
    e_cross = max(r["e_cross"] for r in d1_rows)
    check("el_parity.algebra", e_par <= 1e-12,
          "centro-symmetry of Q|E_-, Q|E_0 and anti-centro-symmetry of Q_-0 to %.1e"
          % e_par)
    check("el_parity.selection_rule", e_cross <= 1e-12,
          "cross-parity coupling blocks vanish to %.1e -- the near-null EVEN mode "
          "v_0 of the smaller window is EXACTLY decoupled from the even E_- channel"
          % e_cross)
    e_dk = max(abs(r["Dk"] - r["Dk_full"]) for r in d1_rows)
    check("el_schur.parity_split", e_dk <= 1e-10,
          "max(D_even, D_odd) = D_k of the unsplit Schur complement to %.1e" % e_dk)
    e_t98 = max(abs(r["lam_S11"] - r["margin"]) for r in d1_rows)
    check("el_target.identity", e_t98 <= 1e-10,
          "lambda_min(Q|E_- + (mu_k/2)I - W) = mu_k/2 - D_k to %.1e -- the T98 "
          "target is exactly the operator statement W <= A_sh" % e_t98)
    e_ext = max(r["id_ext"] for r in d1_rows)
    check("el_schur.extension_id", e_ext <= 1e-11,
          "Q_0- x = (Q xtilde)|centre = arch + pole + old atoms, to %.1e -- the "
          "extension defect of the induction hypothesis, exactly" % e_ext)

    print("  n   delta   n0    binder  lam1_even  lam1_odd   odd/even  lam1(chan) "
          " lam_med/lam1  floor-share  tail?")
    for r in d1_rows:
        print("  %d  %6.4f  %4d  %-6s  %.3e  %.3e  %8.1f  %.3e  %11.1f  %10.2e  %s"
              % (r["n"], r["delta"], r["n0"], r["binder"], r["lam1_even"],
                 r["lam1_odd"], r["parity_gap"], r["lam1"],
                 r["lam_med"] / r["lam1"], r["frac_floor"],
                 "yes" if r["has_tail"] else "no"))
    print("")
    print("  the decay law in the binding channel:  |<phi_j, Q_0- x>|^2 ~ lambda_j^theta,")
    print("  fitted over the low-lambda tail; reported ONLY where a tail exists")
    print("  (lam_1 < %.0e lam_top).  The fit-free form of the same statement is the" % TAIL_GAP)
    print("  SUPPRESSION GAIN 1/(lam_1 J_sup): how far the defect subspace keeps the")
    print("  Schur sum away from the floor 1/lam_1.")
    print("  n   delta   tail  theta_x   R2     theta_s   R2     lam_top   J_x      "
          "J_sup      gain")
    for r in d1_rows:
        print("  %d  %6.4f  %4d  %7.2f  %5.3f  %7.2f  %5.3f  %.3e  %.2e  %.3e  %9.1f"
              % (r["n"], r["delta"], r["ntail"], r["th_x"], r["r2_x"], r["th_s"],
                 r["r2_s"], r["lam_top"], r["Jx"], r["Jsup"], r["gain"]))
    print("")
    print("  three-way cancellation of the extension defect at the binding vector:")
    print("  n   delta   ||g_arch||  ||g_pole||  ||g_atom||  ||g||       cancel")
    for r in d1_rows:
        pa, pp, ps = r["parts"]
        print("  %d  %6.4f  %10.3e  %10.3e  %10.3e  %10.3e  %6.2f"
              % (r["n"], r["delta"], pa, pp, ps, r["gnorm"], r["cancel"]))

    th_all = [r["th_x"] for r in d1_rows if np.isfinite(r["th_x"])]
    tail_zones, zone_theta = [], {}
    for kidx, (n, _u, _mu) in enumerate(ATOMS):
        rs = [r for r in d1_rows if r["kidx"] == kidx]
        ts = [r["th_x"] for r in rs if np.isfinite(r["th_x"])]
        r2 = [r["r2_x"] for r in rs if np.isfinite(r["r2_x"])]
        has = any(r["has_tail"] for r in rs)
        if has:
            tail_zones.append(n)
        zone_theta[n] = (float(np.median(ts)) if ts else float("nan"),
                         float(np.median(r2)) if r2 else float("nan"))
        info("theta n=%d" % n, "%s: median theta_x = %.2f (R2 = %.3f), gain = "
             "%.0f..%.0f over 3 delta samples"
             % ("near-null tail" if has else "NO tail (lam_1 = %.2e ~ lam_top)"
                % min(r["lam1"] for r in rs), zone_theta[n][0], zone_theta[n][1],
                min(r["gain"] for r in rs), max(r["gain"] for r in rs)))
    n_pow = sum(1 for n in tail_zones
                if zone_theta[n][0] > 1.0 and zone_theta[n][1] >= 0.70)
    info("D1 decay law", "tail zones n = %s; power-law form theta > 1 at R2 >= 0.70 in "
         "%d/%d of them (theta_x = %.2f..%.2f); parity gap lam1_odd/lam1_even = "
         "%.1f..%.1f over all zones"
         % (tail_zones, n_pow, len(tail_zones), min(th_all), max(th_all),
            min(r["parity_gap"] for r in d1_rows),
            max(r["parity_gap"] for r in d1_rows)))

    # ------------------------------------------- R2  D2 the recursive inequality
    section("R2  D2 -- THE RECURSIVE INEQUALITY  rho <= R_G * J_sup")
    print("  target      D_k <= mu_k/2  <=>  rho := lam_max(A_sh^{-1/2} W A_sh^{-1/2}) <= 1")
    print("  valid chain rho <= R_G * J_sup   (Cauchy-Schwarz, per parity channel)")
    print("     R_G   = sup ||Q_0- x||^2 / (x^T A_sh x)         [wing / defect side]")
    print("     J_sup = lam_max(P_R Q_00^{-1} P_R|_R) <= 1/lam_1(chan) [smaller window]")
    print("  refinement  rho <= B_rk := ||Z_Lam||^2 + R_G/Lam  -- split the smaller")
    print("     window's spectrum at a THRESHOLD Lam: the modes below it explicitly,")
    print("     the bulk above it uniformly.  Lam_ok is the LEAST threshold at which")
    print("     the bound already closes = how much of the smaller window's spectrum")
    print("     the step has to know explicitly (n_ok/n0 of the modes).")
    print("")
    print("  n   delta   alpha'  bind  mu/2    D_k      margin    lamA      rho    "
          "R_G     J_sup     R_G*J_sup   B_rk   Lam_ok n_ok  loss  rho_max")
    map_rows = []
    for kidx, (n, u, mu) in enumerate(ATOMS):
        for fr in (0.08, 0.22, 0.40, 0.58, 0.76, 0.92):
            r = rec_sample(kidx, fr * delta_max(kidx), M_CAP)
            r["loss"] = r["Bmin"] / r["rho"] if r["rho"] > 0 else float("nan")
            map_rows.append(r)
            ok = ("%6.3f %4d" % (r["lam_ok"], r["J_ok"])) if r["J_ok"] >= 0 \
                else "  --     --"
            print("  %d  %6.4f  %6.4f  %-4s  %6.4f  %7.4f  %+8.4f  %+8.1e  %6.3f  "
                  "%7.2f  %.3e  %9.2f  %6.2f  %s  %5.2f  %6.3f"
                  % (r["n"], r["delta"], r["alpha_p"], r["binder"], r["half_mu"],
                     r["Dk"], r["margin"], r["lamA"], r["rho"], r["R_G"], r["Jsup"],
                     r["prod"], r["B_rk"], ok, r["loss"], 1.0 - r["B_floor"]))

    worst_margin = min(r["margin"] for r in map_rows)
    check("el_target.dk_holds", worst_margin >= -GRID_BAND,
          "min margin mu_k/2 - D_k = %+.2e over %d map samples (T98 grid band %.0e "
          "at the binding end)" % (worst_margin, len(map_rows), GRID_BAND))
    bad_valid = [r for r in map_rows
                 if np.isfinite(r["rho"]) and r["Bmin"] < r["rho"] * (1 - 1e-9)]
    check("el_valid.two_factor", not bad_valid,
          "rho <= R_G * J_sup and rho <= B_rk at all %d samples (no fit enters "
          "either chain)" % len(map_rows))
    bad_equiv = [r for r in map_rows if np.isfinite(r["rho"])
                 and ((r["rho"] <= 1.0) != (r["margin"] >= 0.0))]
    check("el_target.rho_equiv", not bad_equiv,
          "rho <= 1  <=>  D_k <= mu_k/2 at all samples with A_sh > 0")
    bad_j = [r for r in map_rows if r["Jsup"] > (1.0 + 1e-9) / r["lam1"]]
    check("el_valid.jsup_le_floor", not bad_j,
          "J_sup <= 1/lam_1(channel) everywhere; measured gain 1/(lam_1 J_sup) = "
          "%.1f..%.1f" % (min(r["gain"] for r in map_rows),
                          max(r["gain"] for r in map_rows)))

    n_close = sum(1 for r in map_rows if np.isfinite(r["Bmin"]) and r["Bmin"] <= 1.0)
    n_close2 = sum(1 for r in map_rows if np.isfinite(r["prod"]) and r["prod"] <= 1.0)
    n_posA = sum(1 for r in map_rows if r["lamA"] > 0.0)
    info("D2 closure", "best bound <= 1 at %d/%d map samples (two-factor alone %d/%d); "
         "A_sh > 0 at %d/%d; loss min(bound)/rho = %.2f..%.2f"
         % (n_close, len(map_rows), n_close2, len(map_rows), n_posA, len(map_rows),
            min(r["loss"] for r in map_rows), max(r["loss"] for r in map_rows)))
    n_headroom = sum(1 for r in map_rows if r["rho"] <= 1.0 - r["B_floor"])
    info("D2 headroom", "the B_rk family carries an irreducible bulk remainder "
         "R_G/lam_top = %.3f..%.3f, so it can only close where rho <= 1 - R_G/lam_top "
         "= %.3f..%.3f; that happens at %d/%d samples and the bound realises %d of "
         "them -- so the recursive inequality is essentially OPTIMAL in its family "
         "and the obstruction is the remainder, not the low modes"
         % (min(r["B_floor"] for r in map_rows), max(r["B_floor"] for r in map_rows),
            min(1.0 - r["B_floor"] for r in map_rows),
            max(1.0 - r["B_floor"] for r in map_rows), n_headroom, len(map_rows),
            n_close))
    okr = [r for r in map_rows if r["J_ok"] >= 0]
    info("D2 threshold", "where it closes, the step needs only the smaller window's "
         "modes below Lam_ok = %.2f..%.2f -- %d..%d modes, %.1f%%..%.1f%% of its "
         "spectrum: a genuinely FINITE piece of induction data, everything above the "
         "threshold handled by the uniform remainder R_G/Lam"
         % (min(r["lam_ok"] for r in okr), max(r["lam_ok"] for r in okr),
            min(r["J_ok"] for r in okr), max(r["J_ok"] for r in okr),
            100 * min(r["frac_ok"] for r in okr), 100 * max(r["frac_ok"] for r in okr)))
    for kidx, (n, _u, _mu) in enumerate(ATOMS):
        rs = [r for r in map_rows if r["kidx"] == kidx]
        info("closure n=%d" % n, "rho = %.3f..%.3f, best bound = %.2f..%.2f, closes "
             "on %d/%d (deltas %.4f..%.4f)"
             % (min(r["rho"] for r in rs), max(r["rho"] for r in rs),
                min(r["Bmin"] for r in rs), max(r["Bmin"] for r in rs),
                sum(1 for r in rs if r["Bmin"] <= 1.0), len(rs),
                min(r["delta"] for r in rs if r["Bmin"] <= 1.0) if any(
                    r["Bmin"] <= 1.0 for r in rs) else float("nan"),
                max(r["delta"] for r in rs if r["Bmin"] <= 1.0) if any(
                    r["Bmin"] <= 1.0 for r in rs) else float("nan")))

    print("")
    print("  GRID STABILITY -- which factors are continuum objects?  1/lam_1(even) is")
    print("  the object T98 showed to be a discretisation floor.")
    print("  n   delta    lam1_chan (3 grids)             1/lam1_chan  J_sup   R_G  "
          "   rho    lam_top")
    stab = []
    for kidx in (0, 2, 3):
        vals = [rec_sample(kidx, 0.55 * delta_max(kidx), c) for c in CAPS3]
        dl1 = drift([1.0 / v["lam1"] for v in vals])
        djs = drift([v["Jsup"] for v in vals])
        drg = drift([v["R_G"] for v in vals])
        dro = drift([v["rho"] for v in vals])
        ddk = drift([v["Dk"] for v in vals])
        dlt = drift([v["lam_top"] for v in vals])
        stab.append((ATOMS[kidx][0], dl1, djs, drg, dro, ddk, dlt,
                     vals[0]["lam_top"], vals[-1]["lam_top"]))
        print("  %d  %6.4f   %.2e %.2e %.2e     %8.1f%%  %6.1f%%  %5.1f%%  %5.1f%%  "
              "%5.1f%% (%.2f -> %.2f)"
              % (ATOMS[kidx][0], vals[0]["delta"], vals[0]["lam1"], vals[1]["lam1"],
                 vals[2]["lam1"], 100 * dl1, 100 * djs, 100 * drg, 100 * dro,
                 100 * dlt, vals[0]["lam_top"], vals[-1]["lam_top"]))
    jsup_stable = all(s[2] <= 0.10 for s in stab)
    rg_stable = all(s[3] <= 0.10 for s in stab)
    floor_moves = max(s[1] for s in stab) >= 0.40
    info("D2 factors", "grid drift over 3 nested grids: J_sup <= %.1f%%, R_G <= %.1f%%, "
         "rho <= %.1f%%, D_k <= %.1f%% -- while 1/lam_1(chan) drifts up to %.1f%%, "
         "i.e. the FLOOR is a discretisation artefact but the objects the recursive "
         "inequality uses are not"
         % (100 * max(s[2] for s in stab), 100 * max(s[3] for s in stab),
            100 * max(s[4] for s in stab), 100 * max(s[5] for s in stab),
            100 * max(s[1] for s in stab)))

    print("")
    print("  TERMINATION -- alpha' = u_k - alpha < u_k/2 = alpha_k, so every step")
    print("  drops STRICTLY into a lower zone; the chain ends in the classical window.")
    chain_ok = True
    for kidx, (n, u, _mu) in enumerate(ATOMS):
        a = 0.5 * (0.5 * u + alpha_top(kidx))
        chain, done = recursion_chain(a)
        txt = []
        for (aa, kk, _a2) in chain:
            lbl = ("classical" if kk < 0 else
                   "beyond" if kk >= len(ATOMS) else "zone n=%d" % ATOMS[kk][0])
            txt.append("%.4f [%s]" % (aa, lbl))
        ks = [kk for (_a, kk, _b) in chain if 0 <= kk < len(ATOMS)]
        mono = all(ks[i] > ks[i + 1] for i in range(len(ks) - 1))
        steps = len(chain) - 1
        chain_ok = chain_ok and done and mono and chain[-1][1] < 0 and steps <= kidx + 1
        info("chain n=%d" % n, " -> ".join(txt) + "   (%d steps)" % steps)
    dense_ok, dense_max = True, 0
    for kidx, (n, u, _mu) in enumerate(ATOMS):
        for a in np.linspace(0.5 * u + 1e-4, alpha_top(kidx) - 1e-4, 60):
            chain, done = recursion_chain(float(a))
            ks = [kk for (_x, kk, _y) in chain if 0 <= kk < len(ATOMS)]
            dense_max = max(dense_max, len(chain) - 1)
            if not (done and chain[-1][1] < 0
                    and all(ks[i] > ks[i + 1] for i in range(len(ks) - 1))):
                dense_ok = False
    check("el_chain.terminates", chain_ok and dense_ok,
          "240 starting windows: zone index strictly decreasing, all reach the "
          "classical window in <= %d steps (bound: zone index + 1)" % dense_max)

    # -------------------------------------------------------- R3  D3 zone tops
    section("R3  D3 -- THE TOP OF THE ZONE: is the handoff an equality?")
    print("  margin(eps) = mu_k/2 - D_k(alpha_top - eps), two grids.")
    print("")
    eps_list = (0.0020, 0.0040, 0.0080, 0.0160, 0.0320, 0.0640)
    top_fit = {}
    for kidx, (n, u, mu) in enumerate(ATOMS):
        dmx = delta_max(kidx)
        es, ms, ms2 = [], [], []
        for e in eps_list:
            dt = dmx - 2.0 * e
            if dt <= 0.02:
                continue
            es.append(e)
            ms.append(dk_only(kidx, dt, M_CAP)["margin"])
            ms2.append(dk_only(kidx, dt, 1100)["margin"])
        q, r2q = loglog_fit(es, ms)
        # extrapolation to the very top of the zone (eps -> 0) from the three
        # smallest eps, same Richardson machinery, eps in place of the mesh
        pe, m0 = richardson((es[2], es[1], es[0]), (ms[2], ms[1], ms[0]))
        top_fit[n] = (q, r2q, ms[0], m0)
        dr = max(abs(a - b) for a, b in zip(ms, ms2))
        print("  n=%d  alpha_top = %.4f  mu/2 = %.4f" % (n, alpha_top(kidx), 0.5 * mu))
        print("      eps     " + "".join("%10.4f" % e for e in es))
        print("      margin  " + "".join("%10.2e" % v for v in ms))
        print("      m/(mu/2)" + "".join("%10.4f" % (v / (0.5 * mu)) for v in ms))
        info("top n=%d" % n, "margin ~ C eps^q: q = %.2f (R2 = %.3f); at eps = %.4f "
             "margin = %+.2e (T98 %.1e); eps -> 0 extrapolation %+.2e (order %.2f); "
             "grid drift %.1e"
             % (q, r2q, es[0], ms[0], T98_TOP_MARGIN[n], m0, pe, dr))
    qs = [top_fit[n][0] for n in top_fit if np.isfinite(top_fit[n][0])]
    r2s = [top_fit[n][1] for n in top_fit if np.isfinite(top_fit[n][1])]
    m0s = {n: top_fit[n][3] for n in top_fit}
    rel = {n: top_fit[n][3] / (0.5 * ATOMS[i][2]) for i, (n, _u, _m) in enumerate(ATOMS)}
    info("D3 universality", "exponents q = %s (median %.2f), R2 = %.3f..%.3f; "
         "extrapolated top margins %s (relative to mu_k/2: %s)"
         % (", ".join("%.2f" % q for q in qs), float(np.median(qs)), min(r2s), max(r2s),
            ", ".join("n=%d %+.1e" % (n, m0s[n]) for n in sorted(m0s)),
            ", ".join("%.1e" % rel[n] for n in sorted(rel))))
    n_equal = sum(1 for n in rel if abs(rel[n]) <= 1e-2)
    info("D3 handoff", "top margin is within 1%% of mu_k/2 in %d/4 zones -- the "
         "equality D_k(alpha_top) = mu_k/2 is a ZONE-5 phenomenon, not universal; "
         "zones n=2,3,4 keep a finite top margin of %.1e..%.1e"
         % (n_equal, min(m0s[n] for n in (2, 3, 4)), max(m0s[n] for n in (2, 3, 4))))
    seamless = n_equal >= 3

    ds, mv = [], []
    for c in CAPS3:
        r = dk_only(3, delta_max(3) - 2.0 * 0.0020, c)
        ds.append(r["d"])
        mv.append(r["margin"])
    p, lim = richardson(ds, mv)
    info("top n=5 Richardson", "margins %s -> order p = %.2f, limit %+.3e"
         % (", ".join("%+.2e" % v for v in mv), p, lim))

    # ------------------------------------------------------------ R4  synthesis
    section("R4  D4 -- THE INDUCTION SKELETON AND ITS BRICKS")
    print("  Step k, window alpha in zone k, delta = 2 alpha - u_k:")
    print("   (0) the k-th atom is (mu_k/2) diag(-1, 0, +1) in the E_-/E_0/E_+ split")
    print("       => the E_-/E_0 half of positivity is exactly  W <= A_sh, i.e. rho <= 1.")
    print("   (1) E_0 block = Q_{k-1}(alpha'), alpha' = u_k - alpha  [self-similarity,")
    print("       machine-checked to %.0e] -- the induction hypothesis itself." % e_self)
    print("   (2) reflection parity splits the step into two decoupled channels; the")
    print("       near-null EVEN mode of the smaller window is exactly absent from the")
    print("       even channel [selection rule, machine-checked to %.0e]." % e_cross)
    print("   (3) Q_0- x = (Q xtilde)|centre  [extension defect, exact], size set by")
    print("       the three-way arch/pole/old-atom cancellation.")
    print("   (4) rho <= R_G * J_sup  [Cauchy-Schwarz, no fit]: a delta-local wing")
    print("       factor times a smaller-window factor = induction data.")
    print("   (5) alpha' < alpha_k => strictly lower zone => termination at the")
    print("       classical prime-free window alpha < log2/2 in <= k steps.")
    print("")
    bricks = [
        ("atom split / target identity", "MACHINE-CHECKED",
         "S_k = diag(-1/2,0,1/2) to %.0e; lam_min(A_sh - W) = mu/2 - D_k to %.0e"
         % (e_diag, e_t98)),
        ("E_0 self-similarity", "MACHINE-CHECKED", "Q|E_0 = Q_{k-1}(alpha') to %.0e"
         % e_self),
        ("parity selection rule", "MACHINE-CHECKED",
         "cross-parity blocks vanish to %.0e; D_k = max(D_even, D_odd) to %.0e"
         % (e_cross, e_dk)),
        ("extension-defect identity", "MACHINE-CHECKED",
         "Q_0- x = (Q xtilde)|centre to %.0e" % e_ext),
        ("two-factor chain rho <= R_G J_sup", "MACHINE-CHECKED",
         "holds at all %d map samples; loss factor %.2f..%.2f"
         % (len(map_rows), min(r["loss"] for r in map_rows),
            max(r["loss"] for r in map_rows))),
        ("termination", "ARITHMETIC", "<= zone-index steps, 240/240 starting windows"),
        ("floor avoidance (fit-free)", "MEASURED",
         "gain 1/(lam_1 J_sup) = %.0f..%.0f, J_sup grid-stable to %.1f%%"
         % (min(r["gain"] for r in map_rows), max(r["gain"] for r in map_rows),
            100 * max(s[2] for s in stab))),
        ("decay law theta > 1", "MEASURED",
         "theta_x = %.2f..%.2f, %d/%d TAIL zones at R2 >= 0.70"
         % (min(th_all), max(th_all), n_pow, len(tail_zones))),
        ("R_G bound (wing side)", "MEASURED, NOT CERTIFIED",
         "R_G = %.2f..%.2f, grid drift <= %.1f%%"
         % (min(r["R_G"] for r in map_rows), max(r["R_G"] for r in map_rows),
            100 * max(s[3] for s in stab))),
        ("J_sup bound (smaller window)", "MEASURED, NOT CERTIFIED",
         "grid drift <= %.1f%% vs 1/lam_1 drift %.1f%%"
         % (100 * max(s[2] for s in stab), 100 * max(s[1] for s in stab))),
        ("closure of the recursive bound", "OPEN",
         "%d/%d map samples for the plain two-factor form, %d/%d for the threshold "
         "form (needing %d..%d low modes of the smaller window); rho reaches %.3f at "
         "the tops, so any bound with slack > %.1f%% must fail there"
         % (n_close2, len(map_rows), n_close, len(map_rows),
            min(r["J_ok"] for r in okr), max(r["J_ok"] for r in okr),
            max(r["rho"] for r in map_rows),
            100 * (1.0 / max(r["rho"] for r in map_rows) - 1.0))),
        ("bulk remainder R_G/lam_top", "OPEN -- THE GAP",
         "%.3f..%.3f while the true slack 1 - rho falls to %.1e at the zone tops; "
         "lam_top grid drift %.1f%%"
         % (min(r["B_floor"] for r in map_rows), max(r["B_floor"] for r in map_rows),
            1.0 - max(r["rho"] for r in map_rows), 100 * max(s[6] for s in stab))),
        ("A_sh >= 0 certificate", "IMPORTED (T98 R4)",
         "probability measure + multiband Slepian; A_sh > 0 measured at %d/%d here"
         % (n_posA, len(map_rows))),
    ]
    for (nm, st, dt) in bricks:
        info("brick", "%-34s %-22s %s" % (nm, st, dt))

    # ---------------------------------------------------------------- verdict
    section("VERDICT")
    # The law has two forms.  The FIT-FREE form -- the Schur sum stays a factor
    # `gain` away from the floor 1/lam_1, with J_sup a grid-stable object while
    # 1/lam_1 is not -- is the substantive statement and is what the recursive
    # inequality actually uses.  The POWER-LAW form is the shape of that
    # avoidance and is only meaningful in zones that have a near-null tail.
    tail_gain = [r["gain"] for r in map_rows if r["has_tail"]]
    mechanism = (bool(tail_gain) and min(tail_gain) >= 10.0
                 and jsup_stable and floor_moves)
    closure_frac = n_close / float(len(map_rows))
    if not mechanism:
        verdict = "NO-RECURSION"
    elif closure_frac >= 0.5 and chain_ok and dense_ok:
        verdict = "RECURSION-CLOSES"
    else:
        verdict = "DECAY-LAW-FOUND"
    info("selection rule", "exact: the fragile near-null EVEN mode of the smaller "
         "window never enters the binding channel (%d/%d samples bind on the even "
         "channel); parity gap lam1_odd/lam1_even = %.1f..%.1f"
         % (sum(1 for r in map_rows if r["binder"] == "even"), len(map_rows),
            min(r["parity_gap"] for r in map_rows),
            max(r["parity_gap"] for r in map_rows)))
    info("decay law (fit-free)", "floor avoidance gain 1/(lam_1 J_sup) = %.0f..%.0f in "
         "the tail zones, J_sup grid-stable -> %s"
         % (min(tail_gain), max(tail_gain), "YES" if mechanism else "NO"))
    info("decay law (power form)", "theta_x > 1 at R2 >= 0.70 in %d/%d tail zones "
         "(n=4, n=5 clean at theta = 1.1..2.2; n=3 shallower)"
         % (n_pow, len(tail_zones)))
    info("recursive inequality", "valid everywhere (rho <= R_G J_sup and rho <= B_rk); "
         "the two-factor form closes on %.0f%% of the map, the threshold form on "
         "%.0f%%, always the LOWER part of a zone; best loss %.2fx..%.2fx"
         % (100 * n_close2 / float(len(map_rows)), 100 * closure_frac,
            min(r["loss"] for r in map_rows), max(r["loss"] for r in map_rows)))
    info("where it fails", "the upper part of zones n=3,4,5: there 1 - rho falls to "
         "%.1e while the uniform bulk remainder R_G/lam_top is %.2f -- THE named gap"
         % (1.0 - max(r["rho"] for r in map_rows),
            max(r["B_floor"] for r in map_rows)))
    info("termination", "verified, <= zone-index steps to the classical window")
    info("zone tops", "extrapolated top margin %s of mu_k/2 -> handoff %s"
         % (", ".join("n=%d %.1e" % (n, rel[n]) for n in sorted(rel)),
            "an equality in all zones" if seamless
            else "an equality only in zone n=5"))
    info("grid honesty", "J_sup stable (%s), R_G stable (%s), rho stable while "
         "1/lam_1 is a discretisation floor" % ("yes" if jsup_stable else "no",
                                                "yes" if rg_stable else "no"))
    print("")
    print("VERDICT  %s" % verdict)
    print("")
    print("TOTAL  %d checks, %d failures, %.1f s, largest array %d^2"
          % (PASS + FAIL, FAIL, time.time() - T_START, MAXN_SEEN))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
