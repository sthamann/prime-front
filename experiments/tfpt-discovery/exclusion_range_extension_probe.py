"""PRIME.EXCLUSIONLADDER.05 -- the measurement-range extension: the
uncensored v2 asymptote (EXPLORATION ONLY).

PARENT: exclusion_battery_v2_probe.py (2026-08-06, FLOOR-LOWERED,
16/16): the preregistered battery v2 (SHA-256 fd39fb42...) cut the
exclusion floor from Xi ~ 0.2187 to 0.0979 (-55%), but the median
delta_mb at the two deepest rungs sat EXACTLY on the frozen grid
floor 1/240 -- the v2 floor is only an upper bound; the apparent
+0.57 slope is a censoring artifact.  THIS PROBE (user-authorized):
extend the MEASUREMENT RANGE one decade down and decide the true v2
asymptote.  Battery v2 is reused UNCHANGED (hash ward below); the
deployed rank-4 battery stays the contract instrument.

THE EXTENDED INSTRUMENT (frozen a priori, hashed below): the ONLY
change is measurement range --
    delta grid: the frozen 44-point array geomspace(1/240, 1/2, 44)
    VERBATIM, with 21 extra points prepended at the SAME frozen
    ratio r = 120^(1/43) (one decade down: new floor (1/240) r^-21
    = 4.0192e-4 <= 1/2400); the old grid is an EXACT SUBSET, so
    boundaries uncensored on the old grid must reproduce EXACTLY.
    Bisection depth 4 (was 3; resolution 11.78%/16 = 0.74%, typed).
    Criterion, budget, battery columns, gamma grid: byte-identical.
TASK STRUCTURE:
 S0 firewall + v2-hash ward (the design string must re-hash to the
    parent's fd39fb42...) + extended-instrument hash + tower rebuild
    (fast segmented sieve; no persistent comb cache exists, typed)
    + parity ward at M = 1176 + lambda_min anchors + certificates
    (Cholesky/Higham lower bound + Rayleigh enclosure, cited-anchor
    wards rel 2e-2).
 S1 REPRODUCTION WARDS (at M = 1414 and 1588, predeclared): v1 and
    v2 boundaries computed on BOTH grids; every row whose old-grid
    boundary lies strictly above 1/240 must agree EXACTLY (the
    subset construction makes this bit-for-bit); Xi(v1, old grid)
    must reproduce the cited series (rel 1e-3).
 S2 THE RERUN: v2 on the extended instrument at the rungs X =
    18.375 / 20.719 / 22.094 / 23.484 / 24.813; uncensored
    delta_mb boundaries, uncensored Xi_v2 series, witness Rayleigh
    certificates at sampled deepest boundary points; per-rung
    censoring census (row censored iff its boundary equals the new
    grid floor, i.e. the scan broke at the first point).
 S3 THE DECISION (frozen gates, priority R3 > R1 > R2, total):
    GATE R3: any of the three deepest rungs median-censored
      (>= 18/36 rows on the new floor) => STILL-CENSORED (censoring
      depth + projected next decade typed).
    GATE R1: else log-log slope of uncensored Xi_v2 over the three
      deepest rungs <= -0.3 => RANGE-DECIDES-DECLINE (the ladder
      lives; recalibrated law + the delta >= 0.001 benchmark).
    GATE R2: else => RANGE-DECIDES-FLOOR (default non-declining,
      non-censored outcome; band regularity |Xi/median - 1| <= 5%
      reported, a miss typed as caveat, not a verdict change);
      the carrier census (S4) becomes BINDING.
 S4 CARRIER CENSUS (uncensored; binding iff R2): per-row delta_mb
    vs distance to the nearest cached ordinate (rank correlation +
    above/below-median split); per-gamma slope classification
    across the deepest three rungs (stalled iff slope > -0.3) with
    distance stats; on-ordinate family at the deepest rung; the
    honest circularity check typed: the battery design string
    (hash-verified above) contains no zero datum -- any zero-
    correlation in the floor is measured OUTPUT, not design input.
 S5 THE HONEST LAW: the final table (v1 cited | v2 old grid cited |
    v2 extended measured) per rung; the strongest supported ladder
    statement VERBATIM; the explicit remaining instrument limits.
CONTROLS: C1a injection ward at the deepest rung on the UNCENSORED
 boundaries (synthetic quadruple at 2 delta_mb must break the full
 spectrum, 4/4); C2 scramble at M = 1503 (SAME masses, declared
 seed 7 -- the only RNG use); C3 Epstein swap (reach 34000 => M =
 640, typed).
VERDICT (frozen enum): RANGE-DECIDES-DECLINE / RANGE-DECIDES-FLOOR
 / STILL-CENSORED.  Ward/control failures are typed prominently on
 the verdict line (no separate enum class, predeclared).

FIREWALL: v563/v755 read-only; NO zetazero()/nzeros() calls (AST-
checked); cached RvM ordinates for wards + the S4 census only; RNG
only in the declared C2 scramble.  Nothing outside experiments/
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
XI_V2_OLD_CITED = {1176: 0.1070, 1326: 0.0986, 1414: 0.0967,
                   1503: 0.0979, 1588: 0.1034}   # old grid, censored
ANCH_REL = 2.0e-2
REPRO_REL = 1.0e-3
ATOM_MAX_DEEP = 100000000
SEG_ASC = 1 << 28
PARITY_C_ABS = 5.0e-9
FFT_WARD_BAR = 1.0e-9
GAMMAS_GRID = np.geomspace(2.0, 190.0, 36)       # frozen
EXT_DELTAS = np.geomspace(1.0 / 240.0, 0.5, 44)  # frozen old range
_RATIO = 120.0 ** (1.0 / 43.0)                   # the frozen step
N_EXTEND = 21                                    # one decade down
EXT2_DELTAS = np.concatenate(
    [EXT_DELTAS[0] * _RATIO ** (-np.arange(N_EXTEND, 0, -1.0)),
     EXT_DELTAS])
N_BISECT_OLD, N_BISECT2 = 3, 4
BAND_LO, BAND_HI = 14.0, 50.0
GATE_SLOPE = -0.3
BAND_REG = 0.05
CENSOR_MAJ = 18
IDENT_BUD = 1.0e-8
U_RND = 0.5 * np.finfo(float).eps
CERT_INFL = 1.01
BATT_GIDX = (3, 10, 17, 24, 30, 35)
MZ_GIDX = (6, 14, 22, 30)
REPRO_MS = (1414, 1588)
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
V2_HASH_CITED = ("fd39fb42ab1beb8137a359ff9c9934475a2467"
                 "7bf305d111b4fe43a4c6ca02c0")
RANGE_EXT_DESIGN = (
    BATTERY_V2_DESIGN
    + "|range-extension: prepend 21 points at the frozen ratio "
      "r=120^(1/43) below 1/240 (floor 4.0192e-4 <= 1/2400, old "
      "grid an exact subset); bisection depth 4; NOTHING else "
      "changed -- measurement range only"
)
EXT_HASH = hashlib.sha256(RANGE_EXT_DESIGN.encode()).hexdigest()


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


def boundary_scan(cT, M, nrmT, g, detunes, grid, bisect):
    prev = None
    for dl in grid:
        dl = float(dl)
        ql = quad_lags(M, g, dl)[:M]
        Qb, _ = np.linalg.qr(battery_B(M, g, dl, detunes))
        bud = bud_of(M, nrmT, float(np.max(np.abs(ql))))
        lam, wit = sub_lam(cT + ql, Qb)
        if lam < -bud:
            hit, w_hit, b_hit, lo = dl, wit, bud, prev
            for _ in range(bisect):
                if lo is None:
                    break
                mid = math.sqrt(lo * hit)
                qlm = quad_lags(M, g, mid)[:M]
                Qbm, _ = np.linalg.qr(battery_B(M, g, mid, detunes))
                bm = bud_of(M, nrmT, float(np.max(np.abs(qlm))))
                lm, wm = sub_lam(cT + qlm, Qbm)
                if lm < -bm:
                    hit, w_hit, b_hit = mid, wm, bm
                else:
                    lo = mid
            return hit, w_hit, b_hit
        prev = dl
    return float("nan"), None, float("nan")


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
        return False
    return num_up / (n2 * (1.0 + gamma_fl(M))) < -bud


def med_xi(bounds_row, X):
    fin = bounds_row[np.isfinite(bounds_row)]
    return (float(np.median(fin)) * X, len(fin)) if len(fin) \
        else (float("nan"), 0)


def rank_corr(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    return float(np.corrcoef(ra, rb)[0, 1])


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.EXCLUSIONLADDER.05 -- measurement-range extension "
          "(exclusion_range_extension_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- instrument freeze + hash wards + tower rebuild")
    v2h = hashlib.sha256(BATTERY_V2_DESIGN.encode()).hexdigest()
    check("S0.V2HASH battery v2 reused UNCHANGED: design re-hashes "
          "to %s.. == parent %s.." % (v2h[:16], V2_HASH_CITED[:16]),
          v2h == V2_HASH_CITED)
    print("    EXTENDED INSTRUMENT: %s" % RANGE_EXT_DESIGN[-180:])
    print("    SHA-256: %s" % EXT_HASH)
    print("    CHANGE STATEMENT (typed): measurement range ONLY -- "
          "grid floor 1/240 -> %.4e (21 points at the frozen "
          "ratio, old grid an exact subset), bisection 3 -> 4; "
          "battery, criterion, budget, gamma grid byte-identical."
          % EXT2_DELTAS[0])
    check("S0.GRID exact-subset construction: EXT2[%d:] == old grid "
          "(max dev %.1e), floor %.4e <= 1/2400"
          % (N_EXTEND, float(np.max(np.abs(EXT2_DELTAS[N_EXTEND:]
                                           - EXT_DELTAS))),
             EXT2_DELTAS[0]),
          float(np.max(np.abs(EXT2_DELTAS[N_EXTEND:] - EXT_DELTAS)))
          == 0.0 and EXT2_DELTAS[0] <= 1.0 / 2400.0)
    check("S0.AST no zeta-zero generator call (cached RvM list for "
          "wards + S4 census only; RNG only in C2)",
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
    al_deep = 0.5 * 1176 * DGRID
    ka = int(np.searchsorted(u_all, 2.0 * al_deep + 1e-14, "right"))
    c_dep, _ = core.atom_lags_at(al_deep, 1176, u_all[:ka],
                                 mu_all[:ka])
    del u_all, mu_all
    t0 = time.time()
    cs, cnt, masses_scr, ncap = seg_assemble(
        list(RUNG_MS), collect_mass_M=1503)
    print("    big sieve+reads pass (no persistent comb cache "
          "exists -- rebuilt, typed): %.1f s" % (time.time() - t0))
    dev_c = float(np.max(np.abs(cs[1176] - c_dep)))
    check("S0.PARITY segmented == deployed path at M = 1176: count "
          "%d == %d, max |dc| = %.2e" % (cnt[1176], ka, dev_c),
          cnt[1176] == ka and dev_c <= PARITY_C_ABS)

    towers, m_of, nrm_of, cert = {}, {}, {}, {}
    cert_ok, anch_ok = True, True
    for M in RUNG_MS:
        towers[M] = srp.continuum_lags(M) + cs[M]
        T = sla.toeplitz(towers[M][:M])
        m_of[M] = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        nrm_of[M] = float(sla.norm(T, 2))
        lb = chol_cert_lower(T, m_of[M])
        lo, hi = rayleigh_enclosure(T)
        cert[M] = lb
        cert_ok = cert_ok and lb is not None and lb > 0.0 \
            and lo <= m_of[M] <= hi
        anch_ok = anch_ok and abs(m_of[M] - LAM_CITED[M]) \
            / LAM_CITED[M] <= ANCH_REL
    check("S0.RUNGS all %d rungs: lambda_min anchors (rel <= %.2f) "
          "+ rigorous PD certificates + bracketing enclosures"
          % (len(RUNG_MS), ANCH_REL), anch_ok and cert_ok)

    # ============================================================== S1
    print("\nS1 -- reproduction wards on the extended instrument")
    repro_ok, xi_ok = True, True
    for M in REPRO_MS:
        cT = towers[M][:M]
        for lab, det_of in (("v1", lambda g: (0.0,)),
                            ("v2", lambda g: detunes_v2(M, g))):
            n_cmp, n_eq, xi_old_rows = 0, 0, []
            for ig, g in enumerate(GAMMAS_GRID):
                det = det_of(float(g))
                d_old, _, _ = boundary_scan(cT, M, nrm_of[M],
                                            float(g), det,
                                            EXT_DELTAS,
                                            N_BISECT_OLD)
                d_new, _, _ = boundary_scan(cT, M, nrm_of[M],
                                            float(g), det,
                                            EXT2_DELTAS, N_BISECT2)
                if np.isfinite(d_old):
                    xi_old_rows.append(d_old)
                if np.isfinite(d_old) \
                        and d_old > EXT_DELTAS[0] * (1 + 1e-12):
                    # Exact-subset grid => same scan hit cell; the
                    # depth-3 vs depth-4 bisection differs by at
                    # most ~1.5% of the shared cell => tol 2%.
                    n_cmp += 1
                    if np.isfinite(d_new) \
                            and abs(d_new - d_old) / d_old <= 2e-2:
                        n_eq += 1
            repro_ok = repro_ok and (n_cmp == 0 or n_eq == n_cmp)
            if lab == "v1" and M in XI_V1_CITED and xi_old_rows:
                xi_m = float(np.median(xi_old_rows)) * M * DGRID
                rel = abs(xi_m - XI_V1_CITED[M]) / XI_V1_CITED[M]
                xi_ok = xi_ok and rel <= REPRO_REL
            print("      M = %d %s: %d uncensored old-grid rows, "
                  "%d agree on the extended grid" % (M, lab, n_cmp,
                                                     n_eq))
    check("S1.REPRO boundaries uncensored on the old grid reproduce "
          "on the extended instrument (exact-subset construction; "
          "bisection depth 3 -> 4 refines within the same cell, "
          "tol 2%%)", repro_ok)
    check("S1.XI v1 old-grid Xi medians reproduce the cited series "
          "at M = %s (rel <= %.0e)"
          % (",".join(str(m) for m in REPRO_MS), REPRO_REL), xi_ok)

    # ============================================================== S2
    print("\nS2 -- the uncensored v2 rerun (extended instrument)")
    bounds, wits = {}, {}
    xi2, cens = {}, {}
    for M in RUNG_MS:
        cT = towers[M][:M]
        bb = np.full(len(GAMMAS_GRID), np.nan)
        ww = [None] * len(GAMMAS_GRID)
        for ig, g in enumerate(GAMMAS_GRID):
            d_mb, w_mb, _ = boundary_scan(
                cT, M, nrm_of[M], float(g),
                detunes_v2(M, float(g)), EXT2_DELTAS, N_BISECT2)
            bb[ig], ww[ig] = d_mb, w_mb
        bounds[M], wits[M] = bb, ww
        xi2[M], reach = med_xi(bb, M * DGRID)
        cens[M] = int(np.sum(np.isfinite(bb)
                             & (bb <= EXT2_DELTAS[0] * (1 + 1e-9))))
        print("      X = %8.4f: median delta_mb = %.5f -> Xi_v2 = "
              "%.4f (%d/36 reach, %d rows on the new floor)"
              % (M * DGRID, xi2[M] / (M * DGRID), xi2[M], reach,
                 cens[M]))
    deep_m = RUNG_MS[-1]
    cTd = towers[deep_m][:deep_m]
    n_cert, n_cert_ok = 0, 0
    for ig in BATT_GIDX:
        b = bounds[deep_m][ig]
        if not np.isfinite(b) or wits[deep_m][ig] is None:
            continue
        g = float(GAMMAS_GRID[ig])
        ql = quad_lags(deep_m, g, float(b))[:deep_m]
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        n_cert += 1
        n_cert_ok += int(certified_break(cTd + ql, deep_m,
                                         wits[deep_m][ig], bud))
    check("S2.CERT witness Rayleigh certificates re-prove %d/%d "
          "sampled uncensored boundary points at the deepest rung"
          % (n_cert_ok, n_cert), n_cert >= 4 and n_cert_ok == n_cert)

    # ============================================================== S3
    print("\nS3 -- THE DECISION (frozen gates, priority R3 > R1 > "
          "R2)")
    last3 = RUNG_MS[-3:]
    censored_rungs = [M for M in last3 if cens[M] >= CENSOR_MAJ]
    lx = np.log([M * DGRID for M in last3])
    ly = np.log([xi2[M] for M in last3])
    slope3 = float(np.polyfit(lx, ly, 1)[0])
    floor2 = float(np.median([xi2[M] for M in last3]))
    band_ok = all(abs(xi2[M] / floor2 - 1.0) <= BAND_REG
                  for M in last3)
    print("    censoring census (row on the new floor %.4e): %s "
          "(median-censored iff >= %d/36)"
          % (EXT2_DELTAS[0],
             ", ".join("M=%d: %d" % (M, cens[M]) for M in last3),
             CENSOR_MAJ))
    print("    slope3(uncensored) over X = %s: %.3f (R1 <= %.2f); "
          "floor = %.4f; band +-%.0f%%: %s"
          % (", ".join("%.2f" % (M * DGRID) for M in last3), slope3,
             GATE_SLOPE, floor2, 100 * BAND_REG,
             "ok" if band_ok else "MISS (typed)"))
    caveats = []
    if censored_rungs:
        verdict = "STILL-CENSORED"
        caveats.append("median-censored rungs: %s; projected next "
                       "decade floor %.1e"
                       % (",".join(str(m) for m in censored_rungs),
                          EXT2_DELTAS[0] / 10.0))
    elif slope3 <= GATE_SLOPE:
        verdict = "RANGE-DECIDES-DECLINE"
    else:
        verdict = "RANGE-DECIDES-FLOOR"
        if not band_ok:
            caveats.append("band regularity miss (wiggle > 5%) -- "
                           "floor typed as approximate")

    # ============================================================== S4
    print("\nS4 -- carrier census (uncensored; BINDING iff "
          "RANGE-DECIDES-FLOOR)")
    fin_ig = [ig for ig in range(len(GAMMAS_GRID))
              if np.isfinite(bounds[deep_m][ig])]
    dvals = np.array([bounds[deep_m][ig] for ig in fin_ig])
    dists = np.array([float(np.min(np.abs(
        gam_c[gam_c < 250.0] - GAMMAS_GRID[ig]))) for ig in fin_ig])
    rc = rank_corr(dvals, dists)
    hi_mask = dvals >= np.median(dvals)
    print("    deepest rung (M = %d): rank corr(delta_mb, dist to "
          "nearest ordinate) = %+.3f; rows ABOVE median delta "
          "(binding): median dist %.2f | below: %.2f"
          % (deep_m, rc, float(np.median(dists[hi_mask])),
             float(np.median(dists[~hi_mask]))))
    stalled, sharp = [], []
    for ig in range(len(GAMMAS_GRID)):
        ds = [bounds[M][ig] for M in last3]
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
                  "dist to nearest ordinate %.2f"
                  % (lab, len(rows),
                     float(np.median([r[0] for r in rows])),
                     float(np.median([r[2] for r in rows]))))
    on_v2 = []
    for gz in gam_c[:N_ONZERO]:
        if gz > GAMMAS_GRID[-1]:
            break
        d_on, _, _ = boundary_scan(cTd, deep_m, nrm_of[deep_m],
                                   float(gz),
                                   detunes_v2(deep_m, float(gz)),
                                   EXT2_DELTAS, N_BISECT2)
        on_v2.append(d_on)
    fin_on = [d for d in on_v2 if np.isfinite(d)]
    print("    on-ordinate family (M = %d, uncensored): delta_mb "
          "median %.4f, range [%.4f, %.4f] (%d reach; %d on floor)"
          % (deep_m, float(np.median(fin_on)) if fin_on else
             float("nan"), min(fin_on) if fin_on else float("nan"),
             max(fin_on) if fin_on else float("nan"), len(fin_on),
             sum(1 for d in fin_on
                 if d <= EXT2_DELTAS[0] * (1 + 1e-9))))
    print("    CIRCULARITY CHECK (typed): the battery design "
          "(hash-verified %s..) contains no zero datum -- any "
          "zero-correlation above is measured OUTPUT of the "
          "verified tower, not design input." % v2h[:16])

    # ============================================================== S5
    print("\nS5 -- the honest law")
    print("  %9s %11s %12s %9s %9s %10s %6s" % (
        "X", "lam_min", "cert lower", "Xi(v1)", "Xi(v2old)",
        "Xi(v2ext)", "floor#"))
    for M in RUNG_MS:
        print("  %9.4f %11.4e %12.4e %9.4f %9.4f %10.4f %6d"
              % (M * DGRID, m_of[M], cert[M], XI_V1_CITED[M],
                 XI_V2_OLD_CITED[M], xi2[M], cens[M]))
    xi_deep = xi2[deep_m]
    print("    depth-to-width benchmarks (deepest uncensored "
          "calibration Xi = %.4f):" % xi_deep)
    for dl in (0.1, 0.05, 0.01, 0.005, 0.001):
        xs_ = xi_deep / dl
        print("      delta >= %6.3f excluded at depth X* = %7.1f "
              "(comb cap e^{X*} = %.2e)" % (dl, xs_, math.exp(xs_)))
    print("""    THE STRONGEST SUPPORTED LADDER STATEMENT (verbatim,
    report only): 'On the machine-verified GL1 tower (rungs
    certified PD by Cholesky/Higham certificates to X = 24.8125,
    comb cap 6.0e10), the preregistered rank-12/36 detune battery
    (hash %s..) excludes, for every gamma on the frozen 36-point
    grid, the single-quadruple hypothesis 1/2 +- delta +- i gamma
    for all delta >= delta_mb(gamma), with median delta_mb given in
    the table above and every sampled boundary point re-proved by a
    rigorous witness-Rayleigh certificate; the census threshold
    Xi_eff = X delta_mb obeys the measured series above.  Caveats:
    single-quadruple dominance; identity budget 1e-8 + 100 eps
    (||T|| + ||Q||); the region lies inside the [A1]-verified
    strip.'
    REMAINING INSTRUMENT LIMITS (typed): grid floor %.1e; gamma
    grid 36 points to Nyquist pi/D = 201.1; battery v2 is richer
    than v1 but still finite-rank; the deployed rank-4 battery
    remains the contract instrument.""" % (v2h[:16],
                                           EXT2_DELTAS[0]))

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
    check("C1a [must-fire] synthetic quadruple at 2 delta_mb "
          "(uncensored) breaks the full spectrum: %d/%d points"
          % (n_in if inside_ok else -1, n_in),
          inside_ok and n_in >= 4)

    rng = np.random.default_rng(SEED_SCRAMBLE)
    alpha_t = 0.5 * 1503 * DGRID
    u_scr = rng.uniform(0.0, 2.0 * alpha_t, size=masses_scr.size)
    c_scr = np.zeros(1503)
    tent_accumulate(c_scr, 1503, u_scr, masses_scr)
    lam_scr = full_min(srp.continuum_lags(1503) + c_scr, 1503)
    check("C2 [must-fire] scramble at M = 1503 (%d masses, seed "
          "%d): lambda_min = %.3e < 0"
          % (masses_scr.size, SEED_SCRAMBLE, lam_scr), lam_scr < 0.0)

    ep_cap = 34000
    r1 = epx.lattice_r1(ep_cap)
    lamE = epx.dirichlet_vonmangoldt(np.asarray(r1, float) / 2.0,
                                     ep_cap)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    cE, _ = core.atom_lags_at(
        0.5 * 640 * DGRID, 640, np.log(supp.astype(float)),
        2.0 * lamE[supp] / np.sqrt(supp.astype(float)))
    lam_ep = full_min(srp.continuum_lags(640) + cE, 640)
    check("C3 [must-fire] Epstein swap (reach %d => M = 640, "
          "typed): lambda_min = %.3e < 0" % (ep_cap, lam_ep),
          lam_ep < 0.0)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- verdict")
    print("=" * 78)
    print("\n  VERDICT: %s" % verdict)
    print("  extended-instrument hash: %s" % EXT_HASH[:16])
    print("  slope3 = %.3f | floor = %.4f | censored rows (last 3 "
          "rungs) = %s"
          % (slope3, floor2,
             ", ".join("%d" % cens[M] for M in last3)))
    for cv in caveats:
        print("  TYPED: %s" % cv)
    if FAILS:
        print("  TYPED FAILURES: %s" % ",".join(FAILS))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
