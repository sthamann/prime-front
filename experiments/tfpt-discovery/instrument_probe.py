r"""Discovery probe (2026-07-26), part 103 of the zeta/prime investigation.
Contract INSTRUMENT -- door C, the TOOLMAKING door.

THE SITUATION T101 LEFT
  T101 ran the race of the staircase induction over 16 zones and found a clean
  separation:
    * the PRIMITIVE quantities are FLAT.  The target inequality D_k <= mu_k/2
      never fails (64/64 samples), the relative margin 1 - D_k/(mu_k/2) has
      log-slope -0.009..-0.021 per zone with standard errors 0.05..0.10, and
      the handoff window relative to the atom spacing has slope +0.002 +- 0.178.
    * the INSTRUMENT loses.  The two-factor sufficient condition
          rho <= rho_true + R_G / Lam        (T98 uniform bulk remainder)
      needs the threshold Lam_ok = R_G / (1 - rho) to sit inside the available
      spectrum [lam_bot, lam_top] of the smaller window.  The supply lam_top is
      FLAT (7.0..7.9), but the demand Lam_ok grows, because R_G climbs
      0.49 -> 2.16 while the slack S = 1 - rho falls 0.209 -> 0.006..0.044.  The
      race ratio r_k = S_k / B_k = lam_top / Lam_ok falls with log-slope
      -0.162 +- 0.056 (systematic band [-0.181, -0.144] over four matched wing
      fractions), and only zone n = 2 closes throughout.
  T100 built the repair kit for a single zone: the L1 TAIL PROJECTION (keep the
  induction data instead of throwing it away with Bessel),
      W  =  sum_j lam_j^-1 g_j g_j^T
         <= L_Lam + (1/Lam) (G^T G - S_Lam),   m(Lam) := lam_max(G^T G - S_Lam),
  which is COMPLETE (b_tail -> rho exactly at Lam = lam_top), plus the BAND
  form: above Lam_0 use geometric bands with weight 1/(lower band edge), so the
  cost of the instrument is two CONTINUUM numbers (Lam_0, B) instead of a
  grid-dependent mode count.  T100 closed 24/24 samples in zones n = 2..5 with
  Lam_ok = 0.47..2.80 and B = 4..16.  T99 measured the spectral decay of the
  coupling mass, theta = 1.15..2.18 in zones 4..5.

WHAT THIS PROBE DOES
  It builds the T100 instrument at T101 scale and RE-RUNS THE T101 RACE with
  it, over all 16 zones and all four matched wing fractions.  The question is
  not whether the instrument closes one zone -- it is whether its DEMAND grows
  over the zones faster than the flat supply.

  I1  THETA-WEIGHTED, CERTIFIED BAND SUM.  Instead of a uniform 1/Lam bulk,
      partition the spectrum of the smaller window above Lam_0 into geometric
      bands and weight each band by 1 / (its lower edge).  The coupling mass of
      band b is the EXACT spectral projection object
          P_b = sum_{lam_j in band b} z_j z_j^T ,   z_j = <mode j| Q_0- A_sh^-1/2,
      measured by Parseval on the Q_00 eigenbasis (finitely many operator-valued
      numbers per zone -- T100's lesson: do not throw the induction data away).
      The instrument is  [exact band masses up to Lam_max] + [rest above Lam_max
      with weight 1/Lam_max (Bessel)].  Every weight obeys w_j >= 1/lam_j, so
      the resulting bound is CERTIFIED given the data (spectral calculus, no
      fit).  The new race quantity is the demand carried by those band masses:
          raw mass    sum_b ||P_b||         (this is >= R_G and must grow)
          weighted    sum_b ||P_b|| / Lam_b (this is what the bound pays)
      Reported with the measured band decay exponent theta (band mass vs band
      edge) against the T99 anchor 1.15..2.18.
  I2  THE FULL m(Lam) EXPLOITATION.  Zone-adaptive threshold: per zone the
      least CONTINUUM threshold Lam_ok^tail at which
          b_tail(Lam) = lam_max( L_Lam + (T_all - S_Lam)/Lam )  <=  1
      (bisected on the threshold, never on a mode index), together with the
      Pareto pair (Lam_0, largest admissible band ratio r_max) and the band
      count B it implies.  Question: does Lam_ok^tail stay BOUNDED over the 16
      zones?  If yes the instrument is k-uniform with finite data per zone.
  I3  THE RACE REDONE.  For all three instruments -- T101 uniform, I2 tail,
      I1 band -- the SAME race ratio in threshold form,
          r_k = lam_top / Lam_ok ,
      which for the T101 family is identically its S_k / B_k, so the three are
      directly comparable.  Slopes over 16 zones and four matched fractions
      against the T101 anchor -0.162, the closure map of a FIXED k-uniform
      instrument (Lam_0 = 3, r = 2 -- finite data by construction), grid drift,
      and the certified / induction-data / measured ledger.
  I4  SYNTHESIS.  The structural floor: every instrument of this shape bounds
      rho from above, so closure needs its relative excess over rho to be at
      most the slack S = 1 - rho.  S is measured over the zones; if it falls,
      NO fixed-precision instrument of this family is k-uniform, and the honest
      answer is which object class door C needs instead.  Two measured
      pointers, not assertions: (a) the numerical effective rank trace/||.|| of
      the bulk operator, absolute and as a fraction of dim E_-; (b) a direct
      test of the finite-rank route inside the same certified family -- keep
      the ntop heaviest bulk modes at their exact weight 1/lam_j and band the
      rest (still w_j >= 1/lam_j, still certified, ntop extra numbers per
      zone).  If a FIXED small ntop flattens the race, the missing object is a
      handful of directions; if its gain decays to 1 exactly where the race is
      tight, that route is closed and the obstruction is on the other side.

PREREGISTERED VERDICTS
  INSTRUMENT-UNIFORM  : the log-slope of the best r_k over the 16 zones is
      >= -0.05 AND consistent with zero at 2 s.e. AND the fixed instrument
      (Lam_0 = 3, r = 2) closes >= 12/16 zones at every matched fraction.  The
      toolmaking problem is solved and only door A remains.
  INSTRUMENT-IMPROVED : the slope is clearly flatter than the T101 band
      (> -0.106 = -0.162 + 0.056) but still negative at 2 s.e.  The won factor
      is named.
  FAMILY-EXHAUSTED    : neither -- the family cannot be made uniform; why, and
      which object class comes next.
  Element gates: el_firewall, el_kernel, el_forms, el_chain, el_repro, el_i1,
  el_theta, el_i2, el_i3, el_map, el_drift, el_i4, el_budget.

OUTCOME OF THIS RUN  =>  INSTRUMENT-IMPROVED by a factor 2.2 in the race slope
                         and 3x..103x in the demand -- but the toolmaking
                         problem is only HALF solved, and the half that
                         remains is on the OTHER SIDE of the induction step.
  29 checks, 0 failures, 32 s, largest array 2000^2, 16 zones x 4 matched wing
  fractions (64 samples) at T101's own resolution M = 1600 / 2000, so every
  comparison below is like for like.  The T101 race is reproduced to the
  digit: log-slope -0.1622 +- 0.0562 here against -0.162 +- 0.056 there, and
  the T100 thresholds reproduce as well (zones n = 2..5 give Lam_ok^tail =
  0.77, 1.21, 1.37, 1.60 inside T100's 0.47..2.80).
  I1  The band instrument is real and CERTIFIED: every band weight obeys
      w_j >= 1/lam_j at every sample, the ordering rho <= b_band <= b_tail <=
      b_t99 holds at 64/64 samples, and the parity-blind form equals the max
      over the two parity channels to 2.9e-14 with a channel leak of 2.0e-15
      (T100 reproduced), so the data halves for free.  Two decay exponents are
      measured and they disagree in an instructive way: the band mass DENSITY
      falls like Lam^-theta with theta = 0.34..1.51 (median 0.74), FLATTER
      than the T99 zone-4/5 anchor 1.15..2.18, while the defect tail function
      m(Lam) = lam_max(T_all - S_Lam) falls like Lam^-p with p = 0.97..1.40
      (median 1.19), just above T100's 0.50..1.17.  The consequence is the
      one that matters for the race: the raw band-mass sum grows over the 16
      zones with log-slope +0.1151 +- 0.0181 and the theta-WEIGHTED demand
      grows almost identically, +0.1063 +- 0.0242.  The weighting removes a
      factor 1.14 out of a total growth of 5.62.  Weighting the bulk by its
      own measured decay does not buy k-uniformity.
  I2  The m(Lam) family exploited to its end gives the big win.  Lam_ok^tail
      is BOUNDED over all 16 zones and all four fractions: 0.771..3.640, with
      log-slope +0.0806 +- 0.0109, against Lam_ok^T101 = 2.3..376.  The
      demand-reduction factor is 3.0x..103.4x.  But the bound is not free and
      the honest currency is the data: the explicit modes below Lam_ok grow
      2 -> 232 (log-slope +0.2976 +- 0.0306) because dim E_0 itself grows
      1028 -> 1570 as the wing narrows, so a bounded threshold hides an
      unbounded mode count.  The Pareto front (Lam_0, r_max) shows the same
      thing in continuum currency: at the fixed threshold Lam_0 = 1 the
      admissible band ratio collapses from 8.0 to 1.012 and the band count
      runs 1 -> 133 with log-slope +0.1993 +- 0.0545.
  I3  The race redone, in the one currency all three instruments share
      (r_k = lam_top / Lam_ok, which for the T101 family is identically its
      S_k / B_k):  T101 uniform -0.1622 +- 0.0562, I2 tail -0.0748 +- 0.0116
      (systematic band [-0.0754, -0.0730] over the four fractions), I1 band
      -0.0839 +- 0.0151.  The best instrument is therefore 2.2x flatter than
      T101's, r_k^tail falls only 9.33 -> 2.70 and never below 2.0, i.e. it
      NEVER leaves the spectrum, whereas T101's falls 3.06 -> 0.15 and leaves
      it at zone 3.  The closure map of a FIXED k-uniform instrument
      (Lam_0 = 3, r = 2, no zone-dependent tuning) is 16/16, 12/16, 9/16,
      7/16 over the four fractions = 44/64 samples, against 7/64 for the T101
      family in the same currency.  Grid honesty: the threshold drifts <=
      5.8%, the race ratio <= 5.2%, the supply lam_top <= 7.9% (it is not a
      continuum object -- T100 C1), the mode count <= 19% (it is the grid
      shadow of the threshold).  The boundedness of Lam_ok does not use
      lam_top at all.
  I4  What is left is NOT an instrument defect.  Every bound here sits above
      rho, so closure needs relative excess <= S = 1 - rho.  The excess of the
      fixed band instrument grows +0.1786 +- 0.0313 while S falls -0.0791 +-
      0.0474 (0.2091 -> 0.0392); the two have ALREADY crossed inside the
      measured range (tightest headroom 0.32x, over budget in 4/16 zones), and
      the T101 primitive 1 - D_k/(mu_k/2) stays flat (-0.0156 +- 0.0701),
      exactly as T101 found.  The object-class question is then answered by
      two measurements rather than by a recommendation.  First, the bulk
      operator is NOT low-rank relative to the wing: effective rank
      1.91..36.10, i.e. 0.007..0.579 of dim E_- (median 0.336), rising
      +0.0144 +- 0.0067.  Second, and decisively, the finite-rank route is
      tested inside the same certified family: keeping the 8 heaviest bulk
      modes exact gains 285x at n = 4 and a median 10.2x in the lower half of
      the zones, but only 1.09x in the upper half, with the gain decaying
      -0.2143 +- 0.0811 per zone.  A fixed finite-rank correction helps
      exactly where the race was already won and does nothing where it is
      tight.  So door C's remaining obstruction is not a weighting of the E_0
      bulk at all: it is the near-saturation of the pencil A_sh - W on the
      WING side, and the object class that can address it is one adapted to
      the near-null direction on E_- (a prolate / Slepian basis concentrated
      on the wing pair, T96) or the equality argument of Fredholm-alternative
      shape that T100 typed at the zone top.
  Read plainly: T101's obstruction WAS partly an instrument artefact and the
  instrument is now much better -- bounded threshold demand, 44/64 closure,
  2.2x flatter slope -- but the residual fall is driven by the collapse of the
  slack towards the zone tops, which no upper bound of this shape can outrun,
  and the bulk-side repairs are now measured to be exhausted.

FENCES
  * Discovery sandbox.  No promotion, no ledger / TeX / website / changelog
    edit, no load-bearing module, no roadmap edit, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, network imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  A negative
    lambda_min on a genuine window direction is an IMPLEMENTATION SIGNAL,
    fenced, never reported as mathematics.
  * lambda_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute positivity, never prove it.  Every quantity
    proposed as a continuum object is reported with its grid drift, and mode
    counts are labelled as the grid-dependent shadow of a threshold.
  * No "proved" language without a certificate.  Three status labels, never
    mixed:  CERTIFIED (an operator inequality with a closed-form or classical
    justification, valid for whatever data is supplied), INDUCTION-DATA (an
    exact discrete object of the smaller window -- the same footing T99's R_G
    stands on, grid drift reported), MEASURED (needs the full discrete
    spectrum; a signal, never an ingredient).
  * Classical anchors cited, not re-derived: Weil 1952, the digamma
    archimedean kernel, Rayleigh-Ritz, Paley-Wiener, Parseval/Bessel, the
    Schur test, Schur complements, centrosymmetric block diagonalisation
    (Cantoni-Butler 1976), Slepian-Pollak-Landau prolate concentration (cited
    as the SHAPE of the recommended next object class, not implemented as a
    proof), and the Fredholm alternative (T100's typing of the zone top).
"""
import ast
import math
import time

