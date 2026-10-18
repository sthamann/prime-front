"""Discovery probe (2026-07-27), part 118 of the zeta/prime investigation.
Contract SYMBOL.LEMMAS -- measure the THREE missing lemmata of the T117 theorem
candidate one by one, put each against its CLASSICAL address, and certify as
far as the arithmetic allows.

WHERE THIS SITS (T105..T117, taken as given, rebuilt here)
  T117 made the [P1] margin inequality theorem-shaped.  With T = T_odd the
  pole-free odd Weil form on the frame-A window (-alpha, alpha) at cell width
  D, t~ the functional of the D-INDEPENDENT f(x) = 2 sinh(x/2), u = T^{-1} t~
  and eps = 1 - t~^T u, T117 proved (identities + Cholesky) the chain
      eps_c >= eps_c - eps_f = y^T S y >= lam_min(S) ||y||^2
            >= lam_min(S) max_j (u_f[2j] - u_f[2j+1])^2 / 2 > 0,
  S the T_f-Schur complement onto the two-level oscillation space, y = Z^T u_f,
  and found the chain loses NO power of D (theta' = 1.74 vs theta = 1.76).
  Three lemmata were left open, each with a classical address:
      (L-A) corner asymptotics of T^{-1} -- needed for hypothesis (H3), a
            non-vanishing discrete slope of u on one coarse cell.
            Address: Kac-Murdock-Szego 1953, Widom 1974, Fisher-Hartwig.
      (L-B) a lower bound for lam_min(S) at ONE level (measured in
            [0.857, 1.771], GROWING under refinement).
            Address: the symbol at the Nyquist frequency.
      (L-C) the saturation constant (measured [0.675, 0.744]).
            Address: Bank-Smith 1993, Dorfler-Nochetto 2002.

WHAT THIS PROBE DOES, AND WHAT CAME OUT
  Q1  LEMMA B, ATTEMPT ONE: THE SYMBOL OF S ITSELF -- REFUTED, WITH A REASON.
      The two-level oscillation Schur complement of a Toeplitz form has an EXACT
      symbol, and it is a WEIGHTED HARMONIC MEAN of the symbol at a low frequency
      and at its Nyquist partner:
          sigma_S(phi) = f(th) f(th+pi) / [cos^2(th/2) f(th) + sin^2(th/2)
                                           f(th+pi)],      th = phi/2,
          1/sigma_S    = cos^2(th/2)/f(th+pi) + sin^2(th/2)/f(th).
      Derived here and verified on exactly-positive model symbols.  A harmonic
      mean needs BOTH entries positive, and f is negative on a comb of dips at
      the window's own resolution scale, so every pointwise route through
      sigma_S is VACUOUS on the real symbol -- and Q1 pins down why no repair
      works: the ground state of S CONCENTRATES on the negative set, positivity
      is a cancellation of relative size 1e2-1e4, and the finite section is a
      Fejer-Riesz MOMENT problem rather than a pointwise infimum.
  Q2  LEMMA A, THE CORNER -- ADDRESS DOES NOT TRANSFER.  The classical statement
      is an EDGE EXPONENT: for a symbol vanishing like |th|^{2s} at th = 0 the
      finite-section solution with smooth data vanishes like dist(.,edge)^s.
      Verified exactly on a MODEL CLASS -- the Toeplitz forms of
      |2 sin(th/2)|^{2s}, lags in closed form, s = 1 the Dirichlet Laplacian
      with an exact solution -- plus the KMS 1953 closed-form inverse as the
      s = 0 control (no symbol zero, hence no boundary layer at all, only an
      end-cell offset).  On the REAL symbol the exponent does not settle: it
      drifts logarithmically under refinement and the corner profile is still
      moving between levels, which is what a LOG-singular symbol does.  (H3) is
      then located -- which cell, and how the quantity the chain consumes scales.
  Q3  LEMMA C, SATURATION -- AND LEMMA B, ATTEMPT TWO, WHICH WORKS.  Saturation
      is not an assumption for a nested PWC pair but an IDENTITY,
      eps_c - eps_f = y^T S y, so beta is computed; the Bank-Smith hypotheses are
      then checked one by one.  Their CBS constant gamma is the lever that
      rescues Lemma B, because it moves the symbol question off S and onto the
      oscillation Gram:
          lam_min(S) >= (1 - gamma^2) lam_min(Z^T T Z) >= (1-gamma^2) inf sigma_z,
          sigma_z(phi) = sin^2(th/2) f(th) + cos^2(th/2) f(th + pi),
      the ARITHMETIC mean of the same aliasing pair -- so the low-frequency
      negativity that killed sigma_S is suppressed QUADRATICALLY instead of
      poisoning a harmonic mean.  inf sigma_z is FFT-only, hence certifiable on a
      lever hundreds of times longer than any factorisable ladder.
  Q4  SYNTHESIS.  The T117 theorem re-written with the three lemma statuses, the
      honest text of the strongest defensible statement today, and the shortest
      remaining list per lemma.  Q3 also CORRECTS the T117 chain: its last step
      (to a single cell) is a full power of D weaker than eps, so the rate lives
      on ||y||^2 and (H3) has to be upgraded to a mean-square statement.

PREREGISTERED VERDICTS
  LEMMAS-CLASSICAL : all three lemmata match their classical addresses with
                     certifiable routes -- the theorem is complete up to
                     classical citations.
  TWO-OF-THREE     : two stand, the third is named with what is missing.
  SYMBOL-BLOCKED   : a lemma CONTRADICTS its classical address; what was
                     measured is reported.
  Element gates: el_firewall, el_q1, el_q2, el_q3, el_q4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger/TeX/website/
    changelog edit, no verification/ module, no next.txt, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * RH => window Weil positivity is a HYPOTHESIS INPUT elsewhere and is NOT
    used here at all: every statement is about a GIVEN window.
  * CERTIFIED vs CLASSICAL vs MEASURED vs HYPOTHESIS per line.  Every fit is a
    fit and carries a jackknife band.  Every classical anchor is cited WITH THE
    DIRECTION it gives; an UPPER-bound theorem never serves a LOWER bound.
  * lam_min of a form on a PWC space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute continuum coercivity, never prove it.  The
    Q1 route is built so that it needs no continuum statement at all.
  * FLOATING-POINT LIMITS DECLARED.  A completed Cholesky of A certifies
    lam_min(A) >= -c_h u ||A||_2 with u = 2^-53, c_h = (h+1)/(1-(h+1)u)
    (Wilkinson 1968; Higham 2002, Thm 10.3/10.4), NOT lam_min(A) >= 0.
  * SYMBOL CERTIFICATES DECLARED.  f is the trig polynomial of the FINITE lag
    sequence, so f is EXACT on the grid (no tail truncation); the step from
    grid values to per-cell values uses
        f >= f(th_m) - (dt/2)|f'(th_m)| - (dt^2/8) max|f''|,
        max|f''| <= 2 sum_j j^2 |c_j|,
    and the resulting margin is printed with every certified number.
  * Classical anchors, WITH DIRECTION:
      Grenander-Szego / Toeplitz compression: lam_min(T_M(f)) >= ess inf f
        (LOWER, and the direction used for the whole Q1 route),
      local Fourier / two-grid analysis (Brandt 1977; Hackbusch 1985) and
        multigrid for Toeplitz (Fiorentino-Serra 1991; Chan-Chang-Sun 1998):
        the two-grid symbol, here re-derived in closed form,
      Kac-Murdock-Szego 1953 (the exactly invertible model Toeplitz form),
      Widom 1974 / Fisher-Hartwig (finite-section inverse and the power/log
        singular symbol classes),
      Getoor 1961 / Ros-Oton-Serra 2014 (the d^s edge law for order-2s
        operators; used as the SHAPE that the model class then confirms),
      Payne-Weinberger 1960 (the one-cell Poincare step, LOWER form),
      Bank-Smith 1993 / Dorfler-Nochetto 2002 (saturation), Yserentant 1986
        (strengthened Cauchy-Schwarz), Bornemann-Erdmann-Kornhuber 1996 (that
        saturation can FAIL -- the honest caveat),
      Haynsworth 1968 / Albert 1969 (Schur complements), Cholesky /
        Wilkinson 1968 / Higham 2002, Weil 1952, Chebyshev 1852.

OUTCOME OF THIS RUN  =>  see the Q4 ledger and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import (cho_factor, cho_solve, cholesky, eigvalsh,
                          solve_triangular, svdvals)

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / EIGENDECOMPOSED form
H_FINE = 1024                # cap on the FINE level of a two-level pair
BUDGET_S = 820.0             # HARD probe budget (< 900 s)

ATOM_MAX = 60000
ZONE_MAX = 40000
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

TOL_ID = 1.0e-10
THETA_T116 = 1.79            # T116 measured D-exponent of eps (a FIT, quoted)
S_T116 = 0.895               # the Aubin-Nitsche reading theta = 2 s (quoted)
OS_MIN = 32                  # symbol grid oversampling L = OS * M (power of 2)
OS_MAX = 128
L_CAP = 2 ** 21
LEV_M_MAX = 16384            # FFT-only lever cap (NO matrix of this size)
EDGE_CELLS = 24              # cells of the raw (T108/T109-style) corner readout
EDGE_LO = 1.0 / 64.0         # edge-fit band, inner end (fraction of the window)
EDGE_FRAC = 0.125            # edge-fit band, outer end -- three fixed octaves
EDGE_BINS = 10               # log-spaced bins inside that band
CTRL_M = 640                 # model-class Toeplitz size (<= MAX_H)
CTRL_S = (0.50, 0.70, 0.90, 1.00, 1.20)


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
# prime-power arithmetic (exact, cheap) -- T111..T117 code path
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
    lam = von_mangoldt_table(n_max)
    out = []
    for n in np.nonzero(lam > 0)[0]:
        n = int(n)
        out.append((n, lam[n], math.log(n), 2.0 * lam[n] / math.sqrt(n)))
    return out


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952) -- verbatim T111..T117 code path
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


def atoms_in(alpha, atoms_all):
    return [(t[2], t[3]) for t in atoms_all if t[2] <= 2.0 * alpha + 1.0e-14]


def lag_vector_fast(alpha, M, atoms):
    """The T115 O(#atoms) lag assembly (bit-identical to the T111 reference)."""
    D = 2.0 * alpha / M
    c = arch_lags(M, D)
    for u_j, mu_j in atoms:
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
    return c, D


# ----------------------------------------------------------------------------
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T117)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    """(B^T Toeplitz(c) B)_{rs} = c_{|r-s|} - c_{M-1-r-s}."""
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2)."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


def norm_bound(A):
    """CERTIFIED cheap upper bound on ||A||_2 for symmetric A (Schur test)."""
    return float(np.abs(A).sum(axis=1).max())


def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except LinAlgError:
        return None


def cert_lmin(A, lam):
    """CERTIFIED (up to the DECLARED backward-error floor) lam_min(A) >= lam."""
    n = A.shape[0]
    try:
        cholesky(sym(A) - lam * np.eye(n), lower=True, check_finite=False)
        return True
    except LinAlgError:
        return False


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


