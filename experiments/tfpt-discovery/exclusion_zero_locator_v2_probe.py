"""PRIME.EXCLUSIONLADDER.07 -- locator v2: the preregistered
out-of-sample zero-locator test (EXPLORATION ONLY).

PARENT: exclusion_zero_locator_probe.py (2026-08-06, LOCATOR-NULL
under the frozen gates): on the LEARNING window gamma in [5, 60]
the width profile peaked at 12/13 true ordinates (precision 0.070,
depth-improving), but the frozen prominence bar ln(1.5) admitted a
dense false-peak background (61% FP) that kept the shifted null at
chance.  POST-HOC (learned on [5, 60], hence inadmissible there):
matched peaks had prominence >= 0.82, false peaks <= 0.73 -- a
perfect separation, threshold ln(2.2) proposed.  THIS PROBE
(user-authorized): freeze ln(2.2) and score EXCLUSIVELY on the
DISJOINT test window gamma in [60, 120], previously untouched by
any locator evaluation.

THE V2 PREREGISTRATION (frozen + hashed BEFORE any test-window
evaluation):
    locator rule: prominent local maxima of log W(gamma) with
    prominence >= ln(2.2) (the learned constant, now frozen; the
    task's 'minima of the exclusion sharpness 1/W' -- same rule,
    orientation fixed by parent diagnostics);
    W(gamma) = uncensored margin-break boundary of battery v2b on
    the extended instrument (grid floor 4.02e-4, bisection 4);
    test window [60, 120], step 0.25 (241 points); match tol 0.5;
    EDGE GUARD (frozen): detection targets = verified ordinates in
    [61, 119]; peaks matching ANY cached ordinate within 0.5
    (including ordinates just outside the window) are not false
    positives; peaks within 1.0 of the window edges are excluded
    from FP counting;
    rungs X = 18.375 / 22.094 / 24.813 (depth law; deepest primary).
BATTERY V2B (mechanical band extension, typed): the deployed v2
    design with its in-band densification rule dg = k*pi/(4X),
    k in -4..4 (rank 36) applied to the TEST band [60, 120] exactly
    as to the original band [14, 50]; everything else byte-
    identical.  NO zero datum entered: the band is the predeclared
    test window itself.  Hashed below; the parent v2 hash is
    ward-checked for the unmodified base design.
FROZEN BARS: detection >= 80%, false positives <= 20%.
CONTROLS (frozen): C1 scramble comb (M = 1503, masses preserved,
    seed 7): zero prominent peaks expected; C2 Epstein comb
    (M = 640, different zero set): must NOT track zeta ordinates
    (detection <= 0.25 or no peaks); C3 shifted null (+2.5) WITH A
    TYPED STRUCTURAL CEILING: near gamma ~ 100 the mean zero gap is
    ~ 2.4, so shifting the TRUE ordinates by +2.5 re-locks onto the
    zero comb for a computable fraction (the re-lock ceiling, a
    property of the ordinate table, admissible for control
    calibration only) -- an absolute <= 1/3 bar would fail a
    PERFECT locator; frozen bar: shifted detection <= max(true/3,
    ceiling + 0.10), raw numbers reported; C4 grid-refinement x2 on
    the subwindow [75, 95]: matched peaks stable within 0.25.
MECHANISM CARRY-OVER (frozen): at the matched peaks nearest the
    predeclared isolated ordinates 77.14 and 101.32, and at the
    predeclared off-zero points 63.0 and 90.5: boundary, break
    state at the frozen probe delta* = 0.004 (v1 carry-over), and
    the frozen check median(W matched) >= 2 x median(W off-zero).
VERDICT (frozen enum): LOCATOR-V2-RESOLVES (bars met out-of-sample
    with all four controls -- promotion-grade, report the law) /
    LOCATOR-V2-PARTIAL (detection >= max(0.40, 2 x chance) with
    chance = N_peaks * 1.0 / 60 -- above chance, bars missed,
    typed) / LOCATOR-V2-DEAD (the separation was window-specific
    overfit -- typed honestly).
INFORMATION FLOW (typed): the threshold ln(2.2) was learned on
    [5, 60] (instrument diagnostics, admissible); the test-window
    ordinates enter ONLY the scoring and control-calibration steps;
    the battery band extension is a mechanical rule application.
DELIVERABLE EXTRAS: profile data written to
    exclusion_zero_locator_v2_profile.json (data file, no .md).

FIREWALL: v563/v755 read-only; NO zetazero()/nzeros() calls (AST-
checked); cached RvM ordinates for scoring/control calibration
only; RNG only in the declared C1 scramble.  NO RH claim.
"""
import ast
import hashlib
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
RUNG_MS = (1176, 1414, 1588)
SIEVE_MS = (1176, 1414, 1503, 1588)
LAM_CITED = {1176: 3.8825e-6, 1414: 2.0092e-6, 1503: 1.5883e-6,
             1588: 1.0779e-6}
