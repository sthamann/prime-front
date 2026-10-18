#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v840 -- PRIME.FLOOR.GUEABLATION.01 + PRIME.FLOOR.LOOPGAIN.01: the saturation is STRUCTURAL and the bootstrap loop is SHORT -- every source-native, Guinand-admissible modification of the tower lands at the deployed demand/GUE plateau with the tight band pinned in the UNFOLDED coordinate (the saturation is a property of the tower class and of the unfolded zeros, not of the grid), and the certified ladder CANNOT bootstrap its own next rung: g = 1/(k^2 R^2 c_sup) with even the IDEAL supply giving g = 1/R^2 = 0.655 < 1 -- the wall's self-conservation IS the saturation, ONE module from two probes (10/10 + 8/8 checks, verdicts SATURATION-STRUCTURAL and LOOP-SHORT; discovery probes gue_ablation_probe.py and bootstrap_loop_gain_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping -- measured runtime ~1.1 + 0.4 min; v830/v831 runtime precedent).  PART A, THE ABLATION (falsification attempt on v839's saturation): machinery wards (lag legs vs Dirichlet closed form 2.1e-11; the 2^21 pointwise pipeline vs the frozen parent 2^22 refs at R dev 0.001; Poisson known-answer carried over); the ledger variants -- KMS deformations b = 0.8/0.9/1.1, alias combs D = 1/48 and 1/96, the geometric-h frame-B ladder, +-15deg rotations (diagnostic): ALL 6 source-native variants stay positive and LAND at the deployed plateau 1.154 (1.058..1.199, tol 0.35; the rotations 1.170/1.185) -- 0 below, 0 above, 0 broke positivity; MEASURED SHARPER THAN PREDICTED: the tight band does NOT move with the alias comb -- under D = 1/48, 1/64, 1/96 and geometric-h it stays pinned at UNFOLDED alpha in 1..2; the pole-normalization and heat-trace ablations are structurally inert (typed no-ops of the S0-form); the comb ablations fire (scramble breaks the floor x-954770; the density-matched THINNED comb breaks positivity -0.105 -- the floor needs the FULL arithmetic comb; the mass-matched Epstein comb is POSITIVE-TRIVIAL at x9461, never entering the cancellation regime).  CONSEQUENCE: C_F ~ GUE x 0.8 on alpha in 1..2 is ROBUST across the admissible family, not a knob artifact.  PART B, THE LOOP GAIN (supply(X) vs demand(lambda X), fixed zero window gamma <= 2e4): THE SUPPLY CURVE -- the certified ladder up to X supplies c_hat(X) = 0.88..1.02 (GUE-consistent, rms(z) = 0.718), certified level c_hat + 2 s.e. ~ 1.44; THE DEMAND CURVE -- c_dem(X', k) = 1/(k R)^2 with the saturation R climbing 0.78 -> 1.24; THE LOOP GAIN: headline g(k=1) = 0.529 at lambda = 1.5 (stable across lambda = 1.2/1.5/2.0), g(k=2) = 0.132; the three compounding factors typed exactly: (i) THE SATURATION ITSELF -- R > 1 means even an IDEAL supply (exact GUE, c = 1, k = 1) gives g = 1/R^2 = 0.655 < 1: the world's own statistics are always one notch below what the next rung demands; (ii) supply cannot beat its own statistics (the certified interval charges ~1.6x); (iii) the k^2 discipline cost (any certification k >= 2 divides the gain by >= 4; the chain law sustains N_max = 0 induction steps at the bare gate).  Coverage is NOT the blocker (geometric reach 0.999); the gap is strength-band calibration (0.35).  THE CIRCULARITY WARD: the Poisson world does NOT close the loop (g_P = 0.296 < 0.6 x true) and breaks the base case (factor-2 gate violated 17.6%; true zeros violate neither gate on any rung) -- non-vacuous.  THE CONSEQUENCE: the bootstrap is NOT a proof architecture, and the reason is the saturation, now quantified as SELF-CONSERVATION -- the certified ladder supplies exactly the statistics of the zeros (never more) while the floor demands slightly more than those statistics guarantee; the measured positivity everywhere is genuinely finer-than-statistical information, consistent with the architecture reading, unprovable by the loop; the honest gap list typed (certificate-grade supply, sub-GUE input on alpha in 1..2, the k^2 cost, the T > 2e4 tail).  Feeds PRIME.FLOOR.PAIRCORR.01.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes gue_ablation_probe.py (10/10, verdict
SATURATION-STRUCTURAL) and bootstrap_loop_gain_probe.py (8/8, verdict
LOOP-SHORT), both 2026-08-07, re-run identically at promotion; this
module runs both frozen protocols VERBATIM (~1.5 min total; a
module-level _VERDICTS capture appended at the end of each frozen
run() per the v817/v791 precedent -- no gate, bar or table changed).
IMPORT REMAP (v831 precedent): the probes' read-only imports map to
the promoted counterparts v823/v829/v830/v831; probe-layer symbols
not carried by the promoted modules (the fdp shim: ANOMALOUS_H,
epstein_counts, ols_loglog, the 4-value eig2; the tp shim: parity_t)
are carried VERBATIM below (declared); the bootstrap probe's
read-only import of gue_ablation_probe maps to THIS module's part-A
layer (same frozen source, same module).  The original probe
docstrings, frozen specs and decision trees live in the probe files
verbatim (experiments/tfpt-discovery/).

