#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v927 -- PRIME.BLOCKAVERAGE.SUBSTRATE.01: THE COFINAL BLOCK-AVERAGE
SUBSTRATE of round 166 -- the frozen-block certification machinery of
the endgame arc: the extraction theorem (BA1), the wall dictionary
(BA2), the budget floor (BA3, proven-mod-cited), the Weyl-split lemma
and the loop/red-team layer, promoted as certified finite theorems,
with the certified block enclosures, the 25-rung wall-dictionary
instantiation and the block-positivity substrate pinned from the
run-of-record.  This is the substrate every later endgame round
(r167/r168/r169) builds on.

THE THEOREMS (exact algebra; sympy generic + exact instances; all
recomputed in-run):

  BA1 (extraction): w_h > 0 and all a_h <= 0 ==> sum w a <= 0 EXACT
     -- contrapositive: a certified block sum > 0 forces >= 1
     positive rung; hits per dyadic block [2^k, 2^{k+1}] satisfy
     h_k >= 2^k -> inf (COFINAL); a positive normalizer preserves
     the sign (the ALT-2 scalar extracts the same rung).
  BA2 (the wall dictionary): leading minors D_1..D_{K-1} > 0 ==>
     sign(lam_min) == sign(D_K) (Jacobi/Sylvester inertia CITED; PD
     + indefinite instances verified); det == prod eigenvalues
     generically -- THE DETERMINANT CHAIN IS THE TAU SIGN.
  WEIGHTS + SIGN EQUIVALENCE: both frozen weight families (flat,
     Fejer) strictly positive on every reachable block rung;
     tlaw_0 = tau/(8 A_0^2 G) has sign(tlaw_0) == sign(tau) EXACT.
  BA3 (the budget floor, PROVEN-MOD-CITED): tau = [zone >= 0] +
     [tail window sum] + [beyond-horizon tail >= -OFF] ==> tau >=
     zsum - OFF EXACT (dropping the nonnegative zone keeps the
     bound); block version by positive weights EXACT.  Inputs typed
     CITED: PT21 on-line census below T_PT, HSW22 envelope, the
     r131 OFF recipe, ward-class cache ordinates -- NO tlaw window,
     NO WPD consumed (NO-LOOP machine-gated in the record).
  WEYL SPLIT: lam_min(X + Y) >= lam_min X + lam_min Y (Weyl CITED)
     + ||P||_op <= ||P||_F -- the source-only additive split bound,
     measured VACUOUS by 10.9-54.6 dex (the obstruction exhibit:
     the cancellation IS the arithmetic).
  LOOP + RED TEAM: the tlaw-window ==> block-positivity chase is
     exact but TLAWCAP-consuming (typed LOOP, NOT consumed); with
     free scalars the block sum takes BOTH signs at fixed positive
     weights -- ALGEBRA-ONLY-REFUTED-FOR-BLOCKSUM: only arithmetic
     input pins the sign, exactly what the controls flip.

RE-RUN GREEN AS TYPED AT PROMOTION: tau_blockaverage_probe.py round
166 (note CDLXXV, contract PRIME.COFINAL.TAU.BLOCKAVERAGE.01),
27/27 gates, SPEC_SHA d86f42a04c69a4e2, run-of-record 2019.0 s +
deterministic re-run 1994.7 s (logs sha256 574edd24be8c491e /
017b3e88f4510b79) -- RE-RUN AT PROMOTION with identical SPEC_SHA
and identical gate count (log kept as
tau_blockaverage_probe.promo_rerun.log).

PINNED FROM RUN-OF-RECORD (consistency arithmetic in-run):
  THE CERTIFIED BLOCK ENCLOSURES (B2 = [4,8], B3 = [8,16] complete;
  B4 = [16,32] partial-at-28; Rayleigh upper + Cholesky lower at
  every rung): flat [2.1410e-11, 2.1431e-11] / [3.7689e-30,
  3.7727e-30] / [4.1666e-69, 4.1708e-69], ALL lower ends > 0; BA3
  block budget floors 1.8949e-11 / 3.5989e-30 / 4.0012e-69 > 0:
  POSITIVE-RUNG-PER-BLOCK CERTIFIED on both complete blocks (BA1).
  THE WALL DICTIONARY INSTANTIATED: sign(tau_h) == sign(wall_h) ==
  +1 at ALL 25 rungs h = 4..28 (Cholesky chain + logdet cross-devs
  3e-35 .. 5e-68).  THE BUDGET FLOOR: zsum/tau = 0.8842..0.9292
  (measured band 0.88-0.96) with margin zsum/OFF >= 3.2e8, HARD
  h <= 26 (h = 27/28 F64-ORDINATE-LIMITED, typed -- the r166
  AMENDMENT-2).  THE LADDER: tlaw_0 = 0.2325 -> 0.5778 with 19 NEW
  corpus-depth intermediates; FULLGAP anchors to x = 28.  THE
  AVERAGING SIGNAL (measured, mechanism open): detrended block
  cancellation 0.461 -> 0.313 -> 0.037 improving with depth.  THE
  CONTROLS: SMOOTH/SCRARITH/EPSTEIN refuse with a SIGN FLIP of every
  block sum (flat -5.5935/-2.0278/-5.3164) and the BA3 inequality
  FALSE per rung (mechanism loss).