ANCH_REL = 2.0e-2
ATOM_MAX_DEEP = 100000000
SEG_ASC = 1 << 28
PARITY_C_ABS = 5.0e-9
FFT_WARD_BAR = 1.0e-9
EXT_DELTAS = np.geomspace(1.0 / 240.0, 0.5, 44)
_RATIO = 120.0 ** (1.0 / 43.0)
EXT2_DELTAS = np.concatenate(
    [EXT_DELTAS[0] * _RATIO ** (-np.arange(21, 0, -1.0)), EXT_DELTAS])
N_BISECT = 4
BAND_LO, BAND_HI = 14.0, 50.0
TEST_LO, TEST_HI = 60.0, 120.0
IDENT_BUD = 1.0e-8
U_RND = 0.5 * np.finfo(float).eps
CERT_INFL = 1.01

DG_PROF = 0.25
PROF_GS = np.arange(TEST_LO, TEST_HI + 1e-9, DG_PROF)
PROM_MIN = math.log(2.2)              # the learned, now-frozen bar
MATCH_TOL = 0.5
W_CAP = 0.5
EDGE_GUARD = 1.0
SCORE_LO, SCORE_HI = TEST_LO + EDGE_GUARD, TEST_HI - EDGE_GUARD
GATE_DET, GATE_FP = 0.80, 0.20
PART_DET = 0.40
REFINE_LO, REFINE_HI, DG_REFINE = 75.0, 95.0, 0.125
REFINE_MOVE_TOL = 0.25
SHIFT_NULL = 2.5
CEIL_MARGIN = 0.10
CTRL_DG = 0.5
CTRL_DET_BAR = 0.25
MECH_ZEROS = (77.144840, 101.317851)   # predeclared isolated targets
MECH_OFF = (63.0, 90.5)                # predeclared off-zero points
MECH_DELTA = 0.004
MECH_RATIO_BAR = 2.0
SEED_SCRAMBLE = 7
EPSTEIN_CAP = 34000

BATTERY_V2_DESIGN = (
    "battery-v2|columns exp(+/-delta*j*D)*{cos,sin}((gamma+dg)*j*D),"
    "full support,QR-orthonormalized|out-band: dg=k*pi/(2*X),"
    "k in {-1,0,1} (rank 12)|in-band gamma in [14.0,50.0]: "
    "dg=k*pi/(4*X),k in {-4..4} (rank 36)|criterion unchanged: "
    "subspace lambda_min(T+-Q) < -(1e-8+100*eps*(||T||+M*max|q|))|"
    "grids unchanged: gamma geomspace(2,190,36), delta "
    "geomspace(1/240,1/2,44)+3-step bisection|D=1/64"
)
V2_HASH_CITED = ("fd39fb42ab1beb8137a359ff9c9934475a2467"
                 "7bf305d111b4fe43a4c6ca02c0")
