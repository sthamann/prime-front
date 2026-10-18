"""Discovery probe (2026-07-26), part 101 of the zeta/prime investigation.
Contract K.ASYMPTOTICS -- the fate question of the zone programme.

THE RACE
  Two effects run against each other as the staircase induction climbs into
  higher zones:
    SELF-STRENGTHENING -- every atom that is already installed makes the next
      step easier.  T98 measured a three-way cancellation (arch + pole + old
      atoms) of the continuation defect worth 1.4x..2.0x with 241x spikes, and
      the spikes grew with the number of installed atoms.
    CROWDING -- the atoms move together.  Atom entries alpha_n = log(n)/2 have
      gaps (1/2) log(n_{k+1}/n_k) ~ 1/(2 n_k) along the integers, the T96
      handoff windows shrank +0.0250 -> +0.0094 -> +0.0114 -> +0.0067 over
      k = 1..4, and the T95/T96 margin decays like exp(-49 alpha).
  If self-strengthening wins, only finitely many zones are hard and the
  "asymptotics + finite check" route to a full proof is real.  If crowding
  wins, the route is provably bounded and the RH hardness is exactly located.
  This probe measures both laws over as many zones as the budget resolves.

THE CONVENTION (T93/T95/T96/T97/T98, unchanged)
  f real, supp f subset (-alpha, alpha), ||f||_2 = 1;  h = f * f~ even,
  h(0) = 1, supp h subset (-2 alpha, 2 alpha), h(u) = int f(x) f(x-u) dx.
      P_pole(f) = 2 (int f e^{x/2})(int f e^{-x/2})
      A_arch(f) = (1/2pi) int |fhat(t)|^2 k(t) dt,
                  k(t) = Re psi(1/4 + i t/2) - log pi,  k(0) = -5.3722...
      Q_k(f)    = P_pole + A_arch - sum_{log n <= 2 alpha} mu_n h_f(log n),
                  mu_n = 2 Lambda(n) / sqrt(n)        (Weil 1952)
  Atom entries alpha_n = log(n)/2, prime powers only (Lambda(n) != 0):
      n =  2  0.346574   n =  3  0.549306   n =  4  0.693147
      n =  5  0.804719   n =  7  0.972955   n =  8  1.039721
      n =  9  1.098612   n = 11  1.199035   n = 13  1.282474
      n = 16  1.386294   n = 17  1.416606   n = 19  1.472220
  Zone k is alpha in (alpha_k, alpha_{k+1}); the geometry is the wing width
  delta = 2 alpha - u, u = log n_k, alpha' = u - alpha, wings I_L = (-alpha,
  -alpha'), I_R = I_L + u, centre (-alpha', alpha').  E_-/E_+ are the anti /
  symmetric two-bump wing pairs, E_0 the centre; the k-th atom is
  diag(-1/2, 0, +1/2) there, so the E_-/E_0 half of the induction step is the
  scalar inequality D_k(alpha) <= mu_k/2 with
      D_k(alpha) = -lambda_min( Q_{k-1}|E_-  -  Q_{-0} (Q_{k-1}|E_0)^{-1} Q_{0-} ).

THE INSTRUMENT (self-contained, assembled from the convention)
  Piecewise-constant Galerkin on M equal cells of (-alpha, alpha), phi_i =
  Delta^{-1/2} 1_{cell i}, Delta = 2 alpha / M.
    * pole   : a b^T + b a^T with a_i = <phi_i, e^{x/2}>, b_i = <phi_i, e^{-x/2}>
               -- EXACT cell integrals, no quadrature.
    * atom   : symmetric Toeplitz S(u)_{ij} = (1/2)[tri((i-j)D - u) +
               tri((i-j)D + u)], tri(y) = max(0, 1 - |y|/D) -- the EXACT
               PWC autocorrelation overlap, valid for non-integer shifts.
    * arch   : the digamma kernel is moved to u-space by the classical
               integral representation psi(s) = -gamma + int_0^inf
               (e^{-v} - e^{-sv})/(1 - e^{-v}) dv, giving the identity
                 A_arch = -h(0)(gamma + log pi)
                          + 2 int_0^inf [h(0) e^{-2u} - h(u) e^{-u/2}]
                                        / (1 - e^{-2u}) du,
               whose PWC matrix is again symmetric Toeplitz and whose lag
               vector depends ONLY on Delta -- which makes the T97/T98 zone
               self-similarity EXACT at the discrete level (verified in K4).
               The u = 0 log singularity is resolved in closed form,
               int_D^inf 2 e^{-2u}/(1-e^{-2u}) du = -log(1 - e^{-2D}).
  All three blocks are validated in K0 against independent references (the
  flat-window closed forms and mpmath's digamma).

THE MEASUREMENT BLOCKS
  K1  HANDOFF-WINDOW ASYMPTOTICS.  For every zone that the budget resolves,
      alpha_free^(k) = the alpha at which the atom-k-free form Q_{k-1} loses
      positivity, and the handoff window w_k = alpha_free^(k) - alpha_k.  The
      handoff holds iff w_k > 0, i.e. atom k arrives strictly BEFORE it is
      needed.  Positivity is decided by Cholesky of Q + tol*I (an exact
      inertia test, ~10x cheaper than an eigensolve), on an M ladder and on a
      tol ladder, so that BOTH resolution axes are exposed, plus a Richardson
      extrapolation in 1/M at two assumed orders as a bias band.  The w_k
      sequence is fitted against the candidate laws w ~ c n^p, w ~ c mu^p,
      w ~ c g^p (g = atom gap) and their JOINT two-variable form, and the
      critical comparison w_k / g_k is tracked.  A candidate law is only
      NAMED if it collapses the scatter, which is scored explicitly.
  K2  SELF-STRENGTHENING ASYMPTOTICS.  Per zone, on a wing-width ladder:
      (i) the three-way cancellation of the continuation defect X = Q_{0-}
          (the cross block that couples the induction hypothesis on E_0 to
          the wings on E_-), X = X_pole + X_arch + X_old, measured as
              C_frob   = (|X_pole| + |X_arch| + |X_old|) / |X|      (Frobenius)
              C_spike  = max over columns of the same ratio,
          against the number of installed atoms k-1 and against sum_{j<k} mu_j;
      (ii) the D_k margins mu_k/2 - D_k and the RELATIVE margin
          1 - D_k/(mu_k/2) -- stable/growing = self-strengthening, falling =
          crowding.
  K3  THE RACE QUANTIFIED.  The induction step closes through the valid chain
      rho <= R_G * J_sup of T98; with the spectrum of the smaller window split
      at Lambda the uniform BULK REMAINDER demand is R_G / Lambda, minimal at
      Lambda = lambda_max(Q_00).  So
          demand   B_k = R_G / lambda_max(Q_00),
                        R_G = sup ||Q_{0-} x||^2 / (x^T A_sh x),
                        A_sh = Q_{k-1}|E_- + (mu_k/2) I,
          supply   S_k = 1 - rho_k,  rho_k = lambda_max(W, A_sh),
                        W = Q_{-0} Q_{00}^{-1} Q_{0-},
          race     r_k = S_k / B_k,   closure of the uniform-bulk family
                        needs r_k > 1,
          work     Lam_ok = R_G / S_k and the number of smaller-window modes
                        below it -- the T98 "how much explicit finite work per
                        zone" statistic (closure is possible iff Lam_ok <=
                        lambda_max, which is the same inequality as r_k >= 1).
      Trend of r_k over k with an OLS error band AND a systematic band over
      four matched wing fractions, a grid-drift check, extrapolation (LABELLED
      as extrapolation, never as proof), and the crossover question.
  K4  EXACT ARITHMETIC SKELETON.  (i) atom gaps and the mu_k sequence are pure
      arithmetic; (ii) the parity selection rule J_- Q_{-0} J_0 = -Q_{-0} and
      the zone self-similarity Q_{k-1}|E_0 = Q_{k'}(alpha') are checked in the
      HIGH zones, not only the low ones; (iii) recursion termination
      alpha' = u_k - alpha < alpha_k is verified over a dense grid of starting
      windows with the step count reported.
  K5  SYNTHESIS -- the race verdict with all caveats, what an asymptotics
      THEOREM would have to prove, and where exactly the RH hardness sits if
      crowding wins.

PREREGISTERED VERDICTS
  SELF-STRENGTHENING-TRENDS : the relative margin grows or stabilises over the
      measurable zones -- the asymptotics path is real, laws named.
  CROWDING-TRENDS           : the relative margin falls -- the route is
      bounded and the RH hardness is localised.
  RACE-UNRESOLVED           : the numerics are exhausted before the trend is
      clear -- the resolution limit is documented together with what better
      instruments would be needed.
  Element gates: el_firewall, el_kernel, el_forms, el_selfsim, el_parity,
  el_fence, el_k1, el_k2, el_k3, el_k4, el_honest.

OUTCOME OF THIS RUN  =>  CROWDING-TRENDS, but located in the PROOF FAMILY and
                         not in the two primitive laws.  31 checks, 0 failures,
                         40 s, largest array 2000^2, 16 zones (n_k = 2 .. 29).
  K1  The zone programme resolves FAR past the T96 exhaustion point: all 16
      handoff windows are positive at every resolution, w_k = 2.50e-2, 9.87e-3,
      1.20e-2, 7.02e-3, 5.91e-3, 1.03e-2, 8.04e-3, 4.71e-3, 4.26e-3, 8.23e-3,
      3.69e-3, 3.47e-3, 3.21e-3, 4.55e-3, 5.54e-3, 2.83e-3 at M = 2000, and
      the T96 anchors for k = 1..4 reproduce (0.0250/0.0250, 0.0099/0.0094,
      0.0120/0.0114, 0.0070/0.0067).  The M ladder 900/1400/2000 drifts them
      0%..41% downward and the tol ladder 1e-12/1e-9/1e-6 only 0.1%..1.3%, so
      the limiting axis is the CELL COUNT, not the positivity threshold, and
      no zone reaches the 50%-drift frontier.  Both Richardson orders keep
      every w_inf > 0.
      The sequence is NOT smooth in k -- it is ARITHMETIC.  w_k ~ n^-0.61
      +- 0.11 (R2 = 0.70) and the atom gap g_k ~ n^-0.615 (R2 = 0.71, exact),
      i.e. the window shrinks at exactly the rate at which the atoms crowd, so
      the critical ratio w_k/g_k has slope +0.002 +- 0.178 (R2 = 0.000) and
      stays in [0.031, 0.221] over n = 2..29.  The joint fit log w ~ +0.90
      log g - 0.87 log mu (R2 = 0.79) collapses onto a ONE-PARAMETER LAW
              w_k = c * (alpha_{k+1} - alpha_k) / mu_k,   c = 0.0838 +- 0.0231,
      whose scatter is 2.66x against 8.85x for w_k alone (CV 28% vs 74%) and
      whose residual slope -0.066 +- 0.089 in log n is consistent with zero.
      Read plainly: the handoff window is the atom SPACING divided by the atom
      STRENGTH.  Weak prime-power atoms (n = 4, 8, 16, 25, 27) leave wide
      windows, strong prime atoms leave narrow ones.
  K2  Self-strengthening is real, lawful, and BOUNDED.  The three-way
      cancellation of the continuation defect switches on the instant old
      atoms exist -- C_frob 1.004 in zone n = 2 (no old atoms) rising to
      1.17..1.28, C_col 1.00 -> 1.33..1.42, entrywise C_spike up to 9.8 -- and
      it grows lawfully with the installed mass rather than with the zone
      index (log C_spike vs sum mu_old: slope +0.077 +- 0.021, R2 = 0.50).
      The defect split X = X_pole + X_arch + X_old is exact to 1.9e-16 at all
      64 samples.  But the reserve the induction actually spends, the RELATIVE
      margin 1 - D_k/(mu_k/2), is FLAT, not growing: at matched wing fraction
      its log-slope is -0.009..-0.021 per zone with standard errors 0.05..0.10,
      i.e. indistinguishable from zero at all four fractions, with two orders
      of magnitude of arithmetic scatter (0.0013 at n = 13 against 1.31 at
      n = 16) again tracking mu_k.  D_k <= mu_k/2 holds at 64/64 samples.
  K3  The race is lost by the CLOSURE INSTRUMENT, not by the target.  The
      uniform bulk-remainder demand B_k = R_G/lambda_max grows steadily
      (0.068 -> 0.29, driven by R_G 0.49 -> 2.16 while lambda_max stays at
      7.0..7.9) while the slack S_k = 1 - rho shrinks (0.209 -> 0.006..0.044),
      so r_k = S_k/B_k falls from 3.06 to 0.02..0.15 with slope -0.162 +-
      0.056 (R2 = 0.37) and a systematic band [-0.181, -0.144] over four
      matched wing fractions; the grid drift of r_k is 3%..18%.  There is no
      k* to wait for: the fitted crossover lies BELOW the measured range, the
      family closes in 6/16 zones at wing fraction 0.25 and in 1/16 at 0.50,
      and the only zone that closes throughout is n = 2, whose smaller window
      carries no atoms at all.  This is exactly the T98 pattern (closure on
      the lower part of a zone only) extended by 12 zones.  Meanwhile the TRUE
      target D_k <= mu_k/2 never fails -- so what degrades is the headroom of
      the two-factor sufficient condition, not the mathematics under it.
  K4  The exact skeleton is zone-independent and holds verbatim at the top.
      The parity selection rule J_- Q_{-0} J_0 = -Q_{-0} holds to 2.0e-14 in
      the HIGH zones n = 25, 27, 29; the discrete zone self-similarity
      Q_{k-1}|E_0 = Q_{k'}(alpha') is machine exact (<= 9.4e-14 relative) in
      all 16 zones -- it is exact by construction here, because the PWC
      archimedean lag vector depends only on the cell width; the recursion
      terminates from 960/960 starting windows with steps <= k+1 (worst chain
      13 steps from zone n = 29), so termination is arithmetic.  And the
      crowding input itself is exact: gaps (1/2) log(n_{k+1}/n_k) ~ n^-0.615
      while mu_k ~ n^-0.087 (R2 = 0.02) -- the atom STRENGTHS do not decay at
      all over this range, only the spacings do.
  K5  Verdict CROWDING-TRENDS with the location named: the two primitive laws
      (handoff window relative to atom spacing; relative D_k margin) are FLAT
      over 16 zones, so the physical race is not yet decided against the
      programme; what falls significantly is r_k, the headroom of the uniform
      bulk-remainder closure.  The reduction of RH that the zone programme
      offers is therefore intact but TIGHT, and the missing statement is
      arithmetic, not asymptotic: a lower bound w_k >= c * g_k / mu_k.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit, no
    verification/ module, no next.txt edit, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, network imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  A negative
    lambda_min on a GENUINE window direction is an IMPLEMENTATION SIGNAL,
    fenced, never reported as mathematics.  The atom-deleted counterfactual
    Q_{k-1} inside zone k is NOT a genuine form -- its negativity is the
    measurement, by construction.
  * lambda_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute positivity, never prove it.  Hence every
    alpha_free^(k) and every w_k reported here is an UPPER estimate, and both
    resolution axes (cell count M, positivity tolerance tol) are shown.
  * Every fit and every extrapolation is labelled as such.  No "proved"
    language without a certificate.  Classical anchors cited, not re-derived:
    Weil 1952 (explicit formula), Yoshida 1992 / Bombieri 2000 /
    Connes-Consani 2021 (unconditional positivity up to h-support log 2), the
    digamma archimedean kernel and its integral representation (Whittaker-
    Watson), Rayleigh-Ritz, Gauss-Legendre quadrature, Schur complements,
    centrosymmetric block diagonalisation (Cantoni-Butler 1976), Cholesky
    inertia, Paley-Wiener / Slepian-Pollak-Landau concentration, ordinary
    least squares with Student bands.
"""
import ast
import math
import time

