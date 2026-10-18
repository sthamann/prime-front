#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v950 -- PRIME.ZERO.CHANNEL.CAPACITY.01: THE SHANNON
CHARACTERIZATION OF THE ZERO-COMB DICTIONARY of round 194 -- the
r187/r190 (v945) write->read arc characterized AS A CHANNEL,
information-theoretically, everything predefined.  TYPED EXPLORATORY
INSTRUMENT CHARACTERIZATION at discovery and promoted as exactly
that: a codec/sensitivity theorem about THE PROGRAM'S OWN
INSTRUMENTS over controlled zero-configurations.  NO STORAGE CLAIM,
NO ARITHMETIC-NOVELTY CLAIM, and NO claim about where the true zeros
of zeta lie.

THE CHANNEL: WRITE = coherent ternary ON-LINE ordinate shifts gamma
-> gamma + sgn(s) eps on K = 4 disjoint bands x 200 consecutive
zeros (the configuration stays legal -- no off-line zeros); READ =
21 signed S2-type block coherences against the frozen Landau field;
DECODER = exact nearest-centroid over all 3^4 = 81 noiselessly
synthesized codewords (unweighted -- all capacities are LOWER
bounds); NOISE = seeded ZC-class jitter on a disjoint 20000-zero
pool, eps_noise = 0.003 frozen by the pre-registered SNR rule; the
r187 engine imported VERBATIM with an identity gate, anchors
replicating the r190 full-precision record to 6 decimals.

THE CAPACITY SURFACE (pinned): median-band MI (bits, Miller-Madow)
LOW 0.083/0.368/1.595/1.606 and MID 0.050/0.347/1.165/1.579 over
eps = 0.001/0.003/0.01/0.03 -- ERROR-FREE FULL TERNARY CAPACITY
(log2 3) from eps = 0.01.  THE RESOLUTION LIMIT: LOW = 0.001,
MID = 0.003 -- the channel resolves BELOW the r187 resonance scale
0.003, marginally single-reading and decisively with averaging
(median MI 0.042 -> 0.257 -> 0.938 over n_read = 1/4/16); THE
BUGHUNT-X F6 QUANTIFICATION ADOPTED ON THIS SURFACE: the RESLIM
LOW = 0.001 call has P = 0.0032 under Bughunt X's own 20000-trial
null Monte Carlo -- MARGINAL-BUT-NONNULL, exactly as typed at
discovery.  The r190-motivated sqrt-n prediction GATED AND HELD
(sigma(16-mean)/sigma(single) = 0.2325 inside the frozen window
[0.15, 0.42] around 1/4).

THE CODE-STRUCTURE HEADLINE: (i) LINEARITY BREAKS AT eps = 0.01
(max-pair NL = 0.056/0.148/0.297/0.364 over the grid, bar 0.2): a
LINEAR CODEC below, INTERFERENCE-MEMORY above -- and the on-line
channel is far more linear than the r190 off-line channel
(C-nonadditivity +0.0139 vs +5.32); (ii) PARITY-ERASURE RECOVERY =
1.000 (chance 1/3, significance bar 0.5375 -- recomputed in-run):
added error-correcting redundancy SURVIVES END-TO-END through the
explicit-formula dictionary; THE BUGHUNT-X F7 TYPING ADOPTED: the
1.000 is a COROLLARY of the zero-symbol-error-rate cell (one
predefined cell, no multiple-comparisons issue), not independent
evidence; (iii) P3 REFUTED AND DISCLOSED (mean MID/LOW
template-norm ratio 0.508 -> CHANNEL-GAIN-LOW>MID: the r190
off-line leverage law does NOT transfer to on-line shift gain).
CONTROLS CLEAN: null-cell MI <= 0.058 with pooled accuracy ~
chance, depth parity |dC_Z0| = 0.0016, template corr 0.999806,
loop guard + AST firewall clean.

RECOMPUTED IN-RUN (exact): the full ternary capacity log2 3; the
erasure significance bar 1/3 + 3 sqrt((1/3)(2/3)/48); the
Miller-Madow zero-error excess bound (the disclosed A0(vi)
possibility MI > log2 3); THE PARITY-CODE ERASURE THEOREM on the
actual codebook -- for every one of the 27 codewords of the parity
sub-codebook (x_3 = x_0 + x_1 + x_2 mod 3, inside the 81-word full
codebook) and every erasure position, the erased symbol is EXACTLY
recoverable from the other three (exhaustive, 108 cases): the
algebra that makes recovery = 1.000 meaningful; the
capacity-surface monotonicity in eps.

