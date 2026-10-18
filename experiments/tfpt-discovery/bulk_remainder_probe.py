r"""Discovery probe (2026-07-26), part 100 of the zeta/prime investigation.
Contract BULK.REMAINDER -- the ONE named obstruction of the T99 staircase
induction, attacked head on.

T99 left the recursive chain in this state: the induction step of zone k is the
operator statement

    W  <=  A_sh := Q|E_- + (mu_k/2) I ,   W = Q_-0 (Q|E_0)^{-1} Q_0- ,
    rho := lam_max(A_sh^{-1/2} W A_sh^{-1/2})  <=  1 ,

it splits by the exact parity selection rule into two decoupled channels, and it
is bounded by splitting the SMALLER WINDOW's spectrum at a threshold Lam:

    rho  <=  ||Z_Lam||_op^2  +  R_G / Lam            (T99 family, "B_rk")
             \____________/    \______/
              1..16 explicit    UNIFORM BULK REMAINDER
              modes below Lam   R_G/lam_top = 0.04..0.19 at its floor

The remainder is what fails: it exceeds the true slack 1 - rho (which falls to
1e-3) on the upper part of zones n=3,4,5, and the bound closes at EXACTLY the
samples where rho <= 1 - R_G/lam_top -- optimal inside its family, and the
family is the problem.  Zone-top margins are +1.4e-2..+2.7e-2 in zones 2-4 and
0 in zone 5.

WHAT THIS PROBE ADDS
  C1  CERTIFY.  The remainder R_G/lam_top is built from two objects of very
      different quality.  lam_top = lam_max(Q|E_0) is NOT a continuum quantity:
      the archimedean symbol grows like k(t) ~ log(t/2pi), so lam_top diverges
      like log(1/d) and drifts 10.8% over nested grids.  The chain is therefore
      re-indexed by a FIXED continuum threshold Lam (which T99's B_rk already
      is -- the drift lives only in the FLOOR statement R_G/lam_top, and this
      probe separates the two).  R_G itself is then certified in four explicit
      stages, each classical:
        S1  lam_min(A_sh) >= lam_A^cert, CLOSED FORM, from
            (a) the T98 nu-measure identity: for a wing pair of width
                delta < u the autocorrelation h(u) vanishes, so
                d nu_- = (1 - cos(tu)) |phihat_L|^2 dt / 2pi is a PROBABILITY
                measure and A_arch|E_- = int k d nu_- is an AVERAGE of k;
            (b) two certified caps on that measure -- Parseval
                (nu[-T,T] <= max_{|t|<=T}(1-cos(tu))), Cauchy-Schwarz/Bessel
                (|phihat|^2 <= delta, giving nu[-T,T] <= (delta/pi)(T -
                sin(Tu)/u)) and the Slepian-Pollak-Landau concentration
                eigenvalue lam_0(T delta/2) -- plus monotonicity of
                k(t) = Re psi(1/4 + it/2) - log pi in |t|, which turns the
                minimisation into an exact greedy water-filling;
            (c) the T98 closed forms ||a_I|| ||b_I|| = 2 sinh(delta/2),
                <a_I,b_I> = delta, giving
                P_pole|E_- >= -(cosh(u/2)-1)(2 sinh(delta/2) + delta) exactly;
            (d) the old-atom identity h_f(u_j) = -h_L(u-u_j)/2 on E_- (the
                diagonal autocorrelations vanish because delta < log 2 in every
                zone), so old atoms touch E_- ONLY where u_k - u_j < delta --
                which happens in the top third of zone 5 and nowhere else.
        S2  ||Q_0-||_op <= G_cert by the Schur test sqrt(||.||_1 ||.||_inf),
            a row-sum object that converges to int |K| and is grid-stable,
            unlike lam_max(Q|E_-) which diverges.
        S3  bulk resolvent: P_{>=Lam} Q_00^{-1} P_{>=Lam} <= (1/Lam) P_{>=Lam}
            -- exact spectral calculus.
        S4  coupling mass above Lam: ||P_{>=Lam} Q_0- x||^2 <= ||Q_0- x||^2
            -- Bessel.  This is the stage that S1 of the sharpening replaces.
      Chain:  rho <= ||Z_Lam||^2 + R_G^cert / Lam,  R_G^cert = G_cert^2/lam_A^cert.
  C2  SHARPEN.  Three levers, all fit-free operator inequalities.
      L1  TAIL PROJECTION (the main one).  S4 throws away the induction data a
          second time.  Keep it:
              W = sum_{lam_j<Lam} lam_j^{-1} g_j g_j^T + sum_{lam_j>=Lam} ...
                <= L_Lam + (1/Lam) (G^T G - S_Lam),   S_Lam = sum_{j<Lam} g_jg_j^T
          The bulk operator is now G^T G - S_Lam, built from the SAME two inputs
          the T99 chain already needs (the delta-local defect Gram G^T G and the
          modes below Lam) -- no new object.  Its top eigenvalue is the DEFECT
          TAIL FUNCTION m(Lam), and the remainder becomes m(Lam)/Lam instead of
          R_G/Lam.  Because the bulk term is no longer a multiple of the
          identity, the joint Rayleigh quotient lam_max(L + T/Lam) is also
          strictly better than lam_max(L) + lam_max(T)/Lam.
      L2  BANDING.  Above Lam, geometric bands Lam_0 < Lam_1 < ... with
          w_j = 1/Lam_{band(j)} >= 1/lam_j.  B bands with ratio r bound the
          whole bulk by r * (its exact value), so B ~ log(lam_top/Lam_0)/s
          bands suffice for slack s -- and BANDS ARE CONTINUUM OBJECTS while
          mode counts are not.  This is the drift-free form of the remainder.
      L3  PARITY IN THE BULK.  The bulk couples only to the OPPOSITE-parity
          spectrum of the smaller window; the parity-blind remainder is measured
          against the parity-resolved one to price that gain.
      Separately reported as MEASURED (not certified): the true bulk resolvent
      gain Lam * (exact bulk / tail mass), i.e. the fit-free form of the T99
      decay exponent theta.
  C3  THE CLOSURE MAP REDONE, per zone, with mode counts, band counts and grid
      stability of both -- and the zone-5 top typed as a limit case: is the
      saturation D_k(alpha_top) = mu_k/2 a SIMPLE degeneracy (one null direction,
      the rest of the spectrum bounded away), which is a Fredholm-alternative
      shaped statement, or is it structurally hard?
  C4  SYNTHESIS -- the induction skeleton with per-brick status and the honest
      remainder list.

PREREGISTERED VERDICTS
  REMAINDER-CLOSES-ZONES : zones 2-4 fully closed by the certified + sharpened
                           chain with grid-stable data, zone-5 top typed.
  REMAINDER-SHARPENED    : a factor is won and the map improves -- with the
                           part that still fails named.
  REMAINDER-STUCK        : the levers do not bite; why.
  Element gates: el_firewall, el_kernel, el_forms, el_cert, el_sharp, el_band,
  el_parity, el_map, el_top, el_budget.

OUTCOME OF THIS RUN  =>  REMAINDER-CLOSES-ZONES
  27 checks, 0 failures, 39 s, largest array 1900^2.
  C1  The 10.8% drift is located: the CHAIN is already threshold-indexed and
      drift-free; the drift lives entirely in the FLOOR STATEMENT R_G/lam_top.
      lam_top rises with a log(1/d) slope of +0.91..+1.05 over three nested
      grids (9.4%..10.8%), exactly as k(t) ~ log(t/2pi) demands -- so
      R_G/lam_top is a grid artefact and never was a continuum floor.  At a
      fixed Lam = 3 the objects the chain actually needs drift <= 5.7%
      (N(Lam)) and <= 9.9% (m(Lam)), and R_G itself <= 0.3%.  The closed-form
      certificate gives lam_A^cert <= lam_min(A_sh) at 16/16 samples and is
      NON-VACUOUS at 13/16: the whole of zones 3 and 4, the lower 3/4 of zone
      2 and the lower half of zone 5.  It goes vacuous at the tops, where the
      wing is wide, the nu-measure may keep low-frequency mass and k(0) =
      -5.372 dominates.  Where it holds, R_G^cert = G_cert^2/lam_A^cert
      overshoots the measured R_G by 7x..70x; the Schur test overshoots
      ||Q_0-||_op by only 1.0x..2.9x, so the loss is in lam_A, not in G.
  C2  ONE lever carries everything: the Bessel step ||P_{>=Lam}Gx||^2 <=
      ||Gx||^2 discards the induction data a second time.  Keeping it turns
      the remainder R_G/Lam into m(Lam)/Lam and wins 1.7x..68.9x at fixed
      thresholds Lam = 2/4/6 -- with NO new object: m(Lam) is built from the
      delta-local Gram G^T G and the modes below Lam, the same two inputs the
      T99 chain already needs.  The family is COMPLETE (b_tail -> rho exactly
      at Lam = lam_top).  The other levers are priced honestly: banding
      converts the cost into two CONTINUUM numbers (Lam_0, B) and closes
      24/24 with Lam_0 = 2 and B = 4..16; parity costs the bound nothing at
      all (rho_blind = max over channels to 1e-12) and only halves the data;
      and the measured bulk resolvent gain is 0.57..0.99, i.e. the certified
      1/Lam step is already tight and the T99 decay exponent theta has no
      further factor to give.  The defect tail falls only like m ~ Lam^-p
      with p = 0.50..1.17 (R2 = 0.81..0.94): the extension defect couples
      mainly to the BULK of the smaller window, which is why a large Lam is
      needed wherever the true slack is 1e-3.
  C3  Closure goes from 11/24 samples (T99) to 24/24, zone by zone 6/6 in all
      four, with the induction datum 'all modes below Lam_ok = 0.47..2.80'.
      Lam_ok is the continuum statement and drifts 0.5%..9.7% over three
      grids while its mode-count shadow drifts up to 22% -- so the correct
      form of the hypothesis is a THRESHOLD, not a mode count.  A NEW caveat
      over T99: the channel with the largest D_k is not always the channel
      with the largest rho (rho binds odd at 2/24 samples), and the operator
      target needs rho <= 1 in both, so every bound here is a max over the
      two channels.  The zone tops: the bottom eigenvalue of A_sh - W is
      SIMPLE at every sample (gap 0.004..0.324), the null direction is stable
      (participation ratio 0.56..0.94 of the wing), and the zone-5 margin
      falls to 6.7e-4 against >= 1.8e-2 in zones 2-4.  The limit point
      delta -> delta_max of zone 5 therefore cannot be reached by ANY bound
      with a strictly positive remainder; what it needs is an EQUALITY
      argument of Fredholm-alternative shape.

FENCES
  * Discovery sandbox.  No promotion, no ledger/TeX/website/changelog edit, no
    verification/ module, no next.txt edit, no .md output.
  * NO Riemann zero data of any kind; the AST firewall rejects zero-table
    tokens, network imports and write-mode file access in this source.
  * RH => window Weil positivity; the converse is NOT claimed.  A negative
    lambda_min on a genuine window direction is an IMPLEMENTATION SIGNAL,
    fenced, never reported as mathematics.
  * lambda_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute positivity, never prove it.  Every quantity
    proposed here as a continuum object is reported with its grid drift, and
    the whole point of C1 is to separate the drifting objects (lam_top, mode
    counts) from the drift-free ones (fixed thresholds, band counts, m(Lam)).
  * No "proved" language without a certificate.  Three status labels are used
    and never mixed: CERTIFIED (closed form from classical inputs), DELTA-LOCAL
    (an exact wing-side object, grid drift reported -- the same footing T99's
    R_G already stands on), MEASURED (needs the full discrete spectrum; a
    signal, not an ingredient).
  * Classical anchors cited, not re-derived: Weil 1952, Yoshida 1992 /
    Bombieri 2000 / Connes-Consani 2021, the digamma archimedean kernel,
    Rayleigh-Ritz, Paley-Wiener, Parseval/Bessel, the Schur test, Schur
    complements, centrosymmetric block diagonalisation (Cantoni-Butler 1976),
    Slepian-Pollak-Landau prolate concentration (Nystrom, drift reported),
    and the Fredholm alternative (cited as the SHAPE of the missing zone-5
    argument, not as a proof of it).
"""
import ast
import math
import os
import time

