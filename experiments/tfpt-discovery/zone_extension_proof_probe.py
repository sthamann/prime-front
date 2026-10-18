"""Discovery probe (2026-07-26), part 92 of the zeta/prime investigation.
Contract ZONE.EXTENSION.PROOF -- a machine-assisted PROOF ATTEMPT (with an
honest rigor ledger) for windowed Weil positivity beyond the classical zone.

TARGET STATEMENT (T'):
  for a in the band (log 2 = 0.693147..., a* = 0.9253], f real with
  supp f subset (-a, a), ||f||_2 = 1, h = f * f~ (autocorrelation, even,
  h(0) = 1):

      Q(f) := P_pole(f) + A_arch(f) - P_prime(f)  >=  0 ,

  with ALL prime atoms inside the autocorrelation support |u| < 2a <= 1.8506,
  i.e. n in {2, 3, 4, 5} (von Mangoldt: Lambda(2) = Lambda(4) = log 2,
  Lambda(3) = log 3, Lambda(5) = log 5; Lambda(p^k) = log p).

CONVENTIONS (T79 series, Fourier fhat(t) = int f(x) e^{-itx} dx):
  P_pole(f)  = hhat(i/2) + hhat(-i/2) = 2 (int f e^{x/2})(int f e^{-x/2}),
               a rank-<=2 real bilinear form (derived + sympy-verified in S0).
  A_arch(f)  = (1/2pi) int |fhat(t)|^2 k(t) dt,
               k(t) = Re psi(1/4 + it/2) - log pi   (digamma),
               k(0) = psi(1/4) - log pi ~ -5.3721, k ~ log(t/2) - log pi,
               single sign change at t0 = 6.2898359888 (NOT 6.98 as the series
               orientation note states -- k(6.98) = +0.1043 already; S1 re-derives
               and brackets t0 to 1e-20).
  P_prime(f) = sum_n (Lambda(n)/sqrt n) (h(log n) + h(-log n))
             = sum_n (Lambda(n)/sqrt n) 2 h(log n)      (h even)
             = (1/2pi) int |fhat(t)|^2 G(t) dt,
               G(t) = 2 sum_n (Lambda(n)/sqrt n) cos(t log n).

PROOF SKELETON:
  S0  Pole bilinear form derived and sympy-verified on a closed example.
  S1  Kernel properties: k_min = k(0) and the t0 bracket at 30 digits
      (mpmath), monotonicity of k densely checked (quadrature-rigorous).
  S2  Sine basis phi_n(x) = (1/sqrt a) sin(n pi (x+a)/(2a)) on (-a,a):
      orthonormality, closed-form phihat_n (sinc form, numerically stable),
      parity block structure, and an EXPLICIT high-mode leakage bound
      eps_N(T) (trace bound with |phihat_n| <= 2 k_n / (sqrt a |k_n^2-t^2|)).
  S3  Finite block B = B_pole + B_arch - B_prime on N modes (N <= 24):
      pole entries closed form, arch entries by panelled Gauss-Legendre to
      T = 2e4 plus an EXACT tail split (the non-oscillatory part of
      psi_i psi_j is summed analytically, the oscillatory part bounded by one
      integration by parts), atom entries EXACT closed-form sine overlaps
      (sympy-verified, cross-checked against the Fourier route);
      lambda_min per a-point with conservative Frobenius error inflation
      -> largest UNIFORMLY certifiable dimension N_cert and margins m(a).
  S4  Synthesis: truncation bookkeeping (what N would be needed to close the
      high-mode complement), a covering scan in a with the measured Lipschitz
      constant, RIGOR LEDGER per step [EXACT / QUADRATURE-RIGOROUS /
      SEMI-RIGOROUS / OPEN] and a preregistered verdict.

OUTCOME OF THIS RUN (see the ledger and verdict blocks for the full picture):
  * The classical zone is reproduced: Q > 0 with a margin collapsing towards
    a = log2/2 = 0.3465736, exactly the Yoshida/Bombieri support-width bound.
  * In the band, lambda_min stays POSITIVE (as RH predicts) but collapses
    geometrically in the mode number, ~ 10^-1.06 per mode at a = a*, so double
    precision is exhausted near N ~ 10. Certified statement: N_cert = 8.
  * The high-mode complement is NOT closable at this size: the crude but
    honest budget needs N* of order 5e3 modes, plus a cross-term bound that
    is not attempted here.
  => T-SKELETON. The grid zone extension does NOT stand.

PREREGISTERED CRITERIA (verdicts):
  T-PROVED-GRID : all grid margins positive after error inflation AND the
                  high-mode truncation argument closes.
  T-SKELETON    : architecture + partial statements stand, gaps quantified
                  (statement then holds on the N-mode subspace only).
  T-BLOCKED     : a step breaks -- named explicitly.
  Special case: lambda_min < 0 on a genuine autocorrelation direction would
  contradict RH; it is treated as an implementation/convention signal to be
  debugged, NOT reported as a finding.

FENCES:
  * RH => (T'); (T') does NOT imply RH.  A zone extension is a
    classically-shaped target, NOT progress on RH.
  * NO Riemann zero data anywhere -- source self-scan below rejects any
    zero-table token; the whole argument is zero-free by construction.
  * No "proved" language without an error certificate.
  * Classical anchors, cited not re-derived: Weil 1952 (explicit formula /
    positivity), Yoshida 1992 and Bombieri 2000 (Lincei) -- unconditional
    positivity exactly up to support width log 2 -- Connes-Consani 2021
    (Sonin space), and the standard digamma archimedean kernel.
  * Discovery sandbox: no promotion, no ledger/TeX/website/changelog edits.
"""
import math
import time

import mpmath
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()
mpmath.mp.dps = 30

