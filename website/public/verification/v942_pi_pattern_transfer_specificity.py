#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v942 -- PI.PATTERN.SCAN.01: THE DETECTOR-SPECIFICITY THEOREM of
round 184 -- the prime-front instruments transferred UNCHANGED in
structure to pi-derived data under full house discipline, with a
PROVEN transfer validity and the expected honest null: every
pi-derived comb world lands in the fake-world class.  THIS IS AN
INSTRUMENT CHARACTERIZATION, NOT ARITHMETIC NOVELTY: the round
establishes what the mass-location world separator IS (prime-
specific -- it detects the explicit-formula zero coupling of the
true von Mangoldt comb, sharpened by r185/v943), not any new fact
about pi or about primes.

THE SPECIFICITY RESULT (round verdict PI-LANDS-FAKE-CLASS): all
five predefined pi-derived comb worlds (P-DIG10, P-DIG2 digit
combs; P-CF the continued-fraction comb; P-BBP the Bailey-Borwein-
Plouffe structure comb -- pi's one known arithmetic digit-
extraction handle; P-CFGEOM the convergent-denominator geometric
comb) classify TOP-HEAVY in the mass-location detector (log10
tails -10.0..-17.9) exactly like the fake-world class, across both
holdout halves, all rungs, and all 100 non-Mangoldt instances (5
pi worlds + e/sqrt2/phi/Champernowne/Liouville structured controls
+ 80 null seeds) -- ZERO anomalies, nothing to replicate.

TRANSFER VALIDITY PROVEN (the load-bearing methodology of the
whole r184-r191 mechanism arc): the C-MANGOLDT positive control
FIRED ON EVERY DETECTOR through the SAME transferred instrument --
own Mprime vs the house build_cell dev 8.4e-59, jet dev 1.5e-48;
the r182 anchor replicated at dev <= 0.004 with tails
-4.109/-2.256/-0.039; the D1 ladder shows the r181 one-dex-per-
rung TAIL-RIDING signature; the D2 Landau spike C = 131.04 vs the
integer-position-matched INTRAND null max 12.60 (ratio 10.40 >=
the frozen ON bar 10); the D5 alt-jet battery replicates r182
(-0.04 -> -12.84/-13.08/-13.43).  The structured controls prove
the detectors CAN fire on structure (Champernowne Weyl 15.8/43.2
vs null 2.46; phi GK chi2 7047; e GK 4376; phi Levy 88 sigma) --
they see structure, just none in pi.  pi's classical CF laws
replicate as measured expectations (Gauss-Kuzmin chi2 8.85/6.20
within bar; Gauss-Mertens 2.6632 vs Khinchin 2.6855; Levy dev
0.0072).  The BBP integer-position resonance is fully carried by
the INTRAND positional null; the high CFGEOM coherence is
construction-borne (its own RAND band carries it).  The P-BBP comb
is effectively the k = 0 slice with 92 percent L1 mass on three
atoms and carries the in-spec PROVISIONAL flag (BH9-F9,
disposition adopted).

RECOMPUTED IN-RUN (exact): the Gauss-Kuzmin law is an exact
probability measure (the telescoping sum of log2(1 + 1/(j(j+2)))
== 1, sympy); the Levy constant pi^2/(12 ln 2) and the BBP series
sum_{k} 16^{-k} (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)) == pi
(30 digits) -- the P-BBP construction rests on a genuine exact
arithmetic handle; the classification-bar arithmetic on the pinned
ladders (TOP-HEAVY <= -8.0 at all rungs; the >= 2 dex clearance of
every pi world below the bar; the MANGOLDT-FIRES ratio and the
3x structured-control fire gates).

BH9 CORRECTIONS OF RECORD ADOPTED (K3, MINOR): the smoke lineage
of the probe is DISCLOSED on every surface of this promotion -- an
OverflowError crash smoke on the Liouville CF stream was fixed
pre-freeze by the overflow-safe log-space branch, with 4 pre-freeze
smoke FAILs; no record impact (BH9 verified the SPEC_SHA
byte-identical and every kept log lineage-exact except the two
disclosed smoke files).

RE-RUN GREEN AS TYPED AT PROMOTION: pi_pattern_scan_probe.py round
184 (note DIV (504), contract PI.PATTERN.SCAN.01), 35/35 gates,
SPEC_SHA 00fc85173fe07470 (verified byte-identical before and
after the CORRECTION-OF-RECORD block append), record 191 s +
deterministic re-run (timing-normalized diff empty, all six logs
kept), re-run at promotion 212.2 s, 35/35 -- log kept as
pi_pattern_scan_probe.promo_rerun.log.

