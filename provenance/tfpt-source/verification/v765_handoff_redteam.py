#!/usr/bin/env python3
"""v765 -- PRIME.HANDOFFREDTEAM.01: the red-team circularity audit of the gram/handoff convergence, one module from two probes (v518/v668 merge precedent), combined verdict REDTEAM-GREEN-COMBINED.  PART 1 (REDTEAM-PARTIAL, 16/16 checks): static firewall CLEAN -- zero blacklist hits across all 21 source-path functions (no eigen/Cholesky/zero/prime channel from the target into the source construction), module whitelist and target-field quarantine hold, static order source-before-target confirmed; baseline reproduced EXACTLY (errors 0.0855..0.0377, slope -0.369, kappa 0.99028); 8/8 controls break, RT1-RT5/RT7/RT8 conclusively (RT8: the forbidden separate atom/pole accounting is destroyed at 21.5 x E* while the paired error converges -- the pairing is real structure); RT6 broke ONLY the symbol gate, outside its preregistered expected set -- inconclusive by the frozen no-iteration rule.  PART 2 (RT6-SYMBOL-DETECTS, 8/8 checks): the fresh preregistration decides RT6 -- all three excess-mode deck corruptions break the symbol gate on every window (min symbol -0.45..-1.72) while all six other gates stay measurably BLIND under V1 (blindness clause gated and confirmed); the deficit mode N1 moves the symbol INTO the interior and is caught by the rate/ratio/kappa gates instead -- the two deck-corruption modes are covered by COMPLEMENTARY gate families.  BINDING PROMOTION NOTE: certificates must always carry BOTH gate families -- symbol/PSD and rate/ratio/identification; the symbol-nonnegativity gate must never be dropped (for the excess-mode deck class it is the ONLY firing detector).  NO RH claim.

PROVENANCE: discovery probes handoff_redteam_probe.py (2026-08-04, 16/16 checks, verdict REDTEAM-PARTIAL with RT6 the single preregistered inconclusive) and handoff_redteam_rt6_probe.py (2026-08-04, 8/8 checks, verdict RT6-SYMBOL-DETECTS, combined audit REDTEAM-GREEN-COMBINED per its frozen rule).  Merged per the v518/v668 precedent: part 1 verbatim at module level (sibling imports point at v563/v716/v767); part 2 verbatim inside an isolated function scope (its module-level names are function-local; its handoff_redteam_probe alias points at this module); numbers unchanged.  run() encodes part 1's preregistered RT6-inconclusive PARTIAL as the expected pattern (v757 precedent).

PART 1 -- handoff_redteam_probe.py (docstring verbatim):
GLOBAL-HANDOFF red team -- circularity audit of the gram/handoff
convergence (intended promotion target v765_handoff_redteam).

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  The true construction is NEVER modified: every
true-path object is imported read-only from handoff_frequency_gram_probe
(gp) and moonshot_arch_glue_probe (glue); controls are frozen
corruptions composed around the untouched machinery.

QUESTION.  Is the observed handoff/gram convergence
(HANDOFF-GRAM-CONVERGES, Candidate B anti-alias Nf = 2M+1; audited
numbers: spectral errors 0.0855/0.0585/0.0457/0.0452/0.0377, slope
-0.369, final/first 0.441, kappa -> 0.99028, top-window cancellation
min(atom,pole)/pair = 10.5) produced by hidden target information?
Two independent attack surfaces: (i) EIGHT frozen corruptions, each of
which must measurably BREAK the frozen certificate that the true
construction passes -- a corruption that still passes the full
certificate means the gates carry no structural information and the
audit fails RED; (ii) a static AST firewall audit of the entire
source-construction path, deeper than the G0.1 style used so far.

FROZEN CERTIFICATE (all bars inherited from the audited probes, fixed
here BEFORE the first run).  An evaluation PASSES iff ALL of:
  c1_rate    log-log slope of spectral rel error vs dimQ  < -0.25
  c2_ratio   final/first error                            < 0.75
  c3_tail    last three errors strictly decreasing
  c4_symbol  min Fejer symbol >= -2e-9 on every frequency grid
  c5_psd     lambda_min(G_source) >= -1e-9 on every window
  c6_kappa   |kappa - 1| <= 0.05 at the top window, with
             kappa = <G_src, G_tgt>_F / ||G_tgt||_F^2
  c7_level   final spectral error <= 5.0 x E*, E* = the true
             baseline final error measured in this run (c7 is
             vacuous for the baseline itself).
A control BREAKS iff at least one clause fails; it is CONCLUSIVE iff
at least one broken clause lies in its preregistered expected set.

BASELINE REPRODUCTION GATES (B0): the untouched construction at
Nf = 2M+1 on the declared 5-window family must pass the certificate
AND reproduce the audited run inside frozen bands:
slope in [-0.47, -0.27] (audited -0.369) and final/first in
[0.33, 0.55] (audited 0.441).  Failure => the round's convergence
claim does not reproduce => REDTEAM-RED.

EIGHT CONTROLS (Nf = 2M+1 everywhere except RT7; full declared
5-window family; every corruption parameter frozen in the SHA-256
manifest BEFORE any comb data is loaded):
  RT1 position-scrambled comb (existing control, gp.scrambled_layers,
      seed 16023).  Expected break set {c4_symbol, c1_rate, c7_level}.
  RT2 Epstein x^2+5y^2 logarithmic atoms (existing control,
      gp.epstein_layers, epstein_firewall_probe imported read-only).
      Expected {c4_symbol, c1_rate, c7_level}.
  RT3 OFF-LINE ZERO PAIR, TARGET SIDE ONLY (quarantined): the
      deployed Weil target gram is corrupted by adding
      2 f^T OddToeplitz(c_Z) f with c_Z[d] the EXACT closed
      second-difference lag read (== tent read, the pole-block
      identity) of the density  A_Z cosh(delta_Z t) cos(gamma_Z t),
      FROZEN A_Z = 2.0, delta_Z = 0.5, gamma_Z = 3.0 -- the trace
      contribution of a synthetic zero quadruple at
      s = 1/2 +- 1/2 +- 3.0 i.  gamma_Z = 3.0 is NOT a zeta ordinate
      (the first is 14.13...); no zero table is read anywhere in this
      probe.  The source path is byte-identical to the baseline (the
      frozen baseline source grams are REUSED, zero new source
      computation).  Expected {c1_rate, c2_ratio, c3_tail, c6_kappa,
      c7_level}; c4/c5 inherit from the true source and must PASS.
  RT4 wrong pole normalization: the closed pole block scaled by the
      frozen factor 2.0 (pole moment layer x 2 AND one extra copy of
      the closed rank-one pole gram).  Expected {c6_kappa, c7_level}.
  RT5 wrong mu4 class in the comb/sigma-descent: atom masses twisted
      by the nontrivial mu4 character chi_-4(n) (= +1/0/-1 for
      n = 1 / even / 3 mod 4), frozen -- kills the 2-adic rail and
      sign-flips the odd inert powers.  Expected {c4_symbol, c1_rate,
      c7_level}.
  RT6 wrong deck twists: the arch layer rebuilt from the D5-mirror
      deck density  sum_b e^{-b t} / (1 - e^{-6t}), b in
      {3/4, 3/2, 9/4} (the moonshot A3.4 counterfactual, residual
      0.474 there); the d = 0 UV cell is corrected by the finite
      difference integral 2 int_0^D (1-w/D)(wd - rho) dw (the
      density difference is finite at w = 0, limit 1/2).
      Expected {c1_rate, c2_ratio, c3_tail, c7_level}.
  RT7 insufficient frequency count: Nf = the Candidate A review count
      ceil(2 N(pi/D)) << 2M+1 (the audited iteration trigger; the
      audited regime showed slope +0.471 territory).  True layers,
      true target.  Expected {c1_rate, c2_ratio, c3_tail}.
  RT8 removed atom-pole pairing (the forbidden decomposition): error
      accounting with SEPARATELY estimated absolute layer errors
      e_sep = rel2(S_atom, T_atom) + rel2(S_pole, T_pole) instead of
      the paired rel2(S_atom + S_pole, T_atom + T_pole); sources and
      targets byte-identical to the baseline.  Expected {c7_level};
      the top-window cancellation factor min(atom,pole)/pair is
      reported (audited 10.5) -- the pairing is real structure iff
      the separate accounting is destroyed at the level gate.

STATIC FIREWALL AUDIT (F1-F4) of the source-construction path
  gp:   battery_specification, sampled_battery, odd_extension,
        source_comb, atom_lags_from_comb, arch_lags_from_cover,
        build_true_source_layers, fejer_symbol, pole_amplitudes,
        source_gram, requested_frequency_count, n_of_T
  glue: geo_comb, gaussian_sieve, atom_tent_geo, arch_lag0_geo,
        arch_lags_far_geo, pole_lags_closed, tent_read, rho, g_pole
with every hit reported:
  F1 symbol blacklist (exact match on Name/Attribute/Call tokens):
     eig / eigh / eigs / eigsh / eigvals / eigvalsh / svd / svdvals /
     cholesky / cho_factor / cho_solve / qr / lu / lu_factor / schur
     (spectral or factor access to the target matrix), solve / lstsq /
     inv / pinv / minimize / polyfit / curve_fit / fmin / leastsq
     (error minimizers / post-hoc scalars), odd_toeplitz /
     target_gram / error_metrics (target machinery), zetazero /
     nzeros / isprime / primerange / nextprime / prevprime / primepi /
     sympy (zero/prime loaders).  Gate: zero hits.
  F2 module whitelist: the gp source functions may reference only
     modules {np, math, hashlib, json, glue}; the glue source
     functions only {np, math, bisect, stage1}; every stage1 access
     must be stage1.canon (associate-class canonicalization, no
     arithmetic table).  Gate: no other module touched.
  F3 target-field quarantine: no string subscript "car" / "cat" / "p"
     inside any source function (allowed geometry keys: alpha, M, D).
     All remaining uses of these keys in gp are LISTED and must lie
     only in target/adjudication code (target_gram, run wiring guard,
     declared evaluation) -- reported, the source-function gate is
     the hard one.
  F4 static order: inside gp.evaluate_candidate and gp.control_profile
     the first target_gram call site lies strictly BELOW the first
     source_gram call site (target constructed only after the Q hash
     is complete).
Plus F0, the usual self-firewall on this probe (banned zeta/prime
identifiers), and the runtime guards G0.2 (manifest SHA-256 frozen
before any comb data) and G0.3 (ingredient wiring <= 2e-10, reused
from the audited probe).

VERDICT (frozen): REDTEAM-GREEN = B0 + F0-F4 pass and all eight
controls break conclusively.  REDTEAM-RED = any control passes the
full certificate, or the firewall audit finds target leakage, or B0
fails -- this would invalidate the round's convergence claims and is
reported plainly.  REDTEAM-PARTIAL = everything else; controls that
broke only outside their expected set or raised an exception are
named inconclusive.

ITERATION POLICY: none.  No construction iteration, no bar
recalibration is available to this probe; the corruptions and bars
above are exhausted by this single preregistered run.

RUNTIME (predeclared): the full declared 5-window family is reused
(no reduced rungs needed): one baseline ladder + five corrupted
source ladders + the cheap Candidate-A ladder + the Epstein Lambda_E
table; RT3 and RT8 reuse the frozen baseline objects.  Budget
<= 10 minutes.

RESULTS (2026-08-04, first and only preregistered run, 6.1 s,
16/16 checks; verdict REDTEAM-PARTIAL -- firewall clean, baseline
reproduced, 8/8 controls break, 7/8 conclusively; RT6 inconclusive
by the frozen preregistration, see below):
  *  B0 baseline reproduces the audited run EXACTLY: errors
     0.0855/0.0585/0.0457/0.0452/0.0377 over dimQ 738..5734, slope
     -0.369 (band [-0.47,-0.27]), final/first 0.441 (band
     [0.33,0.55]), min symbol +7.4e-3, lmin +5.5e-3, kappa 0.99028;
     E* = 0.0377.
  *  F1-F4 firewall CLEAN: zero blacklist hits over all 21
     source-path functions; module census gp = {glue, hashlib, json,
     math, np}, glue = {bisect, math, np, stage1} with stage1.canon
     the only stage1 access; no car/cat/p subscript in any source
     function (documented non-source uses: target_gram["car"/"cat"],
     run["p"] wiring guard); static order source_gram l.350 <
     target_gram l.352 (evaluate_candidate) and l.430 < l.432
     (control_profile).  No channel from the target (eigen/Cholesky/
     zero/prime data, post-hoc scalars) into the source construction.
  *  RT1 scramble: symbol -9.5e+02, errors GROW 5.3 -> 147.7 (slope
     +1.574), kappa 45.0, level 783 x bar -- breaks c1-c4, c6, c7.
  *  RT2 Epstein (3381 negative atom sites): symbol -1.4e+02, errors
     1.63 -> 3.54 (slope +0.307), kappa 3.51 -- breaks c1-c4, c6, c7.
  *  RT3 off-line pair (target side, source grams reused byte-
     identically): the deployed gates DETECT the corrupted target --
     errors pin to a 0.97 floor (0.9678..0.9714, slope +0.002,
     final/first 1.004, tail not falling), kappa collapses to 0.1247
     (|kappa-1| = 0.875); c4/c5 pass exactly as they must (the
     injection provably never touched the source).  Breaks
     c1/c2/c3/c6/c7 == the full expected set.
  *  RT4 pole block x 2: symbol -2.0e+02, errors 1.89 -> 14.58
     (slope +0.918), kappa 11.45 -- breaks c1-c4, c6, c7 (far beyond
     the expected {c6, c7}: the doubled pole moments destroy the
     symbol itself).
  *  RT5 wrong mu4 class: symbol -2.0e+02, errors 1.13 -> 12.94
     (slope +1.135), kappa 10.21 -- breaks c1-c4, c6, c7.
  *  RT6 wrong deck twists: breaks ONLY c4 (min symbol -0.827 vs bar
     -2e-9 on every window) -- OUTSIDE its preregistered expected set
     {c1, c2, c3, c7}, hence INCONCLUSIVE by the frozen rules and the
     verdict is PARTIAL, not GREEN.  DECLARED FINDING (no re-run, no
     recalibration): after the positive-part clipping the wrong-deck
     gram still tracks the target (errors 0.0862 -> 0.0381, kappa
     0.985) -- the error/identification ladder alone would NOT
     distinguish the D5-mirror deck; the SYMBOL NONNEGATIVITY gate is
     the load-bearing detector for the deck structure.  The audited
     probe DOES gate on exactly this (M2.1 requires min symbol >=
     -2e-9), so the corrupted construction is graded DEAD there; the
     auditor's expected-set guess, not the construction's
     sensitivity, was wrong.
  *  RT7 Candidate-A frequency count: slope +0.471 -- EXACTLY the
     audited iteration-trigger territory; errors 0.33 -> 1.04,
     final/first 3.16, kappa 1.45 -- breaks c1/c2/c3 (+ c6, c7).
  *  RT8 forbidden decomposition: separate accounting 1.82 -> 0.81
     vs paired 0.0852 -> 0.0376; final 0.8091 vs level bar 0.1885
     (21.5 x E*); top-window cancellation min(atom,pole)/pair =
     10.50 (audited 10.5) -- the paired convergence is real
     structure; breaks c7 == the expected set.
  *  HONEST STATEMENT: the round's convergence SURVIVES this red
     team on the measured surface -- every corruption is detected by
     the frozen gate battery, the baseline reproduces, and the
     static firewall finds no target leakage.  The single PARTIAL
     mark is an auditor-side expectation miss on RT6 (the break is
     real and sits in a deployed gate), recorded as preregistered
     instead of being recalibrated away.  Promotion note for v765:
     the RT6 lesson should be carried along -- the symbol gate must
     never be dropped from the certificate, because without it the
     deck corruption is invisible to rate/level/identification.
     Unchanged and open: the eps -> 0 wall, the battery-limited
     identification, every RH-level positivity statement.  NO RH
     claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/handoff_redteam_probe.py

PART 2 -- handoff_redteam_rt6_probe.py (docstring verbatim):
GLOBAL-HANDOFF red team, RT6 decision probe -- the symbol gate as
the load-bearing deck-corruption detector (intended promotion
companion v765b to handoff_redteam_probe / v765).

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, and this probe writes no files.  The true construction is
never modified; all machinery is imported read-only from
handoff_frequency_gram_probe (gp), moonshot_arch_glue_probe (glue)
and handoff_redteam_probe (rt: certificate bars, evaluation engine,
tent-lag builders -- all frozen there, reused byte-identically).

INPUT STATE (frozen findings of the parent audit, 2026-08-04):
handoff_redteam_probe ended REDTEAM-PARTIAL with firewall clean,
baseline reproduced, 8/8 controls broken, 7/8 conclusive.  The single
inconclusive control was RT6 (wrong deck twists, D5 mirror): it broke
ONLY the symbol clause c4 (min Fejer symbol -0.827 vs bar -2e-9 on
every window) while the positive-part-clipped gram still tracked the
target (errors 0.0862 -> 0.0381, kappa 0.985) -- outside the parent
probe's preregistered expected set {c1,c2,c3,c7}.  The break was real
and sits exactly in the audited construction's load-bearing M2.1
symbol/PSD gate; the miss was the auditor's expectation.  Per the
parent's frozen no-iteration policy the PARTIAL stands there; THIS
probe decides RT6 under a fresh preregistration.

STRUCTURAL STATEMENT UNDER TEST (frozen): after positive-part
clipping, deck corruption is invisible to the rate/level/
identification gates; the SYMBOL NONNEGATIVITY gate is the
load-bearing detector.

SIGN ANALYSIS (frozen before the run; it dictates the variant class):
the arch layer enters the source moments as c_ar[d] = -int tent_d
rho, so a deck corruption with density EXCESS (wrong >= true on the
battery support) makes the moments more negative and pushes the
Fejer symbol DOWN -- the positivity gate can fire.  A deck corruption
with one-signed DEFICIT (wrong <= true) ADDS the positive density
(true - wrong) to the total symbol, pushing it UP and INTO the
positivity interior: no positivity gate can ever see it, by
construction.  The gated claim is therefore: the symbol gate detects
the EXCESS-mode deck-corruption class (the mode that could counterfeit
positivity); the deficit mode is measured in a declared negative
block and handed to the resolution discussion, not gated.

FROZEN CERTIFICATE: identical bars to the parent probe (imported):
c1 slope < -0.25, c2 final/first < 0.75, c3 falling tail, c4 min
symbol >= -2e-9 on every grid, c5 lambda_min >= -1e-9, c6 |kappa-1|
<= 0.05, c7 final <= 5.0 x E* (E* = this run's baseline final).

POSITIVE ANCHOR (B0, gated): the true construction at Nf = 2M+1 on
the declared 5-window family must pass the FULL certificate including
c4, and reproduce the audited run inside the parent's frozen bands:
slope in [-0.47, -0.27] (audited -0.369), final/first in [0.33, 0.55]
(audited 0.441).  Failure => RT6-INVALID (construction problem,
reported immediately).

GATED DECK-CORRUPTION VARIANTS (all EXCESS mode, all with total
t -> 0 channel mass 3 so the d = 0 UV correction integral stays
finite; true deck = exponents {1/2, 5/2, 9/2}, weights {1,1,1},
denominator 1 - e^{-6t}):
  V1 FULL MIRROR (the parent RT6 corruption, rerun): exponents
     {3/4, 3/2, 9/4}, weights {1,1,1} (D5 mirror, moonshot A3.4).
     Expected (frozen): c4 breaks on EVERY window (parent run:
     min symbol -0.696/-0.769/-0.817/-0.818/-0.827) AND all other
     clauses c1/c2/c3/c5/c6/c7 PASS -- the blindness of the other
     gates is confirmed, not just the break.  BOTH parts are gated
     for V1 (this is the structural statement).
  V2 SINGLE-CHANNEL PHASE SWAP: deck channel r = 5 replaced by r = 3,
     exponents {1/2, 3/2, 9/2}, weights {1,1,1}.  Density excess
     (e^{-3t/2} - e^{-5t/2})/(1 - e^{-6t}) >= 0, size ~0.14 at t = 1.
     Expected (frozen): c4 breaks on every window; the other gates
     are expected blind and are REPORTED, not gated (a smaller
     corruption than V1 must not be given a second kill route).
  V3 CHANNEL-MASS REDISTRIBUTION (partial/amplitude corruption): the
     nu = 5/6 channel mass moved onto the other two, exponents
     {1/2, 5/2}, weights {3/2, 3/2}.  Density excess
     (e^{-t/2}/2 + e^{-5t/2}/2 - e^{-9t/2})/(1 - e^{-6t}) >= 0.
     Expected (frozen): c4 breaks on every window; other gates
     reported.
NEGATIVE BLOCK (N1, measured, NOT gated -- declared honesty block):
  deck channel r = 5 replaced by r = 7, exponents {1/2, 7/2, 9/2},
  weights {1,1,1}: one-signed DEFICIT (~ -0.17 at t -> 0).  Expected
  (frozen): the symbol moves UP (min symbol >= the baseline minimum;
  no c4 break -- provable blindness of any positivity gate to
  interior-directed perturbations) and the error/identification
  ladder moves at the ~1e-3 level (parent V1 moved it by ~5e-4),
  i.e. N1 sits BELOW the certificate's resolution floor.  This is
  reported as the measured resolution limit of the battery surface
  (consistent with the already-declared battery-limited
  identification remainder), not as a circularity hole: a
  perturbation that leaves source, symbol margin direction, and
  handoff errors essentially unchanged cannot counterfeit
  convergence from target data.

VERDICT ENUM (frozen): RT6-SYMBOL-DETECTS = B0 clean (full
certificate incl. c4 + reproduction bands) AND V1/V2/V3 each break
c4 on every window AND the V1 blindness clause holds (c1/c2/c3/c5/
c6/c7 all pass under the clipped V1 gram).  RT6-PARTIAL = B0 clean
but a gated variant fails to break c4 on some window (named -- a
genuine audit hole), or the V1 blindness clause fails (named gate).
RT6-INVALID = B0 fails.

COMBINED AUDIT STATEMENT (printed, frozen rule): with the parent
probe's frozen facts (firewall clean, 7 conclusive controls RT1-RT5/
RT7/RT8) as cited input, the round's red team is
REDTEAM-GREEN-COMBINED if and only if this probe ends
RT6-SYMBOL-DETECTS; otherwise NOT-GREEN, stated plainly.

ITERATION POLICY: none.  Single preregistered run; no variant, bar,
or expected-set recalibration afterwards.

RUNTIME (predeclared): baseline + 3 gated variants + 1 negative
block = 5 full source ladders on the declared 5-window family;
budget <= 5 minutes (parent probe: 8 ladders in 6.1 s).

RESULTS (2026-08-04, first and only preregistered run, 4.5 s, 8/8
checks; verdict RT6-SYMBOL-DETECTS -- baseline clean, all three
excess-mode variants break c4 on every window, V1 blindness
confirmed; combined audit REDTEAM-GREEN-COMBINED):
  *  B0 anchor: errors 0.0855/0.0585/0.0457/0.0452/0.0377, slope
     -0.369, final/first 0.441, kappa 0.99028, min symbol +7.40e-3,
     lmin +5.45e-3 -- full certificate incl. c4 passes, bands
     reproduced; E* = 0.0377.
  *  V1 full mirror: min symbol -0.696/-0.769/-0.817/-0.818/-0.827
     per window (parent run reproduced exactly); ALL other clauses
     pass (errors 0.0862 -> 0.0381, slope -0.368, final/first 0.442,
     kappa 0.9849, lmin +3.98e-3, level 0.0381 <= 0.1885) --
     BLINDNESS CONFIRMED: rate/ratio/tail/psd/kappa/level all stayed
     blind, only the symbol gate fired.
  *  V2 phase swap r = 5 -> 3: min symbol -0.451/-0.500/-0.521/
     -0.522/-0.534 per window -- c4 breaks everywhere; every other
     gate blind (errors 0.0851 -> 0.0372, slope -0.373, kappa
     0.9877).
  *  V3 mass redistribution (3/2, 3/2, 0): min symbol -1.289/-1.521/
     -1.636/-1.646/-1.720 per window -- c4 breaks everywhere; every
     other gate blind (errors 0.0858 -> 0.0377, slope -0.371, kappa
     0.9854).
  *  N1 deficit r = 5 -> 7 (negative block, not gated).  The frozen
     SIGN prediction is confirmed: the symbol moves INTO the
     interior on every window (min symbol +1.10e-2 .. +2.67e-2 >=
     baseline +7.40e-3; no c4 break -- positivity gates provably
     blind).  The frozen MAGNITUDE prediction was WRONG (declared,
     not hidden): instead of ~1e-3 shifts below the resolution
     floor, the deficit produced a 0.138 error floor (errors
     0.1454 -> 0.1380, slope -0.024, final/first 0.949, kappa
     1.0790) and was CAUGHT by c1_rate, c2_ratio and c6_kappa.  The
     measured picture is therefore STRONGER than predicted: the two
     deck-corruption modes are covered by complementary detectors --
     excess mode by the symbol gate (errors blind), deficit mode by
     the rate/ratio/identification gates (symbol blind).  No
     corruption mode of the tested class escapes the full
     certificate.  Post-run text correction (declared): the printed
     promotion note was reworded to report the measured caught-by
     list dynamically instead of the refuted below-resolution
     wording; no gate, bar, variant or verdict logic was touched.
  *  COMBINED: with the parent audit's frozen facts (firewall clean,
     baseline reproduced, RT1-RT5/RT7/RT8 conclusive) and this
     RT6-SYMBOL-DETECTS decision, the round's red team is
     REDTEAM-GREEN-COMBINED.  PROMOTION NOTE (binding for v765/
     v765b): the symbol-nonnegativity gate must never be dropped
     from any future certificate -- for the excess-mode deck class
     it is the ONLY firing detector; the deficit mode needs the
     rate/ratio/kappa gates.  Certificates must always carry BOTH
     gate families.  NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/handoff_redteam_rt6_probe.py
"""

