"""PRIME.EXCLUSIONLADDER.03 -- deciding the Xi_eff flattening signal
(EXPLORATION ONLY).

PARENT: exclusion_ladder_deep_probe.py (2026-08-06, LADDER-EXTENDED,
26/26): rungs to X = 22.09375 (4e9 comb) with rigorous certificates;
Xi_eff = X median delta_mb fell 0.639 -> 0.457 -> 0.274 -> 0.218 ->
0.219 on the extended grid -- FLAT between the last two rungs
(+0.4%) after the strong decline.  THIS PROBE (user-authorized):
extend to the deciding rungs and adjudicate saturation vs
continuation with FROZEN gates.

TASK STRUCTURE (all bars predeclared, frozen before running):
 S0 FIREWALL + BENCHMARK + CAP DECISION: same segmented sieve +
    bincount tent assembly (deployed T115 convention; parity ward at
    the overlap rung M = 1176 vs the deployed core.atom_lags_at path:
    atom count EXACT, max|dc| <= 5e-9); FFT matvec ward <= 1e-9.
    PREDECLARED CAP RULE (safety x1.5, far extrapolation): target
    rung M = 1503 (X = 23.484375, comb cap e^X = 1.582e10 <= 1.6e10)
    iff t_proj <= 600 s; stretch rung M = 1588 (X = 24.8125, e^X =
    5.977e10 <= 6e10) iff t_proj <= 1200 s; segments 2^28 ascending
    (the far pass), 2^25 reversed for the order ward at M = 1503.
 S1 TOWER: baselines 256/640/1176 on the parent paths (anchors
    5.29e-5 / 1.18e-5 / 3.9e-6, v780 3.882e-6, rel 2e-2); rungs
    1326/1414 rebuilt in the same big pass and anchored against the
    parent run-1 margins 2.4453e-6 / 2.0092e-6 (rel 2e-2); NEW rungs
    1503/1588; summation-order ward at M = 1503 (margin must survive
    sum|dc|); deeper-rung order noise typed by e^{dX/2} scaling.
 S2 CERTIFICATES on ALL rungs (Cholesky PD lower bound via the
    Higham backward-error bound; Rayleigh-residual enclosure); new
    margins gated against the 5-anchor extrapolated decline (ratio
    in (0.2, 5); outside or <= 0 => anomaly typed prominently, the
    verdict then RUNG-LIMITED with the anomaly named -- the frozen
    enum here has no SURPRISE class); W2 packet ward at new rungs.
 S3 THE SATURATION DECISION (frozen gates, SAME instrument as the
    parent: extended grid geomspace(1/240, 1/2, 44) + 3-step
    bisection; INSTRUMENT CONTINUITY WARD: the re-measured Xi_eff at
    X = 20.719 / 22.094 must reproduce the parent 0.2179 / 0.2187
    within rel 2e-2, else the gates are void):
      GATE S1 (priority 1): log-log slope of Xi_eff over the LAST
        THREE rungs <= -0.3  =>  SHARPENING-CONTINUES (recalibrated
        exponent reported).
      GATE S2 (priority 2): |Xi_eff/0.2187 - 1| <= 0.05 on >= 2 new
        rungs  =>  SATURATION-TYPED (mechanism tests S4 binding).
      NEITHER: RUNG-LIMITED typed exactly as 'decision zone between
        the frozen gates' (slope printed) -- not a compute wall.
    Frozen-grid census + monotone ward at the new rungs (loss <= 2%
    vs M = 1414); on-ordinate family at the deepest rung (report).
 S4 MECHANISM LOCALIZATION (computed regardless; BINDING only if
    gate S2 fires; predeclared classifiers):
    (a) SUPPORT TEST at the deepest rung: delta_mb(f) for f in
        (0.6, 0.75, 0.875, 1.0) at 6 sampled gammas; support slope
        s_f = d ln delta_mb / d ln f near f = 1 (median over the
        0.875 -> 1.0 leg); SUPPORT-ACTIVE iff s_f <= -0.3.
    (b) GRID TEST: refined instrument geomspace(1/960, 1/2, 88) +
        5-step bisection over the last three rungs; GRID-LIMITED iff
        the refined slope <= -0.3 while the base instrument stalls
        (this also un-censors the low-gamma rows that the parent
        flagged as floored at 1/240).
    (c) PER-GAMMA CENSUS + BATTERY TREND: per-gamma log-slope of
        delta_mb across the last three rungs at the 6 sampled gammas
        (where does the stall live); rank-12 detuned battery gain at
        the new rungs vs the parent's 19.3% at X = 22.09 (gain >
        30% typed as a battery-limited component, report).
    TYPING ORDER (if S2): GRID-LIMITED else (SUPPORT-ACTIVE =>
    'support-active but X-stalled, mixed/unresolved') else
    INTRINSIC-WIDTH (the rank-4 battery carries an X-independent
    sensitivity floor -- reported prominently).
 S5 THE HONEST LAW: fit-free Xi_eff(X) series with per-step ratios
    across all 7 rungs, the mechanism named, and the updated
    depth-to-width table X*(delta) from the deepest calibration.
CONTROLS: C1a synthetic quadruple at 2 delta_mb inside the deepest
 new region must break the margin (full eigensolve, >= 3 points);
 C2 scramble at M = 1503 (uniform positions, SAME masses, declared
 seed 7 -- the only RNG use) must destroy PSD; C3 Epstein swap
 (Lambda_E table reach 34000 => control at M = 640, typed) must
 destroy PSD.
VERDICT (frozen enum): SHARPENING-CONTINUES / SATURATION-TYPED /
 RUNG-LIMITED (typed exactly: compute wall, anomaly, or decision
 zone).

FIREWALL: v563/v755 read-only; NO zetazero()/nzeros() calls (AST-
checked); cached RvM ordinate list for wards/on-line side only; RNG
only in the declared C2 scramble.  Nothing outside experiments/
touched.  NO RH claim.
"""
import ast
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v755_simpler_schur_recursion as srp     # noqa: E402 (READ-ONLY)
import epstein_firewall_probe as epx           # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
DGRID = 1.0 / 64.0
RUNGS_BASE = ((256, 5.29e-5), (640, 1.18e-5), (1176, 3.9e-6))
V780_DEEP = 3.882e-6
ANCH_1326, ANCH_1414 = 2.4453e-6, 2.0092e-6    # parent run-1 margins
ANCH_REL = 2.0e-2
ATOM_MAX_DEEP = 100000000
M_PREV = (1326, 1414)
M_TARGET, M_STRETCH = 1503, 1588   # X = 23.484375 / 24.8125
SEG_ASC, SEG_DESC = 1 << 28, 1 << 25
T_TARGET_BAR, T_STRETCH_BAR = 600.0, 1200.0
PROJ_SAFETY = 1.5
PARITY_C_ABS = 5.0e-9
FFT_WARD_BAR = 1.0e-9
GAMMAS_GRID = np.geomspace(2.0, 190.0, 36)      # frozen (parent)
DELTAS_GRID = np.linspace(1.0 / 60.0, 0.5, 30)  # frozen (parent)
EXT_DELTAS = np.geomspace(1.0 / 240.0, 0.5, 44)   # base instrument
N_BISECT = 3
REF_DELTAS = np.geomspace(1.0 / 960.0, 0.5, 88)   # refined instrument
N_BISECT_REF = 5
XI_1326_CITED, XI_1414_CITED = 0.2179, 0.2187   # parent, base instr.
XI_INSTR_REL = 2.0e-2                            # continuity ward
GATE_SLOPE = -0.3                                # S1 (priority 1)
GATE_BAND = 0.05                                 # S2 (priority 2)
SUP_FS = (0.6, 0.75, 0.875, 1.0)
SUP_SLOPE_BAR = -0.3
ENRICH_CITED = 0.193                             # parent rank-12 gain
ENRICH_BATT_BAR = 0.30
SURP_DECL_LO, SURP_DECL_HI = 0.2, 5.0
MONO_TOL = 0.02
IDENT_BUD = 1.0e-8
W0_BAR, WQ_BAR, W2_SLACK = 1.0e-12, 1.0e-8, 3.0
A2A, A2B, A2C = 0.1038, 0.2573, 9.3675
W2_PACKETS = (30.0, 50.0, 80.0)
U_RND = 0.5 * np.finfo(float).eps
CERT_INFL = 1.01
BATT_GIDX = (3, 10, 17, 24, 30, 35)
MZ_GIDX = (6, 14, 22, 30)
SEED_SCRAMBLE = 7
N_ONZERO = 30


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
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in ("zetazero", "nzeros", "find_zeros"):
                return False
    return True