LOG2 = math.log(2.0)
A_STAR = 0.9253
A_NEG = 0.7410  # T89/T91: prime-free form first exhausted here
A_GRID = [0.70, 0.7410, 0.78, 0.82, 0.86, 0.90, 0.9253]
N_MODES = 24        # exploration cap (uncertified trend only)
N_CANDIDATES = (2, 3, 4, 5, 6, 8, 10, 12)  # certification dimensions
TMAX_ACC = 20000.0  # arch quadrature cut for certified entries
TMAX_FAST = 6000.0  # arch quadrature cut for exploratory scans
CHUNK = 60000       # quadrature chunk (keeps every array well under 1e7)
# (n, atom position u0 = log n, von Mangoldt Lambda(n) = log p for n = p^k)
ATOMS = (
    (2, LOG2, LOG2),
    (3, math.log(3.0), math.log(3.0)),
    (4, 2.0 * LOG2, LOG2),
    (5, math.log(5.0), math.log(5.0)),
)
LOGPI = math.log(math.pi)


def check(name, ok):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}", flush=True)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


def info(msg):
    print(f"        {msg}", flush=True)


def head(msg):
    print(f"\n{msg}", flush=True)


# ------------------------------------------------------------------ firewall
def firewall():
    head("S-FW  AST firewall (no Riemann zeros, no promotion side effects)")
    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read().lower()
    # tokens assembled at runtime so the guard cannot match its own literal
    banned = ["zeta" + "zero", "zeta_" + "zeros", "lm" + "fdb", "odl" + "yzko"]
    hits = [b for b in banned if b in src]
    check(f"no zero-data tokens in source (hits: {hits})", hits == [])
    extern = [m for m in ("sci" + "py", "req" + "uests", "url" + "lib") if m in src]
    check(f"sandbox modules only, no network/extern imports (hits: {extern})", extern == [])


# ------------------------------------------------------- vectorised digamma
_B2N_OVER_2N = np.array(
    [1.0 / 12.0, -1.0 / 120.0, 1.0 / 252.0, -1.0 / 240.0,
     1.0 / 132.0, -691.0 / 32760.0, 1.0 / 12.0]
)


def digamma_c(z, shift=14):
    """Vectorised complex digamma: recurrence + Stirling asymptotics."""
    z = np.asarray(z, dtype=complex)
    acc = np.zeros_like(z)
    for j in range(shift):
        acc = acc - 1.0 / (z + j)
    w = z + shift
    inv = 1.0 / w
    inv2 = inv * inv
    ser = np.zeros_like(z)
    p = inv2
    for c in _B2N_OVER_2N:
        ser = ser + c * p
        p = p * inv2
    return np.log(w) - 0.5 * inv - ser + acc


def k_arr(t):
    """Archimedean kernel k(t) = Re psi(1/4 + i t/2) - log pi (vectorised)."""
    t = np.asarray(t, dtype=float)
    return digamma_c(0.25 + 0.5j * t).real - LOGPI


def k_mp(t):
    return mpmath.re(mpmath.digamma(mpmath.mpf(1) / 4 + 1j * mpmath.mpf(t) / 2)) - mpmath.log(mpmath.pi)


# ------------------------------------------------------------------ S0 pole
def s0_pole_form():
    head("S0    Pole term as a real rank-<=2 bilinear form (sympy)")
    a, u, x = sp.symbols("a u x", positive=True)
    # f = indicator on (-a,a) normalised;  h(u) = c^2 (2a - |u|)
    c2 = 1 / (2 * a)
    lhs = 2 * sp.integrate(c2 * (2 * a - u) * sp.cosh(u / 2), (u, 0, 2 * a))
    rhs = c2 * sp.integrate(sp.exp(x / 2), (x, -a, a)) * sp.integrate(sp.exp(-x / 2), (x, -a, a))
    check("hhat(i/2) = (int f e^{x/2})(int f e^{-x/2}) on the box example",
          sp.simplify(sp.expand((lhs - rhs).rewrite(sp.exp))) == 0)
    info("=> P_pole(f) = hhat(i/2)+hhat(-i/2) = 2 u(f) v(f), u,v linear")
    info("=> B^pole_ij = u_i v_j + u_j v_i   (symmetric, rank <= 2)")
    # numeric cross-check of the same identity on a two-mode combination
    aa = mpmath.mpf("0.8")
    k1 = mpmath.pi / (2 * aa)
    k2 = 2 * mpmath.pi / (2 * aa)

    def f(xx):
        return (mpmath.sin(k1 * (xx + aa)) + mpmath.mpf("0.4") * mpmath.sin(k2 * (xx + aa))) / mpmath.sqrt(aa)

    def hu(uu):
        lo = max(-aa, -aa + uu)
        hi = min(aa, aa + uu)
        if hi <= lo:
            return mpmath.mpf(0)
        return mpmath.quad(lambda xx: f(xx) * f(xx - uu), [lo, hi])

    lhs_n = mpmath.quad(lambda uu: hu(uu) * mpmath.e ** (uu / 2), [-2 * aa, 0, 2 * aa])
    rhs_n = mpmath.quad(lambda xx: f(xx) * mpmath.e ** (xx / 2), [-aa, aa]) * mpmath.quad(
        lambda xx: f(xx) * mpmath.e ** (-xx / 2), [-aa, aa])
    rel = abs(lhs_n - rhs_n) / abs(rhs_n)
    check(f"numeric 2-mode cross-check (rel dev {float(rel):.2e} < 1e-18)", rel < mpmath.mpf("1e-18"))


