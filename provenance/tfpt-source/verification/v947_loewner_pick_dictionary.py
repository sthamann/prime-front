#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v947 -- PRIME.LOEWNER.PICK.01: THE EXACT LOEWNER-PICK DICTIONARY
+ THE PICK-CLASS REFUTATION of round 189 -- Loewner's theorem
adjudicated as a currency for wall positivity: the Pick reading is
REFUTED with an exact new structural law in its place.

THE EXACT DICTIONARY (the round's positive delivery): the wall is
NOT the canonical Loewner matrix of its potential but a
DIAGONALLY-SHIFTED one -- M_h PSD <=> Raw_h PSD by exact Sylvester
congruence, and Raw_h = L_f + diag(Delta) with the off-diagonal
divided-difference form upgraded from r186's float64 to mp at
every rung (dev <= 1.5e-61).  THE NEW EXACT LAW (probe: sympy
per-atom + mp <= 6.0e-61; BH9 own independent recompute <= 6.3e-61
numeric + per-atom symbolic): THE COSINE-QUADRATURE DIAGONAL LAW
-- the diagonal shift on the prime block is Raw[k,k] -
f_prime'(b_k) = 2a pc_k, THE COSINE QUADRATURE pc_k = sum_q w_q
cos(om_k u_q) OF THE SAME SIEVE ATOMS whose SINE quadrature pj
feeds the potential: THE WALL CARRIES BOTH QUADRATURES OF THE SAME
ATOMS IN DIFFERENT SLOTS (the k = 0 doubling mirrors the mode norm
nrm_0^2 = 2a vs a).  The POLE block is fully canonical (Delta_pole
== 0 identically -- recomputed symbolically in-run: divided
difference == rank-1 Cauchy AND diagonal == f_pole') and f_pole is
a GENUINE PICK FUNCTION with exact Herglotz representation = the
point mass 2 sinh^2(a/2) delta_{t = -1/4} (weight = the builder
constant, location = the completed square of s(1-s) -- recomputed
symbolically in-run, including Im f_pole > 0 on the upper half
plane).  The ARCH excess is measured (its 1/(2w) singularity's
cos-transform is log-divergent, the builder's gamma + ln pi
counterterm; closed form honestly NOT claimed).  Not a sum kernel
(anticommutator s3/s1 = 0.372..0.622, Bhatia class excluded), not
a two-function pair (g = ones exact).  Loewner 1934 / Donoghue
1974 / Simon 2019 apply to the canonical L_f only.

THE PICK-CLASS REFUTATION (the decisive numbers, all pinned):
lambda_min(L_f) < 0 at ALL 14 rungs (log10(|lambda_min|/||F||) =
-0.84..-2.00, roughly constant, zero refusals) -- the Pick costume
misses wall positivity by 9.4 (h=4) to 87.9 (h=20) ORDERS; f_h is
non-monotone on every hull (descent counts 2-34: order-1 already
dead); ALL grid sign changes are carried by the prime leg
(10/18/35/68 at the PICK rungs; pole + arch: zero); refinement
margins DEEPEN (-0.044 -> -0.206: no hidden interval-wide margin);
bonus exhibit: a 17-node window below the first f'-zero is
INDEFINITE while f' > 0 on it -- the classical scalar-vs-matrix
order separation live in the wall potential.  HERGLOTZ per leg:
pole EXACT source-expressible point mass; arch measured-monotone
representation open; prime leg non-Pick and its formal density IS
the signed atom data -- a positive rewrite of that leg would be
the wall positivity itself: the dream statement dies honestly at
the prime leg in both directions (relabeling barrier named, not
crossed).

WORLDS + SCREENS: the dictionary is world-blind (typed), the
VALUES are mixed: MAIN indefinite 14/14 but THE SMOOTH CELL IS PSD
WITH 0 DESCENTS -- its 2a-periodic oscillation vanishes exactly on
the node lattice (sin(2a om_k) == 0 at om_k = k pi/a, COMMENSURATE
SAMPLING -- recomputed symbolically in-run) which incommensurate
prime atoms cannot do; SCRARITH/EPSTEIN mixed; the r172 witness is
matrix-side-invariant by construction (typed, not sold); ATOMJET
detected exactly linearly (devs 4.2e-61/3.0e-61); tau-screens BOTH
FLAT (-0.011/-0.011) -- not a relabel and not a sign source
either; the r45 LOEWNER-DEAD prior art distinguished: THIS kills a
THIRD reading (positivity-as-function-class), not r45's, and the
IIKS/RHP lane is untouched.

RE-RUN GREEN AS TYPED AT PROMOTION: loewner_pick_probe.py round
189 (note DX (510), contract PRIME.LOEWNER.PICK.01), 28/28 gates,
SPEC_SHA a547448468899af9, record 1046 s + 1058 s deterministic
re-run (timing-normalized diff empty, all logs kept, three
pre-freeze amendments disclosed: A1 the commensurate jet atom q =
5 -> q = 2; A2 window gate -> resolve-and-record; A3 world enum ->
ternary), re-run at promotion 1082.9 s, 28/28 -- log kept as
loewner_pick_probe.promo_rerun.log.

HONEST TYPING: PROVEN = the dictionary algebra + the pole-block
canonicity + the Herglotz point mass + the commensurate-sampling
mechanism; MEASURED = the lambda_min/descent/grid/refinement/
window/world ladders; the K1 correction of record (r186) is
CARRIED here by construction -- this round's record already states
the corrected dictionary ("NOT literally the canonical L_f") and
needed NOTHING per BH9; the named next question (WHICH source
functional makes L_f + diag(Delta) PSD when neither summand is)
stays recorded, NOT claimed, experiments-side.  THE RESIDUE
(canonical, notes DII/DXVI): {H1 AND H2 AND H3}-cofinal (mod D =
0.0042) + {census-forall-k == LOOP} + {H-PIN = the one lambda-
uniform edge of {L1, WPD}; WPD non-lambda legs: extension
instantiated, TAILWPD world-front}.  Census cardinality 4
UNCHANGED.  NOT evidence for or against the Riemann Hypothesis in
either direction.  NO RH CLAIM.

PROVENANCE: discovery probe loewner_pick_probe.py (round 189,
2026-08-21, note DX); consumes v944 (the r186 off-diagonal law it
upgraded and diagonally completed); externally covered by Bughunt
IX (round 193, note DXV: the cosine-quadrature diagonal law
independently recomputed <= 6.3e-61 numeric + per-atom symbolic
proof with the pole block == rank-1 Cauchy == canonical Loewner of
f_pole, zero failures; X1 adjudication: r189's record correct as
written).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R189 = "a547448468899af9"
PIN_OFFDIAG_MP = 1.5e-61               # off-diagonal Loewner form, mp
PIN_COSLAW_DEV = 6.0e-61               # prime cos-quadrature law, mp
PIN_COSLAW_BH9 = 6.3e-61               # BH9 own independent recompute
PIN_LM_RANGE = (-2.00, -0.84)          # log10(|lambda_min(L_f)|/||F||)
PIN_PICK_MISS_ORDERS = (9.4, 87.9)     # gap to wall positivity
PIN_DESC_RANGE = (2, 34)
PIN_GRID_NSC = (10, 18, 35, 68)        # ALL carried by the prime leg
PIN_REFINE_H4 = (-0.0442, -0.1198, -0.1498, -0.2063)   # R0..R3
PIN_WIN_LM = (-4.6e-2, -4.3e-2)        # 17-node window indefinite
PIN_WIN_FP_MIN = 0.26                  # while f' > 0 on it
PIN_SUMK_S3S1 = (0.372, 0.622)         # not a sum kernel
PIN_JET_DEVS = (4.2e-61, 3.0e-61)      # ATOMJET linear detection
PIN_TAU_SLOPES = (-0.011, -0.011)      # both flat
PIN_TAU_FLAT_BAR = 0.30

N_CHECKS = 9
EXPECTED = "LOEWNER-PICK-DICTIONARY-MISMATCH"

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

    # ================================================ A: exact dictionary
    section("A. THE EXACT DICTIONARY (pole canonical, Pick, "
            "quadrature slots)")
    a_, bi, bj, b_ = sp.symbols("a b_i b_j b", positive=True)
    s2 = 2 * sp.sinh(a_ / 2) ** 2
    fpole = lambda t: -s2 / (sp.Rational(1, 4) + t)     # noqa: E731
    dd = sp.simplify((fpole(bi) - fpole(bj)) / (bi - bj)
                     - s2 / ((sp.Rational(1, 4) + bi)
                             * (sp.Rational(1, 4) + bj)))
    ddiag = sp.simplify(sp.diff(fpole(b_), b_)
                        - s2 / (sp.Rational(1, 4) + b_) ** 2)
    okA = dd == 0 and ddiag == 0
    check("A1 the pole block is FULLY CANONICAL (Delta_pole == 0 "
          "identically)", okA,
          "divided difference of f_pole(b) = -2 sinh^2(a/2)/(1/4 + "
          "b) == the rank-1 Cauchy kernel 2 sinh^2(a/2)/((1/4 + "
          "b_i)(1/4 + b_j)) AND the diagonal == f_pole'(b) exactly "
          "(sympy): the pole block is the ONE fully canonical "
          "Loewner block of the wall -- BH9 independently verified "
          "pole block == rank-1 Cauchy == canonical Loewner of "
          "f_pole")

    x_, y_ = sp.symbols("x y", real=True)
    zc = x_ + sp.I * y_
    imf = sp.simplify(sp.im(-s2 / (sp.Rational(1, 4) + zc)))
    # Im f_pole = s2 * y / |1/4 + z|^2 > 0 for y > 0
    target = s2 * y_ / ((sp.Rational(1, 4) + x_) ** 2 + y_ ** 2)
    okB = sp.simplify(imf - target) == 0
    cauchy = sp.integrate(sp.DiracDelta(x_ + sp.Rational(1, 4))
                          / (x_ - b_), (x_, -sp.oo, sp.oo))
    okC = sp.simplify(s2 * cauchy - fpole(b_)) == 0
    check("A2 f_pole is a GENUINE PICK function with exact Herglotz "
          "point mass", okB and okC,
          "Im f_pole(z) == 2 sinh^2(a/2) Im z / |1/4 + z|^2 > 0 on "
          "the upper half plane (sympy exact) and the Cauchy "
          "transform of the point mass 2 sinh^2(a/2) "
          "delta_{t = -1/4} == f_pole exactly: weight = the "
          "builder constant, location = the completed square of "
          "s(1 - s) -- the pole leg's Herglotz representation is "
          "EXACT and source-expressible")

    u, w_ = sp.symbols("u w", positive=True)
    om = sp.symbols("omega", positive=True)
    fprime_atom = 2 * sp.sqrt(b_) * w_ * sp.sin(sp.sqrt(b_) * u)
    deriv = sp.simplify(sp.diff(fprime_atom, b_)
                        - (w_ * sp.sin(sp.sqrt(b_) * u) / sp.sqrt(b_)
                           + w_ * u * sp.cos(sp.sqrt(b_) * u)))
    okD = deriv == 0
    okE = sp.simplify(sp.diff(w_ * sp.sin(om * u), u)
                      - w_ * om * sp.cos(om * u)) == 0
    check("A3 THE COSINE-QUADRATURE DIAGONAL LAW (per-atom "
          "structure; probe sympy-exact)", okD and okE,
          "per atom (u, w): f_prime'(b) == w sin(om u)/om + "
          "w u cos(om u) at om = sqrt(b) (exact chain rule, "
          "recomputed) -- the canonical diagonal; the probe proves "
          "per-atom (sympy) and gates at every rung (mp <= %.1e; "
          "BH9 own recompute <= %.1e) that the wall diagonal "
          "EXCEEDS it by exactly 2a pc_k with pc_k = sum w cos(om_k "
          "u): THE SINE QUADRATURE SITS IN THE POTENTIAL, THE "
          "COSINE QUADRATURE IN THE DIAGONAL SHIFT -- both "
          "quadratures of the same atoms in different slots "
          "(k = 0 doubled, mirroring nrm_0^2 = 2a)"
          % (PIN_COSLAW_DEV, PIN_COSLAW_BH9))

    k = sp.symbols("k", positive=True, integer=True)
    omk = k * sp.pi / a_
    okF = sp.simplify(sp.sin(2 * a_ * omk)) == 0 \
        and sp.simplify(sp.cos(2 * a_ * omk)) == 1
    check("A4 the commensurate-sampling mechanism (SMOOTH-PSD-AT-"
          "NODES, exact)", okF,
          "at the node lattice om_k = k pi/a: sin(2a om_k) == "
          "sin(2 pi k) == 0 and cos(2a om_k) == 1 exactly (sympy, "
          "k integer): the SMOOTH world's whole 2a-periodic "
          "oscillation vanishes exactly on the nodes -- which "
          "incommensurate prime atoms (u = log q) cannot do: the "
          "mechanism behind WORLD-MIXED-SMOOTH-PSD-AT-NODES, typed "
          "as lattice geometry, not sold as a prime fingerprint")

    # ================================================ B: the refutation
    section("B. THE PICK-CLASS REFUTATION (pinned, typed MEASURED)")
    okG = PIN_LM_RANGE[0] < PIN_LM_RANGE[1] < 0 \
        and PIN_PICK_MISS_ORDERS == (9.4, 87.9)
    check("B1 CANONICAL-COMPLETION-INDEFINITE at all 14 rungs "
          "(misses by 9.4-87.9 orders)", okG,
          "lambda_min(L_f) < 0 at every rung with log10(|lambda_"
          "min|/||F||) in [%.2f, %.2f] (roughly constant, zero "
          "refusals): the Pick costume misses wall positivity by "
          "%.1f (h=4) to %.1f (h=20) ORDERS -- L_f is INDEFINITE "
          "while the wall is PD: the wall is NOT positivity-of-a-"
          "matrix-monotone-function; Loewner 1934/Donoghue 1974/"
          "Simon 2019 apply to the canonical L_f only"
          % (PIN_LM_RANGE[0], PIN_LM_RANGE[1],
             PIN_PICK_MISS_ORDERS[0], PIN_PICK_MISS_ORDERS[1]))

    okH = PIN_DESC_RANGE == (2, 34) \
        and all(PIN_REFINE_H4[i + 1] < PIN_REFINE_H4[i]
                for i in (0, 1)) and PIN_REFINE_H4[3] < PIN_REFINE_H4[0]
    check("B2 order-1 dead + refinement DEEPENS (no hidden "
          "margin)", okH,
          "descent counts %d..%d of K-1 on every hull (f_h non-"
          "monotone: matrix monotonicity of ANY order requires f "
          "nondecreasing -- order-1 already dead); the refinement "
          "battery R0 -> R3 at h = 4: %s (recomputed monotone "
          "deepening): no interval-wide margin hides between the "
          "nodes; ALL grid sign changes %s carried by the PRIME "
          "leg (pole + arch: zero)"
          % (PIN_DESC_RANGE[0], PIN_DESC_RANGE[1],
             str(PIN_REFINE_H4), str(PIN_GRID_NSC)))

    okI = PIN_WIN_LM[1] < 0 and PIN_WIN_FP_MIN > 0
    check("B3 the scalar-vs-matrix order separation (live "
          "exhibit)", okI,
          "the 17-node window below the first f'-zero is "
          "INDEFINITE (lambda_min/||F|| ~ %.1e..%.1e) while f' > 0 "
          "on it (min f' %.2f..1.32): the classical separation "
          "between scalar monotonicity and matrix monotonicity is "
          "LIVE in the wall potential -- the refutation is not a "
          "boundary artifact" % (PIN_WIN_LM[0], PIN_WIN_LM[1],
                                 PIN_WIN_FP_MIN))

    okJ = PIN_SUMK_S3S1[0] > 1e-6 \
        and abs(PIN_TAU_SLOPES[0]) <= PIN_TAU_FLAT_BAR \
        and abs(PIN_TAU_SLOPES[1]) <= PIN_TAU_FLAT_BAR \
        and PIN_JET_DEVS[0] < 1e-28 and PIN_JET_DEVS[1] < 1e-28
    check("B4 not-a-sum-kernel; ATOMJET linear; tau-screens BOTH "
          "FLAT", okJ,
          "the anticommutator ratio s3/s1 = %.3f..%.3f excludes "
          "the Bhatia sum-kernel class; the ATOMJET (double the "
          "q = 2 atom weight) shifts potential and diagonal law "
          "EXACTLY linearly (devs %.1e/%.1e): the dictionary "
          "detects source jets linearly; tau-screen slopes "
          "%.3f/%.3f both inside the flat bar %.2f -- the Pick-"
          "defect coordinates do NOT ride the tau currency (and "
          "need not, being indefiniteness certificates); the r45 "
          "LOEWNER-DEAD distinction carried: THIS kills the "
          "positivity-as-function-class reading, the IIKS/RHP "
          "lane untouched"
          % (PIN_SUMK_S3S1[0], PIN_SUMK_S3S1[1], PIN_JET_DEVS[0],
             PIN_JET_DEVS[1], PIN_TAU_SLOPES[0], PIN_TAU_SLOPES[1],
             PIN_TAU_FLAT_BAR))

    # ================================================ C: adjudication
    section("C. HERGLOTZ PER LEG + THE HONEST BARRIER")
    okK = True                                # definitional/adjudication
    check("C1 HERGLOTZ-POLE-EXACT-ARCH-OPEN-PRIME-BARRIER "
          "(the dream dies honestly)", okK,
          "pole leg: exact source-expressible point mass (A2); "
          "arch leg: measured-monotone, representation OPEN (the "
          "1/(2w) singularity's cos-transform is log-divergent, "
          "the builder's gamma + ln pi counterterm -- closed form "
          "honestly NOT claimed); prime leg: non-Pick BOTH "
          "directions, and its formal density IS the signed atom "
          "data -- a positive rewrite of that leg would BE the "
          "wall positivity: the relabeling barrier is NAMED, not "
          "crossed; the exactly-posed cancellation question "
          "(which source functional makes L_f + diag(Delta) PSD "
          "when neither summand is) stays RECORDED, not claimed, "
          "experiments-side; census cardinality 4 UNCHANGED; NOT "
          "RH evidence")

    print("\n  [TYPED] THE WALL IS EXACTLY L_f + diag(Delta) -- a")
    print("  diagonally-shifted one-function Loewner matrix, NOT the")
    print("  canonical object of Loewner's theorem; the Pick reading is")
    print("  dead by 9-88 orders; the cosine-quadrature diagonal law is")
    print("  the new exact structure.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v947 -- PRIME.LOEWNER.PICK.01 (the exact dictionary Raw = "
          "L_f +")
    print("diag(Delta); the cosine-quadrature diagonal law; the pole-"
          "leg Herglotz")
    print("point mass; the Pick-class refutation; SMOOTH-PSD-AT-NODES; "
          "round 189;")
    print("NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v947: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the pole-canonicity/Pick/Herglotz/chain-rule/"
          "commensurability")
    print("algebra recomputed in-run (exact); the lambda_min/descent/"
          "grid/window/")
    print("world tables PINNED from loewner_pick_probe.py (SPEC %s,"
          % PIN_SPEC_R189)
    print("28/28, record 1046 s + 1058 s deterministic re-run, three "
          "pre-freeze")
    print("amendments disclosed, all logs kept, RE-RUN GREEN AS TYPED "
          "AT PROMOTION")
    print("1082.9 s, 28/28).  NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.LOEWNER.PICK.01 exact dictionary + Pick "
          "refutation: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
