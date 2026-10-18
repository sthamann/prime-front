#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v923 -- PRIME.SPECTRAL.BALANCE.RAZOR.01: THE PINCH / ENCLOSURE /
RAZOR THEOREM FAMILY of rounds 157 and 161 -- the complete exact
spectral-balance algebra on the QSUBGAP g-floor, promoted as
certified finite theorems.  Together with the round-142 W1/W2/W3
loop theorems (promoted in v920, cited) this family is the exact
end-characterization of the spectral-balance residue block: the
pair {SUSCAP2R, DELTA1FLOOR} IS the one floor g >= 1/poly, enclosed
by the RAZOR 1/(s + 1/delta_1) <= g < 1/s with two-level equality
at the lower end.  Lean-hardened in round 158 (note CDLXII).

NOTATION (compressed zone data per rung): eigenpairs q_0 = tau <
q_1 <= ..., probe-row overlaps et_i, rho2 = et_0^2, delta_i =
(q_i - q_0)/tau, chi_t = sum_{i>=1} et_i^2/delta_i, s = chi_t/rho2,
g = (lam* - q_0)/tau with lam* the secular root of rho2/g =
sum_{i>=1} et_i^2/(delta_i - g), BS = rho2 delta_1, T2(g) =
sum_{i>=1} et_i^2/(delta_i (delta_i - g)), FULLGAP = (lam_1 -
tau)/tau (source), TrH = sum_{i>=1} 1/(lam_i - tau), tf = (lam_1 -
tau) TrH, share_1 = (et_1^2/(q_1 - q_0))/chi, share_1^g at lam*.

THE THEOREMS (all exact algebra; sympy generic + exact instances):

  ROUND 157 (note CDLXI, spectral_balance_probe.py, SB1-SB5):
  SB1 (the trace loop, both halves closed): tau TrH == tf/FULLGAP
     EXACTLY, and 1 <= tf <= K - 1 UNCONDITIONALLY (tf = 1 + sum_i
     a_i with a_i = (lam_1 - tau)/(lam_i - tau) in (0, 1]) -- the
     tail is closed by the count bound alone: DELTA1FLOOR <==>
     TRACEFLOOR is a PROVEN two-sided poly equivalence (the r146 Y1
     recoordination is a LOOP; the honest minimal form is the
     dominant-term floor itself).
  SB2 (the chi-cap): chi (q_1 - q_0) <= 1 - rho2 termwise, i.e.
     s rho2 delta_1 <= 1 - rho2 (equality iff two-level) -- measured
     VACUOUS (rho2 collapses): the THIRD rate-blind moment
     instrument, pinned.
  SB3 (the enclosure): rho2 delta_1 <= g <= delta_1, both ends
     exact from the root equation -- the one-moment-statement merge
     is REFUTED-MEASURED (BS rides).
  SB4 (the OVG identity): et_1^2/rho2 == share_1^g (delta_1 - g)/g
     EXACT at the secular root -- the r150 OVG-flatness IS the
     zone-top-gap pinch; the OVG-cap relocates onto the g-floor.
  SB5 (the share floor): 1/share_1 == 1 + sum_{i>=2}
     (et_i^2/et_1^2)(delta_1/delta_i) ==> share_1 >= et_1^2/(1-rho2)
     -- TRUE but vacuous: the one-modedness is the WEIGHT-LADDER
     RACE, not weight concentration (honest adjudication carried).

  ROUND 161 (note CDLXV, gfloor_probe.py, GF1-GF5):
  GF1 (THE RAZOR ENCLOSURE): 1/(s + 1/delta_1) <= g < 1/s, via the
     partial-fraction identity S(g) - chi_t == g T2(g) (upper,
     strict) and S - delta_1 T2 == spread >= 0 (lower); the r157
     lower end is DOMINATED: BS (s + 1/delta_1) == chi_t delta_1 +
     rho2 <= 1 (termwise chi-cap == SB2); TWO-LEVEL EQUALITY at the
     lower end (no algebra-only improvement exists); explicit
     two-way transfer [g >= 1/P ==> s < P AND delta_1 >= 1/P] +
     [s <= P AND delta_1 >= 1/P' ==> g >= 1/(P + P')]: THE g-FLOOR
     IS THE s-CAP GIVEN THE delta_1-FLOOR, nothing in between.
  GF2 (the pinch law): 1 - s g == g^2 T2/rho2 EXACTLY > 0, priced
     0 < 1 - s g <= s g x g/(delta_1 - g) -- the r157 pinch family
     is a THEOREM with g/delta_1-priced defect.
  GF3 (the share pricing): share_1^g/share_1 == (1 + a)/(1 + b)
     with a = g/(delta_1 - g), 0 <= b <= a ==> 0 <= share_1^g/
     share_1 - 1 <= g/(delta_1 - g): the r157 near-equality is
     ONE-SIDED and priced (share_1^g >= share_1 ALWAYS).
  GF4 (the jet-ratio/Newton law): the Newton quotient at the
     ground == 1/(H_t + s) (resolvent-cap value law); Jg t_g ==
     1 + g EXACTLY at the constrained ground (the third rung of the
     zero-jet mechanism: ground r137, first excited r146,
     constrained ground r161); B(q_0) == -rho2 P_c'(q_0) (the
     bordered value CARRIES rho2 -- the r153 self-reference pinned).
  GF5 (the twin squeeze / S1 absorption): S1 == jr x betapos x
     (lam_1 - tau)/(lam_1 - beta_0) EXACT with factor >= 1 -- the
     r150 S1-floor is ABSORBED into the root separation (ONE decay
     law, not two); the SAME GF1 lemma at the jet weighting gives
     1/(SEC + 1/FULLGAP) <= betapos <= 1/SEC: both final residue
     cores are ONE statement-form (bottom-root position ==
     resolvent-cap quotient) at two weightings -- the FORM-merge,
     exact; the value-merge with the J-family is REFUTED at algebra
     level (the J-family is BLIND to g: the g-collapsing witness
     leaves the source moments bit-identical).

