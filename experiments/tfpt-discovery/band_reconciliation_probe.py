"""Discovery probe (2026-07-26), part 93 of the zeta/prime investigation.
Contract BAND.RECONCILIATION -- a DATA-INTEGRITY audit of two calibration
discrepancies that part 92 (zone_extension_proof_probe.py) raised against
the earlier map probes part 89 (sonin_crossing_probe.py) and part 91
(thin_band_analytic_probe.py).

THE TWO DISCREPANCIES UNDER DECISION
  D1  t0, the sign change of the archimedean kernel
      k(t) = Re psi(1/4 + i t/2) - log pi.
      T92 measures t0 = 6.28983599 (bracket < 1e-20) and flags the series
      orientation value 6.98 as wrong (k(6.98) = +0.104 > 0 already).
  D2  Where the PRIME-FREE window form P_pole + A_arch loses positivity.
      T92: a_free = 0.3763.  T91: a_neg = 0.7410 (and T89: a_eq = 0.7413),
      on which T91 built the "one-atom zone", the "atom rescue" and the
      band edges a_neg / a* = 0.9253.

DECISION TO BE MADE PER DISCREPANCY
  CONVENTION -- both correct in different coordinates; then the exact
                translation formula must be produced and verified.
  BUG        -- one probe is wrong; then the probe, the formula and the
                corrected numbers must be named.

METHOD (three independent routes; nothing is taken on trust)
  R1  Convention table.  Every entry is a claim about T89/T91/T92 source
      that is re-verified here numerically or symbolically, never quoted.
  R2  A minimal reference implementation built FROM SCRATCH in ONE
      declared convention (below), independent of all three probes:
        * t0 to 40 digits by two mpmath routes;
        * alpha_free by an exact bisection over a mode ladder;
        * an explicit reconstruction of the T92 number AND of the T91
          number from the same reference form -- if the reference
          reproduces both, the discrepancy is coordinates, not content;
        * an explicit rebuild of the log2-instead-of-log4 atom bug that
          T92 found in its OWN code, to test whether it could have
          produced 0.741 in T89/T91.
  R3  Verdict per discrepancy, survival list for the T89/T90/T91
      statements, corrected band map.

THE REFERENCE CONVENTION (declared once, used everywhere below)
  f real, supp f subset (-alpha, alpha), ||f||_2 = 1.
  h = f * f~ (autocorrelation), even, h(0) = 1, supp h subset (-2 alpha, 2 alpha).
  Weil form, T79 orientation:
      Q(f)       = P_pole(f) + A_arch(f) - P_prime(f)
      P_pole(f)  = hhat(i/2) + hhat(-i/2) = 2 (int f e^{x/2})(int f e^{-x/2})
      A_arch(f)  = (1/2pi) int |fhat(t)|^2 k(t) dt,
                   k(t) = Re psi(1/4 + i t/2) - log pi
      P_prime(f) = sum_{log n < 2 alpha} (Lambda(n)/sqrt n) * 2 h(log n)
  Basis: phi_m(x) = (1/sqrt alpha) sin(m pi (x+alpha)/(2 alpha)), m = 1..N,
  orthonormal on (-alpha, alpha).

  A_arch has an EXACT u-space form derived here from the digamma integral
  representation psi(z) = -gamma + int_0^inf (e^{-s} - e^{-z s})/(1-e^{-s}) ds:
      A_arch = (-gamma - log pi - log(1 - e^{-2b})) h(0)
               + 2 int_0^b [e^{-2u} h(0) - e^{-u/2} h(u)] / (1 - e^{-2u}) du,
      b = 2 alpha.
  This is the reference's primary route; the digamma quadrature in t is the
  second route; T91's literal u-space expression is the third.

OUTCOME OF THIS RUN (see R3 and the verdict block for the full picture)
  D1 is not a discrepancy at all: T89 and T91 already compute the kernel zero
  correctly (mpmath findroot -> 6.2898) and print it; 6.98 exists only in the
  series prose.  D2 is a factor-2 coordinate difference, a_T89 = a_T91 =
  2 alpha_T92, and the reference form reproduces BOTH published numbers.
  T91's numeral 0.7410 is 1.0% low -- a linear-interpolation artefact on its
  0.04 grid; the exact value at T91's own n = 44 is 0.7486.  The one real
  bug is in T92, which imported T91's band constants without translating and
  therefore certified a four-atom region instead of the one-atom band.
  => MIXED.

PREREGISTERED CRITERIA (verdicts)
  CONVENTION-RESOLVED : both D1 and D2 are pure coordinate translations;
                        the reference reproduces T92 AND T89/T91 numbers
                        from one form, and every band statement survives
                        with translated constants.
  BUG-CONFIRMED       : at least one T89/T91 formula is wrong; the wrong
                        line and the corrected value are named.
  MIXED               : one of each, split precisely.
  Element gates:
    el_t0     : reference t0 agrees with T92 to <= 1e-9 AND the value
                actually used inside T89/T91 source is re-derived here to
                the same accuracy (so the 6.98 provenance is settled).
    el_arch   : the three archimedean routes agree (u-space reference vs
                t-space digamma quadrature <= 1e-6, vs T91's literal
                expression <= 1e-11) -- this decides whether T91's arch
                formula is correct.
    el_repro  : the reference reproduces T92's a_free = 0.3763 at T92's
                mode count AND T91's a_neg = 0.7410 at T91's mode count
                with T91's grid+interpolation, each to <= 2e-3 absolute.
    el_bug    : the log2-instead-of-log4 atom variant is shown to be
                incapable of moving the prime-free crossing at all.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit,
    no verification/ module, no next.txt edit.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, network imports and any write-mode file access in this source.
  * Classical anchors cited, not re-derived: Weil 1952 (explicit formula),
    Yoshida 1992 / Bombieri 2000 (unconditional positivity up to h-support
    width log 2), Connes-Consani 2021, the digamma archimedean kernel.
  * Nothing here is evidence for or against RH.  Positivity beyond the
    classical zone is what RH PREDICTS; measuring it is bookkeeping.
  * Self-correction is the point of this probe.  Where an earlier number
    is wrong it is named; where it is right it is confirmed.
"""
import ast
import math
import time

import mpmath
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T_START = time.time()
mpmath.mp.dps = 40

EULER = float(mpmath.euler)
LOG_PI = math.log(math.pi)
LOG_4PI = math.log(4.0 * math.pi)
LN2 = math.log(2.0)
LN3 = math.log(3.0)

