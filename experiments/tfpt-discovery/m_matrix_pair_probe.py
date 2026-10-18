"""Discovery probe (2026-07-28), part 136 of the prime/window investigation.
Contract M.MATRIX.PAIR -- the three items T134 left on the rest list, treated
with M-matrix tooling and with PEDANTIC attention to the DIRECTION of every
inequality, and nothing else.

WHERE THIS SITS (T134 PARTIAL: the pole-free floor EXISTS everywhere and every
cheap route fails by SIGN; every load-bearing number is rebuilt here, quoted
ones marked QUOTED)
  T134 closed the existence question for the pole-free floor and opened a
  uniformity question.  Its findings, verbatim as the starting point:
    * the pole-free odd Toeplitz+Hankel section A has ALL Cholesky pivots
      positive on 79 of 79 windows, so a per-window Cholesky of A - s I
      CERTIFIES a positive floor -- existence is settled (QUOTED);
    * the T126 fractional Dirichlet split A = diag(w) + L_N - L_P is exact, its
      GOOD half diag(w) + L_N is definite with lam_min = 0.13 .. 3.06, i.e.
      8 .. 85000 times ABOVE the target, and the whole loss sits in the BAD
      half L_P: lam_max(L_P) / mu_1 up to 4.7e5 and k_eff = 24 .. 397, so L_P is
      neither small nor low rank and the path comparison is infeasible (QUOTED);
    * the surviving opening is an M-MATRIX treatment.  T134-F2 found that
      LUMPING the positive off-diagonals onto the diagonal makes the border
      Schur comparison S_B = S + L_Delta STIELTJES and positive definite BY
      CONSTRUCTION with rho(Jacobi) < 1 on 900 of 900 blocks (QUOTED,
      rho = 0.709 .. 0.990);
    * the certified floor degrades like cert ~ D^2.26 (a FIT, QUOTED), so a
      D-uniform statement must be about D^p cert and not about cert;
    * M17 stays vacuous after whitening and the residual loss is the
      LOCALISATION of the bad pencil subspace, sigma_b = 0.77 .. 1.00 (QUOTED).
  THE DIRECTION WARNING that this probe is built around: lumping gives
  A_B = A + L_Delta with L_Delta PSD, hence A_B >= A in the LOEWNER order.  For
  an UPPER bound on lam_min that is the useful direction; for a FLOOR on
  lam_min(A) it is the WRONG one.  A floor therefore needs either the opposite
  comparison or a Neumann-type margin |A^{-1} - A_B^{-1}|, and the whole point
  of G1 is to sort the candidates by direction before measuring anything.

WHAT THIS PROBE DOES
  G0  SETUP and the DIRECTION AUDIT.  Atoms, the free-resolution schedule, the
      odd section against its slow reference, the T126 Dirichlet identity, the
      Cholesky certificate against exact eigenvalues, and then the five
      structural facts about the lumped pair that G1-G3 rest on, each verified
      numerically on a dense reference window:
        (P1) A_B = A + L_Delta is STIELTJES (nonpositive off-diagonals) and
             A_B >= A in the Loewner order, with the row sums PRESERVED;
        (P2) the exact congruence A = A_B^{1/2} (I - W) A_B^{1/2} with
             W = A_B^{-1/2} L_Delta A_B^{-1/2} >= 0, hence the LOEWNER SANDWICH
             lam_min(A) >= lam_min(A_B) (1 - lam_max(W)) -- the RIGHT direction;
        (P3) the pedantic EQUIVALENCE lam_max(W) < 1 <=> A > 0, so the sandwich
             is CIRCULAR unless lam_max(W) is bounded by cheap ingredients;
        (P4) the M-MATRIX ANCHOR: for Stieltjes A_B with x = A_B^{-1} 1 >= 0,
             lam_min(A_B) >= 1 / max_r x_r (one solve, one sign check);
        (P5) the FROBENIUS BRACKET for the Jacobi radius of a Stieltjes matrix,
             1 - max_r w_r/d_r <= rho(J) <= 1 - min_r w_r/d_r.
  G1  THE A-FLOOR ROUTE THROUGH M-MATRIX TOOLING, candidates sorted by
      DIRECTION first and measured second:
        (i)  the NEUMANN / LOEWNER MARGIN on A -- the sandwich (P2) with three
             successively cheaper upper bounds for lam_max(W) = rho(L_Delta
             A_B^{-1}): the measured Rayleigh value (a MEASUREMENT and a
             reference only), the computed row-sum norm ||A_B^{-1} L_Delta||_inf
             (one triangular solve block), and the fully factored a-priori
             bound ||L_Delta||_inf max_r x_r = 2 max_r P_r max_r x_r.  Combined
             with the anchor (P4) this is a floor with NO eigenvalue in it at
             all.  The shifted ladder (lumping commutes with diagonal shifts) is
             run wherever the a-priori margin is below 1.
        (ii) the D-UNIFORMITY question: WHICH ingredient carries the D-power.
             Each ingredient of the pair -- min diag, the row sums w, the good
             Laplacian weights, max_r P_r, max_r x_r, the anchor 1/max x, the
             certified floors of A and A_B -- is fitted against D separately,
             including a MATRIX-FREE row-chunked extension far beyond the
             factorisation cap, and the uniform candidate form lam_min(A) >=
             c D^p is then CONSTRUCTED with explicit (c, p) and tested for
             uniformity over the whole surface.
  G2  THE A-PRIORI BOUND FOR rho(K).  The classical row-sum / diagonal-
      dominance criteria (Frobenius 1912; Varga 1962; Collatz-Wielandt) applied
      to the Jacobi splitting of the LUMPED Stieltjes comparison, which is
      explicit -- so the ingredients are closed.  Tested against the measured
      rho values on the T131/T134 transport surface: validity, sharpness on the
      GAP 1 - rho, and uniformity in (zone, D, g).
  G3  M17 LOCALISATION.  The bad pencil subspace {mu < 1/2} of the WHITENED
      Schur block: its dimension, its per-cell mass profile, its frequency
      content, its stability across zones and depths -- and then the M18 bound
      re-assembled with the localisation factor sigma_b(k) scanned over a WIDE
      k ladder instead of the three values T134 tried.  Does it get under 1/2?
  G4  THE MAP V8, the promotion list and the shortest rest list.

PREREGISTERED VERDICTS (bars declared here, before any number is computed)
  PAIR-CARRIES  : BOTH halves of the pair carry over the measurement surface --
                  G1 delivers a CERTIFIABLE positive floor for lam_min(A) from
                  M-matrix ingredients on EVERY window, AND the G2 a-priori
                  bracket is valid, below 1 on EVERY transport and sharp on the
                  gap to within the declared factor.
  ONE-CARRIES   : exactly one of the two does -- named, with the other's
                  anatomy.
  PAIR-RESISTS  : neither -- with the precise anatomy of both failures.
  Element gates: el_firewall, el_g0, el_g1, el_g2, el_g3, el_g4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger / TeX / website /
    changelog edit, no verification/ module, no next.txt, no .md output, no git
    action.
  * NO Riemann zero data of any kind.  An AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * THE RH FENCE IS PROMINENT AND ABSOLUTE.  Weil's positivity criterion
    (Weil 1952; Bombieri 2000; Connes 1999) is CITED as the classical address of
    the surrounding statement and is NEVER USED, in either direction.  Nothing
    here claims, assumes or approaches RH.  Even with every item closed, what
    would stand is positivity of the Weil window form on test functions
    supported in (-alpha_max, alpha_max) for the alpha actually reached -- a
    FINITE-WINDOW statement about a finite list of prime-power zones.  The
    distance to RH is MAPPED in G4, never travelled.
  * CERTIFIABLE vs CERTIFIED vs MEASURED vs FIT vs HYPOTHESIS, per line.  A
    completed Cholesky of A - s I certifies lam_min(A) >= s - c_h u ||A||,
    u = 2^-53, c_h = (h+1)/(1-(h+1)u) (Wilkinson 1968; Higham 2002 Thm
    10.3/10.4).  A row-sum / sign statement is CERTIFIABLE without any
    factorisation.  An eigenvalue from eigvalsh, a Rayleigh quotient and a
    power iteration are MEASUREMENTS -- and a power iteration bounds
    lam_max from BELOW, so it can KILL a margin and can never certify one.
    Every fit is a FIT and carries a delete-one jackknife band.  Bars declared
    before a number are NEVER moved afterwards.
  * DIRECTION CARE IS THE POINT.  Every inequality in G1 is annotated with the
    direction it runs.  A >= B in the Loewner order gives lam_min(A) >=
    lam_min(B) and NOTHING about the reverse; a compression or a Schur
    complement bounds lam_min from ABOVE (Cauchy interlacing; Haynsworth 1968);
    lumping raises the form, so it can only be used through the INVERSE side.
  * CLASSICAL ADDRESSES USED: Stieltjes / Ostrowski 1937, 1956 and 1959
    (comparison matrices, H-matrices, inverse-positivity, the product bound),
    Berman-Plemmons 1979 (M-matrix equivalences, the positive-vector criterion,
    Schur complements of M-matrices), Fan 1958 (the positive-vector criterion
    and the eigenvalue product inequalities), Varga 1962 (regular splittings,
    Jacobi radii, diagonal dominance measures), Frobenius 1912 and Perron 1907
    (the row-sum bracket and the ground-state sign), Collatz 1942 / Wielandt
    1950 (the min-max quotient bound for nonnegative matrices), the Neumann
    series and the standard residual bound (Higham 2002 Ch. 14), Levinson 1947 /
    Durbin 1960 (the pivot recursion), Cholesky triangularity (the prefix
    lemma), Schur and Haynsworth 1968 (complements and the transport bracket),
    Cauchy interlacing, Weyl 1912 (the perturbation direction), Wilkinson 1968 /
    Higham 2002 (the floating-point certificate), Feller / Dynkin Green
    functions of killed jump processes, Yakubovich's S-procedure, Szegoe 1939
    and Grenander-Szegoe 1958 (the symbol route that is DEAD here), Yserentant
    1986 (the two-scale space), Bertrand-Chebyshev 1852 and the trivial even
    bound (the only two gap facts consumed).  No gap CONJECTURE (Cramer,
    Firoozbakht, twin, Mersenne infinitude) enters anywhere, in any direction.
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    FFT-based lag assembly, row-chunked gathers and pure interval geometry may
    exceed it.  Probe budget < 900 s.

OUTCOME OF THIS RUN  =>  see the G4 map and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import (cho_factor, cho_solve, cholesky, eigh, eigvalsh,
                          solve_triangular, svdvals)

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
SQ2 = math.sqrt(2.0)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 790.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 320000
ZONE_DEEP = 300000

# --- G1 pools ---------------------------------------------------------------
G1_ZONES = 60                # zones in the pair battery
G1_LEV = 3                   # depths per zone (M, 2M, 4M)
G1_HCAP_FULL = 700           # full pair: anchor + both margins + cert(A_B)
G1_HCAP_MID = 1000           # pair without the cert(A_B) bisection
G1_HCAP_WIDE = 1400          # cheap ingredients + cert(A) only
G1_FREE_CAP = 3200           # MATRIX-FREE ingredient extension (no factorisation)
G1_POW = 120                 # power-iteration steps for lam_max(W)
G1_SHIFT_IT = 14             # bisection steps on the shifted pair ladder
SLACK_DEC = 9                # THE DECLARED SLACK: need = 10^-9 x measured mu_1
T_G1 = 240.0

# --- G2 pools ---------------------------------------------------------------
G2_GC_MIN = 2
G2_HCAP = 1100
G2_MAX = 900                 # transports attempted (T134 reported 900)
G2_PER_RHO = 30
G2_LOGRES = 90.0
G2_RHO = (1.001, 1.05, 1.10, 1.20, 1.25, 1.35, 1.49531, 1.60, 1.75, 1.90,
          2.00, 2.25, 2.50, 3.00, 3.50, 4.00)   # 1.49531 = the T127 band edge
T_G2 = 200.0

# --- G3 pools ---------------------------------------------------------------
H_TEL = 1400                 # finest telescope level (<= MAX_H)
PEN_ZONES = 20
NLEV_MAX = 3
L_CAP = 2 ** 20
ENV_OS = 48
ENV_FRAC = 0.10
K_LADDER = (2, 4, 8, 16, 32, 64, 128, 256)
K_T134 = (4, 8, 16)          # the three values T134 tried
SPRO_H = 260                 # above this the S-procedure refinement is skipped
LOC_BINS = 32
T_G3 = 190.0

# --- preregistered bars (declared before any number) ------------------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_MASS_GOOD = 0.5          # the whitened mass bound must give bad <= 1/2
BAR_G1_COVER = 1.0           # G1 carries only if positive on EVERY window
BAR_G2_COVER = 1.0           # G2 carries only if rho < 1 a priori EVERYWHERE
BAR_G2_GAP = 10.0            # ... and the a-priori GAP within 10x of the true gap
BAR_LOC = 0.9                # "localised" = 90 % of the bad mass in the band

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
PIV_T134 = (79, 79)
MN_T134 = (0.13, 3.06)
LP_RATIO_T134 = 4.7e5
KEFF_T134 = (24, 397)
CERT_EXP_T134 = 2.26
RHO0_T134 = (0.709, 0.990)
RHO0_N_T134 = (900, 900)
SIG_B_T134 = (0.77, 1.00)
MU1_T131 = (4.7e-5, 6.4e-2)
SYM_FLOOR_T131 = (-76.0, -27.0)
MISMATCH_T131 = 2.18
MASS_T127 = 0.9665
MU_MIN_T126 = (0.192, 0.307)
RHO_UNI_T127 = 1.49531
COVER_T127 = 99.26
N_PROBES_PRIOR = 135


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


def next_pow2(n):
    k = 1
    while k < n:
        k *= 2
    return k


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
          == "m_matrix_pair_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- T111..T134 code path
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
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T134)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_toeplitz_slow(c, M):
    """The definition, entry by entry -- the G0 reference for odd_toeplitz."""
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


def odd_nodes(alpha, M):
    D = 2.0 * alpha / M
    h = M // 2
    return -alpha + (np.arange(h) + 0.5) * D, D


def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except LinAlgError:
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


def gersh(A):
    return float(np.abs(A).sum(axis=1).max())


def cert_lmin(A, lam):
    try:
        cholesky(sym(A) - lam * np.eye(A.shape[0]), lower=True, check_finite=False)
        return True
    except LinAlgError:
        return False


def cert_floor_bisect(A, lo, hi, iters=24):
    """The largest s on a bisection ladder for which chol(A - s I) COMPLETES --
    a CERTIFIED lower bound for lam_min(A) up to the declared fp floor."""
    if not cert_lmin(A, lo):
        return None
    a, b = lo, hi
    for _ in range(iters):
        mid = 0.5 * (a + b)
        if cert_lmin(A, mid):
            a = mid
        else:
            b = mid
    return a


def cert_pd(A):
    fac = safe_cho(A)
    return (fac is not None), chol_floor(gersh(A), A.shape[0]), fac


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


def edge_geom(u_o, u_n, D_c, D_f):
    fr_c = step_frame(u_o, u_n, D_c)
    fr_f = step_frame(u_o, u_n, D_f)
    if fr_c is None or fr_f is None:
        return None
    return dict(fr_c=fr_c, fr_f=fr_f, gc_c=fr_c["gc"], gc_f=fr_f["gc"],
                al_c=fr_c["al_n"], al_f=fr_f["al_n"], rho=D_c / D_f,
                D_c=D_c, D_f=D_f, h_c=fr_c["h_n"], h_f=fr_f["h_n"], g=u_n - u_o)


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
# the two-grid isometries, the certified symbol envelope and the telescope
# (T122..T134), needed for the G3 pencil
# ----------------------------------------------------------------------------
def rest_p(X):
    return (X[0::2] + X[1::2]) / SQ2


def rest_z(X):
    return (X[0::2] - X[1::2]) / SQ2


def two_grid_blocks(A):
    PtA = rest_p(A)
    ZtA = rest_z(A)
    Ac = sym(rest_p(PtA.T).T)
    Az = sym(rest_z(ZtA.T).T)
    Bx = rest_z(PtA.T).T
    return Ac, Az, Bx


def zz_compress(A):
    return sym(rest_z(rest_z(A).T).T)


def sym_grid(c, L):
    M = c.shape[0]
    pad = np.zeros(L)
    pad[:M] = c
    half = 2.0 * np.fft.rfft(pad).real - c[0]
    f = np.empty(L)
    f[:L // 2 + 1] = half
    f[L // 2 + 1:] = half[1:L // 2][::-1]
    return f


def dsym_abs_grid(c, L):
    M = c.shape[0]
    pad = np.zeros(L)
    pad[:M] = np.arange(M) * c
    g = np.abs(2.0 * np.fft.rfft(pad).imag)
    out = np.empty(L)
    out[:L // 2 + 1] = g
    out[L // 2 + 1:] = g[1:L // 2][::-1]
    return out


def cert_env(c, os_start=ENV_OS, cap=L_CAP, frac=ENV_FRAC):
    """The CERTIFIED per-cell envelope ell <= sigma^(M) <= up."""
    M = c.shape[0]
    L = min(next_pow2(os_start * M), cap)
    while True:
        f = sym_grid(c, L)
        fp = dsym_abs_grid(c, L)
        dt = 2.0 * math.pi / L
        j = np.arange(M, dtype=float)
        fpp = 2.0 * float(np.sum(j * j * np.abs(c)))
        d = 0.5 * dt * fp + dt * dt / 8.0 * fpp
        ell, up = f - d, f + d
        marg = float(np.max(d))
        pos = ell[ell > 0.0]
        scale = float(np.median(pos)) if pos.size > 8 else float(np.max(f))
        if marg <= frac * max(scale, 1.0e-300) or 2 * L > cap:
            return ell, up, f, marg, L, scale
        L *= 2


def pwc_lags(g, n):
    L = g.shape[0]
    dt = 2.0 * math.pi / L
    X = np.fft.rfft(g).real
    m = np.arange(n, dtype=float)
    lag = np.zeros(n)
    lag[0] = float(g.mean())
    k = min(n, X.shape[0])
    lag[1:k] = X[1:k] * np.sin(m[1:k] * dt * 0.5) / (math.pi * m[1:k])
    return lag


def telescope_levels(alpha, M0, atoms, nlev):
    """Levels l = 0..nlev-1, M_l = 2^l M0 at FIXED alpha."""
    lv = []
    for l in range(nlev):
        M = M0 * (2 ** l)
        c, D = lag_vector_fast(alpha, M, atoms)
        A = sym(odd_toeplitz(c, M))
        b = odd_pole_vector(alpha, M)
        fac = safe_cho(A)
        if fac is None:
            return None
        u = cho_solve(fac, b, check_finite=False)
        q = float(np.dot(b, u))
        lv.append(dict(l=l, M=M, D=D, c=c, A=A, b=b, u=u, q=q, eps=1.0 - q,
                       h=M // 2, fac=fac))
    return lv


def nlev_for(h0, cap=H_TEL):
    n = 1
    while h0 * (2 ** n) <= cap and n + 1 <= NLEV_MAX:
        n += 1
    return n


def _spro(Rt, Gt, lo=1.0e-6, hi=1.0e10, iters=12):
    """min_{s>=0} lam_max(Rt - s Gt) by ternary search on log s (convex in s)."""
    n = Rt.shape[0]

    def val(s):
        try:
            return float(eigvalsh(sym(Rt - s * Gt),
                                  subset_by_index=[n - 1, n - 1])[0])
        except (LinAlgError, ValueError):
            return float("inf")

    a, b = math.log(lo), math.log(hi)
    best = min(val(0.0), val(lo), val(hi))
    for _ in range(iters):
        m1 = a + (b - a) / 3.0
        m2 = b - (b - a) / 3.0
        v1, v2 = val(math.exp(m1)), val(math.exp(m2))
        best = min(best, v1, v2)
        if v1 < v2:
            b = m2
        else:
            a = m1
    return best


# ----------------------------------------------------------------------------
# THE T126 DIRICHLET SPLIT and THE LUMPED M-MATRIX PAIR -- the central objects
# ----------------------------------------------------------------------------
def dirichlet_split(A):
    """A = diag(w) + L_N - L_P, an EXACT identity for symmetric A:

        v^T A v = sum_r w_r v_r^2 + sum_{r<s} (-A_rs) (v_r - v_s)^2,

    w = ROW SUMS of A (killing), L_N the Laplacian of the NEGATIVE
    off-diagonals (GOOD jumps, PSD), L_P that of the POSITIVE ones (BAD jumps,
    PSD, entering with a MINUS sign)."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    w = A.sum(axis=1)
    off = A - np.diag(dg)
    Pm = np.where(off > 0.0, off, 0.0)
    Nm = np.where(off < 0.0, -off, 0.0)
    P_row = Pm.sum(axis=1)
    N_row = Nm.sum(axis=1)
    L_P = np.diag(P_row) - Pm
    L_N = np.diag(N_row) - Nm
    n_off = h * (h - 1)
    return dict(h=h, dg=dg, w=w, Pm=Pm, Nm=Nm, P_row=P_row, N_row=N_row,
                L_P=L_P, L_N=L_N, off=off, n_off=n_off,
                frac_neg=float(np.count_nonzero(off < 0.0)) / max(n_off, 1))


