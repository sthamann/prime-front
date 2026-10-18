#!/usr/bin/env python3
r"""logic_audit_report -- PRIME.AUDIT.LOGIC.03: ADVERSARIAL BUG HUNT #3,
the logic and convention layer (2026-08-13, note CCCXXXVII).

READ + REPORT audit of STATEMENTS, not numerics: notes CCLXV..CCCXXXI
(experiments/next.txt, head lines 1..33) diffed against their probes'
actual wards/censuses, the paper
articles/2026-08-11/paper_endform_and_inertia_bridge_en.md diffed
line-by-line against the notes, the sigma-chain conventions
(CCLXV/CCLXXVII/CCLXXIX/CCLXXXV/CCXCIII) cross-checked in the probe
sources, the extraction-chain premises read from
experiments/lean4-carrier-rigidity/TfptCarrier/CofinalWeil.lean and
tfpt_prime_front.tex, and the frozen gate rule ("only an independent
sign source counts") swept across the paper.  Every entry below was
earned by grepping the named artifact, not by trusting the note.

This module is the report of record.  Its __main__ re-checks the ten
most load-bearing NUMBER-claims as executable assertions (A1..A10,
fail-loud, stdlib only).  The assertions verify the actual computed
statements; the findings (what a text says vs what was computed) live
in this docstring.  NO RH CLAIM anywhere; nothing here moves a marker.

=====================================================================
THE TYPED LEDGER (severity-ranked within each type)
=====================================================================

--------------------------- OVERSTATED ------------------------------

O-1 [HIGH]  Paper ABSTRACT + section 8.7 vs the deep census.
    Text: "certifying sigma <= 0.727 and hence M > 0 on 151/151
    built wall-legal cells plus 59/59 deep steps to h = 6344" (abstract)
    and "151 in the census plus 59 deep steps ... => sigma <= 0.727
    => M > 0" (8.7).
    Actually computed (CCLXXXVII + CCXCIX; deep_membership_limit_probe
    docstring, verbatim): "CERT-FINITE(worst bound 0.787603 on 59
    steps)" -- the 59-step deep census certifies bound < 1 with worst
    certified bound 0.787603 (margin 0.212397 against the definiteness
    bar 1).  sigma <= 0.726909 is certified on the 151-cell census
    ONLY (CCLXXIX/CCXCIII).  Section 8.2 states it correctly ("below 1
    on 59/59, worst margin 0.2124"); the abstract and 8.7 compress the
    two tiers into one cap and thereby extend 0.727 to 59 cells where
    the certified cap is 0.7876.  Assertion A5.

O-2 [MEDIUM]  Paper abstract (section-6 sentence) + 6.2 composed
    census: "B >= 0.5523*I (exact-rational, 39/39)".
    Actually computed: 0.5523 is the INTERVAL-certified ideal-object
    class floor (v905 rollout; v909 types it "CLIII interval-certified
    class floor" in its docstring, constants and prints).  The
    exact-rational LDL tier certifies min c_B = 0.5914 on the computed
    float matrices (paper 2.3 has both tiers right).  Both tiers are
    rigorous; the label claims the wrong one.

O-3 [LOW]  Paper 8.5: "all nine cells ever read NEGA -- 6197, 6247,
    7958, 8003, 8642, 8677, 9023, 9447, 9535".
    8642 was never read NEGA: CCCV/CCCVII typed it MARGINAL
    (|tau| = 2.122e-12 <= TAU_NOISE 5e-12, explicitly "kein
    Vorzeichenanspruch"), and CCCXXIII's own re-adjudication list
    prints it "(-2.122e-12 MARGINAL)".  CCCXXIII's headline "9/9 je
    NEGA oder zeugen-NEGA gelesene Zellen" carries the same slip with
    inline disclosure.  8/9 of the list is correct.

O-4 [LOW]  Paper 8.6: "the minimal sign-faithful dimension is 24".
    Actually computed (CCCXXV): a NINE-POINT geometric sweep
    (n = 6/12/24/48/...) -- 24 is the smallest TESTED dimension that
    carries the sign on all 67 rungs; 13..23 were never tested.  The
    note words it correctly ("die kleinste GETESTETE Dimension"); the
    paper drops "tested" (it does mention the nine-point sweep, so the
    granularity is recoverable -- hence LOW).

O-5 [INFO]  CCCXXXI headline + paper 8.6: Selberg "insufficient by
    4-5 orders".  Measured: envelope/alignment-margin ratio min
    1.60e4, MEDIAN 9.09e5 (~5.96 dex).  "4-5 orders" is the min end;
    the median miss is ~6 orders.  Direction of the slip: it makes
    Selberg look CLOSER than measured, i.e. friendly to the route --
    worth one line, nothing more.

----------------------- CONVENTION-MISMATCH -------------------------

C-1 [MEDIUM]  TWO DIFFERENT 67-RUNG LADDERS in one paper, never
    distinguished.  Sections 3/5: "67/67" = the frozen registered
    surface, h 142..1433, registry sha ae292e55 (v907, which carries
    the range string verbatim).  Section 8.6 (CCCXXV/CCCXXXI):
    "67/67" = the CCXI level-rung ladder, kz sweep 2..150 -> 67
    BUILT rungs h 184..1393 (core_fluctuation_normalform_probe /
    selberg_symmetry_rewrite_probe; neither file mentions the
    registry sha or its h-range -- zero hits for both).  Equal
    cardinality by coincidence.  Impact: citation drift -- a reader
    identifies 8.6's censuses with the registered surface.  This is
    exactly the known 66-vs-67-vs-68 minefield; the counts themselves
    check out everywhere (A6), the OBJECTS differ here.  Assertion A10.

C-2 [LOW]  sigma at n <= 0: CCLXI's code convention reads sigma =
    q/n NEGATIVE at n < 0 (one-sided cap vacuously true -- the
    mechanism of the open map), CCLXIX types sigma UNDEFINED at
    b1 <= 0.  Cause of t*_num = 0.9188 vs t*_pos = 0.8828.  Found,
    reconciled, and typed as CONVENTION (not a number dispute) inside
    CCLXV itself -- documented, no action.

C-3 [LOW]  SIGMA_ENV circulates in two precisions: registered
    0.780917 = 0.709925 * 1.1 (CCLXIX) vs consumed
    Fraction(7809,10000) = 0.7809 in CCLXXVII/CCLXXIX/CCLXXXI
    (4-digit truncation, direction HARDER, disclosed each time).
    CCLXV adds a third margin convention (t_bar = t_close - 0.05 =
    0.8312).  All disclosed; three near-caps (0.7809 / 0.780917 /
    0.8312) invite mis-citation.

C-4 [LOW]  B-floor currency zoo (all correctly typed at source, easy
    to mis-cite): 0.5914 (exact-rational LDL, computed matrices,
    39 steps) / 0.5523 (interval, ideal objects, 39 steps) / 0.3496
    resp. 0.349574 (measured ladder min lambda_min(B), bridge cell;
    CCLXXV: any interlacing-shaped route MUST use this, not c_B) /
    0.3146 (widened cited class floor, CCLXV).  Finding O-2 is this
    zoo biting.

C-5 [INFO]  next.txt head ordering: CCCXXIX sits on line 1 ABOVE the
    newer CCCXXXI (line 2) -- concurrent prepend race; "line 1 =
    newest" fails here.  And CCXCIII's census phrase "17 F0 + 83
    Sweep = 151 Zellen" reads as 17+83 != 151-68; its own probe states
    it right (radau_sos_certificate_probe: "151 = 68 ladder + 83
    sweep", the 17 F0 being INSIDE the 83).  Assertion A6.

------------------------- QUANTIFIER-SLIP ---------------------------

Q-1 [MEDIUM]  Abstract + 10.1: "what separates this from RH is
    exactly one quantifier (all computed h -> all h)" -- attached to
    the section-6 closure.  But 6.2/6.5 (UNIF-PATH, frozen language):
    W2 is certified along the MEASURED CRITICAL DIRECTION only,
    "nothing is uniform in h or in direction".  For the section-6
    closure the DIRECTION quantifier is open too; "exactly one
    quantifier" is accurate for the section-8 Level-1 cells (full
    M > 0 per built cell), which is not what the sentence cites.

Q-2 [MEDIUM]  Section 1.2: "Proving cofinal positivity for all h is
    the Riemann Hypothesis, full stop."  The kernel-checked chain
    (CofinalWeil.lean) consumes, besides H_cof: per-element form
    convergence of the deployed ladder to the Weil functional --
    typed IN THE LEAN DOC ITSELF as "Piece 2, MEASURED rates
    -1.58..-1.84 per level" -- plus density and C0-continuity
    (classical citations).  "Full stop" quietly upgrades a measured
    finite-level premise to settled.  Same pattern in
    tfpt_prime_front.tex ("per-element convergence is the only
    analytic input ... theorem-grade modulo the named citations" --
    the named citations do not cover the measured convergence).

Q-3 [MEDIUM]  The PREDEFINED-sequence requirement vs the deep
    ladders.  H_cof (CofinalWeil.lean): the index sequence "must be
    chosen INDEPENDENTLY of any measured signs ... never mined from
    the data".  The corrected sub-ladders of CCXCIX/CCCV/CCCXVII/
    CCCXXI/CCCXXIX (MAX-TAU-PER-BIN, MAX-TAU_IDEAL_UB-PER-BIN over
    eligible = sign-read cells) select rungs BY the measured legality
    datum tau -- CCXCIX even labels the rule "source-only", but tau
    is a wall OUTPUT (a sign datum), not source data.  Consequence:
    these ladders can never instantiate H_cof's idx.  NO current text
    claims they do -- but none states the mismatch either, and paper
    8.5 presents "the corrected ladder runs to h* = 10513" directly
    adjacent to the cofinality question.  The compliant construction
    exists and is so typed: CCCXXIX's blind census rule
    MAX-GAP-PER-BIN (census geometry only, frozen pre-build,
    AC-scanned).
    
Q-4 [LOW]  Paper 8.5 / CCCXXIII: "sign-reliable to h = 3948 and no
    longer beyond" -- the bracket (3948, 5539) is unmeasured (factor
    1.40 disclosed in the note); the deployed guard adopts the
    conservative end (refuse > 3948 without floor).  Conservative
    direction; listed for completeness only.

------------------------------ CLEAN --------------------------------

Verified clean by diffing text against probe wards/censuses (digit
checks in A1-A4, A7-A9 where closed-form):
  * 8.2 deep-census wording ("below 1 on 59/59, worst margin 0.2124")
    -- correct where the abstract/8.7 slip (O-1).
  * 8.3 SOS numbers: 1111 = 5 global + 1106 per-cell; 151/151 at
    eta = 0.273; eta* = 273091/1000000; bound 0.726909 = 1 - eta*;
    kz-45 saturation -- digit-consistent across CCXCIII/CCCIX/probe.
  * 8.1 provenance kill of the 0.665 cap: 0.604556 * 1.10 = 0.665012,
    probe code literally max_truth(sigma)*(1+MARGIN_FRAC) (CCLXV).
  * 8.4(b) + hardening (CCXCVII/CCCIII): razor margin +0.010420 =
    1 - (0.502888 + 0.486693); L_plane = 1.312480 vs fit 1.297491;
    t median 0.8326, threshold 4/5, 20/37 -- digit-identical, and the
    paper preserves the DERIVED / PROVED-CONDITIONAL / LIP-CERTIFIED
    typing including "the razor margin is an irreducible measurement".
  * 8.5 retro-correction (CCCXXIII/CCCXXIX): 5 retracted / 3
    superseded / 2 unaffected; h*_clean = 10513; corrected ladder
    6191->6344->8204->8629->9585->10513; arbiter's own edge ~10.6k;
    E1-plus-exact-inertia positive through 13026; "a positive read is
    only 'no witness found', never certified positivity" carried into
    the paper verbatim.  GUARD_BAR provenance exact (A7).
  * 8.6 (CCCXXV/CCCXXXI): normal form exact; inertia (1,2,9); the
    completed square degenerate (rho == 0 identically); need/delivery
    triples and alignment margins digit-identical; Selberg bit-identity
    A_err - B_err = P_err via A_main = 2*B_main (A9); both notes apply
    the frozen gate rule TO THEIR OWN RUN (REFORMULATION-ONLY /
    SELBERG-INSUFFICIENT).
  * GATE-RULE SWEEP of the paper: no passage found that counts a
    reformulation as progress.  10.1 types the localization as "a
    coordinate achievement, not progress on its sign"; section 5 types
    the dictionary as difficulty-conserving; 7.3 types the Euler phase
    as a coordinate change; the survivor-of-retraction language in 8.5
    claims restoration to "fully open, nothing more".
  * Rung enumerations: 42 surface rungs -> 68 = 40+1+27 steps; 85 =
    68+17 floors; 151 = 68+83 cells (83 = 17+25+23+11+7); 59 deep
    steps h 1173..6344; 39 matched steps -- consistent at every
    checked site (A6); the one genuine collision is C-1 (two 67s).

VERDICT: LOGIC-LAYER-MOSTLY-CLEAN( the load-bearing numerics survive
every diff ) + FIVE-OVERSTATEMENTS( one HIGH: the abstract/8.7 deep-
census cap compression ) + ONE-LIVE-CONVENTION-COLLISION( the two
67-rung ladders ) + THREE-QUANTIFIER-SLIPS( direction quantifier,
measured convergence premise, sign-mined ladders vs H_cof ).  The
recommended one-line fixes are implied by each entry; none is applied
here (READ + REPORT scope).

SCOPE: this file plus the CCCXXXVII prepend note in experiments/
next.txt are the only writes.  No verification/, no papers, no ledger,
no website, no manifests, no commit, no .md.  NO RH CLAIM.
"""

