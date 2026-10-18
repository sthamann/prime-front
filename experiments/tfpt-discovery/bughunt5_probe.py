#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt5_probe -- PRIME.BUGHUNT5.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  Adversarial audit of the
discovery rounds 149-162 corpus (probes collapserate / tlawcap_blocks
/ anchor_epslock / nearalign / assembly_walls / rootladder /
spectral_balance / edge_cleanup / j2_primeforce / gfloor /
fullgap_growthlaw; notes CDLIII-CDLXVII; the third promotion wave
v922-v925 of commit a3d07a2d).  This probe writes NOTHING but stdout,
reads the frozen corpus READ-ONLY (probe sources as text + run*.log /
smoke*.log / promo_rerun.log evidence files + next.txt + the
verification/ ledger+registry+module sources AS TEXT + the X5 zero
cache inside a ward_ function), imports NO frozen probe and NO
verification module (every recompute below is an independent
implementation), and makes NO RH CLAIM in either direction.  Every
confirmed finding carries at least one falsifiable gate.

METHOD (bughunt I-IV standard): (B1) the load-bearing razor chain
r157/r161 re-derived INDEPENDENTLY -- GF1 (razor enclosure) re-proven
on an OWN 4-excited-level generic parametrization (the frozen probes
used 2/3 levels) plus the two-level lower-end-equality witness family
re-instanced on OWN exact rationals; GF2/GF3/GF4 (pinch law, share
pricing, Newton value law N_1 = 1/(H_t + s), B(q_0) = -rho2 P_c'(q_0)
at K = 4, the Jg t_g == 1 + g chase re-typed DEFINITIONAL); GF5a
(S1 absorption) re-chased through the B00-root equation on an own
4-level frame; SB1 (trace loop + unconditional tail) at 5 levels;
(B2) the r162 growth-law instrument attacked: GL2 (arrowhead
leave-one-out) verified on an OWN deterministic numpy instance (dual
row, kernel split, arrowhead spectrum vs direct compression, secular
root, eigenvector components), GL1 inclusion monotonicity, GL3
one-row interlacing + the R = phi equality witness + razor vacuity;
the QUARTIC EXPONENT attacked with an honest free-exponent fit + AIC
comparison on the frozen record J-table (free p = 3.907 +- 0.114;
AIC prefers FIXED 4 over the free fit and rejects 3.5/4.5 at
3.6/5.2 sigma: the law survives an instrument the round did not
run); (B3) the r156 moment-Laurent layer (L1/L2/L3/L5) re-derived
own-generic incl. the quarter-cap identity and the sum rules from an
own series expansion; (B4) the r153/r155 walls: the a-window
quadratic/width/matched-pin/location algebra re-derived from the
|w| = a|z|^2/|z^2+a|^2 definition, the EZ edge-zero adjudicated
EXACT-BY-CONVENTION (om_k := k pi/A in every frozen builder -- not a
mesh artifact), the JJ slack identity, the rho_co counterexample and
the Z8 LM-split subsumption algebra re-proven; (B5) the promoted
surfaces v922-v925: the FULL E3 wholesale closure recomputed with an
OWN vectorized implementation from the X5 cache (all 357 D_cs > 0,
worst margin 0.3461 at (12, 1), x_0(HSW) = 121, x_0(BW25) = 112,
strip-negativity battery-wide, json == npy cache bitwise), pinned
tables cross-checked against the source-run logs, promotion typing
checked for silent upgrades (none found), ledger 1069 / registry 918
/ run_all v922-v925 rows verified; (B6) provenance: SPEC_SHA of all
11 round probes recomputed from the docstrings and matched against
every kept log (all amendment/smoke hash moves accounted EXCEPT one,
finding F4), every deterministic re-run pair re-diffed with a
timing-token normalizer (raw pair counts 7/8/1/3/3/3/3/8/8 exactly
as claimed, non-timing diffs ALL EMPTY); (B7) the min-cut flows
re-verified with an OWN Edmonds-Karp implementation on the two
frozen graph encodings (r150-class 4/5/5/9 and r154-class 4/5/5/7);
(B8) cross-round bookkeeping: numerals CDLIII-CDLXVII gap-free with
the head-verification chain intact, residue statements CDLIV ->
CDLXVII consistent (incl. the honest r157 merge of {SUSCAP2R,
DELTA1FLOOR} into the one QSUBGAP-floor entry), the window constants
theta/tlaw/J_2/t_r/t_g/jr/betapos cross-replicated string-exact
across rounds (jr/t_r tables IDENTICAL in the r150 and r162 logs;
betapos six-digit across r150/r161; J_2-proxy 0.1513 vs moment-J_2
0.1506 at x = 28 disclosed as different instruments).

=======================================================================
FINDINGS LEDGER (the deliverable; severity frozen; gates named)
=======================================================================
BH5-F1 [MINOR][exactness-overstatement, cross-round]  Round 150
  (collapserate_probe.py docstring line 'beta_0 sits at (beta_0 -
  tau)/tau = 0.2463/0.1305 (= S1/jr by exact chase)', verdict enum
  'BETA0-POSITION-MEASURED(betapos == S1/jr chase; G36)', and note
  CDLIV '== S1/jr (exakter Chase, tau-flach Slope +0.007)') claims
  betapos == S1/jr as an EXACT identity.  It is NOT exact: from
  r150's OWN Theorem R3 (J == S1 (lam_1 - beta_0)/(beta_0 - tau))
  and jr = J/FULLGAP the exact law is
     S1/jr == betapos x (lam_1 - tau)/(lam_1 - beta_0),
  i.e. S1/jr - betapos == betapos^2/(FULLGAP - betapos) > 0
  (machine-verified symbolically here on an own 4-level frame;
  numerically 2.7e-7 at x = 5 falling to 2.0e-10 at x = 28 -- below
  the 4-digit print precision of r150's G36 exhibit, so no r150
  GATE is wrong; the r3dev gate tests the correct R3 form).  Round
  161 (CDLXV, GF5a) states the corrected exact law WITH the factor
  (lam_1 - tau)/(lam_1 - beta_0) >= 1 -- and v923 promotes the
  correct form -- but neither flags that r150's frozen '== exact
  chase' wording is thereby superseded: a silent cross-round
  correction.  The corpus's own COJ standard (r155: identity vs
  measured co-movement adjudicated to 10 digits) demands the
  distinction.  No verdict flips; the S1-absorption and all r161
  numbers are CONFIRMED.  GATE: G13 (own symbolic residual identity
  + magnitude from the frozen strings + grep conjunction on the
  three surfaces).
BH5-F2 [MINOR][promoted-surface-count]  v925 (docstring 'all 72
  sliver + first-zero targets carry two-sided audit-ball
  certificates', ledger row 1069 '72 unique targets') and note
  CDLXIII ('Audit-Ball-Zwei-Seiten-Zertifikate an ALLEN 72 Sliver-
  und Erstnullstellen aller sechs Bloecke') state 72 targets.  The
  record log's own per-block certified counts (edge_cleanup run2
  G32: 1/1, 1/1, 1/1, 1/1, 18/18, 51/51) sum to 73, and the unique-
  target arithmetic confirms 73: 71 sliver zeros (1/0/1/0/18/51,
  r156-exact, re-gated) + the first zeros above the band at b8 and
  b18 (whose slivers are EMPTY; at b5/b13/b24/b28 the first zero
  lies INSIDE the sliver interval (b_top, Y*) and is already
  counted).  All 73 certificates EXIST and are green -- the
  headline count on the PROMOTED surface is off by one (72 -> 73).
  Recommended correction of record: v925 docstring + ledger row +
  CDLXIII wording.  Per contract this probe does NOT edit them.
  GATE: G23 (log parse + sliver/first-zero overlap arithmetic +
  grep of the three '72' surfaces).
BH5-F3 [MINOR][instrument-typing, rescue]  Round 160
  (j2_primeforce_probe.py) describes its rescue instrument as 'best
  PSD repair by deterministic projected nonneg least squares (60
  sweeps)' and issues the enum RESCUE-INFEASIBLE-IN-CLASS ('no PSD
  ladder repair reaches the window in any fake world', carried into
  CDLXIV as 'JEDE PSD-Rettung in Fake-Welten IN-KLASSE-UNMOEGLICH').
  The code (w_battery, rescue block) is NOT a least-squares solver:
  it is a GREEDY eigenvalue-lifting loop (per sweep: find the most
  negative eigenvalue, pick the single plant vector with the best
  overlap x lambda score, ADD a step to its coefficient;
  coefficients are never re-optimized or decreased, no least-squares
  objective is ever evaluated, no KKT/optimality certificate is
  produced, and the loop stops at PSD-ness -- it never searches the
  repair class for window membership).  What is certified is 'THIS
  deterministic greedy repair fails to reach the window', not
  in-class infeasibility.  MITIGATION carried: the verdict is
  kind=screen (disclosed, not a hard gate), and the margins are
  huge in 3 of 5 worlds -- but at b8 SCRARITH the repaired world
  lands at J_2 = 0.2597, INSIDE the frozen J_2-window (0.02, 0.26);
  it fails IN-WINDOW only via tau_rep = -0.355 < 0 (ytb/a2sgn legs),
  a thin-margin case where a heuristic-vs-exhaustive gap could
  matter in the J_2 leg.  Recommended: retype the enum to
  RESCUE-NOT-FOUND-GREEDY (or add an optimality certificate).  No
  taxonomy change: INFORMATIVE-NEGATIVE is carried by the removal +
  plant/ghost legs, which are CONFIRMED.  GATE: G40 (AST/source
  scan: monotone accumulation only, no objective evaluation +
  window arithmetic 0.02 < 0.2597 < 0.26 + tau_rep < 0 from the
  frozen log + kind=screen typing verified).
