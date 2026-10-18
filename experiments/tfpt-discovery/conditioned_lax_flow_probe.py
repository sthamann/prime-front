#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""conditioned_lax_flow_probe -- PRIME.PORT.LAX2.02
(EXPLORATION ONLY, experiments/; round 41: expose the LAWFUL
degree-2 Lax flow of the ladder that the raw coefficient basis
masks, 2026-08-09).

THE QUESTION (frozen): PRIME.PORT.LAX2.01 measured FLOW-NOISY /
LAX2-PARTIAL -- the 12 raw deformation-polynomial coefficients,
normalized by the alpha step, have median roughness ratio 1.365
(noise) and operator predictivity misses at 0.350 vs bar 0.3.
The NAMED interpretive lead: the dictionary columns f, Yf, Y^2 f
are nearly collinear because the port y-values cluster near 1 --
the raw basis is ill-conditioned, so the raw coefficients are
noise-amplified even if the FLOW itself is lawful.  This probe
reparametrizes the SAME fit in a well-conditioned basis (thin QR
of the dictionary) and retests lawfulness in three candidate
flow clocks.

THE LADDER (frozen, verbatim from PRIME.PORT.LAX2.01): all
frame-A zones (core.frame_a_zones()) with h <= 900, sorted by
(h, kz); port nodes carry the stable alias index j = uf value of
the folded node; consecutive rungs matched on the COMMON
j-subset (>= 8, typed skips counted); gauge-fixed IIKS
generators (f, g) of [Y, D_P] with the FROZEN gauge (m0 =
smallest alias index j; SO(2)-rotate so f[m0] > 0, g[m0] = 0).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 X1  CONDITIONED COEFFICIENTS: per step, build the 6-column
     dictionary M = [f, Yf, Y^2 f, g, Yg, Y^2 g] on the common-j
     subset (rung-k data), orthonormalize by thin QR (M = QR,
     diag(R) > 0 sign convention so the Q columns are comparable
     across steps), and expand Delta f and Delta g in Q:
       qf = Q^T Delta f,  qg = Q^T Delta g
     (6 + 6 = 12 conditioned coefficients per step, well-
     conditioned by construction).  Report the per-step condition
     number of R (== cond of the raw dictionary -- the
     collinearity measure that explains the v1 noise).
     WARD (K3 SPAN-BROKEN): the conditioned residual fractions
     ||Delta f - Q qf||/||Delta f|| (and g) must equal the RAW-
     basis lstsq residuals to 1e-10 -- same span, same fit.

 X2  LAWFULNESS IN THREE CLOCKS (typed): normalize the 12
     conditioned coefficient series by the step in three
     candidate flow clocks, order the steps by the deeper rung's
     clock value, and measure per series
       ratio_i = RMS(consecutive differences) / RMS(values).
     Clocks (per-rung values, steps = deeper minus shallower):
       (i)   alpha    = U_ALL[kz] (the v1 clock);
       (ii)  logtau   = log|det(I - D_P)| computed on the FULL
                        port matrix of the rung (stated choice:
                        simpler than the 12-index Schur
                        compression of PRIME.PORT.COCYCLE.01 and
                        well-defined per rung; the common-window
                        restriction enters only through the
                        matched coefficients themselves);
       (iii) lammax   = lam_max(D_P) (testing criticality,
                        1 - tau proxy).
     Steps with |Delta clock| <= 1e-9 are typed skips per clock
     (counted).  TYPED per clock: LAWFUL iff the median ratio
     over the 12 conditioned series is <= 0.7.  Deliverable: the
     3-clock table; verdict sublabel = the best clock and its
     ratio -- CLOCK-FOUND iff any clock <= 0.7, else CLOCK-OPEN
     (both honest).

 X3  SMOOTHED-FLOW PREDICTIVITY: with the best clock (smallest
     median ratio), fit each of the 12 conditioned velocity
     series by a degree-2 polynomial in the clock (least squares
     over all non-skipped steps), REBUILD the per-step
     generators from the smoothed coefficients
       F = f + Q (v_fit(t_k) * Delta t_k)  (and G likewise),
     and run the operator-level IIKS prediction of
     PRIME.PORT.LAX2.01 X3 (off-diagonal only; diagonal kept
     ACTUAL -- the commutator does not determine it, typed
     honestly).  Report the median offdiag rel err vs the frozen
     raw-fit reference 0.350 (v1 measured; re-derived here for
     honesty).  TYPED: FLOW-PREDICTIVE iff median <= 0.3,
     FLOW-IMPROVED iff median < 0.350, else FLOW-FLAT.

 X4  GAUGE ROBUSTNESS WARD: repeat X2 for the best clock with
     the alternative gauge anchor -- the SAME SO(2) fix but
     re-anchored on g instead of f (rotate so g[m0] > 0,
     f[m0] = 0 at the smallest-j node).  WARD (K1): the
     lawfulness typing (LAWFUL vs not, at the frozen 0.7 bar)
     for the best clock must not depend on the gauge anchor.

 W   PIPELINE WARDS (verbatim v1): W1 >= 30 rungs built; W2
     every rung [Y, D_P] rank 2 (s3/s1 <= 1e-10); W3 >= 30
     consecutive pairs with >= 8 common j and |Delta alpha| >
     1e-9 (typed skips counted); W4 gauge stability (median
     consecutive |cos(f_k, f_k+1)| >= 0.7).

 C   CONTROLS (kz 9, must fire): Epstein (lambda_eps recursion
     comb rebuilt at kz 9) + scramble (seed 1): lam(E) > 1
     (value fires, printed); [Y, D_P] rank 2 persists (pipeline
     is class membership, not zeta-tuned).

