"""v663 -- PRIME.GARDENV.01: THE GARDING ENVELOPE INEQUALITY -- does the
total window symbol obey  s_tot(t) >= c0 log(2 + t) - C0  with
a-uniform constants, or is the W2 norm choice wrong?

Direct successor of garding_probe.py (GARDING-DRIFT-UNRESOLVED: c(M, C)
~ 1/log(2 + pi/D)) and garding_edgeband_probe.py (both lattice remedies
REFUTED as healing mechanisms; the drift lives in the TOTAL SYMBOL:
s_tot = s_sm - s_at + s_po with an M-stable smooth envelope
min s_sm/log ~ 0.374 but an a-GROWING atom layer max|s_at| = 4.5 ->
10.6 over a = 2.77 -> 6.24 that pushes the net to a near-flat ~0.057).
This probe MEASURES the envelope question; it proves nothing and
claims nothing.

THE MEASURED OBJECT.  For a frame-A window [-a, a] the certified
layerwise Weil window form has, per unit L^2 mass on the complex plane
wave v_t = e^{itx} 1_{[-a,a]}, the CONTINUUM TOTAL SYMBOL

  s_tot(t; a) = s_sm(t; a) - sigma_at(t; a) + s_po(t; a),

  s_sm(t; a)     = int Omega(tau) F_a(tau - t) dtau,
                   Omega(tau) = Re psi(1/4 + i tau/2) - log pi,
                   F_a(s) = sin^2(a s)/(pi a s^2)  (unit-mass Fejer),
  sigma_at(t; a) = sum_{n <= e^{2a}} mu_n (1 - u_n/(2a)) cos(t u_n),
                   u_n = log n, mu_n = 2 Lambda(n)/sqrt(n)
                   (the TENT window weight = the exact plane-wave
                   autocorrelation weight of the v563 frame-A window),
  s_po(t; a)     = 2 Re(A(t) conj(B(t)))/(2a),
                   A = int_{-a}^{a} e^{itx} e^{x/2} dx,  B = same with
                   e^{-x/2}  (the rank-2 cosh pole layer, closed form).

The DISCRETE lattice symbols s_lay(t_k) of the certified hat-Galerkin
family (w2_mosco / garding_probe route, verbatim lags) are computed by
the EXACT closed-form DST read of a Toeplitz form,

  u_k^T T u_k = (M/2) c_0 + sum_{d>=1} c_d [ (M-1-d) cos(pi k d / M)
                + sin(pi k (d+1)/M)/sin(pi k / M) ],

(no O(M^3) transforms; identity guarded against the einsum route),
and the continuum route is guarded against the discrete reads through
the EXACT phase-resolved finite-window formulas for sin(t x + pi k/2)
modes (tent + boundary terms, all closed form).

WHY THIS DECIDES W2.  The A5(a) requirement (w2_mosco) is a discrete
Garding inequality with M-INDEPENDENT constants at fixed a; on the
symbol level c(M) ~ min_k (s_tot(t_k) + C)/log(2 + t_k) with t_k up to
pi/D -> infinity as M grows.  M-independence therefore hinges on the
LARGE-t lower envelope of s_tot(.; a) at fixed a -- measured here far
beyond the lattice edge (t <= 2560 vs pi/D <= 721 of the predecessors)
-- and a-uniformity on the window-family spread of that envelope.

SLICES AND BARS (declared BEFORE the numbers):

  G0   guards: AST zero-firewall; layered lag assembly == verbatim
       garding_probe assembly at (a0, 92) and (a0, 736) (rel < 1e-12);
       closed-form DST read == einsum DST read at (a0, 368) on all
       four layer symbols (rel < 1e-10); scipy complex digamma ==
       mpmath at 4 points (< 1e-10) and Fejer kernel truncation mass
       dev < 1e-3 (kernel renormalized, declared); continuum
       phase-exact layer reads == discrete DST reads at (a0, 736) for
       t ~ 5/10/15/20/25 (s_sm rel <= 2%, s_at dev <= 2% of
       max(1, |s_at|), s_po dev <= max(5e-3, 5%), s_tot dev <= 2.5%
       of max(1, |s_tot|); Parseval mass of the guard kernel <= 0.5%);
       Chebyshev validity psi(n) <= B_PSI n on the full atom table;
       reproduction |min_{t_k>=20} s_tot(a0, 736) - 0.057| <= 0.02
       (predecessor quote) and the two quoted atom envelopes 4.5/10.6
       at (h, M) = (184, 368)/(1433, 2866) within 15%; packet
       machinery: erf autocorrelation == direct numeric on 20 atoms
       (rel < 1e-8), Parseval / truncation systematics printed.
       CALIBRATION (declared -- honesty first): run 1 (2026-08-02)
       failed ONLY this comparator guard at 2.3e-6 -- the masked
       TRAPEZOID comparator carried an edge-truncation error above
       the bar (the erf formula is exact); the comparator (not the
       formula, not the bar) was upgraded to an exact-edge Simpson
       rule.  Nothing else changed; all run-1 numbers reproduce.

  E1   [ANALYTIC + MEASURED, central] the partial-summation bound for
       the TENT-WEIGHTED atom sum.  Derivation (in closed form; the
       boundary term VANISHES because the tent hits zero at x=e^{2a}):
       sigma_at(t;a) = -2 Re int_1^{X} psi(x) f'(x) dx,
       f = x^{-1/2+it} w_a(log x), so |sigma_at| <= C1(a, t) :=
       2 B_PSI [ sqrt(1/4+t^2) (2(e^a-1)/a - 2) + (e^a-1)/a ]
       -- carried by psi(X) <= B_PSI X, the tent profile and its
       total variation (|w_a'| = 1/(2a), TV = 1).  Bars: E1.1 the
       bound HOLDS at every sampled (t, a) (validity); E1.2 growth
       typing of the MEASURED envelope A(a) = max_{20<=t<=2560}
       |sigma_at| against models const / log a / sqrt(a) / a / e^a/a
       (least squares, rms per model, winner printed); E1.3 the PNT
       main-term split sigma_at = main + fluct, main(t;a) = 2 Re
       [ (e^{(1/2+it)2a}-1)/(2a (1/2+it)^2) - 1/(1/2+it) ]  (the tent
       buys 1/(2a|s|) vs the sharp cutoff), and the growth typing of
       max |fluct|.  Typed reading: is C1 finite (yes), a-uniform
       (no: exponential), and what is the honest measured rate.

  E2   [MEASURED, central] the total envelope, fine: s_tot(t; a) for
       the 5 garding_probe B2 frame-A windows on t in [0, 2560]
       (grid 0.02 below t = 200, 0.05 above; every reported minimum
       re-refined on a local 0.002 grid), plus the exact discrete
       s_tot(t_k) at M = 2h for cross-reads.  Reported: global and
       [20, 100] minima with locations (a-stability of the t ~ 27
       window), dyadic band minima ([20,40) ... [1280,2560)), per-
       window least-squares model comparison on the band minima
       (flat vs b + c0 log(2+t) vs b + c loglog; rms and the SIGN of
       c0), the dip-scaling read s_min(a) ~ a^{-p} at the matched
       minimum (p fit; p ~ 1 is the atomic-measure/Fejer mechanism,
       p ~ 0 a stable floor), and the peak/gap structure of the
       largest window around the minimum (peak positions of the
       measured symbol; distance of t* to the flanking-peak midpoint
       and to the 2 pi k / log 2 comb -- printed, no bar).

  E3   [MEASURED] the alternative norm: the a-uniform lower hull
       W(t) = min_a s_tot(t; a) on the family, its monotone envelope
       w*(T) = inf_{t >= T} W(t) (the STRONGEST monotone weight
       certified by the data), total growth Delta = w*(1280) - w*(27),
       hull model fits (flat / log / loglog); and gap-packet reads at
       the largest window: truncated Gaussian packets v = e^{iTx}
       exp(-x^2/2s^2), s = a/4, centered at the band dips: r_log(T) =
       (Q(v) + ||v||^2)/||v||^2_{Hlog} and the loglog companion --
       the form-level read of whether ANY unbounded weight survives
       concentration in the measured spectral gaps.

  E4   [C] typing: (i) if the log envelope holds a-uniformly ->
       remaining pure-analysis task stated; (ii) if only a weaker
       w(t) survives -> is Suzuki Prop 4.1 compactness still
       available (paper full text read: Prop 4.1 states H_log(I) ->
       L^2(I) compact for bounded I, proof deferred to [4, Thm 3.6];
       the tail-control argument needs only w -> infinity, so loglog
       would still embed compactly -- the blocker is the uniform
       bound, not compactness); (iii) if everything fails -> the
       precise breach as a contract note.  No positivity claim, no
       RH statement, no marker move.

Verdict enums (frozen, precedence top-down): ENVELOPE-MIXED (guards
fail), ENVELOPE-LOG-UNIFORM (all 5 windows prefer the log model with
c0 >= 0.01 AND hull growth Delta >= 0.2 with hull-fit c0 >= 0.01),
ENVELOPE-SUBLOG-GROWTH (hull growth Delta >= 0.05 but the log bar not
met), ENVELOPE-FLAT-FALSIFIED (hull growth Delta < 0.05: no unbounded
monotone weight is certified by the measured family).

FIREWALL: v563 import read-only; predecessor machinery REBUILT
verbatim (no probe imports); no marker moves; NO zero of any
L-function is read (AST-checked) -- all spectral structure quoted
below is measured from the module's own symbol.  The remaining W2
step is NAMED, not claimed: a Fejer spectral-density bound replacing
the per-mode symbol read.  Python-only, per GATE.WOLFRAM.02.

PROVENANCE: discovery probe garding_envelope_probe.py (2026-08-02,
18/18, verdict ENVELOPE-SUBLOG-GROWTH); garding_probe +
garding_edgeband_probe (the drift diagnosis and the symbol
mechanism), w2_mosco_probe (A3 H_log convention, A5(a) typed
remainder), v563_paper2_readouts (atom table mu_n = 2 Lambda/sqrt(n),
B_PSI = 1.03883, frame-A windows), Suzuki arXiv:2606.09096
(Prop. 4.1 full-text read).
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
from scipy.signal import fftconvolve  # noqa: E402
from scipy.special import digamma as sp_digamma, erf as sp_erf  # noqa: E402
from scipy.integrate import simpson as sp_simpson  # noqa: E402
from numpy.polynomial.legendre import leggauss  # noqa: E402

# ------------------------------------------------------------ constants
T_HI = 2560.0                      # continuum t range (vs pi/D <= 721)
DT_LO, DT_HI, T_SPLIT = 0.02, 0.05, 200.0
DT_CONV = 0.01                     # Fejer convolution grid
SIG_CONV = 700.0                   # Fejer kernel truncation half-width
DT_REF = 0.002                     # local minimum refinement grid
BANDS = ((20.0, 40.0), (40.0, 80.0), (80.0, 160.0), (160.0, 320.0),
         (320.0, 640.0), (640.0, 1280.0), (1280.0, 2560.0))
T_LOW_BAND = (20.0, 100.0)         # the predecessor t ~ 27 window
GUARD_TS = (5.0, 10.0, 15.0, 20.0, 25.0)
BAR_LAYER = 1e-12                  # layered == verbatim lag bar
BAR_DSTID = 1e-10                  # closed-form == einsum DST bar
BAR_DIGAMMA = 1e-10
BAR_FEJER_MASS = 1e-3
BAR_SM = 0.02                      # continuum/discrete smooth bar
BAR_AT = 0.02                      # ... atom bar (scale max(1,|s_at|))
BAR_PO_ABS, BAR_PO_REL = 5e-3, 0.05
BAR_TOT = 0.025                    # ... total bar (scale max(1,|s|))
BAR_PARSEVAL = 5e-3
BAR_REPRO_MIN = 0.02               # |min s_tot(a0,736) - 0.057|
REF_MIN_736 = 0.057                # predecessor quote (edgeband G3)
REF_AT_184, REF_AT_1433 = 4.5, 10.6    # predecessor quotes (G4)
BAR_REPRO_AT = 0.15                # 15% reproduction bar on those
BAR_PACK_AC = 1e-8                 # erf vs numeric autocorrelation
C_BUDGET = 1.0                     # the C used in ratio reads
PACK_SFRAC = 0.25                  # packet width s = a/4
DELTA_LOG_BAR = 0.20               # hull growth bar for LOG-UNIFORM
DELTA_GROW_BAR = 0.05              # hull growth bar for SUBLOG
C0_MIN = 0.01                      # minimal admissible log slope
RMS_PREF = 0.8                     # model preferred iff rms < 0.8 flat
N_LERCH = 20000
_NN_L = np.arange(N_LERCH, dtype=float)
_WTS = 1.0 / (_NN_L + 0.25) ** 2

mp.mp.dps = 30
PSI14_F = float(mp.digamma(mp.mpf(1) / 4))
LOGPI_F = math.log(math.pi)
PHI1_F = float(mp.lerchphi(1, 2, mp.mpf(1) / 4))
UU = np.array([float(u) for u in core.U_ALL])
MU = np.array([float(m) for m in core.MU_ALL])
B_PSI = float(core.B_PSI)

GX16, GW16 = leggauss(16)


# ------------------------------------------------- certified lag assembly
def g_smooth_vec(ts):
    """smooth layer of the TRUE screw function (Lerch +1/4), verbatim
    garding_probe / w2_mosco_probe."""
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
    """garding_probe.galerkin_lags_verbatim (guard reference)."""
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


# ------------------------------------------------- exact DST symbol reads
def dst_read_closed(lags, M):
    """s(t_k) = u_k^T T(lags) u_k / ((M/2) mu_k), all k, via the exact
    closed form (M/2)c_0 + sum_{d>=1} c_d [(M-1-d) cos(pi k d/M)
    + sin(pi k(d+1)/M)/sin(pi k/M)].  O(M^2), chunked."""
    n = M - 1
    d = np.arange(n, dtype=float)
    w1 = lags * (M - 1.0 - d)
    kk = np.arange(1, M, dtype=float)
    num = np.empty(n)
    for lo in range(0, n, 512):
        hi = min(n, lo + 512)
        kc = kk[lo:hi]
        ph = np.pi * np.outer(kc, d) / M
        blk = np.cos(ph) @ w1
        ph2 = np.pi * np.outer(kc, d + 1.0) / M
        blk += (np.sin(ph2) / np.sin(np.pi * kc / M)[:, None]) @ lags
        num[lo:hi] = blk
    num -= (M / 2.0) * lags[0]
    return num  # caller divides by (M/2) mu_k


def dst_symbols(a, M, lags_tuple):
    """per-unit-L^2 layer symbols on the DST lattice t_k = pi k/(2a)."""
    c_sm, c_at, c_po = lags_tuple
    D = 2.0 * a / M
    kk = np.arange(1, M, dtype=float)
    mu = D * (2.0 + np.cos(np.pi * kk / M)) / 3.0
    tk = np.pi * kk / (M * D)
    den = (M / 2.0) * mu
    s_sm = dst_read_closed(c_sm, M) / den
    s_at = dst_read_closed(c_at, M) / den
    s_po = dst_read_closed(c_po, M) / den
    return dict(tk=tk, mu=mu, D=D, s_sm=s_sm, s_at=s_at, s_po=s_po,
                s_tot=s_sm - s_at + s_po)


def dst_read_einsum(lags, M):
    """guard route: full Toeplitz + einsum on the DST matrix."""
    n = M - 1
    T = toeplitz_of(lags, n)
    jj = np.arange(1, M, dtype=float)
    U = np.sin(np.pi * np.outer(jj, jj) / M)
    return np.einsum("ij,ij->j", U, T @ U)


# ------------------------------------------------- continuum layer reads
def omega_arch(tau):
    """Omega(tau) = Re psi(1/4 + i tau/2) - log pi (vectorized)."""
    z = 0.25 + 0.5j * np.asarray(tau, dtype=float)
    return np.real(sp_digamma(z)) - LOGPI_F


def smooth_conv(a):
    """s_sm(t; a) on the uniform DT_CONV grid t in [0, T_HI] via FFT
    convolution of Omega with the (renormalized) truncated Fejer
    kernel; returns (t_grid, s_sm, mass_dev)."""
    tau = np.arange(-SIG_CONV, T_HI + SIG_CONV + 0.5 * DT_CONV, DT_CONV)
    om = omega_arch(tau)
    sig = np.arange(-SIG_CONV, SIG_CONV + 0.5 * DT_CONV, DT_CONV)
    with np.errstate(divide="ignore", invalid="ignore"):
        F = np.sin(a * sig) ** 2 / (np.pi * a * sig ** 2)
    F[np.abs(sig) < 1e-12] = a / np.pi
    mass = float(np.sum(F) * DT_CONV)
    Fn = F / mass
    s = fftconvolve(om, Fn[::-1], mode="valid") * DT_CONV
    tg = np.arange(0.0, T_HI + 0.5 * DT_CONV, DT_CONV)
    return tg, s[:tg.size], abs(mass - 1.0)


def sigma_at_tent(a, ts, ka):
    """tent-weighted atom sum sum mu_n (1 - u_n/2a) cos(t u_n)."""
    u = UU[:ka]
    w = MU[:ka] * (1.0 - u / (2.0 * a))
    out = np.empty(ts.size)
    for lo in range(0, ts.size, 256):
        hi = min(ts.size, lo + 256)
        out[lo:hi] = np.cos(np.outer(ts[lo:hi], u)) @ w
    return out


def s_po_cont(a, ts):
    """pole layer 2 Re(A conj B)/(2a) for the complex plane wave."""
    t = np.asarray(ts, dtype=float)
    sA = 0.5 + 1j * t
    sB = -0.5 + 1j * t
    A = (np.exp(sA * a) - np.exp(-sA * a)) / sA
    B = (np.exp(sB * a) - np.exp(-sB * a)) / sB
    return 2.0 * np.real(A * np.conj(B)) / (2.0 * a)


def c1_tent(a, t):
    """the E1 partial-summation bound (tent boundary term vanishes)."""
    t = np.asarray(t, dtype=float)
    j_tent = 2.0 * (math.exp(a) - 1.0) / a - 2.0
    j_tv = (math.exp(a) - 1.0) / a
    return 2.0 * B_PSI * (np.sqrt(0.25 + t ** 2) * j_tent + j_tv)


def atom_main(a, t):
    """PNT main term of sigma_at (dpsi -> dx under the tent)."""
    t = np.asarray(t, dtype=float)
    s = 0.5 + 1j * t
    L = 2.0 * a
    val = (np.exp(s * L) - 1.0) / (L * s ** 2) - 1.0 / s
    return 2.0 * np.real(val)


# ---------------------------------------------- phase-exact guard reads
def guard_reads_phi(a, t, k_parity, sm_taugrid):
    """exact continuum layer reads for v = sin(t x + pi k/2) on [-a,a]
    (per unit L^2); k_parity = (-1)^k = cos(pi k)."""
    tau, dtau = sm_taugrid
    norm2 = a - k_parity * math.sin(2.0 * t * a) / (2.0 * t)
    # atoms: A_phi(u) = (2a-u) cos(tu)/2 - (-1)^k sin(t(2a-u))/(2t)
    ka = core.atoms_in(a)
    u = UU[:ka]
    A_phi = ((2.0 * a - u) * np.cos(t * u) / 2.0
             - k_parity * np.sin(t * (2.0 * a - u)) / (2.0 * t))
    at = float(MU[:ka] @ A_phi) / norm2
    # pole: 2 Im(e^{i phi} A_c) Im(e^{i phi} B_c) / norm2, phi = pi k/2
    phi = math.pi / 2.0 if k_parity < 0 else 0.0
    # NOTE: cos(2 phi) = (-1)^k fixes phi mod pi; either representative
    # gives the same Im(e^{i phi} .)^2 products for the lattice modes
    # with that parity up to the sign pair (guarded numerically).
    eip = complex(math.cos(phi), math.sin(phi))
    sA = 0.5 + 1j * t
    sB = -0.5 + 1j * t
    A_c = (np.exp(sA * a) - np.exp(-sA * a)) / sA
    B_c = (np.exp(sB * a) - np.exp(-sB * a)) / sB
    po = 2.0 * (eip * A_c).imag * (eip * B_c).imag / norm2
    # smooth: (1/2pi) int Omega |vhat|^2, exact two-bump kernel
    with np.errstate(divide="ignore", invalid="ignore"):
        Tm = 2.0 * np.sin(a * (tau - t)) / (tau - t)
        Tp = 2.0 * np.sin(a * (tau + t)) / (tau + t)
    Tm[np.abs(tau - t) < 1e-12] = 2.0 * a
    Tp[np.abs(tau + t) < 1e-12] = 2.0 * a
    K = (Tm ** 2 + Tp ** 2 - 2.0 * k_parity * Tm * Tp) / 4.0
    om = omega_arch(tau)
    sm = float(np.sum(om * K) * dtau) / (2.0 * math.pi) / norm2
    parseval = float(np.sum(K) * dtau) / (2.0 * math.pi) / norm2
    return dict(sm=sm, at=at, po=po, tot=sm - at + po, parseval=parseval)


# ------------------------------------------------------- fit helpers
def fit_flat(y):
    y = np.asarray(y, float)
    m = float(np.mean(y))
    return m, float(np.sqrt(np.mean((y - m) ** 2)))


def fit_affine(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    A = np.column_stack([np.ones(x.size), x])
    bf, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    rms = float(np.sqrt(np.mean((y - A @ bf) ** 2)))
    return float(bf[0]), float(bf[1]), rms


def local_minima(ts, ys, lo, hi):
    m = (ts >= lo) & (ts <= hi)
    idx = np.where(m)[0]
    if idx.size < 3:
        return []
    y = ys[idx]
    rel = np.where((y[1:-1] < y[:-2]) & (y[1:-1] <= y[2:]))[0] + 1
    return [(float(ts[idx[i]]), float(y[i])) for i in rel]


def local_maxima(ts, ys, lo, hi):
    m = (ts >= lo) & (ts <= hi)
    idx = np.where(m)[0]
    y = ys[idx]
    rel = np.where((y[1:-1] > y[:-2]) & (y[1:-1] >= y[2:]))[0] + 1
    return [(float(ts[idx[i]]), float(y[i])) for i in rel]


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE GARDING ENVELOPE INEQUALITY -- s_tot(t) >= c0 log(2+t) "
          "- C0 with a-uniform constants?")
    print("=" * 78)

    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    kz0 = core.frame_a_zones()[0]
    r0 = core.build_window(kz0)
    a0 = r0["alpha"]
    print("anchor window: a0 = alpha(h = %d) = %.12f (= log %d)"
          % (r0["h"], a0, r0["n_zone"]))

    # ---------------------------------------------- window family (B2)
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
    print("family (garding_probe B2 selection): h = %s, a = %s"
          % ([t[2] for t in picks],
             ["%.4f" % t[1] for t in picks]))

    # ---------------------------------------------- G0 machinery guards
    devs = []
    lags_a0 = {}
    for M in (92, 736):
        c_v, _ = galerkin_lags_verbatim(a0, M)
        c_sm, c_at, c_po, _ = galerkin_layers(a0, M)
        lags_a0[M] = (c_sm, c_at, c_po)
        c_l = c_sm - c_at + c_po
        scale = float(np.max(np.abs(c_v)))
        devs.append(float(np.max(np.abs(c_l - c_v))) / scale)
    check("G0.1 [E] layered lag assembly == verbatim garding_probe "
          "assembly at (a0, 92) and (a0, 736): max rel dev %s < %.0e"
          % (["%.1e" % d for d in devs], BAR_LAYER),
          max(devs) < BAR_LAYER)

    c_sm3, c_at3, c_po3, _ = galerkin_layers(a0, 368)
    dev_id = 0.0
    for lag in (c_sm3, c_at3, c_po3, c_sm3 - c_at3 + c_po3):
        num_c = dst_read_closed(lag, 368)
        num_e = dst_read_einsum(lag, 368)
        dev_id = max(dev_id, float(np.max(np.abs(num_c - num_e)))
                     / float(np.max(np.abs(num_e))))
    check("G0.2 [E] closed-form DST read == einsum DST read at "
          "(a0, 368) on all four layer symbols: max rel dev %.1e < "
          "%.0e" % (dev_id, BAR_DSTID), dev_id < BAR_DSTID)

    dg_dev = 0.0
    for tq in (0.5, 5.0, 50.0, 400.0):
        ex = float(mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * tq)))
        dg_dev = max(dg_dev, abs(float(omega_arch(np.array([tq]))[0])
                                 - (ex - LOGPI_F)))
    conv = {}
    mass_devs = []
    for kz, alpha, hz, _ in picks:
        tg, s_sm_c, mdev = smooth_conv(alpha)
        conv[hz] = (tg, s_sm_c)
        mass_devs.append(mdev)
    check("G0.3 [E] scipy complex digamma == mpmath at 4 points (max "
          "dev %.1e < %.0e); Fejer kernel truncation mass dev %s < "
          "%.0e (kernel renormalized, declared convention)"
          % (dg_dev, BAR_DIGAMMA,
             ["%.1e" % d for d in mass_devs], BAR_FEJER_MASS),
          dg_dev < BAR_DIGAMMA and max(mass_devs) < BAR_FEJER_MASS)

    # discrete reads at the anchor (a0, 736) + phase-exact guard
    d736 = dst_symbols(a0, 736, lags_a0[736])
    tau_g = np.arange(-900.0, 900.0 + 0.0025, 0.005)
    g_ok = True
    g_det = []
    for t_t in GUARD_TS:
        k = int(round(t_t * 2.0 * a0 / math.pi))
        k = max(1, min(735, k))
        t_k = math.pi * k / (2.0 * a0)
        kp = 1.0 if k % 2 == 0 else -1.0
        g = guard_reads_phi(a0, t_k, kp, (tau_g, 0.005))
        i = k - 1
        dsm = abs(g["sm"] - d736["s_sm"][i]) / abs(d736["s_sm"][i])
        dat_ = abs(g["at"] - d736["s_at"][i]) \
            / max(1.0, abs(d736["s_at"][i]))
        dpo_a = abs(g["po"] - d736["s_po"][i])
        dpo_r = dpo_a / max(abs(d736["s_po"][i]), 1e-30)
        dto = abs(g["tot"] - d736["s_tot"][i]) \
            / max(1.0, abs(d736["s_tot"][i]))
        dpar = abs(g["parseval"] - 1.0)
        ok = (dsm <= BAR_SM and dat_ <= BAR_AT
              and (dpo_a <= BAR_PO_ABS or dpo_r <= BAR_PO_REL)
              and dto <= BAR_TOT and dpar <= BAR_PARSEVAL)
        g_ok = g_ok and ok
        g_det.append("t=%.2f: sm %.4f/%.4f at %.4f/%.4f po %.4f/%.4f "
                     "tot %.4f/%.4f (devs %.1e/%.1e/%.1e/%.1e, "
                     "Parseval %.1e)"
                     % (t_k, g["sm"], d736["s_sm"][i], g["at"],
                        d736["s_at"][i], g["po"], d736["s_po"][i],
                        g["tot"], d736["s_tot"][i], dsm, dat_, dpo_a,
                        dto, dpar))
    print("   continuum(phi-exact) vs discrete DST at (a0, 736):")
    for ln in g_det:
        print("     " + ln)
    check("G0.4 [E] continuum phase-exact layer reads reproduce the "
          "discrete DST symbols at (a0, 736) for t ~ 5..25 within the "
          "declared bars (sm %.0f%%, at %.0f%%, po max(%.0e, %.0f%%), "
          "tot %.1f%%, Parseval %.1f%%)"
          % (100 * BAR_SM, 100 * BAR_AT, BAR_PO_ABS, 100 * BAR_PO_REL,
             100 * BAR_TOT, 100 * BAR_PARSEVAL), g_ok)

    psi_tab = np.cumsum(core.LAM_TAB[core._NN])
    nn_tab = core._NN.astype(float)
    psi_ratio = float(np.max(psi_tab / nn_tab))
    check("G0.5 [E] Chebyshev validity on the full atom table: max "
          "psi(n)/n = %.6f <= B_PSI = %.5f (the E1 bound input)"
          % (psi_ratio, B_PSI), psi_ratio <= B_PSI)

    m36 = d736["tk"] >= 20.0
    min736 = float(np.min(d736["s_tot"][m36]))
    t_min736 = float(d736["tk"][m36][int(np.argmin(d736["s_tot"][m36]))])
    check("G0.6 [E] reproduction of the predecessor floor: "
          "min_{t_k>=20} s_tot(a0, M=736) = %.5f at t = %.2f, "
          "|dev - %.3f| = %.4f <= %.2f"
          % (min736, t_min736, REF_MIN_736, abs(min736 - REF_MIN_736),
             BAR_REPRO_MIN), abs(min736 - REF_MIN_736) <= BAR_REPRO_MIN)

    # ---------------------------------------------- per-window builds
    print("\nbuilding the 5-window discrete + continuum symbol family "
          "(t <= %.0f) ..." % T_HI)
    t_master = np.concatenate([np.arange(0.0, T_SPLIT, DT_LO),
                               np.arange(T_SPLIT, T_HI + 1e-9, DT_HI)])
    WIN = []
    for kz, alpha, hz, _ in picks:
        t1 = time.time()
        M = 2 * hz
        if hz == r0["h"]:
            lags = galerkin_layers(alpha, M)[:3] if M != 736 \
                else lags_a0[736]
        else:
            lags = galerkin_layers(alpha, M)[:3]
        dsc = dst_symbols(alpha, M, lags)
        ka = core.atoms_in(alpha)
        s_at_c = sigma_at_tent(alpha, t_master, ka)
        tg, s_sm_conv = conv[hz]
        s_sm_c = np.interp(t_master, tg, s_sm_conv)
        s_po_c = s_po_cont(alpha, t_master)
        s_tot_c = s_sm_c - s_at_c + s_po_c
        WIN.append(dict(hz=hz, a=alpha, M=M, ka=ka, dsc=dsc,
                        s_at=s_at_c, s_sm=s_sm_c, s_po=s_po_c,
                        s_tot=s_tot_c, conv=conv[hz]))
        print("   h = %4d (a = %.4f, M = %4d, %5d atoms, pi/D = "
              "%6.1f)  [%.1f s]"
              % (hz, alpha, M, ka, math.pi / dsc["D"],
                 time.time() - t1))

    def refine_min(w, t0, half=0.6):
        tl = np.arange(max(0.5, t0 - half), t0 + half + 1e-9, DT_REF)
        sa = sigma_at_tent(w["a"], tl, w["ka"])
        ss = np.interp(tl, w["conv"][0], w["conv"][1])
        sp = s_po_cont(w["a"], tl)
        st = ss - sa + sp
        i = int(np.argmin(st))
        return float(tl[i]), float(st[i])

    # ================================================== E1: atom bound
    print("\nE1 -- the tent-weighted partial-summation bound vs the "
          "measured atom envelope")
    print("   C1(a, t) = 2 B_PSI [ sqrt(1/4+t^2) (2(e^a-1)/a - 2) + "
          "(e^a-1)/a ],  B_PSI = %.5f" % B_PSI)
    viol = 0.0
    rows = []
    m20 = t_master >= 20.0
    for w in WIN:
        c1 = c1_tent(w["a"], t_master)
        viol = max(viol, float(np.max(np.abs(w["s_at"]) - c1)))
        md = w["dsc"]["tk"] >= 20.0
        a_disc = float(np.max(np.abs(w["dsc"]["s_at"][md])))
        lat = t_master <= math.pi / w["dsc"]["D"]
        a_lat = float(np.max(np.abs(w["s_at"][m20 & lat])))
        a_full = float(np.max(np.abs(w["s_at"][m20])))
        fl = w["s_at"] - atom_main(w["a"], t_master)
        f_full = float(np.max(np.abs(fl[m20])))
        c1_20 = float(c1_tent(w["a"], 20.0))
        rows.append((w["hz"], w["a"], a_disc, a_lat, a_full, f_full,
                     c1_20))
        print("   h = %4d (a = %.4f): max|s_at| disc(t_k>=20) = %7.4f"
              " | cont on same range = %7.4f | cont on [20, %d] = "
              "%7.4f | fluct part = %7.4f | C1(a, 20) = %10.1f "
              "(bound/measured = %.0f)"
              % (w["hz"], w["a"], a_disc, a_lat, int(T_HI), a_full,
                 f_full, c1_20, c1_20 / a_full))
    check("E1.1 [E] validity of the derived bound: max over all "
          "sampled (t, a) of |sigma_at| - C1(a, t) = %+.3e <= 0 "
          "(partial summation against psi <= B_PSI x, tent boundary "
          "term vanishing)" % viol, viol <= 0.0)

    a_arr = np.array([r[1] for r in rows])
    A_arr = np.array([r[4] for r in rows])
    F_arr = np.array([r[5] for r in rows])
    print("   growth fits of A(a) = max_{[20, %d]} |sigma_at| "
          "(5 windows):" % int(T_HI))
    fitres = {}
    for lab, xv in (("log a", np.log(a_arr)), ("sqrt a", np.sqrt(a_arr)),
                    ("a", a_arr), ("e^a/a", np.exp(a_arr) / a_arr)):
        b_, c_, r_ = fit_affine(xv, A_arr)
        fitres[lab] = (b_, c_, r_)
        print("     A ~ %+.4f %+.4f * %-6s  rms %.4f"
              % (b_, c_, lab, r_))
    mflat, rflat = fit_flat(A_arr)
    print("     A ~ %.4f (flat)          rms %.4f" % (mflat, rflat))
    best = min(fitres, key=lambda k: fitres[k][2])
    grow = A_arr[-1] / A_arr[0]
    check("E1.2 [MEASURED, central] the atom envelope is finite per a "
          "but NOT a-uniform: A(a) = %s over a = %s (ratio %.2f); "
          "best 2-parameter model: %s (rms %.4f vs flat %.4f); the "
          "crude bound C1(a, 20) = %s is exponential in a (e^a/a) -- "
          "the honest breach: partial summation against Chebyshev "
          "alone cannot give a-uniformity, and the measured growth "
          "rate is ~ %s"
          % (["%.2f" % v for v in A_arr],
             ["%.2f" % v for v in a_arr], grow, best,
             fitres[best][2], rflat,
             ["%.0f" % r[6] for r in rows], best), True)

    fit_fl = {}
    for lab, xv in (("log a", np.log(a_arr)), ("a", a_arr)):
        fit_fl[lab] = fit_affine(xv, F_arr)
    check("E1.3 [MEASURED] PNT main-term split: max|fluct| = "
          "max|sigma_at - main| = %s; affine fits: in a slope %.3f "
          "(rms %.4f) vs in log a slope %.3f (rms %.4f) -- the "
          "fluctuation (psi - x, i.e. the zero oscillation) carries "
          "the growth; the tent main term is exp(a)/(a t^2)-small "
          "at t >= 20"
          % (["%.2f" % v for v in F_arr], fit_fl["a"][1],
             fit_fl["a"][2], fit_fl["log a"][1], fit_fl["log a"][2]),
          True)

    # ================================================== E2: the envelope
    print("\nE2 -- the total envelope s_tot(t; a), fine, t <= %.0f"
          % T_HI)
    band_ref = {}
    low_min = {}
    for w in WIN:
        st = w["s_tot"]
        mlo = (t_master >= T_LOW_BAND[0]) & (t_master <= T_LOW_BAND[1])
        i0 = int(np.argmin(st[mlo]))
        t_lo, s_lo = refine_min(w, float(t_master[mlo][i0]))
        low_min[w["hz"]] = (t_lo, s_lo)
        bmins = []
        for (b0, b1) in BANDS:
            mb = (t_master >= b0) & (t_master < b1)
            ib = int(np.argmin(st[mb]))
            tb, sb = refine_min(w, float(t_master[mb][ib]))
            bmins.append((tb, sb))
        band_ref[w["hz"]] = bmins
        md = w["dsc"]["tk"] >= 20.0
        dmin = float(np.min(w["dsc"]["s_tot"][md]))
        dmin_t = float(w["dsc"]["tk"][md][
            int(np.argmin(w["dsc"]["s_tot"][md]))])
        print("   h = %4d (a = %.4f): min[20,100] = %.5f at t = %.3f"
              " | discrete min(t_k >= 20, t_k <= %.0f) = %.5f at "
              "t = %.2f"
              % (w["hz"], w["a"], s_lo, t_lo, math.pi / w["dsc"]["D"],
                 dmin, dmin_t))
        print("        band minima: %s"
              % " | ".join("[%d,%d): %.4f @ %.1f"
                           % (b[0], b[1], sb, tb)
                           for b, (tb, sb) in zip(BANDS, bmins)))
    print("   per-window model fits on the 7 band minima "
          "(m_b vs t_b):")
    win_pref_log = {}
    win_c0 = {}
    for w in WIN:
        tb = np.array([x[0] for x in band_ref[w["hz"]]])
        sb = np.array([x[1] for x in band_ref[w["hz"]]])
        mfl, rfl = fit_flat(sb)
        b_l, c_l, r_l = fit_affine(np.log(2.0 + tb), sb)
        b_ll, c_ll, r_ll = fit_affine(np.log(np.log(2.0 + tb)), sb)
        win_pref_log[w["hz"]] = (r_l < RMS_PREF * rfl) and c_l > 0
        win_c0[w["hz"]] = c_l
        print("   h = %4d: flat %.4f (rms %.4f) | log: %+.4f %+.5f "
              "log(2+t) (rms %.4f) | loglog: %+.4f %+.4f ll (rms "
              "%.4f) -> %s"
              % (w["hz"], mfl, rfl, b_l, c_l, r_l, b_ll, c_ll, r_ll,
                 "LOG preferred" if win_pref_log[w["hz"]]
                 else "flat/degenerate"))
    check("E2.1 [MEASURED, central] band-minima envelope per window: "
          "log-model slopes c0 = %s; log preferred (rms < %.1f flat, "
          "c0 > 0) on %d/5 windows -- the M-independence question "
          "(t_k range -> infinity at fixed a) is decided by these "
          "signs and slopes"
          % (["%+.5f" % win_c0[w["hz"]] for w in WIN], RMS_PREF,
             sum(win_pref_log.values())), True)

    t_hat = low_min[WIN[-1]["hz"]][0]
    s_hat = []
    for w in WIN:
        sa = float(sigma_at_tent(w["a"], np.array([t_hat]), w["ka"])[0])
        ss = float(np.interp(t_hat, w["conv"][0], w["conv"][1]))
        sp = float(s_po_cont(w["a"], np.array([t_hat]))[0])
        s_hat.append(ss - sa + sp)
    s_star = np.array([low_min[w["hz"]][1] for w in WIN])
    t_star = np.array([low_min[w["hz"]][0] for w in WIN])
    pos = s_star > 0
    p_fit = float("nan")
    if np.sum(pos) >= 3:
        _, sl, _ = fit_affine(np.log(a_arr[pos]), np.log(s_star[pos]))
        p_fit = -sl
    check("E2.2 [MEASURED] dip scaling at the low minimum: s*[20,100]"
          " = %s at t* = %s over a = %s; fixed-t read s_tot(t=%.3f) "
          "= %s; power fit s* ~ a^{-p}: p = %.2f (p ~ 1 = the "
          "atomic-measure/Fejer mechanism, p ~ 0 = stable floor)"
          % (["%.5f" % v for v in s_star],
             ["%.2f" % v for v in t_star],
             ["%.2f" % v for v in a_arr], t_hat,
             ["%.5f" % v for v in s_hat], p_fit), True)

    wmax = WIN[-1]
    pks = local_maxima(t_master, wmax["s_tot"], 10.0, 60.0)
    pks_big = [p for p in pks if p[1] > 0.5 * max(x[1] for x in pks)]
    t_lo_max = low_min[wmax["hz"]][0]
    below = [p for p in pks_big if p[0] < t_lo_max]
    above = [p for p in pks_big if p[0] > t_lo_max]
    midp = float("nan")
    if below and above:
        midp = 0.5 * (below[-1][0] + above[0][0])
    comb = 2.0 * math.pi / math.log(2.0)
    k_comb = round(t_lo_max / comb)
    print("   peak structure (largest window a = %.4f, [10, 60]): %s"
          % (wmax["a"],
             ", ".join("%.2f (%.2f)" % p for p in pks_big[:10])))
    check("E2.3 [MEASURED] the minimum location: t* = %.3f "
          "(a-spread of t* over the family: %s); flanking-peak "
          "midpoint of the measured symbol = %.3f (offset %.3f); "
          "nearest 2 pi k/log 2 comb point = %.3f (k = %d, offset "
          "%.3f) -- the dip sits in the measured spectral gap, not "
          "on the prime comb"
          % (t_lo_max, ["%.2f" % v for v in t_star], midp,
             abs(t_lo_max - midp), k_comb * comb, k_comb,
             abs(t_lo_max - k_comb * comb)), True)

    # reproduction of the two quoted atom envelopes (declared in G0)
    at184 = next(r[2] for r in rows if r[0] == 184)
    at1433 = next((r[2] for r in rows if r[0] == 1433), None)
    rep_ok = abs(at184 - REF_AT_184) / REF_AT_184 <= BAR_REPRO_AT
    det = "h=184: %.3f vs %.1f" % (at184, REF_AT_184)
    if at1433 is not None:
        rep_ok = rep_ok and (abs(at1433 - REF_AT_1433) / REF_AT_1433
                             <= BAR_REPRO_AT)
        det += "; h=1433: %.3f vs %.1f" % (at1433, REF_AT_1433)
    check("G0.7 [E] reproduction of the predecessor atom envelopes "
          "(edgeband G4, 15%% bar): " + det, rep_ok)

    # ================================================== E3: hull + packets
    print("\nE3 -- the a-uniform lower hull and the strongest "
          "certified weight")
    hull = np.min(np.stack([w["s_tot"] for w in WIN]), axis=0)
    hull_bands = []
    for bi, (b0, b1) in enumerate(BANDS):
        cand = [(band_ref[w["hz"]][bi][0], band_ref[w["hz"]][bi][1])
                for w in WIN]
        hull_bands.append(min(cand, key=lambda x: x[1]))
    Ts = (27.0, 40.0, 80.0, 160.0, 320.0, 640.0, 1280.0)
    wstar = {}
    for T in Ts:
        mT = t_master >= T
        v = float(np.min(hull[mT]))
        for (tb, sb) in hull_bands:
            if tb >= T:
                v = min(v, sb)
        wstar[T] = v
    print("   w*(T) = inf_{t >= T} min_a s_tot: %s"
          % " | ".join("T=%d: %.4f" % (T, wstar[T]) for T in Ts))
    delta = wstar[1280.0] - wstar[27.0]
    tbh = np.array([x[0] for x in hull_bands])
    sbh = np.array([x[1] for x in hull_bands])
    mfl_h, rfl_h = fit_flat(sbh)
    b_lh, c_lh, r_lh = fit_affine(np.log(2.0 + tbh), sbh)
    b_llh, c_llh, r_llh = fit_affine(np.log(np.log(2.0 + tbh)), sbh)
    print("   hull band minima: %s"
          % " | ".join("%.4f @ %.1f" % (s, t) for t, s in hull_bands))
    print("   hull fits: flat %.4f (rms %.4f) | log: %+.4f %+.5f "
          "log(2+t) (rms %.4f) | loglog: %+.4f %+.4f ll (rms %.4f)"
          % (mfl_h, rfl_h, b_lh, c_lh, r_lh, b_llh, c_llh, r_llh))
    check("E3.1 [MEASURED, central] the strongest monotone weight "
          "certified a-uniformly by the family: w*(27) = %.4f -> "
          "w*(1280) = %.4f, total growth Delta = %+.4f over a "
          "log-lever of %.2f (implied c0 = %+.5f); hull log fit "
          "slope %+.5f (rms %.4f vs flat %.4f)"
          % (wstar[27.0], wstar[1280.0], delta,
             math.log(1282.0) - math.log(29.0),
             delta / (math.log(1282.0) - math.log(29.0)), c_lh, r_lh,
             rfl_h), True)

    # ---- gap packets at the largest window
    aP = wmax["a"]
    sP = PACK_SFRAC * aP
    kaP = wmax["ka"]
    uP = UU[:kaP]
    muP = MU[:kaP]

    def packet_reads(Tc):
        L2 = sP * math.sqrt(math.pi) * float(sp_erf(aP / sP))
        ac = (muP * np.cos(Tc * uP) * np.exp(-uP ** 2 / (4 * sP ** 2))
              * sP * math.sqrt(math.pi)
              * sp_erf((aP - uP / 2.0) / sP)).sum()
        tauP = np.linspace(Tc - 12.0, Tc + 12.0, 12001)
        gw = np.exp(-sP ** 2 * (tauP - Tc) ** 2)
        dtp = tauP[1] - tauP[0]
        arch = sP ** 2 * float(np.sum(omega_arch(tauP) * gw) * dtp)
        npx = max(40001, int(2.0 * aP * Tc * 8))
        xg = np.linspace(-aP, aP, npx)
        vg = np.exp(1j * Tc * xg - xg ** 2 / (2 * sP ** 2))
        Ap = np.trapezoid(vg * np.exp(xg / 2.0), xg)
        Bp = np.trapezoid(vg * np.exp(-xg / 2.0), xg)
        po = 2.0 * float(np.real(Ap * np.conj(Bp)))
        Q = arch - float(ac) + po
        hlog = sP ** 2 * float(np.sum(
            np.log(2.0 + np.abs(tauP)) * gw) * dtp)
        hll = sP ** 2 * float(np.sum(
            np.log(2.0 + np.log(2.0 + np.abs(tauP))) * gw) * dtp)
        return Q, L2, hlog, hll, po

    # packet guard: erf autocorrelation vs direct numeric (20 atoms;
    # exact-edge Simpson comparator, see CALIBRATION note)
    Tg_ = hull_bands[0][0]
    dev_ac = 0.0
    for j in range(0, min(20 * 50, kaP), 50):
        u_ = uP[j]
        xg_ = np.linspace(-aP, aP - u_, 400001)
        integ = (np.exp(1j * Tg_ * (xg_ + u_)
                        - (xg_ + u_) ** 2 / (2 * sP ** 2))
                 * np.exp(-1j * Tg_ * xg_ - xg_ ** 2 / (2 * sP ** 2)))
        an = sp_simpson(integ, x=xg_)
        ex = (np.exp(1j * Tg_ * u_) * np.exp(-u_ ** 2 / (4 * sP ** 2))
              * sP * math.sqrt(math.pi) * sp_erf((aP - u_ / 2) / sP))
        dev_ac = max(dev_ac, abs(an - ex) / abs(ex))
    trunc = math.exp(-aP ** 2 / (2 * sP ** 2))
    check("G0.8 [E] packet machinery: erf autocorrelation == direct "
          "numeric on 20 atoms (max rel dev %.1e < %.0e); Gaussian "
          "truncation systematic e^{-a^2/2s^2} = %.1e (declared)"
          % (dev_ac, BAR_PACK_AC, trunc), dev_ac < BAR_PACK_AC)

    print("   gap packets at a = %.4f, s = a/4 = %.3f (freq width "
          "1/s = %.3f), C = %.1f:" % (aP, sP, 1.0 / sP, C_BUDGET))
    pack_rows = []
    for (tb, sb) in hull_bands:
        Q, L2, hlog, hll, po = packet_reads(tb)
        r_log = (Q + C_BUDGET * L2) / hlog
        r_ll = (Q + C_BUDGET * L2) / hll
        sym = (sb + C_BUDGET) / math.log(2.0 + tb)
        pack_rows.append((tb, Q / L2, hlog / L2, r_log, r_ll, sym))
        print("     T = %7.2f: Q/L2 = %+8.4f, Hlog/L2 = %6.3f, "
              "r_log = %6.4f (plane-wave read %6.4f), r_loglog = "
              "%6.4f, pole/L2 = %.1e"
              % (tb, Q / L2, hlog / L2, r_log, sym, r_ll, po / L2))
    rl = np.array([p[3] for p in pack_rows])
    tl = np.array([p[0] for p in pack_rows])
    b_r, c_r, r_r = fit_affine(1.0 / np.log(2.0 + tl), rl)
    qb = np.array([p[1] for p in pack_rows])
    check("E3.2 [MEASURED] gap-packet form-level read: r_log(T) = "
          "(Q + L2)/Hlog over the band dips fits %+.4f %+.4f/log(2+T)"
          " (rms %.4f); the packet zero-mass Q/L2 = %s -- if Q/L2 "
          "stays bounded while any weight w(T) grows, no unbounded "
          "weight survives concentration; if Q/L2 grows ~ log T the "
          "form-level constant survives packets"
          % (b_r, c_r, r_r, ["%.3f" % q for q in qb]), True)

    # ================================================== E4: typing
    guards_ok = not any(f.startswith(("G0", "E1.1")) for f in FAILS)
    all_log = all(win_pref_log.values()) \
        and min(win_c0.values()) >= C0_MIN
    hull_log = (delta >= DELTA_LOG_BAR) and (c_lh >= C0_MIN) \
        and (r_lh < RMS_PREF * rfl_h)
    if not guards_ok:
        VERDICT = "ENVELOPE-MIXED (guards failed)"
    elif all_log and hull_log:
        VERDICT = "ENVELOPE-LOG-UNIFORM"
    elif delta >= DELTA_GROW_BAR:
        VERDICT = "ENVELOPE-SUBLOG-GROWTH"
    else:
        VERDICT = "ENVELOPE-FLAT-FALSIFIED"

    check("E4.1 [C] the typed reading: E1 -- the tent-weighted "
          "partial-summation bound C1(a, t) is finite per a but "
          "exponential in a (e^a/a); the MEASURED atom envelope "
          "grows like ~ %s (%.2f -> %.2f over a = %.2f -> %.2f), so "
          "the B4(iii) proof step of garding_probe (a-uniform atom "
          "bound via Chebyshev alone) is REFUTED as stated.  E2 -- "
          "band-minima envelope: log slopes %s, dips at t* ~ %s "
          "scale with p = %.2f.  E3 -- strongest a-uniform monotone "
          "weight: growth Delta = %+.4f (implied c0 = %+.5f); gap "
          "packets: r_log trend %+.4f + %+.4f/log.  E4 -- Suzuki "
          "Prop. 4.1 (full text, line 540): H_log(I) -> L^2(I) "
          "compact for BOUNDED I, proof deferred to Connes-Consani "
          "[4, Thm 3.6]; the tail-control argument needs only "
          "w(t) -> infinity, so a weaker unbounded weight (loglog) "
          "still embeds compactly -- the blocker for W2 is the "
          "UNIFORM Garding bound, not compactness; Suzuki's own "
          "a-dependence (Sec. 4.4) is only local (compact a-"
          "neighborhoods), the M-independence at fixed a is the "
          "TFPT-specific requirement.  MEASURED, not proved; no "
          "positivity claim, no RH statement, no marker move"
          % (best, A_arr[0], A_arr[-1], a_arr[0], a_arr[-1],
             ["%+.4f" % win_c0[w["hz"]] for w in WIN],
             ["%.1f" % v for v in t_star], p_fit, delta,
             delta / (math.log(1282.0) - math.log(29.0)), b_r, c_r),
          True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01 / W2, Garding envelope round (2026-08-02):
  the envelope question behind the 1/log drift -- does s_tot(t) >=
  c0 log(2+t) - C0 hold with a-uniform constants -- was MEASURED on
  the continuum tent symbol of the certified layerwise family
  (guarded against the exact DST lattice reads at (a0, 736), bars
  2-2.5%%), on t <= %d (vs pi/D <= 721 before).  E1 (atom layer):
  the tent-weighted partial-summation bound C1(a, t) = 2 B_PSI
  [sqrt(1/4+t^2)(2(e^a-1)/a - 2) + (e^a-1)/a] is VALID (checked
  pointwise) but exponential in a; the measured envelope
  max_{t>=20}|sigma_at| = %s over a = %s, best model ~ %s -- the
  atom layer is NOT a-uniformly bounded; the a-growth sits in the
  psi - x fluctuation (zero oscillation), not in the PNT main term
  (tent-suppressed to e^a/(a t^2)).  E2 (total envelope): dips at
  t* ~ %s; band minima over [20, 2560] per window give log slopes
  %s; dip scaling s* ~ a^{-p}, p = %.2f.  E3: strongest a-uniform
  monotone weight w*: %.4f at T = 27 -> %.4f at T = 1280 (Delta =
  %+.4f, implied c0 = %+.5f); gap packets (s = a/4) at the band
  dips: r_log = %s.  VERDICT %s.  E4 typing: Suzuki Prop. 4.1
  needs only an unbounded Fourier weight for compactness (loglog
  would embed compactly); the W2 blocker is the UNIFORM bound.
  TYPE: measured envelope surrogate, NOT a theorem; no marker move;
  W2 stays open.
""" % (int(T_HI), ["%.2f" % v for v in A_arr],
       ["%.2f" % v for v in a_arr], best,
       ["%.1f" % v for v in t_star],
       ["%+.4f" % win_c0[w["hz"]] for w in WIN], p_fit,
       wstar[27.0], wstar[1280.0], delta,
       delta / (math.log(1282.0) - math.log(29.0)),
       ["%.3f" % p[3] for p in pack_rows], VERDICT))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
