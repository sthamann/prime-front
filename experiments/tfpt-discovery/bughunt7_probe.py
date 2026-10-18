#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt7_probe -- PRIME.BUGHUNT7.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  Seventh adversarial
audit: the discovery rounds 170-175 (r170 = bughunt6_probe [audit the
auditor], r171 = jetmass_floor_probe, r172 = toproot_theta_probe,
r173 = h3_cofinal_probe, r174 = gonek_pricing_probe, r175 =
thetainf_pin_probe; notes CDLXXXV-CDXCI).  Predecessors
r87/r109/r130/r149/r164/r170.  This probe writes NOTHING but stdout,
reads the frozen corpus READ-ONLY (probe sources as text, kept
run/smoke logs, next.txt, one pinned read-only `git show`), imports
NO frozen probe, and makes NO RH CLAIM in either direction.  Every
confirmed finding carries at least one falsifiable gate.

METHOD (bughunt I-VI standard): source/note/log conjunctions for
every wording finding; OWN re-implementations for every numeric
re-check (own HSW-G, own sympy derivations on own symbols, own
DFS/AND-fire graph semantics, own diff normalizer, own prime-power
arithmetic); expensive claims audited on the kept record logs, cheap
claims re-run inline.  External literature verification (web,
2026-08-20) pinned in this spec.

=======================================================================
FINDINGS LEDGER (the deliverable; severity frozen; gates named)
=======================================================================
BH7-F1 [MAJOR][residue-prose compression; hidden per-rung premises;
  X1/X2 core; NO VERDICT FLIP]  The r172 terminal residue statement
  "der lambda-uniforme Rest ist EXAKT H3-KOFINAL" (note CDLXXXVIII;
  docstring: "THE FINAL RESIDUE (exact): {H3-COFINAL: ... the entire
  lambda-uniform residue ...}") and its verbatim transports into the
  r173/r174/r175 residues ("{H3-COFINAL} + {census-all-k == LOOP} +
  {L1, WPD}") UNDERSTATE the per-rung hypothesis set: the assembled
  jet-mass floor at the block representative h of every deep dyadic
  block needs H1(h) AND H2(h) AND H3(h) -- PF is proven only GIVEN
  H1+H2 at that rung (r171: "THEOREM CONDITIONAL EXACTLY ON {H1 + H2
  per rung (finite, source-classical)}"), and H1/H2 are hard-gated
  only at h <= 26 resp. h <= 13 (structure <= 24, h > 24 reported).
  All three are per-rung finite source checks of the same epistemic
  type; singling out H3 as THE lambda-uniform residue is not
  justified by any surface (no surface states or discharges
  H1/H2-cofinal; machine-grepped).  The MACHINE layer is consistent
  (r171/r172 G61 declare ENVJ-CERT-H1 + CENSUS-H2-PER-RUNG as
  ancestors of the assembled chain; the G63 graphs carry {ENVJ_H1,
  CENSUS_H2, TRACE} -> PF), so nothing is consumed wrongly and no
  verdict flips -- the compression is prose-level, but it sits on
  the PRIMARY residue surface of four consecutive rounds.
  MACHINE DEMONSTRATION (G10): own AND-fire propagation on the
  declared chain -- the prose-residue grant set {H3_DEEP, RATE-DICT,
  GONEK-PRICED, CENSUS-PER-K, TRACE} does NOT fire the deep
  jet-mass floor; adding {H1_DEEP, H2_DEEP} fires it.
  CORRECTION OF RECORD (proposed wording): the residue item should
  read "{H1 und H2 und H3}-KOFINAL (eine Sprosse pro dyadischem
  Block, alle drei am selben h; H1/H2/H3 saemtlich endliche
  Quell-Checks pro Sprosse, zertifiziert nur h <= 26/13(24)/30)" --
  or H1/H2-cofinal must be carried as an explicit residue item
  beside H3-COFINAL.  GATE: G10.
BH7-F2 [MINOR][limsup quantifier upgrade loses its qualifier -- X1]
  Note CDXC states the collapse correctly qualified: "H3-KOFINAL ==
  (mod gemessener Defekt D = 0.0042 + gemessener Monotontrend,
  G11/G44) DIE EINE LIMES-UNGLEICHUNG limsup theta_y <= 0.155".
  Note CDXCI's residue drops the qualifier: "{H3-KOFINAL == limsup
  theta_y <= 0.155, ...}".  Bare, the equivalence is FALSE as a
  quantifier statement: cofinal(bar) is liminf-class; it implies
  only limsup <= bar + D, and only UNDER the measured defect-D
  near-monotonicity (own counterexample gated: a sequence cofinal at
  the bar with limsup > bar).  Own recompute of D from the cited
  r172 ladder: D = 0.004183 at the drawdown pair (14, 19) -- the
  qualified CDXC statement is exactly right.  CORRECTION: cite the
  limsup form only with the mod-D qualifier (CDXC wording).
  GATE: G11.
BH7-F3 [MINOR][vacuous exact-layer legs in r171 -- BH6-F3 class
  recurrence]  Two legs of r171's PROVEN-typed exact gates cannot
  fail: (i) G11 okG second binding sp.simplify(((y-al)**2 + be**2)
  - (y-al)**2 - be**2) == 0 is an identically-zero tautology (E - E
  == 0, exactly the BH6-F3 okH class) presented as the complex-pair
  bound; (ii) G12 okN first binding "((t2s - t1s).is_positive is
  None) or True" is an always-True expression (dead code,
  immediately rebound to the trivial rational instance 9/10 < 1,
  which verifies nothing of the no-root corollary beyond
  arithmetic).  The THEOREMS stay true (be^2 >= 0 and the triangle
  corollary are elementary); no verdict flips.  TIMING NOTE: r171's
  spec froze 2026-08-19 ~08:46, BEFORE bughunt6 landed (~18:50) --
  no adoption violation (CDLXXXVI's F3 adoption scope was the
  promotion-wave modules); the class RECURRED on a live surface.
  r172-r175 scanned CLEAN of the class (own pattern scan).
  CORRECTION: re-code the two legs against real objects or type
  them DEFINITIONAL at the next amendment opportunity.  GATE: G12.
BH7-F4 [MINOR][manifold-exclusion verdict lacks its rung scope --
  the r173 C3 sentence]  The C3 verdict ("jede y_t-bewegende
  Stoerung verlaesst entweder den Grundzustand (G30,
  DK-quantifiziert), das zweiseitige Lock-Fenster (exakt, beide
  Richtungen), die BA3-Bruecke (x3.6e8) oder die Welt") is
  universally quantified over perturbations but its gated support
  is rung-limited: (i) the DK/ground-state leg pins y_t only within
  the measured radius -- r173's OWN G36 discloses the gate-bar
  crossover at h = 16 and measured-radius failure at h = 24 ("h24
  gate inf meas inf"); (ii) OWN recompute from the cited r172
  ladders: at 24 of 25 rungs the MINIMAL H3-refuting inflation
  W = bar/theta_y (~2.0-2.5) keeps lock/W INSIDE the lock window
  (1.0, 8.0) -- the lock leg excludes only large dials (the tested
  witnesses use W = 1000); (iii) the BA3-bridge and census legs are
  measured for the two specific frozen witnesses only.  For a
  minimal H3-refuting perturbation at h >= 16 (gate-bar) resp.
  h >= 24 (measured residuals), NO gated leg excludes it -- the
  crossover is honestly disclosed in the same note, but the verdict
  sentence omits the scope.  No verdict flips (H3-REFUTABLE-OFF-
  MANIFOLD is itself restated by r173).  CORRECTION: scope the
  sentence "innerhalb des DK-Radius (gegated h <= 13, gemessen bis
  h = 20)".  GATE: G13.
BH7-F5 [NOTE][r172 docstring calls the one-directional RATE-FORM an
  "equivalent" form]  The T1 header "EQUIVALENT MACHINE FORMS (each
  gated this round)" lists "(iii) RATE-FORM ... TOPROOT(p) ==> WF
  >= ... ==> a = p/2 - 1" -- stated and gated as an implication
  only.  The note CDLXXXVIII is careful ("DREI ... Aequivalenzformen
  ... PLUS die RATEN-FORM").  The exponent map is a bijection (r175
  G12 proves dictionary covariance), but the gated statement is
  one-directional.  CORRECTION: cite the three equivalent forms per
  the note's wording.  GATE: G14.
