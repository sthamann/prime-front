#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""moving_node_second_order_probe -- PRIME.PORT.GAP.NORMALIZATION.01
(EXPLORATION ONLY, experiments/; round 61, theorem-engineering on
the RH-side wall: the GEOMETRIC normalization of the wall margin --
mu1(h) = 4 sin^2(pi/(2h+1)), the spectral gap of the compressed
second difference (~ pi^2/h^2), and shat_h = m_h / mu1(h):
sign-free, geometric, tau_{h+1}-independent.  Is the normalized
margin an O(1) FLAT band, is it organized by the WANDERING NODE,
and is its infimum stable at depth?  2026-08-10.)

DECLARED OPENLY, FIRST (the tau-screen formality, frozen): shat is
the WALL MARGIN REPARAMETRIZED -- m_h divided by a source-only
geometric gap.  This probe makes NO new-floor claim of any kind:
its content is whether the normalized object is FLAT and
NODE-ORGANIZED (which would make the tail statement 'shat >= c0 >
0' WELL-POSED as a theorem shape), not that anything is proven.
The screens below document flatness; a flat shat while tau spans
decades is exactly the h^-2 margin law restated -- said plainly in
every reading.

THE NORMALIZATION (frozen).  mu1(h) = 4 sin^2(pi / (2h + 1)) is
the smallest parity-geometry eigenvalue of the deployed KMS/
Dirichlet second-difference compression -- literally
core.parity_mu(h)[0] (warded exactly on the subset): a pure
geometry number, no sign information, no tau_{h+1}.  Along the
critical direction v_h the pair (n_h, q_h) of the Schur split
collapses exactly (K v = m v => the inflow column vanishes => q =
0, n = m; warded on the subset), so shat_h = (n_h - q_h)/mu1(h) =
m_h/mu1(h) on this surface.  The matched-asymptotics transfer
(round 59: C_h = m_h h^2 in [4.95, 21.5], flat in alpha) predicts
shat ~ C_h/pi^2 in [~0.50, ~2.18] up to the h^2 mu1/pi^2 -> 1
correction -- the frozen prediction window; the generous typing
belt is BAND = [0.40, 2.50].

THE FOUR QUESTIONS (frozen; typed, never kill):
 (1) BAND: min/med/max of shat over the 67-rung ladder; typed
     BAND-IN(min, max) iff all shat in [0.40, 2.50] (prediction
     window printed next to it), else BAND-OUT(count).
 (2) NODE ORGANIZATION: OLS R^2 of shat against four regressors:
     (i) the MEASURED per-rung node u*_h/alpha (robust_node of
     v_h; NaN excluded and counted -- carries arithmetic scatter,
     the live candidate), (ii) the declared prime-free node LAW
     n*(alpha) = 0.3727 - 0.0116 alpha, (iii) alpha, (iv) log h.
     DISCLOSED A PRIORI: (ii) and (iii) are affine-equivalent, so
     their R^2 are IDENTICAL by construction -- the honest
     comparison is (i) vs (iii) vs (iv).  TYPED:
     NODE-ORGANIZED(R^2_node) iff R^2 of the measured node
     exceeds both competitors by >= 0.10; else
     NODE-NOT-BEST(R^2 list).
 (3) THE INFIMUM: c0 = min shat; alpha-tercile minima (t1, t2,
     t3); jackknife slope of shat vs alpha.  TYPED: INF-ERODING
     iff t3 < t1 and slope + 2SE < 0; INF-RISING iff t3 > t1 and
     slope - 2SE > 0; else INF-FLAT(c0, t1/t2/t3, slope +- 2SE).
 (4) SCREENS (documentation of flatness, NOT a floor): log shat
     vs log m_h slope (a REPARAMETRIZATION reads ~ 0 exactly when
     the margin exponent is ~ -2 -- the flatness statement); log
     shat vs log h slope (= p_margin + 2 + o(1), the residual
     exponent of the h^-2 law); both printed with R^2.

FROZEN PROTOCOL:

 W   LADDER + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): faithful rungs (race verbatim, KZMAX 150); W1
     >= MIN_RUNGS = 40; W2 WARD m_h > 0 everywhere; W3 WARD mu1
     closed form == core.parity_mu(h)[0] to MU_WARD relative on
     the SUBSET (the deployed-geometry tie); W4 WARD the pivot
     collapse on the SUBSET: |K v - m v| / spectral scale <=
     RES_WARD (=> n - q = m along v, the shat definition is the
     margin); W5 REPRODUCTION margin exponent p in [-2.5, -1.5]
     (race band).

 N   THE FOUR TYPED ANSWERS as frozen above.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C1 smooth world:
     shat_sm = lam_sm/mu1 < 0 on EVERY rung (positivity and
     flatness destroyed -- v883 regression); C2 Epstein x^2+5y^2
     comb + scramble (seed 1) at kz 9 fire (lam_min < 0 => shat
     < 0); C3 AST firewall; C4 NO-RH-CLAIM.