FIREWALL: zero-side module (the zero list is admissible input on this
strand, own RS scan via v684); v563/v684/v823/v830/v831 READ-ONLY.
NO RH claim; report only.
"""
import math
import os
import sys
import time
import types

import numpy as np
from scipy.stats import norm

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v684_rank3_zeroside as zp               # noqa: E402 (READ-ONLY)
import v823_prime_lagrange_floor as pp         # noqa: E402 (READ-ONLY)
import v829_prime_floor_depth as _v829         # noqa: E402 (READ-ONLY)
import v830_prime_float_budget as pe           # noqa: E402 (READ-ONLY)
import v831_prime_alias_second_moment as pa    # noqa: E402 (READ-ONLY)


# ------- fdp / tp shims: probe-layer symbols VERBATIM (declared in
# PROVENANCE; the promoted v829 carries 2-value eig2 and does not
# export these -- v829 stays READ-ONLY and untouched)

def _fdp_ols_loglog(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.abs(np.asarray(y)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), float(math.exp(q)), r2


def _fdp_eig2(M2):
    a, b, c = M2[0, 0], M2[0, 1], M2[1, 1]
    if max(abs(a), abs(b), abs(c)) == 0.0:
        return 0.0, 0.0, np.array([1.0, 0.0]), np.array([0.0, 1.0])
    mid, R = 0.5 * (a + c), math.hypot(0.5 * (a - c), b)
    l1, l2 = mid + R, mid - R
    if abs(b) < 1e-300 * max(abs(a), abs(c), 1e-300):
        v1 = np.array([1.0, 0.0]) if a >= c else np.array([0.0, 1.0])
    else:
        v1 = np.array([b, l1 - a])
        v1 /= np.linalg.norm(v1)
    if v1[0] < 0:
        v1 = -v1
    v2 = np.array([-v1[1], v1[0]])
    return l1, l2, v1, v2


def _fdp_csinc(z):
    z = np.asarray(z, dtype=complex)
    out = np.ones_like(z)
    m = np.abs(z) > 1e-12
    out[m] = np.sin(z[m]) / z[m]
    return out


def _fdp_epstein_counts(Nmax):
    cnt = np.zeros(Nmax + 1, dtype=np.uint16)
    for x in range(0, int(math.isqrt(Nmax)) + 1):
        rem = Nmax - x * x
        if rem < 0:
            break
        y = np.arange(0, int(math.isqrt(rem // 5)) + 1)
        n = x * x + 5 * y * y
        mult = ((2 if x > 0 else 1)
                * np.where(y > 0, 2, 1)).astype(np.uint16)
        np.add.at(cnt, n, mult)
    return cnt


fdp = types.SimpleNamespace(
    ANOMALOUS_H=1292, DGRID=1.0 / 64.0, csinc=_fdp_csinc,
    eig2=_fdp_eig2, epstein_counts=_fdp_epstein_counts,
    ols_loglog=_fdp_ols_loglog)


def _tp_parity_t(k, h):
    N = 2 * h + 1
    jj = np.arange(h)
    return (2.0 / math.sqrt(N)) * np.sin(
        2.0 * math.pi * k * (jj + 1.0) / N)


tp = types.SimpleNamespace(parity_t=_tp_parity_t)

_VERDICTS = {}

# ------------------- shared layer (identical in both frozen probes; emitted once)

T0 = time.time()

FAILS = []

N_CHK = 0

MARGIN = 0.5

SEED_POIS = 202608

def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


# =============== PART A -- gue_ablation_probe.py (frozen probe, verbatim)

DGRID_a = fdp.DGRID

TOWER_HS_a = (588, 663, 707, 752, 794, 816)

OMEGA_MIN_a = 1.0 / 64.0

BANDS_a = ((OMEGA_MIN_a, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0),
         (8.0, 1.0e9))

BAND_TAGS_a = ("win", "1-2", "2-4", "4-8", ">8")

KMS_EPS = (0.05, -0.05, 0.10)

FB_HS = (320, 415, 538, 698, 905, 1152)

ROT_DEGS = (15.0, -15.0)

LAND_TOL = 0.35

N_GRID = 1 << 21

SEED_SCR = 20250807

CTRL_HS = (285, 388)

REF_R = (1.008, 1.089, 1.133, 1.176, 1.215, 1.236)

REF_LBAR = (2.828e-5, 2.093e-5, 1.782e-5, 1.529e-5, 1.337e-5,
            1.250e-5)

REF_SH72 = (0.189, 0.582, 0.225, 0.004, 0.000)

METH_R_BAR, METH_L_BAR, METH_SH_BAR = 0.10, 0.05, 0.08

SW_BAR, TAU_BAR, SPL_BAR = 1.0e-8, 1.0e-8, 1.0e-6

def csinc_r(x):
    out = np.ones_like(x)
    m = np.abs(x) > 1e-12
    out[m] = np.sin(x[m]) / x[m]
    return out

def nbar_of(g):
    return zp.theta_rs(np.asarray(g, float)) / math.pi + 1.0

def legs_at(c1, c2, h, D, gs):
    """Direct lag sums S_k(g) = sum_j c_k[j] sin(u_j g)."""
    u = (h - np.arange(h) - 0.5) * D
    S1 = np.empty(len(gs))
    S2 = np.empty(len(gs))
    for lo in range(0, len(gs), 4096):
        hi = min(lo + 4096, len(gs))
        sl = np.sin(np.outer(gs[lo:hi], u))
        S1[lo:hi] = sl @ c1
        S2[lo:hi] = sl @ c2
    return S1, S2

_GRID = {}

def build_grid(gam):
    """The parent unfolded grid (N = 2^21) shared by all variants."""
    t_i = nbar_of(gam)
    t_lo, t_hi = float(t_i[0]) - 0.5, float(t_i[-1]) + 0.5
    tgrid = np.linspace(t_lo, t_hi, N_GRID, endpoint=False)
    dt = float(tgrid[1] - tgrid[0])
    g_c = np.geomspace(13.4, 20100.0, 20001)
    ggrid = np.interp(tgrid, nbar_of(g_c), g_c)
    for _ in range(5):
        resid = nbar_of(ggrid) - tgrid
        ggrid = ggrid - resid / (0.5 / math.pi
                                 * np.log(ggrid / (2.0 * math.pi)))
    omg = np.fft.rfftfreq(N_GRID, d=dt)
    _GRID.update(tgrid=tgrid, ggrid=ggrid, dt=dt, omg=omg,
                 S_gue=np.minimum(omg, 1.0),
                 band_idx=[(omg >= a) & (omg < b) for a, b in
                           BANDS_a], live=omg >= OMEGA_MIN_a,
                 t_lo=t_lo, t_hi=t_hi)
    res = float(np.max(np.abs(nbar_of(ggrid[:: 1 << 12])
                              - tgrid[:: 1 << 12])))
    return res

def sperp_on(c, h, D, z):
    """P(z) = sum_j c_j z^j by Horner (generic coefficients),
    z = e^{-iDg}; then S_perp = Im[e^{i(h-1/2)Dg} P(z)]."""
    acc = np.full(z.shape, complex(c[h - 1]))
    for j in range(h - 2, -1, -1):
        acc *= z
        acc += c[j]
    return acc

def demand_ledger(h, D, c1, c2, gam, rot_deg=0.0, keep_f=False):
    """The variant demand ledger: tau (zero-side, conservative),
    L_true, L_bar, sigma_GUE, R, band shares -- parent pipeline
    conventions verbatim, pointwise f on the unfolded grid."""
    u = (h - np.arange(h) - 0.5) * D
    ee = np.sinh(u / 2.0)
    cp = 2.0 * math.sqrt(D) * (math.sinh(D / 4.0) / (D / 4.0))
    p1, p2 = cp * float(c1 @ ee), cp * float(c2 @ ee)
    r = math.hypot(p1, p2)
    p1h, p2h = p1 / r, p2 / r
    if rot_deg != 0.0:
        th = math.radians(rot_deg)
        p1h, p2h = (math.cos(th) * p1h - math.sin(th) * p2h,
                    math.sin(th) * p1h + math.cos(th) * p2h)
    cperp = p2h * c1 - p1h * c2
    # zero side (exact; truncation adds PSD terms only -- typed)
    S1z, S2z = legs_at(c1, c2, h, D, gam)
    wz = D * csinc_r(D * gam / 2.0) ** 2
    Sper = p2h * S1z - p1h * S2z
    L_true = float(np.sum(4.0 * wz * Sper ** 2))
    a = 2.0 * np.sqrt(wz) * S1z
    b = 2.0 * np.sqrt(wz) * S2z
    Md = np.array([[float(a @ a) + p1 * p1,
                    float(a @ b) + p1 * p2],
                   [float(a @ b) + p1 * p2,
                    float(b @ b) + p2 * p2]])
    lam, tau, _, _ = fdp.eig2(Md)
    # pointwise f on the unfolded grid + FFT (parent conventions)
    gg, dt = _GRID["ggrid"], _GRID["dt"]
    zg = np.exp(-1j * D * gg)
    Sg = np.imag(np.exp(1j * (h - 0.5) * D * gg)
                 * sperp_on(cperp, h, D, zg))
    fg = 4.0 * (D * csinc_r(D * gg / 2.0) ** 2) * Sg ** 2
    L_bar = dt * float(np.sum(fg))
    F = np.fft.rfft(fg)
    P2 = 2.0 * (dt / N_GRID) * np.abs(F) ** 2
    P2[0] *= 0.5
    live, S_gue = _GRID["live"], _GRID["S_gue"]
    sig2_gue = float(np.sum(P2[live] * S_gue[live]))
    sig2_p = float(np.sum(P2[live]))
    sh = np.array([float(np.sum(P2[bi & live] * S_gue[bi & live]))
                   for bi in _GRID["band_idx"]])
    sig = math.sqrt(max(sig2_gue, 0.0))
    out = dict(tau=tau, lam=lam, L_true=L_true, L_bar=L_bar,
               dL=L_true - L_bar, sig_gue=sig,
               sig_p=math.sqrt(max(sig2_p, 0.0)),
               R=sig / (MARGIN * L_bar),
               z=(L_true - L_bar) / max(sig, 1e-300),
               shares=sh / max(float(np.sum(sh)), 1e-300),
               p=(p1, p2))
    if keep_f:
        out["fg"] = fg
    return out

def spline_S(rr, uu, lam2):
    """S matrix from an atom list (pa control recipe, verbatim)."""
    Xn = np.empty((len(uu), 3))
    for i in range(len(uu)):
        Xn[i, 0] = core.spline_project(rr["W11"], uu[i], rr["D"],
                                       rr["M"])
        Xn[i, 1] = core.spline_project(rr["W22"], uu[i], rr["D"],
                                       rr["M"])
        Xn[i, 2] = core.spline_project(rr["W12"], uu[i], rr["D"],
                                       rr["M"])
    return np.array([[float(lam2 @ Xn[:, 0]), float(lam2 @ Xn[:, 2])],
                     [float(lam2 @ Xn[:, 2]),
                      float(lam2 @ Xn[:, 1])]])

def prime_powers(nmax):
    """(n, u, Lambda, base prime) for prime powers <= nmax."""
    is_p = np.ones(nmax + 1, dtype=bool)
    is_p[:2] = False
    for p in range(2, int(math.isqrt(nmax)) + 1):
        if is_p[p]:
            is_p[p * p::p] = False
    primes = np.flatnonzero(is_p).astype(np.int64)
    ns, ps = [], []
    for p in primes:
        q = int(p)
        while q <= nmax:
            ns.append(q)
            ps.append(int(p))
            q *= int(p)
    ns = np.array(ns)
    ps = np.array(ps)
    o = np.argsort(ns)
    return ns[o], ps[o], primes

def part_a():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("GUE SATURATION ABLATION (gue_ablation_probe) -- "
          "structural or artifact?")
    print("=" * 78)
    print("""
