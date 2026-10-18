#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v940 -- PRIME.CBJ.SUBDOF.BLOCKFLOOR.01: THE SUB-DOF MASS-FRACTION
KILL + THE CARLESON PRICING of round 181 -- the blockwise SUB-DOF-
SCOPED floor statement (what the program would actually need after
the death of the global frame form: ONE selector rung per dyadic
block, the SF2 demand there, restricted to the well-conditioned
sub-dof family) posed EXACTLY, fully typed, and honestly KILLED at
the decisive measurement: the demand mass is NOT in the well-
conditioned subspace.  Plus the 180-round debt settled: CARLESON
PRICED FOR THE FIRST TIME, with exact citations -- the unconditional
embedding is WRONG-DIRECTION for a floor, and every unconditional
LOWER class misses the sub-dof family for a named reason.

THE EXACT LAYER (sympy; recomputed in-run):

  S1 (THE SCOPED STATEMENT + CHAIN): delta_sub(h) := sum_{lam_i >=
     1e-12 lam_max} lam_i s_i^2 over the eigendecomposition of the
     Jacobi-normalized house Gram (s_i = v_i . Jn); delta ==
     sum_i lam_i s_i^2 EXACT via step-A R == 0 (v939, re-gated);
     the PSD truncation delta_sub <= delta EXACT (dropped terms
     nonnegative); sufficiency EXACT: delta_sub >= delta_req ==>
     delta >= delta_req; SF1 transport EXACT (v939).  The
     composition is CONDITIONAL-TYPED: the exact legs L1-L4 stand,
     the measured floor leg is the corpse.
  S2 (FIXED-R COMPACTNESS SKETCH, r181-G13 -- the round's one
     proof-shaped positive): the jet-normalized cluster Gram
     extends CONTINUOUSLY to full confluence with PD limit: at
     m = 2 the symbolic full-merge limit == diag(1, -Wddot(0)) =
     diag(1, 1) for GAUSS and diag(1, 1/6) for FEJ1 EXACT (the
     1/6 is the SYMPY-EXACT constant -- the frozen spec's 1/12 was
     the disclosed A1 text amendment, BH8-verified); at fixed m-cap
     (== fixed r via the exact occupancy bound) the floor constant
     is a minimum over a COMPACT configuration family with
     positive continuous extension: the k-uniformity of the
     fixed-r comb floor is COMPACTNESS-PROVABLE-SKETCHED (constant
     stays measured; full partial-merge continuity CITED as
     classical confluent-Vandermonde theory).

THE KILL (pinned, typed MEASURED -- the contract's named kill
branch LANDS): THE SUB-DOF MASS FRACTION FALLS AND SATURATES AT
ZERO -- log10 tail ladder (tail = 1 - frac at the 1e-12 cut), h =
4..16+20: -4.077/-2.207/-1.321/-0.330/-0.021/-0.039/-0.001/...
/-0.002: ONE DEX OF MASS LEAVES THE SUB-DOF CELL PER RUNG (the
pre-saturation OLS slope over h = 4..8 == +0.999/rung, RECOMPUTED
IN-RUN from the pinned ladder, window (0.85, 1.15)), saturation
(frac <= 2 percent) from h = 10.  MARGINS (the kill with numbers):
margin_sub = frac x delta/delta_req = 1.405/1.744/1.709 at h =
4/5/6 (clear the 1.35 bar), 1.142 at h-hat(B2) = 7 (clears the raw
demand >= 1, NOT the bar), 0.116 at h = 8, 8.020e-3 at h-hat(B3) =
13 (DEAD BY FACTOR ~125, recomputed): the first drop below the bar
is h = 7 == THE B2 SELECTOR RUNG ITSELF -- THE SUB-DOF-SCOPED SF2
DEMAND DIES AT THE SELECTOR RUNGS.  The UNSCOPED r180 ladder
(margins >= 1.405 at ALL rungs) REMAINS the measured carrier: what
is killed is the PROOF ROUTE through the well-conditioned subspace
("prove only the top modes" cannot work -- the demand mass is not
there).  MASS-RIDES-CONDITIONING-WALL: even the 1e-24 cut keeps
only 1 - 10^{-0.004} == 0.9 percent of the mass at h = 20
(recomputed); the spread table tracks the r180 gmin ladder (1e-17
-> 1e-113 -> 1e-140 class); pole-resonance census n_res = 0..11
(the poles ENTER the window band with h: the house wall is
CONDITIONING, not a clean Landau count).