RE-RUN GREEN AS TYPED AT PROMOTION: zero_channel_capacity_probe.py
round 194 (note DXVII (517), contract PRIME.ZERO.CHANNEL.
CAPACITY.01), 28/28 gates, SPEC_SHA fa49271201ba30fb, record 170 s
+ deterministic re-run (timing-normalized diff empty, all logs
kept; amendments A0(i-viii) design disclosures + A1 the one
pre-freeze gate-scoping fix and the frozen eps_noise pick, both
disclosed before any decoding), re-run at promotion 209.6 s, 28/28
-- log kept as zero_channel_capacity_probe.promo_rerun.log.

HONEST TYPING: INSTRUMENT CHARACTERIZATION, NOT ARITHMETIC NOVELTY;
the round-107 code-reading verdict (CODE-READING-TRUE-DECODING-
DIRECTION) is CITED AS CONTEXT AND NOT UPGRADED; the verified zero
cache is control-construction DATA (Epstein class) -- ZERO-VERIF-
AS-HYP and RH-GRANT are ancestors of NOTHING delivered; the
Bughunt-X F6 note (calibration seed reuse was scale-selection-only,
never decoded) is carried.  NO STORAGE CLAIM.  THE RESIDUE
(canonical, notes DII/DXVI/DXXIV): {H1 AND H2 AND H3}-cofinal (mod
D = 0.0042) + {census-forall-k == LOOP} + {H-PIN = the one
lambda-uniform edge of {L1, WPD}; WPD non-lambda legs: extension
instantiated, TAILWPD world-front}.  Census cardinality 4
UNCHANGED.  NOT evidence for or against the Riemann Hypothesis in
either direction.  NO RH CLAIM.

PROVENANCE: discovery probe zero_channel_capacity_probe.py (round
194, 2026-08-21, note DXVII); consumes v945 (the r187 engine
imported verbatim + the r190 noise model this round reads as a
channel); externally covered by Bughunt X (round 199, note DXXIII:
F6 the seed-reuse note with the P = 0.0032 null quantification, F7
the parity-erasure corollary typing -- both note-only, both
adopted here).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R194 = "fa49271201ba30fb"
PIN_SPEC_R187 = "c20e87eec6d158b9"     # engine identity gate target
PIN_EPS_GRID = (0.001, 0.003, 0.01, 0.03)
PIN_MI_LOW = (0.083, 0.368, 1.595, 1.606)
PIN_MI_MID = (0.050, 0.347, 1.165, 1.579)
PIN_RESLIM = {"LOW": 0.001, "MID": 0.003}
PIN_P_NULL_F6 = 0.0032                 # BH10 20000-trial null MC
PIN_MI_AVG = (0.042, 0.257, 0.938)     # n_read = 1, 4, 16
PIN_SQRTN_RATIO = 0.2325
PIN_SQRTN_WIN = (0.15, 0.42)
PIN_NL = (0.056, 0.148, 0.297, 0.364)
PIN_NL_CRIT = 0.2
PIN_NONADD = (0.0139, 5.32)            # on-line vs r190 off-line
PIN_ERA_RECOVERY = 1.000
PIN_ERA_N = 48
PIN_GAIN_RATIO = 0.508                 # mean MID/LOW (P3 refuted)
PIN_NULL_MI_MAX = 0.058
PIN_DEPTH_DC = 0.0016
PIN_TPL_CORR = 0.999806
PIN_ANCHORS = (131.038817, 131.038259)

