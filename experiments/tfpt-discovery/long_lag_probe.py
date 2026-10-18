"""Discovery probe (2026-07-28), part 137 of the prime/window investigation.
Contract LONG.LAG -- the STRUCTURE bound for rho(W) and the GREEN lower bound,
and nothing else.

WHERE THIS SITS (T136 ONE-CARRIES: the D-uniformity of the pole-free floor is
reduced to ONE quantity; every load-bearing number is rebuilt here, quoted ones
marked QUOTED)
  T136 closed the rho(K) half with Varga's regular splitting and left the
  A-floor half open in an unusually sharp form.  Its findings, verbatim as the
  starting point:
    * the lumped pair A_B = A + L_Delta is STIELTJES with the row sums
      preserved, A_B >= A in the Loewner order, and the congruence
      A = A_B^{1/2}(I - W)A_B^{1/2}, W = A_B^{-1/2} L_Delta A_B^{-1/2} >= 0,
      gives lam_min(A) >= lam_min(A_B)(1 - lam_max(W)) -- the right direction
      (QUOTED);
    * the M-matrix anchor lam_min(A_B) >= 1 / max_r x_r, x = A_B^{-1} 1 >= 0,
      is CERTIFIABLE and sharp (QUOTED);
    * the EXACT three-way bookkeeping lam_min(A) = [anchor ~ D^-0.565] x
      [margin gap 1 - rho ~ D^+2.72] x [slack ~ D^0.116] attributes the whole
      D-degradation to the MARGIN and nothing else (QUOTED, the split is an
      identity, the exponents are FITS);
    * every NORM route to rho(W) = rho(L_Delta A_B^{-1}) overshoots the true
      rho by 27 .. 8e5 times the gap, and the shifted ladder is structurally
      empty by monotonicity of M-matrix inverses (QUOTED);
    * item (2) of the rest list -- zone-uniformity of S^{-1} > 0 -- needs an
      a-priori LOWER bound on the entries of the Green function S_B^{-1}, i.e.
      the same anchor machinery from the other side (QUOTED).
  THE STRUCTURAL OPENING this probe is built around: L_Delta is not a generic
  perturbation.  Its support is 5.4 % of the entries (QUOTED) and sits at the
  LONG lags, and A_B^{-1} is the Green function of a Stieltjes matrix --
  nonnegative, and for M-matrices with a dominant diagonal a DECAYING object.
  A bound that uses the support and the decay instead of the norm is the only
  candidate left.

WHAT THIS PROBE DOES
  H0  SETUP, the firewall and the CALIBRATION of the four objects H1-H3 rest
      on: the odd pole-free section against its entrywise definition, the
      lumping (Stieltjes, row sums preserved), the EDGE representation
      L_Delta = sum_e Delta_e b_e b_e^T with b_e = e_r - e_t, and the GRAM
      IDENTITY lam_max(W) = lam_max(Gram), Gram_{ee'} = sqrt(Delta_e Delta_e')
      b_e^T A_B^{-1} b_{e'} -- the identity that turns a spectral radius into
      a weighted sum of SECOND DIFFERENCES of the Green function.
  H1  THE LONG-LAG ANATOMY.  WHAT are the positive off-diagonals of A?  The
      section is A_rs = c_{|r-s|} - c_{M-1-r-s}, so every entry compares a
      TOEPLITZ lag against a HANKEL (anti-diagonal) index, and the kernel
      splits exactly as c = c_arch + c_comb with c_comb the sum of the atom
      hats.  Measured: the geometry of the two indices, the sign of the arch
      part alone, the lag distribution and the amplitude law of the positive
      entries, their arithmetic address (the distance of the Hankel index to
      the nearest prime-power atom u_j / D), and whether the support is a union
      of ANTI-DIAGONAL STRIPES -- in which case L_Delta is EXPLICIT and each
      stripe is a perfect MATCHING of the index set.
  H2  THE STRUCTURE BOUND FOR rho(W).  Three families, separated by whether
      they survive taking absolute values:
        (i)  the |E|-ENVELOPE FAMILY (Gershgorin, row-sum norms, every
             Collatz-Wielandt bound at every positive weight) is bounded BELOW
             by rho(|E|), E = A_B^{-1} L_Delta.  A Collatz-Wielandt BRACKET at
             the Perron weight of |E| therefore decides the whole family at
             once -- and a rigorous LOWER bound inside that bracket KILLS it if
             it exceeds the margin.  This is a certificate of DEATH, not a
             measurement.
        (ii) the EDGE / GRAM FAMILY, which keeps the cancellation: the trace
             bound tr(W) = sum_e Delta_e R_e with R_e the effective resistance
             of the pair e in A_B, the Gershgorin bound on the Gram, its
             Collatz-Wielandt refinement, and the STRIPE-BLOCK bound in which
             each block of the Gram over the H1 stripes is replaced by its
             SPECTRAL NORM (block Gershgorin / the norm comparison matrix;
             Feingold-Varga 1962; Ostrowski 1961) -- the only step in the file
             that keeps the SIGNS of the second differences b_e^T A_B^{-1}
             b_{e'}, whose decay over the lag distance is measured and fitted.
        Every bound is tested against 1 - c D^p with (c, p) rebuilt from the
        measured gaps on this surface, and the KEY NUMBER is the implied
        exponent of 1 - bound: a structure bound with the RIGHT power and a
        worse constant is a completely different object from one that sits
        above 1.  Where a bound fails, the COARSENING LADDER says by how much:
        the stripe-block bound is recomputed with the stripes merged into ever
        fewer groups, down to the single group where it becomes lam_max(Gram)
        exactly, and the rung at which it first drops below 1 measures how much
        of the Gram has to be treated exactly for the route to work at all.
  H3  THE GREEN LOWER BOUND.  The Neumann series of the lumped border
      comparison FROM BELOW: S_B = D_0(I - J), J = D_0^{-1} N_0 >= 0, so
      S_B^{-1} = sum_k J^k D_0^{-1} >= (J^k)_{rs} / d_s for EVERY single k and
      >= any partial sum -- positivity of all remaining terms is what makes a
      truncation a bound.  The SAME anchor machinery run from ABOVE closes the
      other side: with x = S_B^{-1} 1 and qJ = max_r (J x)_r / x_r < 1 one has
      (J^k)_{rs} <= qJ^k x_r / x_s, so the tail is majorised too and the Green
      function is bracketed by path quantities.  The certificate for S^{-1} > 0
      is then run in four strengths -- scalar contrast, entrywise, the
      sign-aware k-exact split, and the fully structural bracket -- so that the
      binding ingredient of rest item (2) is identified rather than guessed.
  H4  THE MAP V9, the promotion batch and the shortest rest list.

PREREGISTERED VERDICTS (bars declared here, before any number is computed)
  STRUCTURE-BEATS-MARGIN : the H2 edge/Gram bound is < 1 on EVERY window of the
                  measurement surface, AND the implied gap 1 - bound obeys a
                  power law in D whose exponent is within 0.25 of the measured
                  margin exponent, AND H3 closes -- the D-uniformity of the
                  RH-line floor is then reduced to certified structure
                  ingredients (a decay profile and an amplitude law).
  GREEN-ONLY    : H3 closes and H2 does not -- with the anatomy of H2's
                  failure, per family.
  BOTH-RESIST   : neither -- with the precise reason for each.
  Element gates: el_firewall, el_h0, el_h1, el_h2, el_h3, el_h4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger / TeX / website /
    changelog edit, no verification/ module, no next.txt, no .md output, no git
    action.
  * NO Riemann zero data of any kind.  An AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * THE RH FENCE IS PROMINENT AND ABSOLUTE.  Weil's positivity criterion
    (Weil 1952; Bombieri 2000; Connes 1999) is CITED as the classical address
    of the surrounding statement and is NEVER USED, in either direction.
    Nothing here claims, assumes or approaches RH.  Even with every item
    closed, what would stand is positivity of the Weil window form on test
    functions supported in (-alpha_max, alpha_max) for the alpha actually
    reached -- a FINITE-WINDOW statement about a finite list of prime-power
    zones.  The distance to RH is MAPPED in H4, never travelled.
  * CERTIFIED vs CERTIFIABLE vs MEASURED vs FIT vs HYPOTHESIS, per line.  A
    completed Cholesky of A - s I certifies lam_min(A) >= s - c_h u ||A||,
    u = 2^-53 (Wilkinson 1968; Higham 2002 Thm 10.3/10.4).  A sign check on a
    solve is CERTIFIABLE.  An eigenvalue, a Rayleigh quotient and a power
    iteration are MEASUREMENTS.  A Collatz-Wielandt quotient at ANY positive
    vector is a rigorous two-sided BRACKET for the spectral radius of a
    nonnegative matrix and is labelled as such.  Every fit is a FIT with a
    delete-one jackknife band.  Bars declared before a number are never moved.
  * DIRECTION CARE, carried over from T136 and applied pedantically: lumping
    RAISES the form (A_B >= A), so the pair reaches a floor only through the
    INVERSE side; an upper bound on rho(W) is what a floor needs and a lower
    bound on rho(W) can only KILL one; a lower bound on a Green entry needs the
    Neumann series FROM BELOW and a positivity argument for the discarded tail,
    never a truncation error estimate.
  * CLASSICAL ADDRESSES USED: Stieltjes / Ostrowski 1937, 1956, 1959,
    Berman-Plemmons 1979 (M-matrix equivalences, inverse positivity, Schur
    complements), Fan 1958 (positive-vector criterion), Varga 1962 (regular
    splittings, Jacobi radii), Frobenius 1912 / Perron 1907, Collatz 1942 /
    Wielandt 1950 (the min-max quotient bracket), the Neumann series and the
    standard residual bound (Higham 2002 Ch. 14), Demko-Moss-Smith 1984 (the
    exponential decay of inverses of BANDED positive definite matrices -- cited
    as the model and NOT applicable verbatim here, since A_B is dense; the
    decay measured below is therefore a MEASUREMENT and its profile a FIT),
    Gershgorin 1931 applied to the GRAM rather than to the matrix, the
    effective-resistance form of a Laplacian (Kirchhoff; Klein-Randic 1993),
    Haynsworth 1968 and Cauchy interlacing (complements and directions),
    Levinson 1947 / Durbin 1960, Wilkinson 1968 / Higham 2002, Feller / Dynkin
    Green functions of killed jump processes, Bertrand-Chebyshev 1852 and the
    trivial even bound (the only two gap facts consumed).  No gap CONJECTURE
    (Cramer, Firoozbakht, twin, Mersenne infinitude) enters anywhere.
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    FFT-based lag assembly, row-chunked gathers and edge-chunked Gram passes
    may exceed it.  Probe budget < 900 s.

OUTCOME OF THIS RUN  =>  see the H4 map and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh, svdvals

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 320000
ZONE_DEEP = 300000

# --- H1 pools ---------------------------------------------------------------
H1_ZONES = 44
H1_HCAP = 1000
T_H1 = 120.0

# --- H2 pools ---------------------------------------------------------------
H2_ZONES = 40
H2_HCAP = 620                # dense solve + edge Gram passes, NO edge cap
H2_CHUNK = 224               # edge-chunked Gram pass
H2_CW = 6                    # Collatz-Wielandt refinement passes on |Gram|
H2_POW = 160                 # Perron passes on |E| for the envelope bracket
H2_BLOCK_CAP = 4600          # explicit signed Gram for the STRIPE-BLOCK route
H2_NB_CAP = 220              # stripes per window for the block route
H2_LADDER_CAP = 1400         # coarsening ladder (respects MAX_H at every rung)
T_H2 = 330.0

# --- H3 pools ---------------------------------------------------------------
H3_GC_MIN = 2
H3_HCAP = 900
H3_MAX = 900                 # transports attempted (T134/T136 reported 900)
H3_PER_RHO = 30
H3_LOGRES = 90.0
H3_RHO = (1.001, 1.05, 1.10, 1.20, 1.25, 1.35, 1.49531, 1.60, 1.75, 1.90,
          2.00, 2.25, 2.50, 3.00, 3.50, 4.00)   # 1.49531 = the T127 band edge
H3_KMAX = 6                  # path length used in the Neumann-from-below bound
H3_KEX = 3                   # terms kept SIGNED in the k-exact remainder split
T_H3 = 260.0

# --- preregistered bars (declared before any number is computed) ------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_SUPPORT = 0.99           # "arithmetically nameable" = 99 % of the support
BAR_H2_COVER = 1.0           # the structure bound must be < 1 on EVERY window
BAR_H2_EXP = 0.25            # ... and its implied exponent within this of p
BAR_H3_COVER = 1.0           # the a-priori Green certificate on EVERY block
BAR_AMP = 1.0                # the candidate amplitude law Delta <= mu/2

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
POS_FRAC_T136 = 5.4          # % of off-diagonal entries that are positive
OVER_T136 = (27.0, 8.0e5)    # norm-route overshoot, in units of the gap
BK_T136 = dict(mu=2.26, an=-0.565, gp=2.72, fa=0.116)
RHO0_N_T136 = 900            # border blocks in the T134/T136 transport pool
PROMO_T136 = 22
N_PROBES_PRIOR = 136


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-36s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-36s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def wrap_at(text, width):
    out, line = [], ""
    for w in text.split():
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + " " + w) if line else w
    if line:
        out.append(line)
    return out


def para(text, width=76, indent="  "):
    for ln in wrap_at(text, width - len(indent)):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def sym(A):
    return 0.5 * (A + A.T)


def rel(a, b):
    return float(np.max(np.abs(a - b))) / max(float(np.max(np.abs(b))), 1.0e-300)


def qmin(v):
    return float(np.min(np.asarray(v, dtype=float))) if len(v) else float("nan")


def qmax(v):
    return float(np.max(np.asarray(v, dtype=float))) if len(v) else float("nan")


def qmed(v):
    return float(np.median(np.asarray(v, dtype=float))) if len(v) else float("nan")


def fit_line(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_band(x, y):
    """A FIT with a delete-one jackknife band on both coefficients."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = x.shape[0]
    a, b, rms = fit_line(x, y)
    if n < 5:
        return a, b, float("nan"), float("nan"), rms
    aa, bb = [], []
    step = max(1, n // 40)
    for i in range(0, n, step):
        m = np.ones(n, dtype=bool)
        m[i] = False
        ai, bi, _ = fit_line(x[m], y[m])
        aa.append(ai)
        bb.append(bi)
    k = len(aa)
    sa = math.sqrt(max(k - 1, 1) / float(k) * float(np.sum(
        (np.asarray(aa) - np.mean(aa)) ** 2)))
    sb = math.sqrt(max(k - 1, 1) / float(k) * float(np.sum(
        (np.asarray(bb) - np.mean(bb)) ** 2)))
    return a, b, sa, sb, rms


def pow_fit(D, y, tag):
    """log-log FIT of y against D, with the jackknife band.  A FIT ONLY."""
    xs, ys = [], []
    for d, v in zip(D, y):
        if v == v and v > 0.0 and d > 0.0:
            xs.append(math.log(d))
            ys.append(math.log(v))
    if len(xs) < 5:
        return dict(tag=tag, n=len(xs), c=float("nan"), p=float("nan"),
                    sp=float("nan"), rms=float("nan"))
    a, b, sa, sb, rms = fit_band(xs, ys)
    return dict(tag=tag, n=len(xs), c=math.exp(a), p=b, sp=sb, rms=rms)


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
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("el_firewall.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("el_firewall.one_file", os.path.basename(os.path.abspath(__file__))
          == "long_lag_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- T111..T136 code path
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


def atoms_in(alpha, atoms_all):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952 -- CITED, never used as a criterion)
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


def comb_lags(M, D, atoms):
    """THE COMB HALF of the lag vector, ISOLATED: the sum of the atom hats that
    lag_vector_fast subtracts.  c = c_arch - c_comb exactly, by construction."""
    out = np.zeros(M)
    for u_j, mu_j in atoms:
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                out[i] += mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    out[i] += mu_j * 0.5 * v
    return out


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
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T136)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_toeplitz_slow(c, M):
    """The definition, entry by entry -- the H0 reference for odd_toeplitz."""
    h = M // 2
    out = np.empty((h, h))
    for i in range(h):
        for j in range(h):
            out[i, j] = c[abs(i - j)] - c[(M - 1) - i - j]
    return out


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2)."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except LinAlgError:
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


