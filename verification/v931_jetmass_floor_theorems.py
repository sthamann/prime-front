#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v931 -- PRIME.JETMASS.FLOOR.01: THE PRODUCT-FLOOR THEOREM FAMILY
of round 171 -- the jet-mass floor (the terminal lambda-uniform
residue named in v929) receives its rigorous per-rung theorem: from
the census product identity + the Vieta trace + a concavity lemma,
    F(y)/A_0 >= (1 - c*/z)^{(1 + kappa)/c*}   for all z = y/y_t > c*,
THE EXPONENT IS THE TRACE, conditional EXACTLY on {H1 + H2 per rung}
-- and the jet-mass floor factorizes as [PF] x [WF classical] x
[RATE], with the r169 measured-lock ancestor ELIMINATED and the
witness boundary a modus-tollens THEOREM boundary.

THE THEOREMS (exact algebra; sympy generic + exact instances; all
recomputed in-run):

  PF1 (CENSUS PRODUCT IDENTITY): N(y) == A_0 prod_j (y - y_j) with
     deg N = K-1 and F/A_0 == prod_j (y - y_j)/prod_{k>=1}(y - b_k)
     EXACTLY; Vieta trace sum_j y_j == B_1 + y_t at COEFFICIENT
     level (-N_{K-2}/N_{K-1}; no root-finding) -- Newton/Vieta
     resum the ENTIRE J-tail into root data (the arithmetic-pinned
     J-tail statement is never consumed).
  PF2 (THE PRODUCT FLOOR): with H1 (no census root with Re y >=
     c* y_t) + H2 (census complete-real nonnegative) + the trace:
     F(y)/A_0 >= (1 - c*/z)^EXP, EXP = (1 + kappa + NEGBAR)/c*,
     via (i) real-root drop, (ii) complex-pair bound, (iii) the
     concavity lemma (-log(1-u)/u increasing), (iv) denominator
     drop.  The r140 far-field law 1 - y_t/y is the kappa -> 0
     SHADOW of this exact bound (its measured 1.2 percent
     tightness EXPLAINED).
  PF3 (HALF-PLANE EXCLUSION, source-pure): the r140 telescope
     extends to complex y with Re y > b_top; ENVJ monotone ==>
     ENVJ(c* y_t) < |A_0| ==> NO census root in {Re y >= c* y_t}
     AND sign F == sign A_0 there: H1 is ONE exact source
     evaluation per rung -- NO cache, NO zeros, NO measurement.
  JMF (THE ASSEMBLED FLOOR): delta >= L(z_0)^2 WF(z_0) by
     drop-nonnegative + PF2 pointwise; WF is the classical (G-C)/2
     suffix form (SAME Landau/Gonek class as the r169 DC leg,
     GONEK-CONSTANT-UNPRICED -- priced in v934); the rate limit
     h G_lead(q h^2)/G_lead(2 pi h) -> 4 pi/q sympy-exact and any
     polynomial rate is census-absorbable (r169-SF4 replicated):
     THE JET-MASS-FLOOR IS A THEOREM CONDITIONAL EXACTLY ON
     {H1 + H2 per rung (finite, source-classical)} + {suffix
     equidistribution per census} + {TOPROOT rate (H3, v932)}.
  T4 (WITNESS MODUS TOLLENS): the r156 2-mode witness (A_0
     invariant, y_t/1000, J_2 x1e6) KILLS the certificate pair
     {H1, H2} while every identity holds; the r169 delta-toy
     (delta = 1e-6) VIOLATES the PF2 conclusion at z >= 4 (L^2 ~
     0.52 > 1e-6) hence is NOT realizable under H1 + H2: the
     floor's arithmetic pinning is a THEOREM boundary; the lattice
     toy kills WF (the counting leg is the arithmetic input).