LOCATOR_V2_DESIGN = (
    BATTERY_V2_DESIGN
    + "|v2b band extension (mechanical): the in-band rule "
      "dg=k*pi/(4*X),k in {-4..4} applied ALSO to the test band "
      "[60,120]; no zero datum entered"
    + "|locator-v2: W(gamma)=uncensored delta_mb, extended grid "
      "(floor 4.02e-4, bisect 4); TEST window [60,120] step 0.25 "
      "(disjoint from the learning window [5,60]); peaks of log W "
      "with prominence >= ln(2.2) (learned on [5,60], frozen); "
      "match tol 0.5; edge guard 1.0; rungs M=1176,1414,1588"
    + "|bars: det>=0.80, fp<=0.20|controls: scramble M=1503 + "
      "Epstein M=640 step 0.5 (det<=0.25 or no peaks); shifted "
      "null +2.5 with structural re-lock ceiling (bar: shifted <= "
      "max(true/3, ceiling+0.10)); refine [75,95] x2 (move<=0.25)"
    + "|mechanism: probe delta*=0.004 at matched(77.14,101.32) vs "
      "off(63.0,90.5); median-ratio bar 2.0"
    + "|gates: RESOLVES bars+4 controls; PARTIAL det >= "
      "max(0.40, 2*N_peaks*1.0/60); else DEAD"
)
LOC2_HASH = hashlib.sha256(LOCATOR_V2_DESIGN.encode()).hexdigest()


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


def quad_lags(M, gamma, delta):
    z1, z2 = complex(delta, gamma), complex(-delta, gamma)
    t = np.abs(np.arange(-1, M + 1)) * DGRID
    g = 2.0 * (np.exp(z1 * t) / z1 ** 2 + np.exp(z2 * t) / z2 ** 2).real
    return (g[:-2] - 2.0 * g[1:-1] + g[2:]) / DGRID


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


def seg_assemble(Ms, collect_mass_M=None, seg=SEG_ASC):
    Ms = sorted(Ms)
    ncap = {M: nmax_of_M(M) for M in Ms}
    nmax = max(ncap.values())
    cs = {M: np.zeros(M) for M in Ms}
    cnt = {M: 0 for M in Ms}
    mass_cap = ncap[collect_mass_M] if collect_mass_M else None
    masses = [] if mass_cap else None
    bp = base_primes(int(math.isqrt(nmax)))
    for lo in range(0, nmax + 1, seg):
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


def detunes_v2b(M, gamma):
    X = M * DGRID
    if BAND_LO <= gamma <= BAND_HI or TEST_LO <= gamma <= TEST_HI:
        d = math.pi / (4.0 * X)
        return tuple(k * d for k in range(-4, 5))
    d = math.pi / (2.0 * X)
    return tuple(k * d for k in range(-1, 2))


def battery_B(M, gamma, delta, detunes=(0.0,)):
    jj = np.arange(M) * DGRID
    cols = []
    for dg in detunes:
        g = gamma + dg
        for sgn in (delta, -delta):
            e = np.exp(sgn * jj)
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


def boundary_scan(cT, M, nrmT, g, detunes, grid=EXT2_DELTAS,
                  bisect=N_BISECT):
    prev = None
    for dl in grid:
        dl = float(dl)
        ql = quad_lags(M, g, dl)[:M]
        Qb, _ = np.linalg.qr(battery_B(M, g, dl, detunes))
        bud = bud_of(M, nrmT, float(np.max(np.abs(ql))))
        lam, wit = sub_lam(cT + ql, Qb)
        if lam < -bud:
            hit, w_hit, lo = dl, wit, prev
            for _ in range(bisect):
                if lo is None:
                    break
                mid = math.sqrt(lo * hit)
                qlm = quad_lags(M, g, mid)[:M]
                Qbm, _ = np.linalg.qr(battery_B(M, g, mid, detunes))
                bm = bud_of(M, nrmT, float(np.max(np.abs(qlm))))
                lm, wm = sub_lam(cT + qlm, Qbm)
                if lm < -bm:
                    hit, w_hit = mid, wm
                else:
                    lo = mid
            return hit, w_hit
        prev = dl
    return float("nan"), None


def full_min(cA, M):
    return float(sla.eigvalsh(sla.toeplitz(cA),
                              subset_by_index=[0, 0])[0])


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
        return beta - slack - e_diag
    return None