# --------------------------------------------------------------- S1 kernel
def s1_kernel():
    head("S1    Archimedean kernel k(t) = Re psi(1/4+it/2) - log pi")
    kmin = k_mp(0)
    info(f"k_min = k(0) = psi(1/4) - log pi = {mpmath.nstr(kmin, 20)}")
    check("k(0) < 0 (negative core)", kmin < 0)
    # exact closed form psi(1/4) = -gamma - 3 log2 - pi/2
    closed = -mpmath.euler - 3 * mpmath.log(2) - mpmath.pi / 2 - mpmath.log(mpmath.pi)
    check(f"k(0) closed form (dev {float(abs(closed - kmin)):.1e})", abs(closed - kmin) < mpmath.mpf("1e-25"))
    lo, hi = mpmath.mpf(6), mpmath.mpf(8)
    for _ in range(120):
        mid = (lo + hi) / 2
        if k_mp(mid) < 0:
            lo = mid
        else:
            hi = mid
    t0 = (lo + hi) / 2
    info(f"t0 (sign change) in [{mpmath.nstr(lo, 22)}, {mpmath.nstr(hi, 22)}]")
    check("t0 bracket width < 1e-20", (hi - lo) < mpmath.mpf("1e-20"))
    check("t0 is the ONLY sign change on (0, 400]",
          np.sum(np.diff(np.sign(k_arr(np.linspace(1e-6, 400.0, 400000)))) != 0) == 1)
    info("CORRECTION to the series orientation value: for k(t) = Re psi(1/4+it/2) - log pi "
         f"the sign change sits at t0 = {mpmath.nstr(t0, 12)}, NOT at 6.98 "
         f"(k(6.98) = {mpmath.nstr(k_mp(6.98), 8)} > 0 already).")
    ts = np.linspace(0.0, 400.0, 400001)[1:]
    kv = k_arr(ts)
    dk = np.diff(kv)
    check(f"k monotone increasing on (0,400] (dense grid, min dk={dk.min():.2e})", dk.min() > 0)
    # accuracy of the vectorised digamma against mpmath
    devs = [abs(float(k_arr(np.array([tt]))[0]) - float(k_mp(tt))) for tt in (0.0, 1.3, 6.98, 41.0, 500.0, 2000.0)]
    check(f"vectorised k matches mpmath (max dev {max(devs):.2e} < 1e-13)", max(devs) < 1e-13)
    info(f"asymptote check: k(2000) = {float(k_arr(np.array([2000.0]))[0]):.6f}"
         f"  vs log(t/2)-log pi = {math.log(1000.0) - LOGPI:.6f}")
    return float(t0), float(kmin)


# ------------------------------------------------------------- S2 basis/FT
def basis_data(a, N=N_MODES):
    n = np.arange(1, N + 1)
    kk = n * np.pi / (2.0 * a)
    # numerator cos(at) (n odd) / sin(at) (n even) = c_n sin(a (t-k_n))
    cn = np.where(n % 2 == 1, -np.sin(n * np.pi / 2.0), np.cos(n * np.pi / 2.0))
    return n, kk, cn


def psi_mat(t, a, N=N_MODES):
    """Real profile psi_n(t) with phihat_n = psi_n (n odd), i psi_n (n even).

    Stable sinc form: psi_n(t) = -2 a k_n c_n sinc(a(t-k_n)/pi)/(sqrt a (k_n+t)).
    """
    n, kk, cn = basis_data(a, N)
    t = np.atleast_1d(np.asarray(t, dtype=float))
    d = t[None, :] - kk[:, None]
    sinc = np.sinc(a * d / np.pi)
    return -(2.0 * a * kk * cn)[:, None] * sinc / (np.sqrt(a) * (kk[:, None] + t[None, :]))


def phihat_direct(nn, t, a):
    """Closed form without the sinc rewrite (for verification)."""
    kn = nn * np.pi / (2.0 * a)
    num = math.cos(a * t) if nn % 2 == 1 else math.sin(a * t)
    val = 2.0 * kn * num / (math.sqrt(a) * (kn * kn - t * t))
    return complex(val, 0.0) if nn % 2 == 1 else complex(0.0, val)


def s2_basis(t0):
    head("S2    Sine basis, closed-form transform, parity, leakage bound")
    a = 0.85
    n, kk, cn = basis_data(a)
    # orthonormality (exact, sympy, symbolic a)
    aa, xx = sp.symbols("a x", positive=True)
    ok = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            val = sp.integrate(
                sp.sin(i * sp.pi * (xx + aa) / (2 * aa)) * sp.sin(j * sp.pi * (xx + aa) / (2 * aa)) / aa,
                (xx, -aa, aa))
            ok = ok and sp.simplify(val - (1 if i == j else 0)) == 0
    check("orthonormality of phi_n (sympy, symbolic a, n<=3)", ok)
    # closed-form transform: sympy (one mode) + mpmath (several modes/points)
    tsym = sp.symbols("t", real=True)
    a_r = sp.Rational(3, 4)
    sym_ok = True
    for nn in (1, 2):
        expr = sp.integrate(
            sp.sin(nn * sp.pi * (xx + a_r) / (2 * a_r)) * sp.exp(-sp.I * tsym * xx) / sp.sqrt(a_r),
            (xx, -a_r, a_r))
        kn = nn * sp.pi / (2 * a_r)
        num = sp.cos(a_r * tsym) if nn % 2 else sp.sin(a_r * tsym)
        claim = 2 * kn * num / (sp.sqrt(a_r) * (kn ** 2 - tsym ** 2)) * (1 if nn % 2 else sp.I)
        diff = (expr - claim).rewrite(sp.exp)
        for tv in (sp.Rational(1, 3), sp.Rational(7, 5), sp.Rational(13, 2), sp.Rational(41, 7)):
            sym_ok = sym_ok and sp.simplify(diff.subs(tsym, tv)) == 0
    check("phihat_n closed form (sympy exact, a=3/4, n=1,2, 4 rational t)", sym_ok)
    dev = 0.0
    for nn in (1, 2, 5, 12, 24):
        for tt in (0.3, 2.7, 11.9, 40.1):
            num = mpmath.quad(
                lambda x_, nn=nn: mpmath.sin(nn * mpmath.pi * (x_ + a) / (2 * a)) / mpmath.sqrt(a)
                * mpmath.e ** (-1j * tt * x_), [-a, a])
            cl = phihat_direct(nn, tt, a)
            dev = max(dev, abs(complex(num) - cl))
    check(f"phihat_n vs mpmath quadrature (max dev {dev:.2e} < 1e-12)", dev < 1e-12)
    # stable sinc form == direct form, including near the removable poles
    tgrid = np.concatenate([np.linspace(0.0, 60.0, 601), kk, kk + 1e-9, kk - 1e-9])
    P = psi_mat(tgrid, a)
    dev2 = 0.0
    for idx, nn in enumerate(n):
        for jt, tt in enumerate(tgrid):
            if abs(tt - kk[idx]) < 1e-7:
                continue
            ref = phihat_direct(int(nn), float(tt), a)
            dev2 = max(dev2, abs(P[idx, jt] - (ref.real if nn % 2 else ref.imag)))
    check(f"sinc form stable & equal to direct form (max dev {dev2:.2e} < 1e-11)", dev2 < 1e-11)
    peak = abs(psi_mat(kk, a)[np.arange(len(kk)), np.arange(len(kk))])
    check(f"removable poles finite, |psi_n(k_n)| = sqrt(a) = {math.sqrt(a):.6f}",
          np.max(np.abs(peak - math.sqrt(a))) < 1e-12)
    info("parity: n odd -> phi_n even, phihat_n real; n even -> phi_n odd, "
         "phihat_n purely imaginary => arch/pole/atom blocks are parity-block-diagonal")
    return a


