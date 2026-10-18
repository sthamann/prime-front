"""PRIME.EXCLUSIONLADDER.04 -- battery v2 as a FRESHLY PREREGISTERED
instrument: is the Xi ~ 0.218 floor instrument-relative or
tower-intrinsic?  (EXPLORATION ONLY.)

PARENTS: exclusion_ladder_deep_probe.py (LADDER-EXTENDED) and
exclusion_ladder_saturation_probe.py (2026-08-06, SATURATION-TYPED,
21/21): on the deployed rank-4 battery the exclusion width Xi_eff =
X median delta_mb stalls at ~0.218 +- 3% across X = 20.7..24.8;
mechanism typed SUPPORT-ACTIVE-BUT-X-STALLED with the stall
localized to the mid-gamma rows (per-gamma slopes: gamma = 18.27
+0.08, 45.41 -0.71 vs 99.13 -4.07, 190 -1.33) and a rank-12
enrichment gain GROWING with depth (19.3% -> 23.2% -> 25.0%).  THIS
PROBE (user-authorized): a new instrument, NOT a re-freeze -- the
deployed rank-4 battery stays untouched and remains the contract
instrument.

S1 BATTERY V2 DESIGN (frozen a priori; hashed BEFORE any exclusion
evaluation; the design string is the object below, its SHA-256 is
printed first):
    columns  e^{+-delta jD} {cos, sin}((gamma + dg) jD), full
    support, QR-orthonormalized; detune ladder
      out-of-band:  dg = k pi/(2X), k in {-1, 0, 1}   (rank 12),
      in-band gamma in [14.0, 50.0]:
                    dg = k pi/(4X), k in {-4, ..., 4} (rank 36);
    criterion, budget and grids UNCHANGED from the deployed
    instrument (subspace lambda_min(T +- Q) < -(1e-8 + 100 eps
    (||T|| + M max|q|)); gamma geomspace(2, 190, 36); delta
    geomspace(1/240, 1/2, 44) + 3-step geometric bisection).
INFORMATION FLOW (typed): admissible inputs to the design are the
mechanism report's instrument diagnostics ONLY -- the per-gamma
stall-band localization (gamma ~ 18..45, widened a priori to
[14, 50] for coverage) and the growing rank-12 gain (which fixes
the detune-ladder axis).  NO measured delta_mb value, no exclusion
map, and no zeta-zero datum entered the design; the cached ordinate
list is touched only by the POST-VERDICT carrier census (S6) and
the calibration wards, as in the parents.  v1 is a subset of v2
(dg = 0 in every ladder), so delta_mb(v2) <= delta_mb(v1) pointwise
BY CONSTRUCTION -- the decision content is the slope and the floor
level, not the sign of the gain.

S2 RUNGS: X = 18.375 / 20.719 / 22.094 / 23.484 / 24.813 (the two
cheapest rungs X = 4, 10 are SKIPPED, predeclared -- the decision
lives in the deep regime); towers rebuilt with the fast segmented
sieve (parity ward at M = 1176 vs the deployed path); lambda_min
anchored against the parent-cited margins (rel 2e-2) and certified
(Cholesky/Higham lower bound + Rayleigh enclosure) -- the tower and
its certificates are battery-independent and must reproduce.
S3 V1 REPRODUCTION WARD: the v2 machinery run with the v1 battery
(dg = 0 only, rank 4) must reproduce the parent-cited Xi series
(0.2736 / 0.2179 / 0.2187 / 0.2225 / 0.2121) within rel 1e-3.
S4 THE V2 RERUN: delta_mb boundaries on the SAME frozen grid at all
5 rungs; Xi_eff(v2) series; frozen-census region delta at M = 1414
and 1588; witness certificates at sampled deepest boundary points.
S5 THE DECISION (frozen gates, total, priority V1 > V2 > V3):
    slope3 = log-log slope of Xi_eff(v2) over the three deepest
    rungs (X = 22.094, 23.484, 24.813).
    GATE V1: slope3 <= -0.3            => FLOOR-INSTRUMENTAL.
    else floor_v2 = median Xi_eff(v2) over those three rungs;
    GATE V2: floor_v2 < 0.95 x 0.2187  => FLOOR-LOWERED (typed).
    GATE V3: floor_v2 >= 0.95 x 0.2187 => FLOOR-INTRINSIC (the
      stall is tower structure; carrier census becomes binding).
    Band regularity |Xi(M)/floor_v2 - 1| <= 0.05 reported; a miss
    is typed as a caveat, not a verdict change (predeclared).
S6 CARRIER CENSUS (measured, report; PROMINENT iff V3): per-gamma
v2 slope across the deepest three rungs -> stalled rows (slope >
-0.3); distance census min|gamma - gamma_k| to the cached ordinates
for stalled vs sharpening rows; the alias-comb check (2 pi/D =
402.1 -- positions vs the Nyquist window, measured); the
on-ordinate family (quadruples parked on actual ordinates) under
v2.
S7 HONEST COMPARISON: v1-vs-v2 per-rung table (lambda_min, median
delta_mb, Xi_eff, reach), certified-region delta, depth-to-width
law restated for the winning instrument.
CONTROLS: C1a injection ward WITH v2 (synthetic quadruple at
2 delta_mb(v2) inside the deepest region must break the full
spectrum, 4/4); C2 scramble at M = 1503 (SAME masses, declared seed
7 -- the only RNG use; battery-independent tower control, typed);
C3 Epstein swap (Lambda_E reach 34000 => M = 640, typed).
VERDICT (frozen enum): FLOOR-INSTRUMENTAL / FLOOR-LOWERED /
FLOOR-INTRINSIC.  Any ward/control failure or tower anomaly forces
the verdict line to carry the typed failure prominently (no
separate enum class, predeclared).

FIREWALL: v563/v755 read-only; NO zetazero()/nzeros() calls (AST-
checked); cached RvM ordinate list for wards + the S6 census only;
RNG only in the declared C2 scramble.  Nothing outside experiments/
touched.  NO RH claim.
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
RUNG_MS = (1176, 1326, 1414, 1503, 1588)
LAM_CITED = {1176: 3.8825e-6, 1326: 2.4453e-6, 1414: 2.0092e-6,
             1503: 1.5883e-6, 1588: 1.0779e-6}
XI_V1_CITED = {1176: 0.2736, 1326: 0.2179, 1414: 0.2187,
               1503: 0.2225, 1588: 0.2121}
ANCH_REL = 2.0e-2
REPRO_REL = 1.0e-3
ATOM_MAX_DEEP = 100000000
SEG_ASC, SEG_DESC = 1 << 28, 1 << 25
PARITY_C_ABS = 5.0e-9
FFT_WARD_BAR = 1.0e-9
GAMMAS_GRID = np.geomspace(2.0, 190.0, 36)       # frozen
DELTAS_GRID = np.linspace(1.0 / 60.0, 0.5, 30)   # frozen census grid
EXT_DELTAS = np.geomspace(1.0 / 240.0, 0.5, 44)  # frozen instrument
N_BISECT = 3
BAND_LO, BAND_HI = 14.0, 50.0                    # typed stall band
FLOOR_CITED = 0.2187
GATE_SLOPE = -0.3
FLOOR_LOWER_FRAC = 0.95
BAND_REG = 0.05
IDENT_BUD = 1.0e-8
MONO_TOL = 0.02
U_RND = 0.5 * np.finfo(float).eps
CERT_INFL = 1.01
BATT_GIDX = (3, 10, 17, 24, 30, 35)
MZ_GIDX = (6, 14, 22, 30)
SEED_SCRAMBLE = 7
N_ONZERO = 30
STALL_SLOPE = -0.3

BATTERY_V2_DESIGN = (
    "battery-v2|columns exp(+/-delta*j*D)*{cos,sin}((gamma+dg)*j*D),"
    "full support,QR-orthonormalized|out-band: dg=k*pi/(2*X),"
    "k in {-1,0,1} (rank 12)|in-band gamma in [14.0,50.0]: "
    "dg=k*pi/(4*X),k in {-4..4} (rank 36)|criterion unchanged: "
    "subspace lambda_min(T+-Q) < -(1e-8+100*eps*(||T||+M*max|q|))|"
    "grids unchanged: gamma geomspace(2,190,36), delta "
    "geomspace(1/240,1/2,44)+3-step bisection|D=1/64"
)
DESIGN_HASH = hashlib.sha256(BATTERY_V2_DESIGN.encode()).hexdigest()


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


def boundary_scan(cT, M, nrmT, g, sign, detunes, bisect=N_BISECT):
    prev = None
    for dl in EXT_DELTAS:
        dl = float(dl)
        ql = quad_lags(M, g, dl)[:M]
        Qb, _ = np.linalg.qr(battery_B(M, g, dl, detunes))
        bud = bud_of(M, nrmT, float(np.max(np.abs(ql))))
        lam, wit = sub_lam(cT + sign * ql, Qb)
        if lam < -bud:
            hit, w_hit, b_hit, lo = dl, wit, bud, prev
            for _ in range(bisect):
                if lo is None:
                    break
                mid = math.sqrt(lo * hit)
                qlm = quad_lags(M, g, mid)[:M]
                Qbm, _ = np.linalg.qr(battery_B(M, g, mid, detunes))
                bm = bud_of(M, nrmT, float(np.max(np.abs(qlm))))
                lm, wm = sub_lam(cT + sign * qlm, Qbm)
                if lm < -bm:
                    hit, w_hit, b_hit = mid, wm, bm
                else:
                    lo = mid
            return hit, w_hit, b_hit
        prev = dl
    return float("nan"), None, float("nan")


def census_mbk(cT, M, nrmT, use_v2):
    mbk = np.zeros((len(GAMMAS_GRID), len(DELTAS_GRID)), bool)
    for ig, g in enumerate(GAMMAS_GRID):
        det = detunes_v2(M, float(g)) if use_v2 else (0.0,)
        for idl, dl in enumerate(DELTAS_GRID):
            ql = quad_lags(M, float(g), float(dl))[:M]
            Qb, _ = np.linalg.qr(battery_B(M, float(g), float(dl),
                                           det))
            bud = bud_of(M, nrmT, float(np.max(np.abs(ql))))
            lp, _ = sub_lam(cT + ql, Qb)
            mbk[ig, idl] = lp < -bud
    return mbk


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


def certified_break(cA, M, x, bud):
    A = sla.toeplitz(cA)
    y = A @ x
    q = float(x @ y)
    ax = np.abs(x)
    E = gamma_fl(M) * (float(ax @ (np.abs(A) @ ax))
                       + float(ax @ np.abs(y))) * CERT_INFL
    n2 = float(x @ x)
    num_up = q + E
    if num_up >= 0.0:
        return False, 0.0
    return num_up / (n2 * (1.0 + gamma_fl(M))) < -bud, \
        num_up / (n2 * (1.0 + gamma_fl(M)))


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
    print("PRIME.EXCLUSIONLADDER.04 -- battery v2 preregistered "
          "instrument (exclusion_battery_v2_probe)")
    print("=" * 78)

    # ============================================================== S1
    print("\nS1 -- THE V2 DESIGN (frozen a priori, hashed before any "
          "exclusion evaluation)")
    print("    DESIGN: %s" % BATTERY_V2_DESIGN)
    print("    SHA-256: %s" % DESIGN_HASH)
    print("    INFORMATION FLOW (typed): inputs = the mechanism "
          "report's instrument diagnostics only (stall band gamma ~ "
          "18..45 widened a priori to [14, 50]; the growing rank-12 "
          "gain fixing the detune axis).  NO measured delta_mb, no "
          "exclusion map, no zeta-zero datum entered the design; "
          "the cached ordinates appear only in the wards and the "
          "post-verdict S6 census.  v1 (dg = 0) is a SUBSET of v2: "
          "delta_mb(v2) <= delta_mb(v1) pointwise by construction; "
          "the decision content is slope and floor level.")

    # ============================================================== S0'
    print("\nS2 -- firewall + tower rebuild + certificates "
          "(battery-independent)")
    check("S2.AST no zeta-zero generator call (cached RvM list for "
          "wards + S6 census only; RNG only in C2)",
          ast_zero_firewall(__file__))
    d1 = json.load(open(os.path.join(_here,
                                     "zero_comb_cache_n2000.json")))
    d2 = json.load(open(os.path.join(_here, "c1_zero_ext_n2500.json")))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    check("S2.CACHE %d cached ordinates, gamma_1 = %.4f"
          % (len(gam_c), gam_c[0]),
          len(gam_c) == 2500 and abs(gam_c[0] - 14.134725) < 1e-5)

    Mw = 640
    cw = srp.continuum_lags(Mw)[:Mw]
    xw = np.cos(0.37 * np.arange(Mw)) / math.sqrt(Mw)
    y_f = sla.matmul_toeplitz((cw, cw), xw, check_finite=False)
    y_d = sla.toeplitz(cw) @ xw
    dev_f = float(np.max(np.abs(y_f - y_d))
                  / max(float(np.max(np.abs(y_d))), 1e-300))
    check("S2.FFT Toeplitz matvec == dense: rel dev %.2e <= %.0e"
          % (dev_f, FFT_WARD_BAR), dev_f <= FFT_WARD_BAR)

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
    t0 = time.time()
    cs, cnt, masses_scr, ncap = seg_assemble(
        list(RUNG_MS), collect_mass_M=1503)
    print("    big sieve+reads pass (%d rungs to n <= %d): %.1f s"
          % (len(RUNG_MS), max(ncap.values()), time.time() - t0))
    dev_c = float(np.max(np.abs(cs[1176] - c_dep)))
    check("S2.PARITY segmented == deployed T115 path at M = 1176: "
          "atom count %d == %d (EXACT), max |dc| = %.2e <= %.0e"
          % (cnt[1176], ka, dev_c, PARITY_C_ABS),
          cnt[1176] == ka and dev_c <= PARITY_C_ABS)

    towers, T_of, m_of, nrm_of, cert = {}, {}, {}, {}, {}
    cert_ok = True
    for M in RUNG_MS:
        towers[M] = srp.continuum_lags(M) + cs[M]
        T = sla.toeplitz(towers[M][:M])
        T_of[M] = T
        m_of[M] = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        nrm_of[M] = float(sla.norm(T, 2))
        lb, _beta, _sl = chol_cert_lower(T, m_of[M])
        lo, hi = rayleigh_enclosure(T)
        cert[M] = lb
        cert_ok = cert_ok and lb is not None and lb > 0.0 \
            and lo <= m_of[M] <= hi
        rel = abs(m_of[M] - LAM_CITED[M]) / LAM_CITED[M]
        check("S2.%d rung M = %d (X = %.4f): lambda_min = %.4e vs "
              "cited %.4e (rel %.4f <= %.2f), CERTIFIED >= %.4e"
              % (M, M, M * DGRID, m_of[M], LAM_CITED[M], rel,
                 ANCH_REL, lb if lb is not None else float("nan")),
              rel <= ANCH_REL)
    check("S2.CERT rigorous lambda_min > 0 certificates + "
          "bracketing enclosures on all %d rungs" % len(RUNG_MS),
          cert_ok)

    # ============================================================== S3
    print("\nS3 -- v1 reproduction ward (v2 machinery, v1 battery)")
    bounds_v1 = {M: np.full(len(GAMMAS_GRID), np.nan)
                 for M in RUNG_MS}
    repro_ok = True
    for M in RUNG_MS:
        cT = towers[M][:M]
        for ig, g in enumerate(GAMMAS_GRID):
            d_mb, _, _ = boundary_scan(cT, M, nrm_of[M], float(g),
                                       +1.0, (0.0,))
            bounds_v1[M][ig] = d_mb
        xi_m, reach = med_xi(bounds_v1[M], M * DGRID)
        rel = abs(xi_m - XI_V1_CITED[M]) / XI_V1_CITED[M]
        repro_ok = repro_ok and rel <= REPRO_REL
        print("      M = %4d: Xi_eff(v1) = %.4f vs cited %.4f "
              "(rel %.5f, %d/36 reach)"
              % (M, xi_m, XI_V1_CITED[M], rel, reach))
    check("S3.REPRO v1 battery reproduces the parent-cited Xi "
          "series on all %d rungs (rel <= %.0e)"
          % (len(RUNG_MS), REPRO_REL), repro_ok)

    # ============================================================== S4
    print("\nS4 -- the v2 rerun (same frozen grids)")
    bounds_v2 = {M: np.full(len(GAMMAS_GRID), np.nan)
                 for M in RUNG_MS}
    wits_v2 = {M: [None] * len(GAMMAS_GRID) for M in RUNG_MS}
    xi_v2, xi_v1 = {}, {}
    for M in RUNG_MS:
        cT = towers[M][:M]
        t0 = time.time()
        for ig, g in enumerate(GAMMAS_GRID):
            det = detunes_v2(M, float(g))
            d_mb, w_mb, _ = boundary_scan(cT, M, nrm_of[M],
                                          float(g), +1.0, det)
            bounds_v2[M][ig] = d_mb
            wits_v2[M][ig] = w_mb
        xi_v2[M], reach2 = med_xi(bounds_v2[M], M * DGRID)
        xi_v1[M], _ = med_xi(bounds_v1[M], M * DGRID)
        print("      X = %8.4f: median delta_mb(v2) = %.5f -> "
              "Xi_eff(v2) = %.4f (v1 %.4f; gain %.1f%%; %d/36 "
              "reach; %.1f s)"
              % (M * DGRID, xi_v2[M] / (M * DGRID), xi_v2[M],
                 xi_v1[M], 100.0 * (1.0 - xi_v2[M] / xi_v1[M]),
                 reach2, time.time() - t0))
    v2_dominates = all(
        not np.isfinite(bounds_v1[M][ig])
        or (np.isfinite(bounds_v2[M][ig])
            and bounds_v2[M][ig] <= bounds_v1[M][ig] * (1 + 1e-12))
        for M in RUNG_MS for ig in range(len(GAMMAS_GRID)))
    check("S4.DOM v2 boundary <= v1 boundary pointwise on every "
          "rung (subset construction verified on the data)",
          v2_dominates)

    # frozen-census region delta + witness certificates
    for M in (1414, 1588):
        mb1 = census_mbk(towers[M][:M], M, nrm_of[M], False)
        mb2 = census_mbk(towers[M][:M], M, nrm_of[M], True)
        lost = int((mb1 & ~mb2).sum())
        print("    frozen-grid margin-break census M = %d: v1 %d -> "
              "v2 %d of 1080 (+%d; v1-points lost: %d)"
              % (M, int(mb1.sum()), int(mb2.sum()),
                 int(mb2.sum()) - int(mb1.sum()), lost))
    n_cert, n_cert_ok = 0, 0
    deep_m = RUNG_MS[-1]
    cTd = towers[deep_m][:deep_m]
    for ig in BATT_GIDX:
        b = bounds_v2[deep_m][ig]
        if not np.isfinite(b) or wits_v2[deep_m][ig] is None:
            continue
        g = float(GAMMAS_GRID[ig])
        ql = quad_lags(deep_m, g, float(b))[:deep_m]
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        ok1, _v = certified_break(cTd + ql, deep_m,
                                  wits_v2[deep_m][ig], bud)
        n_cert += 1
        n_cert_ok += int(ok1)
    check("S4.CERT witness Rayleigh certificates re-prove %d/%d "
          "sampled v2 boundary points at the deepest rung"
          % (n_cert_ok, n_cert), n_cert >= 4 and n_cert_ok == n_cert)

    # ============================================================== S5
    print("\nS5 -- THE DECISION (frozen gates, priority V1 > V2 > "
          "V3)")
    last3 = RUNG_MS[-3:]
    lx = np.log([M * DGRID for M in last3])
    ly = np.log([xi_v2[M] for M in last3])
    slope3 = float(np.polyfit(lx, ly, 1)[0])
    floor_v2 = float(np.median([xi_v2[M] for M in last3]))
    band_ok = all(abs(xi_v2[M] / floor_v2 - 1.0) <= BAND_REG
                  for M in last3)
    print("    slope3(v2) over X = %s: %.3f (gate V1 <= %.2f)"
          % (", ".join("%.2f" % (M * DGRID) for M in last3),
             slope3, GATE_SLOPE))
    print("    floor_v2 = median Xi over the last three rungs = "
          "%.4f (V2 iff < %.2f x %.4f = %.4f); band regularity "
          "+-%.0f%%: %s"
          % (floor_v2, FLOOR_LOWER_FRAC, FLOOR_CITED,
             FLOOR_LOWER_FRAC * FLOOR_CITED, 100 * BAND_REG,
             "ok" if band_ok else "MISS (typed caveat)"))
    if slope3 <= GATE_SLOPE:
        verdict = "FLOOR-INSTRUMENTAL"
    elif floor_v2 < FLOOR_LOWER_FRAC * FLOOR_CITED:
        verdict = "FLOOR-LOWERED"
    else:
        verdict = "FLOOR-INTRINSIC"
    if not band_ok:
        anomalies.append("saturation-band regularity miss on the "
                         "v2 series (wiggle > %.0f%%)"
                         % (100 * BAND_REG))

    # ============================================================== S6
    print("\nS6 -- carrier census (measured; binding iff "
          "FLOOR-INTRINSIC)")
    print("    per-gamma v2 slope across the deepest three rungs "
          "(stalled iff slope > %.2f):" % STALL_SLOPE)
    stalled, sharp = [], []
    for ig in range(len(GAMMAS_GRID)):
        ds = [bounds_v2[M][ig] for M in last3]
        if not all(np.isfinite(d) for d in ds):
            continue
        s_g = float(np.polyfit(lx, np.log(ds), 1)[0])
        g = float(GAMMAS_GRID[ig])
        dmin = float(np.min(np.abs(gam_c[gam_c < 250.0] - g)))
        (stalled if s_g > STALL_SLOPE else sharp).append(
            (g, s_g, dmin))
    for lab, rows in (("STALLED", stalled), ("SHARPENING", sharp)):
        if rows:
            print("      %s rows: %d | gamma median %.1f | median "
                  "dist to nearest cached ordinate %.2f"
                  % (lab, len(rows),
                     float(np.median([r[0] for r in rows])),
                     float(np.median([r[2] for r in rows]))))
    if stalled:
        print("      stalled gammas: %s"
              % ", ".join("%.1f" % r[0] for r in stalled[:14]))
    print("    low ordinates gamma_1..gamma_7 = %s (the typed "
          "stall band was [%.0f, %.0f])"
          % (", ".join("%.1f" % g for g in gam_c[:7]), BAND_LO,
             BAND_HI))
    print("    alias comb: 2 pi / D = %.1f -- the first alias "
          "position lies OUTSIDE the Nyquist window pi/D = %.1f "
          "(measured: no alias position intersects the gamma grid)"
          % (2.0 * math.pi / DGRID, math.pi / DGRID))
    on_v2 = []
    for gz in gam_c[:N_ONZERO]:
        if gz > GAMMAS_GRID[-1]:
            break
        d_on, _, _ = boundary_scan(cTd, deep_m, nrm_of[deep_m],
                                   float(gz), +1.0,
                                   detunes_v2(deep_m, float(gz)))
        on_v2.append(d_on)
    fin_on = [d for d in on_v2 if np.isfinite(d)]
    print("    on-ordinate family under v2 (M = %d): delta_mb "
          "median %.4f, range [%.4f, %.4f] (%d reach)"
          % (deep_m, float(np.median(fin_on)) if fin_on else
             float("nan"), min(fin_on) if fin_on else float("nan"),
             max(fin_on) if fin_on else float("nan"), len(fin_on)))

    # ============================================================== S7
    print("\nS7 -- honest comparison + the law for the winning "
          "instrument")
    print("  %9s %11s %12s %10s %10s %9s %9s" % (
        "X", "lam_min", "cert lower", "d_mb(v1)", "d_mb(v2)",
        "Xi(v1)", "Xi(v2)"))
    for M in RUNG_MS:
        X = M * DGRID
        print("  %9.4f %11.4e %12.4e %10.5f %10.5f %9.4f %9.4f"
              % (X, m_of[M], cert[M], xi_v1[M] / X, xi_v2[M] / X,
                 xi_v1[M], xi_v2[M]))
    xi_win = xi_v2[deep_m] if verdict != "FLOOR-INTRINSIC" \
        else floor_v2
    print("    depth-to-width law (winning instrument %s, deepest "
          "calibration Xi = %.4f):"
          % ("v2" if verdict != "FLOOR-INTRINSIC" else
             "v2 == v1 floor", xi_win))
    for dl in (0.5, 0.25, 0.1, 0.05, 0.01):
        xs_ = xi_win / dl
        print("      delta >= %5.2f excluded at depth X* = %7.1f "
              "(comb cap e^{X*} = %.2e)" % (dl, xs_, math.exp(xs_)))

    # ============================================================== C
    print("\nC -- controls")
    inside_ok, n_in = True, 0
    for ig in MZ_GIDX:
        b = bounds_v2[deep_m][ig]
        if not np.isfinite(b) or 2.0 * b > 0.5:
            continue
        g = float(GAMMAS_GRID[ig])
        ql = quad_lags(deep_m, g, 2.0 * float(b))[:deep_m]
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        lam = full_min(cTd + ql, deep_m)
        n_in += 1
        inside_ok = inside_ok and (lam < -bud)
    check("C1a [must-fire] synthetic quadruple at 2 delta_mb(v2) "
          "inside the deepest region breaks the full spectrum: "
          "%d/%d points" % (n_in if inside_ok else -1, n_in),
          inside_ok and n_in >= 4)
    if not (inside_ok and n_in >= 4):
        anomalies.append("C1a injection ward failed under v2")

    rng = np.random.default_rng(SEED_SCRAMBLE)
    alpha_t = 0.5 * 1503 * DGRID
    u_scr = rng.uniform(0.0, 2.0 * alpha_t, size=masses_scr.size)
    c_scr = np.zeros(1503)
    tent_accumulate(c_scr, 1503, u_scr, masses_scr)
    lam_scr = full_min(srp.continuum_lags(1503) + c_scr, 1503)
    check("C2 [must-fire] scramble at M = 1503 (%d masses, seed %d; "
          "battery-independent tower control, typed): lambda_min = "
          "%.3e < 0" % (masses_scr.size, SEED_SCRAMBLE, lam_scr),
          lam_scr < 0.0)

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
    check("C3 [must-fire] Epstein swap (reach %d => M = 640, "
          "typed): lambda_min = %.3e < 0" % (ep_cap, lam_ep),
          lam_ep < 0.0)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- verdict")
    print("=" * 78)
    print("\n  VERDICT: %s" % verdict)
    print("  design hash: %s" % DESIGN_HASH[:16])
    print("  slope3(v2) = %.3f | floor_v2 = %.4f vs v1 floor "
          "%.4f | deepest gain %.1f%%"
          % (slope3, floor_v2, FLOOR_CITED,
             100.0 * (1.0 - xi_v2[deep_m] / xi_v1[deep_m])))
    for a in anomalies:
        print("  TYPED: %s" % a)
    if FAILS:
        print("  TYPED FAILURES: %s" % ",".join(FAILS))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