# ---------------------------------------------------- parent conventions
def quad_lags(M, gamma, delta):
    z1, z2 = complex(delta, gamma), complex(-delta, gamma)
    t = np.abs(np.arange(-1, M + 1)) * DGRID
    g = 2.0 * (np.exp(z1 * t) / z1 ** 2 + np.exp(z2 * t) / z2 ** 2).real
    return (g[:-2] - 2.0 * g[1:-1] + g[2:]) / DGRID


def a_weight(g):
    x = g * DGRID / 2.0
    return DGRID * (np.sin(x) / x) ** 2


def n_upper(t):
    return (t / (2.0 * math.pi) * math.log(t / (2.0 * math.pi * math.e))
            + A2A * math.log(t) + A2B * math.log(math.log(t)) + A2C)


def tail_budget(x, gamma_top, n_cached):
    jj = np.arange(len(x)) * DGRID
    band = np.linspace(0.0, 2.0 * math.pi / DGRID, 4096)
    Xb = np.abs(np.exp(1j * np.outer(band, jj)) @ x)
    x2max = float(np.max(Xb) ** 2)
    tt = np.geomspace(gamma_top, 1.0e9, 4000)
    integ = np.trapezoid(
        16.0 / (DGRID * tt ** 3)
        * np.array([n_upper(t) - n_cached for t in tt]), tt)
    return x2max * (integ + 16.0 / (DGRID * 1.0e9)
                    * n_upper(1.0e9) / 2.0)


# ------------------------------------------- segmented sieve + tent reads
def base_primes(n):
    sv = np.ones(n + 1, dtype=bool)
    sv[:2] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if sv[i]:
            sv[i * i::i] = False
    return np.flatnonzero(sv)


def tent_accumulate(c, M, u, mu, chunk=4000000):
    for s in range(0, u.size, chunk):
        uu, mm = u[s:s + chunk], mu[s:s + chunk]
        i0 = np.floor(uu / DGRID).astype(np.int64)
        for off in (-2, -1, 0, 1, 2):
            idx = i0 + off
            ok = (idx >= 0) & (idx < M)
            if not ok.any():
                continue
            v = 1.0 - np.abs(idx[ok] * DGRID - uu[ok]) / DGRID
            pos = v > 0.0
            if pos.any():
                c -= np.bincount(idx[ok][pos],
                                 weights=mm[ok][pos] * 0.5 * v[pos],
                                 minlength=M)
        refl = uu < DGRID
        if refl.any():
            v = 1.0 - uu[refl] / DGRID
            pos = v > 0.0
            if pos.any():
                c[0] -= float(np.sum(mm[refl][pos] * 0.5 * v[pos]))