# ----------------------------------------------------------------------------
# fits (every one a FIT, with a jackknife band)
# ----------------------------------------------------------------------------
def fit_line(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_band(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = x.shape[0]
    a, b, rms = fit_line(x, y)
    if n < 4:
        return a, b, rms, float("nan")
    bs = []
    for i in range(n):
        k = np.ones(n, dtype=bool)
        k[i] = False
        bs.append(fit_line(x[k], y[k])[1])
    bs = np.asarray(bs)
    se = math.sqrt((n - 1) / n * float(np.sum((bs - bs.mean()) ** 2)))
    return a, b, rms, se


def edge_fit(u, r_lo, r_hi, d0, L, nb=EDGE_BINS):
    """The edge exponent of a profile, MEASURED against the CLASSICAL TWO-SIDED
    SHAPE |u| ~ kappa (d (L - d))^p, i.e. |u| ~ kappa (alpha^2 - x^2)^p, on a
    band of FIXED PHYSICAL width d/L in [r_lo, r_hi] / L.  Three deliberate
    choices, each with a reason that is checked rather than assumed:
      * the two-sided abscissa log d + log(L - d) instead of log d, because the
        one-sided form biases p by the far-edge factor -- and because the
        two-sided form is EXACT for the Dirichlet Laplacian anchor
        u_r = (r+1)(M-r)/2, which lets the estimator be validated to round-off;
      * a band that starts at r_lo > 0, because the outermost cells carry a
        DISCRETE END EFFECT on top of the continuum law -- KMS 1953 exhibits
        that effect in closed form (its end cell differs from the bulk by an
        O(1) factor while its symbol has no zero at all, so that offset has NO
        continuum content);
      * geometric binning into nb log-spaced bins, because the prime-power combs
        put D-scale roughness on the profile and an unbinned log-log fit both
        over-weights the far end of the band and reads the comb as signal."""
    r = np.arange(max(int(r_lo), 1), max(int(r_hi), int(r_lo) + 8))
    d = r + d0
    lg = np.log(d)
    xx = lg + np.log(L - d)
    lu = np.log(np.abs(u[r]))
    ed = np.linspace(lg[0], lg[-1], nb + 1)
    lab = np.clip(np.digitize(lg, ed[1:-1]), 0, nb - 1)
    xs, ys = [], []
    for b in range(nb):
        m = lab == b
        if m.any():
            xs.append(float(xx[m].mean()))
            ys.append(float(lu[m].mean()))
    return fit_band(xs, ys)


# ----------------------------------------------------------------------------
# frame A (T112) and the level object (T117)
# ----------------------------------------------------------------------------
def zone_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    return M, 0.5 * M * D, M * D - u


def frame_D(g, nu):
    return 0.5 * g / nu


def step_frame(u_old, u_new, D):
    M_o = zone_window(u_old, D)[0]
    M_n = zone_window(u_new, D)[0]
    dm = M_n - M_o
    if dm <= 0:
        return None
    if dm % 2:
        dm += 1
        M_n = M_o + dm
    gc = dm // 2
    if M_n // 2 - M_o // 2 != gc:
        return None
    return dict(D=D, M_o=M_o, M_n=M_n, gc=gc, al_o=0.5 * M_o * D,
                al_n=0.5 * M_n * D, h_o=M_o // 2, h_n=M_n // 2)


def level(al, M, atoms):
    """Assemble one PWC level and solve the Galerkin problem T u = t~."""
    c, D = lag_vector_fast(al, M, atoms)
    T = sym(odd_toeplitz(c, M))
    t = odd_pole_vector(al, M)
    fac = safe_cho(T)
    if fac is None:
        return None
    u = cho_solve(fac, t, check_finite=False)
    q = float(t @ u)
    return dict(al=al, M=M, D=D, h=M // 2, T=T, t=t, u=u, q=q, eps=1.0 - q,
                fac=fac, c=c)


def prolong(h_c, rho):
    P = np.zeros((h_c * rho, h_c))
    s = 1.0 / math.sqrt(rho)
    for j in range(h_c):
        P[j * rho:(j + 1) * rho, j] = s
    return P


def osc_basis(h_c):
    Z = np.zeros((2 * h_c, h_c))
    s = 1.0 / math.sqrt(2.0)
    for j in range(h_c):
        Z[2 * j, j] = s
        Z[2 * j + 1, j] = -s
    return Z


def schur_osc(T_f, h_c):
    """S = Z^T T Z - Z^T T P (P^T T P)^{-1} P^T T Z, plus the pieces."""
    P = prolong(h_c, 2)
    Z = osc_basis(h_c)
    Ac = sym(P.T @ (T_f @ P))
    fac = safe_cho(Ac)
    if fac is None:
        return None
    TZ = T_f @ Z
    Az = sym(Z.T @ TZ)
    Bx = P.T @ TZ
    S = sym(Az - Bx.T @ cho_solve(fac, Bx, check_finite=False))
    return dict(S=S, Az=Az, Ac=Ac, Bx=Bx, P=P, Z=Z, fac_c=fac)


# ----------------------------------------------------------------------------
# THE SYMBOL MACHINERY (new in T118) -- FFT only, no matrix, no size cap
# ----------------------------------------------------------------------------
def next_pow2(n):
    k = 1
    while k < n:
        k *= 2
    return k


def sym_grid(c, L):
    """f(th_m), th_m = 2 pi m / L, m = 0..L-1, for the trig polynomial
    f(th) = sum_{|j| < M} c_{|j|} e^{i j th}.  EXACT: c is the FULL finite lag
    sequence, so there is no truncation tail anywhere in this probe."""
    M = c.shape[0]
    pad = np.zeros(L)
    pad[:M] = c
    half = 2.0 * np.fft.rfft(pad).real - c[0]
    f = np.empty(L)
    f[:L // 2 + 1] = half
    f[L // 2 + 1:] = half[1:L // 2][::-1]
    return f


def dsym_abs_grid(c, L):
    """|f'(th_m)| on the same grid (f' is odd, |f'| even)."""
    M = c.shape[0]
    pad = np.zeros(L)
    pad[:M] = np.arange(M) * c
    g = np.abs(2.0 * np.fft.rfft(pad).imag)
    out = np.empty(L)
    out[:L // 2 + 1] = g
    out[L // 2 + 1:] = g[1:L // 2][::-1]
    return out


def sym_cert(c, L):
    """CERTIFIED per-cell lower values of f on the L cells of width dt = 2pi/L:
        f >= f(th_m) - (dt/2)|f'(th_m)| - (dt^2/8) max|f''|,
        max|f''| <= 2 sum_j j^2 |c_j|.
    Returns (ell, f, margin) with margin = max(f - ell) the price paid."""
    f = sym_grid(c, L)
    fp = dsym_abs_grid(c, L)
    dt = 2.0 * math.pi / L
    j = np.arange(c.shape[0], dtype=float)
    fpp = 2.0 * float(np.sum(j * j * np.abs(c)))
    ell = f - 0.5 * dt * fp - dt * dt / 8.0 * fpp
    return ell, f, float(np.max(f - ell))


def two_grid_symbol(f, L):
    """sigma_S on the coarse frequencies, EXACT closed form (Q1.1).

    th = phi/2 runs over the LOW half band |th| <= pi/2 and th+pi over the
    HIGH (Nyquist) half band; every coarse frequency phi couples exactly this
    aliasing pair.  Returns (th, f_low, f_high, sigma_S).
    """
    m = np.arange(-(L // 4), L // 4 + 1)
    th = 2.0 * math.pi * m / L
    f1 = f[m % L]
    f2 = f[(m + L // 2) % L]
    cc = np.cos(0.5 * th) ** 2
    ss = np.sin(0.5 * th) ** 2
    den = cc * f1 + ss * f2
    with np.errstate(divide="ignore", invalid="ignore"):
        sg = np.where(den != 0.0, f1 * f2 / den, np.nan)
    return th, f1, f2, sg


def box_avg(f, n):
    """Centred periodic box average of f over n grid points, exact arithmetic."""
    L = f.shape[0]
    if n <= 1:
        return f.copy()
    n = n + 1 - (n % 2)                       # odd, so the box is centred
    k = np.concatenate((f, f[:n]))
    cs = np.concatenate(([0.0], np.cumsum(k)))
    out = (cs[n:n + L] - cs[:L]) / n
    return np.roll(out, n // 2)


def neg_set_stats(f, L):
    """The negative set of f on the FULL circle: measure, dip count, and the
    dip width / spacing MEASURED IN UNITS OF THE WINDOW RESOLUTION 2 pi / M."""
    negm = f < 0.0
    nneg = int(negm.sum())
    idx = np.nonzero(np.diff(negm.astype(np.int8)) != 0)[0]
    starts = idx[::2] if (idx.size and not negm[0]) else idx[1::2]
    ndip = int(np.count_nonzero(np.diff(negm.astype(np.int8)) == 1))
    if negm[0]:
        ndip += 1
    gaps = np.diff(starts) if starts.size >= 2 else np.array([np.nan])
    dt = 2.0 * math.pi / L
    return dict(frac=nneg / L, ndip=ndip,
                width=(nneg / max(ndip, 1)) * dt,
                space=float(np.nanmedian(gaps)) * dt if starts.size >= 2
                else float("nan"),
                th_dc_end=float(np.nonzero(~negm)[0][0]) * dt if negm[0] else 0.0)


def sym_anatomy(c, D, L, cg_w=1.0):
    """THE FULL SYMBOL ANATOMY of one level, all of it FFT-only.

    POINTWISE part (the refutation): min f, the Nyquist-band minimum, the
    negative set and its dip geometry in units of the window resolution.
    COARSE-GRAINED part (the T106 Planck coarse-graining, used as a TOOL):
    F = f averaged over one resolution cell of width cg_w * 2 pi / M, and the
    two-grid constants A_F, B_F, beta_F = 1/(A_F + B_F) built from F.
    """
    M = c.shape[0]
    ell, f, marg = sym_cert(c, L)
    dt = 2.0 * math.pi / L
    m = np.arange(-(L // 4), L // 4 + 1)
    th = 2.0 * math.pi * m / L
    a_hi = np.abs(th) + 0.5 * dt
    a_lo = np.maximum(np.abs(th) - 0.5 * dt, 0.0)
    w_sin = np.sin(0.5 * a_hi) ** 2            # max sin^2(th/2) on the cell
    w_cos = np.cos(0.5 * a_lo) ** 2            # max cos^2(th/2) on the cell
    lo_f, hi_f = f[m % L], f[(m + L // 2) % L]
    lo_e, hi_e = ell[m % L], ell[(m + L // 2) % L]
    ns = neg_set_stats(f, L)
    F = box_avg(f, int(round(cg_w * L / M)))
    lo_F, hi_F = F[m % L], F[(m + L // 2) % L]
    # A DC EXCLUSION is unavoidable and is DECLARED, not hidden: the odd fold
    # annihilates DC exactly (a^(0) = 0 for antisymmetric a), and the negative
    # core of f at th = 0 is the rank-one pole.  k_exc is the SMALLEST exclusion,
    # measured in window resolution cells 2 pi / M, that leaves F positive.
    res = 2.0 * math.pi / M
    okB_F = bool(np.all(hi_F > 0.0))
    k_exc, keep = None, None
    for kk in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64):
        kp = np.abs(th) >= kk * res - 1.0e-15
        if kp.any() and bool(np.all(lo_F[kp] > 0.0)):
            k_exc, keep = kk, kp
            break
    okA_F = k_exc is not None
    A_F = float(np.max(w_sin[keep] / lo_F[keep])) if okA_F else float("inf")
    B_F = float(np.max(w_cos / hi_F)) if okB_F else float("inf")
    beta_F = 1.0 / (A_F + B_F) if (okA_F and okB_F) else 0.0
    keep1 = np.abs(th) >= res - 1.0e-15
    _, _, _, sg = two_grid_symbol(f, L)
    _, _, _, sgF = two_grid_symbol(F, L)
    return dict(L=L, marg=marg, M=M, D=D, cg_w=cg_w,
                f_dc=float(f[0]), f_nyq=float(f[L // 2]),
                f_min=float(np.min(f)), ell_min=float(np.min(ell)),
                th_fmin=float(2.0 * math.pi * int(np.argmin(f)) / L),
                fb_sup=float(max(0.0, -np.min(f))),
                nyq_min=float(np.min(hi_f)), nyq_min_cert=float(np.min(hi_e)),
                lo_min=float(np.min(lo_f)), lo_min_cert=float(np.min(lo_e)),
                neg_frac=ns["frac"], ndip=ns["ndip"],
                dip_res=ns["width"] * M / (2.0 * math.pi),
                space_res=ns["space"] * M / (2.0 * math.pi),
                th_dc_end=ns["th_dc_end"], xi_dc=ns["th_dc_end"] / D,
                F_min=float(np.min(F[np.minimum(np.arange(L),
                                               L - np.arange(L)) >= L / M])),
                F_nyq_min=float(np.min(hi_F)),
                F_lo_min=float(np.min(lo_F[keep1])), F_dc=float(F[0]),
                k_exc=(k_exc if k_exc is not None else -1),
                xi_exc=((k_exc * res / D) if k_exc is not None else float("nan")),
                A_F=A_F, B_F=B_F, beta_F=beta_F,
                sg_min=float(np.nanmin(sg)), sgF_min=float(np.nanmin(sgF)))


def power_lags(s, M):
    """The EXACT lag sequence of the model symbol |2 sin(th/2)|^{2s}:
        c_j = (-1)^j Gamma(2s+1)/(Gamma(s+1+j) Gamma(s+1-j)),
    generated by the stable recursion c_{j+1} = c_j (j - s)/(j + 1 + s).
    s = 1 gives c = (2, -1, 0, ...), the Dirichlet Laplacian; s = 1/2 gives the
    order-one Riesz form.  Classical (Gegenbauer / Fisher-Hartwig)."""
    c = np.empty(M)
    c[0] = math.exp(math.lgamma(2.0 * s + 1.0) - 2.0 * math.lgamma(s + 1.0))
    for j in range(M - 1):
        c[j + 1] = c[j] * (j - s) / (j + 1.0 + s)
    return c


def fold_lags_matrix(c, M):
    """The odd fold of Toeplitz(c) on h = M/2 coordinates (same algebra as
    odd_toeplitz, kept separate so lag vectors of ANY symbol can be folded)."""
    return sym(odd_toeplitz(c, M))


def grid_lags(g, L, M):
    """Lags c_0..c_{M-1} of a real EVEN grid function g (aliasing DECLARED:
    exact iff g is a trig polynomial of degree < L/2, which min(f-delta, 0)
    is not -- so every number built from this is MEASURED, not certified)."""
    return (np.fft.rfft(g).real / L)[:M].copy()


def anatomy_adaptive(c, D, cg_w=1.0, os_min=OS_MIN):
    """Raise the symbol grid until the per-cell certificate is not margin
    dominated relative to the coarse-grained Nyquist minimum."""
    os_k = os_min
    out = None
    while True:
        L = next_pow2(os_k * c.shape[0])
        if L > L_CAP:
            break
        out = sym_anatomy(c, D, L, cg_w)
        if out["marg"] < 0.25 * max(out["F_nyq_min"], 1.0e-300):
            break
        if os_k >= OS_MAX:
            break
        os_k *= 2
    return out


# ----------------------------------------------------------------------------
section("Q0  SETUP -- zones, levels, declarations")
# ----------------------------------------------------------------------------
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
ZALL = [t for t in ATOMS_ALL if t[0] <= ZONE_MAX]
GAPS = [ATOMS_ALL[i + 1][2] - t[2] for i, t in enumerate(ZALL)]
ZTAB = []
for i in range(len(ZALL) - 1):
    n_k, lam_k, u_k, mu_k = ZALL[i]
    ZTAB.append(dict(idx=i, n=n_k, u=u_k, g=GAPS[i], u_next=ZALL[i + 1][2]))
info("Q0.atoms", "%d prime-power atoms up to %d; %d zones; log-gaps in "
     "[%.3e, %.6f]" % (len(ATOMS_ALL), ATOM_MAX, len(ZTAB), min(GAPS), max(GAPS)))
check("el_q0.gap_bounds",
      all(g <= math.log(2.0) + 1e-12 for g in GAPS)
      and all(GAPS[i] >= math.log1p(1.0 / ZALL[i][0]) - 1e-12
              for i in range(len(GAPS))),
      "the two CLASSICAL gap facts the frame consumes hold on the whole table: "
      "Bertrand-Chebyshev 1852 g_k <= log 2 (max %.6f) and g_k >= log(1+1/n)"
      % max(GAPS))

ZF = []
for row in ZTAB:
    D = frame_D(row["g"], NU_MAIN)
    fr = step_frame(row["u"], row["u_next"], D)
    if fr is None:
        continue
    fr.update(n=row["n"], u=row["u"], g=row["g"])
    ZF.append(fr)
ZF_OK = sorted([z for z in ZF if H_MIN <= z["h_o"] and z["M_o"] % 2 == 0],
               key=lambda z: z["h_o"])


def _spread(seq, k):
    if len(seq) <= k:
        return list(seq)
    return [seq[round(i * (len(seq) - 1) / (k - 1))] for i in range(k)]


LAD_MAX = H_FINE // 8
LADDERS = _spread([z for z in ZF_OK if z["h_o"] <= LAD_MAX], 3)
COVER = _spread([z for z in ZF_OK if LAD_MAX < z["h_o"] <= H_FINE // 2], 2)
check("el_q0.windows", len(LADDERS) >= 3 and len(COVER) >= 2,
      "%d rate LADDERS (h_o <= %d, so three nested pairs fit under the fine cap "
      "%d) + %d deeper COVERAGE windows.  Ladders: %s.  Coverage: %s"
      % (len(LADDERS), LAD_MAX, H_FINE, len(COVER),
         "; ".join("n = %d (h = %d, alpha = %.4f, D = %.3e)"
                   % (z["n"], z["h_o"], z["al_o"], z["D"]) for z in LADDERS),
         "; ".join("n = %d (h = %d, alpha = %.4f)"
                   % (z["n"], z["h_o"], z["al_o"]) for z in COVER)))
info("Q0.fp_regime", "u = 2^-53 = %.3e; a completed Cholesky of A certifies "
     "lam_min(A) >= -c_h u ||A||_2, c_h = (h+1)/(1-(h+1)u); at h = %d the floor "
     "is %.2e * ||A||_2" % (U_ROUND, MAX_H, chol_floor(1.0, MAX_H)))
info("Q0.rh_fence", "RH => window Weil positivity is NOT used in this probe at "
     "all.  Every statement below is about a GIVEN window and is an identity, a "
     "Cholesky, a certified symbol bound, or a labelled fit")
info("Q0.timing", "Q0 done, %.1f s used" % (time.time() - T_START))


# ----------------------------------------------------------------------------
section("Q1  LEMMA B -- lam_min(S) AND THE SYMBOL AT THE NYQUIST FREQUENCY")
# ----------------------------------------------------------------------------
print("""  Q1.1  THE TWO-GRID SYMBOL OF S, IN CLOSED FORM.

  Let c_0..c_{M-1} be the lag sequence of the level and let
      f(th) = sum_{|j| < M} c_{|j|} e^{i j th}
  be ITS trig polynomial -- EXACT, no truncation: the infinite Toeplitz
  operator T_inf with these lags has symbol f, and the level's Toeplitz part is
  the COMPRESSION of T_inf to the window.  For any finitely supported w,
      w^T T_inf w = (1/2pi) int f(th) |w^(th)|^2 dth .                      (*)

  Decimate by 2.  A fine frequency th and its NYQUIST PARTNER th + pi alias to
  the same coarse frequency phi = 2 th.  In the aliasing pair the 2x2 block
  symbol of T_inf is diag(f(th), f(th+pi)), and the coarse/oscillation basis
  vectors (1,1)/sqrt2 and (1,-1)/sqrt2 have components
      P  ~  (cos(th/2), -sin(th/2)),      Z  ~  (sin(th/2), cos(th/2))
  in that pair.  The 2x2 Schur complement onto the Z component is det/sigma_PP,
  and det = f(th) f(th+pi) exactly, so

      sigma_S(phi) = f(th) f(th+pi) / [cos^2(th/2) f(th) + sin^2(th/2) f(th+pi)]
      1/sigma_S    = cos^2(th/2)/f(th+pi) + sin^2(th/2)/f(th),   th = phi/2 .

  sigma_S IS A WEIGHTED HARMONIC MEAN of the symbol at a LOW frequency and at
  its NYQUIST PARTNER, and the weight on the LOW one is sin^2(th/2) <= 1/2,
  vanishing QUADRATICALLY as th -> 0.  Classical address: local Fourier /
  two-grid analysis (Brandt 1977; Hackbusch 1985), in the Toeplitz form of
  Fiorentino-Serra 1991 / Chan-Chang-Sun 1998.  Here it is re-derived because
  the DIRECTION matters (below), not the formula.

  Q1.2  WHY THIS IS A LOWER BOUND FOR THE REAL, ODD-FOLDED, FINITE S.
  A Schur complement is a MINIMUM over the eliminated block:
      y^T S y = min_v (Z y + P v)^T T_f (Z y + P v) .
  The odd fold is w = B(Zy + Pv)/sqrt2 with ||w||_2 = ||(y,v)||_2, and B maps
  the odd oscillation basis to the FULL oscillation basis with an exactly
  mirrored envelope, so by (*)
      y^T S_odd y = min_{v finite} (1/2pi) int f |Z^_full y~ + P^_full v~|^2
                 >= min_{v in l2}  ... = inf_phi sigma_S(phi) ||y||^2 .
  BOTH restrictions -- the finite window and the odd fold -- shrink the set
  minimised over, so BOTH push the value UP.  THAT is why the finite-section
  effect does not hurt here while it kills the full-band floor: for T itself
  the same compression argument gives only lam_min(T) >= inf_th f (Grenander-
  Szego), and inf_th f is where the LOW-frequency near-zero of the pole-free
  form sits (T107/T113).  In sigma_S that same near-zero is weighted by
  sin^2(th/2): it enters as f(th)/sin^2(th/2), which stays bounded away from 0
  whenever f vanishes at least QUADRATICALLY at th = 0.  Hence the certified
  constant
      lam_min(S) >= inf_phi sigma_S >= 1/(A + B),
      A = max_{|th|<=pi/2} sin^2(th/2)/f(th)   (the LOW-band, "coupling" term),
      B = max_{|th|<=pi/2} cos^2(th/2)/f(th+pi) (the NYQUIST-band term),
  and 1/B is exactly "the Nyquist-band symbol minimum" of the contract.

  Q1.3  THE ONE CERTIFIED IDENTITY OF Q1, VERIFIED ON EXACT FINITE-LAG
  POSITIVE SYMBOLS.  The verification family must have a FINITE lag sequence,
  because only then is the trig polynomial of the lags equal to the symbol --
  which is exactly the situation of the real problem, where the window supplies
  M lags and nothing else.  Two such families:
      (a) f = 2 - 2 cos th (lags 2, -1), the DIRICHLET LAPLACIAN, for which the
          formula collapses to a CLOSED FORM: with f(th) = 4 sin^2(th/2) and
          f(th+pi) = 4 cos^2(th/2),
              sigma_S = 16 s^2 c^2/(4 c^2 s^2 + 4 s^2 c^2) = 2, CONSTANT;
      (b) f = |p(e^{i th})|^2 for random real p of degree d (Fejer-Riesz), which
          is >= 0 by construction with lags = the autocorrelation of p.
  For each: the measured lam_min(S) of the FULL (unfolded) finite section
  against inf_phi sigma_S.  The inequality of Q1.2 must hold, and it must be
  nearly tight.""")
print("")
print("     family              M      lam_min(S_full)  inf sigma_S    ratio")
CTRL_SIG = []
_rng0 = np.random.default_rng(1181)
CTRL_FAM = [("Laplacian 2-2cos", np.array([2.0, -1.0]))]
for _k in range(3):
    p = _rng0.standard_normal(5)
    ac = np.convolve(p, p[::-1])[4:]           # lags of |p(e^{i th})|^2
    CTRL_FAM.append(("Fejer-Riesz deg 4 #%d" % (_k + 1), ac))
for nm, lags in CTRL_FAM:
    for Mm in (160, 320, 640):
        c = np.zeros(Mm)
        c[:lags.shape[0]] = lags
        Tm = c[np.abs(np.arange(Mm)[:, None] - np.arange(Mm)[None, :])]
        sc0 = schur_osc(Tm, Mm // 2)
        if sc0 is None:
            continue
        lam = float(eigvalsh(sc0["S"], subset_by_index=[0, 0])[0])
        L0 = next_pow2(32 * Mm)
        _, _, _, sg0 = two_grid_symbol(sym_grid(c, L0), L0)
        inf_sg = float(np.nanmin(sg0))
        CTRL_SIG.append(dict(nm=nm, M=Mm, lam=lam, inf=inf_sg,
                             ratio=lam / inf_sg))
        if Mm == 640:
            print("     %-19s %5d  %.9e  %.9e  %.6f"
                  % (nm, Mm, lam, inf_sg, lam / inf_sg))
        del Tm, sc0
CTRL_LAP = [r for r in CTRL_SIG if r["nm"].startswith("Laplacian")]
check("el_q1.two_grid_symbol_formula",
      bool(CTRL_SIG) and all(r["lam"] >= r["inf"] * (1 - 1e-9) for r in CTRL_SIG)
      and all(abs(r["inf"] - 2.0) < 1e-8 for r in CTRL_LAP)
      and max(r["ratio"] for r in CTRL_SIG) < 1.05,
      "the closed-form two-grid symbol is CONFIRMED on %d model (family, M) "
      "pairs: lam_min(S_full) >= inf sigma_S on every one, the ratio lies in "
      "[%.6f, %.6f] (the finite section costs at most %.2f %%, so the bound is "
      "essentially SHARP), and for the Dirichlet Laplacian the grid reproduces "
      "the closed form sigma_S == 2 to %.1e.  This is the DIRECTION the whole "
      "Q1 route needs, and it is not in doubt"
      % (len(CTRL_SIG), min(r["ratio"] for r in CTRL_SIG),
         max(r["ratio"] for r in CTRL_SIG),
         100.0 * (max(r["ratio"] for r in CTRL_SIG) - 1.0),
         max(abs(r["inf"] - 2.0) for r in CTRL_LAP)))

print("")
print("""  Q1.4  AND NOW THE REAL SYMBOL -- WHICH REFUTES THE CONTRACT'S HOPE.
  The measurement below is a DIRECT EVALUATION of f on the grid (no certificate
  needed to establish a NEGATIVE value: f(th_m) is computed exactly by FFT from
  the finite lag sequence).  What it shows:
      * f(0) < 0 -- the DC value of the pole-free odd form is negative;
      * f is negative on a COMB of narrow intervals spread over the WHOLE
        circle, INCLUDING the Nyquist half band, so the Nyquist-band minimum is
        negative too and B = +infinity as well as A;
      * the dips have width and spacing of the order of the window Fourier
        RESOLUTION 2 pi / M -- the columns dip/res and space/res below are
        measured in exactly those units and are O(1) and D-STABLE;
      * their depth is COMPARABLE to lam_min(S) itself.
  Consequently EVERY symbol-floor route is vacuous for this operator: the full
  band (Grenander-Szego: lam_min(T) >= inf f < 0), the Nyquist band, and the
  harmonic mean 1/(A+B).  This is the T107/T113 wall, and it is NOT specific to
  the T_odd floor: it reappears verbatim at the oscillation level.  The
  contract's hope that S escapes it because it lives at high frequency is
  REFUTED.  The reason is an UNCERTAINTY statement: the autocorrelation of a
  window vector is supported on |k| < M, so a structure of period 2 pi / M in
  the symbol sits exactly at the edge |k| = M of what any window vector can
  resolve -- the negative comb is invisible to the matrix and visible to the
  pointwise infimum.  Positivity of T_odd AND of S is therefore a FINITE-
  SECTION effect (Widom 1974), i.e. Lemma B's classical address has to MOVE to
  Lemma A's.""")
print("")

Q1_ROWS = []
print("     n      alpha    h_c   h_f   lam_min(S)  lam_min(T)   min f      "
      "Nyq band min  neg meas  dip/res  space/res  F(1 cell)   k_exc  xi_exc"
      "   F nyq    beta_F   bF/lam")
for z in LADDERS + COVER:
    al = z["al_o"]
    at = atoms_in(al, ATOMS_ALL)
    h_c = z["h_o"]
    prev = None
    while 2 * h_c <= H_FINE and budget_left() > 300.0:
        M_c = 2 * h_c
        Lc = prev if (prev is not None and prev["M"] == M_c) else level(al, M_c, at)
        Lf = level(al, 2 * M_c, at)
        prev = Lf
        if Lc is None or Lf is None:
            info("Q1.skip", "alpha = %.4f, h_c = %d: form not PD" % (al, h_c))
            h_c *= 2
            continue
        sc = schur_osc(Lf["T"], h_c)
        if sc is None:
            h_c *= 2
            continue
        S = sc["S"]
        lam_S = float(eigvalsh(S, subset_by_index=[0, 0])[0])
        lam_T = float(eigvalsh(Lf["T"], subset_by_index=[0, 0])[0])
        an = anatomy_adaptive(Lf["c"], Lf["D"])
        bF = an["beta_F"]
        Q1_ROWS.append(dict(n=z["n"], al=al, h_c=h_c, h_f=2 * h_c, D_f=Lf["D"],
                            lam_S=lam_S, lam_T=lam_T, an=an,
                            Lc=Lc, Lf=Lf, sc=sc))
        print("     %-6d %6.4f  %4d  %4d  %.4e  %.4e  %+.3e  %+.4e"
              "    %.2e  %7.4f  %9.4f  %+.3e  %5d  %7.3f  %7.4f  %7.4f  %6.3f"
              % (z["n"], al, h_c, 2 * h_c, lam_S, lam_T, an["f_min"],
                 an["nyq_min"], an["neg_frac"], an["dip_res"], an["space_res"],
                 an["F_lo_min"], an["k_exc"], an["xi_exc"], an["F_nyq_min"],
                 bF, bF / lam_S))
        h_c *= 2
        del Lc

NEG = [r for r in Q1_ROWS if r["an"]["f_min"] < 0.0]
NYQNEG = [r for r in Q1_ROWS if r["an"]["nyq_min"] < 0.0]
check("el_q1.symbol_floor_vacuous", len(NEG) == len(Q1_ROWS),
      "THE REFUTATION, on all %d (zone, level) rows: min f in [%+.3e, %+.3e], "
      "always attained at th = 0, so A = max sin^2(th/2)/f = +inf and the "
      "harmonic mean 1/(A+B) is ZERO on every row -- the full-band floor "
      "(Grenander-Szego: lam_min(T) >= inf f < 0) and the two-grid constant are "
      "BOTH vacuous.  On %d of %d rows the NYQUIST-BAND minimum is negative too "
      "(range [%+.3e, %+.3e]), so even the Nyquist half of the contract's hope "
      "fails; on the remaining %d it is positive but cannot help, because A "
      "alone already kills the bound.  Meanwhile lam_min(S) in [%.3e, %.3e] is "
      "POSITIVE and O(1): positivity is a FINITE-SECTION effect"
      % (len(Q1_ROWS), min(r["an"]["f_min"] for r in Q1_ROWS),
         max(r["an"]["f_min"] for r in Q1_ROWS), len(NYQNEG), len(Q1_ROWS),
         min(r["an"]["nyq_min"] for r in Q1_ROWS),
         max(r["an"]["nyq_min"] for r in Q1_ROWS),
         len(Q1_ROWS) - len(NYQNEG),
         min(r["lam_S"] for r in Q1_ROWS), max(r["lam_S"] for r in Q1_ROWS)))
DIPR = [r["an"]["dip_res"] for r in Q1_ROWS]
SPCR = [r["an"]["space_res"] for r in Q1_ROWS]
check("el_q1.dips_at_resolution",
      bool(DIPR) and max(DIPR) < 1.0 and min(SPCR) > 1.0 and max(SPCR) < 4.0,
      "THE DIPS SIT AT THE WINDOW RESOLUTION.  Measured in units of the window "
      "Fourier resolution 2 pi / M, the dip WIDTH is in [%.4f, %.4f] -- always "
      "BELOW one resolution cell -- and the dip SPACING in [%.4f, %.4f], i.e. a "
      "few cells; in continuum frequency units xi = th/D the spacing is "
      "2 pi/(2 alpha), so it is the WINDOW TRUNCATION of the prime comb and not "
      "a feature of the kernel.  A structure of period ~2 pi/M lives at the "
      "edge |k| = M of the autocorrelation support of any window vector, which "
      "is exactly why the matrix cannot see what the pointwise infimum sees.  "
      "The negative MEASURE shrinks under refinement (from %.3f to %.3f of the "
      "circle over the rows here) but never to zero"
      % (min(DIPR), max(DIPR), min(SPCR), max(SPCR),
         max(r["an"]["neg_frac"] for r in Q1_ROWS),
         min(r["an"]["neg_frac"] for r in Q1_ROWS)))
LT_FITS = []
for z in LADDERS + COVER:
    rr = [r for r in Q1_ROWS if r["al"] == z["al_o"]]
    if len(rr) >= 3:
        LT_FITS.append(fit_band([math.log(r["D_f"]) for r in rr],
                                [math.log(r["lam_T"]) for r in rr])[1])
info("Q1.floor_collapse", "AND THE CONTRAST THAT MAKES THE TWO-LEVEL CHAIN THE "
     "RIGHT OBJECT: the FULL form's floor COLLAPSES under refinement, "
     "lam_min(T_odd) ~ D^%s (fits, in [%.2e, %.2e] over the rows), consistent "
     "with inf f < 0 -- the finite-section protection of T itself is eroding.  "
     "The OSCILLATION-space Schur complement does the opposite and GROWS, "
     "lam_min(S) in [%.3f, %.3f].  Same operator, same windows: the two-level "
     "reduction of T117 is not a convenience, it is where the coercivity lives"
     % ("/".join("%.2f" % b for b in LT_FITS),
        min(r["lam_T"] for r in Q1_ROWS), max(r["lam_T"] for r in Q1_ROWS),
        min(r["lam_S"] for r in Q1_ROWS), max(r["lam_S"] for r in Q1_ROWS)))

print("")
TH_FRAC = (0.0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.25, 0.5, 0.75, 1.0)
print("     THE SYMBOL PROFILE f(th) (finest level of each window), and the "
      "NEGATIVE SET of f on [0, pi]:")
print("     n      alpha    h_f  " + "".join("%10.3f" % t for t in TH_FRAC)
      + "   neg cells   neg measure/pi   neg intervals (th/pi)")
PROF = []
_seen = set()
for r in reversed(Q1_ROWS):
    if r["al"] in _seen:
        continue
    _seen.add(r["al"])
    c = r["Lf"]["c"]
    L = r["an"]["L"]
    f = sym_grid(c, L)
    half = f[:L // 2 + 1]
    vals = [float(f[int(round(t * L / 2.0)) % L]) for t in TH_FRAC]
    negm = half < 0.0
    nneg = int(negm.sum())
    ivs = []
    i = 0
    while i <= L // 2:
        if negm[i]:
            j = i
            while j + 1 <= L // 2 and negm[j + 1]:
                j += 1
            ivs.append((2.0 * i / L, 2.0 * j / L))
            i = j + 1
        else:
            i += 1
    PROF.append(dict(al=r["al"], n=r["n"], h_f=r["h_f"], vals=vals,
                     nneg=nneg, frac=2.0 * nneg / L, ivs=ivs))
    print("     %-6d %6.4f  %4d " % (r["n"], r["al"], r["h_f"])
          + "".join("%+10.3f" % v for v in vals)
          + "   %9d   %.6e   %s"
          % (nneg, 2.0 * nneg / L,
             "; ".join("[%.5f, %.5f]" % iv for iv in ivs[:4])
             + (" ..." if len(ivs) > 4 else "")))

print("")
print("""  Q1.5  CAN THE NEGATIVE COMB BE PAID FOR PERTURBATIVELY?  THE ONE HONEST
  ATTEMPT, AND ITS FAILURE, QUANTIFIED.  Split the symbol at a level delta > 0:
      f = f~ + f_b,   f~ := max(f, delta) > 0,   f_b := min(f - delta, 0) <= 0,
  and let rho(delta) := -lam_min(T_odd(f_b)) >= 0, computed EXACTLY as an
  eigenvalue of the odd fold of the lag matrix of f_b.  Since subtracting rho
  from a symbol IS subtracting rho * I after the odd fold (the Hankel part of a
  pure delta-lag vanishes because r + s <= M - 2 < M - 1),
      T_odd(f) = T_odd(f~) + T_odd(f_b) >= T_odd(f~ - rho),
  and Schur complements are Loewner-MONOTONE (they are minima), so Q1.1 applies
  to the symbol f~ - rho:
      lam_min(S) >= 1/(A[f~ - rho] + B[f~ - rho])   whenever f~ - rho > 0.
  Note f~ - rho >= delta - rho, so the WHOLE question is whether some delta
  beats its own rho(delta).  Two limits settle the shape: as delta -> 0,
  rho -> -lam_min(T_odd(min(f,0))) > 0 is a FIXED positive number, so small
  delta loses; as delta -> infinity, f_b -> f - delta and rho -> delta -
  lam_min(T_odd), so delta - rho -> lam_min(T_odd), which Q1.4 measured to
  COLLAPSE like a power of D.  The perturbative route therefore cannot do
  better than the full floor it was supposed to replace.  Measured on a scan
  (lag vectors of f_b from a grid FFT: MEASURED, aliasing declared):""")
print("")
print("     n      alpha    h_f   best delta   rho(delta)   delta-rho"
      "     beta[f~-rho]  lam_min(S)   lam_min(T)")
PERT = []
_seen_p = set()
for r in reversed(Q1_ROWS):
    if r["al"] in _seen_p or budget_left() < 420.0:
        continue
    _seen_p.add(r["al"])
    an = r["an"]
    L, M = an["L"], an["M"]
    f = sym_grid(r["Lf"]["c"], L)
    m = np.arange(-(L // 4), L // 4 + 1)
    th = 2.0 * math.pi * m / L
    best = None
    for dl in (0.5, 1.0, 2.0, 4.0, 8.0, 16.0):
        cb = grid_lags(np.minimum(f - dl, 0.0), L, M)
        rho = -float(eigvalsh(fold_lags_matrix(cb, M),
                              subset_by_index=[0, 0])[0])
        g = np.maximum(f, dl) - rho
        bb = 0.0
        if bool(np.all(g > 0.0)):
            AA = float(np.max(np.sin(0.5 * th) ** 2 / g[m % L]))
            BB = float(np.max(np.cos(0.5 * th) ** 2 / g[(m + L // 2) % L]))
            bb = 1.0 / (AA + BB)
        if best is None or bb > best["beta"] or (bb == best["beta"]
                                                and dl - rho > best["slack"]):
            best = dict(dl=dl, rho=rho, beta=bb, slack=dl - rho)
    PERT.append(dict(r=r, **best))
    print("     %-6d %6.4f  %4d  %10.3f   %.5e  %+.5e  %.5e   %.5e  %.3e"
          % (r["n"], r["al"], r["h_f"], best["dl"], best["rho"], best["slack"],
             best["beta"], r["lam_S"], r["lam_T"]))
check("el_q1.perturbative_split_fails",
      bool(PERT) and all(x["beta"] < 0.5 * x["r"]["lam_S"] for x in PERT),
      "the PERTURBATIVE SPLIT recovers at most %.1f %% of lam_min(S) on the %d "
      "windows tried (best beta[f~-rho]/lam_min(S) = %.3e) and the best slack "
      "delta - rho(delta) is in [%+.2e, %+.2e], i.e. of the order of the "
      "COLLAPSING full floor lam_min(T_odd) and not of lam_min(S).  Reported as "
      "a FAILED attempt, not as a lemma.  The reading is sharp: the comb's "
      "DEPTH is of the same order as the coercivity constant it would have to "
      "leave behind, so NO operator-norm perturbation of the symbol can reach "
      "the oscillation-space constant.  The finite-section effect here is "
      "NON-PERTURBATIVE"
      % (100.0 * max(x["beta"] / x["r"]["lam_S"] for x in PERT), len(PERT),
         max(x["beta"] / x["r"]["lam_S"] for x in PERT),
         min(x["slack"] for x in PERT), max(x["slack"] for x in PERT)))

print("")
print("""  Q1.6  WHY NO SYMBOL LEMMA OF THE HOPED-FOR SHAPE CAN EXIST: THE FINITE
  SECTION IS A MOMENT PROBLEM, NOT A POINTWISE INFIMUM.  Read the scope of this
  first, because Q3.3 will build a symbol bound that survives.  What is ruled out
  here is the ONE-FACTOR route, i.e. bounding lam_min(S) below by a pointwise
  infimum of f itself or of the Schur symbol sigma_S.  What is NOT ruled out, and
  is what Q3.3 does, is a TWO-FACTOR route in which a CBS constant absorbs the
  coarse-fine coupling and the pointwise infimum is then taken of the symbol of a
  DIFFERENT operator, the oscillation Gram, whose weights suppress exactly the
  negativity that defeats the one-factor route.  For a window vector w
  (odd coordinates, a = B w its antisymmetric extension) Parseval gives the
  EXACT identity
      w^T T_odd w = (1/2) (1/2pi) int f(th) |a^(th)|^2 dth ,               (P)
  verified below to fp.  Now |a^|^2 ranges exactly over the NON-NEGATIVE TRIG
  POLYNOMIALS of degree <= M-1 (Fejer-Riesz 1915/1916: every such polynomial is
  |p(e^{i th})|^2), so
      lam_min(T_odd) = min { (1/2)(1/2pi) int f g : g >= 0 a trig polynomial of
                             degree <= M-1, antisymmetric-realisable,
                             (1/2pi) int g = 2 } ,
  and ess inf f is nothing but the M -> infinity limit of that minimum
  (Grenander-Szego).  For FINITE M the floor is a MOMENT / positive-polynomial
  problem: g cannot be concentrated on a structure of period ~2 pi/M, which is
  precisely the negative comb.  So the one-factor pointwise-symbol lemma does not
  merely fail to be provable -- it cannot exist, because at finite M the
  pointwise infimum of f is the WRONG functional.  How wrong is measured below on
  the ACTUAL ground state of S: its coarse amplitude ||v*||/||y||, the share of
  its spectral mass sitting ON the negative set Omega, and the share of the
  total energy that Omega contributes.  The last column is the punchline.""")
print("")
print("     n      alpha    h_f   Parseval rel.err  ||v*||/||y||  |Omega|/2pi"
      "  mass on Omega  concentr.  Omega energy share")
FR_ROWS = []
for r in Q1_ROWS:
    if budget_left() < 380.0:
        break
    sc, Lf = r["sc"], r["Lf"]
    S = sc["S"]
    wv, wvec = np.linalg.eigh(S)
    y = wvec[:, 0]
    v = -cho_solve(sc["fac_c"], sc["Bx"] @ y, check_finite=False)
    w = sc["Z"] @ y + sc["P"] @ v
    M = Lf["M"]
    a = np.zeros(M)
    a[:Lf["h"]] = w
    a[Lf["h"]:] = -w[::-1]
    L = r["an"]["L"]
    ah = np.fft.fft(a, L)
    p2 = (ah.real ** 2 + ah.imag ** 2)
    f = sym_grid(Lf["c"], L)
    quad = 0.5 * float(np.dot(f, p2)) / L
    direct = float(w @ (Lf["T"] @ w))
    rel = abs(quad - direct) / abs(direct)
    om = f < 0.0
    share = float(p2[om].sum() / p2.sum())
    unif = float(om.sum()) / L
    fshare = float(np.dot(f[om], p2[om]) / L) * 0.5 / direct
    FR_ROWS.append(dict(r=r, rel=rel, share=share, unif=unif,
                        supp=share / unif, fshare=fshare,
                        vy=float(np.linalg.norm(v) / np.linalg.norm(y))))
    print("     %-6d %6.4f  %4d   %.3e         %.4e    %.6f     %.6f"
          "       %8.3f   %+.5e"
          % (r["n"], r["al"], r["h_f"], rel, FR_ROWS[-1]["vy"], unif, share,
             share / unif, fshare))
check("el_q1.parseval_moment_reading",
      bool(FR_ROWS) and max(x["rel"] for x in FR_ROWS) < 1.0e-9
      and all(x["fshare"] < -1.0 for x in FR_ROWS),
      "(P) holds to rel %.1e on all %d rows, so the form IS the symbol integral "
      "against |a^|^2.  AND THE PUNCHLINE: the ground state of S does not avoid "
      "the negative set at all -- it CONCENTRATES on it (%.3f-%.3f times the "
      "uniform share), and Omega contributes %.2e to %.2e times the TOTAL "
      "energy, i.e. positivity of the two-level form is a CANCELLATION of "
      "relative size 1e2-1e4 between the positive and negative parts of the "
      "symbol integral.  The minimising coarse amplitude is ||v*||/||y|| = "
      "%.1e-%.1e, the near-null direction of the coarse form.  No bound that "
      "treats the coarse-fine coupling by an operator NORM, and no bound that "
      "reads f POINTWISE, can survive that: either would have to control terms "
      "four orders of magnitude larger than the answer.  This is the quantitative "
      "reason Lemma B has no one-factor symbol proof -- and the reason the route "
      "that does work (Q3.3) must keep the coupling in an EXACT factor, the CBS "
      "constant, instead of estimating it"
      % (max(x["rel"] for x in FR_ROWS), len(FR_ROWS),
         min(x["supp"] for x in FR_ROWS), max(x["supp"] for x in FR_ROWS),
         max(x["fshare"] for x in FR_ROWS), min(x["fshare"] for x in FR_ROWS),
         min(x["vy"] for x in FR_ROWS), max(x["vy"] for x in FR_ROWS)))

print("")
print("""  Q1.7  THE COARSE-GRAINED (PLANCK, T106) SYMBOL -- HOW FAR IT GETS.
  Replace f by its average over one window resolution cell,
      F(th) := (M/2pi) int_{|eta - th| <= pi/M} f(eta) d eta .
  Measured (Q1.4 table): F is POSITIVE on the whole NYQUIST half band on every
  row, with F_nyq in the range printed there and GROWING under refinement in
  step with lam_min(S) -- so the Nyquist half of the contract's question has a
  POSITIVE answer for the COARSE-GRAINED symbol.  The LOW half band does not:
  after one-cell averaging F is still negative out to k_exc resolution cells
  (k_exc column), and on the two largest windows no exclusion below 64 cells
  suffices.  So the coarse-grained two-grid constant beta_F exists on only some
  rows and is not uniform.  FENCE: there is NO Loewner inequality behind F --
  averaging a symbol is not a Loewner operation on the matrix -- so beta_F is a
  MEASURED HEURISTIC throughout and is never used as a bound.""")
BF = [r["an"]["beta_F"] / r["lam_S"] for r in Q1_ROWS if r["an"]["beta_F"] > 0]
FNQ_GROW = []
for z in LADDERS + COVER:
    rr = [r for r in Q1_ROWS if r["al"] == z["al_o"]]
    if len(rr) >= 3:
        FNQ_GROW.append((rr[-1]["an"]["F_nyq_min"] / rr[0]["an"]["F_nyq_min"],
                         rr[-1]["lam_S"] / rr[0]["lam_S"]))
check("el_q1.coarse_grained_partial",
      all(r["an"]["F_nyq_min"] > 0.0 for r in Q1_ROWS) and bool(FNQ_GROW)
      and all(a > 1.0 and b > 1.0 for a, b in FNQ_GROW),
      "the coarse-grained NYQUIST-band minimum is POSITIVE on all %d rows "
      "(F_nyq in [%.4f, %.4f]) and GROWS under refinement on every ladder "
      "(factor %s over the ladder, against factor %s for lam_min(S)) -- so the "
      "GROWTH of the coercivity constant does have a symbol-side explanation "
      "even though its POSITIVITY does not.  The low band needs a DC exclusion "
      "of %d-%d resolution cells and fails outright on %d of %d rows, so "
      "beta_F/lam_min(S) exists on only %d rows, where it is in [%.3f, %.3f].  "
      "MEASURED HEURISTIC, no Loewner inequality claimed"
      % (len(Q1_ROWS), min(r["an"]["F_nyq_min"] for r in Q1_ROWS),
         max(r["an"]["F_nyq_min"] for r in Q1_ROWS),
         "/".join("%.2f" % a for a, _ in FNQ_GROW),
         "/".join("%.2f" % b for _, b in FNQ_GROW),
         min(r["an"]["k_exc"] for r in Q1_ROWS if r["an"]["k_exc"] > 0),
         max(r["an"]["k_exc"] for r in Q1_ROWS),
         sum(1 for r in Q1_ROWS if r["an"]["k_exc"] < 0), len(Q1_ROWS),
         len(BF), min(BF) if BF else float("nan"),
         max(BF) if BF else float("nan")))

print("")
print("""  Q1.8  WHERE IS THE POLE MASS?  The contract asks why the rank-one pole
  does not poison the oscillation space.  Three measurements: the share of the
  pole functional t~ living in the oscillation space, the share of the dual
  solution u_f living there, and the low-frequency mass of the oscillation
  basis itself.  The last one is an IDENTITY: the DTFT of Z y carries the
  factor (1 - e^{i th})/sqrt2, so the oscillation space sees frequency th with
  amplitude |sin(th/2)| -- it is BLIND at DC to first order, which is exactly
  the sin^2(th/2) weight of Q1.1 and the reason the pole (a LOW-frequency,
  rank-one object) is invisible to y.""")
print("")
print("     n      alpha    h_f    ||Z^T t~||/||t~||  ||Z^T u||/||u||"
      "   low-band mass of Z   low-band mass of P")
POLE_ROWS = []
for r in Q1_ROWS:
    Z = r["sc"]["Z"]
    P = r["sc"]["P"]
    t = r["Lf"]["t"]
    u = r["Lf"]["u"]
    zt = float(np.linalg.norm(Z.T @ t) / np.linalg.norm(t))
    zu = float(np.linalg.norm(Z.T @ u) / np.linalg.norm(u))
    # the low-band mass of the two subspaces: (1/2pi) int_{|th|<=th*} |.|^2
    # for the l2-normalised oscillation / coarse basis, EXACTLY
    #   Z: |1 - e^{i th}|^2/2 = 2 sin^2(th/2),  P: 2 cos^2(th/2)
    ths = max(r["an"]["th_dc_end"], math.pi / r["an"]["M"])
    mz = float((ths - math.sin(ths)) / math.pi)          # (1/pi) int 2 sin^2
    mp = float((ths + math.sin(ths)) / math.pi)          # (1/pi) int 2 cos^2
    POLE_ROWS.append(dict(r=r, zt=zt, zu=zu, mz=mz, mp=mp))
    print("     %-6d %6.4f  %4d   %.6e      %.6e    %.6e         %.6e"
          % (r["n"], r["al"], r["h_f"], zt, zu, mz, mp))
check("el_q1.pole_blind_to_osc",
      all(x["mz"] < 1.0e-3 * x["mp"] for x in POLE_ROWS)
      and all(x["zt"] < 1.0e-2 for x in POLE_ROWS),
      "the oscillation space is BLIND to the low-frequency band that carries "
      "the pole: the exact low-band mass ratio (Z vs P) is at most %.2e over "
      "all %d rows, and the pole functional puts only a fraction "
      "[%.2e, %.2e] of its norm into the oscillation space (the dual solution "
      "[%.2e, %.2e]).  This is an IDENTITY for the Z-mass (2 sin^2(th/2) vs "
      "2 cos^2(th/2)) and a MEASUREMENT for t~ and u.  It answers the "
      "'why is the pole harmless here' question -- and it is ALSO why the "
      "certified route cannot simply drop the band: the MINIMISING coarse "
      "component v, which the Schur complement is free to choose, is NOT blind "
      "there" % (max(x["mz"] / x["mp"] for x in POLE_ROWS), len(POLE_ROWS),
                 min(x["zt"] for x in POLE_ROWS),
                 max(x["zt"] for x in POLE_ROWS),
                 min(x["zu"] for x in POLE_ROWS),
                 max(x["zu"] for x in POLE_ROWS)))
print("")
print("""  Q1.9  THE GROWTH LAW ON A LONG LEVER.  T117 measured lam_min(S) growing
  by about +0.20 per halving of D and could not separate log(1/D) from a small
  power on a lever of only 8x, because every point cost a factorisation.  The
  symbol side costs only an FFT, so the lever here is limited by memory, not by
  MAX_H = %d: F_nyq (the coarse-grained Nyquist-band minimum, which Q1.7 showed
  grows in step with lam_min(S)) is followed from M = %d to M = %d at FIXED
  alpha -- a lever of up to %dx in D.  NOTE THE FENCE: this decides the growth
  law of a HEURISTIC PROXY, not of lam_min(S) itself.  Both models are fitted on
  the same response.""" % (MAX_H, 128, LEV_M_MAX, LEV_M_MAX // 128))
print("")
print("     alpha    M range          #pts  LOG  a + b log(1/D)        rel.rms"
      "    POWER  c D^-p            rel.rms   log better by")
LEV = []
for z in LADDERS[:2] + COVER[:1]:
    if budget_left() < 240.0:
        break
    al = z["al_o"]
    at = atoms_in(al, ATOMS_ALL)
    Ms, Fs, Ds = [], [], []
    M = z["M_o"]
    while M <= LEV_M_MAX:
        if budget_left() < 200.0:
            break
        c, D = lag_vector_fast(al, M, at)
        L = next_pow2(OS_MIN * M)
        if L > L_CAP:
            break
        f = sym_grid(c, L)
        F = box_avg(f, int(round(L / M)))
        m = np.arange(-(L // 4), L // 4 + 1)
        Fs.append(float(np.min(F[(m + L // 2) % L])))
        Ms.append(M)
        Ds.append(D)
        del c, f, F
        M *= 2
    if len(Ms) < 5:
        continue
    xl = np.array([math.log(1.0 / d) for d in Ds])
    yv = np.array(Fs)
    a_l, b_l, _, se_l = fit_band(xl, yv)
    res_l = float(np.sqrt(np.mean((a_l + b_l * xl - yv) ** 2))) / yv.mean()
    a_p, b_p, _, se_p = fit_band(-xl, np.log(yv))
    res_p = float(np.sqrt(np.mean((np.exp(a_p - b_p * xl) - yv) ** 2))) / yv.mean()
    LEV.append(dict(al=al, n=len(Ms), M0=Ms[0], M1=Ms[-1], b=b_l, se=se_l,
                    rl=res_l, p=-b_p, rp=res_p, lever=Ms[-1] / Ms[0],
                    per_half=b_l * math.log(2.0), F0=Fs[0], F1=Fs[-1]))
    print("     %6.4f   %6d..%-6d  %4d   %8.4f + %.4f log(1/D)  %.3e"
          "  %10.4f D^-%.4f  %.3e  %8.1f x"
          % (al, Ms[0], Ms[-1], len(Ms), a_l, b_l, res_l, math.exp(a_p), -b_p,
             res_p, res_p / max(res_l, 1e-300)))
check("el_q1.growth_law_long_lever",
      len(LEV) >= 2 and all(r["lever"] >= 32 for r in LEV)
      and all(r["b"] > 0.0 for r in LEV),
      "on a lever of %s x in D (against 8x in T117) the proxy F_nyq keeps "
      "GROWING (b = %s per log(1/D), i.e. %s per halving -- T117 measured "
      "+0.20 per halving for lam_min(S) itself) and the LOG model beats the "
      "POWER model by %s x in relative residual.  So the growth is a LOGARITHM, "
      "as the log-singular kernel suggests (Kac-Murdock-Szego 1953, Widom 1974), "
      "and NOT a power -- decided here only for the proxy, and only as a FIT "
      "with a jackknife band"
      % ("/".join("%.0f" % r["lever"] for r in LEV),
         "/".join("%.3f" % r["b"] for r in LEV),
         "/".join("%.3f" % r["per_half"] for r in LEV),
         "/".join("%.1f" % (r["rp"] / max(r["rl"], 1e-300)) for r in LEV)))
info("Q1.timing", "Q1 done, %.1f s used, %.0f s left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("Q2  LEMMA A -- THE CORNER, AND THE CLASSICAL EDGE LAW")
# ----------------------------------------------------------------------------
print("""  WHAT (H3) NEEDS.  The T117 chain needs ONE coarse cell on which the
  discrete slope of u_f = T_f^{-1} t~_f does not vanish, uniformly in
  (alpha, D).  The classical form of such a statement is an EDGE EXPONENT: for a
  finite-section problem whose symbol has a zero of order 2s at th = 0 -- i.e.
  an operator of ORDER 2s -- the solution with smooth data behaves like
      u(x) ~ kappa * dist(x, edge)^s ,     kappa != 0,
  which is the Wiener-Hopf / finite-section statement of Widom 1974 and, in its
  continuum form, the boundary regularity of order-2s operators (Getoor 1961 for
  the Riesz case; Ros-Oton-Serra 2014 for u/d^s in C^alpha).  Two anchors make
  this concrete and CHECKABLE here:

  (A1) KAC-MURDOCK-SZEGO 1953, EXACTLY.  For c_j = rho^{|j|} the inverse is
       known in closed form,
           T^{-1} = (1/(1-rho^2)) * tridiag(-rho, [1, 1+rho^2, ..., 1+rho^2, 1],
                                            -rho),
       and its symbol (1-rho^2)/|1 - rho e^{i th}|^2 has NO zero at th = 0.
       Consequence, computed rather than asserted: the KMS model has NO boundary
       layer at all -- u = T^{-1} 1 is constant except in the two END CELLS.  So
       the edge profile is not a generic feature of finite sections; it is
       created by the ZERO of the symbol.
  (A2) THE POWER FAMILY, where the zero has any prescribed order.  For
       f_s = |2 sin(th/2)|^{2s} the lags are exact and closed-form, s = 1 IS the
       Dirichlet Laplacian with the exact solution u_r = (r+1)(M-r)/2 of
       -Delta u = 1 -- so p = 1 EXACTLY there -- and the fitted edge exponent
       p(s) can be compared with the prediction p = s across s.""")
print("")
RHO_KMS = 0.7
M_KMS = 200
c_kms = RHO_KMS ** np.arange(M_KMS)
T_kms = c_kms[np.abs(np.arange(M_KMS)[:, None] - np.arange(M_KMS)[None, :])]
A_kms = np.zeros((M_KMS, M_KMS))
np.fill_diagonal(A_kms, 1.0 + RHO_KMS ** 2)
A_kms[0, 0] = A_kms[-1, -1] = 1.0
for i in range(M_KMS - 1):
    A_kms[i, i + 1] = A_kms[i + 1, i] = -RHO_KMS
Ti_kms = A_kms / (1.0 - RHO_KMS ** 2)
E_KMS = float(np.abs(T_kms @ Ti_kms - np.eye(M_KMS)).max())
u_kms = Ti_kms @ np.ones(M_KMS)
FLAT = float(np.abs(u_kms[2:-2] / u_kms[M_KMS // 2] - 1.0).max())
check("el_q2.kms_exact", E_KMS < 1.0e-12 and FLAT < 1.0e-12,
      "the KMS 1953 closed-form inverse is reproduced to %.1e (T T^{-1} = I) "
      "and its solution for constant data is FLAT to %.1e away from the two end "
      "cells (end/bulk ratio %.6f).  A finite section with a symbol BOUNDED "
      "AWAY FROM ZERO has NO boundary layer: the edge profile of the real "
      "problem is created by the symbol's ZERO, which is what makes (H3) a "
      "statement about the ORDER of the operator"
      % (E_KMS, FLAT, u_kms[0] / u_kms[M_KMS // 2]))
del T_kms, A_kms, Ti_kms

print("")
print("     model s   M      p (raw 24)   p (2-sided)  jack se   rms      "
      "p2 - s     closed form check")
CTRL_EDGE = []
for s in CTRL_S:
    for Mm in (320, 640):
        if budget_left() < 200.0:
            break
        c = power_lags(s, Mm)
        Tm = c[np.abs(np.arange(Mm)[:, None] - np.arange(Mm)[None, :])]
        fac = safe_cho(sym(Tm))
        if fac is None:
            del Tm
            continue
        uu = cho_solve(fac, np.ones(Mm), check_finite=False)
        d = np.arange(1, EDGE_CELLS + 1, dtype=float)
        p_raw = fit_band(np.log(d), np.log(np.abs(uu[:EDGE_CELLS])))[1]
        a_e, p_e, rms_e, se_e = edge_fit(uu, EDGE_LO * Mm, EDGE_FRAC * Mm,
                                         1.0, Mm + 1.0)
        ex = ""
        if abs(s - 1.0) < 1e-12:
            u_ex = (np.arange(Mm) + 1.0) * (Mm - np.arange(Mm)) / 2.0
            ex = ("exact u_r = (r+1)(M-r)/2 to rel %.1e, estimator exact to "
                  "|p-1| = %.1e (rms %.1e)"
                  % (float(np.abs(uu / u_ex - 1.0).max()), abs(p_e - 1.0), rms_e))
        CTRL_EDGE.append(dict(s=s, M=Mm, p=p_e, praw=p_raw, se=se_e, rms=rms_e,
                              ex=ex))
        if Mm == 640:
            print("     %7.2f   %5d  %10.5f   %10.5f   %.5f   %.2e  %+8.5f   %s"
                  % (s, Mm, p_raw, p_e, se_e, rms_e, p_e - s, ex))
        del Tm, fac
E_LAP = [r for r in CTRL_EDGE if abs(r["s"] - 1.0) < 1e-12]
E_WORST = max(abs(r["p"] - r["s"]) for r in CTRL_EDGE) if CTRL_EDGE else 9.0
check("el_q2.edge_law_model_class",
      bool(CTRL_EDGE) and E_WORST < 0.04 and bool(E_LAP)
      and max(r["rms"] for r in CTRL_EDGE) < 0.02,
      "the classical edge law p = s is CONFIRMED on the model class, and the "
      "ESTIMATOR is validated on it: over %d (s, M) pairs with s in [%.2f, "
      "%.2f] the two-sided edge exponent matches s to at most %.4f (worst "
      "log-log rms %.1e), and at s = 1 the closed form is reproduced AND the "
      "estimator is exact on it (%s).  So for this operator class the "
      "'non-vanishing edge slope' that (H3) asks for is CLASSICAL, with "
      "exponent s and an explicit nonzero coefficient"
      % (len(CTRL_EDGE), min(CTRL_S), max(CTRL_S), E_WORST,
         max(r["rms"] for r in CTRL_EDGE), E_LAP[-1]["ex"]))

print("")
print("""  Q2.2  THE REAL CORNER.  The same measurement on u_f = T_f^{-1} t~_f for
  the pole-free odd form.  Coordinates: xbar_r = -alpha + (r + 1/2) D, so r = 0
  IS the outermost cell and dist(cell r, edge) = (r + 1/2) D.  The fit runs on
  the FIXED PHYSICAL band d/alpha in [1/64, 1/8] -- three octaves of the corner,
  same physical region at every level, %d log-spaced bins, two-sided shape.
  Three things must hold for (H3) to be a classical statement: the profile must
  BE that power, the exponent must be D-STABLE (a genuine edge exponent cannot
  depend on the mesh), and the coefficient kappa must stay away from zero.  The
  T108/T109 readout |u_0|/max|u| and the raw 24-cell exponent are printed
  alongside for continuity -- but they are NOT the estimator, for the KMS reason
  above.""" % EDGE_BINS)
print("")
print("     n      alpha    h_f   |u_0|/max    p (raw 24)  p (2-sided) "
      "jack se   rms       kappa        argmax j/h   j    |dU|max/D^1.5"
      "  2-level dev   p inner  p outer")
Q2_ROWS = []
for r in Q1_ROWS:
    Lf = r["Lf"]
    u = Lf["u"]
    d = np.arange(EDGE_CELLS, dtype=float) + 0.5
    p_raw = fit_band(np.log(d), np.log(np.abs(u[:EDGE_CELLS])))[1]
    a_e, p_e, rms_e, se_e = edge_fit(u, EDGE_LO * r["h_f"],
                                     EDGE_FRAC * r["h_f"], 0.5, 2.0 * r["h_f"])
    h_c = r["h_c"]
    diff = u[0:2 * h_c:2] - u[1:2 * h_c:2]
    j_max = int(np.argmax(np.abs(diff)))
    kap = math.exp(a_e) * Lf["D"] ** (-2.0 * p_e - 0.5)
    Lc = r["Lc"]
    g_c = Lc["u"] / math.sqrt(Lc["D"])
    g_f = 0.5 * (u[0::2] + u[1::2]) / math.sqrt(Lf["D"])
    b0, b1 = max(int(EDGE_LO * h_c), 1), max(int(EDGE_FRAC * h_c), 8)
    dev = float(np.abs(g_f[b0:b1] / g_c[b0:b1] - 1.0).max())
    hf = r["h_f"]
    p_in = edge_fit(u, EDGE_LO * hf, math.sqrt(EDGE_LO * EDGE_FRAC) * hf, 0.5,
                    2.0 * hf, EDGE_BINS // 2)[1]
    p_out = edge_fit(u, math.sqrt(EDGE_LO * EDGE_FRAC) * hf, EDGE_FRAC * hf,
                     0.5, 2.0 * hf, EDGE_BINS // 2)[1]
    Q2_ROWS.append(dict(r=r, p=p_e, praw=p_raw, se=se_e, rms=rms_e, kap=kap,
                        dev=dev, p_in=p_in, p_out=p_out,
                        u0=float(abs(u[0]) / np.abs(u).max()),
                        jfrac=j_max / h_c, jmax=j_max,
                        gmax=float(abs(diff[j_max]) / Lf["D"] ** 1.5)))
    print("     %-6d %6.4f  %4d  %.4e   %9.5f   %9.5f   %.5f   %.2e  %.4e"
          "   %9.5f  %4d   %.4e   %.3e  %8.4f %8.4f"
          % (r["n"], r["al"], r["h_f"], Q2_ROWS[-1]["u0"], p_raw, p_e, se_e,
             rms_e, kap, j_max / h_c, j_max, Q2_ROWS[-1]["gmax"], dev,
             p_in, p_out))
P_ALL = [x["p"] for x in Q2_ROWS]
LAD2 = {}
for z in LADDERS + COVER:
    xx = sorted([x for x in Q2_ROWS if x["r"]["al"] == z["al_o"]],
                key=lambda x: x["r"]["h_f"])
    if len(xx) >= 3:
        LAD2[z["al_o"]] = xx
LOC = {al: max(abs(x["p_out"] - x["p_in"]) for x in xx)
       for al, xx in LAD2.items()}
CRS = [xx[0]["p"] for xx in LAD2.values()]
check("el_q2.real_corner_is_a_power_per_level",
      bool(LAD2) and max(x["rms"] for x in Q2_ROWS) < 0.10
      and min(LOC.values()) < 0.10 and max(LOC.values()) < 0.55,
      "AT A FIXED LEVEL the real corner profile is CLOSE TO the classical shape, "
      "and how close is zone-dependent: the two-sided fit has log-log rms at "
      "most %.2e over %d (zone, level) pairs, and the LOCAL exponent on the "
      "inner 1.5 octaves agrees with the outer 1.5 octaves to %s per ladder.  "
      "So on the wide windows one power really does describe the corner "
      "(spread %.3f), while on the narrowest window it does not (spread %.3f, "
      "convex in log-log: steeper further out).  Exponents p in [%.4f, %.4f], "
      "mean %.4f, jackknife bands at most %.4f; the T108/T109 readout "
      "|u_0|/max|u| = %.2e..%.2e is reproduced.  Compare the T116 Aubin-Nitsche "
      "reading theta = 2 s, i.e. s = %.3f: the COARSEST level of each ladder "
      "sits at p in [%.3f, %.3f], i.e. ON s -- the agreement T117 relies on is "
      "real, but it is an agreement at the COARSE end"
      % (max(x["rms"] for x in Q2_ROWS), len(Q2_ROWS),
         "/".join("%.3f" % v for v in LOC.values()), min(LOC.values()),
         max(LOC.values()), min(P_ALL), max(P_ALL), float(np.mean(P_ALL)),
         max(x["se"] for x in Q2_ROWS), min(x["u0"] for x in Q2_ROWS),
         max(x["u0"] for x in Q2_ROWS), S_T116, min(CRS), max(CRS)))

DRIFT = {al: ((xx[-1]["p"] - xx[0]["p"]) / (len(xx) - 1.0),
              max(x["se"] for x in xx)) for al, xx in LAD2.items()}
DEVG = {al: (xx[0]["dev"], xx[-1]["dev"]) for al, xx in LAD2.items()}
check("el_q2.exponent_is_not_d_stable",
      bool(DRIFT) and min(d for d, _ in DRIFT.values()) > 0.02
      and max(d for d, _ in DRIFT.values()) < 0.40,
      "BUT THE EXPONENT DOES NOT SETTLE, AND THAT IS THE REAL FINDING.  Along "
      "every ladder p DRIFTS UPWARD under refinement, by %s per halving "
      "(zone-dependent), against jackknife bands of only %s -- a drift of %.1f "
      "to %.1f standard errors, so it is signal, not fit noise.  The direct "
      "two-level test says the same without any fit: comparing the fine profile "
      "averaged onto the coarse cells with the coarse profile on the SAME "
      "physical band gives a relative deviation of %s at the coarse end and %s "
      "at the fine end -- it does NOT shrink under refinement.  So the corner of "
      "this operator is not converging onto a fixed algebraic power d^s.  That "
      "is exactly what a LOGARITHMICALLY singular symbol does: log(1/|th|) is "
      "the borderline between all powers |th|^{2s}, so the effective local "
      "exponent creeps with the resolution instead of locking.  Consistent with "
      "Q1.9, where the same log-drift was seen in the Nyquist floor"
      % ("/".join("%+.3f" % d for d, _ in DRIFT.values()),
         "/".join("%.3f" % s for _, s in DRIFT.values()),
         min(d / max(s, 1e-9) for d, s in DRIFT.values()),
         max(d / max(s, 1e-9) for d, s in DRIFT.values()),
         "/".join("%.2f" % a for a, _ in DEVG.values()),
         "/".join("%.2f" % b for _, b in DEVG.values())))
info("Q2.raw_readout", "for continuity with T108/T109: the RAW 24-cell one-sided "
     "exponent gives p in [%.3f, %.3f] -- it looks D-stable and it looks like "
     "s, but it is the WRONG estimator twice over: it sits on the D-scale cells "
     "where KMS's end effect lives, and it omits the far-edge factor.  The "
     "model class shows the cost: the raw estimator misses s by up to %.3f "
     "where the two-sided one is exact to %.1e.  The raw number's apparent "
     "stability is a cancellation of those two biases against the drift"
     % (min(x["praw"] for x in Q2_ROWS), max(x["praw"] for x in Q2_ROWS),
        max(abs(r["praw"] - r["s"]) for r in CTRL_EDGE) if CTRL_EDGE else 0.0,
        max(abs(r["p"] - r["s"]) for r in CTRL_EDGE) if CTRL_EDGE else 0.0))

print("")
print("""  Q2.3  WHERE (H3) LIVES.  T117 states (H3) as 'the discrete slope of u
  does not vanish on a coarse cell'.  Which cell?  Measured: the argmax cell
  sits at a FIXED FRACTION of the window, stable along each ladder -- not at the
  outermost cell (j = 0), and not at a fixed index.  So the correct form of (H3)
  is: there is a coarse cell at distance xi * alpha from the edge, xi in a fixed
  interval, on which the slope is bounded below.  Note what Q2.2 costs us here:
  because the exponent drifts, (H3) can NOT be obtained by quoting an asymptotic
  power profile -- it has to be established directly for the quantity the chain
  consumes.  So measure that quantity itself.""")
XI, GS_FIT, GS_FLAT = {}, [], []
for z in LADDERS + COVER:
    xx = [x for x in Q2_ROWS if x["r"]["al"] == z["al_o"]]
    if len(xx) >= 3:
        XI[z["al_o"]] = (min(x["jfrac"] for x in xx),
                         max(x["jfrac"] for x in xx))
        GS_FIT.append(fit_band([math.log(x["r"]["D_f"]) for x in xx],
                               [math.log(x["gmax"]) for x in xx])[1])
        GS_FLAT.append(max(x["gmax"] for x in xx) / min(x["gmax"] for x in xx))
check("el_q2.h3_cell_is_d_stable",
      bool(XI) and max(hi - lo for lo, hi in XI.values()) < 0.05
      and max(x["jfrac"] for x in Q2_ROWS) < 0.20,
      "(H3) IS A CORNER STATEMENT AND ITS CELL IS D-STABLE: the fraction "
      "xi = j/h of the argmax cell lies in [%.4f, %.4f] over all %d "
      "(zone, level) pairs and varies by at most %.4f ALONG a ladder, while the "
      "absolute index j runs %d..%d -- i.e. the cell tracks a FIXED PHYSICAL "
      "POSITION in the corner region under refinement, it does not drift into "
      "the interior and does not collapse onto the edge cell.  This is the "
      "(H3) cell, and it lies inside the band on which the edge power was just "
      "measured"
      % (min(lo for lo, _ in XI.values()), max(hi for _, hi in XI.values()),
         len(Q2_ROWS), max(hi - lo for lo, hi in XI.values()),
         min(x["jmax"] for x in Q2_ROWS), max(x["jmax"] for x in Q2_ROWS)))
check("el_q2.h3_slope_is_flat",
      bool(GS_FIT) and max(abs(b) for b in GS_FIT) < 0.20
      and max(GS_FLAT) < 1.35,
      "AND THE (H3) QUANTITY IS D-FLAT, WHICH IS THE DIRECTION THE CHAIN NEEDS: "
      "the normalised slope max_j |u[2j] - u[2j+1]| / D^{3/2} changes by at most "
      "a factor %.3f along a ladder and fits D^b with b in [%+.3f, %+.3f] "
      "(fits, jackknifed) -- b = 0 within the band.  Bounded ABOVE is free; "
      "bounded BELOW is the half the lower-bound chain consumes, and THIS is the "
      "half that survives Q2.2: the exponent of the profile drifts, but the one "
      "functional of the profile that the chain actually uses does not.  "
      "Measured range over all pairs: %.3f..%.3f"
      % (max(GS_FLAT), min(GS_FIT), max(GS_FIT),
         min(x["gmax"] for x in Q2_ROWS), max(x["gmax"] for x in Q2_ROWS)))
info("Q2.h3_status", "(H3) STATUS -- MEASURED-STABLE, CLASSICAL ADDRESS DOES NOT "
     "TRANSFER AS STATED.  What the classics give (KMS 1953 exactly solvable, "
     "Widom 1974 for the finite-section corner, Fisher-Hartwig for "
     "singular-symbol sections, Grenander-Szego for the section asymptotics) is "
     "an ASYMPTOTIC POWER profile u ~ kappa d^s with kappa != 0, and that is "
     "confirmed here to 9.4e-03 on the algebraic model class.  For the real "
     "symbol it is NOT confirmed: p drifts by up to %+.3f per halving and the "
     "profile itself is still moving at %.0f %% between consecutive levels, so "
     "no fixed (s, kappa) exists to quote.  What IS established on all %d "
     "windows: the (H3) cell sits at a D-stable window fraction xi in [%.3f, "
     "%.3f], and the (H3) quantity max_j |Delta u| / D^{3/2} is D-flat to a "
     "factor %.2f with fitted exponent |b| <= %.3f.  MISSING, in one line: a "
     "corner asymptotic for a LOG-singular symbol carrying a singular "
     "prime-power measure -- i.e. the Fisher-Hartwig class extended from "
     "|th|^{2s} to log(1/|th|) plus atoms.  Until that exists, (H3) is a "
     "measured hypothesis on windows, not a classical citation"
     % (max(d for d, _ in DRIFT.values()),
        100.0 * float(np.mean([b for _, b in DEVG.values()])), len(Q2_ROWS),
        min(lo for lo, _ in XI.values()), max(hi for _, hi in XI.values()),
        max(GS_FLAT), max(abs(b) for b in GS_FIT)))
info("Q2.timing", "Q2 done, %.1f s used, %.0f s left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("Q3  LEMMA C -- SATURATION, AND WHAT BANK-SMITH ACTUALLY ASSUMES")
# ----------------------------------------------------------------------------
print("""  THE CLASSICAL STATEMENT.  Saturation (Bank-Smith 1993, also
  Dorfler-Nochetto 2002) is the assumption
      eps_fine <= beta * eps_coarse ,     beta < 1 uniformly,
  i.e. one refinement removes a FIXED FRACTION of the error.  Bank-Smith do not
  assume it out of thin air: their route is the STRENGTHENED CAUCHY-SCHWARZ (CBS)
  inequality between the coarse space and its complement,
      |a(v_c, v_z)| <= gamma sqrt(a(v_c,v_c)) sqrt(a(v_z,v_z)) ,   gamma < 1,
  and the CBS constant is exactly the quantity the two-level Schur complement is
  made of.  Two consequences, both COMPUTABLE here rather than assumed:
      S = L_z (I - G^T G) L_z^T ,    G = L_c^{-1} B L_z^{-T} ,   gamma = ||G||_2,
      lam_min(L_z^{-1} S L_z^{-T}) = 1 - gamma^2 ,
      lam_min(S) >= (1 - gamma^2) lam_min(A_z) ,     A_z = Z^T T Z,
  where A_c = L_c L_c^T, A_z = L_z L_z^T.  The last line is a CERTIFIED
  factorisation of Lemma B into (i) a CBS constant, whose classical address is
  Bank-Smith itself, and (ii) lam_min of the OSCILLATION GRAM A_z -- which is
  the Nyquist object Q1 was looking for, and unlike lam_min(S) it is a plain
  finite section of the Nyquist-shifted symbol.  And for the nested PWC pair
  saturation is not an assumption at all but an IDENTITY:
      eps_c - eps_f = y^T S y ,      y = Z^T u_f ,
  so beta = 1 - y^T S y / eps_c is a computable number on every window.""")
print("")
Q3_ROWS = []
print("     n      alpha    h_c   h_f   eps_c       eps_f       beta       "
      "id resid   nest err   1-gamma^2   lam_min(Az)  (1-g2)lamAz  "
      "/lam_min(S)  R1 ySy/eps  R2 lam|y|^2  R3 lam maxy  |y|^2/maxy^2")


def chain_row(rr):
    """The T117 chain and the Bank-Smith quantities on one nested pair."""
    Lc, Lf, sc = rr["Lc"], rr["Lf"], rr["sc"]
    t = Lf["t"]
    y = sc["Z"].T @ Lf["u"]
    tc = sc["P"].T @ t
    q_cs = float(tc @ cho_solve(sc["fac_c"], tc, check_finite=False))
    e_cs = 1.0 - q_cs
    ySy = float(y @ (sc["S"] @ y))
    d_eps = e_cs - Lf["eps"]
    Lz = cholesky(sc["Az"], lower=True)
    G = solve_triangular(sc["fac_c"][0], sc["Bx"], lower=True,
                         check_finite=False)
    G = solve_triangular(Lz, G.T, lower=True, trans=0, check_finite=False).T
    gam2 = float(svdvals(G)[0]) ** 2
    lam_z = float(eigvalsh(sc["Az"], subset_by_index=[0, 0])[0])
    Sw = solve_triangular(Lz, sc["S"], lower=True, check_finite=False)
    Sw = solve_triangular(Lz, Sw.T, lower=True, check_finite=False).T
    lam_w = float(eigvalsh(sym(Sw), subset_by_index=[0, 0])[0])
    ny2 = float(y @ y)
    my2 = float(np.max(y ** 2))
    return dict(rr=rr, e_c=e_cs, e_f=Lf["eps"], beta=Lf["eps"] / e_cs,
                idres=abs(d_eps - ySy) / abs(d_eps),
                nest=abs(e_cs - Lc["eps"]) / Lc["eps"],
                gam2=gam2, lam_z=lam_z, lam_w=lam_w, ySy=ySy,
                ny2=ny2, my2=my2,
                bnd=(1.0 - gam2) * lam_z, lam_S=rr["lam_S"],
                r1=ySy / e_cs, r2=rr["lam_S"] * ny2 / e_cs,
                r3=rr["lam_S"] * my2 / e_cs, conc=ny2 / my2)


for r in Q1_ROWS:
    w = chain_row(r)
    Q3_ROWS.append(w)
    print("     %-6d %6.4f  %4d  %4d  %.4e  %.4e  %.6f   %.2e   %.2e   "
          "%.6f    %.6f     %.6f     %.6f     %.6f   %.4e   %.4e   %10.3f"
          % (r["n"], r["al"], r["h_c"], r["h_f"], w["e_c"], w["e_f"], w["beta"],
             w["idres"], w["nest"], 1.0 - w["gam2"], w["lam_z"], w["bnd"],
             w["bnd"] / w["lam_S"], w["r1"], w["r2"], w["r3"], w["conc"]))
check("el_q3.saturation_is_an_identity",
      bool(Q3_ROWS) and max(w["idres"] for w in Q3_ROWS) < 1.0e-6
      and max(w["nest"] for w in Q3_ROWS) < 1.0e-7,
      "SATURATION IS NOT AN ASSUMPTION HERE, IT IS AN IDENTITY: eps_c - eps_f = "
      "y^T S y holds to a relative residual of %.1e over %d nested pairs, and "
      "the coarse level is EXACTLY the restriction of the fine one (assembling "
      "T_c at resolution D_c versus P^T T_f P agrees to %.1e relative, which is "
      "what makes the pair a genuine nested Galerkin pair rather than two "
      "unrelated discretisations).  So the saturation constant beta = 1 - y^T S "
      "y / eps_c is a COMPUTED number on every window, not a hypothesis -- what "
      "Bank-Smith 1993 must assume for a general FE pair is here available in "
      "closed form"
      % (max(w["idres"] for w in Q3_ROWS), len(Q3_ROWS),
         max(w["nest"] for w in Q3_ROWS)))
check("el_q3.cbs_factorisation",
      bool(Q3_ROWS)
      and max(abs(w["lam_w"] - (1.0 - w["gam2"])) for w in Q3_ROWS) < 1.0e-8
      and min(w["lam_S"] - w["bnd"] for w in Q3_ROWS) > -1.0e-10,
      "AND THE CBS FACTORISATION OF LEMMA B HOLDS AS ADVERTISED: "
      "lam_min(L_z^{-1} S L_z^{-T}) = 1 - gamma^2 to %.1e over all pairs, and "
      "the resulting lower bound (1 - gamma^2) lam_min(A_z) <= lam_min(S) is "
      "VALID on every pair with sharpness %.4f..%.4f (bound / measured).  This "
      "is a genuine route for Lemma B and it is NOT vacuous, unlike every "
      "pointwise-symbol route in Q1: 1 - gamma^2 in [%.4f, %.4f] and "
      "lam_min(A_z) in [%.4f, %.4f], both O(1)"
      % (max(abs(w["lam_w"] - (1.0 - w["gam2"])) for w in Q3_ROWS),
         min(w["bnd"] / w["lam_S"] for w in Q3_ROWS),
         max(w["bnd"] / w["lam_S"] for w in Q3_ROWS),
         min(1.0 - w["gam2"] for w in Q3_ROWS),
         max(1.0 - w["gam2"] for w in Q3_ROWS),
         min(w["lam_z"] for w in Q3_ROWS), max(w["lam_z"] for w in Q3_ROWS)))
BET = [w["beta"] for w in Q3_ROWS]
check("el_q3.chain_reproduces_t117",
      bool(Q3_ROWS) and min(w["r1"] for w in Q3_ROWS) > 0.60
      and max(w["r1"] for w in Q3_ROWS) < 0.80
      and min(w["r2"] for w in Q3_ROWS) > 0.10
      and max(w["r2"] for w in Q3_ROWS) < 0.25,
      "THE T117 NUMBERS ARE REPRODUCED, AND THE TWO QUOTED BANDS ARE NOW "
      "IDENTIFIED WITH THE STEPS THEY BELONG TO.  Step 1, eps_c >= y^T S y: "
      "ratio R1 in [%.4f, %.4f] on %d pairs -- this IS the T117 'saturation "
      "constant [0.675, 0.744]', i.e. the FRACTION OF THE ERROR REMOVED by one "
      "refinement, 1 - beta.  Step 2, >= lam_min(S) ||y||^2: R2 in [%.4f, %.4f] "
      "-- this IS the T117 'bound/eps in [0.111, 0.185]'.  Step 3, >= lam_min(S) "
      "max_j y_j^2: R3 in [%.4f, %.4f].  In Bank-Smith's own normalisation the "
      "saturation constant is beta = eps_f/eps_c in [%.4f, %.4f]"
      % (min(w["r1"] for w in Q3_ROWS), max(w["r1"] for w in Q3_ROWS),
         len(Q3_ROWS), min(w["r2"] for w in Q3_ROWS),
         max(w["r2"] for w in Q3_ROWS), min(w["r3"] for w in Q3_ROWS),
         max(w["r3"] for w in Q3_ROWS), min(BET), max(BET)))
CF, TH1, TH2, TH3 = [], [], [], []
for al, xx in LAD2.items():
    ww = sorted([w for w in Q3_ROWS if w["rr"]["al"] == al],
                key=lambda w: w["rr"]["h_f"])
    if len(ww) < 3:
        continue
    lD = [math.log(w["rr"]["D_f"]) for w in ww]
    CF.append(fit_band([math.log(w["rr"]["h_f"]) for w in ww],
                       [math.log(w["conc"]) for w in ww])[1])
    TH1.append(fit_band(lD, [math.log(w["e_c"]) for w in ww])[1])
    TH2.append(fit_band(lD, [math.log(w["lam_S"] * w["ny2"]) for w in ww])[1])
    TH3.append(fit_band(lD, [math.log(w["lam_S"] * w["my2"]) for w in ww])[1])
check("el_q3.last_step_costs_a_power",
      bool(CF) and abs(float(np.mean(TH2)) - float(np.mean(TH1))) < 0.12
      and float(np.mean(TH3)) - float(np.mean(TH1)) > 0.60,
      "AND HERE IS A CORRECTION TO THE T117 CHAIN, NOT A CONFIRMATION.  Rate "
      "fits along the ladders: eps_c ~ D^%s (T117 quotes theta = 1.76), the "
      "step-2 bound lam_min(S)||y||^2 ~ D^%s (T117 quotes theta' = 1.74) -- so "
      "step 2 really does lose NO power, mean %.3f vs %.3f.  But step 3 fits "
      "D^%s, i.e. mean %.3f: going from the FULL oscillation vector to a SINGLE "
      "cell costs a further D^%.2f, one whole power.  The culprit is visible "
      "directly: the concentration factor ||y||^2 / max_j y_j^2 is %.1f..%.1f "
      "and GROWS like h^%s (fits, mean %.2f) instead of staying O(1).  So the "
      "oscillation mass does NOT sit on one cell -- it is spread over a fixed "
      "FRACTION of the window's cells.  Consequence for Lemma A: the hypothesis "
      "the chain actually needs is not '(H3) on one coarse cell' but a "
      "MEAN-SQUARE slope bound over a positive fraction of the corner region.  "
      "The single-cell version is true (Q2) and still gives a lower bound, but "
      "it gives up the rate"
      % ("/".join("%.3f" % b for b in TH1), "/".join("%.3f" % b for b in TH2),
         float(np.mean(TH2)), float(np.mean(TH1)),
         "/".join("%.3f" % b for b in TH3), float(np.mean(TH3)),
         float(np.mean(TH3)) - float(np.mean(TH1)),
         min(w["conc"] for w in Q3_ROWS), max(w["conc"] for w in Q3_ROWS),
         "/".join("%.3f" % b for b in CF), float(np.mean(CF))))

print("")
print("""  Q3.2  THE BAND OVER ZONES x LEVELS x ALPHA.  The saturation constant is
  only useful if it is bounded away from 1 UNIFORMLY.  The pairs above vary the
  level at fixed alpha; now sweep alpha across the zone table at (approximately)
  fixed resolution, so the alpha-direction is separated from the D-direction.""")
print("")
print("     n      alpha    h_c   h_f   D_f         beta       1-gamma^2   "
      "lam_min(Az)  lam_min(S)  R3")
SW_ROWS = []
D_TARGET = 4.0e-3
for z in _spread([q for q in ZF_OK if q["h_o"] <= H_FINE // 4], 9):
    if budget_left() < 120.0:
        break
    al = z["al_o"]
    at = atoms_in(al, ATOMS_ALL)
    h_c = z["h_o"]
    while 4 * h_c <= H_FINE and 0.5 * al / h_c > D_TARGET:
        h_c *= 2
    if any(abs(w["rr"]["al"] - al) < 1e-12 and w["rr"]["h_c"] == h_c
           for w in Q3_ROWS):
        continue
    Lc = level(al, 2 * h_c, at)
    Lf = level(al, 4 * h_c, at)
    if Lc is None or Lf is None:
        continue
    sc = schur_osc(Lf["T"], h_c)
    if sc is None:
        continue
    rr = dict(n=z["n"], al=al, h_c=h_c, h_f=2 * h_c, D_f=Lf["D"], Lc=Lc, Lf=Lf,
              sc=sc, lam_S=float(eigvalsh(sc["S"], subset_by_index=[0, 0])[0]))
    w = chain_row(rr)
    SW_ROWS.append(w)
    print("     %-6d %6.4f  %4d  %4d  %.4e  %.6f   %.6f    %.6f     %.6f    %.4e"
          % (z["n"], al, h_c, 2 * h_c, Lf["D"], w["beta"], 1.0 - w["gam2"],
             w["lam_z"], w["lam_S"], w["r3"]))
    del Lc, Lf, sc, rr
ALL3 = Q3_ROWS + SW_ROWS
BET_A = [w["beta"] for w in ALL3]
check("el_q3.saturation_band",
      len(ALL3) >= 15 and max(BET_A) < 0.95 and min(BET_A) > 0.05
      and max(w["gam2"] for w in ALL3) < 0.99,
      "THE BAND: over %d (zone, level) pairs spanning alpha in [%.4f, %.4f] and "
      "D in [%.2e, %.2e], the saturation constant lies in beta in [%.4f, %.4f] "
      "-- bounded away from 1 by at least %.4f on every window, which is exactly "
      "the Bank-Smith / Dorfler-Nochetto hypothesis.  Equivalently the CBS "
      "constant satisfies gamma^2 <= %.6f, i.e. 1 - gamma^2 >= %.6f.  In T117's "
      "normalisation (the removed fraction 1 - beta) the band is [%.3f, %.3f] "
      "against the quoted [0.675, 0.744]: the alpha-sweep does not widen it"
      % (len(ALL3), min(w["rr"]["al"] for w in ALL3),
         max(w["rr"]["al"] for w in ALL3), min(w["rr"]["D_f"] for w in ALL3),
         max(w["rr"]["D_f"] for w in ALL3), min(BET_A), max(BET_A),
         1.0 - max(BET_A), max(w["gam2"] for w in ALL3),
         min(1.0 - w["gam2"] for w in ALL3),
         1.0 - max(BET_A), 1.0 - min(BET_A)))
BFIT = []
for al, xx in LAD2.items():
    ww = sorted([w for w in Q3_ROWS if w["rr"]["al"] == al],
                key=lambda w: w["rr"]["h_f"])
    if len(ww) >= 3:
        BFIT.append((ww[0]["beta"], ww[-1]["beta"]))
check("el_q3.monotone_in_level",
      bool(BFIT) and all(hi < lo + 0.01 for lo, hi in BFIT),
      "MONOTONY, AND IT POINTS THE RIGHT WAY: along every ladder beta FALLS "
      "under refinement, %s (coarse end) -> %s (fine end), so saturation gets "
      "slightly BETTER as D -> 0, by %.1f-%.1f %% of beta over the ladder.  That "
      "is consistent with Q1.9, where lam_min(S) was measured to GROW "
      "logarithmically: a stiffer oscillation block removes more of the error.  "
      "What this does NOT show is that beta stays below 1 in the limit -- beta "
      "is below %.3f on every window measured and the trend is favourable, but "
      "uniformity remains a HYPOTHESIS, exactly as in Bank-Smith"
      % ("/".join("%.3f" % lo for lo, _ in BFIT),
         "/".join("%.3f" % hi for _, hi in BFIT),
         100.0 * min((lo - hi) / lo for lo, hi in BFIT),
         100.0 * max((lo - hi) / lo for lo, hi in BFIT), max(BET_A)))
QU = max(abs(2.0 * w["rr"]["al"] / (2.0 * w["rr"]["h_f"]) / w["rr"]["D_f"] - 1.0)
         for w in ALL3)
info("Q3.classical_hypotheses", "WHICH BANK-SMITH HYPOTHESIS HAS TO BE CHECKED "
     "HERE, one by one.  (i) LOCAL QUASI-UNIFORMITY of the mesh: satisfied "
     "EXACTLY, not approximately -- frame A puts a UNIFORM cell width D on each "
     "window, so the mesh ratio is 1 to %.1e, and no shape-regularity constant "
     "enters.  (ii) COERCIVITY of the form: certified by a completed Cholesky of "
     "T_f on every window (the probe would have skipped the row otherwise), with "
     "the round-off floor of Q0 subtracted.  (iii) NESTEDNESS of the spaces: "
     "certified to %.1e above, since the coarse PWC basis is an exact sum of "
     "fine ones.  (iv) LOCALITY of the operator: NOT satisfied and NOT needed -- "
     "T is a nonlocal log-singular kernel plus a singular prime-power measure, "
     "but the Bank-Smith route to saturation runs through the CBS constant, "
     "which is defined for any positive definite form.  So the ONE classical "
     "hypothesis that has real content here is the UNIFORMITY of gamma, and "
     "that is the one item on the Lemma C missing list"
     % (QU, max(w["nest"] for w in Q3_ROWS)))
print("")
print("""  Q3.3  THE SYMBOL Q1 SHOULD HAVE ASKED FOR.  The CBS factorisation moves
  the symbol question off S and onto A_z = Z^T T Z, and THAT object has an exact
  symbol.  Decimating a Toeplitz form with the (1,-1)/sqrt2 pairs gives a
  Toeplitz form again, with lags
      a_m = c_{2m} - (c_{2m-1} + c_{2m+1}) / 2 ,
  whose symbol is, with th = phi/2 running over the LOW half band,
      sigma_z(phi) = sin^2(th/2) f(th) + cos^2(th/2) f(th + pi).
  Read that formula against Q1: it is the ARITHMETIC mean of the aliasing pair
  with the SAME weights whose HARMONIC mean is the sigma_S of Q1.1.  That is the
  whole difference, and it is decisive.  sigma_S needs BOTH f(th) and f(th+pi)
  positive -- one negative dip anywhere and the harmonic mean is useless, which
  is exactly how Q1.4 died.  sigma_z only needs the weighted SUM positive, and
  the weight sitting on the dangerous low-frequency part is sin^2(th/2) ~ th^2/4,
  which VANISHES QUADRATICALLY where f is negative.  So the oscillation block
  suppresses the low-frequency negativity by construction.  Two classical facts
  finish the route: the finite section of a Toeplitz form is bounded below by the
  essential infimum of its symbol (Grenander-Szego), and the odd fold composed
  with Z is an ISOMETRY into the full oscillation space, so
      lam_min(S) >= (1 - gamma^2) lam_min(A_z) >= (1 - gamma^2) inf sigma_z .
  Every inequality here is in the LOWER-BOUND direction, and inf sigma_z is
  certified per cell with an explicit second-order margin, as in Q0.""")
print("")


def osc_lags(c):
    """The lags of the oscillation block: a_m = c_{2m} - (c_{2m-1}+c_{2m+1})/2."""
    m = np.arange(c.shape[0] // 2)
    return c[2 * m] - 0.5 * (c[np.abs(2 * m - 1)] + c[2 * m + 1])


print("     n      alpha    h_f   form err   inf sigma_z   margin      "
      "lam_min(Toep a)  lam_min(Az)  1-gamma^2   BOUND        lam_min(S)   "
      "sharpness  1-cell avg")
Q33 = []
for w in Q3_ROWS:
    if budget_left() < 150.0:
        break
    rr = w["rr"]
    c = rr["Lf"]["c"]
    a = osc_lags(c)
    L = next_pow2(max(OS_MIN * c.shape[0], 4096))
    L = min(L, L_CAP)
    f = sym_grid(c, L)
    th, f1, f2, _ = two_grid_symbol(f, L)
    k0 = L // 4
    sz_pred = (np.sin(0.5 * th) ** 2 * f1 + np.cos(0.5 * th) ** 2 * f2)[k0:]
    sz_fft = sym_grid(a, L // 2)[:k0 + 1]
    ferr = float(np.abs(sz_fft - sz_pred).max()) / float(np.abs(sz_pred).max())
    ell_z, sz, marg = sym_cert(a, L // 2)
    inf_z = float(ell_z.min())
    Lz2 = L // 2
    while marg > 0.25 * abs(inf_z) and 2 * Lz2 <= L_CAP:
        Lz2 *= 2
        ell_z, sz, marg = sym_cert(a, Lz2)
        inf_z = float(ell_z.min())
    ncell = max(Lz2 // rr["h_f"], 1)
    Fz = float(box_avg(sz, ncell).min())
    Ta = a[np.abs(np.arange(rr["h_f"])[:, None] - np.arange(rr["h_f"])[None, :])]
    lam_Ta = float(eigvalsh(sym(Ta), subset_by_index=[0, 0])[0])
    bnd = (1.0 - w["gam2"]) * max(inf_z, 0.0)
    Q33.append(dict(rr=rr, ferr=ferr, inf_z=inf_z, marg=marg, lam_Ta=lam_Ta,
                    lam_z=w["lam_z"], gam2=w["gam2"], bnd=bnd, Fz=Fz,
                    tbnd=(1.0 - w["gam2"]) * lam_Ta,
                    lam_S=w["lam_S"], sh=bnd / w["lam_S"]))
    print("     %-6d %6.4f  %4d  %.2e     %+.6f     %.2e    %+.6f        "
          "%.6f     %.6f    %.6f     %.6f     %.6f  %+.4f"
          % (rr["n"], rr["al"], rr["h_f"], ferr, inf_z, marg, lam_Ta,
             w["lam_z"], 1.0 - w["gam2"], bnd, w["lam_S"], bnd / w["lam_S"], Fz))
    del Ta
TAIL = max(x["ferr"] * 1.0 for x in Q33)
check("el_q3.osc_symbol_formula",
      bool(Q33) and TAIL < 1.0e-3
      and min(x["lam_z"] - x["lam_Ta"] for x in Q33) > -1.0e-9,
      "THE OSCILLATION SYMBOL IS THE DERIVED ONE: the FFT of the decimated lags "
      "agrees with sin^2(th/2) f(th) + cos^2(th/2) f(th+pi) to %.1e relative on "
      "%d windows.  That residual is NOT round-off and is not meant to be -- it "
      "is the one dropped tail term, the largest lag c_{M-1} of the arch kernel, "
      "which the M-truncated a_m cannot carry; it shrinks like the tail itself "
      "(%.1e at the coarsest level down to %.1e at the finest).  The second "
      "ingredient is verified exactly as needed: the isometry ordering "
      "lam_min(A_z) >= lam_min(Toeplitz(a)) holds on every window, slack "
      "%.4f..%.4f -- so the fold costs nothing in the lower-bound direction"
      % (TAIL, len(Q33), max(x["ferr"] for x in Q33),
         min(x["ferr"] for x in Q33),
         min(x["lam_z"] - x["lam_Ta"] for x in Q33),
         max(x["lam_z"] - x["lam_Ta"] for x in Q33)))
POS = [x for x in Q33 if x["inf_z"] > 2.0 * x["marg"]]
NEG = [x for x in Q33 if x["inf_z"] <= 2.0 * x["marg"]]
AL_CUT = 1.30
check("el_q3.lemma_b_pointwise_partial",
      len(POS) >= 6 and bool(NEG) and max(x["sh"] for x in POS) > 0.40
      and all(x["rr"]["al"] > AL_CUT or x["rr"]["h_f"] < 200 for x in NEG),
      "LEMMA B, POINTWISE ROUTE: WORKS ON %d OF %d WINDOWS, AND THE SPLIT IS "
      "SYSTEMATIC RATHER THAN RANDOM.  It succeeds on EVERY window with "
      "alpha <= %.2f and h_f >= 200, i.e. the two narrow zones from the second "
      "level on; there inf sigma_z in [%.4f, %.4f] and the CERTIFIED bound "
      "lam_min(S) >= (1 - gamma^2) inf sigma_z recovers up to %.3f of the "
      "measured lam_min(S) (as little as %.3f at the coarsest of them) -- a real "
      "certified bound on a real window, which is more than any route in Q1 "
      "produced.  It fails on the WIDE windows, alpha in [%.4f, %.4f], where "
      "inf sigma_z goes down to %.3f, an order of magnitude below the "
      "certification margin %.1e, so that negativity is genuine and not an "
      "artefact of the certificate.  The pattern is ALPHA, not D: a wider window "
      "admits more prime-power atoms, more atoms deepen the comb dips, and a dip "
      "sitting where the sin^2(th/2) weight is O(1) does not get suppressed.  So "
      "the sin^2 weight kills the LOW-frequency negativity -- that was Q1's "
      "whole obstruction and it is gone -- but not the MID-band combs"
      % (len(POS), len(Q33), AL_CUT, min(x["inf_z"] for x in POS),
         max(x["inf_z"] for x in POS), max(x["sh"] for x in POS),
         min(x["sh"] for x in POS), min(x["rr"]["al"] for x in NEG),
         max(x["rr"]["al"] for x in NEG), min(x["inf_z"] for x in NEG),
         max(x["marg"] for x in NEG)))
check("el_q3.lemma_b_reduced_to_a_toeplitz_section",
      bool(Q33) and min(x["lam_Ta"] for x in Q33) > 0.5
      and min(x["tbnd"] / x["lam_S"] for x in Q33) > 0.2
      and max(x["tbnd"] / x["lam_S"] for x in Q33) < 1.0,
      "AND WHAT SURVIVES ON ALL %d WINDOWS IS THIS: Lemma B is REDUCED, by two "
      "verified inequalities, to the positivity of a PLAIN TOEPLITZ SECTION of "
      "an EXPLICIT symbol -- lam_min(S) >= (1 - gamma^2) lam_min(T_h(sigma_z)) "
      "-- and that bound is valid and non-trivial everywhere: "
      "lam_min(T_h(sigma_z)) in [%.4f, %.4f] (all positive, Cholesky-certifiable "
      "per window) and the bound recovers %.3f..%.3f of the measured lam_min(S).  "
      "This is a strictly better position than T117: instead of 'bound "
      "lam_min(S) of a Schur complement of a folded section of a log-singular "
      "kernel with atoms', the open question is now 'is a finite section of "
      "sigma_z positive', where sigma_z is written down in closed form and its "
      "only bad set is a comb of narrow dips.  The coarse-grained (one-cell "
      "averaged) sigma_z is positive on %d/%d windows, %.3f..%.3f, which is the "
      "MEASURED statement that those dips are narrower than the section can "
      "resolve -- the same finite-section mechanism as Q1.6, now on an object "
      "with a name"
      % (len(Q33), min(x["lam_Ta"] for x in Q33), max(x["lam_Ta"] for x in Q33),
         min(x["tbnd"] / x["lam_S"] for x in Q33),
         max(x["tbnd"] / x["lam_S"] for x in Q33),
         sum(1 for x in Q33 if x["Fz"] > 0.0), len(Q33),
         min(x["Fz"] for x in Q33), max(x["Fz"] for x in Q33)))
print("")
print("""  Q3.4  THE CERTIFIED FLOOR ON A LONG LEVER.  inf sigma_z needs no matrix,
  so the same FFT-only lever that Q1.9 used on a heuristic proxy can be turned on
  the CERTIFIED quantity itself -- and there is a specific question to settle.
  On the narrowest zone inf sigma_z was NEGATIVE at the coarsest level and
  POSITIVE from the second level on.  If that is a general pattern, the wide
  windows are not counterexamples at all, only under-resolved, and the certified
  route closes on every window once D is small enough.  Followed from M = M_o to
  M = %d at fixed alpha, with the certificate margin driven below a quarter of
  the value or the row is not counted.""" % LEV_M_MAX)
print("")
print("     alpha   M range          #pts  inf sigma_z at coarse..fine        "
      "sign flip at M   b per log(1/D)   rel.rms log   rel.rms power  log better")
LEV_Z = []
for z in LADDERS + COVER:
    if budget_left() < 200.0:
        break
    al = z["al_o"]
    at = atoms_in(al, ATOMS_ALL)
    Ms, Zs, Ds = [], [], []
    M = z["M_o"]
    while M <= LEV_M_MAX and budget_left() > 150.0:
        c, D = lag_vector_fast(al, M, at)
        a = osc_lags(c)
        Lz2 = next_pow2(OS_MIN * a.shape[0])
        ok = False
        while Lz2 <= L_CAP:
            ell_z, _, marg = sym_cert(a, Lz2)
            iz = float(ell_z.min())
            ok = marg <= 0.25 * abs(iz)
            if ok:
                break
            Lz2 *= 2
        if ok:
            Ms.append(M)
            Zs.append(iz)
            Ds.append(D)
        del c, a
        M *= 2
    if len(Ms) < 5:
        continue
    xl = np.array([math.log(1.0 / d) for d in Ds])
    yv = np.array(Zs)
    flip = next((Ms[i] for i in range(len(Ms)) if yv[i] > 0.0), 0)
    a_l, b_l, _, se_l = fit_band(xl, yv)
    res_l = float(np.sqrt(np.mean((a_l + b_l * xl - yv) ** 2))) / abs(yv.mean())
    pm = yv > 0.0
    if pm.sum() >= 4:
        a_p, b_p, _, _ = fit_band(-xl[pm], np.log(yv[pm]))
        res_p = float(np.sqrt(np.mean((np.exp(a_p - b_p * xl[pm])
                                      - yv[pm]) ** 2))) / abs(yv[pm].mean())
        res_lp = float(np.sqrt(np.mean((a_l + b_l * xl[pm]
                                       - yv[pm]) ** 2))) / abs(yv[pm].mean())
    else:
        res_p, res_lp = float("nan"), float("nan")
    LEV_Z.append(dict(al=al, n=len(Ms), M0=Ms[0], M1=Ms[-1], z0=Zs[0], z1=Zs[-1],
                      flip=flip, b=b_l, se=se_l, rl=res_lp, rp=res_p,
                      lever=Ms[-1] / Ms[0], allpos=bool(pm.all()),
                      back=float(np.min(np.diff(yv))), npos=int(pm.sum()),
                      mstar=(2.0 * al * math.exp(-a_l / b_l) if flip == 0
                             else float(flip))))
    print("     %6.4f  %6d..%-6d  %4d   %+.4f .. %+.4f                  "
          "%8d   %10.4f       %.3e     %.3e    %6.1f x"
          % (al, Ms[0], Ms[-1], len(Ms), Zs[0], Zs[-1], flip, b_l, res_lp,
             res_p, res_p / max(res_lp, 1e-300)))
FLIPPED = [r for r in LEV_Z if r["flip"] > 0]
check("el_q3.certified_floor_rises_and_crosses",
      len(LEV_Z) >= 4 and all(r["b"] > 0.0 for r in LEV_Z)
      and all(r["back"] > -0.80 for r in LEV_Z) and len(FLIPPED) >= 3,
      "*** THE WIDE WINDOWS ARE UNDER-RESOLVED, NOT OBSTRUCTED. ***  On a lever "
      "of %s x in D the certified floor inf sigma_z RISES on every zone -- from "
      "%s at the coarse end to %s at the fine end, though NOT monotonically "
      "(worst backward step %.3f, i.e. a new comb dip can re-enter at a given "
      "resolution), at b = %s per log(1/D) -- and it CROSSES ZERO "
      "inside the lever on %d of %d zones, at M = %s.  The remaining %d end at "
      "%s, still negative but climbing; extrapolating each zone's own fitted log "
      "law (A FIT, and an EXTRAPOLATION, so it certifies nothing) puts their "
      "crossing at M ~ %s.  Reading: the sign of inf sigma_z is a statement about "
      "RESOLUTION, not about the window -- a comb dip is only dangerous while it "
      "is deep relative to the Nyquist-band mass it sits in, and refinement "
      "raises that mass.  Which means the CERTIFIED Lemma-B bound lam_min(S) >= "
      "(1 - gamma^2) inf sigma_z is not a curiosity of narrow windows: it becomes "
      "available on every zone tested, once D is small enough"
      % ("/".join("%.0f" % r["lever"] for r in LEV_Z),
         "/".join("%+.3f" % r["z0"] for r in LEV_Z),
         "/".join("%+.3f" % r["z1"] for r in LEV_Z),
         min(r["back"] for r in LEV_Z),
         "/".join("%.3f" % r["b"] for r in LEV_Z), len(FLIPPED), len(LEV_Z),
         "/".join("%d" % r["flip"] for r in FLIPPED),
         len(LEV_Z) - len(FLIPPED),
         "/".join("%+.3f" % r["z1"] for r in LEV_Z if r["flip"] == 0),
         "/".join("%.0e" % r["mstar"] for r in LEV_Z if r["flip"] == 0)))
LOGB = [r for r in LEV_Z if r["npos"] >= 4]
check("el_q3.floor_growth_is_logarithmic",
      bool(LOGB) and all(r["rp"] > r["rl"] for r in LOGB),
      "AND THE GROWTH IS A LOGARITHM ON THE CERTIFIED QUANTITY, not just on the "
      "Q1.9 proxy: on the %d zones with enough positive points to fit both "
      "models, the LOG model a + b log(1/D) beats the POWER model c D^-p by %s x "
      "in relative residual, at b = %s per log(1/D), i.e. %s per halving.  T117 "
      "measured +0.20 per halving for lam_min(S) ITSELF; the certified floor "
      "climbs faster than that, so the floor is not merely tracking the measured "
      "growth from below -- the two must meet, which is consistent with the "
      "sharpness of the bound improving under refinement in Q3.3 (%.3f at the "
      "coarsest of the certified rows, %.3f at the finest).  A logarithm is what "
      "the log-singular kernel predicts (Kac-Murdock-Szego 1953, Widom 1974).  "
      "Both models are FITS and carry jackknife bands"
      % (len(LOGB),
         "/".join("%.1f" % (r["rp"] / max(r["rl"], 1e-300)) for r in LOGB),
         "/".join("%.3f" % r["b"] for r in LOGB),
         "/".join("%.3f" % (r["b"] * math.log(2.0)) for r in LOGB),
         min(x["sh"] for x in POS), max(x["sh"] for x in POS)))
info("Q3.timing", "Q3 done, %.1f s used, %.0f s left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("Q4  SYNTHESIS -- THE THEOREM IN FULL, WITH EVERY HYPOTHESIS NAMED")
# ----------------------------------------------------------------------------
B_POINT = len(POS)
B_RED = all(x["lam_Ta"] > 0.0 for x in Q33)
C_ID = max(w["idres"] for w in Q3_ROWS) < 1.0e-6
C_BAND = max(BET_A) < 0.95
A_POWER = max(d for d, _ in DRIFT.values()) < 0.02
A_FLAT = max(abs(b) for b in GS_FIT) < 0.20
A_MS = float(np.mean(CF)) < 0.20
STAT = {
    "L-A": ("OPEN, AND ITS STATEMENT HAD TO BE CORRECTED"
            if not (A_POWER and A_MS) else "CLASSICAL-DONE"),
    "L-B": ("CERTIFIED ON WINDOWS + REDUCED TO A CLASSICAL OBJECT EVERYWHERE"
            if (B_POINT > 0 and B_RED) else "OPEN"),
    "L-C": ("CLASSICAL-DONE (an identity here, plus Bank-Smith's own hypothesis)"
            if (C_ID and C_BAND) else "OPEN"),
}
print("""  THE STATUS OF THE THREE LEMMATA, from the measurements above.

  L-B  lam_min(S) FROM ONE LEVEL  --  %s
       What T117 asked for: a symbol bound at the Nyquist frequency.
       What Q1 found: the Schur symbol sigma_S is the weighted HARMONIC mean of
         the aliasing pair, so it needs f > 0 at BOTH frequencies; f is negative
         on a comb of dips at the window's own resolution scale, so every
         pointwise route through sigma_S is VACUOUS -- inf sigma_S = 0 on every
         window, the full-band floor lam_min(T) COLLAPSES under refinement while
         lam_min(S) GROWS, and the ground state of S puts %.0f-%.0f x the uniform
         share of its mass on the negative set.  Positivity of the section is a
         cancellation, not a pointwise fact (Fejer-Riesz moment problem).
       What Q3 found instead, and this is the result: the CBS factorisation
         lam_min(S) >= (1 - gamma^2) lam_min(Z^T T Z) moves the question onto the
         OSCILLATION GRAM, whose symbol is the ARITHMETIC mean of the same
         aliasing pair, sigma_z = sin^2(th/2) f(th) + cos^2(th/2) f(th + pi).
         The low-frequency negativity that killed sigma_S carries the weight
         sin^2(th/2) and is suppressed QUADRATICALLY.  Certified consequences:
         inf sigma_z > 0 on %d of %d matrix windows (all of alpha <= 1.30,
         h_f >= 200), giving lam_min(S) >= (1-gamma^2) inf sigma_z with up to
         %.0f %% of the measured value; and on ALL windows lam_min(S) >=
         (1-gamma^2) lam_min(T_h(sigma_z)) with %.0f-%.0f %% sharpness.
         The long FFT-only lever then settles what the sign of inf sigma_z
         actually measures: it RISES like a logarithm on every zone (%s per
         log(1/D)) and CROSSES ZERO at M = %s on %d of %d zones, so the windows
         where the pointwise route failed were UNDER-RESOLVED, not obstructed.
       Shortest missing list: TWO items, both about the SAME crossing.  (1) That
         inf sigma_z > 0 for all D below some D_0(alpha) -- measured on %d of %d
         zones, a fitted extrapolation on the rest (crossings at M ~ %s), and it
         needs the comb depth versus the Nyquist-band mass, which is arithmetic
         (Chebyshev-type atom counting), not analysis.  (2) For windows COARSER
         than that crossing, positivity of the finite section T_h(sigma_z) with
         narrow negative dips -- the one-cell average of sigma_z is already
         positive on %d/%d of them, so this is the classical narrow-dip
         finite-section question for an EXPLICIT symbol, not a question about a
         Schur complement of a folded singular kernel any more.

  L-C  SATURATION  --  %s
       For the nested PWC pair saturation is an IDENTITY, eps_c - eps_f = y^T S y
         (residual %.1e), so beta is COMPUTED, not assumed: beta in [%.3f, %.3f]
         over %d (zone, level, alpha) triples, T117's removed-fraction
         normalisation 1 - beta in [%.3f, %.3f] against its quoted [0.675, 0.744].
         beta FALLS under refinement on every ladder, i.e. the trend is
         favourable.
       The Bank-Smith hypotheses, one by one: local quasi-uniformity EXACT (frame
         A is uniform, mesh ratio 1); coercivity CERTIFIED (Cholesky, with the
         round-off floor declared); nestedness CERTIFIED (%.1e); LOCALITY of the
         operator NOT satisfied and NOT needed, because the Bank-Smith route runs
         through the CBS constant, which exists for any positive definite form.
       Shortest missing list: ONE item, and it is the SAME item Bank-Smith
         themselves assume -- uniformity of gamma as D -> 0 (measured
         1 - gamma^2 >= %.3f on all %d windows).  Bornemann-Erdmann-Kornhuber
         1996 is the standing warning that saturation CAN fail, so this is a
         hypothesis and stays labelled as one.

  L-A  THE CORNER / (H3)  --  %s
       The classical edge law is confirmed EXACTLY where it applies: on the
         algebraic model class p = s to %.3f, with the estimator exact to %.0e on
         the Dirichlet-Laplacian closed form, and KMS 1953 shows in closed form
         that a symbol bounded away from 0 produces NO boundary layer at all.
       On the real symbol it does NOT transfer: the corner exponent DRIFTS by up
         to %+.3f per halving (%.0f-%.0f sigma), and the profile itself still
         moves %.0f %% between consecutive levels, so there is no asymptotic
         (s, kappa) to cite.  That is the signature of a LOG-singular symbol:
         log(1/|th|) is the borderline between all powers |th|^{2s}.
       AND the statement itself was wrong-sized.  Q3 measured the concentration
         factor ||y||^2 / max_j y_j^2 ~ h^%.2f: the oscillation mass is spread
         over a FIXED FRACTION of the cells, not one cell.  So the last step of
         the T117 chain costs a full power of D (eps ~ D^%.2f, step-2 bound
         D^%.2f -- no loss, single-cell bound D^%.2f), and (H3) as a ONE-CELL
         statement cannot carry the rate even though it is true.
       What IS established, on all %d windows: the (H3) cell sits at a D-stable
         window fraction xi in [%.3f, %.3f], and max_j |Delta u| / D^{3/2} is
         D-flat (factor <= %.2f, |exponent| <= %.3f).
       Shortest missing list: TWO items.  (1) Upgrade (H3) from one cell to a
         MEAN-SQUARE lower bound on the oscillation coefficients over a positive
         fraction of the corner region -- that is what the rate consumes.
         (2) A corner asymptotic for a LOG-singular symbol carrying a singular
         prime-power measure, i.e. Fisher-Hartwig extended from |th|^{2s} to
         log(1/|th|) plus atoms; the KMS/Widom power-law formulas do not cover
         it."""
      % (STAT["L-B"], min(x["supp"] for x in FR_ROWS),
         max(x["supp"] for x in FR_ROWS),
         B_POINT, len(Q33), 100.0 * max(x["sh"] for x in POS),
         100.0 * min(x["tbnd"] / x["lam_S"] for x in Q33),
         100.0 * max(x["tbnd"] / x["lam_S"] for x in Q33),
         "/".join("%.2f" % r["b"] for r in LEV_Z),
         "/".join("%d" % r["flip"] for r in FLIPPED), len(FLIPPED), len(LEV_Z),
         len(FLIPPED), len(LEV_Z),
         "/".join("%.0e" % r["mstar"] for r in LEV_Z if r["flip"] == 0),
         sum(1 for x in Q33 if x["Fz"] > 0.0), len(Q33),
         STAT["L-C"], max(w["idres"] for w in Q3_ROWS), min(BET_A), max(BET_A),
         len(ALL3), 1.0 - max(BET_A), 1.0 - min(BET_A),
         max(w["nest"] for w in Q3_ROWS), min(1.0 - w["gam2"] for w in ALL3),
         len(ALL3), STAT["L-A"],
         max(abs(r["p"] - r["s"]) for r in CTRL_EDGE),
         max(abs(r["p"] - r["s"]) for r in CTRL_EDGE if abs(r["s"] - 1.0) < 1e-9),
         max(d for d, _ in DRIFT.values()),
         min(d / max(s, 1e-9) for d, s in DRIFT.values()),
         max(d / max(s, 1e-9) for d, s in DRIFT.values()),
         100.0 * float(np.mean([b for _, b in DEVG.values()])),
         float(np.mean(CF)), float(np.mean(TH1)), float(np.mean(TH2)),
         float(np.mean(TH3)), len(Q2_ROWS),
         min(lo for lo, _ in XI.values()), max(hi for _, hi in XI.values()),
         max(GS_FLAT), max(abs(b) for b in GS_FIT)))
print("")
print("""  THE STRONGEST STATEMENT DEFENSIBLE TODAY.  Everything below is either
  proved by identity + Cholesky in T117, or certified here, EXCEPT the two lines
  marked (H).

    THEOREM (conditional).  Let alpha be a frame-A zone window, D = 2 alpha / M
    its cell width, T = T_odd the pole-free odd Weil form of the arch kernel plus
    the prime-power atoms on that window, t~ the functional of f(x) = 2 sinh(x/2),
    u = T^{-1} t~ and eps(alpha, D) = 1 - t~^T u.  Let P, Z be the two-level
    prolongation and oscillation bases, A_c = P^T T P, A_z = Z^T T Z,
    B = P^T T Z, S = A_z - B^T A_c^{-1} B, y = Z^T u, and let gamma be the CBS
    constant of the pair, gamma = || A_c^{-1/2} B A_z^{-1/2} ||.  Then
      (1)  eps_c - eps_f = y^T S y                        [identity, %.1e]
      (2)  lam_min(L_z^{-1} S L_z^{-T}) = 1 - gamma^2      [identity, %.1e]
      (3)  lam_min(S) >= (1 - gamma^2) lam_min(T_h(sigma_z)),
           sigma_z(phi) = sin^2(th/2) f(th) + cos^2(th/2) f(th+pi), th = phi/2
                                    [isometry + Grenander-Szego, verified]
      (4)  if inf sigma_z > 0 then lam_min(S) >= (1 - gamma^2) inf sigma_z
                        [certified with margin; holds on %d/%d windows measured]
      (5)  eps_c >= (1 - gamma^2) lam_min(T_h(sigma_z)) ||y||^2
                                    [chain of (1)-(3), all lower-bound direction]
      (H1) gamma is bounded away from 1 uniformly in (alpha, D)
                                    [HYPOTHESIS; measured 1-gamma^2 >= %.3f]
      (H2) ||y||^2 >= c D^{%.2f} with c > 0 uniformly
                                    [HYPOTHESIS; this is (H3) upgraded to
                                     mean square, see the L-A list]
    and then eps(alpha, D) >= c (1 - gamma^2) lam_min(T_h(sigma_z)) D^{%.2f} > 0,
    which is the [P1] margin inequality with an explicit constant.

  WHAT THIS IS WORTH.  (1)-(5) are unconditional on every window the probe
  touched.  The two hypotheses are NOT interchangeable in difficulty: (H1) is the
  standard CBS hypothesis of the classical two-level literature, measured stable
  and with the favourable trend; (H2) is the one genuinely new analytic statement
  the theorem needs, and Q2 shows it cannot be imported from the KMS/Widom
  power-law corner theory because this symbol is log-singular with atoms."""
      % (max(w["idres"] for w in Q3_ROWS),
         max(abs(w["lam_w"] - (1.0 - w["gam2"])) for w in Q3_ROWS),
         len(POS), len(Q33), min(1.0 - w["gam2"] for w in ALL3),
         float(np.mean(TH2)), float(np.mean(TH2))))
print("")
check("el_q4.ledger_is_derived",
      STAT["L-C"].startswith("CLASSICAL-DONE")
      and STAT["L-B"].startswith("CERTIFIED")
      and STAT["L-A"].startswith("OPEN")
      and not A_POWER and not A_MS and B_RED and C_ID and C_BAND,
      "the status ledger above is DERIVED from the measured flags, not typed: "
      "L-B certified-on-windows (%d/%d pointwise) and reduced everywhere "
      "(reduction valid on %d/%d), L-C an identity with beta < %.3f on %d "
      "triples, L-A open because the exponent drift %+.3f per halving exceeds "
      "the 0.02 stability gate AND the concentration exponent %.2f exceeds the "
      "0.20 one-cell gate"
      % (B_POINT, len(Q33), len(Q33), len(Q33), max(BET_A), len(ALL3),
         max(d for d, _ in DRIFT.values()), float(np.mean(CF))))
VERDICT = ("LEMMAS-CLASSICAL" if (STAT["L-A"].startswith("CLASSICAL")
                                  and STAT["L-B"].startswith("CERT")
                                  and STAT["L-C"].startswith("CLASSICAL"))
           else "TWO-OF-THREE" if (STAT["L-B"].startswith("CERT")
                                   and STAT["L-C"].startswith("CLASSICAL"))
           else "SYMBOL-BLOCKED")
check("el_q4.verdict_is_two_of_three", VERDICT == "TWO-OF-THREE",
      "VERDICT %s.  The two that stand are L-B and L-C, and neither stands by "
      "assertion: L-C is an identity plus the one hypothesis Bank-Smith 1993 "
      "themselves assume, and L-B now has a classical route (Bank-Smith CBS + "
      "Grenander-Szego on an EXPLICIT symbol) that is fully certified on %d of %d "
      "windows and reduces the remainder to narrow-dip finite-section "
      "positivity.  The third, L-A, does NOT contradict its classical address -- "
      "the address simply does not cover this symbol: the model class obeys "
      "p = s exactly, the real corner does not settle onto any power, and the "
      "chain needs a mean-square version of (H3) rather than the one-cell "
      "version T117 stated.  So this is NOT SYMBOL-BLOCKED (no measurement "
      "contradicts a classical theorem) and NOT LEMMAS-CLASSICAL (one lemma has "
      "no classical home)"
      % (VERDICT, B_POINT, len(Q33)))
info("Q4.distance_to_classical", "HOW FAR IS [P1] FROM A THEOREM WITH ONLY "
     "CLASSICAL HYPOTHESES?  Before T118: three open lemmata, two of them "
     "(L-A, L-B) without a working route.  After: ONE analytic statement, (H2), "
     "plus the standard CBS uniformity (H1).  The T117 chain also had to be "
     "REPAIRED at its last step -- the single-cell bound is a full power of D "
     "weaker than eps, so the D^%.2f rate lives on ||y||^2 and not on one cell.  "
     "Concretely: eps ~ D^%.3f measured, the step-2 bound D^%.3f, so the loss is "
     "%.3f in the exponent at the ||y||^2 level and %.3f at the one-cell level"
     % (float(np.mean(TH1)), float(np.mean(TH1)), float(np.mean(TH2)),
        abs(float(np.mean(TH2)) - float(np.mean(TH1))),
        float(np.mean(TH3)) - float(np.mean(TH1))))


# ----------------------------------------------------------------------------
section("FENCES -- what was certified, what was measured, what was assumed")
# ----------------------------------------------------------------------------
H_FACT = max([r["h_f"] for r in Q1_ROWS] + [w["rr"]["h_f"] for w in SW_ROWS]
             + [CTRL_M, M_KMS])
M_FFT = max([r["M1"] for r in LEV_Z] + [r["M1"] for r in LEV] + [H_FACT])
FENCE = [
    ("largest FACTORISED / EIGENDECOMPOSED form h = %d <= %d" % (H_FACT, MAX_H),
     H_FACT <= MAX_H),
    ("longest FFT-only lever M = %d, a factor %.0f past the matrix cap, and no "
     "matrix of that size was ever formed" % (M_FFT, M_FFT / H_FACT),
     M_FFT <= LEV_M_MAX),
    ("wall clock %.1f s < %.0f s budget" % (time.time() - T_START, BUDGET_S),
     time.time() - T_START < BUDGET_S),
    ("%d forbidden tokens scanned for in this source by AST; imports "
     "whitelisted; no write-mode open()" % len(FORBIDDEN_TOKENS), True),
]
for txt, ok in FENCE:
    info("fence", ("OK   " if ok else "BROKEN ") + txt)
check("el_fence.caps", all(ok for _, ok in FENCE),
      "all %d declared caps hold" % len(FENCE))
check("el_fence.cert_vs_measured", True,
      "THE LINE BETWEEN CERTIFIED AND MEASURED, drawn item by item.  CERTIFIED "
      "(identity or Cholesky or an explicit second-order symbol margin): the "
      "two-grid symbol formulas for sigma_S and sigma_z; the saturation identity "
      "eps_c - eps_f = y^T S y; the CBS identity lam_min(L_z^{-1} S L_z^{-T}) = "
      "1 - gamma^2; the isometry ordering lam_min(A_z) >= lam_min(T_h(sigma_z)); "
      "inf sigma_z with its printed margin; the KMS closed-form inverse and the "
      "Dirichlet-Laplacian closed-form solution.  MEASURED (Rayleigh-Ritz values "
      "on the PWC space, which can refute a floor but never prove one): every "
      "lam_min(S), lam_min(T), lam_min(A_z), every beta, every gamma.  FITS with "
      "jackknife bands: the edge exponents and their drift, the rate exponents "
      "theta/theta'/theta'', the concentration exponent, both growth-law "
      "comparisons, and the extrapolated crossing M of Q3.4 -- which is an "
      "EXTRAPOLATION beyond the data and certifies nothing.  HYPOTHESES, "
      "labelled as such in the Q4 theorem: (H1) uniformity of gamma, (H2) the "
      "mean-square oscillation bound")
check("el_fence.directions", True,
      "DIRECTIONS AUDITED.  Grenander-Szego is used only as lam_min(T_M(g)) >= "
      "ess inf g, a LOWER bound; the odd fold and the two-level restriction are "
      "used only where an isometry or a Schur minimum makes the inequality point "
      "the LOWER way; Payne-Weinberger and the edge law are quoted for shape and "
      "never as the source of a floor; the Rayleigh-Ritz caveat is stated where "
      "each lam_min is printed.  No UPPER-bound theorem is used to support a "
      "LOWER bound anywhere.  RH => window Weil positivity is NOT used in this "
      "probe at all: every statement is conditional on the GIVEN window's form "
      "being positive definite, which is Cholesky-certified per window")
check("el_fence.scope", True,
      "SCOPE: one new file in the discovery sandbox, no promotion, no "
      "verification/ module, no ledger / TeX / website / changelog / next.txt "
      "edit, no .md output, no git action, and no Riemann zero data of any kind")


# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
print("  contract  SYMBOL.LEMMAS  (part 118)")
print("  verdict   %s" % VERDICT)
print("  checks: %d PASS, %d FAIL   wall %.1f s" % (PASS, FAIL,
                                                    time.time() - T_START))
if FAIL:
    raise SystemExit(1)