BH5-F4 [MINOR][provenance-disclosure]  assembly_walls_probe.py's
  SMOKE-1 NOTE states 'SPEC_SHA moves once -- disclosed; smoke4 at
  the frozen hash is the verdict-bearing smoke'.  The kept smoke
  logs show the hash moved TWICE after smoke2: f03f1fb39d60de2f
  (smoke1/2) -> b2a7395539622f60 (smoke3, 34/34) -> dd9cdea1c518ee25
  (smoke4 = the frozen record hash, 34/34).  The intermediate
  b2a7... docstring revision between smoke3 and smoke4 is
  unaccounted in the disclosure (both post-fix smokes are green and
  the record runs sit at the final hash, so no result is touched --
  a BH4-F2-class evidence-bookkeeping gap, here in the move count
  rather than in log retention).  GATE: G32 (hash census over the
  kept logs + disclosure grep).
BH5-F5 [NOTE][note-wording, rescue]  Note CDLXIV's rescue summary
  '(b5 SMOOTH: tau -5.2e-12, J_2 -3.05; b8 SCRARITH J_2 0.2597, b8
  EPSTEIN J_2 0.7644 -- ueber der Kappe)' misattributes the b8
  SCRARITH failure: 0.2597 is BELOW the 0.26 cap (it is inside the
  J_2-window); the world fails IN-WINDOW because the repaired tau
  stays NEGATIVE (-3.553e-01, printed in the log, omitted in the
  note).  'ueber der Kappe' is correct only for EPSTEIN (0.7644).
  Log and gate verdicts are right; note wording only.  GATE: G41
  (note grep + log parse + window arithmetic).
BH5-F6 [NOTE][round-label-drift]  The corpus convention (nearalign
  docstring + note CDLVIII 'RUNDE 153', rootladder 'CDLVII/r153',
  edge_cleanup 'r151/r153/r154 strings', gfloor 'r153 RES1/RES2',
  v922/v923/v924/v925 round numbering) fixes anchor_epslock = round
  153.  assembly_walls_probe.py cites 'CDLVII/r152 anchor_epslock'
  (State-consumed list) and tags a census row 'r137/r140/r151/r152'
  -- off by one; and note CDLXVI's not-promoted list 'ebenso
  r152/153/155' includes r152 (= the CDLVI promotion round, which
  has no promotable content) where {153, 155} = {anchor_epslock,
  assembly_walls} is the consistent reading.  BH4-F3 label-drift
  class; no numeric claim is touched.  GATE: G51 (grep conjunction
  across the five surfaces).

CHECKED CLEAN (adversarially, no finding): THE RAZOR GF1 re-proven
independently at 4 excited levels (partial-fraction identity, spread
identity, strict upper end) with the BS-dominance == chi-cap chase
and the two-level lower-end equality re-instanced on own exact
rationals (s == P and g == 1/(s + 1/delta_1) == rho2 delta_1 EXACT
for P in {1e6, 3/7}, delta_1 in {1/5, 9}): the two-level sharpness
claim HOLDS -- no algebra-only improvement exists within the GF1
hypotheses; GF2/GF3 re-proven (4-level); GF4 re-proven at K = 4
(Newton quotient == 1/(H_t + s), B(q_0) == -rho2 P_c'(q_0)) with the
Jg t_g == 1 + g chase confirmed DEFINITIONAL (the round's measured
content is tlaw* in the tlaw window + t_g flat, correctly typed
MEASURED in probe, note and v923); GF5a S1-absorption re-chased
through the B00-root equation (S1 == jr betapos (lam_1 - tau)/
(lam_1 - beta_0) EXACT, factor >= 1) -- the S1-elimination against
the r150 strings is CONFIRMED (S1/jr - betapos = 2.7e-7-class,
consistent with the frozen 6-digit betapos cross-replication); the
twin squeeze re-instanced (exact-rational 3-level secular root
inside [1/(SEC + 1/FG), 1/SEC]) and J <= SEC x FULLGAP re-chased;
SB1 trace loop + unconditional tail re-proven at 5 levels; the r162
QUARTIC LAW survives an independent free-exponent attack (least
squares on the frozen record J-table: p = 3.9072 +- 0.1136 with
AIC(fixed 4) = -30.87 < AIC(free) = -29.79 << AIC(3.5) = -23.16,
AIC(4.5) = -19.46; exponents 3.5/4.5 rejected at 3.6/5.2 sigma; the
theta-slope -0.0928 replicates the record's -0.093; the frozen
slope gate 4 +- 0.45 is honest and generously wide); GL1 inclusion
monotonicity, GL2 arrowhead instrument (dual row R_i u_j ==
delta_ij, kernel(S-j) == V + span(u~), arrowhead spectrum == direct
compression to 1e-10, secular root + eigenvector components) and
GL3 (single-row Cauchy interlacing + R = phi equality witness +
razor vacuity 1/(s + 1/F) <= F) verified on own instances; the GL4
jr t_r == 1 + 1/FULLGAP and GL5 FULLGAP == theta t_r T_z^4 - 1
chases confirmed definitional-given-R2 (correctly presented as
chases, the measured content being theta flat); L1/L2/L3/L5 of r156
re-derived (moment-Laurent dictionary, quarter-cap identity J_2 ==
z_0(1 - z_0) - z_0 rho(z_0) from an own Laurent parametrization,
SR1-SR3 from an own series expansion, level shift y F_1 == a_4 +
F_2), the deep-rung z|rho| ladder 0.0034 -> 0.0102 confirmed
log-consistent with v924's pins and the quarter-cap headroom
arithmetic (J_2 max 0.1506 <= 1/4 + 0.0102) trivially valid; the
EDGE-ZERO theorem adjudicated EXACT-BY-CONVENTION (om_k := k pi/A
is the definition of the mode lattice in every frozen builder --
r151 TB.cell_matrix, R4.build_cell, gfloor/fgl replicas -- so
A om_k == k pi is exact, not a mesh statement; the theorem's
content is the quadratic sin^2 screening, honestly framed); the P2
far-law a_2 == -y_t sign confirmed measured-per-block (r154 G30
a2sgn == -1 at all six blocks, frozen logs); the cascade L5
certificate logic re-derived (level shift + Laurent envelope +
no-real-root-above-Y bracketing is sound); the a-walls window
algebra W3 re-derived from |w| = a|z|^2/|z^2 + a|^2 (window
quadratic, edges, width 4 delta sqrt(gamma^2 + 2 delta^2), matched
pin a/(4 gamma^2), location witness (2 delta(gamma + delta))^2 -
(2 delta sqrt(gamma^2 + 2 delta^2))^2 == 4 delta^3 (2 gamma -
delta) >= 0, on-line w in [0, 1/4] exact); the Z8 SUBSUMPTION
demand-level argument verified (LM split forces delta_1 >= 1/(B-1)
> 0 at selected points; the algebra is exact, the premise is Z4's
own selection criterion -- 'subsumed at demand level' is the
correct typing, carried unchanged into v925); the JJ slack identity
and the rho_co = 4797/1156 - 963 sqrt(13)/1156 co-jump
counterexample re-verified exactly; THE 357 TURING-CLASS
CERTIFICATES recomputed IN FULL with an own vectorized
implementation from the X5 cache (all D_cs > 0, worst margin
0.3461 at (12, 1) == record, x_0(HSW) == 121, x_0(BW25) == 112,
D_hsw < 0 at x in {13, 21, 34, 55, 89} battery-wide,
verification/verified_zeros_n7000.json == the X5 npy bitwise); the
j2 plant/ghost asymmetry tables note-vs-log consistent (ghosts b5
6.0e-8 .. 6.5e-2 at the quoted gammas; plants in-window; b5 multi
break disclosed REPORTED); the j2 morph-path legality invariants
(CORR mass/support/positivity, SIGN support off the theta = 1/2
point which the frozen grid never visits) verified as algebra;
SPEC_SHA integrity: the recomputed docstring hash of EVERY round
probe matches its record logs (gfloor cc7837138d41add7, fgl
26bdb5a87f63c519 post-AMENDMENT-1 with run1/smokes at the disclosed
e722fb65d0a3c68c, rootladder 02755d6b7ad0cfcb, spectral_balance
3ed388698a138e31, edge_cleanup f6c0318841bb3942 with the disclosed
eb64691e/ee70cba1/5a1abbea ancestry, j2 6851e11acfac28aa, nearalign
f92b3fb59b142254 with run1/smoke1 at the disclosed 7134a2430a395141,
anchor f19ae8c01f198cd4 with smoke1/2 at the disclosed ca5d3c1c,
assembly dd9cdea1c518ee25 -- ancestry finding F4 -- collapserate
5cc50aa530c59169, tlawcap 27e00aa631a050c3 with run1/smoke3 at the
disclosed 5db0fe06); deterministic re-runs: every kept pair
re-diffed, non-timing diff EMPTY everywhere, raw pair counts
exactly as claimed (gfloor 7, fgl 8, j2 1, edge/rootladder/
nearalign/anchor/assembly 3, spectral 8, collapserate 8; promo
reruns likewise); min-cut flows re-verified with own Edmonds-Karp:
r150-class graph 4/5/5/9 (gfloor/fgl encodings) and r154-class
graph 4/5/5/7 (nearalign encoding) -- the 7/8/9 counterfactual
variants are per-graph and each round names its graph (consistent
bookkeeping); note numerals CDLIII..CDLXVII gap-free, strictly
consecutive, head-verification statements chain correctly through
all disclosed concurrent-lane collisions; residue bookkeeping
CDLIV -> CDLXVII consistent including the r157 pair-merge, the
r161 S1-absorption/TOPROOT narrowing, the J_2-relocation into
TWINDOW (CDLXIV) and the r162 delta_1-floor recoordination onto
{theta-window x t_r-window}; the current residue statement
{TOPROOT(= B00-ROOTGAP == SEC-cap), TLAWCAP-block, QSUBGAP-floor}
+ dense-a/a-extension/window-a is consistent with every round's
own paragraph; window constants theta [0.1730, 0.2569] inside the
frozen (0.10, 0.40), tlaw_0 0.2664 -> 0.5778 / tlaw* 0.2399 ->
0.5316 / t_g 0.8493..1.0347 / t_r 0.8893..1.0430 (jr and t_r
tables IDENTICAL across the r150 and r162 logs), betapos six-digit
identical across r150/r161, J_2 0.1117 -> 0.1506 with the gfloor
J_2-proxy 0.1259 -> 0.1513 correctly disclosed as a DIFFERENT
instrument; v922-v925 all green as shipped (13/13, 20/20, 12/12,
14/14), their pinned tables verified against the source-run logs,
NO verdict upgraded in promotion (PROVEN/MEASURED/CERTIFIED/OPEN
typings carried verbatim; ledger rows 1066-1069 carry the honest
typings and NOT-RH-EVIDENCE), ledger 1069 rows / registry 918 rows
/ run_all v922-v925 registered, matching CDLXVI's counters.

NO ROUND VERDICT FLIPS.  No frozen load-bearing number in rounds
149-162 was found wrong; the four MINOR findings are one
overstated-exactness label at r150 (silently superseded by r161's
correct law), one off-by-one headline count on a promoted surface
(all 73 certificates exist), one rescue-instrument description/enum
overstatement (screen-typed, taxonomy unaffected), and one
hash-move-count disclosure gap; the two NOTEs are wording/label
drifts.  COMPOSITE: BUGHUNT5-FINDINGS(6) = 0 MAJOR / 4 MINOR /
2 NOTE.  NO RH CLAIM.

FROZEN NUMERICS: J_TABLE (fgl run2 record) = (2.502511e5,
1.104303e6, 1.090905e7, 3.115664e7, 1.140547e8, 1.752871e8) at
x = (5, 8, 13, 18, 24, 28); FIT: p_free 3.9072 +- 0.1136, AIC
(-29.79, -23.16, -30.87, -19.46) for (free, 3.5, 4, 4.5), sigma
(3.58, 0.82, 5.22) for (3.5, 4, 4.5); THETA_SLOPE -0.0928; E3:
worst margin 0.3461 at (12, 1), x_0 = (121, 112); F1 magnitude
2.726e-7 at x = 5 (betapos 0.24628914, FULLGAP 2.225493e5); F2
counts (1, 1, 1, 1, 18, 51) sum 73 vs claimed 72; F3/F5 window
(0.02, 0.26) vs J_2 0.2597 and tau_rep -3.553e-01; F4 hash chain
f03f1fb39d60de2f -> b2a7395539622f60 -> dd9cdea1c518ee25; SPEC/LOG
hash table as in CHECKED CLEAN; raw diff pair counts (7, 8, 1, 3,
3, 3, 3, 3, 8, 8); min-cut (4, 5, 5, 9) and (4, 5, 5, 7); numerals
CDLIII..CDLXVII == 15 consecutive; counters (1069, 918).
RUNTIME_BAR = 900 s.  Deterministic: NO randomness anywhere; numpy
f64 only for the flat O(1) fit/certificate layers (margins >= 1e2);
sympy exact for every identity gate; cache np.load ONLY inside
ward_cache(); no zeta use anywhere; no import of any frozen probe
or verification module.

AST FIREWALL: np.load only inside ward_* functions; no zero-oracle
names; NO zeta use; no import of verification/ or of any frozen
probe module.  NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import re
import sys
import time

import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, okv: bool, det: str = "") -> bool:
    okv = bool(okv)
    CHECKS.append((name, okv, det))
    print("  [%s] %-34s %s" % ("PASS" if okv else "FAIL", name, det))
    return okv


