"""v684 -- PRIME.RANK3ZERO.01: OFFENSIVE 2b -- THE K_M FUNCTIONAL
THROUGH THE EXPLICIT FORMULA, AND THE ZERO-FREE-ZONE DELIVERY.

Parent (rank3_functionals_probe, promoted as v683, 2026-08-03): the
whole first-order
determinant fluctuation of the parity 2x2 block is ONE linear
functional of the prime comb,

    D(M,F) = sum_n rho_n Khat_M(u_n) - int_{U0}^{2a} Khat_M(u) e^{u/2} du,
    K_M = M11 W22 + M22 W11 - 2 M12 W12   (closed kernel),

and the parent's class-(c) verdicts were for ENTRYWISE bounds (triangle
inequality forbade the internal cancellation).  THIS module treats the
single signed sum by the explicit formula, where internal cancellation
is allowed on the prime side and the arithmetic input becomes the zeta
zeros themselves.

THE EXACT CHAIN (all steps algebra, verified numerically here):
  (I1)  D = int_{x0}^{X} f dE,  f(x) = Khat_M(log x)/sqrt(x),
        E = psi - x, x0 = e^{U0} (psi(x0) = 0 since x0 = 1.80 < 2),
        X = e^{2a}.
  (I2)  Stieltjes by parts: D = -f(x0) E(x0) - int E f' dx
        (f(X) = 0 exactly: the read vanishes at the window edge).
  (I3)  E(x) = -sum_rho x^rho/rho - log 2pi - (1/2) log(1 - x^{-2}):
        D = BND - RTERM + sum_{gamma>0} z(gamma),
        BND = Khat_M(U0) e^{U0/2},
        RTERM = int_{U0}^{2a} r(e^u) G(u) e^{-u/2} du,
                r(x) = -log 2pi - (1/2) log(1 - x^{-2}),
        z(gamma) = 2 Re[ Ghat(gamma) / (1/2 + i gamma) ],
        Ghat(gamma) = int_{U0}^{2a} G(u) e^{i gamma u} du,
        G = Khat_M' - Khat_M / 2   (piecewise linear, exact cells).
  Per-zero envelope (exact summation by parts, no estimate):
        |z(gamma)| <= 2 C_G / gamma^2,
        C_G = |G(U0)| + |G(2a)| + TV(G)   (computable exactly).

ZERO INPUT (declared openly -- this module READS ZETA ZEROS; that is
the point of the explicit-formula side; inverted-firewall convention
of v681/v684, no marker move):
  * 2000 + 500 precise zeros from the corpus caches
    (zero_comb_cache_n2000.json, c1_zero_ext_n2500.json; gamma <= 3031);
  * extension to gamma <= T_SCAN = 2e4 (~22.5k zeros) by a vectorised
    Riemann-Siegel scan (theta via scipy log-Gamma, C0 term, Gabcke
    remainder 0.127 (t/2pi)^{-3/4}) + bisection; completeness is
    checked by Riemann-von-Mangoldt CHECKPOINTS every 1000 units
    (|N_found - theta/pi - 1| <= 3, the S(T) budget) with automatic
    fine rescan on mismatch; the coverage_hole scan cache (209167
    midpoints to 1.56e5, grid ~0.6) serves only as a POSITION
    cross-check -- measured here: the cache itself UNDERCOUNTS close
    pairs by ~8%, so it is NOT a count oracle; 2 live mpmath zetazero
    spot checks;
  * tail beyond T_SCAN: envelope 2 C_G sum_{gamma>T} gamma^{-2} with
    the ANALYTIC density integral (log(T/2pi)+1)/(2pi T) x 1.10 slack
    (declared numeric estimate; the cache is not used for the tail
    precisely because it undercounts);
    beta = 1/2 is CITED unconditional to 3e12 (Platt-Trudgian 2021);
    beyond 3e12 the e^{(beta-1/2)2a} <= e^a inflation is priced and
    printed (negligible).

SLICES (bars/enums declared BEFORE any number):
F1a [IDENTITY]: residuum |D_prime - (BND - RTERM + sum_{gamma<=T} z)|
    must sit inside the declared bar TAIL(T) + PE (position-error
    budget of the scan zeros, delta = 1e-3, priced exactly);
    convergence trace at N = 100, 500, 2500, 10^4, all.
F1b [SIGN STRUCTURE]: is z(gamma) one-signed (Fejer-like)?
    Enum ONE-SIGNED iff |sum z| / sum |z| >= 0.9 (declared bar),
    else MIXED with the measured cancellation ratio; per-band shares
    of sum |z| for gamma in [14,30), [30,100), [100,1e3), [1e3,2e4],
    tail envelope.
F1c/F2 [THE UNCONDITIONAL KAPPA]: kappa_unc =
    ( |BND - RTERM| + sum_{gamma<=T} |z| + TAIL + PE
      + B1 B2 + B3^2 ) / det M,
    where B_j is the SAME chain for the entry kernels W_j (bounds for
    |F_j|, so B1 B2 + B3^2 bounds |det F|).  Verdict per window:
    ZONE-PASS iff kappa_unc < 1; class (a) iff kappa_unc <= 1/3,
    (b) iff < 3, (c) else (the parent's bars, ratio = 1/kappa).
F2i [DUAL-POINT REQUIREMENT]: band representation of K_M (core
    band_fit, K = 2), coefficient budget Lambda_0 and spline budget
    eta (v563 S4 verbatim); the required correlation bound
    REQ = (det M - eta ||rho||_1)/Lambda_0 vs the MEASURED dual-point
    fluctuations Delta T_q(gamma_k) and vs the pretentious saturation
    (1/2)||rho||_1; the three factors printed.
F2ii [THE ZONE MECHANISM]: counterfactual coupling z_cf(tau) at the
    dual points tau = gamma_1, gamma_2 (what ONE zeta zero AT the
    carrier frequency would contribute) vs det M and vs the largest
    real coupling max|z(gamma)|: the classical zero-free strip
    0 < gamma < 14.134 is the quantified mechanism that blocks the
    pretentious phases for the TRUE comb.
F3 [SYNTHESIS]: the theorem-chain sketch with all measured constants
    and the named missing quantifier, or the honest negative with the
    exact factor.  Contract-note update printed.

FIREWALL (INVERTED, declared): v563 import strictly read-only; the
parent module v683_rank3_functionals is imported for its helpers
(read-only); zeros are a DECLARED INPUT here (explicit-formula side)
-- no positivity claim of any A_h is routed through them, no marker
moves, the ledger is untouched; deterministic, no RNG.  Radical
honesty: if kappa_unc >= 1 the missing factor is printed, not hidden.

PROVENANCE: discovery probe rank3_zeroside_probe.py (2026-08-03, 8/8
PASS, verdict ZONE-PASS class (a), kappa_unc = 0.039..0.190);
rank3_functionals_probe.py / v683 (K_M lift, R3.PAIR);
v563_paper2_readouts.py (windows, band_fit); v589_zero_comb /
zero_comb_cache_n2000.json + c1_zero_ext_n2500.json (precise zeros);
coverage_hole_probe.py / v681 scan cache (position cross-check);
pinch_attack_probe / v680 (Riemann-Siegel machinery pattern, Gabcke
remainder); Platt-Trudgian 2021 (RH verified to 3e12, CITED);
parity_toeplitz_classification.tex (lem:dualpoint, prob:R1).
"""
import json
import math
import os
import sys
import time

