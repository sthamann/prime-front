#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""shat_band_organization_probe -- PRIME.PORT.SHAT.BAND.01
(EXPLORATION ONLY, experiments/; round 62, secondary probe: does
the x = +1 BAND organize the geometric normalization shat_h =
m_h / mu1(h) where alpha, h and the node could not (CXLIII: R^2
0.003 / 0.027 / 0.000)?  The band functionals come from
PRIME.PORT.BAND.ANATOMY.01 (round 62).  2026-08-10.)

THE OBJECT.  shat_h = m_h / mu1(h) with m_h = lam_min of the
odd-Toeplitz wall (arithmetic_lift_race surface, 67 faithful
rungs h 142..1433) and mu1(h) = 4 sin^2(pi/(2h+1)) (deployed
KMS/Dirichlet parity geometry) lies in [0.502, 2.185] with NO
one-variable organization (moving_node_second_order, CXLIII).
REPARAM-DECLARED (frozen, verbatim CXLIII): shat is the wall
margin REPARAMETRIZED; no new floor is claimed anywhere here; a
successful regression would ORGANIZE the scatter, not certify
anything.  The band functionals per rung (Gram surface, 42
rungs; band = x > 1 - DELTA): E_band (the (1 - x)-localized
Mm-eigenvector energy in the band, round-60 object), m_band (raw
mu_- band mass), wshare (band energy share), n90 (census
concentration count), and beta (v902 boundary term, full-window
rungs).  Surfaces are joined on common kz.

FROZEN REGRESSOR LIST (log of positive functionals; two-variable
combos by OLS on the pair): x1 = log E_band; x2 = log m_band;
x3 = wshare; x4 = log n90; x5 = log beta (full-window subset);
baselines alpha, log h (CXLIII comparison recomputed on the SAME
common subset); pairs (x1, log h), (x5, log h), (x3, alpha).
TYPED: BAND-ORGANIZES(best R^2) iff best R^2 >= 0.50 /
BAND-PARTIAL iff >= 0.25 / BAND-DEAD else -- honest R^2
comparison, no fit promoted to law.

FROZEN PROTOCOL: W1 faithful odd-Toeplitz ladder >= 40 rungs
(kill K1); W2 WARD m_h > 0 everywhere (kill K2); W3 REPRODUCTION
CXLIII: shat min/med/max == 0.502/1.027/2.185 (rtol 2e-2/5e-2/
2e-2) (kill K2); W4 Gram-surface band ladder == 42 rungs and W5
common kz >= 30 (kill K1); E1 the regression table (typed, never
kills); C controls (kill K2 if silent): C1 smooth world shat_sm
< 0 on every rung (CXLIII regression); C2 Epstein + scramble at
kz 9: lam_min < 0 (shat undefined/negative -- the organization
question cannot even be posed off the truth comb).

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; DELTA = 1e-2;
SHAT_MIN_REF = 0.502 (rtol 2e-2); SHAT_MED_REF = 1.027 (rtol
5e-2); SHAT_MAX_REF = 2.185 (rtol 2e-2); N_BAND_RUNGS = 42;
MIN_COMMON = 30; R2_ORG = 0.50; R2_PART = 0.25; H_DEEP_MAX =
900; JWIN = (2,...,24); CTRL_KZ = 9; scramble seed 1;
NG_SMOOTH = 6000.  Runtime cap declared: 10 min.

ANTI-CIRCULARITY: mu1 is pure geometry; m_h and the band
functionals are measured outcomes of the deployed pipeline; no
sigma_h, no target factorization; everything here is regression
anatomy, typed as such.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke
run of this script (9/9 with the identical bars; NO bar, band,
count, rule or enum was moved after it) measured: ladders green
(67 faithful rungs, shat 0.502/1.027/2.185 reproduced exactly;
42 band rungs; 42 common kz, 37 with beta).  E1 THE FIRST
PARTIAL ORGANIZATION: log E_band ALONE reaches R^2 = 0.278 --
ABOVE both baselines on the SAME subset (log h 0.156, alpha
0.000; note log h itself climbs from the ladder-wide 0.027 to
0.156 on this 42-rung subset, said openly) -- and the pair
(log E_band, log h) reaches 0.326; the rest: log m_band 0.161,
wshare 0.100, log beta 0.078, log n90 0.000, (log beta, log h)
0.283, (wshare, alpha) 0.100.  Best band value 0.326 is between
the PARTIAL (0.25) and ORGANIZES (0.50) bars: the band energy is
the FIRST functional that sees ANY of the shat variance
(CXLIII: node 0.000, alpha 0.003, log h 0.027 ladder-wide), but
~2/3 of the scatter stays uncarried -- consistent with the
CI/CXL reading that the rest is head-carried lift jitter.
Controls: smooth shat_sm < 0 on 67/67, Epstein lam_min
-1.01e+01 and scramble -7.86e+00 fire.  Runtime 20 s.
Fail-first preserved: nothing was weakened.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above; mechanical concretizations: window memoization,
one- and two-variable OLS R^2 population statistics, common join
strictly by kz, log applied only to strictly positive columns
(rows with nonpositive values excluded and counted).