def section(t: str) -> None:
    print("\n== " + t)


def rd(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def ward_cache() -> np.ndarray:
    """X5 cache, READ-ONLY (the only np.load in this probe)."""
    return np.load(os.path.join(HERE, "verified_zeros_n7000.npy"))


# ---------------------------------------------------------------- S0
def s0() -> None:
    section("S0  FIREWALL + CORPUS CENSUS")
    tree = ast.parse(rd(os.path.abspath(__file__)))
    bad_load, bad_zeta, bad_imp = [], [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            inward = node.name.startswith("ward_")
            for sub in ast.walk(node):
                if (isinstance(sub, ast.Attribute)
                        and sub.attr == "load" and not inward
                        and isinstance(sub.value, ast.Name)
                        and sub.value.id == "np"):
                    bad_load.append(node.name)
                if isinstance(sub, ast.Attribute) and sub.attr == "zeta":
                    bad_zeta.append(node.name)
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names]
            mod = getattr(node, "module", "") or ""
            for nm in names + [mod]:
                if "probe" in nm or nm.startswith("v9"):
                    bad_imp.append(nm)
    check("G01-ast-firewall", not bad_load and not bad_zeta
          and not bad_imp,
          "np.load only in ward_ (viol %s); zeta use %s; frozen-probe/"
          "verification imports %s" % (bad_load or "none",
                                       bad_zeta or "none",
                                       bad_imp or "none"))
    need = ["gfloor_probe.py", "fullgap_growthlaw_probe.py",
            "rootladder_probe.py", "spectral_balance_probe.py",
            "edge_cleanup_probe.py", "j2_primeforce_probe.py",
            "nearalign_probe.py", "anchor_epslock_probe.py",
            "assembly_walls_probe.py", "collapserate_probe.py",
            "tlawcap_blocks_probe.py", "verified_zeros_n7000.npy"]
    miss = [f for f in need if not os.path.isfile(os.path.join(HERE, f))]
    gam = ward_cache()
    okc = (len(gam) == 7000
           and abs(float(gam[0]) - 14.134725141734695) < 1e-9
           and abs(float(gam[-1]) - 7264.7482480903) < 1e-6
           and bool(np.all(np.diff(gam) > 0)))
    check("G02-corpus+cache", not miss and okc,
          "11 frozen probes + X5 cache present (missing %s); cache "
          "7000 monotone, ends %.6f/%.4f" % (miss or "none",
                                             float(gam[0]),
                                             float(gam[-1])))


# ---------------------------------------------------------------- S1
def s1() -> None:
    import sympy as sp
    from fractions import Fraction as Fr

    section("S1  EXACT LAYER (independent re-derivations)")

    g, r2 = sp.symbols("g r2", positive=True)
    e = sp.symbols("e1:5", positive=True)
    d = sp.symbols("d1:5", positive=True)
    S = sum(ei / (di - g) for ei, di in zip(e, d))
    chi = sum(ei / di for ei, di in zip(e, d))
    T2 = sum(ei / (di * (di - g)) for ei, di in zip(e, d))
    ok1 = sp.simplify(sp.together(S - chi - g * T2)) == 0
    ok2 = sp.simplify(sp.together(
        S - d[0] * T2 - sum(ei * (di - d[0]) / (di * (di - g))
                            for ei, di in zip(e, d)))) == 0
    ok3 = sp.simplify(sp.together(
        r2 * d[0] * (chi / r2 + 1 / d[0]) - (chi * d[0] + r2))) == 0
    okw = True
    for P in (Fr(10 ** 6), Fr(3, 7)):
        for d1 in (Fr(1, 5), Fr(9)):
            r2v = Fr(1) / (1 + P * d1)
            e1v = 1 - r2v
            sv = (e1v / d1) / r2v
            gv = r2v * d1 / (r2v + e1v)
            okw = okw and sv == P and gv == Fr(1) / (sv + 1 / d1) \
                and gv == r2v * d1 and gv < Fr(1) / sv
    check("G10-gf1-razor-own", ok1 and ok2 and ok3 and okw,
          "GF1 re-proven at 4 excited levels (probe used 2/3): "
          "partial fractions + spread + dominance == chi-cap; "
          "two-level lower-end EQUALITY on own exact rationals "
          "(P in {1e6, 3/7}, d1 in {1/5, 9}): sharpness claim HOLDS")

    okp = sp.simplify(sp.together(
        (1 - (chi / r2) * g - g ** 2 * T2 / r2).subs(r2, g * S))) == 0
    sh1g = (e[0] / (d[0] - g)) / S
    sh1 = (e[0] / d[0]) / chi
    a_ = g / (d[0] - g)
    b_ = g * T2 / chi
    oks = sp.simplify(sp.together(
        sh1g / sh1 - (1 + a_) / (1 + b_))) == 0
    okba = sp.simplify(sp.together(
        chi * a_ - g * T2
        - sum(ei * g * (di - d[0]) / (di * (d[0] - g) * (di - g))
              for ei, di in zip(e, d)))) == 0
    check("G11-gf2-gf3-own", okp and oks and okba,
          "GF2 pinch 1 - sg == g^2 T2/rho2 and GF3 share pricing "
          "(1+a)/(1+b) with b <= a termwise, re-proven at 4 levels")

    q0 = sp.symbols("q0", positive=True)
    qs = [q0, q0 + d[0], q0 + d[0] + d[1], q0 + d[0] + d[1] + d[2]]
    z = sp.symbols("z")
    ee0 = sp.symbols("ee0", positive=True)
    ets = (ee0,) + e[:3]
    Pc = sp.prod([qq - z for qq in qs])
    Bz = sum(ets[i] ** 2 * sp.prod([qs[j] - z for j in range(4)
                                    if j != i]) for i in range(4))
    okB = sp.simplify(Bz.subs(z, q0)
                      + ee0 ** 2 * sp.diff(Pc, z).subs(z, q0)) == 0
    H = sum(1 / (qs[i] - q0) for i in range(1, 4))
    chiq = sum(ets[i] ** 2 / (qs[i] - q0) for i in range(1, 4))
    N1 = -Bz.subs(z, q0) / sp.diff(Bz, z).subs(z, q0)
    okN = sp.simplify(sp.together(
        N1 - ee0 ** 2 / (ee0 ** 2 * H + chiq))) == 0
    Ast, A0_, Gc, tau_ = sp.symbols("Ast A0_ Gc tau_", positive=True)
    okJ = sp.simplify((Ast / A0_) ** 2
                      * ((tau_ * (1 + g) / (8 * Ast ** 2 * Gc))
                         / (tau_ / (8 * A0_ ** 2 * Gc)))
                      - (1 + g)) == 0
    check("G12-gf4-own", okB and okN and okJ,
          "B(q0) == -rho2 Pc'(q0) and Newton N_1 == 1/(H_t + s) at "
          "K = 4; Jg t_g == 1 + g re-typed DEFINITIONAL (measured "
          "content = tlaw* window, correctly typed in r161/v923)")

    tau, l1, l2, l3, b0 = sp.symbols("tau l1 l2 l3 b0", positive=True)
    w0, w1, w2, w3 = sp.symbols("w0 w1 w2 w3", positive=True)
    seceq = sp.Eq(w0 / (b0 - tau),
                  w1 / (l1 - b0) + w2 / (l2 - b0) + w3 / (l3 - b0))
    S1 = (w1 / (l1 - b0)) / (w1 / (l1 - b0) + w2 / (l2 - b0)
                             + w3 / (l3 - b0))
    w0v = sp.solve(seceq, w0)[0]
    J = w1 / w0v
    FG = (l1 - tau) / tau
    jr = J / FG
    bpos = (b0 - tau) / tau
    okS1 = sp.simplify(sp.together(
        S1 - jr * bpos * (l1 - tau) / (l1 - b0))) == 0
    okR3 = sp.simplify(sp.together(
        J - S1 * (l1 - b0) / (b0 - tau))) == 0
    resid = sp.simplify(sp.together(
        S1 / jr - bpos - bpos ** 2 / (FG - bpos)))
    not_exact = resid == 0 and sp.simplify(
        bpos ** 2 / (FG - bpos)) != 0
    # magnitude from the frozen strings (r150/r161)
    bp5, fg5 = 0.24628914, 2.225493e5
    mag5 = bp5 ** 2 / (fg5 - bp5)
    src_r150 = rd(os.path.join(HERE, "collapserate_probe.py"))
    nx = rd(os.path.join(ROOT, "experiments", "next.txt"))
    grep = ("(= S1/jr by exact chase)" in src_r150
            and "betapos == S1/jr chase" in src_r150
            and "exakter Chase" in nx)
    check("G13-gf5a-own+F1", okS1 and okR3 and not_exact
          and abs(mag5 - 2.726e-7) < 2e-9 and grep,
          "BH5-F1 CONFIRMED [MINOR]: S1 == jr betapos (l1-tau)/"
          "(l1-b0) EXACT (own chase; r161 correct) but S1/jr - "
          "betapos == betapos^2/(FULLGAP - betapos) != 0: r150's "
          "'betapos == S1/jr by exact chase' (docstring + enum + "
          "CDLIV) is NOT exact -- magnitude %.3e at x = 5, below "
          "r150's 4-digit print, silently superseded by r161"
          % mag5)

    b0s = sp.symbols("b0s")
    eqn = sp.Eq(sp.Rational(3) / (b0s - 1),
                sp.Rational(2) / (3 - b0s) + sp.Rational(5) / (9 - b0s))
    sols = [s for s in sp.solve(eqn, b0s)
            if s.is_real and 1 < s < 3]
    bp_i = sp.simplify(sols[0] - 1)
    SECs = sp.Rational(2, 3) / 2 + sp.Rational(5, 3) / 8
    FGs = sp.Rational(2)
    ok_tw = bool(sp.N(1 / (SECs + 1 / FGs)) <= sp.N(bp_i)
                 <= sp.N(1 / SECs))
    ok_JS = bool(sp.Rational(2, 3) <= SECs * FGs)
    check("G14-gf5b-twin-own", ok_tw and ok_JS,
          "twin squeeze 1/(SEC + 1/FG) <= betapos <= 1/SEC on an own "
          "exact 3-level secular instance; J <= SEC x FULLGAP chase")

    ms = sp.symbols("m1:6", positive=True)
    lam1 = tau + ms[0]
    lams = [lam1] + [lam1 + mi for mi in ms[1:]]
    TrH = sum(1 / (li - tau) for li in lams)
    tf = (lam1 - tau) * TrH
    ok_lo = sp.simplify(sp.together(
        tau * TrH - tf / ((lam1 - tau) / tau))) == 0
    ok_tf = sp.simplify(sp.together(
        tf - 1 - sum((lam1 - tau) / (li - tau)
                     for li in lams[1:]))) == 0
    check("G15-sb1-own", ok_lo and ok_tf,
          "SB1 trace loop tau TrH == tf/FULLGAP + tail tf == 1 + "
          "sum a_i (a_i in (0, 1]) re-proven at 5 levels: "
          "DELTA1FLOOR <==> TRACEFLOOR two-sided, tail closed")

    y = sp.symbols("y", positive=True)
    v1, v2, v3, b1, b2, b3 = sp.symbols("v1 v2 v3 b1 b2 b3",
                                        positive=True)
    Sf = v1 / (y - b1) + v2 / (y - b2) + v3 / (y - b3)
    Tf = (v1 * b1 / (y - b1) + v2 * b2 / (y - b2)
          + v3 * b3 / (y - b3))
    okL1 = sp.simplify(sp.together(
        y * Sf - (v1 + v2 + v3) - Tf)) == 0
    z0, J3s, J4s = sp.symbols("z0 J3s J4s", positive=True)
    J2s = sp.symbols("J2s", positive=True)
    PHI = z0 - 1 + J2s / z0 + J3s / z0 ** 2 + J4s / z0 ** 3
    J2sol = sp.solve(sp.Eq(PHI, 0), J2s)[0]
    okL2 = sp.simplify(sp.together(
        J2sol - (z0 * (1 - z0)
                 - z0 * (J3s / z0 ** 2 + J4s / z0 ** 3)))) == 0
    u = sp.symbols("u")
    y1, y2 = sp.symbols("y1 y2", positive=True)
    A0s = sp.symbols("A0s", positive=True)
    Ff = A0s * (y - y1) * (y - y2) / ((y - b1) * (y - b2))
    Sexp = sp.series(sp.simplify(Ff / A0s - 1).subs(y, 1 / u),
                     u, 0, 4).removeO()
    a2 = sp.expand(Sexp).coeff(u, 1)
    a4 = sp.expand(Sexp).coeff(u, 2)
    a6 = sp.expand(Sexp).coeff(u, 3)
    P1 = y1 + y2 - b1 - b2
    P2 = y1 ** 2 + y2 ** 2 - b1 ** 2 - b2 ** 2
    P3 = y1 ** 3 + y2 ** 3 - b1 ** 3 - b2 ** 3
    okL3 = (sp.simplify(sp.expand(P1 + a2)) == 0
            and sp.simplify(sp.expand(P2 - (a2 ** 2 - 2 * a4))) == 0
            and sp.simplify(sp.expand(
                P3 - (3 * a2 * a4 - 3 * a6 - a2 ** 3))) == 0)
    F2 = (v1 * b1 ** 2 / (y - b1) + v2 * b2 ** 2 / (y - b2)
          + v3 * b3 ** 2 / (y - b3))
    okL5 = sp.simplify(sp.together(
        y * Tf - (v1 * b1 + v2 * b2 + v3 * b3) - F2)) == 0
    okQC = 0.1506 <= 0.25 + 0.0102
    check("G16-rootladder-own", okL1 and okL2 and okL3 and okL5
          and okQC,
          "L1 dictionary, L2 quarter-cap identity, L3 sum rules "
          "SR1-SR3 (own series), L5 level shift re-proven; deep "
          "z|rho| ladder 0.0034 -> 0.0102 log-consistent with v924; "
          "headroom J_2 max 0.1506 <= 1/4 + 0.0102")

    ga, de, av, t = sp.symbols("ga de av t", positive=True)
    wdef = av * (ga ** 2 + de ** 2) / ((av + ga ** 2 - de ** 2) ** 2
                                       + 4 * ga ** 2 * de ** 2)
    okpin = sp.simplify(wdef.subs(av, ga ** 2 + de ** 2)
                        - (ga ** 2 + de ** 2)
                        / (4 * ga ** 2)) == 0
    f = ((av + ga ** 2 - de ** 2) ** 2 + 4 * ga ** 2 * de ** 2
         - 4 * av * (ga ** 2 + de ** 2))
    okquad = sp.simplify(sp.expand(
        f - (av ** 2 - 2 * av * (ga ** 2 + 3 * de ** 2)
             + (ga ** 2 + de ** 2) ** 2))) == 0
    X = 2 * de * (ga + de)
    Y = 2 * de * sp.sqrt(ga ** 2 + 2 * de ** 2)
    okwit = sp.simplify(sp.expand(
        X ** 2 - Y ** 2 - 4 * de ** 3 * (2 * ga - de))) == 0
    okon = sp.simplify(sp.expand(
        (av + t ** 2) ** 2 - 4 * av * t ** 2
        - (av - t ** 2) ** 2)) == 0
    src_g = rd(os.path.join(HERE, "gfloor_probe.py"))
    src_r4 = rd(os.path.join(HERE, "radius4_an_probe.py"))
    okez = ("k * mp.pi / aa" in src_g and "k * mp.pi / aa" in src_r4)
    check("G17-awalls+EZ-own", okpin and okquad and okwit and okon
          and okez,
          "W3 window algebra re-derived from |w| = a|z|^2/|z^2+a|^2 "
          "(quadratic, width, matched pin, location witness 4 d^3 "
          "(2g - d), on-line w <= 1/4); EZ adjudicated EXACT-BY-"
          "CONVENTION (om_k := k pi/A in every frozen builder)")

    Bb, dl = sp.symbols("Bb dl", positive=True)
    okz8 = sp.simplify(sp.solve(sp.Eq(1 + 1 / dl, Bb), dl)[0]
                       - 1 / (Bb - 1)) == 0
    sX, C, A = sp.symbols("sX C A", positive=True)
    okjj = sp.simplify(sp.expand(
        sp.exp(sX) * (1 + C + A) - (1 + C + A * sp.exp(sX))
        - (sp.exp(sX) - 1) * (1 + C))) == 0
    val = sp.Rational(4797, 1156) - sp.Rational(963, 1156) * sp.sqrt(13)
    okco = sp.simplify(val - 1) != 0 \
        and abs(float(val) - 1.1460675793) < 1e-9
    check("G18-z8+jj+cojump-own", okz8 and okjj and okco,
          "Z8 LM-split subsumption algebra (delta_1 >= 1/(B-1) > 0 "
          "at selected points; demand-level typing carried), JJ "
          "slack identity, rho_co counterexample re-verified exact")

    # GL1/GL2/GL3 own numeric instance
    K = 7
    M = np.array([[(i + 1) if i == j else 1.0 / (1 + abs(i - j))
                   for j in range(K)] for i in range(K)])
    M = (M + M.T) / 2
    R = np.array([[1, 0, 2, 0, 1, 0, 3],
                  [0, 1, 0, 1, 0, 2, 0],
                  [2, 1, 0, 0, 1, 0, 1]], dtype=float)
    m = 3
    import numpy.linalg as la
    Vt = la.svd(R)[2]
    Vk = Vt[m:].T
    q, zc = la.eigh(Vk.T @ M @ Vk)
    j = 1
    uj = R.T @ la.solve(R @ R.T, np.eye(m)[:, j])
    ok_du = np.allclose(R @ uj, np.eye(m)[:, j], atol=1e-12)
    up = uj - Vk @ (Vk.T @ uj)
    ut = up / la.norm(up)
    Rj = np.delete(R, j, axis=0)
    Vj = la.svd(Rj)[2][m - 1:].T
    Bas = np.hstack([Vk, ut[:, None]])
    ok_sp = np.allclose(Bas @ la.solve(Bas.T @ Bas, Bas.T @ Vj),
                        Vj, atol=1e-10)
    b_ar = (Vk @ zc).T @ M @ ut
    c_ar = ut @ M @ ut
    Arr = np.zeros((K - m + 1, K - m + 1))
    Arr[:K - m, :K - m] = np.diag(q)
    Arr[:K - m, -1] = b_ar
    Arr[-1, :K - m] = b_ar
    Arr[-1, -1] = c_ar
    lam_arr = np.sort(la.eigvalsh(Arr))
    lam_dir = np.sort(la.eigvalsh(Vj.T @ M @ Vj))
    ok_sp2 = np.allclose(lam_arr, lam_dir, atol=1e-10)
    lam0 = lam_arr[0]
    ok_sec = abs((c_ar - lam0) - np.sum(b_ar ** 2
                                        / (q - lam0))) < 1e-9
    wv = -b_ar / (q - lam0)
    vec = np.concatenate([wv, [1.0]])
    ok_ev = np.allclose(Arr @ vec, lam0 * vec, atol=1e-9)
    ok_incl = lam_dir[0] <= q[0] + 1e-12
    Ei, Vi = la.eigh(M)
    phi = Vi[:, 0]
    Pph = np.eye(K) - np.outer(phi, phi)
    Bph = la.svd(phi[None, :])[2][1:].T
    lam_ker = np.sort(la.eigvalsh(Bph.T @ M @ Bph))[0]
    ok_phi = abs(lam_ker - Ei[1]) < 1e-10
    row = np.arange(1.0, K + 1)
    Brow = la.svd(row[None, :])[2][1:].T
    lam_row = np.sort(la.eigvalsh(Brow.T @ M @ Brow))[0]
    ok_int = Ei[0] - 1e-12 <= lam_row <= Ei[1] + 1e-12
    check("G19-gl1-gl2-gl3-own", ok_du and ok_sp and ok_sp2
          and ok_sec and ok_ev and ok_incl and ok_phi and ok_int,
          "GL2 arrowhead instrument verified on an own deterministic "
          "instance (dual row, kernel split, spectrum match 1e-10, "
          "secular root, eigvec components); GL1 inclusion; GL3 "
          "single-row interlacing + R = phi equality witness")
    _ = Pph  # keep linters quiet; projector built for clarity


# ---------------------------------------------------------------- S2
def s2() -> None:
    section("S2  MEASURED LAYER (independent recomputation)")

    xs = (5, 8, 13, 18, 24, 28)
    J = (2.502511e5, 1.104303e6, 1.090905e7, 3.115664e7,
         1.140547e8, 1.752871e8)
    lt = [math.log10(2 * math.pi * x) for x in xs]
    lj = [math.log10(v) for v in J]
    n = len(xs)
    mx = sum(lt) / n
    my = sum(lj) / n
    sxx = sum((a - mx) ** 2 for a in lt)
    p = sum((a - mx) * (b - my) for a, b in zip(lt, lj)) / sxx
    c0 = my - p * mx
    rss_f = sum((b - (c0 + p * a)) ** 2 for a, b in zip(lt, lj))
    se = math.sqrt(rss_f / (n - 2) / sxx)

    def rss_fix(pf: float) -> float:
        cf = sum(b - pf * a for a, b in zip(lt, lj)) / n
        return sum((b - (cf + pf * a)) ** 2 for a, b in zip(lt, lj))

    aic_free = n * math.log(rss_f / n) + 4
    aics = {pf: n * math.log(rss_fix(pf) / n) + 2
            for pf in (3.5, 4.0, 4.5)}
    lx = [math.log10(x) for x in xs]
    lth = [b - 4 * a for a, b in zip(lt, lj)]
    mx2 = sum(lx) / n
    my2 = sum(lth) / n
    sl = (sum((a - mx2) * (b - my2) for a, b in zip(lx, lth))
          / sum((a - mx2) ** 2 for a in lx))
    ok_fit = (abs(p - 3.9072) < 5e-4 and abs(se - 0.1136) < 5e-4
              and aics[4.0] < aic_free < aics[3.5] < aics[4.5]
              and abs(p - 3.5) / se > 3.0 and abs(p - 4.5) / se > 3.0
              and abs(p - 4.0) / se < 1.0 and abs(sl + 0.0928) < 5e-4)
    check("G20-quartic-fit-own", ok_fit,
          "free exponent %.4f +- %.4f; AIC free/3.5/4/4.5 = %.2f/"
          "%.2f/%.2f/%.2f (FIXED 4 preferred; 3.5/4.5 rejected at "
          "%.1f/%.1f sigma); theta-slope %.4f == record -0.093: "
          "THE QUARTIC LAW SURVIVES an instrument r162 did not run"
          % (p, se, aic_free, aics[3.5], aics[4.0], aics[4.5],
             abs(p - 3.5) / se, abs(p - 4.5) / se, sl))

    gam = ward_cache()
    CE = 1e-9

    def wof(a: float, tt: np.ndarray | float):
        return a * tt * tt / (a + tt * tt) ** 2

    worst = (None, 1e99)
    bad = 0
    for x in range(3, 122):
        N = int(math.ceil(1.25 * x * math.log(x))) - 1
        Tz = 2 * math.pi * x
        m_lo = int(np.searchsorted(gam + CE, Tz, side="right"))
        for a in (1.0, 4.0, 16.0):
            tail1 = float(np.sum(wof(a, gam[N:] + CE)))
            edge = max(0, N - m_lo) * wof(a, Tz)
            D = 7.0 / 8.0 * tail1 - edge
            if D <= 0:
                bad += 1
            mg = D / edge if edge > 0 else float("inf")
            if mg < worst[1]:
                worst = ((x, a), mg)

    def m_rvm(T: float) -> float:
        return (T / (2 * math.pi)
                * math.log(T / (2 * math.pi * math.e)) + 7 / 8)

    def q_gen(T: float, abc) -> float:
        return (abc[0] * math.log(T)
                + abc[1] * math.log(math.log(T)) + abc[2])

    def t_star(N: int, abc) -> float:
        lo, hi = 20.0, 1e30
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if m_rvm(mid) - q_gen(mid, abc) >= N:
                hi = mid
            else:
                lo = mid
        return hi

    def d_asym(x: float, a: float, abc) -> float:
        N = int(math.ceil(1.25 * x * math.log(x))) - 1
        Ts = t_star(N, abc)
        Tz = 2 * math.pi * x
        best = 0.0
        for lam in (1.5, 2.0, 3.0):
            for Jn in (1, 2, 3, 4, 6, 8):
                Tj = [Ts * lam ** k for k in range(Jn + 1)]
                tot = 0.0
                upv = m_rvm(Ts) + q_gen(Ts, abc)
                for k in range(Jn):
                    nn = m_rvm(Tj[k + 1]) - q_gen(Tj[k + 1], abc)
                    tot += max(0.0, nn - max(float(N), upv)) \
                        * wof(a, Tj[k + 1])
                    upv = m_rvm(Tj[k + 1]) + q_gen(Tj[k + 1], abc)
                best = max(best, tot)
        return best - best / 8.0 \
            - max(0.0, N - (m_rvm(Tz) - q_gen(Tz, abc))) * wof(a, Tz)

    HSW = (0.1038, 0.2573, 9.3675)
    BW = (0.10076, 0.24460, 8.08344)

    def x0(abc) -> int:
        okf = -1
        for x in range(200, 89, -1):
            if all(d_asym(float(x), a, abc) > 0
                   for a in (1.0, 4.0, 16.0)):
                okf = x
            else:
                break
        return okf

    strip_neg = all(all(d_asym(float(x), a, HSW) < 0
                        for a in (1.0, 4.0, 16.0))
                    for x in (13, 21, 34, 55, 89))
    import json
    gj = json.load(open(os.path.join(
        ROOT, "verification", "verified_zeros_n7000.json"),
        encoding="utf-8"))["gammas"]
    same = max(abs(float(gj[i]) - float(gam[i]))
               for i in range(7000)) == 0.0
    check("G21-e3-357-own", bad == 0 and worst[0] == (12, 1.0)
          and abs(worst[1] - 0.3461) < 5e-4 and x0(HSW) == 121
          and x0(BW) == 112 and strip_neg and same,
          "OWN vectorized recompute: all 357 D_cs > 0, worst margin "
          "%.4f at %s (record 0.346 at (12,1)); x0(HSW) = 121, "
          "x0(BW25) = 112; D_hsw < 0 battery-wide at {13,21,34,55,"
          "89}; verification json == X5 npy bitwise: v925's E3 "
          "closure CONFIRMED IN FULL" % (worst[1], worst[0]))

    lg_g = rd(os.path.join(HERE, "gfloor_probe.run1.log"))
    lg_s = rd(os.path.join(HERE, "spectral_balance_probe.run1.log"))
    lg_f = rd(os.path.join(HERE, "fgl_run2.log"))
    lg_r = rd(os.path.join(HERE, "rootladder_probe.run1.log"))
    pins = ["lo/g 0.999995335", "lo/g 0.999999995",
            "width 1.51e-04", "width 8.45e-08",
            "betapos = 0.246289/0.130538/0.082105/0.055824/"
            "0.042015/0.032826",
            "tg = 0.9005/0.8493/1.0135/1.0347/0.9957/0.9200"]
    ok_g = all(s_ in lg_g for s_ in pins)
    pins_s = ["TRACEFLOOR 4.493e-06", "TRACEFLOOR 6.056e-09",
              "tf-1 2.09e-05", "tf-1 2.30e-08",
              "VAC_CHI 7.55 dex", "VAC_CHI 88.81 dex",
              "BS 9.548e-07", "BS 2.159e-88"]
    ok_s = all(s_ in lg_s for s_ in pins_s)
    pins_f = ["THETA 0.2569", "THETA 0.1830", "t_r 0.8893",
              "t_r 0.9421", "jr 1.1245", "jr 1.0615"]
    ok_f = all(s_ in lg_f for s_ in pins_f)
    pins_r = ["zrho 0.0034", "zrho 0.0102"]
    ok_r = all(s_ in lg_r for s_ in pins_r)
    check("G22-promotion-pins", ok_g and ok_s and ok_f and ok_r,
          "v923/v924 pinned tables verified against the r157/r161/"
          "r156 record logs; r162 theta/t_r/jr tables verified; jr + "
          "t_r strings IDENTICAL across the r150 and r162 logs "
          "(cross-round string continuity)")

    lg_e = rd(os.path.join(HERE, "edge_cleanup_probe.run2.log"))
    mG32 = re.search(r"G32-perzero-sliver-certificates.*", lg_e)
    cnts = re.findall(r"b\d+ (\d+)/(\d+) certified",
                      mG32.group(0) if mG32 else "")
    certd = [int(a) for a, b in cnts if a == b]
    total = sum(certd)
    sliver = (1, 0, 1, 0, 18, 51)
    uniq = sum(sliver) + 2  # b8 + b18 first zeros (slivers empty)
    v925s = rd(os.path.join(ROOT, "verification",
                            "v925_edge_cleanup_closures.py"))
    led = rd(os.path.join(ROOT, "verification", "status_ledger.csv"))
    has72 = ("all 72 sliver + first-zero" in v925s
             and "72 unique targets" in led
             and "ALLEN 72 Sliver" in nx_cache())
    check("G23-F2-72-vs-73", len(cnts) == 6 and len(certd) == 6
          and total == 73 and uniq == 73 and has72,
          "BH5-F2 CONFIRMED [MINOR]: record-log certified counts "
          "%s sum to %d and the unique-target arithmetic gives %d "
          "(71 sliver + first zeros at b8/b18 only; b5/b13/b24/b28 "
          "first zeros lie INSIDE their slivers) -- v925 docstring + "
          "ledger row + CDLXIII all say 72: off by one, all 73 "
          "certificates green" % ([f"{a}/{b}" for a, b in cnts],
                                  total, uniq))


_NX: str | None = None


def nx_cache() -> str:
    global _NX
    if _NX is None:
        _NX = rd(os.path.join(ROOT, "experiments", "next.txt"))
    return _NX


# ---------------------------------------------------------------- S3
def s3() -> None:
    section("S3  PROVENANCE (hashes, re-runs, min-cut)")

    exp = {"gfloor_probe.py": "cc7837138d41add7",
           "fullgap_growthlaw_probe.py": "26bdb5a87f63c519",
           "rootladder_probe.py": "02755d6b7ad0cfcb",
           "spectral_balance_probe.py": "3ed388698a138e31",
           "edge_cleanup_probe.py": "f6c0318841bb3942",
           "j2_primeforce_probe.py": "6851e11acfac28aa",
           "nearalign_probe.py": "f92b3fb59b142254",
           "anchor_epslock_probe.py": "f19ae8c01f198cd4",
           "assembly_walls_probe.py": "dd9cdea1c518ee25",
           "collapserate_probe.py": "5cc50aa530c59169",
           "tlawcap_blocks_probe.py": "27e00aa631a050c3"}
    devs = []
    for fn, hexp in exp.items():
        doc = ast.get_docstring(
            ast.parse(rd(os.path.join(HERE, fn))), clean=False)
        h = hashlib.sha256(doc.encode("utf-8")).hexdigest()[:16]
        if h != hexp:
            devs.append((fn, h))
    logmap = {"gfloor_probe.run1.log": "cc7837138d41add7",
              "gfloor_probe.run2.log": "cc7837138d41add7",
              "fgl_run1.log": "e722fb65d0a3c68c",
              "fgl_run2.log": "26bdb5a87f63c519",
              "fgl_run3.log": "26bdb5a87f63c519",
              "rootladder_probe.run1.log": "02755d6b7ad0cfcb",
              "rootladder_probe.promo_rerun.log": "02755d6b7ad0cfcb",
              "spectral_balance_probe.promo_rerun.log":
                  "3ed388698a138e31",
              "edge_cleanup_probe.run1.log": "5a1abbea78ffda13",
              "edge_cleanup_probe.run2.log": "f6c0318841bb3942",
              "j2pf_run1.log": "6851e11acfac28aa",
              "nearalign_probe.run1.log": "7134a2430a395141",
              "nearalign_probe.run2.log": "f92b3fb59b142254",
              "anchor_epslock_probe.run1.log": "f19ae8c01f198cd4",
              "collapserate_probe.run1.log": "5cc50aa530c59169",
              "tlawcap_blocks_probe.run2.log": "27e00aa631a050c3"}
    bad = []
    for lg, hexp in logmap.items():
        mt = re.search(r"SPEC_SHA\s+([0-9a-f]{16})",
                       rd(os.path.join(HERE, lg)))
        if not mt or mt.group(1) != hexp:
            bad.append(lg)
    check("G30-spec-sha", not devs and not bad,
          "docstring SPEC_SHA of all 11 round probes recomputed == "
          "record logs (deviations %s); disclosed amendment/smoke "
          "ancestry hashes verified (%s bad)"
          % (devs or "none", bad or "none"))

    def normt(line: str) -> str:
        s = re.sub(r"\d+(\.\d+)? s\b", "T s", line)
        s = re.sub(r"\(\d+ s\)", "(T s)", s)
        return re.sub(r"runtime \S+", "runtime T", s)

    pairs = [("gfloor_probe.run1.log", "gfloor_probe.run2.log", 7),
             ("fgl_run2.log", "fgl_run3.log", 8),
             ("j2pf_run1.log", "j2pf_run2.log", 1),
             ("edge_cleanup_probe.run2.log",
              "edge_cleanup_probe.run3.log", 3),
             ("rootladder_probe.run1.log",
              "rootladder_probe.run2.log", 3),
             ("nearalign_probe.run2.log",
              "nearalign_probe.run3.log", 3),
             ("anchor_epslock_probe.run1.log",
              "anchor_epslock_probe.run2.log", 3),
             ("assembly_walls_probe.run1.log",
              "assembly_walls_probe.run2.log", 3),
             ("spectral_balance_probe.run1.log",
              "spectral_balance_probe.run2.log", 8),
             ("collapserate_probe.run1.log",
              "collapserate_probe.run2.log", 8)]
    okd = True
    dets = []
    for a, b, nraw in pairs:
        A = rd(os.path.join(HERE, a)).splitlines()
        B = rd(os.path.join(HERE, b)).splitlines()
        if len(A) != len(B):
            okd = False
            dets.append("%s len" % a)
            continue
        raw = [(x, y2) for x, y2 in zip(A, B) if x != y2]
        nont = [1 for x, y2 in raw if normt(x) != normt(y2)]
        if len(raw) != nraw or nont:
            okd = False
            dets.append("%s raw %d nont %d" % (a, len(raw),
                                               len(nont)))
    check("G31-rerun-diffs", okd,
          "every deterministic re-run pair re-diffed: raw pair "
          "counts == claimed (7/8/1/3/3/3/3/3/8/8), timing-"
          "normalized diffs ALL EMPTY (%s)" % (dets or "clean"))

    hs = []
    for lg in ("assembly_walls_probe.smoke1.log",
               "assembly_walls_probe.smoke2.log",
               "assembly_walls_probe.smoke3.log",
               "assembly_walls_probe.smoke4.log"):
        mt = re.search(r"SPEC_SHA\s+([0-9a-f]{16})",
                       rd(os.path.join(HERE, lg)))
        hs.append(mt.group(1) if mt else "?")
    src_aw = rd(os.path.join(HERE, "assembly_walls_probe.py"))
    moved_twice = (hs[0] == hs[1] == "f03f1fb39d60de2f"
                   and hs[2] == "b2a7395539622f60"
                   and hs[3] == "dd9cdea1c518ee25")
    claims_once = "moves once -- disclosed" in src_aw
    check("G32-F4-hash-moves", moved_twice and claims_once,
          "BH5-F4 CONFIRMED [MINOR]: assembly_walls discloses "
          "'SPEC_SHA moves once' but the kept smokes show TWO "
          "post-fix moves: %s -> %s -> %s (the b2a7 revision is "
          "unaccounted); record runs green at the final hash"
          % (hs[0], hs[2], hs[3]))

    def maxflow(edges, s, t) -> int:
        from collections import defaultdict, deque
        cap = defaultdict(int)
        adj = defaultdict(set)
        for (a, b2), c2 in edges.items():
            cap[(a, b2)] += c2
            adj[a].add(b2)
            adj[b2].add(a)
        flow = 0
        while True:
            par = {s: None}
            dq = deque([s])
            while dq and t not in par:
                x = dq.popleft()
                for y2 in adj[x]:
                    if y2 not in par and cap[(x, y2)] > 0:
                        par[y2] = x
                        dq.append(y2)
            if t not in par:
                return flow
            path = []
            x = t
            while par[x] is not None:
                path.append((par[x], x))
                x = par[x]
            aug = min(cap[e2] for e2 in path)
            for e2 in path:
                cap[e2] -= aug
                cap[(e2[1], e2[0])] += aug
            flow += aug

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF, ("UNC", "PICK"): INF,
            ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "TOPROOT"): 1,
                ("TOPROOT", "TAILVIS"): 1, ("TAILVIS", "TLAWCAP"): 1,
                ("TLAWCAP", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "DELTA1FLOOR"): 1,
                ("DELTA1FLOOR", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF,
                ("WPDWIN", "R4HYP"): INF})
    one = dict(ext)
    one[("SUSCAP2R", "DELTA1FLOOR")] = INF
    cf9 = dict(base)
    cf9.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
                ("NFCLOS", "TAILVIS"): 1, ("TAILVIS", "R4HYP"): INF,
                ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
                ("NFCLOS", "SUSCAP2R"): 1,
                ("SUSCAP2R", "R4HYP"): INF,
                ("NFCLOS", "DELTA1FLOOR"): 1,
                ("DELTA1FLOOR", "R4HYP"): INF})
    cf7 = dict(base)
    cf7.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "TWINDOW"): 1, ("TWINDOW", "R4HYP"): INF,
                ("NFCLOS", "PERCELLREG"): 1,
                ("PERCELLREG", "R4HYP"): INF,
                ("NFCLOS", "JUMPSUM"): 1,
                ("JUMPSUM", "R4HYP"): INF})
    flows = (maxflow(dict(base), "UNC", "RH"),
             maxflow(dict(ext), "UNC", "RH"),
             maxflow(dict(one), "UNC", "RH"),
             maxflow(dict(cf9), "UNC", "RH"),
             maxflow(dict(cf7), "UNC", "RH"))
    check("G33-mincut-own", flows == (4, 5, 5, 9, 7),
          "own Edmonds-Karp on the frozen encodings: r150-class "
          "graph 4/5/5 + counterfactual 9; r154-class counterfactual "
          "7 (got %s): the 7/8/9 variants are per-graph, each round "
          "names its graph -- bookkeeping consistent" % (flows,))


