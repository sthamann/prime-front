#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v829 -- PRIME.FLOOR.DEPTHKILL.01: the authorized kill attempt on the PRIME.FLOOR.RATIO.01 envelope gate at full sieve depth SURVIVED, and the certified pole x alias FAMILY scales where the single pair dies, ONE module from two probes (16/17 with the ONE preregistered-honest S5.HLAW FAIL + 12/12 checks; discovery probes floor_envelope_depth_probe.py ENVELOPE-HOLDS-DEEP and prime_family_depth_probe.py FAMILY-SCALES, 2026-08-06, re-run identically 2026-08-07).  THE KILL ATTEMPT (the contract's own preregistered gates, NO refit): the promoted v818 envelope rho(X) = tau/tau_pnt >= c h^{-3/2} with c = 4.85 (frozen) and the capture gate cos^2 theta >= 1/2 lived on the deployed frame-A ladder (67 rungs, 2 alpha <= 12.9); this round plays gates K1 (envelope) and K2 (capture) at the certified exclusion-tower depths X = 18.375 .. 25.5 (uniform-grid D = 1/64 frames, comb caps to 1.2e11) -- the deep extension DECOUPLES depth from dimension (h = 588..816 sits INSIDE the deployed h-range while the depth jumps 12.9 -> 25.5): if rho were secretly a DEPTH law the kill would fire.  IT DOES NOT: the envelope margins e1/c = 5.76 / 6.24 / 6.53 / 7.16 / 8.17 / 8.92 hold at every deep rung and GROW monotonically with depth, the capture angle stays far above the bar (min cos^2 = 0.8486 vs 0.50), and the depth trend is non-decaying (slope +0.060 per log-unit vs bar -0.10) -- the fence survives its strongest test, and the h-law vs depth-law question is DECIDED for the h-law (rho ~ 1.7e-3..2.0e-3 essentially flat across e^X spanning three orders).  THE SINGLE-PAIR COLLAPSE (S5.HLAW, the ONE preregistered-honest FAIL of the depth probe): the fixed pair (pole x gamma_1) collapses at depth -- the gap rho/rho_cert(pair) widens 40x -> 673x and the old-subset share exponent re-measures +0.54 vs the cited +1.06 (soft tol 0.40, cross-frame) -- the deep-frame pair share is NOT the old ladder's h-law (typed, the expected miss encoded).  THE FAMILY RESCUE (FAMILY-SCALES): the certified top-100 pole x alias family (v823/v824 chain: per-rung psd remainder + float budget) carries 0.9770..0.9809 of the floor at ALL six deep rungs -- the certified family lower bound rho_certF sits within 2% of the measured rho (gap 1.02x, vs the single pair's 40..673x) -- with the Lagrange identity ward holding at the conditioning-aware machine bar, phase extraction at 6.9e-12, and the pole family carrying 1.00000 of the pair total.  ALPHA-COVERAGE (typed): the citation-grade chain (fixed T_ver = 3e12) covers alpha in {9.19, 10.36, 11.05} -- the deep alphas STRADDLE the v824 horizon alpha* ~ 11 -- and alpha in {11.75, 12.41, 12.75} stands on the per-rung verified chain only (lambda_min(A2 - M2) >= 0 on 6/6, float-resolvable above the old quadratic blanket budget on 0/6: exactly the blocker v830 removes).  Controls fire (the seed-7 scramble breaks rho in scale AND the psd chain refuses it at lambda_min = -3.8e3; the mass-matched Epstein comb is measured and typed; the dps-40 mpmath budget ward holds at 3.1e-13; the two pair implementations agree at 9.1e-14).  This module re-runs the full two-probe pipeline live at the first deep rung X = 18.375 (parity ward, frame evaluation, both kill gates, the family certification, all controls) and recomputes the deep-rung gates from the frozen reference table (downscoping predeclared in PROVENANCE).  PRIME.FLOOR.RATIO.01 stays [O]: kill gates played and survived at depth -- necessary-side evidence on frozen frames, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes floor_envelope_depth_probe.py
(2026-08-06, 16/17 checks with the ONE preregistered-honest
cross-frame S5.HLAW FAIL, ~16 min incl. the 973-s sieve to 1.19e11,
verdict ENVELOPE-HOLDS-DEEP) and prime_family_depth_probe.py
(2026-08-06, 12/12 checks, ~17 min, verdict FAMILY-SCALES); both
re-run identically at promotion (2026-08-07, logs in
experiments/tfpt-discovery/).  DOWNSCOPING (predeclared): the suite
module re-runs BOTH pipelines live at the first deep rung X = 18.375
(the deployed-path parity ward at M = 896, the uniform-grid frame
evaluation with full capture geometry, kill gates K1 + K2, the
certified-family numbers via the v823 components machinery, the
citation-chain evaluation, and the scramble / mpmath / cross-
implementation controls); the deployed 67-rung v818 ladder statistics
stand on the in-suite v818 module (cited, not rebuilt here); the five
deeper rungs X = 20.72 .. 25.5 enter as FROZEN REFERENCE (rho, e1,
cos^2, capture, cert_frac, gaps) with gates K1 / K2 / FAM and the
non-decay trend RECOMPUTED here from the frozen numbers.  Original
probe docstrings and frozen protocols live in the two probe files
verbatim.