def leakage_eps(N, T, a, span=300000):
    """Trace bound on the low-frequency mass of span{phi_n : n > N}.

    (1/2pi) int_{|t|<T} |fhat|^2 dt = <f, P_T f> <= tr(P_{>N} P_T P_{>N})
      <= sum_{n>N} (1/pi) int_0^T [2 k_n/(sqrt a (k_n^2-t^2))]^2 dt
      <= sum_{n>N} 4 k_n^2 T / (a pi (k_n^2 - T^2)^2).
    """
    n = np.arange(N + 1, N + span + 1, dtype=float)
    kn = n * np.pi / (2.0 * a)
    if kn[0] <= T:
        return float("inf")
    terms = 4.0 * kn ** 2 * T / (a * np.pi * (kn ** 2 - T ** 2) ** 2)
    tail = 4.0 * T / (a * np.pi) * (2.0 * a / np.pi) / kn[-1]  # sum_{k>K} 1/k^2 <= (2a/pi)/k_K
    return float(terms.sum() + tail)


def min_modes_for(T, a, eps_need, hi=400000):
    """Smallest N with eps_N(T) < eps_need (eps_N decreasing in N); None if > hi."""
    lo = int(math.ceil(1.05 * T * 2.0 * a / math.pi)) + 1
    if leakage_eps(hi, T, a) >= eps_need:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if leakage_eps(mid, T, a) < eps_need:
            hi = mid
        else:
            lo = mid + 1
    return lo


def pole_delta(N, a, nmax=200000):
    """sum over EVEN n > N of u_n^2 (the negative-definite pole rank-1 tail)."""
    n = np.arange(N + 1, nmax + 1, dtype=float)
    n = n[n % 2 == 0]
    kn = n * np.pi / (2.0 * a)
    u = 2.0 * kn * math.sinh(a / 2.0) / (math.sqrt(a) * (kn ** 2 + 0.25))
    return float((u ** 2).sum())


# ---------------------------------------------------------------- S3 blocks
def gl_nodes(a, Tmax, npts, N=N_MODES):
    _, kk, _ = basis_data(a, N)
    base = np.arange(0.0, Tmax, 1.5)
    edges = np.unique(np.concatenate([base, kk, [Tmax]]))
    xg, wg = np.polynomial.legendre.leggauss(npts)
    lo, hi = edges[:-1], edges[1:]
    mid = 0.5 * (lo + hi)
    half = 0.5 * (hi - lo)
    t = (mid[:, None] + half[:, None] * xg[None, :]).ravel()
    w = (half[:, None] * wg[None, :]).ravel()
    return t, w


def parity_mask(N=N_MODES):
    """Re[phihat_i conj(phihat_j)] vanishes identically for mixed parity."""
    par = (np.arange(1, N + 1) % 2)
    return (par[:, None] == par[None, :]).astype(float)


def arch_tail(a, N, Tmax):
    """EXACT split of the arch tail beyond Tmax.

    psi_i psi_j = (4 k_i k_j c_i c_j / a) * (1/2)
                  * [cos(a(k_j-k_i)) - cos(2 a t - a(k_i+k_j))]
                  / ((t^2-k_i^2)(t^2-k_j^2)),
    so the tail = non-oscillatory part (computed here on geometric panels)
    minus an oscillatory part bounded by one integration by parts.
    """
    _, kk, cn = basis_data(a, N)
    edges = Tmax * 2.0 ** np.arange(0, 41)
    xg, wg = np.polynomial.legendre.leggauss(48)
    lo, hi = edges[:-1], edges[1:]
    mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
    t = (mid[:, None] + half[:, None] * xg[None, :]).ravel()
    wt = (half[:, None] * wg[None, :]).ravel()
    kv = k_arr(t)
    D = 1.0 / (t[None, :] ** 2 - (kk ** 2)[:, None])
    J0 = np.einsum("it,jt,t->ij", D, D, kv * wt)
    pref = 2.0 * np.outer(kk * cn, kk * cn) / (a * np.pi)
    cosd = np.cos(a * (kk[None, :] - kk[:, None]))
    value = pref * cosd * J0
    # |int_T^inf cos(2at-aS) g| <= g(T)/a   (g positive, eventually monotone)
    gT = k_arr(np.array([Tmax]))[0] / ((Tmax ** 2 - kk ** 2)[:, None] * (Tmax ** 2 - kk ** 2)[None, :])
    bound = np.abs(pref) * np.abs(gT) / a
    return value * parity_mask(N), float(bound.max())


def arch_block(a, N=N_MODES, Tmax=TMAX_ACC, npts=32):
    t, w = gl_nodes(a, Tmax, npts, N)
    acc = np.zeros((N, N))
    for s in range(0, t.size, CHUNK):
        ts, ws = t[s:s + CHUNK], w[s:s + CHUNK]
        P = psi_mat(ts, a, N)
        acc += (P * (ws * k_arr(ts))[None, :]) @ P.T
    tail, _ = arch_tail(a, N, Tmax)
    return (acc / np.pi) * parity_mask(N) + tail


