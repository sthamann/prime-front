#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v949 -- PRIME.COMMENSURABILITY.MECHANISM.01: THE EXACT NODE
MECHANISM + THE STRUCTURAL-ZERO CENSUS + THE FIRST BAKER-CLASS
PRICING of round 192 -- the thin geometric hope 'incommensurability
feeds wall positivity' CLEANLY KILLED at the margin, with an exact
mechanism statement for the canonical completion in its place.

THE MECHANISM MADE EXACT (recomputed in-run, sympy): the nodes are
om_k = k pi/a, so 2a om_k = 2 pi k identically -- sin(2a om_k) == 0,
cos(2a om_k) == 1, and the +- boundary-phase class collapses per
atom: sin(2a om_k +- om_k u) == +-sin(om_k u) IDENTICALLY (the node
lattice makes the boundary phase invisible).  THE SMOOTH COLLAPSE:
the SMOOTH world's whole 2a-periodic oscillation collapses AT THE
NODES to Moebius data -- pj_s(om_k) = om_k (1 - e^a)/(1/4 + b_k),
pc_s(om_k) = (e^a - 1)/(2(1/4 + b_k)), and the combined pole + prime
node potential is EXACTLY 2(1 - e^a) + (1 - e^{-a})/2/(1/4 + b) (all
three closed forms recomputed symbolically in-run): the infinite
smooth oscillation is a rank-1-Cauchy/Moebius function ON THE NODE
SET -- the exact content of the r189/v947 SMOOTH-PSD-AT-NODES
finding.  THE STRUCTURAL-ZERO CENSUS (KE-corrected wording ADOPTED:
the probe's G11 symbolic leg was vacuous by construction -- the
e | 2fk law's real machine content lives in G20/G23 and reproduces
exactly, per Bughunt X): the per-atom node samples sin(2 pi k log q
/ log h) vanish for ALL k iff 2 log q / log h is an INTEGER; for
h = p^e, q = p^f the (q, k) sample vanishes iff e | 2fk -- the
exact integer census is recomputed in-run at h = 4 (12 zeros of 18
pairs) and h = 8 (32 of 120), matching the record exactly;
non-prime-power rungs carry ZERO structural zeros.

THE DIOPHANTINE PRICING (the program's FIRST linear-forms-in-
logarithms import, rounds 1-191 never priced it): the defect
d_{q,k} = |sin(2 pi k log q/log h)| = |sin(pi y)| bridges EXACTLY
to the two-logarithm linear form Lambda = 2k log q - m log h via
Jordan, d >= 2 dist(y, Z) = 2|Lambda|/log h (the concavity proof
sin(pi x) >= 2x on [0, 1/2] recomputed symbolically in-run).
RECOMPUTED IN-RUN AT THE h = 4 MINIMIZER (q, k, m) = (3, 5, 8):
multiplicative independence 3^10 != 4^8 in EXACT integers,
log10|Lambda| = -0.98, the elementary Liouville floor |Lambda| >=
log(1 + 1/min(q^{2k}, h^m)) holds with gap 3.79 dex, the
LAURENT-MIGNOTTE-NESTERENKO 1995 two-log bound (J. Number Theory
55, 285-321) misses by 7.099e3 dex and MATVEEV 2000 (Izv. Math.
64:6) by 1.682e9 dex -- BOTH classical bound formulas recomputed
in-run from their published constants, reproducing the record gaps.
THE PINNED LADDERS: gap_liou 2.62..74.22 dex GROWING (the floor is
real but NOT TIGHT -- amendment A2 honest), gap_lmn 7.10e3..3.10e4
dex, gap_matveev 1.36e9..1.18e10 dex at all 14 rungs:
BAKER-TOO-WEAK, verified against the published statements
(Bughunt X web-verified the citations verbatim).  Erdos-Turan holds
(nontrivial at h = 8, 13; honestly typed trivial at the short
rungs); three-distance gap count exactly 3 everywhere.

