#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lax2_flow_probe -- PRIME.PORT.LAX2.01
(EXPLORATION ONLY, experiments/; round 40, work package (b): make
the measured degree-2 Lax closure of the ladder flow CONCRETE --
extract the deformation-polynomial coefficients, test whether they
form a LAWFUL flow in the ladder parameter, and test the OPERATOR-
level predictivity of the degree-2 ansatz, 2026-08-09).

THE QUESTION (frozen): PRIME.PORT.ISOFLOW.01 measured that the
ladder increments of the gauge-fixed IIKS generators (f, g) of the
dressed port D_P close in the degree-2 dictionary {f, g, Yf, Yg,
Y^2 f, Y^2 g} with median residuals ~0.24.  Closure alone is a
subspace statement; a LAX reading needs more: the expansion
COEFFICIENTS must be a lawful (smooth, not noisy) function of the
ladder parameter, and the fitted degree-2 flow must be predictive
at the OPERATOR level -- rung k data plus the fitted increment must
reproduce rung (k+1)'s port matrix through the IIKS kernel formula.

THE LADDER (frozen): all frame-A zones (core.frame_a_zones()) with
h <= 900, sorted by (h, kz).  Port nodes carry the stable alias
index j = uf value of the folded node; consecutive rungs are
matched on the COMMON j-subset; a pair with < 8 common indices is
a typed skip (counted, warded).  Ladder parameter: alpha of the
rung (alpha = U_ALL[kz], strictly window-specific); each step is
normalized by Delta alpha = alpha(k+1) - alpha(k) and placed at
the DEEPER rung's alpha.

FROZEN GAUGE (verbatim from PRIME.PORT.ISOFLOW.01): m0 = node with
the smallest alias index j; SO(2)-rotate so f[m0] > 0, g[m0] = 0.
Gauge health is WARDED (W4), not assumed.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 X1  COEFFICIENT EXTRACTION: on each consecutive pair (k, k+1)
     with >= 8 common j, least-squares expand on the common
     section (Y = diag of rung-k y-values there)
       Delta f = (a0 + a1 Y + a2 Y^2) f + (b0 + b1 Y + b2 Y^2) g,
       Delta g = (c0 + c1 Y + c2 Y^2) f + (d0 + d1 Y + d2 Y^2) g
     (12 coefficients per step).  Print the coefficient table
     along the ladder (steps ordered by h), with the fit
     residual fractions (the ISOFLOW closure numbers, re-derived).

 X2  FLOW LAWFULNESS (typed): normalize each coefficient by the
     step size, v_i = c_i / Delta alpha (the flow velocity
     field), order the steps by the deeper rung's alpha, and for
     each of the 12 normalized coefficient series measure
       ratio_i = RMS(consecutive differences) / RMS(values).
     A lawful flow has ratio << 1; independent noise gives
     ~sqrt(2).  TYPED: FLOW-LAWFUL iff the median ratio over the
     12 coefficients is <= 0.7, else FLOW-NOISY (both honest).
     Steps with |Delta alpha| <= 1e-9 would be typed skips
     (counted; none expected since alpha is strictly increasing
     in kz).

 X3  OPERATOR-LEVEL PREDICTIVITY (the decisive test): from rung k
     predict rung (k+1)'s port matrix on the common j-subset via
     the IIKS kernel formula
       D_pred[m,m'] = (F_m G_m' - G_m F_m') / (y'_m - y'_m'),
     m != m', where (F, G) = (f + Delta f_fit, g + Delta g_fit)
     from the X1 fit and y' = the (k+1)-rung node coordinates at
     the matched j.  DIAGONAL: kept from the actual (k+1) matrix
     -- the IIKS commutator formula does NOT determine it (typed
     honestly; the test is off-diagonal only).  Measure per step
       err = ||D_actual - D_pred||_F(offdiag)
             / ||D_actual||_F(offdiag).
     TYPED: LAX2-PREDICTIVE iff the median err <= 0.3, else
     LAX2-PARTIAL (both honest).

 X4  INTEGRATED TAU TRANSFER (report + identity ward): per step,
     on the common-j sections,
       Delta log|tau| = log|det(I - D_{k+1})| - log|det(I - D_k)|
     vs the exact integrated transfer
       log|det(I - (I - D_k)^{-1} (D_{k+1} - D_k))|
     -- an algebraic identity, warded at 1e-10 (consistency check
     of the section bookkeeping); and vs the Lax-predicted
     version with D_pred from X3 in place of D_{k+1} (accuracy
     |pred - actual| / |actual| reported -- the tau-transfer
     content of the degree-2 flow).
     SPEC v2 (mechanical repair, before the first run): the work
     order wrote the identity with a plus sign,
     log|det(I + (I-D_k)^{-1}(D_{k+1}-D_k))|; the actual identity
     is det(I-D_{k+1}) = det(I-D_k) det(I - (I-D_k)^{-1}
     (D_{k+1}-D_k)) -- the sign is corrected here so the 1e-10
     ward tests the intended bookkeeping identity.

 W   PIPELINE WARDS: W1 >= 30 rungs built; W2 every rung
     [Y, D_P] rank 2 (s3/s1 <= 1e-10); W3 >= 30 consecutive
     pairs with >= 8 common j and |Delta alpha| > 1e-9 (typed
     skips counted); W4 gauge stability (median consecutive
     |cos(f_k, f_k+1)| >= 0.7).

 C   CONTROLS (kz 9, must fire): Epstein (lambda_eps recursion
     comb rebuilt at kz 9) + scramble (seed 1): lam(E) > 1
     (value fires, printed); [Y, D_P] rank 2 persists (pipeline
     is class membership, not zeta-tuned).

