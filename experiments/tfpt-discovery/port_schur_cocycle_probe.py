#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_schur_cocycle_probe -- PRIME.PORT.SCHURSTEP.01
(EXPLORATION ONLY, experiments/; round 45, probe 4 of the new
review: does the window ladder carry an exact DISCRETE Moebius/
Schur step -- wild local coefficients but an exact multiplicative
cocycle, 2026-08-09).

THE QUESTION (frozen): the ladder as a PATH is noise in every
tested conditioning (conditioned_lax_flow_probe: FLOW-FLAT), but
the INTEGRATED tau-transfer identity is EXACT (lax2_flow_probe
X4, warded at 5.6e-11) and the compressed 12x12 window converges
(port_cocycle_window_probe).  The review's point: lawful point
set + noisy generator + exact multiplicative transfer is the
signature of a DISCRETE Schur/Moebius dynamics -- seek the update
m_{h+1} = (a m_h + b)/(c m_h + d) or the matrix Schur step with
tau_{h+1}/tau_h = det(I - alpha_h^* alpha_h), NOT a differential
law.

THE LADDER (frozen): all frame-A zones (core.frame_a_zones())
with h <= 900, sorted by (h, kz); consecutive rung pairs.  S1
runs on FULL-WINDOW pairs (both rungs carry all 12 indices of
J = {2, 4, ..., 24}; typed skips counted); S2 runs on pairs with
>= 8 common port alias indices j (typed skips counted).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 S1  THE EXACT TAU QUOTIENT AS A SCHUR DETERMINANT: on the fixed
     12-index window let W_h = I - C_J(h) (Schur-compressed
     Carleson window, port_cocycle_window_probe verbatim).  The
     exact quotient identity
       det(W_{h+1})/det(W_h) = det(I + W_h^{-1}(C_h - C_{h+1}))
     is pure matrix algebra: WARDED at 1e-10 relative on every
     full-window pair (kill -> WARD-BROKEN).  THE SCHUR FORM
     TEST: a naive matrix Schur parameter alpha_h of rank r <= 2
     exists only if the step Delta_h = C_{h+1} - C_h is
     numerically low-rank.  Per step: print the singular-value
     profile of Delta_h and the effective rank at the 90% energy
     level (smallest r with sum_{i<=r} sv_i^2 >= 0.90 sum sv^2);
     report the rank-r Weinstein-Aronszajn reduction
       q_r = det(I_r - V_r^T W_h^{-1} U_r S_r)
     and its relative error against the exact quotient; report
     the naive rank-1 datum |alpha_h| = sqrt(1 - q_h) (Jacobian
     J_h = 1) where the exact quotient q_h lies in (0, 1).
     TYPED: STEP-LOWRANK iff eff rank <= 2 on >= 80% of the
     full-window steps, else STEP-FULLRANK (honest -- then the
     naive matrix alpha_h does not exist and the Moebius step
     must live on the FUNCTION m, S2).

 S2  THE MOEBIUS STEP ON THE CARRIER (the review's 'new clock'):
     per rung extract the scalar carrier m_h(y_j) = g_j / f_j at
     the port nodes ((f, g) = the gauge-fixed IIKS generators of
     the dressed port D_P, port_riemann_hilbert_setup SPEC v2
     extraction, pipeline verbatim from lax2_flow_probe).  All
     carrier arithmetic is HOMOGENEOUS on RP^1 (pairs (g_j, f_j),
     chordal metric |u w' - w u'| on unit pairs) so f ~ 0 nodes
     are regular points, and the SO(2) gauge acts as a Moebius
     map -- the normalization below quotients it out exactly.
     FROZEN NORMALIZATION: per rung, the unique PSL(2, R) map
     sending the carrier values at the three DEEPEST common
     nodes (the three smallest common alias indices j0 < j1 <
     j2; smallest j = smallest port coordinate tau_m = deepest
     port node) to (0, 1, infinity); a step whose reference
     values are degenerate (chordal separation <= 1e-6 or
     singular normalizer) is a typed skip (counted).  THE STEP
     TEST: in the normalized gauge fit ONE Moebius map (a, b, c,
     d) per step by total least squares on all common nodes
     (3 real dof against >= 8 nodes, overdetermined); the
     per-step residual = median chordal deviation over the
     NON-REFERENCE common nodes (the three reference nodes are
     pinned by the normalization and would deflate the median).
     TYPED on the median over steps of the per-step residuals:
     MOEBIUS-STEP iff <= 0.05 (a real discrete integrable step
     -- the conditioned flow the raw coefficients masked);
     MOEBIUS-PARTIAL iff <= 0.2; MOEBIUS-DEAD otherwise (honest
     -- closes the review's route 5 cleanly).

 S3  CONTRACTIVITY CENSUS (only meaningful if S1 or S2 typed
     positive; computed and reported regardless, typed N/A if
     both are negative): (a) the exact-quotient census: fraction
     of full-window steps with q_h in (0, 1) -- exactly where
     the naive rank-1 Schur datum |alpha_h| = sqrt(1 - q_h) < 1
     exists with J_h = 1; (b) the fitted-map census: per S2 step
     the Cayley datum alpha_h = (T_h(i) - i)/(T_h(i) + i) of the
     fitted map T_h; |alpha_h| < 1 iff T_h preserves the upper
     half plane (det > 0) -- the J-contraction census on truth.
     On the controls the ladder census cannot run (single rung):
     the frame must die instead -- reported (C).

 W   PIPELINE WARDS: W1 >= 30 rungs built; W2 [Y, D_P] rank 2 on
     every rung (s3/s1 <= 1e-10); W3 >= 20 full-window S1 pairs
     AND det(W_h) > 0 on every full-window rung (PD window on
     truth); W4 >= 30 S2 pairs with >= 8 common j.

 C   CONTROLS (kz 9, must fire): Epstein (lambda_eps recursion
     comb) + scramble (seed 1): the compressed frame must die --
     I - E_out indefinite (lam(out) > 1) OR lam(C_J) > 1 OR the
     window is unavailable (frame death, typed); which one fires
     is reported, as in the previous window probes.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW the exact
quotient identity breaks -> WARD-BROKEN; K3 controls silent ->
CONTROL-DEAD.

VERDICT (frozen enum): SCHURSTEP-MEASURED with typed sublabels
STEP-LOWRANK / STEP-FULLRANK (S1) and MOEBIUS-STEP /
MOEBIUS-PARTIAL / MOEBIUS-DEAD (S2), plus the S3 census report;
else PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

NO RH claim -- a discrete Schur step on the window ladder is a
numerical measurement on compressed truncations, not a theorem
about zeros.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; window compression
verbatim from port_cocycle_window_probe.py (PRIME.PORT.
COCYCLE.01); IIKS generator pipeline verbatim from
lax2_flow_probe.py (PRIME.PORT.LAX2.01, itself verbatim from
port_riemann_hilbert_setup_probe.py SPEC v2), fused into a
single heavy build per rung (both compressions read the same
negative-arm Gram matrix E; fusion is bookkeeping, not physics).
IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_schur_cocycle_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
HEAVY = (9, 12, 13, 26, 40)
MIN_RUNGS = 30
MIN_PAIRS_S1 = 20
MIN_PAIRS_S2 = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
IDENT_WARD = 1e-10
ENERGY_LEVEL = 0.90
LOWRANK_R = 2
LOWRANK_FRAC = 0.80
MOEB_STEP_BAR = 0.05
MOEB_PART_BAR = 0.20
REF_SEP_MIN = 1e-6
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# --------- pipeline, verbatim from lax2_flow_probe / port_cocycle_window
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def build_rung(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN GAUGE (lax2 verbatim; the S2 normalization quotients
    it out exactly -- the SO(2) rotation is itself a Moebius map on
    the carrier)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, **kw):
    """One heavy build per rung: the negative-arm Gram E feeds BOTH
    the 12-index window compression (S1) and the dressed-port IIKS
    generators (S2)."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=b["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    # ---- window compression (port_cocycle_window verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["CJ"] = CJ
        out["jav"] = jav
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    # ---- dressed port + IIKS generators (lax2 verbatim)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    """Homogeneous carrier pairs p_j = (g_j, f_j), m = g/f,
    normalized to unit length (chordal arithmetic; f ~ 0 regular)."""
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 between unit pair rows:
    |u w' - w u'| in [0, 1]."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (homogeneous); None if degenerate."""
    M = np.stack([p2, p0], axis=1)
    if abs(float(np.linalg.det(M))) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def apply_hom(T, P):
    Q = (T @ P.T).T
    n = np.linalg.norm(Q, axis=1)
    n[n < 1e-300] = 1.0
    return Q / n[:, None]


def moebius_fit(P, Q):
    """Total-least-squares Moebius fit m' = (a m + b)/(c m + d) on
    unit homogeneous rows: nullspace of [u w', w w', -u u', -w u']."""
    rows = np.stack([P[:, 0] * Q[:, 1], P[:, 1] * Q[:, 1],
                     -P[:, 0] * Q[:, 0], -P[:, 1] * Q[:, 0]],
                    axis=1)
    _u, _s, Vh = np.linalg.svd(rows)
    a, b, c, d = Vh[-1]
    T = np.array([[a, b], [c, d]])
    return T, chordal(apply_hom(T, P), Q)


def cayley_alpha(T):
    """S3(b): alpha = (T(i) - i)/(T(i) + i); |alpha| < 1 iff T
    preserves the upper half plane."""
    den = T[1, 0] * 1j + T[1, 1]
    if abs(den) < 1e-300:
        return float("inf")
    z = (T[0, 0] * 1j + T[0, 1]) / den
    return abs((z - 1j) / (z + 1j))


def logdet_pd(W):
    sgn, ld = np.linalg.slogdet(W)
    return float(sgn), float(ld)


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


def main():
    section("PRIME.PORT.SCHURSTEP.01 -- discrete Moebius/Schur step "
            "on the window ladder (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("W -- build the ladder (all frame-A zones, h <= %d)"
            % H_DEEP_MAX)
    rungs = []
    rk_max = 0.0
    for kz in core.frame_a_zones():
        r = rung_all(kz)
        if not isinstance(r, dict):
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
        if kz in HEAVY and "lamC" in r:
            print("    kz %-3d h %4d full-window %-5s lam(C_J) "
                  "%.6f | port nodes %d"
                  % (kz, r["h"], r["full"], r["lamC"],
                     len(r.get("jp", []))))
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"], rk_max))
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")

    # pair inventories
    s1_pairs, n_skip_full = [], 0
    s2_pairs, n_skip_j = [], 0
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        if ra.get("full") and rb.get("full"):
            s1_pairs.append((ra, rb))
        else:
            n_skip_full += 1
        com, ia, ib = np.intersect1d(ra.get("jp", []),
                                     rb.get("jp", []),
                                     return_indices=True)
        if len(com) >= MIN_COMMON_J:
            s2_pairs.append((ra, rb, com, ia, ib))
        else:
            n_skip_j += 1

    section("S1 -- exact tau quotient as a Schur determinant "
            "(%d full-window pairs; %d typed skips)"
            % (len(s1_pairs), n_skip_full))
    print("    det(W_{h+1})/det(W_h) = det(I + W_h^{-1}"
          "(C_h - C_{h+1}))  [warded %.0e]" % IDENT_WARD)
    pd_ok = True
    id_dev, effs, qs, svtab = [], [], [], []
    for ra, rb in s1_pairs:
        Wa = np.eye(len(JWIN)) - ra["CJ"]
        Wb = np.eye(len(JWIN)) - rb["CJ"]
        sga, lda = logdet_pd(Wa)
        sgb, ldb = logdet_pd(Wb)
        pd_ok &= (sga > 0 and sgb > 0)
        lhs = ldb - lda
        Delta = rb["CJ"] - ra["CJ"]
        sgi, ldi = logdet_pd(np.eye(len(JWIN))
                             - np.linalg.solve(Wa, Delta))
        id_dev.append(abs(ldi - lhs) / max(1.0, abs(lhs)))
        q = sgb / sga * math.exp(lhs)
        qs.append(q)
        U, sv, Vt = np.linalg.svd(Delta)
        en = np.cumsum(sv ** 2) / max(float(np.sum(sv ** 2)),
                                      1e-300)
        eff = int(np.searchsorted(en, ENERGY_LEVEL) + 1)
        effs.append(eff)
        svtab.append(sv)
        r = min(eff, LOWRANK_R)
        K = Vt[:r] @ np.linalg.solve(Wa, U[:, :r] * sv[:r])
        q_r = float(np.linalg.det(np.eye(r) - K))
        al1 = (math.sqrt(1.0 - q) if 0.0 < q < 1.0 else
               float("nan"))
        print("    h %3d->%3d  q %.4f  eff-rank %2d  sv "
              "[%.2e %.2e %.2e ..]  q_r(r=%d) relerr %.2e  "
              "|alpha1| %s"
              % (ra["h"], rb["h"], q, eff, sv[0], sv[1], sv[2],
                 r, abs(q_r - q) / max(abs(q), 1e-300),
                 ("%.3f" % al1) if al1 == al1 else "none"))
    check("W3 >= %d full-window S1 pairs and det(W) > 0 on all "
          "full-window rungs" % MIN_PAIRS_S1,
          len(s1_pairs) >= MIN_PAIRS_S1 and pd_ok,
          "%d pairs, PD %s" % (len(s1_pairs), pd_ok), kill="K1")
    dev_max = float(np.max(id_dev)) if id_dev else float("inf")
    check("S1.1 EXACT QUOTIENT WARD: max rel dev %.2e <= %.0e "
          "(algebra)" % (dev_max, IDENT_WARD),
          dev_max <= IDENT_WARD, kill="KW")
    sv_med = np.median(np.stack(svtab), axis=0)
    print("    median sv profile of Delta_h: "
          + " ".join("%.1e" % v for v in sv_med))
    frac_lr = float(np.mean(np.asarray(effs) <= LOWRANK_R))
    s1_type = ("STEP-LOWRANK" if frac_lr >= LOWRANK_FRAC
               else "STEP-FULLRANK")
    print("    eff-rank census (90%% energy): med %d, frac(<= %d) "
          "%.2f vs bar %.2f -> %s"
          % (int(np.median(effs)), LOWRANK_R, frac_lr,
             LOWRANK_FRAC, s1_type))
    check("S1.2 typed: %s (honest either way; FULLRANK means the "
          "naive matrix alpha_h does not exist)" % s1_type, True)

    section("S2 -- Moebius step on the carrier m = g/f "
            "(%d pairs; %d typed common-j skips)"
            % (len(s2_pairs), n_skip_j))
    print("    normalized gauge: three deepest common nodes "
          "(smallest j) -> (0, 1, inf); TLS Moebius")
    print("    fit per step; residual = median chordal dev on "
          "non-reference nodes.")
    res_steps, alphas, dets = [], [], []
    n_skip_ref = 0
    for ra, rb, com, ia, ib in s2_pairs:
        Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
        Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
        order = np.argsort(com)
        i0, i1, i2 = order[0], order[1], order[2]
        seps = [chordal(Pa[[u]], Pa[[v]])[0]
                for u, v in ((i0, i1), (i0, i2), (i1, i2))] \
            + [chordal(Pb[[u]], Pb[[v]])[0]
               for u, v in ((i0, i1), (i0, i2), (i1, i2))]
        Ta = norm_map(Pa[i0], Pa[i1], Pa[i2])
        Tb = norm_map(Pb[i0], Pb[i1], Pb[i2])
        if min(seps) <= REF_SEP_MIN or Ta is None or Tb is None:
            n_skip_ref += 1
            continue
        Na, Nb = apply_hom(Ta, Pa), apply_hom(Tb, Pb)
        T, res = moebius_fit(Na, Nb)
        keep = np.ones(len(com), dtype=bool)
        keep[[i0, i1, i2]] = False
        med = float(np.median(res[keep]))
        res_steps.append(med)
        dt = float(np.linalg.det(T))
        dets.append(dt)
        alphas.append(cayley_alpha(T))
        print("    h %3d->%3d  n %2d  moebius res %.4f  det(T) "
              "%+.2e  |alpha| %.3f"
              % (ra["h"], rb["h"], len(com), med, dt,
                 alphas[-1]))
    check("W4 >= %d S2 pairs measured (typed skips: %d common-j, "
          "%d degenerate-reference)"
          % (MIN_PAIRS_S2, n_skip_j, n_skip_ref),
          len(res_steps) >= MIN_PAIRS_S2,
          "%d steps" % len(res_steps), kill="K1")
    med_res = float(np.median(res_steps)) if res_steps else 1.0
    s2_type = ("MOEBIUS-STEP" if med_res <= MOEB_STEP_BAR else
               "MOEBIUS-PARTIAL" if med_res <= MOEB_PART_BAR else
               "MOEBIUS-DEAD")
    print("    residual ladder: %s" % quart(res_steps))
    print("    TYPED: median residual %.4f vs bars %.2f / %.2f "
          "-> %s" % (med_res, MOEB_STEP_BAR, MOEB_PART_BAR,
                     s2_type))
    check("S2.1 typed: %s (an honest MOEBIUS-DEAD closes the "
          "review's route 5 cleanly)" % s2_type, True)

    section("S3 -- contractivity census")
    positive = (s1_type == "STEP-LOWRANK"
                or s2_type in ("MOEBIUS-STEP", "MOEBIUS-PARTIAL"))
    qs_a = np.asarray(qs)
    frac_q = float(np.mean((qs_a > 0.0) & (qs_a < 1.0)))
    al_a = np.asarray(alphas)
    frac_al = float(np.mean(al_a < 1.0)) if len(al_a) else 0.0
    frac_dt = (float(np.mean(np.asarray(dets) > 0.0))
               if dets else 0.0)
    print("    (a) exact-quotient census: q_h in (0,1) on %.2f "
          "of %d full-window steps (naive rank-1" %
          (frac_q, len(qs)))
    print("        |alpha_h| = sqrt(1-q_h) exists there with "
          "J_h = 1); q ladder: %s" % quart(qs))
    print("    (b) fitted-map census: |alpha_h| < 1 on %.2f of "
          "%d steps (det(T) > 0 on %.2f)"
          % (frac_al, len(al_a), frac_dt))
    if positive:
        print("    TYPED: census MEANINGFUL (S1/S2 positive): "
              "contractive fraction (a) %.2f, (b) %.2f"
              % (frac_q, frac_al))
    else:
        print("    TYPED: census N/A -- neither S1 nor S2 typed "
              "positive (reported, not scored).")
    check("S3.1 census computed and reported", True)

    section("C -- controls (kz %d, must fire)" % CTRL_KZ)
    ok = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        rc = rung_all(CTRL_KZ, **kw)
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e | lam(E) "
              "%.3e -> fires via %s"
              % (nmc, rc["lamO"], rc["lamC"], rc["lamE"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING"))
    check("C1 CONTROLS FIRE (frame death or supercriticality; "
          "the ladder census cannot run on a single control "
          "rung)", ok, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = "SCHURSTEP-MEASURED / %s / %s" % (s1_type,
                                                    s2_type)
        print("\n  VERDICT: %s" % VERDICT)
        print("  (S1 eff-rank frac(<=%d) %.2f; S2 median moebius "
              "res %.4f; S3 census (a) %.2f (b) %.2f%s)"
              % (LOWRANK_R, frac_lr, med_res, frac_q, frac_al,
                 "" if positive else " [N/A]"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