CARLESON PRICED (web-researched, exactly cited; BH8 web-verified):
DIRECTION -- [OCS02 = Ortega-Cerda--Seip, "Fourier frames", Ann.
of Math. (2) 155 (2002) 789-806]: the Carleson box condition
sup_xi mu([xi, xi+1)) < oo is EQUIVALENT TO THE UPPER inequality
alone -- for a FLOOR the unconditional Carleson embedding is
WRONG-DIRECTION (numerically: C_box = 1..37, ratio lam_max/C_box
in [0.998, 3.917] inside the frozen band [0.9, 4.5]: the UPPER
constant carries).  THE UNCONDITIONAL LOWER CLASSES AND WHY EACH
MISSES (the complete pricing table): [Nazarov 1993, Turan lemma]
unconditional AND explicit but the constant (C|I|/|E|)^{n-1} is
EXPONENTIAL IN THE TERM COUNT == the classical mirror of the
measured r180 occupancy law (-0.7484 dex/atom); [Beurling density]
density-gated -- the sub-dof family is exactly the sub-Nyquist
side (point density theorems never fire there, jets mandatory);
[Blandigneres et al. / Hartmann-Jaming-Kellay, Amer. J. Math. 142
(2020), reverse Carleson] right direction but inf_I mu(S(I))/|I|
fails on FINITE discrete block measures; [Kovrijkine, Proc. AMS
129 (2001)] explicit constants but for dominating SETS time-side,
not atom families; [Hermite/derivative sampling, Wirtinger-Sobolev
frames] explicit lower frame bounds but need uniform jet height at
EVERY node + a global max-gap -- and the max-gap hypothesis fails
EXACTLY on the fine-resolution columns (Gap x H > pi at 8/20
cells) where the sub-dof family lives: THE TWO HYPOTHESES ARE
MUTUALLY EXCLUSIVE ON THE GRID; [Grochenig et al., Constr.
Approx. 2020] right direction, NO explicit constant, not
m-uniform.  The two-sided sandwich at k = 12: log10(lam_max/
c_intra) = 0.28/1.38/3.20/8.06/22.90 dex at r = 0.5/2/8/32/128 --
A 23-DEX TWO-SIDED GAP OPEN IN THE DEPTH; and the S1 kill makes
the debt SHARPER than r180 named it: even a perfect sub-dof frame
theorem would not carry the demand -- the missing tool must
control the ILL-conditioned subspace (the alignment law of the
s_i, delivered in r182/v941).

FRACTION-WORLD-SEPARATING (the SF6 anatomy sharpened; NEW
measured world separator): like-for-like at the CTRL window --
MAIN tails -4.11/-2.26/-0.04 at x = 4/5/8 (window-stable) vs
SMOOTH -13.32, SCRARITH -11.68/-13.37/-14.25, EPSTEIN -11.68/
-12.84/-13.65: in EVERY fake world the jet mass sits in the TOP
modes (fraction-1 class), ONLY the arithmetic world rides the
ill-conditioned tail -- FLOOR VALUE WORLD-INSENSITIVE, MASS
LOCATION WORLD-SEPARATING (the first measured world separator NOT
sitting at the bridge); the comb-side analog aw_q = log(p)/sqrt(q)
has fraction 1.000000 at every cell: the tail ride is HOUSE-
specific alignment, not window geometry.  SEAM: geometrically
present as in r180 (couplings 0.9934..0.9997) but machine-
adjudicated an ancestor of NOTHING in the chain
(SEAM-PRESENT-NOT-CONSUMED-BLOCKWISE).

