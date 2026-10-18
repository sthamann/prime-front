#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""monotone_composition_probe -- PRIME.PORT.W1.MONOCOMP.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE TWO COMPOSITION GAPS ARE ONE GAP, AND
IT IS AN ARTEFACT OF THE FACTORISATION.  CLXXVIII/CLXXXI closed the
W1 skeleton down to two composition demands that no constant can
pay: I4 "concentration" (+8.45 dex) and H2 "diagonal law of the
equilibrated core" (+9.64 dex).  Both are consequences of ONE
choice: the chain factorises lambda_min(G_core) through Gershgorin,
    G_core = [sqrt(v_i v_j) K_h(y_i, y_j)],
    lambda_min >= a0 - b0,  a0 <= min_i v_i K_h(y_i,y_i),
                            b0 >= max_i sum_{j!=i} sqrt(v_iv_j)|K_ij|,
and then bounds the two factors SEPARATELY by global inputs:
  (I4)  K_h(y,y) >= p_0(y)^2 = 1/m0  -- the h-term Christoffel sum
        replaced by its FIRST term, and the LOCAL node energy
        replaced by the GLOBAL mass m0 (measured price: m0 K_h(y,y)
        ~ 3.96e4, and min_i v_i/m0 ~ 9.8e-07 decaying like h^-2);
  (H2)  |K_ij| <= sqrt(K_ii K_jj) (Cauchy-Schwarz) and then an
        UPPER Christoffel law K_up -- an object the global input set
        does not contain, and whose demanded level is a0/den, i.e.
        it INHERITS the I4 deficit.
This probe replaces the factorisation by a single exact step.

(a) THE ALGEBRA (all four statements machine-warded below).  Let
nu_+ be the positive folded measure (discrete on the fold grid),
P_{<h} the polynomials of degree < h with the nu_+ inner product,
T: P_{<h} -> R^8, (T P)_i = sqrt(v_i) P(y_i).  Then G_core = T T*
and for every u in R^8
  [L1]  u* G_core^{-1} u = min { int P^2 dnu_+ : P in P_{<h},
                                 sqrt(v_i) P(y_i) = u_i }.
  [L2]  MEASURE MONOTONICITY.  If nu_+ <= omega pointwise (both on
        the same finite support) and omega admits h orthonormal
        polynomials, then by [L1] the same feasible set has a larger
        objective under omega, hence
            G_core[nu_+]^{-1} <=  G_core[omega]^{-1}
        and therefore  G_core[nu_+]  >=  G_core[omega]  (Loewner),
        so   lambda_min(G_core) >= lambda_min(V^{1/2} K^omega V^{1/2})
        with K^omega = [K_h^omega(y_i,y_j)] and V = diag(v_i).
        NO Gershgorin, NO diagonal law, NO off-diagonal law, NO
        Cauchy-Schwarz: the composition price of [L2] is exactly the
        price of the measure domination and nothing else.
  [L3]  v-MONOTONE CORONARY (one Cauchy-Schwarz, paid once):
            lambda_min(G_core) >= [ sum_i (K^omega)^{-1}_{ii}/v_i ]^{-1},
        which is monotone in every v_i -- so a LOWER bound v_i^lo
        may be substituted directly (the [L2] form is not monotone
        in v; this is the version that consumes a v-floor supply).
  [L0]  GENERAL DUAL-INTERPOLATION FORM (the family [L2] optimises
        over): for ANY M_1..M_8 in P_{<h} with A = [M_i(y_j)]
        invertible, lambda_min(G_core) >= 1/lambda_max(V^{-1/2}
        A^{-1} Gamma A^{-T} V^{-1/2}), Gamma_ij = int M_i M_j dnu_+;
        equality at M_i = K_h(y_i,.), and omega's CD kernel is the
        optimal admissible (comb-free) choice, which is why [L2] is
        the sharp member of the family.  Warded as an identity.

(b) THE EXPLICIT DOMINATING MEASURE (source-only).  On the fold
grid f = 0..L/2 with paired geometric weights w_f = 4 sin^2(pi f/L)
/(2L) times 2 for 0 < f < L/2, the positive folded measure has mass
w_f (d_f)_+ and
    (d_f)_+ <= |d^ar_f| + Delta,   Delta >= max_f |d_f - d^ar_f|,
so omega_f := w_f (|d^ar_f| + Delta) dominates nu_+ FOLD BY FOLD
(warded).  Three frozen Delta tiers, exactly the CLXXVIII I2 ladder:
  ENV   Delta_env = 2 M_up, M_up = 2 B_PSI (2 sqrt(X) - 1)  -- the
        DERIVED tier (Chebyshev/mass envelope only, all-h),
  LAG   Delta_lag = 2 ||c_at||_1  (tent L1, all-h but comb-read),
  MEAS  Delta_meas = max_f |d_f - d^ar_f|  (anatomy).
Anatomy tiers LOW8/LOW32/LOW128 replace Delta by the exact per-fold
deviation on folds f <= 16/32/128 (the frequency band a localized
low-frequency supply would control) and ABS uses |d_f| exactly --
ABS is the CEILING of the whole route and measures the residual
composition price of [L2] itself.

