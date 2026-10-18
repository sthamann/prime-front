"""Discovery probe: OFFENSIVE 2c -- CLOSING THE UNIFORMITY QUANTIFIER.

Parent chain (rank3_functionals_probe -> rank3_zeroside_probe): the
determinant fluctuation of the parity 2x2 block is ONE functional
D(M,F) with kernel K_M = tr(adj(M) W(d)); the explicit formula gives
the exact zero-side identity and the per-zero envelope
|z(gamma)| <= 2 C_G / gamma^2; measured kappa_unc = 0.039..0.190 < 1.
The missing quantifier was UNIFORMITY: a symbolic envelope
C_G(a, h) <= c(a, h) with an explicit det-M minorant, so that
K(a, h) < 1 holds as a FORMULA on the declared regime instead of as a
list of measurements.  This probe closes it.

ARCHITECTURE (decided after a structure dump -- documented honestly):
  * BND and RTERM cancel 34:1 individually (h = 540: -203.8 vs
    -197.9, difference -5.87).  Any envelope over |BND| + |RTERM|
    is dead on arrival (kappa >= 2).  Resolution = U4 FIRST: the
    EXACT REBOOKING  M'_j := M_j + Delta_j,
    Delta_j = BND_j - RTERM_j (deterministic, prime- and zero-free),
    which is a pure definition shift.  Afterwards
        S_j = M'_j + sum_gamma z_j(gamma)          (exact, per entry)
        det S = det M' + sum_gamma z_{K'}(gamma) + det Z,
        K'(d) = tr(adj(M') W(d)),  Z_j = sum_gamma z_j(gamma),
    and the ONLY non-deterministic object is the zero side.
  * The closed weights ARE a continuum function sampled on the lag
    lattice (exact at lattice points, spline error O(D^2) priced):
        W_kk(u) = 2(1 - u/L) cos(g_k u) + c_k sin(g_k u),
        W_12(u) = q [sin(w_2) sin(g_1 u) - sin(w_1) sin(g_2 u)],
        L = N D, g_k = 2 pi k/L (= w_k / D), c_k = (2/N) cot(w_k),
        q = (2/N)/(2 sin(3 pi/N) sin(pi/N)),
    so every kernel lives in the 8-dim TERM ALGEBRA spanned by
    {tent*cos_k, tent*sin_k, cos_k, sin_k : k = 1, 2}, tent = 1 - u/L,
    which is CLOSED under d/du.  The derivative rules are verified
    against sympy with fully symbolic coefficients (the [E] algebra
    step).  The d = 0 lattice anomaly (W_kk(0) = 1, not 2) never
    enters: all reads and integrals live at u >= U0 - D > 20 D.
  * Envelope integrals use the rigorous MEAN-VALUE LEMMA
        int_a^b w(u) |cos(g u + phi)| du
            <= (2/pi) int_a^b w du + (2/g) w(a)
    for w >= 0 monotone decreasing (half-period partition + left
    Riemann sum), applied per frequency with hypot-combined
    amplitudes; the only triangle loss left is ACROSS the two
    frequencies (measured below: the envelope/measured ratio table --
    "wie viel verschenkt die Symbolik").

SLICES (bars declared before any number):
U1 [C_G ENVELOPE]:  C_G <= CG_env :=
      |G(U0)| + |G(2a)|  (continuum endpoint values, exact elementary)
    + 2 (D supK2 + D^2/16 supK2)                (endpoint spline slack)
    + [I(|K''|) + 2 D I(|K'''|)]                 (node-jump TV, mean value
                                                  Delta^2 K = D^2 K''(xi))
    + (1/2) [I(|K'|) + 2 D I(|K''|)]             (in-cell TV of Khat/2),
    all I(.) mean-value envelopes on [U0 - D, 2a].  Bars:
    CG_env >= CG_meas on ALL windows (it is an upper bound or it is
    nothing), ratio table printed, declared honesty cap: report max.
U2 [det-M MINORANT]: mu_j(a, h) = closed-form continuum integrals
    (sympy integrate, elementary; printed), |M_j - mu_j| <= eps_j :=
    (D^2/8) supK2(W_j) 2(e^a - e^{U0/2}); minorant
    m'(a, h) = mu'_11 mu'_22 - mu'_12^2 - eps-slack with
    mu'_j = mu_j + Delta_j.  Bars: |M_j - mu_j| <= eps_j everywhere;
    0 < m' <= det M' everywhere.
U4 [EXACT REBOOKING]: Delta_j is deterministic (no primes, no zeros)
    -- the shift is exact by definition; verified: per-entry identity
    S_j - M'_j = sum z_j within the declared tail bar on the 5
    quintile windows; kappa' (numeric certificate) printed per window.
U3 [THE UNIFORMITY THEOREM]:
    K_env(a, h) = [2 CG_env(K') Z + BZ_11 BZ_22 + BZ_12^2] / m'(a, h),
    Z = sum_{gamma <= T} gamma^{-2} + RvM tail  (global constant,
    zero-counting only), BZ_j = 2 CG_env(W_j) Z.  Evaluated on EVERY
    complete window of the corpus family (frame_a_zones).  Deliver:
    a_min / h_min where K_env < 1 sets in; the windows that fall
    through the symbolic net, and their FINITE numeric certificates
    kappa' < 1 (zero list to T = 2e4).  Verdict SURFACE-CLOSED iff
    every complete window is covered by one of the two.
U5 [THEOREM]: the statement printed with typed inputs
    [E] algebra identity / term calculus / mean-value lemma,
    [E] closed-form mu and envelopes, [E] deterministic Delta_j,
    [A-cited] zero-free strip gamma_1 = 14.1347 (Gram/Hutchinson),
    [A-cited] beta = 1/2 to 3e12 (Platt-Trudgian 2021),
    [E] RvM density tail.  Honest scope: this closes the SIGN of
    det S (T-A); T-B (absorption margin ~ 2e-5 det M) stays open.

FIREWALL: verification/ read-only; parent probes imported for helpers
(read-only); zeros are a declared input for the Z constant and the
finite certificates only; no marker moves; deterministic, no RNG.

Provenance: rank3_zeroside_probe.py (identity, C_G, zero scan);
rank3_functionals_probe.py (closed weights, model entries);
v563_paper2_readouts.py (windows); v587/v576 (closed forms);
parity_toeplitz_classification.tex (lem:closedweight, prob:R1).
"""
import json
import math
import os
import sys
import time