import mpmath
import numpy as np
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh

PASS = 0
FAIL = 0
T_START = time.time()
mpmath.mp.dps = 30

EULER = float(mpmath.euler)
LOG_PI = math.log(math.pi)
K0_CLOSED = -EULER - 3.0 * math.log(2.0) - math.pi / 2.0 - LOG_PI
T0_REF = 6.28983599
MAX_ARRAY = 2000
M_CAP = 1900                 # main sweep
CAPS3 = (900, 1300, 1900)    # nested grids
MAXN_SEEN = 0

# (n, log n, mu_n = 2 Lambda(n)/sqrt(n))
ATOMS = (
    (2, math.log(2.0), 2.0 * math.log(2.0) / math.sqrt(2.0)),
    (3, math.log(3.0), 2.0 * math.log(3.0) / math.sqrt(3.0)),
    (4, math.log(4.0), 2.0 * math.log(2.0) / 2.0),
    (5, math.log(5.0), 2.0 * math.log(5.0) / math.sqrt(5.0)),
)
ALPHA_NEXT_ATOM = math.log(7.0) / 2.0
ALPHA_CLASSIC = math.log(2.0) / 2.0
MU_NEXT = 2.0 * math.log(7.0) / math.sqrt(7.0)
DELTA_FRACS = (0.08, 0.22, 0.40, 0.58, 0.76, 0.92)
T99_FLOOR = (0.04, 0.19)         # the obstruction this probe attacks

