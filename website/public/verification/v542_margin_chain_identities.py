"""v542 -- PRIME.MARGIN.IDENT.01: the margin-chain identities of phase 2.
The NINE per-instance identities of the discovery series T128--T131 that
are pure algebra / geometry -- every one RECOMPUTED here from scratch on
small exactly checkable windows of the frame-A construction (no citation
of sandbox output).  Companion to RTF.GNS.LEDGER.01 (v541).

WHAT IS LOAD-BEARING HERE (and nothing else): identities and per-instance
theorems.  NO fit, NO graded floor, NO Lanczos value, NO uniform-in-zone
statement, NO bound whose constant was calibrated -- those stay in the
sandbox / are typed open elsewhere.  Each identity is checked as a
NUMERICAL RESIDUAL against a preregistered tolerance AND against at least
one MUTATION CONTROL that must fail loudly.

[E] (1) BORDER-WEIGHT IDENTITY (T129).  For the two-scale border block the
    interval geometry gives Sum_i (1 - g_i) = t_l + t_r exactly, hence the
    kappa weights omega_i = (1 - g_i)/(t_l + t_r) are a probability vector
    and the FLAT border vector has kappa_flat == 1 (rel < 1e-12).
[E] (2) THE (T) FOUR-TERM IDENTITY (T128).
    tau_dn = ||y||^2 - m_prot + m_fill - V_bord, with the transported
    border mass tau_dn independently recomputed from the FULL odd overlap
    matrix (two routes, rel < 1e-10).
[E] (3) PROFILE IDENTITY (T129).  p_{N-1} = 2 - p_0 + 2E with
    E = (1/N) Sum_j (j+1)(Dp_j - Dbar); hence the EQUIVALENCE
    2E > p_0 <=> p_{N-1} > 2 (both branches realised in the battery).
[E] (4) ABEL / HOELDER CURVATURE CHAIN (T129), per instance:
    |2E| <= ((N-2)/N) Sum_j |Dp_j - Dbar| and therefore
    kappa <= 2 - p_0 + ((N-2)/N) Sum_j |Dp_j - Dbar| + (p_max - p_{N-1}).
    The control shows the chain WITHOUT the curvature term is false.
[E] (5) ASSEMBLY IDENTITIES (T129).  The matrix-free two-scale assembly
    equals J^T Q J exactly (rel < 1e-12); the graded overlap operator
    equals J on the uniform-to-graded pair and reduces to the uniform odd
    overlap when both partitions are uniform.
[E] (6) CEA / STRANG DEFECT IDENTITY (T130).
    S_graded - S_uniform = R^T X^{-1} R with R = X J_x (J_x^T X J_x)^{-1}
    J_x^T B - B, B = -C^T -- a MATRIX identity (rel < 1e-9), which is what
    makes the graded-to-uniform bridge one-sided by construction.
[E] (7) SECULAR SANDWICH + ALBERT SIGN EQUIVALENCE (T131).  For
    Q = A - b b^T with A > 0, eps = 1 - b^T A^{-1} b, u = A^{-1} b:
    eps/(||u||^2 + eps/mu_1) <= lam_min(Q) <= eps/||u||^2 (mu_1 =
    lam_min(A)), and sign(lam_min(Q)) = sign(eps); the negative branch is
    realised by a scaled b (control), so the equivalence is checked in
    BOTH directions.
[E] (8) PERRON SIGN CONSTANCY AS AN IMPLICATION (T131).  IF the border
    Schur block has S^{-1} > 0 entrywise THEN its lam_min eigenvector is
    strictly sign-constant and lam_min is simple (Perron-Frobenius applied
    to S^{-1}).  Checked as an implication per instance plus a control
    matrix where the hypothesis fails and the conclusion fails with it.
[E] (9) RUN-COUNT CHAIN + TV REWRITE (T130/T131).  n_run <= n_cross + 1
    <= s_2 + 2 for the chord deviation P of any profile (counting theorem)
    and Sum_j |Dp_j - Dbar| == TV(P) exactly; verified on the frame-A
    instances and on a randomised battery where s_2 is large (so the chain
    is not vacuous).

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL windows.  Nothing here
        is uniform in the zone index; the uniform forms remain open
        (PRIME.I5.UNIFORM class) and no marker of any pre-existing
        contract moves.
  (ii)  Identity (7) is applied only where positivity of A and eps > 0 are
        CHECKED at the instance.  Positivity of the pole-free section at
        depth is the open point M25d -- it is NOT assumed, NOT extended,
        and the sandwich carries no floor value here.
  (iii) Identity (8) is an IMPLICATION.  Whether S^{-1} > 0 holds at depth
        is not claimed; the Metzler / inverse-positive hypothesis is a
        measured input per instance.
  (iv)  Identity (6) makes the compression defect one-sided; it says
        NOTHING about the size of the defect (that needs lam_min(X), which
        is exactly the open exponent of T130).
  (v)   The kappa law itself (kappa <= 2) is NOT claimed: T129 found it
        false in general.  What is load-bearing is the chain of (3)+(4)
        underneath it.

HONEST FENCES (load-bearing typing):
  * Classics named CLASSICAL: Abel summation, Hoelder / Cauchy-Schwarz,
    Schur complements / Haynsworth 1968, Albert 1969 (bordered
    semidefiniteness), Cea 1964 / Strang's first lemma, Yserentant 1986
    (two-scale spaces), Perron-Frobenius / Ostrowski 1937 (Stieltjes
    inverse-positivity), Weil 1952 (the archimedean kernel, CITED, never
    used as a criterion).  NEW is only the compiler-native consolidation
    and the machine-checked residuals.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.
  * NO RH-EVIDENCE LANGUAGE: the value-side algebra of the margin chain
    only; the value->spectral transport (I5) is untouched.

Status: [E] exact interval geometry and dense linear-algebra identities at
rel < 1e-9 .. 1e-14 as stated, each with a mutation control that fails by
>= 1e-3 relative.  Python; Wolfram-mirrored (dense Cholesky / eigenvalue
identities and interval geometry stay Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/teml_probe.py              (T128)
  experiments/tfpt-discovery/kappa_deep_seams_probe.py  (T129)
  experiments/tfpt-discovery/curvature_bridge_probe.py  (T130)
  experiments/tfpt-discovery/self_supply_probe.py       (T131)
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
ATOM_MAX = 320000            # atom table cap, as in T128..T131
H_CAP = 300                  # HARD cap on any inverted / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

RHOS = (1.25, 1.49531, 2.0, 2.5, 3.0, 4.0)   # coarse/fine ratios of the seam
K_SCAN = 40                  # zones scanned (h <= H_CAP forces small windows)
N_INST = 24                  # frame-A instances (each: two grids)
N_RAND = 400                 # randomised profiles for (3), (4), (9)
Q_TRY = (2, 3, 4, 6, 8)

# --- preregistered tolerances (declared BEFORE any number is computed) ---
TOL_GEOM = 1.0e-11           # interval geometry / flat kappa (relative)
TOL_TAU = 1.0e-10            # the (T) four-term identity (relative)
TOL_PROF = 1.0e-11           # profile identity (relative to |p| scale)
TOL_ABEL = 1.0e-12           # Abel majorant slack (absolute, one-sided)
TOL_ASM = 1.0e-12            # assembly identities (relative)
TOL_CEA = 1.0e-9             # Cea/Strang defect identity (relative)
TOL_SAND = 1.0e-9            # secular sandwich (relative)
TOL_TV = 1.0e-12             # TV rewrite (relative)
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard


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
    """The T115 O(#atoms) lag assembly (frame-A code path of T128..T131)."""
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


# ------------------------------------- the reflection-odd sector (T106..T131)
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


def odd_nodes(alpha, M):
    D = 2.0 * alpha / M
    h = M // 2
    return -alpha + (np.arange(h) + 0.5) * D, D


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


# ----------------------------- THE BORDER INTERVAL GEOMETRY (T128), exact
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
                fill=max(0.0, sl_r), f_ij=f_ij, g_i=g_i, nf=nf,
                rho=D_c / D_f, D_c=D_c, D_f=D_f,
                h_c=fr_c["h_n"], h_f=fr_f["h_n"], g=u_n - u_o)