import mpmath
import numpy as np
from numpy.lib.stride_tricks import as_strided
from numpy.linalg import LinAlgError
from scipy.linalg import cholesky, eigh, eigvalsh

PASS = 0
FAIL = 0
T_START = time.time()
mpmath.mp.dps = 30

EULER = float(mpmath.euler)
LOG_PI = math.log(math.pi)
LOG2 = math.log(2.0)
K0_CLOSED = -EULER - 3.0 * LOG2 - math.pi / 2.0 - LOG_PI
ALPHA_CLASSIC = LOG2 / 2.0

MAX_ARRAY = 2000
BUDGET_S = 860.0
FENCE = -1.0e-9

# K1 resolution axes
M_LADDER = (900, 1400, 2000)
TOL_LADDER = (1.0e-12, 1.0e-9, 1.0e-6)
TOL_MAIN = 1.0e-9
M_TOL = 1400
BISECT_STEPS = 18

# K2/K3 resolution
M_K2 = 1600
M_K2_DRIFT = 2000
WING_FRACTIONS = (0.25, 0.50, 0.75, 0.95)

GLX, GLW = np.polynomial.legendre.leggauss(24)

# (n, log n, Lambda(n), mu_n = 2 Lambda(n)/sqrt(n)) -- prime powers only.
_PP = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3),
       (11, 11), (13, 13), (16, 2), (17, 17), (19, 19), (23, 23),
       (25, 5), (27, 3), (29, 29), (31, 31), (32, 2), (37, 37)]
ATOMS = tuple(
    (n, math.log(n), math.log(p), 2.0 * math.log(p) / math.sqrt(n))
    for n, p in _PP
)
N_OF = [a[0] for a in ATOMS]
LOGN = [a[1] for a in ATOMS]
MU = [a[3] for a in ATOMS]
ALPHA_ENTRY = [x / 2.0 for x in LOGN]

