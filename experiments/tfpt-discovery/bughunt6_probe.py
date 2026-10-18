#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt6_probe -- PRIME.BUGHUNT6.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  Sixth adversarial audit:
the ENDGAME rounds 163-169 (probes selberg_effective / bughunt5 /
novelty_synthesis / tau_blockaverage / window_instrument /
depthblock_transfer / sigmafloor; notes CDLXVIII-CDLXXXIV; the
coordinator commit messages d831f15e / d99c3f4b / 48c2c2da of the
freeze convention).  Predecessors r87/r109/r130/r149/r164.  This probe
writes NOTHING but stdout, reads the frozen corpus READ-ONLY (probe
sources as text, kept run/smoke/calib logs, next.txt, the X5 zero
cache inside a ward_ function, and the three pinned commit messages
via read-only `git show` on frozen hashes), imports NO frozen probe
except the round-114 builder machinery radius4_an_probe (the corpus
convention for source-cell recomputation; every audit computation
below on top of it is an OWN implementation), and makes NO RH CLAIM
in either direction.  Every confirmed finding carries at least one
falsifiable gate.

METHOD (bughunt I-V standard): (B1) the r168 theorem layer re-derived
INDEPENDENTLY -- DT2 recipe chase + dyadic factor + 2^{3/2} limit +
monotone bracket on OWN sympy variables; the census 3/2-law limit
3 pi/kappa and the r169 SF4 general-a limits 2 pi(3/2+a)/kappa at
a in {0, 1/2, 1, 3/2} on an OWN G_lead; the SF1 anatomy identity +
delta x DC factorization on an OWN rational instance (different
numbers than the frozen probe); the SF2 rate-floor chase; (B2) the
r131 OFF-recipe PROVENANCE adjudicated by reading l1_weyllaw_probe
Layer 2/3: the e^A = sqrt(h) factor is the OFF-LINE STRIP allowance
|E(t + id)| <= e^{A d}(2/t)ENV with 2d <= 1 for potentially off-line
zeros above T_PT -- the +1/2 in the census-demand exponent 3/2 is
EXACTLY the price of not assuming RH beyond the verified census
(coherent with the RH-loop adjudication; PROVEN-BY-RECIPE typing
JUSTIFIED); (B3) the r166/r168 SUBSTRATE independently recomputed:
the full B2 block [4, 8] rebuilt from the round-114 builder with OWN
enclosure code (own Rayleigh upper, own Cholesky PD certificate at
tau_up(1 - 1e-3)), OWN jets/eta/OFF recipe port, OWN tail zsum
(Z_OVERHANG 6.0, slop 1e-3) -- block enclosure, budget row, tlaw and
sigma strings, and the DT2 recipe identity re-verified against the
frozen record strings; (B4) Bertrand re-sieved OWN to 1e6; the PT21
horizon h* and the census-demand inversion re-solved with an OWN
HSW-G implementation; (B5) the min-cut flows re-verified with an OWN
Edmonds-Karp on the r168/r169 graph encodings (4/5/5/9 + RH
unreachable without omega edges); the G63 cycle detections
replicated with an OWN DFS, and the reachability SEMANTICS
adjudicated (OR-reach vs AND-fire, finding F4); (B6) provenance:
SPEC_SHA of all 7 round probes recomputed from the docstrings and
matched against EVERY kept log; all hash moves accounted against the
disclosed amendment/smoke lineage (r163 7cfe->6ed9 disclosed in
CDLXVIII; r166 abfc->0d4e->d86f = Amendments 1+2; r167
8e06->a17e->bfdc = Amendments 1+1a incl. the killed duplicate
re-run; r169 eed8->a16a = Amendment 1; r164/r165/r168 single-hash
clean); deterministic re-run pairs re-diffed with an OWN
timing-token normalizer; (B7) the COMMIT-MESSAGE LAYER audited
against the record logs (the contract's new surface): STEP counts,
gate counts, the ENTRY-NEW pattern wording, the "bit-identical"
wording; (B8) cross-round bookkeeping: numerals CDLXVIII-CDLXXXIV
gap-free/unique with the two concurrent sessions' attribution
verified (probe files present; independent-session files uncommitted
per the commit disclosures), the sigma12/tlaw record ladders
transported r168 -> r169 at rel 1e-3, the window-constant tables
(TLAW/FG/CTRL/SIGMA/HSW/T_PT/h*) string-identical across r168/r169
and consistent with the r165 definitive table; (B9) the r163
pricing-table constants spot-checked against the CITED PAPERS
(external web verification 2026-08-19, results pinned here):
HSW22 Cor. 1.2 == 0.1038 log T + 0.2573 loglog T + 9.3675 EXACT,
Cor. 1.4 == min{... + 8.3675, 0.1095 log T + 0.2042 loglog T +
3.0305} EXACT; Bellotti-Wong (arXiv:2412.15470, Math. Comp. 2025)
Cor. 1.5 == 0.10076 log T + min{0.24460 loglog T + 7.20844, 1.68845
loglog T + 1.50956} EXACT; Platt-DB |S| <= 2.5167 for T <= 3.061e10
EXACT (quoted in both papers); PT21 == 3 000 175 332 800 EXACT; the
r165 Yoshida-1992 blocking claim verified against the source
(ASPM 21, doi:10.2969/aspm/02110281, Proposition 2: RH <==>
positive definiteness of the Weil hermitian form on C(a) for EVERY
a > 0 -- exactly the cofinal-window shape; the priority blockade is
VALID and externally load-bearing).

=======================================================================
FINDINGS LEDGER (the deliverable; severity frozen; gates named)
=======================================================================
BH6-F1 [MINOR][commit-layer overstatement, entry law]  The round-168
  freeze commit d831f15e states 'ENTRY-NEW-CONFIRMED(the second
  discovery: cone entry ALWAYS at the LARGEST NEW PRIME ATOM of the
  dyadic gap, 4/4 batteries, ...)'.  The record (dbt_run1.log) has
  entry atoms u = log 7 / log 9 / log 13 / log 17 at the pairs
  (4,8)/(5,10)/(8,16)/(9,18).  Atom 9 = 3^2 is NOT prime, and NO
  consistent reading of the commit phrase reaches 4/4: 'largest new
  prime atom' matches 3/4 (fails (5,10): largest new prime is 7,
  entry is 9); 'largest new atom' matches 2/4 (fails (4,8): largest
  new atom is 8 = 2^3, entry is 7; fails (8,16): largest is 16 =
  2^4, entry is 13).  Only the note CDLXXXIII's careful formulation
  -- largest new PRIME-POWER atom EXCLUDING the trailing powers of
  two, 'die nachlaufenden Zweierpotenz-Atome bewegen den Grund nicht
  mehr' -- fits 4/4, and the probe docstring's own law
  (FINAL-NEW-BLOCK-TAIL) is correct.  The commit layer is load-
  bearing citable documentation under the freeze convention; the
  wording drops both qualifiers.  No gate, log or note is wrong;
  recommended correction of record: cite the pattern in the note's
  formulation.  GATE: G10 (log parse + own prime-power arithmetic
  over the four gaps + commit-text conjunction).
BH6-F2 [NOTE][commit-layer wording, determinism claim]  The r168
  commit says '1971 s record + bit-identical re-run' and the r167
  commit 'record + bit-identical deterministic re-run'.  The raw
  log pairs are NOT bit-identical: dbt_run1/run2 differ in 5 line
  pairs, sf_run2/run3 in 4 (wall-clock tokens only; the OWN
  normalizer confirms timing-normalized EMPTY, and the notes
  CDLXXXIII/CDLXXXIV state exactly that, correctly).  Earlier
  freeze commits used the precise form 'result lines bit-identical'
  (r160 class).  Wording only; no numeric content touched.  GATE:
  G11 (own raw diff counts + own normalizer + commit-text greps).