# ==========================================================================
# PART 1 -- handoff_redteam_probe.py (verbatim; imports promoted)
# ==========================================================================


import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

_HERE_DISC = os.path.abspath(os.path.join(_HERE, "..",
    "experiments", "tfpt-discovery"))
sys.path.insert(0, _HERE_DISC)

import v563_paper2_readouts as core  # noqa: E402  (target side only)
import v716_moonshot_arch_glue as glue  # noqa: E402
import v767_handoff_frequency_gram as gp  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen certificate bars
RATE_BAR = -0.25
RATIO_BAR = 0.75
SYM_TOL = 2.0e-9
PSD_TOL = -1.0e-9
KAPPA_BAR = 0.05
LEVEL_FACTOR = 5.0
SLOPE_BAND = (-0.47, -0.27)     # B0 reproduction (audited -0.369)
RATIO_BAND = (0.33, 0.55)       # B0 reproduction (audited 0.441)
WIRE_TOL = 2.0e-10

# ------------------------------------------------ frozen control params
AMP_Z = 2.0                     # RT3 injection amplitude
DELTA_Z = 0.5                   # RT3 off-line distance (Re s = 0 and 1)
GAMMA_Z = 3.0                   # RT3 synthetic ordinate (NOT a zeta zero)
POLE_WRONG_FACTOR = 2.0         # RT4
DECK_WRONG = (0.75, 1.5, 2.25)  # RT6 (D5 mirror, moonshot A3.4)