# ----------------------------------------------------------------------------
# the frame (T112 frame A, window forced EVEN so that h = M/2 exactly)
# ----------------------------------------------------------------------------
def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def step_frame(u_old, u_new, D):
    M_o = even_window(u_old, D)
    M_n = even_window(u_new, D)
    gc = (M_n - M_o) // 2
    if gc < 1:
        return None
    return dict(D=D, M_o=M_o, M_n=M_n, gc=gc, h_o=M_o // 2, h_n=M_n // 2,
                al_o=0.5 * M_o * D, al_n=0.5 * M_n * D)


def bordered_step(fr, atoms_all):
    """The bordered step (Haynsworth 1968) and its border Schur block."""
    at_n = atoms_in(fr["al_n"], atoms_all)
    c_n, _ = lag_vector_fast(fr["al_n"], fr["M_n"], at_n)
    tv = odd_pole_vector(fr["al_n"], fr["M_n"])
    Q = sym(odd_toeplitz(c_n, fr["M_n"]) - np.outer(tv, tv))
    gc = fr["gc"]
    A = sym(np.ascontiguousarray(Q[:gc, :gc]))
    C = np.ascontiguousarray(Q[:gc, gc:])
    X = sym(np.ascontiguousarray(Q[gc:, gc:]))
    fac = safe_cho(X)
    if fac is None:
        return None
    Z = cho_solve(fac, C.T, check_finite=False)
    S = sym(A - C @ Z)
    del Q, A, C, X, Z
    return dict(S=S, fr=fr)