BH6-F3 [MINOR][vacuous machine-check legs in PROVEN-typed exact
  gates]  Two exact-layer gate legs are tautologies that cannot
  fail and verify nothing beyond 'X == X', yet are presented inside
  PASS-gated PROVEN-typed gates as if they were checks: (i) r168
  G10 (DT1) leg okD 'cofinality: hits h_k >= 2^k unbounded' is
  coded as all(2**k >= 2**k) -- the intended statement (the
  positive rung of block B_k sits at height >= 2^k, so block hits
  are cofinal) is true by block membership but is NOT what the code
  checks; (ii) r169 G11 (anti-lattice) leg okH 'E == sin x R: E ==
  0 needs sin == 0 or R == 0 (product ring)' is coded as
  simplify(sin(az)R - sin(az)R) == 0.  Both theorems remain true
  (the corpus's DT1 chain and the anti-lattice reduction are not
  touched; the mathematical steps are elementary), no verdict
  flips; per the corpus's own COJ/exactness standard the
  VERIFICATION content of these two legs is overstated.
  Recommended: re-code the legs against the actual objects (block
  rung heights; a nonzero-product witness) or type them
  DEFINITIONAL in the gate detail.  GATE: G12 (source-text
  conjunction on both frozen probes).
BH6-F4 [NOTE][graph-semantics precision, silent cross-round
  correction -- BH5-F1 class]  r168 G63(ii) claims the per-k
  schedule + sigma-floor grant 'reaches RH acyclically through
  EITHER typed arrow' and gates it by PLAIN DIGRAPH REACHABILITY
  (rh_reach = RH in reachable(chain_perk, SIGMAFLOOR)): under
  OR-semantics every edge is sufficient, so RH is 'reachable' from
  SIGMAFLOOR alone although the assembly needs the other parents
  (BA3, EPSLAW, CENSUS_K grants, and CARRIER_LEM resp. NFCLOS +
  {L1, WPD}) -- machine-shown here: an AND-fire propagation from
  {SIGMAFLOOR} alone does NOT fire RH; with the full counterfactual
  grant set it does.  r169 G63(iii) adds the missing caveat
  '(AND-semantics: all parents needed; reachability shown per
  grant)' -- but no surface flags that r168's frozen gate text
  needed the same qualification: a silent cross-round precision.
  The r168 gate's own conclusion (COFINAL-TARGET-ASSEMBLY-
  CONDITIONAL, not a loop) is UNAFFECTED, and the RH-loop cycle
  detections (i)/(ii) are semantics-independent (every cycle edge
  is a genuine implication).  GATE: G13 (own OR-reach replication +
  own AND-fire refutation + source greps on both rounds).
BH6-F5 [NOTE][evidence bookkeeping, smoke numbering -- BH5-F4
  class]  Round 167's kept smoke logs are wi_smoke1/3/4 (hashes
  8e06/a17e/bfdc, all green at their hashes).  No wi_smoke2 exists,
  and no surface (the window_instrument docstring mentions only
  'smoke had passed 31/31'; note CDLXXXI contains no smoke
  accounting at all) explains the numbering gap.  Both re-freezes
  themselves are fully disclosed (Amendments 1 + 1a incl. the
  killed duplicate re-run); the gap touches no result.  GATE: G14
  (directory listing + source/note greps).
BH6-F6 [NOTE][always-pass screen gate]  r168 G47-deep-pairs-screen
  is coded check("G47...", True, ...): the computed per-pair screen
  legs (scr_ok: base pattern + tailpos + t*/tangent) are PRINTED
  but not wired into the gate verdict, so the gate cannot fail by
  construction; only the entry-NEW bits feed the ENTRY-NEW-{...}
  enum.  The kind="screen" typing and the pre-freeze-unmeasured
  disclosure make this borderline-legal corpus practice ('screen'
  is also not a special kind in check(), edge/exact only); flagged
  because a reader of '4/4 pairs' in the enum may assume the full
  screen battery is gated.  GATE: G15 (source-text check: literal
  True verdict + scr_ok not consumed).

CHECKED CLEAN (adversarially, no finding): DT2 re-derived (recipe
chase, dyadic factor, 2^{3/2} limit, (3L+1)/2 bracket) on own
symbols; the r131 OFF-recipe provenance TRACED AND JUSTIFIED (the
sqrt(h) = e^A factor is the off-line strip allowance for zeros above
T_PT -- the census 3/2-law's +1/2 exponent is the no-RH-beyond-
census price, and the recipe is a certified bound built from PT21 +
HSW22 + the Layer-3 jet telescope: PROVEN-BY-RECIPE is an honest
typing); the census 3/2-law and the r169 SF4 general-a absorption
limits re-derived by own sympy (2 pi(3/2 + a)/kappa == (3 pi/c)(1 +
2a/3) exact); h* = 1.2566e7 and k* = 23.58 re-solved with an own G
implementation (rel 2e-3), the census inversion re-run on the own G
(T_req/H^{3/2} falling toward 3 pi/sigma_0 = 62.83, exponent fit in
(1.40, 1.60)); Bertrand re-sieved own to 1e6 (interface never
empty); SF1 anatomy identity + delta x DC factorization re-derived
on an OWN rational instance and re-verified on real data through
the OWN B2 recompute; SF2 cap-is-upper refutation + rate-floor
chase re-derived; THE B2 SUBSTRATE INDEPENDENTLY RECOMPUTED (own
enclosure/jets/OFF/zsum code on the round-114 builder): block
enclosure [2.1410e-11, 2.1431e-11], budget row 1.8949e-11, tlaw
strings 0.232537/0.2664/0.3738, sigma strings 0.205602/0.255783/
0.356579 all replicated rel 5e-3, recipe identity dev <= 1e-40 at
every rung 4..8 -- the r166 certificates and the r168 GW-currency
pair verify end-to-end under independent reimplementation; min-cut
flows 4/5/5/9 replicated with an OWN Edmonds-Karp + RH unreachable
without omega edges; the G63 universalized-census cycle and the
r169 pinning-supply cycle replicated with an OWN DFS (the loop
detections are sound; the graphs are hand-declared and typed as
such); SPEC_SHA integrity across all SEVEN rounds (every kept log
accounted, every hash move disclosed -- r163's smoke respec, r166's
two amendments with run1/run2 G34 fails kept as records, r167's two
owner-directive re-freezes with the killed duplicate re-run
disclosed, r169's Amendment 1 with the run1 fail row kept: the
honest-amendment discipline HELD across the endgame); the two r168
pre-record smoke fixes (sigma-string smoke gating; the transposed-
digit log-7 constant 1.945910109 -> 1.945910149) disclosed in note
CDLXXXIII and quantitatively consistent with the kept smoke diffs;
the r169 Amendment-1 fit window recomputed (15 onset rungs 4..18,
clean set == the 12 rungs 4..15 under onset_0.5 <= gamma_top/2,
h=18's 4816 > 3632 excluded; own log-log fits reproduce a_all ~
2.063 and a_clean ~ 1.33 from the record ladders); note claims vs
logs verified for CDLXXXIII/CDLXXXIV (gate counts 36/36 + 35/35,
SHAs, runtimes, smoke/run fail accounting); the STEP instantiation
counts (9/9, 11/11) commit == log; the sigma12/tlaw ladders
transported r168 record -> r169 frozen tables at 4-decimal
identity; TLAW/FG/CTRL/SIGMA/HSW/T_PT/HSTAR tables string-identical
across the r168/r169 sources and consistent with the r165
definitive window table; numerals CDLXVIII-CDLXXXIV gap-free,
unique, attribution verified (audited rounds' notes name their
probe files; the independent session's numerals CDLXXVI-CDLXXX +
CDLXXXII have their probe files present and deliberately
uncommitted per the commit disclosures); the r163 literature
constants EXACT against the cited papers (spot-check 2+: HSW22,
BW24/25, Platt-DB, PT21); the r165 Yoshida-1992 priority blockade
VALID against the source; r169's G43 'h-only criterion' wording
adjudicated acceptable (the criterion consumes measured onsets, is
declared so in the amendment, and does not depend on the fitted
quantity); the DC-classical boundary verified (Landau/Gonek
consumed AS FORM only -- shape limits in G13, constants unpriced,
GONEK-FORM honestly declared an ancestor of the delivered chain).