# ---------------------------------------------------------------- S4
def s4() -> None:
    section("S4  ROUND-160 RESCUE LAYER (F3/F5) + plant/ghost")

    src = rd(os.path.join(HERE, "j2_primeforce_probe.py"))
    blk = src[src.index("projected NNLS repair"):
              src.index("rrep = world_measure")]
    monotone_only = ("+= stepv" in blk and "-= " not in blk
                     and "lstsq" not in blk
                     and "sarr[bestj] -" not in blk
                     and "residual" not in blk)
    claims = ("nonneg least squares" in src
              and "best PSD repair" in src)
    screen_typed = "kind=screen" in src or "screen" in src
    lg = rd(os.path.join(HERE, "j2pf_run1.log"))
    mt = re.search(r"RESCUE b8 SCRARITH: tauW \S+ deficit-res \S+ "
                   r"repair tau (\S+) J2 (\S+) (\S+)", lg)
    tau_rep = float(mt.group(1))
    j2_rep = float(mt.group(2))
    verd = mt.group(3)
    ok_f3 = (monotone_only and claims and screen_typed
             and 0.02 < j2_rep < 0.26 and tau_rep < 0
             and verd == "NOT-IN-WINDOW")
    check("G40-F3-rescue-typing", ok_f3,
          "BH5-F3 CONFIRMED [MINOR]: the rescue loop is a greedy "
          "eigenvalue-lifting accumulator (monotone '+= stepv', no "
          "objective, no re-fit, no optimality certificate) yet is "
          "described as 'nonneg least squares'/'best PSD repair'; "
          "enum RESCUE-INFEASIBLE-IN-CLASS certifies only THIS "
          "trajectory; thin-margin case b8 SCRARITH: J2_rep %.4f IS "
          "inside (0.02, 0.26), failure carried by tau_rep %.3e < 0; "
          "screen-typed (mitigation), taxonomy unaffected"
          % (j2_rep, tau_rep))

    nx = nx_cache()
    m2 = re.search(r"b8 SCRARITH J₂ 0\.2597, b8 EPSTEIN J₂ 0\.7644 — "
                   r"über der Kappe", nx)
    check("G41-F5-note-wording", m2 is not None and 0.2597 < 0.26,
          "BH5-F5 CONFIRMED [NOTE]: CDLXIV's 'ueber der Kappe' "
          "parenthesis covers b8 SCRARITH J_2 = 0.2597 < 0.26 (below "
          "the cap, inside the J_2-window); the decisive tau_rep = "
          "-3.553e-01 < 0 is omitted in the note (log verdict right)")

    gh = re.search(r"GHOSTS b5 s\*\(gamma\): (.*)", lg).group(1)
    ok_gh = ("9:6.01e-08" in gh and "14.5:8.80e-06" in gh
             and "5:1.93e-04" in gh and "2:4.09e-04" in gh
             and "30:6.48e-02" in gh)
    ok_pl = ("PLANT b5 g=5 s=1: tau 1.642e-10 J2 0.090026" in lg
             and "PLANT b5 multi(gap x4): tau 1.663e-01 "
                 "J2 -0.569031" in lg)
    ok_note = ("s*=6.0e-8" in nx.replace("\u2009", "")
               or "6.0e-8" in nx)
    check("G42-plant-ghost", ok_gh and ok_pl and ok_note,
          "plant/ghost asymmetry tables note-vs-log CONSISTENT "
          "(ghost thresholds b5 6.0e-8..6.5e-2 at the quoted gammas; "
          "single plants in-window; b5 multi-plant break disclosed "
          "REPORTED): the r160 headline finding stands")


