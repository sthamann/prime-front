"""PRIME.FLOOR.DEPTHKILL.01 -- the authorized kill attempt on the
PRIME.FLOOR.RATIO.01 envelope gate at full sieve depth (EXPLORATION
ONLY, experiments/).

THE CONTRACT UNDER ATTACK (v818 / PRIME.FLOOR.RATIO.01, round 23):
the sector floor reduces to the single ratio inequality rho(X) =
tau(X)/tau_pnt(X) > 0 with the measured finite lower envelope
rho >= c h^{-3/2}, c = 4.85 (frozen, NO refit), envelope
non-decaying (slope +0.14, bar >= -0.10), capture angle-certified
(min cos^2 th >= 0.5).  PREREGISTERED KILL GATES (the contract's
own): (K1) the envelope failing at depth (rho h^{3/2} < 4.85 at any
rung); (K2) capture collapse (cos^2 th < 1/2 at any rung).  The
promoted measurements lived on the deployed frame-A ladder (67
rungs, e^{2 alpha} <= 4e5, i.e. 2 alpha <= 12.9).  THIS PROBE plays
the kill attempt at the certified exclusion-tower depths 2 alpha =
X = 18.375 .. 24.81 (and 25.5 if the predeclared benchmark allows),
via the fast segmented sieve (exclusion_ladder_deep_probe /
exclusion_range_extension_probe machinery, inherited verbatim).

THE DEEP FRAME (typed): the new rungs are the certified uniform-grid
tower windows D = 1/64, M in {1176, 1326, 1414, 1504, 1588(, 1632)}
(M = 1503 of the certified set is ODD; the frame-A parity split
demands even M, so the floor window at that depth runs at M = 1504,
X = 23.5 -- typed deviation; the lambda_min anchor is still warded
at the certified M = 1503).  Their half-dimensions h = M/2 = 588 ..
794 (816) sit INSIDE the deployed ladder's h-range [128, 1450] while
the depth 2 alpha jumps 12.9 -> 24.8: the deep extension DECOUPLES
depth from dimension -- if rho is an h-law (the contract's claim)
the frozen envelope must hold; if rho secretly decays with DEPTH the
kill fires.  Cross-frame comparison (frame-A gap-rule D vs uniform
D = 1/64) is a typed caveat, not hidden.

TASK (frozen):
 S1 RECONSTRUCT THE FROZEN OBJECTS: the deployed 67-rung ladder
    rebuilt bit for bit on the v818 part-2 recipe (v563 read-only:
    build_window; tau = bottom eig of the 2x2 lock block Ah = B - S;
    tau_pnt = bottom eig of B - S_pnt with the exact-partial-cell
    density integral, delta = D/4; rho = tau/tau_pnt; capture
    geometry per full_A + QR of the parity pair).  WARDS:
    (a) the promoted stats reproduce at printed precision:
        e1 = rho h^{3/2} in [4.85, 24.2], slope +0.14; capture
        median 1.53 (range 1.04..4.36); cos th median 0.9900;
        rho ~ h^-1.36;
    (b) INSTRUMENT PARITY rel <= 1e-6 on every overlap rung: the
        fast vectorized tent path (this probe's deep machinery, run
        at the window's own D on the SAME atom table) must reproduce
        the promoted tau and rho; cos^2 th on the stride-5 subset.
 S2 THE DEEP EXTENSION: predeclared cap rule t_proj(nmax) = t_bench
    x (nmax/nmax_1176) x 1.3 <= T_CAP = 1500 s decides the deepest
    rung (X = 25.5 has NO persistent cache -- it enters by the same
    rule only); one banded segmented-sieve pass per depth range;
    parity ward at M = 896 (fast path vs core.atom_lags_at, max |dc|
    <= 5e-9); lambda_min anchors at the certified rungs vs the cited
    values (rel <= 2e-2): 1176: 3.8825e-6, 1326: 2.4453e-6, 1414:
    2.0092e-6, 1503: 1.5883e-6, 1588: 1.0779e-6.
 S3 THE DEEP RUNG TABLE: per rung tau, tau_pnt, rho, e1 = rho
    h^{3/2}, envelope margin e1/4.85, cos^2 th, capture
    tau/lambda_min(A_h), eps = tau/lambda, conditioning.
 S4 THE GATE DECISION (the contract's frozen gates, no refit):
    K1 envelope: e1 >= 4.85 at every new rung, else the KILL fires;
    K2 capture: cos^2 th >= 0.5 at every new rung, else collapse;
    envelope slope update (new rungs; combined typed cross-frame),
    non-decay bar -0.10; capture median/range update.
 S5 MECHANISM AT DEPTH: the certified pair (pole x gamma_1) legs on
    the deep windows via the v692 conventions (odd_ext / F_of phase
    extraction / T_pair at +-i/2; gamma_1 = 14.1347 from the CACHED
    RvM ordinate list -- read for THIS comparison only; the rho
    measurement path stays zero-free); certified-brick lower bound
    rho_cert = pair/(lambda tau_pnt) vs measured rho per rung (ward:
    rho_cert <= rho); the pair-share h-law share = pair/det vs the
    Lagrange strand's cited h^1.06 growth (old-subset reproduction,
    soft tol +-0.40, typed) and its continuation at depth.
CONTROLS: C1 [must-fire] scramble at the first deep rung (M = 1176,
    positions uniform on (0, 2 alpha], SAME masses, seed 7 -- the
    only RNG use): rho must break in sign or scale; C2 Epstein comb
    (x^2 + 5 y^2, mass-matched) at M = 1176: the amplifier is
    measured and typed (different comb, different amplifier --
    measure, no hard bar per the task).
VERDICT (frozen enum): ENVELOPE-HOLDS-DEEP (fence survives, updated
    constants typed) / ENVELOPE-KILLED (K1 fired -- prominent honest
    report; the contract's own preregistration closes the ratio
    route) / CAPTURE-COLLAPSED (K2 fired -- same discipline).
    Ward/control failures typed prominently on the verdict line.

FIREWALL: v563 READ-ONLY; mpmath VALUES only (the v583 constant
-2 zeta'/zeta(1/2)); NO zetazero()/nzeros() calls (AST-checked); the
cached RvM ordinate list is read for the S5 mechanism comparison
only -- tau, tau_pnt, rho, cos^2 th are zero-free; RNG only in the
declared C1 scramble (seed 7); nothing outside experiments/ touched;
no marker moves.  NO RH claim.
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

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
from mpmath import mp, zeta, diff as mpdiff  # noqa: E402 (VALUES only)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
C_FROZEN = 4.85               # the contract envelope constant (NO refit)
ENV_SLOPE = -0.10             # frozen non-decay bar (v818 I3.C1)
COS2_MIN = 0.50               # frozen capture bar (v818 I1)
GRID_PER_D = 4.0              # v586 pnt_S convention
ANOMALOUS_H = 1292            # v563/v818 declaration
DGRID = 1.0 / 64.0            # the exclusion-tower grid
TARGET_MS = (1176, 1326, 1414, 1504, 1588, 1632)   # floor windows (even)
ANCHOR_MS = (1176, 1326, 1414, 1503, 1588)         # certified rungs
LAM_CITED = {1176: 3.8825e-6, 1326: 2.4453e-6, 1414: 2.0092e-6,
             1503: 1.5883e-6, 1588: 1.0779e-6}     # range-ext probe, cited
ANCH_REL = 2.0e-2
T_CAP = 1500.0                # predeclared projected-time cap (s)
PROJ_SAFETY = 1.3
SEG_ASC = 1 << 28
PARITY_M = 896                # parity ward rung (X = 14, table reach)
PARITY_C_ABS = 5.0e-9
INSTR_REL = 1.0e-6            # the task's reproduction bar
STRIDE = 5
SEED_SCRAMBLE = 7             # the only RNG use (C1)
GAMMA1_REF = 14.134725
HLAW_CITED = 1.06             # Lagrange strand certified-share h-law
HLAW_TOL = 0.40               # soft reproduction tolerance (typed)
# frozen printed-precision reproduction targets (v818, 2026-08-06):
REPRO = dict(e1_min=(4.85, 0.005), e1_max=(24.2, 0.05),
             e1_slope=(0.14, 0.005), rho_slope=(-1.36, 0.005),
             cap_med=(1.53, 0.005), cap_min=(1.04, 0.005),
             cap_max=(4.36, 0.005), cos_med=(0.9900, 5.0e-5))

mp.dps = 30
C_TH = float(-2 * mpdiff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)


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


def ols_loglog(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.abs(np.asarray(y)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), float(math.exp(q)), r2


def eig2(M2):
    """Closed-form 2x2 symmetric eigen (v818 part-2 convention)."""
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


# ------------------------------------------- v818 part-2 density recipe
def pnt_cells(W11, W22, W12, D, Mz, umax):
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((umax - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
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
    """v818 part-2 ingredient-(i) geometry, verbatim."""
    wA, VA = np.linalg.eigh(A)
    l1 = float(wA[0])
    u = VA[:, 0]
    Vq, _ = np.linalg.qr(np.stack([t1, t2], axis=1))
    Mq = Vq.T @ (A @ Vq)
    tau_q = float(np.linalg.eigvalsh(Mq)[0])
    pu = Vq.T @ u
    cos2 = float(pu @ pu)
    return dict(l1=l1, tau_q=tau_q, cos2=cos2)


# ------------------------------------------- fast tent + segmented sieve
def tent_accumulate_D(c, M, D, u, mu, chunk=4000000):
    """Deployed T115 tent convention (core.atom_lags_at), vectorized
    at grid D: offsets -2..2 with idx < M plus the u < D reflection."""
    for s in range(0, u.size, chunk):
        uu, mm = u[s:s + chunk], mu[s:s + chunk]
        i0 = np.floor(uu / D).astype(np.int64)
        for off in (-2, -1, 0, 1, 2):
            idx = i0 + off
            ok = (idx >= 0) & (idx < M)
            if not ok.any():
                continue
            v = 1.0 - np.abs(idx[ok] * D - uu[ok]) / D
            pos = v > 0.0
            if pos.any():
                c -= np.bincount(idx[ok][pos],
                                 weights=mm[ok][pos] * 0.5 * v[pos],
                                 minlength=M)
        refl = uu < D
        if refl.any():
            v = 1.0 - uu[refl] / D
            pos = v > 0.0
            if pos.any():
                c[0] -= float(np.sum(mm[refl][pos] * 0.5 * v[pos]))


def base_primes(n):
    sv = np.ones(n + 1, dtype=bool)
    sv[:2] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if sv[i]:
            sv[i * i::i] = False
    return np.flatnonzero(sv)


def nmax_of_M(M):
    return int(math.floor(math.exp(M * DGRID + 1.0e-14)))


def seg_sieve_bands(caps, n_lo, n_hi, acc, Mpad, cnt,
                    collect_mass_cap=None, seg=SEG_ASC):
    """Segmented Eratosthenes over prime powers in (n_lo, n_hi]; tent
    reads at grid DGRID accumulated into per-band arrays acc[band]
    (band = index of the smallest cap >= n), UNTRUNCATED to Mpad lags
    (rung M later reads sum(bands with cap <= nmax(M))[:M], exactly
    the per-rung tent truncation).  Optionally collects the retained
    mass multiset below collect_mass_cap (for the C1 scramble)."""
    caps = np.asarray(caps, dtype=np.int64)
    masses = [] if collect_mass_cap else None
    bp = base_primes(int(math.isqrt(n_hi)))
    for lo in range(0, n_hi + 1, seg):
        hi = min(lo + seg, n_hi + 1)
        if hi - 1 <= n_lo:
            continue
        sv = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            sv[:2] = False
        for p in bp:
            p = int(p)
            st = max(p * p, ((lo + p - 1) // p) * p)
            if st < hi:
                sv[st - lo::p] = False
        nn = np.flatnonzero(sv).astype(np.float64) + float(lo)
        nn = nn[nn > n_lo]
        if nn.size == 0:
            continue
        lg = np.log(nn)
        mu = 2.0 * lg / np.sqrt(nn)
        bidx = np.searchsorted(caps, nn.astype(np.int64), side="left")
        for b in np.unique(bidx):
            sel = bidx == b
            tent_accumulate_D(acc[b], Mpad, DGRID, lg[sel], mu[sel])
            cnt[b] += int(sel.sum())
        if masses is not None:
            keep = nn <= collect_mass_cap
            if keep.any():
                masses.append(mu[keep].copy())
    for p in bp:                             # prime powers p^k, k >= 2
        p = int(p)
        lp = math.log(p)
        q = p * p
        while q <= n_hi:
            if q > n_lo:
                u1 = np.array([math.log(q)])
                m1 = np.array([2.0 * lp / math.sqrt(q)])
                b = int(np.searchsorted(caps, q, side="left"))
                tent_accumulate_D(acc[b], Mpad, DGRID, u1, m1)
                cnt[b] += 1
                if masses is not None and q <= collect_mass_cap:
                    masses.append(m1.copy())
            q *= p
    return np.concatenate(masses) if masses else None


# ---------------------------------------------- v692 pair-leg conventions
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
    return np.exp(1j * np.outer(np.atleast_1d(np.asarray(phi, complex)),
                                jj)) @ f


def T_pair(f1, f2, D, z):
    z = np.asarray(z, dtype=complex)
    F1p, F1m = F_of(f1, D * z), F_of(f1, -D * z)
    F2p, F2m = F_of(f2, D * z), F_of(f2, -D * z)
    return csinc(D * z / 2.0) ** 2 * D * 0.5 * (F1p * F2m + F2p * F1m)


def pair_brick(t1, t2, D, Mz, gam1):
    """The certified fixed pair (pole x gamma_1): weighted squared
    cross-difference, v692/prime_lagrange_pair_probe conventions."""
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


# --------------------------------------------------- window evaluations
def floor_eval(t1, t2, W11, W22, W12, c_ar, c_at, D, Mz, full_geo=True):
    """tau, tau_pnt, rho, capture, cos^2 via the frozen recipes on one
    window (lag route for the lock block; T163-identical to B - S)."""
    hz = Mz // 2
    cc = c_ar + c_at
    Ah = np.array([[cc @ W11, cc @ W12], [cc @ W12, cc @ W22]])
    lam, tau, v1, _ = eig2(Ah)
    B2 = np.array([[c_ar @ W11, c_ar @ W12], [c_ar @ W12, c_ar @ W22]])
    edges, reads = pnt_cells(W11, W22, W12, D, Mz, Mz * D + 1e-9)
    Sp = pnt_S_of(edges, reads, Mz * D)
    _, tau_p, _, _ = eig2(B2 - Sp)
    out = dict(lam=lam, tau=tau, tau_pnt=tau_p,
               rho=tau / tau_p if tau_p != 0.0 else float("nan"),
               det=lam * tau, h=hz,
               onem=(lam * tau) / max(Ah[0, 0] * Ah[1, 1], 1e-300))
    if full_geo:
        A = core.odd_toeplitz(cc, Mz)
        g = capture_geometry(t1, t2, A)
        out.update(lmin_A=g["l1"], cos2=g["cos2"],
                   cap=tau / g["l1"] if g["l1"] != 0.0 else float("nan"))
        del A
    return out


def deep_window(Mz, c_at):
    """The uniform-grid tower window frame (D = 1/64) with the frame-A
    parity split, v563 conventions verbatim."""
    hz = Mz // 2
    Tb = core.parity_basis(hz, 2)
    t1, t2 = Tb[0].copy(), Tb[1].copy()
    W11 = core.lag_weights_from_v(t1, hz)
    W22 = core.lag_weights_from_v(t2, hz)
    Wpp = core.lag_weights_from_v(t1 + t2, hz)
    W12 = 0.5 * (Wpp - W11 - W22)
    c_ar = np.asarray(core.arch_lags(Mz, DGRID), float)
    return dict(M=Mz, h=hz, D=DGRID, alpha=0.5 * Mz * DGRID,
                t1=t1, t2=t2, W11=W11, W22=W22, W12=W12,
                c_ar=c_ar, c_at=c_at)


def epstein_counts(Nmax):
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


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.FLOOR.DEPTHKILL.01 -- the envelope-gate kill attempt "
          "at sieve depth (floor_envelope_depth_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- firewall + frozen gates")
    check("S0.AST no zeta-zero generator call in this file "
          "(zetazero/nzeros/find_zeros absent); mpmath = the v583 "
          "constant -2 zeta'/zeta(1/2) = %.4f only; RNG only in the "
          "declared C1 scramble (seed %d)" % (C_TH, SEED_SCRAMBLE),
          ast_zero_firewall(__file__))
    g1 = float(json.load(open(os.path.join(
        _here, "zero_comb_cache_n2000.json")))["gammas"][0])
    check("S0.G1 cached RvM ordinate gamma_1 = %.6f (read for the S5 "
          "mechanism comparison ONLY; tau/tau_pnt/rho/cos^2 stay "
          "zero-free)" % g1, abs(g1 - GAMMA1_REF) < 1e-5)
    print("    frozen kill gates (the contract's own): K1 envelope "
          "rho h^{3/2} >= c = %.2f (NO refit); K2 capture cos^2 th "
          ">= %.2f; non-decay bar slope >= %.2f"
          % (C_FROZEN, COS2_MIN, ENV_SLOPE))

    # ============================================================== S1
    print("\nS1 -- reconstruct the frozen objects (deployed 67-rung "
          "ladder, v818 part-2 recipe)")
    t0 = time.time()
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        l1v, l2v, v1, _ = eig2(rr["Ah"])
        w = dict(rr=rr, kz=kz, h=rr["h"], alpha=rr["alpha"],
                 lam=l1v, tau=l2v)
        rows.append(w)
    rows.sort(key=lambda w: w["alpha"])
    hs = [w["h"] for w in rows]
    check("S1.SET the deployed ladder: %d regular complete windows, "
          "alpha %.3f..%.3f, h %d..%d (the promoted 67-rung surface)"
          % (len(rows), rows[0]["alpha"], rows[-1]["alpha"],
             min(hs), max(hs)), len(rows) == 67)

    # frozen tau_pnt + capture per rung (promoted recipe) and the fast
    # instrument in parallel (parity ward)
    worst_tau, worst_rho = 0.0, 0.0
    for w in rows:
        rr = w["rr"]
        edges, reads = pnt_cells(rr["W11"], rr["W22"], rr["W12"],
                                 rr["D"], rr["M"],
                                 2.0 * rr["alpha"] + 1e-9)
        Sp = pnt_S_of(edges, reads, 2.0 * rr["alpha"])
        _, tau_p, _, _ = eig2(rr["B"] - Sp)
        w["tau_pnt"] = tau_p
        w["rho"] = w["tau"] / tau_p
        # fast instrument: vectorized tent at the window's own D
        c_fast = np.zeros(rr["M"])
        tent_accumulate_D(c_fast, rr["M"], rr["D"], rr["uu"],
                          2.0 * rr["lam"])
        w["c_at_fast"] = c_fast
        ev = floor_eval(rr["t1"], rr["t2"], rr["W11"], rr["W22"],
                        rr["W12"],
                        np.asarray(core.arch_lags(rr["M"], rr["D"]),
                                   float),
                        c_fast, rr["D"], rr["M"], full_geo=True)
        w["fast"] = ev
        w["cos2"] = ev["cos2"]
        w["lmin_A"] = ev["lmin_A"]
        w["cap"] = w["tau"] / ev["lmin_A"]
        worst_tau = max(worst_tau, abs(ev["tau"] - w["tau"])
                        / abs(w["tau"]))
        worst_rho = max(worst_rho, abs(ev["rho"] - w["rho"])
                        / abs(w["rho"]))
    print("    rebuilt in %.1f s" % (time.time() - t0))

    e1 = [w["rho"] * w["h"] ** 1.5 for w in rows]
    sl_e1, _, r2_e1 = ols_loglog(hs, e1)
    sl_rho, _, _ = ols_loglog(hs, [w["rho"] for w in rows])
    caps = [w["cap"] for w in rows]
    cos_med = float(np.median(np.sqrt([w["cos2"] for w in rows])))
    stats = dict(e1_min=min(e1), e1_max=max(e1), e1_slope=sl_e1,
                 rho_slope=sl_rho, cap_med=float(np.median(caps)),
                 cap_min=min(caps), cap_max=max(caps), cos_med=cos_med)
    rep_ok = True
    for kk, (tgt, tol) in REPRO.items():
        ok = abs(stats[kk] - tgt) <= tol
        rep_ok = rep_ok and ok
        print("    repro %-9s = %10.4f vs promoted %8.4f (tol %.0e) %s"
              % (kk, stats[kk], tgt, tol, "ok" if ok else "MISS"))
    check("S1.REPRO the promoted v818 statistics reproduce at printed "
          "precision: envelope e1 in [%.2f, %.1f] slope %+.2f (R^2 "
          "%.2f), rho ~ h^%.2f, capture median %.2f (%.2f..%.2f), "
          "cos th median %.4f"
          % (stats["e1_min"], stats["e1_max"], sl_e1, r2_e1, sl_rho,
             stats["cap_med"], stats["cap_min"], stats["cap_max"],
             cos_med), rep_ok)
    check("S1.PARITY instrument parity on ALL %d overlap rungs: the "
          "fast vectorized tent path reproduces the promoted tau "
          "(worst rel %.1e) and rho (worst rel %.1e) <= %.0e"
          % (len(rows), worst_tau, worst_rho, INSTR_REL),
          worst_tau <= INSTR_REL and worst_rho <= INSTR_REL)
    sub5 = rows[::STRIDE]
    worst_cos = 0.0
    for w in sub5:
        rr = w["rr"]
        c_at_slow, _ = core.atom_lags_at(rr["alpha"], rr["M"],
                                         rr["uu"], 2.0 * rr["lam"])
        A_slow = core.odd_toeplitz(
            np.asarray(core.arch_lags(rr["M"], rr["D"]), float)
            + c_at_slow, rr["M"])
        g = capture_geometry(rr["t1"], rr["t2"], A_slow)
        del A_slow
        worst_cos = max(worst_cos, abs(g["cos2"] - w["cos2"])
                        / abs(g["cos2"]))
    check("S1.PARITY2 cos^2 th parity on the stride-%d subset (%d "
          "windows): fast vs deployed path worst rel %.1e <= %.0e"
          % (STRIDE, len(sub5), worst_cos, INSTR_REL),
          worst_cos <= INSTR_REL)

    # ============================================================== S2
    print("\nS2 -- the deep extension (benchmark + predeclared cap)")
    # parity ward at M = PARITY_M against the deployed slow path
    n_pw = nmax_of_M(PARITY_M)
    lam_tab = core.von_mangoldt_table(n_pw)
    nn0 = np.nonzero(lam_tab > 0.0)[0]
    u_pw = np.log(nn0.astype(float))
    mu_pw = 2.0 * lam_tab[nn0] / np.sqrt(nn0.astype(float))
    del lam_tab
    c_slow, _ = core.atom_lags_at(0.5 * PARITY_M * DGRID, PARITY_M,
                                  u_pw, mu_pw)
    acc_pw = {0: np.zeros(PARITY_M + 3)}
    cnt_pw = {0: 0}
    seg_sieve_bands([n_pw], 0, n_pw, acc_pw, PARITY_M + 3, cnt_pw)
    dev_pw = float(np.max(np.abs(acc_pw[0][:PARITY_M] - c_slow)))
    check("S2.PARITY segmented banded assembly == deployed T115 path "
          "at M = %d (X = %.2f, %d atoms): max |dc| = %.2e <= %.0e"
          % (PARITY_M, PARITY_M * DGRID, cnt_pw[0], dev_pw,
             PARITY_C_ABS),
          cnt_pw[0] == len(u_pw) and dev_pw <= PARITY_C_ABS)

    # benchmark pass: the first deep rung (M = 1176) + mass multiset
    ms_all = sorted(set(TARGET_MS) | set(ANCHOR_MS))
    caps_all = [nmax_of_M(M) for M in ms_all]
    Mpad = max(ms_all) + 3
    acc = {b: np.zeros(Mpad) for b in range(len(ms_all))}
    cnt = {b: 0 for b in range(len(ms_all))}
    n_1176 = nmax_of_M(1176)
    t0 = time.time()
    masses_scr = seg_sieve_bands(caps_all, 0, n_1176, acc, Mpad, cnt,
                                 collect_mass_cap=n_1176)
    t_bench = time.time() - t0
    print("    benchmark: sieve+reads to n = %d (%d atoms) in %.1f s"
          % (n_1176, cnt[0], t_bench))
    proj = {M: t_bench * (nmax_of_M(M) / n_1176) * PROJ_SAFETY
            for M in ms_all}
    deep_ms = [M for M in TARGET_MS if proj[M] <= T_CAP]
    dropped = [M for M in TARGET_MS if M not in deep_ms]
    print("    predeclared cap rule: t_proj = t_bench x (nmax/nmax_"
          "1176) x %.1f <= %.0f s" % (PROJ_SAFETY, T_CAP))
    for M in TARGET_MS:
        print("      M = %4d (X = %8.4f, cap e^X = %.3e): t_proj = "
              "%7.0f s -> %s" % (M, M * DGRID, math.exp(M * DGRID),
                                 proj[M],
                                 "BUILD" if M in deep_ms else "DROP"))
    if dropped:
        print("    DROPPED by the predeclared rule: %s (X = 25.5 has "
              "no persistent cache -- typed, not hidden)"
              % ", ".join("M=%d" % M for M in dropped))
    build_ms = sorted(set(deep_ms)
                      | set(M for M in ANCHOR_MS
                            if nmax_of_M(M) <= nmax_of_M(
                                max(deep_ms))))
    n_deep = nmax_of_M(max(build_ms))
    t0 = time.time()
    seg_sieve_bands(caps_all, n_1176, n_deep, acc, Mpad, cnt)
    t_deep = time.time() - t0
    print("    deep sieve+reads to n = %d: %.1f s (projected %.0f s)"
          % (n_deep, t_deep, proj[max(build_ms)]))

    def c_of(M):
        nm = nmax_of_M(M)
        c = np.zeros(M)
        for b, cap in enumerate(caps_all):
            if cap <= nm:
                c += acc[b][:M]
        return c

    # lambda_min anchors at the certified rungs
    anch_ok = True
    import v755_simpler_schur_recursion as srp   # READ-ONLY
    for M in [M for M in ANCHOR_MS if M in build_ms]:
        cT = srp.continuum_lags(M)[:M] + c_of(M)[:M]
        lamM = float(sla.eigvalsh(sla.toeplitz(cT),
                                  subset_by_index=[0, 0])[0])
        rel = abs(lamM - LAM_CITED[M]) / LAM_CITED[M]
        ok = rel <= ANCH_REL
        anch_ok = anch_ok and ok
        print("    anchor M = %4d: lambda_min = %.4e vs cited %.4e "
              "(rel %.3f) %s" % (M, lamM, LAM_CITED[M], rel,
                                 "ok" if ok else "MISS"))
    check("S2.ANCH the certified-rung lambda_min anchors reproduce "
          "(rel <= %.2f) on every built certified rung" % ANCH_REL,
          anch_ok)

    # ============================================================== S3
    print("\nS3 -- THE DEEP RUNG TABLE (frozen recipes on the "
          "uniform-grid tower frames)")
    deep = []
    for M in deep_ms:
        t0 = time.time()
        dw = deep_window(M, c_of(M))
        ev = floor_eval(dw["t1"], dw["t2"], dw["W11"], dw["W22"],
                        dw["W12"], dw["c_ar"], dw["c_at"], DGRID, M,
                        full_geo=True)
        ev.update(M=M, X=M * DGRID, alpha=dw["alpha"], dw=dw,
                  t_s=time.time() - t0)
        deep.append(ev)
    print("    %5s %8s %5s | %11s %11s %11s | %9s %8s | %7s %7s"
          % ("M", "X", "h", "lambda", "tau", "tau_pnt", "rho",
             "e1=rh^1.5", "cos^2", "capt"))
    for ev in deep:
        ev["e1"] = ev["rho"] * ev["h"] ** 1.5
        print("    %5d %8.4f %5d | %11.4e %11.4e %11.4e | %9.3e "
              "%8.3f | %7.4f %7.2f"
              % (ev["M"], ev["X"], ev["h"], ev["lam"], ev["tau"],
                 ev["tau_pnt"], ev["rho"], ev["e1"], ev["cos2"],
                 ev["cap"]))
    fl_ok = True
    for ev in deep:
        bar = 64.0 * np.finfo(float).eps / max(abs(ev["onem"]), 1e-300)
        ev["cond_ok"] = bar < 0.25
        fl_ok = fl_ok and ev["cond_ok"]
    check("S3.FLOAT conditioning at depth: the v818 conditioning bar "
          "64 eps_mach/onem stays a small fraction of the identity "
          "(worst onem = %.2e; tau resolvable in float at every deep "
          "rung)" % min(abs(ev["onem"]) for ev in deep), fl_ok)
    check("S3.PNT the density transversal stays positive at depth "
          "(tau_pnt = %.3e..%.3e > 0; the ratio is well-defined)"
          % (min(ev["tau_pnt"] for ev in deep),
             max(ev["tau_pnt"] for ev in deep)),
          all(ev["tau_pnt"] > 0.0 for ev in deep))

    # ============================================================== S4
    print("\nS4 -- THE GATE DECISION (frozen gates, no refit)")
    k1_viol = [ev for ev in deep if ev["e1"] < C_FROZEN]
    k2_viol = [ev for ev in deep if ev["cos2"] < COS2_MIN]
    for ev in deep:
        print("    X = %8.4f: envelope margin e1/c = %6.3f %s | "
              "cos^2 = %.4f %s"
              % (ev["X"], ev["e1"] / C_FROZEN,
                 "HOLDS" if ev["e1"] >= C_FROZEN else "**KILL**",
                 ev["cos2"],
                 "ok" if ev["cos2"] >= COS2_MIN else "**COLLAPSE**"))
    check("S4.K1 THE ENVELOPE GATE: rho h^{3/2} >= c = %.2f (frozen, "
          "no refit) at every new depth -- %d/%d rungs hold, min "
          "margin %.3f"
          % (C_FROZEN, len(deep) - len(k1_viol), len(deep),
             min(ev["e1"] / C_FROZEN for ev in deep)),
          not k1_viol)
    check("S4.K2 THE CAPTURE GATE: cos^2 th >= %.2f at every new "
          "depth -- %d/%d rungs hold, min cos^2 = %.4f"
          % (COS2_MIN, len(deep) - len(k2_viol), len(deep),
             min(ev["cos2"] for ev in deep)),
          not k2_viol)
    e1_new = [ev["e1"] for ev in deep]
    h_new = [ev["h"] for ev in deep]
    if len(set(h_new)) >= 2:
        sl_new, _, r2_new = ols_loglog(h_new, e1_new)
    else:
        sl_new, r2_new = float("nan"), 0.0
    e1_all = e1 + e1_new
    h_all = hs + h_new
    sl_all, _, r2_all = ols_loglog(h_all, e1_all)
    x_new = [ev["X"] for ev in deep]
    sl_X, _, r2_X = ols_loglog([math.exp(x) for x in x_new], e1_new)
    print("    envelope slope update: new rungs e1 ~ h^%+.2f (R^2 "
          "%.2f; h range %d..%d only -- weak lever, typed); combined "
          "old+new e1 ~ h^%+.2f (R^2 %.2f; CROSS-FRAME, typed); the "
          "depth reading e1 ~ (e^X)^%+.3f i.e. e1 ~ X-depth slope "
          "%+.3f per log-unit (R^2 %.2f)"
          % (sl_new, r2_new, min(h_new), max(h_new), sl_all, r2_all,
             sl_X, sl_X, r2_X))
    cap_all = caps + [ev["cap"] for ev in deep]
    print("    capture update: new rungs %.2f..%.2f; combined median "
          "%.2f (range %.2f..%.2f) vs promoted 1.53 (1.04..4.36)"
          % (min(ev["cap"] for ev in deep),
             max(ev["cap"] for ev in deep),
             float(np.median(cap_all)), min(cap_all), max(cap_all)))
    nd_ok = (min(e1_new) >= min(e1)) if e1_new else False
    check("S4.SLOPE non-decay at depth: every new e1 (min %.2f) sits "
          "at or above the old-ladder floor %.2f and the depth trend "
          "is %s (slope %+.3f vs bar %.2f)"
          % (min(e1_new), min(e1),
             "non-decaying" if sl_X >= ENV_SLOPE else "DECAYING",
             sl_X, ENV_SLOPE),
          nd_ok and sl_X >= ENV_SLOPE)

    # ============================================================== S5
    print("\nS5 -- mechanism at depth: the certified pair vs the "
          "measured rho")
    sub_m = rows[::STRIDE]
    for w in sub_m:
        rr = w["rr"]
        w["pair"] = pair_brick(rr["t1"], rr["t2"], rr["D"], rr["M"],
                               g1)
        w["share"] = w["pair"] / (w["lam"] * w["tau"])
        w["rho_cert"] = w["pair"] / (w["lam"] * w["tau_pnt"])
    for ev in deep:
        dw = ev["dw"]
        ev["pair"] = pair_brick(dw["t1"], dw["t2"], DGRID, ev["M"],
                                g1)
        ev["share"] = ev["pair"] / ev["det"]
        ev["rho_cert"] = ev["pair"] / (ev["lam"] * ev["tau_pnt"])
    s_old, _, r2_so = ols_loglog([w["h"] for w in sub_m],
                                 [w["share"] for w in sub_m])
    print("    old-subset certified-pair share ~ h^%+.2f (R^2 %.2f) "
          "vs the Lagrange strand's cited h^%+.2f (soft tol %.2f)"
          % (s_old, r2_so, HLAW_CITED, HLAW_TOL))
    print("    %8s %5s | %11s %11s %8s | %10s %10s %8s"
          % ("X", "h", "pair", "det", "share", "rho_cert", "rho",
             "gap x"))
    for w in sub_m[-3:]:
        print("    %8.4f %5d | %11.3e %11.3e %8.5f | %10.3e %10.3e "
              "%8.1f" % (2 * w["alpha"], w["h"], w["pair"],
                         w["lam"] * w["tau"], w["share"],
                         w["rho_cert"], w["rho"],
                         w["rho"] / max(w["rho_cert"], 1e-300)))
    for ev in deep:
        print("    %8.4f %5d | %11.3e %11.3e %8.5f | %10.3e %10.3e "
              "%8.1f" % (ev["X"], ev["h"], ev["pair"], ev["det"],
                         ev["share"], ev["rho_cert"], ev["rho"],
                         ev["rho"] / max(ev["rho_cert"], 1e-300)))
    brick_ok = all(w["rho_cert"] <= w["rho"] * (1.0 + 1e-9)
                   for w in sub_m) \
        and all(ev["rho_cert"] <= ev["rho"] * (1.0 + 1e-9)
                for ev in deep)
    check("S5.BRICK coherence: the certified-brick lower bound "
          "rho_cert = pair/(lambda tau_pnt) sits BELOW the measured "
          "rho on every rung (old subset + deep; sum-of-squares "
          "direction, tail psd per the Lagrange strand)", brick_ok)
    hl_ok = abs(s_old - HLAW_CITED) <= HLAW_TOL
    gap_old = [w["rho"] / max(w["rho_cert"], 1e-300) for w in sub_m]
    gap_new = [ev["rho"] / max(ev["rho_cert"], 1e-300) for ev in deep]
    sl_gap, _, _ = ols_loglog([math.exp(ev["X"]) for ev in deep],
                              gap_new)
    check("S5.HLAW the pair h-law: old-subset share exponent %+.2f "
          "within %.2f of the cited %+.2f; deep share %.5f..%.5f; "
          "gap rho/rho_cert old %.0f..%.0f -> deep %.0f..%.0f "
          "(depth trend %+.3f per log-unit) -- typed"
          % (s_old, HLAW_TOL, HLAW_CITED,
             min(ev["share"] for ev in deep),
             max(ev["share"] for ev in deep),
             min(gap_old), max(gap_old), min(gap_new), max(gap_new),
             sl_gap), hl_ok)

    # ============================================================== C
    print("\nC -- controls (at the first deep rung M = 1176, "
          "X = 18.375)")
    M0 = 1176
    dw0 = next(ev["dw"] for ev in deep if ev["M"] == M0)
    ev0 = next(ev for ev in deep if ev["M"] == M0)
    rng = np.random.default_rng(SEED_SCRAMBLE)
    u_scr = rng.uniform(0.0, M0 * DGRID, size=masses_scr.size)
    c_scr = np.zeros(M0)
    tent_accumulate_D(c_scr, M0, DGRID, u_scr, masses_scr)
    ev_s = floor_eval(dw0["t1"], dw0["t2"], dw0["W11"], dw0["W22"],
                      dw0["W12"], dw0["c_ar"], c_scr, DGRID, M0,
                      full_geo=False)
    scale_broken = (ev_s["tau"] < 0.0
                    or abs(math.log(max(abs(ev_s["rho"]), 1e-300)
                                    / abs(ev0["rho"]))) > math.log(3.0))
    check("C1 [must-fire] scramble at M = %d (positions uniform, SAME "
          "%d masses, seed %d): tau %.3e -> %.3e, rho %.3e -> %.3e "
          "-- sign/scale %s"
          % (M0, masses_scr.size, SEED_SCRAMBLE, ev0["tau"],
             ev_s["tau"], ev0["rho"], ev_s["rho"],
             "BROKEN (fires)" if scale_broken else "NOT broken"),
          scale_broken)

    t0 = time.time()
    cntE = epstein_counts(nmax_of_M(M0))
    nnE = np.nonzero(cntE[2:])[0].astype(np.int64) + 2
    uuE = np.log(nnE.astype(float))
    mE = cntE[nnE].astype(float) / np.sqrt(nnE.astype(float))
    del cntE
    kap = float(np.sum(masses_scr)) / float(np.sum(mE))
    cE = np.zeros(M0)
    tent_accumulate_D(cE, M0, DGRID, uuE, kap * mE)
    ev_e = floor_eval(dw0["t1"], dw0["t2"], dw0["W11"], dw0["W22"],
                      dw0["W12"], dw0["c_ar"], cE, DGRID, M0,
                      full_geo=False)
    check("C2 [typing] Epstein x^2+5y^2 comb at M = %d (mass-matched "
          "kappa = %.4f, %d atoms, %.0f s): tau_E = %.3e, rho_E = "
          "%.3e vs real rho %.3e (ratio %.2f), e1_E = %.2f vs frozen "
          "c %.2f -- the deep amplifier is %s (measured, typed as it "
          "falls)"
          % (M0, kap, len(nnE), time.time() - t0, ev_e["tau"],
             ev_e["rho"], ev0["rho"],
             ev_e["rho"] / ev0["rho"],
             ev_e["rho"] * (M0 // 2) ** 1.5, C_FROZEN,
             "comb-specific (Epstein leaves the real envelope band)"
             if abs(math.log(max(abs(ev_e["rho"]), 1e-300)
                             / abs(ev0["rho"]))) > math.log(1.5)
             else "density-level at this depth (Epstein tracks)"),
          True)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- VERDICT (frozen enum; report only, nothing outside "
          "experiments/ touched)")
    print("=" * 78)
    ward_fail = [f for f in FAILS if f.startswith(("S0", "S1", "S2"))]
    if k1_viol:
        verdict = "ENVELOPE-KILLED"
    elif k2_viol:
        verdict = "CAPTURE-COLLAPSED"
    else:
        verdict = "ENVELOPE-HOLDS-DEEP"
    print("\n  VERDICT: %s%s" % (verdict,
          ("  [WARD FAILURES: %s -- typed prominently]"
           % ",".join(ward_fail)) if ward_fail else ""))
    if k1_viol:
        print("  ** THE KILL GATE K1 FIRED: rho h^{3/2} < %.2f at %s"
              " -- per the contract's own preregistration this "
              "closes the ratio route; the status note is a separate "
              "authorized round. **"
              % (C_FROZEN, ", ".join("X=%.3f (e1=%.2f)"
                                     % (ev["X"], ev["e1"])
                                     for ev in k1_viol)))
    if k2_viol:
        print("  ** THE KILL GATE K2 FIRED: cos^2 th < %.2f at %s **"
              % (COS2_MIN, ", ".join("X=%.3f (%.4f)"
                                     % (ev["X"], ev["cos2"])
                                     for ev in k2_viol)))
    if not k1_viol and not k2_viol:
        print("""
  THE FENCE SURVIVES ITS STRONGEST TEST: at depths 2 alpha = X =
  %.3f..%.3f (comb caps to %.1e; %.1fx the promoted depth in
  log-scale) the frozen envelope rho h^{3/2} >= %.2f holds with
  minimum margin x%.3f, and the capture angle stays >= %.4f
  (bar %.2f).  Updated constants (typed): new-rung e1 %.2f..%.2f;
  depth slope %+.3f per log-unit (non-decay bar %.2f); combined
  capture median %.2f (%.2f..%.2f).""" % (
            deep[0]["X"], deep[-1]["X"],
            math.exp(deep[-1]["X"]),
            deep[-1]["X"] / (2.0 * rows[-1]["alpha"]), C_FROZEN,
            min(ev["e1"] / C_FROZEN for ev in deep),
            min(ev["cos2"] for ev in deep), COS2_MIN,
            min(e1_new), max(e1_new), sl_X, ENV_SLOPE,
            float(np.median(cap_all)), min(cap_all), max(cap_all)))
    print("""
  HONESTY: the deep rungs are uniform-grid (D = 1/64) tower frames
  with h = %d..%d INSIDE the deployed h-range while the depth
  2 alpha jumps %.1f -> %.1f -- the test decouples depth from
  dimension (cross-frame comparison typed); the certified set X =
  23.484 runs evenized at X = 23.5 for the parity split; X = 25.5
  %s; interlacing still runs floor => margin only; nothing here
  bounds inf_X lambda_min from below; NO RH claim."""
          % (min(h_new), max(h_new), 2.0 * rows[-1]["alpha"],
             deep[-1]["X"],
             "was included" if 1632 in deep_ms else
             "was dropped by the predeclared benchmark rule (no "
             "persistent cache)"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