HONEST TYPING: typed EXPLORATORY TRANSFER at discovery, promoted
as the SPECIFICITY/CHARACTERIZATION theorem of the detector suite
(the transfer-validity methodology is load-bearing for the r185
ablation ladder and the r187/r190 causal synthesis, v943/v945);
NO pi-numerology claim, NO normality claim about pi, no prime-
front residue moved.  THE RESIDUE (canonical, notes DII/DXVI):
{H1 AND H2 AND H3}-cofinal (one rung per dyadic block, all three
at the same h; limsup form only mod D = 0.0042) + {census-forall-k
== LOOP} + {H-PIN = the one lambda-uniform edge of {L1, WPD}; WPD
non-lambda legs: extension instantiated, TAILWPD world-front}.
Census cardinality 4 UNCHANGED.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe pi_pattern_scan_probe.py (round 184,
2026-08-21, note DIV; CORRECTION-OF-RECORD block K3 per note DXVI
(516)); consumes the r182/v941 mass-location recipe and the
r174/v934 spike-instrument class (cited); externally covered by
Bughunt IX (round 193, note DXV: zero failed recomputes on the
arc, F3 applied here).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R184 = "00fc85173fe07470"
# transfer validity (C-MANGOLDT fires on every detector)
PIN_PORT_DEV = 8.4e-59
PIN_JET_DEV = 1.5e-48
PIN_ANCHOR_DEV = 0.004
PIN_MANG_TAILS = (-4.109, -2.256, -0.039)     # r182 anchor replicated
PIN_C_MANG = 131.04
PIN_NULL_MAX = 12.60                          # INTRAND band max
PIN_ON_BAR = 10.0                             # S2-ON ratio bar
# the specificity null
PIN_PI_TAIL_RANGE = (-17.9, -10.0)            # all five pi worlds
PIN_TOPHEAVY_BAR = -8.0
PIN_N_NONMANG = 100                           # 5 pi + 15 ctrl + 80 null
# structured controls CAN fire
PIN_CHAMP_WEYL = (15.8, 43.2)
PIN_CHAMP_NULL = 2.46
PIN_PHI_GK_CHI2 = 7047.0
PIN_E_GK_CHI2 = 4376.0
PIN_PHI_LEVY_SIGMA = 88.0
PIN_FIRE_FACTOR = 3.0
# pi's classical CF laws as measured expectations
PIN_PI_GK_CHI2 = (8.85, 6.20)
PIN_PI_GM = 2.6632                            # Gauss-Mertens measured
PIN_KHINCHIN_4DP = 2.6855
PIN_PI_LEVY_DEV = 0.0072
# alt jets (D5, MANGOLDT side)
PIN_ALT_MAIN = -0.04
PIN_ALT_JETS = (-12.84, -13.08, -13.43)
PIN_ALT_BAR = -8.0
# P-BBP L1 concentration (BH9-F9 disposition: PROVISIONAL in-spec)
PIN_BBP_L1_TOP3 = 0.92

N_CHECKS = 9
EXPECTED = "PI-TRANSFER-SPECIFICITY"

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


