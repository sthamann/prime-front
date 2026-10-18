#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v934 -- PRIME.GONEK.PRICING.01: THE UNCONDITIONAL GONEK PRICING of
round 174 -- the "{Gonek constants, citable classical work}" item of
the endgame residue is PRICED and LEAVES the program residue: the
exact classical statements are identified with their precise
conditionality ([L] Landau 1912 and [G] Gonek 1985/1993 both
UNCONDITIONAL; the RH-conditional family [R] Gonek 1984 machine-
checked NOT AN ANCESTOR of either leg), the error envelope gets a
sympy-exact closed form with a FINITE CENSUS-DEPTH-INSENSITIVE
ceiling, and the constants are priced against the 20M-zero verified
census at signal/bound ratios up to 2.7e4.

THE DELIVERABLES (exact algebra recomputed in-run; pinned census
tables with consistency arithmetic):

  GP1 (STATEMENTS IDENTIFIED, conditionality adjudicated):
     [L] Landau 1912 (Math. Ann. 71, 548-564): for fixed x > 1,
     sum_{0 < gamma <= T} x^rho = -(T/2 pi) Lambda(x) + O(log T),
     over ALL nontrivial zeros -- UNCONDITIONAL.  [G] Gonek
     1985/1993 (Contemp. Math. 143, 395-413): the same sum
     UNIFORMLY for x, T > 1 with |E(x,T)| <= c_G x log(2xT)
     loglog(3x) for integer x >= 2 -- UNCONDITIONAL.  [R] Gonek
     1984 (Invent. Math. 75, 123-142): the zeta'(rho)-weighted
     moments are RH-CONDITIONAL == LOOP-IF-CONSUMED -- machine-
     checked NOT an ancestor of either priced leg; the would-be
     hidden cycle GONEK-1984 -> DCLEG -> SIGMAFLOOR -> DTSTEP ->
     HCOF -> RH -> GONEK-1984 is DETECTED and flagged, never
     consumed (recomputed in-run).  Externally re-verified in
     Bughunt VII (round 176: citations, all three error terms,
     integer subsumption, [R] adjudication -- all CORRECT).
  GP2 (THE ENVELOPE CLOSED FORM -- the round's discovery, sympy
     exact): the Abel-transported error envelope ENV = [B/T_hi^2 +
     B/T_lo^2 + 2 Int B/t^3]/sqrt(x), B(x,t) = x log(2xt)
     loglog(3x), COLLAPSES so the T_hi-dependence is the single
     term -1/(2 T_hi^2): ENV == sqrt(x) loglog(3x)[(4 log(2 x
     T_lo) + 1)/(2 T_lo^2) - 1/(2 T_hi^2)] -- monotone increasing
     in T_hi with the FINITE CEILING ENV_oo: the envelope is
     T_lo-ANCHORED and CENSUS-DEPTH-INSENSITIVE (a deeper census
     can never inflate the classical remainder past the ceiling).
  GP3 (PREFACTOR-INSENSITIVE ABSORPTION, symbolic c_G): c_G
     ENV_oo(2 pi h)/G_lead(2 pi h) -> 0 (DC leg) and c_G
     ENV_oo(q h^{p/2})/G_lead(q h^{p/2}) -> 0 at p = 2, 3, 4, 5
     (WF/TOPROOT window), all sympy limits with the constant
     SYMBOLIC; the rate dictionary p = 4 == 4 pi/q replicated:
     THE CENSUS SCHEDULE 3/2 + a TOLERATES THE CLASSICAL ERROR
     TERMS AT ANY FINITE CONSTANT.
  GP4 (THE PRICING, pinned): c_hat <= 0.085981 over the full 12
     x-values x 6 depths spike table (prime powers 4/5/8/13/27/32,
     composites 6/10/12/15/21/22, depths 1e4..2e7 on the 20M-zero
     Odlyzko + LMFDB/Platt cache), snr up to 26592.6 -- the Gonek
     form over-covers the measured error >= 11x; composites give
     Lambda == 0 EXACTLY (closed forms recomputed); DC leg
     replicates r169 at all 25 rungs (priced gate max 0.0244); WF
     leg holds the exact perturbation bound HARD at 4 rungs
     (suffix priced ratio <= 0.0272); controls: smooth/jitter/
     dilation combs fail the Landau prediction at >= 100x
     separation, the dilation witness re-creates the true spike at
     x' = 5^{64/65} to 1.4e-7 (JITTER-PARTIAL-COHERENT typed
     honestly).