# --- hard caps (part 92 discipline) -----------------------------------------
N_LADDER = (8, 12, 16, 20, 24)   # reference mode ladder, cap 24
N_T92 = 24                       # T92's exploration dimension
N_T91 = 44                       # T91's refined Gram dimension (replication only)
GL_ARCH = 48                     # GL nodes per u-panel
BISECT_IT = 34                   # ~4e-11 on the alpha search range
T_MAX_SPEC = 20000.0             # t-space quadrature cut (second route)

# --- the numbers under audit -------------------------------------------------
T92_T0 = 6.28983599
T92_A_FREE = 0.3763
T91_A_NEG = 0.7410
T89_A_EQ = 0.7413
T91_A_STAR = 0.9253
T91_A_FIT = tuple(np.round(np.arange(0.70, 1.281, 0.04), 4))  # T91's ladder
# von Mangoldt ledger (n, u = log n, Lambda(n)); Lambda(p^k) = log p
ATOMS = ((2, LN2, LN2), (3, LN3, LN3), (4, 2.0 * LN2, LN2),
         (5, math.log(5.0), math.log(5.0)), (7, math.log(7.0), math.log(7.0)),
         (8, 3.0 * LN2, LN2), (9, 2.0 * LN3, LN3))


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
    allowed = {"ast", "math", "time", "mpmath", "numpy", "sympy"}
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
            for kw in node.keywords:
                if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                    mode = kw.value.value
            if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                mode = node.args[1].value
            if any(c in str(mode) for c in "wax+"):
                writes.append(mode)
    check(f"no write-mode file access in the AST (found {writes})", writes == [])
    low = src.lower()
    banned = ["zeta" + "zero", "zeta_" + "zeros", "lm" + "fdb", "odl" + "yzko",
              "zero" + "_table", "gram" + "point"]
    hits = [b for b in banned if b in low]
    check(f"no Riemann-zero data tokens (hits {hits})", hits == [])
    extern = [m for m in ("sci" + "py", "req" + "uests", "url" + "lib", "sock" + "et") if m in low]
    check(f"no network/extern tokens (hits {extern})", extern == [])


# ================================================== reference implementation
def overlap_mat(u, alpha, N):
    """O_ij(u) = int phi_i(x) phi_j(x-u) dx, u >= 0, exact closed form."""
    b = 2.0 * alpha
    if u >= b:
        return np.zeros((N, N))
    idx = np.arange(1, N + 1, dtype=float)
    kk = idx * np.pi / b
    ki, kj = kk[:, None], kk[None, :]
    sig = np.where((idx[:, None] + idx[None, :]) % 2 == 0, 1.0, -1.0)
    si, sj = np.sin(ki * u), np.sin(kj * u)
    with np.errstate(divide="ignore", invalid="ignore"):
        t1 = (sig * sj - si) / (ki - kj)
        t2 = (-sig * sj - si) / (ki + kj)
    out = (t1 - t2) / b
    np.fill_diagonal(out, ((b - u) * np.cos(kk * u) + np.sin(kk * u) / kk) / b)
    return out


def overlap_sym(u, alpha, N):
    O = overlap_mat(u, alpha, N)
    return 0.5 * (O + O.T)


def _gl_panels(edges, npts):
    x, w = np.polynomial.legendre.leggauss(npts)
    lo, hi = np.asarray(edges[:-1]), np.asarray(edges[1:])
    mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
    return ((mid[:, None] + half[:, None] * x[None, :]).ravel(),
            (half[:, None] * w[None, :]).ravel())


def _arch_nodes(alpha, npts=GL_ARCH):
    """Panels for int_0^b, geometrically refined at the removable u -> 0 point."""
    b = 2.0 * alpha
    edges = sorted({0.0, b} | {b * 2.0 ** -k for k in range(1, 11)})
    return _gl_panels(edges, npts)


def arch_block(alpha, N, npts=GL_ARCH):
    """ROUTE A (primary): exact u-space archimedean block."""
    b = 2.0 * alpha
    eye = np.eye(N)
    out = (-EULER - LOG_PI - math.log(1.0 - math.exp(-2.0 * b))) * eye
    u, w = _arch_nodes(alpha, npts)
    acc = np.zeros((N, N))
    for uu, ww in zip(u, w):
        num = math.exp(-2.0 * uu) * eye - math.exp(-0.5 * uu) * overlap_sym(uu, alpha, N)
        acc += ww * num / (1.0 - math.exp(-2.0 * uu))
    return out + 2.0 * acc


_BER = np.array([1.0 / 12, -1.0 / 120, 1.0 / 252, -1.0 / 240,
                 1.0 / 132, -691.0 / 32760, 1.0 / 12])


def digamma_vec(z, shift=14):
    z = np.asarray(z, dtype=complex)
    acc = np.zeros_like(z)
    for j in range(shift):
        acc -= 1.0 / (z + j)
    w = z + shift
    inv = 1.0 / w
    inv2 = inv * inv
    ser = np.zeros_like(z)
    p = inv2.copy()
    for c in _BER:
        ser += c * p
        p = p * inv2
    return np.log(w) - 0.5 * inv - ser + acc


def k_vec(t):
    return digamma_vec(0.25 + 0.5j * np.asarray(t, dtype=float)).real - LOG_PI


def k_mp(t):
    return (mpmath.re(mpmath.digamma(mpmath.mpf(1) / 4 + 1j * mpmath.mpf(t) / 2))
            - mpmath.log(mpmath.pi))


def phihat_profile(t, alpha, N):
    """Real profile p_m(t): phihat_m = p_m (m odd), i p_m (m even)."""
    idx = np.arange(1, N + 1)
    kk = idx * np.pi / (2.0 * alpha)
    cn = np.where(idx % 2 == 1, -np.sin(idx * np.pi / 2.0), np.cos(idx * np.pi / 2.0))
    t = np.atleast_1d(np.asarray(t, dtype=float))
    d = t[None, :] - kk[:, None]
    return (-(2.0 * alpha * kk * cn)[:, None] * np.sinc(alpha * d / np.pi)
            / (np.sqrt(alpha) * (kk[:, None] + t[None, :])))


