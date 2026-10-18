"""PRIME.EXCLUSIONLADDER.06 -- the zero locator: does the exclusion
instrument LOCATE zeros, not just exclude regions?  (EXPLORATION
ONLY.)

PARENT: exclusion_range_extension_probe.py (2026-08-06,
RANGE-DECIDES-DECLINE, 13/13): the uncensored margin-break
boundaries delta_mb rank-correlate -0.872 with the distance to the
nearest true ordinate, hash-verified non-circular (battery v2,
SHA-256 fd39fb42.., designed without any zero datum).  THIS PROBE
(user-authorized): build a dense width profile W(gamma) = delta_mb
(gamma) and test whether its extremal features localize individual
zeros.

ORIENTATION (typed, fixed by the PARENT's measured sign, which is
instrument diagnostics, not zero data): near-ordinate rows have
LARGER delta_mb (on-ordinate median 0.0112 vs off-zero 0.0033) --
the width profile PEAKS at true zeros (a real zero at gamma makes
the injected synthetic quadruple there REDUNDANT: T + Q stays
consistent to larger delta, so the breakable margin shrinks and the
boundary rises).  The frozen locator therefore takes prominent
local MAXIMA of W, i.e. local minima of the exclusion sharpness
1/W -- the task's dip-in-sensitivity reading, same rule.

THE LOCATOR (frozen a priori, hashed below; NO zero table enters
the construction -- ordinates enter ONLY in the scoring step):
    window gamma in [5, 60], resolution 0.25 (221 points);
    W(gamma) = uncensored margin-break boundary of battery v2 on
    the extended instrument (grid floor 4.02e-4, bisection 4);
    rungs X = 18.375 / 22.094 / 24.813 (depth law; deepest =
    primary); predicted ordinates = local maxima of log W with
    prominence >= ln(1.5); match tolerance 0.5; W capped at 0.5
    where no break occurs (typed).
SCORING (verified RvM cached ordinates, admissible here only):
    detection rate (true zeros with a predicted peak within 0.5),
    false-positive rate (peaks with no zero within 0.5),
    localization precision (median |gamma_pred - gamma_true|) and
    its depth scaling across the three rungs.
MECHANISM (measure, don't narrate): at two matched peaks (the
    peaks nearest gamma_2 = 21.02 and gamma_5 = 32.94, predeclared)
    and two predeclared off-zero points (gamma = 10.0, 28.0):
    boundary, break state at the frozen probe delta* = 0.004, and
    the witness-energy split across detune groups.
CONTROLS (frozen): C1 scramble comb at M = 1503 (masses preserved,
    seed 7; coarse profile 0.5) -- must NOT track zeta ordinates
    (detection <= 0.25 or no peaks); C2 Epstein comb at M = 640
    (different zero set -- the strongest non-circularity
    demonstration): must NOT track zeta ordinates (same bar); C3
    shifted-window null (score the primary peaks against ordinates
    + 2.5): detection must collapse to <= 1/3 of the true rate; C4
    grid-artifact ward (subwindow [18, 34] refined x2 to 0.125):
    every matched peak there must reappear within 0.25.
VERDICT (frozen enum): LOCATOR-RESOLVES (detection >= 80% AND
    false positives <= 20% AND C3 + C4 pass -- precision + depth
    law typed) / LOCATOR-PARTIAL (detection >= 40% AND >= 2x the
    shifted null -- real but unsharp) / LOCATOR-NULL (typed why).
    Ward/control failures are typed on the verdict line.
DELIVERABLE EXTRAS: the full W(gamma) profile data is written to
    exclusion_zero_locator_profile.json (data file, no .md).

FIREWALL: v563/v755 read-only; NO zetazero()/nzeros() calls (AST-
checked); cached RvM ordinates for SCORING only; RNG only in the
declared C1 scramble.  NO RH claim.
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
RUNG_MS = (1176, 1414, 1588)          # depth-law rungs, deepest primary
SIEVE_MS = (1176, 1414, 1503, 1588)   # 1503 only for the C1 scramble
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
IDENT_BUD = 1.0e-8
U_RND = 0.5 * np.finfo(float).eps
CERT_INFL = 1.01

WIN_LO, WIN_HI, DG_PROF = 5.0, 60.0, 0.25
PROF_GS = np.arange(WIN_LO, WIN_HI + 1e-9, DG_PROF)
PROM_MIN = math.log(1.5)
MATCH_TOL = 0.5
W_CAP = 0.5
REFINE_LO, REFINE_HI, DG_REFINE = 18.0, 34.0, 0.125
REFINE_MOVE_TOL = 0.25
SHIFT_NULL = 2.5
CTRL_DG = 0.5
CTRL_DET_BAR = 0.25
GATE_DET, GATE_FP = 0.80, 0.20
PART_DET, PART_FACTOR = 0.40, 2.0
MECH_ZEROS = (21.022040, 32.935062)   # predeclared matched targets
MECH_OFF = (10.0, 28.0)               # predeclared off-zero points
MECH_DELTA = 0.004
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
LOCATOR_DESIGN = (
    BATTERY_V2_DESIGN
    + "|locator: W(gamma)=uncensored delta_mb on the extended grid "
      "(floor 4.02e-4, bisect 4); window [5,60] step 0.25; rungs "
      "M=1176,1414,1588; predicted ordinates = local maxima of "
      "log W with prominence >= ln(1.5); match tol 0.5; W capped "
      "0.5 on no-break|orientation fixed by parent diagnostics: "
      "peaks, not dips (on-ordinate 0.0112 vs off 0.0033)|controls: "
      "scramble M=1503 + Epstein M=640 at step 0.5 (det <= 0.25); "
      "shifted null +2.5 (collapse <= 1/3); refine [18,34] x2 "
      "(move <= 0.25)|gates: RESOLVES det>=0.8 & fp<=0.2 & C3 & "
      "C4; PARTIAL det>=0.4 & det>=2x shifted; else NULL"
)
LOC_HASH = hashlib.sha256(LOCATOR_DESIGN.encode()).hexdigest()


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


def detunes_v2(M, gamma):
    X = M * DGRID
    if BAND_LO <= gamma <= BAND_HI:
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
                                detunes_v2(M, float(g)))
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


def score(peaks, zeros, tol=MATCH_TOL):
    pg = np.array([p[0] for p in peaks]) if peaks else np.array([])
    matches = []
    for gz in zeros:
        if pg.size:
            k = int(np.argmin(np.abs(pg - gz)))
            if abs(pg[k] - gz) <= tol:
                matches.append((float(gz), float(pg[k]),
                                float(abs(pg[k] - gz))))
    det = len(matches) / len(zeros) if len(zeros) else float("nan")
    n_fp = sum(1 for p in pg
               if not len(zeros)
               or float(np.min(np.abs(np.asarray(zeros) - p))) > tol)
    fp = n_fp / len(pg) if pg.size else 0.0
    prec = float(np.median([m[2] for m in matches])) if matches \
        else float("nan")
    return det, fp, prec, matches, len(pg)


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
    print("PRIME.EXCLUSIONLADDER.06 -- zero locator "
          "(exclusion_zero_locator_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- freeze + wards + tower rebuild")
    v2h = hashlib.sha256(BATTERY_V2_DESIGN.encode()).hexdigest()
    check("S0.V2HASH battery v2 reused UNCHANGED: %s.. == %s.."
          % (v2h[:16], V2_HASH_CITED[:16]), v2h == V2_HASH_CITED)
    print("    LOCATOR DESIGN (frozen a priori): window [%g,%g] "
          "step %g; peaks of log W, prominence >= ln(1.5); match "
          "tol %g; zero tables enter SCORING only."
          % (WIN_LO, WIN_HI, DG_PROF, MATCH_TOL))
    print("    SHA-256: %s" % LOC_HASH)
    check("S0.AST no zeta-zero generator call (cached RvM list for "
          "scoring only; RNG only in C1)", ast_zero_firewall(__file__))
    d1 = json.load(open(os.path.join(_here,
                                     "zero_comb_cache_n2000.json")))
    d2 = json.load(open(os.path.join(_here, "c1_zero_ext_n2500.json")))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    zeros_win = [float(g) for g in gam_c
                 if WIN_LO <= g <= WIN_HI]
    check("S0.CACHE %d cached ordinates; K = %d true zeros in the "
          "window [%g, %g] (gamma_1 = %.4f)"
          % (len(gam_c), len(zeros_win), WIN_LO, WIN_HI,
             zeros_win[0]),
          len(gam_c) == 2500 and len(zeros_win) >= 10)
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
    print("\nS1 -- the width profiles W(gamma) (%d points, %d "
          "rungs)" % (len(PROF_GS), len(RUNG_MS)))
    profiles, peaks_of = {}, {}
    for M in RUNG_MS:
        t0 = time.time()
        profiles[M] = dense_profile(towers[M][:M], M, nrm_of[M],
                                    PROF_GS)
        peaks_of[M] = find_peaks(PROF_GS, profiles[M])
        n_cap = int(np.sum(profiles[M] >= W_CAP * (1 - 1e-12)))
        print("      X = %8.4f: W in [%.4f, %.4f], %d capped, %d "
              "prominent peaks (%.1f s)"
              % (M * DGRID, float(np.min(profiles[M])),
                 float(np.max(profiles[M])), n_cap,
                 len(peaks_of[M]), time.time() - t0))
    deep_m = RUNG_MS[-1]
    check("S1.REACH deepest profile fully uncensored above the "
          "floor and below the cap",
          float(np.min(profiles[deep_m])) > EXT2_DELTAS[0] * (1 + 1e-9)
          and float(np.max(profiles[deep_m])) < W_CAP * (1 - 1e-12))
    out_json = {"gammas": [float(g) for g in PROF_GS],
                "W": {str(M): [float(w) for w in profiles[M]]
                      for M in RUNG_MS},
                "peaks": {str(M): peaks_of[M] for M in RUNG_MS},
                "locator_hash": LOC_HASH}
    with open(os.path.join(_here,
                           "exclusion_zero_locator_profile.json"),
              "w") as fh:
        json.dump(out_json, fh)
    print("    profile data -> exclusion_zero_locator_profile.json")

    # ============================================================== S2
    print("\nS2 -- scoring (ordinates admissible HERE only)")
    res = {}
    for M in RUNG_MS:
        det, fp, prec, matches, n_pk = score(peaks_of[M], zeros_win)
        res[M] = (det, fp, prec, matches, n_pk)
        print("      X = %8.4f: peaks %2d | detection %4.0f%% "
              "(%d/%d) | false-pos %4.0f%% | precision %.3f"
              % (M * DGRID, n_pk, 100 * det, len(matches),
                 len(zeros_win), 100 * fp,
                 prec if np.isfinite(prec) else float("nan")))
    det_d, fp_d, prec_d, matches_d, npk_d = res[deep_m]
    print("    predicted-vs-true table (deepest rung, X = %.4f):"
          % (deep_m * DGRID))
    print("      %9s %10s %8s %6s" % ("gamma_pred", "prominence",
                                      "true", "|d|"))
    zt = np.asarray(zeros_win)
    for gp, pr in peaks_of[deep_m]:
        k = int(np.argmin(np.abs(zt - gp)))
        dd = abs(float(zt[k]) - gp)
        print("      %9.3f %10.3f %8s %6s"
              % (gp, pr,
                 ("%.3f" % zt[k]) if dd <= MATCH_TOL else "--",
                 ("%.3f" % dd) if dd <= MATCH_TOL else "FP"))
    missed = [float(z) for z in zeros_win
              if not any(abs(m[0] - z) < 1e-9 for m in matches_d)]
    if missed:
        print("      missed zeros: %s"
              % ", ".join("%.3f" % z for z in missed))
    precs = [(M * DGRID, res[M][2]) for M in RUNG_MS
             if np.isfinite(res[M][2])]
    if len(precs) >= 2:
        lx = np.log([p[0] for p in precs])
        ly = np.log([p[1] for p in precs])
        slope_p = float(np.polyfit(lx, ly, 1)[0])
        print("    precision-vs-depth: %s | log-log slope %.2f "
              "(grid floor %.3f -- precision at or near the grid "
              "step is grid-limited, typed)"
              % (", ".join("X=%.1f: %.3f" % p for p in precs),
                 slope_p, DG_PROF / 2.0))

    # ============================================================== S3
    print("\nS3 -- mechanism decomposition (measure, don't narrate)")
    cTd = towers[deep_m][:deep_m]
    mech_pts = []
    pg_d = np.array([p[0] for p in peaks_of[deep_m]]) \
        if peaks_of[deep_m] else np.array([])
    for gz in MECH_ZEROS:
        if pg_d.size:
            gp = float(pg_d[int(np.argmin(np.abs(pg_d - gz)))])
            mech_pts.append(("matched(%.2f)" % gz, gp))
        else:
            mech_pts.append(("matched(%.2f)" % gz, gz))
    for go in MECH_OFF:
        mech_pts.append(("off-zero", float(go)))
    for lab, g in mech_pts:
        det = detunes_v2(deep_m, g)
        d_mb, wit = boundary_scan(cTd, deep_m, nrm_of[deep_m], g,
                                  det)
        ql = quad_lags(deep_m, g, MECH_DELTA)[:deep_m]
        Qb, _ = np.linalg.qr(battery_B(deep_m, g, MECH_DELTA, det))
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        lam_p, _ = sub_lam(cTd + ql, Qb)
        broke = lam_p < -bud
        split_txt = ""
        if wit is not None and np.isfinite(d_mb):
            fr = witness_group_split(deep_m, g, float(d_mb), det,
                                     wit)
            kd = int(np.argmax(fr))
            split_txt = " | witness energy: dominant detune k = " \
                "%+d (frac %.2f)" % (kd - (len(det) // 2), fr[kd])
        print("      %-14s gamma = %7.3f: delta_mb = %.5f | at "
              "probe delta* = %.3f: lambda_min = %+.2e (%s)%s"
              % (lab, g, d_mb, MECH_DELTA, lam_p,
                 "BREAKS" if broke else "HOLDS", split_txt))
    print("    READING (typed from the data above): if the matched "
          "points HOLD at delta* while the off-zero points BREAK, "
          "the dip-in-sensitivity is the explicit-formula "
          "redundancy: a real zero near gamma makes the injected "
          "synthetic quadruple consistent with the comb, so the "
          "breakable margin shrinks and the boundary rises.")

    # ============================================================== C
    print("\nC -- controls")
    ctrl_gs = np.arange(WIN_LO, WIN_HI + 1e-9, CTRL_DG)

    rng = np.random.default_rng(SEED_SCRAMBLE)
    alpha_t = 0.5 * 1503 * DGRID
    u_scr = rng.uniform(0.0, 2.0 * alpha_t, size=masses_scr.size)
    c_scr = np.zeros(1503)
    tent_accumulate(c_scr, 1503, u_scr, masses_scr)
    tow_scr = srp.continuum_lags(1503) + c_scr
    lam_scr = full_min(tow_scr, 1503)
    T_scr = sla.toeplitz(tow_scr[:1503])
    nrm_scr = float(sla.norm(T_scr, 2))
    W_scr = dense_profile(tow_scr[:1503], 1503, nrm_scr, ctrl_gs)
    pk_scr = find_peaks(ctrl_gs, W_scr)
    det_s, _, _, _, npk_s = score(pk_scr, zeros_win)
    check("C1 scramble comb (lambda_min = %.2e, %d masses, seed "
          "%d): %d peaks, zeta-detection %.0f%% <= %.0f%% (or no "
          "peaks)" % (lam_scr, masses_scr.size, SEED_SCRAMBLE,
                      npk_s, 100 * det_s, 100 * CTRL_DET_BAR),
          npk_s == 0 or det_s <= CTRL_DET_BAR)

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
    T_ep = sla.toeplitz(tow_ep[:Me])
    nrm_ep = float(sla.norm(T_ep, 2))
    W_ep = dense_profile(tow_ep[:Me], Me, nrm_ep, ctrl_gs)
    pk_ep = find_peaks(ctrl_gs, W_ep)
    det_e, _, _, _, npk_e = score(pk_ep, zeros_win)
    check("C2 Epstein comb (lambda_min = %.2e, M = %d): %d peaks, "
          "zeta-detection %.0f%% <= %.0f%% (or no peaks) -- the "
          "locator must NOT track zeta ordinates on a different "
          "zero set" % (lam_ep, Me, npk_e, 100 * det_e,
                        100 * CTRL_DET_BAR),
          npk_e == 0 or det_e <= CTRL_DET_BAR)

    zeros_shift = [z + SHIFT_NULL for z in zeros_win
                   if WIN_LO <= z + SHIFT_NULL <= WIN_HI]
    det_sh, _, _, _, _ = score(peaks_of[deep_m], zeros_shift)
    shift_ok = det_sh <= det_d / 3.0 + 1e-12
    check("C3 shifted-window null (+%.1f, %d shifted targets): "
          "detection %.0f%% vs true %.0f%% -- must collapse to "
          "<= 1/3" % (SHIFT_NULL, len(zeros_shift), 100 * det_sh,
                      100 * det_d), shift_ok)

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
    check("C4 grid-artifact ward (subwindow [%g, %g] refined x2): "
          "%d/%d matched peaks reappear within %.2f"
          % (REFINE_LO, REFINE_HI, n_stable, len(sub_matches),
             REFINE_MOVE_TOL),
          len(sub_matches) >= 2 and n_stable == len(sub_matches))

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- verdict")
    print("=" * 78)
    grid_ok = len(sub_matches) >= 2 and n_stable == len(sub_matches)
    if det_d >= GATE_DET and fp_d <= GATE_FP and shift_ok \
            and grid_ok:
        verdict = "LOCATOR-RESOLVES"
    elif det_d >= PART_DET and det_d >= PART_FACTOR * det_sh:
        verdict = "LOCATOR-PARTIAL"
    else:
        verdict = "LOCATOR-NULL"
    print("\n  VERDICT: %s" % verdict)
    print("  locator hash: %s" % LOC_HASH[:16])
    print("  deepest rung: detection %.0f%% | false-pos %.0f%% | "
          "precision %.3f | shifted null %.0f%%"
          % (100 * det_d, 100 * fp_d, prec_d, 100 * det_sh))
    if FAILS:
        print("  TYPED FAILURES: %s" % ",".join(FAILS))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
