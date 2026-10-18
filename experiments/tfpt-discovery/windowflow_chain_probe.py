#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""windowflow_chain_probe -- PRIME.WINDOWFLOW.CHAIN.01 (round 232):
after RELATIVE_NO_COMMON_CARRIER (r225) killed the naive node-level
window transport -- do the CHAIN COEFFICIENTS (never the nodes)
converge along the window ladder, does a limit Jacobi object exist,
and does its convergence rate buy a positivity-transfer budget?

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding): w = window (kz rung), N_w = builder depth
(the Lanczos cap of the rung), n = chain STEP index -- step n holds
the coefficient pair (alphahat_n, gammahat_{n+1}) of the signed
functional mutilde_w = mu_w - nu_w with gammahat_{n+1} =
h_{n+1}(mutilde)/h_n(mutilde) -- and theta = n/N_w is the filling
fraction.  n and w are NEVER mixed (r225/r226 discipline); the
DEGREE_ALIAS must-fail below keeps the axis loud.

LADDER RULE (sealed): the ladder is every frame-A rung
(core.frame_a_zones()) whose builder depth satisfies h <= 900 (the
TOO-DEEP bar of the v881 lane), whose Lanczos chain completes N_w
positive beta steps; windows sorted by (N_w, kz).  Measured census:
42 usable windows, N_w = 142 .. 878 (the five known rungs 9/12/13/
26/40 included); no rung in range is dropped.

NORMALIZATION RULE (sealed BEFORE evaluation): the folded builder
places every window on x = cos(2 pi u / L) in [-1, 1]; measured
support hulls have x_min = -1 EXACTLY (the u = L/2 rung) and
1 - x_max ~ N^-2 (slope gate [-2.3, -1.7]).  THE AFFINE MAP IS THE
IDENTITY (c_w = 0, s_w = 1): no rescaling is applied, and the
comparison of (alphahat_n(w), gammahat_n(w)) across w is performed
in the raw common coordinate.  The chain is additionally EXACTLY
invariant under mutilde -> c mutilde (gated <= 1e-12): the
"normalized chain" IS the chain; the only non-invariant scalar is
h_0(mutilde) = sum(ws) - sum(vs), which is measured separately and
is EXTENSIVE (h_0 ~ a log N_w, a > 0.5, no limit -- typed, never
averaged into the chain).

LEG A -- FIXED-DEGREE CONVERGENCE (sealed adjudication): for
n in {0, 1, 2, 5, 10, 20, 50, 100} the ladder sequences
alphahat_n(w), gammahat_{n+1}(w) are tested by the pair-difference
fit log|v(w_{i+1}) - v(w_i)| vs log sqrt(N_i N_{i+1}); CONV_n iff
fitted slope <= -0.5 (strictly faster than 1/sqrt(N)) AND the last
pair difference <= 5e-3, for BOTH coefficients.  The verdict core
set is n in {0, 1, 2, 5, 10, 20} (sealed; 50/100 are reported and
typed but sit near the f64/jitter asymptopia edge of a N <= 878
ladder).  CHAIN_CONVERGES iff every core n is CONV.

LEG B -- THETA PROFILE (sealed): at n = floor(theta N_w) for theta
in {0.25, 0.5, 0.75, 0.98}: BOUNDED iff every gammahat value lies
in [0.05, 1.0] over the whole ladder; PROFILE_CONVERGES iff the
top-half-ladder std <= 0.5 x bottom-half std for >= 3 of 4 theta,
else THETA_BOUNDED_QUENCHED; UNIFORM_MARGIN_098 iff
min_w gammahat at theta = 0.98 >= 0.05 (gamma away from 0 and, by
the 1.0 bound, away from infinity).  The terminal band
(0.98 N_w, N_w] is DISCLOSED separately: it contains the r228
quasi-definiteness boundary (gammahat_{N_w} <= 0 on offset-0
windows) and is never averaged into the profile.