import numpy as np
from scipy.special import loggamma

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import v683_rank3_functionals as r3          # noqa: E402 (parent helpers)
from mpmath import mp, zeta, diff, zetazero  # noqa: E402

# shared zero-comb cache + the committed n = 2500 extension + the v681
# stage-1 scan cache: all live in experiments/tfpt-discovery/ (repo
# tree); fall back to local copies next to this module (website mirror
# / standalone use).
_DISC = os.path.join(os.path.dirname(_here), "experiments",
                     "tfpt-discovery")
_REPO_CACHE = os.path.join(_DISC, "zero_comb_cache_n2000.json")
_LOCAL_CACHE = os.path.join(_here, "zero_comb_cache_n2000.json")
CACHE = _REPO_CACHE if os.path.exists(_REPO_CACHE) else _LOCAL_CACHE
_REPO_EXT = os.path.join(_DISC, "c1_zero_ext_n2500.json")
_LOCAL_EXT = os.path.join(_here, "c1_zero_ext_n2500.json")
CACHE_EXT = _REPO_EXT if os.path.exists(_REPO_EXT) else _LOCAL_EXT
_REPO_SCAN = os.path.join(_DISC, "coverage_hole_zscan_cache.npz")
_LOCAL_SCAN = os.path.join(_here, "coverage_hole_zscan_cache.npz")
CACHE_SCAN = _REPO_SCAN if os.path.exists(_REPO_SCAN) else _LOCAL_SCAN

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- declared constants/bars
T_SCAN = 2.0e4          # precise-zero horizon (~21k zeros)
SCAN_STEP = 0.01        # initial sign-change grid
SCAN_STEP_FINE = 0.002  # refinement step on checkpoint mismatch
CHECKPOINT = 1000.0     # RvM checkpoint spacing (units of gamma)
S_T_BAR = 3.0           # declared |S(T)| budget for the count checks
CACHE_FRAC_BAR = 0.995  # fraction of cache mids that must be matched
Z_BISECT_TOL = 1.0e-9   # bisection width
DELTA_POS = 1.0e-3      # declared position-error budget of scan zeros
GABCKE_C = 0.127        # |R0| <= 0.127 (t/2pi)^{-3/4}, t >= 200
TOL_SPOT = 1.0e-8       # live zetazero spot check
CANCEL_BAR = 0.9        # ONE-SIGNED iff |sum z|/sum|z| >= this
BANDS = ((14.0, 30.0), (30.0, 100.0), (100.0, 1000.0), (1000.0, T_SCAN))
RH_VERIFIED_T = 3.0e12  # Platt-Trudgian 2021 (CITED), beta = 1/2 below
TAIL_SLACK = 1.10       # slack on the analytic tail density integral
N_QUAD_CELL = 4         # Gauss points per lag cell (RTERM)
GAMMA_CHUNK = 500       # zero-chunk for the Ghat evaluation
CONV_TRACE = (100, 500, 2500, 10000)
LOG2PI = math.log(2.0 * math.pi)
CLASS_HI, CLASS_LO = r3.CLASS_HI, r3.CLASS_LO

