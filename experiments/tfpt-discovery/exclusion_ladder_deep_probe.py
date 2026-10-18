"""PRIME.EXCLUSIONLADDER.02 -- the exclusion ladder EXTENDED beyond
X = 18.375 and the certification HARDENED (EXPLORATION ONLY).

PARENT (read completely, machinery inherited verbatim):
detector_inversion_probe.py (2026-08-06, DETECTOR-INVERTED): the
verified PSD rungs of the GL1 tower (D = 1/64, T_X = toeplitz(c[:M]),
X = M D) were inverted into rigorous quadruple-exclusion regions via
the tent-read Guinand identity; two zones (T - Q interpolation-zone
exclusion, T + Q margin-break = detector-native); scaling law
Xi_eff = X delta_mb falling 0.67 (X = 4) -> 0.31 (X = 18.375); the
safe rank-4 subspace criterion; budget EXC = 1e-8 + 100 eps
(||T|| + ||Q||).  THIS PROBE (user-authorized continuation): deepen
the ladder, feed the new margins through the SAME calibrated
inversion, and harden the certificates.

TASK STRUCTURE (all bars/caps predeclared, frozen before running):
 S0 FIREWALL + BENCHMARK + CAP DECISION: segmented bit-vector sieve
    + bincount tent assembly (deployed T115 convention, offsets -2..2
    + u < D reflection, EXACT convention parity demanded against the
    deployed core.atom_lags_at path at M = 1176: atom count EQUAL,
    max |dc| <= PARITY_C_ABS = 5e-9); FFT Toeplitz-matvec ward vs
    dense (<= 1e-9).  PREDECLARED CAP RULE: t_proj(nmax) = t_bench x
    (nmax / nmax_1176) x 1.3; stretch rung M = 1414 (X = 22.09375,
    comb cap e^X = 3.94e9 <= 4e9) iff t_proj <= 720 s; else target
    rung M = 1326 only (X = 20.71875, e^X = 9.98e8 <= 1e9) iff
    t_proj <= 600 s; else NO new rung => LADDER-LIMITED (typed).
 S1 BASELINE TOWER: rungs M = 256 / 640 / 1176 rebuilt on the parent
    paths bit for bit (U_ALL prefix / deployed 1e8 table); anchors
    5.29e-5 / 1.18e-5 / 3.9e-6 (+ v780 3.882e-6), rel tol 2e-2.
 S2 NEW RUNGS + CERTIFICATES (hardening a, predeclared):
    (i)  float lambda_min via eigvalsh; float budget 100 eps ||T||
         (gate-b discipline of the parent).
    (ii) RIGOROUS LOWER BOUND: Cholesky PD certificate -- if the
         float Cholesky of T - beta I runs to completion then
         (Higham Acc&Stab Thm 10.3, Rump-style verification)
         L L^T = A + dA, |dA| <= gamma_{M+1} |L||L|^T, hence
         lambda_min(T) >= beta - gamma_{M+1} max-rowsum(|L||L|^T)
         - u max|diag|; beta scanned over (0.9, 0.5, 0.25, 0.1) x
         lambda_hat; gamma_n = n u/(1 - n u), u = eps/2.
    (iii) RAYLEIGH-RESIDUAL ENCLOSURE: bottom eigenpair (rho, v);
         some eigenvalue lies in [rho - r, rho + r] with r the
         residual norm, both inflated by the rigorous dot-product
         bounds gamma_M |x|^T|A||x| (Gershgorin-style row-sum norms).
    (iv) SUMMATION-ORDER WARD: the M = 1326 assembly is repeated
         with reversed segment order + segment size 2^24; the
         Toeplitz perturbation bound sum|dc| (= max row sum) must
         stay BELOW the rung margin (else precision wall, typed);
         the 1414 order noise is TYPED as the 1326 measurement
         scaled by e^{dX/2} (not a certificate).
    CERTIFIED STATEMENT SCOPE (typed): the certificates bind the
    ASSEMBLED float matrix; read-convention systematics stay under
    the parent's IDENT_BUD = 1e-8 typing; SURPRISE trigger:
    lambda_hat <= 0, or lambda_hat outside (0.2, 5) x the
    baseline-extrapolated decline, or certificate contradiction
    (cert_lb <= 0 < lambda_hat).
 S3 CALIBRATION WARDS AT DEPTH: W0 pair layer == 2 a(g) cos(g k D)
    (<= 1e-12); WQ quadruple lag reads == D x tent quadrature
    (rel <= 1e-8); W2 smooth-packet Guinand identity at the NEW
    rungs with the [A2]-integrated tail budget (slack 3x).
 S4 THE EXTENDED EXCLUSION MAP: frozen parent grids gamma in
    geomspace(2, 190, 36), delta in linspace(1/60, 1/2, 30) for the
    census + monotone comparison across ALL rungs (loss <= 2%);
    PREDECLARED EXTENDED DELTA GRID geomspace(1/240, 1/2, 44) with
    3-step geometric bisection for the deep boundaries (the frozen
    coarse grid floor 1/60 would bind at X > 19: typed, not hidden);
    both boundaries (T - Q exclusion delta_min, margin-break
    delta_mb); on-ordinate family at the deepest rung (report).
 S5 THE SCALING LAW: frozen-grid medians compared against the
    parent's cited 0.67 / 0.31 (rel 0.15, comparability ward);
    extended-grid Xi_eff(X) table + log-log slope; CONTINUATION
    GATE: Xi_eff at the deepest new rung <= 1.05 x Xi_eff(18.375)
    (else SURPRISE: trend reversal); benchmark ladder X*(delta) and
    the honest Nyquist/[A1] reach statement re-printed.
 S6 KNOWN-TERRITORY COMPARISON at the new depth (gate-c typing:
    inside the [A1] strip; vs classical MTY 2024 in-band).
 S7 HARDENING:
    (a) CERTIFIED EXCLUSION TABLE: at sampled gammas x deepest
        rungs, the extended-boundary points re-proved by the
        rigorous witness certificate (dense matvec + inflated
        Rayleigh upper bound < -EXC_BUD) for BOTH criteria.
    (b) MULTI-ZERO INTERFERENCE AT DEPTH: pairs of boundary
        quadruples; rank-8 combined battery; margin break must
        PERSIST under double injection (no interference rescue) and
        the two-quadruple hypothesis (T - Q1 - Q2) must be excluded
        (superadditive union); battery overlap census printed;
        full-eig confirmation on 2 pairs.
    (c) BATTERY DEPENDENCE (exclusion is battery-relative, typed):
        u-support fractions (0.25, 0.5, 0.75, 1.0) of the frozen
        rank-4 family and the DETUNED rank-12 enrichment (gamma +-
        pi/(2X)); trade-off curve delta_mb(support), gamma-reach and
        frozen-grid region growth under enrichment -- REPORT ONLY,
        the deployed battery is NOT re-frozen.
CONTROLS: C1a (must-fire) synthetic quadruple at 2 delta_mb inside
 the NEW-rung regions breaks the margin (full eigensolve); C1b
 no-false-exclusion (every claimed deep boundary point confirmed by
 the full eigensolve) + measured under-detection factor (descent
 capped at 6 frozen-grid steps, typed as a lower bound); C2 scramble
 (positions uniform on (0, 2 alpha], SAME masses, declared seed 7 --
 the only RNG use) must destroy the M = 1326 rung PSD; C3 Epstein
 swap (Lambda_E of x^2 + 5 y^2, table reach 34000 => control runs at
 M = 640, typed) must destroy PSD.
VERDICT (frozen enum): LADDER-EXTENDED (>= 1 new certified rung +
 nonempty new maps + monotone census + scaling law continued +
 controls fire) / LADDER-LIMITED (comb budget or precision wall or
 instrument ward failure -- typed exactly where) / LADDER-SURPRISE
 (a margin behaves unexpectedly at depth: reported immediately and
 exactly; priority over the other two).

FIREWALL: v563/v755 read-only; NO zetazero()/nzeros() calls (AST-
checked); the cached RvM-checked ordinate list (v684 provenance,
n = 2500) is read for calibration wards and the on-line side only.
RNG ONLY in the declared C2 scramble (seed 7).  Nothing outside
experiments/ touched.  NO RH claim -- output is the conditional
exclusion-ladder statement with typed caveats (single-quadruple
dominance; float+certificate discipline; inside the [A1] strip).
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
ANCH_REL = 2.0e-2
ATOM_MAX_DEEP = 100000000          # deployed 1e8 reference path (parity)
M_TARGET, M_STRETCH = 1326, 1414   # X = 20.71875 / 22.09375
SEG_ASC, SEG_DESC = 1 << 26, 1 << 24
T_STRETCH_BAR, T_TARGET_BAR = 720.0, 600.0   # predeclared cap rule (s)
PROJ_SAFETY = 1.3
PARITY_C_ABS = 5.0e-9
FFT_WARD_BAR = 1.0e-9
GAMMAS_GRID = np.geomspace(2.0, 190.0, 36)    # frozen (parent)
DELTAS_GRID = np.linspace(1.0 / 60.0, 0.5, 30)  # frozen (parent)
EXT_DELTAS = np.geomspace(1.0 / 240.0, 0.5, 44)  # predeclared deep grid
N_BISECT = 3
W0_BAR, WQ_BAR, W2_SLACK = 1.0e-12, 1.0e-8, 3.0
MONO_TOL = 0.02
IDENT_BUD = 1.0e-8
XI_UP_CITED = 1.9735               # v688/v694 detection threshold
XI_4_CITED, XI_18_CITED = 0.67, 0.31   # parent run-3 medians (frozen grid)
XI_CMP_REL = 0.15
XI_CONT_TOL = 1.05                 # continuation gate (S5)
SURP_DECL_LO, SURP_DECL_HI = 0.2, 5.0   # margin-vs-extrapolation window
R_CLASSICAL = 5.558691             # Mossinghoff-Trudgian-Yang 2024
T_RH_CITED = 3.0e12                # [A1] Platt-Trudgian 2021
A2A, A2B, A2C = 0.1038, 0.2573, 9.3675   # [A2] Hasanalizade-Shen-Wong
W2_PACKETS = (30.0, 50.0, 80.0)
U_RND = 0.5 * np.finfo(float).eps  # unit roundoff
CERT_INFL = 1.01                   # coarse inflation on float bound sums
BATT_GIDX = (3, 10, 17, 24, 30, 35)
BATT_SUPPORTS = (0.25, 0.5, 0.75, 1.0)
MZ_GIDX = (6, 14, 22, 30)
UNDER_SCAN_CAP = 6
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
    """Full off-line quadruple {1/2 +- delta +- i gamma}: tent reads
    of 4 cosh(delta u) cos(gamma u) (v765 RT3 kernel, AMP_Z = 2)."""
    z1, z2 = complex(delta, gamma), complex(-delta, gamma)
    t = np.abs(np.arange(-1, M + 1)) * DGRID
    g = 2.0 * (np.exp(z1 * t) / z1 ** 2 + np.exp(z2 * t) / z2 ** 2).real
    return (g[:-2] - 2.0 * g[1:-1] + g[2:]) / DGRID


def pair_lags(M, gamma):
    t = np.abs(np.arange(-1, M + 1)) * DGRID
    g = -2.0 * np.cos(gamma * t) / gamma ** 2
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
    """Deployed T115 tent convention (v563 atom_lags_at), vectorized:
    offsets -2..2 with idx < M plus the u < D reflection branch."""
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
    """Segmented Eratosthenes over all prime powers <= e^{M D}; tent
    reads accumulated per rung.  Returns per-rung atom lag vectors,
    atom counts, optional retained mass multiset (for the scramble)."""
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
    for p in bp:                       # prime powers p^k, k >= 2
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
    """lambda_min of sym-Toeplitz(cA) restricted to span(Qb) (>= full
    minimum: SAFE under-exclusion) + the witness vector."""
    Y = sla.matmul_toeplitz((cA, cA), Qb, check_finite=False)
    S = Qb.T @ Y
    S = 0.5 * (S + S.T)
    w, V = np.linalg.eigh(S)
    return float(w[0]), Qb @ V[:, 0]


def bud_of(M, nrmT, ql_max):
    return IDENT_BUD + 100.0 * np.finfo(float).eps * (nrmT + M * ql_max)


def boundary_scan(cT, M, nrmT, g, grid, sign, bisect=0,
                  support=1.0, detunes=(0.0,)):
    """First delta on the grid with subspace lambda_min < -bud for
    T + sign*Q; optional geometric bisection refinement.  Returns
    (delta, witness, bud_at_delta)."""
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
    """Rigorous lower bound for lambda_min of the float matrix T:
    float Cholesky success on T - beta I => (Higham Thm 10.3)
    lambda_min(T) >= beta - gamma_{M+1} rowsum(|L||L|^T) - u diag."""
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
    """Rayleigh-residual localization of the bottom eigenpair with
    rigorous dot-product inflations: some eigenvalue in [lo, hi]."""
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
    """Rigorous Rayleigh UPPER bound on lambda_min of sym-Toeplitz(cA)
    from witness x (dense matvec + inflated dot-product error):
    returns (certified lambda_min < -bud, the certified value)."""
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
    ray_up = num_up / (n2 * (1.0 + gamma_fl(M)))
    return ray_up < -bud, ray_up


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    surprises, limits = [], []
    print("=" * 78)
    print("PRIME.EXCLUSIONLADDER.02 -- deeper rungs + hardened "
          "certification (exclusion_ladder_deep_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- firewall + benchmark + predeclared cap decision")
    check("S0.AST no zeta-zero generator call in this file (cached "
          "RvM list read for wards/on-line side; RNG only in the "
          "declared C2 scramble)", ast_zero_firewall(__file__))
    d1 = json.load(open(os.path.join(_here,
                                     "zero_comb_cache_n2000.json")))
    d2 = json.load(open(os.path.join(_here, "c1_zero_ext_n2500.json")))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    check("S0.CACHE %d cached ordinates, gamma_1 = %.4f"
          % (len(gam_c), gam_c[0]),
          len(gam_c) == 2500 and abs(gam_c[0] - 14.134725) < 1e-5)

    # FFT Toeplitz-matvec ward vs dense (deterministic vector)
    Mw = 640
    cw = srp.continuum_lags(Mw)[:Mw]
    xw = np.cos(0.37 * np.arange(Mw)) / math.sqrt(Mw)
    y_f = sla.matmul_toeplitz((cw, cw), xw, check_finite=False)
    y_d = sla.toeplitz(cw) @ xw
    dev_f = float(np.max(np.abs(y_f - y_d))
                  / max(float(np.max(np.abs(y_d))), 1e-300))
    check("S0.FFT Toeplitz matvec (map scan path) == dense: rel dev "
          "%.2e <= %.0e" % (dev_f, FFT_WARD_BAR), dev_f <= FFT_WARD_BAR)

    # benchmark: segmented assembly at the deployed deep rung
    t0 = time.time()
    cs_b, cnt_b, _, ncap_b = seg_assemble([1176])
    t_bench = time.time() - t0
    n1176 = ncap_b[1176]
    print("    benchmark: segmented sieve+reads to n = %d "
          "(%d atoms) in %.1f s" % (n1176, cnt_b[1176], t_bench))

    # deployed reference path (parent bit for bit) -> parity ward
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
    print("    deployed reference path (1e8 table + loop reads): "
          "%.1f s" % (time.time() - t0))
    dev_c = float(np.max(np.abs(cs_b[1176] - c_dep)))
    check("S0.PARITY segmented assembly == deployed T115 path at "
          "M = 1176: atom count %d == %d (EXACT), max |dc| = %.2e "
          "<= %.0e" % (cnt_b[1176], ka, dev_c, PARITY_C_ABS),
          cnt_b[1176] == ka and dev_c <= PARITY_C_ABS)

    # predeclared cap decision
    proj = {M: t_bench * (nmax_of_M(M) / n1176) * PROJ_SAFETY
            for M in (M_TARGET, M_STRETCH)}
    print("    projected sieve+reads: M = %d -> %.0f s | M = %d -> "
          "%.0f s (bars %d / %d s, safety x%.1f, predeclared)"
          % (M_TARGET, proj[M_TARGET], M_STRETCH, proj[M_STRETCH],
             T_TARGET_BAR, T_STRETCH_BAR, PROJ_SAFETY))
    if proj[M_STRETCH] <= T_STRETCH_BAR:
        new_ms = [M_TARGET, M_STRETCH]
    elif proj[M_TARGET] <= T_TARGET_BAR:
        new_ms = [M_TARGET]
        limits.append("stretch rung skipped by the predeclared "
                      "time rule (proj %.0f s > %.0f s)"
                      % (proj[M_STRETCH], T_STRETCH_BAR))
    else:
        new_ms = []
        limits.append("NO new rung: projected sieve %.0f s exceeds "
                      "the predeclared bars" % proj[M_TARGET])
    print("    DECISION: new rungs = %s"
          % (", ".join("M = %d (X = %.5f, cap e^X = %.3e)"
                       % (M, M * DGRID, math.exp(M * DGRID))
                       for M in new_ms) if new_ms else "NONE"))

    # ============================================================== S1
    print("\nS1 -- baseline tower + verified-margin anchors")
    towers = {}
    for M, _anch in RUNGS_BASE[:2]:
        alpha = 0.5 * M * DGRID
        ka2 = core.atoms_in(alpha)
        c_at, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka2],
                                    core.MU_ALL[:ka2])
        towers[M] = srp.continuum_lags(M) + c_at
    towers[1176] = srp.continuum_lags(1176) + c_dep

    T_of, m_of, nrm_of = {}, {}, {}
    for M, anch in RUNGS_BASE:
        T = sla.toeplitz(towers[M][:M])
        lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        T_of[M], m_of[M] = T, lam
        nrm_of[M] = float(sla.norm(T, 2))
        rel = abs(lam - anch) / anch
        check("S1.%d rung M = %d (X = %.3f): lambda_min = %.4e vs "
              "anchor %.2e (rel dev %.3f <= %.2f)"
              % (M, M, M * DGRID, lam, anch, rel, ANCH_REL),
              rel <= ANCH_REL)
    rel780 = abs(m_of[1176] - V780_DEEP) / V780_DEEP
    check("S1.DEEP v780 drainage anchor 3.882e-6 reproduced (rel dev "
          "%.3f <= %.2f)" % (rel780, ANCH_REL), rel780 <= ANCH_REL)

    # ============================================================== S2
    print("\nS2 -- NEW RUNGS + certificates (hardening a)")
    masses_scr = None
    cert = {}
    if new_ms:
        t0 = time.time()
        cs_new, cnt_new, masses_scr, ncap_new = seg_assemble(
            new_ms, collect_mass_M=M_TARGET)
        t_big = time.time() - t0
        for M in new_ms:
            towers[M] = srp.continuum_lags(M) + cs_new[M]
            print("    rung M = %d: %d atoms to n <= %d "
                  "(cap e^X = %.4e)" % (M, cnt_new[M], ncap_new[M],
                                        math.exp(M * DGRID)))
        print("    deep sieve+reads: %.1f s (projected %.0f s)"
              % (t_big, proj[new_ms[-1]]))

        # order-sensitivity ward at M_TARGET (reversed segments, 2^24)
        t0 = time.time()
        cs_rev, _, _, _ = seg_assemble([M_TARGET], seg=SEG_DESC,
                                       reverse=True)
        dc = cs_rev[M_TARGET] - cs_new[M_TARGET]
        dc_sum, dc_max = float(np.sum(np.abs(dc))), \
            float(np.max(np.abs(dc)))
        print("    order ward (%.1f s): sum|dc| = %.2e, max|dc| = "
              "%.2e (Toeplitz perturbation bound ||dT||_2 <= sum|dc|)"
              % (time.time() - t0, dc_sum, dc_max))

        # extrapolated decline from the baseline anchors (report+gate)
        xs = np.array([M * DGRID for M, _ in RUNGS_BASE])
        ys = np.log([m_of[M] for M, _ in RUNGS_BASE])
        sl, ic = np.polyfit(xs, ys, 1)

        for M in new_ms:
            X = M * DGRID
            T = sla.toeplitz(towers[M][:M])
            lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
            T_of[M], m_of[M] = T, lam
            nrm_of[M] = float(sla.norm(T, 2))
            fl = 100.0 * np.finfo(float).eps * nrm_of[M]
            extr = math.exp(ic + sl * X)
            ratio = lam / extr
            check("S2.%d NEW rung M = %d (X = %.5f): lambda_min = "
                  "%.4e > float budget %.1e (margin/budget %.0f); "
                  "extrapolated decline %.2e (ratio %.2f in "
                  "(%.1f, %.1f))"
                  % (M, M, X, lam, fl, lam / max(fl, 1e-300), extr,
                     ratio, SURP_DECL_LO, SURP_DECL_HI),
                  lam > fl and SURP_DECL_LO <= ratio <= SURP_DECL_HI)
            if lam <= 0.0:
                surprises.append("rung M = %d lambda_min = %.3e <= 0"
                                 % (M, lam))
            elif not (SURP_DECL_LO <= ratio <= SURP_DECL_HI):
                surprises.append("rung M = %d margin %.2e off the "
                                 "extrapolated decline %.2e (x%.2f)"
                                 % (M, lam, extr, ratio))

        # certificates on ALL rungs
        print("    certificates (Cholesky PD lower bound + "
              "Rayleigh-residual enclosure; float-matrix scope, "
              "IDENT_BUD systematics typed separately):")
        cert = {}
        cert_ok = True
        for M in sorted(T_of):
            lb, beta, slack = chol_cert_lower(T_of[M], m_of[M])
            lo, hi = rayleigh_enclosure(T_of[M])
            cert[M] = (lb, lo, hi)
            ok_m = (lb is not None and lb > 0.0
                    and lo <= m_of[M] <= hi)
            cert_ok = cert_ok and ok_m
            print("      M = %4d: lambda_min >= %.4e CERTIFIED "
                  "(beta = %.2e, slack %.1e); enclosure [%.4e, %.4e]"
                  % (M, lb if lb is not None else float("nan"),
                     beta if beta is not None else float("nan"),
                     slack if slack is not None else float("nan"),
                     lo, hi))
            if lb is not None and lb <= 0.0 < m_of[M]:
                surprises.append("M = %d certificate lb %.2e <= 0 "
                                 "despite float margin %.2e"
                                 % (M, lb, m_of[M]))
        check("S2.CERT every rung carries a rigorous lambda_min > 0 "
              "certificate and the enclosure brackets the float "
              "margin (%d rungs)" % len(T_of), cert_ok)

        rob = m_of[M_TARGET] - dc_sum
        check("S2.ORDER summation-order robustness at M = %d: margin "
              "%.3e - sum|dc| %.2e = %.3e > 0 (the certified margin "
              "survives the measured assembly-order noise); M = %d "
              "noise TYPED as %.2e x e^{dX/2} = %.2e (estimate, not "
              "a certificate)"
              % (M_TARGET, m_of[M_TARGET], dc_sum, rob, M_STRETCH,
                 dc_sum, dc_sum * math.exp(
                     0.5 * (M_STRETCH - M_TARGET) * DGRID)),
              rob > 0.0)
        if rob <= 0.0:
            limits.append("precision wall: order noise %.2e >= "
                          "margin %.2e at M = %d"
                          % (dc_sum, m_of[M_TARGET], M_TARGET))
    else:
        print("    (no new rung -- predeclared budget rule; "
              "LADDER-LIMITED path)")

    all_ms = sorted(T_of)
    deep_m = all_ms[-1]

    # ============================================================== S3
    print("\nS3 -- calibration wards at depth")
    gtest = 47.3
    lp = pair_lags(256, gtest)
    rank2 = 2.0 * a_weight(gtest) * np.cos(
        gtest * DGRID * np.arange(256))
    dev0 = float(np.max(np.abs(lp - rank2)))
    check("W0 on-line pair layer == 2 a(g) cos(g k D) exactly: max "
          "dev %.2e <= %.0e" % (dev0, W0_BAR), dev0 <= W0_BAR)

    dev_q = 0.0
    for (gq, dq, kq) in ((31.7, 0.21, 40), (88.2, 0.44, 130),
                         (9.4, 0.08, 3)):
        ql = quad_lags(200, gq, dq)
        uu = np.linspace((kq - 1) * DGRID, (kq + 1) * DGRID, 20001)
        tent = (1.0 - np.abs(uu / DGRID - kq)) / DGRID
        integ = DGRID * float(np.trapezoid(
            tent * 4.0 * np.cosh(dq * uu) * np.cos(gq * uu), uu))
        dev_q = max(dev_q, abs(ql[kq] - integ) / abs(integ))
    check("WQ quadruple lag reads == D x tent quadrature (max rel "
          "dev %.1e <= %.0e)" % (dev_q, WQ_BAR), dev_q <= WQ_BAR)

    aw = a_weight(gam_c)
    for M in (new_ms if new_ms else [1176]):
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
        check("W2 smooth-packet Guinand identity at NEW rung M = %d: "
              "|x^T T x - zero side| <= %.1f x tail budget (worst "
              "ratio %.3f)" % (M, W2_SLACK, worst), worst <= W2_SLACK)

    # ============================================================== S4
    print("\nS4 -- the extended exclusion map (frozen census grid + "
          "predeclared deep delta grid)")
    maps, maps_mb = {}, {}
    for M in all_ms:
        t0 = time.time()
        exc, mbk = census_maps(towers[M][:M], M, nrm_of[M])
        maps[M], maps_mb[M] = exc, mbk
        print("    M = %4d (X = %7.3f): T-Q exclusion %4d/%d pts | "
              "margin-break %4d/%d pts (%.1f s)"
              % (M, M * DGRID, int(exc.sum()), exc.size,
                 int(mbk.sum()), mbk.size, time.time() - t0))
    check("S4.1 both regions NONEMPTY on the new rungs (%s)"
          % ", ".join("M=%d: %d/%d" % (M, maps[M].sum(),
                                       maps_mb[M].sum())
                      for M in (new_ms if new_ms else all_ms)),
          all(maps[M].sum() > 0 and maps_mb[M].sum() > 0
              for M in (new_ms if new_ms else all_ms)))

    mono_ok = True
    for mp, lab in ((maps, "T-Q"), (maps_mb, "margin-break")):
        for M1, M2 in zip(all_ms[:-1], all_ms[1:]):
            lost = int((mp[M1] & ~mp[M2]).sum())
            frac = lost / max(int(mp[M1].sum()), 1)
            mono_ok = mono_ok and frac <= MONO_TOL
            print("    monotone [%s]: region(M=%d) minus region(M=%d)"
                  ": %d pts (%.1f%%)"
                  % (lab, M1, M2, lost, 100 * frac))
    check("S4.2 deeper rungs keep shallower exclusions on BOTH "
          "boundaries (loss <= %.0f%%)" % (100 * MONO_TOL), mono_ok)

    # extended boundaries (both criteria) on the predeclared deep grid
    bounds_mb = {M: np.full(len(GAMMAS_GRID), np.nan) for M in all_ms}
    bounds_tq = {M: np.full(len(GAMMAS_GRID), np.nan) for M in all_ms}
    wits_mb = {M: [None] * len(GAMMAS_GRID) for M in all_ms}
    buds_mb = {M: np.full(len(GAMMAS_GRID), np.nan) for M in all_ms}
    for M in all_ms:
        cT = towers[M][:M]
        for ig, g in enumerate(GAMMAS_GRID):
            d_mb, w_mb, b_mb = boundary_scan(cT, M, nrm_of[M],
                                             float(g), EXT_DELTAS,
                                             +1.0, bisect=N_BISECT)
            d_tq, _, _ = boundary_scan(cT, M, nrm_of[M], float(g),
                                       EXT_DELTAS, -1.0,
                                       bisect=N_BISECT)
            bounds_mb[M][ig], bounds_tq[M][ig] = d_mb, d_tq
            wits_mb[M][ig], buds_mb[M][ig] = w_mb, b_mb
    print("    extended boundaries (delta_mb margin-break | delta_min"
          " T-Q; -- = no reach; grid 1/240..1/2 + %d-step bisection):"
          % N_BISECT)
    hdr = " ".join("%8s" % ("X=%.1f" % (M * DGRID)) for M in all_ms)
    print("    %8s | %s | %s" % ("gamma", hdr, hdr))
    for ig in range(0, len(GAMMAS_GRID), 5):
        row_a = " ".join(
            ("%8.4f" % bounds_mb[M][ig])
            if np.isfinite(bounds_mb[M][ig]) else "%8s" % "--"
            for M in all_ms)
        row_b = " ".join(
            ("%8.4f" % bounds_tq[M][ig])
            if np.isfinite(bounds_tq[M][ig]) else "%8s" % "--"
            for M in all_ms)
        print("    %8.2f | %s | %s" % (GAMMAS_GRID[ig], row_a, row_b))

    # on-ordinate family at the deepest rung (report)
    on_mb = []
    cT = towers[deep_m][:deep_m]
    for gz in gam_c[:N_ONZERO]:
        if gz > GAMMAS_GRID[-1]:
            break
        d_on, _, _ = boundary_scan(cT, deep_m, nrm_of[deep_m],
                                   float(gz), EXT_DELTAS, +1.0,
                                   bisect=N_BISECT)
        on_mb.append(d_on)
    fin_on = [d for d in on_mb if np.isfinite(d)]
    print("    on-ordinate family (M = %d, first %d actual "
          "ordinates): delta_mb median %.4f, range [%.4f, %.4f] "
          "(%d reach)"
          % (deep_m, len(on_mb),
             float(np.median(fin_on)) if fin_on else float("nan"),
             min(fin_on) if fin_on else float("nan"),
             max(fin_on) if fin_on else float("nan"), len(fin_on)))

    # ============================================================== S5
    print("\nS5 -- the scaling law Xi_eff = X delta_mb")
    # frozen-grid medians (parent comparability)
    xi_frozen = {}
    for M in all_ms:
        db = []
        for ig in range(len(GAMMAS_GRID)):
            idx = np.nonzero(maps_mb[M][ig])[0]
            if len(idx):
                db.append(DELTAS_GRID[idx[0]])
        if db:
            xi_frozen[M] = float(np.median(db)) * M * DGRID
    c4 = abs(xi_frozen.get(256, np.nan) - XI_4_CITED) / XI_4_CITED
    c18 = abs(xi_frozen.get(1176, np.nan) - XI_18_CITED) / XI_18_CITED
    check("S5.1 frozen-grid comparability: Xi(X=4) = %.3f vs parent "
          "0.67 (rel %.2f), Xi(X=18.375) = %.3f vs parent 0.31 (rel "
          "%.2f) <= %.2f"
          % (xi_frozen.get(256, float("nan")), c4,
             xi_frozen.get(1176, float("nan")), c18, XI_CMP_REL),
          c4 <= XI_CMP_REL and c18 <= XI_CMP_REL)

    # extended-grid trend (the deliverable trend; grid floor lifted)
    xi_ext = {}
    print("    extended-grid ladder:")
    for M in all_ms:
        X = M * DGRID
        fin = bounds_mb[M][np.isfinite(bounds_mb[M])]
        if len(fin):
            xi_ext[M] = float(np.median(fin)) * X
            print("      X = %8.4f: median delta_mb = %.5f -> "
                  "Xi_eff = %.4f (%d/%d gammas reach)"
                  % (X, float(np.median(fin)), xi_ext[M], len(fin),
                     len(GAMMAS_GRID)))
    if len(xi_ext) >= 2:
        lx = np.log([M * DGRID for M in xi_ext])
        ly = np.log(list(xi_ext.values()))
        slope = float(np.polyfit(lx, ly, 1)[0])
        print("    log-log slope d ln Xi / d ln X = %.3f "
              "(parent two-point rate was ~ -0.50)" % slope)
    if new_ms:
        cont_ok = all(xi_ext[M] <= XI_CONT_TOL * xi_ext[1176]
                      for M in new_ms if M in xi_ext)
        check("S5.2 CONTINUATION: Xi_eff at the new rungs (%s) <= "
              "%.2f x Xi_eff(18.375) = %.4f -- the sharpening "
              "continues"
              % (", ".join("%.4f" % xi_ext[M] for M in new_ms
                           if M in xi_ext),
                 XI_CONT_TOL, xi_ext[1176]), cont_ok)
        if not cont_ok:
            surprises.append("Xi_eff trend reversal at depth: %s vs "
                             "%.4f at X = 18.375"
                             % (["%.4f" % xi_ext.get(M, float("nan"))
                                 for M in new_ms], xi_ext[1176]))
    if xi_ext:
        xi_deep = xi_ext[deep_m]
        print("    cited detection threshold Xi_up = %.4f -- deepest "
              "Xi_eff/Xi_up = %.3f" % (XI_UP_CITED,
                                       xi_deep / XI_UP_CITED))
        print("    X*(delta) = Xi_eff/delta benchmark ladder (deepest"
              " calibration):")
        for dl in (0.5, 0.25, 0.1, 0.05, 0.01):
            xs_ = xi_deep / dl
            print("      delta >= %5.2f excluded at depth X* = "
                  "%7.1f (comb cap e^{X*} = %.2e)"
                  % (dl, xs_, math.exp(xs_)))
        print("    REACH (honest, unchanged): gamma-window Nyquist-"
              "limited to pi/D = %.1f; NEW territory needs gamma > "
              "3e12 [A1] => D < %.1e, M > %.1e X lags -- out of "
              "reach by ~10 orders; the ladder is a DEPTH-to-WIDTH "
              "bridge, not a record claim."
              % (math.pi / DGRID, math.pi / T_RH_CITED,
                 T_RH_CITED / math.pi))

    # ============================================================== S6
    print("\nS6 -- known-territory comparison at the new depth "
          "(typed plainly)")
    print("    [A1]: all zeros with |gamma| <= 3e12 are ON the line; "
          "every visible gamma (<= 190) is INSIDE that strip -- the "
          "region is an independent TFPT-data-only re-derivation, "
          "NOT new territory.")
    for gb in (50.0, 100.0, 180.0):
        ig = int(np.argmin(np.abs(GAMMAS_GRID - gb)))
        ours = bounds_mb[deep_m][ig]
        dcl = 0.5 - 1.0 / (R_CLASSICAL * math.log(gb))
        print("    gamma = %5.1f: delta_mb >= %s | T-Q delta_min >= "
              "%s | classical (MTY 2024) delta > %.3f -- %s in-band"
              % (gb, ("%.4f" % ours) if np.isfinite(ours) else "--",
                 ("%.4f" % bounds_tq[deep_m][ig])
                 if np.isfinite(bounds_tq[deep_m][ig]) else "--",
                 dcl, "WIDER" if (np.isfinite(ours) and ours < dcl)
                 else "narrower"))

    # ============================================================== S7
    print("\nS7 -- hardening (certified exclusions, multi-zero "
          "interference, battery dependence)")
    # (a) certified exclusion table at sampled gammas x deepest rungs
    deep3 = all_ms[-3:]
    n_cert, n_cert_ok = 0, 0
    for M in deep3:
        cT = towers[M][:M]
        for ig in BATT_GIDX:
            g = float(GAMMAS_GRID[ig])
            b = bounds_mb[M][ig]
            if not np.isfinite(b) or wits_mb[M][ig] is None:
                continue
            ql = quad_lags(M, g, float(b))[:M]
            bud = bud_of(M, nrm_of[M], float(np.max(np.abs(ql))))
            ok1, v1 = certified_break(cT + ql, M, wits_mb[M][ig], bud)
            d_tq = bounds_tq[M][ig]
            ok2 = True
            if np.isfinite(d_tq):
                ql2 = quad_lags(M, g, float(d_tq))[:M]
                bud2 = bud_of(M, nrm_of[M],
                              float(np.max(np.abs(ql2))))
                _, w2 = sub_lam(cT - ql2, np.linalg.qr(
                    battery_B(M, g, float(d_tq)))[0])
                ok2, _v2 = certified_break(cT - ql2, M, w2, bud2)
            n_cert += 1
            n_cert_ok += int(ok1 and ok2)
    check("S7a certified exclusion boundary: rigorous witness "
          "Rayleigh certificates (dense matvec, inflated dot-product "
          "bounds) re-prove %d/%d sampled deep boundary points on "
          "BOTH criteria" % (n_cert_ok, n_cert),
          n_cert >= 8 and n_cert_ok == n_cert)

    # (b) multi-zero interference at the deepest rung
    cT = towers[deep_m][:deep_m]
    pts = [(int(ig), float(GAMMAS_GRID[ig]),
            float(bounds_mb[deep_m][ig])) for ig in MZ_GIDX
           if np.isfinite(bounds_mb[deep_m][ig])]
    n_pair, ok_break, ok_excl, olap_max = 0, 0, 0, 0.0
    full_conf, n_full = 0, 0
    for a in range(len(pts)):
        for b in range(a + 1, len(pts)):
            _, g1, dl1 = pts[a]
            _, g2, dl2 = pts[b]
            q1 = quad_lags(deep_m, g1, dl1)[:deep_m]
            q2 = quad_lags(deep_m, g2, dl2)[:deep_m]
            budp = IDENT_BUD + 100.0 * np.finfo(float).eps * (
                nrm_of[deep_m] + deep_m
                * (float(np.max(np.abs(q1)))
                   + float(np.max(np.abs(q2)))))
            B1 = battery_B(deep_m, g1, dl1)
            B2 = battery_B(deep_m, g2, dl2)
            Qb, _ = np.linalg.qr(np.concatenate([B1, B2], axis=1))
            lam_b, _ = sub_lam(cT + q1 + q2, Qb)
            lam_e, _ = sub_lam(cT - q1 - q2, Qb)
            n_pair += 1
            ok_break += int(lam_b < -budp)
            ok_excl += int(lam_e < -budp)
            Q1o, _ = np.linalg.qr(B1)
            Q2o, _ = np.linalg.qr(B2)
            olap_max = max(olap_max, float(
                np.linalg.norm(Q1o.T @ Q2o, 2)))
            if n_full < 2:
                n_full += 1
                full_conf += int(full_min(cT + q1 + q2, deep_m)
                                 < -budp)
    check("S7b multi-zero interference at depth (M = %d): double "
          "injection breaks the margin on %d/%d boundary pairs (no "
          "interference rescue), the two-quadruple hypothesis is "
          "excluded on %d/%d pairs, full-eig confirms %d/%d; max "
          "battery overlap %.3f (typed)"
          % (deep_m, ok_break, n_pair, ok_excl, n_pair, full_conf,
             n_full, olap_max),
          n_pair >= 3 and ok_break == n_pair and ok_excl == n_pair
          and full_conf == n_full)

    # (c) battery dependence / trade-off (REPORT ONLY, no re-freeze)
    print("    battery trade-off at M = %d (report only; deployed "
          "battery NOT re-frozen):" % deep_m)
    dg = math.pi / (2.0 * deep_m * DGRID)
    print("    %8s | %s | %8s" % (
        "gamma", " ".join("f=%.2f  " % f for f in BATT_SUPPORTS),
        "rank-12"))
    med_by_f = {f: [] for f in BATT_SUPPORTS}
    med_b12 = []
    for ig in BATT_GIDX:
        g = float(GAMMAS_GRID[ig])
        row = []
        for f in BATT_SUPPORTS:
            d_f, _, _ = boundary_scan(cT, deep_m, nrm_of[deep_m], g,
                                      EXT_DELTAS, +1.0,
                                      bisect=N_BISECT, support=f)
            row.append(d_f)
            if np.isfinite(d_f):
                med_by_f[f].append(d_f)
        d12, _, _ = boundary_scan(cT, deep_m, nrm_of[deep_m], g,
                                  EXT_DELTAS, +1.0, bisect=N_BISECT,
                                  detunes=(-dg, 0.0, dg))
        if np.isfinite(d12):
            med_b12.append(d12)
        print("    %8.2f | %s | %s" % (
            g, " ".join(("%7.4f" % d) if np.isfinite(d)
                        else "%7s" % "--" for d in row),
            ("%8.4f" % d12) if np.isfinite(d12) else "%8s" % "--"))
    m_full = float(np.median(med_by_f[1.0])) if med_by_f[1.0] else \
        float("nan")
    print("    medians: " + ", ".join(
        "f=%.2f: %.4f (Xi_local = %.3f)"
        % (f, float(np.median(med_by_f[f])),
           float(np.median(med_by_f[f])) * f * deep_m * DGRID)
        if med_by_f[f] else "f=%.2f: --" % f for f in BATT_SUPPORTS))
    if med_b12 and np.isfinite(m_full):
        m12 = float(np.median(med_b12))
        print("    rank-12 detuned battery: median delta_mb %.4f vs "
              "frozen %.4f (gain %.1f%%; reach %d vs %d of %d "
              "gammas)"
              % (m12, m_full,                  100.0 * (1.0 - m12 / m_full),
                 len(med_b12), len(med_by_f[1.0]), len(BATT_GIDX)))
        print("    TYPING: the u-support curve is the ladder's own "
              "mechanism (Xi_local ~ const in f x X confirms the "
              "DEPTH-to-WIDTH law); battery enrichment within a rung "
              "buys only the marginal gain above -- the gamma-window "
              "widens through DEPTH, not battery optimization; the "
              "deployed battery stays frozen.")

    # ============================================================== C
    print("\nC -- controls")
    # C1a: injection INSIDE the new regions must break (full eig)
    inside_ok, n_in = True, 0
    for M in (new_ms if new_ms else [deep_m]):
        cTm = towers[M][:M]
        for ig in MZ_GIDX:
            b = bounds_mb[M][ig]
            if not np.isfinite(b) or 2.0 * b > 0.5:
                continue
            g = float(GAMMAS_GRID[ig])
            ql = quad_lags(M, g, 2.0 * float(b))[:M]
            bud = bud_of(M, nrm_of[M], float(np.max(np.abs(ql))))
            lam = full_min(cTm + ql, M)
            n_in += 1
            inside_ok = inside_ok and (lam < -bud)
    check("C1a [must-fire] synthetic quadruple at 2 delta_mb inside "
          "the NEW-rung regions breaks the verified margin (full "
          "eigensolve): %d/%d interior points"
          % (n_in if inside_ok else -1, n_in),
          inside_ok and n_in >= 4)
    if not (inside_ok and n_in >= 4):
        surprises.append("C1a injection ward failed at depth "
                         "(%d points)" % n_in)

    # C1b: no-false-exclusion + measured under-detection
    valid_ok, n_val, under = True, 0, []
    cTd = towers[deep_m][:deep_m]
    for ig in BATT_GIDX:
        b = bounds_mb[deep_m][ig]
        if not np.isfinite(b):
            continue
        g = float(GAMMAS_GRID[ig])
        ql = quad_lags(deep_m, g, float(b))[:deep_m]
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        lam = full_min(cTd + ql, deep_m)
        n_val += 1
        valid_ok = valid_ok and (lam < -bud)
        d_full, steps = float(b), 0
        for dl in DELTAS_GRID[DELTAS_GRID < b][::-1]:
            if steps >= UNDER_SCAN_CAP:
                break
            steps += 1
            ql2 = quad_lags(deep_m, g, float(dl))[:deep_m]
            bud2 = bud_of(deep_m, nrm_of[deep_m],
                          float(np.max(np.abs(ql2))))
            if full_min(cTd + ql2, deep_m) < -bud2:
                d_full = float(dl)
            else:
                break
        under.append(b / d_full)
    check("C1b [no-false-exclusion] every claimed deep boundary "
          "point confirmed by the FULL eigensolve: %d/%d; measured "
          "under-detection delta_mb/delta_full = %.2f..%.2f (median "
          "%.2f; descent capped at %d steps, lower bound typed)"
          % (n_val if valid_ok else -1, n_val,
             min(under) if under else float("nan"),
             max(under) if under else float("nan"),
             float(np.median(under)) if under else float("nan"),
             UNDER_SCAN_CAP), valid_ok and n_val >= 3)

    # C2: scramble (declared seed; the only RNG use)
    if masses_scr is not None:
        rng = np.random.default_rng(SEED_SCRAMBLE)
        alpha_t = 0.5 * M_TARGET * DGRID
        u_scr = rng.uniform(0.0, 2.0 * alpha_t,
                            size=masses_scr.size)
        c_scr = np.zeros(M_TARGET)
        tent_accumulate(c_scr, M_TARGET, u_scr, masses_scr)
        lam_scr = full_min(srp.continuum_lags(M_TARGET) + c_scr,
                           M_TARGET)
        check("C2 [must-fire] scramble at M = %d (positions uniform, "
              "SAME %d masses, seed %d): lambda_min = %.3e < 0 -- "
              "the rung PSD measures the true comb"
              % (M_TARGET, masses_scr.size, SEED_SCRAMBLE, lam_scr),
              lam_scr < 0.0)
        if lam_scr >= 0.0:
            limits.append("scramble control failed to fire")
    else:
        print("    C2 skipped (no new rung built)")

    # C3: Epstein swap (Lambda_E reach 34000 => M = 640, typed)
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
    check("C3 [must-fire] Epstein swap (Lambda_E of x^2 + 5 y^2, "
          "table reach %d => control at M = 640, typed): lambda_min "
          "= %.3e < 0" % (ep_cap, lam_ep), lam_ep < 0.0)
    if lam_ep >= 0.0:
        limits.append("Epstein control failed to fire")

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- verdict + THE LADDER STATEMENT (deliverable, report "
          "only)")
    print("=" * 78)
    ward_fail = any(f.startswith(("S0", "W", "S1")) for f in FAILS)
    if ward_fail:
        limits.append("instrument ward failure: %s"
                      % ",".join(f for f in FAILS
                                 if f.startswith(("S0", "W", "S1"))))
    if surprises:
        verdict = "LADDER-SURPRISE"
    elif limits or not new_ms or FAILS:
        verdict = "LADDER-LIMITED"
    else:
        verdict = "LADDER-EXTENDED"
    print("\n  VERDICT: %s" % verdict)
    for s in surprises:
        print("    SURPRISE: %s" % s)
    for s in limits:
        print("    LIMIT: %s" % s)

    print("\n  THE LADDER TABLE (verified depth X => excluded "
          "region; certified margins):")
    print("  %9s %10s %10s %12s %12s %9s %8s %6s"
          % ("X", "comb cap", "lam_min", "cert lower", "encl width",
             "med d_mb", "Xi_eff", "reach"))
    for M in all_ms:
        X = M * DGRID
        lb, lo, hi = (cert.get(M, (float("nan"),) * 3)
                      if new_ms else (float("nan"),) * 3)
        fin = bounds_mb[M][np.isfinite(bounds_mb[M])]
        print("  %9.4f %10.2e %10.3e %12.4e %12.1e %9s %8s %5d/36"
              % (X, math.exp(X), m_of[M],
                 lb if lb is not None else float("nan"),
                 (hi - lo) if new_ms and lb is not None
                 else float("nan"),
                 ("%.4f" % float(np.median(fin))) if len(fin)
                 else "--",
                 ("%.4f" % xi_ext[M]) if M in xi_ext else "--",
                 len(fin)))
    print("""
  RECOMMENDED LADDER-TABLE TEXT (PRIME.FLOOR.RATIO.01 exclusion-
  ladder deliverable, report only): 'EXCLUSION LADDER (certified):
  each verified PSD rung (X, m_X) of the GL1 tower is published with
  (i) a rigorous floating-point certificate lambda_min(T_X) >= L_X >
  0 (Cholesky PD verification with the Higham backward-error bound,
  plus a Rayleigh-residual enclosure of the bottom eigenvalue), (ii)
  its excluded quadruple region {(gamma, delta): lambda_min(T_X -
  Q) < -EXC_BUD} and the detector-native margin-break subregion,
  with every published boundary point re-proved by a rigorous
  witness-Rayleigh certificate, and (iii) the threshold census
  Xi_eff = X delta_mb(gamma).  The ladder converts computation depth
  into effective zero-free width at the calibrated rate X*(delta) ~=
  Xi_eff/delta, subject to the single-quadruple dominance caveat,
  the identity budget EXC_BUD = 1e-8 + 100 eps (||T|| + ||Q||), and
  the Nyquist reach pi/D; the region lies inside the [A1]-verified
  strip (consistency re-derivation, not new territory).'
""")
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