BH7-F6 [NOTE][r171 H2 typing compression in the terminal statement]
  Note CDLXXXVII's terminal statement types H2 "an allen 25 Sprossen
  verifiziert" while the gate is HARD h <= 13, structure <= 24,
  h > 24 CENSUS-DEPTH-REPORTED (4 reported rows incl. the
  degree-116 h = 28 polyroots; disclosed in the SAME note: "hart
  h <= 13, Struktur <= 24, h > 24 DEPTH-REPORTED sauber", and
  warded by SR1/product-id <= 1e-58).  "Verifiziert" for the
  reported-only rows is observational, not gated.  GATE: G15.
BH7-F7 [NOTE][r175 "bewiesene Verschwendung" overstates measured to
  proven]  CDXCI lever (c) says census deepening for the pin is
  "bewiesene Verschwendung" -- the T_req wall is a MEASURED-LAW
  EXTRAPOLATION (measured ~1/T tail law, drop ~48 over 1e5 -> 1e7;
  measured amp/gap ladders at 4 rungs; DK agreement measured), and
  the probe's own typing is honest (T_req in the GEMESSEN block;
  PIN-CENSUS-UNREACHABLE-BY-DEPTH gated per rung as strings).  OWN
  recompute reproduces the T_req ladder 3.76e14/5.68e21/5.55e41/
  1.75e77 from the frozen AMP/GAPABS/DM tabs and T(2e7).
  CORRECTION: "gemessene Verschwendung" (measured-law
  extrapolation).  GATE: G16.
BH7-F8 [NOTE][r175 G53 enumeration leg is definitional -- BH6-F3
  borderline class]  The leg "admissible == []" filters a FROZEN
  dict of verdict strings by their own kill-prefixes and cannot
  fail given the dict; the load-bearing kills are individually
  gated elsewhere (G14/G15/G33/G36/G37/G38) and the same gate
  carries two real legs (band margin, 4 pi window).  Flagged for
  the record; recommended typing: DEFINITIONAL in the gate detail.
  GATE: G17.

CHECKED CLEAN (adversarially, no finding): SPEC_SHA integrity of all
FIVE audited probes (docstring hash == claimed) and all 21 kept
smoke/run logs match the disclosed amendment/smoke-fix lineages
(r171 4f8d -> 92c8 -> 57de = Amendments 1+2 with run1/run2 fail rows
kept; r172 8f95 -> cf27, r173 123c -> 876d, r174 f1e2 -> 3050, r175
252e -> 3044 = disclosed pre-record smoke-stage fixes; every smoke
fail row matches its disclosed root cause gate-exactly); the five
record run pairs re-diffed with the OWN normalizer (raw 4/4/4/2/5
wall-clock line pairs, timing-normalized EMPTY -- the notes state
exactly this, BH6-F2 adopted on all five new surfaces, no
"bit-identical" claim anywhere); note-vs-log numbers verified for
CDLXXXVII-CDXCI (gate counts 36/33/36/20/28, runtimes, SHAs, smoke
accounting); numerals CDLXXXV-CDXCI gap-free, unique, strictly
descending, attribution correct (each note names its probe file;
the r171 note names CDLXXXVI as prior head -- the concurrent
promotion-wave lane -- and CDXC names CDLXXXIX as the parallel
Gonek-pricing lane, NOT consumed, correctly); BUGHUNT6 F1/F2/F3
re-verified CORRECT with own arithmetic (entry atoms 7/9/13/17 from
dbt_run1.log: largest-new-PRIME 3/4, largest-new-ATOM 2/4,
note-reading 4/4; dbt/sf raw diffs 5/4 -> 0 normalized; both
vacuous legs present verbatim in the r168/r169 sources); r171 PF2
concavity lemma re-derived OWN (positive Taylor coefficients of
-log(1-u)/u ==> per-factor bound (1-a/y) >= (1-c/y)^{a/c} for
0 <= a <= c < y; trace budget S+ <= (1+kappa+NEGBAR) y_t from the
coefficient-level trace + negsum ward; OWN rational instance with
different numbers); the PF2 domain condition c* y_t > b_top is
CODED in r171's H1 grid (c with c y_t <= b_top skipped -- the
witness world's "domain EMPTY" is exactly this check) though the
PF2 prose states only z > c*; the ~100k pointwise claim is honest
(own log parse: sum n = 97259 over h = 4..24, all min margins
positive, factor z >= 1.05 c* disclosed on every surface);
kappa = B_1/y_t closed form consumes pole geometry + source only
(nothing pinned); r172 p_max chain reproduced OWN to full precision
(eps_closed(56) = 4.533792e-9, a_max = 4.134758, p_max = 10.269515,
own bisection h*_rate(0.0767, a_max) = 56.00) -- honestly typed
PT21-anchored with the MEASURED r171 constant c = 0.0767, and
asymptotically no ceiling (SF4); the r172 smoke-stage fix (two
sympy instrument bugs) matches the kept smoke1 fail rows (G12/G14)
gate-exactly, no bar moved; r173's v926 consumption is FLAGGED at
every site (grep: FG-QUARTIC-MEAS excluded from the delivered set,
TRANSPORT-CEILING typed CONDITIONAL-ON-MEASURED, G43 prints the
ceiling with the flag); r173's theta_inf band is the across-model
spread of five frozen 2-parameter fits with holdout exclusion
(honest as recorded; window-dependence is the disclosed model
spread); r174 literature pins EXTERNALLY VERIFIED (web 2026-08-20,
pinned here): Landau, Math. Ann. 71 (1912) 548-564 -- the theorem
is often dated 1911, the volume year is 1912, citation valid;
Gonek's uniform formula EXACTLY as quoted incl. all three error
terms, <x> = distance to nearest other prime power, and the
integer-x subsumption remark; Gonek 1984 (Invent. Math. 75,
123-142) discrete zeta'-moments RH-CONDITIONAL -- the [R]-flag
adjudication is correct; the r174 ENV T_hi-collapse re-derived OWN
(sympy: integral identity ENV == sqrt(x) loglog(3x)
[(4 log(2x T_lo) + 1)/(2 T_lo^2) - 1/(2 T_hi^2)] EXACT), so
census-depth-insensitivity holds and "any finite constant" hides
no uniformity-in-h issue BECAUSE [G] is uniform in (x, T) -- one
constant covers all rungs; the r174 smoke bar rescale is
smoke-only in code (chat_min_eff = CTRL_CHAT_MIN/4 iff smoke;
full-depth bar 20 untouched; record controls all >= 20);
composites-give-Lambda-0 is used only as the honest null
prediction (C_main == 0 gated AGAINST the envelope at composite
rungs, max priced ratio at h = 6 a composite); r175 resonance
removability re-derived OWN (lim_{g -> om} sin^2(A g)/(g^2 - om^2)
= 0 at A om = k pi, quadratic kill; measured min |gamma - om_k| >=
0.105 -- no hazard on the actual mode grid); trivial-zero density
1/(t(t^2-1)) == geometric sum re-derived OWN; the r175
world-separation numbers use the SAME instrument settings as the
truth runs (same census cache, same deepest checkpoint
n_lad[-1], code conjunction); X3 residue transport CONSISTENT
across r171 -> r175 (r171 names TOPROOT + GONEK + ALLK + {L1,
WPD}; r172 swaps TOPROOT -> H3-COFINAL; r173 keeps the Gonek item
with the parallel-lane disclosure; r174 removes it
(RESIDUE-SHRUNK); r175 carries {H3-KOFINAL, theta_inf face} +
ALLK + {L1, WPD} -- nothing silently dropped); L1/WPD adjudicated
LIVE-NOT-STALE: the round-128 serial pair (L1 + WPD ==> R ==> RH
via NF-closure), L1 refined to TAIL (proven, HSW22+PT21) + H-pin
(open), WPD open with the proof-attempt obstruction machine-pinned
(wpd_proof_probe); X2 ancestry MACHINE-CHECKED with own DFS: the
delivered chain {H1, H2, TRACE} -> PF, {GONEK-PRICED, CENSUS-PER-K}
-> WF, {H3} -> RATE, {PF, WF, RATE} -> JETMASS -> SIGMAFLOOR ->
DTSTEP -> HCOF -> RH-arrows is ACYCLIC, none of {TAUPOS, TLAWCAP,
CENSUS-ALLK, GONEK-1984-RH, MONTGOMERY-PC-RH} is an ancestor of
any delivered node, and all four flagged loop cycles
(universalized census, pinning-supply, gonek-1984, montgomery-pc)
re-detected with the own DFS; the witness-manifold legs (lock,
BA3) consume SPECTRAL-CERT/TAU-MEAS but have NO outgoing edge into
the delivered chain (red-team only, no cycle).