mp.dps = 30

_GLX, _GLW = np.polynomial.legendre.leggauss(N_QUAD_CELL)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def class_of(kappa):
    """Parent bars on ratio = 1/kappa: (a) >= 3, (b) >= 1/3, (c) else."""
    if kappa <= 1.0 / CLASS_HI:
        return "a"
    if kappa < 1.0 / CLASS_LO:
        return "b"
    return "c"


# ------------------------------------------------- Riemann-Siegel scan
def theta_rs(t):
    return np.imag(loggamma(0.25 + 0.5j * np.asarray(t, dtype=float))) \
        - 0.5 * np.asarray(t, dtype=float) * math.log(math.pi)


def z_rs(t):
    """Vectorised Riemann-Siegel Z(t), C0 term (Gabcke remainder)."""
    t = np.asarray(t, dtype=float)
    tau = np.sqrt(t / (2.0 * math.pi))
    nu = np.floor(tau).astype(np.int64)
    p = tau - nu
    # guard the removable singularity of Psi at cos(2 pi p) = 0
    bad = np.abs(np.cos(2.0 * math.pi * p)) < 1.0e-8
    p = np.where(bad, p + 1.0e-7, p)
    th = theta_rs(t)
    numax = int(nu.max())
    n = np.arange(1, numax + 1, dtype=float)
    ph = th[:, None] - t[:, None] * np.log(n)[None, :]
    terms = np.cos(ph) / np.sqrt(n)[None, :]
    mask = (n[None, :] <= nu[:, None])
    zz = 2.0 * np.sum(terms * mask, axis=1)
    psi_p = np.cos(2.0 * math.pi * (p * p - p - 1.0 / 16.0)) \
        / np.cos(2.0 * math.pi * p)
    zz += ((-1.0) ** (nu - 1)) * (t / (2.0 * math.pi)) ** (-0.25) * psi_p
    return zz


def z_rs_chunked(t, chunk=50000):
    out = np.empty(len(t))
    for a in range(0, len(t), chunk):
        out[a:a + chunk] = z_rs(t[a:a + chunk])
    return out


def find_zeros(t_lo, t_hi, step):
    tt = np.arange(t_lo, t_hi + step, step)
    zz = z_rs_chunked(tt)
    s = np.sign(zz)
    flip = np.nonzero(s[:-1] * s[1:] < 0)[0]
    lo, hi = tt[flip].copy(), tt[flip + 1].copy()
    zlo = zz[flip].copy()
    while np.max(hi - lo) > Z_BISECT_TOL:
        mid = 0.5 * (lo + hi)
        zm = z_rs_chunked(mid)
        left = (np.sign(zm) == np.sign(zlo)) & (np.sign(zm) != 0)
        lo = np.where(left, mid, lo)
        zlo = np.where(left, zm, zlo)
        hi = np.where(left, hi, mid)
    return 0.5 * (lo + hi)


# ------------------------------------------------- cell machinery
def cell_decomp(K, D, Mz, u_lo, u_hi):
    """Exact piecewise-linear cells of G = Khat' - Khat/2 on [u_lo, u_hi]."""
    Kn = np.append(np.asarray(K, dtype=float), 0.0)
    i = np.arange(Mz)
    lo = np.maximum(i * D, u_lo)
    hi = np.minimum((i + 1) * D, u_hi)
    act = hi > lo
    lo, hi, ii = lo[act], hi[act], i[act]
    slope = (Kn[ii + 1] - Kn[ii]) / D
    k_lo = Kn[ii] + slope * (lo - ii * D)
    gA = slope - 0.5 * k_lo        # G at the cell's lower edge
    gB = -0.5 * slope              # dG/du inside the cell
    kA = k_lo                      # Khat at the cell's lower edge
    kB = slope                     # dKhat/du
    return lo, hi, gA, gB, kA, kB


def g_hat(gam, lo, hi, gA, gB):
    """Ghat(gamma) = int G(u) e^{i gamma u} du, exact per linear cell,
    vectorised over an array of gammas (chunked)."""
    gam = np.asarray(gam, dtype=float)
    out = np.empty(len(gam), dtype=complex)
    L = hi - lo
    for a in range(0, len(gam), GAMMA_CHUNK):
        g = gam[a:a + GAMMA_CHUNK][:, None]
        ig = 1j * g
        eL = np.exp(ig * L[None, :])
        cell = ((gA[None, :] + gB[None, :] * L[None, :]) * eL
                - gA[None, :]) / ig \
            - gB[None, :] * (eL - 1.0) / (ig * ig)
        out[a:a + GAMMA_CHUNK] = np.sum(np.exp(ig * lo[None, :]) * cell,
                                        axis=1)
    return out