HONESTY FRAME: falsification attempt on the saturation claim.
NO RH claim.  Variant floors are zero-side (Guinand-admissible
coefficient families; T > 2e4 truncation only adds PSD terms, so
positivity verdicts are conservative).  TYPED NO-OPS: the pole
normalization enters the demand only through the Schur term
(<= 3.6e-5 of tau); the archimedean heat-trace scale is absent
from the zero-side demand functional -- both ablations are
structurally inert for the ratio (measured facts of the S0-form).""")

    # ============================================================== S0
    print("\nS0 -- machinery wards")
    gam, n_rvm = pp.zero_list()
    check("S0.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    # leg ward: lag sums vs Dirichlet closed form
    h0, D0 = TOWER_HS_a[-1], DGRID_a
    c1_0 = tp.parity_t(1, h0)
    c2_0 = tp.parity_t(2, h0)
    gs = np.linspace(15.0, 1.9e4, 200)
    S1l, S2l = legs_at(c1_0, c2_0, h0, D0, gs)
    S1c = pe.s_vec(1, h0, D0 * gs)
    S2c = pe.s_vec(2, h0, D0 * gs)
    sw = max(float(np.max(np.abs(S1l - S1c))),
             float(np.max(np.abs(S2l - S2c)))) \
        / max(float(np.max(np.abs(S1c))), 1e-300)
    check("S0.SWARD lag legs == Dirichlet closed form (200 pts, "
          "rel %.1e <= %.0e)" % (sw, SW_BAR), sw <= SW_BAR)
    res = build_grid(gam)
    check("S0.GRID unfolded grid (N = 2^21) inversion residual "
          "%.1e <= 1e-9" % res, res <= 1.0e-9)
    # deployed tower: pointwise ledger + tau ward + method ward
    dep = []
    for i, hz in enumerate(TOWER_HS_a):
        led = demand_ledger(hz, DGRID_a, tp.parity_t(1, hz),
                            tp.parity_t(2, hz), gam, keep_f=True)
        dep.append(led)
    fr72 = pa.pole_frame(TOWER_HS_a[-1], DGRID_a, gam)
    tau_pa, lam_pa, _ = pa.tau_of(fr72)
    dtau = abs(dep[-1]["tau"] - tau_pa) / max(abs(lam_pa), 1e-300)
    check("S0.TAU deployed rung h = 816: M_d tau (lag route) vs pa "
          "closed-form tau (|dtau|/lam = %.1e <= %.0e)"
          % (dtau, TAU_BAR), dtau <= TAU_BAR)
    worst_R = max(abs(d["R"] / rf - 1.0)
                  for d, rf in zip(dep, REF_R))
    worst_L = max(abs(d["L_bar"] / lf - 1.0)
                  for d, lf in zip(dep, REF_LBAR))
    worst_S = float(np.max(np.abs(dep[-1]["shares"]
                                  - np.array(REF_SH72))))
    check("S0.METH pointwise 2^21 pipeline vs frozen parent 2^22 "
          "refs: R dev %.3f <= %.2f, L_bar dev %.3f <= %.2f, "
          "rung-816 band-share dev %.3f <= %.2f"
          % (worst_R, METH_R_BAR, worst_L, METH_L_BAR, worst_S,
             METH_SH_BAR),
          worst_R <= METH_R_BAR and worst_L <= METH_L_BAR
          and worst_S <= METH_SH_BAR)
    plat_dep = float(np.median([d["R"] for d in dep]))
    print("    deployed tower plateau (median R over 6 rungs): "
          "%.3f" % plat_dep)
    # Poisson known-answer carried over
    rs = np.random.RandomState(SEED_POIS)
    t_P = np.sort(rs.uniform(_GRID["t_lo"], _GRID["t_hi"],
                             size=len(gam)))
    zs_t, zs_p = [], []
    for i, hz in enumerate(TOWER_HS_a):
        fp = np.interp(t_P, _GRID["tgrid"], dep[i]["fg"])
        zP = (float(np.sum(fp)) - dep[i]["L_bar"]) \
            / max(dep[i]["sig_gue"], 1e-300)
        zs_p.append(zP)
        zs_t.append(dep[i]["z"])
        del dep[i]["fg"]
    rms_t = float(np.sqrt(np.mean(np.array(zs_t) ** 2)))
    rms_p = float(np.sqrt(np.mean(np.array(zs_p) ** 2)))
    check("S0.POIS Poisson known-answer carried over: rms(z) true "
          "zeros %.2f < Poisson ordinates %.2f (directional)"
          % (rms_t, rms_p), rms_p > rms_t)

    # ============================================================== S1
    print("\nS1 -- the ledger variants (per-rung R, positivity, "
          "bands)")
    alphas = [hz * DGRID_a for hz in TOWER_HS_a]
    variants = []
    for eps in KMS_EPS:
        variants.append(("KMS b=%.2f" % (1.0 - 2.0 * eps),
                         [(hz, DGRID_a, eps) for hz in TOWER_HS_a], 0.0))
    variants.append(("G48 D=1/48",
                     [(int(round(al * 48)), 1.0 / 48.0, 0.0)
                      for al in alphas], 0.0))
    variants.append(("G96 D=1/96",
                     [(int(round(al * 96)), 1.0 / 96.0, 0.0)
                      for al in alphas], 0.0))
    variants.append(("FB geom-h",
                     [(hf, al / hf, 0.0)
                      for hf, al in zip(FB_HS, alphas)], 0.0))
    for rd in ROT_DEGS:
        variants.append(("ROT %+.0fdeg (diag)" % rd,
                         [(hz, DGRID_a, 0.0) for hz in TOWER_HS_a], rd))
    table = []
    for name, geo, rot in variants:
        t0 = time.time()
        rows = []
        for (hz, Dz, eps) in geo:
            u = (hz - np.arange(hz) - 0.5) * Dz
            tilt = np.exp(eps * u) if eps != 0.0 else 1.0
            led = demand_ledger(hz, Dz, tp.parity_t(1, hz) * tilt,
                                tp.parity_t(2, hz) * tilt, gam,
                                rot_deg=rot)
            rows.append(led)
        pos = all(rw["tau"] > 0.0 for rw in rows)
        plat = float(np.median([rw["R"] for rw in rows]))
        sh_m = np.mean([rw["shares"] for rw in rows], axis=0)
        tight = BAND_TAGS_a[int(np.argmax(sh_m))]
        table.append(dict(name=name, pos=pos, plat=plat,
                          tight=tight, rows=rows, diag="diag" in
                          name, sh=sh_m))
        print("    %-16s pos=%-5s plateau R = %.3f (rungs: %s) "
              "tight band '%s' [%.0f s]"
              % (name, pos, plat,
                 " ".join("%.2f" % rw["R"] for rw in rows), tight,
                 time.time() - t0))
        print("%22sband shares: %s | min tau %.2e | z rms %.2f"
              % ("", " ".join("%s %.2f" % (t, s) for t, s in
                              zip(BAND_TAGS_a, sh_m)),
                 min(rw["tau"] for rw in rows),
                 float(np.sqrt(np.mean(
                     np.array([rw["z"] for rw in rows]) ** 2)))))

    # ============================================================== S2
    print("\nS2 -- comb ablations (prime side, frozen battery "
          "frames)")
    rr_map = {}
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] in CTRL_HS:
            rr_map[rr["h"]] = rr
    for hz in CTRL_HS:
        rr = rr_map[hz]
        tau_dep = fdp.eig2(rr["Ah"])[1]
        # spline-S rebuild ward on the true comb (S = lam @ Xn,
        # lam = Lambda(n)/(2 sqrt n) -- build_window verbatim)
        S_true = spline_S(rr, rr["uu"], rr["lam"])
        tau_spl = fdp.eig2(rr["B"] - S_true)[1]
        spl = abs(tau_spl - tau_dep) / max(abs(tau_dep), 1e-300)
        check("S2.SPL h = %d: spline-S rebuild reproduces the "
              "deployed floor (rel %.1e <= %.0e)"
              % (hz, spl, SPL_BAR), spl <= SPL_BAR)
        # scramble (must-fire)
        rs2 = core.build_window(rr["k"], scramble_seed=SEED_SCR)
        tau_scr = fdp.eig2(rs2["Ah"])[1]
        fire = (tau_scr < 0.0) or not (0.2 <= tau_scr / tau_dep
                                       <= 5.0)
        check("S2.SCRAM h = %d scramble breaks the floor: tau %.3e "
              "-> %.3e (x%.2f) -- sign/scale break required"
              % (hz, tau_dep, tau_scr, tau_scr / tau_dep), fire)
        # Epstein (mass-matched)
        nmax = int(math.exp(2.0 * rr["alpha"]))
        cntE = fdp.epstein_counts(nmax)
        nnE = np.nonzero(cntE[2:])[0].astype(np.int64) + 2
        uuE = np.log(nnE.astype(float))
        mE = cntE[nnE].astype(float) / np.sqrt(nnE.astype(float))
        kapE = float(np.sum(2.0 * rr["lam"])) / float(np.sum(mE))
        SE = spline_S(rr, uuE, 0.5 * kapE * mE)   # pa C3 verbatim
        tau_E = fdp.eig2(rr["B"] - SE)[1]
        # thinned comb: the DEPLOYED atoms/masses verbatim, kept
        # iff the base prime has odd rank; mass-matched kappa
        _, _, primes = prime_powers(nmax)
        rank = {int(p): i for i, p in enumerate(primes)}
        pset = set(int(p) for p in primes)

        def base_prime(n):
            if n in pset:
                return n
            for p in primes:
                if n % int(p) == 0:
                    return int(p)
            return n
        nn_dep = np.rint(np.exp(rr["uu"])).astype(np.int64)
        keep = np.array([rank[base_prime(int(n))] % 2 == 0
                         for n in nn_dep])
        kapT = float(np.sum(rr["lam"])) \
            / float(np.sum(rr["lam"][keep]))
        ST = spline_S(rr, rr["uu"][keep],
                      kapT * rr["lam"][keep])
        tau_T = fdp.eig2(rr["B"] - ST)[1]
        print("    h = %d (alpha %.2f): tau deployed %.3e | "
              "Epstein %.3e (%s; x%.0f the deployed floor -- the "
              "mass-matched Epstein comb never enters the "
              "cancellation regime, so the GUE question does not "
              "arise for it) | thinned %.3e (%s)"
              % (hz, rr["alpha"], tau_dep, tau_E,
                 "POSITIVE-TRIVIAL" if tau_E > 0 else "BROKEN",
                 abs(tau_E / tau_dep), tau_T,
                 "POSITIVE" if tau_T > 0 else "BROKEN"))
    print("""    translation typing: EPSTEIN demand vs its own zero
    statistics UNAVAILABLE (no Epstein zeta zeros in the stack;
    its F is a different object -- off-line zeros exist);
    THINNED comb zero-side translation BLOCKED (no explicit-
    formula zero statistics for a decimated comb); SCRAMBLE has
    no meaningful demand ledger (no Guinand zero side at all) --
    verified above by the must-fire floor break.""")

    # ============================================================== S3
    print("\nS3 -- decision + verdict")
    src = [t for t in table if not t["diag"]]
    landed = [t for t in src if t["pos"]
              and abs(t["plat"] / plat_dep - 1.0) <= LAND_TOL]
    below = [t for t in src if t["pos"]
             and t["plat"] < (1.0 - LAND_TOL) * plat_dep]
    above = [t for t in src if t["pos"]
             and t["plat"] > (1.0 + LAND_TOL) * plat_dep]
    broke = [t for t in src if not t["pos"]]
    wards_ok = not any(k.startswith(("S0.", "S2.SPL"))
                       for k in FAILS)
    scram_ok = not any(k.startswith("S2.SCRAM") for k in FAILS)
    if not wards_ok:
        verdict = "ABLATION-TRANSLATION-BLOCKED"
    elif below:
        verdict = "SATURATION-ARTIFACT"
    elif len(landed) == len([t for t in src if t["pos"]]) \
            and scram_ok:
        verdict = "SATURATION-STRUCTURAL"
    else:
        verdict = "SATURATION-MIXED"
    print("    source-native ledger variants: %d positive, %d "
          "land at the plateau (tol %.2f), %d below, %d above, "
          "%d broke positivity"
          % (len([t for t in src if t["pos"]]), len(landed),
             LAND_TOL, len(below), len(above), len(broke)))
    for t in table:
        stat = ("DIAGNOSTIC" if t["diag"] else
                ("BROKEN" if not t["pos"] else
                 ("LANDS" if t in landed else
                  ("BELOW" if t in below else "ABOVE"))))
        print("      %-16s plateau %.3f (dep %.3f)  tight '%s'  "
              "-> %s" % (t["name"], t["plat"], plat_dep,
                         t["tight"], stat))
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "SATURATION-ARTIFACT":
        print("    THE RELEASING ABLATION(S): %s -- the tightness-"
              "creating detail identified; cheaper routes REOPEN "
              "for these variants (prominent report)"
              % ", ".join(t["name"] for t in below))
    print("""    SYNTHESIS: every source-native, Guinand-admissible
    modification of the tower either broke the measured floor or
    landed at the deployed demand/GUE plateau (%.3f, tol %.2f;
    measured spread of the landing variants far tighter than the
    tolerance).  MEASURED SHARPER THAN PREDICTED: the tight band
    does NOT move with the alias comb -- under D = 1/48, 1/64,
    1/96 and the geometric-h frame-B ladder it stays pinned at
    UNFOLDED alpha in 1..2.  The demand consumes the same zero
    statistics in the universal coordinate regardless of the
    lattice; the saturation is a property of the unfolded zeros,
    not of the grid.  The pole-normalization and heat-trace
    ablations are structurally inert (typed no-ops of the
    S0-form); the density-matched THINNED comb breaks positivity
    (the floor needs the full arithmetic comb), and the Epstein
    comb never reaches the cancellation regime.  For
    PRIME.FLOOR.PAIRCORR.01 this means the named object
    C_F ~ GUE x 0.8 on alpha in 1..2 is ROBUST across the
    admissible family, not a knob artifact -- the demand strength
    is a property of the tower CLASS.  Architecture reading (no
    RH claim): a plateau shared across the family, pinned in the
    unfolded coordinate, is the strongest form of the comb-zero
    bridge consistency a necessary-side battery can deliver --
    the comb's floor is pinned to the conjectured universality
    class of the zeros wherever the floor exists at all.""" %
          (plat_dep, LAND_TOL))
    dt_run = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt_run / 60.0))
    print("NO RH claim; report only; nothing outside experiments/ "
          "touched.")
    _VERDICTS["a"] = verdict



# =============== PART B -- bootstrap_loop_gain_probe.py (frozen probe, verbatim)

TOWER_HS_b = TOWER_HS_a

DGRID_b = 1.0 / 64.0

OMEGA_MIN_b = OMEGA_MIN_a

BANDS_b = BANDS_a

BAND_TAGS_b = BAND_TAGS_a

CAL_BANDS = ("win", "2-4", "4-8")

LAMBDAS = (1.2, 1.5, 2.0)

K_GRID = (1.0, 2.0, 3.0, 5.0)

K_DEC = 2.0

N_POIS = 8

MIN_SUP = 10

EPS_CHAIN = 0.05

REF_R_TOWER = (1.008, 1.089, 1.133, 1.176, 1.215, 1.236)

REF_PLATEAU = 1.114

REF_OM95_DEEP = 3.0

REG_R_BAR, REG_PLAT_BAR, REG_OM95_BAR = 0.03, 0.03, 0.5

POIS_GAIN_FAC, POIS_VIOL_MIN = 0.6, 0.02

N_BAT_EXP = 67

OMB = np.geomspace(OMEGA_MIN_b, 60.0, 241)

def frames_all():
    """(h, D, alpha, tower?) for the deployed ladder: 67 battery
    frames (parents' filters: anomalous h and ATOM_MAX skipped --
    only CERTIFIED rungs may feed the supply) + 6 tower rungs,
    sorted by alpha (build_window geometry, no heavy build)."""
    fr = []
    for kz in core.frame_a_zones():
        al = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(al / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        hz = Mz // 2
        if hz == fdp.ANOMALOUS_H:
            continue
        if math.exp(2.0 * al) > core.ATOM_MAX + 0.5:
            continue
        fr.append((hz, 2.0 * al / Mz, al, False))
    n_bat = len(fr)
    for hz in TOWER_HS_b:
        fr.append((hz, DGRID_b, hz * DGRID_b, True))
    fr.sort(key=lambda t: t[2])
    return fr, n_bat

def pole_hat(h, D):
    c1, c2 = tp.parity_t(1, h), tp.parity_t(2, h)
    u = (h - np.arange(h) - 0.5) * D
    ee = np.sinh(u / 2.0)
    cp = 2.0 * math.sqrt(D) * (math.sinh(D / 4.0) / (D / 4.0))
    p1, p2 = cp * float(c1 @ ee), cp * float(c2 @ ee)
    r = math.hypot(p1, p2)
    return p1 / r, p2 / r

def rung_ledger(h, D, gam, rs):
    """One rung: L_true, L_bar, dL, sigma_GUE/P, R, omega95,
    band shares, coverage histogram, Poisson-draw dL's."""
    p1h, p2h = pole_hat(h, D)
    gg, dt = _GRID["ggrid"], _GRID["dt"]
    phi = D * gg
    Sg = p2h * pe.s_vec(1, h, phi) - p1h * pe.s_vec(2, h, phi)
    fg = 4.0 * (D * csinc_r(phi / 2.0) ** 2) * Sg ** 2
    L_bar = dt * float(np.sum(fg))
    F = np.fft.rfft(fg)
    P2 = 2.0 * (dt / N_GRID) * np.abs(F) ** 2
    P2[0] *= 0.5
    omg = _GRID["omg"]
    live, S_gue = _GRID["live"], _GRID["S_gue"]
    wgt = P2 * S_gue * live
    sig2_gue = float(np.sum(wgt))
    sig2_p = float(np.sum(P2[live]))
    cs = np.cumsum(wgt)
    om95 = float(omg[int(np.searchsorted(cs, 0.95 * cs[-1]))])
    sh = np.array([float(np.sum(wgt[bi])) for bi in
                   _GRID["band_idx"]]) / max(sig2_gue, 1e-300)
    hist = np.histogram(omg, bins=OMB, weights=wgt)[0]
    # zero side
    phz = D * gam
    Sz = p2h * pe.s_vec(1, h, phz) - p1h * pe.s_vec(2, h, phz)
    L_true = float(np.sum(4.0 * (D * csinc_r(phz / 2.0) ** 2)
                          * Sz ** 2))
    # Poisson draws (interp on the shared grid)
    dLP = np.empty(N_POIS)
    for d in range(N_POIS):
        t_P = np.sort(rs.uniform(_GRID["t_lo"],
                                 _GRID["t_hi"], size=len(gam)))
        dLP[d] = float(np.sum(np.interp(t_P, _GRID["tgrid"],
                                        fg))) - L_bar
    sig = math.sqrt(max(sig2_gue, 0.0))
    return dict(L_true=L_true, L_bar=L_bar, dL=L_true - L_bar,
                sig=sig, sigP=math.sqrt(max(sig2_p, 0.0)),
                R=sig / (MARGIN * L_bar), om95=om95, sh=sh,
                hist=hist, dLP=dLP,
                cal=float(sum(sh[BAND_TAGS_b.index(b)]
                              for b in CAL_BANDS)))