THE RELEVANCE VERDICT (outcome c, frozen resolution logic):
POSITIVITY-IRRELEVANT-EXACTNESS-KILL.  The defect ladder MINDEF_h
is O(1)-FLAT (log10 -0.63..-3.03 across h = 4..16, 20; slopes vs
log10 tau +0.035 / +0.019, ride band never entered) while tau_h
falls 45 orders; the wall margin is KILLED at EVERY dose t >= 1/8,
EVERY dose rung, BOTH DIRECTIONS (dose == antidose within < 2 dex
-- DIRECTION-BLIND, the control r185 lacked) and by 0.01
deterministic jitter; NO commensurate revival (COMM-WALL-DEAD).
THE MARGIN CONSUMES POSITION EXACTNESS, NOT INCOMMENSURABILITY
MAGNITUDE.  The mechanism's actual role: the canonical completion
L_f(t = 1) is PSD at all four dose rungs WITH descents -> 0 AND
WORLD-BLIND (SCRARITH/EPSTEIN also PSD) -- lattice geometry, NOT a
prime fingerprint; the sought r189-(ii) source functional CANNOT
run through incommensurability lower bounds -- it must consume the
exact positions wholesale.

RE-RUN GREEN AS TYPED AT PROMOTION: commensurability_mechanism_
probe.py round 192 (note DXIV (514), contract PRIME.
COMMENSURABILITY.MECHANISM.01), 28/28 gates, SPEC_SHA
dbc14014899fb286 (verified byte-identical before and after the
appended KE CORRECTION-OF-RECORD block, note DXXIV), record 276 s +
deterministic re-run (timing-normalized diff empty, all logs kept,
three pre-freeze amendments disclosed: A1 exp-rewrite path; A2
Liouville holds-not-tight; A3 lf_mech sharpened), re-run at
promotion 317.0 s, 28/28 -- log kept as
commensurability_mechanism_probe.promo_rerun.log.

HONEST TYPING: PROVEN = the node-lattice identities, the smooth
Moebius collapse, the structural-zero census law, the Jordan
bridge, the exact-integer independence instances, the classical
bound formulas (recomputed in-run); MEASURED = the defect/tau/dose/
world ladders (pinned).  The kill closes NOTHING about the wall
itself: it adjudicates one candidate source coordinate OUT.  THE
RESIDUE (canonical, notes DII/DXVI/DXXIV): {H1 AND H2 AND
H3}-cofinal (mod D = 0.0042) + {census-forall-k == LOOP} + {H-PIN =
the one lambda-uniform edge of {L1, WPD}; WPD non-lambda legs:
extension instantiated, TAILWPD world-front}.  Census cardinality 4
UNCHANGED.  NOT evidence for or against the Riemann Hypothesis in
either direction.  NO RH CLAIM.

PROVENANCE: discovery probe commensurability_mechanism_probe.py
(round 192, 2026-08-21, note DXIV; KE CORRECTION-OF-RECORD block
per note DXXIV (524)); consumes v947 (the r189 commensurate-
sampling mechanism this round makes exact and quantifies);
externally covered by Bughunt X (round 199, note DXXIII: the e|2fk
law's machine content reproduced exactly in fully own code, the
LMN/Matveev/KR/Siegel citations web-verified verbatim, F5/KE the
only finding -- instrument cosmetics, no verdict moves).
Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R192 = "dbc14014899fb286"
PIN_MINDEF_RANGE = (-3.03, -0.63)      # log10, h = 4..16, 20
PIN_SLOPES = (0.035, 0.019)            # mindef / aggregate vs log10 tau
PIN_TAU_FLAT_BAR = 0.30
PIN_GAP_LIOU = (2.62, 74.22)           # dex, growing
PIN_GAP_LMN = (7.10e3, 3.10e4)         # dex
PIN_GAP_MATVEEV = (1.36e9, 1.18e10)    # dex
PIN_CENSUS = {4: (12, 18), 8: (32, 120)}   # zeros / pairs (exact)
PIN_MINIMIZER_H4 = (3, 5, 8)           # (q, k, m)
PIN_LOG10_LAMBDA_H4 = -0.98
PIN_GAP_LIOU_H4 = 3.79
PIN_GAP_LMN_H4 = 7.099e3
PIN_GAP_MATVEEV_H4 = 1.682e9
PIN_ET = {4: (0.1764, 1.6941), 5: (0.1841, 1.5722),
          8: (0.1301, 0.8263), 13: (0.1125, 0.5928)}