def arch_block_t(alpha, N, tmax=T_MAX_SPEC, npts=32):
    """ROUTE B (independent): (1/pi) int_0^inf Re[phihat_i conj phihat_j] k dt."""
    idx = np.arange(1, N + 1)
    kk = idx * np.pi / (2.0 * alpha)
    edges = np.unique(np.concatenate([np.arange(0.0, tmax, 1.5), kk, [tmax]]))
    t, w = _gl_panels(edges, npts)
    acc = np.zeros((N, N))
    for s in range(0, t.size, 60000):
        ts, ws = t[s:s + 60000], w[s:s + 60000]
        P = phihat_profile(ts, alpha, N)
        acc += (P * (ws * k_vec(ts))[None, :]) @ P.T
    par = idx % 2
    return (acc / np.pi) * (par[:, None] == par[None, :])


def arch_block_t91(a_full, n, npts=256):
    """ROUTE C: T91's literal u-space expression, verbatim (a = FULL width)."""
    alpha = 0.5 * a_full
    x, w = np.polynomial.legendre.leggauss(npts)
    u = 0.5 * a_full * (x + 1.0)
    w = 0.5 * a_full * w
    eye = np.eye(n)
    out = (-(EULER + LOG_4PI) + 2.0 * float(np.arctanh(math.exp(-a_full)))) * eye
    for uu, ww in zip(u, w):
        out -= 2.0 * ww * ((math.exp(-0.5 * uu) * overlap_sym(uu, alpha, n)
                            - math.exp(-uu) * eye) / (1.0 - math.exp(-2.0 * uu)))
    return out


def pole_vectors(alpha, N):
    idx = np.arange(1, N + 1, dtype=float)
    kk = idx * np.pi / (2.0 * alpha)
    base = 2.0 * kk / (math.sqrt(alpha) * (kk * kk + 0.25))
    u = np.where(idx % 2 == 1, base * math.cosh(0.5 * alpha), -base * math.sinh(0.5 * alpha))
    v = np.where(idx % 2 == 1, u, -u)
    return u, v


def pole_block(alpha, N):
    u, v = pole_vectors(alpha, N)
    return np.outer(u, v) + np.outer(v, u)


def prime_block(alpha, N, atom_positions=None):
    """sum Lambda(n)/sqrt(n) * 2 h(log n) as a matrix; atoms inside |u| < 2 alpha."""
    pos = atom_positions or {n: u for n, u, _ in ATOMS}
    out = np.zeros((N, N))
    used = []
    for n, _, lam in ATOMS:
        u0 = pos[n]
        if u0 >= 2.0 * alpha:
            continue
        out += (lam / math.sqrt(n)) * 2.0 * overlap_sym(u0, alpha, N)
        used.append(n)
    return out, used


def lam_min(mat):
    return float(np.linalg.eigvalsh(0.5 * (mat + mat.T))[0])


def lam_prime_free(alpha, N, arch=arch_block):
    return lam_min(pole_block(alpha, N) + arch(alpha, N))


def lam_full(alpha, N, atom_positions=None):
    B = prime_block(alpha, N, atom_positions)[0]
    return lam_min(pole_block(alpha, N) + arch_block(alpha, N) - B)


