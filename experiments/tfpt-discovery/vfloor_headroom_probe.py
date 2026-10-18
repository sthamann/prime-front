#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""vfloor_headroom_probe -- PRIME.PORT.W1.VHEAD.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE INTERFACE OF THE RE-DERIVED CHAIN TO
THE ONE REMAINING SUPPLY.  PRIME.PORT.W1.MONOCOMP.01 replaced the
Gershgorin factorisation of lambda_min(G_core) by the measure
inequality nu_+ <= omega => G_core[nu_+] >= G_core[omega] and
measured the swing: the composition price fell from +8.26 dex to
+0.29 dex, the derived ENV tier moved from -4.00 dex BELOW the
registered target mu1 to +1.55 dex ABOVE it (surface 39/39, deep
16/16 at +3.13 med), and the whole H2 diagonal-law demand vanished
(+8.25 dex of it was the propagated I4 deficit).  That probe left
TWO honest loose ends, and this probe closes both:

 (1) IT USED THE MEASURED v_i.  MONOCOMP offered the v-monotone
     consumption of a v-floor only through its trace corollary [L3]
     (one Cauchy-Schwarz), which is ~0.5 dex weaker and clears mu1
     on only 36/39.  This probe proves and wards that the FULL
     [L2] bound is already v-monotone, so no Cauchy-Schwarz is
     needed anywhere in the chain:
       [L5]  lambda_min(V^{1/2} K V^{1/2}) is nondecreasing in every
             v_i, for every K > 0 and V = diag(v) > 0.
       PROOF.  lambda_min(V^{1/2}KV^{1/2})^{-1} = lambda_max(
       V^{-1/2}K^{-1}V^{-1/2}); that matrix is similar to K^{-1}V^{-1},
       whose spectrum equals that of V^{-1}K^{-1}, which is similar
       to the SYMMETRIC K^{-1/2}V^{-1}K^{-1/2}.  V^{-1} is Loewner-
       antitone in v, hence K^{-1/2}V^{-1}K^{-1/2} is, hence its
       lambda_max is, hence lambda_min(V^{1/2}KV^{1/2}) is monotone
       nondecreasing in v.  QED.
     (The naive route fails and is recorded as a kill: V >= V_lo
     does NOT give V^{1/2}KV^{1/2} >= V_lo^{1/2}KV_lo^{1/2} in the
     Loewner order -- K = ones(2), V = diag(1,t) is a counter-
     example, warded numerically below.  Only the eigenvalue
     statement [L5] survives, and it is all the chain needs.)
     CONSEQUENCE: the derived certificate is
       lambda_min(G_core) >= lambda_min(V_lo^{1/2} K^omega V_lo^{1/2})
     for ANY per-fold lower bound v_i >= v_i^lo > 0 -- i.e. the
     chain consumes exactly one supply, the CLXXXI v-floor, with
     ZERO further composition loss.

 (2) IT NAMED THE NEXT OBJECT WITHOUT A SPEC.  MONOCOMP measured
     that an EXACT per-fold density deviation on folds f <= 32 buys
     +2.00 dex of the residual +2.58 dex envelope price, but an
     exact deviation is not a supply -- a supply is a BOUND
     |d_f - d^ar_f| <= c * dev_f with some sharpness c > 1.  This
     probe measures the gain as a function of c on a frozen ladder
     c in SHARP_C, on frozen fold bands f <= FBANDS, so the next
     CLXXXI-currency probe has a numeric target: how sharp must the
     sub-gamma_1 low-frequency reads be, over how many folds, to buy
     a given number of dex.

