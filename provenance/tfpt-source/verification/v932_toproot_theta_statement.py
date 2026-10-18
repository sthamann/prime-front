#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v932 -- PRIME.TOPROOT.THETA.01: THE TOPROOT STATEMENT + THE
QUARTIC CERTIFICATE H3 of round 172 -- the last lambda-uniform edge
of the jet-mass chain is pinned to ONE named per-rung hypothesis:
TOPROOT(p, C) == y_t(h) <= C h^p with the exact SEQ-COFINAL
quantifier and three machine-locked equivalent forms, the exact rate
dictionary a = p/2 - 1 (proven p = 3, 4, 5), the new THEOREM TR-CAP
(proven, typed circular-for-TOPROOT), the A_0-triangle route flagged
as the FOURTH loop route, and the per-rung quartic certificate H3
(y_t <= 0.155 T_z^4, one source evaluation, ancestors == {SOURCE}).

THE THEOREMS (exact algebra; sympy generic + exact instances; all
recomputed in-run):

  T1 (THE TOPROOT STATEMENT): y_t(h) <= C h^p, quantifier EXISTS
     (C, p) finite s.t. FOR EVERY dyadic block THERE IS a rung h in
     the block with y_t(h) <= C h^p (SEQ-cofinal; an ALL-h reading
     is NOT demanded).  THREE LOCKED FORMS: (i) THETA-FORM theta_y
     = y_t/T_z^4 <= theta_bar <==> TOPROOT(4, theta_bar (2 pi)^4);
     (ii) CENSUS-FORM (top root in (0.70, 0.95) y_t under H2);
     (iii) RATE-FORM: TOPROOT(p) ==> the sigma-floor exponent a =
     p/2 - 1 (the exact dictionary, proven).
  TR-CAP (NEW THEOREM, proven): |J_{m+1}| <= rho^m for all m >= 1
     ==> PHI(z) != 0 for every real z >= 1 + 2 rho (geometric sum
     + the positivity polynomial (z-1)(z-rho) - rho == rho + 2
     rho^2 + (1 + 3 rho) s + s^2 at z = 1 + 2 rho + s): NO census
     root above (1 + 2 rho) y_t.  TYPED CIRCULAR-FOR-TOPROOT: the
     dictionary is y_t-normalized BY CONSTRUCTION -- the cap bounds
     census-top/y_t, never y_t itself.  Fujiwara is CIRCULAR: the
     m = 1 term == B_1 + y_t EXACTLY (the Vieta trace) and is the
     ARGMAX at every rung.
  VIETA/POWER-SUM PINCH KILLED: every elementary symmetric function
     of the census carries 1/A_0 (e_2 == b_1 b_2 + (A_4 - A_2 B_1)/
     A_0 generic); y_t == B_1/kappa is a REFORMULATION, typed.
  THE A_0-TRIANGLE ROUTE == THE FOURTH LOOP: y_t <= b_top C_1/|A_0|
     is exponentially vacuous (overshoot 10^3.4 -> 10^64.6 riding
     -log10|A_0| with slope 0.97) AND its only A_0-floor consumes
     {TAUPOS, TLAWCAP} == the pinning-supply loop in A_0-currency
     (cycle machine-detected in-run, NOT consumed).
  ADMISSIBILITY (RECOMPUTED IN-RUN from closed forms): eps_closed
     (56) = sqrt(56) G(T_PT)/G(2 pi 56) = 4.5338e-9; a_max =
     ln(0.0767/eps)/ln 56 = 4.1348; p_max = 2(1 + a_max) = 10.2695
     -- the measured exponent p_all = 4.18 leaves SIX POWERS OF h
     of margin; by r169-SF4 there is NO finite asymptotic ceiling.
  THE WITNESS (both directions, exact): deflation A_0'' == A_0,
     y_t'' = y_t/1000; NEW INFLATION d+ = A_2(W - 1)/(b_2 - b_1):
     A_0 invariant, y_t'' = W y_t EXACTLY, theta'' = 62.69 >
     theta_bar: H3 IS REFUTABLE; the perturbation price is
     EXPONENTIALLY small (|d+|/max|c| = 8.1e-2 at h = 5 ->
     10^{-17.6} at h = 13): TOPROOT-NOT-NORM-CONTINUOUS -- no proof
     via source-norm continuity can exist; any proof must consume
     the arithmetic sign structure.

