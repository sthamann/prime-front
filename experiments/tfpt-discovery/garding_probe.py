"""Discovery probe: THE DISCRETE GARDING INEQUALITY -- measuring the
named missing W2 building block

    Q_M(v)  >=  c ||v||_Hlog^2  -  C ||v||_L2^2      (M-independent c, C)

on the hat-Galerkin lattice family of the Weil window form
(w2_mosco_probe A5(a): "the proof needs a discrete Garding-type
inequality ... then Suzuki Prop. 4.1 compactness transfers and the
Mosco liminf follows").  This probe MEASURES the best constants; it
proves nothing and claims nothing.

THE MEASURED OBJECT.  For a window [-a, a] with M cells (D = 2a/M,
interior hats j = 1..M-1) let Q_M be the certified layerwise
hat-Galerkin matrix of the Weil window form (w2_mosco_probe route,
verbatim: smooth TRUE-screw layer by Gauss + exact mpmath d <= 2,
atom layer closed B-spline, pole layer closed), G_M the exact
tridiagonal L^2 Gram, and H_M the H_log GRAM MATRIX

    H_M[j,k] = (1/pi) int_0^T ker(t)^2 log(2 + t) cos(t (j-k) D) dt,
    ker(t)   = D sinc^2(t D / 2),   T = 3000, dt = 0.025

(the EXACT Gram of the w2_mosco A3 H_log functional on pw-linear
nodal vectors, Toeplitz; the T-truncation is a declared convention
of the measured norm).  Then the LARGEST c with Q_M + C G_M >= c H_M
is the minimal generalized eigenvalue
c(M, C) = lambda_min(Q_M + C G_M, H_M).

CALIBRATION HISTORY (declared -- honesty first): run 1 (2026-08-02)
used the w2_mosco convention T = 1500 and FAILED its own weight-1
companion guard at the two deepest ratio-2 builds (h = 1027, M =
2054 and h = 1433, M = 2866: d1 = 7.6e-3 / 7.4e-3 > 5e-3) -- exactly
the predicted T^-3 truncation systematic ~ 3/(pi (T D)^3) at the
smallest D.  THIS version doubles T to 3000 at the same dt (the
systematic drops ~8x and meets the bar everywhere); all run-1
constants reproduce at the 1e-3 level.  Nothing else changed.

SLICES AND BARS (declared BEFORE the numbers):

  G0   guards: AST zero-firewall; layered lag assembly == verbatim
       w2_mosco assembly (rel < 1e-12, two summation orders) at
       (a0, 92) and (a0, 736); the w2_mosco spectral anchors at
       a0 = log 16 (parity identity < 1e-10 per M, |lambda_1(736,
       full)| <= 5e-9, ladder monotone within the solver floor
       20 eps rad n); H-Gram sanity per used (a, M): the weight-1
       companion lags reproduce the exact mass lags (rel < 5e-3 on
       d = 0, 1; |l_d|/(2D/3) < 5e-3 for d >= 2 -- the Parseval-
       truncation systematic), H admits a Cholesky factorization
       (positive definite; min eig printed on the anchor ladder);
       direct cross-check at (a0, 368): v^T H v equals the direct
       FT read of N^2(v) (w2_mosco A3 route on this probe's grid)
       to rel 1e-9 on 2 fixed test vectors; the B2 mass-lag +
       Cholesky guards are collected into one summary check after
       the family loop.

  B1   [MEASURED, central] the C-ladder at the anchor window
       a0 = alpha(h = 184) = log 16 on the dyadic refinement
       M = 92/184/368/736: table c(M, C) for C = 0.5/1/2/4.
       STABILIZATION BAR per C: all c(M, C) > 0 AND the last
       relative increment |c(736) - c(368)|/c(736) <= 0.10.
       DEGENERATION READ per C: c(736) < 0.5 c(92) -> degenerating;
       the log-null column c(M, C) log(2 + pi/D_M) is printed (if Q
       controlled only L^2, c would decay like 1/log(2 + pi/D)),
       plus a TWO-MODEL log-null diagnostic at C = 1 and 4 (least
       squares of c(M) on b + a/log(2 + pi/D) vs a/log(2 + pi/D)
       alone; PRINTED, no bar -- declared: a 4-stage dyadic ladder
       cannot separate a positive limit b > 0 from slow 1/log decay,
       and the honest typing carries that ambiguity).

  B2   [MEASURED] uniformity over the WINDOW FAMILY: 5 frame-A
       windows (the anchor + the h-quantile picks 0.25/0.5/0.75/1.0
       among complete windows), fixed M-ratios M = h and M = 2h,
       C = 1 and 4.  UNIFORMITY BAR per (ratio, C): spread
       (max_a c - min_a c)/min_a c <= 0.5.  This is the actual W2
       requirement (a-uniform constants).

  B3   [MEASURED] where the inequality is tight: the minimizing
       vector at (a0, M = 736, C = 1) -- lumped-mass spatial shares
       (|x| > 0.75 a, > 0.9 a), H_log-mass frequency profile
       (shares t <= 20, t > pi/(2D), the lattice-edge band
       [0.8, 1] pi/D, t > pi/D; centroid), layer attribution
       Q(v) = Q_smooth - Q_atom + Q_pole per layer, and the DST
       SYMBOL SWEEP: R_C(k) = (u_k^T (Q + C G) u_k)/(u_k^T H u_k)
       on the Dirichlet modes u_k[j] = sin(pi k j / M); tightness
       ratio c(M, C)/min_k R_C(k) ~ 1 means the minimizer is
       plane-wave-like and the whole inequality is a SYMBOL
       inequality (reported, no bar).

  B4   [C] typing: measured constants + what a proof needs -- the
       symbol-level chain (i) archimedean growth: Re psi(1/4 + it/2)
       - log pi >= c0 log(2 + |t|) - C0 for all real t (digamma
       asymptotics, elementary); (ii) aliasing transfer: the folded
       hat-Galerkin symbol keeps the log growth on [0, pi/D]
       uniformly in M (sinc^4 folding bound); (iii) atom layer
       uniformly dominated: |sigma_atom(t)| <= C1 uniformly in a by
       partial summation of Lambda(n)/sqrt(n) against the Chebyshev
       bound psi(x) <= B_PSI x; (iv) pole layer explicit rank-2
       cosh, positive on the odd sector.  No positivity claim, no
       RH statement, no marker move.

Verdict enums (frozen, precedence top-down): GARDING-MIXED (guards
fail), GARDING-DEGENERATE (any c <= 0 or majority-C halving on the
ladder), GARDING-DRIFT-UNRESOLVED (neither stabilization nor
degeneration bar met), GARDING-STABLE-NONUNIFORM (B1 bar holds, B2
bar fails), GARDING-STABLE-UNIFORM (both hold).

FIREWALL: experiments-only; verification/ read-only (v563 import);
w2_mosco machinery REBUILT verbatim (no probe imports); no marker
moves; NO zero of any L-function is read (AST-checked).
Python-only, per GATE.WOLFRAM.02.

Provenance: w2_mosco_probe (2026-08-02, certified lag route + H_log
machinery + the typed A5(a) remainder), w2_form_density_probe (FEM
slice), w1_theorem_probe (P2.3 layer certification, C0 convention),
Suzuki arXiv:2606.09096 Prop. 4.1 (compact embedding hypothesis).
"""
import ast
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in (
                "zetazero", "nzeros", "second_sheet_zero"):
            return False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("zetazero", "nzeros"):
            return False
    return True


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp  # noqa: E402
import scipy.linalg as sla  # noqa: E402
from numpy.polynomial.legendre import leggauss  # noqa: E402