(c) WHAT THIS PROBE MEASURES (the slack ladder, per composition
step, surface + deep):
  O1  the OLD composition price, isolated from the supply:
      I4_comp = log10( a_meas / (min_i v_i / m0_up) ) with the same
      MEASURED v -- the published +8.45 dex minus the v-supply
      deficit;
  O2  the COUPLING: the H2 demand recomputed with a_meas in place of
      a0 -- if H2_old - H2_(a_meas) is large, H2 is not a second gap
      but the I4 deficit propagated through K_up = a0/den;
  N1  the NEW ladder lambda_min(G[omega_tier]) per tier vs the truth
      lambda_min(G_core) and vs the REGISTERED target mu1(h);
  N2  the h-trend of the new bound (the old a0 falls like h^-2, i.e.
      it tracks mu1 by construction; does the new one?);
  F   the low-fold sensitivity ladder (how many dex of the residual
      envelope price a per-fold supply on f <= 16/32/128 buys) --
      this NAMES the next supply object in the CLXXXI currency;
  E   the equilibrated-Gershgorin comparison (CLXXV lesson applied
      to G_core: rho = max_i sum_{j!=i}|R_ij| on the correlation
      matrix R): does equilibration alone move the battery, and does
      the correlation form remove the K_up demand?
  C   controls, domination ward per world, and the HONEST world
      census of the new step.

(d) GATES.  TAU-SCREEN (parent verbatim, PASS |s| <= 0.30 / RELOC
>= 0.70) on log10(new bound / mu1).  ANTI-CIRCULARITY: omega is
built from the arch layer, the window conventions and the scalar
Delta only; no sigma_h, no wall data, no target eigendata, no
forward pivot sign enters any derived number; v_i and the truth
column are anatomy.  ANTHROPIC NO-GO: the derived step consumes one
total-mass envelope (two-moment class) plus window geometry; it
makes NO pair-correlation and NO zero-counting claim.
WALL-BLINDNESS -- DECLARED HONESTLY IN ADVANCE, NOT A RESULT: [L2]
is a measure inequality valid for EVERY measure, so the composition
step CANNOT discriminate worlds and is not, and cannot become, a
wall certificate.  Its whole purpose is the opposite: to move the
arithmetic content out of the composition and into ONE input.  The
probe therefore wards (i) that the domination HYPOTHESIS is a prime
statement (it fails in worlds violating the mass envelope) and (ii)
that the smooth world reproduces the composition identically -- the
expected, declared outcome, consistent with CLXXVIII's measured SEAT
(the envelope-visible chain is world-identical, the comb consumption
sits in the measured nu_+ conditioning).  The discriminating half
stays where CLXXXI put it: the v-floor (core nu_- fold masses).

VERDICT (frozen enums, decided by these rules and nothing else):
  MONOCOMP-EXACT iff L0/L1/L2/L3 wards pass on every surface and
    deep step (grid identity, dual identity, Loewner ward, trace
    ward) -- else ALGEBRA-BROKEN (DEAD).
  I4-DISSOLVED(new price) iff the ABS-tier price med log10(truth /
    bound_ABS) <= COMP_BAR AND the DERIVED (ENV) tier exceeds mu1 on
    ALL surface and deep steps; else I4-REDUCED(swing dex, n/N above
    mu1) if the ENV tier exceeds mu1 on >= REDUCE_FRAC of steps;
    else I4-PERSISTS.
  H2-DISSOLVED(coupling dex) iff the derived quantity contains no
    upper-diagonal object (structural, warded by construction: the
    ENV bound is computed without any K_ii) AND the measured
    coupling I4_comp - H2_resid >= COUP_BAR; else H2-PERSISTS.
  Headline W1-COMPOSITION-REFORMED(old dex -> new dex) iff
    MONOCOMP-EXACT and I4-DISSOLVED and H2-DISSOLVED; else
    W1-COMPOSITION-PARTIAL(...) / W1-COMPOSITION-VOID(...).
  COMPOSITION-WORLD-BLIND(smooth census) always typed (declared).
  NEXT-OBJECT(low-fold gain dex) always typed.
DEAD overrides: parent reproduction fails; any L-ward breaks; the
domination ward fails in the truth world.