NO RH claim; no marker moves; no promotion.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; shat machinery
verbatim from moving_node_second_order_probe.py (CXLIII); band
machinery verbatim from band_arithmetic_anatomy_probe.py (round
62); beta from case_edge_christoffel_probe (= v902 chain).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/shat_band_organization_probe.py
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

KZMAX = 150
MIN_RUNGS = 40
DELTA = 1e-2
SHAT_MIN_REF = 0.502
SHAT_MED_REF = 1.027
SHAT_MAX_REF = 2.185
N_BAND_RUNGS = 42
MIN_COMMON = 30
R2_ORG = 0.50
R2_PART = 0.25
H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
CTRL_KZ = 9
NG_SMOOTH = 6000
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


def r2_multi(X, y):
    """OLS R^2 of y on columns of X (with intercept)."""
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    A = np.column_stack([np.ones(len(y))] + [X[:, j] for j in
                                             range(X.shape[1])])
    coef, _res, _rk, _sv = np.linalg.lstsq(A, y, rcond=None)
    fit = A @ coef
    ss = float(np.sum((y - fit) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return 1.0 - ss / st if st > 0 else float("nan")


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


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


# ---------------- band machinery (band_arithmetic verbatim, trim)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def band_objects(kz):
    """One Gram rung -> E_band, m_band, wshare, n90, beta."""
    rr = window_of(kz)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    L = 2 * M - 2
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    xs, ws, _ufp = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    ff = np.arange(1, L // 2)
    xf = np.cos(2.0 * math.pi * ff / L)
    band = ff[(xf > 1.0 - DELTA)]
    bandneg = band[d[band] < 0.0]
    qf = (2.0 * 4.0 * np.sin(math.pi * bandneg / L) ** 2
          / (2.0 * L))
    m_band = float(np.sum(-d[bandneg] * qf))
    hm = h - 1
    Px = eval_chain(al, be, m0, xs, h)
    Pn = eval_chain(al, be, m0, ys, h)
    Mm = ((Px[:, :hm] * (ws * (1.0 - xs))[:, None]).T
          @ Px[:, :hm]
          - (Pn[:, :hm] * (vs * (1.0 - ys))[:, None]).T
          @ Pn[:, :hm])
    Mm = 0.5 * (Mm + Mm.T)
    _wm, Vm = np.linalg.eigh(Mm)
    e = Vm[:, 0]
    qn = Pn[:, :hm] @ e
    cn = vs * (1.0 - ys) * qn ** 2
    cn_tot = float(np.sum(cn))
    wshare = (float(np.sum(cn[ys > 1.0 - DELTA]))
              / max(cn_tot, 1e-300))
    qx = eval_chain(al, be, m0, np.cos(
        2.0 * math.pi * bandneg / L), h)[:, :hm] @ e
    wf = (1.0 - np.cos(2.0 * math.pi * bandneg / L)) * qx ** 2
    E_band = float(np.sum(-d[bandneg] * qf * wf))
    # n90 census concentration (WGT read)
    g = np.zeros(M)
    if len(bandneg):
        ffb = bandneg.astype(float)
        qfw = qf * wf
        kk = np.arange(M)
        fac = 2.0 * np.cos(2.0 * math.pi
                           * np.outer(ffb, kk) / L)
        fac[:, 0] = 1.0
        fac[:, M - 1] = np.where(np.mod(ffb, 2.0) == 0.0, 1.0,
                                 -1.0)
        g = -(qfw[:, None] * fac).sum(axis=0)
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    gi0 = np.where((i0 >= 0) & (i0 < M),
                   g[np.clip(i0, 0, M - 1)], 0.0)
    gi1 = np.where((i0 + 1 >= 0) & (i0 + 1 < M),
                   g[np.clip(i0 + 1, 0, M - 1)], 0.0)
    contrib = -mm * 0.5 * ((1.0 - fr) * gi0 + fr * gi1)
    contrib = contrib + np.where(uu < D, -mm * 0.5
                                 * (1.0 - uu / D) * g[0], 0.0)
    srt = np.sort(np.abs(contrib))[::-1]
    csum = np.cumsum(srt)
    n90 = int(np.searchsorted(
        csum, 0.90 * float(np.sum(np.abs(contrib))))) + 1
    # beta (full-window only)
    beta = float("nan")
    idx = {int(j): k for k, j in enumerate(uf_n)}
    if all(j in idx for j in JWIN):
        G = (Pn * vs[:, None]).T @ Pn
        G = 0.5 * (G + G.T)
        jstar = idx[JWIN[-1]]
        p = Pn[jstar]
        try:
            q = np.linalg.solve(np.eye(h) - G, p)
            beta = float(vs[jstar]) * float(q @ (G @ q))
        except np.linalg.LinAlgError:
            pass
    return dict(kz=kz, h=h, alpha=float(alpha), E_band=E_band,
                m_band=m_band, wshare=wshare, n90=n90, beta=beta)


def main():
    section("PRIME.PORT.SHAT.BAND.01 -- does the band organize "
            "shat = m_h/mu1(h)?  (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  REPARAM-DECLARED: "
          "shat is the wall margin renormalized; a regression "
          "organizes scatter, it certifies nothing.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the two ladders + reproduction")
    rungs = []
    for kz in range(2, KZMAX + 1):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        c_at = np.asarray(core.atom_lags_at(alpha, M, uu,
                                            mu)[0], float)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        Kt = core.odd_toeplitz(c_ar + c_at, M)
        w = np.linalg.eigvalsh(Kt)
        ug, mg = smooth_comb(alpha)
        c_sm = np.asarray(core.atom_lags_at(alpha, M, ug,
                                            mg)[0], float)
        lam_sm = float(np.linalg.eigvalsh(
            core.odd_toeplitz(c_ar + c_sm, M))[0])
        rungs.append(dict(kz=kz, alpha=float(alpha), h=h,
                          m=float(w[0]), mu1=mu1_of(h),
                          lam_sm=lam_sm))
        del Kt
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    ms = np.array([r["m"] for r in rungs])
    check("W2 WARD truth margin m_h > 0 everywhere (min %.3e)"
          % float(ms.min()), bool(np.all(ms > 0)), kill="K2")
    shat = np.array([r["m"] / r["mu1"] for r in rungs])
    ok_rep = (abs(float(np.min(shat)) / SHAT_MIN_REF - 1.0)
              <= 2e-2
              and abs(float(np.median(shat)) / SHAT_MED_REF
                      - 1.0) <= 5e-2
              and abs(float(np.max(shat)) / SHAT_MAX_REF - 1.0)
              <= 2e-2)
    check("W3 REPRODUCTION CXLIII shat min/med/max "
          "%.3f/%.3f/%.3f == %.3f/%.3f/%.3f"
          % (float(np.min(shat)), float(np.median(shat)),
             float(np.max(shat)), SHAT_MIN_REF, SHAT_MED_REF,
             SHAT_MAX_REF), ok_rep, kill="K2")
    band = {}
    for kz in core.frame_a_zones():
        b = band_objects(kz)
        if isinstance(b, dict):
            band[kz] = b
    check("W4 band ladder == %d rungs" % N_BAND_RUNGS,
          len(band) == N_BAND_RUNGS, "%d" % len(band), kill="K1")
    common = [r for r in rungs if r["kz"] in band]
    check("W5 common kz >= %d" % MIN_COMMON,
          len(common) >= MIN_COMMON,
          "%d common rungs (%d with beta)  [%.1f s]"
          % (len(common),
             sum(1 for r in common
                 if np.isfinite(band[r["kz"]]["beta"])),
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E1
    section("E1 -- the regression table (honest R^2, common "
            "subset)")
    y = np.array([r["m"] / r["mu1"] for r in common])
    cols = {
        "log E_band": np.array([band[r["kz"]]["E_band"]
                                for r in common]),
        "log m_band": np.array([band[r["kz"]]["m_band"]
                                for r in common]),
        "wshare": np.array([band[r["kz"]]["wshare"]
                            for r in common]),
        "log n90": np.array([band[r["kz"]]["n90"]
                             for r in common], float),
        "log beta": np.array([band[r["kz"]]["beta"]
                              for r in common]),
    }
    base = {
        "alpha": np.array([r["alpha"] for r in common]),
        "log h": np.log(np.array([r["h"] for r in common],
                                 float)),
    }
    r2 = {}
    for name, v in cols.items():
        if name.startswith("log"):
            msk = np.isfinite(v) & (v > 0)
            x = np.log(v[msk])
            yy = y[msk]
        else:
            msk = np.isfinite(v)
            x, yy = v[msk], y[msk]
        r2[name] = (r2_multi(x[:, None], yy), int(np.sum(msk)))
    for name, v in base.items():
        r2[name] = (r2_multi(v[:, None], y), len(y))
    # pairs
    lh = base["log h"]
    for pname, (v1, v2) in (
            ("(log E_band, log h)", (cols["log E_band"], lh)),
            ("(log beta, log h)", (cols["log beta"], lh)),
            ("(wshare, alpha)", (cols["wshare"],
                                 base["alpha"]))):
        va = v1
        if pname.startswith("(log"):
            msk = np.isfinite(va) & (va > 0)
            xa = np.log(va[msk])
        else:
            msk = np.isfinite(va)
            xa = va[msk]
        xb = np.asarray(v2, float)[msk]
        r2[pname] = (r2_multi(np.column_stack([xa, xb]),
                              y[msk]), int(np.sum(msk)))
    for name in sorted(r2, key=lambda k: -r2[k][0]):
        print("    R^2(shat ~ %-22s) = %.3f  (n = %d)"
              % (name, r2[name][0], r2[name][1]), flush=True)
    band_names = [k for k in r2 if "band" in k or "beta" in k
                  or "wshare" in k or "n90" in k]
    best_name = max(band_names, key=lambda k: r2[k][0])
    best = r2[best_name][0]
    lab = ("BAND-ORGANIZES(%.3f, %s)" % (best, best_name)
           if best >= R2_ORG
           else "BAND-PARTIAL(%.3f, %s)" % (best, best_name)
           if best >= R2_PART
           else "BAND-DEAD(best %.3f at %s)" % (best, best_name))
    print("    CXLIII comparison on this subset: alpha %.3f, "
          "log h %.3f (declared: 0.003 / 0.027 ladder-wide)"
          % (r2["alpha"][0], r2["log h"][0]), flush=True)
    check("E1 typed: %s" % lab, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    n_neg = sum(1 for r in rungs if r["lam_sm"] < 0.0)
    check("C1 WARD smooth world shat_sm < 0 on %d/%d rungs"
          % (n_neg, len(rungs)), n_neg == len(rungs), kill="K2")
    rr9 = window_of(CTRL_KZ)
    alpha9, M9, D9 = rr9["alpha"], rr9["M"], rr9["D"]
    N_E = int(math.floor(math.exp(2.0 * alpha9))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    cE = np.asarray(core.atom_lags_at(
        alpha9, M9, np.log(nn.astype(float)),
        2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))[0], float)
    c_ar9 = np.asarray(core.arch_lags(M9, D9), float)
    lamE = float(np.linalg.eigvalsh(
        core.odd_toeplitz(c_ar9 + cE, M9))[0])
    rs = window_of(CTRL_KZ, scramble_seed=1)
    cS = np.asarray(core.atom_lags_at(
        alpha9, M9, rs["uu"], 2.0 * rs["lam"])[0], float)
    lamS = float(np.linalg.eigvalsh(
        core.odd_toeplitz(c_ar9 + cS, M9))[0])
    check("C2 WARD Epstein (%.2e) + scramble (%.2e) fire "
          "(lam_min < 0)" % (lamE, lamS),
          lamE < 0.0 and lamS < 0.0, kill="K2")

    return finish({"e1": lab})


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("SHATBAND-MEASURED / %s"
                   % labels.get("e1", "-"))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): REPARAM-DECLARED -- shat is the wall
  margin renormalized; the regression table is scatter anatomy,
  never a floor and never a law.  NO RH claim.  No marker
  moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