THE DEFINITIVE TYPED ENDGAME CHAIN (the survival verdict; every
arrow re-checked against its source round):
  A1 SUBSTRATE h <= 28 (r166 BA1/BA2 enclosures + wall chain)
     PROVEN (machine certificates; re-verified here on B2).
  A2 BA3 budget floor tau >= zsum - OFF
     PROVEN-MOD-CITED {PT21, HSW22, r131 OFF recipe}; hard h <= 26;
     h = 27/28 F64-ORDINATE-LIMITED measured (disclosed).
  A3 DT2 demand law eps = sqrt(h)(1+eta)^2 G(T_PT)/G(2 pi h)
     PROVEN-BY-RECIPE (exact chase; sqrt(h) = off-line strip
     allowance -- recipe provenance traced, F-clean).
  A4 census 3/2-law + horizon (T_req -> (3 pi/sigma_0) h^{3/2},
     h* = 1.2566e7)  PROVEN (limit) + COMPUTED; recipe-relative
     through A3 (a sharper certified off-line bound would lower
     the exponent toward 1; the unbounded-census conclusion and
     NO-SELF-SUPPORTING-INDUCTION survive any recipe).
  A5 STEP below horizon (B2 -> B3 9/9, B3 -> B4p 11/11)
     PROVEN-ON-DATA + SUBSTRATE-DIRECT (B_k not consumed).
  A6 SIGMA-FLOOR (the final coordinate)  MEASURED (flat 0.21 ->
     0.52), arithmetic-pinned; factorized EXACT by r169 SF1 into
     delta x DC (identity re-derived + re-instantiated here).
  A7 DC leg -> 1/2  PROVEN-MOD-CITED per census (Landau 1912 +
     Gonek 1993 AS FORM, GONEK-CONSTANT-UNPRICED; ALL-K grant ==
     the machine-flagged RH loop).
  A8 JET-MASS floor delta >= r(h)  THE TERMINAL MEASURED RESIDUE
     (rate form via measured JET-LOCK onsets ~x^2.2, clean fit
     CACHE-TOP-LIMITED beyond onset <= gamma_top/2 -- Amendment 1
     honest; lambda-uniform rate OPEN).
  A9 entry carrier (b-route)  Bertrand interface PROVEN-CITED +
     sieve-gated; entry-at-new-atom MEASURED 4/4; entry position
     ARITHMETIC (algebra-only refuted).
  A10 HCOF ==> RH  CLASSICAL-CONDITIONAL two ways (ARROW-Y
     CARRIER_LEM = Weil/Yoshida form; ARROW-N NFCLOS + {L1, WPD});
     census C6/C7 untouched; universalized census AND
     pinning-supply both machine-flagged LOOPS, never consumed.
  RESIDUE: {JET-MASS rate floor} + {census ALL-K == LOOP} +
  {L1, WPD}; omega census {MEAS, OMEGA-POS} cardinality 4
  UNCHANGED.  VERDICT: THE ENDGAME CHAIN SURVIVES BUGHUNT VI AS
  TYPED -- no arrow is claimed stronger anywhere in probes, notes
  or ledgers than its source round justifies; the two MINOR
  findings live in the commit-wording layer and in two decorative
  verification legs, and flip nothing.

FROZEN NUMERICS (audit pins; sources = frozen record logs/specs):
COMMITS: R168 = d831f15e, R167 = d99c3f4b, R166 = 48c2c2da.
LINEAGES: r163 {smoke1: 7cfe35eb9d779df6, final: 6ed98ca787fffc0c};
r164 {final: b466fd5e6dcbc640}; r165 {final: 6e1c8d106e6b9fe0};
r166 {abfc5932f95cb8ea, 0d4ef50122c334f6, final d86f42a04c69a4e2};
r167 {8e064879b50df7ef, a17e85a0867c6935, final bfdcf374504006e7};
r168 {final: a4cd07144e0c5222}; r169 {eed821a2469a0dc1, final
a16a4db1055488d2}.  ENTRY_ATOMS = {(4,8): 7, (5,10): 9, (8,16): 13,
(9,18): 17}.  B2 strings: ENC = (2.1410e-11, 2.1431e-11), BUDGET =
1.8949e-11, TLAW = {4: 0.232537, 5: 0.2664, 6: 0.2729, 7: 0.3264,
8: 0.3738}, SIGMA = {4: 0.205602, 5: 0.255783, 6: 0.2608,
7: 0.3104, 8: 0.356579}, rel 5e-3; RECIPE_BAR 1e-40.  HSTAR =
1.2566e7 rel 2e-3; KSTAR in (23.3, 23.9); KAPPA_INF = 3 pi/0.15 =
62.8319; CENSUS_SLOPE in (1.40, 1.60).  RATE fits: a_all = 2.063
abs 0.08, a_clean = 1.328 abs 0.08 (own fits on the 4-decimal
record ladders); N_ONSET = 15, N_CLEAN = 12.  DIFF pairs: dbt 5,
sf 4 (raw), 0 (normalized).  MINCUT = (4, 5, 5, 9).  RUNTIME_BAR =
900 s.  Deterministic: no RNG; git reads pinned to frozen hashes.
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.

VERDICT ENUM (frozen): BUGHUNT6-FINDINGS(6: 0 MAJOR / 2 MINOR /
4 NOTE) + ENDGAME-CHAIN-SURVIVES-AS-TYPED + SUBSTRATE-REVERIFIED-
INDEPENDENT(B2) + RECIPE-PROVENANCE-TRACED(off-line strip) +
PROVENANCE-ALL-MOVES-DISCLOSED + LITERATURE-PINS-EXACT +
YOSHIDA-BLOCKADE-VALID.  NO verdict of rounds 163-169 flips.

AST FIREWALL: no zero-oracle names; np.load only inside ward_*;
NO zeta use; no import of verification/.  NO RH CLAIM.
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

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4          # round-114 builder machinery

REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
NEXT = os.path.join(HERE, "..", "next.txt")
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

R168_COMMIT = "d831f15e"
R167_COMMIT = "d99c3f4b"
R166_COMMIT = "48c2c2da"

ROUNDS = {
    "r163": ("selberg_effective_probe.py",
             {"selberg_effective_probe.smoke1.log": "7cfe35eb9d779df6",
              "selberg_effective_probe.smoke2.log": "FINAL",
              "selberg_effective_probe.run1.log": "FINAL",
              "selberg_effective_probe.run2.log": "FINAL"}),
    "r164": ("bughunt5_probe.py",
             {"bughunt5_probe.run1.log": "FINAL",
              "bughunt5_probe.run2.log": "FINAL"}),
    "r165": ("novelty_synthesis_probe.py",
             {"nsp_smoke1.log": "FINAL", "nsp_smoke2.log": "FINAL",
              "nsp_run1.log": "FINAL", "nsp_run2.log": "FINAL"}),
    "r166": ("tau_blockaverage_probe.py",
             {"tba_smoke1.log": "abfc5932f95cb8ea",
              "tba_run1.log": "abfc5932f95cb8ea",
              "tba_run2.log": "0d4ef50122c334f6",
              "tba_run3.log": "FINAL", "tba_run4.log": "FINAL"}),
    "r167": ("window_instrument_probe.py",
             {"wi_smoke1.log": "8e064879b50df7ef",
              "wi_run1.log": "8e064879b50df7ef",
              "wi_smoke3.log": "a17e85a0867c6935",
              "wi_run2.log": "a17e85a0867c6935",
              "wi_smoke4.log": "FINAL",
              "wi_run3.log": "FINAL", "wi_run4.log": "FINAL"}),
    "r168": ("depthblock_transfer_probe.py",
             {"dbt_smoke1.log": "FINAL", "dbt_smoke2.log": "FINAL",
              "dbt_smoke3.log": "FINAL",
              "dbt_run1.log": "FINAL", "dbt_run2.log": "FINAL"}),
    "r169": ("sigmafloor_probe.py",
             {"sf_smoke1.log": "eed821a2469a0dc1",
              "sf_run1.log": "eed821a2469a0dc1",
              "sf_run2.log": "FINAL", "sf_run3.log": "FINAL"}),
}