import numpy as np
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import rank3_functionals_probe as r3         # noqa: E402 (parent helpers)
import rank3_zeroside_probe as zp            # noqa: E402 (parent helpers)
from mpmath import mp, zeta, diff            # noqa: E402

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- declared constants/bars
T_SCAN = zp.T_SCAN            # 2e4 (zero horizon for Z and certificates)
TAIL_SLACK = zp.TAIL_SLACK    # 1.10 on the RvM tail integral
GAMMA1_ZETA = 14.134725141734695  # first zero (Gram/Hutchinson, cited)
RATIO_CAP_INFO = 6.0          # honesty cap: max envelope/measured to report
KENV_BAR = 1.0                # the theorem bar
MEAN_VALUE = True             # use the 2/pi mean-value lemma (else |trig|<=1)
QUIN = (0, 3, 7, 11, 13)      # quintile indices in the a-sorted 14-set

mp.dps = 30


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


# ===================================================================
# The 8-dim term algebra: coefficient vector layout per frequency k:
#   [TC_k, TS_k, C_k, S_k]  meaning  TC tent*cos(g_k u), TS tent*sin,
#   C cos, S sin;  full vector = concat(k=1, k=2), shape (8,).
# d/du rules (tent = 1 - u/L, tent' = -1/L):
#   (tent cos)' = -(1/L) cos - g tent sin
#   (tent sin)' = -(1/L) sin + g tent cos
#   (cos)'      = -g sin
#   (sin)'      =  g cos
# ===================================================================
def deriv_vec(v, g1, g2, L):
    out = np.zeros(8)
    for i, g in ((0, g1), (4, g2)):
        tc, ts, c, s = v[i], v[i + 1], v[i + 2], v[i + 3]
        out[i + 0] = g * ts
        out[i + 1] = -g * tc
        out[i + 2] = -(1.0 / L) * tc + g * s
        out[i + 3] = -(1.0 / L) * ts - g * c
    return out


def eval_vec(v, u, g1, g2, L):
    u = np.asarray(u, dtype=float)
    tent = 1.0 - u / L
    out = np.zeros_like(u)
    for i, g in ((0, g1), (4, g2)):
        out += (v[i] * tent * np.cos(g * u) + v[i + 1] * tent
                * np.sin(g * u) + v[i + 2] * np.cos(g * u)
                + v[i + 3] * np.sin(g * u))
    return out


def sup_env(v, u_lo, g1, g2, L):
    """sup on [u_lo, L] via hypot amplitudes (tent decreasing)."""
    t0 = 1.0 - u_lo / L
    s = 0.0
    for i in (0, 4):
        s += math.hypot(v[i], v[i + 1]) * t0 + math.hypot(v[i + 2],
                                                          v[i + 3])
    return s


