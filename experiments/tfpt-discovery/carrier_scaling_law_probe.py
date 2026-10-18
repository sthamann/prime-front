#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""carrier_scaling_law_probe -- PRIME.PORT.CARRIER.SCALING.01
(EXPLORATION ONLY, experiments/; round 48, the direct sequel to
the round-47 CAUCHY-DEAD(PORT) finding: the static identity died,
but the JOINT LIMIT survived -- measure the SCALING LAW of the
carrier-vs-Cauchy deviation in the two variables (depth h, alias
index j).  2026-08-09).

THE QUESTION (frozen): carrier_cauchy_identity_probe found that
the rung-invariant port carrier m_h (round 46) matches the
discrete Cauchy transform C_nu of the negative-arm measure ONLY
in the joint limit deep-h x small-j: deepest-rung per-node
deviation 0.000 (refs) / 0.008 (j=8) / 0.046 (j=22) / 0.103
(j=32) / ~0.41+ beyond; the J*-restricted deviation drops from
~0.3 (shallow) to ~0.026 (deepest).  The surviving theorem seed
is a LIMIT identification, and its usefulness is decided by ONE
comparison: does dev(h, j) -> 0 FASTER or SLOWER than the wall
margin tau_h ~ e^{-2.4 alpha} shrinks?  This probe measures the
deviation field and its two marginal laws, types separability,
and prints the dev-vs-tau ladder -- the decisive strategic
number.

THE LADDER (frozen, predecessor verbatim): all frame-A zones
(core.frame_a_zones()) with h <= 900, sorted by (h, kz) -- the 42
reachable rungs.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; all bars frozen before the run):

 W   PIPELINE WARDS (predecessor verbatim): W1 exactly 42 rungs
     (>= 30); W2 [Y, D_P] rank 2 on every rung (s3/s1 <= 1e-10).

 S1  REPRODUCTION WARD (kill -> WARD-BROKEN): rebuild the
     round-47 machinery verbatim (J* at presence >= 0.90 with
     the 0.90 -> 0.80 -> 0.70 availability rule, reference
     triple = three smallest J* indices, per-rung three-point
     normalization, ONE global gauge map G on the C_nu side
     frozen from the deepest scored rung's three C_nu reference
     values, PORT variant -- the round-47 FROZEN DECISION).  The
     deepest-rung per-node deviation profile must reproduce the
     predecessor's printed values 0.008 (j=8) / 0.046 (j=22) /
     0.103 (j=32) within the 3-decimal print-rounding radius
     5.001e-4 (the predecessor persists its profile only at
     print precision; the machinery is verbatim, so the
     reproduction is bit-level in fact and the ward bar is the
     rounding radius -- documented amendment, predecessor
     precedent).

 X1  THE DEVIATION FIELD: dev(h, j) = chordal distance on RP^1
     between the normalized carrier and the gauge-fixed C_nu
     (PORT variant, global gauge G) at alias j on rung h;
     reference nodes excluded (dev = 0 by construction).  The
     full field is printed compactly as rungs x alias bins
     (bin medians; frozen bins 1-4 / 5-8 / 9-16 / 17-32 / 33-64
     / 65-128 / >= 129).

 X2  THE TWO MARGINAL LAWS:
     (a) at fixed small alias bins (j in {1-4, 5-8, 9-16,
         17-32}), fit dev vs h per bin: power law dev = A h^{-p}
         (log-log LSQ) AND log law dev = a + b ln h; report p_j,
         R^2, and the leave-last-third-out held-out RMSE (train
         on the shallowest 2/3 by h, test on the deepest 1/3,
         RMSE in dev space) for both models; the winner per bin
         is the lower held-out RMSE.  Occupancy rule (frozen): a
         bin participates iff it has >= 6 rung points.
     (b) at fixed depth bins (shallow/mid/deep thirds of the
         scored rungs), fit dev vs the scaled alias variable,
         all three candidates frozen (log-log LSQ slope q and
         R^2 per third; winner = highest mean R^2 across
         thirds):
           V1 j/h                 (the alias fraction)
           V2 2(1 - y_j)          (the edge variable a_j/h^2)
           V3 j (2 pi/(L D))/h    (= tau_j/h; "window width" =
                                   the alias spacing in tau)
     SEPARABILITY (typed, frozen): on the rung x alias-bin field
     of log bin-median deviations (participating bins: occupancy
     >= 50% of scored rungs among the four X2 bins), fit the
     additive two-way model log dev = mu + r_h + c_bin (the
     rank-1 log-log factorization dev ~ F(bin) x h^{-p}).  TYPED
     SCALING-SEPARABLE iff residual SS <= 20% of the field SS
     around its mean; then p = -(slope of the fitted row means
     vs ln h) and the column effects are the log F profile; else
     SCALING-COUPLED, and the best joint fit dev ~ V_win^q x
     h^{-p} (pooled node-level log-log LSQ) is reported with q,
     p, R^2.  The joint fit is printed in both branches (scored
     only in the COUPLED branch; fail-first preserved).

 X3  THE LIMIT OBJECT (the payoff): tau_h = e^{-2.4 alpha_h}
     (the wall margin, per rung).  Print the full comparison
     ladder dev(h, J*-core) vs tau_h (J*-core = J* minus the
     reference triple).  THE HONEST QUESTION (typed, frozen):
     the LSQ slope of ln(dev/tau_h) vs ln h -- per alias bin
     (participating X2 bins) and for the J*-core series.  A
     series is FASTER iff slope <= -0.1, SLOWER iff slope >=
     +0.1, else FLAT.  TYPED WALLGAP-FASTER(bins) iff at least
     one participating bin is FASTER (name the subdomain -- that
     is where a limit-identification theorem would bite);
     WALLGAP-SLOWER iff no bin is FASTER and the J*-core series
     is SLOWER (then the Cauchy identification can never certify
     the wall by itself -- said plainly); else WALLGAP-FLAT.
     EXTRAPOLATION (report): fit alpha vs depth by BOTH frozen
     models alpha = a0 + a1 ln h and alpha = b0 + b1 h; the
     better R^2 is the frozen tau model (documented amendment).
     Under the log model tau ~ h^{-2.4 a1}, so bin b crosses
     dev <= tau iff p_b > 2.4 a1, at ln h* = (c_b + 2.4 a0) /
     (p_b - 2.4 a1); under the linear model tau decays
     exponentially in h and NO power-law bin ever crosses.
     Report the crossing depth (or NEVER) per participating bin,
     plus the empirical count of rungs with dev_core <= tau_h.

 X4  THE INVARIANT-FUNCTION REFINEMENT (report + typed): the
     round-46 m_* was the pointwise chordal median over ALL
     rungs; recompute m_*^deep restricted to the deep half of
     the scored rungs and measure the per-rung deviation from
     THIS m_*^deep on the J*-core nodes.  Print the per-node
     profile (median over all rungs and over the deep half
     separately, per alias index j).  TYPED (frozen): Spearman
     rho between j and the all-rung per-node median deviation;
     INVARIANCE-ALIAS-GRADED iff rho >= 0.5,
     INVARIANCE-ANTI-GRADED iff rho <= -0.5, else
     INVARIANCE-FLAT.

 C   CONTROLS (kz 9; REPORT ONLY, no kill -- the scaling law is
     a truth-side measurement and the frozen verdict enum
     carries no control channel): Epstein (lambda_eps recursion
     comb) + scramble (seed 1); per control report the FRAME
     channel (window unavailable or I - E_out indefinite or
     lam(C_J) > 1, predecessor verbatim) and, where the frame
     survives, the carrier deviation from the truth m_* (frame
     death expected -- report).

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW the S1
reproduction ward breaks -> WARD-BROKEN.