KILLS: K1 (W1) -> PIPELINE-BROKEN; K2 (W2-W5, C1-C3) ->
WARD-BROKEN.  N-typed outcomes are measurements, never kills.

VERDICT (frozen enum): GAPNORM-MEASURED with typed sublabels
REPARAM-DECLARED, BAND-IN/OUT, NODE-ORGANIZED/NODE-NOT-BEST,
INF-FLAT/RISING/ERODING, SHAT-SCREENS(slopes); else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; SUBSET = (9, 13, 26,
40, 60, 90, 121) intersected with the faithful ladder; BAND =
[0.40, 2.50]; PRED = [0.50, 2.18]; NODE_C = 0.3727, NODE_S =
-0.0116 (node_origin declared input); DR2_BAR = 0.10; MU_WARD =
1e-12; RES_WARD = 1e-9; EXPO_BAND = [-2.5, -1.5]; CTRL_KZ = 9;
scramble seed 1; jackknife = leave-one-out; terciles = equal
thirds of the alpha-sorted ladder.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign as input, no factorization of the target matrix; mu1
is pure geometry; m_h and v_h are measured outcomes of the
deployed wall, used as measurements only.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (12/12 with the identical bars; NO bar, band,
count, rule or enum was moved after it) measured, recorded as the
honest context the frozen run must confirm: 67 faithful rungs
(h 142..1433, 17.0 s); wards exact (mu1 tie 0.0, pivot collapse
4.3e-16, margin exponent -1.934).  (1) BAND-IN: shat in [0.502,
2.185] (med 1.027) -- INSIDE the belt [0.40, 2.50], and exactly
ONE rung sits 0.005 above the matched-asymptotics prediction top
2.18 (the h^2 mu1/pi^2 correction explains it; printed) -- the
normalized margin IS an O(1) band on the measured ladder, and
its edges [0.502, 2.185] REPRODUCE C_h/pi^2 = [0.502, 2.18]
almost exactly.  (2) NODE-NOT-BEST -- the a priori hope of node
organization is DEAD on this ladder: R^2 = 0.000 (measured node,
0 NaN), 0.003 (node law) = 0.003 (alpha, affine-identical as
disclosed), 0.027 (log h) -- NO single-variable organization at
all: shat is a pure arithmetic-scatter band, not a function of
the node, of alpha, or of depth.  (3) INF-FLAT: c0 = 0.502;
tercile minima 0.526 / 0.642 / 0.502 (the global minimum sits in
the DEEPEST tercile but the tercile minima are non-monotone;
slope -0.023 +- 2SE 0.105, CI contains 0 -- no measurable
erosion and no measurable rise).  (4) SCREENS: log shat vs log m
slope +0.022 (R^2 0.009 -- decorrelated flatness, exactly the
reparametrization statement); log shat vs log h slope +0.064
(R^2 0.019, = p + 2 within errors).  Controls: shat_sm < 0 on
67/67 (min -2.7e+05 x the truth band), Epstein -1.0e+01 and
scramble -7.9e+00 fire.  Fail-first preserved: nothing was
weakened; all four answers live in typed measurements.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
race ladder verbatim; ONE eigh per rung (margin + critical
vector); (ii) robust_node verbatim from the race probe; (iii)
mu1 closed form 4 sin^2(pi/(2h+1)); parity tie via
core.parity_mu(h)[0]; (iv) OLS population statistics +
leave-one-out jackknife as the matched-asymptotics probe.