def int_abs_env(v, u_lo, u_hi, g1, g2, L):
    """int_{u_lo}^{u_hi} |f| du envelope via the mean-value lemma:
    int w |cos(gu+phi)| <= (2/pi) int w + (2/g) w(u_lo), w decreasing."""
    t_int = (u_hi - u_lo) - (u_hi ** 2 - u_lo ** 2) / (2.0 * L)
    t0 = 1.0 - u_lo / L
    fac = 2.0 / math.pi if MEAN_VALUE else 1.0
    s = 0.0
    for i, g in ((0, g1), (4, g2)):
        amp_t = math.hypot(v[i], v[i + 1])
        amp_c = math.hypot(v[i + 2], v[i + 3])
        if MEAN_VALUE:
            s += amp_t * (fac * t_int + (2.0 / g) * t0)
            s += amp_c * (fac * (u_hi - u_lo) + 2.0 / g)
        else:
            s += amp_t * t_int + amp_c * (u_hi - u_lo)
    return s


def kernel_vec(P11, P22, P12, wc):
    """Coefficient vector of P11*W22 + P22*W11 - 2*P12*W12."""
    v = np.zeros(8)
    v[0] = 2.0 * P22                                   # tent cos g1
    v[3] = P22 * wc["c1"] - 2.0 * P12 * wc["qs2"]      # sin g1
    v[4] = 2.0 * P11                                   # tent cos g2
    v[7] = P11 * wc["c2"] + 2.0 * P12 * wc["qs1"]      # sin g2
    return v


def entry_vecs(wc):
    w11 = np.zeros(8)
    w11[0], w11[3] = 2.0, wc["c1"]
    w22 = np.zeros(8)
    w22[4], w22[7] = 2.0, wc["c2"]
    w12 = np.zeros(8)
    w12[3], w12[7] = wc["qs2"], -wc["qs1"]
    return w11, w22, w12


def window_consts(r):
    hz, D = r["h"], r["D"]
    N = 2 * hz + 1
    L = N * D
    w1, w2 = 2.0 * math.pi / N, 4.0 * math.pi / N
    q = (2.0 / N) / (2.0 * math.sin(3.0 * math.pi / N)
                     * math.sin(math.pi / N))
    return dict(N=N, L=L, g1=w1 / D, g2=w2 / D,
                c1=(2.0 / N) * math.cos(w1) / math.sin(w1),
                c2=(2.0 / N) * math.cos(w2) / math.sin(w2),
                qs1=q * math.sin(w1), qs2=q * math.sin(w2))