FIREWALL: v563 / v692 / v755 / v823 / v824 READ-ONLY; mpmath VALUES
only; NO zetazero()/nzeros() calls in this module (AST-checked); the
cached RvM ordinate gamma_1 is read for the pair-brick comparison
only -- tau, tau_pnt, rho, cos^2 stay zero-free; the zero list for the
family certification is the v823 RS-scan (on-line by computation
<= 2e4, its own provenance); RNG only in the declared C1 scramble
(seed 7).  NO RH claim.
"""
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v755_simpler_schur_recursion as srp     # noqa: E402 (READ-ONLY)
import v823_prime_lagrange_floor as pp         # noqa: E402 (READ-ONLY)
import v824_prime_floor_skeleton as ft         # noqa: E402 (READ-ONLY)
import v825_prime_exclusion_ladder as xl       # noqa: E402 (READ-ONLY)
from mpmath import mp, mpf, mpc, exp as mexp, sin as msin, \
    sinh as msinh, sqrt as msqrt, re as mre    # noqa: E402 (VALUES)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
C_FROZEN = 4.85               # the contract envelope constant (NO refit)
COS2_MIN = 0.50               # frozen capture bar (v818 I1)
ENV_SLOPE = -0.10             # frozen non-decay bar (v818 I3.C1)
GRID_PER_D = 4.0              # v586 pnt_S convention
DGRID = 1.0 / 64.0
PARITY_M = 896                # parity ward rung (X = 14, table reach)
PARITY_C_ABS = 5.0e-9
K_FAM = ft.K_FAM              # certified family size (100, frozen)
FAM_BAR = 0.90                # family decision bar (frozen)
CHAIN_FAC = ft.CHAIN_FAC
COND_FAC = 64.0               # v818 FACT_COND_FAC convention
WARD_REL = pp.WARD_REL
IMAG_BAR_DEEP = 1.0e-8
T_VER = 3.0e12
MP_DPS = 40
BW_TOP = 3
BW_REL = 1.0e-8
PB_REL = 1.0e-9
SEED_SCRAMBLE = 7
ANCH_1176 = 3.8825e-6
ANCH_REL = 2.0e-2
GAMMA1_REF = 14.134725
EPSM = float(np.finfo(float).eps)
LIVE_REL = 2.0e-2             # live-vs-frozen reproduction bar

# FROZEN DEEP REFERENCE (probe runs 2026-08-06/07):
# X -> (rho, cos^2 theta, capture tau/lambda_min(A), cert_frac,
#       gap_pair)
DEEP_REF = {
    18.375: (1.959e-3, 0.8486, 1.42, 0.9777, 40.2),
    20.71875: (1.773e-3, 0.9365, 1.35, 0.9775, 54.7),
    22.09375: (1.684e-3, 0.9611, 1.20, 0.9770, 95.4),
    23.5: (1.683e-3, 0.9847, 1.08, 0.9778, 672.8),
    24.8125: (1.770e-3, 0.9917, 1.04, 0.9797, 404.4),
    25.5: (1.855e-3, 0.9763, 1.06, 0.9809, 101.4),
}
H_OF = {18.375: 588, 20.71875: 663, 22.09375: 707, 23.5: 752,
        24.8125: 794, 25.5: 816}
ALPHA_COV = ((9.19, True), (10.36, True), (11.05, True),
             (11.75, False), (12.41, False), (12.75, False))
ALPHA_STAR_CITED = 11.0
GAP_OLD = (40.2, 673.0)       # the single-pair gap trend (typed)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


# ------------------------------------------- v818 part-2 density recipe
mp.dps = 30


def eig2(M2):
    a, b, c = M2[0, 0], M2[0, 1], M2[1, 1]
    if max(abs(a), abs(b), abs(c)) == 0.0:
        return 0.0, 0.0
    mid, R = 0.5 * (a + c), math.hypot(0.5 * (a - c), b)
    return mid + R, mid - R


def pnt_cells(W11, W22, W12, D, Mz, umax, u0):
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((umax - u0) / delta))
    edges = u0 + delta * np.arange(n_cells + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    reads = np.empty((n_cells, 3))
    for j, u_j in enumerate(centers):
        reads[j, 0] = core.spline_project(W11, u_j, D, Mz)
        reads[j, 1] = core.spline_project(W22, u_j, D, Mz)
        reads[j, 2] = core.spline_project(W12, u_j, D, Mz)
    return edges, reads


def pnt_S_of(edges, reads, ulim):
    hi = np.minimum(edges[1:], ulim)
    lo = np.minimum(edges[:-1], ulim)
    m = 2.0 * (np.exp(hi / 2.0) - np.exp(lo / 2.0))
    s = m @ reads
    return np.array([[s[0], s[2]], [s[2], s[1]]])


def capture_geometry(t1, t2, A):
    wA, VA = np.linalg.eigh(A)
    l1 = float(wA[0])
    u = VA[:, 0]
    Vq, _ = np.linalg.qr(np.stack([t1, t2], axis=1))
    pu = Vq.T @ u
    return l1, float(pu @ pu)


def odd_ext(x, M):
    h = M // 2
    f = np.zeros(M)
    f[:h] = x
    f[h:] = -x[::-1]
    return f


def csinc(z):
    z = np.asarray(z, dtype=complex)
    out = np.ones_like(z)
    m = np.abs(z) > 1e-12
    out[m] = np.sin(z[m]) / z[m]
    return out


def F_of(f, phi):
    jj = np.arange(len(f))
    return np.exp(1j * np.outer(
        np.atleast_1d(np.asarray(phi, complex)), jj)) @ f


def T_pair(f1, f2, D, z):
    z = np.asarray(z, dtype=complex)
    F1p, F1m = F_of(f1, D * z), F_of(f1, -D * z)
    F2p, F2m = F_of(f2, D * z), F_of(f2, -D * z)
    return csinc(D * z / 2.0) ** 2 * D * 0.5 * (F1p * F2m + F2p * F1m)


def pair_brick(t1, t2, D, Mz, gam1):
    f1, f2 = odd_ext(t1, Mz), odd_ext(t2, Mz)
    wg = float(D * np.real(csinc(np.array([gam1 * D / 2.0]))[0] ** 2))
    F1 = complex(F_of(f1, np.array([D * gam1]))[0])
    F2 = complex(F_of(f2, np.array([D * gam1]))[0])
    rot = np.exp(-1j * (Mz - 1) * D * gam1 / 2.0) * (0.5j)
    S1, S2 = (rot * F1).real, (rot * F2).real
    a_z = 2.0 * math.sqrt(max(wg, 0.0)) * S1
    b_z = 2.0 * math.sqrt(max(wg, 0.0)) * S2
    P = np.empty((2, 2))
    for (i, j), (fa, fb) in {(0, 0): (f1, f1), (1, 1): (f2, f2),
                             (0, 1): (f1, f2)}.items():
        tp = T_pair(fa, fb, D, np.array([0.5j, -0.5j]))
        P[i, j] = P[j, i] = -0.5 * float(np.real(np.sum(tp)))
    pw, pv = np.linalg.eigh(P)
    vp = math.sqrt(max(float(pw[1]), 0.0)) * pv[:, 1]
    return float((vp[0] * b_z - a_z * vp[1]) ** 2)


def deep_window(Mz, c_at):
    hz = Mz // 2
    Tb = core.parity_basis(hz, 2)
    t1, t2 = Tb[0].copy(), Tb[1].copy()
    W11 = core.lag_weights_from_v(t1, hz)
    W22 = core.lag_weights_from_v(t2, hz)
    Wpp = core.lag_weights_from_v(t1 + t2, hz)
    W12 = 0.5 * (Wpp - W11 - W22)
    c_ar = np.asarray(core.arch_lags(Mz, DGRID), float)
    return dict(M=Mz, h=hz, t1=t1, t2=t2, W11=W11, W22=W22, W12=W12,
                c_ar=c_ar, c_at=c_at)


def floor_eval(dw, u0):
    Mz = dw["M"]
    cc = dw["c_ar"] + dw["c_at"]
    Ah = np.array([[cc @ dw["W11"], cc @ dw["W12"]],
                   [cc @ dw["W12"], cc @ dw["W22"]]])
    lam, tau = eig2(Ah)
    B2 = np.array([[dw["c_ar"] @ dw["W11"], dw["c_ar"] @ dw["W12"]],
                   [dw["c_ar"] @ dw["W12"], dw["c_ar"] @ dw["W22"]]])
    edges, reads = pnt_cells(dw["W11"], dw["W22"], dw["W12"], DGRID,
                             Mz, Mz * DGRID + 1e-9, u0)
    Sp = pnt_S_of(edges, reads, Mz * DGRID)
    _, tau_p = eig2(B2 - Sp)
    A = core.odd_toeplitz(cc, Mz)
    lmin_A, cos2 = capture_geometry(dw["t1"], dw["t2"], A)
    del A
    return dict(A2=Ah, lam=lam, tau=tau, tau_pnt=tau_p,
                rho=tau / tau_p, det=lam * tau, cos2=cos2,
                cap=tau / lmin_A)


def mp_family_term(f1, f2, D, Mz, g):
    """One family term x_pz(gamma)^2 in mpmath (budget ward)."""
    mp.dps = MP_DPS
    Dm, gm = mpf(D), mpf(repr(float(g)))
    jj = range(Mz)
    ph = [mexp(mpc(0, 1) * Dm * gm * j) for j in jj]
    F1 = sum(mpf(repr(float(f1[j]))) * ph[j] for j in jj)
    F2 = sum(mpf(repr(float(f2[j]))) * ph[j] for j in jj)
    rot = mexp(-mpc(0, 1) * (Mz - 1) * Dm * gm / 2) * mpc(0, "0.5")
    hw = Dm * gm / 2
    wg = Dm * (msin(hw) / hw) ** 2
    a_z = 2 * msqrt(wg) * mre(rot * F1)
    b_z = 2 * msqrt(wg) * mre(rot * F2)
    dec = [mexp(-Dm * j / 2) for j in jj]
    grw = [mexp(Dm * j / 2) for j in jj]
    Fm = {}
    for tag, f in (("1", f1), ("2", f2)):
        Fm["p" + tag] = sum(mpf(repr(float(f[j]))) * dec[j]
                            for j in jj)
        Fm["m" + tag] = sum(mpf(repr(float(f[j]))) * grw[j]
                            for j in jj)
    cs = msinh(Dm / 4) / (Dm / 4)
    pref = cs * cs * Dm / 2
    P = {}
    for (i, j), (fa, fb) in {(0, 0): ("1", "1"), (1, 1): ("2", "2"),
                             (0, 1): ("1", "2")}.items():
        tsum = pref * (Fm["p" + fa] * Fm["m" + fb]
                       + Fm["p" + fb] * Fm["m" + fa])
        P[(i, j)] = P[(j, i)] = -tsum
    mid = (P[(0, 0)] + P[(1, 1)]) / 2
    rad = msqrt(((P[(0, 0)] - P[(1, 1)]) / 2) ** 2 + P[(0, 1)] ** 2)
    lmax = mid + rad
    v0, v1 = P[(0, 1)], lmax - P[(0, 0)]
    nrm = msqrt(v0 * v0 + v1 * v1)
    sq = msqrt(lmax if lmax > 0 else mpf(0))
    vp0, vp1 = sq * v0 / nrm, sq * v1 / nrm
    x = a_z * vp1 - b_z * vp0
    return float(x * x)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("v829 -- PRIME.FLOOR.DEPTHKILL.01: the envelope kill "
          "attempt at depth + the family")
    print("(two probes: ENVELOPE-HOLDS-DEEP + FAMILY-SCALES; live at "
          "X = 18.375, deeper")
    print(" rungs frozen reference -- downscoping predeclared in "
          "PROVENANCE; NO RH claim)")
    print("=" * 78)

    # ==================================================== S0: freeze
    print("\nS0 -- firewall + the frozen kill gates")
    check("S0.AST no zeta-zero generator call in this module (mpmath "
          "VALUES only; RNG only in the declared C1 scramble)",
          xl.ast_zero_firewall(__file__))
    g1 = float(json.load(open(xl.CACHE))["gammas"][0])
    check("S0.G1 cached RvM ordinate gamma_1 = %.6f (read for the "
          "pair-brick comparison ONLY; rho / cos^2 stay zero-free)"
          % g1, abs(g1 - GAMMA1_REF) < 1e-5)
    from mpmath import zeta as _zeta, diff as _diff
    c_th = float(-2 * _diff(lambda s: _zeta(s), 0.5) / _zeta(0.5))
    u0 = 2.0 * math.log(-c_th / 4.0)
    print("    frozen gates (the contract's own, NO refit): K1 "
          "envelope rho h^{3/2} >= c = %.2f; K2 capture cos^2 >= "
          "%.2f; non-decay bar %.2f; v583 constant -2 zeta'/zeta"
          "(1/2) = %.4f" % (C_FROZEN, COS2_MIN, ENV_SLOPE, c_th))

    # ==================================================== S1: parity
    print("\nS1 -- deployed-path parity ward at M = %d" % PARITY_M)
    n_pw = xl.nmax_of_M(PARITY_M)
    lam_tab = core.von_mangoldt_table(n_pw)
    nn0 = np.nonzero(lam_tab > 0.0)[0]
    u_pw = np.log(nn0.astype(float))
    mu_pw = 2.0 * lam_tab[nn0] / np.sqrt(nn0.astype(float))
    del lam_tab
    c_slow, _ = core.atom_lags_at(0.5 * PARITY_M * DGRID, PARITY_M,
                                  u_pw, mu_pw)
    cs_pw, cnt_pw, _, _ = xl.seg_assemble([PARITY_M])
    dev_pw = float(np.max(np.abs(cs_pw[PARITY_M] - c_slow)))
    check("S1.PARITY segmented assembly == deployed T115 path at "
          "M = %d (%d atoms): max |dc| = %.2e <= %.0e"
          % (PARITY_M, cnt_pw[PARITY_M], dev_pw, PARITY_C_ABS),
          cnt_pw[PARITY_M] == len(u_pw) and dev_pw <= PARITY_C_ABS)

    # ==================================================== S2: live rung
    print("\nS2 -- the live deep rung X = 18.375 (frame evaluation + "
          "kill gates)")
    cs, cnt, masses_scr, _ = xl.seg_assemble([1176],
                                             collect_mass_M=1176)
    cT = srp.continuum_lags(1176)[:1176] + cs[1176][:1176]
    lam1176 = float(sla.eigvalsh(sla.toeplitz(cT),
                                 subset_by_index=[0, 0])[0])
    check("S2.ANCH the certified-rung lambda_min anchor reproduces: "
          "%.4e vs cited %.4e (rel %.4f <= %.2f)"
          % (lam1176, ANCH_1176,
             abs(lam1176 - ANCH_1176) / ANCH_1176, ANCH_REL),
          abs(lam1176 - ANCH_1176) / ANCH_1176 <= ANCH_REL)
    dw = deep_window(1176, cs[1176][:1176])
    ev = floor_eval(dw, u0)
    h = dw["h"]
    e1 = ev["rho"] * h ** 1.5
    rho_ref = DEEP_REF[18.375][0]
    print("    live frame: lambda = %.4e, tau = %.4e, tau_pnt = "
          "%.4e, rho = %.4e, e1 = %.2f, cos^2 = %.4f, capture = "
          "%.2f" % (ev["lam"], ev["tau"], ev["tau_pnt"], ev["rho"],
                    e1, ev["cos2"], ev["cap"]))
    check("S2.LIVE the live frame reproduces the frozen reference "
          "rho = %.3e (rel %.4f <= %.2f)"
          % (rho_ref, abs(ev["rho"] - rho_ref) / rho_ref, LIVE_REL),
          abs(ev["rho"] - rho_ref) / rho_ref <= LIVE_REL)
    check("S2.K1 THE ENVELOPE GATE live: e1 = rho h^{3/2} = %.2f >= "
          "c = %.2f (margin x%.2f) -- the kill does NOT fire"
          % (e1, C_FROZEN, e1 / C_FROZEN), e1 >= C_FROZEN)
    check("S2.K2 THE CAPTURE GATE live: cos^2 theta = %.4f >= %.2f "
          "-- no collapse" % (ev["cos2"], COS2_MIN),
          ev["cos2"] >= COS2_MIN)

    # ==================================================== S3: family
    print("\nS3 -- the certified family live at X = 18.375 "
          "(v823 chain)")
    gam, n_rvm = pp.zero_list()
    check("S3.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    wd = dict(f1=odd_ext(dw["t1"], 1176), f2=odd_ext(dw["t2"], 1176),
              D=DGRID, M=1176, h=588)
    a, b, meta = pp.components_of(wd, gam)
    M2 = np.array([[float(a @ a), float(a @ b)],
                   [float(a @ b), float(b @ b)]])
    det_m2 = float(np.linalg.det(M2))
    x_pz = a[:-1] * b[-1] - b[:-1] * a[-1]
    x2 = x_pz ** 2
    order = np.argsort(x2)[::-1]
    cert1 = float(np.sum(x2[order[:K_FAM]]))
    det_a2 = ev["lam"] * ev["tau"]
    bud = CHAIN_FAC * EPSM * (float(np.linalg.norm(ev["A2"])) ** 2
                              + float(np.linalg.norm(M2)) ** 2)
    lam_r = ft.eig2_min(ev["A2"] - M2)
    cert_frac = (cert1 - bud) / det_a2
    fam_pt = float(np.sum(x2)) / det_m2
    cf_ref = DEEP_REF[18.375][3]
    print("    fam/pt = %.5f, cert_frac = %.4f (frozen %.4f), "
          "lambda_min(A2 - M2) = %.2e, residue = %.4f"
          % (fam_pt, cert_frac, cf_ref, lam_r,
             1.0 - det_m2 / det_a2))
    check("S3.META phase extraction + pole rank-one at depth: "
          "imag_res = %.1e <= %.0e, pole_dev = %.1e <= 1e-8"
          % (meta["imag_res"], IMAG_BAR_DEEP, meta["pole_dev"]),
          meta["imag_res"] <= IMAG_BAR_DEEP
          and meta["pole_dev"] <= 1.0e-8)
    tot, _ = pp.pair_scan(a, b, pp.K_TOP)
    cond = (abs(M2[0, 0] * M2[1, 1]) + M2[0, 1] ** 2) \
        / max(abs(det_m2), 1e-300)
    bar = max(WARD_REL, COND_FAC * EPSM * cond)
    rel_id = abs(tot - det_m2) / max(abs(det_m2), 1e-300)
    check("S3.ID the Lagrange identity ward at depth: SOS == det M2 "
          "(rel %.2e <= conditioning-aware bar %.2e, det cond %.1e)"
          % (rel_id, bar, cond), rel_id <= bar)
    check("S3.FAM the certified family carries the floor live: "
          "cert_frac = %.4f >= %.2f (frozen %.4f, rel %.4f <= "
          "%.2f), pole family %.5f >= 0.999 of the pair total, "
          "lambda_min(A2 - M2) = %.2e >= 0"
          % (cert_frac, FAM_BAR, cf_ref,
             abs(cert_frac - cf_ref) / cf_ref, LIVE_REL, fam_pt,
             lam_r),
          cert_frac >= FAM_BAR
          and abs(cert_frac - cf_ref) / cf_ref <= LIVE_REL
          and fam_pt >= 0.999 and lam_r >= 0.0)
    rho_cf = (cert1 - bud) / (ev["lam"] * ev["tau_pnt"])
    rho_cp = float(x2[0]) / (ev["lam"] * ev["tau_pnt"])
    gap_f = ev["rho"] / rho_cf
    gap_p = ev["rho"] / rho_cp
    check("S3.SYN the synthesis live: the certified family bound "
          "rho_certF = %.3e sits %.2fx below the measured rho (the "
          "single-pair bound sits %.0fx below -- the pair collapse "
          "the family rescues)" % (rho_cf, gap_f, gap_p),
          rho_cf <= ev["rho"] * (1 + 1e-9) and gap_f <= 1.10
          and gap_p >= 10.0)

    # ==================================================== S4: controls
    print("\nS4 -- controls (live)")
    rng = np.random.default_rng(SEED_SCRAMBLE)
    u_scr = rng.uniform(0.0, 1176 * DGRID, size=masses_scr.size)
    c_scr = np.zeros(1176)
    xl.tent_accumulate(c_scr, 1176, u_scr, masses_scr)
    ccs = dw["c_ar"] + c_scr
    A2s = np.array([[ccs @ dw["W11"], ccs @ dw["W12"]],
                    [ccs @ dw["W12"], ccs @ dw["W22"]]])
    lam_s, tau_s = eig2(A2s)
    lam_r_scr = ft.eig2_min(A2s - M2)
    scale_broken = (tau_s < 0.0
                    or abs(math.log(max(abs(tau_s / ev["tau"]),
                                        1e-300))) > math.log(3.0))
    check("S4.C1 [must-fire] scramble at M = 1176 (SAME %d masses, "
          "seed %d): tau %.3e -> %.3e (scale broken: %s) AND the "
          "psd chain refuses the scrambled comb, lambda_min(A2_scr "
          "- M2) = %.3e < 0"
          % (masses_scr.size, SEED_SCRAMBLE, ev["tau"], tau_s,
             scale_broken, lam_r_scr),
          scale_broken and lam_r_scr < 0.0)
    bw_dev = 0.0
    for i in order[:BW_TOP]:
        x2mp = mp_family_term(wd["f1"], wd["f2"], DGRID, 1176,
                              gam[int(i)])
        bw_dev = max(bw_dev, abs(x2mp - float(x2[int(i)]))
                     / max(x2mp, 1e-300))
    check("S4.C2 budget ward: the top-%d family carriers recomputed "
          "in mpmath (dps %d) match the float chain to rel %.1e <= "
          "%.0e" % (BW_TOP, MP_DPS, bw_dev, BW_REL), bw_dev <= BW_REL)
    pb = pair_brick(dw["t1"], dw["t2"], DGRID, 1176, g1)
    pb_dev = abs(pb - float(x2[0])) / max(float(x2[0]), 1e-300)
    check("S4.C3 cross-implementation: pair_brick == "
          "x_pz(gamma_1)^2 (rel dev %.1e <= %.0e)"
          % (pb_dev, PB_REL), pb_dev <= PB_REL)

    # ================================ R: frozen deep gates (recomputed)
    print("\nR -- THE DEEP TABLE (frozen reference; kill gates + "
          "family recomputed)")
    print("  %10s %5s | %10s %8s %8s | %8s %8s | %8s"
          % ("X", "h", "rho", "e1", "e1/c", "cos^2", "cert/fl",
             "gap_pair"))
    e1_ref = {}
    for X in sorted(DEEP_REF):
        rho, cos2, cap, cf, gp = DEEP_REF[X]
        e1_ref[X] = rho * H_OF[X] ** 1.5
        print("  %10.5f %5d | %10.3e %8.2f %8.2f | %8.4f %8.4f | "
              "%8.1f" % (X, H_OF[X], rho, e1_ref[X],
                         e1_ref[X] / C_FROZEN, cos2, cf, gp))
    check("R1.K1 THE ENVELOPE KILL GATE at all six deep rungs "
          "(recomputed): min margin e1/c = %.2f >= 1, and the "
          "deepest margin %.2f EXCEEDS the shallowest %.2f -- the "
          "envelope survives GROWING (K1 does not fire; "
          "ENVELOPE-HOLDS-DEEP)"
          % (min(e1_ref[X] / C_FROZEN for X in DEEP_REF),
             e1_ref[25.5] / C_FROZEN, e1_ref[18.375] / C_FROZEN),
          all(e1_ref[X] >= C_FROZEN for X in DEEP_REF)
          and e1_ref[25.5] > e1_ref[18.375])
    check("R2.K2 THE CAPTURE KILL GATE (recomputed): min cos^2 = "
          "%.4f >= %.2f at every deep rung (K2 does not fire)"
          % (min(DEEP_REF[X][1] for X in DEEP_REF), COS2_MIN),
          all(DEEP_REF[X][1] >= COS2_MIN for X in DEEP_REF))
    xs = sorted(DEEP_REF)
    sl_X = float(np.polyfit(xs, [math.log(e1_ref[X]) for X in xs],
                            1)[0])
    check("R3.TREND non-decay at depth (recomputed): the depth trend "
          "of e1 is %+.4f per X unit >= %.2f, and rho stays in the "
          "band [%.2e, %.2e] while e^X spans THREE orders -- the "
          "h-law vs depth-law question is decided for the h-law "
          "(the deep rungs decouple depth from dimension, "
          "cross-frame comparison typed)"
          % (sl_X, ENV_SLOPE,
             min(DEEP_REF[X][0] for X in DEEP_REF),
             max(DEEP_REF[X][0] for X in DEEP_REF)),
          sl_X >= ENV_SLOPE)
    check("R4.FAM FAMILY-SCALES (recomputed): cert_frac = "
          "%.4f..%.4f >= %.2f at ALL six deep rungs while the "
          "single-pair gap widens %.0fx -> %.0fx (S5.HLAW: the old "
          "ladder's h^{+1.06} pair share law does NOT continue on "
          "the deep frames -- the single-pair collapse, typed; the "
          "FAMILY carries the floor)"
          % (min(DEEP_REF[X][3] for X in DEEP_REF),
             max(DEEP_REF[X][3] for X in DEEP_REF), FAM_BAR,
             GAP_OLD[0], GAP_OLD[1]),
          all(DEEP_REF[X][3] >= FAM_BAR for X in DEEP_REF))
    n_cit = sum(1 for _, c in ALPHA_COV if c)
    check("R5.ALPHA alpha-coverage (frozen, typed): citation grade "
          "(fixed T_ver = %.0e) covers alpha in {%s} -- straddling "
          "the v824 horizon alpha* ~ %.0f -- and alpha in {%s} "
          "stands on the per-rung verified chain only "
          "(float-resolvable above the old quadratic budget on 0/6: "
          "the v830 blocker)"
          % (T_VER,
             ", ".join("%.2f" % a for a, c in ALPHA_COV if c),
             ALPHA_STAR_CITED,
             ", ".join("%.2f" % a for a, c in ALPHA_COV if not c)),
          n_cit == 3)

    # ============================================================== V
    print("\n" + "=" * 78)
    ok_pair = (all(e1_ref[X] >= C_FROZEN for X in DEEP_REF)
               and all(DEEP_REF[X][1] >= COS2_MIN for X in DEEP_REF)
               and all(DEEP_REF[X][3] >= FAM_BAR for X in DEEP_REF))
    print("V -- verdict pair (recomputed): %s + %s"
          % ("ENVELOPE-HOLDS-DEEP" if ok_pair else "?!",
             "FAMILY-SCALES" if ok_pair else "?!"))
    print("=" * 78)
    print("  PRIME.FLOOR.RATIO.01 stays [O]: the kill gates were "
          "played at the contract's own\n  preregistration and "
          "SURVIVED at full sieve depth; necessary-side evidence "
          "on\n  frozen frames; interlacing still runs floor => "
          "margin only; NO RH claim.")
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    ok = not FAILS and ok_pair
    print("[%s] PATTERN GATE: expected all checks green with the "
          "verdict pair ENVELOPE-HOLDS-DEEP + FAMILY-SCALES"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