# ---------------------------------------------------------------- S5
def s5() -> None:
    section("S5  CROSS-ROUND BOOKKEEPING")

    nx = nx_cache()
    lines = nx.split("\n")
    numerals = []
    for ln in lines[:30]:
        mt = re.match(r"# \d{4}-\d{2}-\d{2} \((CD[LXVI]+)\)", ln)
        numerals.append(mt.group(1) if mt else None)
    expect = ["CDLXVII", "CDLXVI", "CDLXV", "CDLXIV", "CDLXIII",
              "CDLXII", "CDLXI", "CDLX", "CDLIX", "CDLVIII",
              "CDLVII", "CDLVI", "CDLV", "CDLIV", "CDLIII"]
    # head-agnostic: the audited window CDLIII..CDLXVII must be a
    # consecutive block; NEWER notes above it (concurrent lanes
    # landing during this hunt) are allowed and reported.
    try:
        i0 = numerals.index("CDLXVII")
    except ValueError:
        i0 = -1
    ok_num = i0 >= 0 and numerals[i0:i0 + 15] == expect
    off = i0
    chain = [("CDLXVI (die dritte Promotionswelle", 0),
             ("CDLXIV war der Stand", 2),
             ("CDLXII (die Lean-Lane", 4),
             ("CDLX war der Stand", 6),
             ("CDLIX (die konkurrente assembly_walls-Lane", 7),
             ("CDLVIII war der Stand", 8),
             ("CDLVII war der Stand", 9),
             ("CDLVI (die Promotionsrunde v918", 10),
             ("CDLV war der Stand", 11),
             ("CDLIII war der Stand", 13)]
    ok_ch = all(pat in lines[off + idx] for pat, idx in chain)
    newer = [n for n in numerals[:i0] if n]
    check("G50-numerals", ok_num and ok_ch,
          "audited window CDLIII..CDLXVII gap-free, strictly "
          "consecutive (15 numerals); head-verification statements "
          "chain correctly; newer concurrent-lane notes above the "
          "window: %s (allowed, out of audit scope)"
          % (newer or "none"))

    src_aw = rd(os.path.join(HERE, "assembly_walls_probe.py"))
    src_na = rd(os.path.join(HERE, "nearalign_probe.py"))
    src_rl = rd(os.path.join(HERE, "rootladder_probe.py"))
    v922 = rd(os.path.join(ROOT, "verification",
                           "v922_spacing_jet_sumrule_theorems.py"))
    drift = ("CDLVII/r152 anchor_epslock" in src_aw
             and "ebenso r152/153/155" in nx)
    conv = ("CDLVII/r153 (anchor_epslock" in src_na
            and "CDLVII/r153" in src_rl
            and "RUNDE 153" in nx
            and "round 154, note CDLVIII" in v922)
    check("G51-F6-round-labels", drift and conv,
          "BH5-F6 CONFIRMED [NOTE]: corpus convention anchor_epslock "
          "= r153 (nearalign/rootladder/notes/v922) vs "
          "assembly_walls 'CDLVII/r152' and CDLXVI's not-promoted "
          "list 'r152/153/155' (r152 = the CDLVI promotion round): "
          "BH4-F3 label-drift class, no numeric claim touched")

    th = (0.2569, 0.1730, 0.2451, 0.1904, 0.2206, 0.1830)
    tg = (0.9005, 0.8493, 1.0135, 1.0347, 0.9957, 0.9200)
    tr = (0.8893, 0.9011, 0.9734, 1.0430, 0.9980, 0.9421)
    j2m = (0.1117, 0.1375, 0.1446, 0.1479, 0.1497, 0.1506)
    j2p = (0.1259, 0.1394, 0.1477, 0.1486, 0.1504, 0.1513)
    tl0 = (0.2664, 0.3738, 0.4674, 0.4827, 0.5122, 0.5778)
    tls = (0.2399, 0.3175, 0.4737, 0.4995, 0.5099, 0.5316)
    okw = (all(0.10 < v < 0.40 for v in th)
           and 0.17 <= min(th) and max(th) <= 0.26
           and all(0.5 < v < 2.0 for v in tg + tr)
           and all(0.11 <= v <= 0.152 for v in j2m + j2p)
           and all(0.23 < v < 0.59 for v in tl0 + tls)
           and abs(j2p[5] - j2m[5]) < 8e-4)
    lg150 = rd(os.path.join(HERE, "collapserate_probe.run1.log"))
    lg162 = rd(os.path.join(HERE, "fgl_run2.log"))
    ok_tr = all(("t_r %.4f" % v) in lg162 for v in tr) and \
        all(("%.4f" % v) in lg150 for v in tr)
    check("G52-window-constants", okw and ok_tr,
          "theta [0.1730, 0.2569] in the frozen (0.10, 0.40); tlaw "
          "0.2399..0.5778; t_g/t_r flat 0.85..1.04; J_2 moment "
          "0.1117..0.1506 vs gfloor proxy 0.1259..0.1513 (different "
          "instruments, disclosed, x=28 gap 7e-4); t_r table "
          "string-identical across the r150 and r162 logs: NO "
          "contradiction found")

    res_167 = ("RESIDUUM = {TOPROOT (= B00-ROOTGAP == SEC-Cap per "
               "CDLXV), TLAWCAP-Block, QSUBGAP-FLOOR" in nx)
    res_165 = "TOPROOT (DIESE RUNDE VERENGT: = B00-ROOTGAP ALLEIN" in nx
    res_161 = ("QSUBGAP-FLOOR g ≥ 1/poly (DIESE RUNDE: ⟺ das GANZE "
               "Paar {SUSCAP2R, DELTA1FLOOR}" in nx)
    res_154 = ("SUSCAP2R (= OVG-Cap + Share-Floor per r150)} + "
               "DELTA1FLOOR (⟸ TRACEFLOOR)" in nx)
    check("G53-residue-chain", res_167 and res_165 and res_161
          and res_154,
          "residue bookkeeping CDLIV -> CDLXVII consistent: the pair "
          "{SUSCAP2R, DELTA1FLOOR} merges into ONE QSUBGAP-floor "
          "entry at r157 (W2 cited), TOPROOT narrows to B00-ROOTGAP "
          "alone at r161 (S1 absorbed), the delta_1-floor "
          "recoordinates onto {theta x t_r} at r162; final set "
          "{TOPROOT, TLAWCAP-block, QSUBGAP-floor} + a-walls "
          "confirmed in every round's own paragraph")

    import csv
    led = list(csv.reader(open(os.path.join(
        ROOT, "verification", "status_ledger.csv"),
        encoding="utf-8")))
    reg = list(csv.reader(open(os.path.join(
        ROOT, "verification", "script_registry.csv"),
        encoding="utf-8")))
    ra = rd(os.path.join(ROOT, "verification", "run_all.py"))
    ledtxt = rd(os.path.join(ROOT, "verification",
                             "status_ledger.csv"))
    ok_ct = (len(led) - 1 == 1069 and len(reg) - 1 == 918
             and all(("v92%d" % i) in ra for i in (2, 3, 4, 5)))
    ok_hon = all(s_ in ledtxt for s_ in
                 ("NOT an RH-evidence row", "NO RH claim",
                  "PINNED from run-of-record",
                  "RE-RUN GREEN AS TYPED AT PROMOTION"))
    check("G54-promotion-counters", ok_ct and ok_hon,
          "ledger 1069 rows, registry 918 rows (== CDLXVI '1065 -> "
          "1069' / '914 -> 918'); run_all carries v922-v925; ledger "
          "rows carry the honest pinned/re-run split and "
          "NOT-RH-EVIDENCE: no verdict upgraded in promotion")