WHAT IS MEASURED (slack ladders, surface 39 + deep DEEP_CAP):
  A  the [L5] wards: the spectrum identity, the Loewner
     counterexample (must FIRE), and randomised v_lo <= v draws
     (RND_DRAWS per rung) with the composed inequality
     lambda_min(G_core) >= bound(v_lo) checked directly;
  B  the UNIFORM v-floor budget: the bound is exactly homogeneous
     of degree 1 in a uniform scaling of v, so the admissible
     uniform relative deficit is exactly 10^{-headroom} with
     headroom = log10(bound_ENV/mu1) -- reported as the chain's
     v-supply budget in the CLXXXI dex currency, surface and deep;
  C  the per-fold INFLUENCE weights s_i = dlog(bound)/dlog(v_i)
     (they sum to 1 by homogeneity -- warded), which say WHICH of
     the eight core folds the supply must get right, and the
     SINGLE-FOLD budget: the admissible deficit in v_i alone;
  D  the SUPPLY SHARPNESS ladder of (2).
  E  gates: tau-screen (parent verbatim) on the budget, the
     domination ward, world census (the step is world-blind BY
     CONSTRUCTION, declared -- see MONOCOMP; repeated here because
     the enum is typed here too), AST firewall, anti-circularity.

VERDICT (frozen enums):
  L5-PROVEN(wards) iff the spectrum identity holds to L5_TOL on
    every rung, the Loewner counterexample FIRES, and all
    randomised v_lo draws satisfy the composed inequality; else
    L5-BROKEN (DEAD).
  VBUDGET(med dex, min dex, n/N above mu1) always typed.
  CS-FREE-CHAIN iff L5-PROVEN and the [L2] bound clears mu1 on all
    surface and deep steps (then the chain contains no Cauchy-
    Schwarz at all and the MONOCOMP [L3] corollary is retired);
    else CS-STILL-NEEDED(n/N).
  SUPPLY-SPEC(c*, band, dex) always typed: c* = the largest frozen
    sharpness in SHARP_C whose gain on the widest frozen band is at
    least SPEC_DEX dex; VOID if none.
  Headline VHEAD-CLOSED-INTERFACE(budget dex) iff L5-PROVEN and
    CS-FREE-CHAIN; else VHEAD-PARTIAL(...).
DEAD overrides: MONOCOMP SPEC-SHA ward fails; parent reproduction
fails; the domination ward fails in the truth world.

HONEST SCOPE: this probe proves a matrix lemma and measures a
budget.  It does NOT supply the v-floor -- CLXXXI's sub-gamma_1
Fourier bound closes the deep block 28/28 and leaves 32 shallow
surface rungs open, and nothing here moves that.  It is world-blind
by construction, it is not a wall certificate, W2 / background
cancellation remain RH-hard, and there is NO RH claim.