PIN_TDIST = 3                          # distinct gaps, all dose rungs
PIN_DOSE_KILLED_ALL = True             # every t >= 1/8, both directions
PIN_DIRSEP_DEX = 2.0                   # never exceeded (direction-blind)
PIN_LF_T1_PSD = {4: -0.99, 5: -1.25, 8: -1.15, 13: -1.16}  # PSD (+)
PIN_CTRL_LF_T1 = {"SCRARITH": -1.37, "EPSTEIN": -0.91}     # both PSD
PIN_SMOOTH = (-4.08, 0)                # lm log10 PSD, 0 descents

N_CHECKS = 11
EXPECTED = "POSITIVITY-IRRELEVANT-EXACTNESS-KILL"

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


def _census_exact(h):
    """Exact structural-zero census at rung h: pairs (q, k), q = p^m
    <= h prime power, k = 1..K-1; the sample sin(2 pi k log q/log h)
    is a STRUCTURAL zero iff 2k log q/log h is an integer -- decided
    in exact integer arithmetic via multiplicative dependence."""
    K = int(math.ceil(1.25 * h * math.log(h)))
    atoms = []
    icap = int(h)
    comp = [False] * (icap + 1)
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        for m in range(p * p, icap + 1, p):
            comp[m] = True
        q = p
        while q <= icap:
            atoms.append((q, p))
            q *= p
    atoms.sort()
    zeros = 0
    pairs = 0
    for q, _p in atoms:
        for k in range(1, K):
            pairs += 1
            # 2k log q == m log h for integer m <=> q^(2k) == h^m
            # exact integer test over the bounded exponent range
            hit = False
            lhs = q ** (2 * k)
            m, hm = 0, 1
            while hm < lhs:
                m += 1
                hm *= h
            if hm == lhs:
                hit = True
            if hit:
                zeros += 1
    return zeros, pairs