KILLS: K1 pipeline/gauge/identity ward breaks -> PIPELINE-BROKEN;
K2 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): LAX2-MEASURED with typed sublabels
FLOW-LAWFUL / FLOW-NOISY (X2) and LAX2-PREDICTIVE / LAX2-PARTIAL
(X3), else PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim -- coefficient lawfulness and operator predictivity
are numerical measurements on the window ladder, not a theorem
about zeros.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; pipeline copied
verbatim from isomonodromy_flow_probe.py (PRIME.PORT.ISOFLOW.01;
itself verbatim from port_riemann_hilbert_setup_probe.py), with
one passthrough addition: dressed_port also returns the window's
alpha (needed for the X2 normalization).  IIKS = Its-Izergin-
Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/lax2_flow_probe.py
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
RANK_BAR = 1e-10
GAUGE_COS_BAR = 0.7
IDENT_WARD = 1e-10
DAL_MIN = 1e-9
CTRL_KZ = 9
COEF_NAMES = ("a0", "a1", "a2", "b0", "b1", "b2",
              "c0", "c1", "c2", "d0", "d1", "d2")
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


# --------------- pipeline, verbatim from isomonodromy_flow_probe.py
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
    """FROZEN GAUGE (docstring): SO(2)-rotate so that f is maximal
    and positive at the smallest-j node m0 (then g[m0] = 0); the
    global flip is excluded by f[m0] > 0."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def gen_rung(kz, **kw):
    r = dressed_port(kz, **kw)
    if not isinstance(r, dict):
        return r
    Y = np.diag(r["yp"])
    C = Y @ r["DP"] - r["DP"] @ Y
    f, g, sv = antisym_generators(C)
    r["f"], r["g"] = gauge_fix(f, g, r["jp"])
    r["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    r["kz"] = kz
    return r


def pair_data(ra, rb):
    com, ia, ib = np.intersect1d(ra["jp"], rb["jp"],
                                 return_indices=True)
    if len(com) < MIN_COMMON_J:
        return None
    return dict(n=len(com),
                fa=ra["f"][ia], ga=ra["g"][ia], ya=ra["yp"][ia],
                fb=rb["f"][ib], gb=rb["g"][ib], yb=rb["yp"][ib],
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


# ------------------------------------------------ probe-specific machinery
def lax2_fit(pd):
    """X1: degree-2 dictionary least squares on the common
    section; returns (cf, cg, res_f, res_g, F, G) with cf =
    (a0, a1, a2, b0, b1, b2), cg = (c0, c1, c2, d0, d1, d2) and
    (F, G) = the fitted rung-(k+1) generators f + Delta f_fit,
    g + Delta g_fit."""
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
    return (cf, cg, res_f, res_g,
            pd["fa"] + A @ cf, pd["ga"] + A @ cg)


def iiks_predict(F, G, yb, Db):
    """X3: IIKS kernel formula off the diagonal; the diagonal is
    NOT determined by the commutator and is copied from the
    actual matrix (typed in the docstring)."""
    n = len(yb)
    num = np.outer(F, G) - np.outer(G, F)
    den = yb[:, None] - yb[None, :]
    off = ~np.eye(n, dtype=bool)
    Dp = np.array(Db)          # diagonal kept actual
    Dp[off] = num[off] / den[off]
    err = (np.linalg.norm((Db - Dp)[off])
           / np.linalg.norm(Db[off]))
    return Dp, float(err)


def logdet_abs(M):
    _sgn, ld = np.linalg.slogdet(M)
    return float(ld)


def main():
    section("PRIME.PORT.LAX2.01 -- is the degree-2 closure a "
            "lawful, predictive Lax flow? (EXPLORATION ONLY)")
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
    n_skip_j = 0
    n_skip_dal = 0
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        pd = pair_data(ra, rb)
        if pd is None:
            n_skip_j += 1
            continue
        dal = rb["alpha"] - ra["alpha"]
        if abs(dal) <= DAL_MIN:
            n_skip_dal += 1
            continue
        pd["ha"], pd["hb"] = ra["h"], rb["h"]
        pd["dal"] = dal
        pd["al_deep"] = rb["alpha"]
        pairs.append(pd)
    check("W3 >= %d consecutive pairs with >= %d common j and "
          "|dal| > %.0e (typed skips: %d common-j, %d dal)"
          % (MIN_PAIRS, MIN_COMMON_J, DAL_MIN, n_skip_j,
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

    section("X1 -- deformation-polynomial coefficients along the "
            "ladder (12 per step)")
    print("    Delta f = (a0+a1 Y+a2 Y^2) f + (b0+b1 Y+b2 Y^2) g")
    print("    Delta g = (c0+c1 Y+c2 Y^2) f + (d0+d1 Y+d2 Y^2) g")
    res_fs, res_gs = [], []
    for pd in pairs:
        cf, cg, res_f, res_g, F, G = lax2_fit(pd)
        pd["cf"], pd["cg"] = cf, cg
        pd["F"], pd["G"] = F, G
        res_fs.append(res_f)
        res_gs.append(res_g)
        print("    h %3d->%3d  n=%2d  dal=%+.4f  res f %.3f "
              "g %.3f" % (pd["ha"], pd["hb"], pd["n"],
                          pd["dal"], res_f, res_g))
        print("      f: " + " ".join("%+9.2e" % v for v in cf))
        print("      g: " + " ".join("%+9.2e" % v for v in cg))
    print("    degree-2 fit residuals (ISOFLOW re-derived):")
    print("      res(Delta f): %s" % quart(res_fs))
    print("      res(Delta g): %s" % quart(res_gs))
    check("X1.1 coefficients extracted on all %d steps"
          % len(pairs), len(res_fs) == len(pairs))

    section("X2 -- flow lawfulness (frozen bar: median "
            "roughness ratio <= %.1f)" % LAWFUL_BAR)
    order = np.argsort([pd["al_deep"] for pd in pairs])
    V = np.array([np.concatenate([pairs[i]["cf"],
                                  pairs[i]["cg"]])
                  / pairs[i]["dal"] for i in order])
    ratios = []
    print("    normalized velocities v_i = c_i/dal, steps "
          "ordered by deeper-rung alpha;")
    print("    ratio_i = RMS(consecutive diff)/RMS(values) "
          "(lawful << 1, noise ~ 1.41):")
    for i, nm in enumerate(COEF_NAMES):
        v = V[:, i]
        rms = math.sqrt(float(np.mean(v ** 2)))
        rmsd = math.sqrt(float(np.mean(np.diff(v) ** 2)))
        rat = rmsd / max(rms, 1e-300)
        ratios.append(rat)
        print("      %-2s  RMS %.3e   ratio %.3f" % (nm, rms,
                                                     rat))
    med_ratio = float(np.median(ratios))
    flow_lawful = med_ratio <= LAWFUL_BAR
    print("    TYPED: median ratio %.3f vs bar %.1f -> %s"
          % (med_ratio, LAWFUL_BAR,
             "FLOW-LAWFUL" if flow_lawful else "FLOW-NOISY"))
    check("X2.1 lawfulness measured on 12 coefficient series "
          "(typed outcome, not a kill)", len(ratios) == 12)

    section("X3 -- operator-level predictivity (frozen bar: "
            "median offdiag err <= %.1f)" % PRED_BAR)
    print("    D_pred[m,m'] = (F_m G_m' - G_m F_m')/(y'_m - "
          "y'_m'), diagonal kept ACTUAL (typed:")
    print("    the IIKS commutator does not determine it -- the "
          "test is off-diagonal only).")
    errs = []
    for pd in pairs:
        Dp, err = iiks_predict(pd["F"], pd["G"], pd["yb"],
                               pd["Db"])
        pd["Dp"] = Dp
        errs.append(err)
    print("      offdiag rel err per step: %s" % quart(errs))
    med_err = float(np.median(errs))
    lax2_pred = med_err <= PRED_BAR
    print("    TYPED: median err %.3f vs bar %.1f -> %s"
          % (med_err, PRED_BAR,
             "LAX2-PREDICTIVE" if lax2_pred else "LAX2-PARTIAL"))
    check("X3.1 predictivity measured on all %d steps (typed "
          "outcome, not a kill)" % len(pairs),
          len(errs) == len(pairs))

    section("X4 -- integrated tau transfer (identity ward %.0e "
            "+ Lax accuracy report)" % IDENT_WARD)
    id_dev = []
    lax_acc = []
    for pd in pairs:
        Ia = np.eye(pd["n"])
        act = (logdet_abs(Ia - pd["Db"])
               - logdet_abs(Ia - pd["Da"]))
        exact = logdet_abs(
            Ia - np.linalg.solve(Ia - pd["Da"],
                                 pd["Db"] - pd["Da"]))
        pred = logdet_abs(
            Ia - np.linalg.solve(Ia - pd["Da"],
                                 pd["Dp"] - pd["Da"]))
        id_dev.append(abs(exact - act) / max(1.0, abs(act)))
        lax_acc.append(abs(pred - act) / max(abs(act), 1e-300))
    dev_max = float(np.max(id_dev))
    check("X4.1 IDENTITY WARD: max |exact - actual| (rel) "
          "%.2e <= %.0e (section bookkeeping consistent)"
          % (dev_max, IDENT_WARD), dev_max <= IDENT_WARD,
          kill="K1")
    print("    Lax-predicted Delta log|tau| (D_pred from X3) vs "
          "actual, |pred - act|/|act|:")
    print("      accuracy: %s  (the tau-transfer content of "
          "the degree-2 flow)" % quart(lax_acc))
    check("X4.2 tau transfer computed on all %d steps (report)"
          % len(pairs), len(lax_acc) == len(pairs))

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
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = ("LAX2-MEASURED / %s / %s"
                   % ("FLOW-LAWFUL" if flow_lawful
                      else "FLOW-NOISY",
                      "LAX2-PREDICTIVE" if lax2_pred
                      else "LAX2-PARTIAL"))
    print("\n  VERDICT: %s" % VERDICT)
    if not KILLS:
        print("  (X2 median roughness %.3f vs %.1f; X3 median "
              "offdiag err %.3f vs %.1f; X4 Lax tau accuracy "
              "med %.3f)"
              % (med_ratio, LAWFUL_BAR, med_err, PRED_BAR,
                 float(np.median(lax_acc))))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
