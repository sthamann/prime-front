"""Discovery probe (2026-07-26), part 95 of the zeta/prime investigation.
Contract CONTINUUM.EXTENSION -- the CONTINUUM attempt at window Weil
positivity on the one-atom band, built on the T92 lesson ("finite blocks
are the wrong instrument") and the T93-corrected band map.

THE T93 CONVENTION (declared once, used everywhere)
  f real, supp f subset (-alpha, alpha), ||f||_2 = 1;  h = f * f~ even,
  h(0) = 1, supp h subset (-2 alpha, 2 alpha), h(u) = int f(x) f(x-u) dx.
      P_pole(f) = hhat(i/2) + hhat(-i/2) = 2 (int f e^{x/2})(int f e^{-x/2})
      A_arch(f) = (1/2pi) int |fhat(t)|^2 k(t) dt,
                  k(t) = Re psi(1/4 + i t/2) - log pi,
                  k(0) = -gamma - 3 log 2 - pi/2 - log pi = -5.3722...,
                  single sign change t0 = 6.28983599...
      atom      = (log 2 / sqrt 2) * 2 h(log 2) = sqrt2 log2 * h(log 2)
  THE TARGET (T''):  for every alpha in (alpha_c, alpha*], every real f with
      supp f subset (-alpha, alpha), ||f||_2 = 1:
          Q(f) = P_pole(f) + A_arch(f) - sqrt2 log2 * h_f(log 2)  >=  0.
  Map:  alpha_c = log2/2 = 0.3465736 (classical edge, h-support = log 2:
        unconditional Weil positivity there -- Yoshida 1992, Bombieri 2000,
        Connes-Consani 2021);  alpha_free = 0.3723..0.3763 (prime-free form
        P_pole + A_arch first has lambda_min = 0);  ONE-ATOM BAND
        (alpha_c, alpha*], alpha* = 0.46265, only u = log 2 inside the
        h-support (second atom would need alpha > log3/2 = 0.5493).

WHY A CONTINUUM INSTRUMENT (T92's lesson)
  Mode-truncated blocks give a Rayleigh-Ritz UPPER bound for lambda_min that
  moves with the block size; at 24 modes the numbers are not resolved.  The
  instrument here is a piecewise-constant (PWC) Nystrom/Galerkin space on a
  uniform cell grid of the window, in which ALL THREE forms are evaluated
  EXACTLY (no mode truncation of the kernels):
      * h of a PWC f is piecewise LINEAR in u with nodes at multiples of the
        cell width d, so h(log 2) is an exact linear interpolation and the
        atom form is an exact Toeplitz matrix;
      * A_arch is assembled from the EXACT u-space identity (below), the
        u-integral being reduced to M one-cell integrals of an analytic
        integrand, each done with a 24-node Gauss-Legendre rule;
      * P_pole is a rank-2 matrix from exact cell integrals of e^{+-x/2}.
  Cap discipline: the "modes <= 24" cap is respected -- no spectral basis is
  used at all, and the only 24 in the pipeline is the GL rule per cell; the
  Nystrom node count M is bounded by the array cap (max array here 801^2).

THE EXACT u-SPACE ARCHIMEDEAN IDENTITY (from psi's integral representation
  psi(z) = -gamma + int_0^inf (e^{-s} - e^{-z s})/(1 - e^{-s}) ds, s = 2u)
      A_arch = C_b h(0) + int_0^b w(u) [e^{-3u/2} h(0) - h(u)] du,
      b = 2 alpha,  w(u) = 2 e^{-u/2} / (1 - e^{-2u}),
      C_b = -gamma - log pi - log(1 - e^{-2b}).
  Both pieces of the u = 0 cell diverge; their combination is analytic and is
  integrated as ONE integral -- this is where a naive assembly would fail, so
  it is validated three ways in R2.

THE THREE STRATEGIES
  C1  ATOM AS A STRUCTURED PERTURBATION.  h_f(log 2) = <f, S_{log2} f> with
      the window-truncated shift.  Support geometry: the atom form only sees
      I = (-alpha, alpha - log2) and J = (-alpha + log2, alpha), both of
      length delta' = 2 alpha - log 2 (the band depth), and I, J are
      DISJOINT exactly when alpha <= log 2 -- true on the whole band
      (alpha* = 0.4627 < 0.6931).  Hence
          |h_f(log2)| <= ||f 1_I|| ||f 1_J|| <= 1/2,
      with equality iff f = g + g(.- log2) for g in L^2(I) with ||g||^2=1/2:
      TWO IDENTICAL BUMPS at distance log 2.  Consequences derived and
      verified here: the truncated shift operator has ||S|| = 1/2 EXACTLY on
      the band with an eigenspace of dimension |I| (infinite-dimensional in
      the continuum, dim = M - n2 on an aligned grid), the saturating f have
      |fhat|^2 = 2(1 + cos(t log 2)) |ghat|^2, and T'' restricted to that
      eigenspace is the sharp necessary condition
          lambda_min( (P_pole + A_arch) | E_{1/2} )  >=  sqrt2 log2 / 2
                                                     =  0.4901291...
  C2  THE COUPLED EXTREMAL PROBLEM.  Above alpha_free the prime-free form is
      INDEFINITE, so the ratio formulation atom/(pole+arch) is ill-posed
      there; the well-posed object is the ADMISSIBLE COUPLING WINDOW
          mu_-(alpha) <= mu <= mu_+(alpha),  { mu : lambda_min(P + A - mu S)
                                               >= 0 },
      an interval because lambda_min is concave in mu.  T'' on the band is
      exactly "mu_phys = sqrt2 log2 = 0.9802581 lies inside", and the margin
      curve is the pair (mu_phys - mu_-, mu_+ - mu_phys) together with
      lambda_min(Q) itself.  Extremiser profiles are read off the Galerkin
      eigenvectors (two-bump content, atom value, I/J mass, sign changes).
  C3  FRAMING THE NYSTROM RESULT.  What is rigorous, what is not:
      (i) exact-on-PWC forms + nested grids => lambda_min^{(M)} is a
          monotone, quadrature-certified UPPER bound for the continuum
          lambda_min (a negative value would be a DISPROOF of T''; positive
          values prove nothing);
      (ii) the GL quadrature error is bounded a posteriori by a Schur bound
          on the coefficient difference between 24- and 48-node rules, giving
          an explicit certified interval for the Galerkin value;
      (iii) the frequency reduction "drop the tail |t| >= T_+ where the
          Weil-atom kernel kappa(t) = k(t) - mu_phys cos(t log2) is
          nonnegative" is rigorous and is measured for wastefulness;
      (iv) the projection-defect route to a LOWER bound (Young split of the
          log-divergent Dirichlet part D, complement controlled by the
          low-frequency bound |rhat(t)| <= ||r|| |t| d sqrt(2 alpha/12) for
          cell-mean-zero r) is quantified here and REFUTED: D's Fourier
          weight grows like log T, so the required cut is exponential in the
          bounded-part norm and the required cell count exceeds the array cap
          by orders of magnitude.  The gap is named, not papered over.

PREREGISTERED VERDICTS
  T-CONTINUUM-CERTIFIED : Nystrom + framing close the band quadrature-
                          rigorously (a two-sided enclosure with a positive
                          lower bound for every alpha in the band).
  T-CONTINUUM-NUMERIC   : the margin curve stands numerically (monotone,
                          resolution-stable, coupling window contains
                          mu_phys) but the lower-bound side of the framing is
                          incomplete -- gaps quantified.
  T-STRUCTURE           : only the C1 chain yields statements.
  T-BLOCKED             : the chain breaks; where.
  Element gates:
    el_kernel   : vectorised Re psi(1/4+it/2) agrees with mpmath <= 1e-12 and
                  t0 is re-derived to <= 1e-8 of the T93 value.
    el_identity : the u-space archimedean identity equals the t-space
                  digamma integral <= 1e-8 on an exactly integrable test
                  function (cos-bell), Plancherel <= 1e-9.
    el_assembly : the discrete kappa assembly reproduces the exact u-space
                  value on the flat window function <= 1e-10 (its h is
                  piecewise linear, so the Galerkin value must be exact).
    el_classical: lambda_min(P+A) > 0 for alpha <= alpha_c (consistency with
                  the unconditional classical zone) and the prime-free
                  crossing lands in [0.355, 0.385] (T93 map).
    el_c1       : ||S|| = 1/2 to 1e-12 with eigenvalue multiplicity M - n2,
                  the two-bump Fourier signature holds to 1e-10, and the
                  restricted necessary condition is decided numerically.
    el_band     : lambda_min(Q) >= -1e-9 at every swept alpha at the finest
                  resolution (a violation would be a rigorous disproof of
                  T'' and hence, via RH => T'', a red flag to be debugged
                  rather than published).
    el_mu       : mu_phys lies strictly inside [mu_-, mu_+] at every swept
                  alpha.
    el_frame    : monotone decrease of lambda_min^{(M)} under nesting, and
                  the quadrature interval width < 1e-6.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit,
    no verification/ module, no next.txt edit, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, network imports and write-mode file access in this source.
  * RH => (T''); (T'') does NOT imply RH.  Nothing here is evidence for or
    against RH: positivity beyond the classical zone is what RH PREDICTS,
    measuring it is bookkeeping.  No "proved" language without a certificate;
    every rigour level is typed in the ledger of R6.
  * Classical anchors cited, not re-derived: Weil 1952 (explicit formula),
    Yoshida 1992 / Bombieri 2000 / Connes-Consani 2021 (unconditional
    positivity up to h-support width log 2), the digamma archimedean kernel,
    Rayleigh-Ritz, Nystrom/collocation for Fredholm equations, Euler-Lagrange
    for the constrained extremal problem, Schur test, Landau-Widom counting.

OUTCOME OF THIS RUN
  C1 is exact and closes its own sub-statement: the truncated shift has norm
  exactly 1/2 on the band, on a two-bump eigenspace of dimension |I| = delta',
  and the restricted necessary condition holds with a margin falling from
  +3.49 just above alpha_c to +0.128 at the band top -- the atom-extremal
  directions are NOT the binding ones.  C2: the prime-free form goes
  indefinite at alpha_free = 0.371654 (continuum value; the 24-mode 0.3763 of
  T92 was an upper bound), and from there on the minimiser has h(log2) < 0, so
  the atom RESCUES rather than threatens; the admissible coupling window
  contains mu_phys across the whole band, narrowing to about [0.9700, 0.9815]
  at alpha*.  The binding extremiser is even, single-humped, low-frequency,
  with a two-bump content of only 0.046.  lambda_min(Q) is positive at every
  swept alpha, falling from 1.3e-3 to 2.1e-5 (M = 800 upper bounds); two
  independent nested ladders (M = 100..1600 and M = 300..2400) extrapolate the
  band-top value to +7.8e-6, so alpha* = 0.46265 behaves like the continuum
  positivity edge.  C3: the upper side and the quadrature are certified
  (Schur bound 4e-15), the frequency reduction is rigorous but structurally
  too lossy, and the projection-defect route to a lower bound is refuted
  quantitatively (it would need M ~ 7e5 cells).  The lower bound stays OPEN.
  => T-CONTINUUM-NUMERIC.
"""
import ast
import math
import time