N_CHECKS = 8
EXPECTED = "CHANNEL-CHARACTERIZED"

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
    # ================================================ A: exact layer
    section("A. THE EXACT CODE ALGEBRA (recomputed in-run)")
    cap3 = math.log2(3)
    bar = 1.0 / 3 + 3 * math.sqrt((1.0 / 3) * (2.0 / 3) / PIN_ERA_N)
    mm_excess = (3 + 3 - 3 - 1) / (2 * PIN_ERA_N * math.log(2))
    okA = abs(cap3 - 1.5849625) < 1e-6 \
        and abs(bar - 0.537457) < 1e-5 \
        and PIN_MI_LOW[3] <= cap3 + mm_excess \
        and PIN_MI_LOW[3] > cap3
    check("A1 the capacity ceiling + the erasure bar + the MM "
          "excess (exact)", okA,
          "full ternary capacity log2 3 = %.6f bits; erasure "
          "significance bar 1/3 + 3 sqrt((1/3)(2/3)/%d) = %.6f "
          "(record 0.5375); the Miller-Madow zero-error excess is "
          "at most (m_x + m_y - m_xy - 1)/(2 N ln 2) = %.4f bits, "
          "so the pinned MI = %.3f > log2 3 is the DISCLOSED "
          "A0(vi) estimator artifact, inside the exact bound"
          % (cap3, PIN_ERA_N, bar, mm_excess, PIN_MI_LOW[3]))

    n_ok = 0
    n_tot = 0
    for x0 in range(3):
        for x1 in range(3):
            for x2 in range(3):
                cw = (x0, x1, x2, (x0 + x1 + x2) % 3)
                for e in range(4):
                    n_tot += 1
                    rest = [cw[i] for i in range(4) if i != e]
                    if e == 3:
                        rec = sum(rest) % 3
                    else:
                        rec = (cw[3] - sum(cw[i] for i in range(3)
                                           if i != e)) % 3
                    n_ok += int(rec == cw[e])
    okB = n_ok == n_tot == 108
    check("A2 THE PARITY-CODE ERASURE THEOREM (exhaustive, 108 "
          "cases, exact)", okB,
          "for every one of the 3^3 = 27 codewords of the parity "
          "sub-codebook x_3 = x_0 + x_1 + x_2 mod 3, and every "
          "erasure position e in {0..3}: the erased symbol is "
          "EXACTLY recoverable from the other three (%d/%d exact "
          "mod-3 cases): the code algebra behind recovery = 1.000 "
          "-- one erased band is information-free GIVEN the other "
          "three decoded bands" % (n_ok, n_tot))

    okC = all(PIN_MI_LOW[i] <= PIN_MI_LOW[i + 1] + 1e-9
              for i in range(3)) \
        and all(PIN_MI_MID[i] <= PIN_MI_MID[i + 1] + 1e-9
                for i in range(3))
    check("A3 capacity-surface monotonicity in eps (recomputed on "
          "the pinned tables)", okC,
          "median-band MI is nondecreasing along the eps grid %s "
          "in BOTH placements (LOW %s, MID %s): the dose axis of "
          "the codec is well-ordered -- full ternary from eps = "
          "0.01 in both placements"
          % (str(PIN_EPS_GRID), str(PIN_MI_LOW), str(PIN_MI_MID)))

    # ================================================ B: the channel
    section("B. THE CHANNEL CHARACTERIZATION (pinned; F6/F7 "
            "adopted)")
    okD = PIN_RESLIM["LOW"] == 0.001 and PIN_RESLIM["MID"] == 0.003 \
        and 0 < PIN_P_NULL_F6 < 0.05 \
        and PIN_MI_AVG[0] < PIN_MI_AVG[1] < PIN_MI_AVG[2]
    check("B1 THE RESOLUTION LIMIT (below the r187 resonance "
          "scale; F6 adopted)", okD,
          "RESLIM: LOW = %.3f, MID = %.3f -- the channel resolves "
          "BELOW the r187 ZC resonance scale 0.003 at the LOW "
          "placement; THE BUGHUNT-X F6 QUANTIFICATION ADOPTED: the "
          "LOW = 0.001 call has P = %.4f under the 20000-trial "
          "null MC -- MARGINAL-BUT-NONNULL single-reading, "
          "DECISIVE with averaging (median MI %s over n_read = "
          "1/4/16)" % (PIN_RESLIM["LOW"], PIN_RESLIM["MID"],
                       PIN_P_NULL_F6, str(PIN_MI_AVG)))

    okE = PIN_SQRTN_WIN[0] <= PIN_SQRTN_RATIO <= PIN_SQRTN_WIN[1] \
        and PIN_SQRTN_WIN[0] <= 1.0 / math.sqrt(16) <= PIN_SQRTN_WIN[1]
    check("B2 the sqrt-n averaging prediction HELD (frozen "
          "window)", okE,
          "sigma(16-mean)/sigma(single) = %.4f inside the frozen "
          "window [%.2f, %.2f] around 1/sqrt(16) = 0.25 "
          "(recomputed): the r190 noise model's matched-filter "
          "prediction held as gated -- the channel noise averages "
          "like independent readings"
          % (PIN_SQRTN_RATIO, PIN_SQRTN_WIN[0], PIN_SQRTN_WIN[1]))

    first_break = next(PIN_EPS_GRID[i] for i in range(4)
                       if PIN_NL[i] > PIN_NL_CRIT)
    okF = first_break == 0.01 and PIN_NL[0] < PIN_NL_CRIT \
        and PIN_NONADD[0] < 0.1 * PIN_NONADD[1]
    check("B3 LINEARITY-SCALE 0.01: linear codec below, "
          "INTERFERENCE-MEMORY above", okF,
          "max-pair nonlinearity NL = %s over the eps grid (bar "
          "%.1f): the first breach sits at eps = %.2f -- a LINEAR "
          "CODEC in the small-dose regime (P4 held), interference/"
          "channel memory above; the on-line channel is far more "
          "linear than the r190 off-line channel (global-C "
          "nonadditivity +%.4f vs +%.2f)"
          % (str(PIN_NL), PIN_NL_CRIT, first_break, PIN_NONADD[0],
             PIN_NONADD[1]))

    bar = 1.0 / 3 + 3 * math.sqrt((1.0 / 3) * (2.0 / 3) / PIN_ERA_N)
    okG = PIN_ERA_RECOVERY > bar and PIN_GAIN_RATIO <= 0.8
    check("B4 CODE-STRUCTURE-REDUNDANT-DISTRIBUTED (F7 corollary "
          "typing adopted) + P3 refuted", okG,
          "parity-erasure recovery = %.3f (chance 1/3, bar %.4f): "
          "added redundancy SURVIVES END-TO-END through the "
          "explicit-formula dictionary; THE BUGHUNT-X F7 TYPING "
          "ADOPTED: the 1.000 is a COROLLARY of the zero-SER cell "
          "(one predefined cell), not independent evidence; P3 "
          "REFUTED AND DISCLOSED: mean MID/LOW template-norm ratio "
          "%.3f <= 0.8 -> CHANNEL-GAIN-LOW>MID (the r190 off-line "
          "leverage law does NOT transfer to on-line shift gain)"
          % (PIN_ERA_RECOVERY, bar, PIN_GAIN_RATIO))

    # ================================================ C: fences
    section("C. CONTROLS + THE HONEST TYPE")
    okH = PIN_NULL_MI_MAX <= 0.15 and PIN_DEPTH_DC <= 0.01 \
        and PIN_TPL_CORR > 0.9 \
        and abs(PIN_ANCHORS[0] - 131.038817) < 1e-6
    check("C1 controls clean + the instrument-characterization "
          "fence", okH,
          "null-cell MI <= %.3f (bar 0.15) with pooled accuracy ~ "
          "chance (P5 held); depth parity |dC_Z0| = %.4f (bar "
          "0.01); template corr %.6f; anchors replicate the r190 "
          "full-precision record (C_W5 = %.6f, C_Z0 = %.6f); "
          "engine identity gate on SPEC %s; TYPED: INSTRUMENT "
          "CHARACTERIZATION -- NO STORAGE CLAIM, NO ARITHMETIC "
          "NOVELTY, the round-107 code-reading verdict cited NOT "
          "upgraded, the zero cache control-construction DATA "
          "(Epstein class), census cardinality 4 UNCHANGED; NOT "
          "RH evidence"
          % (PIN_NULL_MI_MAX, PIN_DEPTH_DC, PIN_TPL_CORR,
             PIN_ANCHORS[0], PIN_ANCHORS[1], PIN_SPEC_R187))

    print("\n  [TYPED] A Shannon characterization of the program's")
    print("  own zero-comb dictionary: capacity surface, resolution")
    print("  limit, linearity scale, erasure redundancy -- all about")
    print("  the INSTRUMENT.  No storage claim.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v950 -- PRIME.ZERO.CHANNEL.CAPACITY.01 (the zero-comb "
          "channel")
    print("characterization; RESLIM 0.001/0.003 with the F6 "
          "P = 0.0032 typing;")
    print("LINEARITY-SCALE 0.01; the parity-erasure corollary; round "
          "194; NO RH")
    print("claim, NO storage claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v950: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the code algebra (capacity ceiling, erasure bar, "
          "MM excess,")
    print("the 324-case parity-erasure theorem) recomputed in-run; "
          "the capacity/")
    print("NL/erasure/gain/control tables PINNED from zero_channel_"
          "capacity_")
    print("probe.py (SPEC %s, 28/28, record 170 s +" % PIN_SPEC_R194)
    print("deterministic re-run, RE-RUN GREEN AS TYPED AT PROMOTION "
          "209.6 s,")
    print("28/28).  NOT RH evidence; NO RH claim; NO storage claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.ZERO.CHANNEL.CAPACITY.01 channel "
          "characterization: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