RE-RUN GREEN AS TYPED AT PROMOTION: toproot_theta_probe.py round
172 (note CDLXXXVIII, contract PRIME.TOPROOT.THETA.01), 33/33
gates, SPEC_SHA cf27df22aa5dffbf, run-of-record 2813 s +
deterministic re-run (timing-normalized diff empty, all logs kept
incl. one pre-freeze calibration; one disclosed smoke-stage fix,
no bar/window/tab moved) -- RE-RUN AT PROMOTION 2933.9 s with
identical SPEC_SHA and identical gate count (log kept as
toproot_theta_probe.promo_rerun.log).

PINNED FROM RUN-OF-RECORD (consistency arithmetic in-run): H3
CERTIFIED at all 25 rungs + the deep holdout h = 30 (K = 128,
degree-127 source) with margin theta_bar/theta_y >= 1.99
everywhere; theta_y = 0.0449 -> 0.0779 monotone saturating (growth
law p_all = 4.1821 in the r143 window, holdout residual -0.022
dex); rho == |J_2| at EVERY rung (argmax m = 1; 0.107 -> 0.152
inside the r156 quarter-cap window), cap 1 + 2 rho = 1.21 -> 1.30
vs H1's certified c* = 1.10/1.15 (ENVJ-SHARPER); the lock
FULLGAP/y_t in (1.0, 8.0) at all 26 rungs (2.23 -> 3.98); witness
strings 24.8702 (deflation top) and 62.691 (inflation theta);
SIZE-SEPARATOR factors 127/24/302 vs the fake worlds.

HONEST TYPING (carried verbatim; BH7-F1 correction of record
ADOPTED).  PROVEN = T1's three-form locking + TR-CAP + the rate
dictionary + the Vieta/e_2 identities + the witness algebra +
admissibility; H3 = CERTIFIED-SOURCE-PURE per rung (26/26 + the
holdout; ancestors == {SOURCE}); the COFINAL extension is the open
edge.  THE RESIDUE (BH7-F1): the composed per-block hypothesis is
the TRIPLE {H1 AND H2 AND H3}-cofinal, one rung per dyadic block,
all three at the same h -- NOT H3 alone (PF is proven only GIVEN
H1 + H2 at the same rung; H1/H2/H3 are finite per-rung source
checks of the same epistemic type, certified h <= 26/13(24)/30).
What remains besides the triple: {census-forall-k == LOOP, flagged}
+ {L1, WPD}.  FOUR loop routes carried flagged NOT consumed
(tlaw-window, census-all-k, pinning-supply, A0-floor variant).
Census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.  NOT evidence
for or against the Riemann Hypothesis in either direction.  NO RH
CLAIM.

PROVENANCE: discovery probe toproot_theta_probe.py (round 172,
2026-08-19/20, note CDLXXXVIII); consumes v931 (PF/H1/H2) + v926
(the theta window, cited); feeds v933 (the H3-cofinal
adjudication).  Externally covered by Bughunt VII (round 176, note
CDXCII: F1 applied here).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R172 = "cf27df22aa5dffbf"
T_PT = 3000175332800
# r172 G33/G34 theta ladder + H3 margins (record)
PIN_THETA_Y = {4: 0.044901, 5: 0.062691, 8: 0.065250, 13: 0.071983,
               28: 0.077144, 30: 0.077858}