import mpmath
import numpy as np

PASS = 0
FAIL = 0
T_START = time.time()
mpmath.mp.dps = 30

EULER = float(mpmath.euler)
LOG_PI = math.log(math.pi)
LOG2 = math.log(2.0)
LOG3 = math.log(3.0)

ALPHA_C = LOG2 / 2.0                    # classical edge (h-support = log 2)
ALPHA_STAR = 0.46265                    # T91/T93 one-atom band ceiling
ALPHA_TWO_ATOM = LOG3 / 2.0             # second atom would enter here
MU_PHYS = math.sqrt(2.0) * LOG2         # 0.9802581... physical atom coupling
T0_T93 = 6.28983599                     # T92/T93 kernel sign change
N_GL = 24                               # GL nodes per cell -- the 24 cap
ARRAY_CAP = 10 ** 7


def check(name, ok):
    global PASS, FAIL
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


def info(msg):
    print(f"        {msg}", flush=True)


def head(msg):
    print(f"\n{msg}", flush=True)


# ============================================================ R0  firewall
def firewall():
    head("R0    AST firewall (zero-free, sandbox-only, read-only)")
    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)
    allowed = {"ast", "math", "time", "mpmath", "numpy"}
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module:
            mods.add(node.module.split(".")[0])
    check(f"imports within the sandbox set (found {sorted(mods)})", mods <= allowed)

    writes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "open":
            mode = "r"
            if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                mode = node.args[1].value
            for kw in node.keywords:
                if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                    mode = kw.value.value
            if "r" not in mode or "+" in mode:
                writes.append(mode)
    check("no write-mode file access in this source", not writes)

    banned = ["zeta" + "zero", "lmf" + "db", "riemann_" + "zero", "zeros_" + "table",
              "14.1347", "21.0220", "urllib", "requests", "socket", "http"]
    hits = [tok for tok in banned if src.count(tok) > 1]
    check(f"no zero-table / network tokens (scanned {len(banned)})", not hits)
    info("Only Riemann-zero-free objects: digamma kernel, prime atom log 2, "
         "window geometry.  No zero list is read, generated or approximated.")
    return True


# ================================================= R1  kernel + band map
def re_psi_quarter(t):
    """Re psi(1/4 + i t/2), vectorised: 24 recurrence steps + Bernoulli tail."""
    z = 0.25 + 0.5j * np.asarray(t, dtype=float)
    acc = np.zeros_like(z)
    w = z.copy()
    for _ in range(N_GL):
        acc = acc + 1.0 / w
        w = w + 1.0
    iw = 1.0 / w
    iw2 = iw * iw
    psi = (np.log(w) - 0.5 * iw
           - iw2 * (1.0 / 12.0 - iw2 * (1.0 / 120.0
                                        - iw2 * (1.0 / 252.0 - iw2 / 240.0))))
    return np.real(psi - acc)


def k_arch(t):
    return re_psi_quarter(t) - LOG_PI


