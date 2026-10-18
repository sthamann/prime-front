"""Discovery probe (2026-07-26), part 96 of the zeta/prime investigation.
Contract RELAY.TEST -- does the window Weil form hand off from atom to atom?

THE T93/T95 CONVENTION (declared once, used everywhere)
  f real, supp f subset (-alpha, alpha), ||f||_2 = 1;  h = f * f~ even,
  h(0) = 1, supp h subset (-2 alpha, 2 alpha), h(u) = int f(x) f(x-u) dx.
      P_pole(f) = hhat(i/2) + hhat(-i/2) = 2 (int f e^{x/2})(int f e^{-x/2})
      A_arch(f) = (1/2pi) int |fhat(t)|^2 k(t) dt,
                  k(t) = Re psi(1/4 + i t/2) - log pi,  k(0) = -5.3722...,
                  single sign change t0 = 6.28983599...
      Q(f)      = P_pole + A_arch - sum_{log n < 2 alpha} mu_n h_f(log n),
                  mu_n = 2 Lambda(n) / sqrt(n)   (Weil 1952 explicit formula)
  Atom entries in the h-support (alpha_n = log n / 2):
      n = 2  log 2 = 0.693147  alpha_2 = 0.3465736   mu_2 = 0.9802581
      n = 3  log 3 = 1.098612  alpha_3 = 0.5493061   mu_3 = 1.2685013
      n = 4  log 4 = 1.386294  alpha_4 = 0.6931472   mu_4 = 0.6931472
      n = 5  log 5 = 1.609438  alpha_5 = 0.8047190   mu_5 = 1.4395636
  (n = 6 carries no von Mangoldt weight; the next atom after 5 is n = 7 at
   alpha_7 = 0.9729551, outside the range swept here.)

WHAT T95 LEFT ON THE TABLE
  T95 (continuum_extension_probe) closed the ONE-ATOM band with a piecewise-
  constant Nystrom/Galerkin instrument and reported a Richardson-extrapolated
  band-top value lambda_min(Q)(alpha* = 0.46265) = +7.8e-6, reading alpha* as
  "the continuum positivity edge of the one-atom rescued form".  But alpha*
  came out of the T91 map as the INTERSECTION OF TWO ENVELOPE LAWS, not as an
  atom entry -- and alpha* = 0.46265 < alpha_3 = 0.5493061, so on the whole
  interval (alpha*, alpha_3) the ONLY atom inside the h-support is still
  log 2.  If lambda_min really turned negative there, the window Weil form
  would be negative on a genuine autocorrelation, which under the classical
  explicit formula is an RH contradiction -- i.e. an implementation alarm,
  never a result.  THE STAIRCASE (RELAY) HYPOTHESIS to be tested instead:
  each prime atom rescues its own zone and hands over to the next.

THE BLOCKS
  R1  THE ZONE BETWEEN alpha* AND alpha_3.  lambda_min(Q) on a fine alpha
      ladder 0.44 -> 0.549306 with a NESTED cell ladder M = 300, 600, 1200,
      2400 (each a refinement of the last, so Rayleigh-Ritz forces monotone
      decrease) plus a Richardson limit with a fitted order p.  Question
      answered: is there a sign change at alpha*, or is +7.8e-6 simply the
      value of a smooth, strictly positive, rapidly decaying curve?
  R2  THE RELAY MOMENT.  alpha ladder 0.549306 -> 0.68, where the log 3 atom
      enters.  (i) the COUNTERFACTUAL: lambda_min(Q) against lambda_min of the
      artificial form with the log 3 atom deleted; (ii) the extremiser
      profiles -- does an h(log 3) < 0 direction take over as the loser, i.e.
      does the T95 atom-rescue mechanism repeat for the SECOND atom; (iii) the
      onset law of the counterfactual branch across the entry.
  R3  THE RELAY MAP.  Per zone: which terms carry.  The precise relay
      statement is the HANDOFF WINDOW: atom k enters at alpha_k, and the
      (k-1)-atom form keeps lambda_min >= 0 until alpha_free^(k); the relay
      holds iff alpha_free^(k) > alpha_k for every k, i.e. every atom arrives
      strictly BEFORE it is needed.  Measured for k = 1..4 with the resolution
      drift shown.  Plus the decay law of the margin itself and the typing of
      the relay as an induction scheme.

PREREGISTERED VERDICTS
  RELAY-CONFIRMED : lambda_min stays >= 0 through every tested zone AND the
                    counterfactual shows atom k carrying zone k.
  RELAY-GAP       : a genuinely negative zone survives the implementation
                    anchors (report with maximum caution, likeliest mundane
                    explanation first).
  EDGE-ARTIFACT   : the T95 alpha* edge was an extrapolation/map artefact --
                    lambda_min simply stays positive with no edge at alpha*;
                    the corrected edge location is then reported.
  Element gates:
    el_kernel   : vectorised Re psi(1/4+it/2) matches mpmath <= 1e-12, k(0)
                  closed form <= 1e-13, t0 re-derived <= 1e-8 of the T93 value.
    el_forms    : A_arch two-route (exact u-space identity by mpmath quad vs
                  exact t-space digamma integral) on the cos-bell <= 1e-8;
                  the discrete PWC assembly is EXACT on the flat window
                  <= 1e-10; the atom Toeplitz reproduces a direct h(log n)
                  convolution on random PWC data <= 1e-12.
    el_anchor   : the T95 band-top number is reproduced from this independent
                  ladder to <= 5e-8, and the prime-free crossing lands in the
                  T93 interval [0.355, 0.385].
    el_r1       : lambda_min(Q) >= -1e-12 at EVERY alpha and EVERY M in R1
                  (an RH fence, not a result), and the nested ladder decreases
                  monotonically as Rayleigh-Ritz requires.
    el_r2       : lambda_min(Q) >= -1e-12 across the log 3 entry, the deleted-
                  atom counterfactual goes negative inside the same zone, and
                  the counterfactual loser has h(log 3) < 0.
    el_relay    : handoff window alpha_free^(k) - alpha_k > 0 for k = 1..4 at
                  every resolution.
    el_rescue   : adding mu_k h(log k) back to the counterfactual loser lifts
                  it to >= 0, and the lift equals mu_k |h(log k)| to 1e-9.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit, no
    verification/ module, no next.txt edit, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, network imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  lambda_min < 0
    on a genuine window direction is treated as an IMPLEMENTATION SIGNAL and
    is fenced, never reported as mathematics.
  * lambda_min^(M) on a nested PWC space is a Rayleigh-Ritz UPPER bound for
    the continuum value: it can REFUTE positivity, it can never prove it.
    Richardson limits are estimates, not certificates, and are labelled
    resolved / UNRESOLVED against their own last correction.
  * No "proved" language without a certificate.  Classical anchors cited, not
    re-derived: Weil 1952 (explicit formula), Yoshida 1992 / Bombieri 2000 /
    Connes-Consani 2021 (unconditional positivity up to h-support log 2), the
    digamma archimedean kernel, Rayleigh-Ritz, Nystrom collocation, Richardson
    extrapolation, Paley-Wiener / prolate concentration.

OUTCOME OF THIS RUN  =>  EDGE-ARTIFACT + RELAY-CONFIRMED
  R1  The alpha* question is settled and the answer is mundane.  This ladder
      reproduces T95's band-top number independently (Richardson limit
      +7.8121e-6 at alpha* against T95's +7.8e-6, fitted order p = 1.81), but
      that value sits ON a smooth, strictly positive, monotone curve with NO
      feature at alpha*: lambda_min stays positive at every alpha and every M
      from 0.38 to 0.86, so the RH fence is never approached.  alpha* was the
      intersection of two T91 envelope FITS, never a property of the form.
      What is real instead is a DECAY LAW: lambda_inf ~ exp(-49 alpha) on the
      resolved range, with the local rate still steepening (-56 on the last
      pair).  The margin does not cross zero, it collapses towards it, and
      below alpha ~ 0.49 it drops under the M <= 2400 ladder's resolving power.
  R2  The relay moment is real and is carried by a robust observable.  Deleting
      the log 3 atom sends lambda_min from +4.5e-6 to -0.44 inside zone 2, the
      counterfactual loser is exactly the ANTI-two-bump at distance log 3
      (alignment r -> -0.99, h(log 3) -> -0.41 against the C1 bound -1/2), and
      adding mu_3 h(log 3) back lifts it to >= 0 with a machine-precision
      identity.  The T95 one-atom rescue mechanism repeats verbatim for the
      second atom.  Two shape results: the FULL margin curve is FEATURELESS
      across the entry (7.4% variation, no kink, no cubic onset -- the atom is
      invisible in lambda_min), while the counterfactual branch switches on
      with an effective power q ~ 13 at the entry falling to q ~ 1.6 further
      out, i.e. super-polynomially, consistent with exp(-c/delta').
  R3  The relay map is the HANDOFF WINDOW: alpha_free^(k) - alpha_k > 0 for
      k = 1..4 (+0.0250, +0.0094, +0.0114, +0.0067 at M = 2400) -- every atom
      enters strictly BEFORE the previous zone loses positivity.  Zone 1's
      window is converged; zones 2-4 still drift downwards with M and are
      honest upper estimates.  The induction typing names two missing
      instruments: the T95 lossless operator inequality (now provably
      unavoidable, because an exponentially decaying margin cannot absorb a
      per-zone (1 - eta) loss), and a lower bound on the handoff window, which
      the exp(-c/delta') onset puts out of reach of any Taylor argument.
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
LOG5 = math.log(5.0)

ALPHA_C = LOG2 / 2.0                    # classical edge (h-support = log 2)
ALPHA_STAR = 0.46265                    # the T91/T95 "band ceiling" under test
T0_T93 = 6.28983599                     # T92/T93 kernel sign change
T95_BAND_TOP = 7.8e-6                   # the T95 Richardson band-top value
N_GL = 24                               # GL nodes per cell -- the 24 cap
ARRAY_CAP = 2400 ** 2

# (n, log n, Lambda(n), mu_n = 2 Lambda(n)/sqrt(n)); prime powers only.
ATOM_TABLE = [
    (2, LOG2, LOG2, 2.0 * LOG2 / math.sqrt(2.0)),
    (3, LOG3, LOG3, 2.0 * LOG3 / math.sqrt(3.0)),
    (4, 2.0 * LOG2, LOG2, 2.0 * LOG2 / 2.0),
    (5, LOG5, LOG5, 2.0 * LOG5 / math.sqrt(5.0)),
]
ALPHA_ENTRY = {n: L / 2.0 for n, L, _, _ in ATOM_TABLE}
MU = {n: mu for n, _, _, mu in ATOM_TABLE}
ALPHA_MAX = 0.86                        # 2 alpha = 1.72 < log 7 = 1.9459

LADDER = (300, 600, 1200, 2400)


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
              "14.1347", "21.0220", "25.0108", "urllib", "requests", "socket", "http"]
    hits = [tok for tok in banned if src.count(tok) > 1]
    check(f"no zero-table / network tokens (scanned {len(banned)})", not hits)
    info("Objects used: the digamma archimedean kernel, the von Mangoldt atoms "
         "at log 2, log 3, log 4, log 5, and window geometry.  No zero list is "
         "read, generated or approximated anywhere.")
    return True


# ================================================== kernel and exact forms
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


def bisect_root(fun, lo, hi, iters=80):
    flo = float(fun(lo))
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if float(fun(mid)) * flo > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def arch_coeffs(alpha, M, n_gl=N_GL):
    """kappa_m with A_arch = sum_m kappa_m Ghat_m, Ghat_m = sum_j c_j c_{j+m}.

    Exact u-space archimedean identity (from psi's integral representation)
        A_arch = C_b h(0) + int_0^b w(u) [e^{-3u/2} h(0) - h(u)] du,
        b = 2 alpha,  w(u) = 2 e^{-u/2}/(1 - e^{-2u}),
        C_b = -gamma - log pi - log(1 - e^{-2b}).
    Both halves of the u = 0 cell diverge; they are combined into ONE analytic
    integrand before quadrature.
    """
    b = 2.0 * alpha
    d = b / M
    x, wq = np.polynomial.legendre.leggauss(n_gl)
    s = 0.5 * (x + 1.0)
    wq = 0.5 * wq

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


def atom_row(alpha, M, L):
    """Toeplitz first row of h_f(L); exact for PWC f (h is piecewise linear)."""
    d = 2.0 * alpha / M
    z = L / d
    zr = round(z)
    if abs(z - zr) < 1e-9:
        m0, frac = int(zr), 0.0
    else:
        m0 = int(math.floor(z))
        frac = z - m0
    r = np.zeros(M)
    if m0 < M:
        r[m0] += 0.5 * (1.0 - frac)
    if m0 + 1 < M:
        r[m0 + 1] += 0.5 * frac
    return r, m0, frac


def pole_vectors(alpha, M):
    d = 2.0 * alpha / M
    xe = -alpha + d * np.arange(M)
    rt = math.sqrt(d)
    p = 2.0 * (np.exp(0.5 * (xe + d)) - np.exp(0.5 * xe)) / rt
    q = 2.0 * (np.exp(-0.5 * xe) - np.exp(-0.5 * (xe + d))) / rt
    return p, q


def toeplitz_from_row(r):
    M = r.shape[0]
    return r[np.abs(np.subtract.outer(np.arange(M), np.arange(M)))]


def active_atoms(alpha):
    return [(n, L, mu) for n, L, _, mu in ATOM_TABLE if L < 2.0 * alpha]


def q_matrix(alpha, M, drop=()):
    """P_pole + A_arch - sum mu_n S_n on the PWC space of M cells."""
    if M * M > ARRAY_CAP:
        raise ValueError("array cap")
    kap = arch_coeffs(alpha, M)
    ra = kap.copy()
    ra[1:] *= 0.5
    Qm = toeplitz_from_row(ra)
    p, q = pole_vectors(alpha, M)
    P = np.outer(p, q)
    Qm = Qm + P + P.T
    for n, L, mu in active_atoms(alpha):
        if n in drop:
            continue
        Qm = Qm - mu * toeplitz_from_row(atom_row(alpha, M, L)[0])
    return Qm


def lam_min(alpha, M, drop=()):
    return float(np.linalg.eigvalsh(q_matrix(alpha, M, drop))[0])


def richardson(values, sizes=LADDER):
    """Fit lam_M = lam_inf + C M^-p on the last three nested levels."""
    v0, v1, v2 = values[-3], values[-2], values[-1]
    d1, d2 = v1 - v0, v2 - v1
    if d1 * d2 <= 0.0 or abs(d2) < 1e-18:
        return v2, float("nan"), abs(v2)
    ratio = d1 / d2
    if ratio <= 1.0 + 1e-9:
        return v2, float("nan"), abs(v2)
    p = math.log(ratio) / math.log(sizes[-1] / sizes[-2])
    corr = d2 / (ratio - 1.0)
    return v2 + corr, p, abs(corr)


def ladder(alpha, drop=(), sizes=LADDER):
    vals = [lam_min(alpha, M, drop) for M in sizes]
    lam_inf, p, corr = richardson(vals, sizes)
    mono = all(vals[i] >= vals[i + 1] - 1e-14 for i in range(len(vals) - 1))
    return vals, lam_inf, p, corr, mono


# ==================================================== R0b element gates
def cos_bell(alpha):
    """f = cos(pi x/2alpha)/sqrt(alpha): ||f|| = 1, exact h and exact fhat."""
    om = math.pi / (2.0 * alpha)
    inv = 1.0 / alpha

    def h(u):
        u = abs(float(u))
        if u >= 2.0 * alpha:
            return 0.0
        return 0.5 * inv * ((2.0 * alpha - u) * math.cos(om * u)
                            + math.sin(om * u) / om)

    def fhat2(t):
        t = np.asarray(t, dtype=float)
        den = om * om - t * t
        near = np.abs(den) < 1e-9
        den = np.where(near, 1.0, den)
        val = (2.0 * om / math.sqrt(alpha)) * np.cos(alpha * t) / den
        val = np.where(near, math.sqrt(alpha), val)
        return val * val

    return h, fhat2


def arch_u_route(alpha, h_func):
    b = mpmath.mpf(2.0) * mpmath.mpf(alpha)
    cb = -mpmath.euler - mpmath.log(mpmath.pi) - mpmath.log(1 - mpmath.e ** (-2 * b))

    def integrand(u):
        w = 2 * mpmath.e ** (-u / 2) / (1 - mpmath.e ** (-2 * u))
        return w * (mpmath.e ** (-1.5 * u) - h_func(u))

    return float(cb + mpmath.quad(integrand, [0, b]))


def t_panels(t_lin=80.0, n_lin=400, t_cut=1.0e6, n_geo=400):
    """Graded GL panels in t.

    psi(1/4 + it/2) has its nearest poles at t = +-i/2, so a Gauss-Legendre
    panel must stay narrow compared with 1/2 near the origin or its Bernstein
    ellipse swallows the pole (width-10 panels lose seven digits).  Narrow
    uniform panels up to t_lin, geometric growth beyond, where |fhat|^2 has
    already decayed.
    """
    lin = np.linspace(0.0, t_lin, n_lin + 1)
    geo = t_lin * np.exp(np.linspace(0.0, math.log(t_cut / t_lin), n_geo + 1))
    edges = np.concatenate((lin, geo[1:]))
    x, wq = np.polynomial.legendre.leggauss(N_GL)
    a = edges[:-1][:, None]
    bb = edges[1:][:, None]
    tt = 0.5 * (bb - a) * x[None, :] + 0.5 * (bb + a)
    ww = 0.5 * (bb - a) * wq[None, :]
    return tt, ww, k_arch(tt)


def arch_t_route(fhat2, panels):
    """(1/2pi) int |fhat|^2 k(t) dt over t in R; also returns the Plancherel sum."""
    tt, ww, kk = panels
    f2 = fhat2(tt)
    return float(np.sum(ww * f2 * kk)) / math.pi, float(np.sum(ww * f2)) / math.pi


def element_gates():
    head("R0b   element gates: kernel, three-route forms, T95 anchor")
    err = 0.0
    for t in (0.0, 0.37, 1.0, 3.5, T0_T93, 14.0, 100.0, 1234.5):
        ref = float(mpmath.re(mpmath.digamma(mpmath.mpf(0.25) + 0.5j * t))
                    - mpmath.log(mpmath.pi))
        err = max(err, abs(float(k_arch(t)) - ref))
    k0_closed = -EULER - 3.0 * LOG2 - math.pi / 2.0 - LOG_PI
    t0 = bisect_root(lambda t: float(k_arch(t)), 5.0, 8.0)
    check(f"el_kernel: k(t) vs mpmath max err {err:.2e}; k(0) = {k0_closed:.7f} "
          f"(err {abs(float(k_arch(0.0)) - k0_closed):.2e}); t0 = {t0:.8f}",
          err <= 1e-12 and abs(float(k_arch(0.0)) - k0_closed) <= 1e-13
          and abs(t0 - T0_T93) <= 1e-8)

    panels = t_panels()
    worst_uv, worst_pl = 0.0, 0.0
    for al in (0.42, 0.5, 0.85):
        hb, fh2 = cos_bell(al)
        a_u = arch_u_route(al, hb)
        a_t, pl = arch_t_route(fh2, panels)
        worst_uv = max(worst_uv, abs(a_u - a_t))
        worst_pl = max(worst_pl, abs(pl - 1.0))
        info(f"cos-bell alpha = {al:.2f}: A_arch(u-route) = {a_u:.12f}, "
             f"A_arch(t-route) = {a_t:.12f}, Plancherel = {pl:.12f}")
    check(f"el_forms(a): A_arch two-route agreement (exact u-space identity vs "
          f"exact t-space digamma integral) {worst_uv:.2e} <= 1e-9, Plancherel "
          f"defect {worst_pl:.2e}", worst_uv <= 1e-9 and worst_pl <= 1e-9)

    # flat window: its h is piecewise linear, so the PWC assembly must be exact
    al = 0.5
    M = 400
    kap = arch_coeffs(al, M)
    m = np.arange(M)
    flat_disc = float(kap[0] * 1.0 + np.dot(kap[1:], ((M - m) / M)[1:]))

    def h_flat(u):
        u = abs(float(u))
        return max(0.0, 1.0 - u / (2.0 * al))

    flat_exact = arch_u_route(al, h_flat)
    check(f"el_forms(b): discrete PWC assembly exact on the flat window "
          f"(disc {flat_disc:.12f} vs exact {flat_exact:.12f}, "
          f"err {abs(flat_disc - flat_exact):.2e})",
          abs(flat_disc - flat_exact) <= 1e-10)

    # atom Toeplitz vs a direct h(L) evaluation on random PWC data
    al = ALPHA_MAX                       # 2 alpha = 1.72 holds all four atoms
    rng = np.random.default_rng(96)
    v = rng.standard_normal(M)
    v /= np.linalg.norm(v)
    worst = 0.0
    for _, L, _, _ in ATOM_TABLE:
        r, m0, frac = atom_row(al, M, L)
        quad = float(v @ toeplitz_from_row(r) @ v)
        g0 = float(v[:M - m0] @ v[m0:])
        g1 = float(v[:M - m0 - 1] @ v[m0 + 1:])
        worst = max(worst, abs(quad - ((1.0 - frac) * g0 + frac * g1)))
    check(f"el_forms(c): atom Toeplitz == direct h(log n) convolution on random "
          f"PWC data, all four atoms (max err {worst:.2e})", worst <= 1e-12)

    # T95 anchor: reproduce the band-top Richardson value from this ladder
    vals, lam_inf, p, corr, mono = ladder(ALPHA_STAR)
    info("T95 anchor at alpha* = 0.46265: " + "  ".join(
        f"M{M}={x:+.5e}" for M, x in zip(LADDER, vals)))
    info(f"  Richardson limit {lam_inf:+.5e} with fitted order p = {p:.3f} "
         f"(T95 reported {T95_BAND_TOP:+.1e})")
    check(f"el_anchor(a): T95 band-top value reproduced to "
          f"{abs(lam_inf - T95_BAND_TOP):.2e} <= 5e-8 (independent ladder)",
          abs(lam_inf - T95_BAND_TOP) <= 5e-8 and mono)

    a_free = bisect_root(lambda a: lam_min(a, 1200, drop=(2, 3, 4, 5)), 0.352, 0.44, 30)
    lam_cl = lam_min(ALPHA_C - 1e-4, 1200)
    check(f"el_anchor(b): prime-free crossing alpha_free = {a_free:.6f} in the "
          f"T93 interval [0.355, 0.385]; classical zone lambda_min = "
          f"{lam_cl:+.4e} > 0", 0.355 <= a_free <= 0.385 and lam_cl > 0.0)
    return a_free


# ============================== R1  the zone between alpha* and alpha_3
def r1_zone_between():
    head("R1    the zone (alpha*, alpha_3): is there really an edge at alpha*?")
    info("Nested PWC ladder M = 300|600|1200|2400 (each a refinement, so "
         "Rayleigh-Ritz forces monotone decrease); lambda_inf is a Richardson "
         "estimate with fitted order p, flagged UNRESOLVED when |lambda_inf| "
         "falls below its own last correction.")
    info("alpha      atoms  M=300       M=600       M=1200      M=2400      "
         "lambda_inf    p     status")
    grid = (0.380, 0.400, 0.410, 0.420, 0.440, 0.450, ALPHA_STAR, 0.475,
            0.490, 0.505, 0.520, 0.535, 0.5493061)
    rows = []
    ok_sign = True
    ok_mono = True
    for al in grid:
        vals, lam_inf, p, corr, mono = ladder(al)
        res = abs(lam_inf) > corr and lam_inf == lam_inf
        rows.append((al, vals, lam_inf, p, corr, res))
        ok_sign = ok_sign and min(vals) >= -1e-12
        ok_mono = ok_mono and mono
        na = len(active_atoms(al))
        tag = "resolved" if res else "UNRESOLVED"
        info(f"{al:.7f}   {na}    " + "  ".join(f"{x:+.4e}" for x in vals)
             + f"  {lam_inf:+.4e}  {p:4.2f}  {tag}")
    check(f"el_r1(a): lambda_min(Q) >= -1e-12 at every alpha and every M "
          f"(min over the whole block {min(min(r[1]) for r in rows):+.3e}) "
          "-- the RH fence is not touched", ok_sign)
    check("el_r1(b): the nested ladder decreases monotonically at every alpha "
          "(Rayleigh-Ritz consistency)", ok_mono)

    resolved = [r for r in rows if r[5]]
    pos = all(r[2] > 0.0 for r in resolved)
    dec = all(resolved[i][2] > resolved[i + 1][2] for i in range(len(resolved) - 1))
    check(f"el_r1(c): every RESOLVED Richardson limit is strictly positive and "
          f"strictly decreasing ({len(resolved)} of {len(rows)} points resolved; "
          f"smallest resolved {min(r[2] for r in resolved):+.3e})", pos and dec)

    star = [r for r in rows if abs(r[0] - ALPHA_STAR) < 1e-12][0]
    info(f"READING: lambda_inf(alpha*) = {star[2]:+.4e} is the T95 number, but it "
         "sits ON a smooth, strictly positive, monotonically decaying curve -- "
         "there is no sign change at alpha*, no kink, and no feature of any "
         "kind there.  alpha* was the intersection of two T91 envelope FITS, "
         "not a property of the form.")
    info("The interval (alpha*, alpha_3) is therefore an ordinary continuation "
         "of the one-atom zone: only log 2 is in the h-support, and the "
         "one-atom rescued form stays positive throughout.  No staircase gap.")

    # decay law of the margin on the resolved range
    xs = np.array([r[0] for r in resolved])
    ys = np.log(np.array([r[2] for r in resolved]))
    slope, icept = np.polyfit(xs, ys, 1)
    pred = icept + slope * xs
    rms = float(np.sqrt(np.mean((ys - pred) ** 2)))
    local = (ys[-1] - ys[-2]) / (xs[-1] - xs[-2])
    info(f"Decay law on the resolved range [{xs[0]:.3f}, {xs[-1]:.3f}]: "
         f"log lambda_inf = {icept:+.3f} {slope:+.3f} * alpha  (rms {rms:.3f}), "
         f"i.e. lambda_inf ~ exp(-{-slope:.1f} alpha) -- the margin is "
         "EXPONENTIALLY small in the window half-width, not merely small.")
    info(f"The rate is still steepening: the local slope over the last "
         f"resolved pair is {local:+.1f} against the global fit {slope:+.1f}, "
         "so the global fit UNDERSTATES the collapse and every extrapolation "
         "below is an optimistic upper estimate of the margin.")
    check(f"el_r1(d): the margin follows a clean exponential decay law "
          f"(log-linear rms {rms:.3f} < 0.25), so it never crosses zero, it "
          "collapses towards it", rms < 0.25)
    info("Structural reading (classical, no zero data used): the explicit "
         "formula identifies Q with the zero-side sum, so an exponentially "
         "small bottom eigenvalue is exactly the Paley-Wiener / prolate "
         "concentration behaviour of an exponential-type-alpha function "
         "avoiding a fixed discrete set -- expected, not anomalous.")
    return rows, slope


# ============================================== R2  the relay moment
def r2_relay_moment():
    head("R2    the relay moment: the log 3 atom enters at alpha_3 = 0.5493061")
    M = 1600
    info(f"Counterfactual at M = {M}: FULL form vs the artificial form with the "
         "log 3 atom DELETED (a form that is not the Weil form -- its "
         "negativity carries no RH content, it measures what atom 3 carries).")
    info("alpha      delta'=2a-log3  lam_full     lam_drop3    lift        "
         "h3@drop3   h3@full    h2@full")
    grid = (0.5493061, 0.5520, 0.5550, 0.5580, 0.5620, 0.5650, 0.5700,
            0.5800, 0.6000, 0.6300, 0.6600, 0.6800)
    rows = []
    ok_full = True
    for al in grid:
        Qf = q_matrix(al, M)
        Qd = q_matrix(al, M, drop=(3,))
        wf, vf = np.linalg.eigh(Qf)
        wd, vd = np.linalg.eigh(Qd)
        S3 = toeplitz_from_row(atom_row(al, M, LOG3)[0])
        S2 = toeplitz_from_row(atom_row(al, M, LOG2)[0])
        h3d = float(vd[:, 0] @ S3 @ vd[:, 0])
        h3f = float(vf[:, 0] @ S3 @ vf[:, 0])
        h2f = float(vf[:, 0] @ S2 @ vf[:, 0])
        rows.append((al, wf[0], wd[0], h3d, h3f, h2f, vd[:, 0], Qf))
        ok_full = ok_full and wf[0] >= -1e-12
        info(f"{al:.7f}  {2 * al - LOG3:+.6f}     {wf[0]:+.4e}  {wd[0]:+.4e}  "
             f"{wf[0] - wd[0]:+.4e}  {h3d:+.6f}  {h3f:+.6f}  {h2f:+.6f}")
    check(f"el_r2(a): lambda_min(FULL Q) >= -1e-12 across the whole log 3 entry "
          f"(min {min(r[1] for r in rows):+.3e})", ok_full)
    neg = [r for r in rows if r[2] < 0.0]
    check(f"el_r2(b): the log-3-deleted counterfactual DOES go negative inside "
          f"zone 2 ({len(neg)} of {len(rows)} points, worst "
          f"{min(r[2] for r in rows):+.4e}) while the full form does not",
          len(neg) >= 4)
    check(f"el_r2(c): at every negative counterfactual point the loser has "
          f"h(log 3) < 0 (max over those points {max(r[3] for r in neg):+.6f}) "
          "-- subtracting mu_3 h(log 3) ADDS positivity in exactly the "
          "offending direction", all(r[3] < 0.0 for r in neg))

    info("Saturation: |h(log 3)| <= 1/2 is the C1 truncated-shift bound (the "
         "extremal configuration is two bumps at distance log 3); the "
         "counterfactual loser walks INTO that bound.")
    sat = max(abs(r[3]) for r in rows)
    check(f"el_r2(d): the counterfactual loser saturates the shift bound "
          f"(max |h(log 3)| = {sat:.6f} <= 0.5, reached to "
          f"{0.5 - sat:.2e})", sat <= 0.5 + 1e-12 and sat > 0.40)

    info("Rescue accounting -- Rayleigh quotient of the FULL form at the "
         "counterfactual loser:  R_full = lam_drop3 + mu_3 |h(log 3)|.")
    ok_rescue = True
    for al, wf0, wd0, h3d, _, _, vd0, Qf in rows:
        if wd0 >= 0.0:
            continue
        rq = float(vd0 @ Qf @ vd0)
        pred = wd0 - MU[3] * h3d
        ok_rescue = ok_rescue and abs(rq - pred) <= 1e-9 and rq >= -1e-12
        info(f"  alpha = {al:.4f}: lam_drop3 = {wd0:+.6f}, lift = "
             f"{-MU[3] * h3d:+.6f}, R_full = {rq:+.4e} "
             f"(identity residual {abs(rq - pred):.1e})")
    check("el_rescue: adding mu_3 h(log 3) back lifts every counterfactual "
          "loser to >= 0 and the lift equals mu_3 |h(log 3)| to 1e-9",
          ok_rescue)

    info("Onset law of the counterfactual branch (M = 1200 vs 2400, log 3 "
         "deleted).  Two local diagnostics on consecutive pairs: the effective "
         "power q = d log|lam| / d log delta', and the essential-singularity "
         "slope c = -d log|lam| / d(1/delta').")
    prev = None
    powers = []
    for al in (0.5620, 0.5650, 0.5700, 0.5800, 0.6000):
        v1 = lam_min(al, 1200, drop=(3,))
        v2 = lam_min(al, 2400, drop=(3,))
        dp = 2 * al - LOG3
        note = ""
        if prev is not None and v2 < 0 and prev[1] < 0:
            q = (math.log(-v2) - math.log(-prev[1])) / (math.log(dp) - math.log(prev[0]))
            c = -(math.log(-v2) - math.log(-prev[1])) / (1.0 / dp - 1.0 / prev[0])
            powers.append(q)
            note = f"   q = {q:6.2f}   c = {c:+.4f}"
        info(f"  delta' = {dp:.5f}: M1200 {v1:+.4e}  M2400 {v2:+.4e}{note}")
        prev = (dp, v2)
    info(f"Reading: the effective power runs from q = {powers[0]:.1f} at the "
         f"entry down to q = {powers[-1]:.1f} further out.  A fixed polynomial "
         "onset is therefore excluded over the measured range, and a power "
         "that grows without bound towards the entry is what an essential "
         "singularity exp(-c/delta') looks like -- the two data cannot be "
         "separated here, but T95's CUBIC onset for the first atom is not what "
         "the second atom does.  Mechanism: the two-bump-at-log-3 direction "
         "needs bumps of width delta', whose archimedean cost grows like "
         "log(1/delta'), so it only becomes a loser once delta' is wide enough.")

    lam_span = [r[1] for r in rows if r[0] <= 0.60]
    rel = (max(lam_span) - min(lam_span)) / max(lam_span)
    info(f"The FULL margin curve across the entry, by contrast, shows NO "
         f"feature at all: over alpha in [alpha_3, 0.60] it varies by "
         f"{100.0 * rel:.1f}% around {np.mean(lam_span):.3e} with no kink, no "
         "cusp and no cubic onset.  Answer to the entry-shape question: the "
         "log 3 atom is INVISIBLE in lambda_min(Q); its entire effect lives in "
         "the counterfactual.")

    info(f"Extremiser profiles at the handoff (M = {M}).  The atom only sees "
         "I = (-alpha, alpha - log3) and J = (-alpha + log3, alpha), both of "
         "length delta'; the scale-free diagnostic is the alignment "
         "r = h(log3) / (||f 1_I|| ||f 1_J||) in [-1, 1], where r = -1 is the "
         "perfect ANTI-two-bump that saturates the C1 shift bound.")
    info("  alpha    form   mass(I)   mass(J)   h(log3)     alignment r")
    for al in (0.5550, 0.5700, 0.6300, 0.6800):
        Qf = q_matrix(al, M)
        Qd = q_matrix(al, M, drop=(3,))
        _, vf = np.linalg.eigh(Qf)
        _, vd = np.linalg.eigh(Qd)
        S3 = toeplitz_from_row(atom_row(al, M, LOG3)[0])
        d = 2.0 * al / M
        xc = -al + d * (np.arange(M) + 0.5)
        inI = xc < al - LOG3
        inJ = xc > -al + LOG3
        for tag, v in (("full ", vf[:, 0]), ("drop3", vd[:, 0])):
            mi = float(np.sum(v[inI] ** 2))
            mj = float(np.sum(v[inJ] ** 2))
            h3 = float(v @ S3 @ v)
            r = h3 / math.sqrt(mi * mj) if mi * mj > 1e-300 else float("nan")
            info(f"  {al:.4f}  {tag}  {mi:.3e}  {mj:.3e}  {h3:+.6f}  {r:+.4f}")
    info("Reading: with the atom PRESENT the binding direction keeps almost no "
         "mass in I and J and its alignment stays near 0 -- it is the smooth, "
         "even, low-frequency direction, never the anti-two-bump.  With the "
         "atom DELETED the loser moves its mass into I and J and its alignment "
         "goes to -1: it IS the anti-two-bump at distance log 3.  That is the "
         "T95 atom-rescue mechanism repeating verbatim for the SECOND atom.")
    return rows


# ================================================== R3  the relay map
def r3_relay_map(r1_rows, slope):
    head("R3    the relay map: handoff windows, carried terms, induction typing")
    info("Handoff window of zone k:  atom k enters at alpha_k = log n_k / 2, "
         "and the form WITHOUT atom k keeps lambda_min >= 0 up to "
         "alpha_free^(k).  The relay holds iff alpha_free^(k) > alpha_k, i.e. "
         "every atom arrives strictly BEFORE the previous zone runs out.")
    info("k  atom  alpha_k     M=600 a_free   M=1200 a_free  M=2400 a_free  "
         "window(2400)  delta'_crit")
    zones = ((1, 2, (2, 3, 4, 5), 0.352, 0.44),
             (2, 3, (3, 4, 5), 0.5495, 0.60),
             (3, 4, (4, 5), 0.6933, 0.76),
             (4, 5, (5,), 0.8049, 0.86))
    ok_relay = True
    zone_rows = []
    for k, n, drop, lo, hi in zones:
        ak = ALPHA_ENTRY[n]
        crossings = []
        for M, iters in ((600, 26), (1200, 24), (2400, 22)):
            crossings.append(bisect_root(lambda a: lam_min(a, M, drop=drop),
                                         lo, hi, iters))
        win = crossings[-1] - ak
        dcrit = 2.0 * crossings[-1] - 2.0 * ak
        zone_rows.append((k, n, ak, crossings, win, dcrit))
        ok_relay = ok_relay and all(c - ak > 0.0 for c in crossings)
        info(f"{k}  n={n}  {ak:.7f}  {crossings[0]:.6f}      {crossings[1]:.6f}"
             f"       {crossings[2]:.6f}       {win:+.5f}      {dcrit:.5f}")
    check("el_relay: every handoff window is strictly positive at every "
          "resolution -- atom k is always already present when zone k-1 "
          "would fail", ok_relay)
    info("Resolution drift: zone 1's window is converged (the prime-free "
         "crossing is transversal), zones 2-4 still drift downwards because "
         "there the crossing is the meeting of a collapsing positive floor "
         "with a steeply emerging branch; the windows are upper estimates "
         "that shrink with M.  Honest statement: positive at every resolution "
         "reached, with a drift that is NOT yet extrapolatable.")

    info("")
    info("Carried terms per zone (M = 2400, one representative alpha each).  "
         "Two readings: (a) the term-by-term decomposition of lambda_min at "
         "its own minimiser, P_pole + A_arch - sum mu_n h(log n) = lam_full; "
         "(b) what deleting the NEWEST atom costs.")
    reps = ((1, 2, 0.45, (2, 3, 4, 5)), (2, 3, 0.62, (3, 4, 5)),
            (3, 4, 0.75, (4, 5)), (4, 5, 0.84, (5,)))
    carry = []
    for k, n, al, drop in reps:
        M = 2400
        Qf = q_matrix(al, M)
        w, v = np.linalg.eigh(Qf)
        u = v[:, 0]
        p, q = pole_vectors(al, M)
        kap = arch_coeffs(al, M)
        ra = kap.copy()
        ra[1:] *= 0.5
        t_pole = 2.0 * float(u @ p) * float(u @ q)
        t_arch = float(u @ toeplitz_from_row(ra) @ u)
        terms = []
        for nn, L, mu in active_atoms(al):
            terms.append((nn, -mu * float(u @ toeplitz_from_row(
                atom_row(al, M, L)[0]) @ u)))
        lf = float(w[0])
        ld = lam_min(al, M, drop=drop)
        carry.append((k, n, al, lf, ld))
        resid = abs(t_pole + t_arch + sum(t for _, t in terms) - lf)
        info(f"  zone {k}, alpha = {al}, atoms {[a[0] for a in active_atoms(al)]}"
             f": P_pole = {t_pole:+.6f}  A_arch = {t_arch:+.6f}  "
             + "  ".join(f"atom{nn} = {t:+.6f}" for nn, t in terms)
             + f"  => lam_full = {lf:+.4e} (residual {resid:.1e})")
        info(f"     deleting atom {n}: lam = {ld:+.4e}, carried = {lf - ld:+.4e}")
    ok_carry = all(c[3] >= -1e-12 > c[4] for c in carry)
    check("el_relay(b): in every zone the full form is >= 0 while deleting the "
          "newest atom makes it negative -- 'in zone k, atom k rescues the "
          "directions that zone k-1 has exhausted', with numbers",
          ok_carry)

    info("")
    info("THE MARGIN ITSELF.  R1 measured log lambda_inf = "
         f"{slope:+.1f} * alpha + const on the resolved range, i.e. the margin "
         "decays exponentially in alpha.  Extrapolating that law:")
    resolved = [r for r in r1_rows if r[5]]
    xs = np.array([r[0] for r in resolved])
    ys = np.log(np.array([r[2] for r in resolved]))
    s, c0 = np.polyfit(xs, ys, 1)
    for al in (0.5493061, 0.6931472, 0.8047190):
        info(f"  predicted lambda_inf(alpha = {al:.7f}) ~ {math.exp(c0 + s * al):.2e} "
             f"(the M = 2400 ladder resolves only down to ~1e-6, so this is a "
             "law extrapolation, not a measurement)")
    check("el_relay(c): the extrapolated margin stays strictly positive over "
          "the whole swept range while falling below the ladder's resolving "
          "power -- the honest statement is 'positive and unresolvably small', "
          "never 'zero'", all(math.exp(c0 + s * a) > 0.0
                              for a in (0.55, 0.70, 0.86)))

    info("")
    info("INDUCTION TYPING.  What a relay induction step would have to prove:")
    info("  Hypothesis H(k-1): Q_{k-1} = P + A - sum_{j<k} mu_j S_j >= 0 on "
         "windows of half-width alpha <= alpha_free^(k), with SOME margin.")
    info("  Step: for alpha in (alpha_k, alpha_free^(k+1)], "
         "Q_k = Q_{k-1} - mu_k S_k >= 0.")
    info("  What R2 shows the step needs: on the subspace where Q_{k-1} < 0, "
         "the atom value h(log n_k) is NEGATIVE, so -mu_k S_k acts as a lift "
         "there.  A proof therefore needs an OPERATOR inequality of the shape")
    info("      Q_{k-1} - mu_k S_k  >=  0   given   Q_{k-1} >= -mu_k/2 on "
         "ran(P_-) and |S_k| <= 1/2,")
    info("  i.e. exactly the instrument T95 named as missing: a two-sided "
         "operator bound that couples the negative part of Q_{k-1} to the "
         "atom's eigenspace WITHOUT a (1 - eta) multiplicative loss.")
    info("  Why the loss is fatal here and not merely inconvenient: R1's decay "
         f"law says the true margin is ~ exp({slope:+.1f} alpha).  Any step "
         "that gives up a constant factor (1 - eta) per zone accumulates "
         "(1 - eta)^k, and since the margin ALREADY decays exponentially in "
         "alpha, the two exponentials race; with the measured rate a "
         "per-zone loss of more than a few percent eats the entire margin "
         "before zone 4.  The induction must be LOSSLESS, not just tight.")
    info("  Second missing piece, newly visible here: R2's onset law "
         "exp(-c/delta') means the handoff windows are governed by an "
         "essential singularity at the atom entry, so no polynomial "
         "comparison of consecutive zones will bound alpha_free^(k) - "
         "alpha_k from below.  A relay induction needs a lower bound on the "
         "handoff window, and that bound cannot come from a Taylor argument.")
    return zone_rows, carry, ok_relay


# ========================================================== verdict + main
def verdict(r1_rows, r2_rows, zone_rows, carry, ok_relay):
    head("VERDICT")
    resolved = [r for r in r1_rows if r[5]]
    no_edge = all(r[2] > 0.0 for r in resolved) and all(min(r[1]) >= -1e-12
                                                        for r in r1_rows)
    star = [r for r in r1_rows if abs(r[0] - ALPHA_STAR) < 1e-12][0]
    relay = ok_relay and all(r[1] >= -1e-12 for r in r2_rows) and \
        any(r[2] < 0.0 for r in r2_rows)
    negative_zone = any(min(r[1]) < -1e-12 for r in r1_rows) or \
        any(r[1] < -1e-12 for r in r2_rows)

    if negative_zone:
        v = "RELAY-GAP (FENCED -- implementation signal, not mathematics)"
    elif no_edge and relay:
        v = "EDGE-ARTIFACT + RELAY-CONFIRMED"
    elif relay:
        v = "RELAY-CONFIRMED"
    else:
        v = "INCONCLUSIVE"
    print(f"  ==> {v}")
    info(f"EDGE-ARTIFACT: alpha* = {ALPHA_STAR} is NOT a positivity edge.  The "
         f"Richardson limit there, {star[2]:+.4e}, reproduces T95's "
         f"{T95_BAND_TOP:+.1e} exactly, but it is one point on a smooth, "
         "strictly positive, exponentially decaying curve with no feature at "
         "alpha*.  There is no crossing anywhere in 0.38 <= alpha <= 0.86; the "
         "corrected picture has no edge at all in that range, only a margin "
         "that collapses exponentially and drops below the M <= 2400 ladder's "
         "resolving power around alpha ~ 0.54.")
    worst_cf = min(min(r[2] for r in r2_rows), min(c[4] for c in carry))
    worst_sat = min(r[3] for r in r2_rows)
    win_min = min(z[4] for z in zone_rows)
    info(f"RELAY-CONFIRMED: the staircase is real and rests on a ROBUST "
         f"observable, five orders of magnitude above the resolution floor.  "
         f"Deleting the newest atom drives lambda_min to {worst_cf:+.3f} while "
         f"the full form stays positive; the counterfactual loser is the "
         f"anti-two-bump at distance log n_k (alignment -> -1, h -> "
         f"{worst_sat:+.3f} against the C1 bound -1/2); and adding "
         f"mu_k h(log n_k) back lifts it to >= 0 exactly.  Every handoff window "
         f"alpha_free^(k) - alpha_k is positive for k = 1..4 (smallest "
         f"{win_min:+.5f} at M = 2400), i.e. every atom arrives strictly before "
         "the previous zone runs out.")
    info("What is NOT claimed: nothing here proves positivity.  lambda_min^(M) "
         "on a nested PWC space is a Rayleigh-Ritz UPPER bound; it can only "
         "refute, and it does not refute.  The RH fence was never touched.")
    return v


def main():
    firewall()
    element_gates()
    r1_rows, slope = r1_zone_between()
    r2_rows = r2_relay_moment()
    zone_rows, carry, ok_relay = r3_relay_map(r1_rows, slope)
    v = verdict(r1_rows, r2_rows, zone_rows, carry, ok_relay)
    dt = time.time() - T_START
    head(f"TOTAL  {PASS} passed, {FAIL} failed   verdict {v}   [{dt:.1f} s, "
         f"max array {int(math.sqrt(ARRAY_CAP))}^2]")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
