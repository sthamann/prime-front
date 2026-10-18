#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wall_matched_asymptotics_probe -- PRIME.PORT.MATCHED.ASYMPTOTICS.01
(EXPLORATION ONLY, experiments/; round 59, theorem-engineering on the
RH-side wall: expand the hub (arithmetic lift) and the demand around
the wandering classical node x*(alpha), verify the H0 cancellation,
and measure the h^-2 coefficient difference H2 - D2 with honest
error bars.  2026-08-10.)

THE SURFACE (frozen, declared).  This probe lives on the LIFT-RACE
surface (arithmetic_lift_race_probe = E8.WALL.LIFTRACE.01): the odd
Toeplitz wall K = odd_toeplitz(c_ar + c_at, M) with margin m_h =
lam_min(K) along the true critical direction v_h, where the EXACT
bookkeeping identity holds:
    lift_h - demand_h = v_h^T K v_h = m_h            [BOOKKEEPING]
    lift_h   = E_at_true(v) - E_at_smooth(v)   (the arithmetic HUB),
    demand_h = -(E_ar(v) + E_at_smooth(v))     (the geometric DEMAND),
all through the T163 lag reads E = c . W(v).  This is the surface
where the h^-2 margin language lives (race probe: both legs ~ 0.077
alpha + 0.81, margin residual exponent in [-2.5, -1.5]); the folded
Jacobi/Gram tau of probes 1-3 is a DIFFERENT surface with its own
exponent (~ -3.1) and is not used here.

THE MATCHED-ASYMPTOTICS READING (frozen).  Around the wandering
classical node u*(alpha)/alpha = NODE_C + NODE_S alpha (the
prime-free drift law; its reproduction on THIS ladder is typed in
A4), the hub and the demand share the SAME leading expansion
    hub    = H0(alpha) + H2(alpha) h^-2 + ...,
    demand = H0(alpha) + D2(alpha) h^-2 + ...,
and the wall margin is the difference: m_h = (H2 - D2)(alpha) h^-2 +
...  The H0 CANCELLATION is not a fit claim -- it is the exact
bookkeeping identity above (the O(alpha) + O(1) parts cancel to the
level of the margin itself, warded per rung); the FITTED statement
(both legs have the same affine alpha-growth, slope difference ~ 0)
is its measured shadow.  The TARGET measurement is the leading
coefficient
    C_h := m_h h^2   (the direct, per-rung, fit-free H2 - D2 readout)
and the two questions: (i) is C(alpha) >= c0 > 0 with STABLE SIGN
(honest error bars: deterministic leave-one-out jackknife on the
fits -- no RNG outside controls); (ii) are H2(alpha) and D2(alpha)
SEPARATELY extractable, i.e. do the per-leg residuals after the
common affine alpha-model resolve at the h^-2 scale, or is only the
difference measurable?  Both typed, never killed.