def kappa_weil(t):
    """The Weil-atom kernel of the target form: k(t) - mu_phys cos(t log2)."""
    return k_arch(t) - MU_PHYS * np.cos(np.asarray(t, dtype=float) * LOG2)


def bisect_root(fun, lo, hi, iters=80):
    flo = fun(lo)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if float(fun(mid)) * float(flo) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def r1_kernel_and_map():
    head("R1    archimedean kernel, the corrected band map, kappa geometry")
    ts = [0.0, 0.37, 1.0, 3.5, T0_T93, 14.0, 100.0, 1234.5]
    err = 0.0
    for t in ts:
        ref = float(mpmath.re(mpmath.digamma(mpmath.mpf(0.25) + 0.5j * t)) - mpmath.log(mpmath.pi))
        err = max(err, abs(float(k_arch(t)) - ref))
    check(f"vectorised k(t) matches mpmath digamma (max err {err:.2e})", err <= 1e-12)

    k0_closed = -EULER - 3.0 * LOG2 - math.pi / 2.0 - LOG_PI
    check(f"k(0) = -gamma-3log2-pi/2-log pi = {k0_closed:.7f} (err "
          f"{abs(float(k_arch(0.0)) - k0_closed):.2e})",
          abs(float(k_arch(0.0)) - k0_closed) <= 1e-13)

    t0 = bisect_root(lambda t: float(k_arch(t)), 5.0, 8.0)
    t0_mp = float(mpmath.findroot(
        lambda t: mpmath.re(mpmath.digamma(mpmath.mpf(0.25) + 0.5j * t)) - mpmath.log(mpmath.pi),
        mpmath.mpf("6.29")))
    check(f"t0 = {t0:.8f} (mpmath {t0_mp:.8f}; T93 {T0_T93:.8f})",
          abs(t0 - T0_T93) <= 1e-8 and abs(t0 - t0_mp) <= 1e-10)
    info(f"t0 / 2pi = {t0 / (2.0 * math.pi):.6f}; the kernel is the smooth zero "
         "density (1/2pi) log(t/2pi) + O(t^-2), hence the sign change near 2pi.")

    info(f"alpha_c = log2/2 = {ALPHA_C:.7f}   alpha* = {ALPHA_STAR:.5f}   "
         f"log3/2 = {ALPHA_TWO_ATOM:.7f}")
    check("one-atom band well posed: alpha_c < alpha* < log3/2",
          ALPHA_C < ALPHA_STAR < ALPHA_TWO_ATOM)
    check(f"band depth delta'(alpha*) = 2alpha*-log2 = {2 * ALPHA_STAR - LOG2:.6f} > 0",
          2 * ALPHA_STAR - LOG2 > 0)
    check(f"disjointness condition alpha* < log2 holds "
          f"(margin {LOG2 - ALPHA_STAR:.6f})", ALPHA_STAR < LOG2)

    # kappa(t) >= 0 for |t| >= T_plus: rigorous because cos <= 1.
    t_plus = bisect_root(lambda t: float(k_arch(t)) - MU_PHYS, 8.0, 40.0)
    grid = np.linspace(t_plus, 4000.0, 400001)
    kmin_tail = float(np.min(kappa_weil(grid)))
    check(f"T_+ = {t_plus:.6f}: k(T_+) = mu_phys, so kappa >= 0 on |t| >= T_+ "
          f"(scan min {kmin_tail:.3e})", kmin_tail >= -1e-12)
    info(f"kappa(0) = k(0) - mu_phys = {float(kappa_weil(0.0)):.6f}; the negative "
         f"mass of kappa lives entirely in |t| < T_+ = {t_plus:.4f}, i.e. in a "
         f"window-band-limited space of Landau-Widom dimension "
         f"~ T_+ * 2alpha*/pi = {t_plus * 2 * ALPHA_STAR / math.pi:.2f}.")
    return t0, t_plus


# ============================================== R2  the Nystrom assembly
def arch_coeffs(alpha, M, n_gl=N_GL):
    """kappa_m with A_arch(f) = sum_m kappa_m Ghat_m, Ghat_m = sum_j c_j c_{j+m}."""
    b = 2.0 * alpha
    d = b / M
    x, wq = np.polynomial.legendre.leggauss(n_gl)
    s = 0.5 * (x + 1.0)
    wq = 0.5 * wq

    # cell m = 0: the two divergent halves are combined into one analytic integral
    u0 = s * d
    w0 = 2.0 * np.exp(-0.5 * u0) / (-np.expm1(-2.0 * u0))
    p0 = d * float(np.sum(wq * w0 * (np.expm1(-1.5 * u0) + s)))
    w2_0 = d * float(np.sum(wq * w0 * s))

    m = np.arange(1, M)
    U = (m[:, None] + s[None, :]) * d
    W = 2.0 * np.exp(-0.5 * U) / (-np.expm1(-2.0 * U))
    w0_m = d * np.sum(wq[None, :] * W * np.exp(-1.5 * U), axis=1)
    w1_m = d * np.sum(wq[None, :] * W * (1.0 - s)[None, :], axis=1)
    w2_m = d * np.sum(wq[None, :] * W * s[None, :], axis=1)

    cb = -EULER - LOG_PI - math.log(-math.expm1(-2.0 * b))
    kap = np.zeros(M)
    kap[0] = cb + p0 + float(np.sum(w0_m))
    w2full = np.concatenate(([w2_0], w2_m))
    kap[1:] = -w1_m - w2full[:M - 1]
    return kap


def atom_coeffs(alpha, M):
    """Toeplitz first row of the atom form h_f(log 2) (exact for PWC f)."""
    d = 2.0 * alpha / M
    z = LOG2 / d
    zr = round(z)
    if abs(z - zr) < 1e-9:
        m2, s2 = int(zr), 0.0
    else:
        m2 = int(math.floor(z))
        s2 = z - m2
    r = np.zeros(M)
    if m2 < M:
        r[m2] += 0.5 * (1.0 - s2)
    if m2 + 1 < M:
        r[m2 + 1] += 0.5 * s2
    return r, m2, s2


def pole_vectors(alpha, M):
    d = 2.0 * alpha / M
    xe = -alpha + d * np.arange(M)
    rt = math.sqrt(d)
    p = 2.0 * (np.exp(0.5 * (xe + d)) - np.exp(0.5 * xe)) / rt
    q = 2.0 * (np.exp(-0.5 * xe) - np.exp(-0.5 * (xe + d))) / rt
    return p, q


def toeplitz_from_row(r):
    M = r.shape[0]
    idx = np.abs(np.subtract.outer(np.arange(M), np.arange(M)))
    return r[idx]


def window_matrices(alpha, M, n_gl=N_GL):
    if M * M > ARRAY_CAP:
        raise ValueError("array cap")
    kap = arch_coeffs(alpha, M, n_gl)
    ra = kap.copy()
    ra[1:] *= 0.5
    rt, m2, s2 = atom_coeffs(alpha, M)
    p, q = pole_vectors(alpha, M)
    A = toeplitz_from_row(ra)
    S = toeplitz_from_row(rt)
    P = np.outer(p, q)
    P = P + P.T
    return P, A, S, (p, q, m2, s2, kap)