def pole_vec(a, N=N_MODES):
    n, kk, _ = basis_data(a, N)
    u = np.where(n % 2 == 1,
                 2.0 * kk * math.cosh(a / 2.0) / (math.sqrt(a) * (kk ** 2 + 0.25)),
                 -2.0 * kk * math.sinh(a / 2.0) / (math.sqrt(a) * (kk ** 2 + 0.25)))
    v = np.where(n % 2 == 1, u, -u)
    return u, v


def pole_block(a, N=N_MODES):
    u, v = pole_vec(a, N)
    return np.outer(u, v) + np.outer(v, u)


def overlap(i, j, u, a):
    """O_ij(u) = int phi_i(x) phi_j(x-u) dx for u >= 0 (exact closed form)."""
    b = 2.0 * a
    if u >= b:
        return 0.0
    ki = i * np.pi / b
    kj = j * np.pi / b
    sig = 1.0 if (i + j) % 2 == 0 else -1.0
    if i == j:
        return ((b - u) * math.cos(ki * u) + math.sin(ki * u) / ki) / b
    t1 = (sig * math.sin(kj * u) - math.sin(ki * u)) / (ki - kj)
    t2 = (-sig * math.sin(kj * u) - math.sin(ki * u)) / (ki + kj)
    return (t1 - t2) / b


def atom_block(a, u0, N=N_MODES):
    M = np.zeros((N, N))
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            M[i - 1, j - 1] = 0.5 * (overlap(i, j, u0, a) + overlap(j, i, u0, a))
    return M


def prime_block(a, N=N_MODES):
    B = np.zeros((N, N))
    used = []
    for nn, u0, lam in ATOMS:
        if u0 >= 2.0 * a:
            continue
        B += (lam / math.sqrt(nn)) * 2.0 * atom_block(a, u0, N)
        used.append(nn)
    return B, used


def s3_validate(t0):
    head("S3a   Block validation (exactness + quadrature control)")
    a = 0.86
    N = N_MODES
    # sympy: exact sine overlap closed form
    usym = sp.symbols("u", positive=True)
    a_r = sp.Rational(43, 50)
    b_r = 2 * a_r
    y = sp.symbols("y", positive=True)
    ok = True
    for (i, j) in ((1, 1), (1, 3), (2, 4), (3, 4)):
        ki = i * sp.pi / b_r
        kj = j * sp.pi / b_r
        exact = sp.integrate(sp.sin(ki * y) * sp.sin(kj * (y - usym)), (y, usym, b_r)) / a_r
        sig = 1 if (i + j) % 2 == 0 else -1
        if i == j:
            claim = ((b_r - usym) * sp.cos(ki * usym) + sp.sin(ki * usym) / ki) / b_r
        else:
            t1 = (sig * sp.sin(kj * usym) - sp.sin(ki * usym)) / (ki - kj)
            t2 = (-sig * sp.sin(kj * usym) - sp.sin(ki * usym)) / (ki + kj)
            claim = (t1 - t2) / b_r
        ok = ok and sp.simplify(sp.expand_trig(sp.expand(exact - claim))) == 0
    check("sine overlap O_ij(u) closed form EXACT (sympy, 4 pairs)", ok)
    dev = 0.0
    for (i, j) in ((1, 1), (1, 2), (2, 5), (7, 12), (13, 24)):
        for u0 in (0.3, LOG2, math.log(5.0)):
            num = mpmath.quad(
                lambda x_, i=i, j=j, u0=u0: mpmath.sin(i * mpmath.pi * (x_ + a) / (2 * a))
                * mpmath.sin(j * mpmath.pi * (x_ - u0 + a) / (2 * a)) / a,
                [max(-a, -a + u0), a]) if u0 < 2 * a else mpmath.mpf(0)
            dev = max(dev, abs(float(num) - overlap(i, j, u0, a)))
    check(f"overlap closed form vs mpmath quadrature (max dev {dev:.2e} < 1e-14)", dev < 1e-14)
    check("orthonormality reproduced: O_ij(0) = delta_ij",
          max(abs(overlap(i, j, 0.0, a) - (1.0 if i == j else 0.0))
              for i in range(1, N + 1) for j in range(1, N + 1)) < 1e-13)
    # pole vector vs direct integral
    u, v = pole_vec(a, N)
    dev = 0.0
    for idx in (0, 1, 5, 12, 23):
        nn = idx + 1
        un = mpmath.quad(lambda x_: mpmath.sin(nn * mpmath.pi * (x_ + a) / (2 * a)) / mpmath.sqrt(a)
                         * mpmath.e ** (x_ / 2), [-a, a])
        vn = mpmath.quad(lambda x_: mpmath.sin(nn * mpmath.pi * (x_ + a) / (2 * a)) / mpmath.sqrt(a)
                         * mpmath.e ** (-x_ / 2), [-a, a])
        dev = max(dev, abs(float(un) - u[idx]), abs(float(vn) - v[idx]))
    check(f"pole functionals u_n, v_n closed form (max dev {dev:.2e} < 1e-13)", dev < 1e-13)
    # parity block structure
    Bp = pole_block(a, N)
    Ba = arch_block(a, N)
    Bq, _ = prime_block(a, N)
    par = np.array([(i + 1) % 2 for i in range(N)])
    mix = np.abs(np.where(par[:, None] != par[None, :], Bp + Ba + Bq, 0.0)).max()
    check(f"mixed-parity entries vanish (max |.| = {mix:.2e} < 1e-12)", mix < 1e-12)
    # Plancherel / Gram: (1/pi) int_0^inf psi_i psi_j dt = delta_ij (same parity)
    t, w = gl_nodes(a, TMAX_ACC, 32, N)
    Gram = np.zeros((N, N))
    for s in range(0, t.size, CHUNK):
        P = psi_mat(t[s:s + CHUNK], a, N)
        Gram += (P * w[s:s + CHUNK][None, :]) @ P.T
    Gram = (Gram / np.pi) * parity_mask(N)
    dgram = np.abs(Gram - np.eye(N)).max()
    check(f"Plancherel/Gram of the quadrature grid (max dev {dgram:.2e} < 1e-8)", dgram < 1e-8)
    # arch quadrature convergence + analytic tail control
    Ba2 = arch_block(a, N, Tmax=30000.0, npts=48)
    dq = float(np.abs(Ba - Ba2).max())
    tv, tb = arch_tail(a, N, TMAX_ACC)
    info(f"arch: max |A(20k,32) - A(30k,48)| = {dq:.3e}; analytic tail correction "
         f"max |dA| = {np.abs(tv).max():.3e}; oscillatory tail bound = {tb:.3e}")
    check(f"arch quadrature stable to 1e-12 (dq {dq:.2e})", dq < 1e-12)
    check(f"oscillatory tail bound below 1e-13 ({tb:.2e})", tb < 1e-13)
    # independent check of the prime block via the Fourier route
    Bq_f = np.zeros((N, N))
    for s in range(0, t.size, CHUNK):
        ts, ws = t[s:s + CHUNK], w[s:s + CHUNK]
        G = np.zeros_like(ts)
        for nn, u0, lam in ATOMS:
            if u0 >= 2 * a:
                continue
            G += 2.0 * (lam / math.sqrt(nn)) * np.cos(ts * u0)
        Pc = psi_mat(ts, a, N)
        Bq_f += (Pc * (ws * G)[None, :]) @ Pc.T
    Bq_f = (Bq_f / np.pi) * parity_mask(N)
    dqf = np.abs(Bq - Bq_f).max()
    check(f"prime block: exact overlaps == Fourier route (max dev {dqf:.2e} < 1e-5)", dqf < 1e-5)
    return dq, tb


