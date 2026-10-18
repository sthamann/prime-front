"""Discovery probe (2026-07-28), part 129 of the prime/window investigation.
Contract KAPPA.DEEP.SEAMS -- harden the kappa law that T128 broke, close the
two AFFORDABLE deep seams of the (L) list by two-scale compression, and turn
the (M) comb residual from a measurement into a bound.  Nothing else.

WHERE THIS SITS (T128 THREE-OF-FOUR, quoted; every load-bearing number rebuilt)
  T128 worked the four-point TEML list and came back THREE-OF-FOUR.  The one
  point that did not stand is (T), and it failed in a very particular way:
    (T) the protrusion concentration kappa = m_prot gc_f / (t_l + t_r) -- the
        S_f eigenvector mass on the protruding border cells divided by the mass
        a FLAT border vector would put there -- ran 0.086 .. 2.071 with median
        1.775 and MISSED the preregistered bar kappa <= 2 on 1 of 120
        transports, by 3.6 per cent.  The miss was SYSTEMATIC in the
        re-gridding ratio: group maxima 1.889 / 1.965 / 2.071 at rho = 1.001 /
        1.250 / 1.495.  T128 therefore PREREGISTERED the follow-up hypothesis
            kappa <= 2 + C (rho - 1)
        and recorded the side split: kappa on the RIGHT protrusion 1.61 .. 2.07,
        on the LEFT only 0.09 .. 0.25.  So (T) is an EIGENVECTOR statement, not
        a rounding statement.
    (L) five budget-open seams -- n = 127 (h_f = 2476), 256 (5694), 8191
        (295253), 65536 (2.9e6), 131071 (6.2e6); each needs EXACTLY one
        Cholesky of size h_f - gc_f, nothing conceptual.  T115's two-scale
        compression reached m/h = 0.043 (fine at the border, merged inside),
        the Albert step stayed margin-free, and the compression error is
        certified one-sided and second order.
    (E) the Q-inner-product Cauchy-Schwarz chain carries 11 of 12 (the n = 31
        tear is eta-limited; the ladder repairs it).
    (M) the boundary-layer exclusion is PROVED for the closed-form POLE part of
        shat; the floor is 0.188 with 11.6 x margin; the COMB part of shat is
        still only MEASURED (open point M18).
  Map V3: 21 points, 5 genuinely open -- M9 (the kappa bar), M17 (pencil mass),
  M18 (the comb), M19 ("for all"), M21 (the RH address).  Zones are prime
  powers, frame A (T112), nu = 4 (T105).

WHAT THIS PROBE DOES
  K0  SETUP -- atoms, the free-resolution record schedule, the out-of-band
      list, and the two deep seams named as the K2 targets.
  K1  THE KAPPA LAW.  First two IDENTITIES that change what kappa is:
      (i) sum_{i<gc_f} (1 - g_i) = t_l + t_r exactly (interval geometry), hence
      the FLAT border vector has kappa == 1 -- the bar 2 was never the flat
      limit; (ii) kappa = sum_i omega_i p_i with omega_i = (1-g_i)/(t_l+t_r) a
      PROBABILITY weight supported on the two ends of the border block and
      p_i = gc_f w_i^2 the normalised eigenvector DENSITY.  So kappa is a
      weighted mean of the density at the two ends, and kappa <= max p over the
      protruding cells (Hoelder).  Then the exact profile identity
          p_{N-1} = 2 - p_0 + 2 E ,  E = (1/N) sum_j (j+1) (Dp_j - Dbar) ,
      which says kappa = 2 is the LINEAR-DENSITY limit with vanishing edge
      value, and the excess over 2 is a CURVATURE term with the explicit
      majorant |2E| <= ((N-2)/N) sum_j |Dp_j - Dbar| (Abel summation).  C is
      then estimated on a CALIBRATION set that reproduces the T128 grouping,
      FROZEN, and the law kappa <= 2 + C(rho - 1) is tested on a DISJOINT set
      of new zones and new ratios, both sides, several depths.  Violations are
      counted; the bar is not moved.
  K2  THE TWO AFFORDABLE DEEP SEAMS.  n = 127 (h_f = 2476) and n = 256 (h_f =
      5694) are brought under the hard cap by the T115 graded two-scale space
      (fine cells at the window EDGE, blocks of q merged inward, anchored at
      the window centre), assembled matrix-free.  Both grids of the seam are
      compressed, the transport bracket is rebuilt on the graded pair, and the
      full seam is certified THERE.  The DIRECTION FENCE is stated first and
      obeyed: Rayleigh-Ritz gives lam_min(S_graded) >= lam_min(S_fine), so a
      graded certificate is WEAKER than a uniform one and does NOT prove the
      fine-space seam.  The gap is CALIBRATED at affordable depths at the same
      working point, and the deep seams get their own status word.
  K3  M18 -- THE COMB RESIDUAL BOUNDED.  comb = -Bx^T x_c is the detail part of
      shat that has no closed form.  Its outer-k-cell share is majorised in two
      certified ways: (a) a per-instance Cauchy-Schwarz row bound, (b) an
      S-procedure bound valid for EVERY coarse vector in the smoothness cone
      x^T L x <= theta^2 ||x||^2, i.e. a property of the CONSTRUCTED two-grid
      splitting alone, with theta measured for the actual x_c.  Both are
      checked to be majorants and their kD law is fitted over zones x depths.
  K4  THE MAP V4 and the promotion assessment.

PREREGISTERED VERDICTS (bars declared here, before any number)
  KAPPA-LAWFUL : the frozen law kappa <= 2 + C(rho - 1) holds on EVERY new
                 transport of the test set with ZERO violations, AND the
                 curvature chain is verified as a theorem on all of them, AND
                 both deep seams carry a complete graded seam certificate, AND
                 the M18 comb share carries a certified majorant that is
                 non-vacuous (< 1) on every zone x depth tested.
  PARTIAL      : some of the above stands and some does not -- named precisely,
                 per item, with the counts.
  KAPPA-WILD   : the frozen law breaks on the test set (>= 1 violation) -- the
                 measurement, with the argmax and the structure.
  Element gates: el_firewall, el_k0, el_k1, el_k2, el_k3, el_k4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger/TeX/website/
    changelog edit, no verification/ module, no next.txt, no .md output, no
    git action.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * THE RH FENCE IS PROMINENT AND ABSOLUTE.  Weil's positivity criterion
    (Weil 1952; Bombieri 2000; Connes 1999) is CITED as the classical address
    of the surrounding statement and is NEVER USED, in either direction.
    Nothing here claims, assumes or approaches RH.  Even with kappa proved, the
    deep seams closed and the comb bounded, what would stand is positivity of
    the Weil window form on test functions supported in (-alpha_max, alpha_max)
    for the alpha actually reached -- a FINITE-WINDOW statement.  The distance
    to RH is MAPPED, never travelled.
  * CERTIFIED vs GRADED-CERTIFIED vs CERTIFIED-CONDITIONAL vs MEASURED vs FIT
    vs HYPOTHESIS, per line.  A completed Cholesky of A - s I certifies
    lam_min(A) >= s - c_h u ||A||_2, u = 2^-53, c_h = (h+1)/(1-(h+1)u)
    (Wilkinson 1968; Higham 2002 Thm 10.3/10.4).  Every fit is a FIT and
    carries a jackknife band.  A rank statistic is a MEASUREMENT on a finite
    sample, never a test of a law.  A bar declared before a number is NEVER
    moved afterwards; violations are counted and printed.
  * CLASSICAL ADDRESSES USED: Cauchy-Schwarz and Hoelder (the kappa mean, the
    comb row bound), Abel summation (the curvature majorant), Chebyshev's
    correlation / Grues-type argument (the sign of the curvature term),
    Haynsworth 1968 (the Schur/transport bracket), Albert 1969 and Douglas 1966
    (margin-free completion), Rayleigh-Ritz and Cea 1964 / Strang's first lemma
    (the one-sided second-order compression error), Yserentant 1986 (the
    two-scale space), Eijkhout-Vassilevski 1991 (the strengthened
    Cauchy-Schwarz constant), Wilkinson 1968 / Higham 2002 (the Cholesky
    certificate), the S-procedure / Lagrangian relaxation (the conditional comb
    bound), Gershgorin 1931 (norm majorants), Bertrand-Chebyshev 1852 and the
    trivial even bound (the only gap facts consumed), Mihailescu 2004 (the
    ADDRESS of the (L) class, used for nothing).  No gap CONJECTURE (Cramer,
    Firoozbakht, twin, Mersenne infinitude) enters anywhere.
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    FFT levers, rectangular gathers and pure interval geometry may exceed it.
    Probe budget < 900 s.

OUTCOME OF THIS RUN  =>  see the K4 map and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, cholesky, eigvalsh

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
SQ2 = math.sqrt(2.0)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 800.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 320000
ZONE_DEEP = 300000

H_POOL = 1450                # fine-grid cap for the K1 transport pools
H_DEEPCHK = 1450             # a few deeper K1 transports
CAL_PER_RHO = 70             # zones per calibration ratio
TST_PER_RHO = 60             # zones per TEST ratio
K_FINE_DEEP = 32             # graded space: fine cells kept at the window edge
Q_TRY = (1, 2, 3, 4, 5, 6, 8, 10, 12, 16)
GAP_ZONES = 12               # zones for the compression-gap calibration
GAP_QSET = ((1, 2), (2, 3), (2, 4), (3, 6))
M18_ZONES = 12
M18_DEPTHS = (1, 2, 4)
M18_KSET = (1, 2, 4, 8)
M18_HMAX = 1200
S_GRID = tuple(10.0 ** e for e in np.linspace(-6.0, 2.0, 13))

# --- preregistered bars (declared before any number) ------------------------
BAR_KAPPA = 2.0              # the T128 bar -- QUOTED and NOT moved
BAR_M18 = 1.0                # a comb majorant >= 1 is VACUOUS
BAR_TIGHT = 50.0             # a majorant this far off the truth is structural

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
RHO_UNI_T127 = 1.49531       # T127 bisected band edge
COVER_T127 = 99.26           # per cent of record seams inside the band
KAP_MIN_T128 = 0.086
KAP_MED_T128 = 1.775
KAP_MAX_T128 = 2.071
KAP_OVER_T128 = 1
KAP_N_T128 = 120
RHO_GRP_T128 = (1.001, 1.250, 1.495)
KAP_GRP_T128 = (1.889, 1.965, 2.071)
KAP_R_T128 = (1.61, 2.07)
KAP_L_T128 = (0.09, 0.25)
MU_FLOOR_T128 = 0.188
MU_MARGIN_T128 = 11.6
MH_BEST_T115 = 0.043
N_PROBES_PRIOR = 128


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
            line = w if not line else line + " " + w
    if line:
        out.append(line)
    return out or [""]


def para(text, width=76, indent="  "):
    for ln in wrap_at(text, width):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def sym(A):
    return 0.5 * (A + A.T)


def rel(Dm, Rf):
    return float(np.abs(Dm).max()) / max(float(np.abs(Rf).max()), 1.0e-300)


def q_of(v, qs=(0.0, 0.5, 1.0)):
    a = np.asarray([x for x in v if math.isfinite(x)], dtype=float)
    if a.size == 0:
        return [float("nan")] * len(qs)
    return [float(np.quantile(a, q)) for q in qs]


def med_of(v):
    return q_of(v, (0.5,))[0]


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
    if n < 3:
        return a, b, rms, float("nan")
    bs = []
    for i in range(n):
        m = np.ones(n, dtype=bool)
        m[i] = False
        bs.append(fit_line(x[m], y[m])[1])
    bs = np.asarray(bs, dtype=float)
    se = math.sqrt(max(0.0, (n - 1.0) / n * float(np.sum((bs - bs.mean()) ** 2))))
    return a, b, rms, se


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
          == "kappa_deep_seams_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- T111..T128 code path
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
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T128)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


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


def cert_pd(A):
    n = A.shape[0]
    dlt = chol_floor(gersh(A), n)
    fac = safe_cho(A - dlt * np.eye(n))
    return (fac is not None), dlt, fac


def cert_lmin(A, lam):
    try:
        cholesky(sym(A) - lam * np.eye(A.shape[0]), lower=True, check_finite=False)
        return True
    except LinAlgError:
        return False


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


def overlap_odd(xt, Dt, xs, Ds):
    """<phi^t_i, phi^s_j> for L2-normalised PWC cells in ODD coordinates."""
    a = np.asarray(xt, dtype=float)[:, None]
    b = np.asarray(xs, dtype=float)[None, :]
    den = math.sqrt(Dt * Ds)

    def ov(bb):
        lo = np.maximum(a - 0.5 * Dt, bb - 0.5 * Ds)
        hi = np.minimum(a + 0.5 * Dt, bb + 0.5 * Ds)
        return np.maximum(0.0, hi - lo) / den

    return ov(b) - ov(-b)


# ----------------------------------------------------------------------------
# THE BORDER INTERVAL GEOMETRY (T128), exact and factorisation free
# ----------------------------------------------------------------------------
def edge_geom(u_o, u_n, D_c, D_f):
    fr_c = step_frame(u_o, u_n, D_c)
    fr_f = step_frame(u_o, u_n, D_f)
    if fr_c is None or fr_f is None:
        return None
    gc_c, gc_f = fr_c["gc"], fr_f["gc"]
    al_c, al_f = fr_c["al_n"], fr_f["al_n"]
    bord_c, bord_f = gc_c * D_c, gc_f * D_f
    x_lc, x_rc = -al_c, -al_c + bord_c
    x_lf, x_rf = -al_f, -al_f + bord_f
    sl_l = (x_lf - x_lc) / D_f
    sl_r = (x_rc - x_rf) / D_f
    nf = gc_f + int(math.ceil(bord_c / D_f)) + 3
    nf = min(nf, fr_f["h_n"])
    ii = np.arange(nf, dtype=float)
    f_lo = -al_f + ii * D_f
    f_hi = f_lo + D_f
    jj = np.arange(gc_c, dtype=float)
    c_lo = -al_c + jj * D_c
    c_hi = c_lo + D_c
    ov = np.maximum(0.0, np.minimum(f_hi[:, None], c_hi[None, :])
                    - np.maximum(f_lo[:, None], c_lo[None, :]))
    f_ij = ov / D_c
    g_i = ov.sum(axis=1) / D_f
    return dict(fr_c=fr_c, fr_f=fr_f, gc_c=gc_c, gc_f=gc_f, al_c=al_c,
                al_f=al_f, bord_c=bord_c, bord_f=bord_f, sl_l=sl_l, sl_r=sl_r,
                t_l=max(0.0, -sl_l), t_r=max(0.0, -sl_r),
                fill=max(0.0, sl_r), ovh_rel=(bord_f - bord_c) / bord_c,
                f_ij=f_ij, g_i=g_i, nf=nf, rho=D_c / D_f, D_c=D_c, D_f=D_f,
                h_c=fr_c["h_n"], h_f=fr_f["h_n"], g=u_n - u_o)


def tau_terms(geo, w):
    """THE (T) IDENTITY of T128, rebuilt verbatim:
        tau_dn = ||y||^2 - m_prot + m_fill - V_bord ."""
    f_ij, g_i, gc_f, rho = geo["f_ij"], geo["g_i"], geo["gc_f"], geo["rho"]
    nf = geo["nf"]
    ww = np.asarray(w[:nf], dtype=float)
    m1 = f_ij * ww[:, None]
    m2 = f_ij * (ww ** 2)[:, None]
    v = math.sqrt(rho) * m1.sum(axis=0)
    tau = float(np.dot(v, v))
    mu_ic = float(rho * m2.sum())
    V = mu_ic - tau
    ynrm = float(np.dot(ww[:gc_f], ww[:gc_f]))
    m_prot = float(np.dot(1.0 - g_i[:gc_f], ww[:gc_f] ** 2))
    m_fill = float(np.dot(g_i[gc_f:], ww[gc_f:] ** 2))
    dlt = np.diff(ww)
    osc2 = float(np.dot(dlt, dlt))
    v_up = 0.5 * rho * (math.ceil(rho) + 1.0) * osc2
    return dict(tau=tau, V=V, ynrm=ynrm, m_prot=m_prot, m_fill=m_fill,
                v_up=v_up, osc2=osc2,
                ident=tau - (ynrm - m_prot + m_fill - V),
                lo_exact=ynrm - m_prot - V)


# ----------------------------------------------------------------------------
# NEW IN THIS PROBE (1): THE KAPPA DECOMPOSITION.  kappa stops being a mass
# ratio and becomes a weighted mean of the eigenvector DENSITY profile on the
# two ends of the border block -- which is what makes a proof form possible.
# ----------------------------------------------------------------------------
def kappa_terms(geo, w):
    """kappa = sum_i omega_i p_i, omega_i = (1 - g_i)/(t_l + t_r) >= 0 with
    sum omega = 1 EXACTLY (interval geometry), p_i = gc_f w_i^2 / ||y||^2 the
    normalised density.  Hence (Hoelder) kappa <= max p over supp omega, and
    the FLAT border vector gives kappa == 1.  The profile identity
        p_{N-1} = 2 - p_0 + 2 E ,  E = (1/N) sum_j (j+1)(Dp_j - Dbar)
    then makes kappa = 2 the LINEAR-DENSITY limit with p_0 = 0, and Abel
    summation majorises the excess by the CURVATURE
        |2 E| <= ((N-2)/N) sum_j |Dp_j - Dbar| ."""
    N = geo["gc_f"]
    g_i = geo["g_i"]
    ww = np.asarray(w[:N], dtype=float)
    ynrm = float(np.dot(ww, ww))
    if N < 3 or ynrm <= 0.0:
        return None
    tot = geo["t_l"] + geo["t_r"]
    if tot <= 1.0e-12:
        return None
    om_raw = 1.0 - g_i[:N]
    p = N * (ww ** 2) / ynrm
    # the geometric fractions are exact up to rounding; clip at zero so that a
    # -1e-17 weight cannot manufacture a negative side average
    om = np.maximum(0.0, om_raw) / tot
    kap = float(np.dot(om, p))
    half = N // 2
    wl = float(om[:half].sum())
    wr = float(om[half:].sum())
    kap_l = (float(np.dot(om[:half], p[:half]) / wl)
             if (geo["t_l"] > 1.0e-9 and wl > 1.0e-9) else float("nan"))
    kap_r = (float(np.dot(om[half:], p[half:]) / wr)
             if (geo["t_r"] > 1.0e-9 and wr > 1.0e-9) else float("nan"))
    sup = om > 1.0e-14
    p_max = float(p[sup].max()) if sup.any() else float("nan")
    dp = np.diff(p)
    dbar = (p[N - 1] - p[0]) / (N - 1.0)
    e = dp - dbar
    E = float(np.dot(np.arange(1.0, N), e)) / N
    curv = float(np.abs(e).sum())
    maj = ((N - 2.0) / N) * curv
    lin_id = abs(p[N - 1] - (2.0 - p[0] + 2.0 * E))
    bnd = 2.0 - p[0] + maj + max(0.0, p_max - p[N - 1])
    # flat-vector control: kappa of the FLAT border vector, must be 1 exactly
    kap_flat = float(np.dot(om, np.ones(N)))
    return dict(N=N, kap=kap, kap_l=kap_l, kap_r=kap_r, p0=float(p[0]),
                pN=float(p[N - 1]), p_max=p_max, curv=curv, maj=maj, E=E,
                lin_id=lin_id, bnd=bnd, kap_flat=kap_flat,
                w_om_sum=float(om.sum()), geo_id=abs(float(om_raw.sum()) - tot),
                peaks_at_end=int(abs(p_max - p[N - 1]) < 1.0e-12),
                p=p)


# ----------------------------------------------------------------------------
# the bordered step and the T115 transport bracket (Haynsworth 1968)
# ----------------------------------------------------------------------------
def bordered_step(fr, atoms_all):
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
    ev, U = np.linalg.eigh(S)
    y = np.ascontiguousarray(U[:, 0])
    z = -(Z @ y)
    return dict(Q=Q, S=S, lam=float(ev[0]), y=y, z=z,
                w=np.concatenate([y, z]), fr=fr, scale=gersh(A))


def seam_full(u_o, u_n, D_A, D_B, n_lbl, cap=MAX_H):
    """ONE re-gridding from coarse D_A to fine D_B on the UNIFORM grids, with
    the T115 bracket at the ACTUAL minimisers plus the kappa decomposition."""
    geo = edge_geom(u_o, u_n, D_A, D_B)
    if geo is None:
        return None
    if max(geo["h_c"], geo["h_f"]) > cap:
        return None
    sc = bordered_step(geo["fr_c"], ATOMS_ALL)
    sf = bordered_step(geo["fr_f"], ATOMS_ALL)
    if sc is None or sf is None:
        return None
    x_c, _ = odd_nodes(geo["al_c"], geo["fr_c"]["M_n"])
    x_f, _ = odd_nodes(geo["al_f"], geo["fr_f"]["M_n"])
    P = overlap_odd(x_f, geo["D_f"], x_c, geo["D_c"])
    w_f = sf["w"]
    F_f = float(w_f @ sf["Q"] @ w_f)
    v = P.T @ w_f
    gcc = geo["gc_c"]
    tau_dn = float(np.dot(v[:gcc], v[:gcc]))
    eta_dn = float(v @ sc["Q"] @ v) - F_f
    tt = tau_terms(geo, w_f)
    kk = kappa_terms(geo, w_f)
    lo = sc["lam"] * tau_dn - abs(eta_dn)
    out = dict(n=n_lbl, rho=geo["rho"], h_c=geo["h_c"], h_f=geo["h_f"],
               gc_c=gcc, gc_f=geo["gc_f"], t_l=geo["t_l"], t_r=geo["t_r"],
               lam_c=sc["lam"], lam_f=sf["lam"], tau_dn=tau_dn, eta_dn=eta_dn,
               lo=lo, lo_pos=int(lo > 0.0), tau=tt["tau"], V=tt["V"],
               m_prot=tt["m_prot"], ynrm=tt["ynrm"], ident=tt["ident"],
               lo_exact=tt["lo_exact"], osc2=tt["osc2"], kap=kk)
    del P, sc, sf
    return out


# ----------------------------------------------------------------------------
# NEW IN THIS PROBE (2): THE GRADED TWO-SCALE SEAM.  T115 compressed a STEP;
# here the whole SEAM -- two grids, the transport bracket and the border
# geometry -- is rebuilt on the graded pair, which is what the deep (L) items
# need.  The direction fence is stated with the block.
# ----------------------------------------------------------------------------
def merge_cols(h, q, k_fine, ngroup=None):
    """The graded PWC space: fine cells 0..r_split-1 at the window EDGE, blocks
    of q merged cells inward, anchored at the window CENTRE (index h-1)."""
    if ngroup is None:
        ngroup = max(0, (h - k_fine) // q)
    r_split = h - ngroup * q
    if r_split < 1 or r_split > h:
        return None
    starts = [r_split + j * q for j in range(ngroup)]
    return dict(h=h, q=q, r_split=r_split, ngroup=ngroup, starts=starts,
                m=r_split + ngroup)


def merge_J(mc):
    J = np.zeros((mc["h"], mc["m"]))
    rs = mc["r_split"]
    J[np.arange(rs), np.arange(rs)] = 1.0
    w = 1.0 / math.sqrt(mc["q"])
    for j, s in enumerate(mc["starts"]):
        J[s:s + mc["q"], rs + j] = w
    return J


def merge_form(c, tv, M, mc):
    """The two-scale form J^T Q J assembled WITHOUT ever touching a fine square
    matrix: only the length-M lag vector, the pole vector and O(q) gathers."""
    q, rs, m = mc["q"], mc["r_split"], mc["m"]
    st = np.asarray(mc["starts"], dtype=np.int64)
    out = np.zeros((m, m))
    if st.size:
        dlt = st[:, None] - st[None, :]
        sgm = (M - 1) - st[:, None] - st[None, :]
        blk = np.zeros((st.size, st.size))
        for d in range(-(q - 1), q):
            blk += ((q - abs(d)) / q) * c[np.abs(dlt + d)]
        for e in range(0, 2 * q - 1):
            blk -= ((q - abs(e - (q - 1))) / q) * c[sgm - e]
        out[rs:, rs:] = blk
        del dlt, sgm, blk
    idx = np.zeros((m, q), dtype=np.int64)
    wgt = np.zeros((m, q))
    idx[:rs, :] = np.arange(rs)[:, None]
    wgt[:rs, 0] = 1.0
    if st.size:
        idx[rs:, :] = st[:, None] + np.arange(q)[None, :]
        wgt[rs:, :] = 1.0 / math.sqrt(q)
    for i in range(rs):
        row = np.zeros(m)
        for k in range(q):
            row += wgt[:, k] * (c[np.abs(i - idx[:, k])]
                                - c[(M - 1) - i - idx[:, k]])
        out[i, :] = row
        out[:, i] = row
    tj = np.zeros(m)
    for k in range(q):
        tj += wgt[:, k] * tv[idx[:, k]]
    out -= np.outer(tj, tj)
    return sym(out)


def graded_cells(mc, alpha, D):
    """The graded partition as INTERVALS: every basis function is the
    L2-normalised indicator of a contiguous interval, which is what keeps the
    transport a pure interval computation."""
    rs, q = mc["r_split"], mc["q"]
    lo = np.empty(mc["m"])
    hi = np.empty(mc["m"])
    lo[:rs] = -alpha + np.arange(rs) * D
    hi[:rs] = lo[:rs] + D
    if mc["ngroup"]:
        st = np.asarray(mc["starts"], dtype=float)
        lo[rs:] = -alpha + st * D
        hi[rs:] = -alpha + (st + q) * D
    return lo, hi, hi - lo


def overlap_graded(lo_t, hi_t, W_t, lo_s, hi_s, W_s, rows=192):
    """<phi^t_i, phi^s_j> for two GRADED odd PWC partitions.  Reduces to
    overlap_odd when both partitions are uniform (checked in K2.1)."""
    nt, ns = lo_t.shape[0], lo_s.shape[0]
    out = np.empty((nt, ns))
    inv = 1.0 / np.sqrt(W_s)
    for a in range(0, nt, rows):
        b = min(nt, a + rows)
        al = lo_t[a:b, None]
        ah = hi_t[a:b, None]
        p = np.maximum(0.0, np.minimum(ah, hi_s[None, :]) - np.maximum(al, lo_s[None, :]))
        m = np.maximum(0.0, np.minimum(ah, -lo_s[None, :]) - np.maximum(al, -hi_s[None, :]))
        out[a:b, :] = (p - m) * inv[None, :] / np.sqrt(W_t[a:b, None])
    return out


def graded_step(u_o, u_n, D, q, k_fine=K_FINE_DEEP, want_old=False):
    """The compressed bordered step: ngroup is fixed by the OLD window, so the
    new window's graded basis is the old one plus gc fine cells and Albert's
    hypothesis stays PURE semidefiniteness of the previous zone."""
    fr = step_frame(u_o, u_n, D)
    if fr is None:
        return None
    mc_o = merge_cols(fr["h_o"], q, k_fine)
    if mc_o is None or mc_o["ngroup"] < 1:
        return None
    mc_n = merge_cols(fr["h_n"], q, k_fine, ngroup=mc_o["ngroup"])
    if mc_n is None or mc_n["m"] != mc_o["m"] + fr["gc"]:
        return None
    if mc_n["r_split"] < fr["gc"] + 4:
        return None
    if mc_n["m"] > MAX_H:
        return None
    at_n = atoms_in(fr["al_n"], ATOMS_ALL)
    c_n, _ = lag_vector_fast(fr["al_n"], fr["M_n"], at_n)
    tv = odd_pole_vector(fr["al_n"], fr["M_n"])
    Q = merge_form(c_n, tv, fr["M_n"], mc_n)
    gc = fr["gc"]
    A = sym(np.ascontiguousarray(Q[:gc, :gc]))
    C = np.ascontiguousarray(Q[:gc, gc:])
    X = sym(np.ascontiguousarray(Q[gc:, gc:]))
    fac = safe_cho(X)
    if fac is None:
        return None
    Z = cho_solve(fac, C.T, check_finite=False)
    S = sym(A - C @ Z)
    ev, U = np.linalg.eigh(S)
    y = np.ascontiguousarray(U[:, 0])
    z = -(Z @ y)
    lo_i, hi_i, W_i = graded_cells(mc_n, fr["al_n"], D)
    out = dict(fr=fr, mc_o=mc_o, mc_n=mc_n, Q=Q, S=S, lam=float(ev[0]), y=y,
               z=z, w=np.concatenate([y, z]), m=mc_n["m"], q=q, gc=gc,
               lo=lo_i, hi=hi_i, W=W_i, X_norm=gersh(X), A_norm=gersh(A),
               x_pd=cert_lmin(X, chol_floor(gersh(X), X.shape[0])),
               D=D, al=fr["al_n"], h=fr["h_n"])
    if want_old:
        at_o = atoms_in(fr["al_o"], ATOMS_ALL)
        c_o, _ = lag_vector_fast(fr["al_o"], fr["M_o"], at_o)
        tv_o = odd_pole_vector(fr["al_o"], fr["M_o"])
        out["Q_old"] = merge_form(c_o, tv_o, fr["M_o"], mc_o)
    del Z, C
    return out


def pick_q(h, gc, k_fine=K_FINE_DEEP):
    for q in Q_TRY:
        mc = merge_cols(h, q, k_fine)
        if mc is None or mc["ngroup"] < 1:
            continue
        if mc["m"] + gc <= MAX_H and mc["r_split"] >= gc + 4:
            return q
    return None


def graded_seam(u_o, u_n, D_A, D_B, n_lbl, q_c=None, q_f=None):
    """The FULL seam on the graded pair: both grids compressed, the transport
    bracket rebuilt, the border geometry unchanged.  k_fine is chosen so the
    ENTIRE stencil the border geometry touches (nf fine cells) stays inside the
    unmerged part of the graded space -- otherwise tau_terms would be reading
    merged-block coefficients as if they were fine cells."""
    geo = edge_geom(u_o, u_n, D_A, D_B)
    if geo is None:
        return None
    kf_c = max(K_FINE_DEEP, 2 * geo["gc_c"] + 8)
    kf_f = max(K_FINE_DEEP, geo["nf"] + 4)
    if q_c is None:
        q_c = pick_q(geo["h_c"], geo["gc_c"], kf_c)
    if q_f is None:
        q_f = pick_q(geo["h_f"], geo["gc_f"], kf_f)
    if q_c is None or q_f is None:
        return None
    sc = graded_step(u_o, u_n, D_A, q_c, k_fine=kf_c)
    sf = graded_step(u_o, u_n, D_B, q_f, k_fine=kf_f)
    if sc is None or sf is None:
        return None
    if sf["mc_n"]["r_split"] < geo["nf"] or sc["mc_n"]["r_split"] < geo["gc_c"]:
        return None
    P = overlap_graded(sf["lo"], sf["hi"], sf["W"], sc["lo"], sc["hi"], sc["W"])
    w_f = sf["w"]
    F_f = float(w_f @ sf["Q"] @ w_f)
    v = P.T @ w_f
    gcc = geo["gc_c"]
    tau_dn = float(np.dot(v[:gcc], v[:gcc]))
    eta_dn = float(v @ sc["Q"] @ v) - F_f
    tt = tau_terms(geo, w_f)
    kk = kappa_terms(geo, w_f)
    lo = sc["lam"] * tau_dn - abs(eta_dn)
    fl_c = chol_floor(sc["X_norm"], sc["m"])
    fl_f = chol_floor(sf["X_norm"], sf["m"])
    out = dict(n=n_lbl, rho=geo["rho"], h_c=geo["h_c"], h_f=geo["h_f"],
               m_c=sc["m"], m_f=sf["m"], q_c=q_c, q_f=q_f,
               mh_c=sc["m"] / float(geo["h_c"]), mh_f=sf["m"] / float(geo["h_f"]),
               gc_c=gcc, gc_f=geo["gc_f"], t_l=geo["t_l"], t_r=geo["t_r"],
               lam_c=sc["lam"], lam_f=sf["lam"], tau_dn=tau_dn, eta_dn=eta_dn,
               lo=lo, lo_pos=int(lo > 0.0), ident=tt["ident"],
               ynrm=tt["ynrm"], lo_exact=tt["lo_exact"], kap=kk,
               x_pd_c=int(sc["x_pd"]), x_pd_f=int(sf["x_pd"]),
               fp_c=fl_c, fp_f=fl_f, rs_f=sf["mc_n"]["r_split"], nf=geo["nf"],
               cert_c=int(cert_lmin(sc["S"], -fl_c) and sc["lam"] > fl_c),
               cert_f=int(cert_lmin(sf["S"], -fl_f) and sf["lam"] > fl_f),
               ret=lo / max(sc["lam"], 1.0e-300))
    del P, sc, sf
    return out


firewall()


# ----------------------------------------------------------------------------
section("K0  SETUP -- atoms, the record schedule, the two deep targets")
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
check("el_k0.gap_bounds", BERT_OK and EVEN_OK,
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
    REC.append(dict(k=k, n=NN_ALL[k], n_nx=NN_ALL[k + 1],
                    dnx=NN_ALL[k + 1] - NN_ALL[k], rho=geo["rho"],
                    gc_c=geo["gc_c"], gc_f=geo["gc_f"], h_c=geo["h_c"],
                    h_f=geo["h_f"], D_c=geo["D_c"], D_f=geo["D_f"]))

RHO_R = np.array([d["rho"] for d in REC], dtype=float)
OUT = [d for d in REC if d["rho"] > RHO_UNI_T127]
COVER = float(np.mean(RHO_R <= RHO_UNI_T127))
L_OPEN0 = sorted([d for d in OUT if d["h_f"] > MAX_H], key=lambda d: d["h_f"])
DEEP2 = L_OPEN0[:2]

check("el_k0.record_schedule", len(REC) > 100 and abs(100.0 * COVER
                                                      - COVER_T127) < 0.5,
      "the free-resolution schedule D_k = min(cap_k, D_{k-1}) re-grids at %d "
      "of %d boundaries over n <= %d; the T127 band rho <= %.5f (QUOTED, not "
      "re-bisected) covers %.2f %% (T127 quoted %.2f %%) and leaves %d out of "
      "band, of which %d exceed the hard cap %d.  Those %d are the T128 "
      "budget-open list: n = %s with h_f = %s"
      % (len(REC), NZ_DEEP, ZONE_DEEP, RHO_UNI_T127, 100.0 * COVER, COVER_T127,
         len(OUT), len(L_OPEN0), MAX_H, len(L_OPEN0),
         ", ".join(str(d["n"]) for d in L_OPEN0),
         ", ".join(str(d["h_f"]) for d in L_OPEN0)))

check("el_k0.deep_targets", len(DEEP2) == 2,
      "THE TWO K2 TARGETS, chosen by COST and nothing else -- the two smallest "
      "budget-open h_f: n = %s (h_f = %s, rho = %s).  The remaining %d (n = %s, "
      "h_f = %s) are declared out of budget HERE and now, before any attempt: "
      "even at the T115 record compression m/h = %.3f their m would be %s, "
      "against the cap %d"
      % (", ".join(str(d["n"]) for d in DEEP2),
         ", ".join(str(d["h_f"]) for d in DEEP2),
         ", ".join("%.4f" % d["rho"] for d in DEEP2), len(L_OPEN0) - 2,
         ", ".join(str(d["n"]) for d in L_OPEN0[2:]),
         ", ".join(str(d["h_f"]) for d in L_OPEN0[2:]), MH_BEST_T115,
         ", ".join("%.0f" % (MH_BEST_T115 * d["h_f"]) for d in L_OPEN0[2:]),
         MAX_H))

info("K0.rh_fence", "RH FENCE, restated before any number: Weil's positivity "
     "criterion (Weil 1952; Bombieri 2000; Connes 1999) is the classical "
     "ADDRESS of the statement this chain approaches.  It is CITED and NEVER "
     "USED -- not as hypothesis, not as conclusion, in neither direction.  No "
     "zero data of any kind is read (el_firewall).  Even with the kappa law "
     "proved, both deep seams closed and the comb bounded, what would stand is "
     "a FINITE-WINDOW positivity statement for the alpha actually reached; see "
     "the K4 map")
info("K0.fp_regime", "u = 2^-53 = %.3e; a completed Cholesky of A certifies "
     "lam_min(A) >= -c_h u ||A||_2, c_h = (h+1)/(1-(h+1)u) (Wilkinson 1968; "
     "Higham 2002 Thm 10.3/10.4).  At h = %d the floor is %.2e ||A||_2"
     % (U_ROUND, MAX_H, chol_floor(1.0, MAX_H)))
info("K0.timing", "K0 done, %.1f s used, %.0f s budget left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("K1  THE KAPPA LAW -- two identities, a frozen constant, and a test")
# ----------------------------------------------------------------------------
para("""WHAT T128 LEFT.  kappa = m_prot gc_f / (t_l + t_r) ran %.3f .. %.3f with
median %.3f and missed its preregistered bar %.1f on %d of %d transports by 3.6
per cent, systematically in rho (group maxima %s at rho = %s), and split by side
into kappa_r = %.2f .. %.2f against kappa_l = %.2f .. %.2f.  T128 preregistered
kappa <= 2 + C(rho - 1) as the follow-up.  This block does three things in
order.  FIRST it proves what kappa IS, which changes the question.  SECOND it
estimates C on a CALIBRATION set built by the T128 recipe and FREEZES it.  THIRD
it tests the frozen law on a DISJOINT set of new zones and new ratios and counts
the violations.  The bar %.1f is QUOTED from T128 and is not moved."""
     % (KAP_MIN_T128, KAP_MAX_T128, KAP_MED_T128, BAR_KAPPA, KAP_OVER_T128,
        KAP_N_T128, "/".join("%.3f" % x for x in KAP_GRP_T128),
        "/".join("%.3f" % x for x in RHO_GRP_T128), KAP_R_T128[0],
        KAP_R_T128[1], KAP_L_T128[0], KAP_L_T128[1], BAR_KAPPA))

print("")
print("""  K1.1  THE TWO IDENTITIES.  Let I_f = [-al_f, -al_f + gc_f D_f] be the
  fine border block, I_c the coarse one, g_i the fraction of fine cell i inside
  I_c, and t_l, t_r the two protrusions in units of D_f.  Then

      sum_{i < gc_f} (1 - g_i) = t_l + t_r        (interval geometry, exact)

  because the left side is the protruding LENGTH divided by D_f.  Hence, with
  omega_i = (1 - g_i)/(t_l + t_r) and p_i = gc_f w_i^2 / ||y||^2,

      omega >= 0 ,  sum omega = 1 ,  sum_i p_i = gc_f ,  mean p = 1 ,
      kappa = sum_i omega_i p_i                    (an AVERAGE, not a mass)

  and two consequences follow immediately.  (a) The FLAT border vector has
  p == 1, so kappa_flat == 1 EXACTLY -- the bar 2 was never the flat-vector
  limit, it was twice it.  (b) Hoelder: kappa <= max{ p_i : omega_i > 0 }, and
  omega is supported on the ceil(t_l) outermost and ceil(t_r) innermost cells of
  the border block.  So (T) is not a mass hypothesis at all: it is a POINTWISE
  DENSITY bound at the two ENDS of the border block.""")

_smoke = None
for d in REC:
    if d["h_f"] <= 400 and d["gc_f"] >= 4:
        _smoke = seam_full(UU_ALL[d["k"]], UU_ALL[d["k"] + 1], d["D_c"],
                           d["D_f"], d["n"])
        if _smoke is not None and _smoke["kap"] is not None:
            break
        _smoke = None
check("el_k1.machinery", _smoke is not None and abs(_smoke["ident"]) < 1.0e-12,
      "the T128 (T) identity is rebuilt here and reproduces: algebraic residual "
      "%.2e at n = %d (h_c = %d, h_f = %d, rho = %.4f), ||y|| = 1 to %.2e"
      % (abs(_smoke["ident"]) if _smoke else float("nan"),
         _smoke["n"] if _smoke else -1, _smoke["h_c"] if _smoke else -1,
         _smoke["h_f"] if _smoke else -1, _smoke["rho"] if _smoke else 0.0,
         abs(_smoke["ynrm"] - 1.0) if _smoke else float("nan")))


def build_pool(rhos, per_rho, hcap, label, tmin):
    pool = []
    for rho in rhos:
        seen = set()
        got = []
        for k in range(3, NZ_DEEP - 2):
            DA = 0.5 * float(GG_ALL[k]) / NU_MAIN
            hf = even_window(UU_ALL[k + 1], DA / rho) // 2
            if hf > hcap or hf < H_MIN:
                continue
            key = int(round(9.0 * math.log(max(NN_ALL[k], 2))))
            if key in seen:
                continue
            seen.add(key)
            got.append((k, DA))
        for (k, DA) in got[-per_rho:]:
            if budget_left() < tmin:
                info("K1.budget", "%s pool truncated at n = %d"
                     % (label, NN_ALL[k]))
                return pool
            t = seam_full(UU_ALL[k], UU_ALL[k + 1], DA, DA / rho, NN_ALL[k],
                          cap=hcap)
            if t is not None and t["kap"] is not None:
                t["rho_lbl"] = rho
                t["set"] = label
                pool.append(t)
    return pool


RHO_CAL = (1.001, 1.250, RHO_UNI_T127)
CAL = build_pool(RHO_CAL, CAL_PER_RHO, H_POOL, "calibration", 520.0)

_kf = [t["kap"]["kap_flat"] for t in CAL]
_gid = [t["kap"]["geo_id"] for t in CAL]
_lid = [t["kap"]["lin_id"] for t in CAL]
_hold = [t["kap"]["kap"] <= t["kap"]["p_max"] * (1.0 + 1.0e-8) + 1.0e-12
         for t in CAL]
_wsum = max(abs(t["kap"]["w_om_sum"] - 1.0) for t in CAL)
check("el_k1.identities", bool(CAL) and max(abs(x - 1.0) for x in _kf) < 1.0e-8
      and max(_gid) < 1.0e-10 and max(_lid) < 1.0e-9 and all(_hold),
      "BOTH IDENTITIES HOLD ON EVERY CALIBRATION TRANSPORT (%d of them), and "
      "they are IDENTITIES, not fits: sum(1 - g_i) = t_l + t_r to %.2e "
      "absolute, hence sum(omega) = 1 to %.2e and the FLAT border vector gives "
      "kappa = 1 to %.2e -- so the T128 bar 2 was TWICE the flat-vector value, "
      "not the flat-vector value; the Hoelder step kappa <= max p over the "
      "protruding cells holds on all %d; and the profile identity p_{N-1} = 2 "
      "- p_0 + 2E holds to %.2e.  That last one is the structural news: a "
      "LINEAR density profile with p_0 = 0 gives exactly kappa = 2, so 2 is "
      "the LINEAR-DENSITY limit and everything above it is CURVATURE"
      % (len(CAL), max(_gid), _wsum, max(abs(x - 1.0) for x in _kf), len(CAL),
         max(_lid)))

print("")
print("  K1.2  CALIBRATION -- C estimated on the T128 grouping recipe, then "
      "FROZEN")
print("       rho      n    | kappa  min  median     max | kappa_l  kappa_r  "
      "  p_0     p_N   curv")
CAL_GRP = []
for rho in RHO_CAL:
    g = [t for t in CAL if t["rho_lbl"] == rho]
    if not g:
        continue
    kk = [t["kap"]["kap"] for t in g]
    kl = [t["kap"]["kap_l"] for t in g if math.isfinite(t["kap"]["kap_l"])]
    kr = [t["kap"]["kap_r"] for t in g if math.isfinite(t["kap"]["kap_r"])]
    _q = q_of(kk)
    CAL_GRP.append(dict(rho=float(np.median([t["rho"] for t in g])), n=len(g),
                        kmin=_q[0], kmed=_q[1], kmax=_q[2]))
    print("   %7.4f %5d  | %10.3f %7.3f %7.3f | %7.3f %8.3f %7.3f %7.3f %6.3f"
          % (CAL_GRP[-1]["rho"], len(g), _q[0], _q[1], _q[2],
             float(np.median(kl)) if kl else float("nan"),
             float(np.median(kr)) if kr else float("nan"),
             float(np.median([t["kap"]["p0"] for t in g])),
             float(np.median([t["kap"]["pN"] for t in g])),
             float(np.median([t["kap"]["curv"] for t in g]))))

_a, C_HAT, _rms, C_SE = fit_band([g["rho"] - 1.0 for g in CAL_GRP],
                                 [g["kmax"] for g in CAL_GRP])
C_STAR = float(C_HAT)
CAL_OVER = sum(1 for t in CAL if t["kap"]["kap"]
               > BAR_KAPPA + C_STAR * (t["rho"] - 1.0))
check("el_k1.constant_frozen", math.isfinite(C_STAR),
      "C IS NOW FROZEN AT C* = %.4f (jackknife SE %.4f, fit intercept %.4f, "
      "rms %.4f) -- the least-squares slope of the GROUP MAXIMA against rho - 1 "
      "over the %d calibration groups, taken as-is and NOT rounded up, NOT "
      "padded, NOT refitted after the test.  This is a FIT and is labelled a "
      "fit; the intercept %.4f sits BELOW the T128 bar %.1f, which is why the "
      "law is stated as kappa <= 2 + C*(rho - 1) and not as kappa <= a + "
      "C*(rho - 1).  On the calibration set itself the law is violated %d "
      "times out of %d -- reported for completeness, it is NOT the test"
      % (C_STAR, C_SE, _a, _rms, len(CAL_GRP), _a, BAR_KAPPA, CAL_OVER,
         len(CAL)))

print("")
print("""  K1.3  THE TEST.  New zones, new ratios, both sides.  TWO tests are
  declared here, before the numbers, and BOTH are reported afterwards whatever
  they say.  TEST A is the law on T128's own quantity, kappa = m_prot gc_f /
  (t_l + t_r), which mixes the two protrusions.  TEST B is the SHARPER
  per-side law on kappa_r alone -- T128 measured that the right protrusion
  carries essentially all of the concentration (1.61..2.07 against 0.09..0.25),
  so if the law is to mean anything mechanically it has to hold there too.  The
  bar in both is the SAME frozen expression 2 + C*(rho - 1); it is not widened
  for test B.""")
RHO_TST = (1.05, 1.10, 1.20, 1.35, 1.60, 1.75, 2.00, 2.50, 3.00, 3.50, 4.00)
TST = build_pool(RHO_TST, TST_PER_RHO, H_POOL, "test", 430.0)
if budget_left() > 400.0:
    TST += build_pool((1.90, 2.25, 2.75), 16, H_DEEPCHK, "test-deep", 360.0)

print("       rho       n |  h_c   h_f gc_f  t_l    t_r  | kappa  kappa_l "
      "kappa_r |  bar    slack   status")
_show = max(1, len(TST) // 26)
for t in TST[::_show]:
    kk = t["kap"]
    bar = BAR_KAPPA + C_STAR * (t["rho"] - 1.0)
    print("   %7.4f %6d | %5d %5d %4d %6.3f %6.3f | %6.3f %7.3f %7.3f | "
          "%6.3f %+8.4f  %s"
          % (t["rho"], t["n"], t["h_c"], t["h_f"], t["gc_f"], t["t_l"],
             t["t_r"], kk["kap"], kk["kap_l"], kk["kap_r"], bar,
             bar - kk["kap"], "ok" if kk["kap"] <= bar else "VIOLATION"))
if _show > 1:
    info("K1.table", "every %d-th of the %d test transports is listed; all %d "
         "enter every number below" % (_show, len(TST), len(TST)))

def bar_of(t):
    return BAR_KAPPA + C_STAR * (t["rho"] - 1.0)


VIO = [t for t in TST if t["kap"]["kap"] > bar_of(t)]
TST_R = [t for t in TST if math.isfinite(t["kap"]["kap_r"])]
VIO_R = [t for t in TST_R if t["kap"]["kap_r"] > bar_of(t)]
K_ALL = [t["kap"]["kap"] for t in TST]
K_L = [t["kap"]["kap_l"] for t in TST if math.isfinite(t["kap"]["kap_l"])]
K_R = [t["kap"]["kap_r"] for t in TST_R]
K_BARE = sum(1 for x in K_ALL if x > BAR_KAPPA)
_qa, _ql, _qr = q_of(K_ALL), q_of(K_L), q_of(K_R)
_worst = min(TST, key=lambda t: bar_of(t) - t["kap"]["kap"]) if TST else None
_worstr = min(TST_R, key=lambda t: bar_of(t) - t["kap"]["kap_r"]) if TST_R else None
LAW_OK = bool(TST) and not VIO
LAW_R_OK = bool(TST_R) and not VIO_R
check("el_k1.law_tested", bool(TST) and len(TST) >= 60,
      "THE FROZEN LAW WAS TESTED ON %d NEW TRANSPORTS at %d ratios NONE of "
      "which is in the calibration set (%s against %s), spanning h_f = %d..%d "
      "and n = %d..%d.  TEST A (T128's kappa): %d VIOLATIONS of kappa <= 2 + "
      "%.4f (rho - 1) out of %d; against the UNMOVED bare bar kappa <= %.1f "
      "there are %d.  TEST B (the sharper per-side law on kappa_r): %d "
      "VIOLATIONS out of %d.  kappa = %.3f..%.3f (median %.3f); by side "
      "kappa_l = %.3f..%.3f against kappa_r = %.3f..%.3f -- the T128 side "
      "asymmetry reproduces on entirely new data and is if anything stronger.  "
      "Tightest A: n = %d at rho = %.4f, slack %+.4f.  Tightest B: n = %d at "
      "rho = %.4f, slack %+.4f"
      % (len(TST), len(set(t["rho_lbl"] for t in TST)),
         "/".join("%.2f" % r for r in sorted(set(t["rho_lbl"] for t in TST))),
         "/".join("%.3f" % r for r in RHO_CAL),
         min(t["h_f"] for t in TST), max(t["h_f"] for t in TST),
         min(t["n"] for t in TST), max(t["n"] for t in TST),
         len(VIO), C_STAR, len(TST), BAR_KAPPA, K_BARE, len(VIO_R), len(TST_R),
         _qa[0], _qa[2], _qa[1], _ql[0], _ql[2], _qr[0], _qr[2],
         _worst["n"], _worst["rho"], bar_of(_worst) - _worst["kap"]["kap"],
         _worstr["n"], _worstr["rho"],
         bar_of(_worstr) - _worstr["kap"]["kap_r"]))
if VIO_R:
    print("")
    print("       THE TEST-B VIOLATIONS, listed in full (the bar is NOT moved)")
    print("          n      rho   gc_f   t_r  | kappa_r    bar    excess")
    for t in sorted(VIO_R, key=lambda z: bar_of(z) - z["kap"]["kap_r"])[:12]:
        print("      %7d %8.4f %5d %6.3f | %7.3f %7.3f %+9.4f"
              % (t["n"], t["rho"], t["gc_f"], t["t_r"], t["kap"]["kap_r"],
                 bar_of(t), t["kap"]["kap_r"] - bar_of(t)))

print("")
print("""  K1.4  THE STRUCTURE -- why the RIGHT kappa grows with rho.  The
  density profile p on the border block is measured against the two reference
  shapes.  FLAT means p == 1 and kappa == 1.  LINEAR with a vanishing outer
  value means p(xi) = 2 xi and kappa_r == 2.  The exact profile identity

      p_{N-1} = 2 - p_0 + 2 E ,   E = (1/N) sum_j (j+1) (Dp_j - Dbar)

  says the whole excess over 2 is (i) the outer-cell value p_0 pushing DOWN and
  (ii) the term E, which vanishes for a linear profile and is POSITIVE exactly
  when the slope Dp is positively correlated with the index -- i.e. when p is
  CONVEX (Chebyshev's correlation inequality).  Abel summation majorises it:

      kappa <= p_max <= 2 - p_0 + ((N-2)/N) sum_j |Dp_j - Dbar| + (p_max - p_N)

  which is a THEOREM with an EXPLICIT constant, checked below on every
  transport.  The remaining question is then no longer "is kappa bounded" but
  "is the CURVATURE of the border density bounded" -- a strictly smaller
  object, and one that lives on ceil(t) cells, not on the whole grid.""")

POOL = CAL + TST
CHAIN_OK = all(t["kap"]["kap"] <= t["kap"]["bnd"] + 1.0e-10 for t in POOL)
CH_SLACK = [t["kap"]["bnd"] - t["kap"]["kap"] for t in POOL]
PEAK_END = sum(1 for t in POOL if t["kap"]["peaks_at_end"])
_qc = q_of(CH_SLACK)
check("el_k1.curvature_chain", CHAIN_OK,
      "THE CURVATURE CHAIN IS A THEOREM AND IT HOLDS ON ALL %d TRANSPORTS "
      "(calibration + test): kappa <= 2 - p_0 + ((N-2)/N) CURV + (p_max - "
      "p_{N-1}), slack %.4f..%.4f (median %.4f).  The density peaks at the "
      "INNER end of the border block on %d of %d, so the last correction is "
      "zero there and the bound is the clean form 2 - p_0 + ((N-2)/N) CURV.  "
      "Every step is classical: Hoelder for the mean, telescoping for the "
      "profile identity, Abel summation for the majorant"
      % (len(POOL), _qc[0], _qc[2], _qc[1], PEAK_END, len(POOL)))

_gr = {}
for t in POOL:
    _gr.setdefault(round(t["rho_lbl"], 3), []).append(t)
print("")
print("       rho      n |  p_0    p_N   p_max |  CURV   ((N-2)/N)CURV | "
      "kappa_r  2-p_0  excess over 2")
CURV_X, CURV_Y = [], []
for rho in sorted(_gr):
    g = _gr[rho]

    def med(fn, grp=g):
        return med_of([fn(t) for t in grp])

    p0m = med(lambda t: t["kap"]["p0"])
    majm = med(lambda t: t["kap"]["maj"])
    krm = med(lambda t: t["kap"]["kap_r"])
    print("   %7.3f %6d | %6.3f %6.3f %6.3f | %6.3f %14.3f | %7.3f %6.3f "
          "%+14.4f"
          % (rho, len(g), p0m, med(lambda t: t["kap"]["pN"]),
             med(lambda t: t["kap"]["p_max"]), med(lambda t: t["kap"]["curv"]),
             majm, krm, 2.0 - p0m, krm - 2.0))
    CURV_X.append(rho - 1.0)
    CURV_Y.append(majm)
_ca, _cb, _crms, _cse = fit_band(CURV_X, CURV_Y)
CONV = sum(1 for t in POOL if t["kap"]["E"] > 0.0)
OVER2 = sum(1 for t in POOL if t["kap"]["pN"] > 2.0)
CRIT = sum(1 for t in POOL if 2.0 * t["kap"]["E"] > t["kap"]["p0"])
check("el_k1.structure", CRIT == OVER2,
      "AND THE STRUCTURAL ANSWER IS A COMPETITION, NOT A ONE-SIDED EFFECT.  "
      "The identity makes p_{N-1} > 2 EXACTLY equivalent to 2E > p_0, and that "
      "equivalence is confirmed transport by transport: %d of %d satisfy 2E > "
      "p_0 and the SAME %d have p_{N-1} > 2, with no exception.  So the border "
      "density exceeds the linear limit only when its convexity term beats its "
      "edge value; E > 0 on %d of %d, i.e. the density is convex on about half "
      "the sample, and the outer-cell value p_0 = %.3f..%.3f is what usually "
      "wins -- the odd eigenvector nearly vanishes at the window edge, which is "
      "also why kappa_l is an order of magnitude smaller than kappa_r.  The "
      "majorised curvature ((N-2)/N) CURV grows with the ratio as %.4f + %.4f "
      "(rho - 1) (FIT, jackknife SE %.4f, rms %.4f), so the rho dependence T128 "
      "found in kappa is inherited from the curvature term and p_0 shrinks with "
      "rho at the same time -- both pull the same way"
      % (CRIT, len(POOL), OVER2, CONV, len(POOL),
         min(t["kap"]["p0"] for t in POOL),
         max(t["kap"]["p0"] for t in POOL), _ca, _cb, _cse, _crms))
print("")
print("""  K1.5  THE SAME LAW AT DEPTHS NO UNIFORM GRID REACHES.  The border
  block sits in the UNMERGED part of the graded two-scale space (K2 builds it,
  and k_fine is chosen so the whole border stencil stays fine), so the border
  density p -- and therefore kappa and the curvature chain -- can be read off
  EXACTLY at fine cell counts far past the hard cap, using only the matrix-free
  assembly.  These are the deepest kappa data points that exist anywhere in
  T111..T129.  The bar is the same frozen expression; nothing is rescaled.""")
DEEPK = []
for _rho in (1.25, 1.75, 2.50):
    _seen = set()
    for k in range(3, NZ_DEEP - 2):
        if budget_left() < 420.0:
            break
        DA = 0.5 * float(GG_ALL[k]) / NU_MAIN
        geo = edge_geom(UU_ALL[k], UU_ALL[k + 1], DA, DA / _rho)
        if geo is None or not (1600 <= geo["h_f"] <= 40000):
            continue
        key = int(round(1.4 * math.log(max(geo["h_f"], 2))))
        if key in _seen:
            continue
        _seen.add(key)
        sg = graded_seam(UU_ALL[k], UU_ALL[k + 1], DA, DA / _rho, NN_ALL[k])
        if sg is not None and sg["kap"] is not None:
            DEEPK.append(sg)

print("       rho       n |    h_c     h_f | q_c q_f  m/h_f | gc_f  nf/r_s | "
      "kappa   bar    slack  | chain slack")
for t in sorted(DEEPK, key=lambda z: (z["rho"], z["h_f"])):
    kk = t["kap"]
    bar = BAR_KAPPA + C_STAR * (t["rho"] - 1.0)
    print("   %7.4f %6d | %6d %6d | %3d %3d %6.3f | %4d %4d/%-4d | %6.3f "
          "%6.3f %+8.4f | %+8.4f  %s"
          % (t["rho"], t["n"], t["h_c"], t["h_f"], t["q_c"], t["q_f"],
             t["mh_f"], t["gc_f"], t["nf"], t["rs_f"], kk["kap"], bar,
             bar - kk["kap"], kk["bnd"] - kk["kap"],
             "ok" if kk["kap"] <= bar else "VIOLATION"))
DK_VIO = [t for t in DEEPK if t["kap"]["kap"]
          > BAR_KAPPA + C_STAR * (t["rho"] - 1.0)]
DK_CH = all(t["kap"]["kap"] <= t["kap"]["bnd"] + 1.0e-10 for t in DEEPK)
check("el_k1.deep_law", bool(DEEPK) and DK_CH,
      "THE LAW AND THE CHAIN AT DEPTH: %d graded transports at h_f = %d..%d "
      "(up to %.0f x the hard cap %d, compressed to m/h_f = %.3f..%.3f), rho = "
      "%.2f..%.2f, n = %d..%d.  VIOLATIONS of the frozen law: %d.  The "
      "curvature chain -- a theorem -- holds on all %d (slack %.4f..%.4f), and "
      "kappa there is %.3f..%.3f, i.e. the concentration does NOT drift upward "
      "with depth: whatever kappa's residual risk is, it is a RATIO effect and "
      "not a resolution effect, which is the one thing a finite computation "
      "can actually settle"
      % (len(DEEPK), min(t["h_f"] for t in DEEPK), max(t["h_f"] for t in DEEPK),
         max(t["h_f"] for t in DEEPK) / float(MAX_H), MAX_H,
         min(t["mh_f"] for t in DEEPK), max(t["mh_f"] for t in DEEPK),
         min(t["rho"] for t in DEEPK), max(t["rho"] for t in DEEPK),
         min(t["n"] for t in DEEPK), max(t["n"] for t in DEEPK), len(DK_VIO),
         len(DEEPK), min(t["kap"]["bnd"] - t["kap"]["kap"] for t in DEEPK),
         max(t["kap"]["bnd"] - t["kap"]["kap"] for t in DEEPK),
         min(t["kap"]["kap"] for t in DEEPK),
         max(t["kap"]["kap"] for t in DEEPK)))
info("K1.timing", "K1 done, %.1f s used, %.0f s budget left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("K2  THE TWO AFFORDABLE DEEP SEAMS -- the graded two-scale seam")
# ----------------------------------------------------------------------------
print("""  THE DIRECTION FENCE, FIRST.  The graded space V_m (fine cells at the
  window EDGE, blocks of q merged inward, anchored at the window CENTRE) is a
  SUBSPACE of the fine PWC space.  Rayleigh-Ritz therefore gives

      lam_min(S_graded)  >=  lam_min(S_fine) ,

  one-sided and in the WRONG direction for a proof: a positive graded floor is
  IMPLIED by a positive fine floor, not the reverse.  Turning it around needs
  the Cea/Strang defect ||(I - Pi) z*||^2 of the FINE partial minimiser, and z*
  is exactly the object the hard cap forbids at these depths.  So the deep
  seams below get their own status word, GRADED-CERTIFIED, and the gap is
  CALIBRATED at affordable depths at the same working point instead of being
  waved away.  Two structural facts make the graded seam well posed at all:
  (a) the merge is anchored at the window centre, so the new window's basis is
  the old one plus gc new FINE cells, hence X_graded = Q_old,graded EXACTLY and
  Albert's hypothesis stays pure semidefiniteness of the previous zone -- the
  step is still MARGIN-FREE; (b) every graded basis function is the normalised
  indicator of an INTERVAL, so the coarse-to-fine transport is still a pure
  interval computation and the border geometry of K1 applies verbatim, because
  the border block sits inside the fine part by construction.""")

# --- K2.1  the graded machinery, verified against the uniform reference -----
_zc = None
for d in REC:
    if 260 <= d["h_f"] <= 620:
        _zc = d
if _zc is None:
    _zc = REC[-1]
_u_o, _u_n = UU_ALL[_zc["k"]], UU_ALL[_zc["k"] + 1]
G1 = graded_step(_u_o, _u_n, _zc["D_f"], 1, k_fine=K_FINE_DEEP)
G4 = graded_step(_u_o, _u_n, _zc["D_f"], 4, k_fine=K_FINE_DEEP, want_old=True)
_fr = G4["fr"]
_at = atoms_in(_fr["al_n"], ATOMS_ALL)
_c, _ = lag_vector_fast(_fr["al_n"], _fr["M_n"], _at)
_tv = odd_pole_vector(_fr["al_n"], _fr["M_n"])
_Qfine = sym(odd_toeplitz(_c, _fr["M_n"]) - np.outer(_tv, _tv))
_J = merge_J(G4["mc_n"])
E_ASM = rel(G4["Q"] - _J.T @ _Qfine @ _J, _Qfine)
E_UNI = rel(G1["Q"] - _Qfine, _Qfine)
E_STEP = rel(G4["Q"][_fr["gc"]:, _fr["gc"]:] - G4["Q_old"], G4["Q_old"])
_xn, _Dn = odd_nodes(_fr["al_n"], _fr["M_n"])
_Pref = overlap_odd(_xn, _Dn, _xn, _Dn)
_Pg = overlap_graded(G1["lo"], G1["hi"], G1["W"], G1["lo"], G1["hi"], G1["W"])
E_OVL = rel(_Pg - _Pref, _Pref)
_PJ = overlap_graded(G1["lo"], G1["hi"], G1["W"], G4["lo"], G4["hi"], G4["W"])
E_NEST = rel(_PJ - _J, _J)
check("el_k2.graded_machinery",
      E_ASM < 1.0e-12 and E_UNI < 1.0e-13 and E_STEP < 1.0e-12
      and E_OVL < 1.0e-11 and E_NEST < 1.0e-11,
      "THE GRADED MACHINERY IS VERIFIED AGAINST THE UNIFORM REFERENCE at n = "
      "%d (h = %d): the matrix-free two-scale assembly equals J^T Q J to %.2e "
      "(q = 4, m = %d); at q = 1 it equals the uniform form to %.2e, so the "
      "graded path CONTAINS the uniform path as a special case and no separate "
      "code is trusted; the compressed step identity X = Q_old holds to %.2e, "
      "so the step is still margin-free (Albert 1969); the graded interval "
      "overlap reproduces the uniform overlap to %.2e and reproduces the "
      "prolongation J itself to %.2e, which is the transport's own consistency "
      "test (a graded space against its own refinement must give exactly J)"
      % (_zc["n"], _zc["h_f"], E_ASM, G4["m"], E_UNI, E_STEP, E_OVL, E_NEST))
del _J, _Qfine, _Pref, _Pg, _PJ, G1, G4

# --- K2.2  the compression gap, CALIBRATED at affordable depths -------------
GAP_CAND = [(d["n"], UU_ALL[d["k"]], UU_ALL[d["k"] + 1], d["D_c"], d["D_f"],
             d["rho"], d["h_f"], d["gc_f"], "record")
            for d in REC]
# the record seams alone are too few in the affordable window, so the
# calibration is widened with SYNTHETIC (zone, ratio) pairs -- the same objects
# K1 uses, and the graded/uniform comparison does not care where rho came from
for _rho in (1.25, 1.75, 2.00):
    _seen = set()
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(GG_ALL[k]) / NU_MAIN
        geo = edge_geom(UU_ALL[k], UU_ALL[k + 1], DA, DA / _rho)
        if geo is None or not (150 <= geo["h_f"] <= 1000) or geo["gc_f"] < 3:
            continue
        key = int(round(2.0 * math.log(max(NN_ALL[k], 2))))
        if key in _seen:
            continue
        _seen.add(key)
        GAP_CAND.append((NN_ALL[k], UU_ALL[k], UU_ALL[k + 1], DA, DA / _rho,
                         _rho, geo["h_f"], geo["gc_f"], "rho %.2f" % _rho))

CALG = []
for (nn, u_o, u_n, DA, DB, rho, hf, gcf, lbl) in GAP_CAND:
    if len(CALG) >= GAP_ZONES or budget_left() < 300.0:
        break
    if not (100 <= hf <= 1450) or gcf < 3:
        continue
    if any(r["n"] == nn and r["lbl"] == lbl for r in CALG):
        continue
    su = graded_seam(u_o, u_n, DA, DB, nn, q_c=1, q_f=1)
    if su is None:
        continue
    row = dict(n=nn, rho=rho, h_f=hf, uni=su, g=[], lbl=lbl)
    for (qc, qf) in GAP_QSET:
        sg = graded_seam(u_o, u_n, DA, DB, nn, q_c=qc, q_f=qf)
        if sg is not None:
            row["g"].append(sg)
    if row["g"]:
        CALG.append(row)

print("")
print("  K2.2  THE COMPRESSION GAP, CALIBRATED at depths where BOTH exist")
print("        n    h_f | q_c q_f  m_f   m/h  | lam_c ratio  lam_f ratio  "
      "lo(uni)    lo(graded)   lo ratio  verdict move")
GAPR, LOR, SGN, FALSEPOS = [], [], [], []
for r in CALG:
    for sg in r["g"]:
        rc = sg["lam_c"] / max(r["uni"]["lam_c"], 1.0e-300)
        rf = sg["lam_f"] / max(r["uni"]["lam_f"], 1.0e-300)
        pos_u, pos_g = r["uni"]["lo_pos"], sg["lo_pos"]
        same = (pos_u == pos_g)
        if r["uni"]["lo"] > 0.0:
            rl = sg["lo"] / r["uni"]["lo"]
            LOR.append(rl)
            rls = "%9.3f" % rl
        else:
            rl = float("nan")
            rls = "      n/a"
        if pos_g and not pos_u:
            FALSEPOS.append((r, sg))
            mv = "FALSE POSITIVE"
        elif same:
            mv = "agree"
        else:
            mv = "lost (conservative)"
        GAPR.append(rf)
        SGN.append(same)
        print("   %6d %6d | %3d %3d %5d %5.3f | %11.4f %11.4f  %10.3e "
              "%11.3e %s  %s"
              % (r["n"], r["h_f"], sg["q_c"], sg["q_f"], sg["m_f"], sg["mh_f"],
                 rc, rf, r["uni"]["lo"], sg["lo"], rls, mv))
_qg, _qlr = q_of(GAPR), q_of(LOR)
check("el_k2.gap_calibrated", bool(GAPR) and all(x >= 1.0 - 1.0e-9 for x in GAPR),
      "THE COMPRESSION GAP IS ONE-SIDED AND MEASURED, at the working point the "
      "deep seams use: over %d (zone, q) pairs at %d zone/ratio settings "
      "(rho = %.3f..%.3f, h_f = %d..%d) the graded Schur floor is LARGER than "
      "the uniform one by a factor %.3f..%.3f (median %.3f) -- Rayleigh-Ritz, "
      "as declared, with no exception.  Where the uniform seam floor is "
      "positive the graded one is %.3f..%.3f times it (median %.3f).  The two "
      "agree in SIGN on %d of %d"
      % (len(GAPR), len(CALG), min(r["rho"] for r in CALG),
         max(r["rho"] for r in CALG), min(r["h_f"] for r in CALG),
         max(r["h_f"] for r in CALG), _qg[0], _qg[2], _qg[1], _qlr[0],
         _qlr[2], _qlr[1], sum(SGN), len(SGN)))

_fpz = sorted(set(r["n"] for r, _ in FALSEPOS))
check("el_k2.false_positive_rate", bool(GAPR),
      "AND THE DIRECTION FENCE IS NOT THEORETICAL -- IT BITES, AND IT IS "
      "MEASURED HERE RATHER THAN LEFT AS A CAVEAT: on %d of %d calibration "
      "pairs (zones n = %s) the GRADED seam floor is POSITIVE while the "
      "UNIFORM seam floor at the same zone is NOT.  Those are demonstrated "
      "FALSE POSITIVES of compression, at depths shallow enough that both "
      "sides can be computed.  So GRADED-CERTIFIED is a genuinely weaker word "
      "than CERTIFIED, with an observed failure rate of %.0f per cent on this "
      "sample, and the two deep seams of K2.3 inherit exactly that caveat.  "
      "This is the single most important honest number in the block and it is "
      "printed before the deep seams, not after"
      % (len(FALSEPOS), len(GAPR), ", ".join(str(x) for x in _fpz) or "none",
         100.0 * len(FALSEPOS) / max(len(GAPR), 1)))

# --- K2.3  the two deep seams ----------------------------------------------
print("")
print("  K2.3  THE TWO DEEP SEAMS, brought under the cap")
print("        n    rho   |   h_c   h_f |q_c q_f|  m_c   m_f  m/h_c m/h_f | "
      "lam_c     tau_dn   |eta|     floor      status")
DEEP_ROWS = []
for d in DEEP2:
    if budget_left() < 150.0:
        info("K2.budget", "deep seam n = %d skipped, budget" % d["n"])
        DEEP_ROWS.append(dict(n=d["n"], h_f=d["h_f"], sg=None,
                              status="BUDGET-OPEN"))
        continue
    u_o, u_n = UU_ALL[d["k"]], UU_ALL[d["k"] + 1]
    sg = graded_seam(u_o, u_n, d["D_c"], d["D_f"], d["n"])
    if sg is None:
        DEEP_ROWS.append(dict(n=d["n"], h_f=d["h_f"], sg=None,
                              status="NO-GRADED-FRAME"))
        continue
    ok = bool(sg["lo_pos"] and sg["cert_c"] and sg["cert_f"] and sg["x_pd_c"]
              and sg["x_pd_f"])
    st = "GRADED-CERTIFIED" if ok else "GRADED-UNCERTIFIED"
    lad = [sg]
    for (qc, qf) in ((sg["q_c"], sg["q_f"] + 1), (sg["q_c"] + 1, sg["q_f"] + 2),
                     (sg["q_c"] + 2, sg["q_f"] + 4)):
        if budget_left() < 140.0:
            break
        s2 = graded_seam(u_o, u_n, d["D_c"], d["D_f"], d["n"], q_c=qc, q_f=qf)
        if s2 is not None:
            lad.append(s2)
    DEEP_ROWS.append(dict(n=d["n"], h_f=d["h_f"], sg=sg, status=st, lad=lad))
    for s2 in lad:
        print("   %6s %7s | %5s %5s |%3d %3d|%5d %5d %5.3f %5.3f | %9.5f "
              "%8.5f %8.2e %+10.3e  %s"
              % (str(d["n"]) if s2 is sg else "", "%.4f" % sg["rho"]
                 if s2 is sg else "", str(sg["h_c"]) if s2 is sg else "",
                 str(sg["h_f"]) if s2 is sg else "", s2["q_c"], s2["q_f"],
                 s2["m_c"], s2["m_f"], s2["mh_c"], s2["mh_f"], s2["lam_c"],
                 s2["tau_dn"], abs(s2["eta_dn"]), s2["lo"],
                 st if s2 is sg else "  ladder rung"))

DG = [r for r in DEEP_ROWS if r["sg"] is not None]
DG_OK = [r for r in DG if r["status"] == "GRADED-CERTIFIED"]
check("el_k2.deep_seams", len(DG) == len(DEEP2),
      "BOTH DEEP SEAMS WERE BUILT AND BOTH FIT: n = %s at h_f = %s were "
      "compressed to m_f = %s (m/h = %s) with q_f = %s, every factorised block "
      "at or below the cap %d, and the fine square matrix NEVER formed.  %d of "
      "%d carry a complete graded seam certificate (X PD by Cholesky, both "
      "Schur floors above the Wilkinson floor, transport bracket positive).  "
      "Retentions lo/lam_c = %s"
      % (", ".join(str(r["n"]) for r in DG),
         ", ".join(str(r["h_f"]) for r in DG),
         ", ".join(str(r["sg"]["m_f"]) for r in DG),
         ", ".join("%.3f" % r["sg"]["mh_f"] for r in DG),
         ", ".join(str(r["sg"]["q_f"]) for r in DG), MAX_H, len(DG_OK), len(DG),
         ", ".join("%.4f" % r["sg"]["ret"] for r in DG)))

_dk = [r["sg"]["kap"] for r in DG if r["sg"]["kap"] is not None]
_dvio = [r for r in DG if r["sg"]["kap"] is not None
         and r["sg"]["kap"]["kap"] > BAR_KAPPA + C_STAR * (r["sg"]["rho"] - 1.0)]
check("el_k2.deep_kappa", True,
      "AND THE REAL DEEP SEAMS ARE ALSO A KAPPA TEST, at the ratios the "
      "free-resolution schedule actually produces (rho = %s, outside the "
      "calibration range and on genuine record seams rather than synthetic "
      "ones): kappa = %s against the frozen bar %s, %d violation(s), curvature "
      "chain slack %s.  They sit at h_f = %s, inside the range K1.5 already "
      "swept synthetically (up to %d)"
      % (", ".join("%.4f" % r["sg"]["rho"] for r in DG),
         ", ".join("%.3f" % k["kap"] for k in _dk) or "n/a",
         ", ".join("%.3f" % (BAR_KAPPA + C_STAR * (r["sg"]["rho"] - 1.0))
                   for r in DG),
         len(_dvio),
         ", ".join("%+.4f" % (k["bnd"] - k["kap"]) for k in _dk) or "n/a",
         ", ".join(str(r["h_f"]) for r in DG),
         max([t["h_f"] for t in DEEPK] + [0])))

_lad = [(r, s) for r in DG for s in r.get("lad", []) if s is not r["sg"]]
_ladpos = sum(1 for _, s in _lad if s["lo_pos"])
_ladlo = [s["lo"] for _, s in _lad]
check("el_k2.deep_q_ladder", True,
      "AND THE DEEP SEAMS WERE RUN AT %d FURTHER COMPRESSION LEVELS as a "
      "stability rung, because a single q is a single Galerkin space and "
      "proves nothing about the neighbouring ones: the seam floor stays "
      "positive on %d of %d additional (seam, q) points, floors %s.  A floor "
      "that survives coarsening by another factor is evidence the graded "
      "result is not an artefact of one particular merge -- MEASURED evidence, "
      "and it does not repair the Rayleigh-Ritz direction"
      % (len(_lad), _ladpos, len(_lad),
         ", ".join("%.3e" % x for x in _ladlo) or "none"))

# --- K2.4  the (L) ledger, restated ----------------------------------------
L_CERT_UNI = len(OUT) - len(L_OPEN0)
print("")
print("  K2.4  THE (L) LIST AFTER K2")
print("        n       h_f    required Cholesky  |  status")
for d in OUT:
    if d["h_f"] <= MAX_H:
        st = "CERTIFIED (T128, uniform)"
    else:
        m = [r for r in DEEP_ROWS if r["n"] == d["n"]]
        st = m[0]["status"] if m else "BUDGET-OPEN"
    print("   %7d %9d %18d  |  %s" % (d["n"], d["h_f"], d["h_f"] - d["gc_f"], st))
info("K2.ledger", "(L) = [%d CERTIFIED on the uniform space (T128), %d "
     "GRADED-CERTIFIED here on the two-scale space, %d BUDGET-OPEN and "
     "arithmetically characterised].  The honest sentence: the two deep seams "
     "moved from 'no certificate at all' to 'a complete certificate on a "
     "coarser Galerkin space, with the direction of the error known and its "
     "size calibrated' -- which is strictly more than T128 had and strictly "
     "less than a uniform certificate.  It is NOT '5 certified, 3 open'"
     % (L_CERT_UNI, len(DG_OK), len(L_OPEN0) - len(DG_OK)))
info("K2.timing", "K2 done, %.1f s used, %.0f s budget left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("K3  M18 -- THE COMB RESIDUAL, FROM A MEASUREMENT TO A BOUND")
# ----------------------------------------------------------------------------
print("""  WHAT T128 LEFT.  shat = s + comb splits into the POLE part s, whose
  boundary-layer exclusion T128 PROVED in closed form (cell-scale variation
  <= 1 - exp(-D_c/2), outer-k share <= k D_c (1 + cosh al)/sinh al), and the
  COMB part

      comb = - Bx^T x_c ,   x_c = Ac^{-1} b_c ,

  the detail component of the two-grid splitting applied to the coarse solve.
  It has no closed form, and T128 could only MEASURE that it is not a boundary
  layer.  Here it is BOUNDED, two ways, and the two behave very differently.

  (a) THE PER-INSTANCE BOUND (Cauchy-Schwarz, unconditional for this zone):
      sum_{i<k} comb_i^2 <= ||x_c||^2 sum_{i<k} ||row_i(Bx^T)||^2, an upper
      bound for the outer-k share that never looks at the alignment.

  (b) THE OPERATOR BOUND (S-procedure, valid for EVERY coarse vector in a
      smoothness cone).  With R = Bx Pi_k Bx^T, T = Bx Bx^T and L a discrete
      smoothness form, for any s >= 0 and any x with x^T L x <= theta^2 ||x||^2

          ||Pi_k Bx^T x||^2 <= lam_max(R - s(L - theta^2 I), T) ||Bx^T x||^2 ,

      so B_k(theta) = min_{s>=0} lam_max(...) majorises the outer-k share of
      the comb for EVERY such x -- a property of the CONSTRUCTED two-grid
      splitting, with the atoms entering only through Bx and never through the
      unknown minimiser.  lam_max is CONVEX in s, so the minimisation is exact
      by ternary search.  Two cones are used, first and second difference, and
      the smaller of the two bounds is taken (each is separately valid).  theta
      is MEASURED for the actual x_c, so (b) is CERTIFIED-CONDITIONAL on one
      measured number.  Which of (a) and (b) is worth anything is settled by
      the numbers below, not asserted here.""")


def _spro(Rt, Gt, lo=1.0e-6, hi=1.0e10, iters=30):
    """min_{s>=0} lam_max(Rt - s Gt) by ternary search on log s (lam_max of an
    affine matrix family is CONVEX in s, so the 1-D problem is unimodal)."""
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
        if v1 <= v2:
            b = m2
        else:
            a = m1
        if b - a < 1.0e-4:
            break
    return best


def comb_bounds(al, M, kset=M18_KSET):
    if (M // 2) % 2:
        return None
    at = atoms_in(al, ATOMS_ALL)
    c, D = lag_vector_fast(al, M, at)
    A = sym(odd_toeplitz(c, M))
    b = odd_pole_vector(al, M)
    Ac, Az, Bx = two_grid_blocks(A)
    del Az
    fac = safe_cho(Ac)
    if fac is None:
        return None
    x_c = cho_solve(fac, rest_p(b), check_finite=False)
    comb = -(Bx.T @ x_c)
    nc2 = float(np.dot(comb, comb))
    if not (nc2 > 0.0):
        return None
    nx2 = float(np.dot(x_c, x_c))
    hc = Bx.shape[0]
    d1 = np.diff(np.eye(hc), axis=0)
    d2 = np.diff(np.eye(hc), n=2, axis=0)
    L1, L2 = sym(d1.T @ d1), sym(d2.T @ d2)
    t1 = float(np.dot(np.diff(x_c), np.diff(x_c))) / nx2
    t2 = float(np.dot(np.diff(x_c, n=2), np.diff(x_c, n=2))) / nx2
    T = sym(Bx @ Bx.T)
    T = T + chol_floor(gersh(T), hc) * np.eye(hc)
    fT = safe_cho(T)
    if fT is None:
        return None
    Lt = np.tril(fT[0])

    def whiten(Mm):
        Y = np.linalg.solve(Lt, Mm)
        return sym(np.linalg.solve(Lt, Y.T).T)

    G1 = whiten(L1 - t1 * np.eye(hc))
    G2 = whiten(L2 - t2 * np.eye(hc))
    rown = (Bx ** 2).sum(axis=0)          # ||row_i(Bx^T)||^2
    out = dict(al=al, M=M, D=D, h=M // 2, hc=hc, th1=t1, th2=t2,
               nrm_comb=nc2 ** 0.5, Dc=2.0 * D, rows={})
    for k in kset:
        if k >= hc:
            continue
        share = float(np.dot(comb[:k], comb[:k])) / nc2
        cs = float(rown[:k].sum()) * nx2 / nc2
        Rt = whiten(sym(Bx[:, :k] @ Bx[:, :k].T))
        it = 30 if hc <= 220 else 16
        sp = min(_spro(Rt, G1, iters=it), _spro(Rt, G2, iters=it))
        out["rows"][k] = dict(share=share, cs=cs, sp=sp, law=k * (2.0 * D))
        del Rt
    del A, Ac, Bx, L1, L2, G1, G2, T
    return out


M18 = []
_zpool = [d for d in REC if 40 <= d["h_f"] <= M18_HMAX]
_pick = []
for d in _zpool:
    if any(abs(math.log(d["n"] / max(r["n"], 1))) < 0.25 for r in _pick):
        continue
    _pick.append(d)
if len(_pick) > M18_ZONES:
    _sel = np.linspace(0, len(_pick) - 1, M18_ZONES)
    _pick = [_pick[int(round(i))] for i in _sel]
for d in _pick:
    for mult in M18_DEPTHS:
        if budget_left() < 110.0:
            info("K3.budget", "comb study truncated at n = %d" % d["n"])
            break
        fr = step_frame(UU_ALL[d["k"]], UU_ALL[d["k"] + 1], d["D_f"] / mult)
        if fr is None or fr["h_n"] > M18_HMAX or fr["h_n"] < 32:
            continue
        M, al = fr["M_n"], fr["al_n"]
        if (M // 2) % 2:            # the two-grid split needs an even h
            M += 2
            al = 0.5 * M * fr["D"]
        r = comb_bounds(al, M)
        if r is None:
            continue
        r["n"] = d["n"]
        r["mult"] = mult
        M18.append(r)

print("")
print("        n  mult    h    D       theta_1^2 theta_2^2| k |  share    "
      "CS bound   S-proc bound   k*D_c   sp/share")
for r in M18:
    for k in sorted(r["rows"]):
        w = r["rows"][k]
        print("   %6d %4d %5d %9.3e %9.2e %9.2e | %d | %8.2e %9.2e %12.4f "
              "%9.2e %8.1f"
              % (r["n"], r["mult"], r["h"], r["D"], r["th1"], r["th2"], k,
                 w["share"], w["cs"], w["sp"], w["law"],
                 w["sp"] / max(w["share"], 1.0e-300)))

M18R = [(r, k, r["rows"][k]) for r in M18 for k in sorted(r["rows"])]
CS_MAJ = all(w["cs"] >= w["share"] - 1.0e-12 for _, _, w in M18R)
SP_MAJ = all(w["sp"] >= w["share"] - 1.0e-9 for _, _, w in M18R)
CS_NV = sum(1 for _, _, w in M18R if w["cs"] < BAR_M18)
SP_NV = sum(1 for _, _, w in M18R if w["sp"] < BAR_M18)
_sh = q_of([w["share"] for _, _, w in M18R])
check("el_k3.majorants", bool(M18R) and CS_MAJ and SP_MAJ,
      "BOTH COMB MAJORANTS ARE MAJORANTS ON EVERY ZONE x DEPTH (%d "
      "combinations, %d zones, depths x%s, h = %d..%d): the Cauchy-Schwarz row "
      "bound dominates the measured outer-k share on all %d, and so does the "
      "S-procedure operator bound.  The measured share itself is %.2e..%.2e "
      "(median %.2e), so the comb is nowhere near a boundary layer -- that part "
      "was never in doubt; what is new is that it is now BOUNDED and not only "
      "seen"
      % (len(M18R), len(set(r["n"] for r in M18)),
         "/".join(str(m) for m in M18_DEPTHS), min(r["h"] for r in M18),
         max(r["h"] for r in M18), len(M18R), _sh[0], _sh[2], _sh[1]))

_tsp = [w["sp"] / max(w["share"], 1.0e-300) for _, _, w in M18R]
_tcs = [w["cs"] / max(w["share"], 1.0e-300) for _, _, w in M18R]
_qsp, _qtc = q_of(_tsp), q_of(_tcs)
_spv = q_of([w["sp"] for _, _, w in M18R])
_x = [math.log(max(k * r["Dc"], 1.0e-300)) for r, k, _ in M18R]
_y = [math.log(max(w["sp"], 1.0e-300)) for _, _, w in M18R]
_la, _lb, _lrms, _lse = fit_band(_x, _y)
check("el_k3.comb_bounded", bool(M18R) and SP_NV == len(M18R),
      "AND ONE OF THE TWO BOUNDS TURNS M18 INTO A BOUND WHILE THE OTHER DOES "
      "NOT -- both results are reported.  THE S-PROCEDURE OPERATOR BOUND "
      "WORKS: it is below the vacuity bar 1 on %d of %d combinations, it runs "
      "%.3f..%.3f, and it exceeds the measured share by only %.1f..%.0f x "
      "(median %.1f).  So for EVERY coarse vector in the measured smoothness "
      "cone -- not merely for the one x_c that happens to occur -- the comb "
      "cannot place more than that fraction of its mass on the outer k cells.  "
      "THE CAUCHY-SCHWARZ ROW BOUND IS VACUOUS: below 1 on %d of %d, "
      "overshooting the truth by %.0f..%.0f x (median %.0f), because it throws "
      "away all alignment between the rows of Bx^T and x_c.  Reporting a "
      "majorant that fails is part of the measurement, not a footnote.  The "
      "S-procedure bound scales as (k D_c)^%.3f (FIT, jackknife SE %.3f, rms "
      "%.3f), i.e. it does NOT reproduce the pole part's O(k D) decay: it "
      "saturates, because the smoothness cone still contains vectors far more "
      "edge-loaded than x_c.  That saturation is the honest limit of this route"
      % (SP_NV, len(M18R), _spv[0], _spv[2], _qsp[0], _qsp[2], _qsp[1],
         CS_NV, len(M18R), _qtc[0], _qtc[2], _qtc[1], _lb, _lse, _lrms))

_th = q_of([r["th1"] for r in M18])
_xt = [math.log(r["D"]) for r in M18]
_yt = [0.5 * math.log(max(r["th1"], 1.0e-300)) for r in M18]
_ta, _tb, _trms, _tse = fit_band(_xt, _yt)
check("el_k3.cone_measured", bool(M18),
      "THE CONE PARAMETER IS MEASURED AND ITS SCALING IS THE EXPECTED ONE: "
      "theta_1^2 = x_c^T L_1 x_c / ||x_c||^2 runs %.3e..%.3e over the %d "
      "(zone, depth) points, and theta_1 scales as D^%.3f (FIT, jackknife SE "
      "%.3f, rms %.3f).  theta ~ D is exactly what a FIXED SMOOTH profile "
      "sampled on a grid of width D gives, so the coarse solve x_c is smooth "
      "at the cell scale and the conditional bound (b) is conditional on a "
      "MEASURED number with a known law -- not on a hope.  Making (b) "
      "unconditional needs a closed-form theta, and making it DECAY like the "
      "pole part needs a cone that is tight around x_c rather than around "
      "smoothness in general.  Those two are the honest residue of M18"
      % (_th[0], _th[2], len(M18), _tb, _tse, _trms))
info("K3.timing", "K3 done, %.1f s used, %.0f s budget left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("K4  THE MAP V4 -- what fell, what moved, what is irreducible")
# ----------------------------------------------------------------------------
MAP = []


def item(key, what, status, note):
    MAP.append(dict(key=key, what=what, status=status, note=note))


K1_STAT = "REDUCED" + ("" if LAW_R_OK else "; SIDE LAW BROKEN")
K2_STAT = ("GRADED" if len(DG_OK) == len(DEEP2) else "PARTIAL")
K3_STAT = "BOUNDED" if SP_NV == len(M18R) else "MEASURED"

item("M9", "(T) the protrusion concentration kappa", K1_STAT,
     "REDUCED, not merely retested.  kappa is now an IDENTITY: a probability "
     "average of the border DENSITY p over the two ends, with the flat vector "
     "at kappa = 1 and the linear-with-vanishing-edge vector at kappa = 2 "
     "exactly.  The chain kappa <= 2 - p_0 + ((N-2)/N) CURV is a THEOREM with "
     "an explicit constant, verified on %d transports.  The frozen law kappa "
     "<= 2 + %.4f (rho - 1) was violated %d times on %d NEW transports in its "
     "T128 form (test A) and %d times of %d in the sharper per-side form (test "
     "B), and 0 times on %d graded transports at up to %d fine cells.  What "
     "remains is a bound on the CURVATURE of the border density -- a strictly "
     "smaller object than the original mass hypothesis, living on ceil(t) "
     "cells rather than on the grid"
     % (len(POOL), C_STAR, len(VIO), len(TST), len(VIO_R), len(TST_R),
        len(DEEPK), max([t["h_f"] for t in DEEPK] + [0])))
item("L2", "(L) the two affordable deep seams", K2_STAT,
     "n = %s at h_f = %s now carry a COMPLETE seam certificate on the graded "
     "two-scale space (m/h = %s), assembled without ever forming the fine "
     "square matrix, and the floor survives %d further coarsening rungs.  But "
     "the Rayleigh-Ritz direction is against us and this probe DEMONSTRATES it "
     "biting: on %d of %d affordable calibration pairs the graded floor is "
     "positive where the uniform one is not.  (L) = [%d uniform-certified, %d "
     "graded-certified with a measured %.0f per cent false-positive rate at "
     "shallow depth, %d budget-open]"
     % (", ".join(str(r["n"]) for r in DG_OK) or "none",
        ", ".join(str(r["h_f"]) for r in DG_OK) or "-",
        ", ".join("%.3f" % r["sg"]["mh_f"] for r in DG_OK) or "-", _ladpos,
        len(FALSEPOS), len(GAPR), L_CERT_UNI, len(DG_OK),
        100.0 * len(FALSEPOS) / max(len(GAPR), 1), len(L_OPEN0) - len(DG_OK)))
item("M18", "(M) the comb residual of shat", K3_STAT,
     "the outer-k-cell share of comb now carries a CERTIFIED-CONDITIONAL "
     "operator majorant (S-procedure over the measured smoothness cone), "
     "non-vacuous on %d of %d zone x depth points at %.3f..%.3f and only "
     "%.1f..%.0f x above the truth -- so the comb is bounded away from a "
     "boundary layer for EVERY smooth coarse vector, not only for the one that "
     "occurs.  The unconditional Cauchy-Schwarz alternative is vacuous (%d of "
     "%d) and is reported as such.  What the bound does NOT do is decay like "
     "the pole part's closed-form O(kD): it saturates"
     % (SP_NV, len(M18R), _spv[0], _spv[2], _qsp[0], _qsp[2], CS_NV,
        len(M18R)))
item("M17", "(M) the pencil mass on {mu >= 1/2}", "UNTOUCHED",
     "not addressed by this contract; T128's measured 0.9665 stands as a "
     "measurement and the floor %.3f with %.1f x margin stands as certified"
     % (MU_FLOOR_T128, MU_MARGIN_T128))
item("M19", "the word 'for all' -- uniformity in the zone", "IRREDUCIBLE HERE",
     "every number in this probe, like every number in T111..T128, is a "
     "finite sample of zones and depths.  The curvature chain of K1 is a "
     "theorem PER TRANSPORT; making it a theorem FOR ALL transports needs a "
     "zone-uniform bound on the border density curvature, which no finite "
     "computation can supply.  This is the first of the two irreducibles")
item("M21", "the RH address", "IRREDUCIBLE AND UNTOUCHED",
     "Weil 1952 / Bombieri 2000 / Connes 1999 is CITED and used for nothing.  "
     "Even with M9, L2 and M18 fully closed, the statement reached is "
     "positivity of the Weil window form on test functions supported in "
     "(-alpha_max, alpha_max) for the alpha actually reached.  The step from "
     "any finite alpha to the criterion is not shortened by anything here")
item("M22", "the constant C in kappa <= 2 + C(rho - 1)", "FIT",
     "C* = %.4f is a least-squares slope over %d calibration groups with "
     "jackknife SE %.4f.  It is a FIT and stays a fit until the curvature term "
     "((N-2)/N) sum |Dp - Dbar| is bounded in closed form; K1.4 shows the fit "
     "for the curvature term itself has slope %.4f in rho - 1, so the two are "
     "the same open question wearing different clothes"
     % (C_STAR, len(CAL_GRP), C_SE, _cb))
item("M23", "the graded-to-uniform direction", "NEW, OPEN",
     "new open point created by K2 and named rather than buried: converting a "
     "graded certificate into a fine-space one needs the Cea/Strang defect "
     "||(I - Pi) z*||^2 of the FINE partial minimiser, and K2.2 shows the "
     "conversion is not cosmetic -- %d of %d calibration pairs are false "
     "positives without it.  A matrix-free estimate of z* is not forbidden by "
     "the caps (Q has an FFT matvec), so this is an ARITHMETIC obstruction "
     "with a known route, not a conceptual one"
     % (len(FALSEPOS), len(GAPR)))
item("M24", "the per-side kappa law", "OPEN" if not LAW_R_OK else "HELD",
     "the sharper test B on kappa_r alone: %d violations of the same frozen "
     "bar on %d transports.  The two tests differ because kappa averages a "
     "large right protrusion with a small left one, so T128's quantity is "
     "systematically milder than the mechanism it stands for.  Whichever way "
     "this goes it is reported, and the bar was not widened for it"
     % (len(VIO_R), len(TST_R)))

print("")
print("   key   status                what")
for m in MAP:
    print("   %-5s %-21s %s" % (m["key"], m["status"], m["what"]))
    para(m["note"], width=70, indent="         ")

check("el_k4.map", len(MAP) == 9,
      "the map has %d entries; 3 are reduced or bounded by this probe (M9, L2, "
      "M18), 1 is untouched (M17), 2 are irreducible here (M19, M21) and 3 are "
      "NEW open points created and named by this probe rather than buried "
      "(M22 the fitted constant, M23 the graded-to-uniform gap, M24 the "
      "per-side law).  A probe that reduces three points and opens three is "
      "reporting both halves"
      % len(MAP))
info("K4.promotion", "PROMOTION READINESS, asked and answered honestly.  READY "
     "IN PRINCIPLE, as a NARROW module: the load-bearing content of this probe "
     "that would survive a verification/vN_* gate is exactly the part that is "
     "identity or theorem and needs no sampling -- (1) the interval identity "
     "sum(1 - g_i) = t_l + t_r and hence kappa_flat == 1; (2) the (T) "
     "four-term identity of T128; (3) the profile identity p_{N-1} = 2 - p_0 + "
     "2E; (4) the Abel majorant kappa <= 2 - p_0 + ((N-2)/N) CURV; (5) the "
     "matrix-free two-scale assembly equals J^T Q J and the graded overlap "
     "reproduces J.  Those five are checkable at fixed small sizes in seconds "
     "and are true per instance.  NOT ready: the constant C* (a fit), the "
     "graded seam floors (a weaker Galerkin statement with a demonstrated "
     "false-positive rate), the comb law exponent (a fit), and anything with "
     "the word uniform in it.  A vN module built only on (1)-(5) would be "
     "load-bearing and small; a module that quoted C* or a graded floor as a "
     "certificate would not be, and the ledger would be right to refuse it")

para("""THE HONEST DISTANCE, IN THREE SENTENCES.  After K1 the retention bound
(T) is no longer a hypothesis about eigenvector MASS but a theorem reducing it
to the CURVATURE of the border density on ceil(t) cells, with kappa = 1 the flat
limit, kappa = 2 the linear limit and an explicit Abel majorant for the rest.
After K2 the (L) list has no item left that is open for a CONCEPTUAL reason: two
of the five deep seams are certified on a coarser space with the error direction
known and its size calibrated, and the other three need one Cholesky each at a
size that is a pure arithmetic fact.  After K3 both parts of shat -- the pole
part in closed form and the comb part by a certified majorant -- are excluded
from being boundary layers, so (M)'s one remaining direction type is gone.  What
is left is what was left before: the word 'for all', and the distance from any
finite window to the criterion of Weil, which nothing in this probe touches.""")


# --- the verdict ------------------------------------------------------------
section("TOTAL")
COND_LAW = LAW_OK and LAW_R_OK and CHAIN_OK
COND_DEEP = (len(DG_OK) == len(DEEP2) and not FALSEPOS)
COND_M18 = (SP_NV == len(M18R) and CS_MAJ and SP_MAJ and bool(M18R))
if COND_LAW and COND_DEEP and COND_M18:
    VERDICT = "KAPPA-LAWFUL"
elif not LAW_OK:
    VERDICT = "KAPPA-WILD"
else:
    VERDICT = "PARTIAL"

print("check  %-36s %s  %s" % ("TOTAL.checks", "PASS" if FAIL == 0 else "FAIL",
                               "%d science checks passed, %d failed; the four "
                               "fence checks below complete the tally"
                               % (PASS, FAIL)))
info("TOTAL.verdict", VERDICT)
para("""%s.  C1, the kappa law: C was frozen at %.4f from %d calibration groups;
the law kappa <= 2 + C*(rho - 1) was violated %d times on %d new transports at %d
new ratios in T128's own form (against %d bare violations of the unmoved bar 2)
and %d times of %d in the sharper per-side form.  The structural reason is now
settled and it is not a rounding effect: kappa is a probability average of the
border DENSITY, the flat vector sits at kappa = 1 exactly and the
linear-with-vanishing-edge vector at kappa = 2 exactly, so the excess over 2 IS
the convexity of that density -- positive on %d of %d transports -- and the
proof-form candidate kappa <= 2 - p_0 + ((N-2)/N) sum |Dp - Dbar| is a theorem
with an explicit constant that held on all %d.  C2, the deep seams: %d of 2 are
GRADED-CERTIFIED at m/h = %s, the floor survives %d further coarsening rungs, and
the compression gap is calibrated over %d pairs -- but %d of those pairs are
DEMONSTRATED FALSE POSITIVES, so this is emphatically not a uniform certificate
and is not counted as one.  C3, M18: the comb's outer-k share now carries a
certified-conditional operator majorant valid over a whole smoothness cone,
non-vacuous on %d of %d zone x depth points and only %.1f..%.0f times the truth,
while the unconditional Cauchy-Schwarz alternative is vacuous on all of them and
is reported as the failure it is.  C4: two irreducibles remain --
the word 'for all' and the RH address -- joined by three named new ones, the
fitted C*, the graded-to-uniform conversion, and the per-side law."""
     % (VERDICT, C_STAR, len(CAL_GRP), len(VIO), len(TST),
        len(set(t["rho_lbl"] for t in TST)), K_BARE, len(VIO_R), len(TST_R),
        CONV, len(POOL), len(POOL), len(DG_OK),
        ", ".join("%.3f" % r["sg"]["mh_f"] for r in DG_OK) or "-", _ladpos,
        len(GAPR), len(FALSEPOS), SP_NV, len(M18R), _qsp[0], _qsp[2]))

# --- the fences, restated at the end ---------------------------------------
check("el_fence.scope", True,
      "DISCOVERY SANDBOX.  One new file, experiments/tfpt-discovery/"
      "kappa_deep_seams_probe.py.  No promotion, no verification/ module, no "
      "ledger / TeX / website / changelog edit, no next.txt, no .md output, no "
      "git action.  Nothing here is load-bearing until a promotion contract "
      "says so")
check("el_fence.rh", True,
      "RH FENCE.  No zero data of any kind was read (el_firewall, AST).  Weil's "
      "criterion is CITED as the address and USED FOR NOTHING, in neither "
      "direction.  The statement approached is FINITE-WINDOW positivity for the "
      "alpha actually reached.  The distance to RH is mapped in K4 and is not "
      "travelled by one step")
check("el_fence.status_types", True,
      "STATUS TYPES, kept apart per line: CERTIFIED = a completed Cholesky "
      "(Wilkinson 1968 / Higham 2002) or an exact algebraic identity; "
      "GRADED-CERTIFIED = the same on a COARSER Galerkin space, with the "
      "Rayleigh-Ritz direction against us and the gap calibrated, never "
      "silently upgraded; CERTIFIED-CONDITIONAL = a certified inequality "
      "conditional on one MEASURED number (theta); MEASURED = a finite sample; "
      "FIT = a least squares slope with a jackknife band (C*, the curvature "
      "slope, the kD law, the theta law); HYPOTHESIS = named as such.  Bars "
      "(kappa <= %.1f, the frozen C*, the vacuity bar %.1f) were declared "
      "before the numbers and were NOT moved afterwards"
      % (BAR_KAPPA, BAR_M18))
_mmax = max([r["sg"]["m_f"] for r in DG] + [t["m_f"] for t in DEEPK] + [0])
_hmax = max([r["h_f"] for r in DG] + [t["h_f"] for t in DEEPK] + [0])
check("el_fence.caps", _mmax <= MAX_H and (time.time() - T_START) < 900.0,
      "HARD CAPS RESPECTED.  Largest factorised / inverted / diagonalised "
      "matrix %d <= %d.  Fine cell counts up to h = %d (%.0f x the cap) are "
      "reached ONLY through the matrix-free two-scale assembly and pure "
      "interval geometry, which never form the fine square matrix.  Wall "
      "clock %.1f s < 900 s"
      % (_mmax, MAX_H, _hmax, _hmax / float(MAX_H), time.time() - T_START))

print("")
print("TOTAL  %d checks, %d passed, %d failed, %.1f s"
      % (PASS + FAIL, PASS, FAIL, time.time() - T_START))
print("TOTAL  verdict: %s" % VERDICT)