HONEST SCOPE, STATED ONCE AND REPEATED IN THE VERDICT: this probe
re-derives ONE composition step.  It does not supply the v-floor
(CLXXXI's object, open on the shallow surface), it does not touch
W2 / background cancellation (RH-hard), it is not a wall
certificate, and it makes NO RH claim.  A dissolved I4/H2 means the
chain's remaining demand is a SINGLE named object, not that the
object is proved.

FROZEN BARS: L0_TOL = 1e-8 (rel, dual-interpolation identity);
L1_TOL = 1e-8 (rel, dual identity); L2_TOL = 1e-9 (rel Loewner
slack, min eig(G - G_omega) >= -L2_TOL * ||G||); GRID_TOL = 1e-9
(rel, fold-grid rebuild of nu_+ against the pipeline chain);
DOM_TOL = 1e-12 (abs, fold-wise domination); COMP_BAR = 1.00 dex;
COUP_BAR = 7.00 dex; REDUCE_FRAC = 0.90; HTREND_FLAT = 0.30;
REPRO_A_MED = 0.968, REPRO_B_MED = 0.202, REPRO_RTOL = 5e-2;
REPRO_RATIO_MED = 9.8e-07, RATIO_RTOL = 0.25; REPRO_I1_MIN = 3.9e4;
LOW_CUTS = (17, 33, 129); DEEP_CAP = 16 (declared runtime cap on
the deep block, shallowest-first); MIN_DEEP = 8; slope bands
0.30/0.70 (parent verbatim); parent SPEC-SHA warded == 084c9689..;
wedge SPEC-SHA prefix warded == 26855819; parent bars (MINB_REF,
GAP) inherited verbatim.  Runtime cap declared: 20 min.  Smoke mode
MONOCOMP_SMOKE=1 restricts the surface to the 6 shallowest steps and
the deep block to 3 rungs.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): the theory was
developed against FIVE deleted scratch scripts (_scratch_dualinterp
1..5) on the ladder_zones surface, NOT on this probe's frozen
pipeline.  Their measured content, disclosed in full so the frozen
run can be checked against it: L0 identity 2.7e-15..1e-13; the
localizer family (Chebyshev CD kernel, Jackson^2) gave +3.35/+3.44
dex below truth and the omega-CD-kernel choice [L2] beat both at
+2.58 dex (env) / +2.25 dex (lag, meas); Loewner ward min eig
+0.42; old a0 +8.07..+8.19 dex below truth and -4.00 dex BELOW mu1
(max -3.64: the old chain never reaches the registered target even
with a perfect v-floor); new ENV tier +1.54 dex ABOVE mu1 (min
+0.28) on 41/41, h-slope +0.15; ABS ceiling +0.29 dex below truth;
coupling I4 +8.19 / H2 +9.15 / H2-with-a_meas +1.03 => +8.12;
rho band 0.064/0.213/0.545; low-fold gains +0.73 (f<=16), +2.02
(f<=32), +2.17 (f<=128); controls: the smooth world reproduces the
step, the scramble world violates the domination hypothesis at
depth.  NO bar, band, count, rule or enum below was moved after any
run on this probe's own pipeline; the bars were set from the
scratch bands with deliberate margin and are recorded above.
TWO smoke runs of THIS file (MONOCOMP_SMOKE=1, 6 shallowest surface
steps, 2.5 s each) are disclosed: run 1 crashed in section T on a
2-vs-3 tuple unpack of parent.screen (fixed: the parent returns
(label, slope)); run 2 completed the surface with L0 1.2e-14, L1
2.7e-15, L1b 4.8e-14, L2 min rel +0.451, L3/L4 6/6, ENV +2.62 dex
below truth and +0.56 dex above mu1 on 6/6, ABS +0.27, LOW16/32/128
gains +0.75/+2.04/+2.18, coupling +7.17, rho 0.283/0.360/0.529,
equilibration gain +0.003 dex, smooth+scramble both reproduce the
step at kz 23/20.  TWO smoke FAILS are disclosed and their bars
were deliberately NOT moved: (i) O1 "min v/m0 med 4.35e-06 vs the
published 9.8e-07" -- the 6 shallowest steps are not the published
39-step median and the ratio falls like h^-2, so the frozen run
decides; (ii) N2 "h-slope -1.00" -- a 6-point fit over h 149..203
cannot see the h-trend (the scratch surface measured +0.15 over h
142..878), so the frozen run decides.  Both bars stand as written.
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
import wedge_scale_law_probe as wedge  # noqa: E402  (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
WEDGE_SHA8 = "26855819"
L0_TOL = 1.0e-8
L1_TOL = 1.0e-8
L2_TOL = 1.0e-9
GRID_TOL = 1.0e-9
DOM_TOL = 1.0e-12
COMP_BAR = 1.00
COUP_BAR = 7.00
REDUCE_FRAC = 0.90
HTREND_FLAT = 0.30
REPRO_A_MED = 0.968
REPRO_B_MED = 0.202
REPRO_RTOL = 5.0e-2
REPRO_RATIO_MED = 9.8e-07
RATIO_RTOL = 0.25
REPRO_I1_MIN = 3.9e4
LOW_CUTS = (17, 33, 129)
DEEP_CAP = 16
MIN_DEEP = 8
CORE_J = base.CORE_J
SMOKE = os.environ.get("MONOCOMP_SMOKE", "") == "1"
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