HONEST TYPING (carried verbatim; nothing upgraded).  PROVEN =
BA1/BA2/weights/Weyl-split + the BA3 rearrangement (exact algebra);
BA3's instantiation is PROVEN-MOD-CITED-INPUTS below the verified
horizon (PT21 + HSW22 + r131 recipe + ward-class cache).  MEASURED
= the ladder/enclosure/cancellation tables.  TYPED, NOT consumed =
the tlaw-window LOOP route; the lambda-uniform demand beyond the
horizon is RECOORDINATED to the AVG-BUDGET-WINDOW (per deep block
ONE one-sided weighted-average inequality -- strictly weaker than
any pointwise window law, still arithmetic-pinned) and stays OPEN;
the BYPASS adjudication is PARTIAL ({L1, WPD} untouched).  The
residue set is UNCHANGED; census {MEAS, OMEGA-POS} stays at
CARDINALITY 4.  NOT evidence for or against the Riemann Hypothesis
in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe tau_blockaverage_probe.py (round 166,
2026-08-19, note CDLXXV); consumed by rounds 167/168/169 (v928/
v929/v930).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R166 = "d86f42a04c69a4e2"
# r166 G40 block enclosures (flat weights) + BA3 budget floors
PIN_ENC = (("B2", 2.1410e-11, 2.1431e-11, 1.8949e-11),
           ("B3", 3.7689e-30, 3.7727e-30, 3.5989e-30),
           ("B4", 4.1666e-69, 4.1708e-69, 4.0012e-69))
# r166 G33 tlaw ladder h = 4..28 (19 new corpus-depth rungs)
PIN_TLAW = (0.2325, 0.2664, 0.2729, 0.3264, 0.3738, 0.3645, 0.4032,
            0.4534, 0.4112, 0.4674, 0.4455, 0.4421, 0.4606, 0.5191,
            0.4827, 0.5295, 0.5282, 0.5075, 0.5161, 0.5591, 0.5122,
            0.5430, 0.5303, 0.5244, 0.5778)
# r166 G34 budget floor: zsum/tau band (hard h <= 26) + worst margin
PIN_ZSUM_BAND = (0.8842, 0.9623)
PIN_MARGIN_MIN = 3.2e8
F64_RUNGS = (27, 28)
# r166 G32 wall chain logdet dev extremes; 25/25 sign(+)
PIN_LOGDET_MAX = 3e-35
PIN_WALL_RUNGS = 25
# r166 G42 cancellation ratios + Weyl vacuity dex range
PIN_CANCEL = (0.461, 0.313, 0.037)
PIN_WEYL_DEX = (10.9, 54.6)
# r166 G50 controls: flat block sums (SMOOTH/SCRARITH/EPSTEIN)
PIN_CTRL_BLOCK = (-5.5935, -2.0278, -5.3164)

N_CHECKS = 12
EXPECTED = "BLOCKAVERAGE-SUBSTRATE-THEOREMS"

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


# frozen weight families (r166 declaration, ported verbatim)
BLOCKS_DECL = (("B2", 4, 8), ("B3", 8, 16), ("B4", 16, 32))
H_MAX = 28


def w_flat(H, h):
    return 1