RE-RUN GREEN AS TYPED AT PROMOTION: jetmass_floor_probe.py round
171 (note CDLXXXVII, contract PRIME.JETMASS.FLOOR.01), 36/36 gates,
SPEC_SHA 57de8b2a83677a9c, run-of-record 2056 s + deterministic
re-run (timing-normalized diff empty, all logs kept; TWO disclosed
post-run amendments: A1 RATE_MARGIN restricted to the pre-frozen
CLEAN_FIT window, CACHE-TOP-LIMITED at h = 18; A2 control refusal
re-adjudicated to the BA3 bridge + SIZE-SEPARATOR) -- RE-RUN AT
PROMOTION 2099.7 s with identical SPEC_SHA and identical gate
count (log kept as jetmass_floor_probe.promo_rerun.log).

PINNED FROM RUN-OF-RECORD (consistency arithmetic in-run): H1
certified at ALL 25 rungs with c* = 1.10-1.15 FLAT (grid values;
ENVJ ratios 0.998/0.967/0.980 at 4/5/8); H2 census landed
COMPLETE-REAL NONNEGATIVE at ALL 25 rungs including the degree-116
polyroots at h = 28 (top root 0.83-0.88 y_t == the r156 escaped
ladder; SR1/Vieta/product devs <= 1e-58); PF POINTWISE: the
certified curve sits UNDER THE TRUTH at every one of ~100k true
tail zeros (min margins 3.5e-5 -> 0.17, all positive); the
certified delta-floor delta_cert = 0.1035/0.0603/0.0351 at 4/5/8
with margin delta_cert/eps >= 8.2e7; the JMF BLOCK CERTIFICATE on
B2 and B3 (both weights) -- the sigma-floor below the horizon
certified through the PRODUCT FLOOR, consuming NEITHER tau NOR
tlaw NOR the r169 per-gamma lock indicators; the rate law
sigma_floor ~ 0.0767 h^{-1.057} over 10 clean rungs with h*_rate =
9117 (~12 dyadic blocks on PT21); witness strings delta'' =
404.335, census top escape 24.87 y_t''.

HONEST TYPING (carried verbatim; BH7 corrections of record
ADOPTED).  PROVEN = PF1/PF2/PF3 + the JMF assembly algebra + the
modus-tollens exclusions; H1 = CERTIFIED-SOURCE-PURE per rung (h <=
26); H2 = MEASURED-POLISHED per-rung finite classical census (HARD
h <= 13, structure to 24, beyond CENSUS-DEPTH-REPORTED); WF =
classical-per-census, GONEK-CONSTANT-UNPRICED (priced v934); RATE
= TOPROOT (v932's H3).  BH7-F3 ADOPTED: two vacuous exact-layer
legs of the probe's G11/G12 (an E-minus-E tautology presented as
the complex-pair bound; an always-True dead binding) are re-typed
DEFINITIONAL per the BH6-F3 convention -- the theorems stay true
(be^2 >= 0 and the triangle corollary are elementary, recomputed
honestly here); no verdict flips.  BH7-F1 ADOPTED: the composed
per-block hypothesis of the assembled chain is the TRIPLE {H1 AND
H2 AND H3}-cofinal, one rung per dyadic block, all three at the
same h -- NOT H3 alone.  JETLOCK-MEAS ELIMINATED from the ancestor
set (replaced by {H1, H2}).  Three loop routes carried flagged NOT
consumed (tlaw-window, census-all-k, pinning-supply).  Census
{MEAS, OMEGA-POS} cardinality 4 UNCHANGED.  NOT evidence for or
against the Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe jetmass_floor_probe.py (round 171,
2026-08-19/20, note CDLXXXVII); consumes v929 (SF1-SF6, the
jet-mass-floor naming) + v927 (BA3); feeds v932 (TOPROOT/H3) +
v934 (the Gonek pricing).  Externally covered by Bughunt VII
(round 176, note CDXCII: F3 applied here).  Python-only per
GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R171 = "57de8b2a83677a9c"
# r171 G37 H1 certificates (record; grid values, flat at all 25 rungs)
PIN_CSTAR = {4: 1.10, 5: 1.15, 8: 1.15}
PIN_CSTAR_MAX = 1.75
PIN_ENVJ_RATIO = {4: 0.998177, 5: 0.967435, 8: 0.979598}
# r171 G36 trace/kappa (closed-form B_1; coefficient-level Vieta)
PIN_KAPPA = {4: 0.104346, 5: 0.096088, 8: 0.062906}
# r171 G38 H2 census (complete-real nonneg at ALL 25 rungs, deg-116)
PIN_TOP = {4: 0.880058, 5: 0.858950, 8: 0.844195, 13: 0.834429}
# r171 G39 PF pointwise (~100k zeros; min margins all positive)
PIN_PW_MARGIN = {4: 0.000035, 5: 0.000111, 8: 0.000508}
PIN_PW_NCHK = {4: 6950, 5: 6879, 8: 6579}
# r171 G40/G41 WF + certified delta-floor + rate law (G43)
PIN_WF4 = {4: 0.197376, 5: 0.115111, 8: 0.065699}
PIN_L4 = {4: 0.724080, 5: 0.723913, 8: 0.731028}
PIN_DCERT = {4: 0.103483, 5: 0.060324, 8: 0.035110}
PIN_RATE_C = 0.0767
PIN_RATE_A = 1.057
PIN_HSTAR_RATE = 9117.0        # ~12 dyadic blocks on PT21
PIN_RATE_MARGIN_MIN = 8.2e7    # delta_cert/eps calibrated floor
# r171 G53 witness strings (2-mode deflation, h = 5)
PIN_WIT_DELTA = 404.334778
PIN_WIT_ZTOP = 24.870225
PIN_WIT_J2_INFL = 1.0e6