def lam_min(P, A, S, mu):
    return float(np.linalg.eigvalsh(P + A - mu * S)[0])


def flat_form_values(alpha, M):
    """A_arch of the flat window function from the discrete kappa assembly."""
    kap = arch_coeffs(alpha, M)
    m = np.arange(M)
    ghat = (M - m) / M
    return float(kap[0] * ghat[0] + np.dot(kap[1:], ghat[1:]))


def arch_u_exact(alpha, h_func):
    """A_arch from the exact u-space identity with mpmath quadrature."""
    b = mpmath.mpf(2.0) * mpmath.mpf(alpha)
    cb = -mpmath.euler - mpmath.log(mpmath.pi) - mpmath.log(1 - mpmath.e ** (-2 * b))

    def integrand(u):
        w = 2 * mpmath.e ** (-u / 2) / (1 - mpmath.e ** (-2 * u))
        return w * (mpmath.e ** (-1.5 * u) - h_func(u))

    return float(cb + mpmath.quad(integrand, [0, b]))


def cos_bell(alpha):
    """f = cos(pi x / 2alpha)/sqrt(alpha): exact h, exact fhat, ||f||=1."""
    om = math.pi / (2.0 * alpha)
    c = 1.0 / math.sqrt(alpha)

    def h(u):
        u = mpmath.mpf(u)
        a = mpmath.mpf(alpha)
        return ((2 * a - u) * mpmath.cos(om * u) + (2 * a / mpmath.pi) * mpmath.sin(om * u)) / (2 * a)

    def fhat(t):
        t = np.asarray(t, dtype=float)
        z = (t - om) * alpha
        sinc = np.where(np.abs(z) < 1e-12, 1.0 - z * z / 6.0, np.sin(z) / np.where(z == 0.0, 1.0, z))
        return 2.0 * c * om * alpha * sinc / (om + t)

    def values(xs):
        return c * np.cos(om * np.asarray(xs, dtype=float))

    return h, fhat, values, om, c


def gl_panels(edges, per_panel=N_GL):
    x, w = np.polynomial.legendre.leggauss(per_panel)
    nodes, wts = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        nodes.append(mid + half * x)
        wts.append(half * w)
    return np.concatenate(nodes), np.concatenate(wts)


def r2_assembly():
    head("R2    Nystrom assembly: three-route validation and calibration")
    alpha = 0.42
    hb, fhat, fvals, om, c = cos_bell(alpha)

    # panel widths follow the cos(t alpha) oscillation (period pi/alpha) so that
    # the 1/t^4 tail of |fhat|^2 is resolved, not merely small
    edges = ([0.0] + list(np.arange(0.25, om, 0.25)) + [om]
             + list(om + np.arange(0.25, 40.0, 0.25))
             + list(np.arange(om + 40.0, 200.0, 0.5))
             + list(np.arange(200.0, 2000.0, 2.0))
             + list(np.arange(2000.0, 20000.0, 20.0)) + [20000.0])
    tn, tw = gl_panels(np.array(sorted(set(np.round(edges, 12)))))
    fh2 = fhat(tn) ** 2
    planch = float(2.0 * np.sum(tw * fh2) / (2.0 * math.pi))
    check(f"Plancherel of the cos-bell test function = {planch:.12f}", abs(planch - 1.0) <= 1e-9)
    a_t = float(2.0 * np.sum(tw * fh2 * k_arch(tn)) / (2.0 * math.pi))
    a_u = arch_u_exact(alpha, hb)
    check(f"el_identity: u-space A_arch {a_u:.12f} vs t-space {a_t:.12f} "
          f"(diff {abs(a_u - a_t):.2e})", abs(a_u - a_t) <= 1e-8)

    a_flat_u = arch_u_exact(alpha, lambda u: 1 - u / (2 * mpmath.mpf(alpha)))
    worst = 0.0
    for M in (37, 101, 400):
        worst = max(worst, abs(flat_form_values(alpha, M) - a_flat_u))
    check(f"el_assembly: discrete kappa form on the flat window reproduces the "
          f"exact u-space value {a_flat_u:.12f} (max dev {worst:.2e})", worst <= 1e-10)

    prev = None
    rates = []
    for M in (50, 100, 200, 400, 800):
        d = 2.0 * alpha / M
        xc = -alpha + d * (np.arange(M) + 0.5)
        cv = fvals(xc) * math.sqrt(d)
        cv = cv / math.sqrt(float(np.dot(cv, cv)))
        kap = arch_coeffs(alpha, M)
        gh = np.array([float(np.dot(cv[:M - m], cv[m:])) for m in range(M)])
        val = float(kap[0] * gh[0] + np.dot(kap[1:], gh[1:]))
        dev = abs(val - a_u)
        if prev is not None:
            rates.append(prev / max(dev, 1e-18))
        info(f"M = {M:4d}  A_arch(PWC sample) = {val:.9f}  |dev| = {dev:.3e}"
             + (f"  ratio {rates[-1]:.2f}" if rates else ""))
        prev = dev
    check(f"PWC sampling error decreases monotonically (ratios "
          f"{['%.2f' % r for r in rates]})", all(r > 1.5 for r in rates))

    p, q = pole_vectors(alpha, 400)
    d = 2.0 * alpha / 400
    xc = -alpha + d * (np.arange(400) + 0.5)
    cv = fvals(xc) * math.sqrt(d)
    cv = cv / math.sqrt(float(np.dot(cv, cv)))
    # exact int f e^{x/2} for the cos-bell (fhat continued to t = -i/2)
    aa = float(2.0 * c * om * math.cosh(alpha / 2.0) / (om * om + 0.25))
    check(f"pole vectors converge to the exact functional: discrete <p,c> = "
          f"{float(np.dot(p, cv)):.9f} vs exact {aa:.9f}",
          abs(float(np.dot(p, cv)) - aa) <= 2e-5)

    info("Classical zone consistency (Yoshida 1992 / Bombieri 2000 / CC 2021: "
         "unconditional positivity for h-support <= log 2):")
    ok_cl = True
    for al in (0.28, 0.32, ALPHA_C):
        P, A, S, _ = window_matrices(al, 400)
        lm = lam_min(P, A, S, 0.0)
        info(f"  alpha = {al:.7f}  lambda_min(P_pole + A_arch) = {lm:+.6f}")
        ok_cl = ok_cl and lm > 0.0
    a_free = bisect_root(lambda al: lam_min(*window_matrices(al, 400)[:3], 0.0), 0.34, 0.42, iters=34)
    check(f"el_classical: prime-free form positive up to alpha_c and the crossing "
          f"alpha_free = {a_free:.6f} in [0.355,0.385]",
          ok_cl and 0.355 <= a_free <= 0.385)
    info(f"T93 map quoted alpha_free = 0.3723..0.3763 (24-mode value 0.3763 is a "
         f"Rayleigh-Ritz upper bound); continuum Nystrom value here {a_free:.6f}.")
    return a_free


# ================================================== R3  C1 structure chain
def aligned_grid(n2, M):
    d = LOG2 / n2
    return M * d / 2.0, d