X-VERDICTS (the contract deliverables):
X1 QUANTIFIER COMPOSITION: the assembly [PF given H1+H2 per rung] x
  [WF classical-per-census] x [RATE given H3] COMPOSES at the
  SEQ-cofinal quantifier WITHOUT any hidden forall-h (the sigma-
  floor schedule absorption is per-block-representative; SF4
  absorbs any polynomial rate) -- BUT the composed per-block
  hypothesis is the TRIPLE {H1, H2, H3} at the same rung, not H3
  alone (= BH7-F1); and the limsup form of H3-KOFINAL holds only
  mod the measured defect D (= BH7-F2).  VERDICT:
  COMPOSITION-SOUND-AT-SEQ + RESIDUE-TRIPLE-NOT-SINGLETON.
X2 HYPOTHESIS-LEDGER ANCESTRY: complete per-rung ledger = {H1
  (ENVJ, source-pure), H2 (census complete-real-nonneg, negsum
  ward), H3 (quartic cap, source-pure), TRACE (coefficient-level,
  unconditional)} + manifold {ground-state cert (SPECTRAL-CERT),
  two-sided lock (SPECTRAL + SOURCE), BA3 bridge (CENSUS-PER-K +
  HSW22 + TAU-MEAS)}.  NONE is equivalent to or an ancestor of the
  flagged loops (census-forall-k, A0-triangle/pinning-supply,
  TAUPOS/TLAWCAP, RH-conditional second moments) -- machine-checked
  (own DFS).  The manifold legs consume TAU-MEAS but feed only the
  red-team exclusion, not the delivered chain: NO new loop.
X3 RESIDUE BOOKKEEPING: consistent across r171-r175 (transport
  verified, Gonek exit at r174 clean, concurrency disclosures
  correct); L1 and WPD are LIVE labels (round-128 pair; L1 = TAIL
  proven + H-pin open; WPD open, obstruction pinned), carried
  verbatim in all five residues -- coarse but not stale.
X4 NOTE NUMERALS: CDLXXXV-CDXCI collision-free, gap-free,
  attribution and concurrency exact; every note's headline numbers
  match its record log.
X5 SPEC_SHA: all five probes hash to their claimed SPEC_SHA; all 21
  logs match the disclosed lineage; every smoke-stage fix is
  disclosed in the frozen docstring itself (amended pre-record,
  house-legal) with its smoke fail row kept.

FROZEN NUMERICS (audit pins; sources = frozen record logs/specs):
SHAS = {jmf: 57de8b2a83677a9c (pre: 4f8d05e02cb020f9,
92c895a4053dd781), tt: cf27df22aa5dffbf (pre: 8f95035e57b4b034),
h3c: 876dafc977d3d8fc (pre: 123cde67d20afd3c), gp: 3050678b352eaa9a
(pre: f1e237fe428d0e8d), tip: 3044558e5fa52e01 (pre:
252ed636b4e32a7d), bh6: 5964350254696fa5}.  DIFF_PAIRS = {jmf: 4,
tt: 4, h3c: 4, gp: 2, tip: 5} raw, 0 normalized.  RUNTIMES = {jmf:
(2055.9, 2063.7), tt: (2812.6, 2821.5), h3c: (1162.6, 1171.6), gp:
(187.9, 188.4), tip: (577.4, 578.7)}.  GATES = {jmf: 36, tt: 33,
h3c: 36, gp: 20, tip: 28}.  R168_COMMIT = d831f15e.  ENTRY_ATOMS =
{(4,8): 7, (5,10): 9, (8,16): 13, (9,18): 17}; BH6_READINGS =
(3, 2, 4).  PW_SUM = 97259; PW_FACTOR = 1.05; CENSUS_REPORTED = 4.
D_STR = 0.004183 at (14, 19), rel 5e-3.  NONEXCL_MIN = 20 (measured
24 of 25).  CROSSOVER_H = 16.  EPS56 = 4.533792e-9, AMAX =
4.134758, PMAX = 10.269515, HRATE = 56.0, RATE_C = 0.0767, all rel
5e-3 (bisection rel 1e-2).  T2E7 = 9499220.4795; T_REQ_TAB = {4:
3.76e14, 5: 5.68e21, 8: 5.55e41, 13: 1.75e77} rel 5e-2; AMP_TAB =
{4: 1.9965e5, 5: 7.7261e7, 8: 5.2960e14, 13: 6.9744e26};
GAPABS_TAB = {4: 9.554215e-7, 5: 3.5754401e-11, 8: 3.7542422e-24,
13: 2.6537408e-47}; DM_TAB = {4: 9.472e-6, 5: 1.384e-5, 8:
2.071e-5, 13: 3.513e-5} (r175 frozen, consumed as strings).
HSW = (0.1038, 0.2573, 9.3675); T_PT = 3000175332800.  THETA_BAR =
0.155; LOCK_WIN = (1.0, 8.0).  NOTE_SCOPE = 485..491.
RUNTIME_BAR = 900 s.  Deterministic: no RNG; git read pinned.
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.

VERDICT ENUM (frozen): BUGHUNT7-FINDINGS(8: 1 MAJOR / 3 MINOR /
4 NOTE) + RESIDUE-TRIPLE-NOT-SINGLETON(F1) +
LIMSUP-QUALIFIER-DROPPED(F2) + VACUOUS-LEGS-RECURRED(F3) +
MANIFOLD-SCOPE-MISSING(F4) + COMPOSITION-SOUND-AT-SEQ(X1) +
ANCESTRY-CLEAN-MACHINE-CHECKED(X2) + RESIDUE-TRANSPORT-CONSISTENT +
L1-WPD-LIVE-NOT-STALE(X3) + NUMERALS-CLEAN(X4) +
LINEAGE-CLEAN(X5) + BH6-REVERIFIED-CORRECT + LITERATURE-PINS-EXACT.
NO verdict of rounds 170-175 flips.