FROZEN BARS: L5_TOL = 1e-9 (rel, spectrum identity); CE_MARGIN =
1e-6 (the Loewner counterexample must show a negative eigenvalue
below -CE_MARGIN); RND_DRAWS = 6; RND_LO = 0.05 (draws are uniform
in [RND_LO, 1] times v); MONO_TOL = 1e-9 (rel, monotonicity of the
bound under the draws); HOMOG_TOL = 1e-6 (rel, sum of influence
weights == 1); FD_EPS = 1e-4 (relative finite difference for the
influence weights); SHARP_C = (1, 2, 5, 10, 30); FBANDS = (16, 32,
64); SPEC_DEX = 1.00; DEEP_CAP = 8; MIN_DEEP = 4; DOM_TOL = 1e-12;
slope bands 0.30/0.70 (parent verbatim); MONOCOMP SPEC-SHA prefix
warded == bed53f23 (the value printed by that probe's frozen run);
parent SPEC-SHA warded == 084c9689..  Runtime cap declared: 20 min.
Smoke mode VHEAD_SMOKE=1 restricts the surface to 6 steps and the
deep block to 2 rungs.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke run
(VHEAD_SMOKE=1, 6 surface steps + 2 deep rungs, 4.9 s, 14/14 on the
FIRST passage).  NO bar, band, count, rule or enum was moved after
it; this disclosure is the only post-smoke change.  Measured smoke
content the frozen run must confirm: Loewner counterexample fires
at -0.303; spectrum identity 6/6 + 2/2 (worst 1e-12 class);
randomised draws 6/6 + 2/2; surface budget +0.28/+0.56/+0.79 dex on
6/6; deep budget +2.81/+2.86; homogeneity ward 1.7e-11; the
influence weights are (0,0,0,0,0,0,0,1.000) -- to first order the
bound is governed ENTIRELY by the HIGHEST core fold j = 16, which
is exactly the fold where CLXXXI measured its supply to be weakest
(omega_16 med 5.50 on the surface); single-fold budget med +1.04
dex, min +0.28; sharpness ladder F=32: +2.04/+1.78/+1.48/+1.26/
+0.90 for c = 1/2/5/10/30.

AMENDMENT A1 (disclosed, after the first frozen run, 45.8 s,
14/14): the FROZEN BARS block promised a MONOCOMP SPEC-SHA prefix
ward that the code did not implement -- the ward is now present
with the constant bed53f23 (the value the MONOCOMP frozen run
printed and the value this probe's first frozen run printed as
"MONOCOMP SPEC SHA-256").  This ADDS a check, moves no bar, band,
count, rule or enum, and changes no measured quantity; the first
frozen run's numbers are reproduced by the amended run and are
recorded here regardless: L5 counterexample -0.3028, spectrum
identity 39/39 + 8/8 (worst 2.44e-15), randomised draws 39/39 +
8/8, surface budget +0.28/+1.55/+2.31 on 39/39, deep budget
+2.81/+2.98 on 8/8, homogeneity 3.19e-11, influence weights
(0,...,0,1.000) with argmax at fold j = 16 on 39/39, single-fold
budget med +2.09 min +0.28, sharpness F=32 +2.00/+1.73/+1.43/
+1.19/+0.82, screens budget AMBIG(-0.557) / bound PASS(-0.061).
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

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)
import monotone_composition_probe as mono  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
MONOCOMP_SHA8 = "bed53f23"
L5_TOL = 1.0e-9
CE_MARGIN = 1.0e-6
RND_DRAWS = 6
RND_LO = 0.05
MONO_TOL = 1.0e-9
HOMOG_TOL = 1.0e-6
FD_EPS = 1.0e-4
SHARP_C = (1, 2, 5, 10, 30)
FBANDS = (16, 32, 64)
SPEC_DEX = 1.00
DEEP_CAP = 8
MIN_DEEP = 4
DOM_TOL = 1.0e-12
SMOKE = os.environ.get("VHEAD_SMOKE", "") == "1"
BANNED_IDS = parent.BANNED_IDS

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
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def bnd(K, v):
    G = np.sqrt(v)[:, None] * K * np.sqrt(v)[None, :]
    return float(np.linalg.eigvalsh(0.5 * (G + G.T))[0])


def spectrum_identity(K, v):
    """lambda_max(V^-1/2 K^-1 V^-1/2) == lambda_max(K^-1/2 V^-1 K^-1/2)."""
    Ki = np.linalg.inv(K)
    sv = 1.0 / np.sqrt(v)
    A = Ki * np.outer(sv, sv)
    ev, U = np.linalg.eigh(0.5 * (K + K.T))
    Kmh = U @ np.diag(1.0 / np.sqrt(np.maximum(ev, 1e-300))) @ U.T
    B = Kmh @ np.diag(1.0 / v) @ Kmh
    la = float(np.linalg.eigvalsh(0.5 * (A + A.T))[-1])
    lb = float(np.linalg.eigvalsh(0.5 * (B + B.T))[-1])
    return abs(la / lb - 1.0), la


def loewner_counterexample():
    """V >= V_lo does NOT give V^1/2 K V^1/2 >= V_lo^1/2 K V_lo^1/2."""
    K = np.ones((2, 2)) + 1e-12 * np.eye(2)
    t = 4.0
    V = np.diag([1.0, t])
    Vl = np.eye(2)
    D = np.sqrt(V) @ K @ np.sqrt(V) - np.sqrt(Vl) @ K @ np.sqrt(Vl)
    return float(np.linalg.eigvalsh(0.5 * (D + D.T))[0])