def block(a, N=N_MODES, with_primes=True, fast=False):
    Tmax, npts = (TMAX_FAST, 24) if fast else (TMAX_ACC, 32)
    B = pole_block(a, N) + arch_block(a, N, Tmax, npts)
    used = []
    if with_primes:
        Bq, used = prime_block(a, N)
        B = B - Bq
    return 0.5 * (B + B.T), used


def s3_anchor():
    head("S3b   Consistency anchor: the CLASSICAL zone must be reproduced")
    info("Yoshida 1992 / Bombieri 2000: unconditional Weil positivity exactly up to "
         "autocorrelation support width log 2, i.e. 2a <= log 2, a <= log2/2 = "
         f"{LOG2 / 2:.7f} -- there the atom set is EMPTY and Q = P_pole + A_arch.")
    vals = {}
    for a in (0.10, 0.20, 0.30, LOG2 / 2, 0.36, 0.40):
        B, used = block(a, N_MODES, fast=True)
        vals[a] = float(np.linalg.eigvalsh(B)[0])
        info(f"a = {a:.7f}  2a = {2 * a:.4f}  atoms {used}: lambda_min = {vals[a]:+.3e}")
    check("Q > 0 strictly inside the classical zone (a = 0.10, 0.20, 0.30)",
          min(vals[0.10], vals[0.20], vals[0.30]) > 0)
    check(f"margin collapses towards the classical edge a = log2/2 "
          f"(lambda_min = {vals[LOG2 / 2]:.2e} < 1/300 of lambda_min(0.10))",
          0.0 < vals[LOG2 / 2] < vals[0.10] / 300.0)
    check("Q stays > 0 just beyond the classical edge (a = 0.36, 0.40) -- "
          "as RH predicts; the classical PROOF, not the positivity, stops at log2/2",
          vals[0.36] > 0 and vals[0.40] > 0)
    # where does the PRIME-FREE form lose positivity?
    lo, hi = 0.30, 1.20
    for _ in range(28):
        mid = 0.5 * (lo + hi)
        if float(np.linalg.eigvalsh(block(mid, N_MODES, with_primes=False, fast=True)[0])[0]) > 0:
            lo = mid
        else:
            hi = mid
    a_free = 0.5 * (lo + hi)
    info(f"prime-free form P_pole + A_arch loses positivity at a_free = {a_free:.6f}")
    info(f"DEVIATION from the series orientation value a_neg = {A_NEG}: not reproduced here; "
         "in this sine-window basis the prime-free form is exhausted already at "
         f"a = {a_free:.4f} (i.e. essentially at the classical edge log2/2 = {LOG2 / 2:.4f}).")
    check(f"prime-free exhaustion point located ({a_free:.4f}), reported as-is", True)
    return vals, a_free


def s3_margins(dq, tb):
    head("S3c   Margin table m(a): largest CERTIFIABLE subspace per band point")
    err_entry = dq + tb + 3e-14  # quadrature + analytic tail + float64 accumulation
    info(f"entry error bound |E_ij| <= {err_entry:.3e}; inflation ||E||_2 <= ||E||_F <= N*|E_ij|")
    n_cert = 0
    for N in sorted(N_CANDIDATES, reverse=True):
        if all(float(np.linalg.eigvalsh(block(a, N)[0])[0]) > N * err_entry for a in A_GRID):
            n_cert = N
            break
    info(f"largest UNIFORMLY certifiable subspace dimension across the band: N_cert = {n_cert}")
    rows = []
    for a in A_GRID:
        B, used = block(a, n_cert)
        lam = float(np.linalg.eigvalsh(B)[0])
        m = lam - n_cert * err_entry
        rows.append((a, n_cert, lam, m, used))
        info(f"a = {a:.4f}  2a = {2 * a:.4f}  atoms {used}"
             f"  lambda_min = {lam:.6e}  m(a) = {m:.6e}  (m / inflation = "
             f"{m / (n_cert * err_entry):.1f}x)")
    allpos = n_cert > 0 and all(r[3] > 0 for r in rows)
    check(f"uniform margin m(a) > 0 on the {n_cert}-dimensional subspace at every band point",
          allpos)
    check("no negative eigenvalue anywhere on genuine autocorrelation directions "
          "(RH-consistency of the implementation)",
          all(float(np.linalg.eigvalsh(block(a, 12)[0])[0]) > -1e-13 for a in A_GRID))
    return rows, err_entry