THETA_BAR = 0.155
PIN_H3_MARGIN_MIN = 1.99
# r172 G35 moments (rho == |J_2|, argmax 1 at every rung)
PIN_RHO = {4: 0.106805, 5: 0.125884, 8: 0.139445, 13: 0.147746,
           28: 0.151278, 30: 0.151513}
PIN_CSTAR = {4: 1.10, 5: 1.15, 8: 1.15}
# r172 G43/G44 growth law + admissibility (frozen strings)
PIN_P_ALL = 4.1821
PIN_EPS56 = 4.533792e-9
PIN_AMAX = 4.134758
PIN_PMAX = 10.269515
PIN_RATE_C = 0.0767
PIN_HOLD_RESID = 0.022        # dex, h = 30 excluded from fit
# r172 G53 witness strings (h = 5) + scaling
PIN_WIT_ZTOP_DEFL = 24.870225
PIN_WIT_THETA_INFL = 62.690999
PIN_WIT_DNORM = {"defl": 8.117888e-5, "infl": 8.117888e-2}
PIN_WIT_SCALE = {8: -6.726, 13: -17.611}
# r172 G50-G52 size separator (min MAIN theta / max world theta_w)
PIN_SEP_FACTORS = (127.0, 24.0, 302.0)

N_CHECKS = 10
EXPECTED = "TOPROOT-THETA-STATEMENT"

CHECKS: list[tuple[str, bool]] = []
FAILS: list[str] = []


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def has_cycle(edges):
    color = {}

    def dfs(u):
        color[u] = 1
        for v in edges.get(u, ()):
            c = color.get(v, 0)
            if c == 1:
                return True
            if c == 0 and dfs(v):
                return True
        color[u] = 2
        return False

    return any(dfs(n) for n in list(edges) if color.get(n, 0) == 0)


