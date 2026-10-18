#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v885 -- PRIME.PORT.ISOFLOW.01 + PRIME.PORT.LADDER.TRANSFER.01 + PRIME.PORT.PRIMELADDER.01 + PRIME.PORT.LAX2.01: THE FLOW/INDUCTION ANATOMY OF THE LADDER -- the deformation direction measured on all four axes, ONE module from four probes (8/8 + 5/5 + 13/13 + 11/11 checks, zero fails, verdicts ISOFLOW-MEASURED (FLOW-OPEN, degree-2 qualifier) + LADDER-MEASURED (LADDER-PERTURBATIVE + NON-MONOTONE) + PRIMELADDER-MEASURED (ARCH-SUBCRITICAL / LAST-CROSSING-EDGE / OSCILLATORY-TAIL / EDGE-INSUFFICIENT) + LAX2-MEASURED (FLOW-NOISY / LAX2-PARTIAL); discovery probes isomonodromy_flow_probe.py, ladder_transfer_probe.py (SPEC v2), nested_prime_ladder_probe.py (SPEC v2), lax2_flow_probe.py (SPEC v2), 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~3.5 min).  The parametrix decision (v883) forces every small parameter into the flow/deformation direction; this module measures that direction honestly.  (1) THE GENERATOR FLOW CLOSES IN DEGREE 2 (isoflow): the gauge-fixed IIKS generator flow (f, g) over 41 consecutive ladder pairs does NOT close in the degree-1 dictionary {f, g, Yf, Yg} (medians 0.498/0.457 vs bar 0.3) but DOES close with {Y^2 f, Y^2 g} added (0.244/0.248 -- residuals halved): the ladder deformation is a DEGREE-2 LAX FLOW, isomonodromy-compatible, one degree above minimal; gauge stable (consecutive cos median 0.943); log tau runs monotonically -58.6 -> -396.6; honest typing: the controls close similarly -- degree-2 closure is a STRUCTURAL precondition, not a discriminator (the arithmetic stays in the VALUE).  (2) THE WINDOW-LADDER STEP IS MARGINALLY PERTURBATIVE BUT NOT A FLOW IN RAW h ORDER (ladder transfer): first-order transfer accuracy median 0.458 (bar 0.5, quartiles 0.19/0.91) on the compressed fixed-window objects; only 52 percent of steps increase lambda (NON-MONOTONE); ||Delta||/gap = 594-2026 (the hit rate comes from port concentration, not step smallness): the induction form needs a BETTER ORDER than h.  (3) THE ONE-PRIME LADDER DECIDES: POSITIVITY IS A PROPERTY OF THE COMPLETE COMB (nested prime ladder, the round-41 execution of that named object): inserting the prime-power atoms one at a time into the fixed window (exact per-atom lag rows, linearity warded at 0; endpoint warded vs the true floor at <= 2.5e-9 rel), the pure-Arch start is CATASTROPHICALLY subcritical (tau(0) = -9.9e13 at kz 9; G_plus not even PD at kz 13/26/40); the LAST sign crossing sits at u*/U = 0.991-0.999 (atom 68/70, 116/120, 133/136, 597/604, 1759/1773 on kz 9/12/13/26/40) -- ascending-u insertion needs 97-99 percent of the atoms; the edge-first ordering reaches stable positivity only at 100 percent (EDGE-INSUFFICIENT): NO ordering yields a monotone one-prime induction -- the wall emerges only at the complete comb (v877's truncation reversal sharpened to atom resolution; consistent with the global rigidity of v883); per-atom increments: 54-64 percent positive, corr(log|dtau|, log m) = +0.32..+0.49; the deterministic mass-scramble control drops the endpoint to -474.7.  (4) THE RAW COEFFICIENT BASIS OF THE DEGREE-2 FLOW IS ILL-CONDITIONED (lax2, the round-41 symbolic follow-up): the 12 deformation-polynomial coefficients per step are extracted on all 41 steps (degree-2 residual medians 0.244/0.248 re-derived), but normalized by the alpha step they behave as NOISE (median roughness ratio 1.365 vs lawful bar 0.7, near the sqrt(2) noise value); operator-level IIKS prediction from the fitted generators misses the bar narrowly (median offdiag rel err 0.350 vs 0.3, q25 0.172 -- LAX2-PARTIAL); the INTEGRATED tau-transfer identity holds exactly (section bookkeeping warded at 5.6e-11) while the Lax-predicted tau transfer is poor (median 2.26); controls fire on the value, the IIKS pipeline persists ([Y, D_P] rank 2 at 1e-14 even on controls); named interpretive lead (recorded, not acted on): the dictionary columns f, Yf, Y^2 f are nearly collinear because the port y-values cluster near 1 -- a well-conditioned reparametrization may expose a lawful flow the raw basis masks.  NET: the deformation direction exists (degree-2 Lax, isomonodromy-compatible) but neither raw h order nor raw coefficient bases are the natural flow parameter -- the natural coordinate is the named open object.  NO RH claim; no marker moves.  Float64 on the deployed v563 machinery; no zeros, no prime oracles (AST firewalls inside the probes); RNG only in declared scramble controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes isomonodromy_flow_probe.py (8/8,
ISOFLOW-MEASURED (FLOW-OPEN)), ladder_transfer_probe.py (5/5,
LADDER-MEASURED, SPEC v2: control-scope amendment on record),
nested_prime_ladder_probe.py (13/13, PRIMELADDER-MEASURED, SPEC v2:
endpoint-ward float-summation tolerance amendment on record),
lax2_flow_probe.py (11/11, LAX2-MEASURED, SPEC v2: X4 identity sign
amendment on record), all 2026-08-09, re-run identically at
promotion.  ROUND-31 EMBEDDING CONVENTION: frozen sources embedded
BYTE-EXACT, executed verbatim in isolated namespaces; printed spec
SHAs reproduce; byte-equality ward vs experiments/tfpt-discovery/
inside the pattern gates.  All probes consume the READ-ONLY deployed
core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; heavy rungs declared in
the frozen headers; all fail-first spec amendments preserved.
NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source isomonodromy_flow_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""isomonodromy_flow_probe -- PRIME.PORT.ISOFLOW.01
(EXPLORATION ONLY, experiments/; round 40, work package 3 first
step: measure whether the ladder evolution of the dressed-port
IIKS data is CLOSED in the integrable module -- the numerical
precondition for reading the window ladder as an ISOMONODROMIC
deformation whose tau function is the wall determinant,
2026-08-09).