def r3_c1_structure(n2=300):
    head("R3    C1: the atom as a structured perturbation (exact chain)")
    M_top = int(math.floor(2.0 * ALPHA_STAR / (LOG2 / n2)))
    alpha_top, d = aligned_grid(n2, M_top)
    info(f"aligned grid: d = log2/{n2} = {d:.8f}; M = n2 corresponds exactly to "
         f"alpha_c, M = {M_top} to alpha = {alpha_top:.6f} (band top, "
         f"alpha* = {ALPHA_STAR:.5f})")

    P, A, S, aux = window_matrices(alpha_top, M_top)
    m2 = aux[2]
    ev = np.linalg.eigvalsh(S)
    n_i = M_top - n2
    mult_hi = int(np.sum(np.abs(ev - 0.5) < 1e-10))
    mult_lo = int(np.sum(np.abs(ev + 0.5) < 1e-10))
    check(f"||S_atom|| = 1/2 EXACTLY on the band (max |ev| = {np.max(np.abs(ev)):.15f})",
          abs(np.max(np.abs(ev)) - 0.5) <= 1e-12)
    check(f"el_c1 multiplicity: dim E_(+1/2) = {mult_hi} = M - n2 = {n_i} "
          f"(and dim E_(-1/2) = {mult_lo})", mult_hi == n_i and mult_lo == n_i)
    info(f"I = (-alpha, alpha-log2) = ({-alpha_top:.6f}, {alpha_top - LOG2:.6f}), "
         f"J = I + log2 = ({-alpha_top + LOG2:.6f}, {alpha_top:.6f}); "
         f"|I| = |J| = delta' = {2 * alpha_top - LOG2:.6f}")
    check("I and J are disjoint on the band (alpha - log2 <= -alpha + log2)",
          alpha_top - LOG2 <= -alpha_top + LOG2)
    info("Cauchy-Schwarz chain: |h_f(log2)| <= ||f 1_I|| ||f 1_J|| and, I,J being "
         "disjoint, ||f 1_I||^2 + ||f 1_J||^2 <= 1, hence |h_f(log2)| <= 1/2 with "
         "equality iff f = g + g(.-log2), ||g||^2 = 1/2 -- two identical bumps at "
         "distance log 2.  The numeric spectrum above IS that statement: the shift "
         f"form saturates at 1/2 on a {n_i}-dimensional space (dimension |I| in the "
         "continuum).")

    # two-bump Fourier signature |fhat|^2 = 2(1+cos(t log2)) |ghat|^2
    j0 = n_i // 3
    cv = np.zeros(M_top)
    cv[j0] = cv[j0 + m2] = 1.0 / math.sqrt(2.0)
    gv = np.zeros(M_top)
    gv[j0] = 1.0
    dd = 2.0 * alpha_top / M_top
    xe = -alpha_top + dd * np.arange(M_top)

    def pwc_hat(coef, t):
        t = np.atleast_1d(np.asarray(t, dtype=float))
        out = np.zeros_like(t, dtype=complex)
        nz = np.nonzero(coef)[0]
        for j in nz:
            with np.errstate(divide="ignore", invalid="ignore"):
                term = np.where(np.abs(t) < 1e-14, dd,
                                (np.exp(-1j * t * xe[j]) - np.exp(-1j * t * (xe[j] + dd)))
                                / np.where(t == 0.0, 1.0, 1j * t))
            out = out + coef[j] * term / math.sqrt(dd)
        return out

    tt = np.array([0.3, 1.7, 4.5324, 6.28983599, 11.0])
    lhs = np.abs(pwc_hat(cv, tt)) ** 2
    rhs = 2.0 * (1.0 + np.cos(tt * LOG2)) * np.abs(pwc_hat(gv / math.sqrt(2.0), tt)) ** 2
    dev = float(np.max(np.abs(lhs - rhs)))
    check(f"el_c1 two-bump signature |fhat|^2 = 2(1+cos(t log2))|ghat|^2 "
          f"(max dev {dev:.2e})", dev <= 1e-10)
    info(f"zeros of the comb at t = (2k+1)pi/log2: first at {math.pi / LOG2:.6f} "
         f"(inside the negative region |t| < t0 = {T0_T93:.4f}), next at "
         f"{3 * math.pi / LOG2:.6f} (outside): a saturating f DOUBLES the weight "
         "at t = 0 where k is most negative, so the atom-extremal directions pay "
         "the largest archimedean penalty -- and they must be carried by P_pole.")

    info("Restricted necessary condition on E_(+1/2):  Q >= 0 there is exactly "
         f"lambda_min((P+A)|E) >= mu_phys/2 = {MU_PHYS / 2:.7f}")
    rows = []
    for frac in (0.02, 0.2, 0.4, 0.6, 0.8, 1.0):
        M = n2 + max(1, int(round(frac * (M_top - n2))))
        al, _ = aligned_grid(n2, M)
        P, A, S, aux = window_matrices(al, M)
        n_ii = M - n2
        V = np.zeros((M, n_ii))
        for j in range(n_ii):
            V[j, j] = V[j + n2, j] = 1.0 / math.sqrt(2.0)
        KR = V.T @ (P + A) @ V
        lmr = float(np.linalg.eigvalsh(KR)[0])
        atom_chk = float(V[:, 0] @ S @ V[:, 0])
        rows.append((al, lmr, lmr - MU_PHYS / 2, atom_chk))
        info(f"  alpha = {al:.6f}  delta' = {2 * al - LOG2:.6f}  "
             f"lambda_min((P+A)|E) = {lmr:+.6f}  margin = {lmr - MU_PHYS / 2:+.6f}  "
             f"(atom value on E: {atom_chk:.12f})")
    ok_restrict = all(r[2] > 0.0 for r in rows) and all(abs(r[3] - 0.5) < 1e-12 for r in rows)
    check("el_c1 restricted condition holds with positive margin on the whole band",
          ok_restrict)
    return rows, alpha_top, n_i


# ================================================= R4  C2 margin curve
def mu_window(alpha, M, lo=0.0, hi=8.0, iters=26):
    P, A, S, _ = window_matrices(alpha, M)
    if lam_min(P, A, S, MU_PHYS) < 0.0:
        return None, None, lam_min(P, A, S, MU_PHYS)
    a, b = lo, MU_PHYS
    if lam_min(P, A, S, a) >= 0.0:
        mu_lo = None
    else:
        for _ in range(iters):
            m = 0.5 * (a + b)
            if lam_min(P, A, S, m) >= 0.0:
                b = m
            else:
                a = m
        mu_lo = 0.5 * (a + b)
    a, b = MU_PHYS, hi
    if lam_min(P, A, S, b) >= 0.0:
        mu_hi = None
    else:
        for _ in range(iters):
            m = 0.5 * (a + b)
            if lam_min(P, A, S, m) >= 0.0:
                a = m
            else:
                b = m
        mu_hi = 0.5 * (a + b)
    return mu_lo, mu_hi, lam_min(P, A, S, MU_PHYS)