def nmax_of_M(M):
    return int(math.floor(math.exp(M * DGRID + 1.0e-14)))


def seg_assemble(Ms, collect_mass_M=None, seg=SEG_ASC, reverse=False):
    Ms = sorted(Ms)
    ncap = {M: nmax_of_M(M) for M in Ms}
    nmax = max(ncap.values())
    cs = {M: np.zeros(M) for M in Ms}
    cnt = {M: 0 for M in Ms}
    mass_cap = ncap[collect_mass_M] if collect_mass_M else None
    masses = [] if mass_cap else None
    bp = base_primes(int(math.isqrt(nmax)))
    los = list(range(0, nmax + 1, seg))
    if reverse:
        los = los[::-1]
    for lo in los:
        hi = min(lo + seg, nmax + 1)
        sv = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            sv[:2] = False
        for p in bp:
            p = int(p)
            st = max(p * p, ((lo + p - 1) // p) * p)
            if st < hi:
                sv[st - lo::p] = False
        nn = np.flatnonzero(sv).astype(np.float64) + float(lo)
        if nn.size == 0:
            continue
        lg = np.log(nn)
        mu = 2.0 * lg / np.sqrt(nn)
        for M in Ms:
            if ncap[M] >= hi - 1:
                tent_accumulate(cs[M], M, lg, mu)
                cnt[M] += int(nn.size)
            else:
                sel = nn <= ncap[M]
                if sel.any():
                    tent_accumulate(cs[M], M, lg[sel], mu[sel])
                    cnt[M] += int(sel.sum())
        if masses is not None:
            masses.append(mu[nn <= mass_cap].copy())
    for p in bp:
        p = int(p)
        lp = math.log(p)
        q = p * p
        while q <= nmax:
            u1 = np.array([math.log(q)])
            m1 = np.array([2.0 * lp / math.sqrt(q)])
            for M in Ms:
                if q <= ncap[M]:
                    tent_accumulate(cs[M], M, u1, m1)
                    cnt[M] += 1
            if masses is not None and q <= mass_cap:
                masses.append(m1.copy())
            q *= p
    return cs, cnt, (np.concatenate(masses) if masses is not None
                     else None), ncap


# ------------------------------------------------- battery + subspace min
def battery_B(M, gamma, delta, support=1.0, detunes=(0.0,)):
    jj = np.arange(M) * DGRID
    msk = (jj <= support * M * DGRID).astype(float)
    cols = []
    for dg in detunes:
        g = gamma + dg
        for sgn in (delta, -delta):
            e = np.exp(sgn * jj) * msk
            cols.append(e * np.cos(g * jj))
            cols.append(e * np.sin(g * jj))
    return np.stack(cols, axis=1)


def sub_lam(cA, Qb):
    Y = sla.matmul_toeplitz((cA, cA), Qb, check_finite=False)
    S = Qb.T @ Y
    S = 0.5 * (S + S.T)
    w, V = np.linalg.eigh(S)
    return float(w[0]), Qb @ V[:, 0]


def bud_of(M, nrmT, ql_max):
    return IDENT_BUD + 100.0 * np.finfo(float).eps * (nrmT + M * ql_max)


def boundary_scan(cT, M, nrmT, g, grid, sign, bisect=0,
                  support=1.0, detunes=(0.0,)):
    prev = None
    for dl in grid:
        dl = float(dl)
        ql = quad_lags(M, g, dl)[:M]
        Qb, _ = np.linalg.qr(battery_B(M, g, dl, support, detunes))
        bud = bud_of(M, nrmT, float(np.max(np.abs(ql))))
        lam, wit = sub_lam(cT + sign * ql, Qb)
        if lam < -bud:
            hit, w_hit, b_hit, lo = dl, wit, bud, prev
            for _ in range(bisect):
                if lo is None:
                    break
                mid = math.sqrt(lo * hit)
                qlm = quad_lags(M, g, mid)[:M]
                Qbm, _ = np.linalg.qr(battery_B(M, g, mid,
                                                support, detunes))
                bm = bud_of(M, nrmT, float(np.max(np.abs(qlm))))
                lm, wm = sub_lam(cT + sign * qlm, Qbm)
                if lm < -bm:
                    hit, w_hit, b_hit = mid, wm, bm
                else:
                    lo = mid
            return hit, w_hit, b_hit
        prev = dl
    return float("nan"), None, float("nan")


def census_maps(cT, M, nrmT):
    exc = np.zeros((len(GAMMAS_GRID), len(DELTAS_GRID)), bool)
    mbk = np.zeros_like(exc)
    for ig, g in enumerate(GAMMAS_GRID):
        for idl, dl in enumerate(DELTAS_GRID):
            ql = quad_lags(M, float(g), float(dl))[:M]
            Qb, _ = np.linalg.qr(battery_B(M, float(g), float(dl)))
            bud = bud_of(M, nrmT, float(np.max(np.abs(ql))))
            lm, _ = sub_lam(cT - ql, Qb)
            lp, _ = sub_lam(cT + ql, Qb)
            exc[ig, idl] = lm < -bud
            mbk[ig, idl] = lp < -bud
    return exc, mbk


def full_min(cA, M):
    return float(sla.eigvalsh(sla.toeplitz(cA),
                              subset_by_index=[0, 0])[0])


# --------------------------------------------------------- certificates
def gamma_fl(n):
    t = n * U_RND
    return t / (1.0 - t)


def chol_cert_lower(T, lam_hat):
    M = T.shape[0]
    for frac in (0.9, 0.5, 0.25, 0.1):
        beta = frac * lam_hat
        A = T.copy()
        A[np.diag_indices(M)] -= beta
        try:
            L = np.linalg.cholesky(A)
        except np.linalg.LinAlgError:
            continue
        aL = np.abs(L)
        w = float(np.max(aL @ aL.sum(axis=0))) * CERT_INFL
        slack = gamma_fl(M + 1) * w
        e_diag = U_RND * float(np.max(np.abs(np.diag(A)))) \
            + U_RND * abs(beta)
        return beta - slack - e_diag, beta, slack + e_diag
    return None, None, None


def rayleigh_enclosure(T):
    M = T.shape[0]
    _w, v = sla.eigh(T, subset_by_index=[0, 0])
    v = v[:, 0] / np.linalg.norm(v[:, 0])
    y = T @ v
    aTv = np.abs(T) @ np.abs(v)
    rho = float(v @ y)
    e_rho = gamma_fl(M) * (float(np.abs(v) @ aTv)
                           + abs(rho)) * CERT_INFL
    r = float(np.linalg.norm(y - rho * v))
    e_y = gamma_fl(M) * float(np.linalg.norm(aTv)) * CERT_INFL \
        + e_rho
    return rho - e_rho - (r + e_y), rho + e_rho + (r + e_y)


def med_xi(bounds_row, X):
    fin = bounds_row[np.isfinite(bounds_row)]
    return (float(np.median(fin)) * X, len(fin)) if len(fin) \
        else (float("nan"), 0)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    anomalies = []
    print("=" * 78)
    print("PRIME.EXCLUSIONLADDER.03 -- the saturation decision "
          "(exclusion_ladder_saturation_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- firewall + benchmark + predeclared cap decision")
    check("S0.AST no zeta-zero generator call (cached RvM list for "
          "wards only; RNG only in the declared C2 scramble)",
          ast_zero_firewall(__file__))
    d1 = json.load(open(os.path.join(_here,
                                     "zero_comb_cache_n2000.json")))
    d2 = json.load(open(os.path.join(_here, "c1_zero_ext_n2500.json")))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    check("S0.CACHE %d cached ordinates, gamma_1 = %.4f"
          % (len(gam_c), gam_c[0]),
          len(gam_c) == 2500 and abs(gam_c[0] - 14.134725) < 1e-5)

    Mw = 640
    cw = srp.continuum_lags(Mw)[:Mw]
    xw = np.cos(0.37 * np.arange(Mw)) / math.sqrt(Mw)
    y_f = sla.matmul_toeplitz((cw, cw), xw, check_finite=False)
    y_d = sla.toeplitz(cw) @ xw
    dev_f = float(np.max(np.abs(y_f - y_d))
                  / max(float(np.max(np.abs(y_d))), 1e-300))
    check("S0.FFT Toeplitz matvec == dense: rel dev %.2e <= %.0e"
          % (dev_f, FFT_WARD_BAR), dev_f <= FFT_WARD_BAR)

    t0 = time.time()
    cs_b, cnt_b, _, ncap_b = seg_assemble([1176], seg=1 << 26)
    t_bench = time.time() - t0
    n1176 = ncap_b[1176]
    print("    benchmark: segmented sieve+reads to n = %d "
          "(%d atoms) in %.1f s" % (n1176, cnt_b[1176], t_bench))

    t0 = time.time()
    lam_tab = core.von_mangoldt_table(ATOM_MAX_DEEP)
    nn0 = np.nonzero(lam_tab > 0.0)[0]
    u_all = np.log(nn0.astype(float))
    mu_all = 2.0 * lam_tab[nn0] / np.sqrt(nn0.astype(float))
    del lam_tab
    al_deep = 0.5 * 1176 * DGRID
    ka = int(np.searchsorted(u_all, 2.0 * al_deep + 1e-14, "right"))
    c_dep, _ = core.atom_lags_at(al_deep, 1176, u_all[:ka],
                                 mu_all[:ka])
    del u_all, mu_all
    print("    deployed overlap path: %.1f s" % (time.time() - t0))
    dev_c = float(np.max(np.abs(cs_b[1176] - c_dep)))
    check("S0.PARITY segmented == deployed T115 path at M = 1176: "
          "atom count %d == %d (EXACT), max |dc| = %.2e <= %.0e"
          % (cnt_b[1176], ka, dev_c, PARITY_C_ABS),
          cnt_b[1176] == ka and dev_c <= PARITY_C_ABS)

    proj = {M: t_bench * (nmax_of_M(M) / n1176) * PROJ_SAFETY
            for M in (M_TARGET, M_STRETCH)}
    print("    projected sieve+reads: M = %d -> %.0f s | M = %d -> "
          "%.0f s (bars %d / %d s, safety x%.1f, predeclared)"
          % (M_TARGET, proj[M_TARGET], M_STRETCH, proj[M_STRETCH],
             T_TARGET_BAR, T_STRETCH_BAR, PROJ_SAFETY))
    new_ms = []
    if proj[M_TARGET] <= T_TARGET_BAR:
        new_ms.append(M_TARGET)
        if proj[M_STRETCH] <= T_STRETCH_BAR:
            new_ms.append(M_STRETCH)
        else:
            anomalies.append("stretch rung skipped by the "
                             "predeclared time rule")
    else:
        anomalies.append("compute wall: projected %.0f s > %.0f s, "
                         "no new rung" % (proj[M_TARGET],
                                          T_TARGET_BAR))
    print("    DECISION: new rungs = %s"
          % (", ".join("M = %d (X = %.6f, cap e^X = %.3e)"
                       % (M, M * DGRID, math.exp(M * DGRID))
                       for M in new_ms) if new_ms else "NONE"))

    # ============================================================== S1
    print("\nS1 -- tower (7 rungs) + anchors + order ward")
    towers = {}
    for M, _a in RUNGS_BASE[:2]:
        alpha = 0.5 * M * DGRID
        ka2 = core.atoms_in(alpha)
        c_at, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka2],
                                    core.MU_ALL[:ka2])
        towers[M] = srp.continuum_lags(M) + c_at
    towers[1176] = srp.continuum_lags(1176) + c_dep

    big_ms = list(M_PREV) + new_ms
    t0 = time.time()
    cs_new, cnt_new, masses_scr, ncap_new = seg_assemble(
        big_ms, collect_mass_M=(M_TARGET if M_TARGET in new_ms
                                else None))
    t_big = time.time() - t0
    for M in big_ms:
        towers[M] = srp.continuum_lags(M) + cs_new[M]
        print("    rung M = %d: %d atoms to n <= %d"
              % (M, cnt_new[M], ncap_new[M]))
    print("    big sieve+reads pass: %.1f s (projected %.0f s)"
          % (t_big, proj.get(new_ms[-1] if new_ms else M_TARGET,
                             float("nan"))))

    all_ms = sorted(towers)
    T_of, m_of, nrm_of = {}, {}, {}
    for M in all_ms:
        T = sla.toeplitz(towers[M][:M])
        T_of[M] = T
        m_of[M] = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        nrm_of[M] = float(sla.norm(T, 2))
    for M, anch in list(RUNGS_BASE) + [(1326, ANCH_1326),
                                       (1414, ANCH_1414)]:
        rel = abs(m_of[M] - anch) / anch
        check("S1.%d anchor M = %d (X = %.3f): lambda_min = %.4e vs "
              "%.4e (rel dev %.4f <= %.2f)"
              % (M, M, M * DGRID, m_of[M], anch, rel, ANCH_REL),
              rel <= ANCH_REL)
    rel780 = abs(m_of[1176] - V780_DEEP) / V780_DEEP
    check("S1.DEEP v780 anchor 3.882e-6 reproduced (rel %.4f)"
          % rel780, rel780 <= ANCH_REL)

    if M_TARGET in new_ms:
        t0 = time.time()
        cs_rev, _, _, _ = seg_assemble([M_TARGET], seg=SEG_DESC,
                                       reverse=True)
        dc = cs_rev[M_TARGET] - cs_new[M_TARGET]
        dc_sum = float(np.sum(np.abs(dc)))
        rob = m_of[M_TARGET] - dc_sum
        check("S1.ORDER summation-order ward at M = %d (%.1f s, "
              "reversed segments 2^25): margin %.3e - sum|dc| %.2e "
              "= %.3e > 0; M = %d noise TYPED as x e^{dX/2} = %.2e "
              "(estimate)"
              % (M_TARGET, time.time() - t0, m_of[M_TARGET], dc_sum,
                 rob, M_STRETCH, dc_sum * math.exp(
                     0.5 * (M_STRETCH - M_TARGET) * DGRID)),
              rob > 0.0)
        if rob <= 0.0:
            anomalies.append("precision wall at M = %d" % M_TARGET)

    # ============================================================== S2
    print("\nS2 -- certificates on all rungs + decline gate + W2")
    xs = np.array([M * DGRID for M, _ in RUNGS_BASE]
                  + [1326.0 * DGRID, 1414.0 * DGRID])
    ys = np.log([m_of[256], m_of[640], m_of[1176], m_of[1326],
                 m_of[1414]])
    sl, ic = np.polyfit(xs, ys, 1)
    cert = {}
    cert_ok = True
    for M in all_ms:
        lb, beta, slack = chol_cert_lower(T_of[M], m_of[M])
        lo, hi = rayleigh_enclosure(T_of[M])
        cert[M] = (lb, lo, hi)
        ok_m = lb is not None and lb > 0.0 and lo <= m_of[M] <= hi
        cert_ok = cert_ok and ok_m
        print("      M = %4d (X = %8.4f): lambda_min = %.4e, "
              "CERTIFIED >= %.4e (slack %.1e), enclosure width %.1e"
              % (M, M * DGRID, m_of[M],
                 lb if lb is not None else float("nan"),
                 slack if slack is not None else float("nan"),
                 hi - lo))
        if lb is not None and lb <= 0.0 < m_of[M]:
            anomalies.append("M = %d certificate lb <= 0 despite "
                             "float margin > 0" % M)
    check("S2.CERT rigorous lambda_min > 0 certificates + bracketing "
          "enclosures on all %d rungs" % len(all_ms), cert_ok)

    for M in new_ms:
        X = M * DGRID
        fl = 100.0 * np.finfo(float).eps * nrm_of[M]
        extr = math.exp(ic + sl * X)
        ratio = m_of[M] / extr
        check("S2.%d NEW rung M = %d (X = %.4f): lambda_min = %.4e "
              "> float budget %.1e; extrapolated decline %.2e "
              "(ratio %.2f in (%.1f, %.1f))"
              % (M, M, X, m_of[M], fl, extr, ratio, SURP_DECL_LO,
                 SURP_DECL_HI),
              m_of[M] > fl and SURP_DECL_LO <= ratio <= SURP_DECL_HI)
        if m_of[M] <= 0.0 or not (SURP_DECL_LO <= ratio
                                  <= SURP_DECL_HI):
            anomalies.append("margin anomaly at M = %d: lambda = "
                             "%.3e vs extrapolated %.2e"
                             % (M, m_of[M], extr))

    aw = a_weight(gam_c)
    for M in new_ms:
        jj = np.arange(M) * DGRID
        worst = 0.0
        for g0 in W2_PACKETS:
            x = np.exp(-0.5 * ((jj - jj[M // 2]) / (M * DGRID / 8.0))
                       ** 2) * np.cos(g0 * jj)
            xTx = float(x @ (T_of[M] @ x))
            Xg = np.abs(np.exp(1j * np.outer(gam_c, jj)) @ x) ** 2
            zside = float(np.sum(2.0 * aw * Xg))
            tb = tail_budget(x, gam_c[-1], len(gam_c))
            worst = max(worst, abs(xTx - zside) / max(tb, 1e-300))
        check("W2 smooth-packet Guinand identity at NEW rung M = %d "
              "(worst ratio %.3f <= %.1f)" % (M, worst, W2_SLACK),
              worst <= W2_SLACK)

    # ============================================================== S3
    print("\nS3 -- THE SATURATION DECISION (frozen gates, base "
          "instrument = parent's grid + 3-step bisection)")
    bounds = {M: np.full(len(GAMMAS_GRID), np.nan) for M in all_ms}
    for M in all_ms:
        cT = towers[M][:M]
        for ig, g in enumerate(GAMMAS_GRID):
            d_mb, _, _ = boundary_scan(cT, M, nrm_of[M], float(g),
                                       EXT_DELTAS, +1.0,
                                       bisect=N_BISECT)
            bounds[M][ig] = d_mb
    xi = {}
    print("    Xi_eff series (base instrument):")
    for M in all_ms:
        X = M * DGRID
        xi_m, reach = med_xi(bounds[M], X)
        xi[M] = xi_m
        print("      X = %8.4f: median delta_mb = %s -> Xi_eff = "
              "%.4f (%d/36 reach)"
              % (X, ("%.5f" % (xi_m / X)) if np.isfinite(xi_m)
                 else "--", xi_m, reach))

    c26 = abs(xi[1326] - XI_1326_CITED) / XI_1326_CITED
    c14 = abs(xi[1414] - XI_1414_CITED) / XI_1414_CITED
    instr_ok = c26 <= XI_INSTR_REL and c14 <= XI_INSTR_REL
    check("S3.INSTR instrument continuity: re-measured Xi(20.719) = "
          "%.4f vs parent %.4f (rel %.3f), Xi(22.094) = %.4f vs "
          "%.4f (rel %.3f) <= %.2f -- the frozen gates are valid"
          % (xi[1326], XI_1326_CITED, c26, xi[1414], XI_1414_CITED,
             c14, XI_INSTR_REL), instr_ok)

    # frozen-grid census + monotone at the new rungs
    maps_ref = {}
    for M in [1414] + new_ms:
        _exc, mbk = census_maps(towers[M][:M], M, nrm_of[M])
        maps_ref[M] = mbk
        print("    frozen-grid margin-break census M = %d: %d/1080"
              % (M, int(mbk.sum())))
    mono_ok = True
    seqm = [1414] + new_ms
    for M1, M2 in zip(seqm[:-1], seqm[1:]):
        lost = int((maps_ref[M1] & ~maps_ref[M2]).sum())
        frac = lost / max(int(maps_ref[M1].sum()), 1)
        mono_ok = mono_ok and frac <= MONO_TOL
        print("    monotone: region(M=%d) minus region(M=%d): %d "
              "pts (%.1f%%)" % (M1, M2, lost, 100 * frac))
    check("S3.MONO new rungs keep the M = 1414 exclusions (loss <= "
          "%.0f%%)" % (100 * MONO_TOL), mono_ok)

    # the gates (priority S1 > S2, predeclared)
    last3 = all_ms[-3:]
    lx = np.log([M * DGRID for M in last3])
    ly = np.log([xi[M] for M in last3])
    slope3 = float(np.polyfit(lx, ly, 1)[0])
    band_devs = {M: abs(xi[M] / XI_1414_CITED - 1.0) for M in new_ms}
    gate_s1 = slope3 <= GATE_SLOPE
    gate_s2 = (len(new_ms) >= 2
               and all(d <= GATE_BAND for d in band_devs.values()))
    print("    GATE S1: log-log slope over the last three rungs "
          "(X = %s) = %.3f (gate <= %.2f) -> %s"
          % (", ".join("%.2f" % (M * DGRID) for M in last3), slope3,
             GATE_SLOPE, "FIRES" if gate_s1 else "no"))
    print("    GATE S2: |Xi/0.2187 - 1| = %s (band %.2f, need >= 2 "
          "new rungs) -> %s"
          % (", ".join("%.3f" % band_devs[M] for M in new_ms),
             GATE_BAND, "FIRES" if gate_s2 else "no"))

    # on-ordinate family at the deepest rung (report)
    deep_m = all_ms[-1]
    cTd = towers[deep_m][:deep_m]
    on_mb = []
    for gz in gam_c[:N_ONZERO]:
        if gz > GAMMAS_GRID[-1]:
            break
        d_on, _, _ = boundary_scan(cTd, deep_m, nrm_of[deep_m],
                                   float(gz), EXT_DELTAS, +1.0,
                                   bisect=N_BISECT)
        on_mb.append(d_on)
    fin_on = [d for d in on_mb if np.isfinite(d)]
    print("    on-ordinate family (M = %d): delta_mb median %.4f, "
          "range [%.4f, %.4f] (%d reach)"
          % (deep_m, float(np.median(fin_on)) if fin_on else
             float("nan"), min(fin_on) if fin_on else float("nan"),
             max(fin_on) if fin_on else float("nan"), len(fin_on)))

    # ============================================================== S4
    print("\nS4 -- mechanism localization (binding only if gate S2)")
    # (a) support test at the deepest rung
    sup_d = {f: [] for f in SUP_FS}
    for ig in BATT_GIDX:
        g = float(GAMMAS_GRID[ig])
        for f in SUP_FS:
            d_f, _, _ = boundary_scan(cTd, deep_m, nrm_of[deep_m],
                                      g, EXT_DELTAS, +1.0,
                                      bisect=N_BISECT, support=f)
            if np.isfinite(d_f):
                sup_d[f].append((ig, d_f))
    sup_slopes = []
    for ig in BATT_GIDX:
        da = dict(sup_d[0.875]).get(ig)
        db = dict(sup_d[1.0]).get(ig)
        if da and db:
            sup_slopes.append(math.log(da / db)
                              / math.log(0.875 / 1.0))
    sup_slope = float(np.median(sup_slopes)) if sup_slopes \
        else float("nan")
    print("    (a) support test at M = %d: median delta_mb by f = "
          "%s; support slope d ln delta / d ln f (0.875 -> 1.0 leg, "
          "median over %d gammas) = %.2f (SUPPORT-ACTIVE iff <= "
          "%.2f)"
          % (deep_m,
             ", ".join("f=%.3f: %.4f"
                       % (f, float(np.median([d for _, d
                                              in sup_d[f]])))
                       if sup_d[f] else "f=%.3f: --" % f
                       for f in SUP_FS),
             len(sup_slopes), sup_slope, SUP_SLOPE_BAR))
    support_active = np.isfinite(sup_slope) \
        and sup_slope <= SUP_SLOPE_BAR

    # (b) grid test: refined instrument over the last three rungs
    xi_ref = {}
    for M in last3:
        cT = towers[M][:M]
        bb = np.full(len(GAMMAS_GRID), np.nan)
        for ig, g in enumerate(GAMMAS_GRID):
            d_mb, _, _ = boundary_scan(cT, M, nrm_of[M], float(g),
                                       REF_DELTAS, +1.0,
                                       bisect=N_BISECT_REF)
            bb[ig] = d_mb
        xi_ref[M], reach = med_xi(bb, M * DGRID)
        print("    (b) refined instrument (1/960 grid, 5-step "
              "bisection): X = %.4f -> Xi_eff = %.4f (%d/36)"
              % (M * DGRID, xi_ref[M], reach))
    lyr = np.log([xi_ref[M] for M in last3])
    slope_ref = float(np.polyfit(lx, lyr, 1)[0])
    print("    (b) refined slope over the last three rungs = %.3f "
          "(GRID-LIMITED iff <= %.2f while the base instrument "
          "stalls)" % (slope_ref, GATE_SLOPE))
    grid_limited = slope_ref <= GATE_SLOPE and not gate_s1

    # (c) per-gamma census + rank-12 battery trend
    print("    (c) per-gamma delta_mb log-slope across the last "
          "three rungs (base instrument):")
    for ig in BATT_GIDX:
        ds = [bounds[M][ig] for M in last3]
        if all(np.isfinite(d) for d in ds):
            s_g = float(np.polyfit(lx, np.log(ds), 1)[0])
            print("        gamma = %7.2f: delta_mb %s  slope %+.2f"
                  % (GAMMAS_GRID[ig],
                     " -> ".join("%.4f" % d for d in ds), s_g))
    gains = {}
    dgt = math.pi / (2.0 * deep_m * DGRID)
    for M in new_ms:
        cT = towers[M][:M]
        g4, g12 = [], []
        dgm = math.pi / (2.0 * M * DGRID)
        for ig in BATT_GIDX:
            g = float(GAMMAS_GRID[ig])
            d4 = bounds[M][ig]
            d12, _, _ = boundary_scan(cT, M, nrm_of[M], g,
                                      EXT_DELTAS, +1.0,
                                      bisect=N_BISECT,
                                      detunes=(-dgm, 0.0, dgm))
            if np.isfinite(d4) and np.isfinite(d12):
                g4.append(d4)
                g12.append(d12)
        if g4:
            gains[M] = 1.0 - float(np.median(g12)) \
                / float(np.median(g4))
            print("    (c) rank-12 battery gain at M = %d: %.1f%% "
                  "(parent cited %.1f%% at X = 22.09; "
                  "battery-limited component iff > %.0f%%)"
                  % (M, 100 * gains[M], 100 * ENRICH_CITED,
                     100 * ENRICH_BATT_BAR))

    # ============================================================== S5
    print("\nS5 -- the honest law (fit-free series + mechanism)")
    print("    Xi_eff(X) series, per-step ratios:")
    prevM = None
    for M in all_ms:
        r = xi[M] / xi[prevM] if prevM else float("nan")
        print("      X = %8.4f: Xi_eff = %.4f%s"
              % (M * DGRID, xi[M],
                 ("  (step ratio %.3f)" % r) if prevM else ""))
        prevM = M
    xi_deep = xi[deep_m]
    print("    depth-to-width table (deepest calibration, Xi_eff = "
          "%.4f):" % xi_deep)
    for dl in (0.5, 0.25, 0.1, 0.05, 0.01):
        xs_ = xi_deep / dl
        print("      delta >= %5.2f excluded at depth X* = %7.1f "
              "(comb cap e^{X*} = %.2e)" % (dl, xs_, math.exp(xs_)))

    # ============================================================== C
    print("\nC -- controls")
    inside_ok, n_in = True, 0
    for ig in MZ_GIDX:
        b = bounds[deep_m][ig]
        if not np.isfinite(b) or 2.0 * b > 0.5:
            continue
        g = float(GAMMAS_GRID[ig])
        ql = quad_lags(deep_m, g, 2.0 * float(b))[:deep_m]
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        lam = full_min(cTd + ql, deep_m)
        n_in += 1
        inside_ok = inside_ok and (lam < -bud)
    check("C1a [must-fire] synthetic quadruple at 2 delta_mb inside "
          "the deepest new region breaks the margin (full "
          "eigensolve): %d/%d points"
          % (n_in if inside_ok else -1, n_in),
          inside_ok and n_in >= 3)
    if not (inside_ok and n_in >= 3):
        anomalies.append("C1a injection ward failed at depth")

    if masses_scr is not None and M_TARGET in new_ms:
        rng = np.random.default_rng(SEED_SCRAMBLE)
        alpha_t = 0.5 * M_TARGET * DGRID
        u_scr = rng.uniform(0.0, 2.0 * alpha_t,
                            size=masses_scr.size)
        c_scr = np.zeros(M_TARGET)
        tent_accumulate(c_scr, M_TARGET, u_scr, masses_scr)
        lam_scr = full_min(srp.continuum_lags(M_TARGET) + c_scr,
                           M_TARGET)
        check("C2 [must-fire] scramble at M = %d (%d masses, seed "
              "%d; stretch-rung scramble skipped -- 19 GB mass "
              "multiset, typed): lambda_min = %.3e < 0"
              % (M_TARGET, masses_scr.size, SEED_SCRAMBLE, lam_scr),
              lam_scr < 0.0)
        if lam_scr >= 0.0:
            anomalies.append("scramble control failed to fire")

    ep_cap = 34000
    r1 = epx.lattice_r1(ep_cap)
    lamE = epx.dirichlet_vonmangoldt(np.asarray(r1, float) / 2.0,
                                     ep_cap)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    masE = 2.0 * lamE[supp] / np.sqrt(supp.astype(float))
    cE, _ = core.atom_lags_at(0.5 * 640 * DGRID, 640, posE, masE)
    lam_ep = full_min(srp.continuum_lags(640) + cE, 640)
    check("C3 [must-fire] Epstein swap (Lambda_E reach %d => M = "
          "640, typed -- the table does NOT reach the new comb "
          "depth): lambda_min = %.3e < 0" % (ep_cap, lam_ep),
          lam_ep < 0.0)
    if lam_ep >= 0.0:
        anomalies.append("Epstein control failed to fire")

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- verdict (frozen gates, priority S1 > S2)")
    print("=" * 78)
    ward_fail = any(f.startswith(("S0", "S1", "S2", "W", "S3.INSTR",
                                  "S3.MONO", "C"))
                    for f in FAILS)
    mech = None
    if not new_ms or anomalies or ward_fail or not instr_ok:
        verdict = "RUNG-LIMITED"
    elif gate_s1:
        verdict = "SHARPENING-CONTINUES"
    elif gate_s2:
        verdict = "SATURATION-TYPED"
        if grid_limited:
            mech = "GRID-LIMITED (the refined instrument restores " \
                   "the decline: the base-grid floor censored it)"
        elif support_active:
            mech = "SUPPORT-ACTIVE-BUT-X-STALLED (mixed/" \
                   "unresolved: the battery still converts support " \
                   "into width inside a rung, yet added depth " \
                   "stopped helping -- per-gamma census above)"
        else:
            mech = "INTRINSIC-WIDTH (support-flat and grid-clean: " \
                   "the rank-4 battery carries an X-independent " \
                   "sensitivity floor)"
    else:
        verdict = "RUNG-LIMITED"
        anomalies.append("decision zone between the frozen gates: "
                         "slope %.3f in (%.2f, band-miss %s)"
                         % (slope3, GATE_SLOPE,
                            ", ".join("%.3f" % band_devs[M]
                                      for M in new_ms)))
    print("\n  VERDICT: %s" % verdict)
    if mech:
        print("  MECHANISM: %s" % mech)
    for a in anomalies:
        print("  TYPED: %s" % a)
    print("\n  slope(last 3, base) = %.3f | slope(last 3, refined) "
          "= %.3f | support slope = %.2f | battery gains = %s"
          % (slope3, slope_ref, sup_slope,
             ", ".join("M=%d: %.1f%%" % (M, 100 * gains[M])
                       for M in gains) if gains else "--"))
    print("\n  THE RUNG TABLE (all 7 rungs, certified):")
    print("  %9s %10s %11s %12s %9s %8s" % (
        "X", "comb cap", "lam_min", "cert lower", "med d_mb",
        "Xi_eff"))
    for M in all_ms:
        X = M * DGRID
        lb = cert[M][0]
        fin = bounds[M][np.isfinite(bounds[M])]
        print("  %9.4f %10.2e %11.4e %12.4e %9s %8.4f"
              % (X, math.exp(X), m_of[M],
                 lb if lb is not None else float("nan"),
                 ("%.5f" % float(np.median(fin))) if len(fin)
                 else "--", xi[M]))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