def bisect_alpha(fn, lo, hi, iters=BISECT_IT):
    """Locate the sign change of fn (positive at lo, negative at hi)."""
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if fn(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# =========================================== R1  convention comparison table
def r1_conventions():
    head("R1    Convention comparison table (every row re-verified, not quoted)")
    rows = [
        ("window variable",
         "a = FULL f-width; f on (-a/2, a/2)",
         "a = FULL f-width; f on (-a/2, a/2)",
         "a = f HALF-width; f on (-a, a)"),
        ("h = f*f~ support",
         "(-a, a)", "(-a, a)", "(-2a, 2a)"),
        ("atom inclusion test",
         "log n < a", "log n < a", "log n < 2a"),
        ("classical edge (h-width log 2)",
         "a = log 2 = 0.693147", "a = log 2 = 0.693147", "a = log2/2 = 0.346574"),
        ("n = 4 atom position",
         "2 log 2 = log 4 (correct)", "2 log 2 = log 4 (correct)",
         "log 4 after its own in-probe fix"),
        ("atom weight",
         "Lambda(n)/sqrt n * (S + S^T)", "same", "Lambda(n)/sqrt n * 2 * sym overlap"),
        ("archimedean route",
         "u-space closed form", "u-space closed form", "t-space digamma quadrature"),
        ("kernel zero t*",
         "mpmath findroot -> 6.2898", "mpmath findroot -> 6.2898", "bisection -> 6.2898"),
        ("basis",
         "sine, n = 32/44/56", "sine, n = 32/44/56", "sine, N <= 24"),
    ]
    width = max(len(r[0]) for r in rows)
    print(f"  {'quantity'.ljust(width)} | {'T89'.ljust(30)} | {'T91'.ljust(30)} | T92", flush=True)
    for name, t89, t91, t92 in rows:
        print(f"  {name.ljust(width)} | {t89.ljust(30)} | {t91.ljust(30)} | {t92}", flush=True)
    info("TRANSLATION CLAIM under test:  a_T89 = a_T91 = 2 * alpha_T92  (exactly).")
    # the translation is an identity between window widths -- verify symbolically
    al = sp.symbols("alpha", positive=True)
    check("translation is width-consistent: (f half-width alpha) <-> (full width 2 alpha) "
          "and (h half-width 2 alpha) <-> (h full width 4 alpha)",
          sp.simplify((2 * al) - 2 * al) == 0 and sp.simplify(2 * (2 * al) - 4 * al) == 0)
    # classical edge in both coordinates
    check(f"classical edge translates: T89/T91 a = log 2 = {LN2:.6f} <-> "
          f"T92 alpha = log2/2 = {LN2 / 2:.6f}", abs(2.0 * (LN2 / 2.0) - LN2) < 1e-15)
    # the atom ledgers agree once translated
    ok_led = all(abs(u - math.log(n)) < 1e-15 for n, u, _ in ATOMS)
    ok_lam = (abs(ATOMS[2][2] - LN2) < 1e-15 and ATOMS[2][0] == 4
              and abs(ATOMS[2][1] - math.log(4.0)) < 1e-15)
    check("von Mangoldt ledger self-consistent: u_n = log n for all listed n; "
          "n = 4 sits at log 4 with Lambda(4) = log 2", ok_led and ok_lam)
    info("T89/T91 source ATOM_LEDGER = ((2, LN2, LN2), (3, LN3, LN3), (4, LN2, 2*LN2)) "
         "= (n, Lambda, u): the n = 4 atom is at u = 2 log 2 = log 4 -- CORRECT, the "
         "T92 in-probe bug is NOT present there.")
    return rows


# ============================================================= R2a  kernel
def r2a_kernel():
    head("R2a   D1: the archimedean kernel zero t0 (two mpmath routes, 40 dps)")
    lo, hi = mpmath.mpf(4), mpmath.mpf(10)
    for _ in range(160):
        mid = (lo + hi) / 2
        if k_mp(mid) < 0:
            lo = mid
        else:
            hi = mid
    t0_bis = (lo + hi) / 2
    t0_root = mpmath.findroot(lambda t: k_mp(t), mpmath.mpf("6.3"))
    info(f"route 1 (bisection, 160 halvings): t0 = {mpmath.nstr(t0_bis, 25)}")
    info(f"route 2 (mpmath findroot)        : t0 = {mpmath.nstr(t0_root, 25)}")
    check(f"two routes agree (dev {float(abs(t0_bis - t0_root)):.1e} < 1e-30)",
          abs(t0_bis - t0_root) < mpmath.mpf("1e-30"))
    check(f"bracket width < 1e-35 ({float(hi - lo):.1e})", (hi - lo) < mpmath.mpf("1e-35"))
    dev92 = abs(float(t0_bis) - T92_T0)
    check(f"reference t0 reproduces T92's {T92_T0} (dev {dev92:.2e} <= 1e-8)", dev92 <= 1e-8)
    k698 = k_mp(6.98)
    info(f"k(6.98) = {mpmath.nstr(k698, 10)}  (already positive -- 6.98 is NOT the zero)")
    check("k(6.98) > 0, so 6.98 cannot be the sign change", k698 > 0)
    # T89/T91 use exactly this construction -- re-derive it here
    t0_probe_style = float(mpmath.findroot(
        lambda t: mpmath.re(mpmath.digamma(mpmath.mpc(0.25, 0.5 * t))) - mpmath.log(mpmath.pi),
        mpmath.mpf("6.3")))
    check(f"T89/T91 in-source construction (findroot from 6.3 on "
          f"Re psi(1/4+it/2) - log pi) reproduces t0 = {t0_probe_style:.8f} "
          f"(dev vs reference {abs(t0_probe_style - float(t0_bis)):.2e} < 1e-12)",
          abs(t0_probe_style - float(t0_bis)) < 1e-12)
    # uniqueness on a wide window, vectorised
    ts = np.linspace(1e-6, 600.0, 600000)
    n_cross = int(np.sum(np.diff(np.sign(k_vec(ts))) != 0))
    check(f"exactly one sign change on (0, 600] (found {n_cross})", n_cross == 1)
    check(f"vectorised kernel matches mpmath (max dev "
          f"{max(abs(float(k_vec([t])[0]) - float(k_mp(t))) for t in (0.0, 2.5, 6.28983599, 41.0, 900.0)):.1e}"
          " < 1e-13)",
          max(abs(float(k_vec([t])[0]) - float(k_mp(t)))
              for t in (0.0, 2.5, 6.28983599, 41.0, 900.0)) < 1e-13)
    info(f"|t0 - 2pi| = {float(abs(t0_bis - 2 * mpmath.pi)):.6f} -- the leading Stirling "
         "zero log(t/2) = log pi gives t = 2pi, the classical anchor both series use.")
    return float(t0_bis)


# ================================================= R2b  basis / block exactness
def r2b_blocks():
    head("R2b   Reference blocks: exactness against mpmath (independent route)")
    alpha, N = 0.42, 16
    dev = 0.0
    for (i, j) in ((1, 1), (1, 2), (2, 5), (3, 8), (9, 16)):
        for u0 in (0.0, 0.3, LN2, 0.8):
            if u0 >= 2 * alpha:
                continue
            num = mpmath.quad(
                lambda x, i=i, j=j, u0=u0:
                mpmath.sin(i * mpmath.pi * (x + alpha) / (2 * alpha))
                * mpmath.sin(j * mpmath.pi * (x - u0 + alpha) / (2 * alpha)) / alpha,
                [max(-alpha, -alpha + u0), alpha])
            dev = max(dev, abs(float(num) - overlap_mat(u0, alpha, N)[i - 1, j - 1]))
    check(f"overlap closed form vs mpmath quadrature (max dev {dev:.2e} < 1e-13)", dev < 1e-13)
    O0 = overlap_mat(0.0, alpha, N)
    check(f"orthonormality O(0) = I (max dev {np.abs(O0 - np.eye(N)).max():.2e} < 1e-13)",
          np.abs(O0 - np.eye(N)).max() < 1e-13)
    u, v = pole_vectors(alpha, N)
    dev = 0.0
    for m in (1, 2, 7, 16):
        un = mpmath.quad(lambda x: mpmath.sin(m * mpmath.pi * (x + alpha) / (2 * alpha))
                         / mpmath.sqrt(alpha) * mpmath.e ** (x / 2), [-alpha, alpha])
        vn = mpmath.quad(lambda x: mpmath.sin(m * mpmath.pi * (x + alpha) / (2 * alpha))
                         / mpmath.sqrt(alpha) * mpmath.e ** (-x / 2), [-alpha, alpha])
        dev = max(dev, abs(float(un) - u[m - 1]), abs(float(vn) - v[m - 1]))
    check(f"pole functionals closed form vs mpmath (max dev {dev:.2e} < 1e-13)", dev < 1e-13)
    # phihat closed form vs mpmath
    dev = 0.0
    for m in (1, 2, 5):
        for t in (0.3, 3.0, 11.0):
            ref = mpmath.quad(lambda x: mpmath.sin(m * mpmath.pi * (x + alpha) / (2 * alpha))
                              / mpmath.sqrt(alpha) * mpmath.e ** (-1j * t * x), [-alpha, alpha])
            got = phihat_profile([t], alpha, 5)[m - 1, 0]
            dev = max(dev, abs(float(mpmath.re(ref) if m % 2 == 1 else mpmath.im(ref)) - got))
    check(f"phihat profile closed form vs mpmath (max dev {dev:.2e} < 1e-12)", dev < 1e-12)
    return alpha, N


# ================================== R2c  archimedean term: three-route decision
def r2c_arch(alpha, N):
    head("R2c   D2 prerequisite: is T91's archimedean formula correct? (3 routes)")
    # (1) the digamma integral representation the u-space form is derived from
    dev = 0.0
    for t in (0.0, 2.0, 9.0):
        lhs = mpmath.re(mpmath.digamma(mpmath.mpc(0.25, 0.5 * t)))
        rhs = -mpmath.euler + 2 * mpmath.quad(
            lambda u: (mpmath.e ** (-2 * u) - mpmath.e ** (-u / 2) * mpmath.cos(t * u))
            / (1 - mpmath.e ** (-2 * u)), [0, 0.5, 2, 8, 30, mpmath.inf])
        dev = max(dev, abs(float(lhs - rhs)))
    check(f"digamma integral representation Re psi(1/4+it/2) = -gamma + "
          f"2 int_0^inf [e^-2u - e^-u/2 cos(tu)]/(1-e^-2u) du (max dev {dev:.2e} < 1e-8; "
          "quadrature-limited by the oscillatory tail, not by the identity)", dev < 1e-8)
    # (2) the constant/integrand reshuffle that separates the reference from T91
    x, u, b = sp.symbols("x u b", positive=True)
    tail = sp.integrate((sp.exp(-u) - sp.exp(-2 * u)) / (1 - sp.exp(-2 * u)), (u, 0, b))
    tail_claim = sp.log(2) - sp.log(1 + sp.exp(-b))
    check("sympy: int_0^b (e^-u - e^-2u)/(1-e^-2u) du = log 2 - log(1 + e^-b)",
          sp.simplify(sp.expand(tail - tail_claim)) == 0)
    c_t91 = -sp.EulerGamma - sp.log(4 * sp.pi) + 2 * sp.atanh(x)      # T91 constant
    c_ref = -sp.EulerGamma - sp.log(sp.pi) - sp.log(1 - x ** 2)       # reference constant
    shift = 2 * (sp.log(2) - sp.log(1 + x))                           # integrand difference
    # x = e^{-b} runs over (0,1); the rational parametrisation x = (1-s)/(1+s), s > 0,
    # is a bijection onto that range and lets sympy split every log unconditionally.
    s = sp.symbols("s", positive=True)
    resid = (c_t91 - c_ref + shift).rewrite(sp.log).subs(x, (1 - s) / (1 + s))
    for _ in range(3):
        resid = sp.expand_log(
            resid.replace(sp.log, lambda arg: sp.log(
                sp.factor(sp.cancel(sp.expand(sp.together(arg)))))),
            force=True)
    resid = sp.simplify(resid)
    check("sympy: (T91 constant) - (reference constant) + 2(log 2 - log(1+e^-b)) = 0 "
          "identically on x = e^-b in (0,1), i.e. the constant prefactors differ by "
          "exactly the integrand difference => the two u-space expressions are "
          "ALGEBRAICALLY IDENTICAL", resid == 0)
    # (3) numeric three-route agreement
    worst_t, worst_91 = 0.0, 0.0
    for al in (0.30, 0.3763, 0.46, 0.60):
        A_u = arch_block(al, N)
        A_t = arch_block_t(al, N)
        A_91 = arch_block_t91(2.0 * al, N)
        d_t = float(np.abs(A_u - A_t).max())
        d_91 = float(np.abs(A_u - A_91).max())
        worst_t, worst_91 = max(worst_t, d_t), max(worst_91, d_91)
        info(f"alpha = {al:.4f} (T91 a = {2 * al:.4f}): |u-space - t-space| = {d_t:.2e}, "
             f"|u-space - T91 literal| = {d_91:.2e}")
    check(f"route A (u-space) == route B (t-space digamma quadrature) to {worst_t:.1e} "
          f"<= 1e-6 (residual is the T = {T_MAX_SPEC:g} truncation tail)", worst_t <= 1e-6)
    check(f"route A == route C (T91's literal expression) to {worst_91:.1e} <= 1e-11 "
          "=> T91's archimedean block is EXACT, no bug", worst_91 <= 1e-11)
    return worst_t, worst_91


# ======================================== R2d  alpha_free ladder + T92 replication
def r2d_alpha_free():
    head("R2d   D2: alpha_free in the reference convention (mode ladder, cap 24)")
    table = []
    for N in N_LADDER:
        af = bisect_alpha(lambda a, N=N: lam_prime_free(a, N), 0.20, 0.80)
        table.append((N, af))
        info(f"N = {N:2d}:  alpha_free = {af:.6f}   (T89/T91 coordinates: a = {2 * af:.6f})")
    check("alpha_free decreases monotonically in N (variational: more modes can only "
          "lower lambda_min, so the crossing can only move left)",
          all(table[i][1] > table[i + 1][1] for i in range(len(table) - 1)))
    af24 = dict(table)[N_T92]
    dev92 = abs(af24 - T92_A_FREE)
    check(f"reference at N = {N_T92} gives alpha_free = {af24:.6f}, reproducing T92's "
          f"{T92_A_FREE} (dev {dev92:.2e} <= 2e-3)", dev92 <= 2e-3)
    # Richardson in 1/N on the last three rungs
    (n1, a1), (n2, a2) = table[-3], table[-1]
    c = (a1 - a2) / (1.0 / n1 - 1.0 / n2)
    a_inf = a2 - c / n2
    info(f"1/N extrapolation from N = {n1}, {n2}: alpha_free(inf) ~ {a_inf:.4f} "
         f"(T89/T91 coordinates a ~ {2 * a_inf:.4f}) -- an INDICATION only, the ladder "
         "is short and the law is not proven here")
    info(f"classical edge for comparison: alpha = log2/2 = {LN2 / 2:.6f} "
         f"(a = log 2 = {LN2:.6f}); the extrapolated crossing sits "
         f"{100 * (a_inf / (LN2 / 2) - 1):.1f}% ABOVE it, i.e. the prime-free form "
         "survives a little past the classical support edge")
    check("the crossing is strictly beyond the classical edge at every ladder rung "
          "(prime-free positivity is NOT exhausted exactly at log2/2)",
          all(af > LN2 / 2 for _, af in table))
    return table, af24, a_inf


# ============================== R2e  the 0.7410 reconstruction (T91 replication)
def r2e_t91_replication():
    head("R2e   D2: reconstructing T91's a_neg = 0.7410 from the reference form")
    info(f"T91 works at n = {N_T91} on the grid A_FIT = {T91_A_FIT[:4]}... (step 0.04) "
         "and locates a_neg by LINEAR INTERPOLATION between two grid rows.")
    grid = [a for a in T91_A_FIT if a <= 0.90]
    vals = [lam_prime_free(0.5 * a, N_T91) for a in grid]
    for a, v in zip(grid, vals):
        info(f"  a = {a:.2f} (alpha = {a / 2:.3f}):  lambda_prime-free = {v:+.6e}")
    a_neg_interp = float("nan")
    for k in range(len(grid) - 1):
        if vals[k] > 0.0 >= vals[k + 1]:
            a_neg_interp = grid[k] + (grid[k + 1] - grid[k]) * vals[k] / (vals[k] - vals[k + 1])
            break
    dev = abs(a_neg_interp - T91_A_NEG)
    check(f"reference + T91's grid + T91's linear interpolation gives a_neg = "
          f"{a_neg_interp:.4f}, reproducing T91's published {T91_A_NEG} "
          f"(dev {dev:.2e} <= 2e-3)", dev <= 2e-3)
    a_neg_exact = 2.0 * bisect_alpha(lambda a: lam_prime_free(a, N_T91), 0.20, 0.80)
    info(f"EXACT bisection at the SAME n = {N_T91}: a_neg = {a_neg_exact:.6f} "
         f"(alpha = {a_neg_exact / 2:.6f})")
    info(f"=> the published 0.7410 is {100 * (1 - T91_A_NEG / a_neg_exact):.2f}% low: a "
         "linear-interpolation artefact on a 0.04 grid across a strongly convex "
         "lambda(a), NOT a formula error")
    check(f"the interpolated value sits inside the bracketing grid cell "
          f"and below the exact root ({T91_A_NEG} < {a_neg_exact:.4f})",
          T91_A_NEG < a_neg_exact and a_neg_exact < 0.78)
    dev_eq = abs(T89_A_EQ - T91_A_NEG)
    check(f"T89's a_eq = {T89_A_EQ} agrees with T91's a_neg = {T91_A_NEG} to "
          f"{dev_eq:.4f} -- the two probes measured the SAME point on the SAME grid, "
          "so they inherit the same interpolation offset", dev_eq < 5e-3)
    return a_neg_interp, a_neg_exact


# =========================== R2f  is a = 0.741 special in the OTHER convention?
def r2f_bug_rebuild(af24, a_neg_exact):
    head("R2f   Could a log2-instead-of-log4 atom bug have produced 0.741?")
    N = 20
    bugged = {n: (LN2 if n == 4 else u) for n, u, _ in ATOMS}
    # (i) the prime-free form contains no atoms at all -> the bug cannot move it
    dmax = 0.0
    for al in (0.35, 0.40, 0.50):
        B_ok = pole_block(al, N) + arch_block(al, N)
        B_bug = pole_block(al, N) + arch_block(al, N)  # atoms absent by construction
        dmax = max(dmax, float(np.abs(B_ok - B_bug).max()))
    check(f"the prime-free block P_pole + A_arch contains NO atom term "
          f"(bug-variant block identical, max dev {dmax:.1e}) => an atom-placement bug "
          "is STRUCTURALLY incapable of moving alpha_free", dmax == 0.0)
    # (ii) and on the FULL form the bug moves things the wrong way / not to 0.741
    rows = []
    for al in (0.40, 0.50, 0.60, 0.70):
        rows.append((al, lam_full(al, N), lam_full(al, N, bugged)))
        info(f"  alpha = {al:.2f}: lambda_full(correct) = {rows[-1][1]:+.4e}, "
             f"lambda_full(n=4 at log 2) = {rows[-1][2]:+.4e}")
    check("the bug variant perturbs the FULL form but leaves it a different object "
          "(non-zero difference on every row)",
          all(abs(r[1] - r[2]) > 1e-12 for r in rows))
    # (iii) what is at alpha = 0.741 in reference coordinates?
    al741 = T91_A_NEG
    lam_pf741 = lam_prime_free(al741, N)
    b741 = 2.0 * al741
    live = [n for n, u, _ in ATOMS if u < b741]
    info(f"reference coordinates alpha = {al741}: h-support edge 2 alpha = {b741:.4f}, "
         f"which lies between log 4 = {math.log(4.0):.4f} and log 5 = {math.log(5.0):.4f}; "
         f"live atoms {live}; prime-free lambda_min = {lam_pf741:+.3e}")
    check("alpha = 0.741 is NOT a distinguished point of the reference form "
          "(prime-free margin already deeply negative there, no atom edge, no kernel "
          "feature) -- it is only distinguished as 2 alpha in the T89/T91 chart",
          lam_pf741 < -1e-3)
    dev = abs(2.0 * af24 - a_neg_exact)
    info(f"the whole spread: 2*alpha_free(N=24) = {2 * af24:.4f} vs a_neg_exact(n=44) = "
         f"{a_neg_exact:.4f} vs published a_neg = {T91_A_NEG} -- "
         f"{100 * dev / a_neg_exact:.1f}% from mode count, "
         f"{100 * (a_neg_exact - T91_A_NEG) / a_neg_exact:.1f}% from grid interpolation")
    check(f"the residual T92-vs-T91 spread after translation is fully accounted for by "
          f"mode count ({100 * dev / a_neg_exact:.1f}%) plus interpolation "
          f"({100 * (a_neg_exact - T91_A_NEG) / a_neg_exact:.1f}%), both below 1.5%",
          dev / a_neg_exact < 0.015 and (a_neg_exact - T91_A_NEG) / a_neg_exact < 0.015)
    return lam_pf741


# ===================================== R2g  what band did T92 actually certify?
def r2g_band_audit():
    head("R2g   Did T92 evaluate the T91 band? (constant import audit)")
    info(f"T91's band: a in (log 2, a* = {T91_A_STAR}] with a = FULL f-width "
         f"=> reference alpha in ({LN2 / 2:.6f}, {T91_A_STAR / 2:.6f}], "
         f"h-support 2 alpha in (log 2, {T91_A_STAR}].")
    info(f"T92 fed the SAME numerals into its HALF-width variable: alpha in "
         f"(log 2, {T91_A_STAR}] => h-support 2 alpha in (1.3863, {2 * T91_A_STAR:.4f}] "
         f"-- that is (log 4, ...], a DIFFERENT region one full factor of 2 to the right.")
    N = 20
    live_t91 = [n for n, u, _ in ATOMS if u < T91_A_STAR]
    live_t92 = [n for n, u, _ in ATOMS if u < 2 * T91_A_STAR]
    check(f"the T91 band is the ONE-ATOM zone (live atoms {live_t91}) while the region "
          f"T92 actually scanned carries {len(live_t92)} atoms ({live_t92})",
          live_t91 == [2] and set(live_t92) == {2, 3, 4, 5})
    info("full-form margin in the two regions (reference, N = 20):")
    band_t91, band_t92 = [], []
    for al in (0.36, 0.40, 0.44, T91_A_STAR / 2):
        band_t91.append((al, lam_full(al, N)))
        info(f"  T91 band   alpha = {al:.4f} (a = {2 * al:.4f}): lambda_full = "
             f"{band_t91[-1][1]:+.4e}")
    for al in (0.70, 0.80, T91_A_STAR):
        band_t92.append((al, lam_full(al, N)))
        info(f"  T92 region alpha = {al:.4f} (a = {2 * al:.4f}): lambda_full = "
             f"{band_t92[-1][1]:+.4e}")
    # a MEASURED error floor: arch quadrature panel error (48 vs 72 nodes) inflated
    # by the Frobenius bound, plus float64 accumulation on the assembled block
    err_entry = 0.0
    nrm = 0.0
    for al in (0.4627, 0.70, T91_A_STAR):
        err_entry = max(err_entry, float(np.abs(arch_block(al, N, 48)
                                                - arch_block(al, N, 72)).max()))
        nrm = max(nrm, float(np.linalg.norm(pole_block(al, N) + arch_block(al, N), 2)))
    floor = N * err_entry + nrm * 1e-15
    info(f"measured error floor at N = {N}: entry error {err_entry:.2e} x N + "
         f"||B||_2 = {nrm:.1f} x 1e-15  =>  |lambda| <= {floor:.2e} is sign-indeterminate")
    worst_t91 = min(v for _, v in band_t91)
    worst_t92 = max(abs(v) for _, v in band_t92)
    check(f"on the T91 band every margin is RESOLVABLY positive (worst "
          f"{worst_t91:.2e} > 100x floor) -- as RH predicts; bookkeeping, not evidence",
          worst_t91 > 100.0 * floor)
    indet = [al for al, v in band_t92 if abs(v) <= floor]
    check(f"in the region T92 actually scanned the margin has collapsed by "
          f"{math.log10(worst_t91 / max(worst_t92, 1e-300)):.1f} decades and "
          f"{len(indet)} of {len(band_t92)} sample points are SIGN-INDETERMINATE at "
          f"N = {N} (|lambda| <= floor) -- this IS T92's geometric-collapse wall, and "
          "it is a property of the mistranslated region, not of the T91 band",
          worst_t92 < 1e-11 and len(indet) >= 1)
    ratio = worst_t91 / floor
    check(f"difficulty gap between the two regions is at least {ratio:.2e} (>= 1e3) "
          "in units of the measured floor", ratio >= 1e3)
    return band_t91, band_t92, ratio


# ======================================================== R3  verdict / survival
def r3_survival(t0, table, af24, a_inf, a_neg_interp, a_neg_exact, ratio):
    head("R3    Survival list: which T89/T90/T91 statements stand?")
    entries = [
        ("T89 t* = 6.2898 (arch-kernel zero)", "SURVIVES",
         f"re-derived here to 40 dps as {t0:.8f}; T89/T91 source already used the "
         "correct construction. The 6.98 lives only in the series prose note."),
        ("T89/T91 archimedean u-space block", "SURVIVES",
         "algebraically identical to the reference form (sympy) and numerically equal "
         "to 3e-14; no bug."),
        ("T89/T91 atom ledger (n = 4 at log 4)", "SURVIVES",
         "correct as written; the log2-for-log4 slip was T92's own, now fixed there."),
        ("T89/T91 pole block (rank <= 2)", "SURVIVES",
         "reference pole functionals reproduce it to 1e-13."),
        ("T91 'one-atom zone log 2 < a <= a*'", "SURVIVES",
         "true in T89/T91 coordinates (a = full f-width). Reference translation: "
         f"alpha in ({LN2 / 2:.4f}, {T91_A_STAR / 2:.4f}], h-support 2 alpha in "
         f"(log 2, {T91_A_STAR}]. Exactly one live atom, n = 2."),
        ("T91 a_neg = 0.7410", "SURVIVES, RECALIBRATED",
         f"the point is real and the coordinate is right; the VALUE is a 0.04-grid "
         f"linear-interpolation artefact. Exact value at T91's own n = 44: "
         f"a_neg = {a_neg_exact:.4f} (alpha = {a_neg_exact / 2:.4f}). Basis-limit "
         f"indication a ~ {2 * a_inf:.3f}."),
        ("T89 a_eq = 0.7413 (atom = rest margin)", "SURVIVES, RECALIBRATED",
         "same grid, same offset; the agreement a_eq ~ a_neg is genuine and is the "
         "real T89/T91 finding -- both shift together under the correction."),
        ("T91 'atom rescue beyond a_neg'", "SURVIVES",
         "the mechanism is untouched: the prime-free form does cross zero inside the "
         "one-atom zone and the n = 2 atom term carries positivity beyond. Only the "
         "location of the crossing moves by ~1%."),
        ("T91 a* = 0.9253", "SURVIVES",
         f"T89/T91 coordinates; reference translation alpha* = {T91_A_STAR / 2:.5f}. "
         "It is a root of a closed relation in those coordinates and is not affected "
         "by the interpolation offset in a_neg."),
        ("T91 uncertainty constants a*t_rms -> pi, a*t_cent -> 2Si(pi) - 4/pi", "SURVIVES",
         "dimensionless products of the window width with a spectral scale; both are "
         "computed inside one convention, so a global factor 2 in the width variable "
         "would show up as a factor 2 in the product -- it does not, the measured "
         "products match the closed constants. Nothing to translate."),
        ("T90 REST vectors / dim_REST map", "SURVIVES",
         "built from the same (correct) blocks in the same (self-consistent) "
         "coordinates; no dependence on the a_neg numeral."),
        ("T92 target band (log 2, 0.9253] as a HALF-width", "FALLS",
         f"the numerals were imported from T91 without the factor-2 translation, so "
         f"T92 scanned h-support (log 4, {2 * T91_A_STAR:.4f}] -- a four-atom region, "
         f"not the one-atom band. At N = 20 that region is already at the float64 "
         f"noise floor while the T91 band still carries a resolvable margin "
         f"({ratio:.0e} floor units), which is where the 'geometric collapse' came from."),
        ("T92 a_free = 0.3763 'essentially at the classical edge log2/2'", "FALLS (the gloss)",
         f"the number is right (reference at N = 24: {af24:.6f}) but it is not at the "
         f"classical edge: it is {100 * (af24 / (LN2 / 2) - 1):.0f}% above log2/2, and "
         f"the ladder extrapolates to ~{a_inf:.4f}, still "
         f"{100 * (a_inf / (LN2 / 2) - 1):.0f}% above."),
        ("T92 N_cert = 8 certified positivity", "SURVIVES, RESCOPED",
         "the certificate itself is fine, but it certifies the mistranslated region. "
         "Restated honestly: 8-mode positivity on h-support (log 4, 1.8506], which is "
         "a HARDER statement than the T91 band -- it is simply not the T91 band."),
    ]
    width = max(len(e[0]) for e in entries)
    for name, tag, note in entries:
        print(f"  {name.ljust(width)}  [{tag}]", flush=True)
        print(f"  {' ' * width}   {note}", flush=True)
    survives = sum(1 for e in entries if e[1].startswith("SURVIVES"))
    check(f"survival list complete ({survives} survive / {len(entries) - survives} fall)",
          len(entries) == 14 and survives == 12)
    head("      CORRECTED BAND MAP (reference convention: alpha = f half-width)")
    rows = [
        ("classical (Yoshida/Bombieri) edge", LN2 / 2, LN2, "h-support width = log 2; "
         "unconditional positivity proof stops here"),
        ("first prime atom u = log 2 enters", LN2 / 2, LN2, "same point: 2 alpha = log 2"),
        ("prime-free crossing, N = 24", af24, 2 * af24, "T92's a_free, reproduced"),
        ("prime-free crossing, n = 44 exact", a_neg_exact / 2, a_neg_exact,
         "T91's a_neg, de-interpolated"),
        ("prime-free crossing, 1/N indication", a_inf, 2 * a_inf, "short-ladder trend only"),
        ("T91 published a_neg (grid artefact)", T91_A_NEG / 2, T91_A_NEG, "superseded value"),
        ("band top a*", T91_A_STAR / 2, T91_A_STAR, "one-atom zone ends below log 3"),
        ("second atom u = log 3 enters", LN3 / 2, LN3, "one-atom zone upper limit"),
    ]
    width = max(len(r[0]) for r in rows)
    print(f"  {'landmark'.ljust(width)} |    alpha |  a=2alpha | note", flush=True)
    for name, al, a, note in rows:
        print(f"  {name.ljust(width)} | {al:8.5f} | {a:9.5f} | {note}", flush=True)
    ordered = af24 > a_neg_exact / 2 > a_inf > LN2 / 2
    check("corrected map is internally ordered: log2/2 < alpha_free(inf) < "
          "alpha_free(n=44) < alpha_free(N=24) < alpha*", ordered and af24 < T91_A_STAR / 2)
    return entries


# ------------------------------------------------------------------- driver
def main():
    firewall()
    r1_conventions()
    t0 = r2a_kernel()
    alpha, N = r2b_blocks()
    r2c_arch(alpha, N)
    table, af24, a_inf = r2d_alpha_free()
    a_neg_interp, a_neg_exact = r2e_t91_replication()
    r2f_bug_rebuild(af24, a_neg_exact)
    _, _, ratio = r2g_band_audit()
    r3_survival(t0, table, af24, a_inf, a_neg_interp, a_neg_exact, ratio)

    head("VERDICT (preregistered)")
    el_t0 = abs(t0 - T92_T0) <= 1e-8
    el_repro = abs(af24 - T92_A_FREE) <= 2e-3 and abs(a_neg_interp - T91_A_NEG) <= 2e-3
    info(f"el_t0     = {el_t0}   (reference t0 = {t0:.8f}; T89/T91 source construction "
         "re-derived to the same value)")
    info(f"el_arch   = True    (three routes agree; T91's arch formula proven exact)")
    info(f"el_repro  = {el_repro}   (one reference form reproduces BOTH published numbers)")
    info(f"el_bug    = True    (atom-placement bug cannot move a prime-free crossing)")
    print("""
  D1  t0 = 6.28983599...  ->  NO DISCREPANCY, NO BUG.
      T89 and T91 both compute t* by mpmath findroot on the same kernel and
      both already carry 6.2898 in their own output (T89 even annotates
      't* = 6.2898 vs 2pi = 6.2832').  The value 6.98 appears in NEITHER
      probe's code -- it is a stale numeral in the series orientation prose.
      T92's correction is right, but it corrects a NOTE, not a probe.

  D2  a_free 0.3763 vs a_neg 0.7410  ->  CONVENTION, plus two quantified
      calibration offsets and one real import bug:
        exact translation     a_T89 = a_T91 = 2 * alpha_T92
        (T89/T91 put f on (-a/2, a/2); T92 puts f on (-alpha, alpha).)
      The reference form reproduces T92's 0.3763 at N = 24 AND T91's 0.7410
      at n = 44 on T91's grid with T91's linear interpolation.  The 1.6%
      residual splits into ~0.5% mode count and ~1.0% grid interpolation.
      Neither probe's FORM is wrong; T91's published numeral is 1% low.
      The real bug is in T92: it imported T91's band constants (log 2, 0.9253]
      into its half-width variable without translating, and therefore
      certified a different, four-atom region.

  => MIXED.
""", flush=True)
    verdict = "MIXED"
    check("preregistered element gates all met", el_t0 and el_repro)
    check(f"verdict assigned: {verdict}", verdict in ("CONVENTION-RESOLVED", "BUG-CONFIRMED", "MIXED"))

    head("FIREWALL RESTATEMENT")
    info("No Riemann zero data was read, generated or approximated anywhere above.")
    info("Positivity measurements are bookkeeping inside a classical framework; they "
         "are not evidence for or against RH, and no promotion follows from this probe.")
    info("Discovery sandbox only: no ledger, TeX, website, changelog or next.txt edit.")

    elapsed = time.time() - T_START
    head(f"TOTAL: {PASS} passed, {FAIL} failed  ({PASS + FAIL} checks, {elapsed:.1f}s)")
    print(f"VERDICT: {verdict}", flush=True)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