import mpmath
import numpy as np
from numpy.lib.stride_tricks import as_strided
from scipy.linalg import eigh, eigvalsh

PASS = 0
FAIL = 0
T_START = time.time()
mpmath.mp.dps = 30

EULER = float(mpmath.euler)
LOG_PI = math.log(math.pi)
LOG2 = math.log(2.0)
K0_CLOSED = -EULER - 3.0 * LOG2 - math.pi / 2.0 - LOG_PI
SQ2 = math.sqrt(2.0)

MAX_ARRAY = 2000
BUDGET_S = 860.0
MAXN_SEEN = 0

# ---- resolution (T101's M_K2 / M_K2_DRIFT, so the race is comparable) -------
M_MAIN = 1600                       # main 16-zone x 4-fraction sweep
M_DRIFT = 2000                      # grid-drift rung (largest array)
WING_FRACTIONS = (0.25, 0.50, 0.75, 0.95)
FRAC_REF = 1                        # index of the reference fraction (0.50)
N_ZONES = 16                        # zones k = 1..16, i.e. n_k = 2 .. 29
BISECT_STEPS = 14                   # geometric bisection on the THRESHOLD

# ---- the instrument constants (all continuum objects) -----------------------
BAND_R = 2.0                        # band ratio of the fixed instrument
BAND_LAM0_FIX = 3.0                 # fixed threshold of the k-uniform instrument
THETA_LAM0 = 0.5                    # band floor used for the theta measurement
THETA_R = 1.6                       # band ratio used for the theta measurement
LAM0_LADDER = (0.5, 1.0, 2.0, 3.0)  # Pareto ladder for the (Lam_0, r_max) front
FIXED_THRESHOLDS = (2.0, 3.0, 6.0)  # map thresholds
NTOP_LADDER = (2, 8)                # finite-rank correction: extra exact modes

# ---- the T101 anchors this probe races against ------------------------------
T101_SLOPE = -0.162
T101_SE = 0.056
T101_FLAT_BAND = T101_SLOPE + T101_SE      # -0.106, the "clearly flatter" line
T99_THETA = (1.15, 2.18)                   # T99 spectral decay, zones 4-5
T100_P = (0.50, 1.17)                      # T100 defect tail m(Lam) ~ Lam^-p
T100_LAM_OK = (0.47, 2.80)                 # T100 closure thresholds, zones 1-4

GLX, GLW = np.polynomial.legendre.leggauss(24)

# (n, log n, log p, mu_n = 2 Lambda(n)/sqrt(n)) -- prime powers only.
_PP = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3),
       (11, 11), (13, 13), (16, 2), (17, 17), (19, 19), (23, 23),
       (25, 5), (27, 3), (29, 29), (31, 31), (32, 2), (37, 37)]
ATOMS = tuple((n, math.log(n), math.log(p), 2.0 * math.log(p) / math.sqrt(n))
              for n, p in _PP)
N_OF = [a[0] for a in ATOMS]
LOGN = [a[1] for a in ATOMS]
MU = [a[3] for a in ATOMS]
ALPHA_ENTRY = [x / 2.0 for x in LOGN]


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-30s %s  %s" % (name, "PASS" if ok else "FAIL", detail),
          flush=True)
    return bool(ok)


def info(msg):
    print("info   %s" % msg, flush=True)


def head(msg):
    print("\n%s\n%s" % (msg, "-" * min(78, max(20, len(msg)))), flush=True)


def note_array(n):
    global MAXN_SEEN
    if n > MAXN_SEEN:
        MAXN_SEEN = n