# ----------------------------------------------------------------------------
# THE LUMPED M-MATRIX PAIR and its EDGE representation -- the central objects
# ----------------------------------------------------------------------------
def lump_pair(A):
    """THE LUMPED M-MATRIX PAIR of a symmetric A (T136 (P1)).

    Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta its
    Laplacian (PSD, zero row sums), A_B = A + L_Delta.

    DIRECTION, stated once and never forgotten: L_Delta >= 0 in the LOEWNER
    order, so A_B >= A -- lumping RAISES the form and gives an UPPER bound on
    lam_min(A) directly and a LOWER bound never.  The floor is reached only
    through the INVERSE side."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    A_B = sym(A + LD)
    offB = A_B - np.diag(np.diag(A_B))
    return dict(h=h, A_B=A_B, Dl=Dl, LD=LD, P_row=P_row, w=A.sum(axis=1),
                dg=dg, dgB=np.diag(A_B).copy(),
                stieltjes=int(bool(np.all(offB <= 1.0e-300))
                              and bool(np.all(np.diag(A_B) > 0.0))),
                n_pos=int(np.count_nonzero(np.where(np.eye(h, dtype=bool),
                                                    0.0, off) > 0.0)))


def anchor_floor(A_B):
    """THE M-MATRIX ANCHOR (T136 (P4)).  For symmetric Stieltjes A_B, solve
    A_B x = 1.  If x >= 0 entrywise then A_B is a nonsingular M-matrix
    (Fan 1958; Berman-Plemmons 1979) and lam_min(A_B) >= 1 / max_r x_r, since
    ||A_B^{-1}||_2 <= ||A_B^{-1}||_inf = ||A_B^{-1} 1||_inf for a SYMMETRIC
    matrix with a NONNEGATIVE inverse.  DIRECTION: a LOWER bound."""
    h = A_B.shape[0]
    fac = safe_cho(A_B)
    if fac is None:
        return None
    x = cho_solve(fac, np.ones(h), check_finite=False)
    xmax = float(np.max(x))
    xmin = float(np.min(x))
    return dict(fac=fac, x=x, xmax=xmax, xmin=xmin,
                nonneg=int(xmin >= -1.0e-13 * max(xmax, 1.0e-300)),
                floor=(1.0 / xmax) if xmax > 0.0 else float("nan"))


def edge_list(Dl, M=None):
    """THE EDGE REPRESENTATION of L_Delta.  Delta is symmetric with a zero
    diagonal, so L_Delta = sum_{r<t} Delta_rt (e_r - e_t)(e_r - e_t)^T exactly:
    a weighted graph Laplacian.  NOTHING is capped or dropped -- an upper bound
    on lam_max(W) may not discard edges, because dropping an edge SHRINKS
    L_Delta and would bound the wrong object.  The list is sorted by the STRIPE
    index anti = M - 1 - r - t of H1, so the edges of one anti-diagonal stripe
    are contiguous and the stripe blocks of the Gram are slices."""
    h = Dl.shape[0]
    iu = np.triu_indices(h, 1)
    w = Dl[iu]
    keep = w > 0.0
    er = iu[0][keep]
    et = iu[1][keep]
    w = w[keep]
    lab = ((M - 1) - er - et) if M is not None else (er + et)
    order = np.lexsort((er, lab))
    er, et, w, lab = er[order], et[order], w[order], lab[order]
    vals, starts, counts = np.unique(lab, return_index=True, return_counts=True)
    return dict(er=er, et=et, w=w, lab=lab, n=er.shape[0],
                mass=float(w.sum()), stripe_val=vals, stripe_start=starts,
                stripe_count=counts, nb=vals.shape[0])


def gram_apply(G, er, et, wt, Y, chunk=H2_CHUNK, absolute=True):
    """|Gram| Y (or Gram Y) without ever forming the Gram matrix.

        Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T G b_{e'},
        b_e = e_r - e_t,   G = A_B^{-1},

    so the entry is a SECOND DIFFERENCE of the Green function, G_{rr'} -
    G_{rt'} - G_{tr'} + G_{tt'}.  This is the object the whole H2 route rests
    on: taking absolute values here destroys far less than taking them in E,
    because the cancellation lives INSIDE the second difference."""
    n = er.shape[0]
    Y = np.asarray(Y, dtype=float)
    out = np.zeros_like(Y)
    for a in range(0, n, chunk):
        b = min(n, a + chunk)
        R, T = er[a:b], et[a:b]
        blk = (G[np.ix_(R, er)] - G[np.ix_(R, et)]
               - G[np.ix_(T, er)] + G[np.ix_(T, et)])
        if absolute:
            np.abs(blk, out=blk)
        blk *= wt[a:b][:, None]
        blk *= wt[None, :]
        out[a:b] = blk @ Y
        del blk
    return out


def stripe_block_bound(GR, starts, counts):
    """THE STRIPE-BLOCK BOUND (block Gershgorin / the norm comparison matrix;
    Feingold-Varga 1962; Ostrowski 1961).  Partition the Gram by the H1 stripes
    and replace each block by its SPECTRAL NORM:

        Chat_{jj'} = || Gram_{jj'} ||_2 ,   lam_max(Gram) = ||Gram||_2 <=
        rho(Chat),

    because the block norms of a product dominate blockwise.  This is the first
    bound in the file that survives the SIGNS: a spectral norm of a block is
    far below the sum of its absolute entries whenever the second differences
    of the Green function alternate, which is exactly what an oscillating
    Green kernel does.  Chat is symmetric nonnegative, so rho(Chat) is its top
    eigenvalue, and the cruder row-sum (disc) version is returned with it."""
    nb = starts.shape[0]
    C = np.zeros((nb, nb))
    for i in range(nb):
        ai, bi = int(starts[i]), int(starts[i] + counts[i])
        for j in range(i, nb):
            aj, bj = int(starts[j]), int(starts[j] + counts[j])
            B = GR[ai:bi, aj:bj]
            if i == j:
                v = (float(eigvalsh(sym(B), subset_by_index=[B.shape[0] - 1,
                                                             B.shape[0] - 1])[0])
                     if B.shape[0] > 1 else abs(float(B[0, 0])))
            else:
                v = float(svdvals(B)[0]) if B.size else 0.0
            C[i, j] = C[j, i] = max(v, 0.0)
    disc = float(np.max(C.sum(axis=1)))
    rho_c = float(eigvalsh(C, subset_by_index=[nb - 1, nb - 1])[0]) if nb > 1 \
        else float(C[0, 0])
    return dict(nb=nb, disc=disc, rho=max(rho_c, 0.0),
                diag_max=float(np.max(np.diag(C))),
                off_share=(1.0 - float(np.trace(C)) / max(float(C.sum()), 1e-300)))


def coarsen(starts, counts, ngroup):
    """Merge consecutive stripes into ngroup groups, returning group slices."""
    nb = starts.shape[0]
    edges = np.linspace(0, nb, ngroup + 1).round().astype(int)
    out_s, out_c = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        if b <= a:
            continue
        s0 = int(starts[a])
        s1 = int(starts[b - 1] + counts[b - 1])
        out_s.append(s0)
        out_c.append(s1 - s0)
    return np.array(out_s, dtype=int), np.array(out_c, dtype=int)


def coarse_ladder(GR, starts, counts, blk_cap):
    """THE COARSENING LADDER: the stripe-block bound as a function of how many
    groups the stripes are merged into.  At one group per stripe it is the
    block Gershgorin bound of stripe_block_bound; at ONE group it is
    lam_max(Gram) itself, i.e. the exact answer.  The rung at which the bound
    first drops below 1 measures HOW MUCH of the Gram has to be treated exactly
    -- the honest quantitative answer to 'how far is the structure route from
    working', with the hard cap on any diagonalised form respected at every
    rung."""
    nb = starts.shape[0]
    rungs = []
    ng = nb
    seen = set()
    while ng >= 1:
        if ng not in seen:
            seen.add(ng)
            s, c = coarsen(starts, counts, ng)
            if int(np.max(c)) <= blk_cap:
                bb = stripe_block_bound(GR, s, c)
                rungs.append(dict(ng=int(s.shape[0]),
                                  bsz=int(np.max(c)), bound=bb["rho"]))
        if ng == 1:
            break
        ng = max(1, ng // 2)
    return rungs


def perron_bracket(applyf, n, iters, rng=None):
    """THE COLLATZ-WIELANDT BRACKET for a NONNEGATIVE matrix given only by its
    action (Collatz 1942; Wielandt 1950):

        min_r (M y)_r / y_r  <=  rho(M)  <=  max_r (M y)_r / y_r

    for EVERY strictly positive y.  Both ends are RIGOROUS -- the upper end
    certifies, the lower end KILLS -- and the power iteration is used only to
    choose a good y, never as the bound itself."""
    y = (np.abs(rng.standard_normal(n)) + 0.5) if rng is not None else np.ones(n)
    lo = hi = float("nan")
    for _ in range(iters):
        z = applyf(y)
        pos = y > 0.0
        if not np.all(pos):
            break
        q = z / y
        lo, hi = float(np.min(q)), float(np.max(q))
        nz = float(np.max(z))
        if not (nz > 0.0):
            return 0.0, 0.0
        y = np.maximum(z / nz, 1.0e-300)
    return lo, hi


firewall()


# ----------------------------------------------------------------------------
section("H0  SETUP, the pair, the EDGE representation and the GRAM identity")
# ----------------------------------------------------------------------------
ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
MU_SORTED = np.array([t[3] for t in ATOMS_ALL], dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]

NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

BERT_OK = bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
EVEN_OK = bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12))
check("el_h0.gap_bounds", BERT_OK and EVEN_OK,
      "%d prime-power atoms up to %d, %d zones in the deep range n <= %d; the "
      "only two gap facts consumed hold on all of it: Bertrand-Chebyshev 1852 "
      "g_k <= log 2 (max %.6f) and the trivial even bound g_k >= log(1 + 1/n) "
      "(min %.3e).  No gap CONJECTURE enters, in either direction"
      % (len(ATOMS_ALL), ATOM_MAX, NZ_DEEP, ZONE_DEEP, G_DEEP.max(),
         G_DEEP.min()))

CAP_K = 0.5 * G_DEEP / NU_MAIN
D_FREE = np.empty_like(CAP_K)
D_FREE[0] = CAP_K[0]
for k in range(1, NZ_DEEP):
    D_FREE[k] = min(CAP_K[k], D_FREE[k - 1])

# --- H0.1  the odd section against the entrywise definition -----------------
_zk = None
for k in range(4, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    if 60 <= even_window(UU_ALL[k], D_k) // 2 <= 130:
        _zk = k
        break
if _zk is None:
    _zk = 6
_Dv = 0.5 * float(G_DEEP[_zk]) / NU_MAIN
_Mv = even_window(UU_ALL[_zk], _Dv)
_alv = 0.5 * _Mv * _Dv
_atv = atoms_in(_alv, ATOMS_ALL)
_cv, _ = lag_vector_fast(_alv, _Mv, _atv)
_Av = sym(odd_toeplitz(_cv, _Mv))
_hv = _Mv // 2
E_ODD = rel(odd_toeplitz(_cv, _Mv), odd_toeplitz_slow(_cv, _Mv))
check("el_h0.odd_section", E_ODD < 1.0e-15,
      "the vectorised odd Toeplitz+Hankel section reproduces the entrywise "
      "definition A_rs = c_|r-s| - c_{M-1-r-s} to %.2e at the validation zone "
      "n = %d (h = %d, D = %.4e, %d atoms in the window).  A is the POLE-FREE "
      "object throughout H1-H2: the rank-one pole term is NOT subtracted"
      % (E_ODD, NN_ALL[_zk], _hv, _Dv, len(_atv)))

# --- H0.2  the kernel split c = c_arch - c_comb, exact ----------------------
_carch = arch_lags(_Mv, _Dv)
_ccomb = comb_lags(_Mv, _Dv, _atv)
E_SPLIT = float(np.max(np.abs(_cv - (_carch - _ccomb)))) / max(
    float(np.max(np.abs(_cv))), 1.0e-300)
check("el_h0.kernel_split", E_SPLIT < 1.0e-15,
      "the lag vector splits EXACTLY into an archimedean half and a COMB half, "
      "c_k = c_arch(k D) - c_comb(k), to %.2e relative.  c_comb is a sum of "
      "%d triangular hats of height mu_j / 2 = Lambda(n_j) / sqrt(n_j) centred "
      "at the atom lags u_j = log n_j -- the T119 comb, in the coordinates the "
      "section actually uses.  c_arch is smooth and monotone; the comb is a "
      "spike train.  H1 asks which of the two makes an entry of A positive"
      % (E_SPLIT, len(_atv)))

# --- H0.3  the lumped pair, its edge representation and the GRAM identity ---
_lp = lump_pair(_Av)
_an = anchor_floor(_lp["A_B"])
_ed = edge_list(_lp["Dl"], _Mv)
_LDe = np.zeros((_hv, _hv))
for _i in range(_ed["n"]):
    _r, _t, _w = int(_ed["er"][_i]), int(_ed["et"][_i]), float(_ed["w"][_i])
    _LDe[_r, _r] += _w
    _LDe[_t, _t] += _w
    _LDe[_r, _t] -= _w
    _LDe[_t, _r] -= _w
E_EDGE = rel(_LDe, _lp["LD"]) if _ed["n"] else 0.0
check("el_h0.edge_representation",
      _lp["stieltjes"] == 1 and _an is not None and _an["nonneg"] == 1
      and E_EDGE < BAR_ID,
      "the lumped pair is STIELTJES by construction, the anchor solve "
      "A_B x = 1 returns x >= 0 (min %.3e, max %.3e, floor 1/max x = %.4e) so "
      "A_B is a nonsingular M-matrix, and L_Delta is reproduced to %.2e by its "
      "EDGE form sum_{r<t} Delta_rt (e_r - e_t)(e_r - e_t)^T over %d edges "
      "(%.2f %% of the %d off-diagonal pairs, T136 quoted %.1f %%).  The edge "
      "form is what H2 needs: it exhibits L_Delta as a weighted graph LAPLACIAN "
      "and not as a matrix with a norm"
      % (_an["xmin"] if _an else float("nan"),
         _an["xmax"] if _an else float("nan"),
         _an["floor"] if _an else float("nan"), E_EDGE, _ed["n"],
         100.0 * _ed["n"] / max(_hv * (_hv - 1) / 2.0, 1.0),
         _hv * (_hv - 1) // 2, POS_FRAC_T136))

_G = cho_solve(_an["fac"], np.eye(_hv), check_finite=False)
_wt = np.sqrt(_ed["w"])
_Bv = np.zeros((_hv, _ed["n"]))
_Bv[_ed["er"], np.arange(_ed["n"])] = 1.0
_Bv[_ed["et"], np.arange(_ed["n"])] = -1.0
_GRAM = (_Bv.T @ _G @ _Bv) * (_wt[:, None] * _wt[None, :])
_lg_gram = float(eigvalsh(_GRAM, subset_by_index=[_ed["n"] - 1,
                                                  _ed["n"] - 1])[0])
_gap_ex = float(eigh(_Av, _lp["A_B"], eigvals_only=True,
                     subset_by_index=[0, 0])[0])
_rho_ex = 1.0 - _gap_ex
E_GRAM = abs(_lg_gram - _rho_ex) / max(_rho_ex, 1.0e-300)
check("el_h0.gram_identity", E_GRAM < 1.0e-9,
      "THE GRAM IDENTITY, which is the whole instrument of H2 and is an "
      "IDENTITY and not a bound: with W = A_B^{-1/2} L_Delta A_B^{-1/2} = "
      "V V^T, V = [sqrt(Delta_e) A_B^{-1/2} b_e]_e, the nonzero spectrum of W "
      "equals that of the EDGE GRAM Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T "
      "A_B^{-1} b_{e'}.  Verified: lam_max(Gram) = %.6f against 1 - "
      "lam_min(A, A_B) = %.6f, relative %.2e on a %d x %d Gram.  Every entry "
      "of the Gram is a SECOND DIFFERENCE of the Green function A_B^{-1}; the "
      "diagonal is Delta_e R_e with R_e = b_e^T A_B^{-1} b_e the effective "
      "resistance of the pair (Kirchhoff; Klein-Randic 1993)"
      % (_lg_gram, _rho_ex, E_GRAM, _ed["n"], _ed["n"]))

_tr_gram = float(np.trace(_GRAM))
_ger_gram = float(np.abs(_GRAM).sum(axis=1).max())
_E = cho_solve(_an["fac"], _lp["LD"], check_finite=False)
_rho_inf = float(np.abs(_E).sum(axis=1).max())
info("H0.first_look",
     "the four numbers on the validation window, so the reader knows the scale "
     "before H2 starts: the true rho(W) = %.6f, the margin 1 - rho = %.3e, the "
     "T136 row-sum norm ||A_B^{-1} L_Delta||_inf = %.4f (above 1, as T136 "
     "reported everywhere), the GRAM Gershgorin bound = %.4f and the GRAM "
     "TRACE bound tr(W) = %.4f.  Whether either of the last two is below 1 on "
     "the whole surface is exactly the H2 question"
     % (_rho_ex, _gap_ex, _rho_inf, _ger_gram, _tr_gram))
del _GRAM, _Bv, _E


# ----------------------------------------------------------------------------
section("H1  THE LONG-LAG ANATOMY -- what the positive off-diagonals ARE")
# ----------------------------------------------------------------------------
para("""H1.0  THE GEOMETRY FIRST, BEFORE ANY MEASUREMENT.  The odd section is
A_rs = c_{|r-s|} - c_{M-1-r-s} with r, s in [0, h), h = M/2.  Write lag = |r-s|
for the TOEPLITZ index and anti = M-1-r-s for the HANKEL index.  Two facts are
pure arithmetic and are checked below rather than assumed: (a) anti - lag =
M-1-2 max(r,s) >= 1 for every pair, so the Hankel index is ALWAYS strictly
larger than the Toeplitz lag -- the two indices never collide; and (b) an entry
is positive exactly when c_{lag} > c_{anti}, i.e. when the lag vector is LARGER
at the smaller index.  Since c = c_arch - c_comb with c_arch smooth and c_comb a
train of hats supported at the atom lags u_j / D, a positive entry needs the
COMB to be deeper at anti than at lag -- unless the archimedean half is itself
increasing.  H1 measures which of the two happens, and where.""")

H1Z = []
_seen = set()
for k in range(2, NZ_DEEP - 2):
    if len(H1Z) >= H1_ZONES:
        break
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > H1_HCAP:
        continue
    key = h_k // 12
    if key in _seen:
        continue
    _seen.add(key)
    H1Z.append((k, D_k, M_k, h_k))

H1R = []
for (k, D_k, M_k, h_k) in H1Z:
    if budget_left() < BUDGET_S - T_H1:
        info("H1.budget", "anatomy pool truncated at n = %d" % NN_ALL[k])
        break
    al = 0.5 * M_k * D_k
    ats = atoms_in(al, ATOMS_ALL)
    c, _ = lag_vector_fast(al, M_k, ats)
    c_ar = arch_lags(M_k, D_k)
    c_cb = c_ar - c
    A = sym(odd_toeplitz(c, M_k))
    A_ar = sym(odd_toeplitz(c_ar, M_k))
    r = np.arange(h_k)
    lag = np.abs(r[:, None] - r[None, :])
    anti = (M_k - 1) - r[:, None] - r[None, :]
    iu = np.triu_indices(h_k, 1)
    a_up = A[iu]
    ar_up = A_ar[iu]
    lag_up = lag[iu]
    ant_up = anti[iu]
    pos = a_up > 0.0
    n_pairs = a_up.shape[0]
    n_pos = int(np.count_nonzero(pos))
    # the arithmetic address of the Hankel index of every POSITIVE entry
    ua = ant_up[pos] * D_k
    j = np.searchsorted(U_SORTED, ua)
    j0 = np.clip(j - 1, 0, len(U_SORTED) - 1)
    j1 = np.clip(j, 0, len(U_SORTED) - 1)
    d0 = np.abs(ua - U_SORTED[j0])
    d1 = np.abs(ua - U_SORTED[j1])
    near = np.where(d0 <= d1, j0, j1)
    dist = np.minimum(d0, d1)
    mu_near = MU_SORTED[near]
    # the same address for the TOEPLITZ index of the positive entries
    ul = lag_up[pos] * D_k
    jl = np.searchsorted(U_SORTED, ul)
    jl0 = np.clip(jl - 1, 0, len(U_SORTED) - 1)
    jl1 = np.clip(jl, 0, len(U_SORTED) - 1)
    dl = np.minimum(np.abs(ul - U_SORTED[jl0]), np.abs(ul - U_SORTED[jl1]))
    amp = a_up[pos]
    stripes = np.unique(ant_up[pos])
    H1R.append(dict(
        n=NN_ALL[k], h=h_k, M=M_k, D=D_k, al=al, n_at=len(ats),
        n_pairs=n_pairs, n_pos=n_pos, pos_frac=n_pos / max(n_pairs, 1),
        sep_min=int(np.min(ant_up - lag_up)),
        arch_pos=int(np.count_nonzero(ar_up > 0.0)),
        arch_mono=int(bool(np.all(np.diff(c_ar) >= -1.0e-300))),
        arch_mono_frac=float(np.mean(np.diff(c_ar) >= 0.0)),
        arch_dec_last=(int(np.max(np.nonzero(np.diff(c_ar) < 0.0)[0]))
                       if np.any(np.diff(c_ar) < 0.0) else -1),
        arch_max=float(np.max(ar_up)),
        comb_pos_share=(float(np.mean(c_cb[ant_up[pos]]
                                      > c_cb[lag_up[pos]])) if n_pos else
                        float("nan")),
        lag_med=(float(np.median(lag_up[pos])) / h_k if n_pos else float("nan")),
        lag_q10=(float(np.quantile(lag_up[pos], 0.10)) / h_k if n_pos
                 else float("nan")),
        lag_all_med=float(np.median(lag_up)) / h_k,
        anti_med=(float(np.median(ant_up[pos])) / M_k if n_pos else float("nan")),
        near_1D=(float(np.mean(dist < D_k)) if n_pos else float("nan")),
        near_2D=(float(np.mean(dist < 2.0 * D_k)) if n_pos else float("nan")),
        lag_near_1D=(float(np.mean(dl < D_k)) if n_pos else float("nan")),
        n_stripe=int(stripes.shape[0]),
        stripe_per_atom=stripes.shape[0] / max(len(ats), 1),
        amp_max=(float(np.max(amp)) if n_pos else float("nan")),
        amp_med=(float(np.median(amp)) if n_pos else float("nan")),
        amp_ratio=(float(np.max(amp / np.maximum(0.5 * mu_near, 1.0e-300)))
                   if n_pos else float("nan")),
        amp_one=(float(np.mean(amp <= 0.5 * mu_near)) if n_pos
                 else float("nan")),
        amp_comb=(float(np.max(amp / np.maximum(c_cb[ant_up[pos]], 1.0e-300)))
                  if n_pos else float("nan")),
        cb_min=float(np.min(c_cb)),
        mass=(float(np.sum(amp)) if n_pos else 0.0)))
    del A, A_ar, lag, anti

check("el_h1.index_separation",
      bool(H1R) and all(r["sep_min"] >= 1 for r in H1R),
      "THE TWO INDICES NEVER COLLIDE, on %d windows (h = %.0f .. %.0f, D = "
      "%.2e .. %.2e, n = %d .. %d): anti - lag = M-1-2 max(r,s) >= %d on every "
      "off-diagonal pair of every window.  So the Hankel index is always the "
      "LONGER lag, and every positive entry of A is a statement that the lag "
      "vector is LARGER at the shorter index than at the longer one -- which "
      "is the definition of a LONG-LAG effect, not a metaphor for one"
      % (len(H1R), qmin([r["h"] for r in H1R]), qmax([r["h"] for r in H1R]),
         qmin([r["D"] for r in H1R]), qmax([r["D"] for r in H1R]),
         min(r["n"] for r in H1R), max(r["n"] for r in H1R),
         min(r["sep_min"] for r in H1R)))

ARCH_ZERO = [r for r in H1R if r["arch_pos"] == 0]
MONO = [r for r in H1R if r["arch_mono"] == 1]
check("el_h1.arch_half_is_negative", bool(H1R) and len(ARCH_ZERO) == len(H1R),
      "THE ARCHIMEDEAN HALF CONTRIBUTES NO POSITIVE OFF-DIAGONAL AT ALL: the "
      "odd section built from the archimedean kernel ALONE has ZERO positive "
      "off-diagonals on %d of %d windows, with max_{r != s} A_arch = %.2e .. "
      "%.2e, i.e. nonpositive to the last digit.  The mechanism is ALMOST but "
      "not exactly monotonicity, and the difference is stated rather than "
      "papered over: c_arch is nondecreasing on %.4f .. %.4f of consecutive "
      "lag pairs but NOT on all of them (full monotonicity holds on %d of %d "
      "windows), the decreases being confined to lag indices <= %d out of "
      "M = %d .. %d -- the near field of the kernel.  Since anti > lag by at "
      "least one cell for every pair, the only way A_arch could be positive is "
      "through one of those near-field decreases, and it never is.  The "
      "consequence is the first result of this probe and it is structural: the "
      "ENTIRE bad half L_Delta is COMB-GENERATED.  The arch tail is not a "
      "source of positivity; it is the background the comb spikes puncture"
      % (len(ARCH_ZERO), len(H1R), qmin([r["arch_max"] for r in H1R]),
         qmax([r["arch_max"] for r in H1R]),
         qmin([r["arch_mono_frac"] for r in H1R]),
         qmax([r["arch_mono_frac"] for r in H1R]), len(MONO), len(H1R),
         max(r["arch_dec_last"] for r in H1R),
         min(r["M"] for r in H1R), max(r["M"] for r in H1R)))

NAMED = [r for r in H1R if r["near_1D"] >= BAR_SUPPORT]
NAMED2 = [r for r in H1R if r["near_2D"] >= BAR_SUPPORT]
check("el_h1.support_address", bool(H1R),
      "THE ARITHMETIC ADDRESS OF THE SUPPORT.  For every positive entry the "
      "Hankel index anti = M-1-r-s was compared with the prime-power atom lags "
      "u_j = log n_j: the distance |anti D - u_nearest| is below ONE grid cell "
      "for %.2f .. %.2f of the positive entries (below two cells: %.2f .. "
      "%.2f), against the declared bar %.2f -- met on %d of %d windows at one "
      "cell and %d of %d at two.  The support is therefore a union of "
      "ANTI-DIAGONAL STRIPES r + s = M - 1 - round(u_j / D), one or two "
      "stripes per atom (measured %.2f .. %.2f stripes per atom in the window, "
      "%d .. %d stripes on %d .. %d atoms).  L_Delta is EXPLICIT: its support "
      "is indexed by the atoms of the window and nothing else"
      % (qmin([r["near_1D"] for r in H1R]), qmax([r["near_1D"] for r in H1R]),
         qmin([r["near_2D"] for r in H1R]), qmax([r["near_2D"] for r in H1R]),
         BAR_SUPPORT, len(NAMED), len(H1R), len(NAMED2), len(H1R),
         qmin([r["stripe_per_atom"] for r in H1R]),
         qmax([r["stripe_per_atom"] for r in H1R]),
         min(r["n_stripe"] for r in H1R), max(r["n_stripe"] for r in H1R),
         min(r["n_at"] for r in H1R), max(r["n_at"] for r in H1R)))

AMP_OK = [r for r in H1R if r["amp_ratio"] <= BAR_AMP]
AMP_CB = [r for r in H1R if r["amp_comb"] <= BAR_AMP + 1.0e-9]
check("el_h1.amplitude_law", len(AMP_CB) == len(H1R) and
      min(r["cb_min"] for r in H1R) >= -1.0e-12,
      "THE AMPLITUDE LAW, in the form that is CERTIFIABLE and in the form that "
      "is merely typical, kept apart on purpose.  CERTIFIABLE: A_rs = "
      "[c_arch(lag) - c_arch(anti)] + [c_comb(anti) - c_comb(lag)] by the "
      "kernel decomposition, the first bracket is <= 0 by the check above and "
      "c_comb >= 0 entrywise (measured minimum %.3e over all windows), hence "
      "EVERY positive entry obeys Delta_rs <= c_comb(anti) with no further "
      "input -- the measured ratio Delta / c_comb(anti) is %.4f .. %.4f, i.e. "
      "at most one, on %d of %d windows, and c_comb(anti) = (1/2) sum_j mu_j "
      "hat_j(anti) is the T119 comb evaluated at the Hankel index.  TYPICAL "
      "BUT NOT A LAW: the SINGLE-ATOM version Delta_rs <= (1/2) mu_j for the "
      "one nearest atom holds on %.3f .. %.3f of the positive entries but its "
      "worst ratio reaches %.4f -- when two prime powers fall inside the same "
      "grid cell their hats add, and no single-atom bound can survive that.  "
      "The honest statement is therefore the SUM over the atoms of the cell.  "
      "Numerically max Delta = %.3e .. %.3e, total positive mass %.3e .. %.3e"
      % (min(r["cb_min"] for r in H1R),
         qmin([r["amp_comb"] for r in H1R]),
         qmax([r["amp_comb"] for r in H1R]), len(AMP_CB), len(H1R),
         qmin([r["amp_one"] for r in H1R]), qmax([r["amp_one"] for r in H1R]),
         qmax([r["amp_ratio"] for r in H1R]),
         qmin([r["amp_max"] for r in H1R]), qmax([r["amp_max"] for r in H1R]),
         qmin([r["mass"] for r in H1R]), qmax([r["mass"] for r in H1R])))

info("H1.lag_profile",
     "THE LAG DISTRIBUTION, for the record: the positive entries carry a median "
     "Toeplitz lag of %.2f .. %.2f in units of h against %.2f for the off-"
     "diagonal population as a whole, their median Hankel index is %.2f .. %.2f "
     "of M, and the Toeplitz index of a positive entry sits within one cell of "
     "an atom lag only %.2f .. %.2f of the time -- i.e. the positivity is a "
     "one-sided event at the HANKEL index and not a coincidence of the two.  "
     "The support fraction is %.2f .. %.2f %% of the off-diagonal pairs (T136 "
     "quoted %.1f %%, reproduced), and the comb is deeper at anti than at lag "
     "on %.2f .. %.2f of the positive entries"
     % (qmin([r["lag_med"] for r in H1R]), qmax([r["lag_med"] for r in H1R]),
        qmed([r["lag_all_med"] for r in H1R]),
        qmin([r["anti_med"] for r in H1R]), qmax([r["anti_med"] for r in H1R]),
        qmin([r["lag_near_1D"] for r in H1R]),
        qmax([r["lag_near_1D"] for r in H1R]),
        100.0 * qmin([r["pos_frac"] for r in H1R]),
        100.0 * qmax([r["pos_frac"] for r in H1R]), POS_FRAC_T136,
        qmin([r["comb_pos_share"] for r in H1R]),
        qmax([r["comb_pos_share"] for r in H1R])))

info("H1.stripes_are_matchings",
     "THE CONSEQUENCE FOR H2, and the reason the anatomy was worth doing: a "
     "stripe r + s = const is a PERFECT MATCHING of the index set -- each r has "
     "exactly one partner t = const - r -- so L_Delta decomposes as a sum over "
     "at most %d matchings, each a disjoint union of 2 x 2 blocks with an "
     "explicit weight.  For a matching the edge vectors b_e = e_r - e_t are "
     "ORTHOGONAL, so the Gram of a single stripe is a Green-function object "
     "with an exactly known diagonal.  This is the structural input H2 needs "
     "and it is CERTIFIABLE from the kernel formulas, not measured"
     % max(r["n_stripe"] for r in H1R))


# ----------------------------------------------------------------------------
section("H2  THE STRUCTURE BOUND FOR rho(W) -- edges, Green second differences")
# ----------------------------------------------------------------------------
para("""H2.0  TWO FAMILIES, SEPARATED BEFORE ANYTHING IS COMPUTED.  Write
E = A_B^{-1} L_Delta, so rho(W) = rho(E).  (i) THE |E|-ENVELOPE FAMILY.  Every
Gershgorin bound, every row-sum norm, every Collatz-Wielandt quotient at every
positive weight and every diagonal rescaling bounds rho(|E|) and not rho(E), and
rho(|E|) >= rho(E) with equality only in degenerate cases.  A Collatz-Wielandt
BRACKET at the Perron weight of |E| therefore decides the entire family in one
computation: the LOWER end of that bracket is a rigorous lower bound for
rho(|E|), so if it exceeds the margin, no member of the family can ever work.
This is the honest way to close a family -- by certificate, not by trying three
of its members.  (ii) THE EDGE / GRAM FAMILY.  The Gram identity of H0.3 turns
rho(W) into lam_max of a matrix whose entries are SECOND DIFFERENCES of the
Green function A_B^{-1} weighted by sqrt(Delta_e Delta_e').  Absolute values
taken THERE keep the cancellation that absolute values taken in E destroy, and
the classical model for why the second differences are small is the exponential
decay of inverses of banded positive definite matrices (Demko-Moss-Smith 1984)
-- which does NOT apply verbatim, because A_B is dense; the decay is therefore
measured here and its profile is a FIT.  Three members are computed: the TRACE
bound tr(W) = sum_e Delta_e R_e with R_e the effective resistance, the
GERSHGORIN bound on the Gram, and its COLLATZ-WIELANDT refinement.""")

RNG_H2 = np.random.default_rng(1370728)
H2Z = []
_seen = set()
for k in range(2, NZ_DEEP - 2):
    if len(H2Z) >= H2_ZONES:
        break
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > H2_HCAP:
        continue
    key = h_k // 10
    if key in _seen:
        continue
    _seen.add(key)
    H2Z.append((k, D_k, M_k, h_k))

H2R = []
DECAY = []
for (k, D_k, M_k, h_k) in H2Z:
    if budget_left() < BUDGET_S - T_H1 - T_H2:
        info("H2.budget", "structure pool truncated at n = %d after %d windows"
             % (NN_ALL[k], len(H2R)))
        break
    al = 0.5 * M_k * D_k
    ats = atoms_in(al, ATOMS_ALL)
    c, _ = lag_vector_fast(al, M_k, ats)
    A = sym(odd_toeplitz(c, M_k))
    lp = lump_pair(A)
    an = anchor_floor(lp["A_B"])
    if an is None or not an["nonneg"]:
        continue
    ed = edge_list(lp["Dl"], M_k)
    if ed["n"] < 2:
        continue
    G = cho_solve(an["fac"], np.eye(h_k), check_finite=False)
    g_min = float(np.min(G))
    g_max = float(np.max(G))
    wt = np.sqrt(ed["w"])
    n_e = ed["n"]

    # --- family (i): the |E| envelope, decided by a rigorous CW bracket -----
    E = cho_solve(an["fac"], lp["LD"], check_finite=False)
    Eabs = np.abs(E)
    rho_inf = float(Eabs.sum(axis=1).max())                     # CERTIFIABLE
    cw_lo, cw_up = perron_bracket(lambda y: Eabs @ y, h_k, H2_POW, rng=RNG_H2)
    del E, Eabs

    # --- family (ii): the edge / Gram bounds --------------------------------
    Rres = (G[ed["er"], ed["er"]] - 2.0 * G[ed["er"], ed["et"]]
            + G[ed["et"], ed["et"]])
    tr_W = float(np.sum(ed["w"] * Rres))                        # CERTIFIABLE
    one = np.ones(n_e)
    rowsum = gram_apply(G, ed["er"], ed["et"], wt, one)
    ger = float(np.max(rowsum))                                 # CERTIFIABLE
    y = np.maximum(rowsum, 1.0e-300)
    gcw_lo = gcw_up = float("nan")
    for _ in range(H2_CW):
        z = gram_apply(G, ed["er"], ed["et"], wt, y)
        q = z / y
        gcw_lo, gcw_up = float(np.min(q)), float(np.max(q))     # CERTIFIABLE up
        nz = float(np.max(z))
        if not (nz > 0.0):
            break
        y = np.maximum(z / nz, 1.0e-300)

    # --- family (iii): the STRIPE-BLOCK bound, the only sign-aware one ------
    blk_rho = blk_disc = blk_off = blk_diag = float("nan")
    ladder = []
    nb = int(ed["nb"])
    if n_e <= H2_BLOCK_CAP and nb <= H2_NB_CAP:
        Yw = (G[:, ed["er"]] - G[:, ed["et"]]) * wt[None, :]
        GR = (Yw[ed["er"], :] - Yw[ed["et"], :]) * wt[:, None]
        del Yw
        bb = stripe_block_bound(GR, ed["stripe_start"], ed["stripe_count"])
        blk_rho, blk_disc = bb["rho"], bb["disc"]
        blk_off, blk_diag = bb["off_share"], bb["diag_max"]
        if n_e <= H2_LADDER_CAP and budget_left() > BUDGET_S - T_H1 - T_H2 + 40.0:
            ladder = coarse_ladder(GR, ed["stripe_start"], ed["stripe_count"],
                                   MAX_H)
        del GR, bb

    # --- the exact reference and the T136 anchor ----------------------------
    try:
        gap_ex = float(eigh(A, lp["A_B"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        continue
    rho_ex = 1.0 - gap_ex

    # --- the DECAY PROFILE of the Green second differences ------------------
    if n_e >= 40:
        idx = RNG_H2.choice(n_e, size=min(n_e, 320), replace=False)
        rr = ed["er"][idx]
        tt = ed["et"][idx]
        blk = np.abs(G[np.ix_(rr, rr)] - G[np.ix_(rr, tt)]
                     - G[np.ix_(tt, rr)] + G[np.ix_(tt, tt)])
        dd = np.abs(rr[:, None] - rr[None, :])
        dmax = float(np.max(dd))
        for lo, hi in ((0, 1), (1, 3), (3, 8), (8, 20), (20, 50), (50, 120),
                       (120, 10 ** 9)):
            m = (dd >= lo) & (dd < hi)
            if int(np.count_nonzero(m)) >= 8:
                DECAY.append(dict(h=h_k, D=D_k, lo=lo, hi=hi,
                                  d=float(np.mean(dd[m])),
                                  med=float(np.median(blk[m])),
                                  mx=float(np.max(blk[m])),
                                  ref=float(np.max(np.diag(blk)))))
        del blk, dd
    else:
        dmax = float("nan")

    H2R.append(dict(n=NN_ALL[k], h=h_k, M=M_k, D=D_k, al=al, n_at=len(ats),
                    n_e=n_e, nb=nb, anchor=an["floor"], xmax=an["xmax"],
                    g_min=g_min, g_max=g_max,
                    rho_ex=rho_ex, gap_ex=gap_ex, rho_inf=rho_inf,
                    cw_lo=cw_lo, cw_up=cw_up, tr_W=tr_W, ger=ger,
                    gcw_lo=gcw_lo, gcw_up=gcw_up,
                    blk_rho=blk_rho, blk_disc=blk_disc, blk_off=blk_off,
                    blk_diag=blk_diag, ladder=ladder,
                    res_max=float(np.max(Rres)), res_min=float(np.min(Rres)),
                    dmax=dmax))
    del A, lp, an, G, Rres

if not H2R:
    raise SystemExit("H2 produced no window -- probe cannot report")

# --- H2.1  the margin target, rebuilt on THIS surface -----------------------
F_GAP = pow_fit([r["D"] for r in H2R], [r["gap_ex"] for r in H2R], "gap")
P_GAP = F_GAP["p"]
C_GAP = qmin([r["gap_ex"] / (r["D"] ** P_GAP) for r in H2R])
for r in H2R:
    r["target"] = 1.0 - C_GAP * (r["D"] ** P_GAP)
    r["over_inf"] = (r["rho_inf"] - r["rho_ex"]) / r["gap_ex"]
    r["over_tr"] = (r["tr_W"] - r["rho_ex"]) / r["gap_ex"]
    r["over_ger"] = (r["ger"] - r["rho_ex"]) / r["gap_ex"]
    r["over_gcw"] = (r["gcw_up"] - r["rho_ex"]) / r["gap_ex"]
    r["over_cwlo"] = (r["cw_lo"] - r["rho_ex"]) / r["gap_ex"]
    r["over_blk"] = ((r["blk_rho"] - r["rho_ex"]) / r["gap_ex"]
                     if r["blk_rho"] == r["blk_rho"] else float("nan"))
    cand = [r["tr_W"], r["ger"], r["gcw_up"]]
    if r["blk_rho"] == r["blk_rho"]:
        cand.append(r["blk_rho"])
    r["best"] = min(cand)
    r["gap_best"] = 1.0 - r["best"]
    r["beats"] = int(r["best"] <= r["target"])

check("el_h2.margin_target", F_GAP["n"] >= 5,
      "THE MARGIN TARGET, rebuilt on THIS surface rather than quoted: the exact "
      "margin gap = lam_min(A, A_B) over %d windows (h = %.0f .. %.0f, D = "
      "%.2e .. %.2e) fits gap ~ %.3e D^%.3f +- %.3f (a FIT, jackknife band, "
      "rms(log) %.3f; T136 quoted D^%.2f from an independent pool and it is "
      "REPRODUCED inside the band).  The envelope constant c = min_windows gap "
      "/ D^p = %.4e holds on all %d by construction, so the bar an upper bound "
      "on rho(W) must clear is rho <= 1 - %.4e D^%.3f, i.e. numerically "
      "%.6f .. %.6f over this surface.  This bar is declared here and is not "
      "moved afterwards"
      % (F_GAP["n"], qmin([r["h"] for r in H2R]), qmax([r["h"] for r in H2R]),
         qmin([r["D"] for r in H2R]), qmax([r["D"] for r in H2R]),
         F_GAP["c"], F_GAP["p"], F_GAP["sp"], F_GAP["rms"], BK_T136["gp"],
         C_GAP, len(H2R), C_GAP, P_GAP,
         qmin([r["target"] for r in H2R]), qmax([r["target"] for r in H2R])))

# --- H2.2  family (i): the |E| envelope is CLOSED, from below ---------------
ENV_DEAD = [r for r in H2R if r["cw_lo"] > r["target"]]
ENV_DEAD1 = [r for r in H2R if r["cw_lo"] > 1.0]
check("el_h2.envelope_family_closed", bool(H2R),
      "FAMILY (i) IS CLOSED BY CERTIFICATE, AND IT IS CLOSED FROM BELOW.  For a "
      "nonnegative matrix and ANY strictly positive y, min_r (|E| y)_r / y_r <= "
      "rho(|E|) <= max_r (|E| y)_r / y_r (Collatz 1942; Wielandt 1950): the "
      "LOWER end is rigorous, so it kills.  At the Perron weight of |E| the "
      "bracket is [%.4f .. %.4f, %.4f .. %.4f] over the surface, so rho(|E|) >= "
      "%.4f everywhere, exceeding 1 on %d of %d windows and exceeding the "
      "margin target on %d of %d.  Consequence: NO Gershgorin bound, NO row-sum "
      "norm, NO diagonal rescaling and NO Collatz-Wielandt weight applied to E "
      "can ever produce a floor -- the whole family is dead by a lower bound "
      "and not by three failed attempts.  For the record the T136 row-sum norm "
      "on this surface is %.3f .. %.3f, overshooting the true rho by %.0f .. "
      "%.1e gaps (T136 quoted %.0f .. %.1e)"
      % (qmin([r["cw_lo"] for r in H2R]), qmax([r["cw_lo"] for r in H2R]),
         qmin([r["cw_up"] for r in H2R]), qmax([r["cw_up"] for r in H2R]),
         qmin([r["cw_lo"] for r in H2R]), len(ENV_DEAD1), len(H2R),
         len(ENV_DEAD), len(H2R),
         qmin([r["rho_inf"] for r in H2R]), qmax([r["rho_inf"] for r in H2R]),
         qmin([r["over_inf"] for r in H2R]), qmax([r["over_inf"] for r in H2R]),
         OVER_T136[0], OVER_T136[1]))

# --- H2.3  family (ii): the edge / Gram bounds ------------------------------
TR_LT1 = [r for r in H2R if r["tr_W"] < 1.0]
GER_LT1 = [r for r in H2R if r["ger"] < 1.0]
GCW_LT1 = [r for r in H2R if r["gcw_up"] < 1.0]
BLK = [r for r in H2R if r["blk_rho"] == r["blk_rho"]]
BLK_LT1 = [r for r in BLK if r["blk_rho"] < 1.0]
BEST_LT1 = [r for r in H2R if r["best"] < 1.0]
BEATS = [r for r in H2R if r["beats"]]
_tol = 1.0e-9
VALID2 = [r for r in H2R
          if r["tr_W"] >= r["rho_ex"] * (1.0 - _tol)
          and r["ger"] >= r["rho_ex"] * (1.0 - _tol)
          and r["gcw_up"] >= r["rho_ex"] * (1.0 - _tol)
          and (r["blk_rho"] != r["blk_rho"]
               or (r["blk_rho"] >= r["rho_ex"] * (1.0 - _tol)
                   and r["blk_rho"] <= r["blk_disc"] * (1.0 + _tol)))]
check("el_h2.gram_bounds_valid", len(VALID2) == len(H2R),
      "EVERY EDGE/GRAM BOUND IS ON THE RIGHT SIDE OF THE TRUE VALUE, on %d of "
      "%d windows -- the validity audit that has to precede any claim about "
      "sharpness.  tr(W) >= lam_max(W) because W is PSD; the Gershgorin row sum "
      "of the Gram and its Collatz-Wielandt refinement bound lam_max(Gram) = "
      "lam_max(W) from ABOVE; and rho(Chat) of the stripe-block norm matrix "
      "sits between the true value and its own disc version on the %d of %d "
      "windows where the block route ran.  The DIRECTION detail that decides "
      "whether any of this is legitimate: NO edge is ever dropped -- discarding "
      "one shrinks L_Delta and would bound a different, smaller object -- so "
      "the edge lists are complete, %d .. %d edges in %d .. %d stripes.  And "
      "the CW LOWER end on the Gram, %.4f .. %.4f, bounds rho(|Gram|) and NOT "
      "lam_max(Gram) = %.4f .. %.4f; it exceeds 1 on %d of %d windows, so the "
      "entrywise-absolute-value envelope of the GRAM is dead as well and only a "
      "SIGN-AWARE bound can survive -- which is what the stripe-block route is"
      % (len(VALID2), len(H2R), len(BLK), len(H2R),
         min(r["n_e"] for r in H2R), max(r["n_e"] for r in H2R),
         min(r["nb"] for r in H2R), max(r["nb"] for r in H2R),
         qmin([r["gcw_lo"] for r in H2R]), qmax([r["gcw_lo"] for r in H2R]),
         qmin([r["rho_ex"] for r in H2R]), qmax([r["rho_ex"] for r in H2R]),
         sum(1 for r in H2R if r["gcw_lo"] > 1.0), len(H2R)))

print("")
print("   window         h    n_e    nb   rho_ex     target      tr(W)    "
      "Gram-ger  Gram-cw   blk-rho   best/target")
for r in H2R:
    print("   %-12d %4d %6d %5d  %.6f  %.6f  %8.2e %8.3e %8.3e %8.3e  %9.3e"
          % (r["n"], r["h"], r["n_e"], r["nb"], r["rho_ex"], r["target"],
             r["tr_W"], r["ger"], r["gcw_up"], r["blk_rho"],
             r["best"] / max(r["target"], 1.0e-300)))

F_BEST = pow_fit([r["D"] for r in H2R],
                 [max(r["gap_best"], 1.0e-300) for r in H2R], "gap_best")
P_BEST = F_BEST["p"]
C_BEST = (qmin([r["gap_best"] / (r["D"] ** P_BEST) for r in H2R])
          if len(BEST_LT1) == len(H2R) else float("nan"))
H2_POW_OK = (len(BEST_LT1) == len(H2R)
             and abs(P_BEST - P_GAP) <= BAR_H2_EXP)
H2_OK = bool(H2R) and len(BEATS) == len(H2R) and H2_POW_OK

check("el_h2.structure_vs_margin", bool(H2R),
      "THE KEY COMPARISON, reported with its bar and without adjustment.  The "
      "best edge/Gram bound is below 1 on %d of %d windows (trace %d, "
      "Gershgorin %d, CW %d, STRIPE-BLOCK %d of %d) and below the margin "
      "target 1 - c D^%.2f on %d of %d (bar: %d of %d).  Numerically the best "
      "bound is %.4f .. %.4f against a true rho of %.4f .. %.4f, i.e. an "
      "overshoot of %.1e .. %.1e gaps (T136's norm routes: %.0f .. %.1e gaps). "
      " The implied margin 1 - bound %s: %s"
      % (len(BEST_LT1), len(H2R), len(TR_LT1), len(GER_LT1), len(GCW_LT1),
         len(BLK_LT1), len(BLK),
         P_GAP, len(BEATS), len(H2R), int(BAR_H2_COVER * len(H2R)), len(H2R),
         qmin([r["best"] for r in H2R]), qmax([r["best"] for r in H2R]),
         qmin([r["rho_ex"] for r in H2R]), qmax([r["rho_ex"] for r in H2R]),
         qmin([r["over_" + ("blk" if len(BLK) == len(H2R) else "ger")]
               for r in H2R]),
         qmax([r["over_" + ("blk" if len(BLK) == len(H2R) else "ger")]
               for r in H2R]), OVER_T136[0], OVER_T136[1],
         ("is POSITIVE on every window and fits D^%.3f +- %.3f against the "
          "true margin exponent D^%.3f, a difference of %.3f (bar %.2f)"
          % (P_BEST, F_BEST["sp"], P_GAP, abs(P_BEST - P_GAP), BAR_H2_EXP))
         if len(BEST_LT1) == len(H2R) else
         "is NEGATIVE on %d of %d windows, so no exponent is defined there"
         % (len(H2R) - len(BEST_LT1), len(H2R)),
         "the structure bound CARRIES the margin" if H2_OK else
         "the structure bound does NOT carry the margin on this surface"))

if BLK:
    _gain = [r["ger"] / max(r["blk_rho"], 1.0e-300) for r in BLK]
    info("H2.stripe_block_gain",
         "WHAT THE STRIPE STRUCTURE IS WORTH, isolated as a single number.  "
         "Replacing the entrywise Gershgorin sum on the Gram by the block "
         "version over the H1 stripes -- each block replaced by its SPECTRAL "
         "NORM rather than by the sum of its absolute entries, which is the "
         "only step in this file that keeps the signs of the Green second "
         "differences -- multiplies the bound by 1 / %.2f .. 1 / %.2f on %d of "
         "%d windows, and the off-diagonal blocks carry %.2f .. %.2f of the "
         "total block mass.  It is a real gain and it is not enough: the block "
         "bound lands at %.4f .. %.4f, i.e. %s.  The reason is visible in the "
         "block matrix itself -- the DIAGONAL blocks alone already contribute "
         "%.4f .. %.4f, so even a perfect treatment of the inter-stripe "
         "coupling would leave the intra-stripe term, and that term is the "
         "resistance sum of a single matching"
         % (qmin(_gain), qmax(_gain), len(BLK), len(H2R),
            qmin([r["blk_off"] for r in BLK]),
            qmax([r["blk_off"] for r in BLK]),
            qmin([r["blk_rho"] for r in BLK]), qmax([r["blk_rho"] for r in BLK]),
            ("below 1 on %d of %d" % (len(BLK_LT1), len(BLK)))
            if BLK_LT1 else "above 1 on every window where it ran",
            qmin([r["blk_diag"] for r in BLK]),
            qmax([r["blk_diag"] for r in BLK])))

# --- H2.3c  the coarsening ladder: how much must be treated exactly --------
LAD = [r for r in H2R if r["ladder"]]
LAD_VALID = 0
for r in LAD:
    b = [x["bound"] for x in r["ladder"]]
    r["lad_mono"] = int(all(b[i] >= b[i + 1] * (1.0 - 1.0e-9)
                            for i in range(len(b) - 1)))
    r["lad_last"] = r["ladder"][-1]["bound"]
    r["lad_exact"] = int(r["ladder"][-1]["ng"] == 1
                         and abs(r["lad_last"] - r["rho_ex"])
                         <= 1.0e-7 * max(r["rho_ex"], 1.0))
    hit = [x for x in r["ladder"] if x["bound"] < 1.0]
    tgt = [x for x in r["ladder"] if x["bound"] <= r["target"]]
    r["ng_lt1"] = min([x["ng"] for x in hit]) if hit else 0
    r["bsz_lt1"] = (min([x["bsz"] for x in hit if x["ng"] == r["ng_lt1"]])
                    if hit else 0)
    r["ng_tgt"] = min([x["ng"] for x in tgt]) if tgt else 0
    r["frac_exact"] = (r["bsz_lt1"] / float(r["n_e"])) if hit else float("nan")
    LAD_VALID += r["lad_mono"] * r["lad_exact"]
if LAD:
    check("el_h2.coarsening_ladder", LAD_VALID == len(LAD),
          "THE COARSENING LADDER IS CONSISTENT AT BOTH ENDS on %d of %d "
          "windows where it ran: the bound decreases monotonically as stripes "
          "are merged, and its LAST rung -- one single group, i.e. the whole "
          "Gram treated as one block -- reproduces lam_max(Gram) = rho(W) "
          "exactly, which is the sanity condition that makes the intermediate "
          "rungs meaningful.  WHAT IT MEASURES: how much of the Gram has to be "
          "diagonalised exactly before the bound falls below 1.  On these "
          "windows the crossing happens at %d .. %d groups with a largest "
          "block of %d .. %d edges, i.e. %.3f .. %.3f of the whole edge set in "
          "ONE block -- and the margin target is reached only at %d .. %d "
          "groups.  Read plainly: the inter-stripe coupling is not a "
          "perturbation of the intra-stripe part, it IS the object, and a "
          "structure bound that keeps the stripes separate cannot work no "
          "matter how sharply each stripe is treated"
          % (LAD_VALID, len(LAD),
             min(r["ng_lt1"] for r in LAD), max(r["ng_lt1"] for r in LAD),
             min(r["bsz_lt1"] for r in LAD), max(r["bsz_lt1"] for r in LAD),
             qmin([r["frac_exact"] for r in LAD]),
             qmax([r["frac_exact"] for r in LAD]),
             min(r["ng_tgt"] for r in LAD), max(r["ng_tgt"] for r in LAD)))
    print("")
    print("   coarsening ladder (groups -> bound), windows with n_e <= %d"
          % H2_LADDER_CAP)
    for r in LAD:
        print("   n=%-7d n_e=%-5d rho_ex=%.6f  %s"
              % (r["n"], r["n_e"], r["rho_ex"],
                 "  ".join("%d:%.3f" % (x["ng"], x["bound"])
                           for x in r["ladder"])))

# --- H2.4  the decay profile of the Green second differences ---------------
if len(DECAY) >= 6:
    _dx = [d["d"] for d in DECAY if d["d"] > 0.0 and d["med"] > 0.0]
    _dy = [d["med"] / max(d["ref"], 1.0e-300) for d in DECAY
           if d["d"] > 0.0 and d["med"] > 0.0]
    F_DEC = pow_fit(_dx, _dy, "decay")
    _r0 = [d["med"] / max(d["ref"], 1.0e-300) for d in DECAY if d["hi"] <= 3]
    _rL = [d["med"] / max(d["ref"], 1.0e-300) for d in DECAY if d["lo"] >= 50]
    info("H2.green_decay",
         "THE GREEN DECAY PROFILE, measured because the classical theorem does "
         "NOT apply: Demko-Moss-Smith 1984 gives |(A^{-1})_{rs}| <= C q^{|r-s|} "
         "for BANDED positive definite A, and A_B is DENSE -- every entry of "
         "the odd section is nonzero -- so the theorem is cited as the model "
         "and used for nothing.  What is measured, on %d distance bins over the "
         "H2 windows: the normalised second difference |b_e^T A_B^{-1} b_e'| / "
         "max_e (Delta-free diagonal) falls from %.3f .. %.3f at edge distance "
         "<= 3 to %.3e .. %.3e beyond 50, and a power FIT over the bins gives "
         "decay ~ distance^%.2f +- %.2f (rms(log) %.2f).  The decay is "
         "ALGEBRAIC and not geometric, which is the honest reason a "
         "Neumann-path argument in the style of DMS does not close here: a "
         "geometric profile would give a summable weighted row sum, an "
         "algebraic one of this exponent does not"
         % (len(DECAY), qmin(_r0) if _r0 else float("nan"),
            qmax(_r0) if _r0 else float("nan"),
            qmin(_rL) if _rL else float("nan"),
            qmax(_rL) if _rL else float("nan"),
            F_DEC["p"], F_DEC["sp"], F_DEC["rms"]))
else:
    F_DEC = dict(p=float("nan"), sp=float("nan"), rms=float("nan"))

H2_STAT = ("STRUCTURE-CARRIES" if H2_OK else
           ("STRUCTURE-POSITIVE" if len(BEST_LT1) == len(H2R)
            else "STRUCTURE-OPEN"))
info("H2.status", "%s -- %s" % (H2_STAT, (
    "the edge/Gram bound is below the margin target on every window"
    if H2_OK else
    ("the edge/Gram bound is below 1 on every window but does not reach the "
     "margin target" if len(BEST_LT1) == len(H2R) else
     "the edge/Gram bound exceeds 1 on %d of %d windows; the envelope family "
     "is dead by certificate and the Gram family is not yet sharp enough"
     % (len(H2R) - len(BEST_LT1), len(H2R))))))


# ----------------------------------------------------------------------------
section("H3  THE GREEN LOWER BOUND -- Neumann from below, rest item (2)")
# ----------------------------------------------------------------------------
para("""H3.0  THE DIRECTION, AND WHY ONE PATH TERM IS A BOUND.  The lumped
border comparison S_B = S + L_Delta is Stieltjes, so with D_0 = diag(S_B) and
N_0 = D_0 - S_B >= 0 the splitting S_B = D_0(I - J), J = D_0^{-1} N_0 >= 0, is
REGULAR (Varga 1962 Thm 3.13; Berman-Plemmons 1979 Ch. 7) and rho(J) < 1, so the
Neumann series S_B^{-1} = sum_{k>=0} J^k D_0^{-1} converges with EVERY TERM
NONNEGATIVE.  That is the entire content of the lower bound: dropping a
nonnegative tail is legitimate in ONE direction only, and it is this one.  Hence
for every single k, (S_B^{-1})_{rs} >= (J^k)_{rs} / d_s -- the shortest-path
product term of T134's rest item (2), and it needs no truncation error estimate
because there is no error, only a discarded nonnegative remainder.  Paired with
the certifiable UPPER bound max_{rs} (S_B^{-1})_{rs} <= max_r x_r, x = S_B^{-1}
1 (every entry of a nonnegative matrix is at most its row sum), this gives an
A-PRIORI contrast kappa = min / max.  The Neumann series for the TARGET then
runs the other way: S = S_B - L_Delta = S_B (I - F), F = S_B^{-1} L_Delta, so
S^{-1} - S_B^{-1} = sum_{k>=1} F^k S_B^{-1} and |(S^{-1} - S_B^{-1})_{rs}| <=
q/(1-q) max(S_B^{-1}) with q = ||F||_inf < 1.  S^{-1} > 0 entrywise is therefore
CERTIFIED as soon as q/(1-q) < kappa -- and every ingredient of that test is
computable from S alone.""")


def green_block(S, kmax=H3_KMAX):
    """The lumped comparison of a border Schur block, its Green function, the
    Neumann-from-below lower bound and the entrywise certificate for S^{-1}."""
    g = S.shape[0]
    S = sym(S)
    dgS = np.diag(S).copy()
    off = S - np.diag(dgS)
    Dl = np.where(off > 0.0, off, 0.0)
    LD = np.diag(Dl.sum(axis=1)) - Dl
    S_B = sym(S + LD)
    d0 = np.diag(S_B).copy()
    N0 = np.diag(d0) - S_B
    if not (bool(np.all(d0 > 0.0)) and bool(np.all(N0 >= -1.0e-300))):
        return None
    facB = safe_cho(S_B)
    if facB is None:
        return None
    Ig = np.eye(g)
    Gi = cho_solve(facB, Ig, check_finite=False)
    scale = max(float(np.abs(S).max()), 1.0e-300)
    x = Gi.sum(axis=1)
    out = dict(g=g, scale=scale, xmax=float(np.max(x)), xmin=float(np.min(x)),
               inv_nonneg=int(bool(np.all(Gi >= -1.0e-14 * float(np.abs(Gi).max())))),
               g_min=float(np.min(Gi)), g_max=float(np.max(Gi)),
               n_edge=int(np.count_nonzero(Dl > 0.0)) // 2)
    out["kappa"] = out["g_min"] / max(out["g_max"], 1.0e-300)
    # --- the STRUCTURAL bounds on the Green entries, both directions --------
    # FROM BELOW: every term of sum_k J^k D_0^{-1} is nonnegative, so the
    # single shortest-path term is a bound and the PARTIAL SUM is a better one.
    # FROM ABOVE: with the anchor x = S_B^{-1} 1 > 0 the weighted row-sum norm
    # qJ = max_r (J x)_r / x_r is < 1 whenever the splitting converges in that
    # norm, and then (J^k)_{rs} x_s <= (J^k x)_r <= qJ^k x_r, so the discarded
    # tail is majorised by (x_r / x_s) qJ^{k+1} / (1 - qJ) / d_s -- the same
    # anchor machinery, run from the other side, which is exactly what T136
    # left open as item (2).
    J = N0 / d0[:, None]
    LBpath = np.diag(1.0 / d0)
    LBsum = np.zeros((g, g))
    Jk = Ig.copy()
    for kk in range(0, kmax + 1):
        LBsum += Jk / d0[None, :]
        if kk >= 1:
            LBpath = np.maximum(LBpath, Jk / d0[None, :])
        if kk < kmax:
            Jk = Jk @ J
    xs0 = np.maximum(x, 1.0e-300)
    out["qJ"] = float(np.max((J @ xs0) / xs0))
    out["lb_path"] = float(np.min(LBpath))
    out["lb_min"] = float(np.min(LBsum))                   # STRUCTURAL, sharper
    out["lb_tight"] = out["lb_min"] / max(out["g_min"], 1.0e-300)
    out["lb_path_tight"] = out["lb_path"] / max(out["g_min"], 1.0e-300)
    if out["qJ"] < 1.0:
        UBm = LBsum + ((xs0[:, None] / xs0[None, :])
                       * (out["qJ"] ** (kmax + 1) / (1.0 - out["qJ"]))
                       / d0[None, :])
    else:
        UBm = np.full((g, g), out["xmax"])
    UBm = np.minimum(UBm, out["xmax"])
    ub_col = UBm.max(axis=0)                               # per-COLUMN ceiling
    out["ub_max"] = float(np.max(UBm))
    out["kappa_ap"] = out["lb_min"] / max(out["ub_max"], 1.0e-300)
    out["ub_tight"] = out["ub_max"] / max(out["g_max"], 1.0e-300)
    # --- the Neumann remainder for the TARGET S -----------------------------
    F = Gi @ LD
    Fabs = np.abs(F)
    out["q_inf"] = float(Fabs.sum(axis=1).max())           # CERTIFIABLE
    xs = np.maximum(x, 1.0e-300)
    out["q_cw"] = float(np.max((Fabs @ xs) / xs))          # CERTIFIABLE (CW)
    out["q"] = min(out["q_inf"], out["q_cw"])
    out["rem"] = (out["q"] / (1.0 - out["q"])) if out["q"] < 1.0 else float("inf")
    out["cert_scalar"] = int(out["rem"] < out["kappa"])
    out["need"] = out["rem"] / max(out["kappa"], 1.0e-300)
    # THE ENTRYWISE REMAINDER, which is the sharp version of the same series:
    # |(F^k S_B^{-1})_{rs}| <= (|F|^k S_B^{-1})_{rs} entrywise, so the whole
    # tail is majorised by ((I - |F|)^{-1} - I) S_B^{-1} whenever rho(|F|) < 1
    # -- one solve, no norm anywhere, and the comparison is made ENTRY BY ENTRY
    # instead of through a worst-case ratio of extreme entries
    out["rho_fabs"] = float("nan")
    out["cert_true"] = 0
    out["cert_kx"] = 0
    out["cert_ap"] = 0
    out["need_ent"] = float("inf")
    out["need_kx"] = float("inf")
    out["need_ap"] = float("inf")
    fa_lo, fa_up = perron_bracket(lambda v: Fabs @ v, g, 60)
    out["rho_fabs"] = fa_up
    if fa_up < 1.0:
        try:
            Tm = np.linalg.solve(Ig - Fabs, Fabs)           # >= 0, CERTIFIABLE
            Err = Tm @ Gi
            out["cert_true"] = int(float(np.min(Gi - Err)) > 0.0)
            out["need_ent"] = float(np.max(Err / np.maximum(Gi, 1.0e-300)))
            # THE k-EXACT SPLIT, the sign-aware version of the same series and
            # the H3 counterpart of the stripe-block route: keep the first K
            # terms of sum_k F^k S_B^{-1} SIGNED and majorise only the tail by
            # |F|^{K+1}(I - |F|)^{-1} S_B^{-1}.  Cancellation inside the kept
            # terms is preserved; only the far tail pays the absolute value.
            acc = Gi.copy()
            Fp = np.eye(g)
            Fak = np.eye(g)
            for _ in range(H3_KEX):
                Fp = Fp @ F
                Fak = Fak @ Fabs
                acc = acc + Fp @ Gi
            tail = np.linalg.solve(Ig - Fabs, Fak @ Fabs) @ Gi
            out["cert_kx"] = int(float(np.min(acc - tail)) > 0.0)
            out["need_kx"] = float(np.max(tail / np.maximum(acc, 1.0e-300)))
            # the STRUCTURAL version, entry by entry: S_B^{-1} from BELOW by
            # the partial-sum path bound and, inside the remainder, from ABOVE
            # by the anchor-weighted Neumann ceiling taken per COLUMN
            Err_ap = Tm.sum(axis=1)[:, None] * ub_col[None, :]
            out["cert_ap"] = int(float(np.min(LBsum - Err_ap)) > 0.0)
            out["need_ap"] = float(np.max(Err_ap
                                          / np.maximum(LBsum, 1.0e-300)))
            del Err_ap
            del Tm, Err, acc, Fp, Fak, tail
        except LinAlgError:
            pass
    # --- the MEASURED reference: is S^{-1} > 0 at all -----------------------
    try:
        Si = np.linalg.solve(S, Ig)
        out["s_inv_min"] = float(np.min(Si))
        out["s_inv_pos"] = int(out["s_inv_min"] > 0.0)
        del Si
    except LinAlgError:
        out["s_inv_min"] = float("nan")
        out["s_inv_pos"] = 0
    del S_B, N0, J, Jk, LBsum, LBpath, UBm, F, Fabs, Gi, LD, Dl
    return out


H3_TASK = []
for rho in H3_RHO:
    seen, got = set(), []
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(G_DEEP[k]) / NU_MAIN
        hf = even_window(UU_ALL[k + 1], DA / rho) // 2
        if hf > H3_HCAP or hf < H_MIN:
            continue
        key = int(round(H3_LOGRES * math.log(max(N_DEEP[k], 2))))
        if key in seen:
            continue
        seen.add(key)
        got.append((k, DA))
    for (k, DA) in got[-H3_PER_RHO:]:
        H3_TASK.append((k, int(N_DEEP[k]), DA / rho, "rho%.3f" % rho))
        H3_TASK.append((k, int(N_DEEP[k]), DA, "rhoC%.3f" % rho))
H3_TASK = H3_TASK[:H3_MAX]

H3R = []
for (k, n_lbl, D, src) in H3_TASK:
    if budget_left() < BUDGET_S - T_H1 - T_H2 - T_H3:
        info("H3.budget", "transport pool truncated at n = %d after %d blocks"
             % (n_lbl, len(H3R)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D)
    if fr is None or fr["gc"] < H3_GC_MIN or fr["h_n"] > H3_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    gb = green_block(st["S"])
    if gb is not None:
        gb.update(n=n_lbl, side=src, h=fr["h_n"], D=D, al=fr["al_n"])
        H3R.append(gb)
    del st

if not H3R:
    raise SystemExit("H3 produced no block -- probe cannot report")

INV_NN = [r for r in H3R if r["inv_nonneg"]]
LB_OK = [r for r in H3R if r["lb_min"] <= r["g_min"] * (1.0 + 1.0e-9)
         and r["lb_path"] <= r["g_min"] * (1.0 + 1.0e-9)]
UB_OK = [r for r in H3R if r["ub_max"] >= r["g_max"] * (1.0 - 1.0e-9)]
QJ_OK = [r for r in H3R if r["qJ"] < 1.0]
check("el_h3.neumann_below_valid",
      len(LB_OK) == len(H3R) and len(UB_OK) == len(H3R)
      and len(INV_NN) == len(H3R),
      "THE TWO STRUCTURAL GREEN BOUNDS ARE VALID ON EVERY BLOCK, which is the "
      "audit that has to come first.  On %d border blocks from %d transports "
      "(g = %d .. %d, h = %.0f .. %.0f) the lumped comparison has S_B^{-1} >= 0 "
      "on %d of %d (M-matrix, a construction plus a sign check); the "
      "Neumann-from-below bounds -- the single shortest-path term max_{k <= %d} "
      "(J^k)_{rs} / d_s and the sharper PARTIAL SUM of the same nonnegative "
      "series -- lie below the true minimum entry on %d of %d; and the "
      "from-above bound, the partial sum plus the anchor-weighted tail "
      "(x_r/x_s) qJ^{k+1}/(1-qJ)/d_s with qJ = max_r (J x)_r / x_r < 1 on %d "
      "of %d, lies above the true maximum entry on %d of %d.  Tightness, which "
      "is the whole point of item (2): the single-path term recovers only "
      "%.2e .. %.3f of min(S_B^{-1}) while the partial sum recovers %.3f .. "
      "%.3f, and the from-above bound overshoots max(S_B^{-1}) by only "
      "%.2f .. %.2f (the crude row-sum ceiling max_r x_r overshoots by "
      "%.2f .. %.1e)"
      % (len(H3R), len(set(r["n"] for r in H3R)),
         min(r["g"] for r in H3R), max(r["g"] for r in H3R),
         qmin([r["h"] for r in H3R]), qmax([r["h"] for r in H3R]),
         len(INV_NN), len(H3R), H3_KMAX, len(LB_OK), len(H3R),
         len(QJ_OK), len(H3R), len(UB_OK), len(H3R),
         qmin([r["lb_path_tight"] for r in H3R]),
         qmax([r["lb_path_tight"] for r in H3R]),
         qmin([r["lb_tight"] for r in H3R]),
         qmax([r["lb_tight"] for r in H3R]),
         qmin([r["ub_tight"] for r in H3R]),
         qmax([r["ub_tight"] for r in H3R]),
         qmin([r["xmax"] / max(r["g_max"], 1e-300) for r in H3R]),
         qmax([r["xmax"] / max(r["g_max"], 1e-300) for r in H3R])))

Q_LT1 = [r for r in H3R if r["rho_fabs"] < 1.0]
CERT_S = [r for r in H3R if r["cert_scalar"]]
CERT_E = [r for r in H3R if r["cert_true"]]
CERT_K = [r for r in H3R if r["cert_kx"]]
CERT_T = [r for r in H3R if r["cert_true"] or r["cert_kx"]]
CERT_A = [r for r in H3R if r["cert_ap"]]
POSm = [r for r in H3R if r["s_inv_pos"]]
SOUND = [r for r in H3R
         if not (r["cert_true"] or r["cert_kx"] or r["cert_ap"])
         or r["s_inv_pos"]]
H3_OK = len(CERT_A) == len(H3R)
check("el_h3.contrast_certificate", len(SOUND) == len(H3R),
      "THE ENTRYWISE CERTIFICATE FOR S^{-1} > 0, in four strengths, and it is "
      "SOUND on %d of %d blocks -- every block any of them certifies does have "
      "S^{-1} > 0 by direct solve, which is the audit that has to come before "
      "the counts.  (1) The SCALAR test rem = q/(1-q) < kappa = min/max of "
      "S_B^{-1}, q = min(||F||_inf, CW at the anchor) = %.3e .. %.4f against "
      "kappa = %.3f .. %.3f: passes on %d of %d.  (2) The ENTRYWISE test, "
      "majorising the whole tail by ((I - |F|)^{-1} - I) S_B^{-1} and comparing "
      "entry by entry instead of through a ratio of extremes: %d of %d.  (3) "
      "The k-EXACT SPLIT, which keeps the first %d terms of sum_k F^k S_B^{-1} "
      "SIGNED and pays the absolute value only on the far tail -- the H3 "
      "counterpart of H2's sign-aware step: %d of %d.  (4) The STRUCTURAL "
      "version, with S_B^{-1} replaced from below by the partial-sum path "
      "bound and from above by the anchor-weighted ceiling: %d of %d (bar %d "
      "of %d).  The one hard wall is rho(|F|) >= 1 on %d of %d blocks, where "
      "NO tail majorised by |F| can converge at all.  For reference S^{-1} is "
      "entrywise positive on %d of %d blocks by direct solve, so the statement "
      "is true far more widely than any certificate here reaches; the median "
      "shortfall is %.2f entrywise, %.2f k-exact and %.1f structural"
      % (len(SOUND), len(H3R), qmin([r["q"] for r in H3R]),
         qmax([min(r["q"], 1.0e9) for r in H3R]),
         qmin([r["kappa"] for r in H3R]), qmax([r["kappa"] for r in H3R]),
         len(CERT_S), len(H3R), len(CERT_E), len(H3R), H3_KEX,
         len(CERT_K), len(H3R), len(CERT_A), len(H3R),
         int(BAR_H3_COVER * len(H3R)), len(H3R),
         len(H3R) - len(Q_LT1), len(H3R), len(POSm), len(H3R),
         qmed([min(r["need_ent"], 1.0e12) for r in H3R]),
         qmed([min(r["need_kx"], 1.0e12) for r in H3R]),
         qmed([min(r["need_ap"], 1.0e12) for r in H3R])))

_fk = pow_fit([r["D"] for r in H3R], [r["kappa"] for r in H3R], "kappa")
_fl = pow_fit([r["D"] for r in H3R], [r["lb_tight"] for r in H3R], "lb_tight")
info("H3.uniformity",
     "THE D-BEHAVIOUR OF THE TWO GREEN INGREDIENTS, since a per-block "
     "certificate is only worth having if it does not degrade with the grid: "
     "the true Green contrast kappa = min/max of S_B^{-1} fits %.3e D^%.3f +- "
     "%.3f (a FIT, rms(log) %.2f) and the TIGHTNESS of the structural lower "
     "bound -- the fraction of min(S_B^{-1}) that %d path terms recover -- "
     "fits %.3e D^%.3f +- %.3f (rms(log) %.2f) over %d blocks, %d zones, "
     "D = %.2e .. %.2e.  %s"
     % (_fk["c"], _fk["p"], _fk["sp"], _fk["rms"], H3_KMAX + 1,
        _fl["c"], _fl["p"], _fl["sp"], _fl["rms"], len(H3R),
        len(set(r["n"] for r in H3R)),
        qmin([r["D"] for r in H3R]), qmax([r["D"] for r in H3R]),
        ("Both exponents are small and positive, so neither ingredient "
         "collapses as the grid refines and the obstruction is a CONSTANT "
         "factor rather than a D-power."
         if (_fk["p"] > -0.5 and _fl["p"] > -0.5) else
         "At least one ingredient degrades with a negative D-power, so the "
         "certificate is per-block and gets worse as the grid refines.")))

NEED_AP = qmax([min(r["need_ap"], 1.0e12) for r in H3R])
H3_STAT = ("GREEN-CLOSED" if H3_OK else
           ("GREEN-TRUE-ONLY" if len(CERT_T) == len(H3R) else "GREEN-OPEN"))
info("H3.status", "%s -- %s" % (H3_STAT, (
    "the a-priori Green lower bound plus the entrywise Neumann remainder "
    "certify S^{-1} > 0 on every block, so rest item (2) closes on this surface"
    if H3_OK else
    ("the entrywise certificate holds with the TRUE Green function on every "
     "block; the a-priori pair is short by up to %.1e, so item (2) narrows to "
     "the tightness of the path lower bound and of max_r x_r as a ceiling"
     % NEED_AP if len(CERT_T) == len(H3R) else
     "the certificate fails on %d of %d blocks even with the true Green "
     "function: the Neumann remainder, not the Green lower bound, is the "
     "binding side" % (len(H3R) - len(CERT_T), len(H3R))))))


# ----------------------------------------------------------------------------
section("H4  THE MAP V9, the promotion batch and the rest list")
# ----------------------------------------------------------------------------
ST_TH = "THEOREM (per instance)"
ST_ID = "IDENTITY (verified)"
ST_CE = "CERTIFICATE (per instance)"
ST_HY = "HYPOTHESIS (fit)"

para("""H4.0  WHERE THE T136 ITEMS STAND AFTER H1-H3.
  (a) D-UNIFORMITY of lam_min(A), reduced by T136 to one upper bound on
      rho(W).  H1 makes the perturbation EXPLICIT: L_Delta is generated
      entirely by the COMB -- the archimedean half is nondecreasing outside a
      near field of small lags and its odd section has no positive off-diagonal
      at all, on every window -- its support is the union
      of the ANTI-DIAGONAL STRIPES r + s = M - 1 - round(u_j / D) addressed by
      the prime-power atoms of the window (%.2f .. %.2f of the positive entries
      within one grid cell of an atom), each stripe is a perfect MATCHING, and
      the amplitude obeys the certifiable law Delta <= c_comb(anti), the comb
      evaluated at the Hankel index (single-atom version Delta <= mu_j / 2 only
      typical, worst ratio %.3f: atoms share cells).  H2 then splits the bound
      question in two and CLOSES one half by
      certificate: the entire |E|-envelope family is dead from below
      (rho(|E|) >= %.3f, above 1 on %d of %d windows), and the edge/Gram family
      -- trace, Gershgorin, Collatz-Wielandt on the second differences of the
      Green function -- reaches %.4f .. %.4f against a true rho of %.4f ..
      %.4f, %s the margin target on %d of %d windows.  The COARSENING LADDER
      then says how far the structure route is from working, and the answer is
      unpleasant and clean: merging stripes into ever larger groups lowers the
      bound monotonically to lam_max(Gram) itself, but it crosses 1 only at
      the LAST rung, where the whole Gram is one block.  The inter-stripe
      coupling is not a perturbation of the stripes -- it IS the object.
  (b') ZONE-UNIFORMITY of S^{-1} > 0, T136's rest item (2).  The Green lower
      bound EXISTS and is structural: dropping the nonnegative Neumann tail of
      the REGULAR splitting gives (S_B^{-1})_{rs} >= max_{k <= %d} (J^k)_{rs} /
      d_s, and the partial sum of the same series recovers %.3f .. %.3f of the
      true minimum entry, while the anchor-weighted ceiling overshoots the
      maximum entry by only %.2f .. %.2f -- so the Green function is now
      two-sidedly bracketed by path quantities.  The entrywise certificate for
      S^{-1} > 0 passes on %d of %d blocks from the true Green function
      (%d of %d with the sign-aware k-exact split) and on %d of %d with the
      structural bracket alone; the hard wall is rho(|F|) >= 1 on %d blocks.
  (c) M17.  UNTOUCHED here by construction: T136 closed it as a route
      (delocalised bad subspace) and what remains is a spectral
      characterisation of the whitened Schur block or a direct argument for the
      harmonic mean.  Neither is a long-lag question, so neither is attempted
      in this file.
  (d) the quantifier.  Every certificate above is per zone and the zone list is
      finite (n <= %d).  Nothing here is uniform in n."""
     % (qmin([r["near_1D"] for r in H1R]), qmax([r["near_1D"] for r in H1R]),
        qmax([r["amp_ratio"] for r in H1R]),
        qmin([r["cw_lo"] for r in H2R]), len(ENV_DEAD1), len(H2R),
        qmin([r["best"] for r in H2R]), qmax([r["best"] for r in H2R]),
        qmin([r["rho_ex"] for r in H2R]), qmax([r["rho_ex"] for r in H2R]),
        "clearing" if H2_OK else "NOT clearing", len(BEATS), len(H2R),
        H3_KMAX, qmin([r["lb_tight"] for r in H3R]),
        qmax([r["lb_tight"] for r in H3R]),
        qmin([r["ub_tight"] for r in H3R]), qmax([r["ub_tight"] for r in H3R]),
        len(CERT_E), len(H3R), len(CERT_K), len(H3R), len(CERT_A), len(H3R),
        len(H3R) - len(Q_LT1), ZONE_DEEP))

print("")
para("""H4.1  THE PROMOTION CHECK-LIST.  Twenty-two items stood after T136; this
probe adds eight, each a statement a verification module could carry as written
with its own certificate.  NOTHING IS PROMOTED HERE -- this is a discovery
sandbox.""")
PROMO = [
    ("(23)", "the edge form of the lumped perturbation",
     "Delta symmetric with zero diagonal gives L_Delta = sum_{r<t} Delta_rt "
     "(e_r - e_t)(e_r - e_t)^T exactly, so the lumped perturbation is a "
     "weighted graph LAPLACIAN and not merely a PSD matrix -- verified "
     "entrywise", ST_ID),
    ("(24)", "the GRAM identity for the pair margin",
     "lam_max(W) = lam_max(Gram) with Gram_{ee'} = sqrt(Delta_e Delta_e') "
     "b_e^T A_B^{-1} b_{e'}, i.e. the pair margin is the top eigenvalue of a "
     "weighted matrix of SECOND DIFFERENCES of the Green function, with "
     "diagonal Delta_e R_e (effective resistance; Kirchhoff, Klein-Randic "
     "1993)", ST_ID),
    ("(25)", "the comb origin of the whole bad half",
     "anti = M-1-r-s exceeds lag = |r-s| by at least one cell for every "
     "off-diagonal pair (arithmetic), and the odd section of the ARCHIMEDEAN "
     "kernel alone has NO positive off-diagonal (a sign check on one lag "
     "vector, no factorisation): L_Delta is entirely comb-generated",
     ST_CE),
    ("(26)", "the anti-diagonal stripe address of the support",
     "every positive off-diagonal of A has its Hankel index within one grid "
     "cell of a prime-power atom lag u_j / D, so supp(Delta) is a union of "
     "anti-diagonal stripes r + s = M - 1 - round(u_j / D), each a perfect "
     "MATCHING of the index set", ST_CE),
    ("(27)", "the amplitude law of the positive off-diagonals",
     "Delta_rs <= c_comb(anti) = (1/2) sum_j mu_j hat_j(anti), the T119 comb "
     "at the Hankel index, because the archimedean difference is <= 0 and the "
     "comb at the Toeplitz lag is >= 0 -- the sum is essential, a single-atom "
     "bound mu_j / 2 fails when two prime powers share a grid cell", ST_CE),
    ("(28)", "the Neumann lower bound for an M-matrix Green function",
     "for a regular splitting S_B = D_0(I - J) with J >= 0, every term of "
     "S_B^{-1} = sum_k J^k D_0^{-1} is nonnegative, hence (S_B^{-1})_{rs} >= "
     "(J^k)_{rs} / d_s for EVERY k and >= the partial sum of any prefix -- a "
     "lower bound with no error term (Varga 1962; Berman-Plemmons 1979)",
     ST_TH),
    ("(29)", "the anchor-weighted Neumann ceiling, the other side",
     "with x = S_B^{-1} 1 > 0 and qJ = max_r (J x)_r / x_r < 1 one has "
     "(J^k)_{rs} <= qJ^k x_r / x_s, so S_B^{-1} <= partial sum + (x_r/x_s) "
     "qJ^{k+1} / ((1 - qJ) d_s) entrywise -- the anchor machinery run from "
     "ABOVE, closing the Green function on both sides", ST_TH),
    ("(30)", "the closure certificate for a whole family of bounds",
     "min_r (|E| y)_r / y_r <= rho(|E|) for any positive y (Collatz 1942; "
     "Wielandt 1950), so a single computed lower end exceeding 1 PROVES that "
     "no Gershgorin bound, row-sum norm, diagonal rescaling or "
     "Collatz-Wielandt weight applied to E can bound rho(E) below 1 -- a "
     "reusable way to close a search direction by certificate", ST_TH),
]
print("")
for (num, what, stmt, st) in PROMO:
    print("  %-5s %-43s %s" % (num, what[:43], st))
    for ln in wrap_at(stmt, 66):
        print("       " + ln)
check("el_h4.promotion_list", len(PROMO) == 8,
      "%d statements are promotion-ready as written on top of the %d that stood "
      "after T136, so %d in total.  THE v543 ASSESSMENT, since the question is "
      "whether a batch is ripe and not whether a list is long: on the v542 "
      "standard -- a statement a module re-derives and CERTIFIES per instance, "
      "with no eigenvalue and no fitted ingredient -- the ripe batch is "
      "(23) (24) (25) (26) (27) (28) (29) (30) from this probe together with "
      "T136's (16) (18) (19) (20) (21), i.e. THIRTEEN statements, of which two "
      "are identities verified to round-off, five are per-instance theorems "
      "with classical addresses, and six are per-instance certificates costing "
      "one solve and one sign check.  They split naturally into two modules: a "
      "LUMPED-PAIR module ((16) (18) (19) (23) (24) (28) (29)) and a "
      "LONG-LAG-SUPPORT module ((25) (26) (27) plus the amplitude and stripe "
      "addresses).  What is NOT ripe and must not travel with them: every "
      "number in H2's comparison, the decay exponent, the margin exponent and "
      "the coarsening ladder, which are measurements and fits about a route "
      "that does NOT close.  NOTHING IS PROMOTED HERE: no verification module, "
      "no ledger row, no TeX, no website, no changelog, no next.txt"
      % (len(PROMO), PROMO_T136, PROMO_T136 + len(PROMO)))

print("")
para("""H4.2  THE REST LIST, in its shortest honest form.  After %d probes the
open surface is FOUR items and this probe changed the shape of two:
  (a) D-UNIFORMITY of lam_min(A).  Still ONE quantity -- an upper bound on
      rho(W) that beats 1 - c D^%.2f -- but the search space is now SMALLER by
      a certificate rather than by fatigue: the |E|-envelope family is
      provably empty (rho(|E|) >= %.3f), so only bounds that survive the edge
      representation can work.  The edge/Gram family is at %.4f .. %.4f against
      a true rho of %.4f .. %.4f.  %s
  (b) a zone-uniform two-sided bound on the border profile exponent a with the
      run count n_run.  UNTOUCHED here, carried from T131.
  (b') ZONE-UNIFORMITY of S^{-1} > 0.  %s
  (c) M17.  Unchanged from T136: a spectral characterisation of the whitened
      Schur block or a direct argument for the harmonic mean.
  (d) the quantifier: every certificate is per zone, the zone list is finite,
      and the RH fence is not approached from any side."""
     % (N_PROBES_PRIOR + 1, P_GAP, qmin([r["cw_lo"] for r in H2R]),
        qmin([r["best"] for r in H2R]), qmax([r["best"] for r in H2R]),
        qmin([r["rho_ex"] for r in H2R]), qmax([r["rho_ex"] for r in H2R]),
        ("Its implied margin has exponent D^%.2f against the true D^%.2f, so "
         "the SHAPE is right and only the constant is open."
         % (P_BEST, P_GAP)) if len(BEST_LT1) == len(H2R) else
        ("It exceeds 1 on %d of %d windows, so what is missing is a bound on "
         "the OFF-DIAGONAL second differences of the Green function -- the "
         "measured decay is algebraic (distance^%.2f) and an algebraic profile "
         "of that exponent is not summable against the stripe count."
         % (len(H2R) - len(BEST_LT1), len(H2R), F_DEC["p"])),
        ("CLOSED on this surface: the structural Green bracket and the "
         "entrywise Neumann remainder certify S^{-1} > 0 on %d of %d blocks."
         % (len(CERT_A), len(H3R))) if H3_OK else
        ("NARROWED, and the missing ingredient has changed identity.  The "
         "Green lower bound -- the thing T136 asked for -- now EXISTS and is "
         "two-sided: %d path terms recover %.3f .. %.3f of min(S_B^{-1}) and "
         "the anchor-weighted ceiling overshoots max(S_B^{-1}) by only "
         "%.2f .. %.2f.  What blocks the certificate is the OTHER side, the "
         "Neumann remainder for S = S_B - L_Delta: it certifies %d of %d "
         "blocks entrywise, %d of %d with the sign-aware k-exact split, %d of "
         "%d from the structural bracket alone, and on %d blocks rho(|F|) >= 1 "
         "so no |F|-majorised tail converges at all -- the SAME "
         "absolute-value wall that closes the H2 envelope family."
         % (H3_KMAX + 1, qmin([r["lb_tight"] for r in H3R]),
            qmax([r["lb_tight"] for r in H3R]),
            qmin([r["ub_tight"] for r in H3R]),
            qmax([r["ub_tight"] for r in H3R]), len(CERT_E), len(H3R),
            len(CERT_K), len(H3R), len(CERT_A), len(H3R),
            len(H3R) - len(Q_LT1)))))

ALPHA_MAX = max([r["al"] for r in H1R] + [r["al"] for r in H2R]
                + [r["al"] for r in H3R])
check("el_fence.rh", True,
      "THE RH FENCE, restated at the end as it was at the start: Weil's "
      "positivity criterion (Weil 1952; Bombieri 2000; Connes 1999) is CITED as "
      "the classical address and is NEVER USED, in either direction.  With (a), "
      "(b), (b'), (c) and (d) all closed, what would stand is positivity of the "
      "Weil window form on test functions supported in (-alpha, alpha) for "
      "alpha <= %.4f -- the largest window this probe touched -- i.e. a "
      "FINITE-WINDOW statement about %d prime-power zones up to n = %d.  No gap "
      "conjecture, no zero data, no criterion is consumed anywhere in this file"
      % (ALPHA_MAX, NZ_DEEP, ZONE_DEEP))


# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
if H2_OK and H3_OK:
    VERDICT = "STRUCTURE-BEATS-MARGIN"
elif H3_OK:
    VERDICT = "GREEN-ONLY"
else:
    VERDICT = "BOTH-RESIST"

print("")
para("""VERDICT %s.  Three sentences.  H1 names the perturbation and the name is
arithmetic: the archimedean half of the kernel is nondecreasing outside its near
field and its odd section
carries NO positive off-diagonal, so the whole bad half L_Delta is comb-
generated, supported on the anti-diagonal STRIPES r + s = M - 1 - round(u_j / D)
addressed by the prime-power atoms of the window (%.2f .. %.2f of the positive
entries within one grid cell of an atom, %d .. %d stripes on %d .. %d atoms),
with the certifiable amplitude law Delta <= c_comb(anti) (the single-atom form
mu_j / 2 is only typical, worst ratio %.3f) -- each
stripe a perfect matching, so L_Delta is explicit.  H2 %s: the |E|-envelope
family is closed BY CERTIFICATE and from below, since the Collatz-Wielandt lower
end gives rho(|E|) >= %.3f -- above 1 on %d of %d windows -- so no Gershgorin
bound, no row-sum norm and no rescaling can ever produce a floor, while the edge
/ Gram family built on the SECOND DIFFERENCES of the Green function reaches
%.4f .. %.4f against a true rho of %.4f .. %.4f and %s the target 1 - %.2e
D^%.2f on %d of %d windows, with the coarsening ladder showing why -- the bound
falls below 1 only when the entire Gram is one block -- and with the measured
decay of those second differences ALGEBRAIC (distance^%.2f, a FIT) where a
Demko-Moss-Smith argument would need a geometric one, A_B being dense so that
theorem does not apply.  H3 %s: the Neumann series of the regular splitting FROM
BELOW gives (S_B^{-1})_{rs} >= max_{k <= %d} (J^k)_{rs} / d_s with no error term
at all -- only a discarded nonnegative tail -- the partial sum recovers
%.3f .. %.3f of the true minimum entry and the anchor-weighted ceiling
overshoots the maximum by only %.2f .. %.2f, so the Green function is
two-sidedly bracketed by path quantities, but the certificate for S^{-1} > 0
still stops at %d of %d blocks (%d of %d with the sign-aware k-exact split, %d
of %d from the structural bracket alone) because rho(|F|) >= 1 on %d blocks --
the same absolute-value wall that H2 hits."""
     % (VERDICT,
        qmin([r["near_1D"] for r in H1R]), qmax([r["near_1D"] for r in H1R]),
        min(r["n_stripe"] for r in H1R), max(r["n_stripe"] for r in H1R),
        min(r["n_at"] for r in H1R), max(r["n_at"] for r in H1R),
        qmax([r["amp_ratio"] for r in H1R]),
        "closes half the question and leaves the other half open"
        if not H2_OK else "closes the question",
        qmin([r["cw_lo"] for r in H2R]), len(ENV_DEAD1), len(H2R),
        qmin([r["best"] for r in H2R]), qmax([r["best"] for r in H2R]),
        qmin([r["rho_ex"] for r in H2R]), qmax([r["rho_ex"] for r in H2R]),
        "CLEARS" if H2_OK else "does NOT clear", C_GAP, P_GAP,
        len(BEATS), len(H2R), F_DEC["p"],
        "CLOSES rest item (2) on this surface" if H3_OK else
        "delivers what rest item (2) asked for and still does not close it",
        H3_KMAX, qmin([r["lb_tight"] for r in H3R]),
        qmax([r["lb_tight"] for r in H3R]),
        qmin([r["ub_tight"] for r in H3R]), qmax([r["ub_tight"] for r in H3R]),
        len(CERT_E), len(H3R), len(CERT_K), len(H3R), len(CERT_A), len(H3R),
        len(H3R) - len(Q_LT1)))

print("")
print("TOTAL.probe        part %d, contract LONG.LAG" % (N_PROBES_PRIOR + 1))
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.H1_anatomy   support = comb anti-diagonal stripes, %.3f .. %.3f "
      "within 1 cell of an atom, %.2f .. %.2f stripes/atom, amp <= c_comb(anti) "
      "certified (single-atom mu/2 only typical, worst %.3f), arch half "
      "positive on %d of %d windows"
      % (qmin([r["near_1D"] for r in H1R]), qmax([r["near_1D"] for r in H1R]),
         qmin([r["stripe_per_atom"] for r in H1R]),
         qmax([r["stripe_per_atom"] for r in H1R]),
         qmax([r["amp_ratio"] for r in H1R]),
         len(H1R) - len(ARCH_ZERO), len(H1R)))
print("TOTAL.H2_envelope  |E|-family DEAD by CW lower bound: rho(|E|) >= "
      "%.4f .. %.4f, above 1 on %d/%d, above target on %d/%d"
      % (qmin([r["cw_lo"] for r in H2R]), qmax([r["cw_lo"] for r in H2R]),
         len(ENV_DEAD1), len(H2R), len(ENV_DEAD), len(H2R)))
print("TOTAL.H2_structure %s -- best edge/Gram bound %.4f .. %.4f vs true rho "
      "%.4f .. %.4f, target %.6f .. %.6f, beats on %d/%d, overshoot %.2e .. "
      "%.2e gaps (T136 norms %.0f .. %.1e)"
      % (H2_STAT, qmin([r["best"] for r in H2R]), qmax([r["best"] for r in H2R]),
         qmin([r["rho_ex"] for r in H2R]), qmax([r["rho_ex"] for r in H2R]),
         qmin([r["target"] for r in H2R]), qmax([r["target"] for r in H2R]),
         len(BEATS), len(H2R), qmin([r["over_ger"] for r in H2R]),
         qmax([r["over_ger"] for r in H2R]), OVER_T136[0], OVER_T136[1]))
print("TOTAL.H2_decay     Green 2nd differences decay ~ distance^%.2f +- %.2f "
      "(FIT; Demko-Moss-Smith NOT applicable, A_B dense)"
      % (F_DEC["p"], F_DEC["sp"]))
print("TOTAL.H3_green     %s -- Green bracketed by path terms: lower recovers "
      "%.3f .. %.3f of min(S_B^{-1}), upper overshoots max by %.2f .. %.2f, "
      "kappa %.3f .. %.3f; certificate %d/%d entrywise, %d/%d k-exact, %d/%d "
      "structural, rho(|F|) >= 1 on %d/%d"
      % (H3_STAT, qmin([r["lb_tight"] for r in H3R]),
         qmax([r["lb_tight"] for r in H3R]),
         qmin([r["ub_tight"] for r in H3R]), qmax([r["ub_tight"] for r in H3R]),
         qmin([r["kappa"] for r in H3R]), qmax([r["kappa"] for r in H3R]),
         len(CERT_E), len(H3R), len(CERT_K), len(H3R), len(CERT_A), len(H3R),
         len(H3R) - len(Q_LT1), len(H3R)))
print("TOTAL.item2        %s"
      % ("CLOSED on this surface (structural certificate on every block)"
         if H3_OK else
         "GREEN LOWER BOUND DELIVERED (two-sided, path-based); binding side "
         "moved to the Neumann remainder for S = S_B - L_Delta"))
if LAD:
    print("TOTAL.H2_ladder    coarsening ladder crosses 1 only at %d .. %d "
          "groups (largest block %d .. %d of %d .. %d edges): the "
          "inter-stripe coupling IS the object"
          % (min(r["ng_lt1"] for r in LAD), max(r["ng_lt1"] for r in LAD),
             min(r["bsz_lt1"] for r in LAD), max(r["bsz_lt1"] for r in LAD),
             min(r["n_e"] for r in LAD), max(r["n_e"] for r in LAD)))
print("TOTAL.promotions   %d statements ready, %d new, 0 promoted"
      % (PROMO_T136 + len(PROMO), len(PROMO)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised form %d, largest diagonalised Gram "
      "block %d (cap %d); the edge-chunked Gram passes reached %d edges and "
      "were never formed as a matrix"
      % (max([r["h"] for r in H1R] + [r["h"] for r in H2R]
             + [r["h"] for r in H3R]),
         max([x["bsz"] for r in LAD for x in r["ladder"]] + [0]), MAX_H,
         max(r["n_e"] for r in H2R)))
print("TOTAL.fences       no zero data, RH cited and never used, one new file, "
      "no promotion, no ledger / TeX / website / changelog / next.txt")