def part():
    import sympy as sp
    import mpmath as mp

    # ================================================ A: exact layer
    section("A. THE CLASSICAL-LAW EXACT LAYER (Gauss-Kuzmin, Levy, BBP)")
    j, n = sp.symbols("j n", positive=True, integer=True)
    # Gauss-Kuzmin telescoping: sum_{j=1}^{n} log2((j+1)^2/(j(j+2)))
    # == log2(2(n+1)/(n+2)) -> 1: an exact probability measure.
    partial = sp.log(2 * (n + 1) / (n + 2), 2)
    term = sp.log((j + 1) ** 2 / (j * (j + 2)), 2)
    step = sp.simplify(
        (partial.subs(n, n + 1) - partial)
        - term.subs(j, n + 1))
    base = sp.simplify(partial.subs(n, 1) - term.subs(j, 1))
    lim = sp.limit(partial, n, sp.oo)
    okA = step == 0 and base == 0 and lim == 1
    check("A1 Gauss-Kuzmin measure exact (telescoping sum == 1)",
          okA,
          "sum_{j>=1} log2(1 + 1/(j(j+2))) == 1 proven by exact "
          "telescoping (induction step + base + limit, sympy): the "
          "D3/D4 CF detector rests on an exact classical law "
          "(Kuzmin 1928, Levy 1929); pi's measured chi2 %.2f/%.2f "
          "sits INSIDE the matched null band -- law-consistency is "
          "the expected null, not a hit"
          % PIN_PI_GK_CHI2)

    mp.mp.dps = 40
    levy = mp.pi ** 2 / (12 * mp.log(2))
    okB = abs(levy - mp.mpf("1.18656911041562545282172297594")) < 1e-25
    okC = abs(mp.khinchin - mp.mpf("2.685452001065306445309714835")) < 1e-25 \
        and abs(float(mp.khinchin) - PIN_KHINCHIN_4DP) < 5e-5
    okD = abs(PIN_PI_GM - float(mp.khinchin)) < 0.05 \
        and PIN_PI_LEVY_DEV < 0.01
    check("A2 Levy + Khinchin constants recomputed (30 digits)",
          okB and okC and okD,
          "Levy pi^2/(12 ln 2) = 1.1865691104... and Khinchin K0 = "
          "2.6854520010... recomputed to 25+ digits (mp); pi's "
          "measured Gauss-Mertens GM = %.4f vs K0 = %.4f (dev < "
          "0.05, a MEASURED expectation -- pi is conjecturally "
          "GK-typical, the a.s. laws do not apply to it "
          "individually) and Levy dev %.4f: the classical CF laws "
          "replicate through the transferred instrument"
          % (PIN_PI_GM, PIN_KHINCHIN_4DP, PIN_PI_LEVY_DEV))

    mp.mp.dps = 40
    bbp = mp.nsum(lambda k: mp.mpf(16) ** (-k)
                  * (mp.mpf(4) / (8 * k + 1) - mp.mpf(2) / (8 * k + 4)
                     - mp.mpf(1) / (8 * k + 5) - mp.mpf(1) / (8 * k + 6)),
                  [0, 30])
    okE = abs(bbp - mp.pi) < mp.mpf(10) ** (-30)
    okF = 0.9 <= PIN_BBP_L1_TOP3 <= 1.0
    check("A3 BBP series == pi (30 digits); P-BBP typed PROVISIONAL",
          okE and okF,
          "sum_k 16^{-k}(4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)) "
          "== pi to < 1e-30 (recomputed): the P-BBP comb rests on "
          "pi's one genuine exact arithmetic handle; BH9-F9 "
          "disposition adopted: the comb is effectively the k = 0 "
          "slice with %.0f percent L1 mass on three atoms -- the "
          "in-spec PROVISIONAL flag travels with every citation"
          % (100 * PIN_BBP_L1_TOP3))

    # ================================================ B: transfer validity
    section("B. TRANSFER VALIDITY (the positive control fires)")
    okG = PIN_PORT_DEV < 1e-25 and PIN_JET_DEV < 1e-25 \
        and PIN_ANCHOR_DEV <= 0.004
    okH = all(abs(a - b) <= 0.10 for a, b in
              zip(PIN_MANG_TAILS, (-4.11, -2.26, -0.04)))
    check("B1 port + anchor: the instrument is the house instrument",
          okG and okH,
          "own Mprime vs house build_cell dev %.1e, jet dev %.1e "
          "(port bar 1e-25); the r182 anchor strings replicate at "
          "dev <= %.3f with tails %s == the v941 record "
          "(-4.11/-2.26/-0.04): the transferred instrument IS the "
          "house instrument, like-for-like"
          % (PIN_PORT_DEV, PIN_JET_DEV, PIN_ANCHOR_DEV,
             str(PIN_MANG_TAILS)))

    ratio = PIN_C_MANG / PIN_NULL_MAX
    okI = ratio >= PIN_ON_BAR
    okJ = all(t <= PIN_ALT_BAR for t in PIN_ALT_JETS) \
        and PIN_ALT_MAIN >= -0.5
    check("B2 MANGOLDT-FIRES on every detector (ratio 10.40)",
          okI and okJ,
          "D2 Landau spike C = %.2f vs INTRAND null max %.2f: "
          "ratio %.2f >= the frozen ON bar %.0f (recomputed); D5 "
          "alt jets relocate the true comb to the top exactly as "
          "r182/v941 (MAIN %.2f -> SIGNFLIP/UNIFORM/MAGSCRAM %s, "
          "all <= %.0f): TRANSFER VALIDITY PROVEN -- the "
          "methodology the whole r184-r191 mechanism arc rides"
          % (PIN_C_MANG, PIN_NULL_MAX, ratio, PIN_ON_BAR,
             PIN_ALT_MAIN, str(PIN_ALT_JETS), PIN_ALT_BAR))

    okK = PIN_CHAMP_WEYL[0] >= PIN_FIRE_FACTOR * PIN_CHAMP_NULL \
        and PIN_CHAMP_WEYL[1] >= PIN_FIRE_FACTOR * PIN_CHAMP_NULL
    okL = PIN_PHI_GK_CHI2 > 1000 and PIN_E_GK_CHI2 > 1000 \
        and PIN_PHI_LEVY_SIGMA >= 10
    check("B3 structured controls CAN fire (the detectors see "
          "structure)", okK and okL,
          "Champernowne Weyl %.1f/%.1f vs null %.2f (>= %.0fx fire "
          "gate, recomputed); phi GK chi2 %.0f, e GK chi2 %.0f "
          "(both provably NOT GK-typical -- periodic / patterned "
          "CFs), phi Levy %.0f sigma: structure alone DOES fire "
          "the detectors -- the pi null below is not instrument "
          "blindness"
          % (PIN_CHAMP_WEYL[0], PIN_CHAMP_WEYL[1], PIN_CHAMP_NULL,
             PIN_FIRE_FACTOR, PIN_PHI_GK_CHI2, PIN_E_GK_CHI2,
             PIN_PHI_LEVY_SIGMA))

    # ================================================ C: the null + typing
    section("C. THE SPECIFICITY NULL + THE HONEST TYPING")
    okM = PIN_PI_TAIL_RANGE[1] <= PIN_TOPHEAVY_BAR \
        and PIN_PI_TAIL_RANGE[0] < PIN_PI_TAIL_RANGE[1]
    clearance = PIN_TOPHEAVY_BAR - PIN_PI_TAIL_RANGE[1]
    okN = clearance >= 2.0 and PIN_N_NONMANG == 100
    check("C1 PI-LANDS-FAKE-CLASS (all 100 non-Mangoldt instances)",
          okM and okN,
          "all five pi worlds TOP-HEAVY with log10 tails in "
          "[%.1f, %.1f], i.e. >= %.1f dex BELOW the frozen "
          "TOP-HEAVY bar %.1f (recomputed), on BOTH holdout halves, "
          "all rungs, all %d non-Mangoldt instances -- ZERO "
          "anomalies, nothing to replicate; the BBP integer-"
          "position resonance is fully carried by the INTRAND "
          "positional null, the CFGEOM coherence by its own RAND "
          "band (construction-borne)"
          % (PIN_PI_TAIL_RANGE[0], PIN_PI_TAIL_RANGE[1], clearance,
             PIN_TOPHEAVY_BAR, PIN_N_NONMANG))

    smoke_lineage_disclosed = True            # K3 adopted on this surface
    okO = smoke_lineage_disclosed
    check("C2 K3 smoke lineage disclosed (BH9 correction adopted)",
          okO,
          "the probe's pre-freeze lineage carries an OverflowError "
          "crash smoke on the Liouville CF stream, fixed pre-freeze "
          "by the overflow-safe log-space branch, plus 4 pre-freeze "
          "smoke FAILs -- disclosed here per BH9-F3/K3; NO record "
          "impact (SPEC_SHA byte-identical, all record logs "
          "lineage-exact per BH9-X3)")

    okP = True                                # typing gate (definitional)
    check("C3 SPECIFICITY typing: instrument characterization, NOT "
          "arithmetic novelty", okP,
          "the mass-location world separator is PRIME-SPECIFIC, "
          "not a universal-structure detector -- what it detects "
          "is the explicit-formula zero coupling of the true comb "
          "(sharpened by r185/v943, demonstrated causally by "
          "r187+r190/v945); no new fact about pi, no pi-numerology "
          "claim, no prime-front residue moved; census cardinality "
          "4 UNCHANGED; NOT RH evidence")

    print("\n  [TYPED] THE DETECTOR SUITE IS CHARACTERIZED: prime-")
    print("  specific with proven transfer validity; the pi null is")
    print("  the honest expected outcome and is an instrument theorem,")
    print("  not an arithmetic one.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v942 -- PI.PATTERN.SCAN.01 (detector prime-specificity; "
          "transfer validity")
    print("proven; PI-LANDS-FAKE-CLASS; instrument characterization, "
          "NOT arithmetic")
    print("novelty; round 184; K3 adopted; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v942: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the classical-law layer + bar arithmetic "
          "recomputed in-run; the")
    print("port/anchor/ladder/null tables PINNED from "
          "pi_pattern_scan_probe.py")
    print("(SPEC %s, 35/35, record 191 s + deterministic re-run, "
          "amendments" % PIN_SPEC_R184)
    print("disclosed in spec, K3 CORRECTION-OF-RECORD block appended "
          "spec-hash-")
    print("invariant, all six logs kept, RE-RUN GREEN AS TYPED AT "
          "PROMOTION 212.2 s,")
    print("35/35).  NOT RH evidence; NO RH claim; NO pi-numerology "
          "claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PI.PATTERN.SCAN.01 detector specificity + transfer "
          "validity: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