import math
import re
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent          # experiments/tfpt-discovery
ROOT = HERE.parent.parent                        # repo root

FAILS = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s%s" % (tag, name, ("  -- " + detail) if detail else ""))
    if not ok:
        FAILS.append(name)


def read(relpath):
    return (ROOT / relpath).read_text(encoding="utf-8", errors="replace")


def main():
    print("logic_audit_report -- executable re-check of the ten most "
          "load-bearing number-claims (see docstring for the ledger)")

    # ---------------------------------------------------------- A1
    # Paper 5.1 dictionary identity, exact in rational arithmetic:
    # (u n + 7)^2 - 7 (u^2 n^2 + 2 u q + 7) == u (14 (n - q) - 6 u n^2),
    # and at u_h = 7 mu1 / (6 n^2) the RHS == 14 u_h (n - q - mu1/2).
    ok = True
    tuples = [(Fraction(3, 2), Fraction(1, 3), Fraction(5, 7),
               Fraction(1, 100)),
              (Fraction(7, 5), Fraction(9, 8), Fraction(2, 11),
               Fraction(3, 1000)),
              (Fraction(-2, 3), Fraction(4, 9), Fraction(13, 6),
               Fraction(1, 7))]
    for n, q, u, mu1 in tuples:
        lhs = (u * n + 7) ** 2 - 7 * (u * u * n * n + 2 * u * q + 7)
        rhs = u * (14 * (n - q) - 6 * u * n * n)
        ok &= (lhs == rhs)
        uh = Fraction(7, 6) * mu1 / (n * n)
        lhs_h = (uh * n + 7) ** 2 - 7 * (uh * uh * n * n + 2 * uh * q + 7)
        ok &= (lhs_h == 14 * uh * (n - q - mu1 / 2))
    check("A1 dictionary identity (5.1) exact over Q, incl. u_h scale",
          ok)

    # ---------------------------------------------------------- A2
    # CCCXXV H2 / paper 8.6 half provenance: (1/2) mu1(h) ==
    # 1 - cos(2 pi / N), N = 2h+1, mu1 = 4 sin^2(pi/N)  (exact trig
    # identity 1 - cos 2x = 2 sin^2 x; float check to 1e-15).
    ok = True
    for h in (142, 878, 1393, 1433, 10513):
        N = 2 * h + 1
        mu1 = 4.0 * math.sin(math.pi / N) ** 2
        ok &= abs(0.5 * mu1 - (1.0 - math.cos(2.0 * math.pi / N))) < 1e-15
    check("A2 half-angle provenance (1/2)mu1 == 1 - cos(2pi/N)", ok)

    # ---------------------------------------------------------- A3
    # CCLXV / paper 8.1: the 0.665 cap is max_truth(sigma) * 1.10 --
    # 0.604556 * 1.10 = 0.665012 (proven coincidence, not mechanism);
    # and the pivot-positive margin 0.8828 - 0.604556 = +0.2782..
    ok = abs(0.604556 * 1.10 - 0.665012) < 5e-7
    ok &= abs((0.8828 - 0.604556) - 0.2783) < 1e-4
    check("A3 sigma-cap provenance 0.604556*1.10 == 0.665012 "
          "and t*_pos margin +0.2783", ok)

    # ---------------------------------------------------------- A4
    # CCXCIII / paper 8.3: eta* = 273091/1000000, worst bound
    # 0.726909 == 1 - eta* exactly at print precision.
    eta = Fraction(273091, 1000000)
    ok = (Fraction(1) - eta == Fraction(726909, 1000000))
    ok &= abs(float(Fraction(1) - eta) - 0.726909) < 5e-7
    check("A4 SOS census saturation: 1 - eta* == 0.726909 exactly", ok)

    # ---------------------------------------------------------- A5
    # Finding O-1: the deep 59-step census certifies worst bound
    # 1 - 0.212397 = 0.787603 (probe docstring, verbatim), which is
    # STRICTLY ABOVE the 0.727 cap that the paper's abstract/8.7
    # extend to those 59 steps.  sigma <= 0.726909 holds on the
    # 151-cell census only.
    ok = abs((1.0 - 0.212397) - 0.787603) < 1e-12
    ok &= (0.787603 > 0.727) and (0.726909 < 0.727)
    probe = read("experiments/tfpt-discovery/"
                 "deep_membership_limit_probe.py")
    ok &= "worst bound 0.787603 on 59 steps" in probe
    paper = read("articles/2026-08-11/"
                 "paper_endform_and_inertia_bridge_en.md")
    present = ("0.727 and hence M" in paper) or ("0.727 ⟹" in paper) \
        or ("σ ≤ 0.727 ⟹" in paper)
    check("A5 deep census worst bound 0.787603 > 0.727 "
          "(O-1; the 0.727 cap is 151-cell-only)", ok,
          "overstating paper passage %s"
          % ("PRESENT (abstract/8.7)" if present else "not found -- fixed?"))

    # ---------------------------------------------------------- A6
    # Census composition arithmetic (CCLXIX/CCLXXIX/CCXCIII):
    # 83 = 17+25+23+11+7 sweep steps, 151 = 68 ladder + 83 sweep,
    # 85 = 68 + 17 floors, 68 = 40 + 1 + 27 steps -- and the probe of
    # record states the 151-composition correctly.
    ok = (17 + 25 + 23 + 11 + 7 == 83) and (68 + 83 == 151)
    ok &= (68 + 17 == 85) and (40 + 1 + 27 == 68)
    sos = read("experiments/tfpt-discovery/radau_sos_certificate_probe.py")
    ok &= "151 = 68 ladder + 83 sweep" in sos
    check("A6 census composition 151 == 68 + 83 (17 F0 inside the 83), "
          "85 == 68 + 17, 68 == 40+1+27", ok)

    # ---------------------------------------------------------- A7
    # CCCXXIX guard bar: GUARD_BAR is the geometric midpoint of the
    # measured CCCXXIII bracket (7.0e-3 reliable, 7.2e-2 unreliable):
    # sqrt(7.0e-3 * 7.2e-2) = 2.2450e-2, and the deployed constant in
    # verdicta_protocol_probe.py equals it.
    gm = math.sqrt(7.0e-3 * 7.2e-2)
    ok = abs(gm - 2.2450e-2) < 5e-6
    verd = read("experiments/tfpt-discovery/verdicta_protocol_probe.py")
    m = re.search(r"^GUARD_BAR\s*=\s*([0-9.eE+-]+)", verd, re.M)
    ok &= (m is not None) and abs(float(m.group(1)) - gm) < 5e-6
    check("A7 GUARD_BAR == geometric midpoint of (7.0e-3, 7.2e-2) "
          "== 2.2450e-2 (declared convention A3)", ok)

    # ---------------------------------------------------------- A8
    # CCLXXXIX finding: the inherited interlacing upper bracket
    # lambda_{m+1}(J) <= lambda_m(J_B) is UNSOUND, Cauchy's
    # lambda_m(J) <= lambda_m(J_B) is the true form.  Explicit 2x2
    # counterexample, closed-form eigenvalues: J = [[10,3],[3,1]],
    # J_B = [1].
    tr, det = 10.0 + 1.0, 10.0 * 1.0 - 3.0 * 3.0
    disc = math.sqrt(tr * tr - 4.0 * det)
    lam_hi, lam_lo = (tr + disc) / 2.0, (tr - disc) / 2.0
    lam_jb = 1.0
    ok = (lam_hi > lam_jb)          # claimed-false bracket violated
    ok &= (lam_lo <= lam_jb)        # Cauchy form holds
    check("A8 interlacing bracket lambda_{m+1}(J) <= lambda_m(J_B) "
          "violated by explicit witness; Cauchy form holds "
          "(CCLXXXIX A1)", ok,
          "lam_hi %.4f > 1 >= lam_lo %.4f" % (lam_hi, lam_lo))

    # ---------------------------------------------------------- A9
    # CCCXXXI C3: A_main - B_main == B_main identically, so the
    # printed triples must satisfy A_main == 2 B_main; and the two
    # 8.6 margin censuses are DIFFERENT quantities, both correctly
    # signed: main-term margin min +0.2246 > 0 (67/67) while the
    # delivered margin (Q-A)-need has min -0.0778 < 0 (66/67).
    a_main = (-5.5388, -4.8014, -4.2121)
    b_main = (-2.7694, -2.4007, -2.1061)
    ok = all(abs(a - 2 * b) <= 2e-4 for a, b in zip(a_main, b_main))
    ok &= (0.2246 > 0.0) and (-0.0778 < 0.0)
    check("A9 Selberg identity A_main == 2*B_main (=> A_err - B_err "
          "== P_err) and the 67/67-vs-66/67 censuses are distinct "
          "quantities", ok)

    # ---------------------------------------------------------- A10
    # Finding C-1: the two 67-rung ladders differ as OBJECTS.  The
    # registered surface is h 142..1433 (v907, "67-rung registered
    # surface"); the 8.6 ladder is the CCXI level-rung sweep, 67
    # built rungs h 184..1393 (notes CCCXXV/CCCXXXI, next.txt) --
    # and the 8.6 probes never consume the registry (no sha
    # ae292e55 anywhere in their sources).
    v907 = read("verification/v907_halfgap_registered_target.py")
    ok = ("142..1433" in v907)
    head = read("experiments/next.txt")[:200000]
    ok &= ("184..1393" in head)
    nf = read("experiments/tfpt-discovery/"
              "core_fluctuation_normalform_probe.py")
    slb = read("experiments/tfpt-discovery/"
               "selberg_symmetry_rewrite_probe.py")
    ok &= ("ae292e55" not in nf) and ("ae292e55" not in slb)
    ok &= (142, 1433) != (184, 1393)
    check("A10 two distinct 67-rung ladders: registry h 142..1433 "
          "(v907) vs CCXI level ladder h 184..1393; 8.6 probes never "
          "consume the registry", ok)

    # ------------------------------------------------------ verdict
    n_fail = len(FAILS)
    print()
    if n_fail == 0:
        print("ALL 10 ASSERTIONS PASS -- the load-bearing numbers check "
              "out; the ledger findings (docstring) are text-vs-"
              "computation diffs, not numeric errors.")
    else:
        print("%d ASSERTION(S) FAILED: %s" % (n_fail, ", ".join(FAILS)))
    print("NO RH CLAIM.  READ + REPORT scope; no marker moved.")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