THE QUESTION (frozen): PRIME.PORT.RIEMANNHILBERT.01 verified that
every rung's dressed port D_P is an IIKS kernel with explicit
generators (f, g) ([Y, D_P] = f g^T - g f^T exactly rank 2).  An
isomonodromic reading of the ladder requires more: the DEFORMATION
of the RH data along the ladder parameter (window depth h) must
stay inside the module generated by the current data -- a Lax-type
equation d(f, g)/dk in span{f, g, Y f, Y g}.  If it does, the
ladder is a discrete isomonodromic flow and log det(I - D_P) is
its tau function (Jimbo-Miwa-Ueno); if not, the deformation leaves
the module and the tau reading needs more data.

THE LADDER (frozen): all frame-A zones (core.frame_a_zones())
with h <= 900, sorted by (h, kz).  Port nodes carry the stable
alias index j = uf value of the folded node; consecutive rungs
are matched on the COMMON j-subset; a pair with < 8 common
indices is a typed skip (counted, warded).

FROZEN GAUGE (documented; the SVD pair (f, g) = sqrt(s1)(u1,
+-u2) has a residual SO(2) freedom -- rotations (f, g) -> (c f +
s g, -s f + c g) preserve f g^T - g f^T; reflections flip its
sign and are excluded): let m0 = the node with the SMALLEST alias
index j on the rung; rotate by (c, s) = (f[m0], g[m0]) /
hypot(f[m0], g[m0]).  Then f[m0] > 0 (maximal overlap of f with
the m0 coordinate) and g[m0] = 0; no SO(2) freedom remains, and
the global flip (f, g) -> (-f, -g) is excluded by f[m0] > 0.
Gauge health is WARDED by F3, not assumed.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 F1  GENERATOR FLOW CLOSURE: on each consecutive pair (k, k+1)
     restrict the gauge-fixed generators to the common j-set and
     form Delta f = f(k+1) - f(k), Delta g = g(k+1) - g(k).
     Least-squares expand each increment in the frozen degree-1
     dictionary {f(k), g(k), Y f(k), Y g(k)} (Y = diag of rung-k
     y-values at the common nodes); residual fraction res =
     ||Delta - fit|| / ||Delta||.  TYPED: FLOW-CLOSED iff the
     median res over all pairs is <= 0.3 for BOTH f and g, else
     FLOW-OPEN (honest).  Also reported (no bar): the enlarged
     degree-2 dictionary + {Y^2 f(k), Y^2 g(k)} -- does closure
     need degree 2?

 F2  TAU-LOGDERIV CONSISTENCY (report, no bar): log tau_k =
     log det(I - D_P(k)) along the ladder (slogdet); on the
     common-j section of each pair, Delta log tau vs the
     first-order transfer -tr[(I - D_P)^{-1} Delta D_P] (the
     finite-difference shadow of the Jimbo-Miwa-Ueno formula);
     accuracy ratio |pred - actual| / |actual| reported.

 F3  GAUGE STABILITY WARD: cos similarity of gauge-fixed f
     between consecutive rungs (common j) must have median
     >= 0.7 (ward: below this the gauge is unstable and F1 is
     meaningless); the profile cos(f(k), f(deepest)) is reported.

 W   PIPELINE WARDS: >= 30 rungs built; every rung [Y, D_P]
     rank 2 (s3/s1 <= 1e-10); >= 30 consecutive pairs with >= 8
     common j (typed skips counted).

 C   CONTROLS (kz 9 -> 12, must fire): Epstein (lambda_eps
     recursion comb rebuilt per rung) + scramble (seed 1, both
     rungs): lam(E) > 1 on both rungs (value fires); [Y, D_P]
     rank 2 persists (algebra is class membership); their F1
     residuals on the pair reported (no bar).