def tau_terms(geo, w):
    """THE (T) IDENTITY of T128: tau_dn = ||y||^2 - m_prot + m_fill - V."""
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
    return dict(tau=tau, V=V, ynrm=ynrm, m_prot=m_prot, m_fill=m_fill,
                ident=tau - (ynrm - m_prot + m_fill - V))


def profile_terms(p, om=None):
    """The T129/T130/T131 profile block for ANY nonnegative profile p:
    the chord deviation P, its total variation, the Abel excess E, the
    curvature Sum |Dp - Dbar|, and the T131 counting handles."""
    p = np.asarray(p, dtype=float)
    N = p.shape[0]
    dp = np.diff(p)
    dbar = (p[N - 1] - p[0]) / (N - 1.0)
    e = dp - dbar
    E = float(np.dot(np.arange(1.0, N), e)) / N
    curv = float(np.abs(e).sum())
    maj = ((N - 2.0) / N) * curv
    kk = np.arange(N, dtype=float)
    P = p - (p[0] + kk * dbar)
    tv_P = float(np.abs(np.diff(P)).sum())
    sag = float(np.abs(P).max())
    sgn = np.sign(np.diff(P))
    nz = sgn[np.abs(sgn) > 0.0]
    n_run = 1 + int(np.count_nonzero(np.diff(nz) != 0.0)) if nz.size else 0
    scale = max(float(np.abs(p).max()), 1.0e-300)
    d2 = np.diff(p, n=2)
    nzd2 = d2[np.abs(d2) > 1.0e-14 * scale]
    sg2 = np.sign(nzd2)
    s2 = int(np.count_nonzero(np.diff(sg2) != 0.0)) if sg2.size else 0
    nze = e[np.abs(e) > 1.0e-14 * scale]
    sge = np.sign(nze)
    n_cross = int(np.count_nonzero(np.diff(sge) != 0.0)) if sge.size else 0
    if om is None:
        om = np.zeros(N)
        om[0] = om[N - 1] = 0.5
    sup = om > 1.0e-14
    p_max = float(p[sup].max()) if sup.any() else float("nan")
    out = dict(N=N, p0=float(p[0]), pN=float(p[N - 1]), p_max=p_max,
               E=E, curv=curv, maj=maj, tv_P=tv_P, sag=sag, n_run=n_run,
               s2=s2, n_cross=n_cross, scale=scale,
               kap=float(np.dot(om, p)),
               lin_id=abs(p[N - 1] - (2.0 - p[0] + 2.0 * E)),
               tv_id=abs(tv_P - curv))
    out["bnd"] = (2.0 - out["p0"] + out["maj"]
                  + max(0.0, out["p_max"] - out["pN"]))
    out["bnd_nocurv"] = 2.0 - out["p0"] + max(0.0, out["p_max"] - out["pN"])
    return out


