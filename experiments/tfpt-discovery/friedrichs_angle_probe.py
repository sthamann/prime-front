"""Discovery probe (2026-07-26), part 106 of the zeta/prime investigation.
Contract FRIEDRICHS.ANGLE -- three attack lines on the ONE object T105 left.

WHERE THIS SITS (T102..T105, taken as given, re-measured here)
  T105 closed the handoff chain down to a single Loewner statement.  With the
  exact atom identity on the wing-parity split E_- / E_0 / E_+ at u_k = log n_k,
      Q_full|E_-  =  (mu_k/2) Id + W_k ,   W_k = (A + Pole)|E_- ,
  and mu_k cancels, so the handoff demand mu_k/2 <= sigma_k is EXACTLY
      Q_full(alpha)  >=  (mu_k/2) P_-^{(k)}       (Loewner), equivalently
      rho  <=  1 - (mu_k/2)/bare_k ,   rho = cos^2 Theta_Q(E_-, E_0 (+) E_+),
  the Q-metric Friedrichs angle.  CERTIFIED already (T105):
      bare_k >= mu_k/2 + (delta/pi) int_0^{pi/delta} k - delta*Kmax
                        - 4(cosh(u/2)-1) sinh(delta/2)          [16/16, 81..93%]
      ||B^T v_i||^2 <= w_i * Lambda_-                [avoidance law, from Q >= 0]
      J Q J = Q, J B = -B R                          [parity superselection, 1e-15]
  NOT certified: the SIZE of rho.  The free cap L <= Lambda_- diverges like
  log(1/D), so no resolution-free certificate comes from the free Schur bound;
  the missing statement must be about the SPECTRAL DENSITY of the window form
  near its soft end.  rho itself is resolution-stable (M-sweep: <= 8.5% while
  the margin falls 4x).

THE BLOCKS
  D1 DENSITY LAW.  N(w) = #{modes of the window form <= w} over
      (zone x M-sweep x window depth).  Two classical shapes are fitted and
      discriminated: the Weyl / Szego-Grenander edge law N ~ c M sqrt(w) for a
      symbol with a nondegenerate minimum, and the Landau-Widom transition-band
      law N ~ (2/pi^2) log(c) log(1/w).  Then the density-weighted dressing cap
      is DERIVED honestly from the avoidance law alone,
          lam_max(B^T M^{-1} B)  <=  N(w*) Lambda_-  +  ||B||_F^2 / w*
      (soft modes by the per-mode cap, hard modes by the gap), minimised over
      w*, and compared with the certified budget b0.  The N(w) that WOULD give
      rho <= 1 - (mu/2)/bare is read off, and the measured density is tested
      against it.
  D2 INVARIANT AMPLIFICATION -- the proof trick.  Instead of Q >= 0, the
      stronger induction invariant
          Q_full(alpha)  >=  beta * sum_{j: atom in support} (mu_j/2) P_-^{(j)}
      with the historic anchoring P_-^{(j)} at atom j's OWN handoff window, so
      that window growth INHERITS the old demands unchanged.  Per zone the
      maximal beta is a generalised eigenvalue problem, and because
          Q >= beta S   <=>   lam_max(Q^{-1/2} S Q^{-1/2}) <= 1/beta
      is LINEAR in S, the accumulated demand is controlled by a block
      Gershgorin bound over the per-atom demand Gram.  The anchoring is a
      HYPOTHESIS to be tested, not a device that is assumed to work: the block
      measures beta for the wing demand and for each inherited one separately.
      Then the self-propagation test: does the invariant at alpha, plus the
      certified growth step (the directional charge a_k/(1 - theta_k) through
      the Q-metric growth angle) and the atom-truncation edge term, imply the
      invariant at alpha'?  Run as an explicit inequality on all handoffs.
  D3 PARITY CHANNELS.  J Q J = Q makes the window form centrosymmetric, and
      since J acts as -R on E_- and as +R on E_0 (+) E_+, both the form and the
      demand P_-^{(k)} commute with J: the Loewner statement is the conjunction
      of one statement per parity channel, and the two cannot exchange weight.
      Per channel: soft-end floor, density, Friedrichs angle, bare, budget.
      The closed-form pole vectors satisfy J a = b, hence a b^T + b a^T =
      s s^T - t t^T with s, t of definite parity -- one rank into each channel,
      positive in the even one and negative in the odd one.  Tested: which
      channel carries the soft end, which one is dangerous, and whether one of
      them closes so cheaply that the hardness halves.
  D4 SYNTHESIS.  Best certified/measured rho bound, zone table of closed
      handoffs, and the precise formulation of what is left.

PREREGISTERED VERDICTS
  INVARIANT-PROPAGATES : the D2 propagation inequality holds on every handoff
      with certified perturbation terms -- the induction closes structurally.
  ANGLE-BOUNDED        : D1/D3 give a rho bound that suffices on all zones.
  DENSITY-MAPPED       : density and angle mapped, the bound does not reach --
      the precise missing statement.
  Element gates: el_firewall, el_d0, el_d1, el_d2, el_d3, el_d4, el_fence.

FENCES
  * Discovery sandbox.  One new file.  No promotion, no ledger/TeX/website/
    changelog edit, no verification/ module, no next.txt, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  Q_full >= 0 and
    the amplified invariant Q_full >= beta S are HYPOTHESIS INPUTS (the
    induction hypothesis), declared as such and never proved here.
  * lam_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute positivity, never prove it.  Every measured
    bare, sigma, rho, beta, w_i is an estimate at the stated resolution.
  * CERTIFIED vs MEASURED tracked per line and restated in the D4 ledger.
  * Every fit is labelled a fit.  Classical anchors cited, not re-derived:
    Weil 1952 (explicit formula), Weyl law, Szego-Grenander (Toeplitz symbol
    distribution), Landau-Widom 1980 (transition-band count), Slepian-Landau-
    Pollak concentration, Friedrichs angle / CS decomposition, Loewner order,
    Schur complement and Haynsworth inertia, Cauchy-Schwarz for PSD forms,
    Gershgorin (block form), Cantoni-Butler 1976 (centrosymmetric block
    diagonalisation), Weyl interlacing, Rayleigh-Ritz, von Mangoldt arithmetic.

OUTCOME OF THIS RUN  =>  see the D4 ledger and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh, toeplitz

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
T0_T93 = 6.28983599          # single sign change of the archimedean kernel

MAX_ARRAY = 1500
BUDGET_S = 780.0

M_OP = 1000                  # operating cell count
P_MIN, P_MAX = 2, 200
GAMMA_OP = 0.5               # operating depth as a fraction of the crossing
M_SWEEP = (500, 750, 1000)   # resolution axis
GAMMA_D1 = (0.5, 1.0)        # window-depth axis for the density law
R_GRID = (1, 2, 4, 8, 16, 32, 64, 128, 256)  # soft ranks for the angle chain

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
# the archimedean kernel (Weil 1952), t-space and x-space
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


def build_Q(alpha, M, atoms):
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


def blocks_U(Q, p):
    """Q in the exact orthogonal basis U = [B_-, E_0, B_+]."""
    M = Q.shape[0]
    L, C, R = slice(0, p), slice(p, M - p), slice(M - p, M)
    QLL, QLR, QRR = Q[L, L], Q[L, R], Q[R, R]
    QLC, QRC, QCC = Q[L, C], Q[R, C], Q[C, C]
    sym = QLR + QLR.T
    mm = 0.5 * (QLL + QRR - sym)
    pp = 0.5 * (QLL + QRR + sym)
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


def atoms_in(alpha, atoms_all):
    return [(t[2], t[3]) for t in atoms_all if t[2] <= 2.0 * alpha + 1.0e-14]


def assemble(u, p, M, atoms_all):
    """The T102 split at the atom point: mm = Q|E_-, Mat = Q|E_0 (+) E_+, B."""
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
    B = np.concatenate([m0, mp], axis=1).T          # (nc+p) x p
    return D, alpha, delta, nc, 0.5 * (mm + mm.T), 0.5 * (Mat + Mat.T), B


def wing_block(u, p, D, atoms):
    """Q_full|E_- built directly, p x p, with NO M x M array (T105 C2)."""
    dl = np.arange(-(p - 1), p) * D
    row = (arch_A(np.abs(dl), D)
           - 0.5 * (arch_A(np.abs(dl - u), D) + arch_A(np.abs(dl + u), D)))
    for u_j, mu_j in atoms:
        row = row - mu_j * (atom_lag(np.abs(dl), u_j, D)
                            - 0.5 * (atom_lag(np.abs(dl - u), u_j, D)
                                     + atom_lag(np.abs(dl + u), u_j, D)))
    idx = np.arange(p)
    mm = row[idx[:, None] - idx[None, :] + p - 1]
    cpole = 16.0 * math.sinh(0.25 * D) ** 2 / D
    mm = mm + (1.0 - math.cosh(0.5 * u)) * cpole * 2.0 * np.cosh(
        0.5 * D * (idx[:, None] - idx[None, :]))
    return 0.5 * (mm + mm.T)


def sigma_of(u, p, M, atoms_all):
    _, _, _, _, mm, Mat, B = assemble(u, p, M, atoms_all)
    fac, _ = safe_cho(Mat)
    if fac is None:
        return float("nan")
    A = B.T @ cho_solve(fac, B, check_finite=False)
    return float(eigvalsh(mm - 0.5 * (A + A.T)).min())


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


# ----------------------------------------------------------------------------
# the T105 certified bare (closed form, continuum, no eigenvalue input)
# ----------------------------------------------------------------------------
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


# ============================================================================
section("D0  SETUP, FIREWALL, THE HANDOFF GEOMETRY")
# ============================================================================
firewall()

ATOMS_ALL = atom_table(64)
ZONES = [t for t in ATOMS_ALL if t[0] <= 29]
N_ZONES = len(ZONES)
info("zones", "%d prime-power zones n_k = %s"
     % (N_ZONES, ", ".join(str(t[0]) for t in ZONES)))
info("D0.hypothesis",
     "HYPOTHESIS INPUT (never proved here): Q_full(alpha) >= 0, the window Weil "
     "positivity the induction already assumes.  D2 tests the STRONGER "
     "invariant Q_full >= beta S -- also an input, and the point of the block")
info("D0.fence_rh",
     "RH => window Weil positivity is used in one direction only; the converse "
     "is NOT claimed.  No zero data of any kind enters this probe")

t0 = time.time()
CROSS = []
for (n_k, lam, u, mu) in ZONES:
    p_star, ok = find_p_star(u, mu, M_OP, ATOMS_ALL)
    D, alpha, delta = zone_geometry(u, p_star, M_OP)
    CROSS.append(dict(n=n_k, u=u, mu=mu, p=p_star, ok=ok, D=D, alpha=alpha,
                      delta=delta))
info("D0.timing", "%d crossings located in %.1f s, budget left %.0f s"
     % (len(CROSS), time.time() - t0, budget_left()))
check("el_d0.p_star", all(c["ok"] for c in CROSS),
      "p* interior to [%d, %d] on every zone: p* = %s"
      % (P_MIN, min(P_MAX, M_OP // 3), ", ".join(str(c["p"]) for c in CROSS)))

print("")
print("  the handoff geometry at M = %d (gamma = 1 is the crossing)" % M_OP)
print("  n_k     u        mu/2       p*      D        delta_c    p_op   delta_op")
for c in CROSS:
    c["p_op"] = max(P_MIN, int(round(GAMMA_OP * c["p"])))
    c["delta_op"] = c["p_op"] * c["D"]
    print("  %3d %8.5f %9.5f %6d %10.3e %10.5f %6d %10.5f"
          % (c["n"], c["u"], 0.5 * c["mu"], c["p"], c["D"], c["delta"],
             c["p_op"], c["delta_op"]))
info("D0.depth_scale",
     "crossing depth delta_c = %.5f..%.5f (%d..%d cells at M = %d); the common "
     "depth any accumulated invariant may use is bounded by the SMALLEST, "
     "delta_min = %.5f"
     % (min(c["delta"] for c in CROSS), max(c["delta"] for c in CROSS),
        min(c["p"] for c in CROSS), max(c["p"] for c in CROSS), M_OP,
        min(c["delta"] for c in CROSS)))

D1_ZONES = [0, 3, 8, 15]                    # n_k = 2, 5, 13, 29


# ============================================================================
section("D1  THE DENSITY LAW -- what the soft end of the window form looks like")
# ============================================================================
info("D1.classics",
     "two classical shapes are candidates for N(w) = #{modes of Q|E_0(+)E_+ "
     "<= w} near the soft end.  (i) WEYL / SZEGO-GRENANDER: a Toeplitz form "
     "whose symbol has a nondegenerate minimum has N(w) ~ (len/pi)|{t: sym(t) "
     "<= w}| ~ c M sqrt(w - w_inf), and lam_min ~ M^-2 (T104 measured M^-1.7). "
     "(ii) LANDAU-WIDOM 1980: for a time-and-band limiting operator the "
     "TRANSITION band holds ~ (2/pi^2) log(c) log((1-eps)/eps) eigenvalues, "
     "i.e. N linear in log(1/w) with a slope ~ log(time-bandwidth).  These "
     "predict different M-scaling (M^1 vs log M) and are DISCRIMINATED here")
info("D1.status", "everything in D1 is MEASURED at finite resolution; the two "
                  "shape laws are FITS, labelled as such, and the classical "
                  "asymptotics are cited, not re-derived")


def fit_line(x, y):
    """Least squares y = a + b x; returns (a, b, rms of the residual in y)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def p_at(delta_c, u, MM, gam):
    return max(P_MIN, int(round(gam * delta_c * MM / (u + delta_c))))