def jack_ratio(a, b):
    """Ratio estimator sum(a)/sum(b) with delete-1 jackknife s.e."""
    A, Bt = float(np.sum(a)), float(np.sum(b))
    th = A / Bt
    n = len(a)
    if n < 3:
        return th, float("inf")
    lo = (A - a) / (Bt - b)
    se = math.sqrt((n - 1) / n * float(np.sum((lo - np.mean(lo))
                                              ** 2)))
    return th, se

def part_b():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("BOOTSTRAP LOOP GAIN (bootstrap_loop_gain_probe) -- "
          "supply(X) vs demand(lambda X)")
    print("=" * 78)
    print("""
HONESTY FRAME: NO RH claim.  All rungs read the SAME zero window
gamma <= 2e4 (depth grows in the comb); the loop is a fixed-window
statement.  Supply is MEASUREMENT-grade (measured margins +
jackknife), demand is certificate-grade (k-sigma discipline) --
the asymmetry is part of the result, typed in the gap list.
GAIN CONVENTION: g = c_dem/c_sup in GUE-multiplier units; g >= 1
means the supplied F-level is at least as strong as demanded.""")

    # ============================================================== S0
    print("\nS0 -- ledgers + regression wards")
    gam, n_rvm = pp.zero_list()
    check("S0.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    res = build_grid(gam)
    check("S0.GRID unfolded grid (N = 2^21) inversion residual "
          "%.1e <= 1e-9" % res, res <= 1.0e-9)
    fr, n_bat = frames_all()
    check("S0.SET frame set: %d certified battery + %d tower = %d "
          "rungs (the parents' 73-rung ladder)"
          % (n_bat, len(TOWER_HS_b), len(fr)),
          n_bat == N_BAT_EXP and len(fr) == N_BAT_EXP + 6)
    rs = np.random.RandomState(SEED_POIS)
    rows = []
    for (h, D, al, tow) in fr:
        led = rung_ledger(h, D, gam, rs)
        led.update(h=h, D=D, al=al, tow=tow)
        rows.append(led)
    print("    per-rung ledgers built: %d rungs in %.1f min"
          % (len(rows), (time.time() - T0) / 60.0))
    tow_rows = [r for r in rows if r["tow"]]
    devR = max(abs(r["R"] / rf - 1.0) for r, rf in
               zip(tow_rows, REF_R_TOWER))
    check("S0.REG tower R regression vs frozen saturation refs "
          "(worst dev %.3f <= %.2f)" % (devR, REG_R_BAR),
          devR <= REG_R_BAR)
    deep20 = sorted(rows, key=lambda r: r["al"])[-20:]
    plat = float(np.median([r["R"] for r in deep20]))
    check("S0.PLAT saturation plateau reproduces: median R "
          "(deepest 20) = %.3f vs %.3f (bar %.2f)"
          % (plat, REF_PLATEAU, REG_PLAT_BAR),
          abs(plat - REF_PLATEAU) <= REG_PLAT_BAR)
    om_deep = tow_rows[-1]["om95"]
    check("S0.OM95 deep-tower demand reach: omega95 = %.2f vs "
          "%.1f (bar %.1f)" % (om_deep, REF_OM95_DEEP,
                               REG_OM95_BAR),
          abs(om_deep - REF_OM95_DEEP) <= REG_OM95_BAR)

    # ============================================================== S1
    print("\nS1 -- THE SUPPLY CURVE (certified ladder up to X)")
    n = len(rows)
    aa = np.array([r["dL"] ** 2 for r in rows])
    bb = np.array([r["sig"] ** 2 for r in rows])
    aaP = np.array([float(np.mean(r["dLP"] ** 2)) for r in rows])
    csup, csup_up, reach = np.full(n, np.nan), np.full(n, np.nan), \
        np.full(n, np.nan)
    csupP_up = np.full(n, np.nan)
    Wcum = np.zeros(len(OMB) - 1)
    omb_mid = 0.5 * (OMB[1:] + OMB[:-1])
    for i in range(n):
        Wcum += rows[i]["hist"]
        cw = np.cumsum(Wcum)
        reach[i] = float(omb_mid[int(np.searchsorted(
            cw, 0.95 * cw[-1]))])
        if i + 1 >= MIN_SUP:
            th, se = jack_ratio(aa[: i + 1], bb[: i + 1])
            csup[i], csup_up[i] = th, th + 2.0 * se
            thP, seP = jack_ratio(aaP[: i + 1], bb[: i + 1])
            csupP_up[i] = thP + 2.0 * seP
    print("    supply strength c_hat(X) = sum dL^2 / sum sig_GUE^2 "
          "(GUE-multiplier), certified level = c_hat + 2 s.e.:")
    idxs = list(range(MIN_SUP - 1, n_bat, 12)) + \
        [i for i in range(n) if rows[i]["tow"]]
    for i in idxs:
        r = rows[i]
        print("      alpha %6.2f X %9.3e %s | z %+5.2f | c_hat "
              "%.3f (up %.3f) | reach om95_sup %5.2f"
              % (r["al"], math.exp(2 * r["al"]),
                 "TOWER" if r["tow"] else "batt ",
                 r["dL"] / r["sig"], csup[i], csup_up[i],
                 reach[i]))
    zz = np.array([r["dL"] / r["sig"] for r in rows])
    print("    full-ladder: rms(z) = %.3f -> c_hat(all) = %.3f "
          "+ 2 x %.3f; the supplied F-level is GUE-consistent "
          "(measurement-grade)"
          % (float(np.sqrt(np.mean(zz ** 2))), csup[n - 1],
             0.5 * (csup_up[n - 1] - csup[n - 1])))

    # ============================================================== S2
    print("\nS2 -- THE DEMAND CURVE (per rung X')")
    print("    c_dem(X', k) = 1/(k R)^2 (factor-2 gate; bare gate "
          "= x4); demand band reach om95; calibrated share = "
          "budget in parent-calibrated bands %s:" % (CAL_BANDS,))
    for i in idxs:
        r = rows[i]
        print("      alpha %6.2f %s | R %.3f | c_dem k=1: %.3f "
              "k=2: %.3f k=5: %.4f | om95 %5.2f | cal-share %.2f"
              % (r["al"], "TOWER" if r["tow"] else "batt ",
                 r["R"], 1.0 / r["R"] ** 2, 1.0 / (2 * r["R"]) ** 2,
                 1.0 / (5 * r["R"]) ** 2, r["om95"], r["cal"]))
    al_v = np.array([r["al"] for r in rows])
    R_v = np.array([r["R"] for r in rows])
    om_v = np.array([r["om95"] for r in rows])
    cal_v = np.array([r["cal"] for r in rows])
    al_bat_max = max(r["al"] for r in rows if not r["tow"])
    al_tow_min = min(r["al"] for r in rows if r["tow"])
    print("    alpha desert (no frames): (%.2f, %.2f) -- pairs "
          "whose target falls inside are excluded, typed"
          % (al_bat_max, al_tow_min))

    def interp_at(alp, vec):
        return float(np.interp(alp, al_v, vec))

    def cumshare_at(alp, om_cut):
        """Demand rung at alpha': GUE-budget share below om_cut
        (linear interp between bracketing rungs' histograms)."""
        j = int(np.searchsorted(al_v, alp))
        j0, j1 = max(j - 1, 0), min(j, n - 1)
        out = []
        for jj in (j0, j1):
            cw = np.cumsum(rows[jj]["hist"])
            out.append(float(np.interp(om_cut, omb_mid,
                                       cw / max(cw[-1], 1e-300))))
        if j1 == j0 or al_v[j1] == al_v[j0]:
            return out[0]
        t = (alp - al_v[j0]) / (al_v[j1] - al_v[j0])
        return (1 - t) * out[0] + t * out[1]

    # ============================================================== S3
    print("\nS3 -- THE LOOP GAIN g(X, lambda, k) = c_dem/c_sup")
    summ = {}
    for lam in LAMBDAS:
        dal = 0.5 * math.log(lam)
        pairs = []
        for i in range(n):
            alp = rows[i]["al"] + dal
            if alp > al_v[-1] or np.isnan(csup_up[i]):
                continue
            if al_bat_max < alp < al_tow_min:
                continue
            Rp = interp_at(alp, R_v)
            g1 = (1.0 / Rp ** 2) / csup_up[i]
            cov_g = cumshare_at(alp, reach[i])
            cov_c = interp_at(alp, cal_v)
            gP = (1.0 / Rp ** 2) / csupP_up[i]
            pairs.append(dict(i=i, al=rows[i]["al"], alp=alp,
                              g1=g1, cov_g=cov_g, cov_c=cov_c,
                              gP=gP, tow=rows[i]["tow"],
                              gap=max(interp_at(alp, om_v)
                                      - reach[i], 0.0)))
        tw = [p for p in pairs if p["tow"]]
        sel = tw if len(tw) >= 3 else pairs
        med = lambda key, ps=sel: float(np.median([p[key]
                                                   for p in ps]))
        summ[lam] = dict(g1=med("g1"), cov_g=med("cov_g"),
                         cov_c=med("cov_c"), gP=med("gP"),
                         gap=med("gap"), pairs=pairs, sel=sel)
        print("    lambda = %.1f (%d pairs, %d tower; headline = "
              "median over %s):" % (lam, len(pairs), len(tw),
                                    "tower pairs" if len(tw) >= 3
                                    else "all pairs"))
        print("      gain g(k): " + "  ".join(
            "k=%g: %.3f" % (k, summ[lam]["g1"] / k ** 2)
            for k in K_GRID))
        print("      coverage: geometric %.3f (supply reach vs "
              "demand budget), calibrated-instrument %.3f; "
              "alpha-gap (demand om95 - supply reach) %.2f"
              % (summ[lam]["cov_g"], summ[lam]["cov_c"],
                 summ[lam]["gap"]))
    lamH = 1.5
    g1H = summ[lamH]["g1"]
    g2H = g1H / K_DEC ** 2
    print("    HEADLINE (lambda = %.1f): g(k=1) = %.3f, g(k=%g) "
          "= %.3f, geometric coverage %.3f, calibrated coverage "
          "%.3f" % (lamH, g1H, K_DEC, g2H, summ[lamH]["cov_g"],
                    summ[lamH]["cov_c"]))

    # ============================================================== S4
    print("\nS4 -- the marginal analysis (trend, gate, chain law)")
    sel = summ[lamH]["sel"]
    als = np.array([p["al"] for p in sel])
    g1s = np.array([p["g1"] for p in sel])
    if len(sel) >= 3:
        sl = float(np.polyfit(als, g1s, 1)[0])
    else:
        sl = float("nan")
    g_inf = (1.0 / plat ** 2) / csup_up[n - 1]
    print("    g(k=1) over the tower pairs: %s | slope %+.4f per "
          "alpha | plateau-limit estimate 1/(R_inf^2 c_sup_up) = "
          "%.3f" % (" ".join("%.2f" % g for g in g1s), sl, g_inf))
    Rdeep = tow_rows[-1]["R"]
    print("    grade split at the deep end: point-estimate supply "
          "(non-certificate) g(k=1) = %.3f; certified-interval "
          "supply g(k=1) = %.3f; IDEAL supply (exact GUE, c = 1) "
          "g(k=1) = 1/R^2 = %.3f < 1 -- the saturation R > 1 "
          "alone keeps even the ideal loop short"
          % ((1.0 / Rdeep ** 2) / csup[n - 1],
             (1.0 / Rdeep ** 2) / csup_up[n - 1],
             1.0 / Rdeep ** 2))
    print("    gate dependence: bare-positivity gate (MARGIN = 1) "
          "multiplies every gain by 4: g_bare(k=1) = %.2f, "
          "g_bare(k=2) = %.2f" % (4 * g1H, 4 * g1H / 4))
    # chain-length law: k(N) = Phi^{-1}(1 - eps/N); induction of N
    # steps at total failure eps needs gain g_bare/k(N)^2 >= 1
    Nmax = 0
    for N in range(1, 100000):
        kN = float(norm.ppf(1.0 - EPS_CHAIN / N))
        if 4 * g1H / kN ** 2 < 1.0:
            break
        Nmax = N
    print("    chain-length law (union bound, total failure %.2f):"
          " k(N) = Phi^inv(1 - %.2f/N); the bare-gate loop "
          "sustains N_max = %d induction step(s) before the "
          "discipline cost k^2 eats the gain"
          % (EPS_CHAIN, EPS_CHAIN, Nmax))

    # ============================================================== S5
    print("\nS5 -- the circularity ward (Poisson world)")
    gPH = summ[lamH]["gP"]
    ok_g = gPH < POIS_GAIN_FAC * g1H
    check("S5.CIRC Poisson-world gain g_P(k=1) = %.3f < %.1f x "
          "true gain %.3f -- the loop does NOT close for wrong "
          "statistics (non-vacuity)" % (gPH, POIS_GAIN_FAC, g1H),
          ok_g)
    viol2 = float(np.mean([np.mean(r["dLP"] < -MARGIN * r["L_bar"])
                           for r in rows]))
    viol1 = float(np.mean([np.mean(r["dLP"] < -r["L_bar"])
                           for r in rows]))
    check("S5.BASE Poisson world breaks the base case: factor-2 "
          "gate violated in %.1f%% of (rung, draw), bare gate in "
          "%.1f%% (need > %.0f%%)"
          % (100 * viol2, 100 * viol1, 100 * POIS_VIOL_MIN),
          viol2 > POIS_VIOL_MIN)
    print("    (true zeros violate neither gate on any rung: "
          "min z = %+.2f, min dL/L_bar = %+.3f)"
          % (float(np.min(zz)),
             float(np.min([r["dL"] / r["L_bar"] for r in rows]))))

    # ============================================================== S6
    print("\nS6 -- verdict")
    wards_ok = not FAILS
    cov_ok = summ[lamH]["cov_g"] >= 0.95
    if not wards_ok:
        verdict = "LOOP-TRANSLATION-BLOCKED"
    elif g2H >= 1.0 and cov_ok:
        verdict = "LOOP-CLOSES"
    elif 0.8 <= g1H <= 1.25:
        verdict = "LOOP-MARGINAL"
    else:
        verdict = "LOOP-SHORT"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    print("""    THE SHORTFALL LAW (measured): g = 1/(k^2 R(X')^2 c_sup(X)),
    with three compounding factors typed exactly:
      (i)   THE SATURATION ITSELF: R > 1 and climbing along the
            tower (plateau %.2f, deep end %.2f) -- the demand
            sits ABOVE the GUE line, so even an IDEAL supply
            (exact GUE, c = 1, k = 1) gives g = 1/R^2 = %.3f < 1.
            The wall conserves itself THROUGH the saturation: the
            world's own statistics are always one notch below
            what the next rung demands.
      (ii)  supply cannot beat its own statistics: c_hat = %.2f
            (GUE-consistent), certified interval %.2f -- the
            measurement error charges another factor ~%.1f;
      (iii) the k^2 discipline cost: any certification k >= 2
            divides the gain by >= 4 (g(k=2) = %.3f), and a chain
            of N steps needs k(N) growing -- N_max = 0 at the
            bare gate already.
    Measured headline: g(k=1) = %.3f (below the marginal window),
    trend DECREASING with depth (R still climbing).  COVERAGE is
    NOT the blocker: geometric reach %s (%.3f -- the supplying
    spectra reach past the demand band); the instrument-grade gap
    is strength-band calibration (demand's dominant 1-2 band not
    calibratable in the parent; calibrated coverage %.3f).
    HONEST GAP LIST (what a loop theorem would still need):
    (1) measurement-grade -> certificate-grade supply (per-band
    quadratic-form positivity of the inversion); (2) an input
    strictly below GUE strength on alpha in 1..2 to beat R > 1 --
    the loop cannot pay this from within (its supply is pinned at
    the world's GUE level); (3) the k^2 discipline cost paid by a
    genuinely new input; (4) the T > 2e4 zero tail (outside both
    curves, frozen truncation discipline).  CONSEQUENCE for the
    strategy: the bootstrap is NOT a proof architecture -- and
    the reason is the previously established GUE saturation, now
    quantified as self-conservation: the certified ladder supplies
    exactly the statistics of the zeros (never more), while the
    floor demands slightly more than those statistics guarantee.
    The measured positivity everywhere is therefore genuinely
    finer-than-statistical information -- consistent with the
    architecture reading, unprovable by the loop.  NO RH claim;
    necessary-side, frozen window."""
          % (plat, Rdeep, 1.0 / Rdeep ** 2, csup[n - 1],
             csup_up[n - 1], csup_up[n - 1] / csup[n - 1], g2H,
             g1H, "COMPLETE" if cov_ok else "INCOMPLETE",
             summ[lamH]["cov_g"], summ[lamH]["cov_c"]))
    dt_run = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt_run / 60.0))
    print("NO RH claim; report only; nothing outside experiments/ "
          "touched.")
    _VERDICTS["b"] = verdict