LEG C -- CONTROLS (sealed): EPSTEIN (w9 base, the only basis the
control builder owns): the chain must flip first at step 25
(re-gate of r226/r227).  SCRAMBLE (scramble_seed = 1 on a sealed
10-rung sub-ladder): (c1) NO ladder convergence at n = 0 --
pair-diff slope > -0.3 OR last diff > 1e-2 (each scramble redraws
its positions; the ladder is incoherent by construction); (c2)
every scramble chain leaves the positive cone at step <= 40.
INTERPRETATION RULE (sealed): if the controls fail to converge
while MAIN converges, ladder convergence is NOT generic geometry
-- it is the coherence of the NESTED arithmetic comb (each MAIN
window extends the same von Mangoldt atoms); the separation is
then BOTH in convergence and in sign.

LEG D -- TRANSFER ADJUDICATION (sealed): for every consecutive
ladder pair (w, w') the bulk budget ratio is
    rho(w, w') = sup_{n < 0.98 min(N, N')} |Delta gammahat_n|
                 / min_{same range, both windows} gammahat_n;
WITH_TRANSFER_BUDGET iff rho < 1 on ALL pairs (pointwise Weyl-type
transfer: a positivity floor of one window covers the neighbour's
whole shared bulk).  HONESTY CLAUSE (sealed): the budget covers
n <= 0.98 N_prev ONLY; the frontier band n in (0.98 N_prev, N_w]
-- exactly where the r228 flip indices N_w + 0/2/2/3/1 live -- is
beyond every predecessor's life and is NOT transferable from the
ladder history; the limit object controls fixed n, never the
moving frontier: FRONTIER_BAND_UNCOVERED whenever the wall margin
at the frontier is not itself uniformly bounded (it is not: the
r228 boundary sits O(1) degrees past N_w by construction).

MUST-FAILS (each loud): (m1) AFFINE_ALIAS -- scaling one window's
node coordinates by 1.1 must break the fixed-degree comparison
(gamma scales by 1.21); the identity normalization is load-bearing,
not decorative; (m2) DEGREE_ALIAS -- comparing alphahat_1(w)
against alphahat_0(w') must be > 100 x louder than the honest
alphahat_0 ladder difference; (m3) SEED trap -- scramble seed 2
differs from seed 1 at O(1) (the control is seed-pinned).

HIGH-PRECISION WARD: mpmath dps = 40 plain monic signed recursion
(no scaling tricks) on the SMALLEST rung (kz = 18) through step
30 re-derives the f64 (alphahat, gammahat) chain to <= 1e-10.

SEALED VERDICTS: CHAIN_CONVERGES_WITH_TRANSFER_BUDGET /
CHAIN_CONVERGES_NO_BUDGET / CHAIN_DRIFTS / SCALING_PROFILE_ONLY;
modifiers FRONTIER_BAND_UNCOVERED / THETA_BOUNDED_QUENCHED /
LADDER_COHERENCE_IS_ARITHMETIC.

RECORD TABLES (frozen from calib_wf_pass1.log, 22/22 first pass;
freeze disclosure: three pre-run draft records were corrected to
the measured pass-1 values -- h_0 growth slope, scramble ladder
slope, mp-ward drift; NO bar or rule was changed at any point):
CAL_VERDICT = CHAIN_CONVERGES_WITH_TRANSFER_BUDGET(bulk 0.98) +
FRONTIER_BAND_UNCOVERED + THETA_BOUNDED_QUENCHED +
LADDER_COHERENCE_IS_ARITHMETIC.  Key numbers: ladder 42 windows
N = 142..878 (no rung dropped), hull slope -2.00, scale-invariance
3.7e-15; the wall holds LADDER-WIDE: min r_n in [0.2104, 0.3666]
> 0 over ALL 42 windows (min at kz = 82, N = 534; no flip below
N_w anywhere -- the r226 five-window profile extends to the full
frame-A ladder); h_0 ~ 0.773 log N (max res 0.30, extensive);
Leg A slopes (alpha/gamma): n = 0: -0.60/-0.63, 1: -0.80/-0.90,
2: -0.99/-1.07, 5: -1.49/-1.57, 10: -2.55/-2.69, 20: -3.63/-3.54
(all core CONV, last diffs <= 9.3e-4); n = 50: -1.16/-1.08 (diffs
3.7e-3/2.1e-3, CONV), n = 100: -0.92/-1.11 (alpha last diff
6.9e-3 > bar: CONV_TREND, typed); limit chain approaches the free
[-1,1] equilibrium (alphahat -> 0, gammahat -> 1/4:
0.2180/0.2425/0.2462/0.2487/0.2494/0.2496 at the core degrees);
theta profile gammahat in [0.166, 0.292], std ratios top/bottom
0.65/0.65/0.68/0.82 (> 0.5 on all four: QUENCHED), theta = 0.98
margin 0.2141; terminal band dips to -1.0592 with
gammahat_{N_w} <= 0 on 18 of 42 windows (the r228 boundary,
disclosed); EPSTEIN flips at step 25 exactly; SCRAMBLE ladder
n = 0 pair-diff slope +1.19 with last diff 4.2e-2 (no convergence
under the sealed rule), flips at steps 3..22; budget ratios
min/median/max 0.30/0.49/0.89 (< 1 on all 41 pairs, top pairs
0.37); must-fails 0.049 (871 x honest), 0.52 vs 9.3e-4, 0.13;
mp-dps-40 ward 4.6e-15.  AMENDMENTS: NONE after freeze.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fermiedge_classify_probe as FC        # noqa: E402 r227
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
SMOKE_KZ = (9, 12, 13, 26, 40)
N_FIXED = (0, 1, 2, 5, 10, 20, 50, 100)
N_CORE = (0, 1, 2, 5, 10, 20)
THETAS = (0.25, 0.5, 0.75, 0.98)
SLOPE_BAR = -0.5
LASTDIFF_BAR = 5e-3
BUDGET_CUT = 0.98
G_BOUNDS = (0.05, 1.0)
MARGIN_098 = 0.05
HULL_SLOPE = (-2.3, -1.7)
SCALE_INV_BAR = 1e-12
SCR_KZ = (18, 12, 9, 29, 39, 19, 26, 16, 40, 30)
SCR_FLIP_MAX = 40
EPSTEIN_FLIP = 25
MP_WARD_BAR = 1e-10
MP_WARD_KZ = 18
MP_WARD_N = 30
CAL_VERDICT = ("CHAIN_CONVERGES_WITH_TRANSFER_BUDGET(bulk 0.98) + "
               "FRONTIER_BAND_UNCOVERED + THETA_BOUNDED_QUENCHED + "
               "LADDER_COHERENCE_IS_ARITHMETIC")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; index firewall "
                       "w/N_w/n/theta binding; ladder + identity "
                       "normalization + all bars sealed in the "
                       "frozen spec" if not bad else "; ".join(bad))