NO RH claim: shat >= c0 on the measured ladder is the wall census
restated in geometric units; the typed content is band shape,
organization and depth trend of the infimum -- a theorem SHAPE
statement ('shat >= c0 is well-posed'), never a theorem.  No
marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (incl. parity_mu = the
KMS/Dirichlet parity geometry); race machinery verbatim from
arithmetic_lift_race_probe.py / wall_matched_asymptotics_probe.py
(C_h band = declared input); node law from node_origin_arch_probe
(declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/moving_node_second_order_probe.py
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
SUBSET = (9, 13, 26, 40, 60, 90, 121)
BAND = (0.40, 2.50)
PRED = (0.50, 2.18)
NODE_C = 0.3727
NODE_S = -0.0116
DR2_BAR = 0.10
MU_WARD = 1e-12
RES_WARD = 1e-9
EXPO_BAND = (-2.5, -1.5)
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


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_fit(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        _ai, bi, _ = ols_line(x[m], y[m])
        bb.append(bi)
    bb = np.array(bb)
    se_b = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                                ** 2)))
    return a, b, r2, se_b


def robust_node(vec, D, alpha):
    v = vec * np.sign(vec[int(np.argmax(np.abs(vec)))])
    ip = int(np.argmax(v))
    im = int(np.argmin(v))
    if v[im] >= -0.02 * v[ip]:
        return float("nan")
    lo, hi = (im, ip) if im < ip else (ip, im)
    seg = v[lo:hi + 1]
    idx = np.where(np.diff(np.sign(seg)) != 0)[0]
    if len(idx) == 0:
        return float("nan")
    i = lo + (int(idx[0]) if im < ip else int(idx[-1]))
    t = v[i] / (v[i] - v[i + 1])
    return (i + t) * D / alpha


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


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def main():
    section("PRIME.PORT.GAP.NORMALIZATION.01 -- shat = m_h/mu1(h): "
            "the geometric normalization of the wall margin "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  REPARAM-DECLARED: "
          "shat is the wall margin renormalized -- no new floor "
          "is claimed anywhere in this probe.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (C3)", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder + wards")
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
        c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0],
                          float)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        Kt = core.odd_toeplitz(c_ar + c_at, M)
        w, V = np.linalg.eigh(Kt)
        v = V[:, 0]
        row = dict(kz=kz, alpha=float(alpha), h=h, m=float(w[0]),
                   mu1=mu1_of(h), node=robust_node(v, D, alpha))
        if kz in SUBSET:
            res = float(np.linalg.norm(Kt @ v - w[0] * v)) \
                / max(float(np.max(np.abs(w))), 1.0)
            row["pivres"] = res
            row["mu1_tie"] = abs(row["mu1"]
                                 - float(core.parity_mu(h)[0])) \
                / row["mu1"]
        # smooth world value (control): lam_min of the smooth wall
        ug, mg = smooth_comb(alpha)
        c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0],
                          float)
        row["lam_sm"] = float(np.linalg.eigvalsh(
            core.odd_toeplitz(c_ar + c_sm, M))[0])
        rungs.append(row)
        del Kt, V
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
    sub = [r for r in rungs if "pivres" in r]
    tie = max(r["mu1_tie"] for r in sub)
    check("W3 WARD mu1 closed form == core.parity_mu(h)[0] on the "
          "subset: max rel dev %.2e <= %.0e (the deployed "
          "KMS/Dirichlet parity-geometry tie)" % (tie, MU_WARD),
          tie <= MU_WARD, kill="K2")
    pres = max(r["pivres"] for r in sub)
    check("W4 WARD pivot collapse |K v - m v|/scale %.2e <= %.0e "
          "on the subset => q = 0, n = m along v: shat = "
          "(n - q)/mu1 = m/mu1 on this surface"
          % (pres, RES_WARD), pres <= RES_WARD, kill="K2")
    hh = np.array([float(r["h"]) for r in rungs])
    als = np.array([r["alpha"] for r in rungs])
    _a, p_exp, _r2, _se = jack_fit(np.log(hh), np.log(ms))
    check("W5 REPRODUCTION margin exponent p = %+.3f in [%.1f, "
          "%.1f]" % (p_exp, EXPO_BAND[0], EXPO_BAND[1]),
          EXPO_BAND[0] <= p_exp <= EXPO_BAND[1], kill="K2")

    # ------------------------------------------------------------ N
    section("N -- the four typed answers")
    shat = ms / np.array([r["mu1"] for r in rungs])
    print("      kz    h    alpha    m_h        mu1(h)     shat")
    for r, s in list(zip(rungs, shat))[:4] + \
            list(zip(rungs, shat))[-4:]:
        print("    %4d %5d  %6.3f  %.3e  %.3e  %7.4f"
              % (r["kz"], r["h"], r["alpha"], r["m"], r["mu1"],
                 s))
    n_out = int(np.sum((shat < BAND[0]) | (shat > BAND[1])))
    n_pred = int(np.sum((shat < PRED[0]) | (shat > PRED[1])))
    print("    shat: min %.3f, med %.3f, max %.3f; outside belt "
          "[%.2f, %.2f]: %d; outside the matched-asymptotics "
          "prediction [%.2f, %.2f]: %d"
          % (float(shat.min()), float(np.median(shat)),
             float(shat.max()), BAND[0], BAND[1], n_out,
             PRED[0], PRED[1], n_pred))
    n1 = ("BAND-IN(%.3f..%.3f)" % (float(shat.min()),
                                   float(shat.max()))
          if n_out == 0 else "BAND-OUT(%d)" % n_out)
    check("N1 typed: %s -- the normalized margin is an O(1) band "
          "iff no rung leaves the belt" % n1, True)

    nodes = np.array([r["node"] for r in rungs])
    okn = np.isfinite(nodes)
    _a1, _b1, r2_node = ols_line(nodes[okn], shat[okn])
    law = NODE_C + NODE_S * als
    _a2, _b2, r2_law = ols_line(law, shat)
    _a3, _b3, r2_al = ols_line(als, shat)
    _a4, _b4, r2_lh = ols_line(np.log(hh), shat)
    print("    R^2 of shat vs: measured node %.3f (%d NaN "
          "excluded), node law %.3f, alpha %.3f "
          "(law/alpha affine-identical, disclosed), log h %.3f"
          % (r2_node, int(np.sum(~okn)), r2_law, r2_al, r2_lh))
    if r2_node >= max(r2_al, r2_lh) + DR2_BAR:
        n2 = "NODE-ORGANIZED(R2=%.3f)" % r2_node
    else:
        n2 = ("NODE-NOT-BEST(node=%.3f, alpha=%.3f, logh=%.3f)"
              % (r2_node, r2_al, r2_lh))
    check("N2 typed: %s (bar: node must beat both competitors by "
          ">= %.2f)" % (n2, DR2_BAR), True)

    order = np.argsort(als)
    thirds = np.array_split(order, 3)
    tmins = [float(np.min(shat[t])) for t in thirds]
    _a5, sl_a, _r5, se_a = jack_fit(als, shat)
    c0 = float(shat.min())
    if tmins[2] < tmins[0] and sl_a + 2 * se_a < 0:
        n3 = "INF-ERODING(c0=%.3f, t=%.3f/%.3f/%.3f)" % (
            c0, *tmins)
    elif tmins[2] > tmins[0] and sl_a - 2 * se_a > 0:
        n3 = "INF-RISING(c0=%.3f, t=%.3f/%.3f/%.3f)" % (c0, *tmins)
    else:
        n3 = ("INF-FLAT(c0=%.3f, t=%.3f/%.3f/%.3f, slope=%+.3f"
              "+-%.3f)" % (c0, tmins[0], tmins[1], tmins[2],
                           sl_a, 2 * se_a))
    check("N3 typed: %s -- the candidate tail constant and its "
          "depth trend" % n3, True)

    _a6, sl_m, r2_m = ols_line(np.log(ms), np.log(shat))
    _a7, sl_h, r2_h = ols_line(np.log(hh), np.log(shat))
    print("    screens: log shat vs log m slope %+.4f (R^2 %.3f); "
          "log shat vs log h slope %+.4f (R^2 %.3f) = p + 2 "
          "within errors" % (sl_m, r2_m, sl_h, r2_h))
    n4 = ("SHAT-SCREENS(vs-m=%+.3f, vs-h=%+.3f)" % (sl_m, sl_h))
    check("N4 typed: REPARAM-DECLARED + %s -- flatness "
          "documentation, NOT a floor claim" % n4, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    shat_sm = np.array([r["lam_sm"] for r in rungs]) \
        / np.array([r["mu1"] for r in rungs])
    check("C1 WARD smooth world destroys the band: shat_sm < 0 on "
          "%d/%d rungs (min %.1e)"
          % (int(np.sum(shat_sm < 0)), len(rungs),
             float(shat_sm.min())),
          bool(np.all(shat_sm < 0)), kill="K2")
    rr9 = core.build_window(CTRL_KZ)
    alpha9, M9, D9 = rr9["alpha"], rr9["M"], rr9["D"]
    c_ar9 = np.asarray(core.arch_lags(M9, D9), float)
    N_E = int(math.floor(math.exp(2.0 * alpha9))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    c_E = np.asarray(core.atom_lags_at(
        alpha9, M9, np.log(nn.astype(float)),
        2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))[0], float)
    rr_s = core.build_window(CTRL_KZ, scramble_seed=1)
    c_s = np.asarray(core.atom_lags_at(
        rr_s["alpha"], rr_s["M"], np.asarray(rr_s["uu"], float),
        2.0 * np.asarray(rr_s["lam"], float))[0], float)
    fired = True
    for name, c_c in (("Epstein", c_E), ("scramble", c_s)):
        lam_c = float(np.linalg.eigvalsh(core.odd_toeplitz(
            c_ar9 + c_c, M9))[0])
        fired &= lam_c < 0
        print("    %-9s: lam_min %+.3e -> %s (shat_ctrl < 0)"
              % (name, lam_c, "FIRES" if lam_c < 0 else "SILENT"))
    check("C2 WARD both controls fire", fired, kill="K2")

    return finish(dict(n1=n1, n2=n2, n3=n3, n4=n4))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("GAPNORM-MEASURED / REPARAM-DECLARED / %(n1)s "
                   "/ %(n2)s / %(n3)s / %(n4)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): shat is the wall margin divided by a
  source-only geometric gap -- a REPARAMETRIZATION of the open
  statement, declared as such; the typed content is whether the
  normalized object is an O(1) band, whether the wandering node
  organizes it, and whether its infimum erodes at depth.  A flat,
  well-banded shat makes the tail statement 'shat >= c0 > 0'
  well-posed as a theorem SHAPE -- nothing here proves it.  NO RH
  claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