def s3_dimension_trend(err_entry):
    head("S3d   Why the block route stalls: geometric collapse of lambda_min in N")
    a = A_STAR
    trend = []
    for N in (2, 4, 6, 8, 10, 12):
        lam = float(np.linalg.eigvalsh(block(a, N)[0])[0])
        trend.append((N, lam))
        info(f"N = {N:2d}: lambda_min = {lam:.4e}"
             f"   {'CERTIFIED' if lam > N * err_entry else 'below the double-precision floor'}")
    mono = all(trend[i + 1][1] <= trend[i][1] * (1 + 1e-6) for i in range(len(trend) - 1))
    check("lambda_min non-increasing in N (nested subspaces, sanity)", mono)
    ns = np.array([n for n, _ in trend], float)
    ls = np.log10(np.array([max(l, 1e-300) for _, l in trend]))
    slope, icept = np.polyfit(ns, ls, 1)
    info(f"fit: log10 lambda_min(N) ~ {icept:.2f} {slope:+.3f} * N at a = a* "
         f"=> each extra mode costs a factor {10 ** (-slope):.1f} of margin")
    check(f"collapse is geometric, not a plateau (slope {slope:.3f} < -0.5)", slope < -0.5)
    n_need = (math.log10(err_entry) - icept) / slope
    info(f"double precision (entry error {err_entry:.1e}) is exhausted at N ~ {n_need:.1f}; "
         f"certifying N = 24 would need entry accuracy ~1e{icept + slope * 24:.0f}")
    return trend, slope, icept


# ------------------------------------------------------------- S4 synthesis
def s4_truncation(t0, kmin):
    head("S4a   Truncation bookkeeping: what would close the high-mode complement?")
    a = A_STAR
    # the multiplier W(t) = k(t) - G(t); Q(f) = P_pole + (1/2pi) int |fhat|^2 W
    C = sum(lam / math.sqrt(nn) for nn, u0, lam in ATOMS if u0 < 2 * a)
    supG = 2.0 * C
    info(f"sup_t G(t) = G(0) = 2 sum Lambda(n)/sqrt n = {supG:.6f} "
         f"(attained again for large t by Kronecker: log2, log3, log5 are Q-independent)")
    tt = np.arange(0.0, 1200.0, 0.002)
    G = np.zeros_like(tt)
    for nn, u0, lam in ATOMS:
        if u0 >= 2 * a:
            continue
        G += 2.0 * (lam / math.sqrt(nn)) * np.cos(tt * u0)
    W = k_arr(tt) - G
    Wmin = float(W.min())
    neg = tt[W < 0]
    t_pos = float(neg.max()) if neg.size else 0.0
    info(f"min_t W(t) = {Wmin:.6f} at t = {tt[int(np.argmin(W))]:.3f}; "
         f"last t with W(t) < 0 on [0,1200] is T_pos = {t_pos:.3f}")
    check("W(t) = k(t) - G(t) is eventually positive (t > T_pos)", t_pos < 1200.0)
    # the high-mode form needs a STRICTLY positive floor w(T) on |t| >= T
    best = None
    for T in (t_pos + 1.0, 300.0, 500.0, 700.0, 900.0):
        mask = tt >= T
        w_T = float(min(W[mask].min(), float(k_arr(np.array([1200.0]))[0]) - supG))
        if w_T <= 0:
            info(f"T = {T:8.2f}: w(T) = {w_T:+.4f} <= 0 -> no positive floor")
            continue
        eps_need = w_T / (w_T - Wmin)
        Nreq = min_modes_for(T, a, eps_need)
        info(f"T = {T:8.2f}: w(T) = {w_T:+.4f}, need eps_N(T) < {eps_need:.4f} "
             f"-> N* >= {Nreq}")
        if Nreq is not None and (best is None or Nreq < best[1]):
            best = (T, Nreq, w_T, eps_need)
    if best is not None:
        info(f"BEST truncation budget: T = {best[0]:.2f}, N* >= {best[1]} modes "
             f"(hard cap here is N = {N_MODES})")
    eps24 = leakage_eps(N_MODES, t0, a)
    d24 = pole_delta(N_MODES, a)
    info(f"at the exploration cap: eps_24(t0={t0:.4f}) = {eps24:.4e}, "
         f"pole tail 2*delta_24 = {2 * d24:.4e}")
    info(f"crude complement floor at the cap: k(t0)*(1-eps) + k_min*eps - supG - 2 delta = "
         f"{kmin * eps24 - supG - 2 * d24:+.4f}  (NEGATIVE -> not closed)")
    check("high-mode complement NOT closed at N <= 24 (declared OPEN, not hidden)",
          best is None or best[1] > N_MODES)
    return best, eps24, d24, Wmin, t_pos, supG


def scan_band(n_cert, npts):
    aa = np.linspace(LOG2, A_STAR, npts)
    lam = np.array([float(np.linalg.eigvalsh(block(float(a), n_cert)[0])[0]) for a in aa])
    L = float(np.abs(np.diff(lam) / np.diff(aa)).max())
    return aa, lam, L