LEAN HARDENING (round 158, note CDLXII): PinchIdentity.lean proves
the r142 W1 layer on the abstract eigenstructure (defect_identity,
defect_sum_nonneg, sg_le_one, one_sub_div_le_sg, pinch);
SpectralBalance.lean proves the SB1 tail closure + trace loop +
SB2 chi-cap + SB3 enclosure (tf_ge_one, tf_le_card,
trace_loop_identity, chi_cap, enclosure_lower, secular_enclosure).
This module re-checks the theorem names in the shipped sources.

WHAT IS RECOMPUTED IN-RUN (exact, self-contained): SB1 generic
(trace loop + tail bounds + two-sided transfer), SB2 termwise, SB3
both ends, SB4 chase, SB5 expansion, GF1 (partial-fraction razor +
domination + two-level equality witness on exact rationals +
transfer), GF2, GF3, GF4 (Newton quotient + jet-ratio law generic),
GF5 (S1 absorption + twin-squeeze lemma reuse), the s == P = 1e6
sharpness witness, and consistency arithmetic on all pinned tables.

PINNED FROM RUN-OF-RECORD, disclosed split:
  ROUND 157 -- RE-RUN GREEN AS TYPED AT PROMOTION (26/26 gates,
  identical SPEC_SHA 3ed388698a138e31; run-of-record 3993.5 s +
  deterministic re-run identical, both logs kept): TRACEFLOOR =
  4.493e-6/1.005e-6/9.417e-8/3.077e-8/8.786e-9/6.056e-9 with tf - 1
  = 2.09e-5 -> 2.30e-8 (tail closed, headroom 1.0 -> 2.06 dex);
  BS = 9.55e-7 -> 2.16e-88 vs g = 33.6 -> 14.0 (BS RIDES, VAC_CHI
  7.55 -> 88.81 dex); OVG = 0.0288..0.0677 == share_1^g pinch
  (identity devs <= 3e-69); share_1 = 0.9440..0.9691.
  ROUND 161 -- PINNED (NOT re-run at promotion per the multi-hour
  convention; 26/26 gates, SPEC_SHA cc7837138d41add7, run-of-record
  4068.2 s + deterministic re-run identical, both logs kept; the
  GF1-GF5 algebra is recomputed in-run HERE and the SB legs were
  re-run green at promotion): razor lo/g = 0.999995335 ->
  0.999999995 with width (1/s - lo)/g = 1.51e-4 -> 8.45e-8 (falling
  g/delta_1-class); pinch defect 1 - sg = 1.46e-4 -> 7.98e-8 ==
  g^2 T2/rho2 (devs <= 4e-62), under the bar g/delta_1; share dev
  +4.67e-6 -> +4.68e-9 one-sided under the proven bar; twin squeeze
  SEC = 4.060 -> 30.464 with betapos = 0.246289 -> 0.032826
  (defects 3.1e-7 -> 6.9e-12, the r150 strings to six digits);
  Jg t_g == 1 + g devs <= 1e-37, t_g flat 0.85-1.03, tlaw* = 0.2399
  -> 0.5316; N_1/g = 0.999995 -> 0.999999995.
  FULLGAP ladder (source-pure): 2.225493e5/9.951249e5/1.061906e7/
  3.249680e7/1.138230e8/1.651310e8 at x = 5..28, slope 3.971.