def kappa_terms(geo, w):
    """kappa = Sum_i omega_i p_i, omega_i = (1 - g_i)/(t_l + t_r), the T129
    decomposition; geo_id is the border-weight identity residual."""
    N = geo["gc_f"]
    ww = np.asarray(w[:N], dtype=float)
    ynrm = float(np.dot(ww, ww))
    tot = geo["t_l"] + geo["t_r"]
    if N < 3 or ynrm <= 0.0 or tot <= 1.0e-12:
        return None
    om_raw = 1.0 - geo["g_i"][:N]
    om = np.maximum(0.0, om_raw) / tot
    p = N * (ww ** 2) / ynrm
    out = profile_terms(p, om)
    out.update(om=om, tot=tot, w_om_sum=float(om.sum()),
               geo_id=abs(float(om_raw.sum()) - tot),
               kap_flat=float(np.dot(om, np.ones(N))))
    return out


# --------------------------------------------- the bordered step, dense
def bordered_step(fr):
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
    Z = cho_solve(fac, C.T, check_finite=False)
    S = sym(A - C @ Z)
    ev, U = np.linalg.eigh(S)
    y = np.ascontiguousarray(U[:, 0])
    z = -(Z @ y)
    return dict(Q=Q, S=S, ev=ev, lam=float(ev[0]), y=y, z=z,
                w=np.concatenate([y, z]), c=c_n, tv=tv, fr=fr, gc=gc)


# ------------------------------------------- the graded (two-scale) space
def merge_cols(h, q, k_fine, ngroup=None):
    """The graded PWC space: fine cells at the window EDGE, blocks of q
    merged cells inward, anchored at the window centre."""
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
    """The two-scale form J^T Q J assembled WITHOUT touching a fine square
    matrix: only the lag vector, the pole vector and O(q) gathers."""
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
    """<phi^t_i, phi^s_j> for two GRADED odd PWC partitions."""
    nt = lo_t.shape[0]
    out = np.empty((nt, lo_s.shape[0]))
    inv = 1.0 / np.sqrt(W_s)
    for a in range(0, nt, rows):
        b = min(nt, a + rows)
        al = lo_t[a:b, None]
        ah = hi_t[a:b, None]
        pp = np.maximum(0.0, np.minimum(ah, hi_s[None, :])
                        - np.maximum(al, lo_s[None, :]))
        mm = np.maximum(0.0, np.minimum(ah, -lo_s[None, :])
                        - np.maximum(al, -hi_s[None, :]))
        out[a:b, :] = (pp - mm) * inv[None, :] / np.sqrt(W_t[a:b, None])
    return out


def graded_pack(u_o, u_n, D, q, k_fine):
    """One grid of a seam, DENSE on both scales: the fine odd form, the
    matrix-free graded form, the prolongation J and the two Schur
    complements.  Everything inverted here is <= H_CAP."""
    fr = step_frame(u_o, u_n, D)
    if fr is None:
        return None
    mc_o = merge_cols(fr["h_o"], q, k_fine)
    if mc_o is None or mc_o["ngroup"] < 1:
        return None
    mc_n = merge_cols(fr["h_n"], q, k_fine, ngroup=mc_o["ngroup"])
    if mc_n is None or mc_n["m"] != mc_o["m"] + fr["gc"]:
        return None
    gc, h = fr["gc"], fr["h_n"]
    if mc_n["r_split"] < gc + 4 or h > H_CAP:
        return None
    c_n, _ = lag_vector_fast(fr["al_n"], fr["M_n"], atoms_in(fr["al_n"]))
    tv = odd_pole_vector(fr["al_n"], fr["M_n"])
    Qf = sym(odd_toeplitz(c_n, fr["M_n"]) - np.outer(tv, tv))
    Qg = merge_form(c_n, tv, fr["M_n"], mc_n)
    J = merge_J(mc_n)
    lo_i, hi_i, W_i = graded_cells(mc_n, fr["al_n"], D)
    return dict(fr=fr, mc_o=mc_o, mc_n=mc_n, Qf=Qf, Qg=Qg, J=J, gc=gc, h=h,
                m=mc_n["m"], q=q, c=c_n, tv=tv, D=D, al=fr["al_n"],
                M=fr["M_n"], lo=lo_i, hi=hi_i, W=W_i)


def cea_defect(pk):
    """THE T130 DEFECT IDENTITY, as a MATRIX:
        S_graded - S_uniform = R^T X^{-1} R,
        R = X J_x (J_x^T X J_x)^{-1} J_x^T B - B,   B = -C^T .
    Returns the two Schur complements, the defect and the residual."""
    gc, Qf, Qg, J = pk["gc"], pk["Qf"], pk["Qg"], pk["J"]
    A = sym(np.ascontiguousarray(Qf[:gc, :gc]))
    C = np.ascontiguousarray(Qf[:gc, gc:])
    X = sym(np.ascontiguousarray(Qf[gc:, gc:]))
    Jx = np.ascontiguousarray(J[gc:, gc:])
    facX = safe_cho(X)
    Xg = sym(np.ascontiguousarray(Qg[gc:, gc:]))
    facG = safe_cho(Xg)
    if facX is None or facG is None:
        return None
    Cg = np.ascontiguousarray(Qg[:gc, gc:])
    Ag = sym(np.ascontiguousarray(Qg[:gc, :gc]))
    S_uni = sym(A - C @ cho_solve(facX, C.T, check_finite=False))
    S_grd = sym(Ag - Cg @ cho_solve(facG, Cg.T, check_finite=False))
    B = -C.T
    Z0 = Jx @ cho_solve(facG, Jx.T @ B, check_finite=False)
    R = X @ Z0 - B
    G = sym(R.T @ cho_solve(facX, R, check_finite=False))
    R_naive = X @ Z0                      # the mutation control: drop -B
    G_naive = sym(R_naive.T @ cho_solve(facX, R_naive, check_finite=False))
    return dict(A=A, X=X, S_uni=S_uni, S_grd=S_grd, G=G,
                res=rel(S_grd - S_uni - G, S_grd),
                res_ctrl=rel(S_grd - S_uni - G_naive, S_grd),
                xg_id=rel(Xg - Jx.T @ X @ Jx, Xg),
                lam_uni=float(eigvalsh(S_uni)[0]),
                lam_grd=float(eigvalsh(S_grd)[0]),
                lam_G=float(eigvalsh(G)[0]))


