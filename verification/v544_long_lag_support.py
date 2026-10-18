"""v544 -- PRIME.LONGLAG.SUPP.01: the long-lag support structure of phase 2.
The SIX per-instance statements of discovery T137 that are pure structure --
every one RECOMPUTED here from scratch on small exactly checkable windows of
the frame-A construction (nothing cited from the sandbox).  Companion to
PRIME.MMATRIX.IDENT.01 / v543, which supplies the lumped pair itself.

WHAT IS LOAD-BEARING HERE (and nothing else): the SUPPORT and AMPLITUDE
structure of the positive off-diagonal part, one two-sided bracket, and one
DEATH CERTIFICATE for a whole family of bounds.  NO fit, NO decay exponent,
NO D-uniform statement, NO structure bound that closes -- T137 found that it
does not, and that negative result is part of the claim.  Each item is a
residual or a count against a preregistered tolerance AND has at least one
MUTATION / NEGATIVE control that must fail loudly.

[E] (1) THE ARCHIMEDEAN HALF CARRIES NO POSITIVE OFF-DIAGONAL (T137 H1).
    The odd section is A_rs = c_{|r-s|} - c_{M-1-r-s} and the kernel splits
    EXACTLY as c = c_arch - c_comb, c_comb = the sum of the atom hats >= 0
    (rel < 1e-14).  The archimedean section alone, A^arch_rs = c^arch_{|r-s|}
    - c^arch_{M-1-r-s}, has ALL off-diagonals <= 0 per instance: every
    positive off-diagonal of A is COMB-generated.  Control: the FULL section
    does have positive off-diagonals, so the statement is not vacuous.
[E] (2) THE SUPPORT IS AN ANTI-DIAGONAL COMB STRIPE SET (T137 H1).  Write
    anti(r, s) = M - 1 - r - s for the Hankel index.  EVERY positive
    off-diagonal entry of A has anti(r, s) inside the atom-hat index set
    {i : c_comb[i] > 0} -- the measured fraction is exactly 1.0 per instance,
    so supp(Delta) is a union of ANTI-DIAGONAL STRIPES sitting at prime-power
    atom positions.  The CONVERSE is NOT claimed: not every stripe carries a
    positive entry, and the count of loaded stripes is reported, not derived.
[E] (3) EACH STRIPE IS A PERFECT MATCHING (T137 H1).  On a stripe anti = a
    the index pair is (r, M - 1 - a - r), so every index occurs in AT MOST
    ONE pair: the edge vectors b_e = e_r - e_t of one stripe have PAIRWISE
    DISJOINT supports and are therefore MUTUALLY ORTHOGONAL (Gram off-block
    exactly 0).  Hence L_Delta restricted to a stripe is a direct sum of
    2x2 blocks.  Control: edges taken ACROSS two stripes are not orthogonal.
[E] (4) THE AMPLITUDE CERTIFICATE (T137 H1).  From (1) and c_comb >= 0,
        A_rs = A^arch_rs - c_comb[|r-s|] + c_comb[anti(r,s)]
             <= c_comb[anti(r,s)],
    so Delta_rs <= c_comb[anti(r, s)] for every positive entry -- the
    amplitude of the lumping is majorised by the COMB VALUE at the stripe
    index, with no eigenvalue and no norm.  Control: replacing the Hankel
    index by the Toeplitz lag |r - t| breaks the certificate on most edges.
    HONESTLY UNDECIDED: on windows this small the atom hats do NOT overlap
    (at most one hat per lag cell), so the tighter ONE-ATOM version
    COINCIDES with the certificate here and is neither confirmed nor refuted
    -- the T137 one-atom violation lives at depth and is NOT promoted.
[E] (5) THE GREEN FUNCTION IS BRACKETED TWO-SIDEDLY (T137 H3).  For the
    lumped Stieltjes comparison B = D_0 - N_0, J = D_0^{-1} N_0 >= 0:
      from BELOW  every term of B^{-1} = sum_k J^k D_0^{-1} is nonnegative,
                  so the PARTIAL SUM up to K is an entrywise lower bound
                  (positivity of the discarded tail is what makes a
                  truncation a bound -- not a truncation error estimate);
      from ABOVE  with the anchor x = B^{-1} 1 > 0 one has the IDENTITY
                  qJ = max_r (Jx)_r/x_r = 1 - min_r 1/(d_r x_r) < 1, hence
                  (J^k)_{rs} <= qJ^k x_r/x_s and the tail is majorised by
                  (x_r/x_s) qJ^{K+1}/((1 - qJ) d_s).
    Both directions are checked ENTRYWISE per instance.  Control: dropping
    the tail term makes the upper bound false.
[X] (6) THE ABSOLUTE-VALUE ENVELOPE FAMILY IS CERTIFIED DEAD (T137 H2).
    E = B^{-1} L_Delta and |E| its entrywise absolute value.  Gershgorin,
    every row-sum norm and every Collatz-Wielandt quotient at every POSITIVE
    weight are all >= rho(|E|), so ONE rigorous LOWER bound on rho(|E|)
    decides the whole family at once.  A Collatz-Wielandt quotient from
    BELOW at a power-iterated positive weight gives rho(|E|) >= 1 on every
    instance -- so NO member of the envelope family can ever certify
    lam_max(W) < 1.  This is a certificate of DEATH, not a measurement.  The
    SIGNED quantity rho(E) = lam_max(W) sits below 1 on the same instances:
    the absolute value alone destroys the cancellation.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   PER-INSTANCE statements on SMALL windows.  Nothing is uniform in the
        zone index, in D or in the gap; no decay profile and no amplitude LAW
        is claimed -- T137's decay measurements are FITS and stay in the
        sandbox.
  (ii)  (2) is one inclusion only: supp(Delta) sits ON the comb stripes.  The
        converse (which stripes are loaded, and how heavily) is NOT claimed.
  (iii) (4) bounds the AMPLITUDE and nothing else.  It does not bound
        lam_max(W); T137 found that the structure bound assembled from (2),
        (3), (4) does NOT beat the margin, and no such bound is promoted here.
  (iv)  (5) brackets the Green function of the LUMPED comparison B, not of
        the target.  Entrywise positivity of the target's inverse at depth is
        the open point and is not claimed.
  (v)   (6) is a NEGATIVE result.  It closes a ROUTE, not the question: what
        survives is a SIGN-PRESERVING bound, which does not exist yet.  No
        marker moves either way.

HONEST FENCES (load-bearing typing):
  * Classics named CLASSICAL: Stieltjes / Ostrowski 1937 (inverse
    positivity), Fan 1958 / Berman-Plemmons 1979 (M-matrix equivalences),
    Varga 1962 (regular splittings), Frobenius 1912 / Perron 1907,
    Collatz 1942 / Wielandt 1950 (the two-sided quotient bracket),
    Gershgorin 1931, the Neumann series (Higham 2002 Ch. 14),
    Haynsworth 1968 (the border Schur complement), Demko-Moss-Smith 1984
    (CITED as the model for inverse decay and NOT applicable verbatim, since
    the comparison is dense), Weil 1952 (the archimedean kernel, CITED,
    never used as a criterion).  NEW is only the compiler-native
    consolidation and the machine-checked residuals.
  * DIRECTION CARE IS PART OF THE CLAIM.  A lower bound on a spectral radius
    can only KILL a margin and never certify one; a Neumann truncation is a
    bound only because the discarded terms are NONNEGATIVE; a
    Collatz-Wielandt quotient is two-sided only at a strictly POSITIVE
    vector.  Each check names its direction.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime side
    is a finite zero-free sum over prime powers.
  * NO RH-EVIDENCE LANGUAGE: finite-window structure only; the
    value->spectral transport (I5) is untouched.

Status: [E] for (1)-(5) -- exact support / amplitude / bracket statements at
rel < 1e-9 .. 1e-15 as stated, each with a control that fails by >= 1e-3
relative or by an explicit count; [X] for (6), a certified negative result
about a whole family of bounds.  Python; Wolfram-mirrored (dense Cholesky /
eigenvalue and power-iteration work stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/long_lag_probe.py           (T137)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigvalsh

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in T128..T137
H_CAP = 300                  # HARD cap on any inverted / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

RHOS = (1.25, 1.49531, 2.0, 2.5, 3.0, 4.0)   # coarse/fine ratios of the seam
K_SCAN = 40                  # zones scanned (h <= H_CAP forces small windows)
N_INST = 20                  # frame-A seam windows
K_NEU = 8                    # Neumann partial sum length of (5)
POW_IT = 200                 # power-iteration steps for the |E| weight of (6)

# --- preregistered tolerances / bars (declared BEFORE any number) --------
TOL_SPLIT = 1.0e-14          # c == c_arch - c_comb (relative)
TOL_SIGN = 1.0e-12           # sign statements (relative to the matrix scale)
TOL_AMP = 1.0e-12            # the amplitude certificate (one-sided, relative)
TOL_ORTH = 1.0e-300          # stripe orthogonality is EXACT (disjoint support)
TOL_GREEN = 1.0e-11          # the Green bracket (one-sided, relative)
TOL_QJ = 1.0e-12             # the qJ identity (relative)
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard
BAR_ENV = 1.0                # the envelope family is dead iff rho(|E|) >= 1


def sym(A):
    return 0.5 * (A + A.T)


def rel(Dm, Rf):
    return float(np.abs(Dm).max()) / max(float(np.abs(Rf).max()), 1.0e-300)


def ast_zero_firewall(src_path: str) -> bool:
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr in (
                "zetazero", "nzeros", "second_sheet_zero",
            ):
                hits.append(f.attr)
            if isinstance(f, ast.Name) and f.id in ("zetazero", "nzeros"):
                hits.append(f.id)
        if isinstance(node, ast.Attribute) and node.attr in ("zetazero",):
            hits.append(node.attr)
    return not hits


# ---------------------------------------------------------------- atoms
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


ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


# --------------------------------- the archimedean kernel (Weil 1952, cited)
def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
               / (-np.expm1(-2.0 * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return ((tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w))
            / (-np.expm1(-2.0 * w)))


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
    """THE COMB HALF of the lag vector, ISOLATED: the sum of the atom hats.
    c = c_arch - c_comb exactly, by construction (T137 H0)."""
    out = np.zeros(M)
    hit = np.zeros(M, dtype=np.int64)          # how many hats reach a lag cell
    near = np.full(M, -1, dtype=np.int64)      # the index of the nearest atom
    ndst = np.full(M, np.inf)
    for j, (u_j, mu_j) in enumerate(atoms):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                out[i] += mu_j * 0.5 * v
                hit[i] += 1
                d = abs(i * D - u_j)
                if d < ndst[i]:
                    ndst[i], near[i] = d, j
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    out[i] += mu_j * 0.5 * v
                    hit[i] += 1
                    d = i * D + u_j
                    if d < ndst[i]:
                        ndst[i], near[i] = d, j
    one = np.zeros(M)                          # the ONE-ATOM (nearest) part
    for i in np.nonzero(hit > 0)[0]:
        u_j, mu_j = atoms[int(near[i])]
        v = max(0.0, 1.0 - abs(i * D - u_j) / D)
        vm = max(0.0, 1.0 - (i * D + u_j) / D) if u_j < D else 0.0
        one[i] = mu_j * 0.5 * (v + vm)
    return out, one, hit


def lag_vector_fast(alpha, M, atoms):
    """The T115 O(#atoms) lag assembly (frame-A code path of T128..T137)."""
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


# ------------------------------------- the reflection-odd sector (T106..T137)
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return (c[np.abs(r[:, None] - r[None, :])]
            - c[(M - 1) - r[:, None] - r[None, :]])


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


def border_schur(fr, c_n, tv):
    """The bordered step (Haynsworth 1968) and its border Schur block."""
    Q = sym(odd_toeplitz(c_n, fr["M_n"]) - np.outer(tv, tv))
    gc = fr["gc"]
    A = sym(np.ascontiguousarray(Q[:gc, :gc]))
    C = np.ascontiguousarray(Q[:gc, gc:])
    X = sym(np.ascontiguousarray(Q[gc:, gc:]))
    fac = safe_cho(X)
    if fac is None:
        return None
    return sym(A - C @ cho_solve(fac, C.T, check_finite=False))


# ------------------------------------------------- the lumped comparison
def lump_pair(A):
    """Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta
    its graph Laplacian, B = A + L_Delta the Stieltjes comparison (T136 P1,
    recomputed here so that this module stands alone)."""
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    LD = np.diag(Dl.sum(axis=1)) - Dl
    return dict(B=sym(A + LD), Dl=Dl, LD=LD,
                scale=max(float(np.abs(A).max()), 1.0e-300),
                n_pos=int(np.count_nonzero(Dl > 0.0)))


def stripes(Dl, M):
    """The anti-diagonal stripe decomposition of supp(Delta).  Returns the
    stripe index anti = M - 1 - r - t of every edge, sorted, plus the count of
    endpoint collisions inside a stripe (0 == a perfect matching)."""
    h = Dl.shape[0]
    iu = np.triu_indices(h, 1)
    w = Dl[iu]
    keep = w > 0.0
    er, et, w = iu[0][keep], iu[1][keep], w[keep]
    lab = (M - 1) - er - et
    coll = 0
    for a in np.unique(lab):
        m = lab == a
        ends = np.concatenate([er[m], et[m]])
        coll += ends.shape[0] - np.unique(ends).shape[0]
    return dict(er=er, et=et, w=w, lab=lab, n=er.shape[0], coll=int(coll),
                nb=int(np.unique(lab).shape[0]))


def green_bracket(B, kmax=K_NEU):
    """(5) the Neumann partial sum from BELOW and the anchor-weighted tail
    from ABOVE, both ENTRYWISE, for a Stieltjes comparison B."""
    g = B.shape[0]
    d0 = np.diag(B).copy()
    N0 = np.diag(d0) - B
    if not (bool(np.all(d0 > 0.0)) and bool(np.all(N0 >= -1.0e-300))):
        return None
    fac = safe_cho(B)
    if fac is None:
        return None
    Gi = cho_solve(fac, np.eye(g), check_finite=False)
    x = Gi.sum(axis=1)
    if float(np.min(x)) <= 0.0:
        return None
    J = N0 / d0[:, None]
    LB = np.zeros((g, g))
    Jk = np.eye(g)
    for kk in range(0, kmax + 1):
        LB += Jk / d0[None, :]
        if kk < kmax:
            Jk = Jk @ J
    qJ = float(np.max((J @ x) / x))
    qJ_id = 1.0 - float(np.min(1.0 / (d0 * x)))
    if not (qJ < 1.0):
        return None
    tail = ((x[:, None] / x[None, :]) * (qJ ** (kmax + 1) / (1.0 - qJ))
            / d0[None, :])
    scale = max(float(np.abs(Gi).max()), 1.0e-300)
    return dict(g=g, qJ=qJ, qJ_res=abs(qJ - qJ_id) / max(qJ, 1.0e-300),
                lo_res=float((LB - Gi).max()) / scale,
                up_res=float((Gi - (LB + tail)).max()) / scale,
                notail=float((Gi - LB).max()) / scale,
                inv_min=float(Gi.min()) / scale,
                lb_tight=float(np.min(LB)) / max(float(np.min(Gi)), 1.0e-300))


def cw_lower(T, iters=POW_IT):
    """A RIGOROUS Collatz-Wielandt LOWER bound for rho(T), T >= 0: for ANY
    strictly positive w, min_r (T w)_r / w_r <= rho(T).  The weight is
    power-iterated (a measurement); the resulting bound is rigorous."""
    n = T.shape[0]
    w = np.ones(n)
    for _ in range(iters):
        v = T @ w
        nv = float(np.abs(v).max())
        if not (nv > 0.0):
            return 0.0, 0.0
        w = v / nv
        w = np.maximum(w, 1.0e-30 * float(w.max()))
    q = (T @ w) / w
    return float(np.min(q)), float(np.max(q))


# ------------------------------------------------------------------ battery
def build_instances():
    """Frame-A seam windows kept small enough that EVERY factorised /
    diagonalised matrix stays <= H_CAP.  Each carries the kernel split, the
    POLE-FREE odd section and the border Schur block of the same seam."""
    cand = []
    for k in range(1, min(K_SCAN, len(UU_ALL) - 1)):
        u_o, u_n = UU_ALL[k], UU_ALL[k + 1]
        g = u_n - u_o
        if g <= 0.0:
            continue
        D_c = 0.5 * g / NU_MAIN
        for rho in RHOS:
            fr = step_frame(u_o, u_n, D_c / rho)
            if fr is None or fr["gc"] < 3:
                continue
            if fr["h_n"] > H_CAP or fr["h_n"] < H_MIN:
                continue
            cand.append((fr["h_n"], k, rho, fr))
    cand.sort(key=lambda r: (r[0], r[1], r[2]))
    if len(cand) > N_INST:
        pick = [cand[round(j * (len(cand) - 1) / (N_INST - 1))]
                for j in range(N_INST)]
    else:
        pick = cand
    out = []
    for _, k, rho, fr in pick:
        M, alpha = fr["M_n"], fr["al_n"]
        at = atoms_in(alpha)
        c, D = lag_vector_fast(alpha, M, at)
        c_ar = arch_lags(M, D)
        c_cb, c_one, hit = comb_lags(M, D, at)
        A = sym(odd_toeplitz(c, M))
        tv = odd_pole_vector(alpha, M)
        S = border_schur(fr, c, tv)
        out.append(dict(n=NN_ALL[k + 1], rho=rho, fr=fr, M=M, D=D, h=fr["h_n"],
                        gc=fr["gc"], c=c, c_ar=c_ar, c_cb=c_cb, c_one=c_one,
                        hit=hit, A=A, S=S, n_at=len(at),
                        split=rel(c - (c_ar - c_cb), c)))
    return out


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v544  PRIME.LONGLAG.SUPP.01 -- the long-lag support structure "
          "(T137)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, the exact kernel split")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = build_instances()
    check(f"S0.INST: {len(INST)} frame-A seam windows built "
          f"(h = {min(t['h'] for t in INST)}..{max(t['h'] for t in INST)} "
          f"<= {H_CAP}, gc >= 3, {min(t['n_at'] for t in INST)}.."
          f"{max(t['n_at'] for t in INST)} prime-power atoms)",
          len(INST) >= 8)
    sp = max(t["split"] for t in INST)
    check(f"S0.SPLIT: c == c_arch - c_comb exactly on all {len(INST)} windows "
          f"(max rel {sp:.2e} < {TOL_SPLIT:.0e}) and c_comb >= 0 everywhere",
          sp < TOL_SPLIT
          and all(float(t["c_cb"].min()) >= 0.0 for t in INST))
    for t in INST:
        print(f"    n={t['n']:>7d} rho={t['rho']:.5f} h={t['h']:>4d} "
              f"gc={t['gc']:>3d} atoms={t['n_at']:>3d} "
              f"comb cells={int(np.count_nonzero(t['c_cb'] > 0.0)):>4d}")

    PAIR = [(t, lump_pair(t["A"])) for t in INST]
    PAIR = [(t, pr) for t, pr in PAIR if pr["n_pos"] > 0]
    check(f"S0.POS: {len(PAIR)} of {len(INST)} sections carry POSITIVE "
          f"off-diagonals (up to {max(pr['n_pos'] for _, pr in PAIR)} "
          f"entries) -- the structure question is only content where they do",
          len(PAIR) >= 8)

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the archimedean half carries NO positive off-diagonal")
    ar_max, ful_max = -np.inf, -np.inf
    for t, pr in PAIR:
        A_ar = sym(odd_toeplitz(t["c_ar"], t["M"]))
        offd = A_ar - np.diag(np.diag(A_ar))
        sc = max(float(np.abs(A_ar).max()), 1.0e-300)
        ar_max = max(ar_max, float(offd.max()) / sc)
        off_f = t["A"] - np.diag(np.diag(t["A"]))
        ful_max = max(ful_max, float(off_f.max())
                      / max(float(np.abs(t["A"]).max()), 1.0e-300))
    check(f"S1.ARCH: the archimedean section A^arch has ALL off-diagonals "
          f"<= 0 on all {len(PAIR)} windows (max off-diagonal {ar_max:.2e} "
          f"relative < {TOL_SIGN:.0e}), so EVERY positive off-diagonal of A "
          f"is comb-generated", ar_max < TOL_SIGN)
    check(f"S1.CTRL: the FULL section does have positive off-diagonals (max "
          f"{ful_max:.2e} relative > {BAR_CTRL:.0e}), so the statement is not "
          f"vacuous", ful_max > BAR_CTRL)

    # ------------------------------------------------------------ (2), (3)
    print("\nS2 -- (2) supp(Delta) = anti-diagonal comb stripes at the atoms")
    STR = [(t, pr, stripes(pr["Dl"], t["M"])) for t, pr in PAIR]
    frac_min, n_edge, n_str, coll = 1.0, 0, 0, 0
    for t, _, st in STR:
        on = t["c_cb"][st["lab"]] > 0.0
        frac_min = min(frac_min, float(on.mean()))
        n_edge += st["n"]
        n_str += st["nb"]
        coll += st["coll"]
    load = [st["nb"] / max(int(np.count_nonzero(t["c_cb"] > 0.0)), 1)
            for t, _, st in STR]
    check(f"S2.SUPPORT: EVERY one of the {n_edge} positive off-diagonal edges "
          f"over the battery has its Hankel index anti = M - 1 - r - t inside "
          f"the atom-hat index set (minimum per-window fraction "
          f"{frac_min:.6f} == 1.0)", frac_min >= 1.0)
    check(f"S2.CONVERSE-NOT-CLAIMED: the reverse inclusion is REPORTED, not "
          f"claimed -- {n_str} loaded stripes over the battery, a fraction "
          f"{min(load):.3f} .. {max(load):.3f} of the comb cells",
          max(load) <= 1.0 + 1.0e-12)

    print("\nS3 -- (3) each stripe is a PERFECT MATCHING (orthogonal edges)")
    orth, cross = 0.0, 0.0
    for t, _, st in STR:
        for a in np.unique(st["lab"]):
            m = np.flatnonzero(st["lab"] == a)
            if m.size < 2:
                continue
            Bm = np.zeros((t["h"], m.size))
            Bm[st["er"][m], np.arange(m.size)] = 1.0
            Bm[st["et"][m], np.arange(m.size)] = -1.0
            Gm = Bm.T @ Bm
            orth = max(orth, float(np.abs(Gm - np.diag(np.diag(Gm))).max()))
        lbs = np.unique(st["lab"])
        if lbs.size >= 2:
            m0 = np.flatnonzero(st["lab"] == lbs[0])
            m1 = np.flatnonzero(st["lab"] == lbs[1])
            b0 = np.zeros(t["h"])
            b0[st["er"][m0[0]]], b0[st["et"][m0[0]]] = 1.0, -1.0
            for i in m1:
                b1 = np.zeros(t["h"])
                b1[st["er"][i]], b1[st["et"][i]] = 1.0, -1.0
                cross = max(cross, abs(float(np.dot(b0, b1))))
    check(f"S3.MATCHING: no index occurs twice inside a stripe on the whole "
          f"battery ({coll} collisions over {n_edge} edges and {n_str} "
          f"stripes) -- each stripe is a perfect matching", coll == 0)
    check(f"S3.ORTHOGONAL: therefore the edge vectors b_e = e_r - e_t of one "
          f"stripe are EXACTLY orthogonal (max off-diagonal Gram entry "
          f"{orth:.1e}), so L_Delta restricted to a stripe is a direct sum of "
          f"2x2 blocks", orth <= TOL_ORTH)
    check(f"S3.CTRL: edges taken ACROSS two stripes are NOT orthogonal (max "
          f"overlap {cross:.1f} >= 1), so the stripe decomposition is what "
          f"carries the orthogonality", cross >= 1.0)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the amplitude certificate  Delta_rt <= c_comb[anti]")
    amp_max, one_vio, one_tot, amp_tight = -np.inf, 0, 0, 0.0
    tpl_vio, hit_max = 0, 0
    for t, _, st in STR:
        sc = max(float(np.abs(t["A"]).max()), 1.0e-300)
        cap = t["c_cb"][st["lab"]]
        amp_max = max(amp_max, float((st["w"] - cap).max()) / sc)
        amp_tight = max(amp_tight, float((st["w"] / np.maximum(cap, 1.0e-300))
                                         .max()))
        cap1 = t["c_one"][st["lab"]]
        one_vio += int(np.count_nonzero(st["w"] > cap1 * (1.0 + 1.0e-9)))
        one_tot += st["n"]
        hit_max = max(hit_max, int(t["hit"].max()))
        tpl = t["c_cb"][np.abs(st["er"] - st["et"])]
        tpl_vio += int(np.count_nonzero(st["w"] > tpl * (1.0 + 1.0e-9)))
    check(f"S4.AMPLITUDE: Delta_rt <= c_comb[anti(r,t)] on ALL {n_edge} edges "
          f"of the battery (max one-sided excess {amp_max:.2e} relative < "
          f"{TOL_AMP:.0e}; sharpest ratio {amp_tight:.8f}) -- no eigenvalue, "
          f"no norm", amp_max < TOL_AMP)
    check(f"S4.CTRL: replacing the ANTI-DIAGONAL index by the TOEPLITZ lag "
          f"|r - t| breaks the certificate on {tpl_vio} of {n_edge} edges, so "
          f"it is the Hankel index that carries the amplitude",
          tpl_vio > n_edge // 2)
    check(f"S4.ONE-ATOM-UNDECIDED: on this battery the atom hats do NOT "
          f"overlap (at most {hit_max} hat per lag cell), so the tighter "
          f"ONE-ATOM version coincides with the certificate here "
          f"({one_vio} violations of {one_tot}) and is NEITHER confirmed NOR "
          f"refuted -- the T137 overlap violation lives at depth and is NOT "
          f"promoted", hit_max == 1 and one_vio == 0)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the Green function of the lumped comparison, bracketed")
    GRN = []
    for t, pr in PAIR:
        gb = green_bracket(pr["B"])
        if gb is not None:
            GRN.append(("section", t, gb))
        if t["S"] is not None and t["S"].shape[0] >= 3:
            prS = lump_pair(t["S"])
            if prS["n_pos"] > 0:
                gs = green_bracket(prS["B"])
                if gs is not None:
                    GRN.append(("border", t, gs))
    qj_res = max(gb["qJ_res"] for _, _, gb in GRN)
    lo_res = max(gb["lo_res"] for _, _, gb in GRN)
    up_res = max(gb["up_res"] for _, _, gb in GRN)
    nt_min = min(gb["notail"] for _, _, gb in GRN)
    inv_min = min(gb["inv_min"] for _, _, gb in GRN)
    n_bd = sum(1 for tag, _, _ in GRN if tag == "border")
    check(f"S5.ROWS: {len(GRN)} lumped comparisons bracketed ({len(GRN)-n_bd} "
          f"pole-free sections + {n_bd} border Schur blocks); every inverse is "
          f"entrywise nonnegative (min relative entry {inv_min:.2e})",
          len(GRN) >= 10 and inv_min >= -1.0e-13)
    check(f"S5.QJ: qJ = max_r (Jx)_r/x_r == 1 - min_r 1/(d_r x_r) exactly on "
          f"all {len(GRN)} rows (max rel {qj_res:.2e} < {TOL_QJ:.0e}), so "
          f"qJ < 1 follows from B x = 1 > 0 and needs no measurement",
          qj_res < TOL_QJ)
    check(f"S5.BELOW: the Neumann partial sum to K = {K_NEU} is an ENTRYWISE "
          f"lower bound for B^-1 on all {len(GRN)} rows (max one-sided excess "
          f"{lo_res:.2e} relative) -- a bound because the discarded terms are "
          f"NONNEGATIVE, not because a truncation error is small",
          lo_res < TOL_GREEN)
    check(f"S5.ABOVE: partial sum + anchor-weighted tail is an ENTRYWISE "
          f"upper bound on all {len(GRN)} rows (max one-sided excess "
          f"{up_res:.2e} relative)", up_res < TOL_GREEN)
    check(f"S5.CTRL: dropping the tail term makes the upper bound FALSE (the "
          f"partial sum alone stays below B^-1 by at least {nt_min:.2e} "
          f"relative on every row, > {BAR_CTRL:.0e})", nt_min > BAR_CTRL)

    # ---------------------------------------------------------------- (6)
    print("\nS6 -- (6) the |E|-envelope family, certified DEAD")
    ENV = []
    for t, pr in PAIR:
        fac = safe_cho(pr["B"])
        if fac is None:
            continue
        Gi = cho_solve(fac, np.eye(pr["B"].shape[0]), check_finite=False)
        E = Gi @ pr["LD"]
        Ea = np.abs(E)
        lo, up = cw_lower(Ea)
        x = Gi.sum(axis=1)
        rows = dict(cw_lo=lo, cw_up=up,
                    inf=float(Ea.sum(axis=1).max()),
                    gersh=float(np.abs(np.diag(Ea)).max()
                                + (Ea.sum(axis=1) - np.diag(Ea)).max()),
                    cw_x=float(np.max((Ea @ x) / x)),
                    cw_one=float(np.max(Ea @ np.ones(Ea.shape[0]))),
                    rho_signed=float(np.abs(np.linalg.eigvals(E)).max()),
                    lam_A=float(eigvalsh(t["A"])[0]))
        ENV.append((t, rows))
    cw_lo_min = min(r["cw_lo"] for _, r in ENV)
    fam_min = min(min(r["inf"], r["gersh"], r["cw_x"], r["cw_one"])
                  for _, r in ENV)
    sg_max = max(r["rho_signed"] for _, r in ENV)
    n_pd = sum(1 for _, r in ENV if r["lam_A"] > 0.0)
    check(f"S6.ROWS: {len(ENV)} envelopes built; the SIGNED radius rho(E) = "
          f"lam_max(W) stays below 1 on all of them (max {sg_max:.8f}) and the "
          f"section is positive definite on {n_pd} of {len(ENV)} -- the two "
          f"facts the envelope has to reproduce and cannot",
          len(ENV) >= 8 and sg_max < 1.0 and n_pd == len(ENV))
    check(f"S6.DEATH: a Collatz-Wielandt quotient FROM BELOW at a "
          f"power-iterated positive weight gives rho(|E|) >= "
          f"{cw_lo_min:.4f} >= {BAR_ENV:.2f} on EVERY row, so no Gershgorin, "
          f"row-sum or Collatz-Wielandt bound at ANY positive weight can ever "
          f"certify lam_max(W) < 1 -- a certificate of DEATH for the whole "
          f"absolute-value envelope family, not a measurement",
          cw_lo_min >= BAR_ENV)
    check(f"S6.FAMILY: consistently, the cheapest four members of the family "
          f"(row-sum norm, Gershgorin, Collatz-Wielandt at the anchor vector "
          f"and at 1) are all >= {fam_min:.4f} >= 1 on every row",
          fam_min >= BAR_ENV)
    check(f"S6.CAUSE: the SAME quantity WITHOUT the absolute value sits below "
          f"1 (rho(E) <= {sg_max:.8f}), so the absolute value alone destroys "
          f"the cancellation -- what survives is a SIGN-PRESERVING bound, "
          f"which does not exist yet", sg_max < 1.0 <= cw_lo_min)

    # ---------------------------------------------------------------- fences
    print("\nS7 -- the fences, restated as a check")
    check("S7.FENCE: PER-INSTANCE statements on SMALL windows only -- nothing "
          "uniform in the zone index, in D or in the gap, no decay profile "
          "and no amplitude LAW (T137's decay measurements are FITS and stay "
          "in the sandbox); (2) is ONE inclusion, the converse is reported "
          "and not claimed; (4) bounds the AMPLITUDE and NOT lam_max(W) -- "
          "the structure bound assembled from (2)-(4) does NOT beat the "
          "margin and is NOT promoted; (5) brackets the Green function of the "
          "LUMPED comparison B, not of the target, and entrywise positivity "
          "of the target inverse at depth stays OPEN; (6) is a NEGATIVE "
          "result closing a ROUTE, not the question, and moves no marker in "
          "either direction; Stieltjes / Ostrowski 1937 / Fan 1958 / "
          "Berman-Plemmons 1979 / Varga 1962 / Collatz 1942 / Wielandt 1950 / "
          "Gershgorin 1931 / Neumann series / Haynsworth 1968 named "
          "CLASSICAL, Demko-Moss-Smith 1984 CITED as a model and NOT applied "
          "(the comparison is dense); Weil 1952 CITED, never used as a "
          "criterion; zero-firewall AST-checked; NO marker upgrade of any "
          "pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv544 runtime: {elapsed:.1f}s")
    print(f"  (1) arch half: max off-diagonal {ar_max:.1e} on {len(PAIR)} "
          f"windows (full section {ful_max:.1e})")
    print(f"  (2) support: {n_edge} edges, all on comb stripes "
          f"(fraction {frac_min:.6f}), {n_str} loaded stripes")
    print(f"  (3) matching: {coll} collisions, stripe Gram off-diagonal "
          f"{orth:.1e}, cross-stripe overlap {cross:.1f}")
    print(f"  (4) amplitude: excess {amp_max:.1e}, sharpest "
          f"{amp_tight:.8f}; Toeplitz-index control violated "
          f"{tpl_vio}/{n_edge}, one-atom version UNDECIDED (no hat overlap)")
    print(f"  (5) Green bracket: qJ identity {qj_res:.1e}, below {lo_res:.1e},"
          f" above {up_res:.1e} on {len(GRN)} rows")
    print(f"  (6) envelope: rho(|E|) >= {cw_lo_min:.4f} vs rho(E) <= "
          f"{sg_max:.8f} -- family DEAD")
    return summary("PRIME.LONGLAG.SUPP.01 long-lag support structure")


if __name__ == "__main__":
    raise SystemExit(run())