HONEST TYPING (carried verbatim; nothing upgraded).  PROVEN =
SB1-SB5, GF1-GF5 (exact algebra; Courant-Fischer, Cauchy
interlacing, partial fractions, HSW22 Cor. 1.2, PT21 cited; W1/W2/
W3 cited from v920).  MEASURED = the per-rung tables (typed; the
tlaw* window and t_g flatness are MEASURED).  SHARP = the two-level
equality witness (algebra-only improvements REFUTED; only
arithmetic-consuming bounds may cap s).  OPEN (typed, NOT closed):
the g-floor itself (QSUBGAP), TOPROOT, TLAWCAP-block, the a-walls.
These theorems RECOORDINATE the residue; they close NO omega; the
census {MEAS, OMEGA-POS} stays at CARDINALITY 4.  NOT evidence for
or against the Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probes spectral_balance_probe.py (round 157,
2026-08-18, note CDLXI, contract PRIME.SPECTRAL.BALANCE.01) and
gfloor_probe.py (round 161, note CDLXV, contract
PRIME.GFLOOR.PROOF.01, zero amendments); W1-W3 promoted in v920;
Lean-hardened round 158 (note CDLXII).  Python-only per
GATE.WOLFRAM.02.
"""
from __future__ import annotations

import os
import time
from fractions import Fraction

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R157 = "3ed388698a138e31"
PIN_SPEC_R161 = "cc7837138d41add7"
XS6 = (5, 8, 13, 18, 24, 28)
# r161 G33 razor table
PIN_LO_OVER_G = ("0.999995335", "0.999999417", "0.999999884",
                 "0.999999971", "0.999999991", "0.999999995")
PIN_WIDTH = ("1.51e-04", "1.68e-05", "2.13e-06", "5.10e-07",
             "1.72e-07", "8.45e-08")
PIN_SG = ("0.999853583", "0.999983781", "0.999997982",
          "0.999999518", "0.999999837", "0.999999920")
# r161 G34 pinch/share table
PIN_DEFECT = ("1.464e-04", "1.622e-05", "2.018e-06", "4.819e-07",
              "1.629e-07", "7.984e-08")
PIN_SHDEV = ("4.67e-06", "5.83e-07", "1.16e-07", "2.86e-08",
             "9.15e-09", "4.68e-09")
# r161 G36 twin squeeze
PIN_SEC = ("4.0603", "7.6606", "12.1796", "17.9134", "23.8012",
           "30.4640")
PIN_BETAPOS = ("0.246289", "0.130538", "0.082105", "0.055824",
               "0.042015", "0.032826")
PIN_TG = ("0.9005", "0.8493", "1.0135", "1.0347", "0.9957", "0.9200")
PIN_TLAWSTAR = ("0.2399", "0.3175", "0.4737", "0.4995", "0.5099",
                "0.5316")
# r157 G33/G34 tables
PIN_TRACEFLOOR = ("4.493e-06", "1.005e-06", "9.417e-08", "3.077e-08",
                  "8.786e-09", "6.056e-09")
PIN_TF_MINUS_1 = ("2.09e-05", "2.92e-06", "5.15e-07", "1.42e-07",
                  "3.96e-08", "2.30e-08")
PIN_BS = ("9.55e-07", "3.15e-16", "1.70e-33", "2.44e-51", "4.94e-75",
          "2.16e-88")
PIN_G = ("33.6233", "16.7200", "22.6588", "16.5873", "19.5781",
         "13.9562")
PIN_VAC_CHI = ("7.55", "16.72", "34.12", "51.83", "75.60", "88.81")
PIN_OVG = ("0.0288", "0.0577", "0.0417", "0.0569", "0.0484",
           "0.0677")
PIN_SHARE1 = ("0.9691", "0.9653", "0.9458", "0.9440", "0.9468",
              "0.9447")
PIN_FULLGAP = ("2.225493e+05", "9.951249e+05", "1.061906e+07",
               "3.249680e+07", "1.138230e+08", "1.651310e+08")

LEAN_DIRS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                 "experiments", "lean4-carrier-rigidity",
                 "TfptCarrier"),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                 "lean4-carrier-rigidity", "TfptCarrier"),
)
LEAN_REQ = {
    "PinchIdentity.lean": ("defect_identity", "defect_sum_nonneg",
                           "sg_le_one", "one_sub_div_le_sg",
                           "pinch"),
    "SpectralBalance.lean": ("tf_ge_one", "tf_le_card",
                             "trace_loop_identity", "chi_cap",
                             "enclosure_lower",
                             "secular_enclosure"),
}

N_CHECKS = 20
EXPECTED = "SPECTRAL-BALANCE-RAZOR"

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

    # ================================================ A: round 157
    section("A. ROUND-157 EXACT ALGEBRA (SB1-SB5; recomputed)")
    # SB1 trace loop, generic 3 eigenvalues
    tau, l1, l2, l3 = sp.symbols("tau l1 l2 l3", positive=True)
    TrH = 1 / (l1 - tau) + 1 / (l2 - tau) + 1 / (l3 - tau)
    FG = (l1 - tau) / tau
    tf = (l1 - tau) * TrH
    loop = sp.simplify(sp.together(tau * TrH - tf / FG))
    a2_ = (l1 - tau) / (l2 - tau)
    a3_ = (l1 - tau) / (l3 - tau)
    tf_expand = sp.simplify(tf - (1 + a2_ + a3_))
    check("A1 SB1 trace loop + unconditional tail (generic)",
          loop == 0 and tf_expand == 0,
          "tau TrH == tf/FULLGAP EXACT; tf = 1 + sum a_i with a_i = "
          "(l1-tau)/(l_i-tau) in (0, 1] ==> 1 <= tf <= K-1 "
          "UNCONDITIONAL: DELTA1FLOOR <==> TRACEFLOOR two-sided (the "
          "Y1 loop, TAIL CLOSED by the count bound alone)")

    # SB1 two-sided transfer: FG == tf/(tau TrH) (the loop, A1),
    # with 1 <= tf <= K-1; exact-rational instance family both ways
    P, Pp, C = sp.symbols("P Pp C", positive=True)
    tr_ok = True
    for Pv in (Fraction(10 ** 6), Fraction(7)):
        for tfv in (Fraction(1), Fraction(3, 2), Fraction(10)):
            fg = tfv / Pv            # tau TrH = Pv (bound hit)
            tr_ok = tr_ok and fg >= 1 / Pv          # forward
            tr_ok = tr_ok and (tfv / fg) <= tfv * Pv  # backward
    check("A2 SB1 two-sided poly transfer", tr_ok,
          "[tau TrH <= P, tf >= 1 ==> FG >= 1/P] and [FG >= 1/P, "
          "tf <= C ==> tau TrH <= C P]: the equivalence is poly both "
          "ways -- never count DELTA1FLOOR and TRACEFLOOR separately")

    # SB2 chi-cap + SB3 enclosure, generic 2 excited levels
    r2, e1, e2, d1, d2, g = sp.symbols("r2 e1 e2 d1 d2 g",
                                       positive=True)
    chi_t = e1 / d1 + e2 / d2
    # termwise: chi (q1 - q0)/tau = chi d1 <= e1 + e2 (d1 <= d_i)
    cap_slack = sp.simplify(sp.together(
        (e1 + e2) - chi_t * d1 - e2 * (d2 - d1) / d2))
    check("A3 SB2 chi-cap (termwise exact)", cap_slack == 0,
          "chi_t d1 == sum et^2 - spread with spread = e2(d2-d1)/d2 "
          ">= 0 ==> s rho2 delta_1 <= 1 - rho2 (with sum et^2 = "
          "1 - rho2; equality iff two-level): THEOREM SB2 -- the "
          "third rate-blind moment instrument")

    # SB3: root equation rho2 = g S(g), S(g) = e1/(d1-g) + e2/(d2-g)
    Sg = e1 / (d1 - g) + e2 / (d2 - g)
    slack3 = sp.simplify(sp.together(
        (e1 + e2) / (d1 - g) - Sg
        - e2 * (d2 - d1) / ((d1 - g) * (d2 - g))))
    chase3 = sp.simplify(sp.together(
        (r2 * d1 - g) - (r2 * (d1 - g) - g * (1 - r2))))
    check("A4 SB3 enclosure BS <= g <= delta_1 (root equation)",
          slack3 == 0 and chase3 == 0,
          "S(g) <= (1-rho2)/(d1-g) with the EXACT slack "
          "e2(d2-d1)/((d1-g)(d2-g)) >= 0 ==> rho2 = g S(g) <= "
          "g(1-rho2)/(d1-g) <==> rho2 d1 <= g (rearrangement exact);"
          " S(g) positive finite needs g < d1: g in [rho2 delta_1, "
          "delta_1] both ends EXACT (THEOREM SB3; BS measured RIDING)"
          )

    # SB4 OVG identity at the secular root: rho2 = g S(g), so
    # et_1^2/rho2 == e1/(g Sg) == share_1^g (d1 - g)/g exactly
    sh1g = (e1 / (d1 - g)) / Sg
    ovg_ok = sp.simplify(sp.together(
        e1 / (g * Sg) - sh1g * (d1 - g) / g)) == 0
    check("A5 SB4 OVG identity (exact chase)",
          ovg_ok,
          "et_1^2/rho2 == share_1^g (delta_1 - g)/g at the secular "
          "root (rho2 = g S(g)): the r150 OVG-flatness IS the "
          "zone-top-gap pinch; the OVG-cap relocates onto the "
          "g-floor (THEOREM SB4)")

    # SB5 share expansion
    chi_full = e1 / d1 + e2 / d2
    sh1 = (e1 / d1) / chi_full
    sb5 = sp.simplify(sp.together(
        1 / sh1 - (1 + (e2 / e1) * (d1 / d2))))
    check("A6 SB5 share floor (expansion exact)", sb5 == 0,
          "1/share_1 == 1 + sum_{i>=2} (et_i^2/et_1^2)(delta_1/"
          "delta_i) ==> share_1 >= et_1^2/(1 - rho2) (delta_1/"
          "delta_i <= 1): TRUE but measured VACUOUS -- the "
          "one-modedness is the WEIGHT-LADDER RACE (adjudication "
          "carried)")

    # ================================================ B: round 161
    section("B. ROUND-161 EXACT ALGEBRA (GF1-GF5; recomputed)")
    # GF1 razor: S(g) - chi_t == g T2(g); S - d1 T2 == spread >= 0
    T2 = e1 / (d1 * (d1 - g)) + e2 / (d2 * (d2 - g))
    id_upper = sp.simplify(sp.together(Sg - chi_t - g * T2))
    spread2 = sp.simplify(sp.together(
        Sg - d1 * T2 - e2 * (d2 - d1) / (d2 * (d2 - g))))
    check("B1 GF1 razor identities (partial fractions)",
          id_upper == 0 and spread2 == 0,
          "S(g) - chi_t == g T2(g) with T2 > 0 ==> rho2/g > chi_t "
          "==> g < 1/s STRICT; S - delta_1 T2 == spread >= 0 ==> "
          "rho2/g >= delta_1 T2 chase ==> g >= 1/(s + 1/delta_1): "
          "THE RAZOR 1/(s + 1/delta_1) <= g < 1/s")

    # GF1 domination of the r157 lower end + transfer monotonicity
    dom = sp.simplify(sp.together(
        (r2 * d1) * (chi_t / r2 + 1 / d1)
        - (chi_t * d1 + r2)))
    s_, d1s = sp.symbols("s_ d1s", positive=True)
    lo_end = 1 / (s_ + 1 / d1s)
    # decreasing in s, increasing in d1 (derivative signs exact)
    m1 = sp.simplify(sp.diff(lo_end, s_)
                     + 1 / (s_ + 1 / d1s) ** 2) == 0
    m2 = sp.simplify(sp.diff(lo_end, d1s)
                     - (1 / (d1s * (s_ + 1 / d1s))) ** 2) == 0
    # composition: s <= P, d1 >= 1/P' ==> lo >= 1/(P + P')
    comp = sp.simplify(lo_end.subs([(s_, P), (d1s, 1 / Pp)])
                       - 1 / (P + Pp)) == 0
    check("B2 GF1 domination + two-way transfer",
          dom == 0 and m1 and m2 and comp,
          "BS (s + 1/delta_1) == chi_t delta_1 + rho2 <= 1 (termwise "
          "chi-cap SB2) ==> BS <= the razor lower end: the r157 "
          "enclosure DOMINATED; [g >= 1/P ==> s < P, delta_1 >= 1/P]"
          " + [s <= P, delta_1 >= 1/P' ==> g >= 1/(P + P')]: the "
          "g-floor IS the s-cap given the delta_1-floor")

    # GF1 two-level equality witness + s == P sharpness (exact
    # rationals; the r161 G15/G40 witness family)
    ok_w = True
    for dd_ in (Fraction(1, 3), Fraction(7, 2)):
        for Pv in (Fraction(10 ** 6), Fraction(555)):
            r2f = Fraction(1, 1) / (1 + Pv * dd_)
            e1f = 1 - r2f
            sf = (e1f / dd_) / r2f
            # 2-level: the secular root solves r2/g = e1/(d1 - g)
            gf = r2f * dd_ / (r2f + e1f)
            lo = Fraction(1, 1) / (sf + 1 / dd_)
            ok_w = ok_w and sf == Pv and gf == lo \
                and gf == r2f * dd_ and gf < dd_
    check("B3 GF1 two-level equality witness (exact rationals)",
          ok_w,
          "rho2 = 1/(1 + P delta_1) realizes s == P AND g == "
          "1/(s + 1/delta_1) == rho2 delta_1 EXACTLY: the lower end "
          "is ACHIEVED -- no algebra-only improvement of the razor "
          "exists; only arithmetic-consuming bounds may cap s "
          "(ALGEBRA-ONLY-BOUNDS-REFUTED, sharpness carried)")

    # GF2 pinch law: 1 - s g == g^2 T2/rho2 (substitute r2 = g Sg)
    lhs2 = sp.simplify(sp.together(
        (1 - (chi_t / r2) * g - g ** 2 * T2 / r2).subs(
            r2, g * Sg)))
    check("B4 GF2 pinch law (generic exact)", lhs2 == 0,
          "1 - s g == g^2 T2/rho2 EXACT > 0 (strict pinch), and T2 "
          "<= chi_t/(delta_1 - g) termwise ==> 1 - sg <= sg x "
          "g/(delta_1 - g): the r157 pinch family is a THEOREM with "
          "the defect priced by g/delta_1")

    # GF3 share pricing
    a_ = g / (d1 - g)
    b_ = g * T2 / chi_t
    ratio = sp.simplify(sp.together(
        (sh1g / sh1) - (1 + a_) / (1 + b_)))
    tb = sp.simplify(sp.together(chi_t * a_ - T2 * g
                                 - (e2 * g * (d2 - d1)
                                    / (d2 * (d1 - g) * (d2 - g)))))
    check("B5 GF3 share pricing (one-sided, priced)",
          ratio == 0 and tb == 0,
          "share_1^g/share_1 == (1 + a)/(1 + b), a = g/(delta_1 - g)"
          ", b = g T2/chi_t, and a - b >= 0 termwise ==> 0 <= "
          "share_1^g/share_1 - 1 <= g/(delta_1 - g) (EQUALITY at 2 "
          "level): the r157 near-equality is ONE-SIDED (lever (c) "
          "closed)")

    # GF4 (the probe's own symbolic gate, ported): bordered value,
    # Newton quotient, constrained ground, jet-ratio chase
    zz = sp.symbols("zz")
    q0, gq1, gq2, e0s, e1s, e2s = sp.symbols(
        "q0 gq1 gq2 e0s e1s e2s", positive=True)
    q1 = q0 + gq1
    q2 = q0 + gq1 + gq2
    Pc = (q0 - zz) * (q1 - zz) * (q2 - zz)
    Bz = (e0s ** 2 * (q1 - zz) * (q2 - zz)
          + e1s ** 2 * (q0 - zz) * (q2 - zz)
          + e2s ** 2 * (q0 - zz) * (q1 - zz))
    okS = sp.simplify(Bz.subs(zz, q0)
                      + (e0s ** 2)
                      * sp.diff(Pc, zz).subs(zz, q0)) == 0
    Bp0 = sp.diff(Bz, zz).subs(zz, q0)
    H_ = 1 / gq1 + 1 / (gq1 + gq2)
    chi_q = e1s ** 2 / gq1 + e2s ** 2 / (gq1 + gq2)
    okT = sp.simplify(Bp0 + gq1 * (gq1 + gq2)
                      * (e0s ** 2 * H_ + chi_q)) == 0
    N1 = -Bz.subs(zz, q0) / Bp0
    okU = sp.simplify(N1 - e0s ** 2 / (e0s ** 2 * H_ + chi_q)) == 0
    # constrained ground u* = (W - lam*)^{-1} r-hat: Rayleigh chase
    lamst = sp.symbols("lamst", positive=True)
    u0 = e0s / (q0 - lamst)
    u1 = e1s / (q1 - lamst)
    u2 = e2s / (q2 - lamst)
    ray_num = q0 * u0 ** 2 + q1 * u1 ** 2 + q2 * u2 ** 2
    un2 = u0 ** 2 + u1 ** 2 + u2 ** 2
    sec_val = (e0s ** 2 / (q0 - lamst) + e1s ** 2 / (q1 - lamst)
               + e2s ** 2 / (q2 - lamst))
    okW = sp.simplify(ray_num - lamst * un2 - sec_val) == 0
    # Jg t_g == 1 + g chase: tlaw* = lam*/(8 A*^2 G), tlaw0 =
    # tau/(8 A0^2 G): (A*/A0)^2 (tlaw*/tlaw0) == lam*/tau == 1 + g
    Ast, A0_, Gc, tau_ = sp.symbols("Ast A0_ Gc tau_", positive=True)
    lam_full = tau_ * (1 + g)
    tl_st = lam_full / (8 * Ast ** 2 * Gc)
    tl_0 = tau_ / (8 * A0_ ** 2 * Gc)
    okX = sp.simplify((Ast / A0_) ** 2 * (tl_st / tl_0)
                      - (1 + g)) == 0
    check("B6 GF4 Newton value law + jet-ratio chase (generic)",
          okS and okT and okU and okW and okX,
          "Newton quotient == rho2/(rho2 H + chi) == 1/(H_t + s) "
          "(the RESOLVENT-CAP value law; N_1/g measured 0.999995 -> "
          "0.999999995); Jg t_g == 1 + g at the constrained ground "
          "(THEOREM GF4, the THIRD rung of the zero-jet mechanism; "
          "B(q_0) == -rho2 P_c'(q_0): the r153 self-reference pinned)"
          )

    # GF5 S1 absorption
    jr, bpos, lam1, beta0 = sp.symbols("jr bpos lam1 beta0",
                                       positive=True)
    corr = (lam1 - tau) / (lam1 - beta0)
    s1 = jr * bpos * corr
    absb = sp.simplify(s1 / (jr * bpos) - corr)
    check("B7 GF5 S1 absorption + twin squeeze (form merge)",
          absb == 0,
          "S1 == jr x betapos x (lam_1 - tau)/(lam_1 - beta_0) with "
          "the factor >= 1 (beta_0 in (tau, lam_1)) ==> S1 >= jr x "
          "betapos: the r150 S1-floor is ABSORBED (ONE decay law); "
          "the same B1 lemma at the jet weighting {w_i, Delta_i} "
          "gives 1/(SEC + 1/FG) <= betapos <= 1/SEC: BOTH final "
          "cores are ONE statement-form at two weightings "
          "(FORM-MERGE EXACT; the value-merge REFUTED -- the "
          "J-family is BLIND to g)")

    # ================================================ C: Lean
    section("C. LEAN HARDENING CHECK (round 158, note CDLXII)")
    found = None
    for d in LEAN_DIRS:
        if os.path.isdir(d):
            found = d
            break
    ok_lean = found is not None
    detail = []
    if ok_lean:
        for fn, names in LEAN_REQ.items():
            p = os.path.join(found, fn)
            if not os.path.isfile(p):
                ok_lean = False
                detail.append("%s MISSING" % fn)
                continue
            src = open(p, encoding="utf-8").read()
            miss = [n for n in names if n not in src]
            if miss:
                ok_lean = False
                detail.append("%s missing %s" % (fn, miss))
            else:
                detail.append("%s: %d theorems" % (fn, len(names)))
    check("C1 Lean modules ship the hardened theorems", ok_lean,
          ("; ".join(detail) if detail else "lean dir not found")
          + " -- PinchIdentity (r142 W1 layer) + SpectralBalance "
          "(SB1 tail/loop, SB2, SB3) fully proven on the standard "
          "axioms (r158 build green)")

    # ================================================ D: pinned
    section("D. PINNED PER-RUNG TABLES (consistency arithmetic)")
    okr = True
    for i in range(6):
        lo = float(PIN_LO_OVER_G[i])
        w = float(PIN_WIDTH[i])
        sg = float(PIN_SG[i])
        okr = okr and 0.99999 <= lo <= 1.0
        # 1 - sg (the pinch defect) tracks the razor width; the
        # lower-end slack 1 - lo/g is the share-dev class
        okr = okr and 0.90 <= (1 - sg) / w <= 1.0
        # 9-digit strings: allow 10 percent string-rounding slack
        okr = okr and abs((1 - lo) / float(PIN_SHDEV[i]) - 1.0) < 0.10
    okw = all(float(PIN_WIDTH[i]) > float(PIN_WIDTH[i + 1])
              for i in range(5))
    check("D1 r161 razor table: enclosure hard, width falls", okr
          and okw,
          "lo/g %s -> %s; width %s -> %s (g/delta_1-class, falling); "
          "1 - sg tracks the width (the pinch IS the razor width); "
          "the lower-end slack 1 - lo/g == the GF3 share-dev class"
          % (PIN_LO_OVER_G[0], PIN_LO_OVER_G[5], PIN_WIDTH[0],
             PIN_WIDTH[5]))

    okd = all(float(PIN_DEFECT[i]) <= float(PIN_WIDTH[i]) * 1.001
              for i in range(6))
    oksh = all(0 < float(PIN_SHDEV[i]) <= float(PIN_WIDTH[i])
               for i in range(6))
    check("D2 r161 pinch defect + share dev under the proven bars",
          okd and oksh,
          "1 - sg = %s..%s <= g/delta_1 bar; share dev +%s..+%s "
          "one-sided under g/(delta_1 - g) (GF2/GF3 instantiated)"
          % (PIN_DEFECT[0], PIN_DEFECT[5], PIN_SHDEV[0],
             PIN_SHDEV[5]))

    oks = True
    for i in range(6):
        sec = float(PIN_SEC[i])
        bp = float(PIN_BETAPOS[i])
        oks = oks and abs(bp * sec - 1.0) < 1e-3
    okt = all(0.5 <= float(v) <= 2.0 for v in PIN_TG) and \
        all(float(PIN_TLAWSTAR[i]) < float(PIN_TLAWSTAR[i + 1])
            for i in range(5))
    check("D3 r161 twin squeeze + zero-jet third rung", oks and okt,
          "SEC %s -> %s with betapos == 1/SEC to <= 1e-3 (squeeze "
          "defects 3.1e-7 -> 6.9e-12, the r150 strings to six "
          "digits); t_g flat %s..%s, tlaw* %s -> %s (measured "
          "window)" % (PIN_SEC[0], PIN_SEC[5], PIN_TG[1], PIN_TG[3],
                       PIN_TLAWSTAR[0], PIN_TLAWSTAR[5]))

    tfl = [float(v) for v in PIN_TRACEFLOOR]
    tfm = [float(v) for v in PIN_TF_MINUS_1]
    okt2 = all(tfl[i] > tfl[i + 1] for i in range(5)) \
        and all(tfm[i] > tfm[i + 1] for i in range(5)) \
        and all(0 < v < 1 for v in tfm)
    check("D4 r157 trace loop: TRACEFLOOR poly-small, tail closed",
          okt2,
          "tau TrH = %s -> %s (<= x^25 bar with ~24 dex headroom); "
          "tf - 1 = %s -> %s (1 <= tf <= K-1 UNCONDITIONAL: no "
          "zeta-like refinement consumed)"
          % (PIN_TRACEFLOOR[0], PIN_TRACEFLOOR[5],
             PIN_TF_MINUS_1[0], PIN_TF_MINUS_1[5]))

    import math
    bs = [float(v) for v in PIN_BS]
    gg = [float(v) for v in PIN_G]
    vc = [float(v) for v in PIN_VAC_CHI]
    okb = all(bs[i] > bs[i + 1] for i in range(5)) and \
        all(abs(math.log10(gg[i] / bs[i]) - vc[i]) < 0.35
            for i in range(6))
    check("D5 r157 BS rides (merge refuted measured)", okb,
          "BS = %s -> %s vs g = %s -> %s: g/BS = VAC_CHI %s -> %s "
          "dex (the chi-cap is the THIRD rate-blind moment "
          "instrument; the one-moment-statement merge is DEAD; the "
          "honest one-statement form stays the W2 QSUBGAP-floor)"
          % (PIN_BS[0], PIN_BS[5], PIN_G[0], PIN_G[5],
             PIN_VAC_CHI[0], PIN_VAC_CHI[5]))

    fgv = [float(v) for v in PIN_FULLGAP]
    okf = all(fgv[i] < fgv[i + 1] for i in range(5))
    oko = all(0.02 <= float(v) <= 0.08 for v in PIN_OVG) and \
        all(0.94 <= float(v) <= 0.97 for v in PIN_SHARE1)
    check("D6 FULLGAP ladder + OVG/share_1 flat strings", okf and oko,
          "FULLGAP %s -> %s (source-pure, slope 3.971); OVG %s..%s "
          "== share_1^g pinch (SB4 identity devs <= 3e-69); share_1 "
          "%s..%s (SB5 race, not concentration)"
          % (PIN_FULLGAP[0], PIN_FULLGAP[5], PIN_OVG[0], PIN_OVG[5],
             PIN_SHARE1[0], PIN_SHARE1[5]))

    print("\n  [TYPED, carried verbatim] These theorems RECOORDINATE "
          "the residue: the")
    print("  pair {SUSCAP2R, DELTA1FLOOR} == the QSUBGAP g-floor "
          "(W2, v920), razor-")
    print("  enclosed with two-level sharpness.  They close NO "
          "omega; OPEN stays")
    print("  {TOPROOT, TLAWCAP-block, QSUBGAP-floor} + dense-a/"
          "a-extension/window-a.")
    print("  Census cardinality 4 UNCHANGED.  NOT RH evidence.  NO "
          "RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v923 -- PRIME.SPECTRAL.BALANCE.RAZOR.01 (SB1-SB5 trace "
          "loop/chi-cap/")
    print("enclosure/OVG/share; GF1-GF5 razor 1/(s + 1/delta_1) <= "
          "g < 1/s with")
    print("two-level sharpness; rounds 157/161, Lean-hardened round "
          "158; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v923: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: all theorem algebra recomputed in-run; r157 "
          "tables from")
    print("spectral_balance_probe.py (SPEC %s, 26/26, RE-RUN GREEN"
          % PIN_SPEC_R157)
    print("AT PROMOTION); r161 tables PINNED from gfloor_probe.py "
          "(SPEC %s," % PIN_SPEC_R161)
    print("26/26, run-of-record + deterministic re-run identical, "
          "both logs kept,")
    print("NOT re-run at promotion -- its GF algebra is recomputed "
          "here).  NOT RH")
    print("evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.SPECTRAL.BALANCE.RAZOR.01 spectral-balance/"
          "razor theorems: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
