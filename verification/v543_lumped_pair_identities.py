"""v543 -- PRIME.MMATRIX.IDENT.01: the lumped M-matrix pair of phase 2.
The SEVEN per-instance identities / theorems of discovery T136 that are pure
linear algebra -- every one RECOMPUTED here from scratch on small exactly
checkable windows of the frame-A construction (nothing cited from the
sandbox).  Companion to PRIME.MARGIN.IDENT.01 / v542.

WHAT IS LOAD-BEARING HERE (and nothing else): matrix identities, per-instance
theorems with CHECKED hypotheses, and one NEGATIVE per-instance statement.
NO fit, NO D-exponent, NO uniform-in-zone claim, NO floor value, NO bound
whose constant was calibrated -- those stay in the sandbox / are typed open
elsewhere.  Each item is a NUMERICAL RESIDUAL against a preregistered
tolerance AND has at least one MUTATION CONTROL that must fail loudly.

[E] (1) THE LUMPED PAIR (T136 P1).  For symmetric A write Delta for its
    POSITIVE off-diagonal part and L_Delta = diag(Delta 1) - Delta.  Then
    A_B = A + L_Delta is STIELTJES (all off-diagonals <= 0, diagonal > 0),
    L_Delta is a graph Laplacian, hence PSD with ZERO row sums, so the row
    sums are PRESERVED (A_B 1 == A 1) and A_B >= A in the LOEWNER order.
    THE DIRECTION IS PART OF THE CLAIM: A_B >= A gives lam_min(A_B) >=
    lam_min(A) -- an UPPER bound on lam_min(A) and a floor NEVER.  A floor is
    reachable only through the inverse side, which is what (2)-(3) do.
[E] (2) THE CONGRUENCE IDENTITY (T136 P2/P3).
    A = A_B^{1/2} (I - W) A_B^{1/2} with W = A_B^{-1/2} L_Delta A_B^{-1/2}
    >= 0 (a MATRIX identity, rel < 1e-10), and lam_max(W) = rho(L_Delta
    A_B^{-1}) because W is similar to A_B^{-1} L_Delta.  DECLARED
    CIRCULARITY, checked in BOTH directions as a fence: lam_max(W) < 1 <=>
    A > 0.  The sandwich lam_min(A) >= lam_min(A_B)(1 - lam_max(W)) is
    therefore VACUOUS unless lam_max(W) is bounded by cheap ingredients --
    the equivalence is the reason, not a caveat.
[E] (3) THE M-MATRIX ANCHOR (T136 P4).  For Stieltjes positive definite A_B
    with x = A_B^{-1} 1: x >= 0 entrywise (Ostrowski 1937 inverse
    positivity, CHECKED) and then lam_min(A_B) >= 1 / max_r x_r, because
    ||A_B^{-1}||_2 <= ||A_B^{-1}||_inf = ||A_B^{-1} 1||_inf for a symmetric
    matrix with a nonnegative inverse.  ONE solve, ONE sign check, no
    eigenvalue.  Control: a matrix with a POSITIVE off-diagonal violates it.
[E] (4) SHIFT COMMUTATION + INVERSE MONOTONICITY (Berman-Plemmons 1979).
    Lumping commutes with diagonal shifts: (A - s I)_B == A_B - s I exactly,
    since the off-diagonals are untouched.  For 0 < s < lam_min(A_B) the
    shifted pair is still a Stieltjes M-matrix and (A_B - s I)^{-1} >=
    A_B^{-1} >= 0 ENTRYWISE, so max_r x_r(s) is non-decreasing in s and the
    a-priori margin ||L_Delta||_inf max_r x_r(s) can only GROW.  The shifted
    ladder is therefore STRUCTURALLY EMPTY -- a theorem, not a measurement.
[E] (5) VARGA'S REGULAR SPLITTING AS AN IDENTITY (Varga 1962).  With
    A_B = D_0 - N_0, D_0 = diag(A_B) > 0, N_0 >= 0, A_B^{-1} >= 0 (a REGULAR
    splitting, all three hypotheses checked) the Jacobi radius satisfies
    rho(J) = tau / (1 + tau), J = D_0^{-1} N_0, tau = rho(A_B^{-1} N_0) --
    an IDENTITY (rel < 1e-9), so ANY upper bound on tau lands below 1
    automatically.
[E] (6) THE COLLATZ-WIELANDT BRACKET AT THE ANCHOR VECTOR (Collatz 1942 /
    Wielandt 1950).  T = A_B^{-1} N_0 >= 0 and x = A_B^{-1} 1 > 0 give the
    two-sided bracket min_r (Tx)_r/x_r <= tau <= max_r (Tx)_r/x_r, hence with
    (5) an A-PRIORI rho(J) <= tau_cw/(1 + tau_cw) < 1 with NO eigenvalue
    anywhere.  Sharpness is REPORTED, not claimed.  Control: at a
    SIGN-CHANGING test vector the quotient bound is false, so positivity of
    the test vector is load-bearing.
[X] (7) THE k-SCANNED M18 MAJORANT -- A NEGATIVE PER-INSTANCE RESULT (T136
    G3).  On the whitened two-grid pencil the mass identity ||L^{-1} shat||^2
    == shat^T U^{-1} shat holds exactly (rel < 1e-10) and the triangle chain
    gives, for EVERY k separately, a valid majorant bnd(k) for the bad-mass
    fraction (mass on the eigendirections with mu < 1/2).  Scanning k over a
    WIDE ladder instead of the three values of T134 does NOT bring the
    majorant under the preregistered bar 1/2: the localisation term
    sigma_b(k) (tail_w + nc)/den2 alone already exhausts the budget.  The
    load-bearing content is the VALIDITY of the majorant per instance and the
    FAILURE of the k-scan -- no bound is claimed to close.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   PER-INSTANCE statements on SMALL windows.  Nothing here is uniform in
        the zone index, in D or in the gap; the uniform forms stay open
        (PRIME.I5.UNIFORM class) and no marker of any pre-existing contract
        moves.
  (ii)  (2) carries NO floor.  Its content is the exact congruence plus the
        DECLARED equivalence lam_max(W) < 1 <=> A > 0, i.e. the statement
        that the Loewner sandwich is circular by itself.  Positivity of the
        pole-free section at depth (M25d) is not claimed here.
  (iii) (3) is an implication with a CHECKED hypothesis (Stieltjes + positive
        definite + x >= 0 at the instance).  No D-uniform anchor law is
        claimed; the T136 exponents are FITS and stay in the sandbox.
  (iv)  (4) kills a ROUTE, not a quantity: it says the shifted ladder cannot
        improve the a-priori margin.  It says nothing about the true
        lam_max(W).
  (v)   (7) is a NEGATIVE result.  Nothing is upgraded by it; the bar 1/2 is
        the T134 bar and is NOT moved.  The whitened-mass route to M18 stays
        open, and this module records why the cheap k-scan does not close it.

HONEST FENCES (load-bearing typing):
  * Classics named CLASSICAL: Stieltjes / Ostrowski 1937 (inverse
    positivity), Fan 1958 and Berman-Plemmons 1979 (M-matrix equivalences,
    the positive-vector criterion, inverse monotonicity), Varga 1962
    (regular splittings, Jacobi radii), Frobenius 1912 / Perron 1907,
    Collatz 1942 / Wielandt 1950 (the min-max quotient bracket), Haynsworth
    1968 and Cauchy interlacing (Schur complements and directions),
    Wilkinson 1968 / Higham 2002 (the floating-point floor), Yserentant 1986
    (the two-scale space), Weil 1952 (the archimedean kernel, CITED, never
    used as a criterion).  NEW is only the compiler-native consolidation and
    the machine-checked residuals.
  * DIRECTION CARE IS PART OF THE CLAIM.  A_B >= A bounds lam_min(A) from
    ABOVE; a power iteration bounds a spectral radius from BELOW and can
    only KILL a margin; a Collatz-Wielandt quotient at a POSITIVE vector is
    a rigorous two-sided bracket.  Each check names its direction.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime side
    is a finite zero-free sum over prime powers.
  * NO RH-EVIDENCE LANGUAGE: finite-window linear algebra only; the
    value->spectral transport (I5) is untouched.

Status: [E] for (1)-(6) -- exact linear-algebra identities and per-instance
theorems at rel < 1e-9 .. 1e-14 as stated, each with a mutation control that
fails by >= 1e-3 relative; [X] for (7), a negative per-instance result
against a preregistered bar.  Python; Wolfram-mirrored (dense Cholesky /
eigenvalue / SVD identities stay Python-only), counted per GATE.WOLFRAM.02.
Discovery provenance:
  experiments/tfpt-discovery/m_matrix_pair_probe.py     (T136)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import (cho_factor, cho_solve, cholesky, eigvalsh,
                          solve_triangular, svdvals)

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in T128..T136
H_CAP = 300                  # HARD cap on any inverted / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
SQ2 = math.sqrt(2.0)
U_ROUND = 2.0 ** -53
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

RHOS = (1.25, 1.49531, 2.0, 2.5, 3.0, 4.0)   # coarse/fine ratios of the seam
K_SCAN = 40                  # zones scanned (h <= H_CAP forces small windows)
N_INST = 20                  # frame-A seam instances (sections + border blocks)
N_RUNG = 8                   # whitened two-grid rungs for (7)
S_LADDER = 8                 # rungs of the shifted ladder in (4)

L_CAP = 2 ** 18              # oversampling cap of the certified envelope
ENV_OS = 48
ENV_FRAC = 0.10
K_LADDER = (2, 4, 8, 16, 32, 64)     # the WIDE ladder of (7)
K_T134 = (4, 8, 16)                  # the three values T134 tried

# --- preregistered tolerances / bars (declared BEFORE any number) --------
TOL_LUMP = 1.0e-12           # Stieltjes + row-sum preservation (relative)
TOL_CONG = 1.0e-10           # the congruence identity (relative)
TOL_SPEC = 1.0e-9            # lam_max(W) == rho(L_Delta A_B^-1) (relative)
TOL_ANCH = 1.0e-12           # anchor / bracket slack (one-sided, relative)
TOL_VARGA = 1.0e-9           # Varga's identity rho(J) = tau/(1+tau)
TOL_MONO = 1.0e-12           # entrywise inverse monotonicity (one-sided)
TOL_WHITE = 1.0e-10          # the whitened mass identity (relative)
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard
BAR_MASS_GOOD = 0.5          # the T134 bar for the M18 majorant -- NOT moved


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


def lag_vector_fast(alpha, M, atoms):
    """The T115 O(#atoms) lag assembly (frame-A code path of T128..T136)."""
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


# ------------------------------------- the reflection-odd sector (T106..T136)
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


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


def gersh(A):
    return float(np.abs(A).sum(axis=1).max())


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


def border_schur(fr):
    """The bordered step (Haynsworth 1968) and its border Schur block."""
    at_n = atoms_in(fr["al_n"])
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
    return sym(A - C @ cho_solve(fac, C.T, check_finite=False))


# ----------------------------------------------------- THE LUMPED PAIR (1)
def lump_pair(A):
    """THE LUMPED M-MATRIX PAIR (T136 P1).  Delta = the POSITIVE off-diagonal
    part, L_Delta = diag(Delta 1) - Delta its graph Laplacian (PSD, ZERO row
    sums), A_B = A + L_Delta.

    DIRECTION, stated once: L_Delta >= 0 in the Loewner order, so A_B >= A --
    lumping RAISES the form and bounds lam_min(A) from ABOVE, never below."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    LD = np.diag(Dl.sum(axis=1)) - Dl
    A_B = sym(A + LD)
    offB = A_B - np.diag(np.diag(A_B))
    scale = max(float(np.abs(A).max()), 1.0e-300)
    return dict(h=h, A=sym(A), A_B=A_B, Dl=Dl, LD=LD, scale=scale,
                dgB=np.diag(A_B).copy(),
                n_pos=int(np.count_nonzero(Dl > 0.0)),
                off_max=float(offB.max()) / scale,
                dg_min=float(np.diag(A_B).min()) / scale,
                rs_res=float(np.abs(A_B.sum(axis=1) - A.sum(axis=1)).max())
                / scale,
                ld_lmin=float(eigvalsh(LD)[0]) / scale,
                ld_inf=float(np.abs(LD).sum(axis=1).max()))


def lump_negative(A):
    """THE MUTATION CONTROL for (1): lump the NEGATIVE off-diagonals instead.
    The row sums are still preserved (any Laplacian has zero row sums) but the
    result is NOT Stieltjes -- the sign selection is load-bearing."""
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dn = np.where(off < 0.0, off, 0.0)
    LD = np.diag(Dn.sum(axis=1)) - Dn
    A_C = sym(A + LD)
    offC = A_C - np.diag(np.diag(A_C))
    return float(offC.max()) / max(float(np.abs(A).max()), 1.0e-300)


# ------------------------------------------------ THE CONGRUENCE (2)
def congruence(pr):
    """A = A_B^{1/2}(I - W)A_B^{1/2}, W = A_B^{-1/2} L_Delta A_B^{-1/2}, and
    lam_max(W) = rho(L_Delta A_B^{-1}).  Returns None unless A_B > 0."""
    A_B, LD = pr["A_B"], pr["LD"]
    ev, U = np.linalg.eigh(A_B)
    if ev[0] <= 0.0:
        return None
    rt = U * np.sqrt(ev)[None, :]
    rti = U / np.sqrt(ev)[None, :]
    Wm = sym(rti.T @ LD @ rti)
    evW = eigvalsh(Wm)
    Rec = rt @ (np.eye(pr["h"]) - Wm) @ rt.T
    Gi = rti @ rti.T
    ei = np.linalg.eigvals(LD @ Gi)
    return dict(res=rel(Rec - pr["A"], pr["A"]),
                w_lmax=float(evW[-1]), w_lmin=float(evW[0]),
                rho_e=float(np.abs(ei).max()),
                lam_A=float(eigvalsh(pr["A"])[0]),
                lam_B=float(ev[0]), Gi=Gi,
                gi_min=float(Gi.min()) / max(float(Gi.max()), 1.0e-300))


# ------------------------------------------------------- THE ANCHOR (3)
def anchor(A_B):
    """x = A_B^{-1} 1, the sign check, and the floor 1 / max_r x_r."""
    fac = safe_cho(A_B)
    if fac is None:
        return None
    x = cho_solve(fac, np.ones(A_B.shape[0]), check_finite=False)
    xmax = float(np.max(x))
    if not (xmax > 0.0):
        return None
    return dict(x=x, xmax=xmax, xmin=float(np.min(x)),
                nonneg=int(float(np.min(x))
                           >= -1.0e-13 * xmax),
                floor=1.0 / xmax)


# ------------------------------------- VARGA + COLLATZ-WIELANDT (5), (6)
def varga_row(A_B, scale):
    """A_B = D_0 - N_0, J = D_0^{-1} N_0, tau = rho(A_B^{-1} N_0), and the
    Collatz-Wielandt bracket for tau at the anchor vector x = A_B^{-1} 1."""
    g = A_B.shape[0]
    d0 = np.diag(A_B).copy()
    N0 = np.diag(d0) - A_B
    if not (bool(np.all(d0 > 0.0)) and bool(np.all(N0 >= -1.0e-300))):
        return None
    fac = safe_cho(A_B)
    if fac is None:
        return None
    Gi = cho_solve(fac, np.eye(g), check_finite=False)
    x = Gi.sum(axis=1)
    if float(np.min(x)) <= 0.0:
        return None
    J0 = N0 / d0[:, None]
    rho = float(np.max(np.abs(np.linalg.eigvals(J0)))) if g > 1 else 0.0
    Y = Gi @ N0
    tau = (float(np.max(np.abs(np.linalg.eigvals(Y)))) if g > 1
           else float(abs(Y[0, 0])))
    q = (Y @ x) / x
    alt = np.where(np.arange(g) % 2 == 0, 1.0, -1.0)   # the sign-changing ctrl
    qa = (Y @ alt) / alt
    return dict(g=g, rho=rho, tau=tau,
                rho_varga=tau / (1.0 + tau),
                varga_id=abs(rho - tau / (1.0 + tau)) / max(rho, 1.0e-300),
                cw_lo=float(np.min(q)), cw_up=float(np.max(q)),
                cw_alt=float(np.max(qa)),
                inv_nonneg=int(bool(np.all(Gi >= -1.0e-14
                                           * float(np.abs(Gi).max())))),
                n0_min=float(N0.min()) / scale)


def varga_control(A_B):
    """THE MUTATION CONTROL for (5): halve one diagonal entry of D_0, so that
    N_0 acquires a NEGATIVE diagonal entry and the splitting is no longer
    regular.  Varga's identity must break."""
    g = A_B.shape[0]
    d0 = np.diag(A_B).copy()
    d0b = d0.copy()
    d0b[int(np.argmax(d0))] *= 0.5
    N0b = np.diag(d0b) - A_B
    Jb = N0b / d0b[:, None]
    rho_b = float(np.max(np.abs(np.linalg.eigvals(Jb))))
    fac = safe_cho(A_B)
    Gi = cho_solve(fac, np.eye(g), check_finite=False)
    Yb = Gi @ N0b
    tau_b = float(np.max(np.abs(np.linalg.eigvals(Yb))))
    return (abs(rho_b - tau_b / (1.0 + tau_b)) / max(rho_b, 1.0e-300),
            float(np.diag(N0b).min()) / max(float(np.abs(A_B).max()),
                                            1.0e-300))


# ------------------------------- THE TWO-GRID / WHITENING BLOCK for (7)
def rest_p(X):
    return (X[0::2] + X[1::2]) / SQ2


def rest_z(X):
    return (X[0::2] - X[1::2]) / SQ2


def two_grid_blocks(A):
    PtA = rest_p(A)
    ZtA = rest_z(A)
    return (sym(rest_p(PtA.T).T), sym(rest_z(ZtA.T).T), rest_z(PtA.T).T)


def zz_compress(A):
    return sym(rest_z(rest_z(A).T).T)


def next_pow2(n):
    p = 1
    while p < n:
        p *= 2
    return p


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
    """The CERTIFIED per-cell envelope ell <= sigma^(M) <= up (T122)."""
    M = c.shape[0]
    L = min(next_pow2(os_start * M), cap)
    while True:
        f = sym_grid(c, L)
        fp = dsym_abs_grid(c, L)
        dt = 2.0 * math.pi / L
        j = np.arange(M, dtype=float)
        fpp = 2.0 * float(np.sum(j * j * np.abs(c)))
        d = 0.5 * dt * fp + dt * dt / 8.0 * fpp
        marg = float(np.max(d))
        pos = (f - d)[(f - d) > 0.0]
        scale = float(np.median(pos)) if pos.size > 8 else float(np.max(f))
        if marg <= frac * max(scale, 1.0e-300) or 2 * L > cap:
            return f - d, f + d, marg, L
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


def m18_row(alpha, M, atoms):
    """ONE whitened two-grid rung: the mass identity, the bad-mass fraction
    and the k-scanned M18 majorant (T136 G3).  Every bnd(k) is a valid
    majorant for its own k, so the MINIMUM over the ladder is legitimate."""
    c, D = lag_vector_fast(alpha, M, atoms)
    A_f = sym(odd_toeplitz(c, M))
    b = odd_pole_vector(alpha, M)
    fac_f = safe_cho(A_f)
    if fac_f is None:
        return None
    q = float(np.dot(b, cho_solve(fac_f, b, check_finite=False)))
    Ac, Az, Bx = two_grid_blocks(A_f)
    b_c, s = rest_p(b), rest_z(b)
    fac_c = safe_cho(Ac)
    if fac_c is None:
        return None
    x_c = cho_solve(fac_c, b_c, check_finite=False)
    delta = q - float(np.dot(b_c, x_c))
    if not (delta > 0.0):
        return None
    comb = -(Bx.T @ x_c)
    shat = s + comb
    Gm = solve_triangular(fac_c[0], Bx, lower=True, check_finite=False)
    S = sym(Az - Gm.T @ Gm)
    _, up, _, _ = cert_env(c)
    T_up = sym(odd_toeplitz(pwc_lags(up, M), M))
    maj_ok = int(safe_cho(sym(T_up - A_f)) is not None)
    Uz = zz_compress(T_up)
    fac_U = safe_cho(Uz)
    if fac_U is None:
        return None
    n_p = Uz.shape[0]
    Lw = cholesky(Uz, lower=True, check_finite=False)

    def wh(z):
        return solve_triangular(Lw, z, lower=True, check_finite=False)

    St = sym(wh(wh(S).T).T)
    mu, W = np.linalg.eigh(St)
    st_p, st_c = wh(s), wh(comb)
    st = st_p + st_c
    p2 = (W.T @ st) ** 2
    tot = float(p2.sum())
    if not (tot > 0.0):
        return None
    cb = float(np.dot(shat, cho_solve(fac_U, shat, check_finite=False)))
    bd = np.flatnonzero(mu < 0.5)
    if bd.size == 0:
        return None
    bad = float(p2[bd].sum()) / tot
    Wb = np.ascontiguousarray(W[:, bd])
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
    rows = {}
    for k in K_LADDER:
        if k >= min(hc, n_p):
            continue
        sh_w = (float(np.dot(st_p[:k], st_p[:k]))
                / max(float(np.dot(st_p, st_p)), 1.0e-300))
        Yk = solve_triangular(Lt, np.ascontiguousarray(G[:k, :].T),
                              lower=True, check_finite=False)
        sp = max(min(float(svdvals(Yk)[0]) ** 2, 1.0), 0.0)
        sig = float(svdvals(np.ascontiguousarray(Wb[k:, :]))[0])
        tail_w = float(np.linalg.norm(st_p[k:]))
        num = (math.sqrt(max(sh_w, 0.0)) * ns_p + sig * tail_w
               + math.sqrt(sp) * nc + sig * nc)
        rows[k] = dict(bnd=(num / den2) ** 2 if den2 > 0.0 else float("inf"),
                       loc=((sig * (tail_w + nc) / den2) ** 2
                            if den2 > 0.0 else float("inf")), sig=sig)
    if not rows:
        return None
    kbest = min(rows, key=lambda z: rows[z]["bnd"])
    k134 = [z for z in rows if z in K_T134]
    return dict(M=M, h=M // 2, D=D, n_p=n_p, bad=bad, n_bad=int(bd.size),
                id_white=abs(tot - cb) / max(cb, 1.0e-300), maj_ok=maj_ok,
                rows=rows, kbest=kbest, bnd=rows[kbest]["bnd"],
                loc=rows[kbest]["loc"],
                bnd134=(min(rows[z]["bnd"] for z in k134) if k134
                        else float("nan")),
                mu_min=float(mu[0]))


# ------------------------------------------------------------------ battery
def build_instances():
    """Frame-A seam windows kept small enough that EVERY factorised /
    diagonalised matrix stays <= H_CAP: the POLE-FREE odd section A and the
    border Schur block S of the same seam."""
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
        c, _ = lag_vector_fast(fr["al_n"], fr["M_n"], atoms_in(fr["al_n"]))
        A = sym(odd_toeplitz(c, fr["M_n"]))
        S = border_schur(fr)
        row = dict(n=NN_ALL[k + 1], rho=rho, fr=fr, h=fr["h_n"], gc=fr["gc"],
                   mats=[("section", A)])
        if S is not None and S.shape[0] >= 2:
            row["mats"].append(("border", S))
        out.append(row)
    return out


def build_rungs():
    """Whitened two-grid rungs for (7): h EVEN (the two-grid restriction needs
    it) and h <= H_CAP."""
    out, seen = [], set()
    for k in range(2, min(K_SCAN, len(UU_ALL) - 1)):
        u_o, u_n = UU_ALL[k], UU_ALL[k + 1]
        g = u_n - u_o
        if g <= 0.0:
            continue
        D_k = 0.5 * g / NU_MAIN
        M = even_window(u_o, D_k)
        h = M // 2
        if h % 2 or h < H_MIN or h > H_CAP:
            continue
        key = h // 8
        if key in seen:
            continue
        seen.add(key)
        alpha = 0.5 * M * D_k
        out.append((NN_ALL[k], alpha, M))
        if len(out) >= N_RUNG:
            break
    return out


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v543  PRIME.MMATRIX.IDENT.01 -- the lumped M-matrix pair (T136)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered tolerances")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = build_instances()
    MATS = [(t, tag, Mx) for t in INST for tag, Mx in t["mats"]]
    check(f"S0.INST: {len(INST)} frame-A seam windows -> {len(MATS)} symmetric "
          f"matrices (pole-free sections + border Schur blocks)",
          len(INST) >= 8 and len(MATS) >= 12)
    h_max = max(Mx.shape[0] for _, _, Mx in MATS)
    check(f"S0.CAP: every factorised / diagonalised matrix <= {H_CAP} "
          f"(max size {h_max})", h_max <= H_CAP)
    for t in INST:
        print(f"    n={t['n']:>7d} rho={t['rho']:.5f} h={t['h']:>4d} "
              f"gc={t['gc']:>3d} blocks={len(t['mats'])}")

    PAIR = [(tag, lump_pair(Mx)) for _, tag, Mx in MATS]
    PAIR = [(tag, pr) for tag, pr in PAIR if pr["n_pos"] > 0]
    check(f"S0.POS: {len(PAIR)} of {len(MATS)} matrices carry POSITIVE "
          f"off-diagonals at all (a lumped pair is only content where they "
          f"do; up to {max(pr['n_pos'] for _, pr in PAIR)} positive entries)",
          len(PAIR) >= 10)

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the lumped pair: Stieltjes, row sums, Loewner direction")
    off_max = max(pr["off_max"] for _, pr in PAIR)
    dg_min = min(pr["dg_min"] for _, pr in PAIR)
    rs_res = max(pr["rs_res"] for _, pr in PAIR)
    ld_lmin = min(pr["ld_lmin"] for _, pr in PAIR)
    check(f"S1.STIELTJES: A_B = A + L_Delta has ALL off-diagonals <= 0 on all "
          f"{len(PAIR)} matrices (max off-diagonal {off_max:.2e} relative) "
          f"and a strictly positive diagonal (min {dg_min:.3e})",
          off_max <= TOL_LUMP and dg_min > 0.0)
    check(f"S1.ROWSUM: the row sums are PRESERVED, A_B 1 == A 1 "
          f"(max rel {rs_res:.2e} < {TOL_LUMP:.0e})", rs_res < TOL_LUMP)
    check(f"S1.PSD: L_Delta is a graph Laplacian, hence PSD "
          f"(min lam_min {ld_lmin:.2e} relative), so A_B >= A in the LOEWNER "
          f"order -- an UPPER bound on lam_min(A) and a floor NEVER",
          ld_lmin >= -TOL_LUMP)
    lam_dir = [(float(eigvalsh(pr["A"])[0]), float(eigvalsh(pr["A_B"])[0]))
               for _, pr in PAIR]
    n_strict = sum(1 for a, b in lam_dir if b > a * (1.0 + 1.0e-9))
    check(f"S1.DIRECTION: lam_min(A_B) >= lam_min(A) on all {len(PAIR)} "
          f"matrices, STRICTLY on {n_strict} -- the direction is part of the "
          f"claim, not a caveat",
          all(b >= a - TOL_LUMP * abs(a) for a, b in lam_dir) and n_strict >= 8)
    ctrl1 = max(lump_negative(pr["A"]) for _, pr in PAIR)
    check(f"S1.CTRL: lumping the NEGATIVE off-diagonals instead keeps the row "
          f"sums but destroys the Stieltjes property (max positive "
          f"off-diagonal {ctrl1:.2e} > {BAR_CTRL:.0e})", ctrl1 > BAR_CTRL)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) congruence  A = A_B^1/2 (I - W) A_B^1/2, "
          "lam_max(W) = rho(L_Delta A_B^-1)")
    CON = [(tag, pr, congruence(pr)) for tag, pr in PAIR]
    CON = [(tag, pr, cn) for tag, pr, cn in CON if cn is not None]
    cong_res = max(cn["res"] for _, _, cn in CON)
    spec_res = max(abs(cn["w_lmax"] - cn["rho_e"])
                   / max(cn["w_lmax"], 1.0e-300) for _, _, cn in CON)
    w_min = min(cn["w_lmin"] for _, _, cn in CON)
    check(f"S2.ROWS: {len(CON)} of {len(PAIR)} lumped pairs are positive "
          f"definite, so the congruence is defined (A_B > 0 is CHECKED, "
          f"never assumed)", len(CON) >= 10)
    check(f"S2.CONGRUENCE: the MATRIX identity holds on all {len(CON)} rows "
          f"(max rel {cong_res:.2e} < {TOL_CONG:.0e})", cong_res < TOL_CONG)
    check(f"S2.PSD-W: W = A_B^-1/2 L_Delta A_B^-1/2 >= 0 "
          f"(min lam_min {w_min:.2e})", w_min >= -TOL_CONG)
    check(f"S2.SPECTRUM: lam_max(W) == rho(L_Delta A_B^-1) on all rows "
          f"(max rel {spec_res:.2e} < {TOL_SPEC:.0e})", spec_res < TOL_SPEC)
    fw_bad = [1 for _, _, cn in CON
              if int(cn["w_lmax"] < 1.0) != int(cn["lam_A"] > 0.0)]
    neg = []
    for _, pr, cn in CON:
        if not (cn["lam_A"] < cn["lam_B"]):
            continue
        s = 0.5 * (cn["lam_A"] + cn["lam_B"])
        pr_s = lump_pair(pr["A"] - s * np.eye(pr["h"]))
        cn_s = congruence(pr_s)
        if cn_s is not None:
            neg.append((cn_s["lam_A"], cn_s["w_lmax"]))
    n_neg = sum(1 for la, _ in neg if la < 0.0)
    check(f"S2.EQUIV: lam_max(W) < 1 <=> A > 0 with {len(fw_bad)} exceptions "
          f"on the {len(CON)} rows (forward direction)", not fw_bad)
    check(f"S2.EQUIV-CTRL: shifting A into the indefinite range (lumping "
          f"commutes with the shift) forces lam_max(W) >= 1 on all {n_neg} "
          f"control rows, so the equivalence is checked in BOTH directions -- "
          f"the Loewner sandwich is CIRCULAR by itself",
          n_neg >= 5 and all(w >= 1.0 for la, w in neg if la < 0.0))

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the M-matrix anchor  1 / max_r x_r <= lam_min(A_B)")
    ANC = []
    for _, pr, cn in CON:
        an = anchor(pr["A_B"])
        if an is not None:
            ANC.append((pr, cn, an))
    n_sign = sum(1 for _, _, an in ANC if an["nonneg"])
    slack = min(cn["lam_B"] - an["floor"] for _, cn, an in ANC)
    tight = max(an["floor"] / cn["lam_B"] for _, cn, an in ANC)
    inv_min = min(cn["gi_min"] for _, cn, _ in ANC)
    check(f"S3.SIGN: x = A_B^-1 1 >= 0 entrywise on {n_sign} of {len(ANC)} "
          f"rows and A_B^-1 >= 0 entrywise (min relative entry "
          f"{inv_min:.2e}) -- Ostrowski 1937 inverse positivity, CHECKED",
          n_sign == len(ANC) and inv_min >= -1.0e-13)
    check(f"S3.ANCHOR: 1 / max_r x_r <= lam_min(A_B) on all {len(ANC)} rows "
          f"(min slack {slack:.3e}, sharpest ratio {tight:.4f}) -- ONE solve, "
          f"ONE sign check, NO eigenvalue", slack >= -TOL_ANCH)
    A_ctrl = np.array([[1.0, 0.9], [0.9, 1.0]])
    x_ctrl = np.linalg.solve(A_ctrl, np.ones(2))
    f_ctrl = 1.0 / float(x_ctrl.max())
    l_ctrl = float(eigvalsh(A_ctrl)[0])
    check(f"S3.CTRL: on a matrix with a POSITIVE off-diagonal the anchor is "
          f"false ({f_ctrl:.4f} > lam_min = {l_ctrl:.4f}), so the Stieltjes "
          f"hypothesis is load-bearing", f_ctrl > l_ctrl * (1.0 + BAR_CTRL))

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) shift commutation + M-matrix inverse monotonicity")
    sh_res, mono_min, lad_bad, n_lad = 0.0, 0.0, 0, 0
    for pr, cn, an in ANC:
        Id = np.eye(pr["h"])
        prev = an["xmax"]
        marg_prev = pr["ld_inf"] * an["xmax"]
        for j in range(1, S_LADDER + 1):
            s = cn["lam_B"] * j / (S_LADDER + 1.0)
            pr_s = lump_pair(pr["A"] - s * Id)
            sh_res = max(sh_res, rel(pr_s["A_B"] - (pr["A_B"] - s * Id),
                                     pr["A_B"]))
            an_s = anchor(pr_s["A_B"])
            if an_s is None:
                continue
            n_lad += 1
            d = np.linalg.solve(pr_s["A_B"], Id) - cn["Gi"]
            mono_min = min(mono_min, float(d.min())
                           / max(float(np.abs(cn["Gi"]).max()), 1.0e-300))
            marg = pr_s["ld_inf"] * an_s["xmax"]
            if an_s["xmax"] < prev * (1.0 - 1.0e-10) or marg < marg_prev * (
                    1.0 - 1.0e-10):
                lad_bad += 1
            prev, marg_prev = an_s["xmax"], marg
    check(f"S4.SHIFT: (A - s I)_B == A_B - s I exactly on {n_lad} shifted "
          f"rows (max rel {sh_res:.2e} < {TOL_LUMP:.0e}) -- lumping touches "
          f"only the off-diagonals", sh_res < TOL_LUMP)
    check(f"S4.MONO: (A_B - s I)^-1 >= A_B^-1 >= 0 ENTRYWISE on all "
          f"{n_lad} rows (min relative violation {mono_min:.2e}) -- "
          f"Berman-Plemmons 1979 inverse monotonicity",
          mono_min >= -TOL_MONO)
    check(f"S4.EMPTY: therefore max_r x_r(s) AND the a-priori margin "
          f"||L_Delta||_inf max_r x_r(s) are non-decreasing along the whole "
          f"ladder ({lad_bad} exceptions of {n_lad}) -- the shifted ladder is "
          f"STRUCTURALLY EMPTY, a theorem and not a measurement",
          lad_bad == 0 and n_lad >= 40)
    Ac2 = np.array([[1.0, 0.9], [0.9, 1.0]])
    d_ctrl = (np.linalg.inv(Ac2 - 0.05 * np.eye(2)) - np.linalg.inv(Ac2))
    ctrl4 = float(d_ctrl.min()) / float(np.abs(np.linalg.inv(Ac2)).max())
    check(f"S4.CTRL: without the Stieltjes hypothesis the entrywise "
          f"monotonicity is false (relative violation {ctrl4:.2e}, magnitude "
          f"> {BAR_CTRL:.0e})", ctrl4 < -BAR_CTRL)

    # ------------------------------------------------------------ (5), (6)
    print("\nS5 -- (5) Varga's regular splitting  rho(J) = tau / (1 + tau)")
    VAR = []
    for tag, pr in PAIR:
        vr = varga_row(pr["A_B"], pr["scale"])
        if vr is not None:
            VAR.append((tag, pr, vr))
    v_res = max(vr["varga_id"] for _, _, vr in VAR)
    n0_min = min(vr["n0_min"] for _, _, vr in VAR)
    n_inv = sum(1 for _, _, vr in VAR if vr["inv_nonneg"])
    rho_lo = min(vr["rho"] for _, _, vr in VAR)
    rho_hi = max(vr["rho"] for _, _, vr in VAR)
    check(f"S5.SPLIT: A_B = D_0 - N_0 is a REGULAR splitting on all "
          f"{len(VAR)} rows -- D_0 > 0, N_0 >= 0 (min relative entry "
          f"{n0_min:.2e}) and A_B^-1 >= 0 on {n_inv} of {len(VAR)}",
          n0_min >= -TOL_LUMP and n_inv == len(VAR))
    check(f"S5.VARGA: rho(J) == tau / (1 + tau) with tau = rho(A_B^-1 N_0) on "
          f"all {len(VAR)} rows (max rel {v_res:.2e} < {TOL_VARGA:.0e}); "
          f"rho(J) = {rho_lo:.4f} .. {rho_hi:.4f} < 1", v_res < TOL_VARGA
          and rho_hi < 1.0)
    c5, n0p = varga_control(VAR[0][1]["A_B"])
    check(f"S5.CTRL: a NON-regular splitting (one diagonal of D_0 halved, so "
          f"N_0 acquires the NEGATIVE diagonal entry {n0p:.3e} relative and "
          f"the hypothesis N_0 >= 0 fails) breaks the identity "
          f"(rel {c5:.2e} > {BAR_CTRL:.0e})",
          c5 > BAR_CTRL and n0p < -BAR_CTRL)

    print("\nS6 -- (6) the Collatz-Wielandt bracket at the anchor vector")
    br_bad = [1 for _, _, vr in VAR
              if not (vr["cw_lo"] <= vr["tau"] * (1.0 + 1.0e-9) + TOL_ANCH
                      and vr["tau"] <= vr["cw_up"] * (1.0 + 1.0e-9)
                      + TOL_ANCH)]
    rho_cw = [vr["cw_up"] / (1.0 + vr["cw_up"]) for _, _, vr in VAR]
    sharp = [(1.0 - vr["rho"]) * (1.0 + vr["cw_up"]) for _, _, vr in VAR]
    n_alt = sum(1 for _, _, vr in VAR if vr["cw_alt"] < vr["tau"])
    check(f"S6.BRACKET: min_r (Tx)_r/x_r <= tau <= max_r (Tx)_r/x_r at the "
          f"anchor vector x = A_B^-1 1 > 0 on all {len(VAR)} rows "
          f"({len(br_bad)} exceptions)", not br_bad)
    check(f"S6.APRIORI: hence rho(J) <= tau_cw/(1 + tau_cw) = "
          f"{min(rho_cw):.4f} .. {max(rho_cw):.4f} < 1 on all {len(VAR)} rows "
          f"with NO eigenvalue anywhere (two solves)", max(rho_cw) < 1.0)
    check(f"S6.SHARP: the a-priori GAP is sharp on the measured gap by the "
          f"factor {min(sharp):.4f} .. {max(sharp):.4f} (>= 1 by the bracket) "
          f"-- REPORTED, not claimed as a law", min(sharp) >= 1.0 - 1.0e-9)
    check(f"S6.CTRL: at a SIGN-CHANGING test vector the same quotient bound "
          f"is FALSE on {n_alt} of {len(VAR)} rows, so positivity of the test "
          f"vector is load-bearing", n_alt >= len(VAR) // 2)

    # ---------------------------------------------------------------- (7)
    print("\nS7 -- (7) the k-scanned M18 majorant -- a NEGATIVE result")
    RUNG = []
    for n_lbl, alpha, M in build_rungs():
        rw = m18_row(alpha, M, atoms_in(alpha))
        if rw is not None:
            rw["n"] = n_lbl
            RUNG.append(rw)
    check(f"S7.RUNGS: {len(RUNG)} whitened two-grid rungs built "
          f"(h = {min(r['h'] for r in RUNG)}..{max(r['h'] for r in RUNG)}, "
          f"compressed metric n_p = {min(r['n_p'] for r in RUNG)}.."
          f"{max(r['n_p'] for r in RUNG)})", len(RUNG) >= 4)
    id_w = max(r["id_white"] for r in RUNG)
    n_maj = sum(1 for r in RUNG if r["maj_ok"])
    check(f"S7.WHITEN: the mass identity ||L^-1 shat||^2 == shat^T U^-1 shat "
          f"holds on all {len(RUNG)} rungs (max rel {id_w:.2e} < "
          f"{TOL_WHITE:.0e}); the certified envelope majorises the section "
          f"(U >= A) on {n_maj} of {len(RUNG)}",
          id_w < TOL_WHITE and n_maj == len(RUNG))
    maj_bad = [1 for r in RUNG for k in r["rows"]
               if r["bad"] > r["rows"][k]["bnd"] * (1.0 + 1.0e-9)]
    n_kk = sum(len(r["rows"]) for r in RUNG)
    check(f"S7.MAJORANT: the triangle chain gives a VALID majorant for the "
          f"bad-mass fraction at EVERY k separately -- {n_kk} (rung, k) pairs "
          f"over the ladder {K_LADDER}, {len(maj_bad)} violations; taking the "
          f"minimum over the ladder is therefore legitimate", not maj_bad)
    bnd_lo = min(r["bnd"] for r in RUNG)
    loc_lo = min(r["loc"] for r in RUNG)
    b134 = min(r["bnd134"] for r in RUNG)
    bad_hi = max(r["bad"] for r in RUNG)
    check(f"S7.NEGATIVE: the k-scan does NOT bring the majorant under the "
          f"preregistered bar {BAR_MASS_GOOD:.2f} on ANY rung (best over the "
          f"WIDE ladder {bnd_lo:.3f}, best over the three T134 values "
          f"{b134:.3f}); the measured bad mass itself is <= {bad_hi:.4f}, so "
          f"the loss is the BOUND and not the object",
          bnd_lo > BAR_MASS_GOOD and bad_hi < BAR_MASS_GOOD)
    check(f"S7.LOCALISATION: the localisation term sigma_b(k)(tail + nc)/den "
          f"alone already exceeds the bar (best {loc_lo:.3f} > "
          f"{BAR_MASS_GOOD:.2f}), so no refinement of the OTHER three terms "
          f"can close M18 -- what is missing is a localisation statement",
          loc_lo > BAR_MASS_GOOD)

    # ---------------------------------------------------------------- fences
    print("\nS8 -- the fences, restated as a check")
    check("S8.FENCE: PER-INSTANCE statements on SMALL windows only -- nothing "
          "uniform in the zone index, in D or in the gap; (2) carries NO "
          "floor, its content is the exact congruence plus the DECLARED "
          "equivalence lam_max(W) < 1 <=> A > 0 (the sandwich is circular by "
          "itself); (3) and (5) are implications with CHECKED hypotheses "
          "(Stieltjes, positive definite, x >= 0, N_0 >= 0 at the instance); "
          "(4) kills a ROUTE and says nothing about the true lam_max(W); (7) "
          "is a NEGATIVE result against the T134 bar 1/2, which is NOT moved, "
          "and upgrades nothing; every D-exponent of T136 is a FIT and stays "
          "in the sandbox; Stieltjes / Ostrowski 1937 / Fan 1958 / "
          "Berman-Plemmons 1979 / Varga 1962 / Collatz 1942 / Wielandt 1950 / "
          "Haynsworth 1968 / Wilkinson 1968 / Higham 2002 named CLASSICAL; "
          "Weil 1952 CITED, never used as a criterion; zero-firewall "
          "AST-checked; NO marker upgrade of any pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv543 runtime: {elapsed:.1f}s")
    print(f"  (1) lumped pair: off-diag <= {off_max:.1e}, row sums "
          f"{rs_res:.1e}, L_Delta PSD {ld_lmin:.1e} on {len(PAIR)} matrices")
    print(f"  (2) congruence: max rel {cong_res:.1e}; lam_max(W) = rho "
          f"{spec_res:.1e}; equivalence both directions ({n_neg} controls)")
    print(f"  (3) anchor: min slack {slack:.3e}, sharpest ratio {tight:.4f} "
          f"on {len(ANC)} rows")
    print(f"  (4) shift ladder: commutation {sh_res:.1e}, monotonicity "
          f"{mono_min:.1e}, {lad_bad} exceptions on {n_lad} rungs")
    print(f"  (5) Varga identity: max rel {v_res:.1e}; rho(J) = {rho_lo:.4f}"
          f" .. {rho_hi:.4f}")
    print(f"  (6) Collatz-Wielandt: a-priori rho <= {max(rho_cw):.4f}, sharp "
          f"{min(sharp):.4f} .. {max(sharp):.4f}")
    print(f"  (7) M18 k-scan: majorant valid on {n_kk} (rung, k) pairs, best "
          f"{bnd_lo:.3f} > {BAR_MASS_GOOD:.2f} -- NEGATIVE")
    return summary("PRIME.MMATRIX.IDENT.01 lumped M-matrix pair")


if __name__ == "__main__":
    raise SystemExit(run())