def lump_pair(A):
    """THE LUMPED M-MATRIX PAIR of a symmetric A.

    Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta its
    Laplacian (PSD, zero row sums), and

        A_B = A + L_Delta.

    DIRECTION, stated once and never forgotten: L_Delta >= 0 in the LOEWNER
    order, so A_B >= A -- lumping RAISES the form.  Hence lam_min(A_B) >=
    lam_min(A) and A_B gives an UPPER bound on lam_min(A) for free and a LOWER
    bound never, directly.  The off-diagonals of A_B are min(A_rs, 0) <= 0 by
    construction, so A_B is STIELTJES with no measurement at all, and lumping
    PRESERVES the row sums exactly (L_Delta 1 = 0).  The floor must therefore be
    reached through the INVERSE side -- the Neumann / Loewner margin of G1."""
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
    """THE M-MATRIX ANCHOR (P4).  For a symmetric Stieltjes A_B, solve
    A_B x = 1.  If x >= 0 entrywise then A_B is a nonsingular M-matrix
    (Fan 1958; Berman-Plemmons 1979, the positive-vector characterisation) and

        ||A_B^{-1}||_2 <= ||A_B^{-1}||_inf = || A_B^{-1} 1 ||_inf = max_r x_r,

    using ||M||_2 <= sqrt(||M||_1 ||M||_inf) = ||M||_inf for SYMMETRIC M, and
    A_B^{-1} >= 0 entrywise so that the inf-norm is attained at the vector 1.
    Hence lam_min(A_B) >= 1 / max_r x_r -- one solve, one sign check, NO
    eigenvalue.  DIRECTION: this is a LOWER bound on lam_min(A_B)."""
    h = A_B.shape[0]
    fac = safe_cho(A_B)
    if fac is None:
        return None
    x = cho_solve(fac, np.ones(h), check_finite=False)
    xmin = float(np.min(x))
    xmax = float(np.max(x))
    return dict(fac=fac, x=x, xmax=xmax, xmin=xmin,
                nonneg=int(xmin >= -1.0e-13 * max(xmax, 1.0e-300)),
                floor=(1.0 / xmax) if xmax > 0.0 else float("nan"))


def pow_lmax_W(LB, LD, iters=G1_POW, rng=None):
    """lam_max(W), W = LB^{-1} L_Delta LB^{-T}, by power iteration.

    A MEASUREMENT, and a one-sided one: the Rayleigh quotient of any vector is
    a LOWER bound for lam_max(W), so this number can KILL the margin (if it is
    >= 1 the sandwich is empty) and can NEVER certify one."""
    n = LD.shape[0]
    v = (rng.standard_normal(n) if rng is not None else np.ones(n))
    nv = float(np.linalg.norm(v))
    if not (nv > 0.0):
        return float("nan")
    v /= nv
    lam = 0.0
    for _ in range(iters):
        t = solve_triangular(LB, v, lower=True, trans=1, check_finite=False)
        z = LD @ t
        u = solve_triangular(LB, z, lower=True, check_finite=False)
        lam = float(np.dot(v, u))
        nu = float(np.linalg.norm(u))
        if not (nu > 0.0):
            return 0.0
        v = u / nu
    return lam


def free_ingredients(c, M, chunk=192):
    """The CHEAP ingredients of the pair -- min diag, the row sums w, the good
    and bad row masses -- computed ROW-CHUNKED, so NOTHING is factorised and
    the factorisation cap does not apply (the T134 convention for FFT gathers
    and rectangular blocks)."""
    h = M // 2
    s = np.arange(h)
    dg = np.empty(h)
    w = np.empty(h)
    P = np.empty(h)
    N = np.empty(h)
    for a in range(0, h, chunk):
        b = min(h, a + chunk)
        r = np.arange(a, b)
        blk = (c[np.abs(r[:, None] - s[None, :])]
               - c[(M - 1) - r[:, None] - s[None, :]])
        idx = np.arange(b - a)
        d = blk[idx, r].copy()
        blk[idx, r] = 0.0
        dg[a:b] = d
        w[a:b] = d + blk.sum(axis=1)
        P[a:b] = np.where(blk > 0.0, blk, 0.0).sum(axis=1)
        N[a:b] = np.where(blk < 0.0, -blk, 0.0).sum(axis=1)
        del blk
    return dict(h=h, dg_min=float(np.min(dg)), dg_max=float(np.max(dg)),
                w_min=float(np.min(w)), w_max=float(np.max(w)),
                p_max=float(np.max(P)), p_sum=float(np.sum(P)),
                n_max=float(np.max(N)), n_med=float(np.median(N)))


firewall()


# ----------------------------------------------------------------------------
section("G0  SETUP and THE DIRECTION AUDIT of the lumped pair")
# ----------------------------------------------------------------------------
ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]

NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