def dense_profile(cT, M, nrmT, gammas):
    W = np.empty(len(gammas))
    for i, g in enumerate(gammas):
        d_mb, _ = boundary_scan(cT, M, nrmT, float(g),
                                detunes_v2b(M, float(g)))
        W[i] = d_mb if np.isfinite(d_mb) else W_CAP
    return W


def find_peaks(gs, W, prom_min=PROM_MIN):
    lw = np.log(W)
    n = len(gs)
    out = []
    for i in range(1, n - 1):
        if lw[i] > lw[i - 1] and lw[i] >= lw[i + 1]:
            keys = []
            for step in (-1, 1):
                j = i + step
                vmin = lw[i]
                while 0 <= j < n and lw[j] <= lw[i]:
                    vmin = min(vmin, lw[j])
                    j += step
                keys.append(vmin)
            prom = lw[i] - max(keys)
            if prom >= prom_min:
                out.append((float(gs[i]), float(prom)))
    return out


def score_v2(peaks, det_zeros, all_zeros, tol=MATCH_TOL):
    pg = np.array([p[0] for p in peaks]) if peaks else np.array([])
    matches = []
    for gz in det_zeros:
        if pg.size:
            k = int(np.argmin(np.abs(pg - gz)))
            if abs(pg[k] - gz) <= tol:
                matches.append((float(gz), float(pg[k]),
                                float(abs(pg[k] - gz))))
    det = len(matches) / len(det_zeros) if len(det_zeros) \
        else float("nan")
    az = np.asarray(all_zeros)
    fp_pool = [p for p in pg if SCORE_LO <= p <= SCORE_HI]
    n_fp = sum(1 for p in fp_pool
               if float(np.min(np.abs(az - p))) > tol)
    fp = n_fp / len(fp_pool) if fp_pool else 0.0
    prec = float(np.median([m[2] for m in matches])) if matches \
        else float("nan")
    return det, fp, prec, matches, len(pg), len(fp_pool)