MS = (92, 184, 368, 736)           # anchor dyadic ladder (w2_mosco)
C_LADDER = (0.5, 1.0, 2.0, 4.0)    # B1 C-ladder
C_B2 = (1.0, 4.0)                  # B2 C values (declared subset)
RATIOS_B2 = (1, 2)                 # B2 fixed M-ratios M = ratio x h
T_MAX, N_T = 3000.0, 120001        # H_log grid (T doubled, run-1 cal.)
FLOOR_SAFETY = 20.0
STAB_BAR = 0.10                    # B1 last-increment bar
UNIF_BAR = 0.50                    # B2 spread bar
BAR_LAYER = 1e-12                  # layered == verbatim lag bar
BAR_PARITY = 1e-10
BAR_LAM736 = 5e-9                  # |lambda_1(736, full)| anchor
BAR_MASS = 5e-3                    # Parseval-truncation lag bar
BAR_DIRECT = 1e-9                  # Gram vs direct FT read
N_LERCH = 20000
_NN_L = np.arange(N_LERCH, dtype=float)
_WTS = 1.0 / (_NN_L + 0.25) ** 2

mp.mp.dps = 30
PSI14_F = float(mp.digamma(mp.mpf(1) / 4))
LOGPI_F = math.log(math.pi)
PHI1_F = float(mp.lerchphi(1, 2, mp.mpf(1) / 4))
UU = np.array([float(u) for u in core.U_ALL])
MU = np.array([float(m) for m in core.MU_ALL])

GX16, GW16 = leggauss(16)

TG = np.linspace(0.0, T_MAX, N_T)
DT = T_MAX / (N_T - 1)
TRAP_W = np.full(N_T, DT)
TRAP_W[0] *= 0.5
TRAP_W[-1] *= 0.5


# ------------------------------------------------- certified lag assembly
def g_smooth_vec(ts):
    """smooth layer of the TRUE screw function (Lerch +1/4), verbatim
    w2_mosco_probe."""
    xf = np.abs(np.asarray(ts, dtype=float))
    out = xf / 2.0 * (LOGPI_F - PSI14_F) - 0.25 * PHI1_F
    lb = np.empty_like(xf)
    for a in range(0, xf.size, 400):
        b = min(xf.size, a + 400)
        E = np.exp(-np.outer(2.0 * xf[a:b], _NN_L) - 0.5 * xf[a:b, None])
        lb[a:b] = E @ _WTS
    return out + 0.25 * lb


def g_sm_mp(tv):
    tv = abs(mp.mpf(tv))
    PHI1m = mp.lerchphi(1, 2, mp.mpf(1) / 4)
    LLm = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)
    if tv == 0:
        return mp.mpf(0)
    return (LLm * tv / 2 - PHI1m / 4 + mp.exp(-tv / 2)
            * mp.lerchphi(mp.exp(-2 * tv), 2, mp.mpf(1) / 4) / 4)