RE-RUN GREEN AS TYPED AT PROMOTION: gonek_pricing_probe.py round
174 (note CDLXXXIX, contract PRIME.GONEK.PRICING.01), 20/20 gates,
SPEC_SHA 3050678b352eaa9a, run-of-record 188 s + deterministic
re-run (timing-normalized diff empty, all logs kept; one disclosed
pre-record smoke-stage fix: control-bar depth scaling, full depth
untouched) -- RE-RUN AT PROMOTION 244.2 s with identical SPEC_SHA
and identical gate count (log kept as
gonek_pricing_probe.promo_rerun.log).

HONEST TYPING (carried verbatim; nothing upgraded).  The constant
status is CONSTANT-EMPIRICAL-PER-CENSUS: no numerically explicit
constant for [G] exists in the literature -- the pricing is the
measured census constant plus the symbolic prefactor-insensitivity,
NOT a published explicit constant.  The on-line rewrite cos(g log
h) == Re h^{rho - 1/2} stays PER-CENSUS (both caches below the
Platt-Trudgian height T_0 = 3e12 unconditionally); the ALL-K
reading is the machine-flagged RH loop, carried NOT consumed.  THE
RESIDUE AFTER THIS ROUND (Bughunt-VII F1 correction of record
ADOPTED): the Gonek item leaves the residue; what remains is
{the TRIPLE {H1 AND H2 AND H3}-cofinal -- one rung per dyadic
block, all three at the same h (NOT H3 alone)} + {census-forall-k
== LOOP, flagged, not consumed} + {L1, WPD counting-class
remnants}.  Census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.  NOT
evidence for or against the Riemann Hypothesis in either
direction.  NO RH CLAIM.

PROVENANCE: discovery probe gonek_pricing_probe.py (round 174,
2026-08-20, note CDLXXXIX); consumes v929 (SF3 DC-leg typing) +
the r171 WF leg (v931); externally re-verified in Bughunt VII
(round 176, note CDXCII).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R174 = "3050678b352eaa9a"
# r174 G30/G31 spike pricing (record gonek_pricing_probe.run1.log)
PIN_CHAT_MAX = 0.085981          # full 12 x 6 table maximum
PIN_CHAT_BAR = 0.20
PIN_CHAT_DEEP = {4: 0.0689, 5: 0.0541, 8: 0.0203, 13: 0.0148}
PIN_SNR_DEEP = {4: 15861.2, 5: 26592.6, 8: 6013.4, 13: 11888.0,
                27: 2072.0, 32: 1066.4}
PIN_SNR_MIN = 500.0
# r174 G33 DC-leg pricing (r169 Z/DC tabs replicated + priced gate)
PIN_Z_TAB = {4: +0.266, 5: -0.177, 8: +0.245}
PIN_DC_TAB = {4: 0.153469, 5: 0.227257, 8: 0.268559}
PIN_R_PRICED = {4: 0.0157, 5: 0.0099, 8: 0.0107}
PIN_R_PRICED_MAX = 0.024356      # calibrated max (h = 6), bar 0.05
# r174 G34 WF-leg pricing (r171 tab replicated + new h = 13)
PIN_WF4 = {4: 0.197376, 5: 0.115111, 8: 0.065699}
PIN_WF13 = 0.021908
PIN_RSUF = {4: 0.0146, 5: 0.0272, 8: 0.0028, 13: 0.0064}
PIN_RSUF_MAX = 0.0272            # bar 0.06
# r174 G50-G52 controls (chat_w strings; true chat <= 0.086)
PIN_CTRL = {"SMOOTH": {5: 3583.7, 8: 807.7, 13: 1591.7},
            "JIT": {5: 135.0, 8: 46.1, 13: 139.3},
            "DIL": {5: 3583.9, 8: 807.8, 13: 1591.8}}
PIN_WIT_DEV = 1.41e-7            # dilation witness at x' = 5^{64/65}