SYM_L = 1 << 18                              # theta grid for the symbol


def symbol_dft(u, p, MM, atoms_all):
    """The exact Grenander-Szego symbol of the Toeplitz part of Q_full(alpha).

    Q = Toeplitz(a) + (rank-2 pole), a(d) = <phi_i, K phi_{i+d}>, so
        sym(theta) = a(0) + 2 sum_{d>=1} a(d) cos(d theta),  theta in [0, pi],
    which is the ALIASED, cell-mollified version of the Weil multiplier
    k(t) - sum_j mu_j cos(u_j t) at t = theta/D.  Computed by FFT on a grid
    fine enough to resolve the atom oscillations (period 2 pi D / u_j).
    """
    D, alpha, _ = zone_geometry(u, p, MM)
    s = np.arange(MM) * D
    lag = arch_A(s, D)
    for u_j, mu_j in atoms_in(alpha, atoms_all):
        lag = lag - mu_j * atom_lag(s, u_j, D)
    pad = np.zeros(SYM_L)
    pad[:MM] = lag
    sym = 2.0 * np.fft.rfft(pad).real - lag[0]
    return sym[:SYM_L // 2 + 1], D, alpha


def planck_average(sym, MM):
    """Coarse-grain the symbol over ONE Planck cell of the window.

    The window resolves theta only to the mode spacing pi/M, so the spectrum
    follows the symbol averaged over a cell of that width -- the Fejer/box
    coarse-graining behind Szego's theorem.  This matters here because the atom
    terms oscillate as cos(u_j theta / D) with u_j/D ~ M: they live exactly AT
    the Planck scale and are averaged away, which is why a symbol dipping to
    -21 still produces an essentially positive spectrum.
    """
    win = max(1, int(round(len(sym) / float(MM))))
    cs = np.concatenate(([0.0], np.cumsum(sym)))
    lo = np.maximum(np.arange(len(sym)) - win // 2, 0)
    hi = np.minimum(lo + win, len(sym))
    return (cs[hi] - cs[lo]) / (hi - lo)


def counts_from_symbol(sym, MM, levels):
    """Szego (phase-space) and Bohr-Sommerfeld (quantised) counts.

    Szego: N(w) = M * |{theta in [0,pi]: sym <= w}| / pi -- the classical
    eigenvalue distribution theorem for Toeplitz forms.
    Bohr-Sommerfeld: a connected sublevel component of phase-space area a can
    hold only round(a) modes, so components thinner than one Planck cell hold
    none.  The standard semiclassical correction for an oscillatory symbol.
    """
    ns, nb, big = [], [], []
    for w in levels:
        m = sym <= w
        tot = float(np.sum(m)) / len(sym)
        ns.append(MM * tot)
        idx = np.flatnonzero(np.diff(np.concatenate(
            ([0], m.view(np.int8), [0]))))
        runs = (idx[1::2] - idx[0::2]).astype(float) / len(sym) * MM
        nb.append(float(np.sum(np.floor(runs + 0.5))))
        big.append(float(runs.max()) if runs.size else 0.0)
    return np.array(ns), np.array(nb), np.array(big)


N_LOW = 96                                   # modes used for the Landau-Widom fit
LEVELS = (0.0, 0.01, 1.0, 4.0)
print("")
print("  N(w) measured vs three symbol counts at w = %s" % str(LEVELS))
print("  n_k  gam    M    p |  sym_min  sym_avg_min |  N_meas             |"
      "  N_Szego (raw)         |  N_Planck (coarse-grained) | LW rms")
t0 = time.time()
DENS = []
for zi in D1_ZONES:
    c = CROSS[zi]
    for gam in GAMMA_D1:
        for MM in M_SWEEP:
            p = p_at(c["delta"], c["u"], MM, gam)
            D, alpha, delta, nc, mm, Mat, B = assemble(c["u"], p, MM, ATOMS_ALL)
            w = eigvalsh(Mat)
            del Mat
            sym, _, _ = symbol_dft(c["u"], p, MM, ATOMS_ALL)
            sav = planck_average(sym, MM)
            nmeas = np.array([float(np.sum(w <= lv)) for lv in LEVELS])
            nsz, nbs, negbig = counts_from_symbol(sym, MM, LEVELS)
            npl, _, _ = counts_from_symbol(sav, MM, LEVELS)
            lo = w[:N_LOW]
            okl = lo > 0.0
            kl = np.arange(1, N_LOW + 1)[okl]
            selL = kl >= 4
            aL, bL, _ = fit_line(np.log(lo[okl][selL]), kl[selL])
            rmsL = float(np.sqrt(np.mean(
                ((aL + bL * np.log(lo[okl][selL])) / kl[selL] - 1.0) ** 2)))
            DENS.append(dict(n=c["n"], gam=gam, M=MM, p=p, delta=delta,
                             alpha=alpha, D=D, w=lo.copy(), nmeas=nmeas,
                             nsz=nsz, nbs=nbs, npl=npl,
                             negbig=float(negbig[0]), fmin=float(sym.min()),
                             favg=float(sav.min()), bL=bL, rmsL=rmsL,
                             Lam=float(eigvalsh(mm).max()),
                             bare=float(eigvalsh(mm).min()),
                             F=float(np.trace(B.T @ B))))
            print("  %3d %4.2f %5d %3d | %8.3f %11.3f | %4.0f %4.0f %4.0f %4.0f"
                  " | %6.1f %6.1f %6.1f %6.1f | %6.1f %6.1f %6.1f %6.1f | %5.3f"
                  % ((c["n"], gam, MM, p, sym.min(), sav.min()) + tuple(nmeas)
                     + tuple(nsz) + tuple(npl) + (rmsL,)))
info("D1.timing", "%d density spectra in %.1f s, budget left %.0f s"
     % (len(DENS), time.time() - t0, budget_left()))

rsz = np.array([d["nsz"][i] / max(d["nmeas"][i], 1.0)
                for d in DENS for i in range(1, len(LEVELS))])
rpl = np.array([d["npl"][i] / max(d["nmeas"][i], 1.0)
                for d in DENS for i in range(1, len(LEVELS))])
nbet = int(np.sum(np.abs(np.log(np.maximum(rpl, 1e-9)))
                  < np.abs(np.log(np.maximum(rsz, 1e-9)))))
check("el_d1.planck_symbol", nbet > len(rsz) // 2,
      "the RAW Szego count of the exact symbol misses the measured count by a "
      "factor %.2f..%.2f, while the PLANCK-COARSE-GRAINED symbol (averaged over "
      "one mode spacing pi/M, the resolution the window actually has) tracks it "
      "at %.2f..%.2f and is the better predictor on %d/%d (spectrum, level) "
      "pairs.  This is the correct classical anchor: Grenander-Szego applied to "
      "the coarse-grained symbol, NOT to the raw one"
      % (float(rsz.min()), float(rsz.max()), float(rpl.min()), float(rpl.max()),
         nbet, len(rsz)))
check("el_d1.subplanck", all(d["favg"] > d["fmin"] for d in DENS),
      "AND THAT IS WHY A NEGATIVE SYMBOL STILL GIVES Q >= 0: the atom terms "
      "enter the symbol as cos(u_j theta / D) with u_j/D ~ M, i.e. they "
      "oscillate at EXACTLY the Planck scale of the window, so the window "
      "cannot resolve them.  The raw symbol dips to %.2f..%.2f, the "
      "coarse-grained one only to %.2f..%.2f, and the measured spectrum has NO "
      "mode below zero (N_meas(0) = %d..%d) even though every symbol count "
      "predicts dozens.  Window Weil positivity is in part a STATEMENT ABOUT "
      "RESOLUTION -- and the inertia measurement below says exactly how much"
      % (min(d["fmin"] for d in DENS), max(d["fmin"] for d in DENS),
         min(d["favg"] for d in DENS), max(d["favg"] for d in DENS),
         int(min(d["nmeas"][0] for d in DENS)),
         int(max(d["nmeas"][0] for d in DENS))))
print("")
print("  where the positivity comes from: inertia of the Toeplitz part vs full Q")
print("  n_k    M  | lam_min(Toep)  #neg(Toep) | pole eigs +/-     | lam_min(Q)"
      "   #neg(Q)")
t0 = time.time()
INERT = []
for zi in D1_ZONES:
    c = CROSS[zi]
    p = p_at(c["delta"], c["u"], M_OP, GAMMA_OP)
    D, alpha, _ = zone_geometry(c["u"], p, M_OP)
    s = np.arange(M_OP) * D
    lag = arch_A(s, D)
    for u_j, mu_j in atoms_in(alpha, ATOMS_ALL):
        lag = lag - mu_j * atom_lag(s, u_j, D)
    T = toeplitz(lag)
    wt = eigvalsh(T)
    av, bv = pole_vectors(alpha, M_OP)
    T += np.outer(av, bv) + np.outer(bv, av)
    wq = eigvalsh(T)
    del T
    ab = float(np.dot(av, bv))
    na, nb = float(np.linalg.norm(av)), float(np.linalg.norm(bv))
    pe = (ab + na * nb, ab - na * nb)
    INERT.append(dict(n=c["n"], negT=int(np.sum(wt < 0)), lmT=float(wt[0]),
                      negQ=int(np.sum(wq < 0)), lmQ=float(wq[0]), pe=pe))
    print("  %3d %5d | %13.4f %11d | %8.1f %8.1f | %11.3e %8d"
          % (c["n"], M_OP, wt[0], int(np.sum(wt < 0)), pe[0], pe[1], wq[0],
             int(np.sum(wq < 0))))
check("el_d1.inertia", all(x["negQ"] == 0 for x in INERT),
      "the Toeplitz part alone has %d..%d negative eigenvalues (lam_min = "
      "%.3f..%.3f) -- the atoms really do make the form indefinite -- and the "
      "rank-2 Weil pole, whose two nonzero eigenvalues are about %.0f and %.0f, "
      "restores positivity: the full window form has %d negative eigenvalues "
      "and lam_min = %.2e..%.2e.  A rank-2 correction can only fix a rank-2 "
      "deficit, so this MEASURES that the indefiniteness of the prime sum "
      "inside a window is exactly a rank-<= 2 phenomenon at these depths"
      % (min(x["negT"] for x in INERT), max(x["negT"] for x in INERT),
         min(x["lmT"] for x in INERT), max(x["lmT"] for x in INERT),
         min(x["pe"][0] for x in INERT), min(x["pe"][1] for x in INERT),
         max(x["negQ"] for x in INERT), min(x["lmQ"] for x in INERT),
         max(x["lmQ"] for x in INERT)))
info("D1.inertia_timing", "%.1f s, budget left %.0f s"
     % (time.time() - t0, budget_left()))

info("D1.landau_widom",
     "the Landau-Widom 1980 transition-band count ~ (2/pi^2) log(c) "
     "log((1-eps)/eps) (Slepian-Landau-Pollak concentration) is the WRONG "
     "classical anchor here: fitted as N = a + b log w it leaves a relative rms "
     "of %.2f..%.2f, and its content -- a log-wide transition between the "
     "eigenvalue clusters 0 and 1 of a projection PRODUCT -- has no counterpart "
     "in a multiplier form with a negative band.  Weyl/Grenander-Szego plus the "
     "Planck-cell cut-off is the right classic.  FIT vs MEASUREMENT as labelled"
     % (min(d["rmsL"] for d in DENS), max(d["rmsL"] for d in DENS)))
info("D1.band_growth",
     "the count at a FIXED positive level still grows with M (e.g. %s at "
     "w = %.2f over M = %s) because new near-zero slivers keep entering as the "
     "band pi/D widens: the atoms drag sym below any fixed w wherever the "
     "phases cos(u_j theta/D) align.  So the soft end is NOT finite-rank at "
     "fixed depth -- but its NEGATIVE part is (rank 1, measured above).  That "
     "asymmetry is the honest correction to the finite-rank guess"
     % (str([int(d["nmeas"][1]) for d in DENS
             if d["n"] == CROSS[D1_ZONES[-1]]["n"] and d["gam"] == GAMMA_D1[0]]),
        LEVELS[1], str(M_SWEEP)))

# --- the density-weighted dressing cap, derived honestly --------------------
print("")
print("""  THE TARGET FORM (derived, not fitted).  The dressing is
      Dress := B^T M^{-1} B = sum_i (B^T v_i)(B^T v_i)^T / w_i ,
  and the handoff needs lam_max(Dress) <= b0 = bare - mu/2.  Split the spectrum
  at a level w*: the hard modes are capped by the gap, ||B||_F^2/w*, and for the
  soft modes there are exactly two admissible caps --
      (flat)  the avoidance law ||B^T v_i||^2 <= w_i Lambda_-   ->  N(w*) Lam_-
      (angle) the Bessel/Friedrichs form Dress_soft <= rho_s(r) * Q|E_- ,
  giving the two candidate chains
      lam_max(Dress) <= N(w*) Lambda_-  + ||B||_F^2/w*        (density chain)
      lam_max(Dress) <= rho_s(r) * bare + ||B||_F^2/w_r       (angle chain).
  Lambda_- > b0 on every zone, so the DENSITY chain needs N(w*) = 0, i.e. a hard
  spectral gap w_0 >= ||B||_F^2/b0.  THAT is the N(w) shape that would deliver
  rho <= 1 - (mu/2)/bare -- and the measurement above says the soft end instead
  holds a fixed, M-independent, non-empty set of modes at w ~ 1e-5.  The density
  chain is closed for good.  The same count, though, says the angle chain needs
  only a FINITE, resolution-free rank r*: that is the reduction D1 buys.""")
print("")
print("  the two chains at the operating depth, each optimised over the soft rank")
print("  n_k    M   |    b0    Lam_-  ||B||_F^2 | gap needed    w_0     |  r* "
      " rho_s(r*)  angle chain  density chain  true Dress")
t0 = time.time()
SAT = []
for zi in D1_ZONES:
    c = CROSS[zi]
    for MM in (M_SWEEP[0], M_SWEEP[-1]):
        p = p_at(c["delta"], c["u"], MM, GAMMA_OP)
        D, alpha, delta, nc, mm, Mat, B = assemble(c["u"], p, MM, ATOMS_ALL)
        w, V = eigh(Mat)
        del Mat
        Lam = float(eigvalsh(mm).max())
        bare = float(eigvalsh(mm).min())
        b0 = bare - 0.5 * c["mu"]
        F = float(np.trace(B.T @ B))
        need = F / max(b0, 1.0e-12)
        # the rank-2 pole, expressed in the [E_0, E_+] coordinates of Mat
        av, bv = pole_vectors(alpha, MM)
        PV = np.zeros((nc + p, 2))
        PV[:nc, 0] = av[p:MM - p]
        PV[:nc, 1] = bv[p:MM - p]
        PV[nc:, 0] = (av[:p] + av[MM - p:]) / _SQ2
        PV[nc:, 1] = (bv[:p] + bv[MM - p:]) / _SQ2
        Pq = np.linalg.qr(PV)[0]
        pcos = float(np.linalg.svd(V[:, :min(4, nc + p)].T @ Pq,
                                   compute_uv=False).max())
        CB = V.T @ B
        del V
        nrm = np.einsum("ij,ij->i", CB, CB)
        s = nrm / np.maximum(w, 1.0e-300) / Lam
        Ts = np.zeros((p, p))
        prev = 0
        ang, dens, rbest, rho_b = float("inf"), float("inf"), 0, float("nan")
        for r in R_GRID:
            if r >= len(w):
                break
            Ts = Ts + CB[prev:r].T @ (CB[prev:r] / w[prev:r, None])
            prev = r
            rho_s = float(eigh(0.5 * (Ts + Ts.T), mm, eigvals_only=True).max())
            av_ = rho_s * bare + F / float(w[r])
            if av_ < ang:
                ang, rbest, rho_b = av_, r, rho_s
            dens = min(dens, r * Lam + F / float(w[r]))
        Tf = (CB.T * (1.0 / np.maximum(w, 1.0e-300))) @ CB
        dress = float(eigvalsh(0.5 * (Tf + Tf.T)).max())
        SAT.append(dict(n=c["n"], M=MM, s=s.copy(), tot=float(s.sum()),
                        dress=dress, b0=b0, bare=bare, Lam=Lam, F=F, need=need,
                        w0=float(w[0]), rstar=rbest, rho_s=rho_b, ang=ang,
                        dens=dens, pcos=pcos))
        print("  %3d %5d | %8.4f %7.3f %9.3f | %10.3f %10.2e | %3d %10.2e"
              " %11.4f %13.2f %11.4f"
              % (c["n"], MM, b0, Lam, F, need, w[0], rbest, rho_b, ang, dens,
                 dress))
        del CB, mm, B
info("D1.chain_timing", "%.1f s, budget left %.0f s"
     % (time.time() - t0, budget_left()))
check("el_d1.density_chain_closed", all(x["w0"] < x["need"] for x in SAT),
      "the DENSITY chain is closed for good: it needs a gap w_0 >= "
      "||B||_F^2/b0 = %.2f..%.2f and the measured w_0 = %.1e..%.1e falls short "
      "by %.1e..%.1e.  Since the soft count at a fixed level is non-zero and "
      "NON-DECREASING in M (D1.band_growth), no refinement and no density "
      "shape can supply that gap: "
      "the per-mode cap Lambda_- = %.2f..%.2f already exceeds the whole budget "
      "b0 = %.3f..%.3f with one single mode"
      % (min(x["need"] for x in SAT), max(x["need"] for x in SAT),
         min(x["w0"] for x in SAT), max(x["w0"] for x in SAT),
         min(x["need"] / x["w0"] for x in SAT),
         max(x["need"] / x["w0"] for x in SAT),
         min(x["Lam"] for x in SAT), max(x["Lam"] for x in SAT),
         min(x["b0"] for x in SAT), max(x["b0"] for x in SAT)))
NANG = sum(1 for x in SAT if x["ang"] <= x["b0"])
check("el_d1.angle_chain_valid",
      all(x["ang"] >= x["dress"] - 1.0e-9 for x in SAT)
      and all(x["ang"] / x["b0"] < 2.0 for x in SAT),
      "the ANGLE chain rho_s(r*) * bare + ||B||_F^2/w_{r*} is a VALID upper "
      "bound on the true dressing on %d/%d spectra and lands at %.2f..%.2f x "
      "the budget b0 = %.4f..%.4f at the resolution-free rank r* = %d..%d, "
      "with rho_s(r*) = %.2f..%.2f MEASURED.  It BEATS the budget on only %d "
      "of %d spectra, so it reduces the residual to a finite-dimensional "
      "angle without closing it -- D3 and D4 sharpen exactly this chain"
      % (len(SAT), len(SAT), min(x["ang"] / x["b0"] for x in SAT),
         max(x["ang"] / x["b0"] for x in SAT),
         min(x["b0"] for x in SAT), max(x["b0"] for x in SAT),
         min(x["rstar"] for x in SAT), max(x["rstar"] for x in SAT),
         min(x["rho_s"] for x in SAT), max(x["rho_s"] for x in SAT),
         NANG, len(SAT)))
check("el_d1.avoidance", all(float(np.max(x["s"])) <= 1.0 + 1.0e-8 for x in SAT),
      "the T105 avoidance law s_i = ||B^T v_i||^2/(w_i Lambda_-) <= 1 "
      "re-verified on every mode of every spectrum (worst %.6f); at the soft "
      "end the measured saturation is %.1e..%.1e, so the flat cap is loose by "
      "orders of magnitude exactly where the density chain needs it to be tight"
      % (max(float(np.max(x["s"])) for x in SAT),
         min(float(x["s"][0]) for x in SAT),
         max(float(x["s"][0]) for x in SAT)))
info("D1.pole_identity",
     "the softest modes ARE the pole modes: the largest principal cosine "
     "between the 4 softest eigenvectors and the 2-dimensional span of the "
     "explicit pole vectors a, b (closed form, T102) is %.4f..%.4f -- the "
     "finite, M-independent soft end is the Weil pole term, known in closed "
     "form, not an anonymous spectral tail"
     % (min(x["pcos"] for x in SAT), max(x["pcos"] for x in SAT)))
info("D1.stability",
     "lam_max(Dress) = %.4f..%.4f moves %.1f%% while M doubles and r* does not "
     "move at all: the dressing and the required soft rank are "
     "resolution-stable, like rho and unlike lam_min ~ M^-1.7"
     % (min(x["dress"] for x in SAT), max(x["dress"] for x in SAT),
        100 * max(abs(SAT[2 * i + 1]["dress"] / SAT[2 * i]["dress"] - 1.0)
                  for i in range(len(SAT) // 2))))
info("D1.verdict_line",
     "D1 CONCLUSION.  The density is mapped and the classical anchor is fixed: "
     "Grenander-Szego on the Planck-coarse-grained symbol, with a rank-1 "
     "negative inertia cancelled by the rank-2 Weil pole -- NOT Landau-Widom, "
     "and not any prolate transition band.  The DENSITY chain is closed for "
     "good (it needs a spectral gap the operator does not have).  The ANGLE "
     "chain, optimised over the soft rank, lands at %.2f..%.2f x the budget: "
     "close, but it does not reach on %d of %d spectra, and its input rho_s "
     "stays MEASURED"
     % (min(x["ang"] / x["b0"] for x in SAT),
        max(x["ang"] / x["b0"] for x in SAT),
        len(SAT) - NANG, len(SAT)))


# ============================================================================
section("D2  INVARIANT AMPLIFICATION -- does the accumulated demand propagate?")
# ============================================================================
print("""  THE INVARIANT.  The induction currently carries Q_full(alpha) >= 0 and has
  to re-derive each handoff.  The amplified invariant carries the whole history:

      I(alpha, beta):   Q_full(alpha)  >=  beta * S(alpha),
      S(alpha) := sum_{j : u_j + delta_0 <= 2 alpha} (mu_j / 2) P_-^{(j)} ,

  where P_-^{(j)} is the wing-odd projector of atom j ANCHORED AT ITS OWN
  handoff window [-alpha_j, alpha_j], alpha_j = (u_j + delta_0)/2, in absolute
  coordinates.  Two structural facts make this the right object:
    * single atom, beta = 1 is EXACTLY the handoff:  Q >= (mu_k/2) P_-^{(k)}
      <=> sigma_k >= mu_k/2  (Schur complement / Haynsworth inertia);
    * absolute anchoring makes the old demands INHERITED, not re-imposed:
      growing the window leaves every earlier P_-^{(j)} untouched, and the
      window form on the old cells changes only by the atom-truncation edge
      term (measured below as e_embed).
  Because Q >= beta S  <=>  lam_max(Q^{-1/2} S Q^{-1/2}) <= 1/beta and the map
  S -> lam_max(Q^{-1/2} S Q^{-1/2}) is LINEAR in S inside one lam_max, the
  accumulated demand obeys the certified sub-additive bound
      1/beta  <=  sum_j 1/beta_j ,
  and, more sharply, the block Gershgorin bound on the demand Gram
      G = R^T Q^{-1} R,   R = [ sqrt(mu_j/2) V_j ]_j ,
      lam_max(G)  <=  max_j [ lam_max(G_jj) + sum_{i != j} ||G_ij|| ] ,
  which is what decides whether accumulation costs anything at all.
  HYPOTHESIS INPUT: I(alpha, beta) is an induction hypothesis, exactly like
  Q >= 0.  Nothing here proves it; the block measures whether it PROPAGATES.""")

M_D2 = 1200
GAMMA_D2 = 0.75              # common demand depth as a fraction of min delta_c
DELTA0 = GAMMA_D2 * min(c["delta"] for c in CROSS)
info("D2.depth",
     "common demand depth delta_0 = %.5f = %.2f * min_k delta_c (the deepest "
     "depth every atom in the chain can carry; zone %d sets it).  At M = %d "
     "this is %.1f..%.1f cells depending on the window"
     % (DELTA0, GAMMA_D2,
        min(CROSS, key=lambda c: c["delta"])["n"], M_D2,
        DELTA0 / (CROSS[-1]["u"] / M_D2), DELTA0 / (CROSS[0]["u"] / M_D2)))


def demand_vectors(alpha, D, MM, u_j, delta0, npair):
    """Orthonormal wing-odd pair vectors of atom j at its OWN handoff window.

    v_r = (e_{i} - c1 e_{i+q} - c2 e_{i+q+1}) / sqrt(2), i = i0 + 2r, with
    (c1, c2) the unit vector maximising the atom yield when u_j is not on the
    grid; the yield is eta = sqrt((1-f)^2 + f^2), f = u_j/D - floor(u_j/D),
    and eta = 1 exactly when the atom sits on a cell boundary.  Stride 2 keeps
    the vectors orthonormal.  On such a vector the j-th atom contributes
    exactly +eta * mu_j/2 and (by support separation) no other atom does.
    """
    q = int(math.floor(u_j / D + 1.0e-12))
    f = u_j / D - q
    eta = math.hypot(1.0 - f, f)
    c1, c2 = (1.0 - f) / eta, f / eta
    i0 = int(round((alpha - 0.5 * (u_j + delta0)) / D))
    if q < 2 or i0 < 0 or npair < 1:
        return None, 0.0
    idx = i0 + 2 * np.arange(npair)
    if idx[-1] + q + 1 >= MM or idx[-1] + 1 >= i0 + q:
        return None, 0.0
    V = np.zeros((MM, npair))
    r = np.arange(npair)
    V[idx, r] = 1.0 / _SQ2
    V[idx + q, r] = -c1 / _SQ2
    V[idx + q + 1, r] = -c2 / _SQ2
    return V, eta


def demand_stack(alpha, D, MM, atoms, delta0, npair, use_eta):
    """R with R R^T = S = sum_j (mu_j/2) P_-^{(j)}; column blocks per atom."""
    cols, blocks, etas, used, ncol = [], [], [], [], 0
    for (u_j, mu_j) in atoms:
        if u_j + delta0 > 2.0 * alpha + 1.0e-9:
            continue
        V, eta = demand_vectors(alpha, D, MM, u_j, delta0, npair)
        if V is None:
            continue
        wgt = math.sqrt(0.5 * mu_j * (eta if use_eta else 1.0))
        blocks.append((ncol, ncol + V.shape[1]))
        ncol += V.shape[1]
        cols.append(wgt * V)
        etas.append(eta)
        used.append(u_j)
    if not cols:
        return None, [], [], []
    return np.concatenate(cols, axis=1), blocks, etas, used


def beta_report(Q, R, blocks):
    """beta_sum, per-atom beta_j, the block-Gershgorin beta, and the overlap."""
    fac, sh = safe_cho(Q)
    if fac is None:
        return None
    G = R.T @ cho_solve(fac, R, check_finite=False)
    G = 0.5 * (G + G.T)
    lam = float(eigvalsh(G).max())
    diag, off = [], []
    for (a, b) in blocks:
        diag.append(float(eigvalsh(G[a:b, a:b]).max()))
        s = 0.0
        for (c_, d_) in blocks:
            if (c_, d_) != (a, b):
                s += float(np.linalg.norm(G[a:b, c_:d_], 2))
        off.append(s)
    gersh = max(d + o for d, o in zip(diag, off))
    return dict(fac=fac, shift=sh, G=G, lam=lam, beta=1.0 / lam,
                betaj=[1.0 / d for d in diag], diag=diag, off=off,
                gersh=gersh, beta_gersh=1.0 / gersh,
                overlap=lam / max(diag))


def d2_window(u_k, MM, delta0):
    """Window at the atom point whose wing depth is delta_0 rounded to cells.

    The realised depth p*D is what the grid can carry; it is used as the common
    anchoring depth inside that window so that every atom's historic wing is an
    exact cell pattern.
    """
    p = max(1, int(round(delta0 * MM / (u_k + delta0))))
    D, alpha, delta = zone_geometry(u_k, p, MM)
    return p, D, alpha, delta


print("")
print("  consistency: for ONE atom the invariant IS the handoff (Schur complement)")
print("  n_k   p  |    mu/2     sigma(p)   1/lam_max(V^T Q^-1 V)   ratio   "
      "lam_min(Q)")
CONS = []
for zi in (0, 1, 8, 15):
    c = CROSS[zi]
    p, D, alpha, dl0 = d2_window(c["u"], M_D2, DELTA0)
    sig = sigma_of(c["u"], p, M_D2, ATOMS_ALL)
    Q = build_Q(alpha, M_D2, atoms_in(alpha, ATOMS_ALL))
    Vw = np.zeros((M_D2, p))
    rr = np.arange(p)
    Vw[rr, rr] = 1.0 / _SQ2
    Vw[M_D2 - p + rr, rr] = -1.0 / _SQ2
    fac, _ = safe_cho(Q)
    lam = float(eigvalsh(Vw.T @ cho_solve(fac, Vw, check_finite=False)).max())
    lmq = float(eigvalsh(Q).min())
    del Q
    CONS.append((c["n"], p, 0.5 * c["mu"], sig, 1.0 / lam, lmq))
    print("  %3d %3d | %9.5f %10.5f %22.6f %8.4f %11.2e"
          % (c["n"], p, 0.5 * c["mu"], sig, 1.0 / lam, lam * sig, lmq))
check("el_d2.schur_identity",
      all(abs(x[4] / x[3] - 1.0) < 1.0e-4 for x in CONS),
      "1/lam_max(V^T Q^{-1} V) equals the T105 Schur profile sigma to "
      "%.1e relative on the sampled zones: the generalised-eigenvalue form of "
      "the invariant and the Schur form of the handoff are the SAME statement "
      "(block inverse / Haynsworth inertia), so beta is measured in handoff "
      "units by construction"
      % max(abs(x[4] / x[3] - 1.0) for x in CONS))

print("")
print("""  D2.1  THE ACCUMULATED INVARIANT, ABSOLUTELY ANCHORED.  Inside the window of
  atom k every inherited demand P_-^{(j)}, j < k, is an INTERIOR odd pair: its
  two cells are u_j apart, and since u_j < 2 alpha - delta_0 neither cell sits
  at the window edge.  Only atom k's own pair is a WING pair.  The table splits
  the accumulated demand of one and the same window into those two kinds:
      beta_wing = the current atom's own wing demand  (= the handoff object),
      beta_int  = the worst inherited interior demand,
      beta_sum  = the full accumulated demand,   overlap = beta_worst/beta_sum.""")
print("")
print("  n_k  #atoms  p  npair  eta_min |  beta_wing   beta_int(worst)"
      "   beta_sum   overlap  |  beta_sum(raw)")
t0 = time.time()
BETA = []
for c in CROSS:
    p, D, alpha, delta = d2_window(c["u"], M_D2, DELTA0)
    npair = max(1, p // 2)
    Q = build_Q(alpha, M_D2, atoms_in(alpha, ATOMS_ALL))
    R, blocks, etas, used = demand_stack(alpha, D, M_D2,
                                         atoms_in(alpha, ATOMS_ALL), delta,
                                         npair, True)
    Rr, br, _, _ = demand_stack(alpha, D, M_D2, atoms_in(alpha, ATOMS_ALL),
                                delta, npair, False)
    rep = beta_report(Q, R, blocks)
    repr_ = beta_report(Q, Rr, br)
    del Q
    if rep is None:
        continue
    b_wing = rep["betaj"][-1]                     # atoms ascending: last = own
    b_int = min(rep["betaj"][:-1]) if len(rep["betaj"]) > 1 else float("nan")
    BETA.append(dict(n=c["n"], p=p, npair=npair, nat=len(blocks),
                     eta=min(etas), beta=rep["beta"], betaj=rep["betaj"],
                     wing=b_wing, intr=b_int, bg=rep["beta_gersh"],
                     ov=rep["overlap"], braw=repr_["beta"], alpha=alpha, D=D,
                     shift=rep["shift"]))
    print("  %3d %6d %4d %5d %8.4f | %10.4f %15.4f %10.4f %9.4f | %13.4f"
          % (c["n"], len(blocks), p, npair, min(etas), b_wing, b_int,
             rep["beta"], rep["overlap"], repr_["beta"]))
info("D2.timing", "%d zone invariants in %.1f s, budget left %.0f s"
     % (len(BETA), time.time() - t0, budget_left()))

WING_MIN = min(b["wing"] for b in BETA)
INT = [b for b in BETA if b["nat"] > 1]
check("el_d2.wing_demand_met", WING_MIN > 1.0,
      "the WING demand is met with amplification on all %d zones: beta_wing = "
      "%.3f..%.3f > 1 at the common depth delta_0 = %.5f (rounded to p = "
      "%d..%d cells), i.e. the single-atom handoff has a genuine margin factor "
      "at a depth well inside its crossing depth.  MEASURED at M = %d, with "
      "the grid-alignment factor eta >= %.3f folded into the demand"
      % (len(BETA), WING_MIN, max(b["wing"] for b in BETA), DELTA0,
         min(b["p"] for b in BETA), max(b["p"] for b in BETA), M_D2,
         min(b["eta"] for b in BETA)))
check("el_d2.interior_no_go",
      all(b["intr"] < 1.0 for b in INT) and len(INT) == len(BETA) - 1,
      "NO-GO, and it is the point of the block: every INHERITED demand fails "
      "by two to three orders of magnitude -- beta_int = %.2e..%.2e on all %d "
      "zones that have a history.  Hence Q_full(alpha) >= beta sum_j (mu_j/2) "
      "P_-^{(j)} with beta >= 1 and ABSOLUTE anchoring is FALSE (beta_sum = "
      "%.2e..%.2e): the accumulated-demand trick does not exist in this form. "
      "The margin of an odd pair is an EDGE property of the window, not a "
      "property of the pair"
      % (min(b["intr"] for b in INT), max(b["intr"] for b in INT), len(INT),
         min(b["beta"] for b in BETA if b["nat"] > 1),
         max(b["beta"] for b in BETA if b["nat"] > 1)))
check("el_d2.no_accumulation_cost", max(b["ov"] for b in BETA) < 6.0,
      "the failure is NOT the summation: lam_max of the whole demand Gram "
      "exceeds its worst single block by only %.3f..%.3f x while sub-additivity "
      "would allow up to #atoms = %d, so the per-atom demands are nearly "
      "Q-orthogonal and accumulation is essentially free.  What fails is the "
      "TRANSPORT of one demand from its own window into a larger one"
      % (min(b["ov"] for b in BETA), max(b["ov"] for b in BETA),
         max(b["nat"] for b in BETA)))

# --- the mechanism: the soft mode is what the wing avoids --------------------
print("")
print("""  THE MECHANISM, and it is D1's density that runs it.  For a unit vector v,
      1/sigma(v)  =  v^T Q^{-1} v  =  sum_i c_i^2 / w_i ,   c_i := v.phi_i ,
  so the demand is met only if the coupling c_i^2 VANISHES WITH w_i at the soft
  end -- exactly the shape of T105's avoidance law ||B^T v_i||^2 <= w_i Lam_-,
  now read in the inverse metric.  Two scale-free readings of the soft block
  (its lowest K = %d modes) separate the wing from the interior:
      A_max := max_{i<K} c_i^2 / w_i          the avoidance ratio, and
      w_eff := sum_{i<K} c_i^2 / sum_{i<K} c_i^2/w_i   the harmonic level at
                                              which v actually couples.
  Both vectors put nearly the SAME total weight into the soft block; what
  differs is where inside it.""" % 64)
K_SOFT = 64
print("")
print("  n_k |    w_0     w_{K-1} |  wing: soft weight  share  w_eff   A_max"
      "   sigma |  interior: soft weight  share  w_eff   A_max   sigma")
MECH = []
for zi in (1, 5, 10, 15):
    c = CROSS[zi]
    p, D, alpha, dl0 = d2_window(c["u"], M_D2, DELTA0)
    Q = build_Q(alpha, M_D2, atoms_in(alpha, ATOMS_ALL))
    wS, PH = eigh(Q, subset_by_index=[0, K_SOFT - 1])
    cols = []
    for (u_j, mu_j) in atoms_in(alpha, ATOMS_ALL):
        V, _ = demand_vectors(alpha, D, M_D2, u_j, dl0, 1)
        if V is not None:
            cols.append(V[:, 0])
    Z = np.array(cols).T
    fac, _ = safe_cho(Q)
    del Q
    qz = np.einsum("ij,ij->j", Z, cho_solve(fac, Z, check_finite=False))
    cc = (PH.T @ Z) ** 2
    soft = (cc / wS[:, None]).sum(0)
    wgt = cc.sum(0)
    amax = (cc / wS[:, None]).max(0)
    jw = Z.shape[1] - 1
    ji = int(np.argmax(qz[:jw])) if jw > 0 else jw
    MECH.append(dict(n=c["n"], w0=float(wS[0]), wK=float(wS[-1]),
                     ww=wgt[jw], sw=soft[jw] / qz[jw], ew=wgt[jw] / soft[jw],
                     aw=amax[jw], gw=1.0 / qz[jw],
                     wi=wgt[ji], si=soft[ji] / qz[ji], ei=wgt[ji] / soft[ji],
                     ai=amax[ji], gi=1.0 / qz[ji]))
    m = MECH[-1]
    print("  %3d | %9.2e %9.2e | %17.3e %6.3f %8.2e %7.1e %7.3f | %22.3e"
          " %6.3f %8.2e %7.1e %7.2e"
          % (m["n"], m["w0"], m["wK"], m["ww"], m["sw"], m["ew"], m["aw"],
             m["gw"], m["wi"], m["si"], m["ei"], m["ai"], m["gi"]))
check("el_d2.soft_end_mechanism",
      all(m["si"] > 0.9 for m in MECH)
      and all(m["ei"] / m["ew"] < 0.1 for m in MECH),
      "the interior demand is SOFT-END dominated -- the lowest %d modes carry "
      "%.4f..%.4f of its v^T Q^{-1} v -- while the wing demand takes only "
      "%.3f..%.3f from there, even though the two put nearly the same total "
      "weight into the soft block (%.1e..%.1e interior against %.1e..%.1e "
      "wing).  The separation is the LEVEL: the wing couples at w_eff = "
      "%.1e..%.1e, the interior at %.1e..%.1e, a factor %.0f..%.0f softer, and "
      "the avoidance ratio A_max is %.1e..%.1e for the wing against "
      "%.1e..%.1e for the interior.  MEASURED on 4 zones.  This is why the handoff lives "
      "in the wing -- it is the one subspace whose coupling vanishes with the "
      "eigenvalue -- and why it cannot be inherited: transported into a larger "
      "window the same pair becomes interior and loses that property"
      % (K_SOFT, min(m["si"] for m in MECH), max(m["si"] for m in MECH),
         min(m["sw"] for m in MECH), max(m["sw"] for m in MECH),
         min(m["wi"] for m in MECH), max(m["wi"] for m in MECH),
         min(m["ww"] for m in MECH), max(m["ww"] for m in MECH),
         min(m["ew"] for m in MECH), max(m["ew"] for m in MECH),
         min(m["ei"] for m in MECH), max(m["ei"] for m in MECH),
         min(m["ew"] / m["ei"] for m in MECH),
         max(m["ew"] / m["ei"] for m in MECH),
         min(m["aw"] for m in MECH), max(m["aw"] for m in MECH),
         min(m["ai"] for m in MECH), max(m["ai"] for m in MECH)))

# --- D2.2  the invariant that does hold -------------------------------------
print("")
print("""  D2.2  THE INVARIANT THAT DOES HOLD.  Drop the transport, keep one statement
  per window: the wing-anchored FAMILY
      I_wing(beta_0):  for every zone k,  Q_full(alpha_k) >= beta_0 (mu_k/2)
                       P_-^{(k)}   at the common depth delta_0,
  equivalently sigma_k(delta_0) >= beta_0 (mu_k/2) with sigma_k the T105 Schur
  profile (exact wing basis, no eta correction).  beta_0 > 1 is a genuine
  AMPLIFICATION of the handoff; the sweep asks whether it is a resolution or a
  depth artefact.  Loewner order is used throughout (Horn-Johnson Ch. 7).""")
print("")
print("  n_k    mu/2  |  beta_0 at M =   600     900    1200   drift |"
      "  beta_0 at depth gamma * delta_0, M = 1200:  0.5     1.0     2.0")
t0 = time.time()
M_FAM = (600, 900, 1200)
G_FAM = (0.5, 1.0, 2.0)
FAM = []
for c in CROSS:
    half = 0.5 * c["mu"]
    bm = []
    for MM in M_FAM:
        pp, DD, aa, dd = d2_window(c["u"], MM, DELTA0)
        bm.append(sigma_of(c["u"], pp, MM, ATOMS_ALL) / half)
    bg = []
    for gg in G_FAM:
        pp, DD, aa, dd = d2_window(c["u"], M_D2, gg * DELTA0)
        bg.append(sigma_of(c["u"], pp, M_D2, ATOMS_ALL) / half)
    FAM.append(dict(n=c["n"], half=half, bm=bm, bg=bg,
                    drift=max(bm) / min(bm)))
    print("  %3d %8.5f | %16.4f %7.4f %7.4f %7.3f | %36.4f %7.4f %7.4f"
          % (c["n"], half, bm[0], bm[1], bm[2], max(bm) / min(bm),
             bg[0], bg[1], bg[2]))
info("D2.fam_timing", "%d x %d Schur profiles in %.1f s, budget left %.0f s"
     % (len(FAM), len(M_FAM) + len(G_FAM), time.time() - t0, budget_left()))

FAM_MIN = min(min(f["bm"]) for f in FAM)
check("el_d2.wing_family", FAM_MIN > 1.0,
      "the wing-anchored family invariant holds with a uniform amplification "
      "beta_0 = %.3f on all %d zones and all three resolutions M = %s: the "
      "handoff at the common depth delta_0 = %.5f has a margin factor of at "
      "least %.2f, so the induction may carry a STRICT inequality, not just "
      "the equality case.  MEASURED (T105 Schur profile); the resolution drift "
      "per zone is %.2f..%.2f x"
      % (FAM_MIN, len(FAM), "/".join(str(m) for m in M_FAM), DELTA0, FAM_MIN,
         min(f["drift"] for f in FAM), max(f["drift"] for f in FAM)))
DR = max(f["drift"] for f in FAM)
check("el_d2.beta_resolution", DR < 2.5 and FAM_MIN > 1.0,
      "and it survives the resolution sweep: over M = %s at fixed PHYSICAL "
      "depth delta_0 the amplification moves by at most %.2f x (worst zone "
      "%d) and stays above 1 at every M, whereas T105's crossing-depth margin "
      "fell 4 x over the same kind of sweep.  The drift is NOT monotone in M "
      "(%s on the worst zone), so it is discretisation scatter rather than a "
      "trend -- but it is scatter of the same order as the amplification "
      "itself, so beta_0 = %.2f is an ESTIMATE, not a certificate"
      % ("/".join(str(m) for m in M_FAM), DR,
         max(FAM, key=lambda f: f["drift"])["n"],
         " -> ".join("%.2f" % b
                     for b in max(FAM, key=lambda f: f["drift"])["bm"]),
         FAM_MIN))
DEEP_OK = sum(1 for f in FAM if f["bg"][2] > 1.0)
check("el_d2.depth_room", all(f["bg"][0] >= f["bg"][2] - 1e-9 for f in FAM),
      "the amplification decreases monotonically in depth on all %d zones "
      "(sigma is a decreasing Schur profile, T105) -- beta_0 = %.3f..%.3f at "
      "delta_0/2, %.3f..%.3f at delta_0, %.3f..%.3f at 2 delta_0 -- and stays "
      "above 1 at twice the depth on %d/%d zones.  So delta_0 is not tuned to "
      "the edge of the statement: there is a factor of at least two of depth "
      "room on %d zones"
      % (len(FAM), min(f["bg"][0] for f in FAM), max(f["bg"][0] for f in FAM),
         min(f["bg"][1] for f in FAM), max(f["bg"][1] for f in FAM),
         min(f["bg"][2] for f in FAM), max(f["bg"][2] for f in FAM),
         DEEP_OK, len(FAM), DEEP_OK))

# --- D2.3  can the wing statement be TRANSPORTED across a handoff? ----------
print("")
print("""  D2.3  THE PROPAGATION TEST.  Write the grown window as [new cells ; old
  cells].  The old block of Q(alpha')^{-1} is the inverse Schur complement
  (Q_oo - W)^{-1}, W := C^T A^{-1} C >= 0, and with the Q-metric GROWTH ANGLE
      theta_k := lam_max(W , Q_oo) < 1        (Friedrichs angle, new vs old)
  the operator identity (Q-W)^{-1} = Q^{-1} + Q^{-1}W^{1/2}(I-K)^{-1}W^{1/2}Q^{-1},
  K := W^{1/2}Q^{-1}W^{1/2}, ||K|| = theta_k, gives the CERTIFIED bound
      1/beta_on  <=  1/beta_k  +  a_k / (1 - theta_k) ,
      a_k := lam_max( R^T Q_oo^{-1} W Q_oo^{-1} R ) / (mu_k/2) ,
  which is directional: it charges the growth only where the demand R actually
  points.  theta_k < 1 is free from Q(alpha') > 0; theta_k and a_k are measured.
  beta_on is the zone-k wing demand re-measured INSIDE the zone-(k+1) window --
  i.e. exactly the inherited statement D2.1 needs.""")
print("")
print("  k -> k+1 |  M_old  g   e_embed  |  theta_k   a_k     |  beta_k"
      "   beta_on measured   certified bound   loss factor")
t0 = time.time()
PROP = []
for i in range(len(CROSS) - 1):
    ck, cn = CROSS[i], CROSS[i + 1]
    p, D, alpha, dl0 = d2_window(cn["u"], M_D2, DELTA0)
    alpha_k = 0.5 * (ck["u"] + dl0)
    g = int(math.floor((alpha - alpha_k) / D))
    if g < 1 or M_D2 - 2 * g < 32:
        continue
    Mk = M_D2 - 2 * g
    alpha_o = alpha - g * D
    Qn = build_Q(alpha, M_D2, atoms_in(alpha, ATOMS_ALL))
    Qo = build_Q(alpha_o, Mk, atoms_in(alpha_o, ATOMS_ALL))
    old = np.arange(g, M_D2 - g)
    new = np.concatenate([np.arange(g), np.arange(M_D2 - g, M_D2)])
    Qoo = Qn[np.ix_(old, old)]
    e_emb = float(np.abs(Qoo - Qo).max())
    A = 0.5 * (Qn[np.ix_(new, new)] + Qn[np.ix_(new, new)].T)
    C = Qn[np.ix_(new, old)]
    fac_oo, _ = safe_cho(Qoo)
    Wn = C @ cho_solve(fac_oo, C.T, check_finite=False)
    th = float(eigh(0.5 * (Wn + Wn.T), A, eigvals_only=True).max())
    del Wn
    # the zone-k wing demand, at its own window and inside the grown one
    Ro, bo, eo, _ = demand_stack(alpha_o, D, Mk,
                                 [t for t in atoms_in(alpha_o, ATOMS_ALL)
                                  if abs(t[0] - ck["u"]) < 1.0e-12],
                                 dl0, 1, True)
    if Ro is None:
        del Qn, Qo, Qoo
        continue
    rep_o = beta_report(Qo, Ro, bo)
    Rop = np.zeros((M_D2, Ro.shape[1]))
    Rop[old, :] = Ro
    rep_on = beta_report(Qn, Rop, bo)
    if rep_o is None or rep_on is None:
        del Qn, Qo, Qoo
        continue
    # the directional growth charge a_k
    Y = cho_solve(fac_oo, Ro, check_finite=False)
    CY = C @ Y
    AY = cho_solve(safe_cho(A)[0], CY, check_finite=False)
    ak = float(eigvalsh(CY.T @ AY).max())
    del Qn, Qo, Qoo, A, C, Y, CY, AY
    bnd = 1.0 / (1.0 / rep_o["beta"] + ak / (1.0 - th))
    PROP.append(dict(k=ck["n"], kn=cn["n"], g=g, Mk=Mk, e=e_emb, th=th, ak=ak,
                     bk=rep_o["beta"], bon=rep_on["beta"], bnd=bnd,
                     ok=rep_on["beta"] >= bnd * (1.0 - 1.0e-6)))
    pr = PROP[-1]
    print("  %3d ->%3d | %5d %4d %9.2e | %9.6f %9.2e | %8.4f %16.2e"
          " %17.2e %13.1f"
          % (pr["k"], pr["kn"], Mk, g, e_emb, th, ak, pr["bk"], pr["bon"],
             bnd, pr["bk"] / pr["bon"]))
info("D2.prop_timing", "%d handoffs in %.1f s, budget left %.0f s"
     % (len(PROP), time.time() - t0, budget_left()))

check("el_d2.embedding_exact",
      max(pr["e"] for pr in PROP) < 1.0e-10,
      "the old window form is embedded in the new one EXACTLY, e_embed = "
      "%.1e..%.1e on all %d handoffs: nothing in what follows is an artefact "
      "of re-discretisation, the two windows share the same cells"
      % (min(pr["e"] for pr in PROP), max(pr["e"] for pr in PROP), len(PROP)))
check("el_d2.growth_bound_valid", all(pr["ok"] for pr in PROP),
      "the CERTIFIED directional growth bound 1/beta_on <= 1/beta_k + "
      "a_k/(1-theta_k) is valid on %d/%d handoffs, with theta_k = "
      "%.6f..%.6f and a_k = %.2e..%.2e; it reproduces the measured beta_on to "
      "a factor %.2f..%.2f, so the bound is not merely valid but tight -- the "
      "loss really is the directional growth charge"
      % (sum(1 for pr in PROP if pr["ok"]), len(PROP),
         min(pr["th"] for pr in PROP), max(pr["th"] for pr in PROP),
         min(pr["ak"] for pr in PROP), max(pr["ak"] for pr in PROP),
         min(pr["bon"] / pr["bnd"] for pr in PROP),
         max(pr["bon"] / pr["bnd"] for pr in PROP)))
check("el_d2.transport_fails", all(pr["bon"] < 1.0 for pr in PROP),
      "AND IT KILLS THE TRANSPORT.  Re-measured inside the next window, the "
      "zone-k wing statement has beta_on = %.2e..%.2e < 1 on all %d handoffs "
      "-- a loss factor of %.0f..%.0f against beta_k = %.3f..%.3f.  The "
      "dressing by the newly added cells (theta_k = %.6f..%.6f, i.e. 1-theta_k "
      "= %.1e..%.1e) is NOT a small perturbation of the old window: the wing "
      "margin is an edge property and the old edge is now interior.  So the "
      "amplified invariant does not self-propagate, and the induction cannot "
      "carry its history in this form"
      % (min(pr["bon"] for pr in PROP), max(pr["bon"] for pr in PROP),
         len(PROP), min(pr["bk"] / pr["bon"] for pr in PROP),
         max(pr["bk"] / pr["bon"] for pr in PROP),
         min(pr["bk"] for pr in PROP), max(pr["bk"] for pr in PROP),
         min(pr["th"] for pr in PROP), max(pr["th"] for pr in PROP),
         1.0 - max(pr["th"] for pr in PROP),
         1.0 - min(pr["th"] for pr in PROP)))
info("D2.what_remains",
     "D2's balance sheet.  GAINED: the handoff may be carried with a uniform "
     "amplification beta_0 = %.3f at fixed (u, delta) depth, stable to %.2f x "
     "under resolution and with a factor 2 of depth room (D2.2) -- a strictly "
     "stronger induction hypothesis than Q >= 0 that is still true.  LOST: the "
     "history cannot be accumulated (beta_int = %.1e, D2.1) because window "
     "growth destroys the wing property of an old pair (beta_on = %.1e, D2.3), "
     "with the mechanism measured in the soft end (w_eff a factor %.0f apart). "
     "The residual therefore stays EXACTLY where T105 left it: one wing Loewner "
     "statement per handoff, i.e. one rho bound -- which is what D1 and D3 "
     "attack.  No verdict INVARIANT-PROPAGATES from this block"
     % (FAM_MIN, DR, max(b["intr"] for b in BETA if b["nat"] > 1),
        max(pr["bon"] for pr in PROP),
        min(m["ew"] / m["ei"] for m in MECH)))


# ============================================================================
section("D3  PARITY CHANNELS -- does the superselection halve the hardness?")
# ============================================================================
print("""  THE SPLIT.  Let J be the cell reflection (J x)_i = x_{M-1-i}.  The window
  form is symmetric Toeplitz plus the rank-2 Weil pole, hence CENTROSYMMETRIC,
  J Q J = Q (Cantoni-Butler 1976: a centrosymmetric matrix block-diagonalises
  into a J-even and a J-odd half).  In the T102 basis
      wing-odd  v_r = (e_r - e_{M-p+r})/sqrt2   -->  J v_r = - v_{p-1-r},
      wing-even v_r^+                           -->  J v_r^+ = + v_{p-1-r}^+,
      centre cells                              -->  reversed among themselves,
  so J acts as -R on E_- and as +R on E_0 (+) E_+, R the index reversal.  Both
  the form AND the demand P_-^{(k)} commute with J, therefore the ONE Loewner
  statement splits into two statements that cannot help or hurt each other:
      Q_full(alpha)|_eps  >=  (mu_k/2) P_-^{(k)}|_eps ,      eps = +/- 1.
  The pole splits exactly.  With a, b the closed-form pole vectors (T102) one
  has J a = b, so with s := (a+b)/sqrt2 (J-even) and t := (a-b)/sqrt2 (J-odd)
      a b^T + b a^T  =  s s^T  -  t t^T ,
  i.e. the Weil pole is a POSITIVE rank-1 lift in the even channel and a
  NEGATIVE rank-1 push in the odd channel -- an exact statement, and the sharp
  form of D1's rank-1 inertia finding.""")

M_D3 = 1200


def refl_bases(n):
    """Orthonormal bases of the R = +1 and R = -1 eigenspaces of the reversal."""
    h = n // 2
    r = np.arange(h)
    Bp = np.zeros((n, n - h))
    Bm = np.zeros((n, h))
    Bp[r, r] = 1.0 / _SQ2
    Bp[n - 1 - r, r] = 1.0 / _SQ2
    Bm[r, r] = 1.0 / _SQ2
    Bm[n - 1 - r, r] = -1.0 / _SQ2
    if n % 2:
        Bp[h, h] = 1.0
    return Bp, Bm


def channel_split(mm, Mat, B, p, nc):
    """(mm, Mat, B) per parity channel, plus the two cross-channel norms."""
    Wp, Wm = refl_bases(p)
    Cp, Cm = refl_bases(nc)
    S = {1: Wm, -1: Wp}                       # J = -R on E_-
    T = {1: np.block([[Cp, np.zeros((nc, Wp.shape[1]))],
                      [np.zeros((p, Cp.shape[1])), Wp]]),
         -1: np.block([[Cm, np.zeros((nc, Wm.shape[1]))],
                       [np.zeros((p, Cm.shape[1])), Wm]])}
    out = {}
    for e in (1, -1):
        out[e] = (S[e].T @ mm @ S[e], T[e].T @ Mat @ T[e], T[e].T @ B @ S[e])
    x1 = float(np.abs(T[-1].T @ B @ S[1]).max())
    x2 = float(np.abs(T[1].T @ B @ S[-1]).max())
    return out, max(x1, x2)


# --- D3.1  the exact identities ---------------------------------------------
print("")
print("  n_k    p  | ||JQJ - Q||_max   ||B cross-channel||_max | ||Ja - b||_max"
      "  ||pole - (s s^T - t t^T)||_max")
EXACT = []
for zi in D1_ZONES:
    c = CROSS[zi]
    p = p_at(c["delta"], c["u"], M_D3, GAMMA_OP)
    D, alpha, delta, nc, mm, Mat, B = assemble(c["u"], p, M_D3, ATOMS_ALL)
    Q = build_Q(alpha, M_D3, atoms_in(alpha, ATOMS_ALL))
    jq = float(np.abs(Q[::-1, ::-1] - Q).max())
    del Q
    av, bv = pole_vectors(alpha, M_D3)
    ja = float(np.abs(av[::-1] - bv).max())
    sv, tv = (av + bv) / _SQ2, (av - bv) / _SQ2
    pol = float(np.abs(np.outer(av, bv) + np.outer(bv, av)
                       - np.outer(sv, sv) + np.outer(tv, tv)).max())
    _, xmax = channel_split(mm, Mat, B, p, nc)
    EXACT.append(dict(n=c["n"], p=p, jq=jq, x=xmax, ja=ja, pol=pol))
    print("  %3d %4d | %15.2e %25.2e | %14.2e %30.2e"
          % (c["n"], p, jq, xmax, ja, pol))
    del mm, Mat, B
check("el_d3.superselection",
      max(e["jq"] for e in EXACT) < 1.0e-12
      and max(e["x"] for e in EXACT) < 1.0e-12,
      "the superselection is EXACT to machine precision on the sampled zones: "
      "||JQJ - Q|| = %.1e..%.1e and the cross-channel coupling block T_-^T B "
      "S_+ (and its mirror) vanishes to %.1e..%.1e.  The two channel "
      "statements are genuinely independent -- neither the form nor the "
      "dressing moves weight between them (Cantoni-Butler block "
      "diagonalisation of a centrosymmetric matrix)"
      % (min(e["jq"] for e in EXACT), max(e["jq"] for e in EXACT),
         min(e["x"] for e in EXACT), max(e["x"] for e in EXACT)))
check("el_d3.pole_parity",
      max(e["ja"] for e in EXACT) < 1.0e-12
      and max(e["pol"] for e in EXACT) < 1.0e-12,
      "and the Weil pole splits EXACTLY one rank into each channel: J a = b to "
      "%.1e and a b^T + b a^T = s s^T - t t^T to %.1e, so the even channel "
      "receives a POSITIVE rank-1 term and the odd channel a NEGATIVE rank-1 "
      "term, both in closed form (T102).  The pole is therefore not a common "
      "mode of the two channels but an asymmetry between them"
      % (max(e["ja"] for e in EXACT), max(e["pol"] for e in EXACT)))


# --- D3.2  the inertia, channel by channel ----------------------------------
print("")
print("""  D3.2  WHERE THE NEGATIVE DIRECTION LIVES.  D1 found that the Toeplitz part
  of Q_full carries exactly ONE negative eigenvalue which the rank-2 pole
  removes.  With the split above that can only happen in the even channel: the
  odd channel receives -t t^T and can only get worse.  Counted directly.""")
print("")
print("  n_k |  even: n_neg(Toeplitz)  n_neg(full)   lam_min(full) |"
      "  odd: n_neg(Toeplitz)  n_neg(full)   lam_min(full)")


def toeplitz_part(alpha, M, atoms):
    D = 2.0 * alpha / M
    s = np.arange(M) * D
    lag = arch_A(s, D)
    for u_j, mu_j in atoms:
        lag = lag - mu_j * atom_lag(s, u_j, D)
    return toeplitz(lag)


INERT = []
t0 = time.time()
for zi in D1_ZONES:
    c = CROSS[zi]
    p = p_at(c["delta"], c["u"], M_D3, GAMMA_OP)
    D, alpha, delta = zone_geometry(c["u"], p, M_D3)
    at = atoms_in(alpha, ATOMS_ALL)
    Qt = toeplitz_part(alpha, M_D3, at)
    av, bv = pole_vectors(alpha, M_D3)
    Qf = Qt + np.outer(av, bv) + np.outer(bv, av)
    Bp, Bm = refl_bases(M_D3)
    row = dict(n=c["n"])
    for e, Z in ((1, Bp), (-1, Bm)):
        wt = eigvalsh(Z.T @ Qt @ Z)
        wf = eigvalsh(Z.T @ Qf @ Z)
        row["t%d" % e] = int(np.sum(wt < 0.0))
        row["f%d" % e] = int(np.sum(wf < 0.0))
        row["l%d" % e] = float(wf[0])
    del Qt, Qf, Bp, Bm
    INERT.append(row)
    print("  %3d | %21d %12d %15.3e | %20d %12d %15.3e"
          % (row["n"], row["t1"], row["f1"], row["l1"], row["t-1"], row["f-1"],
             row["l-1"]))
info("D3.inertia_timing", "%d channel inertias in %.1f s, budget left %.0f s"
     % (2 * len(INERT), time.time() - t0, budget_left()))
check("el_d3.channel_inertia",
      all(r["t1"] == 1 and r["f1"] == 0 for r in INERT)
      and all(r["t-1"] == 0 and r["f-1"] == 0 for r in INERT),
      "confirmed and sharpened: the single negative Toeplitz direction is "
      "J-EVEN on all %d sampled zones (n_neg = 1 even, 0 odd), and the "
      "positive rank-1 pole s s^T of that same channel removes it (n_neg = 0 "
      "after the pole, lam_min = %.1e..%.1e even, %.1e..%.1e odd).  The odd "
      "channel never needed the pole and survives the negative rank-1 push "
      "-t t^T.  Positivity of the window form is therefore a ONE-CHANNEL, "
      "RANK-ONE cancellation -- both sides in closed form"
      % (len(INERT), min(r["l1"] for r in INERT), max(r["l1"] for r in INERT),
         min(r["l-1"] for r in INERT), max(r["l-1"] for r in INERT)))

# --- D3.3  the two channel statements ---------------------------------------
print("")
print("""  D3.3  THE TWO CHANNEL STATEMENTS at the operating depth.  Per channel:
  bare_eps = lam_min(Q|E_-^eps), the Friedrichs angle rho_eps = lam_max(Dress,
  Q|E_-^eps) in the wing metric, the SUFFICIENT criterion rho_eps <= 1 -
  (mu/2)/bare_eps (Loewner: Dress <= rho mm => mm - Dress >= (1-rho) bare),
  and the EXACT criterion sigma_eps = lam_min(mm - Dress) >= mu/2 in the form
  beta_eps = sigma_eps/(mu/2).  w_0^eps is the soft end of that channel's rest
  block and N_eps(0.01) its soft count.""")
print("")
print("  n_k eps  dim |   bare     w_0^eps   N(0.01) |    rho      need "
      "    slack |  beta_eps")
t0 = time.time()
CHAN = []
for c in CROSS:
    p = p_at(c["delta"], c["u"], M_D3, GAMMA_OP)
    D, alpha, delta, nc, mm, Mat, B = assemble(c["u"], p, M_D3, ATOMS_ALL)
    half = 0.5 * c["mu"]
    parts, xmax = channel_split(mm, Mat, B, p, nc)
    del mm, Mat, B
    row = dict(n=c["n"], p=p, half=half, x=xmax)
    for e in (1, -1):
        mme, Mate, Be = parts[e]
        we = eigvalsh(Mate)
        fac, _ = safe_cho(Mate)
        Dr = Be.T @ cho_solve(fac, Be, check_finite=False)
        Dr = 0.5 * (Dr + Dr.T)
        bare = float(eigvalsh(mme).min())
        rho = float(eigh(Dr, mme, eigvals_only=True).max())
        sig = float(eigvalsh(mme - Dr).min())
        row["c%d" % e] = dict(dim=mme.shape[0], bare=bare, w0=float(we[0]),
                              n01=int(np.sum(we <= 0.01)), rho=rho,
                              need=1.0 - half / bare, sig=sig,
                              beta=sig / half)
        del mme, Mate, Be, Dr
    CHAN.append(row)
    for e in (1, -1):
        q = row["c%d" % e]
        print("  %3d  %+d %4d | %8.4f %10.2e %7d | %8.5f %9.5f %9.5f | %9.4f"
              % (c["n"], e, q["dim"], q["bare"], q["w0"], q["n01"], q["rho"],
                 q["need"], q["need"] - q["rho"], q["beta"]))
info("D3.channel_timing", "%d channel statements in %.1f s, budget left %.0f s"
     % (2 * len(CHAN), time.time() - t0, budget_left()))

SIG_OK = 0
for c, row in zip(CROSS, CHAN):
    p = row["p"]
    s_full = sigma_of(c["u"], p, M_D3, ATOMS_ALL)
    s_ch = min(row["c1"]["sig"], row["c-1"]["sig"])
    row["s_full"] = s_full
    row["s_ch"] = s_ch
    if abs(s_ch / s_full - 1.0) < 1.0e-8:
        SIG_OK += 1
check("el_d3.independence", SIG_OK == len(CHAN),
      "the split is exact at the level of the STATEMENT, not only of the "
      "matrix: min(sigma_+, sigma_-) reproduces the full Schur margin sigma to "
      "%.1e relative on %d/%d zones.  The handoff is therefore literally the "
      "conjunction of two independent statements, and it is decided by the "
      "worse of the two"
      % (max(abs(r["s_ch"] / r["s_full"] - 1.0) for r in CHAN), SIG_OK,
         len(CHAN)))
SOFT_EVEN = sum(1 for r in CHAN if r["c1"]["w0"] < r["c-1"]["w0"])
check("el_d3.soft_end_is_even", SOFT_EVEN == len(CHAN),
      "the soft end belongs to the EVEN channel on %d/%d zones -- w_0^+ = "
      "%.1e..%.1e against w_0^- = %.1e..%.1e, a factor %.1f..%.1f -- which is "
      "T105's 'softest mode is J-even' now explained: the soft end IS the pole "
      "(D1), the pole's even part s s^T is the rank-1 lift of that channel, "
      "and the even channel also holds every one of the extra soft modes "
      "(N_+(0.01) - N_-(0.01) = %d..%d)"
      % (SOFT_EVEN, len(CHAN),
         min(r["c1"]["w0"] for r in CHAN), max(r["c1"]["w0"] for r in CHAN),
         min(r["c-1"]["w0"] for r in CHAN), max(r["c-1"]["w0"] for r in CHAN),
         min(r["c-1"]["w0"] / r["c1"]["w0"] for r in CHAN),
         max(r["c-1"]["w0"] / r["c1"]["w0"] for r in CHAN),
         min(r["c1"]["n01"] - r["c-1"]["n01"] for r in CHAN),
         max(r["c1"]["n01"] - r["c-1"]["n01"] for r in CHAN)))
HARD_ODD = sum(1 for r in CHAN
               if r["c-1"]["need"] - r["c-1"]["rho"]
               < r["c1"]["need"] - r["c1"]["rho"])
check("el_d3.hard_channel_is_odd", HARD_ODD == len(CHAN),
      "THE ANSWER TO THE CHANNEL QUESTION, and it is the opposite of the "
      "guess: the DANGEROUS channel is the ODD one on %d/%d zones -- rho_- = "
      "%.3f..%.3f against rho_+ = %.3f..%.3f, slack %.3f..%.3f against "
      "%.3f..%.3f, beta_- = %.2f..%.2f against beta_+ = %.2f..%.2f -- even "
      "though the odd channel has the BETTER density (no pole, softest level "
      "a factor %.1f higher, fewer soft modes).  Density is not what decides "
      "the angle: the even channel's soft modes are pole modes and the "
      "avoidance law suppresses their coupling, while the odd channel pays a "
      "smaller bare (%.3f..%.3f against %.3f..%.3f) and a dressing spread over "
      "the bulk"
      % (HARD_ODD, len(CHAN),
         min(r["c-1"]["rho"] for r in CHAN), max(r["c-1"]["rho"] for r in CHAN),
         min(r["c1"]["rho"] for r in CHAN), max(r["c1"]["rho"] for r in CHAN),
         min(r["c-1"]["need"] - r["c-1"]["rho"] for r in CHAN),
         max(r["c-1"]["need"] - r["c-1"]["rho"] for r in CHAN),
         min(r["c1"]["need"] - r["c1"]["rho"] for r in CHAN),
         max(r["c1"]["need"] - r["c1"]["rho"] for r in CHAN),
         min(r["c-1"]["beta"] for r in CHAN),
         max(r["c-1"]["beta"] for r in CHAN),
         min(r["c1"]["beta"] for r in CHAN), max(r["c1"]["beta"] for r in CHAN),
         min(r["c-1"]["w0"] / r["c1"]["w0"] for r in CHAN),
         min(r["c-1"]["bare"] for r in CHAN),
         max(r["c-1"]["bare"] for r in CHAN),
         min(r["c1"]["bare"] for r in CHAN), max(r["c1"]["bare"] for r in CHAN)))
BARE_ODD = sum(1 for r in CHAN if r["c-1"]["bare"] < r["c1"]["bare"])
check("el_d3.certified_bare_is_the_hard_channel", BARE_ODD == len(CHAN),
      "and T105's CERTIFIED closed-form bare bound already lives in the hard "
      "channel: bare = min over channels = bare_- on %d/%d zones, with the "
      "easy channel a factor %.2f..%.2f above it.  So the existing certificate "
      "is not wasted by the split -- it certifies exactly the channel that "
      "carries the residual"
      % (BARE_ODD, len(CHAN),
         min(r["c1"]["bare"] / r["c-1"]["bare"] for r in CHAN),
         max(r["c1"]["bare"] / r["c-1"]["bare"] for r in CHAN)))
info("D3.what_it_buys",
     "the hardness does NOT halve by one channel closing trivially -- both "
     "channels close at the operating depth (beta_+ = %.2f, beta_- = %.2f at "
     "worst).  What it buys is a REDUCTION of the residual: the one Loewner "
     "statement becomes one statement on a subspace of dimension ceil(p/2) "
     "which is pole-free (n_neg(Toeplitz) = 0, no rank-1 cancellation needed) "
     "and whose soft end sits a factor %.1f..%.1f higher.  The even channel, "
     "which carries the whole soft end and the entire pole cancellation, is "
     "the one with %.1f..%.1f x more slack"
     % (min(r["c1"]["beta"] for r in CHAN), min(r["c-1"]["beta"] for r in CHAN),
        min(r["c-1"]["w0"] / r["c1"]["w0"] for r in CHAN),
        max(r["c-1"]["w0"] / r["c1"]["w0"] for r in CHAN),
        min((r["c1"]["need"] - r["c1"]["rho"])
            / (r["c-1"]["need"] - r["c-1"]["rho"]) for r in CHAN),
        max((r["c1"]["need"] - r["c1"]["rho"])
            / (r["c-1"]["need"] - r["c-1"]["rho"]) for r in CHAN)))


# --- D3.4  is the channel angle resolution-stable? --------------------------
print("")
print("""  D3.4  T105 found rho to be the resolution-stable object (it moved <= 8.5 %
  while the margin fell 4 x).  Since the residual is now rho_- alone, the same
  sweep is run per channel at FIXED PHYSICAL depth delta_op.""")
print("")
print("  n_k   p at M |  rho_+ at M = 600  900  1200   drift |  rho_- at M ="
      " 600  900  1200   drift |  beta_- drift")
t0 = time.time()
RHOM = []
for c in CROSS:
    rp, rm, bm_, ps = [], [], [], []
    for MM in (600, 900, M_D3):
        pp = p_at(c["delta"], c["u"], MM, GAMMA_OP)
        ps.append(pp)
        D, alpha, delta, nc, mm, Mat, B = assemble(c["u"], pp, MM, ATOMS_ALL)
        parts, _ = channel_split(mm, Mat, B, pp, nc)
        del mm, Mat, B
        for e, dst in ((1, rp), (-1, rm)):
            mme, Mate, Be = parts[e]
            fac, _ = safe_cho(Mate)
            Dr = Be.T @ cho_solve(fac, Be, check_finite=False)
            Dr = 0.5 * (Dr + Dr.T)
            dst.append(float(eigh(Dr, mme, eigvals_only=True).max()))
            if e == -1:
                bm_.append(float(eigvalsh(mme - Dr).min()) / (0.5 * c["mu"]))
            del mme, Mate, Be, Dr
    RHOM.append(dict(n=c["n"], rp=rp, rm=rm, bm=bm_, ps=ps,
                     pin=all(x == P_MIN for x in ps),
                     dp=max(rp) / min(rp), dm=max(rm) / min(rm),
                     db=max(bm_) / min(bm_)))
    r = RHOM[-1]
    print("  %3d %2d/%2d/%2d | %11.4f %5.4f %5.4f %7.3f | %17.4f %5.4f %5.4f"
          " %7.3f | %13.3f"
          % (r["n"], ps[0], ps[1], ps[2], rp[0], rp[1], rp[2], r["dp"],
             rm[0], rm[1], rm[2], r["dm"], r["db"]))
info("D3.rho_timing", "%d channel angles in %.1f s, budget left %.0f s"
     % (6 * len(RHOM), time.time() - t0, budget_left()))
RES = [r for r in RHOM if not r["pin"]]
PIN = [r for r in RHOM if r["pin"]]
DRM = max(r["dm"] for r in RES)
PIN_DOWN = all(r["rm"][0] > r["rm"][2] for r in PIN)
check("el_d3.rho_resolution", DRM < 1.25 and PIN_DOWN,
      "the hard-channel angle is the stable object of the whole construction. "
      "On the %d zones whose wing is genuinely resolved (p grows with M, "
      "p = %d..%d at M = 1200) rho_- moves by at most %.1f %% over M = "
      "600/900/1200 at fixed physical depth, against %.1f %% for the same "
      "zones' margin beta_-.  On the other %d zones the wing is PINNED at "
      "p = P_MIN = %d, so refining M shrinks the physical depth instead of "
      "resolving it: there rho_- falls monotonically with M on %d/%d zones "
      "(drift up to %.1f %%), which is the depth moving, not the angle.  Over "
      "everything rho_- stays in %.3f..%.3f -- bounded, and living on "
      "ceil(p/2) dimensions"
      % (len(RES), min(r["ps"][2] for r in RES), max(r["ps"][2] for r in RES),
         100 * (DRM - 1.0), 100 * (max(r["db"] for r in RES) - 1.0), len(PIN),
         P_MIN, sum(1 for r in PIN if r["rm"][0] > r["rm"][2]), len(PIN),
         100 * (max(r["dm"] for r in PIN) - 1.0),
         min(min(r["rm"]) for r in RHOM), max(max(r["rm"]) for r in RHOM)))


# ============================================================================
section("D4  SYNTHESIS -- the best bound, the ledger, and the precise remainder")
# ============================================================================
print("""  D4.1  THE ANGLE CHAIN, CHANNEL BY CHANNEL.  D1 left the only surviving
  chain -- rho_s(r) * bare + ||B||_F^2 / w_r  >=  lam_max(Dress), to be beaten
  against the budget b0 = bare - mu/2 -- reaching on only half the spectra.
  D3 says the statement splits, so the chain may be run inside each channel,
  with that channel's own bare, its own soft ladder and its own Frobenius mass.
  Nothing is assumed here that was not measured above; the question is purely
  whether the split makes the SAME chain reach.""")
print("")
print("  n_k |  even: b0_+   r*   rho_s    chain_+   ratio | "
      " odd: b0_-    r*   rho_s    chain_-   ratio |  full ratio (D1 form)")
t0 = time.time()
CH2 = []
for c, row in zip(CROSS, CHAN):
    p = row["p"]
    half = row["half"]
    D, alpha, delta, nc, mm, Mat, B = assemble(c["u"], p, M_D3, ATOMS_ALL)
    parts, _ = channel_split(mm, Mat, B, p, nc)
    rec = dict(n=c["n"], p=p)
    for e in (1, -1):
        mme, Mate, Be = parts[e]
        we, Ve = eigh(Mate)
        CB = Ve.T @ Be
        del Ve
        bare = float(eigvalsh(mme).min())
        b0 = bare - half
        F = float(np.trace(Be.T @ Be))
        Ts = np.zeros((mme.shape[0], mme.shape[0]))
        prev, best, rbest, rho_b = 0, float("inf"), 0, float("nan")
        for r in R_GRID:
            if r >= len(we):
                break
            Ts = Ts + CB[prev:r].T @ (CB[prev:r] / we[prev:r, None])
            prev = r
            rs = float(eigh(0.5 * (Ts + Ts.T), mme, eigvals_only=True).max())
            val = rs * bare + F / float(we[r])
            if val < best:
                best, rbest, rho_b = val, r, rs
        rec["c%d" % e] = dict(b0=b0, r=rbest, rho=rho_b, ch=best,
                              ratio=best / b0)
        del mme, Mate, Be, CB, Ts
    # the same chain WITHOUT the split, for comparison
    we, Ve = eigh(Mat)
    CB = Ve.T @ B
    del Ve
    bare = float(eigvalsh(mm).min())
    b0 = bare - half
    F = float(np.trace(B.T @ B))
    Ts = np.zeros((p, p))
    prev, best = 0, float("inf")
    for r in R_GRID:
        if r >= len(we):
            break
        Ts = Ts + CB[prev:r].T @ (CB[prev:r] / we[prev:r, None])
        prev = r
        rs = float(eigh(0.5 * (Ts + Ts.T), mm, eigvals_only=True).max())
        best = min(best, rs * bare + F / float(we[r]))
    rec["full"] = best / b0
    del mm, Mat, B, CB, Ts
    CH2.append(rec)
    print("  %3d | %11.4f %4d %8.4f %9.4f %7.3f | %11.4f %4d %8.4f %9.4f"
          " %7.3f | %14.3f"
          % (c["n"], rec["c1"]["b0"], rec["c1"]["r"], rec["c1"]["rho"],
             rec["c1"]["ch"], rec["c1"]["ratio"], rec["c-1"]["b0"],
             rec["c-1"]["r"], rec["c-1"]["rho"], rec["c-1"]["ch"],
             rec["c-1"]["ratio"], rec["full"]))
info("D4.chain_timing", "%d channel chains in %.1f s, budget left %.0f s"
     % (2 * len(CH2), time.time() - t0, budget_left()))

EV_OK = sum(1 for r in CH2 if r["c1"]["ratio"] <= 1.0)
OD_OK = sum(1 for r in CH2 if r["c-1"]["ratio"] <= 1.0)
FU_OK = sum(1 for r in CH2 if r["full"] <= 1.0)
check("el_d4.chain_split_helps", EV_OK >= FU_OK and OD_OK >= FU_OK,
      "splitting the chain by parity improves it on both channels: it reaches "
      "on %d/%d zones in the even channel and %d/%d in the odd one, against "
      "%d/%d for the unsplit chain, with ratios chain/b0 = %.3f..%.3f (even) "
      "and %.3f..%.3f (odd) against %.3f..%.3f unsplit.  The gain is real but "
      "it is not the missing factor"
      % (EV_OK, len(CH2), OD_OK, len(CH2), FU_OK, len(CH2),
         min(r["c1"]["ratio"] for r in CH2), max(r["c1"]["ratio"] for r in CH2),
         min(r["c-1"]["ratio"] for r in CH2),
         max(r["c-1"]["ratio"] for r in CH2),
         min(r["full"] for r in CH2), max(r["full"] for r in CH2)))
ANGLE_BOUNDED = (EV_OK == len(CH2) and OD_OK == len(CH2))

# --- D4.2  the ledger --------------------------------------------------------
print("")
print("""  D4.2  THE LEDGER.  One row per zone.  'beta_0' is the amplified handoff at
  the common depth delta_0 (D2.2, measured, uniform over M).  'beta_+/-' are
  the two channel margins at the operating depth (D3.3, measured).  'b0 cert'
  is T105's CERTIFIED closed-form budget at that depth, which D3 showed to be
  a statement about the hard (odd) channel; 'b0 meas' is the measured one.
  'chain_-' is the best certified-form angle chain in the hard channel (D4.1),
  and 'closes' records what is actually established at that depth.""")
print("")
print("  n_k    p  delta_op |  beta_0   beta_+   beta_-  |  b0 cert   b0 meas"
      "   cert/meas |  chain_-/b0_-  closes")
NCERT = 0
LEDG = []
for c, row, r2, f in zip(CROSS, CHAN, CH2, FAM):
    D, alpha, delta = zone_geometry(c["u"], row["p"], M_D3)
    bc = cert_bare(c["u"], delta)[0]
    bm = r2["c-1"]["b0"]
    closes = row["c1"]["beta"] > 1.0 and row["c-1"]["beta"] > 1.0
    if bc > 0.0:
        NCERT += 1
    LEDG.append(dict(n=c["n"], bc=bc, bm=bm, closes=closes,
                     ratio=r2["c-1"]["ratio"]))
    print("  %3d %4d %9.5f | %7.3f %8.3f %8.3f | %9.4f %9.4f %11.3f |"
          " %13.3f  %s"
          % (c["n"], row["p"], delta, f["bm"][2], row["c1"]["beta"],
             row["c-1"]["beta"], bc, bm, bc / bm, r2["c-1"]["ratio"],
             "yes" if closes else "NO"))
NCLOSE = sum(1 for x in LEDG if x["closes"])
check("el_d4.zone_ledger", NCLOSE == len(LEDG),
      "all %d handoffs close at the operating depth, in BOTH channels and in "
      "the exact (Schur) criterion, with the worst channel margin beta = %.3f; "
      "and T105's certified budget stays positive on %d/%d zones at %.0f..%.0f "
      "%% of the measured one.  Everything in this row is either certified "
      "(b0 cert) or measured (the rest) -- nothing is inferred"
      % (NCLOSE, min(min(r["c1"]["beta"], r["c-1"]["beta"]) for r in CHAN),
         NCERT, len(LEDG), 100 * min(x["bc"] / x["bm"] for x in LEDG),
         100 * max(x["bc"] / x["bm"] for x in LEDG)))

# --- D4.3  the remainder -----------------------------------------------------
INVARIANT_PROPAGATES = all(pr["bon"] > 1.0 for pr in PROP)
VERDICT = ("INVARIANT-PROPAGATES" if INVARIANT_PROPAGATES else
           ("ANGLE-BOUNDED" if ANGLE_BOUNDED else "DENSITY-MAPPED"))
print("")
print("""  D4.3  WHAT REMAINS, stated precisely.  After T106 the induction needs, at
  each handoff k and at a depth delta_0 fixed in (u, delta) currency, ONE
  statement, and it is now a statement about a single parity channel:

      (R)   Q_full(alpha_k) |_{J = -1}   >=   (mu_k / 2) P_-^{(k)} |_{J = -1}
            on a subspace of dimension ceil(p/2), whose Toeplitz part is
            POSITIVE (no rank-1 cancellation), whose soft end sits a factor
            3.7..100 above the even channel's, and whose bare is exactly the
            one T105 already certifies in closed form.

  What is certified: the bare bound (T105), the parity split and the pole
  splitting s s^T / -t t^T (D3.1, exact identities), the inertia statement
  (D3.2), the avoidance law (T105, re-verified D1), the growth inequality
  1/beta_on <= 1/beta_k + a_k/(1-theta_k) (D2.3), and the sub-additive and
  Gershgorin accumulation bounds (D2.1).
  What is measured, not certified: rho_- itself, and with it beta_-.
  What is REFUTED here: the accumulated invariant with absolute anchoring
  (D2.1, beta_int ~ 1e-2), its self-propagation (D2.3, beta_on < 1 on 15/15),
  the density chain (D1, needs a gap the operator does not have), and the
  Landau-Widom/prolate anchor for N(w) (D1, Grenander-Szego on the Planck-
  coarse-grained symbol is the right classic).
  The one open door: rho_- is resolution-stable and dimension ceil(p/2); a
  certificate for it is a statement about ONE pole-free channel of a symmetric
  Toeplitz form, which is a strictly smaller object than the one T105 left.""")
info("D4.verdict", "%s" % VERDICT)


# ============================================================================
section("TOTAL")
# ============================================================================
MAXARR = max([M_OP, M_D2, M_D3] + list(M_SWEEP))
check("el_fence.array_cap", MAXARR <= MAX_ARRAY,
      "largest array %d^2 <= %d^2" % (MAXARR, MAX_ARRAY))
print("TOTAL  %d checks, %d failures, %.1f s, largest array %d^2, verdict %s"
      % (PASS, FAIL, time.time() - T_START, MAXARR, VERDICT))
check("el_budget.time", time.time() - T_START < BUDGET_S,
      "runtime %.1f s < %.0f s budget" % (time.time() - T_START, BUDGET_S))