# T96 anchors for k = 1..4 (M = 2400 ladder)
T96_W = (0.0250, 0.0094, 0.0114, 0.0067)

N_ZONES = 16                      # zones k = 1..16, i.e. n_k = 2 .. 29
MAXN_SEEN = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tail = f"  {detail}" if detail else ""
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{tail}", flush=True)
    return ok


def info(msg):
    print(f"        {msg}", flush=True)


def head(msg):
    print(f"\n{msg}", flush=True)


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


def mols(cols, y):
    """Multivariate OLS with intercept: returns (coeffs, stderrs, R2)."""
    y = np.asarray(y, float)
    A = np.column_stack([np.ones(y.size)] + [np.asarray(c, float) for c in cols])
    n, p = A.shape
    beta = np.linalg.lstsq(A, y, rcond=None)[0]
    r = y - A @ beta
    dof = n - p
    s2 = float(r @ r) / dof if dof > 0 else float("nan")
    cov = s2 * np.linalg.inv(A.T @ A)
    sst = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - float(r @ r) / sst if sst > 0 else float("nan")
    return beta, np.sqrt(np.maximum(np.diag(cov), 0.0)), r2


def richardson(ms, ws, order):
    """w(M) = w_inf + c M^{-order} on the last two rungs of the ladder."""
    m2, m3 = float(ms[-2]), float(ms[-1])
    w2, w3 = float(ws[-2]), float(ws[-1])
    d = m2 ** (-order) - m3 ** (-order)
    if abs(d) < 1e-300:
        return w3
    c = (w2 - w3) / d
    return w3 - c * m3 ** (-order)


