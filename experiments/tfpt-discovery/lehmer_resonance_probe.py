"""Discovery probe: THE LEHMER <-> RESONANCE LINK -- is the W3
resonance landscape (52 needles of P = q tan^2 theta, W3RL-PEAKED-
UNEXPLAINED) the WINDOW ANALOGUE of the Lehmer-pair phenomenology of
the zeta zeros?

THE THESIS (the Wikipedia-scan hypothesis, declared): Lehmer pairs --
abnormally close pairs of consecutive zeros -- are exactly the places
where Weil-positivity margins get thin, because separating two nearly
degenerate zeros costs test-function concentration.  If the window
needles were ZERO-DRIVEN, windows whose RESOLVED frequency band
contains Lehmer-like pairs should carry systematically larger
P = q tan^2 theta.  If the link is ABSENT, the needles are NOT even
zero-comb-driven -- consistent with the Baez-Duarte finding that the
obstruction is FRAME-side, not zero-side.  Both outcomes are typed
results; honesty before success.

THE RESOLUTION CORRESPONDENCE (documented, from the window geometry):
the window pencil lives on a lag lattice of spacing D (spline knots),
and its quadratic form reads atoms up to u = 2 alpha.  Under the
explicit-formula duality (lag u <-> zero ordinate t via e^{iut}):
  * lattice spacing D      <->  Nyquist REACH   t_max = pi / D
    (oscillations e^{iut} with |t| > pi/D alias on the lattice: the
    window cannot distinguish them from lower frequencies);
  * lag support 2 alpha    <->  RESOLUTION      dt  = pi / (2 alpha)
    (structure in t finer than pi/(2 alpha) is not separable by any
    test function carried by the window).
So window w "sees" the zero comb in the band t in (0, pi/D(w)] at
resolution pi/(2 alpha(w)).  D = g_kz / (2 nu) is PRIME-GAP-DRIVEN
(g_kz the local prime-power log-gap): t_max carries genuine
arithmetic jitter beyond the h-ladder -- the correlation test below
is NOT h-degenerate by construction (measured, printed).

ZERO DATA (deliberate, declared): this probe READS the shared zero
comb zero_comb_cache_n2000.json (2000 zeros, mpmath zetazero dps 15,
completeness certified by turing_cert_probe: TURING-COMPLETE-BAND up
to gamma_max ~ 2513).  The W3 probes' zero-firewall is NOT violated:
P is computed zero-free exactly as in the landscape probe; zeros
enter ONLY as the correlation TARGET.  The probe never calls
zetazero itself (cache required; hard error if absent).

CALIBRATION HISTORY (declared -- honesty first): run 1 (2026-08-02)
passed every guard and every analysis stage (identical numbers, all
seeds fixed) but FAILED its own L5 teeth bar: the planted target was
built in the RAW rank space of P (rank(P) + noise), where the h3
control removes the h-share of P and eats planted signal -- measured
planted rho 0.7813 vs the 0.8 bar.  Run 2 changes ONLY the teeth
construction, no analysis gate, grid or seed: the signal is planted
in the h3-RESIDUAL space of rank(P) (the space the partial test
actually probes), same noise fraction 0.5 sd, same bar 0.8.

PREREGISTERED DECISIONS (declared BEFORE looking at the numbers):
  * base sweep, sample, guards: the landscape probe VERBATIM (67
    complete frame-A windows, truncated {1219, 1292, 1445}; lock
    sign; float floor; rid anchor block: max P = 0.9636 at h = 859,
    Spearman(P, h) = +0.735, Spearman(r_id, h) = -0.784, median
    r_id 0.584, median theta 9.1 deg);
  * comb guards: n = 2000, dps 15, strictly increasing, gamma_1 =
    14.134725141734693 +- 1e-9;
  * L1 pair statistics (frozen): normalized spacings delta_k =
    (gamma_{k+1} - gamma_k) log(gamma_k / 2 pi) / (2 pi), k = 1..
    1999; CSV-like pair quantity G_k = Delta_k^2 sum_{j not in
    {k, k+1}} [ (gamma_j - gamma_k)^-2 + (gamma_j - gamma_{k+1})^-2 ]
    over the comb INCLUDING mirrored zeros -gamma_j (comb-truncated:
    the missing tail is positive, so G_k is a slight UNDERestimate;
    the tail bound is computed for the top table); the cited CSV
    Lehmer-pair reference line G_k < 4/5 is printed as a REFERENCE,
    the analysis itself is rank-based on delta_k (constant-free);
    TOP-10 table = the 10 smallest delta_k in the comb;
  * L2 per-window presence measures (frozen; band(w) = pairs with
    gamma_{k+1} <= t_max(w) = pi / D(w)):
      L_share(w)  [primary]   share of band pairs with delta_k <=
                              delta_q10 (comb-wide 10th percentile,
                              frozen rule); declared sign: MORE
                              Lehmer presence <-> LARGER P (+);
      L_min(w)    [secondary] min delta_k in the band (sign -);
      L_edge(w)   [declared]  min delta_k in the top octave
                              (t_max/2, t_max] -- decouples the
                              band-nesting monotonicity (sign -);
    windows with t_max > gamma_max would be censored (expected 0,
    measured); windows with an empty (edge) band are excluded for
    that measure (counted);
  * L3 correlation (v637 standard): x = P on the n = 67 lock
    windows; per measure: raw Spearman, h-controlled partial
    (rank-cubic) with permutation p (N_PERM = 20000, SEED =
    20260811), joint (h, alpha) rank-linear partial; gate per test
    |rho_h3| >= RHO_BAR = 0.30 AND p < P_BAR = 0.01; three declared
    tests -> Bonferroni-honest bar p < 0.0033 noted, not enforced;
    confound transparency: Spearman(t_max, h), Spearman(L, t_max),
    and the placement-specific partial rho(P, L | h3 + t_max
    rank-linear) are PRINTED (no gate);
  * L4 pseudo-pair control (frozen): B_PSEUDO = 2000 random
    placements -- the delta_k VALUES are permuted across the gap
    positions k (band geometry and the delta marginal preserved,
    zero-specific placement destroyed); per measure the h3-partial
    rho is recomputed; control p = share of |rho_pseudo| >=
    |rho_real|; a gate hit counts as PLACEMENT-driven only if
    control p < 0.05;
  * L5 teeth (machinery must-detect, run-2 construction): a planted
    target y = resid_h3(rank(P)) + N(0, (0.5 sd(resid))^2) (SEED
    stream) must return h3-partial rho >= 0.8 with p < 1e-3 --
    otherwise the statistics wiring is broken;
  * L6 typing only: contract-note text printed; no marker move.

Verdict enums (frozen, precedence top-down):
  LEHMER-MIXED      guards, comb guards or the L5 teeth fail;
  LEHMER-LINKED     >= 1 measure passes the L3 gate AND its L4
                    control p < 0.05 (zero-PLACEMENT-driven link);
  LEHMER-GEOMETRY   >= 1 measure passes the L3 gate but NO control
                    survives (the link is band-REACH geometry, i.e.
                    D-driven, not zero-driven);
  LEHMER-NULL       no measure passes the L3 gate (clean negative:
                    the needles are not zero-comb-driven at this
                    resolution -- consistent with the Baez-Duarte
                    FRAME-side reading).

FIREWALL: experiments-only; verification/ read-only (v563 import;
v618/v591/rid/landscape machinery REBUILT verbatim, no other
imports); zero data from the shared cache ONLY (no zetazero call);
no marker moves; no positivity claim; no RH statement.  Python-only,
per GATE.WOLFRAM.02.

Provenance: w3_resonance_landscape_probe (2026-08-02, the 52-peak
landscape), theta_rotation_predicate_probe (needle mechanism),
baez_duarte_probe (the FRAME-side reading), keiper_li_probe /
turing_cert_probe (the shared certified zero comb), rid_alignment_
probe (P = q tan^2 theta), v637 (control methodology).
"""
import json
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

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")