def r4_margin_curve(a_free, M_sweep=800, M_mu=400):
    head("R4    C2: the coupled extremal problem -- margin curve over the band")
    info("alpha        delta'     lam_min(P+A)   atom@argmin   lam_min(Q)     "
         "atom@argmin(Q)")
    fr = [0.002, 0.05, 0.12, 0.22, 0.34, 0.46, 0.58, 0.70, 0.82, 0.92, 0.98, 1.0]
    sweep = []
    for f_ in fr:
        al = ALPHA_C + f_ * (ALPHA_STAR - ALPHA_C)
        P, A, S, _ = window_matrices(al, M_sweep)
        w0, v0 = np.linalg.eigh(P + A)
        atom0 = float(v0[:, 0] @ S @ v0[:, 0])
        wq, vq = np.linalg.eigh(P + A - MU_PHYS * S)
        atomq = float(vq[:, 0] @ S @ vq[:, 0])
        sweep.append((al, w0[0], atom0, wq[0], atomq, vq[:, 0]))
        info(f"{al:.7f}  {2 * al - LOG2:.6f}  {w0[0]:+.7f}     {atom0:+.6f}     "
             f"{wq[0]:+.7f}     {atomq:+.6f}")
    ok_band = all(s[3] >= -1e-9 for s in sweep)
    check(f"el_band: lambda_min(Q) >= -1e-9 at every swept alpha "
          f"(min {min(s[3] for s in sweep):+.3e})", ok_band)
    rescued = [s for s in sweep if s[1] < 0.0]
    if rescued:
        info(f"ATOM RESCUE: for alpha > alpha_free = {a_free:.6f} the prime-free form "
             f"is indefinite ({len(rescued)} swept points), and at its minimiser the "
             f"atom value h(log2) is NEGATIVE (max over those points: "
             f"{max(s[2] for s in rescued):+.6f}) -- subtracting mu_phys h(log2) ADDS "
             "positivity exactly in the offending direction.")
        check("atom rescue: every indefinite prime-free minimiser has h(log2) < 0",
              all(s[2] < 0.0 for s in rescued))

    info("Admissible coupling window { mu : lambda_min(P+A-mu S) >= 0 } "
         f"(concave in mu, so an interval; physical mu_phys = {MU_PHYS:.7f}; "
         f"bisected in the M = {M_mu} Galerkin space, hence itself an OUTER "
         "estimate that shrinks with resolution):")
    ok_mu = True
    mu_rows = []
    for f_ in (0.05, 0.22, 0.46, 0.70, 0.92, 1.0):
        al = ALPHA_C + f_ * (ALPHA_STAR - ALPHA_C)
        mlo, mhi, lmq = mu_window(al, M_mu)
        lo_s = "0 (none)" if mlo is None else f"{mlo:.6f}"
        hi_s = ">8" if mhi is None else f"{mhi:.6f}"
        d_lo = MU_PHYS if mlo is None else MU_PHYS - mlo
        d_hi = 8.0 - MU_PHYS if mhi is None else mhi - MU_PHYS
        mu_rows.append((al, mlo, mhi, d_lo, d_hi, lmq))
        info(f"  alpha = {al:.7f}  mu_- = {lo_s:>10s}  mu_+ = {hi_s:>10s}  "
             f"margins ({d_lo:+.4f}, {d_hi:+.4f})  lambda_min(Q) = {lmq:+.7f}")
        ok_mu = ok_mu and lmq >= -1e-9 and d_lo > 0.0 and d_hi > 0.0
    info("Resolution dependence of the window at the band top (the only place where "
         "it could close):")
    ok_top = True
    for M in (400, 800, 1600):
        mlo, mhi, lmq = mu_window(ALPHA_STAR, M, iters=18)
        d_lo = MU_PHYS if mlo is None else MU_PHYS - mlo
        d_hi = 8.0 - MU_PHYS if mhi is None else mhi - MU_PHYS
        ok_top = ok_top and mlo is not None and mhi is not None and d_lo > 0 and d_hi > 0
        info(f"  alpha* M = {M:5d}  mu_- = {mlo:.6f}  mu_+ = {mhi:.6f}  "
             f"margins ({d_lo:+.5f}, {d_hi:+.5f})  width = {mhi - mlo:.6f}")
    check("el_mu: mu_phys strictly inside the admissible coupling window everywhere, "
          "including the finest band-top resolution", ok_mu and ok_top)

    info("Extremiser profiles of Q (Euler-Lagrange solutions of the Nystrom "
         "collocation system, classical Nystrom/Fredholm theory):")
    for f_ in (0.05, 0.46, 1.0):
        al = ALPHA_C + f_ * (ALPHA_STAR - ALPHA_C)
        P, A, S, aux = window_matrices(al, M_sweep)
        wq, vq = np.linalg.eigh(P + A - MU_PHYS * S)
        v = vq[:, 0]
        d = 2.0 * al / M_sweep
        xc = -al + d * (np.arange(M_sweep) + 0.5)
        m2 = aux[2]
        mass_i = float(np.sum(v[xc < al - LOG2] ** 2))
        mass_j = float(np.sum(v[xc > -al + LOG2] ** 2))
        two_bump = float(np.sum(((v[:M_sweep - m2] + v[m2:]) / math.sqrt(2.0)) ** 2))
        sgn = int(np.sum(np.abs(np.diff(np.sign(v))) > 1.5))
        info(f"  alpha = {al:.7f}: lambda_min = {wq[0]:+.7f}  atom = "
             f"{float(v @ S @ v):+.6f}  mass(I) = {mass_i:.4f}  mass(J) = {mass_j:.4f}"
             f"  two-bump content = {two_bump:.4f}  sign changes = {sgn}  "
             f"|v|_max at x = {xc[int(np.argmax(np.abs(v)))]:+.4f}")
    info("Reading: the binding direction is EVEN, single-humped and low-frequency "
         "(no sign change, mass spread over the whole window, two-bump content far "
         "below the saturating value 1) -- NOT the C1 atom-extremal direction.  The "
         "atom term acts on it with a NEGATIVE h(log2), i.e. as a rescue rather "
         "than a threat.")
    return sweep, mu_rows