KILLS: K1 pipeline/gauge ward breaks -> PIPELINE-BROKEN;
K2 controls silent -> CONTROL-DEAD; K3 conditioned residuals
differ from raw residuals -> SPAN-BROKEN.

VERDICT (frozen enum): LAX2-CONDITIONED-MEASURED with typed
sublabels CLOCK-FOUND(<clock>, <ratio>) / CLOCK-OPEN (X2) and
FLOW-PREDICTIVE / FLOW-IMPROVED / FLOW-FLAT (X3), else
PIPELINE-BROKEN / SPAN-BROKEN / CONTROL-DEAD.

NO RH claim -- conditioned lawfulness and smoothed predictivity
are numerical measurements on the window ladder, not a theorem
about zeros.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; pipeline copied
verbatim from lax2_flow_probe.py (PRIME.PORT.LAX2.01; itself
verbatim from isomonodromy_flow_probe.py /
port_riemann_hilbert_setup_probe.py), with two passthrough
additions: gen_rung also stores the per-rung clock values
log|det(I - D_P)| and lam_max(D_P), and both gauge anchors
(f-anchored, the frozen v1 gauge, plus the g-anchored X4
variant).  IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/conditioned_lax_flow_probe.py
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
MIN_COMMON_J = 8
MIN_RUNGS = 30
MIN_PAIRS = 30
LAWFUL_BAR = 0.7
PRED_BAR = 0.3
RAW_PRED_REF = 0.350          # frozen v1 X3 median (LAX2-PARTIAL)
RANK_BAR = 1e-10
GAUGE_COS_BAR = 0.7
SPAN_WARD = 1e-10
DCLK_MIN = 1e-9
CTRL_KZ = 9
CLOCK_NAMES = ("alpha", "logtau", "lammax")
QCOEF_NAMES = tuple("q%d%s" % (i % 6, "f" if i < 6 else "g")
                    for i in range(12))
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


# ------------------- pipeline, verbatim from lax2_flow_probe.py
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