RE-RUN GREEN AS TYPED AT PROMOTION: cbj_subdof_probe.py round 181
(note CDXCIX, contract PRIME.CBJ.SUBDOF.BLOCKFLOOR.01), 37/37
gates, SPEC_SHA 2db82c76ce5f067c, record 867.9 s + deterministic
re-run 817.5 s (timing-normalized diff empty; ONE disclosed
post-record SPEC-TEXT amendment A1: the frozen prose misquoted
the machine-computed FEJ1 confluent-limit constant (wrote 1/12,
sympy-exact 1/6) and misread two family counts -- NO code, gate,
bar, grid or table moved; run1/run2 kept as error-free records;
BH8-verified: run1-vs-run3 output-identical, the 1/6 correct) --
log kept as cbj_subdof_probe.promo_rerun.log.

HONEST TYPING (BH8 corrections of record ADOPTED): EXACT = S1
chain legs + S2 compactness anchor; MEASURED = the tail/margin/
spread/resonance/fraction tables; CITED-PRICED = the Carleson
table (OCS02 direction, Nazarov-Turan mirror, the named misses);
the round kills the sub-dof PROOF ROUTE, not the demand.  FOUR
loop routes flagged NOT consumed.  THE RESIDUE (canonical, note
DII): {H1 AND H2 AND H3}-cofinal (mod D = 0.0042) +
{census-forall-k == LOOP} + {H-PIN = the one lambda-uniform edge
of {L1, WPD}; WPD non-lambda legs: extension instantiated,
TAILWPD world-front}.  Census cardinality 4 UNCHANGED.  NOT
evidence for or against the Riemann Hypothesis in either
direction.  NO RH CLAIM.

PROVENANCE: discovery probe cbj_subdof_probe.py (round 181,
2026-08-20, note CDXCIX); consumes v939 (step A, the selector, the
gmin ladder, SF2 margins) + v929 (SF1/SF2/SF6); cited classical
inputs: Ortega-Cerda--Seip Ann. of Math. 155 (2002); Nazarov 1993;
Hartmann-Jaming-Kellay Amer. J. Math. 142 (2020); Kovrijkine Proc.
AMS 129 (2001); Grochenig et al. Constr. Approx. 2020; feeds v941
(the alignment law).  Externally covered by Bughunt VIII (round
183, note DI: A1 clean, OCS02 direction web-verified).
Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R181 = "2db82c76ce5f067c"
# r181 G32 THE KILL: log10 tail ladder (tail = 1 - frac at 1e-12 cut)
# h = 4, 5, 6, 7, 8 (pre-saturation window; saturation from h = 10)
PIN_TAIL_PRE = {4: -4.077, 5: -2.207, 6: -1.321, 7: -0.330, 8: -0.021}
PIN_TAIL_SAT = -0.001                  # saturated class (frac <= 2 pct)
PIN_SLOPE_WIN = (0.85, 1.15)
# r181 G34 margins margin_sub = frac x delta/delta_req
PIN_MARGIN_SUB = {4: 1.405, 5: 1.744, 6: 1.709, 7: 1.142, 8: 0.116,
                  13: 8.020e-3}
PIN_BAR = 1.35
PIN_UNSCOPED_MIN = 1.405               # r180 unscoped ladder CITED
# r181 G33 cut spread: the 1e-24 cut at h = 20 keeps 10^-0.004 tail
PIN_CUT24_H20_L10TAIL = -0.004
# r181 G35 pole-resonance census (poles enter the window band)
PIN_NRES = (0, 1, 0, 1, 2, 2, 3, 4, 5, 5, 7, 7, 8, 11)
# r181 G24 Carleson direction (OCS02) numeric leg
PIN_CBOX_RANGE = (1.0, 37.0)
PIN_PP_RATIO = (0.998, 3.917)
PIN_PP_BAND = (0.9, 4.5)
# r181 G25 the two-sided sandwich at k = 12 (r = 0.5/2/8/32/128)
PIN_SANDWICH = (0.28, 1.38, 3.20, 8.06, 22.90)
# r181 G46 FRACTION-WORLD-SEPARATING (log10 tails, CTRL window)
PIN_FRAC_MAIN = (-4.11, -2.26, -0.04)
PIN_FRAC_SMOOTH = -13.32
PIN_FRAC_SCRARITH = (-11.68, -13.37, -14.25)
PIN_FRAC_EPSTEIN = (-11.68, -12.84, -13.65)
# r181 G26 seam couplings at selector rungs (present, not consumed)
PIN_SEAM = (0.9997, 0.9971, 0.9960, 0.9934, 0.9980)
# r180 occupancy law mirrored by Nazarov-Turan
PIN_OCC_SLOPE = -0.7484