def K_f_factory(D):
    def K_f(x):
        u = np.abs(x) / D
        return np.where(u <= 1.0, D * (2.0 / 3.0 - u ** 2 + u ** 3 / 2.0),
                        np.where(u < 2.0, D * (2.0 - u) ** 3 / 6.0, 0.0))
    return K_f


def galerkin_lags_verbatim(a, M):
    """w2_mosco_probe.galerkin_lags, verbatim (guard reference)."""
    D = 2.0 * a / M
    ss = np.concatenate([0.5 * D * (GX16 + 1) - D, 0.5 * D * (GX16 + 1)])
    ww = np.tile(0.5 * D * GW16, 2) * (D - np.abs(ss))
    ks = np.arange(M)
    vals = g_smooth_vec((ks[:, None] * D + ss[None, :]).ravel())
    II = vals.reshape(M, ss.size) @ ww
    c = np.empty(M - 1)
    for d in range(M - 1):
        c[d] = (2.0 * II[d] - II[abs(d - 1)] - II[d + 1]) / (D * D)
    Dm = mp.mpf(D)
    II_b = {k: mp.quad(lambda s: g_sm_mp(k * Dm + s) * (Dm - abs(s)),
                       [-Dm, 0, Dm]) for k in range(4)}
    for d in range(3):
        c[d] = float((2 * II_b[d] - II_b[abs(d - 1)] - II_b[d + 1])
                     / Dm ** 2)
    dd_grid = np.arange(M - 1) * D
    K_f = K_f_factory(D)
    ka = core.atoms_in(a)
    for u_j, m_j in zip(UU[:ka], MU[:ka]):
        c -= 0.5 * m_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))
    Xp = math.exp(D / 2) + math.exp(-D / 2) - 2.0
    c += 2.0 * np.cosh(dd_grid / 2.0) * 16.0 * Xp ** 2 / (D * D)
    return c, D


def galerkin_layers(a, M):
    """the same assembly, layer-resolved: total = c_sm - c_at + c_po."""
    D = 2.0 * a / M
    ss = np.concatenate([0.5 * D * (GX16 + 1) - D, 0.5 * D * (GX16 + 1)])
    ww = np.tile(0.5 * D * GW16, 2) * (D - np.abs(ss))
    ks = np.arange(M)
    vals = g_smooth_vec((ks[:, None] * D + ss[None, :]).ravel())
    II = vals.reshape(M, ss.size) @ ww
    c_sm = np.empty(M - 1)
    for d in range(M - 1):
        c_sm[d] = (2.0 * II[d] - II[abs(d - 1)] - II[d + 1]) / (D * D)
    Dm = mp.mpf(D)
    II_b = {k: mp.quad(lambda s: g_sm_mp(k * Dm + s) * (Dm - abs(s)),
                       [-Dm, 0, Dm]) for k in range(4)}
    for d in range(3):
        c_sm[d] = float((2 * II_b[d] - II_b[abs(d - 1)] - II_b[d + 1])
                        / Dm ** 2)
    dd_grid = np.arange(M - 1) * D
    K_f = K_f_factory(D)
    ka = core.atoms_in(a)
    c_at = np.zeros(M - 1)
    for u_j, m_j in zip(UU[:ka], MU[:ka]):
        c_at += 0.5 * m_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))
    Xp = math.exp(D / 2) + math.exp(-D / 2) - 2.0
    c_po = 2.0 * np.cosh(dd_grid / 2.0) * 16.0 * Xp ** 2 / (D * D)
    return c_sm, c_at, c_po, D


def toeplitz_of(lags, n):
    idx = np.abs(np.arange(n)[:, None] - np.arange(n)[None, :])
    return lags[idx]


def mass_of(D, n):
    Mass = np.zeros((n, n))
    np.fill_diagonal(Mass, 2.0 * D / 3.0)
    rng_ = np.arange(n - 1)
    Mass[rng_, rng_ + 1] = D / 6.0
    Mass[rng_ + 1, rng_] = D / 6.0
    return Mass


def parity_projectors(M):
    n = M - 1
    hh = M // 2
    P_odd = np.zeros((hh - 1, n))
    for i in range(1, hh):
        P_odd[i - 1, i - 1] = 1.0 / math.sqrt(2.0)
        P_odd[i - 1, M - i - 1] = -1.0 / math.sqrt(2.0)
    P_ev = np.zeros((hh, n))
    for i in range(1, hh):
        P_ev[i - 1, i - 1] = 1.0 / math.sqrt(2.0)
        P_ev[i - 1, M - i - 1] = 1.0 / math.sqrt(2.0)
    P_ev[hh - 1, hh - 1] = 1.0
    return P_odd, P_ev


# ------------------------------------------------- the H_log Gram
def hlog_lags(D, n):
    """Toeplitz lags of the H_log Gram (weight log(2+t)) and of the
    weight-1 companion (the Parseval guard) on the w2_mosco grid."""
    ker2 = (D * np.sinc(TG * D / (2.0 * math.pi)) ** 2) ** 2
    w_log = ker2 * np.log(2.0 + TG) * TRAP_W / math.pi
    w_one = ker2 * TRAP_W / math.pi
    dd = np.arange(n) * D
    l_log = np.zeros(n)
    l_one = np.zeros(n)
    for a_ in range(0, N_T, 4000):
        b_ = min(N_T, a_ + 4000)
        Cc = np.cos(np.outer(TG[a_:b_], dd))
        l_log += w_log[a_:b_] @ Cc
        l_one += w_one[a_:b_] @ Cc
    return l_log, l_one


