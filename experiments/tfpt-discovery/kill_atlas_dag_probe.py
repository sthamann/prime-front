#!/usr/bin/env python3
r"""kill_atlas_dag_probe -- PRIME.AUDIT.KILLATLAS.01: the KILL ATLAS and
the typed RH IMPLICATION DAG, as one machine-checked data structure
(2026-08-14, note CCCLXXVI).

EXPLORATION ONLY.  This probe proves nothing about RH.  It supplies no
positivity, no interval, no certificate; it closes no gate, narrows no
gate and moves NO marker.  It is a SYNTHESIS AUDIT: the accumulated
route kills of the campaign (notes CCLXV..CCCLXXV) are encoded as an
explicit atlas, the implication chain from the certified finite head to
RH is encoded as an explicit typed DAG, and the structural claims about
both are re-checked as executable assertions.  NO RH CLAIM.

=====================================================================
WHY THIS FILE EXISTS
=====================================================================
The corpus states the localization in six different coordinate systems
-- tau_h > 0, n_h - q_h > 0, sigma_h <= 1, v_-^T X v_- >= -lam_min(G0),
P_err,h <= Q_h - P_main,h - need_h, and v913's best-conditioned (L) --
and each restatement was recorded in its own note.  Nothing in the tree
holds the whole map in ONE place, in a form a machine can contradict.
Consequence, twice observed by the program's own auditors (CCCXXXVII
C-1, CCCXXXVI): a reader can identify two different objects that carry
the same number, or read a reformulation as an advance.  This file is
the single contradictable object: DAG + atlas as data, with the
typing rules of the audit applied as gates.

THE THREE TYPING RULES APPLIED HERE (frozen, from the audit brief)
  R1  A REFORMULATION IS NOT AN ADVANCE.  Operational test = the
      TAU-SCREEN (registered in PRIME.PORT.BFLOOR.01, bands frozen
      a priori in port_bfloor_uniformity_probe.py): OLS slope s of
      log(candidate margin) against log(tau).  PASS iff |s| <= 0.30,
      RELOCATION iff s >= 0.70.  A candidate that relocates -- or that
      is declared a reparametrization at source -- is DISGUISE.
  R2  THE FROZEN GATE RULE.  Progress on the open edge needs an
      INDEPENDENT SIGN SOURCE that separates true arithmetic from the
      three registered control worlds EPSTEIN (a_Q = r_{x^2+5y^2}/2,
      class number 2, no Euler product), SCRAMBLE (arithmetic-scramble
      = Lambda-label swap; position-scramble = lag relabelling) and
      SMOOTH (the prime-free PNT world).  A certificate that also
      passes on the controls is WALL-BLIND and does not count.
  R3  PROVEN vs MEASURED.  PROVEN = unconditional (or named,
      non-circular premises) in a verification/vN_*.py module or a
      Lean file.  Finitely many certified rungs = CERTIFIED-FINITE.
      Positivity read on finitely many rungs = MEASURED.  Neither is
      PROVEN for all h.

=====================================================================
THE DAG, AS TYPED HERE (10 edges, 11 nodes; see DAG_EDGES)
=====================================================================
  E1  SRC        -> BPOS       CERTIFIED-FINITE  v905 (min c_B .5523)
  E2  SRC        -> SPOS       CERTIFIED-FINITE  v897/v907 + sigma-chain
                                                 (CONDITIONAL: tau(r1))
  E3  BPOS,SPOS  -> MPOS_FIN   PROVEN            v901 Schur equivalence
  E5  SRC        -> HCONV      PROVEN            v912 FORMCONV-PROVEN
  E4  MPOS_FIN   -> HCOF       OPEN              --
  E6  HCOF,HCONV -> QW_DENSE   PROVEN            CofinalWeil.lean/v848
  E7  QW_DENSE   -> QW_CLASS   CITED-CLASSICAL   density + Dini leg
  E8  SRC        -> W1ID       CITED-CLASSICAL   v630/v643 identification
  E9  QW_CLASS,W1ID -> WEILPOS CITED-CLASSICAL   capped == Weil
  E10 WEILPOS    -> RH         CITED-CLASSICAL   Weil's criterion

THE FIRST OPEN EDGE IS E4, and E4 ONLY -- but E4 is NOT the only edge
that fails to be PROVEN.  The honest non-PROVEN list in topological
order is [E1, E2, E8, E4, E7, E9, E10].  E1/E2 are finite by
construction (nothing is missing in them; their SCOPE is finite), and
E7..E10 are classical citations.  The corpus headline "the chain is
reduced to exactly one unproven inequality" (CCCLXXIV) is therefore
right about INEQUALITIES and about what the program must supply, and
the module docstrings say the rest correctly (v912: "Edge 6 of the
implication DAG is NARROWED, not closed"; v848: STEP 3/STEP 4
classical cited) -- the headline is where the four citations vanish.
Gate D4 pins exactly this list so the count cannot drift.

=====================================================================
THE CIRCULARITY LEDGER (gate D5; each entry must be flagged as data)
=====================================================================
  X1  E2 CONSUMES ITS OWN CONCLUSION THROUGH A SELECTION GATE.  The
      sigma-chain step matrices are tau(r1)-normalized, so each
      per-cell certificate proves tau(r1)*S(r2) > 0, not S(r2) > 0;
      tau(r1) > 0 is an uncertified float64 selection gate of the
      PREVIOUS rung (chain_adversary_probe, CCCXXXIII: refusal branch
      fires on 0/85 built cells; on 83/85 the r2 positivity is already
      an admission premise).  Typed CONDITIONAL, not circular-fatal.
  X2  EVERY MAX-TAU-PER-BIN SUB-LADDER IS SIGN-MINED.  It selects
      rungs by tau, a wall OUTPUT, so it can never instantiate E4's
      predefined idx (CCCXXXVII Q-3).  The compliant rule exists and
      is frozen pre-build: MAX-GAP-PER-BIN (census geometry only).
  X3  KAPPA = 1 IS DEFINITIONAL.  The coupling Gram and the coisometry
      Gram are entrywise equal (2.2e-15) and kappa = 1 survives purely
      random densities on 3/3 worlds -- two code paths, zero arithmetic
      content (CCCXXXIII).  Any "coupling scalar" advance built on it
      is a relabelling.
  X4  THE KREIN CONTRACTOR MUST BE SOURCE-SIDE.  KreinDefect.lean types
      the circularity warning in its own module doc: a target-computed
      C (eigendata, or the converse's pseudoinverse) is a reformulation
      of the positivity, and feeding it back is circular.
  X5  W2 CONSUMES ZERO DATA AS A CITATION.  v909's W2 face reads
      2e7 certified ordinates; that is legitimate for a FINITE
      certificate and can never prove RH (ledger says so verbatim).
      It is zero data inside E2's scope, never inside E4.
  CLEAN: v901's n, q are source-only (no tau_{h+1}, no forward sign --
      the gap sign is output, never input); v913 predicts h from its
      own prime-power sieve rather than consuming it; v912 bans every
      zero/primality oracle by AST; v848 never evaluates (H).

=====================================================================
WHAT THE GATES PIN, AND WHAT THEY DO NOT
=====================================================================
PINNED: the DAG shape (acyclicity, reachability, the topological
position of the single OPEN edge, the non-PROVEN list); artifact
existence on disk for every PROVEN/CERTIFIED-FINITE edge; ledger
membership of every cited vN module; atlas well-formedness (one edge
per killed route, declared verdict enum vocabulary, declared
tau-screen and control-screen vocabulary); the presence of each atlas
verdict enum in the named artifact on disk; and thirteen load-bearing
numbers re-derived or re-grepped here (N1..N13).

A2.2 gates the TOKEN, not the number printed beside it, so the killing
numbers needed their own ward: N12 exists because this audit first
wrote the zero-window bootstrap ratio as 0.098 (the real reads are
8.9e-02 at the lowest anchor and 8.0e-05 at T0; 0.098 occurs NOWHERE in
that probe) and attributed the -4.083267 flip ward to the wrong probe.
N13 exists because the research log reuses its numeral space across two
series -- 45 low numerals belong to an earlier one -- so numeral-only
citation is globally ambiguous, and even inside the RH campaign CCCLVII
names two different rounds.

Gate A2.2 -- "every atlas verdict enum literally occurs in its own
cited artifact" -- is the sharpest gate in this file, and it bit on the
first run: it rejected twelve rows whose verdict token this audit had
PARAPHRASED rather than copied (ABEL-TOO-WEAK for the real
TAILABEL-MEASURED, KSTAR-UNBOUNDED for GRAMRADAU-MEASURED,
FLOOR-VS-INVERSE-DEAD for PGSCHUR-MEASURED, and nine more).  The tokens
below are therefore grep-earned, not authored.  Where a campaign
verdict was recorded only in the note and never frozen as a probe enum
(EXTERIOR-HALFGAP-REFUSED), the cited artifact is experiments/next.txt,
the primary historical record.

NOT PINNED (a false input here would NOT fail this probe): every
MEASURED number of the campaign; the correctness of any cited
classical theorem; whether the atlas is COMPLETE (it is complete over
the routes named in notes CCLXV..CCCLXXV that touch the chain, which
is an editorial claim, not a gate); and the truth value of E4.

TWO CORRECTIONS THIS FILE CARRIES (both against the brief it audits)
  A1  NOGO-COMPOSITE-VERIFIED IS NOT AN ADVANCE.  It is the verdict of
      signed_only_nogo_probe.py (87/87); the PROMOTED module v913 emits
      NOGO-CORE-VERIFIED (24/24).  Both are typed no_go_typing [O] and
      the ledger row is titled, verbatim, "A NO-GO / TYPING ROW AND
      EXPLICITLY NOT PROGRESS", adding that it "must NOT be counted as
      evidence for or against the Riemann Hypothesis".  Listing it
      among the advances inverts its own type.
  A2  WIRING-DEGENERATE AND THETA-CONVENTIONAL ARE OFF-CHAIN.  Both
      are seam/compiler-lane results (SEAM.STATE.WIRING.SELECTOR.01,
      promoted in v911): the wiring freedom theorem and the theta_S
      collar frame.  They attack no edge of this DAG.  Gate D6 pins
      them as the ONLY off-chain rows.

SCOPE: this file plus the CCCLXXVI note in experiments/next.txt are the
only writes.  No verification/, no papers, no ledger, no website, no
manifests, no Lean, no .md, no commit.  Stdlib only.  NO RH CLAIM.
"""

import math
import os
import re
import sys
from collections import namedtuple
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent           # experiments/tfpt-discovery
ROOT = HERE.parent.parent                        # repo root

FAILS = []
CHECKS = []

LEDGER = "verification/status_ledger.csv"

# ---------------------------------------------------------------- vocab
# frozen enums; anything outside these sets is a spec error, not a
# result (gate D3 / D6)
EDGE_TYPES = ("PROVEN", "CERTIFIED-FINITE", "MEASURED", "OPEN",
              "CITED-CLASSICAL", "CLOSED-BY-NOGO")
TAU_SCREEN = ("ADVANCE", "DISGUISE", "NOT-APPLICABLE")
CTRL_SCREEN = ("SEPARATES", "WALL-BLIND", "UNTESTED")
CONTROL_WORLDS = ("EPSTEIN", "SCRAMBLE-ARITH", "SCRAMBLE-POS", "SMOOTH")
OFF_CHAIN = "OFF-CHAIN-SEAM"

# the frozen tau-screen bands (PRIME.PORT.BFLOOR.01; declared a priori
# in port_bfloor_uniformity_probe.py as SLOPE_PASS / SLOPE_RELOC)
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70

# ------------------------------------------------------------ the DAG
Edge = namedtuple("Edge", "eid src dst etype statement artifacts "
                          "theorem consumes")

ROOT_NODE = "SRC"
SINK_NODE = "RH"