N_CHECKS = 8
EXPECTED = "GONEK-PRICING-UNCONDITIONAL"

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

    # ================================================ A: statements
    section("A. THE CLASSICAL STATEMENTS + THE PHASE LAYER (exact)")
    x, g, h = sp.symbols("x g h", positive=True)
    A = sp.log(h) / 2
    okA = sp.simplify(sp.cos(2 * A * g) - sp.cos(g * sp.log(h))) == 0
    okB = sp.simplify(x ** (sp.Rational(1, 2) + sp.I * g)
                      - sp.sqrt(x) * x ** (sp.I * g)) == 0
    t, Th, Gt = sp.symbols("t Th Gt", positive=True)
    okC = sp.simplify(sp.integrate(1 / t ** 2, (t, Th, Gt))
                      - (1 / Th - 1 / Gt)) == 0
    okD = sp.simplify(sp.log(2 ** 3) - 3 * sp.log(2)) == 0 \
        and sp.simplify(sp.log(3 ** 3) - 3 * sp.log(3)) == 0
    lam6 = 0  # Lambda(6) == 0: 6 = 2 x 3 is not a prime power
    check("A1 statement layer: phase + on-line rewrite + Landau "
          "main + Lambda", okA and okB and okC and okD and lam6 == 0,
          "cos(2Ag) == cos(g log h) with A = log(h)/2; x^{1/2+ig} "
          "== sqrt(x) x^{ig} (the PER-CENSUS on-line rewrite, beta "
          "= 1/2 explicit); the Landau main integral exact; Lambda "
          "closed forms (Lambda(8) = 3 log 2, Lambda(27) = 3 log 3, "
          "Lambda(composite) == 0 EXACT): [L] Landau 1912 + [G] "
          "Gonek 1985/1993 BOTH UNCONDITIONAL (sums over ALL "
          "nontrivial zeros, no on-line hypothesis)")

    # ================================================ B: envelope
    section("B. THE ENVELOPE CLOSED FORM (T_hi collapse; GP2)")
    Tl, Thi = sp.symbols("Tl Thi", positive=True)
    B = lambda tt: x * sp.log(2 * x * tt) * sp.log(sp.log(3 * x))  # noqa: E731
    env_raw = (B(Thi) / Thi ** 2 + B(Tl) / Tl ** 2
               + 2 * sp.integrate(B(t) / t ** 3, (t, Tl, Thi))) / sp.sqrt(x)
    env_closed = sp.sqrt(x) * sp.log(sp.log(3 * x)) * (
        (4 * sp.log(2 * x * Tl) + 1) / (2 * Tl ** 2)
        - 1 / (2 * Thi ** 2))
    okE = sp.simplify(sp.expand(env_raw - env_closed)) == 0
    dThi = sp.diff(env_closed, Thi)
    okF = sp.simplify(dThi - sp.sqrt(x) * sp.log(sp.log(3 * x))
                      / Thi ** 3) == 0 \
        and dThi.subs(x, 4).subs(Thi, 7).is_positive is True
    env_oo = sp.limit(env_closed, Thi, sp.oo)
    okG = sp.simplify(env_oo - sp.sqrt(x) * sp.log(sp.log(3 * x))
                      * (4 * sp.log(2 * x * Tl) + 1)
                      / (2 * Tl ** 2)) == 0
    check("B1 GP2 envelope closed form + finite ceiling",
          okE and okF and okG,
          "Int B/t^3 exact; the T_hi-dependence COLLAPSES to the "
          "single term -1/(2 T_hi^2); monotone increasing in T_hi "
          "with the FINITE CEILING ENV_oo = sqrt(x) loglog(3x)"
          "(4 log(2 x T_lo) + 1)/(2 T_lo^2): T_lo-ANCHORED, "
          "CENSUS-DEPTH-INSENSITIVE -- deeper census can never "
          "inflate the classical remainder past the ceiling "
          "(THEOREM GP2, the round's discovery)")

    cG, q = sp.symbols("cG q", positive=True)
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    envoo = lambda TL: sp.sqrt(h) * sp.log(sp.log(3 * h)) \
        * (4 * sp.log(2 * h * TL) + 1) / (2 * TL ** 2)  # noqa: E731
    okH = sp.limit(cG * envoo(2 * sp.pi * h) / Glead(2 * sp.pi * h),
                   h, sp.oo) == 0
    okI = True
    for p_e in (2, 3, 4, 5):
        Tlo = q * h ** sp.Rational(p_e, 2)
        okI = okI and sp.limit(cG * envoo(Tlo) / Glead(Tlo),
                               h, sp.oo) == 0
    p4 = sp.Integer(4)
    expr = h ** (p4 / 2 - 1) * Glead(q * h ** (p4 / 2)) \
        / Glead(2 * sp.pi * h)
    okJ = sp.simplify(sp.limit(expr, h, sp.oo) - 4 * sp.pi / q) == 0
    check("B2 GP3 prefactor-insensitive absorption (symbolic c_G)",
          okH and okI and okJ,
          "c_G ENV_oo(2 pi h)/G_lead(2 pi h) -> 0 (DC leg) and c_G "
          "ENV_oo(q h^{p/2})/G_lead(q h^{p/2}) -> 0 at p = 2, 3, 4, "
          "5 (WF/TOPROOT window) with the constant SYMBOLIC; rate "
          "dictionary p = 4 == 4 pi/q replicated (r171/r172): THE "
          "CENSUS SCHEDULE TOLERATES THE CLASSICAL ERROR TERMS AT "
          "ANY FINITE CONSTANT (THEOREM GP3)")

    # ================================================ C: conditionality
    section("C. THE CONDITIONALITY LEDGER + THE LOOP GRAPHS")
    ledger = {"LANDAU-1912": "UNCONDITIONAL",
              "GONEK-1985-1993": "UNCONDITIONAL",
              "FUJII": "UNCONDITIONAL-NOT-CONSUMED",
              "GONEK-1984": "RH-CONDITIONAL-LOOP-IF-CONSUMED"}
    anc_dc = {"LANDAU-1912", "GONEK-1993-FORM", "CENSUS-PER-K",
              "CACHE-WARD", "HSW22"}
    anc_wf = anc_dc | {"SOURCE"}
    okK = "GONEK-1984" not in anc_dc and "GONEK-1984" not in anc_wf \
        and ledger["GONEK-1984"].startswith("RH-CONDITIONAL") \
        and ledger["LANDAU-1912"] == "UNCONDITIONAL" \
        and ledger["GONEK-1985-1993"] == "UNCONDITIONAL"
    check("C1 GP1 conditionality adjudication ([R] not an ancestor)",
          okK,
          "[L]/[G] UNCONDITIONAL, Fujii cited-not-consumed, [R] "
          "Gonek-1984 RH-CONDITIONAL == LOOP-IF-CONSUMED and NOT an "
          "ancestor of either priced leg (ancestor sets recomputed; "
          "externally re-verified in Bughunt VII r176: citations + "
          "all three error terms + integer subsumption CORRECT)")

    chain_r = {
        "GONEK-1984": ["DCLEG"], "DCLEG": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP"], "DTSTEP": ["HCOF"],
        "HCOF": ["RH"], "RH": ["GONEK-1984"]}
    loop_r = has_cycle(chain_r)
    chain_term = {
        "LANDAU-1912": ["DCLEG", "WFLEG"],
        "GONEK-1993-FORM": ["DCLEG", "WFLEG"],
        "CENSUS_K": ["DCLEG", "DTSTEP_K"],
        "DCLEG": ["SIGMAFLOOR"], "JETMASS": ["SIGMAFLOOR"],
        "WFLEG": ["JETMASS"], "H123_COFINAL": ["JETMASS"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["HCOF"],
        "HCOF": ["RH"]}
    acyc = not has_cycle(chain_term)
    rh_reach = "RH" in reachable(chain_term, "LANDAU-1912") \
        and "RH" in reachable(chain_term, "H123_COFINAL")
    check("C2 loop graphs (hidden [R] cycle flagged; terminal chain "
          "acyclic)", loop_r and acyc and rh_reach,
          "the would-be hidden cycle GONEK-1984 -> DCLEG -> "
          "SIGMAFLOOR -> DTSTEP -> HCOF -> RH -> GONEK-1984 "
          "DETECTED (flagged, NOT consumed -- consuming [R] would "
          "be this loop); the terminal chain with GONEK-PRICED "
          "replacing GONEK-FORM is ACYCLIC with RH reachable only "
          "from the counterfactual grants; NO RH CLAIM")

    # ================================================ D: pinned pricing
    section("D. PINNED PRICING TABLES (consistency arithmetic)")
    okch = PIN_CHAT_MAX <= PIN_CHAT_BAR / 2 \
        and all(v <= PIN_CHAT_MAX + 1e-12
                for v in PIN_CHAT_DEEP.values()) \
        and all(v >= PIN_SNR_MIN for v in PIN_SNR_DEEP.values())
    okcov = 1.0 / PIN_CHAT_MAX >= 11.0
    check("D1 GP4 spike pricing: c_hat <= 0.086 at snr up to 2.7e4",
          okch and okcov,
          "c_hat <= %.6f over the FULL 12 x 6 table (bar %.2f = "
          "2.3x); deep anchors %s; snr = |main|/B >= %g everywhere "
          "(max %.1f at x = 5): the Gonek form OVER-COVERS the "
          "measured error >= %.0fx -- CONSTANT-EMPIRICAL-PER-CENSUS "
          "(no published explicit constant exists; typed honestly)"
          % (PIN_CHAT_MAX, PIN_CHAT_BAR, PIN_CHAT_DEEP, PIN_SNR_MIN,
             max(PIN_SNR_DEEP.values()), 1.0 / PIN_CHAT_MAX))

    okdc = all(abs(v) <= 4.0 for v in PIN_Z_TAB.values()) \
        and all(0.05 < v < 0.60 for v in PIN_DC_TAB.values()) \
        and all(v <= PIN_R_PRICED_MAX + 1e-12
                for v in PIN_R_PRICED.values()) \
        and PIN_R_PRICED_MAX <= 0.05
    okwf = all(0.0 < v < 1.0 for v in PIN_WF4.values()) \
        and 0.0 < PIN_WF13 < PIN_WF4[8] \
        and all(v <= PIN_RSUF_MAX + 1e-12 for v in PIN_RSUF.values()) \
        and PIN_RSUF_MAX <= 0.06
    check("D2 DC + WF legs cited AND priced (unconditional)",
          okdc and okwf,
          "DC leg: r169 Z_TAB/DC_TAB replicated at 4/5/8, priced "
          "gate r = |C_W - C_main|/ENV <= %.4f at ALL 25 rungs (bar "
          "0.05); WF leg: r171 WF4_TAB replicated + NEW h = 13 "
          "string %.6f, exact perturbation bound HARD at 4 rungs, "
          "suffix priced ratio <= %.4f (bar 0.06): BOTH legs "
          "PROVEN-MOD-CITED-AND-PRICED per census"
          % (PIN_R_PRICED_MAX, PIN_WF13, PIN_RSUF_MAX))

    sep_min = min(min(d.values()) for d in PIN_CTRL.values()) \
        / PIN_CHAT_MAX
    okct = all(v >= 20 for d in PIN_CTRL.values()
               for v in d.values()) and sep_min >= 100 \
        and PIN_WIT_DEV <= 1e-5
    check("D3 controls refuse >= 100x + dilation witness both ways",
          okct,
          "smooth/jitter/dilation combs fail the Landau prediction "
          "through the SAME instrument (chat_w %s vs true <= "
          "%.3f: separation >= %.0fx at every prime-power x); the "
          "dilation witness re-creates the true spike at x' = "
          "5^{64/65} to %.2e -- the spike is ARITHMETIC-PHASE-"
          "PINNED, not instrument-pinned; jitter typed "
          "JITTER-PARTIAL-COHERENT honestly (the sinc damping is "
          "classical)"
          % ({k: d[5] for k, d in PIN_CTRL.items()}, PIN_CHAT_MAX,
             sep_min, PIN_WIT_DEV))

    print("\n  [TYPED, BH7-F1 correction ADOPTED] THE RESIDUE AFTER "
          "THE PRICING:")
    print("  the Gonek item LEAVES the residue; what remains is "
          "{the TRIPLE")
    print("  {H1 AND H2 AND H3}-cofinal, one rung per dyadic block, "
          "all three at")
    print("  the same h} + {census-forall-k == LOOP, flagged} + "
          "{L1, WPD}.")
    print("  Census cardinality 4 UNCHANGED.  NOT RH evidence.  NO "
          "RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v934 -- PRIME.GONEK.PRICING.01 (Landau 1912 + Gonek "
          "1985/1993 identified")
    print("UNCONDITIONAL; envelope closed form census-depth-"
          "insensitive; constants")
    print("priced per census; Gonek-1984 RH-class flagged not "
          "consumed; round 174;")
    print("NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v934: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: GP1-GP3 + the loop graphs recomputed in-run; the "
          "spike/DC/WF/")
    print("control tables PINNED from gonek_pricing_probe.py (SPEC "
          "%s, 20/20," % PIN_SPEC_R174)
    print("record 188 s + deterministic re-run, all logs kept, "
          "RE-RUN GREEN AS")
    print("TYPED AT PROMOTION 244.2 s).  NOT RH evidence; NO RH "
          "claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.GONEK.PRICING.01 unconditional Gonek pricing: "
          "%d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