FROZEN PROTOCOL:

 W   THE LADDER + RACE REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): faithful rungs = kz in 2..KZMAX with H_MIN <= h
     <= HCAP and X <= ATOM_MAX (race verbatim); W1 >= MIN_RUNGS =
     40 rungs; W2 WARD truth margin m_h > 0 on every faithful rung;
     W3 WARD EXACT BOOKKEEPING |(lift - demand) - m_h| <= RQ_WARD x
     max(1, |m_h|) on every rung; W4 REPRODUCTION of the race
     ledger: affine fits lift = bL alpha + aL, demand = bD alpha +
     aD with bL, bD == 0.077 (rtol 20%), |bL - bD| <= 0.005, and
     the margin exponent p = slope(log m vs log h) in [-2.5, -1.5]
     (race bands); W5 REPRODUCTION demand(v_sm) = -lam_min(K_smooth)
     to RQ_WARD on the frozen SUBSET (the smooth model's ground
     level is its own demand).

 A1  H0 -- THE CANCELLATION (exact + fitted): the bookkeeping ward
     is W3 (exact, per rung); measured here: the cancellation depth
     m_h / (|lift| + |demand|) ladder (how deep the two legs
     cancel), the fitted slope difference bL - bD with jackknife
     error bars.  TYPED: H0-CANCELS(depth, dslope +- 2SE) iff the
     jackknife CI of bL - bD contains 0 or |bL - bD| <= 0.005; else
     H0-RESIDUAL-GROWTH(dslope +- 2SE) (a nonzero leg-growth
     difference would feed the margin at O(alpha), not h^-2).

 A2  H2 - D2 -- THE LEADING COEFFICIENT (the decisive measurement):
     C_h = m_h h^2 ladder (fit-free); exponent p with jackknife CI;
     affine trend C = cA + cB alpha with jackknife SEs; the
     deep-end prediction C(alpha_max) with 2SE.  TYPED:
     H2D2-POSITIVE-STABLE(c0 = min C_h) iff min C_h > 0 AND
     C(alpha_max) - 2SE > 0 AND p CI inside [-2.8, -1.2];
     H2D2-POSITIVE-FRAGILE iff min C_h > 0 but a stability leg
     fails; else H2D2-SIGN-UNSTABLE(count C_h <= 0).  (The
     h^-2 normalization is FROZEN by the spec question even if the
     measured exponent p deviates from -2 -- p is reported next to
     it; a p far from -2 makes C(alpha) drift systematically and is
     part of the FRAGILE/STABLE typing through the CI leg.)

 A3  H2 AND D2 SEPARATELY (typed): per-leg residuals rL, rD after
     the affine alpha-fits, at the h^-2 scale: ratios med(|rL| h^2)
     / med(C) and med(|rD| h^2) / med(C).  TYPED: LEGS-SEPARABLE
     iff both ratios <= 0.5 (the per-leg h^-2 coefficients resolve
     above fit noise); else LEGS-NOT-SEPARABLE(ratios) -- only the
     DIFFERENCE H2 - D2 is measurable on this ladder (honest
     negative for the separate-extraction program).

 A4  THE WANDERING NODE (typed reproduction): robust_node(v_h) per
     rung (race machinery), affine fit node/alpha = c + s alpha;
     TYPED NODE-DRIFT-REPRO(c, s) iff |c - NODE_C| <= 0.05 and |s -
     NODE_S| <= 0.008 on the fit (node_origin drift law reproduced
     on this ladder); else NODE-DRIFT-SHIFTED(c, s); NaN-node count
     printed.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C1 Epstein x^2+5y^2
     comb at kz 9 on THIS surface: lam_min(K_E) < 0 fires; C2
     scramble (seed 1) at kz 9: lam_min < 0 fires.

KILLS: K1 ladder too small (W1) -> PIPELINE-BROKEN; K2 wards
(W2/W3/W4/W5, C1/C2) -> WARD-BROKEN.  A1-A4 typed outcomes are
measurements, never kills.