def witness_group_split(M, g, dl, detunes, wit):
    e0 = float(wit @ wit)
    fr = []
    for dg in detunes:
        Qg, _ = np.linalg.qr(battery_B(M, g, dl, (dg,)))
        fr.append(float(np.linalg.norm(Qg.T @ wit) ** 2) / e0)
    return fr


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.EXCLUSIONLADDER.07 -- locator v2, out-of-sample "
          "(exclusion_zero_locator_v2_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- preregistration + wards + tower rebuild")
    v2h = hashlib.sha256(BATTERY_V2_DESIGN.encode()).hexdigest()
    check("S0.V2HASH base battery v2 unchanged: %s.. == %s.."
          % (v2h[:16], V2_HASH_CITED[:16]), v2h == V2_HASH_CITED)
    print("    PREREG (frozen before any test-window evaluation): "
          "TEST window [%g, %g] (disjoint from the learning window "
          "[5, 60]); prominence >= ln(2.2) = %.4f (learned there, "
          "frozen here); match tol %g; edge guard %g."
          % (TEST_LO, TEST_HI, PROM_MIN, MATCH_TOL, EDGE_GUARD))
    print("    SHA-256: %s" % LOC2_HASH)
    print("    INFORMATION FLOW (typed): threshold ln(2.2) <- "
          "learning-window diagnostics (admissible); battery band "
          "extension <- mechanical rule application, no zero "
          "datum; test-window ordinates -> scoring + control "
          "calibration ONLY.")
    check("S0.AST no zeta-zero generator call (cached RvM list for "
          "scoring/control calibration only; RNG only in C1)",
          ast_zero_firewall(__file__))
    d1 = json.load(open(os.path.join(_here,
                                     "zero_comb_cache_n2000.json")))
    d2 = json.load(open(os.path.join(_here, "c1_zero_ext_n2500.json")))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    det_zeros = [float(g) for g in gam_c
                 if SCORE_LO <= g <= SCORE_HI]
    check("S0.CACHE %d cached ordinates; K = %d detection targets "
          "in [%g, %g]" % (len(gam_c), len(det_zeros), SCORE_LO,
                           SCORE_HI),
          len(gam_c) == 2500 and len(det_zeros) >= 15)
    tgt_sh = [z + SHIFT_NULL for z in det_zeros
              if SCORE_LO <= z + SHIFT_NULL <= SCORE_HI]
    relock = (sum(1 for t in tgt_sh
                  if float(np.min(np.abs(gam_c - t))) <= MATCH_TOL)
              / len(tgt_sh)) if tgt_sh else 0.0
    print("    C3 structural re-lock ceiling (ordinate table, "
          "control calibration): %.0f%% of the +%.1f-shifted TRUE "
          "ordinates land within %.1f of a true ordinate -- the "
          "frozen bar is shifted <= max(true/3, %.0f%% + %.0f pts)"
          % (100 * relock, SHIFT_NULL, MATCH_TOL, 100 * relock,
             100 * CEIL_MARGIN))
    Mw = 640
    cw = srp.continuum_lags(Mw)[:Mw]
    xw = np.cos(0.37 * np.arange(Mw)) / math.sqrt(Mw)
    dev_f = float(np.max(np.abs(
        sla.matmul_toeplitz((cw, cw), xw, check_finite=False)
        - sla.toeplitz(cw) @ xw)))
    check("S0.FFT Toeplitz matvec == dense: max dev %.2e" % dev_f,
          dev_f <= FFT_WARD_BAR)

    lam_tab = core.von_mangoldt_table(ATOM_MAX_DEEP)
    nn0 = np.nonzero(lam_tab > 0.0)[0]
    u_all = np.log(nn0.astype(float))
    mu_all = 2.0 * lam_tab[nn0] / np.sqrt(nn0.astype(float))
    del lam_tab
    al = 0.5 * 1176 * DGRID
    ka = int(np.searchsorted(u_all, 2.0 * al + 1e-14, "right"))
    c_dep, _ = core.atom_lags_at(al, 1176, u_all[:ka], mu_all[:ka])
    del u_all, mu_all
    t0 = time.time()
    cs, cnt, masses_scr, _ = seg_assemble(list(SIEVE_MS),
                                          collect_mass_M=1503)
    print("    big sieve+reads pass: %.1f s" % (time.time() - t0))
    dev_c = float(np.max(np.abs(cs[1176] - c_dep)))
    check("S0.PARITY segmented == deployed path at M = 1176: count "
          "%d == %d, max |dc| = %.2e" % (cnt[1176], ka, dev_c),
          cnt[1176] == ka and dev_c <= PARITY_C_ABS)

    towers, m_of, nrm_of = {}, {}, {}
    anch_ok, cert_ok = True, True
    for M in SIEVE_MS:
        towers[M] = srp.continuum_lags(M) + cs[M]
        T = sla.toeplitz(towers[M][:M])
        m_of[M] = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        nrm_of[M] = float(sla.norm(T, 2))
        anch_ok = anch_ok and abs(m_of[M] - LAM_CITED[M]) \
            / LAM_CITED[M] <= ANCH_REL
        if M in RUNG_MS:
            lb = chol_cert_lower(T, m_of[M])
            cert_ok = cert_ok and lb is not None and lb > 0.0
    check("S0.RUNGS lambda_min anchors (rel <= %.2f) + PD "
          "certificates on the locator rungs" % ANCH_REL,
          anch_ok and cert_ok)

    # ============================================================== S1
    print("\nS1 -- the BLIND RUN: W(gamma) on the test window "
          "(%d points, %d rungs)" % (len(PROF_GS), len(RUNG_MS)))
    profiles, peaks_of = {}, {}
    for M in RUNG_MS:
        t0 = time.time()
        profiles[M] = dense_profile(towers[M][:M], M, nrm_of[M],
                                    PROF_GS)
        peaks_of[M] = find_peaks(PROF_GS, profiles[M])
        print("      X = %8.4f: W in [%.4f, %.4f], %d prominent "
              "peaks (%.1f s)"
              % (M * DGRID, float(np.min(profiles[M])),
                 float(np.max(profiles[M])), len(peaks_of[M]),
                 time.time() - t0))
    deep_m = RUNG_MS[-1]
    check("S1.REACH deepest profile fully uncensored above the "
          "floor and below the cap",
          float(np.min(profiles[deep_m])) > EXT2_DELTAS[0] * (1 + 1e-9)
          and float(np.max(profiles[deep_m])) < W_CAP * (1 - 1e-12))
    out_json = {"gammas": [float(g) for g in PROF_GS],
                "W": {str(M): [float(w) for w in profiles[M]]
                      for M in RUNG_MS},
                "peaks": {str(M): peaks_of[M] for M in RUNG_MS},
                "locator_v2_hash": LOC2_HASH}
    with open(os.path.join(_here,
                           "exclusion_zero_locator_v2_profile.json"),
              "w") as fh:
        json.dump(out_json, fh)
    print("    profile data -> exclusion_zero_locator_v2_profile"
          ".json")

    # ============================================================== S2
    print("\nS2 -- out-of-sample scoring (ordinates admissible "
          "HERE only)")
    res = {}
    for M in RUNG_MS:
        det, fp, prec, matches, n_pk, n_pool = score_v2(
            peaks_of[M], det_zeros, gam_c)
        res[M] = (det, fp, prec, matches, n_pk)
        print("      X = %8.4f: peaks %2d (%2d scored) | detection "
              "%4.0f%% (%d/%d) | false-pos %4.0f%% | precision %.3f"
              % (M * DGRID, n_pk, n_pool, 100 * det, len(matches),
                 len(det_zeros), 100 * fp,
                 prec if np.isfinite(prec) else float("nan")))
    det_d, fp_d, prec_d, matches_d, npk_d = res[deep_m]
    print("    predicted-vs-true table (deepest rung, X = %.4f):"
          % (deep_m * DGRID))
    print("      %9s %10s %8s %6s" % ("gamma_pred", "prominence",
                                      "true", "|d|"))
    for gp, pr in peaks_of[deep_m]:
        k = int(np.argmin(np.abs(gam_c - gp)))
        dd = abs(float(gam_c[k]) - gp)
        print("      %9.3f %10.3f %8s %6s"
              % (gp, pr,
                 ("%.3f" % gam_c[k]) if dd <= MATCH_TOL else "--",
                 ("%.3f" % dd) if dd <= MATCH_TOL else "FP"))
    missed = [float(z) for z in det_zeros
              if not any(abs(m[0] - z) < 1e-9 for m in matches_d)]
    if missed:
        print("      missed zeros: %s"
              % ", ".join("%.3f" % z for z in missed))
    check("S2.BARS out-of-sample: detection %.0f%% >= %.0f%% AND "
          "false-pos %.0f%% <= %.0f%%"
          % (100 * det_d, 100 * GATE_DET, 100 * fp_d, 100 * GATE_FP),
          det_d >= GATE_DET and fp_d <= GATE_FP)

    # ============================================================== S3
    print("\nS3 -- depth law on the test window")
    precs = [(M * DGRID, res[M][2]) for M in RUNG_MS
             if np.isfinite(res[M][2])]
    if len(precs) >= 2:
        lx = np.log([p[0] for p in precs])
        ly = np.log([p[1] for p in precs])
        slope_p = float(np.polyfit(lx, ly, 1)[0])
        print("    precision-vs-depth: %s | log-log slope %.2f "
              "(half-grid floor %.3f, typed)"
              % (", ".join("X=%.1f: %.3f" % p for p in precs),
                 slope_p, DG_PROF / 2.0))
    print("    detection-vs-depth: %s"
          % ", ".join("X=%.1f: %.0f%%" % (M * DGRID,
                                          100 * res[M][0])
                      for M in RUNG_MS))

    # ============================================================== S4
    print("\nS4 -- mechanism carry-over (frozen points)")
    cTd = towers[deep_m][:deep_m]
    pg_d = np.array([p[0] for p in peaks_of[deep_m]]) \
        if peaks_of[deep_m] else np.array([])
    w_matched, w_off = [], []
    mech_pts = []
    for gz in MECH_ZEROS:
        if pg_d.size:
            gp = float(pg_d[int(np.argmin(np.abs(pg_d - gz)))])
            mech_pts.append(("matched(%.2f)" % gz, gp, True))
        else:
            mech_pts.append(("matched(%.2f)" % gz, gz, True))
    for go in MECH_OFF:
        mech_pts.append(("off-zero", float(go), False))
    for lab, g, is_m in mech_pts:
        det = detunes_v2b(deep_m, g)
        d_mb, wit = boundary_scan(cTd, deep_m, nrm_of[deep_m], g,
                                  det)
        ql = quad_lags(deep_m, g, MECH_DELTA)[:deep_m]
        Qb, _ = np.linalg.qr(battery_B(deep_m, g, MECH_DELTA, det))
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        lam_p, _ = sub_lam(cTd + ql, Qb)
        (w_matched if is_m else w_off).append(float(d_mb))
        split_txt = ""
        if wit is not None and np.isfinite(d_mb):
            fr = witness_group_split(deep_m, g, float(d_mb), det,
                                     wit)
            kd = int(np.argmax(fr))
            split_txt = " | witness energy: dominant detune k = " \
                "%+d (frac %.2f)" % (kd - (len(det) // 2), fr[kd])
        print("      %-14s gamma = %8.3f: delta_mb = %.5f | at "
              "delta* = %.3f: lambda_min = %+.2e (%s)%s"
              % (lab, g, d_mb, MECH_DELTA, lam_p,
                 "BREAKS" if lam_p < -bud else "HOLDS", split_txt))
    ratio = (float(np.median(w_matched)) / float(np.median(w_off))) \
        if w_off and all(np.isfinite(w_matched + w_off)) \
        else float("nan")
    check("S4.MECH carry-over: median W(matched) / median "
          "W(off-zero) = %.2f >= %.1f (the redundancy reading "
          "out-of-sample)" % (ratio, MECH_RATIO_BAR),
          np.isfinite(ratio) and ratio >= MECH_RATIO_BAR)

    # ============================================================== C
    print("\nC -- controls")
    ctrl_gs = np.arange(TEST_LO, TEST_HI + 1e-9, CTRL_DG)

    rng = np.random.default_rng(SEED_SCRAMBLE)
    alpha_t = 0.5 * 1503 * DGRID
    u_scr = rng.uniform(0.0, 2.0 * alpha_t, size=masses_scr.size)
    c_scr = np.zeros(1503)
    tent_accumulate(c_scr, 1503, u_scr, masses_scr)
    tow_scr = srp.continuum_lags(1503) + c_scr
    lam_scr = full_min(tow_scr, 1503)
    nrm_scr = float(sla.norm(sla.toeplitz(tow_scr[:1503]), 2))
    W_scr = dense_profile(tow_scr[:1503], 1503, nrm_scr, ctrl_gs)
    pk_scr = find_peaks(ctrl_gs, W_scr)
    det_s = score_v2(pk_scr, det_zeros, gam_c)[0]
    check("C1 scramble comb (lambda_min = %.2e, %d masses, seed "
          "%d): %d peaks, zeta-detection %.0f%% <= %.0f%% (or no "
          "peaks)" % (lam_scr, masses_scr.size, SEED_SCRAMBLE,
                      len(pk_scr), 100 * det_s, 100 * CTRL_DET_BAR),
          len(pk_scr) == 0 or det_s <= CTRL_DET_BAR)

    r1 = epx.lattice_r1(EPSTEIN_CAP)
    lamE = epx.dirichlet_vonmangoldt(np.asarray(r1, float) / 2.0,
                                     EPSTEIN_CAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    Me = 640
    cE, _ = core.atom_lags_at(
        0.5 * Me * DGRID, Me, np.log(supp.astype(float)),
        2.0 * lamE[supp] / np.sqrt(supp.astype(float)))
    tow_ep = srp.continuum_lags(Me) + cE
    lam_ep = full_min(tow_ep, Me)
    nrm_ep = float(sla.norm(sla.toeplitz(tow_ep[:Me]), 2))
    W_ep = dense_profile(tow_ep[:Me], Me, nrm_ep, ctrl_gs)
    pk_ep = find_peaks(ctrl_gs, W_ep)
    det_e = score_v2(pk_ep, det_zeros, gam_c)[0]
    check("C2 Epstein comb (lambda_min = %.2e, M = %d): %d peaks, "
          "zeta-detection %.0f%% <= %.0f%% (or no peaks)"
          % (lam_ep, Me, len(pk_ep), 100 * det_e,
             100 * CTRL_DET_BAR),
          len(pk_ep) == 0 or det_e <= CTRL_DET_BAR)

    det_sh = score_v2(peaks_of[deep_m], tgt_sh, tgt_sh)[0] \
        if tgt_sh else 0.0
    sh_bar = max(det_d / 3.0, relock + CEIL_MARGIN)
    shift_ok = det_sh <= sh_bar + 1e-12
    check("C3 shifted null (+%.1f, %d targets): detection %.0f%% "
          "<= bar %.0f%% (= max(true/3 = %.0f%%, re-lock ceiling "
          "%.0f%% + %.0f pts))"
          % (SHIFT_NULL, len(tgt_sh), 100 * det_sh, 100 * sh_bar,
             100 * det_d / 3.0, 100 * relock, 100 * CEIL_MARGIN),
          shift_ok)

    ref_gs = np.arange(REFINE_LO, REFINE_HI + 1e-9, DG_REFINE)
    W_ref = dense_profile(cTd, deep_m, nrm_of[deep_m], ref_gs)
    pk_ref = find_peaks(ref_gs, W_ref)
    pg_ref = np.array([p[0] for p in pk_ref]) if pk_ref \
        else np.array([])
    sub_matches = [m for m in matches_d
                   if REFINE_LO + 1.0 <= m[1] <= REFINE_HI - 1.0]
    n_stable = sum(
        1 for m in sub_matches
        if pg_ref.size
        and float(np.min(np.abs(pg_ref - m[1]))) <= REFINE_MOVE_TOL)
    grid_ok = len(sub_matches) >= 2 and n_stable == len(sub_matches)
    check("C4 grid-artifact ward (subwindow [%g, %g] refined x2): "
          "%d/%d matched peaks reappear within %.2f"
          % (REFINE_LO, REFINE_HI, n_stable, len(sub_matches),
             REFINE_MOVE_TOL), grid_ok)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- verdict")
    print("=" * 78)
    c1_ok = len(pk_scr) == 0 or det_s <= CTRL_DET_BAR
    c2_ok = len(pk_ep) == 0 or det_e <= CTRL_DET_BAR
    chance = npk_d * (2.0 * MATCH_TOL) / (TEST_HI - TEST_LO)
    if det_d >= GATE_DET and fp_d <= GATE_FP and c1_ok and c2_ok \
            and shift_ok and grid_ok:
        verdict = "LOCATOR-V2-RESOLVES"
    elif det_d >= max(PART_DET, 2.0 * chance):
        verdict = "LOCATOR-V2-PARTIAL"
    else:
        verdict = "LOCATOR-V2-DEAD"
    print("\n  VERDICT: %s" % verdict)
    print("  prereg hash: %s" % LOC2_HASH[:16])
    print("  out-of-sample (X = %.4f): detection %.0f%% | "
          "false-pos %.0f%% | precision %.3f | shifted %.0f%% "
          "(ceiling %.0f%%) | chance %.0f%%"
          % (deep_m * DGRID, 100 * det_d, 100 * fp_d, prec_d,
             100 * det_sh, 100 * relock, 100 * chance))
    if FAILS:
        print("  TYPED FAILURES: %s" % ",".join(FAILS))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