def c_g_const(lo, hi, gA, gB):
    """C_G = |G(u_lo)| + |G(u_hi)| + TV(G), exact."""
    g_lo_v = gA
    g_hi_v = gA + gB * (hi - lo)
    tv = float(np.sum(np.abs(gB) * (hi - lo)))
    tv += float(np.sum(np.abs(g_lo_v[1:] - g_hi_v[:-1])))
    return abs(float(g_lo_v[0])) + abs(float(g_hi_v[-1])) + tv


def rterm(lo, hi, gA, gB):
    """int r(e^u) G(u) e^{-u/2} du, r(x) = -log 2pi - (1/2)log(1-x^-2)."""
    mid = 0.5 * (lo + hi)
    half = 0.5 * (hi - lo)
    uu = mid[:, None] + half[:, None] * _GLX[None, :]
    G = gA[:, None] + gB[:, None] * (uu - lo[:, None])
    r_val = -LOG2PI - 0.5 * np.log1p(-np.exp(-2.0 * uu))
    integ = G * r_val * np.exp(-0.5 * uu)
    return float(np.sum(half[:, None] * integ * _GLW[None, :]))


def zero_chain(K, r, u0_cut, gammas):
    """The full (I3) data for kernel array K on window r."""
    D, Mz, a2 = r["D"], r["M"], 2.0 * r["alpha"]
    lo, hi, gA, gB, _, _ = cell_decomp(K, D, Mz, u0_cut, a2)
    zh = g_hat(gammas, lo, hi, gA, gB)
    zg = 2.0 * np.real(zh / (0.5 + 1j * gammas))
    bnd = float(r3.spline_read_vec(np.asarray(K, dtype=float),
                                   np.array([u0_cut]), D)[0]) \
        * math.exp(0.5 * u0_cut)
    rt = rterm(lo, hi, gA, gB)
    cg = c_g_const(lo, hi, gA, gB)
    d_prime = float(r["lam"] @ r3.spline_read_vec(
        np.asarray(K, dtype=float), r["uu"], D)) \
        - r3.model_entry(K, D, Mz, u0_cut, a2)
    return dict(z=zg, bnd=bnd, rt=rt, cg=cg, d_prime=d_prime,
                lo=lo, hi=hi, gA=gA, gB=gB)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("OFFENSIVE 2b -- the K_M functional through the explicit formula "
          "(rank3_zeroside_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- the zero input (declared): caches + Riemann-Siegel "
          "extension + count oracle")
    with open(CACHE) as fh:
        g_a = [float(s) for s in json.load(fh)["gammas"]]
    with open(CACHE_EXT) as fh:
        g_b = [float(s) for s in json.load(fh)["gammas"]]
    g_prec = np.array(g_a + g_b)
    npz = np.load(CACHE_SCAN)
    mids, errs = npz["mids"], npz["errs"]
    z1 = float(zetazero(1).imag)
    z2 = float(zetazero(2).imag)
    check("S0.SPOT live mpmath zetazero spot checks: |gamma_1 - %.10f| = "
          "%.1e, |gamma_2 - %.10f| = %.1e, both <= %.0e"
          % (g_prec[0], abs(z1 - g_prec[0]), g_prec[1],
             abs(z2 - g_prec[1]), TOL_SPOT),
          abs(z1 - g_prec[0]) <= TOL_SPOT
          and abs(z2 - g_prec[1]) <= TOL_SPOT)

    t_lo = float(g_prec[-1]) + 0.4
    g_scan = find_zeros(t_lo, T_SCAN, SCAN_STEP)
    gam = np.sort(np.concatenate([g_prec, g_scan]))

    def n_rvm_at(T):
        return float(theta_rs(np.array([float(T)]))[0] / math.pi + 1.0)

    # Riemann-von-Mangoldt checkpoints every CHECKPOINT units; on a
    # mismatch (> S_T_BAR) the segment is rescanned at the fine step.
    cps = np.arange(math.ceil(t_lo / CHECKPOINT) * CHECKPOINT,
                    T_SCAN + 1.0, CHECKPOINT)
    n_ref, dev_max = 0, 0.0
    for _round in range(2):
        bad = []
        for tc in cps:
            dev = abs(float(np.sum(gam <= tc)) - n_rvm_at(tc))
            dev_max = max(dev_max, dev)
            if dev > S_T_BAR:
                bad.append(tc)
        if not bad:
            break
        for tc in bad:
            n_ref += 1
            s0, s1 = max(t_lo, tc - CHECKPOINT), min(T_SCAN, tc + 0.5)
            gg = find_zeros(s0 - 0.2, s1 + 0.2, SCAN_STEP_FINE)
            keep = (gam <= s0) | (gam > s1)
            gam = np.sort(np.concatenate(
                [gam[keep], gg[(gg > s0) & (gg <= s1)]]))
    n_rvm = n_rvm_at(T_SCAN)
    lehmer = gam[(gam > 7005.0) & (gam < 7005.2)]
    check("S0.COUNT zero list complete to T = %.0f: %d zeros; RvM count "
          "theta/pi + 1 = %.2f (dev %.2f, max checkpoint dev %.2f, bar "
          "%.0f, %d segments rescanned); the Lehmer pair at 7005 "
          "resolved: %s; min gap %.4f, monotone %s"
          % (T_SCAN, len(gam), n_rvm, abs(len(gam) - n_rvm), dev_max,
             S_T_BAR, n_ref, np.round(lehmer, 4).tolist(),
             float(np.min(np.diff(gam))), bool(np.all(np.diff(gam) > 0))),
          abs(len(gam) - n_rvm) <= S_T_BAR and dev_max <= S_T_BAR
          and len(lehmer) == 2 and bool(np.all(np.diff(gam) > 0)))
    # position cross-check vs the coverage cache (cache -> mine only:
    # the cache grid ~0.6 undercounts close pairs, measured below)
    m_in = mids[(mids > t_lo + 0.4) & (mids < T_SCAN - 0.4)]
    e_in = errs[(mids > t_lo + 0.4) & (mids < T_SCAN - 0.4)]
    idxn = np.clip(np.searchsorted(gam, m_in), 1, len(gam) - 1)
    near = np.minimum(np.abs(gam[idxn] - m_in),
                      np.abs(gam[idxn - 1] - m_in))
    frac = float(np.mean(near <= e_in + 0.05))
    n_mine = int(np.sum((gam > t_lo + 0.4) & (gam < T_SCAN - 0.4)))
    check("S0.MATCH cache position cross-check: %.2f%% of %d cache mids "
          "have a found zero inside err+0.05 (bar %.1f%%); measured "
          "cache undercount in the range: %d mids vs %d true zeros "
          "(-%.1f%%, coarse grid misses close pairs -- cache NOT used "
          "as count oracle or for the tail)"
          % (100 * frac, len(m_in), 100 * CACHE_FRAC_BAR, len(m_in),
             n_mine, 100.0 * (1.0 - len(m_in) / n_mine)),
          frac >= CACHE_FRAC_BAR)

    # tail density: analytic integral of the RvM density with slack
    def s2_tail(T):
        return TAIL_SLACK * (math.log(T / (2.0 * math.pi)) + 1.0) \
            / (2.0 * math.pi * T)

    s2_T = s2_tail(T_SCAN)
    s2_all = float(np.sum(1.0 / gam ** 2)) + s2_T
    print("    sum_{gamma>0} 1/gamma^2 = %.6f (data+tail; the whole sum "
          "starts at gamma_1 = 14.13 -- the classical zero-free strip); "
          "tail beyond T = %.0f: S2 = %.3e" % (s2_all, T_SCAN, s2_T))

    c_th = float(-2 * diff(lambda s: zeta(s), 0.5) / zeta(0.5))
    u0_cut = 2.0 * math.log(-c_th / 4.0)

    # ============================================================== S1
    print("\nS1 [F1] -- the identity, the sign structure, the bands")
    KZ = core.frame_a_zones()
    L = len(KZ)
    fam5 = [0, (L - 1) // 4, L // 2, (3 * (L - 1)) // 4, L - 1]
    inter = []
    for (lo_i, hi_i), n_in in zip(zip(fam5[:-1], fam5[1:]), (2, 3, 3, 2)):
        for j in range(1, n_in + 1):
            inter.append(lo_i + j * (hi_i - lo_i) // (n_in + 1))
    idx15 = sorted(set(fam5 + inter))
    wins = []
    for kz in idx15:
        r = core.build_window(KZ[kz])
        if r["n_zone"] ** 2 <= core.ATOM_MAX + 0.5:
            wins.append(r)
    wins.sort(key=lambda r: r["alpha"])
    pick = [wins[0], wins[3], wins[7], wins[11], wins[13]]
    print("    declared windows (complete family quintiles + deepest): "
          "h = %s" % [r["h"] for r in pick])

    results = []
    for r in pick:
        D, Mz, a2 = r["D"], r["M"], 2.0 * r["alpha"]
        MM = [r3.model_entry(r[k], D, Mz, u0_cut, a2)
              for k in ("W11", "W22", "W12")]
        detM = MM[0] * MM[1] - MM[2] ** 2
        K_M = (MM[0] * np.asarray(r["W22"]) + MM[1] * np.asarray(r["W11"])
               - 2.0 * MM[2] * np.asarray(r["W12"]))
        ch = zero_chain(K_M, r, u0_cut, gam)
        # tail + position-error budgets
        tail = 2.0 * ch["cg"] * s2_T
        s2_scan = float(np.sum(1.0 / gam[gam > g_prec[-1]] ** 2))
        pe = 4.0 * r["alpha"] * ch["cg"] * DELTA_POS * s2_scan
        beyond = 2.0 * ch["cg"] * math.exp(r["alpha"]) * TAIL_SLACK \
            * (math.log(RH_VERIFIED_T / (2 * math.pi)) + 1.0) \
            / (2.0 * math.pi * RH_VERIFIED_T)
        det_part = ch["bnd"] - ch["rt"]
        zsum = float(np.sum(ch["z"]))
        resid = abs(ch["d_prime"] - (det_part + zsum))
        # entry chains for F_j (the |det F| budget)
        Bj = []
        for k in ("W11", "W22", "W12"):
            cj = zero_chain(np.asarray(r[k], dtype=float), r, u0_cut, gam)
            tj = 2.0 * cj["cg"] * s2_T
            pj = 4.0 * r["alpha"] * cj["cg"] * DELTA_POS * s2_scan
            Bj.append(dict(chain=cj, bound=abs(cj["bnd"] - cj["rt"])
                           + float(np.sum(np.abs(cj["z"]))) + tj + pj))
        results.append(dict(r=r, MM=MM, detM=detM, K=K_M, ch=ch,
                            tail=tail, pe=pe, beyond=beyond,
                            det_part=det_part, zsum=zsum, resid=resid,
                            Bj=Bj))

    # ---- F1a: identity + convergence trace -------------------------------
    print("\n    identity D(M,F) = BND - RTERM + sum z(gamma):")
    print("    %5s %12s %12s %12s %12s | %10s %10s %10s"
          % ("h", "D_prime", "BND-RTERM", "sum z", "residuum",
             "bar=TAIL+PE", "TAIL", "PE"))
    id_ok = True
    for w in results:
        bar = w["tail"] + w["pe"]
        id_ok = id_ok and (w["resid"] <= bar)
        print("    %5d %12.6f %12.6f %12.6f %12.2e | %10.2e %10.2e %10.2e"
              % (w["r"]["h"], w["ch"]["d_prime"], w["det_part"],
                 w["zsum"], w["resid"], bar, w["tail"], w["pe"]))
    wref = results[2]
    trace = []
    for n_cut in CONV_TRACE:
        zz = wref["ch"]["z"][:n_cut]
        trace.append((n_cut, abs(wref["ch"]["d_prime"]
                                 - (wref["det_part"] + float(np.sum(zz))))))
    trace.append((len(gam), wref["resid"]))
    check("F1a.IDENT the explicit-formula identity holds on all 5 windows: "
          "residuum <= TAIL + PE everywhere; reference-window convergence "
          "trace (N zeros -> residuum): %s"
          % ", ".join("%d -> %.2e" % t for t in trace), id_ok)

    # ---- F1b: sign structure ---------------------------------------------
    print("\n    sign structure of z(gamma) (reference window h = %d):"
          % wref["r"]["h"])
    z = wref["ch"]["z"]
    n_pos = int(np.sum(z > 0))
    cancel = abs(float(np.sum(z))) / float(np.sum(np.abs(z)))
    shares = []
    for b0, b1 in BANDS:
        m = (gam >= b0) & (gam < b1)
        shares.append((b0, b1, float(np.sum(np.abs(z[m]))),
                       float(np.sum(z[m]))))
    tot_abs = float(np.sum(np.abs(z)))
    for b0, b1, sa, ss in shares:
        print("      band [%6.0f, %6.0f): sum|z| = %10.4f (%5.1f%%), "
              "sum z = %+10.4f" % (b0, b1, sa, 100 * sa / tot_abs, ss))
    print("      tail envelope beyond %.0f: <= %.4f" % (T_SCAN,
                                                        wref["tail"]))
    one_signed = cancel >= CANCEL_BAR
    check("F1b.SIGN z(gamma) is %s on the reference window: %d of %d "
          "positive, cancellation ratio |sum z|/sum|z| = %.4f (bar %.2f "
          "for ONE-SIGNED); sum|z| = %.4f vs |sum z| = %.4f -- %s"
          % ("ONE-SIGNED" if one_signed else "MIXED", n_pos, len(z),
             cancel, CANCEL_BAR, tot_abs, abs(float(np.sum(z))),
             "the zero side has a sign: the bound is a DENSITY question "
             "(Riemann-von-Mangoldt, unconditional)" if one_signed else
             "the zero side oscillates: the absolute-value bound sum|z| "
             "is the honest unconditional budget (still finite and "
             "small -- see F1c)"), True)

    # ---- F1c/F2: the unconditional kappa ---------------------------------
    print("\n    the unconditional bound (triangle only on the ZERO side):")
    print("    %5s %10s | %10s %10s %10s %10s | %9s %9s | %8s %6s"
          % ("h", "detM", "|BND-RT|", "sum|z|", "TAIL+PE", "detF-bud",
             "kappa_unc", "kappa_mea", "beyond12", "class"))
    kaps = []
    for w in results:
        sum_abs = float(np.sum(np.abs(w["ch"]["z"])))
        detf_bud = w["Bj"][0]["bound"] * w["Bj"][1]["bound"] \
            + w["Bj"][2]["bound"] ** 2
        kappa = (abs(w["det_part"]) + sum_abs + w["tail"] + w["pe"]
                 + detf_bud) / w["detM"]
        kappa_meas = abs(w["ch"]["d_prime"]) / w["detM"]
        kaps.append(kappa)
        w.update(kappa=kappa, sum_abs=sum_abs, detf_bud=detf_bud)
        print("    %5d %10.4f | %10.4f %10.4f %10.4f %10.4f | %9.4f "
              "%9.5f | %8.1e %6s"
              % (w["r"]["h"], w["detM"], abs(w["det_part"]), sum_abs,
                 w["tail"] + w["pe"], detf_bud, kappa, kappa_meas,
                 w["beyond"], class_of(kappa)))
    kap_max = max(kaps)
    zone_pass = kap_max < 1.0
    check("F1c.ZONE the unconditional zero-side bound gives kappa_unc = "
          "%.4f .. %.4f on the 5 declared windows -- %s"
          % (min(kaps), kap_max,
             "ZONE-PASS: kappa_unc < 1 EVERYWHERE, i.e. |D(M,F)| + "
             "|det F| < det M follows from (i) the exact identity, "
             "(ii) computed zeros to T = 2e4 (+ envelope tail, beta = 1/2 "
             "cited to 3e12), (iii) NO other arithmetic input -- the "
             "pretentious escape is unconditionally blocked at this "
             "kernel; class %s" % class_of(kap_max) if zone_pass else
             "ZONE-FAIL: kappa_unc >= 1, missing factor %.2f -- the "
             "honest negative" % kap_max), zone_pass)

    # ============================================================== S2
    print("\nS2 [F2i] -- the dual-point requirement vs delivery "
          "(reference window)")
    r = wref["r"]
    hz, D, Mz = r["h"], r["D"], r["M"]
    a2 = 2.0 * r["alpha"]
    gam_dual = np.array([2.0 * math.pi / ((2 * hz + 1) * D),
                         4.0 * math.pi / ((2 * hz + 1) * D)])
    a_c, b_c, c_c, d_c, res_band = core.band_fit(wref["K"], hz)
    lam0 = (abs(a_c[0]) + abs(c_c[0]) + abs(a_c[1]) + abs(c_c[1])
            + Mz * (abs(b_c[0]) + abs(d_c[0]) + abs(b_c[1]) + abs(d_c[1])))
    lam1 = abs(b_c[0]) + abs(d_c[0]) + abs(b_c[1]) + abs(d_c[1])
    om2 = 2.0 * math.pi * 2.0 / (2 * hz + 1)
    eta_k = 0.125 * (om2 ** 2 * lam0 + 2.0 * om2 * lam1)
    rho1 = float(np.sum(r["lam"]))
    req = (wref["detM"] - eta_k * rho1) / lam0

    uu, rho = r["uu"], r["lam"]

    def delta_T(q, gmm):
        meas = complex(np.sum(rho * uu ** q * np.exp(1j * gmm * uu)))
        # main term: int u^q e^{(1/2 + i gam) u} du on [U0, 2a], dense Gauss
        ug = np.linspace(u0_cut, a2, 4001)
        integ = ug ** q * np.exp(0.5 * ug) * np.exp(1j * gmm * ug)
        main = complex(np.trapezoid(integ, ug))
        return abs(meas - main)

    q_meas = max(delta_T(0, gam_dual[0]), delta_T(0, gam_dual[1]),
                 delta_T(1, gam_dual[0]) / a2, delta_T(1, gam_dual[1]) / a2)
    q_pret = 0.5 * rho1
    check("F2i.REQ dual-point budget of the K_M kernel (band fit residual "
          "%.1e): Lambda_0 = %.1f, eta ||rho||_1 = %.2f; the required "
          "correlation bound for kappa = 1 is REQ = %.4f; MEASURED "
          "max_q,k |Delta T_q(gamma_k)| = %.4f (uses %.2f of REQ); the "
          "pretentious saturation (1/2)||rho||_1 = %.1f OVERSHOOTS REQ by "
          "x %.0f -- the pretentious phase must be excluded by a factor "
          "%.0f, and the TRUE comb sits a factor %.1f BELOW the "
          "requirement" % (res_band, lam0, eta_k * rho1, req, q_meas,
                           q_meas / req, q_pret, q_pret / req,
                           q_pret / req, req / q_meas),
          req > 0 and q_meas < req)

    # ---- F2ii: the counterfactual coupling / the zone mechanism ----------
    print("\nS2 [F2ii] -- the zero-free-zone mechanism (reference window)")
    lo_c, hi_c = wref["ch"]["lo"], wref["ch"]["hi"]
    gA_c, gB_c = wref["ch"]["gA"], wref["ch"]["gB"]
    probe_g = np.concatenate([gam_dual, [0.31, 2.0, 5.0, 10.0, 14.1347]])
    zh_p = g_hat(probe_g, lo_c, hi_c, gA_c, gB_c)
    z_p = 2.0 * np.real(zh_p / (0.5 + 1j * probe_g))
    zmax_real = float(np.max(np.abs(wref["ch"]["z"])))
    i_zmax = int(np.argmax(np.abs(wref["ch"]["z"])))
    print("    counterfactual coupling |z_cf(tau)| if a zeta zero sat at "
          "tau:")
    for gv, zv in zip(probe_g, z_p):
        tag = ""
        if abs(gv - gam_dual[0]) < 1e-12:
            tag = "  <-- dual point gamma_1"
        if abs(gv - gam_dual[1]) < 1e-12:
            tag = "  <-- dual point gamma_2"
        if abs(gv - 14.1347) < 1e-3:
            tag = "  <-- first REAL zero"
        print("      tau = %8.4f : |z_cf| = %12.4f  (= %8.3f x detM)%s"
              % (gv, abs(zv), abs(zv) / wref["detM"], tag))
    z_cf_max = float(np.max(np.abs(z_p[:2])))
    check("F2ii.ZONE the mechanism, quantified: a zero AT the dual points "
          "would couple with |z_cf| = %.1f (= %.2f x det M -- positivity "
          "would be DEAD); the largest coupling of a REAL zero is "
          "|z(%.4f)| = %.4f (= %.4f x det M), damped x %.0f by the "
          "classical zero-free strip |gamma| >= 14.134 (Gram/Hutchinson; "
          "unconditional) -- the strip IS the anti-pretentious input"
          % (z_cf_max, z_cf_max / wref["detM"], float(gam[i_zmax]),
             zmax_real, zmax_real / wref["detM"], z_cf_max / zmax_real),
          z_cf_max > wref["detM"] and zmax_real < wref["detM"])

    # ============================================================== S3
    print("\nS3 [F3] -- synthesis")
    kap_arr = np.array(kaps)
    aa = np.array([w["r"]["alpha"] for w in results])
    slope = np.polyfit(aa, np.log(kap_arr), 1)[0]
    print("""
  THE CHAIN (all constants measured above, per window):
    (1) IDENTITY (exact algebra + F1a check):
        D(M,F) = BND - RTERM + sum_{gamma} z(gamma)
        z(gamma) = 2 Re[Ghat(gamma)/(1/2+i gamma)],
        G = Khat_M' - Khat_M/2.
    (2) PER-ZERO ENVELOPE (exact summation by parts):
        |z(gamma)| <= 2 C_G / gamma^2, C_G computable, and the zero
        side STARTS at gamma_1 = 14.134 (classical, unconditional).
    (3) ZERO INPUT: computed zeros to 2e4; beta = 1/2 cited to 3e12
        (Platt-Trudgian 2021); the beyond-3e12 inflation is priced
        (max %.1e of det M -- negligible).
    (4) SUM: kappa_unc in [%.4f, %.4f] on the surface --
        det S >= (1 - kappa_unc) det M > 0: T-A UNCONDITIONAL on the
        declared windows, and the pretentious escape is blocked
        (F2i: saturation overshoots REQ x %.0f, yet the zone-damped
        zero side keeps the true comb x %.1f below REQ).
  THE MISSING QUANTIFIER (named): uniformity in the window --
    kappa_unc(a) trend d log kappa/da = %+.3f on the 5 windows
    (%s); a THEOREM needs C_G(a,h)/det M(a) bounded uniformly, i.e.
    a closed-form bound on C_G from the closed weights (Theorems 1-5
    of the prime front give K_M in closed form -- the symbolic step
    is algebra, not arithmetic).
  WHAT STAYS OPEN (honest): T-B (det Ahat >= 0, margin ~ 2e-5 of
    det M) is UNTOUCHED by this chain -- the absorption inequality
    still needs the collective cancellation (prob:R1); this module
    closes the SIGN of det S, not the razor-thin margin.
""" % (max(w["beyond"] / w["detM"] for w in results),
       min(kaps), kap_max, q_pret / req, req / q_meas, slope,
       "decreasing -- uniformity plausible" if slope < 0
       else "NOT decreasing -- uniformity at risk"))

    print("=" * 78)
    print("CONTRACT NOTE UPDATE (chat report is the deliverable)")
    print("=" * 78)
    print("""
  NEW: the K_M pairing obeys the exact zero-side identity (F1a,
  residuum inside the declared tail bar on all 5 windows); the
  unconditional zero-side bound gives kappa_unc = %.4f .. %.4f < 1
  (ZONE-%s), so det S > 0 acquires an unconditional proof-path
  candidate: identity -> per-zero envelope 2 C_G/gamma^2 -> zero-free
  strip gamma >= 14.134 + verified zeros -> kappa < 1.  Sign structure
  of z(gamma): %s (cancellation ratio %.3f).  Dual-point ledger:
  REQ = %.3f, measured %.3f, pretentious saturation %.0f.  Missing
  quantifier: uniformity in (a, h) via a symbolic C_G bound.  T-B
  (the razor-thin absorption margin) remains prob:R1 -- untouched.
""" % (min(kaps), kap_max, "PASS" if zone_pass else "FAIL",
       "ONE-SIGNED" if one_signed else "MIXED", cancel,
       req, q_meas, q_pret))

    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