def influence(K, v):
    """s_i = dlog(bound)/dlog(v_i) by central differences."""
    b0 = bnd(K, v)
    den = math.log((1.0 + FD_EPS) / (1.0 - FD_EPS))
    s = np.zeros(len(v))
    for i in range(len(v)):
        vp = v.copy()
        vm = v.copy()
        vp[i] *= (1.0 + FD_EPS)
        vm[i] *= (1.0 - FD_EPS)
        s[i] = (math.log(bnd(K, vp)) - math.log(bnd(K, vm))) / den
    return s, b0


def single_fold_budget(K, v, mu1):
    """largest per-fold deficit (dex) in v_i alone keeping bnd > mu1."""
    out = []
    for i in range(len(v)):
        lo, hi = 1e-12, 1.0
        if bnd(K, v) <= mu1:
            out.append(0.0)
            continue
        vv = v.copy()
        vv[i] = v[i] * lo
        if bnd(K, vv) > mu1:
            out.append(float("inf"))
            continue
        for _ in range(40):
            mid = math.sqrt(lo * hi)
            vv[i] = v[i] * mid
            if bnd(K, vv) > mu1:
                hi = mid
            else:
                lo = mid
        out.append(-math.log10(hi))
    return np.array(out)


def payload(alpha, M, c_at, c_ar, y_core, v_core, h, Gc,
            want_sharp=True):
    c_at = np.asarray(c_at, float)
    d = base.grid_density(c_ar + c_at)
    d_ar = base.grid_density(c_ar)
    L = 2 * M - 2
    f, wg, xg = mono.fold_grid(L)
    de = mono.deltas(alpha, c_at, d, d_ar)
    df = d[f]
    daf = np.abs(d_ar[f])
    dom = float(np.max(np.maximum(df, 0.0) - (daf + de["ENV"])))
    K = mono.kernel_of(xg, wg * (daf + de["ENV"]), y_core, h)
    if K is None:
        return None
    out = dict(K=K, dom=dom, truth=float(np.linalg.eigvalsh(Gc)[0]),
               h=h, v=np.asarray(v_core, float))
    if want_sharp:
        dev = np.abs(df - d_ar[f])
        sharp = {}
        for fb in FBANDS:
            for c in SHARP_C:
                dd = np.full(len(f), de["ENV"])
                nn = min(fb + 1, len(dd))
                dd[:nn] = np.minimum(c * dev[:nn], de["ENV"])
                Kc = mono.kernel_of(xg, wg * (daf + dd), y_core, h)
                if Kc is not None:
                    sharp[(fb, c)] = bnd(Kc, out["v"])
        out["sharp"] = sharp
    return out


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "L5-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join([labels.get("head", "-"),
                              labels.get("l5", "-"),
                              labels.get("bud", "-"),
                              labels.get("cs", "-"),
                              labels.get("spec", "-")])
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: a matrix lemma and a budget.  The v-floor itself is
  NOT supplied here (CLXXXI: deep 28/28 closed, 32 shallow surface
  rungs open).  The step is world-blind by construction, it is not
  a wall certificate, W2 / background cancellation stay RH-hard.
  NO RH claim; no marker moves; no promotion.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W1.VHEAD.01 -- the v-floor interface of the "
            "measure-inequality chain (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    mono_sha = hashlib.sha256(mono.__doc__.encode("utf-8")).hexdigest()
    parent_sha = hashlib.sha256(
        parent.__doc__.encode("utf-8")).hexdigest()
    print("    MONOCOMP SPEC SHA-256 = %s" % mono_sha)
    print("    NO RH claim.")
    if SMOKE:
        print("    *** SMOKE MODE ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", parent_sha == PARENT_SHA,
          kill="K2")
    check("S0c MONOCOMP SPEC prefix reproduced (amendment A1)",
          mono_sha[:8] == MONOCOMP_SHA8, mono_sha[:8], kill="K2")

    section("W -- parent ladder reproduction")
    zones, truth, full, rows = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(rows) == 39,
          "%d/%d/%d" % (len(zones), len(full), len(rows)), kill="K1")
    if KILLS:
        return finish({})
    for w in rows:
        Gc = w["H"] @ w["H"].T
        w["Gc"] = 0.5 * (Gc + Gc.T)

    section("A -- the [L5] wards")
    ce = loewner_counterexample()
    check("A0 Loewner counterexample FIRES (naive route is dead)",
          ce <= -CE_MARGIN, "min eig %+.4f" % ce, kill="K3")
    use = rows[:6] if SMOKE else rows
    rng = np.random.default_rng(20260811)
    pay = []
    n_id = n_mono = n_dom = 0
    for w in use:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        c_at = core.atom_lags_at(rr["alpha"], rr["M"], rr["uu"],
                                 2.0 * rr["lam"])[0]
        p = payload(rr["alpha"], rr["M"], c_at, rr["c_ar"],
                    r2["y_core"], r2["v_core"], r2["h"], w["Gc"])
        if p is None:
            continue
        p["kz"] = r2["kz"]
        p["mu1"] = w["mu1"]
        p["tau"] = w["tau"]
        dev, _ = spectrum_identity(p["K"], p["v"])
        p["id"] = dev
        n_id += int(dev <= L5_TOL)
        n_dom += int(p["dom"] <= DOM_TOL)
        b0 = bnd(p["K"], p["v"])
        p["b0"] = b0
        ok = True
        for _ in range(RND_DRAWS):
            fac = rng.uniform(RND_LO, 1.0, size=len(p["v"]))
            bl = bnd(p["K"], p["v"] * fac)
            ok = ok and bl <= b0 * (1.0 + MONO_TOL) \
                and p["truth"] >= bl * (1.0 - MONO_TOL)
        n_mono += int(ok)
        pay.append(p)
        if len(pay) % 10 == 0:
            print("    ... %d rungs  [%.1f s]"
                  % (len(pay), time.time() - T0), flush=True)
    n = len(pay)
    check("A1 spectrum identity lam_max(V^-1/2K^-1V^-1/2) == "
          "lam_max(K^-1/2V^-1K^-1/2)", n_id == n,
          "%d/%d (worst %.2e)" % (n_id, n, max(p["id"] for p in pay)),
          kill="K3")
    check("A2 randomised v_lo <= v: bound monotone AND composed "
          "inequality holds", n_mono == n,
          "%d/%d (%d draws each)" % (n_mono, n, RND_DRAWS), kill="K3")
    check("A3 domination hypothesis (truth world)", n_dom == n,
          "%d/%d" % (n_dom, n), kill="K2")

    section("B -- the UNIFORM v-floor budget (CLXXXI dex currency)")
    mu1 = np.array([p["mu1"] for p in pay])
    b0 = np.array([p["b0"] for p in pay])
    bud = np.log10(b0 / mu1)
    print("    surface budget log10(bound_ENV/mu1): %+.2f / %+.2f / "
          "%+.2f dex; above mu1 on %d/%d"
          % (band(bud) + (int(np.sum(b0 > mu1)), n)))
    print("    i.e. the chain still certifies s_P >= mu1 with a "
          "UNIFORM v-floor deficit of up to %.1f%% of the true core "
          "masses (worst rung %.1f%%)"
          % (100.0 * (1.0 - 10 ** (-float(np.median(bud)))),
             100.0 * (1.0 - 10 ** (-float(np.min(bud))))))
    check("B1 uniform budget recorded", True)

    section("C -- per-fold influence weights and single-fold budget")
    infl = []
    sfb = []
    for p in pay:
        s, _ = influence(p["K"], p["v"])
        infl.append(s)
        sfb.append(single_fold_budget(p["K"], p["v"], p["mu1"]))
    infl = np.array(infl)
    sfb = np.array(sfb)
    sums = infl.sum(axis=1)
    check("C1 homogeneity ward sum_i s_i == 1",
          bool(np.max(np.abs(sums - 1.0)) <= HOMOG_TOL),
          "worst dev %.2e" % float(np.max(np.abs(sums - 1.0))))
    print("    influence weights s_i (median over rungs), core folds "
          "j = %s:" % str(base.CORE_J))
    print("      " + "  ".join("%.3f" % x
                               for x in np.median(infl, axis=0)))
    print("    dominant fold index (argmax s_i) histogram: %s"
          % np.bincount(np.argmax(infl, axis=1), minlength=8).tolist())
    fin = np.isfinite(sfb)
    print("    single-fold budget (dex of deficit in ONE v_i alone): "
          "med %+.2f, min %+.2f, unbounded on %d/%d entries"
          % (float(np.median(sfb[fin])) if fin.any() else float("nan"),
             float(np.min(sfb[fin])) if fin.any() else float("nan"),
             int(np.sum(~fin)), sfb.size))
    check("C2 influence anatomy recorded", True)

    section("D -- the SUPPLY SHARPNESS ladder (the next object's spec)")
    print("    gain in dex over the ENV tier when the per-fold "
          "deviation bound is c * |d_f - d^ar_f| on folds f <= F:")
    print("      F     c=1     c=2     c=5     c=10    c=30")
    spec = {}
    for fb in FBANDS:
        cells = []
        for c in SHARP_C:
            g = [math.log10(p["sharp"][(fb, c)] / p["b0"])
                 for p in pay if (fb, c) in p.get("sharp", {})]
            gm = float(np.median(g)) if g else float("nan")
            spec[(fb, c)] = gm
            cells.append("%+.2f" % gm)
        print("      %-5d %s" % (fb, "  ".join(cells)))
    cstar = None
    fbmax = max(FBANDS)
    for c in sorted(SHARP_C, reverse=True):
        if spec.get((fbmax, c), -1e9) >= SPEC_DEX:
            cstar = c
            break
    check("D1 sharpness ladder recorded", True)

    section("E -- tau-screen and world census")
    taus = np.array([p["tau"] for p in pay])
    for nm, vals in (("budget b/mu1", b0 / mu1), ("bound", b0)):
        lab, sl = parent.screen(vals, taus)
        print("    %-14s %s" % (nm, lab))
    print("    WORLD CENSUS: inherited from MONOCOMP and DECLARED -- "
          "the measure inequality holds for every measure, so the "
          "step is world-blind; the prime content is the domination "
          "HYPOTHESIS (a psi theorem) and the v-floor.")
    check("E1 screens recorded", True)

    section("F -- deep block")
    deep.build_ext_tables()
    cand = []
    for kz in range(2, min(deep.KZ_SCAN_MAX,
                           len(deep.EXT["NN"]) - 2)):
        alpha = float(deep.EXT["U"][kz])
        if math.exp(2.0 * alpha) > deep.TAB_EXT:
            break
        if math.exp(2.0 * alpha) <= core.ATOM_MAX:
            continue
        hz = deep.ext_frame(kz)[2]
        if not (deep.H_HOLD[0] <= hz <= deep.H_HOLD[1]):
            continue
        cand.append(kz)
    cand = sorted(cand, key=lambda k: (deep.ext_frame(k)[2], k))
    cand = cand[:2] if SMOKE else cand[:DEEP_CAP]
    dn = d_id = d_mono = d_pos = 0
    dbud = []
    for kz in cand:
        g = deep.ext_gram(kz)
        if not isinstance(g, dict) or not g.get("core_ok") \
                or "chain" not in g:
            continue
        alpha, Mz, hz, ka = deep.ext_frame(kz)
        c_atd, Dz = core.atom_lags_at(alpha, Mz, deep.EXT["U"][:ka],
                                      deep.EXT["MU"][:ka])
        c_ar = np.asarray(core.arch_lags(Mz, Dz), float)
        Pc = base.eval_chain(g["chain"][0], g["chain"][1],
                             g["chain"][2], g["y_core"], g["h"])
        Gd = np.sqrt(g["v_core"])[:, None] * (Pc @ Pc.T) \
            * np.sqrt(g["v_core"])[None, :]
        p = payload(alpha, Mz, c_atd, c_ar, g["y_core"],
                    g["v_core"], g["h"], 0.5 * (Gd + Gd.T),
                    want_sharp=False)
        if p is None:
            continue
        dn += 1
        mu = 4.0 * math.sin(math.pi / (2 * g["h"] + 1)) ** 2
        b = bnd(p["K"], p["v"])
        dev, _ = spectrum_identity(p["K"], p["v"])
        d_id += int(dev <= L5_TOL)
        ok = True
        for _ in range(RND_DRAWS):
            fac = rng.uniform(RND_LO, 1.0, size=len(p["v"]))
            bl = bnd(p["K"], p["v"] * fac)
            ok = ok and bl <= b * (1.0 + MONO_TOL) \
                and p["truth"] >= bl * (1.0 - MONO_TOL)
        d_mono += int(ok)
        d_pos += int(b > mu)
        dbud.append(math.log10(b / mu))
        print("    deep kz %-4d h %-5d bound %.3e  mu1 %.2e  budget "
              "%+.2f dex  [%.1f s]"
              % (kz, g["h"], b, mu, dbud[-1], time.time() - T0),
              flush=True)
    check("F1 deep census >= %d" % MIN_DEEP, dn >= MIN_DEEP or SMOKE,
          "%d" % dn)
    check("F2 deep [L5] wards", dn and d_id == dn and d_mono == dn,
          "%d/%d id, %d/%d mono" % (d_id, dn, d_mono, dn), kill="K3")
    if dbud:
        print("    deep budget med %+.2f min %+.2f | above mu1 %d/%d"
              % (float(np.median(dbud)), float(np.min(dbud)), d_pos,
                 dn))

    tot = n + dn
    pos = int(np.sum(b0 > mu1)) + d_pos
    l5ok = (ce <= -CE_MARGIN and n_id == n and n_mono == n
            and d_id == dn and d_mono == dn)
    lab_l5 = ("L5-PROVEN(spectrum identity %d/%d + %d/%d deep, "
              "counterexample fires at %+.3f, %d randomised draws "
              "per rung)" % (n_id, n, d_id, dn, ce, RND_DRAWS)) \
        if l5ok else "L5-BROKEN"
    allb = np.concatenate([bud, np.array(dbud)]) if dbud else bud
    lab_bud = ("VBUDGET(med %+.2f dex, min %+.2f dex, above mu1 on "
               "%d/%d)" % (float(np.median(allb)), float(np.min(allb)),
                           pos, tot))
    lab_cs = ("CS-FREE-CHAIN(the [L3] Cauchy-Schwarz corollary is "
              "retired: the full [L2] bound is v-monotone and clears "
              "mu1 on %d/%d)" % (pos, tot)) if (l5ok and pos == tot) \
        else "CS-STILL-NEEDED(%d/%d)" % (pos, tot)
    lab_spec = ("SUPPLY-SPEC(a per-fold bound c*|d_f - d^ar_f| on "
                "folds f <= %d buys >= %.2f dex up to sharpness "
                "c = %s)" % (fbmax, SPEC_DEX, cstar)) if cstar \
        else "SUPPLY-SPEC-VOID(no frozen sharpness reaches %.2f dex)" \
        % SPEC_DEX
    head = ("VHEAD-CLOSED-INTERFACE(the re-derived chain consumes "
            "exactly one supply with zero further composition loss; "
            "budget med %+.2f dex)" % float(np.median(allb))) \
        if (l5ok and pos == tot) else "VHEAD-PARTIAL(%d/%d)" % (pos,
                                                                tot)
    return finish(dict(head=head, l5=lab_l5, bud=lab_bud, cs=lab_cs,
                       spec=lab_spec))


if __name__ == "__main__":
    sys.exit(main())