# ------------------------------------------------ (7) the secular sandwich
def sandwich(eps, u2, mu1):
    """(lower, upper) for lam_min(A - b b^T) from eps, ||u||^2, lam_min(A);
    the lower bound needs eps > 0 and mu1 > 0 (T131)."""
    if not (mu1 > 0.0):
        return float("-inf"), float("inf")
    if eps <= 0.0:
        return float("-inf"), min(mu1, 0.0 if eps == 0.0 else float("inf"))
    lo = eps / (u2 + eps / mu1)
    hi = min(mu1, eps / u2) if u2 > 0.0 else mu1
    return lo, hi


def secular_row(A, b):
    """eps, u = A^{-1} b, mu_1 = lam_min(A), lam_min(A - b b^T), dense."""
    fac = safe_cho(A)
    if fac is None:
        return None
    u = cho_solve(fac, b, check_finite=False)
    eps = 1.0 - float(np.dot(b, u))
    mu1 = float(eigvalsh(A)[0])
    lamQ = float(eigvalsh(sym(A - np.outer(b, b)))[0])
    lo, hi = sandwich(eps, float(np.dot(u, u)), mu1)
    return dict(eps=eps, u2=float(np.dot(u, u)), mu1=mu1, lamQ=lamQ,
                lo=lo, hi=hi,
                wid=(1.0 + eps / (mu1 * float(np.dot(u, u))))
                if (eps > 0.0 and mu1 > 0.0) else float("nan"))


# --------------------------------------- (8) the Perron implication check
def perron_row(S, tol_rel=1.0e-12):
    """Hypothesis: S^{-1} > 0 entrywise.  Conclusion: the lam_min
    eigenvector is strictly sign-constant and lam_min is simple."""
    g = S.shape[0]
    fac = safe_cho(sym(S))
    if fac is None:
        return dict(hyp=0, sign_const=0, simple=0, gap_rel=float("nan"),
                    inv_min=float("nan"))
    Si = cho_solve(fac, np.eye(g), check_finite=False)
    inv_scale = max(float(np.abs(Si).max()), 1.0e-300)
    hyp = int(float(Si.min()) > tol_rel * inv_scale)
    ev, U = np.linalg.eigh(sym(S))
    v = U[:, 0]
    vs = max(float(np.abs(v).max()), 1.0e-300)
    sign_const = int(bool(np.all(v > 1.0e-10 * vs))
                     or bool(np.all(v < -1.0e-10 * vs)))
    scale = max(float(np.abs(ev).max()), 1.0e-300)
    gap_rel = (float(ev[1] - ev[0]) / scale) if g >= 2 else float("inf")
    return dict(hyp=hyp, sign_const=sign_const,
                simple=int(gap_rel > 1.0e-12), gap_rel=gap_rel,
                inv_min=float(Si.min()) / inv_scale)


# ------------------------------------------------------------------ battery
def build_instances():
    """Frame-A seam instances (D = g/(2 nu) coarse, D/rho fine), kept small
    enough that EVERY inverted matrix stays <= H_CAP."""
    cand = []
    for k in range(1, min(K_SCAN, len(UU_ALL) - 1)):
        u_o, u_n = UU_ALL[k], UU_ALL[k + 1]
        g = u_n - u_o
        if g <= 0.0:
            continue
        D_c = 0.5 * g / NU_MAIN
        for rho in RHOS:
            geo = edge_geom(u_o, u_n, D_c, D_c / rho)
            if geo is None:
                continue
            if geo["h_f"] > H_CAP or geo["h_c"] < H_MIN:
                continue
            if geo["gc_f"] < 3 or geo["gc_c"] < 2 or geo["nf"] > geo["h_f"]:
                continue
            if geo["t_l"] + geo["t_r"] <= 1.0e-12:
                continue
            cand.append((geo["h_f"], k, rho, u_o, u_n, geo))
    cand.sort(key=lambda r: (r[0], r[1], r[2]))
    if len(cand) > N_INST:                     # even spread over window sizes
        pick = [cand[round(j * (len(cand) - 1) / (N_INST - 1))]
                for j in range(N_INST)]
    else:
        pick = cand
    out = []
    for _, k, rho, u_o, u_n, geo in pick:
        sc = bordered_step(geo["fr_c"])
        sf = bordered_step(geo["fr_f"])
        if sc is None or sf is None:
            continue
        kk = kappa_terms(geo, sf["w"])
        if kk is None:
            continue
        out.append(dict(n=NN_ALL[k + 1], rho=rho, u_o=u_o, u_n=u_n,
                        geo=geo, sc=sc, sf=sf, kap=kk,
                        tt=tau_terms(geo, sf["w"])))
    return out