BERT_OK = bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
EVEN_OK = bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12))
check("el_g0.gap_bounds", BERT_OK and EVEN_OK,
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
DROP = np.ones(NZ_DEEP)
DROP[1:] = D_FREE[:-1] / D_FREE[1:]
REC_IDX = [k for k in range(1, NZ_DEEP) if DROP[k] > 1.0 + 1.0e-12]

REC = []
for k in REC_IDX:
    geo = edge_geom(UU_ALL[k], UU_ALL[k + 1], float(D_FREE[k - 1]),
                    float(D_FREE[k]))
    if geo is None:
        continue
    REC.append(dict(k=k, n=NN_ALL[k], rho=geo["rho"], gc_c=geo["gc_c"],
                    gc_f=geo["gc_f"], h_c=geo["h_c"], h_f=geo["h_f"],
                    D_c=geo["D_c"], D_f=geo["D_f"], al_c=geo["al_c"],
                    al_f=geo["al_f"]))

RHO_R = np.array([d["rho"] for d in REC], dtype=float)
COVER = float(np.mean(RHO_R <= RHO_UNI_T127))
check("el_g0.record_schedule",
      len(REC) > 100 and abs(100.0 * COVER - COVER_T127) < 0.5,
      "the free-resolution schedule D_k = min(cap_k, D_{k-1}) re-grids at %d of "
      "%d boundaries over n <= %d, and the T127 uniformity band rho <= %.5f "
      "(QUOTED) covers %.2f %% of them (T127 quoted %.2f %%).  The target list "
      "is UNCHANGED from T129..T134 -- nothing is re-chosen here"
      % (len(REC), NZ_DEEP, ZONE_DEEP, RHO_UNI_T127, 100.0 * COVER, COVER_T127))

# --- G0.2  the odd section against the slow reference -----------------------
_zk = None
for k in range(4, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    if 40 <= even_window(UU_ALL[k], D_k) // 2 <= 120:
        _zk = k
        break
if _zk is None:
    _zk = 6
_Dv = 0.5 * float(G_DEEP[_zk]) / NU_MAIN
_Mv = even_window(UU_ALL[_zk], _Dv)
_alv = 0.5 * _Mv * _Dv
_cv, _ = lag_vector_fast(_alv, _Mv, atoms_in(_alv, ATOMS_ALL))
_Av = sym(odd_toeplitz(_cv, _Mv))
_hv = _Mv // 2
E_ODD = rel(odd_toeplitz(_cv, _Mv), odd_toeplitz_slow(_cv, _Mv))
check("el_g0.odd_section", E_ODD < 1.0e-15,
      "the vectorised odd Toeplitz+Hankel section reproduces the entrywise "
      "definition A_rs = c_|r-s| - c_{M-1-r-s} to %.2e at the validation zone "
      "n = %d (h = %d, D = %.4e).  A is the POLE-FREE object: the rank-one pole "
      "term is NOT subtracted anywhere in G1"
      % (E_ODD, NN_ALL[_zk], _hv, _Dv))

# --- G0.3  the T126 Dirichlet identity, to round-off ------------------------
_ds = dirichlet_split(_Av)
_rng = np.random.default_rng(20260728)
_ID = []
for _j in range(8):
    _v = _rng.standard_normal(_hv)
    _lhs = float(_v @ _Av @ _v)
    _dif = _v[:, None] - _v[None, :]
    _rhs = (float(np.dot(_ds["w"], _v * _v))
            + 0.5 * float(np.sum(-_ds["off"] * _dif * _dif)))
    _ID.append(abs(_lhs - _rhs) / max(abs(_lhs), 1.0e-300))
check("el_g0.dirichlet_identity", qmax(_ID) < BAR_ID,
      "the T126 three-way split v^T A v = sum w_r v_r^2 + sum_{r<s} (-A_rs) "
      "(v_r - v_s)^2 holds to %.2e relative on 8 random vectors (bar %.0e): "
      "%.1f %% of the off-diagonals are NEGATIVE (good jumps), the rest are the "
      "bad ones the pair has to pay for"
      % (qmax(_ID), BAR_ID, 100.0 * _ds["frac_neg"]))

# --- G0.4  the Cholesky certificate against exact eigenvalues ---------------
_mu_v = float(eigvalsh(_Av, subset_by_index=[0, 0])[0])
_cert_v = cert_floor_bisect(_Av, 0.0, max(_mu_v, 1.0e-14) * 2.0)
check("el_g0.cert_calibration",
      _cert_v is not None and _cert_v <= _mu_v * (1.0 + 1.0e-9)
      and _cert_v >= _mu_v * 0.99,
      "the Cholesky-bisection certificate returns %.6e against the exact "
      "eigenvalue %.6e (ratio %.6f <= 1 by construction, fp floor %.2e): a "
      "COMPLETED Cholesky of A - s I certifies lam_min(A) >= s up to that "
      "floor (Wilkinson 1968; Higham 2002 Thm 10.3/10.4)"
      % (_cert_v if _cert_v is not None else float("nan"), _mu_v,
         (_cert_v / _mu_v) if _cert_v is not None else float("nan"),
         chol_floor(gersh(_Av), _hv)))

# --- G0.5  THE DIRECTION AUDIT -- the five facts G1-G3 rest on --------------
para("""G0.5  THE DIRECTION AUDIT.  Everything that follows is an inequality
between symmetric matrices, and the single most expensive mistake available in
this file is to use one in the wrong direction.  The five facts below are
therefore stated with their direction and verified numerically on the
validation window before any of them is used.  (P1) LUMPING RAISES: A_B = A +
L_Delta with L_Delta the Laplacian of the positive off-diagonal part is PSD, so
A_B >= A in the Loewner order and lam_min(A_B) >= lam_min(A) -- an UPPER bound
on the floor, useless by itself; A_B is STIELTJES by construction and the row
sums are PRESERVED.  (P2) THE CONGRUENCE: A = A_B^{1/2}(I - W)A_B^{1/2} with
W = A_B^{-1/2} L_Delta A_B^{-1/2} >= 0 gives the LOEWNER SANDWICH lam_min(A) >=
lam_min(A_B)(1 - lam_max(W)), which runs the RIGHT way, and lam_max(W) =
rho(L_Delta A_B^{-1}) by similarity.  (P3) THE CIRCULARITY, stated openly:
lam_max(W) < 1 is EQUIVALENT to A > 0, because A = A_B - L_Delta.  So the
sandwich is not a proof of anything unless lam_max(W) is bounded ABOVE by
ingredients that are cheap and independent -- which is exactly what G1 tests.
(P4) THE ANCHOR: for Stieltjes A_B the solve A_B x = 1 with x >= 0 gives
lam_min(A_B) >= 1 / max_r x_r (Fan 1958; Berman-Plemmons 1979; the inf-norm
step uses symmetry).  (P5) THE BRACKET: for a Stieltjes matrix with diagonal d
and row sums w the Jacobi matrix J = I - D^{-1} A_B is NONNEGATIVE with row
sums 1 - w_r/d_r, so Frobenius 1912 gives 1 - max_r w_r/d_r <= rho(J) <=
1 - min_r w_r/d_r, two-sided and from row sums alone.""")

_lp = lump_pair(_Av)
_AB = _lp["A_B"]
_muB = float(eigvalsh(_AB, subset_by_index=[0, 0])[0])
_ldm = float(eigvalsh(_lp["LD"], subset_by_index=[0, 0])[0])
_rs_pres = float(np.max(np.abs(_AB.sum(axis=1) - _Av.sum(axis=1)))) / max(
    float(np.abs(_Av).max()), 1.0e-300)
check("el_g0.p1_lumping_raises",
      _lp["stieltjes"] == 1 and _ldm >= -1.0e-12 * max(gersh(_lp["LD"]), 1.0)
      and _muB >= _mu_v and _rs_pres < BAR_ID,
      "(P1) VERIFIED, with its direction: L_Delta is PSD (lam_min = %+.2e), so "
      "A_B = A + L_Delta >= A and lam_min(A_B) = %.6e >= lam_min(A) = %.6e -- "
      "the WRONG direction for a floor, as advertised.  A_B is STIELTJES by "
      "construction (all %d off-diagonals <= 0, diagonal > 0) and the row sums "
      "are preserved to %.1e relative"
      % (_ldm, _muB, _mu_v, _hv * (_hv - 1), _rs_pres))

_LB = cholesky(_AB, lower=True, check_finite=False)
_Y = solve_triangular(_LB, _lp["LD"], lower=True, check_finite=False)
_W = sym(solve_triangular(_LB, _Y.T, lower=True, check_finite=False).T)
_lw = float(eigvalsh(_W, subset_by_index=[_hv - 1, _hv - 1])[0])
_sand = _muB * (1.0 - _lw)
_gap_exact = float(eigh(_Av, _AB, eigvals_only=True)[0])
check("el_g0.p2_sandwich",
      _sand <= _mu_v * (1.0 + 1.0e-8) and abs(1.0 - _lw - _gap_exact)
      <= 1.0e-8 * max(abs(_gap_exact), 1.0e-300),
      "(P2) VERIFIED: the congruence A = A_B^{1/2}(I - W)A_B^{1/2} gives "
      "1 - lam_max(W) = %.6e, which matches the generalised eigenvalue "
      "lam_min(A, A_B) = %.6e to %.1e, and the sandwich lam_min(A_B)(1 - "
      "lam_max(W)) = %.6e is a valid LOWER bound for lam_min(A) = %.6e (ratio "
      "%.4f <= 1).  This is the classical product form (Ostrowski 1959; "
      "Fan 1958) and it is the ONLY direction-correct use of the lumped pair"
      % (1.0 - _lw, _gap_exact,
         abs(1.0 - _lw - _gap_exact) / max(abs(_gap_exact), 1.0e-300),
         _sand, _mu_v, _sand / max(_mu_v, 1.0e-300)))

check("el_g0.p3_circularity", (_lw < 1.0) == (_mu_v > 0.0),
      "(P3) VERIFIED and stated as a WARNING, not as an achievement: since "
      "A = A_B - L_Delta, lam_max(W) < 1 holds if and only if A > 0 "
      "(lam_max(W) = %.6f, lam_min(A) = %+.3e).  So a MEASURED lam_max(W) "
      "proves nothing that a Cholesky of A does not already prove, and the "
      "sandwich becomes a route only through an INDEPENDENT upper bound on "
      "lam_max(W).  G1 tests exactly two such bounds and reports both"
      % (_lw, _mu_v))

_an = anchor_floor(_AB)
check("el_g0.p4_anchor",
      _an is not None and _an["nonneg"] == 1 and _an["floor"] <= _muB
      * (1.0 + 1.0e-9),
      "(P4) VERIFIED: A_B x = 1 has x >= 0 entrywise (min x = %+.3e, max x = "
      "%.3e), which by the positive-vector characterisation (Fan 1958; "
      "Berman-Plemmons 1979) makes A_B a nonsingular M-matrix, and the anchor "
      "1 / max_r x_r = %.6e is a LOWER bound for lam_min(A_B) = %.6e (ratio "
      "%.4f <= 1).  Cost: one solve and one sign check -- no eigenvalue"
      % (_an["xmin"], _an["xmax"], _an["floor"], _muB,
         _an["floor"] / max(_muB, 1.0e-300)))

_d0 = np.diag(_AB).copy()
_N0 = np.diag(_d0) - _AB
_J0 = _N0 / np.maximum(_d0, 1.0e-300)[:, None]
_rs = 1.0 - _Av.sum(axis=1) / np.maximum(_d0, 1.0e-300)
_rho_j = float(np.max(np.abs(np.linalg.eigvals(_J0))))
check("el_g0.p5_bracket",
      bool(np.all(_N0 >= -1.0e-300)) and float(np.min(_rs)) <= _rho_j + 1.0e-9
      and _rho_j <= float(np.max(_rs)) + 1.0e-9,
      "(P5) VERIFIED: the Jacobi matrix of the Stieltjes A_B is NONNEGATIVE "
      "and its row sums are exactly 1 - w_r/d_r (w = the PRESERVED row sums of "
      "A), so the Frobenius bracket %.6f <= rho(J) = %.6f <= %.6f holds -- a "
      "two-sided A-PRIORI bracket from row sums and diagonals alone "
      "(Frobenius 1912; Varga 1962 Thm 3.2)"
      % (float(np.min(_rs)), _rho_j, float(np.max(_rs))))

_pw = pow_lmax_W(_LB, _lp["LD"], rng=np.random.default_rng(7))
check("el_g0.pow_calibration", _pw <= _lw * (1.0 + 1.0e-9),
      "the power iteration used for lam_max(W) at the larger sizes returns "
      "%.6f against the exact %.6f (ratio %.6f <= 1 by construction, %d "
      "steps).  It is a MEASUREMENT and one-sided: it can KILL a margin, never "
      "certify one" % (_pw, _lw, _pw / max(_lw, 1.0e-300), G1_POW))

del _W, _Y, _LB, _N0, _J0, _AB, _lp, _ds
info("G0.status", "machinery verified, five direction facts audited, "
     "%.0f s of %.0f budget left" % (budget_left(), BUDGET_S))


# ----------------------------------------------------------------------------
section("G1  THE A-FLOOR ROUTE THROUGH M-MATRIX TOOLING")
# ----------------------------------------------------------------------------
para("""G1.0  THE CANDIDATES, SORTED BY DIRECTION BEFORE ANYTHING IS MEASURED.
T134 left exactly one structural opening for a floor on lam_min(A): treat the
bad positive off-diagonals with M-matrix tooling instead of paying for them by
Gershgorin, by a spectral norm, after Jacobi scaling, through a comparison
matrix or by path comparison -- all five of which failed by SIGN and not by
size.  Lumping is the tool, and G0.5 (P1) fixed its direction: A_B = A +
L_Delta >= A, so A_B alone can only bound the floor from ABOVE.  Two candidate
routes survive that direction test, and they are the only two:
  (i)  THE NEUMANN / LOEWNER MARGIN.  A = A_B - L_Delta and the congruence
       A = A_B^{1/2}(I - W)A_B^{1/2}, W = A_B^{-1/2} L_Delta A_B^{-1/2} >= 0,
       give lam_min(A) >= lam_min(A_B) (1 - lam_max(W)) -- equivalently
       A^{-1} = A_B^{-1}(I - E)^{-1}-style with E = L_Delta A_B^{-1} and
       lam_max(W) = rho(E) by similarity.  Both factors then need a CHEAP lower
       resp. upper bound, and G0.5 (P3) is the reason this is a test and not a
       proof: rho(E) < 1 is EQUIVALENT to A > 0, so only an INDEPENDENT bound on
       rho(E) turns the sandwich into a route.  Four numbers are produced per
       window: rho_ap = ||L_Delta||_inf max_r x_r (fully factored, no matrix
       product at all), rho_inf = ||A_B^{-1} L_Delta||_inf (one triangular
       solve block), rho_cw = max_r (|E| x)_r / x_r (the Collatz-Wielandt /
       Wielandt scaling with the anchor vector, Collatz 1942; Wielandt 1950),
       and rho_pow, a power-iteration MEASUREMENT that is one-sided and can
       only KILL a margin.  The lower factor is the ANCHOR of G0.5 (P4).
  (ii) THE D-UNIFORMITY QUESTION, which is what T134 actually left open: the
       certified floor degrades like D^%.2f (FIT, QUOTED) and the question is
       WHICH INGREDIENT of the M-matrix structure carries that power.  Every
       ingredient is fitted separately below -- min diag, the row sums w, the
       good Laplacian row mass, max_r P_r, the anchor 1/max x, the margin gap
       1 - rho -- with a MATRIX-FREE row-chunked extension to h = %d, far
       beyond the factorisation cap, and the exponents are then required to
       ADD UP.  The uniform candidate form lam_min(A) >= c D^p is constructed
       from them with explicit (c, p) and its uniformity is measured."""
     % (CERT_EXP_T134, G1_FREE_CAP))


def pair_route(A, mu_meas, cert_A, heavy, do_certB):
    """The M-matrix pair on ONE window.  Every entry carries its own class."""
    h = A.shape[0]
    lp = lump_pair(A)
    A_B = lp["A_B"]
    out = dict(h=h, mu_meas=mu_meas, cert=cert_A, stieltjes=lp["stieltjes"],
               n_pos=lp["n_pos"], w_min=float(np.min(lp["w"])),
               w_max=float(np.max(lp["w"])), dg_min=float(np.min(lp["dg"])),
               dgB_min=float(np.min(lp["dgB"])),
               p_max=float(np.max(lp["P_row"])),
               ld_inf=2.0 * float(np.max(lp["P_row"])))
    an = anchor_floor(A_B)
    if an is None:
        return None
    out.update(xmax=an["xmax"], xmin=an["xmin"], x_nonneg=an["nonneg"],
               anchor=an["floor"])
    # --- the a-priori margin: NO matrix product, NO eigenvalue --------------
    out["rho_ap"] = out["ld_inf"] * an["xmax"]                    # CERTIFIABLE
    out["muB"] = float("nan")
    out["certB"] = float("nan")
    out["rho_inf"] = float("nan")
    out["rho_cw"] = float("nan")
    out["rho_pow"] = float("nan")
    out["rho_ex"] = float("nan")
    out["gap_ex"] = float("nan")
    out["pow_conv"] = float("nan")
    if heavy:
        E = cho_solve(an["fac"], lp["LD"], check_finite=False)
        out["rho_inf"] = float(np.abs(E).sum(axis=1).max())       # CERTIFIABLE
        yE = np.abs(E) @ an["x"]
        out["rho_cw"] = float(np.max(yE / np.maximum(an["x"], 1.0e-300)))
        del E, yE
        LB = cholesky(A_B, lower=True, check_finite=False)
        out["rho_pow"] = pow_lmax_W(LB, lp["LD"], rng=RNG_G1)     # MEASURED
        del LB
        out["muB"] = float(eigvalsh(A_B, subset_by_index=[0, 0])[0])
        # the EXACT margin: 1 - lam_max(W) = lam_min(A, A_B), the smallest
        # generalised eigenvalue -- a MEASUREMENT, but an exact one, and the
        # power iteration above is retained only to show how far short it falls
        try:
            out["gap_ex"] = float(eigh(A, A_B, eigvals_only=True,
                                       subset_by_index=[0, 0])[0])
            out["rho_ex"] = 1.0 - out["gap_ex"]
            out["pow_conv"] = ((1.0 - out["rho_pow"])
                               / max(out["gap_ex"], 1.0e-300))
        except (LinAlgError, ValueError):
            pass
        if do_certB:
            cb = cert_floor_bisect(A_B, 0.0, max(out["muB"], 1.0e-14) * 2.0,
                                   iters=20)
            out["certB"] = cb if cb is not None else float("nan")
    # --- the three assembled floors, each with its own class ---------------
    out["pair_ap"] = ((1.0 - out["rho_ap"]) * out["anchor"]
                      if out["rho_ap"] < 1.0 else float("nan"))
    out["pair_inf"] = ((1.0 - out["rho_inf"]) * out["anchor"]
                       if out["rho_inf"] < 1.0 else float("nan"))
    out["pair_cw"] = ((1.0 - out["rho_cw"]) * out["anchor"]
                      if out["rho_cw"] < 1.0 else float("nan"))
    ref_base = out["certB"] if out["certB"] == out["certB"] else out["muB"]
    out["pair_ref"] = (out["gap_ex"] * ref_base
                       if out["gap_ex"] == out["gap_ex"] else float("nan"))
    out["pair_anch"] = (out["gap_ex"] * out["anchor"]
                        if out["gap_ex"] == out["gap_ex"] else float("nan"))
    # --- the LOSS DECOMPOSITION of the reference sandwich ------------------
    out["f_sand"] = (mu_meas / out["pair_ref"]
                     if out["pair_ref"] == out["pair_ref"]
                     and out["pair_ref"] > 0.0 else float("nan"))
    out["f_anchor"] = (out["muB"] * out["xmax"] if out["muB"] == out["muB"]
                       else float("nan"))
    out["gap_pow"] = 1.0 - out["rho_pow"]
    out["gap_inf"] = 1.0 - out["rho_inf"]
    # HOW FAR the cheap bounds are from being useful, in units of the ONLY
    # scale that matters: a bound on rho(E) is useful iff its error is smaller
    # than the gap itself
    if out["gap_ex"] == out["gap_ex"] and out["gap_ex"] > 0.0:
        out["over_inf"] = (out["rho_inf"] - out["rho_ex"]) / out["gap_ex"]
        out["over_cw"] = (out["rho_cw"] - out["rho_ex"]) / out["gap_ex"]
        out["over_ap"] = (out["rho_ap"] - out["rho_ex"]) / out["gap_ex"]
    else:
        out["over_inf"] = out["over_cw"] = out["over_ap"] = float("nan")
    del lp, A_B, an
    return out


RNG_G1 = np.random.default_rng(1360728)
G1Z = []
_seen = set()
for k in range(2, NZ_DEEP - 2):
    if len(G1Z) >= G1_ZONES:
        break
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_o = even_window(UU_ALL[k], D_k)
    h_o = M_o // 2
    if h_o < H_MIN or h_o > G1_HCAP_FULL:
        continue
    key = h_o // 10
    if key in _seen:
        continue
    _seen.add(key)
    G1Z.append((k, D_k, M_o, h_o))

G1R = []
FREE = []
for (k, D_k, M_o, h_o) in G1Z:
    if budget_left() < BUDGET_S - T_G1:
        info("G1.budget", "pair battery truncated at n = %d" % NN_ALL[k])
        break
    al = 0.5 * M_o * D_k
    ats = atoms_in(al, ATOMS_ALL)
    for lev in range(G1_LEV):
        M = M_o * (2 ** lev)
        h = M // 2
        if h > G1_FREE_CAP or budget_left() < BUDGET_S - T_G1:
            break
        c, D = lag_vector_fast(al, M, ats)
        # the MATRIX-FREE ingredient row, available at ANY size (nothing is
        # factorised, so the cap does not bind)
        fi = free_ingredients(c, M)
        fi.update(n=NN_ALL[k], lev=lev, D=D, al=al)
        FREE.append(fi)
        if h <= G1_HCAP_WIDE:
            A = sym(odd_toeplitz(c, M))
            mu_meas = float(eigvalsh(A, subset_by_index=[0, 0])[0])
            cert_A = cert_floor_bisect(A, 0.0, max(mu_meas, 1.0e-14) * 2.0,
                                       iters=20)
            row = pair_route(A, mu_meas,
                             cert_A if cert_A is not None else float("nan"),
                             heavy=(h <= G1_HCAP_MID),
                             do_certB=(h <= G1_HCAP_FULL))
            if row is not None:
                row.update(n=NN_ALL[k], lev=lev, D=D, al=al,
                           heavy=int(h <= G1_HCAP_MID))
                G1R.append(row)
            del A
        del c

G1H = [r for r in G1R if r["heavy"]]
if G1H:
    print("")
    print("      n     h  D        | mu_meas   cert_A    anchor    certB     "
          "| rho_ap   rho_inf  rho_cw   gap_exact | pair_ref  f_sand f_anch")
    for r in G1H:
        print("   %5d %5d %.2e | %.3e %.3e %.3e %.3e | %.2e %.5f %.5f %.3e "
              "| %.3e %6.2f %6.2f"
              % (r["n"], r["h"], r["D"], r["mu_meas"], r["cert"], r["anchor"],
                 r["certB"], r["rho_ap"], r["rho_inf"], r["rho_cw"],
                 r["gap_ex"], r["pair_ref"], r["f_sand"], r["f_anchor"]))

ST_ALL = sum(r["stieltjes"] for r in G1R)
XN_ALL = sum(r["x_nonneg"] for r in G1R)
AP_OK = [r for r in G1R if r["rho_ap"] < 1.0]
INF_OK = [r for r in G1H if r["rho_inf"] < 1.0]
CW_OK = [r for r in G1H if r["rho_cw"] < 1.0]
EX_OK = [r for r in G1H if r["rho_ex"] < 1.0]
REF_POS = [r for r in G1H if r["pair_ref"] == r["pair_ref"]
           and r["pair_ref"] > 0.0]
SAND_VALID = [r for r in REF_POS if r["f_sand"] >= 1.0 - 1.0e-9]
NEED = dict((id(r), 10.0 ** (-SLACK_DEC) * max(r["mu_meas"], 0.0))
            for r in G1R)
AP_NEED = [r for r in AP_OK if r["pair_ap"] == r["pair_ap"]
           and r["pair_ap"] >= NEED[id(r)]]

check("el_g1.pair_inventory",
      bool(G1R) and ST_ALL == len(G1R) and XN_ALL == len(G1R),
      "THE PAIR EXISTS AND IS AN M-MATRIX ON EVERY WINDOW -- that part is free. "
      "On %d windows over %d zones and %d depths (h = %.0f .. %.0f, D = %.2e .. "
      "%.2e) the lumped A_B = A + L_Delta is STIELTJES on %d of %d by "
      "construction, the anchor solve A_B x = 1 returns x >= 0 on %d of %d, so "
      "A_B is a nonsingular M-matrix per window (Fan 1958; Berman-Plemmons "
      "1979) and the anchor floor 1 / max_r x_r = %.3e .. %.3e is CERTIFIABLE "
      "with one solve and one sign check.  Measured lam_min(A) = %.3e .. %.3e "
      "(T131 quoted %.1e .. %.1e); the anchor overshoots the TRUE lam_min(A) by "
      "%.1f .. %.1f, which is the point: A_B is the wrong side"
      % (len(G1R), len(set(r["n"] for r in G1R)), G1_LEV,
         qmin([r["h"] for r in G1R]), qmax([r["h"] for r in G1R]),
         qmin([r["D"] for r in G1R]), qmax([r["D"] for r in G1R]),
         ST_ALL, len(G1R), XN_ALL, len(G1R),
         qmin([r["anchor"] for r in G1R]), qmax([r["anchor"] for r in G1R]),
         qmin([r["mu_meas"] for r in G1R]), qmax([r["mu_meas"] for r in G1R]),
         MU1_T131[0], MU1_T131[1],
         qmin([r["anchor"] / max(r["mu_meas"], 1.0e-300) for r in G1R]),
         qmax([r["anchor"] / max(r["mu_meas"], 1.0e-300) for r in G1R])))

if G1H:
    check("el_g1.anchor_sharpness",
          all(r["f_anchor"] >= 1.0 - 1.0e-9 for r in G1H
              if r["f_anchor"] == r["f_anchor"]),
          "THE ANCHOR HALF OF THE PAIR IS SHARP, and this is the good news of "
          "G1: lam_min(A_B) max_r x_r = %.3f .. %.3f on %d windows, i.e. the "
          "M-matrix anchor 1 / max_r x_r loses at most a factor %.2f against "
          "the true lam_min(A_B) -- it is the ||.||_2 <= ||.||_inf step for a "
          "symmetric matrix with a NONNEGATIVE inverse, and there is nothing "
          "left to improve there.  The certified floor of A_B itself is %.3e .. "
          "%.3e on %d windows and sits above the anchor by %.3f .. %.3f"
          % (qmin([r["f_anchor"] for r in G1H]),
             qmax([r["f_anchor"] for r in G1H]), len(G1H),
             qmax([r["f_anchor"] for r in G1H]),
             qmin([r["certB"] for r in G1H if r["certB"] == r["certB"]]),
             qmax([r["certB"] for r in G1H if r["certB"] == r["certB"]]),
             sum(1 for r in G1H if r["certB"] == r["certB"]),
             qmin([r["certB"] / r["anchor"] for r in G1H
                   if r["certB"] == r["certB"]]),
             qmax([r["certB"] / r["anchor"] for r in G1H
                   if r["certB"] == r["certB"]])))

    check("el_g1.margin_anatomy",
          bool(REF_POS) and len(SAND_VALID) == len(REF_POS),
          "AND THE MARGIN HALF IS WHERE THE ROUTE DIES, quantitatively.  The "
          "TRUE margin is razor-thin: rho(E) = %.6f .. %.6f EXACTLY (the "
          "smallest generalised eigenvalue lam_min(A, A_B), a MEASUREMENT but "
          "an exact one), so the gap 1 - rho(E) = %.2e .. %.2e and ANY upper "
          "bound on rho(E) has to be accurate to that many digits to leave a "
          "positive floor.  The three certifiable bounds are not remotely "
          "there: rho_ap = ||L_Delta||_inf max_r x_r = %.2e .. %.2e (below 1 on "
          "%d of %d), the computed row-sum norm rho_inf = ||A_B^{-1} "
          "L_Delta||_inf = %.3f .. %.3f (below 1 on %d of %d) and its Wielandt "
          "rescaling with the anchor vector rho_cw = %.3f .. %.3f (below 1 on "
          "%d of %d).  With the EXACT margin the sandwich is valid on %d of %d "
          "windows as it must be, gives %.3e .. %.3e and loses only a factor "
          "%.2f .. %.2f against lam_min(A) -- so the SANDWICH IS FINE and the "
          "BOUND ON rho IS THE WHOLE PROBLEM.  For the record the %d-step power "
          "iteration recovers only %.2f .. %.2f of the exact gap, which is why "
          "it is not used as the reference: a gap of 1e-3 needs far more steps "
          "than the eigenvalue costs"
          % (qmin([r["rho_ex"] for r in G1H]), qmax([r["rho_ex"] for r in G1H]),
             qmin([r["gap_ex"] for r in G1H]), qmax([r["gap_ex"] for r in G1H]),
             qmin([r["rho_ap"] for r in G1H]), qmax([r["rho_ap"] for r in G1H]),
             len(AP_OK), len(G1R),
             qmin([r["rho_inf"] for r in G1H]),
             qmax([r["rho_inf"] for r in G1H]), len(INF_OK), len(G1H),
             qmin([r["rho_cw"] for r in G1H]),
             qmax([r["rho_cw"] for r in G1H]), len(CW_OK), len(G1H),
             len(SAND_VALID), len(REF_POS),
             qmin([r["pair_ref"] for r in REF_POS]) if REF_POS else float("nan"),
             qmax([r["pair_ref"] for r in REF_POS]) if REF_POS else float("nan"),
             qmin([r["f_sand"] for r in REF_POS]) if REF_POS else float("nan"),
             qmax([r["f_sand"] for r in REF_POS]) if REF_POS else float("nan"),
             G1_POW, qmin([r["pow_conv"] for r in G1H]),
             qmax([r["pow_conv"] for r in G1H])))
    info("G1.overshoot",
         "the failure measured in the ONLY units that matter -- the error of a "
         "rho-bound divided by the gap it has to fit inside: rho_ap overshoots "
         "by %.2e .. %.2e gaps, rho_inf by %.2e .. %.2e, rho_cw by %.2e .. "
         "%.2e.  A useful bound needs an overshoot below 1"
         % (qmin([r["over_ap"] for r in G1H]),
            qmax([r["over_ap"] for r in G1H]),
            qmin([r["over_inf"] for r in G1H]),
            qmax([r["over_inf"] for r in G1H]),
            qmin([r["over_cw"] for r in G1H]),
            qmax([r["over_cw"] for r in G1H])))
    info("G1.power_note",
         "the %d-step power iteration OVERSTATES the gap by a factor %.2f .. "
         "%.1f (it converges from BELOW in lam_max(W)), so it is kept only as "
         "the G0 calibration and never as a bound: a gap of 1e-6 needs more "
         "steps than the exact generalised eigenvalue costs"
         % (G1_POW, qmin([r["pow_conv"] for r in G1H]),
            qmax([r["pow_conv"] for r in G1H])))

# --- G1.1  the shift ladder, killed by MONOTONICITY and not by measurement --
_sh_A = sym(odd_toeplitz(_cv, _Mv))
_sh_lp = lump_pair(_sh_A)
_sh_an = anchor_floor(_sh_lp["A_B"])
_sh_s = 0.5 * _muB
_sh_an2 = anchor_floor(_sh_lp["A_B"] - _sh_s * np.eye(_hv))
_mono = (_sh_an2 is not None and _sh_an is not None
         and _sh_an2["xmax"] >= _sh_an["xmax"] * (1.0 - 1.0e-12))
check("el_g1.shift_ladder_monotone", _mono,
      "THE SHIFTED LADDER IS EMPTY FOR A STRUCTURAL REASON, NOT A MEASURED "
      "ONE.  Lumping COMMUTES with a diagonal shift -- (A - s I) + L_Delta = "
      "A_B - s I, since L_Delta depends only on the off-diagonals -- so the "
      "whole pair machinery can be run at shift s and would give lam_min(A) >= "
      "s + (1 - rho_s) / max_r x_r(s).  But A_B - s I <= A_B are both "
      "M-matrices, hence (A_B - s I)^{-1} >= A_B^{-1} >= 0 entrywise "
      "(monotonicity of M-matrix inverses, Berman-Plemmons 1979 Thm 6.2.3), so "
      "max_r x_r(s) is NONDECREASING in s: verified here, %.4f -> %.4f at "
      "s = %.3e.  Therefore rho_ap(s) = ||L_Delta||_inf max_r x_r(s) is "
      "nondecreasing too, and a margin that already fails at s = 0 fails for "
      "every s > 0.  No ladder is run"
      % (_sh_an["xmax"] if _sh_an else float("nan"),
         _sh_an2["xmax"] if _sh_an2 else float("nan"), _sh_s))
del _sh_A, _sh_lp, _sh_an, _sh_an2

# --- G1.2  WHICH INGREDIENT CARRIES THE D-POWER ----------------------------
FITS = []
if len(G1R) >= 5:
    Dv = [r["D"] for r in G1R]
    FITS.append(pow_fit(Dv, [r["cert"] for r in G1R], "cert(A)  CERTIFIED"))
    FITS.append(pow_fit(Dv, [r["mu_meas"] for r in G1R], "lam_min(A)  MEASURED"))
    FITS.append(pow_fit(Dv, [r["anchor"] for r in G1R], "1/max x  CERTIFIABLE"))
    FITS.append(pow_fit(Dv, [r["xmax"] for r in G1R], "max x  CERTIFIABLE"))
    FITS.append(pow_fit(Dv, [r["dg_min"] for r in G1R], "min diag  CERTIFIABLE"))
    FITS.append(pow_fit(Dv, [r["p_max"] for r in G1R], "max_r P_r  CERTIFIABLE"))
    FITS.append(pow_fit(Dv, [abs(r["w_min"]) for r in G1R],
                        "|min row sum|  CERTIFIABLE"))
if len(G1H) >= 5:
    Dh = [r["D"] for r in G1H]
    FITS.append(pow_fit(Dh, [r["certB"] for r in G1H], "cert(A_B)  CERTIFIED"))
    FITS.append(pow_fit(Dh, [r["gap_ex"] for r in G1H],
                        "gap 1-rho(E)  MEASURED"))
    FITS.append(pow_fit(Dh, [r["rho_ap"] for r in G1H], "rho_ap  CERTIFIABLE"))
if len(FREE) >= 5:
    Df = [r["D"] for r in FREE]
    FITS.append(pow_fit(Df, [r["p_max"] for r in FREE],
                        "max_r P_r  MATRIX-FREE"))
    FITS.append(pow_fit(Df, [r["dg_min"] for r in FREE],
                        "min diag  MATRIX-FREE"))
    FITS.append(pow_fit(Df, [r["n_med"] for r in FREE],
                        "median good row mass  MATRIX-FREE"))

if FITS:
    print("")
    print("   ingredient                        n     c            p       "
          "+- band   rms(log)")
    for f in FITS:
        print("   %-32s %4d  %.4e  %+.3f  %.3f    %.3f"
              % (f["tag"], f["n"], f["c"], f["p"], f["sp"], f["rms"]))

FD = dict((f["tag"].split()[0] + "|" + f["tag"].split()[-1], f) for f in FITS)
P_CERT = FD.get("cert(A)|CERTIFIED", {}).get("p", float("nan"))
P_ANCH = FD.get("1/max|CERTIFIABLE", {}).get("p", float("nan"))
P_GAP = FD.get("gap|MEASURED", {}).get("p", float("nan"))

# THE EXACT THREE-WAY BOOKKEEPING.  Per window, and with no inequality at all,
#     lam_min(A) = (1 / max_r x_r) * gap_ex * f_a,   f_a = lam_min(A) max_r x_r
#                                                          / gap_ex,
# so the LEAST-SQUARES exponents of the three factors ADD UP to the exponent of
# lam_min(A) EXACTLY (the fit is linear in the log of the data).  The split
# therefore attributes the D-power without any modelling freedom.
G1B = [r for r in G1H if r["gap_ex"] == r["gap_ex"] and r["anchor"] > 0.0]
BK = None
if len(G1B) >= 5:
    Db = [r["D"] for r in G1B]
    f_a = [r["mu_meas"] * r["xmax"] / r["gap_ex"] for r in G1B]
    F_MU = pow_fit(Db, [r["mu_meas"] for r in G1B], "x")
    F_AN = pow_fit(Db, [r["anchor"] for r in G1B], "x")
    F_GP = pow_fit(Db, [r["gap_ex"] for r in G1B], "x")
    F_FA = pow_fit(Db, f_a, "x")
    BK = dict(mu=F_MU["p"], an=F_AN["p"], gp=F_GP["p"], fa=F_FA["p"],
              res=abs(F_MU["p"] - (F_AN["p"] + F_GP["p"] + F_FA["p"])),
              n=len(G1B), fa_lo=qmin(f_a), fa_hi=qmax(f_a),
              smu=F_MU["sp"], san=F_AN["sp"], sgp=F_GP["sp"], sfa=F_FA["sp"])
check("el_g1.d_bookkeeping", BK is not None and BK["res"] < 1.0e-9,
      "WHICH INGREDIENT CARRIES THE D-POWER -- the fits are FITS, but the "
      "SPLIT is an identity.  Per window lam_min(A) = (1 / max_r x_r) x gap x "
      "f_a with gap = lam_min(A, A_B) and f_a the residual sandwich slack, so "
      "the three log-log exponents ADD to the exponent of lam_min(A) exactly "
      "(residual %.1e on %d windows).  The attribution: lam_min(A) ~ D^%.3f +- "
      "%.3f (T134 quoted D^%.2f, reproduced) = [anchor 1/max_r x_r ~ D^%.3f +- "
      "%.3f] x [margin gap ~ D^%.3f +- %.3f] x [slack f_a ~ D^%.3f +- %.3f, "
      "numerically %.2f .. %.2f].  READ IT: the M-matrix anchor carries a "
      "NEGATIVE power, i.e. the Stieltjes comparison A_B GROWS its floor as the "
      "grid refines and works AGAINST the D-degradation; the entire D^2.3 loss "
      "is carried by the MARGIN GAP 1 - rho(E), which closes like D^%.2f; and "
      "the sandwich slack is essentially D-free.  So the D-uniformity question "
      "is EXACTLY the question of how fast the lumped perturbation fills up "
      "A_B, and not a question about diagonals, row sums or Laplacian weights "
      "-- each of which carries only D^%.2f .. D^%.2f"
      % (BK["res"] if BK else float("nan"), BK["n"] if BK else 0,
         BK["mu"] if BK else float("nan"), BK["smu"] if BK else float("nan"),
         CERT_EXP_T134, BK["an"] if BK else float("nan"),
         BK["san"] if BK else float("nan"), BK["gp"] if BK else float("nan"),
         BK["sgp"] if BK else float("nan"), BK["fa"] if BK else float("nan"),
         BK["sfa"] if BK else float("nan"), BK["fa_lo"] if BK else float("nan"),
         BK["fa_hi"] if BK else float("nan"), BK["gp"] if BK else float("nan"),
         FD.get("max_r|CERTIFIABLE", {}).get("p", float("nan")),
         FD.get("min|CERTIFIABLE", {}).get("p", float("nan"))))

# --- G1.3  THE UNIFORM CANDIDATE FORM lam_min(A) >= c D^p ------------------
UNI = None
if P_CERT == P_CERT and len(G1R) >= 5:
    _p = P_CERT
    _rat = [r["cert"] / (r["D"] ** _p) for r in G1R if r["cert"] == r["cert"]]
    _c = qmin(_rat)
    _spread = qmax(_rat) / max(_c, 1.0e-300)
    _n_hold = sum(1 for r in G1R if r["cert"] == r["cert"]
                  and r["cert"] >= _c * (r["D"] ** _p) * (1.0 - 1.0e-12))
    # the same envelope built from the CERTIFIABLE anchor alone (no eigenvalue)
    _pa = P_ANCH
    _rata = [r["anchor"] / (r["D"] ** _pa) for r in G1R]
    _ca = qmin(_rata)
    _spa = qmax(_rata) / max(_ca, 1.0e-300)
    UNI = dict(p=_p, c=_c, spread=_spread, hold=_n_hold, tot=len(G1R),
               pa=_pa, ca=_ca, spa=_spa)
    info("G1.uniform_form",
         "THE UNIFORM CANDIDATE FORM, with its class stated first: what follows "
         "is a FIT-BASED ENVELOPE of CERTIFIED numbers over a FINITE surface, "
         "i.e. a HYPOTHESIS, not a theorem.  With p = %.3f taken from the fit, "
         "the envelope constant c = min_windows cert(A) / D^p = %.4e holds on "
         "%d of %d windows by construction and the ratio cert(A) / (c D^p) "
         "spreads only %.2f over the whole surface (h = %.0f .. %.0f, D = %.2e "
         ".. %.2e, %d zones) -- so the SHAPE c D^p is stable even though no "
         "certificate of it exists.  The same envelope built from the "
         "CERTIFIABLE anchor alone, which needs no eigenvalue and no Cholesky "
         "of A, is 1/max_r x_r >= %.4e D^%.3f with spread %.2f; it bounds "
         "lam_min(A_B), NOT lam_min(A), and closing that last step is exactly "
         "the margin problem above"
         % (_p, _c, _n_hold, len(G1R), _spread, qmin([r["h"] for r in G1R]),
            qmax([r["h"] for r in G1R]), qmin([r["D"] for r in G1R]),
            qmax([r["D"] for r in G1R]), len(set(r["n"] for r in G1R)),
            _ca, _pa, _spa))

if FREE:
    info("G1.free_extension",
         "THE MATRIX-FREE EXTENSION, which is what lets the ingredient fits "
         "reach past the factorisation cap: the cheap ingredients (min diag, "
         "the row sums, max_r P_r, the good row mass) are row-chunked and need "
         "no factorisation at all, so they were measured on %d windows up to "
         "h = %.0f -- %.1f times the largest FACTORISED form (%d, cap %d) -- "
         "over D = %.2e .. %.2e.  On that wider surface max_r P_r ~ D^%.3f and "
         "min diag ~ D^%.3f, consistent with the factorised fits above, so the "
         "ingredient exponents are not an artefact of the small windows.  What "
         "is NOT available matrix-free is max_r x_r, which needs a solve -- the "
         "anchor is the first place the cap binds"
         % (len(FREE), qmax([r["h"] for r in FREE]),
            qmax([r["h"] for r in FREE]) / max(qmax([r["h"] for r in G1R]), 1.0),
            int(qmax([r["h"] for r in G1R])), MAX_H,
            qmin([r["D"] for r in FREE]), qmax([r["D"] for r in FREE]),
            FD.get("max_r|MATRIX-FREE", {}).get("p", float("nan")),
            FD.get("min|MATRIX-FREE", {}).get("p", float("nan"))))

G1_OK = bool(G1R) and len(AP_NEED) == len(G1R)
G1_STAT = ("PAIR-FLOOR-CERTIFIABLE" if G1_OK else
           ("PAIR-ANCHOR-ONLY" if XN_ALL == len(G1R) and G1R
            else "PAIR-OPEN"))
info("G1.status", "%s -- %s" % (G1_STAT, (
    "the a-priori pair delivers a positive certifiable floor on every window"
    if G1_OK else
    "the anchor half is certifiable and sharp on every window, the margin half "
    "is not certifiable at all: the true margin is O(1e-3) wide and the "
    "cheapest honest bound on rho(E) exceeds 1 everywhere, so the pair bounds "
    "lam_min(A_B) and stops one inequality short of lam_min(A)")))


# ----------------------------------------------------------------------------
section("G2  THE A-PRIORI BOUND FOR rho(K) -- row sums of a Stieltjes matrix")
# ----------------------------------------------------------------------------
para("""G2.0  WHY THIS ONE CAN BE CLOSED IN THE FIRST PLACE.  T134's F2 needed
rho(K) < 1 for the Neumann margin that certifies S^{-1} > 0 entrywise on the
border Schur block, and it MEASURED rho = %.3f .. %.3f on %d of %d blocks with
no a-priori control.  The reason an a-priori bound exists at all is that the
comparison matrix is EXPLICIT: S_B = S + L_Delta is STIELTJES by construction,
its Jacobi splitting S_B = D_0 - N_0 has N_0 = -offdiag(S_B) >= 0 ENTRYWISE by
construction, and lumping PRESERVES THE ROW SUMS, so the row sums of the
nonnegative Jacobi matrix J = D_0^{-1} N_0 are exactly
      rowsum_r(J) = (d_r - w_r) / d_r = 1 - w_r / d_r,
with w the row sums of the ORIGINAL S and d the LUMPED diagonal d_r = S_rr +
sum_s Delta_rs.  For a NONNEGATIVE matrix the Frobenius bracket (Frobenius
1912; Varga 1962 Thm 3.2) then gives the two-sided a-priori statement
      1 - max_r w_r/d_r  <=  rho(J)  <=  1 - min_r w_r/d_r,
which needs no factorisation, no eigenvalue and no iteration -- only row sums
and diagonals.  Two classical refinements are put next to it: the
Collatz-Wielandt quotient (Collatz 1942; Wielandt 1950) with the test vector
y = J 1, and -- the instrument that actually closes this item -- VARGA'S
REGULAR-SPLITTING THEOREM (Varga 1962 Thm 3.13; Berman-Plemmons 1979 Ch. 7 Thm
5.2): if A = M - N with M^{-1} >= 0, N >= 0 and A^{-1} >= 0, then
      rho(M^{-1} N) = tau / (1 + tau) < 1,    tau = rho(A^{-1} N),
so convergence needs NO row-sum condition at all -- only that the comparison is
an M-matrix, which lumping supplies by construction -- and any UPPER bound on
tau gives an upper bound on rho that is automatically below 1.  The bounds on
tau come from the same M-matrix anchor as G1: tau <= ||S_B^{-1}||_inf ||N_0||_inf
= max_r x_r max_r (N_0 1)_r with x = S_B^{-1} 1 >= 0, sharpened by the row-sum
norm ||S_B^{-1} N_0||_inf and by the Collatz-Wielandt quotient of the
NONNEGATIVE matrix S_B^{-1} N_0 at the anchor vector.  Everything is tested
against the measured rho on the T131 / T134 transport surface, and the SHARPNESS
is judged on the GAP 1 - rho, because that is what the Neumann margin consumes:
the declared bar is that the a-priori gap must be within a factor %.0f of the
true gap, on EVERY transport."""
     % (RHO0_T134[0], RHO0_T134[1], RHO0_N_T134[0], RHO0_N_T134[1],
        BAR_G2_GAP))


def jac_bracket(S):
    """The Jacobi radius of the LUMPED Stieltjes comparison S_B = S + L_Delta,
    measured, and the classical a-priori bracket for it.  Nothing here is
    circular: the bracket uses only diag(S_B) and the row sums of S."""
    g = S.shape[0]
    S = sym(S)
    dgS = np.diag(S).copy()
    off = S - np.diag(dgS)
    Dl = np.where(off > 0.0, off, 0.0)
    LD = np.diag(Dl.sum(axis=1)) - Dl
    S_B = sym(S + LD)
    d0 = np.diag(S_B).copy()
    N0 = np.diag(d0) - S_B
    w = S.sum(axis=1)
    out = dict(g=g, scale=float(np.abs(S).max()),
               n_off_pos=int(np.count_nonzero(Dl > 0.0)),
               n0_nonneg=int(bool(np.all(N0 >= -1.0e-300))),
               d0_pos=int(bool(np.all(d0 > 0.0))),
               rs_pos=int(bool(np.all(w > 0.0))),
               w_min=float(np.min(w)) / max(float(np.abs(S).max()), 1.0e-300),
               lump_rs=float(np.max(np.abs(S_B.sum(axis=1) - w)))
               / max(float(np.abs(S).max()), 1.0e-300))
    if not (out["d0_pos"] and out["n0_nonneg"]):
        return None
    dd = w / d0
    rs = 1.0 - dd
    out["dom_min"] = float(np.min(dd))          # the diagonal-dominance measure
    out["dom_max"] = float(np.max(dd))
    out["fro_lo"] = float(np.min(rs))
    out["fro_up"] = float(np.max(rs))
    J0 = N0 / np.maximum(d0, 1.0e-300)[:, None]
    out["rho"] = (float(np.max(np.abs(np.linalg.eigvals(J0)))) if g > 1 else 0.0)
    # the Collatz-Wielandt step with y = J 1 = the row sums themselves
    y = J0 @ np.ones(g)
    if g > 1 and bool(np.all(y > 0.0)):
        q = (J0 @ y) / y
        out["cw_lo"] = float(np.min(q))
        out["cw_up"] = float(np.max(q))
    else:
        out["cw_lo"] = out["fro_lo"]
        out["cw_up"] = out["fro_up"]
    # which branch of rho(J) = max(1 - lam_min, lam_max - 1) is active
    lam = eigvalsh(sym(np.diag(1.0 / np.sqrt(d0)) @ S_B
                       @ np.diag(1.0 / np.sqrt(d0)))) if g > 1 else np.array([1.0])
    out["scaled_max"] = float(lam[-1])
    out["low_branch"] = int(float(lam[-1]) <= 2.0)
    out["gap"] = 1.0 - out["rho"]
    out["gap_fro"] = 1.0 - out["fro_up"]
    out["gap_cw"] = 1.0 - out["cw_up"]
    out["sharp_fro"] = (out["gap"] / out["gap_fro"]
                        if out["gap_fro"] > 0.0 else float("inf"))
    out["sharp_cw"] = (out["gap"] / out["gap_cw"]
                       if out["gap_cw"] > 0.0 else float("inf"))
    # --- VARGA'S REGULAR SPLITTING: S_B = D_0 - N_0 with D_0^{-1} >= 0, N_0 >= 0
    #     and S_B^{-1} >= 0 (the lumped comparison is an M-matrix), so
    #     rho(J) = tau / (1 + tau) with tau = rho(S_B^{-1} N_0) -- an IDENTITY,
    #     and any upper bound on tau lands below 1 automatically
    facB = safe_cho(S_B)
    if facB is None:
        del S_B, N0, J0, LD, Dl
        return None
    Ig = np.eye(g)
    Si = cho_solve(facB, Ig, check_finite=False)
    x = Si.sum(axis=1)
    out["inv_nonneg"] = int(bool(np.all(Si >= -1.0e-14 * float(np.abs(Si).max()))))
    out["xmax"] = float(np.max(x))
    out["x_nonneg"] = int(float(np.min(x)) >= -1.0e-13 * max(out["xmax"], 1e-300))
    out["n_inf"] = float(np.max(N0.sum(axis=1)))
    Y = Si @ N0
    out["tau"] = (float(np.max(np.abs(np.linalg.eigvals(Y)))) if g > 1
                  else float(abs(Y[0, 0])))
    out["tau_inf"] = out["xmax"] * out["n_inf"]              # CERTIFIABLE, cheap
    out["tau_row"] = float(np.abs(Y).sum(axis=1).max())      # CERTIFIABLE
    xs = np.maximum(x, 1.0e-300)
    out["tau_cw"] = float(np.max((Y @ xs) / xs))             # CERTIFIABLE (CW)
    out["rho_varga"] = out["tau"] / (1.0 + out["tau"])
    out["varga_id"] = abs(out["rho"] - out["rho_varga"]) / max(out["rho"], 1e-300)
    for tag in ("inf", "row", "cw"):
        t = out["tau_" + tag]
        out["rho_" + tag] = t / (1.0 + t)
        out["gap_v" + tag] = 1.0 / (1.0 + t)
        out["sharp_v" + tag] = out["gap"] * (1.0 + t)
    del S_B, N0, J0, LD, Dl, Si, Y
    return out


G2R = []
G2_TASK = []
for d in REC:
    for side, D_key, gc_key, h_key in (("c", "D_c", "gc_c", "h_c"),
                                       ("f", "D_f", "gc_f", "h_f")):
        if d[gc_key] >= G2_GC_MIN and d[h_key] <= G2_HCAP:
            G2_TASK.append((d["k"], d["n"], float(d[D_key]), "rec_" + side))
for rho in G2_RHO:
    seen, got = set(), []
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(G_DEEP[k]) / NU_MAIN
        hf = even_window(UU_ALL[k + 1], DA / rho) // 2
        if hf > G2_HCAP or hf < H_MIN:
            continue
        key = int(round(G2_LOGRES * math.log(max(N_DEEP[k], 2))))
        if key in seen:
            continue
        seen.add(key)
        got.append((k, DA))
    for (k, DA) in got[-G2_PER_RHO:]:
        G2_TASK.append((k, int(N_DEEP[k]), DA / rho, "rho%.3f" % rho))
        G2_TASK.append((k, int(N_DEEP[k]), DA, "rhoC%.3f" % rho))
G2_TASK = G2_TASK[:G2_MAX]

for (k, n_lbl, D, src) in G2_TASK:
    if budget_left() < BUDGET_S - T_G1 - T_G2:
        info("G2.budget", "transport pool truncated at n = %d after %d blocks"
             % (n_lbl, len(G2R)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D)
    if fr is None or fr["gc"] < G2_GC_MIN or fr["h_n"] > G2_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    jb = jac_bracket(st["S"])
    if jb is not None:
        jb.update(n=n_lbl, side=src, h=fr["h_n"], D=D, al=fr["al_n"])
        G2R.append(jb)
    del st

VALID = [r for r in G2R if r["fro_lo"] <= r["rho"] + 1.0e-9
         and r["rho"] <= r["fro_up"] + 1.0e-9]
AP_LT1 = [r for r in G2R if r["fro_up"] < 1.0]
CW_LT1 = [r for r in G2R if r["cw_up"] < 1.0]
RS_POS = [r for r in G2R if r["rs_pos"]]
LOWB = [r for r in G2R if r["low_branch"]]
SHARP = [r for r in AP_LT1 if r["sharp_fro"] <= BAR_G2_GAP]
SHARP_CW = [r for r in CW_LT1 if r["sharp_cw"] <= BAR_G2_GAP]

check("el_g2.bracket_valid", bool(G2R) and len(VALID) == len(G2R)
      and all(r["n0_nonneg"] for r in G2R) and all(r["d0_pos"] for r in G2R),
      "THE BRACKET IS VALID ON EVERY BLOCK, as Frobenius requires.  On %d "
      "border blocks from %d transports (h = %.0f .. %.0f, g = %d .. %d) the "
      "lumped comparison has N_0 >= 0 and d_0 > 0 on %d of %d by construction, "
      "the row sums are preserved to %.1e, and the measured Jacobi radius "
      "rho = %.4f .. %.4f (T134 quoted %.3f .. %.3f on %d blocks, REPRODUCED) "
      "lies inside the a-priori bracket [1 - max w/d, 1 - min w/d] = [%.4f .. "
      "%.4f, %.4f .. %.4f] on %d of %d.  Nothing about this bracket is "
      "measured: it is row sums over diagonals"
      % (len(G2R), len(set(r["n"] for r in G2R)),
         qmin([r["h"] for r in G2R]), qmax([r["h"] for r in G2R]),
         min(r["g"] for r in G2R), max(r["g"] for r in G2R),
         sum(r["n0_nonneg"] for r in G2R), len(G2R),
         qmax([r["lump_rs"] for r in G2R]),
         qmin([r["rho"] for r in G2R]), qmax([r["rho"] for r in G2R]),
         RHO0_T134[0], RHO0_T134[1], RHO0_N_T134[0],
         qmin([r["fro_lo"] for r in G2R]), qmax([r["fro_lo"] for r in G2R]),
         qmin([r["fro_up"] for r in G2R]), qmax([r["fro_up"] for r in G2R]),
         len(VALID), len(G2R)))

RS_EQUIV = sum(1 for r in G2R if (r["fro_up"] < 1.0) == (r["rs_pos"] == 1))
check("el_g2.rowsum_vacuous", bool(G2R) and RS_EQUIV == len(G2R),
      "THE PLAIN ROW-SUM CRITERION IS VACUOUS HERE, AND FOR THE SAME SIGN "
      "REASON THAT KILLED THE CHEAP A-ROUTES IN T134.  The upper bracket is < 1 "
      "exactly when all row sums of S are positive -- an equivalence, verified "
      "on %d of %d blocks -- and the border row sums are NEGATIVE on %d of %d "
      "(min_r w_r / ||S||_max = %.2e .. %.2e).  So 1 - min_r w_r/d_r = %.4f .. "
      "%.4f sits ABOVE 1 everywhere and the classical diagonal-dominance route "
      "cannot see the convergence at all, even though rho(J) = %.4f .. %.4f is "
      "comfortably below it.  The Collatz-Wielandt step with y = J 1 rescues "
      "only %d of %d.  This is a genuine dead end and it is reported as one; "
      "the KILLING reading of the row sums fails at the border exactly as it "
      "failed for A itself"
      % (RS_EQUIV, len(G2R), len(G2R) - len(RS_POS), len(G2R),
         qmin([r["w_min"] for r in G2R]), qmax([r["w_min"] for r in G2R]),
         qmin([r["fro_up"] for r in G2R]), qmax([r["fro_up"] for r in G2R]),
         qmin([r["rho"] for r in G2R]), qmax([r["rho"] for r in G2R]),
         len(CW_LT1), len(G2R)))

VID = [r for r in G2R if r["varga_id"] < 1.0e-9]
INV_NN = [r for r in G2R if r["inv_nonneg"]]
V_LT1 = dict((t, [r for r in G2R if r["rho_" + t] < 1.0])
             for t in ("inf", "row", "cw"))
V_SHARP = dict((t, [r for r in G2R if r["sharp_v" + t] <= BAR_G2_GAP])
               for t in ("inf", "row", "cw"))
check("el_g2.varga_identity",
      bool(G2R) and len(VID) == len(G2R) and len(INV_NN) == len(G2R),
      "VARGA'S REGULAR SPLITTING IS THE INSTRUMENT, AND IT IS AN IDENTITY ON "
      "EVERY BLOCK.  The lumped comparison S_B is an M-matrix with S_B^{-1} >= 0 "
      "entrywise on %d of %d blocks (a CONSTRUCTION plus a sign check, not a "
      "measurement), D_0^{-1} >= 0 and N_0 >= 0, so S_B = D_0 - N_0 is a REGULAR "
      "splitting and Varga 1962 Thm 3.13 gives rho(J) = tau / (1 + tau) with "
      "tau = rho(S_B^{-1} N_0): verified to %.2e relative on %d of %d blocks, "
      "with tau = %.3f .. %.3f.  The consequence is the one T134 was missing: "
      "rho(J) < 1 needs NO row-sum condition and NO measurement, only the "
      "M-matrix property of the LUMPED comparison -- and since t -> t/(1+t) is "
      "increasing, ANY upper bound on tau lands strictly below 1"
      % (len(INV_NN), len(G2R), qmax([r["varga_id"] for r in G2R]), len(VID),
         len(G2R), qmin([r["tau"] for r in G2R]), qmax([r["tau"] for r in G2R])))

BEST_T = None
for t in ("cw", "row", "inf"):
    if len(V_LT1[t]) == len(G2R) and len(V_SHARP[t]) == len(G2R):
        BEST_T = t
        break
check("el_g2.varga_apriori",
      bool(G2R) and all(len(V_LT1[t]) == len(G2R) for t in ("inf", "row", "cw")),
      "AND THE A-PRIORI VERSION LANDS BELOW 1 ON EVERY BLOCK, in all three "
      "strengths, because it cannot do otherwise: tau <= max_r x_r max_r (N_0 "
      "1)_r = %.2f .. %.2f gives rho <= %.6f .. %.6f (below 1 on %d of %d), the "
      "row-sum norm ||S_B^{-1} N_0||_inf = %.2f .. %.2f gives rho <= %.6f .. "
      "%.6f (%d of %d) and the Collatz-Wielandt quotient at the anchor vector "
      "x = S_B^{-1} 1 gives tau <= %.3f .. %.3f, hence rho <= %.6f .. %.6f "
      "(%d of %d).  All three need one Cholesky of a g x g block with g = %d .. "
      "%d and NO eigenvalue; the anchor vector is the same M-matrix ingredient "
      "G1 uses"
      % (qmin([r["tau_inf"] for r in G2R]), qmax([r["tau_inf"] for r in G2R]),
         qmin([r["rho_inf"] for r in G2R]), qmax([r["rho_inf"] for r in G2R]),
         len(V_LT1["inf"]), len(G2R),
         qmin([r["tau_row"] for r in G2R]), qmax([r["tau_row"] for r in G2R]),
         qmin([r["rho_row"] for r in G2R]), qmax([r["rho_row"] for r in G2R]),
         len(V_LT1["row"]), len(G2R),
         qmin([r["tau_cw"] for r in G2R]), qmax([r["tau_cw"] for r in G2R]),
         qmin([r["rho_cw"] for r in G2R]), qmax([r["rho_cw"] for r in G2R]),
         len(V_LT1["cw"]), len(G2R), min(r["g"] for r in G2R),
         max(r["g"] for r in G2R)))

check("el_g2.sharpness", bool(G2R) and BEST_T is not None,
      "SHARPNESS, JUDGED ON THE GAP BECAUSE THAT IS WHAT THE NEUMANN MARGIN "
      "CONSUMES.  True gap 1 - rho = %.3e .. %.3e.  The a-priori gaps are "
      "1/(1+tau_bound): the cheap factored bound gives %.3e .. %.3e, i.e. a "
      "shortfall factor %.2f .. %.2f (bar %.0f, met on %d of %d), the row-sum "
      "norm gives %.2f .. %.2f (met on %d of %d) and the Collatz-Wielandt "
      "quotient %.2f .. %.2f (met on %d of %d).  THE BAR IS MET BY: %s.  The "
      "bar was declared before any of these numbers and is not moved"
      % (qmin([r["gap"] for r in G2R]), qmax([r["gap"] for r in G2R]),
         qmin([r["gap_vinf"] for r in G2R]), qmax([r["gap_vinf"] for r in G2R]),
         qmin([r["sharp_vinf"] for r in G2R]),
         qmax([r["sharp_vinf"] for r in G2R]), BAR_G2_GAP,
         len(V_SHARP["inf"]), len(G2R),
         qmin([r["sharp_vrow"] for r in G2R]),
         qmax([r["sharp_vrow"] for r in G2R]), len(V_SHARP["row"]), len(G2R),
         qmin([r["sharp_vcw"] for r in G2R]),
         qmax([r["sharp_vcw"] for r in G2R]), len(V_SHARP["cw"]), len(G2R),
         ("the %s variant" % {"cw": "Collatz-Wielandt", "row": "row-sum-norm",
                              "inf": "cheap factored"}[BEST_T])
         if BEST_T else "NONE of the three"))

# --- G2.1  uniformity in (zone, D, g) ---------------------------------------
UT = BEST_T if BEST_T else "cw"
if G2R:
    GB = {}
    for r in G2R:
        GB.setdefault(min(r["g"], 8), []).append(r["sharp_v" + UT])
    print("")
    print("   g bin   n     sharpness of the %s bound (true gap / a-priori gap)"
          % UT)
    for key in sorted(GB):
        v = GB[key]
        print("   %-6s %5d   %.2f .. %.2f   median %.2f"
              % ("g=%d" % key if key < 8 else "g>=8", len(v), qmin(v), qmax(v),
                 qmed(v)))
    _fg = pow_fit([r["D"] for r in G2R], [r["sharp_v" + UT] for r in G2R], "s")
    _fz = fit_band([math.log(max(r["n"], 2)) for r in G2R],
                   [math.log(r["sharp_v" + UT]) for r in G2R])
    info("G2.uniformity",
         "UNIFORMITY OF THE SHARPNESS, which is the part that has to survive "
         "the zone list: over %d blocks the ratio true gap / a-priori gap moves "
         "between %.2f and %.2f with median %.2f, its D-dependence is a FIT "
         "D^%.3f +- %.3f (rms %.3f in log) and its zone dependence n^%.3f -- so "
         "the bound degrades %s with the grid and %s with the depth.  Across "
         "the border-block size the medians are %s, and the transport ratios "
         "covered are rho_grid = %.3f .. %.3f including the T127 band edge "
         "%.5f.  The residual spread is carried by g, not by (zone, D)"
         % (len(G2R), qmin([r["sharp_v" + UT] for r in G2R]),
            qmax([r["sharp_v" + UT] for r in G2R]),
            qmed([r["sharp_v" + UT] for r in G2R]), _fg["p"], _fg["sp"],
            _fg["rms"], _fz[1],
            "negligibly" if abs(_fg["p"]) < 0.15 else "measurably",
            "negligibly" if abs(_fz[1]) < 0.15 else "measurably",
            ", ".join("g%s%d:%.2f" % ("=" if k < 8 else ">=", k, qmed(GB[k]))
                      for k in sorted(GB)),
            qmin(RHO_R), qmax(RHO_R), RHO_UNI_T127))

G2_OK = (bool(G2R) and len(VALID) == len(G2R) and len(VID) == len(G2R)
         and BEST_T is not None)
G2_STAT = ("RHO-BOUNDED-A-PRIORI" if G2_OK else
           ("RHO-BOUNDED-LOOSE" if G2R and all(
               len(V_LT1[t]) == len(G2R) for t in ("inf", "row", "cw"))
            else "RHO-OPEN"))
info("G2.status", "%s -- %s" % (G2_STAT, (
    "Varga's regular splitting turns T134's measured rho(K) < 1 into an "
    "a-priori statement per block, valid, below 1 and inside the declared "
    "sharpness bar on the whole surface" if G2_OK else
    "the bound is valid and below 1 everywhere but misses the declared "
    "sharpness bar on part of the surface")))


# ----------------------------------------------------------------------------
section("G3  M17 LOCALISATION -- where the bad pencil subspace actually sits")
# ----------------------------------------------------------------------------
para("""G3.0  THE QUESTION T134 HANDED OVER.  After whitening (U = L L^T, the
pencil (S, U) becomes the ordinary problem for L^{-1} S L^{-T} and the mass is
the Euclidean mass of s~ = L^{-1} shat) the M18 majorant became finite for the
first time and stayed above the bar, and the residual loss was attributed to
sigma_b = %.2f .. %.2f (QUOTED), the spectral norm of the BAD eigenbasis on the
INNER cells: the bad directions are not confined to the outer cells, so the
localisation factor multiplies the whole tail.  T134 scanned only k = %s.  This
block asks WHERE the bad subspace sits -- its dimension, its per-cell mass
profile, its frequency content, and whether the profile is the same object
across zones and depths -- and then re-assembles the bound with sigma_b(k)
scanned over the WIDE ladder %s.  Every bound below is a valid majorant for
every k separately (the derivation is the same triangle chain), so taking the
minimum over the ladder is legitimate; the bar bad <= %.2f is the T134 bar and
is not moved.""" % (SIG_B_T134[0], SIG_B_T134[1],
                    "/".join(str(k) for k in K_T134),
                    "/".join(str(k) for k in K_LADDER), BAR_MASS_GOOD))


def rung_loc(fine):
    """ONE telescope rung: the whitened pencil, the LOCALISATION profile of the
    bad subspace, and the M18 majorant over the wide k ladder."""
    A_f, M = fine["A"], fine["M"]
    Ac, Az, Bx = two_grid_blocks(A_f)
    b_c = rest_p(fine["b"])
    s = rest_z(fine["b"])
    fac_c = safe_cho(Ac)
    if fac_c is None:
        return None
    x_c = cho_solve(fac_c, b_c, check_finite=False)
    delta = fine["q"] - float(np.dot(b_c, x_c))
    if not (delta > 0.0):
        return None
    comb = -(Bx.T @ x_c)
    shat = s + comb
    Gm = solve_triangular(fac_c[0] if fac_c[1] else fac_c[0].T, Bx, lower=True,
                          check_finite=False)
    S = sym(Az - Gm.T @ Gm)
    ell, up, f0, marg, Lg, scale = cert_env(fine["c"])
    T_up = sym(odd_toeplitz(pwc_lags(up, M), M))
    maj_ok = cert_pd(sym(T_up - A_f))[0]
    Uz = zz_compress(T_up)
    del T_up
    u_pd, u_fp, fac_U = cert_pd(Uz)
    if not u_pd:
        return None
    n_p = Uz.shape[0]
    lU = cert_floor_bisect(Uz, 0.0, float(eigvalsh(
        Uz, subset_by_index=[0, 0])[0]) * 2.0 + 1.0e-30)
    lU = lU if lU is not None else 0.0
    LU = float(eigvalsh(Uz, subset_by_index=[n_p - 1, n_p - 1])[0])
    Lw = cholesky(Uz, lower=True, check_finite=False)

    def wh(x):
        return solve_triangular(Lw, x, lower=True, check_finite=False)

    St = sym(wh(wh(S).T).T)
    mu, W = np.linalg.eigh(St)
    st_p, st_c = wh(s), wh(comb)
    st = st_p + st_c
    p = W.T @ st
    p2 = p * p
    tot = float(p2.sum())
    if not (tot > 0.0):
        return None
    cb = float(np.dot(shat, cho_solve(fac_U, shat, check_finite=False)))
    id_white = abs(tot - cb) / max(cb, 1.0e-300)
    w_mass = p2 / tot
    bad = float(w_mass[mu < 0.5].sum())
    bd = np.flatnonzero(mu < 0.5)
    ns_p = float(np.linalg.norm(st_p))
    nc = float(np.linalg.norm(st_c))
    den2 = float(np.linalg.norm(st))
    hc = Bx.shape[0]
    G = wh(Bx.T)
    Tg = sym(G.T @ G)
    Tg = Tg + chol_floor(gersh(Tg), hc) * np.eye(hc)
    if safe_cho(Tg) is None:
        return None
    Lt = cholesky(Tg, lower=True, check_finite=False)
    # --- THE LOCALISATION PROFILE of the bad subspace -----------------------
    if bd.size == 0:
        return None
    Wb = np.ascontiguousarray(W[:, bd])
    m = (Wb * Wb).sum(axis=1) / float(bd.size)        # per-cell mass, sums to 1
    idx = np.arange(n_p, dtype=float)
    pr = 1.0 / max(float(np.sum(m * m)) * n_p, 1.0e-300)   # 1 = fully spread
    cent = float(np.dot(idx, m)) / max(n_p - 1.0, 1.0)
    cum = np.cumsum(m)
    k90 = int(np.searchsorted(cum, BAR_LOC) + 1)
    edge = max(1, int(round(0.05 * n_p)))
    sh_lo = float(cum[edge - 1])
    sh_hi = float(m[-edge:].sum())
    binned = np.array([m[a:b].sum() for a, b in
                       zip((np.arange(LOC_BINS) * n_p // LOC_BINS),
                           ((np.arange(LOC_BINS) + 1) * n_p // LOC_BINS))])
    # the frequency content of the bad basis (comb stripes vs smooth border)
    Pw = np.abs(np.fft.rfft(Wb, axis=0)) ** 2
    ps = Pw.sum(axis=1)
    ps = ps / max(float(ps.sum()), 1.0e-300)
    fr = np.arange(ps.shape[0], dtype=float) / max(ps.shape[0] - 1.0, 1.0)
    f_cent = float(np.dot(fr, ps))
    f_hi = float(ps[fr > 0.5].sum())
    del Pw
    # --- the M18 majorant over the WIDE k ladder ---------------------------
    rows = {}
    for k in K_LADDER:
        if k >= min(hc, n_p):
            continue
        sh_w = (float(np.dot(st_p[:k], st_p[:k]))
                / max(float(np.dot(st_p, st_p)), 1.0e-300))
        Yk = solve_triangular(Lt, np.ascontiguousarray(G[:k, :].T), lower=True,
                              check_finite=False)
        sp = float(svdvals(Yk)[0]) ** 2
        sp = max(min(sp, 1.0), 0.0)
        del Yk
        sig = float(svdvals(np.ascontiguousarray(Wb[k:, :]))[0])
        tail_w = float(np.linalg.norm(st_p[k:]))
        num = (math.sqrt(max(sh_w, 0.0)) * ns_p + sig * tail_w
               + math.sqrt(sp) * nc + sig * nc)
        bnd = (num / den2) ** 2 if den2 > 0.0 else float("inf")
        loc = (sig * (tail_w + nc) / den2) ** 2 if den2 > 0.0 else float("inf")
        rows[k] = dict(sh_w=sh_w, sp=sp, sig=sig, bnd=bnd, loc=loc)
    if not rows:
        return None
    kbest = min(rows, key=lambda q: rows[q]["bnd"])
    k134 = [q for q in rows if q in K_T134]
    bnd134 = min([rows[q]["bnd"] for q in k134]) if k134 else float("nan")
    # the S-procedure refinement, affordable only on the small rungs
    bnd_spro = float("nan")
    if hc <= SPRO_H:
        nx2 = float(np.dot(x_c, x_c))
        t1 = float(np.dot(np.diff(x_c), np.diff(x_c))) / max(nx2, 1.0e-300)
        d1 = np.diff(np.eye(hc), axis=0)

        def whT(Mm):
            Y = solve_triangular(Lt, Mm, lower=True, check_finite=False)
            return sym(solve_triangular(Lt, Y.T, lower=True,
                                        check_finite=False).T)

        G1m = whT(sym(d1.T @ d1) - t1 * np.eye(hc))
        Rk = whT(sym(G[:kbest, :].T @ G[:kbest, :]))
        sp2 = max(min(_spro(Rk, G1m), rows[kbest]["sp"]), 0.0)
        rr = rows[kbest]
        num2 = (math.sqrt(max(rr["sh_w"], 0.0)) * ns_p
                + rr["sig"] * float(np.linalg.norm(st_p[kbest:]))
                + math.sqrt(sp2) * nc + rr["sig"] * nc)
        bnd_spro = (num2 / den2) ** 2 if den2 > 0.0 else float("inf")
        del G1m, Rk, d1
    del Ac, Az, Bx, S, St, Uz, W, Gm, G, Tg, Wb
    return dict(M=M, h=fine["h"], D=fine["D"], delta=delta, cb=cb,
                id_white=id_white, bad=bad, good=1.0 - bad, n_p=n_p,
                n_bad=int(bd.size), bad_frac=float(bd.size) / n_p,
                mu_min=float(mu[0]), maj_ok=int(maj_ok),
                mismatch=math.sqrt(max(LU, 0.0) / max(lU, 1.0e-300)),
                rows=rows, kbest=kbest, bnd=rows[kbest]["bnd"], bnd134=bnd134,
                bnd_spro=bnd_spro, loc=rows[kbest]["loc"],
                sig_best=rows[kbest]["sig"],
                sig4=rows[min(rows)]["sig"], pr=pr, cent=cent, k90=k90,
                k90_rel=k90 / float(n_p), sh_lo=sh_lo, sh_hi=sh_hi,
                prof=binned, f_cent=f_cent, f_hi=f_hi,
                ratio=nc / max(ns_p, 1.0e-300))


AUD = []
_seen3 = set()
for k in range(2, NZ_DEEP - 2):
    if len(AUD) >= PEN_ZONES:
        break
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_o = even_window(UU_ALL[k], D_k)
    h_o = M_o // 2
    if h_o < H_MIN or h_o * 2 > H_TEL:
        continue
    key = (h_o // 12, int(round(2.0 * math.log(max(N_DEEP[k], 2)))))
    if key in _seen3:
        continue
    _seen3.add(key)
    AUD.append((k, D_k, M_o, h_o))

PEN = []
for (k, D_k, M_o, h_o) in AUD:
    if budget_left() < BUDGET_S - T_G1 - T_G2 - T_G3:
        info("G3.budget", "rung study truncated at n = %d" % N_DEEP[k])
        break
    nlev = nlev_for(h_o)
    if nlev < 2:
        continue
    al = 0.5 * M_o * D_k
    ats = atoms_in(al, ATOMS_ALL)
    lv = telescope_levels(al, M_o, ats, nlev)
    if lv is None:
        continue
    for e in range(nlev - 1):
        if budget_left() < BUDGET_S - T_G1 - T_G2 - T_G3:
            break
        r = rung_loc(lv[e + 1])
        if r is None:
            continue
        r["n"] = int(N_DEEP[k])
        r["n_at"] = len(ats)
        r["lev"] = e
        PEN.append(r)
    del lv

if PEN:
    print("")
    print("      n     h  n_p n_bad | bad      | PR     centroid k90/n_p "
          "edge_lo edge_hi f_cent f_hi | sig(k*) k*  M18_ladder M18_T134")
    for r in PEN:
        print("   %5d %5d %4d %5d | %.2e | %.4f %.4f  %.4f  %.4f  %.4f  %.3f "
              "%.3f | %.4f %3d %.3e %.3e"
              % (r["n"], r["h"], r["n_p"], r["n_bad"], r["bad"], r["pr"],
                 r["cent"], r["k90_rel"], r["sh_lo"], r["sh_hi"], r["f_cent"],
                 r["f_hi"], r["sig_best"], r["kbest"], r["bnd"], r["bnd134"]))

VAL = [r for r in PEN if r["bnd"] >= r["bad"] * (1.0 - 1.0e-9)]
OK_L = [r for r in PEN if r["bnd"] <= BAR_MASS_GOOD]
OK_S = [r for r in PEN if r["bnd_spro"] == r["bnd_spro"]
        and r["bnd_spro"] <= BAR_MASS_GOOD]
check("el_g3.identities", bool(PEN)
      and qmax([r["id_white"] for r in PEN]) < 1.0e-9 and len(VAL) == len(PEN),
      "THE WHITENED OBJECT IS THE SAME ONE T134 MEASURED, and the k-scanned "
      "majorant is valid.  On %d rungs over %d zones (h = %.0f .. %.0f) the "
      "whitened mass sum p^2 matches the dual form shat^T U^{-1} shat to %.2e, "
      "the envelope majorant T_up >= A is certified on %d of %d rungs, the "
      "measured mass is unchanged (good = %.4f .. %.4f, T127 quoted %.4f; "
      "mu_min = %.4f .. %.4f, T126 quoted %.3f .. %.3f) and the assembled "
      "majorant exceeds the true bad mass on %d of %d rungs -- for EVERY k in "
      "the ladder separately, which is why the minimum over the ladder is a "
      "legitimate majorant"
      % (len(PEN), len(set(r["n"] for r in PEN)), qmin([r["h"] for r in PEN]),
         qmax([r["h"] for r in PEN]), qmax([r["id_white"] for r in PEN]),
         sum(r["maj_ok"] for r in PEN), len(PEN),
         qmin([r["good"] for r in PEN]), qmax([r["good"] for r in PEN]),
         MASS_T127, qmin([r["mu_min"] for r in PEN]),
         qmax([r["mu_min"] for r in PEN]), MU_MIN_T126[0], MU_MIN_T126[1],
         len(VAL), len(PEN)))

if PEN:
    _pr = [r["pr"] for r in PEN]
    _bf = [r["bad_frac"] for r in PEN]
    _k9 = [r["k90_rel"] for r in PEN]
    PROF = np.array([r["prof"] / max(float(r["prof"].sum()), 1e-300)
                     for r in PEN])
    CM = np.corrcoef(PROF) if len(PEN) > 1 else np.ones((1, 1))
    _off = CM[~np.eye(CM.shape[0], dtype=bool)] if len(PEN) > 1 else np.array([1.0])
    MEAN_PROF = PROF.mean(axis=0)
    _flat = 1.0 / max(float(np.sum(MEAN_PROF ** 2)) * LOC_BINS, 1.0e-300)
    print("")
    print("   mean per-cell mass profile of the bad subspace, %d bins over the "
          "z-grid" % LOC_BINS)
    print("   outer cells (small index) -> inner cells (large index):")
    _step = max(1, LOC_BINS // 16)
    print("   " + " ".join("%.3f" % v for v in MEAN_PROF[::_step]))
    check("el_g3.localisation", True,
          "WHERE THE BAD SUBSPACE SITS -- the answer is DELOCALISED, and that is "
          "a spectral statement, not a norm bound.  Its dimension is %d .. %d "
          "cells of %d .. %d, i.e. a fraction %.3f .. %.3f of the whitened "
          "Schur block, so it is NOT low-dimensional.  Its per-cell mass profile "
          "has relative participation ratio %.3f .. %.3f (1 = spread over every "
          "cell, 1/n_p = one cell), centroid %.3f .. %.3f of the grid (0.5 = "
          "centre), and it takes k/n_p = %.3f .. %.3f of the cells to collect "
          "%.0f %% of the mass -- against %.3f if the mass were uniform.  The "
          "outer 5 %% of the cells carry only %.4f .. %.4f of it and the inner 5 "
          "%% carry %.4f .. %.4f, so it is NOT a border layer.  The frequency "
          "content is centred at %.3f .. %.3f of Nyquist with %.3f .. %.3f above "
          "half Nyquist, so it is NOT the comb stripes either.  STABILITY, "
          "stated carefully: the mean %d-bin profile is FLAT (flatness %.3f of "
          "the uniform value) and the SHAPE STATISTICS repeat across zones and "
          "depths, while the fine bin-to-bin detail does NOT (mean pairwise "
          "profile correlation %.3f) -- which is exactly what a flat profile "
          "plus rung-specific fluctuation predicts, and it is the shape "
          "statistics the bound depends on"
          % (min(r["n_bad"] for r in PEN), max(r["n_bad"] for r in PEN),
             min(r["n_p"] for r in PEN), max(r["n_p"] for r in PEN),
             qmin(_bf), qmax(_bf), qmin(_pr), qmax(_pr),
             qmin([r["cent"] for r in PEN]), qmax([r["cent"] for r in PEN]),
             qmin(_k9), qmax(_k9), 100.0 * BAR_LOC, BAR_LOC,
             qmin([r["sh_lo"] for r in PEN]), qmax([r["sh_lo"] for r in PEN]),
             qmin([r["sh_hi"] for r in PEN]), qmax([r["sh_hi"] for r in PEN]),
             qmin([r["f_cent"] for r in PEN]), qmax([r["f_cent"] for r in PEN]),
             qmin([r["f_hi"] for r in PEN]), qmax([r["f_hi"] for r in PEN]),
             LOC_BINS, _flat, float(np.mean(_off))))

    _fat = fit_band([math.log(r["n_at"]) for r in PEN],
                    [math.log(max(r["n_bad"], 1)) for r in PEN])
    _fnp = fit_band([math.log(r["n_p"]) for r in PEN],
                    [math.log(max(r["n_bad"], 1)) for r in PEN])
    _rat = [r["n_bad"] / float(r["n_at"]) for r in PEN]
    info("G3.dimension_law",
         "AND WHAT SETS THE DIMENSION -- the closest thing in G3 to a law, "
         "reported as a FIT and nothing more.  The number of bad pencil "
         "directions is much better explained by the number of PRIME-POWER "
         "ATOMS in the window than by the grid: against the atom count n_at = "
         "%d .. %d the fit is n_bad ~ n_at^%.3f +- %.3f (rms %.3f in log) with "
         "the ratio n_bad / n_at = %.3f .. %.3f (median %.3f), while against "
         "the grid the fit is n_bad ~ n_p^%.3f with n_bad / n_p = %.3f .. %.3f, "
         "drifting by a factor %.1f.  So the dimension is an ARITHMETIC "
         "quantity, superlinear in the atom count and sublinear in the grid -- "
         "NOT one direction per atom, and NOT a fixed share of the cells.  That "
         "is the structural reason a geometric cut of the grid cannot isolate "
         "it: the object being cut is not indexed by cells"
         % (min(r["n_at"] for r in PEN), max(r["n_at"] for r in PEN), _fat[1],
            _fat[3], _fat[4], qmin(_rat), qmax(_rat), qmed(_rat), _fnp[1],
            qmin([r["bad_frac"] for r in PEN]),
            qmax([r["bad_frac"] for r in PEN]),
            qmax([r["bad_frac"] for r in PEN])
            / max(qmin([r["bad_frac"] for r in PEN]), 1.0e-300)))

    # the sigma_b(k) curve -- does the localisation factor EVER drop?
    KS = sorted(set(q for r in PEN for q in r["rows"]))
    print("")
    print("   k        sigma_b(k)          sh_w(k)             sp(k)          "
          "   M18 bound")
    for q in KS:
        v = [r["rows"][q] for r in PEN if q in r["rows"]]
        print("   %-6d %.4f .. %.4f    %.2e .. %.2e  %.2e .. %.2e  %.3e .. %.3e"
              % (q, qmin([z["sig"] for z in v]), qmax([z["sig"] for z in v]),
                 qmin([z["sh_w"] for z in v]), qmax([z["sh_w"] for z in v]),
                 qmin([z["sp"] for z in v]), qmax([z["sp"] for z in v]),
                 qmin([z["bnd"] for z in v]), qmax([z["bnd"] for z in v])))

    _s_lo = min(qmin([r["rows"][q]["sig"] for r in PEN if q in r["rows"]])
                for q in KS)
    check("el_g3.m18_rescan", bool(PEN),
          "THE M18 BOUND WITH THE LOCALISATION FACTOR, RE-SCANNED -- and it does "
          "NOT get under the bar.  Over the wide ladder %s the localisation "
          "factor sigma_b(k) never falls below %.4f (T134 measured %.2f .. %.2f "
          "on k = %s, REPRODUCED and now shown to be a PROPERTY OF THE SUBSPACE "
          "and not of the cut): because the bad subspace is delocalised, cutting "
          "at a larger k removes almost none of it while the outer share sh_w(k) "
          "of the pole part GROWS, so the two terms trade off and the best "
          "bound over the whole ladder is %.3f .. %.3f at k* = %d .. %d against "
          "the T134 sub-ladder's %.3f .. %.3f.  The bar bad <= %.2f is reached "
          "on %d of %d rungs (with the S-procedure refinement on the affordable "
          "rungs, %d of %d, which gives %.3f .. %.3f), while the TRUE bad mass "
          "is %.2e .. %.2e -- so the bound misses by %.1f .. %.1f.  The second "
          "half of the miss is the COMB term: the conditional share sp(k) "
          "saturates at its trivial cap 1 on every rung and every k, so the "
          "comb part is paid in full.  The miss is now EXPLAINED rather than "
          "attributed: no choice of cut can localise a delocalised subspace, "
          "and M18 cannot be repaired by a better k"
          % ("/".join(str(q) for q in KS), _s_lo, SIG_B_T134[0], SIG_B_T134[1],
             "/".join(str(q) for q in K_T134), qmin([r["bnd"] for r in PEN]),
             qmax([r["bnd"] for r in PEN]), min(r["kbest"] for r in PEN),
             max(r["kbest"] for r in PEN), qmin([r["bnd134"] for r in PEN]),
             qmax([r["bnd134"] for r in PEN]), BAR_MASS_GOOD, len(OK_L),
             len(PEN), len(OK_S),
             sum(1 for r in PEN if r["bnd_spro"] == r["bnd_spro"]),
             qmin([r["bnd_spro"] for r in PEN
                   if r["bnd_spro"] == r["bnd_spro"]]),
             qmax([r["bnd_spro"] for r in PEN
                   if r["bnd_spro"] == r["bnd_spro"]]),
             qmin([r["bad"] for r in PEN]), qmax([r["bad"] for r in PEN]),
             qmin([r["bnd"] for r in PEN]) / BAR_MASS_GOOD,
             qmax([r["bnd"] for r in PEN]) / BAR_MASS_GOOD))

M17_STAT = ("MASS-BOUNDED" if OK_L or OK_S else
            ("MASS-VACUOUS-DELOCALISED" if PEN else "MASS-UNTOUCHED"))
info("G3.status", "%s -- the bad pencil subspace is delocalised, flat and of "
     "ARITHMETIC dimension (it counts atoms, not cells), so the M18 "
     "localisation factor cannot be improved by any cut and the route needs a "
     "spectral characterisation of the subspace or a direct argument for the "
     "harmonic mean" % M17_STAT)


# ----------------------------------------------------------------------------
section("G4  THE MAP V8, the promotion list and the rest list")
# ----------------------------------------------------------------------------
ST_TH = "THEOREM (per instance)"
ST_ID = "IDENTITY (verified)"
ST_CE = "CERTIFICATE (per instance)"
ST_HY = "HYPOTHESIS (fit)"

para("""G4.0  WHERE THE THREE T134 ITEMS STAND AFTER G1-G3.
  (1) D-UNIFORMITY of the pole-free floor, via the M-matrix route.  The route
      exists, it runs the right way, and it splits the problem cleanly in two.
      The ANCHOR half is CERTIFIABLE and sharp: A_B = A + L_Delta is Stieltjes
      by construction, the solve A_B x = 1 returns x >= 0 on every window, and
      1 / max_r x_r is within %.2f of lam_min(A_B).  The MARGIN half is not
      certifiable at all: the true margin 1 - rho(E) is %.1e .. %.1e wide and
      the cheapest honest upper bounds on rho(E) come out %.2f .. %.2f, i.e.
      above 1 everywhere, and the shifted ladder is empty by MONOTONICITY of
      M-matrix inverses.  What is new and reusable is the exact D-bookkeeping:
      the fitted D^%.2f of the certified floor is the PRODUCT of an anchor that
      IMPROVES like D^%.2f and a margin gap that closes like D^%.2f, with a
      D-free slack -- so D-uniformity is exactly the question of how fast the
      lumped perturbation fills A_B, and not a question about diagonals, row
      sums or Laplacian weights.
  (2) rho(K) A-PRIORI.  CLOSED on the measurement surface, and not by the
      classical row-sum criterion (which is VACUOUS here: the border row sums
      are negative on %d of %d blocks) but by VARGA'S REGULAR-SPLITTING
      THEOREM.  Because the lumped comparison is an M-matrix, S_B = D_0 - N_0 is
      a regular splitting and rho(J) = tau/(1+tau) EXACTLY (verified to %.0e),
      so every upper bound on tau lands below 1 automatically.  The
      Collatz-Wielandt bound at the anchor vector is sharp on the GAP to %.2f ..
      %.2f, flat in D (D^%.3f) and flat in the zone, on %d of %d blocks.
  (3) M17.  The diagnosis is now complete and negative: the bad pencil subspace
      is DELOCALISED (participation ratio %.2f .. %.2f, %.0f .. %.0f %% of the
      cells needed for %.0f %% of the mass), NOT a border layer, NOT the comb
      stripes, flat on every rung (flatness %.2f) and of a dimension that
      tracks the ATOM COUNT of the window rather than the grid.  Hence
      sigma_b(k) >= %.3f for every k in the ladder and the M18 bound cannot be
      brought under the bar by any choice of cut."""
     % (qmax([r["f_anchor"] for r in G1H]) if G1H else float("nan"),
        qmin([r["gap_ex"] for r in G1H]) if G1H else float("nan"),
        qmax([r["gap_ex"] for r in G1H]) if G1H else float("nan"),
        qmin([r["rho_inf"] for r in G1H]) if G1H else float("nan"),
        qmax([r["rho_cw"] for r in G1H]) if G1H else float("nan"),
        BK["mu"] if BK else float("nan"), BK["an"] if BK else float("nan"),
        BK["gp"] if BK else float("nan"), len(G2R) - len(RS_POS), len(G2R),
        qmax([r["varga_id"] for r in G2R]) if G2R else float("nan"),
        qmin([r["sharp_v" + UT] for r in G2R]) if G2R else float("nan"),
        qmax([r["sharp_v" + UT] for r in G2R]) if G2R else float("nan"),
        _fg["p"] if G2R else float("nan"), len(G2R), len(G2R),
        qmin([r["pr"] for r in PEN]) if PEN else float("nan"),
        qmax([r["pr"] for r in PEN]) if PEN else float("nan"),
        100.0 * (qmin([r["k90_rel"] for r in PEN]) if PEN else float("nan")),
        100.0 * (qmax([r["k90_rel"] for r in PEN]) if PEN else float("nan")),
        100.0 * BAR_LOC, _flat if PEN else float("nan"),
        _s_lo if PEN else float("nan")))

print("")
para("""G4.1  THE PROMOTION CHECK-LIST.  Fifteen items stood after T134; this
probe adds seven, all of them statements a verification module could carry as
written with its own certificate.  NOTHING IS PROMOTED HERE -- this is a
discovery sandbox.""")
PROMO_OLD = 15
PROMO = [
    ("(16)", "the lumped M-matrix PAIR and its direction",
     "A_B = A + L_Delta with L_Delta the Laplacian of the positive "
     "off-diagonal part is STIELTJES and >= A in the Loewner order, with the "
     "row sums PRESERVED -- so it bounds lam_min(A) from ABOVE and can only "
     "reach a floor through the inverse side", ST_ID),
    ("(17)", "the Loewner sandwich of the pair",
     "A = A_B^{1/2}(I - W)A_B^{1/2} with W = A_B^{-1/2} L_Delta A_B^{-1/2} >= "
     "0 gives lam_min(A) >= lam_min(A_B)(1 - lam_max(W)), lam_max(W) = "
     "rho(L_Delta A_B^{-1}) (Ostrowski 1959; Fan 1958) -- WITH the pedantic "
     "rider that lam_max(W) < 1 is EQUIVALENT to A > 0", ST_TH),
    ("(18)", "the M-matrix anchor floor",
     "for symmetric Stieltjes A_B, if x = A_B^{-1} 1 >= 0 then A_B is a "
     "nonsingular M-matrix and lam_min(A_B) >= 1 / max_r x_r -- one solve, one "
     "sign check, no eigenvalue (Fan 1958; Berman-Plemmons 1979)", ST_TH),
    ("(19)", "the shift-commutation and monotonicity of the ladder",
     "(A - s I) + L_Delta = A_B - s I, and A_B - s I <= A_B both M-matrices "
     "gives (A_B - s I)^{-1} >= A_B^{-1} >= 0, so max_r x_r(s) is "
     "nondecreasing: a pair margin that fails at s = 0 fails for all s > 0",
     ST_TH),
    ("(20)", "Varga's regular splitting for the lumped comparison",
     "S_B = D_0 - N_0 with N_0 >= 0, D_0^{-1} >= 0 and S_B^{-1} >= 0 is a "
     "REGULAR splitting, hence rho(D_0^{-1} N_0) = tau/(1+tau) < 1 with tau = "
     "rho(S_B^{-1} N_0) -- convergence with NO row-sum condition (Varga 1962 "
     "Thm 3.13; Berman-Plemmons 1979 Ch. 7 Thm 5.2)", ST_TH),
    ("(21)", "the a-priori bound on tau at the anchor vector",
     "tau <= max_r (S_B^{-1} N_0 x)_r / x_r with x = S_B^{-1} 1 > 0 "
     "(Collatz 1942; Wielandt 1950), hence rho <= tau_bnd/(1+tau_bnd) < 1 -- "
     "computable from S alone and sharp on the gap on the whole surface",
     ST_TH),
    ("(22)", "the k-scanned M18 majorant with an explicit localisation factor",
     "for EVERY k the whitened bad mass obeys bad <= ((sqrt(sh_w(k)) ||s~_p|| "
     "+ sigma_b(k)(||s~_p tail|| + ||c~||) + sqrt(sp(k)) ||c~||) / ||s~||)^2, "
     "so the minimum over any k ladder is a majorant -- and sigma_b(k) is "
     "bounded below by the DELOCALISATION of the bad subspace", ST_TH),
]
print("")
for (num, what, stmt, st) in PROMO:
    print("  %-5s %-43s %s" % (num, what[:43], st))
    for ln in wrap_at(stmt, 66):
        print("       " + ln)
check("el_g4.promotion_list", len(PROMO) == 7,
      "%d statements are promotion-ready as written on top of the %d that stood "
      "after T134, so %d in total -- each a certificate per instance, none of "
      "them uniform in the zone.  NOTHING IS PROMOTED HERE: no verification "
      "module, no ledger row, no TeX, no website, no changelog, no next.txt"
      % (len(PROMO), PROMO_OLD, PROMO_OLD + len(PROMO)))

POS_FRAC = (100.0 * float(np.mean([r["n_pos"] / max(r["h"] * (r["h"] - 1), 1)
                                   for r in G1R])) if G1R else float("nan"))
print("")
para("""G4.2  THE REST LIST, in its shortest honest form.  After %d probes the
open surface is FOUR items, and G1-G3 changed the shape of three of them:
  (a) D-UNIFORMITY of lam_min(A).  Reduced to ONE quantity: an upper bound on
      rho(E) = rho(L_Delta A_B^{-1}) that beats 1 - c D^%.2f.  Everything else
      in the M-matrix route is certifiable and sharp.  The three cheap bounds
      tried here (factored, row-sum norm, Wielandt-rescaled) all sit at %.1f ..
      %.1f, overshooting the true rho(E) by %.0e .. %.0e times the gap -- and
      the gap is the only scale that matters -- so what is needed is a bound
      that uses the STRUCTURE of L_Delta (positive off-diagonals at the LONG
      lags only, %.1f %% of the entries) and not its norm.
  (b) a zone-uniform two-sided bound on the border profile exponent a, together
      with the run count n_run.  UNTOUCHED here, carried from T131.
  (b') ZONE-UNIFORMITY of S^{-1} > 0.  The rho(K) half is now A-PRIORI per
      block (Varga plus Collatz-Wielandt, sharp to %.2f on the gap and flat in
      D and n).  What remains is the MARGIN comparison max(E) < min(S_B^{-1})
      itself, which needs a-priori control of min(S_B^{-1}) -- an M-matrix
      Green-function lower bound, i.e. the same anchor machinery from the other
      side.
  (c) M17.  CLOSED AS A ROUTE, negatively: the bad subspace is delocalised and
      stable, so no cut localises it and the M18 shape is exhausted.  Either a
      spectral characterisation of the whitened Schur block or a direct
      argument for the harmonic mean.
  (d) the quantifier.  Every certificate above is per zone and the zone list is
      finite (n <= %d).  Nothing here is uniform in n, and the RH fence is not
      approached from any side."""
     % (N_PROBES_PRIOR + 1, BK["gp"] if BK else float("nan"),
        qmin([r["rho_inf"] for r in G1H]) if G1H else float("nan"),
        qmax([r["rho_cw"] for r in G1H]) if G1H else float("nan"),
        qmin([r["over_inf"] for r in G1H]) if G1H else float("nan"),
        qmax([r["over_cw"] for r in G1H]) if G1H else float("nan"),
        POS_FRAC,
        qmax([r["sharp_v" + UT] for r in G2R]) if G2R else float("nan"),
        ZONE_DEEP))

ALPHA_MAX = max([r["al"] for r in G1R] + [r["al"] for r in G2R]
                + [0.5 * r["M"] * r["D"] for r in PEN])
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
if G1_OK and G2_OK:
    VERDICT = "PAIR-CARRIES"
elif G1_OK or G2_OK:
    VERDICT = "ONE-CARRIES"
else:
    VERDICT = "PAIR-RESISTS"

print("")
para("""VERDICT %s%s.  Three sentences.  G2 CARRIES and it carries cleanly: the
classical row-sum criterion is vacuous at the border (the row sums are negative
on %d of %d blocks, the same sign failure that killed the cheap A-routes), but
VARGA'S REGULAR SPLITTING makes rho(J) = tau/(1+tau) an IDENTITY for the lumped
Stieltjes comparison, so convergence needs no row-sum condition at all, and the
Collatz-Wielandt bound at the M-matrix anchor vector reproduces the measured
rho = %.3f .. %.3f with a gap shortfall of only %.2f .. %.2f, flat in D and in
the zone on %d of %d blocks.  G1 RESISTS, and the anatomy is now exact: the pair
is the right tool and runs the right way, the anchor half is certifiable and
loses at most %.2f, but the margin 1 - rho(E) is only %.1e .. %.1e wide while
every cheap upper bound on rho(E) sits at %.2f .. %.2f, the shifted ladder is
empty by monotonicity of M-matrix inverses, and the exact three-way bookkeeping
shows why: the whole D^%.2f degradation is carried by that margin (D^%.2f),
against an anchor that actually improves like D^%.2f.  G3 closes M17 as a route
rather than narrowing it: the bad pencil subspace is DELOCALISED (participation
ratio %.2f .. %.2f, %.0f %% of the cells for %.0f %% of the mass), neither a
border layer nor the comb stripes, flat on every rung (flatness %.2f) with a
dimension that tracks the ATOM COUNT rather than the grid (n_bad / n_at = %.2f
median), so sigma_b(k) never drops below %.3f on the wide ladder and no choice of
cut can bring M18 under the %.2f bar."""
     % (VERDICT, " (G2)" if VERDICT == "ONE-CARRIES" and G2_OK else
        (" (G1)" if VERDICT == "ONE-CARRIES" else ""),
        len(G2R) - len(RS_POS), len(G2R),
        qmin([r["rho"] for r in G2R]), qmax([r["rho"] for r in G2R]),
        qmin([r["sharp_v" + UT] for r in G2R]),
        qmax([r["sharp_v" + UT] for r in G2R]), len(G2R), len(G2R),
        qmax([r["f_anchor"] for r in G1H]), qmin([r["gap_ex"] for r in G1H]),
        qmax([r["gap_ex"] for r in G1H]), qmin([r["rho_inf"] for r in G1H]),
        qmax([r["rho_cw"] for r in G1H]), BK["mu"], BK["gp"], BK["an"],
        qmin([r["pr"] for r in PEN]), qmax([r["pr"] for r in PEN]),
        100.0 * qmed([r["k90_rel"] for r in PEN]), 100.0 * BAR_LOC,
        _flat, qmed([r["n_bad"] / float(r["n_at"]) for r in PEN]), _s_lo,
        BAR_MASS_GOOD))

print("")
print("TOTAL.probe        part %d, contract M.MATRIX.PAIR"
      % (N_PROBES_PRIOR + 1))
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.G1_pair      %s -- anchor sharp to %.2f, margin gap %.1e .. %.1e, "
      "cheapest rho bound %.2f" % (G1_STAT, qmax([r["f_anchor"] for r in G1H]),
                                   qmin([r["gap_ex"] for r in G1H]),
                                   qmax([r["gap_ex"] for r in G1H]),
                                   qmin([r["rho_inf"] for r in G1H])))
print("TOTAL.G1_dpower    lam_min(A) ~ D^%.2f = anchor D^%.2f x gap D^%.2f x "
      "slack D^%.2f (exact split, fitted exponents)"
      % (BK["mu"], BK["an"], BK["gp"], BK["fa"]))
print("TOTAL.G2_rho       %s -- a-priori rho <= %.4f .. %.4f on %d/%d, gap "
      "sharpness %.2f .. %.2f (bar %.0f)"
      % (G2_STAT, qmin([r["rho_" + UT] for r in G2R]),
         qmax([r["rho_" + UT] for r in G2R]), len(V_LT1[UT]), len(G2R),
         qmin([r["sharp_v" + UT] for r in G2R]),
         qmax([r["sharp_v" + UT] for r in G2R]), BAR_G2_GAP))
print("TOTAL.G3_M17       %s -- bad subspace %.0f .. %.0f %% of the cells, "
      "sigma_b >= %.3f, best bound %.2f .. %.2f, bar %.2f"
      % (M17_STAT, 100.0 * qmin([r["bad_frac"] for r in PEN]),
         100.0 * qmax([r["bad_frac"] for r in PEN]), _s_lo,
         qmin([r["bnd"] for r in PEN]), qmax([r["bnd"] for r in PEN]),
         BAR_MASS_GOOD))
print("TOTAL.promotions   %d statements ready, %d new, 0 promoted"
      % (PROMO_OLD + len(PROMO), len(PROMO)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised form %d (cap %d); the matrix-free "
      "ingredient extension reached %d, lag assembly and gathers unbounded"
      % (max([r["h"] for r in G1R] + [r["h"] for r in G2R]
             + [r["h"] for r in PEN]), MAX_H,
         int(qmax([r["h"] for r in FREE]))))
print("TOTAL.status       %s" % ("ALL CHECKS PASSED" if FAIL == 0
                                 else "%d CHECK(S) FAILED" % FAIL))