VERDICT (frozen enum): MATCHED-ASY-MEASURED with typed sublabels
H0-CANCELS/H0-RESIDUAL-GROWTH, EXPO(p +- 2SE),
H2D2-POSITIVE-STABLE/H2D2-POSITIVE-FRAGILE/H2D2-SIGN-UNSTABLE,
LEGS-SEPARABLE/LEGS-NOT-SEPARABLE, NODE-DRIFT-REPRO/SHIFTED; else
PIPELINE-BROKEN / WARD-BROKEN.  PROBE-5 GATE (frozen): probe 5
(head/tail split) runs ONLY on H2D2-POSITIVE-STABLE.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; SUBSET = (9, 13, 26, 40,
60, 90, 121); RQ_WARD = 1e-10; SLOPE_REF = 0.077 (rtol 0.20);
DSLOPE_BAR = 0.005; EXPO_BAND = [-2.5, -1.5] (ward), EXPO_CI_BAND =
[-2.8, -1.2] (typing); SEP_BAR = 0.5; NODE_C = 0.3727, NODE_S =
-0.0116 (declared input), NODE_CTOL = 0.05, NODE_STOL = 0.008;
NG_SMOOTH = 6000; CTRL_KZ = 9; scramble seed 1; jackknife = full
leave-one-out, SE = sqrt((N-1)/N sum (th_i - mean)^2), CI = +- 2SE.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run of
this script (11/11 with the identical bars; NO bar, band, count,
rule or enum was moved after it) measured, recorded as the honest
context the frozen run must confirm: 67 faithful rungs (h 142..
1433, alpha 2.77..6.30); bookkeeping exact to 4.6e-15; race ledger
reproduced (bL = 0.0769, bD = 0.0770, R^2 0.888/0.888, |bL - bD| =
9.2e-05, exponent p = -1.934); H0-CANCELS (cancellation depth med
1.3e-05, dslope -9.2e-05 +- 2SE 1.4e-02 -- the CI contains 0); THE
LEADING COEFFICIENT IS POSITIVE AND STABLE: C_h = m_h h^2 > 0 on
67/67 with min 4.954, med 10.13, max 21.5, and the alpha-trend is
FLAT (C = 11.54 - 0.21 alpha, R^2 0.003 -- no systematic drift;
deep-end C(6.30) = 10.2 +- 2SE 8.2, positive; exponent CI -1.934 +-
0.127 inside [-2.8, -1.2]) -> H2D2-POSITIVE-STABLE(c0 = 4.954), the
PROBE-5 GATE IS OPEN; the legs are NOT separately extractable (med
|rL| h^2 / med C = 5.5e+02 for BOTH legs: the per-leg fit residuals
sit ~550x above the h^-2 scale -- only the DIFFERENCE H2 - D2 is
measurable, honest negative for the separate-extraction program);
the node drift is SHIFTED on this ladder (fit c = 0.4410, s =
-0.0166, R^2 0.162, 0 NaN -- the robust_node fit here is noisier
than node_origin's dedicated measurement; typed honestly as
NODE-DRIFT-SHIFTED, no tolerance was widened to force a repro).
Fail-first preserved: nothing was weakened; the wards are identity/
reproduction wards and all four answers live in typed measurements.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
lift/demand/RQ through core.lag_weights_from_v exactly as the race
probe; (ii) ONE eigh per rung (true K); smooth eigenvalues only on
SUBSET (values only); (iii) OLS population statistics as v900;
jackknife over rungs; (iv) robust_node verbatim from the race
probe; NaN nodes excluded from the node fit and counted.

NO-GO COMPLIANCE (frozen): no Gershgorin/Brauer/Weyl bound retried
as content; no rank-1 approximation; no plain Herglotz certificate;
no fit where an identity is claimed (the bookkeeping/W5 wards are
exact; ALL fits here are typed trend measurements with error bars,
and the H0 cancellation claim rests on the exact ward, not the
fit).