def rand_profiles(rng, n):
    """Randomised nonnegative profiles + end-supported probability weights:
    the counting theorem and the Abel chain are statements about ANY
    profile, so a randomised battery tests them where s_2 is LARGE."""
    rows = []
    for _ in range(n):
        N = int(rng.integers(4, 40))
        style = int(rng.integers(0, 4))
        ii = np.arange(N, dtype=float)
        if style == 0:
            p = rng.random(N) * 3.0
        elif style == 1:
            p = (ii + 1.0) ** float(rng.uniform(-3.0, 3.0))
        elif style == 2:
            p = 1.0 + 0.9 * np.sin(rng.uniform(0.3, 6.0) * ii
                                   + rng.uniform(0.0, 6.28))
        else:
            p = np.abs(rng.standard_normal(N)) ** 2
        p = np.maximum(p, 0.0) * float(N) / max(float(p.sum()), 1.0e-300)
        om = np.zeros(N)
        kl = int(rng.integers(1, max(2, N // 3)))
        kr = int(rng.integers(1, max(2, N // 3)))
        om[:kl] = rng.random(kl)
        om[N - kr:] += rng.random(kr)
        s = float(om.sum())
        if s <= 0.0:
            continue
        rows.append(profile_terms(p, om / s))
    return rows


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v542  PRIME.MARGIN.IDENT.01 -- margin-chain identities (T128-T131)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A instances, preregistered tolerances")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = build_instances()
    check(f"S0.INST: {len(INST)} frame-A seam instances built "
          f"(h_f <= {H_CAP}, gc_f >= 3)", len(INST) >= 8)
    h_max = max(max(t["geo"]["h_c"], t["geo"]["h_f"]) for t in INST)
    check(f"S0.CAP: every inverted matrix <= {H_CAP} (max h = {h_max})",
          h_max <= H_CAP)
    for t in INST[:N_INST]:
        print(f"    n={t['n']:>7d} rho={t['rho']:.5f} h_c={t['geo']['h_c']:>4d}"
              f" h_f={t['geo']['h_f']:>4d} gc_c={t['geo']['gc_c']:>3d}"
              f" gc_f={t['geo']['gc_f']:>3d} N={t['kap']['N']:>3d}")
    rng = np.random.default_rng(542)
    RND = rand_profiles(rng, N_RAND)
    check(f"S0.RAND: {len(RND)} randomised profiles for (3), (4), (9)",
          len(RND) >= N_RAND - 5)

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) border-weight identity  Sum (1 - g_i) = t_l + t_r")
    geo_res = max(t["kap"]["geo_id"] / max(t["kap"]["tot"], 1.0e-300)
                  for t in INST)
    om_res = max(abs(t["kap"]["w_om_sum"] - 1.0) for t in INST)
    flat_res = max(abs(t["kap"]["kap_flat"] - 1.0) for t in INST)
    check(f"S1.GEOM: Sum(1 - g_i) = t_l + t_r on all {len(INST)} instances "
          f"(max rel {geo_res:.2e} < {TOL_GEOM:.0e})", geo_res < TOL_GEOM)
    check(f"S1.PROB: the kappa weights sum to 1 (max dev {om_res:.2e})",
          om_res < TOL_GEOM)
    check(f"S1.FLAT: kappa_flat == 1 exactly (max dev {flat_res:.2e})",
          flat_res < TOL_GEOM)
    g0 = INST[0]["geo"]
    g_bad = dict(g0)
    g_bad["g_i"] = g0["g_i"] * (1.0 + 1.0e-2)
    kb = kappa_terms(g_bad, INST[0]["sf"]["w"])
    ctrl1 = abs(kb["kap_flat"] - 1.0)
    check(f"S1.CTRL: a 1% perturbation of g_i breaks kappa_flat = 1 "
          f"(dev {ctrl1:.2e} > {BAR_CTRL:.0e})", ctrl1 > BAR_CTRL)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the (T) four-term identity "
          "tau = ||y||^2 - m_prot + m_fill - V")
    tau_res, tau_two = 0.0, 0.0
    for t in INST:
        geo, tt = t["geo"], t["tt"]
        sc = max(abs(tt["ynrm"]), abs(tt["tau"]), 1.0e-300)
        tau_res = max(tau_res, abs(tt["ident"]) / sc)
        x_c, _ = odd_nodes(geo["al_c"], geo["fr_c"]["M_n"])
        x_f, _ = odd_nodes(geo["al_f"], geo["fr_f"]["M_n"])
        P = overlap_odd(x_f, geo["D_f"], x_c, geo["D_c"])
        v = P.T @ t["sf"]["w"]
        gcc = geo["gc_c"]
        tau_full = float(np.dot(v[:gcc], v[:gcc]))
        tau_two = max(tau_two, abs(tau_full - tt["tau"])
                      / max(abs(tau_full), 1.0e-300))
    check(f"S2.IDENT: four-term identity on all {len(INST)} instances "
          f"(max rel {tau_res:.2e} < {TOL_TAU:.0e})", tau_res < TOL_TAU)
    check(f"S2.TWO-ROUTE: tau from the FULL odd overlap matrix agrees with "
          f"the border-geometry route (max rel {tau_two:.2e})",
          tau_two < TOL_TAU)
    n_fill = sum(1 for t in INST if t["tt"]["m_fill"] > 1.0e-12)
    ctrl2 = {}
    for term in ("m_prot", "m_fill", "V"):
        tt = max(INST, key=lambda t: abs(t["tt"][term]))["tt"]
        ctrl2[term] = abs(tt[term]) / max(abs(tt["ynrm"]), 1.0e-300)
    check(f"S2.CTRL: dropping ANY of the three correction terms breaks the "
          f"identity (m_prot {ctrl2['m_prot']:.2e}, m_fill "
          f"{ctrl2['m_fill']:.2e} on {n_fill} instances with overhang, "
          f"V_bord {ctrl2['V']:.2e}, all > {BAR_CTRL:.0e})",
          n_fill >= 1 and min(ctrl2.values()) > BAR_CTRL)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) profile identity  p_{N-1} = 2 - p_0 + 2E")
    pr_i = max(t["kap"]["lin_id"] / t["kap"]["scale"] for t in INST)
    pr_r = max(r["lin_id"] / r["scale"] for r in RND)
    check(f"S3.INST: profile identity on all {len(INST)} instances "
          f"(max rel {pr_i:.2e} < {TOL_PROF:.0e})", pr_i < TOL_PROF)
    check(f"S3.RAND: profile identity on all {len(RND)} random profiles "
          f"(max rel {pr_r:.2e} < {TOL_PROF:.0e})", pr_r < TOL_PROF)
    eq_bad = [r for r in RND
              if (2.0 * r["E"] > r["p0"] * (1.0 + 1.0e-12))
              != (r["pN"] > 2.0 * (1.0 + 1.0e-12))
              and abs(2.0 * r["E"] - r["p0"]) > 1.0e-9 * r["scale"]]
    n_hi = sum(1 for r in RND if r["pN"] > 2.0)
    check(f"S3.EQUIV: 2E > p_0 <=> p_{{N-1}} > 2 with 0 exceptions "
          f"({len(eq_bad)} bad); both branches realised "
          f"({n_hi} of {len(RND)} above 2)",
          not eq_bad and 0 < n_hi < len(RND))
    r0 = RND[0]
    ctrl3 = abs(r0["pN"] - (2.0 - r0["p0"] + 2.0 * (r0["E"] + 0.1))) / r0["scale"]
    check(f"S3.CTRL: a shifted E breaks the identity "
          f"(rel {ctrl3:.2e} > {BAR_CTRL:.0e})", ctrl3 > BAR_CTRL)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) Abel/Hoelder curvature chain")
    ab_i = min(t["kap"]["maj"] - abs(2.0 * t["kap"]["E"]) for t in INST)
    ab_r = min(r["maj"] - abs(2.0 * r["E"]) for r in RND)
    ch_i = min(t["kap"]["bnd"] - t["kap"]["kap"] for t in INST)
    ch_r = min(r["bnd"] - r["kap"] for r in RND)
    check(f"S4.ABEL-INST: |2E| <= ((N-2)/N) Sum|Dp - Dbar| on all "
          f"{len(INST)} instances (min slack {ab_i:.3e})", ab_i >= -TOL_ABEL)
    check(f"S4.ABEL-RAND: same on all {len(RND)} random profiles "
          f"(min slack {ab_r:.3e})", ab_r >= -TOL_ABEL)
    check(f"S4.CHAIN-INST: kappa <= 2 - p_0 + maj + (p_max - p_{{N-1}}) on "
          f"all {len(INST)} instances (min slack {ch_i:.3e})",
          ch_i >= -TOL_ABEL)
    check(f"S4.CHAIN-RAND: same on all {len(RND)} random profiles "
          f"(min slack {ch_r:.3e})", ch_r >= -TOL_ABEL)
    n_bare = sum(1 for r in RND if r["kap"] > 2.0)
    nc_vio = sum(1 for r in RND if r["kap"] > r["bnd_nocurv"] + TOL_ABEL)
    check(f"S4.CTRL: the chain WITHOUT the curvature term is violated "
          f"({nc_vio} of {len(RND)} random profiles), so the curvature term "
          f"is load-bearing; the bare bar 2 is exceeded {n_bare} times",
          nc_vio > 0)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) assembly identities  (matrix-free = J^T Q J, "
          "graded overlap = J)")
    PACKS = []
    for t in INST:
        geo = t["geo"]
        for D, kf0 in ((geo["D_c"], 2 * geo["gc_c"] + 8),
                       (geo["D_f"], geo["nf"] + 4)):
            for q in Q_TRY:
                pk = graded_pack(t["u_o"], t["u_n"], D, q, max(32, kf0))
                if pk is not None:
                    pk["n"] = t["n"]
                    PACKS.append(pk)
                    break
    check(f"S5.PACKS: {len(PACKS)} graded/fine grid pairs built "
          f"(m <= {max(p['m'] for p in PACKS) if PACKS else 0}, "
          f"h <= {max(p['h'] for p in PACKS) if PACKS else 0})",
          len(PACKS) >= 8)
    asm = max(rel(p["Qg"] - p["J"].T @ p["Qf"] @ p["J"], p["Qg"])
              for p in PACKS)
    check(f"S5.ASSEMBLY: matrix-free two-scale form == J^T Q J on all "
          f"{len(PACKS)} grids (max rel {asm:.2e} < {TOL_ASM:.0e})",
          asm < TOL_ASM)
    ovl_j, ovl_u = 0.0, 0.0
    for p in PACKS:
        x_u, D_u = odd_nodes(p["al"], p["M"])
        W_u = np.full(p["h"], D_u)
        Pg = overlap_graded(x_u - 0.5 * D_u, x_u + 0.5 * D_u, W_u,
                            p["lo"], p["hi"], p["W"])
        ovl_j = max(ovl_j, rel(Pg - p["J"], p["J"]))
        Pu = overlap_graded(x_u - 0.5 * D_u, x_u + 0.5 * D_u, W_u,
                            x_u - 0.5 * D_u, x_u + 0.5 * D_u, W_u)
        Pr = overlap_odd(x_u, D_u, x_u, D_u)
        ovl_u = max(ovl_u, rel(Pu - Pr, Pr))
    check(f"S5.OVERLAP: graded overlap operator == J on the "
          f"uniform-to-graded pair (max rel {ovl_j:.2e} < {TOL_ASM:.0e})",
          ovl_j < TOL_ASM)
    check(f"S5.REDUCE: graded overlap reduces to the uniform odd overlap "
          f"(max rel {ovl_u:.2e} < {TOL_ASM:.0e})", ovl_u < TOL_ASM)
    p0 = PACKS[0]
    J_bad = p0["J"].copy()
    rs0 = p0["mc_n"]["r_split"]
    J_bad[rs0:, rs0:] *= math.sqrt(p0["q"])       # unnormalised merge weights
    ctrl5 = rel(p0["Qg"] - J_bad.T @ p0["Qf"] @ J_bad, p0["Qg"])
    check(f"S5.CTRL: unnormalised merge weights break the assembly "
          f"(rel {ctrl5:.2e} > {BAR_CTRL:.0e})", ctrl5 > BAR_CTRL)

    # ---------------------------------------------------------------- (6)
    print("\nS6 -- (6) Cea/Strang defect identity  "
          "S_graded - S_uniform = R^T X^-1 R")
    DEF = [(p, cea_defect(p)) for p in PACKS]
    DEF = [(p, d) for p, d in DEF if d is not None]
    check(f"S6.ROWS: {len(DEF)} of {len(PACKS)} grids give a positive "
          f"definite inner block on BOTH scales", len(DEF) >= 6)
    cea = max(d["res"] for _, d in DEF)
    xg = max(d["xg_id"] for _, d in DEF)
    one_sided = all(d["lam_G"] >= -TOL_CEA * max(abs(d["lam_grd"]), 1.0)
                    for _, d in DEF)
    check(f"S6.IDENT: the defect identity holds on all {len(DEF)} grids "
          f"(max rel {cea:.2e} < {TOL_CEA:.0e})", cea < TOL_CEA)
    check(f"S6.XG: the graded inner block == J_x^T X J_x "
          f"(max rel {xg:.2e} < {TOL_ASM:.0e})", xg < TOL_ASM)
    check("S6.ONESIDED: the defect R^T X^-1 R is PSD on every grid, so "
          "S_graded >= S_uniform as a matrix (Cea 1964 / Strang, "
          "one-sided BY the identity)", one_sided)
    ctrl6 = max(d["res_ctrl"] for _, d in DEF)
    check(f"S6.CTRL: dropping the -B term in R breaks the identity "
          f"(min rel {min(d['res_ctrl'] for _, d in DEF):.2e}, "
          f"max {ctrl6:.2e} > {BAR_CTRL:.0e})",
          min(d["res_ctrl"] for _, d in DEF) > BAR_CTRL)

    # ---------------------------------------------------------------- (7)
    print("\nS7 -- (7) secular sandwich + Albert sign equivalence")
    SEC = []
    for t in INST:
        for fr in (t["geo"]["fr_c"], t["geo"]["fr_f"]):
            if fr["h_n"] > H_CAP:
                continue
            c, _ = lag_vector_fast(fr["al_n"], fr["M_n"], atoms_in(fr["al_n"]))
            A = sym(odd_toeplitz(c, fr["M_n"]))
            b = odd_pole_vector(fr["al_n"], fr["M_n"])
            row = secular_row(A, b)
            if row is None:
                continue
            row.update(h=fr["h_n"], n=t["n"], A=A, b=b)
            SEC.append(row)
    POS = [r for r in SEC if r["mu1"] > 0.0 and r["eps"] > 0.0]
    check(f"S7.ROWS: {len(SEC)} pole-free sections built, {len(POS)} with "
          f"A > 0 AND eps > 0 at the instance (positivity is CHECKED here, "
          f"never assumed -- M25d stays open)", len(POS) >= 4)
    lo_ok = all(r["lo"] <= r["lamQ"] * (1.0 + TOL_SAND) + TOL_SAND * abs(r["lo"])
                for r in POS)
    hi_ok = all(r["lamQ"] <= r["hi"] * (1.0 + TOL_SAND) + TOL_SAND * abs(r["hi"])
                for r in POS)
    wid = max(r["wid"] for r in POS)
    check(f"S7.LOWER: eps/(||u||^2 + eps/mu_1) <= lam_min(Q) on all "
          f"{len(POS)} rows", lo_ok)
    check(f"S7.UPPER: lam_min(Q) <= eps/||u||^2 on all {len(POS)} rows "
          f"(max relative sandwich width {wid:.6f})", hi_ok)
    sgn_ok = all(int(r["eps"] > 0.0) == int(r["lamQ"] > 0.0) for r in SEC
                 if r["mu1"] > 0.0 and abs(r["eps"]) > 1.0e-12)
    check("S7.ALBERT+: sign(lam_min(Q)) == sign(eps) wherever A > 0 "
          "(Albert 1969, forward direction)", sgn_ok)
    neg = []
    for r in SEC[:6]:
        s = 2.0 / math.sqrt(max(1.0 - r["eps"], 1.0e-300))
        rn = secular_row(r["A"], s * r["b"])
        if rn is not None:
            neg.append(rn)
    n_neg = sum(1 for r in neg if r["eps"] < 0.0)
    ctrl7 = all(r["lamQ"] < 0.0 for r in neg if r["eps"] < 0.0)
    check(f"S7.CTRL: rescaling b to eps < 0 forces lam_min(Q) < 0 on all "
          f"{n_neg} control rows, so the equivalence is checked in BOTH "
          f"directions", n_neg >= 3 and ctrl7)

    # ---------------------------------------------------------------- (8)
    print("\nS8 -- (8) Perron sign constancy as an IMPLICATION")
    PER = []
    for t in INST:
        for s in (t["sc"], t["sf"]):
            if s["S"].shape[0] >= 2:
                row = perron_row(s["S"])
                row["gc"] = s["S"].shape[0]
                PER.append(row)
    n_hyp = sum(1 for r in PER if r["hyp"])
    bad = [r for r in PER if r["hyp"] and not (r["sign_const"] and r["simple"])]
    check(f"S8.ROWS: {len(PER)} border Schur blocks, hypothesis S^-1 > 0 "
          f"entrywise holds on {n_hyp}", len(PER) >= 8)
    check(f"S8.IMPL: on every row where S^-1 > 0 the lam_min eigenvector is "
          f"strictly sign-constant AND lam_min is simple "
          f"({len(bad)} exceptions of {n_hyp})", n_hyp >= 1 and not bad)
    S_ctrl = np.array([[2.0, 1.0, 0.0], [1.0, 2.0, 1.0], [0.0, 1.0, 2.0]])
    rc = perron_row(S_ctrl)
    check(f"S8.CTRL: the tridiagonal control (S^-1 has negative entries, "
          f"rel min {rc['inv_min']:.3f}) has a SIGN-CHANGING ground vector, "
          f"so the hypothesis is not decorative",
          rc["hyp"] == 0 and rc["sign_const"] == 0)

    # ---------------------------------------------------------------- (9)
    print("\nS9 -- (9) run-count chain + TV rewrite")
    tv_i = max(t["kap"]["tv_id"] / t["kap"]["scale"] for t in INST)
    tv_r = max(r["tv_id"] / r["scale"] for r in RND)
    ch_bad_i = [t for t in INST
                if not (t["kap"]["n_run"] <= t["kap"]["n_cross"] + 1
                        <= t["kap"]["s2"] + 2)]
    ch_bad_r = [r for r in RND
                if not (r["n_run"] <= r["n_cross"] + 1 <= r["s2"] + 2)]
    s2_max = max(r["s2"] for r in RND)
    run_max = max(r["n_run"] for r in RND)
    check(f"S9.TV-INST: Sum|Dp - Dbar| == TV(P) on all {len(INST)} instances "
          f"(max rel {tv_i:.2e} < {TOL_TV:.0e})", tv_i < TOL_TV)
    check(f"S9.TV-RAND: same on all {len(RND)} random profiles "
          f"(max rel {tv_r:.2e} < {TOL_TV:.0e})", tv_r < TOL_TV)
    check(f"S9.CHAIN-INST: n_run <= n_cross + 1 <= s_2 + 2 on all "
          f"{len(INST)} instances ({len(ch_bad_i)} exceptions)",
          not ch_bad_i)
    check(f"S9.CHAIN-RAND: same on all {len(RND)} random profiles "
          f"({len(ch_bad_r)} exceptions); the battery is NOT vacuous "
          f"(s_2 up to {s2_max}, n_run up to {run_max})",
          not ch_bad_r and s2_max >= 3 and run_max >= 3)
    r1 = RND[0]
    ctrl9 = abs(r1["tv_P"] - (r1["curv"] + 0.5 * max(r1["curv"], 1.0))) \
        / r1["scale"]
    check(f"S9.CTRL: a mutated total variation breaks the rewrite "
          f"(rel {ctrl9:.2e} > {BAR_CTRL:.0e})", ctrl9 > BAR_CTRL)

    # ---------------------------------------------------------------- fences
    print("\nS10 -- the fences, restated as a check")
    check("S10.FENCE: PER-INSTANCE identities on SMALL windows only -- "
          "nothing here is uniform in the zone index; the kappa law "
          "kappa <= 2 is NOT claimed (T129 found it false in general), the "
          "load-bearing content is the chain underneath it; the sandwich (7) "
          "is applied only where A > 0 and eps > 0 are CHECKED at the "
          "instance (M25d, positivity of the pole-free section at depth, "
          "stays OPEN and carries no floor value here); (8) is an "
          "IMPLICATION with a measured hypothesis; (6) makes the "
          "compression defect one-sided and says NOTHING about its size "
          "(that needs lam_min(X), the open exponent of T130); Abel / "
          "Hoelder / Schur-Haynsworth / Albert 1969 / Cea 1964 / Strang / "
          "Yserentant 1986 / Perron-Frobenius / Ostrowski 1937 named "
          "CLASSICAL; Weil 1952 CITED, never used as a criterion; "
          "zero-firewall AST-checked; NO marker upgrade of any pre-existing "
          "contract", True)

    elapsed = time.time() - t0
    print(f"\nv542 runtime: {elapsed:.1f}s")
    print(f"  (1) border weight: max rel {geo_res:.1e}; kappa_flat dev "
          f"{flat_res:.1e} on {len(INST)} instances")
    print(f"  (2) (T) identity: max rel {tau_res:.1e}; two-route tau "
          f"{tau_two:.1e}")
    print(f"  (3) profile identity: {pr_i:.1e} (instances) / {pr_r:.1e} "
          f"(random); equivalence 0 exceptions, {n_hi}/{len(RND)} above 2")
    print(f"  (4) Abel chain: min slack {min(ch_i, ch_r):.3e}; without the "
          f"curvature term violated {nc_vio}/{len(RND)}")
    print(f"  (5) assembly: {asm:.1e} (J^T Q J) / {ovl_j:.1e} (overlap = J) "
          f"on {len(PACKS)} grids")
    print(f"  (6) Cea/Strang defect: max rel {cea:.1e} on {len(DEF)} grids; "
          f"PSD defect on all")
    print(f"  (7) sandwich: {len(POS)} rows with A > 0 and eps > 0, width "
          f"<= {wid:.6f}; sign equivalence both directions")
    print(f"  (8) Perron implication: {n_hyp}/{len(PER)} rows satisfy "
          f"S^-1 > 0, 0 exceptions to the conclusion")
    print(f"  (9) counting chain: 0 exceptions on {len(INST)} instances + "
          f"{len(RND)} profiles (s_2 <= {s2_max}); TV rewrite {tv_r:.1e}")
    return summary("PRIME.MARGIN.IDENT.01 margin-chain identities")


if __name__ == "__main__":
    raise SystemExit(run())