KILLS: K1 pipeline/gauge ward breaks -> PIPELINE-BROKEN;
K2 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): ISOFLOW-MEASURED with typed sublabel
FLOW-CLOSED / FLOW-OPEN, else PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim -- flow closure is a numerical precondition for the
isomonodromy/tau program, not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; pipeline copied
verbatim from port_riemann_hilbert_setup_probe.py (PRIME.PORT.
RIEMANNHILBERT.01, incl. the v2 generator extraction); IIKS =
Its-Izergin-Korepin-Slavnov; JMU = Jimbo-Miwa-Ueno tau function.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/isomonodromy_flow_probe.py
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
RES_BAR = 0.3
GAUGE_COS_BAR = 0.7
RANK_BAR = 1e-10
CTRL_PAIR = (9, 12)
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


# ------------- pipeline, verbatim from port_riemann_hilbert_setup_probe.py
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


# ------------------------------------------------ probe-specific machinery
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


def fit_res(delta, cols):
    A = np.stack(cols, axis=1)
    coef, *_ = np.linalg.lstsq(A, delta, rcond=None)
    return float(np.linalg.norm(delta - A @ coef)
                 / np.linalg.norm(delta))


def pair_data(ra, rb):
    com, ia, ib = np.intersect1d(ra["jp"], rb["jp"],
                                 return_indices=True)
    if len(com) < MIN_COMMON_J:
        return None
    return dict(n=len(com),
                fa=ra["f"][ia], ga=ra["g"][ia], ya=ra["yp"][ia],
                fb=rb["f"][ib], gb=rb["g"][ib],
                Da=ra["DP"][np.ix_(ia, ia)],
                Db=rb["DP"][np.ix_(ib, ib)])


def closure_residuals(pd):
    d1 = [pd["fa"], pd["ga"], pd["ya"] * pd["fa"],
          pd["ya"] * pd["ga"]]
    d2 = d1 + [pd["ya"] ** 2 * pd["fa"], pd["ya"] ** 2 * pd["ga"]]
    df, dg = pd["fb"] - pd["fa"], pd["gb"] - pd["ga"]
    return (fit_res(df, d1), fit_res(dg, d1),
            fit_res(df, d2), fit_res(dg, d2))


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