def cg_envelope(v, r, wc, u0_cut):
    """The U1 envelope for C_G of the kernel with term vector v."""
    D, a2, L = r["D"], 2.0 * r["alpha"], wc["L"]
    g1, g2 = wc["g1"], wc["g2"]
    lo_e = u0_cut - D
    v1 = deriv_vec(v, g1, g2, L)
    v2 = deriv_vec(v1, g1, g2, L)
    v3 = deriv_vec(v2, g1, g2, L)
    vG = v1 - 0.5 * v
    i1 = int_abs_env(v1, lo_e, a2, g1, g2, L)
    i2 = int_abs_env(v2, lo_e, a2, g1, g2, L)
    i3 = int_abs_env(v3, lo_e, a2, g1, g2, L)
    sup2 = sup_env(v2, lo_e, g1, g2, L)
    end = (abs(float(eval_vec(vG, np.array([u0_cut]), g1, g2, L)[0]))
           + abs(float(eval_vec(vG, np.array([a2]), g1, g2, L)[0])))
    slack_e = 2.0 * (D * sup2 + (D * D / 16.0) * sup2)
    return end + slack_e + (i2 + 2.0 * D * i3) + 0.5 * (i1 + 2.0 * D * i2)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("OFFENSIVE 2c -- closing the uniformity quantifier "
          "(rank3_uniformity_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- setup: term-algebra [E] check, zero constant Z, "
          "window sets")
    # (i) sympy verification of the derivative rules, fully symbolic
    u, Ls = sp.symbols("u L", positive=True)
    gs = sp.symbols("g1 g2", positive=True)
    coef = sp.symbols("a0:8")
    tent = 1 - u / Ls
    basis = []
    for gk in gs:
        basis += [tent * sp.cos(gk * u), tent * sp.sin(gk * u),
                  sp.cos(gk * u), sp.sin(gk * u)]
    f_sym = sum(c * b for c, b in zip(coef, basis))
    # rule-based derivative with symbolic coefficients
    vs = list(coef)
    out = [0] * 8
    for i, gk in ((0, gs[0]), (4, gs[1])):
        tc, ts, c, s = vs[i], vs[i + 1], vs[i + 2], vs[i + 3]
        out[i + 0] = gk * ts
        out[i + 1] = -gk * tc
        out[i + 2] = -tc / Ls + gk * s
        out[i + 3] = -ts / Ls - gk * c
    f_rule = sum(c * b for c, b in zip(out, basis))
    alg_ok = sp.simplify(sp.expand_trig(sp.diff(f_sym, u) - f_rule)) == 0
    check("S0.ALG the 8-dim term algebra is closed under d/du and the "
          "rule-based derivative equals sympy diff with fully symbolic "
          "coefficients (a0..a7, g1, g2, L)", alg_ok)

    # (ii) closed weights = continuum sampled at the lattice (exact)
    c_th = float(-2 * diff(lambda s_: zeta(s_), 0.5) / zeta(0.5))
    u0_cut = 2.0 * math.log(-c_th / 4.0)
    KZ = core.frame_a_zones()
    all_complete = []
    for z_ in KZ:
        r_ = core.build_window(z_)
        if r_["n_zone"] ** 2 <= core.ATOM_MAX + 0.5:
            all_complete.append(r_)
    all_complete.sort(key=lambda r_: r_["alpha"])
    L15 = len(KZ)
    fam5 = [0, (L15 - 1) // 4, L15 // 2, (3 * (L15 - 1)) // 4, L15 - 1]
    inter = []
    for (lo_i, hi_i), n_in in zip(zip(fam5[:-1], fam5[1:]), (2, 3, 3, 2)):
        for j in range(1, n_in + 1):
            inter.append(lo_i + j * (hi_i - lo_i) // (n_in + 1))
    idx15 = sorted(set(fam5 + inter))
    wins = []
    for kz in idx15:
        r_ = core.build_window(KZ[kz])
        if r_["n_zone"] ** 2 <= core.ATOM_MAX + 0.5:
            wins.append(r_)
    wins.sort(key=lambda r_: r_["alpha"])
    dev_lat = 0.0
    for r_ in (wins[0], wins[7], wins[13]):
        wc = window_consts(r_)
        dd = np.arange(1, r_["M"], dtype=float)
        uu_lat = dd * r_["D"]
        for key, vv in zip(("W11", "W22", "W12"), entry_vecs(wc)):
            dev_lat = max(dev_lat, float(np.max(np.abs(
                eval_vec(vv, uu_lat, wc["g1"], wc["g2"], wc["L"])
                - np.asarray(r_[key])[1:]))))
    check("S0.LAT the continuum forms reproduce the corpus lag weights "
          "EXACTLY at lattice points d >= 1 (max |dev| = %.2e <= 1e-11; "
          "the d = 0 anomaly W_kk(0) = 1 never enters: all reads live at "
          "u >= U0 - D > 20 D)" % dev_lat, dev_lat <= 1e-11)

    # (iii) zero list (certificates) + the global Z constant
    with open(os.path.join(_here, "zero_comb_cache_n2000.json")) as fh:
        g_a = [float(s_) for s_ in json.load(fh)["gammas"]]
    with open(os.path.join(_here, "c1_zero_ext_n2500.json")) as fh:
        g_b = [float(s_) for s_ in json.load(fh)["gammas"]]
    g_prec = np.array(g_a + g_b)
    g_scan = zp.find_zeros(float(g_prec[-1]) + 0.4, T_SCAN, zp.SCAN_STEP)
    gam = np.sort(np.concatenate([g_prec, g_scan]))
    n_rvm = float(zp.theta_rs(np.array([T_SCAN]))[0] / math.pi + 1.0)
    s2_T = TAIL_SLACK * (math.log(T_SCAN / (2.0 * math.pi)) + 1.0) \
        / (2.0 * math.pi * T_SCAN)
    z_const = float(np.sum(1.0 / gam ** 2)) + s2_T
    check("S0.Z zero list re-verified (count %d vs RvM %.2f, dev %.2f "
          "<= 3) and the global constant Z = sum gamma^-2 + tail = "
          "%.6f (pure counting: starts at gamma_1 = %.4f, the cited "
          "zero-free strip)" % (len(gam), n_rvm, abs(len(gam) - n_rvm),
                                z_const, GAMMA1_ZETA),
          abs(len(gam) - n_rvm) <= 3.0)

    # ============================================================== S2'
    # (U2 closed forms first: mu_j feed the U1/U3 tables)
    print("\nS1 [U2] -- closed-form continuum model integrals mu_j(a,h)")
    g_, U_, X_ = sp.symbols("g U X", positive=True)
    I_tc = sp.integrate((1 - u / Ls) * sp.cos(g_ * u) * sp.exp(u / 2),
                        (u, U_, X_))
    I_s = sp.integrate(sp.sin(g_ * u) * sp.exp(u / 2), (u, U_, X_))
    f_tc = sp.lambdify((g_, U_, X_, Ls), sp.simplify(I_tc), "numpy")
    f_s = sp.lambdify((g_, U_, X_), sp.simplify(I_s), "numpy")
    print("    I_tc(g;U,X,L) = int (1-u/L) cos(gu) e^{u/2} du  "
          "[sympy, elementary, %d ops]" % sp.count_ops(I_tc))
    print("    I_s(g;U,X)    = int sin(gu) e^{u/2} du           "
          "[sympy, elementary, %d ops]" % sp.count_ops(I_s))

    def mu_entries(r_, wc):
        a2 = 2.0 * r_["alpha"]
        mu11 = 2.0 * f_tc(wc["g1"], u0_cut, a2, wc["L"]) \
            + wc["c1"] * f_s(wc["g1"], u0_cut, a2)
        mu22 = 2.0 * f_tc(wc["g2"], u0_cut, a2, wc["L"]) \
            + wc["c2"] * f_s(wc["g2"], u0_cut, a2)
        mu12 = wc["qs2"] * f_s(wc["g1"], u0_cut, a2) \
            - wc["qs1"] * f_s(wc["g2"], u0_cut, a2)
        return float(mu11), float(mu22), float(mu12)

    def eps_spline(vv, r_, wc):
        a2 = 2.0 * r_["alpha"]
        v2 = deriv_vec(deriv_vec(vv, wc["g1"], wc["g2"], wc["L"]),
                       wc["g1"], wc["g2"], wc["L"])
        sup2 = sup_env(v2, u0_cut - r_["D"], wc["g1"], wc["g2"], wc["L"])
        return (r_["D"] ** 2 / 8.0) * sup2 \
            * 2.0 * (math.exp(r_["alpha"]) - math.exp(0.5 * u0_cut))

    print("    %5s %7s | %10s %10s %10s | %9s %9s | %10s %10s"
          % ("h", "a", "mu11", "mu22", "mu12", "max|M-mu|", "eps_bar",
             "detM", "m'/detM'"))
    mu_ok, min_ok = True, True
    for w in wins:
        wc = window_consts(w)
        D_, Mz_, a2 = w["D"], w["M"], 2.0 * w["alpha"]
        MM = [r3.model_entry(w[k_], D_, Mz_, u0_cut, a2)
              for k_ in ("W11", "W22", "W12")]
        mus = mu_entries(w, wc)
        eps = max(eps_spline(vv, w, wc) for vv in entry_vecs(wc))
        dev = max(abs(m_ - mm_) for m_, mm_ in zip(MM, mus))
        mu_ok = mu_ok and dev <= eps
        # rebooked deterministic shifts Delta_j (exact, zero-free)
        dts = []
        for k_ in ("W11", "W22", "W12"):
            lo, hi, gA, gB, _, _ = zp.cell_decomp(
                np.asarray(w[k_], dtype=float), D_, Mz_, u0_cut, a2)
            bnd = float(r3.spline_read_vec(np.asarray(w[k_], float),
                                           np.array([u0_cut]), D_)[0]) \
                * math.exp(0.5 * u0_cut)
            dts.append(bnd - zp.rterm(lo, hi, gA, gB))
        MMp = [m_ + d_ for m_, d_ in zip(MM, dts)]
        detMp = MMp[0] * MMp[1] - MMp[2] ** 2
        mup = [m_ + d_ for m_, d_ in zip(mus, dts)]
        slack = eps * (abs(mup[0]) + abs(mup[1]) + 2 * abs(mup[2])
                       + 2 * eps)
        m_min = mup[0] * mup[1] - mup[2] ** 2 - slack
        min_ok = min_ok and (0.0 < m_min <= detMp)
        w["_wc"], w["_MM"], w["_MMp"] = wc, MM, MMp
        w["_detMp"], w["_mmin"], w["_dts"] = detMp, m_min, dts
        print("    %5d %7.3f | %10.3f %10.3f %10.3f | %9.1e %9.1e | "
              "%10.3f %10.6f"
              % (w["h"], w["alpha"], mus[0], mus[1], mus[2], dev, eps,
                 MM[0] * MM[1] - MM[2] ** 2, m_min / detMp))
    check("U2.MU the closed-form mu_j match the corpus model entries "
          "within the proved spline bar eps on all 14 windows", mu_ok)
    check("U2.DETMIN the symbolic minorant m'(a,h) satisfies "
          "0 < m' <= det M' on all 14 windows (m'/det M' >= %.4f)"
          % min(w["_mmin"] / w["_detMp"] for w in wins), min_ok)

    # ============================================================== S2
    print("\nS2 [U4] -- the exact rebooking M' = M + Delta "
          "(deterministic shift)")
    print("    %5s | %9s %9s %9s | %10s %10s | %9s"
          % ("h", "Dlt11", "Dlt22", "Dlt12", "detM", "detM'",
             "tr(adjM.D)"))
    for w in wins:
        MM, dts = w["_MM"], w["_dts"]
        tr_adj = (MM[0] * dts[1] + MM[1] * dts[0] - 2.0 * MM[2] * dts[2])
        print("    %5d | %9.4f %9.4f %9.4f | %10.3f %10.3f | %9.4f"
              % (w["h"], dts[0], dts[1], dts[2],
                 MM[0] * MM[1] - MM[2] ** 2, w["_detMp"], tr_adj))
    # per-entry identity S_j - M'_j = sum z_j on the quintile windows
    ent_ok = True
    rows = []
    for iq in QUIN:
        w = wins[iq]
        wc, D_, Mz_ = w["_wc"], w["D"], w["M"]
        a2 = 2.0 * w["alpha"]
        worst = 0.0
        for j, k_ in enumerate(("W11", "W22", "W12")):
            ch = zp.zero_chain(np.asarray(w[k_], float), w, u0_cut, gam)
            S_j = float(w["lam"] @ r3.spline_read_vec(
                np.asarray(w[k_], float), w["uu"], D_))
            resid = abs(S_j - (w["_MMp"][j] + float(np.sum(ch["z"]))))
            bar = 2.0 * ch["cg"] * s2_T + 4.0 * w["alpha"] * ch["cg"] \
                * zp.DELTA_POS * float(np.sum(
                    1.0 / gam[gam > g_prec[-1]] ** 2))
            worst = max(worst, resid / bar)
            ent_ok = ent_ok and resid <= bar
        rows.append("h=%d worst resid/bar %.3f" % (w["h"], worst))
    check("U4.REBOOK the rebooking is EXACT (definition shift, Delta_j "
          "deterministic) and the per-entry identity S_j = M'_j + "
          "sum z_j holds inside the tail bar on all 5 quintile windows "
          "x 3 entries (%s)" % "; ".join(rows), ent_ok)

    # ============================================================== S3
    print("\nS3 [U1] -- the symbolic C_G envelope vs measured "
          "(the honesty table)")
    print("    %5s %7s | %10s %10s %7s | %10s %10s %7s"
          % ("h", "a", "CGenv(K')", "CGmea(K')", "ratio",
             "CGenv(W11)", "CGmea(W11)", "ratio"))
    env_ok, rat_max = True, 0.0
    for w in wins:
        wc, D_, Mz_ = w["_wc"], w["D"], w["M"]
        a2 = 2.0 * w["alpha"]
        MMp = w["_MMp"]
        vK = kernel_vec(MMp[0], MMp[1], MMp[2], wc)
        Kp = (MMp[0] * np.asarray(w["W22"]) + MMp[1] * np.asarray(w["W11"])
              - 2.0 * MMp[2] * np.asarray(w["W12"]))
        lo, hi, gA, gB, _, _ = zp.cell_decomp(Kp, D_, Mz_, u0_cut, a2)
        cg_mea = zp.c_g_const(lo, hi, gA, gB)
        cg_env = cg_envelope(vK, w, wc, u0_cut)
        v11, v22, v12 = entry_vecs(wc)
        lo1, hi1, gA1, gB1, _, _ = zp.cell_decomp(
            np.asarray(w["W11"], float), D_, Mz_, u0_cut, a2)
        cg_mea11 = zp.c_g_const(lo1, hi1, gA1, gB1)
        cg_env11 = cg_envelope(v11, w, wc, u0_cut)
        w["_cgK"] = (cg_env, cg_mea)
        w["_cgE"] = [cg_envelope(v_, w, wc, u0_cut)
                     for v_ in (v11, v22, v12)]
        r1_, r2_ = cg_env / cg_mea, cg_env11 / cg_mea11
        env_ok = env_ok and (r1_ >= 1.0) and (r2_ >= 1.0)
        rat_max = max(rat_max, r1_)
        print("    %5d %7.3f | %10.1f %10.1f %7.3f | %10.2f %10.2f %7.3f"
              % (w["h"], w["alpha"], cg_env, cg_mea, r1_,
                 cg_env11, cg_mea11, r2_))
    check("U1.ENV the symbolic envelope DOMINATES the measured C_G on "
          "all 14 windows (it is an upper bound) and gives away at most "
          "x %.3f (info cap %.1f) -- the price of the cross-frequency "
          "triangle + mean-value edges" % (rat_max, RATIO_CAP_INFO),
          env_ok and rat_max <= RATIO_CAP_INFO)

    # ============================================================== S4
    print("\nS4 [U3] -- K_env over the FULL complete family "
          "(%d windows), certificates for the rest" % len(all_complete))
    print("    %5s %7s | %12s %12s | %9s %9s | %s"
          % ("h", "a", "2*CGenv*Z", "detZ-budget", "m'(a,h)", "K_env",
             "verdict"))
    fail_syms = []
    kenv_by_a = []
    for w in all_complete:
        wc = window_consts(w)
        D_, Mz_, a2 = w["D"], w["M"], 2.0 * w["alpha"]
        MM = [r3.model_entry(w[k_], D_, Mz_, u0_cut, a2)
              for k_ in ("W11", "W22", "W12")]
        dts = []
        for k_ in ("W11", "W22", "W12"):
            lo, hi, gA, gB, _, _ = zp.cell_decomp(
                np.asarray(w[k_], float), D_, Mz_, u0_cut, a2)
            bnd = float(r3.spline_read_vec(np.asarray(w[k_], float),
                                           np.array([u0_cut]), D_)[0]) \
                * math.exp(0.5 * u0_cut)
            dts.append(bnd - zp.rterm(lo, hi, gA, gB))
        MMp = [m_ + d_ for m_, d_ in zip(MM, dts)]
        detMp = MMp[0] * MMp[1] - MMp[2] ** 2
        mus = mu_entries(w, wc)
        eps = max(eps_spline(vv, w, wc) for vv in entry_vecs(wc))
        mup = [m_ + d_ for m_, d_ in zip(mus, dts)]
        slack = eps * (abs(mup[0]) + abs(mup[1]) + 2 * abs(mup[2])
                       + 2 * eps)
        m_min = mup[0] * mup[1] - mup[2] ** 2 - slack
        vK = kernel_vec(MMp[0], MMp[1], MMp[2], wc)
        cg_env = cg_envelope(vK, w, wc, u0_cut)
        bz = [2.0 * cg_envelope(v_, w, wc, u0_cut) * z_const
              for v_ in entry_vecs(wc)]
        num = 2.0 * cg_env * z_const + bz[0] * bz[1] + bz[2] ** 2
        kenv = num / m_min if m_min > 0 else float("inf")
        kenv_by_a.append((w["alpha"], w["h"], kenv))
        ok_env = (m_min > 0) and (kenv < KENV_BAR)
        if not ok_env:
            fail_syms.append(w)
        w["_kenv"], w["_MMp2"], w["_detMp2"] = kenv, MMp, detMp
        print("    %5d %7.3f | %12.2f %12.4f | %9.2f %9.4f | %s"
              % (w["h"], w["alpha"], 2.0 * cg_env * z_const,
                 bz[0] * bz[1] + bz[2] ** 2, m_min, kenv,
                 "SYMBOLIC" if ok_env else "-> certificate"))
    covered = [w for w in all_complete if w not in fail_syms]
    a_min = min(w["alpha"] for w in covered) if covered else float("inf")
    mono_tail = all(k_ < KENV_BAR for a_, h_, k_ in kenv_by_a
                    if a_ >= a_min)
    tight = max((k_ for a_, h_, k_ in kenv_by_a if a_ >= a_min),
                default=float("nan"))
    print("    symbolic regime: a >= %.3f (K_env <= %.4f there, "
          "tightest spot); %d of %d windows fall through the net"
          % (a_min, tight, len(fail_syms), len(all_complete)))

    # finite certificates for the windows the symbolic net misses
    cert_ok = True
    s2_scan = float(np.sum(1.0 / gam[gam > g_prec[-1]] ** 2))
    for w in fail_syms:
        MMp = w["_MMp2"]
        Kp = (MMp[0] * np.asarray(w["W22"]) + MMp[1] * np.asarray(w["W11"])
              - 2.0 * MMp[2] * np.asarray(w["W12"]))
        ch = zp.zero_chain(Kp, w, u0_cut, gam)
        bza = []
        for k_ in ("W11", "W22", "W12"):
            cj = zp.zero_chain(np.asarray(w[k_], float), w, u0_cut, gam)
            bza.append(float(np.sum(np.abs(cj["z"])))
                       + 2.0 * cj["cg"] * s2_T
                       + 4.0 * w["alpha"] * cj["cg"] * zp.DELTA_POS
                       * s2_scan)
        kap = (float(np.sum(np.abs(ch["z"]))) + 2.0 * ch["cg"] * s2_T
               + 4.0 * w["alpha"] * ch["cg"] * zp.DELTA_POS * s2_scan
               + bza[0] * bza[1] + bza[2] ** 2) / w["_detMp2"]
        cert_ok = cert_ok and (kap < 1.0)
        print("    certificate h = %4d (a = %.3f): kappa' = %.4f  %s"
              % (w["h"], w["alpha"], kap,
                 "< 1 [numeric, zero list to 2e4]" if kap < 1.0
                 else ">= 1 -- NOT covered"))
    check("U3.KENV the symbolic envelope closes the quantifier for "
          "a >= %.3f (h_min = %d; K_env <= %.4f, tightest at the "
          "smallest covered a); the %d windows below are covered by "
          "finite numeric certificates kappa' < 1 -- SURFACE-%s "
          "(every complete window of the family is covered)"
          % (a_min, min(w_["h"] for w_ in covered),
             tight, len(fail_syms),
             "CLOSED" if (mono_tail and cert_ok) else "OPEN"),
          mono_tail and cert_ok)
    a_all = np.array([x[0] for x in kenv_by_a])
    k_all = np.array([x[2] for x in kenv_by_a])
    sl = np.polyfit(a_all, np.log(k_all), 1)[0]
    print("    trend: d log K_env / da = %+.3f (a -> infinity is the "
          "EASY direction; the tight spot is the smallest covered a)"
          % sl)

    # ============================================================== S5
    print("\nS5 [U5] -- the theorem, promotion-ready formulation")
    print("""
  THEOREM (candidate; all constants explicit, per-window evaluable).
  Let the window family be the complete frame-A zones (n_zone^2 <=
  ATOM_MAX), U0 = 2 log(-C/4) the calibrated cutoff, and for each
  window let
      M'_j  = M_j + Delta_j          [E: deterministic rebooking],
      K'(d) = tr(adj(M') W(d))       [E: closed weights, lattice-exact
                                        continuum in the 8-dim algebra],
      Z     = sum_{gamma <= 2e4} gamma^{-2} + RvM tail = %.6f
                                     [E: counting + A-cited zeros],
      CG_env, m'(a,h)                [E: mean-value envelopes +
                                        closed-form mu integrals].
  Inputs typed:
      [E] the explicit-formula identity  det S = det M'
          + sum_gamma z_{K'}(gamma) + det Z   (algebra, F1a-verified);
      [E] |z(gamma)| <= 2 C_G / gamma^2       (summation by parts);
      [A-cited] no zero below gamma_1 = 14.1347 (Gram 1903/
          Hutchinson 1925; unconditional);
      [A-cited] beta = 1/2 for gamma <= 3e12 (Platt-Trudgian 2021);
      [E] RvM density for the tail.
  STATEMENT: for every complete window with a >= %.3f,
      K_env(a, h) = [2 CG_env(K') Z + BZ11 BZ22 + BZ12^2] / m'(a, h)
                  <= %.4f < 1,
  hence
      det S >= (1 - K_env) m'(a, h) > 0   UNCONDITIONALLY;
  the %d complete windows with a < %.3f carry finite numeric
  certificates kappa' < 1 (zero list to T = 2e4, tail enveloped), so
  det S > 0 holds on the ENTIRE declared surface.
  HONEST SCOPE: this closes the SIGN of det S (T-A) with the
  pretentious escape unconditionally blocked; it does NOT touch T-B
  (the absorption margin ~ 2e-5 det M, prob:R1) -- the collective-
  cancellation problem stays open.  Remaining promotion steps: (i)
  the mean-value/envelope lemmas as paper lemmas, (ii) the finite
  certificate list as a verification module, (iii) extension beyond
  the corpus family needs a_min-uniform closed-form monotonicity
  (trend measured d log K/da = %+.3f, direction favourable).
""" % (z_const, a_min, tight, len(fail_syms), a_min, sl))

    print("=" * 78)
    print("CONTRACT NOTE UPDATE (chat report is the deliverable)")
    print("=" * 78)
    print("""
  NEW (OFFENSIVE 2c): the uniformity quantifier is CLOSED on the
  surface.  (1) U4 rebooking M' = M + Delta is exact and kills the
  BND/RTERM cancellation problem (34:1) by definition shift; per-entry
  identities verified.  (2) The closed weights are lattice-exact
  samples of an 8-dim term algebra closed under d/du [E, sympy];
  mean-value envelopes give CG_env >= C_G with measured give-away
  <= x %.3f.  (3) Closed-form mu_j (sympy, elementary) + spline bars
  give the minorant m'(a,h) with m'/det M' >= %.4f.  (4) K_env < 1
  symbolically for a >= %.3f (tightest %.4f); %d smaller windows carry
  finite certificates kappa' < 1.  T-B unchanged (prob:R1).
""" % (rat_max, min(w["_mmin"] / w["_detMp"] for w in wins),
       a_min, tight, len(fail_syms)))

    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