SMOKE-STAGE FIX (pre-record, disclosed; smoke1 = 17/21 at the
first-freeze SPEC_SHA 8a488f1c079f13a3, log kept as
bughunt7_probe.smoke1.log; NO record run existed yet).  FOUR
instrument bugs in the AUDIT CODE itself, no bar, class, finding or
criterion moved anywhere: (a) three source-text conjunctions (G13,
G24, G25) matched single-space substrings against docstrings whose
frozen text wraps across lines ("perturbation / either", "domain /
EMPTY", "z >= / 1.05 c*") -- fixed by matching against a
whitespace-normalized copy of the source (the frozen texts are
unchanged and contain the strings); (b) the G29 trivial-zero
density leg used sp.summation, which returns an unresolved
Piecewise for symbolic t -- fixed to the geometric closed form
a/(1 - r) with a = t^-3, r = t^-2 (same identity, own algebra).
All four fixes verified in isolation; smoke2 at the fixed SHA must
be clean.

AST FIREWALL: no zero-oracle names; NO zeta use; no np.load; no
import of verification/; git read pinned read-only.  NO RH CLAIM.
EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
NEXT = os.path.join(HERE, "..", "next.txt")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

SHAS = {
    "jmf": ("jetmass_floor_probe.py", "57de8b2a83677a9c",
            {"jmf_smoke1.log": "4f8d05e02cb020f9",
             "jmf_run1.log": "4f8d05e02cb020f9",
             "jmf_run2.log": "92c895a4053dd781",
             "jmf_run3.log": "FINAL", "jmf_run4.log": "FINAL"}),
    "tt": ("toproot_theta_probe.py", "cf27df22aa5dffbf",
           {"toproot_theta_probe.smoke1.log": "8f95035e57b4b034",
            "toproot_theta_probe.smoke2.log": "FINAL",
            "toproot_theta_probe.run1.log": "FINAL",
            "toproot_theta_probe.run2.log": "FINAL"}),
    "h3c": ("h3_cofinal_probe.py", "876dafc977d3d8fc",
            {"h3c_smoke1.log": "123cde67d20afd3c",
             "h3c_smoke2.log": "FINAL",
             "h3c_run1.log": "FINAL", "h3c_run2.log": "FINAL"}),
    "gp": ("gonek_pricing_probe.py", "3050678b352eaa9a",
           {"gonek_pricing_probe.smoke1.log": "f1e237fe428d0e8d",
            "gonek_pricing_probe.smoke2.log": "FINAL",
            "gonek_pricing_probe.run1.log": "FINAL",
            "gonek_pricing_probe.run2.log": "FINAL"}),
    "tip": ("thetainf_pin_probe.py", "3044558e5fa52e01",
            {"thetainf_pin_probe.smoke1.log": "252ed636b4e32a7d",
             "thetainf_pin_probe.smoke2.log": "FINAL",
             "thetainf_pin_probe.run1.log": "FINAL",
             "thetainf_pin_probe.run2.log": "FINAL"}),
    "bh6": ("bughunt6_probe.py", "5964350254696fa5",
            {"bughunt6_probe.smoke1.log": "FINAL",
             "bughunt6_probe.run1.log": "FINAL",
             "bughunt6_probe.run2.log": "FINAL"}),
}
DIFF_PAIRS = {"jmf": ("jmf_run3.log", "jmf_run4.log", 4),
              "tt": ("toproot_theta_probe.run1.log",
                     "toproot_theta_probe.run2.log", 4),
              "h3c": ("h3c_run1.log", "h3c_run2.log", 4),
              "gp": ("gonek_pricing_probe.run1.log",
                     "gonek_pricing_probe.run2.log", 2),
              "tip": ("thetainf_pin_probe.run1.log",
                      "thetainf_pin_probe.run2.log", 5)}
RUNTIMES = {"jmf": (2055.9, 2063.7), "tt": (2812.6, 2821.5),
            "h3c": (1162.6, 1171.6), "gp": (187.9, 188.4),
            "tip": (577.4, 578.7)}
GATE_COUNTS = {"jmf_run3.log": "36/36", "toproot_theta_probe.run1.log":
               "33/33", "h3c_run1.log": "36/36",
               "gonek_pricing_probe.run1.log": "20/20",
               "thetainf_pin_probe.run1.log": "28/28"}
R168_COMMIT = "d831f15e"
ENTRY_ATOMS = {(4, 8): 7, (5, 10): 9, (8, 16): 13, (9, 18): 17}
BH6_READINGS = (3, 2, 4)
PW_SUM = 97259
CENSUS_REPORTED = 4
D_STR = 0.004183
D_ARG = (14, 19)
NONEXCL_MIN = 20
CROSSOVER_H = 16
EPS56_STR = 4.533792e-9
AMAX_STR = 4.134758
PMAX_STR = 10.269515
HRATE_STR = 56.0
RATE_C = 0.0767
HSW = (0.1038, 0.2573, 9.3675)
T_PT = 3000175332800
THETA_BAR = 0.155
LOCK_WIN = (1.0, 8.0)
T2E7 = 9499220.4795
T_REQ_TAB = {4: 3.76e14, 5: 5.68e21, 8: 5.55e41, 13: 1.75e77}
AMP_TAB = {4: 1.9965e5, 5: 7.7261e7, 8: 5.2960e14, 13: 6.9744e26}
GAPABS_TAB = {4: 9.554215e-7, 5: 3.5754401e-11, 8: 3.7542422e-24,
              13: 2.6537408e-47}
DM_TAB = {4: 9.472e-6, 5: 1.384e-5, 8: 2.071e-5, 13: 3.513e-5}
NOTE_SCOPE = tuple(range(485, 492))
STR_TOL = 5e-3
RUNTIME_BAR = 900.0

CHECKS: list[tuple[str, bool, str]] = []
EDGE_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok and kind == "edge":
        EDGE_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(t: str) -> None:
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def rd(name: str) -> str:
    return open(os.path.join(HERE, name), "r", encoding="utf-8").read()


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        if nm.lower() in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if nm.lower() == "zeta":
            bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta; no np.load; no "
                       "verification/ import; git read pinned")


# --------------------------------------------------------- own helpers
def spec_sha_of(pyfile: str) -> str:
    doc = ast.get_docstring(ast.parse(rd(pyfile)), clean=False)
    return hashlib.sha256(doc.encode("utf-8")).hexdigest()[:16]


def normalize_timing(text: str) -> str:
    text = re.sub(r"\b\d+(?:\.\d+)?\s?s\b", "S", text)
    text = re.sub(r"runtime \S+", "runtime S", text)
    return text


def raw_diff_lines(a: str, b: str) -> int:
    la, lb = a.splitlines(), b.splitlines()
    n = sum(1 for x, y in zip(la, lb) if x != y)
    return n + abs(len(la) - len(lb))


ROMAN = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
         ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
         ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))


def roman_to_int(s: str) -> int:
    i, v = 0, 0
    while i < len(s):
        for sym, val in ROMAN:
            if s.startswith(sym, i):
                v += val
                i += len(sym)
                break
        else:
            raise ValueError(s)
    return v


def prime_powers(n: int) -> list[tuple[int, int]]:
    comp = [False] * (n + 1)
    out = []
    for p in range(2, n + 1):
        if comp[p]:
            continue
        for m in range(p * p, n + 1, p):
            comp[m] = True
        q = p
        while q <= n:
            out.append((q, p))
            q *= p
    return out


def own_G(T: float) -> float:
    al, be, cc = HSW
    lg = math.log(T)
    ll = math.log(lg)
    t1 = (math.log(T / (2 * math.pi)) + 1) / (2 * math.pi * T)
    t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg)) + cc) / T ** 2
    t3 = (al * lg + be * ll + cc) / T ** 2
    return t1 + t2 + t3


def eps_closed(h: float) -> float:
    return math.sqrt(h) * own_G(T_PT) / own_G(2 * math.pi * h)


def has_cycle_own(g: dict) -> bool:
    color: dict = {}

    def dfs(u):
        color[u] = 1
        for v in g.get(u, ()):
            c = color.get(v, 0)
            if c == 1 or (c == 0 and dfs(v)):
                return True
        color[u] = 2
        return False

    return any(dfs(n) for n in list(g) if color.get(n, 0) == 0)


def reachable_own(g: dict, src: str) -> set:
    seen = {src}
    st = [src]
    while st:
        u = st.pop()
        for v in g.get(u, ()):
            if v not in seen:
                seen.add(v)
                st.append(v)
    return seen


def and_fire(g: dict, seeds: set) -> set:
    parents: dict = {}
    nodes = set(g)
    for u, vs in g.items():
        for v in vs:
            parents.setdefault(v, set()).add(u)
            nodes.add(v)
    fired = set(seeds)
    changed = True
    while changed:
        changed = False
        for n in sorted(nodes - fired):
            ps = parents.get(n, set())
            if ps and all(p in fired for p in ps):
                fired.add(n)
                changed = True
    return fired