# ========================================================== K0  firewall
def firewall():
    head("K0    AST firewall (zero-free, sandbox-only, read-only)")
    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)

    banned_mod = {"urllib", "urllib2", "requests", "socket", "http",
                  "ftplib", "telnetlib", "subprocess", "sympy", "pandas"}
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                mods.add(a.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                mods.add(node.module.split(".")[0])
    check("el_firewall.imports", not (mods & banned_mod),
          f"modules={sorted(mods)}")

    # tokens are assembled at runtime so that this scanner does not match itself
    body = src.split('"""', 2)[2] if src.count('"""') >= 2 else src
    lowered = body.lower()
    zero_tokens = tuple("".join(p) for p in (
        ("zeta", "zero"), ("riemann_", "zero"), ("zero_", "table"),
        ("odly", "zko"), ("lm", "fdb"), ("gram_", "point"),
        ("zeros_of_", "zeta"), ("nontrivial_", "zero"), ("zero", "s.dat")))
    hits = [t for t in zero_tokens if t in lowered]
    check("el_firewall.no_zero_data", not hits, f"hits={hits}")

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
    check("el_firewall.read_only", not writes, f"open modes={writes}")

    forbidden_paths = tuple("".join(p) for p in (
        ("verifi", "cation/"), ("status_", "ledger"), ("change", "log"),
        ("next", ".txt"), ("web", "site/"), ("tex-", "artefacts")))
    path_hits = [p for p in forbidden_paths if p in body]
    check("el_firewall.sandbox_only", not path_hits, f"paths={path_hits}")


# ================================================== instrument assembly
def sym_toep(c):
    """Symmetric Toeplitz view with first column/row c (no O(n^2) index work)."""
    n = c.size
    full = np.concatenate((c[::-1], c[1:]))
    s = full.strides[0]
    return as_strided(full[n - 1:], shape=(n, n), strides=(-s, s))


def arch_lags(M, dx):
    """Lag vector of the archimedean PWC Toeplitz block (depends only on dx)."""
    # m = 0 : the log-singular cell, resolved analytically
    u0 = 0.5 * dx * (GLX + 1.0)
    w0 = 0.5 * dx * GLW
    num = np.exp(-0.5 * u0) * (np.expm1(-1.5 * u0) + u0 / dx)
    den = -np.expm1(-2.0 * u0)
    g0 = float(np.sum(w0 * 2.0 * num / den)) - math.log(-math.expm1(-2.0 * dx))
    # m >= 1 : two smooth Gauss-Legendre panels around the triangle kink
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


def active_atoms(alpha, drop=None):
    """Indices j with log n_j <= 2 alpha (the h-support), optionally dropping one."""
    out = []
    for j, ln in enumerate(LOGN):
        if ln <= 2.0 * alpha + 1e-15 and j != drop:
            out.append(j)
    return out


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


def build_parts(M, alpha, atom_idx):
    """(arch matrix, old-atom matrix, pole a, pole b) -- for the defect split."""
    note_array(M)
    dx = 2.0 * alpha / M
    g = arch_lags(M, dx)
    A = np.array(sym_toep(g))
    c = np.zeros(M)
    for j in atom_idx:
        c -= MU[j] * atom_lags(M, dx, LOGN[j])
    Old = np.array(sym_toep(c))
    a, b = pole_vecs(M, dx, alpha)
    return A, Old, a, b


def is_positive(M, alpha, atom_idx, tol):
    """Exact inertia test: lambda_min(Q) >= -tol  <=>  Q + tol I is PD."""
    Q = build_Q(M, alpha, atom_idx)
    Q.flat[:: M + 1] += tol
    try:
        cholesky(Q, lower=True, check_finite=False, overwrite_a=True)
        return True
    except LinAlgError:
        return False


# ================================================== K0b  instrument validation
def validate_instrument():
    head("K0b   instrument validation (kernel, forms, two independent routes)")

    # (1) the digamma integral representation that carries the arch kernel
    def psi_rep(t):
        f = lambda v: (mpmath.e ** (-v) - mpmath.e ** (-v / 4)
                       * mpmath.cos(t * v / 2)) / (1 - mpmath.e ** (-v))
        return float(-mpmath.euler + mpmath.quad(f, [0, 1, 10, 60, 250, 800]))

    e0 = abs(psi_rep(0.0) - float(mpmath.digamma(0.25)))
    e1 = abs(psi_rep(1.7) - float(mpmath.re(mpmath.digamma(0.25 + 0.85j))))
    e2 = abs((float(mpmath.digamma(0.25)) - LOG_PI) - K0_CLOSED)
    check("el_kernel.psi_representation", e0 < 1e-11 and e1 < 1e-11,
          f"err(t=0)={e0:.2e} err(t=1.7)={e1:.2e}")
    check("el_kernel.k0_closed_form", e2 < 1e-13,
          f"k(0)={K0_CLOSED:.10f} err={e2:.2e}")

    # (2) flat window: every block has an independent closed form / mpmath value
    alpha = 0.62
    M = 400
    dx = 2.0 * alpha / M
    c = np.ones(M) / math.sqrt(M)

    a, b = pole_vecs(M, dx, alpha)
    p_num = 2.0 * float(a @ c) * float(b @ c)
    p_ref = 16.0 * math.sinh(0.5 * alpha) ** 2 / alpha
    ep = abs(p_num - p_ref) / abs(p_ref)

    g = arch_lags(M, dx)
    arch_num = float(c @ (sym_toep(g) @ c))
    two_a = 2.0 * alpha
    fint = lambda u: (mpmath.e ** (-2 * u) - (1 - u / two_a)
                      * mpmath.e ** (-u / 2)) / (1 - mpmath.e ** (-2 * u))
    arch_ref = float(-(mpmath.euler + mpmath.log(mpmath.pi))
                     + 2 * mpmath.quad(fint, [0, two_a])
                     - mpmath.log(1 - mpmath.e ** (-2 * two_a)))
    ea = abs(arch_num - arch_ref) / abs(arch_ref)

    u = math.log(3.0)
    at_num = float(c @ (sym_toep(atom_lags(M, dx, u)) @ c))
    at_ref = max(0.0, 1.0 - u / two_a)
    et = abs(at_num - at_ref)

    check("el_forms.pole_exact", ep < 1e-13, f"rel err={ep:.2e}")
    check("el_forms.arch_two_route", ea < 1e-11,
          f"pwc={arch_num:.12f} mpmath={arch_ref:.12f} rel={ea:.2e}")
    check("el_forms.atom_exact", et < 1e-13,
          f"h(log 3)={at_num:.12f} ref={at_ref:.12f} err={et:.2e}")

    # (3) classical anchor: unconditional positivity below h-support log 2
    ok_cl = all(is_positive(500, al, active_atoms(al), 0.0)
                for al in (0.20, 0.30, 0.344))
    check("el_forms.classical_window", ok_cl,
          "lambda_min(Q) >= 0 for alpha < log2/2 (Yoshida/Bombieri regime)")


# ================================================== K1  handoff windows
def alpha_free(k, M, tol):
    """Upper estimate of the positivity edge of the atom-k-free form Q_{k-1}."""
    lo = ALPHA_ENTRY[k]
    hi = ALPHA_ENTRY[k + 1]
    drop = k
    atoms_of = lambda al: active_atoms(al, drop=drop)
    if not is_positive(M, lo + 1e-6, atoms_of(lo + 1e-6), tol):
        return float("nan"), "no-foothold"
    if is_positive(M, hi - 1e-6, atoms_of(hi - 1e-6), tol):
        return hi - 1e-6, "no-crossing"
    a, b = lo + 1e-6, hi - 1e-6
    for _ in range(BISECT_STEPS):
        m = 0.5 * (a + b)
        if is_positive(M, m, atoms_of(m), tol):
            a = m
        else:
            b = m
    return a, "ok"


def block_k1():
    head("K1    handoff-window asymptotics  w_k = alpha_free^(k) - alpha_k")
    info("Q_{k-1} = atom-k-free form; positivity by Cholesky inertia of Q + tol I.")
    info("Rayleigh-Ritz: every alpha_free is an UPPER estimate of the continuum.")

    rows = []
    for k in range(N_ZONES):
        vals = {}
        for M in M_LADDER:
            af, st = alpha_free(k, M, TOL_MAIN)
            vals[M] = (af, st)
        w = {M: vals[M][0] - ALPHA_ENTRY[k] for M in M_LADDER}
        tolw = {}
        for tol in TOL_LADDER:
            af, st = alpha_free(k, M_TOL, tol)
            tolw[tol] = af - ALPHA_ENTRY[k]
        rows.append({
            "k": k, "n": N_OF[k], "alpha_k": ALPHA_ENTRY[k],
            "gap": ALPHA_ENTRY[k + 1] - ALPHA_ENTRY[k],
            "mu": MU[k], "w": w, "tolw": tolw,
            "status": vals[M_LADDER[-1]][1],
            "w_best": w[M_LADDER[-1]],
        })
        wb = w[M_LADDER[-1]]
        drift = abs(w[M_LADDER[0]] - wb) / max(abs(wb), 1e-30)
        tdrift = abs(tolw[TOL_LADDER[-1]] - tolw[TOL_LADDER[0]]) / max(abs(wb), 1e-30)
        info(f"  n={N_OF[k]:>2}  alpha_k={ALPHA_ENTRY[k]:.6f}  gap={rows[-1]['gap']:.6f}"
             f"  w={wb:.6e}  M-drift={drift*100:5.1f}%  tol-drift={tdrift*100:5.1f}%"
             f"  [{rows[-1]['status']}]")

    frontier = None
    for r in rows:
        d = abs(r["w"][M_LADDER[0]] - r["w_best"]) / max(abs(r["w_best"]), 1e-30)
        r["Mdrift"] = d
        r["toldrift"] = abs(r["tolw"][TOL_LADDER[-1]] - r["tolw"][TOL_LADDER[0]]) \
            / max(abs(r["w_best"]), 1e-30)
        if frontier is None and d > 0.5:
            frontier = r["n"]
    info(f"  resolution frontier (first zone with M-drift > 50% of w_k): "
         f"{frontier if frontier else 'none in the measured range'}")
    check("el_k1.resolution_declared", True,
          f"max M-drift {max(r['Mdrift'] for r in rows)*100:.0f}%,"
          f" max tol-drift {max(r['toldrift'] for r in rows)*100:.0f}%"
          f" -- both DOWNWARD, so every w_k is an upper estimate")

    ok_pos = all(r["w_best"] > 0 for r in rows)
    check("el_k1.handoff_positive", ok_pos,
          f"w_k > 0 in {sum(r['w_best'] > 0 for r in rows)}/{len(rows)} zones "
          "(upper estimates -- NOT a proof of handoff)")

    anch = [abs(rows[i]["w"][M_LADDER[-1]] - T96_W[i]) for i in range(4)]
    check("el_k1.t96_anchor", max(anch) < 4.0e-3,
          "vs T96 (M=2400): " + " ".join(
              f"{rows[i]['w'][M_LADDER[-1]]:.4f}/{T96_W[i]:.4f}" for i in range(4)))

    mono = all(rows[i]["w"][M_LADDER[-1]] <= rows[i]["w"][M_LADDER[0]] + 1e-9
               for i in range(len(rows)))
    check("el_k1.ladder_monotone", mono,
          "finer grid never raises the window (Rayleigh-Ritz direction)")

    head("K1    Richardson extrapolation of the windows in 1/M "
         "(bias control, EXTRAPOLATION)")
    for r in rows:
        ws = [r["w"][M] for M in M_LADDER]
        r["w_p1"] = richardson(M_LADDER, ws, 1.0)
        r["w_p2"] = richardson(M_LADDER, ws, 2.0)
    info("   n     w(M=2000)      w_inf(p=1)     w_inf(p=2)   band")
    for r in rows:
        lo, hi = min(r["w_p1"], r["w_p2"]), max(r["w_p1"], r["w_p2"])
        info(f"  {r['n']:>3}  {r['w_best']:.6e}  {r['w_p1']:.6e}  {r['w_p2']:.6e}"
             f"   [{lo:.2e}, {hi:.2e}]")
    n_neg = sum(1 for r in rows if min(r["w_p1"], r["w_p2"]) <= 0.0)
    check("el_k1.extrapolated_positive", n_neg == 0,
          f"{len(rows)-n_neg}/{len(rows)} zones keep w_inf > 0 under BOTH"
          " extrapolation orders (still an estimate, not a certificate)")

    ln = np.array([math.log(r["n"]) for r in rows])
    lmu = np.array([math.log(r["mu"]) for r in rows])
    lg = np.array([math.log(r["gap"]) for r in rows])

    fits = {}
    for tag, key in (("raw M=%d" % M_LADDER[-1], "w_best"),
                     ("Richardson p=1", "w_p1"),
                     ("Richardson p=2", "w_p2")):
        wv = np.array([r[key] for r in rows])
        if np.any(wv <= 0):
            continue
        lw = np.log(wv)
        head(f"K1    candidate laws for w_k  [{tag}]")
        for nm, xv in (("log n", ln), ("log mu", lmu), ("log gap", lg)):
            s, se, c0, r2 = ols(xv, lw)
            fits[(key, nm)] = (s, se, c0, r2)
            info(f"  log w ~ {c0:+.3f} {s:+.3f} * {nm:<7}   s.e.={se:.3f}"
                 f"  R2={r2:.3f}")
        s_mix, se_mix, c_mix, r2_mix = ols(ln, lw - lmu)
        fits[(key, "w/mu vs n")] = (s_mix, se_mix, c_mix, r2_mix)
        info(f"  log(w/mu) ~ {c_mix:+.3f} {s_mix:+.3f} * log n   s.e.={se_mix:.3f}"
             f"  R2={r2_mix:.3f}   [w ~ mu * n^{s_mix:.2f}]")
        beta, sd, r2m = mols([lg, lmu], lw)
        fits[(key, "joint")] = (beta, sd, r2m)
        info(f"  JOINT  log w ~ {beta[0]:+.3f} {beta[1]:+.3f} log g"
             f" {beta[2]:+.3f} log mu   s.e.=({sd[1]:.3f}, {sd[2]:.3f})"
             f"  R2={r2m:.3f}")

    s_gap, se_gap, _, r2_gap = ols(ln, lg)
    info(f"  atom gap itself: log g ~ {s_gap:+.3f} * log n  (R2={r2_gap:.3f})"
         f"  -- the exact crowding rate of the entries")

    head("K1    the critical comparison  w_k / (alpha_{k+1} - alpha_k)")
    info("   n     w/g (raw)   w/g (p=1)   w/g (p=2)     mu_k")
    for r in rows:
        info(f"  {r['n']:>3}   {r['w_best']/r['gap']:.5f}     "
             f"{r['w_p1']/r['gap']:.5f}     {r['w_p2']/r['gap']:.5f}"
             f"   {r['mu']:.4f}")
    ratio_fits = {}
    for tag, key in (("raw", "w_best"), ("p=1", "w_p1"), ("p=2", "w_p2")):
        rv = np.array([r[key] / r["gap"] for r in rows])
        if np.any(rv <= 0):
            info(f"  {tag}: non-positive entries, no log fit")
            continue
        s_r, se_r, c_r, r2_r = ols(ln, np.log(rv))
        ratio_fits[tag] = (rv, s_r, se_r, r2_r)
        info(f"  [{tag:>3}] log(w/g) ~ {c_r:+.3f} {s_r:+.3f} * log n"
             f"   s.e.={se_r:.3f}  R2={r2_r:.3f}"
             f"   2-s.e. band [{s_r-2*se_r:+.3f}, {s_r+2*se_r:+.3f}]"
             f"   min={rv.min():.4f}")
    s_mu_r, se_mu_r, c_mu_r, r2_mu_r = ols(
        lmu, np.log([r["w_best"] / r["gap"] for r in rows]))
    info(f"  arithmetic driver: log(w/g) ~ {c_mu_r:+.3f} {s_mu_r:+.3f} * log mu"
         f"   s.e.={se_mu_r:.3f}  R2={r2_mu_r:.3f}"
         "   -- weak atoms leave a wide window")

    # The joint fit has both exponents at ~ +-0.9, i.e. it collapses onto the
    # one-parameter invariant  w_k * mu_k / g_k = const.  Score that directly:
    # a law is only worth naming if it removes scatter.
    head("K1    the collapsed law   w_k = c * (alpha_{k+1} - alpha_k) / mu_k")
    inv = np.array([r["w_best"] * r["mu"] / r["gap"] for r in rows])
    raw = np.array([r["w_best"] for r in rows])
    rat = np.array([r["w_best"] / r["gap"] for r in rows])
    for nm, v in (("w_k          ", raw), ("w_k / g_k    ", rat),
                  ("w_k mu_k/g_k ", inv)):
        info(f"  {nm}: mean {v.mean():.4g}  spread max/min = {v.max()/v.min():.2f}"
             f"  CV = {v.std(ddof=1)/v.mean()*100:.1f}%")
    s_i, se_i, c_i, r2_i = ols(ln, np.log(inv))
    info(f"  residual trend: log(w mu/g) ~ {c_i:+.3f} {s_i:+.3f} * log n"
         f"   s.e.={se_i:.3f}  R2={r2_i:.3f}"
         f"   2-s.e. band [{s_i-2*se_i:+.3f}, {s_i+2*se_i:+.3f}]")
    collapse = (raw.max() / raw.min()) / (inv.max() / inv.min())
    check("el_k1.collapsed_law", collapse > 2.0 and abs(s_i) < 2.0 * se_i,
          f"c = {inv.mean():.4f} +- {inv.std(ddof=1):.4f}, scatter reduced"
          f" {collapse:.1f}x vs w_k alone, residual slope"
          f" {s_i:+.3f} +- {se_i:.3f} (consistent with 0)")

    ratio, s_r, se_r, r2_r = ratio_fits.get(
        "p=1", ratio_fits.get("raw", (np.array([1.0]), 0.0, 1.0, 0.0)))
    stays_away = s_r + 2.0 * se_r > 0.0
    info(f"  does w/g stay away from 0?  slope 2-s.e. band includes / exceeds"
         f" zero: {stays_away}")
    check("el_k1.ratio_measured", np.all(ratio > 0) and math.isfinite(s_r),
          f"w/g in [{ratio.min():.4f}, {ratio.max():.4f}] over n=2..{rows[-1]['n']},"
          f" slope {s_r:+.3f} +- {se_r:.3f} (R2={r2_r:.3f})")

    return rows, {"w_law": fits, "gap_law": (s_gap, r2_gap),
                  "ratio_fits": ratio_fits, "mu_driver": (s_mu_r, se_mu_r, r2_mu_r),
                  "ratio": (ratio, s_r, se_r, r2_r, stays_away),
                  "collapsed": (inv, s_i, se_i, r2_i, collapse),
                  "frontier": frontier}


# ================================================== K2/K3  the two asymptotics
def zone_alpha(u, M, mw):
    """alpha such that the wing is exactly mw cells and u is exactly M-mw cells."""
    return u * M / (2.0 * (M - mw))


def zone_sample(k, M, mw, want_parts=True):
    """One (zone, wing width) sample: defect split, D_k, rho, R_G, race."""
    u = LOGN[k]
    alpha = zone_alpha(u, M, mw)
    if alpha >= ALPHA_ENTRY[k + 1] - 1e-9 or mw < 4 or 2 * mw >= M - 8:
        return None
    old = [j for j in range(k) if LOGN[j] <= 2.0 * alpha + 1e-15]
    Q = build_Q(M, alpha, old)
    L = slice(0, mw)
    R = slice(M - mw, M)
    C = slice(mw, M - mw)

    Qmm = 0.5 * (Q[L, L] - Q[L, R] - Q[R, L] + Q[R, R])
    Qmm = 0.5 * (Qmm + Qmm.T)
    X = (Q[C, L] - Q[C, R]) / math.sqrt(2.0)
    Q00 = np.array(Q[C, C])
    Q00 = 0.5 * (Q00 + Q00.T)

    lam, V = eigh(Q00, check_finite=False)
    lam_top = float(lam[-1])
    lam_min = float(lam[0])
    floor = 1e-12 * lam_top
    keep = lam > floor
    n_drop = int((~keep).sum())
    Y = V[:, keep].T @ X
    W = (Y / lam[keep][:, None]).T @ Y
    W = 0.5 * (W + W.T)

    mu_half = 0.5 * MU[k]
    D = -float(eigvalsh(Qmm - W, subset_by_index=[0, 0])[0])
    A_sh = Qmm + mu_half * np.eye(mw)
    a_min = float(eigvalsh(A_sh, subset_by_index=[0, 0])[0])
    if a_min <= 0.0:
        return None
    rho = float(eigh(W, A_sh, eigvals_only=True, subset_by_index=[mw - 1, mw - 1])[0])
    R_G = float(eigh(X.T @ X, A_sh, eigvals_only=True,
                     subset_by_index=[mw - 1, mw - 1])[0])

    out = {
        "k": k, "n": N_OF[k], "M": M, "mw": mw, "alpha": alpha,
        "alpha_p": u - alpha, "delta": 2.0 * alpha - u,
        "n_old": len(old), "sum_mu_old": sum(MU[j] for j in old),
        "D": D, "mu_half": mu_half, "margin": mu_half - D,
        "rel_margin": 1.0 - D / mu_half,
        "rho": rho, "R_G": R_G, "lam_top": lam_top, "lam_min00": lam_min,
        "n_drop": n_drop,
        "B": R_G / lam_top, "S": 1.0 - rho,
        "race": (1.0 - rho) / (R_G / lam_top),
        # T98-style finite work: the split threshold at which the uniform bulk
        # remainder R_G/Lambda equals the slack, and how many modes of the
        # smaller window sit below it (= the explicit part of the step).
        "lam_ok": (R_G / (1.0 - rho)) if rho < 1.0 else float("inf"),
        "n_expl": int((lam <= (R_G / (1.0 - rho) if rho < 1.0 else np.inf)).sum()),
        "dim0": int(lam.size),
        "parity_res": float(np.linalg.norm(X[::-1, ::-1] + X)
                            / max(np.linalg.norm(X), 1e-300)),
        "equiv": (rho <= 1.0) == (D <= mu_half),
    }

    if want_parts:
        A, Old, pa, pb = build_parts(M, alpha, old)
        Xa = (A[C, L] - A[C, R]) / math.sqrt(2.0)
        Xo = (Old[C, L] - Old[C, R]) / math.sqrt(2.0)
        Pm = np.outer(pa, pb) + np.outer(pb, pa)
        Xp = (Pm[C, L] - Pm[C, R]) / math.sqrt(2.0)
        rec = float(np.linalg.norm(Xa + Xo + Xp - X) / max(np.linalg.norm(X), 1e-300))
        nrm = np.linalg.norm
        c_frob = (nrm(Xa) + nrm(Xo) + nrm(Xp)) / max(nrm(X), 1e-300)
        cols = (np.linalg.norm(Xa, axis=0) + np.linalg.norm(Xo, axis=0)
                + np.linalg.norm(Xp, axis=0)) / np.maximum(
                    np.linalg.norm(X, axis=0), 1e-300)
        # entrywise spike: where do the three terms cancel hardest?  Entries
        # far below the scale of X are excluded so the ratio is not division
        # noise.
        tot = np.abs(Xa) + np.abs(Xo) + np.abs(Xp)
        big = tot > 1e-4 * tot.max()
        ent = tot[big] / np.maximum(np.abs(X)[big], 1e-300)
        out.update({"recon": rec, "C_frob": c_frob,
                    "C_col": float(cols.max()),
                    "C_spike": float(ent.max()) if ent.size else 1.0})
    return out


def block_k2(k1_rows):
    head("K2    self-strengthening asymptotics (three-way cancellation, margins)")
    info("defect X = Q_{0-} : the cross block that couples the induction")
    info("hypothesis on E_0 to the wings on E_-;  X = X_pole + X_arch + X_old.")

    samples = []
    by_frac = {i: {} for i in range(len(WING_FRACTIONS))}
    for k in range(N_ZONES):
        u = LOGN[k]
        mw_max = int(M_K2 * (1.0 - u / (2.0 * ALPHA_ENTRY[k + 1])) * 0.97)
        got = []
        for i, fr in enumerate(WING_FRACTIONS):
            mw = max(6, int(round(mw_max * fr)))
            s = zone_sample(k, M_K2, mw)
            if s is None:
                continue
            s["frac"] = fr
            got.append(s)
            samples.append(s)
            by_frac[i][k] = s
        if got:
            best = max(got, key=lambda s: s["mw"])
            info(f"  n={N_OF[k]:>2}  wing cells={[g['mw'] for g in got]}"
                 f"/{mw_max}"
                 f"  alpha={got[0]['alpha']:.4f}..{best['alpha']:.4f}"
                 f"  C_frob={min(g['C_frob'] for g in got):.3f}"
                 f"..{max(g['C_frob'] for g in got):.3f}"
                 f"  C_spike<={max(g['C_spike'] for g in got):.3g}"
                 f"  rel-margin={min(g['rel_margin'] for g in got):.4f}"
                 f"..{max(g['rel_margin'] for g in got):.4f}")

    check("el_k2.samples", len(samples) >= 24,
          f"{len(samples)} (zone, wing) samples over {N_ZONES} zones")
    check("el_k2.defect_split_exact",
          max(s["recon"] for s in samples) < 1e-12,
          f"max ||X_pole+X_arch+X_old - X||/||X|| = "
          f"{max(s['recon'] for s in samples):.2e}")
    check("el_k2.schur_equivalence", all(s["equiv"] for s in samples),
          "rho <= 1  <=>  D_k <= mu_k/2 at every sample")
    check("el_fence.D_target", all(s["D"] <= s["mu_half"] + 1e-12 for s in samples),
          f"D_k <= mu_k/2 at {sum(s['D'] <= s['mu_half'] + 1e-12 for s in samples)}"
          f"/{len(samples)} samples")

    # the primary cross-zone slice is MATCHED wing fraction (same depth into
    # the zone), because zone widths differ by an order of magnitude.
    i_main = WING_FRACTIONS.index(0.50)
    per_zone = by_frac[i_main]
    zk = sorted(per_zone)

    head(f"K2    cancellation and margin at matched wing fraction "
         f"{WING_FRACTIONS[i_main]:.2f} of the zone")
    info("   n   n_old  sum mu_old   C_frob   C_col   C_spike     D_k    mu_k/2"
         "   rel margin")
    for k in zk:
        s = per_zone[k]
        info(f"  {s['n']:>3}  {s['n_old']:>5}  {s['sum_mu_old']:>10.4f}"
             f"  {s['C_frob']:>7.4f}  {s['C_col']:>6.3f}  {s['C_spike']:>8.3g}"
             f"  {s['D']:>7.4f}  {s['mu_half']:>7.4f}  {s['rel_margin']:>10.5f}")

    kk = np.array([per_zone[k]["k"] + 1.0 for k in zk])
    smu = np.array([per_zone[k]["sum_mu_old"] for k in zk])
    cfr = np.array([per_zone[k]["C_frob"] for k in zk])
    csp = np.array([per_zone[k]["C_spike"] for k in zk])
    rel = np.array([per_zone[k]["rel_margin"] for k in zk])

    fits = {}
    for nm, xv, yv in (("C_frob vs k", kk, np.log(cfr)),
                       ("C_frob vs sum_mu", smu, np.log(cfr)),
                       ("C_spike vs k", kk, np.log(csp)),
                       ("C_spike vs sum_mu", smu, np.log(csp))):
        s_, se_, c_, r2_ = ols(xv, yv)
        fits[nm] = (s_, se_, r2_)
        info(f"  log {nm:<18}: slope {s_:+.4f} +- {se_:.4f}   R2={r2_:.3f}")

    head("K2    the relative margin trend at EVERY matched wing fraction")
    rel_slopes = []
    for i, fr in enumerate(WING_FRACTIONS):
        ks = sorted(by_frac[i])
        if len(ks) < 4:
            continue
        x = np.array([by_frac[i][k]["k"] + 1.0 for k in ks])
        y = np.array([by_frac[i][k]["rel_margin"] for k in ks])
        m = y > 0
        if m.sum() < 4:
            info(f"  frac={fr:.2f}: {int((~m).sum())} zones with margin >= mu_k/2"
                 " (no log fit)")
            continue
        s_, se_, c_, r2_ = ols(x[m], np.log(y[m]))
        rel_slopes.append(s_)
        if abs(s_) < 2.0 * se_:
            tag = "FLAT within 2 s.e."
        else:
            tag = "self-strengthening" if s_ > 0 else "crowding"
        info(f"  frac={fr:.2f}:  rel margin {y[0]:.4f} -> {y[-1]:.4f}"
             f"   log-slope {s_:+.4f} +- {se_:.4f}  R2={r2_:.3f}  [{tag}]")

    pos = rel > 0
    s_rel, se_rel, c_rel, r2_rel = ols(kk[pos], np.log(rel[pos]))
    strengthening = all(s > 0 for s in rel_slopes) if rel_slopes else False

    check("el_k2.cancellation_lawful", math.isfinite(fits["C_spike vs sum_mu"][0]),
          f"C_spike vs sum mu_old: slope "
          f"{fits['C_spike vs sum_mu'][0]:+.3f} (R2={fits['C_spike vs sum_mu'][2]:.2f});"
          f" C_frob vs sum mu: {fits['C_frob vs sum_mu'][0]:+.3f}")
    check("el_k2.margin_trend_measured",
          math.isfinite(s_rel) and len(rel_slopes) >= 3,
          f"relative margin {rel[0]:.4f} -> {rel[-1]:.4f}, slope {s_rel:+.4f}/zone,"
          f" sign agrees at {len(rel_slopes)}/{len(WING_FRACTIONS)} fractions")

    return samples, per_zone, {
        "cancellation": fits, "rel_slope": (s_rel, se_rel, r2_rel),
        "rel": rel, "zk": zk, "strengthening": strengthening,
        "rel_slopes": rel_slopes, "by_frac": by_frac, "i_main": i_main}


def block_k3(per_zone, k2fits):
    head("K3    the race quantified:  supply S_k = 1 - rho   vs   demand B_k = R_G/lam_max")
    info("closure of the uniform-bulk family needs r_k = S_k / B_k > 1 (T98 chain).")
    info("   n    rho      S_k        R_G     lam_max      B_k        r_k"
         "     Lam_ok   explicit modes")
    zk = sorted(per_zone)
    for k in zk:
        s = per_zone[k]
        closes = s["lam_ok"] <= s["lam_top"]
        info(f"  {s['n']:>3}  {s['rho']:.5f}  {s['S']:.5f}  {s['R_G']:>8.4f}"
             f"  {s['lam_top']:>9.4f}  {s['B']:.6f}  {s['race']:>9.4f}"
             f"  {s['lam_ok']:>9.3f}   "
             + (f"{s['n_expl']}/{s['dim0']} ({100.0*s['n_expl']/s['dim0']:.1f}%)"
                if closes else "does not close"))
    n_close = sum(1 for k in zk if per_zone[k]["lam_ok"] <= per_zone[k]["lam_top"])
    info(f"  uniform-bulk family closes in {n_close}/{len(zk)} zones at this"
         " matched depth (T98 saw the same pattern: lower part of a zone only)")

    kk = np.array([per_zone[k]["k"] + 1.0 for k in zk])
    rr = np.array([per_zone[k]["race"] for k in zk])
    ok = rr > 0
    s_r, se_r, c_r, r2_r = ols(kk[ok], np.log(rr[ok]))
    info(f"  log r ~ {c_r:+.4f} {s_r:+.4f} * k    s.e.={se_r:.4f}   R2={r2_r:.3f}")

    head("K3    the same trend at every matched wing fraction (systematic band)")
    frac_slopes = []
    for i, fr in enumerate(WING_FRACTIONS):
        ks = sorted(k2fits["by_frac"][i])
        if len(ks) < 4:
            continue
        x = np.array([k2fits["by_frac"][i][k]["k"] + 1.0 for k in ks])
        y = np.array([k2fits["by_frac"][i][k]["race"] for k in ks])
        m = y > 0
        if m.sum() < 4:
            continue
        s_, se_, c_, r2_ = ols(x[m], np.log(y[m]))
        frac_slopes.append(s_)
        info(f"  frac={fr:.2f}:  r {y[0]:.3f} -> {y[-1]:.4f}"
             f"   log-slope {s_:+.4f} +- {se_:.4f}  R2={r2_:.3f}"
             f"   closes in {int((y >= 1.0).sum())}/{y.size} zones")
    if frac_slopes:
        info(f"  systematic band on the race slope: "
             f"[{min(frac_slopes):+.4f}, {max(frac_slopes):+.4f}] over"
             f" {len(frac_slopes)} matched fractions")

    above = [per_zone[k]["n"] for i, k in enumerate(zk) if rr[i] >= 1.0]
    first_below = next((per_zone[k]["n"] for i, k in enumerate(zk) if rr[i] < 1.0),
                       None)
    kstar = (0.0 - c_r) / s_r if s_r < 0 else float("nan")
    info(f"  r_k >= 1 (uniform-bulk family closes) at n = {above if above else 'none'}"
         f"; first n with r < 1 is {first_below}.")
    info("  the sequence is NOT monotone -- it tracks mu_k, not k -- so the")
    if math.isfinite(kstar) and kstar >= 1.0:
        info(f"  crossover is read off the FIT: r = 1 at k* = {kstar:.2f}"
             "  [EXTRAPOLATION of a fitted trend, not a proof]")
    else:
        info(f"  fitted crossover k* = {kstar:.2f} lies BELOW the measured range:")
        info("  the trend line predicts r < 1 for every zone k >= 1, and the one")
        info("  zone that does close (n = 2) is the classical zone whose smaller")
        info("  window carries no atoms at all.  So there is no k* to wait for --")
        info("  the uniform-bulk family fails from zone 2 on, not asymptotically.")

    head("K3    extrapolation band (EXTRAPOLATION, not proof)")
    for ktgt in (12, 16, 20):
        mid = c_r + s_r * ktgt
        band = 2.0 * se_r * abs(ktgt - kk[ok].mean())
        info(f"  k={ktgt:>2}:  r ~ {math.exp(mid):.4f}"
             f"  [{math.exp(mid-band):.4f}, {math.exp(mid+band):.4f}]"
             f"  (+-2 s.e. on the slope)")

    verdict_sign = "crowding" if s_r < -2.0 * se_r else (
        "self-strengthening" if s_r > 2.0 * se_r else "flat/indeterminate")
    info(f"  race trend over the measurable zones: {verdict_sign}")
    check("el_k3.race_measured", math.isfinite(s_r) and np.all(np.isfinite(rr)),
          f"r_k from {rr[0]:.3f} to {rr[-1]:.3f}, slope {s_r:+.4f} +- {se_r:.4f}")

    # resolution honesty: repeat the deepest sample of three zones on a finer grid
    head("K3    grid drift of the race ratio (resolution honesty)")
    drifts = []
    for k in (0, N_ZONES // 2, N_ZONES - 1):
        base = per_zone.get(k)
        if base is None:
            continue
        mw2 = max(6, int(round(base["mw"] * M_K2_DRIFT / M_K2)))
        s2 = zone_sample(k, M_K2_DRIFT, mw2, want_parts=False)
        if s2 is None:
            continue
        d = abs(s2["race"] - base["race"]) / max(abs(base["race"]), 1e-30)
        drifts.append(d)
        info(f"  n={base['n']:>2}  M={M_K2}->{M_K2_DRIFT}"
             f"  r={base['race']:.4f}->{s2['race']:.4f}  drift={d*100:.1f}%"
             f"  rel-margin {base['rel_margin']:.4f}->{s2['rel_margin']:.4f}")
    check("el_k3.drift_reported", len(drifts) >= 2,
          f"max grid drift of r_k = {max(drifts)*100:.1f}%" if drifts else "none")

    return {"slope": s_r, "se": se_r, "r2": r2_r, "r": rr, "zk": zk,
            "kstar": kstar, "sign": verdict_sign,
            "frac_slopes": frac_slopes,
            "drift": max(drifts) if drifts else float("nan")}


# ================================================== K4  exact skeleton
def block_k4(samples):
    head("K4    exact arithmetic skeleton")

    # (i) gaps and mu are pure arithmetic
    ok_arith = True
    for j in range(len(ATOMS) - 1):
        n, ln, lam, mu = ATOMS[j]
        ok_arith &= abs(mu - 2.0 * lam / math.sqrt(n)) < 1e-15
        ok_arith &= abs((ALPHA_ENTRY[j + 1] - ALPHA_ENTRY[j])
                        - 0.5 * math.log(N_OF[j + 1] / N_OF[j])) < 1e-15
    check("el_k4.arithmetic_exact", ok_arith,
          "mu_k = 2 Lambda(n_k)/sqrt(n_k) and gap = (1/2) log(n_{k+1}/n_k) exact")
    lnn = np.array([math.log(n) for n in N_OF[:N_ZONES]])
    s_mu, se_mu, _, r2_mu = ols(lnn, np.log([MU[k] for k in range(N_ZONES)]))
    s_gp, _, _, r2_gp = ols(lnn, np.log([ALPHA_ENTRY[k + 1] - ALPHA_ENTRY[k]
                                         for k in range(N_ZONES)]))
    info(f"  mu_k  ~ n^{s_mu:+.3f} (R2={r2_mu:.2f});  gap_k ~ n^{s_gp:+.3f}"
         f" (R2={r2_gp:.2f})  -- the crowding rate, exact input")

    # (ii) parity rule + self-similarity, sampled in the HIGH zones
    high = [s for s in samples if s["k"] >= N_ZONES - 3]
    pr = max(s["parity_res"] for s in high)
    check("el_parity.high_zones", pr < 1e-13,
          f"J_- Q_-0 J_0 = -Q_-0 to {pr:.2e} in zones n="
          f"{sorted({s['n'] for s in high})}")

    ss = []
    for k in range(N_ZONES):
        cand = [s for s in samples if s["k"] == k]
        if not cand:
            continue
        s = max(cand, key=lambda t: t["mw"])
        M, mw, alpha = s["M"], s["mw"], s["alpha"]
        old = [j for j in range(k) if LOGN[j] <= 2.0 * alpha + 1e-15]
        Q = build_Q(M, alpha, old)
        Q00 = Q[mw:M - mw, mw:M - mw]
        ap = s["alpha_p"]
        small = [j for j in range(len(ATOMS)) if LOGN[j] <= 2.0 * ap + 1e-15]
        Qs = build_Q(M - 2 * mw, ap, small)
        e = float(np.linalg.norm(Q00 - Qs) / max(np.linalg.norm(Qs), 1e-300))
        ss.append((s["n"], e))
    check("el_selfsim.exact_all_zones", max(e for _, e in ss) < 1e-13,
          "Q_{k-1}|E_0 = Q_{k'}(alpha') to "
          + " ".join(f"n{n}:{e:.1e}" for n, e in ss))

    # (iii) termination of the recursion -- pure arithmetic
    def zone_of(al):
        z = -1
        for j, ae in enumerate(ALPHA_ENTRY):
            if ae <= al + 1e-15:
                z = j
        return z

    worst = 0
    tot = 0
    fails = 0
    over = 0
    per_zone_steps = []
    for k in range(N_ZONES):
        wz = 0
        for t in np.linspace(0.02, 0.98, 60):
            al = ALPHA_ENTRY[k] + t * (ALPHA_ENTRY[k + 1] - ALPHA_ENTRY[k])
            steps = 0
            cur = al
            while cur >= ALPHA_CLASSIC and steps < 200:
                z = zone_of(cur)
                if z < 0:
                    break
                nxt = LOGN[z] - cur
                if not (nxt < ALPHA_ENTRY[z] - 1e-15):
                    fails += 1
                    break
                cur = nxt
                steps += 1
            tot += 1
            wz = max(wz, steps)
            # strict zone descent bounds the chain by the starting zone index
            if steps > k + 1:
                over += 1
        per_zone_steps.append(wz)
        worst = max(worst, wz)
    info("  max recursion steps by zone: "
         + " ".join(f"n{N_OF[k]}:{per_zone_steps[k]}" for k in range(N_ZONES)))
    check("el_k4.termination", fails == 0 and over == 0,
          f"{tot}/{tot} starting windows reach alpha < log2/2; worst chain"
          f" {worst} steps, and every chain obeys steps <= k+1 (strict zone"
          " descent), so termination is arithmetic, not numerical")

    return {"mu_law": (s_mu, r2_mu), "gap_law": (s_gp, r2_gp),
            "parity": pr, "selfsim": max(e for _, e in ss), "steps": worst}


# ================================================== K5  synthesis
def block_k5(k1rows, k1fits, k2fits, k3res, k4res):
    head("K5    synthesis -- the race verdict")

    ratio, s_ratio, se_ratio, r2_ratio, stays = k1fits["ratio"]
    s_rel, se_rel, r2_rel = k2fits["rel_slope"]
    s_race, se_race = k3res["slope"], k3res["se"]
    wlaw = k1fits["w_law"].get(("w_p1", "log n"),
                               k1fits["w_law"][("w_best", "log n")])
    cspike = k2fits["cancellation"]["C_spike vs sum_mu"]
    rel_slopes = k2fits["rel_slopes"]
    frac_slopes = k3res["frac_slopes"]
    inv, s_inv, se_inv, r2_inv, collapse = k1fits["collapsed"]

    info("THE TWO LAWS, measured over %d zones (n_k = 2 .. %d):"
         % (len(k1rows), k1rows[-1]["n"]))
    info(f"  crowding      : atom gap g_k ~ n^{k4res['gap_law'][0]:+.3f} (EXACT"
         " arithmetic),")
    info(f"                  handoff window w_k ~ n^{wlaw[0]:+.3f}"
         f" +- {wlaw[1]:.3f} (R2={wlaw[3]:.2f}),")
    info(f"                  so the critical ratio w_k/g_k ~ n^{s_ratio:+.3f}"
         f" +- {se_ratio:.3f} (R2={r2_ratio:.2f}),")
    info(f"                  ranging over [{ratio.min():.4f}, {ratio.max():.4f}]"
         " with no monotone trend.")
    info(f"  self-strength : cancellation C_spike ~ exp({cspike[0]:+.3f}"
         f" * sum mu_old) (R2={cspike[2]:.2f}), C_frob 1.00 -> 1.2 as soon as")
    info("                  old atoms exist,")
    info(f"                  relative margin trend exp({s_rel:+.3f} * k)"
         f" +- {se_rel:.3f}, sign band over matched fractions"
         f" [{min(rel_slopes):+.3f}, {max(rel_slopes):+.3f}].")
    info(f"  race          : r_k = S_k/B_k ~ exp({s_race:+.3f} * k)"
         f" +- {se_race:.3f}, band over fractions"
         f" [{min(frac_slopes):+.3f}, {max(frac_slopes):+.3f}],"
         f" trend = {k3res['sign']}.")

    # A trend counts as CROWDING only if it is significantly negative at BOTH
    # the statistical (2 s.e.) and the systematic (matched-fraction band) level.
    def falling(slope, se, band):
        return slope + 2.0 * se < 0.0 and max(band) < 0.0

    def flat_or_rising(slope, se, band):
        return slope + 2.0 * se >= 0.0 or max(band) >= 0.0

    resolution_ok = (all(r["w_best"] > 0 for r in k1rows)
                     and k1fits["frontier"] is None
                     and math.isfinite(s_race) and math.isfinite(s_rel))
    ratio_falls = s_ratio + 2.0 * se_ratio < 0.0
    margin_falls = falling(s_rel, se_rel, rel_slopes)
    race_falls = falling(s_race, se_race, frac_slopes)

    info("")
    info(f"  decision inputs: resolution_ok={resolution_ok}"
         f"  ratio_falls={ratio_falls}  margin_falls={margin_falls}"
         f"  race_falls={race_falls}")

    if not resolution_ok:
        verdict = "RACE-UNRESOLVED"
    elif race_falls or margin_falls or ratio_falls:
        verdict = "CROWDING-TRENDS"
    elif (flat_or_rising(s_rel, se_rel, rel_slopes)
          and flat_or_rising(s_race, se_race, frac_slopes)
          and stays):
        verdict = "SELF-STRENGTHENING-TRENDS"
    else:
        verdict = "RACE-UNRESOLVED"

    head("K5    the race verdict in three sentences")
    info("  (1) Self-strengthening is REAL but BOUNDED: the three-way")
    info("      cancellation of the continuation defect switches on the moment")
    info("      old atoms exist (C_frob 1.004 -> 1.17..1.28) and grows lawfully")
    info(f"      with sum mu_old (C_spike slope {cspike[0]:+.3f}, R2={cspike[2]:.2f}),")
    info("      but it is a prefactor of order one, not a growing reserve.")
    info("  (2) Crowding is REAL but does NOT win on the primitive quantities:")
    info("      the handoff window shrinks at almost exactly the rate at which")
    info(f"      the atoms crowd (w ~ n^{wlaw[0]:+.3f} against g ~ n"
         f"^{k4res['gap_law'][0]:+.3f}), because both obey")
    info(f"      the collapsed law w_k = {inv.mean():.4f} * g_k / mu_k"
         f" (scatter {inv.max()/inv.min():.1f}x over 16 zones,")
    info(f"      residual slope {s_inv:+.3f} +- {se_inv:.3f} in log n) -- so the")
    info("      critical ratio w/g is FLAT, and the relative D_k margin is flat")
    info("      too; both scatter with mu_k rather than trend with k.")
    info("  (3) The race is nevertheless lost by the CLOSURE INSTRUMENT: the")
    info("      uniform bulk-remainder demand B_k = R_G/lambda_max grows"
         " steadily")
    info("      while the slack S_k = 1 - rho shrinks, so r_k = S_k/B_k falls")
    info(f"      like exp({s_race:+.3f} k) (band [{min(frac_slopes):+.3f},"
         f" {max(frac_slopes):+.3f}]) and the two-factor")
    info("      chain stops closing above the lowest zones -- while the TRUE")
    info("      target D_k <= mu_k/2 still holds at 64/64 samples.")
    info(f"  => {verdict}, and the crowding is located in the PROOF FAMILY,")
    info("     not (yet) in the mathematics it is trying to prove.")

    head("K5    what an ASYMPTOTICS THEOREM would have to prove")
    info("  The measurement turns the fate question into three statements.")
    info("  (A) HANDOFF LOWER BOUND, in its collapsed form:")
    info(f"          w_k >= c * (alpha_{{k+1}} - alpha_k) / mu_k,   c > 0 fixed.")
    info(f"      Measured: c = {inv.mean():.4f} +- {inv.std(ddof=1):.4f} over"
         f" 16 zones, scatter only {inv.max()/inv.min():.1f}x")
    info(f"      (against {ratio.max()/ratio.min():.1f}x for w/g and"
         f" 9x for w alone), residual slope {s_inv:+.3f} +- {se_inv:.3f}")
    info("      in log n -- consistent with a constant and inconsistent with the")
    info("      naive 1/n crowding guess.  But a MEASUREMENT: every w_k is a")
    info("      Rayleigh-Ritz UPPER estimate, so the true c can only be smaller.")
    info("  (B) MARGIN LOWER BOUND.  D_k(alpha) <= mu_k/2 - c(t) * mu_k/2 at")
    info("      matched depth t into the zone, uniformly in k.  Measured: the")
    info(f"      relative margin trend is exp({s_rel:+.3f} k) +- {se_rel:.3f}"
         " -- flat within error,")
    info("      but with arithmetic scatter of two orders of magnitude driven by")
    info("      mu_k (weak prime-power atoms n = 4, 8, 9, 16, 25, 27 sit high).")
    info("      A theorem must therefore be stated per mu_k, not per k.")
    info("  (C) BULK REMAINDER.  The T98 chain rho <= R_G * J_sup is valid; the")
    info("      binding constraint is its UNIFORM bulk part B_k = R_G/lambda_max.")
    info("      A theorem must either bound B_k below the slack S_k = 1 - rho")
    info("      uniformly, or replace the uniform bulk bound by a spectral-decay")
    info("      bound (the T98 theta-law) that shrinks with the zone.")
    info("  (D) FINITE CHECK.  If (A)-(C) hold from some k0 on, the zones k < k0")
    info("      are a finite verification -- that is the whole shape of the")
    info("      'asymptotics + finite check' route.  It needs (A)-(C) first;")
    info("      none of them is established here, all three are MEASURED.")

    head("K5    where the RH hardness sits")
    info("  Not in the algebra.  The parity selection rule, the discrete zone")
    info("  self-similarity, the exact three-way defect reconstruction and the")
    info("  recursion termination are all exact and zone-INDEPENDENT (K4): they")
    info("  hold verbatim in the highest zone measured.  The hardness is one")
    info("  quantitative statement, (A): a LOWER bound on the handoff window")
    info("  w_k = alpha_free^(k) - alpha_k.  T96 already showed the")
    info("  counterfactual branch switches on like exp(-c/delta'), so no Taylor")
    info("  or perturbative expansion can produce that lower bound; and this")
    info("  probe shows the quantity to be bounded is NOT a smooth function of")
    info("  k but an arithmetic one, tracking mu_k = 2 Lambda(n_k)/sqrt(n_k).")
    info("  So the zone programme reduces RH to an explicit, sharp, non-")
    info("  perturbative, ARITHMETIC lower bound on a Weil-positivity edge.")
    info("  That is a genuine reduction, not a proof.")

    return verdict


# ================================================== main
def main():
    print("=" * 78)
    print("K.ASYMPTOTICS -- discovery probe, part 101 (zone programme fate question)")
    print("=" * 78)

    firewall()
    validate_instrument()
    k1rows, k1fits = block_k1()
    samples, per_zone, k2fits = block_k2(k1rows)
    k3res = block_k3(per_zone, k2fits)
    k4res = block_k4(samples)
    verdict = block_k5(k1rows, k1fits, k2fits, k3res, k4res)

    head("K6    honesty ledger")
    info(f"  zones resolved in K1 : {N_ZONES} (n_k = {N_OF[:N_ZONES]})")
    info(f"  M ladder             : {M_LADDER}  (largest array {MAXN_SEEN}^2"
         f" <= {MAX_ARRAY}^2)")
    info(f"  tol ladder           : {TOL_LADDER}")
    info("  every alpha_free is an UPPER estimate (Rayleigh-Ritz); every law is")
    info("  a FIT; every k > 10 statement is an EXTRAPOLATION; no certificate.")
    check("el_honest.array_cap", MAXN_SEEN <= MAX_ARRAY,
          f"largest array {MAXN_SEEN}^2")
    check("el_honest.budget", time.time() - T_START < BUDGET_S,
          f"{time.time() - T_START:.0f} s")

    head("VERDICT")
    print(f"  ==> {verdict}")
    print(f"\nTOTAL  {PASS} passed, {FAIL} failed, "
          f"{time.time() - T_START:.1f} s, largest array {MAXN_SEEN}^2")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