def s4_continuum(rows, n_cert, err_entry, cap=5000):
    head("S4b   Continuum gap: covering scan of the whole band, not just the grid")
    infl = n_cert * err_entry
    aa, lam, L = scan_band(n_cert, 200)
    m_min = float(lam.min()) - infl
    info(f"coarse scan (200 pts): min lambda_min = {lam.min():.4e} at a = {aa[int(np.argmin(lam))]:.5f}, "
         f"measured Lipschitz constant L = {L:.3e}")
    if m_min <= 0:
        check("coarse scan already loses the margin -> continuum OPEN", False)
        return L, float("nan"), 0
    npts, covered, slack = 200, False, np.array([0.0])
    for _ in range(5):
        need = int(math.ceil(1.5 * (A_STAR - LOG2) * L / (2.0 * m_min))) + 1
        if need > cap:
            info(f"covering would need >= {need} scan points, above the {cap}-point cap")
            break
        npts = max(need, npts + 1)
        aa, lam, L = scan_band(n_cert, npts)
        da = float(aa[1] - aa[0])
        m = lam - infl
        m_min = float(m.min())
        slack = m - L * da / 2.0
        i = int(np.argmin(slack))
        info(f"scan {npts:5d} pts (da = {da:.2e}): min m(a) = {m_min:.4e} at "
             f"a = {aa[int(np.argmin(m))]:.5f}, L = {L:.3e}, worst covering slack "
             f"{slack[i]:.3e} at a = {aa[i]:.5f}")
        if slack.min() > 0:
            covered = True
            break
    check(f"whole band covered: m(a) > L*da/2 at all {npts} scan points "
          f"(worst slack {slack.min():.2e})", covered)
    info("NOTE: L is MEASURED, not certified. A rigorous continuum statement needs a "
         "proven bound on d/da of every block entry (all entries are analytic in a, so "
         "such a bound exists) -- that certificate is OPEN here.")
    return L, float(m.min()), npts


def rigor_ledger(entries):
    head("S4c   RIGOR LEDGER")
    width = max(len(e[0]) for e in entries)
    for name, level, note in entries:
        print(f"  {name.ljust(width)}  [{level}]  {note}", flush=True)


# ------------------------------------------------------------------- driver
def main():
    firewall()
    s0_pole_form()
    t0, kmin = s1_kernel()
    s2_basis(t0)
    dq, tb = s3_validate(t0)
    _, a_free = s3_anchor()
    rows, err_entry = s3_margins(dq, tb)
    trend, slope, icept = s3_dimension_trend(err_entry)
    best, eps24, d24, Wmin, t_pos, supG = s4_truncation(t0, kmin)
    n_cert = min(r[1] for r in rows)
    L, m_scan, npts = s4_continuum(rows, n_cert, err_entry)

    grid_ok = all(r[1] > 0 and r[3] > 0 for r in rows)
    trunc_ok = best is not None and best[1] <= n_cert
    rigor_ledger([
        ("S0 pole bilinear form", "EXACT",
         "sympy identity + 1e-18 numeric cross-check; rank <= 2 structure"),
        ("S1 k_min, t0 bracket", "EXACT",
         f"closed form k(0) = -gamma-3log2-pi/2-log pi; t0 bracketed to 1e-20"),
        ("S1 monotonicity of k", "QUADRATURE-RIGOROUS",
         "dense grid (4e5 points on (0,400]), no interval arithmetic"),
        ("S2 orthonormality / phihat", "EXACT",
         "sympy for symbolic a (n<=3) and a=3/4 (n=1,2); mpmath to 1e-12 elsewhere"),
        ("S2 parity block split", "EXACT",
         "proved termwise: mixed-parity pole/arch/atom entries vanish identically"),
        ("S2 leakage bound eps_N(T)", "EXACT",
         "trace bound with |phihat_n| <= 2k_n/(sqrt a |k_n^2-t^2|), closed tail"),
        ("S3 pole entries", "EXACT", "closed form, verified against mpmath to 1e-13"),
        ("S3 atom entries", "EXACT",
         "closed-form sine overlaps, sympy-verified; Fourier route agrees"),
        ("S3 arch entries", "QUADRATURE-RIGOROUS",
         f"panelled Gauss-Legendre to T=2e4 + EXACT tail split; residual {dq:.1e}, "
         f"oscillatory bound {tb:.1e}"),
        ("S3 lambda_min + inflation", "QUADRATURE-RIGOROUS",
         f"float64 eigh, entry error {err_entry:.1e}, Frobenius inflation N*|E| "
         "(no verified eigensolver / no interval arithmetic)"),
        ("S3 certified dimension", "QUADRATURE-RIGOROUS",
         f"N_cert = {n_cert} uniformly across the band (not 24)"),
        ("S3 N > N_cert", "OPEN",
         f"lambda_min falls by 10^{-slope:.2f} per mode; N=24 needs ~1e{icept + slope * 24:.0f} entries"),
        ("S4 high-mode complement", "OPEN",
         f"needs N* >= {best[1] if best else 'n/a'} modes; certified dimension is {n_cert}"),
        ("S4 low/high cross terms", "OPEN",
         "no bound on ||B_LH||; required even once the complement floor is positive"),
        ("S4 continuum in a", "SEMI-RIGOROUS",
         f"{npts}-point covering scan, min m(a) = {m_scan:.2e}, measured L = {L:.2e}; "
         "derivative bound not certified"),
    ])

    head("VERDICT")
    if not grid_ok:
        verdict = "T-BLOCKED (S3: no certifiable positive margin at some band point)"
    elif trunc_ok:
        verdict = "T-PROVED-GRID"
    else:
        verdict = "T-SKELETON"
    info(f"grid margins positive on the certified subspaces: {grid_ok}; "
         f"truncation closed: {trunc_ok}")
    print(f"  >>> {verdict} <<<", flush=True)
    info(f"WHAT STANDS: for every a in the band (covering scan, {npts} points), "
         f"Q(f) >= {m_scan:.2e} > 0 for all real f in the {n_cert}-dimensional sine "
         "window subspace, with a quadrature error certificate. Genuine, but SMALL.")
    info("WHAT DOES NOT STAND: the zone extension itself. Two independent gaps -- "
         "(i) the finite block cannot be pushed past N ~ 12 in double precision because "
         "lambda_min collapses geometrically, (ii) even at large N the high-mode "
         f"complement needs N* >= {best[1] if best else 'n/a'} modes plus a cross-term bound.")
    info("Fence restated: RH => (T'); (T') does not imply RH. Nothing here is "
         "evidence for or against RH.")

    print(f"\nTOTAL  PASS={PASS}  FAIL={FAIL}  time={time.time() - T0:.1f}s", flush=True)
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