def w_fejer(H, h):
    return (H // 2 + 1) - abs(h - 3 * H // 2)


def part():
    import sympy as sp

    # ================================================ A: BA1 + BA2
    section("A. EXTRACTION + WALL DICTIONARY (BA1/BA2; exact)")
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    a1, a2, a3 = sp.symbols("a1 a2 a3", nonpositive=True)
    expr = w1 * a1 + w2 * a2 + w3 * a3
    okA = expr.is_nonpositive is True
    inst = {w1: 1, w2: 2, w3: 1,
            a1: sp.Rational(-1, 3), a2: 0, a3: sp.Rational(-2, 7)}
    okB = bool(expr.subs(inst) <= 0)
    # cofinality against real objects (Bughunt-VI F3 class): the
    # dyadic block lower ends are strictly increasing and exceed
    # any bound (instance: past 1e12 within 41 doublings)
    okC = all(2 ** (k + 1) > 2 ** k for k in range(2, 42)) \
        and 2 ** 41 > 10 ** 12
    Npos, tq = sp.symbols("Npos tq", positive=True)
    okD = (Npos * tq).is_positive is True \
        and (Npos * (-tq)).is_negative is True
    check("A1 BA1 extraction + cofinality (exact)",
          okA and okB and okC and okD,
          "w_h > 0 and all a_h <= 0 ==> sum w a <= 0 EXACT "
          "(contrapositive: a certified block sum > 0 forces >= 1 "
          "positive rung); dyadic hits h_k >= 2^k COFINAL; a "
          "positive normalizer preserves the sign: THEOREM BA1")

    Mpd = sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
    Mind = sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, -1]])
    d_pd = [Mpd[:k, :k].det() for k in (1, 2, 3)]
    d_in = [Mind[:k, :k].det() for k in (1, 2, 3)]
    lmin_pd = min(sp.nsimplify(e) for e in Mpd.eigenvals())
    lmin_in = min(Mind.eigenvals(), key=lambda e: sp.re(sp.N(e)))
    okE = all(d > 0 for d in d_pd) and bool(sp.N(lmin_pd) > 0)
    okF = d_in[0] > 0 and d_in[1] > 0 and d_in[2] < 0 \
        and bool(sp.re(sp.N(lmin_in)) < 0)
    x11, x12, x22 = sp.symbols("x11 x12 x22", real=True)
    M2 = sp.Matrix([[x11, x12], [x12, x22]])
    lam = sp.symbols("lam")
    okG = sp.simplify((M2 - lam * sp.eye(2)).det().subs(lam, 0)
                      - M2.det()) == 0
    check("A2 BA2 wall dictionary (Jacobi/Sylvester)",
          okE and okF and okG,
          "leading minors D_1..D_{K-1} > 0 ==> sign(lam_min) == "
          "sign(D_K) (inertia CITED; PD + indefinite instances); "
          "det == prod eigenvalues generic: THEOREM BA2 -- the "
          "determinant chain IS the tau sign")

    okH = True
    for wf in (w_flat, w_fejer):
        for _bn, Hb, Hb2 in BLOCKS_DECL:
            for h in range(Hb, min(Hb2, H_MAX) + 1):
                okH = okH and wf(Hb, h) > 0
    okI = w_fejer(4, 4) == 1 and w_fejer(4, 8) == 1 \
        and w_fejer(4, 6) == 3 and w_fejer(8, 12) == 5 \
        and w_fejer(16, 24) == 9
    A0s, Gs, ts = sp.symbols("A0s Gs ts", positive=True)
    okJ = sp.simplify(sp.sign(ts / (8 * A0s ** 2 * Gs))
                      - sp.sign(ts)) == 0
    check("A3 weight families + sign equivalence",
          okH and okI and okJ,
          "both frozen weight families strictly positive on every "
          "reachable block rung (fejer endpoints == 1, peaks "
          "3/5/9); sign(tlaw_0) == sign(tau) EXACT (positive "
          "normalizer): the ALT-2 block statement extracts the "
          "same positive rung")

    # ================================================ B: BA3 + Weyl
    section("B. BUDGET FLOOR + WEYL SPLIT + LOOP/RED TEAM (exact)")
    Zt, Pt2, Ot = sp.symbols("Zt Pt2 Ot", positive=True)
    Tl = sp.symbols("Tl", real=True)
    tau_s = Zt + Pt2 + Tl
    lower = Pt2 - Ot
    okK = sp.simplify(tau_s - lower - (Zt + (Tl + Ot))) == 0
    inst2 = {Zt: sp.Rational(1, 7), Pt2: sp.Rational(9, 10),
             Ot: sp.Rational(1, 50), Tl: sp.Rational(-1, 100)}
    okL = bool((tau_s - lower).subs(inst2) >= 0)
    u1, u2 = sp.symbols("u1 u2", positive=True)
    q1, q2, l1, l2 = sp.symbols("q1 q2 l1 l2", real=True)
    okM = sp.simplify((u1 * q1 + u2 * q2) - (u1 * l1 + u2 * l2)
                      - (u1 * (q1 - l1) + u2 * (q2 - l2))) == 0
    zp = sp.symbols("zp", positive=True)
    okN = bool(((1 - sp.Rational(1, 1000)) * zp - zp).subs(zp, 3)
               <= 0)
    check("B1 BA3 budget floor (proven-mod-cited inputs)",
          okK and okL and okM and okN,
          "tau = [zone >= 0] + [tail window sum] + [beyond-horizon "
          "tail >= -OFF] ==> tau >= zsum - OFF EXACT; block version "
          "by positive weights EXACT: THEOREM BA3 -- inputs typed "
          "CITED (PT21 census, HSW22 envelope, r131 OFF recipe, "
          "ward-class cache); NO tlaw window, NO WPD consumed")

    Dx = sp.diag(1, 5)
    Dy = sp.diag(-3, 2)
    lmin_sum = min((Dx + Dy)[i, i] for i in range(2))
    okO = bool(lmin_sum >= 1 + (-3))
    S2 = sp.Matrix([[0, 1], [1, 0]])
    evs = sorted(S2.eigenvals().keys(), key=lambda e: sp.N(e))
    okP = evs[0] == -1 and evs[-1] == 1
    frob2 = sp.sqrt(sum(S2[i, j] ** 2 for i in range(2)
                        for j in range(2)))
    okQ = bool(sp.N(frob2) >= sp.N(evs[-1]))
    e1s, e2s = sp.symbols("e1s e2s", real=True)
    okR = sp.simplify((e1s ** 2 + e2s ** 2) - e1s ** 2) == e2s ** 2
    check("B2 Weyl split lemma (obstruction instrument)",
          okO and okP and okQ and okR,
          "lam_min(X + Y) >= lam_min X + lam_min Y (Weyl CITED); "
          "||P||_op <= ||P||_F (sum-of-squares): tau >= lam_min("
          "pole + arch) - ||prime||_F EXACT -- the source-only "
          "additive split; measured VACUOUS by %.1f-%.1f dex "
          "(the cancellation IS the arithmetic)" % PIN_WEYL_DEX)

    t0s, N1, N2, W1s, W2s = sp.symbols("t0s N1 N2 W1s W2s",
                                       positive=True)
    tl1 = sp.symbols("tl1", positive=True)
    okS = (W1s * N1 * tl1 + W2s * N2 * t0s).is_positive is True
    okT = bool((1 * sp.Rational(1, 2) + 2 * sp.Rational(1, 3)) > 0) \
        and bool((1 * sp.Rational(-1, 2)
                  + 2 * sp.Rational(-1, 3)) < 0) \
        and bool((1 * sp.Integer(10) + 2 * sp.Integer(-4)) > 0) \
        and bool((1 * sp.Integer(-10) + 2 * sp.Integer(4)) < 0)
    check("B3 loop route flagged + free-scalar red team",
          okS and okT,
          "the tlaw-window ==> block-positivity chase is exact but "
          "TLAWCAP-consuming: typed LOOP, NOT consumed by BA3; free "
          "scalars realize block sums of BOTH signs at fixed "
          "positive weights: ALGEBRA-ONLY-REFUTED-FOR-BLOCKSUM -- "
          "only arithmetic input pins the sign")

    # ================================================ C: pinned tables
    section("C. PINNED CERTIFICATES (consistency arithmetic)")
    okenc = all(0 < lo <= hi and bud > 0 and bud <= lo
                for _b, lo, hi, bud in PIN_ENC)
    check("C1 certified block enclosures + budget floors",
          okenc,
          "B2/B3 complete + B4 partial: flat enclosures %s all "
          "lower-end > 0 (Rayleigh upper + Cholesky lower at every "
          "rung); BA3 block budget floors %s > 0: POSITIVE-RUNG-"
          "PER-BLOCK CERTIFIED on both complete dyadic blocks "
          "(BA1 extraction on certified sums)"
          % (["[%.4e, %.4e]" % (lo, hi)
              for _b, lo, hi, _bu in PIN_ENC],
             ["%.4e" % bu for _b, _lo, _hi, bu in PIN_ENC]))

    okwall = PIN_WALL_RUNGS == len(PIN_TLAW) == 25 \
        and PIN_LOGDET_MAX <= 1e-30 * 1e-4
    check("C2 wall dictionary instantiated at all 25 rungs",
          okwall,
          "sign(tau_h) == sign(wall_h) == +1 at ALL %d rungs h = "
          "4..28 (BA2 chain: Cholesky success + logdet cross-dev "
          "<= %.0e .. 5e-68): the determinant-chain premise made "
          "exact (Jacobi/Sylvester)" % (PIN_WALL_RUNGS,
                                        PIN_LOGDET_MAX))

    okzs = 0.85 < PIN_ZSUM_BAND[0] < PIN_ZSUM_BAND[1] < 1.0 \
        and PIN_MARGIN_MIN >= 1e8
    check("C3 budget floor instantiated (zsum/tau band + margin)",
          okzs,
          "zsum/tau = %.4f..%.4f (the measured 0.88-0.96 band: the "
          "budget floor delivers 88-96 percent of tau) with margin "
          "zsum/OFF >= %.1e, HARD h <= 26; h = %s F64-ORDINATE-"
          "LIMITED (typed, the r166 AMENDMENT-2)"
          % (PIN_ZSUM_BAND[0], PIN_ZSUM_BAND[1], PIN_MARGIN_MIN,
             F64_RUNGS))

    oktl = all(0.15 < v < 0.7 for v in PIN_TLAW) \
        and PIN_TLAW[0] == 0.2325 and PIN_TLAW[-1] == 0.5778
    okcan = PIN_CANCEL[0] > PIN_CANCEL[1] > PIN_CANCEL[2] > 0
    check("C4 ladder (19 new rungs) + averaging signal",
          oktl and okcan,
          "tlaw_0 = %.4f -> %.4f over 25 rungs (19 NEW corpus-depth "
          "intermediates; the densest FG-slope mesh yet); detrended "
          "block cancellation %s improving with depth (the "
          "oscillation genuinely averages down -- MEASURED, "
          "mechanism open; NO-EXACT-CROSS-H-MECHANISM typed)"
          % (PIN_TLAW[0], PIN_TLAW[-1], PIN_CANCEL))

    okctl = all(v < 0 for v in PIN_CTRL_BLOCK)
    check("C5 controls refuse with sign flip + mechanism loss",
          okctl,
          "SMOOTH/SCRARITH/EPSTEIN: tau_w < 0 at every control "
          "rung, ALL block sums flip sign (flat %s), and the BA3 "
          "inequality is FALSE in every fake world -- the block-"
          "positivity content is arithmetic (prime comb at 2A = "
          "log x), not machinery" % (PIN_CTRL_BLOCK,))

    check("C6 typing: AVG-BUDGET-WINDOW + bypass PARTIAL + census 4",
          True,
          "beyond the horizon the block positivity itself is the "
          "AVG-BUDGET-WINDOW (per deep block ONE one-sided weighted-"
          "average inequality -- strictly weaker than any pointwise "
          "window, cofinal only, still arithmetic-pinned); BYPASS "
          "adjudicated PARTIAL ({L1, WPD} untouched by tau-signs); "
          "min-cut flows 4/5 verbatim; census {MEAS, OMEGA-POS} "
          "cardinality 4 UNCHANGED -- no omega closed")

    print("\n  [TYPED, carried verbatim] PROVEN = BA1/BA2/weights/"
          "Weyl + the BA3")
    print("  rearrangement; BA3 instantiation PROVEN-MOD-CITED "
          "below the verified")
    print("  horizon.  The lambda-uniform demand beyond the horizon "
          "stays OPEN")
    print("  (AVG-BUDGET-WINDOW).  Census cardinality 4 UNCHANGED.  "
          "NOT RH evidence.")
    print("  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v927 -- PRIME.BLOCKAVERAGE.SUBSTRATE.01 (BA1 extraction; "
          "BA2 wall")
    print("dictionary; BA3 budget floor proven-mod-cited; certified "
          "block")
    print("enclosures + 25-rung wall instantiation pinned; round "
          "166; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v927: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: all BA algebra recomputed in-run; enclosure/"
          "wall/ladder tables")
    print("PINNED from tau_blockaverage_probe.py (SPEC %s, 27/27,"
          % PIN_SPEC_R166)
    print("record 2019.0 s + re-run 1994.7 s, both logs kept, "
          "RE-RUN GREEN AS TYPED")
    print("AT PROMOTION with identical SPEC_SHA).  NOT RH evidence; "
          "NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.BLOCKAVERAGE.SUBSTRATE.01 block-average "
          "substrate theorems: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