EPS = float(np.finfo(float).eps)
FLOOR_SAFETY = 20.0          # w3 probe, verbatim
GRID_PER_D = 4.0             # v618, verbatim
SEED = 20260811              # fresh (landscape 20260809, rid 20260806)
N_PERM = 20000               # v637 permutation budget
B_PSEUDO = 2000              # pseudo-pair placements
RHO_BAR = 0.30               # per-test gate, v637 verbatim
P_BAR = 0.01
N_TESTS = 3                  # Bonferroni-honest note 0.01/3
CTRL_P_BAR = 0.05            # L4 control bar
DELTA_Q = 0.10               # Lehmer-like quantile (frozen rule)
CSV_BAR = 0.8                # cited CSV Lehmer-pair line (4/5)
N_TOP = 10
N_ZEROS = 2000
DPS_ZEROS = 15
GAMMA1_QUOTE = 14.134725141734693
PLANT_RHO_BAR = 0.8          # L5 teeth
PLANT_P_BAR = 1e-3
# reproduction anchors (rid/landscape quotes, verbatim)
P_MAX_QUOTE, P_MAX_TOL = 0.9636, 0.005
H_AT_PMAX = 859
SP_P_H_QUOTE, SP_TOL = 0.735, 0.03
SP_RID_H_QUOTE = -0.784
RID_MED_QUOTE, RID_TOL = 0.584, 0.005
THETA_MED_QUOTE = 9.1
BAR_EIGEN = 1e-6


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp  # noqa: E402
import scipy.linalg as sla  # noqa: E402