GLX, GLW = np.polynomial.legendre.leggauss(24)
SQ2 = math.sqrt(2.0)


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-32s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-32s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------------
# el_firewall -- AST scan of this source
# ----------------------------------------------------------------------------
FORBIDDEN_TOKENS = tuple("".join(parts) for parts in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
    ("25.01", "0857"), ("30.42", "4876"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "mpmath", "numpy", "scipy"}


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
# archimedean kernel  k(t) = Re psi(1/4 + i t/2) - log pi
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


def kernel_k_scalar(t):
    return float(kernel_k(np.array([float(t)]))[0])


# ----------------------------------------------------------------------------
# PWC Galerkin assembly on (-alpha, alpha) with M cells
#   basis phi_i = 1_{cell i} / sqrt(d),  d = 2 alpha / M   (orthonormal)
# ----------------------------------------------------------------------------
_IDX_CACHE = {}


def index_matrix(M):
    global MAXN_SEEN
    MAXN_SEEN = max(MAXN_SEEN, M)
    if M not in _IDX_CACHE:
        if len(_IDX_CACHE) > 3:
            _IDX_CACHE.clear()
        i = np.arange(M, dtype=np.int32)
        _IDX_CACHE[M] = np.abs(i[:, None] - i[None, :])
    return _IDX_CACHE[M]


def arch_symbol(alpha, M):
    """Symmetric-Toeplitz symbol t[p] of A_arch in the PWC basis (exact)."""
    assert M <= MAX_ARRAY
    d = 2.0 * alpha / M
    b = 2.0 * alpha
    s = (GLX + 1.0) / 2.0
    wq = GLW / 2.0 * d
    U = (np.arange(M)[:, None] + s[None, :]) * d
    W = 2.0 * np.exp(-U / 2.0) / (-np.expm1(-2.0 * U))
    S = np.broadcast_to(s[None, :], U.shape)
    rise = (wq[None, :] * W * S).sum(axis=1)
    fall = (wq[None, :] * W * (1.0 - S)).sum(axis=1)
    lam = np.zeros(M + 1)
    lam[0] = fall[0]
    lam[1:M] = rise[0:M - 1] + fall[1:M]
    reg0 = float((wq * W[0] * (np.expm1(-1.5 * U[0]) + s)).sum())
    rest = float((wq[None, :] * W[1:] * np.exp(-1.5 * U[1:])).sum())
    Cb = -EULER - LOG_PI - math.log(-np.expm1(-2.0 * b))
    t = np.zeros(M)
    t[0] = Cb + reg0 + rest
    t[1:] = -0.5 * lam[1:M]
    return t


def atom_symbol(u, alpha, M):
    """Symmetric-Toeplitz symbol of f -> h_f(u) in the PWC basis (exact)."""
    d = 2.0 * alpha / M
    q = u / d
    qr = round(q)
    if abs(q - qr) < 1e-9:
        m, th = int(qr), 0.0
    else:
        m, th = int(math.floor(q)), q - math.floor(q)
    t = np.zeros(M)
    if m == 0:
        t[0] = 1.0 - th
        if M > 1:
            t[1] += 0.5 * th
    else:
        if m < M:
            t[m] += 0.5 * (1.0 - th)
        if m + 1 < M:
            t[m + 1] += 0.5 * th
    return t


def pole_vectors(alpha, M):
    d = 2.0 * alpha / M
    x = -alpha + d * np.arange(M + 1)
    a = 2.0 * (np.exp(x[1:] / 2.0) - np.exp(x[:-1] / 2.0)) / math.sqrt(d)
    b = 2.0 * (np.exp(-x[:-1] / 2.0) - np.exp(-x[1:] / 2.0)) / math.sqrt(d)
    return a, b


def arch_matrix(alpha, M):
    return arch_symbol(alpha, M)[index_matrix(M)]


def atom_matrix(u, alpha, M):
    return atom_symbol(u, alpha, M)[index_matrix(M)]


def lam_min(Mx):
    return float(eigvalsh(Mx, subset_by_index=[0, 0])[0])


def lam_max(Mx):
    n = Mx.shape[0]
    return float(eigvalsh(Mx, subset_by_index=[n - 1, n - 1])[0])


def sym(Mx):
    return 0.5 * (Mx + Mx.T)


# ----------------------------------------------------------------------------
# el_kernel / el_forms
# ----------------------------------------------------------------------------
def gate_kernel():
    ts = np.array([0.0, 0.37, 1.0, 2.5, 6.28983599, 13.7, 41.0, 260.0])
    ref = np.array([float(mpmath.re(mpmath.digamma(mpmath.mpf(0.25) + 0.5j * mpmath.mpf(t))))
                    - LOG_PI for t in ts])
    err = float(np.max(np.abs(kernel_k(ts) - ref)))
    check("el_kernel.digamma", err <= 1e-12, "max |k - mpmath| = %.2e" % err)
    e0 = abs(kernel_k_scalar(0.0) - K0_CLOSED)
    check("el_kernel.k0", e0 <= 1e-13, "k(0) = %.10f, |err| = %.2e" % (K0_CLOSED, e0))
    lo, hi = 6.0, 7.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if kernel_k_scalar(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    t0 = 0.5 * (lo + hi)
    check("el_kernel.t0", abs(t0 - T0_REF) <= 1e-8, "t0 = %.9f" % t0)
    # MONOTONICITY -- the ingredient that turns the band LP into greedy filling
    tg = np.concatenate([np.linspace(0.0, 40.0, 4001), np.geomspace(40.0, 1e7, 4000)])
    kg = kernel_k(tg)
    dmin = float(np.min(np.diff(kg)))
    check("el_kernel.monotone", dmin >= -1e-14,
          "k increasing on [0,1e7] (min forward diff %.1e); min k = k(0)" % dmin)
    return t0


def arch_flat_uspace(alpha):
    b = 2 * mpmath.mpf(alpha)
    w = lambda u: 2 * mpmath.e ** (-u / 2) / (1 - mpmath.e ** (-2 * u))
    hh = lambda u: 1 - u / b
    Cb = -mpmath.euler - mpmath.log(mpmath.pi) - mpmath.log(1 - mpmath.e ** (-2 * b))
    integ = lambda u: w(u) * (mpmath.e ** (mpmath.mpf(-3) * u / 2) - hh(u))
    return float(Cb + mpmath.quad(integ, [0, b / 8, b / 2, b]))


def gate_forms():
    alpha, M = 0.31, 400
    t = arch_symbol(alpha, M)
    c = np.full(M, 1.0 / math.sqrt(M))
    A_disc = float(c @ (t[index_matrix(M)] @ c))
    A_u = arch_flat_uspace(alpha)
    check("el_forms.arch_uspace", abs(A_disc - A_u) <= 1e-10,
          "PWC %.12f vs mpmath %.12f (d=%.2e)" % (A_disc, A_u, abs(A_disc - A_u)))
    rng = np.random.default_rng(10001)
    v = rng.normal(size=M)
    v /= np.linalg.norm(v)
    d = 2.0 * alpha / M
    worst = 0.0
    for u in (0.2, 0.37, 2.0 * alpha - 0.031):
        q = u / d
        m0 = int(math.floor(q))
        th = q - m0
        direct = (1.0 - th) * float(v[m0:] @ v[:M - m0])
        if m0 + 1 < M:
            direct += th * float(v[m0 + 1:] @ v[:M - m0 - 1])
        mat = float(v @ (atom_matrix(u, alpha, M) @ v))
        worst = max(worst, abs(direct - mat))
    check("el_forms.atom_toeplitz", worst <= 1e-12,
          "max |Toeplitz - direct| = %.2e" % worst)


# ----------------------------------------------------------------------------
# C1  S1 -- the CLOSED-FORM certificate for lam_min(A_sh)
#   A_arch|E_- = int k d nu_-,  nu_- a probability measure (T98 identity)
# ----------------------------------------------------------------------------
_SLEP_CACHE = {}


def slepian_lam0(c, nq=160):
    """Top Slepian-Pollak-Landau concentration eigenvalue at time-bandwidth c.

    lam_0(c) = max over unit f supported on an interval of length delta of the
    energy fraction of fhat in [-T,T], with c = T*delta/2 (Slepian-Pollak 1961,
    Landau-Pollak 1961).  Nystrom on the sinc kernel; grid drift is gated."""
    if c <= 0.0:
        return 0.0
    key = round(c, 6)
    if key in _SLEP_CACHE:
        return _SLEP_CACHE[key]
    x, w = np.polynomial.legendre.leggauss(nq)
    dx = x[:, None] - x[None, :]
    K = np.where(np.abs(dx) < 1e-12, c / math.pi,
                 np.sin(c * np.where(np.abs(dx) < 1e-12, 1.0, dx))
                 / (math.pi * np.where(np.abs(dx) < 1e-12, 1.0, dx)))
    sw = np.sqrt(w)
    val = lam_max(sym(sw[:, None] * K * sw[None, :]))
    val = min(1.0, max(0.0, val))
    if len(_SLEP_CACHE) < 4096:
        _SLEP_CACHE[key] = val
    return val


def nu_cap(T, u, delta, use_slepian=True):
    """Certified upper bound on nu_-([-T,T]) for any unit wing function.

    Three independent classical caps, all valid simultaneously:
      (a) Parseval    : nu <= max_{|t|<=T}(1 - cos(tu)) * ||phi||^2
      (b) Cauchy-Schwarz/Bessel : |phihat(t)|^2 <= delta, so
          nu <= (delta/pi)(T - sin(Tu)/u)
      (c) Slepian     : nu <= max_{|t|<=T}(1-cos(tu)) * lam_0(T delta / 2)"""
    if T <= 0.0:
        return 0.0
    mx = 2.0 if T * u >= math.pi else 1.0 - math.cos(T * u)
    cap = min(1.0, mx)
    cap = min(cap, (delta / math.pi) * (T - math.sin(T * u) / u))
    if use_slepian:
        cap = min(cap, mx * slepian_lam0(0.5 * T * delta))
    return max(0.0, min(1.0, cap))


def arch_cert_minus(u, delta, nband=220, use_slepian=True):
    """CERTIFIED lower bound for A_arch|E_- / ||f||^2 = int k d nu_-.

    k is increasing in |t| (gated), so the LP  min int k dnu  subject to the
    cumulative caps and total mass 1 is solved exactly by greedy water-filling
    from the bottom band upwards."""
    Tmax = max(4.0 * math.pi / max(delta, 1e-6), 8.0 * math.pi / u)
    Ts = np.concatenate([[0.0], np.geomspace(1e-3, Tmax, nband)])
    caps = np.array([nu_cap(T, u, delta, use_slepian) for T in Ts])
    caps = np.maximum.accumulate(caps)
    ks = kernel_k(Ts)
    tot = 0.0
    prev = 0.0
    for j in range(1, Ts.size):
        m = caps[j] - prev
        if m <= 0.0:
            continue
        tot += m * ks[j - 1]        # k >= k(T_{j-1}) on band [T_{j-1}, T_j]
        prev = caps[j]
    tot += (1.0 - prev) * ks[-1]
    return float(tot)


def pole_cert_minus(u, delta):
    """EXACT closed form (T98 R1-iii): P_pole|E_- >= -(cosh(u/2)-1)(2 sinh(d/2)+d)."""
    return -(math.cosh(0.5 * u) - 1.0) * (2.0 * math.sinh(0.5 * delta) + delta)


def atom_cert_minus(kidx, u, delta):
    """CERTIFIED lower bound for the old-atom part of Q|E_-.

    On E_- the diagonal autocorrelations vanish (delta < log 2 in every zone),
    so h_f(u_j) = -h_L(u - u_j)/2 and the atom term is +mu_j h_L(u-u_j)/2 with
    |h_L| <= 1 (Cauchy-Schwarz).  Only atoms with u - u_j < delta touch E_-."""
    lo, hit = 0.0, []
    for (nj, uj, muj) in ATOMS[:kidx]:
        if u - uj < delta:
            lo -= 0.5 * muj
            hit.append(nj)
    return lo, hit


def lamA_cert(kidx, u, delta, mu):
    a = arch_cert_minus(u, delta)
    p = pole_cert_minus(u, delta)
    at, hit = atom_cert_minus(kidx, u, delta)
    return dict(arch=a, pole=p, atom=at, atom_hit=hit, shift=0.5 * mu,
                total=a + p + at + 0.5 * mu)


def schur_test(A):
    """||A||_op <= sqrt(||A||_1 ||A||_inf)  -- row/column sum bound, grid-stable."""
    r = float(np.max(np.abs(A).sum(axis=1)))
    c = float(np.max(np.abs(A).sum(axis=0)))
    return math.sqrt(r * c)


# ----------------------------------------------------------------------------
# geometry, blocks, parity
# ----------------------------------------------------------------------------
def alpha_top(kidx):
    return 0.5 * ATOMS[kidx + 1][1] if kidx + 1 < len(ATOMS) else ALPHA_NEXT_ATOM


def delta_max(kidx):
    return 2.0 * alpha_top(kidx) - ATOMS[kidx][1]


def mu_next(kidx):
    return ATOMS[kidx + 1][2] if kidx + 1 < len(ATOMS) else MU_NEXT


def wing_grid(u, delta_target, m_cap, n_wing_min=6):
    """Grid with d = u/m EXACTLY and delta = nI d exactly; alpha = (u+delta)/2."""
    m = max(8, int(m_cap * u / (u + delta_target)))
    d = u / m
    nI = max(n_wing_min, int(round(delta_target / d)))
    while m + nI > m_cap and m > 16:
        m -= 8
        d = u / m
        nI = max(n_wing_min, int(round(delta_target / d)))
    M = m + nI
    return 0.5 * M * d, M, m, nI, nI * d


def fast_blocks(Q, m, nI):
    QLL = Q[0:nI, 0:nI]
    QLR = Q[0:nI, m:m + nI]
    QRR = Q[m:m + nI, m:m + nI]
    QLC = Q[0:nI, nI:m]
    QRC = Q[m:m + nI, nI:m]
    Qmm = 0.5 * (QLL - QLR - QLR.T + QRR)
    Qm0 = (QLC - QRC) / SQ2
    Q00 = Q[nI:m, nI:m]
    return Qmm, Q00, Qm0


def parity_basis(n):
    """Orthonormal bases of the reflection-even / -odd subspaces (J v = v[::-1])."""
    ke, ko = (n + 1) // 2, n // 2
    Be = np.zeros((n, ke))
    Bo = np.zeros((n, ko))
    r = 1.0 / SQ2
    for i in range(n // 2):
        Be[i, i] = r
        Be[n - 1 - i, i] = r
        Bo[i, i] = r
        Bo[n - 1 - i, i] = -r
    if n % 2:
        Be[n // 2, ke - 1] = 1.0
    return Be, Bo


def build_blocks(kidx, delta_target, m_cap):
    n, u, mu = ATOMS[kidx]
    alpha, M, m, nI, delta = wing_grid(u, delta_target, m_cap)
    Q = arch_matrix(alpha, M)
    av, bv = pole_vectors(alpha, M)
    P = np.outer(av, bv)
    Q += P
    Q += P.T
    for (_nj, uj, muj) in ATOMS[:kidx]:
        Q -= muj * atom_matrix(uj, alpha, M)
    Qmm, Q00, Qm0 = fast_blocks(Q, m, nI)
    return dict(n=n, kidx=kidx, u=u, mu=mu, alpha=alpha, M=M, m=m, nI=nI,
                delta=delta, n0=M - 2 * nI, d=2.0 * alpha / M,
                Qmm=Qmm, Q00=Q00, Qm0=Qm0)


# ----------------------------------------------------------------------------
# C2  the remainder families, per parity channel
# ----------------------------------------------------------------------------
BAND_LAM0 = 2.0        # the fixed continuum threshold below which modes are explicit
N_LADDER = 30          # thresholds in the Lam ladder


def chan_data(Amm, Q00c, Gc, mu):
    """One reflection channel, reduced to the A_sh^{-1/2} coordinates.

    Gc is (dim E_0 channel) x (dim E_- channel); its columns are Q_0- x."""
    nIc = Gc.shape[1]
    lam, Phi = eigh(Q00c)
    C = Phi.T @ Gc
    Ash = Amm + 0.5 * mu * np.eye(nIc)
    aw, AV = eigh(Ash)
    W = sym((C / lam[:, None]).T @ C)
    Dk = -lam_min(Amm - W)
    out = dict(lam1=float(lam[0]), lam_top=float(lam[-1]), lamA=float(aw[0]),
               Dk=Dk, dim=nIc, ndim0=lam.size, ok=bool(aw[0] > 1e-12))
    if not out["ok"]:
        out.update(rho=float("nan"), R_G=float("nan"))
        return out
    Ainv = (AV * (aw ** -0.5)) @ AV.T
    Z = C @ Ainv                                   # rows z_j^T
    T_all = sym(Z.T @ Z)
    out.update(rho=lam_max(sym((Z / lam[:, None]).T @ Z)), R_G=lam_max(T_all),
               lam=lam, Z=Z, T_all=T_all, G2=float(np.sum(Gc * Gc)))
    return out


def bound_at(chans, Lam):
    """Both families at ONE continuum threshold Lam, maximised over the channels.

    The target  W <= A_sh  must hold on ALL of E_-, i.e. rho_c <= 1 in BOTH
    parity channels -- the channel with the larger D_k is not always the channel
    with the larger rho, so every bound here is a max over the two."""
    b99 = btl = mtot = rmax = 0.0
    N = 0
    for ch in chans:
        lam, Z, T_all, R_G = ch["lam"], ch["Z"], ch["T_all"], ch["R_G"]
        J = int(np.searchsorted(lam, Lam, side="right"))
        N += J
        rmax = max(rmax, R_G)
        if J > 0:
            Zl = Z[:J]
            L = sym((Zl / lam[:J, None]).T @ Zl)
            S = sym(Zl.T @ Zl)
            lmax_L = lam_max(L)
        else:
            L = np.zeros((Z.shape[1], Z.shape[1]))
            S = np.zeros_like(L)
            lmax_L = 0.0
        Tt = T_all - S
        m = max(0.0, lam_max(Tt))
        mtot = max(mtot, m)
        b99 = max(b99, lmax_L + R_G / Lam)          # T99 family
        btl = max(btl, lam_max(L + Tt / Lam))       # L1 tail projection
    return dict(Lam=Lam, N=N, m=mtot, R_G=rmax, b_t99=b99, b_tail=btl,
                rem_t99=rmax / Lam, rem_tail=mtot / Lam)


def lam_ladder(chans):
    top = max(ch["lam_top"] for ch in chans)
    return list(np.geomspace(0.15, top, N_LADDER)) + [top * (1.0 + 1e-12)]


def find_lam_ok(chans, rows, Lams, key):
    """Least CONTINUUM threshold at which the family closes (bisected, not a
    mode index -- that is the whole point of C1)."""
    idx = next((i for i, r in enumerate(rows) if r[key] <= 1.0), None)
    if idx is None:
        return None
    lo = Lams[idx - 1] if idx > 0 else 0.5 * Lams[0]
    hi = Lams[idx]
    for _ in range(14):
        mid = math.sqrt(lo * hi)
        if bound_at(chans, mid)[key] <= 1.0:
            hi = mid
        else:
            lo = mid
    return bound_at(chans, hi)


def banded_bound(chans, Lam0, nband):
    """L2: explicit modes below the fixed threshold Lam0, then geometric BANDS.

    w_j = 1 / (lower edge of j's band) >= 1/lam_j, so the bound is valid; band
    EDGES are continuum objects while mode indices are not."""
    out = 0.0
    for ch in chans:
        lam, Z = ch["lam"], ch["Z"]
        n = lam.size
        J0 = min(int(np.searchsorted(lam, Lam0, side="right")), n - 1)
        w = np.empty(n)
        w[:J0] = 1.0 / lam[:J0]
        lo, hi = float(lam[J0]), float(lam[-1])
        if hi <= lo * (1.0 + 1e-12) or nband <= 1:
            w[J0:] = 1.0 / lo
        else:
            edges = np.geomspace(lo, hi, nband + 1)
            idx = np.searchsorted(lam, edges, side="left")
            idx[0], idx[-1] = J0, n
            for b in range(nband):
                a0, a1 = max(idx[b], J0), max(idx[b + 1], J0)
                if a1 > a0:
                    w[a0:a1] = 1.0 / lam[a0]
            w[J0:] = np.maximum(w[J0:], 1.0 / lam[J0:])
        Zw = Z * np.sqrt(w)[:, None]
        out = max(out, lam_max(sym(Zw.T @ Zw)))
    return out


def sample(kidx, delta_target, m_cap, with_blind=False):
    b = build_blocks(kidx, delta_target, m_cap)
    nI, n0, mu = b["nI"], b["n0"], b["mu"]
    Qmm, Q00, Qm0 = b["Qmm"], b["Q00"], b["Qm0"]
    Be, Bo = parity_basis(nI)
    Ce, Co = parity_basis(n0)
    e_cross = max(float(np.max(np.abs(Be.T @ Qm0 @ Ce))),
                  float(np.max(np.abs(Bo.T @ Qm0 @ Co)))) if nI > 1 else 0.0
    cd = {
        "even": chan_data(Be.T @ Qmm @ Be, Co.T @ Q00 @ Co,
                          np.ascontiguousarray((Be.T @ Qm0 @ Co).T), mu),
        "odd": chan_data(Bo.T @ Qmm @ Bo, Ce.T @ Q00 @ Ce,
                         np.ascontiguousarray((Bo.T @ Qm0 @ Ce).T), mu),
    }
    chans = [cd["even"], cd["odd"]]
    binder = "even" if cd["even"]["Dk"] >= cd["odd"]["Dk"] else "odd"
    rbind = "even" if cd["even"]["rho"] >= cd["odd"]["rho"] else "odd"
    Dk = max(c["Dk"] for c in chans)
    out = dict(n=b["n"], kidx=kidx, u=b["u"], mu=mu, alpha=b["alpha"],
               delta=b["delta"], alpha_p=b["u"] - b["alpha"], d=b["d"], M=b["M"],
               nI=nI, n0=n0, binder=binder, rho_binder=rbind, e_cross=e_cross,
               Dk=Dk, half_mu=0.5 * mu, margin=0.5 * mu - Dk,
               rho=max(c["rho"] for c in chans),
               R_G=max(c["R_G"] for c in chans),
               lamA=min(c["lamA"] for c in chans),
               lam_top=max(c["lam_top"] for c in chans),
               ndim0=sum(c["ndim0"] for c in chans),
               # the EVEN E_- channel reads the ODD window spectrum and vice versa
               lamw_odd=cd["even"]["lam1"], lamw_even=cd["odd"]["lam1"],
               G_op=float(np.linalg.norm(Qm0, 2)), G_schur=schur_test(Qm0),
               cert=lamA_cert(kidx, b["u"], b["delta"], mu), cd=cd, chans=chans)
    out["Lams"] = lam_ladder(chans)
    out["rows"] = [bound_at(chans, L) for L in out["Lams"]]
    out["B_floor_t99"] = out["R_G"] / out["lam_top"]
    if with_blind:
        out["blind"] = chan_data(Qmm, Q00, np.ascontiguousarray(Qm0.T), mu)
    return out


def row_at(s, Lam):
    """The combined bound at a threshold, taken from the ladder (nearest above)."""
    cand = [r for r in s["rows"] if r["Lam"] >= Lam]
    return cand[0] if cand else s["rows"][-1]


def drift(vals):
    v = [x for x in vals if np.isfinite(x)]
    if len(v) < 2 or abs(v[-1]) < 1e-300:
        return float("nan")
    return abs(v[-1] - v[0]) / abs(v[-1])


def loglog_fit(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = (x > 0) & (y > 0) & np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3:
        return float("nan"), float("nan")
    lx, ly = np.log(x[ok]), np.log(y[ok])
    A = np.vstack([lx, np.ones_like(lx)]).T
    sol, *_ = np.linalg.lstsq(A, ly, rcond=None)
    res = ly - A @ sol
    ss = float(res @ res)
    st = float(((ly - ly.mean()) ** 2).sum())
    return float(sol[0]), (1.0 - ss / st if st > 0 else float("nan"))


# ----------------------------------------------------------------------------
def main():
    section("BULK.REMAINDER -- part 100 -- gates")
    firewall()
    gate_kernel()
    gate_forms()

    # ------------------------------------------------------ R0  the geometry
    section("R0  THE LAY OF THE LAND -- geometry, and where old atoms reach E_-")
    print("  zone k:  u = log n_k,  delta = 2 alpha - u in (0, delta_max),")
    print("  alpha' = u - alpha = (u - delta)/2 is the smaller window.")
    print("  n   u        delta_max  mu_k/2   mu_next/mu_k   old atoms with u-u_j<delta_max")
    for kidx, (n, u, mu) in enumerate(ATOMS):
        dmx = delta_max(kidx)
        _lo, hit = atom_cert_minus(kidx, u, dmx)
        print("  %d  %7.4f  %8.4f   %6.4f   %10.4f     %s"
              % (n, u, dmx, 0.5 * mu, mu_next(kidx) / mu,
                 ("n=" + ",".join(str(h) for h in hit)) if hit else "none"))
    dmx_all = max(delta_max(k) for k in range(len(ATOMS)))
    check("el_forms.delta_lt_log2", dmx_all < math.log(2.0),
          "delta_max = %.4f < log 2 = %.4f in every zone => the diagonal wing "
          "autocorrelations h_L(u_j) vanish and the old-atom part of Q|E_- is "
          "exactly -sum mu_j h_L(u-u_j)/2" % (dmx_all, math.log(2.0)))
    info("R0 handoff", "mu_{k+1}/mu_k = %s -- zone 5 is the ONLY zone where the "
         "outgoing and incoming atom weights match to 2%%, and (T99) it is the only "
         "zone whose top saturates.  Reported as an OBSERVATION, not a mechanism"
         % ", ".join("%.3f (n=%d)" % (mu_next(k) / ATOMS[k][2], ATOMS[k][0])
                     for k in range(len(ATOMS))))

    # ---------------------------------------- R1 / C1  certify the remainder
    section("R1  C1 -- CERTIFY:  the drift-free object and the closed-form R_G")
    print("  (a) WHERE THE 10.8% DRIFT COMES FROM.  The T99 chain B_rk = ||Z_Lam||^2")
    print("      + R_G/Lam is ALREADY indexed by a threshold Lam and is drift-free at")
    print("      fixed Lam.  The drift sits in the FLOOR statement R_G/lam_top, i.e.")
    print("      in the special case Lam = lam_max(Q|E_0) -- and lam_top is not a")
    print("      continuum object: k(t) ~ log(t/2pi) makes it diverge like log(1/d).")
    print("")
    print("  n   delta    d (3 grids)                lam_top (3 grids)          "
          "drift  slope vs log(1/d)")
    top_rows = []
    for kidx in (0, 2, 3):
        vals = [sample(kidx, 0.55 * delta_max(kidx), c) for c in CAPS3]
        lt = [v["lam_top"] for v in vals]
        ds = [v["d"] for v in vals]
        sl = np.polyfit(np.log(1.0 / np.array(ds)), np.array(lt), 1)[0]
        top_rows.append((ATOMS[kidx][0], vals, drift(lt), sl))
        print("  %d  %6.4f   %.2e %.2e %.2e   %6.3f %6.3f %6.3f     %5.1f%%  %+7.3f"
              % (ATOMS[kidx][0], vals[0]["delta"], ds[0], ds[1], ds[2],
                 lt[0], lt[1], lt[2], 100 * drift(lt), sl))
    lam_top_drift = max(r[2] for r in top_rows)
    check("el_cert.lamtop_drifts", lam_top_drift >= 0.03,
          "lam_top drifts %.1f%% over the three nested grids with a POSITIVE "
          "log(1/d) slope %+.2f..%+.2f: R_G/lam_top is a grid artefact, not a "
          "continuum floor" % (100 * lam_top_drift,
                               min(r[3] for r in top_rows), max(r[3] for r in top_rows)))

    print("")
    print("  (b) THE DRIFT-FREE REPLACEMENTS.  At a FIXED threshold Lam the three")
    print("      objects the chain needs are measured on the same three grids:")
    print("      N(Lam) = #modes below Lam,  m(Lam) = defect tail mass,  R_G/Lam.")
    LAM_FIX = 3.0
    print("  n   delta    N(%.1f) (3 grids)   drift   m(%.1f) (3 grids)          drift   "
          "R_G drift" % (LAM_FIX, LAM_FIX))
    nfix_drifts, mfix_drifts = [], []
    for (n, vals, _dr, _sl) in top_rows:
        Ns, Ms = [], []
        for v in vals:
            r = bound_at(v["chans"], LAM_FIX)
            Ns.append(r["N"])
            Ms.append(r["m"])
        dN, dM = drift([float(x) for x in Ns]), drift(Ms)
        nfix_drifts.append(dN)
        mfix_drifts.append(dM)
        print("  %d  %6.4f   %4d %4d %4d       %5.1f%%  %.3e %.3e %.3e   %5.1f%%   %5.1f%%"
              % (n, vals[0]["delta"], Ns[0], Ns[1], Ns[2], 100 * dN,
                 Ms[0], Ms[1], Ms[2], 100 * dM, 100 * drift([v["R_G"] for v in vals])))
    check("el_cert.driftfree", max(nfix_drifts) <= 0.15 and max(mfix_drifts) <= 0.15,
          "at fixed Lam = %.1f: N(Lam) drifts <= %.1f%% and the defect tail m(Lam) "
          "<= %.1f%% -- both continuum objects, unlike lam_top (%.1f%%)"
          % (LAM_FIX, 100 * max(nfix_drifts), 100 * max(mfix_drifts),
             100 * lam_top_drift))

    print("")
    print("  (c) S1 -- the CLOSED-FORM lower bound lam_A^cert <= lam_min(A_sh).")
    print("      nu-measure identity (T98) + Parseval + Cauchy-Schwarz/Bessel +")
    print("      Slepian lam_0 + monotone k  =>  greedy water-filling on int k dnu;")
    print("      pole part exact; old atoms via |h_L| <= 1.")
    print("  n   delta    A_arch^cert  P_pole^cert  atom^cert  +mu/2    lam_A^cert  "
          "lam_A(meas)  valid")
    cert_rows = []
    for kidx in range(len(ATOMS)):
        for fr in (0.08, 0.40, 0.76, 0.92):
            s = sample(kidx, fr * delta_max(kidx), M_CAP)
            c = s["cert"]
            good = c["total"] <= s["lamA"] + 1e-9
            cert_rows.append((s, c, good))
            print("  %d  %6.4f  %+11.4f  %+11.4f  %+9.4f  %+7.4f  %+10.4f  %+10.4f  %s"
                  % (s["n"], s["delta"], c["arch"], c["pole"], c["atom"],
                     c["shift"], c["total"], s["lamA"], "ok" if good else "VIOLATED"))
    check("el_cert.lamA_lower", all(g for (_s, _c, g) in cert_rows),
          "lam_A^cert <= lam_min(A_sh) at all %d samples (a Rayleigh-Ritz lam_min "
          "is an upper bound for the continuum value, so the certificate must sit "
          "below it)" % len(cert_rows))
    n_pos = sum(1 for (_s, c, _g) in cert_rows if c["total"] > 0)
    frac_pos = {}
    for (s, c, _g) in cert_rows:
        frac_pos.setdefault(s["n"], []).append(c["total"] > 0)
    info("C1 coverage", "lam_A^cert > 0 (a non-vacuous certificate) at %d/%d samples: "
         "%s -- the certificate is strong on the LOWER part of every zone and goes "
         "vacuous towards the top, where the wing gets wide, the nu-measure is "
         "allowed low-frequency mass and k(0) = %.3f dominates"
         % (n_pos, len(cert_rows),
            ", ".join("n=%d %d/4" % (n, sum(v)) for n, v in sorted(frac_pos.items())),
            K0_CLOSED))

    print("")
    print("  (d) S2 -- ||Q_0-||_op by the Schur test (grid-stable) and the resulting")
    print("      fully closed-form R_G^cert = G_cert^2 / lam_A^cert.")
    print("  n   delta    ||G||_op   G_schur   ratio   R_G(meas)  R_G^cert     valid")
    schur_ok, rg_ok, rgc = True, True, []
    for (s, c, _g) in cert_rows:
        r = s["G_schur"] / s["G_op"]
        if s["G_schur"] < s["G_op"] * (1 - 1e-9):
            schur_ok = False
        if c["total"] > 0:
            v = s["G_schur"] ** 2 / c["total"]
            rgc.append((s, v))
            if v < s["R_G"] * (1 - 1e-9):
                rg_ok = False
            txt = "%10.3f  %s" % (v, "ok" if v >= s["R_G"] * (1 - 1e-9) else "VIOLATED")
        else:
            txt = "%10s  %s" % ("vacuous", "--")
        print("  %d  %6.4f  %9.4f %9.4f  %6.3f  %9.4f  %s"
              % (s["n"], s["delta"], s["G_op"], s["G_schur"], r, s["R_G"], txt))
    check("el_cert.schur_test", schur_ok,
          "Schur test sqrt(||.||_1 ||.||_inf) dominates the exact operator norm "
          "at every sample (overshoot 1.0x..%.1fx)"
          % max(s["G_schur"] / s["G_op"] for (s, _c, _g) in cert_rows))
    check("el_cert.rg_cert", rg_ok and rgc,
          "R_G^cert = G_cert^2/lam_A^cert >= R_G(measured) wherever the certificate "
          "is non-vacuous (%d samples); overshoot %.0fx..%.0fx"
          % (len(rgc), min(v / s["R_G"] for (s, v) in rgc),
             max(v / s["R_G"] for (s, v) in rgc)))
    info("C1 chain", "CERTIFIED chain: rho <= ||Z_Lam||^2 + R_G^cert/Lam with "
         "R_G^cert closed form, Lam a FIXED continuum threshold, and the induction "
         "data = the N(Lam) modes of the smaller window below Lam.  Nothing in it "
         "refers to lam_top.")

    # ------------------------------------------ R2 / C2  sharpen the remainder
    section("R2  C2 -- SHARPEN:  tail projection, banding, parity")
    print("  L1  The T99 step  ||P_{>=Lam} G x||^2 <= ||G x||^2  (Bessel, S4) throws")
    print("      the induction data away a second time.  Keeping it replaces the")
    print("      uniform remainder R_G/Lam by  m(Lam)/Lam,  m(Lam) = lam_max(G^T G -")
    print("      S_Lam, A_sh):  the DEFECT TAIL FUNCTION.  Same two inputs, no new")
    print("      object.  The bulk term is then not a multiple of the identity, so")
    print("      the joint Rayleigh quotient gains on top.")
    print("")
    print("  the two remainders side by side at three FIXED continuum thresholds")
    print("  (the T99 floor R_G/lam_top is quoted for reference only -- it is the")
    print("  grid-bound special case Lam = lam_top):")
    print("  n   delta   rho      1-rho    R_G     [floor]  Lam=2: R_G/L  m/L    gain"
          "   Lam=4: R_G/L  m/L    gain   Lam=6: R_G/L  m/L    gain")
    map_rows = []
    GAIN_LAMS = (2.0, 4.0, 6.0)
    for kidx in range(len(ATOMS)):
        for fr in DELTA_FRACS:
            s = sample(kidx, fr * delta_max(kidx), M_CAP)
            s["gL"] = {L: row_at(s, L) for L in GAIN_LAMS}
            s["gains"] = {L: s["gL"][L]["rem_t99"] / max(s["gL"][L]["rem_tail"], 1e-300)
                          for L in GAIN_LAMS}
            map_rows.append(s)
            print("  %d  %6.4f  %7.5f  %.2e  %6.3f  %6.3f  " % (
                s["n"], s["delta"], s["rho"], 1.0 - s["rho"], s["R_G"],
                s["B_floor_t99"]) +
                "   ".join("%8.4f %.2e %6.1fx"
                           % (s["gL"][L]["rem_t99"], s["gL"][L]["rem_tail"],
                              s["gains"][L]) for L in GAIN_LAMS))
    fl = [s["B_floor_t99"] for s in map_rows]
    info("C2 T99 floor", "reproduced: the uniform bulk remainder R_G/lam_top = "
         "%.3f..%.3f (T99 reported %.2f..%.2f)"
         % (min(fl), max(fl), T99_FLOOR[0], T99_FLOOR[1]))
    gains = [s["gains"][L] for s in map_rows for L in GAIN_LAMS]
    g6 = [s["gains"][6.0] for s in map_rows]
    check("el_sharp.tail_gain", min(gains) >= 1.0 - 1e-9,
          "tail projection never loses; at the fixed thresholds Lam = 2/4/6 the "
          "remainder shrinks by %.1fx..%.1fx (at Lam = 6: %.1fx..%.1fx)"
          % (min(gains), max(gains), min(g6), max(g6)))
    npairs, bad_valid = 0, []
    for s in map_rows:
        for r in s["rows"]:
            npairs += 1
            if r["b_tail"] < s["rho"] * (1 - 1e-9) or r["b_t99"] < s["rho"] * (1 - 1e-9):
                bad_valid.append((s["n"], r["Lam"]))
            if r["b_tail"] > r["b_t99"] * (1 + 1e-9):
                bad_valid.append((s["n"], r["Lam"]))
    check("el_sharp.valid", not bad_valid,
          "rho <= b_tail(Lam) <= b_t99(Lam) at all %d (sample, threshold) pairs and "
          "in BOTH parity channels -- operator inequalities, no fit enters either"
          % npairs)
    lim = [abs(s["rows"][-1]["b_tail"] - s["rho"]) / max(s["rho"], 1e-30)
           for s in map_rows]
    check("el_sharp.limit", max(lim) <= 1e-6,
          "b_tail -> rho exactly as Lam -> lam_top (max relative gap %.1e): the "
          "tail-projected family is COMPLETE, so its only cost is induction data"
          % max(lim))

    print("")
    print("  the defect tail m(Lam): how fast does the bulk coupling die?")
    print("  (this is THE quantitative question -- the remainder is m(Lam)/Lam.")
    print("  The power law is fitted on Lam in [0.5, 0.6 lam_top]; above that the")
    print("  discrete tail collapses into the last few modes and the fit would be")
    print("  reading the grid, not the operator.)")
    print("  n   delta   m(1)      m(2)      m(4)      m(6)      R_G      "
          "power p in m ~ Lam^-p   R2")
    tail_fits = []
    for s in map_rows[::2]:
        pick = {L: row_at(s, L)["m"] for L in (1.0, 2.0, 4.0, 6.0)}
        hi = 0.6 * s["lam_top"]
        xs = [r["Lam"] for r in s["rows"] if 0.5 <= r["Lam"] <= hi and r["m"] > 0]
        ys = [r["m"] for r in s["rows"] if 0.5 <= r["Lam"] <= hi and r["m"] > 0]
        p, r2 = loglog_fit(xs, ys)
        tail_fits.append((s, -p, r2))
        print("  %d  %6.4f  %.2e  %.2e  %.2e  %.2e  %.2e  %13.2f  %11.3f"
              % (s["n"], s["delta"], pick[1.0], pick[2.0], pick[4.0], pick[6.0],
                 s["R_G"], -p, r2))
    ps = [p for (_s, p, _r) in tail_fits if np.isfinite(p)]
    r2s = [r for (_s, _p, r) in tail_fits if np.isfinite(r)]
    info("C2 tail law", "m(Lam) falls like Lam^-p with p = %.2f..%.2f (R2 = "
         "%.2f..%.2f): the defect couples MAINLY TO THE BULK of the smaller window "
         "-- a boundary-localised extension defect is rough -- so the tail dies "
         "slowly and the remainder m(Lam)/Lam ~ Lam^-(1+p) needs Lam ~ "
         "slack^(-1/(1+p)) to beat a slack of 1e-3"
         % (min(ps), max(ps), min(r2s), max(r2s)))

    print("")
    print("  L2  BANDING.  Above Lam_0 the bulk is cut into B geometric bands with")
    print("      w_j = 1/(band lower edge) >= 1/lam_j.  B bands of ratio r bound the")
    print("      bulk by r x its exact value, so B ~ log(lam_top/Lam_0)/slack.  Band")
    print("      EDGES are continuum objects; mode INDICES are not.")
    print("  n   delta   rho      N(2)   B=4      B=16     B=64     B=256    B=1024"
          "   least B closing")
    BUDGETS = (4, 16, 64, 256, 1024)
    for s in map_rows:
        vals = [banded_bound(s["chans"], BAND_LAM0, B) for B in BUDGETS]
        least = next((B for B, v in zip(BUDGETS, vals) if v <= 1.0), None)
        if least is None and vals[-1] > 1.0:
            lo, hi = 1024, 262144
            if banded_bound(s["chans"], BAND_LAM0, hi) <= 1.0:
                while lo < hi:
                    mid = (lo + hi) // 2
                    if banded_bound(s["chans"], BAND_LAM0, mid) <= 1.0:
                        hi = mid
                    else:
                        lo = mid + 1
                least = lo
        s["band_vals"] = vals
        s["band_least"] = least
        print("  %d  %6.4f  %7.5f  %5d  %7.4f  %7.4f  %7.4f  %7.4f  %7.4f  %s"
              % (s["n"], s["delta"], s["rho"], row_at(s, BAND_LAM0)["N"],
                 vals[0], vals[1], vals[2], vals[3], vals[4],
                 ("%d" % least) if least else "> 262144"))
    bad_band = [s["n"] for s in map_rows
                if min(s["band_vals"]) < s["rho"] * (1 - 1e-9)]
    check("el_band.valid", not bad_band,
          "every banded bound dominates rho at all %d samples, every budget and "
          "both channels (w_j >= 1/lam_j by construction)" % len(map_rows))
    mono = all(all(s["band_vals"][i] >= s["band_vals"][i + 1] - 1e-9
                   for i in range(len(BUDGETS) - 1)) for s in map_rows)
    check("el_band.monotone", mono,
          "the banded bound decreases monotonically in the band count and converges "
          "to rho -- a genuine Pareto ladder in CONTINUUM data")
    closing = [s for s in map_rows if s["band_least"]]
    info("C2 band budget", "with the explicit modes below the FIXED threshold "
         "Lam_0 = %.1f (%d..%d modes over both channels), B = %d..%d geometric bands "
         "close %d/%d samples -- the entire induction datum is now (Lam_0, B), two "
         "continuum numbers"
         % (BAND_LAM0, min(row_at(s, BAND_LAM0)["N"] for s in map_rows),
            max(row_at(s, BAND_LAM0)["N"] for s in map_rows),
            min(s["band_least"] for s in closing),
            max(s["band_least"] for s in closing), len(closing), len(map_rows)))

    print("")
    print("  L3  PARITY.  The block-diagonalisation is EXACT, so it costs the bound")
    print("      nothing -- what it buys is INDUCTION DATA: each channel's bulk sum")
    print("      runs over the OPPOSITE-parity half of the smaller window only, and")
    print("      the near-null EVEN ground mode is absent from the odd-window sum.")
    print("  (window spectra: lam_1^even / lam_1^odd are the ground eigenvalues of")
    print("   the SMALLER WINDOW's two parity halves; the even one carries the")
    print("   near-null mode T98 showed to be discretisation-limited.)")
    print("  n   delta   e_cross    rho_even  rho_odd   binds  rho_blind  |blind-max| "
          " lam1^even  lam1^odd  parity gap")
    par_rows = []
    for kidx in range(len(ATOMS)):
        s = sample(kidx, 0.76 * delta_max(kidx), M_CAP, with_blind=True)
        re_, ro = s["cd"]["even"]["rho"], s["cd"]["odd"]["rho"]
        db = abs(s["blind"]["rho"] - max(re_, ro))
        par_rows.append((s, db))
        print("  %d  %6.4f  %.2e  %8.5f  %8.5f  %5s  %9.5f  %.3e   %.2e  %.2e  %9.1f"
              % (s["n"], s["delta"], s["e_cross"], re_, ro, s["rho_binder"],
                 s["blind"]["rho"], db, s["lamw_even"], s["lamw_odd"],
                 s["lamw_odd"] / s["lamw_even"]))
    ec = max(s["e_cross"] for (s, _d) in par_rows)
    check("el_parity.rule", ec <= 1e-10,
          "the exact selection rule holds to %.1e: reflection-even E_- couples ONLY "
          "to the reflection-ODD spectrum of the smaller window" % ec)
    check("el_parity.exact", max(d for (_s, d) in par_rows) <= 1e-9,
          "rho(parity-blind) = max(rho_even, rho_odd) to %.1e -- the split loses "
          "NOTHING in the bound; the gain is that each channel needs only half the "
          "smaller window's spectrum as induction data"
          % max(d for (_s, d) in par_rows))
    rho_bind = {}
    for s in map_rows:
        rho_bind[s["rho_binder"]] = rho_bind.get(s["rho_binder"], 0) + 1
    info("C2 parity", "the parity gap lam_1^odd/lam_1^even of the smaller window is "
         "%.0f..%.0f (T99: 3.0..111.5), so the EVEN E_- channel -- which reads the "
         "ODD window spectrum -- never sees the near-null mode.  CAVEAT, new here: "
         "the channel with the largest D_k is NOT always the channel with the "
         "largest rho (rho binds even at %d/%d samples, odd at %d/%d), and the "
         "operator target needs rho <= 1 in BOTH, so every bound in this probe is a "
         "max over the two channels -- including the odd one, which does read the "
         "near-null even mode"
         % (min(s["lamw_odd"] / s["lamw_even"] for (s, _d) in par_rows),
            max(s["lamw_odd"] / s["lamw_even"] for (s, _d) in par_rows),
            rho_bind.get("even", 0), len(map_rows),
            rho_bind.get("odd", 0), len(map_rows)))

    print("")
    print("  MEASURED-ONLY (reported apart from every certified number): the true")
    print("  bulk resolvent gain  Lam x (exact bulk contribution / tail mass), i.e.")
    print("  the fit-free form of the T99 decay exponent theta.  A value near 1")
    print("  means the uniform 1/Lam resolvent bound is already tight.")
    print("  n   delta   Lam=2 gain  Lam=4 gain  Lam=6 gain")
    res_gain = []
    for s in map_rows[::4]:
        line = []
        for L in (2.0, 4.0, 6.0):
            ex = tm = 0.0
            for ch in s["chans"]:
                J = int(np.searchsorted(ch["lam"], L, side="right"))
                Zt = ch["Z"][J:]
                if Zt.shape[0] == 0:
                    continue
                ex = max(ex, lam_max(sym((Zt / ch["lam"][J:, None]).T @ Zt)))
                tm = max(tm, lam_max(sym(Zt.T @ Zt)))
            line.append(L * ex / tm if tm > 0 else float("nan"))
        res_gain.extend([v for v in line if np.isfinite(v)])
        print("  %d  %6.4f  %10.4f  %10.4f  %10.4f"
              % (s["n"], s["delta"], line[0], line[1], line[2]))
    info("C2 resolvent", "the measured bulk resolvent gain is %.2f..%.2f, i.e. the "
         "certified 1/Lam step loses at most %.0f%% -- ALL of the sharpening comes "
         "from the MASS (tail projection), none of it from the resolvent.  The T99 "
         "decay exponent theta therefore has no further factor to give here"
         % (min(res_gain), max(res_gain), 100 * (1.0 - min(res_gain))))

    # -------------------------------------------- R3 / C3  the closure map
    section("R3  C3 -- THE CLOSURE MAP REDONE, and the zone-5 top typed")
    print("  A sample CLOSES when the bound is <= 1.  Columns: the T99 family, the")
    print("  tail-projected family, and the induction-data cost of each.")
    print("  n   delta   rho      1-rho     T99: Lam_ok  N     TAIL: Lam_ok  N     "
          "bands at Lam_0=%.0f  verdict" % BAND_LAM0)
    per_zone = {}
    for s in map_rows:
        r99 = find_lam_ok(s["chans"], s["rows"], s["Lams"], "b_t99")
        rtl = find_lam_ok(s["chans"], s["rows"], s["Lams"], "b_tail")
        s["r99"], s["rtl"] = r99, rtl
        per_zone.setdefault(s["n"], []).append(s)
        print("  %d  %6.4f  %7.5f  %.2e   %9s %5s     %9s %5s     %12s  %s"
              % (s["n"], s["delta"], s["rho"], 1.0 - s["rho"],
                 ("%.3f" % r99["Lam"]) if r99 else "--",
                 ("%d" % r99["N"]) if r99 else "--",
                 ("%.3f" % rtl["Lam"]) if rtl else "--",
                 ("%d" % rtl["N"]) if rtl else "--",
                 ("%d" % s["band_least"]) if s["band_least"] else "> 262144",
                 "closed" if rtl else "OPEN"))
    n99 = sum(1 for s in map_rows if s["r99"])
    ntl = sum(1 for s in map_rows if s["rtl"])
    check("el_map.improves", ntl >= n99,
          "closure: T99 family %d/%d samples -> tail-projected family %d/%d"
          % (n99, len(map_rows), ntl, len(map_rows)))
    zone_close = {n: (sum(1 for s in v if s["rtl"]), len(v)) for n, v in per_zone.items()}
    info("C3 per zone", "tail-projected closure by zone: "
         + ", ".join("n=%d %d/%d" % (n, a, b) for n, (a, b) in sorted(zone_close.items())))
    cl = [s for s in map_rows if s["rtl"]]
    info("C3 cost", "where it closes, the induction datum is 'all modes below "
         "Lam_ok = %.2f..%.2f', i.e. %d..%d modes over both channels (%.2f%%..%.1f%% "
         "of the discrete spectrum).  Lam_ok is the continuum statement; the mode "
         "count is only its grid shadow"
         % (min(s["rtl"]["Lam"] for s in cl), max(s["rtl"]["Lam"] for s in cl),
            min(s["rtl"]["N"] for s in cl), max(s["rtl"]["N"] for s in cl),
            100 * min(s["rtl"]["N"] / s["ndim0"] for s in cl),
            100 * max(s["rtl"]["N"] / s["ndim0"] for s in cl)))

    print("")
    print("  GRID STABILITY OF THE COST -- is the induction data a continuum object?")
    print("  n   delta    N_ok (3 grids)      drift    Lam_ok (3 grids)         drift"
          "    B_ok (3 grids)")
    cost_rows = []
    for kidx in (0, 2, 3):
        fr = 0.76
        Ns, Ls, Bs = [], [], []
        for c in CAPS3:
            v = sample(kidx, fr * delta_max(kidx), c)
            r = find_lam_ok(v["chans"], v["rows"], v["Lams"], "b_tail")
            Ns.append(float(r["N"]) if r else float("nan"))
            Ls.append(r["Lam"] if r else float("nan"))
            bb = next((B for B in (4, 16, 64, 256, 1024, 4096, 16384)
                       if banded_bound(v["chans"], BAND_LAM0, B) <= 1.0), None)
            Bs.append(float(bb) if bb else float("nan"))
        cost_rows.append((ATOMS[kidx][0], drift(Ns), drift(Ls), Ns, Ls, Bs))
        print("  %d  %6.4f   %6.0f %6.0f %6.0f     %5.1f%%   %6.3f %6.3f %6.3f    "
              "%5.1f%%    %6.0f %6.0f %6.0f"
              % (ATOMS[kidx][0], fr * delta_max(kidx), Ns[0], Ns[1], Ns[2],
                 100 * drift(Ns), Ls[0], Ls[1], Ls[2], 100 * drift(Ls),
                 Bs[0], Bs[1], Bs[2]))
    lam_ok_drift = max(r[2] for r in cost_rows if np.isfinite(r[2]))
    check("el_map.cost_continuum", lam_ok_drift <= 0.20,
          "the THRESHOLD Lam_ok drifts only %.1f%% over the three nested grids, "
          "while the mode count n_ok drifts %.1f%%: the continuum statement is "
          "'all modes below Lam_ok', not 'the first n_ok modes'"
          % (100 * lam_ok_drift,
             100 * max(r[1] for r in cost_rows if np.isfinite(r[1]))))

    print("")
    print("  THE ZONE TOPS -- is the saturation a SIMPLE degeneracy?")
    print("  eps-ladder alpha = alpha_top - eps; margin = lam_min(A_sh - W) =")
    print("  mu_k/2 - D_k; gap = lam_2 - lam_1 of the same operator.")
    print("  n   eps      delta    margin      gap        margin/gap   PR(null)/nI")
    top_type = {}
    for kidx in range(len(ATOMS)):
        for eps in (0.020, 0.008, 0.003):
            b = build_blocks(kidx, delta_max(kidx) - 2.0 * eps, 1500)
            cf = cho_factor(b["Q00"], lower=True, check_finite=False)
            Wf = sym(b["Qm0"] @ cho_solve(cf, b["Qm0"].T, check_finite=False))
            S11 = b["Qmm"] + 0.5 * b["mu"] * np.eye(b["nI"]) - Wf
            ev, X = eigh(S11, subset_by_index=[0, 1])
            xv = X[:, 0]
            pr = 1.0 / float(np.sum(xv ** 4)) / b["nI"]
            gap = float(ev[1] - ev[0])
            top_type.setdefault(b["n"], []).append((eps, float(ev[0]), gap, pr))
            print("  %d  %6.4f  %6.4f  %+10.3e  %.3e  %10.3e   %8.4f"
                  % (b["n"], eps, b["delta"], ev[0], gap, ev[0] / gap, pr))
    gaps = [g for v in top_type.values() for (_e, _m, g, _p) in v]
    check("el_top.simple", min(gaps) >= 1e-3,
          "the bottom eigenvalue of A_sh - W is SIMPLE at every zone top sample "
          "(spectral gap %.3f..%.3f, never below 1e-3): the saturation is a "
          "one-dimensional degeneracy" % (min(gaps), max(gaps)))
    z5 = top_type[5]
    z234 = [v for n, v in top_type.items() if n != 5]
    m5 = min(abs(m) for (_e, m, _g, _p) in z5)
    m234 = min(abs(m) for v in z234 for (_e, m, _g, _p) in v)
    info("C3 zone 5", "at eps -> 0 the zone-5 margin reaches %.2e while zones 2-4 "
         "stay at >= %.2e -- a factor %.0f.  The degeneracy is SIMPLE and the null "
         "direction is stable (participation ratio %.2f..%.2f of the wing), so the "
         "missing argument is FREDHOLM-ALTERNATIVE SHAPED: identify the single null "
         "vector of A_sh - W at alpha = alpha_top and show the rest of the spectrum "
         "is bounded away.  That is an EQUALITY statement, and no bound of the form "
         "rho <= (data) + (strictly positive remainder) can ever reach it"
         % (m5, m234, m234 / max(m5, 1e-300),
            min(p for (_e, _m, _g, p) in z5), max(p for (_e, _m, _g, p) in z5)))

    # ------------------------------------------------------- R4  synthesis
    section("R4  C4 -- THE INDUCTION SKELETON, WITH STATUS")
    print("   (1) alpha in zone k, delta = 2 alpha - u_k;  E_-/E_0/E_+ split, and")
    print("       Q|E_0 = Q_{k-1}(alpha') is the induction hypothesis.")
    print("                                                        [T97/T98  EXACT]")
    print("   (2) the k-th atom is (mu_k/2) I on E_-, so the E_-/E_0 half of the step")
    print("       is exactly  rho = lam_max(W, A_sh) <= 1.        [T98      EXACT]")
    print("   (3) parity selection rule J_- Q_-0 J_0 = -Q_-0 splits it into two")
    print("       channels, %.0e here.                            [T99      EXACT]"
          % ec)
    print("   (4) threshold split at a FIXED continuum Lam:")
    print("           rho <= lam_max( L_Lam + (G^T G - S_Lam)/Lam , A_sh )")
    print("       - L_Lam, S_Lam : the N(Lam) modes below Lam    [INDUCTION DATA]")
    print("       - G^T G        : the delta-local defect Gram   [DELTA-LOCAL]")
    print("       - 1/Lam        : spectral calculus             [CERTIFIED]")
    print("                                                        [T100     EXACT]")
    print("   (5) the delta-local inputs are certified closed form:")
    print("           lam_min(A_sh) >= lam_A^cert  (nu-measure + Parseval +")
    print("           Cauchy-Schwarz/Bessel + Slepian + monotone k, exact pole and")
    print("           atom forms)                                  [CERTIFIED, %d/%d]"
          % (n_pos, len(cert_rows)))
    print("           ||Q_0-||_op <= Schur test                    [DELTA-LOCAL]")
    print("   (6) the drift-free form of (4) is BANDED, not truncated: band edges in")
    print("       lambda are continuum objects, mode indices are not.  [T100 EXACT]")
    print("   (7) alpha' = u_k - alpha < alpha_k terminates the recursion in <= k")
    print("       steps at the classical prime-free window.       [T99      EXACT]")
    print("")
    print("  WHAT IS NOW CLOSED, AND WITH WHAT")
    for n, (a, b) in sorted(zone_close.items()):
        ss = per_zone[n]
        clz = [s for s in ss if s["rtl"]]
        bl = [s["band_least"] for s in ss if s["band_least"]]
        print("   zone n=%d: %d/%d delta-samples closed; Lam_ok = %s; bands at "
              "Lam_0 = %.0f: %s"
              % (n, a, b,
                 ("%.2f..%.2f" % (min(s["rtl"]["Lam"] for s in clz),
                                  max(s["rtl"]["Lam"] for s in clz))) if clz else "--",
                 BAND_LAM0,
                 ("%d..%d%s" % (min(bl), max(bl),
                                "" if len(bl) == len(ss) else " (+%d not closing)"
                                % (len(ss) - len(bl)))) if bl else "none"))
    print("")
    print("  THE HONEST REMAINDER LIST")
    print("   R1  The certificate for lam_A is closed form but VACUOUS on the upper")
    print("       part of the zones (%d/%d samples positive).  Missing: a sharper"
          % (n_pos, len(cert_rows)))
    print("       lower bound for A_arch|E_- at large delta.  Shape: the nu-measure")
    print("       is a probability measure and the only lever left is a better cap on")
    print("       its low-frequency mass -- Slepian already applied; the next step is")
    print("       the exact prolate spectrum per band rather than the trace bound.")
    print("       PROVABLE-SHAPED (a quantitative concentration estimate).")
    print("   R2  ||Q_0-||_op is DELTA-LOCAL, not closed form.  The Schur test makes")
    print("       it a row-sum object; a closed form needs the arch kernel's corner")
    print("       integral across the wing/centre junction.  PROVABLE-SHAPED.")
    print("   R3  The defect tail m(Lam) falls only like Lam^-%.1f..Lam^-%.1f, so the"
          % (min(ps), max(ps)))
    print("       remainder m(Lam)/Lam needs a large Lam wherever the true slack is")
    print("       1e-3.  In MODE form the cost drifts with the grid; in BAND form it")
    print("       does not.  This is a QUANTITATIVE gap, not a structural one.")
    print("   R4  Zone 5's top saturates exactly.  No inequality with a strictly")
    print("       positive remainder reaches it.  The degeneracy is SIMPLE, so the")
    print("       missing object is an EQUALITY/limit argument (Fredholm shape).")
    print("       STRUCTURALLY DIFFERENT, but not obviously hard.")
    print("   R5  E_+ and the full 3x3 assembly are untouched here (T98 R4 territory).")

    # ---------------------------------------------------------------- verdict
    zones_full = [n for n, (a, b) in zone_close.items() if a == b and n != 5]
    z5_typed = min(gaps) >= 1e-3
    improved = (ntl > n99) or (max(gains) > 1.5)
    if len(zones_full) >= 3 and z5_typed:
        verdict = "REMAINDER-CLOSES-ZONES"
    elif improved:
        verdict = "REMAINDER-SHARPENED"
    else:
        verdict = "REMAINDER-STUCK"

    section("VERDICT")
    print("  %s" % verdict)
    print("")
    print("  B1 CERTIFY.  The 10.8% drift is located exactly: it is NOT in the chain")
    print("     (which is already threshold-indexed and drift-free) but in the FLOOR")
    print("     STATEMENT R_G/lam_top, and lam_top diverges like log(1/d) (%.1f%% here,"
          % (100 * lam_top_drift))
    print("     positive log(1/d) slope).  Replacing it by a fixed continuum Lam makes")
    print("     N(Lam) and m(Lam) drift <= %.1f%% / %.1f%%.  R_G is certified in four"
          % (100 * max(nfix_drifts), 100 * max(mfix_drifts)))
    print("     explicit stages (nu-measure + Parseval + Bessel + Slepian + monotone k;")
    print("     exact pole and old-atom forms; spectral calculus; Schur test), giving")
    print("     lam_A^cert > 0 on %d/%d samples and R_G^cert >= R_G by %.0fx..%.0fx."
          % (n_pos, len(cert_rows), min(v / s["R_G"] for (s, v) in rgc),
             max(v / s["R_G"] for (s, v) in rgc)))
    print("  B2 SHARPEN.  One lever dominates: DO NOT discard the induction data in")
    print("     the Bessel step.  R_G/Lam -> m(Lam)/Lam wins %.1fx..%.1fx at fixed"
          % (min(gains), max(gains)))
    print("     thresholds Lam = 2/4/6, and the family is COMPLETE (b_tail -> rho).")
    print("     Banding turns the cost into a CONTINUUM count (Lam_0, B).  Parity")
    print("     costs the bound nothing and halves the data.  The resolvent step is")
    print("     already tight (measured gain %.2f..%.2f), so the mass is the whole"
          % (min(res_gain), max(res_gain)))
    print("     story -- the T99 decay exponent theta has no extra factor to give.")
    print("  B3 MAP.  Tail-projected closure %d/%d samples (T99: %d/%d), by zone %s,"
          % (ntl, len(map_rows), n99, len(map_rows),
             ", ".join("n=%d %d/%d" % (n, a, b) for n, (a, b) in sorted(zone_close.items()))))
    print("     with the induction datum 'all modes below Lam_ok = %.2f..%.2f'"
          % (min(s["rtl"]["Lam"] for s in cl), max(s["rtl"]["Lam"] for s in cl)))
    print("     (Lam_ok drifts %.1f%% over three grids, the mode count %.0f%%)."
          % (100 * lam_ok_drift, 100 * max(r[1] for r in cost_rows if np.isfinite(r[1]))))
    print("     The sampled zone-5 points close up to delta = 0.92 delta_max; the")
    print("     LIMIT point delta -> delta_max does not and cannot -- there rho -> 1")
    print("     and the degeneracy of A_sh - W is SIMPLE (gap >= %.3f), so what is"
          % min(gaps))
    print("     missing there is an EQUALITY argument, not a sharper inequality.")
    print("")
    el = time.time() - T_START
    check("el_budget.array", MAXN_SEEN <= MAX_ARRAY,
          "largest array %d^2 <= %d^2" % (MAXN_SEEN, MAX_ARRAY))
    check("el_budget.runtime", el < 600.0, "%.1f s < 600 s" % el)
    print("")
    print("TOTAL  %d checks, %d failures, %.1f s, largest array %d^2, verdict %s"
          % (PASS + FAIL, FAIL, el, MAXN_SEEN, verdict))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