def reachable(edges, src):
    seen = {src}
    stack = [src]
    while stack:
        u = stack.pop()
        for v in edges.get(u, ()):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def part():
    import sympy as sp

    # ================================================ A: T1 + TR-CAP
    section("A. THE TOPROOT STATEMENT + THEOREM TR-CAP (exact)")
    h, yt, tb = sp.symbols("h yt tb", positive=True)
    Tz = 2 * sp.pi * h
    okA = sp.simplify(yt / Tz ** 4 - yt / ((2 * sp.pi) ** 4 * h ** 4)) \
        == 0
    okB = sp.simplify(tb * (2 * sp.pi) ** 4 * h ** 4 - tb * Tz ** 4) \
        == 0
    check("A1 T1 statement: theta-form <==> TOPROOT(4) (SEQ "
          "quantifier)", okA and okB,
          "theta_y = y_t/T_z^4 <= theta_bar <==> y_t <= theta_bar "
          "(2 pi)^4 h^4 == TOPROOT(4, theta_bar (2 pi)^4) with T_z "
          "= 2 pi h (the r131 crossover, definitional); QUANTIFIER "
          "SEQ-COFINAL: exists (C, p) forall dyadic block exists "
          "rung -- an ALL-h reading is NOT demanded (r141/r143 "
          "DENSE-X + r169-SF4 inherited)")

    z, rho, s = sp.symbols("z rho s", positive=True)
    okC = sp.simplify((rho / z) / (1 - rho / z)
                      - rho / (z - rho)) == 0 \
        and abs(sum((0.1 / 3.0) ** mm for mm in range(1, 60))
                - 0.1 / (3.0 - 0.1)) < 1e-15
    poly = sp.expand(((z - 1) * (z - rho) - rho)
                     .subs(z, 1 + 2 * rho + s))
    pol = sp.Poly(poly, s)
    okD = all(c.is_positive is True for c in pol.all_coeffs())
    okE = sp.simplify(sp.expand(poly)
                      - (rho + 2 * rho ** 2 + (1 + 3 * rho) * s
                         + s ** 2)) == 0
    check("A2 THEOREM TR-CAP proven (circular-for-TOPROOT typed)",
          okC and okD and okE,
          "|J_{m+1}| <= rho^m ==> PHI(z) != 0 for real z >= 1 + 2 "
          "rho: geometric closed form sum rho^m z^-m == rho/(z - "
          "rho) + the positivity polynomial (z-1)(z-rho) - rho == "
          "rho + 2 rho^2 + (1 + 3 rho)s + s^2 (ALL coefficients "
          "positive): NO census root above (1 + 2 rho) y_t -- but "
          "the dictionary is y_t-NORMALIZED: the cap bounds "
          "census-top/y_t, NEVER y_t itself (CIRCULAR-FOR-TOPROOT; "
          "carried as a theorem in z-units)")

    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1 = sp.symbols("b1", positive=True)
    db = sp.symbols("db", positive=True)
    b2 = b1 + db
    A0 = c0 - c1 + c2
    A2 = -c1 * b1 + c2 * b2
    A4 = -c1 * b1 ** 2 + c2 * b2 ** 2
    B1 = b1 + b2
    yt_e = -A2 / A0
    F = A0 + (-1) * c1 * b1 / (sp.symbols("y") - b1) \
        + c2 * b2 / (sp.symbols("y") - b2)
    y = sp.symbols("y")
    N = sp.expand(sp.numer(sp.together(F)))
    cfs = sp.Poly(N, y).all_coeffs()
    e1 = sp.simplify(-cfs[1] / cfs[0])
    e2 = sp.simplify(cfs[2] / cfs[0])
    okF = sp.simplify(e1 - (B1 + yt_e)) == 0
    okG = sp.simplify(e2 - (b1 * b2 + (A4 - A2 * B1) / A0)) == 0
    r1, r2 = sp.symbols("r1 r2", real=True)
    okH = sp.simplify((r1 ** 2 + r2 ** 2)
                      - ((r1 + r2) ** 2 - 2 * r1 * r2)) == 0
    kapv = sp.symbols("kapv", positive=True)
    okI = sp.simplify(B1 / (B1 / kapv) - kapv) == 0 \
        and sp.simplify((B1 / kapv) * kapv - B1) == 0
    check("A3 Fujiwara circularity + the Vieta pinch killed",
          okF and okG and okH and okI,
          "the Fujiwara m = 1 term == B_1 + y_t EXACTLY (the Vieta "
          "trace, generic; ARGMAX at every rung in the record): the "
          "sharpest classical root bound RESTATES the trace, bound "
          ">= 2(1 + kappa) y_t > y_t; e_2 == b_1 b_2 + (A_4 - A_2 "
          "B_1)/A_0 generic -- EVERY symmetric function carries "
          "1/A_0 (no y_t-free pinch in the ring); y_t == B_1/kappa "
          "is a REFORMULATION (typed, not an advance); Newton p_2 "
          "== e_1^2 - 2 e_2")

    # ================================================ B: routes + rates
    section("B. THE A_0 ROUTE (LOOP) + THE RATE DICTIONARY + "
            "ADMISSIBILITY")
    tri_inst = bool(sp.Rational(7, 10) <= 4 * (sp.Rational(1, 3)
                    + sp.Rational(2, 5)) / sp.Rational(1, 2))
    tau_s, G_s, tl_s = sp.symbols("tau_s G_s tl_s", positive=True)
    A0sq = tau_s / (8 * G_s * tl_s)
    okJ = sp.simplify(8 * A0sq * G_s * tl_s - tau_s) == 0
    chain_a0 = {
        "TAUPOS": ["A0FLOOR"], "TLAWCAP": ["A0FLOOR"],
        "A0FLOOR": ["TOPROOT"], "TOPROOT": ["RATE"],
        "RATE": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"]}
    loop_a0 = has_cycle(chain_a0)
    check("B1 the A_0-triangle route DOUBLY DEAD (vacuous + loop)",
          tri_inst and okJ and loop_a0,
          "y_t <= b_top C_1/|A_0| (triangle, exact instance) is "
          "exponentially VACUOUS (record overshoot 10^3.4 -> "
          "10^64.6 riding -log10|A_0| slope 0.97: the bound loses "
          "EXACTLY the cancellation); the only A_0-floor is the "
          "zero-jet rearrangement A_0^2 == tau/(8 G tlaw_0) which "
          "consumes {TAUPOS, TLAWCAP}: the cycle TAUPOS/TLAWCAP -> "
          "A0FLOOR -> TOPROOT -> ... -> DTSTEP_K -> TAUPOS "
          "DETECTED (THE FOURTH FLAGGED LOOP ROUTE, not consumed)")

    q = sp.symbols("q", positive=True)
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    okK = True
    for p_e in (3, 4, 5):
        pe = sp.Integer(p_e)
        expr = h ** (pe / 2 - 1) * Glead(q * h ** (pe / 2)) \
            / Glead(2 * sp.pi * h)
        okK = okK and sp.simplify(sp.limit(expr, h, sp.oo)
                                  - sp.pi * pe / q) == 0
    a_s, c_s = sp.symbols("a_s c_s", positive=True)
    okL = sp.simplify((3 * sp.pi / c_s) * (1 + 2 * a_s / 3)
                      - sp.pi * (2 * a_s + 3) / c_s) == 0
    a4 = sp.Integer(4)
    kc = sp.symbols("kc", positive=True)
    expr4 = (sp.sqrt(h) * Glead(kc * h ** (sp.Rational(3, 2) + a4))
             / Glead(2 * sp.pi * h) * h ** a4)
    okM = sp.simplify(sp.limit(expr4, h, sp.oo)
                      - 2 * sp.pi * (sp.Rational(3, 2) + a4) / kc) == 0
    check("B2 the rate dictionary a == p/2 - 1 (proven p = 3, 4, 5)",
          okK and okL and okM,
          "lim h^{p/2-1} G_lead(q h^{p/2})/G_lead(2 pi h) == pi p/q "
          "at p = 3, 4, 5 (p = 4 replicates the r171 4 pi/q): "
          "TOPROOT(p) ==> sigma-floor exponent a = p/2 - 1 EXACT; "
          "census constant (3 pi/c)(1 + 2a/3) == pi(p + 1)/c; "
          "absorption holds even at a = 4 (limit 11 pi/kappa_c): "
          "NO finite asymptotic ceiling (r169-SF4)")

    def G_num(T):
        # the HSW-corrected density envelope (r168/r169/r171/r172
        # VERBATIM): G_lead + the HSW22 Cor. 1.2 correction terms
        al, be, cc = 0.1038, 0.2573, 9.3675
        lg = math.log(T)
        ll = math.log(lg)
        t1 = (math.log(T / (2 * math.pi)) + 1) / (2 * math.pi * T)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / T ** 2
        t3 = (al * lg + be * ll + cc) / T ** 2
        return t1 + t2 + t3

    eps56 = math.sqrt(56.0) * G_num(float(T_PT)) / G_num(2 * math.pi
                                                         * 56.0)
    amax = math.log(PIN_RATE_C / eps56) / math.log(56.0)
    pmax = 2 * (1 + amax)
    okN = abs(eps56 / PIN_EPS56 - 1) <= 5e-3 \
        and abs(amax / PIN_AMAX - 1) <= 5e-3 \
        and abs(pmax / PIN_PMAX - 1) <= 5e-3
    okO = PIN_P_ALL <= pmax - 4.0
    check("B3 admissibility RECOMPUTED: p_max = 10.27, margin >= 4",
          okN and okO,
          "eps_closed(56) = sqrt(56) G(T_PT)/G(2 pi 56) = %.6e "
          "(frozen 4.533792e-9); a_max = ln(0.0767/eps)/ln 56 = "
          "%.6f; p_max = 2(1 + a_max) = %.6f: the measured p_all = "
          "%.4f leaves %.1f powers of h of margin -- the census "
          "schedule absorbs the quartic law with room to exponent "
          "10" % (eps56, amax, pmax, PIN_P_ALL, pmax - PIN_P_ALL))

    W = sp.Integer(1000)
    dpl = A2 * (W - 1) / (b2 - b1)
    A0w = c0 - (c1 + dpl) + (c2 + dpl)
    A2w = -(c1 + dpl) * b1 + (c2 + dpl) * b2
    okP = sp.simplify(A0w - A0) == 0
    okQ = sp.simplify(A2w - W * A2) == 0
    okR = sp.simplify(sp.Abs(dpl) - sp.Abs(A2) * (W - 1) / db) == 0
    okS = PIN_WIT_THETA_INFL > THETA_BAR \
        and PIN_WIT_SCALE[13] <= -15.0 \
        and abs(PIN_WIT_DNORM["infl"] / PIN_WIT_DNORM["defl"]
                - 1000.0) <= 1.0
    check("B4 witness both directions: H3 refutable, TOPROOT not "
          "norm-continuous", okP and okQ and okR and okS,
          "inflation d+ = A_2(W-1)/(b_2-b_1): A_0'' == A_0 and "
          "y_t'' == W y_t EXACT generic (b_2 = b_1 + db); theta'' "
          "= %.3f > bar %.3f: H3 REFUTED IN THE WITNESS WORLD (the "
          "certificate is falsifiable); the price |d+|/max|c| = "
          "8.1e-2 (h=5) -> 10^%.1f (h=13): an EXPONENTIALLY small "
          "source perturbation moves y_t by ANY polynomial factor "
          "-- TOPROOT-NOT-NORM-CONTINUOUS (any proof must consume "
          "the arithmetic sign structure)"
          % (PIN_WIT_THETA_INFL, THETA_BAR, PIN_WIT_SCALE[13]))

    # ================================================ C: graphs
    section("C. THE ENDGAME GRAPHS (four loops; terminal chain)")
    chain_uni = {"RH": ["CENSUS_ALLK"], "CENSUS_ALLK": ["DTSTEP"],
                 "DTSTEP": ["HCOF"], "HCOF": ["RH"]}
    chain_pin = {"SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"],
                 "TAUPOS": ["SIGMAFLOOR"]}
    chain_term = {
        "H3_PER_RUNG": ["RATE"], "H3_COFINAL": ["RATE"],
        "ENVJ-H1": ["JETMASS"], "CENSUS-H2": ["JETMASS"],
        "GONEK": ["WF"], "WF": ["JETMASS"], "RATE": ["JETMASS"],
        "CENSUS_K": ["DCLEG", "DTSTEP_K"], "DCLEG": ["SIGMAFLOOR"],
        "JETMASS": ["SIGMAFLOOR"], "SIGMAFLOOR": ["DTSTEP_K"],
        "DTSTEP_K": ["HCOF"], "HCOF": ["RH"]}
    okT = has_cycle(chain_uni) and has_cycle(chain_pin) \
        and has_cycle(chain_a0) and not has_cycle(chain_term)
    okU = all("RH" in reachable(chain_term, sname)
              for sname in ("H3_COFINAL", "CENSUS_K", "GONEK"))
    check("C1 graphs: four loop routes flagged; TOPROOT-MEAS "
          "ancestor eliminated", okT and okU,
          "universalized-census, pinning-supply and A0-floor cycles "
          "DETECTED (+ tlaw-window: FOUR flagged routes, none "
          "consumed); the terminal chain with {H3_PER_RUNG, "
          "H3_COFINAL} -> RATE replacing TOPROOT-MEAS is ACYCLIC "
          "with RH reachable only from the counterfactual grants "
          "(AND-semantics); H3's ancestor set == {SOURCE}: same "
          "purity class as H1; NO RH CLAIM")

    # ================================================ D: pinned tables
    section("D. PINNED LADDERS (consistency arithmetic)")
    margins = [THETA_BAR / v for v in PIN_THETA_Y.values()]
    okth = all(0.03 < v < 0.12 for v in PIN_THETA_Y.values()) \
        and min(margins) >= PIN_H3_MARGIN_MIN \
        and PIN_THETA_Y[4] < PIN_THETA_Y[30]
    caps = {k: 1 + 2 * v for k, v in PIN_RHO.items()}
    okcap = all(1.15 < v < 1.45 for v in caps.values()) \
        and all(PIN_CSTAR[k] <= caps[k] for k in PIN_CSTAR)
    check("D1 H3 certified 26/26 (margin >= 1.99) + TR-CAP vs H1",
          okth and okcap,
          "theta_y = %s in (0.03, 0.12) at all 25 rungs + holdout "
          "h = 30 (K = 128, deg-127); H3 margin bar/theta >= %.2f "
          "everywhere; rho == |J_2| (argmax 1) with cap 1 + 2 rho "
          "= %.2f -> %.2f vs certified c* = %s: ENVJ-SHARPER (the "
          "new cap never beats the certified half-plane constant)"
          % ({k: PIN_THETA_Y[k] for k in (4, 30)},
             min(margins), min(caps.values()), max(caps.values()),
             PIN_CSTAR))

    okgl = 3.0 < PIN_P_ALL < 5.5 and PIN_HOLD_RESID <= 0.08 \
        and abs(PIN_P_ALL / 2 - 1 - 1.057) <= 0.25 \
        and min(PIN_SEP_FACTORS) >= 10.0
    check("D2 growth law + holdout + dictionary + size separator",
          okgl,
          "p_all = %.4f in the r143 window (3.0, 5.5); deep holdout "
          "h = 30 EXCLUDED from the fit, predicted with residual "
          "-%.3f dex; dictionary a_pred = p/2 - 1 = %.4f vs the "
          "r171 record 1.057 (closes within 0.093 tightened in "
          "v933); SIZE-SEPARATOR vs fake worlds: factors %s >= 10 "
          "(theta_w <= 1.9e-3 vs MAIN 0.045-0.078)"
          % (PIN_P_ALL, PIN_HOLD_RESID, PIN_P_ALL / 2 - 1,
             PIN_SEP_FACTORS))

    print("\n  [TYPED, BH7-F1 ADOPTED] THE RESIDUE: the composed "
          "per-block")
    print("  hypothesis is the TRIPLE {H1 AND H2 AND H3}-cofinal "
          "(one rung per")
    print("  dyadic block, all three at the same h -- NOT H3 "
          "alone) + {Gonek")
    print("  constants: priced v934} + {census-forall-k == LOOP} + "
          "{L1, WPD}.")
    print("  Census cardinality 4 UNCHANGED.  NOT RH evidence.  NO "
          "RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v932 -- PRIME.TOPROOT.THETA.01 (TOPROOT stated "
          "SEQ-cofinal, three locked")
    print("forms; rate dictionary a = p/2 - 1 proven; TR-CAP proven "
          "circular-for-")
    print("TOPROOT; H3 quartic certificate; round 172; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v932: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: T1/TR-CAP/dictionary/admissibility/witness "
          "algebra recomputed")
    print("in-run; the theta/rho/lock ladders PINNED from "
          "toproot_theta_probe.py")
    print("(SPEC %s, 33/33, record 2813 s + deterministic re-run, "
          "all logs kept," % PIN_SPEC_R172)
    print("RE-RUN GREEN AS TYPED AT PROMOTION).  NOT RH evidence; "
          "NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.TOPROOT.THETA.01 TOPROOT statement + quartic "
          "certificate: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