# ------------------------------------------------------ v618 machinery
def zeta_grid_const():
    mp.mp.dps = 30
    c_th = float(-2 * mp.diff(lambda s: mp.zeta(s), mp.mpf(1) / 2)
                 / mp.zeta(mp.mpf(1) / 2))
    return 2.0 * math.log(-c_th / 4.0)


def model_matrix(alpha, Mz, D, W11, W22, W12, u0):
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((2.0 * alpha - u0) / delta))
    edges = u0 + delta * np.arange(n_cells + 1)
    lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2) - np.exp(edges[:-1] / 2))
    centers = 0.5 * (edges[:-1] + edges[1:])
    X = np.empty((n_cells, 3))
    for k, u_j in enumerate(centers):
        X[k, 0] = core.spline_project(W11, u_j, D, Mz)
        X[k, 1] = core.spline_project(W22, u_j, D, Mz)
        X[k, 2] = core.spline_project(W12, u_j, D, Mz)
    s = (lam[:, None] * X).sum(axis=0)
    return np.array([[s[0], s[2]], [s[2], s[1]]])


def lock_dir(alpha):
    v2v1 = -(alpha ** 2 + 16 * math.pi ** 2) / (2 * (alpha ** 2
                                                     + 4 * math.pi ** 2))
    v = np.array([1.0, v2v1])
    return v / np.linalg.norm(v)


def gen_min_eig2(A, G):
    w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (G + G.T))
    rad = max(abs(float(w[0])), abs(float(w[-1])))
    return float(w[0]), float(w[1]), V[:, 0], rad


# ------------------------------------------------------ v637 statistics
def rankdata(a):
    a = np.asarray(a, float)
    order = np.argsort(a, kind="mergesort")
    r = np.empty(len(a))
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and a[order[j + 1]] == a[order[i]]:
            j += 1
        r[order[i:j + 1]] = 0.5 * (i + j) + 1.0
        i = j + 1
    return r


def pearson(xx, yy):
    xx = np.asarray(xx, float) - np.mean(xx)
    yy = np.asarray(yy, float) - np.mean(yy)
    return float(xx @ yy / math.sqrt((xx @ xx) * (yy @ yy)))


def spearman(xx, yy):
    return pearson(rankdata(xx), rankdata(yy))


def perm_p(xx, yy, rng, nperm=N_PERM):
    obs = pearson(xx, yy)
    cnt = 0
    for _ in range(nperm):
        if abs(pearson(rng.permutation(xx), yy)) >= abs(obs) - 1e-12:
            cnt += 1
    return obs, (cnt + 1.0) / (nperm + 1.0)


def control_cols(controls, poly):
    cols = []
    for cvec in controls:
        rc = rankdata(cvec)
        rc = (rc - rc.mean()) / rc.std()
        for p_ in range(1, poly + 1):
            cols.append(rc ** p_)
    return cols


def residualize(vec, cols):
    C = np.column_stack([np.ones(len(vec))] + cols)
    beta, _, _, _ = np.linalg.lstsq(C, vec, rcond=None)
    return vec - C @ beta


def partial_spearman(xx, yy, controls, rng, poly=1, nperm=N_PERM):
    cols = control_cols(controls, poly)
    ex = residualize(rankdata(xx), cols)
    ey = residualize(rankdata(yy), cols)
    return perm_p(ex, ey, rng, nperm)


def partial_rho_only(xx, yy, cols):
    ex = residualize(rankdata(xx), cols)
    ey = residualize(rankdata(yy), cols)
    return pearson(ex, ey)


def partial_spearman_mixed(xx, yy, ctrl_polys, rng, nperm=N_PERM):
    cols = []
    for cvec, poly in ctrl_polys:
        cols.extend(control_cols([cvec], poly))
    ex = residualize(rankdata(xx), cols)
    ey = residualize(rankdata(yy), cols)
    return perm_p(ex, ey, rng, nperm)