NODES = {
    "SRC": "the deployed construction: window ladder h, tent kernel "
           "K_D, dyadic mesh D_j = 2^-j, pinned prime-power table "
           "(source-only data; no zeros, no target vector)",
    "BPOS": "B_h > 0 with a certified floor on the reachable steps "
            "(the 7x7 co-block half of the tangent-Schur end-form)",
    "SPOS": "s_h = n_h - q_h > 0 on the built rungs (the two-scalar "
            "half; equivalently sigma_h = q_h/n_h = 1 - s_h/n_h < 1)",
    "MPOS_FIN": "M_h > 0 on the built/reachable ladder -- the "
                "CERTIFIED FINITE HEAD",
    "HCOF": "(H_cof): the ladder form is PSD at every rung of ONE "
            "sign-independently PREDEFINED family cofinal IN THE "
            "MESH-REFINEMENT ORDER D_j = 2^-j",
    "HCONV": "hconv: per-element convergence ladderForm A idx j v -> "
             "Q_W v over the declared dense family and the full rung "
             "sequence",
    "QW_DENSE": "Q_W >= 0 on the declared dense (dyadic cellwise-"
                "affine) family",
    "QW_CLASS": "Q_W >= 0 on the admissible even compactly supported "
                "BV class",
    "W1ID": "the deployed window layers ARE Suzuki's localized Weil "
            "measure/functional (atoms at log p^k, weights "
            "Lambda(n)/sqrt(n); archimedean layer lag-exact)",
    "WEILPOS": "Weil positivity of the localized Weil functional",
    "RH": "the Riemann Hypothesis",
}

DAG_EDGES = (
    Edge(
        eid="E1", src=("SRC",), dst="BPOS", etype="CERTIFIED-FINITE",
        statement="B >= (1/2) P_G + c_dom I and P_G >= c_G I imply "
                  "B >= c_B I; min c_B = 0.5523 over RIGOROUS OUTWARD "
                  "ENCLOSURES of the ideal source objects on 39/39 "
                  "reachable steps (exact-rational LDL tier on the "
                  "computed float64 matrices: 0.5914; measured "
                  "lam_min(B) floor: 0.679, family O(1) in "
                  "[0.679, 84.0]).  h-uniformity beyond h ~ 900 OPEN.",
        artifacts=("verification/v905_bfloor_ideal_certificate.py",
                   "verification/v901_tangent_schur_bfloor.py"),
        theorem="PRIME.PORT.BFLOOR.PG.IVAL.01 / PRIME.PORT.BFLOOR.01",
        consumes=(),
    ),
    Edge(
        eid="E2", src=("SRC",), dst="SPOS", etype="CERTIFIED-FINITE",
        statement="sigma_h <= 0.726909 on 151/151 built wall-legal "
                  "cells (n > 0 exact, certified ordered co-block "
                  "floors, Gauss-Radau/interval-SOS moment bound, all "
                  "exact-rational), below the definiteness bar 1 on "
                  "59/59 deep steps to h = 6344 (worst certified "
                  "bound 0.787603); interval-rigorous sigma_h > 0 on "
                  "all 42 reachable rungs h = 142..878.  CONDITIONAL: "
                  "per cell this proves tau(r1)*S(r2) > 0, with "
                  "tau(r1) > 0 an uncertified float64 SELECTION gate.",
        artifacts=("verification/v897_certified_interval_ladder.py",
                   "verification/v907_halfgap_registered_target.py",
                   "experiments/tfpt-discovery/chain_adversary_probe.py"),
        theorem="PRIME.PORT.HALFGAP.01 + the CCLXXIX/CCXCIII "
                "sigma-chain census (sandbox, exact-rational)",
        consumes=("X1: wall positivity via the tau(r1) selection gate",
                  "X5: 2e7 cited certified ordinates in the W2 face"),
    ),
    Edge(
        eid="E3", src=("BPOS", "SPOS"), dst="MPOS_FIN", etype="PROVEN",
        statement="THE SCHUR EQUIVALENCE.  For M = [[n, b^T], [b, B]] "
                  "symmetric with B > 0: M > 0 <=> n - q > 0, where "
                  "q = b^T B^-1 b; det M = (n - q) det B.  Both "
                  "scalars source-only -- no tau_{h+1}, no forward "
                  "sign: the gap sign is output, never input "
                  "(det ward 2.8e-14; PD equivalence boolean-exact on "
                  "39/39 steps).",
        artifacts=("verification/v901_tangent_schur_bfloor.py",),
        theorem="PRIME.PORT.TANGENT.SCHUR.01",
        consumes=(),
    ),
    Edge(
        eid="E5", src=("SRC",), dst="HCONV", etype="PROVEN",
        statement="THE FORM-CONVERGENCE THEOREM, unconditional with "
                  "explicit rate and explicit constants: for f real, "
                  "supported in the window and AFFINE ON EVERY GRID "
                  "CELL, |Q_D(f) - Q_W(f)| <= D^2[(8 sinh(B/2) + "
                  "mfrak(B)) A2 + Theta0 A0 + (A0 + A2)(log(1/D) + "
                  "log B + 4) + 2 A0 e^{-B/2}(1/B + 2) + A1(1 + D)] + "
                  "(1 + D)(D^3/12) kappa3, rate O(D^2 log(1/D)).  "
                  "Load-bearing exact step: k_d - K(dD) = "
                  "-(D^2/12) G(dD) for EVERY lag.  Classical input "
                  "ledger closed: elementary + finite prime-power "
                  "table + Rosser-Schoenfeld for the support-uniform "
                  "constant ONLY.  NOT Lean-formalised (DELTA-A).",
        artifacts=("verification/v912_form_convergence_theorem.py",
                   "experiments/lean4-carrier-rigidity/TfptCarrier/"
                   "CofinalEnvelope.lean"),
        theorem="PRIME.FORM.CONVERGENCE.THEOREM.01 (FORMCONV-PROVEN)",
        consumes=(),
    ),
    Edge(
        eid="E4", src=("MPOS_FIN",), dst="HCOF", etype="OPEN",
        statement="THE ONE MISSING INEQUALITY.  On ONE "
                  "sign-independently PREDECLARED family (a_j, D_j) "
                  "cofinal in the MESH-REFINEMENT order, prove ladder "
                  "positivity.  Six equivalent coordinates, all the "
                  "same edge: (i) tau_h > 0 for all h; (ii) "
                  "n_h - q_h > 0; (iii) sigma_h < 1; (iv) "
                  "v_-^T X v_- >= -lam_min(G0) (CCCXXV); (v) "
                  "P_err,h <= Q_h - P_main,h - need_h (CCCLXI); (vi) "
                  "v913's best-conditioned (L) int_0^1 "
                  "[-(1/2)<w, v> - q_c] dtheta > int_0^1 "
                  "[q_0 - n_0] dtheta with v = A_2^T B^-1 b_0.  "
                  "RIDER (external premise, not formalisable without "
                  "a provenance system): the concrete interpretation "
                  "of Predefined(A, idx) -- a source boundary frozen "
                  "before evaluation, excluding A and its sign "
                  "outputs.",
        artifacts=(),
        theorem="",
        consumes=(),
    ),
    Edge(
        eid="E6", src=("HCOF", "HCONV"), dst="QW_DENSE", etype="PROVEN",
        statement="THE ARITHMETIC-FREE LIMIT PASSAGE, kernel-checked: "
                  "a pointwise-convergent sequence of nonnegative "
                  "reals has a nonnegative limit, so under (H_cof) "
                  "Q_W >= 0 on the whole dense family -- NO Mosco "
                  "compactness, NO uniform delta, NO diagonal "
                  "argument.  Cofinality suffices because convergence "
                  "makes the catch set {j : Q_j < 0} a TAIL of the "
                  "mesh order and a cofinal set meets every tail; the "
                  "hierarchy uniform (SUBSET-NEQ) pointwise "
                  "(SUBSET-NEQ) cofinal is proved strictly in the "
                  "kernel.",
        artifacts=("experiments/lean4-carrier-rigidity/TfptCarrier/"
                   "CofinalWeil.lean",
                   "experiments/lean4-carrier-rigidity/TfptCarrier/"
                   "CofinalPredefinition.lean",
                   "verification/v848_extraction_chain.py"),
        theorem="FORM.PRIME.COFINAL.WEIL.01 -- "
                "limit_nonneg_of_cofinal_seq / weil_nonneg_of_cofinal "
                "/ cofinal_weil / cofinal_weil_for_fixed_idx",
        consumes=(),
    ),
    Edge(
        eid="E7", src=("QW_DENSE",), dst="QW_CLASS",
        etype="CITED-CLASSICAL",
        statement="DENSITY + CONTINUITY.  The dyadic cellwise-affine "
                  "family is dense in the admissible even compactly "
                  "supported BV class in the CORRECTED topology: "
                  "uniform convergence PLUS equi-Lipschitz (Dini) at "
                  "the origin.  The formerly cited sup-norm "
                  "C^0-continuity of Q_W at fixed support is FALSE "
                  "(v912 control C5: e_n(w) = (1/n) min(1, "
                  "w/e^{-n^2})(1 - w/2)_+ has ||e_n||_inf = 1/n -> 0 "
                  "while |A[e_n]| = 2.57, 4.28, ..., 12.09 grows "
                  "linearly).  v912 types this edge NARROWED, NOT "
                  "CLOSED; the density leg stays CITED "
                  "[FEM density + IK04 Thm 5.12 / Bombieri 2000].",
        artifacts=("verification/v912_form_convergence_theorem.py",),
        theorem="cited: FEM density; IK04 Thm 5.12; Bombieri 2000",
        consumes=(),
    ),
    Edge(
        eid="E8", src=("SRC",), dst="W1ID", etype="CITED-CLASSICAL",
        statement="THE W1 IDENTIFICATION.  The atom layer of the "
                  "window form IS the prime measure of Suzuki's screw "
                  "function (positions log p^k, weights "
                  "Lambda(n)/sqrt(n)) and the archimedean layer "
                  "matches at every lag (kernel identity ~1e-52, full "
                  "form equality 1.28e-10).  Theorem-closed at the "
                  "MEASURE level in the suite; v912 types the "
                  "identification with the CLASSICAL Weil functional "
                  "as CITED, not pinned (S1).",
        artifacts=("verification/v630_suzuki_contact.py",
                   "verification/v643_w1_theorem.py"),
        theorem="the W1 measure dictionary (v630/v631/v640..v643)",
        consumes=(),
    ),
    Edge(
        eid="E9", src=("QW_CLASS", "W1ID"), dst="WEILPOS",
        etype="CITED-CLASSICAL",
        statement="THE CAPPED-TO-FULL PASSAGE.  With the faithful cap "
                  "C >= b_K + D the capped functional W_C agrees with "
                  "W_inf on the admissible class (v912 (III)), so "
                  "nonnegativity of Q_W on the class is Weil "
                  "positivity of the localized Weil functional.",
        artifacts=("verification/v912_form_convergence_theorem.py",
                   "verification/v848_extraction_chain.py"),
        theorem="cited: Weil's explicit formula (S2); the faithful "
                "cap identity is proven in v912",
        consumes=(),
    ),
    Edge(
        eid="E10", src=("WEILPOS",), dst="RH", etype="CITED-CLASSICAL",
        statement="WEIL'S CRITERION: positivity of the Weil "
                  "functional on the admissible class is equivalent "
                  "to RH.",
        artifacts=(),
        theorem="cited: Weil 1952; Bombieri 2000; Suzuki JLMS 107 "
                "(2023) / JFA 281 (2021) 109116",
        consumes=(),
    ),
)

FIRST_OPEN_EDGE = "E4"
# the honest non-PROVEN list, in the topological order this file
# computes (gate D4.3); E8 fires early because W1ID hangs off SRC
NON_PROVEN_EXPECTED = ("E1", "E2", "E8", "E4", "E7", "E9", "E10")

# ---------------------------------------------------------- the atlas
Row = namedtuple("Row", "route contract edge delivered killer verdict "
                        "tau ctrl worlds artifact")