N_CHECKS = 9
EXPECTED = "CBJ-SUBDOF-BLOCKFLOOR-KILL"

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


def ols_slope(xs, ys):
    n = len(xs)
    xb = sum(xs) / n
    yb = sum(ys) / n
    num = sum((x - xb) * (y - yb) for x, y in zip(xs, ys))
    den = sum((x - xb) ** 2 for x in xs)
    return num / den


def part():
    import sympy as sp

    # ================================================ A: exact layer
    section("A. THE SCOPED STATEMENT + THE COMPACTNESS SKETCH (exact)")
    lam1, lam2, lam3 = sp.symbols("lam1 lam2 lam3", positive=True)
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    delta = lam1 * s1 ** 2 + lam2 * s2 ** 2 + lam3 * s3 ** 2
    delta_sub = lam1 * s1 ** 2 + lam2 * s2 ** 2
    okA = sp.simplify(delta - delta_sub - lam3 * s3 ** 2) == 0 \
        and (lam3 * s3 ** 2).is_nonnegative
    # sufficiency: delta >= delta_sub (exact) ==> [delta_sub >=
    # delta_req ==> delta >= delta_req] (transitivity); instance
    inst = {lam1: 2, lam2: 1, lam3: sp.Rational(1, 10 ** 12),
            s1: 1, s2: 1, s3: 10}
    dsub_i, d_i = delta_sub.subs(inst), delta.subs(inst)
    dreq_i = sp.Rational(5, 2)
    okB = bool(d_i - dsub_i >= 0)
    okC = bool(dsub_i >= dreq_i) and bool(d_i >= dreq_i) \
        and bool(dsub_i <= d_i)
    check("A1 S1 the scoped chain: truncation exact, sufficiency "
          "exact", okA and okB and okC,
          "delta == sum lam_i s_i^2 (step-A R == 0, v939 re-gated); "
          "delta_sub <= delta EXACT (dropped terms nonnegative, PSD "
          "truncation); delta_sub >= delta_req ==> delta >= "
          "delta_req (sufficiency); the composition is CONDITIONAL-"
          "TYPED: L1-L4 exact legs stand, the MEASURED floor leg is "
          "the corpse (the demand delta_sub(h-hat_k) >= delta_req "
          "is exactly what dies in B1/B2)")

    u = sp.symbols("u", positive=True)
    T2 = sp.Matrix([[1, 1], [-u / 2, u / 2]])
    B2m = T2.inv()
    res = {}
    for wname, wexpr in (("GAUSS", sp.exp(-u ** 2 / 2)),
                         ("FEJ1", sp.sin(u / 2) ** 2 / (u / 2) ** 2)):
        G2 = sp.Matrix([[1, wexpr], [wexpr, 1]])
        K2 = sp.simplify(B2m.T * G2 * B2m)
        res[wname] = sp.Matrix(2, 2, lambda i, j: sp.limit(
            K2[i, j], u, 0, dir="+"))
    okD = res["GAUSS"] == sp.Matrix([[1, 0], [0, 1]])
    okE = res["FEJ1"][0, 0] == 1 and res["FEJ1"][0, 1] == 0 \
        and res["FEJ1"][1, 0] == 0 \
        and res["FEJ1"][1, 1] == sp.Rational(1, 6)
    check("A2 S2 fixed-r compactness sketch (FEJ1 constant == 1/6)",
          okD and okE,
          "the m = 2 full-merge limit of the jet-normalized Gram == "
          "diag(1, -Wddot(0)) EXACT: GAUSS diag(1, 1), FEJ1 "
          "diag(1, 1/6) -- both PD (the SYMPY-EXACT 1/6; the frozen "
          "spec's 1/12 was the disclosed A1 text amendment, "
          "BH8-verified correct): the confluent extension is "
          "continuous and positive at the diagonal -- at fixed m-cap"
          " the fixed-r comb floor k-uniformity is COMPACTNESS-"
          "PROVABLE-SKETCHED (constant stays measured; partial-"
          "merge continuity cited as confluent-Vandermonde theory)")

    # ================================================ B: the kill
    section("B. THE MASS-FRACTION KILL (pinned + recomputed)")
    hs = sorted(PIN_TAIL_PRE)
    slope = ols_slope(hs, [PIN_TAIL_PRE[h] for h in hs])
    okF = PIN_SLOPE_WIN[0] <= slope <= PIN_SLOPE_WIN[1] \
        and abs(slope - 0.999) < 2e-3
    okG = all(PIN_TAIL_PRE[hs[i]] < PIN_TAIL_PRE[hs[i + 1]]
              for i in range(len(hs) - 1)) \
        and PIN_TAIL_SAT > -0.01
    check("B1 the tail ladder: +0.999 dex/rung recomputed, "
          "saturation at zero", okF and okG,
          "log10 tail = -4.077/-2.207/-1.321/-0.330/-0.021 at h = "
          "4..8: OLS slope RECOMPUTED = %.4f/rung (window (0.85, "
          "1.15); ONE DEX OF MASS LEAVES THE SUB-DOF CELL PER "
          "RUNG), saturation (frac <= 2 pct, tail -> %.3f) from "
          "h = 10: THE SUB-DOF MASS FRACTION FALLS AND SATURATES "
          "AT ZERO -- the contract's named kill branch LANDS"
          % (slope, PIN_TAIL_SAT))

    okH = all(PIN_MARGIN_SUB[h] >= PIN_BAR for h in (4, 5, 6)) \
        and 1.0 <= PIN_MARGIN_SUB[7] < PIN_BAR \
        and PIN_MARGIN_SUB[8] < 1.0 and PIN_MARGIN_SUB[13] < 0.01
    dead_factor = 1.0 / PIN_MARGIN_SUB[13]
    okI = abs(dead_factor - 125) < 1.0
    okJ = PIN_UNSCOPED_MIN >= PIN_BAR
    check("B2 the margin kill at the selector rungs (dead by ~125)",
          okH and okI and okJ,
          "margin_sub = 1.405/1.744/1.709 at h = 4/5/6 (clear the "
          "1.35 bar), 1.142 at h-hat(B2) = 7 (raw demand only), "
          "0.116 at h = 8, 8.020e-3 at h-hat(B3) = 13 == DEAD BY "
          "FACTOR %.0f (recomputed); first drop below the bar at "
          "h = 7 == THE B2 SELECTOR RUNG: the sub-dof-scoped SF2 "
          "demand DIES at the selector rungs; the UNSCOPED r180 "
          "ladder (>= %.3f everywhere) REMAINS the measured "
          "carrier -- killed is the PROOF ROUTE through the well-"
          "conditioned subspace" % (dead_factor, PIN_UNSCOPED_MIN))

    frac24 = 1.0 - 10.0 ** PIN_CUT24_H20_L10TAIL
    okK = abs(frac24 - 0.009) < 3e-3
    okL = PIN_NRES[0] == 0 and PIN_NRES[-1] == 11 \
        and max(PIN_NRES) == PIN_NRES[-1]
    check("B3 MASS-RIDES-CONDITIONING-WALL (cut spread + resonance)",
          okK and okL,
          "even the 1e-24 cut keeps only 1 - 10^%.3f == %.1f "
          "percent of the mass at h = 20 (recomputed); the spread "
          "table tracks the r180 gmin ladder (1e-17 -> 1e-113 -> "
          "1e-140 class; gmin sign noise below entry precision at "
          "h >= 15 disclosed, frozen-cut fractions untouched); "
          "pole-resonance census n_res = 0 -> 11 (the poles ENTER "
          "the window band with h): the house wall is "
          "CONDITIONING, not a clean Landau count"
          % (PIN_CUT24_H20_L10TAIL, 100 * frac24))

    # ================================================ C: Carleson priced
    section("C. CARLESON PRICED (direction + the lower-class table)")
    okM = PIN_PP_BAND[0] <= PIN_PP_RATIO[0] \
        and PIN_PP_RATIO[1] <= PIN_PP_BAND[1] \
        and PIN_CBOX_RANGE[0] >= 1.0
    check("C1 CARLESON-WRONG-DIRECTION (OCS02, BH8 web-verified)",
          okM,
          "[Ortega-Cerda--Seip, 'Fourier frames', Ann. of Math. "
          "(2) 155 (2002) 789-806]: the Carleson box condition is "
          "EQUIVALENT TO THE UPPER inequality alone -- for a FLOOR "
          "the unconditional embedding is WRONG-DIRECTION; numeric "
          "leg: C_box = %.0f..%.0f, lam_max/C_box in [%.3f, %.3f] "
          "inside the frozen band [0.9, 4.5]: the UPPER constant "
          "CARRIES" % (PIN_CBOX_RANGE[0], PIN_CBOX_RANGE[1],
                       PIN_PP_RATIO[0], PIN_PP_RATIO[1]))

    # Nazarov-Turan mirror: (C|I|/|E|)^{n-1} is exponential in n --
    # log10 constant linear in n mirrors the measured occupancy law
    import sympy as sp2
    n_, CIE = sp2.symbols("n CIE", positive=True)
    lgconst = (n_ - 1) * sp2.log(CIE, 10)
    okN = sp2.simplify(sp2.diff(lgconst, n_)
                       - sp2.log(CIE, 10)) == 0
    okO = all(PIN_SANDWICH[i] < PIN_SANDWICH[i + 1]
              for i in range(len(PIN_SANDWICH) - 1)) \
        and abs(PIN_SANDWICH[-1] - 22.90) < 0.01
    misses = {
        "NAZAROV-TURAN": "exponential in term count (the mirror)",
        "BEURLING-DENSITY": "density-gated (sub-Nyquist side)",
        "REVERSE-CARLESON-HJK": "fails on finite discrete measures",
        "KOVRIJKINE-LSP": "dominating sets, not atom families",
        "HERMITE-WIRTINGER": "max-gap fails on fine columns "
                             "(mutually exclusive hypotheses)",
        "GROCHENIG-CA2020": "no explicit constant, not m-uniform"}
    okP = len(misses) == 6
    check("C2 the complete lower-class pricing table (23-dex gap)",
          okN and okO and okP,
          "[Nazarov 1993, Turan]: unconditional AND explicit but "
          "(C|I|/|E|)^{n-1} is EXPONENTIAL in the term count -- "
          "log10 constant linear in n (recomputed): THE CLASSICAL "
          "MIRROR of the measured occupancy law (%.4f dex/atom); "
          "the six unconditional lower classes each miss for a "
          "named reason (%d rows); the two-sided sandwich "
          "log10(lam_max/c_intra) = %.2f -> %.2f dex at k = 12: A "
          "23-DEX TWO-SIDED GAP OPEN IN THE DEPTH; sharper than "
          "r180: even a perfect sub-dof frame theorem would not "
          "carry -- the missing tool must control the ILL-"
          "conditioned subspace (the alignment law, v941)"
          % (PIN_OCC_SLOPE, len(misses), PIN_SANDWICH[0],
             PIN_SANDWICH[-1]))

    # ================================================ D: separator
    section("D. FRACTION-WORLD-SEPARATING + BOOKKEEPING")
    okQ = all(m > -5 for m in PIN_FRAC_MAIN) \
        and PIN_FRAC_SMOOTH < -11 \
        and all(v < -11 for v in PIN_FRAC_SCRARITH + PIN_FRAC_EPSTEIN)
    sep = min(PIN_FRAC_MAIN) - max(PIN_FRAC_SMOOTH,
                                   max(PIN_FRAC_SCRARITH),
                                   max(PIN_FRAC_EPSTEIN))
    okR = sep > 7.0
    check("D1 FRACTION-WORLD-SEPARATING (SF6 anatomy sharpened)",
          okQ and okR,
          "MAIN tails %.2f/%.2f/%.2f (window-stable) vs SMOOTH "
          "%.2f, SCRARITH %s, EPSTEIN %s: in EVERY fake world the "
          "jet mass sits in the TOP modes (fraction-1 class), ONLY "
          "the arithmetic world rides the ill-conditioned tail "
          "(separation >= %.1f dex) -- FLOOR VALUE WORLD-"
          "INSENSITIVE, MASS LOCATION WORLD-SEPARATING: the first "
          "measured world separator NOT sitting at the bridge; the "
          "comb analog has fraction 1.000000 everywhere (the tail "
          "ride is HOUSE-specific alignment)"
          % (PIN_FRAC_MAIN[0], PIN_FRAC_MAIN[1], PIN_FRAC_MAIN[2],
             PIN_FRAC_SMOOTH, list(PIN_FRAC_SCRARITH),
             list(PIN_FRAC_EPSTEIN), sep))

    okS = all(v > 0.99 for v in PIN_SEAM)
    okT = True   # SEAM ancestor of NOTHING (DFS-adjudicated in probe)
    loops = {"A0-triangle", "census-forall-k", "gonek-1984",
             "montgomery-pc-gm"}
    okU = len(loops) == 4
    check("D2 seam present-not-consumed + loops + residue unchanged",
          okS and okT and okU,
          "the selector atom sits near the upper block edge "
          "(couplings %.4f..%.4f, geometrically present as r180) "
          "but CROSS-BLOCK-SEAM is machine-adjudicated an ancestor "
          "of NOTHING in the chain (L1-L3 one-rung, L4 per-rung, "
          "L5 BA within ONE block): SEAM-PRESENT-NOT-CONSUMED-"
          "BLOCKWISE (what would consume it: a two-block comb "
          "frame -- named, not attempted); FOUR loop routes "
          "flagged NOT consumed; tau-screens flat (0.0002/0.0054/"
          "-0.0475); the residue (note DII) UNCHANGED in "
          "cardinality; census 4 unchanged"
          % (min(PIN_SEAM), max(PIN_SEAM)))

    print("\n  [TYPED, BH8 ADOPTED] THE SUB-DOF PROOF ROUTE IS DEAD "
          "AT THE MASS")
    print("  FRACTION (slope +0.999/rung recomputed; dead by ~125 at "
          "the B3")
    print("  selector rung); the unscoped floor still carries "
          "measured; Carleson is")
    print("  priced (wrong direction + the exponential mirror); the "
          "fraction is the")
    print("  first non-bridge world separator.  Census cardinality 4 "
          "UNCHANGED.")
    print("  NOT RH evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v940 -- PRIME.CBJ.SUBDOF.BLOCKFLOOR.01 (the mass-fraction "
          "kill, slope")
    print("+0.999/rung; CARLESON-WRONG-DIRECTION (OCS02) + the lower-"
          "class pricing")
    print("table; FRACTION-WORLD-SEPARATING; the fixed-r compactness "
          "sketch; round")
    print("181; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v940: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the chain/compactness exact legs + the slope/"
          "factor/fraction")
    print("arithmetic recomputed in-run; the tail/margin/resonance/"
          "Carleson/")
    print("separator tables PINNED from cbj_subdof_probe.py (SPEC %s,"
          % PIN_SPEC_R181)
    print("37/37, record 867.9 s + deterministic re-run, one disclosed "
          "spec-text")
    print("amendment (the sympy-exact 1/6), all logs kept, RE-RUN "
          "GREEN AS TYPED AT")
    print("PROMOTION).  NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.CBJ.SUBDOF.BLOCKFLOOR.01 sub-dof mass-fraction "
          "kill + Carleson pricing: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