def dressed_port(kz, **kw):
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
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    P = G[np.ix_(ip, ip)]
    X = G[np.ix_(ip, ib)]
    R = G[np.ix_(ib, ib)]
    IR = np.eye(len(ib)) - R
    DP = P + X @ np.linalg.solve(IR, X.T)
    DP = 0.5 * (DP + DP.T)
    return dict(DP=DP, yp=ys[ip], jp=uf_n[ip], h=h,
                alpha=b["alpha"],
                lamE=float(np.linalg.eigvalsh(G)[-1]))


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T from the rank-2
    SVD of the antisymmetric C (v2 extraction, verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN GAUGE (v1): SO(2)-rotate so that f is maximal and
    positive at the smallest-j node m0 (then g[m0] = 0)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def gauge_fix_g(f, g, jp):
    """X4 ALTERNATIVE ANCHOR: same SO(2) fix re-anchored on g --
    rotate so g[m0] > 0 and f[m0] = 0 at the smallest-j node."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = g[m0] / r, -f[m0] / r
    return c * f + s * g, -s * f + c * g


def logdet_abs(M):
    _sgn, ld = np.linalg.slogdet(M)
    return float(ld)


def gen_rung(kz, **kw):
    r = dressed_port(kz, **kw)
    if not isinstance(r, dict):
        return r
    Y = np.diag(r["yp"])
    C = Y @ r["DP"] - r["DP"] @ Y
    f, g, sv = antisym_generators(C)
    r["f"], r["g"] = gauge_fix(f, g, r["jp"])
    r["f2"], r["g2"] = gauge_fix_g(f, g, r["jp"])
    r["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    r["kz"] = kz
    # per-rung clock values (passthrough addition, docstring):
    n = r["DP"].shape[0]
    r["ldet"] = logdet_abs(np.eye(n) - r["DP"])
    r["lam"] = float(np.linalg.eigvalsh(r["DP"])[-1])
    return r


def pair_data(ra, rb, fk="f", gk="g"):
    com, ia, ib = np.intersect1d(ra["jp"], rb["jp"],
                                 return_indices=True)
    if len(com) < MIN_COMMON_J:
        return None
    return dict(n=len(com),
                fa=ra[fk][ia], ga=ra[gk][ia], ya=ra["yp"][ia],
                fb=rb[fk][ib], gb=rb[gk][ib], yb=rb["yp"][ib],
                Da=ra["DP"][np.ix_(ia, ia)],
                Db=rb["DP"][np.ix_(ib, ib)])


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.3f  med %.3f  q75 %.3f" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


# ------------------------------------------ probe-specific machinery
def raw_fit(pd):
    """v1 X1 fit, verbatim (for the K3 span ward and the raw
    predictivity re-derivation)."""
    ya = pd["ya"]
    A = np.stack([pd["fa"], ya * pd["fa"], ya ** 2 * pd["fa"],
                  pd["ga"], ya * pd["ga"], ya ** 2 * pd["ga"]],
                 axis=1)
    df = pd["fb"] - pd["fa"]
    dg = pd["gb"] - pd["ga"]
    cf, *_ = np.linalg.lstsq(A, df, rcond=None)
    cg, *_ = np.linalg.lstsq(A, dg, rcond=None)
    res_f = float(np.linalg.norm(df - A @ cf)
                  / np.linalg.norm(df))
    res_g = float(np.linalg.norm(dg - A @ cg)
                  / np.linalg.norm(dg))
    return A, cf, cg, res_f, res_g


def cond_fit(pd):
    """X1: thin QR of the dictionary (diag(R) > 0 convention) and
    the conditioned expansion of (Delta f, Delta g) in Q."""
    A, _cf, _cg, rres_f, rres_g = raw_fit(pd)
    Q, R = np.linalg.qr(A)
    sgn = np.sign(np.diag(R))
    sgn[sgn == 0.0] = 1.0
    Q = Q * sgn[None, :]
    R = sgn[:, None] * R
    condR = float(np.linalg.cond(R))
    df = pd["fb"] - pd["fa"]
    dg = pd["gb"] - pd["ga"]
    qf = Q.T @ df
    qg = Q.T @ dg
    res_f = float(np.linalg.norm(df - Q @ qf)
                  / np.linalg.norm(df))
    res_g = float(np.linalg.norm(dg - Q @ qg)
                  / np.linalg.norm(dg))
    dev = max(abs(res_f - rres_f), abs(res_g - rres_g))
    return dict(Q=Q, qf=qf, qg=qg, condR=condR,
                res_f=res_f, res_g=res_g, span_dev=dev)


def iiks_predict(F, G, yb, Db):
    """v1 X3, verbatim: IIKS kernel formula off the diagonal;
    the diagonal is NOT determined by the commutator and is
    copied from the actual matrix (typed in the docstring)."""
    n = len(yb)
    num = np.outer(F, G) - np.outer(G, F)
    den = yb[:, None] - yb[None, :]
    off = ~np.eye(n, dtype=bool)
    Dp = np.array(Db)          # diagonal kept actual
    Dp[off] = num[off] / den[off]
    err = (np.linalg.norm((Db - Dp)[off])
           / np.linalg.norm(Db[off]))
    return Dp, float(err)


def clock_lawfulness(pairs, clock, fits):
    """X2 core: normalized conditioned-velocity series in the
    given clock; returns (median ratio, ratios, kept indices,
    t positions, dt steps, n skipped)."""
    keep, tpos, dts = [], [], []
    for i, pd in enumerate(pairs):
        dt = pd["clk_b"][clock] - pd["clk_a"][clock]
        if abs(dt) <= DCLK_MIN:
            continue
        keep.append(i)
        tpos.append(pd["clk_b"][clock])
        dts.append(dt)
    n_skip = len(pairs) - len(keep)
    order = np.argsort(tpos)
    keep = [keep[k] for k in order]
    tpos = np.array([tpos[k] for k in order])
    dts = np.array([dts[k] for k in order])
    V = np.array([np.concatenate([fits[i]["qf"], fits[i]["qg"]])
                  / dt for i, dt in zip(keep, dts)])
    ratios = []
    for i in range(12):
        v = V[:, i]
        rms = math.sqrt(float(np.mean(v ** 2)))
        rmsd = math.sqrt(float(np.mean(np.diff(v) ** 2)))
        ratios.append(rmsd / max(rms, 1e-300))
    return (float(np.median(ratios)), ratios, keep, tpos, dts,
            n_skip, V)


def main():
    section("PRIME.PORT.LAX2.02 -- does a conditioned basis "
            "expose a lawful Lax flow? (EXPLORATION ONLY)")
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
        r = gen_rung(kz)
        if not isinstance(r, dict):
            continue
        rk_max = max(rk_max, r["rk"])
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"], rk_max))
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= "
          "%.0e)" % (rk_max, RANK_BAR), rk_max <= RANK_BAR,
          kill="K1")

    pairs = []
    pairs_alt = []
    n_skip_j = 0
    n_skip_dal = 0
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        pd = pair_data(ra, rb)
        if pd is None:
            n_skip_j += 1
            continue
        dal = rb["alpha"] - ra["alpha"]
        if abs(dal) <= DCLK_MIN:
            n_skip_dal += 1
            continue
        pd["ha"], pd["hb"] = ra["h"], rb["h"]
        pd["clk_a"] = dict(alpha=ra["alpha"], logtau=ra["ldet"],
                           lammax=ra["lam"])
        pd["clk_b"] = dict(alpha=rb["alpha"], logtau=rb["ldet"],
                           lammax=rb["lam"])
        pairs.append(pd)
        pa = pair_data(ra, rb, fk="f2", gk="g2")
        pa["clk_a"], pa["clk_b"] = pd["clk_a"], pd["clk_b"]
        pairs_alt.append(pa)
    check("W3 >= %d consecutive pairs with >= %d common j and "
          "|dal| > %.0e (typed skips: %d common-j, %d dal)"
          % (MIN_PAIRS, MIN_COMMON_J, DCLK_MIN, n_skip_j,
             n_skip_dal),
          len(pairs) >= MIN_PAIRS, "%d pairs" % len(pairs),
          kill="K1")

    cosc = [abs(float(pd["fa"] @ pd["fb"]
                      / (np.linalg.norm(pd["fa"])
                         * np.linalg.norm(pd["fb"]))))
            for pd in pairs]
    med_cos = float(np.median(cosc))
    check("W4 GAUGE STABLE: median consecutive |cos(f,f')| "
          "%.3f >= %.1f" % (med_cos, GAUGE_COS_BAR),
          med_cos >= GAUGE_COS_BAR, kill="K1")

    section("X1 -- conditioned coefficients (thin QR of the "
            "dictionary) + span ward")
    fits = []
    conds = []
    span_devs = []
    for pd in pairs:
        ft = cond_fit(pd)
        fits.append(ft)
        conds.append(ft["condR"])
        span_devs.append(ft["span_dev"])
        print("    h %3d->%3d  n=%2d  cond(R) %9.2e  res f %.3f "
              "g %.3f" % (pd["ha"], pd["hb"], pd["n"],
                          ft["condR"], ft["res_f"], ft["res_g"]))
    med_cond = float(np.median(conds))
    print("    cond(R) of the raw dictionary (the collinearity "
          "that noise-amplified v1):")
    print("      median %.2e   max %.2e"
          % (med_cond, float(np.max(conds))))
    check("X1.1 conditioned coefficients extracted on all %d "
          "steps" % len(pairs), len(fits) == len(pairs))
    dev_max = float(np.max(span_devs))
    check("X1.2 SPAN WARD: conditioned residuals == raw lstsq "
          "residuals, max dev %.2e <= %.0e"
          % (dev_max, SPAN_WARD), dev_max <= SPAN_WARD,
          kill="K3")

    section("X2 -- lawfulness in three clocks (frozen bar: "
            "median roughness ratio <= %.1f)" % LAWFUL_BAR)
    print("    ratio_i = RMS(consecutive diff)/RMS(values) of "
          "the 12 conditioned velocity")
    print("    series, steps ordered by the deeper rung's clock "
          "value (lawful << 1, noise ~1.41):")
    clock_res = {}
    print("    %-8s %8s %8s %8s %6s   per-coefficient ratios"
          % ("clock", "med", "min", "max", "skips"))
    for clock in CLOCK_NAMES:
        med, ratios, keep, tpos, dts, n_skip, V = \
            clock_lawfulness(pairs, clock, fits)
        clock_res[clock] = dict(med=med, ratios=ratios,
                                keep=keep, tpos=tpos, dts=dts,
                                n_skip=n_skip, V=V)
        print("    %-8s %8.3f %8.3f %8.3f %6d   [%s]"
              % (clock, med, min(ratios), max(ratios), n_skip,
                 " ".join("%.2f" % r for r in ratios)))
    best = min(CLOCK_NAMES, key=lambda c: clock_res[c]["med"])
    best_med = clock_res[best]["med"]
    clock_found = best_med <= LAWFUL_BAR
    print("    TYPED per clock (LAWFUL iff median <= %.1f): %s"
          % (LAWFUL_BAR,
             ", ".join("%s %s" % (c, "LAWFUL"
                                  if clock_res[c]["med"]
                                  <= LAWFUL_BAR else "NOISY")
                       for c in CLOCK_NAMES)))
    print("    BEST CLOCK: %s (median ratio %.3f) -> %s"
          % (best, best_med,
             "CLOCK-FOUND" if clock_found else "CLOCK-OPEN"))
    check("X2.1 lawfulness measured in all 3 clocks (typed "
          "outcome, not a kill)", len(clock_res) == 3)

    section("X3 -- smoothed-flow predictivity in the best clock "
            "(%s; frozen bar %.1f, v1 raw ref %.3f)"
            % (best, PRED_BAR, RAW_PRED_REF))
    cr = clock_res[best]
    keep, tpos, dts, V = cr["keep"], cr["tpos"], cr["dts"], \
        cr["V"]
    t0 = float(np.mean(tpos))
    ts = max(float(np.std(tpos)), 1e-300)
    tn = (tpos - t0) / ts        # centered/scaled for the polyfit
    Vs = np.empty_like(V)
    for i in range(12):
        co = np.polyfit(tn, V[:, i], 2)
        Vs[:, i] = np.polyval(co, tn)
    errs_s = []
    errs_r = []
    for row, i in enumerate(keep):
        pd = pairs[i]
        q_s = Vs[row] * dts[row]
        F = pd["fa"] + fits[i]["Q"] @ q_s[:6]
        G = pd["ga"] + fits[i]["Q"] @ q_s[6:]
        _Dp, err = iiks_predict(F, G, pd["yb"], pd["Db"])
        errs_s.append(err)
        Fr = pd["fa"] + fits[i]["Q"] @ fits[i]["qf"]
        Gr = pd["ga"] + fits[i]["Q"] @ fits[i]["qg"]
        _Dp, err_r = iiks_predict(Fr, Gr, pd["yb"], pd["Db"])
        errs_r.append(err_r)
    med_raw = float(np.median(errs_r))
    med_s = float(np.median(errs_s))
    print("    per-step raw-fit err (re-derived v1 reference): "
          "%s" % quart(errs_r))
    print("    per-step smoothed-flow err (deg-2 law in %s): %s"
          % (best, quart(errs_s)))
    if med_s <= PRED_BAR:
        x3_type = "FLOW-PREDICTIVE"
    elif med_s < RAW_PRED_REF:
        x3_type = "FLOW-IMPROVED"
    else:
        x3_type = "FLOW-FLAT"
    print("    TYPED: smoothed median %.3f vs bar %.1f / raw ref "
          "%.3f (re-derived %.3f) -> %s"
          % (med_s, PRED_BAR, RAW_PRED_REF, med_raw, x3_type))
    check("X3.1 smoothed predictivity measured on all %d kept "
          "steps (typed outcome, not a kill)" % len(keep),
          len(errs_s) == len(keep))

    section("X4 -- gauge robustness ward (g-anchored gauge, "
            "best clock %s)" % best)
    fits_alt = [cond_fit(pd) for pd in pairs_alt]
    med_alt, _r, _k, _t, _d, n_skip_alt, _V = \
        clock_lawfulness(pairs_alt, best, fits_alt)
    lawful_main = best_med <= LAWFUL_BAR
    lawful_alt = med_alt <= LAWFUL_BAR
    print("    f-anchored median %.3f (%s) | g-anchored median "
          "%.3f (%s), %d skips"
          % (best_med, "LAWFUL" if lawful_main else "NOISY",
             med_alt, "LAWFUL" if lawful_alt else "NOISY",
             n_skip_alt))
    check("X4.1 GAUGE WARD: lawfulness typing in clock %s is "
          "anchor-independent" % best,
          lawful_main == lawful_alt, kill="K1")

    section("C -- controls (kz %d, must fire)" % CTRL_KZ)
    ok = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        rc = gen_rung(CTRL_KZ, **kw)
        fired = isinstance(rc, dict) and rc["lamE"] > 1.0
        persists = isinstance(rc, dict) and rc["rk"] <= 1e-8
        ok &= fired and persists
        if isinstance(rc, dict):
            print("    %-8s: lam(E) %.3e (fires: %s) | [Y,D_P] "
                  "s3/s1 %.1e (pipeline persists: %s)"
                  % (nmc, rc["lamE"], fired, rc["rk"],
                     persists))
        else:
            print("    %-8s: rung not built (%r)" % (nmc, rc))
    check("C1 CONTROLS FIRE (value) and the IIKS pipeline "
          "persists", ok, kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "CONTROL-DEAD",
                   "K3": "SPAN-BROKEN"}[KILLS[0]]
    else:
        VERDICT = ("LAX2-CONDITIONED-MEASURED / %s / %s"
                   % (("CLOCK-FOUND(%s, %.3f)" % (best, best_med))
                      if clock_found else
                      ("CLOCK-OPEN(best %s, %.3f)"
                       % (best, best_med)), x3_type))
    print("\n  VERDICT: %s" % VERDICT)
    if not KILLS:
        print("  (X1 median cond(R) %.2e; X2 clocks %s; X3 "
              "smoothed %.3f vs raw ref %.3f)"
              % (med_cond,
                 ", ".join("%s %.3f" % (c, clock_res[c]["med"])
                           for c in CLOCK_NAMES),
                 med_s, RAW_PRED_REF))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