# ============================================== R5  C3 framing / enclosure
def r5_framing(t_plus, alpha_probe=None):
    head("R5    C3: framing the Nystrom result -- what is rigorous, what is not")
    if alpha_probe is None:
        alpha_probe = [ALPHA_C + f_ * (ALPHA_STAR - ALPHA_C) for f_ in (0.22, 0.70, 1.0)]
    ok_mono = True
    rich = []
    ladder = (100, 200, 400, 800, 1600)
    for al in alpha_probe:
        vals = []
        for M in ladder:
            P, A, S, _ = window_matrices(al, M)
            vals.append(lam_min(P, A, S, MU_PHYS))
        mono = all(vals[i + 1] <= vals[i] + 1e-12 for i in range(len(vals) - 1))
        ok_mono = ok_mono and mono
        p_obs = math.log(abs((vals[-3] - vals[-2]) / (vals[-2] - vals[-1]))) / math.log(2.0) \
            if abs(vals[-2] - vals[-1]) > 1e-15 else float("nan")
        lam_inf = vals[-1] - (vals[-2] - vals[-1]) / (2.0 ** p_obs - 1.0) if p_obs > 0.1 else vals[-1]
        rich.append((al, vals[-1], p_obs, lam_inf))
        info(f"  alpha = {al:.7f}  lambda_min(M={ladder[0]}..{ladder[-1]}) = "
             + " ".join(f"{v:+.7f}" for v in vals)
             + f"   order ~ {p_obs:.2f}   Richardson -> {lam_inf:+.3e}")
    al = alpha_probe[-1]
    deep = []
    for M in (300, 600, 1200, 2400):
        P, A, S, _ = window_matrices(al, M)
        deep.append(lam_min(P, A, S, MU_PHYS))
        del P, A, S
    p_deep = math.log(abs((deep[-3] - deep[-2]) / (deep[-2] - deep[-1]))) / math.log(2.0)
    lam_deep = deep[-1] - (deep[-2] - deep[-1]) / (2.0 ** p_deep - 1.0)
    info(f"  band-top refinement (independent nested ladder M = 300..2400 at alpha = "
         f"{al:.6f}): " + " ".join(f"{v:+.7f}" for v in deep)
         + f"   order ~ {p_deep:.2f}   Richardson -> {lam_deep:+.3e}")
    check(f"el_frame band top: the two independent extrapolations agree in sign and "
          f"order of magnitude ({rich[-1][3]:.2e} vs {lam_deep:.2e})",
          lam_deep > 0.0 and rich[-1][3] > 0.0
          and 0.2 < lam_deep / rich[-1][3] < 5.0)
    info("The extrapolations are NOT bounds; they say the continuum margin at the "
         f"band top is of order {lam_deep:.1e} -- four orders below the margin at "
         f"alpha_free and shrinking -- so alpha* = {ALPHA_STAR} behaves like the "
         "continuum positivity edge of the atom-rescued form.  The certified "
         "statement stops at the upper bounds.")
    rich[-1] = (al, deep[-1], p_deep, lam_deep)
    check("el_frame nesting: lambda_min^(M) decreases monotonically under grid "
          "refinement (nested PWC spaces => rigorous upper bounds)", ok_mono)
    info("RIGOROUS (i): the three forms are EXACT on PWC functions, so every value "
         "above is a genuine Rayleigh-Ritz upper bound for the continuum "
         "lambda_min.  A negative entry would DISPROVE T''; none occurs.  Upper "
         "bounds alone cannot establish T''.")

    worst = 0.0
    for al in alpha_probe:
        k24 = arch_coeffs(al, 400, 24)
        k48 = arch_coeffs(al, 400, 48)
        worst = max(worst, float(np.abs(k24[0] - k48[0]) + np.sum(np.abs(k24[1:] - k48[1:]))))
    check(f"el_frame quadrature: Schur bound on the 24-vs-48-node coefficient "
          f"difference gives |delta lambda_min| <= {worst:.3e}", worst < 1e-6)
    info("RIGOROUS (ii): with that Schur bound the Galerkin value is certified to "
         f"+-{worst:.2e}, i.e. the upper bounds above are quadrature-rigorous.")

    al = alpha_probe[-1]
    M = 200
    d = 2.0 * al / M
    edges = np.concatenate((np.linspace(0.0, 2.0, 9), np.arange(2.5, t_plus, 0.5), [t_plus]))
    tn, tw = gl_panels(np.unique(np.round(edges, 12)))
    with np.errstate(divide="ignore", invalid="ignore"):
        s2 = np.where(np.abs(tn) < 1e-12, d, 4.0 * np.sin(0.5 * tn * d) ** 2
                      / (np.where(tn == 0.0, 1.0, tn) ** 2 * d))
    kv = kappa_weil(tn)
    m = np.arange(M)
    rho = (2.0 / (2.0 * math.pi)) * (np.cos(np.outer(m, tn) * d) * (tw * kv * s2)[None, :]).sum(axis=1)
    row = rho.copy()
    row[1:] *= 0.5
    P, A, S, _ = window_matrices(al, M)
    lam_tr = float(np.linalg.eigvalsh(P + toeplitz_from_row(row))[0])
    lam_full = lam_min(P, A, S, MU_PHYS)
    info(f"RIGOROUS (iii) frequency reduction at alpha = {al:.6f}: dropping the "
         f"nonnegative tail |t| >= T_+ = {t_plus:.4f} leaves lambda_min(Q_trunc) = "
         f"{lam_tr:+.7f} against lambda_min(Q) = {lam_full:+.7f} (same PWC space, "
         f"M = {M}).")
    info(f"  The reduction is WASTEFUL: it discards {lam_full - lam_tr:+.6f} of the "
         "margin, and it cannot be repaired -- the truncated form's negative part is "
         "a nonzero positive-semidefinite band-limited operator while P_pole has rank "
         "2, so Q_trunc can never be >= 0 on a space of dimension > 2.  Band-limited "
         "reduction alone is NOT an instrument for T''.")

    b = 2.0 * al
    rho_u = lambda u: (2.0 * mpmath.e ** (-u / 2) / (1 - mpmath.e ** (-2 * u))) \
        * (1 - mpmath.e ** (-1.5 * u))
    r_norm = float(mpmath.quad(rho_u, [0, b]))
    p_norm = 2.0 * al + 2.0 * math.sinh(al)
    cb = -EULER - LOG_PI - math.log(-math.expm1(-2.0 * b))
    beta = r_norm + p_norm + MU_PHYS / 2.0
    need = beta - cb

    def kappa_D(T):
        f = lambda u: (2.0 * mpmath.e ** (-2 * u) / (1 - mpmath.e ** (-2 * u))) \
            * (1 - mpmath.cos(u * T))
        return float(mpmath.quad(f, [0, b]))

    eta = 0.5
    T_req = bisect_root(lambda T: (1.0 - eta) * kappa_D(math.exp(T)) - need,
                        math.log(10.0), math.log(1e18), iters=60)
    T_req = math.exp(T_req)
    d_req = math.sqrt(36.0 * math.pi * 0.5 / ((2.0 * al) * T_req ** 3))
    M_req = 2.0 * al / d_req
    info(f"RIGOROUS-ROUTE AUDIT (iv), projection defect: bounded part beta = "
         f"||R||_Schur {r_norm:.4f} + ||P_pole|| {p_norm:.4f} + mu_phys/2 "
         f"{MU_PHYS / 2:.4f} = {beta:.4f}; C_b = {cb:.4f}; required Dirichlet "
         f"weight (1-eta) kappa_D(T) >= {need:.4f} at eta = {eta}.")
    info(f"  kappa_D(T) = log(2 alpha T) + O(1) grows LOGARITHMICALLY, so the "
         f"required cut is T >= {T_req:.3e}, and the low-frequency bound "
         f"|rhat(t)| <= ||r|| |t| d sqrt(2 alpha/12) for cell-mean-zero r then "
         f"forces d <= {d_req:.3e}, i.e. M >= {M_req:.3e} cells, a dense matrix of "
         f"{M_req ** 2:.2e} entries.")
    check(f"el_frame: the projection-defect route is quantitatively refuted "
          f"(M_req = {M_req:.2e} exceeds the array cap by "
          f"{math.log10(M_req ** 2 / ARRAY_CAP):.1f} orders)", M_req ** 2 > 1e3 * ARRAY_CAP)
    info("  => the missing instrument for a LOWER bound is not resolution but a "
         "structural one: an operator inequality that keeps the Dirichlet part on "
         "the complement without paying a factor (1-eta).  Named, not claimed.")
    return rich, worst, (lam_tr, lam_full), (beta, cb, T_req, M_req)