def ols(x, y):
    """slope, slope stderr, intercept, R2 for y = a + b x."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = x.size
    if n < 3 or not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        return float("nan"), float("nan"), float("nan"), float("nan")
    X = np.column_stack([np.ones(n), x])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    r = y - X @ beta
    dof = n - 2
    s2 = float(r @ r) / dof if dof > 0 else float("nan")
    cov = s2 * np.linalg.inv(X.T @ X)
    sst = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - float(r @ r) / sst if sst > 0 else float("nan")
    return float(beta[1]), math.sqrt(max(cov[1, 1], 0.0)), float(beta[0]), r2


# ============================================================ I0  firewall
def firewall():
    head("I0    AST firewall (zero-free, sandbox-only, read-only)")
    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)

    banned_mod = {"urllib", "urllib2", "requests", "socket", "http", "ftplib",
                  "telnetlib", "subprocess", "sympy", "pandas", "shutil"}
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                mods.add(a.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                mods.add(node.module.split(".")[0])
    check("el_firewall.imports", not (mods & banned_mod), "modules=%s"
          % sorted(mods))

    # tokens assembled at runtime so that the scanner cannot match itself
    body = src.split('"""', 2)[2] if src.count('"""') >= 2 else src
    lowered = body.lower()
    zero_tokens = tuple("".join(p) for p in (
        ("zeta", "zero"), ("riemann_", "zero"), ("zero_", "table"),
        ("odly", "zko"), ("lm", "fdb"), ("gram_", "point"),
        ("zeros_of_", "zeta"), ("nontrivial_", "zero"), ("zero", "s.dat"),
        ("14.13", "4725"), ("21.02", "2039")))
    hits = [t for t in zero_tokens if t in lowered]
    check("el_firewall.no_zero_data", not hits, "hits=%s" % hits)

    writes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "open":
            mode = None
            if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                mode = node.args[1].value
            for kw in node.keywords:
                if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                    mode = kw.value.value
            if mode is None or any(c in str(mode) for c in "wax+"):
                writes.append(mode)
    check("el_firewall.read_only", not writes, "open modes=%s" % writes)

    forbidden_paths = tuple("".join(p) for p in (
        ("verifi", "cation/"), ("status_", "ledger"), ("change", "log"),
        ("next", ".txt"), ("web", "site/"), ("tex-", "artefacts")))
    path_hits = [p for p in forbidden_paths if p in body]
    check("el_firewall.sandbox_only", not path_hits, "paths=%s" % path_hits)


# ================================================== instrument assembly
def sym(A):
    return 0.5 * (A + A.T)


def lmax(A):
    n = A.shape[0]
    if n == 0:
        return 0.0
    return float(eigvalsh(A, subset_by_index=[n - 1, n - 1],
                          check_finite=False)[0])


def gram_lmax(Zb):
    """lam_max(Zb^T Zb) via the cheaper of the two Gram matrices."""
    r, c = Zb.shape
    if r == 0 or c == 0:
        return 0.0
    return lmax(sym(Zb @ Zb.T)) if r < c else lmax(sym(Zb.T @ Zb))


def sym_toep(c):
    """Symmetric Toeplitz view with first column c (no O(n^2) index work)."""
    n = c.size
    full = np.concatenate((c[::-1], c[1:]))
    s = full.strides[0]
    return as_strided(full[n - 1:], shape=(n, n), strides=(-s, s))


def arch_lags(M, dx):
    """Lag vector of the archimedean PWC Toeplitz block (depends only on dx).

    Classical digamma integral representation
        psi(s) = -gamma + int_0^inf (e^-v - e^-sv)/(1 - e^-v) dv,
    moved to u-space, singular cell resolved in closed form."""
    u0 = 0.5 * dx * (GLX + 1.0)
    w0 = 0.5 * dx * GLW
    num = np.exp(-0.5 * u0) * (np.expm1(-1.5 * u0) + u0 / dx)
    den = -np.expm1(-2.0 * u0)
    g0 = float(np.sum(w0 * 2.0 * num / den)) - math.log(-math.expm1(-2.0 * dx))
    s = np.concatenate([0.5 * dx * (GLX - 1.0), 0.5 * dx * (GLX + 1.0)])
    ws = np.concatenate([0.5 * dx * GLW, 0.5 * dx * GLW])
    tri = 1.0 - np.abs(s) / dx
    m = np.arange(1, M, dtype=float)
    U = m[:, None] * dx + s[None, :]
    val = np.exp(-0.5 * U) / (-np.expm1(-2.0 * U))
    g = np.empty(M)
    g[0] = g0 - (EULER + LOG_PI)
    g[1:] = -np.sum((ws * tri)[None, :] * val, axis=1)
    return g


def atom_lags(M, dx, u):
    """Lag vector of the symmetric PWC autocorrelation Toeplitz S(u)."""
    lag = np.arange(M, dtype=float) * dx
    t1 = np.maximum(0.0, 1.0 - np.abs(lag - u) / dx)
    t2 = np.maximum(0.0, 1.0 - np.abs(lag + u) / dx)
    return 0.5 * (t1 + t2)


def pole_vecs(M, dx, alpha):
    x = -alpha + dx * np.arange(M, dtype=float)
    a = (2.0 / math.sqrt(dx)) * (np.exp(0.5 * (x + dx)) - np.exp(0.5 * x))
    b = (2.0 / math.sqrt(dx)) * (np.exp(-0.5 * x) - np.exp(-0.5 * (x + dx)))
    return a, b


def build_Q(M, alpha, atom_idx):
    note_array(M)
    dx = 2.0 * alpha / M
    c = arch_lags(M, dx)
    for j in atom_idx:
        c -= MU[j] * atom_lags(M, dx, LOGN[j])
    Q = np.array(sym_toep(c))
    a, b = pole_vecs(M, dx, alpha)
    Q += np.outer(a, b)
    Q += np.outer(b, a)
    return Q


def parity_basis(n):
    """Centrosymmetric block diagonalisation (Cantoni-Butler 1976)."""
    h = n // 2
    odd = n % 2
    Be = np.zeros((n, h + odd))
    Bo = np.zeros((n, h))
    for i in range(h):
        Be[i, i] = Be[n - 1 - i, i] = 1.0 / SQ2
        Bo[i, i] = 1.0 / SQ2
        Bo[n - 1 - i, i] = -1.0 / SQ2
    if odd:
        Be[h, h] = 1.0
    return Be, Bo


# ================================================== I0b  validation
def validate_instrument():
    head("I0b   instrument validation (kernel and forms, independent routes)")

    def psi_rep(t):
        f = lambda v: (mpmath.e ** (-v) - mpmath.e ** (-v / 4)
                       * mpmath.cos(t * v / 2)) / (1 - mpmath.e ** (-v))
        return float(-mpmath.euler + mpmath.quad(f, [0, 1, 10, 60, 250, 800]))

    e0 = abs(psi_rep(0.0) - float(mpmath.digamma(0.25)))
    e1 = abs(psi_rep(1.7) - float(mpmath.re(mpmath.digamma(0.25 + 0.85j))))
    e2 = abs((float(mpmath.digamma(0.25)) - LOG_PI) - K0_CLOSED)
    check("el_kernel.psi_representation", e0 < 1e-10 and e1 < 1e-10 and e2 < 1e-12,
          "err %.2e / %.2e, k(0) closed form %.2e" % (e0, e1, e2))

    # flat-window closed forms: the three blocks against independent routes
    alpha = 0.62
    M = 800
    dx = 2.0 * alpha / M
    c = np.ones(M) / math.sqrt(M)               # the flat unit-norm window

    # arch, route 1: the PWC lag vector, contracted with the flat window
    g = arch_lags(M, dx)
    mlag = np.arange(1, M, dtype=float)
    a_arch = float(M * g[0] + 2.0 * np.sum((M - mlag) * g[1:])) / M
    # arch, route 2: the SPECTRAL definition (1/2pi) int |fhat|^2 k(t) dt with
    # the panels placed on the zeros of sin(alpha t) (the integrand oscillates)
    al = mpmath.mpf(alpha)
    kfun = lambda t: mpmath.re(mpmath.digamma(0.25 + 0.5j * t)) - LOG_PI
    fh2 = lambda t: 2.0 * (mpmath.sin(al * t) ** 2) / (al * t * t)
    per = mpmath.pi / al
    pts = [mpmath.mpf(0)] + [n * per for n in range(1, 121)]
    core = mpmath.quad(lambda t: fh2(t) * kfun(t), pts)
    T = 120 * per
    tail = mpmath.quad(lambda t: kfun(t) / (al * t * t), [T, 10 * T, mpmath.inf])
    ref_spec = float(2.0 * (core + tail) / (2 * mpmath.pi))
    # arch, route 3: the u-space identity with the EXACT triangle h(u)
    htri = lambda u: max(0.0, 1.0 - u / (2.0 * alpha))
    fu = lambda u: (mpmath.e ** (-2 * u) - htri(u) * mpmath.e ** (-u / 2)) \
        / (1 - mpmath.e ** (-2 * u))
    ref_u = float(-(EULER + LOG_PI) + 2 * mpmath.quad(
        fu, [0, 1e-3, 0.1, 1, 2 * alpha, 2 * alpha + 1, 10, 60, mpmath.inf]))
    check("el_forms.arch_flat_window",
          abs(a_arch - ref_spec) < 1e-6 and abs(a_arch - ref_u) < 1e-9,
          "PWC %.10f vs spectral %.10f vs u-space identity %.10f"
          % (a_arch, ref_spec, ref_u))

    pa, pb = pole_vecs(M, dx, alpha)
    p_pwc = 2.0 * float(pa @ c) * float(pb @ c)
    ip = 4.0 * math.sinh(alpha / 2.0) / math.sqrt(2.0 * alpha)
    check("el_forms.pole_closed_form", abs(p_pwc - 2.0 * ip * ip) < 1e-11,
          "PWC %.12f vs 2 (int f e^{x/2})(int f e^{-x/2}) %.12f"
          % (p_pwc, 2.0 * ip * ip))

    u = 0.5493061443
    S = np.array(sym_toep(atom_lags(M, dx, u)))
    h_pwc = float(c @ (S @ c))
    h_ref = (2.0 * alpha - u) / (2.0 * alpha)
    check("el_forms.atom_autocorrelation", abs(h_pwc - h_ref) < 1e-12,
          "h_f(u) PWC %.12f vs exact (2a-u)/2a %.12f" % (h_pwc, h_ref))


# ================================================== the bound family
def explicit_part(lamk, Z, J):
    """L_Lam = sum_{j<J} lam_j^-1 z_j z_j^T  -- the kept induction data."""
    mw = Z.shape[1]
    if J <= 0:
        return np.zeros((mw, mw))
    Zl = Z[:J]
    return sym((Zl / lamk[:J, None]).T @ Zl)


def tail_bound(lamk, Z, T_all, Lam):
    """T100 L1: rho <= lam_max(L_Lam + (T_all - S_Lam)/Lam).  CERTIFIED."""
    J = int(np.searchsorted(lamk, Lam, side="left"))
    L = explicit_part(lamk, Z, J)
    S = sym(Z[:J].T @ Z[:J]) if J > 0 else np.zeros_like(L)
    return lmax(sym(L + (T_all - S) / Lam))


def t99_bound(lamk, Z, R_G, Lam):
    """T99/T98 family: lam_max(L_Lam) + R_G/Lam (Bessel on the bulk)."""
    J = int(np.searchsorted(lamk, Lam, side="left"))
    return lmax(explicit_part(lamk, Z, J)) + R_G / Lam


def band_weights(hi, Lam0, r, Lam_max=None):
    """w_j = 1/(lower edge of j's band), capped by the 1/Lam_max Bessel tail."""
    idx = np.floor(np.log(hi / Lam0) / math.log(r)).astype(np.int64)
    np.maximum(idx, 0, out=idx)
    w = 1.0 / (Lam0 * r ** idx)
    if Lam_max is not None:
        w = np.where(hi >= Lam_max, 1.0 / Lam_max, w)
    return w, idx


def band_bound(lamk, Z, Lam0, r, Lam_max=None, want_wcheck=False):
    """I1: explicit modes below Lam_0, exact band masses above, Bessel tail.

    Every weight obeys w_j >= 1/lam_j (spectral calculus), so the bound is
    CERTIFIED given the data; band EDGES are continuum objects, mode indices
    are not."""
    J = int(np.searchsorted(lamk, Lam0, side="left"))
    B = explicit_part(lamk, Z, J)
    hi = lamk[J:]
    nb = 0
    wok = True
    if hi.size:
        w, idx = band_weights(hi, Lam0, r, Lam_max)
        nb = int(np.unique(idx[hi < (Lam_max if Lam_max else np.inf)]).size)
        if Lam_max is not None and np.any(hi >= Lam_max):
            nb += 1
        if want_wcheck:
            wok = bool(np.all(w >= 1.0 / hi - 1e-13))
        Zh = Z[J:] * np.sqrt(w)[:, None]
        B = B + sym(Zh.T @ Zh)
    return lmax(sym(B)), nb, J, wok


def topmode_bound(lamk, Z, Lam0, r, ntop):
    """I1 with a FINITE-RANK correction: the ntop heaviest modes above Lam_0
    keep their exact weight 1/lam_j, everything else is banded.

    Still w_j >= 1/lam_j everywhere, so still CERTIFIED; the extra data is
    ntop modes per zone, a k-uniform amount if ntop is fixed."""
    J = int(np.searchsorted(lamk, Lam0, side="left"))
    B = explicit_part(lamk, Z, J)
    hi = lamk[J:]
    if hi.size:
        Zh = Z[J:]
        w = band_weights(hi, Lam0, r)[0]
        if ntop > 0:
            nz = np.einsum("ij,ij->i", Zh, Zh)
            top = np.argsort(nz)[::-1][:min(ntop, nz.size)]
            w[top] = 1.0 / hi[top]
        Zw = Zh * np.sqrt(w)[:, None]
        B = B + sym(Zw.T @ Zw)
    return lmax(sym(B))


def band_masses(lamk, Z, Lam0, r):
    """Exact coupling mass per band (Parseval on the Q_00 eigenbasis)."""
    J = int(np.searchsorted(lamk, Lam0, side="left"))
    hi = lamk[J:]
    if hi.size == 0:
        return [], [], []
    _, idx = band_weights(hi, Lam0, r)
    masses, edges, counts = [], [], []
    for b in range(int(idx.max()) + 1):
        selection = idx == b
        cnt = int(selection.sum())
        if cnt == 0:
            continue
        masses.append(gram_lmax(Z[J:][selection]))
        edges.append(Lam0 * r ** b)
        counts.append(cnt)
    return masses, edges, counts


def bisect_threshold(fun, lo, hi, steps=BISECT_STEPS):
    """Least CONTINUUM threshold with fun(Lam) <= 1 (geometric bisection)."""
    if fun(lo) <= 1.0:
        return lo, True
    if fun(hi) > 1.0:
        return float("inf"), False
    for _ in range(steps):
        mid = math.sqrt(lo * hi)
        if fun(mid) <= 1.0:
            hi = mid
        else:
            lo = mid
    return hi, False


# ================================================== the zone sample
def zone_alpha(u, M, mw):
    return u * M / (2.0 * (M - mw))


def mw_max_of(k, M):
    u = LOGN[k]
    return int(M * (1.0 - u / (2.0 * ALPHA_ENTRY[k + 1])) * 0.97)


def analyse(k, M, mw, deep=False, parity=False):
    """One (zone, wing width) sample: all three instruments, one eigensolve."""
    u = LOGN[k]
    alpha = zone_alpha(u, M, mw)
    if alpha >= ALPHA_ENTRY[k + 1] - 1e-9 or mw < 6 or 2 * mw >= M - 8:
        return None
    old = [j for j in range(k) if LOGN[j] <= 2.0 * alpha + 1e-15]
    Q = build_Q(M, alpha, old)
    Ls, Rs, Cs = slice(0, mw), slice(M - mw, M), slice(mw, M - mw)

    Qmm = sym(0.5 * (Q[Ls, Ls] - Q[Ls, Rs] - Q[Rs, Ls] + Q[Rs, Rs]))
    X = (Q[Cs, Ls] - Q[Cs, Rs]) / SQ2
    Q00 = sym(np.array(Q[Cs, Cs]))
    par_res = float(np.linalg.norm(X[::-1, ::-1] + X)
                    / max(np.linalg.norm(X), 1e-300))

    lam, V = eigh(Q00, check_finite=False)
    lam_top = float(lam[-1])
    keep = lam > 1e-12 * lam_top
    lamk = np.ascontiguousarray(lam[keep])
    Y = np.ascontiguousarray(V[:, keep].T @ X)

    mu_half = 0.5 * MU[k]
    W_raw = sym((Y / lamk[:, None]).T @ Y)
    D = -float(eigvalsh(Qmm - W_raw, subset_by_index=[0, 0],
                        check_finite=False)[0])
    A_sh = Qmm + mu_half * np.eye(mw)
    aw, AV = eigh(A_sh, check_finite=False)
    if aw[0] <= 1e-13:
        return None
    Ai = (AV * aw ** -0.5) @ AV.T
    Z = Y @ Ai
    T_all = sym(Z.T @ Z)
    R_G = lmax(T_all)
    rho = lmax(sym((Z / lamk[:, None]).T @ Z))
    S = 1.0 - rho

    out = dict(k=k, n=N_OF[k], M=M, mw=mw, alpha=alpha, delta=2.0 * alpha - u,
               n_old=len(old), dim0=int(lamk.size), lam_top=lam_top,
               lam_bot=float(lamk[0]), mu_half=mu_half, D=D, rho=rho, R_G=R_G,
               S=S, rel_margin=1.0 - D / mu_half, par_res=par_res,
               equiv=bool((rho <= 1.0) == (D <= mu_half)))

    # --- the three instruments, all in threshold currency ------------------
    lo = max(0.5 * float(lamk[0]), 1e-3)
    hi = lam_top
    out["lam_ok_t101"] = (R_G / S) if S > 0 else float("inf")
    out["r_t101"] = lam_top / out["lam_ok_t101"] if S > 0 else 0.0

    lok_tail, floor_tail = bisect_threshold(
        lambda L: tail_bound(lamk, Z, T_all, L), lo, hi)
    out["lam_ok_tail"] = lok_tail
    out["tail_at_floor"] = floor_tail
    out["r_tail"] = lam_top / lok_tail if np.isfinite(lok_tail) else 0.0

    lok_band, floor_band = bisect_threshold(
        lambda L: band_bound(lamk, Z, L, BAND_R)[0], lo, hi)
    out["lam_ok_band"] = lok_band
    out["band_floor"] = floor_band          # closes with bands ALONE
    out["r_band"] = lam_top / lok_band if np.isfinite(lok_band) else 0.0
    out["n_expl_tail"] = int(np.searchsorted(lamk, lok_tail, side="left"))
    out["n_expl_band"] = int(np.searchsorted(lamk, lok_band, side="left"))

    # I1 + finite-rank correction: the same certified family, ntop extra modes
    for nt in NTOP_LADDER:
        lk, fl = bisect_threshold(
            lambda L, nt=nt: topmode_bound(lamk, Z, L, BAND_R, nt), lo, hi)
        out["lam_ok_top%d" % nt] = lk
        out["floor_top%d" % nt] = fl
        out["r_top%d" % nt] = lam_top / lk if np.isfinite(lk) else 0.0

    # --- the fixed k-uniform instrument (Lam_0 = 3, r = 2) -----------------
    b_fix, nb_fix, J_fix, wok = band_bound(lamk, Z, BAND_LAM0_FIX, BAND_R,
                                           want_wcheck=True)
    out.update(b_fix=b_fix, nb_fix=nb_fix, n_expl_fix=J_fix, w_ok=wok,
               excess_fix=(b_fix - rho) / max(rho, 1e-300))
    for L in FIXED_THRESHOLDS:
        out["b_tail@%g" % L] = tail_bound(lamk, Z, T_all, L)
        out["b_band@%g" % L] = band_bound(lamk, Z, L, BAND_R)[0]
        out["b_t99@%g" % L] = t99_bound(lamk, Z, R_G, L)

    # --- the chain ordering, at every sample (certified inequalities) ------
    Lc = 2.0
    out["chain"] = (rho <= out["b_band@2"] + 1e-10
                    <= out["b_tail@2"] + 2e-10
                    <= out["b_t99@2"] + 3e-10)

    # --- I1 band masses and the measured decay exponents -------------------
    masses, edges, counts = band_masses(lamk, Z, THETA_LAM0, THETA_R)
    out["masses"], out["edges"], out["counts"] = masses, edges, counts
    out["mass_raw"] = float(sum(masses))
    out["mass_weighted"] = float(sum(m / e for m, e in zip(masses, edges)))
    # a band mass grows with the band WIDTH, so the continuum object is the
    # mass DENSITY per unit Lam -- that is the quantity T99's theta describes.
    if len(masses) >= 3 and min(masses) > 0:
        wdt = [e * (THETA_R - 1.0) for e in edges]
        dens = [m / w for m, w in zip(masses, wdt)]
        sl, se, _, r2 = ols(np.log(edges), np.log(dens))
        out["theta"], out["theta_se"], out["theta_r2"] = -sl, se, r2
    else:
        out["theta"] = out["theta_se"] = out["theta_r2"] = float("nan")
    # the T100 defect tail function m(Lam) = lam_max(T_all - S_Lam) ~ Lam^-p
    lad = np.geomspace(max(0.5, 1.5 * float(lamk[0])), 0.9 * lam_top, 8)
    mm = []
    for L in lad:
        Jm = int(np.searchsorted(lamk, L, side="left"))
        Tm = T_all - sym(Z[:Jm].T @ Z[:Jm]) if Jm > 0 else T_all
        mm.append(max(lmax(sym(Tm)), 1e-300))
    slp, sep, _, r2p = ols(np.log(lad), np.log(mm))
    out["p_tail"], out["p_se"], out["p_r2"] = -slp, sep, r2p

    # --- I4 pointer: numerical effective rank of the bulk operator ---------
    Jb = int(np.searchsorted(lamk, Lc, side="left"))
    Tb = T_all - sym(Z[:Jb].T @ Z[:Jb]) if Jb > 0 else T_all
    tb = lmax(sym(Tb))
    out["bulk_eff_rank"] = float(np.trace(Tb) / tb) if tb > 1e-300 else 0.0
    out["bulk_eff_ratio"] = out["bulk_eff_rank"] / max(mw, 1)
    out["m_of_2"] = tb

    # --- deep extras: the (Lam_0, r_max) Pareto front ----------------------
    if deep:
        front = []
        for L0 in LAM0_LADDER:
            if L0 >= lam_top:
                continue
            f = lambda rr: band_bound(lamk, Z, L0, rr)[0]
            if f(1.0 + 1e-4) > 1.0:
                front.append((L0, None, None, int(np.searchsorted(
                    lamk, L0, side="left"))))
                continue
            rlo, rhi = 1.0 + 1e-4, 8.0
            if f(rhi) <= 1.0:
                rmax = rhi
            else:
                for _ in range(10):
                    rmid = math.sqrt(rlo * rhi)
                    if f(rmid) <= 1.0:
                        rlo = rmid
                    else:
                        rhi = rmid
                rmax = rlo
            nb = band_bound(lamk, Z, L0, rmax)[1]
            front.append((L0, rmax, nb, int(np.searchsorted(lamk, L0,
                                                            side="left"))))
        out["front"] = front
        # truncated band data + Bessel tail above Lam_max (the I1 "rest" term)
        out["b_trunc"] = band_bound(lamk, Z, BAND_LAM0_FIX, BAND_R,
                                    Lam_max=6.0)[0]

    # --- parity: the data-halving check (T100 reproduction) ----------------
    if parity:
        Be, Bo = parity_basis(mw)
        Ce, Co = parity_basis(M - 2 * mw)
        scale = max(float(np.max(np.abs(X))), 1e-300)
        leak_a = max(float(np.max(np.abs(Be.T @ X.T @ Ce))),
                     float(np.max(np.abs(Bo.T @ X.T @ Co))))
        leak_b = max(float(np.max(np.abs(Be.T @ X.T @ Co))),
                     float(np.max(np.abs(Bo.T @ X.T @ Ce))))
        pairs = ((Be, Co), (Bo, Ce)) if leak_a <= leak_b else \
                ((Be, Ce), (Bo, Co))
        out["par_leak"] = min(leak_a, leak_b) / scale
        rhos = []
        for Bw, Cz in pairs:
            Qc = sym(Cz.T @ Q00 @ Cz)
            Gc = (Bw.T @ X.T @ Cz).T
            lc, Vc = eigh(Qc, check_finite=False)
            kp = lc > 1e-12 * float(lc[-1])
            Ac = sym(Bw.T @ Qmm @ Bw) + mu_half * np.eye(Bw.shape[1])
            ac, Ac_V = eigh(Ac, check_finite=False)
            if ac[0] <= 1e-13:
                rhos = []
                break
            Zc = (Vc[:, kp].T @ Gc) @ ((Ac_V * ac ** -0.5) @ Ac_V.T)
            rhos.append(lmax(sym((Zc / lc[kp][:, None]).T @ Zc)))
        out["rho_parity"] = max(rhos) if rhos else float("nan")
    return out


# ================================================== the sweep
def sweep():
    head("SWEEP 16 zones x 4 matched wing fractions, one eigensolve per sample")
    info("M = %d, largest array cap %d^2, budget %ds" % (M_MAIN, MAX_ARRAY,
                                                         int(BUDGET_S)))
    rows = {i: {} for i in range(len(WING_FRACTIONS))}
    n_par = 0
    for k in range(N_ZONES):
        mwm = mw_max_of(k, M_MAIN)
        for i, fr in enumerate(WING_FRACTIONS):
            mw = max(6, int(round(mwm * fr)))
            deep = (i == FRAC_REF)
            par = (i == FRAC_REF and k in (0, 7) and n_par < 2)
            s = analyse(k, M_MAIN, mw, deep=deep, parity=par)
            if s is None:
                continue
            if par:
                n_par += 1
            rows[i][k] = s
        if time.time() - T_START > BUDGET_S:
            info("budget guard hit at zone k=%d -- sweep truncated" % (k + 1))
            break
    got = sum(len(v) for v in rows.values())
    info("samples = %d,  elapsed %.0f s" % (got, time.time() - T_START))
    return rows


# ================================================== I1
def block_i1(rows):
    head("I1    theta-weighted certified band sum  (CERTIFIED + INDUCTION-DATA)")
    info("instrument: [modes below Lam_0 explicit] + [exact band masses P_b,")
    info("weight 1/(lower edge)] + [rest above Lam_max with 1/Lam_max, Bessel].")
    info("P_b = sum_{lam_j in band b} z_j z_j^T is measured EXACTLY by Parseval")
    info("on the Q_00 eigenbasis -- finitely many operator-valued numbers/zone.")

    ref = rows[FRAC_REF]
    zk = sorted(ref)

    wok = all(ref[k]["w_ok"] for k in zk)
    check("el_i1.weights_certified", wok,
          "w_j >= 1/lam_j at every band of every sample (spectral calculus)")
    chain = sum(1 for i in rows for k in rows[i] if rows[i][k]["chain"])
    tot = sum(len(rows[i]) for i in rows)
    check("el_i1.chain_ordering", chain == tot,
          "rho <= b_band <= b_tail <= b_t99 at %d/%d samples (Lam = 2)"
          % (chain, tot))

    par = [(rows[i][k]["rho"], rows[i][k]["rho_parity"], rows[i][k]["par_leak"])
           for i in rows for k in rows[i] if "rho_parity" in rows[i][k]]
    if par:
        dpar = max(abs(a - b) / max(abs(a), 1e-300) for a, b, _ in par)
        lk = max(c for _, _, c in par)
        check("el_i1.parity_free", dpar < 1e-8,
              "rho_blind = max over parity channels to %.1e at %d samples"
              " (channel leak %.1e) -- T100 reproduced, the data halves"
              % (dpar, len(par), lk))

    head("I1    band masses of the smaller window (Lam_0 = %.1f, r = %.1f)"
         % (THETA_LAM0, THETA_R))
    info("   n    band edges -> ||P_b||   (counts)")
    for k in zk[:: max(1, len(zk) // 5)]:
        s = ref[k]
        cells = "  ".join("%.2f:%.3e" % (e, m)
                          for e, m in zip(s["edges"], s["masses"]))
        info("  %3d   %s   (%s)" % (s["n"], cells,
                                    ",".join(str(c) for c in s["counts"])))

    th = [ref[k]["theta"] for k in zk if np.isfinite(ref[k]["theta"])]
    pp = [ref[k]["p_tail"] for k in zk if np.isfinite(ref[k]["p_tail"])]
    if th:
        info("  band mass DENSITY ||P_b||/width ~ Lam^-theta:  theta ="
             " %.2f..%.2f (median %.2f), T99 anchor %.2f..%.2f  [MEASURED]"
             % (min(th), max(th), float(np.median(th)), *T99_THETA))
        info("  (the raw band mass grows with the band width -- the density is")
        info("  the continuum object, the raw mass is not)")
    if pp:
        info("  defect tail m(Lam) = lam_max(T_all - S_Lam) ~ Lam^-p:  p ="
             " %.2f..%.2f (median %.2f), T100 anchor %.2f..%.2f  [MEASURED]"
             % (min(pp), max(pp), float(np.median(pp)), *T100_P))
    check("el_theta.measured", len(th) >= N_ZONES // 2 and len(pp) >= 3,
          "theta in %d/%d zones, p in %d/%d zones" % (len(th), len(zk),
                                                      len(pp), len(zk)))

    head("I1    the new race size: does the band-mass DEMAND grow over zones?")
    info("   n    R_G      sum_b ||P_b||   sum_b ||P_b||/Lam_b   ratio to R_G")
    for k in zk:
        s = ref[k]
        info("  %3d  %7.4f     %10.4f          %10.4f        %6.2f"
             % (s["n"], s["R_G"], s["mass_raw"], s["mass_weighted"],
                s["mass_raw"] / max(s["R_G"], 1e-300)))
    kk = np.array([ref[k]["k"] + 1.0 for k in zk])
    raw = np.array([ref[k]["mass_raw"] for k in zk])
    wgt = np.array([ref[k]["mass_weighted"] for k in zk])
    s_raw, se_raw, _, r2_raw = ols(kk, np.log(raw))
    s_wgt, se_wgt, _, r2_wgt = ols(kk, np.log(wgt))
    info("  log(raw mass sum)     slope %+.4f +- %.4f  R2=%.3f"
         % (s_raw, se_raw, r2_raw))
    info("  log(theta-weighted)   slope %+.4f +- %.4f  R2=%.3f"
         % (s_wgt, se_wgt, r2_wgt))
    gain = float(np.exp((s_raw - s_wgt) * (kk[-1] - kk[0])))
    info("  the theta-weighting removes a factor %.2f of the %.2f total growth"
         % (gain, float(np.exp(s_raw * (kk[-1] - kk[0])))))
    check("el_i1.demand_trend_measured",
          np.isfinite(s_raw) and np.isfinite(s_wgt),
          "raw %+.4f vs weighted %+.4f per zone" % (s_raw, s_wgt))
    return dict(s_raw=s_raw, se_raw=se_raw, s_wgt=s_wgt, se_wgt=se_wgt,
                theta=th, gain=gain)


# ================================================== I2
def block_i2(rows):
    head("I2    the full m(Lam) exploitation: zone-adaptive threshold Lam_k")
    info("b_tail(Lam) = lam_max(L_Lam + (T_all - S_Lam)/Lam),  T100 L1.")
    info("Lam_ok = least CONTINUUM threshold with b_tail <= 1 (bisected on the")
    info("threshold, never on a mode index -- T100 C1).")
    ref = rows[FRAC_REF]
    zk = sorted(ref)
    info("   n   lam_top   Lam_ok^T101   Lam_ok^tail   Lam_ok^band"
         "   factor   modes<Lam_ok^tail / dim E_0")
    for k in zk:
        s = ref[k]
        fac = s["lam_ok_t101"] / max(s["lam_ok_tail"], 1e-300)
        info("  %3d   %7.3f   %11.3f   %11.3f   %11.3f   %6.1fx   %4d/%4d"
             % (s["n"], s["lam_top"], s["lam_ok_t101"], s["lam_ok_tail"],
                s["lam_ok_band"], fac, s["n_expl_tail"], s["dim0"]))
    lt = np.array([ref[k]["lam_ok_tail"] for k in zk])
    kk = np.array([ref[k]["k"] + 1.0 for k in zk])
    bounded = bool(np.all(np.isfinite(lt)))
    low4 = [ref[k]["lam_ok_tail"] for k in zk[:4]]
    check("el_repro.t100_thresholds",
          all(T100_LAM_OK[0] <= v <= T100_LAM_OK[1] for v in low4),
          "zones n=2..5 give Lam_ok^tail %s inside the T100 range %.2f..%.2f"
          % (", ".join("%.2f" % v for v in low4), *T100_LAM_OK))
    s_l, se_l, _, r2_l = ols(kk, np.log(lt))
    info("  Lam_ok^tail range over 16 zones: [%.3f, %.3f]   log-slope"
         " %+.4f +- %.4f (R2=%.3f)" % (lt.min(), lt.max(), s_l, se_l, r2_l))
    fac = np.array([ref[k]["lam_ok_t101"] / max(ref[k]["lam_ok_tail"], 1e-300)
                    for k in zk])
    s_f, se_f, _, r2_f = ols(kk, np.log(fac))
    info("  demand-reduction factor T101 -> tail: %.1fx..%.1fx, log-slope"
         " %+.4f +- %.4f (R2=%.3f)" % (fac.min(), fac.max(), s_f, se_f, r2_f))
    check("el_i2.threshold_bounded", bounded,
          "Lam_ok^tail finite in %d/%d zones, max %.3f vs lam_top %.3f"
          % (len(zk), len(zk), lt.max(),
             max(ref[k]["lam_top"] for k in zk)))

    head("I2    the honest data cost behind the bounded threshold")
    ne = np.array([ref[k]["n_expl_tail"] for k in zk], float)
    d0 = np.array([ref[k]["dim0"] for k in zk], float)
    s_n, se_n, _, r2_n = ols(kk, np.log(np.maximum(ne, 1.0)))
    info("  explicit modes below Lam_ok^tail: %d -> %d, log-slope %+.4f +-"
         " %.4f (R2=%.3f)  [GRID-DEPENDENT shadow of the threshold]"
         % (int(ne[0]), int(ne[-1]), s_n, se_n, r2_n))
    info("  dim E_0 itself: %d -> %d -- the wing narrows, the centre grows,"
         " so a fixed threshold captures more modes" % (int(d0[0]), int(d0[-1])))

    head("I2    the (Lam_0, r_max) Pareto front of the band instrument")
    info("   n    Lam_0=0.5        Lam_0=1.0        Lam_0=2.0        Lam_0=3.0"
         "     (r_max / bands)")
    rmaxs, nbs = [], []
    for k in zk:
        s = ref[k]
        cells = []
        best_nb = None
        for (L0, rmax, nb, ne0) in s.get("front", []):
            if rmax is None:
                cells.append("    ---/--  ")
            else:
                cells.append(" %6.3f/%-4d" % (rmax, nb))
                if best_nb is None or nb + ne0 < best_nb[3]:
                    best_nb = (L0, nb, rmax, nb + ne0)
        info("  %3d  %s" % (s["n"], " ".join(cells)))
        if best_nb:
            nbs.append(best_nb[1])
            rmaxs.append(best_nb[2])
    info("  cheapest = the front point minimising (explicit modes + bands),")
    info("  a DATA PROXY: the two numbers are not the same currency.")
    info("  (r_max = 8.000 is the ladder cap: one band already suffices there)")
    if len(nbs) >= 3:
        s_b, se_b, _, r2_b = ols(np.arange(1.0, len(nbs) + 1.0),
                                 np.log(np.maximum(np.array(nbs, float), 1.0)))
        info("  cheapest band count B = %d..%d, log-slope %+.4f +- %.4f"
             " (R2=%.3f); admissible ratio r_max = %.3f..%.3f"
             % (min(nbs), max(nbs), s_b, se_b, r2_b, min(rmaxs), max(rmaxs)))
    else:
        s_b = se_b = float("nan")

    # the k-UNIFORM column: one fixed continuum threshold for every zone
    col = LAM0_LADDER.index(1.0)
    fix = [(ref[k]["front"][col], ref[k]["k"] + 1.0) for k in zk
           if len(ref[k].get("front", [])) > col]
    okfix = [(f, x) for f, x in fix if f[1] is not None]
    if len(okfix) >= 3:
        xr = np.array([x for _, x in okfix])
        rr = np.array([f[1] for f, _ in okfix])
        nb1 = np.array([float(f[2]) for f, _ in okfix])
        ne1 = np.array([float(f[3]) for f, _ in okfix])
        s_r1, se_r1, _, _ = ols(xr, np.log(np.maximum(rr - 1.0, 1e-6)))
        s_b1, se_b1, _, _ = ols(xr, np.log(np.maximum(nb1, 1.0)))
        s_n1, se_n1, _, _ = ols(xr, np.log(np.maximum(ne1, 1.0)))
        info("  at the FIXED continuum threshold Lam_0 = 1.0 (k-uniform by")
        info("  construction) the instrument closes in %d/%d zones with"
             % (len(okfix), len(zk)))
        info("  r_max - 1 = %.3f..%.3f  (log-slope %+.4f +- %.4f),"
             % (float((rr - 1).min()), float((rr - 1).max()), s_r1, se_r1))
        info("  bands B = %d..%d (log-slope %+.4f +- %.4f), explicit modes"
             " %d..%d (log-slope %+.4f +- %.4f)"
             % (int(nb1.min()), int(nb1.max()), s_b1, se_b1, int(ne1.min()),
                int(ne1.max()), s_n1, se_n1))
    else:
        s_b1 = se_b1 = s_r1 = se_r1 = float("nan")
    check("el_i2.pareto_front", len(nbs) >= N_ZONES // 2,
          "front resolved in %d/%d zones" % (len(nbs), len(zk)))
    return dict(s_l=s_l, se_l=se_l, lam_ok=lt, s_f=s_f, se_f=se_f,
                fac=fac, s_n=s_n, se_n=se_n, nbs=nbs, rmaxs=rmaxs,
                s_b=s_b, se_b=se_b, s_b1=s_b1, se_b1=se_b1,
                s_r1=s_r1, se_r1=se_r1)


# ================================================== I3
def block_i3(rows):
    head("I3    THE RACE REDONE:  r_k = lam_top / Lam_ok  for all instruments")
    info("for the T101 family r_k = lam_top/(R_G/S) = S_k/B_k identically, so")
    info("the three instruments are directly comparable in the SAME currency.")
    ref = rows[FRAC_REF]
    zk = sorted(ref)
    info("   n   supply lam_top   r_k^T101   r_k^tail   r_k^band     S_k     rho")
    for k in zk:
        s = ref[k]
        info("  %3d       %8.4f   %8.4f   %8.3f   %8.3f%s  %.5f  %.5f"
             % (s["n"], s["lam_top"], s["r_t101"], s["r_tail"], s["r_band"],
                "*" if s["band_floor"] else " ", s["S"], s["rho"]))
    nfl = sum(1 for k in zk if ref[k]["band_floor"])
    info("  (*) = the band instrument closes with BANDS ALONE, no explicit")
    info("  modes at all: %d/%d zones.  There r_k^band is limited by the bottom"
         % (nfl, len(zk)))
    info("  of the discrete spectrum, which is a grid object, so those samples")
    info("  are excluded from the r_band fit and priced in band counts instead.")
    kk = np.array([ref[k]["k"] + 1.0 for k in zk])
    info("   n   r_k^band+2 modes   r_k^band+8 modes   (finite-rank variant,")
    info("       same certified family, ntop extra exact modes per zone)")
    for k in zk:
        s = ref[k]
        info("  %3d        %9.3f%s        %9.3f%s"
             % (s["n"], s["r_top2"], "*" if s["floor_top2"] else " ",
                s["r_top8"], "*" if s["floor_top8"] else " "))
    res = {}
    labels = (("r_t101", "T101 uniform"), ("r_tail", "I2 tail"),
              ("r_band", "I1 band"), ("r_top2", "I1 band + 2"),
              ("r_top8", "I1 band + 8"))
    for key, lab in labels:
        y = np.array([ref[k][key] for k in zk])
        m = y > 0
        if key == "r_band":
            m = m & np.array([not ref[k]["band_floor"] for k in zk])
        elif key.startswith("r_top"):
            fk = "floor_top%s" % key[5:]
            m = m & np.array([not ref[k][fk] for k in zk])
        if int(m.sum()) < 3:
            res[key] = (float("nan"),) * 5
            info("  %-14s not resolved (%d usable zones)" % (lab, int(m.sum())))
            continue
        sl, se, c, r2 = ols(kk[m], np.log(y[m]))
        res[key] = (sl, se, r2, float(y[m][0]), float(y[m][-1]))
        info("  %-14s log r slope %+.4f +- %.4f  R2=%.3f   r: %.3f -> %.3f"
             % (lab, sl, se, r2, y[m][0], y[m][-1]))
    lt = max(ref[k]["lam_top"] for k in zk)
    lb = min(ref[k]["lam_top"] for k in zk)
    info("  supply band over the %d zones: lam_top in [%.3f, %.3f] -- FLAT,"
         " as T101 measured (7.0..7.9)" % (len(zk), lb, lt))

    sl101 = res["r_t101"][0]
    check("el_repro.t101_race", abs(sl101 - T101_SLOPE) <= 2.0 * T101_SE,
          "T101 slope reproduced: %+.4f here vs %+.4f +- %.4f there"
          % (sl101, T101_SLOPE, T101_SE))

    head("I3    the same trend at every matched wing fraction (systematic band)")
    keys = ("r_t101", "r_tail", "r_band", "r_top8")
    bands = {k: [] for k in keys}
    for i, fr in enumerate(WING_FRACTIONS):
        ks = sorted(rows[i])
        if len(ks) < 4:
            continue
        x = np.array([rows[i][k]["k"] + 1.0 for k in ks])
        parts = []
        for key in keys:
            y = np.array([rows[i][k][key] for k in ks])
            m = y > 0
            if key == "r_band":
                m = m & np.array([not rows[i][k]["band_floor"] for k in ks])
            elif key.startswith("r_top"):
                fk = "floor_top%s" % key[5:]
                m = m & np.array([not rows[i][k][fk] for k in ks])
            if int(m.sum()) < 3:
                parts.append("%s   n/a  " % key.split("_")[1])
                continue
            sl, se, _, _ = ols(x[m], np.log(y[m]))
            bands[key].append(sl)
            parts.append("%s %+.4f" % (key.split("_")[1], sl))
        info("  frac=%.2f  (%d zones):  %s" % (fr, len(ks), "   ".join(parts)))
    for key in bands:
        if bands[key]:
            info("  systematic band %-7s [%+.4f, %+.4f]"
                 % (key, min(bands[key]), max(bands[key])))

    head("I3    the closure map of the FIXED k-uniform instrument"
         "  (Lam_0 = %.0f, r = %.0f)" % (BAND_LAM0_FIX, BAND_R))
    info("finite data by construction: the modes below Lam_0 plus a handful of")
    info("band masses, with NO zone-dependent tuning of either number.")
    info("  frac    zones closing (b_band <= 1)      b_band range      bands")
    total_close = 0
    total_all = 0
    for i, fr in enumerate(WING_FRACTIONS):
        ks = sorted(rows[i])
        if not ks:
            continue
        b = np.array([rows[i][k]["b_fix"] for k in ks])
        nb = [rows[i][k]["nb_fix"] for k in ks]
        nclose = int((b <= 1.0).sum())
        total_close += nclose
        total_all += len(ks)
        info("  %.2f          %2d/%2d               [%.4f, %.4f]        %d..%d"
             % (fr, nclose, len(ks), b.min(), b.max(), min(nb), max(nb)))
    info("  T101 comparison: the uniform family closed 6/16 at frac 0.25 and"
         " 1/16 at frac 0.50")
    check("el_map.closure_improved", total_close > 7,
          "fixed instrument closes %d/%d samples (T101 family: 7/64 in the"
          " same currency)" % (total_close, total_all))

    head("I3    certified / induction-data / measured ledger of the instrument")
    info("  CERTIFIED      : w_j >= 1/lam_j on every band (spectral calculus);")
    info("                   the Bessel tail 1/Lam_max above the last band;")
    info("                   the ordering rho <= b_band <= b_tail <= b_t99;")
    info("                   the Schur-test route to ||Q_0-|| (T100 S2).")
    info("  INDUCTION-DATA : the band masses P_b and the modes below Lam_0 --")
    info("                   exact objects of the SMALLER window, i.e. the")
    info("                   induction hypothesis one level down (grid drift")
    info("                   reported below).  The count is a threshold, not")
    info("                   a mode index.")
    info("  MEASURED       : theta, R_G, rho, the effective rank -- signals,")
    info("                   never ingredients of the chain.")
    return dict(res=res, bands=bands, total_close=total_close,
                total_all=total_all)


def block_drift(rows):
    head("I3b   grid drift of the new race ratio (resolution honesty)")
    ref = rows[FRAC_REF]
    drifts_r, drifts_l, drifts_n, drifts_t = [], [], [], []
    for k in (0, N_ZONES // 2, N_ZONES - 1):
        base = ref.get(k)
        if base is None:
            continue
        mw2 = max(6, int(round(base["mw"] * M_DRIFT / M_MAIN)))
        s2 = analyse(k, M_DRIFT, mw2)
        if s2 is None:
            continue
        dr = abs(s2["r_tail"] - base["r_tail"]) / max(base["r_tail"], 1e-300)
        dl = abs(s2["lam_ok_tail"] - base["lam_ok_tail"]) / max(
            base["lam_ok_tail"], 1e-300)
        dn = abs(s2["n_expl_tail"] - base["n_expl_tail"]) / max(
            base["n_expl_tail"], 1)
        dt = abs(s2["lam_top"] - base["lam_top"]) / base["lam_top"]
        drifts_r.append(dr)
        drifts_l.append(dl)
        drifts_n.append(dn)
        drifts_t.append(dt)
        info("  n=%2d  M=%d->%d   Lam_ok %.3f->%.3f (%.1f%%)   r_tail"
             " %.2f->%.2f (%.1f%%)   modes %d->%d (%.0f%%)   lam_top"
             " %.2f->%.2f (%.1f%%)"
             % (base["n"], M_MAIN, M_DRIFT, base["lam_ok_tail"],
                s2["lam_ok_tail"], dl * 100, base["r_tail"], s2["r_tail"],
                dr * 100, base["n_expl_tail"], s2["n_expl_tail"], dn * 100,
                base["lam_top"], s2["lam_top"], dt * 100))
    ok = len(drifts_l) >= 2
    if ok:
        info("  reading: the DEMAND Lam_ok is the continuum object and its")
        info("  boundedness is a statement that does not need lam_top at all;")
        info("  lam_top drifts because k(t) ~ log(t/2pi) (T100 C1), and the")
        info("  mode count is the grid shadow of the threshold.")
    check("el_drift.reported", ok,
          "threshold drift <= %.1f%%, race drift <= %.1f%%, supply lam_top"
          " drift <= %.1f%%, mode-count drift <= %.0f%%"
          % (100 * max(drifts_l), 100 * max(drifts_r), 100 * max(drifts_t),
             100 * max(drifts_n))
          if ok else "insufficient rungs")
    return dict(dl=drifts_l, dr=drifts_r, dn=drifts_n, dt=drifts_t)


# ================================================== I4
def block_i4(rows, i1, i2, i3, drift):      # noqa: C901 -- one report block
    head("I4    synthesis -- the structural floor under EVERY instrument here")
    info("every bound of this shape sits ABOVE rho, so closure needs its")
    info("relative excess over rho to be at most the slack S = 1 - rho.")
    ref = rows[FRAC_REF]
    zk = sorted(ref)
    kk = np.array([ref[k]["k"] + 1.0 for k in zk])
    S = np.array([ref[k]["S"] for k in zk])
    ex = np.array([ref[k]["excess_fix"] for k in zk])
    rm = np.array([ref[k]["rel_margin"] for k in zk])
    s_S, se_S, _, r2_S = ols(kk, np.log(np.maximum(S, 1e-12)))
    s_e, se_e, _, r2_e = ols(kk, np.log(np.maximum(ex, 1e-12)))
    s_m, se_m, _, r2_m = ols(kk, np.log(np.maximum(rm, 1e-12)))
    info("   n   dim E_-   S_k = 1-rho   excess of the fixed band instrument"
         "   1 - D/(mu/2)")
    for i, k in enumerate(zk):
        info("  %3d     %4d      %.6f                  %.6f"
             "         %.6f" % (ref[k]["n"], ref[k]["mw"], S[i], ex[i], rm[i]))
    info("  log S           slope %+.4f +- %.4f  R2=%.3f   (%.4f -> %.4f)"
         % (s_S, se_S, r2_S, S[0], S[-1]))
    info("  log excess      slope %+.4f +- %.4f  R2=%.3f   (%.4f -> %.4f)"
         % (s_e, se_e, r2_e, ex[0], ex[-1]))
    info("  log rel-margin  slope %+.4f +- %.4f  R2=%.3f   -- the T101"
         " primitive, flat within its error" % (s_m, se_m, r2_m))
    n_cross = int((ex > S).sum())
    head_room = float(np.min(S / np.maximum(ex, 1e-12)))
    info("  the excess exceeds the slack in %d/%d zones at frac %.2f; the"
         " tightest headroom S/excess over the zones is %.2fx"
         % (n_cross, len(zk), WING_FRACTIONS[FRAC_REF], head_room))
    if s_e - s_S > 2.0 * math.hypot(se_e, se_S) and head_room >= 1.0:
        info("  the two lines CONVERGE at %+.4f per zone: extrapolated (NOT"
             " proved) they meet after %.1f further zones"
             % (s_e - s_S, math.log(head_room) / (s_e - s_S)))
    elif s_e - s_S > 2.0 * math.hypot(se_e, se_S):
        info("  the two lines converge at %+.4f per zone and have ALREADY"
             " crossed inside the measured range (headroom %.2fx < 1): the"
             " fixed band instrument is over budget in %d zones and the ratio"
             " r has to be pushed towards 1 there"
             % (s_e - s_S, head_room, n_cross))
    else:
        info("  the two lines do not separate significantly over the measured"
             " range (%+.4f +- %.4f per zone)"
             % (s_e - s_S, math.hypot(se_e, se_S)))
    check("el_i4.floor_measured", np.isfinite(s_S) and np.isfinite(s_e),
          "slack slope %+.4f, instrument excess slope %+.4f" % (s_S, s_e))

    head("I4    which object class door C needs next (a MEASURED pointer)")
    er = np.array([ref[k]["bulk_eff_rank"] for k in zk])
    fr = np.array([ref[k]["bulk_eff_ratio"] for k in zk])
    mws = np.array([ref[k]["mw"] for k in zk], float)
    s_r, se_r, _, r2_r = ols(kk, er)
    s_fr, se_fr, _, r2_fr = ols(kk, fr)
    info("  numerical effective rank trace/||.|| of the bulk operator at"
         " Lam = 2: %.2f..%.2f (median %.2f), dim E_- = %d..%d"
         % (er.min(), er.max(), float(np.median(er)), int(mws.min()),
            int(mws.max())))
    info("  absolute trend  slope %+.4f +- %.4f (R2=%.3f) -- %s"
         % (s_r, se_r, r2_r,
            "GROWING" if s_r > 2 * se_r else
            ("SHRINKING" if s_r < -2 * se_r else "flat within its error")))
    info("  as a FRACTION of dim E_-: %.3f..%.3f (median %.3f), slope"
         " %+.5f +- %.5f (R2=%.3f)"
         % (fr.min(), fr.max(), float(np.median(fr)), s_fr, se_fr, r2_fr))
    if float(np.median(fr)) <= 0.25:
        info("  reading: the mass the bands may not smear occupies a small")
        info("  FRACTION of the wing space, so the object class that fits is a")
        info("  finite-rank wing-adapted correction -- a Slepian-Pollak-Landau")
        info("  prolate basis concentrated on the wing pair (the T96")
        info("  recommendation) -- rather than a finer scalar weighting of the")
        info("  same bulk.  A scalar weight cannot see a direction; a")
        info("  concentrated basis can.")
    else:
        info("  reading: the bulk fills a large fraction of the wing space, so")
        info("  a finite-rank correction of fixed rank cannot carry it either;")
        info("  the object class has to change more deeply than by deflation.")
    info("  CAVEAT: at matched wing fraction dim E_- shrinks from %d to %d over"
         % (int(mws[0]), int(mws[-1])))
    info("  the zones (the zone itself narrows), so the absolute effective")
    info("  rank is resolution limited at the top -- the FRACTION is the")
    info("  comparable quantity, and the drift rung above prices it.")
    info("  [MEASURED pointer, not a proof]")

    head("I4    the finite-rank test of that pointer (same certified family)")
    info("keep the ntop heaviest bulk modes exact and band the rest: if a FIXED")
    info("small ntop flattens the race, the missing object is a handful of")
    info("directions and the data stays k-uniform.")
    info("   n    Lam_ok band   +2 modes   +8 modes    gain(8)")
    for k in zk:
        s = ref[k]
        info("  %3d      %8.3f   %8.3f   %8.3f     %6.2fx"
             % (s["n"], s["lam_ok_band"], s["lam_ok_top2"], s["lam_ok_top8"],
                s["lam_ok_band"] / max(s["lam_ok_top8"], 1e-300)))
    for nm, lab in (("r_band", "band, ntop=0"), ("r_top2", "band, ntop=2"),
                    ("r_top8", "band, ntop=8")):
        sl_, se_, r2_, y0, y1 = i3["res"][nm]
        info("  %-14s log r slope %+.4f +- %.4f  R2=%.3f   r: %.3f -> %.3f"
             % (lab, sl_, se_, r2_, y0, y1))
    gn = np.array([ref[k]["lam_ok_band"] / max(ref[k]["lam_ok_top8"], 1e-300)
                   for k in zk])
    s_g, se_g, _, r2_g = ols(kk, np.log(gn))
    half = len(zk) // 2
    info("  the GAIN is the honest reading, not the slope: gain(8) falls with")
    info("  slope %+.4f +- %.4f (R2=%.3f), median %.2fx in the lower half of"
         % (s_g, se_g, r2_g, float(np.median(gn[:half]))))
    info("  the zones against %.2fx in the upper half.  The steeper log-r slope"
         % float(np.median(gn[half:])))
    info("  of the finite-rank variant is therefore NOT a defect of the")
    info("  variant: it comes from an enormous gain in the EASY low zones and")
    info("  none where the race is actually tight.")
    sl8 = i3["res"]["r_top8"][0]
    se8 = i3["res"]["r_top8"][1]
    check("el_i4.finite_rank_tested", np.isfinite(sl8) and np.isfinite(s_g),
          "ntop=8: gain %.2fx..%.2fx, median %.2fx in the top half, gain trend"
          " %+.4f +- %.4f" % (gn.min(), gn.max(),
                              float(np.median(gn[half:])), s_g, se_g))
    fr_helps = float(np.median(gn[half:])) > 1.5
    check("el_i4.object_class_typed", np.isfinite(s_r) and np.isfinite(s_fr),
          "effective rank %.2f..%.2f (%.3f..%.3f of dim E_-), slope"
          " %+.4f +- %.4f" % (er.min(), er.max(), fr.min(), fr.max(), s_r,
                              se_r))

    head("I4    where the missing object lives (the typing door C needs)")
    info("every instrument built here is a WEIGHTING of the E_0 spectrum, i.e.")
    info("a bulk-side object.  Two independent measurements say that is the")
    info("wrong side:")
    info("  * the theta-weighting of the bulk removes only a factor %.2f of the"
         % i1["gain"])
    info("    %.2f growth of the demand over the zones;"
         % float(np.exp(i1["s_raw"] * (len(zk) - 1))))
    info("  * a finite-rank exact correction inside the bulk gains %.2fx in the"
         % float(np.median(gn[half:])))
    info("    upper half of the zones, i.e. nothing where it is needed.")
    info("what decides closure is S = 1 - rho, and rho = lam_max(W, A_sh) is a")
    info("WING-side object: the near-saturation of the pencil A_sh - W as the")
    info("wing widens.  So the object class door C needs is one adapted to the")
    info("near-null direction on E_- -- a prolate / Slepian basis concentrated")
    info("on the wing pair (T96), or the equality argument of Fredholm-")
    info("alternative shape that T100 typed at the zone top -- and NOT a finer")
    info("scalar or finite-rank treatment of the E_0 bulk.  %s"
         % ("The finite-rank test above leaves that route open."
            if fr_helps else "The finite-rank test above closes that route."))

    head("I4    VERDICT")
    cand = [(i3["res"][nm][0], i3["res"][nm][1], nm)
            for nm in ("r_tail", "r_band", "r_top2", "r_top8")
            if np.isfinite(i3["res"][nm][0])]
    cand.sort(key=lambda z: -z[0])
    sl, se, best = cand[0] if cand else (float("nan"), float("nan"), "none")
    sys_band = i3["bands"].get(best) or [sl]
    map_ok = i3["total_close"] >= 0.75 * i3["total_all"]
    flat = (sl >= -0.05) and (abs(sl) <= 2.0 * se)
    improved = sl > T101_FLAT_BAND

    info("  best instrument in threshold currency: %s, log-slope %+.4f +- %.4f"
         "  (systematic band over the four fractions [%+.4f, %+.4f])"
         % (best, sl, se, min(sys_band), max(sys_band)))
    info("  grid drift of that slope's inputs: threshold <= %.1f%%, race"
         " <= %.1f%%, mode count <= %.0f%%"
         % (100 * max(drift["dl"] or [0.0]), 100 * max(drift["dr"] or [0.0]),
            100 * max(drift["dn"] or [0.0])))
    info("  T101 anchor: %+.4f +- %.4f;  'clearly flatter' line: %+.4f"
         % (T101_SLOPE, T101_SE, T101_FLAT_BAND))
    info("  fixed k-uniform instrument closes %d/%d samples"
         % (i3["total_close"], i3["total_all"]))
    info("  data currency: threshold BOUNDED (%.2f..%.2f) but the mode count"
         " below it grows with slope %+.4f +- %.4f"
         % (i2["lam_ok"].min(), i2["lam_ok"].max(), i2["s_n"], i2["se_n"]))
    info("  band count: cheapest configuration slope %+.4f +- %.4f, at the"
         " fixed threshold Lam_0 = 1 slope %+.4f +- %.4f"
         % (i2["s_b"], i2["se_b"], i2["s_b1"], i2["se_b1"]))

    data_uniform = (i2["s_b1"] <= 2.0 * i2["se_b1"]) and \
                   (i2["s_n"] <= 2.0 * i2["se_n"])
    if flat and map_ok and data_uniform:
        verdict = "INSTRUMENT-UNIFORM"
        why = ("the demand is flat in BOTH currencies (threshold and data)"
               " over 16 zones -- the toolmaking problem is solved and only"
               " door A remains")
    elif flat and map_ok:
        verdict = "FAMILY-EXHAUSTED"
        why = ("the THRESHOLD demand is flat (slope %+.4f) and the closure map"
               " improves to %d/%d, but the DATA the threshold hides is not"
               " uniform (band count slope %+.4f +- %.4f at the fixed"
               " threshold, explicit-mode slope %+.4f +- %.4f) and the slack"
               " S falls with slope %+.4f +- %.4f, so no fixed-precision"
               " member of this family is k-uniform"
               % (sl, i3["total_close"], i3["total_all"], i2["s_b1"],
                  i2["se_b1"], i2["s_n"], i2["se_n"], s_S, se_S))
    elif improved:
        verdict = "INSTRUMENT-IMPROVED"
        why = ("slope %+.4f is clearly flatter than the T101 band, a factor"
               " %.1fx..%.1fx of demand reduction, but still falling"
               % (sl, i2["fac"].min(), i2["fac"].max()))
    else:
        verdict = "FAMILY-EXHAUSTED"
        why = ("no member of the family flattens the race: best slope %+.4f"
               " against the T101 anchor %+.4f" % (sl, T101_SLOPE))
    info("  => %s" % verdict)
    for line in _wrap(why, 70):
        info("     %s" % line)
    check("el_i4.verdict_reached", verdict in ("INSTRUMENT-UNIFORM",
                                               "INSTRUMENT-IMPROVED",
                                               "FAMILY-EXHAUSTED"),
          verdict)
    return verdict


def _wrap(text, width):
    out, line = [], ""
    for word in text.split():
        if len(line) + len(word) + 1 > width:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out


# ================================================== main
def main():
    print("=" * 78)
    print("TFPT discovery probe -- part 103 -- contract INSTRUMENT (door C)")
    print("=" * 78)
    firewall()
    validate_instrument()

    rows = sweep()
    n_samples = sum(len(v) for v in rows.values())
    check("el_forms.sweep_complete", n_samples >= 3 * N_ZONES,
          "%d samples over %d zones x %d fractions"
          % (n_samples, N_ZONES, len(WING_FRACTIONS)))
    eq = all(rows[i][k]["equiv"] for i in rows for k in rows[i])
    dk = all(rows[i][k]["D"] <= rows[i][k]["mu_half"]
             for i in rows for k in rows[i])
    check("el_chain.target_holds", dk,
          "D_k <= mu_k/2 at %d/%d samples (T101 reproduced: the TARGET never"
          " fails)" % (n_samples, n_samples))
    check("el_chain.rho_equivalence", eq,
          "rho <= 1 <=> D_k <= mu_k/2 at every sample (Schur complement)")
    parres = max(rows[i][k]["par_res"] for i in rows for k in rows[i])
    check("el_chain.parity_selection", parres < 1e-11,
          "J_0 Q_0- J_- = -Q_0- to %.1e (Weil parity selection rule)" % parres)

    i1 = block_i1(rows)
    i2 = block_i2(rows)
    i3 = block_i3(rows)
    drift = block_drift(rows)
    verdict = block_i4(rows, i1, i2, i3, drift)

    head("BUDGET")
    el = time.time() - T_START
    check("el_budget.array_cap", MAXN_SEEN <= MAX_ARRAY,
          "largest array %d^2 <= %d^2" % (MAXN_SEEN, MAX_ARRAY))
    check("el_budget.runtime", el < 900.0, "%.0f s < 900 s" % el)

    print("")
    print("=" * 78)
    print("VERDICT  %s" % verdict)
    print("TOTAL    %d checks, %d failures, %.0f s, largest array %d^2"
          % (PASS + FAIL, FAIL, el, MAXN_SEEN))
    print("=" * 78)
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