VERDICT (frozen enum): CARRIERSCALING-MEASURED with typed
sublabels SCALING-SEPARABLE / SCALING-COUPLED (X2),
WALLGAP-FASTER(...) / WALLGAP-SLOWER / WALLGAP-FLAT (X3),
INVARIANCE-ALIAS-GRADED / INVARIANCE-ANTI-GRADED /
INVARIANCE-FLAT (X4); else PIPELINE-BROKEN / WARD-BROKEN.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) the reproduction ward anchors on the
predecessor's PRINTED deepest-rung profile values (0.008 /
0.046 / 0.103 at j = 8 / 22 / 32) at the 3-decimal rounding
radius 5.001e-4 plus the rung count 42 -- full-precision values
are not persisted (predecessor precedent); (ii) only the PORT
variant is rebuilt (the round-47 FROZEN DECISION named PORT the
candidate; FULL was the report and is not recomputed); (iii) the
prompt's "j x (window width)/h" is concretized with window
width = the alias spacing in tau, 2 pi/(L D), so V3 = tau_j/h --
the only rung-intrinsic width that makes the product a
per-node coordinate; (iv) rung_all restores the round-46
bookkeeping field taup (per-node tau coordinates; bookkeeping
only, physics verbatim); (v) the alpha-vs-depth model for the
X3 extrapolation is frozen as the better-R^2 of the two named
two-parameter fits, both printed; (vi) sparse-bin occupancy
rules as stated in X2 (>= 6 rung points to fit; >= 50%
occupancy for the separability field); (vii) controls are
report-only by mandate (frame death expected; no CONTROL-DEAD
in the frozen enum); the round-47 self-match readout is not
recomputed.

NO RH claim -- a scaling law of a carrier-vs-Cauchy deviation on
compressed truncations is a numerical measurement, not a theorem
about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; machinery verbatim
from carrier_cauchy_identity_probe.py
(PRIME.PORT.CARRIER.CAUCHY.01, round 47) which carries it
verbatim from moebius_source_step_probe.py
(PRIME.PORT.MOEBIUS.SOURCE.01, round 46), port_schur_cocycle_
probe.py (PRIME.PORT.SCHURSTEP.01) and the SPEC v2 IIKS
extraction of port_riemann_hilbert_setup_probe.py.
IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/carrier_scaling_law_probe.py
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
MIN_RUNGS = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
CTRL_KZ = 9
JSTAR_FRACS = (0.90, 0.80, 0.70)
MIN_JSTAR = 6
SELF_EPS = 1e-12