def mass_lag_guard(l_one, D, tag):
    d0 = abs(l_one[0] - 2.0 * D / 3.0) / (2.0 * D / 3.0)
    d1 = abs(l_one[1] - D / 6.0) / (D / 6.0)
    d2 = float(np.max(np.abs(l_one[2:]))) / (2.0 * D / 3.0)
    ok = d0 < BAR_MASS and d1 < BAR_MASS and d2 < BAR_MASS
    return ok, "%s: d0 %.1e / d1 %.1e / d>=2 %.1e" % (tag, d0, d1, d2)


def hlog_direct(v_full, xs):
    """the w2_mosco A3 route: N^2 = (1/pi) int (ker |S|)^2 log(2+t) dt
    with S(t) = sum_j v_j e^{-i t x_j} (chunked)."""
    D = xs[1] - xs[0]
    ker = D * np.sinc(TG * D / (2.0 * math.pi)) ** 2
    w_log = np.log(2.0 + TG)
    tot = 0.0
    for a_ in range(0, N_T, 6000):
        b_ = min(N_T, a_ + 6000)
        S = np.exp(-1j * np.outer(TG[a_:b_], xs)) @ v_full
        P2 = (ker[a_:b_] * np.abs(S)) ** 2
        tot += float(np.sum(P2 * w_log[a_:b_] * TRAP_W[a_:b_]))
    return tot / math.pi


def build_QGH(a, M, layers=False):
    """Q (total form), Mass, H, D at window a with M cells; optionally
    the layer matrices (Q_sm, Q_at, Q_po)."""
    c_sm, c_at, c_po, D = galerkin_layers(a, M)
    n = M - 1
    c_tot = c_sm - c_at + c_po
    Q = toeplitz_of(c_tot, n)
    Mass = mass_of(D, n)
    l_log, l_one = hlog_lags(D, n)
    H = toeplitz_of(l_log, n)
    out = dict(Q=Q, Mass=Mass, H=H, D=D, l_one=l_one, n=n)
    if layers:
        out["Qsm"] = toeplitz_of(c_sm, n)
        out["Qat"] = toeplitz_of(c_at, n)
        out["Qpo"] = toeplitz_of(c_po, n)
    return out


def gen_min(A, B):
    w = sla.eigvalsh(0.5 * (A + A.T), 0.5 * (B + B.T),
                     subset_by_index=[0, 0])
    return float(w[0])


def gen_min_vec(A, B):
    w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (B + B.T),
                    subset_by_index=[0, 0])
    return float(w[0]), V[:, 0]