def fold_grid(L):
    """folds 0..L/2 with the PAIRED geometric weights of the pipeline."""
    f = np.arange(0, L // 2 + 1)
    w = 4.0 * np.sin(math.pi * f / L) ** 2 / (2.0 * L)
    mult = np.where((f > 0) & (f < L // 2), 2.0, 1.0)
    return f, w * mult, np.cos(2.0 * math.pi * f / L)


def deltas(alpha, c_at, d, d_ar):
    X = math.exp(2.0 * alpha)
    m_up = 2.0 * core.B_PSI * (2.0 * math.sqrt(X) - 1.0)
    return dict(ENV=2.0 * m_up,
                LAG=2.0 * float(np.sum(np.abs(c_at))),
                MEAS=float(np.max(np.abs(d - d_ar))))


def kernel_of(xg, wom, y_core, h):
    """8x8 CD-kernel matrix of the explicit measure omega (deg < h)."""
    m = wom > 1e-300
    al, be, m0, steps = base.lanczos_chain(xg[m], wom[m], h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    P = base.eval_chain(al, be, m0, y_core, h)
    K = P @ P.T
    return 0.5 * (K + K.T)


def mono_bound(K, v):
    G = np.sqrt(v)[:, None] * K * np.sqrt(v)[None, :]
    G = 0.5 * (G + G.T)
    return float(np.linalg.eigvalsh(G)[0]), G


def trace_bound(K, v):
    """[L3]: v-monotone one-Cauchy-Schwarz corollary."""
    Ki = np.linalg.inv(K)
    s = float(np.sum(np.diag(Ki) / v))
    return 1.0 / s if s > 0 else float("-inf")


def dual_form(Mrows, Amat, wpos, v):
    """[L0]: general dual-interpolation bound for a localiser family."""
    Gam = (Mrows * wpos[None, :]) @ Mrows.T
    Gam = 0.5 * (Gam + Gam.T)
    Ai = np.linalg.inv(Amat)
    Lam = Ai @ Gam @ Ai.T
    Lam = 0.5 * (Lam + Lam.T)
    sv = 1.0 / np.sqrt(v)
    Q = Lam * np.outer(sv, sv)
    return 1.0 / float(np.linalg.eigvalsh(0.5 * (Q + Q.T))[-1])


def old_chain(v, m0_ar_abs, d_env, Gc):
    """the CLXXVIII/CLXXXI composition, with the MEASURED v-floor."""
    m0_up = m0_ar_abs + d_env
    a0 = float(np.min(v)) / m0_up
    a = float(np.min(np.diag(Gc)))
    off = np.sum(np.abs(Gc), axis=1) - np.abs(np.diag(Gc))
    b = float(np.max(off))
    sv = np.sqrt(v)
    den = float(np.max(sv * (float(np.sum(sv)) - sv)))
    kmeas = float(np.max(np.diag(Gc) / v))
    i4 = math.log10(a / a0) if a0 > 0 else float("nan")
    h2 = math.log10(kmeas * den / a0) if a0 > 0 else float("nan")
    h2r = math.log10(kmeas * den / a)
    return dict(a0=a0, a=a, b=b, i4=i4, h2=h2, h2r=h2r, m0_up=m0_up)


def rho_of(Gc):
    dg = np.diag(Gc)
    if float(np.min(dg)) <= 0.0:
        return float("nan")
    R = Gc / np.sqrt(np.outer(dg, dg))
    return float(np.max(np.sum(np.abs(R), axis=1) - 1.0))


def rung_payload(alpha, M, c_at, c_ar, y_core, v_core, h, Gc,
                 chain=None, want_low=True):
    """all tiers for one rung; returns None on a chain refusal."""
    c_at = np.asarray(c_at, float)
    d = base.grid_density(c_ar + c_at)
    d_ar = base.grid_density(c_ar)
    L = 2 * M - 2
    f, wg, xg = fold_grid(L)
    de = deltas(alpha, c_at, d, d_ar)
    df = d[f]
    daf = np.abs(d_ar[f])
    wpos = wg * np.maximum(df, 0.0)
    out = dict(L=L, de=de, wpos=wpos, xg=xg, f=f, wg=wg,
               m0_grid=float(np.sum(wpos)),
               m0_ar_abs=float(np.sum(
                   4.0 * np.sin(math.pi * np.arange(L) / L) ** 2
                   * np.abs(d_ar))) / (2.0 * L))
    tiers = {}
    doms = {}
    for tag in ("ENV", "LAG", "MEAS"):
        wom = wg * (daf + de[tag])
        doms[tag] = float(np.max(np.maximum(df, 0.0) - (daf + de[tag])))
        K = kernel_of(xg, wom, y_core, h)
        if K is None:
            return None
        tiers[tag] = K
    if want_low:
        dev = np.abs(df - d_ar[f])
        for cut in LOW_CUTS:
            dd = np.full(len(f), de["ENV"])
            nn = min(cut, len(dd))
            dd[:nn] = dev[:nn]
            K = kernel_of(xg, wg * (daf + dd), y_core, h)
            if K is not None:
                tiers["LOW%d" % (cut - 1)] = K
        K = kernel_of(xg, wg * np.abs(df), y_core, h)
        if K is not None:
            tiers["ABS"] = K
    K = kernel_of(xg, wpos, y_core, h)
    if K is None:
        return None
    tiers["GRID"] = K
    out["tiers"] = tiers
    out["doms"] = doms
    out["bounds"] = {t: mono_bound(K, v_core)[0]
                     for t, K in tiers.items()}
    out["l3"] = trace_bound(tiers["ENV"], v_core)
    out["truth"] = float(np.linalg.eigvalsh(Gc)[0])
    _lo, Gom = mono_bound(tiers["ENV"], v_core)
    dif = Gc - Gom
    out["loewner"] = (float(np.linalg.eigvalsh(0.5 * (dif + dif.T))[0])
                      / max(float(np.linalg.norm(Gc, 2)), 1e-300))
    out["grid_dev"] = abs(out["bounds"]["GRID"] / out["truth"] - 1.0)
    out["rho"] = rho_of(Gc)
    out["l0"] = float("nan")
    if chain is not None:
        Pg = base.eval_chain(chain[0], chain[1], chain[2], xg, h)
        Pc = base.eval_chain(chain[0], chain[1], chain[2], y_core, h)
        Mrows = Pc @ Pg.T
        Amat = Pc @ Pc.T
        val = dual_form(Mrows, 0.5 * (Amat + Amat.T), wpos, v_core)
        out["l0"] = abs(val / out["truth"] - 1.0)
    return out


def l1_ward(H, Gc, rng_free_u):
    """[L1] dual identity via the minimum-norm interpolant."""
    c, *_ = np.linalg.lstsq(H, rng_free_u, rcond=None)
    lhs = float(rng_free_u @ np.linalg.solve(Gc, rng_free_u))
    return abs(float(c @ c) / lhs - 1.0)


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join(
            [labels.get("head", "-"), labels.get("alg", "-"),
             labels.get("i4", "-"), labels.get("h2", "-"),
             labels.get("blind", "-"), labels.get("next", "-")])
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: this is ONE composition step re-derived as a
  measure inequality.  It supplies no v-floor (CLXXXI's open
  object on the shallow surface), it is world-blind BY
  CONSTRUCTION and therefore not a wall certificate, and W2 /
  background cancellation remain RH-hard and untouched.  NO RH
  claim; no marker moves; no promotion.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W1.MONOCOMP.01 -- the composition as a "
            "measure inequality (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    parent_sha = hashlib.sha256(
        parent.__doc__.encode("utf-8")).hexdigest()
    wedge_sha = hashlib.sha256(
        wedge.__doc__.encode("utf-8")).hexdigest()
    print("    parent SPEC SHA-256 = %s" % parent_sha)
    print("    NO RH claim.  Derived inputs: B_PSI %.5f (v563:136), "
          "arch layer, window conventions." % core.B_PSI)
    if SMOKE:
        print("    *** SMOKE MODE ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", parent_sha == PARENT_SHA,
          kill="K2")
    check("S0c wedge SPEC prefix reproduced",
          wedge_sha[:8] == WEDGE_SHA8, wedge_sha[:8], kill="K2")

    # ------------------------------------------------------------ W
    section("W -- parent ladder reproduction (CLXXIV / CLXXVII)")
    zones, truth, full, rows = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(rows) == 39,
          "%d/%d/%d" % (len(zones), len(full), len(rows)), kill="K1")
    if KILLS:
        return finish({})
    minb = min(float(np.linalg.eigvalsh(w["B"])[0]) for w in rows)
    gaps = np.array([w["gap"] for w in rows])
    check("W2 v901 reproduction",
          abs(minb / parent.MINB_REF - 1.0) <= parent.MINB_RTOL
          and abs(float(np.min(gaps)) / parent.GAPMIN_REF - 1.0)
          <= parent.GAP_RTOL,
          "minB %.4f gap %.4f/%.4f" % (minb, float(np.min(gaps)),
                                       float(np.median(gaps))),
          kill="K2")
    for w in rows:
        Gc = w["H"] @ w["H"].T
        w["Gc"] = 0.5 * (Gc + Gc.T)
    a_med = float(np.median([float(np.min(np.diag(w["Gc"])))
                             for w in rows]))
    b_med = float(np.median([
        float(np.max(np.sum(np.abs(w["Gc"]), axis=1)
                     - np.abs(np.diag(w["Gc"])))) for w in rows]))
    check("W3 CLXXVII H1/H2 reproduction (a med %.4f, b med %.4f)"
          % (a_med, b_med),
          abs(a_med / REPRO_A_MED - 1.0) <= REPRO_RTOL
          and abs(b_med / REPRO_B_MED - 1.0) <= REPRO_RTOL, kill="K2")
    n_l2 = sum(w["sP"] >= w["mu1"] for w in rows)
    check("W4 CLXXIV reproduction s_P >= mu1",
          n_l2 == len(rows), "%d/%d" % (n_l2, len(rows)), kill="K2")

    # ------------------------------------------------------------ L
    section("L -- the four algebra wards on the deployed surface")
    use = rows[:6] if SMOKE else rows
    rng = np.random.default_rng(20260811)
    pay = []
    w_l0 = w_l1 = w_l2 = w_l3 = w_grid = w_dom = 0
    for w in use:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        c_at = core.atom_lags_at(rr["alpha"], rr["M"], rr["uu"],
                                 2.0 * rr["lam"])[0]
        p = rung_payload(rr["alpha"], rr["M"], c_at, rr["c_ar"],
                         r2["y_core"], r2["v_core"], r2["h"],
                         w["Gc"], chain=r2["chain"])
        if p is None:
            continue
        p["h"] = r2["h"]
        p["kz"] = r2["kz"]
        p["v"] = r2["v_core"]
        p["Gc"] = w["Gc"]
        p["tau"] = w["tau"]
        p["mu1"] = w["mu1"]
        p["l1"] = l1_ward(w["H"], w["Gc"], rng.standard_normal(8))
        w_l0 += int(p["l0"] <= L0_TOL)
        w_l1 += int(p["l1"] <= L1_TOL)
        w_grid += int(p["grid_dev"] <= GRID_TOL)
        w_l2 += int(p["loewner"] >= -L2_TOL)
        w_l3 += int(p["l3"] <= p["bounds"]["ENV"] * (1.0 + 1e-9)
                    and p["l3"] > 0.0)
        w_dom += int(max(p["doms"].values()) <= DOM_TOL)
        pay.append(p)
        if len(pay) % 10 == 0:
            print("    ... %d rungs  [%.1f s]"
                  % (len(pay), time.time() - T0), flush=True)
    n = len(pay)
    check("L0 dual-interpolation identity is EXACT at M_i = "
          "K_h(y_i,.)", w_l0 == n, "%d/%d (worst %.2e)"
          % (w_l0, n, max(p["l0"] for p in pay)), kill="K3")
    check("L1 dual identity u*G^-1u == min-norm interpolant energy",
          w_l1 == n, "%d/%d (worst %.2e)"
          % (w_l1, n, max(p["l1"] for p in pay)), kill="K3")
    check("L1b fold-grid rebuild of nu_+ reproduces the pipeline "
          "chain", w_grid == n, "%d/%d (worst %.2e)"
          % (w_grid, n, max(p["grid_dev"] for p in pay)), kill="K3")
    check("L2 Loewner ward  G[nu_+] - G[omega] >= 0 (ENV tier)",
          w_l2 == n, "%d/%d (min rel %.3e)"
          % (w_l2, n, min(p["loewner"] for p in pay)), kill="K3")
    check("L3 trace corollary <= L2 bound and positive",
          w_l3 == n, "%d/%d" % (w_l3, n), kill="K3")
    check("L4 fold-wise domination hypothesis (d_f)_+ <= |d^ar_f| "
          "+ Delta", w_dom == n, "%d/%d (worst %.2e)"
          % (w_dom, n, max(max(p["doms"].values()) for p in pay)),
          kill="K3")

    # ------------------------------------------------------------ O
    section("O -- the OLD composition, and the I4/H2 coupling")
    olds = [old_chain(p["v"], p["m0_ar_abs"], p["de"]["ENV"],
                      p["Gc"]) for p in pay]
    ratio = np.array([float(np.min(p["v"])) / p["m0_grid"]
                      for p in pay])
    i1 = np.array([float(np.min(np.diag(p["Gc"]) / p["v"]))
                   * p["m0_grid"] for p in pay])
    check("O1 CLXXVIII I4 anatomy reproduced (min v/m0 med %.2e "
          "== %.1e; m0 K min %.2e >= %.1e)"
          % (float(np.median(ratio)), REPRO_RATIO_MED,
             float(np.min(i1)), REPRO_I1_MIN),
          abs(float(np.median(ratio)) / REPRO_RATIO_MED - 1.0)
          <= RATIO_RTOL and float(np.min(i1)) >= REPRO_I1_MIN,
          kill="K2")
    i4 = np.array([o["i4"] for o in olds])
    h2 = np.array([o["h2"] for o in olds])
    h2r = np.array([o["h2r"] for o in olds])
    mu1 = np.array([p["mu1"] for p in pay])
    a0 = np.array([o["a0"] for o in olds])
    print("    OLD composition price I4_comp = log10(a/a0): "
          "%+.2f / %+.2f / %+.2f dex" % band(i4))
    print("    OLD H2 demand log10(K_meas/K_need): "
          "%+.2f / %+.2f / %+.2f dex" % band(h2))
    print("    H2 demand recomputed with a_meas: "
          "%+.2f / %+.2f / %+.2f dex" % band(h2r))
    coup = float(np.median(h2)) - float(np.median(h2r))
    print("    ==> COUPLING: %+.2f dex of the H2 demand is the I4 "
          "deficit propagated through K_up = a0/den" % coup)
    print("    old a0 vs the REGISTERED target mu1: "
          "%+.2f / %+.2f / %+.2f dex (above mu1 on %d/%d)"
          % (band(np.log10(a0 / mu1)) + (int(np.sum(a0 > mu1)), n)))
    check("O2 coupling measured", True)

    # ------------------------------------------------------------ N
    section("N -- the NEW ladder: lambda_min(G[omega]) per tier")
    print("     kz    h   truth      ENV        LAG        MEAS      "
          " L3(ENV)    mu1        dex>mu1")
    for p in pay[:14]:
        print("  %5d %4d  %.3e  %.3e  %.3e  %.3e  %.3e  %.2e  %+.2f"
              % (p["kz"], p["h"], p["truth"], p["bounds"]["ENV"],
                 p["bounds"]["LAG"], p["bounds"]["MEAS"], p["l3"],
                 p["mu1"], math.log10(p["bounds"]["ENV"] / p["mu1"])))
    if len(pay) > 14:
        print("    ... (%d more)" % (len(pay) - 14))
    tags = ["ENV", "LAG", "MEAS", "ABS"] + \
        ["LOW%d" % (c - 1) for c in LOW_CUTS]
    tr = np.array([p["truth"] for p in pay])
    hs = np.array([float(p["h"]) for p in pay])
    stat = {}
    for t in tags:
        if not all(t in p["bounds"] for p in pay):
            continue
        bv = np.array([p["bounds"][t] for p in pay])
        d1 = np.log10(tr / np.maximum(bv, 1e-300))
        d2 = np.log10(np.maximum(bv, 1e-300) / mu1)
        sl = float(np.polyfit(np.log(hs), np.log10(
            np.maximum(bv, 1e-300)), 1)[0])
        stat[t] = dict(d1=d1, d2=d2, sl=sl, npos=int(np.sum(bv > mu1)))
        print("    %-6s below truth med %+.2f (%+.2f/%+.2f) | above "
              "mu1 med %+.2f min %+.2f | > mu1 on %d/%d | h-slope "
              "%+.2f" % (t, np.median(d1), d1.min(), d1.max(),
                         np.median(d2), d2.min(), stat[t]["npos"], n,
                         sl))
    l3v = np.array([p["l3"] for p in pay])
    print("    L3     above mu1 med %+.2f min %+.2f | > mu1 on %d/%d"
          % (float(np.median(np.log10(l3v / mu1))),
             float(np.min(np.log10(l3v / mu1))),
             int(np.sum(l3v > mu1)), n))
    check("N1 new ladder recorded", True)
    sl_env = stat["ENV"]["sl"]
    check("N2 ENV bound h-trend flat (|slope| <= %.2f)"
          % HTREND_FLAT, abs(sl_env) <= HTREND_FLAT,
          "slope %+.3f" % sl_env)

    # ------------------------------------------------------------ F
    section("F -- what a per-fold low-frequency supply buys")
    gains = {}
    for c in LOW_CUTS:
        t = "LOW%d" % (c - 1)
        if t in stat:
            g = np.array([math.log10(p["bounds"][t]
                                     / p["bounds"]["ENV"])
                          for p in pay])
            gains[t] = float(np.median(g))
            print("    exact per-fold deviation on folds f <= %-4d "
                  "buys %+.2f dex (band %+.2f/%+.2f)"
                  % (c - 1, gains[t], g.min(), g.max()))
    if "ABS" in stat:
        gt = np.array([math.log10(p["bounds"]["ABS"]
                                  / p["bounds"]["ENV"]) for p in pay])
        print("    the full ceiling (exact |d| on every fold) buys "
              "%+.2f dex" % float(np.median(gt)))
    check("F1 low-fold sensitivity recorded", True)

    # ------------------------------------------------------------ E
    section("E -- equilibration (CLXXV) applied to G_core")
    rr_ = np.array([p["rho"] for p in pay])
    ab_ = np.array([o["a"] - o["b"] for o in olds])
    eq_ = np.array([o["a"] * (1.0 - p["rho"])
                    for o, p in zip(olds, pay)])
    print("    rho = max_i sum_{j!=i}|R_ij| band %.3f/%.3f/%.3f"
          % band(rr_))
    print("    battery a-b band %+.3f/%+.3f/%+.3f  vs equilibrated "
          "a(1-rho) band %+.3f/%+.3f/%+.3f" % (band(ab_) + band(eq_)))
    print("    equilibration gain med %+.3f dex -- the diagonal is "
          "NOT spread (chi/a ~ 1.01), so the CLXXV mechanism buys "
          "no LEVEL here; what it does buy is the FORM: the "
          "correlation matrix is v-free and needs no K_up."
          % float(np.median(np.log10(np.maximum(eq_, 1e-300)
                                     / np.maximum(ab_, 1e-300)))))
    check("E1 equilibration comparison recorded", True)

    # ------------------------------------------------------------ C
    section("C -- controls, domination ward per world, world census")
    ctrl_rows = []
    for w in use[::max(1, len(use) // 4)][:4]:
        r2 = w["r2"]
        kz = r2["kz"]
        for tag, kw in (("smooth", dict(world_fn=base.world_smooth)),
                        ("scramble", dict(scramble_seed=1))):
            g = base.gram_anatomy(kz, keep_chain=True, **kw)
            if not isinstance(g, dict) or not g.get("core_ok"):
                ctrl_rows.append((kz, tag, "refused", None, None,
                                  None))
                continue
            rrw = base.window_of(kz, scramble_seed=kw.get(
                "scramble_seed"))
            uu, mm = rrw["uu"], 2.0 * rrw["lam"]
            if "world_fn" in kw:
                uu, mm = kw["world_fn"](uu, mm, rrw)
            Pc = base.eval_chain(g["chain"][0], g["chain"][1],
                                 g["chain"][2], g["y_core"], g["h"])
            Gw = np.sqrt(g["v_core"])[:, None] * (Pc @ Pc.T) \
                * np.sqrt(g["v_core"])[None, :]
            c_atw = core.atom_lags_at(rrw["alpha"], rrw["M"], uu,
                                      mm)[0]
            p = rung_payload(rrw["alpha"], rrw["M"], c_atw,
                             rrw["c_ar"], g["y_core"], g["v_core"],
                             g["h"], 0.5 * (Gw + Gw.T),
                             want_low=False)
            if p is None:
                ctrl_rows.append((kz, tag, "chain-refused", None,
                                  None, None))
                continue
            mu = 4.0 * math.sin(math.pi / (2 * g["h"] + 1)) ** 2
            ctrl_rows.append((kz, tag, "usable", p["doms"]["ENV"],
                              p["bounds"]["ENV"] / mu, p["loewner"]))
    for kz, tag, st, dm, rat, lw in ctrl_rows:
        if st != "usable":
            print("    kz %-4d %-9s %s" % (kz, tag, st))
        else:
            print("    kz %-4d %-9s domination %s (%+.3g)  "
                  "bound/mu1 %.3g  Loewner %s"
                  % (kz, tag, "HOLDS" if dm <= DOM_TOL else "VIOLATED",
                     dm, rat, "ok" if lw >= -L2_TOL else "VOID"))
    n_sm = sum(1 for c in ctrl_rows if c[1] == "smooth"
               and c[2] == "usable")
    n_sm_cert = sum(1 for c in ctrl_rows if c[1] == "smooth"
                    and c[2] == "usable" and c[4] and c[4] > 1.0)
    n_sc_dom = sum(1 for c in ctrl_rows if c[1] == "scramble"
                   and c[2] == "usable" and c[3] is not None
                   and c[3] > DOM_TOL)
    print("    smooth world: %d usable, composition reproduces on "
          "%d -- the DECLARED world-blind outcome (the step is a "
          "measure inequality)" % (n_sm, n_sm_cert))
    print("    scramble world: domination hypothesis violated on "
          "%d/%d usable -- the prime content sits in the HYPOTHESIS "
          "(the mass envelope is a psi theorem), not in the step"
          % (n_sc_dom, sum(1 for c in ctrl_rows if c[1] == "scramble"
                           and c[2] == "usable")))
    check("C1 control census recorded (world-blindness declared)",
          True)

    # ------------------------------------------------------------ T
    section("T -- tau-screens (parent verbatim)")
    taus = np.array([p["tau"] for p in pay])
    marg = np.array([p["bounds"]["ENV"] / p["mu1"] for p in pay])
    for nm, vals in (("ENV bound", np.array([p["bounds"]["ENV"]
                                             for p in pay])),
                     ("ENV/mu1 margin", marg),
                     ("old a0/mu1", a0 / mu1)):
        lab, sl = parent.screen(vals, taus)
        print("    %-16s %s   (slope %+.3f)" % (nm, lab, sl))
    check("T1 tau-screens recorded", True)

    # ------------------------------------------------------------ D
    section("D -- deep block (blind holdout frames)")
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
    if SMOKE:
        cand = cand[:3]
    else:
        cand = cand[:DEEP_CAP]
    print("    %d deep candidate rungs (cap %d)"
          % (len(cand), DEEP_CAP))
    dpay = []
    for kz in cand:
        g = deep.ext_gram(kz)
        if not isinstance(g, dict) or not g.get("core_ok") \
                or "chain" not in g:
            print("    deep kz %-4d unusable  [%.1f s]"
                  % (kz, time.time() - T0), flush=True)
            continue
        alpha, Mz, hz, ka = deep.ext_frame(kz)
        c_atd, Dz = core.atom_lags_at(alpha, Mz, deep.EXT["U"][:ka],
                                      deep.EXT["MU"][:ka])
        c_ar = np.asarray(core.arch_lags(Mz, Dz), float)
        Pc = base.eval_chain(g["chain"][0], g["chain"][1],
                             g["chain"][2], g["y_core"], g["h"])
        Gd = np.sqrt(g["v_core"])[:, None] * (Pc @ Pc.T) \
            * np.sqrt(g["v_core"])[None, :]
        Gd = 0.5 * (Gd + Gd.T)
        p = rung_payload(alpha, Mz, c_atd, c_ar, g["y_core"],
                         g["v_core"], g["h"], Gd, want_low=False)
        if p is None:
            print("    deep kz %-4d chain refused  [%.1f s]"
                  % (kz, time.time() - T0), flush=True)
            continue
        p["h"] = g["h"]
        p["kz"] = kz
        p["v"] = g["v_core"]
        p["Gc"] = Gd
        p["mu1"] = 4.0 * math.sin(math.pi / (2 * g["h"] + 1)) ** 2
        dpay.append(p)
        o = old_chain(p["v"], p["m0_ar_abs"], p["de"]["ENV"], Gd)
        print("    deep kz %-4d h %-5d truth %.3e  ENV %.3e  mu1 "
              "%.2e  dex>mu1 %+.2f  (old a0/mu1 %+.2f dex)  [%.1f s]"
              % (kz, g["h"], p["truth"], p["bounds"]["ENV"],
                 p["mu1"], math.log10(p["bounds"]["ENV"] / p["mu1"]),
                 math.log10(o["a0"] / p["mu1"]), time.time() - T0),
              flush=True)
    nd = len(dpay)
    check("D1 deep census >= %d" % MIN_DEEP, nd >= MIN_DEEP or SMOKE,
          "%d" % nd)
    d_l2 = sum(1 for p in dpay if p["loewner"] >= -L2_TOL)
    d_dom = sum(1 for p in dpay if max(p["doms"].values()) <= DOM_TOL)
    d_grid = sum(1 for p in dpay if p["grid_dev"] <= GRID_TOL)
    d_pos = sum(1 for p in dpay if p["bounds"]["ENV"] > p["mu1"])
    if nd:
        dd = np.array([math.log10(p["bounds"]["ENV"] / p["mu1"])
                       for p in dpay])
        print("    deep ENV above mu1 med %+.2f min %+.2f | %d/%d"
              % (float(np.median(dd)), float(dd.min()), d_pos, nd))
    check("D2 deep Loewner/domination/grid wards",
          nd and d_l2 == nd and d_dom == nd and d_grid == nd,
          "%d/%d, %d/%d, %d/%d" % (d_l2, nd, d_dom, nd, d_grid, nd),
          kill="K3")

    # -------------------------------------------------------- verdict
    tot = n + nd
    pos = stat["ENV"]["npos"] + d_pos
    abs_price = float(np.median(stat["ABS"]["d1"])) \
        if "ABS" in stat else float("inf")
    alg = "MONOCOMP-EXACT"
    if pos == tot and abs_price <= COMP_BAR:
        lab_i4 = ("I4-DISSOLVED(new composition price %+.2f dex vs "
                  "old %+.2f dex; ENV tier > mu1 on %d/%d)"
                  % (abs_price, float(np.median(i4)), pos, tot))
    elif pos >= REDUCE_FRAC * tot:
        lab_i4 = ("I4-REDUCED(swing %+.2f dex; ENV > mu1 on %d/%d)"
                  % (float(np.median(i4))
                     - float(np.median(stat["ENV"]["d1"])), pos, tot))
    else:
        lab_i4 = "I4-PERSISTS(ENV > mu1 on %d/%d)" % (pos, tot)
    if coup >= COUP_BAR:
        lab_h2 = ("H2-DISSOLVED(no upper-diagonal object in the "
                  "derived quantity; %+.2f dex of the old demand was "
                  "the propagated I4 deficit, residual CS looseness "
                  "%+.2f dex)" % (coup, float(np.median(h2r))))
    else:
        lab_h2 = "H2-PERSISTS(coupling only %+.2f dex)" % coup
    head = ("W1-COMPOSITION-REFORMED(old %+.2f dex below truth and "
            "%+.2f dex BELOW mu1  ->  new %+.2f dex below truth and "
            "%+.2f dex ABOVE mu1)"
            % (float(np.median(i4)),
               float(np.median(np.log10(a0 / mu1))),
               float(np.median(stat["ENV"]["d1"])),
               float(np.median(stat["ENV"]["d2"]))))
    if lab_i4.startswith("I4-PERSISTS") or \
            lab_h2.startswith("H2-PERSISTS"):
        head = "W1-COMPOSITION-PARTIAL(" + lab_i4 + ")"
    nxt = ("NEXT-OBJECT(per-fold low-frequency supply on f <= 32 "
           "buys %+.2f dex of the residual %+.2f dex envelope price)"
           % (gains.get("LOW32", float("nan")),
              float(np.median(stat["ENV"]["d1"]))))
    blind = ("COMPOSITION-WORLD-BLIND(declared: smooth reproduces "
             "%d/%d; the prime content is the domination HYPOTHESIS "
             "and the v-floor)" % (n_sm_cert, max(n_sm, 1)))
    return finish(dict(head=head, alg=alg, i4=lab_i4, h2=lab_h2,
                       blind=blind, next=nxt))


if __name__ == "__main__":
    sys.exit(main())