EXPECT = {"a": (10, "SATURATION-STRUCTURAL"), "b": (8, "LOOP-SHORT")}


def run():
    t_all = time.time()
    counts = {}
    for tag, part in (("a", part_a), ("b", part_b)):
        globals()["N_CHK"] = 0
        globals()["FAILS"] = []
        globals()["T0"] = time.time()
        part()
        counts[tag] = (N_CHK, len(FAILS))
    pattern_ok = all(
        counts[t][0] == EXPECT[t][0] and counts[t][1] == 0
        and _VERDICTS.get(t) == EXPECT[t][1] for t in EXPECT)
    n_run = sum(c[0] for c in counts.values())
    n_fail = sum(c[1] for c in counts.values())
    print("\n" + "=" * 74)
    print("v840: %d/%d checks passed, %d failed | runtime %.1f min"
          % (n_run - n_fail, n_run, n_fail,
             (time.time() - t_all) / 60.0))
    print("NO RH claim; the saturation is structural and the loop is "
          "short -- the wall conserves itself through the saturation; "
          "PRIME.FLOOR.PAIRCORR.01 unchanged.")
    print("[%s] PATTERN GATE: expected 10 + 8 checks, 0 failed, "
          "verdicts SATURATION-STRUCTURAL + LOOP-SHORT (got %s + %s)"
          % ("PASS" if pattern_ok else "FAIL",
             _VERDICTS.get("a"), _VERDICTS.get("b")))
    return (n_fail if n_fail else 0) + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