def dst_quotients(Q, Mass, H, M):
    """num_Q, num_G, den_H over the Dirichlet modes u_k, k = 1..M-1."""
    j = np.arange(1, M, dtype=float)
    U = np.sin(math.pi * np.outer(j, j) / M)
    nQ = np.einsum("ij,ij->j", U, Q @ U)
    nG = np.einsum("ij,ij->j", U, Mass @ U)
    dH = np.einsum("ij,ij->j", U, H @ U)
    return nQ, nG, dH


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE DISCRETE GARDING INEQUALITY -- measured constants for "
          "Q_M >= c H_log - C L^2")
    print("=" * 78)

    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    # ------------------------------------------------ anchor window
    kz0 = core.frame_a_zones()[0]
    r0 = core.build_window(kz0)
    a0 = r0["alpha"]
    print("anchor window: a0 = alpha(h = %d) = %.12f (= log %d); "
          "ladder M = %s" % (r0["h"], a0, r0["n_zone"], list(MS)))

    # layered == verbatim guard
    devs = []
    for M in (92, 736):
        c_v, _ = galerkin_lags_verbatim(a0, M)
        c_sm, c_at, c_po, _ = galerkin_layers(a0, M)
        c_l = c_sm - c_at + c_po
        scale = float(np.max(np.abs(c_v)))
        devs.append(float(np.max(np.abs(c_l - c_v))) / scale)
    check("G0.1 [E] layered lag assembly == verbatim w2_mosco "
          "assembly (two float summation orders): max rel dev %s "
          "< %.0e" % (["%.1e" % d for d in devs], BAR_LAYER),
          max(devs) < BAR_LAYER)

    # ------------------------------------------------ B1 ladder
    print("\nB1 -- the C-ladder at a0 = log 16 on M = 92/184/368/736")
    dat = {}
    for M in MS:
        t1 = time.time()
        dat[M] = build_QGH(a0, M, layers=(M == MS[-1]))
        d_ = dat[M]
        w_full = sla.eigvalsh(0.5 * (d_["Q"] + d_["Q"].T),
                              0.5 * (d_["Mass"] + d_["Mass"].T))
        d_["w_full"] = w_full
        rad = max(abs(float(w_full[0])), abs(float(w_full[-1])))
        d_["floor"] = FLOOR_SAFETY * float(np.finfo(float).eps) \
            * rad * (M - 1)
        P_odd, P_ev = parity_projectors(M)
        wo = sla.eigvalsh(P_odd @ d_["Q"] @ P_odd.T,
                          P_odd @ d_["Mass"] @ P_odd.T)
        we = sla.eigvalsh(P_ev @ d_["Q"] @ P_ev.T,
                          P_ev @ d_["Mass"] @ P_ev.T)
        d_["low"] = dict(odd=[float(z) for z in wo[:3]],
                         even=[float(z) for z in we[:3]],
                         full=[float(z) for z in w_full[:3]])
        d_["h_min_eig"] = float(sla.eigvalsh(
            0.5 * (d_["H"] + d_["H"].T))[0])
        print("   M = %3d (D = %.6f): lambda_1(Q, G) = %+.3e (floor "
              "%.1e), min eig H = %.3e  [%.1f s]"
              % (M, d_["D"], w_full[0], d_["floor"], d_["h_min_eig"],
                 time.time() - t1))

    par_dev = max(abs(min(dat[M]["low"]["even"][0],
                          dat[M]["low"]["odd"][0])
                      - dat[M]["low"]["full"][0]) for M in MS)
    mono_ok = True
    for i in range(3):
        tol = max(dat[MS[i]]["floor"], dat[MS[i + 1]]["floor"])
        for s in ("odd", "even", "full"):
            if dat[MS[i + 1]]["low"][s][0] > dat[MS[i]]["low"][s][0] + tol:
                mono_ok = False
    check("G0.2 [E] the w2_mosco spectral anchors reproduce: parity "
          "identity worst |dev| %.1e < %.0e, |lambda_1(736, full)| = "
          "%.1e <= %.0e, ladder monotone within the solver floor"
          % (par_dev, BAR_PARITY, abs(dat[736]["low"]["full"][0]),
             BAR_LAM736),
          par_dev < BAR_PARITY
          and abs(dat[736]["low"]["full"][0]) <= BAR_LAM736
          and mono_ok)

    mass_ok = True
    details = []
    for M in MS:
        ok, det = mass_lag_guard(dat[M]["l_one"], dat[M]["D"],
                                 "M=%d" % M)
        mass_ok = mass_ok and ok
        details.append(det)
    h_pd = all(dat[M]["h_min_eig"] > 0.0 for M in MS)
    check("G0.3 [E] H-Gram sanity on the anchor ladder: weight-1 "
          "companion lags reproduce the exact mass lags within the "
          "declared truncation bar %.0e (%s) and H is positive "
          "definite (min eigs %s)"
          % (BAR_MASS, "; ".join(details),
             ["%.1e" % dat[M]["h_min_eig"] for M in MS]),
          mass_ok and h_pd)

    M_chk = 368
    d_ = dat[M_chk]
    xs = -a0 + d_["D"] * np.arange(M_chk + 1)
    dev_dir = 0.0
    for f in (lambda x: np.sin(math.pi * x / a0),
              lambda x: (x / a0) * np.exp(-(x / a0) ** 2)):
        v_full = f(xs)
        v_full[0] = v_full[-1] = 0.0
        vi = v_full[1:M_chk]
        quad = float(vi @ (d_["H"] @ vi))
        direct = hlog_direct(v_full, xs)
        dev_dir = max(dev_dir, abs(quad - direct) / direct)
    check("G0.4 [E] the H Gram reproduces the w2_mosco direct FT "
          "read of N^2 at (a0, M = 368) on 2 test vectors: max rel "
          "dev %.1e < %.0e" % (dev_dir, BAR_DIRECT),
          dev_dir < BAR_DIRECT)

    cMC = {}
    vecs736 = {}
    print("\n   c(M, C) = lambda_min(Q + C G, H)   [log-null column: "
          "c x log(2 + pi/D), C = 1]")
    print("   M      " + "".join("   C = %-6.1f" % C for C in C_LADDER)
          + "   c1*log(2+pi/D)")
    for M in MS:
        d_ = dat[M]
        row = []
        for C in C_LADDER:
            A_ = d_["Q"] + C * d_["Mass"]
            if M == MS[-1]:
                c_, v_ = gen_min_vec(A_, d_["H"])
                vecs736[C] = v_
            else:
                c_ = gen_min(A_, d_["H"])
            cMC[(M, C)] = c_
            row.append(c_)
        lognull = cMC[(M, 1.0)] * math.log(2.0 + math.pi / d_["D"])
        cells = "".join("   %+.5f " % c for c in row)
        print("   %3d %s   %.5f" % (M, cells, lognull))
    stab = {}
    degen = {}
    for C in C_LADDER:
        seq = [cMC[(M, C)] for M in MS]
        pos = all(c > 0.0 for c in seq)
        inc = abs(seq[3] - seq[2]) / abs(seq[3]) if seq[3] != 0 else \
            math.inf
        stab[C] = pos and inc <= STAB_BAR
        degen[C] = (not pos) or seq[3] < 0.5 * seq[0]
        gaps = ["%+.1e" % (seq[i + 1] - seq[i]) for i in range(3)]
        print("   C = %.1f: c ladder %s, gaps %s, last rel inc %.4f "
              "(bar %.2f) -> %s%s"
              % (C, ["%.5f" % c for c in seq], gaps, inc, STAB_BAR,
                 "STABILIZES" if stab[C] else "not stabilized",
                 "; DEGENERATION READ: c(736) < 0.5 c(92)"
                 if degen[C] and pos else ""))
    print("   two-model log-null diagnostic (4 points, PRINTED, no "
          "bar -- declared ambiguity):")
    xs_ln = np.array([1.0 / math.log(2.0 + math.pi / dat[M]["D"])
                      for M in MS])
    for C in (1.0, 4.0):
        ys_ln = np.array([cMC[(M, C)] for M in MS])
        A2c = np.column_stack([np.ones(len(MS)), xs_ln])
        bfit, _, _, _ = np.linalg.lstsq(A2c, ys_ln, rcond=None)
        rms2 = float(np.sqrt(np.mean((ys_ln - A2c @ bfit) ** 2)))
        afit = float((xs_ln @ ys_ln) / (xs_ln @ xs_ln))
        rms1 = float(np.sqrt(np.mean((ys_ln - afit * xs_ln) ** 2)))
        print("   C = %.1f: c = %+0.4f + %.4f/log (rms %.1e, implied "
              "c_inf = %+.4f)  vs  c = %.4f/log (rms %.1e, c_inf = 0)"
              % (C, float(bfit[0]), float(bfit[1]), rms2,
                 float(bfit[0]), afit, rms1))
    b1_stable = all(stab[C] for C in C_LADDER)
    b1_degen = any(degen[C] for C in C_LADDER) and \
        sum(1 for C in C_LADDER if degen[C]) >= len(C_LADDER) // 2 + 1
    check("B1.1 [MEASURED, central] the Garding constant ladder at "
          "a0 = log 16: c(M, C) table above; stabilization bar "
          "(all c > 0, last rel increment <= %.2f) %s for C = %s; "
          "measured Garding pair at the finest stage: (c, C) = "
          "(%.5f, 1) and (%.5f, 4)"
          % (STAB_BAR,
             "HOLDS" if b1_stable else "FAILS",
             [("%.1f ok" if stab[C] else "%.1f MISS") % C
              for C in C_LADDER],
             cMC[(736, 1.0)], cMC[(736, 4.0)]), True)

    # ------------------------------------------------ B2 window family
    print("\nB2 -- uniformity over the window family (fixed ratios "
          "M = h, 2h; C = 1, 4)")
    zones = core.frame_a_zones()
    fam = []
    for kz in zones:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        hz = Mz // 2
        complete = math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5
        fam.append((kz, alpha, hz, complete))
    comp = [t for t in fam if t[3]]
    hs_c = np.array([t[2] for t in comp], float)
    picks = [comp[0]]
    for qq in (0.25, 0.5, 0.75, 1.0):
        tgt = float(np.quantile(hs_c, qq))
        cand = min(comp, key=lambda t: abs(t[2] - tgt))
        if all(cand[0] != p[0] for p in picks):
            picks.append(cand)
    picks = sorted(picks, key=lambda t: t[2])
    check("G0.5 [E] family selection: anchor (h = %d, a = log %d) + "
          "h-quantile picks -> %d windows h = %s (all complete)"
          % (r0["h"], r0["n_zone"], len(picks),
             [t[2] for t in picks]),
          len(picks) >= 4 and any(t[0] == kz0 for t in picks))

    b2 = {}
    b2_guards = []
    for kz, alpha, hz, _ in picks:
        for ratio in RATIOS_B2:
            M = ratio * hz
            if kz == kz0 and M in MS:
                d_ = dat[M]
            else:
                t1 = time.time()
                d_ = build_QGH(alpha, M)
                try:
                    sla.cholesky(0.5 * (d_["H"] + d_["H"].T))
                    chol_ok = True
                except sla.LinAlgError:
                    chol_ok = False
                ok_m, det_m = mass_lag_guard(d_["l_one"], d_["D"],
                                             "h=%d,M=%d" % (hz, M))
                b2_guards.append((ok_m and chol_ok,
                                  det_m + ("" if chol_ok
                                           else " CHOLESKY FAIL")))
                print("      built h = %4d, M = %4d (D = %.6f, "
                      "%d atoms)  [%.1f s]"
                      % (hz, M, d_["D"], core.atoms_in(alpha),
                         time.time() - t1))
            for C in C_B2:
                if (hz, ratio, C) not in b2:
                    if kz == kz0 and M in MS:
                        b2[(hz, ratio, C)] = cMC[(M, C)]
                    else:
                        b2[(hz, ratio, C)] = gen_min(
                            d_["Q"] + C * d_["Mass"], d_["H"])
            if not (kz == kz0 and M in MS):
                del d_
    check("G0.6 [E] B2 H-Gram guards on all %d non-anchor builds "
          "(mass lags within %.0e + Cholesky): %s"
          % (len(b2_guards), BAR_MASS,
             "; ".join(det for _, det in b2_guards)),
          all(ok for ok, _ in b2_guards))

    print("\n   c(a, ratio, C) over the family:")
    print("   h       " + "".join("  r=%d,C=%-4.1f" % (r_, C)
                                  for r_ in RATIOS_B2 for C in C_B2))
    for kz, alpha, hz, _ in picks:
        cells = "".join("   %+.5f" % b2[(hz, r_, C)]
                        for r_ in RATIOS_B2 for C in C_B2)
        print("   %4d  %s" % (hz, cells))
    unif = {}
    for r_ in RATIOS_B2:
        for C in C_B2:
            vals = [b2[(t[2], r_, C)] for t in picks]
            spread = (max(vals) - min(vals)) / min(vals) \
                if min(vals) > 0 else math.inf
            unif[(r_, C)] = spread <= UNIF_BAR
            print("   ratio %d, C = %.1f: min %.5f / max %.5f, "
                  "spread %.4f (bar %.2f) -> %s"
                  % (r_, C, min(vals), max(vals), spread, UNIF_BAR,
                     "UNIFORM" if unif[(r_, C)] else "NON-UNIFORM"))
    b2_uniform = all(unif.values())
    check("B2.1 [MEASURED] a-uniformity of the measured Garding "
          "constants at fixed M-ratio (the actual W2 requirement): "
          "%s (spread bar %.2f per (ratio, C))"
          % ("UNIFORM on all four (ratio, C) combinations"
             if b2_uniform else "NON-UNIFORM on %s"
             % [k for k, v in unif.items() if not v], UNIF_BAR), True)

    # ------------------------------------------------ B3 tightness
    print("\nB3 -- where the inequality is tight (a0, M = 736)")
    d7 = dat[736]
    D7 = d7["D"]
    xs7 = -a0 + D7 * np.arange(737)
    for C in (1.0,):
        v = vecs736[C]
        v = v / math.sqrt(float(v @ (d7["Mass"] @ v)))
        v_full = np.zeros(737)
        v_full[1:736] = v
        # lumped-mass spatial shares
        mloc = D7 * v_full ** 2
        tot = float(mloc.sum())
        s90 = float(mloc[np.abs(xs7) > 0.9 * a0].sum()) / tot
        s75 = float(mloc[np.abs(xs7) > 0.75 * a0].sum()) / tot
        # H_log frequency profile
        ker = D7 * np.sinc(TG * D7 / (2.0 * math.pi)) ** 2
        w_log = np.log(2.0 + TG)
        t_edge = math.pi / D7
        prof = np.zeros(N_T)
        for a_ in range(0, N_T, 6000):
            b_ = min(N_T, a_ + 6000)
            S = np.exp(-1j * np.outer(TG[a_:b_], xs7)) @ v_full
            prof[a_:b_] = (ker[a_:b_] * np.abs(S)) ** 2 \
                * w_log[a_:b_] * TRAP_W[a_:b_] / math.pi
        N2 = float(prof.sum())
        cen = float((TG * prof).sum()) / N2
        sh20 = float(prof[TG <= 20.0].sum()) / N2
        sh_half = float(prof[TG > 0.5 * t_edge].sum()) / N2
        sh_band = float(prof[(TG > 0.8 * t_edge)
                             & (TG <= t_edge)].sum()) / N2
        sh_past = float(prof[TG > t_edge].sum()) / N2
        # layer attribution
        q_sm = float(v @ (d7["Qsm"] @ v))
        q_at = float(v @ (d7["Qat"] @ v))
        q_po = float(v @ (d7["Qpo"] @ v))
        q_tot = q_sm - q_at + q_po
        print("   minimizer at C = %.1f (L^2-normalized): H_log(v) = "
              "%.4f, Q(v) = %+.5f = smooth %+.5f - atom %+.5f + "
              "pole %+.5f" % (C, N2, q_tot, q_sm, q_at, q_po))
        print("   spatial (lumped): share |x| > 0.75 a = %.3f, "
              "|x| > 0.9 a = %.3f" % (s75, s90))
        print("   frequency (H_log mass): centroid t = %.1f "
              "(lattice edge pi/D = %.1f); shares t <= 20: %.3f | "
              "t > pi/2D: %.3f | edge band [0.8, 1] pi/D: %.3f | "
              "past edge: %.3f"
              % (cen, t_edge, sh20, sh_half, sh_band, sh_past))
        check("B3.1 [MEASURED] the tight direction at (a0, 736, C = "
              "1): Q(v) = %+.5f with layer split smooth %+.5f / "
              "atom %+.5f / pole %+.5f; H_log profile centroid "
              "t = %.1f with %.3f of the H_log mass at t <= 20 and "
              "%.3f past pi/(2D) -- the read of WHICH kernel layer "
              "controls the log weight" % (q_tot, q_sm, q_at, q_po,
                                           cen, sh20, sh_half), True)

    print("\n   DST symbol sweep R_C(k) (Dirichlet modes; tightness "
          "c/min_k R):")
    tight = {}
    for M in MS:
        d_ = dat[M]
        nQ, nG, dH = dst_quotients(d_["Q"], d_["Mass"], d_["H"], M)
        line = []
        for C in C_LADDER:
            R = (nQ + C * nG) / dH
            kmin = int(np.argmin(R)) + 1
            tight[(M, C)] = (float(R.min()), kmin / M,
                             cMC[(M, C)] / float(R.min()))
            if C == 1.0:
                ks = [max(1, int(round(f * (M - 1))))
                      for f in (0.05, 0.25, 0.5, 0.75, 1.0)]
                line = ["k/M=%.2f: %.4f" % (k / M, R[k - 1])
                        for k in ks]
        print("   M = %3d: profile (C = 1) %s" % (M, " | ".join(line)))
        print("            min_k R and c/min_k R per C: %s"
              % ", ".join("C=%.1f: %.5f at k/M=%.3f (ratio %.4f)"
                          % (C, tight[(M, C)][0], tight[(M, C)][1],
                             tight[(M, C)][2]) for C in C_LADDER))
    v1 = vecs736[1.0]
    j7 = np.arange(1, 736, dtype=float)
    k_at = max(1, min(735, int(round(tight[(736, 1.0)][1] * 736))))
    u_k = np.sin(math.pi * k_at * j7 / 736)
    ov = float(v1 @ (d7["Mass"] @ u_k)) ** 2 \
        / (float(v1 @ (d7["Mass"] @ v1))
           * float(u_k @ (d7["Mass"] @ u_k)))
    check("B3.2 [MEASURED] symbol-level tightness: c(736, C)/"
          "min_k R_C(k) = %s; the minimizer's L^2 overlap with the "
          "argmin Dirichlet mode (k/M = %.3f) is %.3f -- ratio ~ 1 "
          "and large overlap mean the Garding inequality on this "
          "family IS a symbol inequality (the proof target of B4)"
          % (["C=%.1f: %.4f" % (C, tight[(736, C)][2])
              for C in C_LADDER], tight[(736, 1.0)][1], ov), True)

    # ------------------------------------------------ B4 typing
    guards_ok = not any(f.startswith("G0") for f in FAILS)
    if not guards_ok:
        VERDICT = "GARDING-MIXED (guards failed)"
    elif b1_degen or any(cMC[(M, C)] <= 0.0 for M in MS
                         for C in C_LADDER):
        VERDICT = "GARDING-DEGENERATE"
    elif not b1_stable:
        VERDICT = "GARDING-DRIFT-UNRESOLVED"
    elif b2_uniform:
        VERDICT = "GARDING-STABLE-UNIFORM"
    else:
        VERDICT = "GARDING-STABLE-NONUNIFORM"

    check("B4.1 [C] the typed reading: the discrete Garding "
          "inequality Q_M >= c H_log - C L^2 has MEASURED constants "
          "c(736, C = 1) = %.5f / c(736, C = 4) = %.5f at a0 = "
          "log 16 (stabilization %s), family spread over 5 windows "
          "at fixed ratio %s; what a PROOF needs (symbol level): "
          "(i) Re psi(1/4 + it/2) - log pi >= c0 log(2 + |t|) - C0 "
          "on R (digamma growth), (ii) the sinc^4-folded lattice "
          "symbol keeps that growth on [0, pi/D] uniformly in M, "
          "(iii) |sigma_atom(t)| <= C1 uniformly in a via partial "
          "summation against psi(x) <= B_PSI x, (iv) the explicit "
          "rank-2 cosh pole layer.  MEASURED, not proved; no "
          "positivity claim, no RH statement, no marker move; the "
          "w2_mosco A5(a) remainder stays open"
          % (cMC[(736, 1.0)], cMC[(736, 4.0)],
             "holds" if b1_stable else "fails",
             "uniform" if b2_uniform else "NON-uniform"), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01 / W2, Garding round (2026-08-02): the named
  missing W2 building block (w2_mosco A5(a)) -- the discrete Garding
  inequality Q_M >= c ||.||_Hlog^2 - C ||.||_L2^2 with M-independent
  constants -- was MEASURED on the certified layerwise hat-Galerkin
  family.  H_log Gram = exact Toeplitz Gram of the w2_mosco A3
  functional (T = 3000 truncation, declared).  ANCHOR a0 = log 16,
  M = 92/184/368/736, C-ladder 0.5/1/2/4: c(M, C) table measured;
  finest-stage pairs (c, C) = (%.5f, 1), (%.5f, 4); stabilization
  bar (last rel increment <= %.2f) %s.  FAMILY (5 frame-A windows,
  h = %s, fixed ratios M = h, 2h): spread bar %.2f -> %s.
  TIGHTNESS: the minimizing direction at (a0, 736, C = 1) has H_log
  centroid t = %.1f, %.3f of its H_log mass at t <= 20; layer split
  Q(v) = smooth %+.5f - atom %+.5f + pole %+.5f; DST tightness
  c/min_k R = %.4f with L^2 overlap %.3f on the argmin mode -- the
  inequality is symbol-level tight to that ratio.  PROOF TARGET
  (typed, open): (i) Re psi(1/4 + it/2) - log pi >= c0 log(2+|t|) -
  C0; (ii) uniform sinc^4-folding transfer to [0, pi/D]; (iii)
  a-uniform atom-symbol bound via Chebyshev psi(x) <= B_PSI x; (iv)
  positive rank-2 cosh pole layer.  TYPE: measured surrogate of a
  Garding constant, NOT a theorem; Mosco liminf and W2 stay open;
  no marker move.
""" % (cMC[(736, 1.0)], cMC[(736, 4.0)], STAB_BAR,
       "holds for C = %s / fails for C = %s"
       % ([C for C in C_LADDER if stab[C]],
          [C for C in C_LADDER if not stab[C]]),
       [t[2] for t in picks], UNIF_BAR,
       "UNIFORM" if b2_uniform else "NON-UNIFORM",
       cen, sh20, q_sm, q_at, q_po, tight[(736, 1.0)][2], ov))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