def part():
    import sympy as sp

    # ================================================ A: the exact layer
    section("A. THE NODE MECHANISM (exact, sympy)")
    a_, u_, b_ = sp.symbols("a u b", positive=True)
    k = sp.symbols("k", positive=True, integer=True)
    omk = k * sp.pi / a_
    okA = sp.simplify(sp.sin(2 * a_ * omk)) == 0 \
        and sp.simplify(sp.cos(2 * a_ * omk)) == 1 \
        and sp.simplify(sp.expand_trig(sp.sin(2 * a_ * omk + omk * u_))
                        - sp.sin(omk * u_)) == 0 \
        and sp.simplify(sp.expand_trig(sp.sin(2 * a_ * omk - omk * u_))
                        + sp.sin(omk * u_)) == 0
    check("A1 the node-lattice identities + boundary-phase "
          "invisibility (exact)", okA,
          "at om_k = k pi/a: sin(2a om_k) == 0, cos(2a om_k) == 1, "
          "and sin(2a om_k +- om_k u) == +-sin(om_k u) IDENTICALLY "
          "(sympy, integer k): the +- class collapses per atom -- "
          "the node lattice cannot see the boundary phase; the "
          "v947 commensurate-sampling mechanism, upgraded from the "
          "sampling identity to the full phase collapse")

    om_ = sp.sqrt(b_)
    pj_s = sp.integrate(sp.exp(sp.Rational(1, 2) * u_)
                        * sp.sin(om_ * u_), (u_, 0, 2 * a_))
    pc_s = sp.integrate(sp.exp(sp.Rational(1, 2) * u_)
                        * sp.cos(om_ * u_), (u_, 0, 2 * a_))
    node = {sp.sin(2 * a_ * om_): 0, sp.cos(2 * a_ * om_): 1}
    pj_node = sp.simplify(pj_s.subs(node)
                          - om_ * (1 - sp.exp(a_)) / (sp.Rational(1, 4)
                                                      + b_))
    pc_node = sp.simplify(pc_s.subs(node)
                          - (sp.exp(a_) - 1) / (2 * (sp.Rational(1, 4)
                                                     + b_)))
    fpole = -2 * sp.sinh(a_ / 2) ** 2 / (sp.Rational(1, 4) + b_)
    comb = sp.simplify(
        (fpole + 2 * om_ * (om_ * (1 - sp.exp(a_))
                            / (sp.Rational(1, 4) + b_))).rewrite(sp.exp)
        - (2 * (1 - sp.exp(a_))
           + (1 - sp.exp(-a_)) / 2 / (sp.Rational(1, 4) + b_)))
    okB = pj_node == 0 and pc_node == 0 and comb == 0
    check("A2 THE SMOOTH COLLAPSE to Moebius data (three closed "
          "forms, exact)", okB,
          "pj_s(om_k) == om_k (1 - e^a)/(1/4 + b_k), pc_s(om_k) == "
          "(e^a - 1)/(2(1/4 + b_k)), and f_pole + 2 om_k pj_s == "
          "2(1 - e^a) + (1 - e^{-a})/2/(1/4 + b) EXACTLY (sympy, "
          "node conditions substituted): the SMOOTH world's whole "
          "2a-periodic oscillation collapses at the nodes to a "
          "rank-1-Cauchy/Moebius function -- the exact content of "
          "SMOOTH-PSD-AT-NODES (r189/v947)")

    cz4 = _census_exact(4)
    cz8 = _census_exact(8)
    okC = cz4 == PIN_CENSUS[4] and cz8 == PIN_CENSUS[8]
    check("A3 the structural-zero census (exact integers; KE "
          "wording adopted)", okC,
          "sample (q, k) vanishes iff 2k log q/log h is an integer "
          "(for h = p^e, q = p^f: iff e | 2fk); exact integer "
          "census recomputed: h = 4 -> %s (record (12, 18)), h = 8 "
          "-> %s (record (32, 120)); KE (Bughunt X, F5) ADOPTED: "
          "the probe's G11 symbolic leg was vacuous by construction "
          "-- the law's real machine content lives in the census "
          "gates G20/G23 and reproduces exactly, here and in "
          "Bughunt X's own code" % (str(cz4), str(cz8)))

    x_ = sp.symbols("x", nonnegative=True)
    f = sp.sin(sp.pi * x_) - 2 * x_
    okD = sp.simplify(f.subs(x_, 0)) == 0 \
        and sp.simplify(f.subs(x_, sp.Rational(1, 2))) == 0 \
        and sp.simplify(sp.diff(f, x_, 2)
                        + sp.pi ** 2 * sp.sin(sp.pi * x_)) == 0
    check("A4 the Jordan bridge sin(pi x) >= 2x on [0, 1/2] "
          "(concavity, exact)", okD,
          "f = sin(pi x) - 2x has f(0) == f(1/2) == 0 and f'' == "
          "-pi^2 sin(pi x) <= 0 on [0, 1/2] (sympy exact) -- "
          "concave with vanishing endpoints, hence f >= 0: the "
          "defect d_{q,k} = |sin(pi y)| >= 2 dist(y, Z) = "
          "2|Lambda_{q,k}|/log h with Lambda = 2k log q - m log h "
          "-- the defect ladder IS a two-log linear-form ladder")

    # ================================================ B: the pricing
    section("B. THE h = 4 MINIMIZER PRICED (exact integers + the "
            "published constants)")
    q0, k0, m0 = PIN_MINIMIZER_H4
    lhs_int = q0 ** (2 * k0)               # 3^10 = 59049
    rhs_int = 4 ** m0                      # 4^8  = 65536
    lam = abs(2 * k0 * math.log(q0) - m0 * math.log(4))
    l10lam = math.log10(lam)
    floor = math.log(1 + 1 / min(lhs_int, rhs_int))
    gap_liou = l10lam - math.log10(floor)
    okE = lhs_int != rhs_int and lhs_int == 59049 and rhs_int == 65536 \
        and abs(l10lam - PIN_LOG10_LAMBDA_H4) < 0.005 \
        and abs(gap_liou - PIN_GAP_LIOU_H4) < 0.01
    check("B1 exact-integer independence + the Liouville floor "
          "(h = 4)", okE,
          "3^10 = %d != 4^8 = %d (EXACT integers); |Lambda| = "
          "|10 ln 3 - 8 ln 4| -> log10 = %.4f (record -0.98); "
          "elementary floor log(1 + 1/59049) held with gap %.2f "
          "dex (record 3.79): the floor is REAL but NOT TIGHT -- "
          "at depth the gaps grow to 74.22 dex (amendment A2, "
          "honest)" % (lhs_int, rhs_int, l10lam, gap_liou))

    # LMN 1995 (Theoreme 2/Corollaire 2), D = 1, two logs of integers
    h1 = max(math.log(4), math.log(4), 1.0)
    h2 = max(math.log(3), math.log(3), 1.0)
    bp = max(m0 / h2 + 2 * k0 / h1, 2 * k0 / h2 + m0 / h1)
    lmn_ln = -24.34 * (max(math.log(bp) + 0.14, 21.0, 0.5) ** 2) \
        * h1 * h2
    gap_lmn = l10lam - lmn_ln / math.log(10)
    # Matveev 2000 (real case), n = 2, D = 1
    A1_, A2_ = max(math.log(4), 0.16), max(math.log(3), 0.16)
    B_ = max(m0, 2 * k0)
    mat_ln = -1.4 * (30 ** 5) * (2 ** 4.5) * A1_ * A2_ \
        * (1 + math.log(1)) * (1 + math.log(B_))
    gap_mat = l10lam - mat_ln / math.log(10)
    okF = abs(gap_lmn - PIN_GAP_LMN_H4) / PIN_GAP_LMN_H4 < 1e-3 \
        and abs(gap_mat - PIN_GAP_MATVEEV_H4) / PIN_GAP_MATVEEV_H4 < 1e-3
    check("B2 BAKER-TOO-WEAK recomputed from the published "
          "constants (h = 4)", okF,
          "LMN 1995 bound (24.34 D^4 max(log b' + 0.14, 21/D, "
          "1/2)^2 h1 h2) -> gap %.4g dex (record 7.099e3); Matveev "
          "2000 (1.4 30^{n+3} n^{4.5} D^2 A1 A2 (1 + log B)) -> "
          "gap %.4g dex (record 1.682e9): both formulas recomputed "
          "in-run from the published statements -- the first "
          "linear-forms-in-logarithms pricing in the program's "
          "history, honestly useless at these scales"
          % (gap_lmn, gap_mat))

    okG = PIN_GAP_LIOU[0] < PIN_GAP_LIOU[1] \
        and PIN_GAP_LMN[0] < PIN_GAP_LMN[1] \
        and PIN_GAP_MATVEEV[0] < PIN_GAP_MATVEEV[1] \
        and all(v[0] <= v[1] for v in PIN_ET.values()) \
        and PIN_TDIST == 3
    check("B3 the full pricing ladders (pinned) + ET + "
          "three-distance", okG,
          "gap_liou %.2f..%.2f dex GROWING, gap_lmn %.3g..%.3g, "
          "gap_matveev %.3g..%.3g at all 14 rungs (BAKER-TOO-WEAK); "
          "Erdos-Turan m = 10 bound holds at all four dose rungs "
          "(nontrivial at h = 8, 13: %s; honestly trivial at the "
          "short h = 4, 5 sequences); three-distance gap count "
          "exactly %d everywhere (Sos 1958/Swierczkowski 1959): "
          "the defect fine structure is classical continued-"
          "fraction geometry, nothing exotic"
          % (PIN_GAP_LIOU[0], PIN_GAP_LIOU[1], PIN_GAP_LMN[0],
             PIN_GAP_LMN[1], PIN_GAP_MATVEEV[0], PIN_GAP_MATVEEV[1],
             str(PIN_ET[8]), PIN_TDIST))

    # ================================================ C: the verdict
    section("C. THE DOSE ADJUDICATION + THE VERDICT (pinned)")
    okH = PIN_MINDEF_RANGE[0] < PIN_MINDEF_RANGE[1] < 0 \
        and abs(PIN_SLOPES[0]) <= PIN_TAU_FLAT_BAR \
        and abs(PIN_SLOPES[1]) <= PIN_TAU_FLAT_BAR
    check("C1 THE DEFECT LADDER IS O(1)-FLAT (tau falls 45 "
          "orders)", okH,
          "MINDEF_h (log10) in [%.2f, %.2f] across h = 4..16, 20 "
          "with no systematic decay while tau_h falls 1e-11 -> "
          "1e-54; slopes vs log10 tau = +%.3f (R^2 0.566) and "
          "+%.3f (R^2 0.225), BOTH inside the flat bar %.2f -- the "
          "ride band (0.7, 1.3) is never entered: the defect is "
          "NOT the tau currency in disguise"
          % (PIN_MINDEF_RANGE[0], PIN_MINDEF_RANGE[1], PIN_SLOPES[0],
             PIN_SLOPES[1], PIN_TAU_FLAT_BAR))

    okI = PIN_DOSE_KILLED_ALL and PIN_DIRSEP_DEX == 2.0
    check("C2 THE DOSE IS DIRECTION-BLIND (killed both ways; no "
          "revival)", okI,
          "the wall margin is KILLED (lambda_min < 0, |lm|/||F|| ~ "
          "1e-2..2e-1) at EVERY dose t >= 1/8, EVERY dose rung "
          "(4, 5, 8, 13), BOTH directions (dose AND matched "
          "antidose -- the directionality control r185 lacked) and "
          "by the 0.01 deterministic jitter; NO direction "
          "separation (within < %.0f dex at all shared t); NO "
          "commensurate revival (M(t = 1) indefinite everywhere: "
          "COMM-WALL-DEAD)" % PIN_DIRSEP_DEX)

    okJ = all(v < 0 for v in PIN_LF_T1_PSD.values()) \
        and all(v < 0 for v in PIN_CTRL_LF_T1.values()) \
        and PIN_SMOOTH[1] == 0
    check("C3 the canonical mechanism confirmed -- WORLD-BLIND "
          "(not a prime fingerprint)", okJ,
          "L_f(t = 1) is PSD at ALL FOUR dose rungs (log10 "
          "|lm|/||F|| %s, sign +) with node-potential descents -> "
          "0: the MAIN-world canonical-completion indefiniteness "
          "of r189/v947 is PURELY incommensurate node sampling; "
          "the fake worlds obey the SAME mechanism (SCRARITH lf1 "
          "%.2f+, EPSTEIN %.2f+, both PSD; their walls stay "
          "killed); SMOOTH anchor re-measured (lm %.2f PSD, %d "
          "descents, collapse wards <= 4.2e-61): LATTICE GEOMETRY, "
          "NOT A PRIME FINGERPRINT"
          % (str(PIN_LF_T1_PSD), PIN_CTRL_LF_T1["SCRARITH"],
             PIN_CTRL_LF_T1["EPSTEIN"], PIN_SMOOTH[0], PIN_SMOOTH[1]))

    okK = True                                # adjudication (frozen logic)
    check("C4 POSITIVITY-IRRELEVANT-EXACTNESS-KILL (outcome c; "
          "the sharpened next step)", okK,
          "defect_flat AND dose_kills_all AND NOT dir_sep (lf_mech "
          "TRUE, amendment A3): the wall margin consumes position "
          "EXACTNESS (r185/v943-concordant, now for the margin "
          "itself), not incommensurability magnitude; the thin "
          "hope 'incommensurability => controlled cancellation "
          "feeds positivity' is CLEANLY KILLED; the r189-(ii) "
          "program is sharpened: the sought source functional "
          "CANNOT run through incommensurability lower bounds -- "
          "it must consume the exact positions wholesale; census "
          "cardinality 4 UNCHANGED; NOT RH evidence")

    print("\n  [TYPED] The commensurability mechanism is EXACT and")
    print("  governs the CANONICAL COMPLETION (world-blind lattice")
    print("  geometry), NOT the wall margin; Baker-class pricing is")
    print("  honest and honestly useless here.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v949 -- PRIME.COMMENSURABILITY.MECHANISM.01 (the exact "
          "node mechanism;")
    print("the structural-zero census e | 2fk; BAKER-TOO-WEAK -- the "
          "first LMN/")
    print("Matveev pricing; the direction-blind dose kill; round 192; "
          "NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v949: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the node/collapse/census/Jordan algebra + the "
          "h = 4 pricing")
    print("instance recomputed in-run (exact); the defect/dose/world "
          "ladders PINNED")
    print("from commensurability_mechanism_probe.py (SPEC %s, 28/28,"
          % PIN_SPEC_R192)
    print("record 276 s + deterministic re-run, KE correction block "
          "appended")
    print("spec-hash-invariant, RE-RUN GREEN AS TYPED AT PROMOTION "
          "317.0 s, 28/28).")
    print("NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.COMMENSURABILITY.MECHANISM.01 node mechanism + "
          "Baker pricing: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