ENTRY_ATOMS = {(4, 8): 7, (5, 10): 9, (8, 16): 13, (9, 18): 17}
B2_ENC = (2.1410e-11, 2.1431e-11)
B2_BUDGET = 1.8949e-11
B2_TLAW = {4: 0.232537, 5: 0.2664, 6: 0.2729, 7: 0.3264, 8: 0.3738}
B2_SIGMA = {4: 0.205602, 5: 0.255783, 6: 0.2608, 7: 0.3104,
            8: 0.356579}
STR_TOL = 5e-3
RECIPE_BAR = 1e-40
T_PT = 3000175332800
HSW = (0.1038, 0.2573, 9.3675)
KFAC = 1.25
Z_OVERHANG = 6.0
F64_SLOP = 1e-3
NZSUM = 1200
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
DPSB2 = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80}
HSTAR = 1.2566e7
HSTAR_TOL = 2e-3
KSTAR_WIN = (23.3, 23.9)
KAPPA_INF = 3 * math.pi / 0.15
CENSUS_SLOPE_WIN = (1.40, 1.60)
RATE_ALL = 2.063
RATE_CLEAN = 1.328
RATE_ABS = 0.08
N_ONSET, N_CLEAN = 15, 12
DIFF_PAIRS = {"dbt": 5, "sf": 4}
MINCUT = (4, 5, 5, 9)
RUNTIME_BAR = 900.0
GAMMA1_LIT = 14.134725141734693790   # ward only

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
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno)
                for n in ast.walk(node))))

    def owners(lineno):
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

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
            if not any(f.startswith("ward_")
                       for f in owners(node.lineno)):
                bad.append("np.load outside ward_ @%d" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta; cache in ward_; "
                       "no verification/ import; git reads pinned "
                       "read-only")


def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def git_msg(sha: str) -> str:
    out = subprocess.run(["git", "-C", REPO, "show", "-s",
                          "--format=%B", sha],
                         capture_output=True, text=True, check=True)
    return out.stdout


# --------------------------------------------------------- own helpers
def own_G(T, dps: int = 60):
    """OWN implementation of the corpus HSW-G closed form (r131 T2)."""
    with mp.workdps(dps):
        Tm = mp.mpf(T if isinstance(T, str) else repr(float(T)))
        al, be, cc = (mp.mpf(repr(v)) for v in HSW)
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return t1 + t2 + t3


def prime_powers(n: int) -> list[tuple[int, int]]:
    """[(q, p)] prime powers q <= n, own sieve."""
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
    out.sort()
    return out


def normalize_timing(text: str) -> str:
    text = re.sub(r"\b\d+(?:\.\d+)?\s?s\b", "S", text)
    text = re.sub(r"\(\d+s\)", "(S)", text)
    text = re.sub(r"runtime \S+", "runtime S", text)
    text = re.sub(r"wall \S+", "wall S", text)
    return text


def raw_diff_lines(a: str, b: str) -> int:
    la, lb = a.splitlines(), b.splitlines()
    n = 0
    for x, y in zip(la, lb):
        if x != y:
            n += 1
    n += abs(len(la) - len(lb))
    return n


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


def maxflow_own(edges: dict, s: str, t: str) -> int:
    """OWN Edmonds-Karp (independent of R4.maxflow)."""
    cap = {}
    adj = {}
    for (u, v), c in edges.items():
        cap[(u, v)] = cap.get((u, v), 0) + c
        cap.setdefault((v, u), 0)
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    flow = 0
    while True:
        par = {s: None}
        queue = [s]
        while queue and t not in par:
            u = queue.pop(0)
            for v in sorted(adj.get(u, ())):
                if v not in par and cap.get((u, v), 0) > 0:
                    par[v] = u
                    queue.append(v)
        if t not in par:
            return flow
        path = []
        v = t
        while par[v] is not None:
            path.append((par[v], v))
            v = par[v]
        aug = min(cap[e] for e in path)
        for (u, v) in path:
            cap[(u, v)] -= aug
            cap[(v, u)] += aug
        flow += aug


def has_cycle_own(g: dict) -> bool:
    color = {}

    def dfs(u):
        color[u] = 1
        for v in g.get(u, ()):
            c = color.get(v, 0)
            if c == 1 or (c == 0 and dfs(v)):
                return True
        color[u] = 2
        return False

    return any(dfs(n) for n in list(g) if color.get(n, 0) == 0)


def or_reach(g: dict, src: str) -> set:
    seen = {src}
    st = [src]
    while st:
        u = st.pop()
        for v in g.get(u, ()):
            if v not in seen:
                seen.add(v)
                st.append(v)
    return seen


def and_fire(g: dict, seeds: set, or_nodes: set) -> set:
    """OWN AND-semantics propagation: a non-seed node fires iff ALL
    its parents fired (OR at the declared disjunction nodes)."""
    parents = {}
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
            if not ps:
                continue
            ok = (any(p in fired for p in ps) if n in or_nodes
                  else all(p in fired for p in ps))
            if ok:
                fired.add(n)
                changed = True
    return fired


# ------------------------------------------------------- B2 recompute
def b2_rung(h: int, gam: np.ndarray) -> dict:
    """OWN recompute of enclosure + jets/OFF + zsum + sigma/eps/tlaw
    on the round-114 builder cell (independent audit code)."""
    dps = DPSB2[h]
    ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    with mp.workdps(dps):
        M = ce["mpM"]
        E = ce["mpE"]
        V = ce["mpV"]
        v0 = [V[i, 0] for i in range(K)]
        n0 = mp.sqrt(sum(v * v for v in v0))
        v0 = [v / n0 for v in v0]
        Mv = [sum(M[i, k] * v0[k] for k in range(K)) for i in range(K)]
        ray = sum(v0[i] * Mv[i] for i in range(K))
        tau_up = ray if ray > E[0] else E[0]
        tau_lo = tau_up * (1 - mp.mpf("1e-3"))
        Ms = M.copy()
        for i in range(K):
            Ms[i, i] = Ms[i, i] - tau_lo
        try:
            mp.cholesky(Ms)
            pd_ok = True
        except Exception:                          # noqa: BLE001
            pd_ok = False
        aa = mp.log(h) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0 = sum((-1) ** k * cs[k] for k in range(K))
        b = [o * o for o in oms]
        cs_abs = [abs(v) for v in cs]
        A_j = [A0]
        pw = [mp.mpf(1)] * K
        for m in range(1, M_JETS + 1):
            acc = mp.mpf(0)
            for k in range(1, K):
                pw[k] = pw[k] * b[k] if m > 1 else b[k]
                acc += (-1) ** k * cs[k] * pw[k]
            A_j.append(acc)

        def envres(Tq, mm):
            yq = mp.mpf(repr(float(Tq))) ** 2
            acc = mp.mpf(0)
            yi = mp.mpf(1)
            for i in range(1, mm + 1):
                yi *= yq
                acc += abs(A_j[i]) / yi
            rem = mp.mpf(0)
            for k in range(1, K):
                rem += cs_abs[k] * b[k] ** (mm + 1) / (yi * (yq - b[k]))
            return acc + rem

        eta = min(envres(T_PT, m) for m in MGRID) / abs(A0)
        GPT = mp.mpf(mp.nstr(own_G(T_PT, dps), dps))
        off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta)) ** 2 * GPT
        Tz = 2 * math.pi * h
        zsum = mp.mpf(0)
        for g in gam[:NZSUM]:
            gf = float(g)
            if gf <= Tz + Z_OVERHANG:
                continue
            gm = mp.mpf(repr(gf))
            Rv = 2 * cs[0] / gm
            for k in range(1, K):
                Rv += 2 * cs[k] * (-1) ** k * gm / (gm * gm - b[k])
            ev = mp.sin(aa * gm) * Rv
            zsum += 2 * ev * ev
        zsum_c = zsum * (1 - mp.mpf(repr(F64_SLOP)))
        Gz = mp.mpf(mp.nstr(own_G(Tz, dps), dps))
        den = 8 * A0 * A0 * Gz
        sig = zsum_c / den
        eps = off / den
        eps_form = mp.sqrt(h) * (1 + eta) ** 2 * GPT / Gz
        return dict(h=h, pd_ok=pd_ok,
                    tau_lo=mp.nstr(tau_lo, 40),
                    tau_up=mp.nstr(tau_up, 40),
                    zsum=mp.nstr(zsum_c, 40), off=mp.nstr(off, 40),
                    tlaw=float(E[0] / den), sigma=float(sig),
                    recipe_dev=float(abs(eps / eps_form - 1)))