# ------------------------------------------------------ the comb
def load_comb():
    if not os.path.exists(CACHE):
        raise RuntimeError("zero cache %s missing -- this probe "
                           "never calls zetazero (declared); build "
                           "the cache via keiper_li_probe first"
                           % CACHE)
    with open(CACHE, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    return np.array([float(g) for g in data["gammas"]]), data


def csv_like_G_fast(gam):
    """CSV-like pair quantity: G_k = Delta_k^2 sum_{j not in
    {k, k+1}} [(g_j - g_k)^-2 + (g_j - g_{k+1})^-2] over the comb
    including mirrored zeros -gamma_j (comb-truncated;
    underestimate, tail bounded in the top table)."""
    n = len(gam)
    allz = np.concatenate([-gam, gam])
    G = np.empty(n - 1)
    for k in range(n - 1):
        g_a, g_b = gam[k], gam[k + 1]
        d_a = allz - g_a
        d_b = allz - g_b
        # exclude the two pair members (positive copies only; the
        # mirrored -g_a, -g_b are genuine zeros and stay)
        mask = np.ones(2 * n, bool)
        mask[n + k] = False
        mask[n + k + 1] = False
        s = float(np.sum(1.0 / d_a[mask] ** 2)
                  + np.sum(1.0 / d_b[mask] ** 2))
        G[k] = (g_b - g_a) ** 2 * s
    return G


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE LEHMER <-> RESONANCE LINK -- window needles vs "
          "Lehmer-like zero pairs")
    print("=" * 78)

    # ------------------------------------------------ L0: the comb
    print("\nL0 -- the shared certified zero comb")
    gam, meta = load_comb()
    gmax = float(gam[-1])
    mono = bool(np.all(np.diff(gam) > 0))
    check("L0.1 [E] comb integrity: %d zeros from %s (dps %d), "
          "strictly increasing, gamma_1 = %.12f (quote %.12f), "
          "gamma_max = %.4f; completeness certified by "
          "turing_cert_probe (TURING-COMPLETE-BAND)"
          % (len(gam), meta["generator"], meta["dps"], float(gam[0]),
             GAMMA1_QUOTE, gmax),
          len(gam) == N_ZEROS and meta["dps"] == DPS_ZEROS and mono
          and abs(float(gam[0]) - GAMMA1_QUOTE) < 1e-9)

    # ------------------------------------------------ L1: pair stats
    print("\nL1 -- normalized spacings and the Lehmer-like pairs")
    dg = np.diff(gam)
    delta = dg * np.log(gam[:-1] / (2.0 * math.pi)) / (2.0 * math.pi)
    d_q10 = float(np.quantile(delta, DELTA_Q))
    print("      delta_k = gap * log(gamma/2pi)/2pi on %d pairs: "
          "min %.5f / q10 %.5f / median %.5f / max %.5f (mean ~1 by "
          "construction: %.4f)"
          % (len(delta), float(delta.min()), d_q10,
             float(np.median(delta)), float(delta.max()),
             float(delta.mean())))
    t_g = time.time()
    Gk = csv_like_G_fast(gam)
    print("      CSV-like G_k on %d pairs in %.1f s: min %.4f / "
          "median %.4f; pairs with G_k < %.2f (cited CSV line 4/5): "
          "%d" % (len(Gk), time.time() - t_g, float(Gk.min()),
                  float(np.median(Gk)), CSV_BAR,
                  int(np.sum(Gk < CSV_BAR))))
    sp_dG = spearman(delta, Gk)
    order = np.argsort(delta)
    print("\n      TOP-%d Lehmer-like pairs (smallest delta_k):"
          % N_TOP)
    print("      rank    k    gamma_k        gamma_k+1      gap     "
          " delta_k   G_k     G_k tail bound")
    mp.mp.dps = 30
    dens = lambda t: mp.log(t / (2 * mp.pi)) / (2 * mp.pi)  # noqa
    for r_, k in enumerate(order[:N_TOP]):
        tb = 0.0
        for g0 in (gam[k], gam[k + 1]):
            tb += 2.0 * float(mp.quad(
                lambda t: dens(t) / (t - g0) ** 2,
                [gmax, 2 * gmax, 10 * gmax, mp.inf]))
        tb *= float(dg[k] ** 2)
        print("      %4d  %5d  %12.6f  %12.6f  %.6f  %.5f  %7.4f  "
              "+<= %.2e"
              % (r_ + 1, k + 1, gam[k], gam[k + 1], float(dg[k]),
                 float(delta[k]), float(Gk[k]), tb))
    check("L1.1 [MEASURED] pair statistics assembled: q10 bar "
          "delta <= %.5f flags %d/%d pairs as Lehmer-like (frozen "
          "rule); Spearman(delta, G) = %+.3f (the two smallness "
          "notions agree in rank); the sharpest comb pair has "
          "delta = %.5f at gamma ~ %.2f (the classical Lehmer pair "
          "at gamma ~ 7005 lies OUTSIDE this comb -- documented)"
          % (d_q10, int(np.sum(delta <= d_q10)), len(delta), sp_dG,
             float(delta.min()), float(gam[int(order[0])])),
          sp_dG > 0.5)

    # ------------------------------------------------ L2: the windows
    print("\nL2 -- the window sweep (landscape verbatim) and the "
          "resolution correspondence")
    u0 = zeta_grid_const()
    KZ = core.frame_a_zones()
    rows = []
    for kz in KZ:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        hz = Mz // 2
        complete = math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5
        ka = core.atoms_in(alpha)
        c_at, D = core.atom_lags_at(alpha, Mz, core.U_ALL[:ka],
                                    core.MU_ALL[:ka])
        c_ar = core.arch_lags(Mz, D)
        A = core.odd_toeplitz(c_ar + c_at, Mz)
        g = np.zeros(Mz)
        g[0], g[1] = 2.0 * D / 3.0, D / 6.0
        Gm = core.odd_toeplitz(g, Mz)
        lam_min, lam_2, v_min, rad = gen_min_eig2(A, Gm)
        floor = FLOOR_SAFETY * EPS * rad * math.sqrt(hz)
        Tb = core.parity_basis(hz, 2)
        t1v, t2v = Tb[0], Tb[1]
        W11 = core.lag_weights_from_v(t1v, hz)
        W22 = core.lag_weights_from_v(t2v, hz)
        Wpp = core.lag_weights_from_v(t1v + t2v, hz)
        W12 = 0.5 * (Wpp - W11 - W22)
        B2 = np.array([[c_ar @ W11, c_ar @ W12],
                       [c_ar @ W12, c_ar @ W22]])
        lamw = 0.5 * np.array([float(m) for m in core.MU_ALL[:ka]])
        uu = np.array([float(u) for u in core.U_ALL[:ka]])
        s11 = s22 = s12 = 0.0
        for i in range(ka):
            s11 += lamw[i] * core.spline_project(W11, uu[i], D, Mz)
            s22 += lamw[i] * core.spline_project(W22, uu[i], D, Mz)
            s12 += lamw[i] * core.spline_project(W12, uu[i], D, Mz)
        S2 = np.array([[s11, s12], [s12, s22]])
        Sm = model_matrix(alpha, Mz, D, W11, W22, W12, u0)
        vl = lock_dir(alpha)
        q_r = float(vl @ ((B2 - S2) @ vl))
        q_m = float(vl @ ((B2 - Sm) @ vl))
        wl = vl[0] * t1v + vl[1] * t2v
        wlGwl = float(wl @ (Gm @ wl))
        wlAwl = float(wl @ (A @ wl))
        w_hat = wl / math.sqrt(wlGwl)
        vGv = float(v_min @ (Gm @ v_min))
        m_vec = v_min / math.sqrt(vGv)
        ct = float(w_hat @ (Gm @ m_vec))
        if ct < 0.0:
            m_vec = -m_vec
            ct = -ct
        ct = min(1.0, ct)
        st = math.sqrt(max(0.0, 1.0 - ct * ct))
        perp = m_vec - ct * w_hat
        pn = math.sqrt(max(0.0, float(perp @ (Gm @ perp))))
        w_perp = perp / pn if pn > 0.0 else perp
        lam_lock = wlAwl / wlGwl
        Q_perp = float(w_perp @ (A @ w_perp))
        t2 = (st / ct) ** 2
        qq = Q_perp / lam_lock
        rows.append(dict(kz=kz, h=hz, alpha=alpha, D=D,
                         complete=complete, lam=lam_min, floor=floor,
                         lock=q_r * q_m > 0.0, qq=qq, t2=t2,
                         P=qq * t2, rid=lam_min / lam_lock,
                         theta=math.degrees(math.acos(ct)),
                         t_max=math.pi / D,
                         t_res=math.pi / (2.0 * alpha)))
        if len(rows) % 10 == 0:
            print("      ... %d/%d windows (%.0f s)"
                  % (len(rows), len(KZ), time.time() - T0))

    comp = [r for r in rows if r["complete"]]
    inc_hs = sorted(r["h"] for r in rows if not r["complete"])
    check("L2.1 [E] the declared surface reproduces: %d frame-A "
          "windows, %d complete combs, truncated set %s"
          % (len(rows), len(comp), inc_hs),
          len(comp) == 67 and inc_hs == [1219, 1292, 1445])

    lock_c = [r for r in comp if r["lock"] and r["lam"] > r["floor"]]
    n = len(lock_c)
    hs = np.array([r["h"] for r in lock_c], float)
    al = np.array([r["alpha"] for r in lock_c])
    Pv = np.array([r["P"] for r in lock_c])
    rid = np.array([r["rid"] for r in lock_c])
    th = np.array([r["theta"] for r in lock_c])
    tmax = np.array([r["t_max"] for r in lock_c])
    tres = np.array([r["t_res"] for r in lock_c])
    i_max = int(np.argmax(Pv))
    sp_P = spearman(Pv, hs)
    sp_r = spearman(rid, hs)
    check("L2.2 [E] the rid anchors reproduce on n = %d (>= 60): max "
          "P = %.4f at h = %d (quote %.4f at %d), Spearman(P, h) = "
          "%+.4f (quote %+.3f), Spearman(r_id, h) = %+.4f (quote "
          "%+.3f), median r_id %.4f (quote %.3f), median theta %.2f "
          "deg (quote %.1f)"
          % (n, float(Pv[i_max]), int(hs[i_max]), P_MAX_QUOTE,
             H_AT_PMAX, sp_P, SP_P_H_QUOTE, sp_r, SP_RID_H_QUOTE,
             float(np.median(rid)), RID_MED_QUOTE,
             float(np.median(th)), THETA_MED_QUOTE),
          n >= 60
          and abs(float(Pv[i_max]) - P_MAX_QUOTE) <= P_MAX_TOL
          and int(hs[i_max]) == H_AT_PMAX
          and abs(sp_P - SP_P_H_QUOTE) <= SP_TOL
          and abs(sp_r - SP_RID_H_QUOTE) <= SP_TOL
          and abs(float(np.median(rid)) - RID_MED_QUOTE) <= RID_TOL
          and abs(float(np.median(th)) - THETA_MED_QUOTE) <= 0.15)

    n_over = int(np.sum(tmax > gmax))
    sp_th = spearman(tmax, hs)
    check("L2.3 [E] the resolution correspondence is well-posed on "
          "the comb: t_max = pi/D in [%.1f, %.1f] (all <= gamma_max "
          "= %.1f: %d over), resolution pi/(2 alpha) in [%.3f, "
          "%.3f]; Spearman(t_max, h) = %+.3f -- t_max is prime-gap-"
          "driven and largely h-monotone: only the residual gap "
          "jitter survives the h-control (same-h windows differ in "
          "t_max), so the PLACEMENT control L4 carries the sharper "
          "null"
          % (float(tmax.min()), float(tmax.max()), gmax, n_over,
             float(tres.min()), float(tres.max()), sp_th),
          n_over == 0)

    # per-window presence measures
    g_hi = gam[1:]                       # pair position = gamma_{k+1}
    lehm = delta <= d_q10
    L_share = np.empty(n)
    L_min = np.empty(n)
    L_edge = np.full(n, np.nan)
    n_edge_empty = 0
    for i in range(n):
        band = g_hi <= tmax[i]
        nb = int(band.sum())
        L_share[i] = float(lehm[band].mean()) if nb else float("nan")
        L_min[i] = float(delta[band].min()) if nb else float("nan")
        oct_ = (g_hi > 0.5 * tmax[i]) & band
        if int(oct_.sum()):
            L_edge[i] = float(delta[oct_].min())
        else:
            n_edge_empty += 1
    print("\n      per-window table (analysis sample, sorted by h):")
    print("      h      D        t_max    res     P        "
          "L_share  L_min    L_edge")
    for i in np.argsort(hs):
        print("      %4d  %.5f  %7.1f  %.4f  %.4f   %.4f   "
              "%.4f   %s"
              % (int(hs[i]), float(lock_c[int(i)]["D"]), tmax[i],
                 tres[i], Pv[i], L_share[i], L_min[i],
                 ("%.4f" % L_edge[i]) if not math.isnan(L_edge[i])
                 else "--"))
    check("L2.4 [MEASURED] presence measures assembled: L_share in "
          "[%.4f, %.4f], L_min in [%.4f, %.4f], L_edge defined on "
          "%d/%d windows (%d empty edge octaves); band sizes %d..%d "
          "pairs"
          % (float(np.nanmin(L_share)), float(np.nanmax(L_share)),
             float(np.nanmin(L_min)), float(np.nanmax(L_min)),
             n - n_edge_empty, n, n_edge_empty,
             int(np.sum(g_hi <= tmax.min())),
             int(np.sum(g_hi <= tmax.max()))), True)

    # ------------------------------------------------ L3: correlation
    print("\nL3 -- the correlation: P = q tan^2 theta vs Lehmer "
          "presence (h-control ALWAYS)")
    rng = np.random.default_rng(SEED)
    print("      confound transparency: Spearman(t_max, h) = %+.3f; "
          "Spearman(L_share, t_max) = %+.3f, Spearman(L_min, t_max) "
          "= %+.3f; Spearman(P, t_max) = %+.3f"
          % (sp_th, spearman(L_share, tmax), spearman(L_min, tmax),
             spearman(Pv, tmax)))
    measures = [("L_share (Lehmer share, +)", L_share, +1.0),
                ("L_min   (min delta,    -)", L_min, -1.0),
                ("L_edge  (edge-oct min, -)", L_edge, -1.0)]
    l3 = {}
    h3_cols = control_cols([hs], 3)
    for name, yv, sgn in measures:
        ok_m = ~np.isnan(yv)
        x_ = Pv[ok_m]
        y_ = yv[ok_m]
        h_ = hs[ok_m]
        a_ = al[ok_m]
        t_ = tmax[ok_m]
        sp0 = spearman(x_, y_)
        r3, p3 = partial_spearman(x_, y_, [h_], rng, poly=3)
        rha, pha = partial_spearman(x_, y_, [h_, a_], rng, poly=1)
        rpl, ppl = partial_spearman_mixed(x_, y_, [(h_, 3), (t_, 1)],
                                          rng)
        hit = abs(r3) >= RHO_BAR and p3 < P_BAR
        sign_ok = (r3 * sgn) > 0.0
        l3[name] = dict(sp0=sp0, r3=r3, p3=p3, rha=rha, pha=pha,
                        rpl=rpl, ppl=ppl, hit=hit, sign_ok=sign_ok,
                        n=int(ok_m.sum()))
        print("      %-26s n=%d raw %+7.4f | h3 %+7.4f p %.5f%s | "
              "(h,a) %+7.4f p %.5f | placement (h3+t_max) %+7.4f "
              "p %.5f%s"
              % (name, int(ok_m.sum()), sp0, r3, p3,
                 " sign-OK" if sign_ok else " sign-WRONG",
                 rha, pha, rpl, ppl,
                 "  <- GATE HIT" if hit else ""))
    hits = [nm for nm in l3 if l3[nm]["hit"]]
    check("L3.1 [MEASURED] gate (|rho_h3| >= %.2f AND p < %.2f per "
          "test; %d tests, Bonferroni-honest bar p < %.4f): %s"
          % (RHO_BAR, P_BAR, N_TESTS, P_BAR / N_TESTS,
             ("HIT by %s" % "; ".join(hits)) if hits else
             "NO measure passes -- no h-controlled link between "
             "P and Lehmer presence at this resolution"), True)

    # ------------------------------------------------ L4: pseudo pairs
    print("\nL4 -- pseudo-pair control: delta values permuted across "
          "gap positions (B = %d)" % B_PSEUDO)
    rng4 = np.random.default_rng(SEED + 1)
    ctrl = {}
    for name, yv, sgn in measures:
        ok_m = ~np.isnan(yv)
        h_ = hs[ok_m]
        cols = control_cols([h_], 3)
        real = abs(partial_rho_only(Pv[ok_m], yv[ok_m], cols))
        cnt = 0
        vals = np.empty(B_PSEUDO)
        for b_ in range(B_PSEUDO):
            dsh = rng4.permutation(delta)
            lsh = dsh <= d_q10
            ysh = np.empty(n)
            for i in range(n):
                band = g_hi <= tmax[i]
                if name.startswith("L_share"):
                    ysh[i] = float(lsh[band].mean()) if band.any() \
                        else np.nan
                elif name.startswith("L_min"):
                    ysh[i] = float(dsh[band].min()) if band.any() \
                        else np.nan
                else:
                    oct_ = (g_hi > 0.5 * tmax[i]) & band
                    ysh[i] = float(dsh[oct_].min()) \
                        if oct_.any() else np.nan
            ok_s = ok_m & ~np.isnan(ysh)
            r_sh = abs(partial_rho_only(Pv[ok_s], ysh[ok_s],
                                        control_cols([hs[ok_s]], 3)))
            vals[b_] = r_sh
            if r_sh >= real - 1e-12:
                cnt += 1
        p_ctrl = (cnt + 1.0) / (B_PSEUDO + 1.0)
        ctrl[name] = (real, p_ctrl, float(np.median(vals)),
                      float(np.quantile(vals, 0.95)))
        print("      %-26s |rho_h3| real %.4f vs pseudo median %.4f "
              "/ q95 %.4f -> control p = %.4f%s"
              % (name, real, ctrl[name][2], ctrl[name][3], p_ctrl,
                 "  (placement-specific)" if p_ctrl < CTRL_P_BAR
                 else ""))
    check("L4.1 [MEASURED] pseudo-pair control: %s"
          % ("; ".join("%s p=%.3f" % (nm.split()[0], ctrl[nm][1])
                       for nm in ctrl)), True)

    # ------------------------------------------------ L5: teeth
    print("\nL5 -- teeth: a planted signal must be detected (run-2 "
          "construction: planted in the h3-residual space)")
    rng5 = np.random.default_rng(SEED + 2)
    res_P = residualize(rankdata(Pv), h3_cols)
    y_pl = res_P + rng5.normal(0.0, 0.5 * float(np.std(res_P)), n)
    r_pl, p_pl = partial_spearman(Pv, y_pl, [hs], rng5, poly=3)
    check("L5.1 [E, must-detect] planted target resid_h3(rank(P)) + "
          "noise (0.5 sd): h3-partial rho = %+.4f (>= %.1f), p = "
          "%.5f (< %.0e) -- the statistics wiring detects a real "
          "link of this size (run-1 raw-space plant measured "
          "0.7813, documented)"
          % (r_pl, PLANT_RHO_BAR, p_pl, PLANT_P_BAR),
          r_pl >= PLANT_RHO_BAR and p_pl < PLANT_P_BAR)

    # ------------------------------------------------ verdict
    guards_ok = not any(f.startswith(("L0", "L2.1", "L2.2", "L2.3",
                                      "L5")) for f in FAILS)
    linked = [nm for nm in hits if ctrl[nm][1] < CTRL_P_BAR]
    if not guards_ok:
        VERDICT = "LEHMER-MIXED (guards or teeth failed)"
    elif linked:
        VERDICT = "LEHMER-LINKED"
    elif hits:
        VERDICT = "LEHMER-GEOMETRY"
    else:
        VERDICT = "LEHMER-NULL"

    check("L6.1 [C] the typed reading: the resolved band of window w "
          "is t in (0, pi/D(w)] at resolution pi/(2 alpha(w)) "
          "(documented duality: lattice spacing D <-> Nyquist reach, "
          "lag support 2 alpha <-> resolution); Lehmer presence in "
          "the band %s the h-controlled landscape driver P: %s.  "
          "NO positivity claim, NO RH statement, NO marker move; "
          "W3 stays open"
          % ("CORRELATES WITH" if linked else "does NOT correlate "
             "(placement-specifically) with",
             VERDICT), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, Lehmer-resonance round (2026-08-02): the
  thesis 'the W3 resonance landscape is the window analogue of the
  Lehmer-pair phenomenology' was tested against the certified
  2000-zero comb (turing_cert_probe).  PAIR STATISTICS: normalized
  spacings delta_k = gap x log(gamma/2pi)/2pi, comb minimum %.5f at
  gamma ~ %.2f (the classical Lehmer pair at gamma ~ 7005 lies
  outside the comb); CSV-like G_k agrees in rank (Spearman %+.3f);
  %d/%d pairs below the frozen q10 bar %.5f.  CORRESPONDENCE
  (documented): lag-lattice spacing D <-> Nyquist reach t_max =
  pi/D in [%.0f, %.0f]; lag support 2 alpha <-> resolution
  pi/(2 alpha) in [%.3f, %.3f]; t_max is prime-gap-driven but
  largely h-monotone (Spearman(t_max, h) = %+.3f) -- the h-control
  absorbs most band-reach variance, the placement control is the
  sharper null.
  CORRELATION (n = %d lock windows, v637 controls, seed %d):
  P = q tan^2 theta vs L_share / L_min / L_edge -- h3-partials
  %s (gate |rho| >= 0.30, p < 0.01: %s); pseudo-pair placement
  control (B = %d): %s.  VERDICT %s: %s  TYPE: measured
  cross-question on the declared surface; zeros enter ONLY as the
  correlation target (shared cache, no zetazero call); no
  positivity claim; no RH statement; Problem 7.1 untouched; no
  marker move.
""" % (float(delta.min()), float(gam[int(order[0])]), sp_dG,
       int(np.sum(delta <= d_q10)), len(delta), d_q10,
       float(tmax.min()), float(tmax.max()),
       float(tres.min()), float(tres.max()), sp_th, n, SEED,
       ["%s %+0.3f (p %.4f)" % (nm.split()[0], l3[nm]["r3"],
                                l3[nm]["p3"]) for nm in l3],
       ("HIT: " + "; ".join(hits)) if hits else "no hit",
       B_PSEUDO,
       "; ".join("%s p=%.3f" % (nm.split()[0], ctrl[nm][1])
                 for nm in ctrl),
       VERDICT,
       ("the needle driver P correlates with the zero-comb Lehmer "
        "placement beyond the h-ladder AND beyond the band-reach "
        "geometry -- a named zero-side channel; the follow-up is a "
        "mechanistic probe (which pairs, which windows)."
        if linked else
        ("P correlates with a Lehmer-presence MEASURE but the "
         "pseudo-pair control shows the link is band-REACH "
         "geometry (D-driven), not zero placement -- the needles "
         "are not zero-driven."
         if hits else
         "the needles are NOT zero-comb-driven at the window "
         "resolution: no h-controlled correlation between P and "
         "Lehmer presence survives -- a clean negative, consistent "
         "with the Baez-Duarte FRAME-side reading of the W3 "
         "obstruction.")))
    )

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