NO RH claim: C_h > 0 on the measured ladder is the wall census
restated; a positive fitted trend does not prove H2 - D2 >= c0 for
all h; the probe-5 gate is an exploration schedule, not a theorem.
No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids zetazero
/ nzeros / primerange / isprime / primepi / nextprime / prevprime);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts; lift-race machinery
verbatim from arithmetic_lift_race_probe.py (E8.WALL.LIFTRACE.01);
classical node drift law from node_origin_arch_probe.py (declared
input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wall_matched_asymptotics_probe.py
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
RQ_WARD = 1e-10
SLOPE_REF = 0.077
SLOPE_RTOL = 0.20
DSLOPE_BAR = 0.005
EXPO_BAND = (-2.5, -1.5)
EXPO_CI_BAND = (-2.8, -1.2)
SEP_BAR = 0.5
NODE_C = 0.3727
NODE_S = -0.0116
NODE_CTOL = 0.05
NODE_STOL = 0.008
NG_SMOOTH = 6000
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
    """Leave-one-out jackknife on the OLS (a, b): returns (a, b,
    R2, SE_a, SE_b) -- deterministic honest error bars."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    a, b, r2 = ols_line(x, y)
    n = len(x)
    aa, bb = [], []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        ai, bi, _ = ols_line(x[m], y[m])
        aa.append(ai)
        bb.append(bi)
    aa = np.array(aa)
    bb = np.array(bb)
    se_a = math.sqrt((n - 1) / n * float(np.sum((aa - aa.mean())
                                                ** 2)))
    se_b = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                                ** 2)))
    return a, b, r2, se_a, se_b


# --------------- race machinery, verbatim (arithmetic_lift_race)
def q_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


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
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
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


def main():
    section("PRIME.PORT.MATCHED.ASYMPTOTICS.01 -- hub and demand "
            "expanded around the wandering node; the h^-2 "
            "coefficient H2 - D2 (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder (race surface) + "
            "reproduction wards")
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
        c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
        c_ar = np.asarray(core.arch_lags(M, D), float)
        w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
        v = V[:, 0]
        ug, mg = smooth_comb(alpha)
        c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
        Wv = core.lag_weights_from_v(v, h)
        e_ar = float(np.asarray(c_ar) @ Wv)
        e_t = float(np.asarray(c_at) @ Wv)
        e_s = float(np.asarray(c_sm) @ Wv)
        rungs.append(dict(
            kz=kz, alpha=float(alpha), M=M, D=float(D), h=h,
            m=float(w[0]), lift=e_t - e_s, demand=-(e_ar + e_s),
            node=robust_node(v, D, alpha),
            c_ar=c_ar, c_sm=c_sm, v=v))
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d, alpha %.3f..%.3f  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             min(r["alpha"] for r in rungs),
             max(r["alpha"] for r in rungs), time.time() - T0),
          kill="K1")
    if KILLS:
        return finish({})
    check("W2 WARD truth margin m_h > 0 on every faithful rung "
          "(min %.3e)" % min(r["m"] for r in rungs),
          all(r["m"] > 0 for r in rungs), kill="K2")
    dev_bk = max(abs((r["lift"] - r["demand"]) - r["m"])
                 / max(1.0, abs(r["m"])) for r in rungs)
    check("W3 WARD EXACT BOOKKEEPING lift - demand = m_h: max dev "
          "%.2e <= %.0e" % (dev_bk, RQ_WARD), dev_bk <= RQ_WARD,
          kill="K2")
    als = np.array([r["alpha"] for r in rungs])
    hh = np.array([float(r["h"]) for r in rungs])
    lifts = np.array([r["lift"] for r in rungs])
    dems = np.array([r["demand"] for r in rungs])
    ms = np.array([r["m"] for r in rungs])
    aL, bL, r2L, seaL, sebL = jack_fit(als, lifts)
    aD, bD, r2D, seaD, sebD = jack_fit(als, dems)
    _ae, p_exp, r2e, _see, se_p = jack_fit(np.log(hh), np.log(ms))
    ok_w4 = (abs(bL / SLOPE_REF - 1.0) <= SLOPE_RTOL
             and abs(bD / SLOPE_REF - 1.0) <= SLOPE_RTOL
             and abs(bL - bD) <= DSLOPE_BAR
             and EXPO_BAND[0] <= p_exp <= EXPO_BAND[1])
    check("W4 REPRODUCTION race ledger: lift = %.4f a %+.3f (R^2 "
          "%.3f), demand = %.4f a %+.3f (R^2 %.3f), |dslope| "
          "%.1e <= %.3f, exponent p = %+.3f in [%.1f, %.1f]"
          % (bL, aL, r2L, bD, aD, r2D, abs(bL - bD), DSLOPE_BAR,
             p_exp, EXPO_BAND[0], EXPO_BAND[1]), ok_w4, kill="K2")
    dev_w5 = 0.0
    by_kz = {r["kz"]: r for r in rungs}
    for kz in SUBSET:
        r = by_kz.get(kz)
        if r is None:
            continue
        Ks = core.odd_toeplitz(r["c_ar"] + r["c_sm"], r["M"])
        lam_sm = float(np.linalg.eigvalsh(Ks)[0])
        ws2, Vs2 = np.linalg.eigh(Ks)
        vsm = Vs2[:, 0]
        Wvs = core.lag_weights_from_v(vsm, r["h"])
        dem_sm = -(float(np.asarray(r["c_ar"]) @ Wvs)
                   + float(np.asarray(r["c_sm"]) @ Wvs))
        dev_w5 = max(dev_w5, abs(dem_sm + lam_sm)
                     / max(1.0, abs(lam_sm)))
    check("W5 REPRODUCTION demand(v_sm) = -lam_min(K_smooth) on "
          "the subset: max dev %.2e <= %.0e" % (dev_w5, RQ_WARD),
          dev_w5 <= RQ_WARD, kill="K2")
    for r in rungs:
        r.pop("c_ar", None)
        r.pop("c_sm", None)
        r.pop("v", None)

    # ------------------------------------------------------------ A1
    section("A1 -- H0: the cancellation (exact ward + fitted "
            "shadow)")
    depth = ms / (np.abs(lifts) + np.abs(dems))
    dsl = bL - bD
    se_dsl = math.sqrt(sebL ** 2 + sebD ** 2)
    print("    cancellation depth m/(|lift| + |demand|): med "
          "%.2e, range [%.2e, %.2e]; fitted slope difference "
          "bL - bD = %+.2e +- 2SE %.2e (jackknife)"
          % (float(np.median(depth)), float(np.min(depth)),
             float(np.max(depth)), dsl, 2 * se_dsl))
    if abs(dsl) <= 2 * se_dsl or abs(dsl) <= DSLOPE_BAR:
        a1 = "H0-CANCELS(depth-med=%.1e, dslope=%+.1e+-%.1e)" % (
            float(np.median(depth)), dsl, 2 * se_dsl)
    else:
        a1 = "H0-RESIDUAL-GROWTH(dslope=%+.1e+-%.1e)" % (
            dsl, 2 * se_dsl)
    check("A1.1 typed: %s (exact cancellation is W3; this is the "
          "fitted shadow)" % a1, True)

    # ------------------------------------------------------------ A2
    section("A2 -- H2 - D2: the leading coefficient C_h = m_h h^2 "
            "(fit-free per rung)")
    C = ms * hh ** 2
    print("    kz   h    alpha   m_h        C_h = m h^2")
    for r, c in zip(rungs, C):
        print("    %-4d %-4d %6.3f  %.3e  %8.4f"
              % (r["kz"], r["h"], r["alpha"], r["m"], c),
              flush=True)
    cA, cB, r2C, seA, seB = jack_fit(als, C)
    amax = float(np.max(als))
    Cdeep = cA + cB * amax
    se_deep = math.sqrt(seA ** 2 + (amax * seB) ** 2)
    ci_ok = EXPO_CI_BAND[0] <= p_exp - 2 * se_p and \
        p_exp + 2 * se_p <= EXPO_CI_BAND[1]
    print("\n    C summary: min %.4f, med %.4f, max %.4f; trend "
          "C = %.3f %+.3f alpha (R^2 %.3f), jackknife 2SE "
          "(%.3f, %.3f); deep end C(%.2f) = %.3f +- 2SE %.3f; "
          "exponent p = %+.4f +- 2SE %.4f"
          % (float(np.min(C)), float(np.median(C)),
             float(np.max(C)), cA, cB, r2C, 2 * seA, 2 * seB,
             amax, Cdeep, 2 * se_deep, p_exp, 2 * se_p))
    n_cneg = int(np.sum(C <= 0))
    if n_cneg == 0 and Cdeep - 2 * se_deep > 0 and ci_ok:
        a2 = "H2D2-POSITIVE-STABLE(c0=%.3f)" % float(np.min(C))
    elif n_cneg == 0:
        a2 = ("H2D2-POSITIVE-FRAGILE(c0=%.3f, deep=%.2f+-%.2f, "
              "pCI=[%.2f, %.2f])"
              % (float(np.min(C)), Cdeep, 2 * se_deep,
                 p_exp - 2 * se_p, p_exp + 2 * se_p))
    else:
        a2 = "H2D2-SIGN-UNSTABLE(nonpos=%d)" % n_cneg
    check("A2.1 typed: %s (stability legs: all C_h > 0; deep-end "
          "- 2SE > 0; p CI inside [%.1f, %.1f])"
          % (a2, EXPO_CI_BAND[0], EXPO_CI_BAND[1]), True)

    # ------------------------------------------------------------ A3
    section("A3 -- H2 and D2 separately: leg residuals at the "
            "h^-2 scale")
    rL = lifts - (aL + bL * als)
    rD = dems - (aD + bD * als)
    ratL = float(np.median(np.abs(rL) * hh ** 2)
                 / np.median(C))
    ratD = float(np.median(np.abs(rD) * hh ** 2)
                 / np.median(C))
    print("    med |rL| h^2 / med C = %.3e; med |rD| h^2 / med C "
          "= %.3e (bar %.1f)" % (ratL, ratD, SEP_BAR))
    if ratL <= SEP_BAR and ratD <= SEP_BAR:
        a3 = "LEGS-SEPARABLE(%.2f, %.2f)" % (ratL, ratD)
    else:
        a3 = "LEGS-NOT-SEPARABLE(%.1e, %.1e)" % (ratL, ratD)
    check("A3.1 typed: %s (only the DIFFERENCE H2 - D2 is "
          "measurable when the ratios exceed the bar)" % a3, True)

    # ------------------------------------------------------------ A4
    section("A4 -- the wandering node on this ladder")
    nodes = np.array([r["node"] for r in rungs])
    okn = np.isfinite(nodes)
    cN, sN, r2N = float("nan"), float("nan"), float("nan")
    if int(np.sum(okn)) >= 10:
        cN, sN, r2N = (lambda t: (t[0], t[1], t[2]))(
            ols_line(als[okn], nodes[okn]))
    print("    node fit u*/alpha = %.4f %+.5f alpha (R^2 %.3f, "
          "%d NaN excluded); declared drift law %.4f %+.5f"
          % (cN, sN, r2N, int(np.sum(~okn)), NODE_C, NODE_S))
    if (abs(cN - NODE_C) <= NODE_CTOL
            and abs(sN - NODE_S) <= NODE_STOL):
        a4 = "NODE-DRIFT-REPRO(c=%.4f, s=%+.5f)" % (cN, sN)
    else:
        a4 = "NODE-DRIFT-SHIFTED(c=%.4f, s=%+.5f)" % (cN, sN)
    check("A4.1 typed: %s (tolerances %.2f / %.3f)"
          % (a4, NODE_CTOL, NODE_STOL), True)

    # ------------------------------------------------------------ C
    section("C -- controls on this surface at kz %d" % CTRL_KZ)
    rr = core.build_window(CTRL_KZ)
    alpha, M = rr["alpha"], rr["M"]
    c_ar9 = np.asarray(core.arch_lags(M, rr["D"]), float)
    N_E = int(math.floor(math.exp(2.0 * alpha))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    c_E = core.atom_lags_at(alpha, M, np.log(nn.astype(float)),
                            2.0 * lamE_[nn]
                            / np.sqrt(nn.astype(float)))[0]
    lamE = float(np.linalg.eigvalsh(
        core.odd_toeplitz(c_ar9 + np.asarray(c_E, float), M))[0])
    rr_s = core.build_window(CTRL_KZ, scramble_seed=1)
    uu_s = np.asarray(rr_s["uu"], float)
    mu_s = 2.0 * np.asarray(rr_s["lam"], float)
    c_s = core.atom_lags_at(rr_s["alpha"], rr_s["M"], uu_s, mu_s)[0]
    lamS = float(np.linalg.eigvalsh(core.odd_toeplitz(
        np.asarray(core.arch_lags(rr_s["M"], rr_s["D"]), float)
        + np.asarray(c_s, float), rr_s["M"]))[0])
    print("    Epstein  : lam_min %+.3e -> %s"
          % (lamE, "FIRES" if lamE < 0 else "SILENT"))
    print("    scramble : lam_min %+.3e -> %s"
          % (lamS, "FIRES" if lamS < 0 else "SILENT"))
    check("C1 WARD both controls fire (lam_min < 0)",
          lamE < 0 and lamS < 0, kill="K2")

    return finish(dict(a1=a1, a2=a2, a3=a3, a4=a4, p=p_exp,
                       sep=2 * se_p))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("MATCHED-ASY-MEASURED / %(a1)s / EXPO"
                   "(%(p)+.3f+-%(sep).3f) / %(a2)s / %(a3)s / "
                   "%(a4)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
        print("\n  PROBE-5 GATE: %s"
              % ("OPEN (H2D2-POSITIVE-STABLE)"
                 if labels["a2"].startswith("H2D2-POSITIVE-STABLE")
                 else "CLOSED (gate requires "
                 "H2D2-POSITIVE-STABLE)"))
    print("""
  HONEST FRAME (as frozen): C_h > 0 on the measured ladder is the
  wall census restated in h^2 units -- the typed content is the
  STABILITY of the sign under honest error bars and whether the
  separate leg coefficients resolve at all.  A positive fitted
  trend proves nothing beyond the measured rungs.  NO RH claim.
  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