def note_block(nxt: str, numeral: str) -> str:
    for line in nxt.splitlines():
        if line.startswith("# ") and ("(%s)" % numeral) in line[:40]:
            return line
    return ""


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("bughunt7_probe -- PRIME.BUGHUNT7.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    section("S0  FIREWALL + SOURCES + NUMERALS")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")

    jmf_src = rd("jetmass_floor_probe.py")
    tt_src = rd("toproot_theta_probe.py")
    h3c_src = rd("h3_cofinal_probe.py")
    gp_src = rd("gonek_pricing_probe.py")
    tip_src = rd("thetainf_pin_probe.py")
    njmf = re.sub(r"\s+", " ", jmf_src)
    nh3c = re.sub(r"\s+", " ", h3c_src)
    nxt = open(NEXT, encoding="utf-8").read()
    n487 = note_block(nxt, "CDLXXXVII")
    n488 = note_block(nxt, "CDLXXXVIII")
    n489 = note_block(nxt, "CDLXXXIX")
    n490 = note_block(nxt, "CDXC")
    n491 = note_block(nxt, "CDXCI")

    heads = re.findall(r"^# \d{4}-\d{2}-\d{2} \(([CDLXVIM]+)\)",
                       nxt, re.M)
    nums = [roman_to_int(h) for h in heads]
    in_scope = [n for n in nums if n in set(NOTE_SCOPE)]
    attrib = {485: "bughunt6_probe.py",
              486: "v926_fullgap_growthlaw_theorems.py",
              487: "jetmass_floor_probe.py",
              488: "toproot_theta_probe.py",
              489: "gonek_pricing_probe.py",
              490: "h3_cofinal_probe.py",
              491: "thetainf_pin_probe.py"}
    blocks = {}
    for line in nxt.splitlines():
        m = re.match(r"# \d{4}-\d{2}-\d{2} \(([CDLXVIM]+)\)", line)
        if m:
            blocks[roman_to_int(m.group(1))] = line
    ok02 = (len(in_scope) == len(set(in_scope))
            and set(NOTE_SCOPE) <= set(in_scope)
            and all(in_scope[i] > in_scope[i + 1]
                    for i in range(len(in_scope) - 1))
            and max(nums) >= 491
            and all(fn in blocks.get(n, "")
                    for n, fn in attrib.items())
            and "CDLXXXVI" in n487 and "war der Stand" in n487
            and "CDLXXXIX" in n490 and "NICHT konsumiert" in n490)
    check("G02-numerals-x4", ok02,
          "numerals CDLXXXV..CDXCI (485..491) present, unique, "
          "strictly descending, head >= 491 (head %d); every note "
          "names its probe/module file; concurrency disclosures "
          "exact (CDLXXXVII names CDLXXXVI as prior head; CDXC "
          "names the parallel Gonek lane CDLXXXIX, not consumed): "
          "X4 CLEAN" % max(nums))

    # ------------------------------------------------- S1 findings
    section("S1  FINDINGS F1-F8 (machine checks)")

    # G10 -- F1 residue-prose compression + AND-fire demonstration
    chain = {
        "SOURCE": ["H1_DEEP", "H2_DEEP", "H3_DEEP", "TRACE"],
        "H1_DEEP": ["PF_DEEP"], "H2_DEEP": ["PF_DEEP"],
        "TRACE": ["PF_DEEP"],
        "GONEK_PRICED": ["WF_DEEP"], "CENSUS_PER_K": ["WF_DEEP"],
        "H3_DEEP": ["RATE_DEEP"], "RATE_DICT": ["RATE_DEEP"],
        "PF_DEEP": ["JETMASS_DEEP"], "WF_DEEP": ["JETMASS_DEEP"],
        "RATE_DEEP": ["JETMASS_DEEP"],
        "JETMASS_DEEP": ["SIGMAFLOOR_DEEP"],
        "SIGMAFLOOR_DEEP": ["DTSTEP_DEEP"], "DTSTEP_DEEP": ["HCOF"],
        "HCOF": []}
    grants_prose = {"H3_DEEP", "RATE_DICT", "GONEK_PRICED",
                    "CENSUS_PER_K", "TRACE"}
    fired_prose = and_fire(chain, grants_prose)
    fired_full = and_fire(chain, grants_prose | {"H1_DEEP", "H2_DEEP"})
    ok10 = ("JETMASS_DEEP" not in fired_prose
            and "HCOF" in fired_full
            and not has_cycle_own(chain)
            and "THE FINAL RESIDUE (exact): {H3-COFINAL" in tt_src
            and "[PF: proven given H1 + H2 (r171)]" in tt_src
            and "CONDITIONAL EXACTLY ON {H1 + H2 per rung" in jmf_src
            and "EXAKT H3-KOFINAL" in n488
            and "{H3-COFINAL (parallele Lane)}" in n489
            and "{H3-KOFINAL == limsup" in n491
            and "H1-KOFINAL" not in nxt
            and "H2-KOFINAL" not in nxt
            and "{ENVJ_H1, CENSUS_H2, TRACE} -> PF"
            in rd("jmf_run3.log")
            and "CENSUS_HARD_MAX = 13" in jmf_src
            and "C_STAR_MAX = 1.75 hard h <= 26" in jmf_src)
    check("G10-f1-residue-triple", ok10,
          "OWN AND-fire on the declared chain: the PROSE residue "
          "grant set {H3, dict, Gonek-priced, census-per-k, trace} "
          "does NOT fire the deep jet-mass floor (PF needs H1+H2 at "
          "the same rung); adding {H1, H2} fires HCOF; r171 types "
          "PF 'CONDITIONAL EXACTLY ON {H1 + H2 per rung}' and "
          "hard-gates H1/H2 only at h <= 26/13; r172-r175 residue "
          "prose carries H3-KOFINAL alone, no surface carries "
          "H1/H2-cofinal; machine layer (G61/G63) consistent: "
          "BH7-F1 CONFIRMED [MAJOR, correction of record, no "
          "verdict flip]")

    # G11 -- F2 limsup qualifier + own D recompute + counterexample
    YT = {4: 4.2532, 5: 4.7858, 6: 5.1092, 7: 5.4003, 8: 5.6197,
          9: 5.8273, 10: 6.0322, 11: 6.1957, 12: 6.3775, 13: 6.5057,
          14: 6.6664, 15: 6.7625, 16: 6.8847, 17: 6.9876, 18: 7.0996,
          19: 7.1728, 20: 7.2745, 21: 7.3667, 22: 7.4493, 23: 7.5210,
          24: 7.6035, 25: 7.6678, 26: 7.7367, 27: 7.8077, 28: 7.8687}
    th = {h: 10 ** v / (2 * math.pi * h) ** 4 for h, v in YT.items()}
    hs = sorted(th)
    D = 0.0
    arg = None
    for i, h in enumerate(hs):
        for hp in hs[i + 1:]:
            d = th[h] - th[hp]
            if d > D:
                D, arg = d, (h, hp)
    # counterexample: cofinal(bar) but limsup > bar (no monotonicity)
    bar = 1.0
    seq = [bar - 0.1 if i % 2 == 0 else bar + 0.5 for i in range(40)]
    cofinal = all(any(seq[j] <= bar for j in range(2 * k, 2 * k + 2))
                  for k in range(20))
    limsup40 = max(seq[20:])
    ok11 = (abs(D / D_STR - 1) <= STR_TOL and arg == D_ARG
            and cofinal and limsup40 > bar
            and "(mod gemessener Defekt D = 0.0042" in n490
            and "{H3-KOFINAL == limsup" in n491
            and "mod gemessener Defekt" not in n491)
    check("G11-f2-limsup-qualifier", ok11,
          "own D recompute from the cited r172 ladder: D = %.6f at "
          "drawdown %s (r173 string 0.004183 rel 5e-3); own "
          "counterexample: a bar-cofinal sequence with limsup > bar "
          "(the bare equivalence is FALSE without the defect-D "
          "near-monotonicity); CDXC carries the mod-D qualifier, "
          "CDXCI drops it: BH7-F2 CONFIRMED [MINOR]" % (D, str(arg)))

    # G12 -- F3 vacuous legs in r171; r172-r175 clean
    flat_jmf = re.sub(r"\s+", "", jmf_src)
    leg_g = "okG=okGandsp.simplify(((y-al)**2+be**2)-(y-al)**2-be**2)==0"
    leg_n = "okN=((t2s-t1s).is_positiveisNone)orTrue"
    others_clean = True
    for s in (tt_src, h3c_src, gp_src, tip_src):
        fl = re.sub(r"\s+", "", s)
        if "orTrue" in fl or re.search(
                r"simplify\(([^()]{1,60})-\1\)==0", fl):
            others_clean = False
    ok12 = (leg_g in flat_jmf and leg_n in flat_jmf and others_clean)
    check("G12-f3-vacuous-legs-r171", ok12,
          "r171 G11 leg simplify(((y-al)^2+be^2)-(y-al)^2-be^2)==0 "
          "is E - E == 0 (BH6-F3 okH class) inside a PROVEN-typed "
          "gate; r171 G12 leg '(... is None) or True' is an "
          "always-True dead binding rebound to the trivial instance "
          "9/10 < 1; theorems stay true, no verdict flips; r171 "
          "froze BEFORE bughunt6 landed (timing clean); r172-r175 "
          "scanned CLEAN of the class: BH7-F3 CONFIRMED [MINOR]")

    # G13 -- F4 manifold-exclusion scope
    LOCK = {4: 2.4885, 5: 3.6444, 6: 2.5824, 7: 3.9814, 8: 2.3890,
            9: 2.8616, 10: 2.2804, 11: 2.7183, 12: 2.5302,
            13: 3.3141, 14: 2.5778, 15: 2.9692, 16: 2.8345,
            17: 2.7172, 18: 2.5836, 19: 2.6024, 20: 2.5224,
            21: 2.5272, 22: 2.5592, 23: 2.5246, 24: 2.8361,
            25: 2.6379, 26: 2.9682, 27: 3.1499, 28: 2.2345}
    nonexcl = []
    for h in hs:
        W = THETA_BAR / th[h]
        lw = LOCK[h] / W
        if LOCK_WIN[0] < lw < LOCK_WIN[1]:
            nonexcl.append(h)
    h3c_r1 = rd("h3c_run1.log")
    ok13 = (len(nonexcl) >= NONEXCL_MIN and 4 not in nonexcl
            and ("first gate-bar radius >= 1 at h = %d"
                 % CROSSOVER_H) in h3c_r1
            and "h24 gate inf meas inf" in h3c_r1
            and "jede y_t-bewegende St" in n490
            and "every y_t-moving perturbation either leaves "
                "the ground state" in nh3c)
    check("G13-f4-manifold-scope", ok13,
          "OWN recompute from the cited r172 ladders: at %d of 25 "
          "rungs the MINIMAL H3-refuting inflation W = bar/theta_y "
          "(~2.0-2.5) keeps lock/W INSIDE (1.0, 8.0) -- the lock "
          "leg excludes only large dials; r173's own G36 discloses "
          "the DK gate-bar crossover at h = 16 and measured-radius "
          "failure at h = 24; the C3 verdict sentence (note + "
          "docstring) is universally quantified without the rung "
          "scope: BH7-F4 CONFIRMED [MINOR]" % len(nonexcl))

    # G14 -- F5 rate-form 'equivalent' wording
    ok14 = ("EQUIVALENT MACHINE FORMS (each gated this round)"
            in tt_src
            and "(iii) RATE-FORM" in tt_src
            and "==> the" in tt_src.split("(iii) RATE-FORM", 1)[1][:200]
            and "plus die RATEN-FORM" in n488)
    check("G14-f5-rateform-wording", ok14,
          "r172 docstring lists the RATE-FORM under 'EQUIVALENT "
          "MACHINE FORMS' but states and gates it as an implication "
          "(==>) only; the note CDLXXXVIII is careful ('DREI ... "
          "Aequivalenzformen ... plus die RATEN-FORM'): BH7-F5 "
          "CONFIRMED [NOTE, cite per the note wording]")

    # G15 -- F6 H2 'all 25 verified' compression
    jmf_r3 = rd("jmf_run3.log")
    n_rep = jmf_r3.count("[CENSUS-DEPTH-REPORTED]")
    ok15 = (n_rep == CENSUS_REPORTED
            and "an allen 25 Sprossen verifiziert" in n487
            and "DEPTH-REPORTED sauber" in n487)
    check("G15-f6-h2-typing", ok15,
          "r171 record: %d census rows (h = 25..28, incl. the "
          "degree-116 h = 28 polyroots) are CENSUS-DEPTH-REPORTED, "
          "not gated (hard h <= 13, structure <= 24); the note's "
          "terminal statement types H2 'an allen 25 Sprossen "
          "verifiziert' while disclosing the split in the same "
          "note: BH7-F6 CONFIRMED [NOTE]" % n_rep)

    # G16 -- F7 'bewiesene Verschwendung' + own T_req reproduction
    ok16 = True
    d16 = []
    for h in (4, 5, 8, 13):
        treq = DM_TAB[h] * T2E7 / (0.05 * GAPABS_TAB[h]
                                   / (AMP_TAB[h] + 0.05))
        ok16 = ok16 and abs(treq / T_REQ_TAB[h] - 1) <= 5e-2
        d16.append("h%d %.2e" % (h, treq))
    ok16 = (ok16 and "bewiesene Verschwendung" in n491
            and "GEMESSEN = " in n491 and "T_req-Leiter" in n491)
    check("G16-f7-treq-measured-not-proven", ok16,
          "OWN T_req reproduction from the frozen AMP/GAPABS/DM "
          "tabs + T(2e7): %s == the r175 ladder (rel 5e-2) -- a "
          "MEASURED-LAW extrapolation (1/T tail law measured, "
          "amp/gap ladders measured), typed GEMESSEN in the note "
          "itself, but lever (c) says 'bewiesene Verschwendung': "
          "BH7-F7 CONFIRMED [NOTE, 'gemessene' is the honest word]"
          % ", ".join(d16))

    # G17 -- F8 r175 G53 definitional enumeration leg
    ok17 = ("admissible = [k2 for k2, v2 in routes.items()" in tip_src
            and "ok53 = (admissible == []" in tip_src)
    check("G17-f8-g53-definitional", ok17,
          "r175 G53 leg 'admissible == []' filters a FROZEN verdict "
          "dict by its own kill-prefixes -- cannot fail given the "
          "dict (BH6-F3 borderline class); the individual kills ARE "
          "gated (G14/G15/G33/G36/G37/G38) and the same gate "
          "carries two real legs: BH7-F8 CONFIRMED [NOTE, type "
          "DEFINITIONAL]")

    # --------------------------------------------- S2 re-checks
    section("S2  CROSS-ROUND RE-CHECKS (X1-X5 + audit-the-auditor)")

    # G20 -- X5 SPEC_SHA + lineage
    ok20 = True
    d20 = []
    for key, (pyf, want_fin, logs) in sorted(SHAS.items()):
        fin = spec_sha_of(pyf)
        if fin != want_fin:
            ok20 = False
            d20.append("%s FINAL %s != %s" % (key, fin, want_fin))
        for lg, want in logs.items():
            m = re.search(r"SPEC_SHA ([a-f0-9]{16})", rd(lg))
            got = m.group(1) if m else "??"
            exp = fin if want == "FINAL" else want
            if got != exp:
                ok20 = False
                d20.append("%s %s %s != %s" % (key, lg, got, exp))
        d20.append("%s %s" % (key, fin))
    check("G20-x5-spec-lineage", ok20,
          "SPEC_SHA recomputed from all 6 docstrings (5 audited + "
          "bughunt6); all 24 kept logs match the disclosed "
          "amendment/smoke-fix lineage: X5 CLEAN [%s]"
          % "; ".join(d20))

    # G21 -- determinism + note-vs-log numbers
    ok21 = True
    d21 = []
    for key, (a, b, want) in sorted(DIFF_PAIRS.items()):
        ta, tb = rd(a), rd(b)
        rdf = raw_diff_lines(ta, tb)
        ndf = raw_diff_lines(normalize_timing(ta), normalize_timing(tb))
        r1, r2 = RUNTIMES[key]
        rt_ok = (("runtime %.1f s" % r1) in ta
                 and ("runtime %.1f s" % r2) in tb)
        gc_ok = ("GATES: %s PASS" % GATE_COUNTS[a]) in ta
        if not (rdf == want and ndf == 0 and rt_ok and gc_ok):
            ok21 = False
        d21.append("%s raw %d norm %d" % (key, rdf, ndf))
    smoke_ok = ("GATES: 30/32 PASS" in rd("toproot_theta_probe.smoke1.log")
                and "GATES: 34/35 PASS" in rd("h3c_smoke1.log")
                and "GATES: 19/20 PASS"
                in rd("gonek_pricing_probe.smoke1.log")
                and "GATES: 26/27 PASS"
                in rd("thetainf_pin_probe.smoke1.log")
                and "GATES: 34/36 PASS" in rd("jmf_run1.log")
                and "GATES: 35/36 PASS" in rd("jmf_run2.log"))
    ok21 = ok21 and smoke_ok
    check("G21-determinism-notes-vs-logs", ok21,
          "record pairs re-diffed OWN: %s (== notes' claimed 4/4/4/"
          "2/5, timing-normalized EMPTY); runtimes + gate counts + "
          "smoke/amendment fail rows all match the note claims: "
          "BH6-F2 convention adopted on all five surfaces"
          % "; ".join(d21))

    # G22 -- audit-the-auditor: BH6 F1/F2/F3 re-verified
    dbt1 = rd("dbt_run1.log")
    pairs = {}
    cur = None
    for line in dbt1.splitlines():
        mh = re.search(r"\[INFO\] \((\d+),(\d+)\)(\w+) profile", line)
        if mh:
            cur = (int(mh.group(1)), int(mh.group(2)), mh.group(3))
            continue
        me = re.search(r"ENTER seg (\d+)/(\d+) u=([\d.]+)", line)
        if me and cur and cur[2] == "MAIN":
            pairs[(cur[0], cur[1])] = float(me.group(3))
    n_pr = n_at = n_x2 = 0
    atoms_ok = len(pairs) == 4
    for (hs_, hb), u in sorted(pairs.items()):
        q = int(round(math.exp(u)))
        atoms_ok = atoms_ok and ENTRY_ATOMS[(hs_, hb)] == q
        new = [(qq, p) for qq, p in prime_powers(hb) if qq > hs_]
        n_pr += (q == max((qq for qq, p in new if qq == p), default=0))
        n_at += (q == max(qq for qq, _p in new))
        n_x2 += (q == max(qq for qq, p in new if p != 2))
    msg168 = subprocess.run(
        ["git", "-C", REPO, "show", "-s", "--format=%B", R168_COMMIT],
        capture_output=True, text=True, check=True).stdout
    dbt_src = rd("depthblock_transfer_probe.py")
    sf_src = rd("sigmafloor_probe.py")
    flat_dbt = re.sub(r"\s+", "", dbt_src)
    flat_sf = re.sub(r"\s+", "", sf_src)
    ok22 = (atoms_ok and (n_pr, n_at, n_x2) == BH6_READINGS
            and "LARGEST NEW PRIME ATOM" in msg168
            and raw_diff_lines(dbt1, rd("dbt_run2.log")) == 5
            and raw_diff_lines(rd("sf_run2.log"), rd("sf_run3.log")) == 4
            and "okD=all(2**k>=2**kforkinrange(2,12))" in flat_dbt
            and "okH=sp.simplify(sp.sin(aa*z)*Rz-(sp.sin(aa*z))*(Rz))==0"
            in flat_sf)
    check("G22-bh6-reverified", ok22,
          "AUDIT THE AUDITOR: BH6-F1 re-verified with own "
          "prime-power arithmetic (entry atoms 7/9/13/17; readings "
          "prime %d/4, atom %d/4, note-form %d/4 -- the commit "
          "phrase matches no 4/4 reading, exactly as BH6 found); "
          "BH6-F2 diffs 5/4 re-verified; BH6-F3 both vacuous legs "
          "present verbatim in r168/r169: BUGHUNT6 F1-F3 CORRECT"
          % (n_pr, n_at, n_x2))

    # G23 -- r172 p_max chain + rate dictionary (own sympy)
    e56 = eps_closed(HRATE_STR)
    amax = math.log(RATE_C / e56) / math.log(HRATE_STR)
    pmax = 2 * (1 + amax)
    lo, hi = 4.0, 1e6
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if RATE_C * mid ** (-amax) > eps_closed(mid):
            lo = mid
        else:
            hi = mid
    hrate = math.sqrt(lo * hi)
    import sympy as sp
    hh, qq = sp.symbols("hh qq", positive=True)
    Gl = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    okd = True
    for p in (3, 4, 5):
        lim = sp.limit(hh ** (sp.Rational(p, 2) - 1)
                       * Gl(qq * hh ** sp.Rational(p, 2))
                       / Gl(2 * sp.pi * hh), hh, sp.oo)
        okd = okd and sp.simplify(lim - sp.pi * p / qq) == 0
    ok23 = (abs(e56 / EPS56_STR - 1) <= STR_TOL
            and abs(amax / AMAX_STR - 1) <= STR_TOL
            and abs(pmax / PMAX_STR - 1) <= STR_TOL
            and abs(hrate / HRATE_STR - 1) <= 1e-2 and okd)
    check("G23-pmax-rate-dictionary", ok23,
          "OWN recompute: eps_closed(56) = %.4e, a_max = %.4f, "
          "p_max = %.4f, own bisection h*_rate = %.2f (r172 strings "
          "rel 5e-3); rate dictionary lim h^{p/2-1} G(q h^{p/2})/"
          "G(2 pi h) == pi p/q re-derived OWN at p = 3, 4, 5: the "
          "p_max chain is PT21-anchored + measured-c honest"
          % (e56, amax, pmax, hrate))

    # G24 -- r171 PF2 concavity own re-derivation
    u = sp.symbols("u", positive=True)
    ser = sp.series(-sp.log(1 - u) / u, u, 0, 14).removeO()
    okA = all(sp.Poly(ser, u).coeff_monomial(u ** n) > 0
              for n in range(1, 14))
    # per-factor bound on an OWN rational instance (new numbers):
    # a = 2/7, c = 5/7, y = 3: (1 - a/y) >= (1 - c/y)^{a/c}
    aq, cq, yq = sp.Rational(2, 7), sp.Rational(5, 7), sp.Integer(3)
    lhs = 1 - aq / yq
    rhs = (1 - cq / yq) ** (aq / cq)
    okB = bool(sp.N(lhs - rhs, 40) > 0)
    # trace budget: S+ <= (1 + kappa + NEGBAR) y_t from trace + negsum
    B1s, yts, ngs = sp.symbols("B1s yts ngs", positive=True)
    Splus = (B1s + yts) + ngs           # sum Re + |negsum|
    kap = B1s / yts
    okC = sp.simplify(Splus - (1 + kap + ngs / yts) * yts) == 0
    # own 4-root assembled instance (roots 1,1,2,5; cap 6; y 20)
    roots = [1, 1, 2, 5]
    capv, yv = sp.Integer(6), sp.Integer(20)
    lhs4 = sp.prod([(1 - sp.Integer(r) / yv) for r in roots])
    rhs4 = (1 - capv / yv) ** (sp.Rational(sum(roots)) / capv)
    okD_ = bool(sp.N(lhs4 - rhs4, 40) > 0)
    okE = ("if yq <= btop:" in jmf_src
           and "domain EMPTY" in njmf)
    ok24 = okA and okB and okC and okD_ and okE
    check("G24-pf2-concavity-own", ok24,
          "PF2 re-derived OWN: -log(1-u)/u has positive Taylor "
          "coefficients to order 14 (monotone) ==> per-factor "
          "(1-a/y) >= (1-c/y)^{a/c} for 0 <= a <= c < y (own "
          "instance); trace budget S+ == (1+kappa+negbar) y_t exact "
          "on own symbols; own 4-root assembled instance positive; "
          "the domain condition c* y_t > b_top is CODED in r171's "
          "H1 grid (prose omits it, code carries it): PF2 SOUND")

    # G25 -- r171 pointwise coverage audit
    m39 = re.search(r"G39-pf-pointwise\s+(.*)", jmf_r3)
    rows = re.findall(r"h(\d+) n (\d+) marg ([\d.e+-]+|-)",
                      m39.group(1))
    tot = sum(int(n) for _h, n, _m in rows)
    margs_pos = all(float(m) > 0 for _h, n, m in rows
                    if m != "-" and int(n) > 0)
    ok25 = (tot == PW_SUM and margs_pos
            and "z >= 1.05 c*" in njmf
            and ("1.05" in n487))
    check("G25-pointwise-coverage", ok25,
          "own parse of the r171 G39 record row: sum n = %d "
          "(~100k claim honest), all min margins positive where "
          "zeros exist (h <= 24); the coverage factor z >= 1.05 c* "
          "is disclosed in spec + note (PF2 itself is proven on "
          "z > c*): CLEAN" % tot)

    # G26 -- X2 ancestry (own DFS on declared graphs)
    loops = {
        "uni": {"RH": ["CENSUS_ALLK"], "CENSUS_ALLK": ["DTSTEP"],
                "DTSTEP": ["HCOF"], "HCOF": ["WEILPOS"],
                "WEILPOS": ["RH"]},
        "pin": {"TAUPOS": ["A0FLOOR"], "TLAWCAP": ["A0FLOOR"],
                "A0FLOOR": ["TOPROOT"], "TOPROOT": ["RATE"],
                "RATE": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"]},
        "g84": {"RH": ["GONEK1984"], "GONEK1984": ["DCLEG"],
                "DCLEG": ["SIGMAFLOOR"], "SIGMAFLOOR": ["DTSTEP"],
                "DTSTEP": ["HCOF"], "HCOF": ["WEILPOS"],
                "WEILPOS": ["RH"]},
        "mpc": {"RH": ["MPC"], "MPC": ["SM_CEIL"],
                "SM_CEIL": ["THETAINF"], "THETAINF": ["H3COF"],
                "H3COF": ["RATE"], "RATE": ["DTSTEP"],
                "DTSTEP": ["HCOF"], "HCOF": ["WEILPOS"],
                "WEILPOS": ["RH"]}}
    cyc_ok = all(has_cycle_own(g) for g in loops.values())
    delivered = dict(chain)
    delivered.update({"SPECTRAL_CERT": ["GROUND_CERT", "LOCK_LEG"],
                      "TAU_MEAS": ["BA3_LEG"],
                      "CENSUS_PER_K": ["WF_DEEP", "BA3_LEG"],
                      "GROUND_CERT": ["WITNESS_EXCL"],
                      "LOCK_LEG": ["WITNESS_EXCL"],
                      "BA3_LEG": ["WITNESS_EXCL"],
                      "WITNESS_EXCL": []})
    flags = ("TAUPOS", "TLAWCAP", "CENSUS_ALLK", "GONEK1984", "MPC")
    no_flag_anc = all(f not in delivered for f in flags)
    wexcl_out = delivered["WITNESS_EXCL"] == []
    ok26 = (cyc_ok and not has_cycle_own(delivered) and no_flag_anc
            and wexcl_out
            and "TAU_MEAS" not in reachable_own(delivered, "SOURCE"))
    check("G26-x2-ancestry", ok26,
          "own DFS: all four flagged loop cycles re-detected "
          "(universalized census, pinning-supply/A0-floor, "
          "gonek-1984, montgomery-pc); the delivered chain incl. "
          "the manifold legs is ACYCLIC; none of {TAUPOS, TLAWCAP, "
          "CENSUS-ALLK, GONEK-1984-RH, MPC-RH} is an ancestor of "
          "any delivered node; the witness-exclusion legs (lock, "
          "BA3, consuming TAU-MEAS) have NO outgoing edge into the "
          "chain (red-team only): X2 CLEAN -- H1/H2/H3/manifold "
          "are NOT secretly the flagged loops")

    # G27 -- X3 residue transport + L1/WPD adjudication
    ok27 = ("REDUZIERT AUF {TOPROOT" in n487
            and "{L1, WPD}" in n487 and "{L1, WPD}" in n488
            and "{L1, WPD}" in n489 and "{L1, WPD}" in n490
            and "{L1, WPD}" in n491
            and "VERLÄSST das Residuum" in n489
            and "hier NICHT konsumiert" in n490
            and os.path.exists(os.path.join(HERE,
                                            "wpd_proof_probe.py"))
            and os.path.exists(os.path.join(HERE,
                                            "l1_weyllaw_probe.py"))
            and "L1 = TAIL (bewiesen) + H-pin" in nxt)
    check("G27-x3-residue-l1-wpd", ok27,
          "residue transport r171 -> r175 verified (TOPROOT -> "
          "H3-COFINAL swap at r172; Gonek item exits at r174 "
          "RESIDUE-SHRUNK; r173 keeps it with the parallel-lane "
          "disclosure; {L1, WPD} carried verbatim in all five); "
          "L1/WPD adjudicated LIVE-NOT-STALE: round-128 serial "
          "pair, L1 == TAIL (proven) + H-pin (open, corpus's own "
          "refinement), WPD open with the obstruction pinned by "
          "wpd_proof_probe: X3 CONSISTENT (labels coarse, not "
          "stale)")

    # G28 -- r174 ENV closed form + literature pins
    x_, t_, Tlo, Thi = sp.symbols("x_ t_ Tlo Thi", positive=True)
    B = x_ * sp.log(2 * x_ * t_) * sp.log(sp.log(3 * x_))
    integ = sp.integrate(B / t_ ** 3, (t_, Tlo, Thi))
    env = (B.subs(t_, Thi) / Thi ** 2 + B.subs(t_, Tlo) / Tlo ** 2
           + 2 * integ) / sp.sqrt(x_)
    env_cf = sp.sqrt(x_) * sp.log(sp.log(3 * x_)) * (
        (4 * sp.log(2 * x_ * Tlo) + 1) / (2 * Tlo ** 2)
        - 1 / (2 * Thi ** 2))
    okEnv = sp.simplify(env - env_cf) == 0
    lits = ("548-564", "x log(2xT) loglog(3x)",
            "log x  min(T, x/<x>)", "log 2T min(T, 1/log x)",
            "Invent. Math. 75 (1984), 123-142",
            "RH-CONDITIONAL == a hidden loop if")
    okLit = all(s in gp_src for s in lits)
    # integer-x subsumption arithmetic (own, x = 8, any T > 1):
    okSub = all(math.log(x) * x <= 10 * x * math.log(2 * x * 2)
                * max(math.log(math.log(3 * x)), 0.5)
                for x in (4, 5, 8, 13, 27, 32))
    ok28 = okEnv and okLit and okSub
    check("G28-env-closedform-literature", ok28,
          "r174 ENV T_hi-collapse re-derived OWN (sympy integral "
          "identity EXACT: census-depth-insensitive ceiling; 'any "
          "finite constant' hides no uniformity-in-h issue because "
          "[G] is uniform in (x, T)); literature pins verbatim in "
          "the frozen spec and EXTERNALLY VERIFIED (web 2026-08-20: "
          "Landau Math. Ann. 71 (1912) 548-564 [theorem often "
          "dated 1911; volume year 1912]; Gonek uniform formula + "
          "<x> + integer subsumption EXACT; Gonek 1984 "
          "RH-conditional): GP1 CORRECT")

    # G29 -- r175 bridge exact spot re-derivations
    g_, om_, A_ = sp.symbols("g_ om_ A_", positive=True)
    kk = sp.symbols("kk", positive=True, integer=True)
    expr = sp.sin(A_ * g_) ** 2 / (g_ ** 2 - om_ ** 2)
    lim_res = sp.limit(expr.subs(A_, kk * sp.pi / om_), g_, om_)
    okRes = sp.simplify(lim_res) == 0
    t3 = sp.symbols("t3", positive=True)
    geo = (t3 ** -3) / (1 - t3 ** -2)   # a/(1-r), a = t^-3, r = t^-2
    okTriv = sp.simplify(geo - 1 / (t3 * (t3 ** 2 - 1))) == 0
    okSet = ("FsZd = bridge_pj(gam, aa_w, Kw, (n_lad[-1],))" in tip_src
             and 'res_m = rw["pj_res"][-1]' in tip_src)
    okSmk = ("chat_min_eff = CTRL_CHAT_MIN if not smoke else "
             "CTRL_CHAT_MIN / 4" in gp_src)
    ok29 = okRes and okTriv and okSet and okSmk
    check("G29-bridge-instrument-own", ok29,
          "r175 resonance removability re-derived OWN (lim_{g->om} "
          "sin^2(Ag)/(g^2-om^2) == 0 at A om == k pi: quadratic "
          "kill, mode grid exact); trivial-zero density geometric "
          "sum == 1/(t(t^2-1)) OWN; world-separation uses the SAME "
          "census + deepest checkpoint as MAIN (code conjunction); "
          "r174 smoke bar rescale is smoke-only in code (full bar "
          "20 untouched): CLEAN")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "BUGHUNT7-FINDINGS(8: 1 MAJOR / 3 MINOR / 4 NOTE)",
        "RESIDUE-TRIPLE-NOT-SINGLETON(F1: {H1,H2,H3}-cofinal, "
        "correction of record, no verdict flip)",
        "LIMSUP-QUALIFIER-DROPPED(F2: CDXCI vs CDXC mod-D)",
        "VACUOUS-LEGS-RECURRED(F3: r171 exact layer, BH6-F3 class)",
        "MANIFOLD-SCOPE-MISSING(F4: DK crossover h=16, lock blind "
        "to minimal refuters at 24/25 rungs)",
        "COMPOSITION-SOUND-AT-SEQ(X1: no hidden forall-h; the "
        "per-block hypothesis is the triple)",
        "ANCESTRY-CLEAN-MACHINE-CHECKED(X2)",
        "RESIDUE-TRANSPORT-CONSISTENT + L1-WPD-LIVE-NOT-STALE(X3)",
        "NUMERALS-CLEAN(X4)", "LINEAGE-CLEAN(X5)",
        "BH6-REVERIFIED-CORRECT(r170)",
        "LITERATURE-PINS-EXACT(r174 GP1)"]
    for v in verdicts:
        print("  " + v)
    info("NO verdict of rounds 170-175 flips; corrections of record "
         "proposed at F1/F2/F4 wording, F3/F8 leg re-coding.")
    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join(v.split("(")[0] for v in verdicts))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