# S1 reproduction ward anchors (round-47 printed deepest-rung
# per-node PORT profile; 3-decimal print precision).
REF_N_RUNGS = 42
REF_PROFILE = {8: 0.008, 22: 0.046, 32: 0.103}
PROF_TOL = 5.001e-4

# X1/X2 frozen alias bins.
X1_BINS = ((1, 4), (5, 8), (9, 16), (17, 32), (33, 64),
           (65, 128), (129, 10 ** 9))
X2_BINS = X1_BINS[:4]
MIN_FIT_PTS = 6
OCC_FRAC = 0.50
SEP_BAR = 0.20
MIN_POOL_PTS = 20

# X3 frozen bars.
TAU_COEF = 2.4
RATE_SLOPE_BAR = 0.1

# X4 frozen bars.
SPEAR_BAR = 0.5

# controls (report only).
CTRL_INV_FACTOR = 10.0

CLIP = 1e-12
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


# --------- pipeline, verbatim from carrier_cauchy_identity_probe
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
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h,
                uu=uu, mm=mm, M=M)


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
    """FROZEN GAUGE (lax2 verbatim; the normalization quotients it
    out exactly)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, **kw):
    """One heavy build per rung (predecessor verbatim), plus the
    restored round-46 bookkeeping field taup (amendment iv)."""
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
    out = dict(kz=kz, h=h, alpha=b["alpha"], M=b["M"], D=D,
               uu=b["uu"], mm=b["mm"], xs=xs, ws=ws, ys=ys, vs=vs,
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    # ---- window compression (controls' frame channel, verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    # ---- dressed port + IIKS generators (verbatim)
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
        out["vp"] = vs[ip]
        out["taup"] = tau_m[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 between unit pair rows."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (homogeneous); None if degenerate (verbatim)."""
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


def chordal_median(pairs_list):
    """The chordal median on RP^1 of a list of unit pairs
    (verbatim)."""
    P = np.stack(pairs_list)
    D = np.abs(P[:, None, 0] * P[None, :, 1]
               - P[:, None, 1] * P[None, :, 0])
    return P[int(np.argmin(np.sum(D, axis=1)))]


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


# ------------------------------------------- Cauchy-transform source
def cauchy_at(nodes, masses, y):
    """C_nu(y) = sum_k nu_k / (x_k - y), self-atom excluded at
    |x_k - y| <= SELF_EPS (predecessor's exclusion, verbatim)."""
    d = np.asarray(nodes, float) - float(y)
    m = np.abs(d) > SELF_EPS
    return float(np.sum(np.asarray(masses, float)[m] / d[m]))


def cauchy_vec(nodes, masses, yv):
    return np.array([cauchy_at(nodes, masses, y) for y in yv])