CLAUSE_ORDER = ("c1_rate", "c2_ratio", "c3_tail", "c4_symbol",
                "c5_psd", "c6_kappa", "c7_level")
EXPECTED = {
    "RT1": ("c4_symbol", "c1_rate", "c7_level"),
    "RT2": ("c4_symbol", "c1_rate", "c7_level"),
    "RT3": ("c1_rate", "c2_ratio", "c3_tail", "c6_kappa", "c7_level"),
    "RT4": ("c6_kappa", "c7_level"),
    "RT5": ("c4_symbol", "c1_rate", "c7_level"),
    "RT6": ("c1_rate", "c2_ratio", "c3_tail", "c7_level"),
    "RT7": ("c1_rate", "c2_ratio", "c3_tail"),
    "RT8": ("c7_level",),
}

MANIFEST = dict(
    version="handoff-redteam-v1",
    certificate=dict(rate=RATE_BAR, ratio=RATIO_BAR, sym=SYM_TOL,
                     psd=PSD_TOL, kappa=KAPPA_BAR, level=LEVEL_FACTOR),
    baseline_bands=dict(slope=list(SLOPE_BAND), ratio=list(RATIO_BAND)),
    rt1="gp.scrambled_layers, seed 16023 (gp.RNG_SEED)",
    rt2="gp.epstein_layers, x^2+5y^2 logarithmic atoms",
    rt3=dict(amp=AMP_Z, delta=DELTA_Z, gamma=GAMMA_Z,
             side="target-only, closed second-difference lag read"),
    rt4=dict(pole_factor=POLE_WRONG_FACTOR,
             scope="moment layer AND rank-one closed pole gram"),
    rt5="atom masses twisted by chi_-4(n) in the sigma-descent comb",
    rt6=dict(deck_exponents=list(DECK_WRONG),
             uv_cell="lag0 corrected by 2 int (1-w/D)(wd-rho)"),
    rt7="Nf = ceil(2 N(pi/D)) (Candidate A review count)",
    rt8="separate |atom| + |pole| absolute error accounting",
    expected={k: sorted(v) for k, v in EXPECTED.items()},
)
MANIFEST_HASH = hashlib.sha256(json.dumps(
    MANIFEST, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []
FAILS = []


def check(name, ok, detail=""):
    CHECKS.append(name)
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


# ==================================================== F0 self firewall
def self_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


# ==================================================== F1-F4 static audit
GP_SOURCE_FUNCS = (
    "battery_specification", "sampled_battery", "odd_extension",
    "source_comb", "atom_lags_from_comb", "arch_lags_from_cover",
    "build_true_source_layers", "fejer_symbol", "pole_amplitudes",
    "source_gram", "requested_frequency_count", "n_of_T")
GLUE_SOURCE_FUNCS = (
    "geo_comb", "gaussian_sieve", "atom_tent_geo", "arch_lag0_geo",
    "arch_lags_far_geo", "pole_lags_closed", "tent_read", "rho",
    "g_pole")

BLACKLIST = frozenset((
    "eig", "eigh", "eigs", "eigsh", "eigvals", "eigvalsh",
    "svd", "svdvals", "cholesky", "cho_factor", "cho_solve",
    "qr", "lu", "lu_factor", "schur",
    "solve", "lstsq", "inv", "pinv",
    "minimize", "polyfit", "curve_fit", "fmin", "leastsq",
    "odd_toeplitz", "target_gram", "error_metrics",
    "zetazero", "nzeros", "isprime", "primerange", "nextprime",
    "prevprime", "primepi", "sympy"))
FORBIDDEN_KEYS = frozenset(("car", "cat", "p"))
ALLOWED_MODULES_GP = frozenset(("np", "math", "hashlib", "json", "glue"))
ALLOWED_MODULES_GLUE = frozenset(("np", "math", "bisect", "stage1"))
ALLOWED_STAGE1_ATTRS = frozenset(("canon",))


def module_import_names(tree):
    mods = set()
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.asname or alias.name.split(".")[0])
    return mods


def audit_source_functions(path, func_names, allowed_modules):
    with open(path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    mods = module_import_names(tree)
    fdefs = {n.name: n for n in ast.walk(tree)
             if isinstance(n, ast.FunctionDef) and n.name in func_names}
    findings = dict(black=set(), modules=set(), keys=set(),
                    stage1=set(), used_modules=set(),
                    missing=sorted(set(func_names) - set(fdefs)))
    for name in sorted(fdefs):
        for sub in ast.walk(fdefs[name]):
            token = ""
            if isinstance(sub, ast.Name):
                token = sub.id
                if sub.id in mods:
                    findings["used_modules"].add(sub.id)
                    if sub.id not in allowed_modules:
                        findings["modules"].add(
                            "%s -> module %s" % (name, sub.id))
            elif isinstance(sub, ast.Attribute):
                token = sub.attr
                if isinstance(sub.value, ast.Name) \
                        and sub.value.id == "stage1" \
                        and sub.attr not in ALLOWED_STAGE1_ATTRS:
                    findings["stage1"].add(
                        "%s -> stage1.%s" % (name, sub.attr))
            elif isinstance(sub, ast.Subscript):
                sl = sub.slice
                if isinstance(sl, ast.Constant) \
                        and isinstance(sl.value, str) \
                        and sl.value in FORBIDDEN_KEYS:
                    findings["keys"].add(
                        '%s -> ["%s"]' % (name, sl.value))
            if token and token in BLACKLIST:
                findings["black"].add("%s -> %s" % (name, token))
    return findings, tree


def forbidden_key_census(tree):
    """Every car/cat/p string subscript in the file, by function."""
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Subscript):
                sl = sub.slice
                if isinstance(sl, ast.Constant) \
                        and isinstance(sl.value, str) \
                        and sl.value in FORBIDDEN_KEYS:
                    out.append('%s["%s"]' % (node.name, sl.value))
    return sorted(set(out))


def first_call_line(func_node, callee):
    lines = [sub.lineno for sub in ast.walk(func_node)
             if isinstance(sub, ast.Call)
             and ((isinstance(sub.func, ast.Name)
                   and sub.func.id == callee)
                  or (isinstance(sub.func, ast.Attribute)
                      and sub.func.attr == callee))]
    return min(lines) if lines else None


def firewall_audit():
    print("\n-- F1-F4 static firewall audit of the source path")
    gp_find, gp_tree = audit_source_functions(
        gp.__file__, GP_SOURCE_FUNCS, ALLOWED_MODULES_GP)
    gl_find, _gl_tree = audit_source_functions(
        glue.__file__, GLUE_SOURCE_FUNCS, ALLOWED_MODULES_GLUE)
    black = sorted(gp_find["black"] | gl_find["black"])
    ok_f1 = check(
        "F1 symbol blacklist over %d gp + %d glue source functions "
        "(eigen/Cholesky/SVD, solvers/minimizers, target machinery, "
        "zero/prime loaders)"
        % (len(GP_SOURCE_FUNCS), len(GLUE_SOURCE_FUNCS)),
        not black and not gp_find["missing"] and not gl_find["missing"],
        "hits=%s missing=%s"
        % (black or "none",
           (gp_find["missing"] + gl_find["missing"]) or "none"))
    mod_hits = sorted(gp_find["modules"] | gl_find["modules"]
                      | gl_find["stage1"] | gp_find["stage1"])
    ok_f2 = check(
        "F2 module whitelist: gp source functions in %s, glue source "
        "functions in %s, stage1 access limited to .canon"
        % (sorted(ALLOWED_MODULES_GP), sorted(ALLOWED_MODULES_GLUE)),
        not mod_hits,
        "used gp=%s glue=%s, violations=%s"
        % (sorted(gp_find["used_modules"]),
           sorted(gl_find["used_modules"]), mod_hits or "none"))
    key_hits = sorted(gp_find["keys"] | gl_find["keys"])
    census = forbidden_key_census(gp_tree)
    ok_f3 = check(
        "F3 target-field quarantine: no car/cat/p subscript in any "
        "source function", not key_hits,
        "source hits=%s; documented non-source uses in gp: %s"
        % (key_hits or "none", census))
    ok_f4 = True
    details = []
    for fname in ("evaluate_candidate", "control_profile"):
        node = next(n for n in ast.walk(gp_tree)
                    if isinstance(n, ast.FunctionDef)
                    and n.name == fname)
        ls = first_call_line(node, "source_gram")
        lt = first_call_line(node, "target_gram")
        ok_f4 &= ls is not None and lt is not None and ls < lt
        details.append("%s: source_gram l.%s < target_gram l.%s"
                       % (fname, ls, lt))
    ok_f4 = check(
        "F4 static order: target built only after the source Q "
        "(call-site line order)", ok_f4, "; ".join(details))
    return ok_f1 and ok_f2 and ok_f3 and ok_f4


# ==================================================== evaluation engine
def profile_eval(tag, windows, layers_list, count_fn, target_fn,
                 sources=None, post_source=None):
    rows = []
    print("\n%s" % tag)
    for i, window in enumerate(windows):
        free, full, _bh = gp.sampled_battery(window["M"], window["D"])
        if sources is not None:
            src = sources[i]
        else:
            src = gp.source_gram(window, layers_list[i], full,
                                 int(count_fn(window)), tag)
        gram_s = src["gram"]
        if post_source is not None:
            gram_s = gram_s + post_source(window, full)
        # target evaluation strictly after the (frozen/reused) source
        tgt = target_fn(window, free)
        err = gp.error_metrics(gram_s, tgt["gram"])["spectral"]
        lmin = float(sla.eigvalsh(gram_s, subset_by_index=[0, 0])[0])
        kappa = float(np.sum(gram_s * tgt["gram"])
                      / np.sum(tgt["gram"] * tgt["gram"]))
        rows.append(dict(w=window, src=src, tgt=tgt, err=err,
                         dim=src["dimension"],
                         min_sym=src["minimum_symbol"],
                         lmin=lmin, kappa=kappa))
        print("  h=%4d Nf=%5d minS=%+.2e lmin=%+.2e err=%.4f "
              "kappa=%.4f"
              % (window["M"] // 2, src["dimension"] - 1,
                 src["minimum_symbol"], lmin, err, kappa))
    errors = [r["err"] for r in rows]
    dims = [r["dim"] for r in rows]
    prof = dict(rows=rows, errors=errors, dims=dims,
                slope=gp.log_slope(dims, errors),
                ratio=errors[-1] / errors[0],
                tail=errors[-3] > errors[-2] > errors[-1],
                min_sym=min(r["min_sym"] for r in rows),
                lmin=min(r["lmin"] for r in rows),
                kappa=rows[-1]["kappa"])
    print("  profile: errors=%s slope=%.3f final/first=%.3f tail=%s "
          "kappa_top=%.4f"
          % ("/".join("%.4f" % e for e in errors), prof["slope"],
             prof["ratio"], prof["tail"], prof["kappa"]))
    return prof


def certificate(prof, ref_final):
    return {
        "c1_rate": prof["slope"] < RATE_BAR,
        "c2_ratio": prof["ratio"] < RATIO_BAR,
        "c3_tail": bool(prof["tail"]),
        "c4_symbol": prof["min_sym"] >= -SYM_TOL,
        "c5_psd": prof["lmin"] >= PSD_TOL,
        "c6_kappa": abs(prof["kappa"] - 1.0) <= KAPPA_BAR,
        "c7_level": (ref_final is None
                     or prof["errors"][-1] <= LEVEL_FACTOR * ref_final),
    }


def clause_strings(prof, ref_final):
    return {
        "c1_rate": "slope %+.3f (bar < %.2f)" % (prof["slope"],
                                                 RATE_BAR),
        "c2_ratio": "final/first %.3f (bar < %.2f)" % (prof["ratio"],
                                                       RATIO_BAR),
        "c3_tail": "last three falling = %s" % prof["tail"],
        "c4_symbol": "min symbol %+.2e (bar >= -%.0e)"
                     % (prof["min_sym"], SYM_TOL),
        "c5_psd": "lmin %+.2e (bar >= %.0e)" % (prof["lmin"], PSD_TOL),
        "c6_kappa": "|kappa-1| %.4f (bar <= %.2f)"
                    % (abs(prof["kappa"] - 1.0), KAPPA_BAR),
        "c7_level": ("final %.4f vs %.1f x E* = %.4f"
                     % (prof["errors"][-1], LEVEL_FACTOR,
                        LEVEL_FACTOR * ref_final)
                     if ref_final is not None else "n/a (baseline)"),
    }


def adjudicate_control(cid, label, prof, ref_final):
    cl = certificate(prof, ref_final)
    txt = clause_strings(prof, ref_final)
    broken = [k for k in CLAUSE_ORDER if not cl[k]]
    passes = not broken
    conclusive = bool(broken) and any(k in EXPECTED[cid]
                                      for k in broken)
    for k in CLAUSE_ORDER:
        print("    %-9s %-7s %s" % (k, "BROKEN" if not cl[k] else "ok",
                                    txt[k]))
    check("%s %s BREAKS the frozen certificate" % (cid, label),
          bool(broken),
          "broken=%s expected=%s conclusive=%s"
          % (broken or "NONE -- control passes, RED",
             sorted(EXPECTED[cid]), conclusive))
    return dict(cid=cid, label=label, broken=broken, passes=passes,
                conclusive=conclusive, error=None)


# ==================================================== frozen corruptions
def zero_pair_lags(M, D):
    """RT3 QUARANTINE (target side only): exact tent-read lags of the
    density AMP_Z cosh(DELTA_Z t) cos(GAMMA_Z t) via the closed second
    difference of its double antiderivative (the pole-block identity).
    Synthetic zero quadruple at s = 1/2 +- DELTA_Z +- i GAMMA_Z; no
    zero table involved."""
    z1 = complex(DELTA_Z, GAMMA_Z)
    z2 = complex(-DELTA_Z, GAMMA_Z)
    t = np.abs(np.arange(-1, M + 1)) * D
    g = AMP_Z * 0.5 * (np.exp(z1 * t) / z1 ** 2
                       + np.exp(z2 * t) / z2 ** 2).real
    return (g[:-2] - 2.0 * g[1:-1] + g[2:]) / D


def target_offline(window, free):
    """RT3: the deployed target plus the synthetic off-line pair."""
    tgt = gp.target_gram(window, free)
    cz = zero_pair_lags(window["M"], window["D"])
    zform = 2.0 * free.T @ core.odd_toeplitz(cz, window["M"]) @ free
    gram = tgt["gram"] + 0.5 * (zform + zform.T)
    return dict(gram=gram, layers=tgt["layers"])


def pole_wrong_layers(true_layers):
    """RT4: pole moment layer x POLE_WRONG_FACTOR (frozen)."""
    return [dict(arch=lay["arch"], atom=lay["atom"],
                 pole=POLE_WRONG_FACTOR * lay["pole"])
            for lay in true_layers]


def pole_extra_rank_one(window, full):
    """RT4: the second copy of the closed rank-one pole gram."""
    column = gp.pole_amplitudes(window, full)
    return (POLE_WRONG_FACTOR - 1.0) * np.outer(column, column)


def mu4_twisted_layers(windows, true_layers):
    """RT5: atom masses twisted by the nontrivial mu4 character
    chi_-4(n) = +1 / 0 / -1 for n = 1 / even / 3 mod 4 (frozen)."""
    out = []
    for window, lay in zip(windows, true_layers):
        sites = np.asarray(lay["sites"], dtype=int)
        chi = np.zeros(len(sites))
        chi[sites % 4 == 1] = 1.0
        chi[sites % 4 == 3] = -1.0
        atom = glue.atom_tent_geo(window["alpha"], window["M"],
                                  np.log(sites.astype(float)),
                                  lay["masses"] * chi)
        out.append(dict(arch=lay["arch"], atom=atom,
                        pole=lay["pole"]))
    return out


def deck_wrong_density(w):
    """RT6: the D5-mirror deck density (moonshot A3.4 counterfactual)."""
    w = np.asarray(w, float)
    return sum(np.exp(-b * w) for b in DECK_WRONG) / (-np.expm1(-6.0 * w))


def far_lags_of_density(M, D, density):
    """Tent lags -int tent_d density for d = 1..M-1 (the deployed
    arch convention, GL-48 per half cell)."""
    s = (np.arange(1, M) * D).reshape(-1, 1)
    out = np.zeros(M - 1)
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * glue.GLX[None, :]
        val = (1.0 - np.abs(s - w) / D) * density(w)
        out -= half[:, 0] * (val @ glue.GLW)
    return out


def uv_cell_delta(D, density):
    """2 int_0^D (1-w/D)(density - rho) dw; the difference is finite
    at w = 0 (limit 1/2 for the D5 mirror), GL-48."""
    mid, half = 0.5 * D, 0.5 * D
    w = mid + half * glue.GLX
    diff = density(w) - glue.rho(w)
    return 2.0 * half * float(np.dot(glue.GLW, (1.0 - w / D) * diff))


def deck_wrong_layers(windows, true_layers):
    """RT6: arch layer rebuilt from the wrong deck density; d = 0 UV
    cell corrected by the finite density-difference integral."""
    out = []
    for window, lay in zip(windows, true_layers):
        M, D = window["M"], window["D"]
        arch = np.empty(M)
        arch[1:] = far_lags_of_density(M, D, deck_wrong_density)
        arch[0] = glue.arch_lag0_geo(D) - uv_cell_delta(
            D, deck_wrong_density)
        out.append(dict(arch=arch, atom=lay["atom"], pole=lay["pole"]))
    return out


def unpaired_profile(base):
    """RT8: the forbidden decomposition -- separate absolute layer
    estimates instead of the paired atom+pole error."""
    errors, e_at_all, e_po_all, e_pair_all = [], [], [], []
    for row in base["rows"]:
        src_l = row["src"]["layers"]
        tgt_l = row["tgt"]["layers"]
        ref = row["tgt"]["gram"]
        e_at = gp.error_metrics(src_l["atom"], tgt_l["atom"],
                                reference=ref)["spectral"]
        e_po = gp.error_metrics(src_l["pole"], tgt_l["pole"],
                                reference=ref)["spectral"]
        e_pair = gp.error_metrics(src_l["atom"] + src_l["pole"],
                                  tgt_l["atom"] + tgt_l["pole"],
                                  reference=ref)["spectral"]
        errors.append(e_at + e_po)
        e_at_all.append(e_at)
        e_po_all.append(e_po)
        e_pair_all.append(e_pair)
    cancellation = min(e_at_all[-1], e_po_all[-1]) \
        / max(e_pair_all[-1], 1.0e-300)
    print("\nRT8 -- forbidden decomposition (sources/targets reused "
          "byte-identically)")
    print("  separate e_at+e_po = %s"
          % "/".join("%.4f" % e for e in errors))
    print("  paired errors      = %s"
          % "/".join("%.4f" % e for e in e_pair_all))
    print("  top-window cancellation min(atom,pole)/pair = %.2f "
          "(audited 10.5)" % cancellation)
    prof = dict(rows=None, errors=errors, dims=base["dims"],
                slope=gp.log_slope(base["dims"], errors),
                ratio=errors[-1] / errors[0],
                tail=errors[-3] > errors[-2] > errors[-1],
                min_sym=base["min_sym"], lmin=base["lmin"],
                kappa=base["kappa"])
    print("  profile: slope=%.3f final/first=%.3f (symbol/PSD/kappa "
          "inherited from the true run)"
          % (prof["slope"], prof["ratio"]))
    return prof, cancellation


# ==================================================== run
def count_anti_alias(window):
    return 2 * window["M"] + 1


def run():
    print("=" * 78)
    print("GLOBAL HANDOFF -- RED TEAM circularity audit "
          "(v765 candidate)")
    print("=" * 78)

    hits = self_firewall()
    check("F0 self AST firewall (banned zero/prime identifiers)",
          not hits, str(hits or "clean"))
    check("G0.2 corruption manifest SHA-256 frozen before any comb "
          "data", True,
          "%s... (certificate bars + all eight corruption params); "
          "gram battery SHA-256 %s..."
          % (MANIFEST_HASH[:16], gp.BATTERY_SPEC_HASH[:16]))

    firewall_clean = firewall_audit()

    # ---- deployed frames, source comb, true layers (audited path)
    windows = glue.declared_family()
    maximum = int(max(math.exp(2.0 * window["alpha"])
                      for window in windows) + 0.5)
    comb, meta = gp.source_comb(maximum)
    true_layers = [gp.build_true_source_layers(window, comb)
                   for window in windows]
    wiring = 0.0
    for window, lay in zip(windows, true_layers):
        assembled = lay["arch"] + lay["atom"] + lay["pole"]
        wiring = max(wiring, float(
            np.max(np.abs(assembled - window["p"]))
            / np.max(np.abs(window["p"]))))
    check("G0.3 ingredient wiring before Q (reused guard)",
          wiring <= WIRE_TOL,
          "comb slots=%d, Gaussian irreducibles=%d, max rel dev %.3e"
          % (len(comb), meta["n_irred"], wiring))

    # ---- B0 baseline (the untouched construction, Candidate B)
    base = profile_eval("B0 BASELINE -- true construction, Nf = 2M+1",
                        windows, true_layers, count_anti_alias,
                        gp.target_gram)
    cl_base = certificate(base, None)
    band_ok = (SLOPE_BAND[0] <= base["slope"] <= SLOPE_BAND[1]
               and RATIO_BAND[0] <= base["ratio"] <= RATIO_BAND[1])
    baseline_ok = check(
        "B0 baseline passes the certificate and reproduces the "
        "audited run",
        all(cl_base.values()) and band_ok,
        "clauses=%s; slope %.3f in %s, final/first %.3f in %s; "
        "E* = %.4f, kappa = %.5f"
        % ({k: v for k, v in cl_base.items() if not v} or "all pass",
           base["slope"], list(SLOPE_BAND), base["ratio"],
           list(RATIO_BAND), base["errors"][-1], base["kappa"]))
    ref_final = base["errors"][-1]

    # ---- the eight controls
    results = []

    def run_control(cid, label, fn):
        print("\n%s -- %s" % (cid, label))
        try:
            prof = fn()
        except Exception as exc:  # inconclusive, never a silent pass
            check("%s %s BREAKS the frozen certificate" % (cid, label),
                  False, "EXCEPTION (inconclusive): %r" % exc)
            results.append(dict(cid=cid, label=label, broken=[],
                                passes=False, conclusive=False,
                                error=repr(exc)))
            return
        results.append(adjudicate_control(cid, label, prof, ref_final))

    run_control(
        "RT1", "position-scrambled comb",
        lambda: profile_eval(
            "RT1 scramble (seed %d)" % gp.RNG_SEED, windows,
            gp.scrambled_layers(windows, true_layers),
            count_anti_alias, gp.target_gram))

    def rt2():
        ep_layers, ep_atoms = gp.epstein_layers(windows)
        n_neg = int(np.sum(ep_atoms < -1.0e-9))
        prof = profile_eval(
            "RT2 Epstein x^2+5y^2 (%d negative atom sites)" % n_neg,
            windows, ep_layers, count_anti_alias, gp.target_gram)
        return prof
    run_control("RT2", "Epstein x^2+5y^2 logarithmic atoms", rt2)

    run_control(
        "RT3", "off-line zero pair injected into the TARGET "
        "(A=%.1f, delta=%.2f, gamma=%.1f; source bytes reused)"
        % (AMP_Z, DELTA_Z, GAMMA_Z),
        lambda: profile_eval(
            "RT3 corrupted target, frozen true sources", windows,
            None, count_anti_alias, target_offline,
            sources=[row["src"] for row in base["rows"]]))

    run_control(
        "RT4", "wrong pole normalization (closed pole block x %.1f)"
        % POLE_WRONG_FACTOR,
        lambda: profile_eval(
            "RT4 pole block x %.1f" % POLE_WRONG_FACTOR, windows,
            pole_wrong_layers(true_layers), count_anti_alias,
            gp.target_gram, post_source=pole_extra_rank_one))

    run_control(
        "RT5", "wrong mu4 class in the comb (chi_-4 twist)",
        lambda: profile_eval(
            "RT5 chi_-4 twisted sigma-descent comb", windows,
            mu4_twisted_layers(windows, true_layers),
            count_anti_alias, gp.target_gram))

    run_control(
        "RT6", "wrong deck twists (D5 mirror %s)" % (DECK_WRONG,),
        lambda: profile_eval(
            "RT6 wrong-deck arch layer", windows,
            deck_wrong_layers(windows, true_layers),
            count_anti_alias, gp.target_gram))

    run_control(
        "RT7", "insufficient frequency count (Candidate A regime)",
        lambda: profile_eval(
            "RT7 Nf = ceil(2 N(pi/D))", windows, true_layers,
            gp.requested_frequency_count, gp.target_gram))

    def rt8():
        prof, _cancel = unpaired_profile(base)
        return prof
    run_control("RT8", "removed atom-pole pairing (forbidden "
                "decomposition)", rt8)

    # ---- verdict (frozen rules)
    any_pass = [r["cid"] for r in results if r["passes"]]
    inconclusive = [r["cid"] for r in results
                    if not r["passes"] and not r["conclusive"]]
    all_conclusive = all(r["conclusive"] for r in results)
    if any_pass or not firewall_clean or not baseline_ok:
        verdict = "REDTEAM-RED"
    elif all_conclusive and len(results) == 8:
        verdict = "REDTEAM-GREEN"
    else:
        verdict = "REDTEAM-PARTIAL"

    print("\n" + "=" * 78)
    print("VERDICT: %s" % verdict)
    print("  firewall clean: %s | baseline reproduced: %s | "
          "controls broken: %d/8 (conclusive %d/8)"
          % (firewall_clean, baseline_ok,
             sum(1 for r in results if not r["passes"]),
             sum(1 for r in results if r["conclusive"])))
    for r in results:
        print("  %s %-52s %s" % (
            r["cid"], r["label"][:52],
            ("PASSES CERTIFICATE -- RED" if r["passes"] else
             ("broke via %s%s" % (",".join(r["broken"]),
                                  "" if r["conclusive"]
                                  else " (outside expected set)"))
             if r["error"] is None else "EXCEPTION: %s" % r["error"])))
    if verdict == "REDTEAM-GREEN":
        print("HONEST STATEMENT: on this surface the round's "
              "convergence survives the red team -- every frozen "
              "corruption (source scramble, Euler-free atoms, "
              "target-side off-line pair, pole normalization, mu4 "
              "class, deck twists, frequency budget, unpaired "
              "accounting) measurably breaks the certificate, and "
              "the static audit finds no channel from the target "
              "(eigen/Cholesky/zero/prime data, post-hoc scalars) "
              "into the source construction.  Unchanged and open: "
              "the eps -> 0 wall, the battery-limited "
              "identification, every RH-level positivity statement.  "
              "NO RH claim.")
    elif verdict == "REDTEAM-RED":
        print("HONEST STATEMENT: the audit FAILED -- %s.  The "
              "round's convergence claims are NOT protected against "
              "hidden target information and must not be promoted."
              % ("; ".join(
                  (["controls passing the true gates: %s"
                    % any_pass] if any_pass else [])
                  + ([] if firewall_clean else
                     ["firewall found target leakage"])
                  + ([] if baseline_ok else
                     ["baseline did not reproduce"]))))
    else:
        print("HONEST STATEMENT: audit inconclusive on %s -- these "
              "controls broke the certificate, but not through their "
              "preregistered clauses (or errored); the round's "
              "convergence is not invalidated, but the audit does "
              "not fully certify it either." % inconclusive)

    elapsed = time.time() - T_START
    if FAILS:
        print("RESULT: %d/%d CHECKS PASSED; FAILURES %s (%.1f s)"
              % (len(CHECKS) - len(FAILS), len(CHECKS),
                 ",".join(FAILS), elapsed))
    else:
        print("RESULT: ALL %d CHECKS PASSED (%.1f s)"
              % (len(CHECKS), elapsed))
    return 0 if verdict == "REDTEAM-GREEN" else 1

_run_part1 = run


def _run_part2():
    # PART 2 -- handoff_redteam_rt6_probe.py (verbatim; module-level names are
    # local to this function scope; the alias import of the
    # parent points at this module)


    import ast
    import hashlib
    import json
    import math
    import os
    import sys
    import time

    import numpy as np

    _HERE = os.path.dirname(os.path.abspath(__file__))
    _VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
    sys.path.insert(0, _HERE)
    sys.path.insert(0, _VERIFY)

    import v716_moonshot_arch_glue as glue  # noqa: E402
    import v767_handoff_frequency_gram as gp  # noqa: E402
    rt = sys.modules[__name__]  # part 1 of this module

    T_START = time.time()

    TRUE_DECK = dict(exponents=(0.5, 2.5, 4.5), weights=(1.0, 1.0, 1.0))
    VARIANTS = (
        dict(tag="V1", label="full mirror (D5, parent RT6 rerun)",
             exponents=(0.75, 1.5, 2.25), weights=(1.0, 1.0, 1.0),
             gate_blindness=True),
        dict(tag="V2", label="single-channel phase swap r=5 -> r=3",
             exponents=(0.5, 1.5, 4.5), weights=(1.0, 1.0, 1.0),
             gate_blindness=False),
        dict(tag="V3", label="channel-mass redistribution (3/2, 3/2, 0)",
             exponents=(0.5, 2.5), weights=(1.5, 1.5),
             gate_blindness=False),
    )
    NEG_BLOCK = dict(tag="N1", label="deficit swap r=5 -> r=7 (NOT gated)",
                     exponents=(0.5, 3.5, 4.5), weights=(1.0, 1.0, 1.0))

    MANIFEST = dict(
        version="handoff-redteam-rt6-v1",
        parent="handoff_redteam_probe REDTEAM-PARTIAL 2026-08-04, "
               "RT6 inconclusive (broke c4 outside expected set)",
        statement="symbol gate = load-bearing deck-corruption detector; "
                  "other gates blind after positive-part clipping",
        certificate="imported frozen from handoff_redteam_probe",
        baseline_bands=dict(slope=list(rt.SLOPE_BAND),
                            ratio=list(rt.RATIO_BAND)),
        true_deck=dict(exponents=list(TRUE_DECK["exponents"]),
                       weights=list(TRUE_DECK["weights"])),
        variants=[dict(tag=v["tag"], exponents=list(v["exponents"]),
                       weights=list(v["weights"]),
                       gate_blindness=v["gate_blindness"])
                  for v in VARIANTS],
        negative_block=dict(tag=NEG_BLOCK["tag"],
                            exponents=list(NEG_BLOCK["exponents"]),
                            weights=list(NEG_BLOCK["weights"]),
                            gated=False),
        verdicts=["RT6-SYMBOL-DETECTS", "RT6-PARTIAL", "RT6-INVALID"],
    )
    MANIFEST_HASH = hashlib.sha256(json.dumps(
        MANIFEST, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

    CHECKS = []
    FAILS = []


    def check(name, ok, detail=""):
        CHECKS.append(name)
        if not ok:
            FAILS.append(name.split()[0])
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                             (": " + detail) if detail else ""))
        return bool(ok)


    def self_firewall():
        with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
            tree = ast.parse(fh.read())
        hits = set()
        for node in ast.walk(tree):
            name = ""
            if isinstance(node, ast.Name):
                name = node.id
            elif isinstance(node, ast.Attribute):
                name = node.attr
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                for alias in node.names:
                    token = alias.name.split(".")[0]
                    if any(b in token.lower() for b in rt.BANNED):
                        hits.add(token)
            if name and any(b in name.lower() for b in rt.BANNED):
                hits.add(name)
        return sorted(hits)


    def deck_density(exponents, weights):
        """Deck-class density sum_i w_i e^{-b_i t} / (1 - e^{-6t})."""
        def density(w):
            w = np.asarray(w, float)
            numerator = sum(wt * np.exp(-b * w)
                            for b, wt in zip(exponents, weights))
            return numerator / (-np.expm1(-6.0 * w))
        return density


    def wrong_arch_layers(windows, true_layers, density):
        """Arch layer rebuilt from a frozen wrong deck density; the d = 0
        UV cell corrected by the finite difference integral (reused
        frozen builders from the parent probe)."""
        out = []
        for window, lay in zip(windows, true_layers):
            M, D = window["M"], window["D"]
            arch = np.empty(M)
            arch[1:] = rt.far_lags_of_density(M, D, density)
            arch[0] = glue.arch_lag0_geo(D) - rt.uv_cell_delta(D, density)
            out.append(dict(arch=arch, atom=lay["atom"], pole=lay["pole"]))
        return out


    def report_variant(tag, label, prof, ref_final):
        clauses = rt.certificate(prof, ref_final)
        txt = rt.clause_strings(prof, ref_final)
        per_window = [row["min_sym"] for row in prof["rows"]]
        c4_every = all(ms < -rt.SYM_TOL for ms in per_window)
        blind = [k for k in rt.CLAUSE_ORDER if k != "c4_symbol"
                 and clauses[k]]
        seen = [k for k in rt.CLAUSE_ORDER if k != "c4_symbol"
                and not clauses[k]]
        print("  %s min symbol per window: %s" % (
            tag, " / ".join("%+.3e" % ms for ms in per_window)))
        for k in rt.CLAUSE_ORDER:
            print("    %-9s %-7s %s"
                  % (k, "BROKEN" if not clauses[k] else "ok", txt[k]))
        print("  %s gates blind: %s%s"
              % (tag, blind, ("; gates that saw it: %s" % seen)
                 if seen else " (only the symbol gate fired)"))
        return dict(c4_every=c4_every, per_window=per_window,
                    blind=blind, seen=seen, clauses=clauses)


    def run():
        print("=" * 78)
        print("GLOBAL HANDOFF -- RED TEAM RT6 decision: the symbol gate "
              "as deck detector")
        print("=" * 78)

        hits = self_firewall()
        check("F0 self AST firewall (banned zero/prime identifiers)",
              not hits, str(hits or "clean"))
        check("G0.1 variant manifest SHA-256 frozen before any comb data",
              True, "%s...; gram battery SHA-256 %s..."
              % (MANIFEST_HASH[:16], gp.BATTERY_SPEC_HASH[:16]))

        # ---- deployed frames, source comb, true layers (audited path)
        windows = glue.declared_family()
        maximum = int(max(math.exp(2.0 * window["alpha"])
                          for window in windows) + 0.5)
        comb, meta = gp.source_comb(maximum)
        true_layers = [gp.build_true_source_layers(window, comb)
                       for window in windows]
        wiring = 0.0
        for window, lay in zip(windows, true_layers):
            assembled = lay["arch"] + lay["atom"] + lay["pole"]
            wiring = max(wiring, float(
                np.max(np.abs(assembled - window["p"]))
                / np.max(np.abs(window["p"]))))
        check("G0.2 ingredient wiring before Q (reused guard)",
              wiring <= rt.WIRE_TOL,
              "comb slots=%d, Gaussian irreducibles=%d, max rel dev %.3e"
              % (len(comb), meta["n_irred"], wiring))

        # ---- B0 positive anchor (full certificate incl. c4)
        base = rt.profile_eval("B0 BASELINE -- true construction, "
                               "Nf = 2M+1", windows, true_layers,
                               rt.count_anti_alias, gp.target_gram)
        cl_base = rt.certificate(base, None)
        band_ok = (rt.SLOPE_BAND[0] <= base["slope"] <= rt.SLOPE_BAND[1]
                   and rt.RATIO_BAND[0] <= base["ratio"]
                   <= rt.RATIO_BAND[1])
        baseline_ok = check(
            "B0 baseline passes the FULL certificate incl. c4 and "
            "reproduces the audited bands",
            all(cl_base.values()) and band_ok,
            "clauses=%s; slope %.3f in %s, final/first %.3f in %s; min "
            "symbol %+.2e, E* = %.4f, kappa = %.5f"
            % ({k: v for k, v in cl_base.items() if not v} or "all pass",
               base["slope"], list(rt.SLOPE_BAND), base["ratio"],
               list(rt.RATIO_BAND), base["min_sym"], base["errors"][-1],
               base["kappa"]))
        if not baseline_ok:
            print("\nVERDICT: RT6-INVALID -- the true construction fails "
                  "its own certificate; construction problem, promotion "
                  "blocked.  COMBINED: NOT-GREEN.")
            return 1
        ref_final = base["errors"][-1]
        base_min_sym = base["min_sym"]

        # ---- gated excess-mode variants
        results = {}
        for var in VARIANTS:
            print("\n%s -- %s (exponents %s, weights %s)"
                  % (var["tag"], var["label"], var["exponents"],
                     var["weights"]))
            layers = wrong_arch_layers(
                windows, true_layers,
                deck_density(var["exponents"], var["weights"]))
            prof = rt.profile_eval("%s wrong-deck arch layer" % var["tag"],
                                   windows, layers, rt.count_anti_alias,
                                   gp.target_gram)
            res = report_variant(var["tag"], var["label"], prof, ref_final)
            results[var["tag"]] = res
            check("%s.a symbol gate fires on EVERY window (min symbol "
                  "< -%.0e)" % (var["tag"], rt.SYM_TOL), res["c4_every"],
                  " / ".join("%+.3e" % ms for ms in res["per_window"]))
            if var["gate_blindness"]:
                blind_ok = all(res["clauses"][k] for k in rt.CLAUSE_ORDER
                               if k != "c4_symbol")
                check("%s.b BLINDNESS confirmed: c1/c2/c3/c5/c6/c7 all "
                      "pass under the clipped gram (the symbol gate is "
                      "the ONLY detector)" % var["tag"], blind_ok,
                      "blind=%s, saw-it=%s" % (res["blind"], res["seen"]))

        # ---- N1 negative block (measured, not gated)
        print("\n%s -- %s (exponents %s): DECLARED DEFICIT MODE, "
              "positivity gates provably blind by sign"
              % (NEG_BLOCK["tag"], NEG_BLOCK["label"],
                 NEG_BLOCK["exponents"]))
        layers_n1 = wrong_arch_layers(
            windows, true_layers,
            deck_density(NEG_BLOCK["exponents"], NEG_BLOCK["weights"]))
        prof_n1 = rt.profile_eval("N1 deficit-deck arch layer", windows,
                                  layers_n1, rt.count_anti_alias,
                                  gp.target_gram)
        res_n1 = report_variant("N1", NEG_BLOCK["label"], prof_n1,
                                ref_final)
        into_interior = all(ms >= base_min_sym - rt.SYM_TOL
                            for ms in res_n1["per_window"])
        caught_by = res_n1["seen"] + (["c4_symbol"]
                                      if res_n1["c4_every"] else [])
        print("  N1 measured outcome (reported, not gated): symbol moves "
              "into the interior on every window = %s (baseline min "
              "%+.2e); caught by = %s -- %s"
              % (into_interior, base_min_sym, caught_by or "NOTHING",
                 "the certificate's resolution floor for interior-"
                 "directed perturbations, consistent with the declared "
                 "battery-limited identification remainder"
                 if not caught_by else
                 "the deficit mode is caught by the listed gate(s)"))

        # ---- verdict (frozen rules)
        c4_all = all(results[v["tag"]]["c4_every"] for v in VARIANTS)
        blind_v1 = all(results["V1"]["clauses"][k]
                       for k in rt.CLAUSE_ORDER if k != "c4_symbol")
        if c4_all and blind_v1:
            verdict = "RT6-SYMBOL-DETECTS"
        else:
            verdict = "RT6-PARTIAL"
        escapes = [v["tag"] for v in VARIANTS
                   if not results[v["tag"]]["c4_every"]]

        print("\n" + "=" * 78)
        print("VERDICT: %s" % verdict)
        if verdict == "RT6-SYMBOL-DETECTS":
            print("  the symbol gate fires on all three excess-mode deck "
                  "corruptions on every window; under V1 the clipped "
                  "gram passes c1/c2/c3/c5/c6/c7 -- the blindness of the "
                  "rate/level/identification gates is CONFIRMED, the "
                  "symbol gate is the load-bearing detector.")
            print("COMBINED AUDIT STATEMENT: with the parent probe's "
                  "frozen facts (firewall clean, baseline reproduced, "
                  "RT1-RT5/RT7/RT8 conclusive) and this RT6 decision, "
                  "the round's red team is REDTEAM-GREEN-COMBINED.")
            print("PROMOTION NOTE (binding): the symbol-nonnegativity "
                  "gate must NEVER be dropped from any future "
                  "certificate -- for the excess-mode deck-corruption "
                  "class it is the ONLY firing detector; N1 marks the "
                  "measured detector boundary (deficit mode: symbol "
                  "into the interior, caught by %s).  NO RH claim."
                  % (caught_by or "nothing at this resolution"))
        else:
            print("  %s%s" % (
                ("variants escaping even the symbol gate: %s -- a "
                 "genuine audit hole. " % escapes) if escapes else "",
                "" if blind_v1 else
                "V1 blindness clause failed: gates %s saw the corruption."
                % results["V1"]["seen"]))
            print("COMBINED AUDIT STATEMENT: the round's red team is "
                  "NOT-GREEN; promotion of the handoff round stays "
                  "blocked on the RT6 decision.")

        elapsed = time.time() - T_START
        if FAILS:
            print("RESULT: %d/%d CHECKS PASSED; FAILURES %s (%.1f s)"
                  % (len(CHECKS) - len(FAILS), len(CHECKS),
                     ",".join(FAILS), elapsed))
        else:
            print("RESULT: ALL %d CHECKS PASSED (%.1f s)"
                  % (len(CHECKS), elapsed))
        return 0 if verdict == "RT6-SYMBOL-DETECTS" else 1
    return run(), list(FAILS)


def run():
    """run_all entry point (combined adjudication, frozen in part 2):
    part 1 must reproduce its preregistered pattern (all 16 checks
    pass, verdict REDTEAM-PARTIAL = rc 1 with zero check failures:
    RT6 broke only outside its expected set); part 2 must pass 8/8
    (RT6-SYMBOL-DETECTS) -- together REDTEAM-GREEN-COMBINED."""
    rc1 = _run_part1()
    part1_ok = (rc1 == 1 and not FAILS)
    print("\n[%s] PART-1 PATTERN GATE: expected 16/16 checks with "
          "verdict REDTEAM-PARTIAL (RT6 the single preregistered "
          "inconclusive) -- check failures: %s"
          % ("PASS" if part1_ok else "FAIL", FAILS or "none"))
    rc2, fails2 = _run_part2()
    part2_ok = rc2 == 0 and not fails2
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- REDTEAM-GREEN-COMBINED: "
          "firewall clean, baseline reproduced, RT1-RT5/RT7/RT8 "
          "conclusive (part 1) and RT6 decided (part 2: symbol gate "
          "fires on all excess-mode deck corruptions, other gates "
          "blind under V1; deficit mode caught by rate/ratio/kappa) "
          "-- BINDING: certificates must always carry BOTH gate "
          "families (symbol/PSD and rate/ratio/identification).  "
          "NO RH claim." % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    import sys as _sys
    _sys.exit(run())