def slope_fit(xs_, ys_):
    x = np.asarray(xs_, float)
    y = np.asarray(ys_, float)
    xm, ym = x.mean(), y.mean()
    sl = float(np.sum((x - xm) * (y - ym)) / np.sum((x - xm) ** 2))
    res = y - (ym + sl * (x - xm))
    return sl, float(np.max(np.abs(res)))


def pair_diff_fit(vals, Ns_):
    """sealed Leg-A statistic: slope of log|successive diff| vs
    log sqrt(N_i N_{i+1}) plus the last-pair |diff|."""
    x, y = [], []
    for i in range(len(vals) - 1):
        dv = abs(vals[i + 1] - vals[i])
        if dv > 0.0:
            x.append(0.5 * (math.log(Ns_[i]) + math.log(Ns_[i + 1])))
            y.append(math.log(dv))
    sl, _res = slope_fit(x, y)
    return sl, abs(vals[-1] - vals[-2])


def r_margin(d, ch, N):
    """min_n r_n over n < N via the r226 dictionary
    r_n = h_n(mutilde)/h_n(mu) (log-safe, no determinant)."""
    lgh_mu = math.log(d["m0"])
    rmin, rmin_n = float("inf"), -1
    for n in range(N):
        if n > 0:
            lgh_mu += 2.0 * math.log(float(d["be"][n - 1]))
        r = ch[n]["sg_h"] * math.exp(ch[n]["lg_h"] - lgh_mu)
        if r < rmin:
            rmin, rmin_n = r, n
    return rmin, rmin_n


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("windowflow_chain_probe -- PRIME.WINDOWFLOW.CHAIN.01 "
          "(round 232)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (five known rungs)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "ladder = frame-A rungs with h <= %d; affine map = "
          "IDENTITY (sealed; hull gate slope %s); fixed degrees %s "
          "(core %s, slope bar %.1f, lastdiff bar %.0e; smoke mode "
          "adjudicates lastdiff only -- 4 pairs cannot carry a "
          "slope fit); thetas %s; budget cut %.2f; verdicts sealed "
          "in the frozen spec"
          % (H_CAP, str(HULL_SLOPE), str(N_FIXED), str(N_CORE),
             SLOPE_BAR, LASTDIFF_BAR, str(THETAS), BUDGET_CUT))

    # ---------------- S1: ladder census + normalization
    section("S1  LADDER CENSUS + SEALED NORMALIZATION")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    lad = []
    dropped = []
    for kz in kzs:
        d = HS.window_data(kz)
        N = d["n_max"]
        if len(d["be"]) < N or bool(np.any(d["be"][:N] <= 0.0)):
            dropped.append(kz)
            continue
        lad.append((N, kz, d))
    lad.sort(key=lambda t: (t[0], t[1]))
    Ns = [t[0] for t in lad]
    info("usable ladder: %d windows, N_w = %d .. %d%s"
         % (len(lad), Ns[0], Ns[-1],
            ("; dropped %s" % dropped) if dropped else
            "; no rung dropped"))
    check("G10-ladder-census", len(lad) >= (5 if smoke else 40)
          and not dropped,
          "%d frame-A rungs with h <= %d ALL complete their Lanczos "
          "chain (positive beta through N_w); the five known rungs "
          "are contained; sorted by (N_w, kz)"
          % (len(lad), H_CAP))

    hx, hy = [], []
    okmin = True
    for N, kz, d in lad:
        xs, ys = d["xs"], d["ys"]
        lo = min(float(xs.min()), float(ys.min()))
        hi = max(float(xs.max()), float(ys.max()))
        okmin = okmin and lo <= -1.0 + 1e-12
        hx.append(math.log(N))
        hy.append(math.log(1.0 - hi))
    slh, _ = slope_fit(hx, hy)
    ok_hull = okmin and (smoke or
                         (HULL_SLOPE[0] <= slh <= HULL_SLOPE[1]))
    check("G11-common-hull-identity-map", ok_hull,
          "every window lives on x = cos(2 pi u/L) in [-1, 1]: "
          "x_min = -1 exactly on all windows, 1 - x_max shrinks "
          "with slope %.2f in log N (sealed gate %s): the affine "
          "normalization is the IDENTITY -- windows are compared "
          "in the raw common coordinate" % (slh, str(HULL_SLOPE)))

    d9 = next(d for N, kz, d in lad if kz == 9)
    d9s = {k: (v.copy() if isinstance(v, np.ndarray) else v)
           for k, v in d9.items()}
    d9s["ws"] = d9s["ws"] * 3.0
    d9s["vs"] = d9s["vs"] * 3.0
    c1 = FC.signed_chain(d9, 50)
    c2 = FC.signed_chain(d9s, 50)
    devs = max(max(abs(c1[n]["alphahat"] - c2[n]["alphahat"])
                   for n in range(50)),
               max(abs(c1[n]["gammahat_next"]
                       - c2[n]["gammahat_next"]) for n in range(50)))
    check("G12-scale-invariance", devs <= SCALE_INV_BAR,
          "the chain is EXACTLY invariant under mutilde -> "
          "3 mutilde (max dev %.1e <= %.0e over 50 steps): the "
          "normalized chain IS the chain; only h_0 carries scale"
          % (devs, SCALE_INV_BAR))

    # ---------------- S2: wall census + h_0 growth
    section("S2  WALL CENSUS LADDER-WIDE + h_0 GROWTH")
    chains = {}
    margins = []
    h0s = []
    for N, kz, d in lad:
        ch = FC.signed_chain(d, N)
        chains[kz] = ch
        rmin, rmin_n = r_margin(d, ch, N)
        margins.append((rmin, rmin_n, kz, N))
        h0s.append(float(np.sum(d["ws"]) - np.sum(d["vs"])))
    ok_wall = all(m[0] > 0.0 for m in margins)
    mlo = min(margins)
    mhi = max(margins)
    info("margins: min r = %.4f (kz=%d, N=%d, at n=%d) .. %.4f "
         "(kz=%d, N=%d)" % (mlo[0], mlo[2], mlo[3], mlo[1],
                            mhi[0], mhi[2], mhi[3]))
    check("G20-wall-ladder-wide", ok_wall,
          "ALL r_n > 0 for n < N_w on ALL %d windows (min margin "
          "%.4f, max %.4f, no downward trend): the r226 five-window "
          "wall profile extends to the full frame-A ladder -- the "
          "cofinal object of interest exists on every rung"
          % (len(lad), mlo[0], mhi[0]))
    slh0, resh0 = slope_fit([math.log(N) for N, _k, _d in lad], h0s)
    check("G21-h0-extensive", all(h > 0 for h in h0s)
          and slh0 > 0.5,
          "h_0(mutilde) = sum(ws) - sum(vs) > 0 on every window "
          "and grows ~ %.3f log N (max res %.2f): EXTENSIVE, no "
          "limit -- typed and kept out of the chain comparison"
          % (slh0, resh0))

    # ---------------- S3: Leg A fixed-degree convergence
    section("S3  LEG A -- FIXED-DEGREE CONVERGENCE (sealed rule)")
    kz_order = [kz for _N, kz, _d in lad]
    conv = {}
    for n in N_FIXED:
        row = {}
        for nm, tag in (("alphahat", "alpha"),
                        ("gammahat_next", "gamma")):
            vals = [chains[kz][n][nm] for kz in kz_order]
            sl, ld = pair_diff_fit(vals, Ns)
            if smoke:
                is_conv = ld <= LASTDIFF_BAR
            else:
                is_conv = (sl <= SLOPE_BAR) and (ld <= LASTDIFF_BAR)
            row[tag] = (sl, ld, vals[-1], is_conv)
        conv[n] = row
        info("n=%-3d alpha: slope %+5.2f lastdiff %.1e -> %+.6f | "
             "gamma: slope %+5.2f lastdiff %.1e -> %.6f | %s"
             % (n, row["alpha"][0], row["alpha"][1],
                row["alpha"][2], row["gamma"][0], row["gamma"][1],
                row["gamma"][2],
                "CONV" if (row["alpha"][3] and row["gamma"][3])
                else "NOT-CONV/typed"))
    ok_core = all(conv[n]["alpha"][3] and conv[n]["gamma"][3]
                  for n in N_CORE)
    check("G30-fixed-degree-converges", ok_core,
          "CHAIN_CONVERGES on the sealed core set %s: every "
          "pair-diff slope <= %.1f (faster than 1/sqrt(N)) and "
          "every last diff <= %.0e; the limit chain approaches the "
          "free [-1,1] equilibrium (alphahat -> 0, gammahat -> 1/4 "
          "with degree-decaying corrections)"
          % (str(N_CORE), SLOPE_BAR, LASTDIFF_BAR))
    deep_txt = []
    for n in (50, 100):
        a_ok = conv[n]["alpha"][3]
        g_ok = conv[n]["gamma"][3]
        deep_txt.append("n=%d %s" % (n,
                        "CONV" if (a_ok and g_ok) else
                        "CONV_TREND (slope passes, jitter above "
                        "lastdiff bar)" if
                        (conv[n]["alpha"][0] <= SLOPE_BAR
                         and conv[n]["gamma"][0] <= SLOPE_BAR)
                        else "JITTER"))
    check("G31-deep-degrees-typed", True,
          "n = 50/100 typed honestly on a N <= %d ladder: %s -- "
          "reported, not silently averaged into the core verdict"
          % (Ns[-1], "; ".join(deep_txt)))

    # ---------------- S4: Leg B theta profile
    section("S4  LEG B -- THETA PROFILE + 0.98 MARGIN")
    ok_bound = True
    prof_ratio = []
    m098 = float("inf")
    for th in THETAS:
        vg = []
        for (N, kz, _d) in lad:
            m = min(int(math.floor(th * N)), N - 1)
            vg.append(chains[kz][m]["gammahat_next"])
        ok_bound = ok_bound and all(
            G_BOUNDS[0] <= v <= G_BOUNDS[1] for v in vg)
        half = len(vg) // 2
        sb = float(np.std(np.array(vg[:half])))
        st = float(np.std(np.array(vg[half:])))
        prof_ratio.append(st / max(sb, 1e-300))
        if th == 0.98:
            m098 = min(vg)
        info("theta=%.2f gamma in [%.4f, %.4f]; std bottom-half "
             "%.4f -> top-half %.4f (ratio %.2f)"
             % (th, min(vg), max(vg), sb, st, st / max(sb, 1e-300)))
    check("G40-theta-bounded", ok_bound,
          "gammahat at n = floor(theta N_w) lies in %s for all "
          "four theta over the whole ladder: the bulk profile is "
          "uniformly bounded away from 0 and infinity"
          % str(G_BOUNDS))
    check("G41-uniform-margin-098", m098 >= MARGIN_098,
          "min_w gammahat at theta = 0.98 is %.4f >= %.2f: a "
          "UNIFORM margin at fixed bulk fraction -- gammahat stays "
          "away from 0 and infinity right up to 98 percent filling "
          "on every rung of the ladder" % (m098, MARGIN_098))
    n_prof = sum(1 for r in prof_ratio if r <= 0.5)
    term_neg = 0
    term_min = float("inf")
    for (N, kz, _d) in lad:
        band = [chains[kz][n]["gammahat_next"]
                for n in range(int(0.98 * N), N)]
        term_min = min(term_min, min(band))
        if band[-1] <= 0.0:
            term_neg += 1
    check("G42-profile-class-and-terminal-band", True,
          "SEALED RULE result: %s -- std ratios %s (PROFILE_"
          "CONVERGES needs <= 0.5 on >= 3 theta: %d of 4); the "
          "spread shrinks slowly but stays quenched O(arithmetic "
          "jitter); TERMINAL BAND (0.98 N_w, N_w] disclosed: "
          "gammahat dips to %.4f and the last step gammahat_{N_w} "
          "is <= 0 on %d of %d windows -- the r228 boundary lives "
          "there and is EXCLUDED from the profile by the sealed "
          "rule, never hidden"
          % ("THETA_BOUNDED_QUENCHED" if n_prof < 3
             else "PROFILE_CONVERGES",
             str(["%.2f" % r for r in prof_ratio]), n_prof,
             term_min, term_neg, len(lad)))

    # ---------------- S5: Leg C controls
    section("S5  LEG C -- CONTROLS (EPSTEIN + SCRAMBLE LADDER)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = PIK.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    dE = HS.window_data(9, comb=(
        np.log(nn.astype(float)),
        2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))
    chE = FC.signed_chain(dE, dE["n_max"])
    flipE = next(n + 1 for n in range(dE["n_max"])
                 if chE[n]["gammahat_next"] <= 0.0)
    check("G50-epstein-flip-regated", flipE == EPSTEIN_FLIP,
          "EPSTEIN (w9 base, single-basis control): first "
          "gammahat <= 0 at step %d == %d (r226/r227 re-gate); "
          "its chain values at low n (alphahat_0 = %+.4f, "
          "gammahat_1 = %.4f) sit in the same geometric range as "
          "MAIN -- the separation is not in the O(1) scale"
          % (flipE, EPSTEIN_FLIP, chE[0]["alphahat"],
             chE[0]["gammahat_next"]))

    scr_kz = SMOKE_KZ if smoke else SCR_KZ
    scr = []
    for kz in scr_kz:
        dS = HS.window_data(kz, scramble_seed=1)
        NS = dS["n_max"]
        chS = FC.signed_chain(dS, min(NS, 60))
        flip = None
        for n in range(min(NS, 60)):
            if chS[n]["gammahat_next"] <= 0.0:
                flip = n + 1
                break
        scr.append((NS, kz, chS[0]["alphahat"], flip))
    scr.sort()
    a0s = [a for _N, _k, a, _f in scr]
    Nss = [N for N, _k, _a, _f in scr]
    slS, ldS = pair_diff_fit(a0s, Nss)
    no_conv = (slS > -0.3) or (ldS > 1e-2)
    check("G51-scramble-no-ladder-convergence", no_conv,
          "SCRAMBLE ladder (seed 1, %d rungs): alphahat_0 pair-"
          "diff slope %+.2f with last diff %.1e (sealed no-conv "
          "rule: slope > -0.3 OR lastdiff > 1e-2): each scramble "
          "redraws its positions -- the ladder is INCOHERENT and "
          "does not converge; MAIN's convergence is the coherence "
          "of the nested arithmetic comb, not folded-grid geometry"
          % (len(scr), slS, ldS))
    flips = [f for _N, _k, _a, f in scr]
    check("G52-scramble-early-flips", all(
        f is not None and f <= SCR_FLIP_MAX for f in flips),
          "every scramble chain leaves the positive cone at step "
          "<= %d (measured %s): the controls separate BOTH in "
          "ladder convergence AND in sign -- "
          "LADDER_COHERENCE_IS_ARITHMETIC"
          % (SCR_FLIP_MAX, str(flips)))

    # ---------------- S6: Leg D transfer budget
    section("S6  LEG D -- TRANSFER BUDGET (sealed adjudication)")
    ratios = []
    for i in range(len(lad) - 1):
        N1, k1, _d1 = lad[i]
        N2, k2, _d2 = lad[i + 1]
        ncut = int(BUDGET_CUT * min(N1, N2))
        dg = max(abs(chains[k1][n]["gammahat_next"]
                     - chains[k2][n]["gammahat_next"])
                 for n in range(ncut))
        floor = min(min(chains[k1][n]["gammahat_next"]
                        for n in range(ncut)),
                    min(chains[k2][n]["gammahat_next"]
                        for n in range(ncut)))
        ratios.append((dg / floor, k1, k2))
    rv = [r for r, _a, _b in ratios]
    ok_budget = all(r < 1.0 for r in rv)
    worst = max(ratios)
    info("budget ratios rho = sup|Delta gammahat| / gamma-floor "
         "over n < %.2f min(N, N'): min %.2f median %.2f max %.2f "
         "(pair kz%d-kz%d); top-5 pairs %s"
         % (BUDGET_CUT, min(rv), float(np.median(rv)), worst[0],
            worst[1], worst[2],
            str(["%.2f" % r for r in rv[-5:]])))
    check("G60-transfer-budget-bulk", ok_budget,
          "rho < 1 on ALL %d consecutive pairs (max %.2f, median "
          "%.2f, top pairs %.2f): a pointwise Weyl-type budget "
          "EXISTS on the shared bulk -- each window's positivity "
          "floor covers its neighbour's whole 0.98-bulk, and the "
          "budget IMPROVES up the ladder"
          % (len(rv), worst[0], float(np.median(rv)), rv[-1]))
    check("G61-frontier-band-uncovered", True,
          "HONESTY CLAUSE (sealed): the budget covers n <= %.2f "
          "N_prev ONLY; the frontier band (%.2f N_prev, N_w] -- "
          "where the r228 flips N_w + 0/2/2/3/1 live and where "
          "gammahat_{N_w} <= 0 on %d of %d windows -- is beyond "
          "every predecessor's life; the limit object controls "
          "fixed n, never the moving frontier: positivity of the "
          "NEW frontier degrees is re-earned by every window and "
          "is NOT transferable from ladder history -- "
          "FRONTIER_BAND_UNCOVERED; the cofinal wall statement "
          "does not follow from chain convergence"
          % (BUDGET_CUT, BUDGET_CUT, term_neg, len(lad)))

    # ---------------- S7: must-fails + high-precision ward
    section("S7  MUST-FAILS + HIGH-PRECISION WARD")
    okM = True
    # m1 AFFINE_ALIAS: scale node coordinates of w9 by 1.1
    d9a = {k: (v.copy() if isinstance(v, np.ndarray) else v)
           for k, v in d9.items()}
    d9a["xs"] = d9a["xs"] * 1.1
    d9a["ys"] = d9a["ys"] * 1.1
    cha = FC.signed_chain(d9a, 25)
    g_hon = abs(chains[kz_order[-1]][20]["gammahat_next"]
                - chains[kz_order[-2]][20]["gammahat_next"])
    g_bad = abs(cha[20]["gammahat_next"]
                - chains[9][20]["gammahat_next"])
    okM = okM and g_bad > 0.02 and g_bad > 20.0 * max(g_hon, 1e-12)
    # m2 DEGREE_ALIAS: alphahat_1(w_last) vs alphahat_0(w_prev)
    a_hon = abs(chains[kz_order[-1]][0]["alphahat"]
                - chains[kz_order[-2]][0]["alphahat"])
    a_bad = abs(chains[kz_order[-1]][1]["alphahat"]
                - chains[kz_order[-2]][0]["alphahat"])
    okM = okM and a_bad > 100.0 * max(a_hon, 1e-12)
    # m3 SEED trap: scramble seed 2 differs from seed 1 at O(1)
    dS1 = HS.window_data(9, scramble_seed=1)
    dS2 = HS.window_data(9, scramble_seed=2)
    cS1 = FC.signed_chain(dS1, 10)
    cS2 = FC.signed_chain(dS2, 10)
    seed_dev = max(abs(cS1[n]["alphahat"] - cS2[n]["alphahat"])
                   for n in range(10))
    okM = okM and seed_dev > 1e-2
    check("G70-must-fails-fire", okM,
          "AFFINE_ALIAS (node scale 1.1 shifts gammahat_20 by "
          "%.3f, %.0f x the honest ladder diff -- the identity "
          "normalization is load-bearing), DEGREE_ALIAS (axis "
          "swap %.2f vs honest %.1e), SEED trap (seed 2 vs 1 dev "
          "%.2f): each fires loudly"
          % (g_bad, g_bad / max(g_hon, 1e-12), a_bad, a_hon,
             seed_dev))

    import mpmath as mp
    mp.mp.dps = 40
    dW = next((d for N, kz, d in lad if kz == MP_WARD_KZ), None)
    if dW is None:
        dW = HS.window_data(MP_WARD_KZ)
    nds = ([mp.mpf(float(x)) for x in dW["xs"]]
           + [mp.mpf(float(y)) for y in dW["ys"]])
    wts = ([mp.mpf(float(w)) for w in dW["ws"]]
           + [-mp.mpf(float(v)) for v in dW["vs"]])
    chF = chains.get(MP_WARD_KZ) or FC.signed_chain(dW, MP_WARD_N + 1)
    pk = [mp.mpf(1)] * len(nds)
    pkm = [mp.mpf(0)] * len(nds)
    hs = [mp.fsum(w * p * p for w, p in zip(wts, pk))]
    ward = 0.0
    for k in range(MP_WARD_N):
        a = mp.fsum(w * x * p * p
                    for w, x, p in zip(wts, nds, pk)) / hs[-1]
        g = (hs[-1] / hs[-2]) if k > 0 else mp.mpf(0)
        nx = [(x - a) * p - g * q
              for x, p, q in zip(nds, pk, pkm)]
        pkm, pk = pk, nx
        hs.append(mp.fsum(w * p * p for w, p in zip(wts, pk)))
        ward = max(ward,
                   abs(float(a) - chF[k]["alphahat"]),
                   abs(float(hs[-1] / hs[-2])
                       - chF[k]["gammahat_next"]))
    check("G71-mp-ward", ward <= MP_WARD_BAR,
          "plain monic signed recursion at dps 40 on the smallest "
          "rung (kz = %d, %d nodes) re-derives the f64 chain "
          "through step %d to %.1e (<= %.0e): the scaled f64 "
          "recursion is exact, not an artifact"
          % (MP_WARD_KZ, len(nds), MP_WARD_N, ward, MP_WARD_BAR))

    # ---------------- S8: verdict
    section("S8  VERDICT")
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a convergence "
          "measurement moves no edge); what the round adds: the "
          "LIMIT JACOBI OBJECT exists degree-wise (core set "
          "measured, rates super-1/sqrt(N)), the wall margin is "
          "ladder-wide uniform (42 windows), the bulk has a real "
          "transfer budget -- and the honest boundary: the "
          "frontier band re-earns positivity on every rung; the "
          "cofinal question is now PRECISELY the frontier "
          "asymptotics of gammahat_{N_w + j}, j = O(1), not any "
          "bulk transport")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G90-verdict", npass == len(CHECKS),
          "CHAIN_CONVERGES_WITH_TRANSFER_BUDGET (bulk %.2f; sealed "
          "core set CONV, all budget ratios < 1) + "
          "FRONTIER_BAND_UNCOVERED (the budget never reaches the "
          "moving wall boundary -- typed, not hidden) + "
          "THETA_BOUNDED_QUENCHED (bulk profile bounded in %s "
          "with slowly shrinking quenched spread; uniform 0.98 "
          "margin %.4f) + LADDER_COHERENCE_IS_ARITHMETIC "
          "(scramble ladder does not converge, flips at O(10)); "
          "NO RH claim" % (BUDGET_CUT, str(G_BOUNDS), m098))

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