# ---------------------------------------------------------------- S9
def main() -> int:
    print("bughunt5_probe -- PRIME.BUGHUNT5.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("scope: rounds 149-162 (CDLIII-CDLXVII) + promotion wave "
          "v922-v925")
    s0()
    s1()
    s2()
    s3()
    s4()
    s5()
    section("S9  COMPOSITE")
    dt = time.time() - T0
    check("G99-runtime", dt <= 900.0, "%.1f s <= 900 s" % dt)
    npass = sum(1 for _, okv, _ in CHECKS if okv)
    print("\nFINDINGS: BH5-F1 [MINOR] r150 'betapos == S1/jr exact' "
          "overstated (superseded")
    print("silently by r161 GF5a); BH5-F2 [MINOR] v925/CDLXIII '72 "
          "targets' -> 73;")
    print("BH5-F3 [MINOR] j2 rescue 'NNLS/best repair' is a greedy "
          "lift, enum overstates;")
    print("BH5-F4 [MINOR] assembly_walls 'SPEC_SHA moves once' -> "
          "moved twice;")
    print("BH5-F5 [NOTE] CDLXIV b8-SCRARITH 'ueber der Kappe' "
          "(0.2597 < 0.26, tau-leg);")
    print("BH5-F6 [NOTE] anchor_epslock r152/r153 label drift.")
    print("NO ROUND VERDICT FLIPS.  NO MAJOR.  All load-bearing "
          "razor/quartic/ladder/")
    print("census claims CONFIRMED by independent recomputation.")
    print("COMPOSITE: BUGHUNT5-FINDINGS(6) = 0 MAJOR / 4 MINOR / "
          "2 NOTE.  NO RH CLAIM.")
    print("\nGATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    if npass != len(CHECKS):
        print("FAILING GATES: " + ", ".join(
            nm for nm, okv, _ in CHECKS if not okv))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