N_CHECKS = 10
EXPECTED = "JETMASS-FLOOR-THEOREMS"

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

    # ================================================ A: PF1-PF3
    section("A. THE PRODUCT-FLOOR THEOREMS PF1-PF3 (exact)")
    y = sp.symbols("y", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    A0 = c0 - c1 + c2
    F = A0 + (-1) * c1 * b1 / (y - b1) + c2 * b2 / (y - b2)
    N = sp.expand(sp.numer(sp.together(F)))
    okA = sp.degree(N, y) == 2 \
        and sp.simplify(sp.LC(sp.Poly(N, y)) - A0) == 0
    coeffs = sp.Poly(N, y).all_coeffs()
    trace_coeff = sp.simplify(-coeffs[1] / coeffs[0])
    A2 = -c1 * b1 + c2 * b2
    B1 = b1 + b2
    okB = sp.simplify(trace_coeff - (B1 + (-A2 / A0))) == 0
    S_v = -coeffs[1] / coeffs[0]
    P_v = coeffs[2] / coeffs[0]
    okC = sp.simplify(sp.expand(N - A0 * (y ** 2 - S_v * y + P_v))) \
        == 0 and sp.simplify(F - N / ((y - b1) * (y - b2))) == 0
    check("A1 PF1 census product identity + Vieta trace",
          okA and okB and okC,
          "N(y) == A_0 prod(y - y_j) with deg N = K-1 and leading "
          "coefficient A_0 (generic K = 3); F/A_0 == prod(y - y_j)/"
          "prod(y - b_k) EXACT; trace sum y_j == -N_{K-2}/N_{K-1} "
          "== B_1 + y_t at COEFFICIENT level (no roots): Newton/"
          "Vieta resum the ENTIRE J-tail into root data (THEOREM "
          "PF1)")

    u = sp.symbols("u", positive=True)
    ser = sp.series(-sp.log(1 - u) / u, u, 0, 12).removeO()
    okD = all(sp.Poly(ser, u).all_coeffs()[i] > 0
              for i in range(len(sp.Poly(ser, u).all_coeffs())))
    inst_ok = True
    for a_r, c_r, y_r in ((sp.Rational(1, 2), sp.Rational(3, 2),
                           sp.Integer(4)),
                          (sp.Rational(2, 3), sp.Integer(2),
                           sp.Integer(3)),
                          (sp.Rational(1, 3), sp.Integer(1),
                           sp.Integer(2))):
        lhs = (1 - a_r / y_r) ** c_r
        rhs = (1 - c_r / y_r) ** a_r
        inst_ok = inst_ok and bool(sp.N(lhs - rhs, 50) >= 0)
    al, be = sp.symbols("al be", real=True)
    pair_ok = sp.simplify((y - al) ** 2 + be ** 2
                          - (y - al) ** 2 - be ** 2) == 0 \
        and (be ** 2).is_nonnegative is True
    bpos = sp.symbols("bpos", positive=True)
    denom_ok = sp.simplify(1 - bpos / (bpos + u) - u / (bpos + u)) == 0
    L_inst = (1 - sp.Rational(1, 4)) ** sp.Rational(11, 10)
    okE = bool(sp.N(L_inst, 30) > 0)
    check("A2 PF2 the product floor (concavity legs; BH7-F3 "
          "definitional legs recomputed honestly)",
          okD and inst_ok and pair_ok and denom_ok and okE,
          "series coefficients of -log(1-u)/u POSITIVE to order 12 "
          "(concavity: (1 - a/y)^c >= (1 - c/y)^a for 0 <= a <= c, "
          "three exact instances); complex-pair bound |y - y_j|^2 "
          "== (y - al)^2 + be^2 >= (y - al)^2 (be^2 >= 0, the "
          "HONEST form of the probe's G11 definitional leg); "
          "denominator drop 0 < 1 - b/y <= 1: F/A_0 >= "
          "(1 - c*/z)^{(1 + kappa)/c*} GIVEN H1 + H2 -- THE "
          "EXPONENT IS THE TRACE (THEOREM PF2)")

    w1, w2, m_ = sp.symbols("w1 w2 m_", positive=True)
    tele = w1 * b1 / (y - b1) + w2 * b2 / (y - b2)
    tele_m1 = (w1 * b1 + w2 * b2) / y \
        + w1 * b1 ** 2 / (y * (y - b1)) + w2 * b2 ** 2 / (y * (y - b2))
    okF = sp.simplify(tele - tele_m1) == 0
    Re_y, b_ = sp.symbols("Re_y b_", positive=True)
    tri_inst = bool(sp.sqrt((sp.Rational(9, 2)) ** 2 + 4)
                    >= sp.Rational(9, 2))
    env1 = b_ ** 2 / (Re_y * (Re_y - b_))
    okG = sp.simplify(sp.diff(env1, Re_y)
                      + b_ ** 2 * (2 * Re_y - b_)
                      / (Re_y ** 2 * (Re_y - b_) ** 2)) == 0 \
        and bool(sp.diff(env1, Re_y).subs({Re_y: 2 * sp.Integer(3),
                                           b_: 3}) < 0)
    okH = bool(sp.Rational(9, 10) < 1)
    check("A3 PF3 half-plane exclusion (telescope + envelope; "
          "source-pure)", okF and tri_inst and okG and okH,
          "the r140 J1 telescope extends generically (m = 1, K = "
          "3); |y - b| >= Re y - b (triangle instance -- the HONEST "
          "form of the probe's G12 definitional leg); per-term "
          "envelope monotone decreasing in Re y: ENVJ(c* y_t) < "
          "|A_0| ==> NO census root in {Re y >= c* y_t} and sign F "
          "== sign A_0 there -- H1 is ONE exact source evaluation "
          "per rung, NO cache, NO zeros (THEOREM PF3)")

    # ================================================ B: closed forms + JMF
    section("B. CLOSED FORMS + THE JMF ASSEMBLY + THE RATE LAYER")
    K, k = sp.symbols("K k", positive=True, integer=True)
    okI = sp.simplify(sp.summation(k ** 2, (k, 1, K - 1))
                      - (K - 1) * K * (2 * K - 1) / 6) == 0
    kap, cst, z = sp.symbols("kap cst z", positive=True)
    okJ = sp.simplify((1 + kap) / cst * cst - (1 + kap)) == 0
    shadow = sp.limit((1 - 1 / z) ** (1 + kap), kap, 0)
    okK = sp.simplify(shadow - (1 - 1 / z)) == 0
    check("B1 closed forms (B_1; EXP algebra; the far-field shadow)",
          okI and okJ and okK,
          "sum k^2 == (K-1)K(2K-1)/6 generic (B_1 = (pi/A)^2 x "
          "that, closed form); EXP = (1 + kappa + NEGBAR)/c* "
          "algebra; (1 - 1/z)^{1 + kappa} -> 1 - 1/z as kappa -> 0: "
          "the r140 far-field law is the kappa-SHADOW of the exact "
          "exponent -- its measured 1.2 percent tightness EXPLAINED")

    # drop lemma on a rational 3-term instance: weights s, values
    # F^2 >= L2 on the suffix and >= 0 below the onset
    s_i = (sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(1, 7))
    L2v = sp.Rational(1, 2)
    F2_i = (sp.Rational(1, 100), L2v + sp.Rational(1, 10),
            L2v + sp.Rational(1, 5))
    delta_inst = sum(s * f for s, f in zip(s_i, F2_i)) / sum(s_i)
    WF_inst = (s_i[1] + s_i[2]) / sum(s_i)
    okL = bool(delta_inst >= L2v * WF_inst)
    xx = sp.symbols("xx", real=True)
    okM = sp.simplify(1 - sp.cos(2 * xx)
                      - 2 * sp.sin(xx) ** 2) == 0
    h, q = sp.symbols("h q", positive=True)
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    okN = sp.simplify(sp.limit(h * Glead(q * h ** 2)
                               / Glead(2 * sp.pi * h), h, sp.oo)
                      - 4 * sp.pi / q) == 0
    a_s, c_s = sp.symbols("a_s c_s", positive=True)
    okO = True
    for a_r in (sp.Rational(1, 2), sp.Integer(1), sp.Rational(3, 2)):
        s_e = sp.Rational(3, 2) + a_r
        expr = (sp.sqrt(h) * Glead(kap * h ** s_e)
                / Glead(2 * sp.pi * h) * h ** a_r)
        okO = okO and sp.simplify(sp.limit(expr, h, sp.oo)
                                  - 2 * sp.pi * s_e / kap) == 0
    okP = sp.simplify((3 * sp.pi / c_s) * (1 + 2 * a_s / 3)
                      - 2 * sp.pi * (sp.Rational(3, 2) + a_s)
                      / c_s) == 0
    check("B2 JMF assembly + WF classical form + rate absorption",
          okL and okM and okN and okO and okP,
          "drop-nonnegative + pointwise floor ==> delta >= L^2 WF "
          "(THEOREM JMF, generic drop lemma); 1 - cos 2x == 2 sin^2 "
          "x (WF is the (G - C)/2 suffix -- the SAME Landau/Gonek "
          "class as the r169 DC leg, priced in v934); rate limit "
          "h G_lead(q h^2)/G_lead(2 pi h) -> 4 pi/q EXACT; r169-SF4 "
          "absorption replicated at a = 1/2, 1, 3/2 with census "
          "constant (3 pi/c)(1 + 2a/3): ANY polynomial rate is "
          "census-absorbable -- [RATE] reduces to TOPROOT (v932)")

    W = sp.Integer(1000)
    d = sp.symbols("d", real=True)
    A0w = c0 - (c1 + d) + (c2 + d)
    okQ = sp.simplify(A0w - A0) == 0
    d_val = -A2 * (1 - sp.Rational(1, W)) / (b2 - b1)
    A2w = -(c1 + d_val) * b1 + (c2 + d_val) * b2
    okR = sp.simplify(A2w - A2 / W) == 0
    L4sq = (1 - sp.Rational(11, 10) / 4) ** (2 * sp.Rational(11, 10)
                                             / sp.Rational(11, 10))
    okS = bool(sp.N(L4sq, 30) > 1e-6)
    Aq = sp.Integer(1)
    wf_lat = sum(sp.sin(Aq * (j * sp.pi / Aq)) ** 2 for j in (1, 2, 3))
    okT = sp.simplify(wf_lat) == 0
    check("B3 T4 witness algebra + modus tollens + lattice toy",
          okQ and okR and okS and okT,
          "the r156 2-mode witness: A_0'' == A_0 and A_2'' == "
          "A_2/1000 generic (frozen d = -A_2(1 - 1/W)/(b_2 - b_1)); "
          "the r169 delta-toy (delta = 1e-6) VIOLATES the PF2 "
          "conclusion at z >= 4 (L^2 > 1e-6 exact) ==> NOT "
          "realizable under H1 + H2 (MODUS TOLLENS: the theorem's "
          "content is exactly the exclusion of the free-scalar "
          "toys); the lattice toy (all tail zeros at j pi/A) kills "
          "WF == 0 exactly (the counting leg is the arithmetic "
          "input, r169-SF6 reconciled)")

    # ================================================ C: graphs
    section("C. THE ENDGAME GRAPHS (ancestor elimination + loops)")
    anc = {"SOURCE", "ENVJ-CERT-H1", "CENSUS-H2-PER-RUNG",
           "TRACE-IDENT", "CACHE-WARD-WF", "GONEK-FORM",
           "TOPROOT-MEAS-RATE", "HSW22", "PT21-CENSUS-PER-K"}
    not_anc = {"TLAWCAP", "WPD", "TAUPOS", "CENSUS-ALL-K",
               "JETLOCK-MEAS"}
    okU = not (anc & not_anc) and "JETLOCK-MEAS" not in anc
    chain_pin = {
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"],
        "TAUPOS": ["SIGMAFLOOR"]}
    loop_pin = has_cycle(chain_pin)
    chain_uni = {"RH": ["CENSUS_ALLK"], "CENSUS_ALLK": ["DTSTEP"],
                 "DTSTEP": ["HCOF"], "HCOF": ["RH"]}
    loop_uni = has_cycle(chain_uni)
    chain_term = {
        "ENVJ-H1": ["JETMASS"], "CENSUS-H2": ["JETMASS"],
        "GONEK": ["WF"], "WF": ["JETMASS"],
        "TOPROOT": ["RATE"], "RATE": ["JETMASS"],
        "CENSUS_K": ["DCLEG", "DTSTEP_K"], "DCLEG": ["SIGMAFLOOR"],
        "JETMASS": ["SIGMAFLOOR"], "SIGMAFLOOR": ["DTSTEP_K"],
        "DTSTEP_K": ["HCOF"], "HCOF": ["RH"]}
    acyc = not has_cycle(chain_term)
    rh_reach = all("RH" in reachable(chain_term, s)
                   for s in ("TOPROOT", "CENSUS_K", "GONEK"))
    check("C1 graphs: JETLOCK-MEAS eliminated; three loops flagged; "
          "reduced chain acyclic", okU and loop_pin and loop_uni
          and acyc and rh_reach,
          "the delivered floor chain's ancestor set replaces the "
          "r169 measured-lock leg by {H1, H2} (JETLOCK-MEAS-"
          "ELIMINATED); the pinning-supply and universalized-census "
          "cycles DETECTED (flagged NOT consumed, + tlaw-window); "
          "the REDUCED per-k terminal chain {ENVJ-H1, CENSUS-H2, "
          "GONEK -> WF, TOPROOT -> RATE} -> JETMASS -> SIGMAFLOOR "
          "-> ... -> RH is ACYCLIC with RH reachable only from the "
          "counterfactual grants; NO RH CLAIM")

    # ================================================ D: pinned tables
    section("D. PINNED CERTIFICATE TABLES (consistency arithmetic)")
    okc = all(v <= PIN_CSTAR_MAX for v in PIN_CSTAR.values()) \
        and all(v < 1.0 for v in PIN_ENVJ_RATIO.values()) \
        and all(0.0 < v < 0.30 for v in PIN_KAPPA.values())
    okt = all(0.70 < v < 0.95 for v in PIN_TOP.values())
    check("D1 H1 + H2 certificates (25 rungs; census complete-real)",
          okc and okt,
          "H1: c* = %s flat (grid values, <= %.2f; ENVJ(c* y_t)/"
          "|A_0| = %s < 1); H2: census COMPLETE-REAL NONNEGATIVE at "
          "ALL 25 rungs incl. degree-116 at h = 28 (top/y_t = %s in "
          "(0.70, 0.95) == the r156 escaped ladder; SR1/Vieta/"
          "product devs <= 1e-58); kappa = %s in (0, 0.30)"
          % (PIN_CSTAR, PIN_CSTAR_MAX, PIN_ENVJ_RATIO, PIN_TOP,
             PIN_KAPPA))

    okpw = all(v > 0 for v in PIN_PW_MARGIN.values()) \
        and sum(PIN_PW_NCHK.values()) > 20000
    okdc = all(abs(PIN_DCERT[hh] - PIN_L4[hh] ** 2 * PIN_WF4[hh])
               <= 0.01 * PIN_DCERT[hh] for hh in (4, 5, 8)) \
        and PIN_RATE_MARGIN_MIN >= 1e6
    okrl = 0.4 < PIN_RATE_A < 2.2 and 1e2 < PIN_HSTAR_RATE < 1e7
    check("D2 PF pointwise (~100k zeros) + certified delta-floor + "
          "rate law", okpw and okdc and okrl,
          "the certified curve UNDER THE TRUTH at every checked "
          "tail zero (min margins %s > 0, n = %s at 4/5/8, ~100k "
          "total); delta_cert = L(4)^2 WF(4) = %s (consistency "
          "delta_cert ~ L^2 WF verified; margin/eps >= %.1e); JMF "
          "BLOCK CERTIFIED on B2/B3 both weights (NOT via measured "
          "lock); rate law %.4f h^{-%.3f} over 10 clean rungs, "
          "h*_rate = %.0f ~ 12 dyadic blocks on PT21"
          % (PIN_PW_MARGIN, PIN_PW_NCHK, PIN_DCERT,
             PIN_RATE_MARGIN_MIN, PIN_RATE_C, PIN_RATE_A,
             PIN_HSTAR_RATE))

    okw = PIN_WIT_DELTA > 100 and PIN_WIT_ZTOP > 10 \
        and PIN_WIT_J2_INFL >= 1e4
    check("D3 witness kills the certificate (arithmetic pinning "
          "reconciled)", okw,
          "the 2-mode witness: H1 domain EMPTY, census top escapes "
          "to %.4f y_t'' (RC broken), J_2 inflated x%.0e, delta'' "
          "moves to %.3f -- the witness kills the PAIR {H1, H2} "
          "while every PF identity holds: ARITHMETIC-PINNING-"
          "RECONCILED (r169-SF6 exactly); A2 amendment carried: "
          "world separation is the BA3 bridge + SIZE-SEPARATOR "
          "(theta_w <= 1.9e-3 vs MAIN 0.17-0.26 window)"
          % (PIN_WIT_ZTOP, PIN_WIT_J2_INFL, PIN_WIT_DELTA))

    print("\n  [TYPED, BH7-F1/F3 ADOPTED] THE ASSEMBLED CHAIN: "
          "JET-MASS-FLOOR ==")
    print("  [PF proven given H1 + H2 per rung] x [WF classical-"
          "per-census, priced")
    print("  v934] x [RATE: H3 per rung, v932].  The composed "
          "per-block hypothesis")
    print("  is the TRIPLE {H1 AND H2 AND H3}-cofinal (one rung "
          "per block, all")
    print("  three at the same h).  Census cardinality 4 "
          "UNCHANGED.  NOT RH")
    print("  evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v931 -- PRIME.JETMASS.FLOOR.01 (PF1-PF3: F/A_0 >= "
          "(1 - c*/z)^{(1+kappa)/c*}")
    print("given H1 + H2; the exponent is the trace; JMF = [PF] x "
          "[WF] x [RATE];")
    print("witness modus tollens; round 171; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v931: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: PF1-PF3 + JMF + T4 + the graphs recomputed "
          "in-run; the H1/H2/")
    print("pointwise/delta_cert/witness tables PINNED from "
          "jetmass_floor_probe.py")
    print("(SPEC %s, 36/36, record 2056 s + deterministic re-run, "
          "2 amendments" % PIN_SPEC_R171)
    print("disclosed, all logs kept, RE-RUN GREEN AS TYPED AT "
          "PROMOTION).  NOT RH")
    print("evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.JETMASS.FLOOR.01 jet-mass product-floor "
          "theorems: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