ATLAS = (
    # ---- routes at the OPEN edge E4 (the sign/quantifier front) -----
    Row("Schoenberg conditional positivity",
        "PRIME.CORE.SCHOENBERG.01", "E4",
        "exact algebra of the centered form plus a half-angle "
        "rank-one reduction",
        "the FULL centered form is non-representable by ANY positive "
        "Euler measure -- a theorem, not a measurement",
        "SCHOENBERG-PARTIAL", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/schoenberg_core_probe.py"),
    Row("grid-phase theta-mean of the Schur scalar",
        "PRIME.COFINAL.SHIFT.AVERAGE.01", "E4",
        "three certified theta-mean enclosures at h = 184/388/839, "
        "4-7 orders above the deployed point margin",
        "the piecewise-affinity premise is FALSE: on a breakpoint-free "
        "dyadic interval a 90-digit rebuild puts the ATOM second "
        "difference inside +-4.00000002094905884e-73 while the "
        "archimedean and full-source second differences EXCLUDE zero "
        "strictly at every depth (h 184: [2.28883658345733749e-06, "
        "2.28883658345733833e-06]); corrected mean enclosures "
        "[-inf, +inf]",
        "HH-CLAIMS-WITHDRAWN", "NOT-APPLICABLE", "SEPARATES",
        ("SCRAMBLE-ARITH", "EPSTEIN"),
        "experiments/tfpt-discovery/shift_average_hh_audit_probe.py"),
    Row("deep theta = 1/2 point certificates",
        "PRIME.COFINAL.SHIFT.AVERAGE.DEEP.01", "E4",
        "five rigorous point certificates, two new and deep "
        "(h = 1393: s in [2.27451283174326270e-09, "
        "2.27451283174326353e-09]; h = 2854: "
        "[2.12003444567896238e-10, 2.12003444567896289e-10])",
        "point witnesses bound NO theta-mean: the direct mean route "
        "has no certified finite starting cell at all",
        "SHIFTAVGDEEP-INSTRUMENT-EDGE", "NOT-APPLICABLE", "SEPARATES",
        ("SCRAMBLE-ARITH", "EPSTEIN"),
        "experiments/tfpt-discovery/shift_average_deep_probe.py"),
    Row("all-depth theta-mean, priced classically",
        "PRIME.COFINAL.SHIFT.AVERAGE.ALLDEPTH.01", "E4",
        "sympy-exact mean identities plus three killed wrong "
        "inequality directions (Jensen witness 3/2 < 8/5)",
        "deficit A/G = 2.470e+11 at h = 184 and 1.990e+14 at h = 388 "
        "with deliberately optimistic constants C_VK = c_VK = 1, "
        "x0 = 2; and the B-spline comb energy E+ = 5/12 enters the "
        "mean with a MINUS sign -- the prime energy has the wrong sign",
        "CLASSICAL-GAP", "NOT-APPLICABLE", "WALL-BLIND",
        ("SCRAMBLE-ARITH", "EPSTEIN", "SMOOTH"),
        "experiments/tfpt-discovery/shift_average_all_depth_probe.py"),
    Row("fold covariance / k-arm self-pairing principle",
        "PRIME.BIGPICTURE.FOLDCOV.01", "E4",
        "exact k-arm rotation-fold family, k = 2 reproducing the "
        "deployed wall to 7.5e-17 and saturating 41/41 in band",
        "k = 3 and k = 4 saturate 0/41 with large-negative "
        "compressions GROWING with depth (k = 3: -7.5e+04 at h = 184 "
        "-> -1.7e+08 at h = 997; k = 4: -1.3e+05 -> -1.6e+07) -- no "
        "constant repairs k >= 3",
        "PATTERN-ONLY", "NOT-APPLICABLE", "WALL-BLIND",
        ("SMOOTH",),
        "experiments/tfpt-discovery/fold_covariance_probe.py"),
    Row("multiplicative sign source (Moebius/Dirichlet/Rankin-Selberg)",
        "PRIME.CORE.MULTSIGN.01", "E4",
        "P_err fully normalized; three exact no-go certificates "
        "(polarization, cross-prime, orientation loss)",
        "H_e has exact rank 2 and inertia (1,1,*) with the "
        "rational-interval-certified witness e_2 = log2(log2-2) < 0, "
        "and Y_p = v_p v_p^T is an exact PSD dual with "
        "<Y_p, K> = -1; e e^T is invariant under e -> -e so the "
        "autocorrelation route loses the orientation.  Multiplicativity "
        "IS world-discriminating, but its positive defect energy is "
        "ZERO on truth and does not orient the nonzero P_err",
        "LOCAL-OBSTRUCTION", "NOT-APPLICABLE", "SEPARATES",
        ("EPSTEIN", "SCRAMBLE-ARITH", "SMOOTH"),
        "experiments/tfpt-discovery/multiplicative_sign_source_probe.py"),
    Row("Selberg symmetry rewrite of the localized object",
        "PRIME.CORE.FLUCTUATION.ENERGY.02", "E4",
        "exact representation (4.6e-13); Selberg's identity warded "
        "EXACTLY in integer arithmetic (2999 tables, 0 deviations); "
        "the rewrite kernel measured 100% Selberg-direction "
        "(log(m/n) dependence absent to 2e-16)",
        "delivery envelope coarser than the alignment margin by "
        "1.60e+04 at the friendliest rung, MEDIAN 9.09e+05 (~5.96 "
        "dex; oracle-exact-main median 2e+04); and A_main - B_main == "
        "B_main identically, hence A_err - B_err = P_err bit-exactly "
        "(4.5e-14) -- no rewrite-then-estimate route can beat the "
        "original.  The sign is decided only at resolution "
        "n ~ 2^17 = 131072 (18 of 19 dyadic blocks each move the feed "
        "by more than the final margin)",
        "SELBERG-INSUFFICIENT", "NOT-APPLICABLE", "SEPARATES",
        ("SCRAMBLE-ARITH", "SCRAMBLE-POS", "SMOOTH"),
        "experiments/tfpt-discovery/selberg_symmetry_rewrite_probe.py"),
    Row("core fluctuation normal form (five names -> one scalar)",
        "PRIME.CORE.FLUCTUATION.ENERGY.01", "E4",
        "the sharpest available localization: one scalar "
        "anti-cancellation inequality v_-^T X v_- >= -lam_min(G0), "
        "alignment margin 1.5e-05..2.7e-03 on 67/67",
        "kappa = 1.000000 at 2.2e-15 -- three of the five names are "
        "literally the same number, and kappa = 1 survives purely "
        "random densities on 3/3 worlds (residual <= 1e-15), so it is "
        "a definitional identity of two code paths; the completed "
        "square is degenerate (rho_h == 0 identically) and the "
        "decoupled reading lam_min(X) >= need fails 0/67 by ~5%",
        "REFORMULATION-ONLY", "DISGUISE", "SEPARATES",
        ("SMOOTH",),
        "experiments/tfpt-discovery/"
        "core_fluctuation_normalform_probe.py"),
    Row("matrix-stage conditioning (the demand rebasing)",
        "PRIME.MATRIX.STAGE.CONDITIONING.01", "E4",
        "REAL rebasing: the growth is localized in the Galerkin/Schur "
        "matrix stage; F4 source-profile/Gram-kernel coordinates cut "
        "7.910 orders of demand at the deepest registered rung and "
        "the exponent 8.969 -> 6.103, leaving the SIGNED residual at "
        "2 orders (overshoot 60.888/295.97/205.35) and exponent 2.119",
        "the source factorization b_c = -(1/4) A_2 w holds in BOTH "
        "control worlds at residual 2.22e-16 -- it is an ALGEBRAIC "
        "identity, hence COMB-BLIND: the conditioning gain can NEVER "
        "be the missing discriminating lemma.  And the sign-flipped "
        "counter-world (b_c -> -b_c, admissible in I(R)) is certified "
        "NEGATIVE everywhere, worst certified upper bound -4.083267 "
        "(that flip ward is WARD_FLIP_WORST in "
        "signed_only_nogo_probe.py, not in this route's own probe)",
        "SEAT-CONDITIONING", "NOT-APPLICABLE", "WALL-BLIND",
        ("SCRAMBLE-ARITH", "EPSTEIN"),
        "experiments/tfpt-discovery/matrix_stage_conditioning_probe.py"),
    Row("F4 residual attack with the unconditional toolbox",
        "PRIME.F4.RESIDUAL.ATTACK.01", "E4",
        "the signed part IS EXACTLY Weil's PRIME(F) in CCCLXVI's "
        "normalization (deviation 0.00e+00), the exponent falls "
        "2.119 -> 0.847, and the unsigned part gets a bound with "
        "explicit constants (q_c <= (1/16) lam_max(K_J) 4 L T)",
        "BAR-IS-NEGATIVE: the remaining statement is literally "
        "sum_rho Fhat(gamma_rho) < POLE(F) + ARCH(F) - int[q_0 - n_0 "
        "+ q_c], whose bar is NEGATIVE (-5.771e-01/-5.416e+00/"
        "-3.280e+00) -- the OPPOSITE of a Weil positivity statement.  "
        "The unsigned part is class-IMPOSSIBLE (assumed floor deficit "
        "10.42/28.29/13.44 > 1) and the signed cone floor has deficit "
        "2.11/4.03/1.69 > 1 with exponent 0.863 > 0, so no bound "
        "consuming only {w >= 0, size, local density, support} closes "
        "it or kills its growth; v is Nyquist-dominated (0.61-0.73 of "
        "the l2 mass above omega = pi/2) so NO-BILINEAR-LENGTH",
        "F4-SIGNED-EXPLICIT", "NOT-APPLICABLE", "SEPARATES",
        ("SMOOTH", "SCRAMBLE-ARITH", "EPSTEIN"),
        "experiments/tfpt-discovery/f4_residual_attack_probe.py"),
    Row("extremal window budget (attack from the window side)",
        "PRIME.WINDOW.EXTREMAL.BUDGET.01", "E4",
        "exact symbolic budget functional of the test window; the "
        "supply sign is repaired by an optimal window",
        "1.75/1.77 orders of magnitude remain after the sign repair, "
        "and every CLOSING window is COMB-BLIND "
        "(WINDOW-INADMISSIBLE); band-limiting is forbidden by the "
        "faithful cap",
        "WINDOW-OPTIMAL-INSUFFICIENT", "NOT-APPLICABLE", "WALL-BLIND",
        ("SCRAMBLE-ARITH", "EPSTEIN", "SMOOTH"),
        "experiments/tfpt-discovery/extremal_window_budget_probe.py"),
    Row("hardness calibration + external adversarial falsification",
        "PRIME.CORE.HARDNESS.FALSIFY.01", "E4",
        "the RH-hardness label priced from outside against twelve "
        "named sources (part A) and a falsification sweep for a "
        "negative rung (part B)",
        "part A leaves the hardness label an ASSESSMENT, not a "
        "theorem (HARDNESS-UNRESOLVED); part B finds NO negative rung "
        "to h = 12632 with the corrected instrument -- deepest "
        "certified read 2.79579794131272506e-15, 0 negatives, 0 "
        "straddles -- and the n0-normalized decay FLATTENS with depth "
        "(-3.21092511 globally vs -2.67942161 on the deepest step "
        "5746 -> 12632, one re-derived step outright positive "
        "+0.50302892 against the frozen collapse bar -8.0)",
        "NO-WITNESS", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/"
        "hardness_calibration_falsification_probe.py"),
    Row("zero-window bootstrap (more zeros buy the depth quantifier)",
        "PRIME.ZEROWINDOW.BOOTSTRAP.01", "E4",
        "the exact supply/demand bookkeeping of the transfer law",
        "the ratio is BELOW 1 AT EVERY ANCHOR, which is the probe's "
        "own frozen BOOTSTRAP-DEAD criterion: lowest-anchor D_env = "
        "647 at delta = 0.5 gives ratio 8.9e-02 with D_fire EMPTY, "
        "and at T0 the ratio is 8.0e-05 [4.9e-06..1.3e-03]; the "
        "depth quantifier does not fall to more verified zeros (and "
        "v910's transfer law prices the same wall from the other "
        "side: T_req ~ h^2.8)",
        "BOOTSTRAP-DEAD", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/zero_window_bootstrap_probe.py"),
    Row("transitionwise Riccati barrier (induction on the ladder)",
        "PRIME.HALFGAP.RICCATI.01", "E4",
        "a transition-local induction shape with an isotropic floor",
        "fails broadly 21/37, every fail a down-flow: the mu1 "
        "increment allowance sits 3-6 orders below the pivot flow, "
        "the isotropic floor overprices by +1.5..+4.7 dex, and the "
        "barrier is WALL-BLIND -- adversarial worlds that break the "
        "wall at rung level still CERTIFY transitions (cosh 15/36, "
        "rescale 5/17).  Increments are steeper than levels; "
        "transition-local induction is dead on every granularity",
        "WALL-BLIND", "NOT-APPLICABLE", "WALL-BLIND",
        ("SCRAMBLE-ARITH",),
        "experiments/tfpt-discovery/"
        "halfgap_riccati_transition_probe.py"),
    Row("legality frontier / horizon (a measured termination signal)",
        "PRIME.LEGALITY.FRONTIER.01", "E4",
        "a deep legality census reading tau on the 1e-10 scale with "
        "oscillating sign, and the first measured termination signal "
        "LEGHOR-TERMINATES-MEASURED (last legal h = 8204)",
        "ARTIFACT-RETRACTED: float64 polynomial evaluation past its "
        "resolution floor.  At the chain's own witness Q reads "
        "-8.75e-11 on the chain columns and +2.22e-10 on the same "
        "polynomial in Chebyshev coefficients (opposite signs, 3.5x); "
        "the sign-resolution quotient runs 6.2e-06 (h = 878) -> 3.54 "
        "(h = 9447), sign-reliable only to h = 3948.  All nine cells "
        "ever read negative or marginal are direct-method positive "
        "with exact inertia n_neg = 0",
        "ARTIFACT-RETRACTED", "NOT-APPLICABLE", "SEPARATES",
        ("SMOOTH",),
        "experiments/tfpt-discovery/verdicta_protocol_probe.py"),
    Row("H_cof dodging audit (does Li-style dodging threaten H_cof?)",
        "PRIME.HCOF.DODGING.AUDIT.01", "E4",
        "HARDENING, not a kill: the wall's catch set is a TAIL, so "
        "off-line zeros cannot dodge a cofinal ladder; all three "
        "slots of weil_nonneg_of_cofinal are strictly stronger than "
        "the proof needs",
        "the immunity is bought by CONVERGENCE and costs a mesh-order "
        "qualifier: at FIXED mesh D0 the deployed read is exactly "
        "cap-independent, so a window-only-cofinal ladder is "
        "eventually CONSTANT and yields only Q_W >= -|W_C[e_D0]| -- "
        "measured false floors -2.114e-03 at D0 = 1/32 and "
        "-2.128e-04 at D0 = 1/128",
        "HCOF-IMMUNE", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/hcof_dodging_audit_probe.py"),
    Row("local Euler-factor / local-phase no-go",
        "PRIME.LOCAL.FACTOR.NOGO.01", "E4",
        "the exact local normal form K_p ~ diag((p-1)/p, -1) and its "
        "phase reading",
        "the local identity FAILS as a source of sign: the level "
        "decay sits in a SOURCE CANCELLATION, the peak-minus-"
        "background reading is non-discriminating, and the gate "
        "family is comb-blind",
        "NOGO-TYPED", "NOT-APPLICABLE", "WALL-BLIND",
        ("SMOOTH", "SCRAMBLE-ARITH"),
        "experiments/tfpt-discovery/local_factor_nogo_probe.py"),
    # ---- wall-avoiding routes that bypass E4 and aim at E10 --------
    Row("Xi real-rooted determinant limit, round 1",
        "PRIME.XI.REALROOTED.LIMIT.01", "E10",
        "a wall-avoiding determinant-limit programme with its own "
        "frozen decision bar",
        "vacuous under its own frozen bar (origin cluster, comb and "
        "pole-unit defects diagnosed in the same run)",
        "XILIMIT-VACUOUS", "NOT-APPLICABLE", "WALL-BLIND",
        ("SCRAMBLE-ARITH",),
        "experiments/tfpt-discovery/xi_realrooted_limit_probe.py"),
    Row("Xi real-rooted determinant limit, round 2 (repaired)",
        "PRIME.XI.REALROOTED.LIMIT.01 R2", "E10",
        "round 1's divergence repaired completely: adaptive Nyquist "
        "comb X(t) = (t/2pi)^beta, C^2 atom activation, affinely "
        "gauged resolvent gate, explicit +1 pole-counting unit",
        "still under the frozen decision bar: SEP_CNT 2.58 and "
        "SEP_MID 1.68 against the required max >= 5, with three row "
        "plateaus (slopes -0.018/-0.020/-0.002)",
        "XILIMIT2-STILL-VACUOUS", "NOT-APPLICABLE", "WALL-BLIND",
        ("SCRAMBLE-ARITH",),
        "experiments/tfpt-discovery/xi_realrooted_limit_r2_probe.py"),
    Row("Xi resolvent normalization (the Herglotz repair)",
        "PRIME.XI.RESOLVENT.NORMALIZATION.01", "E10",
        "the HIGH premise bug repaired: residue ward exact before "
        "every read (Res = -1 symbolically and in a rational 70-digit "
        "enclosure), F/dim explicitly discarded at all built "
        "dimensions 20286..71348, affine/Hadamard regularization "
        "proved residue-free",
        "the target residual does NOT converge under the frozen rule "
        "(SAFE slope -0.0184, drop ratio 0.8749; MID -0.0366, 0.7392, "
        "against a required 1.25 drop and slope <= -0.05) and the "
        "scramble separations SEP_SAFE 2.966 / SEP_MID 1.931 sit "
        "against the frozen bar 5",
        "XIRES-VACUOUS", "NOT-APPLICABLE", "WALL-BLIND",
        ("SCRAMBLE-ARITH",),
        "experiments/tfpt-discovery/"
        "xi_resolvent_normalization_probe.py"),
    Row("Xi mollified semilocal resolvent contract",
        "PRIME.XI.MOLLIFIED.SEMILOCAL.01", "E10",
        "the strongest non-circular target exposed as a frozen "
        "contract (M1 safe convergence + M2 uniform local "
        "boundedness of the unnormalized regularized full trace)",
        "the contract is at least RH-hard and possibly stronger for "
        "this family, and its frozen gate ADDITIONALLY demands an "
        "arithmetic-specific estimate violating "
        "Epstein/Scramble/Smooth -- no 'almost proof'",
        "CONTRACT-EXPOSED", "NOT-APPLICABLE", "UNTESTED",
        ("EPSTEIN", "SCRAMBLE-ARITH", "SMOOTH"),
        "experiments/tfpt-discovery/"
        "xi_mollified_semilocal_contract_probe.py"),
    Row("Beurling-Nyman / Baez-Duarte Gram transport",
        "PRIME.BN.GRAM.TRANSPORT.01", "E10",
        "the transport target stated exactly in Q",
        "no transport of compiler objects: lam_min(G_N) <= "
        "(log 2pi - gamma)/N so the Gram has NO N-uniform floor (cap "
        "0.420220 against the needed 0.5523), the Loewner direction "
        "is wrong and the margin inverted; and the explicit family "
        "Gtil = A A^T + (4/5)^2 I meets EVERY hypothesis of the "
        "certificate class at every N while dtil^2 >= 1/2 forever -- "
        "the class is non-implying",
        "BN-NO-TRANSPORT", "DISGUISE", "UNTESTED", (),
        "experiments/tfpt-discovery/beurling_nyman_gram_probe.py"),
    Row("Li-Keiper positivity, arithmetic pass",
        "PRIME.LI.KEIPER.ARITH.01", "E10",
        "an exact zero-free high-precision decomposition of lambda_n "
        "via the Bombieri-Lagarias substitution, with a better "
        "bookkeeping margin than the wall",
        "bookkeeping margin ONLY: the transform is refuted (T-), the "
        "inner-depth disease persists, comb separation is partial, "
        "and the classical delivery is short.  Later corrected: the "
        "round's own VK envelope is WITHDRAWN (HIGH, computation "
        "error localized, two independent refutations)",
        "LI-FAVORABLE", "DISGUISE", "SEPARATES",
        ("SCRAMBLE-ARITH",),
        "experiments/tfpt-discovery/li_keiper_positivity_probe.py"),
    Row("Li lemma attack (pricing the Li-Keiper advantage)",
        "PRIME.LI.LEMMA.ATTACK.01", "E10",
        "the price of the Li advantage, computed",
        "the index quantifier is STRICTLY HARDER, not cofinally "
        "relaxable: Bohr recurrence with an explicit off-line "
        "counterexample (R = 1.05, theta = 2 pi (sqrt(2) - 1), "
        "Re rho = 0.513125026604), and the remaining 'order bound "
        "with 350x air' lies by Bombieri-Lagarias Cor. 1(c) EXACTLY "
        "on the RH-equivalence boundary where the air is zero; the "
        "low-height detector has finite reach n ~ T_0^2 = 9.0e+24 and "
        "the absolute route is insufficient EVEN UNDER RH",
        "LI-QUANTIFIER-PRICED", "NOT-APPLICABLE", "SEPARATES",
        ("SCRAMBLE-ARITH",),
        "experiments/tfpt-discovery/li_lemma_attack_probe.py"),
    Row("de Branges / Krein string / Hermite-Biehler chain",
        "PRIME.DEBRANGES.CHAIN.01", "E10",
        "the Hermite-Biehler chain built and evaluated",
        "the chain is a SYMBOLIC IDENTITY with zero arithmetic "
        "content -- comb-blind by construction, so it cannot "
        "distinguish the true comb from any control world",
        "DEBRANGES-COMB-BLIND", "DISGUISE", "WALL-BLIND",
        ("SCRAMBLE-ARITH", "EPSTEIN", "SMOOTH"),
        "experiments/tfpt-discovery/debranges_chain_probe.py"),
    # ---- routes at the finite scalar edge E2 ------------------------
    Row("registered half-gap target n - q >= (1/2) mu1(h)",
        "PRIME.PORT.HALFGAP.01", "E2",
        "a registered FALSIFICATION instrument: 67/67 surface pass "
        "(margins +0.0025/+0.5273/+1.6845) plus a blind holdout 28/28 "
        "whose minimum sits ~90x above the registered surface minimum",
        "REPARAM-DECLARED in every print: mu1(h) = 4 sin^2(pi/(2h+1)) "
        "exact with tie 0.0 and the pivot collapse n - q = m warded "
        "4.3e-16 -- the inequality IS the wall margin reparametrized, "
        "and all four candidate origins of the 1/2 are typed OPEN",
        "HALFGAP-REGISTERED", "DISGUISE", "SEPARATES",
        ("SMOOTH", "EPSTEIN", "SCRAMBLE-ARITH"),
        "verification/v907_halfgap_registered_target.py"),
    Row("sigma cap / Schur-quotient closure",
        "PRIME.SIGMA.COUPLING.PIVOT.01", "E2",
        "an attractive KS-dual closure under the cap sigma <= 0.665",
        "sigma = q/n = 1 - s/n warded at 3.8e-15 -- ANY cap on sigma "
        "is the open half restated, not an input; and the constant's "
        "provenance is the probe's own margin convention "
        "(0.604556 * 1.10 = 0.665012), so the match with the "
        "measure-side 0.665 is a PROVEN coincidence",
        "CAP-VACUITY", "DISGUISE", "SEPARATES",
        ("SMOOTH",),
        "experiments/tfpt-discovery/sigma_coupling_pivot_probe.py"),
    Row("pivot rewrite / edge-Christoffel positive-weight identity",
        "PRIME.CASE.EDGE.CHRISTOFFEL.01", "E2",
        "an exact positive-weight identity 1/d_12 = 1 + sum_m W_{h,m} "
        "Q(x_m)^2 - beta with W > 0 exactly (min 9.7e-14)",
        "tau-screen RELOCATION: the decisive ratio's distance from 1 "
        "TRACKS the margin itself at slope +1.008 (deflated "
        "Christoffel margin +1.000) -- the open uniform q < 1 target "
        "is the wall's own PD premise quantified",
        "EDGECHRISTOFFEL-MEASURED", "DISGUISE", "UNTESTED", (),
        "verification/v902_wall_relocation_map.py"),
    Row("classical certified eigenvalue bounds on B",
        "PRIME.PORT.BFLOOR.01", "E1",
        "Gershgorin (raw and scaled), Brauer-Cassini and Weyl applied "
        "directly to the co-block",
        "all four are NEGATIVE on all 39 steps, best bound-maximum "
        "-88.2 against the true measured floor +0.679 (cond(B) "
        "quartiles 171/221/278): a certifiable floor needs a damping "
        "congruence class, not a better classical inequality",
        "CERTFLOOR-DEAD", "NOT-APPLICABLE", "UNTESTED", (),
        "verification/v901_tangent_schur_bfloor.py"),
    Row("per-step B-floor certification ladder (the damping "
        "congruence route)",
        "PRIME.PORT.BFLOOR.PG.01", "E1",
        "THE ONE tau-screen ADVANCE OF THE CAMPAIGN: an exact "
        "certified per-step floor that does NOT track the wall "
        "margin -- lam_min(B) family O(1) in [0.679, 83.99] with "
        "tau-screen slope -0.247 (corr -0.346, R^2 0.119), inside "
        "the a-priori PASS band |s| <= 0.30",
        "it is nevertheless NOT the open edge: an h-flat B-floor "
        "supplies the co-block half only, and by the E3 Schur "
        "equivalence the whole difficulty then sits in the scalar "
        "s_h = n_h - q_h.  h-uniformity of the floor beyond the "
        "built range stays OPEN, and the composed interval tier is "
        "0.5523, not the measured 0.679",
        "BFLOOR-CERT-LADDER", "ADVANCE", "UNTESTED", (),
        "experiments/tfpt-discovery/"
        "bfloor_perstep_certification_probe.py"),
    Row("Gram / Lukacs moment completion at matched degree",
        "PRIME.PORT.GRAM.COMPLETION.01", "E2",
        "the identification M_0 = I - H as the moment matrix of the "
        "signed comb measure nu = mu_+ - mu_- (two-route ward "
        "4.9e-13, lam_min(M_0) = tau)",
        "the Lukacs/Gram completion with W >= 0 fails on EVERY rung "
        "at the x = +1 edge where the comb nodes accumulate, with "
        "violation magnitude outrunning the wall margin "
        "(|floor|/tau to -152): no source-only Gram representation "
        "exists at matched degree",
        "GRAM-COMPLETION-FAILS", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/wall_gram_radau_probe.py"),
    Row("directional Loewner floor model D for B",
        "PRIME.PORT.PG.SCHUR.01", "E2",
        "the Loewner step q <= qbar holds EXACTLY, with the whole "
        "construction exact-rationally certified (c_dom bisection "
        "39/39, D PD 39/39, B - D PD 39/39, no D-FAIL)",
        "the loss qbar/q is med 91.3, max 408 on 38/39: D is an "
        "excellent FLOOR model and a catastrophic INVERSE model along "
        "b -- D^-1 inflates exactly the components B^-1 suppresses",
        "PGSCHUR-MEASURED", "NOT-APPLICABLE", "UNTESTED", (),
        "verification/v906_tail_cartography.py"),
    Row("pointwise tail sign and its repair set",
        "PRIME.PORT.TAILSIGN.01 / .02", "E2",
        "two exact tail bookkeepings (1.9e-13) and the located seat: "
        "the entire h-decay of the wall margin lives in the "
        "sign-measured atom tail",
        "the sign is NET, not pointwise (dead 67/67), and the "
        "pointwise repair has no small exception set: the repair "
        "support is diffuse (k_90 med 646) and grows like X^0.89",
        "MECH-NET-ONLY", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/tail_sign_mechanism_probe.py"),
    Row("cumulative / Abel transport of the tail",
        "PRIME.PORT.TAIL.ABEL.01", "E2",
        "the Abel transport to the integer lattice EXACT (chain order "
        "1..3 at 8.9e-16, lattice tie 9.7e-15) with the arithmetic "
        "identity of the cumulants named and warded",
        "five orders too weak, dead 67/67: no order r <= 3 fixes the "
        "dual-kernel sign and the honest all-integer envelope misses "
        "by a gap law e^{+1.744 alpha}, while the true remainder is "
        "~1e+04 mu1 units -- the hole is OSCILLATION, not constants",
        "TAILABEL-MEASURED", "NOT-APPLICABLE", "UNTESTED", (),
        "verification/v906_tail_cartography.py"),
    Row("segment split at classical breakpoints",
        "PRIME.PORT.TAIL.SEGSPLIT.01", "E2",
        "the telescoped segment identity EXACT on 67/67 (3.5e-16)",
        "THE ANCHOR PRICE: every Chebyshev-class envelope pays the "
        "deep anchor at every point of a segment, so the segment "
        "route is COSTLIER than global -- gain < 1 on 67/67",
        "SEGSPLIT-MEASURED", "NOT-APPLICABLE", "SEPARATES",
        ("SMOOTH",),
        "verification/v906_tail_cartography.py"),
    Row("Brun-Titchmarsh / Selberg-class difference envelope",
        "PRIME.PORT.TAIL.DIFFENV.01", "E2",
        "the object the segment split named as missing, built",
        "the deployed BT/monotonicity difference forms beat the "
        "absolute form by only ~1% (gain med 1.010); on window "
        "lengths ~ segment span every classical one-increment "
        "envelope is too wide -- what is missing is CANCELLATION "
        "ACROSS the window",
        "DIFFENV-INSUFFICIENT", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/tail_difference_envelope_probe.py"),
    Row("finite harmonic certificate on the 12 oscillation bins",
        "PRIME.PORT.TAIL.HARMONIC.01", "E2",
        "the oscillation carriers localized: the tail pairing lives "
        "on ~3 low-frequency window harmonics (j* in {1,2,3} on "
        "67/67), measurably BELOW gamma_1 = 14.13 (med distance "
        "13.17 against a uniform null ~1)",
        "dead 67/67 -- the harmonic route is ~7x COSTLIER than direct "
        "at identical envelope, and the entire exponent gain "
        "(+1.74 -> +1.45) comes from the envelope class and accrues "
        "to the direct route equally; the 12-bin reduction carries "
        "the FULL margin decay (-1.042): dimension reduced, "
        "difficulty conserved",
        "HARMCERT-INSUFFICIENT", "DISGUISE", "UNTESTED", (),
        "experiments/tfpt-discovery/finite_harmonic_certificate_probe.py"),
    Row("Krylov / Gauss-Radau moment defect correction, full frame",
        "PRIME.PORT.KRYLOV.KSTAR.01", "E2",
        "Gauss-Radau brackets exact and optimal, med k* = 3 on the "
        "small frame",
        "UNBOUNDED on the full frame: k* grows like h^0.80 (R^2 "
        "0.77), organized by the b-scale k* ~ 37 log(|b|/tau) (R^2 "
        "0.859) with |b|/tau itself ~ h -- the med-k* = 3 of the "
        "small frame was the FRAME SIZE, not a theorem signal",
        "GRAMRADAU-MEASURED", "DISGUISE", "UNTESTED", (),
        "experiments/tfpt-discovery/wall_gram_radau_probe.py"),
    Row("source-only two-moment effective rank (rank-trace)",
        "PRIME.ANTHROPIC.RANKTRACE.01", "E2",
        "an exact dictionary from the end-form into the "
        "moment/inertia currency, machine-verified as an identity on "
        "both frozen surfaces",
        "dead 0/39 + 0/27 blind: the spread deficit 7 f_0 - t_0^2 "
        "(med 2.7e+05) crushes the drive on every step, and qhat/q "
        "med 91.3 is VERBATIM the Loewner table -- the same "
        "D^-1-inflation seat in the effective-rank metric.  Confirms "
        "the adopted two-moment no-go inside this geometry",
        "ANTHRORANKTRACE-MEASURED", "DISGUISE", "UNTESTED", (),
        "experiments/tfpt-discovery/anthropic_ranktrace_core_probe.py"),
    Row("one-bad-mode moment certificate (Chebyshev separator)",
        "PRIME.ONEBADMODE.MOMENTS.01", "E2",
        "a congruence-free, integer-exact certificate closing the "
        "combined ladder 68/68 with a measured h-FLAT order price "
        "r* = 0.544 sqrt(lam_max/c_B)",
        "DISGUISE-MIXED: r* is h-flat but the certificate still "
        "consumes the wall's own spectral width; what it lacks for "
        "all-h is a source-only control of the global spectral width "
        "or of the eight fixed phase values -- the same arithmetic "
        "supply as everything else",
        "DISGUISE-MIXED", "DISGUISE", "UNTESTED", (),
        "experiments/tfpt-discovery/onebadmode_moments_probe.py"),
    Row("Garding minorant M_h >= P_h >= 0 with geometric minorant",
        "PRIME.GARDING.MINORANT.01", "E2",
        "the minorant exists THREEFOLD on the full 8x8 wall",
        "the minorant CLOSES the surface but RELOCATED: it is a "
        "rewriting of the wall's own premise and supplies no "
        "certificate content the direct route does not already have "
        "(recorded in next.txt as NO-NEW-CERTIFICATE-CONTENT); width "
        "refusals on the certified tier",
        "MINORANT-SURFACE-CLOSED-RELOCATED", "DISGUISE", "UNTESTED", (),
        "experiments/tfpt-discovery/garding_minorant_probe.py"),
    Row("Pick / one-bad-atom compression",
        "PRIME.PICK.DUAL.01", "E2",
        "a rational Sturm dual for the bad-atom extremal",
        "PICK-DEAD: the dual encloses a NEGATIVE bad-atom extremal "
        "with Phi = 2.117 >= 1, and the mechanism is a symbolically "
        "exact 2 eps / y^2 high-pole blindness lemma -- the Pick data "
        "cannot see high poles at the required order",
        "PICK-DEAD", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/pick_dual_probe.py"),
    Row("finite-gap reference route (Damanik-Killip-Simon class)",
        "PRIME.FINITEGAP.REFERENCE.01", "E2",
        "the finite-gap class object attempted for the wall",
        "FINITEGAP-ILLDEFINED: the wall's spectral gap set is "
        "SCATTERED, not banded, so the finite-gap class object does "
        "not exist for it",
        "FINITEGAP-ILLDEFINED", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/finitegap_reference_probe.py"),
    Row("Euler-Clark model (Cauchy shape + master relation)",
        "PRIME.EULER.CLARK.01", "E2",
        "the Clark/coisometry model built on the wall block",
        "EC-DEAD: the Cauchy shape is free, the master relation is "
        "sign-indefinite on 42/42, the coisometry defect EQUALS the "
        "Clark residual (so it is one object, not two), and the gate "
        "family is comb-blind",
        "EC-DEAD", "DISGUISE", "WALL-BLIND",
        ("SMOOTH", "SCRAMBLE-ARITH"),
        "experiments/tfpt-discovery/euler_clark_test_probe.py"),
    Row("Krein/Pick index census on the constructed Euler phase",
        "PRIME.KREIN.INDEX.CENSUS.01", "E2",
        "the Euler phase constructed EXACTLY (an identity surviving "
        "all five falsifying control worlds)",
        "WALLPAPER: the negative index is proportional to the "
        "resolution, the half-gap shift removes no negative "
        "direction, and the cosh control world shares truth's FULL "
        "index signature -- index-type functionals are dead, and the "
        "constructed phase is a coordinate change",
        "WALLPAPER", "DISGUISE", "WALL-BLIND",
        ("SMOOTH", "SCRAMBLE-ARITH", "EPSTEIN"),
        "experiments/tfpt-discovery/krein_index_census_probe.py"),
    Row("exterior-square factorization of the wall block",
        "PRIME.EXTERIOR.SQUARE.01", "E2",
        "the Lorentz signature of the block EXPLAINED and the "
        "factorization skeleton built",
        "PARTIAL, then REFUSED: the factorization exists as structure "
        "and supplies no positivity for the deployed object -- the "
        "half-gap read on the exterior side is refused",
        "EXTERIOR-HALFGAP-REFUSED", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/next.txt"),
    Row("deep-membership limit of the class geometry",
        "PRIME.DEEP.MEMBERSHIP.01", "E2",
        "a genuine limit STRUCTURE: g_k = log10(nu_k / n^{k+2}) is "
        "linear in k at R^2 0.99989 (slope +3.102 +- 0.025), so the "
        "deep moment sequence is a one-atom form",
        "DEEP-MEMBERSHIP-BREACH: the MAGNITUDES are not geometric "
        "objects -- all three carriers of the exact split "
        "S = S_AR + S_SM + S_OSC grow like h^2 (slopes "
        "+2.05/+2.12/+1.99, R^2 0.95-0.96) with the partial sums not "
        "even PD; what converges is exclusively the scale-invariant "
        "FORM",
        "DEEP-MEMBERSHIP-BREACH", "DISGUISE", "UNTESTED", (),
        "experiments/tfpt-discovery/deep_membership_limit_probe.py"),
    Row("sigma edge growth beyond the registration edge",
        "PRIME.SIGMA.EDGE.GROWTH.01", "E2",
        "the registered sigma envelope 0.780917 holding blind on all "
        "111 edge steps",
        "EDGE-NONMONOTONE: the measured wall-legal sigma maximum "
        "0.709925 sits at h = 1359, BEFORE the registration edge, and "
        "the deep envelope then falls -- the edge is not a monotone "
        "trend, so no edge extrapolation carries",
        "EDGE-NONMONOTONE", "NOT-APPLICABLE", "SEPARATES",
        ("SMOOTH",),
        "experiments/tfpt-discovery/sigma_edge_growth_probe.py"),
    # ---- OFF-CHAIN: seam / compiler lane, listed to be excluded -----
    Row("seam wiring Groebner census (is pure-I compiler-forced?)",
        "SEAM.STATE.WIRING.SELECTOR.01", OFF_CHAIN,
        "an exact Groebner census: the C6-equivariant commutant is "
        "EXACTLY 24-dimensional and the IOTA rule subspace 8-dim",
        "WIRING-DEGENERATE: the constraint system is degenerate and "
        "the answer is deployment-choice, not compiler theorem -- a "
        "COMPILER/SEAM statement that attacks no edge of the RH DAG",
        "WIRING-DEGENERATE", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/seam_wiring_groebner_probe.py"),
    Row("theta_S collar frame selector",
        "SEAM.STATE.WIRING.SELECTOR.01", OFF_CHAIN,
        "an equivariant selector with an exact selection map; the "
        "deployed pure-I passes the strict collar RP exactly in the "
        "conjugated integer frame",
        "THETA-CONVENTIONAL: no compiler demand pins the theta_S "
        "frame -- five demand classes all COMPATIBLE or "
        "SILENT-ON-ANGLE.  A COMPILER/SEAM statement that attacks no "
        "edge of the RH DAG",
        "THETA-CONVENTIONAL", "NOT-APPLICABLE", "UNTESTED", (),
        "experiments/tfpt-discovery/theta_frame_selector_probe.py"),
)

# --------------------------------------------- candidate sign sources
# every object in the corpus that was offered as an INDEPENDENT SIGN
# SOURCE for the open edge, verdicted against the frozen gate rule R2
Cand = namedtuple("Cand", "name gate reason")

SIGN_SOURCE_GATE = (
    Cand("multiplicativity (Selberg identity, Moebius/Dirichlet)",
         "FAIL",
         "separates all three worlds STRICTLY, but its positive "
         "defect energy is ZERO on truth -- it discriminates without "
         "orienting"),
    Cand("Selberg's symmetry formula as a delivery bound", "FAIL",
         "world-discriminating and a structurally perfect fit, yet "
         "the delivery misses by 1.60e+04 (min) / 9.09e+05 (median); "
         "and A_err - B_err = P_err closes the whole "
         "rewrite-then-estimate class"),
    Cand("every magnitude hypothesis |psi(x) - x| <= f(x) sqrt(x)",
         "FAIL",
         "the conversion constant is ||K_D'||_1 = 4 uniformly in D, "
         "so Littlewood's Omega-theorem empties the class: floor "
         "4 log log log N_h vs slack, ratio 214.7 (own conservative) "
         "and 1527.1 (deployed)"),
    Cand("zero-density inputs N(sigma, T) << T^{A(1-sigma)}", "FAIL",
         "empty for A > 2; A = 2 and Lindeloef land exactly critical "
         "with zero slack"),
    Cand("Vinogradov-Korobov (with or without RH strength)", "FAIL",
         "after the n^{-1/2} weight the range is N^{1/2-o(1)} = "
         "exp((1-o(1)) alpha) against O(1) wall scale; RH strength "
         "removes the N-power but supplies polylogarithmic SIZE "
         "WITHOUT A SIGN"),
    Cand("the Euler grouping / G2 parameter-free weight law", "UNTESTED",
         "the one measured world-discriminating candidate; its "
         "analytic consequences are the open collaboration question"),
    Cand("the F4 signed correlation = Weil's PRIME(F)", "FAIL",
         "the only candidate that is SIGNED and separates SMOOTH-"
         "SOURCE by 4.17/4.49/4.37 orders in the right direction -- "
         "but the resulting bar is NEGATIVE, so the statement is the "
         "OPPOSITE of Weil positivity and reduces to the POSITION of "
         "the ordinates against the sign pattern of Fhat: alignment, "
         "which no size-class bound supplies"),
    Cand("the matrix-stage conditioning gain", "FAIL",
         "the source factorization is an ALGEBRAIC identity holding "
         "in both control worlds at 2.22e-16 -- comb-blind, so it can "
         "only shrink the demand the missing lemma must beat"),
    Cand("kappa = 1 coupling/coisometry scalar", "FAIL",
         "definitional: survives purely random densities on 3/3 "
         "worlds at residual <= 1e-15, zero arithmetic content"),
    Cand("the Krein source contractor (Loewner certificate)",
         "UNTESTED",
         "admissible ONLY if supplied source-side; a target-computed "
         "C is circular by the module's own typed warning "
         "(KreinDefect.lean)"),
    Cand("Beurling-Nyman / Baez-Duarte Gram floor", "FAIL",
         "no N-uniform floor exists (cap 0.420220 < needed 0.5523) "
         "and the certificate class is provably non-implying"),
    Cand("de Branges / Hermite-Biehler chain", "FAIL",
         "a symbolic identity valid in every arithmetic world -- "
         "comb-blind, hence non-discriminating"),
    Cand("Li-Keiper lambda_n positivity on a cofinal index set",
         "FAIL",
         "cofinal/thin index relaxation is REFUTED (Bohr recurrence, "
         "explicit off-line counterexample), and the residual order "
         "bound sits exactly on the RH-equivalence boundary"),
    Cand("an optimal test window", "FAIL",
         "every window that closes the budget is COMB-BLIND; the "
         "optimal admissible window still leaves 1.75/1.77 orders"),
    Cand("more verified zeros", "FAIL",
         "D(H(T))/T = 0.098 and falling; T_req ~ h^2.8 outruns the "
         "spectral window reach"),
    Cand("unconditional statements about ordinate POSITIONS", "UNTESTED",
         "v913 U1/O1: explicitly NOT excluded, and the remaining "
         "statement IS of this kind"),
    Cand("alignment statements (ordinates vs sign pattern of Fhat)",
         "UNTESTED",
         "v913 U2/O2: the no-go forbids only bounds inside I_cone, so "
         "alignment statements are untouched and are exactly what is "
         "needed"),
    Cand("a new GLOBAL inequality restricting the source profile "
         "beyond {w >= 0, size, support}", "UNTESTED",
         "v913 U5/O5: changes I_cone and escapes the S5 class -- the "
         "missing theorem would be exactly this condition"),
)


# --------------------------------------------------------------- utils
def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % (tag, name, ("  -- " + detail) if detail else ""))
    if not ok:
        FAILS.append(name.split()[0])
    return bool(ok)


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def read(relpath):
    return (ROOT / relpath).read_text(encoding="utf-8", errors="replace")


def exists(relpath):
    return os.path.exists(str(ROOT / relpath))


def topo_order(edges):
    """Kahn on the CONJUNCTIVE hypergraph: an edge fires only when ALL
    of its sources are placed, and a node is placed only when ALL of
    its incoming edges have fired.  Returns (node_order, edge_order),
    or (None, None) if a cycle blocks the fixpoint."""
    incoming = {n: [e for e in edges if e.dst == n] for n in NODES}
    placed = [n for n in sorted(NODES) if not incoming[n]]
    order, fired = list(placed), []
    placed, fired_ids = set(placed), set()
    changed = True
    while changed:
        changed = False
        for e in edges:                       # declaration order = ties
            if e.eid in fired_ids:
                continue
            if all(s in placed for s in e.src):
                fired.append(e.eid)
                fired_ids.add(e.eid)
                changed = True
        for n in sorted(NODES):
            if n in placed or not incoming[n]:
                continue
            if all(e.eid in fired_ids for e in incoming[n]):
                placed.add(n)
                order.append(n)
                changed = True
    if len(order) != len(NODES) or len(fired) != len(edges):
        return None, None
    return order, fired


def main():
    print("kill_atlas_dag_probe -- PRIME.AUDIT.KILLATLAS.01: the typed "
          "RH implication DAG and the campaign kill atlas, as one "
          "contradictable object (note CCCLXXVI).  NO RH CLAIM.")

    # ================================================== D -- the DAG
    section("D -- THE IMPLICATION DAG (shape, typing, artifacts)")

    eids = [e.eid for e in DAG_EDGES]
    check("D0.1 edge ids unique", len(eids) == len(set(eids)),
          "%d edges" % len(eids))
    ok = all(e.etype in EDGE_TYPES for e in DAG_EDGES)
    ok &= all(e.dst in NODES for e in DAG_EDGES)
    ok &= all(s in NODES for e in DAG_EDGES for s in e.src)
    check("D0.2 every edge type in the frozen vocabulary and every "
          "endpoint a declared node", ok,
          "%d nodes, types %s" % (len(NODES), "/".join(EDGE_TYPES[:5])))

    node_order, edge_order = topo_order(DAG_EDGES)
    check("D1 THE DAG IS ACYCLIC (Kahn on the conjunctive node graph)",
          node_order is not None,
          "node order %s" % (" -> ".join(node_order) if node_order
                             else "CYCLE"))
    if node_order is None:
        print("\nSPEC ERROR: cyclic DAG, remaining gates skipped.")
        return 1

    # reachability from SRC, and RH reachable
    reach = {ROOT_NODE}
    grew = True
    while grew:
        grew = False
        for e in DAG_EDGES:
            if e.dst not in reach and all(s in reach for s in e.src):
                reach.add(e.dst)
                grew = True
    check("D2.1 EVERY NODE REACHABLE from %s" % ROOT_NODE,
          reach == set(NODES),
          "unreached %s" % (sorted(set(NODES) - reach) or "none"))
    check("D2.2 %s reachable (the chain closes)" % SINK_NODE,
          SINK_NODE in reach)
    sinks = {e.dst for e in DAG_EDGES}
    orphan = [n for n in NODES
              if n != ROOT_NODE and n not in sinks]
    check("D2.3 no orphan node (every non-root node is some edge's "
          "target)", not orphan, "orphans %s" % (orphan or "none"))

    # artifacts on disk for every PROVEN / CERTIFIED-FINITE edge
    hard = [e for e in DAG_EDGES
            if e.etype in ("PROVEN", "CERTIFIED-FINITE")]
    missing = [(e.eid, a) for e in hard for a in e.artifacts
               if not exists(a)]
    check("D3.1 every PROVEN/CERTIFIED-FINITE edge cites artifacts "
          "that EXIST on disk", not missing,
          "%d edges, %d paths, missing %s"
          % (len(hard), sum(len(e.artifacts) for e in hard),
             missing or "none"))
    empty = [e.eid for e in hard if not e.artifacts]
    check("D3.2 no PROVEN/CERTIFIED-FINITE edge is artifact-free",
          not empty, "artifact-free %s" % (empty or "none"))
    check("D3.3 the OPEN edge cites NOTHING (nothing establishes it)",
          all(not e.artifacts and not e.theorem
              for e in DAG_EDGES if e.etype == "OPEN"))

    # every cited verification/vN_*.py is a ledger-carried module
    ledger_blob = read(LEDGER)
    vmods = sorted({os.path.basename(a)
                    for e in DAG_EDGES for a in e.artifacts
                    if a.startswith("verification/v")
                    and a.endswith(".py")})
    absent = [m for m in vmods if m not in ledger_blob]
    check("D3.4 every cited verification/vN_*.py appears in "
          "status_ledger.csv", not absent,
          "%d modules cited, absent %s" % (len(vmods), absent or "none"))

    # the OPEN set and its topological position
    open_e = [eid for eid in edge_order
              if next(e for e in DAG_EDGES if e.eid == eid).etype
              == "OPEN"]
    check("D4.1 the OPEN edge set is NON-EMPTY", bool(open_e),
          "open %s" % open_e)
    check("D4.2 THE FIRST OPEN EDGE IN TOPOLOGICAL ORDER IS %s"
          % FIRST_OPEN_EDGE,
          bool(open_e) and open_e[0] == FIRST_OPEN_EDGE,
          "topological edge order %s" % " ".join(edge_order))
    nonproven = tuple(eid for eid in edge_order
                      if next(e for e in DAG_EDGES if e.eid == eid).etype
                      != "PROVEN")
    check("D4.3 the NON-PROVEN list in topological order is exactly "
          "%s -- so %s is the first OPEN edge but NOT the only "
          "non-PROVEN edge"
          % ("/".join(NON_PROVEN_EXPECTED), FIRST_OPEN_EDGE),
          nonproven == NON_PROVEN_EXPECTED,
          "measured %s" % "/".join(nonproven))
    check("D4.4 no edge is typed MEASURED (Rule 3: a MEASURED edge "
          "would be a chain gap silently typed as progress)",
          not [e.eid for e in DAG_EDGES if e.etype == "MEASURED"])

    # circularity: no edge lists its own target among its sources
    self_consuming = [e.eid for e in DAG_EDGES if e.dst in e.src]
    check("D5.1 no edge consumes its own conclusion as a source",
          not self_consuming, "self-consuming %s"
          % (self_consuming or "none"))
    flagged = {e.eid: e.consumes for e in DAG_EDGES if e.consumes}
    check("D5.2 THE CIRCULARITY LEDGER IS CARRIED AS DATA: E2 is the "
          "ONLY edge that consumes its own conclusion through a "
          "selection gate, and it declares it",
          set(flagged) == {"E2"}
          and any("X1" in c for c in flagged["E2"])
          and any("X5" in c for c in flagged["E2"]),
          "edges with declared consumption: %s" % sorted(flagged))
    check("D5.3 the PROVEN edges consume nothing (no source-only "
          "quantity reads forward sign, zero data or a target vector)",
          all(not e.consumes for e in DAG_EDGES
              if e.etype == "PROVEN"))

    print("\n  topological node order:")
    print("    " + " -> ".join(node_order))
    print("  topological edge order with types:")
    for eid in edge_order:
        e = next(x for x in DAG_EDGES if x.eid == eid)
        print("    %-4s %-18s %-16s %s"
              % (e.eid, "+".join(e.src) + " -> " + e.dst, e.etype,
                 (e.theorem or "--")[:60]))

    # ================================================ A -- the atlas
    section("A -- THE KILL ATLAS (well-formedness and attribution)")

    check("A0.1 atlas non-empty and route names unique",
          len(ATLAS) > 0
          and len({r.route for r in ATLAS}) == len(ATLAS),
          "%d rows" % len(ATLAS))
    bad_tau = [r.route for r in ATLAS if r.tau not in TAU_SCREEN]
    bad_ctrl = [r.route for r in ATLAS if r.ctrl not in CTRL_SCREEN]
    bad_world = [(r.route, w) for r in ATLAS for w in r.worlds
                 if w not in CONTROL_WORLDS]
    check("A0.2 every tau-screen / control-screen / control-world "
          "value in the frozen vocabulary",
          not bad_tau and not bad_ctrl and not bad_world,
          "bad tau %s, bad ctrl %s, bad world %s"
          % (bad_tau or 0, bad_ctrl or 0, bad_world or 0))

    # exactly one DAG edge per killed route
    eidset = set(eids)
    multi = [r.route for r in ATLAS
             if not isinstance(r.edge, str) or " " in r.edge.strip()]
    unknown = [(r.route, r.edge) for r in ATLAS
               if r.edge not in eidset and r.edge != OFF_CHAIN]
    check("A1.1 EVERY KILLED ROUTE MAPS TO EXACTLY ONE DAG EDGE "
          "(single edge id, no compound attribution)",
          not multi and not unknown,
          "compound %s, unknown %s" % (multi or 0, unknown or 0))
    offchain = [r.route for r in ATLAS if r.edge == OFF_CHAIN]
    check("A1.2 the OFF-CHAIN rows are exactly the two seam/compiler "
          "results (WIRING-DEGENERATE, THETA-CONVENTIONAL) -- they "
          "attack no edge of this DAG",
          len(offchain) == 2
          and {r.verdict for r in ATLAS if r.edge == OFF_CHAIN}
          == {"WIRING-DEGENERATE", "THETA-CONVENTIONAL"},
          "off-chain %s" % offchain)
    on_open = [r.route for r in ATLAS if r.edge == FIRST_OPEN_EDGE]
    check("A1.3 the OPEN edge %s carries the largest single block of "
          "kills" % FIRST_OPEN_EDGE,
          len(on_open) >= 10, "%d routes at %s"
          % (len(on_open), FIRST_OPEN_EDGE))

    # every atlas artifact exists, and the verdict enum occurs in it
    miss_art = [(r.route, r.artifact) for r in ATLAS
                if not exists(r.artifact)]
    check("A2.1 every atlas row cites an artifact that EXISTS on disk",
          not miss_art, "missing %s" % (miss_art or "none"))
    absent_verdict = []
    for r in ATLAS:
        if not exists(r.artifact):
            continue
        if r.verdict not in read(r.artifact):
            absent_verdict.append((r.verdict,
                                   os.path.basename(r.artifact)))
    check("A2.2 every atlas VERDICT ENUM literally occurs in its own "
          "cited artifact (earned by grep, not by trust)",
          not absent_verdict, "absent %s" % (absent_verdict or "none"))

    # Rule 1 bookkeeping: DISGUISE rows must not be sold as advances
    disguise = [r.route for r in ATLAS if r.tau == "DISGUISE"]
    advance = [r.route for r in ATLAS if r.tau == "ADVANCE"]
    check("A3.1 the tau-screen classified at least ten routes as "
          "DISGUISE (Rule 1 bites across the campaign)",
          len(disguise) >= 10, "%d DISGUISE, %d ADVANCE"
          % (len(disguise), len(advance)))
    check("A3.2 NO route typed ADVANCE lands on the OPEN edge -- i.e. "
          "not one tau-screen advance touches the missing inequality",
          not [r for r in ATLAS
               if r.tau == "ADVANCE" and r.edge == FIRST_OPEN_EDGE],
          "advances: %s" % (advance or "none"))
    # Rule 2 bookkeeping
    blind = [r.route for r in ATLAS if r.ctrl == "WALL-BLIND"]
    sep = [r.route for r in ATLAS if r.ctrl == "SEPARATES"]
    untested = [r.route for r in ATLAS if r.ctrl == "UNTESTED"]
    check("A3.3 the control screen was RUN on a majority of rows and "
          "every world named is one of Epstein/Scramble/Smooth",
          len(sep) + len(blind) > len(untested) // 2,
          "%d SEPARATES, %d WALL-BLIND, %d UNTESTED"
          % (len(sep), len(blind), len(untested)))

    # ================================== S -- the frozen gate sweep
    section("S -- THE FROZEN GATE RULE ON EVERY CANDIDATE SIGN SOURCE")

    ok = all(c.gate in ("PASS", "FAIL", "UNTESTED")
             for c in SIGN_SOURCE_GATE)
    check("S1.1 every candidate sign source carries a frozen gate "
          "verdict in {PASS, FAIL, UNTESTED}", ok,
          "%d candidates" % len(SIGN_SOURCE_GATE))
    passes = [c.name for c in SIGN_SOURCE_GATE if c.gate == "PASS"]
    fails = [c.name for c in SIGN_SOURCE_GATE if c.gate == "FAIL"]
    unt = [c.name for c in SIGN_SOURCE_GATE if c.gate == "UNTESTED"]
    check("S1.2 NOT ONE CANDIDATE SIGN SOURCE PASSES THE FROZEN GATE",
          not passes, "%d FAIL, %d UNTESTED, %d PASS"
          % (len(fails), len(unt), len(passes)))
    check("S1.3 the UNTESTED residue is exactly the class v913 leaves "
          "open (positions / alignment / a new global source-profile "
          "constraint) plus the two named live candidates",
          len(unt) == 5,
          "untested: %s" % "; ".join(u[:44] for u in unt))
    for c in SIGN_SOURCE_GATE:
        print("    %-8s %s" % (c.gate, c.name))

    # ============================================ N -- number wards
    section("N -- LOAD-BEARING NUMBER WARDS (re-derived or re-grepped)")

    # N1 the Schur equivalence, exact over Q on explicit data
    ok = True
    for (n, b, B) in (
        (Fraction(7, 3), (Fraction(1, 2), Fraction(-1, 5)),
         ((Fraction(3), Fraction(1, 4)), (Fraction(1, 4), Fraction(2)))),
        (Fraction(1, 10), (Fraction(3, 7), Fraction(2, 9)),
         ((Fraction(5, 2), Fraction(-1, 3)),
          (Fraction(-1, 3), Fraction(4, 3)))),
    ):
        detB = B[0][0] * B[1][1] - B[0][1] * B[1][0]
        inv = ((B[1][1] / detB, -B[0][1] / detB),
               (-B[1][0] / detB, B[0][0] / detB))
        q = sum(b[i] * inv[i][j] * b[j] for i in (0, 1) for j in (0, 1))
        M = ((n, b[0], b[1]),
             (b[0], B[0][0], B[0][1]),
             (b[1], B[1][0], B[1][1]))
        detM = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        ok &= (detM == (n - q) * detB)                 # E3 identity
        ok &= (Fraction(1) - (n - q) / n == q / n)     # sigma = 1 - s/n
    check("N1 E3 exact over Q: det M == (n - q) det B, and "
          "sigma = q/n == 1 - s/n (the CCLXV identity that makes "
          "every sigma cap a restatement)", ok)

    # N2 the tau-screen bands are the frozen ones
    pb = read("experiments/tfpt-discovery/port_bfloor_uniformity_probe.py")
    ok = ("SLOPE_PASS = 0.30" in pb) and ("-0.247" in pb)
    ok &= "PASS |s| <= 0.30 / RELOCATION s >= 0.70" in ledger_blob
    check("N2 the tau-screen bands are frozen a priori (SLOPE_PASS "
          "0.30 / RELOCATION 0.70) and the B-floor screen reads "
          "slope -0.247", ok,
          "bands %.2f / %.2f" % (SLOPE_PASS, SLOPE_RELOC))

    # N3 the B-floor currency ordering (guards the C-4 zoo)
    c_interval, c_exact, c_measured = 0.5523, 0.5914, 0.679
    ok = c_interval < c_exact < c_measured
    ok &= "min c_B = 0.5523" in ledger_blob
    ok &= "0.5914" in ledger_blob
    check("N3 B-floor currency ordering interval-ideal 0.5523 < "
          "exact-rational-float 0.5914 < measured lam_min 0.679, and "
          "the ledger carries the interval tier as the composed one",
          ok)

    # N4 the half-gap window provenance, exact trig identity
    ok = True
    for h in (142, 199, 997, 1433, 2854, 12632):
        N = 2 * h + 1
        mu1 = 4.0 * math.sin(math.pi / N) ** 2
        ok &= abs(0.5 * mu1 - (1.0 - math.cos(2.0 * math.pi / N))) < 1e-15
    check("N4 the 1/2 of the registered target is WINDOW provenance: "
          "(1/2) mu1(h) == 1 - cos(2 pi / N), N = 2h + 1", ok)

    # N5 the F4 exponent ladder, and that 2.119 was not a floor
    # (the exponents are computed at runtime by the probe, so the
    # literals live in the note that recorded them: CCCLXXII)
    notes = read("experiments/next.txt")
    ok = ("0.847" in notes) and ("0.863" in notes)
    ok &= ("2.119" in notes) and ("8.969" in notes) and ("6.103" in notes)
    ok &= (0.847 < 2.119) and (0.863 > 0.0)
    check("N5 F4 exponent ladder: the deployed demand exponent 8.969 "
          "-> 6.103 (F4 coordinates) -> 2.119 -> 0.847, and 2.119 was "
          "NOT a floor -- but the certified cone floor exponent 0.863 "
          "> 0, so the growth is not pressable to zero", ok)

    # N6 the Littlewood emptiness ratios (v913 gate S2.8-S2.10)
    v913 = read("verification/v913_signed_alignment_localization.py")
    ok = all(t in v913 for t in ("214.7", "1527.1", "4.1231791",
                                 "2.1654551"))
    ok &= (4.1231791 > 2.1654551)          # floor grows with depth
    check("N6 the magnitude class is UNCONDITIONALLY empty: Littlewood "
          "floor 4 log log log N_h >= 2.1654551 at h = 184 and >= "
          "4.1231791 at h = 12632, ratio 214.7 (own conservative "
          "slack) / 1527.1 (deployed)", ok)

    # N7 the mesh-order counterexample floors
    ok = ("-2.114e-03" in ledger_blob) and ("-2.128e-04" in ledger_blob)
    ok &= "mesh-refinement order" in read(
        "verification/v848_extraction_chain.py")
    check("N7 the mesh-order qualifier is load-bearing, not cosmetic: "
          "a window-only-cofinal ladder yields false floors "
          "-2.114e-03 at D0 = 1/32 and -2.128e-04 at D0 = 1/128, and "
          "v848 carries the qualifier", ok)

    # N8 NO-WITNESS: the deepest certified read and the flattening
    ok = ("2.79579794131272506e-15" in v913)
    ok &= ("-3.21092510922176011" in v913) and ("0.50302892" in v913)
    ok &= (-2.67942161 > -3.21092511)     # deep exponent is FLATTER
    check("N8 counter-evidence carried unsmoothed: deepest certified "
          "read 2.79579794131272506e-15 at h = 12632 (0 negatives, 0 "
          "straddles) and the n0-normalized decay FLATTENS "
          "(-3.2109 global vs -2.6794 deepest step), one re-derived "
          "step positive +0.50302892 vs collapse bar -8.0", ok)

    # N9 v912 is the SECOND edge closed, and it names the first
    v912 = read("verification/v912_form_convergence_theorem.py")
    ok = ('EXPECTED = "FORMCONV-PROVEN"' in v912)
    ok &= ("NARROWED, not closed" in v912)
    ok &= ("(H_cof)" in v912) and ("RH-hard" in v912)
    check("N9 v912 closes hconv UNCONDITIONALLY (FORMCONV-PROVEN), "
          "explicitly does NOT touch (H_cof), and types the density "
          "leg NARROWED-not-closed -- the corpus itself carries the "
          "correction to 'exactly one unproven inequality'", ok)

    # N10 v913 is a no-go, NOT an advance (correction A1)
    ok = ('EXPECTED = "NOGO-CORE-VERIFIED"' in v913)
    ok &= ("NOT progress" in v913)
    ok &= ("A NO-GO / TYPING ROW AND EXPLICITLY NOT PROGRESS"
           in ledger_blob)
    ok &= ("must NOT be counted as evidence for or against the "
           "Riemann Hypothesis" in ledger_blob)
    nogo = read("experiments/tfpt-discovery/signed_only_nogo_probe.py")
    ok &= ("NOGO-COMPOSITE-VERIFIED" in nogo)
    check("N10 correction A1: the promoted module emits "
          "NOGO-CORE-VERIFIED (the probe's is "
          "NOGO-COMPOSITE-VERIFIED) and BOTH are typed no-go -- the "
          "ledger row is titled verbatim 'A NO-GO / TYPING ROW AND "
          "EXPLICITLY NOT PROGRESS'", ok)

    # N11 the localization is signed AND alignment-carrying
    ok = ("SIGNED" in v913) and ("ALIGNMENT-CARRYING" in v913)
    ok &= ("E1" in v913) and ("E10" in v913)     # ten empty classes
    ok &= ("U1" in v913) and ("U5" in v913)      # five unexplored
    check("N11 the localization's two required properties are named "
          "in the promoted module: any closing input must be SIGNED "
          "(odd under the comb sign flip) AND ALIGNMENT-CARRYING "
          "(ordinates vs the sign pattern of Fhat); ten classes "
          "proven empty, five merely unexplored", ok)

    # N12 the two killing numbers this audit got WRONG on first pass
    # (a verdict enum can be right while the number beside it is
    # invented; A2.2 gates the token, so the numbers need their own
    # ward).  Both re-grepped from the artifact that owns them.
    zwb = read("experiments/tfpt-discovery/zero_window_bootstrap_probe.py")
    ok = ("ratio 8.9e-2" in zwb) and ("ratio 8.0e-5" in zwb)
    ok &= ("0.098" not in zwb)      # the number this audit first wrote
    ok &= ("WARD_FLIP_WORST" in nogo) and ("-4.083267" in nogo)
    msc = read("experiments/tfpt-discovery/"
               "matrix_stage_conditioning_probe.py")
    ok &= ("-4.083267" not in msc)   # it is NOT in the route's probe
    check("N12 killing-number provenance: the bootstrap ratio is "
          "8.9e-02 (lowest anchor) / 8.0e-05 (T0) and 0.098 appears "
          "NOWHERE in that probe; the -4.083267 flip ward belongs to "
          "signed_only_nogo_probe.py, not to "
          "matrix_stage_conditioning_probe.py", ok)

    # N13 the note file carries a DUPLICATE Roman numeral.  Each note
    # is ONE long line, so the numeral must be read from the heading
    # prefix only -- matching anywhere in the line also catches every
    # in-body cross-reference.
    heads = re.findall(r"^# \d{4}-\d{2}-\d{2} \(([IVXLCDM]+)\)",
                       notes, re.M)
    dups = sorted({r for r in heads if heads.count(r) > 1})

    def rom(s):
        vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                "D": 500, "M": 1000}
        tot = 0
        for i, ch in enumerate(s):
            v = vals[ch]
            tot += -v if i + 1 < len(s) and v < vals[s[i + 1]] else v
        return tot

    # the log reuses the low numeral space across TWO series, so a
    # global uniqueness claim is false; scope to the RH campaign
    campaign = [r for r in heads if rom(r) >= 261]
    cdups = sorted({r for r in campaign if campaign.count(r) > 1})
    low = [r for r in dups if rom(r) < 261]
    ok = (cdups == ["CCCLVII"]) and campaign.count("CCCLVII") == 2
    ok &= len(low) >= 40          # the earlier series overlaps broadly
    # this audit's own note exists exactly once (a "newest heading"
    # pin would break on the very next research round -- the log grows)
    ok &= heads.count("CCCLXXVI") == 1
    check("N13 corpus defect carried, not smoothed: across %d note "
          "headings the numeral space is REUSED -- %d low numerals "
          "(I..CII) belong to an earlier series, so numeral-only "
          "citation is globally ambiguous; WITHIN the RH campaign "
          "(>= CCLXI, %d headings) the only duplicate is CCCLVII, "
          "used twice (COFINAL.WEIL formal hardening AND "
          "XI.RESOLVENT.NORMALIZATION)"
          % (len(heads), len(low), len(campaign)),
          ok, "campaign duplicates %s; newest heading %s"
          % (cdups or "none", heads[0] if heads else "NONE"))

    # ==================================================== verdict
    section("VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = len(CHECKS) - n_pass
    print("  checks            %d/%d PASS" % (n_pass, len(CHECKS)))
    print("  DAG               %d nodes, %d edges "
          "(%d PROVEN, %d CERTIFIED-FINITE, %d CITED-CLASSICAL, "
          "%d OPEN)"
          % (len(NODES), len(DAG_EDGES),
             sum(1 for e in DAG_EDGES if e.etype == "PROVEN"),
             sum(1 for e in DAG_EDGES if e.etype == "CERTIFIED-FINITE"),
             sum(1 for e in DAG_EDGES if e.etype == "CITED-CLASSICAL"),
             sum(1 for e in DAG_EDGES if e.etype == "OPEN")))
    print("  atlas             %d routes (%d on the open edge %s, "
          "%d off-chain)"
          % (len(ATLAS), len(on_open), FIRST_OPEN_EDGE, len(offchain)))
    print("  tau-screen        %d DISGUISE, %d ADVANCE, %d "
          "NOT-APPLICABLE"
          % (len(disguise), len(advance),
             sum(1 for r in ATLAS if r.tau == "NOT-APPLICABLE")))
    print("  control screen    %d SEPARATES, %d WALL-BLIND, %d "
          "UNTESTED" % (len(sep), len(blind), len(untested)))
    print("  sign-source gate  %d FAIL, %d UNTESTED, %d PASS"
          % (len(fails), len(unt), len(passes)))
    print("  first open edge   %s  (%s -> %s)"
          % (FIRST_OPEN_EDGE,
             "+".join(next(e for e in DAG_EDGES
                           if e.eid == FIRST_OPEN_EDGE).src),
             next(e for e in DAG_EDGES
                  if e.eid == FIRST_OPEN_EDGE).dst))
    print("  non-PROVEN edges  %s" % "/".join(nonproven))
    print()
    if n_fail == 0:
        print("VERDICT: ATLAS-DAG-CONSISTENT( acyclic, all nodes "
              "reachable, every hard edge artifact-backed and "
              "ledger-carried ) + ONE-OPEN-EDGE-CONFIRMED( the first "
              "non-PROVEN implication is E4, the predefined "
              "mesh-cofinal ladder positivity ) + "
              "FOUR-CLASSICAL-CITATIONS-CARRIED( E7/E8/E9/E10 are "
              "cited, not proven in-corpus -- the 'exactly one "
              "unproven inequality' headline counts inequalities, not "
              "edges ) + NO-SIGN-SOURCE-PASSES( %d candidates, %d "
              "FAIL, %d UNTESTED, 0 PASS ) + "
              "LOCALIZATION-DID-NOT-MOVE-THE-EDGE( six coordinate "
              "systems, one edge; every reformulation typed DISGUISE "
              "by Rule 1 )." % (len(SIGN_SOURCE_GATE), len(fails),
                                len(unt)))
    else:
        print("VERDICT: ATLAS-DAG-INCONSISTENT( %d gate failure(s): "
              "%s )" % (n_fail, ", ".join(FAILS)))
    print("NO RH CLAIM.  SYNTHESIS AUDIT scope; no marker moved; "
          "nothing written outside experiments/.")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