def eps_closed_own(h: float) -> float:
    return float(mp.sqrt(h) * own_G(T_PT) / own_G(2 * math.pi * h))


def solve_hstar_own(sigma0: float) -> float:
    lo, hi = 1e2, 1e12
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if eps_closed_own(mid) < sigma0:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("bughunt6_probe -- PRIME.BUGHUNT6.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")
    gtop = float(gam[-1])

    dbt_src = rd("depthblock_transfer_probe.py")
    sf_src = rd("sigmafloor_probe.py")
    dbt1 = rd("dbt_run1.log")
    dbt2 = rd("dbt_run2.log")
    sf1 = rd("sf_run1.log")
    sf2 = rd("sf_run2.log")
    sf3 = rd("sf_run3.log")
    nxt = open(NEXT, encoding="utf-8").read()

    # ------------------------------------------------- S1 findings
    section("S1  FINDINGS F1-F6 (machine checks)")

    # G10 -- F1 entry-law commit overstatement
    msg168 = git_msg(R168_COMMIT)
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
    atoms_ok = True
    n_prime = n_atom = n_excl2 = 0
    d10 = []
    for (hs, hb), u in sorted(pairs.items()):
        q = int(round(math.exp(u)))
        atoms_ok = atoms_ok and abs(math.log(q) - u) < 1e-3 \
            and ENTRY_ATOMS[(hs, hb)] == q
        pp = prime_powers(hb)
        new = [(qq, p) for qq, p in pp if qq > hs]
        big_prime = max((qq for qq, p in new if qq == p), default=0)
        big_atom = max(qq for qq, _p in new)
        big_x2 = max(qq for qq, p in new if p != 2)
        n_prime += (q == big_prime)
        n_atom += (q == big_atom)
        n_excl2 += (q == big_x2)
        d10.append("(%d,%d) entry %d [maxNewPrime %d maxNewAtom %d "
                   "maxNewNon2 %d]" % (hs, hb, q, big_prime,
                                       big_atom, big_x2))
    phrase = ("cone entry ALWAYS at the LARGEST NEW PRIME ATOM of "
              "the dyadic gap, 4/4 batteries")
    note183 = nxt[nxt.find("(CDLXXXIII)"):nxt.find("(CDLXXXII)")]
    ok10 = (atoms_ok and len(pairs) == 4
            and n_prime == 3 and n_atom == 2 and n_excl2 == 4
            and phrase in msg168
            and "PRIM(POTENZ)-Atom" in note183
            and not (9 in
                     [p for _q, p in prime_powers(10) if _q == 9]))
    check("G10-f1-commit-entrylaw", ok10,
          "record entry atoms 7/9/13/17; readings: largest-new-PRIME "
          "3/4 (fails (5,10): 9 = 3^2 not prime), largest-new-ATOM "
          "2/4, note-reading (prime-power excl trailing 2-powers) "
          "4/4; the commit phrase '%s' matches NO 4/4 reading while "
          "the note CDLXXXIII states the careful PRIM(POTENZ) form: "
          "BH6-F1 CONFIRMED [%s]" % (phrase[:40] + "...",
                                     "; ".join(d10)))

    # G11 -- F2 bit-identical wording
    msg167 = git_msg(R167_COMMIT)
    rd_dbt = raw_diff_lines(dbt1, dbt2)
    rd_sf = raw_diff_lines(sf2, sf3)
    nn_dbt = raw_diff_lines(normalize_timing(dbt1),
                            normalize_timing(dbt2))
    nn_sf = raw_diff_lines(normalize_timing(sf2),
                           normalize_timing(sf3))
    ok11 = (rd_dbt == DIFF_PAIRS["dbt"]
            and rd_sf == DIFF_PAIRS["sf"]
            and nn_dbt == 0 and nn_sf == 0
            and "bit-identical re-run" in msg168
            and "bit-identical deterministic re-run" in msg167
            and "Wanduhr-Token" in note183)
    check("G11-f2-commit-bitidentical", ok11,
          "raw diffs dbt %d lines (5 pairs) / sf %d lines (4 pairs), "
          "OWN timing-normalizer -> 0/0; commits r168+r167 say "
          "'bit-identical' while the notes state the honest "
          "timing-token form: BH6-F2 CONFIRMED (wording only)"
          % (rd_dbt, rd_sf))

    # G12 -- F3 vacuous exact-layer legs
    flat_dbt = re.sub(r"\s+", "", dbt_src)
    flat_sf = re.sub(r"\s+", "", sf_src)
    leg_d = "okD=all(2**k>=2**kforkinrange(2,12))"
    leg_h = "okH=sp.simplify(sp.sin(aa*z)*Rz-(sp.sin(aa*z))*(Rz))==0"
    ok12 = (leg_d in flat_dbt and leg_h in flat_sf
            and "block hits are cofinal" in dbt_src
            and "product ring" in sf_src)
    check("G12-f3-vacuous-legs", ok12,
          "r168 G10 leg okD == all(2^k >= 2^k) tautology presented "
          "as 'block hits are cofinal'; r169 G11 leg okH == "
          "simplify(E - E) == 0 presented as the product-ring step: "
          "both cannot fail and check nothing beyond X == X; "
          "theorems stay true, no verdict flips: BH6-F3 CONFIRMED")

    # G13 -- F4 G63 reachability semantics
    chain_perk = {
        "SIGMAFLOOR": ["DTSTEP_ALLK"], "EPSLAW": ["DTSTEP_ALLK"],
        "BA3": ["DTSTEP_ALLK"], "CENSUS_K": ["DTSTEP_ALLK"],
        "DTSTEP_ALLK": ["HCOF"], "SUBSTRATE28": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"], "CARRIER_LEM": ["WEILPOS"],
        "WEILPOS": ["RH"], "NFCLOS": ["RH_VIA_N"],
        "L1": ["RH_VIA_N"], "WPD": ["RH_VIA_N"],
        "RH_VIA_N": ["RH"], "RH": []}
    or_hit = "RH" in or_reach(chain_perk, "SIGMAFLOOR")
    fired_solo = and_fire(chain_perk, {"SIGMAFLOOR"}, {"RH"})
    fired_full = and_fire(chain_perk,
                          {"SIGMAFLOOR", "EPSLAW", "BA3", "CENSUS_K",
                           "SUBSTRATE28", "CARRIER_LEM"}, {"RH"})
    chain_uni = {
        "RH": ["CENSUS_ALLK"], "CENSUS_ALLK": ["DTSTEP_ALLK"],
        "DTSTEP_ALLK": ["HCOF"], "HCOF": ["WEILPOS"],
        "WEILPOS": ["RH"]}
    chain_pin = {
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"],
        "TAUPOS": ["SIGMAFLOOR"]}
    ok13 = (or_hit
            and "RH" not in fired_solo
            and "RH" in fired_full
            and has_cycle_own(chain_uni)
            and has_cycle_own(chain_pin)
            and "throughEITHERtypedarrow" in flat_dbt
            and "AND-semantics" not in dbt_src
            and "AND-semantics" in sf_src)
    check("G13-f4-graph-semantics", ok13,
          "r168 chain_perk OR-reach(SIGMAFLOOR) hits RH (replicated) "
          "but OWN AND-fire from {SIGMAFLOOR} alone does NOT fire RH "
          "(full grant set does): the 'EITHER typed arrow' gate leg "
          "is OR-semantics; r169 adds '(AND-semantics: all parents "
          "needed)' silently -- BH5-F1-class precision: BH6-F4 "
          "CONFIRMED; both LOOP cycles (universalized census, "
          "pinning-supply) replicated with OWN DFS "
          "(semantics-independent, sound)")

    # G14 -- F5 wi_smoke2 gap
    wi_src = rd("window_instrument_probe.py")
    have = [os.path.exists(os.path.join(HERE, "wi_smoke%d.log" % i))
            for i in (1, 2, 3, 4)]
    note181 = nxt[nxt.find("(CDLXXXI)"):nxt.find("(CDLXXX)")]
    ok14 = (have == [True, False, True, True]
            and "wi_smoke2" not in wi_src
            and "wi_smoke2" not in nxt
            and "smoke" not in note181.lower())
    check("G14-f5-smoke2-gap", ok14,
          "kept wi smokes 1/3/4 only; no surface (docstring, note "
          "CDLXXXI, next.txt) accounts for the missing smoke2 "
          "designation; re-freezes themselves fully disclosed "
          "(Amendments 1 + 1a): BH6-F5 CONFIRMED (BH5-F4 class)")

    # G15 -- F6 always-pass screen gate
    ok15 = ('check("G47-deep-pairs-screen", True,' in dbt_src
            and re.search(r'scr_ok = \(base_ok', dbt_src) is not None
            and 'd47.append("screen-ok %s" % scr_ok)' in dbt_src
            and 'kind="screen"' in dbt_src
            and 'elif kind == "exact"' in dbt_src
            and 'kind == "screen"' not in dbt_src.split(
                "def check", 1)[1].split("def info", 1)[0])
    check("G15-f6-alwayspass-screen", ok15,
          "r168 G47 verdict argument is literal True; scr_ok is "
          "computed and printed but never gated; kind='screen' is "
          "not a special branch of check(): the gate cannot fail by "
          "construction (disclosed screen typing; enum carries only "
          "entry-NEW bits): BH6-F6 CONFIRMED")

    # ------------------------------------- S2 independent recompute
    section("S2  INDEPENDENT RECOMPUTATION (exact + numeric)")

    import sympy as sp
    hh, etp, et2, GP, Ga, Gb, A0s, kap = sp.symbols(
        "hh etp et2 GP Ga Gb A0s kap", positive=True)
    off_s = 8 * sp.sqrt(hh) * (A0s * (1 + etp)) ** 2 * GP
    okA = sp.simplify(off_s / (8 * A0s ** 2 * Ga)
                      - sp.sqrt(hh) * (1 + etp) ** 2 * GP / Ga) == 0
    fac = sp.simplify((sp.sqrt(2 * hh) * (1 + et2) ** 2 * GP / Gb)
                      / (sp.sqrt(hh) * (1 + etp) ** 2 * GP / Ga))
    okB = sp.simplify(fac - sp.sqrt(2) * (Ga / Gb)
                      * ((1 + et2) / (1 + etp)) ** 2) == 0
    Gl = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    okC = sp.limit(sp.sqrt(2) * Gl(2 * sp.pi * hh)
                   / Gl(4 * sp.pi * hh), hh, sp.oo) == 2 * sp.sqrt(2)
    okD_ = sp.limit(sp.sqrt(hh) * Gl(kap * hh ** sp.Rational(3, 2))
                    / Gl(2 * sp.pi * hh), hh, sp.oo) == 3 * sp.pi / kap
    okE = True
    for a_r in (sp.Integer(0), sp.Rational(1, 2), sp.Integer(1),
                sp.Rational(3, 2)):
        s_e = sp.Rational(3, 2) + a_r
        lim = sp.limit(sp.sqrt(hh) * Gl(kap * hh ** s_e)
                       / Gl(2 * sp.pi * hh) * hh ** a_r, hh, sp.oo)
        okE = okE and sp.simplify(
            lim - 2 * sp.pi * s_e / kap) == 0
    a_s, c_s = sp.symbols("a_s c_s", positive=True)
    okF = sp.simplify((3 * sp.pi / c_s) * (1 + 2 * a_s / 3)
                      - 2 * sp.pi * (sp.Rational(3, 2) + a_s)
                      / c_s) == 0
    dd = sp.diff(hh ** sp.Rational(3, 2) / (sp.log(hh) + 1), hh)
    okG_ = sp.simplify(dd * (sp.log(hh) + 1) ** 2 / sp.sqrt(hh)
                       - (3 * sp.log(hh) + 1) / 2) == 0
    # SF1 anatomy on OWN rational instance (different numbers)
    s1_, s2_ = sp.Rational(2, 7), sp.Rational(3, 11)
    F1_, F2_ = sp.Rational(5, 4), sp.Rational(4, 9)
    A0q, g1_, g2_ = sp.Rational(7, 3), sp.Integer(2), sp.Integer(7)
    Gzq = sp.Rational(3, 100)
    sup = 8 * (s1_ * F1_ ** 2 / g1_ ** 2 + s2_ * F2_ ** 2 / g2_ ** 2)
    GmC = 2 * (s1_ / g1_ ** 2 + s2_ / g2_ ** 2)
    de_ = (s1_ * F1_ ** 2 / g1_ ** 2 + s2_ * F2_ ** 2 / g2_ ** 2) \
        / (A0q ** 2 * (s1_ / g1_ ** 2 + s2_ / g2_ ** 2))
    okH_ = sp.simplify(sup / (8 * A0q ** 2 * Gzq)
                       - de_ * GmC / (2 * Gzq)) == 0
    tpos = sp.symbols("tpos", nonnegative=True)
    qpos = sp.symbols("qpos", positive=True)
    okI = ((qpos + tpos) ** 2 - qpos ** 2
           ).expand().equals(tpos ** 2 + 2 * tpos * qpos) \
        and (tpos ** 2 + 2 * tpos * qpos).is_nonnegative is True
    okJ = bool(sp.Rational(1, 2) <= sp.Rational(1, 2)
               and -sp.Rational(99, 100) <= sp.Rational(1, 2)
               and 1 + sp.Rational(1, 2) == sp.Rational(3, 2)
               and 1 - sp.Rational(99, 100) == sp.Rational(1, 100))
    check("G20-own-sympy-exact", okA and okB and okC and okD_
          and okE and okF and okG_ and okH_ and okI and okJ,
          "OWN re-derivations: DT2 chase + dyadic factor + limit "
          "2^{3/2}; census limit 3 pi/kappa; SF4 limits == "
          "2 pi(3/2+a)/kappa at a = 0..3/2 == (3 pi/c)(1+2a/3); "
          "monotone bracket (3L+1)/2; SF1 anatomy + delta x DC on "
          "an OWN rational instance; SF2 rate chase + cap-is-upper "
          "instances: ALL EXACT")

    N = 10 ** 6
    sieve = np.ones(2 * N + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(2 * N)) + 1):
        if sieve[p]:
            sieve[p * p:: p] = False
    pr = np.flatnonzero(sieve)
    cnt = np.cumsum(np.concatenate([[0], sieve.astype(np.int64)]))
    hs_ = np.arange(2, N + 1)
    okB6 = bool(np.all(cnt[2 * hs_ + 1] - cnt[hs_ + 1] > 0))
    check("G21-own-bertrand", okB6 and len(pr) > 148000,
          "OWN sieve to 2e6 + cumulative counts: a prime in (h, 2h] "
          "for EVERY 2 <= h <= 1e6 (interface never empty; %d "
          "primes)" % len(pr))

    if not smoke:
        hstar = solve_hstar_own(0.15)
        kstar = math.log2(hstar)
        kappas = []
        lts, lhs = [], []
        for Hx in (1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9):
            target = float(own_G(2 * math.pi * Hx)) * 0.15 \
                / math.sqrt(Hx)
            tlo, thi = 2 * math.pi * Hx * 1.01, 1e40
            for _ in range(300):
                tm = math.sqrt(tlo * thi)
                if float(own_G(tm)) > target:
                    tlo = tm
                else:
                    thi = tm
            Tr = math.sqrt(tlo * thi)
            kappas.append(Tr / Hx ** 1.5)
            lts.append(math.log10(Tr))
            lhs.append(math.log10(Hx))
        slope = float(np.polyfit(lhs, lts, 1)[0])
        ok22 = (abs(hstar / HSTAR - 1) <= HSTAR_TOL
                and KSTAR_WIN[0] <= kstar <= KSTAR_WIN[1]
                and all(kappas[i] > kappas[i + 1]
                        for i in range(len(kappas) - 1))
                and kappas[-1] > KAPPA_INF
                and CENSUS_SLOPE_WIN[0] <= slope
                <= CENSUS_SLOPE_WIN[1])
        check("G22-own-horizon-census", ok22,
              "OWN G + OWN solves: h* = %.4e (r168 string %.4e rel "
              "%.0e), k* = %.2f; T_req/H^{3/2} = %s falling toward "
              "%.2f; exponent fit %.4f in %s"
              % (hstar, HSTAR, HSTAR_TOL, kstar,
                 ["%.1f" % k for k in kappas], KAPPA_INF, slope,
                 str(CENSUS_SLOPE_WIN)))
    else:
        check("G22-own-horizon-smoke", True, "smoke: skipped")

    if not smoke:
        rows = {}
        t_b = time.time()
        for h in (4, 5, 6, 7, 8):
            rows[h] = b2_rung(h, gam)
        with mp.workdps(200):
            lo = sum(mp.mpf(rows[h]["tau_lo"]) for h in rows)
            hi = sum(mp.mpf(rows[h]["tau_up"]) for h in rows)
            bud = sum(mp.mpf(rows[h]["zsum"]) - mp.mpf(rows[h]["off"])
                      for h in rows)
        ok23 = (all(rows[h]["pd_ok"] for h in rows)
                and abs(float(lo) / B2_ENC[0] - 1) <= STR_TOL
                and abs(float(hi) / B2_ENC[1] - 1) <= STR_TOL
                and float(lo) > 0
                and abs(float(bud) / B2_BUDGET - 1) <= STR_TOL
                and all(abs(rows[h]["tlaw"] / B2_TLAW[h] - 1)
                        <= STR_TOL for h in rows)
                and all(abs(rows[h]["sigma"] / B2_SIGMA[h] - 1)
                        <= STR_TOL for h in rows)
                and all(rows[h]["recipe_dev"] <= RECIPE_BAR
                        for h in rows))
        check("G23-own-b2-substrate", ok23,
              "OWN B2 recompute (%.0f s): enclosure [%.4e, %.4e] vs "
              "r166 [2.1410e-11, 2.1431e-11]; budget %.4e vs "
              "1.8949e-11; tlaw %s; sigma %s; recipe devs %s <= "
              "1e-40: the substrate + GW pair verify under "
              "independent reimplementation"
              % (time.time() - t_b, float(lo), float(hi), float(bud),
                 ["%d:%.4f" % (h, rows[h]["tlaw"]) for h in rows],
                 ["%d:%.4f" % (h, rows[h]["sigma"]) for h in rows],
                 ["%.0e" % rows[h]["recipe_dev"] for h in rows]))
    else:
        check("G23-own-b2-smoke", True, "smoke: skipped (heavy)")

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
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
               ("NFCLOS", "TAILVIS"): 1, ("TAILVIS", "R4HYP"): INF,
               ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2R"): 1, ("SUSCAP2R", "R4HYP"): INF,
               ("NFCLOS", "DELTA1FLOOR"): 1,
               ("DELTA1FLOOR", "R4HYP"): INF})
    fb = maxflow_own(base, "UNC", "RH")
    fe = maxflow_own(ext, "UNC", "RH")
    fo = maxflow_own(one, "UNC", "RH")
    fc = maxflow_own(cf, "UNC", "RH")
    noom = {k: [] for k in set(u for u, _v in ext)
            | set(v for _u, v in ext)}
    for (u, v), c in ext.items():
        if c >= INF:
            noom[u].append(v)
    ok24 = ((fb, fe, fo, fc) == MINCUT
            and "RH" not in or_reach(noom, "UNC"))
    check("G24-own-mincut", ok24,
          "OWN Edmonds-Karp on the r168/r169 graph encodings: flows "
          "base %d, refined %d, one-grant %d, counterfactual %d == "
          "%s; RH unreachable without omega edges" %
          (fb, fe, fo, fc, str(MINCUT)))

    # ------------------------------------------- S3 cross-round
    section("S3  CROSS-ROUND BOOKKEEPING")

    def module_consts(src: str, names: set) -> dict:
        out = {}
        for node in ast.parse(src).body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                    and isinstance(node.targets[0], ast.Name) \
                    and node.targets[0].id in names:
                try:
                    out[node.targets[0].id] = ast.literal_eval(
                        node.value)
                except Exception:                  # noqa: BLE001
                    pass
        return out

    names = {"TLAW_TAB", "FG_TAB", "CTRL_TAU_TAB", "SIGMA_TAB",
             "HSTAR_STR", "SIGMA0", "T_PT", "KFAC", "Z_OVERHANG",
             "G34_HARD_MAX", "F64_SLOP", "NZSUM"}
    c168 = module_consts(dbt_src, names)
    c169 = module_consts(sf_src, names)
    hsw_line = "HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675"
    ok30 = all(c168.get(n) == c169.get(n) for n in names) \
        and c168["T_PT"] == T_PT \
        and hsw_line in dbt_src and hsw_line in sf_src
    r165_src = rd("novelty_synthesis_probe.py")
    ok30 = ok30 and all(s in r165_src for s in
                        ("0.2664", "0.3738", "0.4674", "0.4827",
                         "0.5122", "0.5778"))
    check("G30-constants-tables", ok30,
          "TLAW/FG/CTRL/SIGMA/HSTAR/SIGMA0/T_PT/HSW/overhang tables "
          "literal-identical across the r168/r169 sources; the r165 "
          "definitive tlaw row present verbatim: the window-constant "
          "layer is cross-round consistent")

    def parse_ladder(log: str, tag: str) -> dict:
        m = re.search(r"\[INFO\] %s ladder: ([^\n]+)" % tag, log)
        out = {}
        for tok in m.group(1).split():
            k, v = tok.split(":")
            if v != "-":
                out[int(k)] = float(v)
        return out

    sig_rec = parse_ladder(dbt1, "sigma")
    tl_rec = parse_ladder(dbt1, "tlaw")
    lad169 = module_consts(sf_src, {"SIGMA12_LADDER", "TLAW_LADDER"})
    ok31 = all(abs(sig_rec[h] - v) <= 5e-5
               for h, v in lad169["SIGMA12_LADDER"].items()) \
        and all(abs(tl_rec[h] - v) <= 5e-5
                for h, v in lad169["TLAW_LADDER"].items())
    check("G31-ladder-transport", ok31,
          "r169's frozen SIGMA12_LADDER (23 rungs) + TLAW_LADDER "
          "(25 rungs) == the r168 dbt_run1 record info ladders at "
          "4-decimal identity: the record transport is exact")

    heads = re.findall(r"^# \d{4}-\d{2}-\d{2} \(([CDLXVIM]+)\)",
                       nxt, re.M)
    nums = [roman_to_int(h) for h in heads]
    scope = set(range(468, 485))
    in_scope = [n for n in nums if n in scope]
    uniq = len(in_scope) == len(set(in_scope))
    contig = scope <= set(in_scope)
    desc = all(in_scope[i] > in_scope[i + 1]
               for i in range(len(in_scope) - 1)) and nums[0] >= 484
    attrib = {468: "selberg_effective_probe.py",
              469: "bughunt5_probe.py",
              470: "novelty_synthesis_probe.py",
              475: "tau_blockaverage_probe.py",
              481: "window_instrument_probe.py",
              483: "depthblock_transfer_probe.py",
              484: "sigmafloor_probe.py"}
    blocks = {}
    idxs = [m.start() for m in re.finditer(
        r"^# \d{4}-\d{2}-\d{2} \(([CDLXVIM]+)\)", nxt, re.M)]
    idxs.append(len(nxt))
    for i, h in enumerate(heads):
        blocks[roman_to_int(h)] = nxt[idxs[i]:idxs[i + 1]]
    at_ok = all(fn in blocks.get(n, "") for n, fn in attrib.items())
    indep = [476, 477, 478, 479, 480, 482]
    ind_files = ["readout_fourier_factor_probe.py",
                 "rp_nsr_flat_probe.py", "quillen_jet_a4_probe.py",
                 "ftransfer_context15_probe.py",
                 "quillen_ramified_level_probe.py",
                 "quillen_level_dictionary_census_probe.py"]
    ind_ok = all(n in blocks for n in indep) and all(
        os.path.exists(os.path.join(HERE, f)) for f in ind_files)
    check("G32-numerals", uniq and contig and desc and at_ok
          and ind_ok,
          "audit-scope numerals CDLXVIII..CDLXXXIV (468..484) "
          "present, unique, file-order strictly descending, head >= "
          "484 (head %d); audited rounds' "
          "notes name their probe files; independent-session "
          "numerals 476-480+482 present with probe files on disk "
          "(uncommitted per the commit disclosures)" % max(nums))

    ok33 = True
    d33 = []
    for rn, (pyf, logs) in sorted(ROUNDS.items()):
        doc = ast.get_docstring(ast.parse(rd(pyf)), clean=False)
        fin = hashlib.sha256(doc.encode("utf-8")).hexdigest()[:16]
        for lg, want in logs.items():
            m = re.search(r"SPEC_SHA ([a-f0-9]{16})", rd(lg))
            got = m.group(1)
            exp = fin if want == "FINAL" else want
            if got != exp:
                ok33 = False
                d33.append("%s %s %s != %s" % (rn, lg, got, exp))
        d33.append("%s final %s" % (rn, fin))
    check("G33-spec-lineage", ok33,
          "SPEC_SHA recomputed from all 7 docstrings; EVERY kept log "
          "matches the disclosed lineage (all hash moves accounted: "
          "r163 smoke respec, r166 Amendments 1+2, r167 Amendments "
          "1+1a, r169 Amendment 1; r164/r165/r168 single-hash): %s"
          % "; ".join(d33))

    note184 = nxt[nxt.find("(CDLXXXIV)"):nxt.find("(CDLXXXIII)")]
    ok34 = (all(s in note183 for s in
                ("36/36 GATES PASS", "a4cd07144e0c5222", "1971.3",
                 "1966.5", "smoke1 = 32/34", "smoke3 = 34/34"))
            and all(s in note184 for s in
                    ("35/35 GATES PASS", "a16a4db1055488d2",
                     "1971.4", "1966.8", "34/35",
                     "eed821a2469a0dc1", "smoke1 = 33/33"))
            and "GATES: 36/36 PASS" in dbt1
            and "GATES: 35/35 PASS" in sf2
            and "GATES: 34/35 PASS" in sf1
            and "GATES: 32/34 PASS" in rd("dbt_smoke1.log")
            and "GATES: 34/34 PASS" in rd("dbt_smoke3.log")
            and "GATES: 33/33 PASS" in rd("sf_smoke1.log"))
    check("G34-notes-vs-logs", ok34,
          "CDLXXXIII/CDLXXXIV claimed gate counts, SHAs, runtimes "
          "and smoke/run fail accounting ALL verified against the "
          "kept logs (incl. the r168 pre-record smoke fixes and the "
          "r169 run-1 fail row)")

    if not smoke:
        on_rec = parse_ladder(sf2, r"onset\(0\.5\)")
        fl_rec = parse_ladder(sf2, r"ratefloor\(0\.25\)")
        allr = sorted(fl_rec)
        clean = [h for h in allr
                 if h in on_rec and on_rec[h] <= gtop / 2]

        def fit_a(hs2):
            lx = [math.log10(h) for h in hs2]
            ly = [math.log10(fl_rec[h]) for h in hs2]
            return -float(np.polyfit(lx, ly, 1)[0])

        a_all = fit_a(allr)
        a_cl = fit_a(clean)
        ok35 = (len(allr) == N_ONSET and len(clean) == N_CLEAN
                and 18 not in clean and on_rec.get(18, 0) > gtop / 2
                and abs(a_all - RATE_ALL) <= RATE_ABS
                and abs(a_cl - RATE_CLEAN) <= RATE_ABS
                and "h^{-2.063}" in sf1 and "h^{-1.328}" in sf2
                and "12 clean rungs" in sf2
                and "CACHE-TOP-LIMITED" in sf2)
        check("G35-amendment-fit", ok35,
              "r169 Amendment-1 window recomputed OWN: %d onset "
              "rungs (4..18), clean set == %d rungs under onset <= "
              "gtop/2 = %.1f (h=18 onset %.0f excluded); OWN fits "
              "a_all %.3f (~2.063) / a_clean %.3f (~1.328) from the "
              "record ladders; run1 fail row + run2 restricted fit "
              "strings verified"
              % (len(allr), len(clean), gtop / 2,
                 on_rec.get(18, -1), a_all, a_cl))
    else:
        check("G35-amendment-smoke", True, "smoke: skipped")

    ok36 = ("enc 9/9" in dbt1 and "enc 11/11" in dbt1
            and "ENTRY-NEW-CONFIRMED(4/4 pairs)" in dbt1
            and "STEP(B2 -> B3) 9/9" in msg168
            and "STEP(B3 -> B4-partial) 11/11" in msg168
            and "36/36 gates" in msg168
            and "ZERO AMENDMENTS" in msg168
            and "46/46 gates" in msg167
            and "mid-run" in msg167)
    check("G36-commit-vs-record", ok36,
          "commit STEP counts (9/9, 11/11), gate counts (36/36, "
          "46/46), ENTRY-NEW-CONFIRMED(4/4) and the r167 mid-run "
          "re-freeze disclosure all match the record logs (the "
          "commit layer is numerically faithful; the two wording "
          "findings F1/F2 are the only deviations found)")

    r163_src = rd("selberg_effective_probe.py")
    lits = ("0.10076", "0.24460", "7.20844", "1.68845", "1.50956",
            "0.1038", "0.2573", "9.3675", "8.3675", "0.1095",
            "0.2042", "3.0305", "2.5167", "30 610 046 000")
    ok37 = all(s in r163_src for s in lits) \
        and "3000175332800" in dbt_src and "3000175332800" in sf_src \
        and "2969/aspm/02110281" in r165_src \
        and "Yoshida" in dbt_src and "Yoshida" in sf_src
    check("G37-literature-pins", ok37,
          "r163 pricing constants present verbatim and EXACT vs the "
          "cited papers (HSW22 Cor 1.2/1.4, Bellotti-Wong Cor 1.5, "
          "Platt-DB, PT21 -- external verification 2026-08-19 pinned "
          "in the spec); the r165 Yoshida-1992 doi + the r168/r169 "
          "citations consistent: the priority blockade is VALID")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "BUGHUNT6-FINDINGS(6: 0 MAJOR / 2 MINOR / 4 NOTE)",
        "ENDGAME-CHAIN-SURVIVES-AS-TYPED(A1-A10; no arrow retyped)",
        "SUBSTRATE-REVERIFIED-INDEPENDENT(B2; G23)",
        "RECIPE-PROVENANCE-TRACED(off-line strip e^A; DT2 typing "
        "justified)",
        "PROVENANCE-ALL-MOVES-DISCLOSED(G33)",
        "LITERATURE-PINS-EXACT(G37)",
        "YOSHIDA-BLOCKADE-VALID(G37)"]
    for v in verdicts:
        print("  " + v)
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
    print("COMPOSITE: " + " + ".join(v.split("(")[0]
                                     for v in verdicts))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