# ================================================== R6  ledger and verdict
def r6_ledger(a_free, c1_rows, sweep, mu_rows, rich, quad_w, trunc, deadroute):
    head("R6    RIGOR LEDGER (type per statement; nothing upgraded silently)")
    lam_top = sweep[-1][3]
    lam_min_all = min(s[3] for s in sweep)
    c1_margin_top = c1_rows[-1][2]
    rows = [
        ("classical zone alpha <= alpha_c",
         "THEOREM (cited)", "Yoshida 1992 / Bombieri 2000 / Connes-Consani 2021; "
         "reproduced numerically here"),
        ("u-space archimedean identity",
         "EXACT (derived+verified)", f"psi integral representation; u vs t routes "
         f"agree to 1e-8, assembly exact to 1e-10"),
        ("|h_f(log2)| <= 1/2 on the band",
         "PROVED (elementary)", "I,J disjoint for alpha < log2 + Cauchy-Schwarz; "
         "sharp, saturated by two-bump f"),
        ("||S_atom|| = 1/2, dim E_(1/2) = |I|",
         "PROVED + verified", "no shift chains since 2 log2 > 2 alpha*; spectrum "
         "measured to 1e-12"),
        ("two-bump signature 2(1+cos t log2)",
         "EXACT", "verified to 1e-10"),
        ("T'' on E_(1/2) (atom-extremal directions)",
         "NUMERIC (quadrature-rigorous upper bounds)",
         f"margin >= {min(r[2] for r in c1_rows):+.4f} over the band"),
        ("prime-free crossing alpha_free",
         "NUMERIC", f"{a_free:.6f} (continuum Nystrom; 24-mode 0.3763 was an upper "
         f"bound)"),
        ("atom rescue h(log2) < 0 above alpha_free",
         "NUMERIC", "measured at every swept alpha with indefinite P+A"),
        ("T'' on the full band",
         "NUMERIC, NOT CERTIFIED", f"min lambda_min(Q) = {lam_min_all:+.3e} (upper "
         f"bound at the band top; two nested ladders extrapolate to "
         f"{rich[-1][3]:+.2e})"),
        ("coupling window contains mu_phys",
         "NUMERIC", "bisected at 6 alpha; both margins positive"),
        ("Galerkin values are upper bounds",
         "RIGOROUS (Rayleigh-Ritz, nested)", "monotone decrease verified"),
        ("quadrature certification",
         "RIGOROUS (Schur bound)", f"|delta lambda| <= {quad_w:.2e}"),
        ("frequency reduction |t| >= T_+",
         "RIGOROUS but WASTEFUL", f"loses {trunc[1] - trunc[0]:+.4f}; cannot close "
         f"(rank-2 pole vs psd negative part)"),
        ("projection-defect lower bound",
         "REFUTED (quantified)", f"needs M >= {deadroute[3]:.2e}; kappa_D grows only "
         f"like log T"),
        ("lower bound for continuum lambda_min",
         "OPEN", "the one missing link; no certificate exists in this probe"),
    ]
    for name, typ, note in rows:
        info(f"  {name:<42s} | {typ:<42s} | {note}")

    head("VERDICT (preregistered)")
    certified = False
    numeric_ok = (lam_min_all >= -1e-9
                  and all(r[3] > 0 and r[4] > 0 for r in mu_rows)
                  and all(r[2] > 0 for r in c1_rows))
    if certified:
        verdict = "T-CONTINUUM-CERTIFIED"
    elif numeric_ok:
        verdict = "T-CONTINUUM-NUMERIC"
    elif all(r[2] > 0 for r in c1_rows):
        verdict = "T-STRUCTURE"
    else:
        verdict = "T-BLOCKED"
    info(f"el_band  = {lam_min_all >= -1e-9}   (min lambda_min(Q) over the band = "
         f"{lam_min_all:+.3e})")
    info(f"el_mu    = {all(r[3] > 0 and r[4] > 0 for r in mu_rows)}   (mu_phys "
         f"interior to [mu_-, mu_+] at every swept alpha)")
    info(f"el_c1    = {all(r[2] > 0 for r in c1_rows)}   (restricted condition on the "
         f"atom-extremal subspace)")
    info(f"el_frame = certified upper side + quadrature ({quad_w:.1e}); lower side "
         f"OPEN => not CERTIFIED")
    print(f"""
  Does a CONTINUUM statement stand on the band?  Partly, and precisely:
    * YES, unconditionally: the atom form's sharp bound |h_f(log2)| <= 1/2, its
      extremal set (two identical bumps at distance log 2, an |I|-dimensional
      space), and the reduction of T'' on that set to
      lambda_min((P+A)|E) >= mu_phys/2 = {MU_PHYS / 2:.7f}.
    * YES, quadrature-rigorously, in ONE direction: continuum lambda_min(Q) <=
      the Nystrom values, so T'' is NOT disproved anywhere on (alpha_c, alpha*]
      at any resolution reached here; the upper bound at the band top is
      {lam_top:+.2e} and two nested ladders extrapolate to {rich[-1][3]:+.2e},
      i.e. positive but collapsing -- alpha* is the edge, not a safe interior
      point, and the margin falls by four orders across the band.
    * NO certificate for T'' itself: the lower bound is open.  The projection-
      defect route is refuted quantitatively (needs M ~ {deadroute[3]:.1e}); the
      band-limited reduction is rigorous but structurally too lossy.  What the
      numbers DO isolate is where a proof must bite: not on the atom-extremal
      two-bump directions (margin ~ {c1_margin_top:.2f} there), but on the single
      even low-frequency direction where the prime-free form turns negative and
      the atom term rescues it with h(log2) < 0.
  RH => (T''); (T'') does NOT imply RH.  Nothing above is evidence for or
  against RH, no zero data was used, and no promotion follows from this probe.
  Discovery sandbox only: no ledger, TeX, website, changelog or next.txt edit.""",
          flush=True)
    return verdict


def main():
    firewall()
    t0, t_plus = r1_kernel_and_map()
    a_free = r2_assembly()
    c1_rows, alpha_top, n_i = r3_c1_structure()
    sweep, mu_rows = r4_margin_curve(a_free)
    rich, quad_w, trunc, deadroute = r5_framing(t_plus)
    verdict = r6_ledger(a_free, c1_rows, sweep, mu_rows, rich, quad_w, trunc, deadroute)

    elapsed = time.time() - T_START
    head(f"TOTAL: {PASS} passed, {FAIL} failed  ({PASS + FAIL} checks, {elapsed:.1f}s)")
    print(f"VERDICT: {verdict}", flush=True)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