def main():
    section("PRIME.PORT.ISOFLOW.01 -- is the ladder flow of the "
            "IIKS data closed? (EXPLORATION ONLY)")
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
    n_skip = 0
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        pd = pair_data(ra, rb)
        if pd is None:
            n_skip += 1
            continue
        pd["ha"], pd["hb"] = ra["h"], rb["h"]
        pd["ra"], pd["rb"] = ra, rb
        pairs.append(pd)
    check("W3 >= %d consecutive pairs with >= %d common j "
          "(typed skips: %d)" % (MIN_PAIRS, MIN_COMMON_J, n_skip),
          len(pairs) >= MIN_PAIRS, "%d pairs" % len(pairs),
          kill="K1")

    section("F3 -- gauge stability ward (before F1: no stable "
            "gauge, no closure test)")
    cosc = []
    for pd in pairs:
        cosc.append(abs(float(
            pd["fa"] @ pd["fb"]
            / (np.linalg.norm(pd["fa"])
               * np.linalg.norm(pd["fb"])))))
    print("    consecutive |cos(f_k, f_k+1)| on common j: %s"
          % quart(cosc))
    deep = rungs[-1]
    prof = []
    for ra in rungs[:-1]:
        pd = pair_data(ra, deep)
        if pd is None:
            continue
        prof.append((ra["h"], float(
            pd["fa"] @ pd["fb"]
            / (np.linalg.norm(pd["fa"])
               * np.linalg.norm(pd["fb"])))))
    print("    profile cos(f(k), f(deepest h=%d)):" % deep["h"])
    line = "     "
    for hh, cc in prof:
        tok = " %d:%+.2f" % (hh, cc)
        if len(line) + len(tok) > 72:
            print(line)
            line = "     "
        line += tok
    if line.strip():
        print(line)
    med_cos = float(np.median(cosc))
    check("F3.1 GAUGE STABLE: median consecutive |cos| %.3f >= "
          "%.1f" % (med_cos, GAUGE_COS_BAR),
          med_cos >= GAUGE_COS_BAR, kill="K1")

    section("F1 -- generator flow closure (frozen bar: median "
            "res <= %.1f, degree-1 dictionary)" % RES_BAR)
    rf1, rg1, rf2, rg2 = [], [], [], []
    for pd in pairs:
        a, b, c, d = closure_residuals(pd)
        rf1.append(a)
        rg1.append(b)
        rf2.append(c)
        rg2.append(d)
    print("    degree-1 {f, g, Yf, Yg}:")
    print("      res(Delta f): %s" % quart(rf1))
    print("      res(Delta g): %s" % quart(rg1))
    print("    degree-2 + {Y^2 f, Y^2 g} (report, no bar):")
    print("      res(Delta f): %s" % quart(rf2))
    print("      res(Delta g): %s" % quart(rg2))
    med_f1, med_g1 = float(np.median(rf1)), float(np.median(rg1))
    med_f2, med_g2 = float(np.median(rf2)), float(np.median(rg2))
    flow_closed = med_f1 <= RES_BAR and med_g1 <= RES_BAR
    deg2_closed = med_f2 <= RES_BAR and med_g2 <= RES_BAR
    print("    TYPED: degree-1 medians (f %.3f, g %.3f) vs bar "
          "%.1f -> %s" % (med_f1, med_g1, RES_BAR,
                          "FLOW-CLOSED" if flow_closed
                          else "FLOW-OPEN"))
    print("    degree-2 medians (f %.3f, g %.3f) -> %s"
          % (med_f2, med_g2,
             "closes at degree 2" if deg2_closed
             else "open even at degree 2"))
    check("F1.1 closure measured on %d pairs (typed outcome, "
          "not a kill)" % len(pairs), len(pairs) >= MIN_PAIRS)

    section("F2 -- tau log-derivative consistency (report, "
            "no bar)")
    lt = []
    for r in rungs:
        sgn, ld = np.linalg.slogdet(np.eye(r["DP"].shape[0])
                                    - r["DP"])
        lt.append((r["h"], sgn, ld))
    print("    log tau_k = slogdet(I - D_P(k)), full port "
          "matrix (h, sign, log|det|):")
    line = "     "
    for hh, sgn, ld in lt:
        tok = " %d:%+d:%.1f" % (hh, int(sgn), ld)
        if len(line) + len(tok) > 72:
            print(line)
            line = "     "
        line += tok
    if line.strip():
        print(line)
    accs = []
    for pd in pairs:
        Ia = np.eye(pd["n"])
        _, la = np.linalg.slogdet(Ia - pd["Da"])
        _, lb = np.linalg.slogdet(Ia - pd["Db"])
        act = lb - la
        pred = -float(np.trace(np.linalg.solve(
            Ia - pd["Da"], pd["Db"] - pd["Da"])))
        accs.append(abs(pred - act) / max(abs(act), 1e-300))
    print("    common-j section: |pred - actual|/|actual| of "
          "Delta log tau vs -tr[(I-D_P)^{-1} Delta D_P]:")
    print("      accuracy ratio: %s  (JMU shadow: the ladder "
          "step is NOT infinitesimal)" % quart(accs))
    check("F2.1 tau consistency computed on %d pairs (report)"
          % len(accs), len(accs) == len(pairs))

    section("C -- controls (kz %d -> %d, must fire)" % CTRL_PAIR)
    ok = True
    for nmc, kws in (
            ("Epstein", [dict(comb=eps_comb(CTRL_PAIR[0])),
                         dict(comb=eps_comb(CTRL_PAIR[1]))]),
            ("scramble", [dict(scramble_seed=1),
                          dict(scramble_seed=1)])):
        ra = gen_rung(CTRL_PAIR[0], **kws[0])
        rb = gen_rung(CTRL_PAIR[1], **kws[1])
        ok &= ra["lamE"] > 1.0 and rb["lamE"] > 1.0
        ok &= max(ra["rk"], rb["rk"]) <= 1e-8
        pd = pair_data(ra, rb)
        if pd is None:
            print("    %-8s: lam(E) %.3e/%.3e | rank %.1e/%.1e "
                  "| < %d common j (F1 not reportable)"
                  % (nmc, ra["lamE"], rb["lamE"], ra["rk"],
                     rb["rk"], MIN_COMMON_J))
            continue
        a, b, _c, _d = closure_residuals(pd)
        print("    %-8s: lam(E) %.3e/%.3e (fires) | [Y,D_P] "
              "s3/s1 %.1e/%.1e (algebra persists) | F1 res "
              "(no bar): f %.3f g %.3f on %d common j"
              % (nmc, ra["lamE"], rb["lamE"], ra["rk"],
                 rb["rk"], a, b, pd["n"]))
    check("C1 CONTROLS FIRE (value) and the IIKS algebra "
          "persists", ok, kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = ("ISOFLOW-MEASURED / FLOW-CLOSED"
                   if flow_closed
                   else "ISOFLOW-MEASURED / FLOW-OPEN")
    print("\n  VERDICT: %s" % VERDICT)
    if not KILLS and not flow_closed:
        print("  (degree-2 dictionary medians f %.3f, g %.3f -> "
              "%s)" % (med_f2, med_g2,
                       "closure needs degree 2" if deg2_closed
                       else "open at degree 2 as well"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source ladder_transfer_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ladder_transfer_probe -- PRIME.PORT.LADDER.TRANSFER.01
(EXPLORATION ONLY, experiments/; round 40, work package 1 of the
parallel closing push: is the LADDER STEP perturbative -- the
forced direction after FLUCTUATIONS-REQUIRED killed comb-space
perturbation theory, 2026-08-09).

THE QUESTION: comb deformations cannot be the small parameter
(lattice_parametrix_probe: the Euler-product pairing is load-
bearing).  The remaining perturbative direction is ALONG THE
LADDER: the compressed fixed-window family C_J(h) converges fast
(slope -2.80, XCIV), so consecutive rungs are CLOSE.  If the
one-step update is (a) first-order accurate on the top eigenpair
and (b) sign/size-structured, an INDUCTION shape opens: wall
positivity propagates rung to rung -- a proof form that never
needs a uniform margin, only step stability.

FROZEN PROTOCOL (2026-08-09; ALL ladder rungs h <= 900 sorted by
h; the compressed fixed-window objects C_J on the common j-window
J = {2,...,24} subset per pair; consecutive pairs (k, k+1)):

 L1  FIRST-ORDER TRANSFER: with v_k the top eigenvector of
     C_J(h_k) and Delta_k = C_J(h_{k+1}) - C_J(h_k) on the common
     j-subset: predict lam_{k+1} ~ lam_k + <v_k, Delta_k v_k>;
     measure the accuracy ratio acc_k = |predicted - actual| /
     |actual move|; typed LADDER-PERTURBATIVE iff median acc <=
     0.5 (the step is first-order tractable), else LADDER-ROUGH.

 L2  STEP ANATOMY (report): per step the increment norm
     ||Delta_k||_2, the perturbative ratio ||Delta_k||/gap_k
     (gap = lam_1 - lam_2 of rung k), and the inertia of Delta_k
     (positive/negative eigenvalue counts -- is the step
     sign-structured?).

 L3  MONOTONICITY: is lam_max(C_J) increasing at (almost) every
     step (the approach-from-below in step form)?  Typed
     MONOTONE iff >= 90 percent of steps increase lam, else
     NON-MONOTONE (both honest; monotone would be the induction
     invariant candidate).

 C   CONTROLS (kz 9, must fire): Epstein/scramble lam(E) > 1
     (value; the transfer structure is not probed there --
     different criticality side).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 controls silent
-> CONTROL-DEAD.  L1/L3 typed dichotomies.

SPEC v2 (control-scope repair; run 1 = 4/5): the v1 control used
the compressed-window object, but the SCRAMBLE comb's folded port
does not contain the fixed J-window (different sign pattern of
d), so the constructor returned None although lam(E) > 1 is
long-established for it -- a mechanical scope slip.  v2 fires the
control on lam(E) of the plain Carleson Gram (no window
requirement); the window unavailability is typed in the print.
No other change.

VERDICT (frozen enum): LADDER-MEASURED (+ typed sublabels) /
PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
v563 READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; port_cocycle_window
probe (XCIV, the compression machinery), lattice_parametrix
probe (XCVI, the forcing result).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ladder_transfer_probe.py
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

JWIN = tuple(range(2, 25, 2))
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


def compressed_window(kz, **kw):
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) < 8:
        return dict(CJ=None, jav=jav, h=h,
                    lamE=float(np.linalg.eigvalsh(E)[-1]))
    iw = [idx[j] for j in jav]
    io = [k for k in range(E.shape[0]) if k not in set(iw)]
    IO = np.eye(len(io)) - E[np.ix_(io, io)]
    CJ = E[np.ix_(iw, iw)] + E[np.ix_(iw, io)] @ np.linalg.solve(
        IO, E[np.ix_(io, iw)])
    CJ = 0.5 * (CJ + CJ.T)
    return dict(CJ=CJ, jav=jav, h=h,
                lamE=float(np.linalg.eigvalsh(E)[-1]))


def main():
    section("PRIME.PORT.LADDER.TRANSFER.01 -- is the ladder step "
            "perturbative? (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("L1/L2/L3 -- the one-step transfer along the ladder")
    rows = []
    for kz in core.frame_a_zones():
        r = compressed_window(kz)
        if r in (None, "TOO-DEEP") or r["CJ"] is None:
            continue
        rows.append(r)
    rows.sort(key=lambda r: r["h"])
    accs, ratios, mono = [], [], []
    pos_counts, neg_counts = [], []
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        common = [j for j in a["jav"] if j in b["jav"]]
        if len(common) < 8:
            continue
        ia = [a["jav"].index(j) for j in common]
        ib = [b["jav"].index(j) for j in common]
        A = a["CJ"][np.ix_(ia, ia)]
        B = b["CJ"][np.ix_(ib, ib)]
        evA, VA = np.linalg.eigh(A)
        evB = np.linalg.eigvalsh(B)
        v = VA[:, -1]
        Dlt = B - A
        move = float(evB[-1] - evA[-1])
        pred = float(v @ Dlt @ v)
        acc = abs(pred - move) / max(abs(move), 1e-30)
        accs.append(acc)
        gap = float(evA[-1] - evA[-2])
        nrm = float(np.linalg.norm(Dlt, 2))
        ratios.append(nrm / max(gap, 1e-30))
        evD = np.linalg.eigvalsh(Dlt)
        pos_counts.append(int(np.sum(evD > 1e-12)))
        neg_counts.append(int(np.sum(evD < -1e-12)))
        mono.append(move > 0)
    accs = np.array(accs)
    ratios = np.array(ratios)
    med_acc = float(np.median(accs))
    l1_type = ("LADDER-PERTURBATIVE" if med_acc <= 0.5
               else "LADDER-ROUGH")
    check("L1.1 typed: %s -- first-order transfer accuracy over "
          "%d steps: median %.3f, quartiles %.3f/%.3f (bar 0.5)"
          % (l1_type, len(accs), med_acc,
             float(np.percentile(accs, 25)),
             float(np.percentile(accs, 75))), True)
    check("L2.1 STEP ANATOMY (report): ||Delta||/gap quartiles "
          "%.1f/%.1f/%.1f; increment inertia (pos, neg) medians "
          "(%d, %d) of 12 -- sign-structure census"
          % (float(np.percentile(ratios, 25)),
             float(np.percentile(ratios, 50)),
             float(np.percentile(ratios, 75)),
             int(np.median(pos_counts)),
             int(np.median(neg_counts))), True)
    frac_mono = float(np.mean(mono))
    l3_type = "MONOTONE" if frac_mono >= 0.9 else "NON-MONOTONE"
    check("L3.1 typed: %s -- lam_max increases on %.0f percent "
          "of steps (bar 90)" % (l3_type, 100 * frac_mono), True)

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        r = compressed_window(9, **kw)
        fired = (r not in (None, "TOO-DEEP")) and r["lamE"] > 1.0
        ok &= fired
        print("    %-8s: lam(E) %s -> fires %s%s"
              % (nmc, "%.3e" % r["lamE"]
                 if r not in (None, "TOO-DEEP") else "n/a", fired,
                 "" if r in (None, "TOO-DEEP")
                 or r["CJ"] is not None
                 else " (window unavailable, typed -- SPEC v2)"))
    check("C1 CONTROLS FIRE (SPEC v2: on the plain-Gram value)",
          ok, kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    VERDICT = ("CONTROL-DEAD" if KILLS else "LADDER-MEASURED")
    print("\n  VERDICT: %s (%s + %s)" % (VERDICT, l1_type,
                                         l3_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source nested_prime_ladder_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""nested_prime_ladder_probe -- PRIME.PORT.PRIMELADDER.01
(EXPLORATION ONLY, experiments/; round 40, work package (c) of the
closing-cylinder plan: the NESTED ONE-PRIME LADDER, 2026-08-09).

CONTEXT: the window ladder (rung -> rung) is perturbative but
non-monotone (LADDER-PERTURBATIVE, round 40).  The finer induction
object is the ONE-PRIME ladder INSIDE a fixed window: start from
the pure archimedean lag vector and insert the prime-power atoms
one at a time (ascending u = log n, the physical order), tracking
the pencil floor tau(k) after each insertion.  v877 says truncated
combs violate the floor, so the trajectory must end positive only
at the FULL comb -- the question is the ANATOMY of the path: where
is the last sign crossing, what do single atoms contribute, and is
the final approach monotone?  A second ordering (descending u =
edge-first) probes whether the edge zone alone can carry
positivity (39 percent of the mass sits in the last half
log-unit).

FROZEN PROTOCOL (heavy rungs kz in {9, 12, 13, 26, 40}):
  L1  TRAJECTORY (ascending u): per-atom lag rows are exact
      (atom_lags_at is linear in the mass list; ward L1.0 checks
      the row sum against the full call at 1e-12).  tau(0) = pure
      Arch floor; tau(N) must equal the true wall floor (ward
      L1.1, rel 1e-8; SPEC v2: v1 froze 1e-9 and FAILED honestly
      at kz 40 only -- rel 2.50e-9 on tau ~ 6.7e-7, pure float
      summation-order noise over 1773 sequential row additions vs
      one batched call; mechanical tolerance repair, all other
      rungs pass at <= 1e-9).  Report tau(0) sign census (typed
      ARCH-SUBCRITICAL iff tau(0) < 0 on every heavy rung, else
      ARCH-MIXED).
  L2  LAST CROSSING: u* = position of the last sign change of
      tau(k) along ascending-u insertion; typed
      LAST-CROSSING-EDGE iff u*/U >= 0.8 on every heavy rung
      (positivity decided in the edge zone), else
      LAST-CROSSING-BULK.
  L3  INCREMENT ANATOMY: per-atom increments dtau_n = tau(n) -
      tau(n-1); sign census (fraction positive), and the Pearson
      correlation of log|dtau_n| with log m_n (m_n = 2 Lambda/
      sqrt(n)) over atoms with |dtau_n| > 1e-15.  Report only
      (no bar): the size law of single-atom moves.
  L4  TAIL SHAPE: after the last crossing, is tau(k) monotone
      nondecreasing (tolerance 1e-12)?  Typed MONOTONE-TAIL iff
      true on every heavy rung, else OSCILLATORY-TAIL (both
      honest).
  L5  EDGE-FIRST ORDERING (descending u): does the trajectory
      reach tau > 0 earlier (fewer atoms) than ascending?  Report
      k*_desc/N vs k*_asc/N (k* = first index after which tau
      stays positive).  Typed EDGE-CARRIES iff k*_desc/N <= 0.5
      on every heavy rung, else EDGE-INSUFFICIENT.
  C1  CONTROL (kz 9): deterministic mass scramble (multiply atom
      n by (1 + 0.5 * sign(sin(1000 u_n)))): the full-comb floor
      must drop below the true floor minus 0.25 absolute OR go
      negative (the trajectory endpoint is mass-sensitive).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 ward L1.0/L1.1
fails -> LINEARITY-BROKEN; K3 control C1 fails -> CONTROL-DEAD.

VERDICT (frozen enum): PRIMELADDER-MEASURED (+ typed sublabels
from L1/L2/L4/L5) / PIPELINE-BROKEN / LINEARITY-BROKEN /
CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan; the
atoms come from the deployed v563 window tables); v563 READ-ONLY;
no RNG; stdout only.

Sources (read-only): v563_paper2_readouts; v877 (truncation
kills); lattice_parametrix probe (round 40, mass rigidity);
ladder_transfer probe (round 40, window-ladder anatomy).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/nested_prime_ladder_probe.py
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

HEAVY = (9, 12, 13, 26, 40)
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


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def floor_of(c, M):
    K = core.odd_toeplitz(c, M)
    d = grid_density(c)
    c_abs = np.real(np.fft.ifft(np.abs(d)))[:M]
    Tabs = core.odd_toeplitz(c_abs, M)
    Gp = 0.5 * (Tabs + K)
    Gm = 0.5 * (Tabs - K)
    ev, V = np.linalg.eigh(Gp)
    if float(ev[0]) <= 0.0:
        return None
    R = V @ np.diag(ev ** -0.5) @ V.T
    A = R @ Gm @ R
    lam = np.linalg.eigvalsh(0.5 * (A + A.T))
    return 1.0 - float(lam[-1])


def trajectory(c_ar, rows, order, M):
    """tau(k) after inserting atoms rows[order[:k]], k = 0..N."""
    taus = []
    c = c_ar.copy()
    taus.append(floor_of(c, M))
    for idx in order:
        c = c + rows[idx]
        taus.append(floor_of(c, M))
    return taus


def last_crossing(taus):
    """index of the last sign change (None -> treated as sign of 0-)."""
    k_star = 0
    prev = taus[0] if taus[0] is not None else -1.0
    for k in range(1, len(taus)):
        cur = taus[k] if taus[k] is not None else -1.0
        if (prev <= 0.0) != (cur <= 0.0):
            k_star = k
        prev = cur
    return k_star


def first_stable_positive(taus):
    """first k such that tau(j) > 0 for all j >= k."""
    k = len(taus)
    for j in range(len(taus) - 1, -1, -1):
        t = taus[j] if taus[j] is not None else -1.0
        if t > 0.0:
            k = j
        else:
            break
    return k


def main():
    section("PRIME.PORT.PRIMELADDER.01 -- the nested one-prime "
            "ladder inside a fixed window (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; deterministic; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    arch_sub, edge_cross, mono_tail, edge_carries = [], [], [], []
    sign_frac_all, corr_all = [], []
    ward_ok = True
    for kz in HEAVY:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        N = len(uu)
        U = float(np.max(uu))
        c_ar = np.asarray(core.arch_lags(M, D), float)

        section("L -- kz %d (h %d, N_atoms %d, U %.3f)"
                % (kz, h, N, U))
        # exact per-atom lag rows (linearity ward below)
        rows = np.zeros((N, M))
        for n in range(N):
            c_at, _ = core.atom_lags_at(alpha, M, [uu[n]],
                                        [mm[n]])
            rows[n] = np.asarray(c_at, float)
        c_full, _ = core.atom_lags_at(alpha, M, uu, mm)
        lin_err = float(np.max(np.abs(rows.sum(axis=0)
                                      - np.asarray(c_full, float))))
        ok0 = check("L1.0 kz %d linearity ward (row sum == full "
                    "call)" % kz, lin_err <= 1e-12,
                    "max err %.2e" % lin_err, kill="K2")
        ward_ok &= ok0

        asc = list(range(N))
        taus = trajectory(c_ar, rows, asc, M)
        tau0, tauN = taus[0], taus[-1]
        tau_true = floor_of(c_ar + np.asarray(c_full, float), M)
        rel = abs(tauN - tau_true) / max(1e-30, abs(tau_true))
        ok1 = check("L1.1 kz %d endpoint ward (tau(N) == true "
                    "floor)" % kz, rel <= 1e-8,
                    "tau(N) %+0.6e rel %.2e" % (tauN, rel),
                    kill="K2")
        ward_ok &= ok1
        arch_sub.append(tau0 is None or tau0 < 0.0)
        print("    tau(0) [pure Arch] = %s"
              % ("None (Gp not PD)" if tau0 is None
                 else "%+0.6e" % tau0))

        k_cross = last_crossing(taus)
        u_star = uu[k_cross - 1] if k_cross >= 1 else 0.0
        frac = u_star / U
        edge_cross.append(frac >= 0.8)
        print("    L2 last crossing at atom %d/%d, u* %.3f "
              "(u*/U = %.3f)" % (k_cross, N, u_star, frac))

        dt = np.diff(np.array([t if t is not None else np.nan
                               for t in taus]))
        good = np.isfinite(dt) & (np.abs(dt) > 1e-15)
        sf = float(np.mean(dt[good] > 0)) if good.any() else 0.0
        sign_frac_all.append(sf)
        if int(np.sum(good)) >= 8:
            x = np.log(np.abs(dt[good]))
            y = np.log(mm[np.where(good)[0]])
            cx = x - x.mean()
            cy = y - y.mean()
            corr = float(np.sum(cx * cy)
                         / max(1e-30,
                               math.sqrt(float(np.sum(cx * cx))
                                         * float(np.sum(cy
                                                        * cy)))))
        else:
            corr = float("nan")
        corr_all.append(corr)
        print("    L3 increments: frac positive %.3f | corr("
              "log|dtau|, log m) %+.3f" % (sf, corr))

        tail = [t if t is not None else -1.0
                for t in taus[k_cross:]]
        mono = all(tail[i + 1] >= tail[i] - 1e-12
                   for i in range(len(tail) - 1))
        mono_tail.append(mono)
        print("    L4 tail after last crossing: %s"
              % ("MONOTONE" if mono else "OSCILLATORY"))

        desc = list(range(N - 1, -1, -1))
        taus_d = trajectory(c_ar, rows, desc, M)
        ka = first_stable_positive(taus)
        kd = first_stable_positive(taus_d)
        edge_carries.append(kd / max(1, N) <= 0.5)
        print("    L5 first stable positive: ascending %d/%d "
              "(%.3f) | edge-first %d/%d (%.3f)"
              % (ka, N, ka / max(1, N), kd, N, kd / max(1, N)))

    section("T -- typed outcomes")
    lab1 = ("ARCH-SUBCRITICAL" if all(arch_sub) else "ARCH-MIXED")
    lab2 = ("LAST-CROSSING-EDGE" if all(edge_cross)
            else "LAST-CROSSING-BULK")
    lab4 = ("MONOTONE-TAIL" if all(mono_tail)
            else "OSCILLATORY-TAIL")
    lab5 = ("EDGE-CARRIES" if all(edge_carries)
            else "EDGE-INSUFFICIENT")
    check("T.1 typed: %s / %s / %s / %s" % (lab1, lab2, lab4,
                                            lab5), True)
    print("    increment sign fractions: %s"
          % ", ".join("%.3f" % s for s in sign_frac_all))
    print("    size-law correlations:    %s"
          % ", ".join("%+.3f" % c for c in corr_all))

    section("C -- control (kz 9, deterministic mass scramble)")
    rr = core.build_window(9)
    M, alpha = rr["M"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, rr["D"]), float)
    mm_s = mm * (1.0 + 0.5 * np.sign(np.sin(1000.0 * uu)))
    c_s, _ = core.atom_lags_at(alpha, M, uu, mm_s)
    tau_s = floor_of(c_ar + np.asarray(c_s, float), M)
    c_t, _ = core.atom_lags_at(alpha, M, uu, mm)
    tau_t = floor_of(c_ar + np.asarray(c_t, float), M)
    fired = (tau_s is None or tau_s < 0.0
             or tau_s < tau_t - 0.25)
    check("C1 mass scramble drops the endpoint", fired,
          "tau_true %+0.4e tau_scr %s"
          % (tau_t, "None" if tau_s is None else "%+0.4e"
             % tau_s), kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if not ward_ok:
        VERDICT = "LINEARITY-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "PRIMELADDER-MEASURED"
    print("\n  VERDICT: %s (%s / %s / %s / %s)"
          % (VERDICT, lab1, lab2, lab4, lab5))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source lax2_flow_probe (embedded BYTE-EXACT, raw string)
_SRC_3 = r'''
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
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('isomonodromy_flow_probe', _SRC_0, 8, (), 'ISOFLOW-MEASURED', 0),
    ('ladder_transfer_probe', _SRC_1, 5, (), 'LADDER-MEASURED', 0),
    ('nested_prime_ladder_probe', _SRC_2, 13, (), 'PRIMELADDER-MEASURED', 0),
    ('lax2_flow_probe', _SRC_3, 11, (), 'LAX2-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v885 -- PRIME.PORT.ISOFLOW.01 + PRIME.PORT.LADDER.TRANSFER.01 + PRIME.PORT.PRIMELADDER.01 + PRIME.PORT.LAX2.01: the flow/induction anatomy of the ladder -- degree-2 Lax closure, marginal perturbativity, and the complete-comb decision of the one-prime ladder')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v885: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the deformation direction is measured: degree-2 Lax flow; positivity is a property of the COMPLETE comb')
    print("[%s] v885 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