# ------------------------------------------- fit helpers (frozen)
def lsq_line(x, y):
    """LSQ line y = m x + c; returns (m, c, R^2)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m, c = np.polyfit(x, y, 1)
    yh = m * x + c
    ss_t = float(np.sum((y - np.mean(y)) ** 2))
    ss_r = float(np.sum((y - yh) ** 2))
    r2 = 1.0 - ss_r / ss_t if ss_t > 0 else 0.0
    return float(m), float(c), r2


def heldout_rmse(hs, ds):
    """Leave-last-third-out (by h order): fit power and log law on
    the shallowest 2/3, RMSE in dev space on the deepest 1/3.
    Returns (rmse_pow, rmse_log)."""
    n = len(hs)
    ntr = n - n // 3
    ht, dt = hs[:ntr], ds[:ntr]
    hv, dv = hs[ntr:], ds[ntr:]
    mp, cp, _ = lsq_line(np.log(ht), np.log(dt))
    ml, cl, _ = lsq_line(np.log(ht), dt)
    pred_p = np.exp(cp) * np.asarray(hv, float) ** mp
    pred_l = ml * np.log(hv) + cl
    rmse_p = float(np.sqrt(np.mean((pred_p - dv) ** 2)))
    rmse_l = float(np.sqrt(np.mean((pred_l - dv) ** 2)))
    return rmse_p, rmse_l


def spearman(x, y):
    rx = np.argsort(np.argsort(np.asarray(x))).astype(float)
    ry = np.argsort(np.argsort(np.asarray(y))).astype(float)
    if float(np.std(rx)) == 0.0 or float(np.std(ry)) == 0.0:
        return 0.0
    return float(np.corrcoef(rx, ry)[0, 1])


def bin_of(j):
    for b, (lo, hi) in enumerate(X1_BINS):
        if lo <= j <= hi:
            return b
    return None


def bin_name(b):
    lo, hi = X1_BINS[b]
    return ("%d-%d" % (lo, hi)) if hi < 10 ** 9 else (">=%d" % lo)


def main():
    section("PRIME.PORT.CARRIER.SCALING.01 -- the scaling law of "
            "the carrier-vs-Cauchy deviation in (h, j) "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; v563 READ-ONLY.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the ladder (all frame-A zones, h <= %d; "
            "machinery verbatim)" % H_DEEP_MAX)
    rungs = []
    rk_max = 0.0
    for kz in core.frame_a_zones():
        r = rung_all(kz)
        if not isinstance(r, dict):
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"], rk_max))
    check("W1 rung count %d == %d (>= %d)"
          % (len(rungs), REF_N_RUNGS, MIN_RUNGS),
          len(rungs) == REF_N_RUNGS and len(rungs) >= MIN_RUNGS,
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")

    # ------------------------------------------------------------ S1
    section("S1 -- rebuild the round-47 gauge construction "
            "(verbatim) + reproduction ward")
    all_jp = [set(int(j) for j in r.get("jp", [])) for r in rungs]
    jstar, used_frac = [], None
    for fr in JSTAR_FRACS:
        cand = sorted(j for j in set().union(*all_jp)
                      if sum(j in s for s in all_jp)
                      >= fr * len(rungs))
        if len(cand) >= MIN_JSTAR:
            jstar, used_frac = cand, fr
            break
    check("S1.0 ladder-wide node set J* built (|J*| %d >= %d at "
          "presence >= %.2f)" % (len(jstar), MIN_JSTAR,
                                 used_frac or 0.0),
          len(jstar) >= MIN_JSTAR, kill="K1")
    if len(jstar) < MIN_JSTAR:
        return finish(None)
    refs = jstar[:3]
    refs_set = set(refs)
    jset = set(jstar[3:])
    print("    J* = %s; reference triple %s -> (0, 1, inf)"
          % (jstar, refs))
    norm_carriers = {}
    n_skip_inv = 0
    for irx, r in enumerate(rungs):
        jp = list(r.get("jp", []))
        if not all(j in jp for j in refs):
            n_skip_inv += 1
            continue
        pos = {int(j): k for k, j in enumerate(jp)}
        P = unit_pairs(r["g"], r["f"])
        Tn = norm_map(P[pos[refs[0]]], P[pos[refs[1]]],
                      P[pos[refs[2]]])
        if Tn is None:
            n_skip_inv += 1
            continue
        norm_carriers[irx] = dict(N=apply_hom(Tn, P), pos=pos)
    print("    %d rungs carry the reference triple (%d typed "
          "skips)" % (len(norm_carriers), n_skip_inv))
    # ---- truth m_* (full ladder, round-46 verbatim; controls + X4)
    mstar = {}
    for j in jstar:
        vals = [nc["N"][nc["pos"][j]]
                for nc in norm_carriers.values() if j in nc["pos"]]
        if len(vals) >= 3:
            mstar[j] = chordal_median(vals)
    devs_mstar = []
    for irx in sorted(norm_carriers):
        nc = norm_carriers[irx]
        dd = [float(chordal(nc["N"][[nc["pos"][j]]],
                            mstar[j][None, :])[0])
              for j in jstar[3:] if j in nc["pos"] and j in mstar]
        if dd:
            devs_mstar.append(float(np.median(dd)))
    med_dev = (float(np.median(devs_mstar)) if devs_mstar
               else float("inf"))
    print("    per-rung deviation from full-ladder m_*: %s"
          % quart(devs_mstar))
    # ---- global gauge map G, PORT variant (round-47 FROZEN
    #      DECISION), frozen at the deepest scored rung
    ref_irx = max((irx for irx in norm_carriers),
                  key=lambda irx: rungs[irx]["h"], default=None)
    rr = rungs[ref_irx]
    pos_ref = norm_carriers[ref_irx]["pos"]
    cv_ref = cauchy_vec(rr["yp"], rr["vp"], rr["yp"])
    Pc = unit_pairs(cv_ref, np.ones(len(cv_ref)))
    Gp = norm_map(Pc[pos_ref[refs[0]]], Pc[pos_ref[refs[1]]],
                  Pc[pos_ref[refs[2]]])
    check("S1.1 global gauge map G (PORT) frozen at the deepest "
          "scored rung (h %d kz %d)" % (rr["h"], rr["kz"]),
          Gp is not None, kill="K1")
    if Gp is None:
        return finish(None)
    # ---- reproduction ward: deepest-rung per-node profile
    nc_ref = norm_carriers[ref_irx]
    Nc_ref = apply_hom(Gp, Pc)
    prof_ref = {int(j): float(chordal(nc_ref["N"][[k]],
                                      Nc_ref[[k]])[0])
                for k, j in enumerate(rr["jp"])}
    ward_ok = True
    for j, anchor in sorted(REF_PROFILE.items()):
        got = prof_ref.get(j)
        okj = got is not None and abs(got - anchor) <= PROF_TOL
        ward_ok &= okj
        print("    profile anchor j=%-3d: got %s vs %.3f "
              "(radius %.1e) -> %s"
              % (j, "%.4f" % got if got is not None else "ABSENT",
                 anchor, PROF_TOL, "ok" if okj else "BREAK"))
    print("    reference-node devs (must be ~0): %s"
          % "  ".join("j=%d %.1e" % (j, prof_ref[j])
                      for j in refs))
    check("S1.2 REPRODUCTION WARD: round-47 deepest-rung profile "
          "reproduced at j=%s (radius %.1e)"
          % (sorted(REF_PROFILE), PROF_TOL), ward_ok, kill="KW")

    # ------------------------------------------------------------ X1
    section("X1 -- THE DEVIATION FIELD dev(h, j) (PORT variant, "
            "global gauge G; refs excluded)")
    field = []
    for irx in sorted(norm_carriers):
        r = rungs[irx]
        nc = norm_carriers[irx]
        cv = cauchy_vec(r["yp"], r["vp"], r["yp"])
        Nc = apply_hom(Gp, unit_pairs(cv, np.ones(len(cv))))
        nodes = []
        for k, j in enumerate(r["jp"]):
            j = int(j)
            if j in refs_set:
                continue
            dev = float(chordal(nc["N"][[k]], Nc[[k]])[0])
            nodes.append((j, float(r["yp"][k]),
                          float(r["taup"][k]), max(dev, CLIP)))
        field.append(dict(h=r["h"], kz=r["kz"],
                          alpha=float(r["alpha"]), nodes=nodes))
    hdr = "    h    kz " + "".join("%9s" % bin_name(b)
                                   for b in range(len(X1_BINS)))
    print(hdr)
    bin_series = {b: [] for b in range(len(X1_BINS))}
    for f in field:
        cells = []
        for b, (lo, hi) in enumerate(X1_BINS):
            dd = [d for (j, _y, _t, d) in f["nodes"]
                  if lo <= j <= hi]
            if dd:
                m = float(np.median(dd))
                bin_series[b].append((f["h"], m))
                cells.append("%9.3f" % m)
            else:
                cells.append("%9s" % "-")
        print("    %4d %3d %s" % (f["h"], f["kz"], "".join(cells)))
    check("X1.1 deviation field built (%d rungs x %d alias bins)"
          % (len(field), len(X1_BINS)), len(field) >= MIN_RUNGS)

    # ------------------------------------------------------------ X2a
    section("X2a -- MARGINAL LAW IN DEPTH: dev vs h per small "
            "alias bin (power vs log law)")
    print("    fit on all points; leave-last-third-out held-out "
          "RMSE (dev space) decides.")
    print("    bin      n    p_j    R2(pow)   log-law b   R2(log)"
          "   HO-rmse pow/log   winner")
    p_exp = {}
    c_int = {}
    for b in range(len(X2_BINS)):
        pts = bin_series[b]
        if len(pts) < MIN_FIT_PTS:
            print("    %-7s %3d   insufficient (< %d rung points)"
                  % (bin_name(b), len(pts), MIN_FIT_PTS))
            continue
        hs = np.array([p[0] for p in pts], float)
        ds = np.array([p[1] for p in pts], float)
        mp, cp, r2p = lsq_line(np.log(hs), np.log(ds))
        ml, _cl, r2l = lsq_line(np.log(hs), ds)
        rp, rl = heldout_rmse(hs, ds)
        win = "power" if rp <= rl else "log"
        p_exp[b] = -mp
        c_int[b] = cp
        print("    %-7s %3d  %+.3f   %.3f     %+.4f     %.3f"
              "    %.4f / %.4f    %s"
              % (bin_name(b), len(pts), -mp, r2p, ml, r2l,
                 rp, rl, win))
    check("X2a.1 marginal depth exponents fitted on %d/%d bins"
          % (len(p_exp), len(X2_BINS)), len(p_exp) >= 2)

    # ------------------------------------------------------------ X2b
    section("X2b -- MARGINAL LAW IN THE ALIAS: dev vs scaled "
            "variable per depth third")
    print("    V1 = j/h;  V2 = 2(1-y_j);  V3 = tau_j/h "
          "(window-width concretization, amendment iii).")
    thirds = np.array_split(np.arange(len(field)), 3)
    tnames = ("shallow", "mid", "deep")
    r2_acc = {v: [] for v in ("V1", "V2", "V3")}
    print("    third    n_pts   V1: q / R2      V2: q / R2      "
          "V3: q / R2")
    for t, idxs in enumerate(thirds):
        pool = []
        for i in idxs:
            f = field[i]
            for (j, y, tau, d) in f["nodes"]:
                pool.append((j / f["h"], 2.0 * (1.0 - y),
                             tau / f["h"], d))
        if len(pool) < MIN_POOL_PTS:
            print("    %-8s %5d   insufficient" % (tnames[t],
                                                   len(pool)))
            continue
        arr = np.array(pool, float)
        txt = []
        for vi, vn in enumerate(("V1", "V2", "V3")):
            v = arr[:, vi]
            d = arr[:, 3]
            m = v > CLIP
            if int(np.sum(m)) < MIN_POOL_PTS:
                txt.append("%s:      -      " % vn)
                continue
            q, _c, r2 = lsq_line(np.log(v[m]), np.log(d[m]))
            r2_acc[vn].append(r2)
            txt.append("%+.3f / %.3f" % (q, r2))
        print("    %-8s %5d   %s" % (tnames[t], len(pool),
                                     "   ".join(txt)))
    v_win = max(r2_acc, key=lambda v: (np.mean(r2_acc[v])
                                       if r2_acc[v] else -1.0))
    print("    WINNER (highest mean R2 across thirds): %s"
          % v_win)
    check("X2b.1 scaled-alias candidate fits done (winner %s)"
          % v_win, any(r2_acc.values()))

    # ---- separability (typed)
    print("\n    SEPARABILITY (rank-1 log-log factorization on "
          "the rung x alias-bin field):")
    part_bins = [b for b in range(len(X2_BINS))
                 if len(bin_series[b]) >= OCC_FRAC * len(field)]
    print("    participating bins (occupancy >= %.0f%%): %s"
          % (100 * OCC_FRAC,
             [bin_name(b) for b in part_bins]))
    rows, cols, yv = [], [], []
    for i, f in enumerate(field):
        for ci, b in enumerate(part_bins):
            lo, hi = X1_BINS[b]
            dd = [d for (j, _y, _t, d) in f["nodes"]
                  if lo <= j <= hi]
            if dd:
                rows.append(i)
                cols.append(ci)
                yv.append(math.log(float(np.median(dd))))
    nR, nC = len(field), len(part_bins)
    A = np.zeros((len(yv), 1 + (nR - 1) + (nC - 1)))
    A[:, 0] = 1.0
    for k, (i, ci) in enumerate(zip(rows, cols)):
        if i > 0:
            A[k, i] = 1.0
        if ci > 0:
            A[k, nR - 1 + ci] = 1.0
    yv = np.array(yv)
    sol, _res, _rk, _sv = np.linalg.lstsq(A, yv, rcond=None)
    yh = A @ sol
    ss_t = float(np.sum((yv - np.mean(yv)) ** 2))
    ss_r = float(np.sum((yv - yh) ** 2))
    sep_frac = ss_r / ss_t if ss_t > 0 else 1.0
    # fitted row means vs ln h -> p; column effects -> log F
    rowmean = {}
    for k, i in enumerate(rows):
        rowmean.setdefault(i, []).append(yh[k])
    hs = np.array([field[i]["h"] for i in sorted(rowmean)], float)
    rm = np.array([np.mean(rowmean[i]) for i in sorted(rowmean)])
    slope_h, _c, r2_h = lsq_line(np.log(hs), rm)
    colmean = {}
    for k, ci in enumerate(cols):
        colmean.setdefault(ci, []).append(yh[k])
    print("    residual SS / field SS = %.3f (bar %.2f); row-mean"
          " slope vs ln h -> p = %.3f (R2 %.3f)"
          % (sep_frac, SEP_BAR, -slope_h, r2_h))
    print("    log F profile (column effects, grand mean "
          "removed): %s"
          % "  ".join("%s %+.2f" % (bin_name(part_bins[ci]),
                                    np.mean(colmean[ci])
                                    - float(np.mean(yv)))
                      for ci in sorted(colmean)))
    # joint fit (printed in both branches; scored only if COUPLED)
    pool = []
    for f in field:
        for (j, y, tau, d) in f["nodes"]:
            v = {"V1": j / f["h"], "V2": 2.0 * (1.0 - y),
                 "V3": tau / f["h"]}[v_win]
            if v > CLIP:
                pool.append((math.log(v), math.log(f["h"]),
                             math.log(d)))
    arr = np.array(pool, float)
    Aj = np.column_stack([np.ones(len(arr)), arr[:, 0],
                          arr[:, 1]])
    solj, _r, _k, _s = np.linalg.lstsq(Aj, arr[:, 2], rcond=None)
    yhj = Aj @ solj
    ss_tj = float(np.sum((arr[:, 2] - np.mean(arr[:, 2])) ** 2))
    r2_j = 1.0 - float(np.sum((arr[:, 2] - yhj) ** 2)) / ss_tj
    q_j, p_j = float(solj[1]), -float(solj[2])
    print("    joint fit dev ~ %s^q h^-p (pooled, %d pts): "
          "q = %+.3f, p = %+.3f, R2 = %.3f"
          % (v_win, len(arr), q_j, p_j, r2_j))
    if sep_frac <= SEP_BAR:
        x2_label = "SCALING-SEPARABLE(p=%.2f)" % (-slope_h)
    else:
        x2_label = ("SCALING-COUPLED(%s: q=%.2f, p=%.2f)"
                    % (v_win, q_j, p_j))
    check("X2.1 typed: %s (residual frac %.3f vs %.2f)"
          % (x2_label, sep_frac, SEP_BAR), True)

    # ------------------------------------------------------------ X3
    section("X3 -- THE LIMIT OBJECT: dev(h, J*-core) vs the wall "
            "margin tau_h = e^{-%.1f alpha}" % TAU_COEF)
    ladder = []
    print("    h    kz   alpha    dev(J*-core)   tau_h        "
          "dev/tau")
    for f in field:
        dd = [d for (j, _y, _t, d) in f["nodes"] if j in jset]
        if not dd:
            continue
        dc = float(np.median(dd))
        tau = math.exp(-TAU_COEF * f["alpha"])
        ladder.append((f["h"], dc, tau))
        print("    %4d %3d   %6.3f   %10.4f   %.3e   %.3e"
              % (f["h"], f["kz"], f["alpha"], dc, tau, dc / tau))
    hs = np.array([x[0] for x in ladder], float)
    dcs = np.array([x[1] for x in ladder], float)
    tas = np.array([x[2] for x in ladder], float)
    slope_core, _c, r2_core = lsq_line(np.log(hs),
                                       np.log(dcs / tas))
    n_cross = int(np.sum(dcs <= tas))
    print("    ln(dev/tau) vs ln h slope (J*-core): %+.3f "
          "(R2 %.3f); rungs with dev <= tau: %d/%d"
          % (slope_core, r2_core, n_cross, len(ladder)))
    # per-bin ratio slopes
    faster_bins = []
    for b in range(len(X2_BINS)):
        pts = bin_series[b]
        if len(pts) < MIN_FIT_PTS:
            continue
        hb = np.array([p[0] for p in pts], float)
        db = np.array([p[1] for p in pts], float)
        # tau at the same rungs (h can repeat; map via field order)
        taub = []
        k = 0
        for f in field:
            lo, hi = X1_BINS[b]
            if any(lo <= j <= hi for (j, _y, _t, _d)
                   in f["nodes"]):
                taub.append(math.exp(-TAU_COEF * f["alpha"]))
        taub = np.array(taub, float)
        sl, _c2, r2b = lsq_line(np.log(hb), np.log(db / taub))
        tag = ("FASTER" if sl <= -RATE_SLOPE_BAR else
               "SLOWER" if sl >= RATE_SLOPE_BAR else "FLAT")
        if tag == "FASTER":
            faster_bins.append(bin_name(b))
        print("    bin %-7s ln(dev/tau) slope %+.3f (R2 %.3f) "
              "-> %s" % (bin_name(b), sl, r2b, tag))
    # alpha-vs-depth models (frozen selection by R2, amendment v)
    alphas = np.array([f["alpha"] for f in field], float)
    hall = np.array([f["h"] for f in field], float)
    a1, a0, r2_log = lsq_line(np.log(hall), alphas)
    b1, b0, r2_lin = lsq_line(hall, alphas)
    tau_model = "log" if r2_log >= r2_lin else "linear"
    print("    alpha models: alpha = %.3f + %.3f ln h (R2 %.3f) "
          "| alpha = %.3f + %.5f h (R2 %.3f) -> frozen: %s"
          % (a0, a1, r2_log, b0, b1, r2_lin, tau_model))
    if tau_model == "log":
        print("    tau ~ h^-%.2f; a bin crosses dev <= tau iff "
              "p_b > %.2f:" % (TAU_COEF * a1, TAU_COEF * a1))
        for b in sorted(p_exp):
            pb, cb = p_exp[b], c_int[b]
            if pb > TAU_COEF * a1:
                lnh = (cb + TAU_COEF * a0) / (pb - TAU_COEF * a1)
                print("      bin %-7s p = %.3f > %.3f -> crossing"
                      " at h* ~ e^%.1f = %.2e"
                      % (bin_name(b), pb, TAU_COEF * a1, lnh,
                         math.exp(min(lnh, 700.0))))
            else:
                print("      bin %-7s p = %.3f <= %.3f -> NEVER"
                      % (bin_name(b), pb, TAU_COEF * a1))
    else:
        print("    tau decays exponentially in h -> NO power-law "
              "bin ever crosses dev <= tau (NEVER on every bin).")
    if faster_bins:
        x3_label = "WALLGAP-FASTER(%s)" % ",".join(faster_bins)
        print("    THE HONEST ANSWER: the identification "
              "sharpens FASTER than the wall margin")
        print("    shrinks on the subdomain(s) %s -- that is "
              "where a limit-identification" % faster_bins)
        print("    theorem would bite.")
    elif slope_core >= RATE_SLOPE_BAR:
        x3_label = "WALLGAP-SLOWER"
        print("    THE HONEST ANSWER, said plainly: the "
              "identification becomes exact SLOWER")
        print("    than the wall margin shrinks -- the Cauchy "
              "identification can NEVER certify")
        print("    the wall by itself; it can at most feed a "
              "different certificate.")
    else:
        x3_label = "WALLGAP-FLAT"
        print("    THE HONEST ANSWER: no bin certifies and the "
              "core series is flat -- the race")
        print("    is undecided at these depths.")
    check("X3.1 typed: %s (core ratio slope %+.3f; bars +/-%.1f)"
          % (x3_label, slope_core, RATE_SLOPE_BAR), True)

    # ------------------------------------------------------------ X4
    section("X4 -- INVARIANT-FUNCTION REFINEMENT: m_* from the "
            "deep half; is the invariance alias-graded?")
    irx_sorted = sorted(norm_carriers)
    deep_irx = set(irx_sorted[len(irx_sorted) // 2:])
    mstar_deep = {}
    for j in jstar:
        vals = [norm_carriers[irx]["N"][norm_carriers[irx]
                                        ["pos"][j]]
                for irx in deep_irx
                if j in norm_carriers[irx]["pos"]]
        if len(vals) >= 3:
            mstar_deep[j] = chordal_median(vals)
    prof_all = {j: [] for j in jstar[3:] if j in mstar_deep}
    prof_deep = {j: [] for j in jstar[3:] if j in mstar_deep}
    rung_med = []
    for irx in irx_sorted:
        nc = norm_carriers[irx]
        dd = []
        for j in prof_all:
            if j in nc["pos"]:
                d = float(chordal(nc["N"][[nc["pos"][j]]],
                                  mstar_deep[j][None, :])[0])
                prof_all[j].append(d)
                if irx in deep_irx:
                    prof_deep[j].append(d)
                dd.append(d)
        if dd:
            rung_med.append((rungs[irx]["h"],
                             float(np.median(dd)),
                             irx in deep_irx))
    print("    per-rung deviation from m_*^deep: shallow half %s"
          % quart([m for _h, m, dp in rung_med if not dp]))
    print("                                      deep half    %s"
          % quart([m for _h, m, dp in rung_med if dp]))
    print("    per-node profile (median dev from m_*^deep):")
    print("      j        all rungs   deep half")
    js, med_all_v = [], []
    for j in sorted(prof_all):
        ma = float(np.median(prof_all[j]))
        md = (float(np.median(prof_deep[j])) if prof_deep[j]
              else float("nan"))
        js.append(j)
        med_all_v.append(ma)
        print("      %-6d   %8.4f    %8.4f" % (j, ma, md))
    rho = spearman(js, med_all_v)
    if rho >= SPEAR_BAR:
        x4_label = "INVARIANCE-ALIAS-GRADED"
    elif rho <= -SPEAR_BAR:
        x4_label = "INVARIANCE-ANTI-GRADED"
    else:
        x4_label = "INVARIANCE-FLAT"
    check("X4.1 typed: %s (Spearman rho(j, med dev) = %+.3f vs "
          "bar +/-%.1f)" % (x4_label, rho, SPEAR_BAR), True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz %d; REPORT ONLY -- frame death "
            "expected, no kill channel)" % CTRL_KZ)
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        rc = rung_all(CTRL_KZ, **kw)
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME death"
                  % (nmc, rc))
            continue
        frame_dead = ("lamC" not in rc or rc["lamO"] > 1.0
                      or rc["lamC"] > 1.0)
        if frame_dead:
            why = ("window unavailable" if "lamC" not in rc else
                   "lam(out) %.3e" % rc["lamO"]
                   if rc["lamO"] > 1.0 else
                   "lam(C_J) %.3e" % rc["lamC"])
            print("    %-8s: FRAME death (%s) -- as expected"
                  % (nmc, why))
            continue
        jp = list(rc.get("jp", []))
        if "jp" in rc and all(j in jp for j in refs):
            pos = {int(j): k for k, j in enumerate(jp)}
            P = unit_pairs(rc["g"], rc["f"])
            Tn = norm_map(P[pos[refs[0]]], P[pos[refs[1]]],
                          P[pos[refs[2]]])
            if Tn is not None:
                N = apply_hom(Tn, P)
                dd = [float(chordal(N[[pos[j]]],
                                    mstar[j][None, :])[0])
                      for j in jstar[3:]
                      if j in pos and j in mstar]
                if dd:
                    dev_c = float(np.median(dd))
                    print("    %-8s: frame ALIVE; carrier dev vs"
                          " truth m_* %.4f (truth med %.4f, "
                          "x%.0f bar %.4f)"
                          % (nmc, dev_c, med_dev,
                             CTRL_INV_FACTOR,
                             CTRL_INV_FACTOR * med_dev))
                    continue
        print("    %-8s: frame alive but carrier/reference "
              "unavailable -> FRAME-equivalent" % nmc)
    check("C1 controls run and reported (report only by mandate; "
          "no kill channel)", True)

    return finish(dict(x2=x2_label, x3=x3_label, x4=x4_label,
                       sep_frac=sep_frac, slope_core=slope_core,
                       p_exp=p_exp, rho=rho, q_j=q_j, p_j=p_j))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("CARRIERSCALING-MEASURED / %s / %s / %s"
                   % (labels["x2"], labels["x3"], labels["x4"]))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (separability residual frac %.3f; marginal "
              "exponents %s; joint q %+.2f p %+.2f; core "
              "ln(dev/tau) slope %+.3f; X4 rho %+.3f)"
              % (labels["sep_frac"],
                 " ".join("%s %.2f" % (bin_name(b), p)
                          for b, p in sorted(
                              labels["p_exp"].items())),
                 labels["q_j"], labels["p_j"],
                 labels["slope_core"], labels["rho"]))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
